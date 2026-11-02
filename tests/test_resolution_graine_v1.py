"""Rejeu à graine (`runs_nuit.resolution_graine_v1`), sur processeur.

1. Faits dont dépend la méthode : `torch.multinomial(p, 1, generator=g)` = argmax de p / q, q exponentiels du même
   générateur ; un appel de n × V tirages = n appels de V ; graines des actions dérivées comme `jouer_p3` ;
   `tok.decode` de Llama 3.1 = octets concaténés décodés en UTF-8 avec remplacement.
2. Cas sain : un modèle Llama minuscule à poids aléatoires (vocabulaire de 128 256, graine fixe, enregistré puis relu
   dans un dossier temporaire), le vrai tokeniseur de Llama 3.1 et le format réel (gabarit, date figée, fins de P3) ;
   épisodes joués par le harnais (`jouer_episodes`, par lots, remplissage à gauche, cache), dont on ne garde que les
   textes, les longueurs et les graines ; les identifiants retrouvés sont ceux du harnais, l'empreinte aussi, avec des
   découpages non canoniques (vérifié), des actions arrêtées à `max_nouveaux`, un jeton spécial effacé du texte.
3. Artefacts (R5) : graine fausse, texte altéré d'un octet, contexte décalé d'un jeton → non résolu (jamais un faux
   « résolu ») ; repli itératif : une bascule, deux bascules dans deux actions (la seconde erreur n'apparaît que dans le
   rejeu de la première, VG-02) ; budget de l'épisode épuisé → « non résolu : durée », sans exception (VG-01) ;
   caractère de remplacement : résolu par balayage quand c'est simple, déclaré non résolu au-delà de la borne, seuls les
   balayages complets comptés (VG-07) ; seuil de validation contrôlé avant la boucle.
4. Forme « identifiants » de la table version 3 : cas sain, artefacts ; formes des versions 1 et 2 acceptées telles
   quelles ; table v3 écrite scellée, jamais écrasée (VG-08).
5. Bout en bout en mode jouet sur un P3 jouet joué par le vrai code de P3 (`premier_test_ia.run`) : étape validation (à
   l'aveugle, graines lues dans le manifeste de P3), étape résolution (épisodes non conformes en longueur compris),
   table version 3 revérifiée par l'empreinte ; graines fausses → validation « sous le seuil » rapportée, sans arrêt, et
   la résolution se lance quand même (VG-03) ; échéances en milieu d'étape (épisode, étape) et signal TERM : épisodes
   consignés un à un, résultat ou `arret.json` qui les cite (VG-01).
6. Gardes d'exécution (VG-04 à VG-06) : budget par épisode, noyau d'attention, paires en validation, agent comparé au
   manifeste de P3, réserves d'environnement écrites (CUDA, cuDNN, carte), contrôle croisé lu à trois valeurs.

Le tokeniseur de Llama 3.1 (révision de P3) est lu dans `TOKENISEUR_LLAMA31` (dossier) ou dans le cache local de
Hugging Face ; sans lui, les tests qui en ont besoin sont sautés, avec leur motif (jamais en silence)."""
import hashlib
import json
import os
import random
import re
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.harnais.episode import EnvironnementJouet, empreinte_episode, jouer_episodes
from controle_ia.manifeste import generateur, graines
from controle_ia.runs_nuit import rejeu_activations_v1 as ra
from controle_ia.runs_nuit import resolution_graine_v1 as rg
from controle_ia.runs_nuit import resolution_tokenisation_v1 as rt
from controle_ia.scellement import sceller

from test_premier_test_ia_run import entropie_fixe  # noqa: F401  (fixture réutilisée)
from test_runs_nuit_v1 import RUN_P3, source  # noqa: F401  (fixture réutilisée)
from test_runs_nuit_v2 import _table

RACINE = Path(__file__).resolve().parents[1]
MODELE = "meta-llama/Llama-3.1-8B-Instruct"
REVISION = "0e9e39f249a16976918f6564b8830bc894c89659"
TOKENIZER_JSON_SHA256 = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"
V = 128256
FINS_P3 = {128001, 128008, 128009}
SPECIAL_INVISIBLE = 128010          # <|python_tag|> : spécial, hors des fins ; effacé du texte au décodage
T, B, MAX = 3, 4, 24


def _dossier_tokeniseur():
    d = os.environ.get("TOKENISEUR_LLAMA31")
    if d:
        return Path(d)
    try:
        from huggingface_hub import try_to_load_from_cache

        c = try_to_load_from_cache(MODELE, "tokenizer.json", revision=REVISION)
        return Path(c).parent if isinstance(c, str) else None
    except Exception:
        return None


@pytest.fixture(scope="module")
def tok():
    from transformers import AutoTokenizer

    d = _dossier_tokeniseur()
    if d is None or not (d / "tokenizer.json").exists():
        pytest.skip("tokeniseur de Llama 3.1 introuvable (TOKENISEUR_LLAMA31 ou cache local à la révision de P3)")
    assert hashlib.sha256((d / "tokenizer.json").read_bytes()).hexdigest() == TOKENIZER_JSON_SHA256
    return AutoTokenizer.from_pretrained(str(d))


@pytest.fixture(scope="module")
def fmt(tok):
    from controle_ia.harnais.formats import FormatChat

    f = FormatChat(tok, variables={"date_string": "26 Jul 2024"})
    f.fins = set(FINS_P3)
    assert "Today Date: 26 Jul 2024" in tok.decode(f.ouverture("x", "y"))
    return f


def _modele_minuscule(tok, dossier: Path, avec_octets: bool):
    """Llama minuscule (2 couches, largeur 16), vocabulaire de 128 256, graine fixe ; enregistré puis relu. Tête de
    sortie munie d'un biais fixe qui restreint le tirage à des morceaux de mots (« ab », « Ġcd »…), aux trois fins de
    P3, à un jeton spécial invisible et, sur demande, à quelques octets isolés (é en deux jetons, octets orphelins
    décodés en U+FFFD) : textes lisibles, découpages non canoniques fréquents, contexte influent."""
    from transformers import LlamaConfig, LlamaForCausalLM

    oc, _ = rt.table_des_octets(tok)
    permis = [i for i in range(128000) if re.fullmatch(rb" ?[a-z]{1,3}", oc(i))]
    octets = [i for i in range(128000) if oc(i) in (b"\xc3", b"\xa9", b"\xc3\xa9")] if avec_octets else []
    cfg = LlamaConfig(vocab_size=V, hidden_size=16, intermediate_size=32, num_hidden_layers=2, num_attention_heads=2,
                      num_key_value_heads=1, max_position_embeddings=2048, bos_token_id=128000, eos_token_id=128009,
                      tie_word_embeddings=False, initializer_range=0.3)
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(1)
        m = LlamaForCausalLM(cfg)
    m.save_pretrained(dossier)
    m = LlamaForCausalLM.from_pretrained(dossier, dtype=torch.float32).eval()
    tete = torch.nn.Linear(16, V, bias=True)
    with torch.no_grad():
        tete.weight.copy_(torch.randn(V, 16, generator=torch.Generator().manual_seed(7)) * 0.75)
        b = torch.full((V,), -30.0)
        b[permis] = 0.0
        b[128009], b[128001], b[128008], b[SPECIAL_INVISIBLE] = 7.0, 5.0, 5.0, 7.0
        for i in octets:
            b[i] = 6.0
        tete.bias.copy_(b)
    m.lm_head = tete
    return m.eval()


