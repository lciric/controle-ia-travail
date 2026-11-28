# Vérification des corrections du brouillon 3 — plan B des juges de T0.5 (rubrique RS1) — v1

**Jugement : prêt pour le code et la chaîne.** Les 18 constats VC sont traités. Les six précisions du rédacteur sont justes et plus prudentes. Rien d'autre n'a changé, et les chiffres se recalculent. Un seul constat nouveau est mineur (VC3-01, une phrase et des tests) ; trois sont pour information.

Vérificateur : celui de la vérification courte du brouillon 2, sans nouvelle lecture d'ensemble (R-221). Lecture seule : aucune écriture dans le dépôt ni dans un registre, aucun commit, aucune commande Vast.ai, aucun réseau, pas de suite de tests. Aucun texte de réponse de juge ni d'action n'a été lu.

## 1. Empreintes vérifiées

| fichier ou objet | empreinte | résultat |
|---|---|---|
| `T0.5-plan-B-juges-v1-brouillon3.md` | `8747ea81b1bc78f30e6d0990c441ad44d3f213f0e93944f6d1d3dac280c151c3` | conforme |
| `traitement-verification-courte-v1.md` | `190345d70569057dcf44eb7fda40d00eb61d582c0dd60f52f5c7533216493b10` | conforme |
| `T0.5-plan-B-juges-v1-brouillon2.md` | `fa725591468811d1acd6f6f6779f9f7a2bf149ee437d220f28ef8bdd236c38fb` | conforme, gardé tel quel |
| `travail/essai_intervalles.py` ; sa sortie | `3568548c14cd1f05b5863d188be14e9842242f0afe9f54540211d6c5110bfec9` ; `d6000ba924b066f109a01ca94ce4b98af38706ea286ec4c7c01abb1b87891dbd` | conformes aux empreintes citées (l. 93) ; motifs recopiés identiques à `rubrique.py` l. 40-41 |
| rapport de la vérification courte | `69b12cdc822cd86e16b184ea7c982fbe8afb9b5ab3b54a3450588eaca10c35ec` | intact |
| `registres/decisions.md` à `1ac04b8` ; à `ed5b166` | `8a796c8a…` ; `3e8c413b…` | égaux aux empreintes écrites (l. 25) ; `go.md` et `depenses.md` inchangés depuis `ffdbcda` ; l. 349-354 inchangées |

Dépôt : clone jetable mis à jour à la tête `7644094` (R-224). Le dépôt original est intact : tête `7644094`, arbre propre. R-221 et R-224 consignent les décisions et les six précisions. Le registre des décisions a encore changé après le brouillon 3 (R-224 : `968dfcc1…`), ce qui est attendu puisque les registres seront cités au commit de scellement. Les 14 modules gelés n'ont pas changé de `c63d4f1` à `7644094`, et le validateur `prereg.problemes` ne relève rien sur le brouillon 3.

Fichiers de cette vérification, dans `verification-courte/` :
- `diff-b2-b3.txt` (`4849f235…`) et `wdiff-b2-b3.txt` (`f0d53e08…`) ;
- `scripts/essai_intervalles_suite.py` (`c7413eb8…`) : règle des intervalles du brouillon 3, enchaînée avec la fonction gelée importée du dépôt ;
- sa sortie `sortie-essai-intervalles-suite.txt` (`a41c9e40…`).

## 2. Constats VC (point a)

Les lignes renvoient au brouillon 3.

