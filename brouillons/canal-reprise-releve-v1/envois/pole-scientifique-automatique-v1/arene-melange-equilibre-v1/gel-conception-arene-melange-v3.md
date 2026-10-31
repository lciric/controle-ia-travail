# Gel de la conception v3 — arène « mélange d'équilibre » — écrit AVANT toute exécution de B′ et avant le pilote v3

Sous-agent neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026, 10:24 UTC (relevé `date -u`) ; il n'a écrit ni le brouillon 1, ni le brouillon 2, ni les codes v1 et v2, ni les contre-lectures. Ce fichier fixe la conception v3 et les prédictions **avant** toute exécution du code v3 qui touche B′ ou C3′ (essais du code compris) et avant le pilote v3 sur RACINE_ESSAI = 20261311 / 20261312. Son empreinte est consignée au journal `journal-pilotes-arene-melange-v3.txt` avant ces exécutions.

## 0. Nature du changement : bifurcation de conception postérieure au pilote v2 (déclarée)

La contre-lecture 2 (`contre-lecture-arene-melange-v2-brouillon2.md`, `c6751de38ca84f716d424bc34dccd4103757423932204011a65136bd861cc427`, CM2-02 et CM2-03) établit que la réfutation prédite de l'hypothèse principale du brouillon 2 tient à la **classe de fonctions** (B tire un seul moniteur linéaire à la fois, 7 paramètres sur 63 ; C3 et D les déploient tous), pas au tirage au hasard. L'ajout d'une comparaison à classe de fonctions égale est une **décision de routine de conv-audit**, prise **après** la lecture du pilote v2 et de la contre-lecture : c'est un changement de conception postérieur à un pilote, déclaré comme tel. Conséquences : (a) toutes les racines d'essai déjà employées (20261291 à 20261298, 20269501, 20269502) sont refusées par garde en v3 ; (b) les prédictions Q2 ci-dessous sont écrites avant tout calcul de B′, avec leur raisonnement ; (c) les bras A, B, C1, C2, C3, D sont gardés tels quels (même code de calcul, mêmes graines par bras ; la matrice de détection croisée ajoutée ne tire aucune graine nouvelle) ; (d) les δ restent (1,4 ; 1,8) (pas de changement de δ sans décision de Lazar, CM2-06).

Code au moment du gel : `arene_melange_v3.py` `04df57d2761a1249691624f131829bf0bb11749855051b2c2feb5350d1c93721` (jamais exécuté : seule une compilation syntaxique a été faite). Toute modification ultérieure du code (correction révélée par les essais) est consignée au journal avec sa raison et sa nouvelle empreinte ; aucune ne touche à la conception fixée ici.

## 1. Conception gelée v3

1. **Deux questions.**
   - **Q1** (celle du brouillon 2, renommée) : le mélange d'équilibre de moniteurs linéaires B bat-il ses témoins **à nombre de paramètres égal** (63) — C1 (mêmes moniteurs, poids uniformes), C2 (poids de Dirichlet), C3 (« ou » déterministe des mêmes moniteurs), D (maxout unique à 9 unités) ? B déploie 7 paramètres (un moniteur linéaire) par requête ; C3 et D en déploient 63.
   - **Q2** (nouvelle) : **à classe de fonctions égale**, le mélange d'équilibre B′ bat-il D et C3′ ?
