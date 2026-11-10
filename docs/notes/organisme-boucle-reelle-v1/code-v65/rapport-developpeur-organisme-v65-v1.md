# Rapport du développeur — code v65 de l'organisme d'idéation (plus petite course réelle de la boucle complète) — v1

- **Développeur** : Claude Opus 5.5 (`claude-opus-5-5`), session fille `session_01QPDgKhUpjGAMFhKSKNcVEA` de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy`. Développeur neuf : je n'ai écrit aucune pièce de l'organisme ni du programme de contrôle,
  ni le brouillon 1 ; je n'ai pas lu le travail annulé du développeur précédent (R-1758, R-1767), y compris la branche publique
  `prep/organisme-v65-boucle-reelle` (commit `c2c3979`), que je n'ai ni extraite ni ouverte.
- **Heures** (temps universel, `date -u`, 10 novembre 2026) : début 10:23:18 ; code et essais de 10:36 à 10:57 ; rapport écrit
  de 10:58 à 11:05 (heure de fin relevée au rendu).
- **Consigne** : `docs/notes/organisme-boucle-reelle-v1/consigne-developpeur-organisme-v65-v1.md`, sha256
  `2dc207e7bbee89393560f0e95b407782a0ec2c5be70e5440ef42cd4c759eee50` (égale à son compagnon) ; interdits communs v2
  (`1ee3b370…`, vérifiée) ; changements de la mère (commit permis, livraison sur `prep/organisme-v65-v1`).
- **Dépense** : aucune. Aucun appel de modèle, aucune machine, aucune clé ni variable d'environnement lue.

## 1. Base

- Dépôt public cloné en lecture (`/home/user/ideation-organism`). Le commit `94bfd92` existe (branche `claude/new-session-7qxayx`).
- `main` du dépôt public a avancé (trois commits depuis la base commune `faff48b` : nul v9, attaque de Goodhart v5 et son texte
  scellé, état du 8 novembre). **Base inchangée pour la v65** : `git diff 94bfd92 origin/main` ne touche aucun des fichiers de
  base (`pole/tour_ferme_v64.py`, `demonstrations/tour_ferme_v64.py`, `pole/nul_v8.py`, `pole/lecture_tour_ferme_v63.py`,
  `pole/boucle_fermee_v59.py`) ; seul `README.md` diffère (3 lignes d'état). Je suis donc parti de `94bfd92`, comme le dit la consigne.
- Arbre : `/home/user/wt-organisme-v65`, branche locale `prep/organisme-v65-boucle-reelle-v2`, commit
  `cef5ea60ea22a9bb46a2b0be761972672a4c2ede` (un seul commit, dix fichiers neufs, aucun fichier existant modifié). Jamais poussé.
- Interpréteur : `/home/user/controle-ia-travail/.venv/bin/python -I -B` (Python 3.13.18, numpy 2.4.6, scipy 1.17.1,
  pytest 9.1.1), les mêmes versions que l'essai à blanc v1.

## 2. Ce que fait la v65, pièce par pièce

Fichiers neufs (R12 ; la v64 et tout l'existant sont inchangés et réutilisés tels quels) : cœur `pole/boucle_reelle_v65.py`,
lecture `pole/lecture_boucle_reelle_v65.py`, lanceur `demonstrations/boucle_reelle_v65.py`, programme de lecture
`demonstrations/lire_boucle_reelle_v65.py`, outil de préparation `demonstrations/preparer_boucle_reelle_v65.py`, configuration
`exemples/configuration-boucle-reelle-v5.json`, jeu à blanc `exemples/jeu-plante-boucle-reelle-v65.md`, essais
`essais/test_boucle_reelle_v65.py`, `essais/test_lecture_boucle_reelle_v65.py`, banc `essais/mutations_boucle_reelle_v65.py`.

| pièce | ce que fait le code | garde |
|---|---|---|
| **M1** héritage de départ | `ecrire_heritage_depart` scelle `heritage-depart-v65.json` (génération 0, archive {K1}, K1 « connue, déclarée ») ; `lire_heritage_depart` ne l'accepte que si son empreinte est celle du plan gelé du texte (`heritage_depart_sha256`), lue avant le contenu avec le sceau (`boucle_fermee_v59.lire_scelle_verifie`), si l'archive est exactement {K1} du jeu planté (JSON canonique), K1 marquée « connue, déclarée », aucune vraie ni instrument dedans ; sinon `HeritageDepartRefuse`, code 2, aucun repli. Il rend un héritage au format v59 : la génération 1 sert la vue {K1} et juge avec {K1}. | 17 |
| **M2** jeu planté | Bloc `jeu-plante-v65` (JSON entre deux marques) lu à l'octet : empreinte des octets = `jeu_plante_sha256` du plan gelé ; exactement K1, V1 à V4, F1 à F4, T-ELIM, T-MAL ; chaque loi dans la grammaire servie ; **chaque fausse dans la classe couverte du nul v8** (`classe_couverte` : copie d'une loi de l'archive, mélange de lois de l'archive et de lois fixes, loi de l'archive tempérée et inclinée, ou mêlée à une loi aveugle fixe ; par morceaux, produit, composition et loi inconnue refusés) ; sinon `JeuPlanteRefuse`, code 2. Remplace `TEMOINS`. Lois identiques au script de puissance (`lois_du_dessin`, `a2afcdd3…`). | 19 |
| **M3** jugement avec l'archive | `juger_v65` : cartes par `tour_ferme_v64.juger` (inchangé) ; lois plantées par le nul v8 **avec l'archive de leur génération**, hors famille au seuil log(m/α) = log(22/0,05) ; le nombre de membres d'archive de chaque loi plantée doit être celui qu'impose l'archive (`nul_v8.membres_archive_v8` : 4 pour {K1}), sinon `PlanteeSansArchive`, arrêt code 3. L'essai `test_defaut_de_la_v64_reproduit_puis_corrige` montre la v64 promouvoir une fausse de la classe couverte avec 0 membre d'archive, puis la v65 n'en promouvoir aucune (4 membres, log W max ≤ 0). | 18 |
| **M4** bras réel seul, génération 2 | Un seul bras ; tout autre bras → `BrasRefuse`, code 2 ; tout nombre de générations autre que 2 → refus (D2). La génération 2 lit le bilan scellé de la génération 1 par `lire_heritage` (v59), sert la vue {K1} ∪ retenues, juge avec l'archive lue, replante F1 à F4 et une copie renommée des quatre premières retenues par log e, **prises dans l'héritage lu** ; copie d'une carte non retenue ou d'une autre loi → `CopieNonRetenue`, arrêt. Le relevé porte la lecture (empreinte écrite et lue, vue et vue attendue, retenues écrites et lues, copies). Essais : héritage altéré (sélection modifiée après le sceau) → refus `SelectionNonVerifiee`, arrêt, lecture C5 ; héritage lu d'un autre contenu (une retenue ôtée) → vue, archive et membres changés, lecture C4. Arrêt après la génération 2 (sa sélection est scellée puis relue). | 20, 21 |
| **M5** lecture gelée | `lire_criteres` applique C5, C4, C2, C3, C6, C1 dans l'ordre du brouillon (section 8), la première qui s'applique donne l'issue ; sous C5, une fausse ou une copie promue, ou une lecture de sélection en écart, s'écrit aussi « C2 (partielle) » ou « C4 (partielle) ». `audits` : A1 d'office sous C1 (membres d'archive des vraies survivantes, bac réel partout, contre-calcul, log W max des fausses ≤ 0, vue de la génération 2 sans loi plantée), A2 si une fausse est promue (diagnostic, rejeu de 200 tirages par `rejouer_a2`), A3 sous C3, A4 si une copie est promue ou la lecture en écart. L'oracle n'est lu qu'ici, après la course (`mesures_oracle` : P7 par fournisseur ; fausse découverte d'une carte réelle en tête). Aucune moyenne ni médiane sur des jetons. | — |
| **Commandes v6** (M6) | `exemples/configuration-boucle-reelle-v5.json` (sha256 `bff138d8…`) : copie de la v4 (`15b34adf…`) avec `budget.plafond_usd` 40, `--plafond-cumule-usd` 40, et une section `boucle_reelle_v65` qui nomme le GO, les parts (Kimi 33, Argon 7), le plafond de la machine (5) et les commandes v6 avec leurs empreintes, vérifiées sur la branche `outils/commandes-tour-ferme-v1`, commit `12f9e0e3…` (égales à leurs compagnons) : `commande_kimi_v6.py` `889309305aeb37de…`, `commande_argon_v56_nuit_v6.py` `5eae1a0468430e24…`, `registre_depense_cumulee_v1.py` `8ba92066b358ffb8…`. Le lanceur réel refuse (code 2) une commande absente ou d'une autre empreinte, ou une configuration contraire au plan. Rien n'est lancé. | M6 |
| **Gardes de dépense** | Plafond des modèles et parts tenus par `tour_ferme_v64.Compteur` (arrêt au franchissement ; arrêt avant un étage si une part restante est sous le pire cas) ; en plus, avant chaque appel d'un proposeur, la part restante doit couvrir le budget de l'appel (arrêt, aucun appel) ; plan gelé : Kimi + Argon = plafond des modèles, plafond des modèles + machine = montant du GO (45) ; mode réel : GO cité, égal à celui du texte, vérifié au registre (`verifier_go_v56`, montant 45), puis exigé de nouveau par le cœur (`exiger_go`) avant tout appel. | 5, GO |
| **Bac à sable** | Inchangé (`a_blanc_v59.choisir_executeur`) : `bwrap` absent → `BacASableIndisponible`, code 2, aucun repli ; garde 22 neuve en mode réel : `bwrap` ≥ 0.9 lu par `bwrap --version`, utilisateur dédié ≠ 0, puis la sonde. | 3, 22 |

## 3. Essais (dernières lignes exactes)

- Base v64 avant tout code (10:34:06 → 10:35:32) : `169 passed, 2 skipped, 117 subtests passed in 84.69s (0:01:24)` (égal au
  journal de l'essai à blanc v1).
- Suite touchée, finale (`POLE_ESSAI_BAC_REEL_NON_JOUE=1`, `test_boucle_reelle_v65.py`, `test_lecture_boucle_reelle_v65.py`,
  `test_tour_ferme_v64.py`, `test_gardes_tour_ferme_v64.py`, `test_v59_boucle_fermee.py`, `test_v57b_cablage_verdict.py` ;
  10:52:50 → 10:55:40) : **`232 passed, 3 skipped, 160 subtests passed in 170.41s (0:02:50)`**. Les 3 sautés sont les essais du
  vrai bac à sable (deux de la v64, un de la v65), déclarés non joués : `bwrap` absent de cette machine.
- Banc de mutations v65 final (10:52:50 → 10:57:14) : **`38 tuées sur 38 mutations`** (sortie `essai-a-blanc-v65/mutations-v65-final.txt`
  et `.json`). Le banc joue d'abord les essais nommés sur une copie non mutée (ils réussissent), puis chaque mutation dans une copie
  neuve ; une mutation dont le texte d'origine n'est pas trouvé exactement une fois est un défaut du banc, jamais « tuée ».
  Liste : garde 17 (empreinte, K1 altérée, statut, clés), garde 19 (empreinte, classe acceptant tout, mélange avec une loi non
  fixe, composition, jeu incomplet), garde 18, canal de la v64 (plantées sans archive), seuil hors famille, garde 20, D2,
  garde 21 (ordre, exigence), génération 2 jugée sans la sélection lue, GO dans le cœur, part avant l'appel, lecture (C5
  incomplet, C5 masquant C2, ordre C4/C2, C3 sans « survit », C6 sans T-MAL, ordre C3/C6, P6 empreinte, P6 membres, copie promue,
  A1, diagnostic A2, rejeu A2), lanceur (parts, montant du GO, bras du plan, empreinte des commandes v6, version de `bwrap`,
  nom « brouillon », bac factice substitué).
- **Mutation équivalente, dite et hors du banc** : la boucle « aucune vraie ni instrument dans l'héritage » de
  `lire_heritage_depart` est redondante (l'archive doit déjà être exactement {K1} du jeu, et le jeu refuse une vraie égale à K1) ;
  aucun essai ne peut la tuer seule.

## 4. Essai à blanc v65 de bout en bout (journal)

Commande : `bash lancer_essai_a_blanc_v65.sh /home/user/wt-organisme-v65 SORTIES PYTHON` (sha256 `2ffc22d7…`), jouée de 10:51:59 à
10:52:28 ; fournisseurs simulés (doublures du v64, branchées sur le chemin réel), deux générations, **exécuteur factice déclaré
comme tel** (`--bac factice`, et l'audit A1 le dit : « bac_reel_partout » faux). Sorties copiées sous `essai-a-blanc-v65/`.

| étape | commande (depuis `orchestrator/`) | heures | code | issue |
|---|---|---|---|---|
| 1 | `boucle_reelle_v65.py … --a-blanc --graine 20261110 --bac reel` | 10:51:59 | **2** | « BacASableIndisponible : bac réel demandé : bwrap absent de cette machine : refus, aucun repli sur l'exécuteur factice » ; aucun dossier de sortie |
| 2 | même, `--bac factice` | 10:51:59 → 10:52:13 | **0** | relevé `ffd36ec465b35372f122c33c922a846b2d18999a113115d47effc2a17ec651c9` ; 24 cartes, 18 lois plantées, 2 générations |
| 3 | `lire_boucle_reelle_v65.py` sur l'étape 2 | 10:52:13 → 10:52:17 | **0** | **C1**, A1 déclenché d'office ; V1, V2, V4 promues puis survivantes, V3 non promue (mesure P3) ; F1 à F4 refusées dans les deux générations (plus grand log W max −0,17) ; T-ELIM promue puis éliminée ; T-MAL refusée au gardien ; génération 2 : empreinte lue = écrite, vue = {K1} ∪ 11 retenues, 37 membres d'archive partout (= ceux qu'impose l'archive lue), 4 copies toutes refusées ; lecture `56a1347b…` |
| 4 | même que 2, `--scenario-proposeur refus:2` | 10:52:17 → 10:52:20 | **3** | arrêt scellé (refus de modèle servi du proposeur, garde 13) |
| 5 | lecture de l'étape 4 | 10:52:20 → 10:52:25 | **0** | **C5** « non jugeable (arrêt) », rien de partiel à écrire en plus |
| 6 | même que 2, `--cout-simule-usd 0.3 --plafond-kimi-usd 0.5 --plafond-argon-usd 7` | 10:52:25 → 10:52:26 | **3** | « part restante du relais kimi (0.2000 USD) sous le pire cas de l'étage (9.6000 USD) : arrêt avant l'étage » |
| 7 | même que 2, `--bras aleatoire` | 10:52:26 | **2** | `BrasRefuse` (garde 20) |
| 8 | même que 2, `--generations 3` | 10:52:27 | **2** | refus (D2) |
| 9 | `preparer_boucle_reelle_v65.py SORTIES/blocs` | 10:52:27 → 10:52:28 | **0** | blocs du texte, héritage de départ scellé |

**Ce qui casse** : rien dans la chaîne v65. Constats : (a) à graine égale, deux courses à blanc rendent des relevés d'empreintes
différentes (`fe008a12…` à 10:40, `ffd36ec4…` à 10:52) : le relevé porte la durée et des chemins temporaires ; les décisions sont
égales, mais le relevé n'est pas reproductible à l'octet ; (b) les doublures des proposeurs recopient la loi plantée : l'issue C1
à blanc est « trop belle » par construction, A1 le dit, rien n'est montré des vrais agents ; (c) le bac réel n'a pas tourné.

## 5. Bloc qui remplace `<<BLOC-V65>>` du brouillon

Fichier `blocs-v65/blocs-pour-le-texte-v65.md` (sha256 `382e74dd1a3c487b9506a7e7211dbc3b58e580c07e11f620874710a4c3de9725`), à
recopier tel quel dans le texte à sceller : bloc `empreintes-du-code-v65` (96 fichiers : les 92 du bloc gelé v64 et les quatre
fichiers v65 du chemin de course), bloc `plan-gele-v65`, bloc `jeu-plante-v65`. Valeurs du plan : générations 2, six cartes par
proposeur, m 22, bras `reel_seul`, gardien mécanique, plafond des modèles 40 (Kimi 33, Argon 7), machine 5, GO-2026-11-08-02 de
45, durée 72 h, configuration `bff138d8a30c57b898b84c5db49e00a501d15c158009deb12e697b9a13b0e322`, monde
`fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877`, jeu planté
`21b4b0058672deb36a2312370324f2fcc5065576f18f2b69a97eda84f84eb41e`, héritage de départ
`93dcf51715f7a1aa4f313e9e1761c5a375a275d572ffcdb6969fbfaf2fb623c1` (`blocs-v65/heritage-depart-v65.json`, scellé par le code de
l'organisme, déterministe : `preparer_boucle_reelle_v65.py` le réécrit à l'octet).

Commandes exactes de la course (depuis `orchestrator/`, sur la machine à `bwrap`, après le scellement et la contre-lecture) :

```
POLE_ESSAI_BAC_REEL_NON_JOUE= python3 -I -B -m pytest -q -p no:cacheprovider essais/test_boucle_reelle_v65.py essais/test_lecture_boucle_reelle_v65.py essais/test_tour_ferme_v64.py essais/test_gardes_tour_ferme_v64.py essais/test_v59_boucle_fermee.py essais/test_v57b_cablage_verdict.py
python3 -I -B essais/mutations_boucle_reelle_v65.py --processus 4
python3 -I -B demonstrations/boucle_reelle_v65.py SORTIE_ESSAI --a-blanc --graine 20261110 --bac reel --utilisateur-bac 64097
python3 -I -B demonstrations/boucle_reelle_v65.py SORTIE --preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md \
    --heritage-depart CHEMIN/heritage-depart-v65.json --configuration CHEMIN/configuration-boucle-reelle-v5.json \
    --moteur reel --confirmer-moteur-reel --registre-go CHEMIN/registres/go.md --go GO-2026-11-08-02 --bac reel --utilisateur-bac 64097 --verifier-seulement
