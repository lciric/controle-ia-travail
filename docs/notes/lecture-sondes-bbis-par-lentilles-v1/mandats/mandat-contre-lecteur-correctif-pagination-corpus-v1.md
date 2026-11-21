# Mandat du contre-lecteur neuf — correctif de la pagination de l'arbre du corpus (lanceur v8) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, sous les mots de Lazar « turbo max » et « go tu as
mon mot pour tout » (GO-2026-11-21-63). Tu n'es pas l'auteur du code ; tu es d'un autre modèle que lui. Français.

## Ce que tu juges
Le correctif poussé au commit 11f1cee78 (fusion 6afd9c846) sur `claude/brave-galileo-jhp684`, écrit sous le mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-pagination-corpus-v1.md` (c0c07faa…). Question :
**le lanceur v8 et le module `corpus_pagine_v1` peuvent-ils remplacer le lanceur v7 pour la première passe, sans rien changer à ce que le
texte de lecture v1 scellé exige, et en trouvant réellement un fichier de données dans un arbre paginé de Hugging Face ?**

## Pièces (vérifie chaque empreinte scellée avec `PYTHONPATH=src python -m controle_ia.scellement verifier <chemin>`)
- les deux mandats ci-dessus ; `CLAUDE.md` ;
- `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/notes-correctif-pagination-corpus-v1.md` (6e996045…) ;
- `src/controle_ia/lentilles_sondes_bbis/corpus_pagine_v1.py` (77fb4356…), `lanceur_v8.py` (0bba5d4e…) contre `lanceur_v7.py`,
  `montage_v1.py` (lignes 117 à 210 et 633 à 654) ;
- `tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py`, `tests/lentilles_sondes_bbis_jouets_v8.py` contre la v7,
  `tests/test_lentilles_sondes_bbis_lanceur_v8_v1.py` et les autres copies v8 ;
- `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/` : `fabrique-lanceur-v8-v1.py`,
  `essai-des-essais-corpus-pagine-v1.py`, `sortie-essai-des-essais-corpus-pagine-v1.txt` ;
- `requirements-cpu.txt` ;
- `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (sur `origin/main` si absent), « Plan d'analyse » point 4 et ce qui touche au montage
  et aux essais d'un octet, **sans la liste « Jamais ouverts »**.

## Points à trancher, chacun « tenu » ou « à corriger » avec raison
1. La forme réelle de l'en-tête `Link` de l'API d'arbre de Hugging Face (pagination par curseur) : appuie-toi sur la documentation
   publique ou le code source public de `huggingface_hub` (lecture de pages web publiques permise ; **aucune requête vers l'API de
   Hugging Face**, aucun téléchargement, aucune clé). Le module la lit-il ? La garde du lien (hôte, préfixe) refuse-t-elle à tort un lien
   réel (encodage du nom du jeu, `/` encodé, révision) ?
2. Borne de 100 pages, choix « plus petit chemin de la première page qui porte un fichier » : conformes au texte ? suffisants pour un arbre
   de la taille de `fineweb-2` jusqu'à `data/cmn_Hani/train` ?
3. Lanceur v8 = v7 à ce seul changement près ; `MODULES` et contrôle des empreintes contre la fiche ; aucune clé exposée.
4. Les essais prouvent-ils le défaut (artefact qui reproduit l'arrêt de l'ancien code) et la correction (R5) ? L'essai des essais tient-il ?
5. `requests==2.34.2` : version publiée, compatible avec le reste ?
6. Tout autre écart bloquant.
Rejoue `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py tests/test_lentilles_sondes_bbis_lanceur_v8_*.py`
(environnement : `python3 -m venv` hors du dépôt ou `.venv` existant, `requirements-cpu.txt`, torch processeur) ; comptes seulement.

## Cloisonnement
Jamais `diag/`, `runs/`, `docs/verdicts/`, branches `calcul/*` `donnees/*` `verdict/*`, fichiers « consigne-privee » ou « conception-ii-b » ;
aucune sortie, aucun score, aucune table, aucun verdict de l'apprentissage des sondes sur la tâche ni de la lecture par la lentille publique
(`arret.json` compris) ; rien de P3, P3-bis, T0.6, T0.7 hors des textes de lecture. Intitulé interdit vu : déclaré. Refus d'outil jamais rejoué.

## Rendu
Écris `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-correctif-pagination-corpus-v1.md`, scelle-le, ne
committe pas (la session des lentilles committe). Dernier message : verdict « conforme » ou « à corriger » en une à trois lignes ; points
1 à 6 ; corrections demandées, bloquantes ou non ; empreinte de ton fichier.
