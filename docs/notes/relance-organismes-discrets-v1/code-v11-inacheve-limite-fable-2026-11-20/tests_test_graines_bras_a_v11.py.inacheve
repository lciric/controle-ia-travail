"""Essais des graines du bras A, version 11 du code (brouillon 34, 6.2 ; 6.9 ; 13.2 ; R9). **Version 11** (vérification
du code de la version 10, M-1 ; vérification du brouillon 34, M-2) : les phrases d'accord sont en cellule d'objet
exacte, sans le gras de Markdown, la casse ni les accents ; une ligne de type « révocation » ne vaut jamais accord ;
la porte de l'écart à R9 regarde le registre courant avant le tirage de la table. **Version 10** (vérification du
code de la version 9, M-2 ; mot de Lazar du 19 novembre 2026) : les préfixes d'empreinte et les identifiants sans tiret
sont reconnus ; la phrase d'accord de l'écart à R9 est confrontée à la lecture consignée du mot. **Version 9** : une ligne qui retire
se reconnaît à son sens, non à l'orthographe de son type ; la ligne d'inscription d'une configuration a une forme, en
deux constantes nommées (dernier essai). Les essais de la table des clés sont
ceux des versions 4 et 5, repris sur le module de la version 8. Changent, d'après la vérification du code de la
version 7 (C-1) et les brouillons 26 à 28 : **le registre des accords n'est plus lu dans le dépôt** — il est remis
comme une pièce, dans son état figé au scellement de la configuration, et reconnu à sa seule empreinte
(`lire_le_registre_fige`) ; la porte de l'écart à R9 et la ligne d'accord d'une livraison refaite le lisent là.
Registre fabriqué dans l'essai."""
import hashlib
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import cle_de_tache
from controle_ia.organismes_discrets import graines_bras_a_v11 as g

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


def test_le_module_de_la_version_10_reprend_la_table_de_la_version_4():
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
    from controle_ia.organismes_discrets import analyse_bras_a_v11 as an
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
    "bon": "| GO-2026-11-20-01 | 2026-11-20 | décision | Écart à R9 accordé pour la table des identifiants opaques | Lazar |",
    "refus": "| GO-2026-11-20-02 | 2026-11-20 | décision | Lazar refuse l'écart à R9 pour la table des identifiants | — |",
    "refus_avec_la_phrase": "| GO-2026-11-20-03 | 2026-11-20 | décision | refus : écart à R9 accordé pour la table des identifiants opaques ? non | Lazar |",
    "autre": "| GO-2026-11-20-04 | 2026-11-20 | calcul | devis de la course des cartes | Lazar |",
    "double_1": "| GO-2026-11-20-05 | 2026-11-20 | décision | écart à R9 accordé pour la table des identifiants opaques | Lazar |",
    "double_2": "| GO-2026-11-20-05 | 2026-11-20 | décision | écart à R9 accordé pour la table des identifiants opaques, bis | Lazar |",
    "approchant": "| GO-2026-11-20-06 | 2026-11-20 | décision | écart à R9, table des identifiants : accordé | Lazar |",
    "livraison": "| GO-2026-11-20-07 | 2026-11-20 | décision | Livraison refaite du côté habilité accordée pour le bras A | Lazar |",
    # vérification du code de la version 6, M-3 : une ligne d'accord vraie, qui nomme « la livraison refusée »
    "apres_un_refus": ("| GO-2026-11-20-08 | 2026-11-20 | décision | Livraison refaite du côté habilité accordée pour le bras A | après la "
                       "livraison refusée du 20 novembre (refus de forme, rejet de la borne) | Lazar |"),
    "revoquee": "| GO-2026-11-20-10 | 2026-11-20 | décision | Livraison refaite du côté habilité accordée pour le bras A | Lazar |",
    "revocation": "| GO-2026-11-20-11 | 2026-11-21 | révocation | révoque GO-2026-11-20-10 | Lazar |",
    "n_accorde_pas": "| GO-2026-11-20-12 | 2026-11-20 | décision | Lazar n'accorde pas : « livraison refaite du côté habilité accordée pour le bras A » | — |",
    "revocation_d_un_autre": "| GO-2026-11-20-13 | 2026-11-21 | révocation | révoque GO-2026-11-20-070 et GO-2026-11-20-080 | Lazar |",
    "refusee": "| GO-2026-11-20-14 | 2026-11-20 | décision | Refusée : livraison refaite du côté habilité accordée pour le bras A | — |",
    "revocation_qui_porte_la_phrase": "| GO-2026-11-20-15 | 2026-11-21 | révocation | livraison refaite du côté habilité accordée pour le bras A | Lazar |",
    # la cellule d'objet est la phrase, et une autre cellule refuse : une forme de refus, où qu'elle soit dans la ligne
    "refus_dans_une_autre_cellule": "| GO-2026-11-20-16 | 2026-11-20 | décision | livraison refaite du côté habilité accordée pour le bras A | refusé : pas de devis | — |",
}


