# Extrait de la procédure v14 du poste local (sections 7 et 8 entières), copie pour la relecture par Fable ; le reste de la procédure n'est pas servi

## 7. Réserves

- **Trois essais ont tourné** sous les procédures v9 à v11 (serveurs 175751342, 175838427, 177067030) ; la minuterie, la mère
  et la destruction ont fait ce qui était écrit. Le code v8 n'a tourné que hors machine.
- **Éprouvé sur la machine au troisième essai** : pas noyau (18 sur 18), 21 gardes Lean, isolement Python, limites de mémoire
  (Python), de tâches et de durée ; limite de temps de processeur effective (tué à 5,011 s). Compilation d'un item avec Mathlib :
  4,3 à 4,8 s de processeur.
- **Non éprouvé sur une machine, à jouer au quatrième essai** : le classement v8 (« délai » par le temps de l'unité, marge de
  0,05 s) ; le chemin du cgroupe des unités et de la tranche réservée sous Ubuntu 24.04 et systemd 255 (création implicite de
  la tranche par `--slice=`) ; le pic échantillonné ; le classement « mémoire » d'un processus Lean par `oom-kill` ; les issues
  des sondes v3 sous bwrap et l'utilisateur `bac` ; la mesure de la mémoire de la machine entière.
- **Vérificateur v6** : hors machine, environ 8 s et 2,1 Gio de mémoire anonyme par passage, plus 6,9 Gio de pages des fichiers
  `.olean` (récupérables), contre 0,4 Gio de mémoire anonyme pour la compilation d'un item ; sous la borne du bac (6 Gio).
- **La minuterie locale meurt avec l'ordinateur** (extinction, déconnexion). Les garde-fous de fond sont T1 à T3, la ligne
  d'état lue par la routine de reprise, et le rappel de le directeur.
- **Coût au pire**, garde-fous locaux morts :
  - jusqu'à `H` (47 heures après la préparation au plus) si T1 agit ; `H + 30 min` si seule T2 agit ; `H + 24 h` si seule T3
    agit, soit 71 heures, environ 30 USD pour `ccx33` (extrapolation de la contre-lecture, non vérifiée ici) ;
  - au-delà, seuls le rappel de le directeur et la routine de reprise restent.
- **Le bac à sable et le mandataire du poste ne sont pas éprouvés ici.** L'essai à blanc du point 4 de la section 0 en décide.
- **`garde-poste`** :
  - il ne lit que ce qu'on lui donne (l'index git, ou des fichiers nommés) ;
  - il ne connaît ni le nom de la machine ni celui de l'utilisateur, seulement l'adresse, le dossier personnel et le chemin
    du clone. Le reste tient à la discipline de la consigne.
- **Critères de la section 8** : écrits par le développeur sur les propositions du contre-lecteur ; à vérifier par lui avant
  toute consigne (R-3735).
- **Quatrième essai** (v12, serveur 177109613) : éprouvés sur la machine, le classement v8 du « délai » (5,012 s), le chemin
  du cgroupe des unités et de la tranche réservée, le pic échantillonné, « mémoire » d'un processus Lean par `oom-kill`, les
  sondes v3 sous bwrap, la mesure de la mémoire de la machine entière (passage en parallèle compté). Seul en échec : le cas
  137, par l'artefact (changement 1).
- **Non éprouvé sur une machine, à jouer au cinquième essai** : l'artefact v2 sous `/opt/pybac/bin/python` (3.12.3 au
  quatrième essai) et l'extrait de la sortie standard du genre « limites ». La règle 8.7 ne tourne que sur le poste.
