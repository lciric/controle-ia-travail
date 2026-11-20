# Mandat du rédacteur du brouillon 6 du texte de lecture v2 (sous-agent neuf sur Fable 5.2) — v1

- Écrit par la session des lentilles (`session_01XJ6Mgr9o68QqLiFTLg3zRW`, Opus 5.5), le 2026-11-20, sur le mot de Lazar « go reco »
  (note `docs/notes/neuron-lens-v1/mot-lazar-noeuds-n12-n17-et-brouillon6-2026-11-20-v1.md`, `cd02b0fb…`). Classe C.

## Texte du mandat (donné mot pour mot au rédacteur)

Tu es le **rédacteur neuf du brouillon 6** du préenregistrement « lecture des sondes de l'étape B bis par lentilles, v2 » (classe A),
dans le dépôt `/home/user/controle-ia-travail`, branche `claude/brave-galileo-jhp684`. Tu es sur Fable (règle « Qui conçoit » de
`CLAUDE.md`). Règles : `CLAUDE.md` (R1 à R14). Français, sans acronyme nu, choses nommées en clair, identifiants en appui seulement.
Tu n'as écrit ni la v1, ni aucun brouillon de la v2, ni le critère, ni le devis, ni l'addendum, ni aucune contre-lecture ou
vérification ; tu ne seras ni développeur, ni opérateur, ni lecteur de ce texte.

### Pièces
- **Brouillon 5** (ta base) : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon5.md`
  (`88a2011a8b9e02ba9f6f2933ee4ec01ee6f156abf44ccf19960d9b7de3d75003`) et ses pièces de fabrication dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/` (`couples-brouillon4-vers-brouillon5-v1.py` et suivants).
- **Vérification des corrections du brouillon 5** :
  `docs/notes/neuron-lens-v1/verification-corrections-texte-lecture-lentilles-v2-brouillon5-v1.md`
  (`04282064d10c6cdd2a4266bf9e5a526c9835463476108dec8a54dfcae2f64328`), entière : verdict « scellable après corrections », une
  correction bloquante C1 et six non bloquantes M1 à M6 (texte avant et après, lignes du brouillon 5).
- **Contre-lecture du brouillon 4** : `docs/notes/neuron-lens-v1/contre-lecture-texte-lecture-lentilles-v2-brouillon4-v1.md`
  (`08a69857…`), si une correction y renvoie.
- **Mot de Lazar sur N12 et N17** : `docs/notes/neuron-lens-v1/mot-lazar-noeuds-n12-n17-et-brouillon6-2026-11-20-v1.md`
  (`cd02b0fb85e06b0366d731bb9888d753562c8d76cbef403874587975da9c99ed`), entier : **N12, option (a)** ; **N17, option (a) aux deux
  paliers**. Une ligne d'accord de la session principale peut exister sur `origin/main` (`registres/go.md`) quand tu écris :
  cherche-la (`git fetch origin main`, aucune autre branche) ; si tu la trouves, cite-la ; sinon, marqueur
  `LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17` (porté par la session principale).
- Toute pièce que le brouillon 5 ou la vérification citent : lis ce dont une correction a besoin, et déclare-le. Le verdict de la
  tranche de nos lentilles (`3a9b947e…`) : aucune lecture nouvelle n'est demandée ; si une correction l'exige, limite-toi aux lignes
  qu'elle cite et déclare-les.

