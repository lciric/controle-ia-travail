# Rapport du rédacteur — mandat de l'auteur des mondes plantés v2 et son devis v2 (course « seuil et moniteurs ») — v2

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Je n'ai écrit ni le mandat v1 ni sa contre-lecture. Écrit le 2026-11-21 ; relevés de `date -u` : 08:16:09Z au début, 08:18:24Z au devis.
- Version : la v2 remplace le rapport v1 (`a38468b487833023a88f1817bccd2f82897487fa9da54b25020f4cfe9f98468c`, gardé intact) après la contre-lecture `9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5` (« À corriger »).
- Statut : pièce de travail (classe C). **Le mandat v2 et le devis v2 attendent la vérification de leurs corrections par le même contre-lecteur** (mot de la mère, 08:12Z). Aucun appel, aucune dépense, aucune clé lue, aucune écriture dans un dépôt, aucun commit. Aucune branche de quarantaine ni de matière première ouverte, aucune source de la liste scellée. Aucun refus de permission, de classifieur ni de garde.
- Mon mandat : `docs/notes/ideation-seuil-moniteurs-v1/mandat-redacteur-mandat-mondes-plantes-v2-v1.md` (`20d6877b22a7d34a188651c6aa7100f8b345d74c8e7979cd3b1fddeb7ea8625a`, égal à son compagnon).

## 0. Verdict

1. **Le mandat de l'auteur v2 est écrit** : les 22 remplacements du contre-lecteur sont jugés un par un ; **19 adoptés tels quels, 3 corrigés dans leur lettre (n° 6, n° 8, n° 21), 3 ajoutés** (§ 2). Vingt-cinq remplacements appliqués par l'outil à ancres comptées, sans refus. 27 310 octets.
2. **Ma sortie n'est donc pas égale à l'essai du contre-lecteur** (`cmp` : différence dès la ligne 1), et c'est attendu. **Contrôle** : son jeu, rejoué tel quel sur la même copie, rend son essai à l'octet (`cmp` muet, `58a69c74…`). L'écart entre son essai et mon mandat tient en six lignes, toutes voulues (§ 2.3).
3. **Les quatre défauts de fond et l'alignement sur la conception v5 sont tous portés** (§ 3).
4. **Le devis v2 porte les trois retouches.** Le plafond reste à 4,26 USD, deux essais au plus à 2,13 ; le cas haut de R2-a passe de 3,51 à 4,24. Avec la course : 118,74 sous 120.
5. **Deux réserves de fond que je n'ai pas tranchées seul** : le sort attendu d'un témoin « doit tenir » identique à la base, et le témoin du quantile (§ 5, D-M16 et D-M17).

## 1. Pièces lues

Chaque empreinte est recalculée par moi ; « compagnon » : égale au fichier `.sha256` d'origine, lu ou cité par la contre-lecture.

Sur le disque de la branche de l'organisme, dossier `docs/notes/ideation-seuil-moniteurs-v1/` :

