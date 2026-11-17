# Contre-lecture neuve (R2) — lecture courte : commande v8, addendum v3, devis v3, dépôt réduit v9 — v1

Même contre-lecteur que pour les v6 et v7 (n'a rien écrit des pièces). Commit `95eb7e11`. Rien loué, aucune commande `vastai`, aucun code voisin
exécuté, aucune variable d'environnement affichée, aucun fichier existant modifié, rien commité. Seul ajout : ce fichier (et des essais jetables dans le
dossier de travail de la session). Aucun nom de modèle d'IA ici.

## Verdict

**PRÊT POUR LE FEU**, avec des réserves mineures (aucune ne demande une nouvelle version si la mère accepte de les porter au plan de lecture scellé du lecteur
neuf). La majeure M1 et les mineures 1, 2, 4, 5, 6 sont corrigées ; le critère de l'audit de B-7 « par le haut » est calculable tel qu'écrit.

## Vérifié

- **Empreintes** : les 25 lignes du tableau final de la commande v8 sont égales aux fichiers ; compagnons de la commande v8, de l'addendum v3, du devis v3, du
  journal v11-réduit-v9 et du script v9 : `scellement verifier` OK.
- **Dépôt réduit v9** rejoué sur `95eb7e11` : 351 fichiers, liste `e3bcfb92e8b5…` = celle attendue ; le journal de l'essai à blanc (joué sur `5f51ab32`, réduit
  v9) est conforme, 0 écart, et reprend les cas de carte. Le script v9 ne change que l'addendum (v2 → v3) et son nom ; le lanceur v5 est inchangé
  (`c6a5d5db…`), donc les 77 + 168 essais de la lecture précédente restent valides.
- **M1** : l'addendum v3 (§ 4, l. 68-77) fixe le critère avant la course : (1) témoin apparié, (2) norme de pilotage non nulle, (3) verdict de B-7 recalculé à la
  graine 1, même série et même lot, aussi « non reproduit » **par le haut** ; « tient » → lecture valable ; « ne tient pas » → aucune lecture « par le haut ». Les deux
  issues sont écrites. Corrigé.
- **Mineure 1** (devis : « un ou deux audits ») et **2** (addendum § 4 : le motif de B-7 lit l'ablation, l'audit peut n'être requis qu'à une série) : corrigées.
- **Mineure 4** : « ≈ 2 GiB chacun » avec renvoi à `memoire-measure-b-alpha-v1.md` § 3 (qui dit bien « ≈ 2 Go » pour le modèle de la tranche) : corrigée, sourcée.
- **Mineure 5** : rappels réordonnés (a 4,8 h ; a′ 6,9 h ; b = 75 % de D, soit 7,9 h à 0,73 et 9,2 h à 0,62 ; c = 80 % de D, soit 8,4 h et 9,8 h ; minuterie) ; recalcul :
  0,75 × 10,48 = 7,86 h ✓ ; 0,75 × 12,34 = 9,25 h ✓ ; 0,8 × 10,48 = 8,38 h ✓ ; 0,8 × 12,34 = 9,87 h (écrit 9,8 ; arrondi par défaut, sans effet). Cohérent entre devis v3 et commande v8.
- **Mineure 6** : 2,4 à 3,0 USD avec audits (3,7 h × 0,62 + 0,1 = 2,39) ✓, repris à l'identique par la commande.
- **Non repris, déclarés dans la commande** (3, 8, 7) : conformes à ce que j'avais classé « mineure » ; acceptés.

## Le critère (3) est-il calculable avec ce que verse le lanceur v5 ? Oui.

- **Résumés** : `_score(ctx, 1, "seed1" + suffixe, …)` écrit `causal_lens_seed1_<modèle>.json` (lot 16) et `causal_lens_seed1-lot64_<modèle>.json` (lot 64) dans
  `diag/<run>/` et les liste dans le résultat de l'audit ; ce sont les noms de l'addendum. Ils portent `targets` pour les quatre cibles et les quatre lentilles
  (`--lenses logit,J,npJpp,npR`).
