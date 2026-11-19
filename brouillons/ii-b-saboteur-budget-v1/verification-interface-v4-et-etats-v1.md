# Vérification courte du côté exposé : note d'interface v4 et programme des états des lectures du saboteur à budget — v1

> **EXPLORATOIRE, NON OPPOSABLE (R-522).** Rapport du côté exposé, **jamais montré au côté moniteurs** : il cite le code revu et décrit des pièces fermées au côté moniteurs.

- **Vérificateur** : agent neuf, Opus 5.5, côté exposé, sur mandat de la session mère `session_013QMayjsoZJFBUCqcnvD5h1` ; autorisé à ouvrir la conception finale, l'ordre brouillon 8 et le code revu `ec3b0329` ; **désormais exclu de tout rôle côté sondes du barreau 8**. Ouvert : le code revu, par `git show` seulement. **Non ouverts** : la conception, l'ordre, tout fichier dont le nom contient « consigne-privee », la branche `lot/compte-4-v1`, l'enveloppe de la huitième tâche, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.
- **Écrit** le 2026-11-19 vers 00:54Z (UTC, `date -u`), sur la branche `claude/iib-executante-v1`, commit `4f446c97d3207325f4ad412d223b0ca612c05b88` (récupéré par `git fetch`, jamais extrait dans l'arbre de travail : pièces tirées par `git show` et `git archive` dans le bloc-notes de la session).
- Lignes du registre lues : R-3558, R-3562, R-3565, R-3566 de `registres/decisions.md`.

## Verdict

**« transmissible après ces couples »** — **dix couples** : quatre sur la note v4 (N-01 à N-04), trois sur le programme des états (P-01 à P-03), trois sur ses essais (T-01 à T-03). Une décision d'organisation est soumise à la mère dans N-03 ; une réserve d'organisation, sans couple, au § 4.

- La v4 est la v3 **à l'octet** hors des six remplacements déclarés ; le programme de fabrication la rejoue à l'identique.
- Les six remplacements n'introduisent **aucun mécanisme**, **aucun fragment de la consigne privée** (jugé sur le texte ajouté, la consigne n'étant pas ouverte) et **aucun réglage du saboteur ni de l'oracle**. Deux inexactitudes de fait et un manque (place de l'extrait) : N-01 à N-03.
- Le programme des états ne laisse passer, **par construction**, que des valeurs prises dans le vocabulaire de la note, sous des clés constantes ; il **n'ouvre jamais** le fichier des mots pondérés (vérifié par un crochet d'audit des ouvertures). Son dictionnaire est **égal à l'octet** à ce que les lectures (1) et (2) écrivent au code revu. Une seule chaîne libre passe : le nom du run, tiré de la ligne de commande (P-03).
- **Ordre du temps : tenu seulement par la conduite.** Le programme écrit l'extrait sans aucune trace du scellement du texte du côté moniteurs. Garde proposée (P-01), prototypée et éprouvée sur un cas sain et huit artefacts.

## Pièces et empreintes (recalculées par `sha256sum` sur les pièces extraites, égales aux compagnons `.sha256` du commit)

| pièce | empreinte |
|---|---|
| `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v3.md` | `477815d1b48fc681ae4d403f81cf6f6fcff5750611e74f784db802013eed05f1` |
| `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v4.md` | `1983692a79b4802a4d13edc3cf9a9bb21eca0dfb2c860ecf5831431d532c99f7` |
| `docs/notes/barreau8-iib-v1/differences-interface-v3-vers-v4.md` | `f668f845bfe1b6e48ddd5f31f4c89b6fb01c88c4173817caa9f990963ad74b13` |
| `docs/notes/barreau8-iib-v1/appliquer-changements-interface-v3-vers-v4.py` | `98f6a48e14229b9ae196c683c1cc4eafc5e44dc0c0f81cb444c5ba638de51349` |
| `docs/notes/barreau8-iib-v1/changements-interface-v3-vers-v4.json` | `abf2ead2ea75c546f794a4fae2688b3a006031cbc971aba5abd92da3f0529705` |
| `scripts/extrait_iib_etats_lectures_cote_moniteurs_v1.py` (programme des états) | `55e3edbc3c98a784ebcd67659cb15a6d49f1d8a9bee2c305785c335d0264e20a` |
| `tests/test_iib_extrait_etats_lectures_v1.py` (ses essais) | `0ee9900926a95f0fb8548a2c0a341ef200f084cef7d55dbbd7341604d27d309e` |

