"""Essais des graines du bras A, version 2 du code (brouillon 6, section 6.2 ; garde neuve de 8.4 « tirage sans clé de
6.2 ») : table fermée des clés sur cas sain et artefacts, révision bornée, tirages rejouables. Aucune donnée réelle."""
import hashlib

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import cle_de_tache
from controle_ia.organismes_discrets import graines_bras_a_v2 as g

ENTROPIE = 20261119
FAB = [f"tache-fab-{i:02d}" for i in range(16)]
VER = [f"tache-ver-{i:02d}" for i in range(16)]

SAINES = [
    "bras-a-v2/ouve", "bras-a-v2/meca/tache-fab-00", "bras-a-v2/meca-ancre", "bras-a-v2/retr/tache-fab-00/e3/claude",
    "bras-a-v2/retr/tache-fab-00/e7/carbon", "bras-a-v2/refp", "bras-a-v2/alea/lot-honnete-appariement/t/e0/p9",
    "bras-a-v2/alea/lot-mecanique-couverture/t/e0/p0", "bras-a-v2/join/texte-sans-rapport", "bras-a-v2/ancr/seconde",
    "bras-a-v2/opaq/lot-decisif", "bras-a-v2/ordr/ancre-couverture", "bras-a-v2/sent/tache-ver-01/e0",
    "bras-a-v2/relu/lot-decisif/actions", "bras-a-v2/relu/lot-decisif/plans", "bras-a-v2/puis/tache-fab-00",
    "bras-a-v2/boot/taches/lot-decisif", "bras-a-v2/boot/taches/lot-jumeaux-couverture",
    "bras-a-v2/boot/taches/prise-de-la-distillation", "bras-a-v2/boot/moniteur/juge-autre-lignee/dose-0.25",
    "bras-a-v2/boot/aire-conditionnelle/classifieur-lexical/dose-1.00", "bras-a-v2/perm/moniteur/moniteur-boite-noire/dose-0.50",
    "bras-a-v2/perm/page", "bras-a-v2/perm/marginales/dose-0.75", "bras-a-v2/lec6/tache-ver-01", "bras-a-v2/plis",
    "bras-a-v2/moniteur-boite-noire/tache-ver-01/e0/p0", "bras-a-v2/juge/tache-ver-01/e7/p9",
    "bras-a-v2/base-mots-et-cout/aire/N-029/dose-0.25", "bras-a-v2/base-mots-et-cout/audit-r4/temoin-identite",
    "revision/bras-a-v2/join/texte-sans-rapport", "revision/bras-a-v2/alea/lot-honnete-appariement/t/e0/p0",
    "revision/bras-a-v2/opaq/ancre-jumeaux", "revision/bras-a-v2/puis/tache-fab-09",
    "revision/bras-a-v2/boot/taches/lot-jumeaux-appariement", "revision/bras-a-v2/ancr/premiere",
]
ARTEFACTS = [
    "bras-a-v2/inconnu", "bras-a-v2/boot/analyse-libre", "bras-a-v2/perm/analyse-libre",       # usage ou analyse hors table
    "bras-a-v2/opaq/lot-inconnu", "bras-a-v2/alea/lot-decisif/t/e0/p0", "bras-a-v2/alea/lot-jumeaux-appariement/t/e0/p0",
    "bras-a-v2/boot/taches/ancre-jumeaux", "bras-a-v2/join/epreuve-inconnue", "bras-a-v2/ancr/troisieme",
    "bras-a-v2/retr/t/e0/gpt", "bras-a-v2/retr/t/e0/claude-opus", "bras-a-v2/boot/moniteur/base/dose-0.50",
    "bras-a-v2/boot/moniteur/juge/dose-0.50", "bras-a-v2/perm/moniteur/classifieur-lexical/dose-0.5",
    "bras-a-v2/perm/moniteur/classifieur-lexical/0.50", "bras-a-v2/perm/moniteur/classifieur-lexical/dose-0.00",
    "bras-a-v2/relu/lot-honnete-appariement", "bras-a-v2/relu/lot-decisif", "bras-a-v2/relu/lot-decisif/sentinelles",
    "bras-a-v2/sent/t/e8", "bras-a-v2/alea/lot-honnete-appariement/t/e0/p10", "bras-a-v2/ouve/x", "bras-a-v2/puis/",
    "bras-a-v2/perm/signes", "ouve", "bras-a-v3/ouve", "", "bras-a-v2/base-mots-et-cout/aire/N-029/dose-0.33",
    "revision/bras-a-v2/sent/t/e0", "revision/bras-a-v2/meca/t", "revision/bras-a-v2/relu/lot-decisif/actions",
    "revision/bras-a-v2/opaq/lot-honnete-couverture", "revision/bras-a-v2/opaq/lot-decisif", "revision/bras-a-v2/ouve",
    "revision/bras-a-v2/alea/lot-mecanique-couverture/t/e0/p0", "revision/bras-a-v2/boot/taches/lot-decisif",
    "revision/bras-a-v2/perm/page", "revision/revision/bras-a-v2/join/texte-sans-rapport",
    "revision/bras-a-v2/base-mots-et-cout/aire/N-029/dose-0.25", "bras-a-v2/revision/join/texte-sans-rapport",
]


