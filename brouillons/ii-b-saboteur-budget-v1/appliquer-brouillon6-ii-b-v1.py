"""Brouillon 6 de l'ordre exploratoire et du devis (ii-b) : fabrication par programme depuis le brouillon 5.

Usage : python3 -I -B appliquer-brouillon6-ii-b-v1.py DOSSIER CONTRE_LECTURE [--ecrire]
Sans `--ecrire` : essai à blanc (vérifie, rend les empreintes, n'écrit rien).

Deux passes, dans cet ordre, pour chacun des deux textes :
- passe 1 : les couples de la contre-lecture du brouillon 5 (fichier CONTRE_LECTURE, vérifié contre son empreinte). Pour chaque
  couple, les textes « avant » et « après » doivent figurer **mot pour mot** dans la contre-lecture (liste `preuves`) : une faute
  de recopie arrête le script ;
- passe 2 : les changements demandés par la session mère (commit du code revu, marqueurs, forme de la ligne de création de 7b,
  cas déclarés de P6-01, réserve P7-R1, en-tête), appliqués au texte rendu par la passe 1.

Règles, pour chaque passe :
1. les deux brouillons 5 sont vérifiés contre leurs empreintes écrites ici (égales à leurs compagnons `.sha256`) ;
2. les changements sont appliqués dans l'ordre ; chaque « avant » doit être présent **exactement une fois** au moment de son
   application ; tout le reste est recopié à l'octet ;
3. contrôle de recopie : chaque « après » est présent exactement une fois à la fin de sa passe, et l'application inverse (dans
   l'ordre inverse) rend le texte d'entrée de la passe à l'octet ;
4. les marqueurs `<<NOM>>` restants sont comptés par le même motif que `compter-marqueurs-ii-b-v1.py` ; leurs nombres doivent
   être ceux que le texte annonce (`ATTENDU_ORDRE`, `ATTENDU_DEVIS`) ;
5. aucun fichier de sortie ne doit exister (R12) ; avec `--ecrire` seulement : écriture du devis brouillon 6, de l'ordre
   brouillon 6 (qui cite l'empreinte du devis brouillon 6) et de la note des différences.
Tout écart : arrêt (code 2) avant toute écriture.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ORDRE5 = ("ordre-exploratoire-ii-b-v1-brouillon5.md", "73bc2781d79e69d33d0a0949c01f3861a74ff2e0c3ac6d74ac0dcee88068b223")
DEVIS5 = ("devis-ii-b-v1-brouillon5.md", "8ee9ead15fb5feadbffc41ffb3cd8d9abe8a8fc1d82b588f2957de93405e7e32")
CL5_SHA = "9ade0f1d3acaedee346fc082f764917d993545c10cf1d43706e9a3a2dd943a72"
CL5 = "`docs/notes/barreau8-iib-v1/contre-lecture-ordre-et-devis-iib-brouillon5-v1.md` (`" + CL5_SHA + "`)"
ORDRE6 = "ordre-exploratoire-ii-b-v1-brouillon6.md"
DEVIS6 = "devis-ii-b-v1-brouillon6.md"
DIFF = "differences-brouillon5-vers-6-v1.md"
HEURE = "2026-11-18 vers 23:00 UTC"
MERE = "session_013QMayjsoZJFBUCqcnvD5h1"

EC3 = "ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95"
A31 = "a31b8970fedb745c993fe23df18bba4a2d9e3cf4"
CC7 = "`docs/notes/barreau8-iib-v1/controle-court-code-iib-v7-v1.md` (`064b8b9ca56609f09b1acee292fa051aa8f8c0f2c9fab782198db35177dd4af7`)"
CC6 = "`docs/notes/barreau8-iib-v1/controle-court-code-iib-v6-v1.md` (`0d02d003872fb267b010acdad043285efe7c6b238db845570b9af68f252fa7f5`)"
VCC = "`docs/notes/barreau8-iib-v1/verification-courte-corrections-controle-court-iib-v1.md` (`4ef2101e949510491d65c110cc6dfda5da901f6f657c5f00fcc0118f0f86af8e`)"
RV7 = "`brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v7.md` (`46584a845bd0ddff6e7391ac229679fa9c0a79686b0e3f044b548fd449e6f182`)"
RV6 = "`brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v6.md` (`a95eb1051851277d31449fbdbbdc967f544d48a1d18deceb33c2ed59bfec4b6a`)"

MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
ATTENDU_ORDRE = 15   # 13 en attente sur les 30 de la configuration + 2 propres en attente
ATTENDU_DEVIS = 7    # ligne d'engagement, gabarit que la mère remplit au registre


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def abr(h: str) -> str:
    return h[:8] + "…" + h[-4:]


def marqueurs(t: str) -> list:
    return sorted(set(MOTIF_MARQUEUR.findall(t)))


# Un changement : (identifiant, où, raison, avant, après, preuves). `preuves` : textes qui doivent figurer mot pour mot dans la
# contre-lecture (passe 1) ; None en passe 2, ou pour un changement de la passe 1 dit « dérivé » dans sa raison.
def couple(ident, ou, raison, avant, apres, preuves="defaut"):
    return (ident, ou, raison, avant, apres, [avant, apres] if preuves == "defaut" else preuves)


# ================================================================ passe 1 : couples de la contre-lecture
P1_DEVIS = [
    couple("m1", "§ 0", "empreinte abrégée fausse de la note v2",
           "`be431ed5…7207`", "`be431ed5…5207`"),
    couple("m11", "table des remarques, ligne D-M2", "« sans trancher » date du brouillon 4 ; Lazar a tranché depuis",
           "| D-M2 deux branches de l'activité interne non chiffrées | appliquée : les deux branches chiffrées dans le script v3, hypothèses écrites, **sans trancher** | § 8 |",
           "| D-M2 deux branches de l'activité interne non chiffrées | appliquée : les deux branches chiffrées dans le script v3, hypothèses écrites ; tranché depuis par Lazar, branche B (§ 0) | § 8.1 |"),
]

_M2_AVANT = "- chaque compagnon vérifié (`PYTHONPATH=src python -m controle_ia.scellement verifier <fichier>`, puis `verifier-arbre .`) ;"
_M2_APRES = ("- fichiers du run extraits dans l'arbre de travail : `git -C \"$W/depot\" sparse-checkout add /diag/ /runs/ /donnees/ /traces/` ; "
             "`git -C \"$W/depot\" checkout --detach refs/remotes/origin/essai/iib-explo-v1` (forme jouée sur un dépôt jouet par le contre-lecteur du brouillon 5 ; rejouée à blanc à l'étape 6 du § 4) ;\n"
             "   - chaque fichier listé (au résumé ou à l'arrêt, puis au § 7) vérifié un par un depuis `$W/depot` : `PYTHONPATH=src python -m controle_ia.scellement verifier <fichier>` ; "
             "**le nombre de fichiers vérifiés est égal au nombre de fichiers listés** ; `verifier-arbre .` ne tient pas lieu de ce contrôle : il ne parcourt pas `donnees/` et rend « arbre intact » quand les dossiers du run ne sont pas extraits ;")
_M5_LIGNE_FORMAT = "| `FORMAT_ACTIONS_PORTAGE_IIB` (propre, neuf) | en attente | vérification du format des actions du barreau 8 (§ 2, point 2), avant le commit du code revu |"
_M5_LIGNE_TIRAGES = "| `TIRAGES_PERMUTATIONS_LECTURE2_IIB` (propre, neuf) | en attente | nombre de tirages et de permutations de la lecture (2) (§ 2), fixés par la mère avant le commit du code revu |"
_M5_APRES_S2 = ("Restent à fixer avant le commit du code revu, d'après le relevé (§ 4) : le nombre de tirages et de permutations de la lecture (2), `<<TIRAGES_PERMUTATIONS_LECTURE2_IIB>>` (les deux nombres, et la référence de la ligne du registre des décisions où la mère les consigne). "
                "Les versions de `numpy` et `scipy` sont consignées au manifeste. Les quatre réglages ci-dessus et ces deux nombres sont écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage, avant le commit du code revu.")
_M1_APRES_E2 = ("mineurs CC-02 à CC-05, faits avant le commit du code revu : le nœud 5 (a) demande avant la course toutes les corrections et tous les essais manquants, sauf les deux améliorations d'essais ; "
                "CC-04 et CC-05 sont des artefacts sans portée (R5) ; CC-03 est un chemin de fuite du texte privé vers les traces poussées ;")
_M1_APRES_S3 = "celui de la consigne invisible à l'évaluation ne voit pas les contextes, CC-04 ; celui de la garde numérotée (11) par la vérification courte, dans les essais du lanceur, est tautologique, CC-05 ;"
_M1_APRES_S11 = "| en attente | commit du code revu (§ 4 étape 2), après les corrections de CC-01 à CC-05 |"
_M3_APRES_E5 = ("la destruction (étape 6) est retenue jusqu'au mot de la session mère, au plus tard 48 heures après la fin du run et jamais après 2026-11-27T22:00:00Z ; "
                "au-delà de 48 heures d'arrêt, la mère ne prolonge que si la dépense relevée, plus le stockage à l'arrêt jusqu'à la destruction, reste sous 60 USD, calcul consigné au registre des dépenses "
                "(devis § 6 : le plafond de 59,8 USD ne tient que pour 48 heures d'arrêt) ; sans mot de la mère à cette borne, l'exécutante détruit et porte l'écart au compte rendu.**")
_M4_APRES = ("Sur ce mot seulement : relancer l'instance arrêtée ou lire son disque, puis rapatrier de nouveau. Une relance est une dépense de carte, comptée dans la ligne. "
             "Un second démarrage pousse d'abord les commits en attente ; mais l'amorce rejoue le calendrier à l'heure de l'instance (O-M6) : ce qu'elle fait à un second démarrage daté d'après le 2026-11-25 est relu dans le code à la vérification courte de l'ordre, "
             "et la relance est retirée de cette étape si l'amorce se détruit avant d'avoir poussé. Un fichier que les motifs de la poussée ne couvrent pas (CC-09) n'est dans aucun commit en attente : seule la lecture du disque le rend.")
_M3_APRES_E6 = "la mère pose deux rappels datés : 40 heures après la fin du run, et le 2026-11-27T20:00Z.**"
_M3_APRES_S7 = "la destruction est retenue jusqu'au mot de la session mère, dans les bornes du § 5 étape 5** (48 heures après la fin du run, jamais après 2026-11-27T22:00:00Z)."
_M3_APRES_RESUME = "destruction retenue jusqu'au mot de la session mère, au plus tard 48 heures après la fin du run et jamais après 2026-11-27T22:00:00Z (§ 5 étape 5, § 7)"
_M6_APRES_CODE = "- **Code lu** (brouillons 3 et 4) : `origin/prep/iib-code-v3`, à sa tête d'alors, `d88e3d947ec4f05958834e2746a800c854271a8f`."
_M7_APRES = "sinon `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (§ 11) retombe en attente)"
_M8_APRES = ("les extractions réduites de l'étape 1 et l'extraction des fichiers du run de l'étape 5 sont **jouées à blanc d'abord**, sans dépense, par la mère : "
             "une première fois dès la tête `a31b8970` (leur forme ne dépend pas du commit de lancement), puis à ce commit, avant le scellement de l'ordre ;")
_M3_SUFFIXE_4BIS = "(contrôle court, CC-01 ; son essai reste à corriger)"
_M3_APRES_4QUATER = ("poussée par phase corrigée, éprouvée sur la fin de run et sur l'arrêt consigné (la minuterie passe par la même fonction `ajouter_legeres`, sans essai à part) ; "
                     "contrôle de fin par `--ignored` corrigé et éprouvé sur la fin de run, seul chemin où il joue (CC-09) : le rapatriement couvre les autres (§ 5 étape 5) ;")
_M4_APRES_S8 = ("le rédacteur du brouillon 5 ; le contre-lecteur du code v2 ; le vérificateur du code v3 ; le contrôleur du contrôle court du code (tête `a31b8970`), qui a lu la consigne privée par programme ; "
                "**les contre-lecteurs de cet ordre et du devis (brouillons 3, puis brouillons 5)**. Le § 2 porte des réglages de la base textuelle des moniteurs : la mère inscrit au registre « qui a lu quoi » quiconque lit cet ordre.")

P1_ORDRE = [
    couple("m6-a", "en-tête, statut", "on ne savait plus de quel rédacteur il s'agit",
           "Le rédacteur n'a écrit ni la conception, ni le code, ni leurs contre-lectures ; il n'a vu aucun interne de moniteur ;",
           "Le rédacteur des brouillons 3 et 4 n'a écrit ni la conception, ni le code, ni leurs contre-lectures ; il n'a vu aucun interne de moniteur ;"),
    couple("m10", "en-tête, pièces citées", "le brouillon 3 est une pièce à lire avec l'ordre",
           "- **Pièces citées** (non modifiées) : conception",
           "- **Pièces citées** (non modifiées) : ordre, brouillon 3 (`eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f`), que l'exécutante lit avec cet ordre pour tout ce qui y est dit « inchangé depuis le brouillon 3 » ; conception"),
    couple("m6-b", "en-tête, code lu", "la tête citée se lisait comme celle d'aujourd'hui",
           "- **Code lu** : `origin/prep/iib-code-v3`, tête `d88e3d947ec4f05958834e2746a800c854271a8f` (inchangée depuis le brouillon 3).",
           _M6_APRES_CODE),
    couple("M3-d", "résumé « Ce que le brouillon 5 change »", "dérivé : « même correction dans le résumé » (contre-lecture, § 3, M3, dernière phrase), sans couple écrit",
           "destruction retenue jusqu'au mot de la session mère, au plus tard 2026-11-27T22:00:00Z (§ 5 étape 5, § 7)",
           _M3_APRES_RESUME,
           ["Même correction dans le résumé « Ce que le brouillon 5 change »."]),
    couple("m7", "§ 1, ligne « Code de (ii-b) »", "le marqueur n'était plus nommé dans la phrase",
           "sinon ce marqueur retombe en attente)", _M7_APRES),
    couple("m9", "§ 1, ligne « Calendrier »", "deux parenthèses de suite",
           "**aucune création après 2026-11-25T23:00Z** (dernière commande `creation` à 23:00 UTC le 2026-11-25) (l'amorce rejoue",
           "**aucune création après 2026-11-25T23:00Z** : dernière commande `creation` à 23:00 UTC le 2026-11-25 (l'amorce rejoue"),
    couple("m2", "§ 2", "empreinte abrégée fausse du relevé des réglages",
           "`98284ec7…d692`", "`98284ec7…e692`"),
    couple("M5-a", "§ 2, dernier paragraphe avant la table", "deux réglages restaient « indéterminés, sans choix ici », sans marqueur ni responsable",
           "Restent indéterminés d'après le relevé (§ 4), sans choix ici : le nombre de tirages et de permutations de la lecture (2) ; les versions de `numpy` et `scipy` (consignées au manifeste). Ces réglages sont écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage, avant le commit du code revu.",
           _M5_APRES_S2),
    couple("M1-b", "§ 3, titre", "CC-05 manquait au titre des gardes",
           "celui de la consigne invisible à l'évaluation ne voit pas les contextes, CC-04 ;", _M1_APRES_S3),
    couple("M1-a", "§ 4 étape 2", "quatre corrections laissées « souhaitables », contre le nœud 5 (a) et la règle des gardes (R5)",
           "mineurs CC-02 à CC-05, souhaitables avant la course selon le contrôle court (à trancher par la mère) ;", _M1_APRES_E2),
    couple("m8", "§ 4 étape 6", "essai à blanc à jouer plus tôt ; extraction des fichiers du run à jouer aussi",
           "les extractions réduites de l'étape 1 sont **jouées à blanc d'abord**, sans dépense, par la mère, avant le scellement de l'ordre ;",
           _M8_APRES),
    couple("m5", "§ 4 ter, dernière phrase", "point ouvert sans défaut",
           "il ne dit pas si ces essais deviennent des arrêts joués par l'amorce : point ouvert, porté à la mère.",
           "il ne dit pas si ces essais deviennent des arrêts joués par l'amorce : point porté à la mère ; sans mot d'elle avant le commit du code revu, ils ne sont pas joués par l'amorce (état présent du code, aucun code neuf)."),
    couple("m3", "§ 4 quater, « État à `a31b8970` »", "le texte disait plus que le contrôle court",
           "poussée par phase et contrôle de fin par `--ignored` corrigés et éprouvés sur les trois chemins de consignation ; le contrôle par `--ignored` ne joue qu'en fin de run (CC-09) : le rapatriement le couvre (§ 5 étape 5) ;",
           _M3_APRES_4QUATER),
    couple("m12-a", "§ 5 étape 5, premier point", "commandes de relevé et d'arrêt non nommées",
           "- l'instance est à l'état « stopped » (fin normale ou anormale) ; sinon l'exécutante l'arrête d'abord par son identifiant (R10) ;",
           "- l'instance est à l'état « stopped » (fin normale ou anormale), relevé par l'inventaire en champs filtrés sur le seul identifiant créé ; sinon l'exécutante l'arrête d'abord par cet identifiant (R10), avec la commande d'arrêt que la surveillance imprime (étape 4) ;"),
    couple("m12-b", "§ 5 étape 5, troisième point", "la lecture du résumé sur la branche n'avait pas de commande",
           "la liste `resultat.empreintes` de `diag/<run>/resume.json` (ou `sorties_ecrites` de `diag/<run>/arret.json` si le run s'est arrêté) contre",
           "la liste `resultat.empreintes` de `diag/<run>/resume.json` (ou `sorties_ecrites` de `diag/<run>/arret.json` si le run s'est arrêté), lue par `git -C \"$W/depot\" show refs/remotes/origin/essai/iib-explo-v1:diag/<run>/resume.json`, contre"),
    couple("M2", "§ 5 étape 5, quatrième point", "la vérification des compagnons pouvait passer à vide (repli silencieux, R5)",
           _M2_AVANT, _M2_APRES),
    couple("M3-a", "§ 5 étape 5, dernier point", "la retenue de la destruction n'était pas bornée par les 48 heures du devis",
           "la destruction (étape 6) est retenue jusqu'au mot de la session mère, au plus tard jusqu'à 2026-11-27T22:00:00Z.**",
           _M3_APRES_E5),
    couple("M4", "§ 5 étape 5, dernier point", "le remède « relancer l'instance arrêtée » peut se retourner après le 25",
           "Sur ce mot seulement : relancer l'instance arrêtée (un second démarrage pousse d'abord les commits en attente) ou lire son disque, puis rapatrier de nouveau.",
           _M4_APRES),
    couple("M3-c", "§ 5 étape 6", "deux rappels datés au lieu d'un",
           "la mère pose un rappel daté du 2026-11-27T20:00Z.**", _M3_APRES_E6),
    couple("M3-b", "§ 7", "même borne qu'au § 5 étape 5",
           "la destruction est retenue jusqu'au mot de la session mère, au plus tard 2026-11-27T22:00:00Z** (§ 5 étape 5).",
           _M3_APRES_S7),
    couple("m4", "§ 8", "exclus manquants ; le § 2 porte des réglages de la base textuelle des moniteurs",
           "le rédacteur du brouillon 5 ; le contre-lecteur du code v2 ; le vérificateur du code v3 ; **le contre-lecteur de cet ordre et du devis**.",
           _M4_APRES_S8),
    couple("M1-c", "§ 11, ligne des trois marqueurs du code", "CC-02 à CC-05 font partie des corrections attendues",
           "| en attente | commit du code revu (§ 4 étape 2), après la correction de CC-01 |", _M1_APRES_S11),
    couple("M5-b", "§ 11, ligne ajoutée", "marqueur neuf pour les nombres de tirages et de permutations",
           _M5_LIGNE_FORMAT, _M5_LIGNE_FORMAT + "\n" + _M5_LIGNE_TIRAGES,
           [_M5_LIGNE_FORMAT, _M5_LIGNE_TIRAGES]),
]


# ================================================================ passe 2 : changements demandés par la session mère
def chg(ident, ou, raison, avant, apres):
    return (ident, ou, raison, avant, apres, None)


def p2_devis() -> list:
    return [
        chg("D1", "titre", "version du texte",
            "# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 5",
            "# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 6"),
        chg("D2", "statut", "version du texte ; brouillon 5 gardé intact (R12)",
            "- **Statut** : **brouillon 5**, scellé comme brouillon, non contre-lu. Brouillon 4 (",
            "- **Statut** : **brouillon 6**, scellé comme brouillon, non contre-lu. Brouillon 5 (`devis-ii-b-v1-brouillon5.md`, `" + DEVIS5[1] + "`), brouillon 4 ("),
        chg("D3", "en-tête, ligne neuve", "qui a écrit le brouillon 6, depuis quoi, et ce qu'il porte",
            "sortie identique à l'octet à `sortie-calcul-devis-ii-b-v3.txt` (`8eecd277…8bd8`) ; aucun calcul sous nom neuf.",
            "sortie identique à l'octet à `sortie-calcul-devis-ii-b-v3.txt` (`8eecd277…8bd8`) ; aucun calcul sous nom neuf.\n"
            "- **Brouillon 6** : écrit le " + HEURE + " (`date -u`) par un rédacteur neuf (sous-agent de la session mère `" + MERE + "`, modèle Claude Fable 5.2), qui n'a écrit ni la conception, ni le code, ni leurs contre-lectures, ni les brouillons 1 à 5, et n'a ouvert ni la consigne privée ni la conception. "
            "Fabriqué par programme depuis le brouillon 5 (`appliquer-brouillon6-ii-b-v1.py`, scellé dans ce dossier), recopié à l'octet hors des changements listés dans `differences-brouillon5-vers-6-v1.md`. "
            "Il applique les deux couples de la contre-lecture du brouillon 5 qui touchent le devis (m1, m11 ; " + CL5 + ", lue en entier ; pour le devis : aucun chiffre ne change, plafond et coupure tenus, passe de recalcul hors de la ligne). "
            "La réserve R-1 de cette contre-lecture est levée : la ligne `R-3435` du registre des décisions porte, mot pour mot, le verbatim cité au § 0 (vérifié par programme par le rédacteur). "
            "Le commit du code revu est `" + EC3 + "` (contrôle court « autorisable », registre des décisions, ligne `R-3497`) : il est écrit dans la ligne d'engagement (§ 9). "
            "**Aucun chiffre ne change** : le calcul v3 a été rejoué de nouveau (`.venv/bin/python -I -B calcul-devis-ii-b-v3.py`), sortie identique à l'octet à `sortie-calcul-devis-ii-b-v3.txt` ; aucun calcul sous nom neuf."),
        chg("D4", "§ 8.3", "renvoi à l'ordre de même rang",
            "(ordre brouillon 5, § 13)", "(ordre brouillon 6, § 13)"),
        chg("D5", "§ 9, ligne d'engagement", "commit du code revu connu (`R-3497`) : marqueur rempli",
            "(code revu `<<COMMIT_CODE_IIB>>`)", "(code revu `" + EC3 + "`)"),
    ]


_NOUVELLE_SECTION = """## Ce que le brouillon 6 change (détail : `differences-brouillon5-vers-6-v1.md`)

