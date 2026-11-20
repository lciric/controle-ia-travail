# Défauts du brouillon 35 trouvés en écrivant la version 12 du code — relevé du rédacteur Claude Fable 5.2

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md` (`e62b4caec484f53c2afde2c7361136434eaa15ddb15b2f0e609c64edc3f757a2`), lu par passages : 6.9, « Périmètre d'une reprise après un arrêt à l'étape (n) » ; 8.4, lignes « périmètre d'une reprise après un arrêt à l'étape (n) » et « garde du registre au constat : une autre configuration inscrite » ; conventions, garde du registre et septième champ de l'acte de reprise.
- **Corrections reçues en plus**, que le brouillon 36 portera : C-1 et M-1 de la vérification du brouillon 35 (`765f906b830a72fbb3dc99a1fdb8b96b03d00c5c5b843379a6cf3f13ce563e0e`).
- **Code** : les modules `…_v12.py` et `scripts/constat_de_lancement_discretion_bras_a_v5.py` (note `code-v12-bras-a-note-v1.md`).
- **Forme** : pour chaque point, où le texte est muet ou ambigu pour coder ; ce que le code fait ; ce qu'il faudrait écrire. La partie A dit ce qui touche une règle de jugement ou sa conséquence ; la partie B, le reste.

## A. Ce qui touche une règle de jugement, ou sa conséquence

1. **La même configuration, copiée dans un autre dossier de course.**
   - **Ce que j'ai vérifié par un essai.** Je copie le fichier de configuration et son compagnon dans le `livraison-1/` d'une autre course, qui a son propre dossier des arrêts. Les deux fichiers ont la même empreinte : la ligne d'inscription vaut pour les deux. Le programme du constat rend deux constats sains. Je lis la pièce A dans le premier dossier, la pièce B dans le second : « ne repère pas », puis « repère ». Aucune garde ne parle.
   - **Pourquoi.** Le dossier des arrêts est nommé par un chemin relatif au fichier de configuration. La garde du registre compare des empreintes de configuration ; elle ne distingue pas deux dossiers qui portent la même. Le programme d'analyse ne voit que le dossier que sa configuration nomme.
   - **Ce que le code fait** : rien de plus. Il ne peut pas voir un autre dossier.
   - **Ce qu'il faudrait écrire.** Soit une garde de procédure dite comme telle : la session qui lance n'a qu'un dossier de course par configuration inscrite, et son manifeste le montre. Soit un lien au registre : l'empreinte de l'ouverture de lecture est inscrite avant que le fichier de l'étape (m) soit opposable, et une configuration n'a qu'une ouverture inscrite. La seconde ferme ; la première consigne.
   - **Portée** : c'est une seconde première livraison sans mot de Lazar, de même nature que celle que la garde du registre voulait fermer. Elle demande de copier un fichier scellé, ce qui se voit dans l'arbre, mais pas au registre.

2. **Confrontation des vingt lectures : avant ou après l'acte de reprise.**
   - Le texte ne la porte pas encore. Le code la fait **après** l'acte : la ligne de GO est dépensée par une sortie refaite incohérente.
   - L'autre lecture : la faire avant l'acte, comme la garde de la provenance, qui scelle son constat sans dépenser la ligne. Une sortie refaite cohérente pourrait alors être donnée sous la même ligne.
   - À écrire : laquelle des deux.

3. **Une livraison refaite incohérente se reprend-elle ?**
   - Le code : non. Son constat n'est ni un fichier d'arrêt ni un constat de pièce donnée, et aucune ligne ne peut le citer. L'arrêt d'origine est déjà porté par un acte. Les grandeurs de l'étape (n) de la course restent « non rapportées », sans retour.
   - C'est l'issue que l'option (c) donne déjà à ces grandeurs, mais ici elle devient définitive sur une seule sortie fautive du côté habilité.
   - À écrire : si une ligne de GO peut citer ce constat pour ouvrir une autre reprise de l'étape (n), et à quelles conditions.

4. **Ce que « les mêmes lectures » veut dire.**
   - Le code compare ce que porte la clé `lectures`, en entier : même forme, mêmes lectures, mêmes champs, mêmes nombres en fractions exactes. L'ordre des clés ne compte pas ; l'ordre d'une liste de lectures non plus. Un entier vaut le même nombre écrit avec une virgule.
   - Deux points à trancher : une sortie refaite qui donne ses lectures en liste quand l'origine les range par dose est tenue pour incohérente ; un champ de plus dans une lecture aussi.
   - Une sortie refaite dont les lectures ne se lisent pas — pièce illisible, clé absente, clé en double — est incohérente, et non un arrêt.

5. **Les contrôles de lancement à l'ouverture d'une reprise de l'étape (n).**
   - Le texte donne sept champs à l'acte de reprise. Pour une reprise de l'étape (n), le code y écrit le contrôle le plus récent, qui doit être sain, comme à tout premier départ.
   - Il n'exige aucun contrôle pour rappeler l'ouverture sous le même acte, ni pour lire le fichier des scores : l'étape (n) n'a jamais regardé les contrôles.
   - À écrire : si le rejeu d'une étape (n) interrompue demande un contrôle.

## B. Ce que le texte doit dire, sans changer aucune règle de jugement

### Programme du constat

- **Version 5.** Le brouillon 35 nomme la version 4. Le comportement change : la garde du registre ne se lève plus que par une révocation. Le brouillon 36 doit nommer `constat_de_lancement_discretion_bras_a_v5.py` et son empreinte, `fd5fddcd893e2cee91765ced911948009eb09ebd3b2382bc585fb7e4700ce290`.
- **« Refuse » ou « constat malsain ».** Les conventions disent que le programme refuse ; la ligne 8.4 dit « constat malsain, la lecture ne part pas ». Le code arrête le programme, sans constat ni fichier, code de sortie 2. La ligne 8.4 est à accorder.
- **Forme de la ligne qui retire.** Le code exige : une ligne de la table, dont la cellule de type est exactement « révocation » (sans le gras, sans égard à la casse ni aux accents), entrée après la ligne d'inscription, et qui cite l'empreinte entière. Un abrégé ne retire rien. La consigne de tenue du registre (13.2) doit le dire.
- **Une configuration inscrite de nouveau après son retrait** compte de nouveau. Une révocation qui cite deux empreintes retire les deux.
- **Une configuration de rang supérieur à 1 compte aussi.** Pour qu'une configuration de rang 1 parte après une course abandonnée, chaque configuration inscrite de cette course doit être retirée, rang 2 compris.
- **L'artefact de 8.4 qui dépendait de la dispense** (« une ligne … qui porte la phrase d'accord … sans citer l'empreinte … ») est à retirer : toute ligne de reprise laisse la garde fermée.

### Reprise de l'étape (n)

- **Ce qui est lu de la sortie refaite.** Le texte dit : son compagnon, sa provenance, la clé `scores_par_unite`. Avec la confrontation, il faut ajouter : ses vingt lectures, pour la seule comparaison, sans qu'aucune soit rangée dans un cas.
- **La sortie d'origine est une entrée.** Le programme la reçoit de l'appelant et la reconnaît à l'empreinte que portent les constats de l'étape (m). Le texte dit comment elle est reconnue, non qu'elle est redonnée.
- **Les chaînes du module.** Le fichier des scores refait se lit sous la configuration de la livraison refaite ; ce que la règle rapporte de chaque lecture se recompose sous la configuration du rang d'origine. À dire, pour le cas où un module corrigé change une chaîne.
- **Une pièce refusée avant l'acte.** Une sortie refaite arrêtée par la garde du rangement ou de la provenance laisse son constat et ne dépense pas la ligne, comme pour toute livraison refaite. À dire pour cette reprise aussi.
- **Où se demande l'issue.** Après une reprise aboutie, les issues se demandent avec la sortie refaite et sa configuration ; la table C vient du fichier de l'étape (m) d'origine.
- **Le rapport** compte les reprises de l'étape (n) et les livraisons refaites incohérentes.

### Fichiers scellés

- **Constat de livraison refaite incohérente** : `livraison-refaite-incoherente-bras-a-<seize signes>.json`, dans le dossier des arrêts, quatre champs — `evenement`, `sha256_de_la_livraison_refaite`, `sha256_de_la_livraison_d_origine`, `sha256_de_la_configuration`. Nom et champs sont les miens ; le brouillon 36 peut les changer.
- **Libellé de l'issue** : « non rapportées : livraison refaite incohérente », sans nom de garde à la suite, à la différence de « non rapportées : livraison refusée (garde : …) ».
