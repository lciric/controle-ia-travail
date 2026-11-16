# Vérification courte de la procédure du pilote MR-2 — v10 (passage v9 → v10) — et du programme d'épreuve des clés — v2

- **Lecteur** : instance neuve, qui n'a écrit aucune version de la procédure, ni le programme d'épreuve, ni aucune de leurs
  vérifications. Ce rapport n'écrit aucun nom de modèle (seules les étiquettes de la configuration v12 : `opus55`, `fable52`,
  `argon`, `astra` ; les fournisseurs sont dits « premier », « deuxième », « troisième », dans cet ordre).
- **Pièces** (copie `/home/user/verif-pilote-v10`, tête détachée `3726c5cf`, arbre propre avant écriture ; **toutes les empreintes
  des deux dossiers recalculées et égales à leurs compagnons**, 31 compagnons, 31 « OK ») :
  - procédure v10 `28a834440b6c673974716cf8753a49549832451f7843b1d2b7588de0f2f41768` ; v9
    `e71b66983ace4badff1695d885aa3714f7adf805c2eb834e8c688c23103bb288` ;
  - programme `epreuve_cles_pilote_v2.py` `efb939db890aee8fa1f432351d36e3e48fbff9005876330516ce5963407a2ea0` ; v1
    `f56eaecbe6f79aef7b4d40e794a0f317c8306326d8665ae532bf02efa0d8221f` ; essai local v2 (`LISEZMOI.md`, doublure, onze écrans) ;
  - paquet de l'arbre `e3d83e47…` (tête `605e0f60…`, dépaqueté dans le dossier temporaire du lecteur), configuration v12
    `f69503dd4ba5e57a8bde230b3861571549d9598382808a8f3c0f4fa664ea818b`, code du pilote lu : `commande_pilote_v70.py` (celui que
    nomme `pilote_mr2_v74.py` l. 93) ;
  - corrections attendues : vérification de la v9 et du programme v1
    `11118317c0579e3cc7f7f2af654b928c06a5919cdc2d27c12503bfdbc7eb6288` (dépôt de travail, recalculée) ; lignes GO-2026-11-15-02 et
    GO-2026-11-15-05 (`registres/go.md` l. 335 et 338) ; R-2856, R-2866, R-2867 (`registres/decisions.md` l. 2816, 2826, 2827) ;
  - à la référence suivie `refs/remotes/origin/lot/compte-organisme-v1` du dépôt de travail (lue sans `fetch`), la v10 et le
    programme v2 ont ces mêmes empreintes.
- **Fin** : 2026-11-15T08:36:23Z (sortie de `date -u` dans la commande qui écrit ce fichier).
- **Aucun appel réel, aucune clé lue, aucune machine, ni `env` ni `printenv`.** Tout ce qui a été joué l'a été contre la boucle
  locale, avec des clés factices écrites en clair dans la commande d'essai ; là où une commande de la procédure nomme une clé par
  son nom, la variable a d'abord été remplacée par une valeur factice dans l'interpréteur d'essai.
- Aucun refus d'outil, de crochet ni de classifieur rencontré.

## Verdicts

- **Procédure v10 : jouable** — 0 bloquant, **0 majeur**, 5 mineurs (q1 à q5). Sous la seule substitution que sa ligne 166 prévoit
  elle-même : la commande d'épreuve se joue avec `GO_ID=GO-2026-11-15-05` (q1, R-2867).
- **Programme d'épreuve v2 : jouable** — 0 bloquant, **0 majeur**, 5 mineurs (f1 à f5).

**Majeurs : aucun, ni pour la procédure ni pour le programme.**

Le différentiel v9 → v10 est rattaché, bloc par bloc, à un point de la section 12 septies ; MP1 et MP2 sont fermés (éprouvés sur
données factices) ; p1 à p8 sont portés ; aucune régression sur l'argent, les plafonds, les nœuds, l'heure limite, les arrêts, la
destruction, les clés, le préfixe `GO_ID=`. Dans le programme, ME1 et ME2 sont fermés (la règle de l'identifiant servi est celle
du pilote : motif égal caractère pour caractère, zéro écart sur 33 chaînes choisies et 200 000 tirées) ; e1 à e7 sont portés.
L'essai local v2 rejoué rend, pour les onze scénarios versés, les mêmes codes, les mêmes comptes de requêtes et des écrans égaux
à l'octet.

