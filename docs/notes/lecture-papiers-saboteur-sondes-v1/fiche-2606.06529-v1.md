# Fiche de lecture — 2606.06529 — v1

- **Titre** : Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (atelier AIWILD, conférence ICML 2026).
- **Auteurs** : Catherine Ge-Wang, Tyler Crosse, Benjamin Hadad IV, Joachim Schaeffer, Ram Potham, Tyler Tracy. **Identifiant** : arXiv 2606.06529 v1.
- **PDF** : `docs/sources/pdf/anteriorite-P-041-v2/c1/2606.06529.pdf`, sha256 `6042d449d1ae11c7441e8f653675883b352ddafd8389af4a876d77919d6f7f4e` (vérifiée par `sha256sum`, 19 pages ; deux copies identiques sous `c5/` et `mecanisme-adjudant-v1/`).
- **Décision lue** : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v1.md`, ligne 65 ; puis la v3 (l. 74 et 217) et ses errata 1 à 3, le 3 v2 primant (point 11 : q mesuré par strates).
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:54Z (`date -u`).

---

## (a) Ce que le papier établit

L'attaquant décide quand attaquer (politique de départ) et quand abandonner (politique d'arrêt), sans gagner en capacité (p. 1). L'audit relit **les trajectoires les plus suspectes** selon un moniteur de confiance (1 % du budget, p. 1). Au budget de 1 %, le résumé annonce −20 points de sûreté au départ et −20 à −28 points à l'arrêt (p. 1). Mais **un seul** de ces résultats a un intervalle de confiance qui exclut zéro : l'arrêt sur LinuxArena, de 0,36 à 0,09, soit −28 points, intervalle [−37, −8], 23 trajectoires (p. 5). Les deux baisses au départ à 1 % ont des intervalles qui franchissent zéro de 3 points au plus (p. 5). Seuils réglés de façon adverse, arrêt appliqué après coup (p. 5, 7) : C'est une « heuristic upper bound » (p. 11), conditionnelle à une tentative, non la sûreté en service (p. 3, 7).

## (b) Ce que la décision voulait, et si le papier le permet

La v3 (l. 74) : « un attaquant qui choisit quand attaquer abaisse la sûreté mesurée ». Cela touche le plancher par deux voies : si le tirage se devine, et si l'oracle reconnaît inégalement le dommage selon la tâche. **Le permet en partie.** Le papier ne teste qu'un audit qui suit la suspicion, jamais un tirage secret au hasard. Les deux voies sont des transpositions, non des résultats. La seconde, choisir les tâches où q est bas, est l'analogue de sa politique de départ. L'erratum 3 v2 (point 11, strates) en tient compte. La phrase « abaisse la sûreté » doit porter sa réserve : une seule baisse est significative.

## (c) Usage pour l'entretien et le billet

Pour l'objection 8 de la note v6, il complète Schaeffer et al. : en cadre agentique, la sélection paie contre un audit des plus suspects. Cela motive le tirage au hasard, sans prouver qu'il résiste. Il fournit une **épreuve** : les politiques de départ et d'arrêt, avec leur témoin au hasard à taux égal (p. 14), comme bras d'attaque informé contre une sonde. Il crée une antériorité : la sélection d'attaque en cadre agentique est occupée.

## (d) Plus petite action

À la v4 de N-075, ajouter « sous audit des plus suspects ; une baisse significative sur quatre à 1 % (p. 5) ». Coût : dix minutes, aucune dépense. L'épreuve sur notre banc demande un devis et un GO.
