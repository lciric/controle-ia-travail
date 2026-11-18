"""Essai de bout en bout du cœur de la course du bras A sur le modèle jouet (processeur) : épisodes honnêtes, fabrication
au grain du jeton, distillation d'un adaptateur par condition, contrôle d'identité, rejeu ; cas sains et artefacts (R5)."""
import sys

import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.organismes import lora as lo
from controle_ia.organismes_discrets import lanceur_bras_a_v1 as la
from controle_ia.t06.identite import logits_de_controle

ENTROPIE = 20261118
CONFIG = {"T": 4, "lot": 2, "episodes_par_tache": 2, "couches": [1], "max_nouveaux": 6, "temperature": 1.0,
          "tolerance_equivalence": 0.2, "doses_fabrication": [0.5, 1.0], "proportions_temoin_benin": [1.0],
          "adaptateur": {"rang": 2, "alpha": 4, "cibles": ["q_proj", "k_proj", "v_proj", "o_proj"]},
          "distillation": {"epoques": 1, "lot": 2, "pas": 1e-3, "norme_max": 1.0, "pas_declares": 2}}
FAB = [{"identifiant": f"fab-{i}", "questions": f"Question de fabrication {i} ?"} for i in range(2)]
VER = [{"identifiant": f"ver-{i}", "questions": f"Question de verification {i} ?"} for i in range(2)]


def test_aucun_module_de_sondes_charge():
    interdits = ("sondes", "bases", "t07", "couche2", "agregateurs", "mots_et_cout", "t08", "lecture")
    assert not [m for m in sys.modules if m.startswith("controle_ia") and any(k in m for k in interdits)]


def test_plan_des_adaptateurs():
    assert [n for n, _, _ in la.plan_des_adaptateurs(CONFIG)] == ["controls-0.50", "controls-1.00", "identite", "prediction-1.00"]
    for ecart in ({"doses_fabrication": [0.0, 1.0]}, {"doses_fabrication": [0.3]}, {"doses_fabrication": []},
                  {"proportions_temoin_benin": []}, {"doses_fabrication": [0.5, 0.5]}):
        with pytest.raises(GardeArret):
            la.plan_des_adaptateurs(dict(CONFIG, **ecart))


@pytest.fixture(scope="module")
def monde():
    modele, fmt = la.charger_modele_et_format({}, "jouet", 7)
    g = graines(la.cles_des_graines(CONFIG, FAB, VER), ENTROPIE)
    return modele, fmt, g


def scripte(fmt, taches):
    """Épisodes de fabrication écrits à la main (le modèle jouet ne produit pas de champs) : identifiants = tokenisation par
    caractères du texte, plus le jeton de fin."""
    fin = fmt.tok.eos_token_id
    episodes = []
    for t in taches:
        for k in range(CONFIG["episodes_par_tache"]):
            textes = [f"ACTION: ADD\nTITLE: t{i}\nPROPOSAL: p{i}{k}\nCONTROLS: c{i}{k} a\nCOST: {i + 1}\nPREDICTION: e{i}{k}\n"
                      for i in range(CONFIG["T"])]
            actions = [fmt.tok(x, add_special_tokens=False)["input_ids"] + [fin] for x in textes]
            assert [fmt.tok.decode(a, skip_special_tokens=True) for a in actions] == textes
            episodes.append({"episode": f"fabrication/{t['identifiant']}/e{k}", "tache": t, "k": k, "actions": actions, "textes": textes})
    return episodes


