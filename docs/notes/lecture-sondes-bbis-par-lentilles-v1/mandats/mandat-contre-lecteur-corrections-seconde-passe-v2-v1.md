# Mandat du contre-lecteur neuf — corrections de la seconde passe (lanceur de la seconde passe v2) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, sous les mots de Lazar « turbo max » et « go tu as
mon mot pour tout » (GO-2026-11-21-63) ; contre-lecture du diff par un agent neuf d'un autre modèle que l'auteur, accord de la mère du
2026-11-21 20:24Z. Tu n'es pas l'auteur du code. Français.

## Ce que tu juges
Les corrections écrites sous le mandat `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-seconde-passe-lentilles-v2.md`
(a2132568…), code au commit `0690d639a` sur `claude/brave-galileo-jhp684`, après la contre-lecture « pas avant »
`contre-lectures/contre-lecture-code-seconde-passe-v1.md` (0c90e0f6…). Question : **chaque correction demandée par cette contre-lecture
(bloquantes B1 et B2, six non bloquantes), et celles du mandat v2 (points 3 à 6), est-elle faite, juste et éprouvée, sans rien changer
d'autre à ce que le texte de lecture v2 scellé exige ? Le lanceur de la seconde passe v2 peut-il être donné à un opérateur ?**
Le développeur s'est arrêté sur une limite d'usage avant d'écrire ses empreintes et sa sortie d'essais ; la session des lentilles les a
écrites par simple relevé (aucun code touché).

## Pièces (vérifie chaque empreinte scellée ; les fichiers de code n'ont pas de compagnon : compare-les par `sha256sum` à
`developpement/empreintes-code-seconde-passe-v2.txt`)
- `CLAUDE.md` ; les deux mandats ci-dessus ; la contre-lecture v1 en entier ;
- sous `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/` : `corrections-seconde-passe-v2-v1.md` (b35d7459…),
  `noeuds-et-precisions-seconde-passe-v2.md` (28bb60df…), `empreintes-code-seconde-passe-v2.txt` (9e4556fb…),
  `sortie-essais-seconde-passe-v2.txt` (939a6674…), `outils/essai-des-essais-corrections-seconde-passe-v1.py` (a8747dbf…),
  `outils/fabrique-lanceur-seconde-passe-v2-v1.py` (a5df3efa…) ; pour la v1 : `noeuds-et-precisions-seconde-passe-v1.md`,
  `conformite-code-au-texte-v2-scelle-v1.md`, `empreintes-code-seconde-passe-v1.txt` ;
- le diff `git diff ffba6bed8 0690d639a -- src tests` : `lanceur_seconde_passe_v2.py` contre `lanceur_seconde_passe_v1.py`,
  `nos_lentilles_v2.py` contre `nos_lentilles_v1.py`, `phrases_v3.py` contre `phrases_v2.py`, `tests/lentilles_sondes_bbis_seconde_passe_jouets_v3.py`,
  `tests/test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py`, `tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v2.py` ;
- les deux correctifs de la première passe que la v2 reprend : `corpus_pagine_v1.py`, `lanceur_v8.py` (vers la ligne 414),
  `cache_tokeniseur_v2.py`, `lanceur_v9.py`, et leurs contre-lectures `contre-lectures/contre-lecture-correctif-pagination-corpus-v1.md`,
  `contre-lectures/contre-lecture-correctif-tokeniseur-act-corpus-v1.md` (1e8c1704…) ;
- le texte de lecture v2 scellé `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (a2bbed7a…), **sans sa liste « Jamais ouverts »**,
  pour les seules sections que touchent les corrections.

## Points à trancher, chacun « tenu » ou « à corriger » avec raison
1. B1 : `corpus_pagine_v1` et `cache_tokeniseur_v2` dans `MODULES`, `MODULES_DIFFERENTS`, cibles du corpus prises de `corpus_pagine_v1`.
2. B2 : pose du cache par `cache_tokeniseur_v2`, essai en ligne et sans clé, `exiger_cache`, cause nommée en cas d'échec de l'essai
   (révision qui a bougé), champs du rapport ; le lanceur v2 importe `lanceur_v7` : la fonction d'essai est-elle reprise fidèlement de
   `lanceur_v9`, et l'écart est-il déclaré ?
3. Les six non bloquantes de la contre-lecture v1 : faites, ou laissées avec une raison acceptable.
4. Les deux nœuds posés à Lazar, codés selon leur option (a) (défaut le 2026-11-23 vers 18:15Z) : conforme à la contre-lecture v1 ; les
   lignes qui en dépendent sont-elles nommées ?
5. L'essai dépendant de l'ordre : la copie neuve en est-elle libre ? L'échec restant dans l'ancien fichier est-il sans lien avec le code ?
6. R5 : chaque garde neuve a un cas sain et un artefact (refus 401 reproduit, arbre paginé à deux pages) ; l'essai des essais
   (36 défaites, 36 vues) couvre-t-il chaque garde neuve ?
7. Rien d'autre n'a changé : aucun module existant réécrit (R12) ; aucune ligne de calcul changée hors des corrections ; aucune clé exposée.
8. Tout autre écart bloquant.
Rejoue `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v2.py`
(environnement `.venv` du dépôt) ; comptes seulement. Aucune requête vers Hugging Face, aucun téléchargement, aucune clé.

## Cloisonnement
Jamais `diag/`, `runs/`, `docs/verdicts/`, branches `calcul/*` `donnees/*` `verdict/*` `lecture/*`, fichiers « consigne-privee » ou
« conception-ii-b » ; aucune sortie, aucun score, aucune table, aucun verdict de l'apprentissage des sondes sur la tâche ni de la lecture
par la lentille publique (`arret.json` compris) ; rien de P3, P3-bis, T0.6, T0.7 hors des textes de lecture. Intitulé interdit vu :
déclaré. Refus d'outil jamais rejoué.

## Rendu
Écris `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-corrections-seconde-passe-v2-v1.md`, scelle-le,
ne committe pas (la session des lentilles committe). Dernier message : verdict « conforme » ou « à corriger » en une à trois lignes ;
points 1 à 8 ; corrections demandées, bloquantes ou non ; empreinte de ton fichier ; expositions.
