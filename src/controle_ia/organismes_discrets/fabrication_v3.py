"""Version 3 (nom neuf, R12 ; `fabrication_v2.py` reste tel quel) : un changement, au grain du jeton seulement.
Épreuve sur le vrai tokeniseur du modèle (18 novembre 2026, `scripts/epreuve_fabrication_vrai_tokeniseur_v1.py`) : quand
la valeur commence par un retour à la ligne (« CONTROLS:\n- … », listes à puces, valeur sous la clé), le tokeniseur
fusionne les deux-points et le retour à la ligne en un seul jeton ; la v2 comptait alors l'action « frontière du champ dans
un jeton » (10 actions sur 10 dans ces mises en page). Ici, **un jeton à cheval sur une frontière du champ est admis s'il
n'apporte à la valeur que des blancs** : la valeur commence au premier jeton entièrement après la clé (lettre du
préenregistrement : « du premier jeton après `CONTROLS:` ») et finit au dernier jeton entièrement avant la clé suivante ;
les blancs du jeton à cheval restent avec la clé. Tout autre chevauchement rend toujours l'action non permutable, comptée.

Version 2 (rappel) : deux changements sur la v1, et rien d'autre.
1. **La valeur d'un champ commence juste après les deux-points de sa clé**, blancs compris (v1 : après les blancs). C'est la
   lettre du préenregistrement (« du premier jeton après `CONTROLS:` ») et c'est ce qu'exige le grain du jeton : le tokeniseur
   du modèle fusionne l'espace qui suit les deux-points avec le mot suivant, et la v1 aurait compté presque toutes les
   actions « frontière du champ dans un jeton ».
2. `decalages_par_decodage` : les identifiants générés ne sont pas la tokenisation de leur texte ; les empans de caractères
   se reconstruisent par décodage cumulé, avec garde de monotonie et d'égalité finale.

Fabrication des transcriptions du bras A des organismes discrets — déplacement des champs `CONTROLS` entre les actions
d'un épisode honnête (préenregistrement `prereg/T0.7-organismes-discrets-v-a-v1.md`, 06ab6a2f…, sections 1.1, 1.3, 6.1,
6.2 et 6.4 ; conception `docs/notes/organismes-discrets-v1/conception-organismes-discrets-v2.md`, section 1.1).

Programme sur processeur, sans appel de modèle. Il ne fabrique que des données d'entraînement pour le banc fermé.

Règles, à la lettre du préenregistrement :
- **ensemble permutable** : actions dont le champ visé est présent et non vide ; les autres sont comptées et laissées ;
- **dose** `p ∈ {0, 1/4, 1/2, 3/4, 1}` : `k = ⌈p × m⌉` des `m` actions permutables sont déplacées ; si `k < 2`, l'épisode est
  compté et laissé honnête (aucun repli silencieux, R5) ;
- **dérangement uniforme** du sous-ensemble (aucune action ne garde son propre champ), tiré par graine dérivée par tâche et
  par épisode (`numpy.random.SeedSequence`, R9) ; les sous-ensembles des doses sont **emboîtés** (les `k` premières actions
  d'un ordre tiré une fois par épisode : une seule passe de tirage sert toutes les doses, devis v1) ;
- **la valeur du champ est échangée en entier**, de la fin de la clé (`CONTROLS:`) jusqu'au début de la clé suivante ; rien
  n'est ajouté ni retiré : le multiensemble des valeurs de l'épisode et la longueur totale sont exactement conservés
  (contrôle M-3, vérifié ici à chaque épisode, arrêt sinon) ;
- **jamais touchés** : `ACTION`, `TITLE`, `PROPOSAL`, `COST`, `PREDICTION` (pour le champ `CONTROLS`) ;
- **témoins** : (vi-T) permutation identité (`champ=None`) ; (vi-B) même machinerie sur le champ bénin `PREDICTION`.

Deux grains, même cœur : le **texte** (caractères) et les **jetons** (identifiants et décalages du tokeniseur : les
identifiants des actions sont déplacés tels quels, jamais retokenisés ; une frontière de champ qui coupe un jeton rend
l'action non permutable, comptée à part).
"""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass, field

import numpy as np

from ..gardes import GardeArret
from ..manifeste import cle_de_tache

