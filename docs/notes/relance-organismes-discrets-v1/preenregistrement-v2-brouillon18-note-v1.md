# Note de changements — brouillon 18 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon18.md`, `75fef5262d7ba05576ca118214730a151d7958b7e5b345081a3349db14401655` (1 781 lignes). Brouillon 17 inchangé (`9f8242429ce1f23e7b67c3dbd6ef64501488ca3df89f5d0c31999f852724406f`, vérifié).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 à 17.
- **Source unique des trois ajouts** : `docs/notes/bras-a-moniteurs-v1/pour-la-relance-lanceur-et-appariement-sans-interne-v1.md` (`3bec0ee962c23f4a9814b0ffa96e94bcdd1b8930cf3691cf131021abed26f7c3`, R-3873), relue sans interne par la session principale. Le rapport de vérification qu'elle cite n'a pas été ouvert. Pour le quatrième ajout : la règle de choix scellée de l'essai de mesure (`b14b7084…`).
- **Heures (UTC, `date -u`)** : début 2026-11-19T14:20:52Z.
- **Interdits tenus** : aucun interne de moniteur ; aucune fiche de l'organisme d'idéation ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé. Le brouillon et cette note sont scellés par leur compagnon.
- **Contrôles faits** : la phrase sur le lanceur, les sept lignes de la fiche et la note de la session principale sont des sous-chaînes exactes du brouillon 18 (vérifié par programme) ; validateur — deux problèmes attendus (marque dans sept cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes) ; consignes inchangées (`98a9bd34…`, `ecf590ea…`) ; les sept fiches précédentes et les phrases du développeur habilité restent à la lettre ; table d'en-tête, 111 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 17 ; différence avec le brouillon 17 : 40 lignes ajoutées, 16 retirées.

## 1. Ce qui change, du brouillon 17 au brouillon 18

| section | changement | source |
|---|---|---|
| titre, statut, en-tête | brouillon 18 ; date ; commit ; note ; deux lignes à la table des pièces | — |
| 3.4 | réserve sur la conformité complétée : 166,8 USD à l'effort bas contre 146,4 à l'effort moyen ; elle ne change pas la recommandation | règle de choix |
| 3.5 (b) | règle de cloisonnement du fichier des scores par unité ; rangs au lieu des scores ; limite écrite | § 2 |
| 6.9 | fichier des scores par unité : le dixième champ porte le rang dans le pli ; personne ne l'ouvre ; **schéma de permutation écrit sous deux rédactions**, option 1 et option 2 ; puissance, nombre de permutations, valeur p de Monte-Carlo | § 2 ; § 3 |
| 8.4 | deux lignes neuves (schéma de permutation sous l'option 2 ; cloisonnement du fichier) ; la ligne existante marquée « sous l'option 1 » | § 3 ; § 2 |
| 12 | point 17 neuf : fiche à la lettre, nœud ouvert sans défaut, avis du rédacteur ; en-tête des points | § 3 |
| 13 | étape 4 ; 13.1 : case neuve « schéma de permutation », marquée ; case du module : version suivante attendue ; 13.2 : phrase sur le lanceur, à la lettre | § 3 ; § 2 ; § 1 |
| 14 | 14.30 neuf | — |

## 2. Cohérence du cloisonnement avec ce que le texte disait du fichier aux dix champs

Chaque endroit que la règle touche :

| endroit | ce qu'il disait | ce qu'il dit maintenant |
|---|---|---|
| 3.5 (b) | l'analyse reçoit les scores par action ; « des sorties et non des internes », à confirmer | elle reçoit le rang de chaque unité dans son pli ; la phrase est dite insuffisante (moniteurs appris linéaires) ; règle de cloisonnement en deux barrières ; limite : un rang garde l'ordre |
| 6.9, ce que le côté habilité rend pour l'aire conditionnelle | « les scores qui ont servi l'aire de cette dose » | le rang dans le pli, à la place du score |
| 6.9, forme exacte du fichier (citation du développeur habilité, gardée à la lettre) | dixième champ `score` | la citation reste ; une phrase la suit : ce champ porte désormais le rang (rang parmi les lignes du même moniteur, de la même dose et du même pli, étiquettes 0 et 1 ensemble, rang moyen pour les ex æquo) ; **son nom est à inscrire en 13.1** |
| 6.9, calcul de l'aire conditionnelle | lignes d'étiquette 0 entières et lignes d'étiquette 1 des épisodes retenus, par pli, moyenne des deux plis | inchangé : l'aire d'un sous-ensemble ne dépend que de l'ordre, donc des rangs |
| 6.9, intervalle | rééchantillonnage groupé par tâche, vingt clés côté analyse | inchangé : identique sur les rangs (vérifié par le contre-lecteur de la session principale, selon la pièce) |
| 6.9, « ne sont ouverts par aucun agent » | les scores ne sont ouverts par aucun agent | le fichier n'est ouvert par aucun agent ; seul le programme de l'aire conditionnelle le lit, contre-lu et scellé, et ne rend que les aires |
| 7.4, ligne C4 | aire, aires des deux plis, borne haute, deux valeurs p et leurs comptes | **non touchée** : ce sont des nombres rendus par le côté habilité, non tirés de ce fichier |
| 8.4 | garde « scores remis à l'analyse » | gardée ; ligne neuve « cloisonnement » (programme seul lecteur ; rien d'autre que des aires en sortie ; le dixième champ est un rang) |
| 13.2 | le lanceur écrit les scores par unité | il écrit le fichier où le rang tient la place du score |

