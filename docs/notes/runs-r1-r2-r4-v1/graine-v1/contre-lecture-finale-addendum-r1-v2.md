# Contre-lecture finale neuve (R2) de l'addendum de relance v2 de R1, brouillon 4, et du code 0e2a8871 — v1

- Lecteur : sous-agent neuf, contre-lecteur final de la version à sceller (R2). Il n'a écrit ni le code, ni le texte,
  ni aucune vérification antérieure (ni VG, ni les lectures de conv-audit, ni VI).
- Date (UTC) : 2026-11-02, 15:30 environ (relevé par `date -u`).
- Arbre relu (lecture seule) : `wt-addendum`, branche `prep/r1-relance-addendum-v1`, tête
  `fc43ae79b064eb153e86e2eddb63f9af8dfe34d2`. Différence relue en entier : `9ffab30d..fc43ae79`, trois commits — code
  `0e2a88718f4249e556e159f45f2df38ac304331e`, préalables `82a5ed18`, texte `fc43ae79` —, 60 fichiers.
- Version relue : `prereg/R1-addendum-relance-v2.md`, brouillon 4,
  `a2844644e1d87f22f18c6ae2127bd093085b1e45e91961cb19a850e95fe3f19e` ; configuration `prereg/R1-graine-config-v1.json`,
  `0f300925546d886b8408d137903e711af579abb0d5947b1b88a27da894c4070f` (empreinte canonique
  `f91716bf95c4c4ab07e4155c667539cee9baff38b7ca2639dff0dea167d44db2`).
- Base déjà vérifiée : `9ffab30d` (brouillon 3, `0f4c445c…`, code `31f72147`), rapport VI
  `docs/notes/runs-r1-r2-r4-v1/graine-v1/verification-neuve-vi-v1.md` (`7dfe39c9…`).
- Bornes tenues : rien n'est écrit dans l'arbre (`git status` vide avant et après) ; aucune commande vastai ; aucun
  réseau (git local seulement) ; aucune clé ; aucune poussée ; texte et configuration non scellés (le scellement n'est
  simulé que sur des copies du bac à sable, effacées ensuite) ; de P3, seules des empreintes de fichiers et des comptes
  (fenêtres de fuite, voir point 7) ; consignes jamais ouvertes. Pièces du contre-lecteur : bac à sable
  `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/cl-finale/` (liste et empreintes à la fin).

## Verdict

**Scellable après corrections — texte seulement, aucune ligne de code, aucun essai à refaire.** Liste exacte des
corrections exigées : **CF-01, CF-02, CF-04, CF-05, CF-06** (quelques lignes chacune). CF-03, CF-07, CF-08 et CF-09
sont des remarques, à reprendre si l'on touche ces lignes, sans exigence. Aucun faux « résolu » possible ; les quatre
corrections de code (VI-01, VI-08, VI-10, VI-16) sont justes, éprouvées, et leurs essais échouent sans elles ; les
71 essais de la liste `CIBLES` passent ; toutes les citations vérifiées (86) sont égales aux fichiers ; `problemes()`
ne signale que « Contre-lecture » ; le contrôle d'avant l'installation, extrait du script et rejoué sur une copie, passe
le cas sain (et le plafond exact de 235 min) et arrête les 15 artefacts essayés avant l'installation (code 2) ; la
chaîne extraite rend 3 sur un commit refusé et 1 sur une table v3 sans sceau.

## Constats

### CF-01 — mineur (texte ; dit plus que la mesure) — à corriger

