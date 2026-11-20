# Contre-lecture — préenregistrement court de la course « nouvelles attaques » — v1

- Contre-lecteur neuf, modèle O (règle R2). Je n'ai écrit ni ce préenregistrement, ni la conception de la course. Écrit le 2026-11-20 ; relevé de `date -u` : 05:22:39Z, après les vérifications et avant l'écriture.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucune valeur de clé, aucune écriture dans le dépôt, aucun commit. Réseau : deux `git fetch` (`main` ; la branche `claude/pensive-bardeen-1fv7hw`, nommée par GO-2026-11-19-34). Rien ouvert sous `archives-reponses-modeles/` ni dans le coffre. **Aucun refus de permission, de classifieur ni de garde.**
- Deux mots reçus en cours de lecture, pris en compte : GO-2026-11-20-16 (R-4092), qui tranche N1 ; et deux précisions de la mère (séparation du proposeur et du juge de l'espèce 3 ; recherche du besoin du bras A sur Rigaud par chemins nommés).

## 0. Verdict

**Conforme après corrections.**

- Le texte suit le § 12 de l'ordre et le gabarit. Il ne contient aucune recette, aucun identifiant de modèle, aucune prédiction inventée.
- Les quatre coûts par rôle sont justes à un centime près. Ma recherche exhaustive les a confirmés.
- Deux points de fond sont à corriger avant le scellement :
  1. **La répartition par clé n'est pas celle qu'annonce sa propre règle.** Il existe des répartitions dont le plus petit rapport « solde / cas haut » est plus grand (§ 4).
  2. **La période de recherche d'antériorité commence en 2016.** Cette borne pousse vers « inédite » (règle R8 ; § 3).
- La branche « recharge » tombe : GO-2026-11-20-16 tranche N1.
- Les gardes n° 11 et n° 12, telles qu'écrites, ne s'éprouvent pas vraiment sur un artefact (règle R5). Je donne leur texte corrigé.

Les corrections sont au § 8, à appliquer par un rédacteur de modèle F. Une pièce déjà empreintée ne s'écrase pas (règle R12). Elles s'appliquent donc à des **v2** : `preenregistrement-court-course-nouvelles-attaques-v2.md` et `rapport-redacteur-preenregistrement-court-nouvelles-attaques-v2.md`. Les v1 restent archivées, sans modification.

## 1. Empreintes

Chaque empreinte est recalculée. Elle est égale à son compagnon `.sha256`, ou à la valeur que cite la pièce qui la nomme :

| pièce | empreinte | contrôle |
|---|---|---|
| `NA/preenregistrement-court-v1/preenregistrement-court-course-nouvelles-attaques-v1.md` | `0f0d8b9b4c42b56c2e8928b283ca655f4cd88c9fe1529a0debabaaba94979507` | compagnon : égal |
| `NA/preenregistrement-court-v1/rapport-redacteur-preenregistrement-court-nouvelles-attaques-v1.md` | `057b3a4c3e5e87226b0fa922390fef447ca890b83c912388bb3c12ad58390a09` | compagnon : égal |
| `NA/conception-v3/mandat-redacteur-preenregistrement-court-nouvelles-attaques-v1.md` | `750ba73342670fbb8b163da7db35e85d8ad051d0b23f1576e8031f4c801ed7d0` | compagnon : égal |
| `NA/conception-v3/question-course-nouvelles-attaques-v3.md` | `2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b` | compagnon : égal |
| `NA/conception-v3/ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` | compagnon : égal |
| `NA/conception-v3/rapport-redacteur-conception-nouvelles-attaques-v3.md` | `6c28636ce07f73b018e7746cb78a03672a224995ad0aff0d7602a6498174ee98` | compagnon : égal |
| `NA/conception-v2/devis-course-nouvelles-attaques-v2.md` | `714e4fc6a9a292626022adac4a5ddcc4f3e16fd14f81629b6b8a98cf89fcf028` | compagnon : égal |
| `NA/conception-v2/calcul-devis-course-nouvelles-attaques-v2.json` | `ffecbd1172888b815e6f7af84ae54f52c1991554d6d2ff376481af694e60b7cf` | égale à celle que cite le devis |
| `NA/conception-v3/controle-differentiel-conception-nouvelles-attaques-v2-v3-v1.md` | `6fd50296fc7c674b516daa2c2895a96c42ccb775ac2de0b7a5d855a5736cbd5e` | compagnon : égal |
| `NA/mandat-redacteur-conception-course-nouvelles-attaques-v1.md` | `8fd94f6f78e51665eccfd2bc11c634f7bce207f9ed70d237e464e2d9b3eda294` | égale à celle que cite la question |
| `NA/complement-1-mandat-redacteur-conception-course-nouvelles-attaques-v1.md` | `226ea15243c947164d4c3595c350d90fea980694f7d4903cf8dac33e56b81fdd` | égale à celle que cite la question |
| `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` | égale à celle du texte |
| `CLAUDE.md` | `c9d86f7366aa0108d922f167032e2226505d6ad08ef8d5bb8e8c21416fe2768c` | égale à celle du rapport |
| `registres/go.md` au commit `8cf0d3d1…` (cité par le texte) | `8639e38fea4708c2f843202b1bb26fe0321381d9792e79bbdb853fcd3d288024` | égale à celle du texte |
| `registres/decisions.md` au même commit | `f45e63331edbb756fe5519ac9a763965cb1f7058c37225ae962d222c38032903` | égale à celle du texte |
| `registres/go.md` sur `main` relu, commit `0b265f658bdfd3dda8bc432a1f05f2f15766d2e6` | `faa6bd5175a6639a944485b6ab6112b938dabb7e8cbd47fca22e5aa8a31f9a4b` | porte en plus GO-2026-11-20-15 et -16 |
| `registres/decisions.md` sur `main`, même commit | `8c8bded74eb12a3be69929f73c79ddd26c14f3e8d92fd3432794ac86b0af228b` | porte en plus R-4090 à R-4093 |
| devis de l'essai de mesure du bras A, brouillon 3 (`docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, commit `de052f27`) | `533ad5b15e6de1bdfe81c35f8501dbad376f52f907be84094c3fd8621b349592` | égale à celle de GO-2026-11-19-34 |

NA = `docs/notes/ideation-nouvelles-attaques-v1/`. Les extraits de registre sont gardés dans le sous-dossier `lectures/` de mon dossier. Ce ne sont pas des pièces rendues.

Lignes lues sur `main` :
- accords : GO-2026-11-20-05, -08, -10, -12, -13, -14, -16, et GO-2026-11-19-31, -32, -34 ;
- décisions : R-607, R-609, R-611, R-3237, R-3611, R-3647, R-3707 à R-3709, R-3804, R-4082, R-4084, R-4086 à R-4089, R-4091 à R-4093.

## 2. Le § 12 et le gabarit (point 1)

- **Les huit sections du gabarit sont présentes et remplies.** J'ai lu le validateur `src/controle_ia/prereg.py` : il exige « au moins » ces sections. La section en plus, « Ce qui reste à écrire avant l'allumage », ne gêne donc pas le scellement. La section « Contre-lecture » devra citer deux empreintes : le brouillon relu et ce rapport.
- **Tout ce que le § 12 demande est là** : la question par chemin et empreinte ; K = 3 ; la composition ; le tirage et la famille tenue à l'écart ; ce qui est servi (D2 (a)) ; les mesures, dites descriptives, avec les comptes « hors case » du contrôle (§ 3) ; la règle d'antériorité et son périmètre ; les gardes ; les plafonds. Les deux paires d'issues sont écrites au même rang.
- **Rien n'est gelé qui ne soit décidé** : les valeurs de conception sont gelées sous des accords nommés (D1, D2, D4, D5, D6 par GO-2026-11-20-10). Les valeurs propres du rédacteur sont marquées comme telles. Les valeurs ouvertes ont chacune leur règle et leur moment.
- Deux points sont dépassés depuis l'écriture :
  - la branche, tranchée par GO-2026-11-20-16 ;
  - la sonde de Luc et la présence de Rigaud par son nom, faites ou constatées (R-4091).

  Corrections K1, K7, K8, K16, K22 et K24.
- Écart mineur : le commit du code d'analyse est « aucun ». C'est admissible, puisqu'il se porte au complément, scellé avant tout allumage.

## 3. Aucune recette, aucune prédiction inventée, valeurs du rédacteur (points 2, 3 et 7)

**Aucune recette.** Le texte ne nomme même pas les valeurs des axes : il les numérote. Il ne contient aucun procédé, aucune étape, aucun détail opérant.

**Aucun identifiant de modèle.** Une recherche sans casse des noms d'espèces, de fournisseurs et de clés de variable ne trouve que deux faux positifs : « Google Scholar », nom d'une base, et `CLAUDE.md`, dans le rapport. Les noms Minuit, Luc et Rigaud sont des noms de clés, non des modèles.

**Aucune prédiction inventée** (règle R3). Le seul chiffre posé d'avance est un coût.

Les valeurs posées par le rédacteur :

| valeur | avis | pourquoi |
|---|---|---|
| racine des graines : 32 premiers caractères hexadécimaux de l'empreinte de la question ; `SeedSequence(entropy=racine, spawn_key=(c,))` | **proposition acceptable, avec une correction (K10)** | La racine est fixée par une empreinte écrite avant toute sortie et ne vise aucun signe. Mais la méthode de tirage n'est pas nommée (`integers`, `choice`, `permutation`). Le développeur du véhicule pourrait donc essayer plusieurs méthodes sur la même graine avant le scellement du tirage. C'est un degré de liberté que la règle R1 ferme. |
| borne de lecture : 60 fiches, témoins non compris | **proposition acceptable** | L'ordre de course (§ 9) la renvoie à ce texte. Elle est tirée par graine, ne dépend d'aucun résultat et ne vise aucun signe. |
| périmètre : bases, classes de requête, trente premiers résultats | **acceptable pour les bases et les classes ; correction de la période et de l'effort (K11, K12)** | Commencer au 1ᵉʳ janvier 2016 laisse dehors l'apprentissage automatique adverse plus ancien (évasion de classifieurs, dérive de distribution). Pour plusieurs valeurs de l'axe « ce que le moniteur suppose », c'est là qu'une antériorité par classe de mécanisme est le plus plausible. La borne pousse donc vers « inédite » : c'est la zone vierge séduisante que la règle R8 demande de vérifier plus durement. De plus, « trente par base et par classe » est ambigu quand une classe porte plusieurs chaînes de requête. |
| audit de symétrie : inédites nulles ou d'au moins la moitié ; M1 égale à 0 ou à 1 ; portier sans coffre ni hors case | **propositions acceptables ; une addition (K13)** | Les trois seuils déclenchent le même audit dans les deux sens. Il en manque un : le sens « trop de hors case ». Le coffre a sa garde, le hors case n'a rien. Je propose le même quart. |
| précision 1 : dénominateur de M1 et compte à part des filiations invalides | **acceptable ; à préciser (K14)** | Une fiche passée par le portier puis envoyée au coffre par la relecture de la mère n'a pas de place dite. Elle ne peut pas être lue par programme dans M1 (règle R-607). |
| précision 2 : une étiquette interdite arrête la génération suivante, sans retrait silencieux | **proposition acceptable** | Elle est conforme à la règle R5. |
| précision 3 : une espèce retirée à la sonde de refus, donc une version neuve | **proposition acceptable** | Elle est plus stricte que l'ordre (§ 11 : « retirée de tous les rôles »), mais conforme au § 8 de l'ordre et à la règle R12 : la composition est figée. La mère peut le confirmer en routine. |

## 4. La répartition par clé, refaite (point 4)

### 4.1 Calcul

Mon programme : `calcul_repartition_cles_v1.py` (`7f7216501e4ad3d843e5cd59ae2ce2fe6fca42d36400ad8f1e2a1d5f016bca25`), dans mon dossier, lancé par son chemin avec la sortie du calcul du devis pour argument (`ffecbd11…`). Sa sortie : `calcul-repartition-cles-v1.json` (`bf423a5e9106b059e76cd50f6a7e3c0f4ac0e8730d4c0b517def0414890a8fdd`). Je l'ai joué deux fois : les deux sorties sont égales à l'octet.

Les entrées :
- les coûts réels de la course v9 par rôle et par génération (devis v2, § 1, clé S1) : proposeur de l'espèce 3, 7,43 ; proposeur de l'espèce 4, 17,58 ; aiguilleur, 4,59 ; juge de l'espèce 3, 6,86. Leur somme, 36,46, rend la part du premier relais de la v9 (devis, § 3 : 36,457056) ;
- les facteurs du haut, pris dans le JSON (`facteurs_du_haut_par_role`) : 1,1940, 4,4575 et 5,1046. Les facteurs exacts, recalculés sur les totaux du JSON, sont 1,194032, 4,457516 et 5,104639, sans écart au centime ;
- le pire d'un appel de proposeur (champ `pire_par_appel_de_proposeur_usd`) : 6,05 ;
- le plafond d'une génération : 150.

**Coûts par rôle du premier relais, sur trois générations (USD)** :

| rôle | bas | haut | pire |
|---|---|---|---|
| proposeur de l'espèce 3 | 22,29 | 26,61 | 199,65 (11 × 6,05 × 3) |
| proposeur de l'espèce 4 | 52,74 | 62,97 | 199,65 |
| aiguilleur | 13,77 | 61,38 | 450 (plafond de génération × 3) |
| juge de l'espèce 3 | 20,58 | 105,05 | 450 |
| somme | 109,38 | **256,01** à la somme des lignes (256,02 sans arrondir les lignes, valeur du texte) | **450 au plus** : les pires ne s'additionnent pas, le plafond de 150 USD tient tous les rôles d'une génération ensemble |

Les chiffres du texte sont justes. Il y a un écart d'un centime sur la somme haute : c'est l'arrondi.

### 4.2 Par clé, cas bas, haut et pire

Soldes : Minuit 162,56 (calculé) ; Luc 214 (déclaré) ; Rigaud 47 (calculé), moins X, le besoin du bras A.

| répartition | clé : rôles | bas | haut | pire | rapport solde / haut | marge au haut (USD) |
|---|---|---|---|---|---|---|
| **du texte** | Minuit : aiguilleur, espèce 4 | 66,51 | 124,35 | 450 | 1,307 | 38,21 |
| | Luc : juge de l'espèce 3 | 20,58 | 105,05 | 450 | 2,037 | 108,95 |
| | Rigaud : proposeur de l'espèce 3 | 22,29 | 26,61 | 199,65 | 1,766 (X = 0) | 20,39 |
| repli du texte (X > 20) | Minuit : aiguilleur, espèces 3 et 4 | 88,80 | 150,96 | 450 | **1,077** | 11,60 |
| | Luc : juge de l'espèce 3 | 20,58 | 105,05 | 450 | 2,037 | 108,95 |
| **meilleure, X ≤ 9,28** | Minuit : juge de l'espèce 3 | 20,58 | 105,05 | 450 | **1,547** | 57,51 |
| | Luc : aiguilleur, espèce 4 | 66,51 | 124,35 | 450 | 1,721 | 89,65 |
| | Rigaud : proposeur de l'espèce 3 | 22,29 | 26,61 | 199,65 | (47 − X) / 26,61 ≥ 1,418 | 20,39 − X |
| **meilleure, X > 9,28** | Minuit : juge de l'espèce 3 | 20,58 | 105,05 | 450 | 1,547 | 57,51 |
| | Luc : aiguilleur, espèces 3 et 4 | 88,80 | 150,96 | 450 | **1,418** | 63,04 |
| | Rigaud : rien | 0 | 0 | 0 | — | 47 − X, laissés au bras A |
| « une espèce entière par clé », la meilleure | Minuit : aiguilleur, espèce 4 ; Luc : espèce 3 entière ; Rigaud : rien | — | 124,35 ; 131,66 | — | **1,307** | 38,21 |

Le pire d'une clé est au plus 450 : c'est le plafond de la course sur le premier relais entier. La somme brute des pires de ses rôles serait de 649,65 ou de 849,30, mais elle ne peut pas être atteinte.

**Ce que cela dit.**
- *Les deux affirmations du texte sur les rapports sont fausses.* Le texte écrit que sa répartition est « celle dont la marge la plus faible est la plus grande ». Elle donne 1,307 ; une autre donne 1,547. Son repli donne 1,077 ; un autre donne 1,418.
- *La meilleure répartition dépend du seul besoin X.* Le point de bascule est X = 9,28 USD : c'est le point où (47 − X) / 26,61 égale 214 / 150,96.
- *La colonne « solde sur cas haut » du texte est un rapport, non une marge en USD.* Il faut le dire (K5).

**Au pire du devis, aucune répartition ne tient chaque part sous son solde.** Le texte le dit sans forcer, et c'est juste. Entre le cas haut et le pire, c'est l'arrêt n° 12 qui tient la dépense.

### 4.3 Le besoin du bras A sur Rigaud (N2), cherché par chemins nommés

- R-3611 : 124 USD déclarés sur Rigaud ; environ 75,6 déjà comptés ; reste net d'environ 48. Aucun besoin du bras A n'y est chiffré.
- GO-2026-11-19-31 et R-3707 : la part Claude de **l'essai de mesure** des lecteurs du bras A est payée par Rigaud.
- GO-2026-11-19-34 : ligne de calcul de la file Claude de cet essai, **plafond 9,25 USD**, échéance 2026-11-20. Elle porte sur le devis `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, commit `de052f27`, `533ad5b15e6de1bdfe81c35f8501dbad376f52f907be84094c3fd8621b349592`. J'ai lu ce devis :
  - **§ 5.1 et § 6.3** : file Claude, 120 appels ; plafond 9,25 USD (6,00 + 3,00 + 0,25), attendu 1,93, pire 29,23 ; clé Rigaud (§ 5.6) ;
  - **§ 7.3, point 2** : l'estimation des lectures elles-mêmes, environ 580 USD pour le lecteur Claude au seuil de la règle. Le devis la renvoie au « devis des lectures », non écrit.
- R-4089 : 0,904 USD de l'essai de mesure déjà retranchés des 47.
- R-3647, point 2 : la clé Claude des lectures et son budget « se décident au devis » des lectures. Si la part du lecteur Claude dépasse le reste de Rigaud, c'est une décision de Lazar.

**Réponse pour la mère.**
1. *Essai de mesure.* Le chiffre réservé à la file Claude sur Rigaud est **9,25 USD** (chemin et empreinte ci-dessus). 0,904 USD sont déjà dépensés et comptés. Il reste donc **au plus 8,35 USD** réservés si la file n'est pas close. Je n'ai trouvé par chemins nommés ni sa clôture ni sa prolongation.
2. *Lectures du bras A.* **Aucun chiffre sur Rigaud, non trouvé par chemins nommés.** Le seul ordre de grandeur écrit, environ 580 USD, dépasse Rigaud de loin.

Conséquence : si le besoin du bras A sur Rigaud se borne à la file de l'essai, X ≤ 8,35. Cela reste sous la bascule de 9,28 : la répartition « X ≤ 9,28 » s'applique, et Rigaud garde un rapport de 1,452. Si Rigaud doit aussi porter une part des lectures, X est inconnu et dépasse sans doute 9,28 : la répartition « X > 9,28 » s'applique.

### 4.4 Peut-on séparer le proposeur et le juge de l'espèce 3 sur deux clés ?

**Oui.** GO-2026-11-20-14 et -16 disent « une espèce ou un rôle fixe par clé ». Ces deux lignes sont postérieures à R-4087 (« une espèce fixe par clé », routine de la mère), et elles priment. La mère le confirme.

Il y a deux conditions :
- **Le véhicule route les appels par rôle, et non par espèce.** Un appel du juge de l'espèce 3 qui se présente sur la clé du proposeur de la même espèce est refusé. C'est la garde que j'ajoute à l'arrêt n° 12 (K18), éprouvable sur un cas sain et sur un artefact.
- **Le coût rendu à la composition se compte par rôle et par espèce, jamais par clé.** Le texte le tient : M4 est « par espèce et par rôle », et la lecture de la composition se fait par espèce. Mais il ne dit pas que le cumul par clé reste hors du signal. Je l'ajoute (K15) : ce cumul ne vit qu'au journal des gardes, et le coût de l'espèce 3 s'additionne sur ses deux rôles, quelles que soient leurs clés.

### 4.5 Les bornes, l'arrêt nommé et l'absence de bascule sont-ils éprouvables (règle R5) ?

**Absence de bascule : oui**, avec la garde de routage de K18. Une bascule silencieuse serait justement un appel présenté sur une autre clé.

**Arrêt n° 11 : non, tel qu'écrit.** Le texte borne la part de chaque clé « à son solde relevé le jour même ». La garde compare donc le reste du jour à une part qui en est tirée : elle ne peut jamais se déclencher, et son artefact n'existe pas. De plus, les soldes de Minuit et de Rigaud ne sont pas lisibles (R-4082 ; ils sont calculés). La correction K17 fixe la part au complément de valeurs. La garde compare alors le reste du jour à cette part fixée, et la part n'est jamais abaissée en silence. Cas sain : reste égal à la part. Artefact : un centime de moins.

**Arrêt n° 12 : à moitié.** « Le cumul atteint sa part » se lit après l'appel. Un appel lancé à 1 USD de la part peut la dépasser de son coût, jusqu'à 6,05 USD pour un proposeur. Comme la part égale le solde, ce dépassement devient un refus pour crédit du fournisseur, au milieu d'une génération. La correction K18 compte, avant l'appel, le cumul plus le pire des appels en vol et de l'appel à lancer. Le pire d'un appel d'aiguilleur et de juge n'est écrit nulle part ; il va au complément (K7).

**Refus pour crédit sur l'une des trois clés avant sa part.** C'est possible, puisque les soldes sont calculés et non lus. Aucune garde ne le couvre : l'arrêt n° 13 ne vise que les clés sous dispense. K19 l'ajoute à l'arrêt n° 13. La liste garde ainsi quinze conditions.

### 4.6 Ce que GO-2026-11-20-16 change à N2, au plafond total et à la ligne

- **N1 est tranché** : bornes par clé, sans recharge ; la branche « recharge » et la ligne à trois espèces tombent. D7 (a) de GO-2026-11-20-10, « recharge à la part au pire », est remplacée. La condition de GO-2026-11-20-08, « recharge … sinon, repli sur deux espèces », se lit remplacée elle aussi, puisque GO-2026-11-20-16 répond à ce manque. **La mère le consigne à la ligne d'activation**, car c'est ma lecture.
- **La ligne et le plafond total ne changent pas** : ligne de course de 450 USD exactement (trois générations à 150, réservées, montant exigé par l'orchestrateur) ; plafond total de 456 USD ; parts au pire des relais 2 et 3 inchangées.
- **Ce qui change** : la dépense du premier relais est bornée par la somme des parts, au plus 423,56 − X USD. L'arrêt nommé peut couper la course avant sa ligne, entre le cas haut et le pire. Le lanceur compare chaque clé à sa part, non à 450.
- **N2 change de nature.** La règle est tranchée : Rigaud est gardée au bras A « selon son devis ». Reste un chiffre, et un choix si ce chiffre manque ou s'il dépasse 9,28 USD. N2 se récrit donc (K22).

## 5. La liste d'arrêt (point 5)

Il y a **quinze conditions**, dont la garde « hors case » (n° 4) et celle du coffre (n° 5).

- **La garde « hors case »** reprend à la lettre le texte du contrôle (§ 3) : cas sain, une fiche dans sa case passe ; artefact, un témoin planté « hors case » est refusé et compté ; elle se distingue des témoins « hors périmètre ». En course, aucun seuil d'arrêt n'est posé sur son compte. C'est cohérent avec le contrôle, et l'audit de symétrie (K13) en prend le sens haut.
- **La garde du coffre** : « strictement plus d'un quart » est une lecture fidèle de « plus d'un quart » (ordre, § 11). À la troisième génération, aucune génération ne suit, et le texte ne dit pas ce que fait le dépassement : K20 l'écrit.
- **Les arrêts n° 11, 12 et 13** sont à corriger (§ 4.5) : K17 à K19.
- **Il manque la lecture d'une course arrêtée.** Le texte ne dit pas ce qu'on lit si un arrêt coupe la course avant la fin de la troisième génération (arrêts n° 5 à 7, 12 et 13). K21 ajoute une règle de lecture. C'est une proposition de contre-lecteur, que la mère accepte ou refuse ; elle ne vise aucun signe.

## 6. Les nœuds N1 et N2 (point 6)

- **N1** est au format, et son défaut est juste : « Aucun : compte et dépense ». Il est **tranché** par GO-2026-11-20-16 (K22).
- **N2** est au format, avec le défaut « Aucun : compte ». Il se récrit sur ce que GO-2026-11-20-16 a fixé et sur ce que j'ai trouvé (§ 4.3). Sans défaut (K22).
- Les deux « points de routine » du rapport sont répondus :
  - borne et périmètre : acceptés, sauf la période (K11) ;
  - séparation du proposeur et du juge : permise (§ 4.4).

## 7. Réserves (sans correction)

1. **Une fiche passée par le portier est servie aux générations suivantes avant la relecture de la mère**, qui n'a lieu qu'après la troisième génération (D4 (a)). Si la mère juge ensuite qu'elle glisse vers le concret, son énoncé ramené à une ligne aura déjà été servi. C'est la conception tranchée par GO-2026-11-20-10, non une faute du texte. Changer ce point serait un nœud ; je le signale à la mère.
2. **L'espèce de l'aiguilleur n'est pas dite** dans les pièces lues. La lecture « une espèce entière par clé » du § 4.2 le traite comme une unité à part. Si l'aiguilleur est de l'espèce 3 ou 4, cette lecture change. Elle n'est pas proposée.
3. **`main` a avancé** (commit `0b265f65…`) depuis le commit que cite le texte. Le rédacteur F relit `main` au moment d'appliquer, recalcule les deux empreintes de registre et cite le commit relu.
4. Les heures prêtées aux mots de Lazar dans R-4088, R-4089 et R-4092 étaient estimées : la mère l'a corrigé dans R-4093. Cela répond à la réserve 5 du rapport (K23).
5. Une de mes commandes a écrit sa sortie à l'écran au lieu d'un fichier. L'outil l'a gardée de lui-même sous `/root/.claude/…`. Je ne l'ai pas ouverte. Cette sortie est égale à la sortie versée, qui a été rejouée vers un fichier, à empreinte égale.

## 8. Corrections, texte exact

Ces corrections s'appliquent aux v2 nommées au § 0. Dans chaque v2, le titre passe de « — v1 » à « — v2 ». Une ligne s'ajoute sous « Statut », de la forme : « Version : la v2 remplace la v1 (`0f0d8b9b…` ; pour le rapport, `057b3a4c…`) après la contre-lecture `contre-lecture-preenregistrement-court-nouvelles-attaques-v1.md` ([empreinte de ce rapport]) ; corrections K1 à K24 appliquées à texte exact ; la v1 reste archivée, non modifiée. » Les numéros de ligne renvoient à la v1.

### Préenregistrement

**K1** (ligne 9). Ancien :
`puis GO-2026-11-20-14 et R-4089 (une troisième clé ; une répartition proposée pour chacune des deux branches).`

Nouveau :
`puis GO-2026-11-20-14 et R-4089 (une troisième clé), enfin GO-2026-11-20-16 et R-4092 (chaque clé plafonnée à son solde, sans recharge : la branche « bornes par clé » est tranchée).`

**K2** (ligne 20). Ancien :
`` | accords | `registres/go.md` sur `main`, commit `8cf0d3d136ab78d77d8b7978d1fdaff4e9eac59f` : GO-2026-11-20-05, -08, -10, -12, -13, -14 | `8639e38fea4708c2f843202b1bb26fe0321381d9792e79bbdb853fcd3d288024` | ``

Nouveau :
`` | accords | `registres/go.md` sur `main`, commit `0b265f658bdfd3dda8bc432a1f05f2f15766d2e6` : GO-2026-11-20-05, -08, -10, -12, -13, -14, -16 ; GO-2026-11-19-34 | `faa6bd5175a6639a944485b6ab6112b938dabb7e8cbd47fca22e5aa8a31f9a4b` | ``

Si `main` a encore avancé, le commit et l'empreinte sont ceux de la relecture, et les lignes nommées doivent y être inchangées.

**K3** (ligne 21). Ancien :
`R-4084, R-4086, R-4087, R-4088, R-4089 | `f45e63331edbb756fe5519ac9a763965cb1f7058c37225ae962d222c38032903` |`

Nouveau :
`R-4084, R-4086, R-4087, R-4088, R-4089, R-4091, R-4092, R-4093 | `8c8bded74eb12a3be69929f73c79ddd26c14f3e8d92fd3432794ac86b0af228b` |`

Même réserve sur le commit relu.

**K4** (ligne 93). Ancien :
`(GO-2026-11-20-12, lu avec l'erratum R-4086 ; GO-2026-11-20-14 ; R-4084, R-4089). Manière de combiner, gelée (R-4087, GO-2026-11-20-14) :`

Nouveau :
`(GO-2026-11-20-12, lu avec l'erratum R-4086 ; GO-2026-11-20-14 ; GO-2026-11-20-16 ; R-4084, R-4089, R-4092). Manière de combiner, gelée (R-4087, GO-2026-11-20-14, GO-2026-11-20-16) :`

**K5** (lignes 95, 102, 104 et 106).

(a) Ancien :
`Soldes connus à l'écriture ; aucun n'est lu sur le compte, et le relevé du jour de la course prime :`

Nouveau :
`Parts plafonnées au solde de chaque clé, sans recharge (GO-2026-11-20-16). Aucun solde n'est lu sur le compte : Minuit et Rigaud sont calculés au registre des dépenses, Luc est déclaré :`

(b) Ancien :
`| somme | environ 423,56 USD | contre une part au pire de 450 USD (devis, § 3) : il manque environ 26,44 USD |`

Nouveau :
`| somme | environ 423,56 USD, moins le besoin du bras A sur Rigaud | sous la part au pire de 450 USD du premier relais (devis, § 3) : il manque au moins 26,44 USD ; GO-2026-11-20-16 ne recharge pas, et l'arrêt n° 12 tient l'écart |`

(c) Ancien :
`**Ce besoin n'est écrit dans aucune pièce que j'ai lue : il est ouvert**, et il retranche d'autant le solde de Rigaud dans les deux branches ci-dessous.`

Nouveau :
`` GO-2026-11-20-16 garde Rigaud « pour le bras A selon son devis ». Ce que le bras A y réserve, noté X, se retranche des 47 USD. Deux chiffres seulement sont trouvés par chemins nommés. Pour la file Claude de l'essai de mesure : 9,25 USD de plafond (GO-2026-11-19-34 ; devis `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, commit `de052f27`, `533ad5b15e6de1bdfe81c35f8501dbad376f52f907be84094c3fd8621b349592`, § 5.1 et § 6.3), dont 0,904 déjà comptés dans les 47 (R-4089) : au plus 8,35 USD encore réservés. Pour les lectures du bras A : aucun chiffre sur Rigaud n'est trouvé. **X est ouvert** : la mère l'écrit au complément de valeurs, ou le porte à Lazar (nœud N2 du rapport). ``

(d) Ancien :
`(calcul du rédacteur, à la main, non rejoué par programme, à contre-lire)`

Nouveau :
`` (calcul du rédacteur, rejoué par programme à la contre-lecture : `calcul_repartition_cles_v1.py`, `7f7216501e4ad3d843e5cd59ae2ce2fe6fca42d36400ad8f1e2a1d5f016bca25`, sortie `calcul-repartition-cles-v1.json`, `bf423a5e9106b059e76cd50f6a7e3c0f4ac0e8730d4c0b517def0414890a8fdd`, jouée deux fois, égale à l'octet ; versés par la mère avec ce texte) ``

**K6** (lignes 108 à 114, la table des coûts par rôle, entière). Ancien :

```
| rôle | cas bas | cas haut |
|---|---|---|
| proposeur de l'espèce 3 | 22,29 | 26,61 |
| proposeur de l'espèce 4 | 52,74 | 62,97 |
| aiguilleur | 13,77 | 61,38 |
| juge de l'espèce 3 | 20,58 | 105,05 |
| somme | 109,38 | 256,02 |
```

Nouveau :

```
| rôle | cas bas | cas haut | pire |
|---|---|---|---|
| proposeur de l'espèce 3 | 22,29 | 26,61 | 199,65 |
| proposeur de l'espèce 4 | 52,74 | 62,97 | 199,65 |
| aiguilleur | 13,77 | 61,38 | 450 |
| juge de l'espèce 3 | 20,58 | 105,05 | 450 |
| somme | 109,38 | 256,01 (256,02 sans arrondir les lignes) | 450 au plus : les pires ne s'additionnent pas, le plafond d'une génération (150 USD) tient tous les rôles ensemble |
```

Puis, ligne 116. Ancien :
`avec les marges dites ci-dessous`

Nouveau :
`avec les rapports « part / cas haut » dits ci-dessous`

**K7** (lignes 118 à 130 : du titre « **Répartition proposée, la même dans les deux branches** » jusqu'à la fin du paragraphe « **Branche « recharge »**. … aucune clé ne couvre seule le pire de ses rôles. », tout compris). Ce bloc est remplacé en entier par le texte ci-dessous. La branche « recharge » tombe.

```
**Répartition proposée** (proposition, contre-lue avec le véhicule ; GO-2026-11-20-14 et -16). Règle, écrite avant toute lecture : parmi les répartitions où chaque rôle tient sur une seule clé, fixe pour les trois générations, et où chaque clé tient le cas haut de ses rôles, on prend celle dont le plus petit rapport « part de la clé / cas haut de ses rôles » est le plus grand. Le calcul se fait par programme, aux parts du complément de valeurs. Aux parts connues, elle ne dépend que de X, le besoin du bras A sur Rigaud :

| clé | si X ≤ 9,28 USD : rôles | cas bas | cas haut | part | rapport part / cas haut |
|---|---|---|---|---|---|
| Minuit | juge de l'espèce 3 | 20,58 | 105,05 | 162,56 | 1,547 |
| Luc | aiguilleur ; proposeur de l'espèce 4 | 66,51 | 124,35 | 214 | 1,721 |
| Rigaud | proposeur de l'espèce 3 | 22,29 | 26,61 | 47 − X | (47 − X) / 26,61, au moins 1,418 |

| clé | si X > 9,28 USD, ou si X n'est pas écrit : rôles | cas bas | cas haut | part | rapport part / cas haut |
|---|---|---|---|---|---|
| Minuit | juge de l'espèce 3 | 20,58 | 105,05 | 162,56 | 1,547 |
| Luc | aiguilleur ; proposeurs des espèces 3 et 4 | 88,80 | 150,96 | 214 | 1,418 |
| Rigaud | aucun rôle | 0 | 0 | 47 − X, laissés au bras A | — |

Pourquoi : la bascule est à X = 9,28 USD, là où (47 − X) / 26,61 égale 214 / 150,96. Si le besoin du bras A se borne à la file de l'essai de mesure (au plus 8,35 USD), la première table s'applique. Les deux tables font mieux que la répartition « Minuit : aiguilleur et espèce 4 ; Luc : juge ; Rigaud : espèce 3 » (rapport minimal 1,307 ; marge de Minuit 38,21 USD au cas haut). Elles font mieux aussi que son repli « Minuit : aiguilleur, espèces 3 et 4 » (1,077 ; 11,60 USD). Elles séparent le proposeur et le juge de l'espèce 3 sur deux clés, ce que permet la lettre de GO-2026-11-20-14 et -16 (« une espèce ou un rôle fixe par clé »). À la lecture « une espèce entière par clé », la meilleure répartition est « Minuit : aiguilleur et espèce 4 ; Luc : espèce 3 entière ; Rigaud : rien », avec un rapport minimal de 1,307 ; elle est plus serrée, et elle n'est pas proposée. Les rapports sont des rapports, non des marges en USD. Au pire du devis, aucune répartition ne tient : entre le cas haut et le pire, l'arrêt n° 12 tient la dépense.

**Branche retenue : bornes par clé, sans recharge** (GO-2026-11-20-16, R-4092 ; option (b) de R-4088 et R-4089). La branche « recharge » et la ligne à trois espèces tombent. La part de chaque clé est fixée au complément de valeurs : Minuit 162,56 USD ; Luc 214 USD ; Rigaud 47 USD moins X. Une fois fixée, une part ne change plus. Un reste du jour plus bas que sa part refuse le départ (arrêt n° 11) ; il ne l'abaisse jamais en silence. La somme des parts, au plus 423,56 USD moins X, reste sous la part au pire de 450 USD du premier relais : la course peut donc s'arrêter par l'arrêt nommé « part d'une clé épuisée » avant sa ligne, sans bascule. Le lanceur compare chaque clé à sa part, non à 450 USD, et la ligne d'activation le dit.
Ce qui ne change pas : la ligne de course reste de 450 USD exactement (GO-2026-11-20-08) ; le plafond total reste de 456 USD ; les relais 2 et 3 gardent leurs parts au pire (450 et 199,65 USD).
La condition de GO-2026-11-20-08, « recharge … sinon, repli sur deux espèces », se lit avec GO-2026-11-20-12 et R-4086, puis est remplacée par GO-2026-11-20-16 : ni recharge, ni repli. La mère le consigne à la ligne d'activation.
```

**K8** (lignes 132 à 146). Les remplacements suivants s'appliquent dans l'ordre.

(a) Ancien :
`**Valeurs ouvertes.** Les tables ci-dessus sont une proposition ; aucune valeur n'est figée par ce texte. Elles attendent le mot de Lazar, qui tranche la branche (R-4088, R-4089 ; la ligne à trois espèces, 195 USD, reste une option de R-4088).`

Nouveau :
`**Valeurs ouvertes.** La branche est tranchée (GO-2026-11-20-16). Les parts et la répartition se figent au complément de valeurs, selon les valeurs et la règle écrites ci-dessus. Ce qui reste ouvert est dans la table.`

(b) Ancien :
`| la branche : bornes par clé, ou recharge (laquelle, de combien) | le mot de Lazar, inscrit au registre des accords | avant tout allumage et avant la contre-lecture du véhicule |`

Nouveau :
`| X, le besoin du bras A sur Rigaud, donc la part de Rigaud et le choix entre les deux tables de répartition | écrit par la mère au complément de valeurs, d'après le devis du bras A (essai de mesure : au plus 8,35 USD ; lectures : non trouvé par chemins nommés) ; s'il n'est pas écrit, la seconde table s'applique et le nœud N2 va à Lazar | avant tout allumage et avant la contre-lecture du véhicule |`

(c) Ancien :
`| la part bornée de chaque clé, en USD | la branche retenue ; aucune part ne dépasse le solde de sa clé relevé le jour même, retranché pour Rigaud du besoin du bras A | même moment |`

Nouveau :
`| la part bornée de chaque clé, en USD | GO-2026-11-20-16 : Minuit 162,56 ; Luc 214 ; Rigaud 47 moins X ; écrite au complément, jamais abaissée en silence (arrêt n° 11) | même moment |`

(d) Ancien :
`| la répartition des rôles du premier relais entre les trois clés | la proposition ci-dessus, si la contre-lecture du véhicule la confirme et si Lazar ne dit pas autre chose ; chaque rôle sur une seule clé, fixe pour les trois générations | même moment |`

Nouveau :
`| la répartition des rôles du premier relais entre les trois clés | la règle ci-dessus (rapport minimal le plus grand), première ou seconde table selon X, si la contre-lecture du véhicule la confirme ; chaque rôle sur une seule clé, fixe pour les trois générations | même moment |`

(e) Ancien :
`| le besoin du bras A sur la clé Rigaud | écrit par la mère, sur le devis du bras A | même moment |`

Nouveau :
`| le pire d'un appel d'aiguilleur et d'un appel de juge, en USD (arrêt n° 12 ; celui d'un proposeur est de 6,05, devis, § 3) | la mesure des consignes sans appel et la sortie maximale de la configuration | même moment |`

(f) Ancien :
`**Si le mot de Lazar retient la ligne à trois espèces, ce préenregistrement ne vaut plus** : la composition et la ligne changent, et une version 2 s'écrit avant toute dépense.`

Nouveau :
`La ligne à trois espèces (R-4088, option (c)) n'est pas retenue (GO-2026-11-20-16).`

(g) Ancien :
`La décision D7 (a) de GO-2026-11-20-10, « recharge à la part au pire après un relevé du jour », se lit désormais avec GO-2026-11-20-12, GO-2026-11-20-14, R-4088 et R-4089 : elle reste la règle si Lazar retient la branche « recharge ».`

Nouveau :
`La décision D7 (a) de GO-2026-11-20-10, « recharge à la part au pire après un relevé du jour », est remplacée par GO-2026-11-20-16 : aucune recharge.`

**K9** (ligne 6). Après « porté avant la remise. », ajouter :
` Version 2 : [relevé de date -u du rédacteur F], après la contre-lecture et GO-2026-11-20-16.`

**K10** (lignes 158 à 161, la table des graines).

(a) Ancien :
`un entier uniforme de 0 à 4 : la valeur`

Nouveau :
`` un entier uniforme de 0 à 4, `rng.integers(0, 5)` : la valeur ``

(b) Ancien :
`onze cases sans remise parmi les cases restantes, prises dans l'ordre canonique : 100 pour la génération 1, puis 89, puis 78 ;`

Nouveau :
`` onze cases sans remise parmi les cases restantes, prises dans l'ordre canonique, par `rng.choice(n, size=11, replace=False)` sur leurs rangs, n valant 100 pour la génération 1, puis 89, puis 78 ; ``

(c) Ancien :
`| 12, 13 | ordre des lignes du registre servi aux générations 2 et 3 | une permutation uniforme |`

Nouveau :
`` | 12, 13 | ordre des lignes du registre servi aux générations 2 et 3 | `rng.permutation(n)` sur les n lignes, rangées d'abord dans l'ordre de leurs identifiants |``

(d) Ancien :
`60 fiches sans remise parmi les fiches qui passent la relecture de la mère, prises dans l'ordre de leurs identifiants, si elles sont plus de 60 |`

Nouveau :
`` 60 fiches sans remise, `rng.choice(n, size=60, replace=False)`, parmi les n fiches qui passent la relecture de la mère, rangées dans l'ordre de leurs identifiants, si n dépasse 60 |``

Puis, après la table, ajouter :
`L'ordre des identifiants est l'ordre lexicographique de leurs octets UTF-8. Aucune autre méthode de tirage n'est permise.`

**K11** (ligne 178). Ancien :
`- *Période* : du 1ᵉʳ janvier 2016 à la date de la lecture, écrite dans l'étiquette.`

Nouveau :
`- *Période* : sans borne inférieure, jusqu'à la date de la lecture, écrite dans l'étiquette. Une borne en 2016 laisserait hors du périmètre l'apprentissage automatique adverse plus ancien, où une antériorité par classe de mécanisme est plausible ; elle pousserait vers « inédite » (règle R8). Le classement par pertinence de chaque base borne l'effort.`

**K12** (ligne 180). Ancien :
`- *Effort* : pour chaque base et chaque classe de requête, les trente premiers résultats sont examinés sur titre et résumé ; tout résultat retenu est lu sur PDF empreinté. Le journal des requêtes est gardé.`

Nouveau :
`- *Effort* : les chaînes de requête de la classe (i) sont produites par programme à partir de la case, avant toute lecture de la fiche ; celles des classes (ii) et (iii) sont écrites au journal avant d'être lancées. Pour chaque base et chaque chaîne de requête, les trente premiers résultats, dans l'ordre de pertinence de la base, sont examinés sur titre et résumé ; tout résultat retenu est lu sur PDF empreinté. Le journal des requêtes est gardé.`

**K13** (ligne 91). Ancien :
`| audit de symétrie, portier | aucune fiche au coffre et aucune fiche hors case sur les trois générations | valeur du rédacteur de ce texte (règle R4) |`

Nouveau :
`| audit de symétrie, portier | aucune fiche au coffre et aucune fiche hors case sur les trois générations ; ou, dans l'autre sens, strictement plus d'un quart des fiches rendues d'une génération classées hors case (le coffre a sa garde, arrêt n° 5) | valeurs du rédacteur de ce texte et de la contre-lecture (règle R4) |`

**K14** (lignes 65 et 68).

(a) Ancien :
`| M1 | part de filiation | parmi les fiches passées des générations 2 et 3, part dont`

Nouveau :
`| M1 | part de filiation | parmi les fiches passées par le portier aux générations 2 et 3 et gardées à la relecture de la mère, part dont`

(b) Ancien :
`par génération et par case, parmi les fiches rendues (texte du contrôle, § 3) |`

Nouveau :
`par génération et par case, parmi les fiches rendues (texte du contrôle, § 3) ; à part, le compte des fiches passées que la relecture de la mère envoie au coffre, qui ne sont jamais lues par programme |`

**K15** (ligne 69). Ancien :
`| M4 | coût | coût en USD par espèce et par rôle, génération par génération ; part du coût et part des fiches passées par espèce (N-045 v2, points 2 et 3) |`

Nouveau :
`| M4 | coût | coût en USD par espèce et par rôle, génération par génération ; part du coût et part des fiches passées par espèce (N-045 v2, points 2 et 3). Le coût d'une espèce dont les rôles sont sur deux clés s'additionne sur ses rôles. Le cumul par clé ne sert qu'aux arrêts n° 11 à 13 et ne vit qu'à leur journal : il n'entre ni dans M4 ni dans ce qui est rendu à la composition, qui ne lit pas la clé |`

**K16** (lignes 230, 232, 234 et 241).

(a) Ancien :
`aucun ne coûte d'appel, hors les trois lignes à part nommées.`

Nouveau :
`aucun ne coûte d'appel, hors les deux lignes à part nommées.`

(b) Ancien :
`Il porte la manière de combiner les trois clés (R-4087, GO-2026-11-20-14) et la répartition des rôles par clé,`

Nouveau :
`Il porte la manière de combiner les trois clés (R-4087, GO-2026-11-20-14, GO-2026-11-20-16) et la répartition des rôles par clé, avec un routage des appels par rôle, non par espèce (le proposeur et le juge de l'espèce 3 sont sur deux clés), éprouvé à l'arrêt n° 12,`

(c) Ancien :
`3. **Le mot de Lazar sur la branche** (R-4088, R-4089) ; la présence de la clé Rigaud, vérifiée par son nom, dans le conteneur de l'organisme (GO-2026-11-20-14) ; puis le **complément de valeurs** (section « Seuil »), contre-lu et scellé, avant tout allumage et avant la contre-lecture du véhicule.`

Nouveau :
`3. Le mot de Lazar sur la branche est donné (GO-2026-11-20-16) ; la présence de la clé Rigaud par son nom est constatée (R-4091). Reste le **complément de valeurs** (section « Seuil ») : X et les parts des trois clés, la table de répartition, le pire par appel de l'aiguilleur et du juge, les bornes en octets. Il est contre-lu et scellé avant tout allumage et avant la contre-lecture du véhicule.`

(d) Ancien :
`10. Les lignes à part : la sonde minimale de la clé Luc (GO-2026-11-20-13, 0,01 USD) ; la sonde de refus (1 USD) ; l'épreuve réelle des témoins plantés (5 USD).`

Nouveau :
`10. Les lignes à part : la sonde de refus (1 USD) ; l'épreuve réelle des témoins plantés (5 USD). La sonde minimale de la clé Luc est faite (GO-2026-11-20-13 ; R-4091 : 0,000002 USD).`

**K17** (ligne 220). Ancien :
`| 11 | une clé dont le reste, relevé le jour même, ne couvre pas sa part | départ refusé |`

Nouveau :
`` | 11 | une clé dont le reste du jour (calculé au registre des dépenses de `main` pour Minuit et Rigaud, déclaré par Lazar pour Luc, lu pour les autres relais s'il est lisible) est plus bas que sa part écrite au complément de valeurs | départ refusé ; la part n'est jamais abaissée en silence : il faut un complément neuf, contre-lu, ou le mot de Lazar. Épreuve : cas sain (reste égal à la part : départ) ; artefact (reste d'un centime sous la part : refus) | ``

**K18** (ligne 221). Ancien :
`| 12 | **part d'une clé épuisée** en course (premier relais du devis, clés Minuit, Luc et Rigaud) : le cumul compté sur une clé atteint sa part bornée | arrêt nommé de la course, qui dit la clé ; **aucune bascule** vers une autre clé (R-4087) ; les valeurs des parts sont ouvertes (section « Seuil ») |`

Nouveau :
`| 12 | **part d'une clé épuisée** en course (premier relais du devis, clés Minuit, Luc et Rigaud) : avant chaque appel, le cumul compté sur la clé, plus le pire des appels déjà en vol sur elle, plus le pire de l'appel à lancer, dépasserait sa part ; ou un appel d'un rôle se présente sur une autre clé que la sienne | aucun appel neuf sur cette clé ; arrêt nommé de la course, qui dit la clé ; **aucune bascule** vers une autre clé (R-4087, GO-2026-11-20-16). Le pire par appel est de 6,05 USD pour un proposeur (devis, § 3) ; celui de l'aiguilleur et du juge est écrit au complément de valeurs. Épreuve : cas sain (un appel qui tient sous la part, sur sa clé, est lancé et compté sur elle) ; artefacts (un appel qui dépasserait la part d'un centime est refusé, avec l'arrêt nommé ; un appel du juge de l'espèce 3 présenté sur la clé du proposeur de l'espèce 3 est refusé) |`

**K19** (ligne 222). Ancien :
`| 13 | refus pour crédit sur une clé sous dispense de lecture de solde | arrêt de la course ; Lazar prévenu (R-3237, si la dispense est redite) |`

Nouveau :
`| 13 | refus pour crédit sur une clé sous dispense de lecture de solde, ou sur l'une des trois clés du premier relais avant que sa part soit atteinte (leurs soldes sont calculés ou déclarés, jamais lus) | arrêt de la course, nommé, qui dit la clé ; aucune bascule ; Lazar prévenu (R-3237, si la dispense est redite). Épreuve : cas sain (réponse normale) ; artefact (refus pour crédit simulé par le faux fournisseur : arrêt nommé) |`

**K20** (ligne 214). Ancien :
`| la génération suivante ne part pas ; la question dérive vers le concret et se reformule, sur le mot de Lazar |`

Nouveau :
`| la génération suivante ne part pas ; la question dérive vers le concret et se reformule, sur le mot de Lazar ; à la troisième génération, où aucune génération ne suit, le dépassement est consigné et porté en réserve à la relecture de la mère |`

**K21** (ligne 200). Après la phrase « Un résultat trop propre est une réserve, non une trouvaille. », ajouter le paragraphe :

`**Course arrêtée avant la fin de la troisième génération** (arrêts n° 5 à 7, 12 et 13). La relecture de la mère porte sur toutes les fiches passées des générations jouées. M1 à M5 sont rapportées sur les seules générations complètes, sous le titre « course arrêtée par [nom de l'arrêt] ». Si seule la génération 1 est complète, M1 et M2 sont « sans objet ». Aucune phrase sur l'héritage n'est dite d'une génération incomplète.`

### Rapport du rédacteur

**K22** (lignes 62 à 73, de « ### N1 — La branche des clés » à « **Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : compte. », tout compris). Ce bloc est remplacé par :

```
### N1 — La branche des clés — tranché
Tranché par Lazar, GO-2026-11-20-16 (R-4092) : « je recommande de plafonner chaque clé à son solde plutôt que de recharger. go ». C'est l'option (a) : bornes par clé, sans recharge. La branche « recharge » et la ligne à trois espèces tombent. La ligne de course (450 USD) et le plafond total (456 USD) ne changent pas. Plus de nœud.

### N2 — Rigaud, si le besoin du bras A n'est pas écrit ou s'il passe 9,28 USD
**Décision.** Dans ce cas, la part Claude de la course se paie-t-elle sur Minuit et Luc seules, Rigaud restant entière au bras A ?
**Enjeu.** GO-2026-11-20-16 garde Rigaud au bras A selon son devis. Ce devis ne réserve sur Rigaud que la file Claude de l'essai de mesure : 9,25 USD de plafond (GO-2026-11-19-34, `533ad5b1…`), dont 0,904 comptés, soit au plus 8,35 encore réservés. Pour les lectures, aucun chiffre sur Rigaud n'est trouvé par chemins nommés. Or GO-2026-11-20-14 dit que la part Claude se paie sur les trois clés. Sans bascule, ce que la course prend sur Rigaud, le bras A le perd.
**Options.**
(a) Seconde table : Minuit porte le juge de l'espèce 3, Luc l'aiguilleur et les proposeurs des espèces 3 et 4, Rigaud rien. Rapport minimal de 1,418 au cas haut, indépendant du bras A. Mais Rigaud ne porte aucun rôle, contre la lettre « sur les trois clés ».
(b) Lazar écrit maintenant que X se borne à l'essai de mesure (au plus 8,35 USD), et la première table s'applique. Les trois clés servent, avec un rapport minimal de 1,452 ou plus. Mais les lectures du bras A ne pourront plus rien prendre sur Rigaud pendant la course.
(c) Première table quel que soit X, Rigaud bornée à 47 moins X. Les trois clés servent. Mais au-delà de 20,39 USD, Rigaud ne tient plus le cas haut de son rôle (26,61), et la course risque l'arrêt nommé.
**Recommandation.** (b) si le bras A ne lit pas avant la fin de la course, sinon (a) ; confiance 0,6.
**Défaut.** Aucun : compte.
```

Puis, ligne 75. Ancien :
`dire si « une espèce ou un rôle fixe par clé » (GO-2026-11-20-14) permet de séparer le proposeur et le juge de l'espèce 3 sur deux clés, ce que la répartition proposée suppose.`

Nouveau :
`la séparation du proposeur et du juge de l'espèce 3 sur deux clés est permise par GO-2026-11-20-14 et -16 (« une espèce ou un rôle fixe par clé »), confirmée par la mère. Le coût rendu à la composition se compte par rôle et par espèce, jamais par clé.`

**K23** (ligne 83). Après « Je le signale, sans conclure. », ajouter :
` R-4093, erratum de la mère, l'explique : ces heures étaient estimées, et l'heure de la ligne borne celle du mot.`

**K24** (rapport, § 1, § 4 et § 5).

(a) Ligne 11. Ancien :
`Le texte porte une répartition proposée des rôles du premier relais sur les trois clés, pour les deux branches, et dit`

Nouveau :
`La branche est tranchée (GO-2026-11-20-16 : bornes par clé, sans recharge). Le texte porte une règle de répartition des rôles du premier relais sur les trois clés, et ses deux tables selon le besoin du bras A, et dit`

(b) Ligne 44. Ancien :
`six bases, période depuis le 1ᵉʳ janvier 2016, trois classes de requête, trente premiers résultats par base et par classe.`

Nouveau :
`six bases, période sans borne inférieure (correction K11 de la contre-lecture), trois classes de requête, trente premiers résultats par base et par chaîne de requête.`

(c) Ligne 48. Ancien :
`7. **La répartition par clé** : aiguilleur et proposeur de l'espèce 4 sur Minuit ; juge de l'espèce 3 sur Luc ; proposeur de l'espèce 3 sur Rigaud. Les coûts sur trois générations sont calculés à la main à partir du devis et de la sortie de son calcul, non rejoués par programme.`

Nouveau :
`7. **La répartition par clé** (correction K7 de la contre-lecture) : le rapport minimal « part / cas haut » le plus grand. Si X ≤ 9,28 USD : juge de l'espèce 3 sur Minuit ; aiguilleur et proposeur de l'espèce 4 sur Luc ; proposeur de l'espèce 3 sur Rigaud. Sinon : juge de l'espèce 3 sur Minuit ; aiguilleur et proposeurs des espèces 3 et 4 sur Luc ; rien sur Rigaud. Les coûts sur trois générations ont été rejoués par programme à la contre-lecture (`bf423a5e…`).`

(d) Ligne 52. Ancien :
`1. La branche des clés (bornes par clé, ou recharge), les parts en USD, la répartition confirmée : mot de Lazar, puis complément de valeurs.`

Nouveau :
`1. La branche est tranchée (GO-2026-11-20-16). Restent X, les parts en USD et la table de répartition : complément de valeurs, et nœud N2 si X n'est pas écrit.`

## 9. Refus

Aucun refus de permission, de classifieur ni de garde.

— contre-lecteur, modèle O
