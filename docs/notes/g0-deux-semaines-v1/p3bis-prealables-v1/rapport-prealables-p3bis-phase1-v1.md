# Préalables de P3-bis, phase 1 — rapport de la session fille (v1)

Écrit le 2026-11-11T00:20:59Z (heure relevée par `date -u`) par la session fille `session_013QMayo3Je79e17xB1yHiDw`, pour la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, selon la consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-fille-p3bis-prealables-phase1-v1.md` (`0d7dc7e0ea9a7e59e6ebcddcb4dfdecedd18589fbb6c254557124708c19087dc`, vérifiée contre son compagnon). Aucune dépense, aucun appel de modèle ; seul accès externe : registres de paquets (pip) et téléchargement du tokeniseur (Hugging Face, clé `HF_TOKEN` lue par son nom seulement). Aucun fichier de T0.7 ouvert ; `docs/notes/bras-attaque/` retiré par extraction partielle avant tout (absence vérifiée sur disque), dans le dépôt et dans les deux clones.

## Verdict
P-4, P-1, P-2 et la mesure des longueurs : conformes. **N = 531** (Python 3.11.18). **A = T sur les 60 tâches et les quatre mesures** ; A = B aussi (aucune règle d'ajustement à appliquer).

## Textes lus (empreintes vérifiées)
- `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon12.md` (`07b160630811c88eb6a139c89b904f9beb3ea5a8e335948ebec1068ec93cb1f6`) ; contre-lecture 4 `contre-lecture-4-brouillon11-v1.md` (`90847ae2d017c6e100a15cf80ecee17645a4c71ecd33197187767cc2ff9d2c13`, empreinte seule vérifiée).
- Chaîne : branche `prep/p3bis-lanceur-v1` à `614fd5da` ; `controles_avant_depense_p3bis_v1.sh` (`e1591d9d9c0141442204594452fe9df5adc3cc779c561afb7c78ec9df4ff2c67`, égal à son compagnon) ; module commun `verifications_p3bis_v1.py` (`08661404b74c5b0440297c94b67222793a7ee377b3256b87df0eab68da9390b0`, égal à son compagnon). Code : `a1de39151ebae29138a389829751397074239615`.

## P-4 — place disque
`df -Pk /tmp` à 2026-11-10T23:58:51Z : **27 113 316 ko libres** ≥ 12 692 612 ko (conforme). **Réserve** : à 2026-11-11T00:03:54Z, après l'environnement PY, deux clones (4,0 Go chacun) et le cache de pip, 9 291 496 ko libres (< seuil) ; avant P-6 sur cette machine, effacer par leur chemin exact `/home/user/mesure-longueurs-p3bis-v1` (et au besoin le cache de pip), puis relever de nouveau. Pièce : `place-disque-p4-v1.txt`.

## P-1 — environnement PY
`PY=/home/user/venv-p3bis-py311-v1/bin/python`, Python **3.11.18** (`/usr/bin/python3.11 -m venv`), `pip install -r requirements-gpu.txt` du commit du code (code 0, 2026-11-10T23:59:10Z → 2026-11-11T00:02:56Z). Contrôle du bloc 8 recopié : 10 dépendances épinglées, **aucun écart** : matplotlib 3.11.2, numpy 2.4.6, pytest 9.1.1, scipy 1.17.1, torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2, safetensors 0.8.0, huggingface_hub 1.33.0, **pypandoc_binary 1.17**. Pièces : `versions-py-p1-v1.txt` (dont `pip freeze`), `pip-install-p1-sortie-brute-v1.log`.

## P-2 — recompte de N
Clone `/home/user/clone-p3bis-a1de3915-v1` au commit du code, extraction partielle aux motifs `EXTRACTION` de la chaîne, `docs/sources/` présent, chemins interdits absents, `git status --porcelain` vide après. Liste `scripts/essais-cibles-p3bis-v2.txt` (30 fichiers, `3ecf3cdaee807ec4e74059132b4bded1962fb576e3adba6c31e8f64206f62276`, égale à `LISTE_SHA256` de `scripts/p3bis_instance_v2.sh` et à la citation du brouillon 12). Dernière ligne exacte : **`531 passed in 1018.40s (0:16:58)`** ; aucun saut, aucun échec. Égal au N provisoire du brouillon 11 (531, Python 3.13). Pièce : `essais-cibles-p2-sortie-brute-v1.txt`. Note : `tests/test_premier_test_ia_ouverture_p3bis_v1.py` importe le module de code `controle_ia.t07.registre_v1` et monte des fichiers synthétiques de T0.7 dans des dossiers temporaires ; prescrit par la liste, aucun fichier de T0.7 du dépôt ouvert par moi.

## LONGUEURS_P3BIS — mesure au vrai tokeniseur
- Programme : le corps du bloc 7 de `controles_avant_depense_p3bis_v1.sh` (heredoc `EOF_TOK`), extrait à l'octet (`857fbde319764ff1c76def864fc60cd3364dadfee226402a932556b28cb28132`), joué par `PY` avec `HF_HOME` neuf, dans une copie de travail au commit du code (`/home/user/mesure-longueurs-p3bis-v1`, même extraction partielle).
- Entrées : consignes candidates `P3-bis-consignes-v1-brouillon2.md` (`7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367`) copiées en `prereg/P3-bis-consignes-v1.md` et scellées dans la copie de travail seulement ; configuration candidate `P3-bis-temoin-positif-config-v1-brouillon1.json` (`8ab04d54531208b248fad8262283644c3ebd7e25cae10643657fdeccb6a6dbe1`) avec le seul champ `consignes_sha256` rempli par `7d35576d…` (réécrite triée, indentée : copie de travail, non versée) ; tâches `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (`287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa`, égale au compagnon).
- Tokeniseur : `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, `tokenizer.json` `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` (égal au préfixe `79e3e522…` du texte) ; format vérifié (`chat`).
- Résultat : 60 tâches ; **A = T sur chaque tâche et chacune des quatre mesures** ; A = B partout. Résumé : consigne seule 51 (60 tâches), indication seule 51 (60), indication dans le gabarit 51 (60), consigne dans le gabarit 52 (56 tâches) ou 51 (4 tâches), identique pour A, T et B.
- Sous-commande `longueurs` du module commun sur la mesure et le résumé : « longueurs : A = T sur 60 tâches et quatre mesures ; résumé égal aux longueurs attendues », code 0.
- Pièces : `longueurs-mesurees-p3bis-v1.json` (sortie brute), `longueurs-attendues-p3bis-v1.json` (forme `resume_longueurs`, `json.dump(..., indent=1, sort_keys=True)` comme le banc des contrôles), `longueurs-tokeniseur-stderr-v1.txt` (sortie d'erreur : un avertissement de transformers seulement). **Réserve** : mesure valable pour ces consignes et cette configuration ; tout changement des consignes au candidat impose de remesurer.

## Écarts de procédure déclarés
- Avant de lire la consigne, j'ai fait `git fetch origin main` (refspec `main`) et `git checkout origin/main -- <consigne et compagnon>` pour vérifier son empreinte (contenu égal à HEAD, arbre resté propre).
- Le commit du code n'est atteignable que par `prep/p3bis-lanceur-v1` : chaque clone local l'a reçu par `git fetch origin +refs/remotes/origin/prep/p3bis-lanceur-v1:…` (refspec) depuis ce dépôt.
- Aucune demande de fusion ouverte : la consigne borne la sortie à la poussée de la branche.

## Points ouverts
Phase 2 (épingles P-5, passages canoniques P-6) à la consigne neuve de la mère ; réserve de place disque ci-dessus ; `PY` et clones restent sur cette machine.
