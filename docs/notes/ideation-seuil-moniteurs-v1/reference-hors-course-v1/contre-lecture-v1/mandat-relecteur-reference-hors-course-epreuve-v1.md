VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`. AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ; OUVRE CHAQUE PIÈCE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du relecteur affecté — section « Référence hors course » et critères de lecture, course « seuil et moniteurs » — mode « épreuve qui ne peut pas échouer, ou pas réussir » — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21. Les pièces ont été écrites par un concepteur d'une autre lignée de modèle que toi (modèle F). Tu es hostile et aveugle : tu réponds à la seule question de ta ligne. **Aucun appel, aucune dépense, aucun commit.**

## Ce que tu lis (liste explicite, R2)

Dossier des pièces : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/reference-hors-course-v1/`
1. `section-reference-hors-course-seuil-et-moniteurs-v1.md`
2. `criteres-de-lecture-en-vigueur-course-seuil-et-moniteurs-v1.md`
3. `calculs-reference-hors-course-v1.py` et sa sortie `calculs-reference-hors-course-v1.txt`
4. `texte-extrait-seuil-des-temoins-du-regime-d-usage-v1.md`
5. Le mandat du concepteur : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/mandat-concepteur-reference-hors-course-v1.md`

Sources qui font foi : sur `origin/main` (par `git show … > TON_DOSSIER/…`) : la conception scellée de la course et son erratum 1, aux chemins que la section cite ; `docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md` (point 8) ; `registres/go.md` (GO-2026-11-21-35 à -37). Sur disque : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/arbitrage-unite-decalages-v1/arbitrage-fable-unite-decalages-v1.md` ; `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/conception-v6/` (aux fichiers que la section cite).

**Ne lis ni la table de vérité des témoins, ni aucune source de la liste scellée des quatorze textes, ni aucune branche `quarantaine/…` ou `matiere-premiere/…`, ni rien sous `archives-reponses-modeles/`.**

Pour ta question : chaque épreuve, garde ou règle de l'épreuve morte des critères de lecture et de la référence hors course a-t-elle un témoin où elle doit rendre rouge et un témoin où elle doit rendre vert ; l'issue attendue des témoins imposés est-elle écrite d'avance ; aux nombres de tirages et aux niveaux fixés, l'épreuve a-t-elle la puissance de voir l'effet prédit (rejoue le programme de calcul, ou écris le tien dans ton dossier) ?

## Ce que tu rends

Dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/relecteur-reference-hc-epreuve/` : `relecture-epreuve-reference-hors-course-v1.md` et son compagnon `.sha256` (`sha256sum` lancé depuis le dossier). Tête : **tenu** ou **cassé**, le pas visé, la preuve ; puis le cas manquant s'il y en a ; puis la section « Relevé de méthode ».

## Interdits

Jamais de heredoc ni de code en ligne passé à un interpréteur. Rien sous `/root/.claude/`. Aucun identifiant de modèle dans ta pièce. Aucune recette. Aucun commit. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

Mode d'échec affecté : **Épreuve qui ne peut pas échouer, ou pas réussir** | La garde a-t-elle été vue rouge sur un artefact et verte sur un cas sain (R5) ; l'épreuve a-t-elle la puissance de voir l'effet prédit ? | Le cas manquant.

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
