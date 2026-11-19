# Défauts du brouillon 31 trouvés en écrivant la version 9 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon31.md` (`6fd71ee2c7756d07418155e7775ceba67ece71b438fb415838964652983a9768`). Lu : les notes des brouillons 29, 30 et 31, en entier ; des brouillons, les seules phrases neuves depuis le brouillon 28, tirées par programme. Le reste du texte n'a pas été relu.
- **Code** : les modules `…_v9.py` et `scripts/constat_de_lancement_discretion_bras_a_v2.py` (note `code-v9-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est muet ou ambigu pour coder ; ce que le code fait ; ce qu'il faudrait écrire. La partie A dit ce qui touche une règle de jugement ou sa conséquence ; la partie B, le reste.
- Les cinq questions déjà posées à Lazar ne sont pas reprises : le code les porte comme des choix nommés, sans valeur.

## A. Ce qui touche une règle de jugement, ou sa conséquence

1. **Provenance : une pièce qui n'est pas un objet JSON, quand la clé est inscrite.** Le texte range dans « provenance non établie » un `piece_source` d'un autre module, mal formé, ou sans la clé. Il ne dit rien d'une pièce où `piece_source` ne peut pas même se lire : fichier qui n'est pas du JSON, liste, texte.
   - Le code la range aussi dans « provenance non établie » : garde ordinaire, sans événement ni fichier d'arrêt. Sous une clé `null`, la même pièce reste une « pièce illisible », donc un refus de la livraison et l'issue du point 21.
   - La conséquence diffère : l'une entraîne l'issue que Lazar doit trancher, l'autre non. À écrire, dans un sens ou dans l'autre.

2. **Provenance : avant ou après l'acte de reprise ?** Le texte dit que la garde de la provenance joue « avant toute garde de la liste fermée », et ailleurs que l'acte de reprise est écrit « avant toute lecture ».
   - Le code lit `piece_source` avant d'écrire l'acte. Une pièce qui n'est pas la bonne ne dépense donc pas la ligne de GO ; la bonne pièce se lit ensuite sous la même ligne.
   - Dans l'autre ordre, une pièce d'un autre module coûterait une ligne de GO neuve, donc un mot de Lazar. À écrire.

3. **Après le fichier des grandeurs, le résultat de la règle ne se recompose plus.** Le texte dit que l'étape (n) ne se rejoue pas dès que son fichier existe. Le code refuse alors `lire_fichier_des_rangs`, et aussi `resultat_pour_l_etape_n`, qui recompose le résultat de la règle sur les pièces scellées sans rien relire du fichier des scores.
   - Conséquence pour l'enchaînement : ce qui se rapporte du résultat de la règle, dont le rapport de la ligne C4, doit être composé avant la fin de l'étape (n).
   - À écrire : soit cela, soit que recomposer ce résultat pour un rapport n'est pas un rejeu. Le code fait le premier.

## B. Ce que le texte doit dire, sans changer aucune règle de jugement

### Programme du constat

4. **Le nom du programme.** Le texte nomme `scripts/constat_de_lancement_discretion_bras_a_v1.py`. La version 1 est scellée et n'est pas modifiée (R12) ; le programme à huit champs, par le sens et à mode de contrôle est `scripts/constat_de_lancement_discretion_bras_a_v2.py`. À écrire : ce nom.
5. **« Le même constat, sur les mêmes entrées ».** Un contrôle ne peut pas avoir les mêmes entrées que le constat d'origine : le registre courant, son commit et la date sont ceux du moment du contrôle, et c'est ce qu'on veut. Le code prend la même configuration, le même état figé, la même ligne de GO, et le registre courant, le commit et la date qu'on lui donne. À écrire ainsi.
6. **Ce que le programme refuse de plus.** Le code s'arrête, sans constat, quand la ligne de GO donnée ne se lit pas comme un accord dans l'état figé, ou ne cite pas le module et le rapport de la configuration ; quand une ligne de GO est donnée pour une première livraison, ou manque pour une livraison refaite ; quand la configuration inscrit une autre empreinte de programme que la sienne. Le texte ne liste pas ces refus.
7. **Sortie d'un constat sain.** Le texte dit ce que le programme écrit sur sa sortie quand le constat est malsain, ou en mode de contrôle. Le code écrit la même ligne JSON à huit champs quand le constat est sain. Un arrêt du programme n'écrit rien sur la sortie standard.
8. **Deux lignes d'inscription pour une configuration.** « Une seule par configuration » et « cette ligne, et elle seule, cite l'empreinte » : avec deux lignes d'inscription, le code dit la configuration non inscrite, sans dire une révocation. Le constat est malsain ; le texte ne dit pas lequel des deux champs le porte.
9. **« Puis l'empreinte entière ».** Le code admet, entre la marque et l'empreinte, des signes qui ne sont ni lettres ni chiffres, et rien d'autre. Le type est comparé sans égard à la casse ni aux accents ; la marque, à la lettre.
10. **Lignes regardées pour les valeurs fictives.** Dans le registre courant, le code regarde toute ligne qui cite l'empreinte de la configuration, qu'elle soit ou non sa ligne d'inscription, et toute ligne entrée depuis l'état figé qui nomme la ligne de GO. Dans l'état figé, il ne regarde que la ligne de GO donnée ; la version 8 regardait toutes les lignes d'accord. Une ligne de GO donnée qui est elle-même `GO-0000-00-00-00` est refusée avant toute lecture du registre.

### Registre, dans l'état figé

11. **« Une ligne entrée après elle ».** Le code prend l'ordre des lignes dans la pièce : une ligne placée après la ligne de GO. Une ligne placée avant elle qui la nomme n'arrête rien.
12. **La ligne de l'écart à R9.** Elle se lit par la même fonction que la ligne d'une reprise : la règle « par le sens » vaut donc aussi pour elle. Le texte ne le dit que « pour une reprise ».

### Fichiers scellés

13. **Ce que porte `grandeurs`.** Le texte en dit le sens, non la forme. Le code y range six parties : `aire_conditionnelle` (par dose, puis par moniteur), `cles_des_tirages`, `lectures_rapportees` (cas, cause, motif, grandeurs marquées, comptes, effectifs, aux quatre doses, sans état ni règle), `agregateur`, `exclues`, `autres_grandeurs`. Les trois parties tirées de la pièce scellée sont recomposées par le code, et relues à chaque lecture du fichier.
14. **Noms de la valeur ajustée.** `valeur_p_haut_holm` porte la fraction exacte, écrite « numérateur/dénominateur » ; `valeur_p_haut_holm_arrondie` porte le nombre à virgule. Le texte laisse le choix entre fraction et écriture décimale exacte ; le code prend la fraction.
15. **Le résultat de la règle porte son constat.** Un champ `constat_de_lancement` (empreinte, date, commit, ligne de GO) s'ajoute au résultat, pour le manifeste. Ce n'est pas un fichier du texte.

### Somme et maximum de l'agrégateur

16. **Sous quelles clés, et combien de doses.** Le code exige une table aux quatre doses et à elles seules, sous les clés que la configuration inscrit pour `lectures` (`cles_des_doses_dans_lectures`). Trois doses, ou d'autres clés : le champ est « non rapporté » en entier. À confirmer avec la réponse à la demande 31.

### Garde statique

17. **La liste des chemins à élaguer** reste à confirmer par le lecteur habilité. Un fichier qui porte plusieurs noms n'est plus ouvert ; le cloisonnement de T0.8 tient toujours aux noms.
