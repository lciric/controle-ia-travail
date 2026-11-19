# Défauts du brouillon 25 trouvés en écrivant la version 7 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md` (`ab5fc58ee69813288923cbd316848b0b25275659590e5f84e17e498b69d620da`). Lu : toutes les lignes qui diffèrent du brouillon 24 en « conventions », 6.9, 8.4, 10 et 13.2 ; et sa note (`3732b6b4…`), en entier. Le reste du texte n'a pas été relu.
- **Code** : les modules `…_v7.py` (note `code-v7-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est muet, ambigu ou contraire à lui-même pour coder ; ce que le code fait ; ce qu'il faudrait écrire. La partie A dit ce qui touche une règle de jugement ou sa conséquence ; la partie B, le reste.
- Les cinq questions déjà posées à Lazar ne sont pas reprises : le code les porte comme des choix nommés, sans valeur.

## A. Ce qui touche une règle de jugement, ou sa conséquence (à trancher par le rédacteur du texte, ou par Lazar)

1. **« Une livraison refaite est lue une fois, sans relecture » : après un incident de machine, elle ne peut plus être lue.**
   - Le code écrit l'acte de reprise avant la lecture, comme le texte le veut. Si le programme tombe entre l'acte et la fin de la lecture, la livraison refaite porte déjà son acte : elle est refusée à la relecture, même sur une ligne neuve.
   - La règle de discrétion est déterministe : une relecture rendrait le même résultat. Le refus ne protège donc d'aucune retouche ; il peut seulement faire perdre la lecture de la discrétion sur une panne.
   - À écrire : soit « c'est voulu, la discrétion reste alors non lue », soit « la même livraison, sous le même acte, peut être rejouée à l'identique ». Le code fait le premier.
2. **Une révocation de la ligne de GO après la lecture.** Le registre dit qu'une révocation est une ligne neuve. Le code refuse, à la lecture, une ligne de GO qu'une ligne de type « révocation » nomme. Après la lecture, c'est l'acte de reprise scellé qui fait foi : une révocation postérieure n'est pas vue, et le texte ne dit pas ce qu'elle vaudrait.

## B. Ce que le texte doit dire, sans changer aucune règle de jugement

### Configuration scellée de l'analyse

3. **« Deux parties et elles seules » : le code en a trois.** La troisième, `pieces_attendues`, porte deux empreintes que le code doit connaître sans pouvoir les deviner :
   - `sha256_du_registre_des_accords` : l'empreinte du registre de la branche principale, ou `null`. Le texte demande que « le registre lu soit celui de la branche principale » sans donner de moyen ; celui-ci est sans réseau (note du code, partie 4).
   - `sha256_du_module_du_cote_habilite` : l'empreinte du module dont les chaînes sont inscrites (case du module, 13.1). Elle sert au point 20 sous le choix « module corrigé » (vérification du code, M-6) et à la ligne de GO d'une reprise (point 6 ci-dessous).
4. **Une reprise demande une configuration neuve.** Le texte dit la configuration « inscrite au registre avant la réception de la sortie de la lecture commune », une fois. Or la ligne de GO d'une reprise change le registre, donc son empreinte attendue ; et le module corrigé peut changer ses chaînes. Le code lit une configuration par livraison ; son nom étant fixé, la seconde se range dans un autre dossier. À écrire.
5. **Les deux chaînes de plus n'ont pas de nom au texte.** Le code les nomme `doses_du_fichier_des_scores` (une valeur par dose) et `condition_de_l_honnete_du_fichier_des_scores`.

### Livraison refaite

6. **6.9 et 8.4 ne disent pas la même chose de la ligne de GO.** 6.9 : une ligne « qui ne cite pas les trois empreintes, ou qui cite un autre fichier d'arrêt, n'ouvre rien ». 8.4 ajoute : « ou un autre module ». Le code suit 8.4 : la ligne doit citer l'empreinte du module que la configuration scellée inscrit. La troisième empreinte, celle du rapport de contre-lecture, est exigée et non vérifiée.
7. **« Citer une empreinte » : entière ou abrégée ?** Le code exige trois empreintes entières (64 signes), ni plus ni moins. Une empreinte abrégée, usuelle au registre, n'est pas comptée.
8. **Quel fichier d'arrêt, quand il y en a plusieurs.** Les fichiers d'arrêt ne portent pas de date. Le code exige que la ligne cite un seul fichier d'arrêt du dossier, et que sa livraison n'ait pas déjà été reprise par un acte. C'est ce qui fait « un autre fichier d'arrêt » sans plafond ; le texte ne le dit pas ainsi.
9. **« Le rapport compte les livraisons lues ».** La première livraison, lue sans acte, ne laisse aucune trace dans le dossier des arrêts. Le code compte les arrêts et les actes ; l'enchaînement ajoute la première.

### Ce que rend le programme qui refuse

10. **Quatre natures : il en manque pour trois défauts.**
    - Une ligne du fichier des scores par unité aux dix bons champs, hors de l'ordre : le code dit « pièce illisible ».
    - Un champ de plus et un champ de moins ensemble : le code dit « un champ de moins ».
    - Un champ en double à l'intérieur d'un champ que rien ne contrôle (`effectifs`, `exclues`, `plis`) : le code dit « un champ en double » pour la liste qui le contient.
11. **`lectures` : liste, ou table à clés.** La forme n'est pas transmise (demande 14 de la note). Le code lit les deux. Dans une liste, une lecture dont le champ `moniteur` ou `dose` n'est pas reconnu arrête sans moniteur ni dose dans le constat, puisqu'ils ne sont pas connus.

### Fichier des scores par unité

12. **Nom et compagnon : dans la liste des refus du fichier, mais sans événement.** La liste fermée de 6.9 nomme « un nom autre » et « un compagnon en défaut » ; la note (partie 4) dit que la garde ordinaire reste. Le code lève une garde ordinaire : rien n'est consigné, et l'étape (n) s'arrête sans arrêt nommé ni issue. À dire.
13. **`scores_par_unite.fichier` n'est pas dans la liste fermée.** Le code de la version 6 le contrôlait ; la version 7 ne le lit plus, comme `forme`.
14. **Un fichier vide, annoncé tel, n'est pas dans la liste des refus.** Le code le lit ; chaque aire conditionnelle est alors « non calculable », avec son motif.
15. **« Une `cle` vide ».** Le code tient pour vide : `null`, un texte vide, une liste ou un objet vide. Une clé qui n'est pas un texte est admise.
16. **`tache` et `episode` ne sont pas contrôlés, mais le calcul joint par eux.** Si leur forme ne permet pas de joindre une unité aux seize tâches ou aux 128 épisodes de la dose, le code dit l'aire conditionnelle « non calculable », avec ce motif, sans arrêt. Le texte ne dit pas ce cas ; la version 6 arrêtait par une garde ordinaire.
17. **Le dossier « que rien ne parcourt ».** Le programme d'analyse liste le dossier des arrêts. Le code refuse donc un fichier des scores par unité rangé dans ce dossier ou sous lui. À écrire : ce fichier ne se range pas dans le dossier des arrêts.

### Constats de l'étape (m)

18. **Les deux réglages de la table A ne sont pas dans les huit champs.** La table A se lit avec « révision refusée » et « tâches gardées lues ». Les constats ne les portent pas : le journal est relu sans eux. Un journal fait d'un premier échec de l'épreuve dont la révision a été refusée se relit donc comme « aucune ligne ». L'écriture le refuse ; la relecture ne le voit pas. Deux champs de plus, ou ces réglages dans le journal, fermeraient ce trou.

### Garde statique

19. **La liste des chemins cloisonnés est plus large que les préfixes de la vérification.** Voir la note du code, partie 3 : tout nom qui porte `mots_et_cout_`, `autres_moniteurs_v` ou `bras_a_v2_habilite`, tout dossier nommé `t07…`, `bases` ou `sondes`, toute marque de T0.8. À confirmer (demande 17 de la note du brouillon 25).

## C. Écart à la consigne de la session, non au texte

20. **La tolérance des valeurs p n'est pas lue dans la configuration.** La consigne disait « lu dans la configuration ». Le texte fixe la grille : 2 001 pour la valeur p haute, les permutations calculées pour la basse. Le code prend 2 000 du texte, et l'exige de `reglages.n_permutations` et de chaque lecture.
