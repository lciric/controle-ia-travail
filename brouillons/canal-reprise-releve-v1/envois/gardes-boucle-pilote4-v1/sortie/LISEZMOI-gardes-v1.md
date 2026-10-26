# LISEZMOI — gardes de la boucle extérieure du pilote 4 et assemblage des dossiers de lecture — v1

Écrit le 2026-10-26 à 07:58:51 UTC (heure lue sur `date -u` dans la commande qui écrit ce fichier) par un sous-agent neuf de la lignée
conv-audit, qui n'a écrit ni le protocole, ni l'objet, ni la carte des facteurs, et n'a lu aucun score, aucun résultat de
course, aucune tâche de la banque. Brief : `LISEZMOI-brief-gardes-v1.md`
(`1fd49f664350f697b50e180f77b968f0742c9735ef3fefc4ba3e0b18e7f7e9ee`, empreinte vérifiée), et trois messages de conv-audit
reçus pendant le travail (§ 7). Pièces vérifiées avant lecture : `fournis/` contre `EMPREINTES-fournis-v1.txt` (85 sur 85) ;
`fournis-v2/` par leurs compagnons (3 sur 3). Pièce de travail de la boucle extérieure ; rien n'en est servi à un organisme.

**Textes suivis.** Là où ils diffèrent de ceux du brief, les versions nouvelles l'emportent (premier message de
conv-audit) : protocole de la boucle extérieure v4 (`0e8cfee5c0e25db11965e99bf0d1c45654e9d7e8f72b8dd67f01e2ee2b34d2e4`) ;
briefs des agents v4 (`d5c7a60a7f6a636397b341c5be136a8d4bcec1559d1a5857f77a761295c9d16a`) ; spécification du relevé (B)
v3 (`d6ac5d3fa409ab19b4f3e25b600f4da945c62630a189f2e2463a294506eb4bb5`). Aussi : carte des facteurs et zones interdites
v1 (`2aaedd08…`, `0082519c…`), sous réserve de leur contre-lecture ; décisions E1 à E8 du brief v5 ; brief du script de
lecture v3, avec la correction des libellés (iii) (« changement au-delà du bruit des tâches », « dans le bruit des
tâches », la correction de multiplicité dans un champ à part).

## 1. Pièces

| pièce | rôle | empreinte |
|---|---|---|
| `assembler_dossier_lecture_v1.py` | assemblage des dossiers de lecture (modes course et finale) ; G1, G2 (forme), G8 bis (b), G12 ; contrôles d'identité du § 9 | `a9ab8c76bee058b4d5509bfbaae655cbde1d44827bcb54bbda5311757a0f2259` |
| `garde_g4_arbre_organisme_v1.py` | G4 : arbre de l'organisme corrigé, empreinte d'arbre à épingler | `1f7ced7a83c86646c872a7793bf9f7da56fe24f6c25ba7f96c01626610a197b6` |
| `garde_g5_perimetre_v1.py` | G5 : périmètre, facteurs, zones (carte lue au niveau des colonnes) ; noms gelés (carte v2 annoncée) | `7dd41682612f8a28780b8cab1de38e9e089f1de4ec8b0b6f5012c38cd6c4f9d5` |
| `garde_g6_courses_v1.py` | G6 : aucune mise en regard des deux courses (mots entiers) | `e5d77bffcb38c29e9225dd78e6b007758a7d1f36b8439d45b8c54d7ee1cebc29` |
| `garde_g8_valeurs_v1.py` | G8 : aucune valeur de la liste (marqueurs ou valeurs finales) dans les pièces | `4be3d0717482e1a5579a33da3c47f3cb67767f19bb89e7f2cbcb8b3fa658da31` |
| `garde_g9_entree_lancement_v1.py` | G9 : entrée de lancement avec attente chiffrée | `9524474d1f8fe42a6ebc03476da3255560d875fa142a02625c168d1e12bfe3b6` |
| `essais_gardes_v1.py` | banc d'essais (R5) : chaque garde sur ses cas sains et ses artefacts, sous trois interpréteurs | `a06005f06fd268ae8b2fc64d8fd42d806fbf838d58850d4ea50c4cd3bfad4c13` |
| `journal-essais-gardes-v1.log` | journal des essais (une ligne par essai, heures lues sur date -u) | `47eb11526f42d764da513c88a564985c6a3df44afc1cd625706b591f88e2d2d9` |
| `LISEZMOI-gardes-v1.md` | ce fichier | dans son compagnon |

