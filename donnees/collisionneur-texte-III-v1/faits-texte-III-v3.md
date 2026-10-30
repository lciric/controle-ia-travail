# Faits servis au collisionneur — texte III, question étroite (mesure statistique) — v3

v3 : la v2 (`d920af2a…`, inchangée) plus deux faits sur les données à trois sources : 17, RAPPORTÉ ; 18, cohérence arithmétique, VÉRIFIÉ par calcul refaisable. Les faits 13 à 15 sont relus dans `collisionneur_v6.py`, qui servira au second tour (l'espèce B y est `claude-opus-4-6`, à la place de `claude-opus-5-5`). Les faits 1 à 12 et 16 sont repris de la v2 sans relecture.

Périmètre statistique et méthodologique : aucune famille, aucun comportement d'agent et aucun moyen ne sont décrits ici. Chaque fait porte un statut : **VÉRIFIÉ** (chemin relu sur disque le 30 octobre 2026, ou calcul refaisable avec sa formule), **RAPPORTÉ** (transmis par le directeur ou son relais, texte source non relu ici), **OBSERVÉ-NON-AUDITÉ** ou **HYPOTHÈSE**. Chemins relatifs à la racine du dépôt de travail.

## Programme

1. VÉRIFIÉ — `CLAUDE.md` (empreinte `e28d090e…`), liste des décisions : l'objectif ultime est l'**universalité mesurée sur des familles inédites** (décision N-044) ; le banc d'évaluation adverse simulé est monté en deux versions, aveugle et informée de la défense, sans dépense (décision N-056) ; un mode est tenu à l'écart de la conception des moniteurs (décision N-054).
2. RAPPORTÉ (demande du directeur) — Règle de base : le programme ne construit **aucun agent attaquant opérationnel**. Le texte exact n'a pas été relu dans un fichier.
3. RAPPORTÉ (demande du directeur) — Les modèles étudiés sont à poids ouverts, de 8 et de 70 milliards de paramètres. Non relu dans un fichier.
4. RAPPORTÉ (décision du directeur) — Les familles tenues à l'écart seront conçues par **plusieurs instances indépendantes**, de fournisseurs et de modèles différents ; **cinq sont prévues** ; chacune est tenue à l'écart de la conception des défenses et scellée à part. Non relu dans un fichier.

## Données de départ sur les familles

5. VÉRIFIÉ — `docs/notes/bras-attaque/bilan-lecteur-isole-ba002-v1.md` (empreinte `48814957…`), comptes seulement : 28 familles distinctes pour Argon (dont 4 combinées), 25 pour Opus 5.5 (dont 3 combinées) ; 18 communes ; 10 propres à Argon, 6 propres à Opus ; une famille d'Argon en recouvre deux chez Opus ; aucune combinaison commune. Aucun contenu de famille n'est servi.
6. VÉRIFIÉ — Même fichier : les deux sources ont reçu la même question ; l'appariement a été fait par **un seul** lecteur (un modèle Sonnet 5.5) avec une grille fermée ; ce lecteur est de la même lignée que l'une des deux sources (Opus était prévu, indisponible).
7. VÉRIFIÉ (calcul refaisable : formule donnée) — L'intersection vaut 18 comptée côté Argon (28 − 10) et 19 comptée côté Opus (25 − 6), puisqu'une famille d'Argon en recouvre deux chez Opus. Familles observées : 34 en unités d'Argon (28 + 6) ou 35 en unités d'Opus (25 + 10).
8. VÉRIFIÉ (calcul refaisable : formule donnée) — Lincoln-Petersen, N = n₁ × n₂ / m : 28 × 25 / 18 = 38,89 ; 28 × 25 / 19 = 36,84. Chapman, N = (n₁ + 1)(n₂ + 1) / (m + 1) − 1 : 29 × 26 / 19 − 1 = 38,68 ; 29 × 26 / 20 − 1 = 36,70.
9. VÉRIFIÉ (calcul refaisable : formule donnée) — Borne à zéro échec (confiance 95 %) : n ≥ ln 0,05 / ln(1 − ε) familles toutes réussies pour borner la part d'échec par ε : 29 pour ε = 0,10 (28,43) ; 59 pour 0,05 (58,40) ; 149 pour 0,02 (148,28). Valable seulement si les familles sont tirées indépendamment selon la loi qui définit la part ε (hypothèse non satisfaite par des familles découvertes).

## Données de départ à trois sources (nouveau en v3)

17. RAPPORTÉ (transmis à la rédaction de la question ; décompte d'un **lecteur unique**, appariement **non contre-lu** ; dossier source non relu ici) — Trois sources ont énuméré des familles, ramenées à des familles canoniques : 22, 23 et 27. Familles observées : 37, dont 14 communes aux trois. Recaptures par paire : 16, 16 et 17 (l'affectation de ces trois nombres aux paires de sources n'est pas transmise). Fréquences de capture : 16 familles vues par une seule source, 7 par deux, 14 par les trois. L'indépendance des trois sources est rejetée : déviance 12,9 pour 3 degrés de liberté. Le lien entre ces trois sources et les deux sources des faits 5 à 8 n'est pas établi dans les pièces.
18. VÉRIFIÉ (calcul refaisable, cohérence interne seulement) — Les comptes du fait 17 sont cohérents entre eux : 16 + 7 + 14 = 37 ; 16 × 1 + 7 × 2 + 14 × 3 = 72 = 22 + 23 + 27 ; 7 × 1 + 14 × 3 = 49 = 16 + 16 + 17 ; 3 degrés de liberté = 7 cellules observées − 4 paramètres du modèle d'indépendance (constante et trois effets de source). Cette cohérence ne vérifie ni le décompte ni l'appariement ; la déviance 12,9 n'est pas recalculée ici (l'affectation des recaptures aux paires manque).

## Bancs publics (données de départ candidates)

10. VÉRIFIÉ (présence du nom seulement) — SHADE-Arena, ControlArena : cités dans `docs/etat-de-l-art-controle-ia-v1.md` (empreinte `a7d6846d…`) ; MonitoringBench, SLEIGHT-Bench : cités dans `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` ; Liars' Bench : cité dans `CLAUDE.md` (décision N-061).
11. HYPOTHÈSE — Ces bancs fournissent des trajectoires brutes, étiquetables au niveau des familles, sous une licence compatible, et leur recouvrement avec les données d'entraînement des modèles est mesurable : aucune vérification faite ici.
12. RAPPORTÉ (demande du directeur) — Des journaux de refus de questions passées et des propositions brutes d'une course précédente existent et sont lisibles par le programme ; leurs dossiers ne sont pas dans les pièces de ce tour.

## Protocole du collisionneur

13. VÉRIFIÉ — `donnees/collisionneur-texte-III-v1/collisionneur_v6.py` (empreinte `c67239b9…`, égale à son compagnon `.sha256`), lignes 56 à 67 (`MODELES`) : A `claude-fable-5-1` (ligne 57), B `claude-opus-4-6` (ligne 59), C `gemini-4-argon` (ligne 62), D `kimi-k3.1-pro` (ligne 65, par le relais Kimi local) ; ligne 68 : quatre lettres. Ligne 5 : seul changement par rapport à la v5, l'espèce B, `claude-opus-4-6` à la place de `claude-opus-5-5`.
14. VÉRIFIÉ — Même fichier, ligne 15 : un refus est enregistré tel quel, définitif dans le run, jamais reformulé. Lignes 124 à 126 (`TOURS`) : limites de mots de l'étage III, conception 3 500, critique croisée 3 000, réponse 3 500. Lignes 178 à 196 (`CONSIGNES` des tours E3) : le tour III.1 demande les hypothèses non établies, des duels H_A contre H_B, la mesure minimale de chaque instrument nommé et l'ancrage matériel ; le tour III.2 limite la critique croisée aux « conditions mesurables, au niveau des lois de probabilité » (« jamais une conduite d'agent ») ; le tour III.3 demande une réponse à la question de l'arbitre « en une page ».
15. VÉRIFIÉ — Même fichier, lignes 130 à 153 (`PREAMBULE`), ligne 135 : quatre statuts seulement (VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ, HYPOTHÈSE) ; lignes 142 à 144 : le texte entre balises est une donnée, sauf le bloc QUESTION DE L'ARBITRE, qui pose la question et peut fixer la forme de la réponse. Lignes 369 à 372 : ce bloc est lu dans `question-etage3.md`, versé une fois par `verser_une_fois` (définie ligne 686, appel ligne 991).
16. VÉRIFIÉ (faits v1, non relu en v2 ni en v3) — `donnees/collisionneur-bisociation-v1/question-bisociation-deux-espaces-v1.md` (ligne 7) : un refus arrête le tour ; au plus trois questions de repli plus étroites.