2. **B′** : double oracle tronqué à T = 8 tours, même schéma que B (jeu restreint, programme linéaire, stratégie d'équilibre q de l'attaquant), mais l'oracle du défenseur (oracle « détection », le même pour tous) rend à chaque tour un moniteur **maxout à `unites_Bp` = 9 unités**, la classe du moniteur final de D (T + 1 = 9 unités, 63 paramètres). Le moniteur commun du tour 0 (linéaire, sous-classe) est gardé. B′ déploie par requête un maxout à 9 unités (63 paramètres, ou 7 si M0 est tiré), comme D ; il stocke 7 + 8 × 63 = 511 paramètres.
   - **Pourquoi pas « même total de paramètres que D »** : avec 9 moniteurs, l'égalité du total (63) et l'égalité de classe par moniteur ne peuvent tenir ensemble que pour des moniteurs linéaires (c'est B). La v3 retient l'égalité de **classe** et de **paramètres déployés par requête** pour B′ contre D, et l'égalité des **moniteurs et du total** pour B′ contre C3′. Un maxout unique de 73 unités (même total que B′) n'est pas dans l'expérience : lacune déclarée, option écrite pour Lazar (coût élevé).
3. **C3′** : « ou » déterministe des 9 moniteurs mêmes de B′ après le tour T : z_i = (s_i − μ_i)/σ_i sur le propre de calibration, score log-somme-exp_i(λ z_i), λ = S7 = 8, seuil recalibré à α (classe `MoniteurOu` ; identique à `ou_deterministe` sur des moniteurs linéaires, vérifié par essai). 511 paramètres.
4. **Condition d'application (CM2-03)** : pour A (verdict) et B, D, B′ (descriptif), matrice H (moniteur déployé au tour s = 0 … T × attaque du tour t = 1 … T, taux sur les échantillons d'évaluation fixés de chaque attaque) ; I1 = moyenne de (iii) aux tours 5–8 moins aux tours 1–4 (progrès de la défense unique) ; I2 = moyenne sur t = 1 … 7 de H[t, t] − H[8, t] (oubli des attaques passées par le moniteur final) ; rétention par décalage ; I3 = part des tours t ≥ 3 où l'attaque revient vers une attaque d'un tour ≤ t − 2 (cosinus des déplacements), descriptif. Table 5 (verdict par δ, bornes Bonferroni sur 2 δ, marge S15) : « A progresse » si borne basse de I1 > S15 ; « A ne progresse pas, avec oubli » si borne haute de I1 < S15 et borne basse de I2 > S15 ; « … sans oubli » si borne haute de I2 < S15 ; « … oubli indéterminé » ; sinon « indéterminé ». La condition d'application est « vérifiée » si A ne progresse pas aux deux δ.
5. **Marges par principe, sans pilote (CM2-04)** : m = S1 = 0,02 (deux fois α) pour les quatre témoins de Q1 et les deux contrastes de Q2, aux deux δ ; équivalence bilatérale ]−m ; +m[ (« un témoin équivaut à B si leur écart est démontré dans ]−0,02 ; +0,02[ ») ; S15 = 0,02 par le même principe. Aucune marge ne dépend de B − A.
6. **Multiplicité** : Q1 = 8 tests (Bonferroni 8, équivalence au niveau 0,05/8) ; Q2 = 4 tests (Bonferroni 4 : quantiles 0,625 % et 99,375 % ; équivalence 0,05/4 : 1,25 % et 98,75 %) ; deux familles distinctes, chacune à 5 %.
7. **Q2 non exercée** : si les poids finaux de B′ sont purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches d'un δ, Q2 est « non exercée » à ce δ (le tirage au hasard n'est pas exercé, R5 « chemin non exercé »).
8. **R4, déclencheur 9 (CM2-05)** : si le résultat est conforme aux prédictions (Q1 réfutée par C3 ou D, ou Q2 réfutée), contrôle d'attaquant indépendant sur 10 tâches **de la décision** (instances 0 à 4, aux deux δ) pour B, C3, D, B′, C3′ : SLSQP lourd (12 départs structurés, 100 départs tirés, attaques passées et finales, 1 024 échantillons par composante, 300 itérations), puis stratégie d'évolution (1 + 12) sans gradient, 400 générations, depuis la réponse lourde et depuis l'attaque finale standard ; V_audit = minimum de V et des trois réponses ; **artefact** si, dans un δ, la moyenne sur les tâches auditées de B − C3, B − D, B′ − D ou B′ − C3′ change de signe ou de plus de 0,05. Cet audit ne bloque pas la Table 1 ; il bloque la phrase de synthèse des Tables 4 et 7.
9. **S10 (CM2-08)** : bande par bras et par δ = moyenne pilote ± 5 × écart-type par tâche du pilote / √N.
10. **Arrêt par PID (CM2-14)** : PID et instant de départ des processus de travail consignés ; signal TERM converti en arrêt du pool ; à la sortie, arrêt par PID des survivants et garde « aucun orphelin » ; commande `orphelins` exigée avant toute reprise.

## 2. Prédictions signées, écrites avant toute exécution de B′

### 2.1 Q2 — raisonnement

(a) Pour des moniteurs fixés et une même fausse alerte α, la détection d'un mélange contre une attaque donnée est la moyenne pondérée des détections de ses moniteurs : l'attaquant qui joue en dernier ne perd contre un mélange que s'il n'existe pas d'attaque qui échappe à presque tous les moniteurs à la fois, c'est-à-dire si leurs angles morts **diffèrent**. (b) Des moniteurs linéaires en dimension 6 ont chacun une direction, donc des angles morts très différents : le tirage au hasard y vaut quelque chose (B − A = +0,13 au pilote v2), mais l'agrégation déterministe des mêmes moniteurs vaut plus (C3, D). (c) Un maxout à 9 unités couvre déjà les trois directions des composantes et le repli vers l'origine : les angles morts des moniteurs de B′ se recouvrent davantage ; il reste moins à exploiter par le tirage. (d) L'oracle de B′ entraîne chaque moniteur contre la stratégie d'équilibre q de l'attaquant, concentrée sur quelques attaques ; D est entraîné contre toutes les attaques passées à poids égaux, ce qui le rend vraisemblablement plus robuste à une attaque nouvelle. (e) Le « ou » C3′ couvre la réunion des angles morts des 9 moniteurs pour un coût de seuil faible (queues gaussiennes, le même argument qu'en Q1). (f) Le jeu restreint tronqué surestime la valeur de B′ (comme pour B, +0,015 à +0,025 en v2).

