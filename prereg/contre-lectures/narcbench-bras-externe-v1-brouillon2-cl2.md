# Contre-lecture 2 du texte court du barreau 7 (bras externe NARCBench) — brouillon 2 — v1

- **Contre-lecteur** : sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`), autre modèle que le rédacteur (Claude Opus 5.5), même
  famille (N-052, règle R2). Je n'ai écrit ni ce texte, ni le code du bras externe, ni la contre-lecture 1 ; je ne serai ni lecteur ni
  juge du verdict. Travail du 2026-11-18, de ≈ 17:58 à 18:05 UTC (`date -u`). Mandat : `docs/notes/narcbench-8b-v1/mandat-contre-lecture-2-texte-court-v1.md`
  (empreinte vérifiée par son compagnon : conforme).
- **Objet relu** : `prereg/narcbench-bras-externe-v1-brouillon2.md`, `7bb21dc0bec7a5fcbff41c84ee2554966e7ddc0acf8703cf7fe8f78d224acb02`
  (compagnon vérifié : égal). Les numéros de ligne ci-dessous sont ceux de ce fichier.
- **Aucune donnée réelle, aucun score** lus ou calculés. Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Rien commité, rien poussé,
  rien écrit sous `registres/`. L'arbre `/home/user/narcbench-externe-v2` n'a été que lu (voir « Têtes du code lues »).

## Verdict

**Scellable après corrections.** Aucun bloquant. La contre-lecture 1 est traitée conformément au tableau (aucune remarque oubliée ; les
changements hors tableau sont tous déclarés ou découlent d'une remarque, six sont à ajouter au tableau : § 1). Les chiffres de l'article ajoutés
ou déplacés sont exacts. Le calcul de la réserve de l'intervalle se rejoue à l'identique. **Cinq majeurs** : (M1) la section de configuration
canonique n'est pas lisible par le code que le développeur vient de committer (refus constaté en l'essayant) ; (M2) les comparaisons de la règle
d'une cellule ne disent pas leur tolérance d'arrondi, alors qu'une aire moyennée peut tomber à 10⁻¹⁶ de la marge ; (M3) la phrase « même une
reproduction exacte donnerait le plus souvent non tranché » est trop générale ; (M4) la réserve « reproduit à tort » n'est pas dans les phrases
gelées que lit le lecteur du verdict ; (M5) la liste des écarts texte-code est exacte mais incomplète (cinq absents) et le code committé depuis
contredit le texte sur sept points.

## Têtes du code lues

- Base de la liste des 18 écarts : commit `70cb77b848da03f044d676ce04fc79c3c24b371d` (lu par `git show`, empreintes des six fichiers cités par le
  texte recalculées : **toutes égales**, `lecture_externe_v2.py` `a4ee0098…`, `externe_v2.py` `0bf5f73c…`, `chargeur_externe_v1.py` `9193b787…`,
  `externe_v1.py` `69dfdd24…`, `statistiques_v1.py` `fa9970d7…`, `requirements-cpu.txt` `d236a393…`).
- **Pendant ma lecture, le développeur a committé** `3950ee93de8cb9316bf23f844d66f96b75b42c00` (« corrections de la contre-lecture du code (M1, M2, M3)
  et gardes de la liste d'arrêt »), puis rouvert des modifications non committées dans `externe_v2.py`. J'ai lu les deux commits `70cb77b8` et
  `3950ee93` (par `git show` et `git archive` vers mon dossier temporaire), **jamais l'arbre de travail**. Ce qui suit dit à chaque fois sur quelle tête.

## 1. Les remarques de la contre-lecture 1 : traitement et changements hors tableau

J'ai rejoué `diff` entre les brouillons 1 et 2 (1 010 lignes) et lu chaque différence contre le tableau de la section « Contre-lecture ».

**Traité comme dit, vérifié dans le texte** : B1 (lecture déclarée de la règle R9 : graines 0 à 9 constantes de la recette ; constat « dix graines ≈ une » ;
noms des tâches `<modèle>/familles/c<couche>/<famille>/<tâche>` = ceux de `externe_v2.cle_graine_famille` au commit `70cb77b8`) ; B2 (augmentation
« papier », citation de la p. 30 exacte) ; B3 (moyenne des aires par pli) ; B4 (registre propre, trois clés, six lignes de configuration, ligne
`Entropie :`, garde « déjà jouée » n° 4, commit n° 6, registre borné n° 3) ; M1 (trois lignes R3, R4, R5 : exhaustives et exclusives, voir ci-dessous) ;
M2 (probabilités du « oui » et du « non », réserve de l'intervalle : les produits 0,573² = 0,33, 0,783² = 0,61, 0,193² = 0,04, 0,771² = 0,59,
0,978² = 0,96 se recalculent) ; M3 (18 écarts ; voir § 5) ; M4 (plus de section « Points ouverts » ni « Marqueurs » : il reste exactement deux
marqueurs, ligne 258 et ligne 770) ; M5 (seuil de 10 %, liste d'arrêt n° 9) ; les mineurs m-R7-1 à 4, m-I-1 à 3, m-P-1, m-C-1 à 4, m-1 à 7.

**Lignes R0 à R5 de la réponse au barreau** : énumération refaite par moi sur les cas (témoin ≠ reproduit ; huit reproduit ; huit non reproduit ;
au moins un reproduit ; au moins un non reproduit ; sinon). Exhaustive et exclusive par l'ordre. Symétrique : « oui » et « non » exigent la même
force de preuve sur les huit cellules. Rien à corriger.

**Changements hors tableau, à déclarer (mineurs, un par ligne)** :
- m-D1. L'unité de rééchantillonnage de l'étage des comités passe du « scénario » (brouillon 1) au **pli** : conséquence de B3, jamais dite. Après :
  ajouter au tableau une ligne « B3 : unité de rééchantillonnage des comités = pli gardé ; effectif lisible des comités = au moins 10 plis gardés ».
- m-D2. Scores non finis : « non lu : garde » (brouillon 1, n° 10) devient **arrêt** (n° 12), et la phrase gelée devient « non lu : garde (scores
  constants) » au lieu de « garde (nommée) ». Justifiable (le paquet gelé refuse déjà les scores non finis) mais non déclaré. Après : une ligne au tableau
  « garde des scores : non finis → arrêt (le paquet gelé l'impose) ; constants → cellule « non lu » ».
- m-D3. Ligne « garde de reproduction du code rapportée telle quelle, sans valeur de lecture » (section « Métrique ») : vient de la contre-lecture du code
  (m10), absente du tableau de la contre-lecture 1. Après : une ligne au tableau.
- m-D4. Sixième clé `texte :` de la configuration (la contre-lecture 1 en demandait cinq) : choix de la mère, à nommer au tableau.
- m-D5. Le brouillon 1 attribuait un plancher « pli par pli » aux comités et le retire ici : déclaré dans « choix du rédacteur » (§ 2), mais le tableau
  de la contre-lecture 1 n'en parle pas. Rien d'autre à faire.
- m-D6. Statut : la copie scellée dira encore « brouillon 2 … Texte scellé à venir » alors que la mère n'inscrit « rien d'autre » que l'entropie et l'entrée
  de la contre-lecture 2. Avant : « Statut : brouillon 2 du 2026-11-18 … Texte scellé à venir : … » → Après : écrire dès maintenant un statut vrai aux deux
  états (« Statut : texte court du barreau 7, version 1 ; les deux inscriptions de la mère au scellement sont l'entropie et l'entrée de la contre-lecture 2 »).

## 2. Les choix du rédacteur hors des remarques

Pour chacun : déclaré ? justifié sans regard à un résultat ? échappatoire possible (règle R3) ?

| choix | déclaré | justifié | échappatoire | jugement |
|---|---|---|---|---|
| perceptron retiré | oui (tableau, P6) | oui : absent du code v2, « descriptif seulement » au brouillon 1 | aucune : retirer une famille descriptive ne peut favoriser aucune issue | accepté |
| une graine d'apprentissage par couche pour nos familles | oui | oui : comme le code v2 ; la moyenne porte sur les couches ; sur classes égales dix graines ne valent qu'une | aucune | accepté |
| lecture par agent = celle de `nos_familles_v2` | oui | oui : descriptive, sans état | les phrases de la grille D viennent du code, pas du texte : elles ne sont pas gelées ici. Sans valeur de lecture déclarée ; l'empreinte de `statistiques_v1.py` entre dans la fiche du code (tous les fichiers du dossier y sont) | accepté ; mineur : dire que la fiche gèle ces phrases |
| comités sans plancher ni placebo ; Mahalanobis à l'étage stéganographique seulement | oui | raison non écrite (coût de 17 plis × couches × 200 directions ?) | aucune : lecture secondaire « sans effet sur la réponse », phrases « sans plancher » déjà prévues | accepté ; **ajouter une phrase de raison** (« coût ; lecture secondaire ») |
| scikit-learn absent ou autre → refus avant toute lecture | oui (n° 7) | raison non écrite. Raison valable : la lecture n'a qu'un coup (liste d'arrêt n° 4) ; un témoin « non lu » brûlerait ce coup et la réponse serait R0 « non tranchée » à cause d'un oubli d'environnement ; un refus avant l'ouverture ne coûte rien et ne révèle rien | aucune : la version est fixée avant tout résultat (1.9.1) et le refus tombe avant l'ouverture des activations | accepté ; **écrire la raison en une phrase**. Le code committé à `3950ee93` fait l'inverse (§ 5, A25) |
| mémoire insuffisante → arrêt, nœud | oui (n° 11) | oui : une famille « non lue pour mémoire » serait une porte de sortie sélective | aucune | accepté, **mais coûteux** : l'arrêt tombe après l'ouverture et brûle le coup. Proposition : une garde **avant** l'ouverture (« mémoire disponible au moins égale à l'estimation écrite par le code pour la plus grosse famille ; refus sinon »). Majeur ? Non : mineur, la mère peut le décider au registre |
| refus consignés par la mère, sans journal du code | oui | oui (simplicité) | aucune | accepté ; **le code committé tient pourtant un journal** (A23) : à trancher |
| relance permise avant l'ouverture, nœud après | oui | oui : avant l'ouverture rien n'est lu qui dépende d'un résultat | cherché : changer une option (verrouillée par la configuration), un commit (la ligne de code ne se réécrit pas : nœud), un fichier de données (empreintes), la version de scikit-learn (fixée) : aucune marge dépendant d'un résultat. Seule ambiguïté : « avant l'ouverture » est défini par le texte comme avant l'ouverture des activations, mais le code lit déjà les métadonnées (comptes d'exclusions, formes) avant le manifeste ; ces lectures ne portent aucun score, elles sont déclarées | accepté ; mineur : une phrase « les métadonnées sont lues avant l'ouverture ; aucune n'est un score » |
| noms des tâches de graines nouvelles | oui | oui | aucune : une tâche par tirage ; le plancher par couche de nos familles sert à la fois la lecture par agent et les cellules (même tirage, même objet) : dire « un seul objet, deux usages » | accepté ; mineur |

## 3. La réserve de l'intervalle : calcul rejoué, lisibilité

**Rejeu** (données simulées seulement ; script `prereg/pieces-narcbench-bras-externe-v1/puissance-regle-v1.py`, compagnon vérifié ; fonction `simuler`
importée, graine et clé de dérivation de la grille) : publié 1,00, aire vraie 0,97 → **reproduit 0,185 / non reproduit 0,002 / non tranché 0,813,
identique à la sortie scellée**. Même point, autre graine (777, 2 000 simulations) : 0,182. Les 0,060 et 0,102 à l'aire vraie 0,95 sont aux lignes
scellées. L'affirmation « un intervalle exact laisserait au plus 0,025 à la marge » est exacte (intervalle percentile bilatéral à 95 % : 2,5 % de chaque côté).
**Point nouveau, non scellé** : à l'**écart**, l'aire vraie égale à sa marge (0,96, publié 0,99) donne ≈ 0,15 (graine 777, 2 000 simulations) ; le texte
ne donne la valeur que pour le pic. Pour une réponse « oui » (douze cellules), la probabilité de sortir à tort quand toutes les aires vraies sont à la
marge est au plus 0,185 × 0,185 ≈ 0,034 si les deux modèles sont indépendants (hypothèse du texte), au plus 0,185 sinon.

**Le texte le déclare-t-il assez clairement pour un lecteur du verdict ? Non.** La réserve est dans la section « Seuil » (troisième phrase d'un point à
quatre chiffres), dans la table de « Puissance » et en Frontière n° 6. Les phrases gelées que le lecteur des issues recopie (ligne C2, ligne R1)
disent seulement « reproduit » et « oui : notre chaîne reproduit le résultat positif publié ». Le lecteur lira « oui » sans la réserve. Voir M4.

## 4. Configuration canonique de la commande : lecture ligne à ligne

**Ce qui est conforme** : exactement six lignes de forme `clé : valeur` (lignes 253 à 258), chacune **seule** de sa clé dans tout le texte (recherche des
motifs `^clé :` : une occurrence chacune) ; `Entropie : <<ENTROPIE_NARC_EXT>>` est la seule ligne `Entropie :` et reste le seul marqueur de cette
section (l'autre marqueur est l'entrée de la contre-lecture 2, ligne 770). Cohérence des noms : `SCELLEMENT-NARC-EXT` (11 occurrences), `CODE-NARC-EXT`
(13), `LECTURE-NARC-EXT` (6) ; aucune forme `NARCEXT` ; le chemin `registres/narcbench-externe-v1.md` (4 occurrences) et
`registres/code-narc-ext/CODE-NARC-EXT-v1.json` (2) ; le résultat `externe-narcbench-v2.json` (3) ; le suffixe `narc-externe-v2` (5). Validateur
`controle_ia.prereg.problemes` : exactement les deux manques admis (« marqueurs de gabarit restants » ; l'entrée « contre-lecture 2 sans ses deux
empreintes »), rien d'autre.

**Majeur M1 — la section n'est pas lisible par le code committé.** J'ai copié le brouillon dans mon dossier, remplacé la ligne d'entropie par un entier
de 19 chiffres, et lancé la commande de contrôle préalable du code **à la tête `3950ee93`** (`verifier-texte`, qui ne lit que le texte) :
**refus, 24 fautes** : (a) la section ne doit contenir que des lignes `clé : valeur` ; la mienne contient un paragraphe d'introduction, deux clôtures
```` ``` ````, et sept puces explicatives (dont les lignes de continuation) ; (b) la clé `texte` est inconnue du code (il n'attend que `augmentation`, `couches-familles`, `run-id`,
`registre` et la ligne `Entropie`). En outre deux contradictions internes au texte :
- (c) le texte dit que le code refuse « toute option de la commande qui diffère » de la configuration ; or l'option `--run-id` vaut une date réelle
  (`20261119-103000-narc-externe-v2`) et la ligne vaut le modèle `AAAAMMJJ-HHMMSS-narc-externe-v2` : elles diffèrent toujours. Le code lit la ligne
  comme une **forme** ; le texte doit le dire ;