- **n de la graine 1** : le résultat de l'audit contient `grandeurs.n` (calculé par `_grandeurs` sur le fichier de la graine 1, même structure que celui des verdicts).
- **Calcul** : j'ai appelé `verdicts_b_alpha_v3.verdict_b7(t, n)` sur la référence convertie avec « ablate win » forcé à 0,50 aux couches 8-15 : « non reproduit »,
  `par_le_haut = True`. Le lecteur n'a donc besoin ni de code nouveau ni de location, seulement de monter `t` comme le fait `_verdicts` (`targets[cible][lentille]`
  pour `CIBLES` × `LENTILLES`) et de lire `details["par_le_haut"]`.

## Défauts nouveaux et réserves

Aucun bloquant, aucun majeur.

1. **(1) et (2) ne portent pas sur la graine 1 (mineure).** `_audit_trop_beau` calcule `temoin_bien_apparie` sur le fichier de grandeurs de la **graine 0** de la série
   (`fichier_grandeurs`, l. 833 de la v5) et `pilotage_norme_non_nulle` comme `min(n0[c])` où `n0` est le `n` de la graine 0. L'addendum les dit « dans le résultat de l'audit »
   (exact) mais le lecteur y verra des vérifications de la série, non de l'audit. De plus `pilotage_norme_non_nulle` est le plus petit nombre de pôles retenus par couche, pas
   une norme : « > 0 » est presque vide (la chaîne en défaut (b) exige déjà ≥ 32 pôles par couche). C'est (3) qui porte tout le contenu du critère. À dire dans le plan de lecture
   scellé : « (1) et (2) sont lus tels que versés, ils concernent la série ; (3) est le test de la graine 1 ». Rien à coder.
2. **Écrire la fonction de (3) (mineure).** L'addendum dit « par le code des verdicts » ; le plan de lecture doit nommer `verdict_b7` et le champ `par_le_haut`, **pas** `verdict()` :
   si la graine 1 déclenche une chaîne en défaut (essai : `control_med` à 0,20 à une couche), `verdict()` rend `b7 = None` et le critère serait indéfini, alors que `verdict_b7`
   reste calculable. Dans ce cas, (3) se lit sur `verdict_b7`, et la chaîne en défaut de la graine 1 est rapportée à côté.
3. **Statut de B-7 quand l'audit « ne tient pas » (mineure).** L'addendum dit « B-7 de la série est rapporté sans lecture pour un moniteur ». Il ne dit pas si, pour la seconde série,
   la lecture de B-7 de la troisième course (que v2 déclarait remplacée) redevient la lecture en vigueur. À préciser dans le plan : « elle reste en vigueur avec son écart de lot ».
4. **Le calcul (3) est fait par le lecteur après l'ouverture des résultats.** Pour que cela reste « fixé avant », le plan de lecture (qui doit être scellé avant l'ouverture, addendum § 4)
   doit contenir la procédure exacte de 1 à 3 ; rien d'autre n'est à décider ensuite.
5. **Tableau des rappels** : le devis dit « (v2, v3) un ou deux audits » mais le rappel a′ à 6,9 h vise « deux audits » ; avec un seul audit l'attendu codé est 6,1 h
   (4,81 + 1,3) ou 5,6 h (4,81 + 0,8). Sans conséquence (l'alerte est seulement un compte rendu).
6. **Rien trouvé de faux dans les renvois** : `calcul/neuron-lens-b-alpha-v6` et `course/…-reduit-v9` partout, fichiers de suivi `-v6`, `--plafond 8.5`, `CARTE_ATTENDUE`,
   commit source de l'essai (`5f51ab32`) distinct du commit de la course, avec la phrase « à revérifier à l'étape 5 » : la liste a bien été revérifiée ici sur `95eb7e11`.
   Le GO-2026-11-17-04 reste à citer au feu avec le commit de `main` qui l'inscrit (mineure 7 de la lecture précédente, déjà déclarée).

## Réponses

- M1 et mineures 1, 2, 4, 5, 6 : **corrigées**.
- Critère de l'addendum v3 : **calculable** à partir de ce que verse le lanceur v5 (noms de résumés, `n` de la graine 1, champs `temoin_bien_apparie` et
  `pilotage_norme_non_nulle`), avec les précisions 1 à 4 portées au plan de lecture scellé.
- Défaut nouveau : aucun de nature à retarder le feu.
