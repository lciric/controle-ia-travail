# Défauts du brouillon 34 trouvés en écrivant la version 11 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon34.md` (`0b6413d9d75a838f17aabf46ff714a34c5b086f939e44d6a864326a7e1b247a3`), lu par passages : conventions (constats de pièce donnée, ouverture de lecture, trace de rejeu, valeur « en attente ») ; 6.9, « Ce qu'est la bonne pièce » et « Une seule première livraison par course » ; les deux lignes neuves de 8.4 ; 13.2, phrases d'accord. Sa note, en entier.
- **Précisions reçues en plus**, que le prochain brouillon portera : les quatre points tirés de la vérification du brouillon 34 (M-1 et M-2).
- **Code** : les modules `…_v11.py` et `scripts/constat_de_lancement_discretion_bras_a_v4.py` (note `code-v11-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est muet ou ambigu pour coder ; ce que le code fait ; ce qu'il faudrait écrire. La partie A dit ce qui touche une règle de jugement ou sa conséquence ; la partie B, le reste.

## A. Ce qui touche une règle de jugement, ou sa conséquence

1. **Une configuration inscrite, puis abandonnée avant toute lecture.**
   - La précision demande que le programme du constat refuse une configuration de rang 1 dès que le registre porte la ligne d'inscription d'une autre configuration de l'analyse du bras A, non suivie d'une reprise.
   - Le code le fait à la lettre. Une configuration de rang 1 inscrite, jamais lue, puis remplacée — une faute dans une chaîne du module, par exemple — fait donc refuser toute configuration de rang 1 suivante : aucune ligne de reprise ne peut suivre son inscription, puisqu'une reprise demande un arrêt ou un constat de pièce donnée.
   - Conséquence : la discrétion ne se lirait plus dans ce registre. À écrire : le remède — par exemple, une ligne qui retire l'inscription, que le programme reconnaîtrait.

2. **Les mêmes choix pour toutes les livraisons, et la valeur « en attente » qui se tranche.**
   - Les conventions disent que les cinq choix « sont les mêmes pour toutes les livraisons ». 6.9 dit que, « quand le choix « en attente » est tranché », la même pièce est redonnée « sous une configuration neuve et une ligne de GO ». Dans une course, la configuration neuve porte un autre choix que la première : les deux phrases se heurtent.
   - Le code admet une seule exception : une configuration de rang supérieur peut porter une rédaction du point 20 là où celle de rang inférieur portait « en attente ». Jamais l'inverse, jamais un autre choix.
   - À écrire : cette exception, ou qu'une course sous « en attente » se refait en entier. L'une et l'autre disparaissent avec la valeur au scellement.

3. **Ce qu'un constat de pièce donnée peut ouvrir.**
   - 6.9, point (5), dit qu'« après une première livraison lue sans arrêt, aucune autre pièce ne se lit dans la course ». « Ce que le programme confronte » ne demande pourtant au constat cité que d'exister, sans acte, et de venir d'une première livraison.
   - Sans plus, une pièce quelconque donnée sans compagnon après une lecture aboutie laisse un constat d'erreur de rangement, fait sous la configuration de la première livraison ; une ligne de GO qui le cite ouvrirait une seconde lecture.
   - Le code ferme cette voie : un constat de pièce donnée n'ouvre que la première lecture de la course. Dès qu'une ouverture de lecture ou un autre acte de reprise existe, seule une livraison refusée par un arrêt se reprend.
   - À écrire dans « Ce que le programme confronte ».

4. **Le contrôle « fait pour ce rejeu ».**
   - Le texte exige pour tout rejeu un contrôle « fait pour ce rejeu », et dit qu'un contrôle que porte une trace n'en ouvre aucun autre.
   - Une première lecture n'exige aucun contrôle ; s'il y en a un, il doit être sain, et la lecture part sans trace. Si une panne suit, ce même contrôle, fait avant le premier départ, est le plus récent et ne porte aucune trace : le code le prend pour le rejeu. Rien de scellé ne date le premier départ.
   - À écrire : ou bien que ce cas est une limite, ou bien que tout départ sous un contrôle laisse une marque.

5. **« Ponctuation finale admise ».**
   - Le texte admet « une ponctuation finale » après la phrase d'accord, sans dire laquelle. Un point d'interrogation change le sens.
   - Le code n'admet qu'un point final.
   - À fixer à la lettre.

## B. Ce que le texte doit dire, sans changer aucune règle de jugement

### Programme du constat

1. **Son nom.** Le texte nomme la version 3. La garde du registre demande un programme de plus : `scripts/constat_de_lancement_discretion_bras_a_v4.py` (`8ca94b7c9109cdd315457f0d5cbd7f1d5d4ad38b48ece9010b13244da3e73fee`). À nommer, avec son empreinte.
2. **« Suivie d'une reprise ».** Le code tient une inscription pour suivie d'une reprise dès qu'une ligne placée après elle porte, en cellule d'objet, la phrase d'accord d'une livraison refaite, et n'est pas une révocation. Il ne vérifie pas que cette reprise concerne cette configuration. À écrire, si le texte veut plus.
3. **Ce qu'est une ligne d'inscription d'une configuration de l'analyse du bras A** : type « inscription », la marque, puis une empreinte entière. C'est la forme déjà écrite ; la garde lit toute ligne de cette forme, quelle que soit l'empreinte.

### Lignes d'accord

4. **Le gras.** Le code ôte les deux astérisques du gras avant de comparer la cellule d'objet. Il n'ôte ni les accents graves, ni l'italique, ni les guillemets : une cellule ainsi mise en forme n'ouvre rien. À dire à qui tient le registre.
5. **La cellule d'objet** est la quatrième de la ligne, par une constante nommée. À confirmer par la session principale.
6. **Les trois empreintes d'une ligne de reprise** sont comptées sur la ligne entière. Le texte dit que la ligne renvoie aussi au mot de Lazar : écrit avec son empreinte entière, ce renvoi ferait une quatrième empreinte, et la ligne n'ouvrirait rien. À écrire : le renvoi se fait par le chemin, ou par une empreinte abrégée.
7. **La porte de l'écart à R9 et le registre courant.** La porte reçoit le registre courant en plus de l'état figé. C'est le lanceur du côté habilité qui le lui donne ; cela s'ajoute à ce que sa configuration doit inscrire.

### Fichiers scellés

8. **Le champ du résultat qui dit le rejeu** s'appelle encore `rejeu_sous_le_meme_acte` ; il vaut maintenant aussi pour le rejeu d'une première livraison, sous son ouverture. À renommer, si le texte nomme ce champ.
9. **Le résultat dit son ouverture** sous `ouverture` : l'empreinte du fichier, ou `null` pour une livraison refaite.
10. **Constat d'erreur de rangement, « compagnon d'un autre nom ».** Le compagnon nomme un autre fichier, mais il scelle une empreinte : le code la consigne, et c'est elle « la même pièce ». C'est la lettre du texte ; à confirmer pour ce cas.
11. **Le rapport** compte sous cinq noms : `constats_de_provenance`, `constats_d_erreur_de_rangement`, `constats_de_piece_en_attente`, `ouvertures_de_premiere_livraison`, et les arrêts par étape. Il ne compte pas les traces de rejeu, qui sont dans les dossiers des livraisons.
12. **Une configuration de rang 1 qui inscrit un registre figé.** Le texte dit qu'un rang supérieur à 1 en inscrit un ; il ne dit pas l'inverse. Le code l'admet : sa ligne de GO n'aurait rien à citer.
