"""Construit le brouillon 6 du préenregistrement du plan B des juges (T0.5) à partir du brouillon 5, sans le modifier.

Traitement de la vérification des corrections VCB et du brouillon 5 (constats VCB2-01 à VCB2-05), du point ouvert VCB-b
(garde de forme de `max_nouveaux_juge` au lecteur) et de la garde « une seule valeur par intitulé de citation », retenue
par la session. Chaque changement est un remplacement exact : le texte ancien doit figurer une seule fois dans le
brouillon 5, sinon arrêt. Tout le reste, annexe A comprise, est recopié octet pour octet ; le bloc de l'annexe A (de sa
ligne de début à sa dernière ligne de fin) est comparé, octet pour octet, avant et après.
Usage : python3 -I construire_brouillon6.py <brouillon 5> <brouillon 6 à écrire>
"""
import hashlib
import sys
from pathlib import Path

SOURCE, CIBLE = Path(sys.argv[1]), Path(sys.argv[2])
if CIBLE.exists():
    sys.exit(f"{CIBLE} existe déjà : on n'écrase jamais (R12)")
texte = SOURCE.read_text(encoding="utf-8")
B5 = "1d6f1932d8597421caeedeff16e7d0175003921c40bc0173c133cbdb3ef768f2"
VERIF2 = "95926f9c74f1dc7a1b014723b78404d30751a79f9c3635b20b3b5abb5a7e9b4b"
RS1 = "b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7"
HEURE = "06:45"
if hashlib.sha256(texte.encode("utf-8")).hexdigest() != B5:
    sys.exit("brouillon 5 : empreinte inattendue")
print("brouillon 5 :", B5)


def bloc_annexe_a(t: str) -> str:
    lignes = t.split("\n")
    debut = lignes.index("    ## Scoring Rubric")
    fin = max(i for i, x in enumerate(lignes) if x.startswith("    - Do not write any analysis."))
    return "\n".join(lignes[debut:fin + 1])


ANNEXE_AVANT = bloc_annexe_a(texte)
N = 0


def remplacer(ancien: str, nouveau: str) -> None:
    global texte, N
    n = texte.count(ancien)
    if n != 1:
        sys.exit(f"texte ancien trouvé {n} fois (1 attendu) : {ancien[:90]!r}")
    texte = texte.replace(ancien, nouveau, 1)
    N += 1


# --------------------------------------------------------------------------------------------------- en-tête
remplacer("rejeu de la cause profonde — v1 (brouillon 5)\n", "rejeu de la cause profonde — v1 (brouillon 6)\n")

remplacer(
    "il a écrit les corrections de cette vérification (VCB) dans le code et ses tests, et ce brouillon. Brouillon 5 du "
    "2026-10-20, vers 05:40 UTC : le brouillon 4 ",
    "il a écrit les corrections de cette vérification (VCB) dans le code et ses tests, et le brouillon 5. Le rédacteur "
    "du brouillon 6, sous-agent neuf, n'a écrit ni le code du plan B, ni ses relectures R2, ni ses corrections, ni les "
    "corrections VCB, ni leurs vérifications, ni les brouillons 1 à 5 ; il a écrit les corrections de la seconde "
    f"vérification (VCB2) dans le code et ses tests, et ce brouillon. Brouillon 6 du 2026-10-20, vers {HEURE} UTC : le "
    f"brouillon 5 (`{B5}`, gardé tel quel), plus le traitement de la vérification des corrections VCB et du brouillon 5 "
    "(constats VCB2-01 à VCB2-05 ; rapport `verification-v2/verification-corrections-VCB-plan-B-v1.md`, dossier "
    "`plan-b-code/corrections-v1/`, à verser), la garde de forme de `max_nouveaux_juge` au lecteur (point ouvert VCB-b) "
    "et la garde « une seule valeur par intitulé de citation », retenue par la session ; traitement constat par constat : "
    "section « VCB2 » de `traitement-R2-code-plan-B-v1.md`. Le brouillon 5, du 2026-10-20 vers 05:40 UTC, était le "
    "brouillon 4 ")

remplacer(
    "pour le brouillon 5, des empreintes et la configuration du manifeste du pilote, par les contrôles mécaniques).",
    "pour les brouillons 5 et 6, des empreintes et la configuration du manifeste du pilote, par les contrôles "
    "mécaniques).")

remplacer(
    "`travail-b5/` (construction et contrôles du brouillon 5).",
    "`travail-b5/` (construction et contrôles du brouillon 5), `travail-b6/` (construction et contrôles du brouillon "
    "6).")