| pièce | chemin | empreinte | lecture |
|---|---|---|---|
| mon mandat | `mandat-redacteur-mandat-mondes-plantes-v2-v1.md` | `20d6877b22a7d34a188651c6aa7100f8b345d74c8e7979cd3b1fddeb7ea8625a` (compagnon) | en entier |
| mandat de l'auteur v1 | `mandat-mondes-plantes-v1/mandat-auteur-mondes-plantes-seuil-et-moniteurs-v1.md` | `6774507cbf149235d86e0c460aae339585956bca5b23db992a85d3121ca3c1b9` | en entier |
| devis v1 | `mandat-mondes-plantes-v1/devis-auteur-mondes-plantes-v1.md` | `4f5dca99a527586228480fe629269fe29a37ecb13b7ab93e4c01c4b3f43409ae` | en entier |
| programme du devis v1 | `mandat-mondes-plantes-v1/calcul_devis_auteur_mondes_plantes_v1.py` | `d715bcf2ed522737934f8a38994e27997e25f46874c4db96058e3c6090f00385` | en entier |
| sortie du devis v1 | `mandat-mondes-plantes-v1/calcul-devis-auteur-mondes-plantes-v1.json` | `fb467010bb47ab2ef36a5b32f6caf0aea91bb61d08229e7df1f480f268715123` | empreinte seule |
| rapport v1 | `mandat-mondes-plantes-v1/rapport-redacteur-mandat-mondes-plantes-v1.md` | `a38468b487833023a88f1817bccd2f82897487fa9da54b25020f4cfe9f98468c` | en entier |
| table d'empreintes v1 | `mandat-mondes-plantes-v1/table-empreintes-mandat-mondes-plantes-v1.txt` | `59c16ef4147d697a80e397da41c8598b6251c4f8fa056beae193d12d00092ab2` | en entier ; ses cinq lignes sont égales aux cinq empreintes ci-dessus |
| contre-lecture | `mandat-mondes-plantes-v1/contre-lecture-v1/contre-lecture-mandat-mondes-plantes-v1.md` | `9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5` | en entier |
| jeu de 22 remplacements | `mandat-mondes-plantes-v1/contre-lecture-v1/remplacements-mandat-auteur-mondes-plantes-v1-vers-v2.json` | `73c642b45813452bff4323c592e851c952df2df8b48da5dc97fb011fc67b1ac6` | en entier |
| essai sur copie | `mandat-mondes-plantes-v1/contre-lecture-v1/essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v2.md` | `58a69c74cdb020308074d96e67b16445161d800f9a124bd1f0761ee134335efa` | en entier |
| ordre de course v5 | `conception-v5/ordre-course-seuil-et-moniteurs-v5.md` | `8712ddd08dc1cefb72115b67f44338e84cbf45b9244b602cbaed73076a3b8f24` | en entier |
| ordre de course v6 | `conception-v6/ordre-course-seuil-et-moniteurs-v6.md` | `208454c500c455a490f7ba7c23b3f98d9352f2efe474bf99453d4bc2d053b940` (compagnon) | ligne de version, champ `portee_de_la_garantie` (§ 3, § 4) |

Sur `origin/main`, par `git show` redirigé après `fetch`, commit `aea06e6383b1a5ebb6936170e8b29b5faaa83e16` :

