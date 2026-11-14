# Correctif (4) de l'arbre voisin : provenance de la tranche « chat » au nom de Llama 3.1 8B Instruct — v1

Écrit par la session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`) le 2026-11-14, après 11:08 UTC (`date -u`), sur la
consigne de la mère (R-2721, R-2723). Aucune machine, aucune dépense ; code voisin non exécuté (R-2685, R-2710 : exécution seulement sur la
machine louée). Annoncé par l'addendum des empreintes v3 (`e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82`, § 4).

## Objet
`scripts/05_act_corpus.py` (dépôt `stdlogits/neuron-lens`, commit `849bfe16`) lit, pour chaque tranche, la révision du jeu de données dans
le fichier de provenance `data/corpus/act-<tranche>.provenance.json` s'il existe (lignes 60-66) ; pour « chat », ce fichier est propre au
modèle (`act-chat-<modèle>.provenance.json`, `neuron_lens/corpus.py`, `act_file`). Il n'en existe pas pour Llama : sans retouche, le script
prendrait la **dernière** révision de `HuggingFaceH4/ultrachat_200k`, et la tranche « chat » de Llama ne viendrait pas des mêmes lignes que
celle du catalogue de Qwen3-8B. Le script ne lit que la clé `revision` de ce fichier, puis le **réécrit** après la passe (ligne 91).

## Le correctif
`docs/notes/neuron-lens-v1/correctifs/provenance-chat-llama-v1.diff` (création d'un fichier) : dépose
`data/corpus/act-chat-llama-3.1-8b-instruct.provenance.json`, copie exacte de `act-chat-qwen3-8b.provenance.json`
(`a76c6b02057d1a13b00185d589f063f82254fc8f184526db922b53962d82e784`) à la seule clé `file` près (`act-chat-llama-3.1-8b-instruct.jsonl`) ;
révision `8049631c405ae6576f93f445c6b8166f76f5505a` (la même pour Gemma 4 12B), 8 000 identifiants. Fichier déposé :
`777aa068a008b38fc22c6758d283e33ac31e31d6c5ed2eed878f7d75050d231d`. `git apply --check` sur le clone au commit `849bfe16` : réussi.
Argument de la passe : `--docs dclm=40000,zh=8000,code=8000,chat=8000`.

## Vérification après la passe (notre code, contre-lu)
`src/controle_ia/neuron_lens/controles_b0_v1.py`, `verifier_provenances` : les quatre provenances **réécrites par le script** doivent avoir
la révision, le nombre de lignes et la liste ordonnée des identifiants des provenances **du dépôt voisin** (`act-dclm`, `act-zh`, `act-code`,
et pour « chat » `act-chat-qwen3-8b`), jamais le fichier déposé. Le script prend les premières lignes non vides du flux à cette révision ; le
texte d'une conversation n'est jamais vide une fois rendu, d'où l'égalité attendue des identifiants (à constater, non supposée). Tout écart :
arrêt de B-α. `compter_debuts` compte les jetons de début par document (double jeton possible dans la tranche « chat » de Llama, signalé).

## Essais (exécutés ici, sur notre code seulement)
`tests/test_neuron_lens_controles_b0_v1.py` : provenances saines et trois artefacts (révision changée, identifiants permutés, tranche
absente) ; empreinte de la liste `catalog.kept` versée (égale à `cd8a6c23…`) et artefact (un jeton en moins) ; comptes de jetons de début ;
contenu du fichier déposé par le correctif (révision, 8 000 identifiants uniques, nom de fichier). 4 essais passés.

## Contre-lecture
À faire (sous-agent neuf, « modèle D »).
