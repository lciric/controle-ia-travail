# Contre-lecture (R2) du préenregistrement de réplication sur graine neuve de la course de convergence des règles de défense — brouillon 1 — rapport v1

**Verdict : scellable après corrections mineures (14 remarques « CL-nn » au § 3, dont 8 obligatoires) ; aucune ne change les hypothèses, les prédictions chiffrées, les seuils d'effet ni les tables de lecture.**

- Contre-lecteur : sous-agent neuf (Claude Sonnet 5.5). N'a écrit aucune pièce de la chaîne (course originale, code v2, arène v4, lecture, audit, état des lieux, spécification, brouillon).
- Date : 1er novembre 2026, ≈ 21:55 UTC. Aucun fichier existant modifié, aucun réseau, aucun commit. Seul fichier créé dans le dépôt : celui-ci.
- Objet lu : `brouillons/preuves-mentors-v1/convergence-replication-v1/preenregistrement-replication-convergence-v1-brouillon1.md`, 380 lignes, empreinte `f0fd07874c6bba5dfb71c845a693749015caaee2b554ae5772c93b2a82dd7c76`. Pièces lues avec lui : la spécification (`2a1ad6d356ab60d44aebbf8d92ee9ba932bd24f925ae4fb86538545e0706e0e5`), l'état des lieux (`445b31ad9ef283420fcec75b5e78359ebcf989ed0eb5fe30af67ecc25ebae1bc`), le préenregistrement original, sa lecture, son audit, le code v2 (racines, gardes, identité, tâche, analyse, `_boot`, `_travail`, `main` ; inventaire syntaxique complet du niveau module), le gel v2, l'arène v4 (parties employées), le gabarit, l'exemple P3 (titres de sections seulement), les bibliothèques `prereg`, `scellement`, `manifeste`, `gardes`, le manifeste de la course originale (lu sur la branche `origin/canal/session-depot-reprise-n67`, absent de l'arbre de travail), les entrées R-1075, R-1076, R-1079, R-147 de `registres/decisions.md`.
- « CL-nn » = remarque de contre-lecture numéro nn (usage du dépôt). « Obligatoire » = à appliquer avant le scellement ; « recommandée » = à appliquer sauf raison écrite.
- Le brouillon est, par construction, non scellable tant que ses champs « À REMPLIR » restent : mon verdict porte sur le texte. Une fois les corrections faites et les champs remplis mécaniquement, il est scellable. Comme CL-06 à CL-08 ajoutent des essais et une procédure que personne n'a encore relus, je recommande une courte contre-lecture 2 avant le scellement (CL-14).

## 1. En six lignes

1. **Le dessin est bon.** La réplication teste bien ce qu'elle dit tester (la dépendance à la graine), la règle D est correctement définie et reproductible, la statistique recodée depuis la spécification retombe au bit sur l'analyse scellée, les 16 empreintes citées sont exactes, la puissance annoncée tient (HRép1 ≈ 1,00 ; HRép0 ≈ 0,90).
2. **Un chiffre à corriger** : « ≈ 0,85 en tenant compte de l'incertitude de l'original » ; je trouve 0,82 par rééchantillonnage à deux niveaux (script en annexe). Et le script du texte n'est pas versé (R6).
3. **Ce qui manque est de la vérifiabilité, pas du fond** : la parade contre le choix de la graine est une promesse, sans lieu de registre ni règle de non-rejeu ; le diff v2 → v3 est contrôlé sur les seules fonctions (v2 compte 33 affectations, 2 boucles, 2 conditions et 2 assertions de niveau module que l'essai E5 ne voit pas) ; l'implémentation B n'est vérifiable ni dans ses entrées ni dans son ordre, et sa validation sur la course originale n'exerce aucune des classes « R0 > R2 », « R0 ≳ R2 », « R2 > R0 », « R2 ≳ R0 ».
4. **Deux phrases écrites d'avance seraient fausses dans certaines branches** : « ne rien faire reste équivalent à 0,02 près » quand la classe est « R0 > R2 » (que la Table R0 compte comme répliquée) ; « le seul résultat positif du programme » (affirmation hors de portée du texte, et HR1 est appelé « plomberie » par l'original).
5. **Risque pratique** : la machine est partagée (charge à une minute de 8,6 puis de 2,9 sur 2 cœurs ce soir) alors que la course dure ≈ 28 min à vide sous `timeout 3600` ; le manifeste exige un arbre git propre alors que d'autres sessions y laissent des fichiers non suivis ; le dossier `runs/` de la course originale n'est pas encore rapatrié (CL-08).
6. **Décisions pour Lazar** : N = 100 est déjà retenu par défaut de session (R-1079), à confirmer ou changer avant le scellement ; dire si le « go » du 1er novembre (R-1075) tient lieu de GO de course ; option de seuil « graines neuves » (CL-10).

## 2. Verdict point par point

| Point | Verdict | Ce que j'ai trouvé | Corrections |
|---|---|---|---|
| A. Complétude R1 | **à corriger (mineur)** | Présents : hypothèses signées, prédictions chiffrées avec confiance et réfutation (PR1 à PR2), métrique, seuils, plan d'analyse, V0 (a) à (j), Tables R1, R0, R3, Rii, déclencheurs TR1 à TR4, issue globale à 8 lignes, phrases d'issue, liste d'arrêt à 16 lignes avec garde ou essai. Défauts : liste des champs à remplir incomplète (voir ci-dessous) ; S-N et GO désynchronisés de R-1079 et R-1075 ; « ce que chaque issue change » écrit pour la parole, pas pour la suite. | CL-01, CL-02, CL-13 |
| B. Statistique | **conforme, 3 précisions** | Bornes et niveaux cohérents avec la course originale ; seuil recalculé : concorde ; puissance : plausible, reproduite ; un chiffre (0,85) à corriger. | CL-03, CL-04, CL-09, CL-11 |
| C. Graines (règle D) | **à corriger** | Dérivation sans ambiguïté et vérifiée sur les trois vecteurs ; neuveté acquise par construction et contrôlée empiriquement ; mais la parade contre le choix de la graine est une promesse sans lieu ni vérification, et rien n'interdit de rejouer sur une autre graine après un résultat défavorable. | CL-05, CL-10 |
| D. Fidélité | **à corriger** | Liste C1 à C12 nécessaire (C10 utile mais non nécessaire à la réplication) et insuffisamment contrôlée : E5 trop étroit, E6 sans repli de plate-forme ni budget 1,6, analyse et chemin neuf `_travail` / `main` sans essai. Commande du Plan 5 conforme à la ligne de commande de v2 et à celle de la course originale ; quatre points pratiques à corriger (étape 0 périmée, emplacement de v3, arbre propre, délai). | CL-06, CL-08 |
| E. Indépendance de B | **à corriger** | Procédure énoncée, pas vérifiable : pas de liste fermée d'entrées, pas de contrôle de ce que B a ouvert, ordre « avant le manifeste » invérifiable en l'état, validation limitée aux branches de la course originale, famille du modèle non déclarée. | CL-07, CL-14 |
| F. Revendications | **à corriger (mineur)** | La section « Ce que l'expérience n'autorise pas » dit bien capacité du mélange (9 moniteurs contre 1), attaquant du même optimiseur local, deux budgets non indépendants, portée de « ≈ ». Défauts : le Résumé annonce « montrer » et « à la seule exception des racines » ; une phrase et un chiffre sans source ; le jeu lui-même n'est pas recodé et le texte ne le dit pas. | CL-03, CL-04, CL-12 |
| G. Provenance | **conforme** | 16 empreintes distinctes de 64 chiffres citées, 16 rapprochées de fichiers réels (§ 4.1). | — |
| H. Symétrie R4 | **conforme** | TR1 est bilatéral (|z| > 2,4977, quatre contrastes), TR2 couvre « trop propre », TR3 couvre « défense figée plus belle que l'original », TR4 la non-réplication. Aucune correction du texte ; CL-07 ajoute un essai exécutable du côté « plus beau ». | (CL-07) |

**Liste des champs « À REMPLIR » : incomplète.** Le statut (l. 3) en annonce cinq : code v3 et son empreinte, commit, empreinte de B, décision sur N, contre-lecture. Il y a six marqueurs (l. 10, 19, 25, 35, 188, 380) : manque **l'empreinte de la spécification (l. 19)**. Manquent aussi, sans marqueur : le titre (l. 1, « BROUILLON 1 »), le statut (l. 3), l'auteur et la date (l. 8-9 : « ≈ 21:45 UTC » alors que le fichier a été modifié pour la dernière fois à 21:15 UTC), les mentions « ce brouillon » (l. 165, 253, 373), les rôles (l. 370-376) ; et deux pièces que V0 (g) exige mais qu'aucune ligne n'épingle : le **fichier d'essais v3** et le **journal des essais**. Le validateur `controle_ia.prereg.problemes` ne signale aujourd'hui que deux sections (« Seuil » et « Contre-lecture ») ; son message « marqueur À REMPLIR restant hors des sections exigées » (`prereg.py` l. 46-47) ne se produira qu'une fois ces deux sections remplies, donc les marqueurs des lignes 10, 19, 25 et 35 seront bien vus ensuite, mais pas les points sans marqueur.

