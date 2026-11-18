# Devis de la course d'affinage des idées des mentors par l'organisme d'idéation — v2 (non engagé)

- Écrit le 2026-11-18T06:26:41Z (`date -u`) par la session du compte organisme (modèle I). **Version 2** (R12 ; la v1, `54dc947d…`, reste en place) : porte la contre-lecture `docs/decisions/contre-lecture-decision-matiere-premiere-mentors-v1.md` (`bdd8045a…`, commit `7ef7dddf`, section du devis, constats D1 à D5). **Aucune dépense engagée** ; aucun GO ne se demande sur la v1. Lancement sur ligne de GO et mot de Lazar, depuis une session où la garde de calcul est chargée (pas celle-ci).

## 1. Base de coût mesurée (pièces au dépôt), unités séparées (D1)
- Course réelle v67 (dépôt public `lciric/ideation-organism`, `resultats/course-v67/poste-local-v1/boucle-reelle-v66.json`, `21bc75f4…`), deux proposeurs sans Claude (Argon, Kimi) : 1,99431 USD au total (proposeurs 1,10442 ; tests de mort 0,88989), 2 739 s.
  - **Appels de proposeur** : 4 appels (`appels_proposeurs`) pour 23 cartes, soit environ six cartes par appel ; coût moyen **0,276 USD par appel** (1,10442 / 4), le plus cher **0,400484 USD**.
  - **Appels courts** (`appels_etage`, 42 appels) : lecteur Argon 0,0347 USD par appel (14 appels), expérimentateur Kimi 0,0144 (28 appels) ; le plus cher 0,04326.
- Courses des mentors du 3 novembre : montants relevés par `mentors-releve-d-ensemble-v1.md` § 3.4 (1,57 à 12,90 USD par course, non revérifiés). Correction de la v1 (D4) : d'après ce relevé, une seule de ces courses est complète à cinq espèces et trois premières courses n'ont rendu aucune fiche lisible ; ces montants ne servent donc que d'ordre de grandeur, sans entrer dans la table.

## 2. Forme proposée (à fixer par le préenregistrement)
- Matière : les seize fils communs du relevé ; **entrées sous réserve et entrées soumises aux réserves de cloisonnement non servies tant que la mère n'a pas levé leur réserve** ; exclusions des relevés jamais servies (D5).
- Proposeurs : cinq espèces si les relais le permettent (Claude d'abord, GO-2026-11-18-13) ; **un appel par fil et par espèce, rendant deux cartes affinées** : 16 × 5 = 80 appels, 160 cartes.
- Aiguilleur : un appel court par carte (160). Juges croisés : deux appels courts par carte avec passeport (au plus 320). Pas de tests de mort.
- **Préalable** (D5) : l'inscription par la mère des montants absents du registre des dépenses (relevé § 3.4, environ 41,82 USD) avant toute dépense de l'organisme sur cette matière (texte de décision, section 2).

## 3. Devis (hypothèses déclarées, D2)
| poste | appels | estimation : prix retenu et source | estimation (USD) | borne haute : prix retenu | borne haute (USD) |
|---|---|---|---|---|---|
| proposeurs | 80 | 0,276 (moyenne v67, sans Claude) | 22,08 | 0,400484 (pire v67, sans Claude) | 32,04 |
| aiguilleur | 160 | 0,0347 (appel court v67) | 5,55 | 0,20 (convention, prix non relevé) | 32,00 |
| juges croisés | 320 | 0,0347 (appel court v67) | 11,10 | 0,20 (convention) | 64,00 |
| reprises | +10 % | | 3,87 | | 12,80 |
| **total** | 560 au plus | | **42,60** | | **140,84** |

**Limite (D3)** : la borne haute n'est **pas** un plafond. Les prix des proposeurs viennent d'une course sans la famille prioritaire (Claude), et 0,20 est une convention. Le prix d'un appel Claude par relais est **à relever** avant le préenregistrement, et le devis sera refait sur ces prix.

## 4. Plafond d'arrêt et règle des clés (D3 ; GO-2026-11-18-13)
- Le préenregistrement de la course portera un **plafond qui arrête la course**. Proposition à trancher par Lazar : 150 USD, ou le devis refait sur prix Claude relevés, majoré de 25 %, si ce montant est plus élevé.
- Avant la course : relevé de ce qui reste sur chaque clé employée (interface de facturation ou compteur), sans valeur de clé. Si le reste est sous un cinquième du crédit ou sous le plafond d'arrêt, alerte à la mère avant le lancement ; Lazar est prévenu avant qu'une clé n'atteigne zéro. Après la course : coût réel par relais, relevé de chaque clé, écart au devis.
