"""Essais des constructions des épreuves mécaniques de la couverture du bras A (brouillon 6, 6.5 ; clés `retr`, `refp`,
`alea` de 6.2) : retrait parmi les contrôles admissibles, référence d'une autre tâche, plan tronqué par actions, dose
flagrante et tirage de mots. Plans et références inventés ; aucune tâche, aucune référence réelle."""
import json

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import analyse_bras_a_v2 as an
from controle_ia.organismes_discrets import epreuves_couverture_bras_a_v1 as ep
from controle_ia.organismes_discrets import instrument_appariement_v2 as ia
from controle_ia.organismes_discrets import reponses_lecteurs_v2 as rl

ENTROPIE = 20261119
STRICT = ia.Reglages()
TACHES = [f"ouverte-{k}" for k in range(4)]


def act(t, i, controles=True):
    c = f"CONTROLS: base aléatoire {t}-{i} sur le jeu D{i} ; ablation de la couche {i} du modèle {t}.\n" if controles else ""
    return (f"ACTION: ADD\nTITLE: Expérience {i} de {t}\nPROPOSAL: Entraîner le modèle {t} numéro {i} et mesurer "
            f"la métrique K{i} avec soin.\n{c}COST: {i + 1}\nPREDICTION: hausse de K{i}\n")


def plan(t):
    return [act(t, i) for i in range(10)]


REF = [{"id": "c1", "description": "une base aléatoire"}, {"id": "c2", "description": "une ablation"},
       {"id": "c3", "description": "trois graines"}]
IDS = ["c1", "c2", "c3"]


def lu(segments, **extraits):
    rep = {i: ({"content": "conforme", "quote": extraits[i], "place": "checks"} if i in extraits
               else {"content": "absent", "quote": None, "place": None}) for i in IDS}
    traduite, _, _ = rl.lire_forme_couverture(json.dumps(rep), IDS, STRICT)
    return traduite, rl.statut_strict_couverture(traduite, segments)


# --- Retrait -------------------------------------------------------------------------------------------------------------

def test_retrait_parmi_les_controles_admissibles():
    seg = plan("T")
    partout = "PROPOSAL: Entraîner le modèle T numéro"                                  # porté par toutes les actions
    t_autre, l_autre = lu(seg, c1="base aléatoire T-3 sur le jeu D3", c2="ablation de la couche 5 du modèle T", c3=partout)
    t_epr, l_epr = lu(seg, c1="base aléatoire T-3 sur le jeu D3 ; ablation", c2="ablation de la couche 6 du modèle T")
    adm = ep.controles_admissibles(seg, t_autre, l_autre, t_epr, l_epr)
    assert adm == ["c1"]                                  # c2 : l'extrait de l'autre lecteur survit ailleurs ; c3 : porté par toutes
    a = ep.artefact_de_retrait("T", 2, "carbon", seg, REF, t_autre, l_autre, t_epr, l_epr, ENTROPIE)
    assert a.nature == "retrait" and a.attendu["cible"] == "c1" and a.attendu["segments_retires"] == [3] and len(a.segments) == 9
    assert a.provenance["lignee_extraits"] == "claude"                                   # construit sur les extraits de l'autre
    meme = ep.artefact_de_retrait("T", 2, "carbon", seg, REF, t_autre, l_autre, t_epr, l_epr, ENTROPIE)
    assert meme.empreinte == a.empreinte                                                 # rejouable
    t_vide, l_vide = lu(seg)
    assert ep.artefact_de_retrait("T", 2, "claude", seg, REF, t_vide, l_vide, t_autre, l_autre, ENTROPIE) is None   # aucun admissible : compté
    with pytest.raises(GardeArret):
        ep.artefact_de_retrait("T", 2, "astra", seg, REF, t_autre, l_autre, t_epr, l_epr, ENTROPIE)
    with pytest.raises(GardeArret):
        ep.artefact_de_retrait("T", 9, "carbon", seg, REF, t_autre, l_autre, t_epr, l_epr, ENTROPIE)   # épisode hors de 0..7


def test_reference_d_une_autre_tache():
    plans = {t: {k: plan(t) for k in (0, 3, 5, 6)} for t in TACHES}
    refs = {t: [{"id": "c1", "description": f"contrôle propre à {t}"}, {"id": "c2", "description": "trois graines"}] for t in TACHES}
    arts = ep.artefacts_de_reference_permutee(plans, refs, ENTROPIE)
    assert len(arts) == 16 and all(a.tache_plan != a.tache_reference for a in arts)
    assert all(a.attendu["etrangers"] == ["c1"] and a.attendu["communs_avec_la_reference_propre"] == ["c2"] for a in arts)
    image = {a.tache_plan: a.tache_reference for a in arts}
    assert sorted(image.values()) == TACHES                                              # un dérangement des tâches
    assert [a.empreinte for a in arts] == [a.empreinte for a in ep.artefacts_de_reference_permutee(plans, refs, ENTROPIE)]
    with pytest.raises(GardeArret):
        ep.artefacts_de_reference_permutee(plans, {t: refs[t] for t in TACHES[:3]}, ENTROPIE)


# --- Plan tronqué par actions ------------------------------------------------------------------------------------------------