## 3. Corrections, avec texte de remplacement prêt à coller

Chaque bloc `text` remplace exactement la ou les lignes indiquées (numéros du brouillon 1 de 380 lignes).

### CL-01 — Statut, auteur, date, pièces épinglées (point A) — obligatoire

Lignes 1, 3, 8-9, 19 et suivante. Constat : liste incomplète (ci-dessus) ; deux pièces non épinglées ; date postérieure à la modification du fichier.

Remplacer la ligne 3 par :

```text
**Statut** : brouillon 1, écrit le 1er novembre 2026 par un sous-agent neuf (Claude Opus 5.5) qui n'a écrit ni le code de la course (v2), ni l'arène v4, ni le préenregistrement original, ni sa lecture, ni son audit. Rien n'est décidé, scellé ni commité. **Reste à faire avant le scellement (liste complète)** : (1) les huit marqueurs « À REMPLIR » : l. 10 (commit), l. 19 (empreinte de la spécification contre-lue), les lignes des essais et du journal des essais ajoutées sous l. 19, l. 25 (empreinte du code v3), l. 35 (chemins et empreintes de l'implémentation B), l'empreinte du script de puissance (§ Seuil), « Contre-lecture » (S-N est rempli : N = 100) ; (2) les passages que le validateur ne voit pas : titre (l. 1), cette ligne, auteur et date (l. 8-9), rôles, et les mentions « ce brouillon » (§ Prédiction « Déclaré », § Plan 8, § Rôles), à mettre à la forme finale ; (3) le bloc d'identité, à régénérer par `arene_regles_defense_v3.py identite` puis à recopier tel quel ; (4) les corrections de la contre-lecture 1 et, s'il y en a une, l'entrée « Contre-lecture 2 ». Le validateur `controle_ia.prereg` refuse ce texte tant qu'un marqueur reste : c'est voulu ; il ne voit pas (2).
```

Remplacer la ligne 1 (au scellement) par :

```text
# Préenregistrement — réplication sur graine neuve de la course de convergence des règles de défense (mélange d'équilibre, défense figée, historique) — v1
```

Remplacer les lignes 8 et 9 par :

```text
- Auteur : sous-agent neuf (Claude Opus 5.5) pour le brouillon 1 ; corrections de la contre-lecture 1 appliquées par la session principale, sans autre changement de fond.
- Date (UTC) : brouillon 1 le 2026-11-01 ; texte scellé le AAAA-MM-JJ à HH:MM UTC (heure relevée par `date -u` au scellement, non estimée).
```

Ajouter après la ligne 19 :

```text
  - essais du code v3 `docs/notes/convergence-defense-v1/regles-defense-v1/test_arene_regles_defense_v3.py` — À REMPLIR (empreinte) ; journal des essais (E1 à E10, E6 lent compris) `…` — À REMPLIR (chemin et empreinte, journal écrit avant le scellement).
```

### CL-02 — S-N et GO de la course (point A) — obligatoire

Lignes 129, 188, 193. Constat : R-1079 (`registres/decisions.md`, ligne 1043) a retenu N = 100 « par défaut de la session (travail sur processeur, R-147) » ; le texte le présente encore comme « À REMPLIR (décision de Lazar) » et dit « défaut sous 48 heures ». Le Résumé 7 demande « le GO de la course » alors que R-1075 (mots de Lazar, 21:30 et 21:36 heure de Paris) donne « go » sur le dossier de preuves, réplication de la course de convergence comprise ; le texte doit dire si ce « go » tient lieu de GO de course.

Remplacer la ligne 129 par :

```text
7. **Décisions** : N = 100 est retenu par défaut de la session (R-1079) ; tu peux le changer avant le scellement, jamais après (un texte modifié est une course nouvelle). Ton « go » du 1er novembre sur le dossier de preuves (R-1075) couvre la préparation de cette réplication ; la course elle-même (processeur seul, 0 USD) part après ton GO consigné (Plan 5, étape 4), sauf si tu écris que R-1075 en tient lieu.
```

Remplacer la ligne 188 par :

```text
**S-N — nombre d'instances par budget** — Valeur : **N = 100** (option (a)), retenue le 1er novembre 2026 par défaut de la session (R-1079 ; travail sur processeur, R-147) ; Lazar peut la remplacer avant le scellement, jamais après.
```

Remplacer la fin de la ligne 193 (à partir de « Défaut sous 48 heures ») par :

```text
Décision : (a) appliquée par défaut le 1er novembre (R-1079). Le GO de la course (processeur, 0 USD) reste celui de Lazar (Plan 5, étape 4).
```

### CL-03 — Résumé : « montrer », « même code », « équivalent », probabilités (points F, B) — obligatoire

Lignes 123, 124 (b), 125, 127. Constat : (i) « Le but est de montrer qu'aucun des deux constats… ne tient à la graine » présuppose le résultat (R3 : aucun run visant un signe positif ; la réplication peut échouer) ; (ii) « même code à la seule exception des racines » est faux : le diff v2 → v3 comprend le chemin de l'arène, l'identité, les gardes et une sortie supplémentaire (C1 à C12) ; (iii) « équivalent, à 0,02 près » (l. 124) et « la même classe » (l. 125) sont inexacts pour les classes « R0 ≳ R2 » et « R0 > R2 », que la Table R0 (ligne 4) compte comme répliquées ; (iv) le chiffre 0,85 (voir CL-11) ; (v) `timeout 3600` (voir CL-08).

Remplacer la ligne 123 par :

```text
1. **Ce qu'on refait** : la course du 1er novembre, avec le même monde synthétique, les mêmes cinq règles, la même configuration au bit et le même N, et un code dont aucun calcul ne change (le diff avec le code de la course est une liste fermée : chemin de l'arène, racines, identité du préenregistrement, sortie supplémentaire ; § Plan 2), sur une **graine neuve que personne ne choisit** : elle est dérivée de l'empreinte de ce texte une fois scellé (règle D, § Plan 3). Le but est de **vérifier si** l'un ou l'autre des deux constats présentés aux mentors tient à la graine de la course originale ; la réplication peut aussi échouer, et chaque issue est écrite d'avance.
```

Dans la ligne 124, remplacer la phrase « (b) **« ne rien faire fait aussi bien »** … sur l'historique. » par :

```text
(b) **« ne rien faire fait aussi bien »** (réfutation de HR0) : à la course originale, le moniteur initial jamais réentraîné est équivalent, à 0,02 près, au moniteur réentraîné sur l'historique, aux deux budgets ; la réplication demande qu'il n'y soit démontré moins bon à aucun budget.
```

Remplacer la ligne 125 par :

```text
3. **Ce qui comptera comme réplication** : (a) une estimation d'au moins **+0,05** aux deux budgets, avec un intervalle B2 (98,75 % bilatéral) dont la borne basse est au-dessus de zéro (le signe est démontré, la taille est estimée) ; (b) aux deux budgets, la classe de l'original, « équivalentes à 0,02 près », ou une classe en faveur de la défense figée (qui déclenche alors un audit, TR3) ; une classe en faveur du réentraînement donne « non répliquée », une classe imprécise « non jugeable ». Probabilités calculées d'avance si la course originale dit vrai : ≈ 1 pour (a), ≈ 0,90 pour (b), ≈ 0,82 en tenant compte de l'incertitude de l'original.
```

Remplacer la ligne 127 par :

```text
5. **Coût** : processeur seul, **0 USD**, ≈ 28 min de mur sur les 2 cœurs d'une machine libre (1 693 s à l'original ; davantage si d'autres tâches tournent), `timeout 7200`.
```

### CL-04 — Phrases écrites d'avance (points F, B) — obligatoire

Lignes 337 et 340. Constat : (i) la phrase « ne rien faire reste équivalent à réentraîner sur l'historique à 0,02 près » est fausse si une classe est « R0 > R2 » ou « R0 ≳ R2 », cas où la Table R0 écrit « répliquée » et où l'audit TR3 se déclenche ; (ii) « le seul résultat positif du programme » (l. 340) est une affirmation sur le programme entier que ce texte ne peut ni vérifier ni autoriser, et la ligne 134 rappelle que le texte original appelle HR1 « plomberie » ; (iii) la phrase de réussite ne dit pas que la taille est estimée, non démontrée (CL-09). Les lecteurs doivent « reprendre telles quelles » ces phrases : elles doivent être vraies dans chaque branche.

