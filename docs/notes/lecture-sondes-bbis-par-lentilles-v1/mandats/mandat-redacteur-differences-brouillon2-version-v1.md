# Mandat du rédacteur de la pièce des changements du brouillon 2 à la version du texte de lecture v2 (sous-agent neuf sur Fable 5.2) — v1

- Écrit par la session des lentilles (`session_01XJ6Mgr9o68QqLiFTLg3zRW`), le 2026-11-20, sur le mot de Lazar « a » (note
  `docs/notes/neuron-lens-v1/mot-lazar-redacteur-differences-brouillon2-version-2026-11-20-v1.md`). Classe C.

## Texte du mandat (donné mot pour mot au rédacteur)

Tu es le **rédacteur neuf de la pièce des changements du brouillon 2 à la version** du préenregistrement « lecture des sondes de
l'étape B bis par lentilles, v2 » (classe A), dans le dépôt `/home/user/controle-ia-travail`, branche `claude/brave-galileo-jhp684`.
Tu es sur Fable (règle « Qui conçoit » de `CLAUDE.md`). Règles : `CLAUDE.md` (R1 à R14). Français, sans acronyme nu. Tu n'as écrit
ni la v1, ni aucun brouillon de la v2, ni aucune contre-lecture ou vérification.

### Objet
Le texte exige, avant son scellement, à la place du marqueur `DIFFERENCES_DU_BROUILLON_2_A_LA_VERSION` (« Ce que l'auteur savait »,
point 4) : « chemin et empreinte de la pièce qui liste chaque changement du brouillon 2 à la version » ; elle « aura à lister aussi
les changements des brouillons 3, 4, 5 et 6, dont les pièces de fabrication existent ». La version est le candidat de la session
principale.

### Pièces (empreintes à recalculer avant usage)
- Brouillon 2 : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon2.md` (`ff121bddca4786c2c981a335c87000c56e947512ab96068a147198d20a2786bb`).
- Brouillon 3 : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon3.md` (`1bfac4672e27e07ff8680e7be70c28f79dd921d0eccdc00ce873b8af467c47c7`) ; son
  bloc « Brouillon 3 — différences avec le brouillon 2 » dit ce qui a changé, sans pièce de fabrication.
- Brouillons 4, 5, 6 (`fe46a946…`, `88a2011a…`, `f707bced…`) et leurs pièces de fabrication dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/` : `couples-brouillonN-vers-brouillonM-v1.py`, sorties et `diff-…` pour 3→4,
  4→5, 5→6 ; chaque brouillon a en tête un bloc « Brouillon M — différences avec le brouillon N » et une table de traitement.
- Le candidat : `git show origin/main:docs/notes/neuron-lens-v1/scellement-texte-lecture-v2/lecture-sondes-bbis-par-lentilles-v2-candidat.md`
  (`39118ac138dee5ddb21142d1f8cdda6b005e15e0d156b6abaadbbb30d47fef8a`) ; son différentiel au brouillon 6,
  `…/scellement-texte-lecture-v2/differentiel-brouillon6-candidat.diff` (`e99425605c59b1e4…`, deux couples R1 et R2), et le script
  `…/applique.py`. Le rapport qui les motive : `docs/notes/neuron-lens-v1/verification-corrections-texte-lecture-lentilles-v2-brouillon6-v1.md`
  (`d6f7a166…`), R1 et R2. `git fetch origin main` permis, aucune autre branche.
- Les rapports de contre-lecture et de vérification que les blocs citent, si un changement y renvoie.

### Tâches
1. **Différentiel du brouillon 2 au brouillon 3**, par programme : `diff -u` entre les deux fichiers scellés, versé sous
   `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/diff-brouillon2-vers-brouillon3-v1.txt`, scellé. Vérifie que chaque hunk
   est expliqué par une ligne du bloc « Brouillon 3 — différences avec le brouillon 2 » ; tout hunk non expliqué est un écart :
   liste-le, sans le juger au-delà de ce que tu vois.
2. **Contrôle des différentiels existants** : recalcule `diff -u` pour 3→4, 4→5, 5→6 et brouillon 6 → candidat, compare aux pièces
   versées (égalité à l'octet ou écart dit).
3. **La pièce unique** : `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/changements-brouillon2-vers-version-v2-v1.md`, scellée.
   Pour chaque étape (2→3, 3→4, 4→5, 5→6, 6→candidat) : les pièces (chemins, empreintes), puis **une ligne par changement** :
   lieu (section et lignes dans le brouillon d'arrivée), nature (correction de règle, de mots, de citation, marqueur porté, histoire),
   raison (remarque de contre-lecture ou de vérification, décision de Lazar par son identifiant, tâche de mandat), et le couple ou
   hunk qui le porte. Reprends les tables de traitement des brouillons, sans les recopier en vrac : chaque ligne doit renvoyer à un
   hunk réel. En fin : le compte des changements par étape, et la liste de ce qui change une règle de lecture (seuil, statistique,
   libellé, arrêt, condition de lecture) séparée de ce qui ne change que des mots ou des citations. Aucun jugement de fond : tu
   décris.
4. Donne, en une phrase, le texte à porter à la place du marqueur (chemin et empreinte de la pièce unique).

### Forme
- Travaille dans ton bloc-notes (la session des lentilles te donne son chemin), puis verse les deux fichiers et scelle-les :
  `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <chemin>`.
- En tête de la pièce unique : l'auteur (toi, modèle Fable 5.2, sous-agent de la session des lentilles), les heures `date -u`, les
  pièces lues, les expositions.
- Aucun commit, aucun push, aucune machine, aucune dépense, aucun modèle chargé. Ne modifie aucun fichier existant.

### Cloisonnement — tu ne lis JAMAIS
- la liste « Jamais ouverts » de la v1 ;
- toute sortie, tout score, toute table, toute lecture ou tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y
  compris son verdict ;
- toute table ou sortie de la lecture par la lentille publique ;
- les branches `donnees/*` et `calcul/*` ;
- tout `diag/` ou `runs/` ; `docs/verdicts/`, tout fichier « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/` ;
- P3, P3-bis, T0.6, T0.7 hors ce texte, l'étape B, le bras d'attaque, le saboteur à budget ; dans les registres de la branche
  principale, ne lis que les lignes que tu cherches par leur identifiant.
- Le verdict de la tranche de nos lentilles (`3a9b947e…`) : pas de lecture demandée.

**Refus d'outil** : tout refus d'une permission ou d'un classifieur n'est ni rejoué, ni reformulé, ni contourné. Tu le déclares.

### Rends-moi
- chemins et empreintes des deux pièces ;
- le compte des changements par étape, et les changements de règle de lecture, une ligne chacun ;
- les écarts trouvés (hunk non expliqué, différentiel versé différent) ;
- le texte à porter à la place du marqueur ;
- les pièces lues, les expositions, les refus ; la confirmation que tu n'as rien ouvert d'interdit.