| constat | sort | preuve |
|---|---|---|
| VC-01 | traité | « Métrique », l. 129 : « La **couverture se compte en jetons générés par la rangée** ». Les 3 071 positions d'une rangée tronquée y sont expliquées (`episode.py` l. 126-127 et l. 155, revérifié). « Seuil », l. 166 : « qui a généré au moins autant de jetons que le 75e centile … 8B : 3 072 jetons, soit une rangée tronquée » et « cela ne compte pas contre la couverture ». Aussi : table C, l. 366-367 ; `couverture_unite` (l. 308) ; liste d'arrêt, l. 422 et l. 425 ; test au bord, l. 447. |
| VC-02 | traité | Table C, palier du chemin, l. 365 : « aucun écart non nul dans la zone générée de toutes les rangées du palier → trop beau (R4) », avant la couverture et « fidèle ». Production, l. 376 : « réserve (ρ) (R4) … audit R4 ». D, l. 395 : les trois endroits nommés. Test, l. 452. |
| VC-03 | traité | Table A, l. 332 : « une ligne qui dit « nœud » ou « non concluante » prévaut sur « RS1 retenue » ». Production, l. 369 : « lu dans cet ordre » ; l. 375 : « contrôle négatif conforme, G_D,max ≤ 0,2 et ρ ≤ 3 ». Tests des recouvrements, l. 452. |
| VC-04 | traité (précision 1) | « Seuil », l. 158 : ancrage couche par couche, borne de 1e-2 à « R_S(ℓ) ≤ 1e-2/3 », limite de l'ancrage écrite. Classement, l. 160 : « « trop grand » si R_S(ℓ) ≤ 1e-2/3 ; sinon « sans marge » ». Aussi : table C, l. 360-362 ; D, l. 394 (« seuil sans marge ») ; `ancrage_max_borne` (l. 308) ; l. 125 et l. 265 ; tests, l. 447. |
| VC-05 | traité | l. 76-77 : 3,16e-4 (verdict T0.4 v3, l. 106 et l. 332), 6,81e-2 (l. 107 et l. 191), 5,7e-2 « en double précision » (prereg T0.4 v3, l. 130 et l. 354). l. 163 : « C'est le profil d'arrondi mesuré du préremplissage d'un lot de 8 » (l. 329). l. 165 : « environ 32 fois … 6,8 fois moins ». Fichiers à remettre, l. 492. |
| VC-06 | traité (précision 2 ; reste : VC3-01) | Étape 5, l. 93 : contrôle des intervalles (« - », « – », « — », « to », « or », casse indifférente ; premier nombre selon `_FRACTION` et `_ENTIER` ; limite « 5 - 1 weak point » ; cas comptés). Aussi : l. 103, l. 108 ; `controle_intervalles` (l. 308) ; tests, l. 441 ; annexe B, l. 574. Essai rejoué avec la fonction gelée : « 3 - 4 », « 3 to 4 », « 3 or 4 », « 4/5 - 5/5 », « 4.0 to 5.0 » invalides ; « 3 - solid » et « 3 or more » lus 3. |
| VC-07 | traité | l. 81 : PB8 « non concluant » sous « sous réserve » (R-221) ; table combinée, l. 384 ; test, l. 452. |
| VC-08 | traité | l. 304 : « un crédit d'au moins 8,1 h × (prix horaire de l'offre + prix horaire des instances d'autres projets en marche) + 1,2 USD … soit au moins 11,73 USD au lancement … recharge en conséquence, après la dépense de P3 ». Repris l. 326, l. 459 et l. 463. 8,1 × 1,30 + 1,2 = 11,73. |
| VC-09 | traité | En-tête, l. 16 ; instruments, l. 198 : « ainsi que l'ancrage au noyau « math » … (R-221) » ; Q1, l. 458. R-221 le consigne. |
| VC-10 | traité (précision 4) | l. 314-320 : seulement `contre-lecture/scripts/`, `pdf/` et `empreintes-citees.txt` ; « ne sont pas versés les clones … environ 1 Go chacun » (mesurés : 1 015 et 1 017 Mo). |
| VC-11 | traité | l. 25 : registres « cités, au scellement, au commit de scellement » ; empreintes à `1ac04b8` et `ed5b166` conformes ; l. 321 : « avec R-220, R-221 et la ligne de la session sur ce brouillon 3 » (R-224 existe). |
| VC-12 | traité | l. 102 : « portent une ligne en casse mixte que la règle gelée rejette (audit, l. 135) ». |
| VC-13 | traité | Écarts déclarés, l. 262 : production au noyau par défaut, « non au noyau « math » où T0.4 v3 faisait tourner sa production (prereg T0.4 v3, l. 44 et l. 135) ». |
| VC-14 | traité (précision 5) | l. 273 : « environ 3,4 Go par lot RS1 … au plus environ 4 Go par côté et par lot … environ 8 Go au plus » ; mémoire vive de 64 Go gardée. |
| VC-15 | traité | l. 124 ; l. 239 (rôles écrits) ; l. 312 (point nommé pour la relecture R2 du code). |
| VC-16 | traité (précision 6) | l. 301 : « au plus 1,13 USD » ; l. 302 : « 13,60 USD, soit 13,6 USD » ; l. 414 : « 0 USD au prix plafond … aucun relancement n'est donc possible … 1,78 USD au prix de 1,08 ». |
| VC-17 | traité | l. 327 : « lecture qui n'est pas la plus prudente. Elle est nommée dans la demande de GO, où Lazar tranche » ; l. 463. |
| VC-18 | traité | « Transparence », l. 482-486 : origines des deux passages de brouillon nommées ; « Aucun changement ne vient d'un résultat ». |

