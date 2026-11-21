# Mandat — contre-lecture du pilote des entrées de lecture du barreau 5 — v1

Écrit le 2026-11-21 vers 16:40Z par la session de formation du barreau 5 (`session_01Qi7Gr5XKjeM46Bz6Lu9vub`, Opus 5.5), auteur du pilote, au nom de la session mère (accords GO-2026-11-21-63 et -64). Pièce de travail (classe C). Destinataire : un agent neuf, Claude Fable 5.2, contre-lecteur d'une pièce de classe B qu'il n'a pas écrite.

## Objet
Le pilote `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/entrees-de-lecture-v1/preparer_entrees_b5f_v1.py` (dans `/home/user/controle-ia-travail`, branche `formation-b5f/plan-de-marche-v1`, compagnon `.sha256`). Il prépare les entrées de lecture de l'instance de relecture par la seule fonction figée `engagement_v1.preparer_entrees_de_lecture`, puis les fait accepter par `relecture_v1.exiger_entrees`. Il a été joué une fois en local (code 0 ; 30 adaptateurs tenus à l'écart, 9 d'apprentissage, 3 fichiers d'épisodes). Rien n'est poussé avant ta contre-lecture.

Deux modes d'échec à chercher en priorité : **mauvaise source** (une copie, un commit ou un fichier autre que celui que le code de lecture figé lira, par exemple une copie non `-x1` d'une instance relancée, un retirage `-r1` manqué, une famille d'apprentissage mal rattachée à son instance) ; **fuite** (le pilote imprime, écrit ou laisse dans le dossier de sortie quelque chose qui lie un nom opaque à une famille ou à un membre, ou une table, ou un sel).

## Pièces (liste fermée)
1. Le pilote ci-dessus.
2. Le code de lecture figé, extrait à `/tmp/claude-0/-home-user-controle-ia-travail/297a4a07-6190-598e-ba08-f9d65884efdb/scratchpad/arbre-lecture` (commit c76e79169eee337ce66c7d88f62d039e853eebfc) : `src/controle_ia/barreau5_familles/engagement_v1.py` en entier ; dans `relecture_v1.py`, `exiger_entrees`, `exiger_tenseurs_seuls`, les motifs `_ENTREE_*` et la fonction de chargement d'adaptateur (vers la ligne 345) ; dans `lecture_v1.py`, `PLAN_INSTANCES`, `instance_de`, `prefixe_de_copie`, `exiger_copie_lue`, `_familles_formees`, `relance_du_registre` ; dans `formation_v1.py`, les seules lignes 815 à 840 (écriture des adaptateurs).
3. La pièce des sorties : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/sorties-formation-b5f-v1.md` (dépôt principal).
4. Le registre propre de main : `/tmp/claude-0/-home-user-controle-ia-travail/297a4a07-6190-598e-ba08-f9d65884efdb/scratchpad/pieces-additif1/registre-propre-main-25236c16.md` (ligne `GO-RELANCE-FORMATION-B5F` : instances relancées).
5. Les **noms** de fichiers (jamais le contenu) aux sept commits prouvés de la pièce des sorties, par `git -C /home/user/controle-ia-travail ls-tree -r --name-only <commit> -- donnees/` seulement.

## Cloisonnement (à la lettre)
- **Ne lis aucun contenu** de fichier de sortie de la formation : ni `git show` d'un fichier sous `donnees/`, `diag/`, `runs/`, `traces-b5f/`, ni rien sous `…/scratchpad/entrees/` hormis les **noms** de fichiers (`ls`). Jamais `/root/secret-b5f-formation-v1/` (ni liste, ni lecture). Aucun score, aucun épisode.
- Ne joue pas le pilote. Aucun réseau, aucune commande au loueur, aucune clé, aucune poussée, aucun commit.
- Rien d'autre que la liste ci-dessus : ni le texte scellé du barreau 5, ni `brouillons/`, ni fichier dont le nom contient « consigne-privee » ou « conception-ii-b ». Rien sous `/root/.claude/`.
- Au premier refus d'outil ou au moindre doute de périmètre : arrête-toi et dis-le.

## Ce que tu rends
Un rapport `contre-lecture-pilote-entrees-v1.md` dans `/tmp/claude-0/-home-user-controle-ia-travail/297a4a07-6190-598e-ba08-f9d65884efdb/scratchpad/cl-entrees/`, scellé (`PYTHONPATH=/home/user/controle-ia-travail/src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller <fichier>`) : verdict (« conforme », « conforme après ces corrections » avec liste fermée, ou « non conforme ») ; pour chaque constat, ligne du pilote, gravité, correction proposée. Réponse finale : chemin, empreinte, verdict.
