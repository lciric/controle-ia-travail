# Correctif (4) de l'arbre voisin : provenance de la tranche « chat » au nom de Llama 3.1 8B Instruct — note v2

Écrit par la session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`) le 2026-11-14, après 11:08 UTC (`date -u`), sur la
consigne de la mère (R-2721, R-2723). Aucune machine, aucune dépense ; code voisin non exécuté (R-2685, R-2710 : exécution seulement sur la
machine louée). **Note v2** (après 11:11 UTC) : remplace la note v1 (`ce671ab1…`, archivée) après sa contre-lecture
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-1-correctif-chat-v1.md`) ; la différence ne change pas ; retouches non relues
ensuite (déclaré). Annoncé par l'addendum des empreintes v3 (`e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82`, § 4).

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
**Ordre** : les quatre provenances de référence se lisent **avant** la passe, ou par `git show 849bfe16:data/corpus/<fichier>` — jamais dans
l'arbre après la passe, car `05_act_corpus.py` réécrit sur place `act-dclm`, `act-zh`, `act-code` et la provenance « chat » de Llama (sinon
la comparaison porterait sur un fichier comparé à lui-même). `NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct` est posé avant le
lancement (la variable est lue à l'import).
`src/controle_ia/neuron_lens/controles_b0_v2.py`, `verifier_provenances` : les quatre provenances **réécrites par le script** doivent avoir
la révision, le nombre de lignes et la liste ordonnée des identifiants des provenances **du dépôt voisin** (`act-dclm`, `act-zh`, `act-code`,
et pour « chat » `act-chat-qwen3-8b`), jamais le fichier déposé. Le script prend les premières lignes non vides du flux à cette révision ; le
texte d'une conversation n'est jamais vide une fois rendu, d'où l'égalité attendue des identifiants (à constater, non supposée). Pour
dclm, zh et code, des textes vides peuvent être écartés (`strip_header` peut tout retirer), mais la référence a subi le même filtre à la
même révision : l'égalité tient aussi. Tout écart :
arrêt de B-α. `compter_debuts` compte les jetons de début par document (double jeton possible dans la tranche « chat » de Llama, signalé).

## Deux points de la passe de Llama, hors de la provenance
- **Date dans le texte rendu** : selon la révision de son tokeniseur, le gabarit de Llama 3.1 peut insérer la date du jour dans l'en-tête
  système ; les identifiants de lignes ne changent pas, mais le texte de la tranche « chat », donc l'empreinte de son fichier, peut changer
  d'un jour à l'autre. À B0 : relever le texte rendu d'une ligne (ou le gabarit) et la date de la passe dans la partie 2 de l'addendum.
- **Longueur des documents** : l'en-tête du gabarit consomme une part du plafond de caractères des documents ; le corpus de Llama diffère par
  construction de celui de Qwen3-8B. Rapporté, pas un critère d'arrêt.

## Essais (exécutés ici, sur notre code seulement)
`tests/test_neuron_lens_controles_b0_v2.py` : provenances saines et artefacts (révision changée, identifiants permutés, tranche absente, clé
absente des deux côtés) ; empreinte de la liste `catalog.kept` versée (égale à `cd8a6c23…`) et artefacts (un jeton en moins, un jeton ajouté,
doublon refusé) ; comptes de jetons de début (document vide, triple jeton, jeton absent) ; contenu du fichier déposé par le correctif
(révision, 8 000 identifiants uniques, nom de fichier, empreinte `777aa068…`) ; l'égalité avec la provenance de Qwen3-8B (`a76c6b02…`) est
établie par lecture (autrice et contre-lecteur). 6 essais passés.

## Contre-lecture
Contre-lecture 1 : `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-1-correctif-chat-v1.md` (`1929da40…`) ; verdicts : différence
scellable en l'état ; note, code et essais scellables après corrections mineures. Traitement : (1 bis) ordre des références écrit (note et
code) ; (2) filtre des textes vides dit ; (3) date et longueur écrites ; (4) clé absente traitée et essayée ; (5) essais ajoutés, égalité
avec la référence citée.
