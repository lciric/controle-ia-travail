# Rapport : fiche de réception v4 de R1 et son vérificateur — v1

- Rédacteur-développeur neuf (sous-agent, Claude Opus 5.5), pour conv-audit ; consigne
  `docs/notes/runs-r1-r2-r4-v1/consigne-fiche-reception-r1-v4-v1.md` (compagnon vérifié conforme au début). Commencé le
  4 novembre 2026 à 23:28 UTC (`date -u`) ; conteneur redémarré vers 23:45 UTC (fichiers retrouvés sur disque, rien
  refait). Je n'ai écrit ni l'addendum v4, ni son code, ni les fiches précédentes.
- Seul réseau : `git fetch origin refs/heads/prep/r1-relance-v4:refs/remotes/origin/prep/r1-relance-v4` (937f1317 →
  5bd62a00 ; l'arbre `/home/claude/wt/r1-v4` était resté à 937f1317). Aucun commit, aucun `.sha256`, aucun fichier
  existant modifié, aucune sortie de la session 2 ni contenu du témoin lu (noms et empreintes seulement), rien sous
  `donnees/` ni `/home/claude/coffre-*`, aucun modèle, aucune dépense.

## 1. Fichiers produits (dossier `docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/`)

@@EMPREINTES@@

## 2. Ce que fait le vérificateur

`verifier_reception_r1_v4_v1.py verifier` rejoue, sur une copie récupérée (arbre du commit de versement, dépôt qui porte
ce commit, la branche source et 5bd62a00), toutes les attentes de la fiche, dans l'ordre de sa section 8 ; il lit les
JSON par clés nommées (filtre `filtrer` pour le rejeu, `extraire_reparation` pour la réparation, quatre clés du témoin),
les `.npz` par leurs seuls en-têtes `.npy` (`zipfile` + `ast.literal_eval` de l'en-tête ; aucun tableau chargé), et ne
compare les grandeurs de couverture qu'entre pièces, sans les afficher. Codes : 0 conforme, 2 arrêt nommé, 3 course
arrêtée (réception de l'arrêt seulement). `bloc` imprime le bloc d'attendus ; la fiche le porte à l'identique (essai
`test_bloc_de_la_fiche_reelle_egal_au_script`) et le mode réel refuse tout autre bloc.

## 3. Essais

@@ESSAIS@@

## 4. Banc de mutations

@@BANC@@

## 5. Dix points pour un contre-lecteur neuf

1. **Commits lancés supposés, non vérifiés par moi.** Le vérificateur exige `commit` = `937f1317…` au manifeste du témoin
   et `5bd62a00…` à celui de la réparation (addendum, « Coût et GO » : commit de scellement pour la session 1, commit du
   versement du témoin pour la session 2). Je n'ai pas lu le manifeste du témoin ni la commande de création de la
   session 2 (le registre des dépenses ne cite pas `COMMIT`). Si la session 2 a été lancée sur un autre commit, la
   réception s'arrête (`reparation`) : nœud, fiche nouvelle. À recouper par session-depot avant le scellement.
2. **Commit lancé du rejeu.** Il n'est pas connu d'avance : le script d'instance committe la réparation puis la table
   avant le rejeu, donc `commit` du manifeste du rejeu est un commit de la branche source. La fiche exige qu'il descende
   de 5bd62a00 et n'en diffère que par les 184 chemins de la réparation et de la table, blobs égaux aux versés. Cela
   suppose que l'étape « chaine » ne committe rien (vrai au code : `git commit … || true` sans changement) ; vérifier
   que rien d'autre (fichier non ignoré créé par les essais ou le préchargement) ne s'ajoute à `runs`, `diag`, `prereg`.
3. **Ordre « contrôles avant versement ».** Pour tenir l'ordre de la consigne avec un vérificateur qui lit un commit,
   la fiche fait préparer le commit de versement **localement, non poussé** (étape B), le fait vérifier (C), puis
   pousser tel quel (D) ; conv-audit rejoue le même vérificateur sur la ref récupérée (E). Écart de forme avec la v3
   (versement puis réception) à juger : il est plus strict, mais demande à session-depot de ne pas pousser avant C.
4. **Lecture de couverture par le vérificateur.** Il lit `empreinte_retrouvee` de la réparation, les méthodes de la
   table v4 et, du rejeu, `episodes_non_retrouves_v4`, `actions_non_retrouvees_v4`, `corrections_*`,
   `par_methode_resolution`, `methodes_resolution`, `empreintes_p3.trajectoires_identiques` — pour les comparer entre
   pièces, jamais pour les afficher. Ce sont des propriétés de l'instrument (V4-E2), non des scores, mais la couverture
   par condition entre dans un critère gelé (« sous 0,80 ») : juger si ces comparaisons muettes sont admises avant R13.
   `fidelite_toutes.conformes_longueur` et `contextes_conformes`, fixés en v3, ne le sont plus et ne sont pas lus.
5. **Identité des `.npz`.** Le type des quatre tableaux d'identité n'est pas écrit au parent ; la fiche l'exige égal à
   celui de `scores-p3.npz` (en-têtes seulement, empreinte `968414fc…` vérifiée). L'égalité des valeurs reste aux
   lecteurs des analyses (comme en v3). Les autres types (`<i8`, `|b1`, `<f8`, `<f2`) viennent du code de
   `rejeu_activations_v4` (écriture des `.npz`), non du texte du parent : à recouper.
6. **Chemins versés.** 198 chemins exactement, dont 89 épisodes consignés (`000` à `088`) : suppose que chaque cible est
   consignée une fois (vrai au code : `consigner` par cible dans l'étape « reparation », compteur continu). La table v4
   est versée à `prereg/R1-table-tokenisation-v4.json` sur `calcul/r1-r2-reel-v1` (chemin que cite la configuration v6
   et la commande de recalcul) ; les traces ne se versent pas.
7. **Recalcul de réception.** La fiche donne la commande exacte et l'arbre (`git worktree` à 5bd62a00 plus les trois
   pièces versées et les pièces de P3). Je ne l'ai pas jouée (tokeniseur et pièces de P3 sous `donnees/`, interdits
   ici) ; le vérificateur ne lit que sa sortie JSON et l'arbre `src/` (égal à 5bd62a00, `__pycache__` et `*.egg-info`
   exclus). Sa durée sur processeur n'est pas mesurée ; la commande porte `timeout 900`, à relever si elle ne suffit pas.
