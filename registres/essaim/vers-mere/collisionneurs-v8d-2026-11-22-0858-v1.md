# Collisionneurs v8d, compte rendu 36 : acceptation nommée d'un faux positif prête (v8j conforme), reprise du tirage au hasard à ton mot

Écrit à 2026-11-22T08:58:37Z (`date -u`). Aucun appel pour ce travail.

- Suite des versions, chacune contre-lue par le même Opus neuf, avec ses mutations :
  - v8g : à corriger, un chemin réel suivi d'un point passait ;
  - v8h : à corriger, ponctuation interne et jeton coupé ;
  - v8i : à corriger, chemin imbriqué et homoglyphes ;
  - **v8j : conforme** (`docs/notes/collisionneur-v9/collisionneur_v9_v8j.py`, d199a14b…), 393 essais, 15 mutations tuées, les survivantes équivalentes.
- Règle finale : `--accepter-motif CELLULE:chemin interne`. Chaque occurrence dans la cellule scellée doit être `docs|runs|scripts/NOM`, sur deux composants exactement. NOM est en ASCII, ne nomme aucune entrée du dépôt (sans casse, ni préfixe de six caractères ou plus) et se termine sur un blanc ou une ponctuation de phrase. Tout est contrôlé avant toute écriture, puis journalisé. Seul le bloc exact de la cellule est exempté ; `verifier` revalide l'acceptation.
- Non-bloquant laissé : une ponctuation de phrase admise peut couper un jeton (`scripts/depot'expurge.py`). Le texte servi ne contient alors aucun chemin réel exact. Il faudrait un auteur qui déforme exprès un nom connu.
- **Commande proposée**, à lancer sur ton mot. Elle s'arrête au premier refus d'une critique du tour III.2 qui citerait le chemin ; une acceptation de plus se ferait alors avec les mêmes contrôles.
  `GO_ID=GO-2026-11-22-33 … collisionneur_v9_v8j.py etage3 --fable --opus --argon --astra --carbon --neon … --sortie runs/collisionneur-protocole-x-tirage-au-hasard-v1-20261122-080414 --plafond-usd 50 --ligne-usd 50 --reprise --accepter-motif "E3-T1-conception-F:chemin interne"`
  Elle partirait en troisième voie, au-delà des deux dossiers en parallèle de ta règle. Je propose de l'insérer dans la voie des dossiers avec Neon, après le dossier en cours (questions des concurrents) ; ou de la lancer tout de suite, si tu relèves la règle pour ce seul dossier.
- Courses : problématique au tour III.2 ; questions des concurrents au tour III.1.
