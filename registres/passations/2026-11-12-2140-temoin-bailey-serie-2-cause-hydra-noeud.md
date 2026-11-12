# Témoin de Bailey — nouvelle série : seconde chute du pilote ; cause établie (appel de Hydra par import) ; nœud — 12 novembre 2026, 21:40 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas (R12).

## Verdict (addendum 3, § 2.4)
**« Seconde chute du pilote : pas de run principal, pas de verdict ; nœud ; aucune autre série sans nouvelle décision de
Lazar et nouvel addendum. »** La série de l'addendum 3 est consommée. **Cause établie et nommée.**

## Déroulé (journal `sortie-conduite-v9/conduite-v5.jsonl`, bilan `bilan-conduite-v5.json`)
Conduite v9 (envoi `scp` retenté) sur le poste Hetzner v9 (175884265) ; instance 60403564 (Oregon, 1,3314 USD/h), prête à
20:42:25Z ; amorce finie à 21:07:06Z (≈ 24 min) ; auto-arrêt disponible ; mise en place : aucune garde tombée (pas par
tour 1 600, suffixe 13) ; contrôle du juge : garde passée ; **pilote** (21:11:09Z) et **reprise** (21:12:19Z) : code 1 en
≈ 70 s, zéro tour, `erreur_demarrage: true`. Instance détruite par la conduite à 21:15:19Z après transfert complet. D du
poste : 2,778 USD.

## Message d'erreur (addendum 3, § 2.1 ; diagnostic borné de la liste d'arrêt)
`sortie-conduite-v9/pilote/transfert-1/erreur-demarrage-v1.txt` (`33599bfc…`), identique pour la reprise : trace Hydra
`run_and_report` → `hydra.run` → `compose_config` → `config_loader.load_configuration` →
`ensure_main_config_source_available` → `importlib_resources_config_source.available` → `importlib.resources.files` →
**`NotADirectoryError: MultiplexedPath only supports directories`**. Aucune note, aucun texte produit (mort avant la
configuration).

## Cause (établie par reproduction sur processeur, sans dépense)
`execution_v3.main` appelle le script public **par import** (`import train_harmful` ; `train_harmful.main()`), alors que les
auteurs le lancent comme programme (`python train_harmful.py`). Le décorateur public est
`@hydra.main(version_base=None, config_path="configs", config_name="config")` (`train_harmful.py` l. 171, commit
`9c1f4b1a`). Appelé depuis un module importé (non `__main__`), Hydra cherche la configuration comme **ressource du paquet
Python `configs`** au lieu du dossier voisin du fichier, et échoue. Reproduction (code public cloné hors du dépôt, module
minimal portant le même décorateur, dossier `inference_time_experiments`) :
- Hydra 1.3.2 (version figée) et 1.3.8 : appel par import → « Primary config module 'configs' not found » (même chemin de
  code ; sur l'instance, où un autre `configs` existe dans l'environnement, la même recherche lève `NotADirectoryError`) ;
- lancement comme programme (`python …`) → configuration imprimée ;
- **correction candidate** : `runpy.run_path(<clone>/inference_time_experiments/train_harmful.py, run_name="__main__")`
  après la pose de `sys.argv` → configuration imprimée (Hydra 1.3.2). Le remplacement du journaliseur (écart 2) est
  gardé : le script construit son journaliseur dans `obf_reps.utils` (l. 394-396), modifié avant l'appel et réutilisé par
  `runpy` (module déjà chargé).
- La chute du 12 novembre à 15:33Z (même durée, même absence de journal) a très probablement la même cause.

Ce défaut était dans tout le code d'exécution depuis `execution_v1` ; aucune épreuve ne lançait `train_harmful.main()`
(l'essai à blanc de l'installation `fdff1672…` vérifiait seulement que le code public s'importait).

## Dépense
Instance 60403564 ≈ 0,75 USD ; D du poste = 2,778 USD (six instances, toutes détruites) ; B = 75 USD. Poste Hetzner v9 en
marche, sans tâche, ≈ 0,011 EUR/h, **gardé sur consigne de Lazar** (« ne détruis rien »).

## Nœud — décision de Lazar
(a) `execution_v4` (appel par `runpy.run_path`, run_name `__main__`) : code, essais (dont une épreuve qui exécute vraiment
`@hydra.main` sur la configuration publique jusqu'à l'impression, sur processeur), contre-lecture, addendum 4 (écart
nommé : cause technique établie), nouvelle série ; (b) arrêter le témoin.