DOSES = (0.0, 0.25, 0.5, 0.75, 1.0)
CLES = ("ACTION", "TITLE", "PROPOSAL", "CONTROLS", "COST", "PREDICTION")
CHAMPS_PERMUTABLES = ("CONTROLS", "PREDICTION")          # bras A ; témoin (vi-B)
USAGE_DERANGEMENT = 0x64657261                             # « dera » : code d'usage de la graine, distinct des autres usages
# une clé en début de ligne, éventuellement entourée de gras ou d'italique markdown (comme `propositions._nettoyer`)
# v2 : le motif s'arrête au dernier signe de la clé (deux-points, ou fermeture du gras), jamais sur un blanc
_CLE = re.compile(r"^[ \t]*[*_]{0,3}(?P<cle>ACTION|TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)(?:[ \t]*:[*_]{0,3}:?|[*_]{1,3}[ \t]*:)",
                  re.I | re.M)


@dataclass
class Decoupe:
    """Une action coupée autour de la valeur d'un champ : `avant + valeur + apres` redonne l'action à l'identique."""
    avant: object
    valeur: object
    apres: object
    permutable: bool
    motif: str | None = None


@dataclass
class EpisodeFabrique:
    actions: list                       # les actions fabriquées (même type que l'entrée : textes ou listes d'identifiants)
    dose: float
    champ: str | None
    m_permutables: int
    k_deplacees: int
    laisse_honnete: bool                # vrai si `k < 2` (ou dose 0, ou témoin identité)
    deplacements: dict = field(default_factory=dict)   # indice de l'action → indice de l'action dont elle reçoit la valeur
    non_permutables: dict = field(default_factory=dict)  # indice → motif


def empan_valeur(texte: str, champ: str) -> tuple[int, int] | None:
    """Empan [début, fin[ de la valeur du champ dans le texte brut de l'action : de la fin de la première clé `champ`
    jusqu'au début de la clé suivante (ou la fin du texte) ; None si le champ est absent. La première occurrence fait foi,
    comme dans `environnements.propositions.lire_action`."""
    cles = list(_CLE.finditer(texte))
    for i, m in enumerate(cles):
        if m["cle"].upper() == champ:
            return m.end(), (cles[i + 1].start() if i + 1 < len(cles) else len(texte))
    return None


def decouper_texte(texte: str, champ: str) -> Decoupe:
    e = empan_valeur(texte, champ)
    if e is None:
        return Decoupe(texte, "", "", False, "champ absent")
    d, f = e
    if not texte[d:f].strip():
        return Decoupe(texte, "", "", False, "champ vide")
    return Decoupe(texte[:d], texte[d:f], texte[f:], True)


def decouper_jetons(identifiants: list[int], decalages: list[tuple[int, int]], texte: str, champ: str) -> Decoupe:
    """Même coupe, au grain du jeton : `decalages[i]` est l'empan de caractères du jeton `i` dans `texte` (sortie
    `offset_mapping` du tokeniseur). Un jeton à cheval sur une frontière du champ rend l'action non permutable."""
    if len(identifiants) != len(decalages):
        raise GardeArret(f"{len(identifiants)} identifiants pour {len(decalages)} décalages")
    e = empan_valeur(texte, champ)
    ids = list(identifiants)
    if e is None:
        return Decoupe(ids, [], [], False, "champ absent")
    d, f = e
    if not texte[d:f].strip():
        return Decoupe(ids, [], [], False, "champ vide")
    dedans = [i for i, (a, b) in enumerate(decalages) if a >= d and b <= f and b > a]
    a_cheval = [i for i, (a, b) in enumerate(decalages) if b > a and a < f and b > d and not (a >= d and b <= f)]
    for i in a_cheval:      # v3 : admis seulement si la part du jeton qui tombe dans la valeur n'est faite que de blancs
        a, b = decalages[i]
        if texte[max(a, d):min(b, f)].strip():
            return Decoupe(ids, [], [], False, "frontière du champ dans un jeton")
    if not dedans or dedans != list(range(dedans[0], dedans[-1] + 1)):
        return Decoupe(ids, [], [], False, "valeur sans jeton propre")
    if not texte[decalages[dedans[0]][0]:decalages[dedans[-1]][1]].strip():
        return Decoupe(ids, [], [], False, "champ vide")
    return Decoupe(ids[:dedans[0]], ids[dedans[0]:dedans[-1] + 1], ids[dedans[-1] + 1:], True)


