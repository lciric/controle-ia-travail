#!/usr/bin/env python3
"""Assemble le brouillon 4 de la v11 à partir du brouillon 3.

Objet : porter les décisions de la session de l'organisme du 23 novembre 2026 — réglages d'Argon du code (provision de
réflexion 24 576 jetons, sortie maximale 45 056, en flux) ; réflexion de Carbon (et d'Argon) comptée dans la sortie maximale,
sur la page de Google versée sur `main` (`fe0b8d88…`), pire cas de Carbon 1,32 USD, que seule la facture d'une course réelle
confirmera ; libellé de contre-lecture « Opus 5.5, contre-lecteur neuf » ; déclencheurs d'arrêt du lanceur (refus propres au
relais, part engagée au plafond, état illisible trois fois) et cause écrite ; entrée de la clé LUC au relevé des crédits ;
GO de la course GO-2026-11-22-80 et commande de lancement du lanceur v11c — et citer le devis v11c.
Les lignes 1 à 296 du brouillon 3 gardent leur numéro (l'annexe des phrases qui supposent une garde du lanceur, écrite sur le
brouillon 2, vaut pour elles, aux phrases changées près, listées dans la dernière section) ; la dernière section (l. 297 et
suivantes, à retirer de la version scellée) est récrite. Chaque remplacement exige que l'ancienne chaîne figure exactement une
fois dans la ligne visée ; sinon le programme s'arrête.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré dans le brouillon).
Usage : python3 -I assembler-brouillon-4-preenregistrement-v11.py BROUILLON-3.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B1_SHA = "cde6b2d34ddaed05fb5bcd7308896dd0c955bf3d6c15d3db2c5dc99e9f0903f8"
B2_SHA = "4a7e430b81e1e5e3714725bf3c9884dfba75df94f295147bb0794c57e3eadf38"
B3_SHA = "af226efacd7775ab651e10ec9f0e5c25bd60bebcca72094ab5dc8aab4d1927c0"
DEVIS_V11_SHA = "34271cb3cb3dba89c897cc076f7a65cbf73630d96f7106f2f40adac9a2590d52"
DEVIS_V11B_SHA = "13d962b1c56f17235e1e4b90b9b166239c5bb6d0c1bb6c400b3f07ac59a88c03"
DEVIS_V11C_SHA = "94f7f378c36e6af70a05166c9b26e9b012e9a44c7cd4df2ce059fa13a653bb2e"
CALCUL_V11_SHA = "deac25b6fe59332b646cd7b67580126221f3aa5f547623a6270c58b2330428ee"
CALCUL_V11B_SHA = "cf316ba4db4005e2d64a114f4f4aea93187ebfa372a3bf072594e5513f8cd0e6"
CALCUL_V11C_SHA = "bb52afbcc24cffa591c1ef42473ebd2a9aba9fc5aeb9bc4bf992bdd91e968e5f"
ANNEXE_SHA = "abb967a9e2190f0ca607e8f136e1527105137d42c8225ed8f30a8234f9096b95"
CONTRE_LECTURE_LANCEUR_V11B_SHA = "cd7e5455c1c0a7bf81716746205366af7d66c5a4d79236480efc807efb3ba79d"
LANCEUR_V10_SHA = "b08290254982744ba7985232ea54a354bfb31ef7f92ada682d32e349d3294577"
LANCEUR_V11_SHA = "bdca413ca51a04f1f4235ea608886e76492154d2a68b2b2180219e4dd2dc2f79"
LANCEUR_V11B_SHA = "a6f64e79ef1f6e480b0b64ebd04a9643d63ee1833f455bb961cd38bf329c7b1a"
COMMANDE_FLUX_V1_SHA = "6aaf235df31eccd7199c0bcea1e8b68009d56d03c66a01427d05ae8137fdbf55"
RELAIS_GEMINI_V3_SHA = "2cf6bc6df83f8847e75911c8cc0b6153c4467b36ce69273de649b5cbdc7e2378"
SONDE_V3_SHA = "32366123751ba1d1620cadf4dd4cfda039c0bf35af614a75b49e2d9c04dad7ff"
SONDE_COMMUNE_V2_SHA = "80074c82c8ea79d059c9f74b3ae89f7f50635283672a4bd26f1c2e77c27d6704"
PAGE_REFLEXION_SHA = "fe0b8d8820b2ab7b8079bf1477e7871f850f6f5450f92f6b844866cade105892"
PROVENANCE_PAGE_SHA = "2cc1bdc8d6fc58fc75d9cc530f841ccc84d27b870c77b18e2995767cfbe8aaa9"
CONF_V11_SHA = "25d40914192f2c9a1dc849681bf5c31d76bf58c7f15f428f0ac4515bf69c8567"
CONF_V11B_SHA = "c69620daa06a9c39b129038788ebdfd7f6530123d9726674ee14a3244f4795f2"
ANCIEN = {"commit": "61ec4bb16537d899d431fe7a74d10b0c17053d86",
          "go": "8f54197a90d07412e4d7e1aa38e482cea57b5429cb0d01d7eb35ab2a85f64453",
          "decisions": "d70dd20afbd5d3b746b1a74ad013a37fec05dde6b25429a67dce4542204855ab"}
NEUF = {"commit": "2e3221ce5bc369c1031e50ccb0eb1fda850cb491",
        "go": "21e14f64b376829735cc91c11f27381ac12ccca77adca0f8240577b88de1423a",
        "decisions": "792c5162976dbaca142e06c61e2394ae3b286d466c53662206a9b1e76df66318"}
CLAUDE_MD_SHA = "605db83acc28c7fcc6d8d12de8edb41bcdb6ea7b37b717967d6fde29f5301960"
N = "docs/notes/organisme-affinage-mentors-v1"
COMMANDE_LANCEMENT = "`GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11c.py`"
REF = "RÉFÉRENCE À INSCRIRE : ligne du registre des décisions qui les porte"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B3_SHA, "la source n'est pas le brouillon 3"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 327, len(L)   # 326 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
assert lignes[297].startswith("## Emplacements et points à trancher avant le scellement") and lignes[296] == ""
ligne_326_b3 = lignes[326]
touchees = set()


def sub(n, ancien, nouveau):
    assert lignes[n].count(ancien) == 1, (n, ancien[:80], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


def remplacer(n, debut, fin, nouveau):
    """Remplace la ligne n entière, après avoir vérifié son début et sa fin."""
    assert lignes[n].startswith(debut) and lignes[n].endswith(fin), (n, lignes[n][:80], lignes[n][-80:])
    lignes[n] = nouveau
    touchees.add(n)


# ------------------------------------------------------------------------------------------------ en-tête
sub(3, "- **État de ce fichier : brouillon 3 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 2 "
       "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-2.md`, `" + B2_SHA + "`) et le brouillon 1 "
       "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-1.md`, `" + B1_SHA + "`), qui restent en place "
       "(R12), après les décisions de la mère sur cette version (R-4995, R-5006, R-5007, R-5018) et les mots de Lazar "
       "inscrits en GO-2026-11-22-124 et en R-5042 (seuil de recharge de la clé LUC ; seul objet du brouillon 3).",
    "- **État de ce fichier : brouillon 4 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 3 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-3.md`, `" + B3_SHA + "`), le brouillon 2 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-2.md`, `" + B2_SHA + "`) et le brouillon 1 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-1.md`, `" + B1_SHA + "`), qui restent en place "
    "(R12), après les décisions de la mère sur cette version (R-4995, R-5006, R-5007, R-5018), les mots de Lazar inscrits en "
    "GO-2026-11-22-124 et en R-5042, et les décisions de la session de l'organisme du 23 novembre 2026 (réglages d'Argon et "
    "de Carbon du lanceur, réflexion comptée dans la sortie maximale, libellé de la contre-lecture, déclencheurs d'arrêt, "
    "entrée de la clé LUC au relevé des crédits, GO de la course et commande de lancement ; " + REF + " ; seul objet du "
    "brouillon 4).")
sub(3, "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et « RÉGLAGE À INSCRIRE », et une dernière section de "
       "points à trancher : les pièces qu'ils nomment (lanceur, essais, gabarits, configuration, commandes et relais de Carbon "
       "et d'Argon, sonde d'Astra) sont en écriture ou en contre-lecture ailleurs.",
    "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et « RÉFÉRENCE À INSCRIRE », et une dernière section de "
    "points à trancher : les pièces qu'ils nomment (lanceur v11c et ses essais, configuration v11c, gabarit de déclaration "
    "v11c, commande en flux v2, sonde commune d'Astra v3, gabarits des relevés, commandes exactes) sont en écriture ou en "
    "contre-lecture ailleurs (le lanceur v11c, interrompu le 22 novembre, n'est encore ni scellé ni contre-lu).")
sub(4, "- Auteur de la v11 : le rédacteur neuf que mandate la session de l'organisme (mandat "
       "`docs/notes/organisme-affinage-mentors-v1/course-v8/mandat-fable-preenregistrement-affinage-v8.md`, "
       "`0f7ddc5487459ecc637db8b29f0fbad6b47deda43d7fa47f79fec4a98a8f9ec2`, branche `lot/compte-organisme-v1` ; ce mandat nomme "
       "son modèle et son effort), sur l'accord de la mère et la ligne GO-2026-11-22-107 ; il n'a écrit ni le lanceur ni "
       "aucune version antérieure, et n'a lu aucune sortie de course ni aucune réponse de modèle.",
    "- Auteurs de la v11 : brouillons 1 à 3, le rédacteur neuf que mandate la session de l'organisme (mandat "
    "`docs/notes/organisme-affinage-mentors-v1/course-v8/mandat-fable-preenregistrement-affinage-v8.md`, "
    "`0f7ddc5487459ecc637db8b29f0fbad6b47deda43d7fa47f79fec4a98a8f9ec2`, branche `lot/compte-organisme-v1` ; ce mandat nomme "
    "Fable 5.2 en effort maximal), sur l'accord de la mère et la ligne GO-2026-11-22-107 ; **brouillon 4 et suivants : un "
    "rédacteur neuf, Opus 5.5 en effort maximal**, sur GO-2026-11-22-145 (quota de Fable épuisé jusqu'au "
    "2026-11-29T18:00Z, R-5071 : Opus 5.5 en effort maximal écrit les pièces réservées à Fable, contre-lecture par un Opus "
    "neuf) — **écart déclaré** à R-3735 (« Qui conçoit ») et à GO-2026-11-21-75 (« Économie de Fable »), qui réservent les "
    "préenregistrements à Fable 5.2 ; aucun des deux n'a écrit le lanceur ni aucune version antérieure, et aucun n'a lu une "
    "sortie de course ni une réponse de modèle.")
sub(4, "Pour les réglages de la garde et pour les prix, il a lu deux notes de contrôle du collisionneur sur `main` (réglages et "
       "comptes de jetons seulement, aucun contenu de réponse) et la page de prix du fournisseur versée au dépôt ; elles sont "
       "citées par le devis v11.",
    "Pour les réglages de la garde et pour les prix, le rédacteur des brouillons 1 à 3 a lu deux notes de contrôle du "
    "collisionneur sur `main` (réglages et comptes de jetons seulement, aucun contenu de réponse) et la page de prix du "
    "fournisseur versée au dépôt ; elles sont citées par le devis v11. Pour le brouillon 4, le rédacteur a lu en plus la "
    "contre-lecture du lanceur v11b, les rapports du développeur des lanceurs v11, v11b et v11c, le travail interrompu du "
    "lanceur v11c (lanceur, configuration, gabarit de déclaration, commande en flux v2 ; non scellés), la garde commune et la "
    "page de Google sur la réflexion versée sur `main` ; elles sont citées ici (pièces) et par le devis v11c.")
sub(5, "- Date (UTC) de ce brouillon : 2026-11-22T20:33:49Z (`date -u +%FT%TZ`) ; brouillon 2 : 2026-11-22T19:53:46Z ; "
       "brouillon 1 : 2026-11-22T18:54:51Z ;",
    "- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 3 : 2026-11-22T20:33:49Z ; brouillon 2 : "
    "2026-11-22T19:53:46Z ; brouillon 1 : 2026-11-22T18:54:51Z ;")
sub(5, "non versées dans `lot/compte-organisme-v1` à sa tête `f3bd4d17` du 22 novembre :",
    "non versées dans `lot/compte-organisme-v1` à sa tête `f3bd4d17` du 22 novembre (ni à sa tête `13507916`, relue pour le "
    "brouillon 4) :")
sub(5, "cherchée par les mots « affinage » et « mentors »).",
    "cherchée par les mots « affinage » et « mentors » ; revérifié pour le brouillon 4 sur `main` à `2e3221ce` et sur "
    "`lot/compte-organisme-v1` à `13507916`).")
sub(7, "(4) **Argon** — sous la même garde gelée, qui vaut pour tout envoi à un modèle de Google (décision de la mère, R-5007, "
       "point (c)) ;",
    "(4) **Argon** — sous la même garde gelée, qui vaut pour tout envoi à un modèle de Google (décision de la mère, R-5007, "
    "point (c)), aux réglages du lanceur (niveau `high`, provision de réflexion 24 576 jetons, sortie maximale 45 056, en "
    "flux ; brouillon 4) ;")
sub(7, "(5) **plafond de session des juges** — 1,00 USD au lieu de 0,60, conséquence de (4), chiffrée par le devis v11 "
       "(R-5007, point (c) ; R-5018) ;",
    "(5) **plafond de session des juges** — 1,00 USD au lieu de 0,60, conséquence de (4), chiffrée par le devis v11c "
    "(R-5007, point (c) ; R-5018 ; pire cas d'un appel de juge d'Argon 0,917240 USD, la réflexion comprise dans la sortie "
    "maximale) ;")
sub(7, "S'y ajoutent leurs seules conséquences mécaniques : noms et chemins `v11`, configuration fixe v11, relevés et "
       "gabarits v11, devis v11, contre-lecteur.",
    "S'y ajoutent leurs seules conséquences mécaniques : noms et chemins `v11`, lanceur v11c, configuration fixe v11c, "
    "relevés et gabarits v11, devis v11c, contre-lecteur et son libellé, GO de la course passé à l'orchestrateur "
    "(GO-2026-11-22-80, prolongation de GO-2026-11-18-14 ; § Règle des clés, « Période »).")
sub(8, "prolongation de GO-2026-11-18-14 au 2026-12-15 (GO-2026-11-22-80) ;",
    "prolongation de GO-2026-11-18-14 au 2026-12-15 (GO-2026-11-22-80), **GO de la course** passé à l'orchestrateur et cité "
    "par la commande de lancement (décision de la mère sur le point ouvert 11 du rapport du développeur du lanceur v11 ; "
    "configurations v11b et suivantes, champ `changements_v11.go_course`) ;")
sub(8, "Lignes lues sur `main` au commit `" + ANCIEN["commit"] + "` : `registres/go.md` (`" + ANCIEN["go"] + "`), "
       "`registres/decisions.md` (`" + ANCIEN["decisions"] + "`), `CLAUDE.md` (`" + CLAUDE_MD_SHA + "`).",
    "**Brouillon 4** : décisions de la session de l'organisme du 23 novembre 2026 — réglages d'Argon et de Carbon suivant le "
    "code, réflexion comptée dans la sortie maximale, libellé de la contre-lecture, déclencheurs d'arrêt, entrée de la clé LUC "
    "au relevé des crédits, GO de la course et commande de lancement (" + REF + ") ; rédacteur Opus 5.5 en effort maximal "
    "sur GO-2026-11-22-145 ; mesure préalable de la réflexion d'Argon, GO-2026-11-22-128 (au plus 10,50 USD, non exécutée ; "
    "§ Plafond). Lignes lues sur `main` au commit `" + NEUF["commit"] + "` : `registres/go.md` (`" + NEUF["go"] + "`), "
    "`registres/decisions.md` (`" + NEUF["decisions"] + "`), `CLAUDE.md` (`" + CLAUDE_MD_SHA + "`, inchangé depuis le "
    "brouillon 3) ; brouillon 3 : commit `" + ANCIEN["commit"] + "` (`registres/go.md` `" + ANCIEN["go"] + "`, "
    "`registres/decisions.md` `" + ANCIEN["decisions"] + "`).")

# ------------------------------------------------------------------------------------------------ pièces
remplacer(12, "  - configuration fixe de l'orchestrateur, **v11** : EMPREINTE À INSCRIRE :", "items du juge : **inchangés** ;",
          "  - configuration fixe de l'orchestrateur, **v11c** : EMPREINTE À INSCRIRE : `" + N + "/course-v11/"
          "configuration-course-affinage-mentors-v11c.json` — c'est la v9 (`" + N + "/course-v9/"
          "configuration-course-affinage-mentors-v9.json`, `e7378f89ae39eacd169ff912526a8e998e4f01f0aba235eeaa0bf12e4b195d5d`, "
          "branche de la v10 ; elle-même la v6, `0ea89ed2f72ce2693e619eb10b6eecbd46725d4578b548a44c5a98b9bb1ded21`, au plafond "
          "de session des proposeurs près, 3,00 USD au lieu de 1,50) dont seuls changent : le nom de la clé Claude "
          "(`RR_ANTHROPIC_API_KEY_LUC`, à `cles.claude` et à la clé des deux espèces Claude ; la clé Minuit rejoint la clé "
          "Rigaud dans les clés interdites ; le crédit déclaré de 200 USD de la clé Minuit est retiré) ; un bloc "
          "`changements_v11` neuf — plafond de la part Claude (`plafond_part_claude_usd`, **45 USD** ; § Règle des clés), GO "
          "de la course (`go_course`, GO-2026-11-22-80) et GO prolongé (`go_course_initial`, GO-2026-11-18-14), emplacement de "
          "la confirmation de la prolongation de GO-2026-11-22-107 (`confirmation_prolongation_go_107`, vide aujourd'hui ; "
          "§ Règle des clés, « Période »), notes sur la clé, Astra, Carbon, Argon et les prix — ; un bloc `argon_v11` neuf, "
          "dont le champ `plafond_session_juge_usd` vaut **1,00 USD**, que le lanceur exige égal à 1,00 et écrit, à la place "
          "de 0,60, au plafond de session des juges de la configuration servie à l'orchestrateur (§ Espèces, « Argon ») ; la "
          "version et le statut. Budget, plafonds de relais des étapes, plafonds de session des proposeurs (3,00 USD) et de "
          "l'aiguilleur (0,25 USD), espèces, aiguilleur, juges, graines et items du juge : **inchangés**. Les blocs descriptifs "
          "hérités (`relais_persistants_v4`, dont le champ `plafond_relais_claude_usd` garde 150, et `carbon_v5`, qui décrit "
          "le lot) ne sont ni servis à l'orchestrateur ni lus par le lanceur pour ces valeurs : le plafond exigé du relais "
          "Claude est celui de `changements_v11` (45 USD). Configurations v11 (`" + CONF_V11_SHA + "`) et v11b (`"
          + CONF_V11B_SHA + "`), branche `lot/compte-organisme-v1` : même contenu que la v11c à deux points près — la v11 "
          "n'a pas le GO de la course, et les deux disent « code 7 » pour l'arrêt sur la part Claude, dans une note (le "
          "lanceur rend le code 5 ; note corrigée en v11c) ;")
remplacer(14, "  - commandes et relais des espèces hors Claude (copies de `main` ou de la branche,",
          "ne sont plus employés ;",
          "  - commandes et relais des espèces hors Claude (copies de `main` ou de la branche, extraites hors dépôt ou présentes "
          "dans le dépôt de travail, vérifiées à l'empreinte) : **Astra** — `commande_astra_v1.py` "
          "`986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` (inchangée : le modèle et les prix sont ses "
          "arguments), relais compatible OpenAI `relais_kimi_v4.py` (empreinte à la ligne de la procédure, plus bas) ; "
          "**Argon et Carbon, v11** — une seule commande en flux sous la garde gelée, `scripts/commande_gemini_flux_v2.py` : "
          "EMPREINTE À INSCRIRE (la v1, `scripts/commande_gemini_flux_v1.py`, `" + COMMANDE_FLUX_V1_SHA + "`, contre-lue avec "
          "le lanceur v11b, reste en place ; la v2 vérifie en plus, après chaque réponse, que texte et réflexion tiennent "
          "ensemble dans la sortie maximale) ; un relais par espèce, le relais Gemini v3 en flux de `main`, "
          "`docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v3.py`, `" + RELAIS_GEMINI_V3_SHA + "` (Argon au "
          "port 8788, Carbon au port 8791 ; il tient la clé, lit l'amont en flux et demande les pensées en retour ; il ne porte "
          "aucun prix et borne des appels) ; **retraits** : la commande `commande_argon_v3d.py` "
          "(`46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46`) sous l'enveloppe `appel-argon-v5.sh` "
          "(`37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a`), épinglée de la v6 à la v10, ne tient pas la "
          "garde (§ Espèces) et n'est plus employée (le lanceur v11c les épingle encore ; une déclaration qui les emploie est "
          "refusée) ; le relais Gemini v2 `relais_gemini_v2.py` "
          "(`2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb`) n'est plus employé ; la commande Gemini par lot "
          "`commande_gemini_lot_v1.py` (`9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75`) et le relais "
          "Gemini v4 `relais_gemini_v4.py` (`543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4`) ne sont plus "
          "employés ;")
sub(15, "(règle : `CLAUDE.md` de `main`, « Appels aux modèles de Google » et « Appels à Carbon ») ;",
    "(règle : `CLAUDE.md` de `main`, « Appels aux modèles de Google » et « Appels à Carbon ») ; elle doit être présente, à "
    "cette empreinte, dans le dépôt de travail d'où part la course : le lanceur et la commande en flux la vérifient, et la "
    "branche `lot/compte-organisme-v1` ne la porte pas — les commandes exactes disent comment l'extraire de `main` "
    "(contre-lecture du lanceur v11b, constat 14) ;")
sub(16, "copie versée, non une lecture de la console de facturation ;",
    "copie versée, non une lecture de la console de facturation ; page de Google sur la réflexion (**v11**, brouillon 4) : "
    "`docs/sources/google-gemini-reflexion-v1/gemini-thinking-generate-content-2026-11-21-v1.md.txt` sur `main`, `"
    + PAGE_REFLEXION_SHA + "` (provenance : `docs/sources/google-gemini-reflexion-v1/provenance-v1.md`, `"
    + PROVENANCE_PAGE_SHA + "`), l. 914-916, 918-922, 1220-1222 et 1273-1274 (la sortie maximale compte la réflexion ; "
    "coupure dure en `MAX_TOKENS`, la réflexion produite restant facturée ; réflexion facturée au prix de sortie) et l. 931 "
    "(65 536 jetons par requête en flux pour Carbon et Argon, 32 768 hors flux) ;")
remplacer(17, "  - sonde d'Astra, **v11** : EMPREINTE À INSCRIRE :", "un rapport fait avec `gpt-6-astra`, ou un autre jour, ne vaut pas ;",
          "  - sonde d'Astra, **v11** : `scripts/sonde_astra_affinage_v3.py`, `" + SONDE_V3_SHA + "` (contre-lue avec le lanceur "
          "v11b) ; sonde commune, qui contrôle le relais jeté avant l'appel, **v3** : `scripts/sonde_astra_courses_v3.py`, "
          "EMPREINTE À INSCRIRE (la v2, `scripts/sonde_astra_courses_v2.py`, `" + SONDE_COMMUNE_V2_SHA + "`, ne contrôlait pas "
          "la variable de clé du relais jeté : contre-lecture du lanceur v11b, constat 9 ; la v3 exige `--variable-cle "
          "OPENAI_API_KEY_2`, une seule fois, dans la ligne de commande du relais jeté lue par son PID, et l'écrit à son "
          "rapport) — la sonde v2 (`scripts/sonde_astra_affinage_v2.py`, "
          "`1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7`) et la sonde commune v1 "
          "(`scripts/sonde_astra_courses_v1.py`, `d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777`) portent le "
          "nom `gpt-6-astra` en dur : elles ne servent plus ; comme depuis la v7, le lanceur n'accepte le rapport de la sonde "
          "que lié, par son empreinte et par le PID du relais jeté, au rapport réussi de la sonde commune du même jour (un "
          "seul), de version `sonde_astra_courses_v3` ; rapports sous `course-v11/`, aux noms datés "
          "(`sonde-astra-course-affinage-v11-AAAA-MM-JJ.json`, ou sans date, et `sonde-astra-commune-AAAA-MM-JJ-v2.json`, nom "
          "gardé du lanceur v11b, la version étant lue dans le contenu) ; un rapport fait avec `gpt-6-astra`, ou un autre "
          "jour, ne vaut pas ;")
remplacer(22, "  - **devis v11b** : `", "§ 8 : comparaison aux bornes des v6 à v10 ;",
          "  - **devis v11c** : `" + N + "/devis-course-affinage-mentors-v11c.md`, `" + DEVIS_V11C_SHA + "` — c'est le devis "
          "v11b (`" + N + "/devis-course-affinage-mentors-v11b.md`, `" + DEVIS_V11B_SHA + "` ; lui-même le devis v11, `" + N
          + "/devis-course-affinage-mentors-v11.md`, `" + DEVIS_V11_SHA + "`, plus le seuil de recharge de la clé LUC, R-5042, "
          "§ 5 bis) refait aux réglages d'Argon du lanceur (provision 24 576, sortie maximale 45 056, en flux) et à la seule "
          "lecture « réflexion comprise dans la sortie maximale » ; l'estimation ne change pas ; dans ce texte, « devis v11 » "
          "désigne ce devis v11c ; écrit pour cette version sur les décisions de la mère (R-5007, point (d) ; R-5018) et de la "
          "session de l'organisme (23 novembre), à contre-lire ; ses chiffres sont recalculés par `" + N + "/course-v11/"
          "calcul-devis-course-affinage-mentors-v11c.py`, `" + CALCUL_V11C_SHA + "` (176 chiffres contrôlés, aucun écart ; "
          "programmes des devis v11 et v11b : `" + CALCUL_V11_SHA + "`, `" + CALCUL_V11B_SHA + "`) — Argon et Carbon comptés à "
          "4 et 20 USD par million de jetons, réflexion comprise dans la sortie maximale ; Carbon au prix plein (0,4805 USD "
          "par appel estimé, 1,32 au pire) ; plafond de session des juges 1,00 USD au lieu de 0,60, pire cas d'un appel de "
          "juge d'Argon 0,917240 USD (§ 2) ; cinq espèces, **sans la réflexion d'Argon**, non mesurée : 35,68 USD sans marge, "
          "39,25 avec ; 3,52 USD de plus par millier de jetons de réflexion moyenne par appel d'Argon, 122,19 USD si Argon "
          "réfléchit à sa provision entière à chaque appel ; l'étape des juges n'est coupée par le plafond d'arrêt qu'au-delà "
          "de 32 476 jetons de moyenne, au-dessus de la provision mais sous la sortie maximale d'Argon (§ 4) ; aucun « haut » ; "
          "pire cas 150 ; parts au pire par clé : clé LUC 45 (plafond de la part Claude), clé de Google 198, clé d'OpenAI 48 ; "
          "§ 8 : comparaison aux bornes des v6 à v10 ;")
remplacer(27, "  - lanceur : `scripts/lancer_course_affinage_mentors_v11.py`",
          "`docs/notes/organisme-affinage-mentors-v1/course-v11/releve-prix-claude-gabarit-course-affinage-v11.json` ;",
          "  - lanceur : `scripts/lancer_course_affinage_mentors_v11c.py`, écrit à partir du lanceur v11b "
          "(`scripts/lancer_course_affinage_mentors_v11b.py`, `" + LANCEUR_V11B_SHA + "`, contre-lu par un Opus neuf, "
          "« Scellable après corrections » : `" + N + "/course-v11/contre-lecture-lanceur-v11b-v1.md`, `"
          + CONTRE_LECTURE_LANCEUR_V11B_SHA + "`), lui-même le lanceur v11 (`" + LANCEUR_V11_SHA + "`) au GO de la course "
          "près, écrit à partir du lanceur v10 (`scripts/lancer_course_affinage_mentors_v10.py`, `" + LANCEUR_V10_SHA + "`, "
          "branche de la v10), par un développeur qui n'est pas le rédacteur de ce texte (il épingle l'empreinte de ce "
          "préenregistrement : ce texte ne peut donc pas porter la sienne, qui est donnée par "
          "`course-v11/commandes-exactes-course-affinage-v11.md` et doit être citée par la contre-lecture ; EMPREINTE À "
          "INSCRIRE ici seulement si le lanceur v11c ne porte plus l'empreinte de ce texte dans son code : "
          "`scripts/lancer_course_affinage_mentors_v11c.py`) ; **commande de lancement** : " + COMMANDE_LANCEMENT + " ; ses "
          "essais : EMPREINTE À INSCRIRE : `tests/test_lancer_course_affinage_mentors_v11c.py` ; essais de la commande en flux "
          "v2 et de la sonde commune v3 : EMPREINTE À INSCRIRE : `tests/test_commande_gemini_flux_v2.py` et EMPREINTE À "
          "INSCRIRE : `tests/test_sonde_astra_courses_v3.py` ; gabarit de déclaration des relais : EMPREINTE À INSCRIRE : `"
          + N + "/course-v11/declaration-relais-gabarit-course-affinage-v11c.json` ; gabarits des relevés du jour : EMPREINTE "
          "À INSCRIRE : `" + N + "/course-v11/releve-credits-gabarit-course-affinage-v11.json` et EMPREINTE À INSCRIRE : `" + N
          + "/course-v11/releve-prix-claude-gabarit-course-affinage-v11.json` ;")

# ------------------------------------------------------------------------------------------------ espèces
sub(58, "Ce risque vaut pour Kimi (d'où son absence par défaut), mais aussi pour Astra et Carbon ;",
    "Ce risque vaut pour Kimi (d'où son absence par défaut), mais aussi pour Astra et Carbon, et (**v11**) pour Argon, "
    "proposeur et second juge, dont la sortie maximale en flux (45 056 jetons) n'a jamais été servie : un refus du "
    "fournisseur pour ce réglage ferait échouer chacun de ses appels, et A3 arrêterait ses deux rôles ;")
sub(59, "En v11, chaque appel de Carbon est **un appel en flux**, par la commande et le relais épinglés par le lanceur (le mandat "
        "de cette version les dit ceux de la passe X de la course « nouvelles attaques » ; empreintes aux pièces),",
    "En v11, chaque appel de Carbon est **un appel en flux**, par la commande en flux et le relais Gemini v3 épinglés par le "
    "lanceur (empreintes aux pièces ; le mandat de cette version les disait ceux de la passe X de la course « nouvelles "
    "attaques », qui n'avait pas de relais : la commande est neuve, le relais est celui de `main`),")
sub(59, " ; une limite de mots demandée par la consigne ne tient pas dans le plafond de texte. **Après la réponse**",
    ". Avant le départ, le lanceur refuse en outre un texte (sortie maximale moins provision) qui ne dépasse pas la limite de "
    "l'invite d'un proposeur (deux cartes de 9 000 caractères au plus, comptées à un jeton au plus par caractère). **Après la "
    "réponse**")
sub(59, "**Réglages exacts** (provision de réflexion, plafond de sortie, délais, bornes du relais) : RÉGLAGE À INSCRIRE, ceux "
        "du gabarit de déclaration v11, que le lanceur refuse de voir changés et écrit au manifeste de départ.",
    "**Réglages exacts** (ceux du gabarit de déclaration v11c, que le lanceur refuse de voir changés et écrit au manifeste de "
    "départ) : niveau de réflexion `high`, pensées demandées en retour ; provision de réflexion 28 672 jetons ; sortie "
    "maximale 65 536 jetons, la limite de Carbon en flux, soit 36 864 jetons de texte, au-dessus des 16 000 de la règle et des "
    "18 000 caractères de la limite de l'invite ; prix 4 et 20 USD par million de jetons ; délai de la génération 1 500 s, "
    "délai de la requête de compte de jetons 60 s ; relais Gemini v3 au port 8791, `--max-appels` ≥ 40 (un compte de jetons "
    "et une génération par appel : deux fois 16 cases plus 4 de marge), `--delai-silence-s` ≤ 240, `--delai-amont-s` ≥ 1 500, "
    "explicites, sans `--sans-pensees-amont`. Le lanceur garde trois contrôles des v8 et v9 qui valent encore en flux : "
    "provision d'au moins 25 870 jetons (1,25 fois la plus forte pensée observée, 20 696) ; sortie maximale d'au moins 24 500 "
    "jetons ; délai de la génération d'au moins 1 500 s.")
sub(59, "(a) le pire cas d'un appel, **tel que la commande épinglée le compte**, aux prix déclarés (4 et 20 USD par million de "
        "jetons, réflexion comprise dans la sortie : prix le plus haut de la page de prix versée, R-5018 ; 8,3 et 41,5, bornes "
        "hautes de R-3271, de la v5 à la v10 ; plus de facteur de lot), tient sous le plafond de session d'un proposeur "
        "(3,00 USD) sur l'entrée gardée la plus longue de la course (2 618 jetons, devis v10, § 1) : au plafond de sortie le "
        "plus haut que la garde admet, il vaut (2 618 × 4 + 65 536 × 20) / 10⁶ = 1,3212 USD si la commande compte la "
        "réflexion dans le plafond de sortie (lecture de la documentation du fournisseur et de la garde commune), et "
        "2,3042 USD si elle y ajoute la provision de réflexion de Carbon sous la même garde dans le collisionneur (49 152 "
        "jetons ; convention de la commande par lot des v8 à v10, qui tient dans les deux lectures) : devis v11, § 2 ;",
    "(a) le pire cas d'un appel, **tel que la commande épinglée le compte**, la réflexion comprise dans la sortie maximale, "
    "aux prix déclarés (4 et 20 USD par million de jetons, réflexion comprise dans la sortie : prix le plus haut de la page de "
    "prix versée, R-5018 ; 8,3 et 41,5, bornes hautes de R-3271, de la v5 à la v10 ; plus de facteur de lot), tient sous le "
    "plafond de session d'un proposeur (3,00 USD) sur l'entrée gardée la plus longue de la course (2 618 jetons, devis v10, "
    "§ 1) : (2 618 × 4 + 65 536 × 20) / 10⁶ = 1,321192 USD, soit **1,32 USD** (devis v11, § 2). La réflexion est comprise "
    "dans la sortie maximale : la page de Google versée et scellée sur `main` le dit (`fe0b8d88…`, l. 914-916, 1220-1222 et "
    "1273-1274 ; pièces), et la contre-lecture du lanceur v11b l'a établi sur elle ; **seule la facture d'une course réelle "
    "le confirmera**. Le pire cas de 2,3042 USD du brouillon 3 (une provision de 49 152 jetons ajoutée à la sortie maximale) "
    "est retiré ;")
sub(59, "(c) la durée maximale d'un appel, marge de 30 s comprise, reste sous le délai de l'adaptateur de commande de "
        "l'orchestrateur épinglé (1 800 s, écrit en dur) et sous A3 (1 800 s) ;",
    "(c) la durée maximale d'un appel (délai de la génération plus délai du compte de jetons, 1 500 + 60 s), marge de 30 s "
    "comprise, reste sous le délai de l'adaptateur de commande de l'orchestrateur épinglé (1 800 s, écrit en dur) et sous A3 "
    "(1 800 s) ;")
sub(59, "(d) le lanceur refuse le départ si la commande de Carbon n'est pas la commande épinglée, si l'un de ses arguments "
        "diffère de ceux du gabarit, ou si ses réglages ne passent pas la garde sur l'entrée la plus longue et sur la plus "
        "courte de la course.",
    "(d) le lanceur refuse le départ si la commande de Carbon n'est pas la commande épinglée, si l'un de ses arguments diffère "
    "de ceux du gabarit, si ses réglages ne passent pas la garde sur le corps exact que la commande bâtit pour l'entrée la "
    "plus longue de la course (capturé hors ligne, rien ne part), ou si son pire cas dépasse le plafond de session sur "
    "l'entrée la plus longue ou sur la plus courte.")
sub(59, "A3 (trois échecs consécutifs) peut alors arrêter Carbon et A14 marquer l'étape « non mesurée (technique) ».",
    "A3 (trois échecs consécutifs) peut alors arrêter Carbon et A14 marquer l'étape « non mesurée (technique) ». Si le "
    "service facturait la réflexion hors de la sortie maximale, contrairement à la page versée, rien dans l'appel ne la "
    "bornerait (le niveau `high` ne pose pas de budget) et un appel pourrait coûter plus que 1,32 USD : la commande "
    "compterait le coût lu tel quel et rendrait le code 7 au-delà du plafond de session ; la commande en flux v2 écrit après "
    "chaque réponse si texte et réflexion ont tenu ensemble dans la sortie maximale (`hypothese_sortie_maximale_tenue`) et "
    "le signale sinon (`HYPOTHESE_SORTIE_MAXIMALE_TOMBEE`).")
sub(60, "En v11, chaque appel d'Argon, de proposeur comme de juge, passe par une commande épinglée par le lanceur (empreinte "
        "aux pièces), qui emploie ou reproduit la garde commune (`garde_google_v3.py`), essais et mutations à l'appui.",
    "En v11, chaque appel d'Argon, de proposeur comme de juge, passe par la commande en flux épinglée par le lanceur, la même "
    "que pour Carbon (empreinte aux pièces), qui emploie la garde commune (`garde_google_v3.py`, chargée à son empreinte), "
    "essais et mutations à l'appui, et par un relais Gemini v3 en flux au port 8788.")
sub(60, " ; une limite de mots demandée par la consigne ne tient pas dans le plafond de texte. **Après la réponse**",
    ". Avant le départ, le lanceur refuse en outre un texte qui ne dépasse pas la limite de l'invite d'un proposeur (deux "
    "cartes de 9 000 caractères au plus, un jeton au plus par caractère). **Après la réponse**")
sub(60, "**Réglages retenus pour chiffrer** (ceux d'Argon sous la même garde dans le collisionneur ; devis v11, § 2) : niveau "
        "`high`, provision de réflexion 16 384 jetons, plafond de sortie 32 768 jetons, soit 16 384 jetons de texte, appel "
        "hors flux ; réglages exacts : RÉGLAGE À INSCRIRE, ceux du gabarit de déclaration v11, que le lanceur refuse de voir "
        "changés et écrit au manifeste de départ.",
    "**Réglages exacts** (ceux du code : arguments épinglés des lanceurs v11 à v11c et du gabarit de déclaration v11c, que le "
    "lanceur refuse de voir changés et écrit au manifeste de départ ; devis v11, § 2) : niveau `high`, pensées demandées en "
    "retour ; provision de réflexion **24 576** jetons, hypothèse du développeur (aucune réflexion d'Argon au niveau `high` "
    "n'est relevée dans les pièces lues) ; sortie maximale **45 056** jetons, soit 20 480 jetons de texte, au-dessus des "
    "16 000 de la règle et des 18 000 caractères de la limite de l'invite d'un proposeur ; **appel en flux**, la sortie "
    "maximale passant la limite d'Argon hors flux (32 768 ; 65 536 en flux) ; mêmes réglages pour le proposeur et le juge ; "
    "prix 4 et 20 USD par million de jetons ; délais de la génération et du compte de jetons 1 500 s et 60 s ; relais au port "
    "8788, `--max-appels` ≥ 2 × (16 + 32 × espèces actives), `--delai-silence-s` ≤ 240, `--delai-amont-s` ≥ 1 500, sans "
    "`--sans-pensees-amont`. Les réglages sur lesquels chiffrait le brouillon 3 (provision 16 384, sortie 32 768, hors flux) "
    "ne laissaient que 16 384 jetons de texte, sous la limite de l'invite : le lanceur les refuse (contre-lecture du lanceur "
    "v11b, constat 2). Argon n'a jamais été servi au-delà de 32 768 jetons de sortie dans les pièces lues (garde commune, "
    "sources des limites de sortie) : la limite de 65 536 en flux vient de la page de Google versée (l. 931).")
sub(60, "**Plafond de session des juges : 1,00 USD au lieu de 0,60** (configuration v11 ; R-5018). Raison : aux réglages "
        "ci-dessus et sur une entrée de juge de 3 855 jetons (consigne du juge, une carte de 9 000 caractères au plus, cadre ; "
        "devis v11, § 2), le pire cas d'un appel de juge d'Argon, aux prix déclarés (4 et 20 USD par million de jetons), "
        "vaut 0,9985 USD quand la provision s'ajoute au plafond de sortie (convention de la commande retirée, qui tient dans "
        "les deux lectures) et 0,6708 USD quand la réflexion y est comptée : les deux dépassent 0,60 USD, et 1,00 USD est la "
        "plus petite valeur au dixième qui tient dans les deux cas. **Marge étroite dans le premier cas** : 1,00 USD laisse "
        "alors passer une entrée de juge de 4 240 jetons au plus, 385 de plus que l'entrée attendue, dont le cadre est "
        "supposé ; au-delà, la commande refuse l'appel avant l'envoi (échec du juge, compté pour A3 et A14) ; le lanceur "
        "contrôle ce pire cas avant le départ, sur la plus longue entrée de juge admise (liste d'arrêt).",
    "**Plafond de session des juges : 1,00 USD au lieu de 0,60** (configuration v11c, champ "
    "`argon_v11.plafond_session_juge_usd`, que le lanceur exige égal à 1,00 ; R-5018). Raison : la commande compte la "
    "réflexion dans la sortie maximale (page de Google versée, l. 914-916, 1220-1222 et 1273-1274), et le pire cas d'un "
    "appel de juge d'Argon, aux prix déclarés, vaut l'entrée gardée plus 45 056 × 20 / 10⁶ = 0,90112 USD : **0,917240 USD** "
    "sur l'entrée de juge que contrôle le lanceur v11b (11 514 caractères : consigne du juge, une carte de 9 000 caractères "
    "au plus, cadre de 1 000 caractères supposé ; 4 030 jetons gardés) et 0,917356 USD sur celle du brouillon du lanceur "
    "v11c (11 596 caractères, de la forme que bâtit l'orchestrateur ; 4 059 jetons) ; plafond minimal au centime 0,92 USD, "
    "au dixième 1,00 USD. 1,00 USD couvre une entrée de juge de 24 720 jetons, plus de 20 000 au-delà de ces entrées "
    "(devis v11, § 2) : la marge étroite du brouillon 3 (385 jetons) n'a plus d'objet. Une entrée plus longue ferait refuser "
    "l'appel avant l'envoi (échec du juge, compté pour A3 et A14) ; le lanceur contrôle ce pire cas avant le départ, sur la "
    "plus longue entrée de juge qu'il bâtit (liste d'arrêt).")
sub(60, "couvre le pire cas d'un appel de proposeur d'Argon aux mêmes réglages (0,9935 USD).",
    "couvre le pire cas d'un appel de proposeur d'Argon aux mêmes réglages (0,911592 USD sur l'entrée la plus longue).")
sub(60, "et son effet sur la dépense est au § Plafond ;",
    "et son effet sur la dépense est au § Plafond : aux réglages du lanceur, une réflexion moyenne au-delà de 32 476 jetons "
    "par appel, au-dessus de la provision mais sous la sortie maximale, ferait couper l'étape des juges par le plafond "
    "d'arrêt ;")
sub(60, "A3 peut alors arrêter ce juge et A14 marquer l'étape des juges « non mesurée (technique) ».",
    "A3 peut alors arrêter ce juge et A14 marquer l'étape des juges « non mesurée (technique) ». Si le service facturait la "
    "réflexion hors de la sortie maximale, un appel de juge pourrait coûter plus que son pire cas (repère : 1,4088 USD si la "
    "seule provision s'y ajoutait) ; le coût lu serait compté tel quel et la commande rendrait le code 7 au-delà du plafond "
    "de session.")

sub(59, "garde commune `garde_google_v3.py`, employée ou reproduite par la commande, essais et mutations à l'appui)",
    "garde commune `garde_google_v3.py`, employée par la commande, qui la charge à son empreinte, essais et mutations à "
    "l'appui)")
sub(59, "commande épinglée inchangée, arguments exacts du gabarit de déclaration v11 (modèle, prix, sortie maximale, délai)",
    "commande épinglée inchangée, arguments exacts du gabarit de déclaration v11c (modèle, prix, sortie maximale, délai)")
sub(60, "estimé à 0,037 USD par appel, très en dessous des deux valeurs.",
    "estimé à 0,037 USD par appel, très en dessous de ce plafond.")

# ------------------------------------------------------------------------------------------------ sorties, mesure, bonne fin
sub(76, "acte de gel, configuration assemblée, manifestes de départ et de fin du lanceur (scellés), alertes éventuelles.",
    "acte de gel, configuration assemblée, manifestes de départ et de fin du lanceur (scellés), journal de la part Claude au "
    "fil de l'eau (`journal-part-claude-au-fil-de-l-eau.jsonl`, **v11**, scellé à la fin), alertes éventuelles.")
sub(80, "(**v11** : la part Claude est en outre relevée au fil de l'eau sur l'état de son relais)",
    "(**v11** : la part Claude est en outre relevée au fil de l'eau sur l'état et le journal de son relais, chaque lecture "
    "écrite au journal du run ; compte des appels du relais Claude par statut, réserve par appel et dépassement lus, au "
    "manifeste de fin)")
sub(80, "**v11** : devis v11, Argon et Carbon aux prix déclarés",
    "**v11** : devis v11 (v11c ; estimation inchangée depuis le v11), Argon et Carbon aux prix déclarés")
sub(85, "**v11** : un arrêt par la garde de la part Claude (premier refus du relais Claude à son plafond de 45 USD, ou premier "
        "refus de l'interface d'Anthropic relayé par lui ; code 5 du lanceur ; § Règle des clés) est possible aussi",
    "**v11** : un arrêt par la garde de la part Claude (premier déclencheur lu au journal ou dans l'état du relais Claude — "
    "refus de l'interface d'Anthropic relayé par lui, refus propre au relais, à son plafond de 45 USD ou pour une autre "
    "cause, part engagée au plafond, état ou journal illisible trois fois de suite ; code 5 du lanceur ; § Règle des clés) "
    "est possible aussi")

# ------------------------------------------------------------------------------------------------ liste d'arrêt
sub(89, "ligne de GO absente, hors période, révoquée, d'un autre périmètre ou d'un plafond autre que 150 USD, ou registre "
        "dérivé (ligne du GO et révocations qui la visent, écrit et scellé par le lanceur, passé à l'orchestrateur) refusé "
        "par la lecture de l'orchestrateur ;",
    "ligne du GO de la course (**v11** : GO-2026-11-22-80, prolongation de GO-2026-11-18-14, passée à l'orchestrateur comme "
    "`GO_ID` ; GO-2026-11-18-14 en v1 à v10) absente, hors période, révoquée, accordée par un autre que Lazar, qui ne dit pas "
    "prolonger GO-2026-11-18-14, d'un autre périmètre ou d'un plafond autre que 150 USD ; **v11** : ligne de "
    "GO-2026-11-18-14 absente, d'un autre type que « calcul », accordée par un autre que Lazar ou révoquée ; GO de la course "
    "nommé par la configuration (`changements_v11.go_course`) autre que GO-2026-11-22-80 ; registre dérivé (lignes de "
    "GO-2026-11-22-80 et de GO-2026-11-18-14 et révocations qui les visent, écrit et scellé par le lanceur, passé à "
    "l'orchestrateur) refusé par la lecture de l'orchestrateur ;")
sub(89, "ou ligne GO-2026-11-22-124 (qui la précise) absente ou révoquée ; date du jour hors de la période de ces lignes, "
        "prolongations comprises (§ Règle des clés, « Période ») ; après le 2026-11-25, ligne de prolongation absente, ou "
        "confirmation par Lazar de la prolongation de l'exception non inscrite au registre ou non nommée au lanceur ;",
    "ou ligne GO-2026-11-22-124 (qui la précise) absente, révoquée, ou dont le plafond ne dit pas « part Claude 45 USD » ; "
    "date du jour hors de la période de ces lignes, prolongations comprises (§ Règle des clés, « Période ») ; après le "
    "2026-11-25, confirmation par Lazar de la prolongation de l'exception non inscrite au registre ou non nommée dans la "
    "configuration ;")
sub(89, "**v11, commande de Carbon en flux** (les gardes v8 et v9 de la commande par lot sont retirées avec elle) : appel qui "
        "ne serait pas en flux ; réglage de réflexion absent du corps ou autre que le niveau le plus haut admis ; pensées non "
        "demandées en retour ; plafond de sortie sous la provision de réflexion plus 16 000 jetons de texte, ou au-delà de la "
        "limite de Carbon en flux ; limite de mots de la consigne qui ne tient pas dans le plafond de texte (garde gelée des "
        "appels aux modèles de Google, contrôlée sur l'entrée la plus longue et sur la plus courte de la course) ; durée "
        "maximale de la commande plus 30 s au-delà de 1 800 s (adaptateur de l'orchestrateur, A3) ; pire cas d'un appel "
        "au-dessus du plafond de session (3,00 USD) ;",
    "**v11, commande de Carbon en flux** (les gardes propres au lot sont retirées avec lui ; restent, des v8 et v9, une "
    "provision d'au moins 25 870 jetons, une sortie maximale d'au moins 24 500 et un délai de la génération d'au moins "
    "1 500 s) : appel qui ne serait pas en flux ; réglage de réflexion absent du corps ou autre que le niveau le plus haut "
    "admis ; pensées non demandées en retour ; plafond de sortie sous la provision de réflexion plus 16 000 jetons de texte, "
    "ou au-delà de la limite de Carbon en flux (garde gelée des appels aux modèles de Google, sur le corps exact que la "
    "commande bâtit pour l'entrée la plus longue de la course, capturé hors ligne) ; texte (sortie maximale moins provision) "
    "qui ne dépasse pas la limite de l'invite d'un proposeur (deux cartes de 9 000 caractères, un jeton au plus par "
    "caractère) ; option de réglage absente ou donnée deux fois ; durée maximale de la commande (délai de la génération plus "
    "délai du compte de jetons) plus 30 s au-delà de 1 800 s (adaptateur de l'orchestrateur, A3) ; pire cas d'un appel "
    "au-dessus du plafond de session (3,00 USD), sur l'entrée la plus longue ou la plus courte de la course ;")
sub(89, "**v11, commande d'Argon** : commande autre que la commande épinglée sous la garde, ou d'autres arguments que ceux du "
        "gabarit ; niveau de réflexion absent du corps, autre que le plus haut admis, ou accompagné d'un budget ; pensées non "
        "demandées en retour ; plafond de sortie sous la provision de réflexion plus 16 000 jetons de texte, ou au-delà de la "
        "limite d'Argon dans le mode de l'appel ; limite de mots de la consigne qui ne tient pas dans le plafond de texte "
        "(même garde gelée, contrôlée sur l'entrée de proposeur la plus longue et la plus courte de la course, et sur une "
        "entrée de juge) ; pire cas d'un appel de proposeur d'Argon au-dessus de 3,00 USD, ou d'un appel de juge d'Argon "
        "au-dessus de 1,00 USD sur la plus longue entrée de juge admise (consigne du juge, carte de 9 000 caractères, cadre "
        "réel) ; plafond de session des juges de la configuration autre que 1,00 USD ;",
    "**v11, commande d'Argon** : commande autre que la commande en flux épinglée sous la garde (l'enveloppe d'Argon des v6 à "
    "v10 et sa commande sont refusées), ou d'autres arguments que ceux du gabarit ; niveau de réflexion absent du corps, autre "
    "que le plus haut admis, ou accompagné d'un budget ; pensées non demandées en retour ; plafond de sortie sous la "
    "provision de réflexion plus 16 000 jetons de texte, ou au-delà de la limite d'Argon dans le mode de l'appel (même garde "
    "gelée, sur le corps exact que la commande bâtit pour la plus longue entrée de chaque rôle : proposeur, et juge dans la "
    "forme que bâtit l'orchestrateur épinglé) ; texte qui ne dépasse pas la limite de l'invite d'un proposeur ; pire cas d'un "
    "appel de proposeur d'Argon au-dessus de 3,00 USD, ou d'un appel de juge d'Argon au-dessus de 1,00 USD sur la plus longue "
    "entrée de juge que bâtit le lanceur (consigne du juge, carte de 9 000 caractères, cadre de 1 000 caractères supposé) ; "
    "plafond de session des juges de la configuration (`argon_v11.plafond_session_juge_usd`) absent ou autre que 1,00 USD ;")
sub(89, "Claude, plafond égal, au centime, au plafond de la part Claude, 45,00 USD, et journal du relais nommé à ses arguments "
        "et lisible par le lanceur (**v11** ; plafond de 150 en v7 à v10) ;",
    "Claude, plafond égal, au centime, au plafond de la part Claude, 45,00 USD, journal du relais nommé à ses arguments par un "
    "chemin absolu, et réserve par appel lue dans son état (égale à celle de ses arguments s'ils la donnent), de 0 au "
    "plafond exclu (**v11** ; plafond de 150 en v7 à v10) ;")
sub(89, "Argon, `--max-appels` ≥ 2 × (16 + 32 × espèces actives) ;",
    "Argon, `--max-appels` ≥ 2 × (16 + 32 × espèces actives) (**v11** : relais Gemini v3 en flux au port 8788, "
    "`--delai-silence-s` ≤ 240, `--delai-amont-s` ≥ 1 500, explicites, sans `--sans-pensees-amont`) ;")
sub(89, "Carbon (**v11**, relais de l'appel en flux ; les bornes de lots et de relevés du relais Gemini v4 sont retirées avec "
        "lui), bornes d'appels au moins égales à 16 cases plus 4 de marge, comptes de jetons compris s'il en fait (RÉGLAGE À "
        "INSCRIRE : bornes exactes du relais de Carbon, celles du lanceur v11) ;",
    "Carbon (**v11**, relais Gemini v3 en flux au port 8791 ; les bornes de lots et de relevés du relais Gemini v4 sont "
    "retirées avec lui), `--max-appels` ≥ 40 (un compte de jetons et une génération par appel : deux fois 16 cases plus 4 de "
    "marge), `--delai-silence-s` ≤ 240, `--delai-amont-s` ≥ 1 500, explicites, sans `--sans-pensees-amont` ;")
sub(89, "pour Carbon sans les compteurs de son relais) refusé",
    "pour les relais Gemini v3 d'Argon et de Carbon, « appels » seul) refusé")
sub(89, "**v11** : sonde faite avec un autre modèle que `gpt-6.2-astra`, une autre variable de clé ou d'autres prix que ceux "
        "de cette version ;",
    "**v11** : sonde faite avec un autre modèle que `gpt-6.2-astra`, une autre variable de clé ou d'autres prix que ceux de "
    "cette version ; rapport de la sonde commune d'une autre version que `sonde_astra_courses_v3`, ou qui ne porte pas la "
    "variable de clé du relais jeté lue par son PID (`OPENAI_API_KEY_2`, une seule fois) ;")
sub(89, "ne dit pas son modèle sous le libellé exigé (**v11** : un Opus neuf ; modèle K en v2 à v10),",
    "ne porte pas le libellé exigé (**v11** : « Opus 5.5, contre-lecteur neuf » ; « modèle K » en v2 à v10),")
sub(89, "**v11, clé LUC** : entrée de la clé LUC absente du relevé des crédits, ou qui ne dit pas « solde non lu » avec la "
        "référence GO-2026-11-22-124, ou qui porte un solde (aucun solde,",
    "**v11, clé LUC** : entrée de la clé LUC absente du relevé des crédits ou qui n'est pas un objet, qui ne porte pas "
    "`solde_non_lu` vrai et `reference` égale à GO-2026-11-22-124, ou qui porte un montant (solde, crédit, reste, couverture, "
    "réserve, recharge, plancher) ou un champ hors de `solde_non_lu`, `reference`, `source` et `note` (aucun solde,")
sub(91, "la contre-lecture de ce texte et celle du lanceur v11 (le lanceur vérifie la première, § Contre-lecture) ;",
    "la contre-lecture de ce texte et celle du lanceur v11c (le lanceur vérifie la première, § Contre-lecture) ;")
sub(91, "**un essai à blanc** du lanceur v11, sans appel à un fournisseur, joué jusqu'au manifeste de fin sur la configuration "
        "v11 et versé au dépôt avant le départ réel.",
    "**un essai à blanc** du lanceur v11c, sans appel à un fournisseur, joué jusqu'au manifeste de fin sur la configuration "
    "v11c et versé au dépôt avant le départ réel ; un dépôt de travail qui porte la garde commune de `main` à son empreinte "
    "(le lanceur refuse sinon : pièce d'une autre empreinte).")
remplacer(95, "- **Pendant, en plus (v11) — garde de la part Claude** :", "R5.",
          "- **Pendant, en plus (v11) — garde de la part Claude** : le lanceur relève l'état et le journal du relais Claude au "
          "moins une fois par minute (toutes les 10 s dans le lanceur v11c ; compte de la part Claude au fil de l'eau, chaque "
          "lecture écrite au journal du run `journal-part-claude-au-fil-de-l-eau.jsonl`, scellé à la fin) ; il arrête la "
          "course au **premier** des déclencheurs suivants (décision du 23 novembre ; contre-lecture du lanceur v11b, "
          "constat 7) : (a) une ligne du journal du relais de statut 400 à 499, hors 429 — soit un appel que l'interface "
          "d'Anthropic refuse et que le relais relaie (forme relevée du manque de crédit : 400 « credit balance is too low », "
          "R-4833 et R-4842), soit un refus propre au relais, dont la ligne porte un motif : 401 (jeton local), 402 (plafond "
          "de 45 USD atteint), 403 (modèle non permis), 404 (chemin), 413 (corps trop grand) ; (b) un refus compté dans l'état "
          "du relais (`refus` au-dessus de zéro) dont la ligne n'est pas encore lue ; (c) une part engagée (dépense plus "
          "montants réservés des appels en vol) qui atteint 45 USD ; (d) un état ou un journal du relais illisible trois fois "
          "de suite (une lecture manquée isolée est comptée, jamais tue). Alors : signal d'arrêt à l'orchestrateur par son "
          "PID, arrêt propre, manifestes écrits, **code 5** ; ce qui a été fait est écrit, et une alerte scellée pour la mère "
          "(`alerte-arret-part-claude.json`), qui prévient Lazar ; **l'alerte nomme la nature du déclencheur, le statut et la "
          "cause** : pour un refus propre au relais, la cause est le motif écrit à son journal ; pour un refus relayé de "
          "l'interface, la cause est dite « inconnue », le journal du relais ne gardant que le statut (un 400 peut être un "
          "crédit insuffisant ou une requête refusée) ; détail au § Règle des clés, « Clé LUC ». Si l'orchestrateur s'arrête de "
          "lui-même, le lanceur relit une dernière fois l'état et le journal (relecture finale) : un déclencheur lu alors vaut "
          "le code 5 et l'alerte. Cette garde est essayée sur un cas sain (aucun refus : la course va à son terme) et sur des "
          "artefacts (un refus du relais, puis un refus de l'interface, plantés dans l'état et le journal d'un relais factice : "
          "arrêt, code 5, alerte ; un refus écrit après la dernière lecture, l'orchestrateur sortant aussitôt : code 5 par la "
          "relecture finale, non 6), R5.")

# ------------------------------------------------------------------------------------------------ plafond
sub(101, "**v11** : devis v11 (écrit pour cette version sur les décisions de la mère, R-5007, point (d), et R-5018 ; à "
         "contre-lire).",
    "**v11** : devis v11 (v11c, écrit pour cette version sur les décisions de la mère, R-5007, point (d), et R-5018, et sur "
    "celles de la session de l'organisme du 23 novembre ; à contre-lire).")
sub(101, " ; à sa provision entière (16 384 jetons à chaque appel), le sous-total est 93,36 USD, 102,69 avec la marge ; le cumul "
         "n'atteint 150 USD qu'au-delà de 32 476 jetons de moyenne (31 462 avec la marge sur les autres postes), presque le "
         "plafond de sortie d'Argon lui-même : aux prix déclarés, la réflexion d'Argon n'a pas de prise réaliste sur le "
         "plafond d'arrêt (aux bornes des v6 à v10, ce seuil était à 13 812 jetons : devis v11, § 8).",
    " ; à sa provision entière (**24 576** jetons à chaque appel, réglage du lanceur), le sous-total est **122,19** USD, "
    "134,41 avec la marge, et rien n'est coupé ; le cumul n'atteint 150 USD qu'au-delà de **32 476** jetons de moyenne "
    "(31 462 avec la marge sur les autres postes). **Aux réglages du lanceur, ce seuil est atteignable** : il est au-dessus de "
    "la provision (de 7 900 jetons) mais sous la sortie maximale d'Argon (45 056 jetons, de 12 580), qui borne la réflexion "
    "d'un appel avec son texte ; au-delà, le plafond d'arrêt coupe l'étape des juges (« non mesuré (budget) », nœud, code 6 ; "
    "plafonds des étapes, plus bas), sans aucun dollar au-delà de 150 si la réflexion est comprise dans la sortie maximale. "
    "La réflexion d'Argon a donc prise sur le plafond d'arrêt ; ce texte n'en chiffre pas la probabilité, aucune réflexion "
    "d'Argon au niveau `high` sur ces consignes n'étant mesurée (la mesure préalable que Lazar a accordée, GO-2026-11-22-128, "
    "au plus 10,50 USD hors du plafond de la course, et que R-5018 disait sans objet sur l'ancien réglage, n'est pas "
    "exécutée ; devis v11, § 4) (le brouillon 3 disait, sur une sortie maximale de 32 768 "
    "jetons presque égale au seuil, qu'elle n'avait pas de prise réaliste ; aux bornes des v6 à v10, ce seuil était à 13 812 "
    "jetons : devis v11, § 8).")
sub(101, "un prix réel au-dessus du prix déclaré ferait sous-compter la dépense, ce que les bornes des v6 à v10 excluaient : la "
         "page est relue le jour du départ (liste d'arrêt).",
    "un prix réel au-dessus du prix déclaré ferait sous-compter la dépense, ce que les bornes des v6 à v10 excluaient : la "
    "page est relue le jour du départ (liste d'arrêt). De même, la dépense comptée sur la clé de Google suppose la réflexion "
    "comprise dans la sortie maximale (page de Google versée, pièces) : seule la facture d'une course réelle le confirmera.")
sub(110, "**v11** : aucun seuil n'est changé (mêmes budgets d'étapes dans la configuration v11) ;",
    "**v11** : aucun seuil n'est changé (mêmes budgets d'étapes dans la configuration v11c) ;")
sub(110, ": à la provision entière d'Argon à chaque appel, rien n'est coupé (devis v11, § 4).",
    ": à la provision entière d'Argon à chaque appel (24 576 jetons), rien n'est coupé (cumul avant les juges 34,95 USD, "
    "plafond dur des juges 115,05 USD, étape des juges 87,24 USD) ; au-delà de 32 476 jetons de moyenne, l'étape des juges "
    "est coupée (devis v11, § 4).")
sub(112, "Quand il est atteint, ou quand l'interface d'Anthropic refuse un appel avant qu'il le soit, le lanceur arrête la "
         "course (code 5, alerte) :",
    "Quand il est atteint, au premier refus lu au journal ou dans l'état du relais Claude, ou si l'état ou le journal du relais "
    "est illisible trois fois de suite (§ Règle des clés, « Clé LUC », point 5), le lanceur arrête la course (code 5, alerte) :")

# ------------------------------------------------------------------------------------------------ règle des clés
remplacer(127, "**Période (v11).**", "Après le 2026-12-15 : pas de départ.",
          "**Période (v11).** La ligne GO-2026-11-18-14 porte l'échéance 2026-11-25 ; GO-2026-11-22-80 la prolonge au "
          "2026-12-15, mêmes périmètre, conditions et plafond (« 150 USD (plafond de GO-2026-11-18-14) »). La lecture du GO par "
          "l'orchestrateur épinglé (`configuration_v55.verifier_go_v55`) ne voit que la période de la ligne qu'on lui passe "
          "comme `GO_ID` : avec GO-2026-11-18-14, elle refuserait tout départ après le 25 novembre. **Le GO de la course est "
          "donc GO-2026-11-22-80** (décision de la mère sur le point ouvert 11 du rapport du développeur du lanceur v11), passé "
          "à l'orchestrateur et cité par la commande de lancement : " + COMMANDE_LANCEMENT + ". La ligne de l'exception "
          "GO-2026-11-22-107 porte l'échéance 2026-11-25 ; GO-2026-11-22-124 la porte au 2026-12-15 « avec la course », sur une "
          "lecture de la mère (le mot de Lazar « ho » lu « ok ») que la ligne dit elle-même **à confirmer par Lazar**. Le "
          "lanceur lit ces lignes dans le registre de `main` : GO-2026-11-22-80 (accordée par Lazar, de type « calcul », en "
          "période, non révoquée, qui dit prolonger GO-2026-11-18-14 ; plafond lu à 150 USD) ; GO-2026-11-18-14 (une ligne, "
          "« calcul », accordée par Lazar, non révoquée ; sa propre échéance ne borne plus la course) ; GO-2026-11-22-124 "
          "(accordée par Lazar, en période, non révoquée, qui nomme GO-2026-11-22-107 et dont le plafond dit « part Claude "
          "45 USD ») ; GO-2026-11-22-107 (« calcul », accordée par Lazar, en période, non révoquée, qui nomme la clé LUC, la "
          "règle GO-2026-11-22-70 et la course) ; la configuration doit nommer le même GO de la course "
          "(`changements_v11.go_course`). Le registre dérivé qu'il passe à l'orchestrateur garde les lignes de "
          "GO-2026-11-22-80 et de GO-2026-11-18-14 et les révocations qui visent l'une ou l'autre ; l'orchestrateur y lit "
          "GO-2026-11-22-80 (essai du lanceur v11b sur sa vraie fonction : accepté au 26 novembre, refusé au 16 décembre). "
          "**Jusqu'au 2026-11-25 inclus**, le départ ne dépend d'aucune confirmation. **Du 2026-11-26 au 2026-12-15**, "
          "l'exception GO-2026-11-22-107 ne vaut que prolongée, et sa prolongation ne vaut que confirmée : le lanceur exige "
          "alors la ligne du registre où la mère a inscrit la confirmation de Lazar (accordée par Lazar, non révoquée, en "
          "période, qui nomme GO-2026-11-22-107), **nommée dans la configuration** "
          "(`changements_v11.confirmation_prolongation_go_107`, vide aujourd'hui : la nommer change l'empreinte de la "
          "configuration, donc demande une configuration et un lanceur neufs, R12) ; nommée mais absente ou non valide au "
          "registre : refus ; non nommée : pas de départ après le 25 novembre (code 2). Après le 2026-12-15 : pas de départ.")
sub(135, "Noms des champs : ceux du gabarit du relevé des crédits v11.",
    "**Le lanceur exige cette entrée** et refuse le départ (code 2) si elle est absente ou n'est pas un objet, si elle ne "
    "porte pas `solde_non_lu` vrai et `reference` égale à GO-2026-11-22-124, si l'un de ses champs porte un montant (solde, "
    "crédit, reste, couverture, réserve, recharge, plancher, montant en USD ou en euros), ou si elle porte un champ hors de "
    "`solde_non_lu`, `reference`, `source` et `note` (lanceur v11c ; contre-lecture du lanceur v11b, constat 3). Noms des "
    "champs : `solde_non_lu` (vrai) et `reference` (GO-2026-11-22-124), seuls exigés ; `source` et `note`, permis.")
sub(136, "— lecture à confirmer sur l'orchestrateur épinglé par l'essai du lanceur.",
    "— lu sur l'orchestrateur épinglé et essayé sur sa vraie classe de suivi des rôles par le développeur du lanceur v11 "
    "(rapport, § 2.6 : trois refus de suite arrêtent le rôle) ; que l'adaptateur Claude rende un échec sur un refus du relais "
    "est lu, non joué.")
sub(138, "et écrit chaque lecture dans un journal du run (montants, comptes et statuts, jamais un contenu).",
    "et écrit chaque lecture dans un journal du run (montants, comptes et statuts, jamais un contenu ; **v11c** : toutes les "
    "10 s, `journal-part-claude-au-fil-de-l-eau.jsonl`, dans le dossier du run, scellé à la fin ; une lecture illisible y est "
    "écrite aussi).")
sub(138, "Le relais refuse un appel dès que la part engagée, plus la réserve de cet appel (0,40 USD, défaut du programme "
         "épinglé), dépasserait 45 USD : au-delà de 44,60 USD de part engagée.",
    "Le relais refuse un appel dès que la part engagée, plus la réserve de cet appel (0,40 USD, défaut du programme épinglé), "
    "dépasserait 45 USD : au-delà de 44,60 USD de part engagée. La réserve par appel est lue au départ dans l'état du relais "
    "(et dans ses arguments lus par PID, s'ils la donnent) et écrite au manifeste de départ, avec le dépassement possible par "
    "appel en vol (2,60 USD pour un appel de proposeur, à 0,40 USD de réserve).")
remplacer(139, "5. **Arrêt et message, au premier refus.**", "une relance demande une version suivante et une décision nommée.",
          "5. **Arrêt et message, au premier déclencheur.** Quatre déclencheurs valent arrêt (lanceur v11c ; contre-lecture du "
          "lanceur v11b, constat 7 ; décision du 23 novembre) : (a) une ligne du journal du relais Claude de statut 400 à 499, "
          "hors 429 : soit le **refus de l'interface d'Anthropic**, que le relais épinglé relaie tel quel et dont son journal "
          "ne garde que le statut — la forme relevée du manque de crédit est un statut 400, « credit balance is too low » "
          "(R-4833, R-4842) ; le journal ne gardant pas le message, un statut 400 d'une autre cause (requête refusée) arrête la "
          "course de la même façon —, soit un **refus propre au relais**, que sa ligne signale par un motif : 402 quand son "
          "plafond de 45 USD est atteint, 401 (jeton local), 403 (modèle non permis), 404 (chemin inconnu), 413 (corps trop "
          "grand) ; (b) un **refus compté dans l'état** du relais (`refus` au-dessus de zéro) avant que sa ligne soit lue ; "
          "(c) la **part engagée au plafond** : dépense et montants réservés des appels en vol atteignant 45 USD, avant même le "
          "refus du relais ; (d) un état ou un journal du relais **illisible trois fois de suite** : la part Claude n'est plus "
          "comptable. Les statuts 429 et 500 à 599 et les pannes de transport ne sont pas des déclencheurs : ce sont des échecs "
          "d'appel, laissés aux règles de l'orchestrateur (A3, A14). Au premier déclencheur, le lanceur arrête la course : "
          "signal d'arrêt à l'orchestrateur par son PID, arrêt propre, manifestes écrits, **code 5** ; il écrit et scelle une "
          "alerte pour la mère (`alerte-arret-part-claude.json` : nature du déclencheur, statut, cause, moment, plafond, part "
          "engagée lue, compte des appels par statut, dernier état lu, ce qui a été fait), qui prévient Lazar. **La cause est "
          "celle que le lanceur peut lire** : le motif écrit par le relais pour un refus propre au relais ; « inconnue » pour un "
          "refus relayé de l'interface, dont le relais ne garde que le statut ; le nombre de refus comptés pour un refus de "
          "l'état dont la ligne n'est pas lue ; l'erreur de lecture pour un état illisible. Si l'orchestrateur s'arrête de "
          "lui-même avant que le lanceur ait lu un déclencheur (A3 : trois appels refusés de suite arrêtent le rôle), le "
          "lanceur relit l'état et le journal du relais après son arrêt (relecture finale, refaite jusqu'à trois fois si elle "
          "est illisible) : un déclencheur lu alors vaut le code 5 et l'alerte, par la priorité des codes (4, puis 5, puis 6). "
          "Le lanceur ne relance rien, et aucun repli n'est fait (autre clé, autre modèle, abonnement) ; les cartes déjà "
          "produites sont rapportées ; la bonne fin n'est pas atteinte. C'est une cause technique déclarée (crédit, plafond, "
          "refus du relais ou part non comptable) au sens de la règle « une panne technique n'est pas un résultat » "
          "(GO-2026-11-22-77) : l'essai se rapporte tel quel, avec son issue codée, et une relance demande une version suivante "
          "et une décision nommée.")
sub(140, "(i) Un refus qui n'arrive pas sous un statut 400 à 499 :",
    "(i) Un refus qui n'arrive ni sous un statut 400 à 499 ni au compteur de refus de l'état :")
sub(140, "sa dépense peut dépasser 45 USD d'au plus (coût d'un appel − réserve) par appel en vol quand le plafond est atteint ; "
         "le dépassement lu dans son état est écrit au manifeste de fin.",
    "sa dépense peut dépasser 45 USD d'au plus (coût d'un appel − réserve) par appel en vol quand le plafond est atteint "
    "(2,60 USD pour un appel de proposeur) ; le lanceur arrête la course dès que la part engagée atteint 45 USD (point 5, "
    "déclencheur (c)) ; le dépassement lu dans son état est écrit au manifeste de fin.")
sub(146, "elle part sans lecture de solde, sur le mot de Lazar (GO-2026-11-22-124), et le relevé l'écrit « solde non lu » avec "
         "cette référence (paragraphe « Clé LUC »).",
    "elle part sans lecture de solde, sur le mot de Lazar (GO-2026-11-22-124), et le relevé l'écrit `solde_non_lu` vrai avec "
    "`reference` GO-2026-11-22-124, sans aucun montant (paragraphe « Clé LUC », point 1).")

# ------------------------------------------------------------------------------------------------ contre-lecture
remplacer(167, "À faire avant tout lancement, par un contre-lecteur neuf d'un autre modèle que le rédacteur",
          "L'acte de gel écrit par le lanceur au lancement (empreintes du préenregistrement et de la contre-lecture, verdict "
          "lu) est la spécification servie à l'orchestrateur.",
          "À faire avant tout lancement, par un contre-lecteur neuf — **v11** : un Opus 5.5 neuf, puis la vérification des "
          "corrections par le même contre-lecteur (pièce de classe A ; règles « Qui conçoit » et « Allègement de la "
          "procédure » de `CLAUDE.md` sur `main`) ; le rédacteur du brouillon 4 étant lui aussi Opus 5.5, le contre-lecteur "
          "n'est pas d'un autre modèle que lui (écart à la règle « Qui conçoit » déclaré par GO-2026-11-22-145) ; R2 tient : il "
          "est neuf et n'a écrit ni ce préenregistrement ni le lanceur. Son rapport est écrit et scellé à "
          "`docs/notes/organisme-affinage-mentors-v1/course-v11/contre-lecture-preenregistrement-course-affinage-mentors-v11.md` "
          "; il cite en entier l'empreinte de ce préenregistrement et celle du lanceur v11c, **porte le libellé « Opus 5.5, "
          "contre-lecteur neuf »**, que le lanceur v11c exige (« modèle K », « Opus 5.5 » seul ou « contre-lecteur neuf » seul "
          "sont refusés), et porte une section « Verdict » dont la **première ligne est exactement** « Scellable. » (en gras ou "
          "non) ; tout autre verdict, un rapport sans ce libellé, ou un rapport qui dit n'avoir pas relu (« je n'ai pas relu », "
          "« non relu », « sans relecture »…), est refusé par le lanceur. Une correction demandée donne une nouvelle version de "
          "ce préenregistrement et du lanceur (R12). L'acte de gel écrit par le lanceur au lancement (empreintes du "
          "préenregistrement et de la contre-lecture, verdict lu) est la spécification servie à l'orchestrateur.")

# ------------------------------------------------------------------------------------------------ différentiel v10 → v11
sub(279, "et mots de Lazar (GO-2026-11-22-124) : les trois changements du mandat, trois décisions qui en découlent, et leurs "
         "conséquences mécaniques.",
    "et mots de Lazar (GO-2026-11-22-124) ; au brouillon 4, décisions de la session de l'organisme du 23 novembre (réglages et "
    "lectures du lanceur v11c) : les trois changements du mandat, trois décisions qui en découlent, et leurs conséquences "
    "mécaniques.")
sub(284, "arrêt de la course au premier refus — du relais à son plafond (statut 402), ou de l'interface d'Anthropic relayé par "
         "lui (statut 400 à 499, hors 429) — (code 5) et alerte scellée pour la mère, qui prévient Lazar ;",
    "arrêt de la course au premier déclencheur — refus de l'interface d'Anthropic relayé par le relais (statut 400 à 499, hors "
    "429), refus propre au relais (401, 402 à son plafond, 403, 404, 413), refus compté dans son état, part engagée au "
    "plafond, état ou journal illisible trois fois de suite — (code 5), relecture finale après l'arrêt de l'orchestrateur, et "
    "alerte scellée pour la mère, qui prévient Lazar, où sont écrits la nature du déclencheur, le statut et la cause lue "
    "(« inconnue » pour un refus relayé de l'interface) ;")
remplacer(286, "6. **Carbon** :", "en flux, les contrôles sont ceux de la garde gelée et les réglages à inscrire.",
          "6. **Carbon** : appel en flux sous la garde gelée des appels aux modèles de Google (GO-2026-11-21-71, "
          "GO-2026-11-21-47), au prix plein, par la commande en flux et le relais Gemini v3 ; réglages du code : niveau `high`, "
          "provision 28 672, sortie maximale 65 536, délais 1 500 s et 60 s ; pire cas d'un appel **1,32 USD**, la réflexion "
          "comprise dans la sortie maximale (page de Google versée, `fe0b8d88…` ; contre-lecture du lanceur v11b), ce que seule "
          "la facture d'une course réelle confirmera (la seconde lecture du brouillon 3, 2,3042 USD, est retirée)."
          " **Retraits** : la commande Gemini par lot, le relais Gemini v4, le facteur de lot, et les gardes propres "
          "au lot (délai de lot de 1 620 s, bornes de lots et de relevés du relais) ; restent, en flux, une provision d'au "
          "moins 25 870 jetons, une sortie maximale d'au moins 24 500 et un délai de la génération d'au moins 1 500 s, avec les "
          "contrôles de la garde gelée (le brouillon 3 disait retirées ces trois gardes : le lanceur les garde).")
remplacer(287, "7. **Argon** (décision de la mère, R-5007, point (c)) :", "épinglées de la v6 à la v10.",
          "7. **Argon** (décision de la mère, R-5007, point (c)) : sous la même garde gelée — niveau de réflexion `high`, "
          "pensées demandées en retour, 16 000 jetons de texte au moins au-delà de la provision, défauts lus après la réponse "
          "— par la même commande en flux que Carbon et un relais Gemini v3 (port 8788) ; réglages du code : provision 24 576, "
          "sortie maximale 45 056, en flux (brouillon 4 ; le brouillon 3 chiffrait sur 16 384 et 32 768 hors flux). "
          "**Retraits** : la commande `commande_argon_v3d.py` et son enveloppe `appel-argon-v5.sh`, épinglées de la v6 à la "
          "v10 ; le relais Gemini v2.")
remplacer(289, "9. **Plafond de session des juges** :", "seul le plafond d'arrêt borne la dépense.",
          "9. **Plafond de session des juges** : 1,00 USD au lieu de 0,60 (configuration v11c, "
          "`argon_v11.plafond_session_juge_usd`, exigé égal à 1,00 ; R-5018) : aux réglages d'Argon du lanceur, la réflexion "
          "comprise dans la sortie maximale, le pire cas d'un appel de juge vaut 0,917240 USD (0,917356 sur l'entrée de juge du "
          "brouillon du lanceur v11c) ; le relèvement vaut aussi pour le juge Claude. Borne des plafonds de session : 600 USD "
          "au lieu de 472 ; seul le plafond d'arrêt borne la dépense.")
remplacer(290, "10. **Devis v11b**", "pire cas 150, inchangé (§ Plafond).",
          "10. **Devis v11c** (écrit pour cette version, à contre-lire ; le devis v11b aux réglages d'Argon du lanceur, lui-même "
          "le devis v11 plus le seuil de recharge de la clé LUC) : aux prix déclarés, Carbon au prix plein, 0,4805 USD par "
          "appel estimé, 1,32 au pire ; cinq espèces, sans la réflexion d'Argon : 35,68 USD sans marge, 39,25 avec ; base de "
          "l'écart au devis 35,683 ; réflexion d'Argon non mesurée, 3,52 USD par millier de jetons moyens par appel, 122,19 USD "
          "à sa provision entière (24 576 jetons) ; coupure de l'étape des juges au-delà de 32 476 jetons de moyenne, "
          "désormais sous la sortie maximale d'Argon ; plus de « haut » ; pire cas 150, inchangé (§ Plafond).")
remplacer(291, "11. **Lignes de GO et période** :", "(§ Règle des clés, « Période »).",
          "11. **Lignes de GO et période** : GO-2026-11-22-80, prolongation de GO-2026-11-18-14 au 2026-12-15, est le **GO de "
          "la course**, passé à l'orchestrateur et cité par la commande de lancement (" + COMMANDE_LANCEMENT + "), "
          "GO-2026-11-18-14 restant exigé ; GO-2026-11-22-107 (exception, échéance 2026-11-25, portée au 2026-12-15 par "
          "GO-2026-11-22-124 sous la réserve d'une confirmation de Lazar) ; jusqu'au 2026-11-25, départ sans confirmation ; "
          "ensuite, confirmation inscrite au registre et nommée dans la configuration exigée (§ Règle des clés, « Période »).")
sub(292, "essai à blanc du lanceur v11 versé avant le départ ;", "essai à blanc du lanceur v11c versé avant le départ ;")
sub(293, "13. **Contre-lecture** : par un Opus neuf, puis vérification des corrections par le même contre-lecteur (pièce de "
         "classe A) ; le modèle K contre-lisait les v2 à v10.",
    "13. **Contre-lecture** : par un Opus neuf, puis vérification des corrections par le même contre-lecteur (pièce de classe "
    "A) ; libellé exigé par le lanceur v11c : « Opus 5.5, contre-lecteur neuf » ; le modèle K contre-lisait les v2 à v10 ; le "
    "rédacteur du brouillon 4 est lui aussi Opus 5.5 (GO-2026-11-22-145).")
remplacer(294, "14. **Configuration v11** :", "au bloc descriptif de Carbon près.",
          "14. **Configuration v11c** : la v9, à la clé Claude près, plus les blocs neufs `changements_v11` (plafond de la part "
          "Claude, 45 USD ; GO de la course ; emplacement de la confirmation de la prolongation de GO-2026-11-22-107 ; notes) et "
          "`argon_v11` (plafond de session des juges, 1,00 USD, écrit par le lanceur dans la configuration servie) ; les "
          "configurations v11 et v11b, au GO de la course et à une note près (pièces).")
sub(295, "alerte neuve `alerte-arret-part-claude.json` ;",
    "alerte neuve `alerte-arret-part-claude.json` ; journal du run `journal-part-claude-au-fil-de-l-eau.jsonl` ; lanceur "
    "`scripts/lancer_course_affinage_mentors_v11c.py`, lancé par " + COMMANDE_LANCEMENT + " ;")

# ------------------------------------------------------------------------------------------------ dernière section, récrite
DERNIERE = """## Emplacements et points à trancher avant le scellement (section à retirer de la version scellée)