**Preuve.** P-G4, l. 264-265 : « Pour le lot 5, seule la mesure des voisines exactes (lecture du lot de cette cible)
**dit si** les logits sont ceux de P3 ». Or la lecture « fidèle » est un seuil, non une égalité au bit :
`lecture_du_lot` (lot, l. 604-611) rend « fidèle » dès que l'accord des voisines exactes et l'égalité des choix
contraints atteignent `seuil_lecture_lot` = 0,99 ; P-G4 dit lui-même « fidèle au bit, il vaut 1 exactement ». Une
lecture « fidèle » admet donc jusqu'à 1 % de désaccords, et une longueur remplie fausse peut changer les logits de la
cible aux arrondis près sans faire tomber l'accord des voisines sous 0,99. Le lot 5 est celui dont la forme n'est pas
prouvée (`comptes_reels-sortie.txt`, `a2bd318f…` : « à d_max jetons 4 ») et il porte la seule cible à U+FFFD
(`compter_fffd_7-sortie.txt`, `b75658fe…`), donc la seule pour laquelle la cause « budget de balayages dépassé » est
possible (plafond = 16 × nombre de U+FFFD ; P-G2 l'attend pour elle) : c'est la seule cible où une déclaration « non
inversible » par la voie du lot est plausible, et c'est précisément celle de forme non prouvée. `declarer_lot`
(lot, l. 1226-1239) et la ligne « k non résolus » des « Critères » (l. 663) ne lisent pas la forme ; HG-4 range la
preuve par d_max en « descriptif, jamais un arrêt ni une condition de lecture » (choix permis, mais à dire là où il
compte).

**Correction (texte).** (a) P-G4 : « … **indique, au seuil de 0,99 et non au bit,** si les logits sont ceux de P3 … ».
(b) Ligne « k non résolus » (ou G2) : « la liste remise à Lazar porte, pour chaque cible du lot non résolue, la forme
de son lot (prouvée exacte ou non par d_max, P-G4) ; une déclaration « non inversible » d'une cible de forme non
prouvée (lot 5) y est signalée avec la réserve « forme non prouvée » ». La règle gelée et le code restent tels quels.

### CF-02 — mineur (texte ; seuils de VI-11 à valider) — à corriger

**Preuve.** Les noms des champs cités par la ligne « Audit de symétrie » (l. 666) existent dans `agreger_accords`
(cœur, l. 819-835) : `accord_sur_les_pas`, `attendu_graine_independante_sur_les_pas`, `accord_informatif`,
`attendu_informatif`. Sur un pas informatif, le jeton retenu n'est pas l'argmax de p, donc p_k ≤ 1/2 et
`attendu_informatif` ≤ 0,5 (P-G1 le dit : « au plus ≈ 0,5 ») ; la classe « graines validées » exige
`accord_informatif` ≥ 0,90 (`regle_validation`). Sous cette classe, l'écart vaut donc au moins 0,40 > 0,10 : **le
second déclencheur ne peut jamais partir sous « graines validées »**, et la parenthèse « (graines suspectes même si la
classe est « graines validées ») » ne vaut que pour le premier. Le premier, lui, ne part sous cette classe que si
l'accord attendu sur les pas atteint au moins 0,88 (chaque épisode y a un accord ≥ 0,90).
**Validation des valeurs choisies par le correcteur** : + 0,02 sur ≈ 309 797 pas, où l'écart-type d'un accord sous
graine indépendante est au plus 0,5 / √309 797 ≈ 0,0009 : marge large, convenable pour un déclencheur d'audit (non un
arrêt) ; durée cumulée des étapes 0 et 1 sous 5 min : 327 645 jetons à tirer, chacun sur V = 128 256 tirages
exponentiels sur processeur, et au moins ≈ 1 540 passes pleines du 8B sans cache (154 épisodes × 10 actions) — une
durée sous 5 min serait bien suspecte. Valeurs gardées.

**Correction (texte).** Ligne « Audit de symétrie » : rattacher la parenthèse au seul déclencheur « sur les pas » et
écrire que le déclencheur « informatif » ne peut partir que sous les deux autres classes (ou le retirer).

### CF-03 — remarque (règle R5, code ; rien d'exigé avant le scellement)

**Preuve.** `declarations_du_lot` (lot, l. 1251) : `cibles = lot.get("cibles") if lot.get("cibles") is not None else
list(par_e)` — repli écrit dans la docstring, sans trace à l'exécution. Il est inatteignable par un vrai résultat :
`_executer` du lot écrit toujours `"cibles"` (l. 1112) et `construire_table_v3_lot` exige la même `VERSION`. Mais les
quatre cas non résolus de bout en bout de `test_bout_en_bout_jouet_resolution_lot_puis_table_v3` passent par
`_faux_lot` (essais du lot, l. 625-634, l. 806), qui n'écrit pas `"cibles"` : ils éprouvent ce repli, pas le chemin
réel. Le chemin réel (résultat écrit par le module) n'est éprouvé que pour des cibles résolues (essai, `t3` ;
répétition jouet, une cible).

