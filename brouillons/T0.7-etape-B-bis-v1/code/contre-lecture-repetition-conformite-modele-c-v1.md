rédigé sans vue des données de 7b

# Contre-lecture de la répétition sur carte de l'étape B bis de T0.7 — lentille « conformité » (modèle C), v1

- **Lecteur** : « modèle C », neuf, lentille conformité. **Date (UTC)** : 2026-11-14, de 23:05 à 23:15.
- **Copie lue** : `/home/user/relecture-bbis-repetition-v1`, tête `c880f36f9b02b2129cf0c33a9b455445650952a6` (vérifiée par `git rev-parse HEAD`).
- **Lu** : les deux notes du développeur (répétition v1, corrections v4), `scripts/repetition_carte_bbis_v1.py` (`229310db…`), `scripts/amorce_repetition_bbis_v1.sh` (`c56c9cc9…`), `scripts/lancer_repetition_bbis_v1.sh` (`7a02afc4…`), `tests/test_repetition_bbis_v1.py` (`4cc1eab9…`), le différentiel `f4427fb6` → `bbc2e1c8`, les passages utiles de `amorce_bbis_v1.sh`, `registre_bbis_v1.py`, `apprentissage_carte_v1.py`, `commun_v1.py`, `modeles.py` (réglage du déterminisme), et la liste d'arrêt et la section « Calcul et dépense » du texte scellé. Rien sous `diag/`, `runs/`, `donnees/`, `essai/` ; aucune sortie de 7a, 7b, T0.7, P3-bis ; aucun réseau, aucune location, aucun vrai `vastai`, aucune clé.
- **Effet de bord à déclarer** : le rejeu des essais a laissé des dossiers `__pycache__` (ignorés par git) dans la copie ; rien d'autre n'a été écrit hors de ce rapport.

## Verdict

**Feu possible après corrections.** Aucun constat bloquant : le code de la course est inchangé hors les deux modifications annoncées, la répétition appelle les fonctions de la course telles quelles, ne lit aucune entrée de 7b, et les 119 essais passent. Un constat majeur (règle R5 : plusieurs gardes de l'amorce de répétition n'ont ni cas sain ni artefact joués) demande soit une correction courte, soit une réserve écrite de la mère avant le feu.

Couples précis des corrections : voir « Corrections demandées » en fin de rapport (C-1, C-2).

## Réponses aux cinq questions

### (1) Essais : 119 passés — confirmé

`PYTHONPATH=src … -m pytest -q -p no:cacheprovider tests/test_t07bbis_*.py tests/test_repetition_bbis_v1.py` dans la copie : **119 passed, 4 warnings in 250,13 s**, code 0. Les avertissements sont les quatre avertissements de `fork()` déjà décrits par le développeur. Décompte conforme à la note v4 (109 de la course + 10 de la répétition).

### (2) Code de la course inchangé hors 60670453 et MIN_ESSAIS = 87 — confirmé

`git diff --stat f4427fb6 bbc2e1c8` : onze fichiers ; hors notes, sorties d'essais et fichiers neufs de la répétition (script, deux scripts shell, fichier d'essais), seuls trois fichiers existants bougent :
- `src/controle_ia/t07bbis/registre_bbis_v1.py` : `INSTANCES_D_AUTRES_SESSIONS` passe de cinq à six identifiants (`60670453` ajouté) et le commentaire est réécrit ; aucune autre ligne (lu ligne à ligne).
- `scripts/amorce_bbis_v1.sh` : `MIN_ESSAIS=86` → `87` et son commentaire ; aucune autre ligne.
- `tests/test_t07bbis_chaine_instance_v1.py` : un essai ajouté (`test_instance_60670453_refusee_comme_cible_admise_comme_temoin`), rien retiré.
`git diff --stat bbc2e1c8 c880f36f` : quatre fichiers, tous des notes ou sorties d'essais ; aucun code. Les autres fichiers de la course (dont `commun_v1.py`, `apprentissage_carte_v1.py`, `validation_imbriquee_v1.py`, `lancer_bbis_v1.sh`) n'apparaissent pas au différentiel. Aucune autre copie de la liste des instances n'existe dans le code (la liste du lanceur de répétition n'est qu'un commentaire d'en-tête, et le script de répétition la lit sur le module de la course, essai `is`).
Cohérence de 87 : 86 de la note v3 + l'essai neuf, qui entre dans l'ensemble joué sur l'instance (fichier `test_t07bbis_chaine_instance_v1.py`). La sortie `essais-sortie-corrections-v4.txt` (`bf556cde…`, empreinte compagnon égale) porte « 87 passed, 22 skipped » sur l'extraction simulée. **Non rejoué par moi** : l'extraction partielle simulée (elle exige d'écrire un arbre jetable, interdit ici) ; je m'en remets à la sortie scellée du développeur, que le décompte 109 → 119 rejoué corrobore sans la prouver.

