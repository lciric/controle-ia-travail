# Vérification de la conception « monde riche et doublons » v3 par un lecteur Fable — v2

- **Lecteur** : lecteur neuf (règle R2), **Claude Fable 5.2** (`claude-fable-5-2`), sous-agent de la session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. Autre modèle que le concepteur (Claude Opus 5.5), même famille : réserve de lignée
  ordinaire de N-052. Je n'ai écrit ni la conception, ni ses outils, ni la vérification de la v2. La contre-lecture v1
  (`e7d5cda0…`) est d'un autre agent du même modèle que moi.
- **Objet** : `conception-monde-riche-doublons-v3.md` (`386d48bacd6c487d88846d0991d83bd4ad95122f70500d6fbeb7859cde56659c`,
  recalculée, égale à son compagnon), lue en entier ; `outils-v3/` (2 scripts, compagnons justes) lus en entier ;
  `sorties-v3/` (41 pièces, compagnons tous justes) ; `outils-v2/monde_riche_outils_v2.py`, `puissance_monde_riche_v2.py` et
  `devis_multi_generations_v2.py` lus en entier ; contre-lecture v1 (`e7d5cda0…`) et vérification de la v2 (`0d64ed1d…`),
  recalculées, égales à leurs compagnons, lues en entier ; `registres/decisions.md`, lignes R-2441 à R-2443, R-2461, R-2467,
  R-2469, R-2471, R-2474, R-2475, R-2477.
- **Interdits** : interdits communs v2 lus en entier et tenus ; aucun fichier ni dossier interdit ouvert ou listé ; aucune
  recherche récursive ; aucune clé lue ; aucune écriture git ; aucun appel externe ; aucune dépense. Aucun refus de permissions
  ni de classifieur. Écrit : ce rapport et son compagnon ; le reste dans mon bac
  `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/verif-v3-fable/`.
- **Heures** (`date -u`) : début 2026-11-13 01:32:15 ; rejeux 01:35:01 → 01:37:07 ; heure de fin en bas du rapport.

## Verdict

**Utilisable pour le préenregistrement après corrections** : cinq corrections de texte (F-1 à F-5), **aucun recalcul**. Le code
de V-1 est juste et le correctif v3b ne change rien d'autre ; les chiffres v3 sont rejoués égaux.

## Corrections exigées (texte seulement ; à porter dans une v4 courte ou directement au préenregistrement, au choix de la mère)

**F-1 — V-4 n'est pas appliquée dans la table des changements de code.** §1.3, ligne K-2 : « m = 44 sur le décompte du
dessin ». Le §3.3 fixe m par règle : 48 à quatre proposeurs, 54 avec Kimi. Écrire en K-2 : « m par la règle du §3.3 (48 ; 54
avec Kimi) ». Même section §3.3 : l'exemple des onze copies prend m = 40 (seuils 4,29 et 6,68) ; le dire « exemple de l'essai
v1, m = 40 », ou le refaire à m = 48 (rang 11 : log(48/0,55) ≈ 4,47 ; rang 1 : ≈ 6,87 ; l'exemple tient encore à 4,5 > 4,47,
de peu).

**F-2 — V-5 : trois restes de la lecture trop forte, et la mesure demandée au banc n'est pas définie.**
1. §1.2, dernière phrase : la détectabilité contre l'archive réelle se mesurerait « avant la course, selon la taille de
   l'archive (§1.6, E-3) ». C'est ce que V-5 retire. Écrire : « avant la course, au banc, contre des archives sans W₋ᵢ (§1.8,
   V-5) ».
2. §1.8 garde l'ancienne phrase (« puissance … selon la taille de l'archive (1, 8, 16 lois et plus : distinguer monde épuisé
   de juge devenu sourd, E-3) ») à côté de la nouvelle. Une seule doit rester : la nouvelle.
3. §0, point 4 : « ne coûte presque rien ». Vrai pour les faibles (294, 295, 295 sur 540). Faux pour les moyennes : 0,93 →
   0,85, huit points (§1.6). Écrire les deux.
