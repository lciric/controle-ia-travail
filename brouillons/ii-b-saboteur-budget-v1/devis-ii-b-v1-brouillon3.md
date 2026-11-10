# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 3

- **Statut** : **brouillon 3** = brouillon 2 (`devis-ii-b-v1-brouillon2.md`, `959df451…`, intact, R12) recalculé par le développeur du code (sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), le 2026-11-10 vers 11:15 UTC (heure relevée par `date -u`), d'après le code `src/controle_ia/iib/` (branche `prep/ii-b-code-v1`) et **GO-2026-11-10-08** (R-2175 : « avec l'activité interne enregistrée » ; plafond **60 USD**, coupure **55 USD**, A100 seule, échéance 2026-11-27). Non contre-lu, non scellé. **Aucune dépense n'est engagée par ce document.**
- **Arithmétique** : `calcul-devis-ii-b-v2.py` (reprend `calcul-devis-ii-b-v1.py` tel quel pour les débits de 7a et les prix), sortie brute `sortie-calcul-devis-ii-b-v2.txt`. Chaque nombre ci-dessous en vient.
- **M7 tranché** : **variante B** (ligne 60 USD, coupure de la configuration 55 USD, A100 SXM4 80 Go seule, fenêtre vide = nœud). C'est aussi la variante que porte GO-2026-11-10-08.

## 1. Ce qui change par rapport au brouillon 2

| ligne | brouillon 2 | brouillon 3 | raison |
|---|---|---|---|
| juge de T0.8 en une passe | 0,21 h (option) | **0 h** | le code v1 refuse `juge_t08.joue` (forme de T0.8 non scellée) |
| activité interne (ajout R-2175) | — | **0,06 à 0,14 h** de carte ; **15,7 Go** attendus (250 jetons par action), **25,2 Go** au pire (400) | une passe avant par épisode d'évaluation (256 × 0,5 s, non mesuré) ; écriture de 2 560 actions × jetons × 4 096 × 2 octets × 3 couches à 200 Mo/s (prudent, non mesuré) |
| sortie des activations | — | **≤ 0,8 à 1,3 USD** | volume ci-dessus au prix de téléchargement (≤ 0,05 USD/Go) faute d'un prix de sortie relevé : **hypothèse** |
| jumeau | 0,5 à 1,5 s, 3,0 s pire | inchangé | le code joue la forme « cache dupliqué » (un préremplissage, 8 suites de 16 jetons au plus) et ne bascule vers « prérempli par suite » que si l'épreuve de forme échoue (consigné) ; débit **non mesuré** |
| témoin-jumeau | compris | compris | distillation 0,31 à 0,40 h pour les deux adaptateurs ; évaluation TJ100 comprise dans les 256 épisodes |

## 2. Heures de carte par étape (A100, hôte nominal), ligne par ligne

| étape | bas (6 tours, jumeau 0,5 s) | **central** (10 tours, 1,0 s) | haut (12 tours, 1,5 s, 127 acceptés, 400 jetons) | P1 (hôte ×2, 12 tours, 3,0 s, 127, 400 jetons) |
|---|---|---|---|---|
| fixe (amorce, suite ciblée, création, écriture) | 1,00 | **1,00** | 1,00 | 2,00 |
| étalonnage : épisodes (96) | 1,15 | **1,15** | 1,15 | 2,31 |
| étalonnage : jumeau (960 actions) | 0,13 | **0,27** | 0,40 | 1,60 |
| maître : épisodes | 2,31 | **3,85** | 4,62 | 9,24 |
| filtrage : jumeau du maître et ancrage | 0,31 | **0,98** | 1,73 | 6,93 |
| distillation : élève et témoin-jumeau, identité | 0,31 | **0,31** | 0,40 | 0,81 |
| évaluation : épisodes (256) | 3,08 | **3,08** | 3,08 | 6,16 |
| évaluation : jumeau (2 560 actions) | 0,36 | **0,71** | 1,07 | 4,27 |
| activité interne : passes et écriture | 0,06 | **0,06** | 0,07 | 0,14 |
| **total** | **8,71** | **11,40** | **13,53** | **33,45** |

