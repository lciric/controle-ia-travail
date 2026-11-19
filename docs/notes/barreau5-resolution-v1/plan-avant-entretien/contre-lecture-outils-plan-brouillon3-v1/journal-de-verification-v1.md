# Journal de la vérification du brouillon 3 (contre-lecteur Opus 5.5) — v1

Pièce de travail, tenue au fil de la vérification (registre « qui a lu quoi »). Ouvert depuis le rendu de la contre-lecture du brouillon 2 :

- empreintes vérifiées : brouillon 3 (525f338e…), devis brouillon 3 (7ac56a7b…), fiche v3 (d28e9259…), table des corrections (1d010c7d…), simulation v4 (632c048a…) et sa sortie, calcul du devis v3 (9335ac98…) et sa sortie, mandat du rédacteur du brouillon 3 (44078675…), mandat du développeur du code de formation
- dossier docs/notes/barreau5-resolution-v1/plan-avant-entretien/ (liste)
- relu en entier (brouillon 3, par tranches) ; fiche v3 (entière) ; mandat du développeur du code de formation (entier, empreinte 94c6bbb3… vérifiée) ; sortie de la simulation v4 (tableau des taux par monde, par programme) ; calcul du devis v3 (entier)
- ma contre-lecture du brouillon 2 (recherche du mot « trace », lignes citées) ; ma simulation v1 (en-tête, outils, bloc B) ; mon script de couples v1 (couple M-7a)
- comparaison par programme des sections figées, brouillon 2 contre brouillon 3 (points 1 à 7, 14, 17 du plan ; points 1 à 5, 12, 14 de la liste d'arrêt ; « Objet et portée » ; « Données gardées » ; « Code neuf »)

Déroulé (heures UTC approximatives) :

- 16:55 : première version de ma simulation ; une passe rapide (100 mondes par case) ; une passe pleine lancée puis arrêtée par son identifiant de processus après 89 secondes (sortie vide, remplacée), pour ajouter les variantes de sonde et le tirage des graines par case.
- 17:01 : passe pleine de la simulation (69 mondes, deux dimensions, trois sondes, 1 000 mondes par case, quatre processus) ; sortie `sortie-simulation-verification-brouillon3-v1.json`.
- 17:10 : contrôle de précision, neuf cases à 20 000 mondes ; puis quatre cases ajoutées en fin de liste et contrôle rejoué en entier (les neuf premières cases rendent à l'identique, vérifié par programme) ; sortie unique, la seconde.
- 17:15 : couples exacts écrits, vérifiés par programme (23, aucun défaut ; un faux défaut de ma propre vérification corrigé avant la sortie : un « après » contenu dans son « avant ») ; chiffres des couples de la voie (i) repris de la sortie de la simulation et du contrôle de précision.
- 17:20 : comparaison par programme des couples du brouillon 2 qui ont produit les changements des sections figées (m-4a, m-4b, m-12a, m-12b, M-5a, M-5b).
- 17:25 : vérification écrite, scellement de toutes les pièces.

Aucun fichier interdit ouvert ; aucune recherche plein texte hors des dossiers nommés ; rien sous `/root/.claude/` ; aucun refus d'outil ; un appel d'attente refusé par le harnais (attente au premier plan), remplacé par une attente en arrière-plan.
