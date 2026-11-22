# Vérification des pièces v5 du devis et des instruments de l'essaim — v1

- Le même contre-lecteur, sur le commit `bc2290c4a`.
- Travail sur processeur seulement : aucun appel de modèle, aucune dépense, aucun réseau, rien d'écrit dans le dépôt. Je n'ai jamais touché aux chemins du pilote (ni `runs/`, ni `~/.local/state`).
- Outils et sorties : `outils/attaques_v5_cl_v1.py`, `sorties/attaques-v5-cl-v1.json` et `.stdout`, `sorties/rejeu/`.

## Verdict

**Conforme avec réserves.** Le code ferme tout ce qu'un même processus de bonne foi peut fermer. Ce qui reste relève de l'exploitation (clé, ancre, conteneur) et du fournisseur.

## 1. Rejeu

- Les compagnons sont conformes.
- `rejouer_v5.sh` depuis le commit : tenu. Les 49 cas sont égaux hors horodatages, et les 7 tests pytest passent.

## 2. Mes attaques, rejouées contre le registre v2 et le lanceur v3

| attaque | codes | facture (USD) | lecture |
|---|---|---|---|
| N2 : registre tronqué, sans la clé | 0, 22 | — | refusé |
| N3 : deux processus | 25, 0 | 176,45 | verrou tenu |
| N3b : courses entrelacées | 0, 25 | 176,45 | verrou tenu |
| N4 : registre forgé à un plafond de 10⁶ | 24 | 0 | refusé |
| N5 : sous-classe de l'adaptateur | 24 | 0 | refusé |
| K2b : ancre seule supprimée | 22 | 0 | refusé |
| N1 : registre neuf ailleurs, par `_courir` | 0, 0 | **352,90** | `_courir` est une fonction de module ouverte, qui prend les chemins **et la liste d'admission** de l'appelant ; le chemin écrit en dur ne vaut que pour `courir_pilote` (`lanceur_pilote_essaim_v3.py`, l. 144-148, 170) |
| K1 : registre tronqué, re-scellé **avec** la clé, ancre réécrite | 0, 22, 0 | **352,90** | la clé est lisible par le même utilisateur |
| K2 : registre, sceau et ancre supprimés, puis recréés au même chemin | 0, 0 | **352,90** | `creer` n'exige que l'absence des trois (`registre_depense_v2.py`, l. 77-79) |
| K3 : conteneur neuf, dossier d'état perdu | 0, 22, puis 0 | **352,90** | registre gardé : refus 22 (sûr). Registre non poussé : budget neuf. `runs/` n'est pas ignoré par git, mais rien n'impose de pousser le registre |
| K4 : mort entre l'ajout d'une ligne et le sceau | tué, puis 22 | 2,36 | échec sûr, mais la course est bloquée (déclaré par l'auteur) |
| N7 : `AdaptateurChatCompletions.appeler` remplacée en mémoire, fichier inchangé | 0 | **529,34** | l'empreinte porte sur le fichier, pas sur le code chargé. Cela vaut aussi sous `AdaptateurKimiStrict`, qui appelle `super().appeler` ; il ne fige que les méthodes du transport |

- N7, K1 et K2 demandent un acteur fautif dans le processus ou dans le compte : ce ne sont pas des accidents.
- N1 et K3, eux, peuvent arriver **par erreur d'exploitation** : une épreuve qui passe par `_courir`, ou une seconde session dans un autre conteneur.

## 3. A3 et A4

- Le rapport ne dit plus qu'elles sont « arrêtées » (l. 25-30 et 42). Il les renvoie, à juste titre, au transport, à la fumée et à la limite chez le fournisseur.
- Ce renvoi est exact :
  - `tentatives` est mesuré sur la connexion (`transport_kimi_reel_v1.py`, l. 246-265) ;
  - si `completion_tokens_details.reasoning_tokens` manque, l'usage vaut `None` (l. 409-420) ;
  - un excédent de `total_tokens` est compté en sortie.
- Ce qui reste invisible au transport : une relance faite côté serveur, et une réflexion facturée sans trace dans l'usage. Seuls H1 (la fumée, rapprochée de la facture) et la limite chez le fournisseur les couvrent.

## 4. Garde des formes fausses v2 (a-faire v2, § 5)

- **Conforme.** Elle adopte mes quatre réserves.
- J'ai recalculé les seuils : B3 dépasse la queue dans 4 mondes (0, 3, 7 et 11), et son total de 113 dépasse 83,1. B3 échoue donc aux deux gardes.
- À noter :
  - le réglage est fait pour que B3 échoue ;
  - les seuils sont absolus (+24, +8) et ne sont tirés que de 12 mondes ;
  - compter « rien » comme une forme fausse pénalise la troncature, ce qui est voulu, mais doit être écrit.

## 5. Bloquant pour la fumée

1. Les deux bloquants de la contre-lecture du transport (renvoi ; je ne les ai pas rejugés).
2. Lancer la fumée par `courir_pilote` ou par un chemin écrit en dur, **jamais** par `_courir` avec une liste d'admission libre (N1).

## 6. Bloquant pour le pilote

1. **La limite chez le fournisseur n'est pas dure.** L'erratum 1 du transport (commit `5fd4eefbb`) dit : budget de projet réglable en console, application retardée. Le point A.1 de l'a-faire v2 la tient pourtant pour « la seule borne qui tienne ». Il faut un **solde prépayé de 204 USD au plus**, ou réécrire la borne en conséquence.
2. **Registre durable hors du conteneur**, avec une règle d'exploitation : le registre est poussé après chaque course, et l'ancre et la clé sont gardées par le directeur (K3, K2).
3. **`_courir` fermée hors des épreuves** : refus quand la liste d'admission est celle du pilote et que les chemins ne sont pas ceux du pilote (N1).

## 7. À noter

- N7 : remplacement de méthode en mémoire. Figer aussi `AdaptateurChatCompletions.appeler`, comme les méthodes du transport.
- K1 : une clé lisible par le même utilisateur (limite déclarée).
- K4 : la reprise après une mort entre l'ajout et le sceau n'a pas de procédure écrite. Il faut l'écrire sous décision du directeur, sans re-sceller à la main.