Toutes égales aux empreintes du mandat (préfixes compris).

## 1. La v4 est la v3 à l'octet, hors des six remplacements

- **Rejeu** : `appliquer-changements-interface-v3-vers-v4.py` joué (`python3 -I -B`) sur la v3 et le fichier des changements, vers un chemin neuf du bloc-notes : « changement 1 appliqué » … « changement 6 appliqué », sortie `1983692a…c99f7`, **identique à l'octet** à la v4 (`cmp`).
- **Contrôle indépendant** (lecture en octets, sans la conversion des fins de ligne de `read_text`) : aucun retour chariot ni marque d'ordre des octets dans les deux versions ; chaque « avant » est présent **une seule fois dans la v3 d'origine** (et non seulement dans le texte déjà modifié, ce que contrôle le programme) ; les six zones ne se chevauchent pas (positions 82, 796, 1173, 2835, 11646, 17123) ; la v3 reconstruite par positions, hors de ces zones, est **égale à la v4**.
- La différence unifiée recalculée (`diff -u`) est égale, ligne pour ligne hors des deux lignes d'en-tête, à celle qu'affiche `differences-interface-v3-vers-v4.md` (37 lignes chacune).

## 2. Les six remplacements

| n° | place dans la v4 | ce qu'il fait | jugement |
|---|---|---|---|
| 1 | titre | « v2 » → « v4 » (le titre de la v3 portait encore « v2 ») | correct ; rien d'autre |
| 2 | en-tête, « Version 4 » | date, mot de la mère, deux ajouts nommés | rien de la fabrication |
| 3 | en-tête, provenance | « La version 1, la liste des différences… » → « Les versions précédentes, les listes des différences… restent du côté exposé » | **inexact** : la v3 est dans le dossier d'entrées du côté moniteurs, portée sur `main` (R-3563 ; vérifié : `origin/main` porte `…/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v3.md`). Couple N-01 |
| 4 | « Livraison », alinéa neuf | extrait des seuls états, livré après le scellement du texte du côté moniteurs, sans chiffre | aucun mécanisme ; mais (a) l'alinéa précédent dit encore « les seuls textes… sont cette note et l'extrait du point (b) » ; (b) ni la place ni le nom de l'extrait ne sont donnés, alors que la lecture du côté moniteurs doit refuser de s'ouvrir sans lui (R-3565, décision 2) ; (c) « sans aucun chiffre » : l'extrait porte le nom du run (date et heure) et les noms des conditions. Couples N-02, N-03 |
| 5 | question (9), « Portée » | une seule phrase du dommage pour la course, décidée sur la pleine dose | **exact au code revu** : `lecture_v1.lecture_1` (l. 118-133 à `ec3b0329`) rend un seul champ `phrase`, choisi sur les effets appariés pleine dose contre honnête et pleine dose contre témoin-jumeau (après la garde du nombre minimal de tâches communes). Déjà transmis au côté moniteurs par la mère (R-3566 a). Renvoi au code revu de même nature que les renvois de provenance déjà présents |
| 6 | point (e) | exception faite de l'extrait des états | cohérent avec 4 |

Aucun des six n'apporte un mot sur ce que fait le saboteur, sur ce sur quoi les adaptateurs sont appris, ni une valeur de réglage du saboteur, de la règle d'acceptation ou de l'oracle.