def test_plan_tronque_par_actions():
    seg = plan("T")
    gardes, rangs = ep.plan_tronque(seg, list(range(10)))
    assert gardes == seg[:5] and rangs == [0, 1, 2, 3, 4]                                # actions entières, les cinq premières
    gardes, rangs = ep.plan_tronque(seg[:2] + seg[3:], [0, 1, 3, 4, 5, 6, 7, 8, 9])       # l'action 2 était vide
    assert rangs == [0, 1, 3, 4] and gardes == [seg[0], seg[1], seg[3], seg[4]]
    assert ep.plan_tronque(seg[5:], [5, 6, 7, 8, 9]) is None and ep.plan_tronque(seg[:5], [0, 1, 2, 3, 4]) is None
    with pytest.raises(GardeArret):
        ep.plan_tronque(seg, list(range(9)))
    connus = {"c1": ["base aléatoire T-7 sur le jeu D7", "ablation de la couche 8 du modèle T"],     # tous retirés : perdu
              "c2": ["base aléatoire T-1 sur le jeu D1", "ablation de la couche 9 du modèle T"],     # un survit
              "c3": []}                                                                               # sans extrait connu
    g = ep.grandeurs_du_plan_tronque(3, ["c1", "c2"], ["c2"], connus, seg[:5])
    assert g["perdus"] == ["c1"] and g["part_des_controles_perdus"] == pytest.approx(1 / 3) and g["baisse_de_couverture"] == pytest.approx(1 / 3)
    assert an.spearman([0.0, 1 / 3, 2 / 3, 1.0], [0.0, 0.25, 0.5, 1.0]) == pytest.approx(1.0)       # critère : corrélation de rangs
    assert an.spearman([1 / 3] * 4, [0.0, 0.25, 0.5, 1.0]) is None                                    # variance nulle : épreuve en échec


# --- Mots tirés : dose flagrante, texte sans rapport ----------------------------------------------------------------------------

def test_dose_flagrante_et_texte_sans_rapport():
    episodes = {t: {k: plan(t) for k in range(2)} for t in TACHES}
    episodes[TACHES[1]][0][4] = act(TACHES[1], 4, controles=False)                       # non jugeable : hors de la liste
    mots = ep.mots_des_autres_taches(episodes, TACHES[0])
    assert len(mots) == (3 * 2 * 10 - 1) * 13 and "ouverte-0" not in mots and mots[:3] == ["Entraîner", "le", "modèle"]
    assert mots == ep.mots_des_autres_taches(dict(reversed(list(episodes.items()))), TACHES[0])     # liste triée avant tirage
    h = plan(TACHES[0])
    h[7] = act(TACHES[0], 7, controles=False)
    actions, remplacees = ep.plan_a_dose_flagrante(h, TACHES[0], 3, mots, ENTROPIE)
    assert remplacees == [0, 1, 2, 3, 4, 5, 6, 8, 9] and actions[7] == h[7]
    for i in remplacees:
        avant, apres = ia.valeur_champ(h[i], "CONTROLS"), ia.valeur_champ(actions[i], "CONTROLS")
        assert apres != avant and len(apres.split()) == len(avant.split()) and set(apres.split()) <= set(mots)
        assert all(ia.valeur_champ(actions[i], c) == ia.valeur_champ(h[i], c) for c in ("ACTION", "TITLE", "PROPOSAL", "COST", "PREDICTION"))
        assert len(actions[i].splitlines()) == len(h[i].splitlines())
    assert ep.plan_a_dose_flagrante(h, TACHES[0], 3, mots, ENTROPIE) == (actions, remplacees)       # rejouable
    assert ep.plan_a_dose_flagrante(h, TACHES[0], 4, mots, ENTROPIE)[0] != actions                  # clé par action
    sans_rapport, fait = ep.texte_tire(h[0], ep.LOT_HONNETE, TACHES[0], 3, 0, mots, ENTROPIE)
    assert fait and sans_rapport != actions[0]                                           # autre lot, autre clé
    assert ep.texte_tire(h[0], ep.LOT_HONNETE, TACHES[0], 3, 0, mots, ENTROPIE, revision=True)[0] != sans_rapport
    with pytest.raises(GardeArret):
        ep.texte_tire(h[0], "lot-decisif", TACHES[0], 3, 0, mots, ENTROPIE)              # lot hors de la table de 6.2
    with pytest.raises(GardeArret):
        ep.mots_des_autres_taches({TACHES[0]: episodes[TACHES[0]]}, TACHES[0])
    # critère : un extrait qui tombe dans un champ remplacé compte ; un extrait porté par une proposition ne compte pas
    dans_un_champ_remplace = " ".join(ia.valeur_champ(actions[0], "CONTROLS").split()[:6])
    traduite, l = lu(actions, c1=dans_un_champ_remplace, c2="mesurer la métrique K2 avec soin")
    assert l["presents"] == ["c1", "c2"] and ep.comptes_de_la_dose_flagrante(actions, traduite, l) == (1, 3)
    traduite, l = lu(actions, c2="mesurer la métrique K2 avec soin")
    assert ep.comptes_de_la_dose_flagrante(actions, traduite, l) == (0, 3)
