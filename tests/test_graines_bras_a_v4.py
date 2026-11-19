"""Essais des graines du bras A, version 4 du code (brouillon 17, 6.2 ; R9) : table fermée des clés (cas sains et
artefacts de la garde « tirage sans clé de 6.2 »), identifiant de tâche avec « / », préfixe de la révision, partage des
tirages entre le côté habilité (quarante et une clés reconnues, non tirées ; clés `lec6` reconnues, non tirées) et
l'instance d'analyse (vingt clés de l'aire conditionnelle), dérivation ; clé `opaq/moniteurs` inexistante ; entropie
propre de la table des identifiants opaques (écart à R9) refusée par défaut."""
import hashlib

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import cle_de_tache
from controle_ia.organismes_discrets import graines_bras_a_v4 as g

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


def test_entropie_propre_de_la_table_des_identifiants_refusee_par_defaut():
    """6.2 (ligne 537) et 8.4 : l'entropie propre de la table des identifiants opaques est un tirage sans clé de 6.2,
    écart déclaré à R9, en attente du mot de Lazar. Artefacts : sans réglage, avec un réglage approchant, avec le
    réglage mais sans ligne de GO, avec une table tirée de l'entropie du bras : refusés. Cas sain (le jour où Lazar
    l'accorde) : réglage écrit en toutes lettres et ligne de GO — la ligne du manifeste est rendue, sans clé ni graine
    dérivée, et rien n'est tiré."""
    table, bras = 987654321987654321, ENTROPIE
    with pytest.raises(GardeArret, match="R9"):
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras)                       # défaut : refusé
    for reglage in (None, True, "", "accorde", "ECART-A-R9-ACCORDE-PAR-LAZAR", g.ECART_A_R9_REFUSE):
        with pytest.raises(GardeArret, match="R9"):
            g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras, reglage, "GO-2026-11-20-01")
    for go in (None, "", "go de Lazar", "GO-2026-11-20", "R-3857", "GO-2026-11-20-01 et autres"):
        with pytest.raises(GardeArret, match="ligne de GO"):
            g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras, g.ECART_A_R9_ACCORDE, go)
    with pytest.raises(GardeArret, match="entropie du bras"):
        g.admettre_l_entropie_propre_de_la_table_des_identifiants(bras, bras, g.ECART_A_R9_ACCORDE, "GO-2026-11-20-01")
    for fautive in (None, True, -1, 1.5, "12"):
        with pytest.raises(GardeArret):
            g.admettre_l_entropie_propre_de_la_table_des_identifiants(fautive, bras, g.ECART_A_R9_ACCORDE, "GO-2026-11-20-01")
    ligne = g.admettre_l_entropie_propre_de_la_table_des_identifiants(table, bras, g.ECART_A_R9_ACCORDE, "GO-2026-11-20-01")
    assert ligne["entropie"] == table and ligne["cle_de_6_2"] is None and "R9" in ligne["ecart"]
    assert ligne["go"] == "GO-2026-11-20-01" and "graine" not in ligne
    # l'exception ne desserre pas la garde « tirage sans clé » : aucune clé de la table n'existe pour cet usage
    for c in ("bras-a-v2/opaq/moniteurs", "bras-a-v2/table-des-identifiants", "bras-a-v2/opaq/table"):
        with pytest.raises(GardeArret):
            g.generateur_de(c, ENTROPIE)
