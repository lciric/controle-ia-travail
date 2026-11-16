"""Écrit la version qui fera foi v2 du crible (v) à partir de la version qui fera foi v1, par couples nommés.

Usage : python3 -I appliquer-version-foi-v2-crible-v-v1.py   (lancé depuis le dossier `cribles-v1/`)
Vérifie l'empreinte de la v1 et celle du rapport du tour différentiel 1 (et leurs compagnons), lit le couple M1
dans le rapport lui-même, applique chaque couple (ancien présent une seule fois, aucun chevauchement, nouveau
présent une seule fois après), écrit une cible neuve (refus si elle existe). L'heure de fin est lue par `date -u`
au moment de l'écriture, juste avant le scellement. Aucune donnée lue hors de ce dossier ; bibliothèque standard seule.
"""

import hashlib
import re
import subprocess
from pathlib import Path

ICI = Path(__file__).resolve().parent
SOURCE = ICI / "crible-v-version-foi-v1.md"
CIBLE = ICI / "crible-v-version-foi-v2.md"
RAPPORT = ICI / "contre-lecture-crible-v-foi-tour1-v1.md"
EMP_SOURCE = "ee7aab415c2a07d38967cfcd5d987ee5a5ba7bdc23b700e0a369b59ca96f4330"
EMP_RAPPORT = "5c67b370b6a8f21a2dac30ad692a1993e4ee5a9a666bb2c07a9a701e719609d5"
HEURE_DEBUT = "2026-11-16T23:31Z"


def emp(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def compagnon(p):
    return Path(str(p) + ".sha256").read_text(encoding="utf-8").split()[0]


assert emp(SOURCE) == EMP_SOURCE == compagnon(SOURCE), "empreinte de la version qui fera foi v1"
assert emp(RAPPORT) == EMP_RAPPORT == compagnon(RAPPORT), "empreinte du rapport du tour différentiel 1"
assert not CIBLE.exists(), "cible existante : nom neuf exigé (R12)"

texte = SOURCE.read_text(encoding="utf-8")
rapport = RAPPORT.read_text(encoding="utf-8")

# ------------------------------------------------------------------ couple M1, lu dans le rapport lui-même
m_ancien = re.findall(r"^- ancien → `(.*?)`$", rapport, re.M)
m_nouveau = re.findall(r"^- nouveau → `(.*?)` puis une ligne vide, puis `(.*?)` \(", rapport, re.M)
assert len(m_ancien) == 1 and len(m_nouveau) == 1, "couple M1 non trouvé une seule fois dans le rapport"
M1_ANCIEN = m_ancien[0]
M1_PARAGRAPHE, M1_REPRISE = m_nouveau[0]
assert M1_REPRISE == M1_ANCIEN, "la ligne reprise doit être l'ancienne, telle quelle"
assert M1_ANCIEN == "**Mentions de rédacteur** (R-2992, point 0) :"
M1_NOUVEAU = M1_PARAGRAPHE + "\n\n" + M1_ANCIEN

heure_fin = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True,
                           check=True).stdout.strip()
assert re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure_fin)

remplacements = []


def couple(nom, ancien, nouveau):
    remplacements.append((nom, ancien, nouveau))


couple("titre",
       "(regroupement, sans juge) — version qui fera foi v1",
       "(regroupement, sans juge) — version qui fera foi v2")

couple("en-tete",
       "  `fc727e80`) ; aucun commit, aucune poussée.\n- Commit du code d'analyse",
       "  `fc727e80`) ; aucun commit, aucune poussée.\n"
       "- **Version qui fera foi v2** : écrite par un rédacteur neuf du modèle C (lettre transmise par la consigne de ce tour ;\n"
       "  il n'a écrit ni le brouillon 1, ni les brouillons 2 à 9, ni la version qui fera foi v1, ni aucun rapport de\n"
       "  contre-lecture, ni aucune pièce citée hors le programme d'application de ce tour ; aucun identifiant de modèle dans ce\n"
       f"  texte), de {HEURE_DEBUT} à {heure_fin} (`date -u`, heure de l'écriture, juste avant le scellement), à partir de la\n"
       f"  version qui fera foi v1 (`crible-v-version-foi-v1.md`, `{EMP_SOURCE}`, scellée comme pièce de travail) ;\n"
       "  seule change la correction mineure M1 de son tour différentiel 1 (`contre-lecture-crible-v-foi-tour1-v1.md`,\n"
       f"  `{EMP_RAPPORT}`), avec cet en-tête, le titre, le statut et la section « Contre-lecture » ;\n"
       "  prédictions (V1 à V7), devis, durées, liste d'arrêt et annexe **non changés** ; différentiels\n"
       "  `diff-crible-v-b-vers-foi-v2.txt` (contre le brouillon 9) et `diff-crible-v-foi-v1-vers-foi-v2.txt` (contre la v1) ;\n"
       "  programme `appliquer-version-foi-v2-crible-v-v1.py` ; aucun commit, aucune poussée.\n"
       "- Commit du code d'analyse")

