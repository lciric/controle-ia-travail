# Contrôle de la condition (4) de la garde de recouvrement (ligne 3, étage 2) — v1

Pièce de travail (classe C), écrite le 2026-11-20 sous le mandat `mandat-controleur-condition-4-garde-recouvrement-v1.md` (`c7f395df0255f19f4a37aad18d5b0f2b7d1bc8afad5531d6da4f84840f08b726`, recalculée égale à son compagnon). Contrôleur neuf, modèle O, qui n'a écrit ni le générateur, ni le code d'appel, ni le texte de la ligne 3.

## Verdict

**Non conforme.** Un point n'est pas tenu : le compte des rejeux (point 5), parce que le journal est choisi par argument et peut être créé de nouveau ; le compte peut donc repartir de zéro et le refus au sixième rejeu peut être tourné sans le mot de la mère. Le chemin du repli (point 6) en hérite pour sa seule règle « le compte continue ». Les points 1 à 4 sont tenus. **Le défaut ne touche pas l'entrée des 94 cartes** : ce n'est pas un déclencheur du repli. Il se corrige dans le code, qui est contre-lu de nouveau ; d'ici là, la garde ne tourne pas (texte v7, l. 263).

**Cette pièce ne doit pas être passée à `--controle-4`.** Le programme n'en vérifie que le chemin et l'empreinte, pas le verdict (remarque R1).

## Pièces (empreintes recalculées, égales à leur compagnon)

