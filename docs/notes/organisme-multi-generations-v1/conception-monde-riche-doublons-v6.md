# Conception — monde riche écrit par un programme et regroupement des doublons au sein d'une génération — v6 (famille MR-2, corrections des contre-lectures v4 et v5, règle de garde opératoire)

- **Statut** : conception **v6** (aucun préenregistrement, aucun GO consommé, aucune dépense). Elle est la v5
  (`conception-monde-riche-doublons-v5.md`, `a12ab1e50190b8d27ce6daa0e5c44b81f04c674a916103f518d093400b7481d9`, versée inchangée,
  R12) avec les seules corrections exigées par sa contre-lecture, tour 1 (M-1, m-1 à m-5 ; section « Contre-lecture », en
  fin de pièce), et l'en-tête mis à jour. La v5 était la v4
  (`conception-monde-riche-doublons-v4.md`, `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc`, versée
  inchangée, R12) avec, **et rien d'autre que des mises en cohérence sans effet sur un chiffre, ajoutées sans ligne propre dans la table : dernier point du §5, cellule « §17 (devis) » du §6, réserves du §7** : (1) les **9 corrections exigées** (E-1 à E-9) par la contre-lecture v4
  (`contre-lecture-conception-v4-v2.md`, `16da94d4519bf72b1b3672d98099ee482db01ea2d8403f15068e04b4c2a54c97`, « portable dans le
  préenregistrement après 9 corrections »), appliquées une à une (table ci-dessous) ; (2) la règle de garde « pas de course si
  moins de la moitié des mondes de calibration gardent une composante certifiée encore trouvable après une génération 1
  simulée » rendue **opératoire** (§3.2 et §3.4 : compte exact, N fixé, dénominateur = **tous les mondes tirés**,
  GO-2026-11-17-05, Q-B3 (a)) ; (3) **ce que le pilote MR-2 v14 apprend à la conception** (§8), lu dans son seul verdict v2
  (`verdict-issue-pilote-mr2-v14-v2.md`, `e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d`, égal à son
  compagnon, branche `verdict/pilote-mr2-v74-v14-v1`, commit `61230010`). Les corrections suggérées S-1 à S-6 ne sont **pas**
  appliquées (hors du périmètre demandé ; S-2 serait un changement de famille, à proposer à Lazar).
- **Décisions de Lazar déjà prises qui ferment des corrections** (lues dans `registres/decisions.md` et `registres/go.md`, registres
  vivants) : **R-2501** (Q-14 (b) : pilote avant la course ; Q-15 (b) : **24 mondes de calibration**) ; **R-2504** (E-3, option (a) :
  le gabarit servi ne dit rien des conditions ni des sortes d'effets ; seule la profondeur permise est ouverte à 3 conditions) ;
  **GO-2026-11-16-08** (issue P-2 du pilote acceptée) ; **GO-2026-11-17-05** (banc sur machine louée ; **un seul banc complet**,
  après la pièce des règles du banc et le code de la course contre-lus, **la règle de garde en dernier**, ordre D-2 ; dénominateur
  = tous les mondes tirés, un monde sans tirage conforme en 8 ne garde rien).
- **Ce qui reste valable de la v4 et de la v3** : tout ce que ce texte ne remplace pas (famille MR-2 et son générateur, §2 ;
  simulations v4 et leurs chiffres, §4 ; devis, §5 ; et, de la v3, regroupement, représentant à tranche de choix appariée,
  diversité, proposeurs, garde du secret, jeu planté, loi connue de départ, vérité des découvertes). **Aucun chiffre de la v4 n'est
  changé** ; les chiffres neufs viennent de trois programmes neufs, scellés avant leur passage (pièces écrites ci-dessous).
- **Rédacteur** : modèle A, sous-agent neuf d'un script d'orchestration de la session mère. Je n'ai écrit ni la v4, ni sa
  contre-lecture, ni le pilote, ni son verdict, ni le code v68 à v71, ni le préenregistrement de la course. Même lignée que le
  concepteur de la v4 : la contre-lecture de cette v5 doit venir d'un lecteur neuf d'une autre lignée.
- **Rédacteur de la v6** : modèle C, sous-agent neuf d'un script d'orchestration ; je n'ai écrit ni la v4, ni la v5, ni
  leurs contre-lectures ; j'ai appliqué les couples de la contre-lecture v5, tour 1, par un programme (section
  « Contre-lecture »), sous l'interpréteur du venv du dépôt ; aucun calcul neuf, aucun chiffre neuf.