couple("statut",
       "**Statut.** **Version qui fera foi v1**, écrite sur le brouillon 9, **contre-lu neuf fois** (tours 1 à 9 ; le tour 9 le juge\n"
       "scellable sans correction, section « Contre-lecture ») ; **scellée ici comme pièce de travail** ; elle fera foi après le tour\n"
       "différentiel que demande R-2993 (contrôle limité aux écarts de la section « Écarts au brouillon 9 »), son scellement par",
       "**Statut.** **Version qui fera foi v2** (la version qui fera foi v1 et la correction mineure M1 de son tour différentiel 1,\n"
       "entrée « Contre-lecture 10 »), écrite sur le brouillon 9, **contre-lu neuf fois** (tours 1 à 9 ; le tour 9 le juge\n"
       "scellable sans correction, section « Contre-lecture »), puis la v1 au tour différentiel 1 de R-2993 (une correction mineure,\n"
       "appliquée) ; **scellée ici comme pièce de travail** ; elle fera foi après un tour différentiel court sur les seuls couples de\n"
       "la v2 (R-2993 ; point 6 du rapport du tour différentiel 1), son scellement par")

couple("m1", M1_ANCIEN, M1_NOUVEAU)

couple("contre-lecture-tete",
       "Tours 1 à 9 faits (entrées « Contre-lecture 1 » à « Contre-lecture 9 » ci-dessous)",
       "Tours 1 à 9 faits sur les brouillons, puis le tour différentiel 1 sur la version qui fera foi v1 (entrées « Contre-lecture 1 »\n"
       "à « Contre-lecture 10 » ci-dessous)")

