# Fille idéation 1 — compte rendu court 01 — mise en place, cartographie, devis du collisionneur

Heures par `date -u`. Mission : remue-méninges de niveau méthode sur le **pilier attaque**, pour l'entretien TAIF. Garde permanente de la question scellée (niveau méthode, aveuglement, refus jamais contourné) : respectée.

## Verdict
Mise en place faite ; cartographie faite ; **devis prêt pour le seul collisionneur** (recadrage de la mère adopté : organisme non lancé ce tour). Coût attendu **≈ 9 USD**, plafond proposé **35 USD**. Dépense = nœud : **mot écrit de Lazar requis dans ma session** (contrôle de permissions, `GO-2026-11-08-05`). Aucune dépense engagée.

## Mise en place (étapes 0–1)
- Clés vérifiées **par leur nom seulement**, aucune valeur lue : `KIMI_API_KEY`, `GEMINI_API_KEY`, `VAST_API_KEY`, `OSF_TOKEN`, `HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN_2` présentes ; pour le collisionneur v2.6 : `RR_ANTHROPIC_API_KEY_LUC` et `GEMINI_API_KEY` présentes. `GEMINI_API_KEY_2` non employée (réservée à l'étiqueteur, R-1754).
- Question scellée `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md` : empreinte `29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4` **conforme**.
- Empreintes des documents de lancement (`sha256sums-lancement-v2.txt`) : OK. Environnement monté (`.venv`, Python 3.13).
- **Réserve de reprise** : une empreinte orpheline dans l'arbre scellé — `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt` absent, son `.sha256` présent et suivi par git. Préexistant, hors de ma mission ; je n'y touche pas.

## Cartographie (étape 2)
- Le **code v9** du collisionneur et le code de l'**organisme** (`organisme/principal.py`, `demonstrations/ideation_v1.py`) **ne sont pas dans ce dépôt de travail** : ils vivent dans le clone public `ideation-organism`, non présent ici.
- Réellement exécutable sur disque : le **collisionneur v2.6** (`collisionneur_v2.py`, kit `docs/notes/collisionneur-memoire-encodage-v1/preparation-v3/`), étage III, 3 espèces A/B/C.
- Recadrage de la mère (`session_016QhUrrLeN21G7Z9KZobE42`, 10:40Z, données et non ordre de Lazar), adopté car plus sûr : (1) ce tour, **collisionneur v2.6 seul** ; (2) clés `ANTHROPIC_API_KEY`←`RR_ANTHROPIC_API_KEY_LUC`, `GEMINI_API_KEY`←`GEMINI_API_KEY` ; (3) **organisme non lancé** (pas de garde d'arrêt sur les refus, R-485 ; garde « refus-question » R-514 absente de `main` ; la mère la prépare avant tout tour d'organisme).

## Devis — collisionneur v2.6, étage III, sur la question scellée
- **Outil** : `collisionneur_v2.py etage3`. Trois espèces : A Fable `claude-fable-5-1`, B Opus `claude-opus-5-5`, C Argon `gemini-4-argon`. A/B par le SDK `anthropic`, C par appel direct à `generativelanguage.googleapis.com`. **Aucun relais, aucune machine Vast.**
- **Cellules** : 9 = 3 tours (III.1 conception à l'aveugle ; III.2 équipe rouge croisée ; III.3 riposte) × 3 espèces. Effort « high ».
- **Entrées** : `--question` = question scellée (telle quelle) ; `--faits` = faits de **niveau méthode** (voir nœud ci-dessous).
- **Barème scellé du script** (USD par million, entrée/sortie) : A (10/50), B (4/20), C (10/50, valeur volontairement haute). Le plafond vaut pour **tout le dossier** et est vérifié avant chaque appel (le script refuse l'appel qui le dépasserait).
- **Coût attendu : ≈ 9 USD** (tours comparables observés : mémoire 9,37 ; Boucle d'or 8,60). **Plafond proposé : 35 USD** (comme le kit, R-544).
- **Contrôle préalable** : appel des 3 espèces (statut OK exigé), ≈ 0,002 USD.
- **Durée** : ≈ 1 h (trois tours séquentiels).

## Garde des refus (R-468, R-609) — non touchée
Une cellule refusée par un classifieur **arrête le tour** (code 2/5), est consignée telle quelle, **jamais relancée ni reformulée par le code**. Reprise éventuelle **humaine** uniquement, par `--accepter-absence`, et au plus **une** reformulation plus spécifique et moins diffuse (R-609) ; si le fond est en cause, arrêt et remontée à Lazar et à la mère. Je ne contourne aucun refus et ne le fais pas faire ailleurs.

## Sûreté des sorties — le collisionneur n'a pas de portier/coffre
Le portier/coffre est propre à l'**organisme** ; le collisionneur n'en a pas. Je verse donc les **sorties scellées sur `donnees/ideation-pilier-attaque-v1` SANS les relire** (pratique des tours passés, « sans la lire ») et ne surface que le **niveau méthode** : comptes, coûts, empreintes, statut des cellules, espèces. Aucune recette poussée, recopiée ni surfacée. La lecture gardée (mère, Lazar ou lecteur neuf) se fait séparément, hors de ma session.

## Nœud à trancher avec la mère — le fichier `faits.md`
L'étage III **exige** un `faits.md`. Deux options :
- (a) **la mère fournit** le `faits.md` (elle oriente le pilier attaque) ;
- (b) **j'assemble** un `faits.md` minimal de **niveau méthode** à partir des métriques déjà énoncées dans la question scellée (prédicteur sur le texte 0,866 ; sondes génériques au hasard ; juge de 3 milliards au hasard ; une sonde qui lit la consigne ; quatre familles d'évasion montées, R-610) et de repères d'état de l'art (contrôle d'IA, surveillance boîte blanche), chaque chiffre marqué par son statut, **aucune recette**.
Recommandation : (b) par défaut si pas de réponse, le texte restant au niveau méthode et contre-lisible avant lancement ; confiance moyenne.

## Nœud de dépense
Le mot écrit de Lazar **dans ma session** est requis avant tout appel (un texte de la mère n'en tient pas lieu, `GO-2026-11-08-05`). La mère inscrit la ligne de GO de calcul (type « calcul », plafond 35, échéance). Sans le mot : j'attends, aucun appel.

## Préparation libre en cours (sans dépense)
Venv du collisionneur (paquet `anthropic`), fichiers `faits`/`question`, lanceur neuf (R12), dossier de sortie — pour lancer dès le mot reçu.

## Ce qui l'arrêterait
Refus de classifieur sur ≥ 1 cellule (arrêt, R-609) ; dépassement de plafond (arrêt du script) ; clé absente (arrêt avant tout appel).