- **Couples de la contre-lecture du brouillon 5** (""" + CL5 + """ ; verdict : « scellable après ces couples exacts ») : les cinq majeurs (M1 à M5) et les douze mineurs (m1 à m12) sont appliqués, mot pour mot (m1 et m11 portent sur le devis). Le couple R-1 n'est pas appliqué : il ne valait que si la ligne `R-3435` ne portait pas le verbatim cité ; elle le porte, mot pour mot (vérifié par programme par le rédacteur) : **R-1 levée**. **R-2 levée** : les contrôles courts des têtes `6e05a9d9` et `ec3b0329` comparent le portage au relevé du code des deux bases (registre des décisions, lignes `R-3485` et `R-3497`).
- **Commit du code revu** : `""" + EC3 + """`, « autorisable » (""" + CC7 + """ ; `R-3497`). `COMMIT_CODE_IIB` et `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` sont remplis par ce commit (§ 1, § 4 étape 2, § 5 étape 1, § 11). `COMMIT_LANCEMENT_IIB` reste un marqueur : le commit de lancement est l'enfant direct du commit du code revu qui n'ajoute que la configuration et son sceau, et la configuration n'est pas encore écrite (§ 4 étapes 4 et 5).
- **Format des actions pour le portage** : `FORMAT_ACTIONS_PORTAGE_IIB` rempli, « même format » (§ 2, point 2 ; `R-3497`).
- **Forme de la ligne de création de 7b** : écrite telle que le code l'attend à `ec3b0329`, avec son artefact (§ 4 étape 4) ; forme fixée par la session mère d'après le code, `R-3497`.
- **Règle de lecture de la lecture (2)** : les deux cas déclarés de P6-01 et la réserve P7-R1 sont écrits au § 2 (points 1 et 4).
- **Nombres de tirages et de permutations de la lecture (2)** : marqueur neuf `TIRAGES_PERMUTATIONS_LECTURE2_IIB` (couple M5), en attente de la ligne où la mère les consigne ; ce que le code porte à `ec3b0329` est écrit au § 2.
- **Marqueurs** (§ 11) : 15 distincts restent dans ce texte (16 au brouillon 5).

