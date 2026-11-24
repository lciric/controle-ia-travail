# État de l'organisme d'idéation avant le service du dossier groupé et de l'attelage (étape 1) — v1

- Classe C. Session fille du service à l'organisme, 2026-11-24 vers 19:00Z. Inventaire fait par un agent d'exploration Opus en lecture seule ; points clés revérifiés par la fille (marqués « revérifié »).
- Ce que cette note n'est pas : une décision. Les choix sont à la mère et à Lazar.

## 1. Prêt

- **Orchestrateur** : il vit hors du dépôt de travail, dans le dépôt `lciric/ideation-organism`, au commit `a41b7b50` (14 novembre). Le clone se perd à chaque conteneur neuf ; le clone anonyme en lecture est permis (R-4272, R-4827). Copies partielles sur main (`docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/`, paquet v68).
- **Dernière course réelle à vrais proposeurs** : `scripts/lancer_course_auto_conception_v9.py` (`1b47c1cf…`), 19 novembre, code 0, 94 cartes, 72,50 USD sur 150 (R-3800 ; `registres/depenses.md`). Elle a tourné dans un conteneur de session, sans machine louée. Sa sortie est sur `lot/compte-organisme-v1`.
- **Étage des tests de mort** : code `tests_de_mort_v5.py` présent (revérifié, `…/code-organisme-94bfd92/orchestrator/pole/`). Il a tourné une seule fois, à la course v67 du 12 novembre : 14 tests sur des lois promues par le juge, à forme imposée (conception, § 0, revérifié).
- **Choix du modèle expérimentateur** : Sonnet 5.5 pour la seule mesure sur les témoins, Opus 5.5 en repli mesuré ; lecteur témoin Argon ; un expérimentateur de même famille que le proposeur est refusé (GO-2026-11-21-47, GO-2026-11-22-116).
- **Garde de neutralité par motifs** : écrite et éprouvée sur cette branche (`garde_neutralite_question_fusionnee_v1.py`).
- **Reformulation en quatre points** : écrite par Opus (`demande-reformulee-quatre-points-v1.md`, `39e109c1…`). Écart déclaré : ce devait être Fable, gelé jusqu'au 2 décembre (R-5297).

## 2. Manque

1. **Banc d'expérimentateurs et régime général des tests de mort : non branchés.** La conception (`docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-…-v1.md`, `4f3ae86f…`, § 0, revérifié) dit : « Non, ce n'est pas branché en général. » Le régime général n'existe que sur le papier. Rien n'est codé : ni le socle, ni le banc joueur, ni le banc noteur, ni la porte des lots, ni le registre des tentatives, ni la banque de témoins plantés de cet emploi.
2. **La course « seuil et moniteurs »** (tests de mort seuls, GO-2026-11-21-16, ligne de 114,48 USD sous GO-2026-11-21-29) n'est jamais partie. Elle était suspendue à la course « nouvelles attaques », jamais partie elle non plus (R-4801).
3. **L'instrument de l'attelage n'est pas validé.** Note de Fable, § 3.5 et § 4.1 ; amendement de la charte, § 3.5. Les huit épreuves de l'instrument restent à faire, et ses huit nœuds sont tranchés en partie (GO-2026-11-24-38). La conception est prévue du 2 au 4 décembre, le premier chiffre payant au plus tôt du 15 au 19 décembre. Une course maintenant ne peut donc rien revendiquer de « mieux que le hasard » : c'est un atelier d'idées.
4. **Clés.**
   - Le lanceur v9 exige `RR_ANTHROPIC_API_KEY_MINUIT`, qui est sans crédit (R-4833).
   - Il faudra une autre ligne de crédit Anthropic (LUC, déjà partagée avec l'affinage) ou un lanceur adapté.
   - Google : `GEMINI_API_KEY_FREE` est permise pour Carbon et Neon (R-5294).
5. **Lanceurs plus récents jamais joués.**
   - v10 : interrupteurs éteints.
   - v11 : « ne part pas en réel en l'état ».
   - Affinage v11d : préenregistrement non scellé, échéance reportée au 2 décembre (GO-2026-11-24-23).
6. **Défauts connus.**
   - Refus du classifieur (R-4851, R-4762).
   - Coupures de Carbon.
   - Juge Astra illisible sur les témoins.
   - Branche de l'organisme sans ancêtre commun avec main (R-4331).
   - Le lanceur v11 dépend d'environ 736 fichiers de branche (R-4755).
7. **Écart à corriger avant la fusion** : la note d'attelage (§ 3.0) et la priorisation v2 (§ 4) disent que le collisionneur groupé n'a « aucune cellule valide ». C'était vrai avant sa relance de 17:10Z. La note de sortie en compte neuf par bras.

## 3. Machines

- **Aucune machine de l'organisme active.** La dernière, Hetzner 177170935 (palier 0b, essai 3), a été détruite le 23 novembre à 04:50:16Z après l'instantané 459833196 (`registres/arrets.md`, R-5121).
- **Seul serveur Hetzner en marche** (relevé en lecture seule à 18:45Z) : 177425658, l'épreuve plantée des sondes v2, tenu par la mère 016Qh. Non touché.
- **Vast** : quatre instances arrêtées, aucune en marche.

## 4. Ce que la fille propose pour la suite (à trancher par la mère)

- **Voie (a), atelier seul, sans banc neuf.**
  - Servir la question fusionnée neutre à l'organisme (proposeurs et critiques, juge rétrogradé en a priori).
  - Puis passer les propositions à l'étage de tests de mort existant (v5), à forme imposée, comme à la v67.
  - Le banc d'expérimentateurs se réduit à la mesure du modèle expérimentateur sur les témoins existants.
  - Coût modeste, faisable avant le 2 décembre. Elle ne réalise pas le « banc d'expérimentateurs » au sens de la conception.
- **Voie (b), brancher d'abord le banc.**
  - Coder le socle, le banc joueur et le banc noteur, et la banque de témoins plantés, sur processeur, à 0 USD. C'est le « premier pas » de la conception, § 0, point 4.
  - Puis servir.
  - Plusieurs jours de code, contre-lu par un autre modèle (classe B). Des décisions de la conception (§ 6, sept décisions) restent ouvertes pour Lazar.
- **Recommandation de la fille : (a) maintenant, (b) en chantier à part.** Confiance 0,6. Dans (a), deux règles :
  - les constructions déjà réfutées par le collisionneur sont glissées à l'insu des proposeurs comme contrôles cachés, pour éprouver l'étage de tests de mort (proposition de la reformulation, point 1) ;
  - rien d'une lecture ne remonte vers l'organisme (R-5294).
