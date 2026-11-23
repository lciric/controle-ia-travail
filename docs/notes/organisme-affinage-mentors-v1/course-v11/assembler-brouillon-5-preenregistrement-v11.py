#!/usr/bin/env python3
"""Assemble le brouillon 5 de la v11 à partir du brouillon 4.

Objet, sur les messages de la session de l'organisme du 23 novembre 2026 (05:31Z et 05:35Z) : citer R-5130 (ses décisions du
23 novembre, registre des décisions de `main`) à l'emplacement de référence ; nommer le lanceur v11d (le v11c à une ligne près),
la configuration v11d et le gabarit du relevé des crédits v11d ; retirer l'emplacement du gabarit du relevé du prix Claude (le
lanceur lit le relevé du jour, jamais un gabarit) ; dire la mesure préalable de la réflexion d'Argon (GO-2026-11-22-128, portée
à Lazar par R-5130) dans ses deux cas, avec et sans ; citer le devis v11d.
Les lignes 1 à 295 du brouillon 4 (celles du brouillon 3) gardent leur numéro ; le point 16 du différentiel v10 → v11 est
ajouté à la ligne 296 ; la dernière section (à retirer de la version scellée) est récrite. Chaque remplacement exige que
l'ancienne chaîne figure exactement une fois dans la ligne visée ; sinon le programme s'arrête.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré dans le brouillon).
Usage : python3 -I assembler-brouillon-5-preenregistrement-v11.py BROUILLON-4.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B1_SHA = "cde6b2d34ddaed05fb5bcd7308896dd0c955bf3d6c15d3db2c5dc99e9f0903f8"
B2_SHA = "4a7e430b81e1e5e3714725bf3c9884dfba75df94f295147bb0794c57e3eadf38"
B3_SHA = "af226efacd7775ab651e10ec9f0e5c25bd60bebcca72094ab5dc8aab4d1927c0"
B4_SHA = "dc711f945276755110aff48fad913590ba0f041d8c28f45b8f7e2441cffbd05d"
DEVIS_V11C_SHA = "94f7f378c36e6af70a05166c9b26e9b012e9a44c7cd4df2ce059fa13a653bb2e"
DEVIS_V11D_SHA = "daf218f260f835a755db63cf1bc214c44a23dbe5880a23bb3d1520f98d5bad7d"
CALCUL_V11C_SHA = "bb52afbcc24cffa591c1ef42473ebd2a9aba9fc5aeb9bc4bf992bdd91e968e5f"
ANNEXE_SHA = "abb967a9e2190f0ca607e8f136e1527105137d42c8225ed8f30a8234f9096b95"
LANCEUR_V11C_SHA = "fe7358b93fa00648c2e4612846789895d809d534c9e3ff8ebf10f33654175548"
ESSAIS_V11C_SHA = "88a61acd4a55b14addbf94b4583a812a87783cd22bdb21f0c00788100e6e086b"
COMMANDE_FLUX_V2_SHA = "13b968eb440279eb77cd9858cefacfb54bc87b11cbf5fc47cf4476044f8e6a50"
ESSAIS_FLUX_V2_SHA = "35e874ef42696243c3847a342b91a674f2fc07817bee9712acb4ee97189c8bed"
SONDE_COMMUNE_V3_SHA = "d02971f0cbe6f15e5be1f58a5050ff86ca48bd9b6a059e478285315fda5c729e"
ESSAIS_SONDE_V3_SHA = "49142a340bcca3638c319eac0e441bebe4f26e8f2c3f9431ebd1da0b43482a86"
CONF_V11C_SHA = "7615a31c8a5ea7a569368847323812685ce33abb929770e4a3f100355a84cb36"
GABARIT_V11C_SHA = "1c0f8f9a074bbec4b873b382214d5aac3bad4b9605d26b69d60a83d87118cd0d"
RAPPORT_V11C_SHA = "a56faf45ba40adc6c4e81ad20546a249c3f9909819dc72b4be7526af326da157"
LU_B4 = {"commit": "2e3221ce5bc369c1031e50ccb0eb1fda850cb491",
         "go": "21e14f64b376829735cc91c11f27381ac12ccca77adca0f8240577b88de1423a",
         "decisions": "792c5162976dbaca142e06c61e2394ae3b286d466c53662206a9b1e76df66318"}
LU_B5 = {"commit": "dbafadaae9ea4fe11ddabd9fe4ba3e26ac134f68",
         "go": "b8a748fc2c49d57e6373404cc4538cc70e1c504374e5d68bd99e352687269312",
         "decisions": "56cd69feea31b8c6fe4c37ab90ad1c1ff5f1e5ed75060f1c8a8481f11e8af7c4"}
CLAUDE_MD_SHA = "605db83acc28c7fcc6d8d12de8edb41bcdb6ea7b37b717967d6fde29f5301960"
N = "docs/notes/organisme-affinage-mentors-v1"
CMD_C = "`GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11c.py`"
CMD_D = "`GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11d.py`"
REF = "RÉFÉRENCE À INSCRIRE : ligne du registre des décisions qui les porte"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B4_SHA, "la source n'est pas le brouillon 4"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 330, len(L)   # 329 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
assert lignes[296] == "" and lignes[297].startswith("## Emplacements et points à trancher avant le scellement")
assert lignes[295].startswith("15. **Chemins et noms**")
ligne_du_b1_au_b4 = lignes[329]
assert ligne_du_b1_au_b4.startswith("Du brouillon 1 au brouillon 2 :") and "Du brouillon 3 au brouillon 4" in ligne_du_b1_au_b4
touchees = set()


def sub(n, ancien, nouveau, fois=1):
    assert lignes[n].count(ancien) == fois, (n, ancien[:80], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


def remplacer(n, debut, fin, nouveau):
    assert lignes[n].startswith(debut) and lignes[n].endswith(fin), (n, lignes[n][:80], lignes[n][-80:])
    lignes[n] = nouveau
    touchees.add(n)


# ------------------------------------------------------------------------------------------------ en-tête
sub(3, "- **État de ce fichier : brouillon 4 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 3 "
       "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-3.md`, `" + B3_SHA + "`),",
    "- **État de ce fichier : brouillon 5 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 4 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-4.md`, `" + B4_SHA + "`), le brouillon 3 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-3.md`, `" + B3_SHA + "`),")
sub(3, "et les décisions de la session de l'organisme du 23 novembre 2026 (réglages d'Argon et de Carbon du lanceur, réflexion "
       "comptée dans la sortie maximale, libellé de la contre-lecture, déclencheurs d'arrêt, entrée de la clé LUC au relevé des "
       "crédits, GO de la course et commande de lancement ; " + REF + " ; seul objet du brouillon 4).",
    "et les décisions de la session de l'organisme du 23 novembre 2026, inscrites sous **R-5130** au registre des décisions "
    "de `main` (réglages d'Argon et de Carbon du lanceur, réflexion comptée dans la sortie maximale, libellé de la "
    "contre-lecture, déclencheurs d'arrêt, entrée de la clé LUC au relevé des crédits, GO de la course et commande de "
    "lancement ; objet du brouillon 4). Objet du brouillon 5 : R-5130 cité ; lanceur v11d, configuration v11d et gabarit du "
    "relevé des crédits v11d nommés ; mesure préalable de la réflexion d'Argon dite dans ses deux cas, avec et sans ; devis "
    "v11d.")
sub(3, "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et « RÉFÉRENCE À INSCRIRE », et une dernière section de "
       "points à trancher : les pièces qu'ils nomment (lanceur v11c et ses essais, configuration v11c, gabarit de déclaration "
       "v11c, commande en flux v2, sonde commune d'Astra v3, gabarits des relevés, commandes exactes) sont en écriture ou en "
       "contre-lecture ailleurs (le lanceur v11c, interrompu le 22 novembre, n'est encore ni scellé ni contre-lu).",
    "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et une dernière section de points à trancher : les pièces "
    "qu'ils nomment (lanceur v11d et ses essais, configuration v11d, gabarit de déclaration, gabarit du relevé des crédits "
    "v11d, commande en flux v2 et sonde commune d'Astra v3 avec leurs essais, commandes exactes) sont en écriture ou en "
    "vérification ailleurs (le lanceur v11c est scellé, `" + LANCEUR_V11C_SHA + "`, et sa vérification par le même "
    "contre-lecteur est en cours ; le v11d, qui en change une ligne, est en écriture).")
sub(4, "elles sont citées ici (pièces) et par le devis v11c.",
    "elles sont citées ici (pièces) et par le devis v11c. Pour le brouillon 5, il a lu en plus les pièces scellées du lanceur "
    "v11c (branche `prep/lanceur-affinage-v11c-interrompu-v1`, commit `1ed883749`), à l'octet celles du travail interrompu, "
    "et R-5130.")
sub(5, "- Date (UTC) de ce brouillon : 2026-11-23T05:22:30Z (`date -u +%FT%TZ`) ; brouillon 3 : 2026-11-22T20:33:49Z ;",
    "- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 4 : 2026-11-23T05:22:30Z ; brouillon 3 : "
    "2026-11-22T20:33:49Z ;")
sub(7, "chiffrée par le devis v11c", "chiffrée par le devis v11d")
sub(7, "lanceur v11c, configuration fixe v11c, relevés et gabarits v11, devis v11c,",
    "lanceur v11d, configuration fixe v11d, relevés et gabarits v11 (gabarit du relevé des crédits v11d), devis v11d,")
sub(8, "GO de la course et commande de lancement (" + REF + ") ;",
    "GO de la course et commande de lancement (**R-5130**, registre des décisions de `main`) ;")
sub(8, "mesure préalable de la réflexion d'Argon, GO-2026-11-22-128 (au plus 10,50 USD, non exécutée ; § Plafond).",
    "mesure préalable de la réflexion d'Argon, GO-2026-11-22-128 (au plus 10,50 USD, hors du plafond de la course ; nœud de "
    "dépense porté à Lazar par R-5130, rien ne part avant son mot ; ses deux cas : liste d'arrêt, « Avant le départ, hors du "
    "lanceur »). Brouillon 5 : registres relus sur `main` au commit `" + LU_B5["commit"] + "` (`registres/go.md` `"
    + LU_B5["go"] + "`, `registres/decisions.md` `" + LU_B5["decisions"] + "`, où figure R-5130).")

# ------------------------------------------------------------------------------------------------ pièces
remplacer(12, "  - configuration fixe de l'orchestrateur, **v11c** : EMPREINTE À INSCRIRE :", "(le lanceur rend le code 5 ; note corrigée en v11c) ;",
          lignes[12]
          .replace("  - configuration fixe de l'orchestrateur, **v11c** : EMPREINTE À INSCRIRE : `" + N + "/course-v11/"
                   "configuration-course-affinage-mentors-v11c.json` — c'est la v9",
                   "  - configuration fixe de l'orchestrateur, **v11d** : EMPREINTE À INSCRIRE : `" + N + "/course-v11/"
                   "configuration-course-affinage-mentors-v11d.json` (la v11c, `" + CONF_V11C_SHA + "`, scellée avec le lanceur "
                   "v11c, aux notes près : en v11d, les notes de Carbon et d'Argon nomment la commande en flux v2, et le champ "
                   "inerte `relais_persistants_v4.plafond_relais_claude_usd`, 150 en v11c, passe à 45 ou est retiré, selon la "
                   "session de l'organisme ; à constater sur la pièce scellée) — c'est la v9", 1))
assert "configuration-course-affinage-mentors-v11d.json" in lignes[12] and "v11c**" not in lignes[12]
sub(14, "`scripts/commande_gemini_flux_v2.py` : EMPREINTE À INSCRIRE (la v1,",
    "`scripts/commande_gemini_flux_v2.py` : EMPREINTE À INSCRIRE (scellée avec le lanceur v11c : `" + COMMANDE_FLUX_V2_SHA
    + "` ; la v1,")
sub(14, "(le lanceur v11c les épingle encore ; une déclaration qui les emploie est refusée)",
    "(les lanceurs v11 à v11d les épinglent encore ; une déclaration qui les emploie est refusée)")
sub(17, "`scripts/sonde_astra_courses_v3.py`, EMPREINTE À INSCRIRE (la v2,",
    "`scripts/sonde_astra_courses_v3.py`, EMPREINTE À INSCRIRE (scellée avec le lanceur v11c : `" + SONDE_COMMUNE_V3_SHA
    + "` ; la v2,")
remplacer(22, "  - **devis v11c** : `", "§ 8 : comparaison aux bornes des v6 à v10 ;",
          lignes[22].replace("  - **devis v11c** : `" + N + "/devis-course-affinage-mentors-v11c.md`, `" + DEVIS_V11C_SHA
                             + "` — c'est le devis v11b",
                             "  - **devis v11d** : `" + N + "/devis-course-affinage-mentors-v11d.md`, `" + DEVIS_V11D_SHA + "` — "
                             "c'est le devis v11c (`" + N + "/devis-course-affinage-mentors-v11c.md`, `" + DEVIS_V11C_SHA + "`) "
                             "sans aucun chiffre changé, à trois choses près : R-5130 cité, lanceur v11d, mesure préalable de la "
                             "réflexion d'Argon dite avec et sans (§ 4 à § 7) ; le devis v11c est le devis v11b", 1)
          .replace("dans ce texte, « devis v11 » désigne ce devis v11c ;", "dans ce texte, « devis v11 » désigne ce devis v11d ;", 1)
          .replace("et de la session de l'organisme (23 novembre), à contre-lire ;",
                   "et de la session de l'organisme (23 novembre, R-5130), à contre-lire ;", 1))
assert "devis-course-affinage-mentors-v11d.md" in lignes[22] and "désigne ce devis v11d" in lignes[22] and "R-5130" in lignes[22]
remplacer(27, "  - lanceur : `scripts/lancer_course_affinage_mentors_v11c.py`, écrit à partir du lanceur v11b",
          "`docs/notes/organisme-affinage-mentors-v1/course-v11/releve-prix-claude-gabarit-course-affinage-v11.json` ;",
          "  - lanceur : `scripts/lancer_course_affinage_mentors_v11d.py`, le lanceur v11c (`scripts/lancer_course_affinage_mentors_"
          "v11c.py`, `" + LANCEUR_V11C_SHA + "`, scellé au commit `1ed883749` de la branche "
          "`prep/lanceur-affinage-v11c-interrompu-v1`, sa vérification par le même contre-lecteur en cours ; rapport `" + N
          + "/course-v11/rapport-developpeur-lanceur-v11c.md`, `" + RAPPORT_V11C_SHA + "`) à une ligne près, celle de la clé LUC "
          "dans les réglages de l'essai à blanc (selon la session de l'organisme), lui-même écrit à partir du lanceur v11b (`scripts/lancer_course_affinage_mentors_"
          "v11b.py`, `a6f64e79ef1f6e480b0b64ebd04a9643d63ee1833f455bb961cd38bf329c7b1a`, contre-lu par un Opus neuf, « Scellable "
          "après corrections » : `" + N + "/course-v11/contre-lecture-lanceur-v11b-v1.md`, "
          "`cd7e5455c1c0a7bf81716746205366af7d66c5a4d79236480efc807efb3ba79d`), lui-même le lanceur v11 "
          "(`bdca413ca51a04f1f4235ea608886e76492154d2a68b2b2180219e4dd2dc2f79`) au GO de la course près, écrit à partir du "
          "lanceur v10 (`scripts/lancer_course_affinage_mentors_v10.py`, "
          "`b08290254982744ba7985232ea54a354bfb31ef7f92ada682d32e349d3294577`, branche de la v10), par un développeur qui n'est "
          "pas le rédacteur de ce texte (il épingle l'empreinte de ce préenregistrement : ce texte ne peut donc pas porter la "
          "sienne, qui est donnée par `course-v11/commandes-exactes-course-affinage-v11.md` et doit être citée par la "
          "contre-lecture ; EMPREINTE À INSCRIRE ici seulement si le lanceur v11d ne porte plus l'empreinte de ce texte dans son "
          "code : `scripts/lancer_course_affinage_mentors_v11d.py`) ; **commande de lancement** : " + CMD_D + " ; ses essais : "
          "EMPREINTE À INSCRIRE : `tests/test_lancer_course_affinage_mentors_v11d.py` (ceux du v11c : `" + ESSAIS_V11C_SHA
          + "`) ; essais de la commande en flux v2 et de la sonde commune v3 : EMPREINTE À INSCRIRE : "
          "`tests/test_commande_gemini_flux_v2.py` (scellés avec le lanceur v11c : `" + ESSAIS_FLUX_V2_SHA + "`) et EMPREINTE À "
          "INSCRIRE : `tests/test_sonde_astra_courses_v3.py` (scellés avec le lanceur v11c : `" + ESSAIS_SONDE_V3_SHA + "`) ; "
          "gabarit de déclaration des relais : EMPREINTE À INSCRIRE : `" + N + "/course-v11/"
          "declaration-relais-gabarit-course-affinage-v11c.json` (scellé avec le lanceur v11c : `" + GABARIT_V11C_SHA + "` ; ou "
          "son successeur v11d s'il en est écrit un) ; gabarit du relevé des crédits du jour : EMPREINTE À INSCRIRE : `" + N
          + "/course-v11/releve-credits-gabarit-course-affinage-v11d.json` (écrit avec le lanceur v11d) ; aucun gabarit du "
          "relevé du prix Claude : le lanceur lit le relevé du jour (`course-v11/releve-prix-claude-course-affinage-v11.json`), "
          "jamais un gabarit ;")

# ------------------------------------------------------------------------------------------------ espèces
sub(60, "arguments épinglés des lanceurs v11 à v11c et du gabarit de déclaration v11c",
    "arguments épinglés des lanceurs v11 à v11d et du gabarit de déclaration v11c")
sub(60, "(configuration v11c, champ `argon_v11.plafond_session_juge_usd`, que le lanceur exige égal à 1,00 ; R-5018)",
    "(configuration v11d, champ `argon_v11.plafond_session_juge_usd`, que le lanceur exige égal à 1,00 ; R-5018)")
sub(60, "et 0,917356 USD sur celle du brouillon du lanceur v11c (11 596 caractères,",
    "et 0,917356 USD sur celle que bâtissent les lanceurs v11c et v11d (11 596 caractères,")
sub(60, "ferait couper l'étape des juges par le plafond d'arrêt ;",
    "ferait couper l'étape des juges par le plafond d'arrêt (la mesure préalable de cette réflexion, si Lazar la confirme, "
    "éprouve ce risque et le suivant avant le départ : liste d'arrêt, « Avant le départ, hors du lanceur ») ;")

# ------------------------------------------------------------------------------------------------ mesure, liste d'arrêt
sub(80, "devis v11 (v11c ; estimation inchangée depuis le v11)", "devis v11 (v11d ; estimation inchangée depuis le v11)")
sub(91, "la contre-lecture de ce texte et celle du lanceur v11c (le lanceur vérifie la première, § Contre-lecture) ;",
    "la contre-lecture de ce texte et la vérification du lanceur v11d (le lanceur vérifie la première, § Contre-lecture) ;")
sub(91, "**un essai à blanc** du lanceur v11c, sans appel à un fournisseur, joué jusqu'au manifeste de fin sur la configuration "
        "v11c et versé au dépôt avant le départ réel ;",
    "**un essai à blanc** du lanceur v11d, sans appel à un fournisseur, joué jusqu'au manifeste de fin sur la configuration "
    "v11d et versé au dépôt avant le départ réel ;")
sub(91, "Après le 2026-11-25, la confirmation par Lazar de la prolongation de l'exception est exigée par le lanceur lui-même "
        "(§ Règle des clés, « Période »).",
    "Après le 2026-11-25, la confirmation par Lazar de la prolongation de l'exception est exigée par le lanceur lui-même "
    "(§ Règle des clés, « Période »). **Mesure préalable de la réflexion d'Argon** (GO-2026-11-22-128, au plus 10,50 USD, "
    "clé de Google, hors du plafond de la course ; nœud de dépense porté à Lazar par R-5130 ; rien ne part avant son mot) — "
    "deux cas, fixés ici avant toute mesure. **(a) Sans la mesure** (Lazar ne la confirme pas) : la course part sous les deux "
    "risques dits au § Espèces et au § Plafond — une réflexion moyenne d'Argon au-delà de 32 476 jetons par appel fait "
    "couper l'étape des juges ; la sortie maximale de 45 056 jetons en flux n'a jamais été servie à Argon —, sans autre "
    "condition. **(b) Avec la mesure** (mot de Lazar) : elle est jouée après le scellement de ce texte et avant le départ, "
    "par la session d'exécution, par la commande en flux épinglée et un relais jeté, aux arguments exacts du gabarit de "
    "déclaration (niveau `high`, provision 24 576, sortie maximale 45 056, prix 4 et 20), sur des consignes de juge et de "
    "proposeur de la course (pièces servies et nombre d'appels fixés par la mère, dans la limite de la ligne) ; elle ne lit "
    "que des comptes (jetons d'entrée, de texte et de réflexion, raison de fin, statut), jamais un contenu ; son rapport est "
    "scellé et versé avant le départ. **Règle de lecture, fixée ici** : le départ est refusé, et la course demande une "
    "version suivante et une décision nommée, si un appel mesuré est refusé par le fournisseur pour sa requête (statut 400 "
    "à 499 hors 429 ; un statut 429 ou de 500 et plus se rejoue, dans la limite de la ligne) ou rend un défaut au sens de la "
    "garde après la réponse (zéro jeton de pensée, fin autre que `STOP` — `MAX_TOKENS` compris —, texte vide), si la "
    "réflexion moyenne mesurée, pondérée comme dans la course (16 appels de proposeur pour 160 de juge ; la moyenne des "
    "seuls appels de juge si aucun appel de proposeur n'est mesuré), passe 32 476 jetons par appel (§ Plafond : le seuil où "
    "l'estimation atteint 150 USD), ou si la mesure reste inachevée ; sinon la course part sous ce texte, inchangé. La mesure porte sur peu d'appels : elle tranche la faisabilité mieux qu'elle ne prédit la réflexion moyenne "
    "de la course, qui reste un risque dit. Le lanceur ne vérifie pas cette mesure : la session d'exécution la tient et la "
    "cite aux commandes exactes.")
sub(95, "(toutes les 10 s dans le lanceur v11c ;", "(toutes les 10 s dans les lanceurs v11c et v11d ;")
sub(95, "(décision du 23 novembre ; contre-lecture du lanceur v11b, constat 7)", "(R-5130 ; contre-lecture du lanceur v11b, constat 7)")

# ------------------------------------------------------------------------------------------------ plafond, règle des clés
sub(101, "**v11** : devis v11 (v11c, écrit pour cette version sur les décisions de la mère, R-5007, point (d), et R-5018, et "
         "sur celles de la session de l'organisme du 23 novembre ; à contre-lire).",
    "**v11** : devis v11 (v11d, écrit pour cette version sur les décisions de la mère, R-5007, point (d), et R-5018, et sur "
    "celles de la session de l'organisme du 23 novembre, R-5130 ; à contre-lire).")
sub(101, "(la mesure préalable que Lazar a accordée, GO-2026-11-22-128, au plus 10,50 USD hors du plafond de la course, et que "
         "R-5018 disait sans objet sur l'ancien réglage, n'est pas exécutée ; devis v11, § 4)",
    "(la mesure préalable que Lazar avait accordée, GO-2026-11-22-128, au plus 10,50 USD hors du plafond de la course, et que "
    "R-5018 disait sans objet sur l'ancien réglage, est de nouveau portée à Lazar, R-5130 ; ses deux cas, avec et sans, sont "
    "fixés à la liste d'arrêt, « Avant le départ, hors du lanceur » ; devis v11, § 4)")
sub(110, "(mêmes budgets d'étapes dans la configuration v11c)", "(mêmes budgets d'étapes dans la configuration v11d)")
sub(127, CMD_C, CMD_D)
sub(135, "(lanceur v11c ; contre-lecture du lanceur v11b, constat 3)", "(lanceurs v11c et v11d ; contre-lecture du lanceur v11b, constat 3)")
sub(138, "**v11c** : toutes les 10 s,", "**v11c et v11d** : toutes les 10 s,")
sub(139, "(lanceur v11c ; contre-lecture du lanceur v11b, constat 7 ; décision du 23 novembre)",
    "(lanceurs v11c et v11d ; contre-lecture du lanceur v11b, constat 7 ; R-5130)")
sub(167, "il cite en entier l'empreinte de ce préenregistrement et celle du lanceur v11c, **porte le libellé « Opus 5.5, "
         "contre-lecteur neuf »**, que le lanceur v11c exige",
    "il cite en entier l'empreinte de ce préenregistrement et celle du lanceur v11d, **porte le libellé « Opus 5.5, "
    "contre-lecteur neuf »**, que le lanceur v11d exige")

# ------------------------------------------------------------------------------------------------ différentiel v10 → v11
sub(279, "; au brouillon 4, décisions de la session de l'organisme du 23 novembre (réglages et lectures du lanceur v11c) :",
    "; aux brouillons 4 et 5, décisions de la session de l'organisme du 23 novembre (R-5130 : réglages et lectures des "
    "lanceurs v11c et v11d ; mesure préalable d'Argon portée à Lazar) :")
sub(289, "(configuration v11c, `argon_v11.plafond_session_juge_usd`, exigé égal à 1,00 ; R-5018)",
    "(configuration v11d, `argon_v11.plafond_session_juge_usd`, exigé égal à 1,00 ; R-5018)")
sub(289, "(0,917356 sur l'entrée de juge du brouillon du lanceur v11c)", "(0,917356 sur l'entrée de juge des lanceurs v11c et v11d)")
sub(290, "10. **Devis v11c** (écrit pour cette version, à contre-lire ; le devis v11b aux réglages d'Argon du lanceur, lui-même "
         "le devis v11 plus le seuil de recharge de la clé LUC) :",
    "10. **Devis v11d** (écrit pour cette version, à contre-lire ; le devis v11c, sans chiffre changé, avec R-5130, le lanceur "
    "v11d et la mesure préalable d'Argon dite avec et sans ; le devis v11c est le devis v11b aux réglages d'Argon du lanceur, "
    "lui-même le devis v11 plus le seuil de recharge de la clé LUC) :")
sub(291, CMD_C, CMD_D)
sub(292, "essai à blanc du lanceur v11c versé avant le départ ;", "essai à blanc du lanceur v11d versé avant le départ ;")
sub(293, "libellé exigé par le lanceur v11c : « Opus 5.5, contre-lecteur neuf »",
    "libellé exigé par les lanceurs v11c et v11d : « Opus 5.5, contre-lecteur neuf »")
sub(294, "14. **Configuration v11c** :", "14. **Configuration v11d** :")
sub(294, "; les configurations v11 et v11b, au GO de la course et à une note près (pièces).",
    "; les configurations v11, v11b et v11c, au GO de la course et aux notes près (pièces).")
sub(295, "lanceur `scripts/lancer_course_affinage_mentors_v11c.py`, lancé par " + CMD_C,
    "lanceur `scripts/lancer_course_affinage_mentors_v11d.py`, lancé par " + CMD_D)
POINT_16 = ("16. **Mesure préalable de la réflexion d'Argon** (brouillon 5 ; R-5130) : deux cas fixés d'avance — sans la mesure, "
            "départ sous les risques dits ; avec la mesure (mot de Lazar ; GO-2026-11-22-128, au plus 10,50 USD, hors du "
            "plafond de la course), règle de lecture : départ refusé si un appel mesuré est refusé par le fournisseur pour sa "
            "requête ou rend un défaut, si la réflexion moyenne mesurée, pondérée comme dans la course, passe 32 476 jetons "
            "par appel, ou si la mesure reste inachevée (liste d'arrêt, « Avant le départ, hors du lanceur »). Lanceur v11d, configuration v11d, gabarit du relevé des crédits v11d, devis v11d ; "
            "emplacement du gabarit du relevé du prix Claude retiré.")

# ------------------------------------------------------------------------------------------------ dernière section, récrite
DERNIERE = """## Emplacements et points à trancher avant le scellement (section à retirer de la version scellée)

