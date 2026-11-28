# Table « constat → endroit changé » du brouillon 2 de P3b — v1

Rédacteur neuf du brouillon 2 (Claude, sous-agent), session 16, 2026-10-21 vers 00:55 UTC (heure vraie). Une ligne par
constat des contre-lectures R2 du brouillon 1 (20 « méthode », 25 « texte »), selon le traitement de la session
(`…/p3b/traitement-contre-lectures-brouillon1-P3b-v1.md`, `d31c87b1…`), qui adopte avec amendements le projet
(`…/p3b/traitement-brouillon1/traitement-contre-lectures-brouillon1-P3b-projet-v1.md`, `82a90e81…`). Abréviations : T =
`P3b-seconde-lecture-v1-brouillon2.md` ; D = `devis-P3b-v2.md` ; Pl = `plan-code-et-chaine-P3b-v2.md` ; Q =
`questions-ouvertes-P3b-v2.md`. « Mots exacts » : bloc du projet recopié sans changement de sens ; tout changement de mot
est écrit dans la dernière colonne avec son motif.

| constat | décision | passage | écart ou précision (motif) |
|---|---|---|---|
| CR-P3b-methode-01 | accepté | T : Métrique, T4 résiduel (« Recouvrement ») ; Critères, G6 et O5 ; Prédiction, P3b-P2 et P3b-P5 ; Audit (dernière grandeur) ; Pl : `residuel_p3b_v1.py` (tests du recouvrement) | dans P3b-P2, la « même formule » est écrite : « T4 résiduel non établi ou non calculable (≈ 70 %) : une sonde au champ ne serait pas séparée du nombre, de la tâche ou de l'historique à cette puissance (recouvrement faible par construction) » ; a priori de P3b-P2 inchangé (70 %), celui de P3b-P5 porté à 80 % par les mots du rapport |
| CR-P3b-methode-02 | accepté | T : T4 résiduel (« Seconde spécification, gelée ») ; Pl : `residuel_p3b_v1.py` (test de courbure) | aucun |
| CR-P3b-methode-03 | accepté modifié | T : Reconstitution (critère d'épisode, recherche bornée, propagation, M-P3b-2 selon N-032 (C), contrôle négatif, empreintes d'activations) ; Seuil (paires) ; Préalable ; P3b-P0 ; liste d'arrêt (M-P3b-2) ; Chaîne, Ordre ; D : § 3 (poste du contrôle négatif), § 6 ; Pl : `reconstitution_p3b_v1.py`, `controles_avant_depense_p3b_v1.sh` ; Q : Q-03, Q-13 | conséquences écrites par ce rédacteur : (1) la parenthèse du brouillon 1 « celui qui rend l'empreinte… sinon le premier » est remplacée par un renvoi au critère d'épisode (elle contredisait « aucun jeton de fin n'est pris par défaut ») ; (2) P3b-P0 et la ligne du Préalable reprennent les cinq paires du « Seuil » ; (3) version de repli (B) de N-032 dans la Reconstitution : phrase de ce rédacteur, faite des mots de texte-08 (le rapport n'en donnait pas pour cet endroit) |
| CR-P3b-methode-04 | accepté | T : table D (D3, D4, D4b, fusion F-1) ; Seuil, double comptabilité ; Prédiction, P3b-P8 (D4b nommée) | aucun |
| CR-P3b-methode-05 | accepté | T : double comptabilité, fin du point « préférence » (amorçage) ; D3 (F-1) ; H-P3b-3 (seconde rivale nommée) ; Pl : `lentille_p3b_v1.py` (drapeaux) | ajout de ce rédacteur : la rivale « amorçage » nommée dans H-P3b-3, pour que l'hypothèse annonce la lecture de D3 ; aucun seuil neuf |
| CR-P3b-methode-06 | accepté | T : CP-L, item (v) ; D3 et D4 (F-1) ; P3b-P7 ; Plan, étape 2.3 ; graines (`cp-lentille/transformation`) ; D : § 3 (+ 0,05 h) ; Pl : `lentille_p3b_v1.py` ; Q : Q-19 | précisions de ce rédacteur : « (v) ne fait pas passer ni échouer le contrôle : il entre dans la ligne D3 » ; plancher par rotation des items (v) estimé sur les 200 items (v) (suite de methode-07) ; P3b-P7 : aucun a priori écrit pour (v) |
| CR-P3b-methode-07 | accepté | T : double comptabilité, plancher par rotation ; Pl : `lentille_p3b_v1.py` (test R5 de la rotation) | « moyenne μ_ℓ » estimée sur le même échantillon que Σ_ℓ (les mots du rapport ne nomment que Σ_ℓ) |
| CR-P3b-methode-08 | accepté | T : Plan, point 4 ; P3b-P1 (« ; si au-dessus, aire sous 0,65 » retiré) ; réserves (« puissance du nul ») ; Q : Q-17, Q-23 | marqueur neuf `<<ENTREES_M10_P3>>` pour les entrées de la formule M10 (consigne : grandeurs de P3 laissées en marqueurs) ; niveaux et bases selon C-1 et C-4 ; phrase gardée du brouillon 1, adaptée : « La double comptabilité au premier pas lit au plus une action par épisode : puissance faible, déclarée » |
| CR-P3b-methode-09 | accepté modifié | T : Métrique, Action (« Base de lecture ») ; T1 (« sur la base de lecture du bras ») ; T4 résiduel (plis) ; Plan, points 1 et 6 ; P3b-P1 ; Pl : `partition_p3b_v1.py` ; Q : Q-24 | ajout de ce rédacteur pour la version (B) : plis `plis/lecture-40`, 5 plis de 8 tâches (le rapport ne les nomme pas) ; mention « Version de repli (B) de P-016 » ajoutée pour le refus au scellement (texte-15) ; phrase du brouillon 1 « la découverte sert aux choix (oracle), jamais à une lecture rapportée » réécrite pour l'oracle seul (elle contredisait la base de 60 tâches) |
| CR-P3b-methode-10 | accepté | T : Métrique, « Réserves de robustesse reprises de l'addendum 1 » ; liste des réserves ; Plan, point 3 (ordre) ; Pl : `lecture_p3b_v1.py` | aucun |
| CR-P3b-methode-11 | accepté | T : Seuil, « Famille principale » ; Placebo (niveau par bras) ; Plan, point 7 (F-2) ; Q : Q-20 | aucun |
| CR-P3b-methode-12 | nœud (P-023) | T : Oracle, étiquettes (version (A)) ; Périmètre, versions de repli (B) et (C) de P-023 (O6, O7) ; liste d'arrêt ; Q : Q-07 | écrit selon (A), recommandée ; (B) et (C) à côté, mot pour mot |
| CR-P3b-methode-13 | accepté | T : Oracle, estimateur (système), plancher (loi nulle, répliques dégénérées), placebo ; liste d'arrêt (répliques) ; Plan, étape 2.7 ; Pl : `oracle_p3b_v1.py` | aucun |
| CR-P3b-methode-14 | accepté | T : Seuil, réserve VS-01 | aucun |
| CR-P3b-methode-15 | accepté modifié | T : Plan, point 7 (F-2) ; « Bras non aveugles » (F-3 : phrase de texte-03) | phrase de méthode-15 sur l'addendum 1 non ajoutée (F-3) |
| CR-P3b-methode-16 | accepté | T : double comptabilité (leurre par tâche, H_t de l'honnête, exclusions au-delà de 999), CP-L ([2, 999]) ; T4 résiduel (h_t de l'honnête) ; graines (`lentille/leurres/<tâche>`) ; Pl : `lentille_p3b_v1.py`, `residuel_p3b_v1.py` ; Q : Q-16, Q-17, Q-28 | jonction de (a) et (b) par ce rédacteur : leurre tiré sur la médiane de toutes les actions de l'honnête ; action de l'honnête dont τ_h égale τ_d exclue, comptée (Q-28) |
| CR-P3b-methode-17 | accepté | T : Métrique, Positions (f, τ_w, exclusions, désaccords) ; descriptifs (F-6) ; Pl : `positions_p3b_v1.py` | chemin du module de `heures_declarees` non cité (Q-27) |
| CR-P3b-methode-18 | accepté | T : Audit, déclencheurs ; réserves (« attendue au scellement ») | aucun |
| CR-P3b-methode-19 | accepté modifié | T : Oracle, fin du point « validation croisée par tâche » (phrase du traitement) | la branche « Mahalanobis » reste, comme garde |
| CR-P3b-methode-20 | accepté modifié | T : Synthèse, troisième ligne (F-4) | « G2a ou G2b » écrit « G2, G2a ou G2b » : texte-05 garde la ligne G2 (G2a et G2b insérées avant elle) ; sans G2, la synthèse ne couvrirait pas un nul validé par P4 (Q-29) |
| CR-P3b-texte-01 | nœud (N-031) | T : Périmètre, « Ce que P3b ne revendique pas » (marqueur, versions (a), (b), (c)) ; en-tête, Statut ; Q : Q-01 | N-0xx = N-031 (registre l. 516) ; versions de repli (b) et (c) : mots de ce rédacteur, tirés des options du traitement (point A) et de la ligne N-031 |
| CR-P3b-texte-02 | nœud (P-023) | T : en-tête (« Référence de GO-2026-10-20-05 ») ; Périmètre (écarts, F-7) ; tableau hors périmètre (ligne « excès d'aire apparié ») | correction 2 remplacée par F-7 ; correction 3, seconde forme, avec « ce texte le calcule en réserve « plancher conjoint » » ; P-0xx = P-023, défaut le 2026-10-23 vers 00:30 UTC (registre l. 401) |
| CR-P3b-texte-03 | accepté | T : « Bras non aveugles » | aucun |
| CR-P3b-texte-04 | accepté | T : « Exposition des rédacteurs », troisième puce | aucun |
| CR-P3b-texte-05 | accepté | T : table G (G2a, G2b) ; Plan, point 8 ; réserves (« règle conditionnelle P4 » retirée) ; Q : Q-22 | titre du point 8 changé en « Instrument générique et P4 » (le mot « règle conditionnelle » disparaît avec la réserve) |
| CR-P3b-texte-06 | accepté modifié | T : Synthèse, deuxième ligne (mots du rapport) ; troisième ligne (F-4) | voir CR-P3b-methode-20 |
| CR-P3b-texte-07 | accepté | T : en-tête (commit, modules de P3b) ; liste d'arrêt ; Plan, étape 2.1 ; Pl : règle d'en-tête, `controles_avant_depense_p3b_v1.sh`, `passe_p3b_v1.py`, `lecture_p3b_v1.py` | aucun |
| CR-P3b-texte-08 | nœud (N-032) | T : Reconstitution (versions de repli (A) et (B)) ; Chaîne, Ordre ; D : § 6 ; Pl : § 3 et § 4 ; Q : Q-03 | écrit selon (C), recommandée (mots du traitement) ; (B) : mots de texte-08 |
| CR-P3b-texte-09 | accepté modifié | T : Plan, point 7 (F-2) ; Seuil (méthode-11, C-1) | mots du rapport non appliqués : la famille de trois lectures n'est pas retenue (C-1) |
| CR-P3b-texte-10 | accepté | T : liste d'arrêt (garde de 24 heures) ; D : § 4 ; Pl : `arreter_p3b_v1.sh` | aucun |
| CR-P3b-texte-11 | accepté | T : Plan, point 5 ; liste d'arrêt (« autre carte ou autre processeur ») ; D : § 2 ; Pl : `lancer_p3b_v1.sh` | ajout dans la liste d'arrêt pour que le filtre soit une garde (même règle que le reste du filtre) |
| CR-P3b-texte-12 | accepté | D : § 1, § 2, § 4 | « ≈ 20 % de frais » retiré partout |
| CR-P3b-texte-13 | accepté | T : en-tête (cinq modules ajoutés) | préfixes recalculés sur disque par ce rédacteur : égaux |
| CR-P3b-texte-14 | accepté | Q : Q-04 à Q-07, Q-15 ; T : marqueurs P-023 (Pas lus, Positions, Bandes, Oracle) | marqueur écrit « Décision de Lazar en attente : P-023 » (forme demandée par la consigne du brouillon 2) au lieu de « Proposition en attente : P-0xx » ; le scellement refuse les deux |
| CR-P3b-texte-15 | accepté | T : Périmètre, `<<PARTITION_P016>>` ; Pl : `sceller_p3b_v1.sh` | toutes les versions de repli portent « Version de repli » pour être refusées au scellement |
| CR-P3b-texte-16 | accepté | T : Reconstitution, garde (e) | aucun |
| CR-P3b-texte-17 | accepté modifié | T : liste d'arrêt (cinq puces ; troisième selon P-023 (A), F-8) ; versions de repli (B) et (C) de P-023 ; en-tête (`<<SHA_MODELE_P3>>`) ; Q : Q-23 | troisième puce en (B) : « …de la mention ou du témoin… » (en (B), le témoin est exclu de l'apprentissage) : mots de ce rédacteur |
| CR-P3b-texte-18 | accepté modifié | T : Chaîne, Ordre (F-5) ; Pl : § 4 | numéros N-031, N-032, P-023, P-024 remplis |
| CR-P3b-texte-19 | accepté | T : tableau hors périmètre (a) à (d) | ligne « manipulation du nombre écrit » mise à jour selon R-312 (P-017 (C′)) |
| CR-P3b-texte-20 | accepté | T : hypothèse de travail (4) ([KT] retiré) ; lentille jacobienne ([JL] retiré, source exigée avant le scellement) ; en-tête (« Provenance ») ; Chaîne, Modèle (chaîne v2 versée) ; Q : Q-18 | [JL] retiré plutôt que cité : ce rédacteur n'a ni le chemin du PDF dans le dépôt ni la page vérifiée |
| CR-P3b-texte-21 | accepté modifié | T : en-tête (Historique) ; D, Pl, Q : en-têtes (« écrite vers 23:37 / 23:38 / 23:39 UTC ») | heures du brouillon 2 : heure vraie (`date -u`), R-312 |
| CR-P3b-texte-22 | accepté modifié | T : (a) descriptifs (coût écrit divisé par 3) ; (b) τ_w (F-6) ; (c) « retenue » avant la table G ; (d) O2 et P3b-P3 ; (e) H-P3b-1 ; (f) Plan, étape 2.2 ; (g) réserves | aucun |
| CR-P3b-texte-23 | accepté | note transmise v2 (`…/p3b/a-transmettre-contre-lecture-P3b-v2.md`, `86c1518f…`) | rien dans le texte |
| CR-P3b-texte-24 | accepté | T : Exposition (rédacteur du brouillon 2 aveugle au signe de P3-P2 ; déclaration de la session reprise) | aucun |
| CR-P3b-texte-25 | accepté | — | rien à changer ; `<<SHA_LENTILLE_J>>` reste tant que le bras reste |

Constats non appliqués : aucun. Mots de rapport non appliqués par décision du traitement : texte-09 (famille de trois
lectures, C-1) ; correction 2 de texte-02 (remplacée par F-7) ; phrase de méthode-15 sur l'addendum 1 (F-3) ; ligne de
méthode-20 (F-4).

Décisions de Lazar en attente, écrites dans leur version recommandée avec les replis à côté : N-031 (a) ; N-032 (C) ; P-016
(A) ; P-017 (A) ; P-023 (A) ; P-024 (A).