@pytest.fixture
def registre(tmp_path):
    """La pièce qui porte le registre des accords dans son état figé (fabriquée pour l'essai)."""
    f = tmp_path / "registre-fige.md"
    f.write_text("# Registre des accords (fabriqué pour l'essai)\n\n| identifiant | date | type | objet | par |\n|---|---|---|---|---|\n"
                 + "".join(l + "\n" for l in LIGNES_DU_REGISTRE.values())
                 + "Dans le texte : GO-2026-11-20-09 est cité ici, écart à R9 accordé pour la table des identifiants opaques, hors de la table.\n",
                 encoding="utf-8")
    return f


def test_entropie_propre_de_la_table_des_identifiants_refusee_par_defaut(registre, tmp_path):
    """6.2 et 8.4 : l'entropie propre de la table des identifiants opaques est un tirage sans clé de 6.2, écart à R9, en
    attente du mot de Lazar. Contre-lecture du code de la version 5, M-2 : **une ligne qui refuse l'écart, mais nomme R9
    et les identifiants, ouvrait la porte**. Vérification du code de la version 7, C-1 : le registre du dépôt, lu à une
    empreinte attendue, ne pouvait pas être celui de la branche principale au moment de la lecture. Ici : **le registre
    est remis comme une pièce, dans son état figé au scellement de la configuration, reconnu à sa seule empreinte**, et
    la ligne porte, à la lettre, la phrase d'accord, sans forme de refus ni révocation. Cas sain (le jour où Lazar
    l'accorde) : réglage en toutes lettres, GO dont la ligne porte la phrase."""
    table, bras = 987654321987654321, ENTROPIE
    bon = "GO-2026-11-20-01"
    attendu = hashlib.sha256(registre.read_bytes()).hexdigest()
    porte = lambda **c: g.admettre_l_entropie_propre_de_la_table_des_identifiants(  # noqa: E731
        **{**dict(entropie_de_la_table=table, entropie_du_bras=bras, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=bon,
                  registre_fige=registre, sha256_au_scellement=attendu, registre_courant=registre), **c})
    with pytest.raises(TypeError):                                                                       # le registre courant : exigé (version 11)
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=bon,
                                                                  registre_fige=registre, sha256_au_scellement=attendu)
    with pytest.raises(TypeError):                                                                       # la pièce et son empreinte : exigées
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=bon)
    with pytest.raises(TypeError):
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=bon, registre_fige=registre)
    for fautive in (None, "", "abc", attendu.upper(), "0" * 64):
        with pytest.raises(GardeArret, match="registre"):
            porte(sha256_au_scellement=fautive)
    for fautive in (None, "", tmp_path / "absent.md", tmp_path, registre.read_text(encoding="utf-8"), 3):   # la pièce : le chemin d'un fichier
        with pytest.raises(GardeArret, match="registre"):
            porte(registre_fige=fautive)
    ligne = porte()                                                                                      # cas sain
    assert ligne["entropie"] == table and ligne["cle_de_6_2"] is None and "R9" in ligne["ecart"]
    assert ligne["go"] == bon and "graine" not in ligne
    with pytest.raises(TypeError):                                                                       # aucun réglage par défaut
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras)
    for ancien in (dict(registre_des_go=registre), dict(sha256_attendu_du_registre=attendu)):            # les arguments des versions 6 et 7
        with pytest.raises(TypeError):
            porte(**ancien)
    for reglage in (None, True, "", "accorde", "ECART-A-R9-ACCORDE-PAR-LAZAR", g.ECART_A_R9_REFUSE):
        with pytest.raises(GardeArret, match="R9"):
            porte(reglage=reglage)
    for go in (None, "", "go de Lazar", "GO-2026-11-20", "R-3857", bon + " et autres"):
        with pytest.raises(GardeArret, match="GO"):
            porte(go_de_lazar=go)
    with pytest.raises(GardeArret, match="phrase"):                                                      # l'attaque : la ligne qui refuse
        porte(go_de_lazar="GO-2026-11-20-02")
    with pytest.raises(GardeArret, match="n'est pas exactement la phrase"):                              # un refus qui recopie la phrase
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
    accord = lambda go, phrase=g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE: g.ligne_d_accord(  # noqa: E731
        go, phrase, registre_fige=registre, sha256_au_scellement=attendu)
    assert "GO-2026-11-20-07" in accord("GO-2026-11-20-07")
    for go, phrase in ((bon, g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE), ("GO-2026-11-20-07", g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9),
                       ("GO-2026-11-20-07", "livraison refaite")):
        with pytest.raises(GardeArret):
            accord(go, phrase)
    with pytest.raises(TypeError):
        g.ligne_d_accord("GO-2026-11-20-07", g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE)
    # M-3 : des formes de refus entières, non des fragments — une ligne d'accord vraie peut nommer « la livraison refusée »
    assert "livraison refusée du 20 novembre" in accord("GO-2026-11-20-08")
    assert not hasattr(g, "MOTS_DE_REFUS") and "refus" not in g.FORMES_DE_REFUS and all(len(x) > 6 for x in g.FORMES_DE_REFUS)
    for go in ("GO-2026-11-20-12", "GO-2026-11-20-14"):                                                  # « n'accorde pas », « Refusée : » : la phrase n'est pas seule
        with pytest.raises(GardeArret, match="n'est pas exactement la phrase"):
            accord(go)
    with pytest.raises(GardeArret, match="forme de refus"):                                              # la phrase seule, et un refus dans une autre cellule
        accord("GO-2026-11-20-16")
    # une ligne entrée après lui nomme le GO : il n'accorde plus rien, quel que soit le type de cette ligne
    with pytest.raises(GardeArret, match="quel que soit son type"):
        accord("GO-2026-11-20-10")
    assert "GO-2026-11-20-07" in accord("GO-2026-11-20-07") and "GO-2026-11-20-08" in accord("GO-2026-11-20-08")   # -070 et -080 ne sont pas -07 ni -08
    with pytest.raises(GardeArret, match="révocation"):                                                  # une révocation n'est pas un accord,
        accord("GO-2026-11-20-15")                                                                       # même si sa cellule d'objet est la phrase
    # les empreintes que cite une ligne : entières, dans l'ordre, sans doublon
    e1, e2 = "a" * 64, "0123456789abcdef" * 4
    assert g.empreintes_citees(f"| GO | arrêt {e1} ; module {e2} ; encore {e1} ; abrégée 4a6e1b41… ; trop longue {'f' * 65} |") == [e1, e2]
    # le registre du dépôt n'est plus lu : ce module ne nomme aucun fichier de registre
    assert not hasattr(g, "REGISTRE_DES_ACCORDS") and not hasattr(g, "lire_le_registre_des_accords")
    code = Path(g.__file__).read_text(encoding="utf-8").split('"""', 2)[2]
    assert '"registres"' not in code and "go.md" not in code
    # l'exception ne desserre pas la garde « tirage sans clé » : aucune clé de la table n'existe pour cet usage
    for c in ("bras-a-v2/opaq/moniteurs", "bras-a-v2/table-des-identifiants", "bras-a-v2/opaq/table"):
        with pytest.raises(GardeArret):
            g.tirage_de(c, ENTROPIE)