| pièce | sha256 |
|---|---|
| texte v7 `preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, l. 30 et 257 à 263 | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| `generateur-v1/generer_temoins_ligne_3_v1.py` (lu en entier pour la garde : l. 1-400, 820-1259, 1590-1664 ; le reste par l'analyse statique) | `b264760c2234d00972f4c217f55e1233327824164f1e02beb7554910cd9c6dbb` |
| `generateur-v1/rapport-developpeur-generateur-etage-2-v1.md` (en entier ; § 5 point par point) | `c447ed60d6d6b23ab4d67a1c9dda321f304999fb1a01fc1846ff5559b92d0589` |
| `generateur-v1/essais_generer_temoins_ligne_3_v1.py` (lu par recherche seulement : voie d'essai, l. 108-126, 693-737) | `79bd8d87cf2c6d0b7fd9fd809e05255dd5203d271d2930074cfef122b3d89add` |
| analyse statique à moi (arbre syntaxique, sans import du programme) : `analyse_statique_v1.py` et sa sortie `analyse-statique-sortie-v1.txt`, dans mon dossier | `a9f80807bc283e2c01ba58902d55fec6be1da6d90e4e5ec47ec2846a5ed98265` ; `9654c76b03065fd14db26de0de7206e5c3af293f55fb8c533a2ebd22b0760750` |

Aucune commande sur un chemin sous `archives-reponses-modeles/` ; le fichier des cartes n'a pas été ouvert. Je n'ai lancé ni la garde, ni le générateur, ni ses essais. Aucun appel à un fournisseur, aucune écriture dans le dépôt.

Les numéros de ligne ci-dessous renvoient à `generer_temoins_ligne_3_v1.py` (`b264760c…`).

## Points

### 1. Entrée unique — **tenu**

- Chemin, empreinte et compte sont des constantes, l. 125-128 ; ils sont égaux à la lettre au texte v7, l. 258 et 30 (chemin sous le dépôt, `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`, 94). Les sept cartes du repli (l. 129-130) sont égales à l'en-tête, l. 30.
- La production ne prend que ces constantes : `EntreeCartes.production`, l. 846-848 ; défaut l. 1117. Aucune variable d'environnement n'est lue (aucun `environ` ni `getenv` dans tout le programme, d'après l'analyse statique). `DEPOT` est en dur, l. 59.
- La ligne de commande ne permet aucune autre entrée : `principal`, l. 1608-1622, ne transmet `entree_cartes` que s'il est passé en Python ; `__main__` n'en passe aucun, l. 1663.
- Une seule ouverture, l. 857-860 / 1173. L'empreinte est calculée sur les octets et comparée **avant** toute analyse du texte, l. 1174-1176 : si elle est autre, `EmpreinteCartesAutre`, ni garde ni repli. Le compte de 94 est vérifié l. 1185-1186, **avant** toute comparaison : les bardeaux de référence sont faits l. 1189-1192, la comparaison l. 1195. Entre l'empreinte et le compte, il n'y a que le chargement (lecture du JSON, retrait de `meta`, l. 1177), nécessaire pour compter.
- Aucun autre chemin de l'archive : `garde_chemins` passe sur la banque, le journal, la sortie, la pièce du (4) et la pièce du repli **avant toute ouverture**, l. 1125. Elle contrôle la forme écrite puis le chemin réel, liens symboliques résolus, l. 335-353. Ces deux pièces repassent par la garde des chemins, l. 1055. La seconde entrée est une constante hors de l'archive, l. 114-115 et 871.
- La voie d'essai ne peut pas atteindre le vrai fichier. `EntreeCartes.essai`, l. 850-855, passe `garde_chemins` (composant `archives-reponses-modeles` ou commençant par `coffre`, forme écrite et chemin réel) avant de construire l'entrée. Les essais ne passent que par elle (essais l. 118 et 724-726) ; `production()` n'y est que construite, jamais lue (essais l. 736-737).
- Réserves, non bloquantes (R3 à R5) : le constructeur nu `EntreeCartes(...)` (l. 841) contourne la garde des chemins pour un appelant Python ; un lien physique hors de l'archive échapperait à `garde_chemins` ; il reste une fenêtre entre la vérification et l'ouverture.

### 2. Retrait du champ `meta` — **tenu à la lettre ; suffisance sous réserve de la forme réelle du fichier**

- L. 912 : chaque carte est recopiée sans sa clé `meta` de premier niveau, dans `cartes_du_fichier` (l. 895-916), appelée dès que l'empreinte est vérifiée (l. 1177). Avant ce retrait, rien n'utilise `meta` : le choix de la forme (l. 900-909) ne regarde que les types. Après, l'identifiant (l. 913), le compte (l. 1185), les sept cartes du repli (l. 919-928) et les bardeaux (l. 1190-1192) ne voient que la carte sans `meta`. L'objet complet est supprimé l. 915.
- Profondeur : premier niveau de chaque carte seulement. Une clé `meta` imbriquée dans un autre champ reste lue et entre dans les bardeaux (le développeur le dit au silence 3).
- C'est suffisant au sens du texte (« le champ `meta` de chaque carte », l. 259 ; « champ `meta` retiré », l. 30) **si** `meta` est une clé de premier niveau de chaque carte, dans l'une des trois formes admises. Cela n'est pas établi : c'est le silence 1 du développeur, la forme réelle du fichier n'est écrite nulle part. Autre cas : dans la forme `{identifiant: carte}`, une clé `meta` placée au niveau du fichier serait prise pour une carte (l. 904-905). Elle entrerait dans le compte, d'où un refus `CompteCartesAutre` hors repli, et pas dans les bardeaux. À confirmer **avant le premier passage**, sans ouvrir le fichier (code qui l'écrit). Durcissement conseillé et peu coûteux : retirer `meta` à toute profondeur, et refuser une clé `meta` au niveau du fichier dans la forme dictionnaire.

### 3. Aucune écriture d'un bardeau ou d'un texte de carte — **tenu**

J'ai suivi chaque voie de sortie de la garde (analyse statique : toutes les écritures, sorties standard et d'erreur, sous-processus, gestionnaires d'exceptions) :
- Fichiers. Le manifeste est écrit l. 1166, **avant** l'ouverture (l. 1173) : rien n'y vient du fichier. La ligne « ouverture » du journal aussi, l. 1168. Après l'ouverture, il ne sort que la ligne « clôture » (l. 1213-1215 : décision, trois comptes, lieu de l'exception) et le rapport validé (l. 1226, par `ecrire_rapport_garde`, l. 976-978).
- Bardeaux. Ils ne vivent qu'en variables locales (l. 1189-1196, `del`) ; aucun n'est passé à une écriture.
- Sortie standard : seulement le rapport validé, l. 1629. Sortie d'erreur : rien dans le geste `garde` (les `print` sur la sortie d'erreur, l. 1652-1658, ne servent qu'aux autres gestes, qui n'ouvrent pas le fichier des cartes).
- Sous-processus : `git rev-parse` seulement, sortie capturée, l. 324, et appelé avant l'ouverture (l. 1151).
- Exceptions. Toutes sont attrapées (`BaseException`, l. 1201, 1216, 1227, 1623). `lieu_de` (l. 931-938) ne rend que le nom de la classe, le nom du programme et un numéro de ligne. La trace est détachée (l. 1203, 1218, 1229, 1625). Les refus de la garde sont des classes sans texte (l. 192-269).
- Avertissements : changés en exceptions dans le corps de la garde, l. 1123-1124.
- `repr` d'objets : aucun dans la garde.
- J'ai passé en revue les opérations faites sur les données des cartes après l'ouverture (décodage, JSON, retrait de `meta`, identifiants, bardeaux, l. 1173-1195). Aucune ne peut lever une exception dont le message porte du texte de carte, et le fichier est déjà vérifié par empreinte quand on l'analyse.
- Remarque R6, non bloquante, lettre de la condition (5) : l. 1611-1612 et 1627-1629 sont hors de tout `try`. Un échec à cet endroit (lecture du programme dans le gestionnaire, l. 1627 ; écriture sur la sortie standard, l. 1629) afficherait une trace Python brute. D'après ce qui précède, elle ne porterait aucun texte de carte, mais une trace brute est affichée, ce que la l. 262 interdit. À durcir : un seul `try` qui couvre tout `principal` pour le geste `garde`, sans rien recalculer dans le gestionnaire, et `__suppress_context__`.

### 4. Liste fermée des champs de sortie — **tenu**

- L. 138-140 : treize champs, ceux de la l. 260. `valider_rapport_garde` (l. 941-973) refuse tout champ hors liste. Elle contrôle aussi la forme de chacun des treize : entiers ; empreintes ; décision parmi trois ; identifiants pris dans la banque ; compte par témoin refusé ; exception réduite à trois clés ; repli égal à la mention et à l'un des deux déclencheurs.
- Chaque écriture du rapport passe par cette validation : sur disque, l. 977 avant 978 ; en retour et sur la sortie standard, l. 1232, et l. 1628 au niveau de la ligne de commande. Si l'écriture échoue, un rapport minimal est validé, l. 1231-1232. Aucune voie ne la contourne (analyse statique : aucune autre écriture de `r`).
- Remarques, non bloquantes. Les lignes du journal ne sont contrôlées que par leur jeu de clés (l. 1021-1025), pas par la forme des valeurs ; leurs valeurs viennent toutes du programme. Le manifeste n'a pas de liste fermée, mais il est écrit entier avant l'ouverture. Le rapport minimal de la l. 1231 perd `nombre_de_rejeux`, alors que la l. 260 le veut au rapport.

### 5. Compte des rejeux — **non tenu**

Ce qui est tenu :
- Le journal est à ajout seul (`O_APPEND`, `fsync`, l. 1021-1034) et lu en entier au lancement (l. 1131), avant l'ouverture. Absent : `JournalRejeuxAbsent`. Illisible (octets, JSON, numéro de ligne, jeu de clés, rang) : `JournalRejeuxIllisible`, l. 985-1016.
- La ligne « ouverture » est écrite avant l'ouverture (l. 1168), donc toute exécution qui ouvre est comptée, panne comprise.
- Le premier passage est au rang 1, rejeu 0 (l. 1167-1171).
- Refus au sixième rejeu (`jr.ouvertures >= 6`, l. 1139-1141) avant l'ouverture, sans `--mot-de-la-mere`. Un même mot ne vaut qu'une fois (l. 1142-1143) ; le mot est cité au manifeste (l. 1161).

Ce qui ne l'est pas :
- **Le journal n'est pas unique.** Son chemin est un argument libre (`--journal-rejeux`, l. 1617). `creer-journal-rejeux` crée un journal vide sur tout chemin neuf (l. 1037-1049, l. 1632-1635), et de nouveau sur le même chemin s'il a été supprimé (le mode exclusif, l. 1041, ne protège que contre l'écrasement). Une exécution qui ouvre le fichier des cartes peut donc être inscrite au rang 1 d'un journal neuf. Cela contredit la lettre de la l. 262 : « il ne repart jamais de zéro », et « toute exécution suivante qui ouvre ce fichier en est un ». Le refus au sixième rejeu se tourne alors sans le mot de la mère. Il n'en reste de trace que dans des manifestes séparés, sans aucun refus du programme. Ce n'est pas une hypothèse d'école : un journal perdu donne bien `JournalRejeuxAbsent`, mais si l'on refait simplement le journal, le compte repart de zéro.
- Correction attendue, au choix du développeur, à contre-lire de nouveau :
  - le chemin du journal **et** celui de son manifeste de création deviennent des constantes du code, hors de l'archive ;
  - `creer_journal_rejeux` refuse si ce manifeste de création existe déjà ;
  - la garde exige ce manifeste, et que le journal soit celui qu'il nomme.
  
  Une suppression des deux fichiers à la main resterait possible, mais ce serait un geste délibéré hors du programme, visible.
- Remarque, non bloquante : aucun verrou. Deux exécutions simultanées liraient le même compte. La suivante trouverait des `n_ligne` en double et refuserait (journal illisible), ce qui va dans le sens prudent.

### 6. Chemin du repli — **tenu pour ses règles propres ; hérite du non-tenu du point 5 pour « le compte continue »**

- Les deux déclencheurs sont des constantes (l. 133-134). Une cause hors des deux donne `ReplisHorsDeclencheur` (l. 1134-1136), avant l'ouverture. La pièce du déclencheur est exigée par chemin et par empreinte (l. 1137).
- Même fichier, même ouverture, même empreinte (l. 1173-1176 : autre empreinte, ni garde ni repli). Même retrait de `meta` (l. 1177). Les sept cartes nommées (l. 1183, 919-928) sont trouvées chacune une fois et une seule, sinon refus. Même liste fermée ; le repli figure au rapport sous la forme exacte « repli sur sept cartes » avec sa cause (l. 1200, 969-973) ; l'écart est déclaré au manifeste (l. 1162-1164). La pièce du (4) est exigée aussi sous le repli (l. 1133).
- Sous le repli, le compte de 94 n'est pas exigé (l. 1182-1183 ; silence 2). C'est conforme à la lettre du repli, l. 263, qui cite l'empreinte et non le compte.
- « Le compte des rejeux continue sous le repli » : c'est le même journal, donc le même défaut qu'au point 5. La correction du point 5 suffit.

## Remarques hors des six points

- **R1.** La garde exige la pièce du (4) par son chemin et son empreinte (l. 1133, 1052-1062), pas par son verdict : elle tournerait avec une pièce « Non conforme », celle-ci comprise. Je conseille que la correction exige, dans la pièce, une ligne de verdict fixe (« **Conforme** ») et l'empreinte du programme contrôlé, comparée à `programme_sha256()`. Même chose pour la pièce du repli.
- **R2.** La garde ne vérifie pas que le programme qui tourne est celui qui a été contrôlé : elle rapporte son empreinte (l. 1119) sans la comparer. R1 couvrirait ce point.
- **R3.** Le constructeur nu `EntreeCartes(...)` et `EntreeV2(...)` (l. 841, 866) n'appliquent pas `garde_chemins`. Les essais ne les emploient pas. Conseil : faire passer `garde_chemins` dans le constructeur pour toute nature autre que « production ».
- **R4.** Lien physique, et fenêtre entre la vérification d'un chemin et son ouverture : hors de portée du programme ; à tenir par la procédure.
- **R5.** Le texte (l. 30, 258) situe le fichier « (branche) ». Le programme lit `DEPOT/archives-reponses-modeles/…` sur disque. S'il n'y est pas, le premier passage est consommé (ligne « ouverture » écrite, puis échec de lecture). Personne ne doit le vérifier par une commande sur ce chemin : à régler par la procédure (code qui écrit le fichier, geste de mise en place) avant le premier passage.
- **R6.** Trace brute possible hors des `try` (point 3).
- **R7.** Commandes de l'additif (rapport du développeur, § 8) : `python3 -B`. Conseil : `-I -B`, pour qu'aucun module du dossier courant ne soit chargé.

## Ce qui manque pour « Conforme »

Pour les points 5 et 6 : l'unicité du journal des rejeux et de sa création (point 5 ci-dessus), puis une nouvelle contre-lecture du code corrigé. Les remarques R1, R6 et le durcissement de `meta` (point 2) sont conseillés dans la même correction ; ils ne fondent pas à eux seuls le « non conforme ».

Contrôleur de la condition (4), modèle O.