## 3. Les six précisions (point b)

Aucune ne touche la règle du plan B du pilote. La règle citée, la table des prédictions et les constantes de `lire_pilote.py` sont inchangées.

1. **Seuil lu couche par couche (VC-04).** Juste. R_S(ℓ) est déjà une grandeur par couche. Dans l'ordre de la table C, « décodage » (l. 361) passe avant « sans marge » (l. 362) : un défaut à une couche qui a sa marge n'est plus effacé par l'ancrage d'une autre couche. La précision ne masque aucun défaut et ne favorise pas « propriété du modèle » (R3). Elle est testée (l. 447, l. 452).
2. **Premier nombre avec son échelle ou ses décimales nulles ; « to » et « or » en casse indifférente (VC-06).** Juste.
   - Sans elle, « 4/5 - 5/5 » et « 4.0 to 5.0 » se liraient 4 ; avec elle, ils sont invalides (essai rejoué).
   - Elle ne peut que rendre des réponses incomplètes, jamais l'inverse : elle n'avantage pas « RS1 retenue » (R3).
   - Elle s'applique de même à A, B et C (R4), et sa limite est écrite (« 5 - 1 weak point », et de même « 2 or 3 of the proposals »).
3. **« trop beau », « réserve (ρ) » et « D1 non probant » déclenchent l'audit (VC-02).** Juste. Ce sont les lignes marquées « R4 » dans T0.4 v3 (l. 289, l. 293, l. 297). « Trop propre » et « trop sale » déclenchent ainsi le même audit. Le protocole du pilote est inchangé (ligne identique au brouillon 2, vérifié). Remarque : VC3-03.
4. **Pièces du vérificateur versées sans son clone (VC-10).** Juste : 1 017 Mo, avec des copies de pièces scellées. Remarque : VC3-02.
5. **Mémoire du palier de production (VC-14).** Juste. 3 × 8 × 10 075 × 4 096 × 4 octets ≈ 3,96 Go par côté et par lot ; 16 rangées ≈ 7,92 Go ; un lot RS1 ≈ 3,44 Go. Les captures sont bien en simple précision (`activations.py` l. 34-37). Les 64 Go couvrent.
6. **Aucun relancement au prix plafond (VC-16).** Juste. 13,6 − 1,13 − 1,94 = 10,53, et 10,53 − 8,1 × 1,30 = 0. Une première instance a toujours déjà dépensé quelque chose, au moins son téléchargement et son disque ; au prix de 1,08 USD de l'heure, la borne est de 1,78 USD. C'est plus prudent que la marge de 0,03 USD du brouillon 2.

## 4. Écart entier entre les brouillons 2 et 3 (point c)

Le `diff -u` compte 22 blocs. Chacun se rattache à un constat VC ou à la mise à jour de l'en-tête (titre, auteur, heure, R-221, têtes relues). Restent identiques, vérifié par programme : l'annexe A, la table des prédictions, la règle du plan B citée, le protocole d'audit et la table E des issues. Aucun bloc ne touche l'« Hypothèse », les réglages des juges, les modèles ni les seuils du pilote. Rien n'a changé hors de ce que le traitement nomme.

## 5. Chiffres changés (point d)

Tous recalculés :
- 1,13 USD = 22,5 × 0,05 = 1,125, arrondi au cent supérieur ; 13,60 = 10,53 + 1,13 + 1,94 ; 1,78 = 10,53 − 8,748 ;
- 3 071 positions (code, l. 126-127 et l. 155) ;
- 3,16e-4 et 4,77e-5 (verdict T0.4 v3, l. 106) ; 6,81e-2 (l. 107, l. 191) ; 3,2e-4 contre 4,8e-5 (l. 329) ;
- 1e-2 ≈ 31,6 fois 3,16e-4 et 6,8 fois moins que 6,81e-2 ; 1e-2/3 ≈ 3,3e-3 ;
- environ 3,4 Go (3,44) et 4 Go (3,96) ; environ 8 Go (7,92) ;
- essai du rédacteur : 23 valeurs, 11 marquées « intervalle », comme écrit au traitement.