def test_le_registre_se_lit_dans_son_etat_fige_reconnu_a_sa_seule_empreinte(registre, tmp_path):
    """Vérification du code de la version 7, C-1 ; brouillon 26, conventions. La ligne de GO se lit dans le registre
    **tel qu'il était au scellement de la configuration** : la pièce remise n'est lue que si elle porte l'empreinte que
    la configuration inscrit ; sinon l'arrêt dit l'empreinte de la pièce et l'empreinte attendue. Cas sain : la pièce
    de l'état figé, où qu'elle soit rangée et quel que soit son nom. Artefacts : un registre qui a reçu une ligne
    depuis (l'état courant, remis à la place de l'état figé) ; un registre qui en a perdu une ; aucune empreinte."""
    attendu = hashlib.sha256(registre.read_bytes()).hexdigest()
    go, phrase = "GO-2026-11-20-07", g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE
    accord = lambda piece, sha=attendu: g.ligne_d_accord(go, phrase, registre_fige=piece, sha256_au_scellement=sha)  # noqa: E731
    assert len(g.lire_le_registre_fige(registre, attendu)) > 8 and go in accord(registre)
    copie = tmp_path / "ailleurs" / "un-autre-nom.txt"                                    # reconnue à sa seule empreinte
    copie.parent.mkdir()
    copie.write_bytes(registre.read_bytes())
    assert accord(copie) == accord(registre) and accord(str(copie)) == accord(registre)
    texte = registre.read_text(encoding="utf-8")
    en_avance = texte + "| GO-2026-11-22-01 | 2026-11-22 | révocation | révoque GO-2026-11-20-07 | Lazar |\n"       # une révocation de plus
    en_retard = "\n".join(l for l in texte.splitlines() if "GO-2026-11-20-11" not in l) + "\n"                     # une révocation de moins
    for i, autre in enumerate((en_avance, en_retard)):
        piece = tmp_path / f"autre-etat-{i}.md"
        piece.write_text(autre, encoding="utf-8")
        lue = hashlib.sha256(piece.read_bytes()).hexdigest()
        with pytest.raises(GardeArret) as e:
            accord(piece)
        assert lue[:16] in str(e.value) and attendu[:16] in str(e.value) and "état figé" in str(e.value)
    # ce que la garde évite : sur un registre en retard, lu pour lui-même, un GO révoqué depuis accorderait encore
    assert "GO-2026-11-20-10" in g.ligne_d_accord("GO-2026-11-20-10", phrase, registre_fige=piece, sha256_au_scellement=lue)
    # une révocation entrée après l'état figé n'est pas vue ici : c'est le constat de lancement qui la voit
    # (`scripts/constat_de_lancement_discretion_bras_a_v1.py`, essais de l'analyse)
    assert go in accord(registre)
    for sans in (None, "", "celui de la branche principale", 3):
        with pytest.raises(GardeArret, match="empreinte"):
            g.lire_le_registre_fige(registre, sans)
    with pytest.raises(TypeError):                                                                       # aucune valeur par défaut
        g.lire_le_registre_fige(registre)
    illisible = tmp_path / "illisible.md"
    illisible.write_bytes(b"\xff\xfe registre")
    with pytest.raises(GardeArret, match="illisible"):
        g.lire_le_registre_fige(illisible, hashlib.sha256(illisible.read_bytes()).hexdigest())



