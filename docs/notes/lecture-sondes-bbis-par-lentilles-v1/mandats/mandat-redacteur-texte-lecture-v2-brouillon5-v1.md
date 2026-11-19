# Mandat du rédacteur du brouillon 5 du texte de lecture v2 (sous-agent neuf sur Fable 5.2) — v1

- Écrit par la session des lentilles (`session_01XJ6Mgr9o68QqLiFTLg3zRW`, Opus 5.5), le 2026-11-19, sur le mot de Lazar « go reco »
  (note `docs/notes/neuron-lens-v1/mot-lazar-go-redacteur-brouillon5-2026-11-19-v1.md`). Classe C.

## Texte du mandat (donné mot pour mot au rédacteur)

Tu es le **rédacteur neuf du brouillon 5** du préenregistrement « lecture des sondes de l'étape B bis par lentilles, v2 » (classe A),
dans le dépôt `/home/user/controle-ia-travail`, branche `claude/brave-galileo-jhp684`. Tu es sur Fable (règle « Qui conçoit » de
`CLAUDE.md`). Règles : `CLAUDE.md` (R1 à R14). Français, sans acronyme nu, choses nommées en clair, identifiants en appui seulement.
Tu n'as écrit ni la v1, ni aucun brouillon de la v2, ni le critère, ni le devis, ni l'addendum, ni aucune contre-lecture ou
vérification ; tu ne seras ni développeur, ni opérateur, ni lecteur de ce texte.

### Pièces
- **Brouillon 4** (ta base) : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon4.md`
  (`fe46a9468b8b985a76d4e700a5bed82b3b970851335214216c8319e5f8084e4b`) et ses pièces de fabrication dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/` (`couples-brouillon3-vers-brouillon4-v1.py` et suivants).
- **Contre-lecture du brouillon 4** : `docs/notes/neuron-lens-v1/contre-lecture-texte-lecture-lentilles-v2-brouillon4-v1.md`
  (`08a698577a952669dd3cd75fa7d7bcb7447a5b1e795106b322bf0e377792c17b`), entière : verdict « scellable après corrections », quatre
  corrections bloquantes B1 à B4 (texte avant et après, lignes du brouillon 4), dix non bloquantes N1 à N10, nœuds.
- **Mots de Lazar et lignes de la session principale** (branche principale, `git show origin/main:…`) :
  - règle de départage, option (a) : note `docs/notes/neuron-lens-v1/mot-lazar-regle-departage-seconde-passe-2026-11-19-v1.md`
    (`e0ad5502…`) et ligne `GO-2026-11-19-92` de `registres/go.md` ;
  - garde d'égalité de la v1, option 3 : note `…/mot-lazar-garde-egalite-vingtieme-rang-2026-11-19-v1.md` (`dbd1e514…`),
    `GO-2026-11-19-78` ;
  - lectures de la session principale : `R-3994` (« go pour le brouillon 4 » consigné comme mot rapporté, non retrouvé à la source ;
    aucune ligne d'accord due) et `R-3995` (aucune ligne n'étend GO-2026-11-19-47 à la v2, et il n'en faut pas : GO-47 régit
    l'addendum d'écart au texte v1 scellé ; la v2 est un texte neuf, non scellé, qui porte la statistique corrigée par sa propre
    conception et cite GO-47 comme son origine) dans `registres/decisions.md` ;
  - départ de ce mandat : note `docs/notes/neuron-lens-v1/mot-lazar-go-redacteur-brouillon5-2026-11-19-v1.md`.
- Toutes les pièces que le brouillon 4 et la contre-lecture citent (critère v8 et v4, devis v9, programme de comparaison v4,
  addendum de concentration `7c738708…` et ses vérifications, rapport du bloc séparable `4e1fe2d7…`, contre-lecture 3, v1 scellée par
  programme) : lis ce dont une correction a besoin, et déclare-le. Le verdict de la tranche de nos lentilles (`3a9b947e…`) : lecture
  permise, **limitée aux lignes que la correction B2 exige** ; déclare ce que tu en as vu.

### Tâches (chacune donne une ligne de la table de traitement, en tête)
1. **B1 à B4** : applique chacune, selon le texte avant et après de la contre-lecture, ou mieux si tu le justifies. B3 ajoute
   l'écart E7 avec son champ de fiche, sa phrase de tête et son essai (R5 : cas sain et artefact). B4 fixe la règle la plus prudente
   (aucun remplacement d'une première passe arrêtée par une garde d'égalité scellée, aucune phrase de la lentille publique avant le
   nœud de la v1) : écris-la et dis, dans les nœuds, qu'elle est portée à Lazar pour information au scellement.
