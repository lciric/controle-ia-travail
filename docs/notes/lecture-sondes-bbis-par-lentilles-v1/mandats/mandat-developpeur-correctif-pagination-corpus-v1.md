# Mandat du développeur neuf — correctif de la pagination de l'arbre du corpus (première passe) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, à la demande de la mère
(session_01Qi7Gr3eYmAhDEJzqLgWcv1, message direct de 16:21Z), sous les mots de Lazar « on passe au turbo max pour boucler les billets
au plus vite » et « go tu as mon mot pour tout » (GO-2026-11-21-63 ; note `docs/notes/neuron-lens-v1/mot-lazar-turbo-seconde-passe-2026-11-21-v1.md`).
Pièce de travail (classe C). Le code produit est de **classe B** : contre-lecture par un agent neuf d'un autre modèle.

## Le défaut, tel que la mère le relaie (tu ne lis aucune sortie de course)
L'opérateur de la première passe s'est arrêté, avant tout téléchargement long, sur l'arrêt nommé du code
« jeu de données de la tranche zh : aucun fichier de données dans l'arbre ». Cause relevée par lui sur des métadonnées publiques :
l'arbre du jeu `HuggingFaceFW/fineweb-2` à la révision `af9c1333` (recursive=true) est **paginé** (1 000 entrées par page, lien « next »
dans l'en-tête `Link`), la première page ne porte que des dossiers, et `cibles_corpus` (`src/controle_ia/lentilles_sondes_bbis/montage_v1.py`,
lignes 633 à 654) ne lit que la première page. Le dossier attendu des données est `data/cmn_Hani/train`. Autre relevé : `requests`
manque à `requirements-cpu.txt`.

## Le travail — le plus petit correctif, rien d'autre
1. Lis `CLAUDE.md`, puis le mandat du développeur des deux passes
   (`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-deux-passes-lentilles-v1.md`, 0a9517ea…) : **ses règles
   de cloisonnement, de lecture et de travail valent pour toi**. Lis du texte de lecture v1 scellé (`prereg/lecture-sondes-bbis-par-lentilles-v1.md`,
   ca5066d7…) ce qu'il dit du montage, des essais d'un octet et du corpus (sans la liste « Jamais ouverts ») : le correctif ne doit rien
   changer à ce que le texte exige.
2. Un module **neuf** (R12 ; aucun module existant n'est réécrit) : `src/controle_ia/lentilles_sondes_bbis/corpus_pagine_v1.py`, qui
   fournit une version de `cibles_corpus` qui trouve un fichier de données même quand l'arbre est paginé. Deux voies, choisis et
   justifie dans ta note : (a) suivre la pagination (lien `next` de l'en-tête `Link`, ou paramètre de curseur), ce qui demande d'étendre
   le transport sans toucher `TransportRequests` (sous-classe ou transport neuf dans ton module) ; (b) demander l'arbre du seul dossier
   des données, si le chemin peut être tiré de la provenance ou du code voisin **sans règle nouvelle**. Borne le nombre de pages (arrêt
   nommé au-delà), garde la même phrase d'arrêt quand aucun fichier n'est trouvé, et ne journalise ni n'expose jamais la clé.
3. Un lanceur **neuf** `lanceur_v8.py`, copie fidèle de `lanceur_v7` (commit cc7f4576) où seul l'appel à `cibles_corpus` passe par ton
   module, et où `MODULES` (empreintes contrôlées contre la fiche) inclut le module neuf. Aucun autre changement ; si tu en vois un
   nécessaire, nœud écrit.
4. Essais neufs `tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py` (R5) : réponse paginée fabriquée (première page de dossiers
   seulement, fichier en deuxième page) → fichier trouvé ; même réponse lue par l'ancien `cibles_corpus` → l'arrêt nommé (artefact qui
   prouve le défaut) ; arbre sans fichier sur toutes les pages → arrêt nommé ; pages sans fin → arrêt à la borne ; plus les essais
   du lanceur v7 rejoués contre le v8 là où ils s'appliquent (fichier neuf, pas de réécriture d'anciens essais).
5. `requirements-cpu.txt` : ajoute `requests` (version épinglée comme les autres lignes, si elles le sont).
6. Essais : le paquet entier (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q tests/test_lentilles_sondes_bbis_*.py`,
   plus de vingt minutes) ; comptes seulement.
7. Note scellée `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/notes-correctif-pagination-corpus-v1.md` : défaut, voie
   choisie, fichiers et empreintes, essais, nœuds.

## Coexistence
Un autre développeur (seconde passe) travaille en même temps dans `/home/user/controle-ia-travail` : **tu travailles dans ton arbre de
travail isolé**, tu ne touches à aucun de ses fichiers (`statistiques_v4`, `montage_v2`, `audits_v2`, `phrases_v2`, `nos_lentilles_v1`,
`lecture_entree_v1`, `comparaisons_lentilles_v1`, `reproduction_v1`, lanceur de la seconde passe, essais `*seconde_passe*`). Pour pousser :
`git fetch origin claude/brave-galileo-jhp684 && git merge --no-edit FETCH_HEAD` puis `git push origin HEAD:claude/brave-galileo-jhp684`
(quatre essais au plus ; jamais de poussée forcée). Aucun identifiant ni nom de modèle dans les commits ; chaque message finit par
`Co-Authored-By: Claude <noreply@anthropic.com>` et `Claude-Session: https://claude.ai/code/session_01Qi7Gr3vedYVukbyqBbHd7z`.

## Interdits
Aucun téléchargement de modèle, de lentille ou de corpus, aucune requête réseau vers Hugging Face (tout sur réponses fabriquées) ; aucune
clé lue ; branches `calcul/*`, `donnees/*`, `verdict/*` jamais récupérées ; `diag/`, `runs/`, `docs/verdicts/` jamais lus ; tout intitulé
interdit vu : arrêt sur ce point et déclaration. Refus d'outil jamais rejoué. Tu n'inscris aucune ligne de registre et n'écris pas la fiche.

## Rendu
Verdict en une à trois lignes ; commit poussé ; fichiers neufs et changés avec empreintes ; essais (nombre, réussis, échoués) ; nœuds ;
expositions ; liste des fichiers à donner au contre-lecteur.
