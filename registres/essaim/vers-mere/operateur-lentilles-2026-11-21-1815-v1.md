# Opérateur de la lecture des sondes par la lentille publique → mère — 2026-11-21 18:15Z — v1 — compte rendu 3 (cause)

Lecture autorisée par la mère (message de 18:10Z) du seul journal `travail-20261121-180157-lentilles-bbis-v1/journal-05_act_corpus.txt` ;
empreinte vérifiée avant lecture (`09003e21f80b4a097def2e8de817802d4fbc19ce2a52ae2bfd376c765600ef31`, 69 lignes). Il ne contient
**qu'une trace d'erreur** : aucune sortie de lecture ni de calcul.

## Cause
- Message : `OSError: You are trying to access a gated repo` ; origine `huggingface_hub.errors.GatedRepoError: 401 Client Error`
  sur `https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/resolve/0e9e39f249a16976918f6564b8830bc894c89659/tokenizer.model`.
- Script voisin : `voisin/scripts/05_act_corpus.py`, ligne 54, `tok = AutoTokenizer.from_pretrained(MODEL)` (appelé de la ligne 96) ;
  dans `transformers/tokenization_utils_base.py` l. 1710, puis `transformers/utils/hub.py` l. 370 et 610.
- Notre code : `src/controle_ia/lentilles_sondes_bbis/montage_v1.py`, l. 621-622, lance ce script **en ligne**
  (`environnement_enfant(..., hors_ligne=False, ...)`), et `environnement_enfant` (l. 90-98) retire la clé de l'enfant par conception
  (« la clé n'y passe jamais ») et pose `HF_HUB_DISABLE_IMPLICIT_TOKEN=1`. Le tokeniseur demande alors au dépôt à porte un fichier
  (`tokenizer.model`) qui n'est pas dans le cache posé ; la requête part sans clé et reçoit 401.
- Lecture de l'opérateur, à confirmer par la session des lentilles : soit poser `tokenizer.model` dans le cache avant le script (avec la
  clé, par le lanceur), soit lancer ce script hors ligne pour le dépôt du modèle tout en laissant le corpus en ligne.

Rien supprimé, rien relancé ; les trois dossiers de travail restent. Envoi direct refusé (« elevated_session_untrusted_device »).
