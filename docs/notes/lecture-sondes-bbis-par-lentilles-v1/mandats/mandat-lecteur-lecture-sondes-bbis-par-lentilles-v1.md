# Mandat du lecteur neuf — ouverture et lecture humaine des tables de la lecture des directions des sondes de l'étape B bis par la lentille publique (point 8) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, à la demande de la mère (message de 20:20Z), sous
les mots de Lazar « turbo max » et « go tu as mon mot pour tout » (GO-2026-11-21-63). Pièce de travail (classe C). Vaut pour la session
neuve que la mère ouvre pour toi. Français. **L'auteur de ce mandat n'a lu et ne lira aucune table.**

## Qui tu es
Le **lecteur neuf** du texte scellé `prereg/lecture-sondes-bbis-par-lentilles-v1.md`
(`ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`) et de son addendum de concentration scellé
(`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`), section « Qui, quelle machine, quel coût » :
- tu n'as lu aucun résultat de l'apprentissage des sondes sur la tâche (score, aire, issue, verdict), ni des autres chaînes interdites ;
- tu n'es ni l'auteur, ni le développeur, ni l'opérateur de ce texte, ni le lecteur d'aucun verdict qu'il nomme ;
- tu lis ce texte, les tables fermées et la ligne du verdict d'ensemble de la tranche des lentilles publiques ; tu décris selon les
  « Critères de lecture gelés », **et rien d'autre**. Si une seule de ces conditions ne tient pas pour toi : arrêt, message à la mère.

## Ta machine
Le processeur du conteneur de ta session neuve. Aucune machine louée, aucune carte graphique, 0 USD. Aucun calcul neuf : tu ne relances
ni le montage ni le calcul (le texte : « sans nouveau calcul »). La seule commande du lanceur permise est `phrases` (elle relit les
tables fermées et écrit les phrases mécaniques ; elle ne calcule rien).

## Ce que tu lis (autorisé), dans l'ordre
1. `CLAUDE.md` (R1 à R14, interdits).
2. Le texte scellé v1 **en entier** (vérifie son empreinte) et son addendum de concentration scellé (vérifie son empreinte ; la ligne
   `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` du registre propre la donne). Tu les appliques à la lettre ; en cas d'écart entre eux,
   l'addendum prime sur ce qu'il modifie.
3. Le registre propre `registres/lecture-sondes-bbis-par-lentilles-v1.md` (branche principale), en entier ; dans
   `registres/t07-etape-b-bis-v1.md`, **la seule présence de `VERDICT-BBIS`** (clé et heure), jamais le fichier du verdict.
4. La passation de l'opérateur `docs/notes/lecture-sondes-bbis-par-lentilles-v1/operation/passation-operateur-2026-11-21-2015-v1.md`
   (sur la branche que la mère te nomme) : chemins des morceaux versés, manière de les rassembler, empreintes.
5. Les sorties versées de la course `20261121-193607-lentilles-bbis-v1` sur la branche `calcul/lentilles-sondes-bbis-v1`, récupérée
   **en la nommant**, et elle seule de cette famille. Tu en vérifies chaque morceau contre son compagnon `.sha256`, et le fichier des
   tables contre la ligne `TABLES-LENTILLES-BBIS`, **avant** toute ouverture.
6. La ligne du verdict d'ensemble de la tranche des lentilles publiques :
   `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` (branche principale), empreinte attendue
   `ca06acb1550ccc76fef1ec89ae0aec170c5f05252bda2711f131eaa0e645fc1d` ; empreinte différente : « ligne non recopiée : empreinte ».

