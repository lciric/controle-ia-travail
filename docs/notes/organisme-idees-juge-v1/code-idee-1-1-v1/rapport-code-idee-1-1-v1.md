# Rapport du développeur — code de l'idée 1.1 (préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md`, `3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`), version 1

- Auteur : développeur neuf, sous-agent de la session mère ; je n'ai écrit ni le texte, ni la preuve, ni leurs contre-lectures, ni le code de l'idée 1.2.
- Date (UTC) : 2026-11-15, de 22:20 à 22:58 ; dépôt sur `main`, tête `845b962c` ; aucun commit, aucune poussée, aucun appel réseau, aucun appel payant.
- **Pas lancés** : le jeu, l'étape 0 en vraie grandeur et la lecture. Je n'ai lu aucun résultat de jeu. Rien n'a été écrit sous `diag/`, `runs/` ou `donnees/`. Les essais tournent sur des racines d'essai, toutes distinctes de l'empreinte du texte.
- Contrôles faits en développement, sur des cas jouets et hors du dépôt : rejeu **partiel** des essais d'origine du v9 depuis la vue assemblée (classes `DescriptionPublique`, `MembresNulV9`, `GrainesEtPreenregistrement` : 11 essais, 11 passent ; ce n'est pas le préalable, qui reste à passer en entier) ; banc de mutations avec 2 répétitions pour la mutation du certificat ; répétition miniature à 2 processus.

## 1. Fichiers neufs (scellés, compagnon `.sha256`)

Aucun fichier existant n'a été modifié (R12).

| fichier | sha256 |
|---|---|
| `src/controle_ia/organisme_idees_juge/vue_v9_v1.py` | `ff2db3d68c012d2d1c0c6641a910a3b16ad2342f2228c7ee6163191833aeadb3` |
| `src/controle_ia/organisme_idees_juge/nul_limite_v1.py` | `f36cb5b20a9fd75452bbf51494ac7f11beca2bc9bca42f84c774b8f49f8c954a` |
| `src/controle_ia/organisme_idees_juge/morceaux_par_coupe_v1.py` | `d32aead32404ba5f589f9ccfa6ab8deb4393038f4b4922b6c8eb2cca3a48bb4b` |
| `src/controle_ia/organisme_idees_juge/projection_commun_v1.py` | `1f4ada977b6cdb96378f3c913df0119bcf6fc333981217ecbbb3583b38f2ca54` |
| `src/controle_ia/organisme_idees_juge/projection_methodes_v1.py` | `54e5fbb241751a5e375dd810cafbd784ccc35d8d6b5859cb90f2700fd4172afa` |
| `src/controle_ia/organisme_idees_juge/attaque_projection_extrait_v1.py` | `a68aabf266a46de3766cedd8fde6dde723306441fddb2892d36e9b48309f34f8` |
| `src/controle_ia/organisme_idees_juge/projection_bras_v1.py` | `b7ac9c80fc1c333572b74d16e105a2e8523c1c02b2d9775b63dc9c33d19ea9e1` |
| `src/controle_ia/organisme_idees_juge/banc_idee_1_1_v1.py` | `fe3046bc90d23c98cefb70cbd40aa57242edb0ef6d4a8d1502cabc669f7e29a3` |
| `src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v1.py` | `28573a11c2121b43e0a121bda2252b72844a9427f6be3477aa78577e7b8d2eb1` |
| `src/controle_ia/organisme_idees_juge/mutations_idee_1_1_v1.py` | `c5dbb92114f5a6c2746ac4149dc88ccfc842279896e4086765feca223dbd9ea3` |
| `src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v1.py` | `f50680565e0e4ef56d735a017cc11c279bf834d0cc9412d97f8bead53b406607` |
| `src/controle_ia/organisme_idees_juge/execution_idee_1_1_v1.py` | `39820dd6c8598ab0398d5179aad208574a05a83c17f905a8e0e18bfad65f1d11` |
| `scripts/jouer_idee_1_1_v1.py` | `884fef7ef61a708864806ebc46834f07dc69a3432c8833d140eae248a7c7cb75` |
| `scripts/lire_idee_1_1_v1.py` | `952b257927d8213eea97e2a97fafb63eb33aac501735618ac9afd955f63c8d2f` |
| `scripts/etape0_idee_1_1_v1.py` | `40d3a6d0270f4b04271de2da298017bd4ebad42cb4939b5152661aff5a182388` |
| `tests/test_organisme_idees_juge_idee_1_1_projection_v1.py` | `21640d651d949a5271b482221c422c003c01a5bc63523e2625092f2b857e98c4` |
| `tests/test_organisme_idees_juge_idee_1_1_gardes_v1.py` | `8820da51932fb7d54ac35c10fe4101da832acf1487525e9ed26c8a3fa5c681df` |
| `tests/test_organisme_idees_juge_idee_1_1_banc_v1.py` | `256d70da71c527fc3ccff7afe126a0b7d74879e798715bca00063a432c5e0c29` |
| `tests/test_organisme_idees_juge_idee_1_1_lecture_v1.py` | `a6c774d66f7d032e3017b9df6e2cdc07efbdd1b16538239281e8e9b3ebfdf231` |
| `tests/test_organisme_idees_juge_idee_1_1_execution_v1.py` | `56ed5d6fff5c59bf1655dd7c0548d3fa4917b802928e52360a345cc1f43a4e07` |
| `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v1/differentiel-nul-limite-v1.diff` | `1334b735460257edff63b01e01a4e144acf243681bea75e63e9645ac9221ab6e` |
| `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v1/differentiel-morceaux-par-coupe-v1.diff` | `4944e35dac74d509b0bd5aecc7d209deaaba409cef9e64d4fe1bb5b759dc2519` |
| `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v1/differentiel-projection-scindee-v1.diff` | `de82c82e3a2492b5c76807d422273449c85e5c9844027754485fae7e14098e4e` |

