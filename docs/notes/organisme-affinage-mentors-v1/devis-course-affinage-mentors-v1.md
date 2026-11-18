# Devis de la course d'affinage des idées des mentors par l'organisme d'idéation — v1 (non engagé)

- Écrit le 2026-11-18T06:22:27Z (`date -u`) par la session du compte organisme (modèle I), avec le texte de décision `docs/decisions/decision-matiere-premiere-mentors-v1.md`. **Aucune dépense engagée** ; lancement sur ligne de GO et mot de Lazar, depuis une session où la garde de calcul est chargée (pas celle-ci).

## 1. Base de coût mesurée (pièces au dépôt)
- Course réelle v67 (dépôt public `lciric/ideation-organism`, `resultats/course-v67/poste-local-v1/boucle-reelle-v66.json`, `21bc75f4…`) : 23 cartes sur deux générations, deux proposeurs (Argon, Kimi), tests de mort compris : **1,99431 USD** au total (proposeurs 1,10442 ; tests de mort 0,88989), 2 739 s ; soit environ **0,048 USD par carte de proposeur** sans Claude.
- Courses des mentors du 3 novembre, à cinq espèces avec Claude (montants relevés par `mentors-releve-d-ensemble-v1.md` § 3.4, non revérifiés ici) : 1,57 à 12,90 USD par course (Ibrahim seconde course 10,64 ; Scheurer 1,57 et 5,24 ; Colognese-Ward 2,73 et 12,90 ; Jang-Feng 8,74), pour quelques dizaines de fiches chacune.

## 2. Forme proposée de la course (à fixer par le préenregistrement)
- Matière servie : les seize fils communs (relevé § 2), chacun avec les idées qu'il regroupe, entrées sous réserve et exclusions retirées.
- Proposeurs : cinq espèces si les relais le permettent (Claude d'abord, GO-2026-11-18-13), deux cartes affinées par fil et par espèce : **16 × 5 × 2 = 160 cartes**.
- Aiguilleur sur chaque carte ; deux juges croisés par carte avec passeport ; mémoire anti-répétition ; **pas de tests de mort** dans cette course (épreuve avec dépense plus tard, point 3 de la décision).

## 3. Devis
| poste | appels | coût unitaire retenu | estimation (USD) | pire cas (USD) |
|---|---|---|---|---|
| proposeurs | 160 | 0,05 (mesuré sans Claude) à 0,40 (pire appel de proposeur relevé dans la v67, 0,400484) | 16 à 40 | 64,08 |
| aiguilleur | 160 | prix à relever (appel court) | 4 à 8 | 32 (à 0,20) |
| juges croisés | 2 par carte avec passeport, au plus 320 | prix à relever | 8 à 32 | 64 (à 0,20) |
| reprises | +10 % | | 3 à 8 | 16 |
| **total** | au plus 800 | | **31 à 88** | **176** |

Le pire cas suppose tous les appels au prix le plus haut observé pour leur rôle, ou à 0,20 USD quand le prix n'est pas relevé. Le prix réel d'un appel Claude par relais est **à relever** avant le préenregistrement ; le devis sera refait sur ces prix.

## 4. Règle des clés (GO-2026-11-18-13)
Avant la course : relevé de ce qui reste sur chaque clé employée (par l'interface de facturation ou le compteur), sans valeur de clé ; si le reste est sous un cinquième du crédit ou sous le pire cas ci-dessus (176 USD), alerte à la mère avant le lancement. Après la course : coût réel par relais, relevé de chaque clé, écart au devis.