Emplacements à remplir (empreintes des pièces du lanceur v11d, que la session de l'organisme envoie quand elles sont définitives ; entre parenthèses, au texte, les valeurs scellées avec le lanceur v11c, qui peuvent encore changer) :

1. EMPREINTE À INSCRIRE — configuration fixe v11d (pièces).
2. EMPREINTE À INSCRIRE — commande en flux v2 d'Argon et de Carbon, et ses essais (pièces). Le relais Gemini v3 est inscrit (`2cf6bc6d…`) ; les réglages d'Argon et de Carbon et les bornes de leurs relais sont inscrits, ceux du code (§ Espèces, liste d'arrêt).
3. EMPREINTE À INSCRIRE — sonde commune d'Astra v3 et ses essais (pièces) ; la sonde d'Astra v3 est inscrite (`32366123…`).
4. EMPREINTE À INSCRIRE — essais du lanceur v11d ; gabarit de déclaration (v11c, ou v11d s'il en est écrit un) ; gabarit du relevé des crédits v11d (pièces) ; celle du lanceur seulement s'il ne porte plus l'empreinte de ce texte dans son code (sinon, cycle d'empreintes).
5. Inscrits : au brouillon 4, le libellé de la contre-lecture (« Opus 5.5, contre-lecteur neuf ») ; au brouillon 5, la référence des décisions du 23 novembre (R-5130) et le retrait du gabarit du relevé du prix Claude (le lanceur lit le relevé du jour, `course-v11/releve-prix-claude-course-affinage-v11.json`, jamais un gabarit).

Points tranchés ou à confirmer, avec la recommandation du rédacteur :

1. **Plafond de session des juges : 1,00 USD** — tranché (R-5018 ; R-5130) : pire cas d'un appel de juge d'Argon 0,917240 USD (lanceur v11b) ou 0,917356 (lanceurs v11c et v11d, entrée de juge de la forme de l'orchestrateur) ; marge de plus de 20 000 jetons d'entrée. La version scellée gardera les deux valeurs, avec leur source.
2. **Page de prix relue le jour du départ** : retenu, inchangé.
3. **Période** : la forme est établie (GO-2026-11-22-80 comme GO de la course ; essai du lanceur v11b sur la vraie lecture de l'orchestrateur). Un départ après le 25 novembre demande la confirmation de Lazar inscrite au registre et nommée dans une configuration neuve, donc un lanceur neuf (R12).
4. **Écrit de la mère sur les autres dépenses de la clé LUC** (R-5007, point (b)) : inchangé ; ce texte le lit « du départ à la fin de la course » et ne le fait pas contrôler par le lanceur ; à confirmer par la mère.
5. **Refus de l'interface et déclencheurs** : tranché (R-5130) : déclencheurs larges et cause écrite telle que le lanceur la lit ; texte aligné (liste d'arrêt ; § Règle des clés, « Clé LUC », point 5).
6. **Mesure préalable de la réflexion d'Argon** (GO-2026-11-22-128) : portée à Lazar (R-5130) ; le texte dit ses deux cas et fixe la règle de lecture (liste d'arrêt). Recommandation du rédacteur, confiance 0,7 : la jouer avant le départ ; elle protège la tentative unique pour au plus 10,50 USD et éprouve aussi la sortie de 45 056 jetons en flux (point 7). Reste à la mère, si Lazar la confirme : les consignes servies et le nombre d'appels de la mesure. Seuil de la règle : 32 476 jetons, où l'estimation sans marge atteint 150 USD ; 31 462 si la mère veut la marge de 10 % sur les autres postes (recommandation : 32 476, le seuil de l'estimation centrale, la mesure ne prédisant pas la moyenne de la course ; confiance 0,6).
7. **Argon à 45 056 jetons de sortie en flux** : jamais servi au-delà de 32 768 dans les pièces lues. Sans la mesure, un refus du fournisseur pour ce réglage ferait échouer chaque appel d'Argon, et A3 arrêterait ses deux rôles (étape des juges « non mesurée (technique) ») ; avec la mesure, un tel refus interdit le départ (liste d'arrêt). La porte à blanc et l'essai à blanc n'appellent pas le fournisseur.
8. **Notes de la configuration** : corrigées en v11d selon la session de l'organisme (commande en flux v2 nommée ; champ inerte `relais_persistants_v4.plafond_relais_claude_usd` à 45 ou retiré) ; à constater sur la pièce scellée (recommandation : le retirer plutôt que le passer à 45, aucune garde n'en dépendant ; confiance 0,6).

Points que ce texte fixe et que le lanceur v11d doit tenir, avec un essai sain et un essai artefact chacun (R5) ; si le lanceur fait autrement, le texte ou le lanceur change, jamais un écart silencieux. La liste phrase par phrase est dans `course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md` (`""" + ANNEXE_SHA + """`), écrite sur le brouillon 2 : ses numéros de lignes (l. 1 à 295) valent pour ce brouillon 5, dont seules la ligne 296 (point 16 du différentiel) et la dernière section changent ; les brouillons 4 et 5 changent les phrases des items A1 à A4 (GO de la course GO-2026-11-22-80, GO-2026-11-18-14 exigé, registre dérivé, confirmation nommée dans la configuration), B2 et B5 (champs `solde_non_lu` et `reference`, montants et champs hors liste refusés ; gabarit du relevé des crédits v11d), C1 (réserve par appel lue et écrite), C4 (lecture confirmée par l'essai du développeur du lanceur v11), D1 à D4 et D6 (lecture toutes les 10 s, journal du run nommé ; déclencheurs élargis — l'item D3 est renversé : les refus propres au relais, 401, 403, 404 et 413, arrêtent la course — ; part engagée au plafond ; état illisible trois fois ; cause écrite ; relecture finale refaite jusqu'à trois fois), F1 à F5 (garde rejouée sur le corps de l'entrée la plus longue ; limite de l'invite comptée en caractères ; réglages et bornes du relais écrits ; trois gardes des v8 et v9 gardées en flux), G1 à G4 (même commande que Carbon ; garde rejouée sur la plus longue entrée de chaque rôle, juge dans la forme de l'orchestrateur ; pire cas du juge sur un cadre de 1 000 caractères supposé, non « réel » ; champ `argon_v11.plafond_session_juge_usd` ; bornes du relais d'Argon), I2 (base 35,683 : exacte 35,683407, lanceur 35,683424), I4 (libellé) et I6 (pièces : lanceur v11d, commande en flux v2, relais Gemini v3, sondes v3 ; aucun gabarit du relevé du prix Claude), et la section K (dépôt de travail qui porte la garde commune de `main` ; mesure préalable de la réflexion d'Argon, tenue hors du lanceur, l. 91). En résumé :

- le plafond du relais Claude égal à 45,00 USD au centime (arguments lus par PID et état), sa réserve par appel lue et écrite, et l'entrée de la clé LUC au relevé des crédits (`solde_non_lu` vrai, `reference` GO-2026-11-22-124, aucun montant, aucun autre champ que `source` et `note`) ;
- le GO de la course GO-2026-11-22-80 passé à l'orchestrateur et nommé par la configuration ; la lecture des lignes GO-2026-11-18-14, GO-2026-11-22-80, GO-2026-11-22-107 et GO-2026-11-22-124, et, après le 2026-11-25, de la ligne de confirmation nommée dans la configuration ;
- le relevé de l'état et du journal du relais Claude au moins une fois par minute (toutes les 10 s), le journal du run, l'arrêt au premier déclencheur (statut 400 à 499 hors 429 au journal, refus compté dans l'état, part engagée au plafond, trois lectures illisibles), la relecture finale, le code 5 et l'alerte `alerte-arret-part-claude.json` (nature, statut, cause lue) ;
- la garde gelée des appels aux modèles de Google sur la commande en flux de Carbon et d'Argon, avant l'envoi et après la réponse ; les prix d'Argon et de Carbon à 4 et 20 USD par million de jetons ; les réglages d'Argon (24 576, 45 056, en flux) et de Carbon (28 672, 65 536) ; le plafond de session des juges à 1,00 USD, et le pire cas d'un appel de juge d'Argon contrôlé sur la plus longue entrée de juge que bâtit le lanceur ;
- la sonde d'Astra faite avec `gpt-6.2-astra`, `OPENAI_API_KEY_2` et les prix 8 et 40, liée à la sonde commune v3 du jour, qui porte la variable de clé du relais jeté ;
- la base de l'écart au devis, 35,683 USD pour cinq espèces ;
- le libellé « Opus 5.5, contre-lecteur neuf » exigé de la contre-lecture ;
- les gardes héritées des lanceurs v7 à v10 que ce texte garde (bornes basses de tous les relais, exclusion mutuelle avec la course d'auto-conception, sonde liée à la sonde commune, état de relais neuf et lisible, codes de sortie distincts dont le code 6, plafond de session des proposeurs à 3,00 USD).

"""
DU_B4_AU_B5 = (" Du brouillon 4 au brouillon 5 (sur les messages de la session de l'organisme du 23 novembre, 05:31Z et 05:35Z) : "
               "R-5130 cité à l'emplacement de référence ; lanceur v11d (le v11c à une ligne près), configuration v11d et gabarit "
               "du relevé des crédits v11d nommés, valeurs scellées avec le lanceur v11c données à côté des emplacements ; "
               "emplacement du gabarit du relevé du prix Claude retiré ; mesure préalable de la réflexion d'Argon dite dans ses "
               "deux cas, avec sa règle de lecture (liste d'arrêt ; point 16 du différentiel) ; devis v11d ; aucun chiffre "
               "changé.")
corps = [lignes[n] for n in range(1, 296)]
texte = "\n".join(corps) + "\n" + POINT_16 + "\n\n" + DERNIERE + ligne_du_b1_au_b4 + DU_B4_AU_B5 + "\n"
assert "RÉGLAGE À INSCRIRE" not in texte and "RÉFÉRENCE À INSCRIRE" not in texte
assert "lancer_course_affinage_mentors_v11c.py`" not in texte.replace("(`scripts/lancer_course_affinage_mentors_v11c.py`, `", "")
assert "releve-prix-claude-gabarit" not in texte
assert texte.count("\n## Emplacements et points à trancher avant le scellement") == 1
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 4 touchées (1 à 295) :", sorted(touchees))
print("lignes du brouillon 5 :", texte.count("\n"))
print("emplacements « EMPREINTE À INSCRIRE » :", texte.count("EMPREINTE À INSCRIRE"))
