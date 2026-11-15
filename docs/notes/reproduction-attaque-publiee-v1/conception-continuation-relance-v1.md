# Conception — continuation de la relance du témoin de Bailey au-delà du tour coupé — v1 (brouillon, 15 novembre 2026)

Session `session_016QhUrudziqEQujXt4ofM8u`, branche `claude/compassionate-meitner-d4ryyk`. Mot de Lazar, verbatim :
« prépare la continuation à froid, go ». Ce texte **ne lance rien et ne dépense rien** ; c'est une conception à
contre-lire (R2), puis, si Lazar la retient, la base d'un addendum 7 scellé et d'un code neuf. Aucune note de sonde ni de
juge lue pour l'écrire : seuls le code public (commit `9c1f4b1a…`, arbre `c7cf686c…`, vérifié, lu hors du dépôt, jamais
copié), notre code (`execution_v4`, `instance_v16`, `journaliseur_v3`), le préenregistrement et le diagnostic en lecture
seule (`runs/temoin-bailey-v1-20261111/diagnostic-hetzner-v1-sortie.txt`).

## 1. Pourquoi
La relance (`principal-relance`, K = 72 par la règle du texte, l. 248, sur t = 1 316 s du pilote) sera coupée par la
garde à B − 2 vers le 15 novembre 11:30-11:46Z, à K′ ≈ 34 tours complets : verdict au **régime réduit** (l. 165, 332).
Le régime publié exige K ≥ 71. Un tour dure ≈ 1 h 50 au tour 32, contre 22 min au pilote.

## 2. Ce qu'un tour transmet au suivant (code public)
Boucle `train_attack` (`train_harmful.py`, l. 50-166), pour `at_def_epoch` = e :
1. évaluation « défenseur » (`evaluate_model_and_metric_harmful`, sonde courante) ; au tour 0, ses représentations
   deviennent `TestCachedReps("random-obf", e = −1)` ;
2. sauvegarde de la sonde (`save_probe_path`, fichier `…_ade_e.pkl`, `torch.save` du module entier ; `load_pretrained`
   le relit par `torch.load` : aller-retour exact) ;
3. tour de l'attaquant : si `load_tunable_params_path` désigne un fichier existant pour e, les paramètres sont **chargés
   sans entraînement** (mécanisme public, l. 90-99 ; « if params can be loaded, train attack will only evaluate »,
   l. 216) ; sinon `reinit()` puis 2 époques d'entraînement, et sauvegarde (`…model-params-…_ade_e.pkl`) ;
4. évaluation « attaquant », avec le comportement (génération et juge) ; ses représentations de test rejoignent
   `test_cached_reps` (`attacker-e`) ;
5. si e < K − 1 : `metric.refit(e)` (`obf_reps/metrics/__init__.py`, l. 545-575) : représentations d'entraînement sous
   les paramètres de l'attaquant, ajoutées à `metric.reps_bank`, puis **réentraînement de la sonde sur toute la banque**
   (`CachedReps.combine`, mélangée par `random.shuffle`).

État d'un tour au suivant : la sonde (sauvegardée), les paramètres de l'attaquant du tour (sauvegardés ; l'attaquant
repart de zéro à chaque tour, `reinit_tunable_params: True`), `reps_bank` (en mémoire seulement : « start » + un bloc
par tour), `test_cached_reps` (en mémoire seulement), `params_last_train_epoch` (compteur), et l'état des générateurs
aléatoires (non sauvegardé).

**Cause probable du ralentissement** (hypothèse, non mesurée) : la banque grossit d'un bloc de 1 600 exemples par tour
et la sonde est réentraînée sur toute la banque ; l'évaluation parcourt aussi toutes les `test_cached_reps`. Dates des
fichiers (diagnostic) : entraînement de l'attaquant ≈ 16 min par tour (GPU) ; réentraînement ≈ 1 h 30 au tour 32
(processeur dominant : GPU à 0 %, ≈ 5,8 cœurs). Le coût par tour croît avec e.

