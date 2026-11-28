"""Construit le brouillon 5 du préenregistrement du plan B des juges (T0.5) à partir du brouillon 4, sans le modifier.

Traitement de la vérification des corrections du code et du brouillon 4 (constats VCB-01 à VCB-08). Chaque changement
est un remplacement exact : le texte ancien doit figurer une seule fois dans le brouillon 4, sinon arrêt. Tout le
reste, annexe A comprise, est recopié octet pour octet ; le bloc de l'annexe A (de sa ligne de début à sa ligne de fin)
est comparé, octet pour octet, avant et après.
Usage : python3 -I construire_brouillon5.py <brouillon 4> <brouillon 5 à écrire>
"""
import hashlib
import sys
from pathlib import Path

SOURCE, CIBLE = Path(sys.argv[1]), Path(sys.argv[2])
if CIBLE.exists():
    sys.exit(f"{CIBLE} existe déjà : on n'écrase jamais (R12)")
texte = SOURCE.read_text(encoding="utf-8")
B4 = "528a238667a7a5220a207982487682f677a1687f2ecbea1beac6ae247e2225b1"
VERIF = "a751e43cf66d63b6a80f004fd0be7a380e46927b729979cdcc7071385fc18fae"
RS1 = "b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7"
if hashlib.sha256(texte.encode("utf-8")).hexdigest() != B4:
    sys.exit("brouillon 4 : empreinte inattendue")
print("brouillon 4 :", B4)


def bloc_annexe_a(t: str) -> str:
    lignes = t.split("\n")
    debut = lignes.index("    ## Scoring Rubric")
    fin = max(i for i, x in enumerate(lignes) if x.startswith("    - Do not write any analysis."))
    return "\n".join(lignes[debut:fin + 1])


ANNEXE_AVANT = bloc_annexe_a(texte)


def remplacer(ancien: str, nouveau: str) -> None:
    global texte
    n = texte.count(ancien)
    if n != 1:
        sys.exit(f"texte ancien trouvé {n} fois (1 attendu) : {ancien[:90]!r}")
    texte = texte.replace(ancien, nouveau, 1)


# --------------------------------------------------------------------------------------------------- en-tête
remplacer("rejeu de la cause profonde — v1 (brouillon 4)\n", "rejeu de la cause profonde — v1 (brouillon 5)\n")

remplacer(
    "Le rédacteur du brouillon 4, sous-agent neuf, n'a écrit non plus ni le code du plan B, ni ses relectures R2, ni ses "
    "corrections. Brouillon 4 du 2026-10-20, vers 04:30 UTC : le brouillon 3 ",
    "Le rédacteur du brouillon 4, sous-agent neuf, n'a écrit non plus ni le code du plan B, ni ses relectures R2, ni ses "
    "corrections. Le rédacteur du brouillon 5, sous-agent neuf, n'a écrit ni le code du plan B, ni ses relectures R2, "
    "ni ses corrections, ni leur vérification, ni le brouillon 4 ; il a écrit les corrections de cette vérification "
    "(VCB) dans le code et ses tests, et ce brouillon. Brouillon 5 du 2026-10-20, vers 05:40 UTC : le brouillon 4 "
    f"(`{B4}`, gardé tel quel), plus le traitement de la vérification des corrections du code et du brouillon 4 "
    "(constats VCB-01 à VCB-08 ; rapport `verification-corrections/verification-corrections-R2-code-plan-B-v1.md`, "
    "dossier `plan-b-code/corrections-v1/`, à verser) ; traitement constat par constat : section « Vérification des "
    "corrections (VCB) » de `traitement-R2-code-plan-B-v1.md`. Le brouillon 4, du 2026-10-20 vers 04:30 UTC, était le "
    "brouillon 3 ")

remplacer(
    "(section « Transparence » ; pour le brouillon 4, seules des empreintes ont été recalculées).",
    "(section « Transparence » ; pour le brouillon 4, seules des empreintes ont été recalculées ; pour le brouillon 5, "
    "des empreintes et la configuration du manifeste du pilote, par les contrôles mécaniques).")

remplacer(
    "`travail/`, `travail-b4/` (construction et contrôles du brouillon 4).",
    "`travail/`, `travail-b4/` (construction et contrôles du brouillon 4), `travail-b5/` (construction et contrôles du "
    "brouillon 5).")

remplacer(
    "motifs gelés `COMMIT_CITE`, `TACHES_CITEES` et `ENTROPIE_CITEE`).",
    "motifs gelés `COMMIT_CITE`, `TACHES_CITEES` et `ENTROPIE_CITEE`). Le commit, comparé à l'arbre par la fonction "
    "gelée `exiger_code_cite` sur sa première occurrence, a aussi sa valeur unique exigée par `exiger_citations_planb` "
    "(VCB-03).")