@pytest.mark.parametrize("cle", SAINES)
def test_table_fermee_cas_sain(cle):
    g.exiger_cle_de_la_table(cle)
    assert isinstance(g.generateur_de(cle, ENTROPIE), np.random.Generator)


@pytest.mark.parametrize("cle", ARTEFACTS)
def test_table_fermee_artefact_refuse(cle):
    """Garde de 8.4 : usage, lot, épreuve, lecteur, moniteur ou forme de dose hors de la table : tirage refusé."""
    with pytest.raises(GardeArret):
        g.exiger_cle_de_la_table(cle)
    with pytest.raises(GardeArret):
        g.generateur_de(cle, ENTROPIE)


def test_constructeur_de_cle():
    assert g.cle("relu", "lot-decisif", "plans") == "bras-a-v2/relu/lot-decisif/plans"
    assert g.cle("join", "texte-sans-rapport", revision=True) == "revision/bras-a-v2/join/texte-sans-rapport"
    assert g.cle_alea("lot-honnete-appariement", "t/avec/barres", 3, 4) == "bras-a-v2/alea/lot-honnete-appariement/t/avec/barres/e3/p4"
    assert g.cle_retrait("t", 0, "carbon").endswith("/e0/carbon")
    assert g.cle("perm", "moniteur", "juge-autre-lignee", g.forme_dose(0.5)).endswith("dose-0.50")
    for fautif in (lambda: g.cle("relu", "lot-honnete-appariement"), lambda: g.cle("sent", "t", "e0", revision=True),
                   lambda: g.cle_alea("lot-decisif", "t", 0, 0), lambda: g.cle_alea("lot-honnete-appariement", "t", 8, 0),
                   lambda: g.cle_retrait("t", 0, "astra"), lambda: g.cle("puis", ""), lambda: g.cle("puis", 3),
                   lambda: g.forme_dose(0.0), lambda: g.forme_dose(0.3), lambda: g.forme_dose(True),
                   lambda: g.cle_moniteur_modele_de_langue("juge-autre-lignee", "t", 0, 0),
                   lambda: g.cle_sentinelles("t", True)):
        with pytest.raises(GardeArret):
            fautif()
    assert g.cle_moniteur_modele_de_langue("juge", "t", 0, 0) == "bras-a-v2/juge/t/e0/p0"


def test_entropie_et_derivation():
    for fautive in (None, True, -1, 1.5, "7"):
        with pytest.raises(GardeArret):
            g.graine("bras-a-v2/ouve", fautive)
    gr = g.graine("bras-a-v2/refp", ENTROPIE)
    assert gr["spawn_key"] == [str(cle_de_tache("bras-a-v2/refp"))] and gr["entropie"] == str(ENTROPIE)
    attendu = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(cle_de_tache("bras-a-v2/refp"),)))
    assert g.entier_de("bras-a-v2/refp", ENTROPIE) == int(attendu.integers(0, 2 ** 63 - 1))
    assert g.entier_de("bras-a-v2/refp", ENTROPIE) != g.entier_de("revision/bras-a-v2/join/texte-sans-rapport", ENTROPIE)