**Un point que je signale** : la seconde barrière ne cache pas l'ordre. Qui tiendrait les rangs et les textes des actions pourrait encore ajuster un modèle sur l'ordre. C'est donc la première barrière — aucun agent n'ouvre le fichier — qui tient le cloisonnement ; je l'ai écrit comme limite en 3.5 (b).

## 3. Ce que le côté habilité doit changer

1. **Écriture du fichier des scores par unité** (lecture commune, et non étape de préparation : c'est elle qui écrit ce fichier, après les ouvertures) : le dixième champ porte le rang de l'unité dans son pli, à la place du score ; rang calculé parmi toutes les lignes du même moniteur, de la même dose et du même pli ; rang moyen pour les ex æquo ; nom du champ à rendre pour la case de 13.1. Les neuf autres champs ne changent pas.
2. **Étape de préparation des lectures** (phrase du § 1) : elle tient, dans un dossier à part, la table des identifiants opaques **et le bilan par condition** ; la production ne reçoit que les demandes, la consigne et l'engagement de la table.
3. **Lanceur de l'étape de discrétion** (phrase du § 1) : inscrire au registre, datés, l'engagement de la table avant toute production, et chaque manifeste de production dès son écriture ; appeler la garde de production avant le premier appel d'un moniteur à modèle de langue ; envoyer et écrire les lectures dans l'ordre des identifiants opaques ; laisser l'ouverture de la table à la seule lecture commune ; citer par leur empreinte, dans sa configuration scellée, les modules qu'il appelle.
4. **Schéma de permutation**, selon le mot de Lazar : sous l'option 2, échanger les étiquettes dans chaque paire d'épisodes de même tâche et de même rang, une chance sur deux, les huit paires d'une tâche tirées indépendamment, avec les mêmes clés `perm/moniteur/{moniteur}/{dose}` ; garde qui refuse un échange entre rangs ou entre tâches. Sous l'option 1, rien ne change. Ne rien écrire de définitif avant ce mot.
5. **À vérifier par le lecteur habilité**, pour l'option 2 : que rien d'autre que la dose ne distingue les deux épisodes d'une paire dans le lanceur du bras (mêmes graines d'action, même rang).
6. **Version du module** : commit, empreinte et notice de la version qui portera les points 1 et 4, pour la case de 13.1 ; l'épreuve par retrait et la notice de la version 7 restent dues.

Côté relance, pour mémoire : le programme de l'aire conditionnelle lit des rangs et non des scores ; il est le seul lecteur du fichier, il doit être contre-lu et scellé avant de le lire, et il ne sort que des aires, des intervalles et des comptes.

## 4. Cases de 13.1 restantes (sept lignes portent la marque)

| case | ce qui manque | qui |
|---|---|---|
| **schéma de permutation** (neuve) | mot de Lazar sur le point 17 ; sans défaut | Lazar |
| lecteurs et juge des ancres | sortie maximale du lecteur 2 (4 096 à l'essai, 8 192 selon la règle) ; mot de Lazar sur le choix des lecteurs | Lazar |
| lecture du juge d'une autre lignée | 2 560 ou 6 400 | Lazar |
| entropie | l'entier racine ; écart à la règle gelée R9 pour l'entropie propre de la table | Lazar ; session de relance |
| renvoi de la base | « vérifié » ou « non vérifié » | lecteur habilité de la session principale |
| commit du code de l'instrument et de l'analyse | commit et empreintes | session de relance |
| module des cinq moniteurs, côté habilité | la version qui suivra ce brouillon (rang au dixième champ et son nom ; schéma de permutation retenu) ; épreuve par retrait et notice de la version 7 | session principale |

Remplies : nœuds (1 à 18) ; familles ; consignes figées ; seuils ; consignes des moniteurs ; moniteurs à modèle de langue (instrument) ; code de la base ; réserve R-BA2. Hors de 13.1 : la contre-lecture 10, sur le texte aux cases remplies. Avant le scellement, la rédaction du schéma de permutation que Lazar n'aura pas retenue est à retirer de 6.9 et de 8.4.