"""

_FORME_7B_AVANT = r"""Forme proposée de l'extrait cité (`<<LIGNE_REGISTRE_CREATION_7B>>`) : `7b créée : instance <identifiant Vast.ai, chiffres seuls> le <AAAA-MM-JJTHH:MMZ>`. Il doit figurer **une seule fois** dans `registres/decisions.md` du clone de `main` et satisfaire le motif `7b.*\binstance\s+\d+`."""
_FORME_7B_APRES = (r"""Forme de l'extrait cité (`<<LIGNE_REGISTRE_CREATION_7B>>`), **forme fixée par la session mère d'après le code, `R-3497`** : `7b créée, instance <identifiant Vast.ai, chiffres seuls> à <AAAA-MM-JJTHH:MM:SSZ>` (c'est la forme du cas sain des essais à `ec3b0329` : `7b créée, instance 99999999 à 2099-01-01T00:00:00Z`, `tests/test_iib_scripts_v1.py`, l. 29). """
                   r"""Ce que le code exige à `ec3b0329` (`src/controle_ia/iib/session_v1.py`, l. 76-91, fonction `verifier_creation_7b`, appelée par le lanceur aux contrôles et à la création ; l'amorce de l'instance, elle, ne relit pas le registre des décisions) : """
                   r"""(i) l'extrait que porte la configuration (`prealables.ligne_registre_creation_7b`, espaces de bord retirés) n'est pas vide et ne contient aucun chevron double, ouvrant ou fermant ; """
                   r"""(ii) il satisfait le motif `7b.*\binstance\s+\d+`, cherché sans tenir compte de la casse : « 7b », puis, plus loin dans l'extrait, le mot « instance », au moins un blanc, des chiffres ; """
                   r"""(iii) il est contenu tel quel dans **une seule** ligne de `registres/decisions.md` du clone de `main`. """
                   r"""**Artefact** (R5 ; même fichier d'essais, l. 125-131) : l'extrait `7b créée à 2099-01-01T00:00:00Z`, sans identifiant d'instance, est refusé par le motif (« la ligne de création de 7b ne mentionne pas « 7b » suivi d'un identifiant d'instance : refus ») ; """
                   r"""les autres refus sont éprouvés au même endroit (l. 107-122) : extrait vide ou resté en marqueur, extrait absent du registre, extrait trouvé deux fois, registre absent.""")


