# Règles communes aux quatre sous-agents de la lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Écrites par la session conductrice `session_013QMayjNC5GKdDFTN87oAV5` le 2026-11-18, sous le mandat `registres/t07-etape-b-bis/mandat-session-lecture-bbis-v1.md` (empreinte `ab14f2f07cd14d85205554c66e00e930b51156152408ef6943f26ec0fe5765bf`). Chaque mandat de sous-agent renvoie à ce fichier ; il vaut pour tous.

## Dépôt, branche, langue
- Dépôt : `/home/user/controle-ia-travail`, branche de travail `claude/lecture-verdict-etape-b-bis-v1`. `PYTHONPATH=src`. Tu ne commites pas, tu ne pousses pas, tu ne changes pas de branche dans cet arbre : la conductrice le fait. Un arbre de travail séparé (`git worktree add`) ou un clone local dans un dossier temporaire est permis quand ton mandat le demande.
- Langue : français. Nomme chaque chose par ce qu'elle est et ce qu'elle fait ; un identifiant ne vient qu'en appui, après le nom en clair.

## Ce qui fait foi
- Le texte scellé `prereg/T0.7-etape-B-bis-v1.md` et ses trois addenda d'écart (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `-ecart-2-v1.md`, `-ecart-3-v1.md`), inscrits par les lignes `ADDENDUM-ECART-1-BBIS`, `-2-BBIS`, `-3-BBIS` de `registres/t07-etape-b-bis-v1-addenda-v1.md`. Les addenda remplacent le texte là où ils le disent.
- Le feu de la course `registres/t07-etape-b-bis/feu-bbis-v7.txt`, § 12 « Après la course » et § 13 « Réserves ».
- Le registre propre `registres/t07-etape-b-bis-v1.md` ; le code inscrit par sa ligne `CODE-BBIS` la plus récente (fiche `registres/t07-etape-b-bis/code-bbis-v2.json`).
- Les sorties de la course : branche `donnees/t07-etape-b-bis-v2`, tête `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9` ; ligne `SCORES-BBIS` : `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json`, empreinte `645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62`.

## Cloisonnement — fichiers que tu n'ouvres jamais
- Le verdict de l'étape B de T0.7 et son fichier de lecture (`lecture-t07.json`, `arret-etape-b.json`, tout fichier de `docs/verdicts/` qui parle de l'étape B, de T0.7 étape A ou B, de 7a, de 7b, de T0.6 ou de l'épreuve du signal planté). Leur **présence** et leur **commit d'ajout** se relèvent par les noms seulement (`git ls-tree`, `git log --diff-filter=A --format=… -- chemin`), jamais par le contenu.
- Tout résultat de 7a, de 7b, de T0.6 ou de l'épreuve du signal planté (P3-bis) au-delà des clés et des fichiers que le texte scellé nomme comme entrées (plan d'analyse, point 1), et seulement par la chaîne de lecture, jamais à l'œil.
- La liste « Jamais » du plan d'analyse, point 1.
- Tout sujet et tout mécanisme de saboteur discret : `prereg/T0.7-organismes-discrets-*`, `docs/notes/organismes-discrets-v1/`, `docs/notes/barreau8-iib-v1/`, `brouillons/ii-b-saboteur-budget-v1/`.
- Le texte `prereg/lecture-sondes-bbis-par-lentilles-v1.md` et tout ce qui touche à la lecture par la lentille publique : hors mandat.
- `registres/etat.md`, `registres/decisions.md`, `registres/passations/` : ils peuvent porter des résultats d'autres chaînes ; tu ne les ouvres pas. Si une recherche (`grep`) doit y passer, borne-la aux lignes dont tu as besoin et ne lis rien d'autre.
- Pas de `grep -r` ni de lecture large sur `diag/`, `donnees/`, `docs/verdicts/`, `runs/`.

## Règles
- Aucune dépense, aucune machine louée, aucun appel à un service extérieur. Processeur seulement.
- Arrêt d'un processus par son PID relevé au lancement, jamais par motif de ligne de commande (un crochet du dépôt le refuse).
- Dossiers temporaires sous `/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/` ; pour les essais, `--basetemp` dans ce dossier, supprimé après.
- Au premier refus du classifieur, d'une permission ou du crochet du dépôt : **arrêt**, sans reformuler, découper ni contourner ; tu rends le texte exact du refus.
- Aucune analyse non prévue par le texte scellé. Aucun repli silencieux (R5). Fichier qui semble absent : vérifié sur disque et par empreinte avant de le dire absent (R11). On n'écrase jamais : nouvelle version = nouveau nom (R12). Tout fichier que tu déposes reçoit son compagnon : `python -m controle_ia.scellement sceller FICHIER`.
- **Ce que tu rends à la conductrice** : noms, chemins, empreintes, états (« fait », « refusé », « arrêt »), textes exacts des refus. **Jamais** un chiffre de mesure, une aire, un score, un état de cellule, une issue, une phrase du verdict. La conductrice ne doit rien savoir du résultat.
- À la fin, écris dans ton rendu la liste exacte des fichiers de résultat que tu as ouverts (chemin, et « par la chaîne » ou « à l'œil »), pour la liste « qui a lu quoi ».
