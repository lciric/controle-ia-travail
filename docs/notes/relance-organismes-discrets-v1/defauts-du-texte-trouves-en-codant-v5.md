# Défauts du brouillon 20 trouvés en écrivant la version 5 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md` (`b076e3f942d6252883ab5008993cd0fb9d5ac9788171e3c52975b2b38229d697`), lu par recherches ciblées : conventions, 3.2, 3.5 (b), 6.3 (g), 6.9, 7.4, 7.7, 8.4, 12 (points 17 et 18), 13.1, 13.2. Je n'ai lu aucun fichier « brouillon21 ».
- **Code** : les modules `…_v5.py` de `src/controle_ia/organismes_discrets/` et leurs essais (note `code-v5-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est ambigu, contradictoire ou muet pour coder ; ce que le code fait en attendant ; et si le régler **changerait une règle de jugement** (alors c'est pour Lazar) ou non.
- Les seize points « à trancher » de la note du brouillon 20 ne sont pas recopiés. Je cite ceux que le code touche, par leur numéro.

## En bref : ce qui changerait une règle de jugement

| point | question | pourquoi c'est une règle de jugement |
|---|---|---|
| 1 | état d'un moniteur sous « intervalle impossible faute de deux tâches » | aucun état n'est écrit ; tout choix en fixe un |
| 2 | la forme de la version 8 sous « plus de 1 % de tirages dégénérés » | la suivre retire au moniteur la possibilité de « repérer », contre GO-2026-11-19-70 |
| 3 | « moniteur appris non ajustable » : est-ce une « aire non calculable » ? | fixe « indécis », ou un arrêt, pour un moniteur du verdict |
| 4 | une livraison dont un réglage chiffré diffère du texte : refusée, ou lue ? | la lire changerait le nombre de permutations, la taille de la famille ou le niveau |
| 5 | fiche 9 (déjà posée à Lazar) : le quotient écrit dans la règle de l'intervalle dégénéré | au bord, 20 tirages dégénérés font ou ne font pas « ne repère pas » |
| 6 | schéma de permutation (déjà posé à Lazar) | les valeurs p des cinq moniteurs |

Les autres points ne changent aucune règle de jugement : ils touchent une forme, un arrêt de lecture ou une grandeur rapportée.

## A. Forme de la livraison du côté habilité (6.9 ; 13.1)

1. **« Intervalle impossible faute de deux tâches » : aucun état écrit.** Le module rend ce motif avec le plancher rempli et les tirages nuls. Le texte ne dit ni l'état du moniteur, ni si sa valeur p reste dans la famille. (Code : arrêt, garde « tirages nuls sous intervalle impossible ».) **Règle de jugement : oui.**
2. **« Plus de 1 % de tirages dégénérés » : le module contredit la règle tranchée.** Il rend les valeurs p nulles et 1 dans la famille ; le texte garde la valeur p haute dans la famille. (Code : arrêt, garde « valeur p pour la famille égale à 1 sous tirages dégénérés ». Le code applique la règle du texte dès que la valeur p haute est rendue.) **Règle de jugement : oui si l'on suivait le module ; non si le module est corrigé, ce que la passation demande.**
3. **Motif « moniteur appris non ajustable ».** Le texte nomme deux causes survenues avant les permutations (classe absente d'un pli, vocabulaire vide). Le module en rend une troisième sous la même forme, les quatre comptes nuls. Les valeurs du champ `motif` ne sont pas transmises : le code ne peut pas la distinguer. (Code : toute livraison aux quatre comptes nuls, `calculable` faux et `motif` rempli se lit « aire non calculable » : « indécis », 1 dans la famille.) **Règle de jugement : oui, si la réponse n'est pas « indécis ».**
4. **Contrôle des réglages.** Le texte fixe 2 000 permutations, 2 000 tirages, une famille de quinze, un niveau de 0,05. Il ne dit pas ce qu'on fait d'une livraison dont `reglages` en dit autrement. (Code : arrêt, garde « contrôle des réglages ».) **Règle de jugement : oui si la livraison devait être lue ; non si elle est refusée.**
5. **Fiche 9 et quotient écrit.** La règle de l'intervalle dégénéré écrit `tirages_degeneres ÷ tirages` ; `tirages` compte les calculés ; le texte se dit écrit sous l'option (a), sur les demandés. Les deux divergent à 20 tirages dégénérés. (Code : option (a), une constante unique.) **Règle de jugement : oui ; déjà posée à Lazar.**
6. **Schéma de permutation.** Ouvert, sans défaut. (Code : argument obligatoire, aucun des deux n'est retenu.) **Règle de jugement : oui ; déjà posée à Lazar.**
7. **Ce que la livraison déclare sous chaque schéma n'est pas transmis.** Les réponses du développeur habilité nomment `reglages.permutation` et `reglages.unite_de_la_permutation`, sans leurs valeurs. Sans elles, l'analyse ne peut pas vérifier que la livraison a été tirée sous le schéma retenu. (Code : la table des déclarations est vide ; la règle de discrétion s'arrête tant qu'elle l'est.) Règle de jugement : non ; mais **rien ne se lit avant cette transmission**.
8. **Couple de tirages nul sous « plus de 1 % de permutations perdues ».** Le texte n'admet un couple vide que pour une cause antérieure ; le module le rend nul ici. L'état est « indécis » dans les deux lectures ; seule change la question « livraison refusée ou non ». (Code : arrêt, garde « tirages nuls sous permutations perdues » ; la forme aux quatre comptes rendus, celle du texte cité, passe.) Règle de jugement : non ; arrêt de lecture.
9. **À quelle liste s'applique « un champ de plus ou de moins arrête la lecture ».** (Code : un écart dans l'une quelconque des quatre listes arrête, et l'arrêt dit que le cas attend.) Règle de jugement : non.
10. **Ce que l'instance d'analyse reçoit des onze noms.** Le texte dit qu'elle ne voit « aucun score, aucun texte et aucun interne d'un moniteur ». Le contenu de six des onze noms (`plis`, `piece_source`, `exclues`, `preuve_d_ordre`, `comptes_des_lectures`, `nombres_rendus`) n'est pas transmis : je ne peux pas dire s'ils respectent cette phrase. (Code : la liste des onze est exigée ; ces six noms ne sont ni lus ni gardés.) Règle de jugement : non ; c'est une question de cloisonnement, pour la session principale.
11. **Nom et forme de la pièce qui porte la sortie de la lecture commune.** Le texte ne nomme pas ce fichier ni ne dit qu'il est scellé. Or c'est de lui que vient l'empreinte attendue du fichier des rangs. (Code : un objet JSON aux onze noms, scellé par son compagnon, dont le chemin est donné par l'appelant.) Règle de jugement : non.
12. **Formes non transmises**, où le code a dû supposer :
    - clés de dose de `lectures` et champ `dose` (code : `dose-0.50` ou le nombre, les deux admis) ;
    - `effectifs` (code : comptes entiers nommés, à un ou plusieurs niveaux, ou nul) ;
    - `agregateur_somme_sans_etat` et `agregateur_maximum_sans_etat` (code : rapportés tels que rendus, s'ils ne portent que des nombres de 0 à 1) ;
    - `motif` d'un moniteur calculable (code : nul, ou texte ; un texte vide se lit « non rempli ») ;
    - `quantile_borne_haute` quand la borne est nulle (code : nul admis) ;
    - `scores_par_unite.lignes`, `.champs`, `.forme` (code : `lignes` et `champs` sont confrontés au fichier s'ils sont un entier et une liste ; `forme` n'est pas lue).
    Un écart à ces suppositions arrête ; il ne passe pas en silence. Règle de jugement : non.
13. **« Comptes d'exclusion ».** La liste fermée du texte les nomme parmi les nombres rendus par moniteur et par dose ; les dix-huit noms n'en portent pas ; `exclues` est en sortie de la lecture commune, forme inconnue. (Code : non lus, donc non rapportés par l'analyse.) Règle de jugement : non ; une grandeur rapportée manque.
14. **Forme corrigée du cas « intervalle dégénéré seul ».** Quand le module gardera la valeur p haute, dira-t-il `calculable` vrai ou faux ? Rendra-t-il la borne ? (Code : les deux admis ; le cas se décide sur les comptes et la valeur p.) Règle de jugement : non.
15. **« Cause » d'une valeur égale à 1 (6.9 ; 8.4, « famille de Holm complète »).** Le texte la définit par « `motif` rempli et `calculable` faux ». Sous la forme corrigée du point 14, un moniteur à l'intervalle dégénéré peut porter ce même couple avec une valeur p calculable. (Code : la cause se lit dans les comptes — quatre comptes nuls, ou plancher au-delà de 1 % — et le couple est exigé en plus.) Règle de jugement : non ; la définition est à resserrer.

## B. Phrases de 6.9 qui se contredisent encore

16. **« Une valeur p absente ou non calculable […] entre dans la famille pour la valeur 1 »** reste écrit dans le paragraphe « Partage du travail », quelques phrases avant « absente […] elle est refusée, pour tout moniteur ». (Code : la seconde, et 8.4.) Règle de jugement : non, déjà tranché au brouillon 19 ; le mot « absente ou » est à retirer.
17. **« Tirages dégénérés (plus de 1 % […] dans l'intervalle ou le plancher […]) : le moniteur concerné est "indécis" »** (GO-2026-11-19-29) reste écrit avant la règle de GO-2026-11-19-70, qui le précise pour l'intervalle. Lu seul, il redonne l'option (a). (Code : GO-2026-11-19-70.) Règle de jugement : non, déjà tranché ; rédaction.
18. **Plancher au-delà de 1 % : l'aire est-elle rendue ?** « Grandeurs rapportées sans verdict » veut l'aire rapportée ; le texte du développeur habilité cité n'en dit rien ; la version 8 la rend nulle. (Code : aux doses du verdict, les deux admis, l'état est « indécis » ; à la dose ¼, aire nulle : arrêt, garde « grandeurs rapportées à la dose un quart ».) Règle de jugement : non.

## C. Contrôles que le texte ne commande pas mot pour mot

19. **Valeurs p confrontées à leurs comptes.** Le texte donne les deux formules ; il ne dit pas que l'analyse les vérifie, ni à quelle précision. (Code : refus au-delà de 1e-9.) Si le module arrondit, la lecture s'arrête. Règle de jugement : non.
20. **Quantile de la borne haute.** Le texte dit 1 − 0,05 ÷ m ; il ne dit pas que l'analyse refuse un autre `quantile_borne_haute`. (Code : refus.) Proche du point 4, que la note du brouillon 20 laisse ouvert pour `reglages` : à dire de même. Règle de jugement : non si c'est un refus.
21. **Dose ¼ absente.** « La dose ¼ est rendue pour information. » Son absence arrête-t-elle la lecture des trois doses du verdict ? (Code : oui, arrêt nommé.) Règle de jugement : non ; arrêt de lecture pour une dose sans verdict, à confirmer.
22. **Dixième champ.** L'artefact de 8.4 dit « valeurs non entières hors des rangs moyens, ou hors de l'étendue des rangs du pli ». (Code : plus strict — par moniteur, dose et pli, les valeurs sont exactement un jeu de rangs moyens de 1 à n.) Cela suppose que le fichier porte toutes les unités du pli et elles seules, ce que 6.9 dit. Règle de jugement : non.

## D. Étapes, fichiers, graines

23. **Qui constate que l'étape (m) est jouée.** Les conventions disent quand elle ne l'est pas (A15, A16, discrétion « non lue »). Le texte ne dit pas quelles pièces l'écriture du fichier de l'étape (m) exige. (Code : l'issue de la table A sans aucune ligne, le renvoi de la base « vérifié », les effectifs de la base conformes.) Règle de jugement : non.
24. **Une clé `boot/taches/{lot}` pour plusieurs intervalles.** Un lot porte plusieurs grandeurs rapportées, une seule clé. Le texte ne dit pas si chaque intervalle rejoue la clé (mêmes tâches tirées pour toutes les grandeurs) ou si les intervalles se suivent sur un même tirage. Les deux sont rejouables ; les nombres diffèrent. (Code : le tirage porte sa clé ; l'ordre d'emploi reste à l'enchaînement.) Règle de jugement : non ; à fixer avant le scellement, pour qu'un rejeu rende les mêmes nombres.
25. **Seuil du 1 % hors des moniteurs.** La fiche 9 parle des moniteurs. Pour un intervalle seulement rapporté et pour l'aire conditionnelle, le code compte sur les tirages demandés. Si l'option (b) était retenue, le texte devrait dire si elle vaut aussi là. Règle de jugement : non ; grandeurs sans verdict.
26. **Ligne de GO de l'écart à R9.** Le texte dit « avec sa ligne de GO ». Il ne dit pas ce que la ligne doit porter pour être reconnue. (Code : la ligne existe une seule fois au registre et parle de R9 et des identifiants.) Règle de jugement : non.
27. **Nom en clair du fichier.** « Fichier des scores par unité » désigne un fichier de rangs, nommé `rangs-par-unite-…`, sous une clé `scores_par_unite`. (Code : « fichier des rangs par unité » dans ses messages.) Règle de jugement : non.

## Faits, sans défaut

- Le troisième état du contrôle de l'adaptateur est nommé par le texte (« pas au-dessus », à confirmer par le lecteur habilité) : l'essai le confronte au brouillon 20.
- Les textes des réserves R-BA2 et R-BA2b sont, dans le brouillon 20, ceux du brouillon 17, à la lettre (essai).
- La tolérance des blancs de bord sur la ligne de fermeture du bloc de code est écrite en 3.2 ; le code la porte.
