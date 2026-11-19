# Défauts du brouillon 33 trouvés en écrivant la version 10 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon33.md` (`dc3bc0236e9103454c988fa24997c698306ef78a2328587430bed553a5020c4a`). Lu par passages : conventions, « Constat de provenance » ; 6.9, « Livraison refaite », « Règle d'octroi », « Ce qui n'est pas un refus d'une livraison », « Recomposer n'est pas rejouer » ; trois lignes de 8.4 ; la ligne de 13.2 sur l'écart à R9. Les notes des brouillons 32 (partie 6) et 33 (en entier).
- **Code** : les modules `…_v10.py` et `scripts/constat_de_lancement_discretion_bras_a_v3.py` (note `code-v10-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est muet ou ambigu pour coder ; ce que le code fait ; ce qu'il faudrait écrire. La partie A dit ce qui touche une règle de jugement ou sa conséquence ; la partie B, le reste.
- Les points 19 et 20 de la section 12, encore ouverts, ne sont pas repris : le code les porte comme des choix nommés.

## A. Ce qui touche une règle de jugement, ou sa conséquence

1. **La pièce arrêtée par la garde de provenance, redonnée sous une configuration neuve.**
   - Le texte dit que la pièce arrêtée « a été livrée », et que « la pièce qui la remplace » est une livraison refaite. Il ne dit rien du cas où c'est la configuration qui était fautive — elle inscrivait une mauvaise empreinte de module —, et où l'on redonne la même pièce sous une configuration corrigée.
   - Le code la refuse : la pièce arrêtée tient la place d'une livraison refusée, qui n'est pas relue. Il la refuse aussi sous une ligne de GO.
   - Conséquence : si le module, rejoué avec les mêmes clés, rend la même pièce octet pour octet, rien ne peut la remplacer, et la discrétion reste non lue. À écrire, dans un sens ou dans l'autre.

2. **Une seconde « première livraison » dans une course.**
   - Le texte dit « une configuration par livraison : la première a la sienne ; une livraison refaite a la sienne ». Il ne dit pas en toutes lettres qu'une course ne lit qu'une première livraison, ni ce que le programme confronte pour le tenir.
   - Le code lit, sans ligne de GO, une autre pièce sous une configuration de rang 2 qui n'inscrit aucun registre, quand le rang 1 a été lu sans arrêt. Ce défaut est présent depuis la version 8 ; je ne l'ai vu qu'après le scellement de la version 10.
   - Conséquence : deux lectures de la discrétion dans une course. À écrire : dès qu'une lecture existe dans un dossier de livraison de la course, toute autre pièce demande une ligne de GO. La garde est à coder dans la version suivante.

3. **Recomposer le résultat après un arrêt à l'étape (n).**
   - Le texte dit que recomposer « ne lit aucune livraison refusée ». Il dit aussi que, sous la rédaction retenue de l'issue, un arrêt à l'étape (n) garde la table C, et que « le rapport de la ligne C4 n'a donc pas à être composé avant la fin de l'étape (n) ».
   - Le code refuse de recomposer dès qu'un arrêt est consigné pour la livraison, à l'étape (n) aussi.
   - Conséquence : si l'étape (n) finit par un arrêt, la table C est gardée, mais le rapport de la ligne C4 — la valeur ajustée exacte — ne peut plus être recomposé. À écrire : ou bien recomposer reste permis après un arrêt à l'étape (n), ou bien le rapport de la ligne C4 se compose avant cette étape.

4. **Un constat de provenance laissé sous une livraison refaite.**
   - Le texte ne permet de citer un constat de provenance que « pour une première livraison arrêtée par la garde de provenance ». Sous une livraison refaite, chaque pièce arrêtée laisse aussi son constat.
   - Le code vérifie que le constat cité existe, qu'il vient d'une autre configuration que celle de la lecture, et que sa pièce n'a pas d'acte. Il ne vérifie pas que cette autre configuration était celle d'une première livraison.
   - Conséquence : une ligne inscrite à tort pourrait ouvrir une lecture de plus après une livraison refaite déjà lue. À écrire dans « Ce que le programme confronte » ; le programme peut le tenir, puisqu'une configuration de première livraison est celle qui n'inscrit aucun registre figé.

5. **Erreur de rangement : quelle empreinte fait foi quand le compagnon dément la pièce.**
   - Le texte nomme deux erreurs de rangement : un autre nom, pas de compagnon. Il range à part la pièce qui n'a « pas l'empreinte attendue ».
   - Le code consigne l'empreinte des octets donnés dans quatre cas : compagnon absent, illisible, d'un autre nom, d'une autre empreinte. Dans le dernier, la pièce a été changée après son scellement ; si l'on redonne ensuite les octets d'origine, ceux que le compagnon scellait, ils diffèrent de l'empreinte consignée et passent par la règle d'octroi.
   - À écrire : si une pièce retouchée après scellement est une erreur de rangement, et laquelle des deux empreintes est « la même pièce ».

6. **Le choix du moniteur appris non ajustable, tant qu'il est ouvert.**
   - Le texte garde deux rédactions du point 20 et attend la réponse du développeur habilité. Il ne dit pas ce qu'une configuration scellée porte en attendant, ni ce que vaut une lecture arrêtée pour cette raison.
   - Le code admet une troisième valeur écrite, « en attente ». Sous elle, le programme s'arrête s'il rencontre ce motif, à quelque dose que ce soit : garde ordinaire, sans événement, sans fichier d'arrêt, sans issue, avant l'acte de reprise.
   - À écrire : que cette valeur existe, ou qu'aucune configuration ne se scelle avant le choix. Dans le premier cas, que l'arrêt n'emporte aucune issue.

## B. Ce que le texte doit dire, sans changer aucune règle de jugement

### Registre

1. **La phrase d'accord de l'écart à R9.** Le texte dit l'écart « accepté par Lazar » et renvoie au mot. Il ne donne pas la phrase que la ligne de GO doit porter. Le code exige « écart à R9 accordé pour la table des identifiants opaques » ; le mot dit « écart à R9 : entropie propre de la table des identifiants opaques » — « accepter ». Une ligne aux mots du mot n'ouvre pas la porte. À écrire : la phrase exacte, en 13.2, et la reprendre à la lettre dans la ligne du registre.
2. **La porte de l'écart à R9 pour une première livraison.** Elle lit sa ligne dans une pièce de l'état figé du registre, reconnue à son empreinte. Une configuration de première livraison n'inscrit aucun registre figé. À écrire : d'où viennent cette pièce et son empreinte pour une première livraison.
3. **Abrégés d'empreinte.** Le code voit un abrégé dès seize signes. Les abrégés de huit ou douze signes, d'usage dans les notes, ne sont pas vus. À rappeler à qui tient le registre : l'empreinte entière.
4. **La ligne de GO d'un remplacement** porte, pour le code, la même phrase d'accord que celle d'une livraison refaite. À écrire, si le texte veut une autre phrase.

### Programme du constat

5. **Son nom.** Le texte nomme `scripts/constat_de_lancement_discretion_bras_a_v2.py` et dit qu'une version de plus prend un nom neuf. La version 10 du code emploie `scripts/constat_de_lancement_discretion_bras_a_v3.py` (`6ee84152920d0dffe46f0a289279a961648946812ea53e0a86fd28ad7368b17c`). À nommer au prochain brouillon.
6. **Fichiers de contrôle.** « Daté après le constat d'origine » est lu « strictement après ». « Le plus récent » est le plus grand champ `date_utc`. Le résultat de la règle porte le contrôle sous `controle_de_lancement`, à trois champs : empreinte, date, commit. À écrire, si ces noms doivent être ceux du texte.
7. **Le drapeau du rejeu.** `rejeu_sous_le_meme_acte` ne se relit sur aucune pièce scellée, puisqu'un contrôle peut accompagner toute lecture de l'étape (m). C'est le manifeste qui le porte. À dire comme une limite.

### Constats de pièce donnée

8. **Les valeurs du champ `constat` d'un constat de provenance.** Le texte décrit cinq natures sans en fixer la lettre. Le code écrit : « pièce qui n'est pas du JSON » ; « pièce qui n'est pas un objet JSON » ; « `piece_source` absent ou mal formé » ; « clé de provenance absente de `piece_source` » ; « empreinte d'un autre module ». Sous la clé, une valeur qui n'est pas une empreinte entière — `null`, une liste, des majuscules — est rangée « mal formé ». À fixer à la lettre.
9. **Le constat d'erreur de rangement.** Le texte dit que la session qui lance consigne l'empreinte au manifeste. Le code l'écrit lui-même, dans un fichier scellé du dossier des arrêts : `erreur-de-rangement-bras-a-<seize signes>.json`, aux quatre champs du constat de provenance, l'événement « erreur de rangement », et l'une de quatre natures. Une ligne de GO peut le citer à la place d'un fichier d'arrêt. À écrire, avec son nom, ses champs et ses natures, et une ligne de 8.4.
10. **« Au nom attendu ».** Le texte dit que la sortie de la lecture commune est donnée « au nom attendu ». Il ne fixe aucun nom pour cette pièce, et le code n'en exige aucun : « un autre nom » y veut dire que le compagnon nomme un autre fichier. À écrire : le nom, ou retirer ces mots.
11. **Les autres pièces.** L'erreur de rangement n'est consignée que pour la sortie de la lecture commune. Le fichier des scores par unité, la configuration et le registre sont chacun liés par leur empreinte, inscrite ailleurs. À dire, pour que la ligne de 8.4 ne promette pas plus.
12. **Le rapport.** Le code compte les constats sous deux noms : `constats_de_provenance` et `constats_d_erreur_de_rangement`. Il ne dit pas, pour chaque constat, si une reprise a été demandée : c'est au rapport de le dire, comme pour un arrêt.