def test_une_ligne_qui_retire_se_reconnait_a_son_sens_et_la_ligne_d_inscription_a_sa_forme(tmp_path):
    """Brouillon 30, conventions, « Reconnaître par le sens, non par le type » ; vérification du code de la version 8,
    C-1 et M-2. **Dans l'état figé**, une ligne de GO que nomme une ligne placée après elle n'ouvre rien, quel que
    soit le type de cette ligne : « révocation », « revocation » sans accent, « décision » qui dit l'accord révoqué,
    simple mention, texte hors de la table. Cas sains : une ligne placée avant elle ; un identifiant voisin (un
    chiffre de plus) — l'identifiant se compare en entier. **Ligne neuve à voir** (`ligne_neuve_a_voir`) : elle nomme
    la ligne de GO employée, ou cite l'empreinte de la configuration sans être sa ligne d'inscription. **Ligne
    d'inscription** : type « inscription », la marque, puis l'empreinte entière — deux constantes nommées, que la
    session principale peut changer."""
    phrase = g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE
    go = lambda n: f"GO-2099-01-01-{n:02d}"  # noqa: E731
    accorde = lambda n: f"| {go(n)} | 2099-01-01 | décision | {phrase} | Lazar |"  # noqa: E731
    lignes = [f"| GO-2098-12-31-01 | 2098-12-31 | calcul | annonce de {go(1)}, à venir | Lazar |",           # placée avant elle : ne compte pas
              *[accorde(n) for n in range(1, 8)],
              f"| GO-2099-01-02-01 | 2099-01-02 | révocation | révoque {go(1)}1 | Lazar |",                    # un identifiant voisin : n'arrête rien
              f"| GO-2099-01-02-02 | 2099-01-02 | révocation | révoque {go(2)} | Lazar |",
              f"| GO-2099-01-02-03 | 2099-01-02 | revocation | revoque {go(3)} | Lazar |",                     # sans accent
              f"| GO-2099-01-02-04 | 2099-01-02 | décision | {go(4)} est révoqué | Lazar |",                    # un autre type
              f"| GO-2099-01-02-05 | 2099-01-02 | calcul | devis ; voir {go(5).lower()} | Lazar |",             # simple mention
              f"Note hors de la table : {go(6)} ne vaut plus.",
              f"| GO-2099-01-02-07 | 2099-01-02 | inscription | {g.MARQUE_DE_LA_LIGNE_D_INSCRIPTION} {'a' * 64} ; sous {go(7)} | Lazar |"]   # même une inscription
    piece = tmp_path / "etat-fige.md"
    piece.write_text("# Registre\n\n| identifiant | date | type | objet | par |\n|---|---|---|---|---|\n" + "".join(l + "\n" for l in lignes), encoding="utf-8")
    sha = hashlib.sha256(piece.read_bytes()).hexdigest()
    accord = lambda n: g.ligne_d_accord(go(n), phrase, registre_fige=piece, sha256_au_scellement=sha)  # noqa: E731
    assert go(1) in accord(1)                                                              # cas sain
    for n in range(2, 8):
        with pytest.raises(GardeArret, match="quel que soit son type") as e:
            accord(n)
        assert go(n) in str(e.value)
    # l'identifiant se compare en entier, sans égard à la casse
    assert g.nomme_l_identifiant(f"révoque {go(1)}.", go(1)) and g.nomme_l_identifiant(f"({go(1).lower()})", go(1))
    for voisin in (f"{go(1)}1", f"{go(1)}0", f"X{go(1)}", f"1{go(1)}", go(1)[:-1], "GO-2099-01-01"):
        assert not g.nomme_l_identifiant(f"révoque {voisin}", go(1)), voisin
    assert g.sans_accent("Révocation") == g.sans_accent("revocation") == "revocation"
    # la ligne d'inscription : deux constantes, en un seul endroit
    assert g.TYPE_DE_LA_LIGNE_D_INSCRIPTION == "inscription" and g.MARQUE_DE_LA_LIGNE_D_INSCRIPTION == "CONFIG-ANALYSE-DISCRETION-BRAS-A"
    code = Path(g.__file__).read_text(encoding="utf-8")
    assert code.count('"CONFIG-ANALYSE-DISCRETION-BRAS-A"') == 1 and code.count('TYPE_DE_LA_LIGNE_D_INSCRIPTION = "inscription"') == 1
    e64, marque = "e" * 64, g.MARQUE_DE_LA_LIGNE_D_INSCRIPTION
    inscription = f"| GO-2099-02-01-01 | 2099-02-01 | inscription | {marque} {e64} | Lazar |"
    assert g.est_la_ligne_d_inscription(inscription, e64)
    for sain in (f"| G | d | Inscription | {marque} : {e64} |", f"| G | d | inscription | `{marque}` — `{e64}` | Lazar |"):
        assert g.est_la_ligne_d_inscription(sain, e64), sain
    for fautive in (f"| G | d | décision | {marque} {e64} |", f"| G | d | inscription | {e64} |", f"| G | d | inscription | {e64} {marque} |",
                    f"| G | d | inscription | {marque} {e64}ab |", f"| G | d | inscription | {marque.lower()} {e64} |",
                    f"| G | d | inscription | {marque} de {e64} |", f"| G | d | inscription | {marque} {e64[:16]} |",
                    f"| G | d | inscription | {marque} {'f' * 64} |", f"{marque} {e64}", f"| G | inscription | {marque} {e64} |"):
        assert not g.est_la_ligne_d_inscription(fautive, e64), fautive
    # ligne neuve à voir : par le sens
    voir = lambda ligne, ligne_de_go=go(1): g.ligne_neuve_a_voir(ligne, ligne_de_go=ligne_de_go, sha256_de_la_configuration=e64)  # noqa: E731
    assert voir(inscription) is None and voir("| G | d | calcul | un devis | Lazar |") is None and voir(f"révoque {go(1)}1") is None
    for ligne in (f"| G | d | révocation | révoque {go(1)} |", f"| G | d | revocation | revoque {go(1)} |", f"| G | d | décision | {go(1)} est révoqué |",
                  f"voir {go(1)}", inscription[:-2] + f" ; sous {go(1)} |"):
        assert voir(ligne) == g.MOTIF_LIGNE_NEUVE_QUI_NOMME_LA_LIGNE_DE_GO
        assert voir(ligne, None) in (None, g.MOTIF_LIGNE_NEUVE_QUI_CITE_LA_CONFIGURATION)   # une première livraison n'emploie aucune ligne
    for ligne in (f"| G | d | révocation | retire {marque} {e64} |", f"| G | d | décision | {e64.upper()} |", f"{marque} {e64}"):
        assert voir(ligne) == voir(ligne, None) == g.MOTIF_LIGNE_NEUVE_QUI_CITE_LA_CONFIGURATION
    with pytest.raises(TypeError):                                                         # deux arguments nommés, sans valeur par défaut
        g.ligne_neuve_a_voir(inscription)


