# Contre-lecture indépendante (R2) — version 4 de la décision N-075, erratum 3 de la décision N-076 et proposition de mise à jour de `CLAUDE.md`

- **Date** : 2026-11-23T21:11Z (`date -u` ; dépôt sur `main` à `45047a87d`, aucun fichier du dépôt modifié).
- **Contre-lecteur indépendant** : sous-agent neuf (distinct de l'auteur `5aa04b1812ef837c1c7dbb497aaa57cd`), mandaté sous `GO-2026-11-23-32` et `GO-2026-11-23-33`.
- **Verdict** : **`À CORRIGER AVANT SCELLEMENT`** (deux défauts mineurs mais exacts de lettre dans `proposition-ligne-claude-md-n075-n076.md` et un résidu de libellé de ligne dans `decision-N-075-issue-plancher-et-deux-regards-v4.md` ; `decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md` tient sur le fond, les ancrages et les sources, avec une précision de ponctuation facultative aux instructions `E3-3` et `E3-9`).

---

## 1. Synthèse du verdict et corrections exactes demandées avant scellement

Sur le fond scientifique, le rejeu différentiel, les empreintes numériques et les pages de documents PDF citées, la version 4 de la décision N-075 et l'erratum 3 de la décision N-076 sont conformes aux pièces sources et n'outrepassent ni `GO-2026-11-23-32` ni `R-5185`. Trois corrections de lettre précises doivent toutefois être portées avant le scellement définitif et la mise à jour de `CLAUDE.md` :

1. **`proposition-ligne-claude-md-n075-n076.md`, ligne 15 (décompte de signes du segment N-076 proposé)** :
   - **Défaut** : la ligne 15 annonce `(585 signes sans le chevron, plafond de 600)` alors que le segment de la ligne 17 mesure **584 signes** sans le chevron et son espace (`len(ligne[2:]) == 584` ; 585 compte l'espace après `>`), en contradiction avec la convention appliquée aux lignes 13 (`631 signes`, exact) et 29 (`597 signes`, exact). De plus, le segment de la ligne 17 supprime « prévision scellée avant G1 » (présent à la ligne 13 de `CLAUDE.md`, sans lien avec l'erratum 3 et alors qu'il reste de la marge sous 600 signes) ainsi que « à faire » après « boucle, épreuves du devin », sans le signaler aux lignes 19 à 21.
   - **Correction exacte** : corriger la ligne 15 pour lire `(584 signes sans le chevron ni son espace, plafond de 600)` et mentionner l'omission aux lignes 19 à 21 (ou rétablir la mention de la prévision avant l'ouverture de la porte de phase 1 si la mère souhaite la conserver dans `CLAUDE.md`).
2. **`proposition-ligne-claude-md-n075-n076.md`, ligne 31 (décompte de signes du segment N-075 proposé)** :
   - **Défaut** : la ligne 31 annonce `(598 signes sans le chevron, plafond de 600)` alors que le segment de la ligne 33 (dépourvu du point final présent à la ligne 267 de `decision-N-075-issue-plancher-et-deux-regards-v4.md`) mesure **597 signes** sans le chevron et son espace (`len(ligne[2:]) == 597`). Note : la ligne 267 de `decision-N-075-issue-plancher-et-deux-regards-v4.md` porte bien un point final et mesure exactement **598 signes** (ligne 269 exacte). Par ailleurs, les lignes 35 à 38 de la proposition affirment « Aucune perte sur les acquis conservés » sans signaler que deux raccourcis ont retiré « à démontrer » (après « lemme resserré au reste ») et « sur l'oracle » (après « réapprentissage ») par rapport à `ligne-claude-md-N-075-v2.md`.
   - **Correction exacte** : à la ligne 31, remplacer `598 signes sans le chevron` par `597 signes sans le chevron ni son espace` (ou ajouter le point final à la ligne 33 si le décompte à 598 est visé, sachant que la ligne 13 de `CLAUDE.md` sépare les segments par ` ; ` sans point final) et mentionner les deux raccourcis de mots aux lignes 35 à 38.
3. **`decision-N-075-issue-plancher-et-deux-regards-v4.md`, ligne 348 (section 14)** :
   - **Défaut** : la ligne 348 conserve la phrase de la version 3 « `Numéros de ligne de ce fichier, calculés par programme sur un passage unique à chaque fois.` » juste au-dessus du tableau de la ligne 350 renommé « `lignes de la v3 d'origine` ». Or, dans la version 4 (qui compte 362 lignes contre 359 en version 3, du fait des 3 lignes ajoutées à la section 1 et à la section 2), les numéros de la troisième colonne ne sont plus les numéros de ligne de « ce fichier » (la version 4), mais ceux de la version 3 d'origine (par exemple, la ligne 256 de la version 3 mentionnée juste après est devenue la ligne 259 de la version 4, et les lignes 48 et 258 sont devenues 49 et 261).
   - **Correction exacte** : dans `generer_n075_v4.py` et dans `decision-N-075-issue-plancher-et-deux-regards-v4.md` (ligne 348), remplacer `Numéros de ligne de ce fichier, calculés par programme sur un passage unique à chaque fois.` par `Numéros de ligne de la version 3 d'origine, calculés par programme lors de son établissement sur un passage unique à chaque fois.` (et régénérer le différentiel, la table de remplacements et les fichiers compagnons `.sha256`).

*(Correction facultative de ponctuation sur `decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md` : les consignes `E3-3` à la ligne 36 et `E3-9` à la ligne 56 demandent d'« Ajouter à la fin de l'alinéa : `« ; ... »` » sur la ligne 308 de la décision N-076 v1, laquelle se termine déjà par un point final. Préciser « avant le point final de la ligne 308 » évite un point-virgule collé après un point lors d'une consolidation ultérieure.)*

---

## 2. Contrôle des livrables et de leurs empreintes numériques

Les six fichiers livrés dans `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/redaction-n075-n076/` concordent à l'octet avec leurs compagnons `.sha256` (vérifiés par `sha256sum -c`, 6 sur 6 conformes) :

- `decision-N-075-issue-plancher-et-deux-regards-v4.md` : `1101cb8415272137d445229c58c742cfd21bec4775946a47a9e58e1df25f6b23` (362 lignes, 95 240 octets)
- `decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md` : compagnon conforme (92 lignes, 20 058 octets)
- `diff-decision-N-075-v3-contre-v4.patch` : compagnon conforme (223 lignes, 83 792 octets)
- `generer_n075_v4.py` : compagnon conforme (360 lignes, 40 646 octets)
- `proposition-ligne-claude-md-n075-n076.md` : compagnon conforme (39 lignes, 4 972 octets)
- `table-remplacements-n075-v3-vers-v4.md` : compagnon conforme (53 lignes, 10 772 octets)

Aucun fichier du dépôt `/home/antigravity/lciric/controle-ia-travail` n'a été modifié (`git status --porcelain` vide, branche `main`). Le commit `05c6d54102fad068630c4ef1a6a5ba22603fa7f7` cité comme état initial de `main` lors de la rédaction précède uniquement deux commits de registre (`9757ce2be` et `45047a87d`, `R-5191` et `R-5192`) qui ne touchent ni `CLAUDE.md`, ni `docs/decisions/`, ni `registres/go.md`.

---

## 3. Vérification 1 : rejeu différentiel de `decision-N-075-issue-plancher-et-deux-regards-v4.md`

### 3.1 Reproductibilité exacte et absence de modification non déclarée
- Le rejeu de `generer_n075_v4.py` à partir de `main:docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md` (`5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5`, conforme à son compagnon, 359 lignes, 86 245 octets) reproduit `decision-N-075-issue-plancher-et-deux-regards-v4.md` à l'octet près (`True`, 44 remplacements uniques vérifiés).
- Le rejeu de `diff -u` (contexte `n = 2`) entre la version 3 et la version 4 reproduit `diff-decision-N-075-v3-contre-v4.patch` à l'octet près (`True`).
- L'inspection des seize blocs du différentiel (`diff -u`, 56 lignes supprimées, 59 lignes ajoutées) confirme que chaque modification correspond exactement à l'un des quatre ensembles déclarés :
  1. **En-tête et métadonnées de version 4** (`H-1` à `H-5`, lignes 1, 3, 4, 6, 9) : titre `(v4)`, renvois à `GO-2026-11-21-61`, `GO-2026-11-23-32`, `R-5185`, `GO-2026-11-23-33` (remplacement temporaire déclaré de Claude Fable par Carbon en effort élevé), archivage de la version 3 et de ses trois errata, sources et marques des quatre fiches scellées.
  2. **Intégration de l'erratum 1, de l'erratum 2 et de l'erratum 3 version 2 de la version 3** :
     - Les vingt et un remplacements `R-1` à `R-20` (dont `R-15` et `R-15 bis`) et les trois ajouts `A-1` à `A-3` de l'erratum 3 version 2 sont portés fidèlement. Seul `R-18` (ligne 255 de la version 4) adapte la dernière clause de l'erratum 3 version 2 (« `; ce qui est retenu se lit dans l'erratum 3.` » remplacé par « `; d'ici son mot, la règle en vigueur de la décision N-060 v3 (point 4) s'applique.` » tiré de la section 2 de l'erratum 3 version 2 et de l'erratum 2), ce qui est cohérent avec la consolidation.
     - La correction « suite 2 » de la section 1 point 8 de l'erratum 3 version 2 (`signal` remplacé par `motif` à la ligne 117 de la version 3, devenue ligne 120 de la version 4) est portée.
     - Les corrections `C-1` et `C-2` de l'erratum 1 sont intégrées (lignes 236 et 240 de la version 4 ; `C-3` et `C-4` étant remplacées par `R-11` et `R-20` en conservant l'ajout `-46`).
     - La trouvaille de côté de `verification-decision-N-075-v3-erratum-3-v1.md` (`0,0511` corrigé en `0,0510` pour `0,95**58`) est portée (ligne 261 de la version 4).
     - Les mises à jour de « Lecture d'ensemble » sur les lignes 4, 249, 266, 301, 354, 356, 357 et 359 de la version 3 sont portées (hors le défaut signalé en section 1 ci-dessus sur la phrase conservée à la ligne 348 de la version 4).
  3. **Intégration des quatre corrections issues de la lecture des seize papiers (`GO-2026-11-23-32`, `R-5185`)** : `PDF-1a` à `PDF-4b` (lignes 77, 99, 100, 107, 215, 217, 220 de la version 4). Aucune autre section ni aucun énoncé retenu n'est altéré.

### 3.2 Préservation des options ouvertes (notamment le point 9 de la section 11)
- Le texte du point 9 de la section 11 (ligne 259 de la version 4) est conservé **à l'octet près** par rapport à la ligne 256 de la version 3 (`True`), avec la recommandation d'origine de l'auteur `(a)`.
- L'en-tête introduisant les points 7 à 11 (ligne 255) et la section 14 (ligne 348) indiquent explicitement : le point 9 n'est **pas tranché**, Lazar penche pour `(b)`, la question va au collisionneur et à l'organisme, et **d'ici son mot, la règle en vigueur de la décision N-060 v3 (point 4) s'applique**.
- La rubrique « Ne pas écrire » (ligne 222) conserve l'interdiction : « `« le réapprentissage des sondes en service est permis », tant que le point 9 n'est pas tranché.` »
- Les points 1 à 5 de la section 11 (autres que le constat de mise à jour factuelle du point 4 sur la réécriture désormais retenue au point 8) ne sont pas tranchés.
- Le point 11 de la section 11 laisse explicitement la campagne de dommages plantés en dehors de la décision (décision D-3 à part, avec son devis et son cloisonnement).

### 3.3 Concordance des chiffres, pages de documents PDF et empreintes numériques
Toutes les empreintes numériques vérifiées contre les fichiers et leurs compagnons `.sha256` (sur `main` et `origin/lecture/papiers-saboteur-sondes-v1`) concordent à l'octet. Contrôle des quatre corrections par fiches scellées et vérification directe sur les pages extraites par `pdftotext` (R7) :
- **Xu, Yuksekgonul et Zou (`2602.00986 v2`, `da004f53…`, 25 pages vérifiées ; `fiche-2602.00986-v1.md`, `817712a3…`)** :
  - Lignes 100, 107, 215 : pouvoir de séparation et non calibration (`0` occurrence du radical `calibrat` dans les 25 pages du document PDF) ; aire sous la courbe `0,62` pour la longueur de la question contre `0,67` pour les neurones de valeur (Tableau 3, page 8 du document PDF, vérifié) ; aucune récompense manquante ni aucun adversaire testé sur tâches ouvertes (annexe K, page 25 du document PDF, vérifié) ; pages citées `1, 4, 5, 8, 9, 25` conformes à la fiche.
- **Ge-Wang et al. (`2606.06529 v1`, `6042d449…`, 19 pages vérifiées ; `fiche-2606.06529-v1.md`, `508ed82c…`)** :
  - Lignes 77, 220 : audit des plus suspects ; une seule baisse dont l'intervalle de confiance exclut zéro au budget d'audit de `1 %`, sur `23` trajectoires (`−28` points, intervalle `[−37, −8]`, Tableau 2 et texte page 5 du document PDF, vérifié) ; qualifiée de « heuristic upper bound » (page 11 du document PDF, vérifié) ; tirage au hasard non testé (conforme à la fiche).
- **Zhong et Raghunathan (`2508.00161 v3`, `898dffaf…`, 39 pages vérifiées ; `fiche-2508.00161-v1.md`, `8ab9faa7…`)** :
  - Lignes 113, 217 : la répétition d'un écart déjà signalé passe en silence tandis qu'un écart qui grandit pas à pas dépasse l'extrême courant et reste signalé (mécanisme d'élargissement de plage par minimum et maximum, pages 4 et 5 du document PDF, vérifié) ; borne des fausses alertes sous tirages indépendants et échangeables (preuve du théorème 3.1, page 17 du document PDF, vérifié) ; pages citées `1, 2, 4, 5, 7, 8, 16, 17` conformes à la fiche.
- **McKenzie et al. (`2506.24068 v3`, `3e08b7cc…`, 40 pages vérifiées ; `fiche-2506.24068-v1.md`, `180ebfa5…`)** :
  - Lignes 99, 220 : chaîne de garde-fous d'entrée et de sortie sans sonde sur activations (page 3 du document PDF, vérifié) ; suppose que l'attaquant voit quel étage l'a bloqué — `71 %` de succès avec ce retour, `33 %` par transfert sans accès (pages 1 et 10 du document PDF, vérifié).
- **Acronymes et emojis dans les passages nouveaux de la version 4** : aucun emoji ; aucun acronyme nouveau non développé ajouté (les seuls sigles présents dans le texte ajouté sont les identifiants du dépôt `GO`, `CLAUDE.md`, `R7`, `R8`, `R12`, `D-P4`, `V1` à `V10`, `C-1` à `C-4`, « document PDF » ou la marque `[PDF, p.]` définie en en-tête, ainsi que des sigles déjà présents en version 3).

---

## 4. Vérification 2 : `decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md`

### 4.1 Unicité et exactitude de chaque ancrage dans `decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`
Chaque ancrage visé par `E3-1` à `E3-9` dans `main:docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` (`49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78`) a été vérifié par programme :
- `E3-1` (section 2, ligne 72) : le texte « Ancien » existe exactement à la ligne 72 et apparaît **1 seule fois** dans tout le fichier.
- `E3-2` (section 11, tableau, ligne 304) : le texte « Ancien » correspond à l'octet près à la ligne 304 et apparaît **1 seule fois** dans tout le fichier.
- `E3-3` (section 11, « Ne pas écrire », ligne 308) : la ligne 308 cible existe exactement et est unique. *(Remarque de forme : elle se termine par un point final ; l'ajout de `; ...` doit s'entendre avant ce point final.)*
- `E3-4` (section 1, « Nul par acte », ligne 29) : le texte « Ancien » correspond à l'octet près à la ligne 29 et apparaît **1 seule fois**.
- `E3-5` (section 2, « Ce qui pourrait être revendiqué… », ligne 68) : la section 2 contient une seule rubrique de ce nom à la ligne 68, dont le texte complet est unique.
- `E3-6` (section 2, « Voisins qui occupent une part », ajout après la ligne 76) : la dernière puce de cette liste en section 2 est exactement la ligne 76, unique.
- `E3-7` (section 7, ligne 204 en contexte et ajout à la fin de la ligne 208) : la rubrique « Voisins qui occupent une part » de la section 7 est exactement la ligne 208, unique.
- `E3-8` (section 11, ajout après la ligne 304) : l'insertion suit immédiatement la ligne `point 1` (ligne 304), à l'intérieur du tableau des lignes 291 à 306.
- `E3-9` (section 11, « Ne pas écrire », ligne 308, à la suite de `E3-3`) : même ligne 308, unique.
- Contrôle d'exhaustivité : aucun autre passage de `decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` ni de ses errata 1 et 2 ne cite `1608.00698`, `1612.09027` ou `2109.11761`.

### 4.2 Fidélité aux fiches scellées, aux documents PDF et respect de `GO-2026-11-23-32`
- **He et al. (`1612.09027 v1`, `93e70341…`, 4 pages vérifiées ; `fiche-1612.09027-v1.md`, `3d931038…`) et Sobers et al. (`1608.00698 v3`, `4dcdbde7…`, 14 pages vérifiées ; `fiche-1608.00698-v1.md`, `105915a7…`)** :
  - Citations exactes vérifiées directement sur document PDF : « overly optimistic » (1612.09027, page 1) et « overestimates the covertness » ainsi que l'annulation du débit lorsque le niveau de détection tend vers zéro quel que soit le niveau d'incertitude (page 4) ; pour 1608.00698, théorème 1 sous puissance de brouilleur retirée uniformément à chaque fenêtre (page 5), observations hors fenêtre ne renseignant pas le guetteur (page 2), clé partagée de longueur illimitée (page 10) et retour à la loi en racine avec de nombreuses fenêtres calmes (page 1).
  - La nuance porte fidèlement la fiche et la synthèse sans inventer de règle nouvelle ; elle précise simplement que l'énoncé de ligne 72 doit mentionner la probabilité de détection fixée et l'exigence de bruit retiré à chaque fenêtre.
- **Arnold, Henzi et Ziegel (`2109.11761 v3`, `252a4c29…`, 35 pages vérifiées ; `fiche-2109.11761-v1.md`, `959857b4…`)** :
  - Occupation statistique du nul par acte : tests séquentiels valides à tout instant par e-valeurs (inégalité de Ville, pages 2 et 7) sur l'uniformité du rang d'une observation parmi les `m` membres d'un ensemble de prévisions (pages 1, 6, 10 et 11), sous dépendance sérielle et ordre stochastique (pages 3 et 6) ; vérifié directement sur document PDF.
  - Facteur de durcissement `e · log h` et moyenne de `h` sous-produits lorsque le verdict est différé de `h > 1` pas : vérifié exactement sur la proposition 4.1 et la formule du temps d'arrêt aux pages 7 et 8 du document PDF (`1 / (h e log(h))` devant la somme des `h` produits).
  - Limites de la page 2 et de la page 20 (biais changeant de signe manqué sur toute la période ; e-valeur qui baisse ne prouvant pas la calibration) vérifiées sur document PDF.
- **Respect du périmètre de `GO-2026-11-23-32` et `R-5185`** : la section 3 (« Ce qui ne change pas ») maintient explicitement les neuf points de N-076, les quatre invariants d'audit, la table du seuil, l'exception de l'horizon `m` pour le nul par acte (seule la nouveauté statistique sur cet outil est retirée et sa citation rendue obligatoire). Aucune revendication ajoutée, aucune porte ni dépense touchée.
- **Acronymes et emojis** : zéro emoji ; aucun acronyme non développé (`PDF` est développé « document PDF » dans le titre et les en-têtes ; les identifiants du dépôt et la fonction d'empreinte sont conformes aux usages du dépôt).

---

## 5. Vérification 3 : `proposition-ligne-claude-md-n075-n076.md`

- Les segments « actuels » repris aux lignes 13 et 29 concordent caractère pour caractère avec la ligne 13 de `CLAUDE.md` (`2246ff0183348d525737aca0086c3149a8b630358490b5f4acef7d94c18edabd`), respectivement 631 et 597 signes.
- Les deux segments proposés (lignes 17 et 33) tiennent sous le plafond de 600 signes (584 et 597 signes sans le chevron ni son espace) et renvoient aux bons identifiants (`GO-2026-11-23-32`) et aux bons fichiers.
- Le segment N-075 de la ligne 33 respecte le statut non tranché du point 9 (« réapprentissage non tranché, N-060 v3 tient »).
- **Défauts à corriger avant versement dans `CLAUDE.md`** : les deux erreurs d'une unité dans les décomptes affichés aux lignes 15 (`585` au lieu de `584`) et 31 (`598` au lieu de `597`), et la transparence sur les raccourcis par rapport aux segments actuels (notamment la suppression de `prévision scellée avant G1` et `à faire` dans N-076, et de `à démontrer` et `sur l'oracle` dans N-075).

---

## Ligne « qui a lu quoi »

- **Sous-agent contre-lecteur indépendant (R2)** (session neuve distincte de l'auteur `5aa04b1812ef837c1c7dbb497aaa57cd`, mandat `GO-2026-11-23-32` et `GO-2026-11-23-33`, 2026-11-23T21:11Z) — **lu en entier** : `CLAUDE.md` (`2246ff01…`), les six livrables de `scratch/redaction-n075-n076/` (`decision-N-075-issue-plancher-et-deux-regards-v4.md` `1101cb84…`, `generer_n075_v4.py`, `diff-decision-N-075-v3-contre-v4.patch`, `table-remplacements-n075-v3-vers-v4.md`, `decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md`, `proposition-ligne-claude-md-n075-n076.md`) ; sur `main` : `decision-N-075-issue-plancher-et-deux-regards-v3.md` (`5aed4bab…`), ses errata 1 (`c6efeccf…`), 2 (`b19852b4…`), 3 version 2 (`fbe3298e…`), `verification-decision-N-075-v3-erratum-3-v1.md` (`59b18766…`), `ligne-claude-md-N-075-v2.md` (`dd6cbe15…`), `decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` (`49b664c1…`), ses errata 1 (`34a59c49…`) et 2 (`c2943188…`), lignes `GO-2026-11-23-32` et `-33` de `registres/go.md` et `R-5185` de `registres/decisions.md` ; sur `origin/lecture/papiers-saboteur-sondes-v1` : `synthese-lecture-papiers-saboteur-sondes-v1.md` (`8b63dc17…`), `contre-lecture-synthese-v1.md` (`b786fbe4…`), `explications-pour-lazar-trois-points-v1.md` (`f1ec7cfa…`) et les sept fiches scellées (`fiche-2602.00986-v1.md` `817712a3…`, `fiche-2606.06529-v1.md` `508ed82c…`, `fiche-2508.00161-v1.md` `8ab9faa7…`, `fiche-2506.24068-v1.md` `180ebfa5…`, `fiche-1612.09027-v1.md` `3d931038…`, `fiche-1608.00698-v1.md` `105915a7…`, `fiche-2109.11761-v1.md` `959857b4…`) ; **extraits des documents PDF vérifiés directement par `pdftotext` et `pdfinfo`** (R7) : `2602.00986v2.pdf` (`da004f53…`, 25 pages, p. 1, 4, 5, 8, 9, 25 et recherche intégrale du radical `calibrat`), `2606.06529.pdf` (`6042d449…`, 19 pages, p. 1, 5, 11), `2508.00161v3.pdf` (`898dffaf…`, 39 pages, p. 1, 2, 4, 5, 7, 8, 16, 17), `2506.24068v3.pdf` (`3e08b7cc…`, 40 pages, p. 1, 3, 10), `1612.09027v1.pdf` (`93e70341…`, 4 pages, p. 1, 2, 4), `1608.00698v3.pdf` (`4dcdbde7…`, 14 pages, p. 1, 2, 5, 10) et `2109.11761v3.pdf` (`252a4c29…`, 35 pages, p. 1 à 3, 6 à 8, 10, 11, 14, 20). **Non lu** : `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/*` et aucun autre fichier du dépôt hors la liste fermée du mandat.
