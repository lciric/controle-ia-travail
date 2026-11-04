"""Relance v4 de R1 : lot fidèle à plusieurs cibles, témoin, réparation, table v4 (`runs_nuit.resolution_graine_lot_v2`),
sur processeur, **sans aucun téléchargement** : modèle jouet de type Llama à poids aléatoires et tokeniseur par
caractères du harnais (`charger_modele_et_format(..., "jouet", ...)`), qui tire parfois un jeton spécial effacé du texte
stocké : le texte retokenisé n'a alors pas le compte de jetons de la génération, la classe même des 89 épisodes.

1. Propriété clé : le lot rejoué, toutes lignes forcées, redonne **au bit près** les logits de la génération du harnais
   (`jouer_episodes`), pas après pas, ligne par ligne, et les **empreintes de capture** des actions d'équivalence ;
   lecture du témoin « exact » (cas sain) ; artefacts (R5) : graine fausse sur une ligne (accord < 1), modèle décalé
   d'une unité au dernier rang sur un poids (captures différentes), capture de P3 altérée → « non exact ».
2. Plusieurs cibles en même temps : chaque cible retrouve les identifiants vrais (non canoniques) ; mêmes identifiants
   qu'à une cible (v1) ; forme égale (passes = forme de P3) ; une cible au texte altéré échoue seule, déclarée, les autres
   sont retrouvées, la forme reste celle de P3.
3. Gardes unitaires : ligne approchée (remplissage ordinaire, jamais une fin), voie écrite d'avance, lecture du témoin
   (sain, accord, capture, forme, sans mesure), lecture globale.
4. Bout en bout en mode jouet sur un P3 jouet (lot 0 : quatre épisodes cassés ; lot 1 : quatre connus) : témoin « exact »
   sur le lot 1 ; témoin sur un lot sans identifiants connus refusé ; réparation « lot fidèle » (4 sur 4, voie
   « lot_multi:directe ») ; table v4 écrite, scellée, rechargée, revérifiée ; refus : identifiants faux, table v3 au
   chargeur v4, résultat d'une autre configuration ; R3 ; témoin « non exact » (modèle décalé) → voie « passe forcée »
   (4 sur 4) ; configuration (voie non écrite d'avance, comptes attendus faux)."""
import copy
import json
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.harnais.episode import EnvironnementJouet, empreinte_episode, jouer_episodes
from controle_ia.manifeste import creer_manifeste, ecrire_resultat
from controle_ia.runs_nuit import resolution_graine_lot_v1 as rl
from controle_ia.runs_nuit import resolution_graine_lot_v2 as rv
from controle_ia.runs_nuit import resolution_graine_v1 as rg
from controle_ia.runs_nuit.rejeu_activations_v1 import reconstruire_episode
from controle_ia.scellement import sceller

from test_premier_test_ia_run import entropie_fixe  # noqa: F401  (fixture réutilisée)
from test_resolution_graine_lot_v1 import _preparer
from test_resolution_graine_v1 import _config_graine
from test_runs_nuit_v1 import RUN_P3, source  # noqa: F401  (fixture réutilisée)

T, MAX, B = 3, 8, 4
COUCHES = [0, 2]
V2 = {"lots_temoin": [1], "lots_d_abord": [], "cibles_attendues": None, "lots_cibles_attendus": None,
      "combinaisons_max_lot": 6, "duree_max_episode_lot_s": 300, "duree_max_lot_s": 900, "seuil_lecture_lot": 0.99,
      "capture_equivalence": True, "voie_si_temoin_non_exact": "passe_forcee"}


@pytest.fixture(scope="module")
def jouet():
    """Modèle jouet (poids aléatoires, graine fixe) et format par caractères, un seul fil de calcul (comme P3)."""
    from controle_ia.environnements.lancer_pilote_a import charger_modele_et_format

    fils = torch.get_num_threads()
    torch.set_num_threads(1)
    try:
        modele, fmt = charger_modele_et_format({"nom": "agent-jouet"}, "jouet", 11)
        yield modele, fmt
    finally:
        torch.set_num_threads(fils)