# VCB2-03 : marqueurs refusés par les gardes du lanceur (trois) et par la chaîne (trois)
remplacer(
    "  - **Marqueurs à remplir au candidat**, au commit du code. Tant qu'il en reste un, les gardes de citation refusent "
    "le texte : aucun motif ne lit un marqueur (essai : « Avant le scellement »). `<<COMMIT_CODE>>` : commit du code "
    "d'analyse, 40 caractères hexadécimaux ; `<<EMPREINTE_CONFIG>>` : empreinte canonique de la configuration, 64 ; "
    "`<<ENTROPIE>>` : entier, tiré au scellement. Pour la chaîne de lancement : `<<TESTS_ATTENDUS>>` (nombre de tests "
    "de la suite au commit du code), `<<SHA256_AMORCE>>` et `<<SHA256_SCRIPT_INSTANCE>>` (empreintes des deux scripts "
    "de l'instance).\n",
    "  - **Marqueurs à remplir au candidat**, au commit du code. `<<COMMIT_CODE>>` : commit du code d'analyse, "
    "40 caractères hexadécimaux ; `<<EMPREINTE_CONFIG>>` : empreinte canonique de la configuration, 64 ; "
    "`<<ENTROPIE>>` : entier, tiré au scellement. Tant que l'un de ces trois reste, les gardes de citation du lanceur "
    "refusent le texte : aucun motif ne lit un marqueur (essai : « Avant le scellement »). Pour la chaîne de lancement : "
    "`<<TESTS_ATTENDUS>>` (nombre de tests de la suite au commit du code), `<<SHA256_AMORCE>>` et "
    "`<<SHA256_SCRIPT_INSTANCE>>` (empreintes des deux scripts de l'instance). Ces trois-là, les gardes du lanceur ne "
    "les lisent pas : un texte où seuls eux restent passe `exiger_code_cite` et `exiger_citations_planb` (essai de la "
    "vérification des corrections VCB, refait sur ce brouillon 6 ; VCB2-03). Leur refus revient à la chaîne, à écrire "
    "(point 6) : le script de l'instance lit « Tests attendus » et les empreintes des deux scripts, et doit refuser un "
    "texte où l'un d'eux reste un marqueur ; ce refus est à éprouver sur un artefact à la relecture R2 de la chaîne.\n")

# VCB2-05 (a) : renvoi périmé (le texte est le brouillon 6)
remplacer(
    "la session consigne aussi, au registre, ce qu'elle retient de ce brouillon 4.",
    "la session consigne aussi, au registre, ce qu'elle retient des brouillons 4, 5 et 6.")

# --------------------------------------------------------------------------------------------------- Dépassement
remplacer(
    "ils sont comptés sous la borne d'un lot ou d'un appel de la même phase (point ouvert du traitement, VCB-06).",
    "ils sont comptés sous la borne d'un lot ou d'un appel de la même phase (point ouvert du traitement, VCB-a).")

# --------------------------------------------------------------------------------------------------- Lecture
remplacer(
    "`lot_juge` présent et entier positif, exigé avant toute lecture, qu'un fichier du rejeu soit écrit ou non (VCB-02) ;",
    "`lot_juge` présent et entier positif, exigé avant toute lecture des fichiers du run, qu'un fichier du rejeu soit "
    "écrit ou non (VCB-02, VCB2-04) ; `max_nouveaux_juge` présent et entier positif, exigé de même (point ouvert "
    "VCB-b) ;")

# --------------------------------------------------------------------------------------------------- Configuration
remplacer(
    "| `lot_juge` | `8` | égal au pilote ; lu aussi par le lecteur, pour recalculer le tirage des lots ; absent ou autre "
    "qu'un entier positif : arrêt de la lecture, avant toute lecture (R-249 ; VCB-02) |",
    "| `lot_juge` | `8` | égal au pilote ; lu aussi par le lecteur, pour recalculer le tirage des lots ; absent ou autre "
    "qu'un entier positif : arrêt de la lecture, avant toute lecture des fichiers du run (R-249 ; VCB-02, VCB2-04) |")
remplacer(
    "| `max_nouveaux_juge` | `3072` | égal au pilote |",
    "| `max_nouveaux_juge` | `3072` | égal au pilote ; lu aussi par le lecteur, plafond du cadre du rejeu et de la "
    "lecture RS1 ; absent ou autre qu'un entier positif : arrêt de la lecture, avant toute lecture des fichiers du run "
    "(VCB-b) |")