## 3. Ce qui survit à la destruction de l'instance
Le transfert prévu ne rapatrie que les journaux (≈ 5 Mo). La sauvegarde du 15 novembre (mot de Lazar « go ») a copié,
en lecture seule, `sondes/` et `params/` de `principal-relance` sur le serveur Hetzner 176187199 (68 fichiers, 34 + 34,
580,5 Mo, empreintes en accord ; listes `runs/temoin-bailey-v1-20261111/sauvegarde-sondes-v2/`), et continue toutes
les 20 min jusqu'à la destruction. Rien d'autre n'est gardé : ni `reps_bank`, ni `test_cached_reps`, ni générateurs.

## 4. Mécanisme proposé : rejeu des tours 0 … e₀ − 1, puis tours neufs e₀ … 71
Une exécution neuve, même modèle, même code public au même commit, même configuration (`zf-iter-100-mlp`, surcharges
de l'écart 1 à 9 inchangées, K = 72), même graine, dossiers neufs, avec un module d'exécution neuf
(`execution_continuation_v1`, sur le modèle d'`execution_v4` : `runpy` du script public, journaliseur substitué), qui
ajoute **seulement** :
- **Paramètres de l'attaquant** : `load_tunable_params_path` pointe vers les paramètres sauvegardés des tours
  0 … e₀ − 1 (mécanisme public ; aucun entraînement de l'attaquant rejoué). Pour e ≥ e₀ aucun fichier n'existe : la
  boucle entraîne normalement.
- **Sonde** : au début de chaque tour rejoué e (e = 1 … e₀), la sonde est **chargée** depuis `…_ade_e.pkl` sauvegardé
  au lieu d'être réentraînée : `metric.refit(e)` est remplacée, pour e < e₀, par sa première moitié publique (calcul
  des représentations sous les paramètres chargés et ajout à `reps_bank`, assertion `len == e + 2` gardée), suivie de
  `load_pretrained(…_ade_{e+1}.pkl)`. Pour e ≥ e₀, `refit` publique inchangée. Le premier réentraînement réel a lieu à
  la fin du tour e₀, sur une banque reconstituée de e₀ + 1 blocs.
- **Sonde initiale** : la construction publique (représentations « start », `fit`) est gardée telle quelle, puis la
  sonde est remplacée par `…_ade_0.pkl` (contrôle : le fichier sauvegardé et la sonde recalculée doivent avoir la même
  empreinte, sinon garde tombée — c'est aussi un contrôle de la graine et du déterminisme).
- **Évaluations des tours rejoués** : exécutées telles quelles (elles reconstituent `test_cached_reps` et
  `random-obf`), journalisées dans un journal **de rejeu** distinct, scellé, jamais lu comme résultat.
- **Garde « rejeu fidèle »** (à préenregistrer) : par programme, sans lecture humaine, égalité, tour par tour
  (0 … e₀ − 1), des notes du journal de rejeu et du journal scellé de la relance (même sonde, mêmes paramètres, mêmes
  entrées ⇒ mêmes notes, aux arrondis de demi-précision près ; tolérance à fixer, ou égalité exacte si le banc est
  déterministe). Seul le booléen et le premier tour en écart sont imprimés. Garde tombée : pas de continuation lue.

Coût du rejeu : par tour, deux évaluations (≈ 8 min au tour 32, dont génération et juge) et un passage du modèle sur les
1 600 exemples d'entraînement, sans entraînement de l'attaquant ni de la sonde : ≈ 10-12 min × 34 ≈ 6-7 h.

## 5. Ce que la continuation ne reproduit pas (à déclarer)
- **Générateurs aléatoires** : à partir du tour e₀, les tirages (réinitialisation et entraînement de l'attaquant,
  mélange de la banque, entraînement de la sonde) diffèrent de ceux d'un run d'un seul tenant. La continuation est un
  run « même état déterministe au tour e₀, tirages neufs ensuite », pas le prolongement exact.
- **Déterminisme du GPU** : les représentations reconstituées peuvent différer au dernier bit si l'instance neuve n'a pas
  la même carte ou les mêmes noyaux ; la garde « rejeu fidèle » le mesure.
- **Deux instances** : la machine change au tour e₀ (durées non comparables entre les deux parties).

## 6. Écarts au préenregistrement (nœud : écart à un texte scellé)
1. Le texte ne prévoit qu'**une seule relance entière** (l. 371) et lit un run coupé après 20 tours comme tronqué, sans
   relance (l. 338, 372) : la continuation est un troisième mode d'exécution, non prévu.
2. B = 75 (GO-2026-11-10-10) est épuisé : dépense hors enveloppe (voir § 7) ; le passage à un B supérieur est « hors
   enveloppe, retour à Lazar » dans la ligne de GO.
3. La règle du nombre de tours (l. 248) a fixé K = 72 sur un t de pilote faux d'un facteur ≈ 5 ; la continuation garde
   K = 72 (régime publié si K′ final ≥ 71).
4. Lecture : P1 sur les 72 tours assemblés (34 de la relance, 38 de la continuation), P2 sur 71 valeurs, dernier tiers
   = tours 48-71, tous dans la continuation ; critères, seuils et audit de symétrie inchangés. À trancher : la
   continuation porte-t-elle seule un verdict, ou seulement l'assemblage ? Lecture proposée : verdict de la relance à
   K′ ≈ 34 (régime réduit) rendu d'abord, comme prévu ; puis verdict de l'assemblage au régime publié, avec la
   discontinuité des tirages au tour e₀ écrite à côté ; les deux rapportés.
5. Code neuf (`execution_continuation_v1`, conduite et lanceur neufs, assembleur neuf, `lecture` neuve ou adaptée) :
   contre-lecture et essais comme pour le code v17-v20.

## 7. Devis (estimation à refaire sur `sortie-durees-v3.jsonl` après le transfert)
- Hypothèse : coût d'un tour ≈ a + b·e, avec a ≈ 0,27 h (attaquant et évaluations) et b ≈ 0,047 h par tour
  (réentraînement, ≈ 1,5 h au tour 32) ; la moyenne observée (32 tours en ≈ 44 h, 1,4 h par tour) est ≈ 1,4 fois ce
  modèle : fourchette large.
- Tours 34 … 71 : 105 à 140 h ; rejeu : 6 à 7 h ; mise en place et transfert : ≈ 1 h ; total ≈ 112 à 148 h.
- À 1,17 USD/h (A100 SXM4 de la relance ; taux relevé à la création) : **≈ 130 à 175 USD**, plus le stockage. Au
  taux de 1,6 USD/h d'autres offres A100 : jusqu'à ≈ 240 USD. Durée : 5 à 6 jours, fin vers le 21-22 novembre si lancé
  le 16 ; dans l'échéance du GO (30 novembre).
- À comparer : run neuf de 72 tours, ≈ 140 à 190 h, ≈ 165 à 225 USD à 1,17 USD/h, sans discontinuité.

## 8. Risques
- Le rejeu exige que `load_tunable_params_path` accepte notre schéma de noms (`convert_path`) : à vérifier sur le code,
  et sur un essai à blanc à 2 tours avant tout lancement.
- La banque reconstituée occupe la mémoire vive de l'hôte (≈ 34 × 1 600 représentations) comme dans le run d'origine.
- Une garde « rejeu fidèle » qui tombe pour une raison de déterminisme du GPU rendrait la continuation non lisible : il
  faut fixer d'avance la tolérance et ce qu'on fait alors (pas de continuation lue ; run neuf ou rien).
- Coût dominé par le réentraînement de la sonde, qui croît encore : la borne haute du devis peut être dépassée ; la
  garde B − 2 de la continuation coupera alors à K′ < 72.

## 9. Ce qu'il faut pour lancer (rien de cela n'est fait)
1. Choix de Lazar : continuation, run neuf, ou rien (le verdict à ≈ 34 tours se fait dans tous les cas).
2. Contre-lecture R2 de cette conception par un sous-agent neuf.
3. Addendum 7 scellé, contre-lu (R2), puis ligne de GO hors enveloppe sur `main` (session mère).
4. Code : `execution_continuation_v1`, lanceur et conduite neufs, transfert des sauvegardes du serveur 176187199 vers
   l'instance neuve, assembleur, lecture ; essais sur processeur ; essai à blanc à 2 tours sur une petite carte avant
   le run (inclus dans le devis).
