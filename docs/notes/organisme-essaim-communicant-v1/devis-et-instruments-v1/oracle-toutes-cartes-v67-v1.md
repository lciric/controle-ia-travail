# Instrument — oracle recalculé sur toutes les cartes de la course v67, sans verdict du juge — v1

- Aucun appel, aucun réseau, aucune dépense. Script : `oracle_toutes_cartes_v67_v1.py` ; épreuves : `epreuves_oracle_v67_v1.py`, sorties dans `epreuves-oracle-v67-v1/` (résultat : `epreuves-oracle-v67-v1/epreuves-oracle-v67-v1.json`). Empreintes dans les compagnons `.sha256`.
- **Verdict d'abord. Le calcul sur la course v67 n'a pas pu être fait : le journal de la course est absent du disque.** Le chemin que cite l'analyse (`/home/user/ideation-organism/resultats/course-v67/poste-local-v1/boucle-reelle-v66.json`, empreinte attendue `21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71`) n'existe pas sur cette machine, ni son dossier (vérifié par `sha256sum` et `ls`, R11). Le script refuse proprement (code 2, aucune sortie). C'est le résultat : **aucun chiffre d'oracle sur toutes les cartes n'est rendu**. L'instrument est prêt et éprouvé ; il tournera dès que le journal sera posé à son empreinte.
- Ce n'est pas le même empêchement que pour la génération 2 : d'après la structure relevée par l'analyse (§ 1, S1), le journal porte l'arbre `loi` de chacune des 23 cartes. La vérité de chaque carte est donc **calculable** à partir du journal et de la loi du monde, sans aucun verdict ; ce qui manque ici, c'est le fichier.

## 1. Ce que fait l'instrument

- **Lecture par liste blanche** : du journal, seuls `releve.cartes[i].identifiant`, `generation`, `proposeur` et `loi` sont gardés, avant tout calcul ; le reste est jeté. Le fichier de lecture gelée (`lecture-course-reelle.json`), qui porte l'oracle sur les promues, n'est jamais ouvert.
- **Garde indépendante par liste noire** : si la projection contient, à n'importe quelle profondeur (y compris dans un arbre de loi), un champ de verdict, de promotion, de test de mort ou de score du juge (`promue`, `retenue`, `verdict`, `gardien`, `log_w_max`, `statut`, `survit`, `oracle`, `vraies_decouvertes`, etc. ; liste complète dans la sortie), le script refuse (code 3) sans rien écrire.
- **Oracle** (même définition que la course simulée v4, `monde_riche_v4.course`) : loi du monde S-V1 et loi connue K1 de `docs/notes/organisme-multi-generations-v1/outils-v1/puissance_monde_riche_v1.py` (compagnon vérifié) ; 20 000 instances, graine `SeedSequence(20261122)` ; carte **vraie** si son gain au-delà de l'enveloppe du nul de {K1} atteint 0,02 nat, **fausse** si elle est évaluable sans atteindre ce seuil, **rien** si sa loi est absente ou non évaluable. En information : gain au sens v60 (au-delà de K1 seule), identité à l'octet à la loi du monde, forme canonique.
- **Archive {K1} à toutes les générations** : l'archive réelle de la génération 2 dépend des cartes retenues, donc du juge ; la prendre ferait entrer un verdict dans la mesure. Une carte de génération 2 qui ne fait que recopier une retenue de génération 1 compte donc « vraie » si celle-ci l'était : la mesure dit ce que la carte porte du monde, non ce qu'elle ajoute à l'archive du moment.

Références de l'oracle (sortie de l'artefact a1) : gain du monde 0,523558 ; gain de K1 0,052427 ; enveloppe de {K1} 0,052453.

## 2. Épreuves (toutes tenues)

| épreuve | attendu | rendu |
|---|---|---|
| carte = loi du monde (vraie par construction) | vraie | vraie (gain au-delà 0,471105) |
| carte = copie de K1 (fausse par construction) | fausse | fausse (−0,000026) |
| carte = K1 mêlée à l'uniforme (fausse par construction) | fausse | fausse (−0,006676) |
| carte = monde mêlé à 10 % d'uniforme | vraie | vraie (0,447598) |
| carte malformée (type inconnu) | rien | rien |
| canari inscrit dans un champ de verdict | absent de la sortie | absent |
| verdicts permutés, puis supprimés | sortie des cartes identique | identique dans les deux cas |
| mutation : liste blanche élargie à `promue` | refus code 3, aucune sortie | refus code 3, aucune sortie |
| mutation : liste blanche élargie à `verdict` | refus code 3 | refus code 3 |
| score du juge (`log_w_max`) caché dans un arbre de loi | refus code 3 | refus code 3 |
| artefact présenté comme source réelle | refus code 2 (empreinte) | refus code 2 |
| source réelle au chemin cité | calcul | **refus code 2 : source absente du disque** |

## 3. Comparaison avec l'oracle sur les promues seulement

L'analyse rapporte, sur les promues seulement (§ 2, M1) : argon 12 proposées, 6 promues, 6 vraies, 0 fausse ; kimi 11, 5, 5, 0 ; toutes les promues de la génération 1 ; vérité des 12 cartes de la génération 2 non rendue. **Aucune comparaison chiffrée n'est possible ici**, faute du journal. Ce que l'on sait sans lui, par l'analyse : 0 carte sur 23 n'est identique à une loi plantée du monde (M1, après l'écart E1) ; 4 cartes de génération 1 ont été resservies comme copies C1 à C4 ; 11 formes distinctes sur 23 cartes.

## 4. Réserves

1. La loi S-V1 utilisée est celle recopiée dans `puissance_monde_riche_v1.py` (étalonnée contre les chiffres publiés de v67) ; sa conformité à la loi du monde réellement servie en v67 n'a pas pu être vérifiée contre le journal.
2. La définition de l'oracle de la lecture gelée v67 n'a pas été relue (l'analyse ne l'a pas relue non plus, écart E2) ; mon oracle est celui de la v4, pas forcément celui de v67 : les deux comptes « vraies » ne seront pas comparables à l'identique, même avec le journal.
3. Le module standard `json` lit tout le fichier en mémoire avant la projection ; la garantie porte sur ce que le programme **utilise**, pas sur ce qui transite en mémoire. La liste noire ne protège que contre les noms qu'elle connaît.
4. Le seuil de 0,02 nat est celui des outils v1 (`SEUIL_ORACLE`) ; les vraies « faibles » de v67 (V3, V4 de l'étalonnage) peuvent tomber dessous : une carte faible mais juste compterait « fausse ».