4. **La loi jugée dans la mesure de surdité n'est pas dite.** Le §1.8 dit « puissance sur une composante faible contre des
   archives sans W₋ᵢ ». Si la loi jugée est le monde W, elle bat une archive partielle de bien plus que I_i, et la mesure ne
   dit rien de la surdité à un effet faible. Écrire : loi jugée = sentinelle « meilleure loi (ou enveloppe) de l'archive plus
   la seule composante i, calibrée » ; archive = retenues simulées d'une génération 2, sans W₋ᵢ ; comparaison à la même
   sentinelle contre {W₋ᵢ}.
5. **Q-5, option (c)**, la règle qui fixera n : « un effet à 0,025-0,03 nat au-delà d'une archive de 8 lois ». Dire la
   composition de cette archive (sans W₋ᵢ, comme au point 4) et la loi jugée. Sinon n serait fixé sur le cas que V-5 écarte.

**F-3 — V-2 : une phrase fausse reste.** Table « Changements depuis la v1 », ligne E-2 : « rejoués sous `PYTHONHASHSEED=1` …
(graine 0) ». Sous `python3 -I` ces deux graines n'ont jamais été en vigueur. Écrire : « second lancement à une autre graine
aléatoire ». Sans effet sur les chiffres. Voir aussi G-2.

**F-4 — Devis : deux montants incomplets.**
1. **« 409 USD au pire » ne compte pas la machine.** 409,20 = modèles seuls (363 + 34,20 + 12, vérifié par la formule et par
   `devis-v2.json`). Avec le plafond de la machine (10) : 419,20. Les deux lignes proposées font 365 + 57 = **422 USD**
   d'engagement. Le §0, point 10, écrit « 409 au pire (365 sur crédits, 57 hors crédits avec la machine) » : les parenthèses
   ne font pas 409. Écrire les trois nombres.
2. **Q-12 (b) : GO-β2 monte aussi.** Si les fausses et copies promues sont testées (46 tests), le vérificateur Argon passe de
   34,20 à 39,60 (6 × (2 + 46 × 0,10)) : GO-β2 = 39,60 + 12 + 10 = 61,60, soit **62 USD et non 57**. Le texte ne donne que
   GO-β1 445. Le total « ≈ 496 » est juste pour les modèles (495,60) ; avec la machine 505,60 ; lignes 445 + 62 = 507.

**F-5 — V-1 : trois précisions à écrire au préenregistrement** (le code de simulation est juste, voir réponse 1).
1. **Graine de la tranche.** Dans le code, la tranche se tire des seules empreintes canoniques triées des membres
   (`rng_de("choix-v3", clé)`, clé réduite à 32 bits). Pour la course : graine = racine de la tâche de la génération (comme
   les tirages du juge) **et** empreintes triées des membres.
2. **La tranche n'est jamais servie** : ni aux proposeurs, ni à l'expérimentateur (qui voit la tranche du test de mort).
3. **Garde 25, cas d'artefact de la tranche** (R5) : la liste des artefacts n'en a aucun. Ajouter : tranche différente d'un
   candidat à l'autre, ou égale à la tranche du test de mort ou aux tirages du juge → arrêt.

## Corrections suggérées

- **G-1** Titre du §0 : « En dix lignes (v2) » → v3. Point 7 : archive 16,3 (v2) → 16,1 (v3).
- **G-2** `puissance_monde_riche_v3b.py` écrit le champ `graine_de_hachage` en dur (« aléatoire (python -I) »), même lancé
  sans `-I`. Les 12 parties scellées ont bien été lancées sous `-I` (journal) : sans effet ici. Dans le code v68, lire
  `sys.flags.isolated`, comme le fait le script v3.
- **G-3** `resume` (v3 et v3b) agrège ce qu'il trouve : avec 0 partie, il a écrit un résumé de valeurs vides au code 0 (pièce
  gardée, déclarée). Pour le banc : refus si le nombre de parties n'est pas celui attendu (pas de repli silencieux, R5).
- **G-4** Le pire cas tient si les bornes sont imposées par le code (1,50 USD par test d'Opus, plafonds de session, 0,10 du
  vérificateur — borne gelée de la v64, vérifié au devis v66, l. 18). Le préenregistrement doit le dire et l'essayer (R5).
