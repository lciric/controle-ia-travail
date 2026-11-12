# Conception — monde riche écrit par un programme et regroupement des doublons au sein d'une génération — v1

- **Statut** : conception (aucun préenregistrement, aucun GO). Écrite pour la course de l'organisme d'idéation à plusieurs
  générations (accord de principe R-2442 ; mots de Lazar R-2443, R-2444, et **R-2461**). **Aucune dépense, aucun appel de
  modèle** ; essais hors ligne seulement, sur des mondes synthétiques écrits par programme.
- **Changement de cadre en cours de travail** : la consigne demandait un monde écrit par Kimi (R-2444). Message de la mère reçu
  vers 22:13 UTC : mot direct de Lazar **R-2461**, « a synthèse place en premier un monde écrit par un programme : go » ; R-2444
  est remplacé sur ce point. Cette conception suit **R-2461** : le monde est **écrit par un programme** (§2) ; l'exclusion de
  Kimi tombe avec son rôle d'auteur ; plus de devis d'écriture par Kimi. Le brouillon de consigne de Kimi
  (`consigne-kimi-monde-riche-v1-brouillon-1.md`, `de6bc5fa…`) reste versé tel quel (R12), **sans objet**. Le vérificateur
  garde son nom de prototype (`verifier_monde_kimi_v1.py`, scellé avant R-2461) : il ne dépend pas de l'auteur du monde.
- **Concepteur** : Claude Opus 5.5 (`claude-opus-5-5`), concepteur neuf, sous-agent de la session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. Je n'ai écrit ni le texte v2 de la course, ni son code, ni son verdict.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-concepteur-monde-riche-doublons-v1.md`
  (`6cab9057ef201a837025bbe58ffed84633ec1ac23bdc6ccd2063b74f08f8094d`, vérifiée, égale à son compagnon) ; interdits communs v2
  (`1ee3b370…`, vérifiés) tenus : aucune lecture de `diag/`, `runs/`, des pièces du bras d'attaque, du mode tenu à l'écart,
  de 7a ou 7b, du dossier du collisionneur sur la diversité (sauf sa synthèse, après levée par la mère) ; aucune écriture git ; recherches par `git grep` avec exclusions ; aucune
  clé lue.
- **Heures** (relevées par `date -u`) : début 2026-11-12 20:26:45 ; fin de la rédaction 2026-11-12 22:31:14 (`date -u`) ; sorties : journal `sorties-v1/journal-sorties-v1.txt` (21:15:24 → 22:12:43), compléments 21:34:46 → 21:34:57, générateur 22:16:07 → 22:30:32.
- **Synthèse du collisionneur sur la diversité** (`docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md`,
  `4f99077b7002782374060ff79d9ccaf64c78d7f0de1ac5db4f0cf054a4d89adc`, vérifiée contre son compagnon) : lue sur message de la mère
  reçu pendant le travail (restriction levée pour ce seul fichier), **après** que l'essentiel de cette conception était écrit
  et ses sorties lancées ; écrite par l'opérateur du tour, **non contre-lue** : traitée comme une entrée à discuter. Ce qu'elle
  change ici et où je diverge : §3.8 et §5.4. Je n'ai ouvert aucune autre pièce de ce dossier.
- **Interpréteur** : Python 3.13.18 et numpy 2.5.3 du système (l'environnement `.venv` n'a pas numpy) ; le scellement par
  `.venv/bin/python -m controle_ia.scellement`.
