# Rapport de sous-agent (texte de modèle, non opposable)

## Contre-lecture R2 n° 1 d'A1-v3 (brouillon 3) — remise

**Verdict en trois lignes**
1. **Scellable après les 42 couples, à une condition** : le bloquant B1 n'est levé par les couples que si son prix déclaré est accepté par écrit. Je propose ce choix par défaut (nœud ci-dessous). Sinon, il faut une version 3.1 du code et un brouillon 4.
2. **B1 — à 400 USD, c'est la garde du registre des commandes qui mord, pas le compteur.** Elle refuse un appel quand réglé + engagé + pire cas du nouvel appel dépasserait 400 USD, donc dès ≈ 398,4 USD réglés, avant que le compteur de l'orchestrateur n'atteigne 400. Le mécanisme est établi par l'addendum d'A1 (§1.1) et confirmé par les n° 287 (l. 313) et 290. Une panne de l'interface Gemini sort en code 3 au pire cas (≈ 1,6 USD par appel), sans attente : de ≈ 103 à 123 tentatives perdues suffisent, soit quelques minutes à quelques dizaines de minutes de panne. Ensuite, toutes les tentatives restantes sont refusées en code 4, en quelques millisecondes. La course finit en code 0 avec des cases vidées et une issue 6, et la section 8 n'ouvre pas de seconde course dans ce cas. C'est le défaut (1) d'A1, cette fois au plafond, contraire à la décision (ii). Le texte annonce au contraire un arrêt propre au plafond (code 3).
3. **Le reste tient** : plan gelé, GO, 73 empreintes, lanceur, ordre 2, 6, 1, 3, 4, 5, issue 6, A9, attente. Les importants I1 à I7 et les mineurs M1 à M9 sont couverts par les couples ; M10 est une question pour toi.

**Fichiers produits (neufs, non committés, sans `.sha256`)**
- `/home/claude/ideation-organism/orchestrator/prereg/contre-lecture-preenregistrement-attaque-goodhart-v3-v1.md` — sha256 `01a2041a197122525b5dce642a5a20fb8ced9f9538c1120d8d605d8c4a35705a`
- `/home/claude/ideation-organism/orchestrator/prereg/couples-contre-lecture-attaque-goodhart-v3-v1.json` — sha256 `e5f669e440a93eaf8918bacf7361db8e8f8a43263b745e90f6d80167f3a61480`
  - Liste d'objets `{"ancien", "nouveau"}`, dans l'ordre du document. Chaque « ancien » est présent une seule fois dans le brouillon 3, sans recouvrement.
  - Appliqués à la suite, ils donnent `5507536934dfb733…`. Ce texte, renommé `…-v3-v1.md` avec un compagnon factice hors du dépôt, est accepté par `lire_preenregistrement` : 73 empreintes, plan identique hors `decision_ecart`, aucun marqueur, seul GO nommé GO-2026-11-02-21.

**Importants**
- **I1 — le code 5 compte comme non répondus des comportements du proposeur.** D'après le n° 287, il couvre aussi le refus du modèle et la réponse vide ou tronquée. Avec cette commande, le cas « ok au texte vide » n'arrive jamais. Un refus systématique du proposeur pourrait donc se lire « bras perdu » (infrastructure).
- **I2 — tentatives perdues dans les suites jouées.** Elles réduisent la pression sur la suite, ce qui rend « résiste » et « sans dents » plus faciles. Aucune règle de lecture ne le traite ; le couple ajoute une qualification « sous pression réduite ».
- **I3 — le délai de l'orchestrateur est de 1 800 s, pas 1 750 s.** Voir `pole/adaptateurs.py:622` et `demonstrations/ideation_v8.py:74` ; l'audit A §1.4 le confirme. 1 750 s est le délai propre de la commande. Le pire cas des délais devient 144 appels muets (259,2 USD) au lieu de « 148, 266,4 USD ».
- **I4 — la ligne de GO-21 (registre privé, ligne 67) cite le commit `d15f489`, le texte gèle `e58cfec`.** La différence porte sur l'ordre des issues et le code 6, sans effet sur le devis. C'est à toi de consigner cet écart avant le scellement.
- **I5 — la seconde course n'est prévue qu'après un arrêt.** Ni une issue 6 d'infrastructure, ni un plantage du lanceur, ni un arrêt décidé par Lazar n'ouvrent de seconde course.
- **I6 — écarts à T incomplets en section 0.4.** Il manque l'instrument calculé sur les seules tentatives répondues (et le sens R4 de la part de lois distinctes), les audits A8 et A9, et la règle du registre des GO (T, ligne 173).
- **I7 — trois points du relais à lire avant la course** : son plafond propre (402/429), sa taille de requête maximale face aux 90 363 octets de la consigne la plus longue (413), et ce qu'il rend sur une erreur ou un refus de quota de l'interface.

**Nœud B1, recommandation**
- (a) Accepter et déclarer, couples seuls : la course part dès le scellement, le risque reste.
- (b) Code 3.1 : attendre aussi sur le code 3 au pire cas, et lire un refus de la garde du registre comme un arrêt au plafond. Coût : quelques heures (code, essais, banc, brouillon 4, contre-lecture).
- (c) Faire reprendre les erreurs passagères par le relais, chez session-depot.
- Je recommande (a), avec d'abord la réponse de session-depot au point (c) du couple n° 39. Je garde (b) pour les courses suivantes, Kimi en premier. Confiance 0,6 ; défaut sous 48 heures : (a).

**M10 (question, sans couple)** : R-1276 demande des témoins positif et négatif plantés dans chaque course. A1-v3 n'a pas de témoin négatif planté. À toi de l'appliquer à cette course (il faudrait du code) ou de l'en dispenser par écrit.

**Rejoués (arbre extrait de `08b1f17`, hors du dépôt, `nice -n 10`)**
- Essais v3 : 68 réussis, 98 sous-essais, 0 échec (19:40:26 à 19:41:48 UTC).
- Essais v2 : 45 réussis, 54 sous-essais.
- Banc : 40 mutations sur 40 tuées pour la raison attendue, témoin 29 essais sans échec avant et après, code 0 (19:41:48 à 19:43:25).
- `lire_plan` accepte le bloc ; le devis est égal à la section 12.
- `verifier_go` : la ligne factice à 400 USD est acceptée et les artefacts refusés. La vraie ligne GO-21 et le registre privé entier sont acceptés à 400 USD (seule ligne qui porte l'identifiant).
- Le bloc des 73 empreintes correspond à `FICHIERS_GELES`, au commit `e58cfec` et au disque. Les 71 lignes de T sont identiques.
- Tableau de lecture recalculé pour u = 1 à 24 : exact. Les lignes u = 17, 15 et 13 manquaient (M5).

**Notes**
- La tête du dépôt est passée de `08b1f17` à `516feca` pendant mon travail (commits d'autres sessions). Le brouillon 3 et les 73 fichiers gelés sont inchangés.
- `pole/juges_idees_v2.py` modifié et `essais/__pycache__` (touché à 20:05 UTC) viennent d'autres sessions, pas de moi.
- Scripts, sorties et arbre extrait sont dans `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-v3-contre-lecture/` (empreintes en section 7 du rapport).
- Rien de nouveau à mettre en mémoire.