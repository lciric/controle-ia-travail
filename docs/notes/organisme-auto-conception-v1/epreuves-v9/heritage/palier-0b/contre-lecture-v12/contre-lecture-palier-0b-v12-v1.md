# Contre-lecture — préenregistrement du palier 0b, version 12 (erratum du commit après le code v5) — v1

- **Auteur** : contre-lecteur neuf, modèle O. Je n'ai écrit ni contre-lu aucune version de ce préenregistrement, ni aucun code, ni aucune vérification. Pièce de travail (classe C) rendant un avis sur une pièce décisive (classe A).
- **Date** : 2026-11-20 ; `date -u` lu à 14:17Z en cours de travail.
- **Mandat** : `P/mandat-contre-lecteur-palier-0b-v12-v1.md` (`84b76af6311303d8a690e091bcd22a44ed3ac0be4ee7c49529882fd07d0892f3`), empreinte recalculée avant tout geste, égale à celle de son compagnon. P = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- **Message reçu en cours de travail** (session du compte organisme, sans changer le mandat) : « Décision de la mère (14:10Z) pour ta contre-lecture de la v12, point 4 » — (a) la remarque 5 tranchée : les règles n° 14 et 15 vont dans une pièce à part, une pièce de contrôle de la mère, écrite et scellée avant le lancement, qui porte les règles n° 14 et 15, puis après coup la règle n° 8, inscrite au registre des décisions ; la pièce du verrou garde ses quatre lignes ; textes exacts demandés ; (b) « comme pour la portée 200 » : citer `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/controle-manifeste-portee-200-par-la-mere-v1.md` (`0dcd2dc7…`) ; (c) le n° 8 lu sur le champ « commit du code » de la pièce : juste. Je l'applique au point 4 ; cette décision n'est pas encore sur `main` (§ 6, point 1).
- **Conditions** : processeur seul ; aucun tirage, aucun lancement du palier, aucune pièce d'autorisation écrite, aucun appel à un fournisseur de modèles, aucune dépense ; aucune écriture dans le dépôt, aucun commit, aucun `git fetch` (`origin/main` lu tel qu'il est, au commit `3bd027df1331bffb3ae5c2bdfcc381ec4c4a13df`) ; quatre `git show` sur `origin/main`, chacun redirigé vers mon dossier ; aucune commande de liste, aucun heredoc, aucun code en ligne ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**À corriger.** Douze corrections, aucune de fond : aucun critère, aucune valeur gelée, aucune prédiction, aucune issue, aucun seuil d'arrêt, aucune règle de signalement ne change, et la ligne du commit et sa table sont justes.