def test_bout_en_bout(monde):
    modele, fmt, g = monde
    # 1. épisodes honnêtes du modèle de base : forme, et reproductibilité par les graines
    honnetes = la.jouer_honnetes(modele, fmt, VER, CONFIG, g, None, "verification")
    assert len(honnetes) == 4 and all(len(e["actions"]) == CONFIG["T"] for e in honnetes)
    assert la.empreinte_des_episodes(honnetes) == la.empreinte_des_episodes(
        la.jouer_honnetes(modele, fmt, VER, CONFIG, g, None, "verification"))
    # 2. fabrication sur des épisodes à champs
    episodes = scripte(fmt, FAB)
    plein = la.fabriquer(fmt, episodes, "CONTROLS", 1.0, ENTROPIE, CONFIG, None)
    assert plein["bilan"]["actions_deplacees"] == 16 and plein["bilan"]["episodes_laisses_honnetes"] == 0
    for avant, apres in zip(episodes, plein["episodes"]):
        assert sorted(x for a in avant["actions"] for x in a) == sorted(x for a in apres["actions"] for x in a)   # M-3
        for i, (ta, tb) in enumerate(zip(avant["textes"], apres["textes"])):
            assert ta != tb and ta.split("CONTROLS:")[0] == tb.split("CONTROLS:")[0]
            assert ta.split("COST:")[1] == tb.split("COST:")[1]                # COST et PREDICTION jamais touchés
            j = int(apres["deplacements"][str(i)])
            assert tb.split("CONTROLS:")[1].split("COST:")[0] == avant["textes"][j].split("CONTROLS:")[1].split("COST:")[0]
    identite = la.fabriquer(fmt, episodes, None, 1.0, ENTROPIE, CONFIG, None)
    assert [e["actions"] for e in identite["episodes"]] == [e["actions"] for e in episodes]
    benin = la.fabriquer(fmt, episodes, "PREDICTION", 1.0, ENTROPIE, CONFIG, None)
    assert all(a.split("PREDICTION:")[0] == b.split("PREDICTION:")[0] and a != b
               for x, y in zip(episodes, benin["episodes"]) for a, b in zip(x["textes"], y["textes"]))
    # 3. exemples : seules les cibles d'action changent
    ex_a, ex_i = la.exemples(fmt, plein["episodes"], CONFIG, None), la.exemples(fmt, identite["episodes"], CONFIG, None)
    for (ia, ea), (ii, ei) in zip(ex_a, ex_i):
        assert len(ia) == len(ii) and ia != ii
        assert [x for x, e in zip(ia, ea) if e == -100] == [x for x, e in zip(ii, ei) if e == -100]   # contexte identique
    # 4. artefact : nombre de pas déclaré faux → arrêt avant toute injection
    with pytest.raises(GardeArret, match="addendum 2"):
        la.distiller_tous(modele, fmt, episodes, dict(CONFIG, distillation=dict(CONFIG["distillation"], pas_declares=3)),
                          g, None, ENTROPIE, fmt.tok.pad_token_id)
    assert not lo.modules_lora(modele)
    # 5. distillation
    ids_controle = ex_i[0][0][:64]
    logits_base = logits_de_controle(modele, ids_controle)
    res = la.distiller_tous(modele, fmt, episodes, CONFIG, g, None, ENTROPIE, fmt.tok.pad_token_id)
    ad = res["adaptateurs"]
    assert list(ad) == ["controls-0.50", "controls-1.00", "identite", "prediction-1.00"]
    assert all(x["pas_calcules"] == x["pas_declares"] == 2 for x in ad.values())
    assert ad["controls-1.00"]["bilan_fabrication"]["actions_deplacees"] == 16
    assert ad["controls-0.50"]["bilan_fabrication"]["actions_deplacees"] == 8
    assert ad["identite"]["bilan_fabrication"]["actions_deplacees"] == 0
    assert len({x["empreinte"] for x in ad.values()}) == 4 and lo.empreinte_base(modele) == res["empreinte_base"]
    # 6. identité à l'échelle 0, écart à l'échelle 1 (M-4), et son artefact
    controle = la.controler_identite(modele, ids_controle, logits_base, ad)
    assert all(c["dose_0_identique"] and c["dose_1_differente"] for c in controle.values())
    nul = {"x": {"etat": {k: torch.zeros_like(v) for k, v in ad["identite"]["etat"].items()}}}
    with pytest.raises(GardeArret, match="artefact"):
        la.controler_identite(modele, ids_controle, logits_base, nul)
    # 7. rejeu : la condition honnête, adaptation à l'échelle 0, rend les épisodes de la base au bit près
    rejeu = la.rejouer(modele, fmt, VER, CONFIG, g, None, ad)
    assert list(rejeu) == ["H"] + list(ad)
    assert la.empreinte_des_episodes(rejeu["H"]) == la.empreinte_des_episodes(honnetes)
    assert all(len(v) == 4 and [e["episode"] for e in v] == [e["episode"] for e in honnetes] for v in rejeu.values())
