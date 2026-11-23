# Erratum de chaîne de la relecture décisive du barreau 5 — v1 (conception, à contre-lire)

Écrit le 22 novembre 2026 vers 22:45Z (`date -u`) par un concepteur neuf, Claude Opus 5.5 en effort maximal, sous-agent du conducteur de la lecture du barreau 5 (`session_013QMayjM1PQPWkLifMw9HDR`) ; le quota de Fable est épuisé jusqu'au 29 (GO-2026-11-22-145).

- **Consigne** : `consigne-concepteur-erratum-chaine-lecture-b5f-v1.md` (`caecf8f69390c8ec5e052c23c94851a2a283d711a9b03a139c5bd3404ea3be67`, égale à son compagnon). Trois mots du conducteur : (1) au lancement, une précision de la mère, voie par défaut « nom neuf `-r1` » ; puis, pendant le travail, (2) un complément, la variante de la table des étiquettes à noms suffixés, dans ce même erratum ; (3) un fait neuf, la garde figée de « scores » exige la branche du texte, avec la consigne de peser les deux voies et de recommander l'exception à R12 si elle réduit nettement le code touché. Le troisième, le plus récent, fixe la recommandation du § 3.
- **Classe** : A pour la règle (écarts, nœuds), B pour le code, que ce texte décrit sans l'écrire. Suite : contre-lecture par un Opus neuf, vérification des corrections par le même, puis un développeur Opus neuf. **Aucune relance, aucun geste payant, aucune suppression de branche avant le mot de Lazar.**

## 0. En bref

1. **Cause confirmée et reproduite.** Le clone partiel des entrées de lecture n'a pas l'aide d'identification quand l'extraction tire ses fichiers en différé. Un sondage jetable rejoue l'erreur de l'instance à la lettre.
2. **Correction recommandée (voie B)** : **une seule ligne ajoutée à l'amorce** (empreinte `54a676f3…` → `0adb6efb…`). La branche de sortie garde son nom : la branche existante est copiée à l'octet sous `traces/barreau5-lecture-tentative-1`, puis supprimée, sous une exception nommée à R12. L'autre voie (A, nom neuf `-r1`) tient en une ligne au § 3.2.
3. **Admission.** L'arbre gelé du commit de la marche ne peut pas changer : la marche elle-même, sur l'instance, le refuserait (§ 2.4). L'amorce corrigée part donc par la commande. Un module de commande, version 3, bâti sur la version 2, la calcule depuis l'amorce figée par la liste fermée des différences, vérifie les deux empreintes et l'embarque. Une ligne libre sous la table du registre propre l'épingle. Aucune garde figée n'est retouchée.
4. **Variante de l'ouverture.** Si la table engagée porte des noms suffixés, une règle mécanique en décide (empreintes de deux listes écrites d'avance), puis une traduction contrôlée, après l'égalité d'empreinte de la table d'origine. Une ouverture recomposée appelle alors le programme de lecture figé, inchangé à son empreinte. Elle est admise par la même voie.

## 1. Ce que j'ai lu, ce que je n'ai pas ouvert

- **Empreintes vérifiées avant lecture** (égales au compagnon ou à la valeur citée) :
  - consigne ;
  - mandat de la session de lecture v2 (`b1eb2afc…`) et ses errata 1 à 3 (`cde0279c…`, `4d1678b5…`, `1c9d9ce1…`) ;
  - note `format-activations-gardees-relecture-b5f-v1.md` (`b8539886…`) ;
  - rapport de vérification de la commande v2, `signal-conducteur-v1/verification-corrections-commande-lecture-v2-v1.md` : sans compagnon dans ce dossier, empreinte recalculée égale à `fca7d949…` ;
  - texte scellé (`bdff244f…`) ;
  - au commit `c76e79169` : amorce `54a676f3…`, lanceur v1 `ae501c55…`, `relecture_v1.py` `f6bd8c15…`, `lecture_v1.py` `ed0999df…`, `validation_reelle.py` `d25e4cd9…`, essais de l'amorce `5d3f0302…` ;
  - au commit `5402367e` : module `c6c5d11c…`, lanceur `c07fc124…`, essais `82452204…`.

  `5402367e` et `2beeec31` descendent de `c76e7916`.
- **Lu en entier** : `CLAUDE.md`, la consigne, le mandat v2 et ses errata, la note de format, le rapport de vérification v2, l'amorce, le lanceur v1, le module et le lanceur de la commande v2, les essais de l'amorce.
- **Lu en partie** :
  - texte scellé, l. 35, 151 à 179, 217 à 233, 257 à 261 et 345 à 448 ; rien des l. 53 à 77 ;
  - `relecture_v1.py`, l. 1 à 140, 184 à 232, 533 à 600 et 836 à 1247 ;
  - `validation_reelle.py`, `CHEMINS_GELES` et `exiger_code_cite`.
- **Lu en plus, hors de la liste, code seulement (écart 8)** :
  - dans `lecture_v1.py`, ce qui sert l'ouverture et sa garde (le complément du conducteur m'y renvoyait) : constantes l. 101 à 158, `programme_sha256`, `lire_registre_de_lecture`, `exiger_code_de_lecture_au_commit`, `garde_d_ouverture`, `instance_de`, `prefixe_de_copie`, `exiger_copie_lue`, `_lire_json`, le début d'`exiger_arbre`, `exiger_arbre_sans_etiquettes` et ses deux détecteurs, `familles_tenues`, `lire`, `charger_entrees`, `exiger_alignement`, `ouvrir`, `_familles_formees`, `relance_du_registre`, `couts_depuis_formation`, `resume_formation_depuis_branche`, `preparer`, `_main`, `_registre_au_commit` ;
  - dans `engagement_v1.py`, l. 1 à 200 et 240 à 315 ;
  - dans `formation_v1.py`, les suffixes (l. 89 à 92), `decomposer_famille`, `familles_du_plan`, l. 1214 à 1226 et 1274 à 1284 ;
  - dans `epreuve_verite_plantee_v1.py`, la liste des fonctions, `noms_opaques`, `_octets_table`, le début de `fabriquer`, l. 1140 à 1160 ;
  - l'en-tête de `traducteur_verite_plantee_v1.py` ;
  - dans `tests/test_amorce_b5f_lecture_entiere_v1.py`, les lignes qui montent le dépôt distant ;
  - dans `tests/test_commande_lecture_v2.py`, l'en-tête, les montages et la liste des essais.
