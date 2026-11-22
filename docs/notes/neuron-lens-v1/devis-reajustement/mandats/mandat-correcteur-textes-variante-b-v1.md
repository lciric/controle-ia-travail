# Mandat du correcteur neuf — brouillons 2 des deux textes de la variante B du réajustement — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-22, sous GO-2026-11-22-05 (réajustement) et le mot de
Lazar ed47f2e3… (autonomie). Pièces de classe A. Français.

## Ce que tu fais
Tu écris, **mot pour mot d'après les corrections demandées**, les brouillons 2 des deux textes, sous
`docs/notes/neuron-lens-v1/devis-reajustement/textes-variante-b/` :
- `statut-seconde-mesure-reajustement-v1-brouillon2.md`, depuis le brouillon 1 (561e8ac2…), avec les corrections S-1 à S-7 ;
- `plan-lecture-seconde-course-reajustement-v1-brouillon2.md`, depuis le brouillon 1 (ed802f8d…), avec P-1 à P-12 ;
- la déclaration à part que demande S-4 : `declaration-redacteur-textes-variante-b-v1.md` ;
- s'il faut un extrait scellé du verdict d'identité (P-3), sa **forme** seulement (gabarit), jamais son contenu.
Les corrections sont celles de la contre-lecture
`docs/notes/neuron-lens-v1/devis-reajustement/textes-variante-b/contre-lecture-textes-variante-b-opus-v1.md` (a92149e8…), dont tu suis le
texte exact quand elle en donne un. Chaque brouillon 2 porte en tête un bloc « Différences avec le brouillon 1 », une ligne par
correction (identifiant, ce qui change, lignes), et la liste de celles que tu n'as pas pu faire telles quelles, avec la raison (nœud).
Les brouillons 1 restent tels quels (R12). Ne change rien d'autre.

## Ordre de lecture
`CLAUDE.md` ; le mot de Lazar ; la contre-lecture en entier ; les deux brouillons 1 ; puis, pour vérifier une source citée, les
documents qui font foi qu'ils citent (devis v9, critère v8, texte gelé, son addendum, plan de la tranche v2), **seulement aux lignes
utiles**. Tu ne lis pas le verdict du 18 ni l'accord de Lazar sur ce verdict.

## Ce que tu ne fais pas
Rien ne se lance ni ne se dépense ; aucune requête réseau hors git. Jamais `diag/`, `runs/`, `docs/verdicts/`, branches `donnees/*`,
`calcul/*`, `verdict/*`, `lecture/*` ; rien de l'apprentissage des sondes sur la tâche, de P3, P3-bis, T0.6, T0.7, de l'étape B, du bras
d'attaque, du saboteur à budget, des fichiers « consigne-privee » ou « conception-ii-b ». Aucune hypothèse ni revendication neuve.

## Commits et rendu
Arbre de travail isolé : `git fetch origin claude/brave-galileo-jhp684 && git checkout --detach FETCH_HEAD` ; poussée
`git push origin HEAD:claude/brave-galileo-jhp684` après `git fetch origin claude/brave-galileo-jhp684 && git merge --no-edit FETCH_HEAD` ;
jamais de poussée forcée ; aucun nom de modèle ; lignes de fin `Co-Authored-By: Claude <noreply@anthropic.com>` et
`Claude-Session: https://claude.ai/code/session_01Qi7Gr3vedYVukbyqBbHd7z`. Fichiers scellés. Rendu : verdict en une à trois lignes ;
chemins et empreintes ; table « correction → fait / non fait (raison) » ; nœuds ; expositions.
