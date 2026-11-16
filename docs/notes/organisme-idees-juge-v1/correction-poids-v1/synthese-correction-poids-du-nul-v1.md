# Synthèse — apprendre les poids du nul sans casser sa garantie — v1

- Rédacteur : sous-agent neuf de la session mère. Je n'ai écrit aucune des pièces citées (ni la preuve, ni le
  préenregistrement, ni la contre-lecture, ni les rendus des cinq concepteurs, ni les cinq réfutations).
- Date : 2026-11-15, de 19:26 à 19:50 UTC environ (`date -u`). Dépôt `/home/user/controle-ia-travail`, branche `main`, lu
  sans commit.
- **Statut : mise au point exploratoire, aucune revendication.** Le résultat décisif viendra seulement du préenregistrement
  scellé de l'idée 1.1 (version 2) et de son jeu. Adopter une de ces voies dans le juge ferait un nul v10 : c'est une
  décision du directeur.

## 1. Verdict en trois lignes

1. **Oui, il existe des façons valides d'apprendre les poids du nul**, mais pas celles des fiches. La seule qui rend de la
   puissance sans rétrécir la classe du v9 est la **projection par blocs** (M3) : les poids sont calculés à partir de la
   carte, gelés avant chaque bloc de 25 tirages, et la valeur e du bloc est divisée par un certificat exact.
2. Sur un banc simplifié, M3 **regagne de 41 % à 82 % de la puissance que le v9 perd** contre le v8 (+0,045 à +0,185 de taux
   de promotion), avec la même classe que le v9 ; elle reste un peu sous le nul limité aux coupures de l'archive (−0,11 à
   +0,03). Deux règles de lecture du v9 (lire 40 instants, et rejeter chaque famille à son propre instant) gagnent aussi,
   mais peu (+0,02 à +0,03).
3. Condition à ajouter, que l'auteur n'avait pas écrite : **la loi de la carte ne doit pas lire les issues du bloc jugé**.
   Sinon la projection fausse la taille, jusqu'à 45 % de fausses promotions. Le juge accepte aujourd'hui deux lois de ce
   type. Les autres angles (ensemble de confiance, borne de regret, moitiés des tirages) sont valides mais ne regagnent rien.

## 2. Pièces lues et empreintes

Toutes les empreintes ont été recalculées le 15 novembre. Elles sont égales à leurs compagnons `.sha256`, soit 632
compagnons dans `correction-poids-v1/` avant ce texte, sans aucun écart.

| empreinte (sha256) | pièce |
|---|---|
| `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` |
| `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` |
| `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` |
| `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` | `docs/verdicts/verdict-validation-nul-v9-v1.md` (seul fichier ouvert dans ce dossier, par son chemin exact) |
| `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` | relevé d'idées, section 1.1 |
| `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` | `sortie--fiches-validees.json` (fiches argon-p1-01, argon-p2-01, opus-p1-05, fable-p1-05) |
| `681eb7f5c75b9599ddb7508b575f1824fb126fa781409104e08115d106e51f2e` | `projection/methodes-projection-v1.md` |
| `7bfaa88eae7485c973ab6d07271324eca4da4b0bf1404aa1e7e2afce00f5d5e4` | `projection/refutation-projection-v1.md` |
| `324e1243f4d508f5ebb26ff67cb490e9e56e1cdd7c25dc1d45ab2d009b6fa2c4` | `universelle/methodes-universelle-v1.md` |
| `f1f03b19f034579ccfa41a360bdc33a7e09d9c48ed456ff375f6b86ba033af84` | `universelle/refutation-universelle-v1.md` |
| `b2cb2685f5fc1b10d0cbb2be9deef158d11e2979e2a519dbfc682bb5a293f266` | `confiance/methodes-confiance-v1.md` |
| `04028cf3707aef6b74e1bbbcb5bf6ce6c1492b2f405fbf662f3177d1dae81020` | `confiance/refutation-confiance-v1.md` |
| `fac20a285737517f31ececd8062b38b93b25b8349813bd120311e42e93c990c4` | `regret/methodes-regret-v1.md` |
| `ca3fad0cb6e388818be2af851ed181bf9e21469af62a88c386331aa9185045f4` | `regret/refutation-regret-v1.md` |
| `e7a2bb6c67241cbb41477c3f6839d802392d74e60960272e5da10ef2cbffc14c` | `libre/methodes-libre-v1.md` |
| `8ee42bd6ba74f7326f9f1540db5538bee1373f9a6e6bfa8143ef62ea9f58318b` | `libre/refutation-libre-v1.md` |

Le fichier `instantane-en-cours-v1.md` de ce dossier dit lui-même qu'il ne fait pas foi. Je ne l'ai pas utilisé.

