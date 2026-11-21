**Mot de Lazar, GO-2026-11-21-74 (`registres/go.md` sur `origin/main`, l. 673), sur les quatre coupures de classifieur de l'organisme : « tous de faux positifs je confirme ».** Si une coupure revient : arrête-toi aussitôt, ne reformule pas, ne découpe pas, et dis-le avec ce que tu faisais.

VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du développeur — véhicule NA-1, lot 6 v2 (reprise du lot 6 v1 récupéré, refus de câblage, rapport) — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 18:30Z. Tu es un développeur neuf (modèle O) : tu n'as écrit ni le lot 6 v1, ni les lots 1 à 5 ni 10 a, ni la conception. Code par un développeur O, vérifié ensuite par un vérificateur S. **Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules ; aucun commit.**

## Ce qui fait foi
1. Le mandat du lot 6 v1 : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-6-v1.md` (`b59766267b5b285ad12395a86bb388fc12af48ebe6ded630a3062c2bac6f6b1d`).
2. Son erratum 1 v2, qui prime : `…/erratum-1-mandat-developpeur-vehicule-na-lot-6-v2.md` (`24d37f857f1e77399c8015a00b5d0b0d2f422301f1c873c39a760806d1601730`).
3. La note de lancement (racine et dossiers) : `…/lancement-developpeurs-vehicule-na-lots-6-et-10-a-v1.md` (`08a6bac6…`) ; son en-tête « EN ATTENTE » est levé. Orchestrateur en lecture seule, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` : `/home/user/orchestrateur-a41b7b50/` ou `/home/user/lciric/ideation-organism`.
4. Le lot 6 v1 récupéré, incomplet, non vérifié : `…/lot-6-vehicule-na-v1-recupere-incomplet/` (lis son LISEZ-MOI) ; tu le reprends comme base, tu ne l'écrases pas.
5. Le lot 10 a vérifié « Conforme » : `…/lot-10-a-vehicule-na-v1/` (paquet et `verification-v1/verification-lot-10-a-na-v1.md`, remarque 1).
6. Le mot de la mère du 21 novembre à 18:15Z (GO-2026-11-21-69), relayé par la session : le lot 6 refuse aux états 1 et 2 tout contexte dont le journal n'est pas `JournalRequetesColonneNA` ; écart au mandat déclaré, qui renforce la garde.

## Ce que tu fais
1. Le paquet v2, sous des noms neufs : le lot 6 v1 récupéré, plus **le refus de câblage**. Au départ de la course et à la construction de chaque génération, le contexte d'appel est refusé si l'état de la colonne est 1 ou 2 et que son journal n'est pas `JournalRequetesColonneNA`. C'est un arrêt nommé, inscrit aux arrêts connus et au journal des arrêts et des générations ; son numéro est à l'additif. La course reçoit l'état de l'interrupteur et une fabrique de journal. Épreuves : état 1 avec le journal de la colonne, départ ; états 1 et 2 avec un journal ordinaire, refus qui nomme l'arrêt ; état 0 avec un journal ordinaire, départ. Une mutation qui retire ce refus doit être tuée.
2. Rejoue tout : application sur une copie neuve, sur les lots 2 v5 à 5 v1, 10 a et la v68 ; essais ; mutations du v1 et neuves.
3. Le **rapport** que le v1 n'a pas écrit : les exigences et les lieux du code (fichier et ligne), les formats pour les lots 7, 8 et 10 a, les écarts du v1 (LISEZ-MOI) et les tiens. Puis la table d'empreintes et un compagnon par fichier.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/dev-vehicule-na-lot-6-v2/` ; copie aux jalons vers `/home/user/dossiers-developpeurs-vehicule-na-v1/lot-6-v2/`. Commandes de liste permises : ton dossier, les dossiers des lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a, le lot 6 récupéré et les deux copies de l'orchestrateur. Pose `TMPDIR` dans ton dossier avant tout essai. Interdits : rien sous `docs/notes/ideation-nouvelles-attaques-v1/additif-matiere-premiere-v1/`, `archives-reponses-modeles/`, `/root/.claude/`, ni aucune branche `quarantaine/…` ou `matiere-premiere/…` ; aucune attache de dépôt ; aucun identifiant de modèle dans les pièces.

## Consigne commune de méthode de recherche (`docs/procedures/consigne-commune-methode-de-recherche-v1.md`, `d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`), partie 1 collée telle quelle

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

Tu es développeur : les rubriques « Mode d'échec affecté » et « Dérivation de l'énoncé seul » portent « Sans objet : » et leur motif. La rubrique « Objets de contrôle » n'est jamais sans objet pour toi : chaque garde et chaque arrêt a son cas sain et son artefact, nommés, avec ce que tu attendais et ce qui est rendu.