**Correction proposée.** Texte (« Essais », l. 639-642) : « cas non résolus éprouvés sur des résultats du lot
fabriqués (sans `cibles`), passés à la vraie construction de la table ». Code, au prochain commit de code seulement
(addendum v3) : arrêt si `cibles` manque, et `_faux_lot` qui l'écrit.

### CF-04 — mineur (règle R6) — à corriger

**Preuve.** L. 83-84 : l'addendum v1, document qui fait foi « pour les faits de P3 qu'il établit », est cité par chemin
et commit (`72f68fea`) sans empreinte. Son sha256 est le même au commit `72f68fea` et à la tête :
`485acc3a57bf5377cc2d62d8b161eb7b3f669dbeb3ec0bc1b35d260e6f518652` (`verif-citations-sortie.txt`).

**Correction (texte).** Ajouter cette empreinte à la citation.

### CF-05 — mineur (règles R6 et R5) — à corriger

**Preuve.** « Calendrier », l. 590-592 : « répétition jouet … (cas principal …, cas « sans objet », **commit refusé**,
**table sans sceau**, libellé du lot absent, plafond trop bas : chacun avec l'issue attendue) ». Au code cité, seuls le
cas principal et le cas « sans objet » sont versés ; « libellé du lot absent » et « table v2 sans sceau » sont dans
`prevol-final-sortie.txt` (`9d9c1c87…`) ; « plafond trop bas » dans le rapport VI (au code `31f72147`) ; **« commit
refusé » n'a aucune trace versée** (ni chemin ni empreinte). La « Liste d'arrêt » renvoie ce qui n'est pas éprouvé à
« la contre-lecture » : fait ici (point 6 b) — fonctions de chaîne du script extraites telles quelles, module factice,
dépôt distant nu local : sain → code 0 ; crochet qui refuse les commits → code 3, « FIN EN ÉCHEC : commit refusé après
la validation » ; table v3 écrite sans sceau → code 1, « FIN EN ÉCHEC : table v3 arrêtée ».

**Correction (texte).** Dans « Calendrier », citer pour « commit refusé » et « table v3 sans sceau après écriture » ce
rapport et ses pièces (chemin et empreinte, une fois versés), ou écrire « fait au code `31f72147`, trace non versée ;
script inchangé depuis (`da07025f…`) ; rejoué par extraction à la contre-lecture finale ».

### CF-06 — mineur (gouvernance, condition de lancement) — à corriger

**Preuve.** VI-02 est déclaré (« Coût et GO », l. 604-607 ; « Lancement », l. 725-726 : « le devis révisé porté à
Lazar »), mais le texte ne dit pas si le lancement **attend sa réponse**. La ligne GO-2026-11-02-02
(`registres/go.md` au commit `ddfff6e4`, l. 190, relue) annonce « ≈ 1 USD attendu, 2 USD au pire » ; le texte dit
6,2 USD au pire, trois fois plus (dans le plafond de 25 USD, ≈ 10,8 au pire, calcul vérifié : 265 min × 1,40 USD/h
= 6,18 ; 4,6 + 6,2 = 10,8 ; 45-100 min = 1,05-2,33 USD). CLAUDE.md range toute dépense de calcul parmi les nœuds
(« devis par phase ») et interdit de « dépenser sans GO sur devis ».

**Correction (texte).** « devis révisé porté à Lazar **et accepté par lui** (mot consigné dans `registres/go.md` ou
`registres/decisions.md`, cité au lancement) avant la création » ; ou, si la session lit le plafond de 25 USD comme seul
engagement du GO, l'écrire tel quel (« information, sans attente »). La condition doit être univoque.

### CF-07 — remarque (VI-15, formulation)

**Preuve.** L. 571-572 : « Les non résolus restent `non_resolu`, chacun avec la cause écrite » ; « Critères », ligne
« k non résolus » : « chaque non résolu porte sa cause et sa déclaration ». Lu dans la section de la table, cela
contredit la phrase de VI-15 deux lignes plus haut (les causes ne sont pas dans la table).

**Correction proposée.** « … sa cause, écrite au résultat scellé du cœur ou du lot (non dans la table, VI-15) ».

### CF-08 — remarque (devis)

**Preuve.** « Coût et GO », l. 602 : « 71 essais de 9 à 12 min ». Mesuré sur la machine de la session : 13 min 17 s
(`tests-cibles-final.txt`), 12 min 33 s (`repetition-principale-journal.txt`), 12 min 07 s (ce rapport). Par ailleurs
l'amorce coupe à 235 min puis tue 3 min plus tard (`--kill-after=3m`, amorce l. 44) : pire cas ≈ 268 min, 6,25 USD,
non 6,2. Sans effet sur les bornes (la mise en place de 40 min n'est pas coupée à part ; somme 235 = plafond, vérifiée).

**Correction proposée.** « 12 à 15 min » ; « ≈ 6,3 USD au pire » (ou garder « ≈ 6,2 » en citant les 3 min).

### CF-09 — remarque (HG-4, formulation de la preuve)

**Preuve.** L. 212-213 : « aucune ligne approchée n'est à d_max jetons ou moins de fixer la longueur remplie ». Le calcul
cité (`comptes_reels.py`, `1a2e9803…`) compte une action « non prouvée » si et seulement si la longueur d'une ligne
approchée plus son d_max **dépasse strictement** la plus grande longueur des autres lignes (exactes et cible, celle-ci
à ses fins par défaut) ; l'égalité est prouvée exacte, et compter la cible à ses fins par défaut (sa longueur minimale)
garde la preuve conservatrice sous la prémisse du texte (fin non par défaut = un jeton de plus chez P3). Le calcul est
juste ; la phrase peut se lire avec l'égalité.

**Correction proposée.** « si, à chaque action jouée, la longueur de chaque ligne approchée augmentée de son d_max ne
dépasse pas la plus grande longueur des autres lignes (exactes et cible, celle-ci à ses fins par défaut) ».

## Points demandés

### 1. VI-01 à VI-16 : chacun traité comme dit

| VI | Sort annoncé | Constat de la contre-lecture |
|---|---|---|
| VI-01 | traité (code et texte) | Conforme. `declarer_lot` (l. 1226-1239) applique la règle de la ligne k (résolu ; classe ≠ « graines validées » → nœud ; cause du lot « budget de balayages dépassé » **et** lecture « fidèle » de la cible → non inversible ; sinon nœud) ; `declarations_du_lot` (l. 1242-1255) arrête sur cible sans entrée ou entrées contradictoires ; fusion l. 1357-1361 (`declarations_coeur` gardé) ; entrée versée par le lot avec « résolu » (l. 1339). Une cible « non tentée » du lot a le statut `non_resolu` et une cause « durée : … » (`rg.non_tente`, l. 1502-1507) → nœud. Texte : étape 2 (l. 566-569), ligne k (l. 663). Remarque CF-03. |
| VI-02 | déclaré | Conforme sur les chiffres (vérifiés) ; condition de lancement à préciser : CF-06. |
| VI-03 | traité (texte) | Conforme : HG-4 (preuve par d_max), P-G4 égal à `comptes_reels-sortie.txt` (lots 0, 5, 14, 24 : approchées 2, 1, 1, 3 ; strict 0, 3, 0, 0 ; à un jeton 1, 3, 0, 1 dont égalités 1, 0, 0, 1 ; à d_max 0, 4, 0, 0). Remarques CF-01, CF-09. |
| VI-04 | traité (texte) | Conforme (l. 577-579, l. 671-672) ; l'en-tête du script (l. 12-14) dit la même exception. |
| VI-05 | traité (retiré) | Conforme : l. 710 dit que l'étape table ne compare pas le code, ce qui est vrai (`construire_table_v3_lot` n'appelle pas `exiger_meme_code`) ; le lot, lui, compare le code de la validation et de la résolution du cœur (l. 886, l. 910), comme le dit l. 529-531. |
| VI-06 | traité (texte) | Conforme : `exiger_seuil_atteignable` et `exiger_compte_validation` (cœur, l. 1531-1532) viennent après `_modele` (l. 1523), dans `_executer`. |
| VI-07 | traité (texte) | Conforme (l. 462-465). |
| VI-08 | traité (code et texte) | Conforme : arrêt sur manifeste illisible (cœur, l. 1199-1203), essai `test_r3_manifeste_illisible_arrete` qui échoue sur l'ancien code (« DID NOT RAISE ») ; texte l. 390-392 et l. 695-696. Les 45 manifestes `runs/*/manifeste.json` de la tête sont des objets JSON lisibles : la garde plus stricte n'arrêtera pas l'instance sur le dépôt réel. |
| VI-09 | traité (texte et code) | Conforme : lignes du lot des « Critères » (l. 659-661) ; le code lit la lecture de la cible. Mutation (lecture d'ensemble à la place de celle de la cible) : les deux essais échouent (`mutation-lecture-ensemble.txt`). |
| VI-10 | traité (code) | Conforme : `corriges_table_v2` (cœur, l. 1683-1690), essai l. 858-860 ; l'ancien code échoue (`KeyError: 'corriges_table_v2'`). L'essai ne vérifie pas `identifiants_egaux` (champ bien rempli : `detail` le porte pour les 147). |
| VI-11 | traité (texte) | Seuils validés ; formulation à corriger : CF-02. |
| VI-12 | traité (texte) | Conforme : graines décalées → « méthode non transposée » (essai du cœur, l. 862-868). |
| VI-13 | traité | Conforme : compagnons de C-6 (4) et des 22 pièces, tous conformes ; citations égales (point 4). |
| VI-14 | traité (texte) | Conforme : le script ne journalise que CUDA et la carte (l. 256, l. 278) ; le module écrit CUDA, cuDNN et carte (`reserves_environnement`). |
| VI-15 | traité (texte) | Conforme au code (voie du cœur : `lecture_validation` à `classe` ; voie du lot : `classe_validation`, `lecture_lot`, `validation`, `lectures_lot_par_episode`). Formulation voisine : CF-07. |
| VI-16 | traité (code) | Conforme : le préparateur se place à la racine du dépôt de répétition (essai/finally) ; `repetition.sh` refuse un répertoire courant qui contient `donnees/`. |

### 2. Code corrigé : essais qui échoueraient sans lui, aucun repli silencieux

Essais neufs de la tête lancés sur le code de `31f72147` (copie du bac à sable : `src` et `scripts` de `31f72147`,
essais de la tête) : **4 échecs sur 4** (`essais-ancien-code.txt`) — `test_declaration_finale_des_cibles_du_lot`
(`AttributeError` : pas de `declarer_lot`), `test_bout_en_bout_jouet_resolution_lot_puis_table_v3` (les 4 cibles
portent « non résolu par la méthode : nœud » au lieu de « résolu »), `test_r3_manifeste_illisible_arrete` (« DID NOT
RAISE »), `test_bout_en_bout_jouet_validation_resolution_table` (`KeyError: 'corriges_table_v2'`). Le correcteur en
rapportait 3 (sans l'essai de VI-10) : concordant. Le jouet a bien 4 cibles : les quatre cas non résolus de VI-01
sont tous joués (la troncature `attendu[:len(nr)]` ne retire rien). Mutation VI-09 détectée (point 1). Aucun repli
silencieux dans les corrections, hors celui de CF-03 (inatteignable par un vrai résultat). VI-16 n'a pas d'essai
automatique : éprouvé par la répétition finale versée.

### 3. Liste `CIBLES` : 71 passés, égal à « Tests attendus »

Les sept fichiers de `CIBLES`, commande du script (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests python -m pytest -q
-p no:cacheprovider --color=no …`), tokeniseur de la révision de P3, copie de la tête : **« 71 passed in 727.01s
(0:12:07) », code 0, sortie d'erreur vide, aucun sauté** ; la ligne satisfait le motif du script pour 71
(`tests-cibles-cl.txt`). Note : ces essais lisent des fichiers du dépôt en chemin relatif (`donnees/T0.7-…`,
`docs/sources/invites-2606.08892-v1/`) ; mes deux premiers lancements, dans une copie partielle, ont échoué pour cette
seule raison (traces gardées : `tests-cibles-cl-essai1-sans-donnees.txt`, `tests-cibles-cl-essai2-sans-invites.txt`,
`essais-ancien-code-essai1-sans-invites.txt`, sans valeur de preuve). Le script lance les essais depuis la racine du
clone complet : sans objet pour l'instance.

### 4. Citations du texte égales aux fichiers au commit

`verif-citations-sortie.txt` : 86 vérifications, toutes égales — commit du code (seule occurrence ; arbre gelé
identique de `0e2a8871` à la tête, `exiger_code_cite` rend `0e2a8871…` sur l'arbre) ; les 9 empreintes de code au
commit cité et à la tête (compagnons conformes, `rejeu_activations_v3.py` sans compagnon comme déclaré) ;
configuration (`0f300925…` au commit cité et à la tête ; 42 clés ; canonique `f91716bf…` recalculée, et par
`empreinte_config` du module) ; 22 pièces versées sous `graine-v1/` (empreinte citée = fichier = compagnon) ; table v2
`5f6cf489…` à la tête et à `cdca33bb`, compagnon ajouté au commit `82a5ed18` et conforme ; résultat de C-6 et les
compagnons de `resolution_c6_v1.py`, `journal-c6-v1.out`, `journal-c6-v1.err` (ajoutés à `82a5ed18`, conformes) ;
parent `80c85a00…` ; manifeste de P3 `3f21774c…` ; enquête `377101ec…` ; brouillons 3, 2, 1 (`0f4c445c…`,
`d4617ea8…`, `7915a3d6…`) à leurs commits ; ligne de GO (l. 190 au commit `ddfff6e4`). Seul manque : l'empreinte de
l'addendum v1 (CF-04). Trois commits terminés par les deux lignes d'attribution demandées.

### 5. `problemes()` et libellés lus par le script

`problemes()` : `['section vide ou à remplir : Contre-lecture']` ; sur une variante en mémoire où seule l'entrée
« Contre-lecture 1 » est remplie (deux empreintes) : `[]` (`problemes-sortie.txt`). Libellés lus par le script et les
modules, chacun une occurrence sur une ligne : « Tests attendus » (`71`), « Chemin de la configuration de la résolution
à graine », « Configuration de la résolution à graine (empreinte canonique) », « … , lot fidèle (empreinte
canonique) » (chacun suivi de la canonique exacte), « Commit du code d'analyse », « Entropie ». « Révision du modèle »
n'est pas lu par ces modules.

### 6. Script d'instance : arrêt avant l'installation sur artefact, passage sur le cas sain

**(a) Contrôle d'avant l'installation** (`rejeu-avant-install/`) : lignes 55-81 et 114-188 du script de la tête
extraites telles quelles (le bloc 114-188 est comparé octet à octet au script) ; lignes 83-112 (clonage, `git
ls-remote` : réseau) omises ; rejoué dans des copies (texte et configuration copiés puis scellés **dans la copie
seulement** ; pièces de P3 par liens symboliques vers l'arbre, jamais écrites), avec un Python sans aucune bibliothèque
tierce (rien n'est installé à ce stade). Résultats (`resultats-cas.txt`) :

| Cas | Code | Motif journalisé |
|---|---|---|
| sain | 0 | « addendum lu : 71 tests attendus ; … canonique f91716bf95c4, citée sous ses deux libellés … 7 pièces : présentes et scellées ; table v3 … absente ; budgets : 40 + 50 + 50 + 5 + 70 + 15 + 5 = 235 min ≤ plafond 235 min » |
| table v2 sans sceau | 2 | « empreinte compagnon R1-table-tokenisation-v2.json.sha256 absente : arrêt avant l'installation » |
| canonique fausse sous le libellé du lot | 2 | « … lot fidèle (empreinte canonique) » absent, cité plusieurs fois ou ≠ empreinte canonique |
| canonique fausse sous le libellé du cœur | 2 | idem, libellé du cœur |
| libellé du lot absent | 2 | idem, libellé du lot |
| libellé du cœur cité deux fois | 2 | idem, libellé du cœur |
| « Tests attendus » cité deux fois | 2 | « nombre de tests attendus introuvable ou cité plusieurs fois » |
| « Tests attendus » sans valeur entre accents graves | 2 | idem |
| chemin de la configuration cité deux fois | 2 | « chemin de la configuration introuvable ou cité plusieurs fois » |
| texte sans sceau | 2 | « préenregistrement … ou son sceau absent » |
| texte modifié après scellement | 2 | « sceau non conforme (… empreinte 914bd1ca… ≠ scellée a2844644…) » |
| configuration sans sceau | 2 | « configuration … ou son sceau absent » |
| empreinte de pièce citée fausse (table v2 dans la configuration) | 2 | « empreinte 5f6cf489eb97 ≠ empreinte citée par la configuration (table_tokenisation_sha256) » |
| table v3 déjà présente | 2 | « table v3 … déjà présente au commit : R12 » |
| plafond 234 min | 2 | « budgets : … = 235 min > plafond de l'amorce 234 min » |
| plafond 235 min | 0 | passe |
| répétition jouet demandée sur la configuration réelle | 2 | « mode 'reel' de la configuration ≠ répétition jouet » |

**(b) Chaîne d'exécution** (`rejeu-chaine/`, pour CF-05) : lignes 55-81, 196-251 et 356-465 extraites telles quelles
(`etape()` comparée octet à octet), module remplacé par un module factice, dépôt distant nu local : sain → 0 ; sain
avec table → 0 (table scellée, committée, poussée) ; commit refusé → **3** ; table v3 écrite sans sceau → **1**.

### 7. Ce qui manque

1. Les corrections CF-01, CF-02, CF-04, CF-05, CF-06 (texte seul ; le commit du code, les empreintes de code, la
   configuration et « Tests attendus » ne changent pas ; aucun essai à refaire). Vérifier ensuite par la différence
   brouillon 4 → brouillon 5 qu'aucune autre ligne n'a changé, et le consigner dans l'entrée « Contre-lecture 1 ».
2. Remplir l'entrée « Contre-lecture 1 » (identifiant ; brouillon relu `a2844644…` ; chemin et empreinte de ce rapport,
   une fois versé sous `graine-v1/` avec son compagnon ; traitement de CF-01 à CF-09). **N'y recopier aucun des six
   libellés lus par le script et les modules** (« Tests attendus : `…` », « Chemin de la configuration … : `…` », les
   deux libellés de la canonique, « Commit du code d'analyse : `…` », « Entropie : `…` ») : un doublon arrête le script
   avant l'installation (point 6 a).
3. Sceller le texte et la configuration ; le compagnon de la configuration doit porter le nom de base
   `R1-graine-config-v1.json`.
4. Devis révisé à Lazar, avec la condition de CF-06 ; relevé des dépenses (≈ 4,6 USD) revérifié avant la création.
5. Lecteur neuf de conv-audit sur la version scellée (condition de lancement déjà écrite).
6. Pour information : `verifier-arbre` sur la branche (`verifier-arbre-wt.txt`) signale 70 fichiers non scellés, tous
   antérieurs à cette différence (dont l'addendum v1, déclaré non scellé, et le texte et la configuration à sceller) ;
   aucune pièce citée par ce texte n'y figure hors ces trois. La routine de reprise le verra.
7. Fuite : aucune des 22 pièces versées ni le texte ne contient un extrait de 40 caractères d'une des 2 400 actions de
   P3 (`fuite-textes-p3-sortie.txt` : 0 partout ; comptes seulement).

## Pièces du contre-lecteur (bac à sable `cl-finale/`, sha256)

| Pièce | sha256 |
|---|---|
| `scripts/verif_citations.py` | `78705c9dbbc4169703da5eaa1ae6e54292d70e7e2ce674c473d14a8c3bbbedd2` |
| `verif-citations-sortie.txt` | `fdf59853a2889d437ffe240f636ad6d2c68c1993e4fdee9efdf058b6e690a69b` |
| `scripts/fuite_textes_p3.py` | `4109b2f213b6598e5d978d8f344d45092983a0eb2fb5e57b035e630950856f26` |
| `fuite-textes-p3-sortie.txt` | `0f60c292fe325d090fef1220ce3d69af6eeee68bb4e47b2ded7e9b174d1995f4` |
| `scripts/problemes_rempli.py` | `9d4ec42ea9c8d1b272fa72e173059008cb471ef8c72408b1aad2a0008d9cdf59` |
| `problemes-sortie.txt` | `a865bb37efcb6a7509af9665ae91c7c0003577250ccad38289092f0266367434` |
| `rejeu-avant-install/avant_installation_extrait.sh` | `e5c5ccfaf1b283d5e5180839b8fd4b9f308ca1d75473caeb93ea8141966b5443` |
| `rejeu-avant-install/cas.sh` | `2f2bc563ac58318063e4a83eaeb42833badadfa3f52a2c0e06ae3880b78e0d32` |
| `rejeu-avant-install/resultats-cas.txt` | `dc7f7f70aa25836a5a81a337dc310d37f8c423ecd943326b028fcebe097afa41` |
| `rejeu-chaine/chaine_extraite.sh` | `79f68d6c9d148ed0ffdeefdefc24fe0b2d7e6317b2424fe314c730aa9dc08c0f` |
| `rejeu-chaine/modfaux/faux_module.py` | `e56e55274db72b1b4af5af5b4f3003946f725a0dfb69d22b9f5b966d1035157e` |
| `rejeu-chaine/cas.sh` | `1b6ca12b654361b702ee270b9e9255c2f81c1b6343b2f19b3336a253fad22b34` |
| `rejeu-chaine/resultats-cas.txt` | `cbea7436402080777fecf7c2c66584dab39cd027ec484037cb88a78308945411` |
| `tests-cibles-cl.txt` | `11c2c7972f375b01c0306ffa1720dea3333a8a6ea57371a3f025e811fbab8767` |
| `tests-cibles-cl-debut.txt` | `a4747725622c9daaa9c79d219ee8eb571082b339891970d8a71842284f2244dd` |
| `essais-ancien-code.txt` | `a39de8d8179ebf46e44311e315b82756a58427dbaa3fdacbf7f51350a4a52a5e` |
| `mutation-lecture-ensemble.txt` | `e1b8ab781b6f09c4d680ad166118504dcffd8ccd33a240eceed0c0cac2997e08` |
| `verifier-arbre-wt.txt` | `b6f0024edc900507578ca96ca6e484c1adc7bca602300d1d3200a47cd94e7c6b` |
| `texte-b4.md` (copie du brouillon relu) | `a2844644e1d87f22f18c6ae2127bd093085b1e45e91961cb19a850e95fe3f19e` |
| `tests-cibles-cl-essai1-sans-donnees.txt` (copie partielle, sans valeur de preuve) | `93a8247ff4986fd632a7fea912769f2dfe61855a82e44ff4183a5afb299810ca` |
| `tests-cibles-cl-essai2-sans-invites.txt` (idem) | `838e522469cef7196ced8f89c34d01c8b3d1d6ed693ddbc843bff49fd4d216fb` |
| `essais-ancien-code-essai1-sans-invites.txt` (idem) | `e0f2394274041177d8390b3438c4a004bb533404aa41c0e68505a2bc919aaadc` |

Copies de travail effacées après usage (reproductibles par `git archive`) : `copie-head/` (`src`, `tests`, `scripts`,
`runs`, table v2, `donnees/T0.7-…`, `docs/sources/invites-2606.08892-v1/` de `fc43ae79`), `copie-ancien-code/` (`src`
et `scripts` de `31f72147`, le reste de `fc43ae79`), `copie-mutation/` (copie de la tête, une ligne changée à
`declarations_du_lot`, l. 1247). Les scripts `cas.sh` les supposent recréées.
