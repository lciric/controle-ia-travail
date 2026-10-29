# Emprunt de la proposition 13 de 2609.17560 (borne composée à budget unique) dans le bras du juge figé — squelette de préenregistrement — v1

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 08:11 UTC. Suite à la proposition de Lazar (29 octobre,
≈ 02:25 heure de Paris : « la borne de boucle de notre bras équivaut à sa répartition égale à horizon connu : et si on l'empruntait ? »),
à la reproduction scellée (`reproduction-borne-boucle-2609.17560-v1/`, R-402) et au rapport d'antériorité Q2 v2 (`anteriorite-Q2-v2.md`,
R-396). **Brouillon, non scellé comme préenregistrement** : l'emprunt est une proposition (défaut sous 48 h : oui, R-396/R-398 ;
échéance ≈ 30 octobre 01:30 UTC) ; la réécriture de la revendication Q2 est un nœud (modification de revendication) qui attend le mot
de Lazar. Ce squelette prépare le préenregistrement (R1) pour qu'il soit scellé dès le mot, et contre-lu (R2) par un sous-agent d'un
autre modèle avant scellement.

## 1. Ce qu'on emprunte, mot pour mot (à vérifier sur PDF avant scellement, R7)

2609.17560, proposition 13 (p. 12, extrait `corpus-primaire-v2/extrait-2609.17560-v1.md`) : pour une suite d'audits k = 1, 2, …, chacun
muni d'une suite de confiance valable à tout instant au niveau δ_k, **la validité familiale** (aucune fausse certification sur toute la
suite, probabilité ≥ 1 − Σ δ_k) tient par la **borne d'union** sur un **calendrier** de δ_k — répartition égale δ_k = δ/K à horizon K connu,
ou δ_k ∝ k⁻² à horizon inconnu — **sans indépendance entre audits**, sur trafic frais ou partagé, **tant que les candidats ne dépendent
pas du jeu audité** ; coût de chaque audit en log(1/δ_k) (théorème 7). Ce que notre bras fait déjà : richesse de pari mélangée sur Λ,
promotion au seuil m/α, e-BH pondéré — **la répartition égale à horizon connu, sans le dire**. L'emprunt consiste à **le dire, à citer la
proposition 13 comme garantie de la boucle, et à préenregistrer les conditions sous lesquelles elle tient chez nous** (R-396 : « pas une
nouveauté en soi »).

## 2. Ce qui, chez nous, viole ses hypothèses (reproduction v1, cellules C et E — INFÉRÉ, hors extrait)

| hypothèse de la proposition 13 | notre bras | effet mesuré (monde synthétique, δ = 0,05, 20 audits) |
|---|---|---|
| candidats indépendants du jeu audité | **jeu fini réutilisé et candidats choisis sur ce jeu** (la course sélectionne le meilleur de m variantes sur les mêmes unités) | 0,023 → 0,07 (m = 5), 0,18 (m = 20), 0,34 (m = 100) ; exploitation des points étiquetés : 1,00 dès le deuxième audit |
| perte déterminée par la prédiction (étiquette vraie) | **verdict lu par un juge-modèle** | juge biaisé + 0,1 : 1,00 ; juge sans biais mais bruité (10 %) : 0,31 à 3 000 points, 1,00 à 20 000 (atténuation de Δ contre une tolérance) |
| juge qui n'oriente que l'acheminement | notre juge rend le verdict | si le juge n'oriente que l'acheminement : 0,0245 (couverture tenue, p. 9-10) |

## 3. Remèdes mesurés (cellules D) — ce que le préenregistrement doit choisir

- **D-i, unités neuves à chaque génération** (jamais réutilisées pour la sélection) : 0,031 / 0,025 — la borne tient, au prix d'unités
  fraîches (≈ 9 000 points par suite dans le monde synthétique). C'est la fraîcheur **K9-1** du juge figé : à écrire comme condition.
- **D-ii-a, nulles de bibliothèque injectées** : l'alarme ne détecte le gonflement que si les nulles **passent par la boucle** (0,089 contre
  0,017 figées hors boucle) ; sous exploitation, alarme 1,00 (passées) contre 0,020 (figées). → **les nulles injectées sont traitées comme
  des candidats, dans la boucle, jamais figées à part** (N-053 : jamais de sélection sur le verdict).
