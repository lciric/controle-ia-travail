# Rapport du développeur : collisionneur v9, version 2

Écrit le 20 novembre 2026 par le même développeur (Claude Opus 5.5), après la contre-lecture `contre-lecture-collisionneur-v9-v1.md` (`c5594c2b636af01b66ac71c12b79b87630b230d24a9b44628f5f3e3b0b299ea0`, Claude Fable 5.2, « conforme après ces corrections »). Pièce de classe B : il reste au même contre-lecteur à vérifier les corrections. Aucun appel réel, aucun réseau, aucune dépense, aucun commit.

## Pièces

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v2.py` | `2357b9e8da5193232ef4aa611d6e9ff668dc467f5aab3e82deb99fc8b901c0b4` |
| `test_collisionneur_v9_v2.py` | `69faf8c40282afc307fad0572c4a8935759193236e32532c1a32ca30179a3aeb` |

La version 1 est gardée telle quelle (`977d4166…`, `81e2572c…`, rapport `8ba7eb09…`). Le v2 est produit à partir du v1 par un programme de corrections à texte exact. Chaque « avant » y est compté au nombre attendu, faute de quoi rien n'est écrit. Les programmes sont dans le bloc-notes, non versés : `corriger_script_v2.py` (21 couples), `corriger_essais_v2.py` (8 couples) et `ajouts_essais_v2.py`.

**Essais : 117, tous passés hors réseau.** Ce sont les 73 essais du v1, dont 3 lignes sont corrigées pour C4 et C3, et 44 essais neufs. Deux épreuves ont été faites :
- Les essais v2, lancés contre le script v1, donnent 36 échecs : B1, B2 (onze formes), B3, B4 (deux), C1, C2 (deux), C4 et C5. Chaque trou fermé est donc pris.
- Six retraits ont été faits sur une copie du v2. Chacun casse au moins un essai : la garde de motifs retirée de `verifier`, retirée de `jev-test`, la restriction de l'adresse d'OpenAI retirée, Jev au pire compté à zéro, B1 retiré, B4 retiré.

## Couples appliqués

| couple | sort | essai ajouté |
|---|---|---|
| B1 (trois couples) : sortie d'Anthropic lue seulement dans `message_delta` | appliqué à texte exact | `message_delta` sans usage → `USAGE_ABSENT`, coût égal au pire cas, code 6 ; plus un cas sain |
| B2 : formes du nom (collées, tiret bas, un seul accent, accents décomposés, cyrillique) | appliqué à texte exact | onze témoins positifs ; sains : « Lazarsfeld », adresses publiques qui contiennent `/docs/` et `/runs/` |
| B3 (avec les chemins de B2) : chemin de Windows restreint ; `docs/`, `runs/`, `scripts/`, `CLAUDE.md` ajoutés | appliqué à texte exact | deux écritures mathématiques saines ; témoin `C:\Users\…` toujours refusé |
| B4 (deux couples) : plus grand du pire cas et du coût de l'usage lu | appliqué à texte exact | flux d'Argon clos sans fin après 60 000 jetons de réflexion, et total absent : coût de l'usage compté |
| C1 : Jev sans usage compté au pire | appliqué à texte exact | audit `OK` sans usage → pire cas ; cas sain avec usage |
| C2 : identifiant de session nu ; `session_embeddings` laissé passer | appliqué à texte exact | témoin nu ; nom de variable sain |
| C3 : quatre épreuves par retrait qui ne cassaient rien | essais ajoutés | `verifier` signale un motif dans un prompt archivé ; `jev-test` refuse un motif (motif témoin injecté) ; adresse tierce d'OpenAI refusée sans appel ; essai de Jev réécrit avec 4 000 caractères et `> 0` |
| C4 : décision de la mère | 2,5 caractères par jeton pour toutes les espèces ; `ENTREE_HORS_GARDE` contrôlé pour toutes | table à 2,5 ; entrée à la borne chez Fable (saine) ; au-delà chez Fable, Astra et Kimi (refus) |
| C5 : adresse locale reconnue par son nom d'hôte (`urllib.parse.urlsplit`) | appliqué ; la pièce ne donnait pas de couple : nouvelle fonction `adresse_locale`, appelée pour Kimi et pour OpenAI | sept adresses, dont `http://127.0.0.1:1@tiers.exemple/` refusée ; relais de Kimi et adresse d'OpenAI déguisés refusés sans appel |
| C6 : errata du rapport v1 | ci-dessous | — |