def p2_ordre(e6d: str) -> list:
    return [
        chg("E1", "titre", "version du texte",
            "# Ordre — saboteur à budget (ii-b), **course exploratoire**, instance à part — v1, brouillon 5",
            "# Ordre — saboteur à budget (ii-b), **course exploratoire**, instance à part — v1, brouillon 6"),
        chg("E2", "en-tête, statut", "qui a écrit le brouillon 6, depuis quoi ; brouillon 5 gardé intact (R12)",
            "- **Statut** : **brouillon 5**, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon5-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 4 (",
            "- **Statut** : **brouillon 6**, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon6-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 5 (`" + ORDRE5[0] + "`, `" + ORDRE5[1] + "`, intact, R12), recopié à l'octet hors des changements listés dans `differences-brouillon5-vers-6-v1.md`. "
            "Écrit le " + HEURE + " (`date -u`) par un rédacteur neuf (sous-agent de la session mère `" + MERE + "`, modèle Claude Fable 5.2), qui n'a écrit ni la conception, ni le code, ni leurs contre-lectures, ni les brouillons 1 à 5, qui n'a ouvert ni la consigne privée ni la conception, "
            "et qui n'a lu, du côté des moniteurs, que ce que portent les contrôles courts et les rapports du développeur cités plus bas (noms des fonctions de la pièce inscrite, seuils), sans ouvrir la pièce, les relevés ni l'enveloppe de la huitième tâche. "
            "Il applique les couples de la contre-lecture du brouillon 5 (" + CL5 + ", vérifiée, lue en entier ; verdict : « scellable après ces couples exacts »). "
            "Le brouillon 5 a été fabriqué par programme (`appliquer-brouillon5-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 4 ("),
        chg("E3", "en-tête, accords", "lignes du registre des décisions lues au brouillon 6",
            "Ces lignes renvoient à `R-3434`, non lue par le rédacteur.",
            "Ces lignes renvoient à `R-3434`, non lue par le rédacteur du brouillon 5. Au brouillon 6, lues dans le registre des décisions, ces seules lignes : `R-3434` ; `R-3435` (elle porte, mot pour mot, le verbatim cité au § 0 bis) ; `R-3485` (contrôle court de la tête `6e05a9d9`) ; `R-3490` (tête `ec3b0329`) ; `R-3497` (contrôle court de la tête `ec3b0329`, « autorisable » ; cette tête devient le commit du code revu ; réserve P7-R1 acceptée par la mère comme réserve écrite)."),
        chg("E4", "en-tête, pièces citées", "devis de même rang",
            "devis `devis-ii-b-v1-brouillon5.md` (`" + DEVIS5[1] + "` ; brouillon 4 `08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`, remplacé)",
            "devis `devis-ii-b-v1-brouillon6.md` (`" + e6d + "` ; brouillon 5 `" + DEVIS5[1] + "`, remplacé)"),
        chg("E5", "en-tête, pièces citées", "pièces citées au brouillon 6",
            "relevé des réglages de la base textuelle, `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md` (`98284ec7f6ac6bafbae0400234945d2b769db51fe7304b1ae5b181247ddde692`).",
            "relevé des réglages de la base textuelle, `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md` (`98284ec7f6ac6bafbae0400234945d2b769db51fe7304b1ae5b181247ddde692`) ; "
            "au brouillon 6 : contre-lecture du brouillon 5, " + CL5 + " ; contrôle court de la tête `6e05a9d9`, " + CC6 + " ; contrôle court de la tête `ec3b0329`, commit du code revu, " + CC7 + " ; "
            "rapports du développeur v6 et v7, sur la branche `prep/iib-code-v3`, " + RV6 + " et " + RV7 + " ; vérification courte des corrections du contrôle court, tête `ff6a9475`, " + VCC + " (lignes de CC-02 à CC-05 seules)."),
        chg("E6", "en-tête, code lu", "ce qui est pris du code à la tête du code revu",
            "Au brouillon 5, le code n'est pas relu : l'état de la tête `" + A31 + "` est pris du contrôle court (`02962a4a…c3a2`).",
            "Au brouillon 5, le code n'est pas relu : l'état de la tête `" + A31 + "` est pris du contrôle court (`02962a4a…c3a2`). "
            "Au brouillon 6 : le commit du code revu est `" + EC3 + "` (`R-3497`) ; son état est pris des deux contrôles courts et des deux rapports du développeur cités ci-dessus ; "
            "le rédacteur n'a lu au code, à cette tête, que ce qu'il faut pour la forme de la ligne de 7b et pour le format des actions : `src/controle_ia/iib/session_v1.py` (l. 70-96), les essais de cette ligne (`tests/test_iib_scripts_v1.py`, l. 29 et 105-132), "
            "l'en-tête et la fonction `action_pour_la_piece` de `src/controle_ia/iib/bases_textuelles_v1.py`, les constantes de `src/controle_ia/iib/configuration_v1.py` (l. 46-96) ; aucun essai rejoué."),
        chg("E7", "section neuve, avant « Ce que le brouillon 5 change »", "résumé des changements du brouillon 6",
            "## Ce que le brouillon 5 change (détail : `differences-brouillon4-vers-5-v1.md`)",
            _NOUVELLE_SECTION + "## Ce que le brouillon 5 change (détail : `differences-brouillon4-vers-5-v1.md`)"),
        chg("E8", "§ 0 bis", "devis de même rang",
            "pas au bit près**. Ordre de grandeur : devis brouillon 5, § 8.3.",
            "pas au bit près**. Ordre de grandeur : devis brouillon 6, § 8.3."),
        chg("E9", "§ 0 bis", "devis de même rang",
            "(ce qu'elle demanderait : devis brouillon 5, § 8.1)",
            "(ce qu'elle demanderait : devis brouillon 6, § 8.1)"),
        chg("E10", "§ 1, ligne « Conception, consigne, devis »", "devis de même rang",
            "`brouillons/ii-b-saboteur-budget-v1/devis-ii-b-v1-brouillon5.md` (`" + DEVIS5[1] + "`)",
            "`brouillons/ii-b-saboteur-budget-v1/devis-ii-b-v1-brouillon6.md` (`" + e6d + "`)"),
        chg("E11", "§ 1, ligne « Code de (ii-b) »", "commit du code revu connu (`R-3497`) ; il descend du commit des corrections du relais et de la poussée",
            "commit du code revu `<<COMMIT_CODE_IIB>>` sur `prep/iib-code-v3`, empreintes `<<EMPREINTES_CODE_IIB>>` ; il porte les corrections du relais et de la poussée (§ 4 quater), au commit `" + A31 + "` (contrôle court `02962a4a…c3a2` ; le commit du code revu doit en descendre, sur la même branche ; " + _M7_APRES + " ;",
            "commit du code revu `" + EC3 + "` sur `prep/iib-code-v3` (contrôle court `064b8b9c…4af7`, « autorisable », `R-3497`), empreintes `<<EMPREINTES_CODE_IIB>>` ; il porte les corrections du relais et de la poussée (§ 4 quater) : "
            "il descend, sur la même branche, du commit `" + A31 + "` (contrôle court `02962a4a…c3a2`), vérifié par le rédacteur (`git merge-base --is-ancestor`) : `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (§ 11) est rempli sans réserve ;"),
        chg("E12", "§ 1, ligne « Essais »", "liste ciblée relue au commit du code revu",
            "(`847676eff87f20c8aa5d7b1a1b401a7dd025c71c57d190ec0ba9c306f397e3b6` à `d88e3d94` ; à relire au commit du code revu, et dans l'amorce si la liste change)",
            "(`847676eff87f20c8aa5d7b1a1b401a7dd025c71c57d190ec0ba9c306f397e3b6` à `d88e3d94` ; relue au commit du code revu `ec3b0329` : inchangée, recalculée par le rédacteur avec `git show ec3b0329:scripts/tests-cibles-iib-v1.txt | sha256sum`, et égale à celle que l'amorce porte à ce commit)"),
        chg("E13", "§ 2, point 1", "réserve P7-R1 (contrôle court de la tête `ec3b0329`, `R-3497`)",
            "elle reprend les gardes de l'enveloppe de T0.8 (champs interdits, plis mêlés, lecture de transfert). Aucun réglage de la pièce n'est touché.",
            "elle reprend les gardes de l'enveloppe de T0.8 (champs interdits, plis mêlés, lecture de transfert). Aucun réglage de la pièce n'est touché. "
            "**Réserve P7-R1** (contrôle court de la tête `ec3b0329`, § 3 ; acceptée par la mère comme réserve écrite, `R-3497`) : la garde « lecture de transfert » est écrite d'après son nom, sans ouvrir l'enveloppe de la huitième tâche ; elle refuse tout transfert (un modèle ne note que le jeu sur lequel il a appris) ; "
            "elle ne laisse donc rien passer que l'enveloppe refuserait, mais son égalité de sens avec la garde de l'enveloppe n'est pas vérifiée : si cette égalité est voulue, un lecteur qui peut ouvrir l'enveloppe la confirme."),
        chg("E14", "§ 2, point 2", "marqueur `FORMAT_ACTIONS_PORTAGE_IIB` rempli d'après le code à la tête du code revu",
            "Issue de la vérification : `<<FORMAT_ACTIONS_PORTAGE_IIB>>` (« même format » ou « adaptateur déclaré », avec la référence de la vérification).",
            "Issue de la vérification, marqueur `FORMAT_ACTIONS_PORTAGE_IIB` : **« même format »**. À `ec3b0329`, le code applique le lecteur gelé `t06.cout.cout_action` au texte de l'action et compte les jetons par les identifiants générés, sans adaptateur (`src/controle_ia/iib/bases_textuelles_v1.py`, fonction `action_pour_la_piece`) ; "
            "le format a été vérifié par le développeur dans le code du lanceur, qui emploie déjà ce lecteur pour ses fiches d'épisodes (rapport du développeur v6, § 2 ; non rejoué par le rédacteur) ; "
            "les choix n° 2 et n° 3 du relevé suivent sa recommandation (A) d'après le contrôle court de la tête `6e05a9d9` (`R-3485`) ; le rapport du développeur v7 ne change que la règle de lecture (point 4) et la garde de transfert (point 1) ; tête `ec3b0329` « autorisable » (`R-3497`)."),
        chg("E15", "§ 2, point 4", "les deux cas déclarés de P6-01 (rapport du développeur v7, § 1 ; `R-3490` ; `R-3497`)",
            "4. **Règle de lecture** : l'état par unité de lecture (maximum des deux bases, seuil 0,70, plancher), sans les issues M1 à M4.",
            "4. **Règle de lecture** : l'état par unité de lecture (maximum des deux bases, seuil 0,70, plancher), sans les issues M1 à M4. "
            "À `ec3b0329` (P6-01, levé au contrôle court de cette tête, `R-3497`), cet état est le retour de la fonction d'état inscrite de la pièce (`etat_dose`), appelée telle quelle ; la règle propre au paquet est retirée. "
            "**Deux cas déclarés** où le résultat diffère de l'ancienne règle du paquet (rapport du développeur v7, § 1 ; `R-3490` ; d'après le contrôle court, ce sont les seuls écarts sur 3 698 combinaisons) : "
            "**(a)** une seule des deux bases ne se calcule pas : l'état de l'unité est « non calculable », et non plus l'état de la base qui se calcule ; "
            "**(b)** aires moyennes égales et états des deux bases différents : la base (A) décide, et non plus la base « mots et coût ». "
            "Ce que cela change pour la lecture (2), exploratoire : seul l'état de l'unité décisive (B100 contre H) entre dans la phrase de la lecture ; dans le cas (a), cette unité est « non calculable » et la phrase qui exige l'état « échoue » n'est pas prononcée ; dans le cas (b), l'issue est celle de la base (A). "
            "Rien ne change pour la course elle-même, ni pour la lecture (1)."),
        chg("E16", "§ 2, dernier paragraphe avant la table", "état du code au commit du code revu ; le marqueur des nombres de tirages et de permutations reste en attente",
            _M5_APRES_S2,
            "À fixer d'après le relevé (§ 4) : le nombre de tirages et de permutations de la lecture (2), `<<TIRAGES_PERMUTATIONS_LECTURE2_IIB>>` (les nombres, et la référence de la ligne du registre des décisions où la mère les consigne). "
            "État au commit du code revu `ec3b0329` : le code garde pour la lecture (2) les nombres de la configuration de la course (rapport du développeur v7, § 1), vérifiés à l'égalité par `configuration_v1.TEXTE`, clé `lecture_2` : `tirages_aire` 2 000, `tirages_taux` 10 000, `permutations` 200 (lus par le rédacteur à cette tête) ; "
            "le marqueur reste en attente de la ligne où la mère les consigne ; tout autre nombre demanderait un code neuf, donc un autre commit du code revu. "
            "Les versions de `numpy` et `scipy` sont consignées au manifeste. À `ec3b0329`, `FIXES_PAR_LE_CODE` porte le chemin et l'empreinte de la pièce inscrite et le choix de la meilleure base par action ; les réglages d'ajustement sont ceux de la pièce (rapport du développeur v6 ; `configuration_v1.py`, l. 54-61) ; les essais du portage sont dans la suite ciblée."),
        chg("E17", "§ 3, titre", "état des artefacts au commit du code revu",
            "l'essai du relais de la ligne des épreuves ne lit pas la ligne réelle du lanceur, CC-01, majeur)",
            "l'essai du relais de la ligne des épreuves ne lit pas la ligne réelle du lanceur, CC-01, majeur ; au commit du code revu `ec3b0329` : CC-02 à CC-05 corrigés (vérification courte de la tête `ff6a9475`, `4ef2101e…af8e`), CC-01 levé (contrôle court de la tête `6e05a9d9`, `R-3485`), "
            "forme de la ligne de 7b fixée (§ 4 étape 4), tête « autorisable » sans bloquant, majeur ni mineur (`R-3497`))"),
        chg("E18", "§ 4 étape 2", "forme de la ligne de 7b fixée",
            "forme de la ligne de création de 7b fixée, motif et artefact alignés (contrôle court, § 6, point 3) ;",
            "forme de la ligne de création de 7b **fixée** (§ 4 étape 4 ; forme fixée par la session mère d'après le code, `R-3497`), motif et artefact alignés à `ec3b0329` ;"),
        chg("E19", "§ 4 étape 2", "issue du format des actions connue",
            "issue `<<FORMAT_ACTIONS_PORTAGE_IIB>>` comprise) écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage ;",
            "issue « même format » comprise) portés par le code, avec les essais du portage, à `ec3b0329` ;"),
        chg("E20", "§ 4 étape 2", "contrôle court fait, commit du code revu connu ; répétition jouet et sa configuration",
            "contrôle court par un lecteur qui n'est pas le développeur ; **commit du code revu** `<<COMMIT_CODE_IIB>>`, empreintes `<<EMPREINTES_CODE_IIB>>`, dernière ligne `<<DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR>>`, répétition jouet identique à l'octet.",
            "contrôle court par un lecteur qui n'est pas le développeur : **fait**, « autorisable », 0 bloquant, 0 majeur, 0 mineur, une réserve de sens (P7-R1, § 2 point 1) (" + CC7 + " ; `R-3497`) ; "
            "**commit du code revu** `" + EC3 + "` : il porte CC-01 (levé, `R-3485`), CC-02 à CC-05 (corrigés, vérification courte `4ef2101e…af8e`), le portage, P6-01 et P6-02 ; "
            "empreintes `<<EMPREINTES_CODE_IIB>>`, dernière ligne `<<DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR>>` (à ce commit, le contrôle court rapporte pour la suite ciblée 456 essais réussis, aucun saut) ; "
            "répétition jouet identique à l'octet à ce commit (48 fichiers comparés, 0 différent ; configuration jouet `2e65c31b…`, entropie 20261118, d'après le contrôle court ; l'empreinte entière de cette configuration n'est écrite dans aucune pièce lue par le rédacteur)."),
        chg("E21", "§ 4 étape 4, premier point", "forme de la ligne de création de 7b telle que le code l'attend, avec son artefact",
            _FORME_7B_AVANT, _FORME_7B_APRES),
        chg("E22", "§ 4 étape 6", "la tête du code est désormais le commit du code revu",
            "une première fois dès la tête `a31b8970` (leur forme ne dépend pas du commit de lancement), puis à ce commit, avant le scellement de l'ordre ;",
            "une première fois dès le commit du code revu `ec3b0329` (le couple de la contre-lecture disait « dès la tête `a31b8970` », tête d'alors ; leur forme ne dépend pas du commit de lancement), puis au commit de lancement, avant le scellement de l'ordre ;"),
        chg("E23", "§ 4 bis, point 6", "CC-01 levé depuis",
            _M3_SUFFIXE_4BIS,
            "(contrôle court, CC-01 ; son essai, corrigé depuis, lit la sortie réelle d'un jeu jouet du lanceur : CC-01 levé au contrôle court de la tête `6e05a9d9`, `R-3485`)"),
        chg("E24", "§ 4 bis, point 6", "commit du code revu connu",
            "(`a31b8970`, ou le commit du code revu qui en descend)",
            "(commit du code revu `ec3b0329`, qui descend de `a31b8970`)"),
        chg("E25", "§ 4 quater, titre", "commit du code revu connu",
            "(session de développement ; tête : `" + A31 + "`, contrôlée)",
            "(session de développement ; fait : tête `" + A31 + "`, contrôlée, puis commit du code revu `" + EC3 + "`, « autorisable », `R-3497`)"),
        chg("E26", "§ 4 quater, « État à `a31b8970` »", "CC-01 levé depuis ; commit du code revu connu",
            "(CC-01, majeur, à corriger avant la course ; le commit qui en sortira sera celui de `COMMIT_CODE_IIB`)",
            "(CC-01, majeur ; corrigé depuis et levé au contrôle court de la tête `6e05a9d9`, `R-3485` ; le commit du code revu, `COMMIT_CODE_IIB`, est `" + EC3 + "`, `R-3497`)"),
        chg("E27", "§ 5 étape 1", "commit du code revu connu",
            "`git -C \"$W/depot\" rev-parse HEAD^` = `<<COMMIT_CODE_IIB>>` ; `git -C \"$W/depot\" diff --name-only <<COMMIT_CODE_IIB>> <<COMMIT_LANCEMENT_IIB>>`",
            "`git -C \"$W/depot\" rev-parse HEAD^` = `" + EC3 + "` ; `git -C \"$W/depot\" diff --name-only " + EC3 + " <<COMMIT_LANCEMENT_IIB>>`"),
        chg("E28", "§ 7", "commit du code revu connu",
            "et au commit du code revu qui en descend**",
            "et au commit du code revu `ec3b0329`, qui en descend**"),
        chg("E29", "§ 8", "exclus de la lecture des sondes : rédacteur du brouillon 6 ; le contrôleur a contrôlé quatre têtes",
            "le rédacteur du brouillon 5 ; le contre-lecteur du code v2 ; le vérificateur du code v3 ; le contrôleur du contrôle court du code (tête `a31b8970`), qui a lu la consigne privée par programme ;",
            "le rédacteur du brouillon 5 ; le rédacteur du brouillon 6 ; le contre-lecteur du code v2 ; le vérificateur du code v3 ; le contrôleur du contrôle court du code (têtes `a31b8970`, `ff6a9475`, `6e05a9d9` et `ec3b0329`), qui a lu la consigne privée par programme ;"),
        chg("E30", "§ 9-10", "devis de même rang",
            "Devis : `devis-ii-b-v1-brouillon5.md` (chiffres inchangés depuis le brouillon 4)",
            "Devis : `devis-ii-b-v1-brouillon6.md` (chiffres inchangés depuis le brouillon 4)"),
        chg("E31", "§ 11, première phrase", "six marqueurs propres",
            "plus cinq marqueurs nommés propres à l'ordre (hors de la configuration ; le cinquième, `FORMAT_ACTIONS_PORTAGE_IIB`, est neuf au brouillon 5).",
            "plus six marqueurs nommés propres à l'ordre (hors de la configuration ; le cinquième, `FORMAT_ACTIONS_PORTAGE_IIB`, est neuf au brouillon 5 ; le sixième, `TIRAGES_PERMUTATIONS_LECTURE2_IIB`, est neuf au brouillon 6, couple M5 de la contre-lecture du brouillon 5)."),
        chg("E32", "§ 11, `EMPREINTE_LISTE_TESTS_IIB`", "relue au commit du code revu",
            "| `EMPREINTE_LISTE_TESTS_IIB` | rempli, à relire | `847676ef…e3b6` au commit du code revu |",
            "| `EMPREINTE_LISTE_TESTS_IIB` | rempli | `847676ef…e3b6`, relue au commit du code revu `ec3b0329` : inchangée (§ 1) |"),
        chg("E33", "§ 11, devis", "devis de même rang",
            "`devis-ii-b-v1-brouillon5.md`, `8ee9ead1…7e32` |",
            "`devis-ii-b-v1-brouillon6.md`, `" + abr(e6d) + "` |"),
        chg("E34", "§ 11, marqueurs du code", "`COMMIT_CODE_IIB` rempli ; les deux autres restent en attente",
            "| `COMMIT_CODE_IIB`, `EMPREINTES_CODE_IIB`, `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR` " + _M1_APRES_S11,
            "| `COMMIT_CODE_IIB` | rempli | `" + EC3 + "` : commit du code revu, après les corrections de CC-01 à CC-05, le portage, P6-01 et P6-02 ; contrôle court « autorisable » (`064b8b9c…4af7`) ; `R-3497` |\n"
            "| `EMPREINTES_CODE_IIB`, `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR` | en attente | à relever par la mère au commit du code revu `ec3b0329` (§ 4 étape 2) ; à ce commit, le contrôle court rapporte pour la suite ciblée 456 essais réussis, aucun saut |"),
        chg("E35", "§ 11, `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`", "le commit du code revu porte ces corrections ; réserve levée",
            "| `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (propre) | rempli, sous réserve | `" + A31 + "` (contrôle court) ; retombe en attente si le commit du code revu n'en descend pas |",
            "| `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (propre) | rempli | `" + EC3 + "` : commit du code revu, qui porte ces corrections ; il descend, sur la même branche, de `" + A31 + "` (contrôle court de cette tête, `02962a4a…c3a2`) ; réserve du brouillon 5 levée (`R-3497`) |"),
        chg("E36", "§ 11, `COMMIT_LANCEMENT_IIB`", "le code n'est plus en cause ; le marqueur attend la configuration",
            "| `COMMIT_LANCEMENT_IIB` (propre) | en attente | § 4 étape 5 ; reste un marqueur : le développeur corrige encore un défaut majeur du code (CC-01) |",
            "| `COMMIT_LANCEMENT_IIB` (propre) | en attente | § 4 étape 5 : enfant direct du commit du code revu `" + EC3 + "`, qui n'ajoute que la configuration et son sceau ; il n'existe pas tant que la configuration n'est pas écrite, et elle attend les faits de la remise (§ 4 étape 4) ; le code n'est plus en cause |"),
        chg("E37", "§ 11, `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB`", "réglages portés par le code au commit du code revu",
            "point 4 (§ 2) ; écrits au code avant le commit du code revu |",
            "point 4 (§ 2) ; portés par le code au commit du code revu `ec3b0329` (contrôles courts des têtes `6e05a9d9` et `ec3b0329`, `R-3485`, `R-3497`), sous la réserve P7-R1 (§ 2, point 1) |"),
        chg("E38", "§ 11, `FORMAT_ACTIONS_PORTAGE_IIB`", "marqueur rempli",
            _M5_LIGNE_FORMAT,
            "| `FORMAT_ACTIONS_PORTAGE_IIB` (propre) | rempli | **« même format »** : lecteur gelé appliqué au texte de l'action, jetons comptés par les identifiants générés, sans adaptateur, à `ec3b0329` (§ 2, point 2 ; `R-3497`) |"),
        chg("E39", "§ 11, `TIRAGES_PERMUTATIONS_LECTURE2_IIB`", "le commit du code revu existe : ce que le marqueur attend encore",
            _M5_LIGNE_TIRAGES,
            "| `TIRAGES_PERMUTATIONS_LECTURE2_IIB` (propre, neuf) | en attente | nombres de tirages et de permutations de la lecture (2) : ceux que le code porte à `ec3b0329` (§ 2), à consigner par la mère au registre des décisions ; le marqueur attend la référence de cette ligne |"),
        chg("E40", "§ 11, comptes", "comptes refaits par programme",
            "Comptes : sur les 30, **14 remplis, 14 en attente, 2 hors de ce texte** (inchangés depuis le brouillon 4) ; plus 5 propres : **3 remplis** (`MOT_LAZAR_ACTIVITE_INTERNE_IIB`, `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`, `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB`), **2 en attente** (`COMMIT_LANCEMENT_IIB`, `FORMAT_ACTIONS_PORTAGE_IIB`). "
            "Compté par programme (`compter-marqueurs-ii-b-v1.py`, scellé dans ce dossier, qui ne cherche que le motif des marqueurs ; sortie `sortie-compter-marqueurs-ii-b-v1.txt`) : **16 marqueurs distincts restent dans ce texte** = les 14 en attente des 30 + les 2 propres en attente ; aucun marqueur rempli n'y reste.",
            "Comptes : sur les 30, **15 remplis, 13 en attente, 2 hors de ce texte** (au brouillon 5 : 14, 14, 2 ; `COMMIT_CODE_IIB` est rempli depuis) ; plus 6 propres : **4 remplis** (`MOT_LAZAR_ACTIVITE_INTERNE_IIB`, `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`, `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB`, `FORMAT_ACTIONS_PORTAGE_IIB`), **2 en attente** (`COMMIT_LANCEMENT_IIB`, `TIRAGES_PERMUTATIONS_LECTURE2_IIB`). "
            "Compté par programme (`compter-marqueurs-ii-b-v1.py`, scellé dans ce dossier, qui ne cherche que le motif des marqueurs ; sortie `sortie-compter-marqueurs-ii-b-v2.txt`) : **15 marqueurs distincts restent dans ce texte** = les 13 en attente des 30 + les 2 propres en attente ; aucun marqueur rempli n'y reste."),
        chg("E41", "§ 13", "devis de même rang",
            "sur le mot de Lazar. Ordre de grandeur : devis brouillon 5, § 8.3",
            "sur le mot de Lazar. Ordre de grandeur : devis brouillon 6, § 8.3"),
    ]