- **Règle 8.7** : écrite par Opus 5.5 ; à faire relire par Fable 5.2 (R-3735, R-4717) avant tout usage décisif.
- **Points à faire relire par Fable 5.2 (critères de décision ; R-3735, R-4717)**, sans les trancher ici :
  1. le **§ 8.2, cas « sortie de lui-même en code 137 »** : les quatre conditions (code 137, aucun incident, temps de
     processeur de l'ordre de quelques dizaines de millisecondes, « SORTIE 137 » sur la sortie standard), toutes exigées ;
  2. le **§ 8.7 en entier**, v2 comprise : l'épreuve « tenue » seulement entière (B1), la contradiction du pilote « apres »
     en code 0 avec un pas `noyau` non conforme lue « non établi » et non « non conforme » (H8), `parallele_3_compte` vrai
     avec un passage refusé (H12), les noms et passages des 18 cas du noyau, un cas à `ok` vrai avec des écarts, l'erreur
     inattendue en code 3, et l'étape de concordance (point 6) ;
  3. **les codes 124 ou 255 du pilote « avant »** : la règle lit tout code non nul du pilote « avant » « non tenu », donc
     l'outillage « non conforme », alors qu'une borne de temps (124) ou une connexion tombée (255) ne dit rien de
     l'outillage, et qu'à l'épreuve ces mêmes codes sont lus « non établi ». **Point noté, non tranché** : la v14 garde la
     lecture de la v13.
- **Mutations de la règle v2** (journal v2) : deux mutations survivent, retirer seul le contrôle du code de l'épreuve ou
  seul celui du statut dans B1. Elles sont équivalentes sur les pièces que la règle accepte : un code autre que 0 avec un
  statut « conforme » est déjà « non établi » par la contradiction du code et du statut, un statut autre que « conforme »
  avec le code 0 aussi, et le code 1 avec le statut « non conforme » est pris par le contrôle du code. Gardés par prudence,
  comme B1 les nomme.

## 8. Lecture des sorties du cinquième essai (écrite avant l'essai)

Rien de cette section ne se change après avoir vu une sortie. Une sortie qui ne rentre dans aucune lecture écrite ici est
rapportée telle quelle à la mère, sans lecture inventée.

### 8.1 Ordre de lecture

1. **Pilote « avant »** : code 0, essais R5 de la phase « avant » conformes (inchangés depuis la v10). Sinon : ni coupure, ni
   pilote « apres » ; section 5.
2. **`premier-pas-noyau-v6.json`** : `conforme` vrai, 18 cas (9 cas, avec et sans G-L3+). Non conforme : le pilote s'arrête
   (`set -e`) ; rien d'autre n'est lu.
3. **`epreuve-code-v6.txt`** : 0 conforme, 1 non conforme, 3 épreuve morte, 124 borne de temps atteinte.
4. **`epreuve-isolement-v6.json`**, dans cet ordre :
   1. `statut` (« conforme », « non conforme » ou « épreuve morte ») ;
   2. `genres` et `genres_morts`. **Un genre « épreuve morte » arrête la lecture de ce genre** : ses autres cas ne disent
      rien, ni pour ni contre ; on lit seulement la sortie de son cas sain (`sortie_compilation_extrait` ou sortie standard)
      pour en dire la cause ;
   3. les cas, genre par genre : gardes Lean (21), isolement Lean (5), Python (4), limites (5), limites Lean (1) ;
   4. `controles_hote` (vide attendu) ;
   5. le bloc `memoire` (point 6).
5. **`mesures-v6.json`** : `suite` (3 passages), `parallele_3` (3 passages), `memoire`, `releve_machine`, puis
   `parallele_3_compte` et `parallele_3_motifs` (point 7).
6. **Sondes réseau** (après coupure et de fin) : « fermée », aucun écart.

### 8.2 Lectures cas par cas de l'épreuve

- **Isolement Lean (sondes v3)** : chacun des cinq cas porte `sonde_muette` faux, `code_compilation` 0 et son extrait de
  sortie ; chaque tentative a l'issue attendue ; le cas sain rend `ecriture-tmp` et `ecriture-item` « REUSSI ».
- **Détail des trois tentatives réseau** (`reseau-curl-ip`, `reseau-python-tcp`, `reseau-dns`), lu dans l'extrait de sortie,
  même quand le cas est conforme : il doit dire un refus du réseau (connexion impossible, délai, résolution impossible). Un
  détail qui dit que le programme n'a pas été lancé (« could not execute external process », déjà refusé par l'épreuve ; ou
  « No such file », code 127, que l'épreuve ne refuse pas) : la tentative ne prouve rien ; le cas est lu « non éprouvé »,
  jamais « conforme », et le dit au compte rendu. L'item ne garde que les 160 premiers caractères de la sortie d'erreur ;
  pour Python, c'est le début de la trace : si la raison n'y est pas, le dire.
- **« sortie de lui-même en code 137, sans consommer la limite (5 s) »** : code 137, aucun incident, temps de processeur de
  l'unité de l'ordre de quelques dizaines de millisecondes, **et « SORTIE 137 » sur la sortie standard** (v13 : attente de
  l'épreuve depuis les attendus v6, désormais écrite ici ; `stdout_extrait` la montre). Les quatre conditions sont exigées ;
  une seule manquée : cas non conforme, cause rapportée telle quelle (l'extrait est dans la pièce).
- **« temps de processus (5 s) »** : incident « délai » (point 3 pour la marge).
- **« mémoire (512M) »** (Python) : incident « mémoire » ; **« durée murale (10 s) »** : « délai » ; **« tâches (32) »** :
  « REFUS » sans « LANCES ».
- **Limites Lean, « mémoire d'un processus Lean (512M) »** : **lu sur la compilation seule** : `temps.resultat` vaut
  `oom-kill` (résultat systemd de la compilation), `incident_compilation` vaut « mémoire », `code_compilation` est non nul, et
  l'extrait de sortie ne porte pas « ALLOUE ». `incident_noyau` (le vérificateur, qui suit sous les mêmes limites) et
  `incident_bac` sont relevés sans compter. Une compilation en échec d'elle-même (`exit-code`) est un écart, même si le
  vérificateur est tué par la mémoire.

### 8.3 « Délai » : définition et marge

Les trois phrases de la contre-lecture (§ 3.1), reprises telles quelles :
1. « Délai » veut dire : l'unité n'a pas réussi et a consommé, tous processus confondus, au moins la limite de temps de
   processeur ; ou systemd a rendu `timeout`. Cela ne veut pas dire qu'un processus a été tué par la limite.
2. Une réussite n'est jamais un incident, même au-delà de la limite. Un item à plusieurs processus peut consommer plus que la
   limite au total : la borne de l'unité est la durée murale.
3. « Délai » ne doit jamais valoir mieux qu'un échec dans ce qui lit le bac (ni rejeu, ni retrait du dénominateur). Sinon un
   item à plusieurs processus pourrait l'acheter.

**Décision sur la marge (recommandation R1), prise avant l'essai : une tolérance fixe.** La phrase 1 s'entend « au moins la
limite moins 0,05 s » : l'exécuteur v8 classe « délai » dès que le temps de processeur de l'unité atteint `cpu_max_s - 0,05`
(`TOLERANCE_CPU_S`). Motif : le noyau tue sur un compte par battements d'horloge, systemd rapporte le temps exact du cgroupe ;
au troisième essai, l'écart était de 11 ms au-dessus de la limite, sur une seule mesure. La tolérance ne donne rien à un item :
il doit brûler la limite à 0,05 s près, et la phrase 3 tient. Essais : 4,95 s « délai », 4,949 s rien, 5,011 s « délai »,
sortie en 137 après 31 ms rien.

**Lecture écrite d'avance du cas « temps de processus (5 s) »** :
- « délai », temps de l'unité au moins 4,95 s : conforme ;
- aucun incident, fin en 137 ou par un signal, temps entre 4,90 et 4,95 s : « tolérance trop étroite » ; non conforme ; cause
  identifiée ; aucun reclassement à la main ; correction en version neuve, contre-lue, avant un essai suivant ;
- aucun incident avec un temps sous 4,90 s, ou toute autre combinaison : non conforme, cause à établir ; rien n'est conclu sur
  la limite.

### 8.4 Mémoire : signal d'un chemin de cgroupe faux

- Une unité qui a tourné au moins 1 s (`duree_service_s`) avec `memoire_echantillons` à zéro dit que le chemin du cgroupe
  (`/sys/fs/cgroup/<tranche>/<unité>.service/memory.peak`) est faux sur cette machine : le bloc `memoire` porte alors
  `chemin_cgroupe_faux` vrai et la liste des unités ; **aucun pic n'est rapporté**, ni par unité ni pour la tranche, et le
  passage en parallèle n'est pas compté. Le dire au compte rendu.
- Sinon, un pic par unité n'est rapporté que s'il porte au moins trois relevés (`pics_rapportes_octets`) ; c'est un minorant
  (seul est perdu ce qui monte pendant la dernière période de 0,1 s).
- **Aucun « conforme » ne dépend du pic** : ni le pas noyau, ni l'épreuve. Ordre de grandeur attendu (troisième essai et hors
  machine) : quelques dizaines de Mio pour une compilation sans Mathlib, de l'ordre de 2 Gio pour le vérificateur ; des
  valeurs de quelques centaines de Kio pour un processus Lean avec Mathlib diraient que la mesure est encore fausse.

### 8.5 Mémoire de la machine entière, trois passages en parallèle

`mesurer` lance trois passages de l'item sain en suite (tranche `system.slice`), puis trois en parallèle dans une **tranche
réservée de nom neuf**, `bacmesure<8 hexadécimaux>.slice` (créée par systemd au premier lancement, cgroupe
`/sys/fs/cgroup/bacmesure….slice`), où ne tourne rien d'autre. Pendant le bloc parallèle, toutes les 0,1 s, root relève
`memory.peak` de la tranche (le plus-haut de la mémoire simultanée des trois passages, tenu par le noyau ; seul est perdu ce
qui monte pendant la dernière période) et `MemAvailable` de `/proc/meminfo` ; `MemTotal` et `MemAvailable` sont lus aussi
avant et après. Le pic de la tranche compte aussi les pages de fichiers que les passages y chargent (fichiers `.olean` de
Mathlib s'ils ne sont plus en mémoire : récupérables) ; le critère 5 est donc prudent, et le critère 7 prend le plus grand
des deux comptes.

**Critères écrits d'avance** (épreuve v8, `juger_parallele` ; `parallele_3_compte` vrai seulement si tous tiennent) :
1. les trois passages parallèles acceptent l'item sain, sans incident (ni « mémoire », ni « délai ») ;
2. pas de chemin de cgroupe faux (point précédent) ;
3. au moins trois relevés de la tranche ; sinon « mesure de la tranche absente » ;
4. au moins trois relevés de `MemAvailable`, `MemTotal` et `MemAvailable` lus avant ;
5. pic de la tranche au plus la moitié de `MemTotal` (16 428 718 080 octets pour une machine de 32 857 436 160 octets, celle
   du troisième essai) ;
6. recoupement : la baisse de `MemAvailable` (avant moins plus bas relevé) au plus le pic de la tranche plus 1 Gio ; sinon la
   tranche ne compte pas ce que la machine a perdu, et la mesure n'est pas retenue ;
7. mémoire disponible au plus bas, estimée prudemment (avant moins le plus grand de la baisse et du pic), au moins le quart
   de `MemTotal` (8 214 359 040 octets pour la même machine).

**Lecture** : critères tenus : la mémoire de la machine entière pour trois passages en parallèle est mesurée, et **le passage
en parallèle est compté** (le bac peut lancer trois items à la fois, à l'empreinte mesurée). Un seul critère manqué : **aucun
passage en parallèle n'est compté** ; les items tournent un à la fois dans les usages suivants ; les motifs sont rapportés
tels quels, sans correction après coup. La tranche réservée reste chargée sur la machine après la mesure ; la machine est
détruite ensuite.

### 8.6 Ce que le poste écrit au rapport

- Le verdict du poste reste une lecture, jamais un verdict de porte : « noyau », « épreuve » (statut et genres),
  « mesures » (parallèle compté ou non, et pourquoi), et la liste de ce qui reste non éprouvé.
- La lecture combinée de la section 8.7 (`lecture-combinee-<jeton12>-v1.json`, code de sortie compris), recopiée telle
  quelle, et sa concordance avec les lectures 8.1 à 8.5 du poste (§ 8.7, point 6 : fichier des lectures du poste, son
  empreinte, table d'accord).
- L'outillage D-1a n'est déclaré conforme par personne d'autre que la mère, sur ces lectures.

### 8.7 Règle de combinaison : une lecture de l'outillage (v13, v2 du code en v14, écrite avant le cinquième essai)

Nœud 2 de la lecture de conformité du quatrième essai : la v12 n'écrivait aucune règle qui combine noyau, épreuve et
mesures. La voici, écrite avant l'essai, appliquée par `conformite_outillage_v2` aux sorties copiées sur le poste, **après la
section 5** (destruction faite ; aucune commande sur la machine). Rien de cette règle ne se change après avoir vu une sortie.

```
env -u <clés de modèle> PYTHONPATH=src python3 -B -m controle_ia.lean_essai.conformite_outillage_v2 \
    --sorties <dossier de sorties hors du clone> --pilote-avant-code <fichier du code du pilote « avant »> \
    --pilote-apres-code <fichier du code du pilote « apres »> > <dossier hors du clone>/lecture-combinee-<jeton12>-v1.json ; \
    echo $? > <dossier hors du clone>/lecture-combinee-code-<jeton12>-v1.txt
```

Le code de sortie est gardé, l'entier seul (0 « conforme », 1 « non conforme », 3 « non établi », y compris toute erreur
inattendue du code, dont le JSON ne porte alors que le type de l'erreur, champ `erreur` ; 2 usage, sans JSON) ; il doit
répondre au champ `outillage` du JSON (sinon : désaccord, point 6). Les deux fichiers passent
`MV7 garde-poste --ip-poste IP_POSTE --fichier …` avant d'être versés sous `pieces-poste-local-d1a-<jeton12>-v1/`.

1. **Cinq lectures** : pilotes (codes des deux pilotes) ; noyau (`premier-pas-noyau-v6.json` et le vérificateur épinglé) ;
   épreuve (`epreuve-code-v6.txt`, `epreuve-isolement-v6.json`) ; sondes réseau (après la coupure et de fin) ; mesures
   (`mesures-v6.json`).
2. **Chaque lecture sort « tenu », « non tenu » ou « non établi »** :
   - **non tenu** : une lecture écrite d'avance dit non conforme — pilote « avant » en code non nul (codes 124 et 255
     compris : point 3 de la liste de la section 7, non tranché) ; pas `noyau` à `conforme` faux, quand le pilote « apres »
     ne sort pas en code 0 ; un cas de l'épreuve en échec, dans une pièce cohérente (code 1, statut « non conforme »), hors
     d'un genre mort ; un contrôle de l'hôte ; manifestes d'avant et d'après différents ; une sonde réseau avec un écart ;
   - **non établi** : une pièce absente ou illisible ; **une pièce qui n'est pas un objet JSON, un élément de `cas`,
     `suite` ou `parallele_3` qui n'est pas un objet, un champ mal typé (`genres` et `sains` des objets ; `genres_morts`,
     `controles_hote` et `ecarts` des listes ; `ok` un booléen ; un extrait de sortie un texte)** ; une version autre que
     `epreuve_isolement_v9` ; un vérificateur épinglé d'une autre empreinte que `3ef23bfa…` ; deux pièces ou deux champs
     qui se contredisent (code et statut, `conforme` vrai et un cas en échec, **un cas à `ok` vrai avec des écarts, au
     noyau comme à l'épreuve**, `parallele_3_compte` et `parallele_3_motifs`, **`parallele_3_compte` vrai et un passage en
     parallèle refusé ou en incident, un pilote « apres » en code 0 et un pas `noyau` à `conforme` faux**) — une pièce qui
     se dément n'est lue ni pour ni contre ; un nombre de cas ou des noms autres que ceux des attendus v8 (**18 cas du
     noyau, par nom et par passage, avec et sans G-L3+** ; 36 de l'épreuve, par genre) ; **une épreuve qui n'est pas tenue
     entière (code 0, statut « conforme », `conforme` vrai, chaque genre « conforme », chaque cas à `ok` vrai et sans
     écart, chaque témoin sain vrai) sans qu'une lecture écrite dise « non tenu »** ; épreuve morte (code 3 : un genre mort
     ne dit rien, ses autres cas ne comptent pas contre) ; code 124, 255 ou tout code hors de la liste ; une tentative
     réseau dont le programme n'a pas été lancé (§ 8.2 : « non éprouvé ») ; pilote « apres » en code non nul alors que le
     noyau n'est pas non conforme ; un passage en suite de l'item sain refusé ou en incident ; **toute erreur inattendue du
     code (code 3)** ;
   - **tenu** sinon ; « non tenu » l'emporte sur « non établi », qui l'emporte sur « tenu ».
3. **L'outillage** : « non conforme » si une lecture est « non tenu » ; sinon « non établi » si une lecture l'est ; sinon
   « conforme ». Après un pilote « avant » en échec, ou un pas `noyau` non conforme, rien d'autre n'est lu (§ 8.1).
4. **Mesures et usage** : que le passage en parallèle soit compté ou non ne décide pas de la conformité ; il dit l'usage :
   « trois en parallèle » s'il est compté, « un à la fois » sinon (§ 8.5). L'usage n'est rendu que si l'outillage est
   « conforme ».
5. **Aucune tolérance** : ni le poste ni le code ne tolèrent un cas, un écart ou une lecture. « non conforme » et
   « non établi » sont des nœuds pour la mère. Une tolérance passe par un mot de le directeur inscrit par la mère et se déclare
   comme écart au rapport ; l'option (b) du quatrième essai (R-4716) ne vaut que pour lui.
6. **Concordance** : le poste écrit ses lectures 8.1 à 8.5 sans la règle, puis la lecture combinée. Un désaccord entre les
   deux est rapporté tel quel, sans correction ni d'un côté ni de l'autre. **Étape écrite (v14)**, dans cet ordre :
   1. **avant de lancer la règle**, le poste écrit, dans un fichier au nom neuf hors du clone,
      `lectures-poste-<jeton12>-v1.md`, ses lectures 8.1 à 8.5 et, pour chacune des cinq lectures du point 1 (pilotes,
      noyau, épreuve, sondes réseau, mesures), l'issue qu'il en tire lui-même selon les points 2 et 3 (« tenu »,
      « non tenu » ou « non établi », avec ses motifs), puis sa lecture de l'outillage et l'usage ; il en relève l'empreinte
      (`sha256sum`) et ne touche plus au fichier ;
   2. il lance la règle (commande ci-dessus) et garde son code ;
   3. il dresse, au rapport, une table de sept lignes (pilotes, noyau, épreuve, sondes réseau, mesures, outillage, usage) à
      quatre colonnes : la lecture du poste, celle de la règle (champ `issue` de chaque lecture, puis `outillage` et
      `usage`), « accord » ou « désaccord », et les motifs des deux côtés en cas de désaccord ; une huitième ligne dit si le
      code de sortie répond à `outillage` ;
   4. un désaccord est rapporté tel quel : ni le fichier du poste ni le JSON de la règle ne sont repris ; c'est un nœud
      pour la mère ;
   5. le fichier du poste passe `MV7 garde-poste --ip-poste IP_POSTE --fichier …` et se verse avec les pièces, son
      empreinte au rapport.
7. **La règle rend une lecture, jamais un verdict de porte.** La mère déclare (8.6), après qu'un lecteur neuf (R13) a
   rejoué la règle sur les pièces versées et appliqué les sections 8.1 à 8.7.
8. **Essais R5 de la règle** (hors machine) : pièces réelles du quatrième essai telles quelles → « non conforme », sur le
   seul cas 137 ; les mêmes, le seul cas 137 réparé et la version portée à v9 → « conforme » ; puis une pièce cassée à la
   fois, chacune à l'issue attendue. **v2** : de plus H1, H2, H3, H10 et H17 → « non établi » (et la v1, témoin de la faute,
   les lisait « conforme ») ; pièces et éléments qui ne sont pas des objets, genres en liste, mesures valant `[1, 2]` →
   « non établi » ; erreur inattendue → code 3, JSON « non établi » au seul type d'erreur ; noms et passages du noyau, H8
   et H12 → « non établi », avec leurs cas sains (pilote « apres » en code 1 → « non conforme » ; passage refusé non
   compté → « conforme », « un à la fois ») ; mutations de la v2 (journal v2). Sous Python 3.11, 3.12, 3.13 et 3.14.6.
