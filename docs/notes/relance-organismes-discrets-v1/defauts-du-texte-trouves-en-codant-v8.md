# Défauts du brouillon 28 trouvés en écrivant la version 8 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md` (`604e0410f251c903c7e34d37762292ccafbdac821c2e08d0779f3886991736e9`). Lu : les lignes qui diffèrent des brouillons 25 à 27 en « conventions », 6.9, 8.4 et 13 ; ses notes. Le reste du texte n'a pas été relu.
- **Code** : les modules `…_v8.py` et `scripts/constat_de_lancement_discretion_bras_a_v1.py` (note `code-v8-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est muet, ambigu ou contraire à lui-même pour coder ; ce que le code fait ; ce qu'il faudrait écrire. La partie A dit ce qui touche une règle de jugement ou sa conséquence ; la partie B, le reste.
- Les cinq questions déjà posées à Lazar ne sont pas reprises : le code les porte comme des choix nommés, sans valeur.

## A. Ce qui touche une règle de jugement, ou sa conséquence

1. **Dans quelle arithmétique l'état se dit.** Les règles (α) et (β) comparent en fractions exactes, puis la valeur rendue est « prise telle quelle ». Le texte ne dit pas comment l'état se calcule ensuite.
   - Le cas : une écriture longue que (α) et (β) admettent, et que le nombre à virgule le plus proche arrondit de l'autre côté d'un niveau. `0.0033333333333333333343` dépasse 0,05 ÷ 15, comme sa formule 7 ÷ 2 001 ; quinze fois le nombre à virgule ne dépasse pas 0,05. En nombres à virgule, le moniteur « repère » ; sur sa formule, non.
   - Le code dit les états en fractions exactes, sur l'écriture décimale : rejets de Holm, valeur p basse contre 0,05, borne haute contre 0,60. Il exige que la valeur de la famille s'écrive comme la valeur p haute, et refuse une écriture hors de ]0 ; 1]. Les valeurs ajustées rapportées restent des nombres à virgule, calculés sur les valeurs rendues.
   - À écrire, en 6.9 : « les comparaisons qui disent un état se font sur l'écriture décimale de la pièce, en fractions exactes ». Ou dire le contraire, et je retire l'ajout. Sur des écritures de six décimales, les deux lectures donnent les mêmes états.

2. **« Sous la même configuration (même empreinte) » : rien ne garde cette empreinte.** L'acte de reprise a quatre champs. Au rejeu d'une livraison refaite, le code ne peut pas savoir sous quelle configuration la première lecture était partie.
   - Le code confronte de nouveau la ligne de GO de l'acte à la configuration donnée : module et rapport doivent être ceux qu'elle inscrit. Une configuration aux mêmes empreintes et à d'autres chaînes passerait.
   - À écrire : un cinquième champ à l'acte, `sha256_de_la_configuration`. Le code le vérifierait au rejeu.
   - Pour une première livraison, aucune pièce ne dit qu'une lecture a été interrompue : le code rejoue sans le voir, et `rejeu_sous_le_meme_acte` reste faux. Le « rejeu consigné au manifeste » y est donc à la charge de la session qui lance. À dire.

3. **Le résultat de l'étape (n) n'a pas de pièce.** « À l'étape (n), ce sont les grandeurs rendues de cette étape, ou un fichier d'arrêt. » Le fichier d'arrêt, le code le voit. Les grandeurs rendues, non : aucun fichier nommé ne les porte.
   - Le code refuse de rejouer l'étape (n) après son fichier d'arrêt, et seulement alors. Une étape (n) aboutie peut être rappelée ; elle rend les mêmes grandeurs, les clés des tirages étant fixées.
   - À écrire : le nom du fichier scellé des grandeurs de l'étape (n), ou que le rappel d'une étape (n) aboutie n'est pas une relecture.

4. **Constat de lancement : six points où le texte ne suffit pas pour coder.**
   - (a) **« La ligne de GO que la lecture emploie »** n'est ni une entrée du programme ni un champ du constat. Le programme la retrouve : toute ligne de l'état figé qui porte la phrase d'accord d'une livraison refaite et cite le module et le rapport de la configuration ; la révocation de l'une quelconque compte. L'analyse ne peut pas vérifier que le constat vise la ligne qu'elle emploie. À écrire : la ligne en entrée, et un septième champ `ligne_de_go` (`null` pour une première livraison), que l'analyse confronte.
   - (b) **Constat malsain : « il rend un fichier scellé », puis « le constat est refait ».** Un fichier scellé ne s'écrase pas (R12). Le code n'en scelle pas : le constat malsain est affiché, le programme sort en échec, et le constat se refait sans rien écraser. À écrire ainsi, ou nommer le fichier du constat malsain.
   - (c) **« Un constat écrit à la main, sans le programme » : refusé — par qui ?** Un fichier scellé aux six bons champs n'est pas distinguable de celui du programme. Le code ne le refuse pas. À écrire : c'est une garde du manifeste, tenue par la session ; ou ajouter au constat l'empreinte du programme.
   - (d) **« Absent du manifeste »** : le programme d'analyse ne lit pas le manifeste. Il ne vérifie que le dossier de la livraison.
   - (e) **Un registre courant qui n'est pas la suite de l'état figé.** Le texte ne le prévoit pas. Le code s'arrête si une ligne de l'état figé manque au registre courant.
   - (f) **Ce qu'est une révocation, et ce qu'est « inscrite ».** Le code retient : une ligne de type « révocation » qui nomme l'identifiant ; l'empreinte entière de la configuration lue dans une ligne quelconque du registre courant. À confirmer.

5. **Valeurs de l'exemple fictif : la portée du refus** (précision de la session principale, à porter au prochain brouillon). Le programme du constat refuse une empreinte de soixante-quatre zéros inscrite dans la configuration, et une ligne d'identifiant `GO-0000-00-00-00` ou citant soixante-quatre zéros. Pour les lignes, le code ne regarde que celles sur lesquelles le constat s'appuie : lignes d'accord d'une livraison refaite dans l'état figé, lignes qui inscrivent la configuration dans le registre courant. Une telle ligne ailleurs au registre n'arrête pas : le registre ne perd jamais de ligne, et l'arrêt serait sans remède. À écrire : la portée voulue.

## B. Ce que le texte doit dire, sans changer aucune règle de jugement

### Configuration scellée

6. **La clé de `piece_source` qui porte l'empreinte du module n'a pas de nom au texte** (vérification du code, M-6 ; demande 18). Le code lit une chaîne de plus dans `chaines_du_module`, `cle_du_module_dans_piece_source` ; nulle, `piece_source` n'est pas lu. Inscrite, une livraison dont `piece_source` ne porte pas l'empreinte du module est refusée, sous la garde de la forme, champ `piece_source` : cette cause de refus n'est pas dans la liste fermée de 6.9. À écrire : le nom de la chaîne, et la ligne de la liste.
7. **`dossier_des_arrets` : « le chemin », relatif à quoi ?** Le code le lit relatif au dossier de la configuration (`../arrets` dans les essais). Il exige qu'il existe, et qu'il ne soit ni un dossier de livraison, ni sous l'un, ni au-dessus.
8. **Le dossier d'une livraison** : le code exige le nom `livraison-<rang>`, rang entier sans zéro devant, et lit les configurations voisines pour vérifier que les cinq choix et le dossier des arrêts sont les mêmes. Un dossier `livraison-<rang>` sans configuration arrête.

### Étape (m)

9. **Ordre d'écriture des deux fichiers de l'étape (m).** Le texte dit que le résultat est « le fichier scellé de cette étape ». Le code écrit les constats d'abord, le fichier ensuite, pour qu'une panne ne laisse jamais le fichier sans ses constats. À dire.
10. **Les deux champs de plus des constats** : je confirme `revision_refusee` et `taches_gardees_lues`.

### Formes reconnues

11. **Aires de l'agrégateur, « valeur par valeur ».** Le code garde la structure rendue et remplace chaque valeur qui n'est pas un nombre de 0 à 1 par « non rapportée » ; un champ qui n'est ni un nombre, ni une liste, ni une table est « non rapportée » en entier.
12. **`effectifs` et `exclues`, tout ou rien.** Une seule valeur hors forme, et le champ entier est « non rapportés (forme non reconnue) ». Une liste ou une table vide est une forme reconnue.

### Garde statique

13. **La liste des chemins à élaguer** reste à confirmer par le lecteur habilité (demande 17). Elle répond maintenant sans égard à la casse (M-4).
