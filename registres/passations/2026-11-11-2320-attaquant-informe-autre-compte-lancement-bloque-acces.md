# Session « attaquant informé » sur l'autre compte — lancement du témoin de Bailey bloqué par l'accès — 11 novembre 2026, 23:20 UTC

Session neuve (`session_01XJ6Mgqg6DeUDvNm87LXApc`), autre compte, brief de passation v2. Branche
`claude/compassionate-meitner-d4ryyk`, tête lue `abbb1896` (dépôt chez le tiers de l'addendum 2 du témoin consigné). Ne se
réécrit pas (R12).

## Verdict
Témoin **non lancé** : ce conteneur n'a ni accès réseau à Vast.ai ni aux poids des modèles, ni les clés. Aucune instance
créée, aucune dépense.

## Constaté
- `VAST_API_KEY`, `HF_TOKEN` : absentes de l'environnement (noms seuls vérifiés, aucune valeur lue).
- `console.vast.ai:443` et `huggingface.co:443` : connexion refusée par le mandataire de sortie du conteneur (refus 403
  au tunnel), domaines non autorisés pour ce compte.
- Prêt pour le lancement : `.venv` en Python 3.11 avec `requirements-cpu.txt`, `hydra-core`, `pandas`, `vastai` 1.11.0 ;
  `lanceur_v13.py` `9257266f…` et `instance_v12.py` `de466986…` conformes à l'addendum 2 ; essais
  `test_temoin_bailey_condition6_v13.py` et `test_temoin_bailey_analyse_v3.py` : 175 passés ; `docs/sha256sums-lancement-v2.txt`
  conforme ; `GO-2026-11-10-10`, `-11-01`, `-11-02` relus sur `origin/main` (`1d434188`, l. 300, 305, 306).
- `verifier-arbre` : deux écarts antérieurs à cette session (empreinte orpheline
  `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` ; compagnon absent de
  `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v9.md`), non corrigés, hors du code du run.
- `registres/etat.md` non lu ni modifié (cloison du brief v2).

## Ce qu'il faut à Lazar (nœud : compte)
1. Autoriser `console.vast.ai` et `huggingface.co` (et les hôtes de téléchargement des poids, `cdn-lfs*.huggingface.co`,
   `*.hf.co`) dans les réglages de ce compte, rubrique « Capabilities » ; ou relancer depuis un poste qui les atteint.
2. Rendre `VAST_API_KEY` et `HF_TOKEN` disponibles dans l'environnement de la session (jamais collées dans la conversation).

## Prochaine action
Une fois 1 et 2 faits : reprendre à l'étape 2 de la procédure (`2026-11-11-1624-…`), inventaire `vastai show instances`,
puis manifeste, offre, ordre de lancement consigné, conduite détachée.

## Instances actives
Aucune créée par cette session.
