# Conception — monde riche écrit par un programme et regroupement des doublons au sein d'une génération — v4 (famille revue, Q-13 (c))

- **Statut** : conception **v4** (aucun préenregistrement, aucun GO consommé). Elle répond au mot de Lazar **R-2492** sur la
  note de décision du préenregistrement (`preenregistrement-v1/note-decisions-lazar-v1.md`,
  `d2bcf5810be0ac7cec214eb908a873a2a98cb6500ce74478868cc3eb68f2b2ee`, vérifiée contre son compagnon) : recommandations retenues
  (Q-1 (b) 2 × 3 ; Q-3 (c) ; Q-9 (a) ; Q-10 (a) ; Q-11 (a) ; Q-12 (i) (a), (ii) un tiers) et **Q-13 (c) : revoir la famille des
  mondes**, avec la règle de garde écrite d'avance. Lignes inscrites : **GO-2026-11-13-01** (365 USD sur crédits) et
  **GO-2026-11-13-02** (57 USD) (`registres/go.md`, lignes 314 et 315), dont une condition est « conception v4 (famille revue,
  Q-13 (c)) contre-lue » et « devis revu après la v4, sous ce plafond ». **Aucune dépense, aucun appel de modèle, aucune écriture
  git** : calcul seul, un processus à la fois (`ulimit -v 6000000`, `OMP_NUM_THREADS=2`), par parties scellées.
- **Ce qui reste valable de la v3** (`conception-monde-riche-doublons-v3.md`,
  `386d48bacd6c487d88846d0991d83bd4ad95122f70500d6fbeb7859cde56659c`, versée inchangée, R12) : **tout ce que ce texte ne
  remplace pas** — regroupement des doublons (§3), représentant à tranche de choix appariée (§3.4), diversité (§4), proposeurs
  (§5), garde du secret (§2.5), jeu planté (§1.5), loi connue de départ (§1.4), vérité des découvertes (§1.7). La v4 remplace
  la **famille** (§1.2 de la v3 → §2 ici), complète le **vérificateur** (§2.3 de la v3 → §2.4 ici), ajoute la **règle de garde**
  (§3), refait les **simulations de génération** (§4), le **devis** (§5) et dit **ce qui change pour le préenregistrement** (§6).