2. **N1 à N10** : applique chacune ou refuse-la avec sa raison, une ligne de table chacune.
3. **Marqueurs qui se remplissent** :
   - `MOT_DE_LAZAR_SUR_LA_REGLE_DE_DEPARTAGE` : remplace-le par la citation de la note `e0ad5502…` et de la ligne GO-2026-11-19-92 ;
     retire du texte les formes conditionnelles du nœud N18 (option (a) retenue), garde N18 comme nœud tranché, daté ;
   - `MOT_DE_LAZAR_GO_47_POUR_LA_V2` : remplace-le par la phrase de R-3995 et sa citation ; reprends le nœud N19 et la ligne 20 de la
     table des changements ;
   - la phrase du bloc de tête du brouillon 4 sur le mot « go pour le brouillon 4 » : écris qu'il est consigné comme mot rapporté
     (R-3994).
   Vérifie chaque ligne citée sur `origin/main` (tu peux lancer `git fetch origin main`, aucune autre branche). Les autres marqueurs
   restent ; mets la table des marqueurs à jour (qui porte, qui reste).
4. **N12 et N17** (nœuds ouverts, défauts vers le 21 novembre) : laisse-les ouverts ; écris le texte sous forme conditionnelle pour
   chaque option, et pour le défaut de N17 au deuxième palier (option (b)), dis ce qu'il demanderait (addendum écrit après le verdict).
   Ne tranche aucun nœud.
5. **Table « Changements de la v1 à la v2 »** et bloc « Changements du brouillon 4 au brouillon 5 » : une ligne par changement neuf.
6. **Contrôle par programme des lignes de la v1** (programme de l'annexe B de la contre-lecture 3, rejoué) : donne le compte et
   corrige-le dans le texte s'il change.

### Forme
- Base : le brouillon 4, archivé sans changement (R12). En tête, un bloc « Brouillon 5 — différences avec le brouillon 4 », puis la
  table de traitement (faite, ou refusée avec sa raison).
- **Fabrication par programme**, comme le brouillon 4 : script de couples (chaque « avant » trouvé une fois et une seule dans le
  brouillon 4), sa sortie, un `diff` contre le brouillon 4 ; noms neufs dans `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`
  (`couples-brouillon4-vers-brouillon5-v1.py`, `sortie-couples-brouillon4-vers-brouillon5-v1.txt`,
  `diff-brouillon4-vers-brouillon5-v1.txt`), scellés.
- Le reste du texte, déclarations d'auteur, dates et pieds des brouillons 1 à 4 compris, n'est pas réécrit, sauf ce qu'une
  correction exige ; écris-le dans le bloc de tête lieu par lieu.
- Lance le validateur (`src/controle_ia/prereg.py`, fonction `problemes`, qui prend un chemin) et donne son résultat exact ; les
  marqueurs restants sont attendus : liste-les.
- Travaille d'abord dans ton bloc-notes (la session des lentilles te donne son chemin), puis copie dans
  `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon5.md` et scelle-le comme brouillon :
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
- P3, P3-bis, T0.6, T0.7 hors ce texte, l'étape B, le bras d'attaque, le saboteur à budget.

**Refus d'outil** : tout refus d'une permission ou d'un classifieur n'est ni rejoué, ni reformulé, ni contourné. Tu le déclares.

### Rends-moi
- le chemin et l'empreinte du brouillon 5, et ceux des pièces de fabrication ;
- la table de traitement (B1 à B4, N1 à N10, marqueurs, N12 et N17, contrôle de la v1), une ligne chacune ;
- les marqueurs restants et qui les porte ;
- les nœuds pour Lazar et tout choix au-delà de la lettre du mandat ;
- les pièces lues, les expositions et les refus éventuels ;
- la confirmation que tu n'as rien ouvert d'interdit.

---

## Après le brouillon 5 (pour mémoire, hors mandat)
- Vérification des corrections par le contre-lecteur du brouillon 4 (Opus 5.5) ; vérification du seul couple de la couche 15 par le
  lecteur désigné (Opus 4.6), décidée par la session principale (R-3995).
- Scellement par la session principale.