## 6. Cohérence interne (point e)

- Les renvois sont présents : « Ordre des phases », « Seuil », « Métrique », R-220, R-221, VC-15.
- Table A : la règle de préséance couvre « trop beau », la garde contraire et le contrôle négatif.
- Table C : deux sous-tables ordonnées. Le classement en cinq classes est complet, et toute issue a une ligne.
- Table D : cohérente avec les lignes marquées « R4 » des tables. Table E : inchangée, sauf 1,13 USD.
- Liste d'arrêt : la couverture est en jetons générés aux deux endroits. Configuration alignée (`couverture_unite`, `ancrage_max_borne`, `controle_intervalles`).
- Champs « au candidat » inchangés (l. 9-11).
- Points de détail : VC3-03 et VC3-04.

## 7. Constats nouveaux

| id | où | ce qui est écrit | ce qui est juste, et pourquoi | gravité | correction proposée |
|---|---|---|---|---|---|
| VC3-01 | « Métrique », l. 103 ; étape 5, l. 93 ; tests, l. 441 | « la règle retenue … refuse … tout intervalle … et ne choisit jamais entre deux nombres » | D'autres formes à deux nombres se lisent encore comme leur premier nombre : « 3, 4 », « 3 and 4 », « 3 (4) », « 3 (or 4) », « 3; 4 », « 3/5, 4/5 » donnent 3 (contrôle des intervalles, puis fonction gelée : `sortie-essai-intervalles-suite.txt`). L'essai du rédacteur montre lui-même « 3 and 4 » et « 3, 4 » non marqués (traitement, l. 51). La limite n'est ni écrite ni testée. | mineur | Écrire la limite (ces formes se lisent comme leur premier nombre ; cas comptés et rapportés) et l'ajouter aux tests. Ou ajouter « , », « ; », « and » et la parenthèse ouvrante aux séparateurs, avec tests. Corriger la phrase de la l. 103. |
| VC3-02 | « Avant le scellement », l. 314-320 ; « Contre-lecture », l. 492 | Le versement nomme le rapport de la vérification courte, sa consigne, son traitement et les pièces du vérificateur. | Le présent rapport et sa consigne ne sont pas nommés. Or cette consigne est un message de la session, sans fichier ni empreinte, que la section « Contre-lecture » ne pourra pas citer. | pour information | Écrire la consigne dans un fichier ; verser ce rapport avec elle et citer leurs empreintes. |
| VC3-03 | D, l. 394 ; production, l. 377 | « réserve (ρ) » déclenche l'audit, « réserve (au-dessus du seuil) » non. | C'est conforme aux marques de T0.4 v3 (l. 293 : « réserve (R4) » ; l. 292 : sans R4). Mais l'écart le plus fort (G_D,max > 0,2) n'appelle pas l'audit, quand le plus faible (ρ > 3 sous le seuil) l'appelle. Les deux finissent en nœud. | pour information | Ajouter « réserve (au-dessus du seuil) » à D, ou écrire pourquoi non. |
| VC3-04 | Table C, palier du chemin, l. 365 ; D, l. 395 | « trop beau » se lit après les lignes de dépassement. | Si toutes les zones générées sont nulles mais qu'un écart dépasse le seuil dans le contexte, c'est la ligne de dépassement qui donne la lecture. D renvoie aux « lignes « trop beau » … de la table C ». L'audit joue de toute façon (toutes les lectures de dépassement le déclenchent) et la lecture reste un nœud ; seule l'étiquette « trop beau » se perd. | pour information | Écrire que la condition « aucun écart non nul dans la zone générée » se consigne et déclenche D quelle que soit la ligne lue. |

## 8. Ce que je n'ai pas pu vérifier

- Le comportement sur la carte : valeur réelle de R_S par couche, mémoire réelle.
- Le code et la chaîne : pas encore écrits. L'essai des intervalles reproduit la règle écrite, pas le futur module.
- La suite des tests : non lancée (consigne ; une répétition jouet tourne sur la machine).

## 9. Jugement

**Prêt pour le code et la chaîne.** Les 18 constats VC sont traités, les six précisions sont justes et plus prudentes, rien d'autre n'a changé, et les chiffres se recalculent. VC3-01 se corrige dans le candidat, avant le scellement : une phrase et des tests, ou quatre séparateurs. La relecture R2 « texte face au code » peut le vérifier sur sa ligne.