- **Langue** : « loi » = loi prédictive (probabilité de chaque issue sachant les traits d'une instance) ; « nat » = unité
  d'information (logarithme naturel) ; « gain » d'une loi = gain moyen de log-score par instance sur la loi qui ne connaît que
  la fréquence des issues ; « au-delà de l'archive » = gain moins celui de la meilleure loi de l'archive (sens de l'oracle
  v60) ; « au-delà de l'enveloppe » = gain moins celui du meilleur membre du nul v8 engendré par l'archive (sens neuf, §1.7).

## 0. En dix lignes

1. **Monde riche (famille MR-1)** : 8 traits, 3 sous-populations, 3 issues ; 6 à 9 **effets** nommés de six sortes (principal,
   seuil, interaction de seuil, interaction de sous-population, sous-population, trait latent non observé), en trois classes de
   taille mesurée (forte 0,10-0,25 ; moyenne 0,04-0,08 ; faible 0,02-0,035 nat, **au voisinage du seuil g₀ = 0,02** de
   l'oracle) ; au moins deux traits distracteurs. Le devis du monde se **compile dans la grammaire existante**
   (`par_sous_population` → `si_sinon` → `softmax`, `melange` pour le latent) : `proba` ne change pas.
2. **Changements de code** (noms neufs) : dimension et sous-populations lues dans le monde (la v66 reprend une constante `DIM` de la v65), tirages par
   carte 200 → **400**, oracle neuf (enveloppe, information des effets, attribution), regroupement (étape A), mesures de
   diversité, témoins par test, réponses brutes. Liste au §1.3.
3. **Puissance hors ligne** : juge simplifié (modèle du nul v8 avec l'archive) **étalonné** sur la course v67 : V3 et V4 promues puis survivantes 595 et 489 fois sur 1 000 (publié : 617 et 501), fausses avec {K1} 0 sur 4 000, sans archive 722 à 814 sur 1 000 chacune (publié : 725 à 810).
   Dans 12 mondes MR-1 : fausses couvertes 0 promotion sur 5 760 jugements (sans archive : 99 à 100 % promues) ; à n = 400, le point de 50 % du juge tombe sur g₀ (0,66 de promotion à 0,02-0,03 nat au-delà de l'archive, 0,92 à 0,03-0,04), contre ≈ 0,045 nat à n = 200.
4. **Monde écrit par un programme** (R-2461) : générateur générique (aucune loi dans son code) ; graine d'un monde de test
   dérivée d'un **secret tiré après le scellement**, engagé par son empreinte avant le tirage, révélé après le verdict ;
   gabarit (nombres et sortes de composantes), traits, directions et tailles tirés ; vérifié par programme (C0 à C8 : forme,
   structure, grammaire, tailles, ensemble, jeu planté, oracle, fuite, détectabilité certifiée), **retiré** si refusé ; aucun
   modèle ne voit les lois ; mondes de test privés ; mondes répartis développement / calibration / test. Banc : 12 mondes
   conformes sur 12 (un retirage) ; fortes toutes certifiées détectables, faibles à puissance médiane 0,56 (proches du seuil).
5. **Doublons, étape A** (avant tout tirage, programme) : forme canonique, puis **équivalence prédictive au sens du nul** :
   d(i, j) = min des deux « distances au nul » (ce que i rapporterait au-delà du nul v8 engendré par j si i était le monde),
   liaison complète, ε = 0,01 nat, **et** lecture au maximum par strate publique (192 strates, ε_strat = 0,04 : une différence
   confinée à une région rare ne s'efface plus). Chaque carte est jugée ; **e-valeur du groupe = moyenne** de celles de ses
   membres ; **e-BH sur les groupes** ; un représentant par groupe, **fixé avant tout tirage** (médoïde), seul testé, seul hérité.
6. Essais : sur 12 mondes (`doublons-w12-v1.json`), reformulations, tempérées, mêlées et variantes à σ ≤ 0,1 toujours regroupées (12 sur 12), lois qui diffèrent d'un effet faible ou moyen jamais regroupées (12 sur 12) ; six variantes « à la v67 » d'un même constat (y compris `si_sinon` et par sous-population) en un seul groupe ; sur une génération synthétique de 24 cartes, e-BH par groupe retient 7,3 lois au lieu de 15,4 pour le même nombre d'idées distinctes (4,7 contre 4,8).
7. **Étape B (redondance jugée sur tirages) rejetée pour la sélection** : avec le nul v8 (mélanges, tempérées), elle écarte aussi
   les lois **complémentaires** (élagage par domination : 4,25 lois gardées et 2,5 idées distinctes, contre 7,3 et 4,7 sans lui).
8. **Diversité** : D2, mesure principale, par l'oracle lu une seule fois : composantes du monde **certifiées détectables**
   couvertes, **additionnelles à l'archive**, mesurées sur les **propositions brutes**, puis sur les représentants, puis sur les
   retenues (pertes de la chaîne) ; D1 sans oracle (groupes, nombre effectif de Hellinger, supports de traits), descriptive ;
   **jamais** un critère de sélection ni de composition (N-058). Mondes répartis en développement, calibration et test scellés.
9. **Proposeurs** : aucune famille exclue du fait de l'auteur du monde ; Claude Fable 5.2 et Opus 5.5 (crédits de Claude),
   Argon, Astra (identifiant et prix à confirmer), et Kimi si son compte est rechargé ; expérimentateur Opus, vérificateur
   Argon ; réponses brutes et témoins d'isolement versés par appel et par test, absence = arrêt ; composition jugée sur
   l'oracle et le coût seuls (N-058).
10. **Devis** (estimé) : génération des mondes : calcul seul ; course à 3 générations ≈ 20 USD attendus par monde (dont ≈ 14 sur crédits de Claude), pire cas ≈ 113 USD par monde, machine ≤ 10. Huit questions pour Lazar
    (§7), dont le nombre de mondes (2 mondes × 3 générations recommandé).

## Pièces lues (chemin, empreinte)

| pièce | chemin | sha256 |
|---|---|---|
| texte scellé v2 de la course | `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` | `80fe4f03b4905b2376b8cd16873c9ab93da3b97e4e01a9a2932be329bab0954d` |
| verdict de la course v67 | `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` | `d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459` |
| script de puissance v1 et sa sortie à 1 000 répétitions | `docs/notes/organisme-boucle-reelle-v1/puissance-boucle-reelle-v1.py` ; `sorties-puissance-v1/puissance-boucle-reelle-v1-r1000.json` | `a2afcdd3…` ; `a23959fa…` (texte v2, en-tête) |
| complément génération 2 | `docs/notes/organisme-boucle-reelle-v1/puissance-boucle-reelle-v1-generation2.py` | `f552b1b9…` |
| patch du code v66 (cœur `boucle_reelle_v66.py`, juge `juger_v66`) | `docs/notes/organisme-boucle-reelle-v1/code-v66/organisme-v66-contre-cef5ea6.patch` | compagnon `.sha256` |
| orchestrateur v52b : grammaire et juge par pari, nul des filles, nul de l'archive, e-BH, monde du noyau | `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/selection_pari.py`, `nul_filles_v2.py`, `cycle.py` (`membres_de_l_archive`, `appliquer_multiplicite`), `monde_noyau.py`, `outils.py` | compagnons `.sha256` |
| monde S-V1 | `docs/notes/ideation-organisme-v1/orchestrateur-v52b/exemples/temoins-pari-demo-v1.json` | `fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877` |
| devis de la course v66 | `docs/notes/organisme-boucle-reelle-v1/devis-boucle-reelle-organisme-v1.md` | `60643868de86bb5be71393283e6ecf8dc7c03998a072519bc479af8943a26437` |
| plan chiffré des crédits de Claude | `docs/notes/credits-claude-v1/plan-chiffre-credits-claude-v1.md` | `8f9ee89e7c31535cb57e054531e02a4fc5202e6978318fc682af369845bf8c47` |
| GO-2026-11-12-01 à -06 | `registres/go.md` l. 308-313 | (registre vivant) |
| R-2389, R-2440 à R-2444 | `registres/decisions.md` l. 2347, 2398-2402 | (registre vivant) |
| prix de Kimi | `docs/notes/ideation-organisme-v1/relais-kimi-v1/LISEZMOI-relais-kimi-v4.md` l. 57-58 | `e5d6c5ce3a0d243b6a3d804f7de47539d11807ff1561174712428e40399db17a` |
| prix supposés d'Argon et d'Astra | `…/configuration-v8/commandes-v6/commande_argon_v56_nuit_v6.py` l. 234 ; `docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py` l. 79-82 | `5eae1a04…` ; `22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264` |
| validation du nul v9 (audit du verdict : « puissance perdue ») | `docs/notes/ideation-organisme-v1/validation-nul-v9-v1/audit-verdict-validation-nul-v9-v1.md` | `9086a420a082ed8fd7d76dc666ef5ef336a9f6842be8ff90e4aca7db0d72f7c8` |
| N-045 v2, N-049, N-050, N-053, N-058, N-064, N-065 | `docs/decisions/` | `c7b05e39…`, `8a5bf5e5…`, `a54b128d…`, `2204256d…`, `854f2724…`, `387c9d4e…`, `f820e90d…` |

**Ce que je n'ai pas pu lire** : le code gelé de la course (`a_blanc_v59.py`, `nul_v8.py`, `oracle_tour_ferme_v60.py`,
`boucle_reelle_v65.py`, `tests_de_mort_v5.py`) n'est pas dans le dépôt de travail ; les paquets git v66 et v67 exigent le
commit `94bfd92` (absent ici) ; je n'ai rien cloné. D'où le **juge simplifié** (§1.6), étalonné sur les chiffres publiés, et
les points « à vérifier dans le code gelé » du §1.3.

## Pièces écrites par cette conception (toutes scellées, compagnon `.sha256`)

Chemins relatifs au dossier `docs/notes/organisme-multi-generations-v1/` ; chaque pièce a son compagnon `.sha256` (vérifié par
le script qui a écrit ce tableau). Le présent document est scellé à part (son empreinte ne peut pas y figurer).

| pièce | sha256 | compagnon |
|---|---|---|
| `consigne-kimi-monde-riche-v1-brouillon-1.md` | `de6bc5fa29d437cdd32e92a688e86430ec5750cd4ebb0ebaeac82fc26fb45d83` | oui |
| `outils-v1/complements_synthese_v1.py` | `89eb7ba8c8cf8633541a6de8090767f74619e3f3968ebed8f894b1f8d593e9ba` | oui |
| `outils-v1/devis_multi_generations_v1.py` | `15256924d4373d52f560aebfb9550c8e85e19b3faa7bfee8bf4267d7bbdc43b1` | oui |
| `outils-v1/essais_complements_synthese_v1.py` | `1217d25590b6d76360aa38febc20c2d67d07585fc212eb051899012f98ecc989` | oui |
| `outils-v1/essais_generateur_mondes_v1.py` | `50aa0b9249090917327d0987f5da36394a85e57160b3b154abd59fa543d226ec` | oui |
| `outils-v1/essais_monde_riche_v1.py` | `fe97097bd594d245ebe2a8b8f2adb4b68754b565f1a19f4f5517b4b8858fe5a4` | oui |
| `outils-v1/etalonnage_urne_v1.py` | `c142c77f14d3eeb09da7ff407f02e3808564c52623b38d3c87035a580a095de7` | oui |
| `outils-v1/faire_exemples_v1.py` | `403bd260a9f180d17f6013d10c810f73730408256a46b09e9f897ea025bd7eea` | oui |
| `outils-v1/generateur_mondes_v1.py` | `46f3ac2d40efad200e382d95450d3683529f96a73e716913dbbaf24a3bceb1c5` | oui |
| `outils-v1/lancer_sorties_v1.sh` | `f3f99261fcd15d0a814753b2acaad66b751ade4889a80e1011f5fb4226d95b50` | oui |
| `outils-v1/monde_riche_outils_v1.py` | `1825b956eed638fe4daf3d7395a169fdbdf7c9679076d9ba3fb4a15cfd7ec85e` | oui |
| `outils-v1/normes_coefficients_v1.py` | `a2a6bfffdd001ac30d353ee4913d6857c4714128f5f50ca9b1ef53cf0f672a44` | oui |
| `outils-v1/puissance_monde_riche_v1.py` | `7344b10781928eaf123f6fe27e0370a0be2963c6632665a411a1673d177d844b` | oui |
| `outils-v1/variantes_v67_v1.py` | `8b5b6896e211174da09142d4a907011b083611e21fa0284141af5f49bd1d9a5b` | oui |
| `outils-v1/verifier_monde_kimi_v1.py` | `679f437d966fd2d184885ed77e28b152d76d46f2ca096d58330cf755ff189d7d` | oui |
| `sorties-v1/attribution-w12-v1.json` | `816a7477ab22e63047a48ce3228cc131cb3a0fdd38d0829ce0cf756840b17653` | oui |
| `sorties-v1/attribution-w12-v1.stdout` | `b96ca25d8a3bb7e322ae40c1d0ebd33d0a97743170d5dbb4ce00d886c706712b` | oui |
| `sorties-v1/banc-complements-synthese-v1.json` | `c3f90d88782cf089ad5e82b12e6118273aeabfd567e4af878de68dc65d9f35bb` | oui |
| `sorties-v1/banc-generateur-w12-v1.json` | `f6574bc5ada1ba762d8646b0452ae375d1263a8acb7c65a1abcef39748933865` | oui |
| `sorties-v1/banc-generateur-w12-v1.stdout` | `7508816e85d8e4ade9e34cec1a1d8be12ace90b9b9c9cd1f42ffe28e06dbc854` | oui |
| `sorties-v1/complements-v1-heures.txt` | `c357121de5ec7dc15dd109315547e881d49d1d8cedac95dc6ae1d1a0be308cae` | oui |
| `sorties-v1/detection-w12-r40-v1.json` | `8da67edd2b64f93970a9b5f3f5f67c58c08e05797994f3615a3062fe6aab89b7` | oui |
| `sorties-v1/detection-w12-r40-v1.stdout` | `4f47348d322b16063efc19a74a283742f46c0a5382a812e5bbbb2e90472fbb7b` | oui |
| `sorties-v1/devis-multi-generations-v1.json` | `07162b53ad019f4ac3c2a19486c14cd6f6397fc6be931b17f69313fe1e999466` | oui |
| `sorties-v1/devis-multi-generations-v1.stdout` | `c68068435449e14baafab00932b185ba3426f0a55a40ec603595a4649a79ef95` | oui |
| `sorties-v1/doublons-w12-v1.json` | `2e8cb29bb4263a13e9b3724ead768be38391260e19bd89becc500bccdaa29d99` | oui |
| `sorties-v1/doublons-w12-v1.stdout` | `fde10d676b8a98330e2e9075d4b73d79a9f3d8ae0dee11f2badaf26869459d2d` | oui |
| `sorties-v1/essais-complements-v1.stderr` | `cfaa7ea37d53cf78dad189b2e41686969a015bcc47ff36f2a307b3da494acd08` | oui |
| `sorties-v1/essais-complements-v1.stdout` | `17bc5ccaf22bc9d92de94d5780e0919bfe6e81af2acd2193f6f255ebcfeb3e47` | oui |
| `sorties-v1/essais-generateur-v1.stderr` | `6235fc95aea5b1fcb176565ab2150f96f6b6d2968eed5811e25a552a68475cec` | oui |
| `sorties-v1/essais-generateur-v1.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | oui |
| `sorties-v1/essais-v1.stderr` | `16326af418817262c8c86a34858a07365577e7664f8e9cddab88e6de15fad6e0` | oui |
| `sorties-v1/essais-v1.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | oui |
| `sorties-v1/etalonnage-r1000-v1.json` | `3ee96059581c5281a385e08a037c980ffce0eb8d00d0c0bef933229106268f43` | oui |
| `sorties-v1/etalonnage-r1000-v1.stdout` | `77ff0ab224584d1b5b5b351af7c0d73f44193121715209619ddf22aaaa4b4cc8` | oui |
| `sorties-v1/etalonnage-urne-r300-v1.json` | `c87f964d87dd9610874e8270c1639549f586b4ecdf49786e20e2239a1ffd4e60` | oui |
| `sorties-v1/etalonnage-urne-r300-v1.stdout` | `57c4255661f068120545472061dab12d2f96a5e894f3fa439bb5d8e78584cec6` | oui |
| `sorties-v1/etalonnage-urne-v1-heures.txt` | `994b5f03174aed3a6394664e699a67691b16468a0ab6c4f508e2c2f94e836407` | oui |
| `sorties-v1/exemple-devis-synthetique-v1.json` | `71f20cd05b17876351d0c9ad20c2a7da0170e38d1335a7f0ce5d5420dbe9d0dc` | oui |
| `sorties-v1/exemples-v1.stdout` | `682f4398854f8d8706f0836b9e731b8640c7b34e439e8620934c43ea96c075af` | oui |
| `sorties-v1/exigences-monde-riche-v1.json` | `6076cade5539d0d1bdfd6576a0b240d6180d918133a2810c94d69eb320d46c34` | oui |
| `sorties-v1/generateur-v1-heures.txt` | `8514b74524165e2c26392f8ca69e3678c8f9246f0a413ee86916cbf81591a618` | oui |
| `sorties-v1/generations-w12-g3-n400-v1.json` | `86c7ac0edeb12f12826476de6ab4a922ebee8dc0ed9be076f19d033613516c6a` | oui |
| `sorties-v1/generations-w12-g3-n400-v1.stdout` | `673c50c8fa5f417989643270fb68c595004eec505fc8f41ef806cbab7a8e8e50` | oui |
| `sorties-v1/journal-sorties-v1.txt` | `20c556d44d84f92bf1e024ce69ab4845e273401018c3b676fe7997538649012c` | oui |
| `sorties-v1/normes-coefficients-v1.stdout` | `77e35825879567d028bc0254b08fb363db91bf600c3405928a201c0da73fa5c5` | oui |
| `sorties-v1/rapport-verificateur-exemple-synthetique-v1.json` | `c0ec4238c95a575c349294bb23c69e9dfda2fa215ecf84bc826fc034377ee1f4` | oui |
| `sorties-v1/variantes-v67-v1.stdout` | `3a7a0197d72da177c97780e9a8c9a0982468cfa63c7a562e946ed0f0112eb67f` | oui |
| `sorties-v1/verificateur-exemple-v1.stdout` | `e53936eb6ae969f89467c4162006f4c07e878c8f714747b4728b41a0c4a8fbd8` | oui |

## 1. Monde riche

### 1.1 Pourquoi le monde S-V1 ne suffit plus

S-V1 a 3 issues, 2 traits et une loi softmax ; K1 en tient le trait z0, et **un seul** constat restait à trouver (le trait z1,
≈ 0,47 nat). La course v67 l'a montré : 11 cartes retenues en génération 1, « variantes proches d'un même constat », puis
12 refus sur 12 en génération 2 (verdict v67, réserve R-5). Plusieurs générations n'ont de sens que s'il reste, après chaque
génération, des effets à trouver, de tailles décroissantes jusqu'au voisinage du seuil.

### 1.2 Forme des lois : famille MR-1

- **Instances** (publiques) : 8 traits z0 à z7 indépendants, loi normale centrée réduite, arrondis à six décimales (comme
  `selection_pari.tirer_instances`) ; sous-population g ∈ {0, 1, 2} uniforme. **Issues** : 3.
- **Loi du monde** : scores s_k(x) = b_k + Σ (effets actifs en x), puis softmax. Six sortes d'effets, chacune un vecteur de
  trois nombres :

| sorte | ajoute aux scores | interaction ? | se compile en |
|---|---|---|---|
| `principal` | pente × z_t | non | colonne t des poids de chaque feuille |
| `seuil` | décalage si z_t > c | non (non linéaire) | `si_sinon` sur (t, c), biais de la branche « si » |
| `interaction_seuil` | pente × z_t si z_u > c | **oui** (trait × trait) | `si_sinon` sur (u, c), colonne t de la branche « si » |
| `interaction_sous_population` | pente × z_t dans la sous-population h | **oui** (trait × sous-population) | `par_sous_population`, colonne t de la branche h |
| `sous_population` | décalage dans la sous-population h | non | `par_sous_population`, biais de la branche h |
| `latent` | u × décalage, u ∈ {+1, −1} **non observé** | caché | `melange` de deux arbres (u = +1 et u = −1) |

- **Compilation** (`compiler_monde`, `outils-v1/monde_riche_outils_v1.py`) : `par_sous_population` (si un effet dépend de g) →
  `si_sinon` imbriqués sur les conditions de seuil (au plus 2) → feuilles `softmax` de largeur 8 ; `melange` 1/2-1/2 (ou
  `poids_melange`) au-dessus pour le latent. Au plus 3 × 4 × 2 = 24 feuilles. **Toutes ces formes sont dans la grammaire
  existante** (`selection_pari.TYPES_LOI`) : l'évaluateur `proba`, les tirages du noyau et l'évaluateur servi à
  l'expérimentateur n'ont pas à changer. Égalité vérifiée : l'évaluateur vectorisé de la conception rend les mêmes
  probabilités que `selection_pari.proba` de la copie v52b à 10⁻¹² près (essai `Lois.test_egal_a_selection_pari_v52b`).
- **Tailles** : la taille d'un effet i est son **information** I_i = E_x KL(W(·|x) ‖ W₋ᵢ(·|x)), ce que l'on perd en le retirant
  du monde, les autres gardés (`Oracle.information_effet`). Classes (exigences `sorties-v1/exigences-monde-riche-v1.json`) :
  **forte** [0,10 ; 0,25] (2 effets), **moyenne** [0,04 ; 0,08] (2 ou 3), **faible** [0,02 ; 0,035] (2 à 4) ; au moins 2
  interactions ; au moins 2 distracteurs ; gain du monde [0,30 ; 0,90] nat. La classe faible est posée **au voisinage de
  g₀ = 0,02** : un effet faible ajouté à une loi qui tient déjà le reste rapporte ≈ I_i, juste au-dessus du seuil ; ajouté à K1
  seule, il rapporte moins (de 0,001 à 0,025 nat, médiane 0,016, sur les 36 « K1 + faible » de 12 mondes synthétiques :
  `sorties-v1/detection-w12-r40-v1.json`, champ `oracle` ; donc le plus souvent sous g₀). C'est voulu : les faibles ne
  deviennent trouvables qu'après les fortes, ce qui donne un sens à plusieurs générations.
- **Gabarit tiré par monde, privé** (synthèse, rang 1 : « le nombre et le type des composantes doivent être tirés au hasard,
  de façon privée, par monde ») : le générateur tire, de la graine du monde, les nombres de composantes (forte 2 ; moyenne 2 ou
  3 ; faible 2 à 4), leurs sortes (forte : principale ; moyenne : interaction de seuil, interaction de sous-population ou
  principale ; faible : principale, seuil, sous-population ou interaction de sous-population), la présence d'un trait latent
  (probabilité 1/3), sous les contraintes : au moins 2 interactions, au plus 2 conditions de seuil, au moins 2 traits leurres
  (`tirer_gabarit`, `outils-v1/generateur_mondes_v1.py`) ; puis traits (permutation), directions (centrées), seuils,
  sous-populations, et tailles visées dans chaque classe ; les tailles sont étalonnées par bissection.
- **« Proche du seuil » rendu opératoire** (contrôle C8) : pour chaque effet, la part des graines où le monde W est promu
  contre le nul v8 de {W₋ᵢ} (n = 400 tirages, seuil log(40/0,05)) ; exigence : fortes ≥ 0,9, moyenne des faibles dans
  [0,1 ; 0,9]. Chaque composante reçoit une étiquette : **certifiée détectable** (puissance ≥ 0,8, seuil de la synthèse,
  illustratif là-bas, fixé ici), **proche du seuil** (0,1 à 0,8) ou **indétectable** (< 0,1 : refus si elle n'est pas
  déclarée faible). La mesure principale de diversité compte les certifiées ; les proches du seuil sont rapportées à part.
  Cette certification est faite **contre {W₋ᵢ}**, l'archive la plus favorable (le reste du monde déjà connu) : elle borne la
  détectabilité par le haut ; la détectabilité contre l'archive réelle de chaque génération (sentinelles de la synthèse) se
  mesure **après** la course, hors ligne, quand les archives sont scellées (§1.8). Exemple, sur le monde synthétique de démonstration (`sorties-v1/rapport-verificateur-exemple-synthetique-v1.json`, `c0ec4238…`) : fortes 1,00 et 1,00 ; moyennes 1,00 et 0,92 ; faibles 0,64, 0,59 et 0,48 (100 graines).

### 1.3 Changements de code nécessaires (noms neufs, R12 ; à vérifier dans le code gelé, non lu ici)

| # | pièce | changement | pourquoi |
|---|---|---|---|
| K-1 | juge de la boucle (`a_blanc_v59.juger_carte` ; constante `DIM` de `boucle_reelle_v65`, reprise par `boucle_reelle_v66` l. « ALPHA, K, DIM = B65.ALPHA, B65.K, B65.DIM » du patch ; valeur non lue, 2 d'après le monde S-V1) | `juger_carte_v68(loi, monde, archive, racine, tâche, dimension, sous_populations, tirages)` : dimension et sous-populations lues dans `espace_instances` du fichier du monde (la forme des fiches de `temoins-pari-demo-v1.json` les porte déjà) | D = 8, 3 sous-populations |
| K-2 | même juge | tirages frais par carte **400** (la v67 : 200), instants de lecture 50, 100, …, 400 | puissance aux faibles (§1.6) |
| K-3 | tranche et épisodes servis (`tour_ferme_v64.episodes_de_developpement`, étage v5) | instances à 8 traits et 3 sous-populations ; tranche de 400 épisodes inchangée | idem |
| K-4 | gardien mécanique (jeu factice fixe) | jeu factice à la dimension du monde | une loi à 8 traits doit s'évaluer |
| K-5 | gabarit du proposeur (bornes ±4) | dimension 8, 3 sous-populations, `par_sous_population`, `si_sinon` permis ; **aucune description des sortes d'effets du monde** (seulement la grammaire) | ne pas souffler la structure |
| K-6 | oracle (`oracle_tour_ferme_v60`) | `oracle_monde_riche_v68` : gains v60 inchangés **plus** gain au-delà de l'enveloppe, information des effets, attribution des effets à une loi (§4) ; lu une seule fois, après la course | vérité des « découvertes » quand l'archive grandit |
| K-7 | jeu planté (`boucle_reelle_v65`, garde 19) | règle `jeu_plante_mr1` (§1.5) dérivée du monde par programme ; bloc gelé au texte = empreinte du jeu (le monde reste privé) | le jeu n'est plus écrit à la main |
| K-8 | juge v66 (`juger_v66`, e-BH à m fixé) | `juger_v68` : étape A du regroupement entre gardien et juge ; e-BH sur les groupes ; représentant par groupe (§3) | doublons |
| K-9 | lecture gelée | mesures neuves (groupes, D1, D2, attribution) ; jetons d'Argon lus aux champs `entree` et `sortie` (réserve R-6) ; touches de la recherche de la loi plantée **toutes rapportées** (réserve R-1) | réserves de la v67 |
| K-10 | commandes externes et étage | réponse brute de chaque appel de proposeur et témoin d'isolement de chaque exécution versés, absence = arrêt (§5.3) | réserve R-2 |
| K-11 | lanceur | plusieurs mondes : une course par monde, graines par monde, relevés séparés ; **aucune information d'un monde servie dans un autre** | §1.6 |

Ce que la v67 garde : la loi `proba`, le nul v8 et sa classe couverte, l'étage des tests de mort v5 et son bac `bwrap`, le
contre-calcul, la sélection v57, la lecture de la sélection par la génération suivante (gardes 17, 18, 21, 23).

### 1.4 Archive de départ

**K1 du monde** : la meilleure loi softmax du **seul trait de l'effet principal le plus fort**, ajustée par le programme au
maximum de vraisemblance attendue sous le monde (étiquettes douces, Newton ; `k1_du_monde`), arrondie à six décimales, scellée
comme bilan de génération 0 (comme la pièce M1 de la v65). Exigences (C4) : gain de K1 dans [0,05 ; 0,30] et au plus 0,6 fois
celui du monde. Raison (celle du texte v2, §3.2) : sans loi connue, les fausses « couvertes » seraient des lois fixes refusées
trivialement ; avec K1, elles portent de l'information et ne sont refusées que par l'archive.

### 1.5 Lois plantées (jeu planté dérivé du monde par programme, règle gelée avant le tirage)

- **Vraies** (`jeu_plante_mr1`) : **V-monde** (le monde lui-même) ; pour chaque autre effet i, **V-K1+i** = le monde réduit aux
  effets de K1 et de i, **calibré** (tempéré et incliné au maximum de vraisemblance attendue : une loi partielle juste mais trop
  confiante devient calibrée) ; **V-diluée-0,03** et **V-diluée-0,05** = mélanges λ·W + (1 − λ)·K1, λ choisi pour un gain
  au-delà de {K1} de 0,03 et 0,05 nat (vraies « faibles » au sens du gain). Une V-K1+i dont le gain au-delà de l'archive
  (v60 **et** enveloppe) est sous g₀ reste une **mesure**, jamais une vraie du critère (cas des V-K1+faible en génération 1).
- **Fausses couvertes** (classe du nul v8, comme F1 à F4 de la v67) : F1 copie de K1, F2 0,8·K1 + 0,2·uniforme, F3 0,8·K1 +
  0,2·loi fixe, F4 K1 tempérée et inclinée ; en génération g ≥ 2, en plus : **copies des quatre premières représentantes
  retenues** (P5 de la v67) et **F5 = mélange 1/2-1/2 de deux lois de l'archive** (« tout mélange de lois connues », docstring
  du nul v8 citée par le texte v2, §3.4). Vérification C5 : gain au-delà de l'enveloppe ≤ 10⁻³.
- **Sonde hors classe** (mesure, jamais un critère) : H1 = `si_sinon(z_t > 0, K1, A2)`, recombinaison par morceaux de deux
  lois d'archive (classe non couverte du nul v8 ; brèche d'A1-v3 sur W2). Dans un monde riche à structure par morceaux, une
  telle loi peut porter de l'information vraie : l'oracle la classe par son gain au-delà de l'enveloppe (§1.7).
- **Instruments** : T-ELIM (le monde à la puissance 1,25, seuil de test 2,0) et T-MAL (sans statistique), comme la v67.
- Toutes servies à l'aveugle (identifiant opaque), hors famille au seuil log(m/α), **jamais regroupées avec les cartes**,
  jamais retenues ni servies (garde 7).

### 1.6 Puissance par simulation hors ligne

**Juge simplifié** (`juger`, `outils-v1/monde_riche_outils_v1.py`) : pari plein ; dénominateur = maximum, aux instants de
lecture, de la marginale ajustée, de l'uniforme, des moyennes glissantes (fenêtres 5, 10, 20, 50) et, par loi de l'archive,
de la loi, de son mélange à l'uniforme (grille de 21 poids), de sa version tempérée et inclinée ajustée (Newton), et du
mélange linéaire ajusté de toutes les lois de l'archive et des lois certaines (espérance-maximisation, écart de Frank-Wolfe
ajouté) ; seuil hors famille log(m/α) ; e-BH ; test de mort = statistique gelée sur 400 épisodes, seuil 0,02. **L'urne de la
bibliothèque v1 est écartée** (`outils-v1/etalonnage_urne_v1.py`, sortie `sorties-v1/etalonnage-urne-r300-v1.json`,
`c87f964d…`, 300 répétitions) : avec elle, F1, F2 et F4 jugées sans archive sont promues 112, 64 et 93 fois sur 300 (0,21 à
0,37), loin des 725 à 810 sur 1 000 publiés ; sans elle, 244, 228 et 215 sur 300 (0,72 à 0,81) ; V3 et V4 bougent peu (182 et
153 sans, 178 et 149 avec). C'est une inférence sur le code gelé, à vérifier.

**Étalonnage** (`sorties-v1/etalonnage-r1000-v1.json`, `3ee96059…`, 21:20:10 → 21:23:02) sur le dessin exact de la v67 (S-V1, archive {K1}, m = 22,
1 000 répétitions), contre la sortie publiée (`puissance-boucle-reelle-v1-r1000.json`, `a23959fa…`, recopiée au texte v2 §4.2) :

| loi | promue puis survivante, juge simplifié (sur 1 000 ; Wilson à 95 %) | publié (v67, sur 1 000) | plus grand log W maximal |
|---|---|---|---|
| V1 | 1 000 [0,996 ; 1] | 1 000 | 116,2 |
| V2 | 1 000 [0,996 ; 1] | 1 000 | 103,3 |
| V3 (L* tempérée 0,08) | 595 [0,564 ; 0,625] | 617 | 20,6 |
| V4 (0,15 L* + 0,85 uniforme) | 489 [0,458 ; 0,520] | 501 | 19,0 |
| F1 à F4 avec {K1} (promues) | 0, 0, 0, 0 (4 000 jugements) | 0 sur 4 000 | −0,007 au plus |
| F1 à F4 sans archive (artefact, promues) | 814, 760, 779, 722 | 725 à 810 | 24,0 au plus |
| au moins une fausse promue sans archive | 1 000 | 994 | — |
| T-ELIM promue puis éliminée | 1 000 | 1 000 | 124,2 |

Écarts au publié : ≤ 2,2 points sur les vraies faibles, intervalles qui couvrent ou frôlent la valeur publiée ; le juge simplifié
est un peu plus sévère sur V3 et V4 et un peu moins sur F1 sans archive. Gain de S-V1 sur 20 000 instances : 0,521 nat
(publié 0,520) ; K1 0,053 (publié 0,052).

**Détection dans les mondes MR-1** (`sorties-v1/detection-w12-r40-v1.json`, `8da67edd2b64f93970a9b5f3f5f67c58c08e05797994f3615a3062fe6aab89b7`, 21:34:17 → 21:48:19 ; 12 mondes synthétiques, 40
répétitions par loi et par n, m = 40) — part des vraies plantées promues puis survivantes selon leur gain au-delà de l'archive
{K1} (sens v60), pour n = 200, 400, 800 tirages par carte :

| gain au-delà de {K1} (nat) | n = 200 | n = 400 | n = 800 |
|---|---|---|---|
| [0 ; 0,01[ | 0 / 160 (0,00) | 8 / 160 (0,05) | 34 / 160 (0,21) |
| [0,01 ; 0,02[ | 50 / 1 120 (0,04) | 375 / 1 120 (0,33) | 906 / 1 120 (0,81) |
| [0,02 ; 0,03[ | 41 / 240 (0,17) | 158 / 240 (0,66) | 235 / 240 (0,98) |
| [0,03 ; 0,04[ | 179 / 880 (0,20) | 811 / 880 (0,92) | 880 / 880 (1,00) |
| [0,04 ; 0,06[ | 708 / 920 (0,77) | 907 / 920 (0,99) | 920 / 920 (1,00) |
| [0,06 ; 0,08[ | 71 / 80 (0,89) | 80 / 80 (1,00) | 80 / 80 (1,00) |
| [0,08 ; 0,12[ | 272 / 280 (0,97) | 280 / 280 (1,00) | 280 / 280 (1,00) |
| [0,12 ; 0,20[ | 159 / 160 (0,99) | 160 / 160 (1,00) | 160 / 160 (1,00) |
| ≥ 0,20 | 480 / 480 (1,00) | 480 / 480 (1,00) | 480 / 480 (1,00) |

Par classe de l'effet ajouté à K1 (vraies « K1 + un effet », calibrées ; promues puis survivantes, Wilson à 95 %) :

| classe | n = 200 | n = 400 | n = 800 |
|---|---|---|---|
| forte (gain au-delà de {K1} : 0,079 à 0,166) | 466 / 480 [0,952 ; 0,983] | 480 / 480 [0,992 ; 1] | 480 / 480 [0,992 ; 1] |
| moyenne (0,024 à 0,061) | 524 / 960 [0,514 ; 0,577] | 866 / 960 [0,882 ; 0,919] | 958 / 960 [0,992 ; 0,999] |
| faible (0,001 à 0,025, médiane 0,016) | 72 / 1 440 [0,040 ; 0,062] | 485 / 1 440 [0,313 ; 0,362] | 1 097 / 1 440 [0,739 ; 0,783] |

Fausses couvertes (F1 à F4 avec {K1} ; F5 mélange de deux lois d'archive et F6 copie, avec une archive de deux lois) :
**0 promotion sur 5 760 jugements** (2 880 à n = 200, 2 880 à n = 400 ; Wilson [0 ; 0,002] par genre et par n) ; jugées sans
archive (artefact), 1 908 sur 1 920 à n = 200 et 1 920 sur 1 920 à n = 400 : la protection vient de l'archive, comme en v67.
Sonde hors classe H1 (recombinaison par morceaux de deux lois d'archive) : 1 sur 480 à n = 200, 3 sur 480 à n = 400 (dans ces
mondes, le découpage sur le trait de K1 n'apporte presque rien ; ce n'est pas une borne sur la classe non couverte).
Dispersion entre mondes du taux des « K1 + faible » à n = 400 : de 0,21 à 0,54, écart-type 0,10 entre les 12 mondes.

**Choix de n** : à n = 200 (la v67), le point de 50 % du juge tombe vers 0,045 nat au-delà de l'archive : un effet faible
(0,02-0,035) n'est presque jamais promu (0,17 dans [0,02 ; 0,03[), et la classe « proche du seuil » serait invisible. À
**n = 400**, ce point tombe vers 0,02-0,025 nat, c'est-à-dire **sur g₀** : la décision du juge et la vérité de l'oracle
coïncident à peu près (0,66 dans [0,02 ; 0,03[, 0,92 dans [0,03 ; 0,04[ ; mais 0,33 dans [0,01 ; 0,02[, lois réelles sous g₀
que l'oracle comptera comme fausses découvertes). À n = 800, le juge promeut aussi la plupart des lois sous g₀ (0,81 dans
[0,01 ; 0,02[) : il devient plus fin que l'oracle. **Recommandation : n = 400** (Q-5). Les tirages frais sont simulés : n ne
coûte que du calcul. Les promotions sous g₀ deviennent une mesure rapportée (« découvertes réelles sous le seuil »).

**Nombre de mondes et de graines** (`sorties-v1/generations-w12-g3-n400-v1.json`, `86c7ac0edeb12f12826476de6ab4a922ebee8dc0ed9be076f19d033613516c6a`, 21:48:19 → 22:12:43) : 12 mondes MR-1, 3 générations, n = 400, m = 40, ε = 0,01 ; **proposeurs
synthétiques** (4 × 6 cartes ; une carte garde chaque effet déjà connu avec la probabilité 0,9 et ajoute un effet inconnu avec
0,5, 0,25 ou 0,1 selon sa classe, coefficients bruités σ = 0,15 : modèle **estimé**, pas une mesure) ; mêmes cartes et mêmes
tirages pour les trois conditions. Moyennes sur les 12 mondes :

| condition | génération | promues | groupes | retenues | archive | composantes captées (oracle) sur 7 [écart-type entre mondes] | faibles captées | fausses découvertes / retenues (au-delà de l'enveloppe < g₀) |
|---|---|---|---|---|---|---|---|---|
| sans regroupement (règle v67) | 1 | 13,0 | — | 13,0 | 14,0 | 6,17 [1,03] | 2,25 | 11 / 156 |
| | 2 | 11,9 | — | 11,9 | 25,9 | 6,75 [0,62] | 2,75 | 15 / 143 |
| | 3 | 0,17 | — | 0,17 | 26,1 | 6,92 [0,29] | 2,92 | 1 / 2 |
| étape A seule | 1 | 7,8 | 13,2 | 7,8 | 8,8 | 6,08 [1,00] | 2,17 | 11 / 94 |
| | 2 | 6,5 | 15,2 | 6,5 | 15,3 | 6,67 [0,89] | 2,67 | 12 / 78 |
| | 3 | 0,08 | 16,3 | 0,08 | 15,4 | 6,83 [0,39] | 2,83 | 0 / 1 |
| étapes A et B (domination) | 1 | 7,8 | 13,2 | 2,25 | 3,25 | 4,58 [0,79] | 1,00 | 0 / 27 |
| | 2 | 3,8 | 15,0 | 2,17 | 5,4 | 5,83 [0,94] | 1,83 | 7 / 26 |
| | 3 | 1,08 | 15,8 | 0,83 | 6,25 | 6,33 [0,78] | 2,33 | 4 / 10 |

Lecture (estimée) : (i) l'étape A garde **les mêmes composantes captées** (6,83 contre 6,92 sur 7 en génération 3) avec une
**archive plus petite de 40 %** (15,4 contre 26,1 lois) et presque deux fois moins de cartes promues à tester (7,8 contre 13,0 en
génération 1) ; (ii) l'étape B perd des composantes tôt (4,58 contre 6,08 en génération 1) et ne les rattrape pas en trois
générations ; (iii) **les fausses découvertes au sens de l'oracle** (lois retenues à moins de g₀ au-delà de l'enveloppe, le
plus souvent « K1 + un effet faible » portées par e-BH) font 8 à 15 % des retenues à n = 400 : à rapporter, et argument pour que
le préenregistrement exige la vérité par l'enveloppe (§1.7) ; (iv) avec ces proposeurs généreux, le monde est presque épuisé en
génération 2 et la génération 3 ne promeut presque rien : **3 générations suffisent pour un monde de 6 à 9 composantes**, 4
n'ajouteraient que du coût ; avec de vrais proposeurs, plus lents, la génération 3 a plus à trouver ; (v) **dispersion entre
mondes** des composantes captées : écart-type ≈ 1 composante en génération 1 (sur 7), et la puissance du juge sur les faibles
varie d'un monde à l'autre de 0,21 à 0,54 (détection, n = 400). Un seul monde ne dit donc rien de cette dispersion ; deux mondes
en donnent une première réplication ; trois, une estimation grossière.

**Plusieurs graines** : par monde, la sensibilité aux effets faibles se mesure sans agent et sans dépense sur des graines (C8 :
100 graines par composante avant la course ; rejeux des retenues et sentinelles sur 200 graines après, §1.8) ; **plusieurs mondes**
mesurent la dispersion due au monde et aux proposeurs, au prix d'une course par monde. Recommandation : **2 mondes × 3
générations** (Q-1).

### 1.7 Lois fausses, classe couverte et vérité des découvertes quand l'archive grandit

- **Classe couverte** : inchangée (nul v8). Les fausses plantées restent dans la classe couverte **de l'archive de leur
  génération** (garde 18) ; en simulation, 0 promotion sur 5 760 jugements, contre 1 908 sur 1 920 (n = 200) et 1 920 sur 1 920 (n = 400) quand on les juge sans
  archive (artefact).
- **Classe non couverte** : avec une archive de plusieurs lois et un monde à structure par morceaux, les recombinaisons par
  morceaux d'archive deviennent un chemin naturel des proposeurs. Le nul v9 ferme ce trou mais sa validation a rendu
  « puissance perdue » (audit `9086a420…`) : question Q-4 (§7).
- **Vérité** : l'oracle v60 dit « au-delà de l'archive » contre **la meilleure loi seule** ; avec une archive de plusieurs
  lois, une recombinaison couverte (mélange de deux lois d'archive) peut battre chaque loi seule sans rien apporter de neuf.
  L'oracle neuf (K-6) rapporte **aussi** le gain au-delà de l'**enveloppe** (meilleur membre du nul v8 de l'archive, ajusté
  sous le monde : `Oracle.gain_enveloppe`) ; une « vraie découverte » du préenregistrement multi-générations devrait exiger
  les deux (proposition ; décision du rédacteur du préenregistrement).

### 1.8 Répartition des mondes et banc de métrologie (préalable sans appel)

- **Développement** : les mondes synthétiques de cette conception (graines publiques, `outils-v1/`) ; ils ont servi à choisir
  ε, ε_strat, le seuil d'attribution et n ; ils ne servent plus à rien de décisif.
- **Calibration** : un second jeu de mondes **écrits par programme** sur une graine scellée avant le préenregistrement (au moins
  12), où le **banc de métrologie** (synthèse, convergence des cinq espèces) refait, avec le code v68 gelé : l'étalonnage du juge
  (§1.6), la détection par classe, les doublons (paires difficiles **disjointes** de celles du développement), l'attribution,
  et les mondes témoins : **monde à une seule composante** (la couverture doit valoir 1), **monde dont la vérité est un membre du
  nul de l'archive** (aucune promotion attendue), lois sans dépendance à une composante (fausse couverture), variantes éloignées
  de même gain (inflation), recombinaisons couvertes (comptées comme anciennes). Coût : calcul seulement.
- **Test** : les mondes tirés du secret de test (§2.2), scellés, jamais utilisés pour régler un seuil ; lus seulement par le
  vérificateur, le lanceur, puis l'oracle et le lecteur du verdict.
- **Après la course** (hors ligne, sans agent) : sentinelles « archive scellée de la génération g + une composante non captée »
  jugées contre cette archive sur 200 graines (détectabilité réelle génération par génération) ; rejeux des représentantes
  retenues sur 200 graines (fragilité de chaque découverte) ; réinjection des sœurs (§3.5).

## 2. Génération du monde par programme (cadre R-2461 ; remplace l'écriture par Kimi)

### 2.1 Qui écrit le générateur, et comment il reste aveugle aux lois tirées

- **Prototype** : `outils-v1/generateur_mondes_v1.py` (`46f3ac2d43efad200e382d95450d3683529f96a73e716913dbbaf24a3bceb1c5`), écrit par moi (Claude Opus 5.5). **Celui qui fera foi** :
  écrit dans l'arbre de l'organisme sous un nom neuf, essayé (R5), contre-lu par un autre modèle (N-052), gelé par son
  empreinte au bloc du code du préenregistrement.
- **Aveugle** : le code ne contient **aucune loi** ; tout est tiré de la graine (gabarit, traits, directions, seuils,
  sous-populations, latent, tailles visées), puis étalonné. La graine d'un monde de test dérive d'un secret qui n'existe pas
  quand le code est écrit, gelé et contre-lu : ni l'auteur du générateur, ni la session mère, ni un proposeur ne connaissent
  les lois. « Lois inconnues de toute famille de modèles » est tenu par trois règles : (i) seul un programme lit le fichier du
  monde avant le verdict (vérificateur, lanceur, oracle) ; (ii) le rapport du vérificateur ne porte **aucun coefficient**
  (essai `test_sain_monde_genere_conforme_et_rapport_sans_coefficient`) ; (iii) le monde ne s'écrit que dans un dossier privé
  (`ecrire_prive` refuse un chemin public : essai `test_artefact_ecriture_publique_refusee`).
- **Fuite par le générateur** (risque nommé par la synthèse) : la famille (8 traits, six sortes d'effets, classes) est publique
  par la grammaire servie et par ce document ; les proposeurs n'ont pas accès au dépôt. Le prototype garde **deux régularités
  à retirer** dans le générateur v68 : une interaction de seuil est toujours conditionnée sur le premier trait fort, au seuil
  0 ; K1 est toujours la loi du plus fort effet principal. Le gabarit concret de la synthèse ([C-T3]) n'est pas repris.

### 2.2 Graine scellée, paramètres tirés après le scellement

1. Le préenregistrement est scellé : il porte l'empreinte du générateur, les exigences, cette procédure, **aucun secret**.
2. Sur la machine privée qui génère (machine de la course, ou bac à sable de la session mère qui n'écrit aucune pièce servie),
   un secret de 32 octets est tiré (`secrets.token_bytes`, ou combiné à une phrase de Lazar : Q-3) ; son **empreinte**
   (`engagement`) est inscrite au registre et au relevé **avant** tout tirage.
3. Graine du monde r : sha256(secret ∥ empreinte du texte scellé ∥ r), entier ≥ 2⁶⁴ (`graine_de_monde` ; essai
   `test_graine_engagee`).
4. Génération et vérification (C0 à C8) ; **refus → retirage** avec la graine suivante de la même suite, au plus 8 fois
   (`generer` ; essai `test_artefact_verificateur_refuse_puis_retirage`) ; nombre de refus et contrôles en cause au rapport.
5. Fichiers du monde (devis, loi compilée, jeu planté, rapport complet) écrits au dossier privé, sans écrasement, avec leurs
   compagnons ; **seules leurs empreintes** vont au registre et au préenregistrement (bloc gelé lu par le lanceur).
6. Course. 7. Après le verdict : le secret est **révélé** ; quiconque peut regénérer les mondes et vérifier leurs empreintes ;
   la publication des mondes reste un nœud de Lazar.

La même procédure, avec un **autre secret**, tire les mondes de **calibration** (banc de métrologie, §1.8), révélé après le
banc ; les mondes de **développement** ont des graines publiques (celles de cette conception).

### 2.3 Programme de vérification (prototype `outils-v1/verifier_monde_kimi_v1.py`)

Contrôles, dans l'ordre (le premier refus donne le code 2 ; tous écrits au rapport, **sans aucun coefficient du monde**) :

| contrôle | ce qu'il vérifie |
|---|---|
| C0 forme | clés permises seules, aucun texte libre, identifiants `E1`…, types, bornes (±4 ; seuils ±1,5), domaines des traits et sous-populations |
| C1 structure | effets par classe (ceux tirés pour ce monde, dans 2 / 2-3 / 2-4), au moins 2 interactions, distracteurs = traits sans effet (≥ 2), ≤ 2 conditions de seuil, ≤ 1 latent |
| C2 grammaire | loi compilée évaluable, `valider_loi` de la grammaire, ≤ 24 feuilles |
| C3 tailles | I_i sur deux échantillons indépendants de 50 000 instances (accord ≤ max(0,002 ; 5 % de I_i)), dans les bornes de sa classe ; sensibilité nulle aux distracteurs |
| C4 ensemble | gain du monde [0,30 ; 0,90] ; K1 informative et partielle |
| C5 jeu planté | V-monde et au moins 3 V-K1+i vraies au-dessus de g₀ (v60 et enveloppe) ; diluées à ±0,002 de leur cible ; fausses couvertes ≤ 10⁻³ au-delà de l'enveloppe |
| C6 oracle | l'attribution retrouve exactement les effets de chaque V-K1+i au-dessus de g₀ |
| C7 fuite | aucun paramètre du monde (exact, ou à deux décimales si \|x\| ≥ 0,1) dans les pièces gelées servies aux proposeurs, à l'expérimentateur et au vérificateur |
| C8 sensibilité | puissance du juge sur chaque effet (W contre le nul de {W₋ᵢ}, 100 graines, n = 400) : fortes ≥ 0,9 ; moyenne des faibles dans [0,1 ; 0,9] ; étiquette « certifiée détectable » (≥ 0,8), « proche du seuil », « indétectable » |

- **Étalonnage** : fait par le générateur lui-même (bissection de l'échelle de chaque composante vers une taille visée tirée
  dans sa classe) ; l'option `--etalonner` du vérificateur reste pour un devis venu d'ailleurs.
- **Essais (R5)** : 21 essais ciblés, tous passés (`sorties-v1/essais-v1.stderr`, journal : 21:15:24 → 21:17:31), plus 6 essais des
  compléments (`sorties-v1/essais-complements-v1.stderr`, 21:34:46 → 21:34:57) ; pour le vérificateur :
  cas sain (monde synthétique conforme ; aucun coefficient au rapport) ; artefacts refusés au bon contrôle — texte libre (C0),
  coefficient hors borne (C0), distracteur utilisé (C1), deux latents (C1), effet faible hors de sa classe (C3), fuite d'un
  paramètre dans une pièce servie (C7), faibles jamais détectés (C8) ; étalonnage qui ramène dans les classes un monde
  refusé en C3.
- **Exemple de rapport** : `sorties-v1/rapport-verificateur-exemple-synthetique-v1.json` (`c0ec4238…` ; devis `exemple-devis-synthetique-v1.json` `71f20cd0…` ; exigences `exigences-monde-riche-v1.json` `6076cade…` : **conforme**, C0 à C8 tenus (C7 sans objet : aucune pièce donnée) ; tailles mesurées 0,196 et 0,136 (fortes), 0,065 et 0,047 (moyennes), 0,022, 0,029 et 0,027 (faibles), accord des deux échantillons ≤ 0,0007 nat ; gain du monde 0,385, de K1 0,128 ; V-K1+faible à 0,014-0,017 au-delà de {K1}, sous g₀, gardées comme mesures ; fausses ≤ 0 au-delà de l'enveloppe ; attribution exacte pour les six V-K1+i).
- **Ce que le programme ne fait pas** : il ne juge pas la « naturalité » du monde ; il ne lit ni ne sert aucune proposition.

### 2.4 Essais du générateur (R5) et banc

- **Essais** (`outils-v1/essais_generateur_mondes_v1.py`, `50aa0b92…` ; sortie `sorties-v1/essais-generateur-v1.stderr`) :
  8 sur 8 — même graine → même monde (sain) ; graines distinctes → mondes distincts ; 60 gabarits tirés tous dans les
  fourchettes et variés (plus de 20 distincts) ; monde généré conforme, rapport sans coefficient (sain) ; graine liée au rang
  et au texte scellé, ≥ 2⁶⁴ ; écriture dans un dossier public refusée (artefact) ; écriture privée sans écrasement ; exigence
  impossible → deux refus C4 puis abandon (artefact du retirage).
- **Banc** sur 12 mondes de développement (graines publiques 1000 à 1011 ; vérificateur complet, C8 à 100 graines) :
  sortie `sorties-v1/banc-generateur-w12-v1.json` (`f6574bc5…`, 22:16:07 → 22:30:32, sans aucun
  coefficient) : **12 mondes conformes sur 12**, après **un** tirage refusé en tout (C0 : un coefficient étalonné au-delà de la
  borne ±4, retiré) ; 6, 7 ou 8 composantes par monde ; un trait latent dans un monde. Détectabilité C8 (100 graines,
  n = 400) : fortes 24 sur 24 certifiées (puissance 1,00) ; moyennes : 27 sur 28 certifiées (médiane 1,00, plus faible 0,17) ;
  faibles : médiane 0,56, la plus faible à 0,19, 3 sur 32 au-dessus de 0,8 (certifiées) — **la classe faible est bien « proche du seuil »**.

### 2.5 Garde du secret (graine et mondes de test)

- **Ordre** : (1) consignes et gabarits des proposeurs, de l'expérimentateur et du vérificateur **gelés et scellés** ;
  (2) générateur, vérificateur et exigences gelés au préenregistrement scellé ; (3) secret tiré, empreinte inscrite ;
  (4) génération et vérification **dans un processus qui n'imprime que des empreintes et des contrôles** ; (5) empreintes
  du monde au registre ; (6) course. Rien de ce qui est écrit après l'étape 3 n'entre dans un texte servi, sauf les lois de
  l'archive et les épisodes tirés par le noyau (voulu).
- **Où** : secret, devis, loi compilée, jeu planté, rapport complet : dossier privé de la machine qui génère, puis branche
  privée `donnees/monde-riche-v1-prive` du dépôt de travail (privé), chaque fichier avec son compagnon ; une copie à l'octet
  sur la machine de la course. **Jamais** dans `lciric/ideation-organism` (public) ni dans la copie expurgée
  (`scripts/depot_expurge*.py` doit l'exclure : à vérifier).
- **Qui lit** : des programmes seulement (vérificateur, lanceur, oracle) jusqu'au relevé scellé ; puis le lecteur du verdict
  (R13). La branche, le dossier privé et le secret entrent dans les interdits communs (règle 1) de tout sous-agent jusqu'au
  verdict ; aucun modèle d'aucune famille ne les ouvre.
- **Quand publié** : le secret après le verdict (vérifiabilité) ; les mondes, sur ton mot seulement.
- **Fuite vers les proposeurs** : contrôle C7 avant la course sur les pièces gelées ; pendant la course, la recherche de la
  loi plantée (v62 C16, reprise par la v66) étendue aux paramètres du monde, **toutes les touches rapportées** (réserve R-1),
  relues à la main.

## 3. Regroupement des doublons au sein d'une génération

### 3.1 Définition opératoire (étape A, avant tout tirage)

Deux cartes d'une même génération sont **doublons** si (a) leurs formes canoniques sont égales, ou (b) elles sont
**équivalentes au sens du nul** :

- **forme canonique** (`forme_canonique`) : flottants à six décimales ; softmax recentrée sur sa ligne 0 ; mélange sans poids
  nul, composantes triées et fusionnées, composante seule déballée ; transformée sans étape déballée ; `si_sinon` à branches
  égales déballé ;
- **distance au nul** d_nul(i → j) = min, sur les membres m du nul v8 engendré par la seule loi j (j seule ; j mêlée à toute
  loi aveugle fixe ; j tempérée et inclinée), de E_x KL(p_i(·|x) ‖ m(·|x)) : **ce que i rapporterait par instance au-delà de ce
  nul si i était le monde** ; d(i, j) = min(d_nul(i → j), d_nul(j → i)) ;
- calculée sur un **jeu public de 2 000 instances** (traits et sous-populations seulement, **aucune issue**, aucun oracle),
  tiré d'une graine dérivée de la tâche de la génération ;
- **groupes** : liaison complète (deux groupes ne fusionnent que si toutes leurs paires sont sous ε), la paire la plus proche
  d'abord, égalités rompues par l'empreinte de la forme canonique (jamais par le fournisseur) ; **ε = 0,01 nat** (g₀/2).

- **et lecture par strate** (ajoutée après la synthèse, rang 2 : « la moyenne globale efface une différence confinée à une
  région rare ») : la projection m* ajustée globalement est relue au **maximum, sur 192 strates publiques** (sous-population ×
  octile de chaque trait, bornes de la loi normale publique), de la moyenne de KL(p_i ‖ m*) dans la strate ; une paire n'est
  admissible au regroupement que si d < ε **et** d_strat < ε_strat = 0,04 (`outils-v1/complements_synthese_v1.py`,
  `grouper_stratifie`).

Pourquoi ces seuils : deux lois à moins de 0,01 nat l'une du nul de l'autre ne peuvent pas différer d'une « vraie découverte »
(g₀ = 0,02) dans le monde le plus favorable à l'une ; la liaison complète empêche la chaîne a ~ b ~ c avec a ≁ c (essai
`test_liaison_complete_sans_chaine`) ; ε_strat = 4·ε parce qu'une différence étalée sur un octile pèse environ huit fois plus
dans sa strate que dans la moyenne. Banc (`sorties-v1/banc-complements-synthese-v1.json`, `c3f90d88…`) : un effet de seuil
**rare** (z > 1,5 sur un trait distracteur, décalage 0,8) donne d = 0,0095 (la règle globale le fusionnerait) mais d_strat =
0,063 (séparé) ; des variantes bruitées (σ = 0,05 à 0,3, une par σ, dans le monde du banc) restent à d_strat ≤ 0,014 (regroupées). Essais
`essais_complements_synthese_v1.py` : 6 sur 6. Une borne au pire monde (E_x max_y |log p_i − log m|) est aussi rapportée.

### 3.2 Qui le calcule

Un **programme de l'orchestrateur** (`grouper`), entre le gardien et le juge, sur les seules lois des cartes passées au
gardien ; déterministe ; recalculé par la lecture gelée (même entrée → mêmes groupes, sinon écart). **Jamais** un modèle,
jamais un juge de la famille de l'auteur du monde, jamais un score de moniteur (N-053, point 5). Les lois plantées n'y entrent
pas.

### 3.3 Effet sur le juge statistique

- Chaque carte est jugée comme aujourd'hui (tirages frais propres, graine de sa tâche) ; sa e-valeur est arrêtée au seuil
  m/α (`appliquer_multiplicite`).
- **e-valeur d'un groupe = moyenne des e-valeurs de ses membres** (`log_e_groupe`) : une moyenne d'e-valeurs est une e-valeur
  (chaque carte teste le même nul : « le monde est dans la classe du nul de l'archive ») ; la perte au pire est log(taille du
  groupe) quand un seul membre porte la preuve.
- **e-BH sur les groupes**, m fixé d'avance (borne : cartes au plus, plus lois plantées et instruments) : les rangs comptent
  des groupes, non des copies. Ainsi onze copies à log e = 4,5 ne se portent plus l'une l'autre au-dessus du seuil de rang 11
  (log(40/(0,05·11)) ≈ 4,29) : leur groupe affronte le seuil de rang 1, log(40/0,05) ≈ 6,68 (essai
  `test_e_bh_par_groupe_ne_compte_pas_les_copies`).
- Lois plantées : inchangées (hors famille, seuil log(m/α), avec l'archive de leur génération).
- **Preuve écrite de validité** (condition bloquante de la synthèse pour un regroupement avant le juge ; à contre-lire) : sous le
  nul H₀ « le monde est dans la classe du nul v8 de l'archive de la génération », la richesse de chaque carte i, calculée sur ses
  propres tirages frais, est majorée par une surmartingale positive d'espérance ≤ 1 ; arrêtée au premier instant de lecture où
  elle atteint m/α (temps d'arrêt), elle donne une e-valeur E_i, E[E_i] ≤ 1 (arrêt optionnel). Les groupes sont une fonction
  des seules lois des cartes et d'instances publiques **sans issue**, fixée avant tout tirage : ils sont indépendants des
  tirages. Donc Ē_g = (1/|g|) Σ_{i∈g} E_i vérifie E[Ē_g] ≤ 1 : c'est une e-valeur. La règle e-BH (Wang et Ramdas, 2022) appliquée
  à des e-valeurs, sous dépendance quelconque, avec m ≥ nombre d'hypothèses fixé avant les tirages, borne le taux de fausses
  découvertes par α. Le représentant (médoïde, §3.4) est choisi avant les tirages et n'entre pas dans Ē_g. Limite, la même
  qu'en v67 : toutes les cartes testent le même H₀ ; la garantie dit « le monde n'est pas dans la classe du nul », pas « cette
  loi est une découverte au sens de l'oracle » (ce que l'oracle lit après la course).

### 3.4 Effet sur la sélection et sur l'héritage

- Un **représentant** par groupe, **fixé avant tout tirage** : le **médoïde** (le membre dont la plus grande distance aux autres
  membres est la plus petite ; égalités : empreinte de la forme canonique ; `medoide`, invariant à l'ordre d'entrée : essai
  `test_independant_de_l_ordre_d_entree`). **Jamais le membre à la plus grande valeur e** (objection de la synthèse, rang 2 :
  choisir par les tirages du juge romprait la lecture « e-valeur » du représentant). Coût : tous les membres sont à moins de
  ε = 0,01 nat les uns du nul des autres, donc le médoïde perd au plus de l'ordre de ε sur le meilleur membre. **Les simulations
  de cette conception (`generations`, `doublons`) prennent encore le membre au plus grand log e et la seule distance globale** :
  écart dit, d'effet borné par ε sur le gain du représentant ; à refaire avec le code v68.
- Le représentant est **seul testé** au test de mort (économie d'appels d'expérimentateur) ; s'il meurt, le groupe est éliminé
  (aucun second essai).
- **Retenues** = représentants survivants ; **archive** de la génération suivante = archive + retenues ; **vue servie** aux
  proposeurs = cette archive (garde 23 inchangée). Les autres membres sont écrits au relevé (identifiants, fournisseurs,
  distances), jamais servis.
- Copies plantées de la génération suivante (P5) : copies des quatre premières **représentantes** retenues.

### 3.5 Étape B (redondance jugée sur tirages frais) : rejetée pour la sélection

J'ai essayé deux élagages après e-BH, sur tirages neufs : (i) garder un représentant seulement s'il bat le nul de l'archive
et des représentants déjà gardés ; (ii) écarter un représentant **dominé** (un autre va au-delà de lui, lui pas au-delà de
l'autre). Avec le nul v8, qui ne sait que mêler et tempérer, une loi qui apporte un effet neuf mais en manque un autre ne
« va pas au-delà » d'une loi meilleure : les deux élagages écartent des lois **complémentaires**. Sur 12 mondes (`doublons-w12-v1.json`, génération synthétique de 24 cartes), l'élagage par domination garde 4,25 lois et **2,5 idées distinctes** en moyenne, contre 7,3 représentants et **4,7 idées** sans lui ; la première forme écartait davantage encore (essai de développement sur quatre mondes, non versé : aucun chiffre n'en est tiré). L'étape B
n'est donc **pas** une règle de sélection ; elle peut être rapportée comme mesure (redondance par domination), sans effet.

**Contrôle des groupes mal formés (repris du « temps 1 » de la synthèse, comme mesure)** : après la sélection scellée de la
génération, chaque sœur d'un représentant retenu est rejugée hors ligne (tirages neufs, tâche propre, sans agent) contre le nul
de archive ∪ {son représentant} ; une sœur promue montre un groupe mal formé : comptée, rapportée, sans effet sur la sélection ni
sur l'héritage.

### 3.6 Essais hors ligne

Sortie `sorties-v1/doublons-w12-v1.json` (`2e8cb29bb4263a13e9b3724ead768be38391260e19bd89becc500bccdaa29d99`, 21:23:21 → 21:34:17) ; 12 mondes MR-1 ; distances sur 2 000
instances de référence. Paires (a = monde restreint aux deux fortes et à une moyenne ; b = sa transformée) :

| paire | doit être regroupée | d médiane [min ; max] (nat) | gain oracle b − a (médiane, nat) | justes à ε = 0,005 | 0,01 | 0,02 |
|---|---|---|---|---|---|---|
| reformulation (lignes décalées, composante à poids nul) | oui | 0 [0 ; 0] | 0 | 12/12 | 12/12 | 12/12 |
| tempérée 1,2 | oui | 0 [0 ; 0] | −0,018 | 12/12 | 12/12 | 12/12 |
| mêlée 0,8 + 0,2 uniforme | oui | 0 [0 ; 0] | −0,011 | 12/12 | 12/12 | 12/12 |
| variante σ = 0,05 | oui | 0,0003 [0 ; 0,0031] | −0,001 | 12/12 | 12/12 | 12/12 |
| variante σ = 0,1 | oui | 0,0012 [0,0002 ; 0,0047] | −0,002 | 12/12 | 12/12 | 12/12 |
| variante σ = 0,2 | oui | 0,0099 [0,0012 ; 0,078] | −0,015 | 4/12 | 6/12 | 10/12 |
| variante σ = 0,3 | oui | 0,0146 [0,003 ; 0,046] | −0,038 | 1/12 | 3/12 | 8/12 |
| ajout d'un effet faible | non | 0,028 [0,023 ; 0,034] | +0,023 | 12/12 | 12/12 | 12/12 |
| ajout d'un effet moyen | non | 0,061 [0,048 ; 0,079] | +0,061 | 12/12 | 12/12 | 12/12 |
| distincte (une moyenne échangée) | non | 0,109 [0,096 ; 0,128] | +0,009 | 12/12 | 12/12 | 12/12 |
| distincte (une forte en moins) | non | 0,107 [0,078 ; 0,160] | −0,161 | 12/12 | 12/12 | 12/12 |

Les variantes à σ ≥ 0,2 qui restent séparées sont de **moins bonnes** lois (−0,015 et −0,038 nat) : les garder à part ne coûte
qu'un groupe. Génération synthétique de 24 cartes (trois idées × six variantes à σ = 0,15, plus six cartes au hasard) : à
ε = 0,01, 11,75 groupes en moyenne, **99,3 % de groupes purs** (une seule idée), 2,1 idées sur 3 coupées en plusieurs groupes
(la liaison complète préfère couper que mêler) ; à ε = 0,02, 9,8 groupes, 97,5 % purs. Effet sur e-BH (archive {K1}, n = 200,
m = 40) : **15,4 cartes retenues par carte et 4,75 idées distinctes ; 7,3 groupes retenus et 4,67 idées** ; élagage par
domination : 4,25 et 2,5. Variantes « à la v67 » (`sorties-v1/variantes-v67-v1.stdout`) : huit cartes écrites par programme
dans le monde S-V1 (L* arrondie, bruitée, en `si_sinon` sur z0, par sous-population, tempérée ; z1 seul ; un découpage par
morceaux sur z1) → **3 groupes** à ε = 0,01, 0,02 et 0,05 : les six formes de L* ensemble (distances ≤ 0,009), « z1 seul »
(0,343 nat au-delà de K1 contre 0,468, distance 0,033 à 0,054) et le découpage (0,284 nat, distance ≥ 0,134) à part.
Essais (`essais_monde_riche_v1.py`, `essais_complements_synthese_v1.py`) : copies regroupées (artefact), lois distinctes et
lois emboîtées non regroupées (cas sain), chaîne refusée par la liaison complète, e-valeur de groupe = moyenne, e-BH par groupe
qui ne compte pas les copies, différence rare séparée par la lecture par strate, médoïde indépendant de l'ordre d'entrée.

### 3.7 Garde neuve (liste d'arrêt)

**Garde 25 (regroupement)** : cas sain — groupes et médoïdes recalculés par la lecture égaux à ceux du relevé ; e-valeurs de
groupe égales à la moyenne de celles des membres ; un seul représentant par groupe, le médoïde, testé et retenu. Artefacts — deux représentants d'un même
groupe retenus, un membre servi aux proposeurs, groupes dépendant de l'ordre des fournisseurs (permutation des fournisseurs →
mêmes groupes), une loi plantée dans un groupe → arrêt, code 3, incident consigné.

### 3.8 Confrontation au rang 2 de la synthèse du collisionneur

| point | synthèse (non contre-lue) | cette conception | statut |
|---|---|---|---|
| distance | prédictive, grille publique, maximum par strate, diamètre en log-rapport, lien complet, départage par empreinte | prédictive **au sens du nul** (projection sur le nul v8 de l'autre loi, pas une simple divergence), grille publique de 2 000 instances, maximum par strate (192), borne au pire monde rapportée, lien complet, départage par empreinte | convergent (strates ajoutées après lecture) |
| quand | temps 1 : après le test de mort, juge inchangé, sœurs réinjectées ; temps 2 (avant le juge) seulement avec une preuve écrite ; divergence ouverte (confiance 0,55 pour « après ») | **avant le juge** : ta décision demande les « comparaisons multiples comptées par groupe » (consigne, point 3), ce que le temps 1 ne fait pas (les copies se portent encore l'une l'autre dans e-BH : 15,4 retenues par carte contre 7,3 groupes, `doublons-w12-v1.json`) ; preuve écrite au §3.3 ; réinjection gardée comme mesure | **divergence** : à trancher par le contre-lecteur et par toi (Q-8) |
| représentant | jamais par la plus grande valeur e ; médoïde ou empreinte, avant les données | médoïde avant les données | convergent (changé après lecture) |
| e-valeur des sœurs | temps 2 : e = 0 pour les sœurs, m inchangé | moyenne des e-valeurs des membres (toutes les cartes jugées) | deux formes valides ; la moyenne garde la preuve d'une sœur meilleure que le médoïde, au prix de log(taille du groupe) au pire |
| seuils | deux seuils (juge, oracle), le plus strict | ε et ε_strat fixés sur des mondes de développement, sans juge ni oracle | divergence mineure : un seuil tiré du refus du juge mesure la proximité au juge, non la redondance (objection d'E en [E-T2], rapportée par la synthèse) |

## 4. Mesure de la diversité des idées retenues

### 4.1 Définitions

- **D1, par programme, sans oracle, descriptive** (`diversite_programme`), calculée **après** la sélection scellée de chaque
  génération, jamais servie, jamais optimisée, sur les cartes proposées, promues et retenues et sur l'archive : nombre de
  **groupes** (étape A) ; **nombre effectif de Hellinger** N_eff = k²/‖K‖²_F, K_ij = E_x Σ_y √(p_i p_j) (semi-défini positif ; 1
  pour k lois égales ; `n_effectif_hellinger`, synthèse section 2) ; **signature de traits** de chaque loi (sensibilité à chaque
  trait et à la sous-population : E_x KL(p(x) ‖ p(x avec ce trait retiré au hasard)), `signature_traits`) ; nombre de
  **supports distincts** (ensembles de traits de sensibilité ≥ 0,005 nat) ; **traits couverts** ; **entropie** de la signature
  agrégée ; distance moyenne entre paires.
- **D2, mesure principale, par l'oracle, lu une seule fois après la course** (convergente avec la section 2 de la synthèse) :
  nombre de **composantes du monde certifiées détectables** (C8) **couvertes** par au moins une loi, chacune comptée une fois,
  **additionnelles à l'archive** du début de la génération (`complements_synthese_v1.couverture`), mesuré à trois étages :
  **propositions brutes** (toutes les cartes rendues qui s'évaluent : c'est la mesure des proposeurs, N-058), **représentants**
  (après regroupement), **retenues** (après juge et test de mort) ; les écarts entre étages sont les pertes de la chaîne. Une loi
  couvre la composante i si Δ_i = gain(loi | W) − gain(loi | W₋ᵢ) ≥ max(0,005 ; 0,75·I_i) (`Oracle.attribution`) — critère sur
  les prédictions, invariant à la syntaxe ; la synthèse rapporte la chute à celle de la loi plantée elle-même, je la rapporte à
  I_i (même rôle ; à fixer au préenregistrement). Stratifiée par classe et par étiquette de C8 ; composantes « proches du
  seuil » rapportées à part ; gain de l'**enveloppe** de l'archive par génération (progrès) ; par fournisseur : composantes
  couvertes par ses propositions brutes, avec le coût.
- **Validation de l'attribution** (`sorties-v1/attribution-w12-v1.json`, `816a7477…`, 21:23:02 → 21:23:21) : sur 144 lois synthétiques (mondes restreints à un sous-ensemble connu d'effets, coefficients bruités, σ = 0,15) dans 12 mondes MR-1, l'ensemble des effets captés est **exactement** retrouvé pour 127 lois sur 144 (0,88 ; Wilson [0,82 ; 0,93]) ; aucune erreur sur les effets forts (129 sur 129) ni moyens (128 sur 128) ; sur les faibles, 174 retrouvés, 12 manqués, 5 attribués à tort. D2 est donc fiable pour les fortes et moyennes, approchée pour les faibles (dit au rapport).

### 4.2 Coût

Programme seul : de l'ordre de la seconde à la minute de processeur par génération (2 000 instances de référence ; 276 paires
pour 24 cartes) ; oracle : quelques minutes après la course. Aucun appel.

### 4.3 Ce qu'elle ne doit pas piloter

- **La composition des proposeurs** : jugée sur l'oracle et le coût seuls (N-058) ; D1 dérive des verdicts (cartes promues et
  retenues) et ne peut pas servir à choisir ou pondérer un proposeur ; D2 peut être **rapportée** par fournisseur comme
  information, la décision de composition restant à un texte neuf et à Lazar.
- **La sélection** : aucune prime de nouveauté dans le juge ni dans la retenue (la diversité serait alors une cible à
  tromper) ; **les consignes des proposeurs** pendant la course (rien de D1 ni de D2 n'est servi) ; **le nombre de générations**.
- Une course qui voudrait **agir** sur la diversité (consignes diversifiantes, proposeurs à rôles, nouveauté dans la sélection)
  est un dessin neuf : c'est la place de la synthèse du collisionneur (§5.4).

## 5. Proposeurs

### 5.1 Composition proposée

| rôle | modèle | crédits | remarque |
|---|---|---|---|
| proposeur | Claude Fable 5.2 (`claude-fable-5-2`) | Claude | moins chère que 5.1 (8 / 40 contre 10 / 50, plan des crédits §1) ; le choix de version est à toi (Q-7) |
| proposeur | Claude Opus 5.5 (`claude-opus-5-5`) | Claude | |
| proposeur | Argon (`gemini-4-argon`) | hors crédits | prix supposé 10 / 50 |
| proposeur | Astra (`gpt-6-astra`) | hors crédits | identifiant « rapporté, à confirmer », prix supposé 10 / 50 ; « si retenu » (R-2444) |
| proposeur (si son compte est rechargé) | Kimi (`kimi-k3.1-pro`) | hors crédits | redevenu possible : aucune famille n'est exclue du fait de l'auteur du monde (R-2461) ; compte suspendu le 11 novembre (R-2389) ; Q-7 |
| expérimentateur des tests de mort | Opus 5.5 | Claude | crédits qui expirent ; Kimi possible (le moins cher, éprouvé en v67) s'il est rechargé ; Q-2 |
| vérificateur | Argon | hors crédits | autre famille que l'expérimentateur (garde 9) |
| auteur du monde | **programme** (générateur à graine scellée, §2) | — | aucune famille de modèles |

Six cartes par proposeur et par génération (24 cartes ; 30 avec Kimi), comme la v67 ; un appel par proposeur et par génération. Aucun juge
d'idées à modèle : le juge reste mécanique.

### 5.2 Isolement et témoins par test

- **Proposeurs** : chaque appel est une session neuve sans historique, par le relais de son fournisseur ; la **réponse brute**
  de l'interface (corps entier, avant toute extraction), le texte servi et son empreinte, l'en-tête du modèle servi, l'usage
  (Kimi `prompt_tokens`/`completion_tokens` ; Argon `entree`/`sortie` tels que le relevé v67 les porte ; Claude
  `input_tokens`/`output_tokens` ; Astra : à fixer) sont écrits dans `sessions-proposeurs/<monde>/<génération>/<proposeur>/`
  et scellés **avant** l'extraction des cartes. **Garde 26** : dossier vide ou réponse brute absente → arrêt, code 3 (réserve
  R-2 (a) de la v67) ; cas sain et artefact.
- **Tests de mort** : pour **chaque** exécution, un **témoin d'isolement** versé : description de la sonde (`bwrap`, version,
  options `--unshare-all --unshare-net`, profil `--seccomp` et son empreinte), identité dans le bac (64097, sortie de `id`), fichier
  témoin écrit dans le bac et relu sur l'hôte (propriétaire, empreinte), journal de `bwrap`, code de sortie ; scellé à côté de
  `gains.csv`. **Garde 27** : témoin absent ou incohérent → le test est « non concluant » et la course s'arrête (code 3)
  (réserve R-2 (b)).
- **Comptes** : le relevé compte, par fournisseur, appels, jetons et dollars, rapprochés du journal de chaque relais (réserve
  R-6) ; « sans usage » compté à part.

**Les sept réserves du verdict v67 (R-2441) et leur réponse dans ce dessin** : R-1 (touches de la recherche de la loi
plantée tues) → toutes rapportées, relues à la main (K-9, §2.3) ; R-2 (réponses brutes et témoins de `bwrap` absents) → gardes
26 et 27 (ci-dessus) ; R-3 (`arbre_modifie` sans explication) → le manifeste nomme chaque fichier non suivi (copie du texte
scellé) ; R-4 (une carte de moins) → m reste une borne, le relevé compte les cartes rendues par fournisseur ; R-5 (génération
2 sans contenu, retenues proches d'un même constat) → monde riche (§1) et regroupement (§3) ; R-6 (jetons d'Argon) → champs
`entree` et `sortie` lus (K-9) ; R-7 (égalité à l'octet de la lecture) → la lecture écrit l'heure et le chemin à part de son
corps empreinté.

### 5.3 Ce que la lecture rapporte par fournisseur (N-058)

Cartes proposées, refusées au gardien, groupes auxquels il contribue, représentants promus, retenus, vraies et fausses
découvertes (oracle, v60 et enveloppe), effets captés (D2), coût. **Aucun classement par verdicts**, aucune décision de
composition dans la course.

### 5.4 Synthèse du collisionneur sur la diversité des idées : ce qui est repris, ce qui diverge

La synthèse (`4f99077b…`, non contre-lue) est arrivée pendant ce travail ; elle est traitée comme une entrée.

- **Rang 1 (monde riche calibré, leurres)** — repris : composantes **certifiées détectables** (C8, étiquette ≥ 0,8), **traits
  leurres** (au moins 2 distracteurs, sensibilité nulle vérifiée par C3), mondes témoins à une composante et à vérité dans le
  nul (banc, §1.8), mondes répartis **développement / calibration / test scellés** (§1.8), nombres de composantes **tirés
  privément par monde** (§1.2), et, depuis ton mot R-2461, le **monde écrit par programme** (§2). Écart qui reste : la synthèse
  veut chaque composante ≥ 80 % détectable ; ta décision R-2443 demande des effets « du fort au proche du seuil » : je garde des
  faibles détectables 10 à 90 % en moyenne, **étiquetés** et comptés à part, pour que « idée manquée » ne se confonde pas avec
  « effet hors de portée du juge ».
- **Rang 2 (regroupement)** : §3.8.
- **Rang 3 (portefeuille de missions servies aux proposeurs, contre témoins à coût égal)** — **non repris** dans cette course :
  la synthèse le place après un duel ; il changerait les consignes des proposeurs (à geler avant le tirage des mondes, §2.5) et
  demanderait ses témoins (même catalogue sans partage, tirages répétés du même modèle). **Place réservée** dans le
  préenregistrement : une section « Diversification », vide par défaut.
- **Rang 4 (garde certifiée en absolu, extension bornée du nul)** — rejoint Q-4 ; la sonde hors classe H1 et le classement des
  fausses découvertes par forme en sont la part mesurée ici.
- **Rang 5 (allocation entre proposeurs sur l'oracle et le coût)** — convergent avec N-058 et le §5.3 : **rapportée** par
  fournisseur (D2 sur propositions brutes, coût), **aucune allocation pendant la course** ; une règle d'allocation est un texte
  neuf, après la course.
- **Rejets de la synthèse, tous tenus ici** : aucune prime numérique de nouveauté (§4.3), aucun quota de formes, aucun masquage
  de l'archive, aucun représentant choisi par la plus grande valeur e (§3.4).
- **Ordre proposé par la synthèse** (banc de métrologie, puis pilote A/A des proposeurs, puis duel « le monde offre-t-il, les
  proposeurs prennent-ils ? », puis seulement la course à plusieurs générations) : **divergence partielle**. Le banc de
  métrologie est repris comme **préalable sans dépense** (§1.8). Le pilote A/A et le duel ajoutent une étape payante avant la
  course que tu as acceptée (R-2442) ; je propose de lire « le monde offre-t-il » par C8 et « les proposeurs prennent-ils » par
  D2 sur les propositions brutes de la génération 1, dans la course même. Question Q-8.

## 6. Devis

Script `outils-v1/devis_multi_generations_v1.py`, sortie `sorties-v1/devis-multi-generations-v1.json` (`07162b53ad019f4ac3c2a19486c14cd6f6397fc6be931b17f69313fe1e999466` ; script `15256924…`). Tout est
**estimé** sauf les prix cités (et ceux-ci sont « à vérifier » au moment du GO).

### 6.1 (a) Génération des mondes

**Par programme (R-2461) : aucun appel de modèle, calcul seul** (≈ 1 à 2 minutes de processeur par monde vérifié, C8
compris : `sorties-v1/generateur-v1-heures.txt`). Le devis d'écriture par Kimi est **sans objet** ; ses chiffres restent dans
`devis-multi-generations-v1.json` (champ `monde_par_kimi`), où un appel de `kimi-k3.1-pro` au gabarit d'un appel de proposeur
vaut ≈ 0,36 USD attendus, 1,32 au pire (prix 2 / 10 USD par million, `LISEZMOI-relais-kimi-v4.md` l. 57-58, `e5d6c5ce…`) :
c'est aussi le coût d'**un appel de Kimi proposeur** s'il entre dans la course (Q-7).

### 6.2 (b) Course à plusieurs générations (ordre de grandeur)

Hypothèses : 4 proposeurs (Kimi en cinquième : + 0,36 USD attendus et + 2 USD au pire par génération et par monde, plafond de
session), 1 appel chacun par génération (central : Opus ≈ 0,80, Fable 5.2 ≈ 1,60, Argon ≈ 0,25 d'après la v67,
Astra ≈ 1,00 ; pire cas = plafond de session de 2 USD par appel, garde proposée) ; tests de mort par génération : central 15
(≈ 6 représentants et ≈ 9 vraies plantées et T-ELIM), pire 33 (24 représentants et 9) ; par test : expérimentateur central 2
tours, pire 12 tours bornés à 0,80 USD (devis v66 §3.4), vérificateur Argon 0,06 / 0,10 ; **les fausses et copies promues ne
sont pas testées** (brèche lue à la promotion ; change le dessin de la v66, qui les testait). Machine : course v67 ≈ 2 heures
≈ 0,12 EUR ; ≈ 0,15 USD par génération et par monde (estimé), plafond 10.

Expérimentateur Opus 5.5 (recommandé, Q-2), en USD, « central / pire cas » :

| mondes × générations | Claude (crédits) | Argon | Astra | total des modèles | machine, central (plafond) |
|---|---|---|---|---|---|
| 1 × 3 | 13,68 / 91,20 | 3,45 / 15,90 | 3,00 / 6,00 | 20,13 / 113,10 | 0,45 (10) |
| 2 × 3 | 27,36 / 182,40 | 6,90 / 31,80 | 6,00 / 12,00 | 40,26 / 226,20 | 0,90 (10) |
| 3 × 3 | 41,04 / 273,60 | 10,35 / 47,70 | 9,00 / 18,00 | 60,39 / 339,30 | 1,35 (10) |
| 2 × 4 | 36,48 / 243,20 | 9,20 / 42,40 | 8,00 / 16,00 | 53,68 / 301,60 | 1,20 (10) |

Variantes à 2 × 3 : expérimentateur **Kimi** : Claude 14,40 / 24,00, Kimi 3,60 / 158,40 (compte à recharger), total 30,90 / 226,20 ;
expérimentateur **Argon** : Argon 39,30 / 190,20, Claude 14,40 / 24,00. Le pire cas est dominé par les tests de mort (24
représentants promus à chaque génération, 12 tours chacun) ; la v67 a fait 14 tests à 2 tours (verdict v67 §4.4). Un plafond
plus bas que le pire cas ferait d'un dépassement un arrêt « non jugeable » ; la v66 avait choisi un plafond au-dessus du pire
cas (devis v66 §5, mot de Lazar du 2 novembre cité) : même choix proposé ici.

### 6.3 Lignes de GO proposées (à présenter à Lazar ; aucune n'est inscrite)

Montants pour **2 mondes × 3 générations** (option (b) de Q-1) ; entre crochets, 1 monde et 3 mondes. Plafonds = pire cas
arrondi au-dessus (§6.2) ; plafond de chaque relais ou clé égal à sa part. **Aucune ligne pour la génération des mondes**
(programme, calcul seul).

| ligne proposée | texte | plafond | échéance |
|---|---|---|---|
| GO-β1 (course, crédits de Claude) | **Course de l'organisme à plusieurs générations, part sur crédits de Claude** : proposeurs Fable 5.2 et Opus 5.5, expérimentateur Opus 5.5 ; 2 mondes × 3 générations ; plafond de session 2 USD par appel de proposeur, 0,80 USD par test de mort ; conditions toutes exigées : préenregistrement neuf contre-lu et scellé, code v68 contre-lu (regroupement, réponses brutes, témoins par test), mondes vérifiés et scellés, banc de métrologie fait ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 185 USD sur crédits [95 ; 275] | 2026-11-30 (et avant la fin de cycle des comptes) |
| GO-β2 (course, hors crédits) | **même course, part hors crédits** : Argon proposeur et vérificateur 32, Astra proposeur 12 (identifiant et prix confirmés avant l'appel), machine jetable à `bwrap` 10, validée par l'essai à blanc au vrai bac avant tout appel payant | 54 USD [32 ; 76] | 2026-11-30 |

Si Q-2 (b) (Kimi expérimentateur) : GO-β1 tombe à 24 USD [12 ; 36] et une ligne Kimi de 159 USD [80 ; 238] s'ajoute (compte
rechargé). Si Kimi est aussi proposeur (Q-7) : + 12 USD [6 ; 18] sur la ligne Kimi (2 USD par appel au pire). Aucune de ces
lignes n'est inscrite : seul ton mot le fait.

## 7. Questions ouvertes pour Lazar

Format : décision ; enjeu ; options (avantage, inconvénient) ; recommandation et confiance. Aucune n'a de défaut sous
48 heures dans cette conception : ce sont des nœuds (dépense, modèle, revendication) que seul ton mot tranche.

**Q-1 — Nombre de mondes (et de générations).**
- *Enjeu* : la « sensibilité aux effets faibles » (R-2443) se mesure à deux niveaux : la puissance du juge sur chaque effet
  d'un monde (sans agent, par graines : C8 avant la course, rejeux après) et ce que trouvent les proposeurs, qui varie d'un
  monde à l'autre ; chaque monde ajoute une course entière (coût × M).
- *Options* : **(a) 1 monde × 3 générations**, sensibilité par graines seulement — avantage : ≈ 20 USD attendus ;
  inconvénient : aucune mesure de la dispersion entre mondes, un monde « facile » ou « dur » décide de tout. **(b) 2 mondes ×
  3 générations** — avantage : première mesure de dispersion, réplication de l'issue de la chaîne ; inconvénient : ≈ 40
  USD attendus. **(c) 3 mondes × 3 générations** — avantage : dispersion estimée ; inconvénient : ≈ 60 USD attendus, pire
  cas ≈ 339.
- *Recommandation* : **(b) 2 mondes × 3 générations**, plus la sensibilité par graines de chaque monde (C8 et rejeux, sans dépense) ; confiance ≈ 0,55. Les proposeurs synthétiques épuisent un monde de 7 composantes en 2 générations : 4 générations ne se justifient pas sur ce monde (`generations-w12-g3-n400-v1.json`).

**Q-2 — Expérimentateur des tests de mort.**
- *Enjeu* : depuis R-2461, aucune famille n'est exclue du fait de l'auteur du monde ; l'expérimentateur voit la tranche et la loi
  gelée, le verdict est calculé par l'orchestrateur sur le fichier brut, avec contre-calcul ; le choix pèse sur le coût et sur
  la disponibilité.
- *Options* : **(a) Opus 5.5** (crédits de Claude), vérificateur Argon — avantage : crédits qui expirent, compte disponible ;
  inconvénient : jamais éprouvé dans ce rôle en course réelle (≈ 0,20 USD attendus par test, estimé). **(b) Kimi** — avantage :
  le moins cher (≈ 0,10 par test, devis v66), éprouvé en v67 (28 appels, 14 tests) ; inconvénient : compte suspendu, à recharger.
  **(c) Argon**, vérificateur Opus — avantage : disponible ; inconvénient : ≈ 0,42 USD par test (estimé), cinq fois Kimi.
- *Recommandation* : **(a)**, confiance ≈ 0,6 ; (b) si le compte de Kimi est rechargé avant le préenregistrement.

**Q-3 — Origine du secret qui tire les mondes de test.**
- *Enjeu* : « lois inconnues de toute famille de modèles » repose sur un secret tiré après le scellement ; qui le tire décide
  de qui pourrait, en principe, connaître les mondes.
- *Options* : **(a) machine** (`secrets.token_bytes` sur la machine privée qui génère, engagé par son empreinte avant le tirage,
  révélé après le verdict) — avantage : rien à faire de ta part ; inconvénient : une session de la famille Claude lance le
  programme (elle n'imprime que des empreintes). **(b) phrase de toi**, jamais écrite au dépôt, seule son empreinte inscrite —
  avantage : aucune session ne la connaît ; inconvénient : une étape de plus, un secret humain moins uniforme. **(c) les deux
  combinés** (sha256 du secret machine et de ta phrase) — avantage : ni la session ni toi seul ne fixez les mondes ;
  inconvénient : les deux étapes.
- *Recommandation* : **(c)**, confiance ≈ 0,6.

**Q-4 — Nul du juge pour la course : v8 ou v9.**
- *Enjeu* : dans un monde riche à structure par morceaux, les proposeurs écriront des `si_sinon` ; les recombinaisons par
  morceaux de lois d'archive sont hors de la classe couverte du nul v8 (brèche d'A1-v3) ; le nul v9 les couvre mais sa
  validation a rendu « puissance perdue » (audit `9086a420…`).
- *Options* : **(a) nul v8** (comme la v67) avec l'oracle d'enveloppe et le classement des fausses découvertes par forme —
  avantage : code et validation existants, puissance connue ; inconvénient : la classe non couverte reste une portée.
  **(b) nul v9** — avantage : ferme la recombinaison par morceaux ; inconvénient : perte de puissance mesurée, code à brancher,
  et une vraie découverte par morceaux peut être refusée.
- *Recommandation* : **(a)**, confiance ≈ 0,6 ; la sonde hors classe H1 mesure le trou dans ce monde.

**Q-5 — Tirages frais par carte : 200, 400 ou 800.**
- *Enjeu* : la puissance aux effets proches du seuil contre les promotions de lois réelles mais sous g₀ (que l'oracle compte
  comme fausses découvertes).
- *Options* : **(a) 200** (comme la v67) — avantage : le juge gelé tel quel ; inconvénient : point de 50 % vers 0,045 nat, les
  effets « proches du seuil » presque jamais promus (0,17 à 0,02-0,03 nat). **(b) 400** — avantage : point de 50 % sur g₀ ;
  inconvénient : un tiers des lois réelles sous g₀ (0,01-0,02 nat) promues, comptées fausses découvertes par l'oracle. **(c)
  800** — avantage : faibles presque toujours trouvés ; inconvénient : le juge promeut l'essentiel des lois sous g₀ (0,81),
  l'oracle et le juge divergent ; une marge minimale (règle « delta0 » de `selection_pari.evaluer`, 2·δ₀ = g₀) les
  réaccorderait, au prix d'un changement de règle.
- *Recommandation* : **(b) 400**, confiance ≈ 0,6 (`detection-w12-r40-v1.json`, juge simplifié : à refaire au banc de métrologie avec le code v68).

**Q-6 — Mondes refusés par le vérificateur : retirage automatique ou arrêt.**
- *Enjeu* : un tirage peut tomber hors des exigences (classes, détectabilité C8) ; retirer, c'est choisir des mondes
  « conformes » (biais voulu, à dire) ; arrêter, c'est un délai.
- *Options* : **(a) retirage automatique**, au plus 8 tirages par monde, nombre de refus et contrôles en cause rapportés —
  avantage : aucun délai ; inconvénient : sélection des mondes par le vérificateur (dite au rapport). **(b) un seul tirage**,
  refus = arrêt et nouvelle graine sur ton mot — avantage : aucune sélection cachée ; inconvénient : délai.
- *Recommandation* : **(a)**, confiance ≈ 0,7 (banc du générateur : 1 tirage refusé pour 12 mondes, `banc-generateur-w12-v1.json`).

**Q-7 — Version de Fable, présence d'Astra et de Kimi.**
- *Enjeu* : coût et diversité des proposeurs ; changer de modèle demande ton GO ; Kimi redevient possible (R-2461).
- *Options* : **(a) Fable 5.2 et Astra** — avantage : quatre familles de proposeurs (deux de Claude), Fable 5.2 moins chère ;
  inconvénient : identifiant et prix d'Astra à confirmer (`GET /v1/models`). **(b) Fable 5.1 et Astra** — avantage : la
  version nommée par N-052 (pour la contre-lecture) ; inconvénient : plus chère. **(c) sans Astra** (18 cartes par génération)
  — avantage : moins de pièces ; inconvénient : moins de diversité de fournisseurs.
- *Recommandation* : **(a)**, confiance ≈ 0,6 ; **et Kimi en cinquième proposeur** si son compte est rechargé (une famille de
  plus, ≈ 0,36 USD attendus par appel), confiance ≈ 0,55. La composition reste jugée sur l'oracle et le coût (N-058).

**Q-8 — Regroupement avant le juge ou après le test de mort ; ordre des étapes.**
- *Enjeu* : la synthèse du collisionneur (non contre-lue) préfère, à confiance 0,55, regrouper **après** le test de mort sans
  toucher au juge, et placer un pilote A/A et un duel avant la course ; cette conception regroupe **avant** le juge (multiplicité
  comptée par groupe, preuve au §3.3) et lit l'offre du monde (C8) et la prise des proposeurs (D2 brute) dans la course.
- *Options* : **(a) avant le juge, course directe après le banc de métrologie** — avantage : ta demande « comparaisons
  multiples comptées par groupe » tenue, moins de tests de mort (coût) ; inconvénient : touche au juge (code v68 et preuve à
  contre-lire). **(b) après le test de mort (temps 1 de la synthèse)** — avantage : juge v67 inchangé, sœurs réinjectées ;
  inconvénient : les copies se portent encore l'une l'autre dans e-BH, plus de tests payés. **(c) (a) précédé du pilote A/A et
  du duel de la synthèse** — avantage : sépare « le monde n'offre pas » de « les proposeurs ne prennent pas » avant de payer
  plusieurs générations ; inconvénient : une étape payante et du délai en plus.
- *Recommandation* : **(a)**, confiance ≈ 0,6.

## 8. Limites et réserves de cette conception

- **Juge simplifié** : modèle du nul v8 écrit d'après la copie v52b, étalonné sur la v67 (V3 595 contre 617, V4 489 contre 501 sur 1 000) ; l'urne écartée par
  inférence ; tout chiffre de puissance est à refaire avec le code gelé dans le préenregistrement.
- **Proposeurs synthétiques** (`generations`) : modèle arbitraire (probabilités de trouver un effet 0,5 / 0,25 / 0,1 selon sa
  classe, 0,9 de garder un effet connu) ; ses chiffres disent l'effet relatif du regroupement et l'ordre de grandeur de la
  dispersion entre mondes, pas ce que feront Claude, Argon et Astra.
- **Générateur écrit par un modèle de la famille Claude** (moi) ; les lois sont tirées d'un secret après le scellement, et le
  générateur v68 sera contre-lu par un autre modèle ; la famille (sortes d'effets, classes) est publique par la grammaire
  servie et par ce document ; deux régularités du prototype à retirer (§2.1).
- **Code gelé non lu** : les points « à vérifier » du §1.3 (constantes `DIM`, `TIRAGES`, instants de lecture, bibliothèque du
  juge) restent des inférences.
- Rien ici n'est une prédiction de préenregistrement : le préenregistrement neuf fixera critères, seuils et portée (R1), et sera
  contre-lu (R2).
