# Mandat du développeur neuf — corrections après la contre-lecture du lanceur v4 et de la commande v9 — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-22, sous GO-2026-11-22-05. Toutes les règles du mandat
`docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-developpeur-lanceur-v4-commande-v9-reajustement-v1.md` (6ed54244…) valent
pour toi (rien ne se lance ni ne se dépense, aucune clé lue, cloisonnement, R12, commits), sauf là où ce mandat les complète. Français.

## Ce que tu corriges
La contre-lecture `docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/contre-lecture-lanceur-v4-commande-v9-v1.md` (2b223595…),
par versions neuves seulement :
- **C-1 (bloquante)** : une attente entre les essais de copie d'un même fichier (60 s puis 300 s, ou ce que la contre-lecture
  dit), avec un essai sain et un essai artefact ; module de rangement en version neuve, banc d'altérations rejoué, essai à blanc refait
  (liste du dépôt réduit neuve), commande en version neuve (`commande-b-beta-v10.md`) au nom de la nouvelle liste ; lanceur en version
  neuve s'il change.
- **Non bloquantes C-2 à C-8** : fais-les si elles tiennent dans la même version (C-2, C-3, C-4, C-5, C-6 ; C-7 et C-8 au moins écrites
  en réserve dans la commande) ; sinon, raison écrite.
- **N-2** n'est pas à toi : la mère le tranche ; ne change pas son comportement.

## Lecture
`CLAUDE.md` ; le mandat cité ; la contre-lecture en entier ; le rendu du développeur précédent
(`developpement-v4/rendu-developpement-v4-v1.md`), ses passations et sa table des items ; puis le code et la commande qu'ils citent.

## Rendu
Arbre isolé (`git fetch origin claude/brave-galileo-jhp684 && git checkout --detach FETCH_HEAD` ; poussée `git push origin HEAD:claude/brave-galileo-jhp684`
après fetch et merge ; jamais de poussée forcée). Dans `developpement-v4/` : `corrections-contre-lecture-lanceur-v4-v1.md` (table
« correction → fait / non fait → essai »), empreintes neuves (`empreintes-lanceur-v4-v2.txt`), scellés. Dernier message : verdict ;
commit ; fichiers et empreintes ; comptes des essais ; nœuds ; expositions.
