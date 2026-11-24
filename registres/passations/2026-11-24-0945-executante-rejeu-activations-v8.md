# Passation — exécutante v8 du rejeu des activations du saboteur, voie (A), phase 1 — 2026-11-24 09:45Z

Pièce de travail (classe C). Session session_01Qi7Gr7RUpB7HCrA9DPfsR9 (Opus 5.5, effort élevé). Mère : session_01Qi7Gr3Ggccg85kjmP654WC. Branche : `claude/iib-executante-v8`. Reprend l'exécutante v7 (`claude/iib-executante-v7`, 8aee9bd5), injoignable. Accord : GO-2026-11-24-06 (devis v2, 11 USD).

## Fait (phase 1, sans machine, 0 USD)
- Lu : passation, compte rendu et faits de l'exécutante v7 ; mandat v2 ; devis v2 et sa vérification finale R2 ; R-5244 à R-5256 ; notice d'emploi v6 de la passe (écrite pour l'exécutante). Code de la passe non ouvert ; aucune sortie, aucun score lus.
- Amorce écrite : `src/controle_ia/rejeu_activations_voie_a_v1.py` (session et machine, bibliothèque standard), essais `tests/test_rejeu_activations_voie_a_v1.py` (52 passent), ordre de lancement à remplir et notice sous `docs/notes/rejeu-activations-saboteur-voie-a-v1/amorce-executante-v8/`.
- Gardes : minuterie dure (passe coupée par son PID à 4 h, destruction par l'identifiant à 4,5 h, plus une minuterie de secours avant le clonage) ; refus du départ si les activations ne s'écrivent pas (sonde d'écriture, vérification des entrées et essai à blanc en code 0, rapport de l'essai donnant une taille positive aux trois archives d'activité brute) ; garde « activations écrites » après la passe ; rapatriement prouvé (clone séparé, commit, inventaire scellé, empreintes, aucun fichier de trop) ; destruction par l'identifiant de la fiche seulement ; surveillance externe (horloge 4,5 h, dépense tout compris coupée à 9,60 USD) ; passe sans secret.
- Contre-lecture classe B par un agent neuf Sonnet : « à corriger » (3 bloquants, 7 majeurs) ; corrigé ; vérification 1 : tout fermé sauf un défaut neuf (fiche sans identifiant), corrigé avec la destruction sans relevé après trois échecs ; vérification 2 : voir le compte rendu à la mère.
- Inventaire Vast en lecture seule : quatre intouchables seulement (58936096, 58936099, 58936100, 60988826), aucune machine à moi ; crédit 19,84 USD. Recherche d'offres en lecture seule : une A100 SXM4 80 Go conforme au filtre (1,1953 USD/h stockage compris).
- Outil de location 1.11.0 installé dans le bloc-notes (`…/scratchpad/vast11/bin/vastai`).

## Reste (préalables de la phase 2, hors de mon ressort)
1. GO-2026-11-24-06 est de type « dépense » : le crochet `.claude/hooks/garde_calcul.py` refusera toute création (type « calcul » exigé).
2. La garde P0 de la passe exige que la ligne d'accord porte l'empreinte entière du devis ; la ligne porte « 9a4a794c… ».
3. Ordre de lancement à remplir après l'additif 2 (entropie F-3, extrait D-13, entrées de la course), contre-lire, sceller, committer au commit de lancement avec ce module, l'extrait, le registre propre et le bordereau du code.

## Réserves
- `verifier-arbre` de `main` : 9 défauts préexistants (passations d'autres sessions), sans lien avec ce travail. Suite complète des essais du dépôt non jouée ici (dépendances non installées) ; seuls les 52 essais de l'amorce l'ont été.
- Dépense « lue » = baisse du crédit du compte : une dépense parallèle sur le même compte peut couper tôt (sens prudent).
- Réserves de la contre-lecture acceptées : voir la notice.

## Prochaine action
Attendre « feu, additif 2 scellé » de la mère ; puis, dans l'ordre de la notice : offres, `creer --verifier-seulement`, `creer`, `surveiller` détaché, `rapatrier`, `detruire`, registres.

## Machines, serveurs, tâches
Aucune machine ni serveur à moi. Aucune tâche de fond. Aucune tâche planifiée.