Rôle des fichiers :
- `vue_v9_v1` vérifie la copie `a41b7b5` par empreinte et charge `pole.nul_v9` au-dessus de `94bfd92`. Il porte aussi la condition (a) (16 noms) et assemble la vue hors du dépôt.
- `nul_limite_v1` sert La et Ld : c'est une copie de `nul_v9.py` avec les quatre changements déclarés, rien d'autre (différentiel `differentiel-nul-limite-v1.diff`).
- `morceaux_par_coupe_v1` sert J9-Dc : un seul changement, le nom de la fonction et deux champs rendus en plus.
- Copies octet pour octet du code de la course :
  - `projection_commun_v1` : fichier entier, empreinte `1f4ada97…`, égale ;
  - `projection_methodes_v1` et `attaque_projection_extrait_v1` : corps de fonctions recopiés par analyse syntaxique, égalité éprouvée par essai.
- `projection_bras_v1` : forme scindée de la projection, sans issue reçue, plus la garde d'accès et la garde P4.
- `banc_idee_1_1_v1` : les lignes, les bras et les gardes.
- `lecture_idee_1_1_v1` : la lecture gelée.
- `mutations_idee_1_1_v1` : le banc de mutations.
- `etape0_idee_1_1_v1` : l'étape 0.
- `execution_idee_1_1_v1` : le jeu par processus, la reprise et l'addendum.
- Les trois scripts et les cinq fichiers d'essais.

## 2. Essais

**117 essais, tous passés**, en 120 s sur un processus (`OMP_NUM_THREADS=1`, `nice -n 10`). La collecte de toute la suite du dépôt donne 6 629 essais et n'est pas perturbée. Répartition :

| fichier | essais |
|---|---|
| projection | 22 |
| gardes | 30 |
| banc | 41 (dont 30 constructions de ligne) |
| lecture | 16 |
| exécution | 8 |

Le banc de mutations passe en entier dans les essais : **17 mutations, toutes tuées pour la raison attendue, 17 cas sains passés**.

## 3. Liste d'arrêt : correspondance texte → code (cas sain et artefact dans `tests/…_gardes_v1.py` sauf mention)

