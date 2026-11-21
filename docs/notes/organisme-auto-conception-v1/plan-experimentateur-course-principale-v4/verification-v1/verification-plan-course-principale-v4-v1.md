# Vérification du plan v4 — l'expérimentateur et l'étage des tests de mort sur la course principale d'auto-conception — v1

- Contre-lecteur des plans v2 et v3 (modèle O). Je vérifie ici que la v4 porte les quatre corrections de mon contrôle de la v3 (`864159fa…`), qu'elle reprend juste les deux errata de la note, et que les écarts qu'elle déclare sont fondés. Je n'ai écrit ni le plan, ni la note, ni ses errata.
- Date (UTC) : 2026-11-21 ; `date -u` : 08:28:09Z, après les lectures, avant l'écriture.
- Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt, aucun commit. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Le seul programme joué est celui des calculs du plan, sans entrée, par `python3 -B`. Aucun refus rencontré.
- Deux relevés de la mère, reçus en cours de vérification, sont pris en compte : les dix champs de la fiche de la course v9, et la lecture de « GO-15 et GO-28 ».

## Pièces

Toutes égales à leur compagnon et à l'empreinte annoncée.

| pièce | empreinte |
|---|---|
| plan v4 | `ebb4cb47707e30929b535c8f65249f3f55abe831386e1fcaf5cf69cffcecc14f` |
| rapport v4 | `29e18ef8d436c9be67a3003f6b3452ecc4bb0b09472b1a31a2c45842f93b3512` |
| différentiel v3 → v4 | `d6440df2bed22f82b593d39905184610cc6733a241ac5204a77203eae01fd5dd` |
| calculs, script | `6560afffad364ef8b13e73bd41a1f284e1b373c494fec7e5d27fc124b290b962` |
| calculs, sortie | `1f26453325d1733375d0a51d3bb128662a80cc30f54610c750ba3ee057e7a315` |
| table v4 | `3c1c7578d08225c05067e0da9335c4ebc1dd3e85063e7dc77d08fc203beda0ee` |

Sur `origin/main`, après `git fetch origin main` :
- erratum 1 de la note : `0198f5f8dc6d12e34d0beaa6493e761211ef1d613c9306dc651b432afb8f44d7` ;
- erratum 2 de la note : `12c6034978e7475e007147df632327537b6a4a32c458ceef5e7d51b4aa3127de`.

Sur le disque :
- compte des cartes, rapport `9e410b09…` et sortie `9515bae3…` ;
- configuration v5 de la course, `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8`, clé `champs_fiche`.

**Rejeu des calculs** : `rejeu-calculs-plan-v4.txt` (dans ce dossier), sortie égale à l'octet à celle du planificateur (`1f264533…`).

## Verdict : **Conforme**, sous deux retouches de lettre

Les quatre corrections sont portées. Les chiffres de l'erratum 1 sont repris juste, et je les ai rejoués. L'alignement sur l'erratum 2 tient, et les écarts déclarés sont fondés. Aucun nom de modèle ni de fournisseur n'apparaît. Il reste deux retouches de lettre, à faire par le rédacteur, sans changement de fond. La première (D8 (a), avec les dix noms) est à faire avant que D8 aille à Lazar.

## 1. Les quatre corrections

1. **D5 (a) récrite** (§ 7.2, § 3.1, § 0, point 4) : portée.
   - Le socle est la couche sous le sommet : les maillons existants, l'enveloppe du palier 0b, et C2 et C3 hors de la v69.
   - AC-1 a son sommet et son lanceur ; la v69 garde les siens tels que scellés.
   - Le sommet unique est l'option (c), déclarée nœud de Lazar, sans défaut, non tranchée.
   - Le défaut de (a) est compté à partir de la v4, et il est dit que celui de la v3 ne doit pas courir.
   - Le passage de la confiance de 0,6 à 0,7 est déclaré (écart 8) : acceptable.