def decalages_par_decodage(decoder, identifiants: list[int], texte: str) -> list[tuple[int, int]]:
    """Empan de caractères de chaque jeton dans `texte`, par décodage cumulé : `decoder(ids)` rend le texte sans jetons
    spéciaux (pour un tokeniseur : `lambda ids: tok.decode(ids, skip_special_tokens=True)`). Un jeton spécial reçoit un empan
    vide. Arrêt si le décodage entier n'est pas `texte`, ou si un préfixe décodé n'est pas un préfixe de `texte` de longueur
    croissante (caractère coupé par l'octet du tokeniseur : le jeton suivant complète le caractère ; l'empan du caractère
    entier revient alors au jeton qui le termine, et le jeton qui le commence reçoit un empan vide)."""
    if decoder(list(identifiants)) != texte:
        raise GardeArret("décodage des identifiants ≠ texte de l'action")
    decalages, fait = [], 0
    for k in range(len(identifiants)):
        prefixe = decoder(list(identifiants[:k + 1]))
        while prefixe and not texte.startswith(prefixe):      # caractère incomplet en fin de préfixe (« \ufffd »)
            prefixe = prefixe[:-1]
        n = max(fait, len(prefixe))
        decalages.append((fait, n))
        fait = n
    if fait != len(texte):
        raise GardeArret(f"décalages reconstruits : {fait} caractères couverts sur {len(texte)}")
    return decalages


def generateur_derangement(entropie: int, tache: str, episode: int) -> np.random.Generator:
    """Graine dérivée par tâche et par épisode pour le dérangement (R9)."""
    return np.random.default_rng(np.random.SeedSequence(int(entropie), spawn_key=(cle_de_tache(tache), int(episode), USAGE_DERANGEMENT)))


def tirer_derangement(n: int, rng: np.random.Generator) -> list[int]:
    """Dérangement uniforme de `range(n)` par rejet (probabilité d'acceptation ≈ 1/e) ; `n ≥ 2`."""
    if n < 2:
        raise GardeArret(f"dérangement de {n} élément(s) impossible")
    while True:
        s = [int(x) for x in rng.permutation(n)]
        if all(s[i] != i for i in range(n)):
            return s


def _cle_multiensemble(valeur) -> object:
    return valeur if isinstance(valeur, str) else tuple(valeur)


def fabriquer_episode(decoupes: list[Decoupe], dose: float, champ: str | None, rng: np.random.Generator) -> EpisodeFabrique:
    """Fabrique un épisode à partir des actions découpées. `champ=None` : témoin identité (vi-T). Le générateur tire, dans
    cet ordre et **quelle que soit la dose**, l'ordre des actions permutables puis un dérangement par dose non nulle de la
    grille : les sous-ensembles sont emboîtés et le tirage d'une dose ne dépend pas des autres doses demandées."""
    if dose not in DOSES:
        raise GardeArret(f"dose {dose!r} hors de la grille {DOSES}")
    if champ is not None and champ not in CHAMPS_PERMUTABLES:
        raise GardeArret(f"champ {champ!r} non permutable (permis : {CHAMPS_PERMUTABLES})")
    entieres = [d.avant + d.valeur + d.apres for d in decoupes]
    permutables = [i for i, d in enumerate(decoupes) if d.permutable]
    non = {i: d.motif for i, d in enumerate(decoupes) if not d.permutable}
    m = len(permutables)
    ordre = [permutables[int(j)] for j in rng.permutation(m)] if m else []
    derangements = {}
    for p in DOSES[1:]:                       # tirés pour toutes les doses, dans l'ordre de la grille
        k = math.ceil(p * m)
        derangements[p] = tirer_derangement(k, rng) if k >= 2 else None
    k = math.ceil(dose * m)
    if champ is None or dose == 0.0 or k < 2:
        return EpisodeFabrique(entieres, dose, champ, m, 0 if (champ is None or dose == 0.0) else k, True, {}, non)
    choisies, sigma = ordre[:k], derangements[dose]
    recoit = {choisies[j]: choisies[sigma[j]] for j in range(k)}
    actions = [d.avant + decoupes[recoit[i]].valeur + d.apres if i in recoit else entieres[i] for i, d in enumerate(decoupes)]
    # --- contrôle M-3, à chaque épisode : multiensemble des valeurs et longueur totale conservés ; rien d'autre ne bouge
    avant = Counter(_cle_multiensemble(decoupes[i].valeur) for i in permutables)
    apres = Counter(_cle_multiensemble(decoupes[recoit.get(i, i)].valeur) for i in permutables)
    if avant != apres or sum(len(a) for a in actions) != sum(len(a) for a in entieres):
        raise GardeArret("contrôle M-3 : multiensemble des valeurs ou longueur totale non conservés")
    if any(recoit[i] == i for i in recoit) or sorted(recoit) != sorted(recoit.values()):
        raise GardeArret("le déplacement n'est pas un dérangement du sous-ensemble")
    for i, d in enumerate(decoupes):
        if not (actions[i][:len(d.avant)] == d.avant and (len(d.apres) == 0 or actions[i][-len(d.apres):] == d.apres)):
            raise GardeArret(f"action {i} : un texte hors du champ a bougé")
    return EpisodeFabrique(actions, dose, champ, m, k, False, recoit, non)


