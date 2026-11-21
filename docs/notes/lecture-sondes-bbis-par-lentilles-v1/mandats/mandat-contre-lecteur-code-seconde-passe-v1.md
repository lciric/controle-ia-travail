# Mandat du contre-lecteur neuf — code de la seconde passe (nos lentilles R et S) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, sous les mots de Lazar « turbo max » et « go tu as
mon mot pour tout » (GO-2026-11-21-63 ; note `docs/notes/neuron-lens-v1/mot-lazar-turbo-seconde-passe-2026-11-21-v1.md`). Tu n'es ni
l'auteur du texte ni celui du code ; tu es d'un autre modèle que le développeur. Pièce jugée : classe B (instrument). Français.

## Question
Le code de la seconde passe, figé au commit `ffba6bed8fa68e702db33ad68bb82323fdc2ba7e` (notes jusqu'à `a7df1266`), écrit sous le mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-seconde-passe-lentilles-v1.md` (4a3cf535…), applique-t-il
**exactement** la section « Code neuf » du texte de lecture v2 scellé, avec ses gardes, sa statistique, sa règle de départage, ses phrases
gelées et tous ses essais, sans règle nouvelle ? Verdict : « conforme », « conforme sous corrections non bloquantes » ou « pas avant » (avec
les corrections bloquantes).

## Pièces (vérifie chaque empreinte : `PYTHONPATH=src python -m controle_ia.scellement verifier <chemin>` ; pour le code sans compagnon,
`sha256sum` contre `developpement/empreintes-code-seconde-passe-v1.txt`)
- `CLAUDE.md` ; le mandat du développeur ci-dessus et celui qu'il reprend (`mandat-developpeur-deux-passes-lentilles-v1.md`, 0a9517ea…).
- Le texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (a2bbed7a…), **sans sa liste « Jamais ouverts » (lignes 1320 à 1343 environ)** :
  « Code neuf », « Métrique », « Plan d'analyse », « Critères », « Liste d'arrêt », et ce qu'ils renvoient. Mots de Lazar qui fixent sa
  lecture : `docs/notes/neuron-lens-v1/mot-lazar-noeuds-n12-n17-et-brouillon6-2026-11-20-v1.md`, `mot-lazar-regle-departage-seconde-passe-2026-11-19-v1.md`,
  `mot-lazar-declaration-verdict-seconde-passe-2026-11-20-v1.md`, `mot-lazar-phase-exploratoire-et-option-c-2026-11-20-v1.md`.
- Code, `src/controle_ia/lentilles_sondes_bbis/` : `constantes_v2`, `statistiques_v4`, `nos_lentilles_v1`, `lecture_entree_v1`,
  `comparaisons_lentilles_v1`, `reproduction_v1`, `audits_v2`, `phrases_v2`, `montage_v2`, `lanceur_seconde_passe_v1` ; et ce qu'ils
  réemploient (`statistiques_v3`, `entrees_v3`, `lanceur_v7`/`lanceur_v8` pour le schéma des messages d'arrêt, `corpus_pagine_v1`).
- Essais : `tests/test_lentilles_sondes_bbis_seconde_passe_*_v1.py`, `tests/lentilles_sondes_bbis_seconde_passe_jouets_v1.py` et `_v2.py`.
- Notes, `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/` : `notes-developpement-seconde-passe-v2.md`,
  `conformite-code-au-texte-v2-scelle-v1.md`, `table-essais-seconde-passe-v1.md`, `noeuds-et-precisions-seconde-passe-v1.md`,
  `empreintes-code-seconde-passe-v1.txt`, `sortie-essais-seconde-passe-v1.txt`, `outils/essai-forme-archive-torch-save-v1.py` et sa
  sortie, `outils/essai-des-essais-seconde-passe-v3.py`, `outils/alterations-seconde-passe-*-v1.py`.
- Le correctif de la pagination, désormais sur la branche (contre-lu conforme : `contre-lectures/contre-lecture-correctif-pagination-corpus-v1.md`).

## Points à trancher en plus de la conformité générale
1. **Nœud N-dev-1 (corpus des jetons gardés)** : `corpus_pagine_v1.cibles_corpus(voisin, transport, borne=…)` est maintenant présent.
   `montage_v2` le prend-il correctement ? Le lanceur de la seconde passe contrôle-t-il son empreinte (liste des modules contre la fiche) ?
   Faut-il, oui ou non, une version neuve du lanceur de la seconde passe pour qu'il puisse partir ? Dis le changement minimal exact.
2. Les nœuds N-dev-2 à N-dev-10 : chacun « tenu », « à corriger » ou « nœud pour Lazar » (si le texte ne tranche pas et que le choix
   change une lecture), avec raison.
3. L'écart N-dev-6 (extraction en flux comparée à `torch.load` plutôt qu'à `lenses.load_fits`) : acceptable sans voisin versé ?
4. Gardes : chaque garde a-t-elle cas sain et artefact (R5) ? Les trois altérations non vues sont-elles vraiment équivalentes ?
5. Messages d'arrêt : même schéma que `lanceur_v7` (GO-2026-11-20-56, GO-2026-11-21-06) ; égalité de la relecture de contrôle de
   l'audit écrite sans arrêt.
6. Statistique corrigée et départage par identifiant de jeton croissant (GO-2026-11-19-92) : exacts ?
7. Phrases gelées : conformes mot pour mot au texte ?
Rejoue au moins les cinq fichiers d'essais de la seconde passe (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src`, environnement
`/home/user/controle-ia-travail/.venv/bin/python` ou un venv de ton bloc-notes) ; comptes seulement.

## Cloisonnement
Jamais `diag/`, `runs/`, `docs/verdicts/`, branches `calcul/*` `donnees/*` `verdict/*`, fichiers « consigne-privee » ou « conception-ii-b »,
`brouillons/ii-b-saboteur-budget-v1/` ; aucune sortie, aucun score, aucune table, aucun verdict de l'apprentissage des sondes sur la tâche
ni de la lecture par la lentille publique (`arret.json` compris) ; rien de P3, P3-bis, T0.6, T0.7 hors des textes de lecture, de l'étape B,
du bras d'attaque, du saboteur à budget. N'exécute pas `verifier-arbre` (il affiche des chemins de `runs/`). Aucun téléchargement, aucune
requête vers Hugging Face, aucune clé lue. Intitulé interdit vu : déclaré. Refus d'outil jamais rejoué.

## Rendu
Écris `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-seconde-passe-v1.md`, scelle-le, ne committe
pas. Dernier message : verdict en une à trois lignes ; points 1 à 7 ; corrections bloquantes et non bloquantes, chacune avec fichier et
ligne ; nœuds pour Lazar ; empreinte de ton fichier. Si ta mémoire de travail ne suffit pas, dis-le au départ et arrête-toi proprement sur
une note partielle scellée.
