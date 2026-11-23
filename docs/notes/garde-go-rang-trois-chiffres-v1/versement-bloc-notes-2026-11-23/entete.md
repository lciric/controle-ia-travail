# Inventaire des épingles de l'empreinte de la garde de calcul et des expressions de GO à deux chiffres — v1

Classe C (travail). Demande de la mère du 2026-11-22 vers 19:50Z (R-5026), session fille de la correction de la garde de calcul (demande de fusion n° 71). Relevé fait à 19:55Z sur `origin/main` = `43505ffb`. Rien n'a été changé dans le dépôt hors de ce dossier. Pas de dépense, aucune instance touchée.

**Méthode** :
- Recherche par programme : `inventaire_epingles_garde_v1.py`, dans ce dossier. Il lit `origin/main` par `git grep` et ne touche à aucun fichier.
- Le dépôt local est un clone partiel (historique tronqué) : la date du dernier commit d'un fichier n'est pas fiable et n'est pas donnée.
- L'activité de chaque procédure est jugée sur trois sources :
  1. la dernière décision datée de `registres/decisions.md` qui cite la famille, hors R-5013 et R-5026, qui portent sur la correction elle-même ;
  2. la dernière passation nommée par date qui la cite ;
  3. `registres/etat.md`, lu à la main.
- Le jugement final d'activité reste à la mère. Ce relevé donne des indices, pas un verdict.

## Synthèse par famille

### Feux de l'étape B bis, apprentissage des sondes sur la tâche
- **Pièces** : 9 fichiers, dont `registres/t07-etape-b-bis/feu-bbis-v7.txt`, ligne 402.
- **Nature de l'épingle** : contrôle exigé au moment du feu. Le geste 2 (b) attend `sha256sum garde_calcul.py` = `73be0638…`. Les autres fichiers sont les projets v3 à v7 et leurs contre-lectures.
- **Indices d'activité** : verdict de l'étape B bis scellé et accepté le 19 novembre (`registres/etat.md`). La course est finie, ce que la mère confirme.
- **Effet de la fusion** : le geste 2 (b) échouerait si on le rejouait. C'est sans objet si l'étape est close.

### Lanceur v3 de l'organisme d'idéation « bassins étroits »
- **Pièces** :
  - `verification-courte-lanceur-v3-v2.md`, lignes 29, 197 et 387 ;
  - `verification-outils-v3-v2/couples-epingle-lanceur-v3-v1.json`, ligne 5.
- **Nature de l'épingle** : précondition d'une modification non encore appliquée de la garde. Le fichier JSON porte `"sha256_avant": "73be0638…"` et quatre couples H1 à H4 (texte d'origine → texte neuf), marqués « NON appliqués » : retrait de l'épingle du lanceur v2, ajout de celle du v3.
  - Les textes d'origine de H1 à H4 ne sont pas touchés par la demande n° 71. Ils restent présents une seule fois chacun (vérifié par le contre-lecteur de la correction).
  - Seule la précondition d'empreinte casse, si l'outil qui applique les couples la vérifie.
- **Indices d'activité** :
  - Aucune mention dans `registres/etat.md`.
  - Dernière passation qui cite les bassins étroits : `2026-11-13-1732.md`.
  - Dernière décision qui les cite : R-4926 (22 novembre, 15:00Z). Elle porte sur le remue-méninges du 13 novembre retrouvé, pas sur le lanceur.
  - La mère le tient pour actif (R-5026). **Divergence à trancher par la mère** : aucun registre ne montre d'activité de ce lanceur depuis le 13 novembre.
- **Effet de la fusion** : il faudrait recalculer `sha256_avant` avec l'empreinte nouvelle, ou appliquer les couples avant la fusion puis rebaser la demande n° 71. Les deux modifications touchent des lignes différentes de la garde.

### Procédure du pilote v74 de l'organisme multi-générations
- **Pièces** : 8 notes de vérification, des versions 6 à 14 de la procédure pour la machine.
- **Nature de l'épingle** : constat. Les notes disent « crochet lu, `73be0638…`, égal dans la copie et dans le dépôt de travail » et l'ont éprouvé sur des entrées factices. La procédure elle-même ne cite pas l'empreinte : aucune ligne avec `73be0638`, `garde_calcul.py.sha256` ou `sha256sum … garde_calcul` dans son dossier.
  - En revanche, la vérification « égal dans la copie et dans le dépôt » échouerait si une copie de la garde avait été faite avant la fusion, puis comparée après.
- **Indices d'activité** :
  - Aucune décision ne cite « v74 » hors R-5026.
  - Dernière passation qui la cite : `2026-11-15-0912.md`.
  - `registres/etat.md` mentionne des instances du pilote les 16 et 17 novembre.
  - La mère la tient pour active (R-5026).
- **Effet de la fusion** : à confirmer par la mère selon que la procédure recopie la garde ou non.

### Machine du jeu de l'idée du poids du nul
- **Pièces** : `rapport-machine-jeu-idee-1-1-v1.md`, ligne 141.
- **Nature de l'épingle** : constat d'un rapport.
- **Indices d'activité** : dernière décision R-3236 (18 novembre) ; dernière passation `2026-11-18-1045.md`.
- **Effet de la fusion** : aucun, sauf si le rapport est rejoué.

### Préalables de l'étape A de T0.7
- **Pièces** : `prealables-etape-a-v1.md`, ligne 69.
- **Nature de l'épingle** : constat (case Q-19 remplie).
- **Indices d'activité** : dernière décision R-3542 (18 novembre) ; dernière passation `2026-11-14-0227.md`.
- **Effet de la fusion** : aucun.

### Registre des décisions
- **Pièces** : R-3148, R-3292 et R-5026.
- **Nature de l'épingle** : journal.
- **Effet de la fusion** : aucun.

### Compagnon de la garde
- **Pièces** : `.claude/hooks/garde_calcul.py.sha256`.
- **Nature de l'épingle** : le compagnon lui-même.
- **Effet de la fusion** : mis à jour par la demande n° 71.

**Contrôles à l'exécution** : aucun script de `src/`, `scripts/` ni `docs/procedures/` ne porte l'empreinte `73be0638` en clair. Les contrôles faits par le compagnon (`sha256sum -c garde_calcul.py.sha256`) passeront après la fusion, puisque le compagnon est mis à jour avec la garde.

**Précédent** : la garde a déjà porté au moins deux autres empreintes, `84512d4a…` et `184b3bbd…` (ordre non relevé). Les anciennes épingles restent dans des pièces closes, par exemple le préenregistrement P3-bis, qui cite `184b3bbd…`.

**Expressions à deux chiffres** : 36 fichiers, listés à la section 2. Tous restent fermés, sans brèche : un GO de rang 100 ou plus y est invisible ou refusé. Les lanceurs encore en service parmi eux devront recevoir la même correction le jour où un accord de rang 100 ou plus leur sera donné. Aucun n'a été modifié.