# ================================================================ application et contrôles
def appliquer(texte: str, changements: list, nom: str) -> str:
    for ident, _ou, _raison, avant, apres, _p in changements:
        n = texte.count(avant)
        if n != 1:
            sys.exit(f"ARRÊT : {nom} {ident} : « avant » présent {n} fois (1 attendu)")
        if avant == apres:
            sys.exit(f"ARRÊT : {nom} {ident} : changement vide")
        texte = texte.replace(avant, apres)
    return texte


def controler(final: str, origine: str, changements: list, nom: str) -> None:
    for ident, _ou, _raison, _avant, apres, _p in changements:
        n = final.count(apres)
        if n != 1:
            sys.exit(f"ARRÊT : {nom} {ident} : « après » présent {n} fois à la fin de la passe (1 attendu)")
    t = final
    for ident, _ou, _raison, avant, apres, _p in reversed(changements):
        if t.count(apres) != 1:
            sys.exit(f"ARRÊT : {nom} {ident} : application inverse impossible")
        t = t.replace(apres, avant)
    if t != origine:
        sys.exit(f"ARRÊT : {nom} : l'application inverse ne rend pas le texte d'entrée")


def controler_preuves(changements: list, cl: str, nom: str) -> None:
    for ident, _ou, _raison, _avant, _apres, preuves in changements:
        for p in preuves:
            if p not in cl:
                sys.exit(f"ARRÊT : {nom} {ident} : texte absent de la contre-lecture : {p[:80]!r}")