| pièce | chemin | empreinte | lecture |
|---|---|---|---|
| outil de remplacement à ancres comptées | `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | en entier |
| registre des décisions | `registres/decisions.md` | `0d1f19d10e3f6c447166166a5c9098fb9b66a5ac88ef3df1bcfa35f1febd29ec` | R-4416, R-4430 à R-4442 |
| registre des accords | `registres/go.md` | `ec9baf4f0651c831c64cacef408027e179e96ea547133bb32de22be24f51be3d` | GO-2026-11-21-16 |
| scellement de la conception | `prereg/ideation-seuil-moniteurs-v1/scellement-conception-course-seuil-et-moniteurs-v1.md` | `4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07` | la phrase de sa ligne 10 |
| programme de calcul de la note de conception | `docs/notes/experimentateurs-et-tests-de-mort-v1/calculs-conception-tests-de-mort-v1.py` | `301c0f52fc11c7a7bc9de2292b51f56b314277fda72402fc7c76b33323fdb857` | par recherche de motifs seulement : le sens du test répété (sa ligne 152). Aucune valeur lue, sa sortie non ouverte |

Mes copies de lecture sont sous `lecture/` et sont **exclues du versement**.

**Non lu.** Les notes de conception, la synthèse du collisionneur, le registre servi des visées, le préenregistrement court v5 et v6, le reste de l'ordre v6, la table du collisionneur : je m'appuie pour eux sur le rapport v1 et sur la contre-lecture, qui les ont lus.

## 2. Les 22 remplacements, jugés un par un

### 2.1 Adoptés tels quels : dix-neuf

| n° | objet | mon jugement |
|---|---|---|
| 1 | en-tête : retire le nom du rédacteur et « non contre-lue » | juste : le texte part scellé |
| 2 | tailles 200, 300 ou 400 | égal à la v5, § 7 bis |
| 3 | `population_de_calibration` et `portee_de_la_garantie`, deux valeurs | égal au champ de la v5 et de la v6 (§ 3) ; la troisième valeur de la fiche, « non dite », ne sert pas à un témoin |
| 4 | calcul « scellé avant la lecture » ; témoins imposés sans supposition ; portée par défaut | juste ; T14, T16 et T17 sont bien les trois témoins à portée conditionnelle, T15 se lit sur tous |
| 5 | T09 ne déclare aucune supposition | juste : sous la définition du § 2, il déclare alors tenir sur la famille F et peut mourir |
| 7 | T13 : rapport de vraisemblance de 0,30 contre 0,20, alerte à 100 ou plus | sort unique ; ce sont des paramètres du monde S, aucune valeur vraie |
| 9 | famille H : variance 1, familles neuves en usage, « épisodes honnêtes échangeables » | égal à la v5 et à la décision D-M13 |
| 10 | « Vérité exacte : une exigence » | porte la règle de la v5 et le mot de la mère de 07:56Z |
| 11 | témoins du monde M, dont celui à portée conditionnelle au réglage γ = 0 | égal au témoin que la v5 propose à l'auteur |
| 12, 13 | deux familles libres au plus, retenues au scellement | juste |
| 14, 15 | deux lignes d'orientation retirées | la v5 dit ces visées hors des mondes de la course |
| 16 | objets à clés libres nommés | juste |
| 17 | clés `portee_de_la_garantie` et `signal` | juste |
| 18 | `valeurs_de_plus` pour T05 et T07 | juste, et nécessaire à ma correction du n° 8 |
| 19 | `verite.mode` : `exacte` seulement | juste |
| 20 | alerte strictement au-dessus du seuil | juste |
| 22 | témoins du monde M exigés ; un monde écarté n'est pas une sortie illisible | juste ; repris au devis v2, § 3 |

### 2.2 Corrigés dans leur lettre : trois

| n° | lettre du contre-lecteur | défaut que j'y vois | ma lettre |
|---|---|---|---|
| 6 | T12 : « test binomial exact unilatéral […] alerte dès que sa valeur p est strictement sous 0,01 » | « unilatéral » ne dit pas de quel côté : le sort n'est pas encore unique. Le programme de la note prend la queue haute (probabilité d'un compte au moins égal au compte observé) | « unilatéral à droite », et la valeur p définie par cette phrase |
| 21 | la même définition, dans la grammaire de `test_repete_sans_correction` | le même | la même précision |
| 8 | T05 et T07 : « leur puissance et leur écart de puissance à la base, et tiens-en compte dans `issue_attendue` » | trois manques. (a) La puissance dépend de la taille du signal : laquelle ? (b) T07 se joue à n = 200 et à n = 400, mais un témoin n'a qu'un `n` et qu'une `valeur_vraie` : deux taux moyens pour un seul champ. (c) « Tiens-en compte » ne dit pas comment : le mandat ne définit nulle part l'issue `morte_sans_gain`, et l'auteur écrirait « tient » pour la base jouée contre elle-même, ce que la v5 interdit | (a) « à chacune des trois tailles de signal » ; (b) `n` vaut 200, `valeur_vraie` est le taux moyen à n = 200, celui à n = 400 va dans `valeurs_de_plus` ; (c) si la garantie de T05 ou de T07 tient et que l'écart à la base n'est pas strictement positif, l'issue est `morte_sans_gain` et la sorte `doit_mourir` ; pour les autres témoins imposés, `issue_attendue` ne dit que la tenue de la garantie dite |

La phrase (c) est conditionnelle : elle ne donne à l'auteur ni valeur vraie ni sort tout fait, il calcule encore la garantie et l'écart (décision D-M12 tenue). Elle n'écrit ni seuil d'épreuve, ni niveau, ni nombre de tirages : elle porte sur l'écart vrai, non sur un test.

### 2.3 Ajoutés : trois

| n° | où | quoi | pourquoi |
|---|---|---|---|
| 23 | § 6, point 4 | « comparés à notre calcul scellé » devient « comparés à notre calcul, fait par un programme scellé avant la lecture de ta sortie » | le défaut « notre calcul scellé » restait une fois dans l'essai ; mon mandat demande qu'il soit porté en entier |
| 24 | titre | « v1 » devient « v2 » | le fichier est la v2 (règle R12) ; l'essai gardait « v1 » en titre |
| 25 | § 5, premier tiret | « sous les définitions du § 2 » devient « du § 2 et du § 3.1 » | accord avec ma correction du n° 8, qui définit `morte_sans_gain` au § 3.1 |

**Écart entre l'essai et mon mandat v2** (`diff -u`, au différentiel `differentiel-essai-du-contre-lecteur-vers-mandat-v2.diff`) : six lignes changées, une par objet — le titre, T12, le paragraphe de T05 et T07, la grammaire, le § 5, le § 6 point 4. Rien d'autre.

**Laissé tel quel, à dessein.** `version_forme` garde la valeur `mondes-plantes-seuil-et-moniteurs-v1` : aucune sortie n'a été rendue sous le mandat v1, c'est la première forme jouée. Les mots « population de lecture » restent une fois en prose (§ 3.1, dernière phrase) : ce n'est plus un nom de champ, la phrase se lit sans lui.

## 3. Ce que le mandat v2 porte, et où

| exigence de mon mandat | où dans le mandat v2 | remplacement |
|---|---|---|
| défaut de fond : T09 inversé | table des témoins, ligne T09 ; règle générale du § 3.1 | n° 5, n° 4 |
| défaut de fond : T08 sans sort unique | § 4.3, convention du quantile | n° 21 |
| défaut de fond : T12 sans sort unique | ligne T12 ; § 4.3 | n° 6 et n° 21, corrigés |
| défaut de fond : T13 sans sort unique | ligne T13 | n° 7 |
| défaut de fond : « notre calcul scellé » | § 3.1 ; § 6, point 4 | n° 4 ; n° 23, ajouté |
| défaut de fond : « non contre-lue » | en-tête | n° 1 |
| vérité exacte | § 3.2, « Vérité exacte : une exigence » ; § 4.2, `verite.mode` | n° 10, n° 19 |
| ce qui écarte un monde | § 3.2 ; § 6, point 2 | n° 10, n° 22 |
| familles C, D, E et G | § 3.2, la même exigence | n° 10 |
| témoins du monde M | § 3.3 ; § 4.2, clé `signal` ; § 6, point 2 | n° 11, n° 17, n° 22 |
| famille H, « échangeables » | § 3.2, ligne H | n° 9 |
| `portee_de_la_garantie` | § 2 ; § 3.1 ; § 4.2 | n° 3, n° 4, n° 17 |
| familles libres, deux au plus | § 3.4 | n° 12 à n° 15 |
| tailles 200, 300 et 400 | § 2 | n° 2 |
| T07, la base jouée contre elle-même | § 3.1 ; § 4.2 | n° 8, corrigé ; n° 18 |

Aucune correction ne va vers la conception v5 ou v6.

## 4. Le choix du relais

Inchangé : le deuxième relais, candidat R2-a, confiance 0,6. Le contre-lecteur le juge « acceptable » (son § 7). Une raison du rapport v1 tombe : « le plafond nominal de R2-a contient la sortie » ne vaut que si la provision de réflexion ne se compte pas dans le plafond ; le premier essai part donc à 32 000 jetons (devis v2, § 2). Une raison s'ajoute : le mandat v2 réduit les familles libres à deux, ce qui laisse moins de prise à une habitude de lignée.

## 5. Décisions

### Closes par les mots de la mère

| décision | objet | comment elle est close |
|---|---|---|
| D-M11 | la population sur laquelle une garantie est lue | **close** (07:57Z, R-4433) : un seul champ, `portee_de_la_garantie`, celui de la conception v5. Porté au mandat v2 (n° 3, n° 4, n° 17) |
| D-M12 | les valeurs vraies de la note ne sont pas servies à l'auteur | **close** (07:57Z), selon la recommandation (a). Le mandat v2 ne sert aucune valeur vraie |
| D-M13 | la supposition que cassent les grappes | **close** (07:57Z), option (a) : « épisodes honnêtes échangeables », écrit dans la table des familles (n° 9) |
| D-M14 | le partage des témoins | **close** (07:57Z), option (a) : l'auteur écrit ceux des mondes, la mère garde ceux de l'étage et de la mise en fiches |
| D-M15 | contre-lecture avant envoi | **close** (07:57Z), option (a) : la contre-lecture est rendue (`9ea0ab89…`) ; la vérification des corrections par le même contre-lecteur est accordée (08:12Z) et reste à faire |

Le mot de 07:56Z (R-4432) y ajoute : le monde à trois populations et un monde parmi C, D, E et G sont exigés du mandat, s'ils ont une vérité exacte et des témoins ; la pièce la plus stricte gagne.

### Pour la mère, restantes

**D-M16 — Le sort attendu d'un témoin « doit tenir » qui est la base elle-même.**
- Décision en une phrase : dire si `issue_attendue` d'un témoin imposé se lit sur la seule garantie dite, ou sur la classe d'issue entière.
- Enjeu : T02, T15 et T16 ont pour règle « le plus grand score », qui est la base, et le contre-lecteur dit que leur garantie tient (son § 5). Leur écart de puissance à la base est nul. Lus sur la classe entière, ils sortiraient « sans gain », alors que la banque de la v5 dit « le plus grand score de 299, certifié à 95 % » : « doit tenir : garantie tenue ».
- (a) Sur la seule garantie dite, sauf T05 et T07 (lettre de mon n° 8). Avantage : égal à la banque de la v5, où seuls « ne jamais alerter » et « la base contre elle-même » meurent sans gain. Inconvénient : deux lectures d'un même champ selon le témoin.
- (b) Sur la classe entière pour tous. Avantage : une seule lecture. Inconvénient : un témoin « doit tenir » de la banque de la v5 changerait de sorte ; ce serait une correction vers la v5, que la règle de la mère exclut.
- Recommandation : (a), confiance 0,7. Défaut sous 48 heures : (a).

**D-M17 — Garder ou retirer le témoin du quantile empirique (T08).**
- Décision en une phrase : garder T08 avec la convention du n° 21, ou le retirer comme la v5 l'a retiré de l'étage.
- Enjeu : la contre-lecture laisse ce choix à la mère (sa table, ligne 14).
- (a) Le garder. Avantage : son sort est maintenant unique ; il éprouve la convention du quantile. Inconvénient : un témoin de plus à calculer chez nous.
- (b) Le retirer. Avantage : égal à l'étage de la v5. Inconvénient : seize témoins imposés ; le texte du mandat change encore.
- Recommandation : (a), confiance 0,6. Défaut sous 48 heures : (a).

**D-M18 — Garder deux familles libres, ou aucune.**
- Décision en une phrase : laisser à l'auteur deux familles de son choix, ou les retirer toutes.
- Enjeu : la contre-lecture dit que la mère « peut aller plus loin » (sa table, ligne 10) ; ce sont elles qui donnent le plus de prise à une habitude de lignée.
- (a) Deux au plus, retenues seulement au scellement (mandat v2). Avantage : une idée de monde que nous n'avons pas eue peut entrer ; la mère garde la main. Inconvénient : de la place de sortie prise aux blocs imposés.
- (b) Aucune. Avantage : aucune prise ; plus de place. Inconvénient : les mondes ne sont que les nôtres.
- Recommandation : (a), confiance 0,6. Défaut sous 48 heures : (a).

### Pour Lazar

**D-L1 — La ligne de calcul de l'auteur des mondes, avec son exception.**
- Décision en une phrase : accorder, ou non, 4,26 USD pour un appel au deuxième relais, deux essais au plus, par exception écrite à la phrase « Aucune dépense avant ce scellement » du scellement de la conception (`4286bf39…`).
- Enjeu : sans mondes scellés, la course ne part pas ; et le préenregistrement court, que cette phrase attend, attend lui-même les mondes. Avec le devis de la course (114,48), le total est 118,74, sous le plafond indicatif de 120.
- (a) R2-a, 4,26. Avantage : tarif lu sur page versée. Inconvénient : le plafond le plus haut ; premier essai à 32 000 jetons.
- (b) R2-b, 4,04. Avantage : la plus grande provision de réflexion. Inconvénient : tarif et réglages à relever.
- (c) R3, 3,44. Avantage : le moins cher ; la lignée qui a le moins de textes en jeu. Inconvénient : tarif à relever, plafond nominal trop court.
- Recommandation : (a), confiance 0,6. **Aucun défaut : c'est une dépense, et une exception à un texte scellé.**

**D-L2 — Le modèle de l'expérimentateur fixe le relais de l'auteur (nœud N4 de la note de conception).** Mise à jour.
- Décision en une phrase : nommer le modèle de l'expérimentateur d'épreuve, avant la ligne de l'auteur.
- État : la mère recommande le premier relais pour l'expérimentateur ; ce n'est pas accordé (contre-lecture, § 7 et § 8 ; R-4432 : « N4 bloque D-M9 : à Lazar » ; R-4433 : « N4 d'abord »).
- Enjeu : si l'expérimentateur était du deuxième relais, l'auteur des mondes ne pourrait pas en être ; l'appel serait à refaire ailleurs.
- (a) Accorder le premier relais à l'expérimentateur. Avantage : l'affectation tient d'un coup — un traducteur au premier relais, l'auteur au deuxième, le second traducteur au troisième. Inconvénient : fixe le modèle de l'expérimentateur avant la mesure de son coût sur les seuls témoins.
- (b) Un autre relais pour l'expérimentateur. Avantage : garde le choix ouvert. Inconvénient : le relais de l'auteur est à rechoisir, et le devis à rejouer pour ce relais.
- Recommandation : (a), puis D-L1 ; confiance 0,6. **Aucun défaut : changer de modèle demande ton mot, et D-L1 est une dépense.**

## 6. Calendrier : deux lignes à ajouter, en sessions, sans dollar

| étape | quand | sessions |
|---|---|---|
| **le programme de vérification de la sortie de l'auteur** : forme, complétude, cohérence et motifs (mandat v2, § 6, points 1 à 3 et 5), avec ses essais sur un cas sain et sur un artefact (règle R5) ; contre-lu | **avant l'envoi** : c'est lui, et non une main, qui dit une sortie « illisible », donc qui décide d'un second essai payé | une |
| **le programme scellé qui calcule la vérité des dix-sept témoins imposés**, paramétré par la loi que l'auteur écrira ; contre-lu, scellé | **avant la lecture de la sortie** (règles R1 et R4) ; c'est la promesse du mandat v2, § 3.1 et § 6, point 4 | une, la même si possible |

Le recalcul de toutes les autres valeurs (mandat v2, § 6, point 4) peut suivre l'envoi ; il précède la lecture. Ni le rapport v1 ni le § 10 de la conception v5 ne portaient ces lignes.

## 7. Réserves

1. **Mes trois corrections de lettre et mes trois ajouts ne sont pas contre-lus.** Le contre-lecteur les verra au différentiel.
2. Je n'ai vérifié par le calcul aucune valeur vraie : c'est voulu (D-M12). Que la famille I approche la borne à 0,001 près est une demande faite à l'auteur ; le contre-lecteur l'a jugée faisable (son § 5).
3. La règle « quatre décimales au moins » ne se vérifie que sur le texte brut de la sortie (remarque 1 de la contre-lecture) : à porter au programme de vérification.
4. La borne de 40 000 caractères reste serrée ; le mandat dit quoi réduire d'abord.
5. Le compte des caractères du mandat v2 est son compte d'octets, qui le majore.
6. Pour T09 à T11, notre valeur se calcule sous la loi que l'auteur choisit (remarque 2 de la contre-lecture) : le programme de vérité des témoins doit être paramétré, non écrit pour la seule loi normale.
7. L'empreinte de la table du collisionneur n'est pas recalculée par moi ; je la tiens du rapport v1 et de la contre-lecture.
8. Aucun refus de permission, de classifieur ou de garde pendant ce travail.

rédacteur du mandat des mondes plantés v2, modèle F
