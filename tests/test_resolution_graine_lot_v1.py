"""Rejeu à graine, repli « lot fidèle » (`runs_nuit.resolution_graine_lot_v1`), sur processeur, avec le modèle Llama
minuscule et le vrai tokeniseur de Llama 3.1 des essais de la v1 (fixtures réutilisées).

1. Propriété clé : le lot fidèle, toutes lignes forcées à leurs jetons, redonne **au bit près** les logits de la
   génération originale du harnais (`jouer_episodes`, lots de 8 et de 4, remplissage à gauche, cache), pas après pas,
   ligne par ligne (empreintes sha256 de `generer_lot(empreinte_logits=True)`).
2. Cas sain : chaque épisode d'un lot de 8 (et de 4), généré par le harnais, est retrouvé par le lot fidèle (empreinte
   de P3, identifiants, découpages non canoniques compris), avec des logits identiques ; les autres lignes approchées
   (découpage canonique à longueur forcée) ne changent rien aux logits de la cible.
3. Artefacts (R5) : lot recomposé (une autre ligne, contexte plus long : remplissage différent) → logits différents
   détectés et déclarés ; permutation des lignes → mêmes bits (fait déclaré) ; graine fausse → non résolu ; texte altéré →
   non résolu ; repli : quasi-égalité basculée, et non résolu déclaré sous un seuil trop bas.
4. Plan des lots de P3 reconstruit depuis son code, vérifié contre l'ordre des textes : cas sain, artefacts.
5. Bout en bout en mode jouet sur un P3 jouet joué par le vrai code de P3 (lots de 4) : étape validation-lot à l'aveugle
   (toutes les empreintes retrouvées, identifiants égaux), étape resolution-lot sur les non résolus d'un résultat v1,
   gardes (validation absente, épisode résolu par la v1, noyau différent de P3)."""
import json

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
    modele = _modele_minuscule(tok, tmp_path_factory.mktemp("llama-minuscule-lot"), avec_octets=False)
    return modele, _jouer_lot(modele, fmt, 8, 0), _jouer_lot(modele, fmt, 4, 5)


def _lignes(eps, cible: int | None, ids=None, textes=None, jetons=None):
    """Lignes du lot : toutes forcées à leurs identifiants vrais, sauf la cible (sans identifiants)."""
    out = []
    for b, ep in enumerate(eps):
        c = b == cible
        out.append(rl.LigneLot(ep["identifiant"], EnvironnementJouet, textes if c and textes else ep["textes"],
                               jetons if c and jetons else ep["jetons"], ep["jetons_notes"],
                               None if c else [list(x) for x in (ids[b] if ids else ep["ids"])],
                               rl.SOURCE_CIBLE if c else "identique_base", True))
    return out


def _resoudre(modele, tok, fmt, eps, cible, lignes=None, moteur=None, textes=None, graines_=None, reference=True,
              **reglages):
    ep = eps[cible]
    voc = rg.Vocabulaire(tok, fmt.fins, V)
    Qs = [rg.tirages_exponentiels(g, n, V) for g, n in zip(graines_ or ep["graines"], ep["jetons"])]
    reg = rg.Reglages(max_nouveaux=MAX, combinaisons_max=8, **reglages)
    return rl.resoudre_episode_lot(moteur or rl.MoteurLot(modele), voc, fmt, lignes or _lignes(eps, cible, textes=textes),
                                   cible, T, Qs, ep["empreinte"], reg,
                                   reference_logits=ep["empreintes_logits"] if reference else None)


# ------------------------------------------------------------------------------- 1. propriété clé : logits au bit près


