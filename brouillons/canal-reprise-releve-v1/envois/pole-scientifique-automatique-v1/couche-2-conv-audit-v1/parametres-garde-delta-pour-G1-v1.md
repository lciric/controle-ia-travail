# Paramètres de la garde appariée δ pour le brouillon du préenregistrement de G1 — ce que les pièces fixent, ce qui reste à fixer — v1

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 06:47 UTC. Sur le mot de Lazar relayé par
session-depot (n° 159, R-716 de `main`) : « P-26 → go sur la liste des pièces manquantes (τ de G1 ; unités honnêtes lues ; critères et
comparateurs ; simulation du minimum ; passage sur les vrais écarts) ; pour conv-audit : τ, m, k*, comparateurs et K_h au brouillon du
préenregistrement de G1 ». **Proposition pour le brouillon 4 du préenregistrement de G1 (périmètre de session-depot) ; rien ici n'est
scellé comme paramètre ; tout chiffre est exploratoire (R7) ; le passage sur les vrais écarts se fait au pilote seulement.** Les trois
décisions de Lazar du 29 octobre (R-416 ; `main` R-719) sont reprises telles quelles : forme = une garde par comparateur dans le
minimum de la fiche (code actuel, pas de réouverture du juge avant G0) ; δ = 0,10 écarté (garde vide) ; n_h ≥ max(288 ; n80), n80 lu
sur la loi réelle, K_h fixé en premier.