- **Jamais ouvert** :
  - aucune branche `donnees/*`, `formation-b5f/*`, `traces/*`, `course/*` (les fichiers de la commande v2 sont lus par `git show` à son commit, déjà présent) ;
  - ni `registres/etat.md`, ni `registres/decisions.md`, ni le registre propre, ni le registre des accords, ni une passation ;
  - ni table, ni sel, ni score, ni coût, ni activation ; ni les têtes `81061453` et `254f9280`, absentes de ce dépôt.

  Aucun résultat de ce plan n'existe ; je n'en ai lu aucun.
- **Routine de reprise** non jouée : je suis un sous-agent, et l'état et les passations me sont fermés. Seules les empreintes utiles ont été vérifiées.
- **Sondage de faisabilité**, jetable, dans mon bloc-notes, hors du dépôt, non livré et pas à reprendre comme code :
  - un dépôt servi en HTTP par `git http-backend`, derrière un petit serveur Python qui exige une identification ;
  - un clone partiel par les commandes de l'amorce, extraction sans puis avec l'aide inscrite ;
  - un clone partiel vers un chemin local.

  Serveur arrêté par son PID.
- **Comptes d'essais** : par collecte seule (`--collect-only`), sur une extraction de `c76e7916` dans le bloc-notes, retirée ensuite.

## 2. Le fait, confirmé ; trois précisions à la consigne

### 2.1 Cause

Dans l'amorce au commit `c76e79169` :
- l. 324 : l'aide est définie ; sa chaîne porte `${GH_TOKEN}` à la lettre, lu seulement à l'appel ;
- l. 325 : le clone du code la reçoit par `-c` ;
- l. 326 : elle est inscrite dans sa configuration.

**La consigne dit « l. 326 et 327 » : décalage d'une ligne.**

Pour les entrées :
- l. 362 : le clone partiel (`--filter=blob:none --no-checkout`) reçoit l'aide par `-c`, sans l'inscrire ;
- l. 363 : l'extraction partielle ne tire rien, faute d'index ;
- l. 364 : `checkout` tire les fichiers en différé, sans aide, et le dépôt privé refuse.

### 2.2 Reproduit à la lettre (sondage, git 2.43)

**Code actuel** : extraction en échec, code 128, avec deux lignes :
- « fatal: could not read Username for 'http://127.0.0.1:<port>': terminal prompts disabled » ;
- puis « fatal: could not fetch <objet> from promisor remote ».

Aucun fichier n'est extrait.

**Aide inscrite dans le clone des entrées** : extraction réussie.

Dans les deux cas, la configuration du clone ne porte pas la valeur du jeton.

### 2.3 Pourquoi aucun essai ne l'a vu

- **Essais de l'amorce** : les entrées y sont clonées depuis un chemin local, sans filtre ni identification (`_depot_entrees`, l. 178 à 212).
- **Essai à blanc de l'amorce entière** : l'URL officielle y désigne un chemin local (`insteadOf`), et git ignore le filtre d'un clone local (« warning: --filter is ignored in local clones », vu au sondage). Tous les fichiers sont tirés au clone ; rien n'est descendu en différé ; aucune identification n'est demandée.
- **Répétition générale** : elle n'a pas d'entrées.
- **Épreuve à vérité plantée** : elle ne passe pas par l'amorce.

### 2.4 Le point qui décide de l'admission (absent de la consigne)

Sur l'instance, la marche elle-même appelle `lecture_v1.exiger_code_de_lecture_au_commit` (`relecture_v1.executer`, mode réel, l. 547 et 548). Cette fonction (l. 497 à 513 de `lecture_v1.py`) exige que l'arbre gelé de la tête soit celui du commit de `CODE-LECTURE-B5F`. L'arbre gelé (`CHEMINS_GELES`) couvre tout, sauf `prereg`, `brouillons`, `registres`, `docs`, `diag`, `runs`, `donnees`, `livrables`, `papiers`, `traces` et `CLAUDE.md`. Ce programme est figé par son empreinte (`ed0999df…` ; liste d'arrêt, point 10).

**Un commit de la marche qui porterait l'amorce ou `relecture_v1.py` retouchés serait donc refusé trois fois** :
- par « verifier » de la version 1 ;
- par la vérification (a) de la commande ;
- par la marche sur l'instance, après la dépense.

L'ouvreur le refuserait aussi : `garde_d_ouverture` appelle la même fonction.

Le premier exemple de la consigne (« un commit de la marche qui ne diffère de `c76e7916` que par une liste fermée de différences ») n'est donc pas admissible sans toucher au programme de lecture.

Mais **l'amorce jouée sur l'instance n'est pas celle de l'arbre** : c'est celle que la commande emporte en base64 (`echo … | base64 -d > /root/amorce_b5f_lecture_v1.sh`). C'est par là que la correction passe, l'arbre restant égal.

## 3. La correction minimale

### 3.1 Voie recommandée (B) : une ligne ajoutée, rien d'autre

**Lieu** : `scripts/amorce_b5f_lecture_v1.sh` tel qu'au commit `c76e79169` (`54a676f35bde811e8ebcfb0f643d510c2a1a79ca6a8554d61b7a39dd8e44453f`, 33 412 octets, 404 lignes). La ligne 362 reste telle quelle :

```
    git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_ENTREES" "$DEPOT_URL" "$E" || arret "clonage des entrées de lecture" 2
```

**Ligne ajoutée juste après**, qui devient la l. 363 (quatre espaces ; « é » en forme composée ; fin de ligne LF) :

```
    git -C "$E" config credential.helper "$AIDE" || arret "aide d'identification non inscrite dans le clone des entrées" 2
```

**Résultat** : 405 lignes, 33 536 octets, sha256 **`0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001`**. L'empreinte est calculée sur les octets figés. Toute retouche de la chaîne la change : le développeur la recalcule, le contre-lecteur la recoupe.

**Pourquoi l'inscription, et non `-c` à l'extraction** (qui marcherait aussi) :
- c'est le geste du clone du code (l. 326) ;
- elle vaut pour toute descente différée ultérieure dans ce clone ;
- la valeur du jeton n'est pas écrite (vu au sondage).

**Pourquoi `|| arret`**, quand la l. 326 n'en a pas : aucun repli silencieux (R5). L'asymétrie est voulue.

**Branche de sortie** : nom inchangé. La branche existante est traitée avant la relance (§ 3.4).

### 3.2 Autre voie (A), en une ligne

