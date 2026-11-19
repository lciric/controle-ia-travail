# Défauts du brouillon 24 trouvés en écrivant la version 6 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md` (`12609c048b7c1118845af38bd639988df9388728e2791fd88e7ac5fbbb4b9012`), lu par recherches ciblées : 6.9 (table des formes, « Ce que vaut cet arrêt », définition unique), 8.4 (lignes de la discrétion). Les autres passages cités ont été lus au brouillon 22 (conventions, 6.3 (m) et (n), 7.2, 7.5) ; je n'ai pas vérifié qu'ils sont inchangés au brouillon 24.
- **Code** : les modules `…_v6.py` (note `code-v6-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est ambigu, contradictoire ou muet pour coder ; ce que le code fait ; et si le régler **changerait une règle de jugement** (pour Lazar) ou non.
- Les cinq questions déjà posées à Lazar (schéma de permutation ; fiches 9 à 12) ne sont pas reprises : le code les porte comme des choix nommés, sans valeur.

## A. Ce qui changerait une règle de jugement, ou la conséquence d'une règle (pour Lazar)

1. **Contrôles du code que le texte ne nomme pas, et qui arrêtent la lecture.** La liste des écarts de structure de 6.9 est fermée. Le code refuse aussi :
   - une valeur p qui ne répond pas à ses comptes, à 1e-9 près (demandé par la contre-lecture du code de la version 4 ; la note du brouillon 22 dit que le texte ne l'exige pas) ;
   - une lecture dont les champs `moniteur` ou `dose` ne sont pas ceux de sa place ;
   - une aire, une valeur p ou une borne hors de 0 à 1, ou qui n'est pas un nombre ;
   - une borne haute rendue sans son quantile ;
   - au cas E, sous les rédactions (a) et (b), une borne haute remplie (la table dit « `borne_haute` `null` » ; la liste des écarts ne le reprend pas).

   Chacun est une cause d'arrêt de plus. Depuis le brouillon 23, un arrêt peut rendre la discrétion « non lue », ou ne plus rien prononcer de la course : ajouter une cause d'arrêt touche donc la conséquence que fixe la fiche 12. **À trancher** : inscrire ces contrôles dans la liste de 6.9 et en 8.4, ou les retirer du code. Je recommande de les inscrire, sauf le premier, qui peut arrêter à tort si le module arrondit ses valeurs p : pour lui, l'épreuve de forme avant toute dépense doit le dire.
2. **« La discrétion se lit alors sur elle, une seule fois »** (rédaction (b), livraison refaite). Le code exige une ligne de GO pour lire une livraison refaite, mais il ne compte pas les reprises et ne lie pas la ligne à une livraison donnée : la même ligne ouvrirait une troisième livraison après un second arrêt. Le texte ne dit pas ce que la ligne de GO doit porter (l'empreinte de la livraison refaite ? celle du module corrigé ?). **Règle de jugement : oui**, si « une seule fois » doit borner le nombre de livraisons lues.
3. **Arrêt à l'étape (n) sous la rédaction (b).** La discrétion devient « non lue » alors que le fichier de l'étape (m), déjà scellé et inscrit au registre, porte les états et la table C. Le texte ne dit pas ce que le rapport fait de ce fichier. (Code : la table C n'est pas reçue ; le fichier reste où il est.) C'est la différence même entre les rédactions (b) et (c) : **à dire dans la fiche 12**, qui est déjà partie.

## B. Forme de l'événement d'arrêt (6.9, définition unique)

4. **« Le nom du champ en défaut, c'est-à-dire le nom d'une clé des listes fermées ».** Quand le défaut est celui d'une liste entière — un champ de plus, un champ en double, une sortie illisible — ou d'une ligne du fichier des rangs, aucune clé des listes n'est en défaut. (Code : six désignations fermées, qui nomment la liste : « liste des onze clés de la sortie », « champ en double », etc. Un champ de plus n'est jamais nommé, puisque son nom vient de la livraison.) Règle de jugement : non ; la définition est à compléter.
5. **Champs du fichier des rangs.** La définition parle des « listes fermées » ; les dix champs du fichier des rangs en font-ils partie ? (Code : oui, ils sont nommables.) Non.
6. **Réglages.** Une clé de `reglages` et une clé d'une lecture portent le même nom, `n_permutations`. (Code : `reglages.n_permutations` pour la première.) Non.
7. **Défauts de l'appelant.** Un fichier absent, non scellé, ou une pièce qui n'est pas celle de l'étape (m) ne sont pas des refus de livraison. (Code : garde ordinaire, sans événement, rien de consigné.) Le texte ne distingue pas les deux. Non.

## C. Fichiers que le texte ne nomme pas

8. **La configuration scellée de l'analyse.** Le texte dit « paramètres obligatoires, lus dans la configuration scellée » et nomme, en 13.2, celle du lanceur de l'étape de discrétion, du côté habilité. Il ne nomme pas celle de l'instance d'analyse, ni qui l'écrit, ni où s'inscrit son empreinte. (Code : un fichier JSON à deux parties, les cinq choix et les chaînes du module ; chemin donné par l'enchaînement.) Non.
9. **La pièce qui porte la sortie de la lecture commune** n'a toujours pas de nom (relevé de la version 5, point 11 ; contre-lecture du code de la version 5, M-4). Non.
10. **Le fichier des constats de l'étape (m).** Les conventions disent du fichier de l'étape (m) : « trois champs et eux seuls ». Pour que la garde « étape (m) jouée » tienne à la lecture, il faut le journal de la table A, la case « renvoi de la base », les effectifs et l'empreinte de la livraison. (Code : un second fichier scellé, `constats-de-l-etape-m-bras-a.json`, à côté.) Le texte doit le nommer, ou élargir le premier. Non.
11. **Les fichiers d'arrêt.** « L'arrêt est consigné » : où, sous quel nom ? (Code : `arret-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json`, scellé, dans un dossier donné par l'enchaînement ; il porte le constat et l'empreinte de la livraison.) Non.
12. **La phrase d'accord d'une ligne de GO.** Pour l'écart à R9 et pour une livraison refaite, le code exige une phrase à la lettre dans la ligne du registre, et refuse une ligne qui porte un mot de refus. Ces deux phrases sont de moi. Qui écrit le registre doit les connaître. Non.

## D. Chaînes du module du côté habilité

13. **Causes que la table distingue.** La configuration range chaque valeur de `motif` sous l'une de cinq causes : antérieure aux permutations ; moniteur appris non ajustable ; permutations perdues ; tirages dégénérés ; intervalle impossible. Si le module rend un motif qui ne nomme aucune des cinq, il ne peut pas s'inscrire, et toute lecture qui le porte arrête. À confirmer avec la liste demandée au développeur habilité. Non.
14. **`quantile_borne_haute` quand la borne est nulle.** Le texte dit ce que le champ doit dire, non ce qu'il porte quand il n'y a pas de borne. (Code : la valeur inscrite, ou nul si la borne est nulle.) Non.
15. **`scores_par_unite.lignes`, `.champs`, `.forme`.** Leur forme n'est pas transmise. (Code : un entier, une liste des dix noms ; `forme` n'est pas lue ; toute autre forme arrête, à l'étape (n).) Non.
16. **Aires de la somme et du maximum de l'agrégateur.** Leur forme n'est pas transmise. (Code : rapportées telles que rendues, sans contrôle, comme `effectifs` et `exclues`.) La version 5 exigeait des nombres ; je l'ai retiré, pour ne pas ajouter une cause d'arrêt. Non.

## E. Graines

17. **Une clé `boot/taches/{lot}` pour plusieurs intervalles** (relevé de la version 5, point 24 ; contre-lecture, M-1). Le code tranche de fait : un tirage ne sert qu'une fois, donc chaque intervalle rejoue la clé du lot et toutes les grandeurs du lot voient les mêmes tâches tirées. Un rejeu ne dépend plus de l'ordre des calculs. Le texte ne le dit pas. Règle de jugement : non (intervalles seulement rapportés) ; les nombres rapportés en dépendent.

## F. Garde statique

18. **Lecture d'un dossier.** Un programme qui lit tous les fichiers d'un dossier lit le fichier des rangs s'il s'y trouve. La garde ne peut pas le refuser sans arrêter à tort huit programmes du dépôt. (Code : signalement sans arrêt ; limite écrite.) Le texte, ou l'enchaînement, doit dire où le fichier des rangs est rangé : dans un dossier qu'aucun lanceur ne parcourt. Non ; règle de procédure.
19. **Chemins du côté habilité.** La garde exclut un seul dossier, par son chemin exact. Si le côté habilité range ailleurs un programme qui nomme le fichier, la garde le refusera. Le chemin est à confirmer par la session principale. Non.

## Faits, sans défaut

- La table des formes se code telle qu'elle est écrite : l'ordre B, C, E, D, A suffit à ranger toute lecture bien formée, et chaque ligne dit ce qu'elle exige.
- La définition unique de ce que rend le programme qui refuse se tient : les cinq éléments suffisent à dire tout arrêt du code.
- Les textes des réserves R-BA2 et R-BA2b, et le nom « pas au-dessus », sont au brouillon 24 ce qu'ils étaient au brouillon 20 (essai).
