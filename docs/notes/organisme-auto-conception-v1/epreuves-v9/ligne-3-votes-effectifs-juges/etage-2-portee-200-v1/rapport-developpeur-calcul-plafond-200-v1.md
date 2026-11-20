# Rapport du développeur — calcul versionné des conditions du plafond de l'étage 2 à 200 témoins (ligne 3, nœud 3 de l'additif 3) — v1

Pièce d'instrument (classe B), écrite le 2026-11-20 (`date -u` : 12:22Z à la fin des essais), sur le mandat `mandat-developpeur-calcul-plafond-200-v1.md` (`10f22d1c447cb3c99c4701e3e76b0b5820ce4e002cbd1f1c25ccf24058e1dd24`, égale à son compagnon, contrôlée par `sha256sum -c` avant tout autre geste). Développeur neuf, modèle O : je n'ai écrit ni le texte de la ligne 3, ni ses additifs, ni le devis, ni ses calculs. Processeur seul ; aucun appel de modèle, aucune dépense, aucune clé lue ; aucune écriture dans le dépôt.

## Verdict du calcul

À 200 témoins et au plafond de 88,36 USD, **le pire cas du devis (88,3617 USD) est coupé par le compteur au bloc B, sur le témoin 198 de l'ordre du bloc B (moitié « étalonnage »)** : 996 envois partent sur 1 004 ; la plomberie et le bloc A sont complets ; le bloc B est complet sur 197 témoins, **dont les 100 de la moitié « lecture »**. Le seuil de 40 est tenu : **le compteur ne donne pas le rang 1** ; le pire cas n'est plus « non concluant par manque de témoins » comme à 100. Le cas haut (44,7783 USD) et le cas attendu (32,9044 USD) passent entiers. Les chiffres du contre-lecteur sont tous retrouvés ; une seule différence de lecture, au multiple du bloc A (§ 4).

## 1. Pièces lues (empreintes recalculées égales à leur compagnon)

