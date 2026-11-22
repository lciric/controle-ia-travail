# Collisionneur v9-v8g : rapport du développeur

Écrit à 2026-11-22T08:36:12Z (`date -u`). Classe B, Opus 5.5, session des collisionneurs, sur la décision de la mère (08:34Z) : Lazar veut Neon « absolument » dans le dossier du tirage au hasard, arrêté par la garde de motifs. Aucun réseau, aucune clé ; aucune reprise avant la contre-lecture, la vérification des corrections et le mot de la mère.

- `collisionneur_v9_v8g.py` (93f96e95…), copie de la **v8d** (b7803838…, intacte), et non de la v8e ni de la v8f : les dossiers en cours sont sans balises. Fabriquée par `fabriquer_v8g_depuis_v8d_v1.py`. Essais `test_collisionneur_v9_v8g.py` : 359 passés (351 hérités, 8 neufs), 11 sautés.

## Changement, et seulement celui-là
`--accepter-motif CELLULE:CATÉGORIE` : l'arbitre accepte un faux positif établi de la garde de motifs.
- Forme contrôlée avant toute écriture ; seule la catégorie « chemin interne » est admise.
- Contrôle sur la cellule scellée : chaque occurrence de la catégorie doit être de forme relative (`docs/`, `runs/`, `scripts/`), et le chemin entier (jeton) ne doit pas exister dans le dépôt. Sinon refus (code 7), rien n'est journalisé. Ainsi une forme absolue, une forme interne (`docs/notes/`) ou un chemin réel (par exemple `docs/programme-controle-ia-v2.md`) sont refusés.
- Journal : `{"decision": "motif_accepte", "cellule", "categorie", "sha256_cellule", "chemins"}`, une fois par cellule, catégorie et empreinte ; `etat.md` le dit.
- Portée : la garde (avant chaque envoi), `verifier` et le devis de reprise ne retirent que le **bloc exact** de la cellule acceptée, avec son texte et son empreinte scellés et identiques à ceux de l'acceptation. Ailleurs dans l'invite (faits, question, autres pièces) et pour les autres catégories, la garde reste entière. Une cellule changée rend l'acceptation caduque.

## Essai à blanc sur le dossier réel (sans écriture)
Dans `runs/collisionneur-protocole-x-tirage-au-hasard-v1-20261122-080414`, la conception de Neon (`E3-T1-conception-F`) contient le seul chemin `scripts/pipelines`, écrit en prose (« dans des scripts/pipelines d'analyse »), absent du dépôt : acceptable. Avec cette seule acceptation, les six invites du tour III.2 passent la garde (sans elle, cinq sont refusées).

## À savoir
- Au tour III.3, les critiques du tour III.2 peuvent citer ce chemin. Chaque critique qui le cite demande alors sa propre acceptation : arrêt au code 7, puis `--accepter-motif` de la critique, mêmes contrôles.
- Reprise d'un dossier de la v8d par la v8g : `--reprise` déclare le changement de script (règle de la v8d).
