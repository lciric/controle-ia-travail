# Course 1, tentative 2 — lecture complémentaire : doublons fusionnés, modèle servi d'Argon — v1

Lignée session-depot (instance 2), 30 octobre 2026, 10:45 UTC (`date -u`). Demandes de Lazar : « il faut empêcher les duplicatas » ; « corrige et vérifie ». **Aucun appel payant** : lecture mécanique des sorties scellées de `sortie-juges-course-v2/` (`classement.json`, `doublons-par-juge.json`, `noyau/cles-anonymisation-par-juge.json`, `lecture.json`) et des journaux des relais Gemini.

## 1. Doublons

**Règle, fixée avant le calcul** : deux fiches forment un doublon si **les deux juges** les ont signalées comme jumelles, chacun sans connaître l'auteur (identifiants anonymisés propres à chaque juge). Les groupes sont fermés par transitivité. Chaque groupe garde la fiche la mieux classée ; les autres sont listées comme « doublon de ». Les notes ne changent pas.

**Résultat** : 12 paires signalées par les deux juges, toutes entre la passe 1 et la passe 2 du même proposeur. Une paire signalée par un seul juge (Opus : argon-p2-02 et fable-p2-03) n'est pas fusionnée. **29 fiches, 17 idées distinctes**. Les deux témoins jumeaux plantés (temoin-p0-03 et p0-04) ont été signalés par les deux juges : l'instrument de détection des doublons marche.

| Rang dédoublonné | Fiche gardée | Total | Éligible | Doublon(s) |
|---|---|---|---|---|
| 1 | fable-p1-01 (rang 1) — Q3 sur grille publiée : prédire les cellules où notre propre sonde échoue | 12.5 | oui | fable-p2-01 (rang 3) |
| 2 | argon-p2-08 (rang 2) — Approche A3 — Test par mutation chirurgicale des moniteurs (témoins plantés côté défense) | 12.5 | oui | — |
| 3 | fable-p1-07 (rang 4) — Approche : la carte de contrôle du pôle — les témoins plantés comme processus surveillé | 12.0 | oui | fable-p2-07 (rang 8) |
| 4 | argon-p1-07 (rang 5) — Approche A2 — Opérateur de dilution et de greffe contrefactuelle sans attaquant (emprunt à | 12.0 | oui | argon-p2-07 (rang 6) |
| 5 | argon-p2-05 (rang 7) — Nouvelle Q-N3 — Péché antigénique originel et hystérésis d'ordre dans l'héritage de la bou | 12.0 | oui | — |
| 6 | argon-p2-03 (rang 9) — Q3 + Q-pont fusionnées — Prédiction préenregistrée des angles morts par cellule (moniteur  | 12.0 | oui | argon-p1-03 (rang 14) |
| 7 | fable-p2-06 (rang 10) — Q6 sur bancs d'agents : la part de provenance dans le rappel, mutant aveugle au contenu, p | 12.0 | oui | fable-p1-06 (rang 24) |
| 8 | argon-p2-04 (rang 11) — Nouvelle Q-N2 — Masse cachée d'évasion et plafond de couverture par capture-recapture inte | 12.0 | oui | — |
| 9 | argon-p1-02 (rang 12) — Nouvelle Q-N1 — Dégradation en ligne des bancs co-évolutifs (loi de Goodhart du juge) | 11.5 | oui | argon-p2-02 (rang 13) |
| 10 | argon-p1-01 (rang 15) — Q4 — Le diffus comme axe d'universalité séparé sous borne d'horizon | 11.5 | oui | argon-p2-01 (rang 16) |
| 11 | fable-p1-04 (rang 17) — Q4 par l'axe structurel publié : dilution à dommage constant, même score, deux règles | 11.5 | oui | fable-p2-04 (rang 18) |
| 12 | fable-p2-03 (rang 19) — Q2 : résultat ou hygiène ? Rejugement des courbes publiées sous juge figé à borne | 11.5 | oui | — |
| 13 | fable-p2-02 (rang 20) — La diagonale de l'auto-jeu : le score contre l'attaquant co-évolué prédit-il la généralisa | 11.0 | oui | fable-p1-02 (rang 22) |
| 14 | fable-p2-08 (rang 21) — Approche : le prédicteur en quarantaine — date de coupure antérieure et annexes non lues c | 11.0 | oui | fable-p1-08 (rang 23) |
| 15 | fable-p2-05 (rang 25) — Q-pont à coût nul : fabriqué (SLEIGHT-Bench) contre exécuté (MonitoringBench), par catégor | 10 | oui | fable-p1-05 (rang 26) |
| 16 | argon-p1-08 (rang 27) — Approche A3 — Détournement de l'organisme en auditeur adversarial des courbes publiées (mé | 10.0 | oui | — |
| 17 | argon-p2-06 (rang 28) — Approche A1 — Juge à support de désaccord et portefeuille de vigilance (fusion Discern + P | 11.0 | non | argon-p1-06 (rang 29) |

**Cause** : la passe 2 reçoit la même question que la passe 1, sans la liste des fiches déjà écrites ; elle refait donc souvent la même idée. **Correction pour la course 2** (orchestrateur tenu par conv-audit, v53) : (i) la passe 2 reçoit les noms et énoncés des fiches de la passe 1, de tous les proposeurs, et la consigne de n'en redire aucune ; (ii) le classement fusionne mécaniquement les paires signalées par les deux juges, selon la règle ci-dessus, et rapporte le nombre d'idées distinctes.

## 2. Modèle servi d'Argon

`lecture.json` porte `servi_lu: false` pour Argon : l'orchestrateur ne lit pas le modèle servi (CL13-05). Le relais Gemini, lui, le journalise à partir du champ `modelVersion` de la réponse amont (`docs/notes/ideation-organisme-v1/lancement-v2/relais_gemini_v1.py`, l. 145-146). Lecture des journaux :
- `relais-gemini-journal-v2.jsonl` (proposeur et contrôles) : 3 appels `generateContent`, statut 200, **servi `gemini-4-argon`** pour les 3 ;
- `relais-gemini-juges-journal-v1.jsonl` (juge) : 2 appels `generateContent` (essai de 48 jetons, puis jugement), statut 200, **servi `gemini-4-argon`** pour les 2.

**Réserve levée** : 5 appels sur 5, modèle servi égal au modèle demandé.

## 3. Témoins plus courts que les fiches

Les 6 témoins servis font de 1 203 à 4 333 caractères ; les fiches, de 4 795 à 7 975 (médiane 5 762) ; les 6 sont hors fourchette (`lecture.json`). Un juge pourrait les reconnaître à leur longueur. Correction proposée : témoins v2 de longueur tirée dans la fourchette des fiches, mêmes défauts plantés, écrits par un tiers qui ne voit pas les fiches ; puis rejugement des 29 fiches et des témoins v2 par Opus 5.5 et Argon (mode « juges seulement », mêmes consignes). **Dépense : attend le mot de Lazar.**

## 4. Autres signaux lus au passage

- Auto-préférence d'Argon : total moyen 13,14 sur ses propres fiches contre 11,93 sur celles de Fable ; Opus n'avait aucune fiche à lui, la grandeur n'est donc pas séparable d'une différence de qualité.
- Corrélation entre longueur et total : 0,22.