Remplacer la ligne 337 par deux puces :

```text
- **Réplication réussie, défense figée équivalente (classes « ≈ » aux deux budgets)** : « Sur une graine neuve que personne n'a choisie — dérivée de l'empreinte du texte scellé —, le mélange d'équilibre reste plus détecteur que la défense réentraînée sur l'historique (+a et +b ; signe démontré, B2 [ … ] et [ … ] ; taille estimée d'au moins 0,05 aux deux budgets) et ne rien faire reste équivalent à réentraîner sur l'historique à 0,02 près (classes « ≈ » ; E8 [ … ] et [ … ]) ; la statistique, recodée par un agent qui n'a pas vu le code, concorde à 10⁻⁹. Les deux constats de la course du 1er novembre ne tiennent donc pas à sa graine. Portée inchangée : même code de simulation, monde synthétique de l'arène v4, deux budgets, huit tours, attaquant local ; la capacité déployée et la force de l'attaquant restent à tester. »
- **Réplication réussie, défense figée meilleure qu'à l'original** (une classe « R0 ≳ R2 » ou « R0 > R2 » à au moins un budget ; l'audit TR3 est rendu) : « … le mélange d'équilibre reste plus détecteur que la défense réentraînée (+a et +b ; … ) et ne rien faire n'est démontré moins bon que réentraîner à aucun budget : classes … ; à tel budget il est meilleur d'au moins […], ce que la course originale ne montrait pas. La phrase « équivalent à 0,02 près » ne vaut que pour les budgets classés « ≈ ». Portée inchangée : (même fin que ci-dessus). »
```

Remplacer la ligne 340 par :

```text
- **Échec de réplication du résultat positif** (après un audit « pas d'artefact ») : « Sur une graine neuve, l'avantage du mélange d'équilibre ne se retrouve pas à la taille de 0,05 (ou s'inverse) : le constat de la course du 1er novembre ne tient pas à la réplication ; il n'est plus présenté comme acquis ; l'écart entre les deux courses devient l'objet d'une enquête (nœud de décision pour Lazar). »
```

### CL-05 — Règle D : parade vérifiable, vocabulaire, non-rejeu (point C) — obligatoire

Lignes 228, 363, 373 ; V0 ; liste d'arrêt. Constats :

