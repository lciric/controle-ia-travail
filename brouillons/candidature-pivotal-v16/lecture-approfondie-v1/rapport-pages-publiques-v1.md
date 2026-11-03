# Rapport — pages publiques de P3 et de la simulation préenregistrée — v1

Rédacteur neuf : je n'ai écrit ni le préenregistrement de P3, ni son verdict, ni la simulation, ni sa lecture. Travail du 3 novembre 2026, de 05:23 à 05:52 UTC (`date -u`). Consigne suivie : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pages-publiques-p3-et-simulation-prompt.md`, lue en entier, puis `CLAUDE.md`.

## Verdict

- Deux pages publiques écrites, en anglais, avec leurs pièces copiées et scellées. Rien n'est commité ni poussé.
- **La simulation qui porte « 31 of 31 » et « 21 à 35 % » est T0.3** (simulation du lemme d'additivité et du théorème négatif, run `20261004-080257-t03`, 4 octobre 2026). Ce n'est pas l'essaim du 1er novembre. Le chiffre est retrouvé exactement dans une sortie scellée.
- « Chirurgie de l'historique » : absente des deux dépôts. Elle relève de l'instance sycophancie, que nous n'avons pas.

## 1. Sources retrouvées

Toutes les empreintes ci-dessous ont été recalculées par `sha256sum` et sont égales à leur compagnon `.sha256`.

### 1.1 P3

| pièce | chemin (dépôt privé) | sha256 | ce que j'y ai lu |
|---|---|---|---|
| verdict v2 (complété, celui qui fait foi) | `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` | `05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751` | l. 5-8 (ligne d'issue) ; l. 10-16 (P3-P1 établie, P3-P3 réfutée, « non détecté à cette puissance ») ; l. 17-20 (aucun critère de G0) ; l. 23-33 (trois réserves de l'addendum 2, forme gelée) ; l. 186, 209, 214 (table gelée, ligne 4 ; les deux jeux lus) ; l. 352, 357-358 (grandeurs des réserves) ; l. 504-536 (ce qu'il établit et n'établit pas) ; l. 541 (aucune réserve bloquante) ; l. 553-554 (les réserves doivent accompagner les conclusions partout où elles seront citées) |
| verdict v1 | `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` | `0c8ecbdf4a95824a91acf8a45d36d3b165f6dc24f889a9fc8633738b9bb71113` | empreinte et contrôle de publication seulement |
| fichiers de travail des verdicts (tar) | `docs/verdicts/verdict-P3-premier-test-i-a-v1-fichiers-de-travail.tar` ; `…-v2-fichiers-de-travail.tar` | `2bfd0ec30c917b93dd392f1d4e37a74f4488060731e927938f87c974ac69775b` ; `81c4e9d0203d72c82033e12550edb5ac0db097d9b5bc6ab4b33a62724966e13c` | empreintes seulement (non ouverts) |
| préenregistrement | `prereg/P3-premier-test-i-a-v1.md` | `d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672` | l. 122-145 (hypothèses ; Llama-3.1-8B-Instruct l. 122) ; l. 153-161 (prédictions) ; l. 222-283 (aire, intervalle, plancher, seuils) ; l. 287-339 (plan, conditions) ; l. 386-397 (puissance écrite) ; l. 423-436 (table gelée, réserves) |
| configuration | `prereg/P3-premier-test-config-v1.json` | `702303e9453f7c4ce8f0cf900f45fc8075b75744eedab0b1652dd8e52d55abde` | empreinte seulement |
| consignes privées | `prereg/P3-consignes-v1.md` | `a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c` | **non ouvertes** ; empreinte seulement |
| premier addendum | `prereg/P3-addendum-lecture-complementaire-v1.md` | `8ff834229444b214f3f4c248ecdbf619a4b7149700825ef39bac2e86a6ff80ac` | contrôle de publication |
| addendum 2 | `prereg/P3-addendum2-audit-verdict-v1.md` | `c91a3b4e600bca029f77fbd8ecea12fe9d9658da26219ddcbf3d95102f02ddb6` | contrôle de publication |
| lecture décisive [L] | `diag/20261020-075740-p3-lecture/lecture-p3.json` | `c221d9552bef0487620a2dd2a360b586735388f8f39a76d35a375de7c4a2009a` | `resultat.issue.ligne` ; `resultat.P3-P1` (`effet` 1,522739…, `bas` 1,246449…, `haut` 1,801176…, `n_taches` 60, `taches_exclues` []) ; `resultat.P3-P3.tromperie-difference_moyennes-c15` (`aire` 0,574833, `bas` 0,531323, `haut` 0,618312, `plancher_quantile` 0,571715) ; `resultat.P3-P3.enjeux-lineaire-c15` (0,524797 ; 0,481286 ; 0,570033 ; 0,535588) ; `resultat.placebo` ; `resultat.audit_R4` (`declenche` faux ; coût seul 0,887754 sur 926 actions) ; `resultat.actions_non_notees` (0 partout) — tout égal au verdict |
| résumé du run [R] | `diag/20261019-230011-p3-reel/resume.json` | `4d6894b309ca138541fec29d07e8541a707c8266295e0dcd2019f9e646d628f6` | `episodes` 240, `actions_notees` 2 400 |
| sorties des addenda | `diag/20261020-075849-addendum-p3/lecture-addendum-p3.json` ; `diag/20261020-220858-addendum2-p3/lecture-addendum2-p3.json` | `6c8335b8023574f72b4ec838db3889f3ce7de94ac84cb9e415e692fcae52e65c` ; `916f453647af00992528a5bb3ede9be3dcc68be9618eff990fffc58a47358c8a` | contrôle de publication ; phrases des réserves dans `resultat.recommandation_au_verdict_R13` |
| autres sorties du run | `diag/20261019-230011-p3-reel/sondes-figees.json` ; `episodes-p3.json` | `fb41812732711c1a2a152fa776c46be5a4c50a72ccdc8fd9b7b7f9edcc37d208` ; `1a96cbf8ac6e10d3315bb20248453836d6ae5570b2312ded2be5ebb67cd14381` | empreintes |
| manifestes | `runs/20261019-230011-p3-reel/` ; `runs/20261020-075740-p3-lecture/` ; `runs/20261020-075849-addendum-p3/` ; `runs/20261020-220858-addendum2-p3/` (`manifeste.json`) | `3f21774c…1685` ; `49e91517…620e` ; `ff045e7e…8b9b` ; `9bc77d2a…8d37` (complètes sur la page) | `cree_le` : 19 oct. 23:00:13 ; 20 oct. 07:57:46 ; 07:58:55 ; 22:09:02 UTC ; `commit` : `97dd829…` (= S), `e03df08…`, `63386e6…`, `af97266…` (= S2) ; `decisif` vrai pour le run et la lecture, faux pour les addenda |
| registre des décisions | `registres/decisions.md` (registre vivant, modifié par une autre session à 05:37 UTC pendant mon travail ; empreinte à 05:50 UTC : `4ac7745a30f428e97cd00d94440a6eafc75f2972d974c719d35dff6e96d039f3`) | — | l. 441 (N-024) ; l. 447 (R-248 : run fini, sondes figées à 23:25:47 UTC) ; l. 455 (R-256 : verdict v1) ; l. 456 (R-257 : « audit d'abord ») ; l. 457 (N-025) ; l. 501 (R-297 : addendum 2 scellé) ; l. 502 (R-298 : passage unique) ; l. 507 (R-303 : verdict v2) ; l. 509 (R-305 : verdict v2 scellé et **GO-2026-10-20-12**, message vers 23:10 UTC le 20 octobre ; P3 clos sur ce verdict) ; lignes vérifiées stables après la modification de 05:37 |
| registre des GO | `registres/go.md` | — | l. 40 : GO-2026-10-20-12, type « décision » |

Commits de scellement (S `97dd829`, `e03df08`, S2 `af97266`) : **non vérifiables dans le clone local**, qui est superficiel (14 commits). La page les donne « tels que les pièces scellées et les manifestes les citent ».

### 1.2 La simulation : T0.3, et non l'essaim

- **Identification.** « 31 of 31 predictions » = T0.3 : 31 prédictions P1.1 à P8.4, toutes « confirmée » (`diag/20261004-080257-t03/lecture.md` l. 7-37 ; recompté dans `lecture.json` : 31 confirmées, 342 cellules statistiques et 544 trajectorielles, toutes conformes). L'essaim (`20261101-222901-essaim`, verdict `brouillons/preuves-mentors-v1/essaim-simulation-v1/verdict-R13-essaim-v1.md`, `0e9007c0dd5fc949b1f6e555d95aab9f469428908daa9baaea89faac6e1d934c`) compte **23** prédictions, et son taux de Ville sous τ = 0,2 vaut 3 966 / 20 000 ≈ 0,198 : il ne porte pas « 21 à 35 % ».
- **Le chiffre, dans la sortie scellée** `diag/20261004-080257-t03/bloc-P8.json` (`9af85122e168279f2c6a6407b136b08dca1d1caf491b23fdc9c5edf372bb7dad`), clé `resultat.reglages[i].alarmes.e_unilat_ville`, sur `R` = 20 000 :
  - `[8]` `1x200_tau0.2` : **4 210** (l. 1048) → 0,2105 ;
  - `[12]` `1x1000_tau0.1` : **4 723** (l. 1569) → 0,2361 ;
  - `[13]` `1x1000_tau0.2` : **7 029** (l. 1699) → 0,3514 ;
  - `[16]` `5x40_equi0.4` : 3 312 (l. 2089) → 0,1656 (« 17 % entre agents ») ;
  - bien spécifiés : 333 (l. 8), 387 (l. 1309), 337 (l. 1829) → 0,017 à 0,019 ;
  - calibrage conforme : `resultat.reglages[i].conforme.alarmes_par_tirage` → 0,04605 à 0,05455 (= `lecture.json`, `resultat.lecture.predictions.P8.4.cellules[].taux`), prédit 0,04995.
- **Note de résultats** `docs/notes/resultats-T0.3-v1.md` (`9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545`), l. 95-107 : table « 0,21 ; 0,35 ; 0,24 ; 0,17 ; 0,066 ; 0,057 » et « 0,046 à 0,055 ». Égale au bloc.
- **Lecture gelée de la garde de G1** : `lecture.md` l. 50 (« dépasse α aux niveaux les plus forts d'effet épisode… »). Audit de symétrie : `lecture.md` l. 39 ; `lecture.json` `resultat.lecture.audit_symetrie` (0,9554 sur 63 ; 0,8526 sur 104 ; non déclenché).
- **Préenregistrement** `prereg/T0.3-simulation-lemme-theoreme-v1.md` (`7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb`) : P8 l. 203-215 ; P8.3 « exploratoire vu », valeurs vues avant scellement 0,214 ; 0,364 ; 0,164 ; 0,067 (l. 212-214) ; transparence l. 394-424 ; hors de portée l. 53-59. Grille `prereg/T0.3-grille-v2.json` (`5609f920…`). Manifeste `runs/20261004-080257-t03/manifeste.json` (`c9bba5e1…`), `cree_le` 2026-10-04 08:02:57 UTC, 3 280 graines `SeedSequence`. Registre : R-024 (l. 33, scellement), R-025 (l. 34, run, « R13 (aucune porte franchie) »).
- **Aucun verdict de lecteur neuf** n'existe pour T0.3 (rien dans `docs/verdicts/`) : l'issue est la lecture gelée appliquée par le code. La page le dit.

### 1.3 « Chirurgie de l'historique »

Absente des deux dépôts (recherche sans `donnees/`) : ni « chirurgie de l'historique », ni « retirer la concession », ni équivalent anglais, hors des brouillons de candidature qui la citent (`brouillons/candidature-pivotal-v16/mentors/mentor-1-ibrahim-v12` à `v18`, `mentor-5-colognese-ward-v11` à `v15`, `source-questions-reponses-mentors-v1.html`). Elle relève de l'instance sycophancie, que nous n'avons pas.

### 1.4 Constats à te signaler

1. **README public, l. 130** : « (a preregistered simulation on adaptive defences, 1 November 2026) ». La simulation de « 31 of 31 » et « 21–35 % » est du **4 octobre** (T0.3) ; celle du 1er novembre est l'essaim (23 prédictions). Si la ligne vise T0.3, sa date est fausse. Je n'y ai pas touché.
2. **« 21 à 35 % » ne vaut qu'aux effets d'épisode les plus forts de la grille** (τ = 0,2 à n₀ = 200 et 1 000 ; τ = 0,1 à n₀ = 1 000). Le même bloc scellé donne 0,034 (τ = 0,05, n₀ = 200 : 676, l. 788), 0,089 (τ = 0,1, n₀ = 200 : 1 773, l. 918) et 0,107 (τ = 0,05, n₀ = 1 000 : 2 146, l. 1439) ; le premier est sous α. La lecture gelée dit elle-même « aux niveaux les plus forts ». J'ai écrit ces trois nombres dans « What this does not show », pas dans le résultat. C'est le seul endroit où la page cite un chiffre absent de la note de résultats ; il vient du bloc scellé, avec ses lignes.
3. **P8.3 était « exploratoire vu »** : les cellules où Ville dépasse α ont été choisies après des explorations qui avaient montré ces valeurs. La page le dit ; la phrase de candidature aussi.
4. **La puissance « about 0.03 at the observed deception-probe shift of 0.27 honest-score SD »** de `brouillons/candidature-pivotal-v14/mentors-v10/mentor-6-jang-feng-v10.md` ne vient pas du verdict. Elle vient de `brouillons/preuves-mentors-v1/p3-borne-v2/` : analyse non décisive, a posteriori, non aveugle, plan sans contre-lecture ; sa vérification dit que « 0,33–0,46 » mélange deux seuils. La page n'en dit rien. La borne scellée du nul est celle de l'addendum 2 : aire minimale détectable 0,6315 et 0,5966.
5. **Le verdict v2 exige que ses trois réserves accompagnent P3-P1 et le nul partout où ils sont cités** (l. 553-554). Les phrases de candidature de la section 5 les portent.

## 2. Contrôle de publication

Fait avant d'écrire, puis sur chaque fichier écrit. Le script de crible est hors des dépôts (`/tmp/crible_v2.py`). Motifs : `donnees` ; chemins `/tmp/`, `/home/`, `/Users/`, `/root` ; courriels ; motifs de clés ; identifiants d'instance ; `GO-2026` ; `USD` ; fragments probables des consignes privées, c'est-à-dire les motifs que le préenregistrement de P3 cherche dans les actions (l. 187-190 : « private note », « three times », « lower case », « another agent »…) ; identifiants arXiv de tâches ; « almost detected », « does not separate ».

| pièce candidate | constat | décision |
|---|---|---|
| verdict v2 et v1 de P3 | 3 chemins sous `donnees/` (pièces [S], [J], [T]) ; 2 chemins de bloc-notes `/tmp/claude-0/…` ; citations ligne à ligne du registre | **non copiés** ; empreintes sur la page ; nombres repris tels quels |
| préenregistrement de P3 | 7 chemins sous `donnees/` ; montants en dollars, identifiants de GO et d'instances ; motifs des consignes privées | **non copié** ; empreinte |
| addendum 2 (texte) | 3 chemins sous `donnees/` | **non copié** ; empreinte |
| sortie de l'addendum 2 | table par tâche : les 60 identifiants arXiv des tâches (fichier des tâches tenu sous `donnees/`) | **non copiée** ; empreinte et nombres des réserves seulement |
| premier addendum (texte) et sa sortie | aucun `donnees/`, aucun motif ; mais le texte cite mot pour mot ta décision N-024 (« Oui, réserves au verdict »), alors que la section 7 du README public dit les décisions verbatim du directeur hors du dépôt ; il n'ajoute aucune réserve | **non copiés** (choix prudent) ; empreintes ; **à toi de dire** s'ils doivent l'être |
| lecture décisive `lecture-p3.json` | nombres, étiquettes et empreintes seulement (77 chaînes, aucune de plus de 90 caractères, aucun identifiant de tâche) | **copiée** |
| T0.3 : préenregistrement, grille, `lecture.md`, `lecture.json`, `bloc-P8.json`, note de résultats | données synthétiques ; aucun motif ; « Lazar » une fois (auteur du programme ; « la décision reste à Lazar ») ; « 57721566 » est une graine, pas un identifiant | **copiés** |

Réserves du contrôle :
- `lecture-p3.json` contient aussi des nombres que les règles gelées ne lisent pas dans cette issue : les huit autres jeux, P3-P4, T1 à T4, dont le drapeau T2 que l'addendum 2 dit « ni lu ni cité ». La page dit qu'ils ne sont pas des résultats et n'en cite aucun. Si tu préfères ne pas les exposer, il suffit de ne pas committer `pieces/lecture-p3.json` : la page tient sans lui.
- Le mot « inflate » / « inflated cost » est le nom du mode (« coût gonflé »), déjà public sur la page R1. La page ne reprend ni « three times », ni « lower case », ni « another agent » : je les ai reformulés.
- Précédent : le dépôt public porte déjà des références `donnees/` dans certaines pièces scellées, et des chemins `/tmp/claude-0/…` (`MANIFEST.md` l. 345). La consigne exclut « toute ref `donnees/` » : je l'ai appliquée strictement. Si tu acceptes les références de chemin, le verdict v2 peut être versé tel quel. Ce serait ta décision (publication).
- Résultat final du crible sur les deux pages : aucun motif, sauf « does not separate », une fois, dans la règle elle-même (« never "does not separate" »).

## 3. Fichiers écrits (tous neufs)

Sous `/home/claude/ideation-organism/resultats/controle-p3-premier-test/` :

| fichier | sha256 |
|---|---|
| `README.md` | `00707c0bc24d29150297c10c4d1932d16d72f148071f89acbc00490dc26b1f0b` |
| `pieces/lecture-p3.json` (copie octet pour octet) | `c221d9552bef0487620a2dd2a360b586735388f8f39a76d35a375de7c4a2009a` |
| `pieces/lecture-p3.json.sha256` (recalculé, égal à l'original par `cmp`) | `23efcb13e15f387f3ccb4afc8f078d0e71f235a1ea1ca94331ad11a639a2c6d0` |

Sous `/home/claude/ideation-organism/resultats/controle-simulation-defenses/` :

| fichier | sha256 |
|---|---|
| `README.md` | `b954958fdcd9866131ec1d182e28adae5cb9cab87e71826d780bcb659c5dd98f` |
| `pieces/T0.3-simulation-lemme-theoreme-v1.md` | `7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb` |
| `pieces/T0.3-simulation-lemme-theoreme-v1.md.sha256` | `c12e87b630eda8bc7fb4bb37fa6a6ed68de516e7775f6fbd1416f9e493a4c289` |
| `pieces/T0.3-grille-v2.json` | `5609f920c0d606a192e92b2c2172416dad740b158940aac1ee049de8b8affe23` |
| `pieces/T0.3-grille-v2.json.sha256` | `ab41b5fe817b4904bb63c5c08734e69be236da40f0bae5e9f92ab42ad2b492e4` |
| `pieces/lecture.md` | `650ef86bef453104784fa7237187aa2d211be3169f25ffa9bba854d0b2f5722d` |
| `pieces/lecture.md.sha256` | `8d13866b16974bc4cdfb6de703c25551ac6c26d10447cd0d6747fc3505f3b5cb` |
| `pieces/lecture.json` | `c5aa62b42feed399e8626e3f681830023dc2dd124663d138e3a0c8170f1a7bbb` |
| `pieces/lecture.json.sha256` | `d337331f6d25254f0478e5f4a0def5815ddf1984f416c3a34802fb9316e94d93` |
| `pieces/bloc-P8.json` | `9af85122e168279f2c6a6407b136b08dca1d1caf491b23fdc9c5edf372bb7dad` |
| `pieces/bloc-P8.json.sha256` | `eb7bc2238efdedc3b49d6f547961bb6414b3e6419830415b6996280d7ff84891` |
| `pieces/resultats-T0.3-v1.md` | `9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545` |
| `pieces/resultats-T0.3-v1.md.sha256` | `ebc05c29445691248ad43cf6bb96ec88ce9f1b3cdacde94dbb235a092356a28a` |

Chaque copie est identique à son original (`cmp`). Chaque compagnon recalculé est égal, octet pour octet, au compagnon d'origine (`cmp`) et passe `sha256sum -c`. Les deux `README.md` n'ont pas de compagnon, comme les pages existantes (`controle-r1-blanche-noire`, `attaque-goodhart-v2`).

Ce rapport : `/home/claude/scratch/pages-publiques/rapport-pages-publiques-v1.md`.

## 4. Lignes proposées pour le README principal (non touché)

Il n'existe pas de tableau intitulé « What has been shown ». L'équivalent est le tableau de la section 4, « Evidence so far » (colonnes What | Result | Reproducible here?). Je propose deux lignes, à placer après la ligne R1 :

```
| **First white-box test on real activations (P3, control programme)** (Llama-3.1-8B-Instruct, 60 tasks, four conditions, 2,400 scored actions; two generic probes against a floor of 200 random probes matched in covariance) | **In (verdict of 20 Oct 2026, published 3 Nov 2026).** The instructed saboteur inflates its declared cost: paired log10 difference 1.5227, 95% interval [1.2464, 1.8012]; the size exceeds the instructed factor of about 3, cause not measured. Neither generic probe clears its floor (lower bounds at 97.5%: deception 0.5313 against a floor quantile of 0.5717, high stakes 0.4813 against 0.5356): "not detected at this power", and the null does not exclude areas below 0.6315 and 0.5966. Preregistered and sealed before the data; verdict by fresh readers; no criterion of the gate G0 pronounced. | No — real model runs, records private; the sealed decisive reading is copied with its seal. Result page: [`resultats/controle-p3-premier-test/`](resultats/controle-p3-premier-test/) |
| **Preregistered simulation of the additivity lemma and the negative theorem (T0.3, control programme)** (synthetic scores; 31 signed predictions, 342 statistical and 544 trajectory cells; one decisive run, 4 Oct 2026) | **In (published 3 Nov 2026).** 31 of 31 predictions confirmed, 0 contrary cell, symmetry audit not triggered; most predictions are instrument checks, so this validates the statistical instruments, not the theorems on real models. Informative: with no attack, Ville's threshold on a one-sided e-process gives 0.21 to 0.35 false alarms under the strongest episode effects of the grid (0.17 under correlation between agents), against 0.017 to 0.019 well specified; a threshold calibrated on 1,000 whole honest episodes holds 0.046 to 0.055 for 0.04995 predicted. The strongest cells were selected after exploratory runs; frozen reading by the code, no fresh-reader verdict. | No — the simulation code is private; the sealed preregistration, grid, reading, block output and results note are copied with their seals. Result page: [`resultats/controle-simulation-defenses/`](resultats/controle-simulation-defenses/) |
```

Et, si la l. 130 vise T0.3, remplacer « (a preregistered simulation on adaptive defences, 1 November 2026) » par « (T0.3, a preregistered simulation of its statistical instruments, 4 October 2026: [result page](resultats/controle-simulation-defenses/)) ». C'est à confirmer par toi : je ne sais pas ce que la ligne visait.

## 5. Phrases exactes pour une réponse de candidature (anglais)

**P3.** Les réserves du verdict sont incluses, comme il l'exige :

> In our first white-box test on real activations (Llama-3.1-8B-Instruct, 60 tasks, 2,400 scored actions; preregistered, verdict by fresh readers), a saboteur privately instructed to inflate a declared cost does so plainly (paired log10 cost difference 1.52, 95% CI [1.25, 1.80], larger than the instructed factor of about 3, cause not measured), yet neither generic probe (deception, high stakes) clears its floor of random probes matched in covariance: not detected at this power, and the null does not exclude AUCs below 0.63 and 0.60 — https://github.com/lciric/ideation-organism/tree/main/resultats/controle-p3-premier-test

**Simulation (T0.3).**

> A preregistered simulation of our statistical instruments on synthetic scores (31 of 31 signed predictions confirmed, most of them instrument checks) found that, with no attack, an e-process at Ville's threshold raises 21–35% false alarms instead of the 5% target under the strongest episode effects of the grid (17% under correlation between agents; those cells were chosen after exploratory runs), whereas a threshold calibrated on 1,000 whole honest episodes holds 4.6–5.5% — https://github.com/lciric/ideation-organism/tree/main/resultats/controle-simulation-defenses

Arrondis tirés des valeurs exactes des pages : 1,5227 → 1,52 ; [1,2464 ; 1,8012] → [1,25 ; 1,80] ; 0,6315 → 0,63 ; 0,5966 → 0,60 ; 0,2105-0,3514 → 21-35 % ; 0,1656 → 17 % ; 0,04605-0,05455 → 4,6-5,5 %. Ne pas écrire « 21–35% under episode effects » sans « the strongest » : la lecture gelée elle-même restreint le dépassement de α aux niveaux les plus forts. Ne jamais écrire « almost detected » ni « does not separate ».

## 6. Ce qui a été respecté, et limites

- Aucun commit, aucune poussée. Aucun fichier existant modifié, dans aucun des deux dépôts. `git status --short`, en lecture seule (`--no-optional-locks`), ne montre côté public que des dossiers non suivis : mes deux dossiers et `banc-tricheurs-v9-validation-v1/`, d'une autre session. Côté privé, il montre deux fichiers non suivis d'une autre session.
- Rien lu sous `donnees/` : toutes les recherches passent par `--exclude-dir=donnees`. `resultats/banc-tricheurs-v9-validation-v1/` n'a été ni listé ni ouvert ; son nom n'apparaît que dans la liste de `resultats/` et dans `git status`.
- Aucun appel réseau ni modèle. `nice -n 10` sur les recherches, copies, calculs et scripts, pas sur chaque `ls` ou `sha256sum` isolé.
- Les deux pages n'ont pas été relues par un sous-agent neuf. Je le recommande avant publication.
- Commits de scellement non vérifiables localement (clone superficiel).
