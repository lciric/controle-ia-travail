#!/usr/bin/env python3
"""Assemble le texte scellable du préenregistrement v11 (candidat 1) à partir du brouillon 8.

Sur le message de la session de l'organisme du 23 novembre 2026 daté 06:52Z : empreintes des pièces du lanceur v11d (branche
`prep/lanceur-affinage-v11c-interrompu-v1`, commit `708549da5`), vérifiées à leur compagnon par le rédacteur ; « écris le texte
scellable, mais ne le scelle pas avant mon feu » ; limite de l'essai à blanc à écrire.
Ce programme : retire la ligne d'état (l. 3) et la dernière section du brouillon 8 ; inscrit les quatorze empreintes ; nomme
le lanceur de la course v11e, le v11d à deux lignes près (sa version, et `PREREG_SHA256`, vide dans le v11d, posée à
l'empreinte de ce texte), le lanceur relisant sa propre empreinte au départ (R12 : un fichier changé prend un nom neuf ; comme
le lanceur v10, le v9 à l'empreinte de son texte et aux chemins près) — nom proposé à la session de l'organisme, à confirmer
avant son feu ; écrit la limite de l'essai à blanc. Aucun chiffre ne change.
Le texte produit n'est pas scellé : au feu de la session de l'organisme, il est copié à l'octet sous le nom
`course-v11/preenregistrement-course-affinage-mentors-v11.md`, puis scellé (R1, R12). Chaque remplacement exige que l'ancienne
chaîne figure exactement une fois dans la ligne visée ; sinon le programme s'arrête.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré dans le texte).
Usage : python3 -I assembler-preenregistrement-v11-candidat-1.py BROUILLON-8.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B8_SHA = "f4629f234521603f2c87d8a6f055a97817dbcaf461a44daac9320775d1d20163"
N = "docs/notes/organisme-affinage-mentors-v1"
C = "docs/notes/organisme-affinage-mentors-v1/course-v11"
COMMIT_V11D, BRANCHE_LANCEUR = "708549da5", "prep/lanceur-affinage-v11c-interrompu-v1"
LANCEUR_V11D = "8be7786ee30279fc3c0fb1f2f7da06302460afe5eed65379216ea04ef1a9ecf8"
ESSAIS_V11D = "1bff94611e85c2ff337fd38221508d441cbe43afc510324cd17258e779dbec35"
CONF_V11D = "7373818a288b540126c2610fe3715de8a9fad33ae8b0fa9e1d3bb4f47f07b0b1"
GABARIT_CREDITS_V11D = "c4ec18e2ee5b69421f7bf93983db398c3b51a8f923f10267a66c2e3e8976c28c"
RAPPORT_V11D = "16cfecd0ab3c74d867df57c310c7813ee914f2685d7f52b9b8d4b3f8c941993f"
COMMANDE_FLUX_V2 = "13b968eb440279eb77cd9858cefacfb54bc87b11cbf5fc47cf4476044f8e6a50"
ESSAIS_FLUX_V2 = "35e874ef42696243c3847a342b91a674f2fc07817bee9712acb4ee97189c8bed"
SONDE_COMMUNE_V3 = "d02971f0cbe6f15e5be1f58a5050ff86ca48bd9b6a059e478285315fda5c729e"
ESSAIS_SONDE_V3 = "49142a340bcca3638c319eac0e441bebe4f26e8f2c3f9431ebd1da0b43482a86"
GABARIT_DECLARATION_V11C = "1c0f8f9a074bbec4b873b382214d5aac3bad4b9605d26b69d60a83d87118cd0d"
LANCEUR_V11C = "fe7358b93fa00648c2e4612846789895d809d534c9e3ff8ebf10f33654175548"
RAPPORT_V11C = "a56faf45ba40adc6c4e81ad20546a249c3f9909819dc72b4be7526af326da157"
VERIFICATION_V11C = "525dc1587c9a98a786837a075b7295361195bd9182546aa6ad2f72562e37f089"
CMD_D = "`GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11d.py`"
CMD_E = "`GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11e.py`"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B8_SHA, "la source n'est pas le brouillon 8"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 333, len(L)   # 332 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
assert lignes[3].startswith("- **État de ce fichier : brouillon 8 de la v11, non scellé comme préenregistrement.**")
assert lignes[296].startswith("16. **Mesure préalable de la réflexion d'Argon**") and lignes[297] == ""
assert lignes[298].startswith("## Emplacements et points à trancher avant le scellement")
touchees = set()


def sub(n, ancien, nouveau, fois=1):
    assert lignes[n].count(ancien) == fois, (n, ancien[:80], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


# ------------------------------------------------------------------------------------------------ en-tête
sub(4, "Pour le brouillon 8, R-5140 (commit `903f4bfc0`).",
    "Pour le brouillon 8, R-5140 (commit `903f4bfc0`). Pour ce texte, les pièces scellées du lanceur v11d (branche `"
    + BRANCHE_LANCEUR + "`, commit `" + COMMIT_V11D + "`), chacune vérifiée à son compagnon et aux empreintes envoyées par la "
    "session de l'organisme : lanceur, essais, configuration, gabarit du relevé des crédits, rapport du développeur, et la "
    "vérification des corrections du lanceur v11c.")
sub(5, "- Date (UTC) de ce brouillon : 2026-11-23T06:04:13Z (`date -u +%FT%TZ`) ; brouillon 7 :",
    "- Date (UTC) de la v11 : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 8 : 2026-11-23T06:04:13Z ; brouillon 7 :")
sub(5, "**Version 11** (R12) : les v1 à v10 restent en place, scellées, jamais lancées.",
    "**Version 11** (R12) : les v1 à v10 restent en place, scellées, jamais lancées ; les brouillons 1 à 8 de la v11 restent en "
    "place, non scellés comme préenregistrement. Ce texte est le brouillon 8 (`course-v11/preenregistrement-course-affinage-"
    "mentors-v11-brouillon-8.md`, `" + B8_SHA + "`) sans sa ligne d'état ni sa dernière section, ses emplacements remplis des "
    "empreintes des pièces du lanceur v11d et son lanceur nommé (v11e, le v11d à l'épingle de ce texte près ; pièces).")
sub(7, "noms et chemins `v11`, lanceur v11d, configuration fixe v11d,",
    "noms et chemins `v11`, lanceur v11e (le v11d à l'épingle de ce texte près), configuration fixe v11d,")

# ------------------------------------------------------------------------------------------------ pièces
sub(12, "**v11d** : EMPREINTE À INSCRIRE : `" + C + "/configuration-course-affinage-mentors-v11d.json` (la v11c,",
    "**v11d** : `" + C + "/configuration-course-affinage-mentors-v11d.json`, `" + CONF_V11D + "` (scellée au commit `"
    + COMMIT_V11D + "` de la branche `" + BRANCHE_LANCEUR + "` ; la v11c,")
sub(12, "est retiré (R-5132) ; à constater sur la pièce scellée)",
    "est retiré (R-5132), ce que dit une note `note_v11d` ; constaté sur la pièce scellée)")
sub(14, "`scripts/commande_gemini_flux_v2.py` : EMPREINTE À INSCRIRE (scellée avec le lanceur v11c : `" + COMMANDE_FLUX_V2 + "` ;",
    "`scripts/commande_gemini_flux_v2.py`, `" + COMMANDE_FLUX_V2 + "` (scellée avec le lanceur v11c, inchangée en v11d ;")
sub(17, "`scripts/sonde_astra_courses_v3.py`, EMPREINTE À INSCRIRE (scellée avec le lanceur v11c : `" + SONDE_COMMUNE_V3 + "` ;",
    "`scripts/sonde_astra_courses_v3.py`, `" + SONDE_COMMUNE_V3 + "` (scellée avec le lanceur v11c, inchangée en v11d ;")

DEBUT_27 = ("  - lanceur : `scripts/lancer_course_affinage_mentors_v11d.py`, le lanceur v11c (`scripts/lancer_course_affinage_mentors_"
            "v11c.py`, `" + LANCEUR_V11C + "`, scellé au commit `1ed883749` de la branche `" + BRANCHE_LANCEUR + "`, sa "
            "vérification par le même contre-lecteur en cours ; rapport `" + C + "/rapport-developpeur-lanceur-v11c.md`, `"
            + RAPPORT_V11C + "`) à une ligne près, celle de la clé LUC dans les réglages de l'essai à blanc (selon la session de "
            "l'organisme), lui-même écrit à partir du lanceur v11b")
PIVOT_27 = "par un développeur qui n'est pas le rédacteur de ce texte"
FIN_27 = ("(il épingle l'empreinte de ce préenregistrement : ce texte ne peut donc pas porter la sienne, qui est donnée par "
          "`course-v11/commandes-exactes-course-affinage-v11.md` et doit être citée par la contre-lecture ; EMPREINTE À INSCRIRE "
          "ici seulement si le lanceur v11d ne porte plus l'empreinte de ce texte dans son code : `scripts/lancer_course_affinage_"
          "mentors_v11d.py`) ; **commande de lancement** : " + CMD_D + " ; ses essais : EMPREINTE À INSCRIRE : `tests/test_lancer_"
          "course_affinage_mentors_v11d.py` (ceux du v11c : `88a61acd4a55b14addbf94b4583a812a87783cd22bdb21f0c00788100e6e086b`) ; "
          "essais de la commande en flux v2 et de la sonde commune v3 : EMPREINTE À INSCRIRE : `tests/test_commande_gemini_flux_"
          "v2.py` (scellés avec le lanceur v11c : `" + ESSAIS_FLUX_V2 + "`) et EMPREINTE À INSCRIRE : `tests/test_sonde_astra_"
          "courses_v3.py` (scellés avec le lanceur v11c : `" + ESSAIS_SONDE_V3 + "`) ; gabarit de déclaration des relais : "
          "EMPREINTE À INSCRIRE : `" + C + "/declaration-relais-gabarit-course-affinage-v11c.json` (scellé avec le lanceur v11c : `"
          + GABARIT_DECLARATION_V11C + "` ; ou son successeur v11d s'il en est écrit un) ; gabarit du relevé des crédits du jour : "
          "EMPREINTE À INSCRIRE : `" + C + "/releve-credits-gabarit-course-affinage-v11d.json` (écrit avec le lanceur v11d) ; "
          "aucun gabarit du relevé du prix Claude : le lanceur lit le relevé du jour (`course-v11/releve-prix-claude-course-"
          "affinage-v11.json`), jamais un gabarit ;")
t27 = lignes[27]
assert t27.startswith(DEBUT_27) and t27.count(PIVOT_27) == 1, t27[:200]
milieu = t27[len(DEBUT_27):t27.index(PIVOT_27)]
reste = t27[t27.index(PIVOT_27) + len(PIVOT_27):]
assert reste == " " + FIN_27, reste[:200]
lignes[27] = (
    "  - lanceur de la course : `scripts/lancer_course_affinage_mentors_v11e.py`, le lanceur v11d (`scripts/lancer_course_"
    "affinage_mentors_v11d.py`, `" + LANCEUR_V11D + "`, scellé au commit `" + COMMIT_V11D + "` de la branche `" + BRANCHE_LANCEUR
    + "` ; rapport `" + C + "/rapport-developpeur-lanceur-v11d.md`, `" + RAPPORT_V11D + "` ; sa vérification par le même "
    "contre-lecteur que le v11c en cours à l'écriture de ce texte) à deux lignes près : sa version, et l'épingle de ce "
    "préenregistrement (`PREREG_SHA256`, vide dans le v11d, qui refuse alors tout lancement), posée à l'empreinte de ce texte une "
    "fois scellé — le lanceur relit sa propre empreinte au départ et exige que la contre-lecture la cite : un fichier changé prend "
    "un nom neuf (R12), comme le lanceur v10, le v9 à l'empreinte de son texte et aux chemins près. Le v11d est le lanceur v11c "
    "(`scripts/lancer_course_affinage_mentors_v11c.py`, `" + LANCEUR_V11C + "`, scellé au commit `1ed883749` ; rapport `" + C
    + "/rapport-developpeur-lanceur-v11c.md`, `" + RAPPORT_V11C + "` ; vérifié par le même contre-lecteur, « Scellable après "
    "corrections », une régression, R1, que le v11d corrige : `" + C + "/contre-lecture-lanceur-v11c-verification-v1.md`, `"
    + VERIFICATION_V11C + "`) à trois remplacements près (version ; ligne de la clé LUC dans les réglages de l'essai à blanc, "
    "R1 ; épingle de la configuration v11d), lui-même écrit à partir du lanceur v11b" + milieu + PIVOT_27 + ". Le v11e épingle "
    "l'empreinte de ce préenregistrement : ce texte ne peut donc pas porter la sienne, qui est donnée par `course-v11/commandes-"
    "exactes-course-affinage-v11.md` et doit être citée par la contre-lecture, laquelle vérifie aussi que le v11e ne diffère du "
    "v11d que par ces deux lignes ; **commande de lancement** : " + CMD_E + " ; essais du v11d : `tests/test_lancer_course_"
    "affinage_mentors_v11d.py`, `" + ESSAIS_V11D + "` (330 réussis, 4 sautés : rapport v11d, § 3) ; ceux du v11e, s'il en a de "
    "propres, sont donnés par les commandes exactes ; essais de la commande en flux v2 et de la sonde commune v3 : `tests/test_"
    "commande_gemini_flux_v2.py`, `" + ESSAIS_FLUX_V2 + "`, et `tests/test_sonde_astra_courses_v3.py`, `" + ESSAIS_SONDE_V3
    + "` (scellés avec le lanceur v11c, inchangés en v11d) ; gabarit de déclaration des relais : `" + C + "/declaration-relais-"
    "gabarit-course-affinage-v11c.json`, `" + GABARIT_DECLARATION_V11C + "` (scellé avec le lanceur v11c ; aucun gabarit v11d) ; "
    "gabarit du relevé des crédits du jour : `" + C + "/releve-credits-gabarit-course-affinage-v11d.json`, `"
    + GABARIT_CREDITS_V11D + "` (scellé avec le lanceur v11d) ; aucun gabarit du relevé du prix Claude : le lanceur lit le relevé "
    "du jour (`course-v11/releve-prix-claude-course-affinage-v11.json`), jamais un gabarit ; **limite de l'essai à blanc** : "
    "l'essai de bout en bout du développeur n'a tourné que sur un dépôt d'essai, avec un préenregistrement d'essai et le faux "
    "orchestrateur des essais, l'orchestrateur épinglé n'étant pas sur sa machine (rapport v11d, § 2) ; l'essai à blanc réel "
    "(`--a-blanc`) se fait sur la machine de départ, avec l'orchestrateur épinglé (liste d'arrêt) ;")
touchees.add(27)

# ------------------------------------------------------------------------------------------------ liste d'arrêt, règle des clés
sub(91, "la contre-lecture de ce texte et la vérification du lanceur v11d (le lanceur vérifie la première, § Contre-lecture) ;",
    "la contre-lecture de ce texte, et la vérification du lanceur v11d par le même contre-lecteur que le v11c (le lanceur vérifie "
    "la première, § Contre-lecture) ;")
sub(91, "**un essai à blanc** du lanceur v11d, sans appel à un fournisseur, joué jusqu'au manifeste de fin sur la configuration "
        "v11d et versé au dépôt avant le départ réel ;",
    "**un essai à blanc** du lanceur de la course (v11e, commande `--a-blanc` de son en-tête), sur la machine de départ et avec "
    "l'orchestrateur épinglé, sans appel à un fournisseur, joué jusqu'au manifeste de fin sur la configuration v11d et versé au "
    "dépôt avant le départ réel (l'essai de bout en bout du développeur n'a tourné que sur un dépôt d'essai, avec un faux "
    "orchestrateur : pièces) ;")
sub(127, CMD_D, CMD_E)
sub(167, "il cite en entier l'empreinte de ce préenregistrement et celle du lanceur v11d, **porte le libellé « Opus 5.5, "
         "contre-lecteur neuf »**, que le lanceur v11d exige",
    "il cite en entier l'empreinte de ce préenregistrement et celle du lanceur de la course (v11e), **porte le libellé « Opus "
    "5.5, contre-lecteur neuf »**, que le lanceur exige")

# ------------------------------------------------------------------------------------------------ différentiel v10 → v11
sub(291, CMD_D, CMD_E)
sub(292, "essai à blanc du lanceur v11d versé avant le départ ;",
    "essai à blanc du lanceur de la course (v11e), sur la machine de départ avec l'orchestrateur épinglé, versé avant le départ ;")
sub(293, "libellé exigé par les lanceurs v11c et v11d :", "libellé exigé par les lanceurs v11c à v11e :")
sub(295, "lanceur `scripts/lancer_course_affinage_mentors_v11d.py`, lancé par " + CMD_D,
    "lanceur `scripts/lancer_course_affinage_mentors_v11e.py` (le v11d à l'épingle de ce texte près), lancé par " + CMD_E)
sub(296, "Lanceur v11d, configuration v11d (champ inerte retiré),",
    "Lanceur v11e (le v11d à l'épingle de ce texte près), configuration v11d (champ inerte retiré),")

# ------------------------------------------------------------------------------------------------ assemblage
corps = [lignes[n] for n in range(1, 297) if n != 3]
texte = "\n".join(corps) + "\n"
for interdit in ("EMPREINTE À INSCRIRE", "RÉFÉRENCE À INSCRIRE", "RÉGLAGE À INSCRIRE", "État de ce fichier",
                 "## Emplacements et points à trancher", "Du brouillon 1 au brouillon 2"):
    assert interdit not in texte, interdit
for h in (LANCEUR_V11D, ESSAIS_V11D, CONF_V11D, GABARIT_CREDITS_V11D, RAPPORT_V11D, COMMANDE_FLUX_V2, ESSAIS_FLUX_V2,
          SONDE_COMMUNE_V3, ESSAIS_SONDE_V3, GABARIT_DECLARATION_V11C, VERIFICATION_V11C,
          "32366123751ba1d1620cadf4dd4cfda039c0bf35af614a75b49e2d9c04dad7ff"):
    assert h in texte, h
assert texte.count(CMD_E) == 4 and CMD_D not in texte
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 8 touchées :", sorted(touchees), "; ligne 3 et dernière section retirées")
print("lignes du texte :", texte.count("\n"))
