# Attestation de séparation — versant honnête de l'essai « jumeau contre jumeau » (v1)

- **Accord** : GO-2026-11-24-17. **Mandat** : session mère du compte 01Qi7 (`session_01Qi7Gr3Ggccg85kjmP654WC`).
- **Écrite par** : la session habilitée du coffre du compte 01Qi7 (`session_01Qi7Gr4qGhdorfC7VG4KA4b`, Opus 5.5, effort élevé), le 2026-11-24 vers 11:10Z (`date -u`). Habilitation : mot de Lazar tapé le 24 novembre vers 10:50Z, à inscrire au registre par la mère. Exclue à vie de toute conception de moniteur, de sonde ou de saboteur, et de tout rôle aveugle.
- **Classe** : C (application d'une pièce de choix scellée ; aucune conception). Aucune dépense, aucun appel externe, rien sur `main`.
- **Forme** : faits seulement (oui, non, indéterminé), tailles, chemins, empreintes. Aucun contenu de coffre ci-dessous. Lisible par la mère.

## Pièces et têtes de branche lues

| pièce | lieu (tête) | empreinte sha256 |
|---|---|---|
| pièce de choix des modes tenus à l'écart, hors section 4 | `coffre/choix-modes-tenus-a-l-ecart-v1` (`39839826e5`), `choix-v1/piece-de-choix-modes-tenus-a-l-ecart-v1.md` | `83eb1fa85afd5c32d66f5fd78ee958389d2310b700457a764747177a00ddaec4` |
| règle d'ouverture de ce coffre | même branche, `REGLE-D-OUVERTURE-v1.md` | voir son `.sha256` |
| banque des 64 tâches d'évaluation | `main` (`6172b24815`), `donnees/20261007-082440-t05-extraction/taches-evaluation.json` | `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` ; empreinte d'ensemble (identifiants triés, joints par un saut de ligne, sans saut final) `a18abadfe1044e4935a404a83650a3b5ccab77dbbbf3da82eaf10611c6b39ea3`, recalculée |
| banque de réserve (32) | `main`, `donnees/20261007-082440-t05-extraction/taches-entrainement.json` | `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` |
| pilote de l'environnement (60) | `main`, `donnees/t05-pilote-v1/taches-pilote-60-v1.json` | `287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa` |
| premier test boîte blanche (60) | `main`, `runs/20261019-230011-p3-reel/manifeste.json`, clés « tache/… » | `3f21774ca2a740e0…` |
| instruction opérationnelle du versant honnête | `main`, `docs/notes/dossier-entretien-2026-12-01-v1/instruction-b6-versant-honnete-jumeau-v1.md`, § 1 | `df6d6dfe1cd78403f100b97dcebc2eccbad24934045ebe66bd2cc841a704e6d8` |
| index du scellement 2 (lieu de la pièce 4) | `main`, `registres/index-scellement-2-familles-aveugles-v3.md` | `cde486b03a81aeb33d5a05a3355479fe917077c84cd5a044e66a6b7abb47d893` |
| coffre de la famille aveugle de réserve du cycle 2 | `claude/scellement-2-famille-reserve-cycle-2-v1` (`5d6b7a2aa2`), pièces 2 à 5 en v1 et v2, pièce 6 v2 | empreintes égales à celles de l'index v3 (voir `sortie-intersection-v1.txt`) |
| devis de la banque d'épisodes de cette famille, v3 (en clair) | `main`, `docs/notes/devis-famille-reserve-cycle-2-v1/devis-banque-d-episodes-famille-reserve-cycle-2-v3.md`, lignes 473 à 478 | `1ab6eb4b1134d66384756a83535f031e4f4b6bfda317f362055448cf335c9804` |

Programme : `attestation-v1/intersection_identifiants_v1.py` (`288a5254…`) ; sortie complète, tailles seulement : `attestation-v1/sortie-intersection-v1.txt` (`02498a6f…`).

## Réponses

| n° | question | réponse | appui (tailles, chemins, empreintes) |
|---|---|---|---|
| 1 | Les 64 tâches d'évaluation, qui incluent les 60 du premier test, toujours séparées de la famille tenue à l'écart, au sens du § 3.2 de la pièce de choix ? | **oui** | Verdict du § 3.2 : « séparée » pour les 64 et pour les 60, confiance 0,8, sous trois conditions. Rien n'a changé depuis : fichiers de tâches identiques sur la tête de `main` ; 64 identifiants distincts, empreinte d'ensemble `a18abadf…` retrouvée ; 60 du premier test incluses dans les 64 et égales aux 60 du pilote ; intersection avec la réserve de 32 : 0. Aucune branche ni ligne de registre postérieure à la pièce de choix (06:43Z) n'attribue de banque de tâches à la famille choisie (relevé de toutes les branches du dépôt à 11:06Z). La lecture stricte du § 3.2 reste ouverte pour Lazar. |
| 2 | Condition 1 (épreuve à blanc, instrument, pilote et lecture de la famille choisie tirés hors des 96) tenue à ce jour ? | **oui** | Aucune épreuve à blanc, aucun instrument de vérité du dommage, aucun pilote de capacité ni aucune lecture de la famille choisie n'existe au dépôt à 11:06Z : la condition tient parce que rien n'a encore été tiré. Limite : la suite est confiée (GO-2026-11-24-09, R-5250) à la session habilitée au mode tenu à l'écart d'un autre compte (`session_016QhUrtEEhGywC23WKoNEdL`), dont le travail non poussé échappe à ce relevé. |
| 3 | Condition 2 (aucune sortie de l'essai « jumeau contre jumeau » dans l'instrument de la famille) tenue à ce jour ? | **oui** | L'essai n'a encore produit aucune sortie (aucun manifeste ni dossier de course de cet essai sur aucune branche à 11:06Z ; son départ attend la présente attestation). L'instrument de la famille n'existe pas encore. |
| 4 | Condition 3 : les 64 et les 60 disjointes de la famille aveugle de réserve du cycle 2 (pièce 4) ? | **indéterminé** | Coffre trouvé : `claude/scellement-2-famille-reserve-cycle-2-v1` (`5d6b7a2aa2`), pièce 4 v2 `b8d9febb…` (fait foi), v1 `9938abfe…`. Intersection calculée par programme sur neuf pièces de ce coffre (pièces 2 à 5 en v1 et v2, pièce 6 v2) : **0** avec les 64, **0** avec les 60, **0** avec les 32 ; ces pièces portent **0** identifiant de tâche. Donc : disjointes aujourd'hui par identifiants, parce qu'aucune banque n'est encore attribuée à cette famille. Non garanti pour la suite : le choix de sa banque reste ouvert au devis v3 en clair (`1ab6eb4b…`, lignes 473 à 478, « point 4 »), et aucune ligne de `registres/go.md` ni de `registres/decisions.md` ne le tranche à 11:06Z. Le « oui » demande que ce choix soit tranché hors des 96 de la banque initiale. |

## Accès à consigner par la mère (N-057, point 5 : qui, quand, pourquoi)

- **Qui** : `session_01Qi7Gr4qGhdorfC7VG4KA4b`, session habilitée du coffre du compte 01Qi7, Opus 5.5 ; ne conçoit aucun moniteur, aucune sonde, aucun agrégateur.
- **Quand** : le 2026-11-24, de 10:58Z à 11:06Z environ.
- **Pourquoi** : condition 3 de la pièce de choix des modes tenus à l'écart (attestation pour GO-2026-11-24-17).
- **Lu au coffre du cycle 2** : les neuf pièces passées au programme (identifiants seulement, tailles affichées), et, pour savoir comment la pièce 4 v2 définit sa matière, ses lignes 9 à 20 et les lignes repérées par recherche de mots (tâche, banque, pilote, tirage, disjoint, réserve, 60, fichier), soit une vingtaine de lignes ; la pièce 6 v2 (en clair) par la même recherche. Rien d'autre.

## Réserves

1. Le relevé « à ce jour » couvre les branches du dépôt à 11:06Z, pas le travail non poussé d'autres sessions.
2. Routine de reprise non faite en entier (session de coffre sans calcul, sans clés) : ni tests, ni inventaire d'instances.
3. Section 4 de la pièce de choix non lue (réservée à Lazar et au gardien).