### 2.2 Q2 — prédictions (branche prédite ; branche opposée qui réfute)

| Contraste (iii) | δ = 1,4 : prédit (confiance) | δ = 1,8 : prédit (confiance) | Ordre de grandeur prédit | Branche opposée (réfutation, déclencheur 1) |
|---|---|---|---|---|
| B′ − D (Q2) | − : D ≥ B′ (0,60) | − : D ≥ B′ (0,55) | dans [−0,10 ; +0,02], centre −0,03 | moyenne > 0 (le tirage au hasard paie à classe égale) |
| B′ − C3′ (Q2) | − : C3′ ≥ B′ (0,70) | − : C3′ ≥ B′ (0,65) | dans [−0,12 ; 0], centre −0,04 ; moins négatif que B − C3 au même δ | moyenne > 0 |
| B′ − B (descriptif) | + (0,80) | + (0,80) | +0,05 à +0,25 | moyenne ≤ 0 |
| C3′ − D (descriptif) | + (0,55) | + (0,55) | proche de 0 | moyenne ≤ 0 |
| Poids de B′ | support moyen ≥ 2 et part pure ≤ 0,5 (0,55) | idem (0,55) | — | part pure > 0,5 (Q2 « non exercée ») |

Lecture prédite de Q2 (Table 7, m = 0,02) : **« Q2 réfutée »** (au moins un des deux témoins « X > B′ » ou « ≈ » à chaque δ), confiance 0,6. La branche « Q2 confirmée » (B′ bat D et C3′ d'au moins 0,02 aux deux δ) contredit la prédiction et déclenche l'audit (R4, symétrie) ; elle n'est pas visée (R3).

### 2.3 Condition d'application — prédictions

| Indicateur | δ = 1,4 | δ = 1,8 | Raison | Branche opposée |
|---|---|---|---|---|
| A, I1 (progrès) | \|I1\| < 0,02 (0,75) | \|I1\| < 0,02 (0,75) | (iii) de A par tour au pilote v2 : 0,061 0,052 0,046 0,047 0,055 0,051 0,052 0,056 (moyenne sur les deux δ), soit I1 ≈ +0,002 | I1 ≥ 0,02 |
| A, I2 (oubli) | > 0,02 (0,65) | > 0,02 (0,65) | un moniteur linéaire réentraîné sur un nombre croissant d'attaques de directions différentes fait un compromis : il détecte moins une attaque ancienne qu'au tour qui a suivi son apparition | I2 ≤ 0,02 |
| Table 5 | « A ne progresse pas, avec oubli » (0,5) | idem (0,5) | conjonction des deux lignes | toute autre ligne |
| B, D, B′, I1 (descriptif) | > 0 (0,8) | > 0 (0,8) | (iii) par tour croissant pour B et D au pilote v2 | ≤ 0 |

Lecture prédite : condition d'application **vérifiée** au sens de la Table 5 (A ne progresse pas), avec oubli. Elle ne dira pas pourquoi : « plafond de la classe linéaire » et « cycle » ne sont distingués que par I2 et I3.

### 2.4 Q1 sur le pilote v3 (racine fraîche) — prédictions

Signes du pilote v2 reconduits : B − A (iii) + (0,9 aux deux δ) ; B − C1 + (0,7) ; B − C2 + (0,7) ; B − C3 − (0,9) ; B − D − (0,9) ; B − A (ii) − (0,8). Classes sous m = 0,02 non prédites avec confiance pour C1 et C2 (écarts pilotes v2 de +0,018 à +0,037, voisins de la marge) ; « C3 > B » et « D > B » prédits (0,9) ; Q1 « réfutée » (0,9).

### 2.5 Temps

Prévu par tâche (8 bras) : 45 à 70 s de processeur (v2 : 30 s pour 6 bras ; ajout de la trajectoire de B′, de 8 entraînements maxout à 9 unités, et des finales de B′ et C3′). Le run de décision à N = 100 risque de dépasser 1 h 15 de mur sur 2 cœurs : S4 et S8 seront recommandés après mesure.

## 3. Après le pilote v3

Aucune modification de la conception fixée ici. Seuls les chiffres des prédictions pour la décision, les bandes S10 et les valeurs recommandées de S4 et S8 viennent du pilote. Les marges (S6, S15) et le critère d'artefact (S17) sont fixés ci-dessus, par principe.
