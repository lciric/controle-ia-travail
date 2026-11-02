"""Rejeu à graine, repli « lot fidèle » (`runs_nuit.resolution_graine_lot_v1`), sur processeur, avec le modèle Llama
minuscule et le vrai tokeniseur de Llama 3.1 des essais du cœur (fixtures réutilisées).

1. Propriété clé : le lot fidèle, toutes lignes forcées à leurs jetons, redonne **au bit près** les logits de la
   génération originale du harnais (`jouer_episodes`, lots de 8 et de 4), pas après pas, ligne par ligne ; la mesure des
   lignes voisines exactes (B-L2) y vaut 1 exactement (cas sain) ; graine fausse sur une voisine → accord qui tombe,
   lecture « réserve » (artefact).
2. Cas sain : chaque épisode d'un lot de 8 (et de 4) est retrouvé par le lot fidèle, logits identiques, lecture
   « fidèle », forme exacte prouvée.
3. Lignes approchées (B-L1) : ligne approchée la plus longue du lot → mêmes bits après correction, pas où elle fixe la
   longueur remplie comptés ; même ligne avec un jeton de contexte de plus (forçage d'avant la correction) → bits
   différents, déclarés ; gardes de `forcee`.
4. Artefacts (R5) : lot recomposé, graine fausse, texte altéré (accords de la cible rapportés même non résolue) ; repli
   à une bascule et repli itératif à deux bascules dans deux actions ; budget de l'épisode → « non résolu : durée ».
5. Plan des lots ; gardes de configuration (cœur compris), cibles (C-6 refusé), unicité de l'étape (R3).
6. Bout en bout en mode jouet sur un P3 jouet : résolution-lot sur les non résolus d'un résultat du cœur, classe de la
   validation exigée et recopiée, épisodes consignés un à un, échéance de l'étape (non tenté), signal TERM (arrêt citant
   les épisodes consignés), texte attendu de l'ouverture, citation de la configuration ; table v3 fusionnée (cœur et
   lot), écrite et scellée ; refus : contrôle croisé non conforme, deux résultats différents, identifiants faux."""
import json
import time

import numpy as np
import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.harnais.episode import EnvironnementJouet, empreinte_episode, jouer_episodes
from controle_ia.manifeste import creer_manifeste, ecrire_resultat
from controle_ia.runs_nuit import resolution_graine_lot_v1 as rl
from controle_ia.runs_nuit import resolution_graine_v1 as rg
from controle_ia.scellement import sceller

from test_premier_test_ia_run import entropie_fixe  # noqa: F401  (fixture réutilisée)
from test_resolution_graine_v1 import FINS_P3, MAX, T, V, _config_graine, _modele_minuscule, fmt, tok  # noqa: F401
from test_runs_nuit_v1 import RUN_P3, source  # noqa: F401  (fixture réutilisée)
from test_runs_nuit_v2 import _table

LOT = {"episodes_resolution_lot": [], "combinaisons_max_lot": 6, "duree_max_episode_lot_s": 300,
       "duree_max_lot_s": 900, "seuil_lecture_lot": 0.99}


def _jouer_lot(modele, fmt, B: int, graine0: int):
    """Épisodes joués par le harnais en un lot de B ; gardés : textes, longueurs, graines, empreinte de trajectoire,
    identifiants vrais et empreintes des logits par pas (référence des essais, jamais disponibles pour P3)."""
    gr = [{(0, t): 1000 * b + 17 * t + 3 + graine0 for t in range(T)} for b in range(B)]
    sorties = jouer_episodes(modele, fmt, EnvironnementJouet(), [f"e{b}" for b in range(B)], 1, T, gr, [1],
                             max_nouveaux=MAX, empreinte_logits=True)
    eps = []
    for b, (ep, acts, rapport) in enumerate(sorties):
        actions = ep.transcriptions[0].actions
        eps.append({"identifiant": ep.identifiant, "textes": [a.texte for a in actions],
                    "jetons": [len(a.ids) for a in actions],
                    "jetons_notes": [len(a.ids) - (1 if a.ids and a.ids[-1] in fmt.fins else 0) for a in actions],
                    "graines": [gr[b][(0, t)] for t in range(T)], "empreinte": empreinte_episode(ep, acts)["trajectoire"],
                    "ids": [list(a.ids) for a in actions],
                    "empreintes_logits": [rapport["empreintes_logits"][f"0,{t}"] for t in range(T)]})
    return eps


@pytest.fixture(scope="module")
def jeu_lots(tok, fmt, tmp_path_factory):
    """Un seul fil de calcul (comme P3, `fils` = 1) pour la référence et les rejeux : avec plusieurs fils, le découpage
    des réductions sur processeur peut varier avec la charge de la machine et changer les bits (essai instable observé
    à quatre fils, machine partagée)."""
    fils = torch.get_num_threads()
    torch.set_num_threads(1)
    try:
        modele = _modele_minuscule(tok, tmp_path_factory.mktemp("llama-minuscule-lot"), avec_octets=False)
        yield modele, _jouer_lot(modele, fmt, 8, 0), _jouer_lot(modele, fmt, 4, 5)
    finally:
        torch.set_num_threads(fils)


def _lignes(eps, cible: int | None, ids=None, textes=None, jetons=None, graines=None):
    """Lignes du lot : toutes forcées à leurs identifiants vrais (exactes, munies de leurs graines), sauf la cible."""
    out = []
    for b, ep in enumerate(eps):
        c = b == cible
        out.append(rl.LigneLot(ep["identifiant"], EnvironnementJouet, textes if c and textes else ep["textes"],
                               jetons if c and jetons else ep["jetons"], ep["jetons_notes"],
                               None if c else [list(x) for x in (ids[b] if ids else ep["ids"])],
                               rl.SOURCE_CIBLE if c else "identique_base", True,
                               list((graines or {}).get(b, ep["graines"]))))
    return out


def _resoudre(modele, tok, fmt, eps, cible, lignes=None, moteur=None, textes=None, graines_=None, reference=True,
              **reglages):
    ep = eps[cible]
    voc = rg.Vocabulaire(tok, fmt.fins, V)
    Qs = [rg.tirages_exponentiels(g, n, V) for g, n in zip(graines_ or ep["graines"], ep["jetons"])]
    reg = rg.Reglages(max_nouveaux=MAX, **{"combinaisons_max": 8, **reglages})
    return rl.resoudre_episode_lot(moteur or rl.MoteurLot(modele), voc, fmt, lignes or _lignes(eps, cible, textes=textes),
                                   cible, T, Qs, ep["empreinte"], reg,
                                   reference_logits=ep["empreintes_logits"] if reference else None)


def _fin_defaut(fmt):
    return rl.fin_par_defaut(fmt, (EnvironnementJouet().consigne_privee(0), EnvironnementJouet().observation(0, 0, [])))


# ------------------------------------------------------------- 1. propriété clé : logits au bit près, mesure des voisines


