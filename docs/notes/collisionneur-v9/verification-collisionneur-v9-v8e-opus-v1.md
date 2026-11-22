# Contre-lecture du collisionneur v9-v8e (classe B), rendu v1

**Verdict : à corriger.** Deux bloquants. Tous deux sont des refus ou des écritures en trop. Aucun ne laisse partir une consigne différente de celle scellée.

Pièces lues : v8e 0d591933…, essais 40fe099c…, v8d b7803838… (intacte), relecture c1cebee3…, points ouverts 1f313ce8…. Résultat des essais : 353 passés et 11 sautés, sans les clés.

## Constats
1. **Différences entre la v8d et la v8e.** Elles se limitent à ce qui est annoncé : en-tête, VERSION, bloc des balises (lignes 559 à 616), lecture de la place (868 à 878), arrêt nommé dans `construire_prompt` (953), options et appels dans `principal`.
   - Le texte servi est identique, comparé par programme, à la citation de Fable.
   - Le préambule, les autres consignes, les gardes et les critères n'ont pas bougé.
2. **Place au tour III.1.** Le texte va en fin de consigne, après la phrase unique « Livrable : (a) … (d) », qui demande les duels en (b). Cette place se défend.
3. **Deux options du tour III.3.** Elles sont bien construites, et la coupe est vérifiée par `assert`.
4. **Aucun départ sans place.** Aucune course ne part à l'étage III sans place : l'option est exigée par argparse, la valeur est contrôlée avant toute écriture, et `construire_prompt` s'arrête par un arrêt nommé si la place manque.
5. **Lecture de la place.** `verifier` et `devis-reprise` lisent la place dans `consignes-etage3.json`. Une place différente, ou des consignes d'une autre version, sont refusées.
6. **Code de référence de Fable.** Il reconnaît un texte écrit selon la consigne. Il tolère aussi les espaces insécables avant « : » et les balises en gras ou en titre, ce que j'ai vérifié.

## Bloquants
1. **Faux refus, ligne 612.** Le test `any("essai" in e …)` compte les essais de tous les étages. Un dossier ouvert sous la v8e, avec les étages I et II faits, est donc refusé à l'étage III, avec un message faux (« commencé sous un autre script »). Je l'ai reproduit par un essai à moi : étage I puis étage III sur un même dossier de la v8e, code 1.
   - Correction : ne compter que les essais dont la cellule commence par « E3- ».
   - Ajouter un essai pour ce parcours.
2. **Écritures avant le refus, ordre dans `principal` (lignes 2884 à 2897).** `verser_une_fois` du fichier de la question, puis `sceller_composition`, passent avant le refus du dossier ancien. Je l'ai reproduit : un dossier ouvert sous la v2, étage I seul, reçoit `question-etage3.md` et son sceau, puis il est refusé.
   - C'est contraire au rapport, qui dit « rien n'est écrit ». Et c'est gênant : la question versée fixe celle de toute reprise future du dossier par la v8d.
   - Correction : séparer le contrôle « essais du tour III sans `consignes-etage3.json` ». Le placer juste après `fixer_place_iii3`, avant tout versement. Garder l'écriture du fichier là où elle est.
   - Essai : rien de neuf dans le dossier après le refus.

## Non bloquants
- **Dix essais sautés, faux sous la v8e.** Ce sont `test_v7_copie_des_dossiers_a_reprendre` et `test_v8_copie_des_dossiers_commandes_de_reprise`. Ils sont sautés faute des références des runs, mais ils échoueraient avec ces références, puisque la v8e refuse ces dossiers. Le rapport les dit « les mêmes que la v8d », sans le signaler. Il faut les retirer comme les six autres, ou les changer pour qu'ils attendent le refus.
- **Six essais retirés.** Leur retrait se défend : ils reprennent des dossiers de la v2 ou de la v3, et le rejugement ne vise que des essais arrêtés par une garde ancienne.
  - Couverture perdue et non remplacée : la ligne de reprise par `principal` avec `--go-ligne` (ouverture unique, relance), la croissance du pire cas, et l'issue « Plafond retenu : None » de `devis-reprise`.
  - On peut s'en accommoder (fonctions inchangées), mais un essai sur un dossier de la v8e serait peu coûteux.
- **L'enveloppe des essais hérités ne masque rien.** Elle n'ajoute la place que si l'option manque. Les essais d'option manquante appellent `principal_brut`.
- **`--place-iii3` au devis** est de forme seulement : `devis` ne construit aucune consigne.
- **`ecrire_etat`, dans l'`except`,** réécrit `etat.md` d'un dossier refusé. L'écriture est dérivée, mais à dire.
- **`verifier` ne signale pas** un `consignes-etage3.json` effacé dans un dossier qui a des essais du tour III. Il ne contrôle pas non plus que les invites des tours III.1 et III.3 contiennent la consigne scellée. Ce contrôle est à ajouter.
- **Pour Fable, déjà relevé par le développeur :** au tour III.3, aucune phrase ne demande de duel, alors que l'article 4 exige au moins un duel.

## Mutations (six, toutes prises)
| Mutation | Prise par |
|---|---|
| Texte de Fable altéré (un mot) | essai « mot pour mot » |
| Place ignorée (toujours « fin ») | essai « mot pour mot », essai « servies et scellées » de la place « avant-livrable » |
| Refus du dossier ancien retiré | essai « ancien refusé » |
| Lecture de la place retirée de `lire_composition` | essais « reprise même script et devis » et « verifier refuse » |
| Comparaison au fichier scellé retirée (`sceller_consignes_etage3`) | les deux essais « servies et scellées » |
| Comparaison retirée dans `lire_consignes_etage3` | essai « verifier refuse » |

Copies et essais : `/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/verif-v8e/mut/`, et `/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/verif-v8e/test_mut.py`, qui contient mes deux essais `test_cl_…`, en échec sur la v8e.
