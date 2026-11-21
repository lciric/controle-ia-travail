VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`. AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ; OUVRE CHAQUE PIÈCE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du concepteur — corrections de l'additif « matière première » (v1 vers v2) après contre-lecture — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21. L'auteur de la v1 (modèle F) ne peut plus être joint (redémarrage de la machine) ; tu es un concepteur neuf de la même lignée (modèle F), effort élevé, et tu portes les corrections. Ensuite : vérification des corrections par un contre-lecteur d'un autre modèle, scellement par la mère. **Aucun appel, aucune dépense, aucun commit.**

## Ce que tu lis (liste explicite)

1. Le mandat d'origine, qui fixe ce que la pièce doit faire et ce qui fait foi : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/mandat-concepteur-additif-matiere-premiere-v1.md` (lis aussi les sources qu'il nomme, aux mêmes conditions).
2. Les pièces v1, dossier `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/additif-matiere-premiere-v1/` : `additif-matiere-premiere-preenregistrement-court-v9-v1.md`, `devis-lecture-de-fin-matiere-premiere-v1.md`, `calcul_devis_lecture_de_fin_matiere_premiere_v1.py`, `entrees-devis-lecture-de-fin-matiere-premiere-v1.json`, `calcul-devis-lecture-de-fin-matiere-premiere-v1.json`, `liste-nominative-lecture-de-fin-matiere-premiere-v1.md`, `texte-servi-aux-deux-juges-lecture-de-fin-v1.txt`, `rapport-concepteur-additif-matiere-premiere-v1.md`.
3. Les deux relectures, dossier `…/additif-matiere-premiere-v1/contre-lecture-v1/` : `contre-lecture-additif-matiere-premiere-v1.md` (À corriger, treize corrections) et `relecture-fuite-additif-matiere-premiere-v1.md` (fuite de la vérité : cassé, § 4 point 1), avec `entrees-objet-faux.json`.

**N'ouvre ni le registre servi réel, ni aucune branche `quarantaine/…` ou `matiere-premiere/…`, ni rien sous `archives-reponses-modeles/`.**

## Ce que tu écris

Dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/concepteur-corrections-additif-matiere-premiere/` :
1. Les pièces en v2, noms neufs (R12 : on n'écrase rien) : additif, devis et son programme (joué deux fois, `cmp` muet), entrées et sortie du calcul, liste nominative, texte servi aux deux juges — seulement celles qui changent ; celles qui ne changent pas restent en v1 et sont dites telles.
2. Une **table des corrections** : pour chaque correction des deux relectures (numéro, relecture), portée telle quelle, portée autrement (pourquoi), ou refusée (pourquoi, pièce à l'appui).
3. **Points délicats séparés, jamais tranchés dans le texte** : tout ce qui serait un écart à un texte scellé sur `main` (par exemple : le nombre d'espèces de la course scellée, des clés de tirage neuves, une lecture de la branche par un programme avant l'état 2) est écrit dans une section « Points délicats pour la mère » au format de décision (décision en une phrase, enjeu, options, recommandation et confiance) ; le texte v2 prend l'option qui **ne s'écarte pas** du scellé, ou laisse le point ouvert et le dit.
4. Un rapport court, les différentiels v1 vers v2, une table d'empreintes, un compagnon `.sha256` par fichier (`sha256sum` lancé depuis le dossier).

## Interdits

Jamais de heredoc ni de code en ligne passé à un interpréteur. Rien sous `/root/.claude/`. Aucun identifiant de modèle (les rôles se disent par lignée ou relais). Aucune recette. Aucun commit. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

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
