# Lecture du script voisin du corpus (`scripts/05_act_corpus.py`) — v1

Session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z), 2026-11-21T19:36:34Z. Ferme la réserve 2 de la contre-lecture du correctif du tokeniseur
(`contre-lectures/contre-lecture-correctif-tokeniseur-act-corpus-v1.md`, 1e8c1704…), à la demande de la mère (19:35Z).

## Copie versée
- Chemin : `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/scripts-05_act_corpus.py.txt` (code archivé avec le suffixe .txt, **non exécuté**).
- Adresse : https://raw.githubusercontent.com/stdlogits/neuron-lens/849bfe1678e28becceb1e3864afe5fc8297d02e4/scripts/05_act_corpus.py
  (commit du voisin `COMMIT_VOISIN` de `constantes_v1.py`).
- Octets : 4497. SHA-256 : 518f4176bec915d649efe1016078515f19e912203285ec2a238752ee61eb100c. Relevé : 2026-11-21T19:36:34Z, par curl, sans clé, sans donnée du projet.

## Ce que le script demande au réseau
1. `AutoTokenizer.from_pretrained(MODEL)` : **seule demande au dépôt du modèle, à porte**. C'est ce que le correctif du tokeniseur
   (`cache_tokeniseur_v2`, lanceur v9) couvre ; le gabarit de conversation (tranche « chat ») vient de `tokenizer_config.json`, posé.
2. `HfApi().dataset_info(repo).sha` quand aucune provenance n'est déjà en place, puis `load_dataset(..., streaming=True, revision=...)`
   pour les quatre jeux publics : `HuggingFaceFW/dclm_100BT-shuffled`, `HuggingFaceFW/fineweb-2` (`cmn_Hani`),
   `codeparrot/codeparrot-clean`, `HuggingFaceH4/ultrachat_200k` (`test_sft`). Aucun n'est le dépôt du modèle.
3. La tranche « dclm » lit `dclm.provenance.json` dans le dossier du corpus si sa propre provenance manque (lecture locale).

## Conclusion
Aucune autre demande au dépôt à porte que le tokeniseur : le point 2 du développeur et la réserve 2 de la contre-lecture sont fermés
sur pièce. Ce que je n'ai pas vérifié : les modules `neuron_lens.corpus` et `neuron_lens.paths` importés, non versés ; ils
nomment des fichiers locaux.