Chaque pièce a son compagnon `.sha256` (« empreinte, deux espaces, nom nu »). Codes de sortie communs aux six scripts :
0 accepté (ou dossier assemblé) ; 2 usage (arguments, ou fichier `test_final` donné à une garde qui ne l'ouvre jamais) ;
3 refusé, motif sur la sortie d'erreur, sans contenu de pièce ni valeur ; 4 erreur interne (type et ligne seulement).
Python 3.11, 3.12 et 3.13, `python3 -I`, bibliothèque standard seule. Aucun script n'exécute le code de l'objet ; seul
l'assemblage écrit, et seulement son dossier de sortie.

## 2. Commandes exactes

Variables : `GARDES` = dossier de ces scripts ; `DOSSIER` = nom exact du dossier de course poussé
(`pilote4-gemini-v6-2-v1-tentative2` pour la course M, `pilote4-gemini-v6-2-s-v1` pour la course S) ; `COURSE` = copie
poussée de ce dossier de course ; `COMMIT` = tête citée au message de départ de la course ; `ARBRE` =
`4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d` (objet v6.2.1 ; pour une relance, l'arbre que son texte
nomme). Chaque fichier donné en argument a son compagnon `.sha256` à côté de lui.

**2.1 Dossier de lecture d'une course (fin de course ; conv-audit, après l'ouverture).**

```
python3 -I "$GARDES/assembler_dossier_lecture_v1.py" --mode course \
  --dossier "$DOSSIER" --sortie "$LECTURE" --dossier-course "$COURSE" \
  --releve "$RELEVE" --ouverture "$OUVERTURE" \
  --lecture-json "$A_TEST_JSON" --lecture-md "$A_TEST_MD" \
  --registre "$REGISTRE" --protocole "$PROTOCOLE" --script-lecture "$SCRIPT_LECTURE" \
  --commit-attendu "$COMMIT" --arbre-attendu "$ARBRE" \
  --objet "$OBJET" --carte "$CARTE_MD" --zones "$ZONES_MD"
```

`LECTURE` : chemin du dossier à créer (il ne doit pas exister) ; `RELEVE` : `releve-mecanique-$DOSSIER-v1.txt` ;
`OUVERTURE` : `ouverture-lecture-$DOSSIER-v1.txt` ; `A_TEST_JSON`, `A_TEST_MD` : `lecture-$DOSSIER-test-v3.json` et `.md` ;
`REGISTRE` : `registre-hypotheses-conception-pilote4-v5.md` ; `PROTOCOLE` : `protocole-boucle-exterieure-pilote4-v4.md` ;
`SCRIPT_LECTURE` : `lire_pilote4_v3.py` (sa version et son empreinte font la ligne de version du manifeste) ; `OBJET` :
`organisme/` au commit `7ea3270` ; `CARTE_MD`, `ZONES_MD` : `carte-facteurs-v1.md`, `zones-interdites-v1.md`. La sortie
standard donne l'empreinte du manifeste : c'est `<empreinte-manifeste>` des briefs des agents.