# --------------------------------------------------------------------------------------------------- Avant le scellement
remplacer(
    "ses constats VCB-01 à VCB-08 sont traités dans le code et dans ce brouillon 5, et ses mutants survivants rejoués "
    "(traitement, « Vérification des corrections (VCB) »). **Restent** : la relecture R2 de la chaîne de lancement, "
    "quand elle sera écrite (point 6) ; une vérification des corrections VCB par un sous-agent neuf, si la session la "
    "demande ;",
    "ses constats VCB-01 à VCB-08 sont traités dans le code et dans le brouillon 5, et ses mutants survivants rejoués "
    "(traitement, « Vérification des corrections (VCB) »). **Faite aussi** : la vérification des corrections VCB et du "
    "brouillon 5 par un sous-agent neuf, mutants nommés rejoués : « prêt après corrections » ; ses constats VCB2-01 à "
    "VCB2-05 sont traités dans le code et dans ce brouillon 6, avec le point ouvert VCB-b, et ses mutants rejoués "
    "(traitement, « VCB2 »). **Restent** : la relecture R2 de la chaîne de lancement, quand elle sera écrite (point 6), "
    "avec le refus des trois marqueurs de la chaîne éprouvé sur un artefact (VCB2-03) ; une vérification des "
    "corrections VCB2 par un sous-agent neuf, si la session la demande ;")
remplacer(
    "puis refaits sur ce brouillon 5 (traitement, « Vérification des corrections (VCB) ») ;",
    "puis refaits sur le brouillon 5 (traitement, « Vérification des corrections (VCB) ») et sur ce brouillon 6 "
    "(traitement, « VCB2 ») ;")
remplacer(
    "  - fichiers de travail des rédacteurs : `travail/`, et, pour les brouillons 4 et 5, `travail-b4/` et `travail-b5/` ;",
    "  - fichiers de travail des rédacteurs : `travail/`, et, pour les brouillons 4, 5 et 6, `travail-b4/`, "
    "`travail-b5/` et `travail-b6/` ;")
remplacer(
    "notes des corrections VCB (`corrections-v1/NOTES-CORRECTIONS-VCB-plan-b-v1.md`) et résultats des mutants rejoués ;",
    "notes des corrections VCB (`corrections-v1/NOTES-CORRECTIONS-VCB-plan-b-v1.md`) et résultats des mutants "
    "rejoués ; rapport de la vérification des corrections VCB et ses pièces (`corrections-v1/verification-v2/`), notes "
    "des corrections VCB2 (`corrections-v1/NOTES-CORRECTIONS-VCB2-plan-b-v1.md`) et résultats des mutants rejoués "
    "(`corrections-v1/mutants-v3/`) ;")
remplacer(
    "R-247, R-249 et les lignes de la session sur les brouillons 4 et 5 ;",
    "R-247, R-249 et les lignes de la session sur les brouillons 4, 5 et 6 ;")

# --------------------------------------------------------------------------------------------------- liste d'arrêt
# garde « une seule valeur par intitulé », retenue par la session (plus stricte que `exiger_code_cite`)
remplacer(
    "invite RS1 et son index, entropie) ; annexe A du texte scellé,",
    "invite RS1 et son index, entropie ; une seule valeur par intitulé dans tout le texte, commit du code compris, "
    "exigée par `exiger_citations_planb`, plus stricte que la fonction gelée `exiger_code_cite`, qui ne lit que la "
    "première occurrence : VCB-03, garde retenue par la session) ; annexe A du texte scellé,")
remplacer(
    "ou `lot_juge` absent ou autre qu'un entier positif (R-249 ; exigé avant toute lecture, même sans fichier du rejeu, "
    "VCB-02) ;",
    "ou `lot_juge` ou `max_nouveaux_juge` absents ou autres qu'un entier positif (R-249 ; exigés avant toute lecture "
    "des fichiers du run, même sans fichier du rejeu ; VCB-02, VCB2-04, VCB-b) ;")

# --------------------------------------------------------------------------------------------------- code et tests
remplacer(
    "**État au brouillon 5** : les points 1 à 5 sont écrits, intégrés, relus (R2, trois angles), corrigés, vérifiés, "
    "puis corrigés de nouveau dans un clone à part, non commités (R-247, R-249 ; VCB-01 à VCB-04, VCB-06 à VCB-08) ;",
    "**État au brouillon 6** : les points 1 à 5 sont écrits, intégrés, relus (R2, trois angles), corrigés, vérifiés, "
    "corrigés de nouveau, vérifiés une seconde fois, puis corrigés encore, dans un clone à part, non commités (R-247, "
    "R-249 ; VCB-01 à VCB-04, VCB-06 à VCB-08 ; VCB2-01, VCB2-02, VCB2-04, VCB-b) ;")