def _jouer(modele, fmt, graine0: int, echantillon=None):
    """Un lot joué par le harnais (B épisodes, T pas) ; gardés : textes, longueurs, graines, empreinte de trajectoire,
    identifiants vrais, empreintes des logits par pas et de capture par pas (référence, « P3 »), découpage de base."""
    gr = [{(0, t): 1000 * b + 17 * t + 3 + graine0 for t in range(T)} for b in range(B)]
    ech = set(echantillon if echantillon is not None else {(b, 0, t) for b in range(B) for t in range(T) if (b + t) % 2})
    sorties = jouer_episodes(modele, fmt, EnvironnementJouet(), [f"e{b}" for b in range(B)], 1, T, gr, COUCHES,
                             max_nouveaux=MAX, echantillon_equivalence=ech, empreinte_logits=True)
    eps = []
    for b, (ep, acts, rapport) in enumerate(sorties):
        actions = ep.transcriptions[0].actions
        textes = [a.texte for a in actions]
        jetons = [len(a.ids) for a in actions]
        notes = [len(a.ids) - (1 if a.ids and a.ids[-1] in fmt.fins else 0) for a in actions]
        lignes = [{"episode": f"e{b}", "pas": t, "texte": textes[t]} for t in range(T)]
        base = reconstruire_episode(fmt, EnvironnementJouet(), T, lignes, jetons, notes)
        eps.append({"identifiant": ep.identifiant, "textes": textes, "jetons": jetons, "jetons_notes": notes,
                    "graines": [gr[b][(0, t)] for t in range(T)], "empreinte": empreinte_episode(ep, acts)["trajectoire"],
                    "ids": [list(a.ids) for a in actions], "base_nv": [list(a["nv"]) for a in base["actions"]],
                    "canonique": all(a["conforme"] for a in base["actions"]),
                    "empreintes_logits": [rapport["empreintes_logits"][f"0,{t}"] for t in range(T)],
                    "captures": {int(k.split(",")[1]): v for k, v in rapport["empreintes_capture"].items()}})
    return eps


@pytest.fixture(scope="module")
def lots(jouet):
    modele, fmt = jouet
    fils = torch.get_num_threads()
    torch.set_num_threads(1)
    try:
        # graine choisie pour qu'au moins deux lignes tirent un jeton spécial effacé (classe des 89) ; vérifié ci-dessous
        for g in range(0, 400, 7):
            eps = _jouer(modele, fmt, g)
            if sum(not e["canonique"] for e in eps) >= 2:
                return eps
        raise AssertionError("aucun lot jouet à deux lignes non canoniques")
    finally:
        torch.set_num_threads(fils)


def _lignes(eps, fmt, cibles=(), graines=None, textes=None):
    voc_remp = rv.remplissage_ordinaire(rg.Vocabulaire(fmt.tok, fmt.fins, len(fmt.tok)))
    out = []
    for b, ep in enumerate(eps):
        c = b in cibles
        out.append(rv.LigneLotV2(ep["identifiant"], EnvironnementJouet, (textes or {}).get(b, ep["textes"]),
                                 ep["jetons"], ep["jetons_notes"], None if c else [list(x) for x in ep["ids"]],
                                 rv.SOURCE_CIBLE if c else "identique_base", True,
                                 list((graines or {}).get(b, ep["graines"])), voc_remp,
                                 [list(x) for x in ep["base_nv"]]))
    return out


def _tirages(eps, V, graines=None):
    def f(b, t):
        g = (graines or {}).get(b, eps[b]["graines"])
        return rg.tirages_exponentiels(g[t], eps[b]["jetons"][t], V)
    return f


def _voc(fmt):
    return rg.Vocabulaire(fmt.tok, fmt.fins, len(fmt.tok))


def _cap(eps):
    return {(b, t): e for b, ep in enumerate(eps) for t, e in ep["captures"].items()}


# --------------------------------------------------------------------------------- 1. propriété clé et témoin


def test_lot_rejoue_logits_et_captures_au_bit_et_temoin_exact(jouet, lots):
    modele, fmt = jouet
    voc = _voc(fmt)
    reg = rg.Reglages(max_nouveaux=MAX)
    moteur = rl.MoteurLot(modele)
    r = rv.rejouer_lot_multi(moteur, voc, fmt, _lignes(lots, fmt), T, None, reg, True, set(_cap(lots)), COUCHES)
    assert r["cibles"] == {} and len(r["plans"]) == T
    for t in range(T):
        assert r["plans"][t]["empreintes_logits"] == [ep["empreintes_logits"][t] for ep in lots]
        assert r["plans"][t]["passes_decodage"] == r["plans"][t]["passes_de_la_forme"]
    assert r["captures"] == _cap(lots) and len(r["captures"]) >= 4
    lec = rv.lire_temoin(r["plans"], r["captures"], _cap(lots))
    assert lec["lecture"] == rv.LECTURE_EXACT and lec["mesure"]["accord"] == 1.0
    assert lec["mesure"]["pas"] == sum(sum(ep["jetons"]) for ep in lots) and lec["captures"]["egales"] == len(_cap(lots))


