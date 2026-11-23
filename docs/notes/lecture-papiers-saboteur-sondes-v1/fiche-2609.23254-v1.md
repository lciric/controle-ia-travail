# Fiche de lecture — arXiv 2609.23254 — v1

- **Titre** : The Price of Self-Calibration: Exact Evidence Budgets and Manufactured Blind Sets in Adaptive Monitoring. **Auteur** : Abdou-Raouf Atarmla (seul auteur, prépublication).
- **PDF** : `docs/sources/pdf/percee-controle-securite-v1/2609.23254v1.pdf`, sha256 `1d212b4a1b233c9a20de08a14f80647d5eadf6e11701aeedbee753e4de06eda8` (recalculée, R11). Registre : `registres/veille-de-cap/papiers-du-depot-v1.md`, rang 13.
- **Décision lue** : `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, l. 73 (et l. 43-100, l. 304), errata 1 et 2 (sans effet sur ce papier).
- **Lecteur** : Claude Opus 5.5, effort élevé. **Date** : 2026-11-23T08:46Z (`date -u`). Pages lues : 1-2, 6, 12.

---

**(a) Ce que le papier établit.** Un moniteur qui recale lui-même son seuil absorbe le changement lent. Un saut persistant de hauteur δ ne produit qu'une masse d'alertes en excès égale à δ/η, à une alerte près (η : gain d'adaptation) ; une rampe de pente c produit un taux d'excès c/η, jusqu'à la borne c = η(1 − α) (p. 1-2 du PDF). Théorème 4 : tout moniteur tenu à une taille uniforme α sur une classe de dérives tolérées D a une puissance au plus α contre toute panne de l'ensemble différence D − D, pour toute règle et tout horizon ; les procédures valides à tout instant y sont comprises : « no betting scheme recovers what the tolerance obligation removes » (p. 6). Corollaire 2 : pour des dérives de vitesse au plus v, l'ensemble aveugle est exactement la classe de vitesse 2v, quelle que soit la grandeur finale (p. 6). Limites dites par l'auteur : scores scalaires, suiveur à gain linéaire, pire cas sur la classe, scores à plusieurs dimensions non traités (p. 12).

**(b) Ce que la décision voulait en tirer.** Un voisin qui occupe une part de la loi de la référence honnête : l'ensemble aveugle d'un moniteur tolérant. **Le permet** : la citation est exacte à la page dite. Mais l'objet du papier est la tolérance à une dérive, non la taille m de la référence ; il occupe le revers (guetteur qui ne connaît pas son bruit), pas la règle d'horizon. Le cadre scalaire et sans agent est une limite du papier, non un trou du champ (R8).

**(c) Usage.** Pour l'entretien : il prévient l'objection « accumuler des indices faibles finit par détecter ». Si la référence honnête doit tolérer une dérive (modèle mis à jour, tâches qui changent), tout sabotage plus lent que deux fois la vitesse tolérée est invisible pour toute règle (p. 6). Pour le billet sur les sondes : une sonde au seuil recalé en ligne fabrique son propre ensemble aveugle, ce qui rejoint la sonde aveuglée par la dérive d'entraînement ordinaire. Épreuve fournie : un monde planté « dérive honnête tolérée à vitesse v, sabotage à vitesse 2v », où tout agrégateur reste à puissance α. Antériorité : « l'ensemble aveugle créé par la tolérance » ne se revendique pas.

**(d) Plus petite action.** Proposer d'ajouter ce monde planté aux mondes de l'étape 0 (sur processeur), et une ligne à l'objection sur l'accumulation de la note d'entretien. Coût : environ 30 minutes de session, aucune dépense.
