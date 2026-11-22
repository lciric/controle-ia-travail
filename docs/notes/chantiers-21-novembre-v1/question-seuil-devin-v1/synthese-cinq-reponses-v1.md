# Seuil et budget du devin — synthèse des cinq réponses (v1)

- **Date** : 2026-11-22, vers 13:45 UTC. **Auteur** : session des chantiers du 21 (Opus 5.5), qui orchestre. Pièce de classe C, non contre-lue.
- **Question servie** : `question-seuil-budget-devin-v3.md`, à l'identique pour les cinq. Aux tests de devinette, la v1 était orientée (0,6) et la v2 neutre (0,35) ; la v3 = v2 plus une précision de fait.
- **Dépense** : Fable 0,79 USD ; Argon 0,11 ; Carbon 0,20 ; Neon 0,74 ; Opus en agent, sans dépense. Total 1,84 USD sur 10 (GO-2026-11-22-58).

## Ce que chacun choisit

| Modèle | Choix | Confiance | Si l'on s'en tient aux trois options |
|---|---|---|---|
| Fable 5.2, effort maximal | (d) : seuil corrigé de 0,0125 par test et 8 000 épisodes par test, avec trois amendements | 0,6 | (c), confiance 0,4 : l'erreur coûteuse est la fuite manquée |
| Opus 5.5, effort maximal | (d) : 0,0125 et 8 000 épisodes, plus une confirmation exacte avant toute suspension durable (le seul prédicteur rejetant, figé, sur 4 000 épisodes neufs à 0,05), et des statistiques de queue pour le secret d'audit | 0,65 | (b) si seules les fuites de plus de 0,12 sont dangereuses ; (c) en deçà ; (a) seulement si une suspension ne coûte presque rien |
| Argon | (d) : le maximum de permutation pris sur les quatre tests à la fois, au lieu de Bonferroni | — | (c) ; (b) rejetée nettement (fuite de 0,21 à 5 % d'audit jugée rédhibitoire) |
| Carbon | (d) : contrôle par admission, seuil pondéré, budget inégal selon le test, statistiques studentisées | 0,65 | (b), si toutes les cibles sont équilibrées |
| Neon | (d) : le contrôle par admission de (b) et le budget de (c), une statistique insensible au déséquilibre, une borne haute de confiance à chaque non-rejet | — | — |

## Où ils convergent

1. **Aucun ne garde (a)**, qui est pourtant le défaut actuel de la conception.
2. **Quatre sur cinq contrôlent l'erreur par admission** (Fable, Opus, Carbon, Neon). Argon la contrôle aussi, mais par un maximum commun plutôt que par Bonferroni.
3. **Quatre sur cinq doublent le budget** : 8 000 épisodes par test (Fable, Opus, Neon, et Argon, qui part de (c)).
4. **Deux préviennent que la variation totale mesure mal le danger du secret d'audit** (Opus, Neon). Une fuite concentrée sur quelques épisodes non audités peut suffire à une attaque ; une statistique de queue la retrouve plus tôt.

## Erreurs relevées dans la question

- La fuite de (c) à 5 % d'audit vaut environ 0,14 et non 0,13 (Opus : 0,137).
- Le taux de 18,5 % suppose l'indépendance des tests ; sans elle, la borne est de 20 %. Le test de devinette l'avait déjà dit.
- Si une épreuve réussie après coup lève une suspension, la puissance réelle s'effondre (Opus : 0,64 après une seule reprise).
- Le prédicteur appris est plus faible que le prédicteur optimal (Opus, par simulation : puissance 0,72 contre 0,92), ce qui rend les chiffres de la question optimistes.

## Pour Lazar

- **Ce que ces réponses soutiennent** : une option (d) qui combine le contrôle par admission (0,0125 par test) et le budget doublé (8 000 épisodes par test, 32 000 par admission). C'est la recommandation de Fable et d'Opus.
- **Deux ajouts à trancher** : la confirmation exacte avant toute suspension durable (Opus) ; des statistiques de queue pour le secret d'audit (Opus, Neon).
- **Ce qu'il faudrait pour l'écrire** : un couple de plus dans la conception des devins, écrit par Fable, et sa contre-lecture.
- **En attendant**, le défaut reste (a).

## Pièces

- Fable : `reponses/fable/relecture-fable-api.md` (`89cd8962…`).
- Argon, Carbon et Neon : `reponses/argon/`, `reponses/carbon/`, `reponses/neon/` (fichiers `.md` et `.json` scellés).
- Opus : `reponses/opus-max/reponse-opus-max-v1.md` (`2ec7e556…`). Ses scripts de calcul et ses brouillons sont versés depuis le bloc-notes sous `reponses/opus-max/calculs/`, scellés.
