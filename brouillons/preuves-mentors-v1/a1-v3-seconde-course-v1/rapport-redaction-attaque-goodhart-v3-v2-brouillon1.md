# Rapport de rédaction — A1-v3, seconde course : préenregistrement version 2, brouillon 1

3 novembre 2026, de 07:54 à 08:51 UTC (heures relevées par `date -u`) : premier assemblage à 08:29 UTC ; complément du directeur
(audit A9 rendu, sept points) reçu vers 08:33 UTC ; assemblage final à 08:50 UTC ; épreuve finale de 08:50:30 à 08:50:31 UTC ;
rapport réécrit à partir de 08:45 UTC. Rédacteur neuf : il n'a écrit ni le texte scellé d'A1-v3 (v1), ni ses brouillons, ni leurs
contre-lectures, ni le code v3 ou v3.1, ni la vérification du lanceur, ni l'audit A9. Copie de travail isolée du dépôt public
`/home/claude/wt/a1-v3-seconde/` (tête `eaa74ca`) ; dépôt privé `/home/claude/controle-ia-travail` en lecture seule. Aucun commit,
aucun fichier `.sha256`, aucun `git fetch`, `checkout`, `stash` ni `reset`, aucun fichier existant modifié, rien sous `donnees/`,
aucun appel de réseau ni de modèle, jamais `--moteur reel` ; calculs sous `nice -n 10 python3 -I -B`.

## 1. Verdict

1. Le brouillon 1 de la v2 est écrit : la v1 scellée avec les seuls changements de sa section 0.6 (36 lignes : 28 de la consigne,
   7 pour les points de la section 8 de l'audit A9, 1 pour la source du registre de la première course). **Aucun marqueur** : celui
   de l'audit A9 est rempli par l'audit rendu (`ed078aaa…`, cause d'infrastructure établie, aucune lecture utile, 4,245753 USD). Le
   lanceur du commit `9776ed0` refuse le brouillon sans compagnon et l'**accepte** avec un compagnon simulé en mémoire (73 empreintes
   vérifiées) : renommé `prereg/preenregistrement-attaque-goodhart-v3-v2.md` et scellé, il serait lu.
2. **Point bloquant pour la course, trouvé par l'épreuve** : le registre des GO de `main` du dépôt privé (`e12540bf`, cité par la
   consigne, et `db454552`, plus récent) est **refusé en entier** par le lecteur du lanceur — « registre des GO : identifiant
   GO-2026-10-24-07 en double », seize identifiants en double —, pour GO-2026-11-03-01 comme pour GO-2026-11-02-21. La copie de la
   première course (`53985197…`, audit A9, section 1) est le registre de la branche `canal/conv-audit-n04` au commit `e9d7b78d…`,
   non celui de `main` ; sur cette branche, la ligne neuve est recopiée et le registre est accepté. Le texte exige un registre accepté
   et laisse le choix du commit au directeur (section 4, point (1 bis)) ; décision D-A en section 7.
3. Deux autres utilisations d'Argon sont accordées pour le même jour : la course Heimersheim (GO-2026-11-03-02, chez la même fille)
   et deux appels seuls Astra et Argon (GO-2026-11-03-03) ; la règle « Argon seul » les veut finies, relais arrêtés par identifiant
   de processus, avant le départ (D-B).

## 2. Fichiers neufs

| fichier | sha256 |
|---|---|
| `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v2-brouillon1.md` (1 856 lignes) | `c76ac6bc9e1f94a05962bac3f0d4667f0705d2f2e07db7853923e43160370d29` |
| `orchestrator/prereg/diff-attaque-goodhart-v3-v1-vers-v2-brouillon1.txt` (`diff -u` depuis `orchestrator/`, 636 lignes, 19 blocs ; appliquée par `patch` à la v1, elle rend le brouillon octet pour octet) | `9dd6d2ffd6c789cb13e67b309ad4ce05a9a395ee9e19bc094241140ff551160e` |
| `orchestrator/prereg/rapport-redaction-attaque-goodhart-v3-v2-brouillon1.md` (ce rapport) | donnée avec la remise |

Déclaré : ces trois fichiers ont été écrits une première fois de 08:29 à 08:33 UTC (brouillon `2bed4c99…`, avec le marqueur), puis
réécrits avant remise pour intégrer le complément du directeur ; la première forme est gardée dans le bloc-notes (ci-dessous).

Bloc-notes du rédacteur, `/home/claude/scratch/a1-v3-seconde-redacteur/` (hors des deux dépôts) :