def _jouer(modele, fmt, graine0: int = 0):
    """Épisodes joués par le harnais ; on ne garde que ce que P3 a stocké : textes, longueurs, graines, empreinte."""
    gr = [{(0, t): 1000 * b + 17 * t + 3 + graine0 for t in range(T)} for b in range(B)]
    sorties = jouer_episodes(modele, fmt, EnvironnementJouet(), [f"e{b}" for b in range(B)], 1, T, gr, [1],
                             max_nouveaux=MAX)
    eps = []
    for b, (ep, acts, _) in enumerate(sorties):
        actions = ep.transcriptions[0].actions
        eps.append({"identifiant": ep.identifiant, "textes": [a.texte for a in actions],
                    "jetons": [len(a.ids) for a in actions],
                    "jetons_notes": [len(a.ids) - (1 if a.ids and a.ids[-1] in fmt.fins else 0) for a in actions],
                    "graines": [gr[b][(0, t)] for t in range(T)], "empreinte": empreinte_episode(ep, acts)["trajectoire"],
                    "ids": [list(a.ids) for a in actions]})
    return eps


@pytest.fixture(scope="module")
def jeu(tok, fmt, tmp_path_factory):
    modele = _modele_minuscule(tok, tmp_path_factory.mktemp("llama-minuscule"), avec_octets=False)
    return modele, _jouer(modele, fmt)


@pytest.fixture(scope="module")
def jeu_octets(tok, fmt, tmp_path_factory):
    modele = _modele_minuscule(tok, tmp_path_factory.mktemp("llama-minuscule-octets"), avec_octets=True)
    return modele, _jouer(modele, fmt)


def _resoudre(modele, tok, fmt, ep, moteur=None, textes=None, graines_=None, **reglages):
    voc = rg.Vocabulaire(tok, fmt.fins, V)
    Qs = [rg.tirages_exponentiels(g, n, V) for g, n in zip(graines_ or ep["graines"], ep["jetons"])]
    reg = rg.Reglages(max_nouveaux=MAX, **{"combinaisons_max": 8, **reglages})
    return rg.resoudre_avec_repli(moteur or rg.Moteur(modele), voc, fmt, EnvironnementJouet, ep["identifiant"], T,
                                  textes or ep["textes"], ep["jetons"], ep["jetons_notes"], Qs, ep["empreinte"], reg)


class MoteurDecale(rg.Moteur):
    """Artefact : chaque position voit son contexte décalé d'un jeton (séquence décalée à droite, premier jeton
    doublé) ; mêmes formes, mêmes positions."""

    def logits(self, ids, k):
        return super().logits([ids[0]] + list(ids[:-1]), k)


def _perturbateur(ep, fmt, choisis):
    """Moteur artefact : à chaque position (t0, s0) choisie, quand le contexte est exactement le vrai, le logit du faux
    candidat est relevé pour passer devant le vrai d'un écart de 0,1 (quasi-égalité retournée)."""
    rec = rg.transcription(fmt, EnvironnementJouet(), T, ep["textes"], ep["ids"], ep["jetons"], ep["jetons_notes"])
    perts = []
    for (t0, s0, vrai, faux) in choisis:
        prefixe = rec["ids"][:rec["actions"][t0]["debut"]] + ep["ids"][t0][:s0]
        Q = rg.tirages_exponentiels(ep["graines"][t0], ep["jetons"][t0], V)[s0].double()
        perts.append((prefixe, vrai, faux, Q))

    class Perturbe(rg.Moteur):
        def logits(self, ids, k):
            L = super().logits(ids, k)
            for prefixe, vrai, faux, Q in perts:
                j = len(prefixe) - 1 - (len(ids) - k)
                if 0 <= j < k and list(ids[:len(prefixe)]) == prefixe:
                    L[j, faux] = float(L[j, vrai]) - float(torch.log(Q[vrai])) + float(torch.log(Q[faux])) + 0.1
            return L

    return Perturbe


def _quasi_cibles(ep, sain):
    """Positions (t, s, vrai, faux) à second candidat ordinaire, hors dernier jeton noté, par action."""
    par_t = {}
    for x in sain["pas"]:
        t, s, vrai, _, n, _, faux, _, _ = x
        if n > 1 and faux not in FINS_P3 and faux < 128000 and s < ep["jetons_notes"][t] - 1:
            par_t.setdefault(t, []).append((t, s, vrai, faux))
    return par_t


# ------------------------------------------------------------------------------------------------- 1. faits de base


def test_tirage_de_p3_egal_argmax_p_sur_q_et_tirages_en_un_appel():
    assert rg.exiger_equivalence_tirage(V)["egalites"] == 12
    assert rg.exiger_equivalence_tirage(50, graines=tuple(range(40)), pas=5)["egalites"] == 200
    # le tirage de `generer_lot` (softmax de logits float32, une graine par ligne) suit argmax(p / q), pas après pas
    g = torch.Generator(device="cpu").manual_seed(99)
    Q = rg.tirages_exponentiels(99, 6, V)
    for s in range(6):
        logits = torch.randn(V, generator=torch.Generator().manual_seed(s)) * 3
        p = torch.softmax(logits / 1.0, dim=-1)
        assert int(torch.multinomial(p, 1, generator=g)) == int(torch.argmax(p / Q[s]))


def test_graines_comme_jouer_p3():
    from controle_ia.environnements.pilote_a import graines_des_actions

    m = {"graines": graines(["tache/2506.00001v1", "tache/autre"], 20261102)}
    g = generateur(m["graines"]["tache/2506.00001v1"])
    attendu = graines_des_actions(g, 1, 10)
    g.random(10)                    # tirage de l'échantillon d'équivalence de P3, après les graines : sans effet
    assert rg.graines_p3(m, "2506.00001v1", 10) == [attendu[(0, t)] for t in range(10)]
    assert rg.graines_p3(m, "autre", 10) != rg.graines_p3(m, "2506.00001v1", 10)
    g2 = generateur(m["graines"]["tache/2506.00001v1"])
    g2.random(10)                   # ordre inverse : d'autres graines (l'ordre de P3 compte)
    assert [graines_des_actions(g2, 1, 10)[(0, t)] for t in range(10)] != rg.graines_p3(m, "2506.00001v1", 10)
    with pytest.raises(GardeArret, match="absente"):
        rg.graines_p3(m, "inconnue", 10)


