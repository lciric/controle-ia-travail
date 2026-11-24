# Constat — lectures du dommage et de la diffusion de la course lue du saboteur à budget : les scripts désignés refusent sur la course v5 — v1

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de travail (classe C), côté exposé. Aucun chiffre de la course, aucun mécanisme.

- **Écrit** le 2026-11-24 vers 16:15Z par la session du côté exposé lancée par Lazar (`session_01Qi7Gr3KR5S1fcJtia9KMrT`, Opus 5.5), branche `barreau8/cote-expose-pieces-lecture-v1`, sous `GO-2026-11-24-36`.
- **Course lue** : `20261123-043944-iib-course-reel`, branche `essai/iib-explo-v8` (`3326499e666c6b2a3670feda6ee5e15ed055170a`), code au commit de lancement `192a429e67b93e9a89d273ba5a4b5c0c61d139f1` (note d'interface v7, question 12).

## Ce qui a été joué

Lecture (1), du dommage, par le script scellé du code de la course, sans aucune modification, sur processeur, dans un arbre de travail détaché au commit `3326499e` :

```
PYTHONPATH=src python scripts/lecture_iib_1_dommage_v1.py --racine . --run-id 20261123-043944-iib-course-reel
```

- Joué à 2026-11-24T16:04:42Z (`date -u`). Script `24b3976b3fd4fb9b3f0922733f64b469af2c4853a40905df528da12ae1384bc1`, module `src/controle_ia/iib/lecture_v1.py` `b8e904c0b40eab4b612d6afa21284cd7e3e562daed983af77b335a9e733fb119`.
- Sortie, mot pour mot : `ARRÊT : donnees/20261123-043944-iib-course-reel/oracle-iib.json absent du résumé scellé de la course` ; code 1 ; rien écrit (arbre inchangé).
- Lecture (2) non jouée : elle refuse sans la sortie scellée de (1) et sa ligne au registre des décisions.

## Pourquoi

1. **Le seul texte qui désigne des scripts pour ces lectures** est l'ordre de la première course : brouillon 3, § 8 (`brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon3.md`, `eed42f07…`) : « lecture (1) par `scripts/lecture_iib_1_dommage_v1.py` … lecture (2) par `scripts/lecture_iib_2_diffusion_v1.py` ». Ils lisent les sorties de l'organisme v1.
2. **L'ordre neuf** (trois pièces attestées par `attestation-ordre-course-lue-additif-1-v1.json`, `8f6b5025…`), **le texte scellé de l'organisme v5** (`c1dc5459…`, sections 10.6 et 13 : aucun module de lecture du dommage ni de la diffusion dans la spécification du code v5) et **l'additif 1 du texte des sondes** (« par leurs propres scripts ») ne désignent aucun autre script.
3. **Les fichiers attendus par `lecture_v1.charger_sorties`** (`donnees/RUN/oracle-iib.json`, `diag/RUN/episodes-iib.json`, `diag/RUN/acceptation-iib.json`, `donnees/RUN/textes-actions-iib.jsonl`) n'existent ni sous le nom de la course ni sous celui de l'étalonnage (`20261122-202132-iib-reel`), où la course v5 verse ses sorties d'évaluation sous d'autres noms et d'autres schémas (vérifié par les noms de fichiers et la seule structure des clés, sans valeur lue).
4. Aucune version v5 de ces scripts ni du module n'existe sur les branches du saboteur relevées (`claude/iib-executante-v1` à `v8`, `claude/iib-reconception-oracle-v1`, `ordre/iib-etalonnage-v5`, `prep/iib-code-v5`, `prep/iib-code-v5-r2`, `prep/iib-tirage-carte-v1`, `essai/iib-explo-v8`).

## Conséquence

Les lectures (1) et (2) ne peuvent pas être jouées sur la course lue par des scripts scellés. Les étapes qui en dépendent attendent : l'extrait des treize états (condition D-12) et l'attestation de la course et de l'oracle (D-15, écrite « après les lectures du dommage et de la diffusion », clé `lectures_jouees_sous_cet_oracle`). Jouer ces lectures demande un code de lecture neuf pour la course v5 (portage des statistiques de la conception d'origine, sections 6.1 et 6.2, sur l'oracle désigné et les fichiers v5) : choix de conception (quel champ de l'oracle désigné tient lieu d'excès, quelles actions sont bornables, source des textes et des comptes de jetons), donc nœud, hors du mandat de cette session.