- **G-5** La perte restante (monde 4 : tempérée à 0,3 préférée à la loi, 0,038 nat) est un départage sur 400 épisodes
  appariés ; la tranche de 2 000 épisodes proposée au banc la vise : à garder.
- **G-6** L'en-tête dit que `.venv` n'a pas numpy ; il porte aujourd'hui numpy 2.4.6 (le système : 2.5.3). Mes rejeux sous
  2.4.6 sont égaux aux sorties faites sous 2.5.3.

## Réponses

**1. V-1 à V-7 à la lettre ?**

| | appliquée ? | remarque |
|---|---|---|
| **V-1** | **oui, dans le code et le texte** | F-5 (précisions pour la course) |
| V-2 | oui, à une phrase près | F-3, G-2 |
| V-3 | oui | les deux noms fautifs ne restent que dans la ligne qui dit leur retrait |
| V-4 | oui au §3.3 ; **non en K-2** | F-1 ; décompte vérifié : 24 + 12 + 5 + 4 + 1 + 2 = 48 ; 54 avec Kimi ; log(48/0,05) = 6,87 ; écart à m = 44 : 0,087 nat |
| **V-5** | **oui au §0 et au §1.6 ; restes ailleurs** | F-2 |
| V-6 | oui pour GO-β1 (444 par la formule) et pour la borne par test (Q-2, Q-12) | F-4 |
| V-7 | oui | Q-11 dit le coût du latent ; recommandation passée de (c) à (a), dite |

T-1 à T-5 : repris.

*V-1, lecture du code.* `representant_v3` (v3) et `rep_v3` (v3b) font la même chose :
- la clé du groupe est la liste triée des empreintes canoniques de **tous** ses membres ;
- la tranche (400 instances, issues tirées du monde) est tirée **une fois**, au premier candidat, puis gardée pour les
  suivants ; chaque candidat est noté sur les mêmes instances et les mêmes issues ; la marginale de référence est donc la
  même, et la comparaison ne porte que sur les lois ;
- la statistique est celle de `test_de_mort` de la v1 (même formule, comptes + 0,5, plancher 10⁻¹²), recopiée ;
- le flux aléatoire de la tranche (« choix-v3 ») est distinct de ceux du juge (« gen-juge », « doublons-juge ») et du test
  de mort (« gen-mort ») : les graines se dérivent par clé, sans état partagé ;
- la tranche n'est tirée que s'il y a égalité de couverture ; la valeur e du groupe n'en dépend pas.

Contrôle par instrument dans mes rejeux : monde 4, partie « représentant » : 4 tranches tirées pour 4 groupes départagés,
4 clés et 4 tranches distinctes, 10 notes, **toutes sur la tranche de leur groupe** (2 ou 3 candidats par tranche) ; partie
« générations » : 5 tranches, 10 notes, même constat.

*V-5, portée.* Vérifié dans `_archive_monde` : l'archive est `[W₋ᵢ] + k` lois partielles sans la composante i. Le test mesure
le coût d'ajuster le mélange sur plus de membres, rien d'autre. Le §0 et le §1.6 le disent maintenant. Restes : F-2.

**2. E-1 à E-12 toujours tenues ?** Oui. Le texte v3 garde les douze corrections ; la v3 n'en défait aucune. E-1 est
renforcée par V-1. Sondes dans le code v2 : latent à part (E-5), C7 en mesure avec refus à six décimales (E-7), 200 graines et
borne basse de Wilson 0,8 (E-11), liste blanche par chemins réels (S-7), parcours triés (E-2) : conformes. Restes : F-1 (m,
côté E-3) et F-3 (phrase de E-2). Je n'ai pas relu ligne à ligne le générateur ni le vérificateur v2.

**3. Le correctif v3b change-t-il autre chose ?** Non. Différences avec la partie « générations » du script v3, toutes lues :
- la règle v2 d'origine est gardée à part avant le remplacement (c'est le correctif : plus de récursion) ;
- le résumé ajoute `faibles_captees_moyen` ;
- le champ `graine_de_hachage` est en dur (G-2) ; le nom de version change.

