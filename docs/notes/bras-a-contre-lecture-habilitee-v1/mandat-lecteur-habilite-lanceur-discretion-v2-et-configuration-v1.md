# Mandat court (classe C) — lecteur habilité — lanceur de l'étape de discrétion v2 et sa configuration scellée — v1

Écrit par la session mère le 2026-11-22 vers 21:45Z, sur la demande de la session du bras A (texte v2, brouillon 55, cc55502a…, section 13.2, ligne « restes de la case du module des cinq moniteurs », restes (b) et (c)). Ouvert sur un agent Opus neuf habilité. **L'accès est inscrit au registre des décisions par la mère avant toute lecture.**

## Ce que tu fais
- (b) Sur la branche `claude/bras-a-habilite-developpeur-v1`, commit `848c17649`, dans un arbre de travail à toi (`git worktree add` dans ton bloc-notes, jamais dans le dossier de la mère) : donner le chemin et l'empreinte du lanceur de l'étape de discrétion en version 2, et ton mot sur sa réserve C9 (levée, ou non, et pourquoi en une ligne sans interne).
- (c) Écrire la configuration scellée de ce lanceur qui fixe le dossier du fichier des scores par unité (proposé : `donnees/bras-a-v2-discretion/rangs-par-unite`, disjoint de la sortie) et qui cite l'empreinte du texte scellé du bras A ; cette empreinte n'existe qu'après le scellement de 00:05Z : laisse un marqueur unique `EMPREINTE_TEXTE_V2_BRAS_A` que la mère remplacera, et un essai qui refuse la configuration tant que le marqueur reste (cas sain et artefact). Version neuve, jamais d'écrasement.

## Ce que tu rends
- un rapport interne, versé sur la branche `claude/bras-a-habilite-developpeur-v1` (fichier neuf, compagnon `.sha256`, commit et poussée sur cette seule branche) ;
- une pièce sans interne, `docs/notes/bras-a-contre-lecture-habilitee-v1/lanceur-discretion-v2-et-configuration-sans-interne-v1.md` : en-tête (titre, heure `date -u`, mandat) ; chemin, commit et empreinte du lanceur ; réserve C9 levée ou non ; chemin, commit et empreinte de la configuration et de ses essais ; nombre d'essais passés sur le total ; chemin, commit et empreinte du rapport interne.

## Interdits
Aucun appel payant ; aucune clé ; rien d'autre que les fichiers nécessaires au lanceur et à sa configuration. Aucune ligne de code, aucun score, aucun nom de champ interne dans la pièce sans interne. N'ouvre rien sous `archives-reponses-modeles/`, aucun fichier « consigne-privee » ni « conception-ii-b », ni la branche `lot/compte-4-v1`, ni aucune sortie de course. N'écris rien sur `main` hors de la pièce sans interne, ne la committe pas : la mère scelle et verse. La configuration (c) sera contre-lue par un autre agent avant usage.
