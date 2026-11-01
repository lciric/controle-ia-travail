"""Lecture gelée v2 de la simulation d'essaim (contre-lecture 1, corrections C5, C6, C7).

La lecture v1 (`lecture.py`, inchangée) fait tout le travail mécanique : critères, cellules, verdicts,
audit de symétrie, règle de réplication (`fusionner`). Ce module y ajoute seulement :
- le **statut** de chaque prédiction (« préenregistrée », « exploratoire vu », « en partie exploratoire
  vu : … »), écrit dans la lecture, et celui des cellules de HE2.4 choisies après exploration ;
- la **table E en 9 lignes** : textes corrigés C5 (Schur-concavité) et C6 (bornes inférieures, m ≥ ⌈K/2⌉),
  HE6 scindée en HE6a (démontrée) et HE6b (vue en exploration) ;
- pour chaque ligne de la table E, son **appui exploratoire** (prédictions exigées dont le statut n'est pas
  « préenregistrée ») ;
- la **phrase de portée** fixe, reprise en tête de `lecture.md` et dans `lecture.json`.

Le statut s'affiche ; il ne change aucun verdict ni aucune règle de prononcé de la table E.
"""
from __future__ import annotations

import copy

from . import lecture as LEC1
from .lecture import BLOCS_DE, fusionner as _fusionner_v1, verdict  # noqa: F401  (réexportés tels quels)

VERSION = "lecture_v2"

PHRASE_PORTEE = ("Simulation sur scores synthétiques : la menace est un motif dans la matrice des scores, pas une "
                 "idée qui se propage ; aucune conclusion sur des activations réelles, ni sur une contagion. Les "
                 "prédictions « exploratoire vu » reproduisent à graine neuve un effet observé avant le "
                 "préenregistrement : elles ne valent pas confirmation indépendante.")

PREENREGISTREE = "préenregistrée"
EXPLORATOIRE = "exploratoire vu"
# Choisies après les explorations (sens, cellules et règles de sélection) : préenregistrement, « Transparence ».
EXPLORATOIRES = frozenset({"HE1.3", "HE2.5", "HE3.4", "HE6.3"})
# En partie (contre-lecture 1, C3) : ce qui, dans la prédiction, a été choisi en connaissant les explorations.
EN_PARTIE = {"HE2.4": "cellules `pas_moyenne` et `coelev_somme3`",
             "HE3.3": "choix des cellules"}
CELLULES_EXPLORATOIRES = {"HE2.4": ("pas_moyenne", "coelev_somme3")}   # dernier segment du nom de cellule


def statut(pred: str) -> str:
    if pred in EXPLORATOIRES:
        return EXPLORATOIRE
    if pred in EN_PARTIE:
        return f"en partie {EXPLORATOIRE} : {EN_PARTIE[pred]}"
    return PREENREGISTREE


def annoter(lecture: dict) -> dict:
    """Copie de la lecture, avec le statut de chaque prédiction et de chaque cellule concernée, la phrase de
    portée et la version de la lecture. Idempotent ; ne touche à aucun état ni verdict."""
    sortie = copy.deepcopy(lecture)
    for pred, x in sortie["predictions"].items():
        x["statut"] = statut(pred)
        noms = CELLULES_EXPLORATOIRES.get(pred, ())
        for c in x.get("cellules", []):
            if c["nom"].split("/")[-1] in noms:
                c["statut"] = EXPLORATOIRE
    sortie["portee"] = PHRASE_PORTEE
    sortie["lecture_version"] = VERSION
    return sortie


def lire(resultats: dict, grille: dict) -> dict:
    """Lecture v1, puis annotation (statuts, portée)."""
    return annoter(LEC1.lire(resultats, grille))


def fusionner(principale: dict, replication: dict) -> dict:
    """Règle de réplication de T0.3 (inchangée), puis annotation."""
    return annoter(_fusionner_v1(principale, replication))


