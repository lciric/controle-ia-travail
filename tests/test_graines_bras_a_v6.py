"""Essais des graines du bras A, version 6 du code (brouillon 24, 6.2 ; R9). Les essais de la table des clés sont
ceux des versions 4 et 5, repris sur le module de la version 6. Changent, d'après la contre-lecture du code de la
version 5 et ses essais d'attaque (`attaques_graines_v1.py`) : un tirage à clé ne se fabrique que par ses fabriques et
ne sert qu'une fois (M-1) ; la porte de l'écart à R9 lit le registre du dépôt et une forme fixe de la ligne d'accord
(M-2 ; registre fabriqué dans l'essai) ; ligne d'accord d'une livraison refaite."""
import hashlib
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import cle_de_tache
from controle_ia.organismes_discrets import graines_bras_a_v6 as g

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
    "bras-a-v2/boot/taches/prise-de-la-distillation",
    "bras-a-v2/boot/aire-conditionnelle/classifieur-lexical/dose-1.00", "bras-a-v2/boot/aire-conditionnelle/juge/dose-0.25",
    "bras-a-v2/perm/page",
    "revision/bras-a-v2/join/texte-sans-rapport", "revision/bras-a-v2/alea/lot-honnete-appariement/t/e0/p0",
    "revision/bras-a-v2/opaq/ancre-jumeaux", "revision/bras-a-v2/puis/tache-fab-09",
    "revision/bras-a-v2/boot/taches/lot-jumeaux-appariement", "revision/bras-a-v2/ancr/premiere",
]
# Clés de 6.2 tirées côté habilité : reconnues par la garde, jamais tirées par la relance.
RECONNUES = [
    "bras-a-v2/boot/moniteur/juge/dose-0.25", "bras-a-v2/perm/moniteur/moniteur-boite-noire/dose-0.50", "bras-a-v2/plis",
    "bras-a-v2/perm/moniteur/juge/dose-1.00", "bras-a-v2/boot/moniteur/agregateur-sequentiel/dose-0.75",
    "bras-a-v2/moniteur-boite-noire/tache-ver-01/e0/p0", "bras-a-v2/juge/tache-ver-01/e7/p9",
    "bras-a-v2/base-mots-et-cout/aire/N-029/dose-0.25", "bras-a-v2/base-mots-et-cout/audit-r4/temoin-identite",
    "bras-a-v2/lec6/tache-ver-01",                       # sous-échantillon du juge : étape de préparation, côté habilité
]
ARTEFACTS = [
    "bras-a-v2/inconnu", "bras-a-v2/boot/analyse-libre", "bras-a-v2/perm/analyse-libre",       # usage ou analyse hors table
    "bras-a-v2/opaq/lot-inconnu", "bras-a-v2/opaq/moniteurs", "revision/bras-a-v2/opaq/moniteurs",
    "bras-a-v2/alea/lot-decisif/t/e0/p0", "bras-a-v2/alea/lot-jumeaux-appariement/t/e0/p0",
    "bras-a-v2/boot/taches/ancre-jumeaux", "bras-a-v2/join/epreuve-inconnue", "bras-a-v2/ancr/troisieme",
    "bras-a-v2/retr/t/e0/gpt", "bras-a-v2/retr/t/e0/claude-opus", "bras-a-v2/boot/moniteur/base/dose-0.50",
    "bras-a-v2/boot/moniteur/juge-autre-lignee/dose-0.50", "bras-a-v2/perm/moniteur/juge-autre-lignee/dose-1.00",
    "bras-a-v2/boot/aire-conditionnelle/juge-autre-lignee/dose-1.00", "bras-a-v2/perm/aire-conditionnelle/juge/dose-1.00",
    "bras-a-v2/perm/marginales/dose-0.75", "bras-a-v2/perm/moniteur/classifieur-lexical/dose-0.5",
    "bras-a-v2/alea/lot-honnete-appariement/t/avec/barres/e0/p9", "bras-a-v2/meca/a/b", "bras-a-v2/puis/a/b",
    "bras-a-v2/lec6/a/b", "bras-a-v2/juge/a/b/e0/p0", "bras-a-v2/sent/a/b/e0", "revision/bras-a-v2/puis/a/b",
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


@pytest.mark.parametrize("cle", RECONNUES)
def test_cles_du_cote_habilite_reconnues_non_tirees(cle):
    """6.2 : les quarante et une clés de la lecture commune, les clés de la base et les clés de lecture des deux
    moniteurs à modèle de langue passent la garde « tirage sans clé » (cas sain), mais la relance refuse de les tirer."""
    g.exiger_cle_de_la_table(cle)
    assert g.tiree_cote_habilite(cle)
    for tirage in (g.graine, g.generateur_de, g.entier_de):
        with pytest.raises(GardeArret):
            tirage(cle, ENTROPIE)


def test_partage_des_soixante_et_une_cles():
    habilite, analyse = g.cles_cote_habilite_de_la_lecture_commune(), g.cles_de_l_aire_conditionnelle()
    assert len(habilite) == 41 and len(analyse) == 20 and not set(habilite) & set(analyse)
    assert sum("/boot/moniteur/" in c for c in habilite) == 20 and sum("/perm/moniteur/" in c for c in habilite) == 20
    assert "bras-a-v2/plis" in habilite and all(g.tiree_cote_habilite(c) for c in habilite)
    for c in analyse:                                     # tirées ici, par l'instance d'analyse
        assert not g.tiree_cote_habilite(c) and isinstance(g.generateur_de(c, ENTROPIE), np.random.Generator)
    assert g.cle_aire_conditionnelle("juge", 0.25) == "bras-a-v2/boot/aire-conditionnelle/juge/dose-0.25" in analyse
    assert len({g.entier_de(c, ENTROPIE) for c in analyse}) == 20
    for fautif in (lambda: g.cle_aire_conditionnelle("juge-autre-lignee", 0.5), lambda: g.cle_aire_conditionnelle("juge", 0.0),
                   lambda: g.cle_aire_conditionnelle("base", 0.5)):
        with pytest.raises(GardeArret):
            fautif()


def test_identifiant_de_tache_avec_barre_arrete():
    """Garde de 6.2 et de 8.4 : « identifiant de tâche qui contient « / » : arrêt », dans chaque constructeur."""
    assert g.exiger_tache("tache-ver-01") == "tache-ver-01"                              # cas sain
    for fautif in (lambda: g.exiger_tache("a/b"), lambda: g.exiger_tache(""), lambda: g.exiger_tache(None),
                   lambda: g.exiger_tache("a\nb"),
                   lambda: g.cle_alea("lot-honnete-appariement", "t/avec/barres", 3, 4),
                   lambda: g.cle_retrait("a/b", 0, "claude"), lambda: g.cle_sentinelles("a/b", 0),
                   lambda: g.cle("meca", "a/b"), lambda: g.cle("puis", "a/b", revision=True), lambda: g.cle("lec6", "a/b"),
                   lambda: g.cle_moniteur_modele_de_langue("juge", "a/b", 0, 0),
                   lambda: g.coupe_puissance("a/b", ENTROPIE),
                   lambda: g.cles_fixes(FAB[:15] + ["fab/15"], VER, FAB[:8]),
                   lambda: g.cles_de_la_revision(FAB[:7] + ["fab/7"])):
        with pytest.raises(GardeArret):
            fautif()


def test_constructeur_de_cle():
    assert g.cle("relu", "lot-decisif", "plans") == "bras-a-v2/relu/lot-decisif/plans"
    assert g.cle("join", "texte-sans-rapport", revision=True) == "revision/bras-a-v2/join/texte-sans-rapport"
    assert g.cle_alea("lot-honnete-appariement", "t", 3, 4, revision=True) == "revision/bras-a-v2/alea/lot-honnete-appariement/t/e3/p4"
    assert g.cle_retrait("t", 0, "carbon").endswith("/e0/carbon")
    assert g.cle("perm", "moniteur", "juge", g.forme_dose(0.5)) == "bras-a-v2/perm/moniteur/juge/dose-0.50"
    for fautif in (lambda: g.cle("relu", "lot-honnete-appariement"), lambda: g.cle("sent", "t", "e0", revision=True),
                   lambda: g.cle_alea("lot-decisif", "t", 0, 0), lambda: g.cle_alea("lot-honnete-appariement", "t", 8, 0),
                   lambda: g.cle_retrait("t", 0, "astra"), lambda: g.cle("puis", ""), lambda: g.cle("puis", 3),
                   lambda: g.forme_dose(0.0), lambda: g.forme_dose(0.3), lambda: g.forme_dose(True),
                   lambda: g.cle_moniteur_modele_de_langue("juge-autre-lignee", "t", 0, 0),
                   lambda: g.cle("perm", "moniteur", "juge-autre-lignee", g.forme_dose(0.5)),
                   lambda: g.cle("perm", "marginales", g.forme_dose(0.5)),
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
    assert sum("/boot/aire-conditionnelle/" in c for c in cles) == 20 and not any("/perm/marginales/" in c for c in cles)
    assert not any("juge-autre-lignee" in c for c in cles)
    tirees = g.cles_tirees_par_la_relance(FAB, VER, ouv)
    assert set(g.cles_de_l_aire_conditionnelle()) <= set(tirees) and not set(tirees) & set(g.cles_cote_habilite_de_la_lecture_commune())
    assert not any(g.tiree_cote_habilite(c) for c in tirees)
    # lecture commune, base, lectures des deux moniteurs, sous-échantillon du juge (seize clés `lec6`)
    assert len(cles) - len(tirees) == 41 + 28 + 2 * 16 * 8 * 10 + 16 and not any("/lec6/" in c for c in tirees)
    for c in tirees:
        g.graine(c, ENTROPIE)
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
    assert not hasattr(g, "positions_du_juge")                 # 6.2 : le sous-échantillon du juge se tire côté habilité
    with pytest.raises(GardeArret, match="côté habilité"):
        g.generateur_de(g.cle("lec6", VER[0]), ENTROPIE)
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


def test_le_module_de_la_version_6_reprend_la_table_de_la_version_4():
    from controle_ia.organismes_discrets import graines_bras_a_v4 as g4
    assert g.TABLE is g4.TABLE and g.TABLE_REVISION is g4.TABLE_REVISION and g.cle is g4.cle and g.LOTS == g4.LOTS
    assert g.admettre_l_entropie_propre_de_la_table_des_identifiants is not g4.admettre_l_entropie_propre_de_la_table_des_identifiants


def test_tirage_a_cle_et_garde_au_point_du_tirage():
    """La garde « tirage sans clé de 6.2 » mord au moment du tirage. Cas sain : un tirage fabriqué par `tirage_de`,
    demandé pour son usage — même suite que `generateur_de` sur la même clé. Artefacts : générateur nu, générateur du
    système, clé d'un autre usage, clé exigée différente, clé hors de la table, clé du côté habilité, entropie fautive."""
    cle = g.cle("boot", "taches", "lot-decisif")
    t = g.tirage_de(cle, ENTROPIE)
    assert t.cle == cle and t.entropie == ENTROPIE and not t.cote_habilite and cle in repr(t)
    a = g.generateur_pour(t, g.USAGE_TACHES).integers(0, 10 ** 9, size=5)
    assert list(a) == list(g.generateur_de(cle, ENTROPIE).integers(0, 10 ** 9, size=5))               # la même dérivation
    assert g.generateur_pour(g.tirage_de(cle, ENTROPIE), g.USAGE_TACHES, cle) is not None
    for usage, c in ((g.USAGE_PAGE, g.cle("perm", "page")), (g.USAGE_TACHES, g.cle("boot", "taches", "prise-de-la-distillation")),
                     (g.USAGE_TACHES, g.cle("boot", "taches", "lot-jumeaux-appariement", revision=True)),
                     (g.USAGE_AIRE_CONDITIONNELLE, g.cle_aire_conditionnelle("juge", 0.5))):
        assert isinstance(g.generateur_pour(g.tirage_de(c, ENTROPIE), usage), np.random.Generator)
    assert g.tirage_de_l_aire_conditionnelle("juge", 0.5, ENTROPIE).cle == "bras-a-v2/boot/aire-conditionnelle/juge/dose-0.50"
    for nu in (np.random.default_rng(), np.random.default_rng(3), g.generateur_de(cle, ENTROPIE), None, cle, 3):
        with pytest.raises(GardeArret, match="sans clé"):
            g.generateur_pour(nu, g.USAGE_TACHES)
    for usage in (g.USAGE_PAGE, g.USAGE_AIRE_CONDITIONNELLE, g.USAGE_PERMUTATION_D_UN_MONITEUR):         # clé d'un autre usage
        with pytest.raises(GardeArret):
            g.generateur_pour(g.tirage_de(cle, ENTROPIE), usage)
    with pytest.raises(GardeArret):
        g.tirage_de("revision/bras-a-v2/boot/taches/lot-decisif", ENTROPIE)
    with pytest.raises(GardeArret, match="exigée"):
        g.generateur_pour(g.tirage_de_l_aire_conditionnelle("juge", 0.5, ENTROPIE), g.USAGE_AIRE_CONDITIONNELLE,
                          g.cle_aire_conditionnelle("juge", 0.75))
    with pytest.raises(GardeArret):
        g.generateur_pour(g.tirage_de(cle, ENTROPIE), "usage inconnu")
    for fautive in ("bras-a-v2/boot/quelconque", "boot/taches/lot-decisif", "bras-a-v2/perm/moniteur/juge/dose-0.50",
                    "bras-a-v2/plis", "bras-a-v2/lec6/t1"):
        with pytest.raises(GardeArret):
            g.tirage_de(fautive, ENTROPIE)
    for entropie in (None, True, -1, 1.5):
        with pytest.raises(GardeArret):
            g.tirage_de(cle, entropie)
    with pytest.raises(GardeArret):
        t.cle = "bras-a-v2/perm/page"
    # clés du côté habilité : une fabrique à part, pour la seule lettre du schéma de permutation
    h = g.tirage_reconnu_cote_habilite("bras-a-v2/perm/moniteur/juge/dose-0.50", ENTROPIE)
    assert h.cote_habilite and isinstance(g.generateur_pour(h, g.USAGE_PERMUTATION_D_UN_MONITEUR), np.random.Generator)
    with pytest.raises(GardeArret):                                                                       # jamais pour un tirage de l'analyse
        g.generateur_pour(g.tirage_reconnu_cote_habilite("bras-a-v2/perm/moniteur/juge/dose-0.50", ENTROPIE), g.USAGE_TACHES)
    for fautive in (cle, "bras-a-v2/boot/moniteur/juge/dose-0.50", "bras-a-v2/perm/page", "bras-a-v2/perm/moniteur/base/dose-0.50"):
        with pytest.raises(GardeArret):
            g.tirage_reconnu_cote_habilite(fautive, ENTROPIE)
    with pytest.raises(GardeArret):
        g.tirage_reconnu_cote_habilite("bras-a-v2/perm/moniteur/juge/dose-0.50", None)


def test_m1_un_tirage_ne_se_fabrique_que_par_ses_fabriques_et_ne_sert_qu_une_fois():
    """Contre-lecture du code de la version 5, M-1, et ses essais d'attaque. Artefacts : un tirage fabriqué **avec le
    jeton du module** et un générateur du système ; un tirage fabriqué par `object.__new__` ; **un tirage réemployé**
    (il rendait deux intervalles différents). Cas sain : deux tirages refaits de la même clé partent du même point —
    un rejeu ne dépend pas de l'ordre d'emploi."""
    from controle_ia.organismes_discrets import analyse_bras_a_v6 as an
    page = "bras-a-v2/perm/page"
    blocs = np.arange(10).reshape(5, 2) * 1.0
    avec_le_jeton = g.TirageAClef(g._JETON, page, 0, np.random.default_rng(), False)                     # attaque 1
    a_la_main = object.__new__(g.TirageAClef)                                                            # attaque 2
    for nom, valeur in (("cle", page), ("entropie", 0), ("cote_habilite", False), ("_generateur", np.random.default_rng())):
        object.__setattr__(a_la_main, nom, valeur)
    for faux in (avec_le_jeton, a_la_main):
        with pytest.raises(GardeArret, match="fabriqué à la main"):
            an.page(blocs, faux, n=50)
        with pytest.raises(GardeArret, match="fabriqué à la main"):
            g.generateur_pour(faux, g.USAGE_PAGE)
    with pytest.raises(GardeArret, match="tirage_de"):                                                    # sans le jeton
        g.TirageAClef(object(), page, 1, np.random.default_rng(), False)
    assert an.page(blocs, g.tirage_de(page, 0), n=50)[1] > 0                                             # cas sain
    cle = g.cle("boot", "taches", "lot-decisif")
    valeurs = {f"t{i}": float(i) for i in range(16)}
    tirage = g.tirage_de(cle, 7)
    premier = an.intervalle_rapporte(valeurs, tirage)["percentiles"]
    with pytest.raises(GardeArret, match="déjà servi"):                                                   # attaque 3 : réemploi
        an.intervalle_rapporte(valeurs, tirage)
    with pytest.raises(GardeArret, match="déjà servi"):
        g.generateur_pour(tirage, g.USAGE_TACHES)
    assert an.intervalle_rapporte(valeurs, g.tirage_de(cle, 7))["percentiles"] == premier                # refait : le même intervalle
    # l'ordre d'emploi ne change rien : deux grandeurs d'un même lot, dans un ordre ou dans l'autre
    autres = {t: 2 * x for t, x in valeurs.items()}
    a = (an.intervalle_rapporte(valeurs, g.tirage_de(cle, 7)), an.intervalle_rapporte(autres, g.tirage_de(cle, 7)))
    b = (an.intervalle_rapporte(autres, g.tirage_de(cle, 7)), an.intervalle_rapporte(valeurs, g.tirage_de(cle, 7)))
    assert a == (b[1], b[0])
    # un tirage rendu à la mémoire ne laisse pas sa marque à un autre (l'identité n'est pas réemployée à tort)
    for _ in range(200):
        assert isinstance(g.generateur_pour(g.tirage_de(page, 1), g.USAGE_PAGE), np.random.Generator)


LIGNES_DU_REGISTRE = {
    "bon": "| GO-2026-11-20-01 | 2026-11-20 | décision | Écart à R9 accordé pour la table des identifiants opaques (bras A) | Lazar |",
    "refus": "| GO-2026-11-20-02 | 2026-11-20 | décision | Lazar refuse l'écart à R9 pour la table des identifiants | — |",
    "refus_avec_la_phrase": "| GO-2026-11-20-03 | 2026-11-20 | décision | refus : écart à R9 accordé pour la table des identifiants opaques ? non | Lazar |",
    "autre": "| GO-2026-11-20-04 | 2026-11-20 | calcul | devis de la course des cartes | Lazar |",
    "double_1": "| GO-2026-11-20-05 | 2026-11-20 | décision | écart à R9 accordé pour la table des identifiants opaques | Lazar |",
    "double_2": "| GO-2026-11-20-05 | 2026-11-20 | décision | écart à R9 accordé pour la table des identifiants opaques, bis | Lazar |",
    "approchant": "| GO-2026-11-20-06 | 2026-11-20 | décision | écart à R9, table des identifiants : accordé | Lazar |",
    "livraison": "| GO-2026-11-20-07 | 2026-11-20 | décision | Livraison refaite du côté habilité accordée pour le bras A | Lazar |",
}


@pytest.fixture
def registre(tmp_path, monkeypatch):
    f = tmp_path / "go.md"
    f.write_text("# Registre des accords (fabriqué pour l'essai)\n\n| identifiant | date | nature | objet |\n|---|---|---|---|\n"
                 + "".join(l + "\n" for l in LIGNES_DU_REGISTRE.values())
                 + "Dans le texte : GO-2026-11-20-09 est cité ici, écart à R9 accordé pour la table des identifiants opaques, hors de la table.\n",
                 encoding="utf-8")
    monkeypatch.setattr(g, "REGISTRE_DES_ACCORDS", f)
    return f


def test_entropie_propre_de_la_table_des_identifiants_refusee_par_defaut(registre, monkeypatch, tmp_path):
    """6.2 et 8.4 : l'entropie propre de la table des identifiants opaques est un tirage sans clé de 6.2, écart à R9, en
    attente du mot de Lazar. Contre-lecture du code de la version 5, M-2 : **une ligne qui refuse l'écart, mais nomme R9
    et les identifiants, ouvrait la porte**, et le registre était donné par l'appelant. Ici : le registre est celui du
    dépôt, et la ligne porte, à la lettre, la phrase d'accord, sans mot de refus. Cas sain (le jour où Lazar
    l'accorde) : réglage en toutes lettres, GO dont la ligne porte la phrase."""
    table, bras = 987654321987654321, ENTROPIE
    bon = "GO-2026-11-20-01"
    porte = lambda **c: g.admettre_l_entropie_propre_de_la_table_des_identifiants(  # noqa: E731
        **{**dict(entropie_de_la_table=table, entropie_du_bras=bras, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=bon), **c})
    ligne = porte()                                                                                      # cas sain
    assert ligne["entropie"] == table and ligne["cle_de_6_2"] is None and "R9" in ligne["ecart"]
    assert ligne["go"] == bon and "graine" not in ligne
    with pytest.raises(TypeError):                                                                       # aucun réglage par défaut
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras)
    with pytest.raises(TypeError):                                                                       # le registre n'est plus un argument
        porte(registre_des_go=registre)
    for reglage in (None, True, "", "accorde", "ECART-A-R9-ACCORDE-PAR-LAZAR", g.ECART_A_R9_REFUSE):
        with pytest.raises(GardeArret, match="R9"):
            porte(reglage=reglage)
    for go in (None, "", "go de Lazar", "GO-2026-11-20", "R-3857", bon + " et autres"):
        with pytest.raises(GardeArret, match="GO"):
            porte(go_de_lazar=go)
    with pytest.raises(GardeArret, match="phrase"):                                                      # l'attaque : la ligne qui refuse
        porte(go_de_lazar="GO-2026-11-20-02")
    with pytest.raises(GardeArret, match="refus"):                                                       # un refus qui recopie la phrase
        porte(go_de_lazar="GO-2026-11-20-03")
    for go in ("GO-2026-11-20-04", "GO-2026-11-20-06", "GO-2026-11-20-07"):                              # autre affaire, forme approchante
        with pytest.raises(GardeArret, match="phrase"):
            porte(go_de_lazar=go)
    for go in ("GO-1999-01-01-00", "GO-2026-11-20-09", "GO-2026-11-20-05"):                              # absent, hors de la table, en double
        with pytest.raises(GardeArret, match="ligne"):
            porte(go_de_lazar=go)
    with pytest.raises(GardeArret, match="entropie du bras"):
        porte(entropie_de_la_table=bras)
    for fautive in (None, True, -1, 1.5, "12"):
        with pytest.raises(GardeArret):
            porte(entropie_de_la_table=fautive)
    # limite écrite de la seconde garde : une entropie de table dérivée de celle du bras par une clé n'est pas vue ici
    assert porte(entropie_de_la_table=g.entier_de(g.cle("ouve"), bras))["entropie"] != bras
    # ligne d'accord d'une livraison refaite : la même lecture, une autre phrase
    assert "GO-2026-11-20-07" in g.ligne_d_accord("GO-2026-11-20-07", g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE)
    for go, phrase in ((bon, g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE), ("GO-2026-11-20-07", g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9),
                       ("GO-2026-11-20-07", "livraison refaite")):
        with pytest.raises(GardeArret):
            g.ligne_d_accord(go, phrase)
    # le registre est celui du dépôt : `registres/go.md`, à la racine ; absent, rien ne s'ouvre
    monkeypatch.undo()
    assert g.REGISTRE_DES_ACCORDS == Path(g.__file__).resolve().parents[3] / "registres" / "go.md"
    monkeypatch.setattr(g, "REGISTRE_DES_ACCORDS", tmp_path / "absent.md")
    with pytest.raises(GardeArret, match="registre"):
        porte()
    # l'exception ne desserre pas la garde « tirage sans clé » : aucune clé de la table n'existe pour cet usage
    for c in ("bras-a-v2/opaq/moniteurs", "bras-a-v2/table-des-identifiants", "bras-a-v2/opaq/table"):
        with pytest.raises(GardeArret):
            g.tirage_de(c, ENTROPIE)