def test_lot_fidele_force_redonne_les_logits_au_bit_et_mesure_des_voisines(tok, fmt, jeu_lots):
    modele, eps8, eps4 = jeu_lots
    voc = rg.Vocabulaire(tok, fmt.fins, V)
    reg = rg.Reglages(max_nouveaux=MAX)
    for eps in (eps8, eps4):
        moteur = rl.MoteurLot(modele)
        rec, trouves, plans = rl.rejouer_episode_lot(moteur, voc, fmt, _lignes(eps, None), None, T, None, reg)
        assert rec is None and trouves == [] and len(plans) == T
        for t in range(T):
            assert plans[t]["empreintes_logits"] == [ep["empreintes_logits"][t] for ep in eps]
            assert plans[t]["jetons_manquants"] == 0 and not plans[t]["L_fixee_par_approchee"]
        # autant de passes que le harnais : préremplissage plus (longueur de la plus longue ligne − 1) par pas
        assert moteur.passes == sum(max(ep["jetons"][t] for ep in eps) for t in range(T))
        # validation du lot, cas sain (B-L2) : lignes exactes, logits de P3 → accord 1 exactement, choix contraints
        # égaux, accord attendu sous graine indépendante plus bas ; lecture « fidèle »
        m = rl.mesure_des_voisines(plans, 0.99)
        assert m["pas"] == sum(sum(ep["jetons"]) for ep in eps)
        assert m["accord"] == 1.0 and m["egalite_contraints"] == 1.0 and m["hors_candidats"] == 0
        assert m["accord_attendu_graine_independante"] < 1.0 and m["lecture"] == rl.LECTURE_FIDELE
        assert all(x["accord"] == 1.0 for x in m["par_ligne"].values()) and len(m["par_ligne"]) == len(eps)
    # artefact : graine fausse sur une ligne voisine → son accord tombe (vers l'accord attendu), lecture « réserve » ;
    # les autres lignes restent à 1 (les logits ne changent pas : la mesure ne touche pas au lot)
    fausse = {2: [g + 1 for g in eps8[2]["graines"]]}
    _, _, plans = rl.rejouer_episode_lot(rl.MoteurLot(modele), voc, fmt, _lignes(eps8, None, graines=fausse), None, T,
                                         None, reg)
    assert plans[0]["empreintes_logits"] == [ep["empreintes_logits"][0] for ep in eps8]
    m = rl.mesure_des_voisines(plans, 0.99)
    assert m["lecture"] == rl.LECTURE_RESERVE
    assert m["par_ligne"]["e2"]["accord"] < 0.9 and all(v["accord"] == 1.0 for k, v in m["par_ligne"].items()
                                                        if k != "e2")
    assert abs(m["par_ligne"]["e2"]["accord"] - m["par_ligne"]["e2"]["accord_attendu_graine_independante"]) < 0.35
    assert rl.lecture_du_lot({"pas": 0}, 0.99) == rl.LECTURE_SANS
    # le même lot en une seule ligne (passe pleine du cœur ou lot de 1) ne donne pas ces bits
    _, _, plans1 = rl.rejouer_episode_lot(rl.MoteurLot(modele), voc, fmt, _lignes(eps8[:1], None), None, T, None, reg)
    assert plans1[0]["empreintes_logits"][0] != eps8[0]["empreintes_logits"][0]


# ------------------------------------------------------------------------------------------------------- 2. cas sain


def test_cas_sain_lot_de_8_et_de_4_retrouves(tok, fmt, jeu_lots):
    modele, eps8, eps4 = jeu_lots
    non_canoniques = 0
    for eps in (eps8, eps4):
        for b, ep in enumerate(eps):
            for t in range(T):
                notes = ep["ids"][t][:ep["jetons_notes"][t]]
                non_canoniques += list(tok(ep["textes"][t], add_special_tokens=False)["input_ids"]) != notes
            r = _resoudre(modele, tok, fmt, eps, b)
            assert r["statut"] == "resolu" and r["voie"] == "directe", r["cause"]
            assert r["ids"] == ep["ids"] and r["empreinte"] == ep["empreinte"]
            assert r["logits_conformes"] is True and r["empreintes_logits"] == ep["empreintes_logits"]
            assert rg.accord_non_contraint(r["pas"]) == 1.0 == rg.accord_non_contraint(r["pas"], ep["ids"])
            assert r["accord_cible"]["accord"] == 1.0 and r["accord_cible"]["pas"] == sum(ep["jetons"])
            assert all(x[5] > 0 for x in r["pas"]) and r["rang_dans_le_lot"] == b and r["lignes_approchees"] == 0
            assert [p["remplissage_cible"] for p in r["plans"]][0] == 0
            assert all(p["passes_decodage"] == ep["jetons"][t] - 1 for t, p in enumerate(r["plans"]))
            assert r["forme"]["forme_exacte_prouvee"] and r["forme"]["actions_jouees"] == T
            assert r["lecture_lot"] == rl.LECTURE_FIDELE and r["mesure_voisines"]["accord"] == 1.0
            assert r["mesure_voisines"]["egalite_contraints"] == 1.0
    assert non_canoniques >= 3


# ----------------------------------------------------------------------------------- 3. lignes approchées (B-L1)


def _ancienne_forcee(self, t, pad_id, fin_defaut, fins):
    """Forçage du commit 99022f43 (avant B-L1) : reconstruction tronquée ou complétée par `pad_id` à `jetons[t]`."""
    nv = [int(x) for x in self.ids[t]][:int(self.jetons[t])]
    return nv + [int(pad_id)] * (int(self.jetons[t]) - len(nv))


def _approchee_la_plus_longue(fmt, eps):
    """(cible, autre, t1, t) : la ligne `autre` est strictement la plus longue du lot à l'action t ≥ 1, toutes ses
    actions finies le sont par la fin par défaut, et son action t1 < t en a une, avec au moins deux jetons notés."""
    fd = _fin_defaut(fmt)
    for t in range(1, T):
        # longueurs de contexte à l'action t, calculées comme le harnais (transcription des identifiants vrais)
        lon = []
        for ep in eps:
            rec = rg.transcription(fmt, EnvironnementJouet(), T, ep["textes"], ep["ids"], ep["jetons"], ep["jetons_notes"])
            lon.append(rec["actions"][t]["debut"])
        b = max(range(len(eps)), key=lambda k: lon[k])
        if sorted(lon)[-1] == sorted(lon)[-2]:
            continue
        ep = eps[b]
        if any(ep["jetons"][k] - ep["jetons_notes"][k] == 1 and ep["ids"][k][-1] != fd for k in range(T)):
            continue                                    # une vraie fin autre que la fin par défaut : hors de ce cas
        for t1 in range(t):
            if ep["jetons"][t1] - ep["jetons_notes"][t1] == 1 and ep["jetons_notes"][t1] >= 2:
                cible = 0 if b != 0 else 1
                return cible, b, t1, t
    return None