**2.2 Dossier de lecture finale (fin du compteur ; conv-audit, après l'ouverture finale).**

```
python3 -I "$GARDES/assembler_dossier_lecture_v1.py" --mode finale \
  --dossier "$DOSSIER" --sortie "$LECTURE_FINALE" --dossier-course "$COURSE" \
  --releve "$RELEVE" --ouverture "$OUVERTURE_FINALE" \
  --lecture-json "$A_FINAL_JSON" --lecture-md "$A_FINAL_MD" \
  --registre "$REGISTRE" --protocole "$PROTOCOLE" --script-lecture "$SCRIPT_LECTURE" \
  --commit-attendu "$COMMIT" --arbre-attendu "$ARBRE"
```

`OUVERTURE_FINALE` : `ouverture-lecture-finale-$DOSSIER-v1.txt` ; `A_FINAL_JSON`, `A_FINAL_MD` :
`lecture-$DOSSIER-test-final-holm-quatre-v3.json` et `.md` (pour M sans course S saine : `-holm-deux-`). Ni `--objet`, ni
`--carte`, ni `--zones` (protocole, § 3). Les deux fichiers `test_final` sont hachés et copiés octet par octet, jamais
ouverts.

**2.3 G4, arbre de l'organisme corrigé (conv-audit, après la pièce de correction, avant la commission).**

```
python3 -I "$GARDES/garde_g4_arbre_organisme_v1.py" \
  --arbre "$SORTIE_CORRECTEUR/copie-organisme" --origine "$SORTIE_CORRECTEUR/objet-origine" --arbre-origine "$ARBRE" \
  --marqueurs "$MARQUEURS" --empreinte-marqueurs "$EMPREINTE_MARQUEURS" \
  --piece-lecture "$A_TEST_JSON_M" --piece-lecture "$A_TEST_MD_M" --piece-lecture "$RELEVE_M" \
  --piece-lecture "$A_TEST_JSON_S" --piece-lecture "$A_TEST_MD_S" --piece-lecture "$RELEVE_S"
```

`--marqueurs` : la liste empreintée des marqueurs des dossiers d'audit de la ronde (facultatif s'il n'y en a pas) ;
`--piece-lecture` : (A-test) et (B) lus pendant la ronde (jamais un fichier `test_final`). La sortie standard donne
l'empreinte d'arbre de l'arbre inspecté, que le lanceur dérivé épingle.

**2.4 G5, périmètre, facteurs, zones (conv-audit, après la pièce de correction, avant la commission).**

```
python3 -I "$GARDES/garde_g5_perimetre_v1.py" \
  --diff "$SORTIE_CORRECTEUR/correction-$DOSSIER-ronde-$K-v1.diff" \
  --perimetre "$SORTIE_CORRECTEUR/perimetre-$DOSSIER-ronde-$K-v1.md" --empreinte-perimetre "$EMPREINTE_PERIMETRE" \
  --carte "$CARTE_JSON" --empreinte-carte 2aaedd08a719e93d2e18437377e9cc565dc4de230ef1af97b0a6e6ef807cec25 \
  --zones "$ZONES_JSON" --empreinte-zones 0082519cc0ef2400c198c89a8504f52948e7abb9b7e35e113db9ba1319f0b342 \
  --objet "$SORTIE_CORRECTEUR/objet-origine" --copie "$SORTIE_CORRECTEUR/copie-organisme"
```

`EMPREINTE_PERIMETRE` : l'empreinte de la pièce de périmètre consignée par conv-audit avant le diff. Pour une autre version
de la carte de même forme, ses chemins et empreintes.

**2.5 G6, les deux courses (conv-audit, sur chaque pièce rendue).** Pièce de la course S :

```
python3 -I "$GARDES/garde_g6_courses_v1.py" --piece "$PIECE" \
  --autre pilote4-gemini-v6-2-v1 --autre pilote4-gemini-v6-2-v1-tentative2 --autre gemini-organisme-v6-2 --autre v6-2
```

ajouter `--autoriser-preseance` pour la seule pièce de correction motivée par S. Pièce de la course M :
`--autre pilote4-gemini-v6-2-s-v1 --autre gemini-organisme-v6-2-s --autre v6-2-s`.

**2.6 G8, valeurs recopiées (conv-audit, sur chaque pièce rendue).**

```
python3 -I "$GARDES/garde_g8_valeurs_v1.py" --valeurs "$LISTE" --empreinte-valeurs "$EMPREINTE_LISTE" \
  --piece "$PIECE_1" [--piece "$PIECE_2" …]
```

**2.7 G9, entrée de lancement (conv-audit, avant chaque relance).**

```
python3 -I "$GARDES/garde_g9_entree_lancement_v1.py" --journal "$JOURNAL" --numero "$N"
python3 -I "$GARDES/garde_g9_entree_lancement_v1.py" --entree "$ENTREE"
```

**2.8 Essais.** Depuis le dossier qui contient `fournis/`, `fournis-v2/` et `travail/` (par défaut, le parent du dossier
des scripts) ; un journal nouveau à chaque exécution (le banc refuse d'en écraser un) :

```
python3 -I "$GARDES/essais_gardes_v1.py" --journal "$GARDES/journal-essais-gardes-v<N>.log" [--racine "$RACINE"]
```

## 3. Formes que les gardes lisent

**3.1 Pièce de périmètre (G5).** G5 lit ces lignes « clé : valeur » (puce, gras et code permis ; casse et accents
indifférents) ; le reste de la pièce (nom du défaut, raison, ce qui change) est pour le contre-lecteur :
- `facteur : F05 — <nom>` : une seule ligne, qui ne nomme qu'un facteur, de la carte ;
- `élément : F04-b` (F04 seulement, un seul) ; `instance : F07-a` (F07 seulement) ;
- `exception : défaut du chemin des réponses — délai` (F09 seulement ; format, analyse ou délai) ;
- `lieu : <fichier>, <fonction>, l. <plages>` : une ou plusieurs lignes ; plages au commit, par exemple « l. 988–996,
  998 » ; le texte entre parenthèses n'est pas lu (colonnes, entrées de la carte, remarques) ; plusieurs fichiers séparés
  par « ; » ;
- `accompagnement : manifeste.json ; principal.py, l. 27 (VERSION) ; CORRECTIONS-v<N>.md ; tests/test_corrections_v<N>.py`
  (facultatif ; pour `principal.py`, la ligne `VERSION` seulement) ;
- `essai hérité adapté : tests/<fichier>.py — raison : …` (une ligne par essai hérité changé).

**3.2 Fichier d'ouverture (G2, forme).** Non vide ; une ligne qui porte le mot « référence », nomme une ligne (du
registre des décisions) ou un message (du canal) et donne l'empreinte complète, 64 caractères, du registre ou du
message ; une heure UTC lue sur `date -u` (forme `AAAA-MM-JJTHH:MM:SSZ` ou `AAAA-MM-JJ à HH:MM:SS UTC`) ; un compagnon.
La référence elle-même (la ligne existe et dit ce qu'on lui fait dire) est contrôlée par conv-audit.

**3.3 Entrée de lancement (G9).** Un titre `### Entrée <N> — lancement … — <heure lue sur date -u>` ; une ligne
`- attente chiffrée : <élément> ; <élément>` (ou ses éléments en sous-puces), chaque élément de la forme
`HC-P4-03 : <observation mécanique>, nombre attendu ≥ 1` (fiche visée, observation, comparateur et entier ; un décimal
seulement avec son unité, USD, s ou octets) ; une ligne `- test_final : « aucune attente au-delà des nulles HC-P4-11 et
12 »`.

**3.4 Liste des valeurs (G8) et des marqueurs (G4).** Une valeur par ligne (le premier mot ; le reste de la ligne est un
libellé, jamais affiché) ; lignes vides et lignes commençant par `#` ignorées ; un compagnon ; son empreinte donnée en
argument. Une valeur textuelle a au moins quatre caractères.

**3.5 Relevé (G1).** Lignes `clé = valeur` (lignes vides et lignes commençant par `#` ignorées, toute autre ligne
refusée, une clé en double refusée). Champs lus : `releve.dossier`, `sources.liste_fermee` (l'empreinte de
`EMPREINTES-pilote-v1.txt` du dossier de course), `sources.liste_fermee_verifiee`, `fin.liste_fermee_poussee`,
`fin.recherche_cles_faite`, `fin.reprise_attendue`, `identite.commit`, `identite.arbre`.

**3.6 Noms gelés (G5 ; carte v2 annoncée).** Champ `noms_geles`, au premier niveau du JSON de la carte ou de celui des
zones : une liste non vide ; chaque entrée est un identifiant, ou un objet `{"nom": "<identifiant>", "fichier": "<fichier
de l'objet>", …}` ; chaque nom doit paraître dans le code de l'objet. Tout bloc, dans tout fichier Python que touche le
diff, qui lie, délie ou masque un de ces noms est refusé, par analyse syntaxique du fichier nouveau (lignes ajoutées ou
changées) comparé à l'ancien (lignes retirées) : affectation simple, augmentée ou annotée, `:=`, `for`, `with`,
`except … as`, compréhension, capture de `match`, `del`, `global`, `nonlocal`, `def`, `class`, paramètre (et sa valeur
par défaut), `import` (et `import *`), `setattr` et `delattr` à nom constant, écriture à nom constant dans `globals()`,
`vars()`, `locals()` ou `__dict__`. Un champ de premier niveau inconnu fait refuser la carte.

## 4. Qui exécute quoi (protocole v4, fin du § 11)

| garde | qui | quand | comment |
|---|---|---|---|
| G1, G2 | conv-audit ; chaque agent à son départ | avant l'assemblage ; au départ de l'agent | `assembler_dossier_lecture_v1.py` ; l'agent, par les vérifications de son brief (partie commune), sans script |
| G8 bis (b), G12 | conv-audit ; chaque agent à son départ | à l'assemblage ; au départ de l'agent | `assembler_dossier_lecture_v1.py` ; l'agent, par son brief |
| G4, G5 | conv-audit | après la pièce de correction, avant la commission | `garde_g4_arbre_organisme_v1.py`, `garde_g5_perimetre_v1.py` |
| G6, G8 | conv-audit ; le contre-lecteur | sur chaque pièce rendue | `garde_g6_courses_v1.py`, `garde_g8_valeurs_v1.py` ; le contre-lecteur par lecture (brief, section 3B) |
| G9 | conv-audit | avant chaque relance | `garde_g9_entree_lancement_v1.py` |
| G8 bis (a) | session-depot | sur données synthétiques, sans affichage | essai « séparation » du script de lecture v3 (hors de cette tâche) |
| G3, G7, G10, G11 | — | — | hors de cette tâche (essais d'agents ; essais du relevé) |
| essais | qui change une garde | à chaque version nouvelle | `essais_gardes_v1.py`, journal nouveau |

## 5. Ce que chaque garde ne couvre pas

**Assemblage (G1, G2, G8 bis (b), G12).** La référence citée par l'ouverture et la décision elle-même (conv-audit). Au
§ 9, seuls le dossier, le commit du segment 1 et l'arbre sont comparés ; nom de course, lignée, graine, question,
lanceur : l'analyste. G8 bis (b) cherche des motifs (le mot `test_final`, une ligne (iii) et ses marques, « McNemar »,
« Holm », une valeur p, la mention d'essai) dans le seul fichier `test` : une valeur écrite sans mot-clé n'est pas
reconnue ; la séparation des courses dans les fichiers « holm-quatre » relève de l'essai « séparation » (G8 bis (a)) et de
l'étape 1 de l'analyste final (E3) : l'assemblage n'ouvre aucun fichier `test_final`. G12 juge les noms seulement. La
liste fermée est close : un fichier du dossier de course absent de `EMPREINTES-pilote-v1.txt` fait refuser. Un arrêt du
processus laisse un dossier `.<sortie>.en-cours-<pid>` à effacer, jamais le dossier final ; entre le dernier contrôle
d'absence et le renommage, un dossier vide créé au même nom par un autre processus serait remplacé. Les fichiers
assemblés sont en lecture seule ; les dossiers ne le sont pas.

**G4.** Les fichiers textes UTF-8 seulement (un fichier binaire est refusé, jamais inspecté). Le contenu du § 14 se
cherche par motifs dans les lignes ajoutées par rapport à l'origine ; un critère ou une consigne de classement sans forme
reconnaissable : contre-lecteur. « Aucun score » : seulement les valeurs données (marqueurs, nombres de (A-test) et de
(B)) ; chaînes de (A) et (B) d'au moins 16 caractères ; nombres d'au moins trois chiffres significatifs, ou entiers d'au
moins quatre chiffres ; marqueurs à la valeur exacte, sous toutes leurs écritures, jamais arrondis (G8 cherche les
arrondis dans les pièces). Ni le périmètre, ni la liste d'accompagnement (G5).

**G5.** La forme du § 3.1 ; les fonctions déclarées ne sont pas vérifiées. F04 : l'élément se contrôle ligne par ligne ;
à l'intérieur des l. 1011 et 1039, que la carte partage entre éléments, le contre-lecteur. F01, l. 2106 : qu'un
changement n'y porte que sur une condition de ronde (carte, D8), le contre-lecteur. Des caractères insérés au bord d'un
segment de facteur comptent dans ce segment ; au bord d'un segment gelé ou d'un point hors boucle, ils sont refusés.
Un bloc qui retire et ajoute des nombres de lignes inégaux est apparié par le début puis par la fin ; s'il ne se range
d'aucune façon, il est refusé, même s'il était permis. Contenu interdit (e) : motifs du § 14 et listes d'au moins quatre
mots (ou alternances) ; une règle, un seuil, un exemple ou une consigne sans ces formes : contre-lecteur. Noms gelés :
les constructions du § 3.6 ; non couverts : `exec` ou `eval` d'un texte calculé, `setattr` ou écriture dans un espace de
noms à nom calculé, réaffectation par un module importé. La règle d'insertion resserrée annoncée pour la carte v2 n'est
pas écrite ici. G5 n'exécute pas les essais de la correction.

**G6.** Les noms donnés en arguments, en mots entiers (protocole v4 : ni lettre, ni chiffre, ni `-`, ni `_` de part et
d'autre) : un nom collé dans un nom de fichier (`lecture-<dossier>-test-v3.md`) n'est pas compté (essai « limite
documentée ») ; un rapprochement des courses sans leurs noms (« l'autre course ») ; une fiche ou un verdict de l'autre
course hors de ses noms : contre-lecteur. Sur la ligne « condition de préséance » : une fiche (`HC-P4-…`) et une liste
close de mots de verdict.

**G8.** Les valeurs de la liste seulement. Une valeur écrite en lettres, ou collée à un identifiant (`HC-P4-11`, `g003`,
`v3`), n'est pas lue. Les arrondis comptent si le nombre écrit a au moins deux chiffres significatifs. Un nombre court
(entier de moins de trois chiffres, décimal d'un seul chiffre significatif) est refusé avec la mention « peu
distinctive » : souvent une coïncidence, à trancher par lecture.

**G9.** La forme du § 3.3 ; les autres champs de l'entrée de lancement (identité de l'objet, noyau, banque, texte,
graine, devis, question servie) ne sont pas contrôlés, ni la justesse de l'attente (le bon champ du relevé, le bon
nombre). Fiches motivantes par défaut : 01, 03, 07, 08, 09 (brief des agents v4, section 2) ; option
`--fiches-motivantes` si le registre change.

## 6. Table « garde du § 11 → script → essais »

Chaque cas tourne sous Python 3.11.17, 3.12.3 et 3.13.17 : 172 cas, 516 essais consignés au journal,
516 conformes.

| garde du § 11 | script | cas sains | artefacts (refusés) |
|---|---|---|---|
| G1 — lecture pendant une course | `assembler_dossier_lecture_v1.py` | course simulée v14 (liste fermée vérifiée, fichiers hachés) ; course synthétique ; lecture finale holm-quatre et holm-deux | 10 : arrêt par `STOP` entre deux segments (`fin.reprise_attendue = oui`), en fin de course et en lecture finale ; liste fermée absente ; ligne falsifiée ; fichier hors de la liste ; lien symbolique ; recherche des clés non consignée ; liste non poussée ; champ de fin absent ; autre liste citée par le relevé |
| (identité, § 9 : ajout déclaré) | `assembler_dossier_lecture_v1.py` | commit abrégé à sept caractères | 3 : relevé d'un autre dossier ; autre commit ; autre arbre |
| G2 — lecture sous la retenue | `assembler_dossier_lecture_v1.py` | les cinq assemblages sains | 7 : ouverture absente ; vide ; sans référence ; empreinte tronquée ; sans heure ; d'une autre course ; ouverture de fin de course donnée en lecture finale |
| G3 | hors de cette tâche | — | — |
| G4 — arbre de l'organisme corrigé | `garde_g4_arbre_organisme_v1.py` | 2 : arbre corrigé du cas sain de G5 (avec marqueurs et pièces (A-test), (B)) ; arbre d'origine | 17 : `test_final` synthétique (nom ; contenu) ; marqueur (exact ; en pourcentage) ; copie d'une pièce de lecture ; chaîne de (B) ; ligne de (A-test) ; `CORRECTIONS-v6.md` qui cite une fiche, un fait de course, un libellé du point 4 bis ; `__pycache__` ; binaire ; lien ; origine autre ; marqueur mal choisi ; liste autre ; pièce `test_final` donnée (jamais ouverte) |
| G5 — périmètre, facteurs, zones | `garde_g5_perimetre_v1.py` | 22 : F02 et la liste d'accompagnement ; `VERSION` jointe à F03 ; chaque segment des lignes partagées 997, 2103, 2104 (F12, F05, F03 ×2, F10, F01) ; sur chaque ligne à segment gelé (Z03 l. 1009, 1011, 1039 ; PHB-1 à PHB-4) un autre segment de la ligne ; F09 sous l'exception « délai » ; F09 dans son domaine ; ligne insérée (règle 9) ; essai hérité déclaré ; carte de même forme (v1-bis) ; deux cas sains sous noms gelés | 54 : (a) 3 ; (b) 5 ; (c) 7, dont les trois segments gelés ; (d) 3 ; (e) 3, contenu interdit planté ; (f) 2 ; (g) 3 ; (h) 4 ; (i) 3 ; hors du périmètre déclaré 1 ; noms gelés 11 ; forme et intégrité 9 (bloc décalé, périmètre autre que l'empreinté, copie hors du diff, `nom` du manifeste, essai hérité non déclaré, binaire, diff vide, carte incohérente, champ inconnu) |
| G6 — mise en regard des deux courses | `garde_g6_courses_v1.py` | 3 : pièce de S qui porte `gemini-organisme-v6-2-s` et `v6-2-s` ; correction de S avec la ligne « condition de préséance » ; pièce de M ; plus 1 limite documentée | 9 : lignée, nom de course, clé de M dans une pièce de S ; dossier de S dans une pièce de M ; « M − S » ; préséance avec fiche ; avec verdict ; sans l'option ; deux lignes |
| G7 | hors de cette tâche | — | — |
| G8 — valeur de `test_final` recopiée | `garde_g8_valeurs_v1.py` | 1 : cellules citées par coordonnées et libellés | 8 : score marqueur ; valeur p à virgule ; pourcentage arrondi ; compte (peu distinctif) ; compagnon faux ; liste autre ; liste vide ; pièce `test_final` donnée (jamais ouverte) |
| G8 bis (a) | hors de cette tâche (session-depot) | — | — |
| G8 bis (b) — le seul fichier `test` réel | `assembler_dossier_lecture_v1.py` | les assemblages de fin de course (fichier `test` avec la phrase (iv)) | 5 : mot `test_final` ; ligne (iii) ; valeur p ; mention d'essai ; fichier `test_final` donné en mode course (non ouvert) |
| G9 — entrée de lancement sans attente chiffrée | `garde_g9_entree_lancement_v1.py` | 3 : attentes chiffrées ; en sous-puces avec un montant ; entrée lue dans un journal | 8 : sans nombre ; score ; fiche HC-P4-11 ; décimal sans unité ; fiche non motivante ; `test_final` absent ; pas d'attente ; entrée qui n'est pas de lancement |
| G10, G11 | hors de cette tâche | — | — |
| G12 — sortie de lecture hors du script v3 | `assembler_dossier_lecture_v1.py` | les cinq assemblages sains (version 3 au manifeste et aux fichiers) | 8 : `-provisoire-` (fin de course, finale) ; version 2 (script ; fichiers finals) ; version 4 contre script 3 ; autre course ; holm-quatre et holm-deux mêlés ; fichiers `test` en lecture finale |
| (intégrité de l'assemblage) | `assembler_dossier_lecture_v1.py` | — | 6 : compagnon absent ; compagnon faux ; objet altéré ; `__pycache__` dans l'objet ; dossier de sortie existant (intact) ; usage |

## 7. Messages reçus, écarts déclarés, réserves

**Messages de conv-audit reçus pendant le travail.** (1) Pièces nouvelles dans `fournis-v2/` (protocole v4, briefs des
agents v4, spécification v3), suivies ; règle 9 du § 0 de la carte adoptée telle qu'elle est écrite, G5 applique les
règles 1 à 9. (2) Trois précisions (constat CLB5-03) : cas sains et artefacts sur chaque ligne à segment gelé ; `VERSION`
(l. 27) jointe à un autre facteur acceptée, sans compter pour un second facteur ; bornes de mot de G6, avec le cas sain
et l'artefact inverse. (3) Noms gelés : lecture d'une liste dans le JSON et contrôle par analyse syntaxique, essayés sur
une liste fabriquée (§ 3.6), en attendant la carte v2.

Je déclare les écarts suivants à mon brief :
1. Versions : protocole v4, briefs des agents v4 et spécification du relevé v3 à la place des versions du brief (message
   1) ; G5 a donc les artefacts (g), (h) et (i) en plus de (a) à (f), et l'exemple de (a) est une ligne de F01 et une de F02.
2. G6 compte les noms selon la règle des mots entiers du protocole v4 ; conséquence déclarée : un nom collé dans un nom de
   fichier n'est pas compté (essai « limite documentée »).
3. Ajouts non demandés : contrôles d'identité à l'assemblage (`releve.dossier`, `identite.commit` contre la tête citée,
   `identite.arbre` ; § 9 : « aucun assemblage en cas d'écart ») ; G6 refuse aussi « M − S » écrit ; G5 refuse une carte à
   champ de premier niveau inconnu, vérifie que `copie-organisme/` est exactement l'objet modifié par le diff et lit
   `noms_geles` (message 3) ; G4 rend l'empreinte d'arbre à épingler.
4. Choix de lecture : la lecture finale ne reçoit ni `objet/`, ni la carte, ni les zones (protocole, § 3) ; tout fichier
   copié doit avoir son compagnon, fichier d'ouverture compris ; le relevé est exigé sous le nom `-v1` ; la liste fermée
   est `EMPREINTES-pilote-v1.txt` (spécification, § 2.1), close sur le dossier de course.
5. G4 cherche les marqueurs à la valeur exacte et G8 aussi à leurs arrondis : la première exécution de mise au point a
   montré qu'un arrondi à deux chiffres d'un marqueur synthétique coïncide avec des nombres courts des documents de
   l'objet (18 écarts, tous de G4).
6. Mise au point : trois exécutions du banc sur les brouillons, dans `travail/` (effacé), avant celle du journal livré :
   495 conformes sur 513 (écart 5), puis 513 sur 513, puis 516 sur 516 (un cas de G6 ajouté, la phrase (iv) ajoutée au
   fichier `test` synthétique). Les brouillons ont été modifiés dans `travail/` pendant la mise au point ; aucune pièce de
   `sortie/` n'a été réécrite ; le journal livré consigne l'exécution des scripts tels qu'ils sont livrés (empreintes en
   tête du journal).
7. Contenu interdit de l'artefact (e) de G5 : une liste de mots inventés, tirés à l'exécution, et deux variantes (un nom
   de fiche, un identifiant de la forme t-0001), écrits dans `travail/` seulement et effacés avec lui ; le journal dit
   « contenu interdit planté : refusé ». Les marqueurs et les décimaux de forme score des artefacts sont tirés à
   l'exécution, jamais écrits dans le banc ni dans le journal ; quelques nombres illustratifs restent dans le banc (graine
   et coût d'une entrée synthétique, nombre de fichiers 26).

**Réserves et points pour conv-audit.**
1. La forme de la pièce de périmètre que lit G5 (§ 3.1) n'est pas dans les briefs des agents v4 : à donner au correcteur
   (version nouvelle de son brief) ; sans elle, G5 refuse une pièce qu'il ne sait pas lire.
2. G6 et les noms collés (écart 2) : décider s'il faut une recherche de plus ; d'ici là, le contre-lecteur.
3. G1 : confirmer avec l'auteur du script du relevé que `sources.liste_fermee` est l'empreinte de
   `EMPREINTES-pilote-v1.txt`, et que le dossier de course poussé ne porte aucun fichier hors de sa liste fermée.
4. G8 bis (b) : avant la première lecture réelle, assembler un dossier sur un fichier `test` produit par le script v3 sur
   données synthétiques (mention d'essai retirée par la forge), pour écarter un faux refus par motif.
5. Noms gelés : le nom du champ et la forme des entrées sont des choix de cette pièce ; une carte v2 qui les nommerait
   autrement serait refusée (champ inconnu) ; une G5 v2 suivra la carte v2 et sa règle d'insertion resserrée.
6. La carte et les zones v1 restent sous réserve de leur contre-lecture ; G5 en vérifie la cohérence interne et
   l'accord avec l'objet (empreintes des fichiers et des segments), pas la justesse.