# --------------------------------------------------------------------------------------------------- métrique (VCB-05)
remplacer(
    "R_S(ℓ) : maximum, sur ses positions, de l'écart relatif par jeton entre cette passe et sa passe en simple précision "
    "au noyau par défaut.",
    "R_S(ℓ) : maximum, sur ses positions, de l'écart relatif par jeton entre cette passe et sa passe en simple précision "
    "au noyau par défaut ; rôles : numérateur ‖a_défaut − a_math‖, dénominateur ‖a_math‖, la passe au noyau « math » "
    "étant la référence (`ecarts_par_jeton(a_défaut, a_math)` ; vérification des corrections, VCB-05 ; « Ordre des "
    "phases »).")

# --------------------------------------------------------------------------------------------------- plan d'analyse
remplacer(
    "ancrage au noyau « math » ; palier du chemin sur L1 et L2 ; contrôle positif D1 sur L3 ; puis `rejeu-3B-simple.json`",
    "ancrage au noyau « math » (rôles : la passe au noyau « math » est la référence, au dénominateur ; numérateur "
    "‖a_défaut − a_math‖, dénominateur ‖a_math‖ ; VCB-05) ; palier du chemin sur L1 et L2 ; contrôle positif D1 sur "
    "L3 ; puis `rejeu-3B-simple.json`")

remplacer(
    "- **Dépassement** : chaque échéance se contrôle avant chaque lot et avant chaque appel du témoin. Une phase peut donc "
    "dépasser son échéance d'au plus un lot ou un appel : au plus environ 500 s",
    "- **Dépassement** : chaque échéance se contrôle avant chaque lot, avant la conversion et le repère, avant l'ancrage, "
    "avant chaque rechargement d'un juge pour le témoin et avant chaque appel du témoin (fonction `_avant` du lanceur ; "
    "VCB-06). Une phase peut donc dépasser son échéance d'au plus l'étape commencée avant elle. Pour un lot ou un appel : "
    "au plus environ 500 s")
remplacer(
    "500 s pour un appel du témoin (ces trois derniers estimés). Une phase échue s'arrête sans écrire son fichier ; la "
    "phase suivante commence.",
    "500 s pour un appel du témoin (ces trois derniers estimés). La conversion et le repère (16 passes uniques en simple "
    "précision), l'ancrage (une passe) et un rechargement n'ont pas de durée mesurée : ils sont comptés sous la borne "
    "d'un lot ou d'un appel de la même phase (point ouvert du traitement, VCB-06). Sans ces contrôles, ils "
    "s'ajouteraient au lot qui les précède. Une phase échue s'arrête sans écrire son fichier ; la phase suivante "
    "commence.")

remplacer(
    "juges « 8B » et « 3B », `lot_juge` présent ;",
    "juges « 8B » et « 3B », `lot_juge` présent et entier positif, exigé avant toute lecture, qu'un fichier du rejeu "
    "soit écrit ou non (VCB-02) ;")

remplacer(
    "| égal au pilote ; lu aussi par le lecteur, pour recalculer le tirage des lots ; absent : arrêt (R-249) |",
    "| égal au pilote ; lu aussi par le lecteur, pour recalculer le tirage des lots ; absent ou autre qu'un entier "
    "positif : arrêt de la lecture, avant toute lecture (R-249 ; VCB-02) |")

remplacer(
    "**Restent** : la vérification des corrections du code et de ce brouillon 4 par un sous-agent neuf, mutants de la "
    "relecture 3 rejoués (R-249) ; la relecture R2 de la chaîne de lancement, quand elle sera écrite (point 6) ;",
    "**Faite ensuite** : la vérification des corrections du code et du brouillon 4 par un sous-agent neuf, mutants de la "
    "relecture 3 rejoués (R-249) : « prêt après corrections » ; ses constats VCB-01 à VCB-08 sont traités dans le code "
    "et dans ce brouillon 5, et ses mutants survivants rejoués (traitement, « Vérification des corrections (VCB) »). "
    "**Restent** : la relecture R2 de la chaîne de lancement, quand elle sera écrite (point 6) ; une vérification des "
    "corrections VCB par un sous-agent neuf, si la session la demande ;")

remplacer(
    "Faits sur ce brouillon 4 (résultats : traitement, « Contrôles mécaniques ») ;",
    "Faits sur le brouillon 4 (résultats : traitement, « Contrôles mécaniques »), puis refaits sur ce brouillon 5 "
    "(traitement, « Vérification des corrections (VCB) ») ;")

