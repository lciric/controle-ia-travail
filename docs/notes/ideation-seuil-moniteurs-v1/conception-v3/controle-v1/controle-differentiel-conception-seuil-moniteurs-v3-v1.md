# Contrôle par différentiel — conception v3 de la course « seuil et moniteurs » — v1

- Signé : contre-lecteur de la conception seuil et moniteurs, modèle O (le même qu'à la v1 et à la v2). 2026-11-21. Python 3.13.18.
- Statut : pièce de travail. Aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde.
- **Table v3** `empreintes-dossier-v3.txt`, `9615de873144a5f61f27804cfb72fe2e618fa5f149e429ee967c98d93d2f9be6` :
  - identique dans le dossier versé et dans le dossier du rédacteur ;
  - `sha256sum -c` dans le dossier du rédacteur rend vingt lignes « OK » ;
  - les cinq pièces versées de `conception-v3/` sont à leurs empreintes.
- Registre relu sur `origin/main` au commit `c9d7faf24a1e5c746d0d1e4a901d40bc86e9aba2` (`registres/decisions.md` : `169bfbd3…`) :
  - R-4399 (D-M6 à D-M10) ;
  - **R-4410** (07:24Z) ;
  - **R-4412** (07:32Z, D-M7 précisée : « les cinq propositions nommées par GO-2026-11-21-15 […] passent en premier ; le tirage ordonne le reste »).
- Note du moniteur de dissonance relue par extraits sur `origin/main` (`403fe3e2…`, égale) : test de mort n° 1, « monde B » sur MATH500, et devis à part.

## 0. Verdict : **À corriger**

Deux corrections, puis la v3 est à sceller :

1. **D-M7** : la « lecture du rédacteur » est retirée. Les quatre entrées nommées par la mère à 07:32Z (cinq propositions) passent toutes en premier, dans l'ordre (§ 5), dans le préenregistrement (Hypothèse, point 3) et dans le rapport (D-M7, avec le compte de places de l'option (a)).
2. **Documents qui font foi du préenregistrement** : ils nomment encore les *fichiers* `…-v2.md` et la « table d'empreintes v2 ». La règle « v2 se lit v3 » ne couvre pas un nom de fichier : scellé tel quel, le texte se lierait à l'ordre et au devis v2, qui ne portent pas les corrections. J'y ajoute la contre-lecture de la v2 et les décisions de la mère sur cette course. La dernière ligne du rapport (« table d'empreintes v2 ») est corrigée de même.

Tout le reste est conforme. Jeu : huit remplacements en trois JSON ; chaque ancre est comptée une fois ; l'essai sur copie passe (§ 7).

## 1. La passe 1 : égale à mon essai, et rien d'autre n'a changé

- **Pas de `cmp` direct sur les fichiers de la passe 1** : leurs noms ne sont pas dans la table du rédacteur, et l'en-tête m'interdit toute liste.
- **J'ai fait mieux : reconstruit la v3 entière.** Je suis parti de mes quatre sorties d'essai de `essai-v2/` (`917868db…`, `ee0bea71…`, `b984983c…`, `3f9c4a67…`, les empreintes que tu cites). J'y ai appliqué, avec l'outil contre-lu, les jeux de la passe 2 (5, 6, 3 et 2 remplacements, tous « FAIT »), puis ceux de la passe 3 (3, 3, 3 et 2, tous « FAIT »).
- **Les quatre résultats sont égaux à l'octet aux pièces v3 versées** (`cmp` muet ×4), aux empreintes `ca1a58d1…`, `a057cf25…`, `8aff91f1…` et `ce21e8ed…`. Cela prouve trois choses :
  - la passe 1 est mon jeu tel quel ;
  - les passes 2 et 3 sont exactement les jeux déclarés ;
  - **rien d'autre n'a changé** entre la v2 et la v3.
- L'écart du rédacteur (empreintes comparées au lieu de `cmp`) est déclaré et sans effet.

## 2. La passe 2 : les décisions de la mère de 07:24Z (R-4410)