def test_prefixes_d_empreinte_et_identifiants_sans_tiret_reconnus(tmp_path):
    """Vérification du code de la version 9, M-2 : une ligne qui retirait la configuration en n'en citant que
    l'empreinte abrégée n'était pas vue, ni un identifiant de GO écrit sans ses tirets (« GO 2099-01-01-01 »). Cas
    sains : l'empreinte entière, l'identifiant écrit en entier. Artefacts : un préfixe de **seize signes au moins**
    (brouillon 32, conventions) ; l'identifiant sans tiret, avec des blancs, des points, des tirets bas. Ce qui n'est
    pas pris : quinze signes, et donc les abrégés de huit ou douze signes d'usage — **limite écrite** : la consigne de
    tenue du registre demande l'empreinte entière — ; le début d'une autre empreinte ; un identifiant voisin, ou suivi
    d'une lettre."""
    e = "0123456789abcdef" * 4
    assert g.LONGUEUR_MINIMALE_D_UN_PREFIXE_D_EMPREINTE == 16
    for cite in (e, e.upper(), f"retire {e[:16]}…", f"retire `{e[:16]}`", f"retire {e[:20].upper()}", f"x{e}y", e[:40], f"({e[:17]})", e[:63]):
        assert g.cite_l_empreinte(cite, e), cite
    for ne_cite_pas in (e[:15], f"retire {e[:15]}…", f"retire {e[:8]}…", f"retire {e[:12].upper()}", "1123456789abcdef", e[1:17], e[8:40], "",
                        "retire la configuration", e[:16][::-1]):
        assert not g.cite_l_empreinte(ne_cite_pas, e), ne_cite_pas
    go = "GO-2099-01-01-01"
    for nomme in (go, go.lower(), "GO 2099-01-01-01", "go 2099 01 01 01", "GO2099-01-01-01", "GO_2099_01_01_01", "GO.2099.01.01.01",
                  "GO–2099–01–01–01", "GO-2099/01/01-01", f"révoque ({go})", "GO2099010101"):
        assert g.nomme_l_identifiant(f"| X | d | décision | {nomme} est retirée | Lazar |", go), nomme
    for ne_nomme_pas in (go + "1", "GO-2099-01-01-011", "GO 2099-01-01-011", "GO-2099-01-01", "GO-2099-01-01-02", "XGO-2099-01-01-01",
                         "GO-2099-01-01-1", "GO-12099-01-01-01", "2099-01-01-01", go + "b", "GO-2099-01-01-01bis", "GO2099010101x"):
        assert not g.nomme_l_identifiant(f"| X | d | décision | {ne_nomme_pas} est retirée | Lazar |", go), ne_nomme_pas
    with pytest.raises(GardeArret):
        g.nomme_l_identifiant("texte", "")
    # la ligne d'inscription porte toujours l'empreinte entière : abrégée, elle cite la configuration sans l'inscrire
    marque = g.MARQUE_DE_LA_LIGNE_D_INSCRIPTION
    abregee = f"| G | d | inscription | {marque} {e[:16]} |"
    assert not g.est_la_ligne_d_inscription(abregee, e) and g.cite_l_empreinte(abregee, e)
    assert g.ligne_neuve_a_voir(abregee, ligne_de_go=None, sha256_de_la_configuration=e) == g.MOTIF_LIGNE_NEUVE_QUI_CITE_LA_CONFIGURATION
    assert g.ligne_neuve_a_voir(f"| G | d | révocation | révoque GO 2099-01-01-01 |", ligne_de_go=go, sha256_de_la_configuration=e) \
        == g.MOTIF_LIGNE_NEUVE_QUI_NOMME_LA_LIGNE_DE_GO
    # dans l'état figé aussi : une ligne placée après la ligne de GO qui la nomme sans tiret
    phrase = g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE
    lignes = [f"| {go} | 2099-01-01 | décision | {phrase} | Lazar |", f"| GO-2099-01-01-02 | 2099-01-01 | décision | {phrase} | Lazar |",
              "| GO-2099-01-02-01 | 2099-01-02 | révocation | révoque GO 2099-01-01-01 | Lazar |"]
    piece = tmp_path / "etat-fige.md"
    piece.write_text("# Registre\n\n| identifiant | date | type | objet | par |\n|---|---|---|---|---|\n" + "".join(l + "\n" for l in lignes), encoding="utf-8")
    sha = hashlib.sha256(piece.read_bytes()).hexdigest()
    with pytest.raises(GardeArret, match="quel que soit son type"):
        g.ligne_d_accord(go, phrase, registre_fige=piece, sha256_au_scellement=sha)
    assert "GO-2099-01-01-02" in g.ligne_d_accord("GO-2099-01-01-02", phrase, registre_fige=piece, sha256_au_scellement=sha)