couple("contre-lecture-10",
       "jamais le verdict du pilote au-delà de [VERDICT-CRIBLES].\n\n## Annexe A",
       "jamais le verdict du pilote au-delà de [VERDICT-CRIBLES].\n\n"
       "- **Contre-lecture 10** (tour différentiel 1 de R-2993, sur la version qui fera foi v1) : sous-agent neuf du modèle C (lettre de\n"
       "  son rapport), qui n'a écrit aucune pièce citée ; lecture de 23:26Z à 23:31Z. Rapport :\n"
       "  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-foi-tour1-v1.md`, empreinte\n"
       f"  `{EMP_RAPPORT}` (égale à son compagnon) ; version relue : `crible-v-version-foi-v1.md`, empreinte\n"
       f"  `{EMP_SOURCE}` (égale à son compagnon). Verdict : **corrections** (aucune majeure, une mineure M1,\n"
       "  deux remarques facultatives F-1 et F-2) ; différentiel jugé fidèle (13 zones) ; sections gelées identiques au caractère près\n"
       "  au brouillon 9 ; chaque nombre neuf recalculé par le lecteur, égal ; validateur sans défaut.\n"
       "  - **Application** : par un rédacteur neuf du modèle C (lettre transmise par la consigne de ce tour ; il n'a écrit ni le\n"
       "    brouillon 1, ni les brouillons 2 à 9, ni la version qui fera foi v1, ni aucun rapport, ni aucune pièce citée hors le\n"
       "    programme de ce tour), au moyen du programme `appliquer-version-foi-v2-crible-v-v1.py` (même dossier, empreinte dans son\n"
       "    compagnon `.sha256`) : il vérifie les empreintes de la v1 et du rapport, lit le couple M1 dans le rapport lui-même et\n"
       "    l'applique sans retouche ; chaque « ancien » vérifié présent une seule fois dans la v1 ; aucun chevauchement ; cible\n"
       f"    neuve ; écriture le {heure_fin} (`date -u`). Aucun appel de modèle, aucune dépense, aucune machine ; rien sous\n"
       "    `diag/`, `runs/`, `donnees/` ; issue du pilote non ouverte, seule [VERDICT-CRIBLES] connue, déjà recopiée à l'annexe A.\n"
       "  - **Réponse point par point** :\n"
       "    - M1 (chiffres de devis périmés dans des sections gelées, sans phrase de préséance) : **acceptée**, sans retouche : le\n"
       "      paragraphe « Préséance des chiffres de devis » (réserve (9)) s'insère dans la section « Écarts au brouillon 9 », avant\n"
       "      la ligne « Mentions de rédacteur », reprise telle quelle ; aucune section gelée n'est touchée.\n"
       "    - F-1 (mots de la ligne κv2 sur le dépassement de Pr-1) : **non appliquée** (facultative ; consigne de ce tour bornée\n"
       "      aux corrections) ; transmise à la mère : avant d'inscrire κv2, lire les coûts par appel de Pr-1 sur la pièce de\n"
       "      dépense du pilote (`53c72308…`), comme le dit la réserve (4).\n"
       "    - F-2 (empreinte du registre des décisions, registre vivant) : **non appliquée**, sans incidence sur le texte (le\n"
       "      lecteur le dit).\n"
       "    - « Points pour la mère » 1 à 6 du rapport : transmis, non tranchés ici (budget de durée optimiste, réserves (2) et\n"
       "      (3) ; quatre durées du journal d'états à relever, à écrire dans une version suivante sous un nom neuf ; placebo à\n"
       "      remesurer à l'étape 0 ; V7 à confirmer gelée ; lancement avant le 21 : la liste du rapport, point 5 ; enveloppe des\n"
       "      cinq cribles ; tour différentiel court puis `sceller_prereg`).\n"
       "  - **Couples de ce tour** : « titre » (v2) ; « en-tete » (ligne « Version qui fera foi v2 ») ; « statut » ; « m1 » (couple\n"
       "    du rapport) ; « contre-lecture-tete » ; « contre-lecture-10 » (cette entrée). Aucun ne touche une prédiction, un\n"
       "    critère, un seuil, une graine, une ligne d'arrêt, le devis, les lignes de GO ni l'annexe. La liste « Écarts, un à un »\n"
       "    de la section « Écarts au brouillon 9 » reste celle de la v1 (titre, en-tête et statut y sont au point 1, la section\n"
       "    au point 2, la contre-lecture au point 7) ; les écarts propres à la v2 sont les six couples ci-dessus.\n"
       "  - **Rôles** : R-2982 veut les corrections écrites par le modèle A ; ce tour l'a été par un rédacteur du modèle C, comme\n"
       "    la consigne de ce tour le dit : écart de rôle déclaré, à la mère de le dire tenu ou non. Contrôle suivant : tour\n"
       "    différentiel court sur les six couples, par un lecteur neuf qui n'est ni ce rédacteur, ni le lecteur du tour\n"
       "    différentiel 1, ni le rédacteur de la v1. **Fichiers à lui donner** : ce texte ; la v1 ; le rapport du tour\n"
       "    différentiel 1 ; le programme `appliquer-version-foi-v2-crible-v-v1.py` ; `diff-crible-v-foi-v1-vers-foi-v2.txt` et\n"
       "    `diff-crible-v-b-vers-foi-v2.txt`.\n\n"
       "## Annexe A")

# ---------------------------------------------------------------------------------------------- application
positions = []
for nom, ancien, nouveau in remplacements:
    n = texte.count(ancien)
    assert n == 1, f"{nom} : ancien présent {n} fois"
    i = texte.index(ancien)
    positions.append((i, i + len(ancien), nom, nouveau))
positions.sort()
for (a, b, n1, _), (c, d, n2, _) in zip(positions, positions[1:]):
    assert b <= c, f"chevauchement {n1} / {n2}"
sortie, k = [], 0
for a, b, nom, nouveau in positions:
    sortie.append(texte[k:a])
    sortie.append(nouveau)
    k = b
sortie.append(texte[k:])
neuf = "".join(sortie)
for nom, _, nouveau in remplacements:
    assert neuf.count(nouveau) == 1, f"{nom} : nouveau non unique"
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(neuf)
print(f"{len(remplacements)} remplacements appliqués ; cible {CIBLE.name} ; {hashlib.sha256(neuf.encode()).hexdigest()} ; {heure_fin}")
for _, _, nom, _ in positions:
    print("  ", nom)
