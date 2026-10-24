# Provenance — organisme écrit par Gemini sous le contrat du noyau (v1)

- Source : dépôt `lciric/controle-ia-travail`, branche `canal/gemini-organisme-v1`, commit `6c61956c0318a2eab344c15b6fd1a347b8a5a816`
  (arbre git `0636f2f75a25ec87ecc10f8985f09832b2196ef7`), auteur « Controle IA », 2026-10-24 17:27:25 +0200 ; poussée par Lazar, écrite par Gemini
  (relève) d'après la consigne d'amorçage transmise par Lazar. Copié tel quel (marques d'ordre d'octets comprises) le
  24 octobre 2026 par la lignée conv-audit ; aucun fichier modifié.
- Empreinte d'arbre (chemins relatifs triés + SHA-256 des contenus, `essaim_m3.noyau.boucle.empreinte_arbre`) :
  `1e883c549595a18fdfc97c3bc5300f1abb682a230f310ae388699eb9ec38578f`
- Lecture avant tout lancement : aucune clé, aucun chemin de clé, aucun réseau, aucun sous-processus, aucune commande
  git ; appels par `noyau_client` seulement ; lecture de `dossier_archive` (`rglob("memoire_isvd.json")`) ;
  copie de soi-même en successeur avec `memoire_isvd.json` et `etat_generation_precedente.json`.
- Réserve (R4) : le rapport livré (`RAPPORT-ORGANISME-GEMINI-v1.md`, section 2) montre `1 failed, 2 passed`,
  `EXIT_CODE=1` (marque d'ordre d'octets en tête de `metrique/attaques.json`), alors que le texte de passation
  transmis par Lazar annonce « 3 passed, EXIT_CODE=0 ». Les deux ne peuvent pas être vrais du même état des fichiers.
- Famille déclarée pour la confrontation : `gemini` (auteur de l'organisme) ; l'organisme appelle en pratique la
  première espèce que `noyau_client.especes()` lui rend (ordre alphabétique : `CLAUDE_FABLE_5_1`).
