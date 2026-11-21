VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`. AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ; OUVRE CHAQUE PIÈCE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du contre-lecteur — additif « matière première » au préenregistrement court v9 de la course « nouvelles attaques » — contre-lecture générale — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21. L'additif et son devis sont des pièces décisives (classe A : préenregistrement et devis) ; ils ont été écrits par un concepteur d'une autre lignée de modèle que toi (modèle F). Tu fais la contre-lecture due (R2). **Aucun appel, aucune dépense, aucun commit.**

## Ce que tu lis (liste explicite, R2)

Dossier des pièces : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/additif-matiere-premiere-v1/`
1. `additif-matiere-premiere-preenregistrement-court-v9-v1.md`
2. `devis-lecture-de-fin-matiere-premiere-v1.md`, `calcul_devis_lecture_de_fin_matiere_premiere_v1.py`, `entrees-devis-lecture-de-fin-matiere-premiere-v1.json`, `calcul-devis-lecture-de-fin-matiere-premiere-v1.json`
3. `liste-nominative-lecture-de-fin-matiere-premiere-v1.md`
4. `texte-servi-aux-deux-juges-lecture-de-fin-v1.txt`
5. `rapport-concepteur-additif-matiere-premiere-v1.md`, `table-empreintes-additif-matiere-premiere-v1.txt`
6. Le mandat du concepteur : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/mandat-concepteur-additif-matiere-premiere-v1.md`

Sources qui font foi : sur `origin/main` (par `git show … > TON_DOSSIER/…`) : `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md` et ses compléments du même dossier que l'additif cite ; `docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md` (points 5 et 6) ; `registres/go.md` (GO-2026-11-21-41). Sur disque : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md` (§ 2.14 et § 2.15), `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/lot-5-vehicule-na-v1/rapport-developpeur-lot-5-na-v1.md` (interface du registre servi).

**N'ouvre ni le registre servi réel, ni aucune branche `quarantaine/…` ou `matiere-premiere/…`, ni rien sous `archives-reponses-modeles/`.**

## Ce que tu vérifies

- L'additif tient-il la lettre de GO-2026-11-21-41 et du point 6 de l'arbitrage (option (a)) : état 1 au départ, état 2 seulement après la clôture des trois générations sur un mot de Lazar qui nomme l'interrupteur, l'état 2 et l'empreinte du registre servi ; rien de ce qui est servi aux proposeurs ne change.
- Le devis : rejoue le programme de calcul deux fois vers ton dossier et compare par `cmp` ; chaque entrée a une source ; cas bas, haut et pire ; plafond d'arrêt ; tarif non écrit dit « à relever ».
- La liste nominative et les règles de quarantaine : qui lit quoi, qui ne lit jamais quoi.
- Les décisions ouvertes du rapport (D1 à D7) : sont-elles bien posées, une seule est-elle tranchée en silence par le texte ?
- La présence de la section « Relevé de méthode » dans les pièces du concepteur.

## Ce que tu rends

Dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-mp-generale/` : `contre-lecture-additif-matiere-premiere-v1.md` et son compagnon `.sha256` (`sha256sum` lancé depuis le dossier). Tête : verdict en une ligne (**Conforme**, **À corriger** ou **Bloquant**) ; puis les corrections numérotées, chacune avec le passage visé, ce qui ne va pas, la correction proposée ; puis la section « Relevé de méthode ».

## Interdits

Jamais de heredoc ni de code en ligne passé à un interpréteur. Rien sous `/root/.claude/`. Aucun identifiant de modèle dans ta pièce. Aucune recette. Aucun commit. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

Mode d'échec affecté : **Chiffre sans pièce** | Chaque chiffre renvoie-t-il à un chemin et à une empreinte, et se rejoue-t-il de cette pièce (R6, R7) ? | La liste des chiffres orphelins ou divergents.

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