(puis la même sans --verifier-seulement)
python3 -I -B demonstrations/lire_boucle_reelle_v65.py SORTIE LECTURE.json --releve-sha256 <empreinte du relevé>
```

## 6. Écarts à la consigne (dits)

1. **Nom de branche** : `prep/organisme-v65-boucle-reelle-v2` au lieu de `prep/organisme-v65-boucle-reelle` (R12 : ce nom porte
   déjà, sur le dépôt public, le travail annulé du développeur précédent).
2. **Commit, compagnons `.sha256`** : permis par la mère (la consigne les interdisait) ; un seul commit dans l'arbre de
   l'organisme, jamais poussé ; compagnons dans la livraison seulement (plus celui que le code de l'organisme écrit pour
   `heritage-depart-v65.json`).
3. **Environnement virtuel** : `.venv` du dépôt de travail créé par la routine de `CLAUDE.md` (`pip install -r requirements-cpu.txt`,
   depuis PyPI), absent au départ ; la consigne disait « rien à installer qui touche le réseau ». Mêmes versions que l'essai à blanc v1.
4. **Récupération de la branche des commandes** : `git fetch origin 'refs/heads/outils/commandes-tour-ferme-v1:refs/remotes/origin/outils/commandes-tour-ferme-v1'`
   (refspec explicite, permise) ; commit `12f9e0e3` lu par `git show`, rien d'extrait.
5. **Format des blocs** : le brouillon ne porte V1 à V4, F1 à F4 et les instruments qu'en prose ; j'ai fixé le format du bloc
   `jeu-plante-v65` et du bloc `plan-gele-v65` (aucune loi ni valeur changée : les lois sont celles du script de puissance).
6. **Oracle** : le cœur v65 ne calcule plus l'oracle pendant la course (la v64 le faisait) ; il est lu une fois par la lecture
   gelée, après (brouillon, section 7, point 3).

## 7. Ce qui reste ouvert, et pour la contre-lecture

- **Machine** (M0, garde 22) : rien du vrai bac à sable n'est montré ici ; l'essai `test_sain_bac_reel_essai_a_blanc` et l'essai à
  blanc `--bac reel` sont à jouer sur la machine à `bwrap`. **M7** : numpy 2.5.3 non essayé (le Python du système n'a ni scipy ni
  pytest).
- **Où vit le texte scellé** : le lanceur, comme celui de la v64, n'accepte que `orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md`
  **dans l'arbre de l'organisme**, dépôt public ; le brouillon vit dans le dépôt de travail privé. Décision de la mère : copier le
  texte scellé dans l'arbre de l'organisme (comme les textes du tour fermé), ou une v66 qui accepte un autre dossier.
- **Configuration v5 et commandes v6 (M6)** : la configuration doit être placée à côté de `configuration-tour-ferme-v4.json`
  (ses pièces `pieces/…` y sont), et les commandes v6 versées aux chemins qu'elle nomme (session de dépôt). Le coût de la
  machine (5 USD) n'est pas compté par le code : le GO (45) le couvre, le relevé de la location reste à la session de dépôt.
- **Réutilisation sans modification de la v64** : quelques étiquettes de la v64 restent dans la course (fiches de l'étage marquées
  « tour-ferme-v64 », étape des portes de plafond `tour_ferme_v64` dans `roles_reels`) ; sans effet sur le dessin, dit.
- **Preuve de lecture si aucune carte réelle n'est retenue** : il n'y a alors aucune copie ; la preuve repose sur l'empreinte, la
  vue et les membres d'archive (question ouverte du brouillon, section 15).
- **Pour le contre-lecteur** : la liste « classe couverte » de `classe_couverte` contre la docstring de `nul_v8.py` ; le seuil
  « log W max ≤ 0 aux marges près » de A1 (marge 10⁻⁶) ; le choix « mêlée à une loi aveugle fixe » (`melange_aveugle` seul) admis
  comme couvert ; l'ordre de la lecture ; la reproductibilité à l'octet du relevé (constat a).

## 8. Empreintes des fichiers neufs (commit `cef5ea6`)

| sha256 | fichier (`orchestrator/`) |
|---|---|
| `5d20d9fb4d8bc53ff6c4ffb8f3f2442200c8d51c9075828cd183277cdbe8ff13` | `pole/boucle_reelle_v65.py` |
| `43ef73d7d5170c17378514f6a32c7eac44bbad2f101f1a4ec97f937ddc1d4fb1` | `pole/lecture_boucle_reelle_v65.py` |
| `32175d9d7a51a6ea86b66b20047e6fc90cec8950c779a1402b56002f622f6ad1` | `demonstrations/boucle_reelle_v65.py` |
| `89678ab63c74b87c5c8245ab540cbcc1ce42d5b47dfe421444ff9a4e66929c12` | `demonstrations/lire_boucle_reelle_v65.py` |
| `fd32060cbcebee94a47d9d879fec2bb0716df743074160c2e37786b36b4afef4` | `demonstrations/preparer_boucle_reelle_v65.py` |
| `bff138d8a30c57b898b84c5db49e00a501d15c158009deb12e697b9a13b0e322` | `exemples/configuration-boucle-reelle-v5.json` |
| `e5ec2fa2e10294d5a399102142c0d31d03ee9b4d3264187e81b61076a16c0793` | `exemples/jeu-plante-boucle-reelle-v65.md` |
| `14a91fed2b4e870e6a55710f8a7f563c9067ba85016cb5f63d0321ef9d6b45bd` | `essais/test_boucle_reelle_v65.py` |
| `8903ee1246a5d00df84adc6033b76476aeec7e2c2a212ca0da820e127dc9b1fa` | `essais/test_lecture_boucle_reelle_v65.py` |
| `29c767735406c4e86d516fc074ba05a0002c33a07d97d875ea16c375302d1b9a` | `essais/mutations_boucle_reelle_v65.py` |

Livraison (ce dossier) : paquet git `organisme-v65-boucle-reelle-v2.bundle` (`94bfd92..prep/organisme-v65-boucle-reelle-v2`,
prérequis `94bfd92`, vérifié par `git bundle verify`), patch `organisme-v65-contre-94bfd92.patch` (`git format-patch`), ce
rapport, le script et les sorties de l'essai à blanc, les blocs du texte ; chacun scellé par son compagnon.