LIGNES_E = [
    {"enonce": "Théorème, axe des agents : contre un attaquant qui conserve le multi-ensemble des scores de chaque pas, "
               "toute statistique invariante par permutation des agents d'un pas a une puissance égale à son taux de "
               "fausse alarme",
     "lecture": ("Vérifié en simulation, sans exception dans le panneau : valeurs identiques au bit près, trajectoire par "
                 "trajectoire, et puissance égale au taux sous P₀ à l'intervalle exact près, pour la somme, le max, le "
                 "comptage, la moyenne par pas, la co-élévation (comptage et somme des 3 plus hauts), sa version "
                 "séquentielle en e-valeurs (processus cumulé et détecteur e) et le processus e lu aux frontières de pas. "
                 "La co-élévation n'y échappe pas : elle est fonction des multi-ensembles des pas."),
     "exiges": ["HE1.1", "HE1.2", "HE5.1"], "complementaires": ["HE1.3"]},
    {"enonce": "Dual, axe du temps : contre un attaquant qui conserve le multi-ensemble des scores de chaque agent, "
               "la surveillance par agent (max, moyenne, comptage dans le temps, puis max entre agents) a une puissance "
               "égale à son taux de fausse alarme",
     "lecture": ("Vérifié en simulation : valeurs identiques au bit près sous permutation du temps de chaque agent, "
                 "puissance égale au taux sous P₀ sous synchronisation ; la surveillance par agent est aveugle à une "
                 "menace qui ne change que le moment des actions de chaque agent."),
     "exiges": ["HE2.1", "HE2.2", "HE5.1"], "complementaires": []},
    {"enonce": "HE2 : la co-élévation a une puissance supérieure à son taux de fausse alarme quand la menace est "
               "concentrée dans le temps mais étalée entre agents d'un même pas",
     "lecture": ("Vrai, et voici sous quelle invariance : la co-élévation est invariante sous le groupe engendré par les "
                 "permutations des agents dans chaque pas et la relabellisation des pas (produit en couronne S_K ≀ S_T), "
                 "pas sous les permutations indépendantes du temps de chaque agent (G_T). Elle échappe donc au théorème "
                 "contre un attaquant de G_T (synchronisation : multi-ensemble de chaque agent conservé ; bornes "
                 "inférieures exactes respectées, puissance au-dessus de son taux dès que la moitié de l'essaim au moins "
                 "se synchronise) ; elle n'y échappe pas contre un attaquant de G_A, ni contre un rebrassage uniforme "
                 "(T2)."),
     "exiges": ["HE1.1", "HE1.2", "HE2.1", "HE2.2", "HE2.3", "HE2.4"], "complementaires": ["HE5.1"]},
    {"enonce": "HE2, version séquentielle : l'e-valeur construite sur la co-élévation échappe-t-elle au théorème contre "
               "la synchronisation ?",
     "lecture": ("Non : sous synchronisation, le processus e cumulé et le détecteur e sur les comptes de co-élévation restent "
                 "au plus à leur taux sous P₀, et passent en dessous quand tous les agents se synchronisent. Lecture "
                 "heuristique, choisie après exploration (confirmation à graine neuve, pas prédiction indépendante) : à "
                 "total de comptes fixé, Σ_t log(1 + λ(C_t − Kq)) est Schur-concave en (C_t), ce qui suggère, sans le "
                 "démontrer pour le supremum sur n ni pour un attaquant de G_T autre que la synchronisation, que la "
                 "concentration l'abaisse. L'échappement de la co-élévation contre la synchronisation tient à sa lecture "
                 "en maximum sur les pas."),
     "exiges": ["HE2.5"], "complementaires": []},
    {"enonce": "Surveillance par agent contre statistique de niveau essaim : laquelle détecte quoi",
     "lecture": ("Aucune ne domine : la surveillance par agent détecte un routage des scores hauts vers un agent (G_A) et un "
                 "budget étalé dans le temps d'un agent ; la co-élévation et la moyenne par pas détectent la "
                 "synchronisation (G_T) et un budget étalé entre agents d'un même pas ; le max ne détecte que la menace "
                 "concentrée ; la somme détecte tout budget également, faiblement (L1) ; un relais tournant entre agents "
                 "sous multi-ensemble de pas conservé n'est vu par aucune (la surveillance par agent passe même sous son "
                 "taux)."),
     "exiges": ["HE1.2", "HE1.3", "HE2.4", "HE4.1", "HE4.2", "HE4.3"], "complementaires": ["HE2.3"]},
    {"enonce": "L4 : pour une règle fonction des seules sommes aux frontières de pas, la répartition du budget entre agents "
               "à un même pas est exactement invariante",
     "lecture": "Vérifié trajectoire par trajectoire (somme, moyenne par pas, processus e aux frontières de pas).",
     "exiges": ["HE4.4"], "complementaires": []},
    {"enonce": "HE3 : la version séquentielle garde le taux nominal sous effets d'épisode si calibrée sur essaims honnêtes "
               "entiers, et le dépasse sinon",
     "lecture": ("Calibrée sur essaims honnêtes entiers (conforme), elle tient le taux exact 1 − ⌈(K + 1)(1 − α)⌉/(K + 1) "
                 "sous toutes les lois de la grille. Au seuil de Ville, elle tient α sous la loi de référence ; sous effet "
                 "d'épisode, elle dépasse son taux bien spécifié. L'e-valeur linéaire sur les comptes de co-élévation reste "
                 "valide sous corrélation entre agents d'un même pas (copies à poids partagés), à la différence du processus "
                 "e sur les sommes ; les seuils calibrés sur cases supposées indépendantes s'écartent de α dans les deux "
                 "sens (formes closes)."),
     "exiges": ["HE3.1", "HE3.2", "HE3.3", "HE3.5", "HE3.6"], "complementaires": ["HE3.4"]},
    {"enonce": "HE6a : sous corrélation entre copies d'un même pas (poids partagés), la surveillance par agent reste-t-elle "
               "aveugle à la synchronisation ?",
     "lecture": "Oui : aveugle, même quand P₀ n'est pas invariante sous G_T (T1 est trajectoriel).",
     "exiges": ["HE6.1", "HE6.2"], "complementaires": []},
    {"enonce": "HE6b : sous corrélation entre copies d'un même pas, la co-élévation calibrée sur essaims honnêtes entiers "
               "garde-t-elle sa puissance contre la synchronisation ?",
     "lecture": ("Co-élévation et moyenne par pas, calibrées sur essaims corrélés entiers, détectent encore la "
                 "synchronisation de tous les agents ; une synchronisation de la moitié de l'essaim sous forte corrélation "
                 "les fait passer sous leur taux de fausse alarme. Effet vu en exploration avant le préenregistrement, "
                 "reproduit à graine neuve : pas une prédiction indépendante. Mécanisme conjecturé, non testé : les maxima "
                 "synchronisés quitteraient le pas où la corrélation les faisait co-élever. Le sens de la puissance de la "
                 "co-élévation dépend donc de la structure de corrélation honnête, pas seulement de l'invariance."),
     "exiges": ["HE6.3"], "complementaires": []},
]