La tranche, la clé, la statistique sont celles du script v3 (`P3.tranche_de_choix`, `P3.statistique`). La fonction non
appariée passée par le script v2 est ignorée ; son flux (« gen-choix ») n'est plus tiré, sans effet sur les autres flux. Les
parties « représentant » et « doublons » du script v3 n'étaient pas touchées par la récursion (elles ne remplacent rien).
Comparaison des 12 parties v3b à la condition « regroupement » de la v2 : 4 mondes égaux en tout ; 5 mondes ne diffèrent que
par le gain d'enveloppe (autre représentant, mêmes comptes) ; mondes 5 et 6 : une fausse découverte de plus, une de moins ;
monde 9 : 1 retenue au lieu de 3 en génération 2. Composantes captées égales à la condition « sans » dans les 12 mondes.

**4. Rejeux** (un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`, `.venv/bin/python -I -B`, Python 3.13.18,
numpy 2.4.6) :

| sortie scellée | rejeu | résultat |
|---|---|---|
| `sorties-v3/representant-v3-monde-4.json` (`f8ec9fc6…`) | partie « représentant », monde 4, 01:35:01 → 01:35:08 | champ `resultat` **égal** |
| `sorties-v3/generations-a2-v3b-monde-4.json` (`617a5b1b…`) | partie « générations, regroupement » v3b, monde 4, 01:35:12 → 01:37:07 | champ `resultat` **égal** |

Recoupements sans calcul lourd, sur les parties scellées : 82 groupes, 1 perte au-dessus de 0,01 (0,0376, monde 4), 0 sous g₀
à tort, départages 38 et 44 ; doublons 7,83 groupes retenus, 5,00 idées (5,33 par carte) ; générations 15 sur 108, 13 sur 73,
0 sur 0 ; parts captées 0,889 et 0,937. Tous égaux aux résumés et au texte.

**5. Devis et questions.**
- 409,20 USD au pire pour les modèles à 2 × 3 : **juste** (6 × (5 + 37 × 1,50) = 363 ; Argon 6 × (2 + 37 × 0,10) = 34,20 ;
  Astra 12). GO-β1 365 : juste. GO-β2 57 : juste (34,20 + 12 + 10 = 56,20). Bornes par test recalculées : Opus 1,344 → 1,50 ;
  Kimi 0,672 → 0,80 ; Argon 3,36 → 3,40. Variantes 1 × 3, 3 × 3, Kimi cinquième proposeur (417 ; 475,80), Kimi
  expérimentateur (295,20), plafond de travail (207,60) : justes.
- **Incomplet** : F-4 (machine hors des 409 ; GO-β2 à 62 sous Q-12 (b)).
- Q-1 à Q-12 : formes justes, enjeux et options fidèles au texte. À corriger : Q-5 (F-2, point 5) et Q-12 (F-4, point 2).
  **Aucune question ne manque** pour Lazar.

**6. Prête à servir de base au préenregistrement ?** Oui, une fois F-1 à F-5 portées. Aucune ne touche un chiffre de
simulation ni la preuve du §3.3. Ce que le préenregistrement doit reprendre sans faute : la règle de m (48 ou 54), la
définition de la mesure de surdité et de la règle de n (F-2), la graine et la garde de la tranche de choix (F-5), les montants
des deux lignes selon la réponse à Q-12 (F-4).

## Limites

- Rejeux partiels : deux parties du monde 4 sur 36 parties v3.
- E-1 à E-12 : relues dans le texte, sondées dans le code ; le générateur et le vérificateur v2 n'ont pas été relus ligne à
  ligne par moi (ils l'ont été par la vérification de la v2, faite par Opus : la réserve de lignée reste sur ces deux pièces).
- Code gelé du juge non lu (absent du dépôt), comme tous avant moi.
- **Cette v2 remplace la v1** du même rapport (`verification-conception-v3-fable-v1.md`,
  `b5c592bf5ec9eb097f8e879bbbab7d1d01e3c5c474abc720263413348bdc530b`, scellée, gardée sans modification, R12) : deux comptes
  faux corrigés par moi à la relecture — 41 pièces dans `sorties-v3/` et non 39 ; 5 mondes (1, 2, 7, 8, 10) ne diffèrent
  de la v2 que par le gain d'enveloppe, et non 6. Verdict, corrections et réponses inchangés.
- **Heure de fin** (`date -u`) : 2026-11-13 01:39:20.