### Tâches (chacune donne une ligne de la table de traitement, en tête)
1. **N12 et N17 tranchés.** Écris-les comme tranchés, datés, avec la citation du mot (note `cd02b0fb…`) et de la ligne d'accord ou
   du marqueur. Retire les formes conditionnelles de leurs options écartées partout où elles paraissent (« Entrées », condition de
   lecture, puce « par gabarit », plan, critères, liste d'arrêt, essais, nœuds, table des changements, description de la ligne
   `GO-LENTILLES-BBIS-V2`). N12 (a) : la lecture d'une lentille au deuxième palier en ajustement seul ou en seconde course
   incomplète attend la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS`, postérieure à l'avertissement ; ce mot ouvre ou non
   la lecture, il ne choisit aucune branche : écris-le. N17 (a) aux deux paliers : aucun addendum de recopie ; la clé
   `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2` et tout ce qui en dépend sont retirés, ou dits sans objet, avec leurs lieux.
2. **C1** : applique-la dans ce qui reste après la tâche 1. L'issue des deux nœuds est désormais fixée avant le scellement par le
   mot de Lazar : dis-le ; garde l'arrêt nommé si une pièce de `GO-LENTILLES-BBIS-V2` portait une autre issue, ou une ligne datée
   après le scellement de la v2 ; essai, cas sain et artefact (R5). Si la vérification demande plus, fais-le ou refuse avec la raison.
3. **M1 à M6** : applique chacune ou refuse-la avec sa raison, une ligne de table chacune. Pour M6 (le mot « go reco » qui a lancé
   le rédacteur du brouillon 5) : cite la ligne de la session principale si elle existe sur `origin/main`, sinon la note
   `docs/notes/neuron-lens-v1/mot-lazar-go-redacteur-brouillon5-2026-11-19-v1.md` (`f28f18ae…`) seule, et dis-le. Pour M1 : les
   couples de la couche 15 à donner au lecteur désigné sont ceux du brouillon 5, L16 à L19, et L12 et L15 pour information.
4. **Table « Changements de la v1 à la v2 »** et bloc « Changements du brouillon 5 au brouillon 6 » : une ligne par changement neuf.
5. **Contrôle par programme des lignes de la v1** (programme de l'annexe B de la contre-lecture 3, rejoué) : donne le compte et
   corrige-le dans le texte s'il change.
6. **Bloc séparable** : aucune valeur chiffrée ne bouge ; bornes uniques et intactes ; si une tâche touche le bloc, dis quels couples
   iraient au lecteur désigné.

### Forme
- Base : le brouillon 5, archivé sans changement (R12). En tête, un bloc « Brouillon 6 — différences avec le brouillon 5 », puis la
  table de traitement (faite, ou refusée avec sa raison).
- **Fabrication par programme**, comme les brouillons 4 et 5 : script de couples (chaque « avant » trouvé une fois et une seule dans
  le brouillon 5), sa sortie, un `diff` contre le brouillon 5 ; noms neufs dans `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`
  (`couples-brouillon5-vers-brouillon6-v1.py`, `sortie-couples-brouillon5-vers-brouillon6-v1.txt`,
  `diff-brouillon5-vers-brouillon6-v1.txt`), scellés.
- Le reste du texte, déclarations d'auteur, dates et pieds des brouillons 1 à 5 compris, n'est pas réécrit, sauf ce qu'une
  correction exige ; écris-le dans le bloc de tête lieu par lieu.
- Lance le validateur (`src/controle_ia/prereg.py`, fonction `problemes`, qui prend un chemin) et donne son résultat exact ; les
  marqueurs restants sont attendus : liste-les.
- Travaille d'abord dans ton bloc-notes (la session des lentilles te donne son chemin), puis copie dans
  `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon6.md` et scelle-le comme brouillon :
  `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <chemin>`.
- En tête : l'auteur (toi, modèle Fable 5.2, sous-agent de la session des lentilles `session_01XJ6Mgr9o68QqLiFTLg3zRW`), les heures
  `date -u`, les pièces lues, les expositions.
- Aucun commit, aucun push, aucune machine, aucune dépense, aucun modèle chargé. Ne modifie aucun fichier existant.

### Cloisonnement — tu ne lis JAMAIS
- la liste « Jamais ouverts » de la v1 ;
- toute sortie, tout score, toute table, toute lecture ou tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y
  compris son verdict ;
- toute table ou sortie de la lecture par la lentille publique ;
- les branches `donnees/*` et `calcul/*` ;
- tout `diag/` ou `runs/`, sauf les noms de clés et la structure de `diag/20261118-164930-neuron-lens-b-beta/b-beta-export.json` et
  `b-beta-ajustement-R.json` si tu en as besoin ;
- `docs/verdicts/`, tout fichier « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/` ;
- P3, P3-bis, T0.6, T0.7 hors ce texte, l'étape B, le bras d'attaque, le saboteur à budget ; dans les registres de la branche
  principale, ne lis que les lignes que tu cherches par leur identifiant.

**Refus d'outil** : tout refus d'une permission ou d'un classifieur n'est ni rejoué, ni reformulé, ni contourné. Tu le déclares.

### Rends-moi
- le chemin et l'empreinte du brouillon 6, et ceux des pièces de fabrication ;
- la table de traitement (N12 et N17, C1, M1 à M6, changements, contrôle de la v1, bloc séparable), une ligne chacune ;
- les marqueurs restants et qui les porte ;
- les nœuds pour Lazar et tout choix au-delà de la lettre du mandat ;
- les pièces lues, les expositions et les refus éventuels ;
- la confirmation que tu n'as rien ouvert d'interdit.

---

## Après le brouillon 6 (pour mémoire, hors mandat)
- Vérification des corrections par le contre-lecteur des brouillons 4 et 5 (Opus 5.5) ; couche 15 par le lecteur désigné (Opus 4.6).
- Scellement par la session principale.