**Hors des six remplacements, porté de la v3** (relevé parce qu'il contredit le remplacement 3) : le point (e) ferme « dans le dossier de cette note, la version 1 … et les pièces qui ont fait la version 2 ». Depuis la v3, la note est dans `docs/notes/barreau8-cote-moniteurs-entrees-v1/`, alors que ces pièces sont dans `docs/notes/barreau8-iib-v1/` (vérifié par `git ls-tree` au commit), avec la version 2 de la note et les pièces des versions 3 et 4, qui ne sont pas nommées. La règle de la mère (R-3562, décision 2 : dans ce dossier, le côté moniteurs ne lit que ce que la mère lui nomme) n'est pas dite dans la note. Couple N-04.

## 3. Le programme des états

### 3.1 Ce qui sort, par construction
- Les clés de sortie sont toutes des constantes du programme : `avertissement`, `run_id`, `lecture_dommage.phrase`, `lecture_diffusion.par_paire.<paire>.<base>` (paires « B100-H », « B50-H », « TJ100-H » avec `cout`, `traits`, `mots_et_cout`, `unite` ; « B100-TJ100 » avec `mots_et_cout`), `lecture_diffusion.phrase`.
- Chaque valeur lue passe par `_dans` (l. 47-50) : refusée si booléen, si ni chaîne ni `null`, ou si elle n'est pas **égale** à une valeur permise. Une valeur rendue est donc égale à une constante du programme : quinze champs catégoriels (une phrase du dommage, dix états de jeu, trois états d'unité, une phrase de la diffusion), rien d'autre.
- Les messages de refus n'impriment jamais la valeur refusée ni les clés en trop (ils impriment les clés attendues).
- **Seule chaîne libre** : `run_id`, tiré de la ligne de commande, non contrôlé, recopié dans la sortie (essai D-1 ci-dessous : un nom de run « aire 0,71 seuil 0,05 » passe et s'écrit). Au déroulement normal, c'est le nom du dossier des lectures, créé au lancement sous la forme exigée par `manifeste._RUN_ID` (`^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$`, code revu), et le côté moniteurs le connaît déjà par les chemins du point (b) : ce n'est pas un canal des lectures, mais la propriété « sans aucun chiffre » n'est tenue que par la conduite. Couple P-03.
- Ce que l'extrait laisse inférer : les états voulus, rien de plus. Une phrase de la diffusion non nulle ne s'obtient, au code revu, qu'avec certains états des autres sorties de la lecture (2), dont la règle reste fermée au côté moniteurs ; ce n'est ni un mécanisme ni un réglage, et l'extrait arrive après le scellement. Pas de couple.

### 3.2 Le fichier des mots pondérés n'est jamais ouvert
- Par lecture du code : seuls `NOM_DOMMAGE` et `NOM_DIFFUSION` (et leurs compagnons, par `verifier`) sont ouverts.
- Par essai : un crochet d'audit des ouvertures (`sys.addaudithook`, évènement `open`) relève, pendant un appel sain, **exactement quatre fichiers** sous le dossier du run : les deux lectures et leurs deux compagnons ; aucun chemin ne contient « mots-ponderes ». Un **dossier** posé au nom du fichier des mots pondérés (toute ouverture échouerait) laisse l'extrait s'écrire.
- Les essais livrés ne le prouvent pas : ils vérifient seulement que le contenu des mots ne parvient pas à la sortie. Couple T-03.

### 3.3 Le dictionnaire correspond à ce que les lectures écrivent au code revu (`ec3b0329`)
- Comparaison par l'arbre syntaxique des littéraux de `src/controle_ia/iib/lecture_v1.py` et `bases_textuelles_v1.py` (extraits par `git show`) : les quatre phrases du dommage, les trois états, la phrase de la diffusion et les trois unités sont présents **à l'octet** (forme normale composée des accents, apostrophe et trait d'union simples), ainsi que les deux noms de fichiers. Ils sont aussi présents à l'octet dans la note v4.
- Phrase du dommage : `lecture_1`, l. 126-133 (quatre valeurs, une seule phrase). Phrase de la diffusion : `lecture_2`, l. 393 (la phrase ou `None`).
- Jeux : `lecture_2`, l. 369-371, boucle `f"{base}/{pos}-{neg}"` sur `cout`, `traits`, `mots_et_cout` × trois paires, plus « B100-TJ100 » pour `mots_et_cout` seul : **égale** à `JEUX` (dix clés). État d'un jeu : « non calculable » (l. 292) ou « réussit » / « échoue » (l. 296).
- États d'unité : `etat_par_unite.unites` (l. 390-392), rendus par la fonction d'état de la pièce, que `bases_textuelles_v1.etat_unite` (l. 277) **arrête** hors des trois mots ; la pièce elle-même (`scripts/mots_et_cout_t06_v3.py` à `da06bb57`, empreinte `9dbcc55c…e674` égale à `PIECE_SHA256`) rend les mêmes trois mots.
- Les deux sorties sont écrites telles quelles, au premier niveau, par `lecture_v1.ecrire` (l. 403-408) et scellées ; `verifier` lève une garde sur toute empreinte différente.

### 3.4 Essais joués
- **Essais livrés** (arbre extrait par `git archive` au commit, `-p no:cacheprovider`, `--basetemp` dans le bloc-notes) : **19 passed** (2 cas sains, 17 artefacts), comme dit R-3566.
- **Mes artefacts neufs** (fichier du bloc-notes `test_artefacts_verificateur.py`, `795cbd10e24d64ade71abec837a190ed8d0df24aefc729c541c0a10d0297da2c`) : **26 passed**.
  - (A) **Valeurs hors vocabulaire, refusées**, rien d'écrit, valeur non imprimée : état « réussit » en forme décomposée, avec une espace finale, « non calculable » avec une espace insécable, chaîne vide, liste, objet, entier, nombre non défini ; phrase de la diffusion vide, « null » écrit en texte, zéro, faux, objet ; phrase du dommage en forme décomposée ; clé `etat` absente d'une unité.
  - (B) **Clés imbriquées, refusées** : jeux imbriqués par base au lieu de clés plates, état donné comme objet imbriqué, unité en trop, unités sous une profondeur de plus, clé de jeu prolongée (« cout/B100-H/aire »). Clés imbriquées **à côté** d'un état permis : ignorées, non recopiées (vérifié sur la sortie).
  - (C) Non-ouverture du fichier des mots pondérés (§ 3.2).
  - (D) **Constats**, qui passent aujourd'hui : D-1 nom de run libre recopié ; D-2 une lecture (2) qui cite l'empreinte d'une **autre** lecture (1) (champ `lecture_1.sha256`, que le script de la lecture (2) écrit au code revu) est acceptée (couple P-02) ; D-3 l'extrait s'écrit sans aucun registre du côté moniteurs (§ 4).

## 4. Ordre du temps

- **Tenu seulement par la conduite.** Le programme ne lit aucune trace du scellement du texte du côté moniteurs (essai D-3) ; la phrase de la note « livré seulement après le scellement » n'est garantie par aucun code.
- **Garde proposée (P-01)** : refuser d'écrire tant que le registre propre du côté moniteurs, `registres/sondes-iib-v1.md` (nom et clé fixés par R-3548, alignés sur le barreau 7 ; le fichier n'existe encore ni sur `main` ni sur les deux branches vues), ne porte pas **une seule** ligne `| SCELLEMENT-SONDES-IIB | AAAA-MM-JJTHH:MM:SSZ | chemin | empreinte |` bien formée, datée au plus tard maintenant, dont le fichier cité (chemin relatif, sans « .. ») est scellé avec l'empreinte de la ligne. Prototype éprouvé (fichier du bloc-notes `test_garde_ordre_du_temps_prototype.py`, `e9a1f771ec07146492af1d5551623c8362ef816f6a367f1bd5d6a71b66b87820`) : **9 passed** — un cas sain ; huit artefacts refusés (registre absent, ligne absente, deux lignes, empreinte autre, texte changé après sceau, date future, empreinte de 63 caractères, chemin sortant). Corps du prototype :

```python
CLE = "SCELLEMENT-SONDES-IIB"
LIGNE = re.compile(r"^\| SCELLEMENT-SONDES-IIB \| (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) \| ([^|]+?) \| ([0-9a-f]{64}) \|\s*$")

def exiger_texte_des_sondes_scelle(racine: Path, registre: Path) -> str:
    if not registre.is_file():
        raise GardeArret("registre propre du côté moniteurs absent : l'extrait n'est écrit qu'après le scellement de son texte")
    lignes = [l for l in registre.read_text(encoding="utf-8").splitlines() if l.startswith(f"| {CLE} |")]
    if len(lignes) != 1:
        raise GardeArret(f"{CLE} : {len(lignes)} ligne(s) au registre propre, une seule exigée")
    m = LIGNE.match(lignes[0])
    if not m:
        raise GardeArret(f"{CLE} : ligne mal formée")
    date, chemin, sha = m.group(1), m.group(2).strip(), m.group(3)
    if datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) > datetime.now(timezone.utc):
        raise GardeArret(f"{CLE} : ligne datée dans le futur")
    if Path(chemin).is_absolute() or ".." in Path(chemin).parts:
        raise GardeArret(f"{CLE} : chemin cité non relatif à la racine")
    if verifier(racine / chemin) != sha:
        raise GardeArret(f"{CLE} : le texte cité n'a pas l'empreinte de la ligne")
    return sha
```

- La garde rend impossible l'existence d'un extrait avant la ligne de scellement ; la remise dans le dossier d'entrées reste un geste de la mère, après l'écriture.
- **Réserve d'organisation (sans couple)** : la lecture de la diffusion refuse de tourner sans une ligne de `registres/decisions.md` qui cite l'empreinte de la sortie de la lecture du dommage ; or ce registre est commun et lu par le côté moniteurs. Si les lectures tournent avant la ligne `SCELLEMENT-SONDES-IIB`, la ligne consignée ne doit porter que le chemin et l'empreinte, **jamais la phrase ni un état**. Recommandation : ne jouer les deux lectures qu'après cette ligne (confiance 0,7) ; à défaut, consigner l'empreinte seule.

## 5. Couples

### Sur la note (version 5, nom neuf, même dossier ; fabriquée par programme comme la v4)

**N-01** (en-tête, remplacement 3) —
avant : « Les versions précédentes, les listes des différences, les pièces qui ont fait cette version et les rapports de vérification restent du côté exposé, qui tient la provenance de cette version (point (e)). »
après : « Les versions 1 et 2, les listes des différences, les pièces qui ont fait chaque version et les rapports de vérification restent du côté exposé, qui tient la provenance de cette version (point (e)) ; la version 3, dans ce dossier, est remplacée par celle-ci. »

**N-02** (« Livraison », alinéa « Ce que le côté moniteurs reçoit ») —
avant : « Les seuls textes qui les accompagnent sont cette note et l'extrait sans mécanisme du point (b), transmis par la mère. »
après : « Les seuls textes qui les accompagnent sont cette note, l'extrait sans mécanisme du point (b), transmis par la mère, et l'extrait des seuls états des lectures (alinéa suivant). »

**N-03** (« Livraison », alinéa neuf, remplacement 4 ; place, garde, portée du « sans chiffre ») —
avant : « livré **seulement après le scellement du texte du côté moniteurs** ; il ne porte que le vocabulaire « réussit / échoue / non calculable » et les phrases de cette note (question (9)), **sans aucun chiffre**. »
après : « livré **seulement après le scellement du texte du côté moniteurs**, dans ce dossier, sous le nom `<nom fixé par la mère>` avec son `.sha256` ; le programme qui l'écrit refuse de le faire sans une ligne `SCELLEMENT-SONDES-IIB` au registre propre `registres/sondes-iib-v1.md` dont le texte cité est scellé à l'empreinte de la ligne. Il ne porte que le vocabulaire « réussit / échoue / non calculable » et les phrases de cette note (question (9)), sous des clés fixes [option (a) : `lecture_dommage.phrase` ; `lecture_diffusion.par_paire.<paire>.<base>`, paires « B100-H », « B50-H », « TJ100-H » avec les bases `cout`, `traits`, `mots_et_cout` et l'état de l'unité `unite`, paire « B100-TJ100 » avec `mots_et_cout` ; `lecture_diffusion.phrase`], **sans aucun chiffre** hors du nom du run et des noms des conditions. »
**Décision pour la mère** — donner ou non la forme des clés de l'extrait avant le scellement du texte du côté moniteurs. Enjeu : leur lecture doit refuser de s'ouvrir sans l'extrait (R-3565), et, si leur texte lit un état, son code doit en connaître la clé avant d'être scellé ; mais la forme nomme les bases de la lecture de la diffusion. (a) Donner la forme entre crochets : le code du côté moniteurs peut lire les états ; il apprend le nom de trois bases boîte noire du programme (règle du coût déclaré, traits du texte, mots et coût), sans seuil ni critère, le mode « coût » étant déjà déclaré (question (10)). (b) Ne donner que la place, le nom et la phrase d'avertissement constante : rien de plus avant scellement ; leur garde ne peut alors exiger que la présence et le sceau, et leur texte ne peut lire aucun état par programme. Recommandation (a), confiance 0,65 ; défaut sous 48 heures : (a).

**N-04** (point (e), porté de la v3, hors des six remplacements) —
avant : « dans le dossier de cette note, la version 1 de la note (`interface-passe-cote-moniteurs-v1.md`) et les pièces qui ont fait la version 2 (`differences-interface-v1-vers-v2.md`, `appliquer-couples-interface-v2.py`, `ajouts-interface-v2.json`), qui portent les passages retirés ou y mènent ; »
après : « le dossier `docs/notes/barreau8-iib-v1/`, hors des seuls fichiers que la mère nomme au côté moniteurs : il porte notamment les versions 1 et 2 de la note (`interface-passe-cote-moniteurs-v1.md`, `interface-passe-cote-moniteurs-v2.md`), les listes des différences et les pièces qui ont fait les versions suivantes (dont `differences-interface-v1-vers-v2.md`, `appliquer-couples-interface-v2.py`, `ajouts-interface-v2.json`), qui portent les passages retirés ou y mènent ; »

### Sur le programme des états (version 2, nom neuf ; la v1 reste)

**P-01** (ordre du temps) — ajouter l'argument obligatoire `--registre-sondes` et appeler, **avant** `construire`, la garde du § 4 (`exiger_texte_des_sondes_scelle(racine, registre)`) ; imprimer, au succès, l'empreinte du texte cité par la ligne, pour la consignation. Le docstring le dit.

**P-02** (même chaîne de lectures) — dans `construire`, après la lecture des deux sorties : refuser si `l2["lecture_1"]` n'est pas un objet, si `l2["lecture_1"]["sha256"]` n'est pas égale à l'empreinte rendue par `verifier` sur la sortie de la lecture du dommage, ou si `l2["lecture_1"]["phrase"]` diffère de `l1["phrase"]` ; messages sans valeur.

**P-03** (nom du run ; docstring) — contrôler `run_id`, avant de bâtir le moindre chemin, par la forme du lancement (`controle_ia.manifeste._RUN_ID`, ou une copie déclarée de la même expression) ; refus sinon, sans imprimer le nom. Dans le docstring : « vocabulaire exact de la note d'interface v4 » (au lieu de v3, vocabulaire inchangé) et « aucun chiffre hors du nom du run, fixé au lancement, et des noms des conditions ».

### Sur ses essais (version 2, nom neuf ; la v1 reste)

**T-01** — essais de P-01 : un cas sain (ligne et texte scellé) et les huit artefacts du prototype (registre absent, ligne absente, deux lignes, empreinte autre, texte changé après sceau, date future, empreinte mal formée, chemin sortant) ; les essais existants passent un registre sain.

**T-02** — essais de P-02 et P-03 : lecture (2) qui cite une autre empreinte, phrase recopiée discordante, `lecture_1` absent ; nom de run avec espace, avec « .. » ou hors de la forme du lancement ; les gabarits factices de la lecture (2) portent un `lecture_1` cohérent.

**T-03** — preuve de la non-ouverture du fichier des mots pondérés : soit un dossier posé à son nom (l'extrait s'écrit quand même), soit un crochet d'audit des ouvertures qui relève exactement les quatre fichiers attendus.

## 6. Remarques sans couple

- Une exception autre qu'une garde (contenu non décodable, texte qui n'est pas du format attendu) sort en trace d'appel, code 1, rien n'est écrit et aucune valeur n'est imprimée au-delà d'une position d'octet : pas de repli silencieux.
- L'en-tête garde « hors des couples de cette vérification », devenu ambigu depuis plusieurs vérifications : cosmétique.
- Le remplacement 1 corrige un titre de la v3 qui portait « v2 » : déclaré par la mère (R-3566).