- **Interpréteur** : Python 3.13.18 et numpy 2.5.3 du système (le même que la v4, pour rejouer ses tirages à l'identique) ;
  scellement par `.venv/bin/python -m controle_ia.scellement`. Calculs : un processus à la fois, `ulimit -v 6000000`,
  `OMP_NUM_THREADS=2`. Aucun appel de modèle, aucun réseau hors de la lecture du dépôt, aucune machine.
- **Heures** (relevées par `date -u`) : début 2026-11-17 00:28:13 ; calcul de la règle 00:34:15 (heure de la sortie) ; rejeu des refus 00:32:23 → 01:01:24 (un premier lancement, par
  erreur sous l'interpréteur du venv, numpy 2.4.6, a été arrêté par son PID, 25601, à 00:32:18, avant toute sortie, R10) ;
  complément des sortes 01:02:02 → 01:03:15 ; fin de la rédaction 2026-11-17 01:04:25 (v5). **v6** : début 2026-11-17 01:11:23 ; application des couples et scellement
  2026-11-17 01:13:01.

## Pièces lues (chemin, empreinte, vérifiées contre leur compagnon)

| pièce | empreinte |
|---|---|
| `conception-monde-riche-doublons-v4.md` | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` |
| `contre-lecture-conception-v4-v2.md` | `16da94d4519bf72b1b3672d98099ee482db01ea2d8403f15068e04b4c2a54c97` |
| `outils-v4/monde_riche_v4.py` (lu ; importé sans modification) | `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` |
| `outils-v1/verifier_monde_kimi_v1.py`, `outils-v2/verifier_monde_v2.py` (extraits : C0 à C8) | compagnons |
| `sorties-v4/partie-v4-monde-{0…11}.json` (champs `refus`, `gabarit`, `conditions`) et `journal-sorties-v4.txt` | compagnons |
| verdict v2 du pilote MR-2 v14 (sur la branche `verdict/pilote-mr2-v74-v14-v1`, par `git show`) | `e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d` |
| `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon3.md` (§6, §16.1 : ordre D-2, banc) | `2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39` |
| `banc-calibration-mr2-v1/devis-banc-calibration-mr2-v3.md` (§2, §6, §7 : lecture du code par le devis) | `ec5a6e99313dd1a48f4105e756813b3500a1181cc66babbb0af4bfb7c5a62eb2` |
| rapport du développeur du code v68 (branche `prep/pilote-mr2-v1`, tête `a5fdfcdf`, par `git fetch` à refspec et `git show` dans un dossier neuf ; §0 à §2 seulement) | `6635e43a11956eb28d7eb8ee4e0975405bbceea32572609e13b0fa8812d82a51` (égale au compagnon sur la branche) ; il dit `compiler_v4` et `verifier_v4` **portés octet pour octet** sous `orchestrator/mr2_v68/` (C-4) : porté à l'octet, le module y ajoute donc la sorte de la même façon, par remplacement à l'exécution (déduit, code du pilote non relu) ; d'où E-5 |
| `registres/go.md` (GO-2026-11-13-01, -02, GO-2026-11-17-05) ; `registres/decisions.md` (R-2500 à R-2510, R-3001, R-3005, R-3050, R-3051) | registres vivants |

## Pièces écrites (v5 ; toutes scellées, compagnon `.sha256`)

| pièce | empreinte |
|---|---|
| `outils-v5/motifs_refus_v4_v1.py` (E-6 : motifs des refus du générateur v4, scellé avant son passage) | `150a831c397929f98e9a1fc6f88b106322057da1ee8212ac84fc91af266d2b82` |
| `sorties-v5/motifs-refus-v4-v1.json` ; `.stdout` | `a70cbc06883a6c047fc18cc606d65d412338dfff535cc7ee770ed1d126d7bd98` ; `1df6a77a67307ed50b85c0f37178df82a7eb815c1465a3d7770f5bd68ee17381` |
| `outils-v5/sortes_refus_c6_v4_v1.py` (E-6 : sortes des composantes des tirages refusés en C6, scellé avant son passage) | `b77f062be9418c7b041fa1f96234d5b3ae4370001139ce7bf14af4880d10afb8` |
| `sorties-v5/sortes-refus-c6-v4-v1.json` ; `.stdout` | `9542b6cfa511413a1fec7513bc5e83e86f10598cd824f2994ef27566f527f15f` ; `02d8e3cb616ab933a2e3eb43c268b0de9320f2cf4c6320935123173bd21fc3ba` |
| `outils-v5/calcul_regle_v5.py` (§3.4 : compte exact de la règle et table de E-1 refaite par somme binomiale exacte, scellé avant son passage) | `41e5bcf07f9f422b589d9466cab5ffbf2f46259be814e8d3c9bc49da992329eb` |
| `sorties-v5/calcul-regle-v5.json` ; `.stdout` | `10ff446d0c7438642e1fe4a327d6fb35a5308f07ce04b10adcc315ac215958d0` ; `f2419d19aba7df21429e5601c3483e6883dc50b6e857228f6550d66ab88b7054` |
| `differentiel-conception-v4-v5.diff` (différentiel v4 → v5, `diff -u`) | compagnon |

## Changements depuis la v4 (correction → où, ancien → nouveau)

| correction | où | ancien (v4) | nouveau (v5) |
|---|---|---|---|
| **E-1** point de bascule et ce que la règle mesure | §3.3, §3.4 (neuf), §4.2, §0 | « son issue dépend surtout de la probabilité 0,02 » ; aucun point de bascule ; banc présenté comme lieu de la décision | bascule écrite : la part attendue des mondes qui gardent vaut 0,5 vers **p ≈ 0,028 à 0,032** et la règle tient à 24 mondes avec la probabilité 0,5 vers **p ≈ 0,030 à 0,034** (calcul exact du modèle réduit, §3.4 ; la contre-lecture disait ≈ 0,03) ; **le banc ne mesure que les mondes, rien sur les proposeurs** ; le 0,25 « une fois la condition connue » est aussi estimé que l'était le 0,02 ; avec P_CACHÉE = 0 (pilote), la règle tient au banc **presque par construction** (§3.4, §8) |
| **E-2** lettre de Q-13 (c) | §2.1, §2.3, §6 | « Pourquoi elle ne se trouve pas seule » sans réserve | MR-2 **ne satisfait pas la lettre** de Q-13 (c) : la composante est invisible dans la marginale de son trait, pas introuvable ; la dépendance à l'archive est logée **dans le comportement des proposeurs**, ni dans le monde ni dans le juge (C5 et C6 tiennent « K1 + conditionnelle » pour une vraie dès la génération 1) ; dépendance **du côté du juge** non examinée (§2.3) ; à écrire au préenregistrement (§6) |
| **E-3** ce qui est servi aux proposeurs | §6 (ligne « §3.6 »), §0 ligne 10 | le gabarit servi « dit l'existence possible d'une condition sur le signe d'un trait » | **retiré** (R-2504, option (a)) : le gabarit ne dit rien des conditions, des sortes d'effets ni de la famille ; seule la profondeur permise des propositions est ouverte à 3 conditions ; la régularité « une ou deux conditionnelles » est publique **avec le générateur** (Q-10 (a)), jamais dans la consigne |
| **E-4** Q-14 nœud sans défaut | §7 | Q-14 « défaut sous 48 heures : (a) » ; option (c) présentée comme une option | Q-14 était un **nœud** (lecture d'une condition de GO et dépense) : le défaut (a) est **retiré** ; l'option (c) était **factice** (elle échoue par construction : sans masquage, 0 sur 12) ; Q-14 est tranchée par Lazar, **(b)** (R-2501), pilote fait, issue P-2 acceptée (GO-2026-11-16-08) |
| **E-5** essais R5 du vérificateur et du générateur | §2.4, §6 | règle « toute conditionnelle certifiée » jamais éprouvée ; sorte ajoutée par remplacement à l'exécution de trois fonctions scellées | essais R5 **exigés avant le gel**, listés (cas sain et artefact pour chaque refus neuf ; égalité de la compilation avec la grammaire de référence sur une chaîne) ; le code de la course et du banc porte la sorte **sous des noms neufs**, sans remplacement à l'exécution, et prouve son **égalité** avec `monde_riche_v4.py` sur les 12 graines de développement (§2.4) ; non faits ici (code, pas conception) |
| **E-6** cause des refus C6 et C0 | §4.1 | « cause non établie » (C6) ; « motif non relu » (C0) | motifs relus sur les 12 tirages refusés, rejoués à l'identique (§4.1) : **C6 ne vient pas des conditionnelles** (0 « K1 + conditionnelle » en écart) ; les 10 vraies en écart sont des « K1 + effet de sous-population » dont l'attribution capte en plus un décalage de sous-population, presque toujours faible : non-séparabilité de la grammaire de la v3 ; C0 : coefficient au-delà de la borne 4 après étalonnage (3) ; C3 : désaccord de l'oracle (1) ; sélection déclarée |
| **E-7** essai à blanc et force de « scellé avant toute partie » | §2, §4, §4.1, réserves | « essai à blanc du bac à sable » cité sans graine ni sortie ; « scellé avant toute partie » sans dire sur quoi l'antériorité repose | essai à blanc dit **non consigné** (aucune graine, aucune sortie gardée, il ne compte pour rien) ; antériorité dite telle qu'elle est : empreinte du code portée par chaque sortie (solide) ; heure du compagnon et première ligne du journal, écrite à part du lanceur scellé ; un seul commit à 09:20:57 (`2338b372`) : rien ne contredit « premier et seul passage », rien ne le prouve hors la parole du concepteur ; pour le banc : code, modèle de proposeurs et règle **versés et poussés avant** l'engagement du secret de calibration (§3.2) |
| **E-8** définitions de la règle à fermer | §3.2, §3.4 | « au moins 12 » mondes ; dénominateur proposé seulement (le code compte sur les conformes) ; aucun compte restreint ; table de E-1 absente | **N = 24 fixé** (Q-15 (b), R-2501) ; **dénominateur = les 24 mondes tirés** (GO-2026-11-17-05), à coder (le code v4 compte sur les conformes) ; **compte restreint aux conditionnelles** rapporté à côté du compte de la règle ; le banc refait la **variante sans masquage** et la **table de E-1** (passes rapportées, ne décident pas) |
| **E-9** lecture de l'issue P sous MR-2 | §6 (lignes §7, §8), §4.4 | « rapporter à part les conditionnelles captées avant et après leur condition » (facultatif en pratique) ; τ « à mesurer au banc » sans dire qu'il change | écrit d'avance : (i) P sur une conditionnelle **n'établit pas** que l'archive a causé la découverte ; pour chaque conditionnelle captée, rapporter **obligatoirement** si sa condition était dans l'archive servie au début de la génération et la part des cartes qui la portent avant et après ; (ii) la génération 3 n'a de quoi répondre que dans les mondes à chaîne (2 sur 12) : avec deux mondes de test, chance qu'un au moins en porte une ≈ **0,31** ; (iii) τ **refait sur MR-2** (17,6 % en v4 contre 15,5 % en v3b) |
| règle rendue opératoire | §3.2, §3.4 (neuf) | définitions de la v4 (au moins 12 mondes, conformes, P_CACHÉE = 0,02) | compte exact `G`, règle `2·G ≥ N` en entiers, N = 24, tous les mondes tirés ; génération 1 simulée **à la dernière étape du banc complet** (ordre D-2), avec f, fusion, n et forme retenus avant elle ; P_CACHÉE = **0** (p_c ponctuel du pilote) décide ; passes rapportées sans décider à la borne haute 0,042965, sans masquage et aux valeurs de la table de E-1 ; prédictions chiffrées par le modèle réduit (§3.4) |
| ce que le pilote v14 apprend | §8 (neuf), §0 | — | P_CACHÉE := 0, P_VUE := 0,25 supposée ; p_c ne vaut que pour le gabarit servi ; témoin positif 14 sur 14 ; 6 appels sur 14 portent la condition ; lois à condition rares dans les cartes ; troncatures d'un proposeur ; ce qui en découle pour la règle, la course et le préenregistrement |
| identifiant de modèle | en-tête | identifiant du concepteur entre accents graves | retiré (aucun identifiant de modèle dans les fichiers) |

Les changements de la v3 à la v4 restent décrits dans la v4 (table « Changements depuis la v3 »).

## 0. En dix lignes

1. Constat C-1 : sur MR-1, la génération 1 prend toutes les fortes et moyennes ; progrès certifié dans 0 monde sur 12.
2. Cause : chaque composante MR-1 se voit seule, dans la marginale de son trait ; rien n'ordonne les découvertes.
3. MR-2 ajoute 1 ou 2 composantes **conditionnelles** (taille moyenne) **invisibles marginalement** : leur pente change de signe
   avec le signe du trait d'une moyenne (ou de la conditionnelle précédente) ; part marginale médiane 2 %.
4. Elles sont **certifiées** (C8, m = 48) dans tous les mondes gardés ; 12 sur 12 mondes conformes, 12 tirages refusés avant.
5. Règle de garde (mot de Lazar) rendue opératoire (v5, §3.2, §3.4) : G mondes gardants sur **N = 24 mondes tirés** (un monde
   sans tirage conforme en 8 ne garde rien) ; elle tient si **2·G ≥ 24** ; mesurée en v4 sur 12 graines de développement.
6. **Avec masquage** (v4 : conditionnelle à 0,02 tant que sa condition n'est pas connue, 0,25 ensuite ; estimé) : **8 sur 12**
   (Wilson [0,39 ; 0,86]). La règle **bascule vers p ≈ 0,03** (E-1) : la v4 l'avait posée à un facteur 1,5 de sa bascule.
7. **Sans masquage** : **0 sur 12**. Le pilote v14 a mesuré **p_c = 0 sur 14 appels** ([0 ; 0,043]) : au banc, P_CACHÉE = 0
   décide, et la règle y tient **presque par construction** ; le banc ne mesure que les mondes, rien sur les proposeurs (§8).
8. Avec masquage, progrès certifié en génération 2 ou 3 dans 8 mondes sur 12 ; la génération 3 reste presque vide (1 monde).
9. Devis : pire inchangé, 363 sous 365 et 56,20 sous 57 USD ; marges minces ; central ≈ 41 USD.
10. Pour le préenregistrement : famille MR-2, règle en **dernière étape du banc complet** (D-2) et à la liste d'arrêt avant tout
    appel payant ; E-2, E-3 (rien servi sur les conditions), E-9 portées ; Q-14 (b) et Q-15 (b) tranchées par Lazar.

## Pièces de la v4 (inchangées, pour mémoire)

### Lues par la v4

| pièce | empreinte |
|---|---|
| `preenregistrement-v1/note-decisions-lazar-v1.md` | `d2bcf5810be0ac7cec214eb908a873a2a98cb6500ce74478868cc3eb68f2b2ee` |
| `preenregistrement-v1/comptes_c1_c4_v3b_v1.py` et `.json` (C-1) | `54dfbbb2…` ; `0599ae20…` |
| `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon3.md` (§3, §17, en partie) | `2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39` |
| `conception-monde-riche-doublons-v3.md` (la mienne) | `386d48bacd6c487d88846d0991d83bd4ad95122f70500d6fbeb7859cde56659c` |
| `registres/go.md`, lignes de GO-2026-11-13-01 et -02 (lecture seule) | — (registre vivant) |
| outils v1, v2, v3 et v3b (importés, non modifiés) | v3 §« Pièces écrites » |

### Écrites par la v4 (toutes scellées, compagnon `.sha256`)

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

**Force de « scellé avant toute partie » (E-7, v5)** : ce qui est **solide**, c'est que chaque sortie de `sorties-v4/` porte dans
son champ `script_sha256` l'empreinte `4b165847…` (vérifiée par la contre-lecture) : le code qui a tourné est le code scellé.
L'**antériorité** du scellement, elle, repose sur l'heure du compagnon (08:02:15) et sur la première ligne du journal, **que le
lanceur scellé n'écrit pas** (écrite à part) ; tout a été versé en **un seul commit**, à 09:20:57 (`2338b372`). Rien ne contredit
« premier et seul passage » ; rien ne le prouve hors la parole du concepteur. Pour le banc, l'antériorité se prouve autrement :
code, modèle de proposeurs et règle **versés et poussés avant** l'engagement du secret de calibration (§3.2).

**Noms neufs exigés (E-5, v5)** : le remplacement à l'exécution de trois fonctions scellées vaut pour la conception ; il ne vaut
pas pour le code qui décide. Le code de la course et du banc porte la sorte `interaction_xor` sous **des noms neufs** (R12), dans
un module neuf, sans remplacer de fonction d'un module scellé, et prouve son égalité avec `monde_riche_v4.py` (§2.4).

### 2.1 La composante conditionnelle (sorte neuve `interaction_xor`)

- **Définition** : sur un trait neuf z_t, ajoute **+ p · z_t** aux scores quand **z_B > 0**, **− p · z_t** sinon ; z_B est le trait
  d'une autre composante du monde, sa **composante de condition** (déclarée dans le devis, `composante_condition`).
- **Pourquoi elle ne se trouve pas seule** : z_B est symétrique autour de 0, indépendant de z_t ; en moyenne sur z_B, la pente
  de z_t est **nulle**. Une loi qui ajoute à l'archive un effet de z_t sans condition n'en tire presque rien ; il faut une
  condition sur le signe de z_B. Ce n'est pas une affirmation du modèle de proposeurs : c'est **mesuré sur chaque monde**, sans
  proposeur, par la **part marginale** (§4.3) : la part de l'information I_i qu'une correction sans condition sur z_t
  (logits de W₋ᵢ + β·z_t + γ, ajustés au maximum de vraisemblance attendue sous W) rend.
- **Ce que MR-2 ne fait pas (E-2, v5)** : MR-2 **ne satisfait pas la lettre** de Q-13 (c). La note de décision parlait de
  « composantes moyennes que la génération 1 **ne peut pas** capter seule » ; MR-2 rend la composante **invisible dans la
  marginale** de son trait, elle ne la rend pas introuvable : rien n'empêche une carte de la génération 1 de la porter avec la
  bonne condition (en v4, la première conditionnelle est captée dès la génération 1 dans 6 mondes sur 12, même avec masquage,
  §4.2). La dépendance à l'archive est logée **dans le comportement des proposeurs** (lire ou non par branche ce que l'archive
  montre), **ni dans le monde ni dans le juge** : C5 et C6 tiennent « K1 + conditionnelle » pour une vraie découverte dès la
  génération 1, sans que sa condition soit dans l'archive. À écrire tel quel au préenregistrement (§6).
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
- **Non examiné (E-2, v5)** : une dépendance **du côté du juge** — une composante dont le gain au-delà de l'archive n'excède le
  seuil qu'une fois une autre captée, comme les faibles de MR-1 — n'a pas été examinée. Elle mettrait la dépendance dans le monde
  et le juge, non dans les proposeurs ; c'est une autre famille (mot de Lazar requis), pas une correction de MR-2.

### 2.4 Vérificateur v4 (v2 étendu)

`verifier_v4` = `verifier_v2` (C0 à C8 inchangés) avec les exigences `EXIGENCES_V4` : classe « conditionnelle » [0,04 ; 0,08],
1 ou 2 par monde ; conditions de seuil ≤ 3 ; feuilles ≤ 48 ; **C8 à m = 48** (règle de m, V-4 ; 44 en v3) ; et une règle
neuve : **toute conditionnelle doit être certifiée** (borne basse de Wilson ≥ 0,8 à 200 graines, contre le nul de {W₋ᵢ}),
sinon refus et retirage (au plus 8). Raison : une conditionnelle non certifiée ne compterait pas dans la règle de garde ;
l'exiger règle la **capacité** du dessin (une composante de plus à trouver et que le juge sait voir), pas le signe. C'est une
sélection de mondes de plus, **déclarée** comme C5 et C6.

**Essais R5 exigés avant le gel du générateur et du vérificateur (E-5, v5)**. En v4, la règle neuve « toute conditionnelle
certifiée, sinon refus » n'a jamais tiré (0 refus C8 sur 24 tirages) : elle n'est éprouvée sur aucun artefact. Avant tout gel
(et donc avant l'engagement du secret de calibration), le code de la course et du banc passe, chaque essai avec un **cas sain**
qui passe et un **artefact** qui est refusé pour le motif attendu :

| # | règle éprouvée | cas sain | artefact |
|---|---|---|---|
| R5-1 | conditionnelle non certifiée → refus C8 | monde de développement conforme (une conditionnelle certifiée) | même monde, pente de la conditionnelle réduite jusqu'à une puissance C8 sous la borne (Wilson basse < 0,8) : refus C8, motif « (conditionnelle) non certifiée » |
| R5-2 | conditions de seuil distinctes ≤ 3 | monde à 3 conditions | monde à 4 conditions (une interaction de seuil de plus) : refus |
| R5-3 | feuilles ≤ 48 | monde à 48 feuilles au plus | monde à plus de 48 feuilles : refus |
| R5-4 | composantes ≤ 10 (conditionnelles et latente comprises) | monde à 10 | monde à 11 : refus. En v4, cette borne n'est tenue **que par le gabarit** (`tirer_gabarit_v4`) ; le vérificateur ne la contrôle pas (ses bornes par classe permettent jusqu'à 2 + 3 + 4 + 2 + 1 = 12 composantes ; lecture du code). Le vérificateur neuf la contrôle, puisque T_pire = 37 du devis en dépend |
| R5-5 | au moins 2 leurres (traits sans effet) | monde à 2 leurres | monde à 1 leurre : refus |
| R5-6 | compilation de la conditionnelle | monde à **conditionnelle chaînée** : la loi compilée par le code neuf est égale, sur un jeu fixe d'instances, à la loi écrite à la main dans la grammaire de référence (une principale − p et une interaction de seuil + 2p à 0 sur le trait de condition), écart ≤ 10⁻⁹ | même monde, signe de la branche inversé : écart refusé |
| R5-7 | égalité du module neuf avec `monde_riche_v4.py` | sur les 12 graines de développement (`cle("monde-mr1-v4-calibration-developpement", r)`) : devis égaux à l'octet, suite des refus égale au champ `refus` des parties v4, étiquettes C8 égales, champ `resultat` d'une génération simulée égal | une graine décalée : différence détectée |

Ces essais sont du **code**, non de la conception : ils ne sont pas faits ici. Un échec de R5-7 (le module neuf ne rend pas les
mondes de la v4) est un nœud : le pilote a tiré ses mondes avec le générateur v4, et p_c ne se transporte que sur la même famille.

## 3. Règle de garde, écrite d'avance

### 3.1 Texte (mot de Lazar R-2492, recopié)

> « Pas de course si moins de la moitié des mondes de calibration gardent une composante certifiée encore trouvable après une
> génération 1 simulée. »

### 3.2 Définitions opératoires (v5 : forme qui décide au banc ; entre parenthèses, ce que faisait la mesure indicative de la v4)

La règle se lit au banc de calibration complet (GO-2026-11-17-05, Q-B2 (b)), en **dernière étape** de l'ordre D-2 du brouillon 3
(§6 : f, fusion, n, forme de la valeur e de groupe, τ, puis la règle) ; elle se sert des valeurs que les étapes d'avant ont
fixées et n'en rejoue aucune.

- **Mondes de calibration** : **N = 24** mondes, rangs r = 0 à 23, **fixé** (Q-15 (b), R-2501 ; E-8 (i)), tirés d'un **secret de
  calibration neuf**, distinct du secret du pilote et du secret de test (conception v3 §1.8 et §2.5 ; Q-3 (c), même forme). (v4 :
  12 graines de développement publiques, mesure indicative qui ne décide pas.)
- **Tirage d'un monde** : au plus **8 tirages** du générateur MR-2 (module neuf égal à `generer_v4`, §2.4, R5-7), chacun vérifié
  C0 à C8 v4 (toute conditionnelle certifiée) ; le premier tirage conforme est le monde du rang r.
- **Indicatrice par monde** g_r ∈ {0, 1} :
  - g_r = 0 si **aucun tirage conforme en 8** (le monde est tiré, compté au dénominateur, et ne garde rien ; GO-2026-11-17-05,
    Q-B3 (a) ; E-8 (ii)) ;
  - sinon g_r = 1 si et seulement si l'ensemble E_r des composantes **certifiées** du monde (latente exclue), **non captées** au
    sortir de la génération 1 simulée à P_CACHÉE (valeur qui décide, ci-dessous), est non vide ; g_r = 0 sinon.
- **Compte et règle** : **G = Σ_r g_r** (somme sur les **24 mondes tirés**, conformes ou non) ; la règle **tient si et seulement si
  2·G ≥ N**, soit **G ≥ 12** : comparaison d'entiers, aucun arrondi, aucune virgule. (v4 : compte sur les seuls mondes
  conformes, `resume` de `monde_riche_v4.py` : `garde * 2 >= len(ok)` ; le code de la course et du banc doit coder la forme v5,
  avec un essai R5 : 12 conformes gardants et 12 non conformes → tenue ; 11 et 13 → non tenue.)
- **Composante certifiée** : étiquette C8 « certifiée détectable quand le reste du monde est connu » du vérificateur (borne basse
  de Wilson à 95 % ≥ 0,8, 200 graines, m = 48), **inchangée** par les valeurs du banc ; la latente est exclue (V-7). Après la
  règle de fusion du banc (brouillon 3, §6), une composante fusionnée compte pour une, avec l'étiquette la moins favorable de ses
  membres ; pour le compte restreint (ci-dessous), elle compte comme conditionnelle si l'un de ses membres en est une.
- **Captée** : attribution de l'oracle Δ_i ≥ max(0,005 ; f · I_i), **f retenu par le banc** (étape 1 de D-2). (v4 : f = 0,75.)
- **Génération 1 simulée** : 4 proposeurs × 6 cartes, archive de départ {K1}, **m = 48**, regroupement stratifié ε = 0,01 et
  ε_strat = 0,04, e-BH sur les groupes, représentant à tranche de choix appariée, test de mort ; juge simplifié contre le nul v8 de
  l'archive à **n retenu** et valeur e de groupe à la **forme retenue** (étapes 3 et 4 de D-2) ; composantes fusionnées selon la
  règle retenue (étape 2). (v4 : n = 400, forme `log_e_groupe` de la v3b, sans fusion.) **Modèle de proposeurs**, gelé : celui de
  la v3b (garder un effet connu 0,9 ; proposer une composante inconnue : forte 0,5, moyenne 0,25, latente 0,25, faible 0,1 ; bruit
  σ = 0,15) ; une conditionnelle est proposée à **P_VUE = 0,25** (supposée, non mesurée) si sa composante de condition est connue
  (dans une carte retenue d'une génération **antérieure**), à **P_CACHÉE** sinon. En génération 1, les connus sont {K1} : aucune
  conditionnelle n'y a sa condition connue (K1 est une forte, jamais la condition ; la seconde conditionnelle d'une chaîne a pour
  condition la première).
- **Valeur qui décide** : **P_CACHÉE = p_c ponctuel du pilote = 0** (x = 0 sur 14 appels ; verdict v2 du pilote, champ `regle`
  `P_CACHEE_banc = 0,0`). (v4 : 0,02, estimée sans pièce.)
- **Passes rapportées, qui ne décident pas** (E-8 (iii) et (iv) ; verdict v2 : « le banc rapporte aussi la règle aux deux bornes
  de l'intervalle ») : sur les **mêmes 24 mondes** et le **même flux** de génération 1 (indice de flux = rang r ; dans la v4 la graine du flux porte le drapeau de masquage : la passe 0,25 « sans masquage » n'a donc pas le même flux que les autres, sauf si le module neuf sépare la graine du drapeau, à coder et à essayer (R5) ; `course` tire une
  uniforme par composante quelle que soit sa probabilité, si bien que les passes ne diffèrent que par le seuil appliqué à la même
  uniforme), une génération 1 simulée pour chaque P_CACHÉE de **{borne haute de l'intervalle du pilote ; 0,01 ; 0,02 ; 0,03 ; 0,04 ;
  0,05 ; 0,25 (sans masquage)}**. La borne basse de l'intervalle égale le ponctuel (0) : pas de passe de plus. La borne haute se
  recopie du champ de la sortie de mesure scellée du pilote par qui a le droit de la lire ; son recalcul est 1 − 0,025^(1/84) =
  **0,042965** (Clopper-Pearson à 95 % de 0 sur 14 appels, ramené à la carte, six cartes par appel ; le verdict v2 dit 0,0430).
  Pour chaque passe : G, sa borne de Wilson, et la règle « tenue » ou « non tenue » **à titre d'information**. La passe qui
  décide se joue la première et son compte s'écrit avant les autres.
- **Comptes rapportés à côté de G, pour chaque passe** (E-8 (iii)) : **G_cond**, le compte restreint aux mondes qui gardent une
  **conditionnelle** certifiée non captée (en v4 : 7 sur 12 contre 8 ; le monde 0 n'y gardait qu'une moyenne ordinaire manquée par
  le hasard du flux, « connue » mais non « captée », ce n'est pas la capacité que la famille revue devait créer) ; le nombre de
  mondes sans tirage conforme ; les refus par contrôle **avec leurs motifs** (§4.1) ; la classe de chaque composante restante.
- **Prédiction chiffrée** (R1 ; modèle réduit du §3.4) : à P_CACHÉE = 0, G = 24 le plus probable (0,91 à ρ = 0,5), la règle tient avec une probabilité
  au-dessus de 0,9999 ; au moins un monde sans tirage conforme avec la probabilité 0,09 (0,5 refus par tirage) à 0,33 (0,6) ; à la
  borne haute, part attendue des mondes gardants 0,35 à 0,38 (G ≈ 8 à 9), règle tenue avec la probabilité 0,08 à 0,17 seulement ;
  sans masquage, G ≈ 0. Aucun signe n'est visé (R3) : la règle décide d'une dépense, elle ne dit rien du progrès.
- **Audit de symétrie (R4), écrit d'avance** : déclenché si G = 24 à P_CACHÉE = 0 (résultat « trop propre », attendu par
  construction, §3.4) **comme** si G < 12 ; il relit les refus, les mondes sans tirage conforme, toute composante certifiée captée
  en génération 1 sans carte qui la porte, et l'égalité des flux entre passes.
- **Ordre et antériorité** (E-7) : code du banc (module neuf, §2.4), modèle de proposeurs (ce paragraphe, avec P_CACHÉE = 0,
  P_VUE = 0,25 et la liste des passes) et cette règle **versés et poussés avant** l'engagement du secret de calibration ; le secret
  s'engage ensuite, puis la phrase de Lazar ; aucune définition ne se change après.
- **Seuil** : « au moins la moitié » = au moins 12 mondes sur 24. **Ce seuil n'a aucune pièce** (note de décision, Q-13) ; il est
  de Lazar, recopié.
- **Ce qui suit un échec** : **pas de course** ; aucune nouvelle famille, aucun nouveau tirage de mondes de calibration et aucun
  réglage du modèle de proposeurs sur ces mêmes mondes ; une famille revue passe par un texte neuf et le mot de Lazar. Un
  succès ne prouve rien sur le progrès : il dit que la course **peut** y répondre.

### 3.3 Ce que la règle mesure, et sa faiblesse dite d'avance (réécrit en v5, E-1)

La règle mesure la **capacité** du dessin sous un modèle de proposeurs, **pas** sous les vrais. Trois choses, dites d'avance :

1. **Point de bascule.** Sous le modèle déclaré, un monde « garde » surtout quand aucune des 24 cartes de la génération 1 ne
   porte la conditionnelle : probabilité (1 − p)²⁴. La part attendue des mondes gardants passe 0,5 vers **p ≈ 0,028** (mondes à
   une conditionnelle) à **0,032** (un monde sur six à chaîne, comme en v4), et la règle tient à 24 mondes avec la probabilité 0,5
   vers **p ≈ 0,030 à 0,034** (§3.4). La valeur posée par la v4 (0,02, sans pièce) était à un facteur 1,5 de ce point.
2. **Le banc ne mesure que les mondes, rien sur les proposeurs.** Avec le modèle gelé, l'issue de la règle au banc est
   presque une fonction de la seule P_CACHÉE posée : à 0,02 elle tenait avec une probabilité d'environ 0,9 quel que soit le tirage
   du secret ; **à 0, valeur que le pilote a mesurée et qui décide, elle tient presque par construction** (au-dessus de 0,9999,
   §3.4) : tout monde conforme porte une conditionnelle certifiée, et aucune carte de la génération 1 n'en porte. Le banc vérifie
   donc que la famille n'est pas vide sur 24 mondes neufs, que le générateur y tient, comment le dénominateur compte, et que rien
   n'est capté par une carte qui ne porte pas la composante ; il **n'est pas une garde** contre le cas « vrais proposeurs sans
   masquage ». Cette garde-là, c'est le pilote qui l'a donnée, avec ses taux d'erreur (§8) ; la passe à la borne haute dit ce que
   vaudrait la règle au bord de ce que le pilote n'a pas exclu.
3. **Le 0,25 « une fois la condition connue » est tout aussi estimé** que l'était le 0,02 : le pilote ne l'a pas mesuré (« P_VUE
   = 0,25 supposée, non mesurée », verdict v2). Il ne pèse pas sur la règle (qui se lit après la génération 1) ; il pèse sur tout
   ce que la conception dit du progrès en génération 2 et 3 (§4.4).

La **part marginale** (§4.3) reste la seule partie de l'argument qui ne dépend d'aucun modèle de proposeurs.

### 3.4 Calcul de la règle (v5 ; E-1, E-8)

Programme `outils-v5/calcul_regle_v5.py` (`41e5bcf07f9f422b589d9466cab5ffbf2f46259be814e8d3c9bc49da992329eb`, scellé avant son
passage, essais internes passés), sortie `sorties-v5/calcul-regle-v5.json` (`10ff446d0c7438642e1fe4a327d6fb35a5308f07ce04b10adcc315ac215958d0`). Il code la règle exacte
(`2·G ≥ N` en entiers ; essais : 12 sur 24 tenue, 11 sur 24 non tenue, 6 sur 12 tenue, 5 sur 12 non) et calcule, par **somme
binomiale exacte**, la probabilité qu'elle tienne au banc sous un **modèle réduit** : 24 cartes en génération 1, chacune porte une
conditionnelle inconnue avec la probabilité p, indépendamment ; un monde à une conditionnelle garde si aucune carte ne la porte ;
un monde à chaîne garde si l'une au moins de ses deux conditionnelles n'est portée par aucune carte ; un tirage est refusé avec la
probabilité ρ, un monde sans tirage conforme en 8 ne garde rien. Le modèle réduit **ignore** les cartes porteuses non retenues et
les autres certifiées manquées (qui font garder plus) et les captures par une carte qui ne porte pas la composante (qui font
garder moins) : c'est un calcul, pas une simulation ; le banc refait la table avec le code gelé (E-8 (iv)).

| P_CACHÉE (p) | part attendue des mondes gardants (q) | règle tenue sur 24 mondes | sur 12 (pour mémoire, v4) |
|---|---|---|---|
| **0 (pilote, décide)** | 0,996 | **1,0000** | 1,0000 |
| 0,01 | 0,78 à 0,81 | 0,9995 à 0,9999 | 0,994 à 0,997 |
| 0,02 (v4) | 0,61 à 0,65 | 0,91 à 0,96 | 0,86 à 0,92 |
| 0,03 | 0,48 à 0,52 | 0,50 à 0,66 | 0,56 à 0,67 |
| 0,04 | 0,37 à 0,41 | 0,14 à 0,25 | 0,27 à 0,37 |
| **0,042965 (borne haute du pilote)** | 0,35 à 0,38 | **0,09 à 0,17** | 0,21 à 0,30 |
| 0,05 | 0,29 à 0,33 | 0,02 à 0,06 | 0,10 à 0,16 |
| 0,25 (sans masquage) | 0,001 | 0,0000 | 0,0000 |

Chaque fourchette va du cas « aucun monde à chaîne » au cas « un monde sur six à chaîne » (2 sur 12 en v4), à ρ = 0,5 (12 refus
pour 12 conformes en v4) ; à ρ = 0,6, les valeurs baissent de moins de 0,03 (sortie, champ `table`). Bascules à ρ = 0,5 (champ
`bascules_rho_0_5`) : q = 0,5 à p = 0,0283 et 0,0318 ; règle tenue avec la probabilité 0,5 à p = 0,0300 et 0,0336, avec la
probabilité 0,05 à p = 0,0463 et 0,0507. Probabilité qu'aucun des 24 mondes ne soit sans tirage conforme : 0,91 (ρ = 0,5),
0,67 (ρ = 0,6). Les valeurs à 12 mondes recoupent la table approchée de la contre-lecture (0,87 à 0,02 ; 0,56 à 0,03 ; 0,27 à 0,04 ;
0,11 à 0,05) : elles en sont la forme exacte sous le même modèle réduit.

## 4. Simulations sur la famille v4

Script `outils-v4/monde_riche_v4.py` (`4b165847…`, scellé avant toute partie ; chaque sortie porte cette empreinte dans son
champ `script_sha256`, vérifié) ; lanceur `outils-v4/lancer_sorties_v4.sh` (`e2f6e0ea…`) ; **une partie par monde, scellée**,
un seul processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2` ; journal `sorties-v4/journal-sorties-v4.txt`
(`8d284f0b…`) : 08:02:15 → 09:17:45 UTC, 12 parties code 0, résumé code 0. Résumé `sorties-v4/resume-v4.json`
(`c4c55f010bed7e28d0e87c72a8702cabd4f0807a7023309f4c62c238829dfbd5`) ; table par monde `sorties-v4/table-v4.json`
(`145c0dbcaeff5c5657ce7680a8375f1413686e382b8f754603fb66e5bcfb0604`, par `outils-v4/table_v4.py`, `1b48486a…`). Chaque partie :
générer et vérifier le monde (C0 à C8 v4, 200 graines), mesurer la part marginale, courir **3 générations avec masquage** et
**1 génération sans masquage** (même monde, autre flux aléatoire). Aucun réglage de la famille, du modèle de proposeurs ou de
la règle après lecture : les chiffres ci-dessous sont ceux du premier et seul passage (force de cette affirmation : §2, E-7).

### 4.1 Générateur et vérificateur

- **12 mondes conformes sur 12** ; **12 tirages refusés** avant eux (C6 : 8 ; C0 : 3 ; C3 : 1), contre 5 refus pour 8 mondes au
  banc v2 (`sorties-v2/banc-generateur-v2-resume.json`). C6 (attribution d'une « K1 + un effet » en écart) refuse plus souvent :
  **cause non établie** en v4 (le concepteur soupçonnait l'attribution des « K1 + conditionnelle » sans leur condition) ; C0 :
  motif non relu dans les parties en v4. Au plus 3 refus pour un monde (mondes 4 et 11), sous la borne de 8.
- **L'« essai à blanc du bac à sable » (E-7, v5)** que la v4 citait pour le motif C0 n'est **pas consigné** : aucune graine, aucune
  sortie gardée, rien d'autre de lu que la phrase de la v4 (« un décalage au-delà de la borne 4 après étalonnage »). Il ne compte
  pour rien ; les motifs qui font foi sont ceux du point suivant.
- **Motifs des refus établis (E-6, v5)** : les 12 tirages refusés des 12 graines de développement, rejoués par
  `outils-v5/motifs_refus_v4_v1.py` (`150a831c…`, scellé avant son passage ; 00:32:23 → 01:01:24 UTC ; sortie
  `sorties-v5/motifs-refus-v4-v1.json`, `a70cbc06883a6c047fc18cc606d65d412338dfff535cc7ee770ed1d126d7bd98`) : la suite des
  contrôles refusés est **égale**, monde par monde, au champ `refus` des parties v4 (`tous_egaux` vrai) ; les sortes des
  composantes des tirages refusés en C6, par `outils-v5/sortes_refus_c6_v4_v1.py` (`b77f062b…`, scellé avant son passage ;
  sortie `sorties-v5/sortes-refus-c6-v4-v1.json`, `9542b6cfa511413a1fec7513bc5e83e86f10598cd824f2994ef27566f527f15f` ; structure
  seule, aucun paramètre de taille).
  - **C6 (8 tirages, 10 vraies plantées en écart)** : le soupçon de la v4 est **réfuté sur ces graines** : **aucune** « K1 +
    conditionnelle » n'est en écart, et aucune conditionnelle n'est captée en trop. Les 10 vraies en écart sont toutes des
    « K1 + un effet de sous-population » (interaction de sous-population forte : 4 ; décalage de sous-population moyen : 4 ;
    décalage faible : 2) ; dans les 10, l'attribution capte **en plus** un **décalage de sous-population** (11 composantes en trop :
    10 faibles, 1 moyenne), sur la même sous-population dans 6 vraies sur 10. Lecture : deux effets qui ne
    jouent que par la sous-population se recouvrent assez pour que la loi de l'un franchisse le seuil d'attribution d'un faible
    (Δ_i ≥ max(0,005 ; 0,75 · I_i)) ; c'est une **non-séparabilité** de la grammaire de la v3 (MR-1), non un effet de la sorte
    neuve. Pourquoi la v4 refuse plus souvent que le banc v2 (8 C6 en 24 tirages, contre 5 refus de tout motif pour 8 mondes) :
    **non établi** ; hypothèse, non mesurée : la borne « au plus 6 traits portant un effet » de la v4 favorise les effets de
    sous-population, qui n'ont pas de trait.
  - **Sélection déclarée** : C6 écarte les mondes où un décalage de sous-population (presque toujours faible) n'est pas séparable
    par l'attribution d'un autre effet de sous-population ; il **n'a pas sélectionné** sur les conditionnelles dans ces 12 graines (8 tirages refusés, aucune « K1 + conditionnelle » en écart) ; rien ne le garantit pour les 24 mondes du banc, où les refus se rapportent par motif (§3.2). La règle de fusion
    du banc (brouillon 3, §6) ne s'applique qu'aux mondes conformes : elle ne change pas cette sélection.
  - **C0 (3 tirages)** : un coefficient au-delà de la borne 4 après étalonnage (décalage de E4 au monde 1 ; pente de E1, une
    principale, aux mondes 4 et 7) : c'est ce que la v4 disait de son essai à blanc, établi cette fois sur les tirages eux-mêmes.
  - **C3 (1 tirage, monde 11)** : « E6 : deux échantillons de l'oracle en désaccord (0,0022 nat) » : désaccord de mesure de
    l'information entre deux échantillons de l'oracle, au-delà de la tolérance.
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
(Q-13 (e)) mesurerait (§7). **v5** : la règle bascule vers p ≈ 0,03 (§3.3, §3.4) ; le pilote l'a mesurée depuis (p_c = 0 sur 14
appels, intervalle [0 ; 0,043], §8).

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
  contre 28 sur 181 en v3b (15,5 %) ; tolérance de Q-9 (a), à mesurer au banc. **v5 (E-9 (iii))** : la tolérance τ est **refaite
  sur MR-2** au banc (étape 5 de D-2) ; la valeur de la v3b ne se transporte pas.
- Sous le modèle, la génération 3 reste presque vide : elle n'a à répondre que dans les mondes à chaîne (2 sur 12) ou en
  retard (monde 10). Une course de 2 × 3 a donc peu de chances de dire quoi que ce soit sur la génération 3 ; la question
  « progrès » se joue en génération 2. **v5 (E-9 (ii))** : avec 2 mondes de test et une part de mondes à chaîne de 2 sur 12, la
  chance qu'un au moins des deux en porte une est 1 − (10/12)² ≈ **0,31** (calcul, part estimée sur 12 mondes).

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
  journal v4), aucune ligne de GO. **v5** : ce point est dépassé par GO-2026-11-17-05 (banc sur une machine jetable louée, ligne
  « calcul » sur devis refait pour le banc complet, au pire sous 3 USD) ; les coûts par appel mesurés au pilote (§8) entrent dans
  le devis de la course, à revoir dans sa propre pièce (condition « devis revu après la v4 » de GO-2026-11-13-01). La v5 ne change
  aucun chiffre de ce §5.


## 6. Ce qui change pour le préenregistrement (brouillon 3, `2dda3b74…` ; pour le rédacteur du texte neuf)

Décisions de Lazar (R-2492) à porter comme **figées** : Q-1 (b) 2 mondes × 3 générations ; Q-3 (c) secret machine engagé et
poussé, puis la phrase de Lazar ; Q-9 (a) vraie découverte = gain au-delà du seuil contre l'archive **et** contre ses mélanges,
tolérance mesurée au banc ; Q-10 (a) générateur publié avec le code, mondes et secret privés jusqu'au verdict, mondes publiés
seulement sur son mot ; Q-11 (a) traits observés à effet caché, leurres, latent un monde sur trois ; Q-12 (i) (a) fausses non
testées, vraies testées à chaque génération ; Q-12 (ii) **un tiers** (arrêt au-delà de 12 tests coupés sur 37 en génération 1) ;
Q-13 (c) famille revue (cette conception) avec la règle de garde.

| section du brouillon 3 | changement |
|---|---|
| §0, §3.1 (famille, générateur, vérificateur) | famille **MR-2** (§2 ici) : classe « conditionnelle » (1 ou 2, [0,04 ; 0,08], condition sur une moyenne, seconde chaînée sur la première) ; au plus 10 composantes ; conditions de seuil ≤ 3 ; **au plus 48 feuilles** (24) ; générateur et vérificateur **sous des noms neufs**, égaux à `generer_monde_v4` et `verifier_v4` (C8 à m = 48, toute conditionnelle certifiée ; **essais R5-1 à R5-7**, §2.4, E-5 ; borne de 10 composantes contrôlée par le vérificateur) ; régularités neuves déclarées publiques **avec le générateur** (Q-10 (a)), **jamais dans la consigne servie** (R-2504) : « une ou deux composantes conditionnelles, sur le signe d'un trait d'une moyenne ou de la conditionnelle précédente » ; fréquences déformées par les rejets, mesurées au banc et déclarées ; **motifs des refus** et sélection qu'ils font, déclarés (§4.1, E-6) |
| §1, §2 (question, hypothèse) | écrire tel quel (E-2) : MR-2 rend la composante **invisible dans la marginale**, non introuvable ; la dépendance à l'archive est logée **dans le comportement des proposeurs**, ni dans le monde ni dans le juge ; une dépendance du côté du juge n'a pas été examinée |
| §3.4 (jeu planté) | inchangé dans sa règle ; « K1 + un effet » d'une conditionnelle **sans** sa condition : vraie au sens de l'oracle si au-dessus de g₀ (C5, C6 la vérifient) ; au plus 9 « K1 + un effet » tenu par la borne de 10 composantes |
| §3.5, §3.6 (proposeurs, grammaire servie) | **E-3 tranché (R-2504, option (a))** : le gabarit servi ne dit **rien** des conditions, des sortes d'effets ni de la famille (le §3.5 du brouillon 3 tient) ; seule la profondeur permise des propositions est ouverte à **3 conditions** (gabarit et gardien) ; le gabarit servi dans la course est **celui du pilote** (empreinte du bloc gelé relevée par le verdict v2, `e77d3041…`), seul le contexte (archive, épisodes) change : p_c ne vaut que pour ce gabarit (§8) |
| §4.1 (prédictions indicatives) | chiffres de la v3b remplacés par ceux de la v4 (§4 ici), marqués « [BANC] » à refaire sur les mondes de calibration ; **prédiction chiffrée de la règle** au banc (§3.2, §3.4 : G = 24 le plus probable à P_CACHÉE = 0 ; règle tenue avec la probabilité 0,09 à 0,17 à la borne haute) |
| §6 (seuils) | **τ refait sur MR-2** (E-9 (iii) : 17,6 % en v4 contre 15,5 % en v3b) ; la règle de garde en **sixième et dernière étape** de D-2, avec f, fusion, n et forme retenus avant elle |
| §6 (seuils), §10 (liste d'arrêt), §16.1 (préalables) | **règle de garde** dans sa forme v5 (§3.2) : **N = 24**, **G sur les 24 mondes tirés** (un monde sans tirage conforme en 8 ne garde rien ; GO-2026-11-17-05), tenue si **2·G ≥ 24** ; **P_CACHÉE = 0** décide ; passes rapportées sans décider (borne haute 0,042965, 0,01 à 0,05, sans masquage) ; G_cond rapporté ; ajoutée à la liste d'arrêt **avant tout appel payant** ; code, modèle de proposeurs et règle **versés et poussés avant** l'engagement du secret de calibration (E-7) ; arrêt Q-12 (ii) au tiers |
| §7 (plan d'analyse), §8 (lecture) | « progrès certifié » se lit par monde : une composante certifiée **captée en génération 2 ou 3** et absente à la fin de la génération 1. **Écrit d'avance (E-9 (i))** : P sur une conditionnelle **n'établit pas** que l'archive a causé la découverte (une seconde génération est aussi un second tirage) ; pour **chaque** conditionnelle captée, rapporter **obligatoirement** si sa composante de condition était dans l'archive servie au début de la génération, et la part des cartes qui portent la conditionnelle avant et après que sa condition soit connue |
| §8 (lecture), §4.2 (puissance) | **écrit d'avance (E-9 (ii))** : la génération 3 n'a de quoi répondre que dans les mondes à chaîne (2 sur 12 en v4) ; avec deux mondes de test, la chance qu'un au moins en porte une est ≈ **0,31** : une génération 3 vide ne se lit pas comme un résultat sur le progrès |
| §8.4 (relevé brut) | ajouter la part marginale de chaque conditionnelle (mesure du monde, avant la course, sans tirage d'issue) |
| §9 (audit de symétrie) | audit de la règle de garde déclenché à G = 24 comme à G < 12 (§3.2) |
| §14 (décisions) | Q-1, Q-3, Q-9 à Q-13 portées comme tranchées (mot R-2492) ; **Q-14 (b)** (pilote d'abord, R-2501 ; fait, issue P-2, GO-2026-11-16-08), **Q-15 (b)** (24 mondes, R-2501), **E-3 (a)** (R-2504), **Q-B1 (a), Q-B2 (b), Q-B3 (a)** du banc (GO-2026-11-17-05) portées comme tranchées |
| §17 (devis) | §5 ici : pire inchangé (409,20 modèles ; 365 sur crédits, 56,20 hors crédits avec la machine sous 57) ; central refait ; à revoir dans la pièce du devis avec les coûts par appel du pilote (§8) |
| §20 (blocs gelés lus par le lanceur) | exigences de la famille (bornes de la v4), contraintes du gabarit v4, la règle de garde (forme v5) et le modèle de proposeurs de la mesure gelés comme blocs : probabilités par classe, **P_CACHÉE = 0** (décide), la liste des passes rapportées et **P_VUE = 0,25** (supposée) |

## 7. Questions et réserves (v5 : Q-14 et Q-15 tranchées ; aucune question neuve)

**Q-14 — Que faire d'une règle qui ne tient que sous l'hypothèse de masquage** (v4 ; **corrigée par E-4, tranchée**). La v4 la
posait avec un « défaut sous 48 heures : (a) ». **Correction E-4** : Q-14 était un **nœud**, sans défaut : elle lisait une
condition de GO-2026-11-13-01 (« règle écrite d'avance ») qui ne tient que sous une hypothèse non mesurée, et le défaut aurait
engagé jusqu'à 419,20 USD sur le silence (hiérarchie de décision : lecture d'une condition de GO et dépense) ; l'option (c)
(« règle exigée sous les deux modèles ») était **factice** : sans masquage, une conditionnelle se comporte comme une moyenne de
MR-1 et la règle échoue par construction (0 sur 12). **Tranchée par Lazar : (b)** (R-2501, « pilote d'une génération avec les vrais
proposeurs » avant la course) ; dessin du pilote : 4 mondes, bras A seul (R-2506) ; pilote MR-2 v14 joué, **issue P-2** (verdict
v2), acceptée (GO-2026-11-16-08). Ce qu'il apprend : §8.

**Q-15 — Nombre de mondes de calibration** (v4 ; **tranchée**) : **(b), 24 mondes** (R-2501). Correction E-8 (i) : N est **fixé**
à 24 avant l'engagement du secret (§3.2), non « au moins 12 ». 24 mondes n'ôtent que le hasard des mondes : sous le modèle gelé,
la règle ne mesure toujours rien sur les proposeurs (§3.3).

**Réserves.**
- Le modèle de proposeurs synthétiques reste **arbitraire** (v3) pour les probabilités par classe (0,5 ; 0,25 ; 0,25 ; 0,1) et pour
  P_VUE (0,25) ; seule P_CACHÉE a désormais une pièce (le pilote : 0 sur 14 appels), et une pièce faible (taux d'erreur, §8).
- **La règle tient au banc presque par construction** à P_CACHÉE = 0 (§3.3, §3.4) : son « succès » attendu ne garde rien contre des
  proposeurs qui trouveraient les conditionnelles sans leur condition ; la garde contre ce cas est le pilote, non le banc.
- La mesure de la règle de la v4 est faite sur des **graines de développement publiques** : elle ne décide rien ; la décision se
  prend au banc complet, sur les 24 mondes du secret de calibration, en dernière étape de D-2.
- La famille **sélectionne** des mondes de plus (conditionnelles certifiées exigées ; plus de refus C6, §4.1) : les mondes de la
  course sont ceux où le juge voit les conditionnelles quand le reste est connu ; dit, comme C5 et C6.
- **Ordre (v4)** : famille, modèle de proposeurs, règle et code **scellés à 08:02 UTC avant toute partie** ; antériorité prouvée par
  l'heure et la parole du concepteur seulement (E-7, §2) ; les §2, §3 et §6 de la v4 ont été rédigés pendant les calculs, après
  avoir vu les sorties des mondes 0 et 1 (contrôle de bon fonctionnement) ; la définition du dénominateur de la v4 a été corrigée
  ensuite pour dire ce que fait le code. **Ordre (v5)** : les trois programmes neufs ont été scellés avant leur passage ; la table du
  §3.4 et les motifs du §4.1 ont été lus après leur passage ; aucune définition de la règle n'a été changée après lecture (la
  forme v5 est fixée par GO-2026-11-17-05, R-2501 et le verdict v2).
- **Ordre des classes pour la fusion** : la règle de fusion du brouillon 3 donne à une composante fusionnée « la classe la plus
  faible » ; la classe « conditionnelle » n'y a pas de rang. La pièce des règles du banc doit le fixer avant le banc ; pour la
  règle de garde, la v5 fixe seulement que l'étiquette la moins favorable vaut (§3.2).
- Lignée : la v4, son code et sa mesure, et cette v5, sont du même modèle (modèle A) ; la contre-lecture de la v4 venait
  d'une autre lignée (modèle B) ; celle de la v5 doit venir d'un lecteur neuf, d'une autre lignée.

## 8. Ce que le pilote MR-2 v14 apprend à la conception (v5 ; verdict v2 seul)

Source unique : `verdict-issue-pilote-mr2-v14-v2.md` (`e64458e8…`), sections lisibles (issue, contrôles, comptes, points 5 et 6,
audit de symétrie, « pour les cribles »). Rien d'autre du pilote n'est lu (ni mondes, ni cartes, ni relevé, ni texte scellé).

| ce que le verdict établit | ce que la conception en fait |
|---|---|
| **Issue P-2 sans réserve**, ligne « P-2 banc » ; « ce qui suit » : « banc de 24 mondes de calibration (code v68 gelé) : P_CACHÉE := p_c ponctuel, P_VUE := 0,25 supposée ; la règle de garde de la conception v4 y décide de la course ; le banc rapporte aussi la règle aux deux bornes de l'intervalle (mesure, ne décide pas) » | §3.2 : P_CACHÉE = 0 décide ; passe à la borne haute rapportée ; la borne basse égale le ponctuel ; le « code v68 gelé » est lu ici comme le code de la course et du banc, sous des noms neufs et égal à la v4 (§2.4, R5-7), au titre de GO-2026-11-17-05 (banc complet), **lecture à confirmer par la mère** : le devis du banc v3 (`ec5a6e99…`, lignes 34, 68, 150 et 188) importe `monde_riche_v4.py` sans le modifier et lit « code v68 gelé » comme l'arbre v68 à v74 du pilote, alors que E-5 exige un module à noms neufs égal à la v4 (R5-7) ; la pièce des règles du banc et le devis du banc complet fixent laquelle des deux lectures vaut, avant tout engagement de secret |
| **x = 0 sur 14 appels répondus** (4, 4, 3, 3 par monde), p_c = 0, intervalle à 95 % [0 ; 0,043] ; par proposeur : Argon 0 sur 4, Astra 0 sur 4, Fable 5.2 0 sur 2, Opus 5.5 0 sur 4 ; unité carte : 0 sur 84 emplacements | la probabilité « cachée » posée à 0,02 sans pièce (v4) est remplacée par 0 ; la borne haute (0,043) est **au-delà** de la bascule de la règle (≈ 0,03, §3.4) : le pilote **n'exclut pas** des valeurs de p où la règle ne tiendrait pas ; à la borne haute, la règle tiendrait avec la probabilité 0,09 à 0,17 seulement (§3.4) |
| **Taux d'erreur du texte, à 14 appels** : course refusée à tort 0,21 si p vaut 0,02 ; permise à tort 0,27 si p vaut 0,051 et 0,09 si p vaut 0,075 ; ces taux sont **optimistes** (appels supposés indépendants) ; entre 0,03 et 0,05, le pilote ne décide rien de fiable | à recopier au préenregistrement de la course : le progrès n'est posable que si les vrais proposeurs masquent, et le pilote ne l'établit pas ; il ne l'a pas réfuté ; le verdict écrit aussi que x = 0 sur 14 est « trop propre pour l'hypothèse » (réserve d'audit, qui ne change pas l'issue). « Une issue P-2 favorable ne dit pas que les proposeurs « ne voient pas » les conditionnelles » (verdict v2) |
| « **P_VUE = 0,25 supposée, non mesurée** » | §3.3 point 3 : P_VUE est aussi estimée que l'était le 0,02 ; elle ne pèse pas sur la règle, elle pèse sur tout ce que la conception dit de la génération 2 |
| « **p_c ne vaut que pour ce gabarit** » ; empreinte du gabarit du relevé égale à celle du bloc gelé (`e77d3041…`) ; témoins d'isolement conformes 16 sur 16 (un message, aucun message système, aucun outil, texte servi égal au manifeste) | §6, ligne §3.5-§3.6 : la course sert **le même gabarit** (consigne et grammaire), conforme à R-2504 ; seul le contexte (archive, épisodes) change ; tout changement du gabarit rompt le transport de p_c au banc et à la course (nœud) |
| **Témoin positif 14 sur 14** : chaque appel répondu porte une composante autre que K1 ; **c = 6 appels sur 14** portent la composante de condition sans la conditionnelle | les vrais proposeurs vont au-delà de K1 dès la génération 1 ; mais la condition n'est portée que par 6 appels sur 14, alors que le modèle synthétique (moyenne inconnue proposée à 0,25 par carte) la ferait porter par 1 − 0,75⁶ ≈ 0,82 des appels de six cartes **si** les cartes étaient indépendantes et si « porter » avait le même sens dans les deux comptes (non vérifié : la règle d'attribution du programme de mesure n'est pas relue ici). Réserve, sans changement du modèle gelé : la vitesse à laquelle la condition devient connue, donc le progrès en génération 2, n'a pas de pièce et le pilote ne l'appuie pas |
| Audit R4 : 42 cartes tirées sur 73 admises ; types de loi : `par_sous_population` 20, `softmax` 12, `melange` 5, **`si_sinon` 3**, `transformee` 2 ; aucune carte refusée au gardien, au-delà de six ou non évaluable | les lois à condition sur un trait (`si_sinon`) sont **rares** dans les cartes relues (3 sur 42) : la profondeur ouverte à 3 conditions (R-2504) est peu employée par les vrais proposeurs en génération 1 ; fait descriptif, compatible avec le masquage, qui ne dit rien de la génération 2 |
| **Deux appels tronqués sur quatre** pour Fable 5.2 (mondes 3 et 4, réponse illisible, 553 s et 510 s), sans carte ; sa mesure repose sur **2 appels** ; 73 cartes admises pour 14 appels (moins de 6 par appel en moyenne) | la génération 1 simulée suppose 24 cartes par génération : c'est une **borne haute** du nombre de cartes réelles ; une génération réelle en porte moins (troncatures, propositions de moins de six lois) ; la lecture de la course rapporte, par génération et par proposeur, les cartes admises et les appels tronqués ; le devis de la course compte les troncatures (pièce du devis, non ici) |
| Durées par appel (« pour les cribles ») : Fable 5.2 de 389 à 553 s, les trois autres de 34 à 109 s ; dépense totale 15,378197 USD, aucune part atteinte | le temps d'une génération réelle est fixé par le proposeur le plus lent (≈ 6 à 9 minutes par appel) ; coûts : pièce du devis de la course, non ici |

## Contre-lecture (v6 : réponse à la contre-lecture de la v5, tour 1)

- **Rapport** : `contre-lecture-conception-v5-tour1-v1.md`, `8ad9488e8f3f10a84298421ad6613a720d7fe5a2faf199810d4faf4e2cd1a28a` (égale à son
  compagnon) ; lecteur neuf (modèle C), d'une autre lignée que le rédacteur de la v5 (modèle A) et que le lecteur de la v4
  (modèle B) : la condition de lignée posée au §7 (réserve « Lignée ») est remplie pour la v5.
- **Verdict du rapport** : « Corrections » ; neuf corrections de la v4 jugées appliquées, règle jugée opératoire, dénominateur
  jugé conforme à GO-2026-11-17-05 ; **une correction majeure (M-1) et cinq mineures (m-1 à m-5)** (le verdict d'une ligne du
  rapport dit « quatre mineures », sa liste en porte cinq : les cinq sont traitées ici) ; quatre remarques facultatives.
- **Pièce de départ** : v5, `a12ab1e50190b8d27ce6daa0e5c44b81f04c674a916103f518d093400b7481d9` (égale à son compagnon).
- **Méthode** : programme `outils-v6/appliquer_corrections_v6_v1.py` (empreinte dans son compagnon `.sha256`, scellé avant son
  passage) : il vérifie l'empreinte de la v5 et du rapport, que chaque « ancien » figure exactement une fois dans la v5 et dans
  le texte courant au moment où il s'applique, et refuse d'écraser la cible. Différentiel `differentiel-conception-v5-v6.diff`
  (`diff -u`, compagnon `.sha256`). Rédacteur de la v6 : modèle C, neuf, qui n'a écrit ni la v5 ni son rapport.
- **Contrôles faits avant d'appliquer** (lecture seule) : M-1 : les lignes 34, 68, 150 et 188 du devis du banc v3
  (`ec5a6e99…`, égale) disent bien que le banc importe `monde_riche_v4.py` sans le modifier et lisent « code v68 gelé » comme
  l'arbre v68 à v74 du pilote ; m-1 : dans `course` de `monde_riche_v4.py` (`4b165847…`, égale), la graine du flux de
  proposition (ligne 212) et celle du juge (ligne 231) portent le drapeau `masquage` ; celle du test de mort aussi (ligne 237),
  ce que le rapport ne cite pas et que le texte neuf de m-1 couvre (« la graine du flux »).

| point | réponse | où | ancien (v5) → nouveau (v6) |
|---|---|---|---|
| **M-1** (majeure) : « code v68 gelé » donné pour conforme au GO alors qu'il contredit le devis v3 du banc | **appliquée** | §8, première ligne de la table | « conformément à GO-2026-11-17-05 (banc complet) » → « au titre de GO-2026-11-17-05 (banc complet), **lecture à confirmer par la mère** : le devis v3 importe `monde_riche_v4.py` sans le modifier […] ; la pièce des règles du banc et le devis du banc complet fixent laquelle des deux lectures vaut, avant tout engagement de secret » (texte du rapport, recopié). La tension reste **ouverte** : elle se tranche dans la pièce des règles du banc et le devis du banc complet, non ici |
| **m-1** : « même flux » faux pour la passe sans masquage dans le code v4 | **appliquée** | §3.2, « Passes rapportées » | « (indice de flux = rang r ; `course` tire une » → la même phrase, précédée de : dans la v4 la graine du flux porte le drapeau de masquage, la passe 0,25 « sans masquage » n'a donc pas le même flux, sauf si le module neuf sépare la graine du drapeau, à coder et à essayer (R5). L'« égalité des flux entre passes » lue par l'audit de symétrie (§3.2) n'est pas réécrite : le rapport ne la vise par aucun couple |
| **m-2** : « et rien d'autre » dépasse la table des changements | **appliquée** | en-tête, « Statut » | « **et rien d'autre** » → « **et rien d'autre que des mises en cohérence sans effet sur un chiffre, ajoutées sans ligne propre dans la table : dernier point du §5, cellule « §17 (devis) » du §6, réserves du §7** » |
| **m-3** : noms de modèles encore dans la pièce | **appliquée** pour les trois couples donnés | en-tête, « Rédacteur » ; §7, réserve « Lignée » | le nom du modèle du rédacteur → « modèle A » (deux fois) ; le nom de la lignée du lecteur de la v4 → « une autre lignée (modèle B) ». La consigne de la tâche (aucun identifiant de modèle ; lettres A, B, C) est lue comme visant ces noms de rédacteurs et de lecteurs |
| m-3, suite : noms des proposeurs et des relais cités du verdict v2 et des lignes de GO (§5, deux points du devis ; §8, lignes « x = 0 sur 14 », « Deux appels tronqués », « Durées par appel ») | **non appliquée** | — | le rapport ne donne **aucun couple** et renvoie la décision à la mère ; ce sont des noms cités de pièces qui font foi (verdict v2, GO), où ils désignent les proposeurs mesurés et les lignes de dépense, non un rédacteur. Inchangés ; à trancher par la mère |
| **m-4** : portée de la sélection C6 dite trop large | **appliquée** | §4.1, « Sélection déclarée » | « il **ne sélectionne pas** sur les conditionnelles » → « il **n'a pas sélectionné** sur les conditionnelles dans ces 12 graines (8 tirages refusés, aucune « K1 + conditionnelle » en écart) ; rien ne le garantit pour les 24 mondes du banc, où les refus se rapportent par motif (§3.2) » |
| **m-5** : réserve du verdict v2 omise au §8 | **appliquée** | §8, ligne « Taux d'erreur du texte » | « il ne l'a pas réfuté. « Une issue » → « il ne l'a pas réfuté ; le verdict écrit aussi que x = 0 sur 14 est « trop propre pour l'hypothèse » (réserve d'audit, qui ne change pas l'issue). « Une issue » |
| remarques facultatives (audit presque certain ; type de E1 pour C0 ; hypothèses de la table du §3.4 ; nom de fichier du §0) | **non appliquées** | — | non exigées par le rapport ; la tâche borne la v6 aux corrections exigées |
| en-tête | mis à jour | titre, « Statut », « Rédacteur de la v6 », « Heures » | version v5 → v6 ; heures de la v6 par `date -u` |

**Rien d'autre ne change** : aucun chiffre de la v5 n'est modifié ; les suggestions S-1 à S-6 de la contre-lecture v4 restent non
appliquées. **Reste à faire** : les couples appliqués sont à revoir par un lecteur neuf (tour 2), qui ne soit ni le rédacteur de
la v6 ni celui du rapport ; la lecture de « code v68 gelé » (M-1) et les noms cités du verdict (m-3, suite) attendent la mère.