def test_lot_fidele_force_redonne_les_logits_au_bit(tok, fmt, jeu_lots):
    modele, eps8, eps4 = jeu_lots
    voc = rg.Vocabulaire(tok, fmt.fins, V)
    reg = rg.Reglages(max_nouveaux=MAX)
    for eps in (eps8, eps4):
        moteur = rl.MoteurLot(modele)
        rec, trouves, plans = rl.rejouer_episode_lot(moteur, voc, fmt, _lignes(eps, None), None, T, None, reg)
        assert rec is None and trouves == [] and len(plans) == T
        for t in range(T):
            assert plans[t]["empreintes_logits"] == [ep["empreintes_logits"][t] for ep in eps]
            assert plans[t]["jetons_manquants"] == 0
        # autant de passes que le harnais : préremplissage plus (longueur de la plus longue ligne − 1) par pas
        assert moteur.passes == sum(max(ep["jetons"][t] for ep in eps) for t in range(T))
    # le même lot en une seule ligne (passe pleine de la v1 ou lot de 1) ne donne pas ces bits
    moteur = rl.MoteurLot(modele)
    _, _, plans1 = rl.rejouer_episode_lot(moteur, voc, fmt, _lignes(eps8[:1], None), None, T, None, reg)
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
            assert all(x[5] > 0 for x in r["pas"]) and r["rang_dans_le_lot"] == b and r["lignes_approchees"] == 0
            assert [p["remplissage_cible"] for p in r["plans"]][0] == 0
            assert all(p["passes_decodage"] == ep["jetons"][t] - 1 for t, p in enumerate(r["plans"]))
    assert non_canoniques >= 3


def test_lignes_approchees_sans_effet_sur_les_logits_de_la_cible(tok, fmt, jeu_lots):
    """Les jetons des autres lignes ne comptent que par la longueur de leurs contextes : une ligne remplacée par son
    découpage canonique (à longueur forcée, complétée par le jeton de remplissage au besoin) laisse les logits de la
    cible au bit près et le lot est déclaré approché."""
    modele, eps8, _ = jeu_lots
    cible = 0
    autre = max(range(1, 8), key=lambda b: sum(eps8[b]["jetons"]))
    lignes = _lignes(eps8, cible)
    fin = fmt._pieces(("x", "y"))["cloture"][0]
    canon = [list(tok(x, add_special_tokens=False)["input_ids"]) + ([fin] if j != jn else [])
             for x, j, jn in zip(eps8[autre]["textes"], eps8[autre]["jetons"], eps8[autre]["jetons_notes"])]
    assert canon != eps8[autre]["ids"]
    lignes[autre] = rl.LigneLot(eps8[autre]["identifiant"], EnvironnementJouet, eps8[autre]["textes"],
                                eps8[autre]["jetons"], eps8[autre]["jetons_notes"], canon, rl.SOURCE_APPROCHEE, False)
    r = _resoudre(modele, tok, fmt, eps8, cible, lignes=lignes)
    assert r["statut"] == "resolu" and r["ids"] == eps8[cible]["ids"] and r["logits_conformes"] is True
    assert r["lignes_approchees"] == 1 and r["lot"][autre] == {"episode": eps8[autre]["identifiant"],
                                                              "source": rl.SOURCE_APPROCHEE, "exacte": False}