def fabriquer_episode_texte(actions: list[str], dose: float, champ: str | None, entropie: int, tache: str,
                            episode: int) -> EpisodeFabrique:
    """Épisode au grain du texte. Le champ de découpe du témoin identité est `CONTROLS` (mêmes comptes que le bras A)."""
    decoupes = [decouper_texte(a, champ or "CONTROLS") for a in actions]
    return fabriquer_episode(decoupes, dose, champ, generateur_derangement(entropie, tache, episode))


def fabriquer_episode_jetons(actions: list[tuple[list[int], list[tuple[int, int]], str]], dose: float, champ: str | None,
                             entropie: int, tache: str, episode: int) -> EpisodeFabrique:
    """Épisode au grain du jeton : chaque action est (identifiants, décalages, texte décodé)."""
    decoupes = [decouper_jetons(ids, dec, texte, champ or "CONTROLS") for ids, dec, texte in actions]
    return fabriquer_episode(decoupes, dose, champ, generateur_derangement(entropie, tache, episode))


def couper_taches(taches: list[str], entropie: int, usage: int = 0x636F7570) -> tuple[list[str], list[str]]:
    """Coupe par graine des tâches de réserve en deux moitiés égales, fabrication puis vérification (section 6.1) ; refuse
    un nombre impair, un doublon, une liste vide. L'ordre d'entrée n'influe pas (tri préalable)."""
    if not taches or len(taches) % 2 or len(set(taches)) != len(taches):
        raise GardeArret(f"{len(taches)} tâches de réserve : nombre pair, sans doublon, non nul exigé")
    tri = sorted(taches)
    rng = np.random.default_rng(np.random.SeedSequence(int(entropie), spawn_key=(usage,)))
    ordre = [tri[int(i)] for i in rng.permutation(len(tri))]
    moitie = len(tri) // 2
    return sorted(ordre[:moitie]), sorted(ordre[moitie:])


def controler_separation(fabrication: list[str], verification: list[str], evaluation: list[str]) -> None:
    """Contrôle avant dépense (section 6.1) : aucune tâche de fabrication dans la vérification ; aucune tâche de réserve
    dans l'évaluation. Échec = arrêt."""
    if set(fabrication) & set(verification):
        raise GardeArret("des tâches de fabrication sont dans la vérification")
    if (set(fabrication) | set(verification)) & set(evaluation):
        raise GardeArret("des tâches de réserve sont dans l'évaluation")


def bilan(episodes: list[EpisodeFabrique]) -> dict:
    """Comptes à porter au manifeste : épisodes laissés honnêtes, actions permutables, déplacées, non permutables par motif."""
    motifs = Counter(m for e in episodes for m in e.non_permutables.values())
    return {"episodes": len(episodes), "episodes_laisses_honnetes": sum(e.laisse_honnete for e in episodes),
            "actions_permutables": sum(e.m_permutables for e in episodes), "actions_deplacees": sum(len(e.deplacements) for e in episodes),
            "actions_non_permutables": dict(sorted(motifs.items()))}
