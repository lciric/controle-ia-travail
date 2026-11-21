VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`. AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ; OUVRE CHAQUE PIÈCE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du contre-lecteur — section « Référence hors course », critères de lecture et réponse sur le véhicule, course « seuil et moniteurs » — contre-lecture générale — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21. La section et les critères de lecture entrent dans un préenregistrement (classe A) ; ils ont été écrits par un concepteur d'une autre lignée de modèle que toi (modèle F). Tu fais la contre-lecture due (R2). **Aucun appel, aucune dépense, aucun commit.**

## Ce que tu lis (liste explicite, R2)

Dossier des pièces : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/reference-hors-course-v1/`
1. `section-reference-hors-course-seuil-et-moniteurs-v1.md`
2. `criteres-de-lecture-en-vigueur-course-seuil-et-moniteurs-v1.md`
3. `reponse-vehicule-reference-hors-course-v1.md`
4. `calculs-reference-hors-course-v1.py` et sa sortie `calculs-reference-hors-course-v1.txt`
5. `texte-extrait-seuil-des-temoins-du-regime-d-usage-v1.md`
6. `rapport-concepteur-reference-hors-course-v1.md`, `table-empreintes-concepteur-reference-hors-course-v1.txt`
7. Le mandat du concepteur : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/mandat-concepteur-reference-hors-course-v1.md`

Sources qui font foi : sur `origin/main` (par `git show … > TON_DOSSIER/…`) : la conception scellée de la course et son erratum 1, et le préenregistrement de la conception, aux chemins que le rapport du concepteur cite (vérifie leurs empreintes) ; `docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md` (point 8) ; `docs/notes/papier-dopamine-moniteur-v1/derive-de-regime-v1/corriger-derive-de-regime-v1.md` (§ 6) ; `registres/go.md` (GO-2026-11-21-35 à -37). Sur disque : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/arbitrage-unite-decalages-v1/arbitrage-fable-unite-decalages-v1.md` ; `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/conception-v6/` (ordre et préenregistrement, aux fichiers que le rapport cite) ; `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/programme-verification-sortie-mondes-v5/rapport-developpeur-verification-sortie-mondes-v6.md`.

**Ne lis ni la table de vérité des témoins, ni aucune source de la liste scellée des quatorze textes, ni aucune branche `quarantaine/…` ou `matiere-premiere/…`, ni rien sous `archives-reponses-modeles/`.**

## Ce que tu vérifies

- La référence reste hors de la liste scellée des sources, jouée hors course par programme sur les mondes scellés, rapportée à côté de la base, jamais parmi les candidates (point 8 de l'arbitrage).
- Les critères de lecture (condition (a) de GO-2026-11-21-37) : seuils, nombres de tirages, niveaux des tests, règle de l'épreuve morte, issues attendues des témoins imposés, liste nominative des valeurs que les mondes fourniront ; la réserve « sans gain en monde à dérive » avec les taux de la base aux trois tailles, la ligne d'arrêt « aucun score du suspect dans l'étalonnage d'un seuil » (GO-2026-11-21-35) ; l'unité des décalages selon l'arbitrage.
- Rejoue le programme de calcul deux fois vers ton dossier, compare par `cmp` à la sortie versée.
- La réponse sur le véhicule : est-elle juste, et ce qui manque est-il dit ?
- La présence de la section « Relevé de méthode » dans les pièces du concepteur.

## Ce que tu rends

Dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-reference-hc-generale/` : `contre-lecture-reference-hors-course-v1.md` et son compagnon `.sha256` (`sha256sum` lancé depuis le dossier). Tête : verdict en une ligne (**Conforme**, **À corriger** ou **Bloquant**) ; puis les corrections numérotées (passage visé, ce qui ne va pas, correction proposée) ; puis la section « Relevé de méthode ».

## Interdits

Jamais de heredoc ni de code en ligne passé à un interpréteur. Rien sous `/root/.claude/`. Aucun identifiant de modèle dans ta pièce. Aucune recette. Aucun commit. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

Mode d'échec affecté : **Réglage sur l'épreuve** | Un seuil, une couche, une invite, un critère ou un choix d'analyse a-t-il été fixé après lecture des données qui servent au verdict ; le jeu final a-t-il été lu plus d'une fois (N-050) ? | Le choix, sa date, la date de la lecture.

## Consigne commune de méthode de recherche (`docs/procedures/consigne-commune-methode-de-recherche-v1.md`, `d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`, GO-2026-11-21-38), partie 1 collée telle quelle

> **Consigne commune de méthode (v1).** Ta pièce rendue contient une section intitulée exactement « Relevé de méthode », avec les rubriques ci-dessous, dans cet ordre, sous ces intitulés exacts. Une rubrique qui ne s'applique pas porte « Sans objet : » suivi du motif en une phrase ; une rubrique vide ou absente rend la pièce irrecevable.
>
> **Chaîne de raisonnement.** Écris la chaîne, non la conclusion : des pas numérotés, chacun appuyé sur une pièce (chemin et empreinte), un calcul rejouable, un pas antérieur, ou marqué « supposé ». Une affirmation sans pas qui la porte n'est pas reçue.
>
> **Objets de contrôle.** Avant de croire un mécanisme (une sonde, un moniteur, un test de mort, un juge, un argument, une garantie), éprouve-le sur au moins un objet où ce qu'il doit établir est faux par construction, et sur un objet où c'est vrai par construction. Nomme les deux, dis d'avance ce que le mécanisme doit y rendre, puis ce qu'il y rend. Un mécanisme qui « réussit » là où la conclusion est fausse est mort, quel que soit son résultat ailleurs.
>
> **Premier pas non justifié.** Désigne, par son numéro dans ta chaîne, le premier pas que tu ne sais pas justifier entièrement, et dis ce qui le justifierait. « Aucun » n'est reçu que si chaque pas renvoie à une pièce ou à un calcul rejoué.
>
> **Mode d'échec affecté.** (Relecteur seulement.) Tu es hostile et aveugle : tu ne lis ni les autres relectures ni les échanges avec l'auteur. Tu réponds à une seule question, celle de ta ligne ; tu ne « vérifies » pas la pièce en général. Tu rends : tenu ou cassé, le pas visé, la preuve de ce que tu avances.
>
> **Dérivation de l'énoncé seul.** (Agent de re-dérivation seulement.) Tu ne reçois que l'énoncé. Tu le démontres, le recalcules ou le réfutes par ta propre voie, sans chercher la pièce d'origine. Tu rends ta chaîne et ton résultat ; la comparaison n'est pas ton travail.
>
> **Trouvaille de côté.** Si ce que tu cherches se révèle vide, faux ou déjà connu, dis-le en clair, avec ce qui le montre : c'est un résultat. Si tu vois en chemin autre chose que ta cible, note-le en trois lignes sans le poursuivre. Tu n'ouvres aucune course, aucune lecture de résultat et aucune dépense pour le suivre.
>
> **Évaluateur et conseil.** Dis ce qui juge ton produit (programme, épreuve, lecteur), sur quels témoins ce juge a été admis, et par où ton produit pourrait obtenir un bon jugement sans le mériter. Si tu conçois une course : le juge est écrit et admis avant la génération.