def test_ligne_approchee_la_plus_longue_memes_bits_apres_correction(tok, fmt, jeu_lots, monkeypatch):
    """B-L1. Une ligne voisine approchée (identifiants à un jeton noté de moins à l'action t1, comme un découpage
    canonique plus court) qui est la plus longue du lot à l'action t : après correction (`forcee` : notes complétées au
    nombre de jetons notés, puis la fin par défaut), la longueur de son contexte est celle de P3, les logits de la cible
    sont ceux de P3 au bit près, et le pas où elle fixe la longueur remplie est compté (forme non prouvée, déclarée).
    Artefact : l'ancien forçage (dernier jeton = remplissage, clôture entière) donne un jeton de contexte de plus → bits
    différents dès l'action t, détectés et déclarés."""
    modele, eps8, eps4 = jeu_lots
    eps, trouve = next(((x, y) for x in (eps8, eps4) for y in [_approchee_la_plus_longue(fmt, x)] if y), (None, None))
    assert trouve is not None
    cible, autre, t1, t = trouve
    fd = _fin_defaut(fmt)
    ids = [list(x) for x in eps[autre]["ids"]]
    ids[t1] = ids[t1][:eps[autre]["jetons_notes"][t1] - 1] + [fd]          # un jeton noté de moins, fin par défaut
    lignes = _lignes(eps, cible)
    lignes[autre] = rl.LigneLot(eps[autre]["identifiant"], EnvironnementJouet, eps[autre]["textes"], eps[autre]["jetons"],
                                eps[autre]["jetons_notes"], ids, rl.SOURCE_APPROCHEE, False, list(eps[autre]["graines"]))
    pad = rl.pad_du_format(fmt)
    assert len(lignes[autre].forcee(t1, pad, fd, set(fmt.fins))) == eps[autre]["jetons"][t1]
    assert lignes[autre].forcee(t1, pad, fd, set(fmt.fins))[-1] == fd
    r = _resoudre(modele, tok, fmt, eps, cible, lignes=lignes)
    assert r["statut"] == "resolu" and r["ids"] == eps[cible]["ids"] and r["logits_conformes"] is True
    assert r["lignes_approchees"] == 1 and r["lot"][autre]["source"] == rl.SOURCE_APPROCHEE
    assert r["forme"]["pas_L_fixee_par_approchee"] >= 1 and r["forme"]["forme_exacte_prouvee"] is False
    assert r["plans"][t]["L_fixee_par_approchee"]
    # la ligne approchée n'est pas mesurée ; les autres voisines exactes le sont, accord 1
    assert eps[autre]["identifiant"] not in r["mesure_voisines"]["par_ligne"] and r["mesure_voisines"]["accord"] == 1.0
    # artefact : l'ancien forçage, un jeton de contexte en plus à l'action t → longueur remplie + 1, bits différents
    monkeypatch.setattr(rl.LigneLot, "forcee", _ancienne_forcee)
    a = _resoudre(modele, tok, fmt, eps, cible, lignes=lignes)
    assert a["logits_conformes"] is False
    assert a["plans"][t]["longueur_remplie"] == r["plans"][t]["longueur_remplie"] + 1
    assert a["empreintes_logits"][t] != eps[cible]["empreintes_logits"][t]
    assert a["empreintes_logits"][:t1 + 1] == eps[cible]["empreintes_logits"][:t1 + 1]
    assert a["forme"]["pas_L_fixee_par_approchee"] >= 1 and a["forme"]["forme_exacte_prouvee"] is False


def test_gardes_du_forcage_des_lignes():
    fd, pad, fins = 9, 5, {7, 9}
    sain = rl.LigneLot("x", None, ["a"], [4], [3], [[1, 2, 9]], rl.SOURCE_APPROCHEE, False)
    assert sain.forcee(0, pad, fd, fins) == [1, 2, pad, fd]
    long_ = rl.LigneLot("x", None, ["a"], [3], [2], [[1, 2, 3, 4, 9]], rl.SOURCE_APPROCHEE, False)
    assert long_.forcee(0, pad, fd, fins) == [1, 2, fd]
    sans_fin = rl.LigneLot("x", None, ["a"], [3], [3], [[1]], rl.SOURCE_APPROCHEE, False)
    assert sans_fin.forcee(0, pad, fd, fins) == [1, pad, pad]
    with pytest.raises(GardeArret, match="clôture"):
        sans_fin.forcee(0, fd, fd, fins)                    # complétée par la fin par défaut : clôture plus courte
    exacte = rl.LigneLot("x", None, ["a"], [3], [2], [[1, 2, 9]], "identique_base", True)
    assert exacte.forcee(0, pad, fd, fins) == [1, 2, 9]
    with pytest.raises(GardeArret, match="ligne exacte"):
        rl.LigneLot("x", None, ["a"], [4], [3], [[1, 2, 9]], "identique_base", True).forcee(0, pad, fd, fins)
    with pytest.raises(GardeArret, match="jetons − jetons notés"):
        rl.LigneLot("x", None, ["a"], [5], [3], [[1]], rl.SOURCE_APPROCHEE, False).forcee(0, pad, fd, fins)
    assert rl.forme_du_pas([10, 12, 11], [False, True, False]) == {"L_fixee_par_approchee": True,
                                                                  "L_a_un_jeton_d_une_approchee": True}
    assert rl.forme_du_pas([12, 12, 10], [False, True, False]) == {"L_fixee_par_approchee": False,
                                                                  "L_a_un_jeton_d_une_approchee": True}
    assert rl.forme_du_pas([12, 11], [False, True]) == {"L_fixee_par_approchee": False,
                                                       "L_a_un_jeton_d_une_approchee": False}
    assert rl.forme_du_pas([12, 11], [False, False]) == {"L_fixee_par_approchee": False,
                                                        "L_a_un_jeton_d_une_approchee": False}


# ------------------------------------------------------------------------------------------------------ 4. artefacts


def test_artefact_lot_recompose_logits_differents_declares(tok, fmt, jeu_lots):
    modele, eps8, _ = jeu_lots
    cible = 0
    # une autre ligne du lot (contexte plus long : 40 jetons de plus à sa première action) : le remplissage change,
    # les logits de la cible aussi, dès le deuxième pas ; détecté par les empreintes, déclaré
    autre = 3
    ab = tok.convert_tokens_to_ids("ab")
    ids = [[list(x) for x in ep["ids"]] for ep in eps8]
    ids[autre][0] = [ab] * 40 + ids[autre][0]
    lignes = _lignes(eps8, cible, ids=ids)
    lignes[autre].jetons = [eps8[autre]["jetons"][0] + 40] + eps8[autre]["jetons"][1:]
    r = _resoudre(modele, tok, fmt, eps8, cible, lignes=lignes)
    assert r["logits_conformes"] is False
    assert r["empreintes_logits"][0] == eps8[cible]["empreintes_logits"][0]
    assert any(a != b for a, b in zip(r["empreintes_logits"][1:], eps8[cible]["empreintes_logits"][1:]))
    assert r["plans"][1]["longueur_remplie"] > eps8[cible]["jetons"][0] + len(fmt.ouverture("", ""))
    assert r["mesure_voisines"]["hors_candidats"] >= 1 and r["lecture_lot"] == rl.LECTURE_RESERVE
    # ordre des lignes permuté, mêmes contextes : mêmes bits (chaque ligne ne dépend des autres que par la forme du lot)
    perm = [3, 1, 0, 7, 5, 6, 2, 4]
    eps_p = [eps8[b] for b in perm]
    r = _resoudre(modele, tok, fmt, eps_p, perm.index(cible))
    assert r["statut"] == "resolu" and r["logits_conformes"] is True and r["ids"] == eps8[cible]["ids"]
    # lot de 7 lignes (la cible retirée d'un autre lot) : forme différente, déclarée par les plans
    r7 = _resoudre(modele, tok, fmt, eps8[:7], 1)
    assert len(r7["lot"]) == 7 and r7["statut"] == "resolu"


