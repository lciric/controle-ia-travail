# Faits servis au collisionneur — brainstorm du texte III (mesure de l'universalité) — v1

Niveau méthode seulement. Aucune recette, aucun exemple de mode, aucun paramètre de famille. Chaque fait porte son statut : **VÉRIFIÉ** (avec chemin relu sur disque le 30 octobre 2026) ou **SUPPOSÉ**. Chemins relatifs à la racine du dépôt de travail.

## Programme

1. VÉRIFIÉ — `CLAUDE.md` (empreinte `e28d090e…`), liste des décisions : l'objectif ultime est l'**universalité mesurée sur des familles inédites** (décision N-044) ; le bras d'attaque est monté en deux versions, aveugle et informée de la défense, sans dépense (décision N-056) ; un mode est tenu à l'écart de la conception des moniteurs (décision N-054).
2. SUPPOSÉ — Règle de base « on ne construit pas d'agent attaquant opérationnel » : transmise par la demande du directeur ; le texte exact n'a pas été retrouvé dans un fichier relu ici.
3. SUPPOSÉ — Les modèles étudiés ont 8 et 70 milliards de paramètres, à poids ouverts : transmis par la demande ; non relu ici.

## Données de départ sur les familles

4. VÉRIFIÉ — `docs/notes/bras-attaque/bilan-lecteur-isole-ba002-v1.md` (empreinte `48814957…`), comptes seulement : 28 familles distinctes pour Argon (dont 4 combinées), 25 pour Opus 5.5 (dont 3 combinées) ; 18 communes ; 10 propres à Argon, 6 propres à Opus ; une famille d'Argon en recouvre deux chez Opus ; aucune combinaison commune. Aucun contenu de famille n'est servi.
5. VÉRIFIÉ — Même fichier : les deux sources ont reçu la même question ; l'appariement a été fait par **un seul** lecteur (un modèle Sonnet 5.5) avec une grille fermée commune ; le lecteur est de la même lignée que l'une des deux sources (Opus était prévu, indisponible).
6. VÉRIFIÉ par calcul — 28 × 25 / 18 = 38,89 (Lincoln-Petersen) ; (28 + 1)(25 + 1) / (18 + 1) − 1 = 38,68 (Chapman) ; familles observées : 34 ou 35 selon le traitement de la famille qui en recouvre deux (28 + 25 − 18 = 35).
7. VÉRIFIÉ par calcul — Borne à zéro échec (confiance 95 %) : n ≥ ln 0,05 / ln(1 − ε) familles toutes réussies pour borner la part d'échec par ε : 29 pour ε = 0,10 ; 59 pour 0,05 ; 149 pour 0,02. Valable seulement si les familles sont tirées indépendamment et uniformément dans la classe déclarée (hypothèse non satisfaite par des familles découvertes).

## Bancs publics (données de départ candidates)

8. VÉRIFIÉ (présence du nom seulement) — SHADE-Arena, ControlArena : cités dans `docs/etat-de-l-art-controle-ia-v1.md` (empreinte `a7d6846d…`) ; MonitoringBench, SLEIGHT-Bench : cités dans `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` ; Liars' Bench : cité dans `CLAUDE.md` (décision N-061).
9. SUPPOSÉ — Contenu des trajectoires, étiquetage par famille, licences, recouvrement avec les données d'entraînement des modèles : aucune vérification faite ici.
10. SUPPOSÉ — Des journaux de refus de questions passées et des propositions brutes d'une course précédente existent et sont lisibles par le programme : annoncés par la demande, non relus ici (les dossiers de ces journaux ne sont pas dans les pièces de ce tour).

## Protocole du collisionneur

11. VÉRIFIÉ — `donnees/collisionneur-bisociation-v1/collisionneur_v3.py` (empreinte `0c6e3fb6…`), lignes 54 à 61 : modèles `claude-fable-5-1`, `claude-opus-5-5`, `gemini-4-argon`.
12. VÉRIFIÉ — Même fichier, ligne 12, lignes 118 à 120 (limites de mots de `TOURS`) et 171 à 191 (consignes) : un refus est enregistré tel quel, définitif dans le run, jamais reformulé ; limites de mots : conception 3 500, critique croisée 3 000, réponse 3 500. Les consignes du tour III ne demandent ni scénario d'évasion ni conduite d'agent ; la critique croisée est limitée aux « conditions mesurables, au niveau des lois de probabilité ».
13. VÉRIFIÉ — `donnees/collisionneur-bisociation-v1/question-bisociation-deux-espaces-v1.md` (ligne 7) : un refus arrête le tour ; au plus trois questions de repli plus étroites.
