"""Essais des graines du bras A, texte neuf (brouillon 5, section 6.2) : dérivation conforme au code existant, clés de
la section 6.2, tirages par clé ; gardes sur cas sain et artefact (R5)."""
import hashlib
import importlib.util

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import cle_de_tache, graines
from controle_ia.organismes_discrets import graines_bras_a_v1 as g

ENTROPIE = 20261119
FAB = [f"fab-{k:02d}" for k in range(16)]
VER = [f"ver-{k:02d}" for k in range(16)]
LECTEURS = ("lecteur-claude", "gemini-4-carbon")


def test_derivation_conforme_au_manifeste():
    """6.2, ligne 444 : `SeedSequence(entropie, spawn_key=(cle_de_tache(clé),))`."""
    cle = g.cle("refp")
    ss = np.random.SeedSequence(ENTROPIE, spawn_key=(cle_de_tache(cle),))
    attendu = int(np.random.default_rng(ss).integers(0, 2 ** 63 - 1))
    assert g.graine(cle, ENTROPIE) == graines([cle], ENTROPIE)[cle]
    assert int(g.generateur_de(cle, ENTROPIE).integers(0, 2 ** 63 - 1)) == attendu
    assert g.entier_de(cle, ENTROPIE) == attendu


@pytest.mark.skipif(importlib.util.find_spec("torch") is None, reason="torch absent : lanceur non importable")
def test_graine_entiere_egale_a_celle_du_lanceur():
    from controle_ia.organismes_discrets.lanceur_bras_a_v2 import graine_entiere
    gr = graines(["injection"], ENTROPIE)["injection"]
    assert g.graine_entiere(gr) == graine_entiere(gr)


def test_entropie_absente_ou_fautive_refusee():
    for e in (None, -1, 1.5, True):
        with pytest.raises(GardeArret):
            g.graine(g.cle("ouve"), e)


def test_cles_de_la_base_vingt_neuf():
    cles = g.cles_de_la_base()
    assert len(cles) == 29 and cles[-1] == "bras-a-v2/plis"
    assert "bras-a-v2/base-mots-et-cout/aire/N-029/dose-0.25" in cles
    assert "bras-a-v2/base-mots-et-cout/plancher/transfert/dose-1.00/temoin-identite" in cles
    assert sum(c.startswith("bras-a-v2/base-mots-et-cout/audit-r4/") for c in cles) == 6
    assert sum("/aire/" in c for c in cles) == 13 and sum("/plancher/" in c for c in cles) == 9


def test_cles_fixes_completes_et_distinctes():
    ouvertes, _ = g.couper_ouvertes_gardees(FAB, ENTROPIE)
    cles = g.cles_fixes(FAB, VER, ouvertes, LECTEURS)
    assert len(cles) == len(set(cles))
    assert g.cle("lec6", "ver-00") in cles and g.cle("sent", "ver-03", "e7") in cles
    assert g.cle("perm", "moniteur", "juge-autre-lignee", "dose-0.50") in cles
    assert "bras-a-v2/juge/ver-15/e7/p9" in cles and "bras-a-v2/moniteur-boite-noire/ver-00/e0/p0" in cles
    assert all(c.startswith("bras-a-v2/") for c in cles)
    # la même graine sert à la même position dans les cinq conditions : la clé ne porte pas la condition
    lecture = [c for c in cles if c.startswith(("bras-a-v2/juge/", "bras-a-v2/moniteur-boite-noire/"))]
    assert len(lecture) == 2 * 16 * 80 and not any("dose" in c or "honnete" in c for c in lecture)


def test_cles_gardes():
    with pytest.raises(GardeArret):
        g.cle("inconnu")
    with pytest.raises(GardeArret):
        g.cle_moniteur_modele_de_langue("juge", "t", 8, 0)
    with pytest.raises(GardeArret):
        g.cle_moniteur_modele_de_langue("classifieur", "t", 0, 0)
    with pytest.raises(GardeArret):
        g.forme_dose(0.3)
    with pytest.raises(GardeArret):
        g.cle_action("alea", "t", 0, 0, "lot-inconnu")
    assert g.cle_action("alea", "t", 1, 2, "lot-honnete-appariement") == "bras-a-v2/alea/lot-honnete-appariement/t/e1/p2"
    ouvertes, _ = g.couper_ouvertes_gardees(FAB, ENTROPIE)
    with pytest.raises(GardeArret):
        g.cles_fixes(FAB, VER, ouvertes, ("a", "a"))
    with pytest.raises(GardeArret):
        g.cles_fixes(FAB, FAB, ouvertes, LECTEURS)