| décision | portée | jugement |
|---|---|---|
| « le relais de l'espèce retirée » | ordre § 4 : « le relais de l'espèce retirée est absent » | **fidèle** |
| clés désignées | déjà fait par mon jeu (devis § 6, rapport § 6) ; aucune autre forme ne reste | **fidèle** |
| D-M7 « trois points » | ordre § 5, préenregistrement point 3, rapport D-M7 : trois points (dissonance ; budget d'audit ; aiguillage), les deux seuils renvoyés au tirage | **fidèle à la lettre de 07:24Z, mais dépassé** par la précision de 07:32Z (R-4412) : **à corriger** (§ 3) |
| D-M9 et la chute de la clause de D-M4 | ordre § 7, changement 1 (mon texte, plus « la mère retient cette affectation ») ; préenregistrement, point 5 ; rapport D-M9 | **fidèle** |
| plafond des traducteurs au complément, 8 000 jetons provisoires | ordre § 4 ; devis § 4 (table : « valeur provisoire » ; alinéa : le calcul se refait si le plafond monte, et le plafond d'arrêt de 20,48 tient la dépense) ; préenregistrement, point 5 ; rapport D-M9 | **fidèle**. Le programme garde 8 000, et c'est dit |
| test du moniteur de dissonance accordé, chaque dépense avec son devis et sa ligne, monde à K actions sur devis à part | ordre § 7, changement 3 ; devis § 7, point 5 ; préenregistrement, point 7 | **fidèle**. Le test est décrit (« la sonde ordonne-t-elle deux actions sur un même début, sur MATH500 ») d'après le test n° 1 et le « monde B » de la note (l. 46, 89, 142) : la paraphrase est juste |

Un ajout du rédacteur, dans l'ordre § 7 : « tant que le monde à K actions n'existe pas, une fiche du moniteur de dissonance n'est jouable que sur le monde à trois populations ; si sa règle exige les K actions, elle sort « non exécutée » ». C'est une conséquence directe, cohérente avec la classe « non exécutée », et dite. **Acceptable.**

## 3. Les deux ajouts du rédacteur

**(a) Noms de fournisseurs retirés du devis** (« deuxième relais », « troisième relais »). **Juste.** Les relais restent désignés comme au registre, rien d'utile n'est perdu, et la règle de versement (compte nul) l'exige.

**(b) Sa lecture de D-M7.** À 07:24Z, la lettre de la mère (« trois points ») rendait sa lecture défendable, et il l'a dite « lecture du rédacteur, à confirmer ». **Mais elle n'est plus fidèle** : à 07:32Z, la mère garde nommées toutes les propositions de GO-2026-11-21-15 (R-4412 ; ton message). Sa parenthèse de 07:16Z n'était qu'un exemple. La liste nommée est désormais :

1. le moniteur de dissonance et le budget d'audit réparti selon la valeur ;
2. le seuil certifié au plus 1 %, avec la bande de seuils ;
3. le seuil unique sur score normalisé ;
4. l'aiguillage en lecture rétrospective.

Toutes passent avant le tirage, qui ordonne le reste. **Correction K3-O1, K3-P4, K3-R1.** L'inconvénient de l'option (a) de D-M7 au rapport (« trois ou quatre places sur onze ») devient « jusqu'à cinq » : **K3-R2**.

**Pour la mère** : avec cinq propositions nommées, l'option (c) du devis (cinq candidates) ne laisserait plus aucune place au tirage. Le devis le dit déjà en substance (« il ne reste presque que les propositions nommées ») ; ce n'est pas à corriger.

## 4. La passe 3 : la règle « v2 se lit v3 »

**Acceptable dans le corps des textes.** Elle est écrite sur la ligne de version de chaque pièce, et elle a un précédent (devis v6 de la course « nouvelles attaques »). Elle évite des dizaines de remplacements sur des ancres non uniques. Les numéros de section n'ont pas changé, et le calcul reste explicitement le programme v2.

**Une limite :** la règle porte sur des mots (« ordre de course v2 », « devis v2 »), non sur des **noms de fichiers**. Or le tableau « Documents qui font foi » du préenregistrement cite `ordre-course-seuil-et-moniteurs-v2.md` et `devis-course-seuil-et-moniteurs-v2.md`, « à la table d'empreintes v2 ». Ce tableau est ce qui lie le texte scellé à ses pièces (règles R1 et R6) : il doit nommer les fichiers v3. **K3-P1, K3-P2.**

J'ajoute au même tableau deux lignes, **K3-P3** :
- la contre-lecture de la v2, `662f7510…`, dont le chemin versé est vérifié ;
- les décisions de la mère qui fixent la lecture : R-4399, R-4410, R-4412, au commit `c9d7faf2…`, avec l'empreinte du registre.

Le rapport v3, dernière ligne, renvoie encore à la table v2 : **K3-R3**. La ligne « empreintes à la table v2 » du devis (l. 7) parle du programme v2, qui y est : elle est juste.

Le rapport des passes garde, à son § 3, la trace de la lecture de 07:24Z : c'est un compte rendu de ce qui a été fait, à ne pas réécrire.

## 5. Noms de modèles et de fournisseurs : **0**

J'ai cherché moi-même, sans distinction de casse, vingt-deux noms de modèles et de fournisseurs, dont ceux du collisionneur, ceux du papier et les trois fournisseurs des relais. Les fichiers examinés : les quatre pièces v3, le rapport des passes, la table v3, le programme v2 et sa sortie. **Aucune occurrence.** Le compte est encore nul sur mes trois sorties d'essai après le jeu. Les différentiels et les jeux des passes en portent, comme le rédacteur le dit : ils ne sont pas versés, et c'est ce qui convient.

## 6. Le devis

- **Inchangé.** La reconstruction le prouve (§ 1), et la table du § 0 rend toujours 20,77 / 97,41 / 114,48.
- **75,77 et 114,07 sont dits écrits à la main** : sur la ligne de version (« écrits à la main, dits comme tels au § 3 ») et au § 3, qui donne à côté la valeur du programme (75,76 ; 114,06) et la raison de l'arrondi vers le haut. **Conforme.**

## 7. Corrections (outil `scripts/remplacer_texte_exact_v1.py`)

Chaque ancre est comptée **1** par `grep -c -F -e` dans la pièce v3 visée.

| fichier | empreinte | pièce | remplacements |
|---|---|---|---|
| `corrections-v3-ordre-v1.json` | `32c24407f3b4dc8613957a9691bb088146edecd2a6bb96b235c0c6101a96ebaa` | ordre v3 | 1 : K3-O1, D-M7 à quatre entrées, la lecture du rédacteur retirée |
| `corrections-v3-preenregistrement-v1.json` | `792d46ef0e6f60ba55109e69e4f3f6f281f936f9476addb1d666e9b02d12135b` | préenregistrement court v3 | 4 : K3-P1 et K3-P2, fichiers v3 et table v3 ; K3-P3, contre-lecture de la v2 et décisions R-4399, R-4410, R-4412 ; K3-P4, D-M7 |
| `corrections-v3-rapport-v1.json` | `28aa33303e62fa9140461df3802751d9689eab798046540a4d90a181aef7743b` | rapport v3 | 3 : K3-R1, D-M7 tranchée ; K3-R2, « jusqu'à cinq places » ; K3-R3, table v3 |

**Essai sur copie** (`essai-v3/`, copies d'empreintes égales à la table v3) : trois « FAIT ».
- ordre : `5856b2527a73b24b3c8dcea5bb056f3eab54a9bdb8932d510476f024ce9c01b8` ;
- préenregistrement : `fdcc968a7b8a984faa98e74094a67d09b67fee349e90d02bf10002d2c03882ca` ;
- rapport : `342b72823f3a882dbbb6f53c740473e9ffdc141147b3fe0187d2353ad9c27847`.

Le devis n'est pas touché.

Ces remplacements font une version neuve (règle R12). Sa ligne de version, comme à la passe 3, est de la tenue du rédacteur. Le contrôle de son différentiel peut se borner à ces huit remplacements et à cette ligne.

— contre-lecteur de la conception seuil et moniteurs, modèle O