remplacer(
    "fichiers de travail du rédacteur : `travail/`, et, pour le brouillon 4, `travail-b4/` ;",
    "fichiers de travail des rédacteurs : `travail/`, et, pour les brouillons 4 et 5, `travail-b4/` et `travail-b5/` ;")

remplacer(
    "notes des corrections et traitement des constats (`traitement-R2-code-plan-B-v1.md`) ;",
    "notes des corrections et traitement des constats (`traitement-R2-code-plan-B-v1.md`) ; rapport de la vérification "
    "des corrections et ses pièces (`corrections-v1/verification-corrections/`), notes des corrections VCB "
    "(`corrections-v1/NOTES-CORRECTIONS-VCB-plan-b-v1.md`) et résultats des mutants rejoués ;")

remplacer(
    "R-247, R-249 et la ligne de la session sur ce brouillon 4 ;",
    "R-247, R-249 et les lignes de la session sur les brouillons 4 et 5 ;")

# --------------------------------------------------------------------------------------------------- liste d'arrêt
remplacer(
    "ou `lot_juge` absent (R-249) ;",
    "ou `lot_juge` absent ou autre qu'un entier positif (R-249 ; exigé avant toute lecture, même sans fichier du rejeu, "
    "VCB-02) ;")

# --------------------------------------------------------------------------------------------------- code et tests
remplacer(
    "**État au brouillon 4** : les points 1 à 5 sont écrits, intégrés, relus (R2, trois angles) et corrigés dans un clone "
    "à part, non commités (R-247, R-249) ;",
    "**État au brouillon 5** : les points 1 à 5 sont écrits, intégrés, relus (R2, trois angles), corrigés, vérifiés, "
    "puis corrigés de nouveau dans un clone à part, non commités (R-247, R-249 ; VCB-01 à VCB-04, VCB-06 à VCB-08) ;")

remplacer(
    "garde de l'annexe A avant le manifeste.",
    "garde de l'annexe A avant le manifeste ; commit du code cité une seule fois, exigé par `exiger_citations_planb` "
    "(VCB-03).")

remplacer(
    "tirage des lots recalculé par `lots_du_rejeu` et `exiger_lots_du_rejeu` (R-249).",
    "tirage des lots recalculé par `lots_du_rejeu` et `exiger_lots_du_rejeu` (R-249) ; `lot_juge` exigé, entier "
    "positif, par `exiger_config_de_l_etape`, avant toute lecture (VCB-02).")

remplacer(
    "retrait manquant, début absent, fin absente : arrêt, au lanceur et au lecteur ;",
    "retrait manquant, début absent, fin absente : arrêt, au lanceur et au lecteur ; règle « première ligne de début, "
    "dernière ligne de fin » (VCB-07) : ligne de fin en double après l'annexe, ligne de début en double avant elle : "
    "arrêt ; ligne de fin isolée avant l'annexe : sans effet sur l'extraction ; sur chacun de ces textes, la commande de "
    "`LISEZMOI.md` rend l'empreinte de `RS1.txt` exactement quand la garde passe ;")

remplacer(
    "bibliothèque sans `_prepare_generation_config` : arrêt (R-249) ;",
    "bibliothèque sans `_prepare_generation_config` : arrêt (R-249) ; graine par appel (VCB-01) : espion sur "
    "`torch.manual_seed` (la graine de l'appel, une fois, avant `generate`) ; jetons générés égaux à graine égale depuis "
    "deux états du générateur global, différents sous une autre graine ;")

remplacer(
    "lignes de citation (chaque intitulé absent, répété avec deux valeurs, ou différent) ;",
    "lignes de citation (chaque intitulé absent, répété avec deux valeurs, ou différent : un test par intitulé, commit "
    "du code et notations de chaque juge compris ; l'entropie, sans valeur attendue, absente ou répétée ; VCB-03) ;")

remplacer(
    "cadre de 2 lots) ;",
    "cadre de 2 lots ; règles du cadre propres au lecteur, cadre attendu écrit en clair et égal à celui du lanceur : "
    "notation « tronquée » sous le plafond hors du cadre, dernier lot incomplet exclu, VCB-04) ; `lot_juge` absent, nul, "
    "négatif ou d'un autre type qu'entier : arrêt, même sans fichier du rejeu (cas sain : lecture d'un run sans fichier "
    "du rejeu ; VCB-02) ;")

# --------------------------------------------------------------------------------------------------- transparence
remplacer(
    "les empreintes des fichiers scellés, recalculées par le rédacteur du brouillon 4 sans en afficher le contenu.\n",
    "les empreintes des fichiers scellés, recalculées par le rédacteur du brouillon 4 sans en afficher le contenu ;\n"
    "- pour le brouillon 5 : le rapport de la vérification des corrections du code et du brouillon 4 (VCB-01 à VCB-08), "
    "ses mutants et leurs sorties ; les mutants survivants, rejoués par le rédacteur sur une copie du code (modèle "
    "jouet, aucun juge réel) ; les empreintes des fichiers scellés et la configuration du manifeste du pilote, relues "
    "par les contrôles mécaniques (« Avant le scellement ») sans afficher le contenu des fichiers scellés.\n")