| fichier | rôle | sha256 |
|---|---|---|
| `assembler_v2b1.py` | v1 + couples ; unicité de chaque « ancien » ; aucun marqueur ; empreintes à l'assemblage | `a7fa57ee4386a8872e0c79b836c1cf481a7edd2cbf83ff2c248f6c9c7e013b17` |
| `changements_v2b1.py` | les 36 couples et les passages neufs (état final, après la retouche de l'intitulé du point 4 de la section 13) | `a37810394a6a4123145689e22181ed514cb513a242d2c614635175d836f815bc` |
| `complement_a9_v2b1.py` | complément du directeur, 28 remplacements (marqueur rempli, sept points) | `73de7d14d0e086e7fd8a98de8530ecfd03bf8782b37142d11be12a89c35e3ec9` |
| `complement_a9_v2b1_suite.py` | complément, 5 remplacements dans la liste des couples (sections 4, 12, 13) | `f71da1861f0638ee8e5a656157ed94180c0f706731ff8b402b0daff34594ae67` |
| `epreuve_lanceur_v2b1.py` | épreuve de lecture par le lanceur (point 4 de la consigne) | `dc3a7fabee2f705f9fa1f79a8aca4b384cb974f3a943674875de6faabe6f6fed` |
| `registre-go-factice.md` | en-tête + ligne GO-2026-11-03-01 recopiée sans retouche | `19eb48609643eee991cc6e82cf51c36cfa8935523923f4855f746444e782aa86` |
| `sorties/brouillon1-final-complement.md` | sortie de l'assembleur (= brouillon de la copie de travail) | `c76ac6bc9e1f94a05962bac3f0d4667f0705d2f2e07db7853923e43160370d29` |
| `sorties/couples-v1-vers-v2b1-final.json` | couples appliqués, ligne d'application | `82a854ca61b37af76a9373de83500b541098cf00573b419e759becc114d2da28` |
| `sorties/epreuve-v2b1-final.json` | sortie complète de l'épreuve finale | `386b6cd3b893d385e11681d73daf1f6ca8676b6437ecb20c301d359a6cb0c2cc` |
| `sorties/epreuve-v2b1-final.txt` | résumé imprimé de l'épreuve finale | `13dad1924517323d38107abe21cd74cdbb36800ea818f2cfb272c5913356dc3c` |
| `sorties/refs-avec-go-0301.txt` | références du clone privé dont `registres/go.md` porte la ligne | `0ebf983637a0e4f564aabd6402824042e463b2647dee7ae8fe72abb854f3a4d1` |
| `sorties/historique-doublons-main.txt` | doublons d'identifiants sur 60 commits de `main` (lecture seule) | `7cade2937e24b17252e2db3f9a9228f21d8f8428356c62382653e093051cf88c` |
| `sorties/brouillon1-avec-marqueur-0829.md` | premier assemblage, avec le marqueur (preuve du refus) | `2bed4c99f3a9d44a7e060288ad482b7530c01d772ffd8053b3d5d145d634c0dc` |
| `sorties/epreuve-v2b1-avec-marqueur.json` / `.txt` | épreuve de ce premier assemblage | `9e9e84ac47217c7442c9cd7ed2bbe934bb7770cd48932031e83769837e529192` / `a3ca5ce5238aaabefe243c05396793e314a9a735fb929b1141d73674e2b12ea9` |
| `sorties/couples-v1-vers-v2b1-avec-marqueur.json` | couples du premier assemblage | `ece2326eceb71538e0553305c3334ca7926476431bf81f7ceaf54942d2143443` |
| `sorties/changements_v2b1-avant-complement.py` | fichier des couples avant le complément | `82ac8327602451caf4dd866a4fcdb220db0b276003833c14539c7d01fd85c6ee` |

Arbre de l'épreuve : `/home/claude/scratch/a1-v3-seconde/` = `orchestrator/` du commit `9776ed0efee97146182ff2c4b409e5ec224a0bbf`
extrait par `git archive … | tar -x --strip-components=1 --exclude='*.sha256'` (aucun fichier `.sha256` dans l'arbre ; lanceur
`87d52ace…`, cœur `cb9cffe7…`), plus la copie du brouillon sous `prereg/preenregistrement-attaque-goodhart-v3-v2.md`. Les autres
sorties (`*provisoire*`, `brouillon1-essai.md`, `brouillon1-final.md`) sont des étapes, sans valeur de remise.

## 3. Ce qui change et pourquoi

La v2 est la v1 (`898d5be4…`) plus 36 couples appliqués dans l'ordre, chaque « ancien » présent exactement une fois au moment de son
application (contrôle de l'assembleur ; 36 couples pour les 36 changements de la section 0.6, certains changements touchant
plusieurs lieux et certains couples portant plusieurs changements). Le paragraphe de scellement de la v1 (lignes 3 à 24) est remplacé
en tête par un paragraphe neuf et recopié tel quel en section 0.5 (contrôle : présent une fois, caractère pour caractère). Rien
d'autre : bloc `empreintes-du-code` identique à la v1 (73 lignes), bloc `plan-gele` identique hors de la ligne `go:`, configuration,
hypothèses, prédictions, métriques, critères, audits, liste d'arrêt et code inchangés. Différence : 64 lignes retirées, 401 ajoutées,
19 blocs (comptes sur le fichier de la différence ; 1 519 → 1 856 lignes). Une ligne de contenu de la v1 commence par
« --plafond-cumule-usd » (paragraphe de scellement déplacé) : dans la différence elle s'écrit « ---plafond… » ; `patch` la traite
correctement (reconstruction exacte).

Les 36 changements, une ligne chacun (texte complet : section 0.6 du brouillon) :
1. Titre : « brouillon 4 » → « seconde course : version 2, brouillon 1 ».
2. Paragraphe de tête : celui du scellement de la v1 → celui de la v2 (nom scellé `prereg/preenregistrement-attaque-goodhart-v3-v2.md`,
   statut, aucun marqueur, graine) ; l'ancien recopié tel quel en section 0.5.
3. Fait (iii) : GO-2026-11-02-21 dit « de la première course », « seul GO que la v1 nommait » ; + GO-2026-11-03-01 en fin du fait.
4. Section 0.4 : le GO de chaque course ; « ce texte (v2) est celui de la seconde ».
5. Section 0.4 (e) : I4 ne tient plus pour la ligne neuve (elle ne cite aucun commit : « code que gèle le texte neuf »).
6. Section 0.4 : + écart (h) (renvoi aux sections 0.5 et 0.6).
7. Section 0.5 neuve : faits n° 305 et 306, GO neuf, règle de la section 8, cause établie par l'audit A9 (marqueur rempli), lecture,
   dépense.
8. Section 0.6 neuve : la liste des changements.
9. Section 4, « Graines » : provenance de la graine, lignes citées ; graine neuve, cartes neuves.
10. Section 4, « Un scellement, une course » : renvoi à la section 0.5.
11. Section 4, « GO » : GO-2026-11-03-01, échéance 2026-11-17 ; épreuve de la ligne neuve ; I4 « première course (rappel) ».
12. Section 4, registre des GO : chemin neuf ; commit qui porte GO-2026-11-03-01 **et dont le registre est accepté par le lecteur** ;
    `grep -n "GO-2026-11-03-01"` ; + point (1 bis) (`main` refusé, `canal/conv-audit-n04` accepté, choix du directeur).
13. Section 4, dossier de sortie : `/home/user/hors-clone-a1-v3-seconde-v1/sortie-attaque-goodhart-v3`.
14. Section 4, commande exacte : seuls chemins, GO et texte changés ; hôte nommé.
15. Bloc `plan-gele` : `go: GO-2026-11-03-01`.
16. Notes du bloc : lecture de la v2 par le lanceur.
17. Section 8 : + « Seconde course (v2) : hôte nommé et gardé vivant, observé du dehors, fin brutale acceptée, Argon seul ».
18. Section 9 : + L17 ; phrase finale complétée.
19. Section 11 : + « Version 2 : bloc inchangé ».
20. Section 12 : montant de GO-2026-11-03-01 (repris de GO-2026-11-02-21) ; dépense de la première course non imputée.
21. Section 13, point 2 : contre-lecture R2 n° 3, courte, sur le delta ; nom `…-v2.md`.
22. Section 13, point 3 : GO-2026-11-03-01, échéance 2026-11-17.
23. Section 13, point 4 : intitulé « Marqueurs (aucun ne reste) » ; marqueur de l'audit A9, rempli ; chemins neufs à créer.
24. Section 13 : + points 7 bis (hôte nommé et gardé vivant) et 7 ter (Argon seul).
25. Section 13, point 9 : la seconde course rapportée avec la première, arrêtée, jamais seule.
26. Section 14 : n° 2 rendue ; n° 3 à faire (fichiers, neuf points).
27. Annexe B : marqueur de la v2, rempli ; celui du brouillon 4 marqué « rappel ».
28. Empreintes : fichiers du rédacteur de la v2.
29. Audit A9, point 1 (survie de l'hôte) : « jamais plus de quelques minutes sans activité, période nettement inférieure à 5 min »
    (section 8 ; section 13, point 7 bis).
30. Point 2 (observation hors du conteneur) : le harnais de la fille ou session-depot suit la course, jamais la seule relève horaire
    (section 8 ; point 7 bis).
31. Point 3 (fin brutale) : la perte de toute la trace est acceptée et dite (même instrument, code gelé `9776ed0`), troisième course
    sous la règle de la section 8 (sections 0.5 et 8).
32. Point 4 (sortie neuve) : déjà au changement 13 ; renvoi à l'audit (section 4).
33. Point 5 (imputation) : 4,245753 USD sous GO-2026-11-02-21, ne s'imputent pas sur les 400 USD de GO-2026-11-03-01, aucune garde
    de la seconde course ne les voit (sections 0.5 et 12).
34. Point 6 (identifiant de processus du guetteur) : chacun pris du processus lui-même (point 7 bis).
35. Point 7 (hôte nommé) : la fille de session-depot (sections 0.5 et 4 ; point 7 bis).
36. Registre, point (1 bis) : la copie de la première course venait de `canal/conv-audit-n04` (`e9d7b78d…`) (section 4).

Écart à la consigne, déclaré : la consigne dit « `main` `e12540bf` ou plus récent » pour la copie du registre ; l'épreuve montre que ce
registre est refusé par le lecteur du lanceur. Le texte garde `e12540bf` comme commit qui porte la ligne, exige un registre accepté,
et donne les faits des deux branches (changements 12 et 36) ; il ne choisit pas la branche à la place du directeur.

Choix du rédacteur, déclarés : (a) le marqueur était écrit une seule fois (section 0.5) et décrit ailleurs (« jeton AUDIT_A9 entre
doubles chevrons »), pour qu'un remplacement ne touche que lui ; il est désormais rempli, avec le commit de l'audit (`c8c34784`) dans
la même citation, sans second marqueur ; (b) une utilisation d'Argon pendant la course est un écart déclaré, non un arrêt : aucune
règle d'arrêt neuve (mots de Lazar : « je ne veux pas de blocage ») ; (c) les identifiants de processus et chaque réarmement de
l'attente sont écrits au journal de lancement (point 7 bis), pour qu'un audit A9 ait de quoi établir une cause ; (d) le texte ne
prescrit aucun mécanisme technique précis pour garder la session active : il fixe l'exigence (période nettement inférieure à 5 min,
observation hors du conteneur) et laisse le moyen à la fille.

## 4. Épreuve de lecture par le lanceur (point 4 de la consigne)

Lanceur et cœur pris dans l'arbre extrait du commit `9776ed0` (`RACINE` = `/home/claude/scratch/a1-v3-seconde`, `DOSSIER_PREREG` =
son `prereg/`, `pole` chargé depuis cet arbre : vérifié). Copie du brouillon sous
`/home/claude/scratch/a1-v3-seconde/prereg/preenregistrement-attaque-goodhart-v3-v2.md` (sha256 `c76ac6bc…`, égale au brouillon).
**Compagnon** : la règle interdit tout fichier `.sha256` ; la vraie fonction `verifier_scelle` (`pole/outils.py:72-79`) est jouée
telle quelle, mais son `open` du fichier compagnon lit une chaîne en mémoire (tout autre fichier est lu sur disque) : déclaré. Pour
les cas (d) à (h), le texte est écrit dans un dossier temporaire tenu pour `prereg/` (`DOSSIER_PREREG` remplacé le temps de l'appel ;
le code gelé reste vérifié sur l'arbre extrait) : déclaré. Les dossiers temporaires sont supprimés ; aucun `.sha256` n'existe dans les
blocs-notes (vérifié par `find`).

| cas | fonction | résultat | message |
|---|---|---|---|
| bloc `empreintes-du-code` contre `FICHIERS_GELES` | lecture du bloc | 73 lignes = 73 fichiers, ensemble égal ; 0 écart entre le bloc, l'arbre extrait, les objets git du commit `9776ed0` et la tête `eaa74ca` | — |
| plan | `lire_plan(texte, "course")` | **accepté** ; seule la clé `go` diffère de la v1 (devis compris) : 24 cartes, 24 unités par case, Argon, `relais_perdu_s` `None`, 400 USD, 72 h ; devis : 1 152 à 2 112 appels, 71,42 à 130,94 USD, maximum 3 072 appels et 190,46 USD, durée attendue haute 25,12 h, maximale 35,78 h | — |
| (a) copie, aucun compagnon | `lire_preenregistrement` | **refusé** | « préenregistrement non scellé (compagnon .sha256 absent ou non conforme) : …/prereg/preenregistrement-attaque-goodhart-v3-v2.md » |
| (b) compagnon simulé juste | `lire_preenregistrement` | **accepté** : 73 empreintes vérifiées, entropie = entier de l'empreinte (`c76ac6bc…`), ≥ 2⁶⁴, plan égal à `lire_plan`, `go` GO-2026-11-03-01 | — |
| (c) compagnon simulé faux | `lire_preenregistrement` | **refusé** | « préenregistrement non scellé (compagnon .sha256 absent ou non conforme) : … » |
| (d) texte réécrit dans un dossier tenu pour `prereg/` (aucun marqueur à remplir : identique à (b)) | `lire_preenregistrement` | **accepté**, mêmes valeurs | — |
| (e) même texte au nom du brouillon | `lire_preenregistrement` | **refusé** | « mode réel : le texte est prereg/preenregistrement-attaque-goodhart-v3-v<N>.md (course) ou prereg/fiche-essai-attaque-goodhart-v3-v<N>.md (essai), pas … » |
| (f) une empreinte du bloc altérée | `lire_preenregistrement` | **refusé** | « code différent du code gelé : pole/attaque_goodhart_v3.py : gelé db9cffe77fb8…, présent cb9cffe77fb8… » |
| (g) le brouillon à son chemin dans la copie de travail | `lire_preenregistrement` | **refusé** | même message de chemin |
| (h) premier assemblage (`2bed4c99…`, avec le marqueur), compagnon simulé | `lire_preenregistrement` | **refusé** | « marqueur(s) non rempli(s) : ['<<AUDIT_A9>>'] (décision de Lazar à porter avant scellement) » |
| GO du texte, registre factice | `verifier_go` (lanceur v2, `demonstrations/attaque_goodhart_v2.py:185-196`, puis `verifier_go_v56`) | **accepté** : GO-2026-11-03-01, calcul, Lazar, 2026-11-03 → 2026-11-17, 400 USD lus = 400 requis | — |
| GO-2026-11-02-21 en ligne de commande | `verifier_go` | **refusé** | « GO GO-2026-11-02-21 : le texte scellé nomme GO-2026-11-03-01 (aucun autre GO) » |
| plafond 399 USD / 401 USD | `verifier_go` | **refusés** | « A15 : la ligne GO-2026-11-03-01 porte 400 USD, pas exactement le plafond requis 399 USD (401 USD) : aucun lancement à un autre plafond (plus petit ou plus grand) » |
| dates 2026-11-02 / 2026-11-17 / 2026-11-18 | `verifier_go_v56` | refusé / **accepté** / refusé | « A15 : GO-2026-11-03-01 hors de sa période de validité (2026-11-03 → 2026-11-17) » |
| révocation qui nomme le GO | `verifier_go` | **refusé** | « A15 : GO-2026-11-03-01 révoqué par GO-2026-11-03-99 » (ligne factice) |
| décision qui nomme le GO | `verifier_go` | **accepté** | — |
| révocation de GO-2026-11-02-21 qui porte aussi l'identifiant GO-2026-11-03-01 | `verifier_go` (GO neuf) | **refusé** | « A15 : GO-2026-11-03-01 révoqué par GO-2026-11-03-99 » |
| révocation de GO-2026-11-02-21 seule | `verifier_go` | GO neuf **accepté** ; GO-2026-11-02-21 refusé (« révoqué par ») | — |
| registre de l'arbre privé (branche `canal/conv-audit-n04`, 81 lignes à l'épreuve finale, `8223230c…`) | `verifier_go` | GO neuf **accepté** (ligne 79) ; GO-2026-11-02-21 avec le plan de la v1 **accepté** (ligne 67) ; 0 doublon | — |
| `canal/conv-audit-n04` à `e4fd36905b58…` (79 lignes, `a5036824…`), à `3f1323719918…` et à `c8c3478422bd…` (80 lignes, `45d56fa0…`) | `verifier_go` | **acceptés** (ligne 79, identique à celle de l'arbre) | — |
| `canal/conv-audit-n04` à `e9d7b78dc7c1…` (78 lignes, `53985197d3e9…` : la copie de la première course, audit A9, section 1) | `verifier_go` | GO neuf **refusé** (« A15 : GO-2026-11-03-01 absent du registre … ») ; GO-2026-11-02-21 **accepté** (ligne 67) | — |
| `main` à `e12540bf1e1c…` (221 lignes, `7582a58e…`) et à `db454552d445…` (222 lignes, `13d69db3…`) | `verifier_go` | **refusés**, GO neuf comme GO-2026-11-02-21 ; la ligne du GO neuf y est (ligne 221), identique | « registre des GO : identifiant GO-2026-10-24-07 en double » |
| renvois `fichier:ligne` | contrôle du rédacteur | 45 renvois des passages neufs : contenu attendu à la ligne citée, 0 écart ; 151 renvois vers les deux fichiers v3 dans tout le brouillon : dans les bornes | — |
| marqueurs | motif du lanceur v3.1 | **aucun** (un, `<<AUDIT_A9>>`, au premier assemblage) ; aucun dans la v1 ; aucun double chevron hors motif | — |

Doublons du registre de `main` (relevé indépendant, `e12540bf` et `db454552` ; histoire : `sorties/historique-doublons-main.txt`) :
GO-2026-10-24-04, -05, -07 ; GO-2026-10-25-01, -02 ; GO-2026-10-26-04 ; GO-2026-10-27-01, -02 ; GO-2026-10-28-02, -05, -11, -14 ;
GO-2026-10-29-01, -02, -06 ; GO-2026-11-02-02. Sur l'histoire de `main` (60 derniers commits qui touchent `registres/go.md`, lecture
seule), les 60 commits ont au moins quinze doublons (le plus ancien relevé, `e97d9cb1`, 29 octobre, 09:43 UTC, en a quinze) ;
GO-2026-11-02-02 s'y ajoute le 2 novembre (`ddfff6e4`, 08:34 UTC) ; **les cinq commits de `main` qui portent GO-2026-11-02-21
(`f1791003` à `ea1bfd2e`) en ont seize**. La première course a donc pris son registre ailleurs : l'audit A9 donne son empreinte
(`53985197…`, GO-2026-11-02-21 à la ligne 67) ; le rédacteur l'a retrouvée sur `canal/conv-audit-n04` au commit
`e9d7b78dc7c177d6b22247639cfec42727b9f9ec` (même préfixe d'empreinte, ligne 67), non sur `main`.

Non fait ici, déclaré : `--verifier-seulement` (il exige la configuration `e5306c47…`, chez session-depot, et `--moteur reel`) ; les
essais et le banc du code (code inchangé, rejoués avant la première course : section 9, L16 de la v1).

## 5. Graine (point de la consigne)

La graine est l'empreinte du texte scellé : `demonstrations/attaque_goodhart_v3.py:288` (`sha256_fichier(reel)`), `:289`
(`verifier_entropie(int(empreinte, 16), decisif=True)`), rendue à `:540`, écrite au manifeste à `:577` (règle des graines `:583-588`),
passée à `jouer_tout` à `:607` et à `lire` à `:637` ; dans le cœur, `pole/attaque_goodhart_v3.py:708` (vérification), `:729`
(`carte(entropie, ci, w)`), `:500` (`ag.juger(…, entropie, …)`), `:769-770` (rejeux, audit A2) ; dans le cœur v2,
`pole/attaque_goodhart_v2.py:104-108` (`graine` : `SeedSequence(entropie, spawn_key=(cle(étiquette), …))`), `:165-186` (`carte`, graines
`monde|W` à `:170`, `developpement|W` à `:178`), `:442-444` (tirages d'évaluation), `:813` (rééchantillonnage). Texte neuf, empreinte neuve :
graine neuve, 48 cartes neuves et tirages neufs ; rien de la première course n'y entre ; aucune carte n'a été calculée (ni de la
première course, ni de la seconde). Le lanceur ne distingue pas une v1 d'une v2 : le nom `…-v2.md` est la règle R12, non une garde.

## 6. Le complément du directeur (audit A9) : ce qui est intégré, où

Audit lu en entier : `brouillons/preuves-mentors-v1/a1-v3-seconde-course-v1/audit-A9-a1-v3-premiere-course-v1.md` du dépôt privé,
sha256 `ed078aaa77e69a29a04bc2bbf198e5cac9906766677291b09154c22882d83e55`, compagnon égal, committé sur `canal/conv-audit-n04`
(`c8c3478422bd335bd4e1003b84dadba2a26f6206`, R-1337 ; fichier du commit égal). Marqueur remplacé par son chemin, son commit, son
empreinte et sa conclusion (section 0.5). Les sept points de sa section 8, chacun en une ou deux lignes, sans toucher hypothèses,
prédictions, métriques ni critères :

| point de l'audit | où dans le texte | changement (section 0.6) |
|---|---|---|
| 1. survie de l'hôte : période nettement inférieure à 5 min, ≈ 25 h attendues, 72 h au plus | section 8, « Seconde course (v2) », (1) ; section 13, point 7 bis | 29 |
| 2. observation hors du conteneur (harnais de la fille ou session-depot), pas la seule relève horaire | section 8, (2) ; point 7 bis | 30 |
| 3. fin brutale : toute la trace perdue, acceptée et dite, même instrument, code `9776ed0`, troisième course sous la section 8 | section 8, (3) ; section 0.5 (« Si cette course s'arrête… ») | 31 |
| 4. sortie neuve (le lanceur refuse un dossier non vide) | section 4, dossier de sortie (renvoi à l'audit) | 13, 32 |
| 5. imputation : 4,245753 USD sous GO-2026-11-02-21, non imputés aux 400 USD de GO-2026-11-03-01, invisibles des gardes | section 0.5, « Dépense » ; section 12 | 33 |
| 6. identifiant de processus du guetteur pris du processus lui-même (1403 contre 1405) | section 13, point 7 bis | 34 |
| 7. hôte nommé : la fille de session-depot (la ligne de GO-2026-11-02-21 disait « chez session-depot ») | section 0.5 ; section 4, commande exacte ; point 7 bis | 35 |

Faits de l'audit utiles à la seconde course, non portés au texte : à la première course, le relais 8805 avait un plafond propre de
410 USD et 9 000 appels (audit A9, section 1, 06:16:55-06:17:12 UTC) — au-dessus de ce qu'exige la section 13, point 7 (a) (au moins
400 USD et 8 000 appels) ; la course était lancée détachée (`nohup setsid …`) et aucun processus n'était suivi par le harnais
(audit A9, section 6).

## 7. Décisions à proposer au directeur

**D-A — Source de la copie du registre des GO.** Décision : de quel commit session-depot extrait-il `registres/go.md` ? Enjeu : le
registre de `main` fait refuser la course à `--verifier-seulement` (code 2, rien dépensé, mais pas de course). Options : (a) un commit
de `canal/conv-audit-n04` qui porte la ligne (accepté ; ligne recopiée octet pour octet ; c'est la branche dont venait la copie de la
première course, `e9d7b78d`), plus la sortie de `grep -n "GO-2026-11-03-01"` sur le registre de `main` au journal (aucune révocation
ne doit l'y nommer) — avantage : course possible tout de suite, même source qu'à la première course ; inconvénient : copie d'une
branche qui n'est pas `main` ; (b) lever les doublons de `main` — avantage : `main` redevient lisible pour tous les lanceurs v56 ;
inconvénient : touche des lignes de GO (« une ligne par GO, jamais modifiée » : décision de Lazar). Recommandation : (a), confiance
0,8. Défaut sous 48 heures : (a).

**D-B — Ordre avec les autres utilisations d'Argon.** GO-2026-11-03-02 (registre privé, ligne 80 de `canal/conv-audit-n04`) : course
d'idéation « cinq espèces (Fable 5.1, Opus 5.5, Argon, Kimi, Astra) », « course chez la fille, session active jusqu'à la fin », « go
lance heimersheim dès que le devis est prêt » (mots de Lazar reçus entre 07:44:11 et 08:03:02 UTC). GO-2026-11-03-03 (ligne 81,
ajoutée pendant la rédaction) : « pour les deux appels seuls Astra et Argon : go ». Aucune ne peut tourner pendant la seconde course
(relais 8805 à un seul fil, quota commun : section 8 du brouillon). Recommandation : les finir d'abord, relais arrêtés par leur
identifiant de processus, puis la seconde course d'A1-v3 (ou l'inverse, au choix de Lazar) ; confiance 0,8.

**D-C — Relance de la v1.** Le code n'empêche pas de relancer la v1 sous GO-2026-11-02-21 (accepté sur le registre de
`canal/conv-audit-n04` : épreuve). Options : (a) laisser la règle de procédure (« un scellement, une course ») ; (b) que Lazar révoque
GO-2026-11-02-21, par une ligne qui **ne porte pas** l'identifiant GO-2026-11-03-01 (sinon celui-ci serait refusé : épreuve).
Recommandation : (a) jusqu'à la course, (b) ensuite ; confiance 0,6.

**D-D — « à corriger sur le mot de Lazar ».** La ligne de GO-2026-11-03-01 finit son périmètre par ces mots ; le texte les cite sans
les interpréter. À faire préciser (le montant, 400 USD, est-il appelé à changer ?) ; tant qu'aucun mot neuf n'est inscrit, 400 USD
exactement (le lanceur l'exige à 10⁻⁹ près).

## 8. Points à viser pour le contre-lecteur (R2 n° 3, courte, sur le delta)

1. **Registre (section 4, points (1) et (1 bis))** : la règle « registre accepté par le lecteur » et le choix laissé au directeur
   suffisent-ils, ou faut-il fixer la branche dans le texte ? Les faits (doublons de `main`, acceptation de `canal/conv-audit-n04`,
   source `e9d7b78d` de la première copie) sont-ils exacts (rejouer `epreuve_lanceur_v2b1.py`) ?
2. **Le delta et rien d'autre** : appliquer `diff-…-brouillon1.txt` à la v1 ; comparer à la section 0.6 (36 lignes) ; vérifier que le
   paragraphe de la v1 est recopié tel quel en section 0.5 et que les blocs sont inchangés hors de `go:`.
3. **Audit A9 dans le texte** : citation (chemin, commit, empreinte) et conclusion fidèles à l'audit ; l'argument de code (« manifeste
   sans `attaque-goodhart-v3.json` = arrêt hors des codes 0, 2 et 3 ») concorde-t-il avec la section 2 de l'audit, qui cite pour les
   mêmes fins `:562-566`, `:618-620` et `:640-648` (le texte cite `:562-567`, `:609-621`, `:637-646`, bornes plus larges des mêmes
   blocs) ?
4. **Les sept points** : chacun au bon endroit, en une ou deux lignes, sans toucher hypothèses, prédictions, métriques ni critères ;
   l'exigence « période nettement inférieure à 5 min » est-elle compatible avec « une attente suivie par le harnais, réarmée avant son
   délai (2 h au plus) » telle qu'écrite (le texte exige les deux : activité de la session à moins de 5 min d'intervalle, et un délai
   d'attente borné) ?
5. **GO** : chaque occurrence de GO-2026-11-02-21 restante désigne la première course, l'historique ou un « avant » (41 lignes du
   brouillon ; `lieux.GO_21` de la sortie de l'épreuve) ; I4 ne tient plus ; le piège de la révocation qui porterait l'identifiant neuf.
6. **Argon seul** : ordre avec GO-2026-11-03-02 et GO-2026-11-03-03 (D-B) ; « écart déclaré, pas un arrêt » est-il le bon traitement ?
7. **Règle de lecture et dépense** : rapportée avec la course arrêtée, jamais seule ; 4,245753 USD non imputés (registre de dépense neuf
   par le jeton `{REGISTRE}`, relais neuf, compteur à zéro).
8. **Section 13, point 1, inchangé** : le texte ne redemande pas de rejouer essais et banc (code identique au commit `9776ed0`,
   vérifié) ; acceptable ?
9. **Faits non vérifiables ici** (n° 305 et 306 : état de la fille, branche `donnees/…`, empreintes du rapport et de la liste de la
   fille, écart de 07:20:01 UTC) : cités comme faits de session-depot ; l'audit A9 les a confrontés à la copie de l'état (sa section 0).

## 9. Réserves

- **Effet de bord dans le dépôt privé** : une de mes boucles de lecture (`git show` et `git log` sur une quarantaine de commits de
  `canal/conv-audit-n04`, vers 08:34 UTC) a déclenché le tassement automatique de git (« Auto packing the repository in background for
  optimum performance », sept fois). C'est de l'entretien des objets, sans changement de branche, de fichier suivi ni d'historique ;
  il a fini seul (aucun `gc.pid` ni `gc.log` restant). Je ne l'avais pas voulu ; toutes les lectures suivantes ont été faites avec
  `-c gc.auto=0 -c maintenance.auto=false`. À dire au directeur (autres sessions sur ce clone).
- Le registre de l'arbre privé a changé pendant la rédaction (79 lignes, `a5036824…`, à la première lecture ; 80 lignes, `45d56fa0…` ;
  81 lignes, `8223230c…`, à l'épreuve finale : lignes GO-2026-11-03-02 et GO-2026-11-03-03 ajoutées) et `origin/main` a avancé
  (`e12540bf` → `ea1bfd2e` → `db454552`) : l'épreuve porte aussi sur des commits fixes, nommés.
- La ligne GO-2026-11-03-01 contient elle-même l'identifiant GO-2026-11-02-21 (« plafond repris du GO-2026-11-02-21 ») : sans effet (elle
  est de type calcul, non révocation), mais `grep -n "GO-2026-11-02-21"` la trouve aussi (lignes 67 et 79 sur la branche, 209 et 221
  sur `main`).
- Compagnon simulé en mémoire et dossier `prereg/` remplacé pour (d) à (h) : la vraie lecture d'un compagnon sur disque se fait chez
  session-depot, au lancement.
- Les faits de l'audit A9 sont repris tels qu'il les écrit ; le rédacteur a vérifié son empreinte, son compagnon et son commit, et
  relié l'empreinte `53985197…` qu'il donne au registre de `e9d7b78d` (même préfixe de huit caractères, ligne 67) ; il n'a pas eu accès
  à la copie de l'état interrompu.