def test_la_porte_de_l_ecart_a_r9_et_la_lecture_consignee_du_mot_de_lazar(tmp_path):
    """Mot de Lazar « go recos » du 19 novembre 2026 : « écart à R9 : entropie propre de la table des identifiants
    opaques — accepter ». La porte s'ouvre sur une ligne de GO que la session principale inscrira au registre. **Le
    code ne change pas** : il exige, à la lettre, sa phrase d'accord. **Elle diffère des mots de la lecture
    consignée** : une ligne qui recopierait ces mots n'ouvrirait pas la porte ; la ligne à inscrire doit porter la
    phrase du code (note du code de la version 10, partie 3)."""
    assert g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9 == "écart à R9 accordé pour la table des identifiants opaques"
    lecture_consignee = "écart à R9 : entropie propre de la table des identifiants opaques — accepter"
    assert g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9.casefold() not in lecture_consignee.casefold()
    go_mots_du_mot, go_phrase_du_code = "GO-2099-11-19-01", "GO-2099-11-19-02"
    lignes = [f"| {go_mots_du_mot} | 2099-11-19 | décision | {lecture_consignee} | Lazar |",
              f"| {go_phrase_du_code} | 2099-11-19 | décision | {g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9} | mot de Lazar « go recos » | Lazar |"]
    piece = tmp_path / "etat-fige.md"
    piece.write_text("# Registre\n\n| identifiant | date | type | objet | par |\n|---|---|---|---|---|\n" + "".join(l + "\n" for l in lignes), encoding="utf-8")
    sha = hashlib.sha256(piece.read_bytes()).hexdigest()
    porte = lambda go: g.admettre_l_entropie_propre_de_la_table_des_identifiants(  # noqa: E731
        987654321987654321, ENTROPIE, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=go, registre_fige=piece, sha256_au_scellement=sha,
        registre_courant=piece)
    with pytest.raises(GardeArret, match="phrase"):                                        # les mots du mot de Lazar, recopiés : la porte reste fermée
        porte(go_mots_du_mot)
    ligne = porte(go_phrase_du_code)                                                       # la phrase du code : la porte s'ouvre
    assert ligne["go"] == go_phrase_du_code and ligne["cle_de_6_2"] is None and "R9" in ligne["ecart"]
    with pytest.raises(GardeArret, match="R9"):                                            # sans le réglage en toutes lettres, elle reste fermée
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(987654321987654321, ENTROPIE, reglage=g.ECART_A_R9_REFUSE,
                                                                  go_de_lazar=go_phrase_du_code, registre_fige=piece, sha256_au_scellement=sha,
                                                                  registre_courant=piece)


