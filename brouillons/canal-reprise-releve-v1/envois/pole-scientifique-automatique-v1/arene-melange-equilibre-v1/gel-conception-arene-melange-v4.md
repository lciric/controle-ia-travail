# Gel de la conception v4 — arène « mélange d'équilibre » — écrit AVANT tout calcul de la v4 (racines, règle de recalibrage, règles nouvelles, prédictions du pilote v4)

Rédacteur neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026, 12:43 UTC (relevé `date -u` : 2026-10-31T12:42:32Z juste avant l'écriture). Il n'a écrit aucun des brouillons 1 à 3, aucun des codes v1 à v3, aucune des trois contre-lectures de ce pilote. Reprise d'une consigne dont un premier rédacteur a été interrompu à 12:09 UTC sans rendre de fichier v4 (vérifié : aucun fichier `*v4*` ni `*brouillon4*` dans le dossier à 12:32 UTC).

Ce fichier est écrit **avant** toute ligne de code v4, tout essai, tout calibrage et tout pilote v4. Il ne sera jamais rouvert. Le code v4 épinglera son empreinte (constante dans le code) et refusera de partir en mode d'essai, de calibrage ou d'audit d'essai si ce fichier manque, a changé, ou ne cite pas la racine demandée : la chaîne gel → code → sorties (empreinte du code dans chaque manifeste) fixe l'ordre sans dépendre d'une déclaration (CM3-08).

## 0. Nature des changements (déclarée)

Brouillon 4 écrit **après** le pilote v3 et la contre-lecture 3 (`contre-lecture-arene-melange-v3-brouillon3.md`, scellée, `7ccc1460d6925fb1c743cb099a4490fcca2c7146c99ec4098e49234bb15dc236` ; 4 majeurs, 7 moyens, 5 mineurs) et **après** la décision R-739 de `registres/decisions.md` (Lazar a délégué ; conv-audit a tranché) : (1) Q2 gardée, lecture réécrite (la pureté des poids de B′ est un plafond de la classe de moniteurs, pas une preuve que le tirage au hasard est inutile) ; (2) δ recalibrés avant scellement sur au moins 48 instances d'une racine d'essai neuve, par la règle déjà écrite, sur le seul bras A ; (3) S18 = 0,10, N = 100, délai externe 9 000 s, choisis après lecture du pilote v3. Tout ce qui suit est donc postérieur au pilote v3 ; rien ne lit une racine de décision.

## 1. Racines

### 1.1 Racines neuves de la v4 (toutes dans la plage 20264001 à 20264999 ; aucune n'apparaît ailleurs dans le dépôt hors de la mention de la plage dans R-747, recherche faite à 12:38 UTC hors `donnees/` et hors `arene-extension-familles-v1/`)

| Racine | Usage (unique) |
|---|---|
| 20264101 / 20264102 | recalibrage des δ : bras A seul, instances 0 à 47, grille de 9 δ (racine principale / racine des familles tenues à l'écart) |
| 20264201 / 20264202 | pilote v4 (24 instances × 2 δ, 8 bras) et audit d'essai v4 sur des tâches de ce pilote |
| 20264211 / 20264212 | réservées : reprise du pilote v4 seulement si une erreur de code oblige à le rejouer (non employées sauf déclaration au journal) |
| 20264301 / 20264302 | essais du code v4 et mesures de temps |
| 20264303 | essais du code v4 : « autre racine » de l'essai de reproductibilité (une autre racine change le résultat) |
| 20264401 | simulations du calcul de puissance v4 (rééchantillonnage de la décision, bandes S10, critère d'audit, incertitude de P10, valeur nulle de I3), une clé de dérivation par simulation |

Décision inchangée : **RACINE = 20261201, RACINE_TENUE = 20261202**, jamais employées hors décision autorisée par un préenregistrement scellé.

### 1.2 Racines refusées par garde en v4

Relevé complet dans les brouillons 1 à 3, les LISEZMOI v1 à v3, les journaux, les codes et essais v1 à v3, le gel v2, le gel v3 et les trois contre-lectures :
- 20261291, 20261292 (brouillon 1, code v1) ; 20262291 (essais v1 : RACINE_ESSAI + 1000) ;
- 20261293, 20261294 (pilotes v2) ; 20261295, 20261296 (calibrage v2) ; 20261297, 20261298 (essais v2) ; 20262297 (essais v2 : RACINE_TESTS + 1000) ;
- 20269501, 20269502 (diagnostics de la contre-lecture 2) ;
- 20261311, 20261312 (pilote v3 et audit d'essai v3) ; 20261313, 20261314 (essais v3) ; 20262313 (essais v3 : RACINE_TESTS + 1000) ; 20261315, 20261316 (réservées en v3 au recalibrage, non employées, mais nommées : R-739 exige une racine neuve) ; 20261301 (écartée par le journal v3, présente ailleurs dans le dépôt) ;
- 20269731, 20269732 (diagnostic de la contre-lecture 3) ; 20269741, 20269742 (simulations de la contre-lecture 3) ;
- 20261101 (valeur fautive écrite par les essais v1 à v3 ; jamais une graine, refusée par prudence) ;
- **toute racine de 20265001 à 20265999** (plage d'une autre session, dossier voisin, qui travaille en parallèle) ;
- toute racine hors décision qui n'est pas listée au § 1.1 (racine non gelée).

Garde : `gen` refuse toute racine non permise (décision sans autorisation, déjà employée, plage voisine, non gelée) ; les modes d'essai exigent en plus que ce fichier soit présent, à l'empreinte épinglée, et qu'il cite la racine.

## 2. Règle de recalibrage des δ (R-739, décision 2), écrite avant tout calcul

- Bras **A seul** (défense unique réentraînée, même oracle « détection »), configuration v4 sauf `deltas` = la grille, mode léger (trajectoire de A et phase finale standard puis renforcée ; V(A) en léger est identique au bit à V(A) en mode complet : mêmes graines, les familles tenues tirent d'un générateur à part).
- Grille : **0,6 ; 0,8 ; 1,0 ; 1,2 ; 1,4 ; 1,6 ; 1,8 ; 2,0 ; 2,4** (champ `grille_calibrage`, inchangé depuis la v2).
- Instances : **0 à 47** (48 instances) de la racine 20264101 / 20264102 ; 432 tâches.
- Statistique : moyenne sur les 48 instances de V(A) (= `V_iii_final` de A) à chaque δ de la grille ; rapportée avec son erreur-type (écart-type par instance / √48).
- **δ_haut** = plus grand δ de la grille où la moyenne de V(A) est ≥ 3α = 0,03 ; **δ_bas** = plus grand δ de la grille strictement inférieur à δ_haut où la moyenne de V(A) est ≥ 10α = 0,10. Règle de `choisir_deltas` (code v2, v3), appliquée telle quelle, sur l'estimation ponctuelle ; aucune autre considération (pas de lecture de B, B′, D ni d'aucun autre bras).
- Si aucun δ ne satisfait une condition : arrêt par garde, pas de choix à la main, retour à conv-audit.
- Rapport descriptif en plus, sans effet sur le choix : stabilité du couple choisi sous rééchantillonnage des 48 instances (2 000 tirages, générateur dérivé de 20264101, rôle 98).
- Après le calibrage, **une seule ligne de configuration change** dans le code v4 : `DELTAS_V4 = None` devient `DELTAS_V4 = (δ_bas, δ_haut)`. L'empreinte du code au calibrage et celle d'après sont consignées au journal ; remettre l'ancienne ligne dans le code final redonne l'empreinte du calibrage.

## 3. Règles nouvelles de la v4, fixées avant tout calcul

1. **S18 = 0,10** (champ `taux_nonconv_max`), **N = 100**, **délai externe 9 000 s** : R-739, choisis après lecture du pilote v3 (à 0,05, risque d'arrêt par la garde ≈ 0,16 d'après 2 non-convergences sur 1 632, chiffre fragile dans les deux sens).
2. **Critère d'artefact de l'audit indépendant (S17, CM3-01)**, par δ, sur **K = 10 tâches de la décision par δ** (instances 0 à 9, aux deux δ : 20 tâches), bras **A**, B, C3, D, B′, C3′ :
   - pour chaque bras et chaque tâche, « choix source » = la meilleure des deux réponses de la décision (standard, renforcée), « choix audit » = la meilleure du choix source et des trois réponses de l'attaquant indépendant (selon leurs évaluations propres) ; les deux choix sont **réévalués sur un même échantillon frais** (graine commune ; si le choix ne change pas, l'écart est nul au bit), ce qui retire le biais de sélection du minimum (CM3-01, point 3) ;
   - pour chaque contraste audité (**B − A**, B − C3, B − D, B′ − D, B′ − C3′) : c_i = contraste sur les choix audit réévalués − contraste sur les choix source réévalués ; c̄ = moyenne sur les K tâches, ES = écart-type / √K ;
   - **artefact** si (i) |c̄| > m/2 = **0,01** (écart pratique : la moitié de la marge), **ou** (ii) |c̄| > t(K − 1 ; 0,995) × ES **et** la classe du contraste dans sa table (Table 1 par δ pour B − A ; Table 3 pour B − C3, B − D ; Table 6 pour B′ − D, B′ − C3′), recalculée en décalant l'estimation et toutes ses bornes de c̄, diffère de la classe lue ;
   - aucun changement de signe ne compte à lui seul (CM3-01, point 1).
   - **Condition d'application (Table 5, CM3-04)** : pour A, à chaque tour t, réponse renforcée (départs renforcés + départs structurés + attaque du tour) contre le moniteur déployé au tour t ; (iii) du tour audité = minimum de (iii) du tour et de la réponse renforcée évaluée sur un échantillon frais ; I1 et I3 recalculés ; artefact si |écart moyen de I1| > S15/2 = 0,01, ou si la ligne de la Table 5 recalculée avec I1 et I3 décalés de leurs écarts moyens diffère de la ligne lue et que l'un des deux écarts dépasse t(K − 1 ; 0,995) × ES.
   - Taux de fausse alerte vérifié par simulation avant le gel des seuils (bruit apparié estimé sur un audit d'essai du pilote v4, instances 0 à 4 aux deux δ, centré puis non centré ; tâches de décision simulées par rééchantillonnage du pilote v4). **Repli fixé d'avance** : si le taux simulé de fausse alerte sur l'ensemble des tests de l'audit dépasse 0,05, le multiplicateur de (ii) passe de t(K − 1 ; 0,995) à t(K − 1 ; 0,9995), et rien d'autre ne change.
3. **Déclencheur 9 étendu (CM3-04)** : « conforme et trop propre » couvre aussi P1 (plomberie), P10 (Q2 non exercée), P11 (Table 5) ; A entre dans l'audit. Pour P10, l'audit ajoute un contrôle de non-unicité : pour chaque tâche, le plus petit poids maximal parmi toutes les stratégies d'équilibre du défenseur du jeu restreint final (programme linéaire), qui dit si la pureté est forcée par le jeu ou tient au sommet rendu par le solveur (descriptif calculé pour toutes les tâches de B et B′).
4. **S10 (CM3-05)** : bande par bras et par δ = moyenne pilote ± k × écart-type par tâche du pilote × √(1/n_pilote + 1/N), **k = 3** (correction pour 16 bandes au niveau 5 % : Φ⁻¹(1 − 0,05/32) ≈ 2,95, arrondi) ; taux de fausse alerte des 16 bandes vérifié par simulation (pilote et décision tirés par tâches entières du pilote v4). **Repli fixé d'avance** : si le taux simulé dépasse 0,05, k = 4.
5. **Valeur nulle de I3 (CM3-03)** : sous échangeabilité des déplacements, E[I3] = moyenne sur t = 3 … T de (t − 2)/(t − 1) = 0,7345 à T = 8 ; l'indicateur lu est **I3 − valeur nulle**, avec son intervalle. **Table 5 réécrite** : « A progresse » (borne basse de I1 > S15) ; « A ne progresse pas, retours au-delà du hasard (cycle) » (borne haute de I1 < S15 et borne basse de I3 − nul > 0) ; « A ne progresse pas, sans retours au-delà du hasard » (borne haute de I1 < S15 et borne haute de I3 − nul < 0) ; « A ne progresse pas, forme indéterminée » ; « indéterminé ». I2 renommé « baisse de détection des attaques passées (oubli ou saturation) », recopié sans verdict ; H et I2 de B et B′ portent sur les moniteurs un à un, pas sur la défense mixte.
6. **Pureté** : un poids ≥ 1 − 10⁻⁹ (le code suit le texte, CM3-12 c). Descriptives ajoutées : B′ − D et B′ − C3′ selon la pureté (tâches pures, tâches à mélange réel), indice du moniteur de poids maximal de B′.
7. **Garde relative de variance de `MoniteurOu` (CM3-15)** : écart-type du score propre d'un membre > 10⁻⁶ × max(1, |moyenne|).
8. **Non ajoutés** (déclaré) : maxout unique de 73 unités (diagnostic non opposable de la contre-lecture 3 : ne change rien ; coût d'ordre de grandeur : il doublerait au moins le temps par tâche et sortirait du délai de 9 000 s) ; témoin « mode » de B′ (option pour Lazar, CM3-02 « si Lazar y consent ») ; « ou » restreint au support de B′ (option pour Lazar, CM3-07).
9. Rien d'autre ne change dans les bras A, B, C1, C2, C3, D, B′, C3′ : même code de calcul, mêmes graines par bras ; essai de continuité contre le code v3 (sorties identiques champ à champ sur une même racine).

## 4. Prédictions pour le pilote v4 (racine 20264201), écrites avant tout calcul ; δ_bas et δ_haut = ceux que rendra la règle du § 2

| Quantité | δ_bas : prédit (confiance) | δ_haut : prédit (confiance) | Branche opposée |
|---|---|---|---|
| V(A) moyen au pilote | ≥ 10α (0,6) | ≥ 3α (0,5 : la règle place δ_haut près du seuil) | sous le seuil |
| B − A (iii) | + (0,9) | + (0,9) | ≤ 0 |
| B − C1, B − C2 (iii) | + (0,7) | + (0,7) | ≤ 0 |
| B − C3, B − D (iii) | − (0,9) | − (0,9) | ≥ 0 |
| B − A (ii) | − (0,8) | − (0,8) | ≥ 0 |
| B′ − D (iii) | \|·\| < 0,02 (0,8) | \|·\| < 0,02 (0,8) | \|·\| ≥ 0,02 |
| B′ − C3′ (iii) | + (0,7) | + (0,7) | ≤ 0 |
| part pure de B′ | > 0,5 à au moins un δ (0,7) | | ≤ 0,5 aux deux δ |
| pureté forcée (plus petit poids maximal parmi les équilibres ≥ 1 − 10⁻⁶) parmi les tâches pures de B′ | ≥ 0,8 (0,7) | ≥ 0,8 (0,7) | < 0,8 |
| A : \|I1\| < 0,02 | (0,75) | (0,75) | \|I1\| ≥ 0,02 |
| A : I3 − 0,7345, borne basse B2 > 0 (cycle) | (0,7) | (0,7) | borne basse ≤ 0 |
| D : I3 − 0,7345 < 0 | (0,7) | (0,7) | ≥ 0 |
| Temps par tâche (8 bras) | 45 à 75 s (0,7) | | hors plage |

Audit d'essai du pilote v4 (instances 0 à 4, deux δ) : aucun drapeau (i) (0,9). Simulations : fausse alerte de S10 à k = 3 ≤ 0,05 (0,6) ; fausse alerte de l'audit ≤ 0,05 (0,7).

## 5. Après le pilote v4

Aucune modification des règles fixées ici, hors les deux replis écrits d'avance (§ 3.2, § 3.4). Seuls viennent du pilote v4 : les chiffres des prédictions pour la décision, les bandes S10, le temps projeté, les tailles et probabilités simulées. Toute correction de code révélée par les essais ou le pilote est consignée au journal avec sa raison et sa nouvelle empreinte ; une correction qui change un résultat du pilote oblige à le rejouer sur la racine réservée 20264211 / 20264212.
