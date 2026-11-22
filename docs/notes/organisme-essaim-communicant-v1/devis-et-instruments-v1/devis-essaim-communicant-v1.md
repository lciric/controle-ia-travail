# Devis — expérience « essaim qui communique » (organisme d'idéation) — v1

- Pièce de préparation, **aucune dépense, aucun appel de modèle, aucun appel réseau**. Écrite le 22 novembre 2026 (sous-agent, modèle Claude Opus 5.5), à partir de la conception rendue par Claude Fable 5.2 (`docs/notes/organisme-essaim-communicant-v1/reponse-fable-demande-7-v1/relecture-fable-api.md`, `dd60dd678b215326d16cd46e1fb180a522d3f82ec8ba15e9519edd9d42277a0c`), sections C.1, C.5, C.7, D et F.
- Calcul rejouable : `calcul_devis_essaim_v1.py` (ce dossier) → `calcul-devis-essaim-v1.json` (empreintes dans les compagnons `.sha256`). Le script lit chaque tarif dans sa pièce, à l'empreinte, et refuse si une empreinte diffère. Extraction par ligne : `extraire_lignes_devis_v1.py`.
- **Verdict d'abord.** Au cas attendu, sur l'espèce la moins chère dont le prix est établi (Kimi), l'estimation vaut **2 366 USD** ; sur la première espèce Claude, **3 869 USD** ; sur l'espèce la plus chère (seconde espèce Claude, ou Astra, même prix), **8 380 USD**. Le pire du cas attendu va de 20 949 à 91 943 USD, et le pire du cas haut atteint **159 588 USD**. **Les tests de mort et les objets de contrôle pèsent de 70 à 80 % de l'estimation au cas attendu**, alors que la section D de la conception ne les chiffre pas. Le périmètre que la section D chiffre (proposeurs, messages, aiguilleur) vaut à lui seul de 469 à 2 343 USD au cas attendu.

## 1. Tarifs (USD par million de jetons, entrée / sortie)

| espèce | tarif | pièce lue (empreinte vérifiée sur disque) | statut |
|---|---|---|---|
| première espèce Claude | 4 / 20 | `docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v2.json`, champ `prix.prop-claude-1` (`91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b`) ; même barème dans `docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md`, § 1 (`521470096f98861d0a4183b24b1ab313af9fb365ee398da4b82afbfbbbfb3f30`) | tarif repris par citation : la pièce primaire, le barème de `/home/user/ideation-organism/orchestrator/pole/relais_reel_v2.py` (`98c3e79e…`), est **absente du disque** (vérifié) |
| seconde espèce Claude | 10 / 50 | mêmes pièces, `prix.prop-claude-2` | idem |
| Fable 5.2 | 8 / 40 | `src/controle_ia/relecture_fable_api_v3.py`, lignes 99-100 (`95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62`) | tarif écrit dans le code d'après la compétence de Claude Code ; c'est le tarif facturé par la relecture qui a produit la conception (1,130496 USD) |
| Argon | 8,3 / 41,5 | `rapports/fille-ideation-1-v1/appel-argon-v5.sh`, ligne 29 (`37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a`) ; égal au calcul v2 (contrôle croisé fait par le script) | sortie « SUPPOSÉ » selon le devis d'affinage v5, § 1 |
| Kimi | 2 / 10 | calcul v2, `prix.prop-kimi` | repris par citation (« procédure des relais § 2.2, vérifiés le 30 octobre ») ; pièce primaire non relue |
| Astra | 10 / 50 | calcul v2, `prix.prop-astra` | repris par citation ; la pièce primaire `docs/notes/organisme-conception-propre-v1/prix-astra-v2.md` (`bf211a07…`) est **absente du disque** (vérifié par `sha256sum`) |
| Carbon | 8,3 / 41,5 | calcul v2, `prix.prop-carbon` | **borne haute** donnée par la mère (R-3271), remise du lot non comptée |

Le rapport sortie / entrée vaut exactement **5** pour les sept espèces : le ρ = 5 de la section C.1 est cohérent avec toutes les pièces de tarifs.

## 2. Unités (section D), recontrôlées par programme

