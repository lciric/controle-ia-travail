# Devis — lecture des fiches de la course « conception propre » par Astra (`gpt-6-astra`), outil v3.1 — v2

Auteur de l'outil (modèle A), sous-agent de la session mère ; 14 novembre 2026, vers 09:25 UTC (`date -u`). Remplace,
pour la lecture, `lecture-classement-v3/devis-lecture-astra-v1.md` (`6f8f97c0…`, gardé, R12), qui chiffrait en formule
faute de prix lu. Ligne : GO-2026-11-13-06 (plafond 21 USD). **Aucun appel fait.**

## Verdict

Au **prix lu** (`prix-astra-v2.md`, `bf211a07…`, page officielle relevée le 14 novembre à 08:45:38Z) :

| Palier, effort | 18 appels, attendu | Plafond nécessaire pour que les 18 appels passent | Tient dans le reste de la ligne (14,21) ? |
|---|---|---|---|
| Standard, `medium` | **17,28 USD** | **18,57 USD** | **non** |
| Standard, `low` | 8,68 USD | 10,37 USD | oui |
| **Flex, `medium`** | **8,64 USD** | **9,28 USD** | **oui** |
| Flex, `low` | 4,34 USD | 5,18 USD | oui |

Aucune de ces lectures ne tient dans le reste de la réserve du lecteur (2,74 USD) : **la part de la ligne accordée au
lecteur est un nœud de Lazar**. Recommandation : **Flex, effort `medium`, plafond 14,20 USD** (§ 5).

## 1. Prix (USD par million de jetons ; contexte ≤ 272 000 jetons d'entrée, où tombent tous nos corps)

| Palier | Entrée | Entrée en cache | Sortie |
|---|---|---|---|
| Standard | 10,00 | 1,00 | 50,00 |
| Flex | 5,00 | 0,50 | 25,00 |

Source : `prix-astra-v2.md` (lignes « Standard » et « Flex / Batch » de son tableau), copie de la page
`docs/sources/tarifs-openai-v1/developers-openai-com-api-docs-pricing-2026-11-14.html` (`099c9496…`). L'outil v3.1 porte
ces six nombres en constantes, revérifie à chaque préparation l'empreinte de `prix-astra-v2.md` et la présence de la
ligne de son palier, et les recopie au manifeste avec la source et la date (condition C2) ; aucune option de prix.

## 2. Volumes (inchangés depuis le devis v1 ; 43 fiches, lots de 5, 18 appels)

| | Lot de 5 | Lot de 4 |
|---|---|---|
| Octets du corps (estimés ; Flex : 24 octets de plus, `service_tier`) | ≈ 49 900 | ≈ 45 850 |
| Jetons d'entrée attendus (3,32 octets par jeton) / pire cas (un par octet, + 1 024) | ≈ 15 000 / ≈ 50 900 | ≈ 13 800 / ≈ 46 900 |
| Jetons de sortie attendus, `low` / `medium` (SUPPOSÉ) ; pire cas | 7 000 / 17 000 ; 32 768 | 5 600 / 13 600 ; 32 768 |

Deux lectures, 18 appels : ≈ 265 700 jetons d'entrée attendus (≈ 900 600 au pire) ; sortie ≈ 120 400 (`low`),
≈ 292 400 (`medium`), 589 824 au pire. Méthode et hypothèses : devis v1, § 4 (octets tirés des tailles des envois scellés
de la v1, sans ouvrir leur contenu ; 3,32 octets par jeton mesurés sur Kimi ; raisonnement par fiche supposé).

## 3. Coût

| | Standard | Flex |
|---|---|---|
| Un appel (lot de 5), attendu `medium` / `low` | 1,00 / 0,50 | 0,50 / 0,25 |
| Un appel (lot de 5), **pire cas** | **2,15** | **1,07** |
| 18 appels, attendu `medium` | 17,28 | 8,64 |
| 18 appels, attendu `low` | 8,68 | 4,34 |
| 18 appels, pire cas (jamais atteint : la garde arrête avant le plafond) | 38,50 | 19,25 |
| Économie possible si le préambule (≈ 8 900 jetons) est servi en cache pour 17 appels — non comptée | ≈ 1,36 | ≈ 0,68 |

## 4. Condition des 18 appels (corrigée, m2 de la contre-lecture)

La garde laisse partir le dernier appel si la dépense des 17 premiers plus le pire cas du 18e ne dépassent pas le
plafond. Le 18e appel, dans l'ordre du manifeste (L1 lots 1 à 9, puis L2 lots 1 à 9), est **un lot de 4**. Avec les
hypothèses du § 2 :

- 17 premiers, attendu : 251 900 jetons d'entrée et, en `medium`, 278 800 de sortie (292 400 − 13 600) ;
- 18e, pire cas : (45 850 + 1 024) jetons d'entrée et 32 768 de sortie ;
- **`medium` : 0,2988 PE + 0,3116 PS ≤ plafond** ; **`low` : 0,2988 PE + 0,1476 PS ≤ plafond**.

Vérification de la formule du contre-lecteur (0,2978 PE + 0,3116 PS) : le coefficient de PS est le même ; celui de PE
diffère de 0,0010 parce que sa formule omet la marge de 1 024 octets que la garde ajoute au pire cas d'entrée (je
retrouve 0,2978 sans cette marge). L'écart vaut 0,01 USD au prix standard. Au prix lu : standard 18,57 (`medium`),
10,37 (`low`) ; Flex 9,28 (`medium`), 5,18 (`low`). La v1 et `prix-astra-v2.md` écrivaient 18,46 et 9,23 (formule
0,3019 PE + 0,3089 PS, qui supposait un 18e lot de 5) : **à remplacer par les valeurs ci-dessus**.

## 5. Comparaison avec la ligne et recommandation

- Reste de la ligne GO-2026-11-13-06 : **14,208913 USD** (21 − 6,791087, `registres/depenses.md`) ; l'outil refuse tout
  plafond au-delà de 14,20 moins la dépense antérieure déclarée (`--depense-anterieure-usd`, 0 à ce jour : aucun appel à
  Astra depuis le devis v1).
- Reste de la réserve du lecteur (devis de la course) : **2,743658 USD** ; toute lecture complète la dépasse (nœud).
- **Recommandation (confiance 0,65)** : palier **Flex**, effort **`medium`**, **plafond 14,20** (un plafond plus haut
  que la condition ne coûte rien de plus en attendu ; il évite d'arrêter en route une lecture dont la sortie dépasserait
  les hypothèses, ce qui serait payé sans rien produire, E2). Premier appel seul (`--envois-max 1`, C3) : 0,50 USD
  attendus, 1,07 au pire ; puis recalcul de ce devis sur ses jetons réels avant les 17 autres.
- Risque propre à Flex : la page des prix ne dit pas la disponibilité ; un refus faute de ressources (statut autre que
  200) arrête la lecture (règle « arrêt au premier écart », compté au pire cas, sans relecture) ; une reprise serait un
  nœud. Le palier servi est vérifié à chaque réponse (`service_tier` égal à `flex`, sinon arrêt).
- Option de repli, si Lazar préfère le standard : effort `low`, plafond 14,20 (condition 10,37) ; le raisonnement réduit
  peut affaiblir la lecture de R7 (mécanisme), seul critère qui approche le fond.
- Défaut sous 48 heures : aucun appel (dépense : nœud, jamais de défaut qui dépense).