Aucun mineur n'a d'effet sur l'argent, les clés ou la mesure ; aucun n'exige une version nouvelle avant de jouer. Ils sont à porter
dans la version suivante, s'il y en a une.

## Point connu : `GO_ID=` de la commande d'épreuve

- **Constat** : l. 160 de la v10, « `&& GO_ID=GO-2026-11-15-02 env -i PATH=/usr/bin:/bin …` ». La ligne GO-2026-11-15-02 nomme
  `epreuve_cles_pilote_v1.py` ; la ligne GO-2026-11-15-05 (`go.md` l. 338) nomme `epreuve_cles_pilote_v2.py`, plafond commun
  0,10 USD. R-2867 demande que la commande cite la seconde.
- **Est-ce le seul endroit à changer ? Oui, pour la commande** : c'est la seule occurrence où un identifiant de ligne est
  joué. Les autres mentions sont du texte et restent vraies sans changement : l. 5-6 et 12-13 (« ligne d'extension de Lazar qui
  nomme le programme d'épreuve v2 », sans numéro), l. 146 (« préalable d'exécution, GO-2026-11-15-02 » : la ligne d'origine),
  l. 150-151 (« jouée seulement sous la ligne d'extension de Lazar qui nomme la v2 (la ligne GO-2026-11-15-02 nomme la v1 ; même
  plafond, 0,10 USD) »), l. 398 (« GO-2026-11-15-02 et sa ligne d'extension »), l. 698 (table du différentiel).
- **Une version nouvelle n'est pas nécessaire pour cela** : la l. 166 écrit « (`GO_ID=` : la ligne d'extension, une fois inscrite,
  remplace l'identifiant si la mère le dit.) ». La ligne est inscrite (R-2867) ; le mot de la mère suffit, et la commande se joue
  avec `GO_ID=GO-2026-11-15-05`, tout le reste à l'octet (éprouvé : une seule ligne diffère).
- **Portée réelle de cet identifiant** : une citation, non une garde. Le crochet (`73be0638…`, égal dans la copie et le dépôt de
  travail), joué sur entrée factice avec le registre de `main`, laisse passer la commande d'épreuve avec `-02`, avec `-05` et sans
  identifiant (elle ne porte aucun motif de lancement d'instance) ; `env -i` ne transmet pas `GO_ID` au programme.
- Si une v11 est écrite malgré tout : l. 160 `-05` ; l. 146 « GO-2026-11-15-02, étendue au programme v2 par GO-2026-11-15-05,
  R-2867 » ; l. 151 et 398, le numéro de la ligne d'extension ; l. 166, la parenthèse retirée (retrait à déclarer).

## Limites

- Non vérifiable sans appel (inchangé depuis la vérification précédente) : que la borne de sortie passée à `argon` borne aussi sa
  réflexion (le code 5 la signale **après coup**, il ne l'empêche pas) ; qu'une borne de 16 jetons rende 200 chez les trois
  fournisseurs ; que le mandataire de la session qui lance laisse passer les trois adresses (sinon : `erreur:URLError` trois fois,
  code 4, épreuve consommée, rien de dépensé alors que `depense_usd` affiche le pire cas, voir f4).
- Indice lu dans la configuration v12 (l. 2, note de tête) : la sonde v71 a envoyé à `argon` cette même consigne et n'a observé
  aucune réflexion. C'est un indice, pas une garantie.
- Pour un appel coupé (délai) chez `argon`, le coût compté est le pire cas à 16 jetons ; si la réflexion n'est pas bornée, le coût
  réel peut être plus haut et ne se lit qu'à la console du fournisseur.
- Bibliothèque cliente : `urllib` de la bibliothèque standard, Python 3.13.18 (`/usr/bin/python3` ici), éprouvée par essais.
- Le code du pilote a été lu et deux de ses fonctions (`modele_conforme`, `lire_dialecte`) appelées sur des chaînes factices ;
  rien d'autre n'en a été exécuté.

---

# Partie A — procédure, v9 → v10

## A1. Différentiel exact

`diff` : 16 blocs. Relecture mot à mot des retraits (`git diff --no-index --word-diff=porcelain`).

| lignes de la v10 | changement | point déclaré (12 septies) |
|---|---|---|
| 1 | titre « v10 » | non nommé (q3) |
| 5-6 | « vérification « jouable » du différentiel v9 → v10 (mère) et la ligne d'extension de Lazar » | programme d'épreuve v2 (« en-tête ») |
| 8-14 | versions ; « la v10 remplace la v9 » ; rapport `11118317…` ; renvoi à 12 septies | programme d'épreuve v2 (« en-tête ») |
| 96-99 | constat « aucun `jouer` ne tourne » : code 1, code supérieur à 1 | p3 |
| 148-153 | programme v2 nommé, empreinte, délai de 600 s, sortie réservée, marque | programme v2, p4 |
| 157-162 | tirage de la v2 ; `sha256sum -c -` enchaîné ; marque ; appel de la v2 | MP2, p4 (retrait de la ligne d'affichage : dit) |
| 166-176 | attendu, codes, conduites, dépense, écart au texte scellé | MP2, p4, p5 |
| 202-204 | préambule sur la ligne d'avant ; `${ENV:?}` ; phrase retirée | MP1 (retrait dit) |
| 256 | `test $k -lt 3 && sleep 30` | p7 |
| 397-398, 403-406 | section 9 : épreuve faite à la section 1 ; ce qu'elle ne couvre pas | p6 (deux retraits dits) |
| entre 419 et 420 | commentaire `# dès que « lancé »…` retiré du bloc | p1 (retrait dit) |
| 424-426 | règle hors du bloc : « lancé », ou journal ou code vus au suivi | p1 |
| 453-455 | même règle pour `reel-2` | p1 |
| 510-511 | `REEL` écrit, dossier absent : code non nul attendu | p2 |
| 693-713 | section 12 septies (p8 y est déclaré) | déclaré |

- **Changement de fond non déclaré : aucun.** Aucun bloc dans les sections 4 à 8, 10, 12 à 12 sexies, 13 (bornes relues : l. 274
  à 362, 466 à 505, 548 à 692) : la dernière phrase de 12 septies est exacte.
- **Retraits non nommés : quatre groupes de mots, dont un seul touche une conduite** (q2) ; les autres sont sans effet (q3).

## A2. MP1 : fermé (l. 202-204)

Les deux lignes extraites de la v10, chemin d'envoi remplacé par un dossier d'essai, outil du loueur remplacé par un programme
factice qui note ses arguments et la valeur de `GO_ID` reçue :

| état | résultat |
|---|---|
| `variables.sh` porte `ETIQ` | code 0 ; outil appelé une fois avec `GO_ID=GO-2026-11-14-14`, `--label` égal à l'étiquette lue ; `creation.json` écrit dans le dossier d'envoi |
| dossier présent, `variables.sh` absent | « ETIQ: parameter null or not set », code 1, **outil non appelé, aucun fichier** |
| dossier d'envoi absent | même refus, outil non appelé |
| `variables.sh` sans `ETIQ` | même refus, outil non appelé |
| ligne de création jouée seule (forme de la v9) | même refus : la v10 ne dépend plus de la commande d'avant |

Crochet, entrée factice, registre de `main` : la commande de deux lignes **passe** (code 0 ; l'identifiant est cherché dans toute
la commande) ; la même sans `GO_ID=` est **bloquée** (code 2). La ligne de création commence par `GO_ID=` ; l'aide reste « sous le
même préfixe » (l. 181-183, inchangées).

## A3. MP2 : fermé (l. 156-163)

Bloc extrait de la v10, chemin d'envoi remplacé, trois clés factices posées en tête, adresse d'essai locale ajoutée à l'appel
(seconde doublure, port 8897), le reste à l'octet :

| état | écran | requêtes | marque | sortie |
|---|---|---|---|---|
| programme tiré de la référence suivie (empreinte juste) | « OK », la ligne JSON, `code=0` | 3 | écrite | écrite |
| même commande une seconde fois | « OK », `code=1` | **0** | — | — |
| `git show` en échec (programme **vide**, 0 octet) | « FAILED », `code=1` | **0** | **non écrite** | absente |
| autre contenu sous le même nom (la v1) | « FAILED », `code=1` | **0** | non écrite | absente |
| sortie déjà là, marque absente | `code=1` | 0 | — | — |
| marque déjà là, sortie absente (commande coupée d'avant) | `code=1` | 0 | — | — |
| une clé absente de l'environnement | « REFUS : clé … absente (nom seul) », `code=2` | 0 | **écrite** | absente |

Un programme vide joué seul rend toujours code 0 : c'est bien le contrôle d'empreinte, placé devant, qui l'empêche d'être joué, et
la phrase « un `code=0` sans cette ligne vaut « tout autre code » » (l. 166-168) couvre le reste. Dernière ligne de la table : q4.

## A4. p1 à p8

| mineur | porté | où (v10) | essai |
|---|---|---|---|
| p1 | oui | 424-426, 453-455 ; commentaire retiré | lecture |
| p2 | oui | 510-511 | lecture |
| p3 | oui | 96-99 | joué sans `ssh` : absent → « aucun processus du pilote » ; processus factice présent → listé, aucune phrase ; outil introuvable → « constat illisible (code 127) ». Le crochet laisse passer la ligne (lecture seule) |
| p4 | oui | 151-153, 159, 169, 175-176 | table A3 ; délai de 600 s contre 3 × 60 s au plus pour le programme |
| p5 | oui, sauf un mot | 172-175 | (i) code 5 → nœud ; (ii) pire cas compté ; (iii) écart porté au journal du pilote avec le résultat ; reste q2 |
| p6 | oui | 397-398, 403-406 | lecture ; `fable52`, `output_config`, quota, chemin de réseau dits |
| p7 | oui | 256 | boucle jouée sur outil factice : jamais montée → trois lectures, **deux** attentes, « pas encore montée » ; montée → une lecture, marques remplacées, `0` restante. Le code de sortie de la boucle n'est lu par rien |
| p8 | oui | 708 | les deux retraits de la v9 y sont nommés |

## A5. Régressions : aucune

- **Argent, plafonds** : lignes GO-2026-11-14-13 (20 USD) et GO-2026-11-14-14 (21,72 USD, dont machine 3 USD), l. 37-38 ; prix
  horaire au plus 0,20 USD, pire cas ≈ 14 h, l. 197-200 : hors de tout bloc du différentiel. Épreuve : montant passé `0.10`
  (l. 163), plafond commun aux deux lignes.
- **Nœud à 2,70 USD, heure limite, arrêt par PID sur le mot de la mère** : l. 101-106, inchangées.
- **Destruction** : l. 528-539, inchangées (identifiant relu et exigé entier, étiquette comparée par programme devant
  `destroy … -y`, liste relue, absence prouvée, témoins toujours listés).
- **Clés** : les lignes neuves affichent un chemin et « OK », une heure, un code, quatre champs JSON, une ligne de commande de
  processus (chemins seuls). Recherche des clés factices dans tous les écrans, marques et sorties des essais A2 et A3 : aucune
  occurrence. Les clés restent passées par leur nom sous `env -i`.
- **`GO_ID=`** : ligne de création et aide, voir A2.
- **R10** : aucun arrêt par motif ajouté.

## A6. Constats de la procédure

### Bloquant, majeurs

Aucun.

### Mineurs

- **q1 — Identifiant de ligne de la commande d'épreuve** (l. 160). Ancien : « `&& GO_ID=GO-2026-11-15-02 env -i PATH=/usr/bin:/bin
  HOME=/root …` » ; nouveau : « `&& GO_ID=GO-2026-11-15-05 env -i PATH=/usr/bin:/bin HOME=/root …` ». Seul endroit à changer ;
  prévu par la l. 166 ; sans effet mécanique (voir « Point connu »).
- **q2 — La dépense de l'épreuve n'est plus dite « proposée à la mère »** (l. 173-174 ; retrait non déclaré). Ancien (v9
  l. 156) : « La dépense de l'épreuve est proposée à la mère depuis `depense_usd`. » ; nouveau (v10 l. 173) : « **Dépense** :
  `depense_usd` (un appel parti sans usage lu y est compté au pire cas de sa clé, `cout_origine` « pire_cas »), **proposée à la
  mère avec le résultat de l'épreuve, que le code soit 0 ou non** ; au-dessus de 0,10 (code 5) : nœud. » Après un code 0 la
  procédure enchaîne sur la location : sans ces mots, rien ne dit quand la dépense de l'épreuve est remise.
- **q3 — Déclaration (sans effet)** : ne sont pas nommés parmi les retraits de 12 septies les mots « (pire cas 0,027168 USD sous
  la ligne de 0,10) » (v9 l. 153 ; le montant reste dans la ligne JSON attendue), « ce sont celles de la sonde v74 du
  14 novembre, 13:38Z » (v9 l. 378), « **Réduit par l'épreuve des clés de la section 1** (GO-2026-11-15-02) » (v9 l. 384), ni le
  changement du titre (l. 1). À porter dans la section du différentiel suivant.
- **q4 — « L'épreuve a eu lieu » après un refus sans appel** (l. 159, 175-176). La marque `epreuve-cles.lancee` est écrite avant
  le programme ; un code 2 (refus avant tout appel : aucune requête, aucune dépense, éprouvé) la laisse en place, et le texte dit
  alors « l'épreuve a eu lieu : ne pas la rejouer ». De même une empreinte qui diffère (rien n'est joué, aucune marque) est
  rangée sous « aucune reprise de l'épreuve ». L'arrêt et le nœud sont justes ; seule la phrase est inexacte.
  Ancien (l. 175-176) : « Si `epreuve-cles.lancee` ou `epreuve-cles.json` existe déjà, l'épreuve a eu lieu : **ne pas la
  rejouer**. » ; nouveau : la même phrase, suivie de « Après un code 2 ou une empreinte qui diffère, aucun appel n'est parti :
  nœud ; la reprise (marque retirée) est une décision de la mère, jamais de l'exécutant. »
- **q5 — Devis non repris pour la v2 (remarque)** : `devis-et-ligne-epreuve-cles-pilote-v1.md` décrit la sortie de la v1
  (« jamais l'identifiant », codes 0 et 4). Le montant est inchangé (pire cas recalculé égal, B3) et la ligne GO-2026-11-15-05
  nomme la v2 : rien à corriger avant de jouer. La sortie `epreuve-cles.json` porte désormais l'identifiant servi : si elle est
  remise à la mère dans un nœud, il ne doit pas être recopié dans un registre de `main` (R-2731 ; la l. 150 le dit pour le
  fichier).

---

# Partie B — programme `epreuve_cles_pilote_v2.py`

## B1. ME1, ME2, e1 à e7

| point | porté | ligne du programme | essai |
|---|---|---|---|
| **ME1** identifiant servi | oui | 38, 46-60, 157 | motif `SUFFIXE` égal à `SUFFIXE_DATE` du pilote (`commande_pilote_v70.py` l. 71) ; `conforme` contre `modele_conforme` (l. 113-126) : **0 écart** sur 33 chaînes choisies (exact, deux formes de date, `-2026`, `-mini`, `-preview`, dates impossibles, années 1999 et 2100, espace ou saut de ligne en queue, préfixe `models/`, chiffres non latins, non-chaînes) et 200 000 suffixes tirés. Posé aussi quand rien n'est servi (faux) |
| **ME1** usage exigé | oui | 158-162, 164 | `toutes_valides` exige `cout_origine` « usage » ; scénario « sansusage » → code 4. Écart résiduel avec le pilote : f1 |
| **ME2** dépense contre la ligne | oui | 167, 171-172 | `depassement` écrit et imprimé ; **code 5 prioritaire** ; scénario « reflexion » : `depense_usd` 1,60068, `depassement` vrai, code 5 |
| e1 redirections | oui | 63-65, 131 | 301, 302, 303, 307, 308 : statut rendu, code 4, **3 requêtes `POST`, aucun `GET`** |
| e2 sortie réservée | oui | 120-128, 169-170 | programme arrêté par son PID pendant le deuxième appel : la sortie porte « appels en cours » ; rejoué : « REFUS : sortie existante », code 2, aucune requête. Dossier absent → refus code 2 avant tout appel |
| e3 montant | oui | 105-110 | `nan` et `0` : code 2, 0 requête |
| e4 pire cas compté | oui | 138, 146, 161-162 | corps illisible, corps non objet, usage absent : `cout_origine` « pire_cas », 0,01132 |
| e5 codes | oui | 16-18, 41-43, 172 | 0, 4, 5, 2, 1 dits et tenus |
| e6 délai | oui | 36, 147 | 60 s par appel |
| e7 portée | oui | 8-10 | dite (`fable52`, `output_config`, quota, chemin de réseau) |

## B2. Clés, corps, appels, bornes

| question | constat |
|---|---|
| clés lues par leur nom | l. 118, 135, 140 : `os.environ[conf["proposeurs"][n]["variable_cle"]]` ; présence des trois contrôlée avant tout appel (l. 117-119) |
| aucune valeur de clé affichée ni écrite | la clé n'entre que dans un en-tête de requête (reçu par la doublure : un seul en-tête à clé par requête, celui du dialecte). Écran : quatre champs. Refus : le **nom** de la variable. Erreur : le **nom du type**. Recherche des clés factices dans tous les écrans, erreurs et sorties de 34 exécutions : **aucune occurrence** |
| aucun corps affiché ni écrit | corps d'erreur HTTP non lu (l. 150-152) ; corps de réponse marqué (texte de réponse, corps d'erreur) recherché partout : **aucune occurrence**. Un seul champ du corps est écrit : l'identifiant servi |
| l'identifiant servi écrit : sans risque ? | **Pour les clés, oui** : c'est une chaîne d'une réponse 200 du fournisseur, jamais un écho de la requête ; écrit seulement si c'est une chaîne (l. 155-156), dans la sortie seulement, jamais à l'écran. Deux réserves, sans effet sur les clés : sa longueur n'est pas bornée (f2) ; c'est un identifiant de modèle, à tenir hors de `main` (dit l. 13 du programme et l. 150 de la procédure) |
| un seul appel par clé | une boucle, un `open` par clé, aucune reprise : **3 requêtes exactement** sur 200, 401, 403, 404, 429, 500, 529 (avec `Retry-After`), cinq redirections, corps illisible ; 2 quand une clé est illisible (rien n'est envoyé pour elle) |
| borne de sortie passée | corps reçus par la doublure : `max_tokens` 16 (premier fournisseur), `generationConfig.maxOutputTokens` 16 (`argon`), `max_completion_tokens` 16 (`astra`) ; consigne de 28 octets ; modèle de la configuration |
| adresse d'essai | `re.fullmatch(r"http://127\.0\.0\.1:\d{1,5}")` (l. 100) : la forme à nom d'usager de la vérification précédente est refusée par construction |

## B3. Pire cas recalculé

(28 + 1024) × prix d'entrée + 16 × prix de sortie, prix de la configuration v12 : `opus55` 0,004528 ; `argon` 0,011320 ; `astra`
0,011320 ; **total 0,027168 USD**, égal au programme (écran), à la procédure (l. 167) et à la ligne. Sous 0,10 USD. Le refus
d'avant appel (l. 115-116) le compare au montant passé.

## B4. Codes de sortie et conduite de la procédure

| code | programme | procédure (l. 166-176) | cohérent |
|---|---|---|---|
| 0 | trois statuts 200, trois identifiants conformes, trois usages lus, dépense sous la ligne | on continue, si la ligne JSON est là | oui |
| 4 | une clé au moins ne passe pas | arrêt, aucune location, nœud | oui |
| 5 | dépense lue au-dessus de la ligne (prioritaire sur 4) | nœud | oui |
| 2 | refus avant tout appel (aussi le code de l'interprète quand le fichier manque : aucun appel non plus) | arrêt, nœud | oui ; phrase q4 |
| 1 | erreur non rattrapée ; aussi le `code=` affiché quand la chaîne s'arrête avant le programme (empreinte, marque, sortie) | arrêt, nœud | oui |

## B5. Essai local v2 rejoué (doublure versée, port 8898, clés factices, aucun réseau)

Doublure `essai-local-v2/doublure-essai-v2.py` lancée puis arrêtée par son PID ; programme sous `env -i PATH=/usr/bin:/bin
HOME=/root`, trois clés factices, configuration v12, montant 0.10 (sauf « nan » et « nul »), `--amont-essai http://127.0.0.1:8898`.

| scénario | code | requêtes | écran égal à l'écran versé |
|---|---|---|---|
| normal | 0 | 3 `POST` | oui |
| mini | 4 | 3 | oui |
| 401 | 4 | 3 | oui |
| 302 | 4 | 3, aucun `GET` | oui |
| sansusage | 4 (`pire_cas`) | 3 | oui |
| illisible | 4 (`pire_cas`, 0,01132) | 3 | oui |
| reflexion | 5 (`depense_usd` 1,60068) | 3 | oui |
| montant `nan` | 2 | 0 | oui |
| montant `0` | 2 | 0 | oui |
| clé à saut de ligne | 4 | 2 | oui |
| sortie existante | 2 | 0 | oui |

**Compte : onze scénarios sur onze conformes au `LISEZMOI.md`**, codes, requêtes et écrans (comparés à l'octet). Aucune clé
factice ni corps d'erreur dans les écrans et les sorties.

Scénarios ajoutés par ce lecteur (seconde doublure, dossier temporaire) : redirections 301 à 308 ; statuts 401 à 529 ; corps non
objet ; identifiant servi non chaîne (non conforme, code 4, rien d'écrit) ; identifiant daté réel (0), date impossible (4),
`-preview` (4), suffixe de 5 000 caractères (4, écrit en entier : f2) ; `argon` avec la seule réflexion comptée (0) ; `argon`
avec le seul compte d'entrée (4 : f1) ; coupure par PID.

## B6. Constats du programme

### Bloquant, majeurs

Aucun.

### Mineurs

- **f1 — Règle de l'usage : deux écarts avec le pilote, hors de l'identifiant** (l. 88-89, 158). Le pilote lit, pour `argon`, les
  deux comptes de sortie avec 0 par défaut : un usage qui ne porte que le compte d'entrée y est **lu** (sortie 0) ; l'épreuve le
  dit **absent** et rend 4 (éprouvé sur la fonction du pilote et sur doublure). Écart du côté sûr — une fausse alerte qui consomme
  l'épreuve —, peu probable (il faut une réponse sans aucun jeton de sortie ni de réflexion). En sens inverse, le pilote refuse
  un compte booléen ou négatif, l'épreuve l'accepte (cas absurdes).
  Ancien (l. 88-89) : « `c, t = u.get("candidatesTokenCount"), u.get("thoughtsTokenCount")` / `sortie = None if c is None and t
  is None else (c or 0) + (t or 0)` » ; nouveau : « `c, t = u.get("candidatesTokenCount", 0), u.get("thoughtsTokenCount", 0)` /
  `sortie = c + t if entier(c) and entier(t) else None` », avec « `def entier(x): return isinstance(x, int) and not
  isinstance(x, bool) and x >= 0` » employé aussi l. 158.
- **f2 — Identifiant servi écrit sans borne** (l. 155-156). Éprouvé : une chaîne de 5 012 caractères est écrite telle quelle.
  Aucun risque pour les clés ; c'est le seul champ du corps qui atteint le disque.
  Ancien : « `ligne["modele_servi"] = servi` » ; nouveau : « `ligne["modele_servi"] = servi if re.fullmatch(r"[\x21-\x7e]{1,200}",
  servi) else "illisible"` » (la conformité reste calculée sur la chaîne entière).
- **f3 — Clé illisible découverte dans la boucle** (l. 141-142). Une clé à espace ou à saut de ligne n'est vue qu'à son tour :
  les autres appels partent, code 4. Contrôlée avec la présence (l. 117-119), elle rendrait un refus sans aucun appel.
  Ancien (l. 118-119) : « `if not os.environ.get(…): refus(f"clé … absente (nom seul)")` » ; nouveau : la même, suivie de
  « `if not re.fullmatch(r"[\x21-\x7e]+", os.environ[…]): refus(f"clé … illisible (nom seul)")` ».
- **f4 — Pire cas compté pour un appel qui n'est jamais parti** (l. 146, 153-154, 161-162). `parti` est posé avant l'ouverture :
  un refus du mandataire ou un port fermé compte le pire cas de la clé (éprouvé : port fermé, trois `erreur:URLError`,
  `depense_usd` 0,027168 alors que rien n'est parti, code 4). Du côté prudent ; `depense_usd` est alors une borne, non une dépense : les montants facturés se lisent aux
  consoles. Rien à changer ; à savoir en lisant la sortie.
- **f5 — En-tête** (l. 17-18) : la liste des refus de code 2 omet « arguments », « sortie non inscriptible » ; « clé illisible »
  n'est pas un refus mais un code 4. Sans effet.

## Pièces

- Essais : dossier temporaire de la session du lecteur, hors de tout dépôt
  (`/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/lecteur-v10/` : `b` essai local
  rejoué, `c` seconde doublure et comparaison avec le pilote, `f` procédure, `arbre` paquet dépaqueté).
- Rien d'autre n'a été écrit dans la copie que ce rapport et son compagnon ; aucun commit, aucune poussée.