def test_vocabulaire_et_decodage_de_llama(tok):
    voc = rg.Vocabulaire(tok, FINS_P3, V)
    assert voc.maxlen == 128 and len(voc.speciaux_non_fins) == 253 and voc.fins == sorted(FINS_P3)
    r = random.Random(0)
    for _ in range(500):
        s = [r.randrange(V) for _ in range(r.randint(1, 10))]
        assert tok.decode(s, skip_special_tokens=True) == b"".join(voc.octets[i] or b"" for i in s).decode("utf-8",
                                                                                                            "replace")
    with pytest.raises(GardeArret, match="dimension"):
        rg.Vocabulaire(tok, FINS_P3, V + 1)
    with pytest.raises(GardeArret, match="hors des jetons spéciaux"):
        rg.Vocabulaire(tok, FINS_P3 | {100}, V)
    # cible avec octets orphelins : « a », 0xC3 isolé (→ U+FFFD), « b » ; « é » en deux jetons (0xC3, 0xA9)
    a, c3, a9, b = (voc.par_octets[x] for x in (b"a", b"\xc3", b"\xa9", b"b"))
    for ids in ([a, c3, b], [a, c3, a9, b], [c3], [a9, a9]):
        texte = tok.decode(ids, skip_special_tokens=True)
        cible, etat = rg.Cible(texte, voc), rg.Cible.initial()
        for i in ids:
            cands, _ = cible.candidats(etat)
            assert i in cands
            etat = cible.avancer(etat, i)
            assert etat is not None
        assert cible.fini(etat)
    cible = rg.Cible("a�b", voc)
    etat = cible.avancer(cible.initial(), a)
    cands, balayage = cible.candidats(etat)
    assert balayage and {c3, a9} <= set(cands) and voc.par_octets[b"b"] not in cands
    assert rg.Cible("ab", voc).avancer((0, b""), voc.par_octets[b"x"]) is None


# ------------------------------------------------------------------------------------------------------- 2. cas sain


def test_cas_sain_identifiants_et_empreinte_retrouves(tok, fmt, jeu):
    modele, eps = jeu
    non_canoniques = arretees = invisibles = 0
    for ep in eps:
        for t in range(T):
            notes = ep["ids"][t][:ep["jetons_notes"][t]]
            non_canoniques += list(tok(ep["textes"][t], add_special_tokens=False)["input_ids"]) != notes
            arretees += ep["jetons"][t] == ep["jetons_notes"][t] == MAX
            invisibles += SPECIAL_INVISIBLE in ep["ids"][t]
        r = _resoudre(modele, tok, fmt, ep)
        assert r["statut"] == "resolu" and r["voie"] == "directe", r["cause"]
        assert r["ids"] == ep["ids"] and r["empreinte"] == ep["empreinte"]
        assert rg.accord_non_contraint(r["pas"]) == 1.0 == rg.accord_non_contraint(r["pas"], ep["ids"])
        assert all(x[5] > 0 for x in r["pas"])          # le choix retenu est le premier candidat
    assert non_canoniques >= 3 and arretees >= 1 and invisibles >= 1


# ------------------------------------------------------------------------------------------------------ 3. artefacts


