# LISEZMOI de sortie — synthèse du tour « graines de plus pour le pilote 4 » (collisionneur v2.6, étage III, deux tours) — v1

Écrit le 2026-10-26 à 05:27:34 (heure universelle, lue sur `date -u` dans la commande même d'écriture) par le sous-agent neuf qui a exécuté
`BRIEF-synthese-graines-v1.md`. Modèle du sous-agent : Claude Fable 5.1 (le modèle de la cellule A, voir « écarts »).

## Ce qui a été fait

1. Vérification du brief : `sha256sum` = `9558d6f5d9864372b0b75fb7def9c78c0d5514070244e9cacf3b7f1291033869`, conforme à l'ordre.
2. Vérification des pièces : `EMPREINTES-v1.txt` contre son compagnon (OK) ; les cinq cellules de `cellules/` contre leurs
   compagnons `.sha256` (cinq OK) et contre les lignes `run-graines-pilote4-q3-e3t1-v1/cellules/…` de `EMPREINTES-v1.txt`
   (identiques) ; `question-graines-pilote4-collisionneur-v3.md` (`0b9bbfb3…`) et `LISEZMOI-v1.md` (`eabc35c1…`) contre
   `EMPREINTES-v1.txt` (OK). Aucun autre fichier de `EMPREINTES-v1.txt` n'est fourni ni n'a été cherché ailleurs.
3. Lecture en entier : brief, question v3, LISEZMOI-v1, registre R-491 à R-495, les cinq cellules (E3-T1-conception-A et -C ;
   E3-T2-redteam-A, -B, -C) ; l'exemple de synthèse précédente, pour la forme seulement. La cellule refusée (E3-T1-conception-B,
   Opus) n'est pas fournie et n'a pas été supposée.
4. Écriture de `synthese-collisionneur-graines-v1.md` selon les sept points du brief (trois lignes ; six points de la question ;
   table de décision, recommandation, défaut ; transfert et modèle de calcul ; pièges et gardes ; références ; réserves).
   Heure insérée par `date -u` dans la commande d'écriture ; rafraîchie après chaque retouche.
5. Contrôles sur le texte : aucun score (il n'en existe pas), aucun verbe de jugement sur des scores, aucun critère ni stratégie
   de classement des tâches (les scénarios d'évasion des cellules sont résumés sans leur heuristique), aucun contenu de
   réflexion interne, aucun tutoiement, aucun acronyme d'une liste de contrôle (devises et interfaces écrites en toutes
   lettres), chiffres marqués illustratifs sauf calcul explicite cité. Ni git, ni réseau, ni sous-agent, ni clé, ni dépense.
6. Scellement : compagnons `.sha256` de la synthèse et de ce LISEZMOI.

## Fichiers produits (dossier `/var/tmp/synthese-collisionneur-graines-v1/`)

| fichier | empreinte sha256 |
|---|---|
| `synthese-collisionneur-graines-v1.md` | `b8cdeb5c18335b1c94417ca2f820404a07b68309550a5fe11ec52bc8c3a2df2a` |
| `synthese-collisionneur-graines-v1.md.sha256` | compagnon de la ligne ci-dessus |
| `LISEZMOI-sortie-v1.md` | ce fichier ; empreinte dans `LISEZMOI-sortie-v1.md.sha256` |

## Écarts déclarés

- **Modèle.** Le brief dit « tu es le même modèle que B » ; le sous-agent est Claude Fable 5.1, modèle de la cellule A (conception
  et attaque). Le biais de proximité possible va donc vers A, non vers B ; il est signalé dans la synthèse (§ 7, première réserve).
- **Structure du III.2.** Le brief dit que les trois modèles attaquent les deux conceptions valides ; dans les cellules, A n'attaque
  que C, C n'attaque que A (sections « contre B » vides, construction croisée), seul B attaque A et C. Dit dans la synthèse (§ 7).
- **Longueur.** Le brief demande deux pages au plus ; la synthèse fait 3 387 mots selon `wc -w` (19 837 octets), contre 1 976 pour
  l'exemple fourni : environ 1,7 fois l'exemple, au-dessus de deux pages imprimées. Trois passes de condensation ont été faites
  (brouillons de 4 500, 3 967 et 3 616 mots, écrasés avant toute empreinte, jamais diffusés) ; le reste tient aux sept points
  obligatoires, à la table à cinq colonnes sur neuf dessins et à la liste de vingt et une références. Le brief n'est pas tenu
  sur ce point ; rien n'a été retiré du fond pour le tenir.
- **Vérifications d'arithmétique.** La synthèse a refait à la main (sans outil ni fichier) quelques calculs explicites des
  cellules (A § 2 ; attaque A F2 et F3 ; attaque B A-F1 et C-F3) et les dit concordants à l'arrondi près ; ce n'est pas une
  recherche extérieure, mais c'est un ajout du sous-agent, déclaré comme tel (§ 7). Les quantiles de table de B C-F6 n'ont pas
  été vérifiés.
- Aucun autre écart : rien lu hors `/var/tmp/fournis-synthese-graines-v1/`, rien écrit hors `/var/tmp/synthese-collisionneur-graines-v1/`.
