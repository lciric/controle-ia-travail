# Relevé des dépôts publics de Bailey et de StrongREJECT, et écart de modèle — v1

10 novembre 2026, ≈ 07:45 UTC. Session « attaquant informé », mandat réduit à la reproduction de l'attaque publiée
(`registres/passations/2026-11-10-0725-decision-lazar-envoi-brief-mandat-reduit.md`, branche `claude/upbeat-cray-dmauvv`,
commit `9ed5fe75`). Lecture seule de deux dépôts publics clonés hors du dépôt de travail ; aucune dépense ; aucun fichier
de ces dépôts n'est copié ici ; rien du coffre n'a été lu.

**Niveau.** Infrastructure et mesure : quel fichier, quelle taille de jeu, quel juge, quelle licence. Aucun paramètre de
l'attaque n'est recopié : les configurations publiques sont désignées par leur nom et leur empreinte.

**Portée (R7).** Tout ce qui suit vient de la lecture de dépôts publics : provenance non opposable seule. Les renvois à
l'article sont faits sur le PDF empreinté `docs/sources/pdf/anteriorite-P-041-v2/c3/bailey-2025-obfuscated-activations-2412.09565.pdf`
(`9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9`, conforme à son compagnon, recalculé ce jour).

## 1. Dépôt de Bailey et collègues

- `github.com/LukeBailey181/obfuscated-activations`, commit de tête `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942`
  (11 février 2025), arbre `c7cf686c7325573460505647531284b90e5f34e2`. Deux commits en tout. La tête est encore celle
  relevée le 31 octobre (`bailey-depot-public-parametres-v1.md`, R-897).
- **Licence : aucun fichier de licence dans le dépôt** (ni `LICENSE`, ni `COPYING`, ni mention dans les `README`). Seul
  `inference_time_experiments/obf_reps/metrics/probes.py` reproduit une notice Apache pour un code tiers repris. Sans
  licence, aucun droit de copie, de modification ni de redistribution n'est accordé. **Nœud pour Lazar** (devis v2,
  section 5).
- Boucle de la section 3.5 de l'article : script `inference_time_experiments/train_harmful.py`
  (`83c3e4e747035311cfefa2163211ab6fcdb3058928db7d935633221a650d1b9b`), évaluation `evaluate.py`
  (`8cd2ecbce601421582ce64f56c45e2a4dd06b22f1e7c40bbd3123c587073131e`).
- Configuration publique de la boucle pour la sonde à une couche cachée : `configs/experiment/zf-iter-100-mlp.yaml`
  (`7d3bd16aed266f4a0e0ac12628cb88bf17e3c2e74032e3ada1d7d38ffa9bf592`), qui hérite de `z-jailbreak.yaml`
  (`bb2f85e43d69fe33129fa171f1af16c57b6ca62b7e441b6168ba80ee1ae47e97`) puis de `default.yaml`
  (`f38bb18951ef775ae114b1783a5d8a32d91270fcbdf587aee0ddf576956e211c`). Celle de l'ensemble de sondes :
  `zf-iter-100-ensemble.yaml` (`a0e5298999702a0c…`, non retenue ici).
- La configuration publique fixe 100 tours d'attaque et de défense. Chaque tour d'attaque fait deux passes sur le jeu
  nuisible d'entraînement, par lots de un : 1 600 pas de gradient par tour, selon la lecture du code (à confirmer au
  pilote par le compte journalisé).
- Jeu `inference_time_experiments/datasets/harmful_dataset/`, colonnes `prompt` et `response`, lignes comptées par un
  lecteur de fichiers à valeurs séparées (les fichiers ont des champs sur plusieurs lignes) :

| Fichier | Lignes | Empreinte |
|---|---:|---|
| `harmful_train_no_spec_tokens.csv` | 800 | `1063d28221dc5a59e1f60d6fa0bc4828c9983ce3db15a106e160d487bafbb081` |
| `harmful_val_no_spec_tokens.csv` | 100 | `e1ff21a28b06a771c0bdba0e5f732dd659b02a6c3c10ffe833dc1f136135391c` |
| `harmful_test_no_spec_tokens.csv` | 100 | `77b81432ab98f1d583df649622d641157cfe9b4339d0ad320269fc10c4a1a661` |
| `benign_train_no_spec_tokens.csv` | 800 | `690b038241fe4b0f9e3b6bbb61ef34e10aa7d2d7a0766214543e0c96813116ff` |
| `benign_val_no_spec_tokens.csv` | 100 | `0f0a0e77dab83eae68e1a4e6e8dcdfec049be40ce8ca1b14106676dde8fc1cef` |
| `benign_test_no_spec_tokens.csv` | 100 | `782901e4e9e6b2da4816ddc2a47060cec9c884758890bdbc4e96f4c46f9e2d88` |

