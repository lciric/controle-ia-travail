# Témoins plantés de la course « conception propre » — v1

Écrits ou tirés le 13 novembre 2026 (entre 23:05 et 23:20 UTC, heures relevées par `date -u` ; tirage et validation à 23:13 UTC) par le préparateur neuf (modèle A, qui est aussi le
modèle d'un proposeur et du juge `opus-juge` : « tiers » vaut pour l'instance, pas pour le modèle). Règle de sélection et
usage : `conception-course-v1.md`, § 4 à 7.

## Fichiers

| Fichier | Contenu | Servi à |
|---|---|---|
| `temoins-organisme-conception-propre-v1.json` | 4 témoins aux classes imposées par l'orchestrateur (vrai, jumeau, faux de falsifiabilité, faux d'antériorité) | juge de l'organisme (exigé par le code) ; mêlés aussi à la pile du lecteur |
| `temoins-lecteur-v1.json` | 12 témoins du lecteur (les 4 précédents + 6 conceptions publiées + 2 fausses fiches), avec la cible et les valeurs attendues critère par critère | programme de classement seul (le lecteur ne voit que les fiches) |
| `temoins-hasard-v1.json` | 8 idées tirées au hasard (`outils/tirer_fiches_hasard_v1.py`, entropie 2026111301, une graine fille par fiche, numpy 2.4.6) | idem |
| `catalogue-conceptions-publiees-v1.md` | 12 entrées C1 à C12 | lecteur |

Les 20 fiches de témoins passent le validateur réel de l'orchestrateur (`valider_fiche_ideation`, sans appel) et aucune ne
déclenche la garde lexicale « niveau méthode » ; les 4 de l'orchestrateur passent `charger_temoins` (quatre classes)
(`outils/valider_temoins_v1.py`, résultat `outils/resultat-valider-temoins-v1.txt`). Le clone est resté propre.

## Les conceptions publiées (7), et leur source vérifiée (R7)

Chaque témoin réécrit le **mécanisme central** d'une conception publiée dans le vocabulaire de l'organisme, sans nom ni
référence, et se dit « inédit ». Chaque mécanisme a été relu, le 13 novembre 2026, sur le PDF du dépôt, empreinte vérifiée
contre son compagnon, à la page citée.

| Code | Témoin (nom de la fiche) | Conception, référence | PDF (empreinte), page, ce qui y est lu |
|---|---|---|---|
| T-FA | « Validation des cartes par falsifications séquentielles à valeurs e combinées » | C2, POPPER (Huang, Jin, Li, Li, Candès, Leskovec ; ICML 2025, PMLR 267) | `pdf/huang-2025-icml-…-sequential-falsifications.pdf` (`a3c4b370…`) : p. 2, valeurs p converties en valeurs e et combinées, contrôle strict de l'erreur de première espèce ; p. 3 (figure 1), validation quand la valeur e agrégée dépasse 1/α |
| T-CS | « Tournoi à cotes Elo entre cartes, par débats appariés, pour ordonner le test de mort » | C1, Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026) | `co-scientist-v1/gottweis-2026-nature-655-487-….pdf` (`351f49d8…`) : p. 489 de la revue, tournois qui comparent et classent les hypothèses ; p. 13 du PDF (méthodes, « Ranking agent »), tournoi à base d'Elo, cote initiale 1 200, comparaisons appariées en débats à plusieurs tours pour les mieux classées, une seule pour les autres, appariement par le graphe de proximité |
| T-AIS | « Archive d'idées qui grandit et filtre de nouveauté par recherche bibliographique » | C3, The AI Scientist (Lu, Lu, Lange, Foerster, Clune, Ha ; arXiv 2408.06292v3, 2024) | `pdf/2408.06292v3.pdf` (`e911f900…`) : p. 4, archive d'idées, modèle comme opérateur de mutation, notes auto-attribuées, filtre par l'interface de Semantic Scholar et le Web qui écarte les idées trop proches de la littérature |
| T-FKF | « Fourches à contexte neuf et reprise depuis la meilleure trajectoire » | C5, Fork-and-Flush (Cai, Ziakas, Kontonis, Pearce, Sen, Krishnamurthy, Garg, Papailiopoulos ; arXiv 2610.07447v1, 2026) | `arxiv-bassins-idees-20261113/arxiv-2610.07447v1.pdf` (`4eba26a1…`) : p. 1, trajectoires parallèles héritant de l'espace de travail avec un contexte neuf, reprise depuis la mieux notée après un horizon fixe, à calcul égal contre exécution unique et meilleur de N |
| T-PACE | « Porte d'acceptation séquentielle appariée pour les réécritures de la consigne des proposeurs » | C7, PACE (arXiv 2606.08106v1, 2026) | `pdf/2606.08106v1.pdf` (`779f4960…`) : p. 1, comparaison à la version en place sur les mêmes instances, adoption quand un e-processus par paris accumule une preuve décisive, arrêt anticipé, fausse adoption bornée par décision même sous arrêt optionnel, contre « garder si le score a monté » |
| T-DW | « Réserve de tirages frais réutilisable par un mécanisme à seuil bruité » | C11, Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (arXiv 1506.02629v2, 2015) | `pdf/anteriorite-P-041-v2/c8/1506.02629.pdf` (`dcfbb9aa…`) : p. 1, méthode simple et pratique pour réutiliser une réserve de test de façon adaptative sans surajustement. **Réserve** : le détail du mécanisme à seuil bruité (comparaison au jeu d'apprentissage, valeur bruitée rendue au-delà d'un seuil) n'a pas été relu page par page ici ; seul le principe l'a été |
| T-PD | « Ne payer les tirages frais du juge que là où la carte et l'archive divergent » | C9, Pay Only for Disagreement (Balachandran ; arXiv 2609.17560v1, 2026) | `pdf/2609.17560v1.pdf` (`ef318a96…`) : p. 1, la différence de risque vit sur les entrées de désaccord, observables sans étiquette ; palier sans étiquette sous une tolérance de désaccord ; palier audité qui n'étiquette que des désaccords échantillonnés, séquence de confiance valide à tout instant |