2. **E1 scindé, C3 sorti de la v69** (§ 4.2) : portés. Il y a désormais E1-v69 (palier 1 seul, hors de cette course) et E1-AC (fichier neuf d'AC-1, 1 à 2 heures, hypothèse). C3 est en fichiers neufs hors de la v69.
3. **D8 (a)** : « étend le modèle de GO-2026-11-20-15 et de GO-2026-11-20-28 sur deux points », avec les deux lignes d'accord citées à la lettre. Portée. Les noms des champs restaient à relever : voir le point 4.1.
4. **D8 (d) chiffrée** : 92 au plus, puis 90 ou 81. Vérifié sur `registres/go.md`.
   - GO-2026-11-19-55 nomme 5 cartes porteuses.
   - GO-2026-11-19-56 en nomme 6, dont 2 « et ses fusionnées ».
   - Aucune des onze n'est l'une des deux exclues (`fafa0062508c9`, `f0497de657ec8`, proposition `a2cd45ad…`, § 2).
   - 92 − 2 = 90 (porteuses des lignes 1 et 3) ; 92 − 11 = 81.
   - Les trois réserves sont dites : fusionnées non dénombrées, présence des onze parmi les 94 supposée, et GO-2026-11-19-57 et -59 non comptées.
5. **0,081 porté** (§ 6.3, première ligne) : oui. Les montants 0,57 et 13,35 en découlent.

## 2. Les ordres de grandeur de l'erratum 1, rejoués

Le rejeu du programme rend une sortie identique à l'octet. Contrôles à la main :
- **Par greffon** : 0,081 + 0,061 = 0,142, et 4 + 0,10 = 4,10. Facteur 4,10 / 0,142 = 28,9, soit environ 29. Hausse due au lecteur : 0,061 / 0,081 = 75 %.
- **Ligne 1** : 4 × 0,142 = 0,57 ; 4 × 4,10 = 16,40 ; 12 × 0,142 = 1,70 ; 12 × 4,10 = 49,20. Machine : 1,22 h arrondies à 2 ; 3,80 à 4 ; 12 h. Montants 0,15 / 0,56 / 2,60, 0,29 / 1,12 / 5,20 et 0,88 / 3,36 / 15,60. Plafond 5 USD sur 12 h, soit 0,4167 USD de l'heure.
- **Ligne 2** : 94 × 0,142 = 13,35 ; 94 × 4,10 = 385,40 ; à 92 cartes, 13,06 et 377,20. Machine : 6,09 h arrondies à 7 ; 24,10 à 25 ; 48 h. Plafond 15 USD sur 48 h, soit 0,3125 USD de l'heure.
- **§ 6.4, barreau 2 à cinq espèces**, dix générations, 94 tentatives par génération :
  - propositions : 586,40 ;
  - étage : 56,40 / 133,48 / 564 / 846 ;
  - carte : 642,80 / 719,88 / 1 150,40 / 1 432,40.
- **§ 6.4, à deux espèces**, 38 tentatives : propositions 89,20 ; carte 112 / 143,16 / 317,20 / 431,20.
- **Juges en plus** : 13,86 × 10 = 139 et 5,54 × 10 = 55.

Les fourchettes « 640 à 1 430 » et « 110 à 430 » sont justes. L'écart « 642 contre 643 » est bien dit : l'erratum tronque 642,80. L'erratum écrit aussi « 134 » pour l'étage à 0,142 (13,35 × 10, arrondi avant le produit), quand le plan écrit 133 (133,48). Le plan est le plus exact ; aucun effet.

**Le non mesuré est dit** : le lecteur est une borne haute, relevée sur une seule course et un seul modèle. Le greffon est non mesuré. Les traducteurs ne sont pas chiffrés. Le barreau 2 est fait de produits de bornes et d'un devis. La durée du rejeu du banc joueur n'est mesurée nulle part : les heures de machine sont dites planchers, et les deux plafonds de machine « non établis » (§ 6.2). C'est la bonne lecture de l'erratum 1, § 1 : la première mesure se fait au banc d'étalonnage, avant tout devis de machine.

## 3. L'alignement sur l'erratum 2

1. **C3 porte le rejeu et le banc joueur ; C2 porte le banc noteur, le contre-calcul, la porte des lots, le registre et le mécanisme des témoins** (§ 3.1, § 4.2). L'erratum 2 range ces pièces dans le socle sans les répartir entre lots (§ 1). La répartition du plan suit la note : son C2 de départ était « mesure hors machine, porte des lots, registre », et l'erratum 1, § 1, phrase 2, met le contre-calcul dans la mesure hors machine. Elle suit aussi l'erratum 2, § 2, point 5, qui met le rejeu dans C3. Conforme.
2. **Le socle passe avant E3** (§ 4.2, « Ordre ») ; E3 dépend de C2 et de C3, puisque l'étalonnage joue sur le banc du socle. Conforme.
3. **Les écarts du § 3.3** (le plan en compte cinq, dont deux « sans écart ») :
   - (1) Nœud du sommet unique déclaré, contre « aucun nœud neuf » : **juste**. L'erratum 2, § 1, dit lui-même que la variante « serait un nœud de Lazar ». Le plan ne fait que la nommer à D5 (c), sans défaut.
   - (2) Heures non redistribuées : **juste**. L'erratum 2, § 2, point 5, ne touche que la ligne de C3 (« socle : 1 à 2 »). Garder les totaux et dire C2 et C3 sans doute bas, E3 sans doute haut, est honnête.
   - (3) Table d'admission, mécanisme commun et valeurs propres à chaque emploi : **lecture fondée**, dite comme lecture du planificateur, à confirmer par l'auteur. Elle concilie le § 1 de l'erratum 2 (« la table d'admission » parmi les témoins du socle) et « la banque de mondes et le contenu de ses témoins » propres à chaque emploi.
   - (4) et (5) : sans écart.