def test_temoin_artefacts_graine_fausse_modele_decale_capture_alteree(jouet, lots):
    modele, fmt = jouet
    voc = _voc(fmt)
    reg = rg.Reglages(max_nouveaux=MAX)
    cap = _cap(lots)
    # graine fausse sur une ligne : l'accord de cette ligne tombe, lecture « non exact » (logits inchangés)
    fausse = {1: [g + 1 for g in lots[1]["graines"]]}
    r = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt, graines=fausse), T, None, reg, True,
                             set(cap), COUCHES)
    lec = rv.lire_temoin(r["plans"], r["captures"], cap)
    assert lec["lecture"] == rv.LECTURE_NON_EXACT and lec["mesure"]["accord"] < 1.0
    assert lec["captures"]["egales"] == len(cap)
    # modèle décalé d'une unité au dernier rang sur un poids de la première couche : calcul autre que celui de « P3 »
    m2 = copy.deepcopy(modele)
    with torch.no_grad():
        w = m2.model.layers[0].self_attn.q_proj.weight
        w.view(-1)[0] = torch.nextafter(w.view(-1)[0], torch.tensor(1e9, dtype=w.dtype))
    r = rv.rejouer_lot_multi(rl.MoteurLot(m2), voc, fmt, _lignes(lots, fmt), T, None, reg, True, set(cap), COUCHES)
    lec = rv.lire_temoin(r["plans"], r["captures"], cap)
    assert lec["lecture"] == rv.LECTURE_NON_EXACT and lec["captures"]["differentes"]
    # capture de « P3 » altérée : une seule différence suffit
    k = sorted(cap)[0]
    r = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt), T, None, reg, True, set(cap), COUCHES)
    lec = rv.lire_temoin(r["plans"], r["captures"], {**cap, k: "0" * 64})
    assert lec["lecture"] == rv.LECTURE_NON_EXACT and lec["captures"]["differentes"] == [f"{k[0]},{k[1]}"]


# --------------------------------------------------------------------------------- 2. plusieurs cibles


def test_plusieurs_cibles_retrouvees_ensemble_et_comme_une_a_une(jouet, lots):
    modele, fmt = jouet
    voc = _voc(fmt)
    reg = rg.Reglages(max_nouveaux=MAX)
    cibles = [b for b, ep in enumerate(lots) if not ep["canonique"]]
    assert len(cibles) >= 2
    moteur = rl.MoteurLot(modele)
    r = rv.rejouer_lot_multi(moteur, voc, fmt, _lignes(lots, fmt, cibles), T, _tirages(lots, voc.V), reg, True,
                             set(_cap(lots)), COUCHES)
    for b in cibles:
        d = r["cibles"][b]
        assert d["echec"] is None and d["ids"] == lots[b]["ids"] and d["empreinte"] == lots[b]["empreinte"]
        assert d["ids"] != lots[b]["base_nv"]                                   # identifiants non canoniques retrouvés
    assert all(p["passes_decodage"] == p["passes_de_la_forme"] for p in r["plans"])
    for t in range(T):
        assert r["plans"][t]["empreintes_logits"] == [ep["empreintes_logits"][t] for ep in lots]
    assert r["captures"] == _cap(lots)
    # même résultat qu'à une cible (v1), chaque cible seule dans son lot
    for b in cibles:
        Qs = [rg.tirages_exponentiels(g, n, voc.V) for g, n in zip(lots[b]["graines"], lots[b]["jetons"])]
        r1 = rl.resoudre_episode_lot(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt, [b]), b, T, Qs,
                                     lots[b]["empreinte"], rg.Reglages(max_nouveaux=MAX, combinaisons_max=4))
        assert r1["statut"] == "resolu" and r1["ids"] == r["cibles"][b]["ids"]


def test_cible_en_echec_seule_declaree_forme_gardee(jouet, lots):
    modele, fmt = jouet
    voc = _voc(fmt)
    reg = rg.Reglages(max_nouveaux=MAX)
    cibles = [b for b, ep in enumerate(lots) if not ep["canonique"]]
    b0 = cibles[0]
    textes = list(lots[b0]["textes"])
    textes[0] = "☃" + textes[0][1:] if textes[0] else "☃"         # caractère hors du vocabulaire jouet
    r = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt, cibles, textes={b0: textes}), T,
                             _tirages(lots, voc.V), reg, True, (), None)
    assert r["cibles"][b0]["echec"] is not None and r["cibles"][b0]["echec"]["pas"] == 0
    assert r["cibles"][b0]["ids"] is None
    for b in cibles[1:]:
        assert r["cibles"][b]["ids"] == lots[b]["ids"] and r["cibles"][b]["empreinte"] == lots[b]["empreinte"]
    assert all(p["passes_decodage"] == p["passes_de_la_forme"] for p in r["plans"])
    # la cible en échec garde exactement la longueur de P3 à chaque action : les contextes de toutes les lignes ont, à
    # chaque pas, la longueur du lot rejoué toutes lignes forcées (jamais une fin au milieu d'une action)
    ref = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt), T, None, reg, False, (), None)
    assert [p["longueurs_contextes"] for p in r["plans"]] == [p["longueurs_contextes"] for p in ref["plans"]]
    # les autres lignes ont toujours les logits de « P3 » (la cible en échec garde la forme)
    for t in range(T):
        assert [e for b, e in enumerate(r["plans"][t]["empreintes_logits"]) if b != b0] == \
            [ep["empreintes_logits"][t] for b, ep in enumerate(lots) if b != b0]