remplacer(
    "`lot_juge` exigé, entier positif, par `exiger_config_de_l_etape`, avant toute lecture (VCB-02).",
    "`lot_juge` et `max_nouveaux_juge` exigés, entiers positifs, par `exiger_config_de_l_etape`, avant toute lecture "
    "des fichiers du run (VCB-02, VCB2-04, VCB-b).")
remplacer(
    "8B, 10 075 positions, simple précision ; R-249) ; copies versées et scellées.",
    "8B, 10 075 positions, simple précision ; R-249) ; refus d'un texte où reste l'un des trois marqueurs de la "
    "chaîne, que les gardes du lanceur ne lisent pas (artefact à éprouver à sa relecture R2 ; VCB2-03) ; copies versées "
    "et scellées.")
remplacer(
    "- échéances : chaque phase échue sans fichier, phase suivante lancée ; ancrages de chaque échéance ; dépassement "
    "d'au plus un lot ; échéance globale : arrêt consigné ; signal TERM ;",
    "- échéances : chaque phase échue sans fichier, phase suivante lancée ; ancrages de chaque échéance ; dépassement "
    "d'au plus l'étape commencée ; échéance globale : arrêt consigné ; signal TERM ; un test par point de contrôle neuf "
    "du « Dépassement », horloge remplacée (VCB2-01) : échéance du rejeu atteinte pendant le lot L2 de production (ni "
    "conversion, ni repère, ni ancrage ; `rejeu-…-demi` écrit, `rejeu-…-simple` échu), atteinte pendant le repère "
    "(aucun ancrage, aucun lot du chemin), échéance des témoins atteinte pendant le second appel du 8B (le 3B n'est pas "
    "rechargé) ; cas sains : l'autre juge, ou une échéance large, va au bout ; signal TERM au premier et au troisième "
    "point, échéance globale au deuxième : arrêt consigné à ce point ;")
remplacer(
    "`lot_juge` absent, nul, négatif ou d'un autre type qu'entier : arrêt, même sans fichier du rejeu (cas sain : "
    "lecture d'un run sans fichier du rejeu ; VCB-02) ;",
    "`lot_juge` absent, nul, négatif ou d'un autre type qu'entier : arrêt, même sans fichier du rejeu (cas sain : "
    "lecture d'un run sans fichier du rejeu ; VCB-02) ; `lot_juge` de la configuration employé au tirage (VCB2-02) : "
    "lecture synthétique avec `lot_juge` 4 et un tirage cohérent, la garde du tirage passe (la lecture s'arrête ensuite "
    "au nombre de rangées, 16 et 8, fixé par ce texte pour des lots de 8) ; le même run, tirage fait avec des lots de 8, "
    "arrête ; `max_nouveaux_juge` absent, nul, négatif ou d'un autre type qu'entier : arrêt (VCB-b) ;")

# --------------------------------------------------------------------------------------------------- Transparence
remplacer(
    "relues par les contrôles mécaniques (« Avant le scellement ») sans afficher le contenu des fichiers scellés.\n",
    "relues par les contrôles mécaniques (« Avant le scellement ») sans afficher le contenu des fichiers scellés.\n"
    "- pour le brouillon 6 : le rapport de la vérification des corrections VCB et du brouillon 5 (VCB2-01 à VCB2-05), "
    "ses mutants et leurs sorties ; les mutants nommés, rejoués par le rédacteur sur une copie du code (modèle jouet, "
    "aucun juge réel) ; les empreintes des fichiers scellés et la configuration du manifeste du pilote, relues par les "
    "contrôles mécaniques sans afficher le contenu des fichiers scellés.\n")
