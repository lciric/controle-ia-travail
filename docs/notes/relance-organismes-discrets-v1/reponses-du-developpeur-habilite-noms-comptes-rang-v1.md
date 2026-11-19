# Réponses du développeur habilité aux quatre questions de la relance (noms, comptes, forme, rang) — v1

Transmises par la mère à la relance du bras A, 2026-11-19T14:38:03Z, « sans interne et transmissibles telles quelles » ; inscrites côté mère en R-3888. Module cité : `autres_moniteurs_v8.py`, 61105129…, commit `18f63f40` (branche du développeur habilité ; non ouvert par la relance). Recopie à la lettre du message de la mère.

1. **Noms rendus, en listes fermées.**
   - Par moniteur et par dose, dix-huit clés, toujours toutes présentes : `moniteur`, `dose`, `calculable`, `motif`, `aire`, `pli0`, `pli1`, `valeur_p_bas`, `valeur_p_haut`, `n_permutations`, `permutations_degenerees`, `au_moins_egales`, `borne_haute`, `quantile_borne_haute`, `tirages`, `tirages_degeneres`, `effectifs`, `valeur_p_pour_la_famille`.
   - Sortie de la lecture commune, onze clés : `plis`, `lectures` (rangé par dose puis par moniteur), `piece_source`, `reglages`, `agregateur_somme_sans_etat`, `agregateur_maximum_sans_etat`, `exclues`, `preuve_d_ordre`, `scores_par_unite`, `comptes_des_lectures`, `nombres_rendus`.
   - `reglages`, neuf clés : `n_permutations`, `n_tirages`, `taille_de_la_famille`, `niveau`, `statistique_agregateur`, `doses_de_la_famille`, `dose_pour_information`, `permutation`, `unite_de_la_permutation` (les deux dernières sont neuves en version 8).
   - `scores_par_unite`, cinq clés : `fichier`, `sha256`, `lignes`, `champs`, `forme` (neuve en version 8).
2. **Sens des comptes.**
   - `tirages` est le nombre calculé, c'est-à-dire non dégénéré ; `tirages` + `tirages_degeneres` = `reglages.n_tirages`, le nombre demandé.
   - `n_permutations` est le nombre demandé, et `permutations_degenerees` celles qui sont perdues.
   - Le dénominateur du 1 % est le nombre demandé, dans les deux cas. Un moniteur est non calculable si les dégénérés dépassent strictement 0,01 × les demandés : 20 sur 2 000 n'est pas « plus de 1 % », 21 l'est.
3. **Forme des comptes.** Le champ est toujours présent ; il vaut `null` quand il n'est pas connu, jamais zéro par défaut ; zéro veut dire « compté, aucun ». Selon le motif :
   - calculable : les quatre comptes sont remplis ;
   - non calculable avant les permutations (pli sans action, classe absente, moniteur appris non ajustable) : les quatre sont nuls ;
   - plus de 1 % de permutations perdues : les deux comptes de permutations sont remplis, les deux de tirages nuls ;
   - plus de 1 % de tirages dégénérés : les quatre sont remplis ;
   - intervalle impossible faute de deux tâches : permutations remplies, tirages nuls.
   Dans tous les cas non calculables : `calculable` faux, `motif` rempli, aire, valeurs p et borne nulles, `valeur_p_pour_la_famille` = 1.
4. **Dixième champ : `rang`.** C'est le rang moyen de l'unité dans son pli, pour son moniteur et sa dose ; 1 pour la plus petite valeur ; un nombre à virgule, les ex æquo partageant la moyenne de leurs rangs. Les neuf autres champs et leur ordre sont inchangés. Fichier : `rangs-par-unite-moniteurs-bras-a.jsonl`.

**Hypothèse de l'échange par paire**, vérifiée par lecture du lanceur du bras. Note sur la branche du développeur : `docs/notes/bras-a-moniteurs-v1/hypothese-de-l-echange-par-paire-lanceur-du-bras-v1.md` (95e656e7…). En bref :
- Dans une paire, sont identiques les graines, la tâche, l'environnement, le nombre de pas, les réglages et la place dans les lots.
- Trois différences de fait existent hors de la dose : l'ordre d'exécution ; l'épisode honnête joué avec le premier adaptateur chargé à l'échelle 0 ; le remplissage des lots dès que les textes divergent. Aucune n'avantage l'un des deux épisodes autrement que par l'adaptateur.
- L'épisode honnête est commun aux quatre doses : les valeurs p des doses ne sont pas indépendantes, ce que la correction de Holm ne demande pas.
- Non vérifié : que la machine rejoue au bit près d'un lot à l'autre.

**Le lanceur de l'étape de discrétion n'est pas écrit.** La mère le fait écrire par le développeur habilité, contre-lu ensuite par Opus.

## Remarque de la relance (hors recopie)
Le point 2 rejoint l'option (a) de la fiche 9 (seuil du 1 % sur le nombre demandé) : sous l'option (b), le quotient `tirages_degeneres / tirages` porterait sur le nombre calculé et divergerait du module au bord. La fiche reste à Lazar.
