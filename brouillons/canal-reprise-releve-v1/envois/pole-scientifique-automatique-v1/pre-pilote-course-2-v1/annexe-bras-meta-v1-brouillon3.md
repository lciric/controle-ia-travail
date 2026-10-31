# Annexe des paramètres du bras méta, version 1 (« trou à structure commune »)

**Statut.** Version de travail de l'annexe ; le nom du fichier et les deux premières lignes du bloc N4 (section 8) disent laquelle (numéro de brouillon, option portée). Elle ne vaut annexe scellée que si les deux champs `contre_lecture` et `approbation_lazar` du bloc de paramètres (bloc N4) sont remplis et que le fichier porte son compagnon `.sha256` ; tant qu'ils portent « À REMPLIR », le code v55 la refuse (A20 : bras méta « non produit (annexe non conforme) »). Chaque valeur est proposée « À GELER par Lazar », avec raison, alternative et confiance ; seule la décision `R-NNN` citée dans `approbation_lazar` les gèle. L'écriture de ce texte n'a rien lancé : aucune dépense, aucun réseau, aucun appel de modèle.

**Pourquoi le texte est écrit ainsi (code v55).** `bisociateur_v55.lire_annexe_meta_v55` compare le brouillon relu à l'annexe scellée et refuse toute différence hors des deux champs libres (textes hors blocs JSON identiques, blocs JSON identiques une fois ces deux champs retirés). Le brouillon qui sera relu pour le scellement doit donc déjà avoir son texte définitif. Ce texte est écrit dans cette forme, **sauf le bloc marqué N4** (section 8), qui dépend de l'option retenue pour CA1-05 et CA1-04 au nœud N4 du collisionneur : choisir une option change ce bloc, et lui seul (mode d'emploi en section 0.4). Le script imprime l'empreinte de tout le texte hors du bloc N4 (sortie § 8) : elle doit rester la même d'un brouillon à l'autre tant que seule l'option change.

- **Exigée par** : `preenregistrement-pre-pilote-course-2-brouillon10.md` (même dossier, `ea940d56e5ee949e7b71a57488f7c2c8a2b7ac4835f30cb5f98933e4c00c824f`, compagnon conforme) : M9 (bras méta), P14, S28, S29 (a à f), Plan É0 et É7b, A20, garde R5 lignes 22a, 22b, 23, 24, DEP10, décision D-h. Lazar a tranché **D-h (a)** : le pré-pilote attend cette annexe scellée avant son gel (R-718). Nom de la version scellée : `annexe-bras-meta-v1.md` (même dossier).
- **Auteurs** : **brouillon 2** — rédacteur neuf Opus 5.5 de la lignée conv-audit, 31 octobre 2026, qui n'avait écrit ni le brouillon 1, ni sa contre-lecture, ni le préenregistrement ; interrompu à 12:09:23 UTC avant d'exécuter son script (R-747) : ses chiffres étaient laissés en marqueurs. **Brouillon 3** — second rédacteur neuf Opus 5.5 de la même lignée, 31 octobre 2026 (à partir de 12:34 UTC), qui n'a écrit ni le brouillon 1, ni le brouillon 2, ni la contre-lecture, ni le préenregistrement : il a exécuté le script du brouillon 2, rempli les chiffres, corrigé ce que la sortie contredit ou ne montre pas, et ce qui empêchait qu'un seul bloc change avec l'option (section 13). **A9 respecté** par les deux : aucune fiche de Kimi lue, aucun témoin, aucune clé, rien sous `donnees/`. **Réserve d'indépendance (inchangée)** : la contre-lecture doit venir d'un modèle autre qu'Opus (Sonnet 5.5 ou Fable 5.1 ; R2).
- **Pièces lues (sha256sum à la lecture)** :
  - brouillon 1 `annexe-bras-meta-v1-brouillon1.md` `3a2e8dc2f8d764674941498ab0da9a977e7cbbd1478d868428efb8d1ca3441a0` (compagnon conforme) ;
  - contre-lecture `contre-lecture-annexe-bras-meta-v1-brouillon1.md` `db249b9356f8d19cd8c9811c3db184b0d7587eba97ed8386501e146434e24f1d` (compagnon conforme ; constats CA1-01 à CA1-15) ;
  - brouillon 2 `annexe-bras-meta-v1-brouillon2.md` `dfd68fcf631456ad8a28aac636faa683b42ae2b84323b7d4b9b76844945a8c6e` et son script `calcul-profil-bras-meta-v1-brouillon2.py` `3659692cc06808a9a93b37f39efdb123a51f1d48fee112fbc2625945b9993dd5` (sans compagnons ; lus en entier par le rédacteur du brouillon 3, gardés sans modification, R12) ;
  - préenregistrement brouillon 10 (ci-dessus) : en-tête, résumé, M4, M9, P14, S23, S28, S29, D-h, Plan (É0, É7, table des coûts), table R5 ligne 22a, DEP10 ;
  - `registres/decisions.md` (vivant ; `ba31cdb1edcf43faf9dd3f2eab2c2e14fc62394941168242a011050ea9f6a5ea` à la lecture du brouillon 2, `73177497128ebf35ea803813aeb498d558e9c781dbb76f51366f25e676b5a21a` à celle du brouillon 3) : R-638, R-672, R-675, R-678, R-718, R-747, R-748 ; aucune décision sur CA1-05 ni CA1-04 ;
  - question des nœuds `collisionneur-noeuds-31-octobre-v1/question-noeuds-decisionnels-collisionneur-v10.md` `a6fe1b66c403f9803065193b32173e1a1fc524986fea2a17e18fc2f7fbde5c69` (compagnon conforme) : N4, identique mot pour mot à celui de la v9 (`7df2e92ba9ded34489f38913295cba7fc8e2238bd17c5dc2af4e56f66cecff7b`, lue par le brouillon 2) ; N5 (choix de code 8). Une v11 (`4d322cf5e892cb1d95f7a4e0e9479ddf84c753ef4c657e6ae511b2b02539bd78`, compagnon conforme) est apparue pendant la vérification (≈ 12:45 UTC) : son N4 ajoute deux renvois (script v9 et brouillon 10) et une phrase sur le brouillon 2 de cette annexe ; les options (a) à (e) sont inchangées ;
  - code v55 (`docs/notes/ideation-organisme-v1/orchestrateur-v55/pole/`) : `bisociateur_v55.py` `d9521311a96384494871e9f9fcd4b4554548b9f45fdc28e8e75ca30d4c54d22f` ; `bisociateur_v54.py` `20d938b2dcafcd4bb7c9777a0182a3590b390a146a8375590905741ea0e250f8` ; `bisociateur_v53.py` `962eb8ce22d5af1bf59970e9ef9cab15620edef4d5e9746161bc302e97c2af02` ; `course2_v55.py` `ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70` ; `course2_v54.py` `ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342` ; `configuration_v54.py` `3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66` ; `gardes_e0_v55.py` `e46c5cd0a301c89830d97c098ee52b33ead6b01cafe15ab8454e6b7957c54db1` ; `outils.py` `966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444` ; `LISEZMOI-orchestrateur-pole-v7-v55.md` `bbfdcb3c30d174dd7feeee9ba8dd20aeb7777c5f0e65aeb087e3c4388c743aa3` (empreintes recalculées au brouillon 3, égales) ;
  - texte I `question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v5.md` `a750144963913ba1c3dcf3eed5d4f8322d7d0246135e17c95ac8e7253c2dd680` : glossaire, règles, « Déroulé » (l. 48 : « Deux fiches par axe et par proposeur au plus »), axes 1 à 5 et 7, liste D ;
  - devis `docs/notes/ideation-organisme-v1/course-2/devis-course-2-et-pre-pilote-v6.md` `13ef84f9fcee9f43914ba76748805a4f2bff2f30bc42de62f42a0600a97473ed` (compagnon conforme) : § 3.2 (l. 157 : É2, attendu 2,9 pour un relais de 3,0 ; l. 164 : 60 lectures d'étiquettes, 1,5 USD, 4 000 / 450 jetons au prix d'Opus ; l. 181 : 0,025 USD la lecture) ; script de puissance v9 `calcul-puissance-pre-pilote-course-2-v9.py` `a28eca2dc2d58f127f010a0f07f9bc86b9697696bffea0b0b58ba0d4b922cd3d` (compagnon conforme) : l. 526 (É2 = 2,0 × 1,447, relais 3,0), l. 534 (passe « tableau » et 20 lectures d'aiguillage à 0,057).
- **Calcul** : `calcul-profil-bras-meta-v1-brouillon3.py` (même dossier, `50e0c0e13cef458a17d990c9e9c4b14594ef81d12b2942fcd1ec4bc5c6de71f3`) reprend le script du brouillon 2 sans changer aucun tirage (sections 1 à 7 de sa sortie) et ajoute les sections 8 à 13 : texte hors bloc N4 et marqueurs restants ; texte exact de l'annexe éprouvé par le code v55 ; marges de la loi par axe et paires de niches retenues ; fourchette détaillée par loi ; sensibilités de toutes les options et classement ; ordre des bras. Il lit les trois blocs JSON de l'annexe (aucune valeur n'y est recopiée) et se joue par `python3 -I` depuis un dossier temporaire vide (python 3.13.18, numpy 2.5.3), sur le fichier qui porte le bloc N4 ; **sa sortie dépend de l'option écrite : nom, empreintes et rejeux au bloc N4.** Le script du brouillon 2 a été joué deux fois sur le brouillon 2 par le rédacteur du brouillon 3, chacun depuis un dossier temporaire vide neuf : sortie `calcul-profil-bras-meta-v1-brouillon2.sortie.txt` `c4b4d8106b63c7b44e1124f028167a43e8933e7f38eaf19cd119e788a133c2f2`, identique octet pour octet aux deux rejeux ; les sections 1 à 7 de la sortie v3 lui sont identiques, ligne de titre exceptée. Scripts et sorties sont versés sans compagnon (aucun droit d'en écrire) : compagnons à écrire au scellement (R6). Renvois « sortie § n » : sections de la sortie v3.
- **Non vérifié (réserve R1, inchangée du brouillon 1)** : DEP10 exige les verdicts des collisionneurs des questions 4 à 7 rendus et scellés ; d'après R-678 et la question v10 des nœuds (N6), la question 6 est rendue sans Kimi (synthèse en cours) et la question 7 sur 3 cellules. À vérifier avant la contre-lecture qui précède le scellement.

## Résumé (douze lignes)

1. **Constat pour Lazar, en tête (CA1-05, nœud N4, non tranché ici)** : aux paramètres du brouillon 1 (bande [2 ; 3], canal faible ≤ 1), 4 paires de niches sur 15 sont dans le profil et n5 (bornes et théorie) n'y a aucun partenaire (CA1-03) ; sous la loi par axe de cette annexe, un lot de 10 fiches contient au moins une paire du profil avec 0,55 et la paire méta retenue y est avec 0,55 ; à 6 fiches, 0,27 et 0,25 (fourchette de P(≥ 1) : 0,37–0,85 à 10 fiches, 0,15–0,54 à 6). Le pré-pilote éprouverait donc souvent le seul repli, **plus souvent que ne le disent les chiffres posés au collisionneur** : zéro paire du profil 0,73 contre 0,59–0,67 à 6 fiches, 0,45 contre 0,25–0,36 à 10 ; sous la loi du brouillon 1, le script retrouve ces derniers (0,60 et 0,25 ; table 0.2 bis).
2. **Options (section 0)** : (a) accepter le repli comme mesure ; (b1) bande [2 ; 4] ; (b2) bande retirée ; (c1) quinze fiches en passe 1 ; (c2) réunir passe 1 et passe « tableau » ; (d1) canal ≤ 2 ; (d2) toucher le profil de R-638 (non chiffrée). Probabilités, effets et coûts en table 0.2.
3. **Recommandation** : (b1) avec la lecture de (a) (repli déclaré quand il joue) ; confiance 0,55 ; **option : demander au collisionneur** (déjà posé en N4). Sous la loi par axe, (b1) porte P(≥ 1) de 0,27 à 0,49 à 6 fiches et de 0,55 à 0,84 à 10, sans coût ; sous la loi du brouillon 1, le gain n'est que de 0,06 et 0,05.
4. **Grille** (S29 a) : six niches inchangées, portée restreinte aux cases des axes 1 à 5 (CA1-14) ; règle nouvelle pour les affirmations mixtes de l'axe 1 (lecture d'activations agrégée dans le temps : n2 par défaut ; CA1-01).
5. **Accord (S28)** : kappa ≥ 0,40 ; Jaccard ≥ 0,30 ; inchangés, lus par `accord_s28` (v54).
6. **Canal** (S29 b) : table inchangée ; c(n1, n2) = 1 gardé, limite et contrôle « même axe » écrits (CA1-01).
7. **Structures** (S29 c) : 20 structures inchangées ; règle du lecteur qui retire **toute** structure imposée par le texte I à toutes les fiches (CA1-04, incohérence corrigée) ; compter ou non les jeux de données reste au bloc N4 (écart à R-638, mot de Lazar).
8. **Désaccord** : lu par paire après le choix, au plus 5 paires, ≤ 0,25 USD hors devis (I-13) ; écart à M9 déclaré (CA1-10).
9. **Éloignement** (S29 d) : table inchangée ; la borne basse ne joue sur aucune paire et n'est pas fondée sur Uzzi (CA1-07) ; bande au bloc N4.
10. **Score et repli** (S29 e, f) : inchangés ; nouvelle limite d'interprétation (le score favorise les paires faciles à fusionner, CA1-08).
11. **Jeu d'essai neuf** : non vide et non plein sous les 18 variantes du bloc N4 (1 à 7 paires du profil sur 41 de niches différentes), éprouvé par le code réel v55 (section 6) ; le texte exact de l'annexe aussi (sortie § 9).
12. **Code v55** : format lu vérifié, sur des blocs réécrits et sur le texte exact ; refus avec « À REMPLIR » ; acceptation une fois remplis ; I-1 à I-10 traités par v54 et v55 ; restent I-11 (chiffré ici), I-13 (dépense), I-14 (grille par case, nouvelle).

## 0. Constat CA1-05 et options (nœud N4 ; non tranché ici)

### 0.1 Le constat

Le profil exige trois choses à la fois : canal faible entre les deux niches, structure comptée partagée par les deux fiches, éloignement dans la bande. Canal et éloignement sont des propriétés de la **paire de niches** ; seules 4 paires de niches sur 15 passent les deux aux valeurs du brouillon 1 (n1–n2, n1–n4, n1–n6, n3–n4). Le pré-pilote n'a qu'une case et au plus 10 fiches non aiguillées de la passe 1 (deux par axe, texte I, « Déroulé »). La contre-lecture a mesuré, sous la loi a priori du brouillon 1 et deux lois voisines, zéro paire du profil avec 0,59 à 0,67 à 6 fiches et 0,25 à 0,36 à 10.

**Ce que cette annexe change dans la prédiction** (toutes hypothèses SUPPOSÉ ; script, section 6) :
- **loi par axe** (CA1-06) : la niche d'une fiche dépend de son axe (axe 1 : n2 0,50, n1 0,25, n3 0,20, n4 0,05 ; axe 2 : n5 0,55 ; axe 3 : n6 0,45 ; axe 4 : n6 0,70 ; axe 5 : n5 0,80 ; détail dans le script) ; marges : n1 0,16, n2 0,17, n3 0,09, n4 0,05, n5 0,27, n6 0,26 (sortie § 10). Les axes 2, 4 et 5 pèsent : n5 et n6 deviennent fréquentes, alors que le brouillon 1 leur donnait 0,15 et 0,05, et n1 devient plus rare (0,16 contre 0,30) ;
- les fiches d'un lot sont tirées sans remise parmi deux places par axe ;
- **paires prises** (I-11, CA1-09) : le rang du bras méta est tiré (premier, deuxième ou troisième, un tiers chacun) ; un bras basique (produit avec 0,99, paire sur deux axes différents) ou Gu-Krenn (produit avec 0,9) placé avant lui prend une paire tirée au hasard (SUPPOSÉ), qui sort des candidates du méta. **Simplification déclarée** : quand le méta est deuxième, le script place toujours le basique avant lui ; avec Gu-Krenn une fois sur deux à cette place, P(méta) bouge d'au plus 0,0006 (sortie § 13, tirages communs) ;
- **même axe** (CA1-01) : part des paires méta du profil dont les deux fiches viennent du même axe.

Deux grandeurs par option : **P(≥ 1)** = probabilité qu'un lot contienne au moins une paire du profil ; **P(méta)** = probabilité que la paire méta retenue soit dans le profil, après les paires prises. Scénario principal : loi par axe, accord des deux lecteurs par fiche 0,7, structure partagée 0,3, indépendance ; CA1-04 option A. Fourchette : lois {par axe, brouillon 1, « n6 fort », « n2 fort »} × structure {0,15 ; 0,3 ; 0,5} ; « n6 fort » et « n2 fort » sont des reconstructions (les vecteurs de la contre-lecture ne sont pas versés) ; chaque cellule a sa propre graine, d'où des écarts de 0,01 avec le scénario principal.

### 0.2 Options

| Option (lettre N4 du collisionneur) | Paramètres changés | P(≥ 1) à 6 / 10 fiches (fourchette) | P(méta) à 6 / 10 | P(≥ 1) sous la loi du brouillon 1, structure 0,3 | Effet sur le pré-pilote | Coût |
|---|---|---|---|---|---|---|
| **(a)** accepter le repli comme mesure — N4 (a) | aucun : bande [2 ; 3], canal ≤ 1 ; 4 paires de niches sur 15 ; n5 sans partenaire | 0,27 [0,15 ; 0,54] / 0,55 [0,37 ; 0,85] | 0,25 / 0,55 | 0,40 / 0,75 | éprouve la chaîne (lecture, paire, fusion, aiguilleur, juges) ; le profil dans une minorité de lots à 6 fiches, un sur deux à 10 ; résultat nommé « méta : profil ou repli » ; les fiches rangées en n5 (sous la loi supposée : 0,55 des fiches de l'axe 2, 0,80 de l'axe 5) ne sont jamais dans le profil (CA1-03) | 0 USD ; aucun changement de plan |
| **(b1)** bande [2 ; 4] — nouvelle | bande [2 ; 4] : seule l'extrémité e = 5 est exclue ; 6 paires sur 15 (n4–n5, n5–n6 en plus) ; seule n2–n5 reste exclue comme extrême | 0,49 [0,27 ; 0,65] / 0,84 [0,58 ; 0,93] | 0,47 / 0,83 | 0,46 / 0,80 | idem, profil plus souvent éprouvé (n5–n6 : 0,45 des paires méta du profil ; n4–n5 : 0,08 ; sortie § 10) ; n5 a deux partenaires (règle CA1-03) ; « non extrême » lu comme « pas le cran maximal de l'échelle » | 0 USD |
| **(b2)** bande retirée ([2 ; 5]) — N4 (c) | 7 paires sur 15 | 0,58 [0,33 ; 0,73] / 0,90 [0,68 ; 0,96] | 0,56 / 0,90 | 0,53 / 0,86 | gain sur (b1) de 0,09 à 6 fiches et 0,06 à 10, par la seule paire extrême n2–n5 (0,23 des paires méta du profil) ; **contraire à R-638** (« éloignement non extrême ») : modification de revendication, nœud de Lazar | 0 USD |
| **(c1)** quinze fiches en passe 1 — N4 (b) | aucun dans l'annexe ; plan : passe 1 à 15 fiches (12 à 15 non aiguillées) | à 12 / 15 : 0,66 [0,48 ; 0,92] / 0,79 [0,63 ; 0,97] | 0,66 / 0,79 | 0,85 / 0,94 (à 12 / 15) | **le texte I limite Kimi à deux fiches par axe** (10 sur les axes 1 à 5) : il faut un second proposeur en passe 1 ou un changement du texte I ; M5 et M8 changent ; préenregistrement brouillon 11, script v10, nouvelle contre-lecture | ≈ +2,77 USD ; É2 dépasse son relais (2,89 → 4,34 pour 3,0) : devis et GO |
| **(c2)** réunir passe 1 et passe « tableau » — nouvelle | aucun dans l'annexe ; M9 : fiches non aiguillées des deux passes de Kimi (≤ 20) | réunies à 12 / 20 : 0,66 [0,48 ; 0,92] / 0,91 [0,81 ; 1,00] ; **avec la perte de la passe « tableau » (0,53)** : 0,45 (passe 1 à 6) / 0,72 (à 10) | 0,44 / 0,71 (avec la perte) | 0,85 / 0,99 (réunies à 12 / 20) | la passe « tableau » est retirable et perdue avec 0,53 (préenregistrement brouillon 10, résumé point 3) ; mêle des fiches écrites avec et sans tableau (M8 en dépend) ; M9 et É7b à réécrire | ≈ +1,50 USD de lectures d'étiquettes (É7b 1,50 → 3,00 pour un relais souple de 1,0) |
| **(d1)** canal ≤ 2 — N4 (d) | seuil 2 ; 10 paires sur 15 | 0,55 [0,35 ; 0,79] / 0,88 [0,70 ; 0,97] | 0,53 / 0,87 | 0,65 / 0,93 | « faible » couvre 13 paires sur 15 : il ne distingue plus rien ; le profil devient « structure partagée hors extrêmes » | 0 USD |
| **(d2)** modifier le profil de R-638 — N4 (e) | non chiffrée | — | — | — | décision du directeur à rouvrir | — |

Médianes du nombre de paires du profil par lot (forme de P14) : (a) 0 à 6 fiches, 1 à 10 ; (b1) 0 et 2 ; (b2) 1 et 3 ; (c1) 1 et 2 (à 12 et 15) ; (c2) 1 et 4 (réunies, à 12 et 20) ; (d1) 1 et 2 (sortie § 3). Coûts : arithmétique de la sortie § 7 sur les bases du devis v6 et du script v9 (pièces lues) ; (c1) = 5 fiches × (Kimi 0,2 × 1,447 + aiguilleur et second lecteur 2 × 0,057 + 6 lectures d'étiquettes × 0,025).

**Table 0.2 bis — concordance avec les chiffres de N4** (zéro paire du profil = 1 − P(≥ 1) ; à 6 puis 10 fiches).

| Option de N4 (lettre ici) | Chiffre de N4 (contre-lecture, loi du brouillon 1) | Ce script, loi du brouillon 1, structure 0,3 (sortie § 11) | Ce script, loi par axe (scénario principal, sortie § 3) |
|---|---|---|---|
| (a) repli comme mesure ((a)) | 0,59 ; 0,25 (0,59–0,67 et 0,25–0,36 sur trois lois) | 0,60 ; 0,25 (trois lois : 0,60–0,69 et 0,25–0,39) | 0,73 ; 0,45 |
| (b) quinze fiches ((c1)) | 0,06 à 15 fiches | 0,06 | 0,21 |
| (c) bande retirée ((b2)) | 0,47 ; 0,14 | 0,47 ; 0,14 | 0,42 ; 0,10 |
| (d) canal ≤ 2 ((d1)) | 0,35 ; 0,07 | 0,35 ; 0,07 | 0,45 ; 0,12 |
| bande [2 ; 4] ((b1) ; contre-lecture section C, absente de N4) | 0,54 ; 0,21 | 0,54 ; 0,20 | 0,51 ; 0,16 |

Lecture : sous la loi du brouillon 1, le script retrouve la contre-lecture à 0,01 près ; les écarts de la dernière colonne viennent de la seule loi par axe (SUPPOSÉ), qui rend fréquentes n5 (sans partenaire sous (a), (c1), (d1)) et n6 (un seul partenaire, n1), et plus rare n1. Sous cette loi, (a), (c1) et (d1) sont plus défavorables que dans N4, (b1) et (b2) plus favorables. Les reconstructions « n6 fort » et « n2 fort » ne sont pas celles de la contre-lecture (« n2 fort », option (a) : 0,61 et 0,28 ici, 0,66 et 0,34 chez elle).

**Lecture des sensibilités (sortie § 5 et § 12).** P(≥ 1) / P(méta), à 6 puis 10 fiches. Structure moins fréquente entre niches qui se parlent peu (CA1-06 a) : (a) 0,21 / 0,20 et 0,48 / 0,47 ; (b1) 0,41 / 0,39 et 0,77 / 0,76. Accord plus bas sur les axes 1 et 3, plus haut ailleurs (CA1-06 c) : (a) 0,27 / 0,26 et 0,57 / 0,56 ; (b1) 0,56 / 0,54 et 0,89 / 0,89. c(n1, n2) relevé à 2 (CA1-01) : (a) 0,20 / 0,19 et 0,45 / 0,44 ; (b1) 0,43 / 0,42 et 0,78 / 0,78. Sans les paires prises, P(méta) remonte à 0,26 et 0,55 sous (a), 0,50 et 0,84 sous (b1) : les paires prises coûtent au plus 0,03. Mêmes sensibilités pour (b2), (c1), (c2), (d1) : sortie § 12. **Classement (sortie § 12)** : dans tous les scénarios joués (principal, quatre lois à structure 0,3, trois sensibilités), (a) est la plus basse et (a) < (b1) < (b2) (profils emboîtés) ; (d1) dépasse (b1), sauf sous l'accord par axe, où (b1) l'égale ou la dépasse de 0,01 ; l'ordre de (b2) et (d1) dépend du scénario : (b2) passe devant sous la loi par axe (0,58 contre 0,55 à 6 fiches ; 0,90 contre 0,88 à 10) et sous l'accord par axe, (d1) sous les trois lois globales (égalité à 0,01 près sous « n6 fort » à 10 fiches) et sous la structure dépendante du canal ; sous c(n1, n2) = 2, l'écart est de 0,01. (c1) et (c2) ne se comparent pas à effectif égal : ils changent le plan.

### 0.3 Recommandation

**(b1) avec la lecture de (a)**, confiance **0,55** — **option : demander au collisionneur** (la question est déjà posée au nœud N4 ; cette annexe lui fournit les chiffres).
- Pour (b1) : ne coûte rien ; ne change ni le plan ni le texte I ; tient R-638 en excluant le cran extrême de l'échelle (e = 5 : n2–n5) ; règle CA1-03 (n5, où la loi supposée range la plupart des fiches des axes 2 et 5, retrouve deux partenaires) ; sous la loi par axe, P(≥ 1) passe de 0,27 à 0,49 à 6 fiches et de 0,55 à 0,84 à 10, et le gain vient surtout de n5–n6 (0,45 des paires méta du profil sous (b1), n4–n5 0,08 ; sortie § 10). Le repli reste déclaré quand il joue (lecture de (a)) : à 6 fiches il joue encore avec 0,53.
- Contre (b1) : e = 4 est « presque extrême » ; les tables sont écrites à la main (SUPPOSÉ) et une bande élargie après avoir vu le compte de paires est un choix de conception fait pour remplir le profil — déclaré comme tel (aucune fiche n'a été lue ; le choix précède toute donnée) ; le gain dépend de la loi par axe, elle-même SUPPOSÉ : sous la loi du brouillon 1, il n'est que de 0,06 à 6 fiches (0,40 → 0,46) et 0,05 à 10 (0,75 → 0,80) (sortie § 11), d'où la conclusion de la contre-lecture (« l'option 3 ne sert pas »).
- Pourquoi pas (c1) ou (c2) : (c1) heurte la règle de deux fiches par axe du texte I et demande devis, GO, un brouillon 11 et une contre-lecture ; (c2) n'apporte rien une fois sur deux (passe « tableau » perdue avec 0,53) et mêle deux populations de fiches. Pourquoi pas (d1) : « faible » ne veut plus rien dire. Pourquoi pas (b2) : contraire à R-638 ; son gain sur (b1) vient de la seule paire extrême n2–n5.

### 0.4 Mode d'emploi du bloc N4

Le bloc N4 (section 8, entre les marqueurs `BLOC N4 : DÉBUT` et `BLOC N4 : FIN`) contient : la ligne « version du fichier », la ligne « option retenue », le paragraphe « conséquences » (P14 de l'option, recopiée de la table 0.2), la ligne « calcul » (sortie du script joué sur le fichier et ses empreintes) et le bloc JSON `parametres_bras_meta`. Ses deux premières lignes disent quel brouillon et quelle option il porte. Pour une autre option : (1) recopier dans le bloc la ligne de la table 0.2 ; (2) appliquer au JSON les clés `remplace` de la variante (bloc `variante_bloc_n4`, section 6) — `bande` et `seuil_communication_faible` pour CA1-05, `structure_forte` pour CA1-04 — et écrire les deux identifiants dans `option_ca1_05` et `option_ca1_04` ; (3) rejouer deux fois le script v3 (il éprouve la variante écrite, ses artefacts et le texte exact, et imprime l'empreinte du texte hors bloc N4) ; (4) écrire dans le bloc la sortie et ses empreintes, et vérifier que l'empreinte du texte hors bloc N4 est celle qu'écrit le bloc N4 du brouillon 3. Rien d'autre ne change : les sections 0 à 7 et 9 à 13 sont écrites pour toutes les options ; le jeu d'essai est non vide et non plein sous les 18 combinaisons. Sous (c1) ou (c2), l'annexe ne change que par ce bloc ; le préenregistrement, lui, change (M9, effectifs, É2 ou É7b, devis).

## 1. Grille fermée des niches (S29 a)

**Portée (CA1-14).** Cette grille vaut pour les fiches des **axes 1 à 5 de la question « défense »** : la case unique du pré-pilote et, en course 2, génération 1, les cases de ces axes. Elle **ne couvre pas l'axe 7** (angles sur tout le contrôle : élicitation, conscience d'évaluation, débat, délégation, argumentaires de sûreté…), ni un autre texte que le texte I : pour ces cases, le préenregistrement de la course doit fournir une annexe de grille scellée (version 1 bis) ou déclarer le bras méta « non produit (hors portée de la grille) » ; le code v55 ne connaît qu'une grille pour toutes les cases (I-14, section 10).

**Proposition (À GELER par Lazar ; inchangée).** Six niches. Une fiche reçoit la niche **de la communauté dont la méthode porte son affirmation centrale** (champ « hypothèse » du texte I), pas celle de son axe ni de son matériau secondaire. Définitions et mots-indices : table ci-dessous, recopiée mot pour mot dans `definitions_niches` du bloc N4 (servies au lecteur par le code, `bisociateur.meta.definitions = "annexe"`, I-4).

| Identifiant | Définition en une ligne | Mots-indices (un indice ne suffit pas) |
|---|---|---|
| `n1_detection_sequentielle` | statistique séquentielle : décider au fil de la trajectoire qu'une loi a changé, avec fausse alerte tenue à tout instant | somme cumulée, test séquentiel du rapport de vraisemblance, e-valeur, test valide à tout instant, temps d'arrêt, délai de détection |
| `n2_lecture_activations` | lire ou modifier les activations internes d'un modèle à poids ouverts pour en tirer un signal | sonde linéaire, direction, couche, jeton lu, auto-encodeur parcimonieux, intervention ou ablation sur activations |
| `n3_anomalies_hors_distribution` | détecter ce qui s'écarte d'une loi de référence apprise, sans modèle de l'écart, en une fois | distance de Mahalanobis, estimation de densité, seuil conforme, score d'anomalie, rejet hors distribution |
| `n4_moniteurs_et_protocoles` | surveiller un agent par un autre modèle et organiser l'audit autour de lui | moniteur par modèle, juge, budget d'audit, rééchantillonnage, édition, report, collusion |
| `n5_bornes_et_theorie` | énoncés prouvés : impossibilités, garanties, bornes d'information ou de délai | borne, impossibilité, garantie, divergence, théorie de l'information, preuve dans Lean |
| `n6_science_evaluation` | concevoir et lire des bancs de comparaison : transfert, familles tenues à l'écart, puissance, robustesse au changement de loi | banc, famille tenue à l'écart, transfert, universalité, puissance simulée, préenregistrement |

**Retraits d'indices par rapport au brouillon 1 (neuf ; liste complétée au brouillon 3).** Imposés par le texte I à toutes les fiches ou à toutes celles d'un axe, donc sans pouvoir de distinguer les niches (CA1-01) : « plancher apparié » (n2 ; axe 1 (c)), « agrégation dans le temps » (n1 ; axe 1), « calibration » (n3 ; le glossaire impose calibrage, seuil et vérification sur trois jeux disjoints), « classe de lois déplacées » (n5 ; glossaire, « famille »). Retirés sans être imposés : « équipe rouge » (n6 ; recouvrement n4–n6 relevé par la contre-lecture, section B ; le texte I ne la nomme que comme angle de l'axe 7), « chaîne de raisonnement lue » (n4) et « angle mort » (n5) — le brouillon 2 les disait imposés par le texte I, je ne les y trouve pas (il ne cite qu'une « théorie des angles morts ») ; retrait gardé, il ne change aucune définition. Doublons, non listés au brouillon 2 : « dictionnaire de caractéristiques » (n2 ; « auto-encodeur parcimonieux ») et « environnement de comparaison » (n6 ; « banc »). « Couche » et « sonde linéaire » restent des indices de n2 alors que la contre-lecture les dit imposés à l'axe 1 : ils définissent la niche ; leur effet sur l'axe 1 est absorbé par le défaut n2 de la règle des affirmations mixtes ci-dessous.

- Raison : (i) les six communautés couvrent les familles de méthodes des axes 1 à 5 (axe 1 : statistiques et agrégateurs ; axe 2 : lois, garanties ; axe 3 : failles ; axe 4 : universalité ; axe 5 : théorie ; matériau : Mahalanobis, auto-encodeurs, e-valeurs, seuils conformes) ; (ii) à 10 fiches au plus, six niches évitent à la fois les cases vides et la plupart des paires « même niche » (refusées) ; (iii) la règle « méthode de l'affirmation centrale » sépare la niche de l'axe (D-e). **Les niches ne sont pas de même nature** (méthode pour n1, n2, n3 ; type d'énoncé pour n5 ; situation pour n4 ; tâche pour n6) : relevé par la contre-lecture, assumé et déclaré ; une grille homogène demanderait la carte des chapelles (R-637).
- Alternatives : (b) cinq niches, n1 et n2 fusionnées (« boîte blanche séquentielle », la fusion du programme) — avantage : supprime le bruit d'étiquette n1/n2 sur l'axe 1 (CA1-01) ; inconvénient : le profil perd n1–n2, qui est précisément le trou que le programme parie exploiter (0,32 des paires méta du profil sous (a), 0,16 sous (b1) ; sortie § 10) ; effet sur P(≥ 1) non chiffré ; (c) quatre niches (n1 + n5, n2 + n3) — avantage : accord plus haut ; inconvénient : presque toutes les paires deviennent « même niche ». **Correction CA1-02** : le brouillon 1 écrivait que l'alternative à quatre niches (sa lettre (b), ici (c)) ferait perdre « la paire la plus nette (lecture des activations contre bornes) » ; or cette paire (n2–n5, c = 0, e = 5) est **hors profil sous toutes les options sauf (b2)**, exclue comme extrême : c'est une conséquence voulue de la lecture d'Uzzi (section 5), pas une perte.
- Confiance : 0,45.

**Règle pour les affirmations mixtes (À GELER par Lazar ; nouvelle, CA1-01).** Une fiche de l'axe 1 propose presque toujours une statistique qui lit des activations **et** s'agrège dans le temps. Sa niche est celle de l'élément que la fiche déclare comme **source d'avantage** (champ « source d'avantage (L) ou élément manquant à l'antériorité la plus proche ») : n1 si l'avantage revendiqué est l'agrégation séquentielle (délai, fausse alerte tenue à tout instant), n2 s'il est le signal lu (couche, direction, invariance), n3 s'il est le score d'écart à une loi apprise ; **si la fiche ne le dit pas, n2**. Raison : le défaut unique range ensemble les fiches ambiguës de l'axe 1 (même niche : paire refusée par le bras méta), au lieu de fabriquer une paire « loin » n1–n2 par bruit d'étiquette. Alternative : laisser le choix au lecteur (brouillon 1) — inconvénient : deux fiches voisines de l'axe 1 rangées chacune de façon stable en n1 et en n2 font une paire du profil. Confiance : 0,5. **Contrôle (journal, 0 USD, après É9)** : pour la paire méta et chaque paire du profil, « même axe » oui/non (l'axe est dans la fiche). Part prédite des paires méta du profil dont les deux fiches viennent du même axe (sortie § 3) : (a) 0,11, dont n1–n2 0,05 ; (b1) 0,07, dont 0,02 ; (b2) 0,06, dont 0,02 ; (c1) 0,14, dont 0,06 ; (c2) 0,15 à 0,16, dont 0,07 ; (d1) 0,10, dont 0,02.

**Règle de lecture (À GELER par Lazar ; inchangée sur le fond).** Deux lecteurs neufs, isolés l'un de l'autre et du dépôt, qui ne connaissent ni les règles ni les bras (M9, A4) ; une fiche par appel ; **une niche exactement**, prise dans la grille (pas de « autre », pas d'« indécidable » ; niche hors grille ou deux niches : lecture rejetée, garde R5 ligne 23). **Une fiche n'entre au bras méta que si les deux lecteurs lui donnent la même niche** (`bisociateur.meta.regle_divergence = "fiche_ecartee"`, I-5) ; ses structures sont l'**union** des deux lectures (`bisociateur.meta.structures = "union"`). Raison : une niche disputée ne fabrique pas de paire « loin ». Alternative : niche du premier lecteur (`premier_lecteur`) — avantage : effectif plus grand ; inconvénient : une erreur de lecture suffit à fabriquer une paire « loin ». Confiance : 0,6. **Biais déclaré** : l'union favorise les fiches à nombreuses étiquettes (contrôle descriptif, section 7).

**Format exact de la réponse du lecteur (CA1-13 ; à recopier dans la consigne figée).** Un bloc JSON clôturé :
`{"niche": "<un identifiant de la grille>", "structures": ["<identifiant>", "<identifiant>"], "affirmation_centrale": "<une phrase>"}`.
Chaque structure est **un identifiant de la liste fermée, écrit tel quel** (chaîne) ; la forme `{"type": "<identifiant>", "nom": "<identifiant>"}` est aussi acceptée, à condition que `nom` recopie `type`. Le code v54 (`valider_niche_v54`) **rejette** la lecture entière (comptée, jamais corrigée en silence) si une structure est hors liste ou si son nom diffère de son identifiant (I-1). Liste vide permise (aucune structure : Jaccard selon la règle de S24).

**Accord exigé (S28 ; À GELER par Lazar ; inchangé).** Kappa de Cohen sur la niche ≥ **0,40** ; Jaccard moyen des structures ≥ **0,30** (fiche sans structure chez les deux lecteurs exclue et comptée ; chez un seul, Jaccard 0). Lus dans le bloc N4 (`accord_min_niche_kappa`, `accord_min_structures_jaccard`) par `seuils_s28` avec `bisociateur.meta.s28 = "annexe"`, calculés par `accord_s28` (v54). Raison : repère S24 ; garde grossière (erreur-type du kappa de l'ordre de 0,3 à 10 fiches, SUPPOSÉ). Alternative : 0,50 et 0,40 — inconvénient : « niches non lisibles » deviendrait l'issue la plus probable (P14 : kappa 0,5 [0,2 ; 0,8]). Confiance : 0,4. Conséquence (M9, inchangée) : sous S28, bras marqué « niches non lisibles », gardé (R-638), nœud joint à la demande de GO de la course sans l'empêcher.

**Marges dégénérées (inchangé ; codé dans `kappa_niches`).** Les deux lecteurs constants sur tout le lot : kappa lu 1 si leurs niches coïncident, 0 sinon, grille marquée « dégénérée sur ce lot » ; un seul lecteur constant : formule ordinaire.

**Aucune paire de niches différentes parmi les fiches retenues (I-7 traité par v54 ; cause de la v55 ajoutée au brouillon 3).** Le code donne trois causes (`course2_v54._notes`, `course2_v55._notes`) : moins de deux fiches retenues, « non produit (moins de 2 fiches étiquetées) » (v55) ; une seule niche pour toutes les fiches retenues, « non produit (niches indistinctes sur ce lot) », réserve « grille dégénérée », O15 ouverte ; autre cas, « non produit (aucune paire éligible) ». Chacune : « non lancé », compté dans C12 ; pas un échec de garde. Probabilité des trois réunies (le script ne les sépare pas) : 0,028 à 6 fiches, 0,001 à 10, sous toutes les options à deux places par axe (elle ne dépend pas de la bande ; sortie § 3).

## 2. Communication faible (S29 b)

**Ce qui tient lieu de citations (inchangé).** Le pré-pilote n'a ni citations ni graphe. La communication est une **propriété de la paire de niches**, lue dans la littérature du sous-domaine et fixée avant toute fiche : le « canal » de la réponse 2 v2 (capacité d'échange : personnes, revues, conférences, vocabulaire), distinct du flux et de la distance de contenu.

**Proposition (À GELER par Lazar ; table inchangée).** Table c(n_a, n_b) écrite à la main, échelle 0 à 3 (0 : aucun échange connu ; 1 : échanges rares ; 2 : échanges réguliers ; 3 : même communauté en pratique), SUPPOSÉ ; seuil « faible » au bloc N4 (1 sauf option (d1)).

| c (canal) | n2 activations | n3 anomalies | n4 moniteurs | n5 bornes | n6 évaluation |
|---|---|---|---|---|---|
| **n1 séquentiel** | 1 | 2 | 1 | 3 | 1 |
| **n2 activations** | — | 2 | 2 | 0 | 2 |
| **n3 anomalies** | | — | 1 | 2 | 2 |
| **n4 moniteurs** | | | — | 1 | 3 |
| **n5 bornes** | | | | — | 1 |

- Raison des valeurs (une par cellule, de mémoire, SUPPOSÉ) : détection séquentielle et bornes de délai forment une seule tradition statistique (3) ; moniteurs et bancs d'évaluation du contrôle vivent dans les mêmes laboratoires (3) ; interprétabilité et bornes formelles ne se lisent presque pas (0). Raison du seuil 1 : 7 paires sur 15 sont « faibles » ; à 2, 13 sur 15.
- **n1–n2 (CA1-01)** : je garde c = 1. Le programme réunit détection séquentielle et lecture des activations (« boîte blanche séquentielle ») **parce que** les deux littératures se parlent peu : c'est le trou qu'il parie exploiter, donc un vrai cas du profil, pas une erreur de table. Le risque relevé par la contre-lecture est ailleurs : le bruit d'étiquette sur l'axe 1 ; il est traité par la règle des affirmations mixtes (section 1) et le contrôle « même axe ». Alternative : c(n1, n2) = 2 — effet : le profil perd n1–n2 (3 paires de niches sur 15 sous (a), 5 sous (b1) ; sortie § 1) ; P(≥ 1) 0,20 à 6 fiches et 0,45 à 10 sous (a), 0,43 et 0,78 sous (b1) (sortie § 5). Confiance : 0,5.
- Alternatives à la table : (b) table calculée sur la moisson OpenAlex de R-633 (flux observé contre attendu) — mesurée ; mais la correspondance niche → concepts est un choix à la main, et c'est un flux de citations ; (c) deux tables remplies indépendamment par deux instances de familles différentes — retire une part de l'idiosyncrasie de l'auteur. Recommandation : (a) ; si la moisson est empreintée avant le gel, une concordance de rang entre (a) et (b) est rapportée (aucune fiche lue). Confiance : 0,45 (table) ; 0,5 (seuil).

## 3. Structure commune forte (S29 c)

**Liste fermée (À GELER par Lazar ; inchangée).** 20 structures nommées en quatre types (objet mathématique `om_`, méthode `me_`, jeu de données `jd_`, protocole `pr_`) ; définitions recopiées dans `definitions_structures` du bloc N4.

| Type | Identifiants |
|---|---|
| objet mathématique | `om_martingale_e_processus` ; `om_rapport_vraisemblance_divergence` ; `om_covariance_mahalanobis` ; `om_direction_sous_espace` ; `om_somme_cumulee_temps_arret` ; `om_jeu_minimax` ; `om_graphe_causal` |
| méthode | `me_test_sequentiel_cusum` ; `me_seuil_conforme` ; `me_dictionnaire_parcimonieux` ; `me_intervention_activations` ; `me_moniteur_par_modele` ; `me_estimation_densite` ; `me_preuve_formelle` |
| jeu de données | `jd_simulateur_fige` (D1) ; `jd_donnees_publiques` (D2) ; `jd_notations_juges` (D3) |
| protocole | `pr_exclusion_famille` ; `pr_audit_budgete` ; `pr_reechantillonnage_report` |

**Règle du lecteur sur les éléments imposés (À GELER par Lazar ; nouvelle, CA1-04).** Le lecteur **ne relève une structure que si elle porte l'affirmation centrale ou la méthode propre de la fiche** ; il n'en relève **jamais** une au seul motif que le texte I l'impose : champ « données (D) » de toute fiche ; fausse alerte « comptée par épisode et tenue à tout instant » (glossaire) ; plancher apparié et sonde nulle de chaîne (glossaire, axe 1 (c)) ; trois jeux disjoints ; borne valide à tout instant de l'axe 4 (c) ; bornes classiques de délai de l'axe 5 (f). Cette règle s'applique **à tous les types**, y compris `om_martingale_e_processus`, `om_somme_cumulee_temps_arret` et `me_test_sequentiel_cusum`. Raison : le brouillon 1 retirait les jeux de données parce que presque toutes les fiches les partagent, mais gardait trois structures séquentielles imposées de la même façon (incohérence relevée, CA1-04). La règle traite toutes les structures imposées de la même manière, au niveau de la lecture, sans retirer d'identifiant de la liste : une fiche dont la méthode **est** un test séquentiel garde `me_test_sequentiel_cusum`. Alternative : retirer les trois structures séquentielles du compte (option C ci-dessous). Confiance : 0,5. Limite : la frontière « imposé / propre » est un jugement du lecteur ; l'accord S28 sur les structures la mesure en partie.

**« Forte » : nombre et types comptés (bloc N4 ; À GELER par Lazar ; écart à R-638).** Au moins **1** structure partagée (même identifiant chez les deux fiches) parmi les types comptés ; mesure s(a, b) = nombre de structures comptées partagées (`indicateurs_meta`). Trois options, posées avec CA1-05 au nœud N4 :
- **A (recommandée)** : objets mathématiques et méthodes comptés (14) ; jeux de données et protocoles lus, rapportés, non comptés. Avantage : ce qui reste compté distingue des fiches. Inconvénient : **écart à R-638**, qui nomme le jeu de données ; mot de Lazar exigé. Confiance 0,55.
- **B** : jeux de données comptés aussi (17), lecture littérale de R-638. Avantage : conforme. Inconvénient : D1 sert à presque toutes les fiches ; même avec la règle du lecteur, si le champ « données » est relevé, presque toute paire partage une structure et le profil se réduit au canal et à la bande (démontré sur le jeu d'essai : la paire e09–e10 n'entre dans le profil que sous B). Effet chiffré (structure partagée 0,85, SUPPOSÉ ; sortie § 5) : P(≥ 1) 0,47 à 6 fiches et 0,73 à 10 sous (a), 0,77 et 0,96 sous (b1).
- **C** : A sans les trois structures séquentielles (11). Avantage : ne dépend pas du jugement du lecteur sur l'imposé. Inconvénient : une fiche dont la méthode est séquentielle ne peut plus partager sa méthode ; le profil se vide (structure partagée 0,15, SUPPOSÉ ; sortie § 5 : P(≥ 1) 0,16 et 0,37 sous (a), 0,30 et 0,64 sous (b1)).
- Alternatives écartées : au moins 2 structures partagées (profil vide sur la plupart des lots).

## 4. Désaccord, lu à part (M9, L3, garde R5 ligne 24)

**Proposition (À GELER par Lazar ; inchangée sur le fond ; I-2 et I-12 traités par v54).**
- **Quand** : après le choix et le dépôt scellé des paires (fin d'É7b) ; `verifier_ordre_desaccord` (v54) arrête si une lecture est horodatée avant le dépôt des paires (artefact d'ordre, ancien I-12).
- **Sur quoi** : la paire méta retenue puis les suivantes du classement méta (profil d'abord) : `bisociateur.meta.desaccord.paires_max = 5`.
- **Par qui** : les deux lecteurs de niches, un appel par paire, avec le champ « hypothèse » des deux fiches (`champ_affirmation = "hypothèse"`), anonymes, passeport d'aiguillage exigé ; réponse fermée `oui` / `non` / `indecidable` (consigne figée empreintée, `bisociateur.meta.desaccord.consigne`).
- **Journal** : déposé au coffre (`desaccord-paires`), ouvert après É9 (A21).
- **Hors score** : `garde_desaccord_v54` (signature et valeur) en É0 ; essai R5 ligne 24 : cas sain = même score pour oui, non, indécidable ; artefact = fonction de score qui varie avec le désaccord → arrêt.
- **Écart à M9 du brouillon 10, à écrire pour Lazar (CA1-10)** : M9 dit « rapporté pour chaque paire candidate » ; l'annexe en lit **au plus cinq** (à 10 fiches, il y a jusqu'à 45 paires : 90 lectures). M9 de la version gelée doit dire « pour la paire retenue et, au plus, les quatre suivantes du classement méta ». L'entrée du lecteur est le champ « hypothèse » des fiches, non un champ « affirmation centrale » recopié par fiche (le code garde aussi ce champ, `valider_niche_v54`, pour le journal).
- **Dépense (I-13)** : 10 lectures courtes au plus, à ≤ 0,025 USD la lecture (prix d'une lecture d'étiquettes, devis v6 § 3.2, compté au prix d'Opus pour une entrée de 4 000 jetons, plus longue que celle d'une lecture de désaccord) : **≤ 0,25 USD**, absente du devis v6 et du script v9 ; à ajouter à É7b au gel (dans le plafond de GO-2026-10-31-03 ; à écrire au devis, pas à dépenser sans lui).
- Confiance : 0,7.

## 5. Bande d'éloignement non extrême (S29 d)

**Mesure (À GELER par Lazar ; table inchangée).** e(n_a, n_b) = distance de contenu entre les deux niches (objets étudiés et vocabulaire), échelle 1 à 5, table à la main, SUPPOSÉ ; distincte du canal.

| e (contenu) | n2 activations | n3 anomalies | n4 moniteurs | n5 bornes | n6 évaluation |
|---|---|---|---|---|---|
| **n1 séquentiel** | 3 | 2 | 3 | 2 | 3 |
| **n2 activations** | — | 2 | 3 | 5 | 3 |
| **n3 anomalies** | | — | 3 | 3 | 3 |
| **n4 moniteurs** | | | — | 4 | 2 |
| **n5 bornes** | | | | — | 4 |

**Bande** : au bloc N4 ; [2 ; 4] sous (b1), la recommandation ; [2 ; 3] sous (a), (c1), (c2), (d1) ; [2 ; 5] sous (b2). Inégalité triangulaire tenue (contre-lecture).

**Ce que dit Uzzi et ce qu'il ne dit pas.**
- **Vérifié sur PDF** (`docs/sources/pdf/bisociation-fertilite-v1/uzzi-mukherjee-stringer-jones-2013-science.pdf` `532970985650d07fe69c66d912dfae96d6f45522fcb72e92c88857f4fd101173`, empreinte recalculée au brouillon 3 ; lu par le brouillon 1 et la contre-lecture ; pages citées par eux, non relues par les rédacteurs des brouillons 2 et 3) : succès = article dans les 5 % les plus cités à 8 ans (p. 469) ; « peak impact occurred in the 85th to 95th percentile of median conventionality, an exceptionally high level » et, en légende de la figure 4, « after which the relationship reverses » (p. 471).
- **Nuance (CA1-07)** : chez Uzzi, la cloche porte sur la **conventionnalité médiane** des combinaisons de références ; la **nouveauté de queue** est favorable à tout niveau. Rien chez Uzzi ne fonde l'exclusion du quasi identique, ni un chiffre de bande. **SUPPOSÉ (transposition)** : je n'en retiens qu'une forme — l'optimum n'est pas à l'extrême lointain — d'où l'exclusion du cran maximal de l'échelle (e = 5) sous toutes les options sauf (b2), et de e = 4 sous (a), (c1), (c2), (d1).
- **Borne basse (CA1-07)** : e_min = 2 ne joue sur **aucune** paire (aucune paire de niches différentes n'a e = 1 dans la table) ; elle n'est pas fondée sur Uzzi ; elle n'exprime qu'une raison de conception (deux niches de contenu quasi identique ne font pas un trou), SUPPOSÉ. Sous (a), la bande effective est **e = 3** : les 4 paires du profil ont toutes e = 3.
- Références non vérifiées (Yegros-Yegros 2015, Dunbar, Shi et Evans 2023 ; CA1-11) : **retirées de l'argument** ; aucune n'est citée comme appui tant qu'elle n'est pas vérifiée sur PDF empreinté (R7).
- Confiance : 0,4 (table) ; bande : voir table 0.2.

## 6. Score, repli, non-vacuité, prédiction P14 (S29 e, f ; garde 22a)

**Forme (À GELER par Lazar ; inchangée).** score méta(a, b) = 1[c ≤ seuil] × 1[s ≥ 1] × 1[e dans la bande] × (1 + **poids** × s), **poids = 0,5** (≥ 0, contrôlé par v54, I-6) ; paire méta = argmax ; égalités par `pp2-bisoc-meta`. Raison : dans le profil, préférer la paire qui partage le plus de structures, sans faire entrer une paire hors profil. Alternative : poids 0 (égalités au tirage). Confiance : 0,5. **Limite d'interprétation (CA1-08)** : voir section 7.

**Repli (À GELER par Lazar ; inchangé).** `indicateurs_puis_structure`, seul admis par le code : sans paire du profil, la paire retenue satisfait le plus d'indicateurs, puis partage le plus de structures, égalités au tirage ; comptée « hors profil ». Le code range toujours une paire du profil avant toute paire hors profil. Confiance : 0,8.

**Non-vacuité (garde 22a ; rejouée en É0 par `verifier_non_vacuite`, I-10).** Jeu d'essai **neuf**, 10 fiches étiquetées à la main par le rédacteur du brouillon 2 (aucune fiche réelle), écrit pour que le profil soit non vide et non plein **sous les 18 variantes du bloc N4** (6 options de CA1-05 × 3 de CA1-04). Le jeu du brouillon 1 ne l'était pas : ses cinq paires du profil ne partageaient que des structures séquentielles et le profil se vidait sous l'option C (A20 en É0). La paire e07–e08 (n3–n4, canal 1, éloignement 3, seuil conforme partagé) est dans le profil sous toutes les variantes ; e01–e05 (canal 3) est hors profil sous toutes. Témoins : e09–e10 (jeu de données et protocole seuls : dans le profil sous B seulement) ; e05–e06 (n5–n2, e = 5 : dans le profil sous (b2) seulement) ; e01–e04 (deux structures séquentielles : hors profil sous C). Ces six affirmations ont été recomptées à la main au brouillon 3 sur le jeu ci-dessous ; elles concordent avec la sortie § 2.

```json
{"jeu_essai_non_vacuite": {
 "e01": {"niche": "n1_detection_sequentielle", "structures": ["om_somme_cumulee_temps_arret", "me_test_sequentiel_cusum"]},
 "e02": {"niche": "n2_lecture_activations", "structures": ["om_direction_sous_espace", "me_intervention_activations", "me_seuil_conforme"]},
 "e03": {"niche": "n4_moniteurs_et_protocoles", "structures": ["me_moniteur_par_modele", "om_martingale_e_processus"]},
 "e04": {"niche": "n6_science_evaluation", "structures": ["jd_simulateur_fige", "pr_exclusion_famille", "om_somme_cumulee_temps_arret", "me_test_sequentiel_cusum"]},
 "e05": {"niche": "n5_bornes_et_theorie", "structures": ["om_rapport_vraisemblance_divergence", "om_somme_cumulee_temps_arret", "me_preuve_formelle"]},
 "e06": {"niche": "n2_lecture_activations", "structures": ["om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis"]},
 "e07": {"niche": "n3_anomalies_hors_distribution", "structures": ["om_covariance_mahalanobis", "me_seuil_conforme"]},
 "e08": {"niche": "n4_moniteurs_et_protocoles", "structures": ["me_moniteur_par_modele", "me_seuil_conforme", "pr_audit_budgete"]},
 "e09": {"niche": "n1_detection_sequentielle", "structures": ["me_test_sequentiel_cusum", "jd_simulateur_fige"]},
 "e10": {"niche": "n6_science_evaluation", "structures": ["jd_simulateur_fige", "pr_exclusion_famille"]}
}}
```

Résultat (code réel v55, sortie § 2 et § 9) : les 18 variantes passent `verifier_non_vacuite`. Paires du profil parmi les 41 paires de niches différentes (4 paires de même niche refusées) : (a), (c1) et (c2) : 3 sous A, 4 sous B, 1 sous C ; (b1) : 4, 5, 1 ; (b2) : 5, 6, 2 ; (d1) : 6, 7, 4 ; hors profil, 34 à 40. Argmax toujours dans le profil : e01–e04 (score 2,0) sous A et B ; sous C, e07–e08 ((a), (b1), (c1), (c2)), e05–e06 ((b2)), e02–e07 ((d1)), à 1,5. Sur le texte exact de l'annexe (variante écrite au bloc N4), même résultat que sa variante en sortie § 2.

**Variantes du bloc N4 (lues par le script ; clés `remplace` à appliquer au bloc).**

```json
{"variante_bloc_n4": {
 "ca1_05": {
  "a": {"libelle": "accepter le repli comme mesure", "n4_collisionneur": "(a)", "remplace": {"bande": [2, 3], "seuil_communication_faible": 1}},
  "b1": {"libelle": "bande [2 ; 4] : seule l'extrémité e = 5 exclue", "n4_collisionneur": "nouvelle", "remplace": {"bande": [2, 4], "seuil_communication_faible": 1}},
  "b2": {"libelle": "bande retirée", "n4_collisionneur": "(c)", "remplace": {"bande": [2, 5], "seuil_communication_faible": 1}},
  "c1": {"libelle": "quinze fiches en passe 1 (plan ; paramètres de a)", "n4_collisionneur": "(b)", "remplace": {"bande": [2, 3], "seuil_communication_faible": 1}},
  "c2": {"libelle": "passe 1 et passe tableau réunies (plan ; paramètres de a)", "n4_collisionneur": "nouvelle", "remplace": {"bande": [2, 3], "seuil_communication_faible": 1}},
  "d1": {"libelle": "canal faible = c <= 2", "n4_collisionneur": "(d)", "remplace": {"bande": [2, 3], "seuil_communication_faible": 2}}
 },
 "ca1_04": {
  "A": {"libelle": "objets mathématiques et méthodes comptés ; jeux de données et protocoles lus, non comptés (écart à R-638)", "remplace": {"structure_forte": {"nombre_min": 1, "types": ["om_martingale_e_processus", "om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis", "om_direction_sous_espace", "om_somme_cumulee_temps_arret", "om_jeu_minimax", "om_graphe_causal", "me_test_sequentiel_cusum", "me_seuil_conforme", "me_dictionnaire_parcimonieux", "me_intervention_activations", "me_moniteur_par_modele", "me_estimation_densite", "me_preuve_formelle"]}}},
  "B": {"libelle": "jeux de données comptés aussi (R-638 à la lettre)", "remplace": {"structure_forte": {"nombre_min": 1, "types": ["om_martingale_e_processus", "om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis", "om_direction_sous_espace", "om_somme_cumulee_temps_arret", "om_jeu_minimax", "om_graphe_causal", "me_test_sequentiel_cusum", "me_seuil_conforme", "me_dictionnaire_parcimonieux", "me_intervention_activations", "me_moniteur_par_modele", "me_estimation_densite", "me_preuve_formelle", "jd_simulateur_fige", "jd_donnees_publiques", "jd_notations_juges"]}}},
  "C": {"libelle": "A sans les trois structures séquentielles", "remplace": {"structure_forte": {"nombre_min": 1, "types": ["om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis", "om_direction_sous_espace", "om_jeu_minimax", "om_graphe_causal", "me_seuil_conforme", "me_dictionnaire_parcimonieux", "me_intervention_activations", "me_moniteur_par_modele", "me_estimation_densite", "me_preuve_formelle"]}}}
 }
}}
```

**Prédiction P14 refaite (garde 22a ; indicative ; remplace la ligne « paires dans le profil » de P14 au gel).** Hypothèses, toutes SUPPOSÉ : loi par axe (section 0.1) ; accord par fiche 0,7 ; structure partagée par paire 0,3 ; indépendances ; paires prises par les bras antérieurs (basique 0,99 sur deux axes différents, Gu-Krenn 0,9), tirées au hasard ; poids sur s ignoré pour la part « même axe ». Valeurs par option : table 0.2 ; valeur de l'option retenue : bloc N4. **Pourquoi ces chiffres diffèrent du brouillon 1 et de la contre-lecture** : loi par axe au lieu d'une loi globale (n5 et n6 fréquentes, n1 plus rare), tirage sur deux places par axe, paires prises comptées (I-11), indices et règle des affirmations mixtes (axe 1 : n2 par défaut). Sous la loi globale du brouillon 1, le script retrouve les chiffres de la contre-lecture à 0,01 près pour (a), (b1), (b2), (d1) et quinze fiches (table 0.2 bis ; sortie § 11). Cette loi n'est pas la « fourchette basse » : le minimum de chaque fourchette vient de la structure 0,15, sous la loi par axe pour (a), (c1), (c2), (d1), sous « n2 fort » pour (b1), sous la loi du brouillon 1 pour (b2) ; le maximum vient de la structure 0,5, sous la loi du brouillon 1 pour (a), (c1), (c2), sous « n2 fort » pour (d1), sous la loi par axe pour (b1) et (b2) (sortie § 11).

**Calcul et rejeu.** Script et sortie : en-tête (« Calcul ») et bloc N4 (nom de la sortie, empreintes, rejeux, empreinte du bloc de paramètres et du texte hors bloc N4) ; la sortie dépend de l'option écrite.

**Erreur-type citée (CA1-11).** Le brouillon 1 renvoyait à la « sortie v6 » une erreur-type d'environ 0,2 pour une aire à 6 contre 6 : ce chiffre n'y est pas. Hanley et McNeil (1982), aire 0,5, 6 contre 6 : **0,173** (sortie § 6 ; formule seule, aucun PDF lu ; la contre-lecture trouvait ≈ 0,17).

## 7. Garde-fous de la synthèse, transposés ; limites d'interprétation ; journal

La synthèse v2 (décision 1) rend six garde-fous obligatoires **sur littérature réelle**. Dans la course, le bras méta choisit une paire de fiches à fusionner ; l'issue est lue par l'aiguilleur, les juges, l'antériorité et les tests de mort. Transposition (À GELER par Lazar ; confiance 0,6) :

| Garde-fou | Dès la génération 1 ? | Forme dans la course |
|---|---|---|
| Étiquette de pont indépendante du canal | oui, transposée | l'issue d'une fusion n'utilise ni c, ni e, ni la niche, ni le score ; c et e sont fixés avant toute fiche et jamais recalés |
| Rétrodiction inversée | non (littérature réelle) | journal : score méta sous permutation tirée des niches entre fiches pour la paire retenue (placebo descriptif) |
| Graphe amputé des ponts | non (littérature réelle) | journal : paire méta recalculée sans s et sans bande (quel indicateur a décidé) |
| Bras « popularité seule » | **aucun équivalent** (correction CA1-08) | le bras basique n'est **pas** un bras de popularité : il note par axe et par concept. Contrôle descriptif à la place : nombre de structures et de concepts des fiches retenues par chaque bras contre la moyenne du lot |
| Jeux disjoints | oui, transposée | paramètres scellés avant toute fiche (A9, A20) ; aucun ajustement entre générations sans annexe v2 scellée |
| Puissance préalable | oui | P14 refaite (section 6) ; dans la course, aucune comparaison méta contre basique sans calcul de puissance préenregistré (à 12 fusions par bras, une aire à 6 contre 6 a une erreur-type d'environ 0,17, section 6) |

**Limite d'interprétation nouvelle (CA1-08).** Le score croît avec le nombre de structures partagées ; deux fiches qui partagent des structures se fusionnent plus facilement en une fiche cohérente ; les juges notent la cohérence entre champs. Une avance du bras méta sur le bras basique dans la course peut donc venir de ce lien mécanique, non d'un « trou » fertile. **Règle** : toute comparaison méta / basique de la course rapporte s pour les paires des trois bras et lit la différence à s égal (stratifiée ou ajustée), préenregistrée ; sans cela, elle n'est pas lue comme effet du profil. Au pré-pilote, aucune comparaison (R-634).

**Les trois défauts relevés au collisionneur (inchangés).** Pic de variance : aucune variance de taux de passage n'est lue comme criticité sans surdispersion entre réplicats ou nul d'urne, préenregistrés. Sur-additivité : aucune quantité R(A ∪ B) − R(A) − R(B) + R(A ∩ B) n'est calculée sur les fusions. Retour à la moyenne et étiquette circulaire : le profil ne lit aucun flux observé sur les fiches ; une annexe v2 qui recalerait c ou e sur les passages devra tester la rétrodiction inversée sur les générations suivantes.

**Journal dès la génération 1 (À GELER par Lazar ; confiance 0,6 ; programme, 0 USD, lu après É9).**
1. par fiche : axe, niche de chaque lecteur, retenue ou non, structures de chaque lecteur ;
2. par lot : comptes par niche ; paires éligibles ; paires du profil ; cause si aucune ; pour **chaque** paire éligible, les trois indicateurs, s, le score, le rang, **et « même axe »** (CA1-01) ;
3. s des paires retenues par les trois bras (CA1-08) ;
4. désaccord des paires lues (section 4) ;
5. par fusion : parents, bras, case, génération ;
6. graphe fiche → fusion → fiche cumulé : part de la plus grande composante faiblement connexe, nombre de composantes, profondeur de la plus longue cascade, rapport de branchement (analogies seulement ; Bettencourt et Kaiser 2015, p. 3, vérifié par la réponse 3 v2) ;
7. passages par bras, comptés, sans comparaison au pré-pilote.
Attendus en génération 1, déclarés : cascade ≤ 1 par construction ; composante géante triviale. Lignes de base, non résultats ; tout énoncé d'« allumage » attend la génération 2 et un préenregistrement (R-642, R-878).

## 8. Format lisible par le code ; bloc N4

**Contrat du code v55 (vérifié sur le code et par le script).** `course2_v55.declarer_bras_v55` appelle `bisociateur_v55.lire_annexe_meta_v55(chemin, sha256, definitions, texte_consigne_lecteur, brouillon_relu, rapport)`, qui enchaîne :
1. `bisociateur_v53.lire_annexe_meta` : fichier présent, compagnon `.sha256` conforme, empreinte égale à `bisociateur.meta.annexe.sha256` ; **dernier** bloc JSON portant `parametres_bras_meta` ; onze clés (`niches`, `types_structure`, `communication`, `seuil_communication_faible`, `structure_forte`, `eloignement`, `bande`, `poids`, `repli`, `contre_lecture`, `approbation_lazar`) ; **les deux derniers refusés s'ils sont vides ou contiennent « À REMPLIR »** ; tables définies pour chaque paire de niches, clé = deux identifiants triés joints par « | » ; repli connu ; bande ordonnée ;
2. `bisociateur_v54.lire_annexe_meta_v54` : types et signes (I-6 : poids ≥ 0, réels finis, `nombre_min` entier ≥ 1, types comptés ⊆ liste) ; `contre_lecture` cite **deux** empreintes SHA-256 distinctes et `approbation_lazar` un `R-NNN` (I-9) ; avec `definitions = "annexe"`, une définition non vide par niche et par structure (`definitions_niches`, `definitions_structures`, I-4) ; jeu d'essai lu (`jeu_essai_non_vacuite`) ;
3. v55 (I-9 sur pièces) : `bisociateur.meta.annexe.brouillon_relu` et `.rapport_contre_lecture` (`{chemin, sha256}`) présents, empreintes recalculées, **toutes deux citées dans `contre_lecture`**, distinctes ; `R-000` refusé ; **brouillon relu identique à l'annexe hors des deux champs** ;
puis `verifier_non_vacuite` (I-10), `garde_desaccord_v54`, `seuils_s28`. Tout refus (y compris une erreur de lecture, de clé ou de type) : bras méta « non produit (annexe non conforme) », jamais un arrêt (A20).

**Épreuve (script, sortie § 2 et § 9).** Pour chacune des 18 variantes, bloc de paramètres réécrit dans le texte : refus avec les deux champs à « À REMPLIR » (motif « annexe sans contre_lecture déclarée ») ; acceptation une fois remplis d'un texte d'essai citant les empreintes du brouillon relu et d'un rapport d'essai, avec `R-999` ; non-vacuité passée. Artefacts sur la variante écrite, tous refusés : paramètre changé après relecture, texte changé après relecture, `R-000`, une seule empreinte, poids négatif, compagnon absent, définitions absentes. **Texte exact (sortie § 9, ajout du brouillon 3)** : le fichier tel qu'il est est refusé ; une copie où seules les deux valeurs « À REMPLIR » sont remplacées est acceptée, le brouillon relu étant le fichier exact ; les paramètres et le jeu d'essai que lit le code sont ceux que lit le script ; une ligne de texte changée après relecture est refusée. Le compagnon est simulé en mémoire (aucun `.sha256` écrit).

**Configuration à écrire au gel (fragment ; empreintes à poser au scellement, jamais dans l'annexe).**
`bisociateur.meta` : `annexe` = `{chemin: ".../annexe-bras-meta-v1.md", sha256: <annexe scellée>, brouillon_relu: {chemin, sha256}, rapport_contre_lecture: {chemin, sha256}}` ; `definitions: "annexe"` ; `s28: "annexe"` ; `regle_divergence: "fiche_ecartee"` ; `structures: "union"` ; `desaccord: {paires_max: 5, champ_affirmation: "hypothèse", consigne: <pièce empreintée>}`.

**Remplissage des deux champs au scellement** : `contre_lecture` = modèle, date, chemin et empreinte du brouillon relu, chemin et empreinte du rapport (les deux empreintes en clair, 64 caractères) ; `approbation_lazar` = numéro de décision `R-NNN` de `registres/decisions.md` et date. Rien d'autre ne change dans le fichier.

<!-- BLOC N4 : DÉBUT — seul passage qui change selon l'option retenue au nœud N4 (CA1-05 et CA1-04) ; mode d'emploi en section 0.4 -->

### Bloc N4 — version du fichier, option retenue, calcul et paramètres

- **Version du fichier** : brouillon 3 de l'annexe (`annexe-bras-meta-v1-brouillon3.md`), 31 octobre 2026, écrit par le rédacteur du brouillon 3 ; nœud N4 ouvert : aucune option n'est choisie.
- **Option retenue** : CA1-05 = **(b1) bande [2 ; 4], à titre provisoire (recommandation ; À CHOISIR au nœud N4)** ; CA1-04 = **A, à titre provisoire (recommandation ; À CHOISIR au nœud N4 ; écart à R-638)**.
- **Conséquences** : 6 paires de niches sur 15 dans le profil (n1–n2, n1–n4, n1–n6, n3–n4, n4–n5, n5–n6) ; P14 (paires dans le profil méta), à recopier au gel : au moins une paire du profil dans le lot 0,49 à 6 fiches, 0,84 à 10 (fourchettes 0,27–0,65 et 0,58–0,93 ; sous la loi du brouillon 1, 0,46 et 0,80), médiane 0 et 2 ; paire méta retenue dans le profil 0,47 et 0,83 ; sinon repli, compté « hors profil » (0,53 à 6 fiches, 0,17 à 10), réserve « seul le repli éprouvé » ; aucune paire éligible 0,028 et 0,001 ; part « même axe » des paires méta du profil 0,07 (dont n1–n2 0,02) ; aucun changement de plan ni de coût.
- **Calcul joué sur ce fichier** : script `calcul-profil-bras-meta-v1-brouillon3.py` `50e0c0e13cef458a17d990c9e9c4b14594ef81d12b2942fcd1ec4bc5c6de71f3` ; sortie `calcul-profil-bras-meta-v1-brouillon3.sortie.txt` `9441c437704df960f8904e80ce977122a8d7128dc7bb447ced7047a771150838` ; rejeu 1 et rejeu 2, chacun par `python3 -I` depuis un dossier temporaire vide neuf : `9441c437704df960f8904e80ce977122a8d7128dc7bb447ced7047a771150838` et `9441c437704df960f8904e80ce977122a8d7128dc7bb447ced7047a771150838` (identiques octet pour octet) ; empreinte du bloc de paramètres en JSON canonique sans les deux champs libres (inchangée au remplissage) : `ef1eccc708002194713b1a76a0d43d6a3c3b60bc6592e1d45d0bfd0918d529cc` ; **empreinte du texte hors bloc N4** (sortie § 8 ; elle doit être la même au brouillon qui portera l'option choisie) : `13417f16c2cf1a3575796d8eff413551f31750ac712c8e389034afdd4c00d5a1` ; marqueurs restants : 0.

```json
{"parametres_bras_meta": {
 "version": "annexe-bras-meta-v1",
 "option_ca1_05": "b1",
 "option_ca1_04": "A",
 "echelle_communication": "0 à 3 (0 aucun échange connu ; 3 même communauté), table écrite à la main, SUPPOSÉ",
 "echelle_eloignement": "1 à 5 (1 objets et vocabulaire quasi identiques ; 5 sans objet ni vocabulaire communs), table écrite à la main, SUPPOSÉ",
 "portee": "fiches des axes 1 à 5 de la question défense (texte I) ; axe 7 et autres textes hors portée (I-14)",
 "regle_niche": "une niche par fiche, celle de la méthode de l'affirmation centrale ; affirmation mixte de l'axe 1 : niche de la source d'avantage déclarée, n2 à défaut ; fiche retenue au bras méta seulement si les deux lecteurs posent la même niche",
 "regle_structures": "identifiants de la liste fermée écrits tels quels ; jamais une structure relevée au seul motif que le texte I l'impose ; union des deux lecteurs",
 "accord_min_niche_kappa": 0.4,
 "accord_min_structures_jaccard": 0.3,
 "desaccord": "lu à part, par paire, après le dépôt des paires, au plus 5 paires ; n'entre jamais dans le score (R-638 ; garde R5 ligne 24)",
 "niches": ["n1_detection_sequentielle", "n2_lecture_activations", "n3_anomalies_hors_distribution", "n4_moniteurs_et_protocoles", "n5_bornes_et_theorie", "n6_science_evaluation"],
 "definitions_niches": {
  "n1_detection_sequentielle": "Statistique séquentielle : décider au fil de la trajectoire qu'une loi a changé, avec fausse alerte tenue à tout instant. Indices : somme cumulée, test séquentiel du rapport de vraisemblance, e-valeur, test valide à tout instant, temps d'arrêt, délai de détection.",
  "n2_lecture_activations": "Lire ou modifier les activations internes d'un modèle à poids ouverts pour en tirer un signal. Indices : sonde linéaire, direction, couche, jeton lu, auto-encodeur parcimonieux, intervention ou ablation sur activations. Niche par défaut d'une affirmation de l'axe 1 qui lit des activations et s'agrège dans le temps sans dire laquelle des deux est sa source d'avantage.",
  "n3_anomalies_hors_distribution": "Détecter ce qui s'écarte d'une loi de référence apprise, sans modèle de l'écart, en une fois. Indices : distance de Mahalanobis, estimation de densité, seuil conforme, score d'anomalie, rejet hors distribution.",
  "n4_moniteurs_et_protocoles": "Surveiller un agent par un autre modèle et organiser l'audit autour de lui. Indices : moniteur par modèle, juge, budget d'audit, rééchantillonnage, édition, report, collusion.",
  "n5_bornes_et_theorie": "Énoncés prouvés : impossibilités, garanties, bornes d'information ou de délai. Indices : borne, impossibilité, garantie, divergence, théorie de l'information, preuve dans Lean.",
  "n6_science_evaluation": "Concevoir et lire des bancs de comparaison : transfert, familles tenues à l'écart, puissance, robustesse au changement de loi. Indices : banc, famille tenue à l'écart, transfert, universalité, puissance simulée, préenregistrement."
 },
 "types_structure": ["om_martingale_e_processus", "om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis", "om_direction_sous_espace", "om_somme_cumulee_temps_arret", "om_jeu_minimax", "om_graphe_causal", "me_test_sequentiel_cusum", "me_seuil_conforme", "me_dictionnaire_parcimonieux", "me_intervention_activations", "me_moniteur_par_modele", "me_estimation_densite", "me_preuve_formelle", "jd_simulateur_fige", "jd_donnees_publiques", "jd_notations_juges", "pr_exclusion_famille", "pr_audit_budgete", "pr_reechantillonnage_report"],
 "definitions_structures": {
  "om_martingale_e_processus": "Objet mathématique : martingale, surmartingale, e-processus.",
  "om_rapport_vraisemblance_divergence": "Objet mathématique : rapport de vraisemblance, divergence entre lois.",
  "om_covariance_mahalanobis": "Objet mathématique : matrice de covariance, distance de Mahalanobis.",
  "om_direction_sous_espace": "Objet mathématique : direction, projection, sous-espace d'activations.",
  "om_somme_cumulee_temps_arret": "Objet mathématique : somme cumulée, marche aléatoire, temps d'arrêt.",
  "om_jeu_minimax": "Objet mathématique : jeu à deux, stratégie minimax, équilibre.",
  "om_graphe_causal": "Objet mathématique : graphe causal, intervention au sens causal.",
  "me_test_sequentiel_cusum": "Méthode : test séquentiel (somme cumulée, rapport de vraisemblance séquentiel).",
  "me_seuil_conforme": "Méthode : seuil ou ensemble conforme calibré sur des données de référence.",
  "me_dictionnaire_parcimonieux": "Méthode : auto-encodeur parcimonieux, dictionnaire de caractéristiques.",
  "me_intervention_activations": "Méthode : intervention sur activations (patching, ablation, pilotage).",
  "me_moniteur_par_modele": "Méthode : un modèle surveille un autre modèle ou un agent.",
  "me_estimation_densite": "Méthode : estimation de densité, score de vraisemblance d'une loi apprise.",
  "me_preuve_formelle": "Méthode : preuve vérifiée par machine (Lean).",
  "jd_simulateur_fige": "Jeu de données D1 : trajectoires synthétiques du simulateur figé.",
  "jd_donnees_publiques": "Jeu de données D2 : données publiques tierces.",
  "jd_notations_juges": "Jeu de données D3 : notations brutes des juges.",
  "pr_exclusion_famille": "Protocole : une famille de lois déplacées exclue à la fois.",
  "pr_audit_budgete": "Protocole : audit sous budget fixé.",
  "pr_reechantillonnage_report": "Protocole : rééchantillonnage, édition ou report d'actions suspectes."
 },
 "communication": {"n1_detection_sequentielle|n2_lecture_activations": 1, "n1_detection_sequentielle|n3_anomalies_hors_distribution": 2, "n1_detection_sequentielle|n4_moniteurs_et_protocoles": 1, "n1_detection_sequentielle|n5_bornes_et_theorie": 3, "n1_detection_sequentielle|n6_science_evaluation": 1, "n2_lecture_activations|n3_anomalies_hors_distribution": 2, "n2_lecture_activations|n4_moniteurs_et_protocoles": 2, "n2_lecture_activations|n5_bornes_et_theorie": 0, "n2_lecture_activations|n6_science_evaluation": 2, "n3_anomalies_hors_distribution|n4_moniteurs_et_protocoles": 1, "n3_anomalies_hors_distribution|n5_bornes_et_theorie": 2, "n3_anomalies_hors_distribution|n6_science_evaluation": 2, "n4_moniteurs_et_protocoles|n5_bornes_et_theorie": 1, "n4_moniteurs_et_protocoles|n6_science_evaluation": 3, "n5_bornes_et_theorie|n6_science_evaluation": 1},
 "seuil_communication_faible": 1,
 "structure_forte": {"nombre_min": 1, "types": ["om_martingale_e_processus", "om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis", "om_direction_sous_espace", "om_somme_cumulee_temps_arret", "om_jeu_minimax", "om_graphe_causal", "me_test_sequentiel_cusum", "me_seuil_conforme", "me_dictionnaire_parcimonieux", "me_intervention_activations", "me_moniteur_par_modele", "me_estimation_densite", "me_preuve_formelle"]},
 "eloignement": {"n1_detection_sequentielle|n2_lecture_activations": 3, "n1_detection_sequentielle|n3_anomalies_hors_distribution": 2, "n1_detection_sequentielle|n4_moniteurs_et_protocoles": 3, "n1_detection_sequentielle|n5_bornes_et_theorie": 2, "n1_detection_sequentielle|n6_science_evaluation": 3, "n2_lecture_activations|n3_anomalies_hors_distribution": 2, "n2_lecture_activations|n4_moniteurs_et_protocoles": 3, "n2_lecture_activations|n5_bornes_et_theorie": 5, "n2_lecture_activations|n6_science_evaluation": 3, "n3_anomalies_hors_distribution|n4_moniteurs_et_protocoles": 3, "n3_anomalies_hors_distribution|n5_bornes_et_theorie": 3, "n3_anomalies_hors_distribution|n6_science_evaluation": 3, "n4_moniteurs_et_protocoles|n5_bornes_et_theorie": 4, "n4_moniteurs_et_protocoles|n6_science_evaluation": 2, "n5_bornes_et_theorie|n6_science_evaluation": 4},
 "bande": [2, 4],
 "poids": 0.5,
 "repli": "indicateurs_puis_structure",
 "contre_lecture": "À REMPLIR",
 "approbation_lazar": "À REMPLIR"
}}
```

<!-- BLOC N4 : FIN -->

## 9. Procédure jusqu'à É0

1. **Nœud N4** (collisionneur, puis mot de Lazar) : option de CA1-05 et de CA1-04 ; consignée dans `registres/decisions.md`.
2. **Brouillon 4** = le brouillon 3 avec le bloc N4 remplacé selon la section 0.4 (même si l'option choisie est (b1) × A : la ligne « option retenue » perd « à titre provisoire » et cite la décision), et avec toute correction d'une contre-lecture du brouillon 3, si elle a lieu avant ; le script v3 rejoué deux fois sur lui (sortie nommée, empreintes au bloc). **L'empreinte du texte hors bloc N4 doit être celle du brouillon 3** (imprimée par la sortie § 8 et écrite au bloc N4 du brouillon 3) ; sinon, le brouillon 4 se relit en entier.
3. **Contre-lecture (R2)** du brouillon 4 par un sous-agent neuf d'un modèle autre qu'Opus, qui n'a écrit aucune pièce lue ici ; pièces à lui donner : brouillon 4 et son empreinte ; ce brouillon 3 et le brouillon 2 ; la contre-lecture du brouillon 1 ; le préenregistrement brouillon 10 (ou sa version gelable) ; `bisociateur_v53.py`, `bisociateur_v54.py`, `bisociateur_v55.py`, `course2_v54.py`, `course2_v55.py`, `gardes_e0_v55.py`, `outils.py` ; les scripts v2 et v3 et leurs sorties ; le texte I ; la question des nœuds (N4). Points : chaque valeur a raison, alternative, confiance ; le bloc passe le code une fois rempli et le refuse avant ; le jeu d'essai est non vide et non plein ; la sortie se rejoue ; l'empreinte du texte hors bloc N4 est celle du brouillon 3 ; la transposition d'Uzzi reste SUPPOSÉ ; les incompatibilités sont exactes. La relecture du texte hors bloc N4 peut commencer sur ce brouillon 3 avant le nœud ; le rapport cite le brouillon 4 (le code v55 exige que le brouillon relu soit le texte scellé, hors des deux champs).
4. **Mot de Lazar** sur chaque valeur de la table 11, y compris S28, l'écart à R-638 (CA1-04), la règle des affirmations mixtes, la portée (CA1-14), l'écart à M9 sur le désaccord (CA1-10) et la dépense de I-13 ; aucune valeur ne prend de défaut à 48 heures.
5. **Annexe à sceller** `annexe-bras-meta-v1.md` = brouillon relu (brouillon 4), **seuls les deux champs remplis** (le code v55 refuse tout autre écart).
6. **Scellement** : `python -m controle_ia.scellement sceller annexe-bras-meta-v1.md` ; scripts et sorties versés avec compagnons (R6).
7. **Empreintes injectées** : dans l'en-tête du préenregistrement avant son gel (D-h (a)) ; dans `bisociateur.meta.annexe` (annexe, brouillon relu, rapport).
8. **É0** : `declarer_bras_v55` ; gardes 22b, 23, 24 sur cas sain et artefact (R5) ; sans annexe conforme, A20.

## 10. Incompatibilités avec le code v55 (mise à jour)

| N° | Objet | État en v55 | Reste à faire |
|---|---|---|---|
| I-1 | nom de structure non contrôlé | **traité** (`valider_niche_v54` rejette un nom différent de l'identifiant ; garde 23) | format recopié dans la consigne (section 1) |
| I-2 | désaccord non lu | **traité** (lecture par paire après le dépôt, journal au coffre) | consigne figée du désaccord à écrire et empreinter |
| I-3 | S28 jamais calculé | **traité** (`accord_s28`, seuils lus dans le bloc) | — |
| I-4 | définitions non servies | **traité** (`definitions = "annexe"` ; clés `definitions_*` du bloc N4) | — |
| I-5 | fiche écartée si les lecteurs divergent | **traité** (`regle_divergence`) | règle écrite en mots dans M9 gelée |
| I-6 | types et signes non contrôlés | **traité** (v54 ; artefact « poids négatif » refusé, sortie § 2) | — |
| I-7 | causes « aucune paire éligible », « niches indistinctes » | **traité** (v54, comptées ; v55 ajoute « moins de 2 fiches étiquetées ») | C12 et O15 du préenregistrement à relire |
| I-8 | n = 2 | **traité** (v54 : bras de priorité 1) ; la question des nœuds (v10, sous N5) note que la v55 ne reporte pas la paire au bras suivant (choix de code 8) | lecture à geler au préenregistrement |
| I-9 | champs d'approbation non contrôlés | **traité** (v54 forme ; v55 pièces, empreintes citées, R-000, différence limitée ; texte exact éprouvé, sortie § 9) | — (ancien CA1-15) |
| I-10 | non-vacuité non revérifiée en É0 | **traité** (`verifier_non_vacuite` sur le jeu de l'annexe) | — |
| I-11 | paires prises par un bras antérieur | non traité par le code (comportement voulu, R5 ligne 16) | **chiffré ici** (P(méta) contre P(≥ 1) : au plus 0,03 d'écart ; sortie § 3, § 5, § 12, § 13) |
| I-12 | artefact d'ordre du désaccord | **traité** (`verifier_ordre_desaccord`) | — |
| I-13 | dépense du désaccord hors devis | — | ≤ 0,25 USD à écrire au devis et à É7b (section 4) |
| **I-14** (nouvelle) | une grille pour toutes les cases ; l'axe 7 n'a pas de niche (CA1-14) | le code ne connaît qu'une grille | au préenregistrement de la course : annexe 1 bis ou « non produit (hors portée de la grille) » par case, avec une cause de code (v56) |

## 11. Table récapitulative (toutes À GELER par Lazar)

| Paramètre | Valeur proposée | Alternative | Confiance |
|---|---|---|---|
| CA1-05 (bloc N4) | (b1) bande [2 ; 4], repli déclaré quand il joue | (a), (b2), (c1), (c2), (d1), (d2) — table 0.2 | 0,55 : option : demander au collisionneur |
| S29 a — grille | 6 niches, niche = méthode de l'affirmation centrale ; portée axes 1 à 5 | 5 niches (n1 + n2) ; 4 niches ; carte des chapelles | 0,45 |
| Affirmations mixtes de l'axe 1 | niche de la source d'avantage déclarée ; n2 à défaut | choix libre du lecteur | 0,5 |
| Règle de lecture | deux lecteurs, une niche forcée, fiche retenue si accord, structures en union, format exact | premier lecteur seul | 0,6 |
| S28 | kappa ≥ 0,40 ; Jaccard ≥ 0,30 ; marges constantes 1/0 « dégénérée » | 0,50 ; 0,40 | 0,4 |
| Aucune paire de niches différentes sur le lot | « non produit » avec sa cause (moins de 2 fiches étiquetées ; niches indistinctes ; aucune paire éligible), C12, O15 | échec de grille (nœud) | 0,55 |
| S29 b — canal | table 0–3 inchangée ; faible = c ≤ 1 (≤ 2 sous (d1)) ; c(n1, n2) = 1 | OpenAlex ; deux tables ; c(n1, n2) = 2 | 0,45 ; 0,5 |
| S29 c — structures | 20 structures ; règle des éléments imposés ; comptées selon CA1-04 (A recommandée) | B (R-638 à la lettre) ; C | 0,5 ; 0,55 |
| Désaccord | par paire, après le dépôt, ≤ 5 paires, ≤ 0,25 USD | chaque paire candidate (≤ 90 lectures) | 0,7 |
| S29 d — éloignement | table 1–5 inchangée ; bande selon CA1-05 | — | 0,4 |
| S29 e — score | indicateurs × (1 + 0,5 × s) ; lecture à s égal en course (CA1-08) | poids 0 | 0,5 |
| S29 f — repli | `indicateurs_puis_structure` | aucune en v55 | 0,8 |
| P14 refaite | selon l'option retenue (bloc N4 ; table 0.2) | valeurs fictives du script v9 | indicative |
| Garde-fous et journal | trois dès la génération 1, trois en journal ; « même axe » et s des trois bras ajoutés | — | 0,6 |

## 12. Traitement des constats de la contre-lecture du brouillon 1 (fait au brouillon 2, chiffré et complété au brouillon 3)

| Constat | Traitement | Où |
|---|---|---|
| CA1-01 (majeur) n1–n2 dans le profil, bruit d'étiquette sur l'axe 1 | c(n1, n2) = 1 gardé (le trou que le programme parie exploiter) ; **règle des affirmations mixtes** (source d'avantage, n2 à défaut) ; indices imposés retirés des définitions (« couche » et « sonde linéaire » gardés, absorbés par le défaut n2) ; contrôle « même axe » au journal, part prédite (0,11 sous (a), dont n1–n2 0,05 ; 0,07 sous (b1)) ; alternative c = 2 chiffrée (P(≥ 1) 0,20 et 0,45 sous (a)) | § 1, § 2, § 7, sortie § 3 et § 5 |
| CA1-02 (moyen) « paire la plus nette » exclue par la bande | phrase corrigée : n2–n5 est hors profil comme extrême, par la lecture d'Uzzi | § 1 |
| CA1-03 (majeur) n5 dans aucune paire du profil | dit en tête (résumé 1, table 0.2) ; **réglé par l'option (b1)** (n4–n5, n5–n6 : 0,53 des paires méta du profil sous (b1) à 6 fiches) ; limite déclarée sous (a), (c1), (c2), (d1) | résumé, § 0.2, bloc N4 |
| CA1-04 (moyen) jeux de données retirés, structures séquentielles gardées | **règle du lecteur sur tous les éléments imposés par le texte I** (incohérence corrigée) ; compter les jeux reste un écart à R-638 au mot de Lazar, au bloc N4 (A, B, C chiffrées : P(≥ 1) à 6 fiches sous (a) 0,27, 0,47, 0,16) | § 3, bloc N4, sortie § 5 |
| CA1-05 (majeur) profil rarement éprouvé | **non tranché** (nœud N4) : six options chiffrées par simulation, effets et coûts ; concordance avec les chiffres de N4 (table 0.2 bis) ; recommandation (b1) 0,55, option : demander au collisionneur ; annexe prête pour toute option (bloc N4 seul, contrôlé par l'empreinte du texte hors bloc) | § 0, bloc N4 |
| CA1-06 (moyen) loi a priori, indépendances | **loi par axe** dérivée du texte I ; fourchette sur quatre lois et trois probabilités de structure, détaillée par loi ; sensibilités structure dépendante du canal et accord par axe, pour toutes les options | § 0.1, § 0.2, sortie § 4, § 5, § 11, § 12 |
| CA1-07 (mineur) borne basse inopérante, Uzzi | dit : bande effective e = 3 sous (a) ; borne basse = raison de conception, non fondée sur Uzzi ; nuance « nouveauté de queue » écrite | § 5 |
| CA1-08 (moyen) score favorable aux paires faciles à fusionner ; « popularité seule » | limite d'interprétation et règle « lecture à s égal » en course ; s des trois bras au journal ; ligne « popularité seule » réécrite (aucun équivalent) | § 7 |
| CA1-09 (moyen) paires prises par un bras antérieur | **chiffré** : P(méta) contre P(≥ 1) (écart au plus 0,03) ; ordre des bras simplifié, effet ≤ 0,0006 ; I-11 | § 0.1, § 10, sortie § 3, § 5, § 13 |
| CA1-10 (moyen) désaccord : écart à M9 ; I-12, I-13 | écart écrit pour Lazar (≤ 5 paires, champ « hypothèse ») ; I-12 traité par v54 ; I-13 chiffré (≤ 0,25 USD) | § 4, § 10 |
| CA1-11 (mineur) renvoi faux à la sortie v6 ; références non vérifiées | renvoi retiré ; Hanley et McNeil calculé (0,173) ; Yegros-Yegros, Dunbar, Shi et Evans retirés de l'argument | § 5, § 6, § 7 |
| CA1-12 (mineur) script P14 non versé | scripts v2 et v3 et leurs sorties versés (compagnons au scellement), chacun rejoué deux fois à l'identique | en-tête, § 6, bloc N4 |
| CA1-13 (mineur) format des structures | format exact de la réponse du lecteur écrit (chaînes ou `{type, nom}` égaux) | § 1 |
| CA1-14 (mineur) huit cases sans niche ; axe 7 | portée restreinte aux axes 1 à 5 ; I-14 nouvelle (grille par case) | § 1, § 10 |
| CA1-15 (mineur) champ `contre_lecture` contrôlé par non-vacuité seule | réglé par le code v55 (pièces, empreintes citées, différence limitée), éprouvé sur le texte exact ; procédure réécrite en conséquence | § 8, § 9, § 10 |

Autres changements du brouillon 2 (gardés) : titre et statut écrits pour la comparaison « brouillon relu / annexe » du code v55 ; définitions des niches et des structures ajoutées au bloc (lecture `definitions = "annexe"`) ; clés `option_ca1_05`, `option_ca1_04`, `portee`, `regle_niche`, `regle_structures` ajoutées (ignorées par le code, lues par l'humain et par le script) ; clés `statut`, `valeurs_a_geler_par_lazar`, `structures_nom_impose`, `structures_lues_non_comptees` retirées (elles changeaient avec l'option ou avec le scellement) ; bloc JSON de configuration du brouillon 1 remplacé par un fragment en texte (section 8 ; il aurait porté des empreintes connues au seul scellement) ; jeu d'essai refait (robuste aux 18 variantes) ; incompatibilités mises à jour contre la v55 ; procédure réécrite (le brouillon relu doit être le texte final).

## 13. Ce qui change par rapport au brouillon 2

Les trois blocs JSON sont **inchangés** (mêmes empreintes canoniques, imprimées en tête des sorties v2 et v3) ; seule la prose change, dans le bloc N4 comme hors de lui.

| Objet | Brouillon 2 | Brouillon 3 | Où |
|---|---|---|---|
| Chiffres | 82 marqueurs entre doubles crochets (67 distincts) à la place des probabilités, des coûts, de l'erreur-type, du résultat de non-vacuité et des empreintes ; script jamais exécuté (interruption de 12:09:23 UTC, R-747) | script v2 exécuté deux fois (sortie `c4b4d810…`, rejeux identiques) ; chaque chiffre rempli depuis sa sortie ou celle du script v3 (sections 1 à 7 identiques) ; aucun marqueur ne reste (sortie § 8, garde du script) | partout |
| Classement des options | « sous toutes [les sensibilités], le classement ne change pas : (a) < (b1) ≤ (b2) < (d1) » | faux sous le scénario principal ((b2) 0,58 > (d1) 0,55 à 6 fiches ; 0,90 > 0,88 à 10) ; les sensibilités n'étaient jouées que pour (a) et (b1). Réécrit sur la sortie § 12 (sensibilités de toutes les options) | § 0.2 |
| Loi du brouillon 1 | « fourchette basse de la table » (§ 0.3 et § 6) | faux : le minimum de chaque fourchette vient de la structure 0,15, et pour (a), (c1), (c2) la loi du brouillon 1 donne au contraire le maximum (structure 0,5 ; sortie § 11). Remplacé par les chiffres par loi ; le script retrouve la contre-lecture sous sa loi, à 0,01 près | § 0.3, § 6 |
| Concordance avec N4 | absente | table 0.2 bis : chiffres de N4 contre ce script, sous la loi du brouillon 1 et sous la loi par axe ; sous la loi par axe, (a), (c1), (d1) sont plus défavorables que dans N4 (zéro paire 0,73 et 0,45 sous (a)) | résumé 1, § 0.2 |
| « Même axe » | renvoi à la table 0.2, qui n'a pas cette colonne | parts écrites par option (sortie § 3) | § 1 |
| CA1-03 | « fiches des axes 2 et 5 jamais dans le profil » | « fiches rangées en n5 » (sous la loi supposée, n5 ne prend que 0,55 des fiches de l'axe 2 et 0,80 de l'axe 5) ; dit aussi au résumé | résumé, § 0.2 |
| Un seul bloc change | trois passages hors du bloc N4 dépendaient de l'option ou du numéro de brouillon : statut (« écrit comme brouillon 2 »), § 0.4 (« il porte aujourd'hui (b1) × A »), § 6 (empreintes d'une sortie qui dépend de l'option) ; et « aucune valeur n'est gelée », « aucune valeur n'a été gelée ni tranchée » auraient été faux dans l'annexe scellée | statut et fin écrits pour rester vrais avant et après scellement ; version du fichier, sortie et empreintes du calcul déplacées dans le bloc N4 ; empreinte du texte hors bloc N4 imprimée par le script et contrôlée au brouillon suivant | statut, § 0.4, § 6, § 9, bloc N4 |
| Épreuve du code | bloc de paramètres réécrit par le script | en plus, texte exact de l'annexe : refus tel quel, acceptation d'une copie dont seules les deux valeurs changent, paramètres lus par le code = ceux du script | § 8, sortie § 9 |
| Ordre des bras (I-11) | « l'ordre des bras est tiré » | simplification déclarée (méta deuxième : basique toujours avant lui) et chiffrée (ordre uniforme : écart ≤ 0,0006, tirages communs) | § 0.1, sortie § 13 |
| Gain de (b1) ; (b2) | « vient surtout de n5–n6 » (non montré) ; (b2) « gain faible sur (b1) » | montré : n5–n6 0,45, n4–n5 0,08 des paires méta du profil ; (b2) : +0,09 et +0,06 sur (b1), par n2–n5 (0,23) (sortie § 10) | § 0.2, § 0.3 |
| Retraits d'indices | sept listés (six entrées), tous dits « imposés par le texte I » | neuf listés ; deux doublons omis ajoutés ; trois retraits dont le texte I ne parle pas (« équipe rouge », « chaîne de raisonnement lue », « angle mort ») requalifiés | § 1 |
| Causes « non produit » | deux causes | troisième cause de la v55 (« moins de 2 fiches étiquetées ») ; la probabilité du script les réunit | § 1, § 10, § 11 |
| Alternative (b) de la grille | « P(≥ 1) baisse » | non chiffré, dit tel ; part de n1–n2 donnée | § 1 |
| Question des nœuds | v9 | v10 (N4 identique) ; v11 notée | en-tête |
| Procédure | « brouillon 3 » = choix de l'option | brouillon 4 = choix de l'option, même pour (b1) × A ; contrôle par l'empreinte du texte hors bloc N4 | § 9 |
| Coûts, erreur-type | marqueurs | 2,77 ; 2,89 → 4,34 ; 1,50 ; 1,50 → 3,00 ; ≤ 0,25 ; 0,173 — arithmétique vérifiée sur les bases du devis v6 (§ 3.2) et du script v9 | § 0.2, § 4, § 6 |

*Fin. Ce texte ne gèle ni ne tranche aucune valeur ; seule la décision `R-NNN` écrite dans le champ `approbation_lazar` les gèle, et il ne vaut pas approbation.*
