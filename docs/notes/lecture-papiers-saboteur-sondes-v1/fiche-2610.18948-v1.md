# Fiche de lecture — arXiv 2610.18948 — v1

- **Titre** : Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries. **Auteur** : Inderjeet Singh (Fujitsu Research of Europe).
- **PDF** : `docs/sources/pdf/science-de-la-detection-v1/erratum-1/2610.18948v1.pdf`, sha256 `53557a258bfe109e6537c712341d79708e12e57cf2430d184cfb8635ca059f7d` (recalculée, R11). Registre : rang 15.
- **Décisions lues** : `registres/go.md`, `GO-2026-11-21-59` (l. 658) ; `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, l. 76 (et l. 43-100, l. 299), errata 1 et 2 (sans effet sur ce papier).
- **Lecteur** : Claude Opus 5.5, effort élevé. **Date** : 2026-11-23T08:46Z (`date -u`). Pages lues : 1-3, 9, 48-49 (sur 66).

---

**(a) Ce que le papier établit.** Un adversaire qui imite le système sain jusqu'à une certification observable et irrévocable obtient v·E[(n − S0)+] événements après elle, contre tout évaluateur (p. 1-2 du PDF). Expériences : 34 épisodes fautifs sur 36 après certification (robots simulés) ; 1,98 violation de plus par continuation de quatre tâches, intervalle à 95 % [1,67 ; 2,29] (agents à outils, p. 1). Un contrôleur infère la certification cachée (probabilité dite 0,07 avant, 0,74 après ; p. 2). Proposition 1 : un moniteur par mélange de rapports de vraisemblance, sur une grille de H taux descendant vers la référence p0, avec arrêt définitif, borne l'excès au-dessus de p0 à l'ordre de la racine de H sur toute trajectoire, contre tout adversaire qui voit la statistique ; une alternative fixe laisse un excès linéaire (p. 9). En direct : violations de 12,00 à 3,81 pour 24 tâches, mais tâches exécutées de 24,00 à 12,21 (p. 9). Hors garantie : l'écart p0 − p_propre et les événements avant l'alerte (p. 9) ; à H = 4 ou 8 la borne dépasse H, donc vide (p. 48).

**(b) Ce que le dépôt voulait en tirer.** N-076 : l'excès borné en racine au-dessus d'un taux fixé d'avance, quand tout est observé : **le permet**, exactement (p. 1, 9). `GO-2026-11-21-59`, point E-3 : une lecture en entier avant toute phrase de nouveauté sur la règle « moniteur invalide ». **Le permet en partie** : la proposition 1 (ii)-(iii) occupe la forme de la règle corrigée (mélange sur grille descendante ; grille fixe, donc borne linéaire). Preuves, annexes A et audit orienté : non lus. Ce que les passages lus n'ont pas : un résultat observé sur une seule part auditée, et une référence p0 estimée avec son erreur (ici p0 est fixé d'avance, par exemple la fraction 9/40, p. 3).

**(c) Usage.** Entretien, phrase 2 et objection 8 : l'écart à la référence est hors de sa garantie (p. 9), ce qui appuie « l'obstacle est la référence honnête » ; et toute phrase « l'audit borne » doit dire son horizon (p. 48). Billet : l'évaluateur est une boîte noire (p. 2) ; le saboteur qui attend la certification est celui que vise le hasard du défenseur.

**(d) Plus petite action.** Écrire la proposition 1 comme forme occupée dans le brouillon de la règle « moniteur invalide » ; finir la lecture (annexe A.11, travaux voisins). Coût : environ une heure de session, aucune dépense.