8. **Courses arrêtées.** Code 3 pour `arret.json` de la réparation, rejeu absent, ou `arret.json` du rejeu (motif fermé
   « non conforme » / « echec ») ; le vérificateur ne lit rien d'autre de l'arrêt. Le cas « table-v4 ou chaîne arrêtée »
   n'a pas de pièce propre (le script n'écrit pas d'`arret.json` pour ces étapes) : il se reçoit par l'absence du rejeu,
   sans plus de contrôle de la table. À juger si cela suffit pour le nœud.
9. **Ce que le vérificateur ne refait pas.** Il ne revérifie pas les corrections par l'empreinte de P3 (le recalcul et
   le rejeu le font), ni la configuration au-delà de l'égalité au fichier scellé, ni la reprise V4-E16 au-delà du nom
   de la branche source (`-v1` ou `-v2`) : la déclaration de reprise reste à vérifier par la session.
10. **Robustesse de l'outil.** Bibliothèque standard ; `git` en lecture seule ; arrêts nommés au premier écart ; toute
    exception de lecture rend le code 2 (garde `lecture`) ; aucun repli silencieux. Limites : le banc mute les gardes
    (toutes les occurrences), pas les fonctions d'aide (`chemins_attendus`, `entete_npy`, `blob_fichier`), couvertes
    seulement par le cas sain et les artefacts qui en dépendent ; les essais sont jouets (6 épisodes, T = 2), sauf la
    garde `textes`, jouée sur les vraies pièces de 5bd62a00.