def test_phrases_d_accord_en_cellule_d_objet_exacte(tmp_path):
    """Brouillon 34, 13.2 et 8.4, « phrases d'accord des lignes de GO » ; vérification du code de la version 10, M-1, et
    son essai d'attaque (`attaques_v10.py`, « la phrase de l'écart à R9 ») ; vérification du brouillon 34, M-2 (a) et
    (b). **La cellule d'objet de la ligne de GO est exactement la phrase** : sans le gras de Markdown, sans égard à la
    casse ni aux accents, un point final seul admis ; rien avant, rien après. Vaut pour les deux phrases.
    Cas sains : la phrase ; sans accents ; en capitales ; en gras ; avec un point final ; des blancs en trop.
    Artefacts : la phrase précédée de « aucun » ou de « pas d' », suivie de « avant le devis » ou de « ? à trancher »,
    ou simplement contenue dans une cellule plus longue ; dans une autre cellule que celle de l'objet ; une ligne de
    type « révocation » dont la cellule d'objet est la phrase ; les mots du mot de Lazar."""
    assert g.CELLULE_DE_L_OBJET == 3 and g.CELLULE_DU_TYPE == 2 and g.GRAS_DE_MARKDOWN == "**"
    ligne = lambda objet, type_="décision", suite="Lazar": f"| GO-2099-03-01-01 | 2099-03-01 | {type_} | {objet} | {suite} |"  # noqa: E731
    for phrase in (g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9, g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE):
        sans_accents = g.sans_accent(phrase).replace("r9", "R9")
        for ouvre in (phrase, sans_accents, phrase.upper(), f"**{phrase}**", f"**{phrase}.**", phrase + ".", "  " + phrase.replace(" ", "  ") + " ",
                      f"**{phrase[:8]}**{phrase[8:]}"):
            assert g.dit_l_accord(ligne(ouvre), phrase), ouvre
        assert g.dit_l_accord(ligne(phrase, suite=f"fichier d'arrêt {'a' * 64} ; module {'b' * 64} ; rapport {'c' * 64}"), phrase)   # le reste est ailleurs
        for n_ouvre_rien in ("aucun " + phrase, "aucune " + phrase, "pas d'" + phrase, "pas d'" + phrase + " avant le devis", phrase + " avant le devis",
                             phrase + " ? à trancher", phrase + " ?", phrase + " (bras A)", phrase + ", refusé : pas de devis", "refus : " + phrase,
                             phrase + " ; fichier d'arrêt " + "a" * 64, f"`{phrase}`", f"« {phrase} »", phrase[:-1], phrase + "..", "", "accordé"):
            assert not g.dit_l_accord(ligne(n_ouvre_rien), phrase), n_ouvre_rien
        assert not g.dit_l_accord(ligne("voir la cellule suivante", suite=phrase), phrase)             # la phrase, dans une autre cellule
        assert not g.dit_l_accord(f"| GO-2099-03-01-01 | 2099-03-01 | {phrase} |", phrase)            # une ligne sans cellule d'objet
        assert not g.dit_l_accord(f"GO-2099-03-01-01 : {phrase}", phrase)                             # hors de la table
        for revocation in ("révocation", "revocation", "Révocation", "RÉVOCATION", "révocation de GO"):   # jamais un accord, quel que soit son objet
            assert not g.dit_l_accord(ligne(phrase, revocation), phrase), revocation
    assert not g.dit_l_accord(ligne(g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9), g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE)   # une phrase n'est pas l'autre
    assert g.forme_d_une_cellule("  **Écart   à R9**  ") == "ecart a r9"
    # --- la porte de l'écart à R9, sur l'état figé fabriqué de l'essai d'attaque : sept lignes
    P = g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9
    objets = {1: P, 2: "aucun " + P, 3: "pas d'" + P + " avant le devis",
              4: "écart à R9 : entropie propre de la table des identifiants opaques — accepter",       # les mots du mot de Lazar
              5: "ecart a R9 accorde pour la table des identifiants opaques", 6: P + " ? à trancher", 7: P + ", refusé : pas de devis",
              8: f"**{P}**"}
    lignes = [f"| GO-2099-03-01-0{k} | 2099 | décision | {objet} |" for k, objet in objets.items()]
    lignes.append(f"| GO-2099-03-01-09 | 2099 | révocation | {P} |")
    piece = tmp_path / "etat-fige.md"
    piece.write_text("# Registre\n\n| identifiant | date | type | objet |\n|---|---|---|---|\n" + "".join(x + "\n" for x in lignes), encoding="utf-8")
    sha = hashlib.sha256(piece.read_bytes()).hexdigest()
    porte = lambda k: g.admettre_l_entropie_propre_de_la_table_des_identifiants(  # noqa: E731
        1, 2, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=f"GO-2099-03-01-0{k}", registre_fige=piece, sha256_au_scellement=sha, registre_courant=piece)
    for k in (1, 5, 8):                                                                    # la phrase ; sans accents (la version 10 la refusait) ; en gras
        assert porte(k)["go"] == f"GO-2099-03-01-0{k}"
    for k in (2, 3, 4, 6, 7, 9):                                                           # les quatre que la version 10 ouvrait à tort : 2, 3, 6 — et 4, 7, 9
        with pytest.raises(GardeArret, match="n'est pas exactement la phrase") as e:
            porte(k)
        assert objets.get(k, P) not in str(e.value) or k == 9                              # le message ne recopie pas la cellule fautive


