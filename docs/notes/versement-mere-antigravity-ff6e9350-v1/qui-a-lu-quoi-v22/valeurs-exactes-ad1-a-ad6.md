# Valeurs exactes vérifiées pour les champs `AD-1` à `AD-6`, la table des expositions et « Contre-lecture 2 » — additif 1 aux sondes du barreau 8 (brouillon 7)

- **Date et heure de vérification (temps universel coordonné)** : `2026-11-23T21:33:23Z`
- **Pièces vérifiées** :
  - Brouillon 7 de l'additif : [`lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/redaction-additif-b8/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md) (empreinte cryptographique à 256 bits `ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`) ;
  - Protocole de scellement : [`protocole-scellement-mere-additif-b8-v1.md`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/redaction-additif-b8/protocole-scellement-mere-additif-b8-v1.md) ;
  - Rapport de contre-lecture du brouillon 6 : [`contre-lecture-additif-sondes-barreau8-brouillon6-v1.md`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cl-additif-b8/contre-lecture-additif-sondes-barreau8-brouillon6-v1.md) (empreinte `ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`) ;
  - Rapport de vérification finale du brouillon 7 : [`verification-corrections-additif-sondes-barreau8-brouillon7-v1.md`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cl-additif-b8/verification-corrections-additif-sondes-barreau8-brouillon7-v1.md) (empreinte `2f08ff60ae22f39dfd2b82c47955c2ce8a1fb089b8d73276630830fd3b9c511c`) ;
  - Liste « qui a lu quoi » version 22 établie dans ce même dossier : [`qui-a-lu-quoi-v22.md`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/qui-a-lu-quoi-v22/qui-a-lu-quoi-v22.md) (empreinte `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4`, 589 lignes).
- **Contrôle préalable sur la branche `claude/iib-executante-v7` (`9dcbce074e473b322f99c2196b19588a11bc49be`) et sur `main` via l'interface de programmation GitHub (noms de fichiers seuls, aucune sortie ni pièce privée ouverte)** :
  - **Aucune pièce `attestation-ordre-course-lue-additif-1-v1.json`**, **aucune pièce `attestation-course-et-oracle-additif-1-v1.json`** et **aucune attestation séparée des exclus de l'ordre neuf** n'existent ni sur `main` ni sur `claude/iib-executante-v7` (`9dcbce07`).
  - Dans `docs/notes/barreau8-cote-moniteurs-entrees-v1/`, seule la version 6 (`interface-passe-cote-moniteurs-v6.md` et `.sha256`, plus `v3` et `v5`) existe à ce jour sur les deux branches ; dans la comparaison `main...9dcbce07`, la seule pièce d'ordre présente en écart est `brouillons/ii-b-saboteur-budget-v5/additif-course-v1/additif-ordre-course-voie-A-v1-brouillon8-commit-lancement.md` (et son compagnon).