- **Rejeu** : la v12 est exactement la v11 plus les 42 remplacements du jeu (`cmp` muet) ; le différentiel du rédacteur est égal au mien hors des deux lignes d'en-tête ; il ne touche que les 42 lieux annoncés.
- **Ligne du commit** : une seule ligne commence par « - Commit du code d'analyse : » ; commit `e308b84d68a85416fab1a80b0c116858d24b85a5`, ancêtre d'`origin/main` ; le bloc qui suit est, retrait de deux espaces ôté, égal à l'octet à `table-empreintes-code-v5.txt` (58 lignes, 24 sous `src/`) ; **le lecteur d'en-tête du verrou (`graines.lire_en_tete_du_texte` du code v5), appliqué à une copie de la v12, lit ce commit et cette table** ; aucune graine dérivée.
- **Les neuf points du § 6, les deux ajouts, les trois précisions, R-4285** : portés, à la lettre, sauf un lieu du point 5 (la remarque 3 de l'annexe H, que le § 6 nomme, n'est pas touchée : C11, C12).
- **Corrections** : neuf portent la décision de la mère sur la remarque 5 et le renvoi à la portée 200 (C1, C3 à C10) ; deux, le lieu manquant du point 5 (C11, C12) ; une, une ambiguïté de B8 (C2). Un texte non exigé (NE-1, l'heure de la version 12).

## 1. Rejeu (point 1 du mandat)

- Empreintes recalculées, égales aux compagnons : mandat du rédacteur (`1485b861…`), v11 (`9faf31a3…`), v12 (`a4234028…`), jeu (`7e85da70…`), différentiel (`97c639f2…`), rapport du rédacteur (`78723282…`), rapport du code v5 (`a2966a3c…`), table (`56bddae7…`), vérification du code v5 (`0e2c46bb…`), contrôle v10 → v11 (`88c37d86…`), outil (`391db990…`), journal de l'outil de la v12 (`06f5d162…`).
- `python3 -B scripts/remplacer_texte_exact_v1.py --cible v11 --remplacements jeu --sortie <mon dossier>/rejeu-v12.md` : « FAIT : 42 remplacement(s) », sortie `a4234028486ce0d6cfe24d15e991e0bf03bd6e56397395f4b3cb53fa86d5d398` ; `cmp` avec la v12 : muet.
- `diff -u` v11 → v12 refait dans mon dossier : 252 lignes, égal au différentiel du rédacteur hors des deux lignes d'en-tête (chemins et heures). Seize blocs.
- **Lieux** (mon programme, § 8) : chaque ancre est trouvée une fois ; les 30 lignes de la v11 que le différentiel retire sont toutes sous une ancre ; les sept ancres sur des lignes non retirées (l. 23, 25, 64, 89, 445, 490, 952) sont des ajouts après une ligne reprise entière. Les lieux sont ceux du tableau du rapport du rédacteur (§ 2) : titre ; ligne de version ; date ; ligne du commit et table ; mandat et pièces ; section « Seuil » (l. 209, puce qui porte « Précisions de la version 9 ») ; B7 bis (l. 299) ; B8 (l. 323) ; garde 27 (l. 359) ; ordre des opérations (l. 377) ; « Contre-lecture » (l. 429, 445) ; annexe C (l. 490) ; réserves 24 et 25 (l. 531, 532) ; « Erratum du commit » (l. 827) ; remarque 4 (l. 917) ; annexe H, « Version 9 » (l. 938, 940, 942) ; fin du texte.

## 2. La ligne « Commit du code d'analyse » (point 2)

- `grep` : une seule ligne commence par le préfixe (l. 7), une seule le contient ; dix lignes contiennent « Commit du code d'analyse », elle et neuf renvois.
- Le seul groupe de quarante chiffres hexadécimaux entre accents graves de cette ligne est `e308b84d68a85416fab1a80b0c116858d24b85a5` ; `git merge-base --is-ancestor e308b84d… origin/main` : code 0 ; le rapport du code v5 relu sur `origin/main` a l'empreinte `a2966a3c…`.
- Le premier bloc qui suit (l. 9 à 68, une ligne vide entre la ligne du commit et l'ouverture) compte 58 lignes, toutes à deux espaces de retrait ; retrait ôté, égal à l'octet à la table (`56bddae7…`) ; 24 chemins sous `src/`.
- **Le lecteur du verrou** (`controle_v12_v1.py`, sortie `sortie-controle-v12-v1.txt`) : `lire_en_tete_du_texte` du code v5, importée de `P/code-v5/src/` (empreinte de `graines.py` `d0c0d56f…`, celle de la table), appliquée à une copie de la v12, rend le commit `e308b84d…` et une table de 58 entrées égale à la table extraite, 24 sous `src/` ; journal des graines vide. Je n'ai appelé aucune autre fonction du code.

## 3. Les neuf points du § 6, les ajouts, les précisions, R-4285 (point 3)

| point du § 6 | où la v12 le porte | jugement |
|---|---|---|
| 1 — ligne du commit, table, forme lue par le verrou (silence n° 4) | en-tête (rang 7 et table) ; B8 | juste, à la lettre ; « le commit inscrit doit être celui que portera la pièce » est écrit |
| 2 — B8 et remarque 4 : champs, heure, GO, modules, « scellée », moment, manifeste (n° 1 à 3, 5 à 8) | B8, « Version 12 » (rang 29) ; remarque 4 (rang 38, renvoi) | juste ; une ambiguïté de mots : « l'empreinte de la pièce » y a deux sens (C2) |
| 3 — NE-3, colonne hors des doses (n° 9), mots de la zone médiane (n° 10) | « Seuil » (rangs 25, 26) ; « Ce qui demande un code v5 », point 1 (rang 41) | juste ; rang 41 égal à l'octet au NE-3 du contrôle v10 → v11 (§ 5) |
| 4 — ordre plis puis permutation (n° 11) | « Précisions de la version 9 » (rang 27) | juste |
| 5 — B7 bis, garde 27, **remarque 3** (n° 12, 13) | B7 bis (rang 28), garde 27 (rang 30) | **incomplet** : la remarque 3, qui dit encore « rien ne l'appelle encore », n'est pas touchée (C11, C12) |
| 6 — « Ce qui demande un code v5 » fait ; ligne du commit et réserve 24 | rangs 40, 7, 35, 36 | juste |
| 7 — annexe C | rang 34 | juste ; 6 + 17 + 10 + 18 + 5 + 15 + 11 + 24 + 1 = 107 ; 71 + 42 = 113 ; vingt artefacts du verrou : rapport du code v5, § 3 |
| 8 — ordre des opérations, statut | rangs 31, 2 | juste ; C9 y ajoute la pièce de contrôle |
| 9 — statut, « Contre-lecture », ligne de version, NE-4 | rangs 2, 3, 32, 33, 5 | juste ; rang 5 égal à l'octet au NE-4 du contrôle v10 → v11 |

- **Ajout (a)** : porté (ligne du commit, « Forme que le verrou lit » ; annexe H, « Version 12 », § 3) ; le rapport du rédacteur écrit le compte (1), que je retrouve.
- **Ajout (b)** : `non_departagees_sans_mention` (rang 26), `seuil_d_arret` nul pour le contenu et les réunis (rang 25), les quatre clés de `lancer_etape_4` (rang 28) : portés, égaux à la vérification.
- **Précisions** : n° 2 (jour de la semaine, nombres sans zéro), n° 7 (`Graines.g` hors de `lancer_famille`), n° 13 (identité d'objet ; intégrité portée par les contrôles d'empreinte) : portées, à la lettre de la vérification.
- **R-4285** (`registres/decisions.md` sur `origin/main`, l. 4423) : citée à la lettre, « par » et le nom qui suit omis et marqués « […] » ; R-4210 (l. 4348) citée à la lettre, et elle dit « NE-3 […] et NE-4 (heure de la v11) : oui, avec l'erratum du commit » ; `GO-2026-11-20-25` (`registres/go.md`, l. 556) inchangée. Les n° 8, 14, 15 sont écrits, le n° 16 en remarque : à la lettre de R-4285 ; le détail (« à la main », `git merge-base --is-ancestor`) vient du mandat du rédacteur, et la v12 le dit.
- **Rien d'autre** : hors des lieux du § 1, rien ne change ; les phrases neuves ne changent ni critère, ni valeur gelée, ni seuil, ni règle de signalement.

## 4. Les dix remarques du rédacteur (point 4)

1. **Remarque 5 (n° 14 et 15 : pièce du verrou ou pièce à part)** — la question était juste : la pièce du verrou, lue par `graines.lire_piece`, refuse toute ligne hors des quatre champs (code v5, `graines.py`, l. 200 à 219). **Tranchée par la mère (14:10Z) : pièce à part.** Textes : C1, C3 à C10.
2. **N° 8, « champ `commit du code` » de la pièce** — juste (la mère le confirme) ; aucune correction de ce point.
3. **« Comme pour la portée 200 »** — absent de la v11, de `go.md` et de `decisions.md` : le rédacteur avait raison de ne pas l'écrire sans source. La mère donne le modèle ; empreinte vérifiée sur `origin/main` : `0dcd2dc72ff0f1db2bce7609a943c45a9848e30d3150329472c873a251d272c4`, égale à son compagnon du dépôt. Texte qui le cite : C1 (B8) et C3 (annexe H) ; le chemin et l'empreinte seuls, sans l'identifiant de session que cette pièce porte.
4. **NE-4 porté sur R-4210** — juste : R-4210 dit en propres termes « NE-4 (heure de la v11) : oui, avec l'erratum du commit », et le rapport du code v5 la cite en tête. Rien à corriger ; le garder.
5. **Détail des n° 8, 14, 15 venu du mandat** — juste, et dit dans le texte.
6. **« Le contre-lecteur du code »** — juste : le contre-lecteur du code v2 et le vérificateur du code v4 sont du modèle S (v11, l. 87 et 88), le vérificateur du code v5 aussi ; la phrase de la v12 est exacte.
7. **Remarques du § 7 du rapport du code v5 non portées** — juste : le mandat du rédacteur ne les met pas dans ce que la v12 porte ; la remarque 2 (commit de la pièce comparé au seul en-tête) est couverte par le n° 8.
8. **Forme de la date de la version 12** — juste qu'elle reprend la forme que NE-4 corrige ; l'heure du journal est connue (`2026-11-20T14:06:34Z`, journal versé, compagnon OK). **Texte non exigé NE-1** (§ 5).
9. **Comptes de l'annexe C non rejoués** — juste ; je les ai rapprochés du rapport du code v5 (§ 3, § 4) et de la vérification (§ 4) : égaux.
10. **Statut de la plume du rédacteur** — juste.

## 5. Corrections

Chaque ancien est compté une fois par `grep -c -F -e` dans la v12 (treize comptes, tous à 1). Les douze s'appliquent ensemble par l'outil sur la v12 : « FAIT : 12 remplacement(s) », sortie `bf6e40d2d7448ba5ba750d208293251bba354e2c64697c6de5015db72cf667e0` ; NE-1 par-dessus : « FAIT : 1 remplacement(s) », sortie `3617d9544aa80e8af5eb073470aacf759ba28be4a89993cb8eebf9d81e867a5d` ; ce sont des essais, non des versions. Sur les deux, le lecteur d'en-tête du verrou lit toujours une seule ligne du commit, le commit `e308b84d…` et la table des 58 (`sortie-controle-essai-corrige-v1.txt`). Jeu : `corrections-palier-0b-v12-v1.json` (C1 à C12, dans cet ordre) ; NE-1 : `texte-non-exige-palier-0b-v12-v1.json`. Règle des textes : la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord ; un programme (`verifier_textes_v1.py`) les tient égaux au jeu.

- **C1** — B8, alinéa « Version 12 » (rang 29), n° 8, 14 et 15 : la pièce de contrôle de la mère, et la portée 200.
  - Ancien : `— la mère le compare, à la main, au contrôle du manifeste, au commit du code de la pièce d'autorisation, que le verrou tient égal à celui de la ligne « Commit du code d'analyse » (silence n° 8) ; la racine de l'arbre lancé et le texte présenté sont donnés par l'appelant, aucun programme de lancement des étapes 8 et 9 n'existant encore — ils sont fixés dans la pièce d'autorisation de ces étapes (silence n° 14) ; « sur `main` » — la mère le contrôle (`git merge-base --is-ancestor`) et l'écrit dans la pièce d'autorisation (silence n° 15) ;`
  - Neuf : `— la mère le compare, à la main, au contrôle du manifeste, comme elle a contrôlé le manifeste de la mesure « portée à 200 » (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/controle-manifeste-portee-200-par-la-mere-v1.md`, `0dcd2dc72ff0f1db2bce7609a943c45a9848e30d3150329472c873a251d272c4`, sur `main`), au commit du code de la pièce d'autorisation du verrou, que le verrou tient égal à celui de la ligne « Commit du code d'analyse » (silence n° 8) ; la racine de l'arbre lancé et le texte présenté sont donnés par l'appelant, aucun programme de lancement des étapes 8 et 9 n'existant encore — ils sont fixés dans la pièce de contrôle de la mère (silence n° 14) ; « sur `main` » — la mère le contrôle (`git merge-base --is-ancestor`) et l'écrit dans cette même pièce (silence n° 15) ; **la pièce de contrôle de la mère est à part de la pièce d'autorisation du verrou, qui garde ses quatre lignes** (décision de la mère du 2026-11-20 à 14:10Z ; annexe H, « Version 12 », remarque 5) : écrite et scellée par la mère avant le lancement des étapes 8 et 9, elle porte les contrôles des silences n° 14 et 15, puis, après le lancement, au contrôle du manifeste, celui du silence n° 8 ;`
- **C2** — B8, alinéa « Version 12 » (rang 29), *L'en-tête du texte* : « l'empreinte de la pièce » y dit le champ `empreinte du texte scellé`, et, deux phrases plus loin (« l'empreinte de la pièce les fixant »), l'empreinte du fichier de la pièce ; je nomme les champs.
  - Ancien : `le commit de la pièce doit être celui de cette ligne, et l'empreinte de la pièce celle du texte présenté, recalculée.`
  - Neuf : `le commit de la pièce (champ `commit du code`) doit être celui de cette ligne, et l'empreinte qu'elle porte (champ `empreinte du texte scellé`) celle du texte présenté, recalculée.`
- **C3** — annexe H, « Version 12 », § 2, silence n° 8 : la portée 200 et la pièce de contrôle.
  - Ancien : `**La mère le compare, à la main, au contrôle du manifeste, au commit du code de la pièce d'autorisation**, que le verrou tient égal à celui de la ligne « Commit du code d'analyse » de ce texte.`
  - Neuf : `**La mère le compare, à la main, au contrôle du manifeste, au commit du code de la pièce d'autorisation**, que le verrou tient égal à celui de la ligne « Commit du code d'analyse » de ce texte, **comme elle a contrôlé le manifeste de la mesure « portée à 200 »** (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/controle-manifeste-portee-200-par-la-mere-v1.md`, `0dcd2dc72ff0f1db2bce7609a943c45a9848e30d3150329472c873a251d272c4`, sur `main` : pour chaque point, l'attendu, ce que porte le manifeste, et s'ils sont égaux) ; elle écrit ce contrôle dans sa pièce de contrôle (remarque 5 ci-dessous).`
- **C4** — annexe H, « Version 12 », § 2, silence n° 14.
  - Ancien : `**Ils sont fixés dans la pièce d'autorisation de ces étapes.**`
  - Neuf : `**Ils sont fixés dans la pièce de contrôle de la mère, à part de la pièce du verrou (remarque 5 ci-dessous).**`
- **C5** — annexe H, « Version 12 », § 2, silence n° 15.
  - Ancien : `**La mère le contrôle (`git merge-base --is-ancestor`) et l'écrit dans la pièce d'autorisation.**`
  - Neuf : `**La mère le contrôle (`git merge-base --is-ancestor`) et l'écrit dans sa pièce de contrôle (remarque 5 ci-dessous).**`
- **C6** — annexe H, « Version 12 », § 2, titre de la remarque 5.
  - Ancien : `- **Remarque 5 — non tranchée, portée à la mère : où s'écrivent les contrôles des silences n° 14 et n° 15.**`
  - Neuf : `- **Remarque 5 — portée à la mère et tranchée par elle (décision du 2026-11-20 à 14:10Z, au cours de la contre-lecture de cette version) : où s'écrivent les contrôles des silences n° 14 et n° 15.**`
- **C7** — annexe H, « Version 12 », § 2, fin de la remarque 5 : la décision.
  - Ancien : `le point touche ce que la mère écrit au lancement des étapes 8 et 9, après le GO de Lazar sur le palier.`
  - Neuf : `le point touche ce que la mère écrit au lancement des étapes 8 et 9, après le GO de Lazar sur le palier. **Décision de la mère** : dans une pièce à part, non dans la pièce du verrou, qui garde ses quatre lignes et sa forme (B8, « Version 12 ») : **la pièce de contrôle de la mère**, écrite et scellée par elle avant le lancement des étapes 8 et 9, porte les contrôles des silences n° 14 (la racine de l'arbre lancé et le texte présenté de ces étapes) et n° 15 (« sur `main` », contrôlé par `git merge-base --is-ancestor`), puis, après le lancement, au contrôle du manifeste, celui du silence n° 8 (le champ `commit` du manifeste comparé au champ `commit du code` de la pièce du verrou, comme pour la portée 200) ; ce qui s'écrit après le scellement s'écrit sous un nom neuf, la pièce scellée restant intacte (règle R12) ; la pièce est inscrite au registre des décisions. Ce texte n'en fixe ni le chemin ni la forme. Les mots « ce texte ne tranche pas » se disent de la version 12 rendue.`
- **C8** — ligne de version (rang 2), fin de la phrase en gras.
  - Ancien : `et là où la lettre des décisions ne suffit pas, le point est écrit en remarque, sans être tranché (annexe H, « Version 12 », remarque 5).**`
  - Neuf : `et là où la lettre des décisions ne suffisait pas, le point a été écrit en remarque et porté à la mère, qui l'a tranché au cours de la contre-lecture : les contrôles des silences n° 14 et 15, puis celui du n° 8, s'écrivent dans une pièce de contrôle de la mère, à part de la pièce d'autorisation du verrou (annexe H, « Version 12 », remarque 5).**`
- **C9** — ordre des opérations, point 2 (rang 31).
  - Ancien : `puis, après le GO de Lazar sur le palier, la pièce d'autorisation du verrou, écrite par la mère (B8).`
  - Neuf : `puis, après le GO de Lazar sur le palier, la pièce d'autorisation du verrou, écrite par la mère (B8), et la pièce de contrôle de la mère, écrite et scellée par elle avant le lancement des étapes 8 et 9 (annexe H, « Version 12 », remarque 5).`
- **C10** — section « Contre-lecture », alinéa « Version 12 » (rang 32).
  - Ancien : `la remarque 5 de l'annexe H (« Version 12 ») est portée à la mère.`
  - Neuf : `la remarque 5 de l'annexe H (« Version 12 ») est portée à la mère (elle l'a tranchée au cours de la contre-lecture de cette version : pièce de contrôle de la mère, à part de la pièce du verrou).`
- **C11** — annexe H, « Version 9 », remarque 3 (lieu que nomme le point 5 du § 6 du rapport du code v5) : renvoi.
  - Ancien : `La garde ne contrôle que le registre servi à chaque bras : aucun critère, aucune mesure rapportée n'en dépend.`
  - Neuf : `La garde ne contrôle que le registre servi à chaque bras : aucun critère, aucune mesure rapportée n'en dépend. **Version 12** (silence n° 12 du rapport du code v5) : le programme de lancement de l'étape 4 est `etapes.lancer_etape_4`, qui appelle `etape_4_jeu_de_la_garde_27` après les bras 1 à 3, dans le même appel (B7 bis, « Version 12 ») ; ce que la garde compare est dit à la garde 27 (B9, « version 12 ») ; « rien ne l'appelle encore » se dit du code v4.`
- **C12** — annexe H, « Version 12 », § 1, ligne 5 du tableau, colonne « où ».
  - Ancien : `| n° 12, 13 | B7 bis ; B9, garde 27 |`
  - Neuf : `| n° 12, 13 | B7 bis ; B9, garde 27 ; remarque 3 |`

**Texte non exigé (tenue).**

- **NE-1** — ligne de date, l'heure de la version 12 (journal versé : `2026-11-20T14:06:34Z`), du modèle de NE-4.
  - Ancien : `version 12 le 2026-11-20 (`date -u` à 14:00Z en cours de travail ; l'heure exacte est au journal de l'outil)`
  - Neuf : `version 12 le 2026-11-20, à 14:06Z (heure du journal de l'outil : 14:06:34Z ; `date -u` à 14:00Z en cours de travail)`

## 6. Pour la mère

1. **La décision de 14:10Z n'est pas sur `main`** (dernière ligne de `decisions.md` lue : R-4287, 14:01:55Z). C1, C6, C7 la citent par son heure. Recommandation : l'inscrire au registre avant le scellement ; la citation par l'heure suffit (si la mère veut le numéro, la vérification des corrections l'ajoute après l'heure). Confiance élevée.
2. **« Écrite et scellée avant le lancement … puis après coup la règle n° 8 »** : une pièce scellée ne se réécrit pas (R12). C7 écrit donc que le complément d'après le lancement s'écrit sous un nom neuf, la pièce scellée restant intacte. Recommandation : garder cette clause, le contrôle d'après le lancement prenant la forme de la note de la portée 200 (un tableau : attendu, manifeste, égal). Confiance moyenne à haute ; si la mère l'entend autrement, la clause se retire de C7 seule.
3. **Chemin et forme de la pièce de contrôle** : le texte ne les fixe pas (C7 le dit). Aucun critère, seuil ni graine n'en dépend. Recommandation : les fixer dans la ligne du registre qui inscrit la décision, avant le lancement. Confiance moyenne.
4. **NE-4** : à garder (lettre de R-4210). **NE-1** : à prendre, du même modèle. Confiance élevée.
5. **La version suivante** : ces corrections font un texte neuf (R12) ; sa tenue (titre, ligne de version, alinéa de la section « Contre-lecture ») n'est pas dans mes textes. Recommandation : le rédacteur applique C1 à C12 (et NE-1) à la lettre par l'outil, plus la tenue, et la vérification des corrections se fait sur son différentiel. Confiance élevée.

## 7. Écarts et gestes

- Message de la session du compte organisme reçu en cours de travail (décision de la mère de 14:10Z) : appliqué au point 4 ; il n'étend pas mes interdits. Il m'a fait lire un fichier de plus sur `origin/main` (la note de la portée 200 et son compagnon).
- Quatre `git show origin/main:…` redirigés vers mon dossier : `registres/decisions.md` (`19eda597…`, la ligne R-4285 inchangée depuis la lecture du rédacteur, faite à `ed74b95e…`), `registres/go.md` (`766a63e7…`, égal à celui du rédacteur), le rapport du code v5 (`a2966a3c…`), la note de la portée 200 (`0dcd2dc7…`) et son compagnon (un cinquième appel, pour ce compagnon). Aucun `git fetch` : `origin/main` lu tel qu'il était (`3bd027df…`).
- Lancés : l'outil de remplacement (le rejeu, puis mes deux essais, sorties dans mon dossier) ; mes trois programmes (`controle_v12_v1.py`, `controle_essai_corrige_v1.py`, `verifier_textes_v1.py`) et un programme de lecture (`deplier_jeu_v1.py`, qui plie le jeu du rédacteur pour le lire). Du code v5, seul le module `graines` (et, par l'import, `constantes`, le `__init__.py` du paquet et `numpy`) est chargé, et seule `lire_en_tete_du_texte` est appelée, sur des copies.
- Commandes `sed -n`, `awk` et `grep -o` sur des fichiers nommés, pour lire des lignes de la v11, de la v12 et des registres ; aucune recherche sur un dossier.
- Aucun identifiant de modèle dans cette pièce ni dans mes jeux ; la copie de travail de `decisions.md` en porte, elle n'est pas rendue.

## 8. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/`, chacun avec son compagnon :
- `contre-lecture-palier-0b-v12-v1.md` (cette pièce) ;
- `corrections-palier-0b-v12-v1.json` (C1 à C12) ; `texte-non-exige-palier-0b-v12-v1.json` (NE-1) ;
- `controle_v12_v1.py` et sa sortie `sortie-controle-v12-v1.txt` ; `controle_essai_corrige_v1.py` et sa sortie `sortie-controle-essai-corrige-v1.txt` ; `verifier_textes_v1.py` et sa sortie `sortie-verifier-textes-v1.txt` ;
- fichiers de travail, non rendus : `rejeu-v12.md` et son journal, `diff-v11-v12-rejoue.diff`, `copie-v12-pour-lecteur-d-en-tete.md`, `essai-v12-corrige.md`, `essai-v12-corrige-avec-ne.md` et leurs journaux, `deplier_jeu_v1.py`, `jeu-deplie-lecture.txt`, `decisions-main.md`, `go-main.md`, `rapport-code-v5-main.md`, `controle-manifeste-portee-200-main.md` et le compagnon du dépôt.

*Contre-lecteur neuf, modèle O.*