Les totaux de la conception sont recalculés à partir de ses lignes, **sans aucun écart** : 92, 200 et 336 courses de bras ; 2 300, 5 000 et 8 400 appels de proposeur (25 par course de bras) ; 4 600, 10 000 et 16 800 appels d'aiguilleur (un par carte, deux cartes par appel) ; 384, 864 et 1 440 appels de message (12 par course de bras du bras (a), plus la moitié des bras d'instrument) ; 9,2 / 6,9, 45 / 30 et 168 / 134,4 millions de jetons de proposeur (entrée / sortie).

Postes ajoutés à la section D, parce qu'ils sont payés (C.1 : « tout compte ») :
- **Tests de mort des cartes**, sous la forme du noyau à monde planté (`docs/notes/organisme-multi-generations-v1/outils-v2/devis_multi_generations_v2.py`, compagnon vérifié, formule importée telle quelle par le devis v4) : un test vaut des tours d'expérimentateur (estimation : 2 tours de 8 000 / 2 000 jetons ; pire : 12 tours de 8 000 / 4 000, arrondis au dixième au-dessus) plus un vérificateur (0,06 USD ; pire 0,10). Cartes testées : estimation, 23,7 % des cartes (taux de promus de la simulation v4, `sorties-v4/devis-v4.json`, `1fdfaa51…` : 7,92 + 8,58 + 0,58 sur 72 cartes, **proposeurs synthétiques**) ; pire, toutes les cartes.
- **Tests de mort des objets de contrôle** : C.7 sert le même jeu « dans chaque bras et dans chaque lignée de (b) », soit 6 jeux pour les 3 courses de bras d'un monde (2 par course) ; plantées testées par génération : 10 à l'estimation, 13 au pire (même formule v2). Hors du budget égalisé (C.1), mais payés.
- **Juge statistique** : aucun appel (hypothèse vérifiée, § 4).

## 3. Devis en dollars

Estimation = jetons du régime, tests à l'estimation ; pire = jetons du régime, tests au pire (toutes les cartes testées, 12 tours). Chiffres de `calcul-devis-essaim-v1.json`, clé `resume_usd`.

### 3.1 Totaux par espèce (USD)

| espèce | bas : estimation | bas : pire | attendu : estimation | dont section D seule | dont tests | attendu : pire | haut : estimation | haut : pire |
|---|---|---|---|---|---|---|---|---|
| Kimi | 996 | 9 544 | **2 366** | 469 | 1 897 | 20 949 | 4 999 | 36 218 |
| première espèce Claude | 1 596 | 17 911 | **3 869** | 937 | 2 932 | 39 337 | 8 550 | 68 136 |
| Fable 5.2 | 2 794 | 33 467 | **6 876** | 1 875 | 5 002 | 73 555 | 15 651 | 127 670 |
| Argon | 2 884 | 34 663 | **7 102** | 1 945 | 5 157 | 76 185 | 16 183 | 132 243 |
| Carbon (borne haute) | 2 884 | 34 663 | 7 102 | 1 945 | 5 157 | 76 185 | 16 183 | 132 243 |
| seconde espèce Claude | 3 394 | 41 833 | **8 380** | 2 343 | 6 036 | 91 943 | 19 201 | **159 588** |
| Astra | 3 394 | 41 833 | 8 380 | 2 343 | 6 036 | 91 943 | 19 201 | **159 588** |

