# Passation — développeur du code des sondes v2 (2026-11-23, 06:38Z)

- **Session** : session_013QMaykMZAR8jYKempS4coQ, fille de la mère session_013QMayjbmQUdDuDs2S3i3XD. Écrite sur demande de la mère (GO-2026-11-23-09). Scellée, jamais réécrite. Aucun résultat, aucun secret.

## Mandat
Écrire le code des sondes de la boîte blanche v2 (accord GO-2026-11-22-126, décision 2), en restant **aveugle** : consigne `docs/procedures/sondes-v2/consigne-developpeur-code-sondes-v1.md` (`60aef942…`), erratum 1 (`e9c8cde1…`), erratum 2 (`1e6ebdbe…`), au service du texte scellé `prereg/diagnostics-prealables-sondes-v1.md` (`e8dca00b…`). Données fabriquées seulement, aucune dépense.

## Fait
- Paquet `src/controle_ia/sondes_v2/` (magasin, formes closes, lecture, statistiques des errata, copies sans torch, épreuve plantée v3, programme) et essais `tests/test_sondes_v2_*.py` : 128 passent, 1 sauté (essai lent, passé à part).
- Contre-lecture par Sonnet (`contre-lecture/sondes-v2-code-v1`, `d4abb3e94`), corrections, vérification : conforme (`3f0651812`) ; réserve 8 c levée.
- Demande de fusion n° 78 **fusionnée sur main**. Fiches de code scellées : `docs/procedures/sondes-v2/fiche-code-sondes-v2-v1.md`, `-v2.md`, `-v2-erratum-1.md` (`b4c613fe…`).
- Versement du bloc-notes : `docs/notes/sondes-v2-developpeur-v1/versement-bloc-notes-2026-11-23/` (23 fichiers, chacun avec son compagnon `.sha256`) : copies des errata et de la pièce de format lus, journaux et rapports de fumée, essais de profilage, journaux d'essais.

## Reste
- Trancher E-5, Q12, E-1 à E-8 (concepteur ; voir `src/controle_ia/sondes_v2/LISEZ-MOI.md`). Toute réponse contraire donne des vérités v4 et un erratum de code, sans réécriture.
- Pièces d'autres sessions, sans résultat : note des effectifs, table de correspondance des champs du rejeu croisé, format de la table de l'ouvreur (pour un petit lecteur des familles et des paires, **non écrit**).
- Additif scellé qui inscrit le commit du code (texte scellé, étape 2).
- Épreuve plantée aux effectifs retenus, 500 répliques : devis et GO ; entropie racine tirée par la mère.

## Réserves
- Choix provisoires Q1 à Q13 (confirmés par la mère) et E-1 à E-8 (miens) : à revoir par le concepteur.
- E-5 : le changement de signe par unité du contraste apparié est invalide (plis à apprentissage partagé) ; le contraste se lit sur le nul par paire de poids, valeur p plancher voisine de 2/2^P.
- Suite complète du dépôt jamais menée à terme (consigne d'économie) ; essais limités à mon paquet.
- `verifier-arbre` échoue sur main pour `registres/passations/2026-11-22-0800-relais-mere-sortante.md.sha256` (hors de mon paquet).

## PROCHAINE ACTION exacte
Attendre un message de la mère. Si l'erratum du concepteur arrive : lire le texte, coder l'écart (nouveau nom de fichier de vérités, jamais de réécriture), essais, fiche v3, contre-lecture. Si le format de la table de l'ouvreur arrive : écrire `ouvreur_v1.py` (familles, paires, poids par série) et ses essais sur fichiers fabriqués.

## Machines, serveurs, tâches
Aucune instance de calcul, aucun serveur. Tâche planifiée : aucune active (la vérification de la demande n° 78 est éteinte, demande fusionnée). Aucune dépense.

## Branches et commits
- `sondes-v2/code-v1` : code au commit `c92d4e14`, tête `9f967867` avant cette passation ; fusionnée sur main (`bd472b89cdb05b9cfbf8d9966daf36ed1a0120fb` au moment d'écrire).
- Branche de contre-lecture, lecture seule pour moi : `contre-lecture/sondes-v2-code-v1`.

## Sessions avec qui je parle
- Mère : `session_013QMayjbmQUdDuDs2S3i3XD`.
- Concepteur : `session_013QMayndh51FN5XbmHpmEFg` (via la mère seulement).
- Contre-lecteur Sonnet : via la mère seulement.