## Ce que tu ne lis jamais
La liste « Jamais ouverts » du texte (les fichiers qu'elle nomme, jamais ouverts par personne de cette chaîne) ; `diag/`, `runs/` et
`docs/verdicts/` hors des chemins nommés ci-dessus ; les branches `donnees/*` et `verdict/*` ; aucune autre branche `calcul/*` ; les
fichiers « consigne-privee » ou « conception-ii-b » ; rien de P3, P3-bis, T0.6 ni de l'étape B ; le fichier d'arrêt de toute course
arrêtée (`arret.json`). Tout intitulé interdit vu par mégarde : arrêt, déclaration écrite, message à la mère.

## Ce que tu fais, dans l'ordre (plan d'analyse, points 1 (g) et 8)
1. **Préalables** au registre propre : `SCELLEMENT-`, `ABSENCE-VERDICT-`, `ADDENDUM-CONCENTRATION-`, `GO-`, `CODE-` (dernière ligne :
   fiche v3), `MONTAGE-`, `ENTREES-` et `TABLES-LENTILLES-BBIS` présentes ; la dernière `CODE-` après `ADDENDUM-CONCENTRATION-` ;
   `MONTAGE-`, `ENTREES-` puis `TABLES-` après la dernière `CODE-`, dans cet ordre (les lignes des premières clés se suivent dans
   l'ordre de leur inscription, `ABSENCE-VERDICT-` avant `SCELLEMENT-` comprise : ce n'est pas un écart) ; `VERDICT-BBIS` présente au
   registre de l'apprentissage des sondes sur la tâche. Sinon rien ne s'ouvre ; message à la mère.
2. **Empreintes** de tous les morceaux et du fichier des tables rassemblé, contre les compagnons et la ligne `TABLES-`.
3. **Proposer à la mère la ligne `OUVERTURE-LENTILLES-BBIS`** (heure `date -u`, chemin et empreinte du fichier des tables), et
   **attendre qu'elle l'inscrive** avant d'ouvrir quoi que ce soit. Tu n'inscris aucune ligne toi-même.
4. **Phrases mécaniques** : `PYTHONPATH=src python -m controle_ia.lentilles_sondes_bbis.lanceur_v9 phrases --tables <tables> --sortie <dossier-de-lecture>/phrases-code-lentilles-bbis-v1.json`
   (sortie neuve, jamais dans les dossiers versés). Note son empreinte.
5. **Lecture** : ouvre les tables ; applique les « Critères de lecture gelés » (phrase de tête toujours écrite, ligne du verdict
   d'ensemble recopiée telle quelle, phrases gelées par direction, signe et lentille, familles, pôles, comparaisons, « Non lue :
   [motif] », règles ; issue de l'audit de symétrie telle que les tables la portent, en réserve si déclenché). Toute phrase au-delà des
   phrases gelées est marquée « description libre, après lecture, non préenregistrée ». Aucune phrase sur la détection du sabotage.
6. **Comparaison** de chacune de tes phrases à celle que le code rend : table « direction → ta phrase → phrase du code → égales ou
   non ». Tout désaccord est listé ; tu ne le tranches pas : **un second lecteur neuf** le tranche, sans nouveau calcul ; tu le
   signales à la mère.
7. **Écrire et sceller** `docs/notes/lecture-sondes-bbis-par-lentilles-v1/lecture/lecture-lentilles-bbis-v1.md` (la description), la
   table de comparaison `lecture/comparaison-phrases-lecteur-code-v1.md` et les phrases du code ; pousser sur la branche que la mère te
   nomme à l'ouverture (jamais `main`, jamais `lciric/controle-ia`) ; **proposer à la mère la ligne `LECTURE-LENTILLES-BBIS`** (chemin et
   empreinte de la description).
8. **Rendre à la mère** : état (lu, désaccords ou non), chemins et empreintes, lignes proposées. Le contenu de la lecture ne va qu'à la
   mère et à Lazar ; **rien à la session des lentilles**, qui a coordonné le code et n'en lit rien.

## Commits
Aucun identifiant ni nom de modèle dans les messages ; chaque message finit par `Co-Authored-By: Claude <noreply@anthropic.com>` et
la ligne `Claude-Session:` de ta session. Fetch et pull en nommant la branche ; jamais de poussée forcée.

## Arrêts
La « Liste d'arrêt » du texte scellé, entière. Tout refus d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni
contourné ; arrêt et message à la mère. Empreinte différente : arrêt, rien ne s'ouvre. Avant de t'arrêter : passation scellée dans
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/lecture/`, poussée.
