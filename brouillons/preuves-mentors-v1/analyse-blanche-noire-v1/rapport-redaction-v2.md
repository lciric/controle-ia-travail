# Rapport de rédaction — analyse appariée boîte blanche / boîte noire, brouillon 2 et code v2

Rédacteur : sous-agent (Claude, Opus 5.5), 2026-11-01, ≈ 22:25 UTC, au 2026-11-02, ≈ 00:00 UTC. Le bras (ii) a été rétabli dans le brouillon 2 après R-1086 (mot de Lazar, 23:50 heure de Paris : N-029, option (a)). Aucune donnée de R1, R2 ni R4 vue ; aucune statistique décisive calculée sur P3 ; aucun commit, aucun `.sha256` ; aucun fichier existant modifié (R12) : le paquet v1 (commit `a3db3e3e`) et le brouillon 1 restent tels quels.

## Traitement de la contre-lecture 1 (`contre-lecture-preenregistrement-analyse-v1.md`, `2af7ee33…`)

| point | traitement |
|---|---|
| C1 (B) | Version « autorisé » (R-1086) : bras (ii) lu, famille de Holm de quatre comparaisons ((i) − (ii), (ii) − (iii) tromperie, (ii) − (iii) enjeux, (i) − (L)), (L) obligatoire ; en tête et dans la lecture : « ne compte pas pour G1 ; la référence de porte de N-029 reste sur T0.6 » (écrit aussi par le code en tête de l'issue et du rendu). GO-13 n'est pas cité comme dérogation. Règle d'arrêt du bras (ii) : `R2: null` avec un motif fermé (`sorties_non_livrees`, `garde_N029_du_kit`, `consigne_dans_contexte`, clé `motif_R2` de la fiche, vérifiée par le code) → lecture « R1 seul », famille (i) − (L), sans autre repli. Le brouillon intermédiaire « R1 seul + addendum » n'a jamais été versé. |
| C2 (B) | `entrees_v2` : fichiers scindés `…-moyenne.npz` (exigé, fini) / `…-maximum.npz` (facultatif ; défaut → `i_max` seul non lu) ; tolérance du fournisseur 0,02 × (1 + \|score\|) reprise dans la fidélité indépendante. R4 par transfert (`evaluation_v2.plis_transfert`, `evaluer_une_tache_laissee`, `lecture_v2.calculer_r4`), minimum 32 tâches. Le contexte du juge « énoncé + action » est écrit dans la Métrique et les Limites ; le code exige que le fournisseur déclare invite et contexte (pointeurs), il ne lit pas le texte du contexte. Juge de R4 lu par ses scores livrés. |
| C3 (M) | `calculs-predictions-v2.py` (puissance exacte, intégrale du relecteur) et sa sortie ; table des prédictions remplacée par les nombres obtenus (identiques à ceux du relecteur). |
| C4 (M) | `AIRE_PLAFOND = 0,99` ; plafond si les deux puissances ≥ 0,95 ou les deux aires ≥ 0,99 ; essai. |
| C5 (M) | `CONSEQUENCES` remplacé par `SUGGESTIONS` (texte du relecteur, `i-ii`, `i-L`, `ii-iii`) ; état « non concluante » ; préfixe N-026 sur toute comparaison qui porte (i) ; rendu : « Suggestions à Lazar ». |
| C6 (M) | Écart 2 remplacé ; « borne haute » renommé « sonde entraînée sur l'organisme » ; point « i_max devient (i) » supprimé. Sur commande de la session : planchers appariés pour `i_sh` et `i_max` (premier découpage), en descriptif. |
| C7 (M) | Fidélité bloquante : corrélation < 0,95, pente hors de [0,95 ; 1,05], écart relatif médian > **0,02** (la tolérance du fournisseur ; le relecteur proposait 0,05), plus de 5 % des actions hors tolérance ; réserves en deçà ; réserve « couche retenue non vérifiée ». Essais : pente 0,8 à corrélation 1 → raté ; décalage → raté par l'écart médian. |
| C8 (m) | Étape 0 du Plan d'analyse : arbre de travail séparé au commit cité, même procédure que la simulation d'essaim ; ligne « Commit du code d'analyse » en tête. |
| C9 (m) | Pointeurs fixés par le `LISEZMOI` v2 du kit (empreinte au scellement), vérification par la session qui scelle la fiche (le code ne compare pas au `LISEZMOI`) ; `R2: null` motivé dans `redaction`. |
| C10 (m) | Empreintes ajoutées (calculs de G1, résultats de P3, `conftest.py`) ; versions Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (celles du dépôt et de P3 ; le relecteur avait 2.5.3 / 1.18.1 dans un autre environnement) ; registre des décisions : à citer au scellement avec la réponse de Lazar. |
| C11 (m) | Heures corrigées (UTC et heure de Paris). |
| C12 (m) | `tests/test_analyse_blanche_noire_v2.py`, 11 essais (liste dans le préenregistrement, point 9). L'état « rééchantillonnage en échec » est couvert par la branche « non lue » de `ligne_comparaison`, sans essai propre. |
| C13 (m) | BN-P12 remplacée par la formulation descriptive. |
| C14 (m) | Limites : paragraphe du relecteur repris. |
| C15 (M) | `frequence-regle-decision-v2.py` : 200 répliques nulles, famille de quatre → 8/200 = 0,040 (Wilson [0,020 ; 0,077]) pour la règle v2, 27/200 = 0,135 pour la règle abandonnée ; famille « R1 seul » 13/200 = 0,065. `frequence-regle-decision-v1.py` (écrit avant R-1086) : (i) − (L) seule, 9/200 = 0,045. Le scénario nul de la graine 21 (famille de quatre) est gardé comme essai dans le fichier neuf des essais v2. |
| C16 (m) | λ = 10 : phrase remplacée. |
| C17 (m) | `BrasNonLu` / `BrasEntraineV2` : non-convergence → ce bras seul non lu ; contrôle positif en échec → (i) et variantes non lus ; arrêt technique après manifeste écrit dans la liste d'arrêt. |
| C18 (m) | Déclencheurs dans les deux sens (fourchettes prédites ± 0,10 ; (c) hors de (i)) ; essai. |
| C19 (m) | Verdict « pour information et pour les nœuds ouverts » ; motif R3 ajouté. |
| C20 (m) | Fourchette des fausses alarmes 0,03 à 0,07 ; réserve à 0,08. |
| S1 | Non retenu : un bras « moyenne des scores par jeton des sondes génériques » serait un bras de diagnostic nouveau, qui exige son plancher apparié de même agrégation (directions aléatoires sur les activations moyennes de R1 à la couche 15, au contraire des sondes de production) ; c'est un ajout de lecture, donc un nœud (préenregistrement complémentaire), proposé à Lazar. |

## Code v2 (modules neufs, v1 repris sans modification)

- `constantes_v2.py` : constantes neuves seulement ; l'empreinte couvre v1 et v2.
- `entrees_v2.py` : fiche v2 (avec `motif_R2`, liste fermée), juge par le chargeur v1, fichiers scindés, chargeur partiel de R4, fidélité indépendante bloquante.
- `evaluation_v2.py` : `BrasNonLu`, `BrasEntraineV2`, `difference_v2` (m de la famille), transfert vers R4.
- `lecture_v2.py` : orchestration (famille de quatre avec le juge, ou « R1 seul » si R2 est nul pour un motif fermé), planchers de `i_sh` et `i_max`, comparaisons, audit, issue et suggestions, R4 par transfert ; liste fermée du code cité (12 modules du paquet, 2 fichiers d'essais, 13 modules gelés) ; constantes citées par « Empreinte des constantes (v2) ».
- `rendu_v2.py` : rendu Markdown.

## Ce qui reste ouvert pour Lazar

1. N-029 accordée (R-1086) : le texte cite R-1086 ; l'empreinte du registre des décisions à la version qui porte R-1086 est un marqueur à remplir au scellement. La règle « R1 seul » s'applique si R2 ne vient pas ou si la garde N-029 du kit refuse : à confirmer que la garde du kit de session-depot est levée pour R2 (sinon la lecture sera « R1 seul »).
2. R4 à 32 tâches par transfert (conception proposée par le relecteur, retenue) : réplication non décisive, intervalles ≈ 1,37 fois plus larges.
3. Ordre des commits et arbre de travail séparé (étape 0) ; gel du paquet dès le scellement.
4. Seuils de fidélité (écart médian bloquant à 0,02, plus serré que la proposition du relecteur).
5. S1 (moyenne des scores par jeton des sondes génériques) : préenregistrement complémentaire, si Lazar le veut.