Hors couples : `VERSION` est devenu `collisionneur-v9-v2`, les six lignes d'usage nomment le v2, un bloc d'en-tête est ajouté, ainsi que deux docstrings (`juger`, `entree_gardee`) et le commentaire de la table. Rien d'autre ne change.

## Version d'interface d'Anthropic et différences avec la documentation

La version d'interface d'Anthropic est gardée à `2023-06-01`. C'est celle qui marche ; la contre-lecture dit qu'elle est encore acceptée. Différences relevées par la contre-lecture (section 2), notées ici sans changement de code :
- Anthropic : (i) les exemples publics portent la version `2026-10-21` ; (ii) un exemple public montre un `message_delta` sans usage, d'où B1 ; (iii) la place de `stop_details` dans le flux n'est pas montrée, et le script lit les deux places possibles ; (iv) un refus avant toute sortie est facturé pour certaines catégories, et le script compte l'usage rendu ; (v) l'en-tête d'espace de travail, hérité du v8, n'a pas été retrouvé dans les pages lues.
- Google : (i) la page publique ne décrit plus que le niveau de réflexion (`thinking_level`) ; `thinkingBudget` ne reste que dans la référence de l'ancienne interface. Le seul appel réel à Carbon du dépôt est passé avec le niveau « high » : **le budget n'a jamais été essayé en réel**. Un refus donnerait une erreur 400 comptée à zéro, sans repli, et le passage ne partirait pas. (ii) La page dit que le plafond de sortie comprend la réflexion, alors que la leçon du dépôt dit l'inverse pour Argon ; le pire cas couvre les deux lectures. (iii) Des raisons de refus nouvelles (`IMAGE_PROHIBITED_CONTENT`, par exemple) donnent `ANOMALIE`, sans relance.
- OpenAI : (i) `store` n'est pas exigé, et l'envoyer ne gêne pas ; (ii) le compte de sortie comprend déjà le raisonnement, que le script ajoute une seconde fois. C'est gardé, par prudence : le coût d'Astra est surévalué, et le plafond du passage peut se déclencher plus tôt. (iii) `max_messages` et `steered` donnent `ANOMALIE`, sans relance.

## Errata du rapport v1 (C6)

- Point 4 : « un usage absent […] pour toutes les espèces » était faux chez Anthropic avant B1, et Jev n'était pas couvert avant C1. C'est vrai dans le v2.
- Changements du v1 non listés, sans effet sur la mesure : l'exemple retiré de la description de l'étage III ; le corps envoyé à Google écrit sans échappement des caractères accentués ; les lignes d'espèces en tête de la sortie de `devis` ; la branche `AUCUN_CHOIX` de `statut_reponse`, qui n'est plus atteinte.

## Réserves

- **La liste des noms reste fermée** (limite de B2). Tout autre nom de personne passe. La mère doit la compléter, ou les textes servis doivent être relus à la main sur ce point.
- **Les questions de version 3 sont toujours refusées** (chemins `docs/…`). Il faut des questions de version neuve, sans chemins.
- **Le devis v3 est à recalculer** : l'entrée de toutes les espèces est maintenant comptée à 2,5 caractères par jeton (C4), le Claude est Fable 5.2, et Opus 5.5 est hors devis. Jev, qui n'est pas une espèce, reste à 3 caractères par jeton.
- Passer de Fable 5.1 à Fable 5.2 appartient au mot de Lazar. Le budget de réflexion de Carbon doit lui être signalé avant le premier passage payant.