- **Concepteur** : Claude Opus 5.5 (`claude-opus-5-5`), le même sous-agent que pour les v1 à v3 (session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`). Je n'ai écrit ni le préenregistrement, ni sa contre-lecture, ni la note de décision.
- **Interpréteur** : Python 3.13.18 et numpy 2.5.3 du système ; scellement par `.venv/bin/python -m controle_ia.scellement`.

- **Heures** (relevées par `date -u`) : début 2026-11-13 07:49:28 ; code v4 scellé 08:02 ; parties 08:02:15 → 09:17:45 ;
  fin de la rédaction 2026-11-13 09:20:16 (`date -u`).

## Changements depuis la v3

| # | demande (R-2492, message de la mère) | ce que fait la v4 | où |
|---|---|---|---|
| 1 | famille revue où il reste, après une génération 1 simulée, des composantes certifiées à trouver | famille **MR-2** : 1 ou 2 composantes **conditionnelles** (pente de z_t de signe opposé selon le signe de z_B, z_B le trait d'une moyenne ; la seconde chaînée sur la première), taille d'une moyenne, **toutes certifiées** ; au plus 10 composantes ; conditions ≤ 3 ; 48 feuilles | §2 |
| 2 | construction justifiée | marginalement nulle par symétrie ; **mesuré** : part marginale médiane 0,0195 (14 conditionnelles) contre 0,47 (18 moyennes) ; alternatives écartées dites | §2.1, §2.3, §4.3 |
| 3 | rien réglé sur un signe (R3) | code, modèle de proposeurs et règle **scellés avant toute partie** (`4b165847…`, 08:02) ; un seul passage ; variante sans masquage rapportée | §3.2, §4, §7 |
| 4 | règle de garde écrite d'avance | texte recopié ; définitions opératoires (mondes, génération 1 simulée, certifiée, encore trouvable, seuil, suite d'un échec) | §3 |
| 5 | simulations v4 (mêmes proposeurs, code v3b sinon), dont la règle | 12 mondes conformes (12 refus de tirage) ; **règle : 8 sur 12 avec masquage (tenue), 0 sur 12 sans** ; progrès certifié en génération 2 ou 3 dans 8 mondes sur 12 (v3b : 0) ; fausses 36 sur 204 | §4 |
| 6 | devis revu sous 365 et 57 USD | pire inchangé : 363,00 (marge 2,00) et 56,20 (marge 0,80) ; central 41,11 | §5 |
| 7 | ce qui change pour le préenregistrement | décisions R-2492 portées ; table section par section | §6 |
| — | m de C8 | 48 (règle V-4) au lieu de 44 | §2.4 |
| — | questions neuves | Q-14 (règle qui ne tient que sous masquage), Q-15 (12 ou 24 mondes de calibration) | §7 |

## 0. En dix lignes

1. Constat C-1 : sur MR-1, la génération 1 prend toutes les fortes et moyennes ; progrès certifié dans 0 monde sur 12.
2. Cause : chaque composante MR-1 se voit seule, dans la marginale de son trait ; rien n'ordonne les découvertes.
3. MR-2 ajoute 1 ou 2 composantes **conditionnelles** (taille moyenne) **invisibles marginalement** : leur pente change de signe
   avec le signe du trait d'une moyenne (ou de la conditionnelle précédente) ; part marginale médiane 2 %.
4. Elles sont **certifiées** (C8, m = 48) dans tous les mondes gardés ; 12 sur 12 mondes conformes, 12 tirages refusés avant.
5. Règle de garde (mot de Lazar) définie et gelée avant les calculs ; mesurée ici sur 12 graines de développement.
6. **Avec masquage** (une conditionnelle proposée à 0,02 tant que sa condition n'est pas connue, 0,25 ensuite ; estimé) :
   **8 mondes sur 12** gardent une certifiée après la génération 1 : la règle **tient** (Wilson [0,39 ; 0,86]).
7. **Sans masquage** : **0 sur 12** : la règle ne tient que sous l'hypothèse sur les proposeurs ; seul le pilote la mesurerait.
8. Avec masquage, progrès certifié en génération 2 ou 3 dans 8 mondes sur 12 ; la génération 3 reste presque vide (1 monde).
9. Devis : pire inchangé, 363 sous 365 et 56,20 sous 57 USD ; marges minces ; central ≈ 41 USD.
10. Pour le préenregistrement : famille MR-2, règle à la liste d'arrêt avant tout appel payant, décisions R-2492 portées ;
    Q-14 et Q-15 à trancher.

## Pièces lues (chemin, empreinte, vérifiées contre leur compagnon)

| pièce | empreinte |
|---|---|
| `preenregistrement-v1/note-decisions-lazar-v1.md` | `d2bcf5810be0ac7cec214eb908a873a2a98cb6500ce74478868cc3eb68f2b2ee` |
| `preenregistrement-v1/comptes_c1_c4_v3b_v1.py` et `.json` (C-1) | `54dfbbb2…` ; `0599ae20…` |
| `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon3.md` (§3, §17, en partie) | `2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39` |
| `conception-monde-riche-doublons-v3.md` (la mienne) | `386d48bacd6c487d88846d0991d83bd4ad95122f70500d6fbeb7859cde56659c` |
| `registres/go.md`, lignes de GO-2026-11-13-01 et -02 (lecture seule) | — (registre vivant) |
| outils v1, v2, v3 et v3b (importés, non modifiés) | v3 §« Pièces écrites » |

## Pièces écrites (v4 ; toutes scellées, compagnon `.sha256`)

| pièce | empreinte |
|---|---|
| `outils-v4/monde_riche_v4.py` (famille, vérificateur v4, part marginale, course, règle) | `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` |
| `outils-v4/lancer_sorties_v4.sh` | `e2f6e0eab2879dbf4110f847d4812fee5dde32a66939496ddf66ff0ad0822339` |
| `outils-v4/table_v4.py` | `1b48486ad3b3dc69842ceb8151a2ce3719b609db31e70686dcac8cc2e0a22ffc` |
| `outils-v4/devis_multi_generations_v4.py` | `f166fa4abed34b87dce9e58a8d7c786764d4f0866b8119cae010de88fcb356f9` |
| `sorties-v4/partie-v4-monde-{0…11}.json` (et `.stdout`) | compagnons ; 0 `91841b78…`, 1 `909ba9ce…`, 2 `c0bb5fb2…`, 3 `c2f8c90d…`, 4 `29376e0b…`, 5 `61d37b71…`, 6 `d52c8795…`, 7 `c5af3a9d…`, 8 `8ad0c726…`, 9 `d611ca03…`, 10 `e313daf3…`, 11 `adbeed10…` |
| `sorties-v4/resume-v4.json` | `c4c55f010bed7e28d0e87c72a8702cabd4f0807a7023309f4c62c238829dfbd5` |
| `sorties-v4/table-v4.json` | `145c0dbcaeff5c5657ce7680a8375f1413686e382b8f754603fb66e5bcfb0604` |
| `sorties-v4/devis-v4.json` | `1fdfaa5118d9053b6b8f0f95772f589b9f025f674517c32aea1ec335b37ecc96` |
| `sorties-v4/journal-sorties-v4.txt` | `8d284f0b6dbcfcbbb00385ab6d8ecfec08e5f14bceb001b8a99fc9175381498b` |

## 1. Le constat à résoudre (C-1)

Contre-lecture du préenregistrement, point C-1 ; comptes recomptés par programme : `preenregistrement-v1/comptes_c1_c4_v3b_v1.py`
(`54dfbbb2…`), sortie `preenregistrement-v1/comptes_c1_c4_v3b_v1.json` (`0599ae20…`), sur les 12 parties
`sorties-v3/generations-a2-v3b-monde-*.json` (famille MR-1, générateur v2). Sous le modèle de proposeurs synthétiques
(probabilité de proposer une composante inconnue : forte 0,5, moyenne 0,25, latente 0,25, faible 0,1), la génération 1 capte
**toutes** les fortes et les moyennes dans les 12 mondes ; une composante neuve n'apparaît ensuite que dans 4 mondes, toujours
une faible non certifiée ; la génération 3 ne retient rien ; « progrès certifié » dans **0 monde sur 12**.

**Cause, dans la famille et non dans le juge** : dans MR-1, chaque composante se voit **seule**. Un effet principal, un seuil,
une interaction de sous-population : leur signal existe dans la marginale de leur trait, quel que soit ce que l'archive sait
déjà. Rien n'ordonne les découvertes ; une génération de 24 cartes suffit à tout prendre, sauf ce qui est trop petit pour le
juge. Pour qu'une course de trois générations ait **quelque chose à répondre** sur le progrès, il faut des composantes dont la
trouvabilité **dépend** de ce qui est déjà capté. C'est un changement du dessin de la question, pas du signe attendu : la
famille v4 ne dit pas si la boucle progresse ; elle rend la question répondable (R3).

## 2. Famille MR-2 (générateur v4)

Code : `outils-v4/monde_riche_v4.py` (`4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8`), **scellé à
08:02 UTC, avant toute partie** (journal `sorties-v4/journal-sorties-v4.txt`, première ligne) ; il importe les outils v1, v2, v3
scellés, sans les modifier, et ajoute une sorte d'effet par remplacement à l'exécution de trois fonctions de la v1
(`compiler_monde`, `_conditions`, `traits_d_un_effet`).

### 2.1 La composante conditionnelle (sorte neuve `interaction_xor`)

- **Définition** : sur un trait neuf z_t, ajoute **+ p · z_t** aux scores quand **z_B > 0**, **− p · z_t** sinon ; z_B est le trait
  d'une autre composante du monde, sa **composante de condition** (déclarée dans le devis, `composante_condition`).
- **Pourquoi elle ne se trouve pas seule** : z_B est symétrique autour de 0, indépendant de z_t ; en moyenne sur z_B, la pente
  de z_t est **nulle**. Une loi qui ajoute à l'archive un effet de z_t sans condition n'en tire presque rien ; il faut une
  condition sur le signe de z_B. Ce n'est pas une affirmation du modèle de proposeurs : c'est **mesuré sur chaque monde**, sans
  proposeur, par la **part marginale** (§4.3) : la part de l'information I_i qu'une correction sans condition sur z_t
  (logits de W₋ᵢ + β·z_t + γ, ajustés au maximum de vraisemblance attendue sous W) rend.
- **Pourquoi elle devient trouvable après sa condition** : une fois z_B dans une loi de l'archive, un proposeur qui lit les
  résidus **par branche** de z_B (ce que l'archive l'invite à faire) voit une pente nette de z_t dans chaque branche. Que de vrais
  proposeurs le fassent est une **hypothèse** ; la v4 la rend mesurable, ne la suppose pas vraie (§3.3, §7).
- **Taille** : classe **« conditionnelle »**, information visée [0,04 ; 0,08] nat (celle d'une moyenne), même étalonnage par
  bissection que la v2. **Une ou deux** par monde (tirées uniformément).
- **Profondeur** : la première conditionnelle dépend d'une **moyenne à trait** du monde (principal, seuil, interaction ; pas un
  décalage de sous-population, qui n'a pas de trait), tirée uniformément ; **la seconde, s'il y en a deux, dépend de la première**
  (chaîne de profondeur 2). Raison écrite d'avance : une course de **trois** générations a besoin d'une composante qu'on ne
  peut trouver qu'en génération 3 au plus tôt sous le dessin le plus favorable ; sans chaîne, la génération 3 n'aurait rien à
  répondre (le constat C-1 en génération 3 : vide partout).
- **Compilation dans la grammaire existante** : une principale (− p sur z_t) et une interaction de seuil (+ 2p sur z_t si
  z_B > 0) ; le seuil 0 de z_B devient une condition de l'arbre `si_sinon`. Aucune sorte neuve dans la grammaire servie.

### 2.2 Contraintes du gabarit v4 (toutes écrites avant toute partie)

Le gabarit v2 (`tirer_gabarit_v2`, inchangé : 2 fortes dont une principale, 2 ou 3 moyennes, 2 à 4 faibles, latent un monde
sur trois, au moins 2 interactions, au plus 2 effets à seuil) est tiré, puis **rejeté et retiré** tant que l'une de ces
conditions manque :

| contrainte | raison |
|---|---|
| traits portant un effet (conditionnelles comprises) ≤ 6 | au moins 2 leurres sur 8 traits (régularité déclarée de la v3) |
| au moins une moyenne à trait | porter la condition de la première conditionnelle |
| **au plus 10 composantes** (conditionnelles et latente comprises) | au plus 9 « K1 + un effet » : jeu planté de 13 au plus, **devis inchangé** (§5) |
| conditions de seuil distinctes ≤ 3 (le seuil 0 de chaque condition compris) | arbre d'au plus 2³ × 3 sous-populations × 2 (latent) = **48 feuilles** (24 en v3) |

Ces contraintes **déforment les fréquences** des sortes (comme en v3) : déclarées publiques avec le générateur (Q-10 (a)).

### 2.3 Ce que j'ai écarté, et pourquoi

- **Effet masqué par un effet principal** (une composante dont la pente s'annule dans la marginale parce qu'une autre la
  compense) : demande d'accorder deux tailles l'une sur l'autre ; l'étalonnage par bissection ne le tient pas sans réglage fin,
  et le masquage disparaît dès que la taille de l'une bouge. Rejeté pour fragilité.
- **Interaction de seuil plus forte** (la sorte existante, avec un seuil plus haut) : sa marginale n'est pas nulle
  (p · P(z_c > s)) ; elle se trouve seule, plus tard seulement en probabilité. Ne change pas l'ordre des découvertes.
- **Trait non observé de plus** (Q-11 (b)) : Lazar a retenu Q-11 (a) ; et un trait non observé n'est jamais « capté » (4 sur 23
  en v2), donc ne rend pas le progrès répondable.
- **Rendre les moyennes plus petites** (moins de puissance en génération 1) : déplace des moyennes vers « proche du seuil » ;
  elles cessent d'être certifiées ; la règle de garde ne compte que les certifiées. Rejeté.

### 2.4 Vérificateur v4 (v2 étendu)

`verifier_v4` = `verifier_v2` (C0 à C8 inchangés) avec les exigences `EXIGENCES_V4` : classe « conditionnelle » [0,04 ; 0,08],
1 ou 2 par monde ; conditions de seuil ≤ 3 ; feuilles ≤ 48 ; **C8 à m = 48** (règle de m, V-4 ; 44 en v3) ; et une règle
neuve : **toute conditionnelle doit être certifiée** (borne basse de Wilson ≥ 0,8 à 200 graines, contre le nul de {W₋ᵢ}),
sinon refus et retirage (au plus 8). Raison : une conditionnelle non certifiée ne compterait pas dans la règle de garde ;
l'exiger règle la **capacité** du dessin (une composante de plus à trouver et que le juge sait voir), pas le signe. C'est une
sélection de mondes de plus, **déclarée** comme C5 et C6.

## 3. Règle de garde, écrite d'avance

### 3.1 Texte (mot de Lazar R-2492, recopié)

> « Pas de course si moins de la moitié des mondes de calibration gardent une composante certifiée encore trouvable après une
> génération 1 simulée. »

### 3.2 Définitions opératoires (gelées dans le code scellé avant toute partie : `monde_riche_v4.py`, `partie` et `resume`)

- **Mondes de calibration** : au banc, les mondes du **secret de calibration** (au moins 12, conception v3 §1.8 ; Q-3 (c) pour
  le secret de test, même forme). **Ici**, faute de secret engagé, la mesure se fait sur **12 graines de développement**
  publiques (`cle("monde-mr1-v4-calibration-developpement", r)`, r = 0 à 11) : elle est **indicative**, elle ne décide pas ; la
  décision se prend au banc, sur les mondes du secret de calibration, avec ce même code gelé.
- **Monde compté** : monde conforme (C0 à C8 v4, au plus 8 tirages) ; le code compte sur les **mondes conformes**. Je propose
  pour le préenregistrement la forme plus dure : un monde sans tirage conforme en 8 compte comme **ne gardant rien**
  (dénominateur : tous les mondes tirés). Sans effet ici : 12 conformes sur 12.
- **Génération 1 simulée** : le code de la v3b sinon (juge simplifié contre le nul v8 de l'archive, n = 400 tirages, regroupement
  stratifié ε = 0,01 et ε_strat = 0,04, e-BH sur les groupes, représentant v3 à tranche de choix appariée, test de mort), **m =
  48**, 4 proposeurs × 6 cartes, archive de départ {K1} ; **modèle de proposeurs** : celui de la v3b (garder un effet connu 0,9 ;
  proposer une composante inconnue : forte 0,5, moyenne 0,25, latente 0,25, faible 0,1 ; bruit σ = 0,15) plus **une règle
  déclarée** pour la conditionnelle : 0,25 si sa composante de condition est connue (dans une carte retenue), **0,02 sinon**
  (**estimé**, aucune pièce : un proposeur qui n'a pas vu z_B peut encore tomber sur la condition, rarement).
- **Composante certifiée** : étiquette C8 « certifiée détectable quand le reste du monde est connu » (borne basse de Wilson à
  95 % ≥ 0,8, 200 graines, m = 48) ; **la latente est exclue** (elle n'est presque jamais « captée », V-7).
- **Encore trouvable après la génération 1** : certifiée et **non captée** par l'archive au sortir de la génération 1 (attribution
  de l'oracle, Δ_i ≥ max(0,005 ; 0,75 · I_i), comme en v3).
- **Seuil** : « au moins la moitié » = au moins 6 mondes sur 12 (au moins ⌈N/2⌉ sur N au banc). **Ce seuil n'a aucune pièce**
  (note de décision, Q-13) ; il est de Lazar, recopié.
- **Ce qui suit un échec** : **pas de course** ; aucune nouvelle famille, aucun nouveau tirage de mondes de calibration et aucun
  réglage du modèle de proposeurs sur ces mêmes mondes ; une famille revue passe par un texte neuf et le mot de Lazar. Un
  succès ne prouve rien sur le progrès : il dit que la course **peut** y répondre.

### 3.3 Ce que la règle mesure, et sa faiblesse dite d'avance

La règle mesure la **capacité** du dessin sous un modèle de proposeurs, **pas** sous les vrais. Son issue dépend surtout de la
probabilité « 0,02 » de la conditionnelle cachée, qui est **estimée** ; je rapporte donc aussi, sur les mêmes mondes, la
variante **« sans masquage »** (0,25 toujours : les proposeurs trouveraient la conditionnelle sans voir sa condition). Si la
règle ne tient qu'avec masquage, c'est que la v4 dépend de l'hypothèse « les proposeurs lisent par branche ce que l'archive
leur montre » ; le pilote de Q-13 (e) (une génération des vrais proposeurs sur 2 mondes de calibration) est la seule pièce qui
la mesurerait. La **part marginale** (§4.3) est la partie de l'argument qui ne dépend d'aucun modèle de proposeurs.

## 4. Simulations sur la famille v4

Script `outils-v4/monde_riche_v4.py` (`4b165847…`, scellé avant toute partie ; chaque sortie porte cette empreinte dans son
champ `script_sha256`, vérifié) ; lanceur `outils-v4/lancer_sorties_v4.sh` (`e2f6e0ea…`) ; **une partie par monde, scellée**,
un seul processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2` ; journal `sorties-v4/journal-sorties-v4.txt`
(`8d284f0b…`) : 08:02:15 → 09:17:45 UTC, 12 parties code 0, résumé code 0. Résumé `sorties-v4/resume-v4.json`
(`c4c55f010bed7e28d0e87c72a8702cabd4f0807a7023309f4c62c238829dfbd5`) ; table par monde `sorties-v4/table-v4.json`
(`145c0dbcaeff5c5657ce7680a8375f1413686e382b8f754603fb66e5bcfb0604`, par `outils-v4/table_v4.py`, `1b48486a…`). Chaque partie :
générer et vérifier le monde (C0 à C8 v4, 200 graines), mesurer la part marginale, courir **3 générations avec masquage** et
**1 génération sans masquage** (même monde, autre flux aléatoire). Aucun réglage de la famille, du modèle de proposeurs ou de
la règle après lecture : les chiffres ci-dessous sont ceux du premier et seul passage.

### 4.1 Générateur et vérificateur

- **12 mondes conformes sur 12** ; **12 tirages refusés** avant eux (C6 : 8 ; C0 : 3 ; C3 : 1), contre 5 refus pour 8 mondes au
  banc v2 (`sorties-v2/banc-generateur-v2-resume.json`). C6 (attribution d'une « K1 + un effet » en écart) refuse plus souvent :
  **cause non établie** (je soupçonne l'attribution des « K1 + conditionnelle » sans leur condition ; à lire au banc) ; C0 :
  motif non relu dans les parties (dans l'essai à blanc du bac à sable, un décalage au-delà de la borne 4 après étalonnage). Au plus 3 refus pour un monde (mondes 4 et 11), sous la borne de 8.
- **Conditionnelles** : 14 sur 12 mondes (deux chaînes, mondes 1 et 10) ; **toutes certifiées** (exigé ; puissance C8 de 0,955
  à 1,0). Composante de condition : moyenne certifiée dans 11 mondes, moyenne « proche du seuil » dans le monde 0 (E4,
  puissance 0,545).

### 4.2 Règle de garde (mesure indicative, graines de développement)

| | mondes gardant une composante certifiée non captée après la génération 1 | règle (au moins la moitié) |
|---|---|---|
| **avec masquage** (modèle déclaré, §3.2) | **8 sur 12** (Wilson 95 % : [0,39 ; 0,86]) | **tenue** |
| **sans masquage** (conditionnelle proposée à 0,25 toujours) | **0 sur 12** | **non tenue** |

Ce qui reste après la génération 1 avec masquage (par classe, sur les 12 mondes) : **8 conditionnelles**, 2 moyennes, 0 forte,
0 faible. Le monde 0 ne garde qu'une moyenne ordinaire (E3, décalage de sous-population, non captée en génération 1 par le hasard du flux, captée en génération 2) :
sans elle, **7 sur 12** mondes gardent une **conditionnelle**. La borne basse de Wilson (0,39) est **sous la moitié** : à 12
mondes, la règle ne se distingue pas de son seuil avec confiance ; au banc, le même risque.

**Lecture** : la règle tient **seulement** sous l'hypothèse de masquage. Sans elle, la famille v4 se vide en génération 1
comme MR-1 (0 sur 12). La v4 ne crée donc pas, à elle seule, de quoi trouver après la génération 1 : elle crée des
composantes **dont la trouvabilité peut dépendre de l'archive**, et la règle mesure ce qui arrive **si** les proposeurs se
comportent ainsi. Que de vrais proposeurs « voient » une conditionnelle sans sa condition est la question que seul le pilote
(Q-13 (e)) mesurerait (§7).

Même avec masquage, la première conditionnelle est captée **dès la génération 1 dans 6 mondes sur 12** (0, 1, 5, 6, 8, 9) :
24 cartes à 0,02 donnent 1 − 0,98²⁴ ≈ 0,38 de chances qu'une carte au moins la porte (**estimé**, calcul) ; 6 sur 12 est au-dessus,
sans écart significatif à 12 mondes. La chaîne (profondeur 2) est ce qui a gardé le monde 1.

### 4.3 Part marginale (mesure structurelle, sans modèle de proposeurs)

Part de l'information I_i qu'une correction **sans condition** sur le trait rend (`part_marginale`, oracle de 12 000
instances) :

| classe | composantes | minimum | médiane | maximum |
|---|---|---|---|---|
| **conditionnelle** | 14 | 0,0085 | **0,0195** | 0,0821 |
| moyenne à trait (principal, seuil, interactions) | 18 | 0,23 | 0,47 | 1,0 |

Une conditionnelle ne laisse **presque rien** (2 % de son information en médiane, 8 % au plus) à qui ne conditionne pas sur
le signe de sa condition ; une moyenne ordinaire en laisse 23 % à 100 %. C'est le seul fait de la v4 qui ne dépend d'aucun
modèle de proposeurs : la composante est **invisible marginalement**, visible par branche. Il ne dit pas qu'un vrai proposeur
ne testera pas des conditions au hasard.

### 4.4 Course de trois générations (avec masquage)

| | génération 1 | génération 2 | génération 3 |
|---|---|---|---|
| retenues, moyenne par monde (v4) | 7,83 | 8,58 | 0,58 |
| retenues, moyenne par monde (v3b, MR-1, pour mémoire) | 9,0 | 6,08 | 0 |
| représentants promus, moyenne par monde (v4) | 7,92 | 8,58 | 0,58 |

- **Progrès certifié** (une composante certifiée captée en génération 2 ou 3, absente à la fin de la génération 1) : **8 mondes
  sur 12** (MR-1 v3b : 0 sur 12). En génération 3 : **1 monde** (monde 10, la seconde conditionnelle de la chaîne) ; la génération 3
  retient quelque chose dans 3 mondes seulement (1, 2, 10).
- **Fausses découvertes** (retenues sans gain au-delà de l'enveloppe ≥ 0,02 selon l'oracle) : **36 sur 204** retenues (17,6 %),
  contre 28 sur 181 en v3b (15,5 %) ; tolérance de Q-9 (a), à mesurer au banc.
- Sous le modèle, la génération 3 reste presque vide : elle n'a à répondre que dans les mondes à chaîne (2 sur 12) ou en
  retard (monde 10). Une course de 2 × 3 a donc peu de chances de dire quoi que ce soit sur la génération 3 ; la question
  « progrès » se joue en génération 2.

## 5. Devis revu (sous les plafonds inscrits)

Script `outils-v4/devis_multi_generations_v4.py` (`f166fa4abed34b87dce9e58a8d7c786764d4f0866b8119cae010de88fcb356f9`), qui
importe la formule v2 (`outils-v2/devis_multi_generations_v2.py`, `710954c7…`, inchangée) ; sortie `sorties-v4/devis-v4.json`
(`1fdfaa5118d9053b6b8f0f95772f589b9f025f674517c32aea1ec335b37ecc96`). Tout est **estimé** sauf les prix cités dans la v3.

- **Pire cas inchangé** : la v4 garde au plus 10 composantes, donc au plus 9 « K1 + un effet » et **T_pire = 37** tests par
  monde et par génération (24 représentants au plus, 13 plantées) ; 2 mondes × 3 générations, Q-12 (i) (a) : **Claude 363,00 USD**
  (GO-2026-11-13-01 : **365**, marge 2,00) ; **Argon 34,20 + Astra 12,00 + machine 10 = 56,20** (GO-2026-11-13-02 : **57**,
  marge 0,80) ; modèles 409,20. **Les deux lignes tiennent.**
- **Central refait** avec les représentants promus simulés (7,92 ; 8,58 ; 0,58 par génération, au lieu de 6) : modèles
  **41,11 USD** (Claude 27,96 ; Argon 7,15 ; Astra 6,00), machine 0,90 ; v3 : 41,48. La génération 3 presque vide compense la
  génération 2 plus chargée.
- **Ce que la v4 pourrait changer sans que la formule le voie** : des lois plus profondes (48 feuilles) allongent les réponses des
  proposeurs et les tests de l'expérimentateur ; les plafonds de session et la borne par test (1,50 USD) les tiennent, au prix de
  plus de tests « non concluants » (rapportés ; arrêt Q-12 (ii) au tiers). **Marges minces** (2,00 et 0,80 USD) : aucune
  composante de plus, aucun proposeur de plus, aucun test de plus par génération sans texte neuf et mot de Lazar.
- Banc de calibration et génération des mondes : **calcul seul** (≈ 4 à 8 minutes de processeur par monde vérifié et simulé,
  journal v4), aucune ligne de GO.


## 6. Ce qui change pour le préenregistrement (brouillon 3, `2dda3b74…` ; pour le rédacteur du texte neuf)

Décisions de Lazar (R-2492) à porter comme **figées** : Q-1 (b) 2 mondes × 3 générations ; Q-3 (c) secret machine engagé et
poussé, puis la phrase de Lazar ; Q-9 (a) vraie découverte = gain au-delà du seuil contre l'archive **et** contre ses mélanges,
tolérance mesurée au banc ; Q-10 (a) générateur publié avec le code, mondes et secret privés jusqu'au verdict, mondes publiés
seulement sur son mot ; Q-11 (a) traits observés à effet caché, leurres, latent un monde sur trois ; Q-12 (i) (a) fausses non
testées, vraies testées à chaque génération ; Q-12 (ii) **un tiers** (arrêt au-delà de 12 tests coupés sur 37 en génération 1) ;
Q-13 (c) famille revue (cette conception) avec la règle de garde.

| section du brouillon 3 | changement |
|---|---|
| §0, §3.1 (famille, générateur, vérificateur) | famille **MR-2** (§2 ici) : classe « conditionnelle » (1 ou 2, [0,04 ; 0,08], condition sur une moyenne, seconde chaînée sur la première) ; au plus 10 composantes ; conditions de seuil ≤ 3 ; **au plus 48 feuilles** (24) ; générateur `generer_monde_v4`, vérificateur `verifier_v4` (C8 à m = 48, toute conditionnelle certifiée) ; régularités neuves déclarées publiques : « une ou deux composantes conditionnelles, sur le signe d'un trait d'une moyenne ou de la conditionnelle précédente » ; fréquences déformées par les rejets, mesurées au banc et déclarées |
| §3.4 (jeu planté) | inchangé dans sa règle ; « K1 + un effet » d'une conditionnelle **sans** sa condition : vraie au sens de l'oracle si au-dessus de g₀ (C5, C6 la vérifient) ; au plus 9 « K1 + un effet » tenu par la borne de 10 composantes |
| §3.6 (grammaire servie) | le gabarit servi aux proposeurs dit l'existence possible d'une condition sur le **signe** d'un trait (régularité publique, Q-10 (a)) ; profondeur d'arbre permise à 3 conditions |
| §4.1 (prédictions indicatives) | chiffres de la v3b remplacés par ceux de la v4 (§4 ici), marqués « [BANC] » à refaire sur les mondes de calibration |
| §6 (seuils), §10 (liste d'arrêt), §16.1 (préalables) | **règle de garde** (§3 ici) ajoutée à la liste d'arrêt **avant tout appel payant**, mesurée au banc sur les mondes du secret de calibration avec le code gelé ; arrêt Q-12 (ii) au tiers ; dénominateur de la règle écrit (§3.2) |
| §7 (plan d'analyse), §8 (lecture) | « progrès certifié » se lit par monde : une composante certifiée **captée en génération 2 ou 3** et absente à la fin de la génération 1 ; rapporter à part les conditionnelles captées **avant** leur condition (trouvées « sans la voir ») et **après** |
| §8.4 (relevé brut) | ajouter la part marginale de chaque conditionnelle (mesure du monde, avant la course, sans tirage d'issue) |
| §14 (décisions) | Q-1, Q-3, Q-9 à Q-13 portées comme tranchées (mot R-2492) ; Q-13 (e) (pilote) reste possible comme ligne distincte si la règle ne tient qu'avec masquage (§7 ici) |
| §17 (devis) | §5 ici : pire inchangé (409,20 modèles ; 365 sur crédits, 56,20 hors crédits avec la machine sous 57) ; central refait |
| §20 (blocs gelés lus par le lanceur) | `EXIGENCES_V4`, les contraintes du gabarit v4, la règle de garde et le modèle de proposeurs de la mesure (probabilités, dont 0,02 et 0,25) gelés comme blocs |

## 7. Questions et réserves pour Lazar (nouvelles ; le reste de la v3 §7 est tranché par R-2492)

**Q-14 — Que faire d'une règle qui ne tient que sous l'hypothèse de masquage.** Enjeu : la règle de garde tient à 8 sur 12 avec
masquage, 0 sur 12 sans ; tout le gain de la v4 sur le progrès vient de l'hypothèse « un proposeur trouve rarement une
conditionnelle sans avoir vu sa condition » (0,02 contre 0,25, **estimé**). (a) **Course sur la v4 si la règle tient au banc**
(modèle gelé tel quel) : aucun délai de plus ; le progrès devient répondable **si** l'hypothèse est vraie, et la course la teste
en passant (conditionnelles captées avant ou après leur condition, rapportées) ; si elle est fausse, la course retombe sur la
réponse de la v3 (garde et boucle). (b) **Pilote Q-13 (e) avant la course** (une génération des vrais proposeurs sur 2 mondes de
calibration v4, au pire 9 USD par monde, ligne de GO distincte) : mesure directement si les vrais proposeurs trouvent les
conditionnelles en génération 1 ; un texte et une ligne de plus, quelques jours. (c) **Règle exigée sous les deux modèles** :
elle échouerait (0 sur 12) : pas de course. Recommandation : **(a)**, confiance 0,5 ; (b) à 0,4 si l'échéance du 30 novembre le
permet. Défaut sous 48 heures : (a).

**Q-15 — Seuil de la règle à 12 mondes.** 8 sur 12 a une borne basse de Wilson de 0,39 : au banc, le résultat peut tomber de
part et d'autre de 6 sur 12 par le seul hasard des mondes. (a) Garder « au moins la moitié » sur 12 mondes (le mot de Lazar) ;
(b) 24 mondes de calibration (≈ 1 h 15 de processeur de plus, aucun coût) : le seuil se lit mieux. Recommandation : **(b)**,
confiance 0,55 ; défaut : (b) (calcul seul, routine).

**Réserves.**
- Le modèle de proposeurs synthétiques reste **arbitraire** (v3) ; la v4 y ajoute une probabilité de plus (0,02), sans pièce.
- La mesure de la règle est faite sur des **graines de développement publiques** : elle ne décide rien ; la décision se prend au
  banc, sur les mondes du secret de calibration.
- La famille v4 **sélectionne** des mondes de plus (conditionnelles certifiées exigées ; plus de refus C6) : les mondes de la
  course sont ceux où le juge voit les conditionnelles quand le reste est connu ; dit, comme C5 et C6.
- **Ordre** : famille, modèle de proposeurs, règle et code **scellés à 08:02 UTC avant toute partie** ; les §2, §3 et §6 ont
  été rédigés pendant les calculs, après avoir vu les sorties des mondes 0 et 1 (contrôle de bon fonctionnement) ; la
  définition du dénominateur (§3.2) a été corrigée ensuite pour dire ce que fait le code. Rien n'a été réglé après lecture.
- Lignée : conception, code et mesure par le même modèle (Claude Opus 5.5) ; la contre-lecture exigée par GO-2026-11-13-01
  doit venir d'un lecteur neuf, de préférence d'une autre lignée (Fable).