def test_cibles_plus_courtes_que_le_lot_forme_complete_et_controle_du_texte(jouet, lots, monkeypatch):
    """Cibles = toutes les lignes sauf la plus longue d'une action : le lot va jusqu'à la fin de la ligne la plus longue
    (forme de P3), les captures des lignes forcées restent celles de « P3 » ; contrôle du texte décodé éprouvé sur un
    artefact (décodage altéré : chaque cible échoue, déclarée « texte décodé ≠ texte stocké »)."""
    modele, fmt = jouet
    voc = _voc(fmt)
    reg = rg.Reglages(max_nouveaux=MAX)
    t0 = next(t for t in range(T) if len({ep["jetons"][t] for ep in lots}) > 1)
    longue = max(range(B), key=lambda b: lots[b]["jetons"][t0])
    cibles = [b for b in range(B) if lots[b]["jetons"][t0] < lots[longue]["jetons"][t0]]   # strictement plus courtes
    assert cibles
    r = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt, cibles), T, _tirages(lots, voc.V), reg,
                             True, set(_cap(lots)), COUCHES)
    assert all(p["passes_decodage"] == p["passes_de_la_forme"] for p in r["plans"])
    assert r["plans"][t0]["passes_decodage"] == lots[longue]["jetons"][t0] - 1
    assert r["captures"] == _cap(lots)
    assert all(r["cibles"][b]["ids"] == lots[b]["ids"] for b in cibles)
    lignes = _lignes(lots, fmt, cibles)
    vrai = fmt.tok.decode
    monkeypatch.setattr(fmt.tok, "decode", lambda ids, **k: "§" + vrai(ids, **k))
    r = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, lignes, T, _tirages(lots, voc.V), reg, False, (), None)
    assert all(r["cibles"][b]["echec"]["pas"] == 0 and "texte décodé" in r["cibles"][b]["echec"]["cause"]
               for b in cibles)


def test_cible_en_echec_action_sans_fin_remplie_d_un_jeton_ordinaire(jouet, lots):
    """Une cible ne peut échouer qu'à son dernier jeton (les jetons spéciaux hors fins, sans octet, sont toujours
    candidats) ; dans une action sans fin (tronquée à `max_nouveaux`), ce dernier jeton est le remplissage **ordinaire** :
    la clôture et donc le contexte de l'action suivante gardent la longueur de P3 (un remplissage qui serait une fin, comme
    chez Llama 3, raccourcirait la clôture)."""
    modele, fmt = jouet
    voc = _voc(fmt)
    reg = rg.Reglages(max_nouveaux=MAX)
    b0, t1 = next((b, t) for b in range(B) for t in range(T - 1) if lots[b]["jetons"][t] == lots[b]["jetons_notes"][t])
    textes = list(lots[b0]["textes"])
    textes[t1] = "\u2603" + textes[t1][1:]          # même longueur : l'observation suivante ne change pas de longueur
    r = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt, [b0], textes={b0: textes}), T,
                             _tirages(lots, voc.V), reg, False, (), None)
    assert r["cibles"][b0]["echec"]["pas"] == t1 and "après le dernier jeton" in r["cibles"][b0]["echec"]["cause"]
    ref = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt, textes={b0: textes}), T, None, reg,
                               False, (), None)
    assert [p["longueurs_contextes"] for p in r["plans"]] == [p["longueurs_contextes"] for p in ref["plans"]]
    assert all(p["passes_decodage"] == p["passes_de_la_forme"] for p in r["plans"])


def test_cibles_coupees_par_l_echeance_forme_gardee(jouet, lots):
    """Échéance dépassée (garde de durée) : chaque cible échoue dès son premier jeton (`DureeEpuisee`) et reçoit le
    remplissage ordinaire jusqu'à sa longueur ; les contextes gardent, à chaque pas, les longueurs de P3 (un remplissage
    qui serait une fin arrêterait la ligne au premier jeton)."""
    modele, fmt = jouet
    voc = _voc(fmt)
    reg = rg.Reglages(max_nouveaux=MAX, echeance=rg.horloge() - 1.0)
    cibles = list(range(B))
    r = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt, cibles), T, _tirages(lots, voc.V), reg,
                             False, (), None)
    assert all(r["cibles"][b]["echec"]["pas"] == 0 and "DureeEpuisee" in r["cibles"][b]["echec"]["cause"]
               for b in cibles)
    ref = rv.rejouer_lot_multi(rl.MoteurLot(modele), voc, fmt, _lignes(lots, fmt), T, None, rg.Reglages(max_nouveaux=MAX),
                               False, (), None)
    assert [p["longueurs_contextes"] for p in r["plans"]] == [p["longueurs_contextes"] for p in ref["plans"]]
    assert all(p["passes_decodage"] == p["passes_de_la_forme"] for p in r["plans"])


# --------------------------------------------------------------------------------- 3. gardes unitaires