def test_artefacts_graine_fausse_texte_altere_contexte_decale(tok, fmt, jeu):
    modele, eps = jeu
    ep = max(eps, key=lambda x: sum(x["jetons"]))
    sain = _resoudre(modele, tok, fmt, ep)
    assert sain["statut"] == "resolu"
    # graine fausse (action 1) : jamais résolu ; l'accord du choix non contraint s'effondre
    fausses = list(ep["graines"])
    fausses[1] += 1
    r = _resoudre(modele, tok, fmt, ep, graines_=fausses)
    assert r["statut"] == "non_resolu" and r["ids"] is None and r["cause"]
    assert rg.accord_non_contraint(r["pas"]) < 0.9
    # texte altéré d'un octet (une lettre remplacée par une autre, même longueur)
    t = max(range(T), key=lambda k: len(ep["textes"][k]))
    x = ep["textes"][t]
    k = next(i for i in range(len(x) // 2, len(x)) if x[i].isalpha())
    alt = list(ep["textes"])
    alt[t] = x[:k] + ("q" if x[k] != "q" else "z") + x[k + 1:]
    assert len(alt[t].encode()) == len(x.encode()) and alt[t] != x
    r = _resoudre(modele, tok, fmt, ep, textes=alt)
    assert r["statut"] == "non_resolu" and r["ids"] is None
    # contexte décalé d'un jeton : détecté (non résolu), accord nul ou presque
    r = _resoudre(modele, tok, fmt, ep, moteur=MoteurDecale(modele))
    assert r["statut"] == "non_resolu" and rg.accord_non_contraint(r["pas"]) < 0.5


def test_repli_bascule_une_quasi_egalite(tok, fmt, jeu):
    """Le repli écrit retrouve l'empreinte quand l'essai direct se trompe sur une quasi-égalité. Artefact : un moteur
    qui, à un pas choisi (deux candidats compatibles ou plus, second candidat ordinaire), relève le logit du second
    candidat pour qu'il passe devant le vrai d'un écart de 0,1 ; l'essai direct se trompe, le repli bascule ce pas vers
    son second candidat (le vrai) et l'empreinte est retrouvée. Sous un seuil de 0,05, ce pas n'est pas une
    quasi-égalité : le repli ne le bascule pas, non résolu, cause écrite."""
    modele, eps = jeu
    ep = max(eps, key=lambda x: sum(x["jetons"]))
    sain = _resoudre(modele, tok, fmt, ep)
    t0, s0, vrai, _, _, _, faux, _, _ = next(x for x in sain["pas"] if x[4] > 1 and x[6] not in FINS_P3
                                            and x[1] < ep["jetons_notes"][x[0]] - 1)
    rec = rg.transcription(fmt, EnvironnementJouet(), T, ep["textes"], ep["ids"], ep["jetons"], ep["jetons_notes"])
    prefixe = rec["ids"][:rec["actions"][t0]["debut"]] + ep["ids"][t0][:s0]
    Q = rg.tirages_exponentiels(ep["graines"][t0], ep["jetons"][t0], V)[s0].double()

    class Perturbe(rg.Moteur):
        def logits(self, ids, k):
            L = super().logits(ids, k)
            j = len(prefixe) - 1 - (len(ids) - k)
            if 0 <= j < k and list(ids[:len(prefixe)]) == prefixe:
                cible = float(L[j, vrai]) - float(torch.log(Q[vrai])) + float(torch.log(Q[faux])) + 0.1
                L[j, faux] = cible
            return L

    r = _resoudre(modele, tok, fmt, ep, moteur=Perturbe(modele))
    assert r["statut"] == "resolu" and r["voie"] == "repli" and r["ids"] == ep["ids"], r["cause"]
    assert r["forcages"][0]["pas"] == t0 and r["forcages"][0]["rang"] == s0 and r["forcages"][0]["jeton"] == vrai
    assert r["ids_directs"][t0][s0] == faux
    r = _resoudre(modele, tok, fmt, ep, moteur=Perturbe(modele), seuil_ecart=0.05)
    assert r["statut"] == "non_resolu" and "repli" in r["cause"]
    assert all((q["pas"], q["rang"]) != (t0, s0) for q in r["quasi_egalites"])


def test_repli_iteratif_deux_bascules_dans_deux_actions(tok, fmt, jeu):
    """VG-02 (perturbation du vérificateur, `e2e_repli2.py`) : deux erreurs à 0,1 près, l'une dans l'action 1, l'autre
    dans l'action 2 ; la seconde n'existe que dans le contexte vrai, donc seulement dans le rejeu de la première bascule
    (la bascule change le découpage et la longueur des jetons qui suivent). Repli itératif : résolu par deux bascules,
    identifiants et empreinte du harnais. Artefact : à une seule bascule (`bascules_max` = 1), non résolu, cause écrite
    (jamais un faux « résolu »)."""
    modele, eps = jeu
    ep = max(eps, key=lambda x: sum(x["jetons"]))
    sain = _resoudre(modele, tok, fmt, ep)
    par_t = _quasi_cibles(ep, sain)
    assert par_t.get(1) and par_t.get(2)
    paires = [(par_t[1][0], par_t[2][0]), (par_t[1][-1], par_t[2][-1])]
    for a, b in paires:
        P = _perturbateur(ep, fmt, [a, b])
        r = _resoudre(modele, tok, fmt, ep, moteur=P(modele), combinaisons_max=136, quasi_egalites_max=16)
        assert r["statut"] == "resolu" and r["voie"] == "repli" and r["ids"] == ep["ids"], r["cause"]
        assert r["empreinte"] == ep["empreinte"]
        assert [(f["pas"], f["rang"], f["jeton"]) for f in r["forcages"]] == [a[:2] + (a[2],), b[:2] + (b[2],)]
        assert r["repli"]["par_niveau"].get("2", 0) >= 1 and r["combinaisons_essayees"] <= 136
        # la seconde erreur n'est pas parmi les quasi-égalités de l'essai direct : seul le rejeu basculé la révèle
        assert (b[0], b[1], b[3]) not in {(q["pas"], q["rang"], q["choix"]) for q in r["quasi_egalites"]}
        r1 = _resoudre(modele, tok, fmt, ep, moteur=P(modele), combinaisons_max=136, quasi_egalites_max=16,
                       bascules_max=1)
        assert r1["statut"] == "non_resolu" and r1["ids"] is None and "repli itératif" in r1["cause"]


def test_budget_de_l_episode_non_resolu_duree(tok, fmt, jeu, monkeypatch):
    """VG-01 : le budget de l'épisode s'épuise au milieu d'un essai → « non résolu », cause « durée », sans exception
    (l'étape continue) ; budget suffisant → résolu (cas sain) ; échéance de l'étape plus proche que celle de l'épisode :
    elle prime."""
    import time

    modele, eps = jeu
    ep = max(eps, key=lambda x: sum(x["jetons"]))
    decalage = [0.0]
    monkeypatch.setattr(rg, "horloge", lambda: time.perf_counter() + decalage[0])

    class Lent(rg.Moteur):
        def passe(self, ids, k, Q, temperature):
            decalage[0] += 10.0                 # chaque passe « dure » 10 s
            return super().passe(ids, k, Q, temperature)

    sain = _resoudre(modele, tok, fmt, ep, moteur=Lent(modele), duree_episode_s=1e6)
    assert sain["statut"] == "resolu" and not sain["duree_epuisee"] and sain["passes"] >= 3
    r = _resoudre(modele, tok, fmt, ep, moteur=Lent(modele), duree_episode_s=25.0)
    assert r["statut"] == "non_resolu" and r["duree_epuisee"] and r["cause"].startswith("durée")
    assert r["ids"] is None and 0 < len(r["pas"]) < len(sain["pas"])
    assert rg.echeance_episode(rg.Reglages(echeance=5.0, duree_episode_s=100.0), 0.0) == 5.0
    assert rg.echeance_episode(rg.Reglages(echeance=500.0, duree_episode_s=100.0), 0.0) == 100.0
    assert rg.echeance_episode(rg.Reglages(), 0.0) is None
    # pendant le repli : le budget s'épuise entre deux combinaisons → non résolu, durée, combinaisons comptées
    a = _quasi_cibles(ep, sain)[1][0]
    P = _perturbateur(ep, fmt, [a])

    class LentPerturbe(P):
        def passe(self, ids, k, Q, temperature):
            decalage[0] += 10.0
            return super().passe(ids, k, Q, temperature)

    direct = _resoudre(modele, tok, fmt, ep, moteur=LentPerturbe(modele), duree_episode_s=1e6)
    assert direct["voie"] == "repli"
    r = _resoudre(modele, tok, fmt, ep, moteur=LentPerturbe(modele), duree_episode_s=10.0 * direct["passes"] + 5,
                  quasi_egalites_max=16)
    assert r["statut"] == "non_resolu" and r["duree_epuisee"] and "durée" in r["cause"]


def test_caractere_de_remplacement_resolu_ou_declare(tok, fmt, jeu_octets):
    modele, eps = jeu_octets
    avec = [ep for ep in eps if any("�" in x for x in ep["textes"])]
    assert avec, "aucun texte à caractère de remplacement dans le jeu"
    assert any("é" in x for ep in eps for x in ep["textes"])
    for ep in eps:
        r = _resoudre(modele, tok, fmt, ep)
        assert r["statut"] == "resolu" and r["ids"] == ep["ids"], r["cause"]
        assert r["fffd"] == sum(x.count("�") for x in ep["textes"])
    ep = avec[0]
    r = _resoudre(modele, tok, fmt, ep)
    assert r["balayages"] >= 1
    r = _resoudre(modele, tok, fmt, ep, balayages_max=0)
    assert r["statut"] == "non_resolu" and "caractère de remplacement" in r["cause"] and r["fffd"] >= 1


def test_seuls_les_balayages_complets_sont_comptes(tok, fmt, jeu_octets):
    """VG-07 : un balayage n'est compté que s'il examine tout le vocabulaire (octets connus épuisés devant un U+FFFD) ;
    les pas proches d'un U+FFFD dont le préfixe connu est non vide (recherche bornée) ne comptent pas. Au plus deux
    balayages complets par U+FFFD sur l'essai direct (ici, le jeu à octets orphelins), et chacun est bien un examen de
    tout le vocabulaire (autant de candidats qu'un appel à `commencant_par(b"")` filtré)."""
    modele, eps = jeu_octets
    voc = rg.Vocabulaire(tok, fmt.fins, V)
    total_fffd = total_complets = 0
    for ep in eps:
        r = _resoudre(modele, tok, fmt, ep)
        assert r["statut"] == "resolu"
        n = sum(x.count("�") for x in ep["textes"])
        total_fffd += n
        total_complets += r["balayages"]
        assert r["balayages"] == sum(1 for x in r["pas"] if x[8]) <= 2 * n
    assert total_fffd >= 1 and total_complets >= 1
    # près d'un U+FFFD, avec un préfixe connu non vide : candidats par recherche bornée, non comptée
    a, b = voc.par_octets[b"a"], voc.par_octets[b"b"]
    cible = rg.Cible("ab�", voc)
    cands, complet = cible.candidats(cible.initial())
    assert not complet and a in cands
    cands, complet = cible.candidats(cible.avancer(cible.avancer(cible.initial(), a), b))
    assert complet and len(cands) > 100


def test_garde_du_seuil_de_validation():
    rg.exiger_seuil_validation(147, 147, 147)
    with pytest.raises(GardeArret, match="sous le seuil"):
        rg.exiger_seuil_validation(146, 147, 147)
    with pytest.raises(GardeArret, match="seuil de validation"):
        rg.exiger_seuil_validation(140, 148, 147)
    # avant la boucle (VG-04) : seuil atteignable, sinon arrêt avant tout calcul
    rg.exiger_seuil_atteignable(147, 147)
    rg.exiger_seuil_atteignable(0, 0)
    with pytest.raises(GardeArret, match="seuil de validation 148 > 147"):
        rg.exiger_seuil_atteignable(148, 147)


# ------------------------------------------------------------------------------------------ 4. table, forme nouvelle


def _lignes(ep):
    return [{"episode": ep["identifiant"], "pas": t, "texte": ep["textes"][t]} for t in range(T)]


def test_forme_identifiants_cas_sain_et_artefacts(tok, fmt, jeu):
    modele, eps = jeu
    fiches, entrees = {}, []
    for ep in eps:
        base = ra.reconstruire_episode(fmt, EnvironnementJouet(), T, _lignes(ep), ep["jetons"], ep["jetons_notes"])
        base_nv = [list(a["nv"]) for a in base["actions"]]
        fiches[ep["identifiant"]] = {"trajectoire": ep["empreinte"]}
        if base_nv == ep["ids"]:
            continue
        e = rg.entree_identifiants(ep["identifiant"], ep["empreinte"], base_nv, ep["ids"])
        assert e["actions"] and all(a["canonique"] != a["p3"] for a in e["actions"])
        entrees.append(e)
    assert entrees

    def contexte(e):
        ep = next(x for x in eps if x["identifiant"] == e)
        return EnvironnementJouet(), _lignes(ep), ep["jetons"], ep["jetons_notes"], T

    assert rg.verifier_entrees_v3(entrees, fmt, contexte, fiches) == len(entrees)
    e0 = entrees[0]
    ep0 = next(x for x in eps if x["identifiant"] == e0["episode"])
    # artefacts : base citée fausse ; identifiants qui ne redonnent pas le texte ; empreinte de P3 fausse ; formes
    a = json.loads(json.dumps(e0))
    a["actions"][0]["canonique"] = a["actions"][0]["canonique"][::-1] + [5]
    with pytest.raises(GardeArret, match="canonique"):
        rg.appliquer_entree_v3(fmt, EnvironnementJouet(), T, _lignes(ep0), ep0["jetons"], ep0["jetons_notes"], a)
    a = json.loads(json.dumps(e0))
    p3 = a["actions"][0]["p3"]
    k = next(i for i, x in enumerate(p3) if x not in FINS_P3)
    za, zb = tok.convert_tokens_to_ids("zz"), tok.convert_tokens_to_ids("qq")
    assert isinstance(za, int) and isinstance(zb, int)
    p3[k] = za if p3[k] != za else zb
    with pytest.raises(GardeArret, match="non conforme"):
        rg.appliquer_entree_v3(fmt, EnvironnementJouet(), T, _lignes(ep0), ep0["jetons"], ep0["jetons_notes"], a)
    with pytest.raises(GardeArret, match="empreinte de P3"):
        rg.verifier_entrees_v3([e0], fmt, contexte, {e0["episode"]: {"trajectoire": "0" * 64}})
    for casse in ({"fins": {"1": 128008}}, {"paires": [{"pas": 0}]}, {"actions": []},
                  {"actions": [{"pas": 0, "canonique": [1], "p3": [1]}]},
                  {"actions": [{"pas": 1, "canonique": [1], "p3": [2]}, {"pas": 0, "canonique": [1], "p3": [2]}]},
                  {"actions": [{"pas": 0, "canonique": [1], "p3": [True]}]}, {"methode": "inventee"}):
        with pytest.raises(GardeArret):
            rg.verifier_forme_v3({**e0, **casse})


def test_formes_des_tables_v1_et_v2_acceptees_telles_quelles(tmp_path):
    t2 = json.loads((RACINE / "prereg" / "R1-table-tokenisation-v2.json").read_text(encoding="utf-8"))
    for e in t2["episodes"]:
        rg.verifier_forme_v3(e)
    v3 = {**t2, "version": rg.VERSION_TABLE_V3,
          "episodes": t2["episodes"] + [{"episode": "x/y/e0", "methode": rg.METHODE_IDENTIFIANTS,
                                         "trajectoire_p3": "0" * 64, "fins": {}, "paires": [],
                                         "actions": [{"pas": 0, "canonique": [1, 2], "p3": [3, 4]}]}]}
    p = tmp_path / "table-v3.json"
    p.write_text(json.dumps(v3), encoding="utf-8")
    sceller(p)
    assert len(rg.charger_table_v3(p, None)["episodes"]) == len(t2["episodes"]) + 1
    with pytest.raises(GardeArret, match="empreinte citée"):
        rg.charger_table_v3(p, "f" * 64)
    v3["episodes"].append(v3["episodes"][-1])
    p2 = tmp_path / "table-v3-double.json"
    p2.write_text(json.dumps(v3), encoding="utf-8")
    sceller(p2)
    with pytest.raises(GardeArret, match="double"):
        rg.charger_table_v3(p2, None)
    with pytest.raises(GardeArret, match="version"):
        p3 = tmp_path / "table-v2.json"
        p3.write_text(json.dumps(t2), encoding="utf-8")
        sceller(p3)
        rg.charger_table_v3(p3, None)


def test_table_v3_ecrite_scellee_jamais_ecrasee(tmp_path):
    """VG-08 : l'étape « table » écrit la table v3 avec son sceau (relu par `verifier`, chargeable par
    `charger_table_v3` à l'empreinte citée) ; jamais par-dessus un fichier ou un sceau existant (R12)."""
    from controle_ia.scellement import verifier

    t2 = json.loads((RACINE / "prereg" / "R1-table-tokenisation-v2.json").read_text(encoding="utf-8"))
    v3 = {**t2, "version": rg.VERSION_TABLE_V3}
    sortie = tmp_path / "R1-table-tokenisation-v3.json"
    sha = rg.ecrire_table_v3(v3, sortie)
    assert (tmp_path / "R1-table-tokenisation-v3.json.sha256").exists() and verifier(sortie) == sha
    assert rg.charger_table_v3(sortie, sha)["version"] == 3
    with pytest.raises(GardeArret, match="existe déjà"):
        rg.ecrire_table_v3(v3, sortie)
    orphelin = tmp_path / "autre.json"
    (tmp_path / "autre.json.sha256").write_text("0" * 64 + "  autre.json\n")
    with pytest.raises(GardeArret, match="existe déjà"):
        rg.ecrire_table_v3(v3, orphelin)


# --------------------------------------------------------------------------------------- 5. bout en bout (P3 jouet)


def _config_graine(depot, f, c, table, episodes_resolution, **k):
    d = depot / "donnees" / RUN_P3
    base = {"agent": {"nom": "agent-jouet"}, "mode": "jouet", "T": c["T"], "run_source": RUN_P3,
            "chemin_textes": str(d / "textes-actions-p3.jsonl"), "textes_sha256": None,
            "chemin_scores": str(d / "scores-p3.npz"), "scores_sha256": None, "identite_sha256": None,
            "chemin_fiches": str(depot / "diag" / RUN_P3 / "episodes-p3.json"), "fiches_sha256": None,
            "chemin_taches": str(f), "taches_sha256": None, "chemin_consignes": c["chemin_consignes"],
            "consignes_sha256": c["consignes_sha256"],
            "chemin_manifeste_p3": str(depot / "runs" / RUN_P3 / "manifeste.json"), "manifeste_p3_sha256": None,
            "chemin_table_tokenisation": str(table), "table_tokenisation_sha256": None,
            "episodes_resolution": episodes_resolution, "temperature": c["temperature"],
            "max_nouveaux": c["max_nouveaux"], "noyau_attention": "math", "fils": 1, "hors_ligne": True,
            "fils_tirages": 2, "episodes_d_avance": 1, "seuil_ecart": 0.5, "quasi_egalites_max": 4, "bascules_max": 2,
            "combinaisons_max": 10, "combinaisons_max_validation": 10, "balayages_max": 8, "seuil_validation": 0,
            "duree_max_s": 900, "duree_max_episode_s": 300}
    base.update(k)
    return base


def test_bout_en_bout_jouet_validation_resolution_table(source, tmp_path, monkeypatch):
    from conftest import committer

    depot, f, c = source
    fiches_p = depot / "diag" / RUN_P3 / "episodes-p3.json"
    table0 = _table(depot, f, c, fiches_p, tmp_path / "table0.json")
    # épisodes non conformes en longueur (jeton spécial tiré, effacé du texte stocké) : hors de portée de la table,
    # cités « non résolus » dans une table v2 jouet pour éprouver la forme nouvelle de bout en bout
    conf0 = _config_graine(depot, f, c, tmp_path / "table0.json", [])
    pieces0 = rg.charger_pieces(conf0, depot)
    from controle_ia.environnements.lancer_pilote_a import charger_modele_et_format
    from controle_ia.harnais.run_harnais_factice import graine_entiere

    _, fmt_j = charger_modele_et_format(conf0["agent"], "jouet", graine_entiere(pieces0.manifeste_p3["graines"]
                                                                                 ["modele-jouet"]))
    cl = rg.classer(pieces0, fmt_j, int(c["T"]))
    connus = [e for e, x in cl.items() if x["identique_base"] or (x["entree"] and x["entree"]["methode"] != "non_resolu")]
    autres = [e for e in cl if e not in connus]
    assert connus and autres, (len(connus), len(autres))
    table = json.loads((tmp_path / "table0.json").read_text(encoding="utf-8"))
    table["episodes"] += [{"episode": e, "methode": "non_resolu", "trajectoire_p3": pieces0.fiches[e]["trajectoire"],
                           "fins": {}, "paires": [], "essais": {}} for e in autres]
    table["comptes"]["non_resolu"] = table["comptes"].get("non_resolu", 0) + len(autres)
    tp = tmp_path / "table-jouet-v2.json"
    tp.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(tp)
    committer(depot)
    resolution = autres + connus[:1]                  # un épisode connu : contrôle croisé
    conf = _config_graine(depot, f, c, tp, resolution, seuil_validation=len(connus))
    del table0
    # étape « resolution » sans validation : refusée avant tout calcul
    with pytest.raises(GardeArret, match="validation"):
        rg.executer(conf, depot, "20261102-100000-graine-jouet", None, "resolution", None, autoriser_depot_sale=True,
                    entropie_essai=3)
    v = rg.executer(conf, depot, "20261102-100100-graine-jouet", None, "validation", autoriser_depot_sale=True,
                    entropie_essai=3)
    assert v["lecture"] == "atteint" and v["empreintes_retrouvees"] == v["episodes_etape"] == len(connus)
    assert v["identifiants_egaux_episodes"] == len(connus) and v["actions_egales"] == v["actions_comparees"]
    assert v["accord_non_contraint"]["par_episode_min"] == 1.0 and not v["erreurs_directes"]
    pas_v = depot / "diag" / "20261102-100100-graine-jouet" / v["pas_fichier"]
    assert (pas_v.parent / (pas_v.name + ".sha256")).exists()
    with np.load(pas_v) as z:
        assert len(z["choix"]) == v["accord_non_contraint"]["pas"] and (z["choix"] == z["non_contraint"]).all()
    chemin_v = depot / "diag" / "20261102-100100-graine-jouet" / "resolution-graine-validation.json"
    committer(depot)            # comme l'instance : résultats de la validation committés avant la résolution
    r = rg.executer(conf, depot, "20261102-100200-graine-jouet", None, "resolution", str(chemin_v),
                    autoriser_depot_sale=True, entropie_essai=3)
    assert r["lecture"] == "complète" and r["controle_croise_lecture"] == "conforme"
    assert [x["episode"] for x in r["episodes"]] == resolution
    assert all(x["empreinte_retrouvee"] and x["ids"] for x in r["episodes"])
    # table version 3 : les non résolus de la table v2 reçoivent la forme « identifiants », revérifiée par l'empreinte
    chemin_r = depot / "diag" / "20261102-100200-graine-jouet" / "resolution-graine-resolution.json"
    t3 = rg.construire_et_verifier_table(conf, depot, None, str(chemin_r), fmt=fmt_j)
    assert t3["version"] == 3 and t3["comptes"]["identifiants"] == len(autres) and t3["comptes"]["non_resolu"] == 0
    anciennes = sum(1 for x in table["episodes"] if x["methode"] != "non_resolu")
    assert t3["corrections_verifiees"] == len(autres) + anciennes
    assert all(x["methode"] == rg.METHODE_IDENTIFIANTS for x in t3["episodes"] if x["episode"] in autres)
    # épisodes consignés un à un, scellés (VG-01) ; validation à paires permises (VG-03)
    d_v = depot / "diag" / "20261102-100100-graine-jouet"
    assert [x["fichier"] for x in v["episodes_consignes"]] == [f"episodes-validation/{k:03d}.json"
                                                               for k in range(len(connus))]
    for x in v["episodes_consignes"]:
        assert (d_v / (x["fichier"] + ".sha256")).exists()
        assert json.loads((d_v / x["fichier"]).read_text(encoding="utf-8"))["statut"] == x["statut"] == "resolu"
    assert v["seuils"]["combinaisons_max_validation"] == v["seuils"]["combinaisons_max"]
    assert v["reserves"] == [] and v["environnement"]["torch"] == torch.__version__
    assert set(v["accord_non_contraint"]["par_episode"]) == set(connus)
    # graines fausses (artefact, R5) : la validation tombe sous le seuil, rapportée, SANS arrêt (VG-03)
    vraies = rg.graines_p3
    monkeypatch.setattr(rg, "graines_p3", lambda m, tache, T_: [g + 1 for g in vraies(m, tache, T_)])
    sous = rg.executer(conf, depot, "20261102-100300-graine-jouet", None, "validation", autoriser_depot_sale=True,
                       entropie_essai=3)
    assert sous["lecture"] == "sous le seuil" and sous["empreintes_retrouvees"] < len(connus)
    assert not (depot / "diag" / "20261102-100300-graine-jouet" / "arret.json").exists()
    assert sous["accord_non_contraint"]["moyenne_par_episode"] < 0.9 and sous["non_resolus"]
    # code modifié après la validation (arbre gelé) : la validation ne vaut plus
    m_v = json.loads((depot / "runs" / "20261102-100100-graine-jouet" / "manifeste.json").read_text(encoding="utf-8"))
    rg.exiger_meme_code(depot, m_v["commit"])
    (depot / "README").write_text("modifié\n")
    committer(depot)
    with pytest.raises(GardeArret, match="autre code"):
        rg.exiger_meme_code(depot, m_v["commit"])
    # une validation « sous le seuil » n'empêche pas la résolution (VG-03) : un « résolu » se certifie par l'empreinte
    monkeypatch.setattr(rg, "graines_p3", vraies)
    m_s = json.loads((depot / "runs" / "20261102-100300-graine-jouet" / "manifeste.json").read_text(encoding="utf-8"))
    (depot / "README").write_text("x\n")          # arbre gelé ramené à celui de la validation
    committer(depot)
    rg.exiger_meme_code(depot, m_s["commit"])
    r2 = rg.executer(conf, depot, "20261102-100400-graine-jouet", None, "resolution",
                     str(depot / "diag" / "20261102-100300-graine-jouet" / "resolution-graine-validation.json"),
                     autoriser_depot_sale=True, entropie_essai=3)
    assert r2["lecture"] == "complète" and r2["controle_croise_lecture"] == "conforme"
    assert all(x["empreinte_retrouvee"] and x["empreinte"] == x["empreinte_cible"] for x in r2["episodes"])
    # artefact : un résultat « résolu » sans l'empreinte recalculée égale n'entre pas dans la table v3
    faux = json.loads(json.dumps(json.loads(chemin_r.read_text(encoding="utf-8"))["resultat"]))
    cible_ep = next(x for x in faux["episodes"] if x["episode"] in autres)
    cible_ep["empreinte"] = "0" * 64
    with pytest.raises(GardeArret, match="sans l'empreinte"):
        rg.construire_table_v3(table, "0" * 64, faux, "1" * 64, {e: x["base_nv"] for e, x in cl.items()})


def _preparer_jouet(source, tmp_path):
    """P3 jouet, table v2 jouet (épisodes hors de portée de la table cités « non résolus »), classement."""
    from conftest import committer
    from controle_ia.environnements.lancer_pilote_a import charger_modele_et_format
    from controle_ia.harnais.run_harnais_factice import graine_entiere

    depot, f, c = source
    fiches_p = depot / "diag" / RUN_P3 / "episodes-p3.json"
    _table(depot, f, c, fiches_p, tmp_path / "table0.json")
    conf0 = _config_graine(depot, f, c, tmp_path / "table0.json", [])
    pieces0 = rg.charger_pieces(conf0, depot)
    _, fmt_j = charger_modele_et_format(conf0["agent"], "jouet", graine_entiere(pieces0.manifeste_p3["graines"]
                                                                                 ["modele-jouet"]))
    cl = rg.classer(pieces0, fmt_j, int(c["T"]))
    connus = [e for e, x in cl.items() if x["identique_base"] or (x["entree"] and x["entree"]["methode"] != "non_resolu")]
    autres = [e for e in cl if e not in connus]
    table = json.loads((tmp_path / "table0.json").read_text(encoding="utf-8"))
    table["episodes"] += [{"episode": e, "methode": "non_resolu", "trajectoire_p3": pieces0.fiches[e]["trajectoire"],
                           "fins": {}, "paires": [], "essais": {}} for e in autres]
    table["comptes"]["non_resolu"] = table["comptes"].get("non_resolu", 0) + len(autres)
    tp = tmp_path / "table-jouet-v2.json"
    tp.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(tp)
    committer(depot)
    return depot, f, c, tp, connus, autres


def test_bout_en_bout_echeances_en_milieu_d_etape_et_signal(source, tmp_path, monkeypatch):
    """VG-01, en mode jouet de bout en bout, horloge des échéances avancée artificiellement : (1) le budget d'un épisode
    s'épuise au milieu de son essai → « non résolu : durée », l'étape continue et l'épisode suivant est résolu ; (2) le
    budget de l'étape s'épuise au milieu d'un épisode → cet épisode « durée », les suivants « non tenté : durée » ; le
    résultat est écrit, chaque épisode consigné aussitôt dans un fichier scellé. (3) Signal TERM au milieu de l'étape :
    arrêt consigné, `arret.json` cite les épisodes déjà consignés (fichiers scellés, identifiants retrouvés)."""
    import time

    from controle_ia import gardes

    depot, f, c, tp, connus, autres = _preparer_jouet(source, tmp_path)
    assert len(connus) >= 4, len(connus)
    conf = _config_graine(depot, f, c, tp, autres, seuil_validation=len(connus), duree_max_s=900,
                          duree_max_episode_s=300)
    decalage = [0.0]
    monkeypatch.setattr(rg, "horloge", lambda: time.perf_counter() + decalage[0])
    vraie = rg.resoudre_avec_repli
    appels = [0]
    sauts = {2: 301.0, 3: 700.0}            # appel 2 : budget de l'épisode ; appel 3 : budget de l'étape (900 s)

    def espion(moteur, *a, **k):
        appels[0] += 1
        n, passe = appels[0], moteur.passe
        fait = [False]

        def passe_qui_saute(*x, **y):
            sortie = passe(*x, **y)
            if n in sauts and not fait[0]:
                decalage[0] += sauts[n]
                fait[0] = True
            return sortie

        moteur.passe = passe_qui_saute
        try:
            return vraie(moteur, *a, **k)
        finally:
            moteur.passe = passe

    monkeypatch.setattr(rg, "resoudre_avec_repli", espion)
    v = rg.executer(conf, depot, "20261102-110000-graine-jouet", None, "validation", autoriser_depot_sale=True,
                    entropie_essai=3)
    eps = v["episodes"]
    assert appels[0] == 3 and len(eps) == len(connus) == v["episodes_etape"]
    assert eps[0]["statut"] == "resolu"
    assert eps[1]["statut"] == "non_resolu" and eps[1]["duree_epuisee"] and eps[1]["cause"].startswith("durée")
    assert not eps[1].get("non_tente")
    assert eps[2]["statut"] == "non_resolu" and eps[2]["duree_epuisee"] and not eps[2].get("non_tente")
    assert all(x.get("non_tente") and x["cause"].startswith("durée : budget de l'étape") for x in eps[3:])
    assert v["non_tentes"] == len(connus) - 3 and v["non_resolus_duree"] == len(connus) - 1
    assert v["lecture"] == "sous le seuil" and v["empreintes_retrouvees"] == 1
    d = depot / "diag" / "20261102-110000-graine-jouet"
    assert len(v["episodes_consignes"]) == len(connus) and not (d / "arret.json").exists()
    for x in v["episodes_consignes"]:
        assert (d / (x["fichier"] + ".sha256")).exists()
    # (1 bis) l'épisode suivant un budget d'épisode épuisé est traité : avec un seul saut d'épisode, il est résolu
    decalage[0], appels[0] = 0.0, 0
    sauts.clear()
    sauts[1] = 301.0
    v2 = rg.executer(conf, depot, "20261102-110100-graine-jouet", None, "validation", autoriser_depot_sale=True,
                     entropie_essai=3)
    assert v2["episodes"][0]["duree_epuisee"] and all(x["statut"] == "resolu" for x in v2["episodes"][1:])
    # (3) signal TERM après le deuxième épisode : arrêt consigné, épisodes déjà consignés cités par arret.json
    decalage[0], appels[0] = 0.0, 0
    sauts.clear()

    def espion_term(moteur, *a, **k):
        r = vraie(moteur, *a, **k)
        appels[0] += 1
        if appels[0] == 2:
            gardes.SIGNAL_TERM_RECU.append(15)
        return r

    monkeypatch.setattr(rg, "resoudre_avec_repli", espion_term)
    with pytest.raises(GardeArret, match="signal TERM"):
        rg.executer(conf, depot, "20261102-110200-graine-jouet", None, "validation", autoriser_depot_sale=True,
                    entropie_essai=3)
    d = depot / "diag" / "20261102-110200-graine-jouet"
    arret = json.loads((d / "arret.json").read_text(encoding="utf-8"))["resultat"]
    consignes = arret["partiel"]["episodes_consignes"]
    assert "signal TERM" in arret["motif"] and len(consignes) == 2 and arret["partiel"]["episodes_traites"] == 2
    for x in consignes:
        corps = json.loads((d / x["fichier"]).read_text(encoding="utf-8"))
        assert (d / (x["fichier"] + ".sha256")).exists() and corps["statut"] == "resolu" and corps["ids"]
        assert corps["empreinte"] == corps["empreinte_cible"]
    assert not (d / "resolution-graine-validation.json").exists()


def test_gardes_d_execution_agent_environnement_controle_croise():
    """VG-04 à VG-06 : gardes avant tout chargement (budget par épisode, noyau, paires en validation), agent comparé au
    manifeste de P3, réserves d'environnement écrites sans arrêt, contrôle croisé lu à trois valeurs. Chaque garde :
    cas sain, artefact."""
    base = {"duree_max_s": 1800, "duree_max_episode_s": 300, "noyau_attention": "defaut", "combinaisons_max": 136,
            "combinaisons_max_validation": 136}
    rg.exiger_reglages_execution(base)
    rg.exiger_reglages_execution({**base, "noyau_attention": "math"})
    for k, v, motif in (("noyau_attention", "flash", "noyau_attention"), ("noyau_attention", None, "noyau_attention"),
                        ("combinaisons_max_validation", 16, "paires"), ("duree_max_episode_s", 0, "duree_max_episode_s"),
                        ("duree_max_episode_s", 4000, "duree_max_episode_s"),
                        ("duree_max_episode_s", True, "duree_max_episode_s")):
        with pytest.raises(GardeArret, match=motif):
            rg.exiger_reglages_execution({**base, k: v})
    with pytest.raises(GardeArret, match="incomplète"):
        rg.exiger_reglages_execution({k: v for k, v in base.items() if k != "duree_max_episode_s"})
    # agent de P3 (manifeste réel de P3 : configuration seule)
    m = json.loads((RACINE / "runs" / "20261019-230011-p3-reel" / "manifeste.json").read_text(encoding="utf-8"))
    agent = {"nom": "8B", "modele": MODELE, "revision": REVISION, "variables_gabarit": {"date_string": "26 Jul 2024"},
             "texte_attendu_ouverture": "Today Date: 26 Jul 2024"}
    rg.exiger_agent_de_p3(agent, m, True)
    for k, v in (("revision", "f" * 40), ("modele", "meta-llama/Llama-3.1-70B-Instruct"),
                 ("variables_gabarit", {"date_string": "02 Nov 2026"}), ("variables_gabarit", None)):
        with pytest.raises(GardeArret, match="agent"):
            rg.exiger_agent_de_p3({**agent, k: v}, m, True)
    rg.exiger_agent_de_p3({"nom": "agent-jouet"}, {"config": {"agent": {"nom": "agent-jouet"}}}, False)
    with pytest.raises(GardeArret, match="sans modèle"):
        rg.exiger_agent_de_p3({"nom": "x"}, {"config": {"agent": {"nom": "x"}}}, True)
    # réserves d'environnement (VG-05) : écrites, jamais un arrêt ; rien en mode jouet
    p3 = {"torch": "2.14.1+cu130", "cuda": "13.0", "cudnn": 92400, "carte": "NVIDIA A100-SXM4-80GB"}
    assert rg.reserves_environnement(p3, True) == []
    r = rg.reserves_environnement({**p3, "torch": "2.14.1+cu128", "cuda": "12.8"}, True)
    assert len(r) == 1 and "CUDA '12.8'" in r[0]
    r = rg.reserves_environnement({**p3, "cudnn": 91000, "carte": "NVIDIA H100 80GB HBM3"}, True)
    assert len(r) == 2 and any("cuDNN" in x for x in r) and any("carte" in x for x in r)
    assert rg.reserves_environnement({"torch": "2.14.1+cpu", "cuda": None}, False) == []
    assert rg.environnement_d_execution(False)["torch"] == torch.__version__
    # contrôle croisé à trois valeurs (VG-06) : un non résolu n'est jamais lu « contraire »
    ok = {"statut": "resolu", "identifiants_egaux": True}
    assert rg.lecture_controle_croise([ok, ok]) == "conforme"
    assert rg.lecture_controle_croise([ok, {"statut": "non_resolu", "identifiants_egaux": False}]) == "non résolu"
    assert rg.lecture_controle_croise([{"statut": "non_resolu", "identifiants_egaux": False},
                                       {"statut": "resolu", "identifiants_egaux": False}]) == "contraire"
    assert rg.lecture_controle_croise([]) == "sans objet"


def test_configuration_gardes():
    base = {k: None for k in rg.CLES}
    base.update(mode="reel", T=10, max_nouveaux=400, fils=1, fils_tirages=8, episodes_d_avance=2, quasi_egalites_max=12,
                bascules_max=2, combinaisons_max=80, combinaisons_max_validation=12, balayages_max=64,
                seuil_validation=147, temperature=1.0, seuil_ecart=0.5, duree_max_s=3000, episodes_resolution=["a"])
    with pytest.raises(GardeArret, match="obligatoire"):
        rg.exiger_config(base)
    with pytest.raises(GardeArret, match="incomplète"):
        rg.exiger_config({k: v for k, v in base.items() if k != "seuil_ecart"})
    jouet = {**base, "mode": "jouet"}
    rg.exiger_config(jouet)
    for k, v in (("temperature", 0.0), ("seuil_validation", -1), ("fils", True), ("episodes_resolution", ["a", "a"]),
                 ("mode", "autre")):
        with pytest.raises(GardeArret):
            rg.exiger_config({**jouet, k: v})