**Pire toutes espèces** : seconde espèce Claude et Astra (même tarif, 10 / 50) ; 41 833 (bas), 91 943 (attendu), 159 588 USD (haut). **Borne dure par plafonds de session** (proposeur 3,00 USD, aiguilleur 0,25 USD par appel, devis d'auto-conception v1, § 4 et calcul v1, `PLAFONDS_SESSION`) : 8 050, 17 500 et 29 400 USD pour ces deux rôles seulement ; **aucun plafond de session n'est établi pour les messages et les tests de mort** dans ce dessin, qui restent donc non bornés par une garde. Un plafond d'arrêt de course est à fixer au préenregistrement.

### 3.2 Par ligne de la section D, cas attendu, estimation (USD ; entre parenthèses, la section D seule)

| espèce | pilote A/A | confirmatoire | bras d'instrument | familles inédites |
|---|---|---|---|---|
| Kimi | 426 (84) | 1 135 (225) | 379 (76) | 426 (84) |
| première espèce Claude | 696 (168) | 1 857 (449) | 620 (151) | 696 (168) |
| Fable 5.2 | 1 237 (337) | 3 299 (899) | 1 102 (302) | 1 237 (337) |
| seconde espèce Claude, Astra | 1 508 (421) | 4 021 (1 123) | 1 343 (378) | 1 508 (421) |

Au pire du cas attendu (première espèce Claude) : pilote 7 080, bras d'instrument 6 295 USD. Les **instruments payants** nommés par la conception sont le pilote (bruit, test A/A) et les bras d'instrument (placebo, scores visibles, archive commune seule, (b0), vote à k) : 1 316 USD à l'estimation sur la première espèce Claude au cas attendu (805 sur Kimi, 2 851 sur la seconde espèce Claude), dont 319 pour la section D seule.

### 3.3 Détail d'une ligne (confirmatoire, cas attendu, première espèce Claude)

| poste | appels ou tests | jetons d'entrée / de sortie | USD (estimation) | USD (pire) |
|---|---|---|---|---|
| proposeurs | 2 400 appels | 21,6 M / 14,4 M | 374,40 | 374,40 |
| messages | 384 appels | 1,152 M / 0,154 M | 7,68 | 7,68 |
| aiguilleur | 4 800 appels | 9,6 M / 1,44 M | 67,20 | 67,20 |
| juge statistique | 0 | — | 0 | 0 |
| tests de mort des cartes | 1 139 tests (3 appels chacun) ; pire 4 800 (13 appels) | 8 000 / 2 000 par tour ; pire 8 000 / 4 000 | 232,29 | 7 200,00 |
| tests de mort des objets de contrôle | 5 760 tests ; pire 7 488 | idem | 1 175,04 | 11 232,00 |
| **total** | | | **1 856,61** | **18 881,28** |

## 4. Hypothèses de la conception « à vérifier dans le noyau »

| hypothèse (section D) | issue | pièce |
|---|---|---|
| Message : 3 000 jetons d'entrée, 400 de sortie | **non vérifiable** : aucun rôle « message » n'existe dans les pièces du noyau lues (la dépense par rôle de la course v67 ne porte que `proposeur` et `tests_de_mort`, analyse § 1, S1 ; la formule du devis multi-générations v2 n'a aucun tel poste) | `docs/notes/organisme-re-search-v1/analyse-journaux-re-search-v1.md` (`8a82b5ee1eb709ac752212a40fc181b7a7c236c4b5c5dfa0315825bfb3ae08bc`), § 1 ; `outils-v2/devis_multi_generations_v2.py` (compagnon vérifié) |
| Aiguilleur : 2 000 d'entrée, 300 de sortie | **réfutée pour la taille** par la seule pièce qui chiffre ce rôle (6 250 / 300 à l'estimation, 23 000 / 2 000 au haut, quatre caractères par jeton ; chiffres eux-mêmes déclarés « non mesurés ») ; **existence du rôle non attestée** dans la course à monde planté (aucun aiguilleur dans la dépense par rôle de v67 ni dans le devis multi-générations). Avec 6 250 / 300, l'aiguilleur coûte 0,031 USD par appel sur la première espèce Claude au lieu de 0,014 (+170 USD au cas attendu) | `devis-course-affinage-mentors-v5.md`, § 2 (`52147009…`) ; analyse v67, § 1 |
| Juge statistique : aucun appel de modèle | **vérifiée, indirectement** : la dépense par rôle de v67 n'a aucun poste de juge (proposeurs et tests de mort seuls), la dépense de la génération 2 est exactement celle des proposeurs (0,16409 + 0,400484 = 0,564574 USD), et le juge du noyau est un pari apparié calculé (modèle simplifié dans `monde_riche_outils_v1.juger`). Le journal primaire de v67 est absent du disque : vérification sur les chiffres que l'analyse en rapporte | analyse v67, § 1 et § 2 (M1) ; `outils-v1/monde_riche_outils_v1.py` (compagnon vérifié), lignes 392-435 |
| Test de mort : un appel par carte promue, au plus 52 par course de bras | **réfutée** : dans le noyau à monde planté, un test est un expérimentateur en plusieurs tours (2 à l'estimation, 12 au pire) plus un vérificateur d'une autre famille ; et les objets de contrôle plantés sont testés à chaque génération (10 à l'estimation, 13 au pire). La course v67 le confirme : 16 appels d'Argon dont 14 de vérificateur ; tests de génération 1 : 1,429736 − 0,539846 = 0,88989 USD ; génération 2, sans promue : 0 USD (la partie « par carte promue » tient) | `outils-v2/devis_multi_generations_v2.py`, lignes 4-11, 20-23 ; `outils-v1/devis_multi_generations_v1.py`, ligne 43 (cite le verdict v67 § 4.5, `d7902432…`, non relu) ; analyse v67, § 2 (M1) |

Autres contrôles :
- **Sortie du proposeur** (6 000 jetons à l'estimation, 16 000 au haut, deux cartes par appel) : la course v67 a mesuré 31 891 et 38 343 jetons de sortie pour les deux appels de Kimi, de 5 et 6 cartes, soit environ 6 400 par carte, environ **12 800 pour deux cartes** : au-dessus de l'estimation, sous le haut. Pour Argon, 0,20637 USD pour 6 cartes donne au plus 4 973 jetons de sortie, soit au plus environ 830 par carte. L'écart entre espèces est d'un facteur huit environ. Pièce : `outils-v1/devis_multi_generations_v1.py`, lignes 28-30 (cite le verdict v67 § 4.1, `d7902432…`, non relu ici) ; analyse v67, § 2 (M1).
- **[HYPOTHÈSE] de C.1** (« la communication pèse environ un dixième du coût des proposeurs, soit deux appels de plus pour (b) sur vingt-quatre ») : **réfutée par le calcul** aux tailles de la conception elle-même. Au cas attendu, ρ = 5 : messages 12 × (3 000 + 5 × 400) = 60 000 équivalents ; proposeurs de (a) 24 × (9 000 + 5 × 6 000) = 936 000 ; part **6,4 %** ; converti en appels de proposeur, chaîne aval comprise et arrondi à l'inférieur : **un appel de plus**, et un reliquat de 14 000 équivalents. Le tableau de la section D, qui donne 26 appels à (b), ne suit pas la règle de C.1 ; à corriger avant le préenregistrement (le tableau de coût n'en bouge presque pas).

## 5. Réserves

1. **Les tests de mort dominent** : leur forme (tours, vérificateur) et leur nombre (objets de contrôle par lignée de (b)) ne sont fixés par aucune pièce de la conception ; je les ai pris au noyau à monde planté. Leviers : un jeu d'objets de contrôle par bras (et non par lignée de (b)) divise ce poste par deux ; un seul jeu par monde, partagé entre les trois bras, par six (mais l'invalidation de C.7 se lit alors par monde, non par bras) ; un expérimentateur sur Kimi réduit le coût d'un test d'un tiers environ (0,132 au lieu de 0,204 USD à l'estimation). C'est une décision à porter devant le directeur avant le préenregistrement.
2. Le taux de promus (23,7 %) vient de proposeurs **synthétiques** ; sur de vrais modèles, il n'est pas mesuré.
3. Quatre tarifs sur sept ne sont repris que **par citation** (première et seconde espèces Claude, Kimi, Astra), et les pièces primaires de deux d'entre eux sont absentes du disque ; Carbon n'a qu'une borne haute. Aucun tarif n'est inventé.
4. La machine (temps de processeur du noyau) n'est pas comptée ; le devis multi-générations l'estime à 0,15 USD par monde et par génération.
5. Messages et tests de mort n'ont **aucun plafond de session** établi : le pire n'est borné que par le plafond d'arrêt de la course, à fixer.
6. L'espèce unique n'étant pas choisie (décision 6), le même modèle est supposé tenir tous les rôles payants, aiguilleur et expérimentateur compris ; le vérificateur reste au prix fixe d'Argon.