def test_la_porte_de_l_ecart_a_r9_regarde_le_registre_courant_avant_le_tirage_de_la_table(tmp_path):
    """Vérification du brouillon 34, M-2 (c) : la porte lit sa ligne dans l'état du registre au commit de son
    inscription ; **une révocation entrée après ce commit, mais avant le tirage de la table, n'était pas vue**. La
    porte reçoit donc aussi le registre courant, et fait le contrôle que fait le constat de lancement pour une
    lecture : aucune ligne entrée depuis l'état figé ne nomme la ligne de GO de l'écart — reconnue par son sens, quel
    que soit le type de la ligne. Cas sains : le registre courant est l'état figé ; il a reçu des lignes qui ne la
    nomment pas, ou qui nomment un identifiant voisin. Artefacts : une révocation, bien ou mal orthographiée ; une
    décision qui dit l'accord retiré ; l'identifiant écrit sans tiret ; un registre courant qui a perdu une ligne de
    l'état figé ; aucun registre courant."""
    go, P = "GO-2099-04-01-01", g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9
    en_tete = "# Registre\n\n| identifiant | date | type | objet | par |\n|---|---|---|---|---|\n"
    figees = [f"| GO-2099-03-31-01 | 2099-03-31 | calcul | un devis | Lazar |", f"| {go} | 2099-04-01 | décision | {P} | Lazar |"]
    fige = tmp_path / "etat-fige.md"
    fige.write_text(en_tete + "".join(x + "\n" for x in figees), encoding="utf-8")
    sha = hashlib.sha256(fige.read_bytes()).hexdigest()

    def porte(lignes_de_plus=(), sans=(), courant=None):
        if courant is None:
            courant = tmp_path / f"courant-{len(list(tmp_path.iterdir()))}.md"
            courant.write_text(en_tete + "".join(x + "\n" for x in [l for l in figees if l not in sans] + list(lignes_de_plus)), encoding="utf-8")
        return g.admettre_l_entropie_propre_de_la_table_des_identifiants(
            987654321, ENTROPIE, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=go, registre_fige=fige, sha256_au_scellement=sha, registre_courant=courant)

    assert porte()["go"] == go and porte(courant=fige)["go"] == go                         # cas sains
    assert porte(["| GO-2099-04-02-01 | 2099-04-02 | calcul | un autre devis | Lazar |",
                  f"| GO-2099-04-02-02 | 2099-04-02 | révocation | révoque {go}1 | Lazar |"])["go"] == go     # un identifiant voisin : n'arrête rien
    for entree in (f"| GO-2099-04-02-03 | 2099-04-02 | révocation | révoque {go} | Lazar |",
                   f"| GO-2099-04-02-03 | 2099-04-02 | revocation | revoque {go} | Lazar |",
                   f"| GO-2099-04-02-03 | 2099-04-02 | décision | {go} est retiré | Lazar |",
                   "| GO-2099-04-02-03 | 2099-04-02 | révocation | révoque GO 2099-04-01-01 | Lazar |",
                   f"Note hors de la table : {go.lower()} ne vaut plus."):
        with pytest.raises(GardeArret, match="le tirage de la table ne part pas") as e:
            porte([entree])
        assert go in str(e.value)
    with pytest.raises(GardeArret, match="ne contient pas une ligne de l'état figé"):       # un registre ne perd pas de ligne
        porte(sans=[figees[0]])
    for absent in (None, tmp_path / "absent.md", tmp_path, 3):
        with pytest.raises(GardeArret, match="registre courant"):
            g.admettre_l_entropie_propre_de_la_table_des_identifiants(
                987654321, ENTROPIE, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=go, registre_fige=fige, sha256_au_scellement=sha, registre_courant=absent)
    illisible = tmp_path / "illisible.md"
    illisible.write_bytes(b"\xff\xfe registre")
    with pytest.raises(GardeArret, match="illisible"):
        porte(courant=illisible)
    # la fonction nommée, seule : les lignes entrées depuis l'état figé
    deux = tmp_path / "deux.md"
    deux.write_text("a\nb\na\nc\n", encoding="utf-8")
    assert g.lignes_entrees_depuis(["a", "b"], deux) == ["a", "c"] and g.lignes_entrees_depuis([], deux) == ["a", "b", "a", "c"]
    with pytest.raises(GardeArret):
        g.lignes_entrees_depuis(["a", "a", "a"], deux)