Entrées du catalogue **sans témoin** (leurres, pour que le lecteur ne puisse pas déduire qu'à chaque entrée répond une
fiche) : C4 (The AI Scientist-v2, `pdf/2504.08066v1.pdf`, `53bafd30…`, p. 1), C6 (Scaling Discovery Requires Forgetting,
`arxiv-2610.20563v1.pdf`, `9c14df83…`, p. 1), C8 (Ensemble Monitoring, `pdf/2605.15377v2.pdf`, `fe591700…`, p. 1), C10
(E-valuator, `pdf/2512.03109v2.pdf`, `b7a46e4c…`, p. 1), C12 (The Ladder, `…/c8/1502.04585.pdf`, `957ef473…`, p. 4 :
« only for those that made a significant improvement », p. 5 : mécanisme).

## Valeurs attendues (scellées dans `temoins-lecteur-v1.json`)

1 = le critère doit tenir ; 0 = il doit manquer ; « — » = non fixé (rapporté seulement). R4 vaut 1 hors `levier:juge`.

| Code | Famille | Cible | R1 | R2 | R3 | R4 | R5 | R6 | R7 | N |
|---|---|---|---|---|---|---|---|---|---|---|
| T-V | vrai | doit passer | 1 | 1 | 1 | 1 | 1 | 1 | 1 | aucune |
| T-J | jumeau de T-V | doit passer | 1 | 1 | 1 | 1 | 1 | 1 | 1 | aucune |
| T-FF | faux | R1 | 0 | 0 | 1 | 1 | — | 0 | — | aucune |
| T-FA | publiée | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | C2 |
| T-CS | publiée | N | 1 | 1 | 0 | 0 | 1 | 1 | 1 | C1 |
| T-AIS | publiée | N | 1 | 1 | 0 | 1 | 1 | 1 | 1 | C3 |
| T-FKF | publiée | N | 1 | 1 | 0 | 1 | 1 | 1 | 1 | C5 |
| T-PACE | publiée | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | C7 |
| T-DW | publiée | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | C11 |
| T-PD | publiée | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | C9 |
| T-F58 | faux | R2 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | aucune |
| T-F53 | faux | R3 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | aucune |
| T-H1 à T-H8 | hasard | R7 | — | — | — | — | — | — | — | aucune |

Pourquoi ces attentes : T-CS fait décider l'ordre du test de mort, donc les promotions sous budget, par des juges à modèle
(R3) et ne dit aucune garantie (R4) ; T-AIS sert le Web à un modèle qui écarte des cartes (R3) ; T-FKF choisit la trajectoire
sur les cartes promues par le juge (R3 : N-053, N-058) ; T-F58 mesure et choisit sur les promotions par dollar (R2, R3) ;
T-F53 sert une note de nouveauté aux proposeurs (R3 : rejet établi et N-053) ; T-FF n'a ni seuil, ni mesure par l'oracle,
ni contrôle négatif.

## Ce qu'on mesure sur eux

- **Sensibilité de N** : part des 7 publiées reconnues avec la bonne entrée (L1 : au moins 5) ; détail par lecture.
- **Spécificité** de R1, R2, R3 : les trois fausses fiches, chacune à son critère, dans les deux lectures (L2).
- **Faux rejets** : T-V et T-J passent les portes et restent neufs (L3) ; leur accord mutuel.
- **Hasard** : part des huit idées tirées au hasard qui passent les portes, et test L5 (fiches réelles contre hasard).
- **Exactitude du lecteur** sur chaque critère aux valeurs fixées, par lecture ; passages non prouvés.
- **Juge de l'organisme** (information, après le scellement du classement) : ses classes attendues sur les quatre témoins
  de l'orchestrateur (vrai et jumeau éligibles ; T-FF inéligible, falsifiabilité ≤ 1 ; T-FA inéligible, originalité ≤ 1,
  POPPER étant déjà dans les faits : valeurs e et règle de Benjamini et Hochberg sur les valeurs e).

## Réserves

- Témoins écrits par le modèle d'un proposeur ; style et longueur peuvent les trahir ; les idées tirées au hasard ont un
  style mécanique visible (nom « Doubler : … »). L5 en est d'autant plus facile ; c'est dit, non corrigé.
- T-DW : principe vérifié page 1 ; détail du mécanisme non relu page par page (voir tableau).
- T-FA est aussi en partie occupé par les faits servis (l'organisme emploie déjà des valeurs e) : c'est voulu pour le juge
  de l'organisme (faux d'antériorité), et indifférent pour le lecteur (entrée C2).