## 4. Les écarts que le planificateur déclare

### 4.1 Les champs de D8 (a)

Le relevé de la mère comble le trou. J'ai vérifié la configuration v5 (`3f662ee8…`), clé `champs_fiche` : titre, axe, module_change, mecanisme, plus_proche_voisin, ce_qui_distingue, epreuve_monde_plante, cout, ce_qui_la_refuterait, limites. La configuration ne déclare **aucune liste de valeurs** pour ces champs. « Fermé » veut donc dire ici « liste fermée de noms », non « valeur prise dans une liste fermée ».

**Conséquences, à porter par le rédacteur (retouche de lettre 1, avant que D8 aille à Lazar)** :
- Écrire les dix noms dans D8 (a), avec leur source (`3f662ee8…`, `champs_fiche`).
- Le point (1) de l'extension (« valeurs par identifiant ») **tombe**, comme le plan l'annonçait lui-même (« si aucun des dix n'est fermé, le point (1) tombe »). Il tombe aussi au mot de la mère : « sur ces seuls noms, sans aucune valeur ».
- Dire ce qui reste de l'option (a), en deux branches, sans la trancher :
  - (a1) **les seuls noms et des comptes** : c'est déjà, à peu près, ce que GO-2026-11-20-28 a rendu (noms hors des dix champs, avec leurs comptes). Cette branche n'apporte presque rien de plus, et rien vers un compte de nature.
  - (a2) **avec la recherche de mots dans `module_change`** : le programme lit alors la valeur d'un champ libre, même s'il ne rend que la présence de mots par identifiant. C'est la seconde extension, qui demeure, et qui n'est pas « sans aucune valeur » au sens de la mère.
  - Le rédacteur doit dire que (a) se réduit à (a1) si l'on tient la règle « sans aucune valeur », et ne garde de substance qu'en (a2).

### 4.2 « GO-15 et GO-28 »

Je visais **GO-2026-11-20-15** (journal de l'aiguilleur, identifiants et comptes) et **GO-2026-11-20-28** (noms de clés hors des dix champs, comptes, sans valeur ni identifiant). Ma contre-lecture de la v2 les écrit en entier (« GO-2026-11-20-15 et -28 », point 5.3), et mon contrôle de la v3 aussi (point 4.3). « GO-15 et GO-28 » en était l'abrégé. La lecture du planificateur est la bonne. GO-2026-11-21-28 n'existe pas.

### 4.3 Lots et ordre changés au-delà de la lettre de mon contrôle

C'est **fondé** : l'alignement sur l'erratum 2 était demandé par la mère, et chaque changement est déclaré (écart 7, § 3.3) :
- banc joueur et banc noteur sortis de E3 ;
- C2 et C3 sans dépendance à E3 ;
- socle avant E3 ;
- C2 sur le chemin du premier dollar.

**Retouche de lettre 2 (forme).** Le chemin critique (§ 4.2) et le total du code (§ 5) comptent E1-AC à 4,75 + 1 à 2 heures : ce sont les heures de l'ancien E1 (sommet et enveloppe) plus le supplément de mon contrôle. Mais la table du § 4.2 donne à E1-AC « 1 à 2 heures » seulement, et ne chiffre pas E1-v69. Dire dans la table que E1-AC porte les 4,75 heures de l'ancien E1 plus 1 à 2 (soit 5,75 à 6,75), et que E1-v69 relève du devis d'heures du palier 1. Sinon, le chemin de 18,25 à 20,25 heures (20,25 à 23,25 avec C2) ne se retrouve pas depuis la table. Les additions sont justes : 17,25 + 1 = 18,25 ; 18,25 + 2 = 20,25 ; plus C2, 20,25 à 23,25.

### 4.4 Un écart de procédure, pour la mère

Écart 3 du rapport : le planificateur a fait une recherche à joker, interdite par l'en-tête de son mandat, pour retrouver le chemin de l'additif. Il le déclare ; elle n'a rendu qu'une ligne d'une table. Sans effet sur le fond, mais c'est à consigner.

## 5. Le compte des cartes comme seule borne

Oui. Le plan dit, au § 0, point 3, « une borne pour le devis, jamais le compte que la note demande ». Le § 6.2 garde 94 comme borne du devis, et 92 est montré à côté. Le § 6.3 donne les deux lignes. Le § 7.3 (d) dit ce que le compte est et ce qu'il n'est pas, et précise qu'« aucune carte ne passe sur sa foi ».

Le compte lui-même est tiré des deux pièces de `main`, à leurs empreintes : le rapport `9e410b09…` en donne la liste des commandes, et aucune ne nomme les archives.

## 6. Noms de modèles ou de fournisseurs

Aucun dans les six pièces. J'ai cherché les noms des modèles et des fournisseurs du programme, ainsi que des loueurs de machines. Les seules touches sont « greffable » et le chemin système du bloc-notes (`/tmp/claude-0/…`), qui ne nomment aucun modèle ni aucun fournisseur. Les rôles sont dits « modèle F », « premier relais », « deux lignées ».

## Retouches de lettre, à faire par le rédacteur

1. **§ 7.3, D8 (a)** : écrire les dix noms de `champs_fiche` (`3f662ee8…`) ; dire que la configuration ne déclare aucune liste de valeurs, donc que le point (1) tombe ; dire ce qui reste en deux branches, (a1) les seuls noms, à peu près ce que GO-2026-11-20-28 a déjà rendu, et (a2) la recherche de mots dans `module_change`, qui lit une valeur par programme ; mettre à jour l'écart 1 du rapport et le § 9, réserve 8. **Avant que D8 aille à Lazar.**
2. **§ 4.2, table** : E1-AC à 5,75 à 6,75 heures (ancien E1 plus le supplément), E1-v69 au devis d'heures du palier 1, pour que le chemin critique et le total se retrouvent depuis la table.

## Pour la mère

- D8 (a), lue avec ton relevé, ne garde de substance que par la recherche de mots dans `module_change` (a2), qui n'est pas « sans aucune valeur ». Sans elle, (a) se réduit à peu près à ce que GO-2026-11-20-28 a déjà rendu. C'est à dire tel quel à Lazar.
- Le défaut de D5 ne court que sur le texte de la v4.
- L'écart 3 du rapport (recherche à joker, déclarée, sans effet) est à consigner.

— contre-lecteur du plan de la course principale, modèle O