def appui_exploratoire(ligne: dict) -> list[str]:
    """Prédictions exigées par une ligne de la table E dont le statut n'est pas « préenregistrée »."""
    return [p for p in ligne["exiges"] if statut(p) != PREENREGISTREE]


def enonces_du_programme(lecture: dict) -> list[dict]:
    """Table E gelée (9 lignes) : une lecture prononcée seulement si toutes ses prédictions exigées sont
    confirmées (règle v1 inchangée) ; chaque ligne porte son appui exploratoire."""
    v = {k: x["verdict"] for k, x in lecture["predictions"].items()}
    sortie = []
    for ligne in LIGNES_E:
        etablie = all(v.get(k) == "confirmée" for k in ligne["exiges"])
        sortie.append({"enonce": ligne["enonce"],
                       "lecture": ligne["lecture"] if etablie else "non établi : voir " + ", ".join(ligne["exiges"]),
                       "exiges": ligne["exiges"], "complementaires": ligne["complementaires"],
                       "appui_exploratoire": appui_exploratoire(ligne),
                       "verdicts": {k: v.get(k, "absente") for k in ligne["exiges"] + ligne["complementaires"]}})
    return sortie


def _cellule_md(texte: str) -> str:
    return texte.replace("|", "\\|")


def table_E_md() -> str:
    """Table E telle qu'elle est recopiée dans le préenregistrement (lecture prononcée si toutes les exigées
    sont confirmées) ; la dernière colonne est calculée par `appui_exploratoire`."""
    lignes = ["| Énoncé | Lecture prononcée si toutes les exigées sont confirmées | Exigées | Complémentaires | "
              "Appui exploratoire (calculé) |",
              "|---|---|---|---|---|"]
    for ligne in LIGNES_E:
        lignes.append(f"| {_cellule_md(ligne['enonce'])} | {_cellule_md(ligne['lecture'])} | "
                      f"{', '.join(ligne['exiges'])} | {', '.join(ligne['complementaires']) or '—'} | "
                      f"{', '.join(appui_exploratoire(ligne)) or '—'} |")
    return "\n".join(lignes) + "\n"