- (d) « Entropie : entier d'au moins dix chiffres » : le code exige au moins 2³² = 4 294 967 296 ; un entier à dix chiffres entre 10⁹ et 4,29·10⁹
  serait accepté par le texte et refusé par le code.

Avant (lignes 244-276) → Après, **version recommandée (le texte change, le code garde son analyseur strict)** :
```
## Configuration canonique de la commande

augmentation : papier
couches-familles : bande
run-id : AAAAMMJJ-HHMMSS-narc-externe-v2
registre : registres/narcbench-externe-v1.md
texte : prereg/narcbench-bras-externe-v1.md
Entropie : <<ENTROPIE_NARC_EXT>>

## Notes de la configuration canonique

(toute la prose et les puces actuelles, avec trois changements : « `run-id` : la ligne donne la **forme** ; l'option doit avoir la même forme et le
même suffixe, avec une date et une heure valides » ; « `Entropie` : entier d'au moins 2³² (4 294 967 296), donc d'au moins dix chiffres et plus
grand » ; « la clé `texte` est comparée à l'option `--texte` et à la ligne `SCELLEMENT-NARC-EXT` »)
```
Si la mère préfère garder la section telle quelle, c'est au code d'accepter la prose et la clé `texte` : dans les deux cas **un écart de plus** entre
texte et code (A19 ci-dessous) à fermer avant la ligne `CODE-NARC-EXT`. Le code refuse en sécurité (aucun risque silencieux) : c'est une
affaire de cohérence, pas de danger ; d'où « majeur » et non « bloquant ».