| condition du texte | code | essai sain / artefact |
|---|---|---|
| préalable 1 ou 2 non levé | `etape0.bloquants` ; `prealable_2` ; `classer_rejeu` ; `execution.lire_addendum` refuse une étape 0 qui porte des bloquants | `test_prealable_2_…`, `test_bloquants_…`, `test_rejeu_classement_…`, `test_addendum_…` |
| `nul_v9.py` ≠ `7ae450df…` ; module `94bfd92` non conforme | `vue_v9_v1.verifier_copie_v9` ; `juge_v1.verifier_copie` (déjà éprouvé en 1.2) | `test_copie_nul_v9_empreinte_fausse_refusee` |
| fichier gelé ≠ addendum ; essai échoue ; mutation survit | `lire_addendum` (`execution_v1.verifier_addendum`) ; le lanceur rejoue les essais et les mutations avant le jeu | `test_addendum_sain_et_artefacts` (fichier absent, empreinte fausse) ; mutations : `test_banc_de_mutations_…` |
| essai E0, E9, EP ou ED manqué | `etape0.essai_E0/E9/EP/ED` → `bloquants` | `test_essais_d_egalite_en_miniature` (sain) ; `test_bloquants_…` (artefact) |
| issue fraîche tirée avant le gel | `Repetition.tirer` exige l'état « gelée » | `test_issue_fraiche_avant_le_gel_refusee` ; mutation « issues tirées avant le gel » |
| … lue par la fonction qui bâtit un engagement | `construire_engagement` est refusé après la création du flux ; elle ne reçoit aucune issue | `test_engagement_bati_apres_le_flux_refuse` |
| … issue du bloc b reçue par la projection ou le certificat du bloc b | `projeter` n'a aucun argument d'issue ; `FluxFrais.passe(b)` exige exactement b blocs tirés ; une projection sans mémoire après la création du flux est refusée | `test_flux_frais_garde_d_acces_sous_gel`, `test_projection_d_une_carte_sans_memoire_apres_le_flux_refusee` ; mutations « projection sur les issues du bloc », « projection sous gel recevant une issue du bloc courant » |
| exceptions déclarées (gel : issues des blocs < b, empreinte avant le tirage du bloc b ; J9-P-nu sur les lignes H seules) | `_projeter_sous_gel` ; `exiger_garde("nu", ligne_h)` | `test_journal_empreinte_avant_creation_du_flux_et_gel_par_bloc` (issues reçues 0, 25, …, 175) ; `test_garde_p4_…` (« nu » hors H refusé) |
| loi de carte : exception ou valeur non finie | `proba_carte` traduit une division par zéro en `GardeArret` ; `probas_finies` ; contrôle du lissage par `verifier_moyenne_glissante` | `test_loi_de_carte_exception_ou_non_finie` |
| carte qui lit l'historique sans forme de la garde P4 | `exiger_garde` ; `lit_historique` | `test_carte_qui_lit_l_historique_sans_forme_de_garde`, `test_garde_p4_deux_formes_…` |
| engagement avec `fractions` | `construire_engagement` et `gardes_d_evaluation` | `test_engagement_avec_fractions_refuse` |
| certificat non calculé, non fini, ou < 1 − 10⁻⁹ | `exiger_certificats` (dans `projeter`) | `test_garde_certificat` (4 cas) |
| exception dans une évaluation ; log W non fini | `_resume` et les contrôles de finitude ; `execution` consigne `arret.json`, qui interdit la reprise et la lecture | `test_log_w_non_fini_arrete`, `test_jeu_miniature_…` (arrêt → reprise interdite), `test_lecture_avant_scellement_refusee` |
| monotonie violée | `verifier_monotonie_et_nichage` (J9, La, Ld ≤ J8 + 10⁻⁶) | `test_monotonie_et_nichage` |
| nichage violé (les deux formes) | idem, avec g = plus grand écart résiduel des membres par morceaux du bras | idem (3 artefacts) |
| domination violée | `verifier_domination` ; règle pure `regle_j9d` | `test_domination` ; mutation « J9-D sans la réunion » |
| > 1 % d'écarts résiduels > 2·10⁻³ : rapporté | les écarts sont enregistrés par répétition ; la part est calculée par `lecture.audit` ; aucun arrêt | essai de lecture synthétique |
| chronométrage absent ; D > 32 h après réductions | `regle_de_reduction` ; `lire_addendum` (bloc programme exigé) | `test_regle_de_reduction_…`, `test_addendum_…` (« sans programme ») |
| réduction hors de la règle, ou décidée après une lecture | `actifs_pour` (1 à 5 dans l'ordre, entières) ; `lire_addendum` rejoue la règle sur le fichier d'étape 0 ; la reprise refuse d'autres réductions | `test_reductions_dans_l_ordre_seulement`, `test_addendum_…` (« reduction ») |
| durée murale > 48 h | `GardeDuree`, comptée depuis le premier départ (`depart.json`), vérifiée à chaque répétition | `test_duree_murale_48_h`, `test_duree_depassee_dans_une_tache` |
| lecture avant scellement | `charger_sortie` : `sortie.json` et chaque tranche vérifiés ; les 1 000 répétitions sont exigées | `test_lecture_avant_scellement_refusee`, `test_jeu_miniature_…` |
| dépense, réseau, modèle | `installer_garde_reseau` (lanceurs et étape 0) | `test_appel_reseau_interdit` |

Exigences du texte couvertes en plus de la liste d'arrêt :
- **Garde P4, deux formes.**
  - Refus : `types_de_la_loi` contre `TYPES_LISANT_L_HISTORIQUE`. La carte H7, hors grammaire, est tenue pour une carte qui lit l'historique.
  - Gel : `carte_gelee_bloc` appelle `proba` avec l'historique tronqué, jamais le `Cache` (lemme 4). Sous gel, le numérateur de W^reste est la carte gelée.
  - Pour une carte sans mémoire, le code vérifie à chaque répétition que la loi au gel est égale au numérateur du juge à 10⁻¹² près. C'est l'essai sain des trois formes qui coïncident.
- **Journal empreinté avant le tirage du bloc.** Sans mémoire : les huit empreintes sont dans l'enregistrement avant la création du générateur des issues (essai par espion). Sous gel : une empreinte par bloc, avant le tirage de ce bloc.
- **Mêmes issues pour tous les bras.** Un seul flux par répétition, en huit appels `random(25)` sur toutes les lignes. Chaque bras reçoit un dictionnaire lié à son empreinte. Des issues différentes arrêtent le jeu. Les issues ne dépendent pas des bras joués (`test_memes_issues_quels_que_soient_les_bras`).
- **Égalité avec le code du juge.** Les richesses de J8, J9, La, Ld et du jumeau, arrondies à 6 décimales, sont égales à `evaluer_v2`, `evaluer_v9` et `nul_limite.evaluer_v9`. La forme scindée de la projection est égale à `_blocs_projection` et à `m3_toutes_coupures` (écart observé 0,0).

## 4. Étape 0 (à lancer par la mère)

La commande lance tout le reste : préalable 1, avec le rejeu complet des essais d'origine dans une vue hors du dépôt, interpréteur fils `-I -B`, dossier courant et dossier temporaire dans la vue ; préalable 2 ; E0, E9, EP, ED ; mutations et cas sains ; H7 et Hn sur 200 répétitions chacune ; chronométrage sur 20 répétitions × 30 lignes ; règle de réduction.

```
cd /home/user/controle-ia-travail && .venv/bin/python -I -B scripts/etape0_idee_1_1_v1.py --travail /tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/etape0-travail-v1 --processus 3
```

Ce que fait la commande :
- Elle écrit le fichier scellé `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v1/etape0-v1/etape0-idee-1-1-v1.json`. Il contient des comptes, des temps, les clés (97, k) et les empreintes des fichiers gelés.
- Elle imprime le bloc programme à recopier dans l'addendum : processus, réductions, D, chemin et empreinte du fichier d'étape 0.
- Les lignes « sha256  chemin » de l'addendum s'obtiennent par `scripts/etape0_idee_1_1_v1.py --lister-empreintes`.
- Code de sortie : 0 si le jeu est permis, 2 si un bloquant est inscrit.

**Durée estimée : environ 1 heure sur un processus** (de 1 h à 1 h 30 si la machine est chargée). L'essentiel vient du chronométrage : 600 répétitions à environ 3 s, soit 30 min. Le reste se répartit ainsi : E9 et ED environ 8 min ; H7 et Hn environ 8 min ; mutations environ 4 min ; EP environ 1 min ; E0 environ 0,5 min ; rejeu du v9 de l'ordre de quelques minutes, non mesuré en entier.

**Durée attendue du jeu, d'après mes mesures jouets (non opposables)** : de 1,2 à 4 s par répétition, environ 3,3 s en moyenne, soit environ 9 à 10 h sur trois processus. Aucune réduction ne serait nécessaire. Le jeu s'écrirait sur environ 200 Mo ; il reste 8,4 Go libres.

Lancement du jeu, une fois l'addendum scellé et l'arbre propre : `python -I -B scripts/jouer_idee_1_1_v1.py --addendum CHEMIN`. En cas d'interruption sans arrêt consigné : `--reprendre RUN_ID`.

## 5. Écarts et questions pour la mère (lecture la plus stricte codée ; un écart au texte est réservé à Lazar)

1. **Forme scindée de `_blocs_projection`.** Le texte dit que l'optimiseur est « repris octet pour octet ». La garde d'accès et le gel par bloc interdisent pourtant qu'un même appel reçoive les issues. J'ai donc recopié `_blocs_projection` à l'identique, comme référence, et je l'emploie à travers une forme scindée (`projeter` sans issue, puis `valeurs_e`) dont l'égalité est éprouvée (0,0 ; EP à 10⁻⁹). Faut-il compter cette forme scindée comme un écart ?
2. **J9-Dc « sans coût de plus ».** Le texte dit aussi que le jumeau est « évalué par le code du v9 ». J'ai gardé le v9 pour le jumeau, et J9-Dc fait un second appel au solveur, qui coûte environ 1 à 3 s par répétition et est chronométré dans le groupe « jumeau ». Remplacer l'appel du v9 par la copie, dont la valeur est égale bit pour bit, supprimerait ce coût, mais l'engagement jumeau ne serait plus évalué par le code du v9 seul. À trancher.
3. **Richesses calculées fonction par fonction.** Elles sont calculées par les fonctions du v9 et du juge, dans l'ordre de `evaluer_sur_issues`, sans arrondi, au lieu de lire `evaluer_v9` dont la trajectoire est arrondie à 10⁻⁶. Les gardes de `evaluer_v9` sont rejouées. Les membres communs sont partagés entre les bras, après une vérification d'égalité. L'égalité avec les évaluations officielles est éprouvée par essai, et dans E9 sur deux répétitions de chaque ligne. Est-ce acceptable comme « évaluation par `evaluer_v9` » ?
4. **Lectures de texte.**
   - Ordre des lignes V : par type, puis par dose croissante.
   - Tirages d'entraînement : les uniformes sont tirés avant le plan, et l'issue est lue une fois le plan connu, parce que le monde de Q8 dépend du plan.
   - E0 : l'archive A0 = {S1, S2} sert au nul seulement ; le monde Q1 reste construit sur S1 à S4.
   - Quantité fatale de J9-D : le membre qui contient la copie est fixé par la table `MEMBRE_DE_LA_COPIE`. Q9a correspond à `archive:S1`, Q9b à la famille linéaire.
   - La-P reprend l'optimiseur de J9-P (départ chaud et 150 pas ; « comme J9-P »), et non les 300 pas à froid de `m2b`.
   - Coût du « processus retenu » : celui de la famille qui réalise le minimum à t = 200.
   - Strate sans membres log-linéaires : recalculée à partir des pièces communes, sans relancer le solveur.
   - A2 est lu à t = 200 seulement.
5. **Comptes non écrits par le texte.**
   - E9 et ED : 2 répétitions de chacune des 29 lignes jugeables.
   - EP : 50 mondes de `essai_projection_cas_v1.construire`, avec les cas T01 à T12 en cycle. Le texte dit « mondes de `essai_projection_commun_v1.py` », mais c'est `cas` qui bâtit les mondes.
   - Mutation « certificat retiré, 3 pas » : 30 répétitions de chacune des lignes Q8, Q1 et Q2. Elle est tuée par au moins une promotion. Cas sain : aucune promotion sur les copies Q1 et Q2 ; Q8 est seulement rapporté.
   - Mutation « W^reste oublié » : son détecteur est une carte log-linéaire de S1 bâtie pour la mutation, hors du banc.
6. **Hn sous gel.** J'ai codé la lecture la plus stricte : le jeu est bloqué si le terme sur toutes les familles **ou** la famille linéaire seule atteint 3 promotions ou plus sur 200.
7. **Route « à défaut ».** Dans la vue assemblée, les 7 essais de `GrainesEtPreenregistrement` passent (rejeu partiel en développement). La réécriture prévue par le texte pourrait donc être sans objet. Aucun essai réécrit n'est fourni (`ESSAIS_REECRITS` est vide) : si l'un d'eux échoue au rejeu officiel, le jeu est bloqué.
8. **Prédiction P12.** Le chiffre « Hn environ 0,10 » est marqué non évaluable dans `predictions`, ce qui retire cette partie du drapeau « toutes vraies ».
9. **Écart résiduel.** La part « > 1 % des évaluations avec un écart résiduel > 2·10⁻³ » est comptée sur J9, par répétition. Les écarts de La et de Ld sont enregistrés mais n'entrent pas dans ce compte.

## 6. Ce qui n'est pas éprouvé

- L'étape 0 entière : rejeu complet du v9, critères de H7 et de Hn à 200 répétitions, chronométrage réel. La valeur de D sous trois processus, quand la machine est chargée.
- Le jeu en vraie grandeur. La reprise après un vrai arrêt de machine (elle n'est éprouvée que par une tranche pré-écrite).
- La lecture sur des données réelles : elle n'est éprouvée que sur des données synthétiques, et le script `lire_idee_1_1_v1.py` n'a jamais été lancé sur une sortie.
- La contre-lecture du code par un sous-agent neuf, avec les trois différentiels de ce dossier.