def test_ligne_approchee_remplissage_ordinaire_et_gardes(jouet):
    _, fmt = jouet
    voc = _voc(fmt)
    remp = rv.remplissage_ordinaire(voc)
    fins = set(fmt.fins)
    assert remp not in fins and voc.octets[remp]
    f = sorted(fins)[0]
    # base trop courte : complétée ; fin interne remplacée ; fin finale ôtée puis remise (la fin par défaut)
    assert rv.forcee_approchee([10, f, 11, f], 6, 5, remp, 99, fins) == [10, remp, 11, remp, remp, 99]
    assert rv.forcee_approchee([10, 11, 12, 13], 3, 3, remp, 99, fins) == [10, 11, 12]
    with pytest.raises(GardeArret, match="jetons notés"):
        rv.forcee_approchee([1], 5, 3, remp, 99, fins)
    with pytest.raises(GardeArret, match="parmi les fins"):
        rv.forcee_approchee([1], 2, 1, f, 99, fins)
    # le remplissage de P3 chez Llama 3 est une fin : la v1 l'aurait inséré au milieu d'une ligne approchée
    assert rv.voie_de_reparation(rv.LECTURE_EXACT) == rv.VOIE_LOT
    assert rv.voie_de_reparation(rv.LECTURE_NON_EXACT) == rv.VOIE_PASSE
    with pytest.raises(GardeArret, match="lecture du témoin"):
        rv.voie_de_reparation(rv.LECTURE_SANS)
    assert rv.lecture_globale_temoin([rv.LECTURE_EXACT, rv.LECTURE_EXACT]) == rv.LECTURE_EXACT
    assert rv.lecture_globale_temoin([rv.LECTURE_EXACT, rv.LECTURE_NON_EXACT]) == rv.LECTURE_NON_EXACT
    assert rv.lecture_globale_temoin([]) == rv.LECTURE_SANS
    assert rv.lecture_globale_temoin([rv.LECTURE_EXACT, rv.LECTURE_SANS]) == rv.LECTURE_SANS


def test_cibles_v4_hors_table_v3_et_base_identique():
    cl = {"a": {"identique_base": True}, "b": {"identique_base": False}, "c": {"identique_base": False},
          "d": {"identique_base": False}}
    t3 = {"episodes": [{"episode": "b", "methode": "une_paire"}]}
    assert rv.cibles_v4(cl, t3) == ["c", "d"]                  # ni la base identique, ni l'entrée de la table v3
    assert rv.cibles_v4(cl, {"episodes": []}) == ["b", "c", "d"]


def _plan(pas_mesures, passes=3, forme=3, manquants=0, hors=0):
    return {"pas": 0, "passes_decodage": passes, "passes_de_la_forme": forme, "jetons_manquants": manquants,
            "mesure_voisines": [{"rang": 0, "episode": "e0", "pas": pas_mesures, "hors_candidats": hors,
                                 "non_mesures_fffd": 0}]}


def test_lecture_du_temoin_gelee():
    sain = [(0, 5, 5, 0.4, 5, 5), (1, 7, 7, 0.9, 7, 7)]
    assert rv.lire_temoin([_plan(sain)], {(0, 0): "a"}, {(0, 0): "a"})["lecture"] == rv.LECTURE_EXACT
    desaccord = [(0, 5, 6, 0.4, 5, 5), (1, 7, 7, 0.9, 7, 7)]
    assert rv.lire_temoin([_plan(desaccord)], {}, {})["lecture"] == rv.LECTURE_NON_EXACT
    # un seul désaccord sur 400 pas (accord 0,9975) suffit : l'égalité est exacte, sans tolérance
    presque = [(k, 5, 5, 0.4, 5, 5) for k in range(399)] + [(399, 5, 6, 0.4, 5, 5)]
    lec = rv.lire_temoin([_plan(presque)], {}, {})
    assert lec["mesure"]["accord"] == 399 / 400 and lec["lecture"] == rv.LECTURE_NON_EXACT
    contraint = [(0, 5, 5, 0.4, 5, 6)]
    assert rv.lire_temoin([_plan(contraint)], {}, {})["lecture"] == rv.LECTURE_NON_EXACT
    assert rv.lire_temoin([_plan(sain)], {}, {(0, 0): "a"})["lecture"] == rv.LECTURE_NON_EXACT       # capture absente
    assert rv.lire_temoin([_plan(sain)], {(0, 0): "a", (1, 0): "b"}, {(0, 0): "a"})["lecture"] == rv.LECTURE_NON_EXACT
    assert rv.lire_temoin([_plan(sain, passes=2)], {}, {})["lecture"] == rv.LECTURE_NON_EXACT        # forme
    assert rv.lire_temoin([_plan(sain, manquants=1)], {}, {})["lecture"] == rv.LECTURE_NON_EXACT
    assert rv.lire_temoin([_plan(sain, hors=1)], {}, {})["lecture"] == rv.LECTURE_NON_EXACT
    assert rv.lire_temoin([_plan([])], {}, {})["lecture"] == rv.LECTURE_SANS


# --------------------------------------------------------------------------------- 4. bout en bout jouet