## 5. La liste des 18 écarts texte-code

**Exactitude de la liste contre `70cb77b8`** : les dix-huit écarts sont **exacts** (chacun vérifié par lecture du code : 1 clés lues ; 2 registre libre,
chemin absolu accepté ; 3 aucune garde « déjà jouée » ; 4 commit non comparé ; 5 options non comparées, entropie en sous-chaîne, identifiant non contraint ;
6 transfert non refusé ; 7 version de scikit-learn consignée ; 8 exclusions sans seuil, agent sans trois lignes compté ; 9 deux colludeurs et mode d'un même
épisode non vérifiés ; 10 pas de repli de Cholesky ; 11 scores constants non détectés ; 12 `NaN` possibles ; 13 à 16 cellules, intervalle, plancher et
placebo des cellules, lecture secondaire des comités absents ; 17 règles C et T absentes ; 18 tâches de graines nouvelles absentes). Les « choix qui suivent
le code » sont aussi exacts (augmentation, recette, graines, `nos_familles_v2`).

**Majeur M5 — la liste est incomplète : cinq absents** (contre `70cb77b8` ; aucun n'est fermé à `3950ee93`) :
- **A19** (comptes structurels, plan d'analyse n° 3) : épisodes par étage, modèle et condition ; domaines et plis gardés par modèle ; sabots ; lignes
  d'apprentissage par classe ; comparaison des identifiants d'épisodes entre les deux modèles (« le 70B lit-il ses propres textes ? ») : **aucune de ces
  sorties n'existe** dans le code (`groupes` ne rend que `agents_differents_de_4` et `lignes_par_agent`). Le texte la promet « écrite au résultat ».
- **A20** (liste d'arrêt n° 8, colludeurs) : « épisode de collusion sans exactement deux colludeurs, ou témoin avec un colludeur » : l'écart 9 ne cite que
  `nos_familles_v2` ; or le chemin du témoin de recette (`reproduire_helios_v2`) ne vérifie rien (`exiger_roles_episodes`, committé à `3950ee93`, n'est
  appelée que par `nos_familles_v2`). Après : écart 9 « pour toutes les procédures, témoin de recette compris ».
- **A21** (liste d'arrêt n° 11, mémoire) : absent de la liste ; à `70cb77b8` aucun traitement (une `MemoryError` sortirait en trace) ; à `3950ee93` le code
  rend « non lu : garde (mémoire) » **par famille**, contre le texte (arrêt, nœud).
- **A22** (liste d'arrêt n° 12, scores) : le texte dit « non lu : garde (scores constants) » et « non finis → arrêt » ; le code rend « garde (scores
  dégénérés) » et traite les non finis comme constants.
- **A23** (journal) : le texte dit « le code ne tient pas de journal » (n° 3) et « n'écrivent rien » (plan d'analyse n° 2) ; le code committé écrit
  `registres/narcbench-externe-v1.md.ouvertures.md` (lignes `REFUS-NARC-EXT`, `OUVERTURE-NARC-EXT`, `ARRET-NARC-EXT`) et salit l'arbre jusqu'à son commit.
  Le texte ou le code change ; recommandation : **le code garde son journal et le texte le dit** (un refus sans trace est pire), en ajoutant « le journal
  est committé avant toute relance ».

**Écarts nouveaux contre la tête `3950ee93`** (le code a été corrigé sur la base du brouillon 1 et de la contre-lecture 1, pas du brouillon 2 ; le texte
fait foi, c'est donc le code qui s'aligne, sauf décision contraire de la mère) :
- **A24** registre : le texte dit « toute autre clé au registre → refus » (n° 3, règle d'ouverture) ; le code **ignore et compte** toute autre clé bien
  formée et ne refuse que celles aux segments `NARC-EXT`.
- **A25** scikit-learn : texte, refus avant toute lecture ; code, « témoin de recette non lu : garde (scikit-learn) », sans arrêter. Les deux textes
  de comportement sont incompatibles ; le texte du rédacteur est préférable (voir § 2).
- **A26** commit : le texte dit « commit exécuté = commit de la fiche » (n° 6, règle d'ouverture, plan n° 2 « arbre propre au commit de la fiche ») ; le code
  accepte le commit de la fiche s'il est la tête **ou un ancêtre** et compare le **paquet exécuté** fichier pour fichier (règle DF-02 de T0.7). Le code est
  plus sûr ; proposition de texte : « paquet exécuté égal, fichier pour fichier, à `src/controle_ia/` du commit de la fiche ; ce commit est la tête ou un
  ancêtre ».
- **A27** configuration : voir M1 (section, clé `texte`, entropie à 2³²).
- **A28** exclusions : le texte classe le n° 9 **après** l'ouverture (nœud) ; le code les calcule sur les métadonnées **avant** le manifeste (refus,
  relance possible). Sans effet sur le résultat (mêmes métadonnées, même comptes) ; dire dans le texte « n° 9 : calculé sur les métadonnées, avant le
  manifeste ; un arrêt ici est un refus, une relance reste un nœud ».
- **A29** numérotation : les messages et commentaires du code citent les numéros du brouillon 1 (n° 6 exclusions, n° 7 scikit-learn, n° 8 Cholesky,
  n° 9 mémoire, n° 10 scores) ; le texte les a renumérotés (n° 9, 7, 10, 11, 12). La fiche du code doit donner la table de correspondance.
- **A30** `Entropie` seule : le code accepte un tiret de liste et des guillemets inverses autour de la ligne ; le texte dit « rien d'autre sur la ligne ».
  Inoffensif ; une ligne.

**Lesquels exigent du code avant la ligne `CODE-NARC-EXT`** : **tous**, par la règle du texte lui-même (plan d'analyse n° 1 : « le code ferme chaque
écart »). En travail : à `3950ee93`, les écarts 1 à 12 sont **traités** (registre propre, `CODE-NARC-EXT`, « déjà ouverte », commit et paquet, transfert,
10 %, repli de Cholesky, `None` au lieu de `NaN`, graine booléenne), sauf les divergences A21 à A28 ci-dessus. **Les écarts 13 à 18 sont intacts aux deux têtes**
(aucune fonction de cellule, d'intervalle de cellule, de plancher ou placebo de cellule, de lecture secondaire des comités pour nos familles, de règle C, T
ou R, ni de tâche de graines de cellule) : c'est **la plus grosse part du code restant**. Rien de cela n'empêche de sceller le texte.

## 6. Chiffres de l'article ajoutés ou déplacés, et validateur

**Lus sur le PDF `02527fd4…` (pages 1, 6, 15, 17, 27, 28, 29, 30)** : tous exacts.
- Page 1 et page 6 : « HELIOS » nommé comme cadre (« Hidden-state Ensemble Lens for Identification Of Scheming », p. 6, § 4.1) : exact pour nommer le cadre.
- Page 27 : « layers 26–30 of 64 for Qwen3-32B » ; bande de cinq couches non nommée pour les autres ; pour les comités « the last token of system_prompt +
  round-N user_prompt + round-N public message averaged over rounds N=1,2,3 » ; pour les deux autres étages « final-round activations only » ; « balanced by
  downsampling the majority class » ; équation 8 ; Table 2 (Qwen3-32B) : comités pic 1,00 écart 1,00, stéganographique pic 1,00 écart 0,99. Exact.
- Page 28 : Table 3 (Llama-3.1-70B) mêmes quatre valeurs ; **Table 4 (DeepSeek-R1 32B) stéganographique pic 0,98, écart 0,87 ; Table 5 (GPT-OSS 20B)
  stéganographique pic 0,74, écart 0,40** : exact (Frontière n° 6).
- Page 29 : `penalty=l2`, `C=25`, `max_iter=8`, `solver="liblinear"` : exact.
- **Page 30** : « It slightly reduced OOD mean AUROC score (by less than 0.001) and wasn't used for the main results » : citation **mot pour mot**. Précision à
  ajouter (mineur) : la phrase parle de la moyenne hors distribution (transfert plus stéganographie), pas de l'étage des comités ni de l'étage
  stéganographique seuls ; elle justifie « papier » parce qu'elle dit « wasn't used for the main results » (c'est ce membre qu'il faut citer pour B2).
- Page 15 : « Three of the five methods (Peak Suspicion, Deception Split and Asymmetry Probe) require no training beyond the deception direction » :
  citation exacte ; la page 17 (« Asymmetry Probe … classifier trained on Core ») confirme la contradiction écrite. Même page : « 20 shoes … fresh
  agent-invented encoding (40 runs) » : 20 sabots, 40 épisodes, exact. Page 17 : « Every model reaches 1.00 AUROC on CORE, near-perfect detection on STEGO » exact.
- La numérotation imprimée coïncide avec celle du fichier (p. 27 imprimée = page 27 du PDF) : exact.

**Empreintes des documents cités** : recalculées, toutes égales (PDF, N-026, N-052, N-061, devis v2, brouillons 3 et 4, contre-lecture 3, contre-lecture 1,
contre-lecture du code, brouillon 1, gabarit, `prereg.py`, `familles.py`, `evaluation.py`, `plancher_v1.py`, `registre_v1.py`, `manifeste.py`, pièces de
puissance, mandat du rédacteur, `requirements-cpu.txt` du commit `70cb77b8`, six fichiers du code à ce commit ; rapport du développeur `40fbdc70…`,
manifeste des données `43106834…`, relevé des licences `ba780896…` : égaux **à ce commit de la branche du développeur**). **Mineur** : ces trois dernières
pièces ne sont **pas dans `main`** : la mère doit les faire entrer dans `main` avant de sceller, sinon le texte cite des chemins que le dépôt du
scellement ne contient pas.

## 7. Bloquants et majeurs : couples avant → après

**Aucun bloquant.**

**M1 — configuration canonique** : voir § 4 (deux versions possibles ; la version « le texte change » est recommandée).

**M2 — tolérance d'arrondi de la règle d'une cellule.** Avant (section « Seuil », « Règle d'une cellule ») : « « reproduit » si **bas ≥ m** ; « non
reproduit » si **haut < m** » et « strictement » / « inférieure ou égale » pour le plancher et le placebo. Les aires sont des moyennes de nombres de la forme
k/400 sur cinq ou six couches (et dix graines) ; la contre-lecture du code a déjà mesuré des écarts de 10⁻¹⁶ et le développeur a dû mettre une tolérance de
10⁻⁹ à la garde de reproduction (1,00 − 0,97 vaut 0,030000000000000027). Une aire moyenne à 388/400 = 0,97 exactement peut donc tomber d'un côté ou de
l'autre de la marge selon l'ordre des additions ; après le scellement, c'est un nœud. Après : ajouter « Toutes ces comparaisons se font à 10⁻⁹ près :
« reproduit » si bas ≥ m − 10⁻⁹ ; « non reproduit » si haut < m − 10⁻⁹ ; « au-dessus du plancher » si bas > quantile + 10⁻⁹ ; « placebo déclenché » si
bas ≤ quantile + 10⁻⁹. » (« reproduit » et « non reproduit » restent exclusifs, puisque bas ≤ haut.) Fermer dans le code l'écart 17 avec un essai à la borne.

**M3 — phrase trop générale sur l'issue d'une reproduction exacte.** Avant (Puissance, « La réponse au barreau ») : « **Même si notre chaîne égalait
exactement le résultat publié, l'issue la plus probable serait « non tranché à cette puissance » : ce n'est pas un échec** » ; et Frontière n° 8 :
« c'est l'issue la plus probable même d'une reproduction exacte ». Faux si l'aire vraie vaut 0,9999 ou plus (« oui » : 0,998, table de Puissance), ce que les
valeurs publiées arrondies (1,00 = [0,995 ; 1] ; 0,99 = [0,985 ; 0,995[) n'excluent pas. La phrase n'est vraie que pour une aire vraie de 0,99 à 0,995.
Après : « Si l'aire vraie de chaque cellule vaut 0,99 à 0,995 (la valeur publiée, arrondie), « oui » sort au plus 33 à 61 fois sur cent et « non tranché »
est l'issue la plus probable ; si elle vaut 0,9999 ou plus, « oui » sort presque toujours (≈ 0,998). Un « non tranché » n'est pas un échec. » Même
changement en Frontière n° 8.

**M4 — la réserve de l'intervalle absente des phrases gelées.** Avant (Critères, ligne C2 et ligne R1) : « reproduit » ; « oui : notre chaîne reproduit le
résultat positif publié (deux familles, deux modèles, deux statistiques), à côté de la recette des auteurs ; plancher apparié : <…> ». Après : (i) ligne C2 :
« reproduit (au sens « compatible avec la valeur publiée à 0,03 près » ; avec 20 sabots, la règle conclut « reproduit » à tort dans environ 18 cas sur 100 par
cellule quand l'aire vraie est exactement à la marge au pic, 0,97 ; section « Seuil ») » ; (ii) ligne R1, à la fin : « ; réserve : ce « oui » signifie
« compatible à 0,03 près », pas « égal » ; si les aires vraies étaient toutes à la marge, il sortirait à tort au plus 3 fois sur 100 (deux modèles
indépendants) et au plus 18 fois sur 100 sinon. » Et dans « Seuil », ajouter la valeur de l'écart à sa marge (≈ 0,15) **après l'avoir rejouée avec le
script scellé** (mon 0,15 n'est pas une pièce scellée).

**M5 — liste des écarts** : ajouter A19 à A30 (§ 5) à la liste de la section « Code », avec, pour A24, A25, A26, A28, la décision « le texte fait foi » ou la
phrase de texte proposée.

## 8. Autres mineurs

- **m1** (« exposition (d) », ligne 686) : « La contre-lecture 2 lui fait confirmer cette ligne » : un contre-lecteur ne peut pas confirmer ce que la mère a
  lu ; il ne confirme que ce que les registres disent. Avant : « La contre-lecture 2 lui fait confirmer cette ligne » → Après : « La mère confirme cette ligne
  au scellement ; la contre-lecture 2 n'a lu que les registres ».
- **m2** : ajouter une exposition (g) : « Contre-lecteur 2 (Claude Sonnet 5.5) : aucune donnée réelle ; code lu aux têtes `70cb77b8` et `3950ee93` ; la
  commande de contrôle préalable `verifier-texte` du code exécutée sur une copie du brouillon (texte seulement) ; un point de la simulation de puissance
  rejoué (données simulées) ».
- **m3** (Hypothèse, dernière phrase sur le critère de G0) : conforme ; rien.
- **m4** (n° 2 de la liste d'arrêt : « ou ouverture d'un de ses fichiers → refus, nœud ») : « refus » (avant ouverture) et « ouverture d'un fichier »
  (après) se contredisent ; écrire « arrêt » pour la seconde moitié.
- **m5** (plan d'analyse n° 2, « sans rien écrire en cas de refus ») : voir A23.
- **m6** (garde mémoire avant l'ouverture) : § 2, à décider par la mère.

## Lectures hors du mandat (déclarées)

- Les sources de l'article aux **pages 1, 6, 15, 17, 28, 29, 30** (le mandat liste la p. 27-30 et les chiffres ajoutés ; 1, 6 et 15, 17 parce que le texte les
  cite) ; rien d'autre du PDF.
- Le **commit `3950ee93`** de la branche du développeur, apparu pendant ma lecture (dossier extrait par `git archive` vers mon dossier temporaire) ; la
  commande `verifier-texte` du code, qui ne lit que le texte, lancée sur une copie du brouillon dont j'ai rempli l'entropie ; aucun autre point d'entrée
  du code exécuté ; aucune donnée ouverte.
- Un **point de la simulation de puissance** rejoué (le script scellé, fonction `simuler` importée), plus le point « écart à sa marge » (données simulées).
- Les lignes de `registres/decisions.md` R-3333, R-3335, R-3336 et R-3341 (par leur numéro de ligne, comme le mandat les nomme) et le début de la ligne R-3336.
- Rien lu sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Rien commité, rien poussé, rien écrit sous `registres/` ; l'arbre du développeur n'a pas été
  modifié (aucun fichier écrit, `PYTHONDONTWRITEBYTECODE=1`). Mon dossier temporaire (`/tmp/claude-0/cl2-tmp`) est supprimé à la fin.