remplacer(
    "commit du code cité une seule fois, VCB-03). Aucune règle de fond n'est ajoutée ; ce qui n'est pas tranché est "
    "nommé dans le traitement.\n",
    "commit du code cité une seule fois, VCB-03). Aucune règle de fond n'est ajoutée ; ce qui n'est pas tranché est "
    "nommé dans le traitement.\n"
    "- du brouillon 5 au brouillon 6 : de la vérification des corrections VCB et du brouillon 5 (VCB2-01 à VCB2-05), et "
    "de deux points retenus par la session : la garde de forme de `max_nouveaux_juge` au lecteur (point ouvert VCB-b) "
    "et la garde « une seule valeur par intitulé de citation », écrite à la liste d'arrêt. Le rédacteur a ajouté des "
    "tests (VCB2-01, VCB2-02) et cette garde de forme, et précisé la rédaction (VCB2-03 à VCB2-05). Aucune règle de fond "
    "n'est ajoutée : le lanceur exige déjà `max_nouveaux_juge` entier positif et égal au pilote (liste d'arrêt, « Avant "
    "le manifeste ») ; le lecteur l'exige à son tour, comme `lot_juge`, pour qu'aucun arrêt ne passe sans message de "
    "garde ; ce qui n'est pas tranché est nommé dans le traitement.\n")

# --------------------------------------------------------------------------------------------------- Contre-lecture
# renvoi périmé de même nature que VCB2-05, relevé par le rédacteur (le texte n'est plus le brouillon 4)
remplacer("décision R-225, transcrite par ce brouillon 4.", "décision R-225, transcrite par le brouillon 4.")
remplacer(
    "traitement : section « Vérification des corrections (VCB) » du traitement des constats R2 du code, et ce "
    "brouillon 5.\n",
    "traitement : section « Vérification des corrections (VCB) » du traitement des constats R2 du code, et le "
    "brouillon 5.\n"
    "- **Vérification des corrections VCB et du brouillon 5** : sous-agent neuf, qui n'a écrit ni ce texte, ni le code, "
    "ni ses tests, ni aucune correction, ni aucune relecture ou vérification précédente ; rapport "
    "`corrections-v1/verification-v2/verification-corrections-VCB-plan-B-v1.md` (bloc-notes, à verser), "
    f"`{VERIF2}` ; jugement : « prêt après corrections » ; corrections VCB-01 à VCB-08 faites et justes ; 20 mutants "
    "nommés rejoués, tous tués ; 14 mutants neufs, dont 4 survivants ; 5 constats (VCB2-01 : mineur, tests au sens de "
    "R5 ; VCB2-02 à VCB2-05 : information) ; traitement : section « VCB2 » du traitement des constats R2 du code, et ce "
    "brouillon 6.\n")
remplacer(
    "- **À venir avant le scellement** : vérification des corrections VCB par un sous-agent neuf, si la session la "
    "demande ;",
    "- **À venir avant le scellement** : vérification des corrections VCB2 par un sous-agent neuf, si la session la "
    "demande ;")
remplacer(
    "Fichiers à leur remettre explicitement : ce brouillon, et les brouillons 3 et 4 pour les différences ; le rapport "
    "de la vérification des corrections et la section « Vérification des corrections (VCB) » du traitement ;",
    "Fichiers à leur remettre explicitement : ce brouillon, et les brouillons 3 à 5 pour les différences ; les rapports "
    "des deux vérifications des corrections et les sections « Vérification des corrections (VCB) » et « VCB2 » du "
    "traitement ;")

# --------------------------------------------------------------------------------------------------- annexe A
remplacer(
    "Le texte est celui du brouillon 1, inchangé dans les brouillons 2 à 5 ",
    "Le texte est celui du brouillon 1, inchangé dans les brouillons 2 à 6 ")
remplacer(
    "Contrôle sur les brouillons 4 et 5 : la commande de `LISEZMOI.md`, jouée sur une copie nommée "
    f"`T0.5-plan-B-juges-v1.md`, rend `{RS1}`, et `exiger_annexe_a_egale_a_rs1` la même empreinte (traitement, "
    "« Contrôles mécaniques » et « Vérification des corrections (VCB) »).",
    "Contrôle sur les brouillons 4, 5 et 6 : la commande de `LISEZMOI.md`, jouée sur une copie nommée "
    f"`T0.5-plan-B-juges-v1.md`, rend `{RS1}`, et `exiger_annexe_a_egale_a_rs1` la même empreinte (traitement, "
    "« Contrôles mécaniques », « Vérification des corrections (VCB) » et « VCB2 »).")

if bloc_annexe_a(texte) != ANNEXE_AVANT:
    sys.exit("le bloc de l'annexe A a changé : arrêt")
print("remplacements :", N)
print("bloc de l'annexe A : identique, octet pour octet")
CIBLE.write_text(texte, encoding="utf-8")
print("brouillon 6 :", hashlib.sha256(texte.encode("utf-8")).hexdigest(), f"({texte.count(chr(10))} lignes)")