Voie A (nom neuf `donnees/barreau5-familles-jumelles-v1-lecture-r1`, sans exception à R12) : elle comporte trois changements.
- une seconde différence à l'amorce, l. 103 (`…-v1-lecture";;` → `…-v1-lecture-r1";;`) ; amorce `27b1166a3a8114185d7299a9c83dc1fb0e6b5cf56de0291820a8953dd167fb12`, 33 539 octets ;
- une sous-commande « scores » neuve dans la version 3 : la garde figée `ligne_scores` (l. 1139 à 1144 de `relecture_v1.py`) exige `origin/…-lecture`, et `relecture_v1.py` ne peut pas changer (§ 2.4) ;
- un écart à la lettre de « Données gardées », qui nomme la branche.

### 3.3 Pesée des deux voies

| | Voie B (recommandée) | Voie A |
|---|---|---|
| Différences à l'amorce | 1 ligne ajoutée | 1 ligne ajoutée, 1 ligne changée |
| Code neuf pour la ligne des scores | aucun : « scores » figé de la version 1 | sous-commande neuve et ses essais |
| Garde figée remplacée pour la ligne des scores | aucune | `ligne_scores` |
| Noms écrits en dur | inchangés | un changé en jeu (l. 103) ; trois restent faux sans être joués (l. 961 de `relecture_v1.py`, l. 8 du lanceur v1, l. 100 de l'amorce) |
| « Données gardées » | tenu à la lettre | écart (nom de la branche) |
| Mandat de la session | versement et scores inchangés ; une précision sur la référence distante (§ 8.2) | pas 8 (branche) ; « scores » par la version 3 |
| Règles du dépôt | exception nommée à R12, règle gelée | aucune |
| Réversibilité | suppression définitive ; rien de perdu (même commit sous un autre nom) | rien n'est supprimé |

**Verdict de la pesée.** B réduit nettement le code touché : une seule ligne hors de l'arbre gelé, aucune garde figée remplacée, aucun nom changé, le texte tenu. Son coût est une exception à une règle gelée, que seul Lazar peut accorder. **Recommandation : B, confiance moyenne.** Si Lazar refuse l'exception, A est prête : mêmes pièces, deux éléments de plus.

### 3.4 Gestes de la voie B

Ils sont faits par la mère ou le conducteur, après le mot de Lazar, jamais par la session de lecture. Aucun fichier n'est ouvert.

1. **L'instance tombée (62047649)** est traitée d'abord, si elle existe encore : inventaire, puis destruction par son identifiant, selon le mandat (§ 5.4, pas 9). On le fait tant que la branche de sortie porte encore le commit prouvé.
2. **Tête H de `donnees/barreau5-familles-jumelles-v1-lecture`** : relevée par `git ls-remote` (attendue `81061453…`, en 40 signes), puis récupérée par le nom entier vers une référence distante.
3. **Copie.** On vérifie que `traces/barreau5-lecture-tentative-1` est absente du dépôt distant ; sinon arrêt (R12). Puis `git push origin H:refs/heads/traces/barreau5-lecture-tentative-1`. C'est le même commit : les cinq fichiers et tout son arbre, à l'octet.
4. **Vérifications de la copie** : la tête de la branche neuve égale H. `traces-b5f-lecture/inventaire-final.json` y est, à l'empreinte de la marche tombée (`cae5107f…`), vérifiée par calcul, sans affichage.
5. **Suppression** de `donnees/…-lecture` sur le dépôt distant (`git push origin --delete …`), en citant le mot de Lazar. Vérification par `git ls-remote --exit-code` : code 2, branche absente. Si une garde du dépôt refuse ce geste, on ne la contourne pas : on le dit.
6. **La branche de la répétition** (`…-repetition`) n'est pas touchée.

## 4. L'admission par les gardes figées

### 4.1 Ce que vérifient les gardes, et où

| Où | Garde | Effet d'un arbre gelé changé |
|---|---|---|
| « verifier », v1, arbre figé | registre au commit de la marche ; arbre gelé de la session égal à `CODE-LECTURE-B5F` ; arbre que l'amorce extraira | refus |
| « commande », v2, arbre de commande | (a) arbre gelé du commit de la marche égal au code figé ; (b) tête = commit cité par `GO-LECTURE-B5F` ; (c) ce commit = code figé + liste fermée ; (d) format de la référence ; **amorce prise au commit de la marche** | refus en (a) |
| marche, sur l'instance | registre ; `exiger_code_de_lecture_au_commit` sur la tête du clone ; entrées ; arbre propre | refus après la dépense |
| amorce, sur l'instance | arguments ; branche de sortie absente (l. 355, R12) ; entrées en un seul commit ; 146 essais ; arbre propre | sans objet |
| lecteur figé du registre propre (`lignes_du_registre`, `engagement_v1.py` l. 130 à 145) | ne lit que les lignes qui commencent par « \| » et portent « -B5F » ; refuse toute clé inconnue ou en double | sans objet |
| ouvreur (`garde_d_ouverture`) | même garde du code au commit, si la racine est donnée | refus |

`GO-LECTURE-B5F` est inscrite : sans elle, la commande v2 n'aurait rien imprimé. Elle cite la commande v2 (`5402367e`) et ne sera pas réécrite.

### 4.2 Voies pesées

- **(i) Corriger dans le commit de la marche** : refusée (§ 2.4).
- **(ii) Un module de commande, version 3**, qui calcule l'amorce corrigée depuis l'amorce figée par la liste fermée des différences, vérifie les deux empreintes et l'embarque : **retenue**. C'est la plus étroite qui reste éprouvable hors ligne. Le code figé ne change pas, et l'empreinte de l'amorce jouée s'écrit au journal de l'instance (l. 280), donc se contrôle après coup.
- **(iii) L'aide par variables d'environnement git** (`GIT_CONFIG_COUNT`, `GIT_CONFIG_KEY_0`, `GIT_CONFIG_VALUE_0`) ajoutées à la commande, l'amorce restant figée : **écartée**, pour quatre raisons.
  - La valeur porte des espaces, des guillemets, « $ » et « ; ». Elle traverse le shell de la session puis l'analyseur d'environnement du loueur, qu'aucun essai local ne peut rejouer : une erreur se paierait d'une instance.
  - Elle vaudrait pour tout appel git de l'instance.
  - Elle ne laisserait aucune trace dans l'empreinte d'amorce du journal.
  - Elle ne suffirait pas à la voie A.
- **(iv) Une ligne libre sous la table, citée par `GO-LECTURE-B5F`** : impossible telle quelle, car la ligne de l'accord est inscrite et ne se réécrit pas. Une ligne libre peut épingler le code à elle seule : c'est le mécanisme d'épinglage de (ii).

### 4.3 La voie retenue, en détail

Le développeur écrit le code ; ce texte en fixe le contenu.

**(a) Le commit de code.**
- Un commit neuf, enfant de `5402367e`, qui ajoute sur les chemins gelés les seuls fichiers de la liste fermée, et rien d'autre.
- Il est poussé sous une branche hors des préfixes fermés à la session (proposition : `commande-b5f/lecture-v3`), puis contre-lu et vérifié.
- Liste fermée, noms neufs (R12) :
  - commande : `src/controle_ia/barreau5_familles/commande_lecture_v3.py`, `scripts/lancer_b5f_lecture_v3.sh`, `tests/test_commande_lecture_v3.py`, `tests/test_amorce_b5f_lecture_identification_v1.py` ;
  - ouverture (§ 5) : `src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py`, `scripts/lancer_b5f_ouverture_suffixes_v1.sh`, `tests/test_ouverture_suffixes_v1.py`.

**(b) Constantes du module de commande v3.**
- `AMORCE_FIGEE_SHA256` = `54a676f3…`.
- `PAIRES_AMORCE` = la paire du § 3.1 (texte ancien : la l. 362 et sa fin de ligne ; texte neuf : la même, suivie de la ligne ajoutée). Voie A : plus la paire de la l. 103.
- `AMORCE_CORRIGEE_SHA256` = `0adb6efb…` (voie A : `27b1166a…`).
- `BRANCHE_SORTIE` = `donnees/barreau5-familles-jumelles-v1-lecture`, égale en voie B à `relecture_v1.PIECES_LECTURE["decisif"]["branche"]` (un essai le vérifie) ; voie A : `…-lecture-r1`.
- `ERRATUM_SHA256` = l'empreinte de la version de cet erratum que le code applique, après contre-lecture.
- `LISTE_FERMEE_REUNIE` = la liste v2 et les sept fichiers.

**(c) `amorce_corrigee(octets)`.**
- Elle exige l'empreinte figée.
- Chaque texte ancien doit être présent une fois et une seule.
- Elle remplace, exige l'empreinte corrigée et rend les octets.
- Toute autre entrée : refus.

**(d) Ligne d'épinglage.** Elle s'écrit au registre propre, sous la table, hors de toute ligne de table. Format exact :

```
Erratum de chaîne de la relecture décisive (barreau 5) : erratum sha256 <64 signes> ; commande de lecture v3, commit <40 signes>, vérifiée sha256 <64 signes> ; accord <GO-AAAA-MM-JJ-NN> ; branche de sortie donnees/barreau5-familles-jumelles-v1-lecture
```

Règles :
- elle ne commence pas par « | » : le lecteur figé du registre l'ignore donc (vu au code, l. 134) ;
- elle ne porte ni « | » ni saut de ligne ;
- elle est en forme composée (« î », « é »), sans aucun caractère combinant ;
- **une seule** ligne commence par le préfixe et porte l'objet « commande de lecture v3 » ;
- l'erratum cité égale `ERRATUM_SHA256` ; la branche égale `BRANCHE_SORTIE` ;
- l'empreinte qui suit « vérifiée » (le rapport de vérification du code) est lue pour sa forme seulement ;
- l'accord est le mot de Lazar pour la relance (deux ou trois chiffres au rang final).

**(e) Vérifications, dans cet ordre, avant le corps.**
- **(a)** inchangée : `relecture_v1.exiger_code_du_commit`.
- **(d)** inchangée : `commande_lecture_v2.commit_de_commande_cite`, qui exige que la référence de `GO-LECTURE-B5F` cite l'additif et rend le commit v2.
- **(d')** : la ligne d'épinglage donne le commit v3.
- **(c')** : le commit v3 descend de `c76e7916` et du commit v2 cité. Sur les chemins gelés, il n'en diffère que par des ajouts, tous de la liste fermée réunie, et des fichiers ordinaires seulement : un lien symbolique est refusé, ce qui referme la remarque laissée par la vérification v2. Le module et le lanceur v3 sont présents.
- **(b')** : la tête de l'arbre de la session est le commit v3 ; arbre de travail inchangé sur les chemins gelés ; aucun fichier non suivi sous `src/`. Le module est joué depuis cet arbre.

**(f) Le corps.** C'est celui de la commande v2 (`corps_recompose`), ligne pour ligne, à deux remplacements près :
- le commit de code vient de (d'), (c') et (b') ;
- l'amorce embarquée est `amorce_corrigee(_montrer(racine, commit, AMORCE))`.

Tout le reste est rejoué tel quel par les fonctions des versions 1 et 2 : offre au plafond de stockage de l'additif, configuration, registre, (a), texte, adaptateurs existants, arbre extrait, commit des entrées sur sa branche, échéance, garde de calcul. Aucun attribut d'un module figé n'est affecté. Aucun objet privé n'est importé : les objets privés employés sont récrits à l'identique, avec un essai d'égalité, comme en v2.

**(g) Entrée et lanceur.**
- Seule « commande decisif », avec les arguments de la version 2.
- Le lanceur imprime, avant la commande, l'empreinte de l'amorce embarquée.
- Toute autre sous-commande : refus.
- Voie A : plus « scores RACINE COMMIT_MARCHE COMMIT_PROUVE RUN_ID » ; même calcul que `ligne_scores`, branche `-r1`, après (d'), (c') et (b').

**(h) Ce que le module ne fait pas** : il ne crée, n'arrête ni ne détruit rien ; il n'atteint pas le réseau ; il ne lit aucune sortie.

### 4.4 Ce que le texte scellé permet à la lettre, et ce qui reste un écart

**Permis à la lettre :**
- la ligne d'épinglage : « Lignes de registre » dit « Tout le reste […] s'écrit dans la colonne de référence de la ligne de l'étape, ou sous la table, hors de toute ligne de table » ;
- le programme de lecture inchangé (point 10) et l'arbre gelé inchangé ;
- l'aveugle tenu : rien n'est lu.

**Ce que disent les textes, et où ils s'arrêtent :**
- **Point 18 (a)** ne permet que « la correction d'une erreur de chaîne par erratum », écrit pour une erreur vue par la répétition générale. Ici, la répétition n'a pas d'entrées et ne pouvait rien voir : l'erreur est vue par la relecture décisive elle-même.
- **Mandat, § 5.3** : même règle pour une répétition tombée (« seule suite permise : un erratum contre-lu »).
- **Mandat, § 9, point 5** (pièce de lecture tombée) : « rien de relancé avant un mot de Lazar ». Le texte n'a aucune règle de relance pour la lecture.
- **Liste d'arrêt, point 12** : la relance se décide sur une ligne d'étape (« ARRET : commit des entrées … introuvable »), avant toute relecture. Il n'y a là aucune sortie de ce plan, aucun score, aucune grandeur d'adaptateur. Mais elle n'est pas dans la liste des règles mécaniques : elle passe par le mot de Lazar.
- **Règle du dépôt** « une panne technique n'est pas un résultat » (GO-2026-11-22-77) : une panne d'identification donne droit à une relance sur le même accord. C'est un faux échec, d'issue « jamais parti ». Les gardes « aucune relance après dépense » restent, sauf décision nommée ; ici, c'est la garde R12 de l'amorce.

**Écarts qui restent** : voir le § 9.

## 5. La variante de la table à noms suffixés

### 5.1 Ce que fait le code figé

**La table engagée** est la forme canonique de `{nom, famille, membre, sel}`. Les noms opaques suivent l'ordre des HMAC du sel sur « famille/membre » (`engagement_v1.py`, l. 68 à 91). Une même famille écrite `T03` ou `T03-x1` donne donc d'autres noms et une autre empreinte. Personne ne sait laquelle des deux a été engagée (`553cb395…`).

**Noms possibles d'une famille formée** (`formation_v1.py`, l. 89 à 92 ; `lecture_v1.py`, l. 540 à 561) :
- la base, `T01` à `T10` ;
- puis `-x1` si son instance est citée par `GO-RELANCE-FORMATION-B5F` ;
- puis `-r1` après un retirage.

La copie lue est `prefixe_de_copie(base, relance)`, ou ce nom suivi de `-r1`. « Pièce » ne règle que l'arrêt (famille ou instance), pas les noms.

**Avec une table nue**, rien ne change.

**Avec une table suffixée**, les deux entrées figées refusent :
- `preparer` refuse : `couts_depuis_formation` → `_familles_formees` → `prefixe_de_copie`, l. 551, « famille de base … attendue » ;
- `ouvrir` refuse : `garde_d_ouverture`, l. 529 à 531, famille hors de `T01` à `T10`.

**Une table traduite à la main** serait refusée deux fois : noms qui ne se redérivent plus du sel (`exiger_table_coherente`), empreinte différente de l'engagement.

**Si `preparer` passait avec des clés suffixées**, la boucle de la copie lue d'`ouvrir` (l. 1365 à 1370) les sauterait en silence. La traduction rétablit cette garde.

### 5.2 Les deux listes écrites d'avance, et la règle

Rien de ce qui suit n'a lieu avant les gardes figées sur la table d'origine T :
- `exiger_table_coherente(T)` ;
- empreinte de T égale à `ENGAGEMENT-B5F` et à `OUVERTURE-B5F` ;
- dates engagement < scores < ouverture (`verifier_table_a_l_ouverture`).

Ensuite :
1. **Graphie.** Chaque famille de T se lit par le motif fermé `(?P<base>T(?:0[1-9]|10))(?P<relance>-x1)?(?P<retirage>-r1)?`, celui de la formation réduit aux familles tenues à l'écart. Toute autre graphie : refus (« suffixe inconnu »).
2. **Une seule graphie par base** dans T ; sinon refus (« deux graphies pour une famille »).
3. **Paires et sel** : P = les paires (base, membre) de T ; s = le sel unique de T.
4. **Copie lue c(base)** : celle que donne la formation par les fonctions figées. Dans `preparer`, c'est le champ « copie » de `resume_formation_depuis_branche`, tiré de la branche de la formation par `_familles_formees`. Dans `ouvrir`, c'est le même champ du résumé, contrôlé par `exiger_copie_lue`. `-x1` vient de la ligne de relance, `-r1` de la sortie formée.
5. **Les deux listes.** Liste (a) : [(base, membre)]. Liste (b) : [(c(base), membre)]. E_a et E_b sont les empreintes de `table_des_etiquettes(s, liste)`.
6. **La règle.**
   - E_a égale l'engagement : **variante (a)**, entrée figée ; aucun code neuf n'est joué, le module neuf refuse.
   - Sinon, E_b égale l'engagement : **variante (b)**.
   - Sinon : refus, nœud.
   - Sans famille relancée ni retirée, (a) et (b) coïncident : variante (a).

« Écrites d'avance » : les règles de graphie sont fixées ici. Les paires viennent de la table engagée, déjà vérifiée par son empreinte. Les suffixes viennent de la ligne de relance et des sorties de la formation, jamais de la table.

### 5.3 La traduction contrôlée

- **Seulement en variante (b)**, après le point 6 : T_nu = T, chaque famille réduite à sa base ; noms opaques, membres et sel inchangés.
- **Puis les gardes figées des l. 529 à 532**, jouées sur T_nu : famille dans `T01` à `T10`, membre connu, nom `X-NN`, aucune paire en double.
- `exiger_table_coherente` et l'égalité à l'engagement **ne sont jamais jouées sur T_nu** : elles échoueraient par construction. Elles l'ont été sur T, avant. Aucune autre garde ne change.
- **Trace.** La table de traduction (graphie vers base, par famille), E_a, E_b, l'engagement et l'empreinte de cet erratum s'écrivent dans un fichier scellé à côté du résultat (`traduction-table-b5f.json`). Le résultat garde son format (`b5f-resultat-lecture-v1`).

### 5.4 Ce que cela touche dans le code figé

**Rien n'est modifié.** `lecture_v1.py` reste à son empreinte, vérifiée par `programme_sha256`, appelée.

**Un module neuf recompose, ligne pour ligne, trois fonctions** : `preparer` (l. 1480 à 1495), `garde_d_ouverture` (l. 516 à 535) et `ouvrir` (l. 1351 à 1385). Il le fait à trois remplacements près :
1. cohérence, engagement, ouverture et dates, jouées sur T ;
2. la règle des deux listes et la traduction, placées avant les gardes de ligne, qui sont jouées sur T_nu ;
3. la garde du code au commit (`exiger_code_de_lecture_au_commit`), qui refuserait l'arbre du commit de code, remplacée par (d'), (c') et (b'), comme la commande v2 l'a fait.

Le `preparer` recomposé vérifie de plus l'engagement, l'ouverture et la règle, ce que le `preparer` figé ne fait pas : c'est un renfort, exigé par « seulement après l'égalité d'empreinte ».

**Tout le reste est appelé tel quel** : `lire_registre_de_lecture`, `programme_sha256`, `exiger_table_coherente`, `verifier_table_a_l_ouverture`, `empreinte_table`, `table_des_etiquettes`, `exiger_arbre`, `exiger_arbre_sans_etiquettes` (qui reconnaît déjà les noms suffixés, l. 396), `charger_entrees`, `partition_des_plis`, `charger_arbre`, `exiger_copie_lue`, `exiger_alignement`, `lire`, `couts_depuis_formation`, `resume_formation_depuis_branche`, `sceller`. Les objets privés employés sont récrits à l'identique, avec un essai d'égalité de source.

**Non retenu, au choix du contre-lecteur** : vérifier les compagnons de `couts.json` et `formation.json` à la relecture (`_lire_json` ne le fait pas, dans le code figé non plus).

### 5.5 Admission : la même voie que l'amorce

- **Commit.** Le même commit de code, ou un commit à part au choix de la mère. La règle (c') vaut pour l'un comme pour l'autre : le commit de l'ouverture descend de `c76e7916`, sans exigence sur le commit v2.
- **Ligne d'épinglage propre**, sous la table, avant `OUVERTURE-B5F`. Même format qu'au § 4.3 (d), sans champ de branche :

  ```
  Erratum de chaîne de la relecture décisive (barreau 5) : erratum sha256 <64 signes> ; ouverture à noms suffixés v1, commit <40 signes>, vérifiée sha256 <64 signes> ; accord <GO-AAAA-MM-JJ-NN>
  ```

- **Ce que joue l'ouvreur**, depuis un arbre de travail au commit épinglé :
  - d'abord `variante RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json`, qui rend les trois empreintes et « a », « b » ou un refus ;
  - en (a), l'entrée figée, comme prévu (lanceur v1, depuis un arbre dont la partie gelée est celle du code figé) ;
  - en (b), `preparer` puis `ouvrir` du lanceur neuf, avec les arguments de la version 1.
- **Limites du module** : il refuse d'être joué depuis un autre arbre. L'ouverture recomposée sans racine n'existe que pour les essais, comme « monde ».

### 5.6 Essais, écrits avant le code

**Cas sain (b).** Un monde fabriqué par la fabrique figée (`epreuve_verite_plantee_v1.fabriquer`) et son jumeau suffixé, bâti par un outil d'essai :
- même sel ; une instance relancée, une famille retirée ;
- noms opaques redérivés ; renommage cohérent dans tous les fichiers du monde ;
- inventaire, `SCORES-B5F`, `ENGAGEMENT-B5F` et `OUVERTURE-B5F` recalculés au registre fabriqué ;
- champ « copie » du résumé posé selon la règle.

**Parité.** Pour chaque monde de `liste_mondes()`, le rendu du traducteur figé (`traducteur_verite_plantee_v1`, qui ne porte aucun nom opaque) doit être le même pour l'entrée figée sur le monde nu et pour l'ouverture recomposée sur le jumeau. Les mondes dont l'artefact porte sur la table refusent tous deux.

**Témoin (a).** Table nue : `variante` dit (a) ; l'entrée figée passe ; le module neuf refuse (« variante (a) »).

**Artefacts :**
- suffixe inconnu (`T03-y1`, `T03-x2`, `T03-r1-x1`, `T11`) ;
- deux graphies pour une famille (`T03-x1` et `T03` ; `T03-x1` et `T03-x1-r1`) ;
- table retouchée (une graphie, un nom ou le sel changés après l'engagement) : refus par l'engagement, avant toute traduction, aucun fichier écrit ;
- graphie hors règle (`-x1` sans ligne de relance ; `T05` quand la copie lue est `T05-r1`) : ni (a) ni (b) ;
- `OUVERTURE-B5F` différente de la table ;
- famille d'apprentissage dans la table ;
- doublon après traduction ;
- (d'), (c') et (b') comme pour la commande.

**Mutations qui doivent rendre un essai rouge :**
- traduire avant la vérification d'engagement ;
- tirer la liste (b) de la table au lieu de la formation ;
- admettre deux graphies ;
- oublier `-r1` dans la règle ;
- jouer `exiger_table_coherente` sur T_nu.

### 5.7 Limites

- **Troisième graphie.** Une table écrite sur une troisième graphie (par exemple `-x1` sans `-r1` alors qu'un retirage a eu lieu) n'égale ni (a) ni (b) : refus à l'ouverture, nœud. Une troisième liste demanderait un mot neuf.
- **Lever l'incertitude d'avance.** Si la session de formation est encore joignable, une question fermée de la mère (« graphie des familles de la table : nue, ou nom formé ? ») suffirait, sans rien livrer de la table. C'est au conducteur d'en juger.

## 6. Les essais (R5), écrits avant le code

### 6.1 L'essai qui aurait vu le défaut

Fichier : `tests/test_amorce_b5f_lecture_identification_v1.py`.

**Le monde :**
- un dépôt nu servi par `git http-backend`, derrière un serveur Python local (127.0.0.1) qui exige « Authorization: Basic » avec un jeton factice, et répond 401 sinon. Le gestionnaire CGI de la bibliothèque est déprécié en Python 3.13 : un petit gestionnaire maison suffit ;
- réglages du dépôt : `uploadpack.allowFilter=true` (suffit au protocole 2 pour la descente différée) et `http.receivepack=true` (versement) ;
- une branche du code, montée comme dans `test_amorce_b5f_lecture_entiere_v1.py`, dont les faux outils sont réemployés (import ou copie déclarée) ;
- une branche des entrées : un commit de base, puis un commit qui ajoute le dossier ;
- l'URL officielle désigne le serveur par `insteadOf`, et non un chemin local, qui ferait ignorer le filtre ;
- environnement : `HOME` et configuration globale propres à l'essai, `GIT_CONFIG_NOSYSTEM=1`, `GIT_TERMINAL_PROMPT=0`, aucun `GIT_ASKPASS`, variables de mandataire retirées, `NO_PROXY=127.0.0.1,localhost` ;
- serveur arrêté par `shutdown()` ; aucun réseau extérieur.

**Artefact, le défaut.** L'amorce figée (fichier de l'arbre), jouée en essai à blanc :
- journal « ARRET : commit des entrées <C> introuvable » ;
- sortie d'erreur qui porte « could not read Username » et « promisor remote » ;
- branche de sortie créée avec les seules traces : c'est l'incident, rejoué.

**Artefact, R12 tenue.** Branche de sortie présente : l'amorce corrigée refuse (« branche de sortie … présente sur le dépôt distant (R12) ») avant tout clone des entrées.

**Cas sain (voie B).** On copie la branche sous `traces/barreau5-lecture-tentative-1` (même commit), on la supprime, puis on joue l'amorce corrigée (`amorce_corrigee`, écrite dans un fichier jetable). On attend :
- entrées extraites, fausse marche, versement sur `…-lecture`, preuve, témoin ;
- `relecture_v1.ligne_scores`, figée, accepte le commit prouvé ;
- le clone des entrées porte l'aide, sans la valeur du jeton ; le jeton factice n'est écrit dans aucun fichier ni dans le journal.

Voie A : sans suppression, branche `-r1`, « scores » v3.

**Témoins.**
- Une requête sans identification reçoit 401.
- Le cas sain ne vaut que parce que l'amorce figée tombe, dans ce même monde, sur le motif du défaut.
- `remote.origin.promisor` n'est pas un témoin : git le pose même quand il ignore le filtre (vu au sondage).

**Mutations qui doivent rendre le cas sain rouge** : la ligne ajoutée retirée ; ou placée après l'extraction.

### 6.2 Essais de la commande v3

Fichier : `tests/test_commande_lecture_v3.py`, sur le modèle de `test_commande_lecture_v2.py` (dépôt jetable : code, commit v2, commit v3, marche).

- **`amorce_corrigee`** : cas sain ; artefacts : autre empreinte d'entrée, texte ancien absent, présent deux fois, empreinte de sortie différente.
- **Différence fermée** : la commande v3 égale à l'octet la commande v2, jouée depuis l'arbre v2 du même monde, hors du segment base64. Les deux segments, décodés, sont l'amorce figée et l'amorce corrigée ; leur différence ligne à ligne est exactement la ligne du § 3.1.
- **(a) et (d)** : les artefacts de la v2.
- **(d')** : ligne absente, présente deux fois, autre empreinte d'erratum, accent décomposé, barre verticale, autre branche, autre objet.
- **(c')** : ne descend pas de `c76e7916` ou du commit v2 cité ; fichier modifié, supprimé, ajouté hors liste ou en lien symbolique ; module ou lanceur absent.
- **(b')** : autre tête ; arbre de travail changé ; fichier non suivi sous `src/` ; module joué depuis un autre arbre.
- **Autres gardes** : toutes refusent comme en v1 et v2 (liste paramétrée de la v2) ; le plan « repetition » est refusé.
- **Intégrité** : aucune substitution dans les modules neufs (analyse de l'arbre syntaxique, comme en v2) ; modules figés intacts après import et appel ; liste fermée du module égale à celle de ce texte.
- **Lanceur v3** : seule « commande decisif » ; refus de toute autre sous-commande ; aucune création, aucun arrêt, aucune destruction joués.

### 6.3 Essais existants à rejouer

Comptes relevés à la collecte, au commit `c76e7916`.

- **Arbre figé** (commit de la marche) :
  - relecture 24, lanceur v1 43, engagement 23 (mandat, § 5.1) ;
  - plus amorce 51 et amorce entière 4 : l'amorce figée du dépôt n'a pas changé et ne voit pas le défaut ; ces essais doivent rester verts ;
  - facultatif : lecture 102, sondes 20 et relecture 24, soit 146, le plancher de l'amorce sur l'instance.
- **Arbre de commande** (commit v3) :
  - commande v2 : 113 passés et 1 sauté, selon le rapport de vérification ;
  - les trois fichiers d'essais neufs ;
  - lecture 102 et épreuve à vérité plantée 155, le programme et la fabrique sur lesquels reposent les essais de parité.
- **Pour tous** : `--tb=no -rN -q -p no:cacheprovider --basetemp=<bloc-notes>`, rien laissé dans les arbres (mandat, erratum 2, point 3, et erratum 3).

## 7. Ce qui ne change pas

**Textes et lignes :**
- le texte scellé (`bdff244f…`) ;
- l'engagement (`553cb395…`) ;
- `GO-LECTURE-B5F` : contenu `GO-2026-11-19-86`, référence qui cite la commande v2.

**Entrées** : même branche, même commit (`f6e2072d…`).

**Code figé** : tout l'arbre gelé de `c76e7916`, dont :
- le programme de lecture (`lecture_v1.py`, `ed0999df…`) ;
- `relecture_v1.py` (`f6bd8c15…`) ;
- les sondes (`sondes_v1.py`) et la notation ;
- le lanceur v1 ;
- l'amorce figée du dépôt (`54a676f3…`) : le fichier ne change pas, seule l'amorce embarquée diffère.

**Réglages de la pièce :**
- l'accord de calcul cité par la commande (`GO_ID=GO-2026-11-19-86`) ;
- la coupure tenue par la session, 14 USD (chiffre de la consigne) ;
- l'échéance que calcule le code (coupure du devis, 21 USD, au prix de l'offre) ;
- la garde des activations `une_sur_dix` ;
- la règle des scores fermés : aucune statistique sur l'instance, journaux d'étapes et de comptes seulement ;
- l'étiquette `b5f-lecture-v1`, le disque de 300 Go, la carte et les bornes de l'offre, le plafond de stockage de l'additif ;
- `DIVERGENCE` et la liste des points d'ancrage ;
- l'ordre des étapes de l'amorce et le plancher d'essais de 146.

**Le reste :**
- en voie B, le nom de la branche de sortie ;
- la répétition et sa branche ;
- le format du résultat de lecture.

## 8. La relance

### 8.1 Avant la relance

Mère et conducteur, dans cet ordre :
1. le mot de Lazar (§ 10) ;
2. le code v3 écrit, contre-lu, vérifié et poussé ;
3. l'instance tombée traitée (§ 3.4, geste 1) ;
4. les gestes de la voie B (§ 3.4) ;
5. la ligne d'épinglage de la commande sous la table, d'où un commit de la marche neuf (enfant de `2beeec31`, qui ne diffère que sous `registres/`) ;
6. le registre des accords à jour dans les arbres d'où la commande se joue ;
7. l'erratum 4 au mandat (§ 8.5).

### 8.2 Ce que la session fait de neuf

- **Arbres** : arbre de commande au commit v3, récupéré par le nom entier de sa branche, au lieu de `5402367e` ; arbre figé au commit de la marche neuf.
- **Essais** : ceux du § 6.3.
- **« config » et « verifier »** de la version 1, comme avant, sur le commit de la marche neuf.
- **« commande decisif »** par `scripts/lancer_b5f_lecture_v3.sh`, avec les arguments de la v2. L'identifiant de marche est neuf (l'ancien n'est jamais repris) ; les entrées sont les mêmes.
- **Avant de jouer la commande** : l'empreinte imprimée est `0adb6efb…`, et le segment base64 décodé y est égal.
- **Après la création** : la ligne du journal « amorce de lecture v1 : empreinte … » porte `0adb6efb…`. Sinon : arrêt de l'instance par son identifiant (R10), appel du conducteur.
- **Voie B, référence distante périmée.** Si un dépôt de la session a récupéré l'ancienne `…-lecture`, il la met à jour par une récupération forcée par le nom entier (`+refs/heads/<nom>:refs/remotes/origin/<nom>`) avant « scores » et « detruire ». Sinon, `ligne_scores` refuserait à tort.
- **« scores », « detruire » et « verifier-destruction »** de la version 1, depuis l'arbre figé. Voie A : « scores » de la v3.

### 8.3 La ligne de l'accord de lecture

`GO-LECTURE-B5F` reste inchangée : ni réécrite, ni doublée.

### 8.4 À inscrire

- **Registre propre** :
  - la ligne d'épinglage de la commande ; avant `OUVERTURE-B5F`, celle de l'ouverture ;
  - aucune ligne à clé neuve ; `SCORES-B5F` ensuite, comme prévu ;
  - si la relance est menée par une autre session que celle que nomme `GO-LECTURE-B5F`, sa désignation sous la table : version de la liste « qui a lu quoi » consultée, catégorie vérifiée (point 7).
- **Registre des accords** : le mot de Lazar, qui porte sur la relance, sur l'exception nommée à R12 (ou la voie A) et sur la variante d'ouverture.
- **Registre des dépenses** : une ligne d'engagement neuve pour la relance ; coupure de 14 USD ; dépense antérieure égale au cumul commun relevé, marche tombée comprise.
- **Registre des arrêts** : l'instance tombée.
- **Registre des idées de la veille de cap** : un faux échec, issue « jamais parti » (GO-2026-11-22-77).
- **Liste « qui a lu quoi »** : le concepteur de cet erratum, son contre-lecteur, le développeur et le vérificateur du code v3 entrent dans la catégorie (a) des exclusions du point 7. Aucun d'eux ne sera ouvreur, lecteur du verdict ni agent de l'audit de symétrie.

### 8.5 Erratum 4 au mandat de la session (par le conducteur)

- § 3, point 6 : la liste de lecture devient le module, le lanceur et les essais v3, avec le rapport de vérification ;
- § 5 : le commit et la branche de code ; la ligne d'épinglage ;
- § 5.1 : les arbres et les essais ;
- § 5.4, pas 5 (lanceur v3), pas 6 (contrôles de l'empreinte de l'amorce), pas 8 (référence distante ; voie A : branche et « scores ») ;
- § 9, point 5 : la relance a son accord.

## 9. Écarts à déclarer

1. **La relance elle-même.** Le texte ne règle pas la relance d'une pièce de lecture tombée : le point 18 (a) est écrit pour la répétition, et le mandat, § 9, point 5, renvoie au mot de Lazar. La relance se décide sur une ligne d'étape, avant toute relecture (liste d'arrêt, point 12).
2. **La branche de sortie.** Voie B : exception nommée à R12 (branche de sortie supprimée après sa copie à l'octet, nom réemployé). Voie A : écart à la lettre de « Données gardées ».
3. **L'amorce jouée n'est plus l'amorce figée** par `CODE-LECTURE-B5F` : une ligne est ajoutée (`0adb6efb…` au lieu de `54a676f3…`), vérifiée par le module v3. L'arbre gelé reste égal. Le point 7 (« son programme est figé ») est tenu pour le programme, non pour l'amorce.
4. **L'épinglage.** Le code v3 est épinglé par une ligne libre sous la table, et non par la référence de `GO-LECTURE-B5F`.
5. **L'ouverture recomposée**, si la table est suffixée. L'épreuve à vérité plantée inscrite (`EPREUVE-B5F`) porte sur l'entrée figée ; la recomposition est éprouvée par parité.
6. **Le mandat de la session** : erratum 4 (§ 8.5).
7. **Le concepteur.** Conception par Opus, et non par Fable (« Qui conçoit ») : couvert par GO-2026-11-22-145.
8. **Mes lectures** : lectures de code hors de la liste de la consigne, et sondage jetable (§ 1).
9. **La consigne elle-même** : « l. 326 et 327 » au lieu de 325 et 326 ; et l'exemple d'un commit de la marche qui ne diffère que par une liste fermée, qui n'est pas admissible (§ 2.4).
10. **Exclusions du point 7** pour les quatre auteurs du code v3 (§ 8.4).

## 10. Nœuds pour Lazar

Aucun défaut ne s'applique : ce sont des nœuds (dépense, règle gelée, écart à un texte scellé). On attend le mot.

**1. Relance.**
- **Décision** : relancer la relecture décisive sur cet erratum, sous l'accord de calcul GO-2026-11-19-86, avec une coupure de 14 USD.
- **Enjeu** : une panne d'identification avant la marche ; aucun calcul fait. Sans relance, pas de relecture décisive, donc pas de verdict du barreau 5. Le calendrier du texte veut le verdict au plus tard le 29.
- **Options** : relancer, soit une marche de plus à l'attendu du devis ; ou ne pas relancer.
- **Recommandation** : relancer. Confiance haute.

**2. Branche de sortie.**
- **Décision** : voie B (exception nommée à R12) ou voie A (nom neuf `-r1`).
- **Enjeu** : une règle gelée, contre du code de plus et un écart au texte scellé.
- **Options** :
  - B : une ligne d'amorce, aucune garde figée remplacée, texte tenu ; mais une branche supprimée pour de bon, sans rien perdre ;
  - A : aucune exception ; mais une ligne de plus, une sous-commande neuve à la place de la garde figée « scores », et un écart à « Données gardées ».
- **Recommandation** : B. Confiance moyenne.

**3. Admission.**
- **Décision** : admettre que l'amorce embarquée diffère de l'amorce figée d'une ligne fermée, par un code de commande v3 épinglé sous la table.
- **Enjeu** : c'est la seule voie qui laisse égal l'arbre gelé que vérifient la marche et l'ouvreur.
- **Options** : admettre ; ou refuser, et rouvrir le code figé, ce qui demanderait une seconde ligne `CODE-LECTURE-B5F`, que le registre refuse : en pratique, une version neuve du texte.
- **Recommandation** : admettre. Confiance haute.

**4. Variante d'ouverture.**
- **Décision** : accorder d'avance la règle des deux listes et la traduction contrôlée.
- **Enjeu** : sinon, si la table est suffixée, l'ouverture s'arrête au jour L+1 et attend un nouvel erratum.
- **Options** : accorder d'avance (code écrit et éprouvé maintenant, joué seulement en (b)) ; ou attendre le jour de l'ouverture.
- **Recommandation** : accorder d'avance. Confiance moyenne à haute.

**Pour le conducteur, non pour Lazar** :
- un commit ou deux pour le code ;
- la question fermée à la session de formation (§ 5.7) ;
- l'ordre des gestes (§ 8.1).

Ce texte n'écrit aucun code. Aucun commit, aucune poussée, aucun appel payant, aucune commande vers le loueur.