def test_artefacts_graine_fausse_et_texte_altere(tok, fmt, jeu_lots):
    modele, eps8, _ = jeu_lots
    cible = max(range(8), key=lambda b: sum(eps8[b]["jetons"]))
    ep = eps8[cible]
    assert _resoudre(modele, tok, fmt, eps8, cible)["statut"] == "resolu"
    fausses = list(ep["graines"])
    fausses[1] += 1
    r = _resoudre(modele, tok, fmt, eps8, cible, graines_=fausses)
    assert r["statut"] == "non_resolu" and r["ids"] is None and r["cause"]
    # accords de la cible rapportés même non résolue (I-D) : sous 0,9, accord attendu sous graine indépendante écrit
    assert rg.accord_non_contraint(r["pas"]) < 0.9 and r["accord_cible"]["accord"] < 0.9
    assert 0 < r["accord_cible"]["accord_attendu_graine_independante"] < 1 and r["accord_cible"]["pas"] == len(r["pas"])
    # la cible est fausse, les voisines restent exactes : lecture du lot « fidèle » (la mesure ne dépend pas de la cible)
    assert r["mesure_voisines"]["accord"] == 1.0
    t = max(range(T), key=lambda k: len(ep["textes"][k]))
    x = ep["textes"][t]
    k = next(i for i in range(len(x) // 2, len(x)) if x[i].isalpha())
    alt = list(ep["textes"])
    alt[t] = x[:k] + ("q" if x[k] != "q" else "z") + x[k + 1:]
    assert len(alt[t].encode()) == len(x.encode()) and alt[t] != x
    r = _resoudre(modele, tok, fmt, eps8, cible, textes=alt)
    assert r["statut"] == "non_resolu" and r["ids"] is None


class _PerturbeLot(rl.MoteurLot):
    """Artefact : à chaque position (t0, s0) choisie de la ligne cible, quand son contexte est exactement le vrai, le
    logit du faux candidat passe devant le vrai d'un écart de 0,1 (quasi-égalité retournée)."""

    def __init__(self, modele, cible, perts):
        super().__init__(modele)
        self.cible, self.perts, self.ctx = cible, perts, []

    def preremplir(self, ids, masque, positions):
        r = self.cible
        self.ctx = [int(x) for x, m in zip(ids[r].tolist(), masque[r].tolist()) if m]
        return super().preremplir(ids, masque, positions)

    def pas(self, jetons, masque, positions, sortie):
        self.ctx.append(int(jetons[self.cible, 0]))
        return super().pas(jetons, masque, positions, sortie)

    def logits_cpu(self, sortie):
        L = super().logits_cpu(sortie)
        for prefixe, vrai, faux, Q in self.perts:
            if self.ctx == prefixe:
                L[self.cible, faux] = float(L[self.cible, vrai]) - float(torch.log(Q[vrai])) \
                    + float(torch.log(Q[faux])) + 0.1
        return L


def _perts(fmt, ep, choisis):
    rec = rg.transcription(fmt, EnvironnementJouet(), T, ep["textes"], ep["ids"], ep["jetons"], ep["jetons_notes"])
    out = []
    for (t0, s0, vrai, faux) in choisis:
        prefixe = rec["ids"][:rec["actions"][t0]["debut"]] + ep["ids"][t0][:s0]
        Q = rg.tirages_exponentiels(ep["graines"][t0], ep["jetons"][t0], V)[s0].double()
        out.append((prefixe, vrai, faux, Q))
    return out


def _quasi(ep, sain):
    par_t = {}
    for x in sain["pas"]:
        t, s, vrai, _, n, _, faux = x[:7]
        if n > 1 and faux not in FINS_P3 and faux < 128000 and s < ep["jetons_notes"][t] - 1:
            par_t.setdefault(t, []).append((t, s, vrai, faux))
    return par_t


def test_repli_une_bascule_puis_iteratif_deux_bascules_dans_le_lot(tok, fmt, jeu_lots):
    """Repli (règle du cœur au commit 755959e1, recopiée) : une quasi-égalité basculée (cas sain), et non résolu
    déclaré sous un seuil trop bas ; deux erreurs dans deux actions, la seconde révélée par le rejeu de la première
    seulement → résolu par deux bascules ; à une seule bascule permise : non résolu, cause écrite."""
    modele, eps8, _ = jeu_lots
    cible = max(range(8), key=lambda b: sum(eps8[b]["jetons"]))
    ep = eps8[cible]
    sain = _resoudre(modele, tok, fmt, eps8, cible)
    par_t = _quasi(ep, sain)
    a = next(iter(par_t.get(1) or par_t[0]))
    r = _resoudre(modele, tok, fmt, eps8, cible, lignes=None, moteur=_PerturbeLot(modele, cible, _perts(fmt, ep, [a])))
    assert r["statut"] == "resolu" and r["voie"] == "repli" and r["ids"] == ep["ids"], r["cause"]
    assert [(f["pas"], f["rang"], f["jeton"]) for f in r["forcages"]] == [(a[0], a[1], a[2])]
    assert r["ids_directs"][a[0]][a[1]] == a[3] and r["logits_conformes"] is False
    assert all(p["empreinte_logits_cible"] for p in r["plans"]) and r["repli"]["par_niveau"] == {"1": 1}
    r = _resoudre(modele, tok, fmt, eps8, cible, moteur=_PerturbeLot(modele, cible, _perts(fmt, ep, [a])),
                  seuil_ecart=0.05)
    assert r["statut"] == "non_resolu" and "repli" in r["cause"]
    assert all((q["pas"], q["rang"]) != (a[0], a[1]) for q in r["quasi_egalites"])
    # deux bascules dans deux actions (la seconde n'apparaît que sur le chemin rejoué après la première)
    assert par_t.get(1) and par_t.get(2)
    b1, b2 = par_t[1][0], par_t[2][0]
    P = _PerturbeLot(modele, cible, _perts(fmt, ep, [b1, b2]))
    r = _resoudre(modele, tok, fmt, eps8, cible, moteur=P, combinaisons_max=136, quasi_egalites_max=16)
    assert r["statut"] == "resolu" and r["voie"] == "repli" and r["ids"] == ep["ids"], r["cause"]
    assert [(f["pas"], f["rang"], f["jeton"]) for f in r["forcages"]] == [b1[:3], b2[:3]]
    assert r["repli"]["par_niveau"].get("2", 0) >= 1
    assert (b2[0], b2[1], b2[3]) not in {(q["pas"], q["rang"], q["choix"]) for q in r["quasi_egalites"]}
    r1 = _resoudre(modele, tok, fmt, eps8, cible, moteur=_PerturbeLot(modele, cible, _perts(fmt, ep, [b1, b2])),
                   combinaisons_max=136, quasi_egalites_max=16, bascules_max=1)
    assert r1["statut"] == "non_resolu" and r1["ids"] is None and "repli itératif" in r1["cause"]


def test_budget_de_l_episode_non_resolu_duree(tok, fmt, jeu_lots, monkeypatch):
    """Budget par épisode (C-1 pour le lot) : épuisé au milieu d'un essai → « non résolu », cause « durée », sans
    exception ; budget suffisant → résolu (cas sain) ; pendant le repli → « durée », combinaisons comptées."""
    modele, eps8, _ = jeu_lots
    cible = max(range(8), key=lambda b: sum(eps8[b]["jetons"]))
    ep = eps8[cible]
    decalage = [0.0]
    monkeypatch.setattr(rg, "horloge", lambda: time.perf_counter() + decalage[0])

    class Lent(rl.MoteurLot):
        def logits_cpu(self, sortie):
            decalage[0] += 10.0
            return super().logits_cpu(sortie)

    sain = _resoudre(modele, tok, fmt, eps8, cible, moteur=Lent(modele), duree_episode_s=1e6)
    assert sain["statut"] == "resolu" and not sain["duree_epuisee"]
    r = _resoudre(modele, tok, fmt, eps8, cible, moteur=Lent(modele), duree_episode_s=55.0)
    assert r["statut"] == "non_resolu" and r["duree_epuisee"] and r["cause"].startswith("durée")
    assert r["ids"] is None and 0 < r["accord_cible"]["pas"] < sain["accord_cible"]["pas"]
    a = next(iter(_quasi(ep, sain).get(1)))

    class LentPerturbe(_PerturbeLot):
        def logits_cpu(self, sortie):
            decalage[0] += 10.0
            return super().logits_cpu(sortie)

    direct = _resoudre(modele, tok, fmt, eps8, cible, moteur=LentPerturbe(modele, cible, _perts(fmt, ep, [a])),
                       duree_episode_s=1e6)
    assert direct["voie"] == "repli"
    n_pas = sum(ep["jetons"])
    r = _resoudre(modele, tok, fmt, eps8, cible, moteur=LentPerturbe(modele, cible, _perts(fmt, ep, [a])),
                  duree_episode_s=10.0 * n_pas + 5, quasi_egalites_max=16)
    assert r["statut"] == "non_resolu" and r["duree_epuisee"] and "durée" in r["cause"]


# ----------------------------------------------------------------------- 5. plan des lots, configuration, cibles, R3


def test_plan_des_lots_reconstruit_et_verifie():
    from controle_ia.premier_test_ia.run import plan_p3

    taches = [{"identifiant": f"25{k:02d}.00001v1", "questions": "q"} for k in range(5)]
    plan = [e for e, _, _ in plan_p3(taches)]
    assert len(plan) == 20 and plan[:4] == [f"{c}/2500.00001v1/e0" for c in ("honnete", "saboteur", "temoin", "mention")]
    lignes = [{"episode": e, "pas": t} for e in plan for t in range(3)]
    lots = rl.plan_des_lots(taches, 8, lignes)
    assert [len(x) for x in lots] == [8, 8, 4] and lots[0] == plan[:8] and lots[2] == plan[16:]
    assert rl.lot_de(lots, plan[9]) == (1, plan[8:16], 1)
    with pytest.raises(GardeArret, match="plan des lots ≠ ordre des textes"):
        rl.plan_des_lots(taches[::-1], 8, lignes)
    with pytest.raises(GardeArret, match="plusieurs morceaux"):
        rl.plan_des_lots(taches, 8, lignes[:1] + lignes[3:6] + lignes[1:3] + lignes[6:])
    with pytest.raises(GardeArret, match="premier écart au rang 0"):
        rl.plan_des_lots(taches, 8, lignes[3:] + lignes[:3])
    with pytest.raises(GardeArret, match="taille de lot"):
        rl.plan_des_lots(taches, 0, lignes)
    with pytest.raises(GardeArret, match="absent du plan"):
        rl.lot_de(lots, "x/y/e0")


def test_configuration_gardes_cibles_et_unicite(tmp_path):
    from types import SimpleNamespace

    base = {k: None for k in rg.CLES_COMPLETES}
    base.update(mode="jouet", T=10, max_nouveaux=400, fils=1, fils_tirages=8, episodes_d_avance=2, quasi_egalites_max=16,
                bascules_max=2, combinaisons_max=136, combinaisons_max_validation=136, balayages_max=64,
                seuil_validation=147, temperature=1.0, seuil_ecart=1.0, duree_max_s=2400, duree_max_episode_s=600,
                episodes_resolution=["a"], noyau_attention="defaut")
    with pytest.raises(GardeArret, match="incomplète"):
        rl.exiger_config(base)
    lot = {**base, **LOT}
    rl.exiger_config(lot)
    for k, v, motif in (("combinaisons_max_lot", -1, "combinaisons_max_lot"),
                        ("seuil_lecture_lot", 1.5, "seuil_lecture_lot"), ("seuil_lecture_lot", True, "nombre"),
                        ("duree_max_episode_lot_s", 0, "duree_max_episode_lot_s"),
                        ("duree_max_episode_lot_s", 1000, "duree_max_episode_lot_s"),
                        ("episodes_resolution_lot", ["a", "a"], "sans doublon"), ("temperature", 0.0, "température"),
                        # gardes du cœur (rg.exiger_reglages_execution) : noyau, paires, budget par épisode du cœur
                        ("noyau_attention", "flash", "noyau_attention"),
                        ("combinaisons_max_validation", 16, "paires"), ("duree_max_episode_s", 0, "duree_max_episode_s")):
        with pytest.raises(GardeArret, match=motif):
            rl.exiger_config({**lot, k: v})
    with pytest.raises(GardeArret, match="incomplète"):
        rl.exiger_config({k: v for k, v in lot.items() if k != "duree_max_episode_s"})
    with pytest.raises(GardeArret, match="noyau"):
        rl.exiger_meme_lot_que_p3({"noyau_attention": "math"}, {"config": {"lot": 8, "noyau_attention": "defaut"}})
    with pytest.raises(GardeArret, match="taille de lot"):
        rl.exiger_meme_lot_que_p3({"noyau_attention": "defaut"}, {"config": {}})
    assert rl.exiger_meme_lot_que_p3({"noyau_attention": "defaut"}, {"config": {"lot": 8}}) == 8
    # cibles (B-L2, R2-05) : non résolus du cœur à entrée « non_resolu » de la table v2 ; un épisode de C-6 non résolu
    # par le cœur n'est pas une cible (cité hors cibles, cause écrite ; demandé nommément : refusé)
    pieces = SimpleNamespace(par_episode={"a": [0], "b": [1], "c": [2], "d": [3]}, table={"episodes": [
        {"episode": "a", "methode": "non_resolu"}, {"episode": "b", "methode": "deux_paires"},
        {"episode": "c", "methode": "non_resolu"}]})
    cibles, hors = rl.cibles_du_lot(lot, pieces, ["a", "b", "c"])
    assert cibles == ["a", "c"] and hors == [{"episode": "b", "cause": hors[0]["cause"]}] and "C-6" in hors[0]["cause"]
    assert rl.cibles_du_lot({**lot, "episodes_resolution_lot": ["c"]}, pieces, ["a", "b", "c"])[0] == ["c"]
    with pytest.raises(GardeArret, match="C-6"):
        rl.cibles_du_lot({**lot, "episodes_resolution_lot": ["b"]}, pieces, ["a", "b", "c"])
    with pytest.raises(GardeArret, match="résolus par le cœur"):
        rl.cibles_du_lot({**lot, "episodes_resolution_lot": ["d"]}, pieces, ["a", "b", "c"])
    with pytest.raises(GardeArret, match="aucune cible"):
        rl.cibles_du_lot(lot, pieces, ["b"])
    # R3 : une seule exécution de l'étape par configuration
    (tmp_path / "runs" / "x").mkdir(parents=True)
    rl.exiger_execution_unique(tmp_path, lot, rl.ETAPE_LOT)
    (tmp_path / "runs" / "x" / "manifeste.json").write_text(json.dumps(
        {"run_id": "x", "commande": f"{rl.COMMANDE} --etape {rl.ETAPE_LOT}",
         "config_sha256": rg.empreinte_config({**lot, "seuil_lecture_lot": 0.5})}), encoding="utf-8")
    rl.exiger_execution_unique(tmp_path, lot, rl.ETAPE_LOT)              # autre configuration : permis
    (tmp_path / "runs" / "y").mkdir()
    (tmp_path / "runs" / "y" / "manifeste.json").write_text(json.dumps(
        {"run_id": "y", "commande": f"{rl.COMMANDE} --etape {rl.ETAPE_LOT}", "config_sha256": rg.empreinte_config(lot)}),
        encoding="utf-8")
    with pytest.raises(GardeArret, match="R3"):
        rl.exiger_execution_unique(tmp_path, lot, rl.ETAPE_LOT)
    # ligne de commande : étape « table-lot » déclarée (arguments obligatoires), étape « validation-lot » retirée
    cfg = tmp_path / "config-lot.json"
    cfg.write_text(json.dumps(lot), encoding="utf-8")
    sceller(cfg)
    with pytest.raises(GardeArret, match="obligatoires"):
        rl._main(["--etape", rl.ETAPE_TABLE, "--config", str(cfg), "--resolution", "r.json"])
    with pytest.raises(SystemExit):
        rl._main(["--etape", "validation-lot", "--config", str(cfg)])


# --------------------------------------------------------------------------------------- 6. bout en bout (P3 jouet)


def _preparer(source, tmp_path):
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
    assert connus and len(autres) >= 2, (len(connus), len(autres))
    table = json.loads((tmp_path / "table0.json").read_text(encoding="utf-8"))
    table["episodes"] += [{"episode": e, "methode": "non_resolu", "trajectoire_p3": pieces0.fiches[e]["trajectoire"],
                           "fins": {}, "paires": [], "essais": {}} for e in autres]
    table["comptes"]["non_resolu"] = table["comptes"].get("non_resolu", 0) + len(autres)
    tp = tmp_path / "table-jouet-v2.json"
    tp.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(tp)
    committer(depot)
    return depot, f, c, tp, pieces0, fmt_j, cl, connus, autres


def _coeur(depot, conf, horodatage, non_resolus, resolus, fiches, classe="graines validées", controle="conforme"):
    """Résultats scellés du cœur, jouets (même configuration du cœur) : validation (avec ou sans `classe_validation`)
    et résolution (`controle_croise_lecture`), comme les écrit `resolution_graine_v1`."""
    from conftest import committer

    chemins = []
    for nom, etape, contenu in (
            ("validation", "validation", {"etape": "validation", "version": rg.VERSION, "lecture": "atteint",
                                          **({rl.CLE_CLASSE: classe} if classe else {})}),
            ("resolution", "resolution", {
                "etape": "resolution", "version": rg.VERSION, "lecture": "partielle",
                "controle_croise_lecture": controle,
                "non_resolus": [{"episode": e, "cause": "jouet"} for e in non_resolus],
                "episodes": [{"episode": e, "statut": "resolu", "ids": ids, "voie": "directe", "forcages": [],
                              "empreinte": fiches[e]["trajectoire"], "empreinte_cible": fiches[e]["trajectoire"]}
                             for e, ids in resolus.items()]
                            + [{"episode": e, "statut": "non_resolu", "ids": None} for e in non_resolus]})):
        run = f"{horodatage}-graine-{nom}-jouet"
        m, _ = creer_manifeste(depot, run, conf, ["aucun-tirage-propre"], entropie=3, autoriser_depot_sale=True,
                               commande=f"{rg.COMMANDE} --etape {etape}")
        chemins.append(ecrire_resultat(depot, m, f"resolution-graine-{etape}", contenu))
    committer(depot)
    return [str(x) for x in chemins]


def _faux_lot(depot, conf, run, sha_r, episodes):
    from conftest import committer

    m, _ = creer_manifeste(depot, run, conf, ["aucun-tirage-propre"], entropie=3, autoriser_depot_sale=True,
                           commande=f"{rl.COMMANDE} --etape faux")
    ch = ecrire_resultat(depot, m, "resolution-graine-resolution-lot", {
        "etape": rl.ETAPE_LOT, "version": rl.VERSION, "resolution_v1": {"sha256": sha_r}, rl.CLE_CLASSE: "graines validées",
        "lecture_lot": rl.LECTURE_FIDELE, "episodes": episodes})
    committer(depot)
    return str(ch)


def test_bout_en_bout_jouet_resolution_lot_puis_table_v3(source, tmp_path, monkeypatch):
    from controle_ia import gardes
    from controle_ia.scellement import verifier

    depot, f, c, tp, pieces0, fmt_j, cl, connus, autres = _preparer(source, tmp_path)
    T_ = int(c["T"])
    conf = {**_config_graine(depot, f, c, tp, autres, seuil_validation=len(connus)), **LOT}
    fiches = pieces0.fiches
    ch_v, ch_r1 = _coeur(depot, conf, "20261102-120000", autres, {}, fiches)
    # plan des lots de ce P3 jouet : deux lots de quatre (deux tâches × quatre conditions), comme son code
    from controle_ia.environnements.pilote_a import charger_taches

    assert [len(x) for x in rl.plan_des_lots(charger_taches(f), int(pieces0.manifeste_p3["config"]["lot"]),
                                             pieces0.lignes)] == [4, 4]
    # gardes avant tout calcul : noyau autre que celui de P3 ; validation absente ; validation sans classe (I-B)
    with pytest.raises(GardeArret, match="noyau"):
        rl.executer({**conf, "noyau_attention": "defaut"}, depot, "20261102-120050-graine-lot-jouet", None,
                    rl.ETAPE_LOT, ch_v, ch_r1, autoriser_depot_sale=True, entropie_essai=3)
    with pytest.raises(GardeArret, match="validation du cœur est obligatoire"):
        rl.executer(conf, depot, "20261102-120100-graine-lot-jouet", None, rl.ETAPE_LOT, None, ch_r1,
                    autoriser_depot_sale=True, entropie_essai=3)
    ch_v_sans, _ = _coeur(depot, conf, "20261102-120110", autres, {}, fiches, classe=None)
    with pytest.raises(GardeArret, match="classe_validation"):
        rl.executer(conf, depot, "20261102-120120-graine-lot-jouet", None, rl.ETAPE_LOT, ch_v_sans, ch_r1,
                    autoriser_depot_sale=True, entropie_essai=3)
    # citation de la configuration du lot dans le préenregistrement : absente → arrêt ; présente → la garde passe (la
    # suivante, l'entropie, arrête ce texte d'essai)
    (depot / "prereg").mkdir(exist_ok=True)
    pr = depot / "prereg" / "essai-lot.md"                    # hors de l'arbre gelé (le dépôt jouet est tmp_path)
    pr.write_text("texte sans citation\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="ne cite pas la configuration du lot"):
        rl.executer(conf, depot, "20261102-120130-graine-lot-jouet", str(pr), rl.ETAPE_LOT, ch_v, ch_r1,
                    autoriser_depot_sale=True)
    pr.write_text(rl.CONFIG_CITEE.format(rg.empreinte_config(conf)) + "\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="entropie"):
        rl.executer(conf, depot, "20261102-120140-graine-lot-jouet", str(pr), rl.ETAPE_LOT, ch_v, ch_r1,
                    autoriser_depot_sale=True)
    assert not (depot / "runs" / "20261102-120140-graine-lot-jouet").exists()
    # étape « resolution-lot »
    r = rl.executer(conf, depot, "20261102-120200-graine-lot-jouet", None, rl.ETAPE_LOT, ch_v, ch_r1,
                    autoriser_depot_sale=True, entropie_essai=3)
    from conftest import committer

    committer(depot)
    assert r["lecture"] == "complète" and r["non_resolus_v1"] == autres and sorted(r["cibles"]) == sorted(autres)
    assert r["hors_cibles"] == [] and r[rl.CLE_CLASSE] == "graines validées"
    assert r["lecture_validation"] == {rl.CLE_CLASSE: "graines validées", "lecture_validation_coeur": "atteint",
                                       "lecture_lot": r["lecture_lot"]}
    assert r["resolution_v1"]["sha256"] == verifier(ch_r1) and r["validation"]["sha256"] == verifier(ch_v)
    assert all(x["empreinte_retrouvee"] and x["ids"] and x["base_nv"] != x["ids"] for x in r["episodes"])
    assert all(x[rl.CLE_CLASSE] == "graines validées" for x in r["episodes"])
    for x in r["episodes"]:
        m = x["mesure_voisines"]
        exactes = [y for y in x["lot"] if y["exacte"] and y["source"] != rl.SOURCE_CIBLE]
        assert (m["pas"] > 0) == bool(exactes) and m["hors_candidats"] == 0, x["episode"]
        assert set(m["par_ligne"]) == {y["episode"] for y in exactes}
        if not exactes:
            assert x["lecture_lot"] == rl.LECTURE_SANS                 # lot sans voisine exacte : déclaré, non lu
        elif x["forme"]["forme_exacte_prouvee"]:
            assert m["accord"] == 1.0 and m["egalite_contraints"] == 1.0 and x["lecture_lot"] == rl.LECTURE_FIDELE
        assert x["accord_cible"]["accord"] == 1.0
    sources = {y["source"] for x in r["episodes"] for y in x["lot"]}
    assert rl.SOURCE_CIBLE in sources and sources <= {rl.SOURCE_CIBLE, "identique_base", "lot_fidele",
                                                      rl.SOURCE_APPROCHEE} | {f"table:{m}" for m in rg.METHODES_V3}
    assert all(y["exacte"] for x in r["episodes"] for y in x["lot"] if y["source"] != rl.SOURCE_APPROCHEE)
    d = depot / "diag" / "20261102-120200-graine-lot-jouet"
    chemin_lot = d / "resolution-graine-resolution-lot.json"
    assert chemin_lot.exists() and (d / "resolution-graine-resolution-lot.json.sha256").exists()
    assert [x["fichier"] for x in r["episodes_consignes"]] == [f"episodes-resolution-lot/{k:03d}.json"
                                                               for k in range(len(autres))]
    for x in r["episodes_consignes"]:
        assert (d / (x["fichier"] + ".sha256")).exists()
        corps = json.loads((d / x["fichier"]).read_text(encoding="utf-8"))
        assert corps["statut"] == "resolu" and corps[rl.CLE_CLASSE] == "graines validées"
    with np.load(d / r["pas_fichier"]) as z:
        assert len(z["choix"]) == sum(x["pas"] for x in r["episodes"]) and len(z["p_choix"]) == len(z["choix"])
    # R3 : une seconde exécution sous la même configuration est refusée avant tout calcul
    with pytest.raises(GardeArret, match="R3"):
        rl.executer(conf, depot, "20261102-120250-graine-lot-jouet", None, rl.ETAPE_LOT, ch_v, ch_r1,
                    autoriser_depot_sale=True, entropie_essai=3)
    # un résultat du cœur qui cite un des « autres » résolu : ligne « resolution_v1 », revérifiée par l'empreinte, dans
    # les lots des autres cibles ; identifiants faux refusés
    e1, ids1 = r["episodes"][0]["episode"], r["episodes"][0]["ids"]
    faux = [list(a) for a in ids1]
    faux[0] = faux[0][::-1] if len(faux[0]) > 1 else faux[0] + faux[0]
    with pytest.raises(GardeArret, match="empreinte de P3"):
        rl.connus_de_la_v1(pieces0, fmt_j, T_, {e1: faux})
    assert rl.connus_de_la_v1(pieces0, fmt_j, T_, {e1: ids1}) == {e1: (ids1, "resolution_v1")}
    reste = [e for e in autres if e != e1]
    ch_v2, ch_r2 = _coeur(depot, conf, "20261102-120300", reste, {e1: ids1}, fiches)
    r2 = rl.executer({**conf, "episodes_resolution_lot": reste}, depot, "20261102-120400-graine-lot-jouet", None,
                     rl.ETAPE_LOT, ch_v2, ch_r2, autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    assert r2["lecture"] == "complète" and [x["episode"] for x in r2["episodes"]] == reste
    assert {x["episode"]: x["ids"] for x in r2["episodes"]} == {x["episode"]: x["ids"] for x in r["episodes"]
                                                                if x["episode"] in reste}
    assert any(y["source"] == "resolution_v1" and y["episode"] == e1 for x in r2["episodes"] for y in x["lot"])

    # ---- table v3 fusionnée : cœur (rien de résolu ici) et lot ; chaque entrée revérifiée par l'empreinte de P3
    t3 = rl.construire_table_v3_lot(conf, depot, None, ch_r1, str(chemin_lot), fmt=fmt_j)
    assert t3["version"] == 3 and t3["comptes"]["identifiants"] == len(autres) and t3["comptes"]["non_resolu"] == 0
    assert sorted(t3["episodes_verses_par_le_lot"]) == sorted(autres) and t3["non_resolus_apres_lot"] == []
    assert t3["lecture_validation"][rl.CLE_CLASSE] == "graines validées"
    assert t3["resultat_lot_sha256"] == verifier(chemin_lot) and t3["resultat_graine_sha256"] == verifier(ch_r1)
    assert all(x["resolution_graine"]["voie"].startswith("lot_fidele") and
               x["resolution_graine"][rl.CLE_CLASSE] == "graines validées"
               for x in t3["episodes"] if x["episode"] in autres)
    sortie = depot / "prereg" / "table-v3-lot.json"
    sha = rg.ecrire_table_v3(t3, sortie)
    assert verifier(sortie) == sha and rg.charger_table_v3(sortie, sha)["version"] == 3
    # cœur et lot ensemble : e1 résolu par le cœur (r2 du cœur), les autres par le lot r2 ; mêmes comptes
    t3b = rl.construire_table_v3_lot({**conf, "episodes_resolution_lot": reste}, depot, None, ch_r2,
                                     str(depot / "diag" / "20261102-120400-graine-lot-jouet"
                                         / "resolution-graine-resolution-lot.json"), fmt=fmt_j)
    assert t3b["comptes"]["identifiants"] == len(autres) and sorted(t3b["episodes_verses_par_le_lot"]) == sorted(reste)
    # refus : contrôle croisé du cœur non conforme (R-11) ; lot fait sur un autre résultat du cœur
    _, ch_r_nc = _coeur(depot, conf, "20261102-120500", autres, {}, fiches, controle="non résolu")
    with pytest.raises(GardeArret, match="contrôle croisé"):
        rl.construire_table_v3_lot(conf, depot, None, ch_r_nc, str(chemin_lot), fmt=fmt_j)
    with pytest.raises(GardeArret, match="autre résultat de la résolution du cœur"):
        rl.construire_table_v3_lot(conf, depot, None, ch_r2, str(chemin_lot), fmt=fmt_j)
    # refus : deux résultats différents pour un même épisode (dans le lot ; entre cœur et lot) ; identifiants faux
    traj = fiches[e1]["trajectoire"]
    ent = {"episode": e1, "statut": "resolu", "voie": "directe", "forcages": [], "empreinte": traj,
           "empreinte_cible": traj}
    sha_r1 = verifier(ch_r1)
    ch = _faux_lot(depot, conf, "20261102-120600-graine-lot-jouet", sha_r1, [{**ent, "ids": ids1}, {**ent, "ids": faux}])
    with pytest.raises(GardeArret, match="deux résultats du lot différents"):
        rl.construire_table_v3_lot(conf, depot, None, ch_r1, ch, fmt=fmt_j)
    ch = _faux_lot(depot, {**conf, "episodes_resolution_lot": reste}, "20261102-120700-graine-lot-jouet",
                   verifier(ch_r2), [{**ent, "ids": faux}])
    with pytest.raises(GardeArret, match="cœur et du lot différents"):
        rl.construire_table_v3_lot({**conf, "episodes_resolution_lot": reste}, depot, None, ch_r2, ch, fmt=fmt_j)
    ch = _faux_lot(depot, conf, "20261102-120800-graine-lot-jouet", sha_r1, [{**ent, "ids": faux}])
    with pytest.raises(GardeArret, match="revérification"):
        rl.construire_table_v3_lot(conf, depot, None, ch_r1, ch, fmt=fmt_j)

    # ---- échéance de l'étape après le premier épisode : le suivant « non tenté : durée », résultat écrit et scellé
    decalage = [0.0]
    monkeypatch.setattr(rg, "horloge", lambda: time.perf_counter() + decalage[0])
    vraie = rl.resoudre_episode_lot

    def saute(*a, **k):
        sortie_ = vraie(*a, **k)
        decalage[0] += 1000.0
        return sortie_

    monkeypatch.setattr(rl, "resoudre_episode_lot", saute)
    conf3 = {**conf, "episodes_resolution_lot": list(autres)}
    r3 = rl.executer(conf3, depot, "20261102-120900-graine-lot-jouet", None, rl.ETAPE_LOT, ch_v, ch_r1,
                     autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    assert r3["episodes"][0]["statut"] == "resolu" and r3["lecture"] == "partielle"
    assert all(x.get("non_tente") and x["cause"].startswith("durée : budget de l'étape") for x in r3["episodes"][1:])
    assert r3["non_tentes"] == len(autres) - 1 and len(r3["episodes_consignes"]) == len(autres)
    # ---- signal TERM après le premier épisode : arrêt consigné, arret.json cite l'épisode déjà consigné (scellé)
    monkeypatch.setattr(rg, "horloge", time.perf_counter)

    def term(*a, **k):
        sortie_ = vraie(*a, **k)
        gardes.SIGNAL_TERM_RECU.append(15)
        return sortie_

    monkeypatch.setattr(rl, "resoudre_episode_lot", term)
    conf4 = {**conf, "episodes_resolution_lot": list(reversed(autres))}
    with pytest.raises(GardeArret, match="signal TERM"):
        rl.executer(conf4, depot, "20261102-121000-graine-lot-jouet", None, rl.ETAPE_LOT, ch_v, ch_r1,
                    autoriser_depot_sale=True, entropie_essai=3)
    gardes.SIGNAL_TERM_RECU.clear()
    d4 = depot / "diag" / "20261102-121000-graine-lot-jouet"
    arret = json.loads((d4 / "arret.json").read_text(encoding="utf-8"))["resultat"]
    cons = arret["partiel"]["episodes_consignes"]
    assert "signal TERM" in arret["motif"] and len(cons) == 1 and arret["partiel"]["episodes_traites"] == 1
    corps = json.loads((d4 / cons[0]["fichier"]).read_text(encoding="utf-8"))
    assert (d4 / (cons[0]["fichier"] + ".sha256")).exists() and corps["statut"] == "resolu" and corps["ids"]
    assert not (d4 / "resolution-graine-resolution-lot.json").exists()
    monkeypatch.setattr(rl, "resoudre_episode_lot", vraie)
    committer(depot)
    # ---- texte attendu de l'ouverture : absent → arrêt (consigné) ; présent → l'étape part
    ep0 = rg.EpisodeP3(pieces0, autres[0], T_).env()
    ouverture = fmt_j.tok.decode(fmt_j.ouverture(ep0.consigne_privee(0), ep0.observation(0, 0, [])))
    for attendu, run, ok in (("zz-absent-zz", "20261102-121100", False), (ouverture[-12:], "20261102-121200", True)):
        conf5 = {**conf, "agent": {**conf["agent"], "texte_attendu_ouverture": attendu}}
        v5, r5 = _coeur(depot, conf5, run, autres, {}, fiches)
        if ok:
            assert rl.executer(conf5, depot, f"{run[:-2]}50-graine-lot-jouet", None, rl.ETAPE_LOT, v5, r5,
                               autoriser_depot_sale=True, entropie_essai=3)["lecture"] == "complète"
        else:
            with pytest.raises(GardeArret, match="ouverture sans"):
                rl.executer(conf5, depot, f"{run[:-2]}50-graine-lot-jouet", None, rl.ETAPE_LOT, v5, r5,
                            autoriser_depot_sale=True, entropie_essai=3)
            assert (depot / "diag" / f"{run[:-2]}50-graine-lot-jouet" / "arret.json").exists()
        committer(depot)