- **D-ii-b, recalibrage par les nulles** (380 nulles) : 0,040 sous sélection ; 0,000 sous exploitation (**R4 : trop beau, réserve** — la
  puissance y tombe à 0).
- **D-iii, seuil × m ou e-BH pondéré** : 0,0125 sous sélection (seuil × 20) mais 1,00 sous exploitation ; e-BH pondéré 0,17 / 1,00 → **ne
  suffisent pas seuls**.
- **D-iv, parts jamais réutilisées** : 0,009 mais puissance 0,04 — inutilisable.

## 4. Squelette du préenregistrement (gabarit `prereg/gabarit-preregistrement-v1.md`)

- **Hypothèse H-E13** : dans la boucle du juge figé (générations de l'organisme, candidats sélectionnés par la course), avec (i) unités
  **neuves à chaque génération** pour toute promotion (K9-1), (ii) **nulles de bibliothèque des deux signes injectées comme candidats dans
  la boucle** (part fixée, ≥ 10 % des candidats par génération — à chiffrer), (iii) calendrier δ_k = α/K à horizon K connu (K = nombre de
  générations écrit d'avance), la part de suites avec au moins une fausse promotion est **≤ α** ; **sans (i)**, elle dépasse α d'un facteur
  ≥ 3 dès m = 5 variantes sélectionnées sur le même jeu.
- **Prédiction chiffrée et signe** : avec (i)-(iii), fausses promotions de nulles injectées ≤ 0,05 (Wilson 95 % haut ≤ 0,08) sur ≥ 2 000
  suites synthétiques, **et** sur les générations réelles : aucune nulle injectée promue dans la première campagne (0 sur n, n ≥ 20) ;
  sans (i) (bras témoin à jeu réutilisé, simulation seulement) : ≥ 0,15 à m = 20.
- **Métrique** : part de suites à fausse promotion (nulles injectées) ; taux par audit ; étiquettes (coût) ; puissance sur bons candidats.
- **Plan d'analyse gelé** : cellules A (frais), C (réutilisé + sélection, témoin), D-i + D-ii-a (notre bras) ; graines `SeedSequence`,
  manifeste ; lecture par un sous-agent neuf (R13) ; aucun chiffre lu avant scellement.
- **Critères de lecture** : H-E13 tenue si D-i + D-ii-a ≤ 0,08 (borne haute) et témoin C ≥ 0,15 ; **suspecte de propreté** si D-i + D-ii-a
  = 0 sur ≥ 2 000 suites (R4, audit) ; non concluante sinon.
- **Liste d'arrêt** : nulles injectées promues en réel → arrêt de la campagne, nœud ; juge qui rend un verdict non fini → pas de lecture ;
  réutilisation d'une unité entre générations détectée (fraîcheur K9-1 violée) → génération annulée.
- **Ce qui change dans le code** : rien dans le pari apparié ; le **calendrier** δ_k = α/K écrit au manifeste de la boucle (K connu) ; les
  nulles injectées marquées comme candidats et comptées ; un essai R5 (cas sain : nulle non promue ; artefact : nulle promue par un juge
  mutant biaisé → alarme).

## 5. Réserves et ce qui manque

- Les chiffres du § 2-3 sont **synthétiques, non opposables** ; la proposition 13 n'est pas reproduite sous juge-verdict (cellule E1 :
  1,00) : **l'emprunt ne couvre pas le juge-modèle qui rend le verdict** — c'est la zone encore vierge de Q2 (verdict lu par un
  juge-modèle sur jeu réutilisé), à garder comme revendication propre, pas comme emprunt.
- Vérification sur PDF des pages 12 et 22 (allocation adaptative non permise) et de l'annexe B (trafic partagé) avant scellement.
- La part de nulles injectées et K sont à fixer ; le coût (unités neuves à chaque génération) entre au devis de la campagne.
- Non contre-lu (R2) : à faire par un sous-agent d'un autre modèle avant scellement, après le mot de Lazar.