def test_listes_de_cles():
    ouv, gar = g.couper_ouvertes_gardees(FAB, ENTROPIE)
    cles = g.cles_fixes(FAB, VER, ouv)
    assert len(set(cles)) == len(cles)
    for c in cles:
        g.exiger_cle_de_la_table(c)
    assert sum(c.startswith("bras-a-v2/relu/") for c in cles) == 2
    assert sum("/perm/moniteur/" in c for c in cles) == 20 and sum("/boot/moniteur/" in c for c in cles) == 20
    assert sum("/boot/aire-conditionnelle/" in c for c in cles) == 20 and sum("/perm/marginales/" in c for c in cles) == 4
    assert sum("/boot/taches/" in c for c in cles) == 7 and sum("/puis/" in c for c in cles) == 8
    assert sum("/retr/" in c for c in cles) == 8 * 8 * 2 and all(c.rsplit("/", 1)[1] in g.LECTEURS for c in cles if "/retr/" in c)
    assert len(g.cles_de_la_base()) == 29 and set(g.cles_de_la_base()) <= set(cles)
    rev = g.cles_de_la_revision(gar)
    assert all(c.startswith("revision/bras-a-v2/") for c in rev) and not set(rev) & set(cles)
    assert sum("/puis/" in c for c in rev) == 8 and not any("couverture" in c or "lot-decisif" in c for c in rev)
    with pytest.raises(GardeArret):
        g.cles_fixes(FAB, VER, VER[:8])
    with pytest.raises(GardeArret):
        g.cles_fixes(FAB, FAB, ouv)
    with pytest.raises(GardeArret):
        g.exiger_cles_distinctes(["bras-a-v2/ouve", "bras-a-v2/ouve"])


def test_coupe_ouvertes_gardees_et_separation():
    ouv, gar = g.couper_ouvertes_gardees(FAB, ENTROPIE)
    assert len(ouv) == len(gar) == 8 and not set(ouv) & set(gar) and set(ouv) | set(gar) == set(FAB)
    assert g.couper_ouvertes_gardees(list(reversed(FAB)), ENTROPIE) == (ouv, gar)       # indépendant de l'ordre d'entrée
    assert g.couper_ouvertes_gardees(FAB, ENTROPIE + 1) != (ouv, gar)
    g.controler_ouvertes_gardees(FAB, ouv, gar, VER)                                    # cas sain
    for a in (lambda: g.controler_ouvertes_gardees(FAB, ouv, ouv, VER),                 # tâche commune
              lambda: g.controler_ouvertes_gardees(FAB, ouv[:7] + [VER[0]], gar, VER),   # tâche de vérification
              lambda: g.controler_ouvertes_gardees(FAB, ouv, gar, [gar[0]]),             # tâche d'évaluation présente
              lambda: g.couper_ouvertes_gardees(FAB[:15], ENTROPIE)):
        with pytest.raises(GardeArret):
            a()


def test_tirages_par_cle():
    pos = g.positions_du_juge(VER[0], ENTROPIE)
    assert len(set(pos)) == 32 and all(0 <= e < 8 and 0 <= p < 10 for e, p in pos) and pos == g.positions_du_juge(VER[0], ENTROPIE)
    assert pos != g.positions_du_juge(VER[1], ENTROPIE)
    a, b = g.coupe_puissance(FAB[0], ENTROPIE)
    assert sorted(a + b) == list(range(8)) and len(a) == 4
    c, d = g.coupe_puissance(FAB[0], ENTROPIE, revision=True)                            # autre clé sous la révision
    assert sorted(c + d) == list(range(8)) and len(c) == 4
    assert sorted(g.ordre_des_appels("lot-decisif", 50, ENTROPIE)) == list(range(50))
    with pytest.raises(GardeArret):
        g.ordre_des_appels("lot-inconnu", 5, ENTROPIE)
    with pytest.raises(GardeArret):
        g.ordre_des_appels("lot-decisif", 5, ENTROPIE, revision=True)                    # le lot décisif n'a pas de révision


def test_identifiants_opaques():
    ids = g.identifiants_opaques("lot-honnete-appariement", 100, ENTROPIE)
    assert len(set(ids)) == 100 and all(len(i) == 32 and int(i, 16) >= 0 for i in ids)
    assert g.identifiants_opaques("lot-honnete-appariement", 10, ENTROPIE) == ids[:10]   # rang i indépendant de n
    assert g.identifiants_opaques("lot-jumeaux-appariement", 10, ENTROPIE) != ids[:10]   # une relecture : identifiant neuf
    assert g.identifiants_opaques("lot-honnete-appariement", 10, ENTROPIE, revision=True) != ids[:10]
    with pytest.raises(GardeArret):
        g.identifiants_opaques("lot-honnete-appariement", 0, ENTROPIE)
    contenu = "TITLE: t\nPROPOSAL: p\nCONTROLS: c"
    g.exiger_identifiant_independant(ids[0], [contenu])                                  # cas sain
    for h in (hashlib.sha256, hashlib.sha1, hashlib.md5):                                # artefact : empreinte du contenu
        with pytest.raises(GardeArret):
            g.exiger_identifiant_independant(h(contenu.encode()).hexdigest()[:32], [contenu])
    with pytest.raises(GardeArret):
        g.exiger_identifiant_independant("XYZ", [contenu])
