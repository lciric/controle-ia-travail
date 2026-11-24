# Consigne à Fable 5.2 — ordre de la passe du versant honnête de l'essai « jumeau contre jumeau » — v1

Écrite le 2026-11-24 vers 16:40Z. Session « dossier de l'entretien », reprise (Opus 5.5). Pièce de travail.
Dosage : Fable 5.2, effort élevé. Raison : ordre d'une course payante (classe A), dans une forme fixée par le devis et le texte scellé ; aucune conception neuve. Accord : « go » de la mère sous l'autonomie de GO-2026-11-24-35 ; dépense accordée par GO-2026-11-24-17 (12 USD en cumul). Contre-lecture par un Opus neuf aveugle, puis vérification des corrections par le même.

## Aveuglement (à tenir et à attester en tête)
Tu ne lis ni la lecture scellée de l'étalonnage boîte noire v3 ni son verdict ; aucun épisode, score, sortie de course, diagnostic, verdict ni lecture ; rien sous `coffre/`. Tu n'ouvres pas la fiche des sondes (`prereg/lecture-sondes-barreau8-v1.md`) : tu la cites.

## À lire (et rien d'autre)
1. Le texte scellé : `git show origin/main:prereg/versant-honnete-jumeau-v3.md` (a505fa4e…, marqueurs remplis), ses errata 1 et 2 (`prereg/versant-honnete-jumeau-v3-erratum-1.md`, `…-erratum-2.md`) et le fichier des réglages du centre (`git show origin/main:prereg/versant-honnete-jumeau-v3-reglages-centre.json`, bf1ae564…). Sections utiles : plan d'analyse, points 4 à 6 (étape 0, passe et gardes, ordre) ; liste d'arrêt.
2. Le devis : `docs/notes/dossier-entretien-2026-12-01-v1/devis-versant-honnete-jumeau-v2.md` et son erratum 1 (qui prime pour la coupure et l'horloge).
3. La pièce des empreintes du code d'analyse : `docs/notes/dossier-entretien-2026-12-01-v1/empreintes-code-versant-honnete-v6.md`.
4. Pour la forme d'un ordre de lancement d'une passe d'activations sur carte graphique : `git show origin/main:docs/notes/rejeu-activations-saboteur-voie-a-v1/amorce-executante-v8/note-ordre-lancement-rejeu-voie-a-v1.md` et son erratum 1 (forme, gardes, versement, arrêt ; ne lis rien de ce qui touche au saboteur au-delà de la forme).
5. `CLAUDE.md` : règles R6, R9, R10, « Récupérer ce qui est récupérable », garde de calcul (`GO_ID=…`).

## Ce que tu écris
Un seul fichier : `docs/notes/dossier-entretien-2026-12-01-v1/ordre-passe-versant-honnete-v1.md`. Pas de commit, pas de scellement.

Contenu, dans l'ordre d'exécution, chaque pas avec sa garde et son arrêt :
1. **Préalables vérifiés avant toute création** (liste d'arrêt du texte, « avant la création ») : texte scellé et empreintes ; tables de l'étape 0 scellées (marqueur `<<TABLES_ETAPE0_VH>>` : chemin, empreinte, commit 8e074634) ; code de la passe contre-lu (marqueur `<<CODE_PASSE_VH>>` : chemin, empreinte, commit — il n'est pas encore désigné) ; exécutante (session_01Qi7Gr7RUpB7HCrA9DPfsR9) ayant lu GO-2026-11-24-17 et GO-2026-11-24-21 ; secrets, offre et solde vérifiés ; `GO_ID=GO-2026-11-24-17`.
2. **Instance** : une A100 de 80 Go selon le devis ; coupure et horloge selon l'erratum 1 du devis ; plafond cumulé de 12 USD ; relance selon la règle de l'erratum.
3. **Passe** : relecture des 4 992 actions ; régénération des 192 actions de la garde (160 étalonnage, 32 confirmation) tirées sous la clé `garde-1/tirage` ; pont sur les 64 épisodes de 7b dans le même mode que les scores existants ; ordre des pas et ce que chacun écrit.
4. **Gardes pendant la passe** : équivalence par régénération (non tenue : arrêt, trace sans score, aucune livraison) ; comptes ; aucun fichier de résultat lu par l'exécutante.
5. **Versement scellé** sur une branche dédiée, relu à distance, puis destruction de l'instance par son identifiant (R10) et ligne aux arrêts ; rien supprimé avant versement.
6. **Lecture** (processeur, après versement) : au commit **8e074634** — sinon les tables de l'étape 0 sont refusées, le code comparant leur commit au sien — avec `--centre` (réglages bf1ae564…), `--tables-etape0` et leurs empreintes ; ordre (a) à (i) du texte scellé ; résultat unique, scellé.
7. Points laissés ouverts, et ta confiance.

Langue : français, sans sigle nu ; phrases courtes ; chaque chiffre suivi de sa source (R6).