def bloc(t: str) -> str:
    if "~~~" in t:
        sys.exit("ARRÊT : un texte contient la clôture de bloc")
    return "~~~text\n" + t.strip("\n") + "\n~~~\n"


def note_differences(passes: dict, e6o: str, e6d: str, mo5: list, mo6: list, md5: list, md6: list) -> str:
    l = []
    l.append("# Différences du brouillon 5 au brouillon 6 — ordre exploratoire et devis du saboteur à budget (ii-b) — v1\n")
    l.append("- **Statut** : brouillon, scellé comme brouillon, non contre-lu. Écrit le " + HEURE + " (`date -u`) par le rédacteur neuf du brouillon 6 (sous-agent de la session mère `" + MERE + "`, modèle Claude Fable 5.2). Course **exploratoire, non opposable (R-522)**. Processeur seulement ; aucune dépense ; ni commit, ni poussée ; rien d'écrit sous `registres/`.")
    l.append("- **Fabrication** : `appliquer-brouillon6-ii-b-v1.py` (ce dossier, scellé), en deux passes. Passe 1 : les couples de la contre-lecture du brouillon 5 ; chaque « avant » et chaque « après » de ces couples figure mot pour mot dans la contre-lecture (contrôlé par le script). Passe 2 : les changements demandés par la session mère, sur le texte rendu par la passe 1. Dans chaque passe, chaque « avant » est présent exactement une fois au moment de son application, chaque « après » exactement une fois à la fin de la passe, et l'application inverse rend le texte d'entrée à l'octet ; tout le reste est recopié à l'octet.")
    l.append("- **Pièces** :")
    l.append(f"  - ordre : brouillon 5 `{ORDRE5[0]}` (`{ORDRE5[1]}`) → brouillon 6 `{ORDRE6}` (`{e6o}`) ;")
    l.append(f"  - devis : brouillon 5 `{DEVIS5[0]}` (`{DEVIS5[1]}`) → brouillon 6 `{DEVIS6}` (`{e6d}`) ;")
    l.append("  - contre-lecture du brouillon 5 : " + CL5 + ", lue en entier ; verdict : « scellable après ces couples exacts » ;")
    l.append("  - contrôle court de la tête du code revu : " + CC7 + ", « autorisable » ; rapport du développeur v7 : " + RV7 + ", sur la branche `prep/iib-code-v3` ;")
    l.append("  - registre des décisions, ces seules lignes : `R-3434`, `R-3435`, `R-3485`, `R-3490`, `R-3497` ; registre des accords, ces seules lignes : `GO-2026-11-10-08`, `GO-2026-11-18-55`, `GO-2026-11-18-56`.")
    l.append("- **Application des couples de la contre-lecture** :")
    l.append("")
    l.append("| couple | texte | appliqué | changements |")
    l.append("|---|---|---|---|")
    l.append("| R-1 | ordre et devis | **non, sans objet** : le couple ne valait que si `R-3435` ne portait pas le verbatim cité ; la ligne le porte, mot pour mot (vérifié par programme) ; réserve levée | — |")
    l.append("| R-2 | ordre | réserve levée, aucun couple : les contrôles courts des têtes `6e05a9d9` et `ec3b0329` comparent le portage au relevé (`R-3485`, `R-3497`) | — |")
    l.append("| M1 | ordre | oui, trois couples, mot pour mot | M1-a, M1-b, M1-c |")
    l.append("| M2 | ordre | oui, mot pour mot | M2 |")
    l.append("| M3 | ordre | oui, trois couples mot pour mot, plus la même correction dans le résumé du brouillon 5 (demandée sans couple écrit : dérivée) | M3-a, M3-b, M3-c, M3-d |")
    l.append("| M4 | ordre | oui, mot pour mot | M4 |")
    l.append("| M5 | ordre | oui, mot pour mot : paragraphe du § 2 et ligne ajoutée au § 11 ; comptes refaits par programme en passe 2 (E31, E40) | M5-a, M5-b |")
    l.append("| m1 | devis | oui | m1 |")
    l.append("| m2 | ordre | oui | m2 |")
    l.append("| m3 | ordre | oui | m3 |")
    l.append("| m4 | ordre | oui | m4 |")
    l.append("| m5 | ordre | oui | m5 |")
    l.append("| m6 | ordre | oui, deux couples | m6-a, m6-b |")
    l.append("| m7 | ordre | oui | m7 |")
    l.append("| m8 | ordre | oui | m8 |")
    l.append("| m9 | ordre | oui | m9 |")
    l.append("| m10 | ordre | oui | m10 |")
    l.append("| m11 | devis | oui | m11 |")
    l.append("| m12 | ordre | oui, deux couples | m12-a, m12-b |")
    l.append("")
    l.append("- **Couples dont la passe 2 retouche ensuite le texte**, parce que le commit du code revu existe désormais (le texte de la contre-lecture a d'abord été posé tel quel, puis mis à jour) : M5-a (E16), M5-b (E38, E39), M1-c (E34), m7 (E11), m8 (E22), m4 (E29). Le sens de chaque couple est gardé.")
    l.append("- **Les deux fautes d'empreinte abrégée** de la note des différences précédente (m1, m2) ne sont pas reprises ici : les empreintes de cette note sont entières.")
    l.append("- **Devis** : aucun chiffre ne change ; calcul v3 rejoué, sortie identique à l'octet ; aucun calcul sous nom neuf. Le § 6 du devis (instance arrêtée détruite sous 48 heures) n'est pas touché : le couple M3 aligne l'ordre sur lui.")
    l.append("- **Marqueurs** (motif `<<[A-Z0-9_]+>>` seul ; `compter-marqueurs-ii-b-v1.py`, sortie `sortie-compter-marqueurs-ii-b-v2.txt`, scellée dans ce dossier) :")
    l.append(f"  - ordre : brouillon 5, {len(mo5)} distincts ; brouillon 6, **{len(mo6)} distincts**. Retirés : " + ", ".join(f"`{m}`" for m in sorted(set(mo5) - set(mo6))) + ". Ajouté : " + ", ".join(f"`{m}`" for m in sorted(set(mo6) - set(mo5))) + ".")
    l.append("  - ordre, restants : " + ", ".join(f"`{m}`" for m in mo6) + ".")
    l.append(f"  - devis : brouillon 5, {len(md5)} distincts ; brouillon 6, **{len(md6)} distincts**, tous dans la ligne d'engagement (gabarit que la mère remplit au registre). Retiré : " + ", ".join(f"`{m}`" for m in sorted(set(md5) - set(md6))) + ".")
    l.append("  - devis, restants : " + ", ".join(f"`{m}`" for m in md6) + ".")
    l.append("- **Points portés à la session mère** :")
    l.append("  1. **`COMMIT_LANCEMENT_IIB` reste un marqueur**, alors que la demande de la mère disait que le commit du code revu le remplace. Le commit de lancement est, par la définition de l'ordre et par le code (la configuration cite le commit du code revu et ne peut pas citer le commit qui la contient ; l'exécutante vérifie que le parent du commit de lancement est le commit du code revu et que leur différence est la configuration et son sceau), un enfant direct du commit du code revu. Il n'existe pas tant que la configuration n'est pas écrite. Le commit `ec3b0329…` remplit `COMMIT_CODE_IIB` et `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`. Si la mère voulait autre chose, c'est un changement du § 1, du § 4 étape 5 et du § 5 étape 1.")
    l.append("  2. **Forme de la ligne de 7b** : le contrôle est dans `session_v1.verifier_creation_7b`, appelé par le lanceur aux contrôles et à la création ; l'amorce de l'instance ne relit pas le registre des décisions. Le motif est inchangé depuis le brouillon 5 ; la forme écrite est celle du cas sain des essais.")
    l.append("  3. **`FORMAT_ACTIONS_PORTAGE_IIB`** : la vérification du format est rapportée par le rapport du développeur v6 (§ 2) et le contrôle court de la tête `6e05a9d9` ; le rapport v7 ne numérote pas de choix n° 2 ni n° 3. Le rédacteur a lu la fonction au code ; il n'a rien rejoué.")
    l.append("  4. **`TIRAGES_PERMUTATIONS_LECTURE2_IIB`** : aucune des lignes de registre lues ne consigne ces nombres ; le marqueur attend la référence de la ligne de la mère. Les nombres que le code porte sont écrits au § 2.")
    l.append("  5. **`EMPREINTES_CODE_IIB` et `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR`** restent en attente : la mère les relève au commit du code revu.")
    l.append("  6. **M3**, dernière clause (« sans mot de la mère à cette borne, l'exécutante détruit ») : c'est le choix du contre-lecteur entre perdre un fichier et dépasser la ligne ; l'inverse demanderait une ligne de dépense, donc un mot de Lazar.")
    l.append("  7. **M4** : ce que fait l'amorce à un second démarrage daté d'après le 2026-11-25 reste à relire dans le code, à la vérification courte de l'ordre ; le rédacteur ne l'a pas relu.")
    l.append("  8. **Réserve P7-R1** : écrite au § 2, point 1 ; acceptée par la mère comme réserve écrite (`R-3497`).")
    l.append("  9. **Configuration jouet** : aucun marqueur ne la porte, ni dans l'ordre ni dans le devis ; son empreinte abrégée (`2e65c31b…`) est citée au § 4 étape 2 d'après le contrôle court ; sa forme entière n'est dans aucune pièce lue.")
    l.append("  10. **Phrase du § 2 non touchée** : « Le sous-point « gradient lu après le dernier pas » est fixé par le code à la tête `a31b8970` (contrôle court, CC-08) ». Depuis le portage sur la pièce inscrite, les réglages d'ajustement sont ceux de la pièce : la mère dit si cette phrase est à garder.")
    l.append("  11. Inchangés depuis le brouillon 5 : la copie publique et `donnees/*-iib-*` ; l'inscription de la branche `prep/iib-code-v2` au registre « qui a lu quoi » ; les deux lignes du `.gitignore` (CC-07) ; le défaut du couple m5 (essais du jetoniseur réel non joués par l'amorce sans mot de la mère).")
    l.append("")
    for cle, titre, fich in (("devis", "Devis", DEVIS6), ("ordre", "Ordre", ORDRE6)):
        for num, nom_passe in ((1, "passe 1, couples de la contre-lecture du brouillon 5"), (2, "passe 2, changements demandés par la session mère")):
            ch = passes[cle][num]
            l.append(f"## {titre} (`{fich}`), {nom_passe} : {len(ch)} changements\n")
            l.append("| changement | où | raison |\n|---|---|---|")
            for ident, ou, raison, _a, _b, _p in ch:
                l.append(f"| {ident} | {ou} | {raison} |")
            l.append("")
            for ident, ou, raison, avant, apres, _p in ch:
                l.append(f"### {ident} — {ou}\n")
                l.append("Avant :\n")
                l.append(bloc(avant))
                l.append("Après :\n")
                l.append(bloc(apres))
    return "\n".join(l)


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("usage : appliquer-brouillon6-ii-b-v1.py DOSSIER CONTRE_LECTURE [--ecrire]")
    d = Path(sys.argv[1])
    ecrire = "--ecrire" in sys.argv[3:]
    bcl = Path(sys.argv[2]).read_bytes()
    if sha(bcl) != CL5_SHA:
        sys.exit(f"ARRÊT : empreinte de la contre-lecture : {sha(bcl)} ≠ {CL5_SHA}")
    cl = bcl.decode("utf-8")
    srcs = {}
    for nom, emp in (ORDRE5, DEVIS5):
        b = (d / nom).read_bytes()
        if sha(b) != emp:
            sys.exit(f"ARRÊT : empreinte de {nom} : {sha(b)} ≠ {emp}")
        comp = (d / (nom + ".sha256")).read_text(encoding="utf-8").split()[0]
        if comp != emp:
            sys.exit(f"ARRÊT : compagnon de {nom} différent")
        srcs[nom] = b.decode("utf-8")
    for nom in (ORDRE6, DEVIS6, DIFF):
        if (d / nom).exists():
            sys.exit(f"ARRÊT : {nom} existe déjà (R12)")
    devis5, ordre5 = srcs[DEVIS5[0]], srcs[ORDRE5[0]]

    controler_preuves(P1_DEVIS, cl, "devis")
    controler_preuves(P1_ORDRE, cl, "ordre")

    devis_p1 = appliquer(devis5, P1_DEVIS, "devis passe 1")
    controler(devis_p1, devis5, P1_DEVIS, "devis passe 1")
    cd2 = p2_devis()
    devis6 = appliquer(devis_p1, cd2, "devis passe 2")
    controler(devis6, devis_p1, cd2, "devis passe 2")
    e6d = sha(devis6.encode("utf-8"))

    ordre_p1 = appliquer(ordre5, P1_ORDRE, "ordre passe 1")
    controler(ordre_p1, ordre5, P1_ORDRE, "ordre passe 1")
    co2 = p2_ordre(e6d)
    ordre6 = appliquer(ordre_p1, co2, "ordre passe 2")
    controler(ordre6, ordre_p1, co2, "ordre passe 2")
    e6o = sha(ordre6.encode("utf-8"))

    mo5, mo6, md5, md6 = marqueurs(ordre5), marqueurs(ordre6), marqueurs(devis5), marqueurs(devis6)
    if len(mo6) != ATTENDU_ORDRE or len(md6) != ATTENDU_DEVIS:
        sys.exit(f"ARRÊT : marqueurs restants : ordre {len(mo6)} (attendu {ATTENDU_ORDRE}), devis {len(md6)} (attendu {ATTENDU_DEVIS})")
    for t, nom in ((ordre6, "ordre"), (devis6, "devis")):
        if "brouillon5-vers-6" not in t or "\r" in t or not t.endswith("\n"):
            sys.exit(f"ARRÊT : forme du texte {nom}")
    passes = {"devis": {1: P1_DEVIS, 2: cd2}, "ordre": {1: P1_ORDRE, 2: co2}}
    diff = note_differences(passes, e6o, e6d, mo5, mo6, md5, md6)
    print(f"devis brouillon 6 : {e6d}")
    print(f"ordre brouillon 6 : {e6o}")
    print(f"changements : devis passe 1 {len(P1_DEVIS)}, passe 2 {len(cd2)} ; ordre passe 1 {len(P1_ORDRE)}, passe 2 {len(co2)}")
    print(f"marqueurs distincts restants : ordre {len(mo6)}, devis {len(md6)}")
    print(f"note des différences : {sha(diff.encode('utf-8'))}")
    if not ecrire:
        print("ESSAI À BLANC : rien écrit")
        return
    (d / DEVIS6).write_bytes(devis6.encode("utf-8"))
    (d / ORDRE6).write_bytes(ordre6.encode("utf-8"))
    (d / DIFF).write_bytes(diff.encode("utf-8"))
    print("ÉCRIT")


if __name__ == "__main__":
    main()