# ------------------------------------------------------------------------------------------------------ 3. artefacts


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
    assert rg.accord_non_contraint(r["pas"]) < 0.9
    t = max(range(T), key=lambda k: len(ep["textes"][k]))
    x = ep["textes"][t]
    k = next(i for i in range(len(x) // 2, len(x)) if x[i].isalpha())
    alt = list(ep["textes"])
    alt[t] = x[:k] + ("q" if x[k] != "q" else "z") + x[k + 1:]
    assert len(alt[t].encode()) == len(x.encode()) and alt[t] != x
    r = _resoudre(modele, tok, fmt, eps8, cible, textes=alt)
    assert r["statut"] == "non_resolu" and r["ids"] is None


def test_repli_bascule_une_quasi_egalite_dans_le_lot(tok, fmt, jeu_lots):
    modele, eps8, _ = jeu_lots
    cible = max(range(8), key=lambda b: sum(eps8[b]["jetons"]))
    ep = eps8[cible]
    sain = _resoudre(modele, tok, fmt, eps8, cible)
    t0, s0, vrai, _, _, _, faux, _, _ = next(x for x in sain["pas"] if x[4] > 1 and x[6] not in FINS_P3
                                            and x[1] < ep["jetons_notes"][x[0]] - 1)
    Q = rg.tirages_exponentiels(ep["graines"][t0], ep["jetons"][t0], V)[s0].double()

    class Perturbe(rl.MoteurLot):
        """Au pas (t0, s0) de la ligne cible, le second candidat passe devant le vrai d'un écart de 0,1 en log."""

        def logits_cpu(self, sortie):
            L = super().logits_cpu(sortie)
            if self.etiquette == (t0, s0):
                L[cible, faux] = float(L[cible, vrai]) - float(torch.log(Q[vrai])) + float(torch.log(Q[faux])) + 0.1
            return L

    r = _resoudre(modele, tok, fmt, eps8, cible, moteur=Perturbe(modele))
    assert r["statut"] == "resolu" and r["voie"] == "repli" and r["ids"] == ep["ids"], r["cause"]
    assert r["forcages"][0]["pas"] == t0 and r["forcages"][0]["rang"] == s0 and r["forcages"][0]["jeton"] == vrai
    assert r["ids_directs"][t0][s0] == faux and r["logits_conformes"] is False
    assert all(p["empreinte_logits_cible"] for p in r["plans"])
    r = _resoudre(modele, tok, fmt, eps8, cible, moteur=Perturbe(modele), seuil_ecart=0.05)
    assert r["statut"] == "non_resolu" and "repli" in r["cause"]
    assert all((q["pas"], q["rang"]) != (t0, s0) for q in r["quasi_egalites"])


# ------------------------------------------------------------------------------------------------- 4. plan des lots


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


def test_configuration_gardes():
    base = {k: None for k in rg.CLES}
    base.update(mode="jouet", T=10, max_nouveaux=400, fils=1, fils_tirages=8, episodes_d_avance=2, quasi_egalites_max=12,
                bascules_max=2, combinaisons_max=80, combinaisons_max_validation=12, balayages_max=64,
                seuil_validation=147, temperature=1.0, seuil_ecart=0.5, duree_max_s=3000, episodes_resolution=["a"])
    with pytest.raises(GardeArret, match="incomplète"):
        rl.exiger_config(base)
    lot = {**base, "episodes_validation_lot": ["b"], "episodes_resolution_lot": [], "combinaisons_max_lot": 6,
           "seuil_validation_lot": 1}
    rl.exiger_config(lot)
    for k, v in (("combinaisons_max_lot", -1), ("seuil_validation_lot", True), ("episodes_resolution_lot", ["a", "a"]),
                 ("temperature", 0.0)):
        with pytest.raises(GardeArret):
            rl.exiger_config({**lot, k: v})
    with pytest.raises(GardeArret, match="noyau"):
        rl.exiger_meme_lot_que_p3({"noyau_attention": "math"}, {"config": {"lot": 8, "noyau_attention": "defaut"}})
    with pytest.raises(GardeArret, match="taille de lot"):
        rl.exiger_meme_lot_que_p3({"noyau_attention": "defaut"}, {"config": {}})
    assert rl.exiger_meme_lot_que_p3({"noyau_attention": "defaut"}, {"config": {"lot": 8}}) == 8


# --------------------------------------------------------------------------------------- 5. bout en bout (P3 jouet)


def test_bout_en_bout_jouet_validation_lot_puis_resolution_lot(source, tmp_path):
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
    assert connus and autres, (len(connus), len(autres))
    table = json.loads((tmp_path / "table0.json").read_text(encoding="utf-8"))
    table["episodes"] += [{"episode": e, "methode": "non_resolu", "trajectoire_p3": pieces0.fiches[e]["trajectoire"],
                           "fins": {}, "paires": [], "essais": {}} for e in autres]
    table["comptes"]["non_resolu"] = table["comptes"].get("non_resolu", 0) + len(autres)
    tp = tmp_path / "table-jouet-v2.json"
    tp.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(tp)
    # plan des lots de ce P3 jouet : deux lots de quatre (deux tâches × quatre conditions), comme son code
    from controle_ia.environnements.pilote_a import charger_taches

    lots = rl.plan_des_lots(charger_taches(f), int(pieces0.manifeste_p3["config"]["lot"]), pieces0.lignes)
    assert [len(x) for x in lots] == [4, 4]
    # résultat de la résolution v1, jouet : les « autres » laissés non résolus (le lot fidèle n'est appelé que pour eux)
    conf_v1 = _config_graine(depot, f, c, tp, autres, seuil_validation=len(connus))

    def resultat_v1(run, non_resolus, resolus):
        chemin_m1, _ = creer_manifeste(depot, run, conf_v1, ["aucun-tirage-propre"], entropie=3,
                                       autoriser_depot_sale=True, commande=f"{rg.COMMANDE} --etape resolution")
        return ecrire_resultat(depot, chemin_m1, "resolution-graine-resolution", {
            "etape": "resolution", "version": rg.VERSION, "lecture": "partielle" if resolus else "aucune",
            "episodes_etape": len(autres), "empreintes_retrouvees": len(resolus),
            "non_resolus": [{"episode": e, "cause": "jouet"} for e in non_resolus],
            "episodes": [{"episode": e, "statut": "resolu", "ids": ids} for e, ids in resolus.items()]
                        + [{"episode": e, "statut": "non_resolu", "ids": None} for e in non_resolus]})

    chemin_r1 = resultat_v1("20261102-120000-graine-v1-jouet", autres, {})
    committer(depot)
    conf = {**conf_v1, "episodes_validation_lot": connus, "episodes_resolution_lot": [], "combinaisons_max_lot": 6,
            "seuil_validation_lot": len(connus)}
    # noyau d'attention autre que celui de P3 : refusé avant tout calcul
    with pytest.raises(GardeArret, match="noyau"):
        rl.executer({**conf, "noyau_attention": "defaut"}, depot, "20261102-120050-graine-lot-jouet", None,
                    "validation-lot", autoriser_depot_sale=True, entropie_essai=3)
    # résolution-lot sans validation-lot : refusée avant tout calcul
    with pytest.raises(GardeArret, match="validation"):
        rl.executer(conf, depot, "20261102-120100-graine-lot-jouet", None, "resolution-lot", None, str(chemin_r1),
                    autoriser_depot_sale=True, entropie_essai=3)
    v = rl.executer(conf, depot, "20261102-120200-graine-lot-jouet", None, "validation-lot", autoriser_depot_sale=True,
                    entropie_essai=3)
    assert v["lecture"] == "atteint" and v["empreintes_retrouvees"] == v["episodes_etape"] == len(connus)
    assert v["identifiants_egaux_episodes"] == len(connus) and v["actions_egales"] == v["actions_comparees"]
    assert v["accord_non_contraint"]["par_episode_min"] == 1.0 and not v["erreurs_directes"] and v["taille_lot"] == 4
    assert all(x["voie"] == "directe" and len(x["lot"]) == 4 for x in v["episodes"])
    pas_v = depot / "diag" / "20261102-120200-graine-lot-jouet" / v["pas_fichier"]
    assert (pas_v.parent / (pas_v.name + ".sha256")).exists()
    with np.load(pas_v) as z:
        assert len(z["choix"]) == v["accord_non_contraint"]["pas"] and (z["choix"] == z["non_contraint"]).all()
    chemin_v = depot / "diag" / "20261102-120200-graine-lot-jouet" / "resolution-graine-validation-lot.json"
    committer(depot)
    # un épisode résolu par la v1 demandé au lot : refusé ; une configuration autre que celle de la validation : refusée
    with pytest.raises(GardeArret, match="résolus par la v1"):
        rl.episodes_de_l_etape("resolution-lot", {**conf, "episodes_resolution_lot": connus[:1]}, cl, autres)
    with pytest.raises(GardeArret, match="aucun épisode non résolu"):
        rl.episodes_de_l_etape("resolution-lot", conf, cl, [])
    with pytest.raises(GardeArret, match="autre configuration"):
        rl.executer({**conf, "episodes_resolution_lot": autres[:1]}, depot, "20261102-120300-graine-lot-jouet", None,
                    "resolution-lot", str(chemin_v), str(chemin_r1), autoriser_depot_sale=True, entropie_essai=3)
    r = rl.executer(conf, depot, "20261102-120400-graine-lot-jouet", None, "resolution-lot", str(chemin_v),
                    str(chemin_r1), autoriser_depot_sale=True, entropie_essai=3)
    assert r["lecture"] == "complète" and r["non_resolus_v1"] == autres
    assert sorted(x["episode"] for x in r["episodes"]) == sorted(autres)
    assert all(x["empreinte_retrouvee"] and x["ids"] and x["base_nv"] != x["ids"] for x in r["episodes"])
    # les autres lignes de chaque lot : exactes quand connues (base, table, résolues plus tôt par l'étape), sinon
    # approchées et déclarées
    sources = {y["source"] for x in r["episodes"] for y in x["lot"]}
    assert rl.SOURCE_CIBLE in sources and sources <= {rl.SOURCE_CIBLE, "identique_base", "lot_fidele",
                                                      rl.SOURCE_APPROCHEE} | {f"table:{m}" for m in rg.METHODES_V3}
    assert all(y["exacte"] for x in r["episodes"] for y in x["lot"] if y["source"] != rl.SOURCE_APPROCHEE)
    chemin_r = depot / "diag" / "20261102-120400-graine-lot-jouet" / "resolution-graine-resolution-lot.json"
    assert chemin_r.exists() and (chemin_r.parent / "resolution-graine-resolution-lot.json.sha256").exists()
    # un résultat v1 qui cite un des « autres » résolu (identifiants que le lot vient de retrouver) : ligne
    # « resolution_v1 », revérifiée par l'empreinte, dans les lots des autres cibles ; identifiants faux refusés
    e1, ids1 = r["episodes"][0]["episode"], r["episodes"][0]["ids"]
    faux = [list(a) for a in ids1]
    faux[0] = faux[0][::-1] if len(faux[0]) > 1 else faux[0] + faux[0]
    with pytest.raises(GardeArret, match="empreinte de P3"):
        rl.connus_de_la_v1(pieces0, fmt_j, int(c["T"]), {e1: faux})
    assert rl.connus_de_la_v1(pieces0, fmt_j, int(c["T"]), {e1: ids1}) == {e1: (ids1, "resolution_v1")}
    reste = [e for e in autres if e != e1]
    chemin_r2 = resultat_v1("20261102-120500-graine-v1-jouet", reste, {e1: ids1})
    committer(depot)
    r2 = rl.executer(conf, depot, "20261102-120600-graine-lot-jouet", None, "resolution-lot", str(chemin_v),
                     str(chemin_r2), autoriser_depot_sale=True, entropie_essai=3)
    assert r2["lecture"] == "complète" and [x["episode"] for x in r2["episodes"]] == reste
    assert {x["episode"]: x["ids"] for x in r2["episodes"]} == {x["episode"]: x["ids"] for x in r["episodes"]
                                                                if x["episode"] in reste}
    assert any(y["source"] == "resolution_v1" and y["episode"] == e1 for x in r2["episodes"] for y in x["lot"])