## 7. Refus, écarts, lectures hors mandat

- **Refus** (classifieur, permission, crochet) : **aucun**.
- **Écarts** : (1) dans mon prototype de garde, le cas sain a d'abord échoué parce que sa ligne factice était datée de 01:00Z alors qu'il était 00:52Z ; la garde avait raison (« ligne datée dans le futur ») ; j'ai corrigé la date du gabarit à 2026-11-18T23:00:00Z, non la garde, puis rejoué (9 passed). (2) L'arbre d'essai, extrait par `git archive` au commit, contient le paquet `src/controle_ia/iib/` sur le disque du bloc-notes ; je n'en ai ouvert que ce que je cite, par `git show` au code revu.
- **Lectures hors mandat**, toutes pour fonder un point de ce rapport : extrait de R-3548 (clé `SCELLEMENT-SONDES-IIB` et nom du registre propre) et de R-3567 (recherche de « extrait » : aucune place de l'extrait n'y est fixée) dans `registres/decisions.md` ; `scripts/mots_et_cout_t06_v3.py` au commit `da06bb57` (empreinte et vocabulaire de `etat_dose` seulement) ; au code revu, outre `lecture_v1.py`, `bases_textuelles_v1.py` (`etat_unite`), les deux scripts de lecture et l'expression du nom de run dans `manifeste.py` ; `src/controle_ia/scellement.py` au commit (sens de `verifier`) ; la liste des fonctions de `src/controle_ia/t07/registre_v1.py` et les 1 500 premiers octets de `registres/lecture-sondes-bbis-par-lentilles-v1.md` (forme d'un registre propre : titre et deux lignes) ; `tests/conftest.py` et `pyproject.toml` (pour jouer les essais) ; les **noms** des fichiers de `docs/notes/barreau8-iib-v1/` et du dossier d'entrées, sur trois références.
- Ni commit, ni poussée, ni écriture sous `registres/`. Fichiers écrits : ce rapport et son compagnon ; dans le bloc-notes de la session seulement, les pièces extraites, l'arbre d'essai, deux outils de contrôle (`verif_bytes.py`, `comparer_vocabulaire.py`), deux copies de modules du code revu tirées par `git show`, et les deux fichiers d'essais cités avec leur empreinte, qui ne durent pas au-delà de la session.