Emplacements à remplir (empreintes des pièces du lanceur v11c, que la session de l'organisme envoie dès leur scellement) :

1. EMPREINTE À INSCRIRE — configuration fixe v11c (pièces).
2. EMPREINTE À INSCRIRE — commande en flux v2 d'Argon et de Carbon (pièces). Le relais Gemini v3 est inscrit (`2cf6bc6d…`) ; les réglages d'Argon et de Carbon et les bornes de leurs relais sont inscrits, ceux du code (§ Espèces, liste d'arrêt).
3. EMPREINTE À INSCRIRE — sonde commune d'Astra v3 (pièces) ; la sonde d'Astra v3 est inscrite (`32366123…`).
4. EMPREINTE À INSCRIRE — essais du lanceur v11c, de la commande en flux v2 et de la sonde commune v3 ; gabarit de déclaration v11c ; gabarits des deux relevés (pièces) ; celle du lanceur seulement s'il ne porte plus l'empreinte de ce texte dans son code (sinon, cycle d'empreintes).
5. RÉFÉRENCE À INSCRIRE — ligne du registre des décisions qui porte les décisions de la session de l'organisme du 23 novembre (en-tête ; devis v11c). Le libellé de la contre-lecture est inscrit : « Opus 5.5, contre-lecteur neuf ».

Points tranchés ou à confirmer, avec la recommandation du rédacteur :

1. **Plafond de session des juges : 1,00 USD** — tranché (R-5018 ; décision du 23 novembre) : la commande compte la réflexion dans la sortie maximale ; pire cas d'un appel de juge d'Argon 0,917240 USD (lanceur v11b) ou 0,917356 (brouillon du lanceur v11c, entrée de juge de la forme de l'orchestrateur) ; marge de plus de 20 000 jetons d'entrée. La recommandation du brouillon 3 (1,10 USD si la provision s'ajoutait à la sortie maximale) est sans objet. Reste : la version scellée gardera la valeur que calcule le lanceur v11c scellé.
2. **Page de prix relue le jour du départ** : retenu, inchangé.
3. **Période** : la forme est établie (GO-2026-11-22-80 comme GO de la course ; essai du lanceur v11b sur la vraie lecture de l'orchestrateur). Un départ après le 25 novembre demande la confirmation de Lazar inscrite au registre et nommée dans une configuration neuve, donc un lanceur neuf (R12).
4. **Écrit de la mère sur les autres dépenses de la clé LUC** (R-5007, point (b)) : inchangé ; ce texte le lit « du départ à la fin de la course » et ne le fait pas contrôler par le lanceur ; à confirmer par la mère.
5. **Refus de l'interface et déclencheurs** : tranché (décision du 23 novembre) : déclencheurs larges et cause écrite telle que le lanceur la lit ; texte aligné (liste d'arrêt ; § Règle des clés, « Clé LUC », point 5).
6. **Réflexion d'Argon et plafond d'arrêt** (neuf). Aux réglages du lanceur, le seuil de 32 476 jetons de réflexion moyenne par appel d'Argon est sous la sortie maximale (45 056) : au-delà, l'étape des juges est coupée (« non mesuré (budget) », nœud, code 6) et la tentative unique est consommée sans bonne fin. R-5018 disait sans objet la mesure préalable de cette réflexion (GO-2026-11-22-128 : au plus 10,50 USD, hors du plafond de la course, non exécutée sauf confirmation de Lazar), sur un seuil alors presque égal à la sortie maximale (32 768). La même mesure dirait aussi si le fournisseur accepte pour Argon une sortie de 45 056 jetons en flux, jamais servie (point 7). Recommandation du rédacteur, confiance 0,7 : que la mère tranche avant le scellement entre (a) accepter ces deux risques tels que le texte les dit, sans dépense, et (b) jouer avant le départ la mesure de GO-2026-11-22-128 aux arguments exacts du gabarit v11c, sur une consigne de juge et une consigne de proposeur (périmètre et pièces à fixer par elle) ; (b) a ma préférence : elle protège la tentative unique pour au plus 10,50 USD. C'est une dépense : nœud, et mot de Lazar exigé par la note de GO-2026-11-22-128.
7. **Argon à 45 056 jetons de sortie en flux** (neuf) : jamais servi au-delà de 32 768 dans les pièces lues. Sans la mesure du point 6, un refus du fournisseur pour ce réglage ferait échouer chaque appel d'Argon, et A3 arrêterait ses deux rôles (étape des juges « non mesurée (technique) »). La porte à blanc et l'essai à blanc n'appellent pas le fournisseur.
8. **Notes de la configuration v11c** (neuf, rédaction seulement) : `changements_v11.carbon` et `changements_v11.argon` citent encore `commande_gemini_flux_v1.py`, alors que le lanceur v11c épingle la v2 ; `relais_persistants_v4.plafond_relais_claude_usd` garde 150, inerte (ni servi à l'orchestrateur ni lu par le lanceur). Recommandation, confiance 0,8 : corriger les deux notes avant de sceller la configuration v11c et dire le champ inerte au rapport du développeur ; aucune garde n'en dépend.

Points que ce texte fixe et que le lanceur v11c doit tenir, avec un essai sain et un essai artefact chacun (R5) ; si le lanceur fait autrement, le texte ou le lanceur change, jamais un écart silencieux. La liste phrase par phrase est dans `course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md` (`""" + ANNEXE_SHA + """`), écrite sur le brouillon 2 : ses numéros de lignes (l. 1 à 295) valent pour ce brouillon 4, dont seule la dernière section change de longueur ; le brouillon 4 change les phrases des items A1 à A4 (GO de la course GO-2026-11-22-80, GO-2026-11-18-14 exigé, registre dérivé, confirmation nommée dans la configuration), B2 et B5 (champs `solde_non_lu` et `reference`, montants et champs hors liste refusés), C1 (réserve par appel lue et écrite), C4 (lecture confirmée par l'essai du développeur du lanceur v11), D1 à D4 et D6 (lecture toutes les 10 s, journal du run nommé ; déclencheurs élargis — l'item D3 est renversé : les refus propres au relais, 401, 403, 404 et 413, arrêtent la course — ; part engagée au plafond ; état illisible trois fois ; cause écrite ; relecture finale refaite jusqu'à trois fois), F1 à F5 (garde rejouée sur le corps de l'entrée la plus longue ; limite de l'invite comptée en caractères ; réglages et bornes du relais écrits ; trois gardes des v8 et v9 gardées en flux), G1 à G4 (même commande que Carbon ; garde rejouée sur la plus longue entrée de chaque rôle, juge dans la forme de l'orchestrateur ; pire cas du juge sur un cadre de 1 000 caractères supposé, non « réel » ; champ `argon_v11.plafond_session_juge_usd` ; bornes du relais d'Argon), I2 (base 35,683 : exacte 35,683407, lanceur 35,683424), I4 (libellé) et I6 (pièces : lanceur v11c, commande en flux v2, relais Gemini v3, sondes v3), et la section K (dépôt de travail qui porte la garde commune de `main`). En résumé :

- le plafond du relais Claude égal à 45,00 USD au centime (arguments lus par PID et état), sa réserve par appel lue et écrite, et l'entrée de la clé LUC au relevé des crédits (`solde_non_lu` vrai, `reference` GO-2026-11-22-124, aucun montant, aucun autre champ que `source` et `note`) ;
- le GO de la course GO-2026-11-22-80 passé à l'orchestrateur et nommé par la configuration ; la lecture des lignes GO-2026-11-18-14, GO-2026-11-22-80, GO-2026-11-22-107 et GO-2026-11-22-124, et, après le 2026-11-25, de la ligne de confirmation nommée dans la configuration ;
- le relevé de l'état et du journal du relais Claude au moins une fois par minute (toutes les 10 s), le journal du run, l'arrêt au premier déclencheur (statut 400 à 499 hors 429 au journal, refus compté dans l'état, part engagée au plafond, trois lectures illisibles), la relecture finale, le code 5 et l'alerte `alerte-arret-part-claude.json` (nature, statut, cause lue) ;
- la garde gelée des appels aux modèles de Google sur la commande en flux de Carbon et d'Argon, avant l'envoi et après la réponse ; les prix d'Argon et de Carbon à 4 et 20 USD par million de jetons ; les réglages d'Argon (24 576, 45 056, en flux) et de Carbon (28 672, 65 536) ; le plafond de session des juges à 1,00 USD, et le pire cas d'un appel de juge d'Argon contrôlé sur la plus longue entrée de juge que bâtit le lanceur ;
- la sonde d'Astra faite avec `gpt-6.2-astra`, `OPENAI_API_KEY_2` et les prix 8 et 40, liée à la sonde commune v3 du jour, qui porte la variable de clé du relais jeté ;
- la base de l'écart au devis, 35,683 USD pour cinq espèces ;
- le libellé « Opus 5.5, contre-lecteur neuf » exigé de la contre-lecture ;
- les gardes héritées des lanceurs v7 à v10 que ce texte garde (bornes basses de tous les relais, exclusion mutuelle avec la course d'auto-conception, sonde liée à la sonde commune, état de relais neuf et lisible, codes de sortie distincts dont le code 6, plafond de session des proposeurs à 3,00 USD).

"""
DU_B3_AU_B4 = (" Du brouillon 3 au brouillon 4 (Opus 5.5, GO-2026-11-22-145 ; décisions de la session de l'organisme du "
               "23 novembre) : réglages d'Argon du code (provision 24 576, sortie maximale 45 056, en flux) ; réflexion comptée "
               "dans la sortie maximale, pour Argon et Carbon, sur la page de Google versée (pires cas : juge d'Argon "
               "0,917240 USD, proposeur d'Argon 0,911592, Carbon 1,32) ; seuil de coupure par la réflexion d'Argon désormais "
               "sous la sortie maximale ; libellé « Opus 5.5, contre-lecteur neuf » ; déclencheurs d'arrêt élargis et cause "
               "écrite ; entrée de la clé LUC au relevé, champs nommés ; GO de la course GO-2026-11-22-80 et commande de "
               "lancement ; lanceur v11c, commande en flux v2, relais Gemini v3, sondes v3, configuration v11c, devis v11c ; "
               "trois gardes des v8 et v9 gardées en flux pour Carbon ; garde Google rejouée sur la plus longue entrée de "
               "chaque rôle ; rédacteur Opus déclaré.")
assert ligne_326_b3.startswith("Du brouillon 1 au brouillon 2 :")
corps = [lignes[n] for n in range(1, 297)]
texte = "\n".join(corps) + "\n" + DERNIERE + ligne_326_b3 + DU_B3_AU_B4 + "\n"
assert "RÉGLAGE À INSCRIRE" not in texte, "un emplacement de réglage reste"
assert texte.count("\n## Emplacements et points à trancher avant le scellement") == 1
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 3 touchées (1 à 296) :", sorted(touchees))
print("lignes du brouillon 4 :", texte.count("\n"))
print("emplacements « EMPREINTE À INSCRIRE » :", texte.count("EMPREINTE À INSCRIRE"),
      "; « RÉFÉRENCE À INSCRIRE » :", texte.count("RÉFÉRENCE À INSCRIRE"))
