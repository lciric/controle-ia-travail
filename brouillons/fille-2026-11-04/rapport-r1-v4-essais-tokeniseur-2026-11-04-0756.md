# Rapport court — R1 v4, essais avec le tokeniseur — 2026-11-04-0756 UTC (date -u)
Ordre : `docs/procedures/ordre-fille-r1-v4-essais-tokeniseur-v1.md` (210564a7…), `main` à ebc3710a. Aucune dépense, aucune instance, aucun appel de modèle.

## Résultat
- Verdict : **381 passed, 0 skipped, 0 failed**, code 0, durée 24 min 28 s.
- Commit de départ : `af1f2f4f3ab5340586dcda19c0327d0c5beeefca` (branche `prep/r1-relance-v4`, récupérée par refspec explicite).
- Arbre de travail : `/home/user/wt/r1-v4`, `git status --porcelain` vide.

## Tokeniseur
- Dépôt et révision lus dans `prereg/R1-reparation-v4-config-v2.json` et `prereg/R1-rejeu-config-v6.json` (champs `agent`) : `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`.
- Chemin lu par les essais : `TOKENISEUR_LLAMA31` (dossier), d'après `tests/test_resolution_graine_v1.py`.
- Trois fichiers du tokeniseur seulement, sans les poids. Téléchargés sous `env -i` avec `HF_TOKEN` et le mandataire, HTTP 200 chacun, rien affiché du jeton :
  - `tokenizer.json` 79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4 (égal à TOKENIZER_JSON_SHA256 de l'essai) ;
  - `tokenizer_config.json` 177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424 ;
  - `special_tokens_map.json` 6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec.

## Commande
`TOKENISEUR_LLAMA31=/home/user/tokeniseur-llama31-0e9e39f2 HF_HUB_OFFLINE=1 PYTHONPATH=src nice -n 10 python -I -B -m pytest -q -p no:cacheprovider -rs <les 26 fichiers de CIBLES>`

## Écarts déclarés
- Environnement : un environnement neuf a échoué, disque plein (Errno 28) pendant l'installation de torch. Je l'ai supprimé et j'ai vidé le cache de pip. Les essais ont tourné dans l'environnement `/home/user/controle-ia-travail/.venv`, installé le 4 novembre depuis un `requirements-cpu.txt` identique à l'octet à celui de af1f2f4f (vérifié par diff ; torch 2.14.1, transformers 5.18.0).
- Ajouts à la commande de l'ordre : `HF_HUB_OFFLINE=1` (aucun accès réseau pendant les essais) et `-rs` (affiche les essais sautés ; il n'y en a aucun).

## Sortie complète de pytest
```
2026-11-04T07:31:36Z début pytest
........................................................................ [ 18%]
........................................................................ [ 37%]
........................................................................ [ 56%]
........................................................................ [ 75%]
........................................................................ [ 94%]
.....................                                                    [100%]
381 passed in 1468.33s (0:24:28)
code=0
2026-11-04T07:56:07Z fin
```