## 3. USD, ligne par ligne

| scénario | carte | stockage arrêté | téléchargement (modèle, image) | sortie des activations | **total** | sous 55 ? |
|---|---|---|---|---|---|---|
| bas, 1,12 USD/h | 9,8 | ≤ 1,9 (24 h) | ≤ 1,0 (20 Go) | ≤ 0,8 | **13,5** | oui |
| **central, 1,12 USD/h** | 12,8 | ≤ 1,9 | ≤ 1,0 | ≤ 0,8 | **16,5** | oui |
| central, 1,30 USD/h | 14,8 | ≤ 1,9 | ≤ 1,0 | ≤ 0,8 | 18,5 | oui |
| haut, 1,30 USD/h | 17,6 | ≤ 1,9 | ≤ 1,0 | ≤ 1,3 | **21,8** | oui |
| arrêt précoce M-1 (tour 4), 1,12 à 1,30 | 4,9 à 5,7 | ≤ 1,9 | ≤ 1,0 | 0 | **7,9 à 8,6** | oui |
| **P1, 1,30 USD/h** | 43,5 | ≤ 3,8 (48 h) | ≤ 2,0 (40 Go) | ≤ 1,3 | **50,6** | oui (marge 4,4) |
| P1, 1,40 USD/h | 46,8 | ≤ 3,8 | ≤ 2,0 | ≤ 1,3 | **53,9** | oui (marge 1,1) |

Prix horaire maximal de la carte pour que P1 tienne sous la coupure de 55 USD : **1,432 USD/h** (la borne de l'offre est 1,30).

## 4. M7 : variante B recommandée (confiance ≈ 0,8)

- **B couvre tout ce qui peut arriver sur A100** : l'attendu (13,5 à 21,8 USD) et le pire cas P1 jusqu'à 1,43 USD/h (borne de l'offre : 1,30). La coupure de 55 n'est atteinte que par un scénario que l'offre interdit déjà.
- **A n'achète qu'un repli qui ne tient pas** : sur H200 NVL à 4,70 USD/h, le haut de l'attendu coûte ≈ 70,7 USD et la configuration de 75 ne laisse que **0,92 h** de marge au-delà de 13,53 h (débits du jumeau et de la H200 non mesurés) : le moindre ralentissement fait détruire l'instance par la minuterie avant l'évaluation, pour ≈ 75 USD et des résultats partiels.
- **Coût de B** : une fenêtre A100 vide (12 recherches à 15 minutes, 0 USD) devient un nœud de Lazar au lieu d'un repli automatique ; avec une création visée entre le 14 et le 17 novembre et une échéance au 27, ce nœud coûte au plus une demi-journée, sans dépense.
- GO-2026-11-10-08 porte déjà B (60 USD, coupure 55) : `<<PLAFOND_LIGNE_IIB>>` = 60, `<<PLAFOND_CONFIG_IIB>>` = 55, `<<REPLI_H200_PERMIS>>` = non.

## 5. Hors devis, déclarés

- **Destination des activations** (15,7 à 25,2 Go) : le dépôt git ne peut pas les recevoir (fichiers ≤ 100 Mo, dépôt de plusieurs gigaoctets) ; le code les écrit en morceaux scellés de 90 Mo au plus sur le disque de l'instance ; **où les rapatrier est un point ouvert pour la mère** (nœud si un stockage payant ou un compte est nécessaire). À défaut, l'option sans dépense nouvelle est de ne garder que les conditions H, B100 et TJ100 (−25 %) ou une seule couche (−67 %), ce qui change la configuration (nom neuf).
- Contre-lecture, code, essais, répétition jouet, lectures (1) et (2) : processeur, 0 USD.
- Toute lecture de sonde ultérieure : préenregistrement scellé à part, verdict scellé de P3-bis, GO et devis à part.
- Témoin distillé honnête (adaptateur distillé sur des épisodes honnêtes) : non compris (voir le rapport du développeur, question (a)) ; s'il est ajouté : ≈ 1,0 h de carte, ≈ 1,2 à 1,4 USD (64 transcriptions, une condition d'évaluation de 64 épisodes et son jumeau), toujours sous la coupure en attendu.
