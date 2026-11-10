# Passation — NARCBench, bras externe (session fille) — 2026-11-10, 11:16 UTC (`date -u`)

- **Session** : fille de `session_01QPDgKgACWyCkCN8HjqwNXy`. Identifiant `session_01QPDgKgGRpVYqfbzKs8dpT6`
  (https://claude.ai/code/session_01QPDgKgGRpVYqfbzKs8dpT6). Modèle Claude Opus 5.5. Environnement avec réseau.
- **Motif** : le quota hebdomadaire du compte atteint 92 % à 11:11 UTC (mot de Lazar transmis par la mère). Le travail passe à
  une nouvelle instance, sur un autre compte.
- **Branche** : `prep/narcbench-externe-v1`, partie de `c43824d4`. Dernier commit de travail : `abbbcfde`, poussé.

## Mandat (mère, d'après R-2175)

Bras externe NARCBench, à faire sur les activations publiées par les auteurs, au processeur, pour 0 USD. Les cinq étapes :

1. Licences.
2. Téléchargement de CORE et STEGO seuls, plafond 1,5 Go, hors du dépôt, avec un manifeste d'empreintes.
3. scikit-learn épinglé et chargeur, avec un cas sain et un artefact pour chaque garde (R5).
4. Les trois points de recette tranchés sur le code publié.
5. Rapport scellé.

**Interdit avant le texte court scellé (R1)** : toute lecture des aires et toute course de la recette. Seuls des essais de
forme sont permis.

## Fait

- **Rapport scellé** : `docs/notes/narcbench-8b-v1/rapport-externe-donnees-v1.md`, sha256
  `be31452feef03d854353aa693e33fe107d6751964cd0c19f28d063745190220f`. Tout le détail s'y trouve.
- **Licences**, vérifiées à la source le 10 novembre entre 11:05 et 11:07 UTC :
  - jeu NARCBench : MIT ; fiche `05be2d89…`, identique au brouillon 4 ;
  - code des auteurs : MIT ; `4744a390…`, identique au brouillon 4 ;
  - Qwen3-32B : Apache 2.0 ;
  - Llama 3.1 : licence communautaire ; l'usage est permis, sans redistribution.
  - Écart : le nom de point de contrôle Llama donné par la fiche n'existe pas (réponse 401).
- **Données** : 8 fichiers, activations et métadonnées CORE et STEGO de `qwen3_32b` et de `llama_3_1_70b`. Total
  712 344 334 octets ; chaque taille sur disque est égale à la taille publiée. Révision du jeu `19cb14b2…`. Manifeste :
  `docs/notes/narcbench-8b-v1/manifeste-donnees-externe-v1.json` (`fc096b82…`). Les empreintes publiées sont aussi codées dans
  `chargeur_externe_v1.EMPREINTES_PUBLIEES`.
- **scikit-learn** : `scikit-learn==1.9.1`, avec `joblib==1.6.0`, `threadpoolctl==3.8.0` et `narwhals==2.28.0`, figés dans
  `requirements-cpu.txt`.
- **Chargeur** : `src/controle_ia/narcbench/chargeur_externe_v1.py` et `tests/test_narcbench_chargeur_v1.py`, 13 essais. Avec
  les essais existants du module : 40 verts sur 40.
- **Trois points de recette**, tranchés sur `probes/reproduce_LR.py` au commit `85fea3be2a9d` :
  - (i) l'aire de CORE est la moyenne des aires par pli (`mode_core = "par-pli"`) ;
  - (ii) la standardisation se fait sur le jeu d'apprentissage équilibré, en vecteurs par message ;
  - (iii) les couches vont de 26 à 30 pour Qwen3-32B et de 32 à 37 pour Llama-3.1-70B.
- **Écarts E1 à E7**, à trancher dans le texte court : voir le rapport, § 6.

## En attente : le refus de permission

Vers 11:07 UTC, le contrôle de sécurité intégré de Claude Code a refusé la commande de calcul des empreintes sur disque.
C'était une boucle de `sha256sum` et `git hash-object`, sans aucune suppression. Motif cité : « could not be checked for
dangerous rm operations ». La commande n'a été ni relancée ni reformulée. Consigne de la mère : ne pas calculer les empreintes
autrement **en attendant le mot de Lazar**.

## Reste

1. Le mot de Lazar sur le refus. Ensuite, `verifier_fichiers` sur les données ; le manifeste v2 (R12) reçoit les empreintes
   sur disque.
2. L'essai de forme : clés, formes, types, nombre de tours par phase, épisodes à quatre agents, domaines. Il ne lit aucun
   score.
3. `externe_v2.py` pour E1 à E4, puis la contre-lecture du code par un autre modèle (N-052).
4. Le texte court neuf, sa contre-lecture (R2), le scellement, puis la course.

## Fichiers hors du dépôt : ils seront perdus avec la machine

- **Données** : `/home/user/narcbench-donnees/activations/…`, 712 344 334 octets, non versées. **Elles disparaîtront avec ce
  conteneur.** La nouvelle instance doit les retélécharger depuis
  `https://huggingface.co/datasets/aaronrose227/narcbench/resolve/19cb14b269e052b19ba6d2bd2f4519afd3b10c57/<chemin>`.
  Les chemins et les empreintes publiées sont dans le manifeste. Il faut ensuite les vérifier par `verifier_fichiers`, si le
  mot de Lazar le permet.
- **`.venv`** : non versé. Pour le recréer :
  `python3 -m venv .venv && pip install numpy==2.4.6 scipy==1.17.1 pytest==9.1.1 matplotlib==3.11.2 scikit-learn==1.9.1`,
  puis `pip install torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu`.
- **Bloc-notes** : textes des licences, code des auteurs, texte extrait du PDF. Leurs empreintes sont citées dans le rapport ;
  on peut les relire à la source.

## Prochaine action exacte

Attendre le mot de Lazar sur le refus, relayé par la mère. S'il autorise :

1. retélécharger les 8 fichiers ;
2. lancer `PYTHONPATH=src python -c "from controle_ia.narcbench.chargeur_externe_v1 import verifier_fichiers; print(verifier_fichiers('/home/user/narcbench-donnees'))"` ;
3. écrire `manifeste-donnees-externe-v2.json` ;
4. faire l'essai de forme seulement.

Aucune instance de calcul active. Aucune dépense.