- **Population de la mesure dans le code public.** `evaluate_model_and_metric_harmful` réunit validation et test : 200
  entrées nuisibles et 200 entrées bénignes tenues à l'écart de l'entraînement. Appelée par la boucle avec
  `evaluate_metric_on_gens=False` : la sonde lit l'activation du dernier jeton de l'entrée, pour les 200 entrées
  nuisibles avec le suffixe, les mêmes sans suffixe, et les 200 bénignes ; la population n'est pas filtrée par le succès
  du comportement. Le code journalise les notes brutes de la sonde et l'aire sous la courbe ; **il ne calcule pas le
  rappel à 1 % de fausses alertes** : ce calcul revient au code d'analyse.
- **Comportement.** Le taux journalisé est la part des 200 réponses produites avec le suffixe (300 jetons au plus) dont
  la note du juge dépasse 0,5 (`behavior_threshold`). Les réponses produites sans suffixe sont gardées dans la table mais
  ne sont pas notées.
- **Journal : service externe.** Les configurations publiques écrivent leurs résultats chez Weights & Biases
  (`logger: "WAndBLogger"`, compte exigé). Le seul autre journaliseur du dépôt (`DummyLogger`) ne garde rien. Une
  reproduction sans compte externe demande un journaliseur local, à écrire.
- **Graine.** La configuration fixe `seed: 0`, transmis à l'initialisation du suffixe ; aucune graine globale n'est posée
  dans le code lu : le run publié n'est pas reproductible au bit près.
- **Dépendances non épinglées.** `setup.py` installe trois paquets depuis la branche `main` de dépôts tiers
  (`representation-engineering`, `sparsify`, `strong_reject`) : à épingler par commit.
- **Matériel.** `inference_time_experiments/README.md` : « All experiments we run used a single NVIDIA A100 GPU, which
  has 80G memory per chip. » (confirme l'erratum du 31 octobre).

## 2. Écart de modèle — erreur de la note de choix

- L'article surveille **Llama-3-8B-Instruct** (PDF, p. 7 : « Unless stated otherwise, we use Llama-3-8B-Instruct as our
  model being monitored »).
- Le programme utilise **Llama-3.1-8B-Instruct** (`docs/programme-controle-ia-v2.md`, l. 249 ; brief v2, l. 38 ;
  `src/controle_ia/harnais/modeles.py`, l. 25-30 : seuls quatre modèles sont autorisés, Llama-3-8B-Instruct n'y est pas ;
  « tout ajout passe par un GO de Lazar »).
- La note de choix (`docs/notes/reproduction-attaque-publiee-v1/choix-et-anteriorite-v1-brouillon1.md`, branche
  `claude/upbeat-cray-dmauvv`, empreinte `c6020167…`, en contre-lecture) écrit « modèle identique au nôtre
  (Llama-3-8B-Instruct) » et reproche au candidat 2 d'être sur Llama-3.1-8B, « pas notre Llama-3-8B-Instruct ». **Les
  deux phrases sont inversées** : c'est le candidat 2 qui est sur le modèle du programme, et Bailey qui est sur un autre.
  Le choix de Bailey tient par ses autres raisons (code public, PDF empreinté, vérification faite, autorisation
  existante) ; l'avantage « même modèle » tombe.
- Détail du dépôt public : `download.py` associe le nom `llama3-8b` à `meta-llama/Meta-Llama-3-8B`, la version de base,
  alors que l'article dit « Instruct ». La reproduction suit l'article.
- **Nœud pour Lazar** : reproduire sur le modèle de l'article demande un GO de modèle (devis v2, section 5).

## 3. Dépôt du juge StrongREJECT

- `github.com/dsbowen/strong_reject`, commit de tête `7a551d5b440ec7b75d4f6f5bb7c1719965b76b47` (7 juillet 2025).
  **Licence MIT** (fichier `LICENSE`, « Copyright (c) 2024, Dillon Bowen »).
- `strongreject_finetuned` (`strong_reject/evaluate.py`) charge un **modèle local** depuis Hugging Face
  (`qylu4156/strongreject-15k-v1`) : le juge tourne sur la carte graphique louée, sans appel payant. Le poste « juge »
  du devis v1 (5 à 10 USD d'appels) n'a pas lieu d'être ; le juge coûte du temps de carte et de la mémoire.
- Accès au modèle du juge (conditions d'accès, modèle de base) : non vérifiable d'ici ; à vérifier à la mise en place.

## 4. Ce que cette note ne contient pas

Aucun paramètre d'attaque recopié, aucun texte des jeux, aucun contenu du coffre, aucun résultat.