### (3) La répétition joue les fonctions de la course sans les modifier, sans entrée de 7b — conforme, avec deux remarques

- **Appels tels quels** : `LotCarte`, `entrainer`, `controle_carte_processeur` (module `apprentissage_carte_v1`), `regler_determinisme(1, appareil)`, `grille`, `COUCHES_REELLES`, `FAMILLES`, `L2`, `N_PLIS_INTERNES`, `N_REETIQUETAGES`, `TOLERANCE_CARTE`, `VARIANTES`, `N_ACTIONS_CONTROLE_CARTE`, `validation_imbriquee_v1.apprentissages_prevus` et ses constantes, `registre_bbis_v1.garde_depense` (coupure 3 USD), `registre_bbis_v1.exiger_absence`. Aucune fonction réécrite, sauf la projection de la garde de débit (voir M-3).
- **Algorithmes déterministes** : `regler_determinisme(1, appareil)` est appelé avant tout apprentissage ; en cas de refus, code 2 écrit. Le déterminisme est relu : premier réglage de chaque famille réappris, égalité au bit près de `w`, `b`, `q`, sinon code 9. Cas sain et artefact joués (essai « instable », second apprentissage perturbé → 9).
- **Seuil 10⁻⁴ jamais relâché** : `jouer_carte` refuse (code 2, avant tout calcul) toute tolérance hors de `]0 ; TOLERANCE_CARTE]` ; l'amorce ne passe pas l'option `--tolerance` ; `controle_carte_processeur` de la course lève l'arrêt au-delà. Cas sain (≤ 10⁻⁴), relâchement à 10⁻³ (→ 2), seuil trop strict (→ 9 avec motif) joués. Les deux familles sont contrôlées (la course n'en joue qu'une : plus strict, déclaré).
- **Aucune entrée de 7b** : le script ne lit aucun fichier (il n'écrit que sa sortie) ; les jetons sont tirés par `SeedSequence` (R9) ; les imports (`registre_bbis_v1`, `commun_v1`, `apprentissage_carte_v1`, `modeles`) ne lisent aucun fichier à l'import (vérifié par lecture des en-têtes et recherche des lectures au niveau du module). L'amorce ne récupère que `BRANCHE_CODE` (`--single-branch`), lit par `git show` deux chemins nommés (amorce de la course, script de la répétition), extrait par les `MOTIFS` de la course et refuse (code 2) si `runs`, `diag`, `donnees` ou `essai` existe dans l'arbre. Le texte de l'amorce ne contient ni `fetch` ni nom de branche de 7b (essai). Le jeu de contrôle est tiré avec une clé distincte, donc une direction de signal distincte : sans conséquence pour une comparaison carte-processeur.
- *Remarque 3a (mineure)* : « aucune entrée de 7b » est garanti sur l'arbre de travail, non sur la base d'objets : un clonage partiel de la branche rapatrie quand même les commits et les arbres (noms de chemins, messages) de son historique ; seuls les blobs sont lazy. L'amorce n'en ouvre aucun, et c'est le même état que celui de la course ; à dire dans le compte rendu de la mère pour ne pas sur-promettre.
- *Remarque 3b (mineure)* : les essais de l'arbre de l'instance (`tests/test_t07bbis_*.py`) sont ceux de la course ; leurs 22 sautés sont ceux qui attendent des données absentes (par conception). Rien ne les lit.

### (4) R5 — un cas sain et un artefact par garde : **partiel** (constat M-1)

**Gardes de la partie Python** : toutes couvertes, sauf trois détails mineurs.
- Partie carte : sain, sortie déjà présente (2), tolérance relâchée (2), tolérance trop stricte (9), erreur de torch simulée (8, motif et pile écrits), non-déterminisme (9), carte demandée absente (2). 
- Offre : sain, identifiant, H200, étiquette, prix, disque ; commande : sain, feu sans R-2802, échéance trop lointaine, commit absent, amorce du commit différente, script absent ; dépense : 2,0 accepté, 2,7 refusé avec destruction annoncée ; destruction : ligne avec `-y`, cas du 14 novembre (sans `-y`, « Aborted. », code 0, absence non prouvée), témoin absent, six instances d'autres sessions refusées comme cibles et admises comme témoins.
- Non jouées (mineur m-1) : offre avec peu de cœurs, peu de mémoire vive ou stockage trop cher ; commande avec prix hors de ]0 ; 1,40] ; feu sans GO-2026-11-14-09 (le feu sans R-2802 est joué, pas l'inverse).

**Gardes de l'amorce en shell** : les blocs extraits (motifs de la course, aucune entrée de 7b, installation bornée 0/5/6, lecture du minimum et du décompte de la course, traces poussées sur COMMIT, minuterie) ont leurs cas sain et artefact. **Les lignes suivantes n'ont ni l'un ni l'autre** (aucun essai ne joue l'amorce au-delà de l'essai local des arguments) :
1. l'appariement code de la partie carte → code d'arrêt (l. 165-167 : 0 continue, 8 → arrêt 8, 9 → arrêt 9, 2 → arrêt 2, autre → 4) : c'est le chemin qui rend les codes 8 et 9 « écrits » ; le test Python prouve que le script rend 8 ou 9, pas que l'amorce les traduit ;
2. la garde « essais en échec ou moins de MIN passés » avec son code 7 (le test n'appelle `arret … 7` que sur un texte écrit à la main dans le banc, pas la condition ; la lecture du décompte, elle, est jouée) ;
3. la garde « les essais ont écrit sous src ou tests » (`git status --porcelain`) ;
4. la garde « branche de sortie déjà présente » (`ls-remote`, code 2 attendu = branche absente) ;
5. l'empreinte du script (`SCRIPT_SHA256`) et « tête ≠ COMMIT » ;
6. `GH_TOKEN` absent, carte autre qu'une A100, torch sans carte, outil absent ;
7. la fenêtre d'échéance ]maintenant ; + 3 h] et l'identifiant d'instance illisible : l'essai local sort (l. 69) **avant** ces deux contrôles, donc ils ne sont jamais joués (la garde de commande côté session couvre l'échéance, pas l'identifiant d'instance, que Vast pose).
Ce sont des lignes simples et leur relecture ne montre pas de défaut ; mais la règle R5 est gelée, et la répétition coûte (jusqu'à 3 USD) pour exercer précisément ces chemins sur la carte.

### (5) Codes d'arrêt 2 à 9 : fermés et écrits — **oui, avec un trou de vocabulaire**

Ensemble réellement émis par l'amorce : **0, 2, 4, 5, 6, 7, 8, 9**. Chaque `arret` écrit au journal « ARRET : motif » puis « fin, code N » et pousse les traces (si la branche neuve est contrôlée). Tout code inattendu de la partie carte (1 par exception non attrapée, 137 par arrêt du système, 2 par erreur d'arguments) tombe dans 2, 4 ou 8 ; aucune sortie n'échappe au tableau. Correspondance au tableau de la note (§ 3) : 2, 5, 6, 7, 8, 9, 4 présents et conformes au texte de l'amorce.
- *Mineur m-2* : le code **3** n'est ni émis ni écrit (la demande « 2 à 9 » est donc vraie par fermeture, pas par présence) ; à dire pour qu'on ne cherche pas un code 3 au journal.
- *Mineur m-3* : les refus d'arguments avant la minuterie (variables, COMMIT, échéance, identifiant d'instance : `exit 2` avec la ligne « REFUS » sur la sortie standard seulement, l. 60-72) ne sont ni dans le tableau ni poussés ; le conteneur finit alors sans minuterie : l'instance reste facturée jusqu'à la destruction par la mère (la note le dit indirectement au geste 5, « rien au journal 15 min après running → geste 9 »). Même comportement que la course ; à citer au tableau.
- *Mineur m-4* : un code 8 vient aussi d'un défaut de la sonde pendant les deux phases qui précèdent le contrôle, mais un arrêt de la sonde (`SondeEnEchec`, sous-classe de l'arrêt de garde) levé **pendant le contrôle carte-processeur** est classé 9 (« contrôle »), non 8 ; le sens du tableau (« contrôle au-delà de 10⁻⁴ ») ne le couvre pas ; sans conséquence sur la sûreté.

## Constats

### Bloquant
Aucun.

### Majeur
- **M-1 (R5, amorce de répétition)** : les sept familles de lignes listées en (4) n'ont ni cas sain ni artefact ; en particulier l'appariement 8/9/2/autre de l'étape 5 et la condition du code 7, qui sont les chemins que la répétition doit éprouver. Couple de correction : **C-1** (voir ci-dessous).

### Mineur
- **M-2 (note à jour)** : `rapport-developpeur-repetition-carte-v1.md` (`a053aa8f…`, non réécrit, R12) porte encore, au § 2 point 4, au § 3 geste 7 et au § 4, « 86 passed, 22 skipped … minimum 86 », « 117 » et l'empreinte `9a01d36a…` du script ; la bonne valeur est 87 / 119 / `229310db…` (note v4). La mère qui suit la note v1 à la lettre attend « 86 » au suivi et peut croire à une erreur. Couple : **C-2**.
- **M-3 (projection recopiée)** : la formule de projection de la garde de débit (`relecture + (n − 20) × médiane × 1,2 / 3600 + 0,6`) est recopiée dans la répétition (constantes importées, formule non appelée) ; la médiane porte sur au plus six apprentissages (la course : les vingt premiers, dix par famille). La projection de la répétition est un ordre de grandeur, déclaré « prudent » ; une dérive de la formule de la course ne serait pas vue. À dire dans le compte rendu.
- **M-4 (durée haute contre échéance)** : le devis donne un haut ≈ 100 min, alors que l'échéance est de 95 min à 1,30 USD/h (86 à 1,40) ; installation à 47 min observée ailleurs + clonage 15 + essais 5 + carte 30 dépasse 95 min. Dans ce cas la minuterie détruit l'instance sans traces poussées : dépense bornée (c'est voulu), mais répétition perdue. Pas un défaut de conformité ; à dire à la mère pour qu'elle fixe l'échéance au plus près du plafond.
- **M-5 (borne)** : `garde_commande` accepte `durée ≤ durée_max`, soit un coût maximal exactement égal à 3,00 USD ; la note dit « < 3 USD par construction ». Écart de fait nul (marge d'un quart d'heure et marge de 0,40), mais la phrase est vraie à l'égalité près.
- **m-1** à **m-4** : voir (4) et (5).
- **Remarques 3a et 3b** : voir (3).

## Corrections demandées (couples)

- **C-1 ↔ M-1** : ajouter à `tests/test_repetition_bbis_v1.py` un essai qui joue, par bash, (a) l'appariement de l'étape 5 de l'amorce sur un faux script de partie carte rendant 0, 8, 9, 2, 1 (attendu : 0 continue ; 8, 9, 2, 4 d'arrêt) ; (b) les gardes 7 (essais en échec ; moins de passés que le minimum), 2 (écriture sous `src`/`tests`), 2 (branche de sortie présente et dépôt injoignable), 2 (empreinte du script, tête ≠ COMMIT) sur un dépôt jetable avec faux `nvidia-smi` et faux `python`, chacune avec son cas sain. Moyen minimal acceptable : marquer ces lignes de l'amorce comme blocs extraits (`# >>> … # <<<`) comme les autres et les jouer comme eux ; **ou**, à défaut, une réserve écrite de la mère avant le feu : « gardes de l'amorce non éprouvées hors essai local : la répétition les éprouve sur carte ». Après correction, l'empreinte de l'amorce change : le lanceur la contrôle au commit, il faut donc un commit neuf, une note de développeur neuve et une relecture courte des seuls blocs déplacés.
- **C-2 ↔ M-2** : une note d'errata du développeur (nouveau nom, R12) qui remplace dans la commande de la mère les valeurs 86, 117 et `9a01d36a…` par 87, 119 et `229310db…` (ou une ligne en tête du geste 7), et qui ajoute m-2 et m-3 au tableau des arrêts.

Aucun refus de permission ni du classifieur dans cette lecture.