def test_cles_distinctes_cas_sain_et_artefact():
    g.exiger_cles_distinctes(["a", "b", "c"])
    with pytest.raises(GardeArret):
        g.exiger_cles_distinctes(["a", "b", "a"])


def test_revision_prefixe():
    assert g.avec_revision(g.cle("ouve")) == "revision/bras-a-v2/ouve"
    with pytest.raises(GardeArret):
        g.avec_revision("revision/bras-a-v2/ouve")
    assert g.entier_de(g.avec_revision(g.cle("refp")), ENTROPIE) != g.entier_de(g.cle("refp"), ENTROPIE)


def test_coupe_ouvertes_gardees_cas_sain_et_artefacts():
    o, gd = g.couper_ouvertes_gardees(FAB, ENTROPIE)
    assert len(o) == len(gd) == 8 and not set(o) & set(gd) and set(o) | set(gd) == set(FAB)
    assert (o, gd) == g.couper_ouvertes_gardees(list(reversed(FAB)), ENTROPIE)     # l'ordre d'entrée n'influe pas
    assert (o, gd) != g.couper_ouvertes_gardees(FAB, ENTROPIE + 1)
    with pytest.raises(GardeArret):
        g.couper_ouvertes_gardees(FAB[:15], ENTROPIE)
    with pytest.raises(GardeArret):
        g.couper_ouvertes_gardees(FAB[:15] + FAB[:1], ENTROPIE)
    g.controler_ouvertes_gardees(FAB, o, gd, VER)
    with pytest.raises(GardeArret):                       # une tâche commune
        g.controler_ouvertes_gardees(FAB, o, gd[:7] + [o[0]], VER)
    with pytest.raises(GardeArret):                       # une tâche d'évaluation présente
        g.controler_ouvertes_gardees(FAB + ["eval-1"], o, gd[:7] + ["eval-1"], VER + ["eval-1"])
    with pytest.raises(GardeArret):                       # une tâche hors de la fabrication
        g.controler_ouvertes_gardees(FAB, o, gd[:7] + ["ver-00"], [])


def test_positions_du_juge():
    p = g.positions_du_juge("ver-00", ENTROPIE)
    assert len(p) == 32 == len(set(p)) and all(0 <= e < 8 and 0 <= s < 10 for e, s in p)
    assert p == g.positions_du_juge("ver-00", ENTROPIE) and p != g.positions_du_juge("ver-01", ENTROPIE)


def test_coupe_puissance():
    a, b = g.coupe_puissance("fab-00", ENTROPIE)
    assert len(a) == len(b) == 4 and sorted(a + b) == list(range(8))
    assert (a, b) == g.coupe_puissance("fab-00", ENTROPIE)


def test_identifiants_opaques_cas_sain_et_artefacts():
    ids = g.identifiants_opaques("lot-honnete-appariement", 2000, ENTROPIE)
    assert len(set(ids)) == 2000 and all(len(i) == 32 for i in ids)
    assert ids == g.identifiants_opaques("lot-honnete-appariement", 2000, ENTROPIE)
    assert ids[:5] != g.identifiants_opaques("lot-decisif", 5, ENTROPIE)
    with pytest.raises(GardeArret):
        g.identifiants_opaques("lot-inconnu", 3, ENTROPIE)
    texte = "TITLE: x\nPROPOSAL: y"
    g.exiger_identifiant_independant(ids[0], [texte])
    with pytest.raises(GardeArret):        # identifiant égal à une empreinte du contenu
        g.exiger_identifiant_independant(hashlib.sha256(texte.encode()).hexdigest()[:32], [texte])
    with pytest.raises(GardeArret):
        g.exiger_identifiant_independant(hashlib.md5(texte.encode()).hexdigest(), [texte])
    with pytest.raises(GardeArret):
        g.exiger_identifiant_independant("xyz", [texte])


def test_ordre_des_appels():
    o = g.ordre_des_appels("lot-decisif", 50, ENTROPIE)
    assert sorted(o) == list(range(50)) and o != list(range(50))