remplacer(
    "ce qu'il n'a pas tranché est nommé dans le traitement (« Points ouverts »).\n",
    "ce qu'il n'a pas tranché est nommé dans le traitement (« Points ouverts ») ;\n"
    "- du brouillon 4 au brouillon 5 : de la vérification des corrections du code et du brouillon 4 (VCB-01 à VCB-08). "
    "Sur la consigne de la session, le rédacteur a écrit les rôles de l'ancrage (VCB-05, point ouvert 1 du traitement) "
    "et les contrôles d'échéance du code (VCB-06, point ouvert 2) ; il a aligné le code sur deux règles déjà écrites "
    "(`lot_juge` exigé par le lecteur sans condition, VCB-02 ; commit du code cité une seule fois, VCB-03). Aucune "
    "règle de fond n'est ajoutée ; ce qui n'est pas tranché est nommé dans le traitement.\n")

# --------------------------------------------------------------------------------------------------- contre-lecture
remplacer(
    "traitement constat par constat, avec la place de chaque correction dans ce brouillon et dans le code : "
    "`corrections-v1/traitement-R2-code-plan-B-v1.md`.\n",
    "traitement constat par constat, avec la place de chaque correction dans ce brouillon et dans le code : "
    "`corrections-v1/traitement-R2-code-plan-B-v1.md`.\n"
    "- **Vérification des corrections du code et du brouillon 4** (R-249) : sous-agent neuf, qui n'a écrit ni ce texte, "
    "ni le code, ni ses tests, ni les corrections, ni les relectures ; rapport "
    "`corrections-v1/verification-corrections/verification-corrections-R2-code-plan-B-v1.md` (bloc-notes, à verser), "
    f"`{VERIF}` ; jugement : « prêt après corrections » ; corrections D-1 à D-15 faites et justes ; mutants de la "
    "relecture 3 rejoués et mutants neufs ; 8 constats (VCB-01 à VCB-04 : mineurs, tests au sens de R5 ; VCB-05 : "
    "mineur, texte ; VCB-06 à VCB-08 : information) ; traitement : section « Vérification des corrections (VCB) » du "
    "traitement des constats R2 du code, et ce brouillon 5.\n")

remplacer(
    "- **À venir avant le scellement** : vérification des corrections du code et de ce brouillon 4 par un sous-agent "
    "neuf, mutants de la relecture 3 rejoués (R-249) ; chaîne de lancement,",
    "- **À venir avant le scellement** : vérification des corrections VCB par un sous-agent neuf, si la session la "
    "demande ; chaîne de lancement,")

remplacer(
    "Fichiers à leur remettre explicitement : ce brouillon, et le brouillon 3 pour les différences ;",
    "Fichiers à leur remettre explicitement : ce brouillon, et les brouillons 3 et 4 pour les différences ; le rapport "
    "de la vérification des corrections et la section « Vérification des corrections (VCB) » du traitement ;")

# --------------------------------------------------------------------------------------------------- annexe A
remplacer(
    "Le texte est celui du brouillon 1, inchangé dans les brouillons 2 à 4 ",
    "Le texte est celui du brouillon 1, inchangé dans les brouillons 2 à 5 ")
remplacer(
    "Contrôle sur ce brouillon 4 : la commande de `LISEZMOI.md`, jouée sur une copie nommée `T0.5-plan-B-juges-v1.md`, "
    f"rend `{RS1}`, et `exiger_annexe_a_egale_a_rs1` la même empreinte (traitement, « Contrôles mécaniques »).",
    "Contrôle sur les brouillons 4 et 5 : la commande de `LISEZMOI.md`, jouée sur une copie nommée "
    f"`T0.5-plan-B-juges-v1.md`, rend `{RS1}`, et `exiger_annexe_a_egale_a_rs1` la même empreinte (traitement, "
    "« Contrôles mécaniques » et « Vérification des corrections (VCB) »).")

if bloc_annexe_a(texte) != ANNEXE_AVANT:
    sys.exit("le bloc de l'annexe A a changé : arrêt")
print("bloc de l'annexe A : identique, octet pour octet")
CIBLE.write_text(texte, encoding="utf-8")
print("brouillon 5 :", hashlib.sha256(texte.encode("utf-8")).hexdigest(), f"({texte.count(chr(10))} lignes)")