- **Simulation sur [`src/controle_ia/prereg.py`](file:///home/antigravity/lciric/controle-ia-travail/src/controle_ia/prereg.py)** : sur le brouillon 7 brut, la fonction `problemes(...)` retourne `['section vide ou à remplir : Contre-lecture']` et dénombre exactement 7 marqueurs d'attente aux lignes 153 à 158 et 599 ; après substitution simulée des valeurs ci-dessous, `problemes(...)` retourne `[]` (zéro erreur, zéro marqueur restant).

---

## 1. Tableau récapitulatif des valeurs vérifiées pour `AD-1` à `AD-6`

### Champ `AD-1` (ligne 153 du brouillon 7)
- **Sources vérifiées** : `registres/go.md` lignes 855 (`GO-2026-11-23-17`), 870 (`GO-2026-11-23-32`) et 871 (`GO-2026-11-23-33`).
- **Texte exact à placer dans la cellule d'état** :
```text
GO-2026-11-23-32 (complété par GO-2026-11-23-17 point 4 et GO-2026-11-23-33) — mots de Lazar : NL-0 « go » (scellement après la fin de course, trois bornes), NL-11 « go » (lecture sur activations recalculées), NL-9 « go » (cinq lectures comparées hors verdict), NL-1 à NL-6 « go » ; résultat comparé dans l'additif ; sous-agents autorisés sur la classe A avec Carbon en effort élevé.
```

### Champ `AD-2` (ligne 154 du brouillon 7) et attestation des exclus
- **Constat vérifié** :
  - Chaque agent nommé dans la table des expositions du brouillon 7 (lignes 510 à 515 : rédacteur du brouillon 1, lecteur de la note de couverture, correcteurs des brouillons 2 et 3 et relecteur, rédacteur des brouillons 5 et 6 `session_016QhUrs5yLghTY6Gthp4k3P`, contre-lecteur du brouillon 6 et vérificateur du brouillon 7 `289f9a3a862f39f87ccb565b8aa65125`, rédacteur du brouillon 7 `a99cfcf7527baf9160bb77d7cb2dca01`) ainsi que les trois sessions mères successives et les agents initiaux de la ligne 516 sont recensés dans `registres/qui-a-lu-quoi-v22.md` (`7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4`) ; aucun ne figure parmi les agents du côté exposé nommés aux registres pour le saboteur à budget (`session_013QMaymHf2YhybDs3MJ62xr`, `session_013QMaym1QE4UyYr1H8KU8Rf`, `session_016QhUrrzvUnExGyzZHznnaF`, `session_013QMayiwfx2DB6CHn9yZ2wH`, ni aucun auteur ou exécutant d'ordre/consigne privée).
  - **Point bloquant à vérifier par la mère avant scellement** : comme aucune pièce séparée et scellée « attestation d'exclus de l'ordre neuf » n'existe encore sur `main` ni sur `9dcbce07` (voir section 0 ci-dessus), la session mère doit, avant de sceller ou en demandant l'attestation d'ordre à un agent habilité du côté exposé, recueillir l'attestation d'exclus (sans lire le contenu de l'ordre neuf) et insérer son chemin et son empreinte exacte de 64 caractères hexadécimaux dans `AD-2`.
- **Modèle exact de cellule pour `AD-2` une fois la pièce d'exclus disponible** :
```text
Table des expositions complétée ci-dessous ; attestation de la session mère (date -u : <HEURE_UTC_SCELLEMENT>) : vérification effectuée contre l'attestation d'exclus de l'ordre neuf (<CHEMIN_EXCLUS>, empreinte <SHA_EXCLUS>) — aucun agent nommé dans la table des expositions ne figure parmi les exclus de l'ordre neuf.
```

### Champ `AD-3` (ligne 155 du brouillon 7)
- **Valeurs exactes vérifiées contre `registres/decisions.md` (`R-5173`, `R-5186`) et les horodatages de commits via l'interface de programmation GitHub** :
  - **Première sortie de l'étalonnage** (commit `8d839f33c730dec5e4dad55ec66af108ca43da79`, branche `essai/iib-explo-v7`, horodatage auteur et committeur vérifié) : `2026-11-22T20:29:04Z` ;
  - **Première sortie de la course lue** (commit `0ee74d3fb755c1bd33ed5ab956e2831a043cec1a`, branche `essai/iib-explo-v8`, horodatage auteur et committeur vérifié) : `2026-11-23T04:41:59Z` ;
  - **Fin de la course lue** :
    - `2026-11-23T13:20:20Z` selon `R-5186` (fin de l'évaluation des 4 conditions) ;
    - pour information exacte des commits sur `essai/iib-explo-v8` : versement fin de course `e797898c4f68efc85b5d42544e4fc1e7b6d5f54a` à `2026-11-23T13:20:24Z`, fin des traces `3326499e666c6b2a3670feda6ee5e15ed055170a` à `2026-11-23T13:20:33Z`, arrêt amorce à `13:20:36Z` (`registres/arrets.md` ligne 165). Conformément au protocole de scellement (ligne 44), l'heure de fin d'évaluation de `R-5186` (`2026-11-23T13:20:20Z`) est celle attendue au champ `AD-3`.
  - **Scellement de l'additif** : `<HEURE_UTC_SCELLEMENT>` relevée par `date -u` lors du scellement effectif par la mère ;
  - **Lectures du dommage et de la diffusion jouées avant ce scellement** : à vérifier par la mère à l'instant du scellement (`non` si aucune lecture d'oracle/dommage n'a été inscrite ou lancée d'ici là) ;
  - **Bornes dures `(b1)`, `(b2)` et `(b3)` tenues** : `oui` (aucun agent du côté des moniteurs ni de la chaîne n'a ouvert de sortie ; l'extrait `etats-lectures-iib-v1.json` n'est pas écrit ; aucune passe de recalcul n'est partie, `registres/sondes-iib-v1.md` ne portant toujours que la ligne `SCELLEMENT-SONDES-IIB`) ;
  - **Source de `(b1)`** : `registres/qui-a-lu-quoi-v22.md`, empreinte `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4` (une fois ce brouillon v22 versé tel quel et accompagné de son `.sha256` sur `main` par la session mère ; sinon, si la mère modifie ou complète v22 avant dépôt, utiliser l'empreinte réelle du fichier `registres/qui-a-lu-quoi-v22.md` versé sur `main`).
- **Texte exact à placer dans la cellule d'état (forme imposée par la ligne 548 du brouillon 7)** :
```text
première sortie de l'étalonnage : 2026-11-22T20:29:04Z ; première sortie de la course : 2026-11-23T04:41:59Z ; fin de la course : 2026-11-23T13:20:20Z ; scellement de l'additif : <HEURE_UTC_SCELLEMENT> ; lectures du dommage et de la diffusion jouées avant ce scellement : <oui ou non> ; bornes (b1), (b2) et (b3) tenues : oui ; source de (b1) : registres/qui-a-lu-quoi-v22.md, empreinte 7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4
```

### Champ `AD-4` (ligne 156 du brouillon 7)
- **Constat vérifié** : aucun fichier `attestation-ordre-course-lue-additif-1-v1.json` (ni autre fichier d'attestation d'ordre) n'existe dans l'arborescence de `main` ni de `claude/iib-executante-v7` (`9dcbce07`).
- **Deux options exactes au moment où la mère scelle** :
  1. Si la mère obtient la pièce d'attestation d'ordre scellée auprès d'un agent habilité du côté exposé avant le scellement de l'additif :
     `<oui | non> (pièce d'attestation de l'ordre : <CHEMIN_ATTESTATION_ORDRE>, empreinte <SHA_ATTESTATION_ORDRE>)`
  2. Si la mère scelle sans que la pièce d'attestation d'ordre ait encore été produite (la réponse à `E-1` restant alors non établie au scellement) :
```text
inconnue (pièce d'attestation de l'ordre : absente au scellement)
```

### Champ `AD-5` (ligne 157 du brouillon 7)
- **Texte exact à placer dans la cellule d'état** :
```text
rempli (dans la section)
```

### Champ `AD-6` (ligne 158 du brouillon 7)
- **Sources vérifiées** :
  - `registres/depenses.md`, ligne 615 (`R-5109`, engagement de la course voie (A)) : `GO-2026-11-22-75 (prolongé par -93), exception de crédit GO-2026-11-23-02` ;
  - `registres/arrets.md`, ligne 165 (destruction `62094628`) : `GO-2026-11-22-75, -93, GO-2026-11-23-30` ;
  - `registres/go.md`, ligne 762 (`GO-2026-11-22-75`, type `calcul`, plafond `60 USD`) et ligne 780 (`GO-2026-11-22-93`, prolongation au `2026-12-31`).
- **Texte exact à placer dans la cellule d'état** :
```text
GO-2026-11-22-75 (prolongé au 31 décembre 2026 par GO-2026-11-22-93 ; exception de crédit au départ GO-2026-11-23-02 ; clôture et destruction GO-2026-11-23-30)
```

---

## 2. Lignes exactes de la table des expositions du brouillon 7 (lignes 516 et 517)

La règle du scellement (ligne 121 du brouillon 7) autorise exclusivement la complétion des lignes ouvertes de la table des expositions par `AD-2` (et l'ajout de lignes si de nouveaux agents aval sont déjà désignés au scellement). Les lignes 510 à 515 étant déjà remplies et vérifiées dans le brouillon 7, seule la **ligne 516** est à compléter ; la **ligne 517** reste intacte tant que le lecteur, le juge et l'auditeur ne sont pas désignés (ou est complétée seulement si la mère les désigne au scellement).

- **Ligne 516 complétée (une ligne Markdown, quatre colonnes exactes)** :
```markdown
| conductrice du côté des moniteurs (`session_013QMayjujdhnn94JyDTmgSs`, v21 lignes 246 et 278) ; développeurs de la passe, de la lecture et du programme de report (`session_013QMayjujdhnn94JyDTmgSs` sous-agents v21 ligne 281 : codes v5 ; nouveaux codes post-additif non encore écrits au scellement) ; contre-lecteurs des codes (v21 ligne 281 ; contre-lecteur neuf des futurs codes non encore désigné au scellement) ; session mère (`session_013QMayjbmQUdDuDs2S3i3XD` v21 lignes 324 et v22 ligne 378 ; `session_016QhUrvi45g3jX5saFefVED` v22 ligne 379 ; session Antigravity `ff6e9350` v22 ligne 391) | conductrice et développeurs/contre-lecteurs initiaux (v21 lignes 246, 258, 278 à 281) : texte scellé, notes d'interface v3 à v6, codes v1 à v5 ; sessions mères : registres vivants (`R-5173`, `R-5186` donnant les seules heures et noms de commits d'étalonnage/course et le fait qu'aucune activité interne n'est enregistrée), mandats et pièces de travail sans sortie ; aucune pièce de la course lue ni de la note d'interface v7 ; futurs développeurs/contre-lecteurs des codes et du programme de report : non encore désignés au scellement | aucun pour la conductrice, les développeurs et contre-lecteurs v1 à v5 et la session mère Antigravity `ff6e9350` ; les sessions mères ont orchestré la chaîne et l'accord sans jamais ouvrir une ligne de `consigne-privee*` ni de `conception-ii-b*` et aucune agent nommé ici n'a vu la course lue ni ne figure parmi les exclus (AD-2) | aucune : attestation de la session mère (`AD-2`, `AD-3`) qu'aucune des trois sessions mères ni aucun agent du côté des moniteurs inscrit au registre « qui a lu quoi » version 22 (`7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4`) n'a lu aucune sortie de la course lue (`essai/iib-explo-v8`) ni de l'étalonnage (`essai/iib-explo-v7`) |
```
- **Ligne 517 (à garder intacte tant que non désignés au scellement)** :
```markdown
| lecteur des sondes, juge, auditeur (à désigner) | déclaré dans leur mandat et au registre « qui a lu quoi » | cause de nullité (liste d'arrêt, ligne 12) | cause de nullité (ligne 25) |
```

---

## 3. Entrée exacte « Contre-lecture 2 (finale, texte rempli) » (ligne 599 du brouillon 7)

Une fois le rapport de vérification [`verification-corrections-additif-sondes-barreau8-brouillon7-v1.md`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cl-additif-b8/verification-corrections-additif-sondes-barreau8-brouillon7-v1.md) (`2f08ff60ae22f39dfd2b82c47955c2ce8a1fb089b8d73276630830fd3b9c511c`) versé avec son compagnon `.sha256` dans le dépôt (à son chemin cible `<CHEMIN_RAPPORT_VERIF_SCELLE_DANS_LE_DEPOT>`), remplacer la ligne 599 par la ligne suivante (qui satisfait `src/controle_ia/prereg.py` en retirant l'unique marqueur restant et en portant toutes les empreintes à 64 caractères hexadécimaux) :

```markdown
- **Contre-lecture 2 (finale, texte rempli)** — contre-lecture du brouillon 6 (`bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e`) par le sous-agent neuf `289f9a3a862f39f87ccb565b8aa65125`, modèle Gemini 4 Carbon en effort élevé, mandaté directement par la session mère (règle R2 ; décisions `GO-2026-11-23-16`, `GO-2026-11-23-32` et `GO-2026-11-23-33`, en remplacement temporaire d'Opus autorisé pour ce contre-lecteur distinct du rédacteur), rapport `contre-lecture-additif-sondes-barreau8-brouillon6-v1.md` (empreinte `ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`, conclusion « À CORRIGER AVANT SCELLEMENT » : 0 bloquant, 3 majeurs M-1 à M-3, 5 mineurs m-1 à m-5) ; correction du brouillon 6 vers le brouillon 7 (empreinte `ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`) par le sous-agent neuf distinct `a99cfcf7527baf9160bb77d7cb2dca01` (Gemini 4 Carbon en effort élevé sous `GO-2026-11-23-33`), via le script reproductible `corrections-brouillon6-vers-brouillon7-v1.py` (empreinte `a7af0989f331b547d67ff1e5b3cd14cef23b0e638ceb09cd2dd8c989e7d9160e`) ; puis vérification finale des corrections du brouillon 7 à `2026-11-23T21:11:23Z` par ce même contre-lecteur `289f9a3a862f39f87ccb565b8aa65125` : rapport `<CHEMIN_RAPPORT_VERIF_SCELLE_DANS_LE_DEPOT>` (copie source dans l'espace de travail : `scratch/cl-additif-b8/verification-corrections-additif-sondes-barreau8-brouillon7-v1.md`, empreinte `2f08ff60ae22f39dfd2b82c47955c2ce8a1fb089b8d73276630830fd3b9c511c`), conclusion exacte : « **SCELLABLE EN L'ÉTAT (APRÈS REMPLISSAGE DES SEPT MARQUEURS PAR LA MÈRE)** » (0 bloquant, 0 majeur restant, rejeu exact octet pour octet confirmé, test `prereg.problemes` et `manifeste.graines` sur 270 clés validés). **Déclaré** : ce n'est pas l'agent de la contre-lecture 1, dont la vérification, prévue sur le brouillon 2, n'a pas eu lieu ; le contre-lecteur du brouillon 6 a donc relu le texte entier, non les seules différences. **Règle** : le texte soumis au scellement ne diffère du texte vérifié par cette contre-lecture qu'aux trois lieux permis par la règle du scellement (section « Ce que cet additif est, et n'est pas ») ; la session mère le vérifie par une comparaison faite par programme (liste d'arrêt, ligne 18).
```