def _table_v3_jouet(depot, tmp_path, table_v2_chemin):
    t2 = json.loads(Path(table_v2_chemin).read_text(encoding="utf-8"))
    corriges = [x for x in t2["episodes"] if x["methode"] != "non_resolu"]
    comptes = {k: v for k, v in t2["comptes"].items()}
    for m in rg.METHODES_V3:
        comptes[m] = sum(1 for x in corriges if x["methode"] == m)
    comptes["identiques_apres_table"] = comptes["identiques_base"] + sum(comptes[m] for m in rg.CORRIGEES_V3)
    t3 = {**{k: v for k, v in t2.items() if k not in ("version", "comptes", "episodes")}, "version": 3,
          "comptes": comptes, "episodes": corriges}
    p = tmp_path / "table-jouet-v3.json"
    p.write_text(json.dumps(t3, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(p)
    return p


def _config_v4(depot, f, c, table_v2, table_v3, **k):
    base = {**_config_graine(depot, f, c, table_v2, []), **V2, "chemin_table_v3": str(table_v3),
            "table_v3_sha256": None}
    base.update(k)
    return base


def test_bout_en_bout_jouet_temoin_reparation_table_v4(source, tmp_path, monkeypatch):
    from conftest import committer
    from controle_ia.scellement import verifier

    depot, f, c, tp, pieces0, fmt_j, cl, connus, autres = _preparer(source, tmp_path)
    t3 = _table_v3_jouet(depot, tmp_path, tmp_path / "table0.json")
    committer(depot)
    conf = _config_v4(depot, f, c, tp, t3)
    # configuration : voie non écrite d'avance, lots témoins vides → refus avant tout calcul
    with pytest.raises(GardeArret, match="écrite d'avance"):
        rv.exiger_config({**conf, "voie_si_temoin_non_exact": "lot_fidele"})
    with pytest.raises(GardeArret, match="au moins un lot"):
        rv.exiger_config({**conf, "lots_temoin": []})
    with pytest.raises(GardeArret, match="null en jouet seulement"):
        rv.exiger_config({**conf, "mode": "reel", **{k: "0" * 64 for k in rg.CLES if k.endswith("_sha256")},
                          "table_v3_sha256": "0" * 64, "cibles_attendues": None})
    # témoin sur un lot sans identifiants connus (lot 0 : quatre cassés) : refus, arret.json, aucun résultat
    with pytest.raises(GardeArret, match="sans identifiants connus"):
        rv.executer({**conf, "lots_temoin": [0]}, depot, "20261104-100000-v4-temoin-jouet", None, rv.ETAPE_TEMOIN,
                    autoriser_depot_sale=True, entropie_essai=3)
    assert (depot / "diag" / "20261104-100000-v4-temoin-jouet" / "arret.json").exists()
    # réparation sans témoin : refus avant le manifeste
    with pytest.raises(GardeArret, match="témoin est obligatoire"):
        rv.executer(conf, depot, "20261104-100100-v4-reparation-jouet", None, rv.ETAPE_REPARATION, None,
                    autoriser_depot_sale=True, entropie_essai=3)
    assert not (depot / "runs" / "20261104-100100-v4-reparation-jouet").exists()
    # captures de P3 : échantillon d'équivalence recalculé depuis les graines ; fiches dont un épisode perd une action
    # d'équivalence (actions et empreintes cohérentes entre elles, échantillon faux) → refus (R5)
    fiches_p = depot / "diag" / RUN_P3 / "episodes-p3.json"
    frac = float(pieces0.manifeste_p3["config"]["fraction_equivalence"])
    cap = rv.captures_de_p3(fiches_p, None, pieces0, int(c["T"]), frac)
    assert set(cap) == set(cl) and sum(len(v) for v in cap.values()) >= 4
    d_f = json.loads(fiches_p.read_text(encoding="utf-8"))
    eq = next(x for x in d_f["resultat"]["fiches"] if x["equivalence"]["actions"])["equivalence"]
    k0 = eq["actions"].pop()
    eq["empreintes_capture"].pop(k0)
    fiches_f = depot / "diag" / "fiches-echantillon-faux.json"            # hors de l'arbre gelé
    fiches_f.write_text(json.dumps(d_f), encoding="utf-8")
    sceller(fiches_f)
    with pytest.raises(GardeArret, match="échantillon d'équivalence recalculé"):
        rv.captures_de_p3(fiches_f, None, pieces0, int(c["T"]), frac)
    # ---- témoin (lot 1, quatre connus) : exact
    r_t = rv.executer(conf, depot, "20261104-100200-v4-temoin-jouet", None, rv.ETAPE_TEMOIN,
                      autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    assert r_t["lecture"] == rv.LECTURE_EXACT and r_t["voie_ecrite_d_avance"] == rv.VOIE_LOT
    (lot1,) = r_t["lots"]
    assert lot1["lot"] == 1 and lot1["captures"]["attendues"] == lot1["captures"]["egales"] >= 1
    assert lot1["mesure"]["accord"] == 1.0 and lot1["forme_egale"] and set(lot1["sources"]) == {"identique_base"}
    ch_t = depot / "diag" / "20261104-100200-v4-temoin-jouet" / "resolution-graine-lot-v2-temoin.json"
    assert ch_t.exists() and Path(f"{ch_t}.sha256").exists()
    with pytest.raises(GardeArret, match="R3"):
        rv.executer(conf, depot, "20261104-100250-v4-temoin-jouet", None, rv.ETAPE_TEMOIN,
                    autoriser_depot_sale=True, entropie_essai=3)
    # comptes attendus : faux → arrêt ; justes → passent ; aucune cible → arrêt
    with pytest.raises(GardeArret, match="cibles_attendues = 3"):
        rv.exiger_comptes_attendus({**conf, "cibles_attendues": 3}, autres, [0])
    with pytest.raises(GardeArret, match="lots_cibles_attendus = 2"):
        rv.exiger_comptes_attendus({**conf, "lots_cibles_attendus": 2}, autres, [0])
    rv.exiger_comptes_attendus({**conf, "cibles_attendues": 4, "lots_cibles_attendus": 1}, autres, [0])
    with pytest.raises(GardeArret, match="aucune cible"):
        rv.exiger_comptes_attendus(conf, [], [])
    # ---- réparation, voie du lot : 4 cibles sur 4 retrouvées en un essai à plusieurs cibles
    r_r = rv.executer(conf, depot, "20261104-100300-v4-reparation-jouet", None, rv.ETAPE_REPARATION, str(ch_t),
                      autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    assert r_r["voie"] == rv.VOIE_LOT and r_r["lecture"] == "complète" and sorted(r_r["cibles"]) == sorted(autres)
    assert r_r["empreintes_retrouvees"] == 4 and r_r["par_voie"]["lot_multi"] == 4
    assert r_r["temoin"]["sha256"] == verifier(ch_t) and r_r["temoin"]["lecture"] == rv.LECTURE_EXACT
    assert r_r["lots_a_cible"] == [0] and r_r["lots_rapport"][0]["forme_egale"]
    assert r_r["lots_rapport"][0]["captures_differentes"] == [] and r_r["lots_rapport"][0]["captures_egales"]
    d = depot / "diag" / "20261104-100300-v4-reparation-jouet"
    assert [x["fichier"] for x in r_r["episodes_consignes"]] == [f"episodes-reparation/{k:03d}.json" for k in range(4)]
    assert all((d / (x["fichier"] + ".sha256")).exists() for x in r_r["episodes_consignes"])
    ch_r = d / "resolution-graine-lot-v2-reparation.json"
    # ---- table v4
    table = rv.construire_table_v4(conf, depot, None, str(ch_r), fmt=fmt_j)
    assert table["version"] == 4 and table["comptes"]["cibles_v4"] == 4 and table["comptes"]["retrouvees_v4"] == 4
    assert table["comptes"]["identifiants"] >= 4 and table["non_resolus_v4"] == []
    assert table["corrections_verifiees"] == table["comptes"]["identiques_apres_table"] - table["comptes"]["identiques_base"]
    assert table["comptes"]["identiques_apres_table"] == len(cl)
    sortie = tmp_path / "R1-table-tokenisation-v4-jouet.json"
    sha = rv.ecrire_table_v4(table, sortie)
    assert rv.charger_table_v4(sortie, sha)["version"] == 4
    with pytest.raises(GardeArret, match="R12"):
        rv.ecrire_table_v4(table, sortie)
    with pytest.raises(GardeArret, match="version 3"):
        rv.charger_table_v4(t3, None)
    with pytest.raises(GardeArret, match="empreinte"):
        rv.charger_table_v4(sortie, "0" * 64)
    # artefact : identifiants faux dans le résultat de la réparation (réécrit et rescellé) → refus à la revérification
    corps = json.loads(ch_r.read_text(encoding="utf-8"))
    x0 = corps["resultat"]["episodes"][0]
    x0["ids"][0] = x0["ids"][0][::-1] if len(set(x0["ids"][0])) > 1 else x0["ids"][0][:-1] + [4]
    faux = d / "resolution-graine-lot-v2-reparation-faux.json"
    faux.write_text(json.dumps(corps, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(faux)
    monkeypatch.setattr(rv, "verifier_resultat", lambda racine, chemin: json.loads(Path(chemin).read_text("utf-8")))
    with pytest.raises(GardeArret, match="revérification"):
        rv.construire_table_v4(conf, depot, None, str(faux), fmt=fmt_j)
    monkeypatch.undo()
    # autre configuration : refus
    with pytest.raises(GardeArret, match="autre configuration"):
        rv.construire_table_v4({**conf, "seuil_lecture_lot": 0.5}, depot, None, str(ch_r), fmt=fmt_j)


def test_bout_en_bout_jouet_temoin_non_exact_voie_passe_forcee(source, tmp_path, monkeypatch):
    from conftest import committer

    depot, f, c, tp, pieces0, fmt_j, cl, connus, autres = _preparer(source, tmp_path)
    t3 = _table_v3_jouet(depot, tmp_path, tmp_path / "table0.json")
    committer(depot)
    conf = _config_v4(depot, f, c, tp, t3, seuil_lecture_lot=0.98)
    vrai = rg._modele

    def decale(config, racine, pieces):
        m, fmt = vrai(config, racine, pieces)
        with torch.no_grad():
            w = m.model.layers[0].self_attn.q_proj.weight
            w.view(-1)[0] = torch.nextafter(w.view(-1)[0], torch.tensor(1e9, dtype=w.dtype))
        return m, fmt

    monkeypatch.setattr(rg, "_modele", decale)
    r_t = rv.executer(conf, depot, "20261104-110000-v4-temoin-jouet", None, rv.ETAPE_TEMOIN,
                      autoriser_depot_sale=True, entropie_essai=3)
    monkeypatch.setattr(rg, "_modele", vrai)
    committer(depot)
    assert r_t["lecture"] == rv.LECTURE_NON_EXACT and r_t["voie_ecrite_d_avance"] == rv.VOIE_PASSE
    assert r_t["lots"][0]["captures"]["differentes"]
    ch_t = depot / "diag" / "20261104-110000-v4-temoin-jouet" / "resolution-graine-lot-v2-temoin.json"
    r_r = rv.executer(conf, depot, "20261104-110100-v4-reparation-jouet", None, rv.ETAPE_REPARATION, str(ch_t),
                      autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    assert r_r["voie"] == rv.VOIE_PASSE and r_r["lots_rapport"] == [] and r_r["passes_lot"] == 0
    assert r_r["empreintes_retrouvees"] == 4 and r_r["par_voie"]["passe_forcee"] == 4
    assert all(x["voie"].startswith("passe_forcee:") for x in r_r["episodes"])
    table = rv.construire_table_v4(conf, depot, None, str(depot / "diag" / "20261104-110100-v4-reparation-jouet"
                                                         / "resolution-graine-lot-v2-reparation.json"), fmt=fmt_j)
    assert table["voie"] == rv.VOIE_PASSE and table["comptes"]["retrouvees_v4"] == 4


def test_table_v4_cible_non_retrouvee_entree_non_resolu(source, tmp_path):
    """Une cible non retrouvée reçoit une entrée « non_resolu » (cause recopiée) ; une cible « résolue » sans
    l'empreinte est refusée. Résultat de réparation jouet écrit comme le module l'écrit (manifeste, sceau)."""
    from conftest import committer

    depot, f, c, tp, pieces0, fmt_j, cl, connus, autres = _preparer(source, tmp_path)
    t3 = _table_v3_jouet(depot, tmp_path, tmp_path / "table0.json")
    committer(depot)
    conf = _config_v4(depot, f, c, tp, t3)
    from controle_ia.scellement import verifier

    def resultat(run, episodes):
        m, _ = creer_manifeste(depot, run, conf, ["aucun-tirage-propre"], entropie=3, autoriser_depot_sale=True,
                               commande=f"{rv.COMMANDE} --etape {rv.ETAPE_REPARATION}")
        ch = ecrire_resultat(depot, m, "resolution-graine-lot-v2-reparation",
                             {"etape": rv.ETAPE_REPARATION, "version": rv.VERSION, "cibles": autres,
                              "table_v3_sha256": verifier(t3), "voie": rv.VOIE_PASSE,
                              "temoin": {"lecture": rv.LECTURE_NON_EXACT}, "episodes": episodes})
        committer(depot)
        return str(ch)

    eps = [{"episode": e, "statut": "non_resolu", "ids": None, "empreinte": None,
            "empreinte_cible": pieces0.fiches[e]["trajectoire"], "cause": "jouet : non retrouvé"} for e in autres]
    table = rv.construire_table_v4(conf, depot, None, resultat("20261104-120000-v4-reparation-jouet", eps), fmt=fmt_j)
    assert table["comptes"]["non_resolu"] == 4 and sorted(table["non_resolus_v4"]) == sorted(autres)
    assert all(x["cause_v4"] == "jouet : non retrouvé" for x in table["episodes"] if x["methode"] == "non_resolu")
    eps[0] = {**eps[0], "statut": "resolu", "ids": [[4]], "empreinte": "f" * 64}
    with pytest.raises(GardeArret, match="sans l'empreinte"):
        rv.construire_table_v4(conf, depot, None, resultat("20261104-120100-v4-reparation-jouet", eps), fmt=fmt_j)
    with pytest.raises(GardeArret, match="épisodes du résultat de la réparation ≠ cibles"):
        rv.construire_table_v4(conf, depot, None, resultat("20261104-120200-v4-reparation-jouet", eps[:3]),
                               fmt=fmt_j)