1. La règle D est déterministe et publique : n'importe qui calcule ρ d'un texte candidat en microsecondes. La graine n'est donc pas « imprévisible » (mot de la ligne 373), elle est **non choisie** : on ne sait si elle « arrange » un résultat qu'en jouant le jeu dessus (≈ 28 min). La garantie réelle est l'interdiction de jouer le jeu, même réduit, sur une racine dérivée d'un texte non scellé.
2. Cette interdiction est écrite comme une promesse (« personne n'applique la règle D à un brouillon », « une seule version scellée sera lancée »). Le code ne la rend technique que sur un chemin (`exiger_prereg_scelle`) ; le registre des versions scellées n'a pas de lieu ; V0 ne le vérifie pas.
3. Rien n'interdit de relancer une réplication sur une autre graine (texte modifié = racines nouvelles) après un résultat défavorable, puis de ne rapporter que la favorable. Le Plan 7 ne traite que la reprise après interruption.

Dans la ligne 228, remplacer le passage « Aucun tirage n'est fait sur une racine dérivée d'un texte non scellé ; … en rescellant. » par :

```text
**Ce que la règle D garantit et ne garantit pas.** Elle est déterministe et publique : n'importe qui peut calculer ρ d'un texte candidat ; la graine n'est donc pas imprévisible, elle est **non choisie** : personne ne peut savoir si une graine arrange un résultat sans jouer le jeu dessus (≈ 28 min), et jouer le jeu, même réduit, même sur une seule tâche, sur une racine dérivée d'un texte non scellé est interdit (R1). Cette interdiction est une règle de procédure, non un verrou technique ; sa trace est vérifiable : (1) `arene_regles_defense_v3.py` ne dérive de racine qu'après `exiger_prereg_scelle` (E1, E4) ; (2) le lecteur (V0 (k)) compte dans l'historique git les versions scellées de ce texte sous ce nom (`git log --oneline -- prereg/preregistrement-replication-regles-defense-convergence-v1.md` : une seule lancée) et lit dans `registres/decisions.md` l'empreinte de chacune, consignée **avant** la course ; (3) un seul manifeste de réplication existe sous `runs/`. **Aucune seconde course pour changer l'issue** : si l'issue n'est pas « réplication réussie » (échec, partielle, imprécise, artefact), aucune autre réplication n'est lancée sur une autre graine pour en obtenir une autre ; une seconde course, si Lazar la décide, est un préenregistrement nouveau (nouveau texte, nouvelles racines) **rapporté avec** la première, jamais à sa place ni sans elle. Un texte modifié est une course nouvelle (R12).
```

Ajouter à V0 (l. 259), après « (j) … » :

```text
; (k) un seul fichier scellé de ce texte dans l'historique git, l'empreinte de chaque version scellée antérieure consignée dans `registres/decisions.md` avant la course, un seul manifeste de réplication sous `runs/`
```

Ajouter dans la liste d'arrêt (après la ligne 363) :

```text
| Seconde course de réplication lancée pour changer l'issue ; version scellée non consignée | interdit (R1, R12) ; consignation et rapport conjoint des deux courses | V0 (k) |
```

Remplacer, dans la ligne 373, « que la règle D est bien imprévisible pour l'auteur et non réessayable » par :

```text
que la règle D rend la graine non choisie (calculable par tous, inexploitable sans jouer le jeu) et que la parade de procédure du Plan 3 est vérifiable
```

### CL-06 — Essais du code v3 (point D) — obligatoire

Ligne 225. Constats (vérifiés sur le code v2, `9f0dcf5e…`) :

1. **E5 est trop étroit.** « Chaque fonction et classe de niveau module » : v2 compte 37 fonctions, **aucune classe**, et 33 affectations, 2 affectations annotées, 2 boucles `for`, 2 conditions `if`, 2 `assert`, 16 imports et une docstring de niveau module. Une constante décisive comme `MESURES_CONTRASTE` (l. 592), `MESURES_INDICATEUR`, `REGLES`, `CODES`, `NOMS`, `GRILLE_LAMBDA`, `REFERENCES` ou `TOLERANCE_CHOIX_LAMBDA` pourrait changer sans qu'E5 le voie. De plus, les fonctions listées en C4 à C11 sont exemptées de la comparaison : E5 ne dit rien sur ce qu'elles font d'autre que le changement déclaré.
2. **E6 ne couvre pas le chemin de production** (la sérialisation C10 est active en production) ni le budget 1,6, et n'a aucun repli : si l'égalité au bit avec le fichier original échoue pour une raison de plate-forme (processeur différent de celui de la course originale, dont le manifeste donne seulement le noyau et les versions), le plan n'a pas de branche écrite ; l'improviser serait un écart.
3. **Rien ne teste** l'analyse `analyser_regles` (la statistique décisive de A) contre l'analyse scellée, ni les deux chemins nouveaux `_travail` (C8) et `main decision` (C9) de bout en bout ; v2 non plus (ses 25 essais ne testent que le refus sans texte scellé).

Remplacer la ligne 225 par :

```text
Essais `test_arene_regles_defense_v3.py` : les 25 essais de v2 adaptés, plus :
- **E1** règle D : les trois vecteurs d'essai de la spécification § 4 ; gardes, cas sains et artefacts (racines égales, racine dans l'ensemble interdit, racine égale à un vecteur d'essai) ;
- **E2** 20266201 et 20266202 refusées hors de l'essai E6 (cas sain : une racine dérivée est acceptée) ;
- **E3** identité v3 (cas sain ; artefacts : identifiant v2, ligne de la règle D absente, empreinte du code v2 absente) ;
- **E4** décision refusée sans texte scellé (artefact) et acceptée avec un texte temporaire scellé par `sceller_prereg` (cas sain) ;
- **E5** diff restreint : par l'arbre syntaxique (`ast.dump` sans positions), **chaque nœud de niveau module** de v2 — fonctions, affectations (dont `MESURES_CONTRASTE`, `MESURES_INDICATEUR`, `REGLES`, `CODES`, `NOMS`, `GRILLE_LAMBDA`, `REFERENCES`, `TOLERANCE_CHOIX_LAMBDA`), instructions `for`, `if` et `assert`, imports, docstring — est retrouvé à l'identique dans v3, sauf une liste nominative écrite dans l'essai (`VERSION`, `IDENTIFIANT_PREREG`, `ARENE_V4`, les constantes de racines, `RACINES_GELEES`, `RACINES_EMPLOYEES_V1`, `__all__`, et les fonctions des changements C4 à C11) ; tout nœud ajouté, supprimé ou modifié hors liste fait échouer l'essai ; pour chaque fonction de la liste l'essai imprime son diff (`difflib`) dans le journal, que le contre-lecteur lit : il ne doit contenir que les lignes décrites par C1 à C12 ;
- **E6 (lent)** non-régression au bit, **sur le chemin de production** (sérialisation C10 active) : v3 rejoue les tâches (δ 1,4 ; instances 0 et 1) et (δ 1,6 ; instance 0) de la course originale sur leurs racines d'origine (autorisation posée par l'essai seulement ; aucune information neuve : résultats déjà scellés et lus) et rend au bit, pour les cinq variantes, `V_iii_final`, `V_iii_standard`, `V_iii_renforce`, `exploitabilite_moyenne_tours`, `ii_final`, `fpr_final`, `par_tour.iii`, `par_tour.ii`, `poids_finaux` de `resultats-regles-defense.json` (`d07ece47…`) ; **si l'égalité au bit avec ce fichier échoue**, l'essai rejoue les mêmes tâches avec le code v2 inchangé sur cette machine et compare v3 à v2 au bit : v3 = v2 ici suffit pour passer (l'écart avec le fichier original est consigné comme différence de plate-forme, avec sa taille maximale), v3 ≠ v2 arrête ;
- **E7** la sérialisation ne change aucune valeur (une tâche, petite configuration, avec et sans) ;
- **E8** non-régression de l'analyse : `analyser_regles` de v3, appliquée aux résultats originaux (`d07ece47…`) avec la racine 20266201, rend au bit l'analyse originale (`18b80112…`) pour les 16 contrastes sur les deux budgets (quelques secondes) ;
- **E9** garde de l'étape C8 : cas sain (les racines dérivées dans le processus de travail égalent celles de la tâche) et artefact (une racine de tâche modifiée d'une unité est refusée, sans repli) ;
- **E10** bout en bout minuscule : `main decision` sur une configuration réduite (2 instances, 2 tours, petits échantillons), avec un texte temporaire scellé dont la racine dérivée dépasse 2⁶³ (chercher un texte temporaire qui y conduit, hors de tout texte réel), dans un dépôt git temporaire propre si le manifeste est écrit : manifeste, résultats et analyse écrits, racines relues exactement (entiers et chaînes), aucune conversion en binaire64.
```

(Durée de E6 : ≈ 50 s de processeur au lieu de ≈ 35 s ; le « ≈ 1 min » de l'étape 1 du Plan 5 devient « ≈ 2 min ».)

### CL-07 — Implémentation B vérifiable ; cas limites ; gardes ; symétrie exécutable (points E, H et règle R5) — obligatoire

Lignes 35, 231, 259 (V0 (h)), 356, 372. Constats :

1. **Entrées non fermées.** Le texte dit que B « ne voit ni le code v2, ni le code v3, ni l'arène », mais le dépôt les contient. Les entrées isolées existent (`implementation-b/entrees/` : spécification `2a1ad6d3…`, résultats `d07ece47…`, analyse `18b80112…`, vérifiées, commitées en `f6641bc0`) ; le texte ne les nomme pas et ne prévoit aucun contrôle de ce que B a réellement ouvert.
2. **Ordre invérifiable.** « Scellée avant la création du manifeste » : le scellement par fichier compagnon `.sha256` ne porte pas d'horodatage ; la seule preuve d'ordre est l'historique git.
3. **Validation aveugle aux branches.** La course originale rend seulement, sur V : « ≈ », « R2 ≳ R1 », « ? », « R3 > R2 », « R4 ≳ R2 » (Table B) et les lignes 1 et 4 de la Table C (spécification § 12). B n'est donc jamais éprouvée sur « R0 > R2 », « R0 ≳ R2 », « R2 > R0 », « R2 ≳ R0 », « R4 > R2 », « R2 > R4 », ni sur les lignes 2, 3, 5, 6 de la Table C, ni sur TR3 et TR4, ni sur la lecture d'entiers de plus de 2⁶³ (les racines originales valent 20266201 : un lecteur qui convertit en binaire64 passerait la validation puis échouerait sur la réplication). Ces branches décident pourtant HRép0.
4. **Règle R5** (garde testée sur un cas sain et sur un artefact) : pour la garde « graines non neuves », la spécification § 12 ne donne que l'artefact (la course contre elle-même) ; son « cas sain » est celui de la règle D, pas celui de la garde.
5. **Famille.** R-1079 annonce « un agent d'une autre famille » ; le texte dit seulement « agent neuf ».

Remplacer le § 4 (lignes 230 et 231, titre compris) par :

```text
### 4. Implémentation indépendante B
**Entrées (liste fermée)** : exactement les trois fichiers de `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/` : la spécification dans sa version finale (empreinte écrite ici au scellement), les résultats originaux `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b`, l'analyse originale `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42`. **B n'a pas accès** au code v2, au code v3, à l'arène v4, au préenregistrement original, à sa lecture ni à son audit : elle est lancée dans un répertoire de travail limité à `implementation-b/`, avec la consigne écrite de ne rien ouvrir hors de `entrees/`, et son rapport donne la liste de tous les fichiers qu'elle a ouverts. Famille du modèle de B : [à déclarer par la session qui la lance ; R-1079 prévoit « une autre famille » que celle de l'auteur de la spécification].
**Validation avant scellement** (rapport scellé avec le code) : (1) sur la course originale : spécification § 12, écart ≤ 10⁻⁹ sur les 16 contrastes de chaque budget, classes et verdicts originaux retrouvés ; (2) **branches que la course originale n'exerce pas** : une ligne de test par ligne de chaque table (A, B, B′, C, R1, R0, R3, Rii, issue globale), sur des vecteurs de différences synthétiques dont la ligne attendue est connue d'avance (moyenne et dispersion choisies), par exemple « R0 > R2 », « R0 ≳ R2 », « R2 ≳ R0 », « R2 > R0 » ; (3) **gardes de réplication, cas sain et artefact**, sur des variantes de la course originale : (a) original contre lui-même : g_π = 0, TR2 déclenché, 200 égalités par variante, arrêt « graines non neuves » ; (b) cas sain : V (les trois champs V_iii_final, V_iii_standard, V_iii_renforce) de toutes les variantes décalé de +10⁻⁶ et celui de R3 de +0,01 : aucune égalité, ni TR1, ni TR2, ni arrêt ; (c) R3 décalé de +0,06 : TR1 déclenché vers le haut ; (d) R3 décalé de −0,03 borné à zéro : TR1 déclenché vers le bas (le signe de z_π est celui du décalage) ; (4) **lecture exacte des entiers de 64 bits** : fichiers synthétiques dont les racines dépassent 2⁶³, et règle D sur les trois vecteurs d'essai.
**Ordre et scellement** : code, essais et rapport de validation de B sont commités avec leurs empreintes **avant** la création du manifeste de la course ; V0 (h) le vérifie mécaniquement (le commit de B est l'ancêtre du commit du manifeste : `git merge-base --is-ancestor`).
```

Remplacer V0 (h) (ligne 259) par :

```text
(h) implémentation B : code, essais, rapport de validation et leurs empreintes (celles de la ligne « Implémentation indépendante B » du bloc d'identité) présents dans le commit du manifeste ou l'un de ses ancêtres (`git merge-base --is-ancestor`) ; validation passée (§ Plan 4, points (1) à (4)) ; liste des fichiers ouverts par B limitée aux trois entrées de `implementation-b/entrees/`
```

Remplacer la ligne 35 par :

```text
- Implémentation indépendante B : chemins et empreintes du code, des essais et du rapport de validation — À REMPLIR (commités avant la création du manifeste de la course)
```

Dans la ligne 372, remplacer « agent neuf, qui ne voit que la spécification (et les formats de fichiers qu'elle décrit), ni v2, ni v3, ni l'arène » par :

```text
agent neuf d'une autre famille [à confirmer], qui ne voit que les trois fichiers de `implementation-b/entrees/` (la spécification et les deux fichiers originaux), ni v2, ni v3, ni l'arène
```

Note d'exécution : B est lancée aujourd'hui (le dossier `implementation-b/` contient déjà du code), sur la spécification `2a1ad6d3…`. Toute correction de la spécification (CL-10) ou de ses vecteurs doit lui être transmise avant qu'elle termine, ou B est relancée : V0 (h) exige que l'empreinte de la spécification lue par B soit celle de la version finale.

### CL-08 — Plan 5 : rapatriement, placement de v3, arbre propre, délai (point D) — obligatoire

Lignes 127 (déjà traitée en CL-03), 186, 234, 235, 239, 240. Constats :

1. **Étape 0 périmée.** R-1079 a déjà rapatrié 80 fichiers (`docs/notes/convergence-defense-v1/`, `diag/…`, préenregistrement scellé ; 40 sceaux sur 40 conformes). Reste `runs/20261101-160323-regles-defense-convergence/`, absent de l'arbre (vérifié) ; son manifeste est lisible sur la branche et sa somme est celle que le brouillon cite (`36db58cf…`).
2. **Placement de v3.** Le code v2 lit le gel à côté de lui (`GEL = ICI / …`) : v3 et ses essais doivent être copiés, octet pour octet, dans `docs/notes/convergence-defense-v1/regles-defense-v1/`, alors que les fichiers sont aujourd'hui sous `brouillons/preuves-mentors-v1/convergence-replication-v1/code/` ; l'empreinte du bloc d'identité est celle de la copie placée.
3. **Arbre propre.** `creer_manifeste` exige `git status --porcelain --untracked-files=all` vide. L'arbre partagé reçoit les fichiers d'autres sessions (14 entrées non suivies à 22:53 heure locale, dont des fichiers de `brouillons/` d'autres tâches).
4. **Délai.** La course a duré 1 692,7 s sur deux processus à vide. La charge à une minute était de 8,56 à 22:42 et de 2,91 à 22:53 (heure locale, 2 cœurs, `nproc` = 2) à cause des sous-agents en cours : avec une charge de 4, la course dépasse 3 600 s, et la garde de 600 s de processeur par tâche ne s'applique pas (c'est du temps processeur, non du temps de mur). Une interruption coûte une reprise complète puis « non jugeable (plomberie) ».

Remplacer la ligne 186 par :

```text
- **S8 : `timeout 7200`** (quatre fois la durée observée à vide, 1 692,7 s : la machine est partagée avec d'autres sessions), 2 processus, 600 s de processeur par tâche (garde interne inchangée). Condition de départ : charge à une minute ≤ 1,0 relevée par `uptime` et consignée, et aucune autre tâche de calcul lancée pendant la course.
```

Remplacer les étapes 0 et 1 (lignes 234 à 236) par :

```text
0. **Préparation** (dans `/home/claude/controle-ia-travail`, aucune ref `donnees/*`, aucun `git fetch` sans refspec) : au 1er novembre soir, `docs/notes/convergence-defense-v1/`, `diag/20261101-160323-regles-defense-convergence/` et `prereg/preregistrement-regles-defense-convergence-v1.md` (avec leurs compagnons) sont déjà dans l'arbre (R-1079, 40 sceaux sur 40 conformes). **Reste à rapatrier** `runs/20261101-160323-regles-defense-convergence/` (manifeste et `pids-travail.txt`, avec compagnons) depuis la branche déjà récupérée `origin/canal/session-depot-reprise-n67` (par exemple `git checkout origin/canal/session-depot-reprise-n67 -- runs/20261101-160323-regles-defense-convergence`), puis vérifier leurs empreintes (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier <fichiers>` ; manifeste attendu `36db58cfac9bfc4cf199ca5cdf74ac17ea24afab84b95ffd0aac945b922a6720`). Ne déplacer ni renommer, jusqu'à la fin de la course, les chemins que ce texte cite sous `brouillons/` (l'arène v4 de `canal-reprise-releve-v1`, le dossier de la réplication).
1. **Placement et essais du code v3** : copier `arene_regles_defense_v3.py` et `test_arene_regles_defense_v3.py` octet pour octet dans `docs/notes/convergence-defense-v1/regles-defense-v1/` (le code lit le gel v2 à côté de lui ; l'empreinte du bloc d'identité est celle de cette copie), puis (≈ 2 min dont ≈ 50 s de processeur pour E6) :
   `cd /home/claude/controle-ia-travail/docs/notes/convergence-defense-v1/regles-defense-v1 && PYTHONPATH=/home/claude/controle-ia-travail/src OMP_NUM_THREADS=1 REGLES_ESSAIS_LENTS=1 /home/claude/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_arene_regles_defense_v3.py` ; journal et empreinte consignés (lignes « essais » et « journal » des documents qui font foi).
```

Remplacer l'étape 4 (ligne 239) par :

```text
4. **Contre-lecture** (R2) puis **scellement** de ce texte sous `prereg/preregistrement-replication-regles-defense-convergence-v1.md` (`controle_ia.prereg.sceller_prereg`) ; empreinte de ce texte consignée dans `registres/decisions.md` ; commit. **Arbre propre exigé par le manifeste** : `git status --porcelain --untracked-files=all` doit être vide ; l'arbre partagé reçoit les fichiers d'autres sessions, donc lancer la course depuis une copie propre du dépôt au commit scellé (par exemple `git worktree add`, à essayer avant la course : le manifeste lit l'état git du répertoire courant), avec l'interpréteur `/home/claude/controle-ia-travail/.venv/bin/python`, et consigner la sortie de `git status` ; les sorties sont ensuite commitées depuis cette copie. **GO de Lazar** consigné (ou mention explicite que R-1075 en tient lieu) ; charge relevée par `uptime` (≤ 1,0 à une minute) et consignée ; aucune autre charge lourde sur la machine pendant la course.
```

Dans l'étape 5 (ligne 240), remplacer « (≈ 28 min de mur ; 1 692,7 s à l'original ; plafond 60 min) » par « (≈ 28 min de mur à vide ; 1 692,7 s à l'original ; plafond 120 min) » et `timeout 3600` par `timeout 7200` dans la commande.

La commande elle-même est conforme : mêmes options que celle du manifeste original (`decision --prereg … --instances 0:100 --run-id … --lambda 0.3 --reference moyenne --processus 2`), identifiant de run conforme au motif `^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$`.

### CL-09 — HRép1 : signe démontré, taille estimée (point B) — recommandée

Ligne 144. Constat : « d'au moins τ = +0,05 à chaque budget, avec la borne basse de B2 strictement positive (signe et taille) » laisse croire que la taille est démontrée. La Table R1 (ligne 3) exige est_c ≥ 0,05 (estimation ponctuelle) et bas_c > 0 : seul le signe est démontré. La conséquence est faible aux erreurs-types de la course originale (0,0057 et 0,0043) : si l'effet vrai valait 0,03, l'estimation atteindrait 0,05 avec une probabilité de l'ordre de 2 × 10⁻⁴ au budget 1,4 et de 2 × 10⁻⁶ au budget 1,6, et il faut les deux budgets. Mais le texte doit dire ce que « répliquée » établit.

Remplacer la première phrase de la ligne 144 (jusqu'à « (signe et taille). ») par :

```text
- **HRép1 (primaire) — « le mélange bat l'historique » tient sur graine neuve** : Δ(R3, R2) = moyenne sur les instances de V(R3) − V(R2) a, à chaque budget, une estimation d'au moins τ = **+0,05** et une borne basse de B2 strictement positive : le **signe est démontré** (98,75 % bilatéral), la **taille est seulement estimée** (une borne basse entre 0 et 0,05 est permise ; « répliquée » ne dit pas que l'effet vrai atteint 0,05).
```

### CL-10 — Liste d'arrêt, concordance, « graines neuves » (points B, C, D) — recommandée

Lignes 184, 360, 361 ; Table R1 ; spécification § 6 (l. 114) et § 10.3. Constats :

1. **Incohérence de la spécification.** § 6 (l. 114) : « l'arrêt pour discordance ne porte que sur les décisifs et le secondaire » (quatre contrastes) ; § 11 (« Concordance exigée ») ajoute le descriptif (R1, X̄), soit cinq contrastes, et classe les 11 autres en alerte. La liste d'arrêt (l. 361) reprend la version courte. B lit la spécification : les deux textes doivent dire la même chose.
2. **Étiquette contradictoire.** La ligne 360 écrit « arrêt ; non jugeable (artefact) » ; l'issue globale (ligne 1) range toute condition d'arrêt sous « non jugeable (plomberie) » et réserve « artefact » au rapport d'audit.
3. **Qui, quand.** La garde « graines non neuves » n'a ni auteur désigné ni moment : elle ne peut être calculée qu'après la course (par B, recomptée par le lecteur), donc avant toute lecture, pas pendant le jeu.
4. **Seuil lâche (option).** « Plus de 10 tâches sur 200 » : le nombre attendu de coïncidences au bit par hasard est de 0,04 à 0,08 par variante sur les 200 tâches (11 paires égales sur 49 500 dans la course originale, soit 2,2 × 10⁻⁴ ; script du contre-lecteur), donc « plus de 2 tâches » (probabilité < 10⁻⁴ par variante au hasard) reste sûr et mieux placé ; le défaut réel serait un lot de graines partiellement réutilisé, que 10 tâches laissent passer. Garder 10 est acceptable ; je recommande 2 et l'extension à X̄ et à (ii) (sans effet sur la décision). Cela touche aussi la spécification § 10.3, donc B : à trancher avant qu'elle termine.
5. **Ligne inatteignable.** Table R1 ligne 2 (« jeu dégénéré ») est déjà couverte par T2 (ligne 1 : « moy_c(k, V) ≤ 2α pour les cinq variantes » figure dans T2, spécification § 7) ; sans effet, à garder pour correspondre mot pour mot à la Table A originale.
6. **Interdits de procédure.** Trois lignes de la liste d'arrêt n'ont ni garde ni essai (lecture avant scellement, appel de modèle ou réseau, `git fetch` sans refspec) : ce sont des interdits de procédure, pas des gardes au sens de R5 ; le texte doit le dire.

Remplacer la ligne 361 par :

```text
| Discordance A/B > 10⁻⁹ sur l'un des cinq contrastes de concordance exigée (spécification § 11 : (R3, V), (R0, V), (R4, V), (R0, (ii)), (R1, X̄)) ou sur z_π ; classe, ligne de table, contrôle de santé ou verdict brut différent hors « frontière numérique » (spécification § 8) ; une discordance sur l'un des 11 autres contrastes est une alerte consignée, non un arrêt | arrêt ; aucune lecture ; diagnostic par un sous-agent neuf ; toute correction après lecture = écart au préenregistrement (nœud de Lazar) | spécification § 11 |
```

Remplacer la ligne 360 par :

```text
| Graines non neuves : plus de 2 tâches égales au bit à l'original, pour une variante, sur V, X̄ ou (ii) (option : garder « plus de 10 » sur V seul) | arrêt après la course et avant toute lecture ; issue globale ligne 1 (« non jugeable (plomberie) ») ; l'audit peut la requalifier en artefact | calculé par B, recompté par le lecteur ; spécification § 10.3 ; testé cas sain et artefact (§ Plan 4, point (3)) |
```

Dans la spécification (`specification-statistique-decisive-v1.md`, ligne 114) : remplacer « l'arrêt pour discordance ne porte que sur les décisifs et le secondaire » par « l'arrêt pour discordance porte sur les cinq contrastes de concordance exigée du § 11 (les trois décisifs, le secondaire et (R1, X̄)) ; les 11 autres donnent une alerte ».

Ajouter sous le tableau de la liste d'arrêt (après la ligne 366) :

```text
Les lignes « Lecture d'un résultat de la réplication avant scellement », « Appel de modèle, réseau, dépense » et « `git fetch` sans refspec » sont des interdits de procédure (vérifiés par le lecteur sur les registres et l'historique git), non des gardes de code au sens de R5.
```

### CL-11 — Chiffres de puissance et sources (points B, G, règle R6) — recommandée

Lignes 125 (déjà traitée en CL-03), 136, 191, 195. Constats :

1. « ≈ 0,85 en tenant compte de l'incertitude de l'original » (l. 125, 191) : le texte ne dit pas comment. Par un rééchantillonnage à deux niveaux (la « vérité » est un rééchantillon de l'original, puis la réplication tire dans cette vérité), je trouve **0,82** (non répliquée 0,010 ; non jugeable 0,171). À un niveau (vérité = original) : 0,903 (approximation normale, comme le texte) et 0,918 (rééchantillonnage percentile réel, 500 tirages). Le 0,903 du texte est exact ; 0,85 n'est pas reproduit.
2. Le script de puissance est « dans son dossier temporaire, non versé » (l. 195) : un chiffre sans chemin ni empreinte viole R6. L'annexe donne un script qui relit le fichier de résultats original (empreinte vérifiée) et reproduit les lignes 1 de la table (HRép1 1,000 ; HRép0 0,903 / 0,000 / 0,097).
3. Ligne 136 : « ≈ 17 % du niveau de V au δ 1,4 » : 0,02 / 0,1220 = 16,4 % (0,02 / 0,1244 = 16,1 % pour R0) ; au budget 1,6 : 30,9 % (29,2 % pour R0). Écrire « ≈ 16 % » et « ≈ 30 % ».
4. Les corrélations de la ligne 137 (0,45 et 0,20) sont exactes (0,453 et 0,201, recalculées).

Remplacer le passage « (≈ 0,85 en comptant l'incertitude de l'original) » de la ligne 191 par :

```text
(≈ 0,82 en comptant l'incertitude de l'original, rééchantillonnage à deux niveaux du script versé)
```

Remplacer, dans la ligne 195, « script de l'auteur dans son dossier temporaire, non versé » par :

```text
script `brouillons/preuves-mentors-v1/convergence-replication-v1/puissance-replication-v1.py` (empreinte À REMPLIR, versé avant le scellement ; il relit `d07ece47…` et vérifie son empreinte) ; recalcul du contre-lecteur par un script distinct (rapport de contre-lecture, annexe) : HRép1 1,000, HRép0 0,903 (approximation normale) et 0,918 (percentile réel), 0,82 avec l'incertitude de l'original
```

Dans la ligne 136, remplacer « ≈ 17 % du niveau de V au δ 1,4, ≈ 30 % au δ 1,6 » par « ≈ 16 % du niveau de V au δ 1,4, ≈ 30 % au δ 1,6 ».

### CL-12 — « Ce que l'expérience n'autorise pas » : jeu non recodé ; source du pilote (points F, G) — recommandée

Lignes 134 et 138. Constats : (i) la réplication rejoue le même simulateur (jeu, attaquant, oracle, finale) ; seule la statistique est recodée par B. Une erreur du simulateur, commune aux deux courses, se retrouverait à l'identique et serait prise pour de la robustesse ; le texte ne le dit pas explicitement (« rien au-delà de la robustesse à la graine » le suggère). (ii) Ligne 134 : « Au pilote de l'arène v4 (non opposable), des combinaisons déterministes des mêmes moniteurs faisaient nettement mieux que le mélange » n'a pas de renvoi. La source existe : `docs/notes/convergence-defense-v1/argon-seul-convergence-v1/reponse-argon-convergence-v2-v1.md` (`fa49440fb82f4eec528a712ee619fe5359cb94b47bbdd91b8e2ab262004ace49`), lignes 102 et 254, qui cite les chiffres du pilote.

Ajouter une puce après la ligne 135 :

```text
- **Même simulateur, jeu non recodé** : le code v3 rejoue le jeu, l'attaquant, l'oracle et la finale de v2 sans changement ; seule la statistique est recodée par une seconde implémentation (B). Une erreur du simulateur, commune aux deux courses, se retrouverait dans la réplication et serait prise pour de la robustesse. Une réplication sur graine neuve teste la dépendance à la graine, pas l'exactitude du jeu.
```

Dans la ligne 134, remplacer « Au pilote de l'arène v4 (non opposable), des combinaisons déterministes des mêmes moniteurs faisaient nettement mieux que le mélange. » par :

```text
Au pilote de l'arène v4 (chiffres cités, non vérifiés sur la pièce d'origine, par `docs/notes/convergence-defense-v1/argon-seul-convergence-v1/reponse-argon-convergence-v2-v1.md`, `fa49440f…`, l. 102 : B − C3 = −0,1935 et −0,1443, B − D = −0,2341 et −0,1795), des combinaisons déterministes des mêmes moniteurs faisaient nettement mieux que le mélange.
```

### CL-13 — Ce que chaque issue change (point A) — recommandée

Après la ligne 343 (sous les phrases d'issue). Constat : les phrases disent quoi écrire, pas ce que l'issue autorise ou décide ensuite.

Ajouter :

```text
**Conséquence de chaque issue (rien d'autre n'est autorisé)** :
1. non jugeable (plomberie) : aucune phrase sur la réplication ; reprise selon la liste d'arrêt ; Lazar informé du motif.
2. en attente d'audit : aucune phrase ; audit confié à un sous-agent neuf ; le rapport scellé rétablit ou non les verdicts bruts.
3. non jugeable (artefact) : aucune phrase ; version nouvelle du texte (nouvelles racines), rapportée avec celle-ci (§ Plan 3).
4. échec de réplication du résultat positif : le constat « le mélange bat l'historique » n'est plus présenté aux mentors comme acquis ; enquête sur l'écart (nœud de décision pour Lazar) ; aucune seconde graine pour changer l'issue.
5. réplication réussie : les deux constats peuvent être présentés par Lazar (contact externe : Lazar décide et envoie) avec la mention « réplication sur graine neuve, même code, même monde » et la portée du § Ce que l'expérience n'autorise pas ; aucune généralisation.
6. réplication partielle (équivalence non tenue) : la phrase « ne rien faire fait aussi bien » est retirée ; HR1 est présenté avec sa réplication.
7. réplication partielle (équivalence imprécise) : « ne rien faire fait aussi bien » reste la phrase d'une seule course, dite comme telle.
8. non jugeable : aucune phrase.
```

### CL-14 — Section « Contre-lecture », contre-lecture 2, ordre des travaux (points A, E) — recommandée

Lignes 378-380. Remplacer la ligne 380 par l'entrée suivante (l'empreinte du présent rapport s'écrit après `sha256sum` : un rapport ne peut contenir sa propre somme) :

```text
**Contre-lecture 1** — sous-agent neuf (Claude Sonnet 5.5), 1er novembre 2026 ; brouillon relu : `brouillons/preuves-mentors-v1/convergence-replication-v1/preenregistrement-replication-convergence-v1-brouillon1.md`, empreinte `f0fd07874c6bba5dfb71c845a693749015caaee2b554ae5772c93b2a82dd7c76` ; rapport : `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-preenregistrement-replication-v1.md`, empreinte À REMPLIR (somme du rapport, calculée par la session principale) ; verdict : scellable après corrections mineures ; traitement : CL-01 à CL-14, une ligne chacune (accepté, ou refusé et pourquoi).
```

Recommandation : **contre-lecture 2**, courte, par un autre sous-agent neuf, sur : le texte corrigé, `arene_regles_defense_v3.py` et son fichier d'essais, le journal des essais, le code, les essais et le rapport de validation de B. Points à juger : E5 à E10 réellement présents ; diff C1 à C12 (pas de calcul changé, diffs de E5 lus) ; B conforme à CL-07 ; texte et spécification d'accord (CL-10). Ajouter ensuite l'entrée « Contre-lecture 2 » (deux empreintes, exigées par le validateur).

Ordre recommandé : (1) appliquer CL-01 à CL-14 au texte et, pour CL-10, à la spécification, **avant** que B termine (sinon la relancer, V0 (h) exigeant l'empreinte finale) ; (2) code v3 et essais conformes à CL-06 ; B et sa validation conformes à CL-07 ; (3) contre-lecture 2 ; (4) régénérer le bloc d'identité, remplir les marqueurs, valider (`problemes` muet), sceller, consigner l'empreinte dans `registres/decisions.md`, commiter ; (5) GO, course, B, comparaison A/B, lecteur R13.

## 4. Ce que j'ai vérifié moi-même

### 4.1 Provenance (point G) : conforme, 16 sur 16

Les 16 empreintes distinctes de 64 chiffres du brouillon (extraites par motif, comparées par script aux sommes `sha256sum` des fichiers réels) sont toutes exactes :

| Pièce | Empreinte (12 premiers chiffres) |
|---|---|
| préenregistrement original `prereg/preregistrement-regles-defense-convergence-v1.md` | `d82dea338868` |
| code v2 `docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v2.py` | `9f0dcf5e0d10` |
| essais v2 `…/test_arene_regles_defense_v2.py` | `78d979ab76bb` |
| gel v2 `…/gel-regles-defense-v2.md` | `9977d7df7f87` |
| arène v4 `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/arene_melange_v4.py` | `70c77fd5c0ec` |
| résultats `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` | `d07ece476cc1` |
| analyse `diag/20261101-160323-regles-defense-convergence/analyse-regles-defense.json` | `18b801123040` |
| manifeste `runs/20261101-160323-regles-defense-convergence/manifeste.json` (lu par `git show` sur `origin/canal/session-depot-reprise-n67` ; absent de l'arbre) | `36db58cfac9b` |
| lecture `…/lecture-course-regles-defense-v1.md` | `24081eed65ce` |
| audit « trop beau » `…/audit-trop-beau-course-regles-defense-v1.md` | `7e81d094868e` |
| gabarit `prereg/gabarit-preregistrement-v1.md` | `8cad43714b56` |
| bibliothèques `src/controle_ia/gardes.py`, `prereg.py`, `scellement.py`, `manifeste.py` | `a83c48ceba48`, `3b2e3ee56463`, `93beeb1c8aae`, `1a5c7464523e` |
| configuration canonique (somme `config_sha256` du manifeste original) | `3fbb27fc0824` |

Recoupements : le manifeste original enregistre la racine 20266201, la racine tenue 20266202, `arene_v4_sha256` = `70c77fd5…` (donc la copie suivie par git est bien identique au bit au fichier chargé par la course, sans lire `donnees/`), `gel_sha256` = `9977d7df…`, `code_sha256` = `9f0dcf5e…`, les quatre sommes de bibliothèque (inchangées depuis), `commit` = `1dc492bae948c08b523378b839e0e6a2d0704f8d`, la commande `decision --prereg … --instances 0:100 --run-id … --lambda 0.3 --reference moyenne --processus 2`. Le JSON de configuration canonique du brouillon est identique au bit à celui du texte original. Les trois fichiers de `implementation-b/entrees/` ont les sommes `2a1ad6d3…` (spécification, identique à la copie principale), `d07ece47…`, `18b80112…`. Le chemin de la lecture donné dans la mission (`…/session-depot/convergence-resultats-v1/`) n'existe pas ; j'ai lu les copies de `docs/notes/convergence-defense-v1/regles-defense-v1/`, de même somme.

### 4.2 Règle D (point C)

Recalculée sans le code de la course : `SeedSequence(entropy=int(H, 16)).generate_state(2, dtype=numpy.uint64)` avec numpy 2.4.6 rend exactement les trois vecteurs de la spécification § 4 : `d82dea33…` → (11786724493248295725, 9136419304016434890) ; soixante-quatre « 0 » → (15793235383387715774, 12390638538380655177) ; soixante-quatre « f » → (10168828190493638947, 4616211851522120706). Aucun n'est dans F. La constante z* = 2,497705474412374 est le quantile 0,99375 de la loi normale (`scipy.stats.norm.ppf`, égal au bit). Les gardes de neuveté (ρ ≠ ρ_t, hors F, hors vecteurs) sont formelles : la probabilité qu'une dérivation légitime les touche est de l'ordre de 10⁻¹⁵ ; la neuveté tient à la construction (entropies distinctes, flux indépendants) et au contrôle empirique (coïncidences au bit). La parade contre le choix de la graine est discutée en CL-05.

### 4.3 Statistique (point B)

- **Recodification sans importer le code**, d'après la spécification : écart maximal 0,0 sur les moyennes, écarts-types et dix quantiles des 16 contrastes pour chaque budget, par rapport à `analyse-regles-defense.json` (`18b80112…`) ; vecteurs du générateur du § 5.5 retrouvés (indices 80, 79, 39, 86, 45, 87, 54, 22, 58, 80 pour la clé (1, 203, 0, 0, 99)) ; tableau du § 12 identique ; classes de l'original retrouvées.
- **Contrôles de santé** recalculés sur les résultats originaux : T2 non ; T3 0 tâche à poids pur ; T4 5 et 2 tâches sur 100 à cosinus moyen ≥ 0,999 (seuil 50) ; T5 écarts 0,00039 et 0,00043 (δ 1,4), 0,00029 et 0,00040 (δ 1,6) (seuil 0,01) ; T6 0,00019 et 0,00016 (seuil 0,001) ; V = min(standard, renforcé) exact.
- **Bornes et niveaux** : HRép1 : B2 = [q0,00625 ; q0,99375] (98,75 % bilatéral, quatre tests de Bonferroni), comme la Table A originale. HRép0 et HRép3 : B8 = [q0,003125 ; q0,996875] (99,375 %) et E8 = [q0,00625 ; q0,99375] pour l'équivalence, comme la Table B originale. HRép-ii : B8, Table C. Rééchantillonnage apparié des instances, B = 20 000, quantiles linéaires (type 7). TR1 : z* = 2,4977 (Bonferroni 5 % sur quatre contrastes).
- **Cohérence avec l'original.** HRép1 : réplique en plus strict (estimation ≥ 0,05 contre ≥ 0,02 à l'original). HRép0 : l'original concluait « réfutée » si « R0 > R2 », « R0 ≳ R2 » ou « ≈ » à **un** budget ; la réplication exige les trois classes aux **deux** budgets (plus strict) et « même classe » signifie « même classe ou meilleure pour la défense figée » (déclaré à la ligne 145, à répéter au Résumé : CL-03). Une classe « R0 ≳ R2 » ou « R0 > R2 » déclenche TR3 : audit.
- **Recalcul d'un seuil.** R0 − R2 : écart-type 0,0438 (δ 1,4) et 0,0384 (δ 1,6), erreurs-types 0,0044 et 0,0038 ; m = 0,02 vaut 4,5 et 5,3 erreurs-types ; demi-largeur d'E8 = 2,4977 × erreur-type = 0,0110 et 0,0095 ; borne haute d'E8 originale (+0,0134 ; +0,0133) à 0,0066 et 0,0067 de m, soit 1,5 et 1,75 erreur-type : **concorde** avec « 1,5 à 1,7 » (l. 190). Pour rendre « ≈ » à un budget il faut est_rép < 0,0090 (δ 1,4), < 0,0105 (δ 1,6) : probabilité Φ(1,5) = 0,93 et Φ(1,79) = 0,96 si l'original dit vrai, ≈ 0,90 aux deux budgets (corrélation 0,20 entre budgets) : **concorde** avec 0,903.
- **Puissance.** HRép1 : estimations originales 0,1045 et 0,1236 contre τ = 0,05, soit 9,6 et 17 erreurs-types au-dessus ; borne basse de B2 0,0906 et 0,1127 : 1,000. HRép0 (script en annexe) : 0,903 / 0,000 / 0,097 par approximation normale (valeurs du texte : 0,903 / 0,000 / 0,096), 0,918 / 0,000 / 0,082 par rééchantillonnage percentile réel, 0,82 / 0,010 / 0,171 avec l'incertitude de l'original. Les autres lignes de la table de puissance (effet de HR1 réduit de moitié : 0,655 ; +0,06 : 0,955 ; Δ(R0, R2) = −0,01 : 0,317 / 0,535 ; −0,02 : 0,999 de « non répliquée ») sont plausibles à ±0,02 près par un calcul normal élémentaire ; HRép3 (1,000) reproduit.
- **TR2** : « probabilité ≈ 2,5 × 10⁻⁴ » : produit des quatre probabilités marginales |g_π| < 0,001 (0,100 × 0,132 × 0,129 × 0,147) = 2,5 × 10⁻⁴, calculé comme si les quatre écarts étaient indépendants ; avec les corrélations entre budgets (0,45 et 0,20) la probabilité réelle est un peu plus forte ; sans importance pour la décision.
- **Graines neuves.** Dans la course originale, 11 paires de tâches de même variante et même budget ont un V égal au bit sur 49 500 paires (2,2 × 10⁻⁴) ; nombre attendu de coïncidences par variante sur 200 tâches : 0,04 à 0,08 (le « ≈ 0,07 » du texte est la valeur haute, celle de R3).
- **Valeurs citées dans le texte** vérifiées : V moyen de R2 0,1220 (δ 1,4) et 0,0648 (δ 1,6) ; corrélations entre budgets 0,453 (R3 − R2) et 0,201 (R0 − R2) ; estimations et erreurs-types des quatre contrastes primaires.
- **TR1 est réel dans les deux sens.** Avec s_rép ≈ s_orig, TR1 se déclenche si la réplication de R3 − R2 sort de [0,0845 ; 0,1245] (δ 1,4) ou de [0,1085 ; 0,1387] (δ 1,6), ou si celle de R0 − R2 sort de [−0,013 ; +0,018] (δ 1,4) ou de [−0,010 ; +0,017] (δ 1,6) : un résultat plus beau que l'original déclenche exactement comme un plus faible.

### 4.4 Fidélité (point D)

- La commande de l'étape 5 reprend les options du CLI de v2 (`decision`, `--prereg`, `--instances`, `--run-id`, `--lambda`, `--reference`, `--processus`) et celles de la commande consignée au manifeste original ; le motif d'identifiant de run est respecté ; l'arbre propre est exigé par `etat_git` (`git status --porcelain --untracked-files=all`).
- La sérialisation C10 est faisable : `phase_finale(nom, dfin, ctx, etat, leger=False, rendre_attaques=False)` existe dans l'arène v4 (`70c77fd5…`) avec l'option citée.
- Les racines passent comme entiers Python jusqu'à `SeedSequence(entropy=int(racine), …)` dans `gen_regles` : je n'ai trouvé aucun passage par un entier signé de 64 bits dans v2 ni dans la partie employée de v4. Le manifeste accepte les entiers de 64 bits. E10 (CL-06) garde son intérêt : il exerce `_travail` et `main`, que rien ne teste.
- Le code v3 (apparu à 22:25 heure locale) et son fichier d'essais ne sont **pas lus** (voir § 5).

## 5. Ce que je n'ai pas pu vérifier, ou pas voulu lire

- **Le code v3 et ses essais** (`…/convergence-replication-v1/code/`) : écrits en ce moment par un autre sous-agent, hors de ma liste. CL-06 est donc une exigence sur ces pièces, à vérifier lors de la contre-lecture 2 ; je ne certifie ni C1 à C12 ni E1 à E10.
- **L'implémentation B** (`implementation-b/`) : en cours, non lue, pour ne pas être influencé et ne pas la perturber. CL-07 en est une exigence.
- **Les calculs du jeu** : je n'ai rejoué aucune tâche ; je n'ai donc pas vérifié l'égalité au bit de v2 avec les résultats originaux sur cette machine (c'est l'objet d'E6).
- **`pids-travail.txt` de la course originale** : lu sur la branche, non cité par empreinte dans le brouillon.
- **Le texte « ≈ 28 min »** : valeur de la course originale ; non mesurée ici, la machine étant chargée.
- Mes scripts de contrôle sont dans le dossier temporaire de la session, hors du dépôt ; seul le script de l'annexe est reproduit ici.

## Annexe — contrôle de puissance (script du contre-lecteur)

Relit `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` (empreinte vérifiée), n'écrit aucun fichier, graine `SeedSequence(2718)` sans lien avec la course. Lancé avec `python -I script.py chemin-du-json`. Sortie obtenue :

```text
niveau 1 {'HRep1 repliquee': 1.0, 'HRep0 repliquee': 0.903, 'HRep0 non repliquee': 0.0, 'HRep0 non jugeable': 0.097}
niveau 2 {'HRep1 repliquee': 1.0, 'HRep0 repliquee': 0.819, 'HRep0 non repliquee': 0.01, 'HRep0 non jugeable': 0.171}
```

```python
import hashlib, json, sys
import numpy as np

CHEMIN = sys.argv[1]
ATTENDU = "d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b"
octets = open(CHEMIN, "rb").read()
assert hashlib.sha256(octets).hexdigest() == ATTENDU, "empreinte inattendue"
taches = json.loads(octets)["resultat"]["resultats"]

def vec(c, k):
    t = sorted((t for t in taches if t["code_delta"] == c), key=lambda t: t["instance"])
    assert [x["instance"] for x in t] == list(range(100))
    return np.array([x["regles"][k]["V_iii_final"] for x in t])

d0 = {c: vec(c, "R0") - vec(c, "R2") for c in (1, 2)}   # R0 - R2
d3 = {c: vec(c, "R3") - vec(c, "R2") for c in (1, 2)}   # R3 - R2
M, TAU, Z2, Z8 = 0.02, 0.05, 2.497705474412374, 2.734368786533176
rng = np.random.default_rng(np.random.SeedSequence(2718))

def classe_b(est, se):   # Table B : 1 R0>R2, 2 R2>R0, 3 ≈, 4 R0≳R2, 5 R2≳R0, 6 ?
    b8l, b8h, el, eh = est - Z8 * se, est + Z8 * se, est - Z2 * se, est + Z2 * se
    cls = np.full(est.shape, 6)
    for k, cond in ((5, b8h < 0), (4, b8l > 0), (3, (el > -M) & (eh < M)), (2, b8h < -M), (1, b8l > M)):
        cls = np.where(cond, k, cls)
    return cls

def une(niveau, R=20000):
    i1 = rng.integers(0, 100, size=(R, 100)) if niveau == 2 else np.tile(np.arange(100), (R, 1))
    i2 = rng.integers(0, 100, size=(R, 100))
    cl, ok1 = [], []
    for c in (1, 2):
        s0 = np.take_along_axis(d0[c][i1], i2, axis=1)
        cl.append(classe_b(s0.mean(1), s0.std(1, ddof=1) / 10.0))
        s3 = np.take_along_axis(d3[c][i1], i2, axis=1)
        est, se = s3.mean(1), s3.std(1, ddof=1) / 10.0
        ok1.append((est >= TAU) & (est - Z2 * se > 0))
    nr = np.isin(cl[0], (2, 5)) | np.isin(cl[1], (2, 5))
    rep = np.isin(cl[0], (1, 3, 4)) & np.isin(cl[1], (1, 3, 4))
    return {"HRep1 repliquee": float((ok1[0] & ok1[1]).mean()),
            "HRep0 repliquee": float(rep.mean()), "HRep0 non repliquee": float(nr.mean()),
            "HRep0 non jugeable": float(1 - rep.mean() - nr.mean())}

for niveau in (1, 2):
    print("niveau", niveau, {k: round(v, 3) for k, v in une(niveau).items()})
```