| pièce | sha256 | lecture |
|---|---|---|
| devis v7 (`origin/main`, `git show` redirigé) | `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270` | en entier |
| texte de la ligne 3 v7 (`origin/main`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | l. 180-309 et 330-391 (seuils, plan d'analyse, étage 2, graines et gestes, critères de l'étage 2, liste d'arrêt, section « Plafond ») ; l. 15 et l. 80 par recherche sur ce seul fichier |
| additif 3 v3 (`origin/main`) | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` | en entier |
| calcul du devis v3 (L3) | `9364867e7a21d28e2b30f3f73d3f0a6604cecfa3eee5efb46eb2331ba3dcbaf8` | en entier |
| sa sortie (L3) | `1a13fe2756a5587398e122c17700fab6472350d6c38975d58c1c3cf337ad6cf6` | en entier |
| contre-lecture de l'additif 3 (L3) | `f264cf9e8c8fca02a308e6831963ab55672f77017e522c653fa2ac2c08b57082` | en entier |
| inventaire de l'étage 2 (L3) | `a2039f7d1e06ea3a045cfe1c1f9142c8ae4bf8e4a49e92a65c454dd00d49cfbe` | en entier |
| entrées du calcul v3 : manifeste de fin de la course v9 ; épreuve réelle des témoins v9 | `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7` ; `e7837f4c40bca9aaed7ae0d3e8bdb51f9f36284ffb21c677575368699a61ca84` | lus par le programme seulement ; du manifeste, une recherche bornée aux champs de coût des juges |

## 2. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-calcul-plafond-200/`, chacun avec son compagnon `.sha256`.

| fichier | sha256 |
|---|---|
| `calcul_conditions_plafond_200_ligne_3_v1.py` | `4814f314af8706e032e6cbe1ac273893377c8dfa1cb5c44ef6478c08f814d0c3` |
| `calcul-conditions-plafond-200-ligne-3-v1.json` | `20ade9a3feae5b6c5dea3be61808dc71a656d81291857a13facd950baca44fc0` |
| `essais_calcul_conditions_plafond_200_v1.py` | `2ebe71fdb6fc323f4b067cd4578e93701ec3f943133a0b1aeb2b8b27dd9c19fd` |
| ce rapport | dans son compagnon |

- **Joué deux fois**, `env -C /home/user/controle-ia-travail python3 -I -B CHEMIN > SORTIE` : la sortie et le rejeu (`rejeu-calcul-conditions-plafond-200-ligne-3-v1.json`, gardé) ont la même empreinte, `20ade9a3…` : égales à l'octet. Le programme ne prend aucun argument et écrit sur la sortie standard, pour que la commande du mandat soit jouée à la lettre ; la redirection `>` est le seul ajout.
- **Essais** : `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_calcul_conditions_plafond_200_v1.py` : **19 essais passés** (2,47 s). Aucun dossier de cache écrit (contrôle par `stat` sur le seul chemin `__pycache__`).

**Ce que fait le calcul.** Il part du calcul v3 (mêmes entrées par empreinte, mêmes tarifs par appel, mêmes trois cas, même plan par témoin), tout en fractions exactes ; plafond et réserve en centimes entiers (8 836 et 60) ; aucun flottant dans une comparaison de seuil ni dans la sortie (garde). Il rend deux lectures de la règle du compteur :
- **« formule du devis »**, la forme fermée du v3 : un groupe d'appels est complet si le cumul compté *après* son dernier envoi tient sous 87,76 USD ; prudente ; indépendante de l'ordre des envois dans le bloc A ;
- **« envoi par envoi »**, la règle elle-même (texte l. 382) : un envoi part si le cumul compté *avant* lui plus 0,60 USD ne dépasse pas 88,36 USD ; c'est elle qui dit où le compteur coupe.

Hypothèses de modèle, dites (non tirées de la lettre) : chaque appel coûte le tarif moyen du juge à la course v9 multiplié par le facteur du cas ; dans le bloc A, par témoin, juge Opus puis juge Argon ; un envoi refusé est compté 0,60 USD puis rejoué une fois avec succès, les refus tombant au début du plan ; « tous refusés » : chaque envoi et son rejeu refusés.

## 3. Les chiffres à 200 témoins et 88,36 USD

Plan : plomberie 4, bloc A 400, bloc B 600 ; **1 004 envois**. Tarif par appel : juge Opus 0,073013 USD, juge Argon 0,025626 USD (cas haut). Facteurs : estimation 0,7348 ; haut 1 ; pire 1,9733 (exact : 3431597/1739000).

| cas | total du plan | coupure | envois partis | bloc B complets (lecture) | issue |
|---|---|---|---|---|---|
| estimation (cas attendu) | 32,9044 USD | aucune | 1 004 | 200 (100) | plan entier |
| haut | 44,7783 USD | aucune | 1 004 | 200 (100) | plan entier |
| pire | **88,3617 USD** | bloc B, témoin 198 | **996** | **197 (100)** | coupure sans manque de témoins |

### Condition (i) — arrêt dur par compteur

- Cumul utile : **87,76 USD** (8 776 centimes). Borne de la dépense : 88,36 USD si aucun appel ne coûte plus que 0,60 USD ; sinon 87,76 USD plus le coût du dernier envoi, qui arrête le programme.
- Chiffres pour les essais des gardes du code de l'étage 2 : cas sain (cas haut) **1 004 envois partent**, cumul compté égal au total du plan (44,7783 USD) ; artefact « coût gonflé » au pire cas : **996 envois partent** ; coût relevé de 0,61 USD : arrêt après le premier envoi.
- Multiples du tarif des cartes qui laissent un groupe complet :

| groupe complet | formule du devis | envoi par envoi |
|---|---|---|
| plomberie et bloc A | **4,4045** | 4,4102 |
| en plus, bloc B sur 40 témoins de la moitié « lecture » (seuil) | **3,5251** | 3,5287 |
| en plus, bloc B sur les 100 témoins de la moitié « lecture » | **2,7127** | 2,7148 |
| tout, les 200 témoins | **1,9599** | 1,9610 |

  Chaque frontière « envoi par envoi » est vérifiée par la simulation, de part et d'autre (au facteur exact, le groupe est complet ; un millionième de millionième au-dessus, il ne l'est plus). Le pire cas (1,9733) est au-dessus des deux lectures de « tout » : il est coupé dans les deux.
- Au cas haut, sous 88,36 USD, la banque pourrait monter à 392 témoins (394 sans la réserve). Marge nominale sur le cas haut : 1,9733 ; effective : 1,9599.
- Au seuil d'arrêt de la plomberie (coût par appel à trois fois le tarif des cartes, texte l. 378) : coupure au bloc B, témoin 76 de la moitié « lecture » ; 630 envois ; 75 témoins complets dans la moitié « lecture », seuil tenu.

### Condition (ii) — l'issue du pire cas, écrite d'avance

Phrase rendue par le programme (clé `condition_ii_issue_du_pire_cas_ecrite_d_avance`) :

> Au pire cas du devis (tarif des cartes × 1,9733), le plan de 1004 envois coûterait 88,3617 USD, au-dessus du plafond de 88,36 USD. Le compteur coupe au bloc B : le dernier envoi parti est le rendu 2 du juge Opus sur le témoin 198 de l'ordre du bloc B (moitié « étalonnage », rang 98), parti à un cumul compté de 87,6260 USD ; le rendu 2 du juge Argon sur le témoin 198 ne part pas : cumul compté 87,7701 USD plus la réserve de 0,60 USD dépasse 88,36 USD. 996 envois partent sur 1004 ; plomberie et bloc A complets ; bloc B complet sur 197 témoins, dont les 100 de la moitié « lecture ». Dépense comptée à l'arrêt : 87,7701 USD ; reste sous le plafond : 0,5899 USD, moins que la réserve.

- **Ce qui est encore lu** : plomberie complète ; bloc A complet sur 200 témoins et deux juges (ρ entre juges, votes effectifs, table par juge ; bras U, C, F, P, S-Opus, S-Argon sur la moitié « lecture », 100 témoins) ; bloc B complet sur 197 témoins (100 de lecture, 97 d'étalonnage) : bras R-Argon et R-Opus-2 sur les 100 témoins de la moitié « lecture », ρ, ρ′ et ρ′ − ρ pour cette comparaison sur les 197 témoins complets, même ensemble pour les deux juges (texte l. 293, l. 388) ; seuil de 40 tenu (100).
- **Ce qui manque** : 8 rendus, tous de la moitié « étalonnage » du bloc B : les rendus 2 et 3 du juge Argon sur le témoin 198 ; les trois rendus de plus sur les témoins 199 et 200. Le rendu 2 du juge Opus sur le témoin 198 est parti : déposé, hors de l'ensemble des témoins complets.
- **Verdict** : pas de rang 1 par le compteur ; la table de l'étage 2 se lit selon ses rangs. Le programme s'arrête quand même à la coupure : aucune suite sous la ligne ; ce qui est fait est déposé, scellé, rapporté (l. 382).
- **Avec des envois refusés, au pire cas** (envoi par envoi ; formule du devis égale sauf à 80) :

| envois refusés | 0 | 1 | 2 | 3 | 5 | 10 | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bloc B complets | 197 | 195 | 192 | 190 | 185 | 173 | 148 | 99 | 50 | 2 (formule : 1) | 0 |
| dont moitié « lecture » | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 99 | 50 | 2 | 0 |
| issue | sans manque | ← | ← | ← | ← | ← | ← | ← | ← | **manque** | **manque** (bloc A coupé : 140 complets) |

  Seuils, envoi par envoi : moitié « lecture » entière jusqu'à **39** refus ; au seuil de 40 témoins jusqu'à **64** ; plomberie et bloc A complets jusqu'à **80**. À partir de **65** envois refusés : « non concluant par manque de témoins », jamais lu comme un « non ».

### Condition (iii) — tout envoi refusé compté au pire

- Si tous les envois sont refusés : **147 envois partent**, **88,20 USD comptés** ; le dernier est le premier essai du juge Argon sur le témoin 35 de l'ordre du bloc A ; son rejeu ne part pas ; aucun rendu obtenu ; « manque ».
- Envois refusés que le plan supporte sans coupure : estimation **91**, haut **71**, pire **0** (déjà coupé) ; formule du devis et envoi par envoi égales.
- Seuils au cas haut : lecture entière jusqu'à 92 refus, au seuil de 40 jusqu'à 104, bloc A complet jusqu'à 113 ; au cas attendu : 106, 115, 121.

### Contrôle à 100 témoins et 25 USD

- **83 clés de la sortie v3 recalculées, toutes égales** (compteur d'arrêt, plafond, scénarios à 100 et 200, facteurs, coût du bloc B, coût de la paire de juges). Le programme s'arrête si une clé diffère (garde).
- **Les chiffres du devis v7 sont retrouvés à l'octet** dans son texte scellé (essai `test_100_chiffres_du_devis_v7_a_l_octet`, dix-sept fragments) : 16,52 ; 22,49 ; 44,38 ; 41 envois (24,60 USD) ; 13, 3, 0 refus ; 91 et 67 ; 2,4 fois (2,43) ; 1,62 ; 1,50 ; 1,085 ; 24,27 USD ; **18 témoins (16, 13, 11)** ; « non concluant par manque de témoins » ; 108 (110) ; 29,66 USD ; la ligne « 200 témoins : 32,90 ; 44,78 ; 88,36 USD ».
- Envoi par envoi, le pire cas à 100 coupe au témoin 19 de la moitié « lecture » (rendu du juge Opus parti, ceux du juge Argon non) : 259 envois, 18 témoins complets, « manque » ; avec 1, 2, 3 refus : 16, 13, 11. Les deux lectures donnent la même issue que l. 384.
- **Un arrondi intermédiaire du v3**, trouvé par ce contrôle : le v3 lit les coûts de la plomberie, du bloc A et les totaux dans sa propre sortie arrondie à quatre décimales avant ses formules du plafond. Le contrôle le reproduit. Tout exact, une seule clé diffère au dernier chiffre : « plomberie, bloc A et B sur 40 témoins au pire » vaut 29,6625 et non 29,6626. Le texte du devis (29,66 USD) n'en est pas touché. Les chiffres à 200 de ce calcul sont tout exacts.

## 4. Ce qui diffère du calcul approché du contre-lecteur, et pourquoi

Son tableau (contre-lecture, § 6, « Ce qui manque, et que j'ai calculé ») est retrouvé, chiffre par chiffre : cumul utile 87,76 ; 147 envois (88,20 USD) ; 71 refus au cas haut (3 à 100) ; 996 envois sur 1 004 ; 197 témoins sur 200 ; moitié « lecture » complète ; multiples 4,41 ; 3,53 ; 2,71 ; 1,96.

- **Ses multiples sont la lecture « envoi par envoi »**, avec le juge Argon pour dernier envoi du bloc A. La preuve : ses multiples à 100 (2,431 ; 1,626 ; 1,502 ; 1,086) sont exactement les miens dans cette lecture (2,4314 ; 1,6260 ; 1,5016 ; 1,0863). Le devis v7 imprime la lecture « formule du devis » (2,43 ; 1,62 ; 1,50 ; 1,085). Les deux lectures ne diffèrent que d'un envoi, le dernier du groupe. À 200, elles ne se séparent à deux décimales qu'au bloc A : **4,40** (formule, indépendante de l'ordre) contre 4,41 (envoi par envoi, ordre supposé).
- **Ce qu'il ne donnait pas, rendu ici** : le lieu exact de la coupure (témoin 198, rendu du juge Opus parti, rendus du juge Argon non), le cumul compté à l'arrêt (87,7701 USD), les 8 rendus manquants, la table selon les refus et ses seuils (39, 64, 80), le lieu du dernier envoi si tout est refusé, les refus supportés au cas attendu (91), le cas au seuil de la plomberie. Sa phrase « il n'ôte les répétitions qu'aux trois derniers témoins de la moitié d'étalonnage » est juste au compte des témoins complets ; plus précisément, le témoin 198 garde le rendu de plus du juge Opus.
- **Aucun désaccord de chiffre.** Je n'ai pas lu son programme, qui n'est pas versé (son § 11) : la comparaison porte sur les chiffres de son tableau seulement.

## 5. Remarques : ce que la lettre ne tranche pas

1. **L'ordre des envois dans le bloc A.** La lettre tire l'ordre des témoins à graine. Elle ne dit pas si le bloc A va par témoin ou juge par juge, ni quel juge passe en premier. Cela ne joue que sur la frontière « envoi par envoi » du bloc A. La « formule du devis » (4,4045) n'en dépend pas. Si le compteur coupait dans le bloc A, la moitié du témoin coupé ne serait pas connue d'avance.
2. **Le rendu isolé du témoin 198.** L. 293 lit ρ, ρ′ et ρ′ − ρ sur les seuls témoins complets. La lettre ne dit pas si le rendu de plus du juge Opus sur un témoin incomplet est rapporté à part. Il est déposé (« récupérer ce qui est récupérable »), hors de l'ensemble des témoins complets.
3. **88,3617 > 88,36.** La ligne GO-2026-11-20-26 est donnée « au pire du devis », mais le pire du devis la dépasse de 0,0017 USD. Surtout, la réserve de 0,60 USD fait couper le compteur 8 envois avant la fin. Le pire cas ne passerait entier qu'avec un plafond de 88,92 USD (frontière éprouvée en centimes : 88,92 passe, 88,91 coupe). La lettre ne dit pas si la ligne devait couvrir le pire cas entier ; sous la lettre, la coupure ne touche que des répétitions de la moitié « étalonnage », sans effet sur le rang (inventaire, § 4, point 3, et § 5, remarque 4).
4. **Un modèle à coût moyen.** Le lieu de la coupure suppose que chaque appel coûte le tarif moyen du juge. Les coûts réels varient d'un appel à l'autre : l'issue écrite est celle de ce modèle, une prévision, pas une promesse. Seule la règle du compteur est une garantie.
5. **Le modèle des refus.** Un refus suivi d'un rejeu réussi coûte 0,60 USD de plus. Un double échec rend un rendu « absent » (1,20 USD comptés). Le témoin est alors incomplet sans coupure, et l'absent compte dans la règle des 10 % d'absents. Ce cas n'est pas modélisé : les seuils de refus valent pour la forme modélisée seulement.
6. **Le rang 1 « par manque de témoins » devient rare à 200.** Sous le seuil d'arrêt de la plomberie (trois fois le tarif), le tarif seul ne fait pas passer la moitié « lecture » sous 40 : elle tient jusqu'à 3,53 fois. Il faut des refus en nombre (65 au pire cas, 105 au cas haut) ou une coupure dans le bloc A. C'est conforme à la décision de garder le seuil à 40 (GO-2026-11-20-36 ; inventaire, remarque 8).
7. **« Dépasse » lu au sens strict.** Un envoi qui porte exactement le cumul compté plus la réserve à 88,36 USD part (lecture du v3 : `k × 60 + 60 ≤ plafond`). La lettre (« dépasse ») le permet. Les frontières sont éprouvées des deux côtés.
8. **Le facteur du pire** reste celui du devis : le rapport réel sur devis du juge Opus à la course v9, appliqué aux deux juges (devis, § 4 ; réserve 2). Rien ne dit qu'il borne.

## 6. Ce que j'ai fait, et mes écarts

- Commandes : `sha256sum -c` du mandat ; `git show origin/main:…` redirigé vers mon bloc-notes (devis v7, texte v7, additif 3 v3 et leurs compagnons) ; `sha256sum -c` sur chaque compagnon (pour les deux pièces en sous-dossier, le premier essai depuis le dossier L3 a échoué parce que leurs compagnons portent un nom nu ; rejoué depuis leur propre dossier, égal) ; `sha256sum` sur des chemins nommés ; `python3 --version` et la version du Python de l'environnement virtuel ; le calcul joué deux fois ; les essais ; `stat` sur un seul chemin ; `date -u`.
- **Écarts déclarés** : (1) trois recherches, chacune sur un seul fichier nommé, jamais sur un dossier : par l'outil de recherche du poste, dans le manifeste de la course v9, bornée aux champs de coût et de devis des juges, pour connaître les décimaux exacts lus par le programme ; par `grep -n`, dans mes copies, l'intitulé « Plafond : arrêt dur par compteur » du texte v7 et les titres de l'additif 3, pour les situer ; (2) un programme de diagnostic, `diag_ecart_v3_v1.py`, écrit dans mon bloc-notes et joué une fois (`python3 -I -B`), qui a trouvé l'arrondi intermédiaire du v3 ; non rendu ; il importe le calcul par son chemin ; (3) mes copies de travail des trois textes scellés sont dans le même bloc-notes, pas dans un sous-dossier ; (4) le programme écrit sur la sortie standard et ne prend aucun argument, à la différence du v3, qui prend un chemin de sortie.
- Aucune mesure de l'étage 1 ouverte ; aucun verdict ouvert (la portée en « issue B » n'est connue que par l'inventaire et n'entre dans aucun calcul) ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/` ; aucune écriture dans le dépôt, aucun commit ; aucun heredoc, aucun code en ligne passé à un interpréteur. Aucun refus de permission, de classifieur ou de garde.

Développeur, modèle O.