Ce que dit le verdict du v9 (« puissance perdue », chemin ci-dessus) : la validité du v9 tient sur 18 lignes fatales sur 18.
Mais sur la ligne I02 (interaction faible hors de l'archive), le v9 perd 0,105 de puissance appariée contre le v8, avec
une borne de Clopper-Pearson unilatérale à 95 % de [0,0894 ; 0,1223], au-delà de la marge de 0,05.

## 3. Mes rejeux (un programme d'attaque au moins par méthode recommandée)

J'ai lancé tous les programmes avec `.venv/bin/python -I -B` depuis le dossier `synthese-rejeu-v1/`, sur processeur seul.
Les programmes sont ceux des dossiers d'angle, jamais ceux des dossiers de copie du juge. Chaque lancement a duré moins de
dix minutes (le plus long : 269 s). Les graines sont celles des programmes, par `numpy.random.SeedSequence`, et elles sont
écrites dans chaque sortie. J'ai choisi des numéros de monde ou de lot neufs pour avoir des mondes neufs. Toutes les sorties
et tous les journaux sont scellés dans `correction-poids-v1/synthese-rejeu-v1/`.

| ce qui est rejoué | programme, commande | résultat | lecture |
|---|---|---|---|
| M3, M1, M2b : pire cas de la famille linéaire (dose 0,6), **300 mondes neufs** (r = 5000 à 5299) | `projection/attaque_projection_v1.py taille pire_lin_d06 5000 5300 … --m3` | M3 complet **0/300** [0 ; 0,0122] ; borne de M3 par la vraie famille 3/300 [0,0021 ; 0,0289] ; M1 3/300 ; M2b 3/300 ; M2 1/300 ; artefacts : A1 233 à 237/300, A2 102 à 118/300 [0,287 ; 0,451] | même régime que le réfutateur (35/2 120 au pire, environ 1,7 %), sous α |
| M3 et M2b : copie coupée hors de l'archive, **250 mondes neufs** | même programme, `taille copie_coupure_hors 5000 5250 … --m3` | M3 **0/250** [0 ; 0,0146] ; M2b 227/250 et M1 243/250 (hors de leur classe : trou attendu) ; A1 250/250 ; A2 240/250 | M3 ferme bien la copie hors archive, comme le v9 |
| Garde P4 : carte qui lit l'historique du bloc (réglage 7) | même programme, `memoire 7 … --mondes 400` | **198/400 promues [0,445 ; 0,545]** ; valeur e moyenne du premier bloc 2,13 ; témoin à historique gelé 0/400 ; témoin vrai 14/400 | contre-exemple retrouvé (le réfutateur : 904/2 000 ; mêmes graines, ses 400 premiers mondes) |
| M3, M2b : puissance, ligne V4 dose 0,2, 100 mondes | `projection/essai_projection_puissance_v1.py V4_loi_neuve_sous_population 1 0 100 3 …` | sortie **identique** à la sortie scellée de l'auteur, durée exclue. R9 15, M3 38, RLa 40, M2b 55, R8 50 sur 100 | gain de M3 sur R9 retrouvé sur cette tranche |
| Lecture dense (40 instants) et rejet membre par membre : rejeu | `libre/attaque_libre_lecture_dense_v1.py lot N1b 0..3` et `lot P1 0..3`, 250 mondes par lot, pas de 5 | totaux **identiques** à `sortie-attaque-libre-lecture-dense-v1.json` sur tous les bras ; le lot N1b-3 est identique à l'octet (`a50c5f7b…`) ; 0 domination violée | P1 : v9 293 puis 316 en dense ; membre par membre 300 puis 322 ; avec les membres log-linéaires, v9 238 → membre par membre dense 265 sur 1 000 |
| Lecture dense et membre par membre : **mondes neufs** (lots 10 à 13) | même programme, `lot N1b 10..13` et `lot N2b 10..11` | taille en dense, carte qui n'est pas une copie : v9 et membre par membre **5/1 000** [0,0016 ; 0,0116] (N1b) et **2/500** [0,0005 ; 0,0144] (N2b) ; rapport au monde 24/1 000 et 12/500 ; 0 domination violée | sous α ; aucune promotion sans que le rapport au monde atteigne 1/α |

Je n'ai pas refait de banc à moi. Mes rejeux confirment les chiffres des réfutateurs ; ils n'élargissent pas leur portée.

## 4. Tableau de toutes les voies

**Règle de lecture.** Une voie n'est dite **valide** que si sa preuve a été suivie sans pas faux **et** si l'attaque du
réfutateur a échoué. Sinon elle est « non établie » ou « non valide ». Une voie valide seulement sur une classe plus petite
que celle du v9 est dite « valide sur sa classe » : c'est un nul plus petit, pas une correction des poids.

« Copie » : taux de promotion d'une copie exacte d'un membre du nul (intervalle de Clopper-Pearson à 95 %). « Puissance » :
écart de taux de promotion sur de vraies découvertes, sur les mêmes tirages, comparé au maximum certifié façon v9 (« v9 »)
et au nul limité aux coupures de l'archive (« La »). Chaque banc est celui de l'angle : les ampleurs ne se comparent pas
d'un angle à l'autre. Les coûts sont mesurés sur une machine partagée.

### 4.1 Angle « projection » (dossier `projection/`)

| voie | principe en une phrase | auteur | réfutateur | copie | puissance | coût par carte | change au juge |
|---|---|---|---|---|---|---|---|
| **M3** projection, toutes les coupures (classe du v9) | Poids projetés depuis la carte, bloc par bloc, sur chacune des 402 familles du v9, certificat exact, minimum des processus. | valide | tient, **sous la garde P4** | 0/1 000 dans chaque cas de sa classe ; pire cas (borne par la vraie famille) 35/2 120 [0,0115 ; 0,0229] ; moi 0/300 et 0/250 sur des mondes neufs | contre v9 **+0,045 à +0,185** sur 9 lignes, intervalles au-dessus de 0 ; part de la perte regagnée 0,41 à 0,82 ; contre La −0,110 à +0,030 | 0,46 à 0,53 s | nul v10 : produit de valeurs e de blocs, blocs = instants de lecture, pari plein seul, garde sur les cartes qui lisent l'historique, certificat journalisé |
| **M1** projection, membre linéaire du v8 | Même chose sur le seul mélange des lois connues. | valide | tient, sous la garde P4 | 50/16 240 dans sa classe ; pire cas 35/2 120 [0,0115 ; 0,0229] ; trou par morceaux 1 954/2 000 (hors classe) | contre v8 (même classe) +0,030 à +0,105 | 0,05 s | remplace le membre linéaire ; garde la classe du v8, donc le trou par morceaux |
| **M2** projection, 4 cellules de l'archive, bruit commun | Une seule famille aux poids propres à chaque cellule. | valide | tient, sous la garde P4 | 33/18 540 ; pire cas 26/2 120 [0,0080 ; 0,0179] ; hors archive 1 820/2 050 (hors classe) | contre v9 +0,110 à +0,385 ; contre La +0,015 à +0,130 | 0,05 à 0,06 s | classe des coupures de l'archive (question de sens, R-1768, R-1779) |
| **M2b** projection de La (min sur linéaire, A, B) | Version « projection » du nul limité. | valide | tient, sous la garde P4 | 25/18 440 ; pire cas 21/2 120 [0,0061 ; 0,0151] ; moi 3/300 ; hors archive 1 856/2 050, moi 227/250 (hors classe) | contre La (même classe) **+0,035 à +0,160** ; contre v9 +0,115 à +0,410 | 0,08 à 0,09 s | comme M2 |
| M2c projection, famille même des fiches (bruit par cellule) | Projection sur la famille des fiches. | valide | tient, sous la garde P4 | 20/12 540 ; pire cas 17/2 120 [0,0047 ; 0,0128] | contre v9 −0,015 à +0,300 ; contre La −0,180 à +0,045 | 0,07 à 0,08 s | comme M2, en moins bien |
| M4 horizon fixe, Bonferroni sur 8 instants | Projection recalculée à chaque instant, seuil log(8/α). | valide | tient, sous la garde P4 sur tout l'horizon (attaque partielle : deux cas) | 4/4 020 ; pire cas 4/2 000 [0,0006 ; 0,0051] | contre v9 +0,005 à +0,235 ; contre La −0,135 à +0,020 ; sous M2 | 0,18 à 0,21 s | change le seuil ; dominée |
| M5 pas à pas, avec bruit aveugle | Blocs d'une instance. | valide, sans puissance | tient | 0/14 640 (richesse ≤ 1 par calcul) | nulle par nature | 0,03 s | aucune |
| M6 pas à pas sur l'enveloppe des lois connues, min avec M1 | Chaque instance projetée sur les lois connues et l'uniforme. | valide sur sa classe, plus large | tient pour sa classe | 10/14 540 ; au plus 6/1 000 [0,0022 ; 0,0130] ; trou « bruit commun » 41/500 (auteur), 11/100 (réfutateur) | contre v9 −0,265 à +0,040 (perte sur 8 lignes sur 9) | 0,08 à 0,10 s | élargit le sens de « rien au-delà de l'archive » |
| M7 poids appris sur le passé, certifiés (correction de argon-p2-01) | Poids de la fiche en ligne, gelés par bloc, divisés par le certificat. | valide, sans puissance | tient, sous la garde P4 | 0/12 540 | au plus 0,005 | 0,07 à 0,08 s | non proposée |
| M7b M7 mêlé à la projection | Moitié poids appris, moitié projection. | valide, sans puissance | tient, sous la garde P4 | 0/12 540 | au plus 0,060 | 0,14 à 0,16 s | non proposée |
| M8 moitié, certifiée par bloc (correction de argon-p1-01) | Poids ajustés sur les blocs 1 à 4, certificat sur les blocs 5 à 8. | valide, sans puissance | tient, sous la garde P4 | 0/12 540 | au plus 0,005 | 0,01 s | non proposée |
| M9 alternative à fraction gelée par bloc | Pari à fraction gelé par bloc, puis projection. | valide | tient, sous la garde P4 (attaque partielle : deux cas) | 16/4 140 ; pire cas 16/2 000 [0,0046 ; 0,0130] | contre v9 +0,045 à +0,290 ; sous M2 partout | 0,21 à 0,23 s | remplace le pari à fraction |
| A1 fiche argon-p2-01 (en ligne, sans correction) | Le dénominateur est la loi prédictive courante. | non valide | ne tient pas | 933/1 000 [0,916 ; 0,948] à 1 000/1 000 (auteur) ; 1 880/2 020 [0,919 ; 0,941] (réfutateur) ; moi 237/300 au pire cas | sans objet | 0,002 s | écartée |
| A2 fiche argon-p1-01 (moitié, sans correction) | Poids ajustés sur les tirages 1 à 100, rapport sur 101 à 200. | non valide | ne tient pas | 582/1 000 [0,551 ; 0,613] à 814/1 000 (auteur) ; 1 662/2 020 [0,805 ; 0,839] (réfutateur) | sans objet | 0,01 s | écartée |
| P1 lois connues par tirages, certificat « comme si exact » | Certificat calculé sur des lois estimées. | non valide | ne tient pas | 429/2 000 [0,197 ; 0,233] à 50 tirages par loi | sans objet | négligeable | aucune (les lois du juge sont exactes) |
| P2 lois par tirages, certificat robuste | Certificat majoré sur une boule de confiance. | valide dans le cas d'école | tient dans le cas d'école ; borne de concentration non vérifiée sur pièce | 0/6 000 | découverte 0,18 à 0,82 contre 0,87 à 0,89 avec les vraies lois | négligeable | **non établie** pour le juge (rien avec des traits) |

### 4.2 Angle « inférence universelle » (dossier `universelle/`)

| voie | principe | auteur | réfutateur | copie | puissance | coût | change au juge |
|---|---|---|---|---|---|---|---|
| Référence : maximum certifié sur tous les tirages | Le v9 du banc (grille de 9 déciles). | valide | tient | 0/2 000 dans 8 cas ; pire carte « loterie » 1 857/40 000 = 0,0464 [0,0444 ; 0,0485] | référence 0,080 / 0,493 / 0,800 | 0,15 à 0,17 s | rien |
| Fiche argon-p2-01 | Poids en ligne. | non valide | ne tient pas | 0,955 [0,940 ; 0,967] à 1,000 (auteur) ; 0,709 à 1,000 (réfutateur) | sans objet | 0,003 s | écartée |
| Fiche argon-p1-01 | Moitié. | non valide | ne tient pas | 0,097 [0,079 ; 0,117] à 0,435 [0,404 ; 0,466] (auteur) ; 0,106 à 0,642 (réfutateur) | sans objet | 0,11 à 0,16 s | écartée |
| Moitié jugée | Maximum pris sur la moitié où l'on évalue. | valide | tient | 0 ; pire carte 0,0460 [0,0439 ; 0,0481] | contre v9 −0,070 / −0,317 / −0,300 | 0,08 à 0,11 s | ne pas adopter |
| Découpes croisées | Moyenne des valeurs e des tirages pairs et impairs. | valide | tient | 0 ; pire carte 0,0452 [0,0431 ; 0,0472] | −0,067 / −0,263 / −0,180 | 0,18 à 0,22 s | ne pas adopter |
| Sous-échantillons (4 moitiés tirées d'avance) | Moyenne de 4 valeurs e. | valide | tient | 0 ; pire carte 0,0446 [0,0426 ; 0,0466] | −0,070 / −0,223 / −0,163 | 0,37 à 0,42 s | ne pas adopter |
| Région de confiance apprise sur D1, maximum sur D0 | Forme de Berger et Boos, β = 0,025. | valide | tient ; presque dominée par le v9 (section 8.2) | 0 ; pire carte 0,0404 [0,0385 ; 0,0424] | −0,067 / −0,217 / −0,150 | 0,23 à 0,28 s | ne pas adopter |
| Lecture dense, un instant tous les 10 tirages | Même valeur e, lue à 20 instants. | valide, « ne peut que promouvoir plus » | tient, **mais la phrase est fausse** : ces instants ne contiennent pas 25, 75, 125, 175 (158 mondes sur 4 000 perdus par construction) | 0 ; pire carte 0,0465 [0,0445 ; 0,0486] | +0,007 / +0,027 / 0 ; réfutateur +0,012 / +0,013 / +0,007, dont 6 mondes perdus | 0,24 à 0,27 s | remplacée par la lecture à 40 instants (4.5) |
| Pénalité vers le bas (1 nat ; (d/2)·log t) | Dénominateur baissé d'une constante. | non valide | ne tient pas | complexité : 1,000 ; 1 nat : 0 sur copie, mais 1 197/10 000 = 0,120 [0,113 ; 0,126] sur carte « loterie » | sans objet | celui du v9 | écartée |
| Mélange a priori des membres (fable-p1-05) | Moyenne pondérée des membres au dénominateur. | non valide | ne tient pas | 0,179 à 0,543 (auteur) ; 0,110 à 0,467 (réfutateur) | sans objet | celui du v9 | écartée (garantie α/π) |
| Un instant de rejet par famille (constat du réfutateur, section 8.1) | Chaque famille rejetée à son propre instant. | (non étudiée) | valide pour la carte seule ; pas une valeur e | 0 sur copies ; mondes « tranchants » : mêmes promotions que le v9 | 0, +2, +1 monde sur 300 | gratuit | voir 4.5 |

### 4.3 Angle « ensemble de confiance » (dossier `confiance/`)

| voie | principe | auteur | réfutateur | copie | puissance | coût | change au juge |
|---|---|---|---|---|---|---|---|
| BB_A (ensemble sur les tirages jugés eux-mêmes) | Suite de confiance sur les tirages frais. | valide | tient (validité seule) | 0/1 000 [0 ; 0,0037] ; réfutateur 0/15 000 ; pire carte 11/1 000 [borne haute 0,0196] | jamais plus que le v9 (lemme 1) ; perd β | 0,04 s en plus | écartée |
| BB_T_seq (ensemble séquentiel sur les 100 tirages d'entraînement) | Ensemble par Ville sur l'entraînement. | valide | tient (validité seule) ; gain annoncé à 1 000 tirages **non retrouvé** | 0/15 000 | à maxima serrés : 0 à −0,02 contre v9 | 0,21 à 0,92 s | écartée |
| BB_T_coupe (ensemble universel coupé sur l'entraînement) | La moitié de l'entraînement centre un ensemble. | valide ; regagne 14 %, 42 %, 55 % à 1 000 tirages | tient (validité seule) ; **le gain ne tient pas** : 0 %, 0 %, −7 % à maxima serrés (le v9 du banc était sous-optimisé, 80 pas) | 0/15 000 ; non-couverture au plus 13/2 000 | perd le prix β avec 100 tirages ; nul avec 1 000 | 0,15 à 0,45 s (sous-estimé, 12 à 300 fois le v9 en compte) | écartée |
| BB_S_moitie | Ensemble sur la première moitié des tirages frais. | valide | tient (validité seule) | 0/15 000 ; pire carte 18/2 000 | perd toujours (0,130 / 0,350 / 0,670 contre 0,310 / 0,610 / 0,850) | 0,07 s | écartée |
| BB_Q_blocs | Maximum par bloc sur une suite de confiance. | valide | tient (validité seule) | 0/15 000 ; pire carte 3/1 000 | perd toujours (0,040 / 0,200 / 0,530) | 0,26 à 1,12 s | écartée |
| F1 en ligne (argon-p2-01) | Artefact. | non valide | ne tient pas | 0,936 [0,919 ; 0,950] à 1,000 (auteur) ; 80,3 % à 100 % (réfutateur) | sans objet | 0,002 s | écartée |
| F2 moitié (argon-p1-01) | Artefact. | non valide | ne tient pas | 0,052 [0,039 ; 0,068] au sommet à 0,318 [0,289 ; 0,348] (auteur) ; 5,0 % à 48,8 % (réfutateur) | sans objet | 0,007 s | écartée |

Réserve commune aux cinq BB (réfutateur, R1) : elles perdent une protection du v9. Une carte qui est elle-même un membre du
nul peut être promue quand le monde est hors du nul : de 6,9 % à 23,9 % dans un calcul exact, contre 0 pour le v9.

### 4.4 Angle « borne de regret » (dossier `regret/`)

| voie | principe | auteur | réfutateur | copie | puissance | coût | change au juge |
|---|---|---|---|---|---|---|---|
| R0-a en ligne sans correction (argon-p2-01) | Loi prédictive au dénominateur. | non valide | l'échec est réel | 72,9 % [70,0 ; 75,6] à 99,9 % ; 0 au sommet, masqué par un membre ordinaire | sans objet | 0,03 à 0,04 s | écartée |
| R0-b moitié (argon-p1-01) | Algorithme EM sur la première moitié. | non valide | l'échec est réel | 9,9 % [8,1 ; 11,9] à 30,0 % [27,2 ; 33,0] | sans objet | 0,03 à 0,05 s | écartée |
| R1 portefeuille universel plus sa borne | Mélange uniforme sur les poids, plus une borne de regret prouvée. | valide, dominée | tient **pour le mélange exact** ; version estimée **non établie** (erreur de −2,54 à +2,74 nats) | 0/2 000 dans 12 cas | 0 / 0 / 0,4 % contre 0,8 / 22,6 / 63,8 % pour le maximum ; jamais une promotion de plus | 0,1 à 0,9 s en plus | écartée (théorème 2) |
| R2 gradient exponentié lissé plus borne de Hedge | Borne de 196 à 228 nats. | valide, inutilisable | tient | 0 partout | 0 | 0,03 à 0,2 s | écartée |
| R3 borne dépendante des données | Identité : redonne le maximum certifié. | valide, égale au maximum | tient | celui du maximum | égale | plus cher | rien à adopter |
| R4 mélange sur les découpages plus log(1/π_min) | Valide par inégalité, dominé par R1. | valide | tient (par inégalité, sans essai séparé) | au plus celui de R1 | au plus celle de R1 | celui de R1 | écartée |
| R5 constante calibrée par simulation | Diviser par une constante plus petite que la borne. | non valide en garantie, non essayée | rejet fondé, essayée | calibrée sur un seul type de monde : 35,6 % à 98,5 % ailleurs | calibrée au pire cas : 0,0 / 0,5 / 21,4 % contre 0,8 / 22,6 / 63,8 % | simulation par carte | écartée |

### 4.5 Angle « toute autre voie » (dossier `libre/`)

| voie | principe | auteur | réfutateur | copie | puissance | coût | change au juge |
|---|---|---|---|---|---|---|---|
| Référence v9 du banc | Maximum certifié sur toutes les coupes observées. | valide | tient | 0/22 000 ; carte « tout ou rien » 0,01525 [0,0117 ; 0,0196] | 0,336 / 0,650 / 0,792 | 0,16 s | rien |
| La (coupures de l'archive) | Nul plus petit. | valide sur sa classe | tient sur sa classe seulement | 0/14 000 dans sa classe ; hors classe 0,90 à 0,99 | +0,140 / +0,118 / +0,084 ; **+0,078 / +0,072 / +0,062 avec les membres log-linéaires** | 0,10 s | nul plus petit (question de sens) |
| Ld (La plus partitions déclarées) | Nul plus petit, ferme la sous-population. | valide sur sa classe | tient sur sa classe seulement | 0/18 000 ; hors classe 0,77 à 0,89 | +0,104 / +0,104 / +0,064 ; avec log-linéaires +0,066 / +0,067 / +0,047 | 0,10 s | idem |
| Grille de déciles | Coupes fixées d'avance aux déciles. | valide sur sa classe | tient sur sa classe seulement | 0/12 000 ; hors classe 0,27 à 0,58 (y compris la coupure de l'archive : 0,377) | +0,064 / +0,072 / +0,044 ; avec log-linéaires +0,034 / +0,035 / +0,026 | 0,07 s | idem, le plus petit gain |
| Mc seuil simulé au pire cas sur une grille de 17 points | Seuil critique simulé. | non valide | ne tient pas | 0,269 à 0,617 | −0,056 à −0,084 sous le v9 | 0,13 s | écartée |
| Mc2 grille plus projection de la carte | Idem, plus un point projeté. | non valide (dépasse au bord) | **indéterminé** : avec le rang exact, bord 0,0575 [0,0477 ; 0,0686] | **non établie** | −0,29 à −0,35 sous La | 0,15 s | écartée (aucune preuve, puissance la plus basse) |
| Md rééchantillonnage sous le nul ajusté | Seuil simulé sous le nul ajusté. | non valide | ne tient pas | bord 0,102 [0,084 ; 0,122] | −0,13 à −0,22 sous le v9 | 0,11 s | écartée |
| Filtre « OU » | La ou v9, chacun à α/2. | non valide | ne tient pas | copie hors archive 0,9295 [0,917 ; 0,940] | sans objet | somme | écartée |
| Filtre « ET » | La et v9. | valide | tient | comme le v9 | égale au v9, monde pour monde | somme | sans intérêt |
| Pari mixte ½ W_La + ½ W_v9 | Moyenne de deux richesses. | non valide | ne tient pas | 0,940 | sans objet | somme | écartée |
| Méthode 10 : élagage certifié par la carte | Retirer un membre par une borne de Chernoff. | non valide (non mesurée) | indéterminé | **non établie** (aucun certificat) | non mesurée | — | écartée faute de certificat |
| Méthode 11 : poids appris sur d'autres données | Nul ajusté sur des tirages d'autres cartes. | non valide | ne tient pas (aucune garantie) ; mais « mêmes taux » est faux avec 10 fois plus de données (0 à 0,023) | N' = 200 : 0,20 à 0,70 | non mesurée | faible | écartée |
| Méthode 12 : seuil certifié plus bas | Baisser le seuil sous log(1/α). | non valide (aucun certificat) | indéterminé ; un tel seuil existe en principe | **non établie** | non mesurée | — | ouverte, sans certificat |
| A1, A2 artefacts | Fiches. | non valides | ne tiennent pas | A1 0,999 à 1,000 ; A2 0,19 à 0,64 | sans objet | — | écartées |
| **Lecture à 40 instants** (réfutateur, section 10) | Même valeur e que le v9, lue tous les 5 tirages ; les 8 instants du juge en font partie. | (non étudiée) | valide sur toute la classe du v9 (Ville) | 0/1 000 copies ; non-copies ≤ 0,006 ; moi : 0 domination violée sur 2 500 mondes | +0,012 à +0,023 ; aucune carte perdue | celui du v9 fois 5 instants | change `instants_lecture` ; nœud |
| **Rejet membre par membre** (réfutateur, section 10) | Chaque famille du nul doit être rejetée à au moins un instant, pas forcément le même. | (non étudiée) | valide sur toute la classe du v9 ; preuve écrite par le réfutateur lui-même, **non contre-lue par un tiers** (je l'ai suivie : aucun pas faux) | 0/22 000 copies ; « tout ou rien » 0,02275 [0,0184 ; 0,0279] ; moi 5/1 000 et 2/500 en dense | +0,005 à +0,008 seule ; **+0,020 à +0,032 avec les 40 instants** (juge complet approché +0,027 / +0,032 / +0,027) | gratuit | règle de lecture ; ce n'est **pas une valeur e** : ne se branche pas tel quel sur la règle e-BH |

## 5. Pourquoi les deux façons des fiches échouent, et la condition que respectent les voies valides

**En une phrase.** Les deux fiches remplacent le maximum du nul par **une seule loi devinée à partir des tirages**, qui ne
majore pas la vraisemblance du vrai membre. Pour une copie exacte, l'espérance du rapport vaut alors Σ P*²/p ≥ 1 : c'est le
regret du prédicteur, et la richesse monte d'elle-même (en ligne). Ou encore, sachant la première moitié, elle vaut Π Σ P*²/p_ŵ ≥ 1 (moitié).

**La condition des voies valides.** Chaque voie valide garde l'une des deux propriétés suivantes, et aucune autre ne l'a
été :
- (a) **le dénominateur domine trajectoire par trajectoire** la vraisemblance de chaque membre sur les tirages jugés. C'est
  le cas du maximum certifié du v9, de la moitié jugée, de la région de confiance, du portefeuille universel avec sa borne et
  des nuls plus petits. Le lemme A montre que le maximum est alors le plus petit dénominateur possible : ces voies ne
  peuvent pas battre le v9 à lecture égale (universelle, regret, libre) ;
- (b) **la valeur e de chaque bloc a une espérance au plus 1 sous chaque membre**, parce que les poids et la loi de la carte
  sont fixés avant le bloc et que le certificat exact est divisé (lemme 1 de la projection). Seule cette voie sort du
  plancher du lemme A, et c'est elle qui rend la puissance. Elle exige que **rien de ce qui entre dans le bloc ne lise les
  issues du bloc**, ni les poids du nul ni la loi de la carte (garde P4).

Les deux règles de lecture (40 instants, membre par membre) gardent (a). Elles gagnent un peu parce que le lemme A ne parle
que d'une lecture au même instant pour tous les membres, aux 8 instants du juge.

## 6. Bras recommandés pour la version 2 du préenregistrement de l'idée 1.1

Je propose ; le concepteur de la version 2 décide, et la contre-lecture tranche. Les bras s'ajoutent au banc B de la v1, que
je ne change pas, sauf les corrections déjà demandées par la contre-lecture (M1 : ligne V5 sur une coupure de l'archive ;
M2 à M4 : code du v9 et tolérances).

**Bras à jouer, dans l'ordre :**
1. **J8 et J9** (inchangés) : ce sont les références. Le prix du v9 doit d'abord se reproduire sur ce banc.
2. **La et Ld** (inchangés, sous la forme corrigée par la contre-lecture) : c'est la question de départ. Le gain de La sur
   le v9 tombe d'environ un tiers à la moitié quand on garde les membres log-linéaires du v8. La version 2 doit donc les
   garder dans tous les bras, ce que font J8 et J9.
3. **J9-P, projection par blocs sur la classe du v9 (M3)** : c'est le seul bras qui peut répondre « oui » à R-1779 sans
   rouvrir aucune copie. Il remplace, pour les membres linéaires en leurs poids, le maximum par un produit de blocs, en
   minimum avec la richesse actuelle des membres ordinaires et log-linéaires. Conditions à écrire avant le jeu : pari plein
   seulement ; blocs = intervalles entre les 8 instants ; projections calculées au gel et journalisées ; nombre de pas de
   l'optimiseur gelé ; certificat journalisé par bloc ; seuil d'audit écrit pour « une carte membre reste près de 1 »
   (l'audit « jamais au-dessus de 1 » ne vaut plus) ; règle de marge des filles redéfinie ou laissée au maximum ;
   **garde P4** : refus au gel de toute carte qui contient un type qui lit l'historique (« sans_remise »,
   « moyenne_glissante »), ou historique gelé au début du bloc. Le banc B n'a que des cartes sans mémoire. Il ne verrait
   donc pas le trou : voir le point 6.
4. **La-P, projection de La (M2b)** : même classe que La. Elle sépare ce qui vient de la projection de ce qui vient de la
   restriction de classe, et dit si « projection et classe du v9 » (J9-P) suffit, ou s'il faut aussi rétrécir.
5. **J9-D, v9 lu à 40 instants et rejeté membre par membre** : règle de lecture seule, même classe et même dénominateur que
   J9. Gain petit mais gratuit, et monde pour monde jamais inférieur à J9 sur les mondes rejoués. Le bras se lit comme un test
   de niveau α pour la carte seule. Ce n'est pas une valeur e : son branchement sur e-BH reste un nœud à part.
6. **Témoins à ajouter** (dents du banc, sans verdict sur le juge) : A1 et A2 (les deux fiches, sans correction), qui doivent
   promouvoir les copies Q1 et Q2 (borne basse > 0,5 pour A1, > 0,05 pour A2). Ajouter aussi une ligne « carte qui lit
   l'historique du bloc » (forme du réglage 7, plus « sans_remise » de la grammaire) jouée par J9-P avec et sans garde : sans
   garde elle doit promouvoir, avec garde rester sous α. Sans ces témoins, le banc ne montre pas qu'il voit les défauts que
   les bras corrigent (règle R5).

**Bras à ne pas jouer, avec la raison :**
- M1, M2, M2c, M4, M9 : même classe que J8 ou que La-P, et dominés par M3 ou M2b sur le banc de l'angle.
- M5 (sans puissance par nature) ; M7, M7b, M8 (corrections valides des fiches, sans puissance : au plus 0,06).
- M6 : elle change le sens de « rien au-delà de l'archive » et perd contre le v9 ; question de sens d'abord.
- Les cinq bras à ensemble de confiance : à maxima serrés, aucun gain, et ils perdent la protection « une carte membre
  n'est jamais promue ».
- La famille du regret (R1 à R5) : dominée par le maximum, par un théorème.
- Moitié jugée, découpes croisées, sous-échantillons, région de confiance de l'angle universel : valides, mais elles perdent
  de 0,07 à 0,32.
- Lecture tous les 10 tirages : elle ne contient pas les instants du juge ; elle est remplacée par la lecture à 40 instants.
- Grille de déciles : nul plus petit au gain le plus faible, qui laisse passer la coupure de l'archive elle-même.
- Pénalités, mélange a priori, seuils simulés (Mc, Mc2, Md), « OU », pari mixte, méthode 11 : non valides ou non établies.
  Filtre « ET » : égal au v9.
- P1 et P2 : les lois du juge sont exactes. P2 reste à reprendre seulement si une archive à lois estimées apparaît.

Ce que la version 2 doit dire en plus : ces bras font des nuls v10 candidats. Le jeu ne les branche pas ; un résultat
favorable ouvre un nœud du directeur avec sa propre validation scellée.

## 7. Ce qui reste non vérifié

**Références non lues sur pièce** (toutes « à vérifier sur pièce » ; aucun chiffre n'en est repris) : inégalité de Ville ;
numéraire et projection d'information inverse (Larsson, Ramdas et Ruf) ; « Safe testing » (Grünwald, de Heide et Koolen) ;
inférence universelle (Wasserman, Ramdas et Balakrishnan) ; tests de Berger et Boos ; borne de concentration en norme 1
(Weissman et al.) utilisée par P2 ; portefeuille universel (Cover) et borne de Hedge ; correction minimax de Shtarkov ;
règle e-BH et règle de Benjamini et Yekutieli. Les réfutateurs ont vérifié les pas de preuve par calcul, pas les textes.

**Résultats vus seulement sur un banc réduit** :
- Tous les gains de puissance sont mesurés sur les bancs des angles, pas sur le juge. Ces bancs ont deux à quatre lois
  connues, un code du v9 recopié et simplifié, souvent une grille de seuils au lieu de tous les seuils, et pas de membres
  log-linéaires (sauf le bras « complet approché » du réfutateur libre). Le vrai code du v9 n'a jamais été exécuté (règle des
  dossiers de copie).
- Le gain de M3 (+0,045 à +0,185) repose sur un banc à 100 ou 200 mondes par dose. La référence R9 y perd jusqu'à 0,37
  contre R8, bien plus que le vrai v9 (0,105 au plus dans son verdict). L'ampleur ne se transpose pas. Sa puissance a été
  rejouée, pas refaite sur un banc indépendant ; la référence R9 n'est encadrée que sur 18 mondes (à 0,004 nat de la valeur
  atteinte). Avec les membres log-linéaires, le gain de M3 n'est pas mesuré : par analogie avec La, il pourrait baisser.
- Pour M4 et M9, l'attaque n'a porté que sur deux cas. Mon M3 complet est joué sur 550 mondes neufs ; l'amplification du
  réfutateur sur 100 engagements.
- La lecture à 40 instants et le rejet membre par membre ne sont éprouvés que sur le banc du réfutateur libre ; leur preuve
  n'est pas contre-lue par un tiers. La lecture de la valeur e arrêtée membre par membre n'a pas été jouée.

**Désaccords entre auteur et réfutateur non résolus** (l'auteur n'a pas répondu ; je rapporte sans trancher, sauf mention) :
1. **Garde P4 (projection)** : l'auteur dit P4 « vraie au pari plein » ; le réfutateur montre que c'est faux pour la
   grammaire du juge (198/400 dans mon rejeu). Limites dites : la carte du réglage 7 n'est pas vérifiée comme écrivable dans
   la grammaire ; la loi « sans_remise » seule est couverte dans le juge complet par le membre « uniforme » ; les mélanges
   de « sans_remise » cassent l'espérance (1,011 à 1,031) sans rien promouvoir (0/4 000).
2. **Gain de BB_T_coupe** (confiance) : l'auteur annonce 14 %, 42 %, 55 % ; le réfutateur trouve 0 %, 0 %, −7 % avec un
   maximum serré. Il attribue le gain à un v9 du banc calculé en 80 pas, loin du vrai maximum (écart médian 2,1 nat). Je
   tiens la démonstration du réfutateur pour convaincante, mais elle n'est pas contre-lue. **Avertissement transversal** :
   tout banc qui sous-optimise le maximum fabrique un faux gain. Le banc de la projection a été vérifié sur ce point, mais
   sur 18 mondes seulement.
3. **Origine du prix du v9** (universelle) : l'auteur dit « surtout la liberté des poids par morceau » ; le réfutateur
   trouve des parts égales sur une base sans coupure.
4. **« Aucune méthode valide plus puissante »** (libre) : la phrase est fausse à cause des deux règles de lecture, mais le
   gain est petit. Le fond tient à peu près.
5. **Mc2** (libre) : l'auteur la dit non valide ; le réfutateur dit « indéterminée » (règle de quantile). Elle reste non
   établie, et sans intérêt pratique.
6. **Estimateur du mélange de R1** (regret) : l'auteur annonce une erreur de −0,20 à +0,38 nat ; le réfutateur mesure −2,54 à
   +2,74 en dimension 4 et 5. La version estimée n'est pas établie ; la version exacte l'est. Sans effet sur la décision.
7. **Le « v9 du banc »** (universelle, confiance, libre) n'est pas le v9 : avec la grille de déciles, il promeut 50,8 % des
   copies coupées entre deux déciles (universelle) et 66/150 sur un seuil hors grille (confiance). Les tailles « sur toute la
   classe du v9 » de ces angles ne sont donc pas montrées. La projection, elle, joue toutes les coupures du plan.
8. **Réserve R1 de la confiance** (perte de la protection d'une carte membre) : non discutée par l'auteur.

## 8. Options épuisées

Chaque option essayée ou écartée, en une ligne :
1. Poids appris en ligne, sans correction (argon-p2-01) : non valide, vu dans les cinq bancs (de 72,9 % à 100 % des copies).
2. Poids ajustés sur une moitié, sans correction (argon-p1-01) : non valide, vu dans les cinq bancs (de 5 % à 81 %).
3. Mélange a priori des membres (fable-p1-05) : non valide (garantie α/π).
4. Poids appris sur le passé, gelés par bloc, certificat exact (M7) : valide, sans puissance.
5. Moitié certifiée par bloc (M8) et mélange appris plus projection (M7b) : valides, sans puissance.
6. Projection par blocs sur la classe du v9 (M3) : **valide sous la garde P4, regagne la moitié environ de la perte du v9**.
7. Projection sur le membre linéaire (M1), sur 4 cellules (M2, M2c), version projection de La (M2b) : valides sous la garde
   P4, gagnent sur leur référence de même classe.
8. Projection à horizon fixe avec Bonferroni (M4) : valide, dominée par les blocs.
9. Projection pas à pas (M5) : valide, puissance nulle par nature.
10. Projection pas à pas sur l'enveloppe des lois connues (M6) : valide sur une classe plus large, perd.
11. Alternative à fraction gelée par bloc (M9) : valide, dominée.
12. Numéraire exact par bloc : non calculable (3^25 suites par bloc).
13. Une seule projection sur tout l'horizon, lue aux 8 instants : non valide aux instants intermédiaires.
14. Minimum sur les familles pris bloc par bloc : valide, dominé.
15. Lois connues seulement par tirages, certificat « comme si exact » (P1) : non valide ; certificat robuste (P2) : valide
    dans le cas d'école, sans objet pour le juge.
16. Moitié jugée, découpes croisées, sous-échantillons : valides, perdent.
17. Région de confiance sur une moitié, maximum sur l'autre (Berger et Boos) : valide, presque dominée par le v9.
18. Ensembles de confiance sur l'entraînement (BB_A, BB_T_seq, BB_T_coupe, BB_S_moitie, BB_Q_blocs) : valides, aucun gain à
    maxima serrés.
19. Ensembles de type « moments », prédicteur plus riche que le nul, ensembles asymptotiques : écartés (sens changé, ou
    garantie seulement à la limite).
20. Portefeuille universel avec sa borne (R1), Hedge lissé (R2), borne dépendante des données (R3), mélange sur les découpages
    (R4) : valides, dominés ou égaux au maximum.
21. Constante calibrée par simulation (R5) : non valide en garantie, perd une fois calibrée au pire cas.
22. Dénominateur pénalisé vers le bas (1 nat, ou complexité) : non valide.
23. Lecture tous les 10 tirages : valide, mais elle ne contient pas les instants du juge.
24. Lecture à 40 instants : valide, petit gain.
25. Rejet de chaque famille à son propre instant : valide, petit gain, pas une valeur e.
26. Nuls plus petits (La, Ld, grille de déciles) : valides sur leur classe seulement ; gain réel, mais ils rouvrent des
    copies.
27. Filtres « OU », pari mixte : non valides ; filtre « ET » : égal au v9.
28. Seuils simulés (Mc, Mc2, Md) : non valides ou non établis.
29. Élagage des membres certifié par la carte (méthode 10) : non établi, aucun certificat.
30. Poids appris sur d'autres données indépendantes (méthode 11) : aucune garantie.
31. Seuil certifié plus bas que log(1/α) (méthode 12) : non établi ; un tel seuil existe en principe, mais aucun certificat.
32. Tests par permutation ou conditionnels : écartés (aucune échangeabilité, aucune statistique suffisante simple).
33. Partage de α entre membres à la façon de Bonferroni : inutile (lemme B).
34. Poids bornés loin du bord : c'est un changement de classe, pas un apprentissage.
35. Vérifier E[q/D] ≤ 1 par simulation : ce n'est pas une preuve, car le pire membre est au bord.

Restent ouvertes, non essayées : la projection combinée à une lecture plus dense (blocs plus petits, donc moins de
puissance par bloc, et à mesurer) ; la projection avec membres log-linéaires et le vrai code du v9 ; un certificat de seuil
pour la méthode 12.

## 9. Fichiers de cette synthèse

Dossier `docs/notes/organisme-idees-juge-v1/correction-poids-v1/synthese-rejeu-v1/`. Chaque fichier y est scellé par un
compagnon `.sha256`, journaux compris.

| empreinte (sha256) | fichier |
|---|---|
| `e5e258d75047b2611ab48548f325db4080e91cf148c39c0ca586eba3f5b3addf` | `rejeu-projection-taille-pire_lin_d06-r5000-5300-v1.json` |
| `e918dc3950db6dded9fd6456984a4d489609a86400eb6b01b5e6824a079fb52c` | `rejeu-projection-taille-copie_coupure_hors-r5000-5250-v1.json` |
| `d89977d6547dd77cce7e12014fc85a85f83a948fa19a6d1f5c5348fb4ad896fc` | `rejeu-projection-memoire-7-v1.json` |
| `ef2fa7f8c6a6b66456d28d823108adcaea42d1efdeba02b58376f8c8bb557de4` | `rejeu-projection-puissance-V4-d1-r0000-0100-v1.json` |
| `d65b98ee40e8d37b3e733240720d93374052a114e93ebcaf6fbd00b8d0eb70e1` | `rejeu-libre-dense-N1b-0-v1.json` |
| `7450add41edfb3c83988b5433cb957d71de51fbba398de0b665b103c6cc444b8` | `rejeu-libre-dense-N1b-1-v1.json` |
| `6f75433e7fa0c3ead4bec75de18e4bd9aaa7aa291ff5986bdb1daa2971edfe41` | `rejeu-libre-dense-N1b-2-v1.json` |
| `a50c5f7bfc5cd51dca09230ee670bd76d0c3a9e16ee9d5ec0f4528ec6d506316` | `rejeu-libre-dense-N1b-3-v1.json` |
| `dfe732a278837a45edcdb387292e0f7dcb0cdbd05132b09a4227a3b255fa6502` | `rejeu-libre-dense-P1-0-v1.json` |
| `47f1e0784da3ebb3fde68054b93a038f184b15f45ee0460df00fc9292e864cf6` | `rejeu-libre-dense-P1-1-v1.json` |
| `f551980f3c4dda0b6b64ddcc8b809b01a85a4fc098b516b4d5122a196a699192` | `rejeu-libre-dense-P1-2-v1.json` |
| `0ceaf7d4350ac5a95bf6525478854935a0613690370e2cbd318e3857e48c6363` | `rejeu-libre-dense-P1-3-v1.json` |
| `f32858685a199fd70b1cb644d75709118f318681124a213a72747c48d1ee96ea` | `neuf-libre-dense-N1b-10-v1.json` |
| `93beb7eceaca0bfb82f9fd743a0cd0c62dc1a15ab5ecbf28427d587a15d0c9de` | `neuf-libre-dense-N1b-11-v1.json` |
| `9284bedd89c31f60031ee75bc0654b427a6e5f93ca466cbc2f4137b7a9beeca7` | `neuf-libre-dense-N1b-12-v1.json` |
| `7effa6d9b92f75eb6b260350e6b3dd077565c929fc3a702c43d151b1f36ab533` | `neuf-libre-dense-N1b-13-v1.json` |
| `c49e15d5416a6cb04152fb8611567c380a4c495f4ad525a4d6630f278465719f` | `neuf-libre-dense-N2b-10-v1.json` |
| `be278285eefaed2fc098236a61edfcdd043f23690f1e379ed62f2c6a61a11ac5` | `neuf-libre-dense-N2b-11-v1.json` |

Aucun fichier d'un auteur ou d'un réfutateur n'a été modifié, et aucun dossier de cache n'a été écrit (option `-B`).
Je n'ai fait aucun commit, aucun appel réseau, aucun appel payant, et je n'ai rien écrit sous `diag/` ni sous `donnees/`.

**Rappel.** Tout ceci est exploratoire. Le résultat décisif viendra du préenregistrement scellé (version 2 de l'idée 1.1).
Adopter une de ces voies dans le juge est une décision du directeur.
