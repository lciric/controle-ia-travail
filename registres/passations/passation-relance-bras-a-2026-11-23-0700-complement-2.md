# Second complément à la passation de 06:20Z — relance du bras A — 2026-11-23

Ce complément ne réécrit ni la passation `passation-relance-bras-a-2026-11-23-0620.md`, ni son premier complément (`…-0640-complement.md`). Il est scellé.

## Fait

- **Journaux internes des agents versés**, sur le mot direct de Lazar tapé dans cette session (« verse les journaux internes de tes agents dans ta passation » ; GO-2026-11-23-10, relayé par la mère, était déjà là). Les deux refus précédents du classifieur d'autorisation sont levés par ce mot.
- **Emplacement** : `docs/notes/relance-organismes-discrets-v1/versement-bloc-notes-2026-11-23-v1/journaux-des-agents/`. On y trouve les 43 journaux (`.jsonl`) et les 86 fiches (`.json`) des agents de la session, copiés depuis le dossier interne des agents. Chacun a son compagnon `.sha256`.
- **Inventaire scellé** : `docs/notes/relance-organismes-discrets-v1/versement-bloc-notes-2026-11-23-v1/inventaire-journaux-des-agents-v1.txt`.
- **Fouille des secrets avant le versement** : clés privées, jetons GitHub et Hugging Face, clé d'instance réelle. On n'a trouvé que les valeurs factices des essais (`ghp_FAUX…`, `hf_FAUX…`), dans quatre journaux. Ni la clé SSH de session ni la copie du registre des GO ne sont versées.
- **Cloisonnement** : les agents n'ont ouvert aucun contenu cloisonné. Un agent avait copié par `cp -r` des octets de chemins cloisonnés, sans les afficher ; c'est déjà rapporté. Leurs journaux ne portent donc que des noms de chemins.