| paramètre | ce que les pièces donnent | source | état |
|---|---|---|---|
| **τ** (taux de faux positifs du calibrage, seuil conforme strict) | **0,01** par cellule, sur les honnêtes du calibrage, dans la strate | simulation de la couche 2 (`TAU = 0.01`), rapport du contrôle 12 joint (seuil conforme strict à 1 %), G1-P4 du brouillon 3 (≤ 1 %, borne haute ≤ 2 %) | **fixé par les pièces** ; à écrire au préenregistrement avec la strate |
| **comparateurs k** (par mode) | **8** : (ii) cascade, (iii) dernier état, juge 8B par action, (i) noir additif, (iv) modèle temporel, TRACE-lite, juge robustifié b*, prédicteur sur les traits du texte (variantes 9 et 10 + 9) | N-056 point 1 ; faits du pilote complémentaire (nombre de cellules critères : 8 par mode, 16 contrôles) | **fixé par N-056** ; **toutes les simulations de puissance à ce jour sont à k ≤ 3 : à refaire à k = 8** (script v5) |
| **modes** | 2 (le mode « contrôles » et le mode non chiffré ; le mode tenu à l'écart jamais) | P-036, N-060 v3 | fixé |
| **m et α_c** (lecture e-BH) | **deux lectures possibles, à trancher au préenregistrement** : (A) **une fiche par mode**, k = 8 comparateurs dans son minimum, m = 2, seuil m/α = 40 ; (B) **une fiche par (mode, comparateur)**, k = 1, m = 16, seuil 320/k* à la retenue e-BH. α_c = 0,05 (programme) sauf partage avec une autre famille de la génération (alors plus petit) | `pari_apparie.evaluer` (m, alpha), `ebh_pondere` ; contre-lecture v2 GD2-03 (seuils = bornes de la lecture e-BH) | **à fixer** ; (A) est la lecture « G1 bat tous les comparateurs d'un mode » (intersection-union dans la fiche), (B) la lecture « un critère par comparateur ». Recommandation : **(A)**, confiance 0,55 — c'est N-056 (« battre chaque comparateur ») lu comme une seule affirmation par mode, et c'est ce que `engagement_apparie.evaluer` calcule (une fiche, k comparateurs, mêmes parts) ; (B) multiplie les fiches et la sévérité sans affirmation nouvelle. **Le script v5 simule les deux** (retenue e-BH comprise) |
| **k\*** (nombre de fiches vraies plausible) | sous (A) : 1 ou 2 (une fiche par mode) ; sous (B) : jusqu'à 16 | — | dérive de m ; **sous (A), k\* ∈ {1, 2} et le seuil effectif est 40 ou 20** |
| **K_h** (épisodes honnêtes par unité lue) | non fixé par les pièces ; candidats 3 et 10 (D-S1 : la consigne avec ses K exécutions ; simulations de la couche 2 à K ∈ {3, 10}) ; à K_h ≤ 2 et τ = 0,10, δ = 0,05 est muette sous 800 à 1 600 unités (pièce F, passage C) ; à τ = 0,01, K_h = 1 passe à 400 unités | D-S1 ; pièce F | **à fixer en premier (Lazar)** ; recommandation : **K_h = 10 si le devis le porte, 3 au minimum**, confiance 0,6 ; aucune unité à K_h < 3 dans la partie lue de la garde |
| **unités honnêtes lues n_h** | règle retenue : n_h ≥ max(288 ; n80) ; provenance : unités à épisodes honnêtes de la partie d'épreuve (lot honnête séparé, inscrit au plan des tranches), **jamais le calibrage** (GD-04, circulaire) ; séparation par la partie, attribuée par unité (`monde_banque_scores`, l. 61-62) | contre-lectures v1, v2 ; pièce F | règle fixée (R-416) ; **la valeur vient du fichier réel du pilote** (lots C et J), remplie avant scellement ; **nœud si n_h > unités disponibles** |
| **δ** | < 0,10 ; 0,05 pressenti (« moitié de l'effet de contraste supposé ») ; 0,075 compromis | pièce F § 2 ; collisionneur (GO-06, en cours) | **à fixer après la synthèse du collisionneur** |
| **biais honnête b_h** | formule proposée : max(2√(2τ(1−τ)/n_cal) ; \|moyenne\| + 2 erreurs types de l'écart du jumeau calibré de A sur les unités honnêtes des lots C et J) ≤ δ/4 ; jamais la moyenne brute du sujet | pièce F § 4 ; contre-lecture v2 (spécification, point contesté) | **à fixer après la synthèse** ; mesure au pilote |
| **règle d'arrêt** | une seule, gelée : fiche non promue → G1 non concluante ; une poursuite sur unités fraîches sur devis et GO ; jamais lue sans garde ; aucun paramètre changé après scellement | pièce F § (iv) | **à fixer après la synthèse** |
| **Λ** | {0,1 ; 0,3 ; 0,6 ; 0,9}, gelé dans le code ; taille minimale à écarts nuls : 144 (δ = 0,05, seuil 160), 93 (seuil 20), 74 et 48 pour δ = 0,10 | `pari_apparie.LAMBDAS` ; rapports v1 à v4 | fixé ; **sous (A) à m = 2, les tailles minimales sont celles du seuil 40 : à recalculer (script v5)** |

## Ce que change k = 8 (à vérifier au script v5 avant toute phrase au préenregistrement)

Toutes les puissances publiées (rapports v2 à v4, pièce F) sont à k ≤ 3 comparateurs. Avec 8 gardes et 8 contrastes dans le même
minimum, la fiche est plus sévère (à comparateurs indépendants, 0,9⁸ ≈ 0,43 pour des gardes à 0,9 chacune ; le partage du sujet et la
corrélation entre comparateurs relèvent ce chiffre, non chiffré). **Sous (A) le seuil tombe à 40 (m = 2)**, ce qui compense en partie
(taille minimale à écarts nuls ≈ 110 unités à δ = 0,05 contre 144 au seuil 160 ; à calculer exactement). Le script v5 doit donner, à
k = 8 et seuil 40 puis 320/k\*, la puissance de la fiche aux tailles 160, 300, 400 et 650, K_h ∈ {3, 10}, τ = 0,01, biais 0 et b_h ;
c'est la « simulation du minimum » de la liste de Lazar, avant le fichier réel.

## Ce qui est hors de ce document

δ, b_h et la règle d'arrêt attendent la synthèse du collisionneur (GO-2026-10-29-06, tours partis à 06:32 UTC) et la pièce F ; le
passage sur les vrais écarts attend le pilote (GO-05, tranche 0 d'abord) ; le brouillon 4 du préenregistrement de G1 est à session-depot.
