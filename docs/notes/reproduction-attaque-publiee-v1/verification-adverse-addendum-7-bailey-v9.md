# Vérification adverse de l'addendum 7 du témoin de Bailey — v9 (lecture scellée v3)

Workflow `verification-lecture-v3-addendum-7-bailey`, run `wf_e15e59d0-626`, trois relecteurs neufs, sur l'addendum au commit `4d02db6f`
et `lecture_scellee_v3` (commit `a904aa39`). Retours consignés tels quels, dans l'ordre du journal ; l'angle de chaque retour est déduit de son résumé.

## Retour 1 — angle « critère central » — bloquant : oui

L'addendum 7 ne peut pas être scellé en l'état : il y a un bloquant, démontré dans /tmp. La règle du « retour perdu » (l. 202-205, reprise l. 237) fait consigner l'empreinte que rend `python -m controle_ia.scellement verifier <sortie>`. Or cette commande n'affiche que `OK <12 premiers caractères>…`, alors que `--controler --empreinte` compare les 64 caractères. Le contrôle rend donc « écart », et le run tombe à tort en « pas de verdict » sur un chemin réel : une ligne coupée à l'écriture est déjà arrivée à la répétition v2. Démonstration dans /tmp/claude-0/-home-user-controle-ia-travail/2cfa1854-671e-5aa7-83ff-79ac90ee7d37/scratchpad/demo_ctl.py : `controler` avec ce que rend `verifier` donne False ; avec l'empreinte complète du compagnon, True.

Recréation des répertoires vides. Elle ne dépend d'aucun résultat lu : c'est un geste mécanique, fait avant l'attendu, sur une liste produite par `find`. Mais elle n'est applicable que pour la sortie de la conduite v13. Elle ne couvre ni le dossier de reprise de la lecture 38, ni la relance par le chemin de l'addendum 5 :
- la reprise est écrite par un poste à part : `poste-fini-reprise-v2/v3` existent dans le dépôt ;
- le dossier de la relance est assemblé avant la clôture, à partir de sources venues par git, donc sans répertoires vides, alors que la recréation n'a lieu qu'ensuite.

« Eux seuls » est inapplicable aux répertoires emboîtés : `find` ne liste que la feuille, dont les parents sont absents de git. Et `find <sortie>` rend des chemins absolus, pas relatifs. Enfin, rien ne dit quand la liste est « absente », ni que faire d'une entrée déjà présente ou mal formée.

Poste v12 et § 6. Le poste v12 peut fournir la liste demandée : il a `find`, l'environnement Python, `PYTHONPATH` et la fonction qui pousse ; il suffit d'écrire la liste après la fin de la conduite, avant la marque de fin. Mais la liste des différences du § 6, étape 2, n'admet pas les noms neufs exigés par R12. La conduite refuse une sortie qui n'est pas neuve (`lanceur_v21`, l. 1654-1655). Côté poste, `offre-choisie-v12.json`, déjà sur la branche, ferait lancer l'offre suédoise de la relance après 24 h sans offre conforme (poste v12, l. 151). Cette liste ne nomme pas non plus la vérification d'empreinte de la l. 104 (conduite v13 → v15, manifeste v6 → v7). Le § 4, l. 332-333, omet la liste des répertoires vides que nomme le § 6.

Remarques. Les trois réglages ne sont pas exigés par `--controler`, contrairement à ce que dit le texte (sans effet). Les répertoires recréés et le `.venv` n'existent que sur la machine de la session : rien ne règle le cas d'un arbre recloné avant le contrôle final. Le § 5 ne déclare pas le risque que `lecture-assemblee-v1` soit lu sans les répertoires vides des postes, alors que c'est le verdict retenu dans la plupart des cas.

### 1. bloquant — l. 202-205 (puce « La lecture est faite par le code… », retour perdu) et l. 237 (puce « Cloison de la session », `--controler`)

**Constat.** Retour perdu : la session doit consigner « l'empreinte que rend `python -m controle_ia.scellement verifier <sortie>` ». Or `scellement._main` affiche `OK {verifier(a)[:12]}…  <chemin>`, soit 12 caractères suivis de « … ». `lecture_scellee_v3.controler` exige `scellement.verifier(sortie) == empreinte` sur les 64 caractères. Si l'on suit le texte à la lettre, `--controler` rend « écart », ce qui vaut « pas de verdict » pour ce run (puce « Refus ou erreur »). Le vrai chemin tombe donc à tort, sur un seul incident technique, déjà survenu à la répétition v2 (dernière ligne coupée à l'écriture). La l. 237 (« celle du compagnon ») contredit la l. 204. Démontré sur une sortie factice : `controler` avec ce que rend `verifier` donne False ; avec le premier champ du compagnon `.sha256`, il donne True.

**Correction proposée.** l. 202-205, remplacer « la session consigne l'empreinte que rend `python -m controle_ia.scellement verifier <sortie>`, sans ouvrir la sortie, et l'issue « non lue » » par : « la session joue `python -m controle_ia.scellement verifier <sortie>` (qui doit rendre « OK » ; il n'affiche que 12 caractères), puis consigne l'empreinte complète, 64 caractères, premier champ du compagnon `<sortie>.sha256`, sans ouvrir la sortie, et l'issue « non lue » ; si `verifier` ne rend pas « OK », l'absence de sortie scellée est constatée ». À la l. 237, remplacer « (ou, retour perdu, celle du compagnon, consignée de même) » par « (ou, retour perdu, l'empreinte complète de 64 caractères lue dans le compagnon `<sortie>.sha256` et consignée comme ci-dessus) ».

### 2. à corriger — l. 156-164 (liste des répertoires vides) ; renvois l. 155 (assemblage avant la clôture) et l. 256-260 (rejeu de l'assemblage)

**Constat.** La liste ne couvre que « la sortie de la conduite », écrite par le poste v13. Deux dossiers de lecture prévus par le même paragraphe ne sont pas couverts. (a) Le dossier de reprise de la lecture 38 est écrit après la fin du poste v13 par un poste de reprise distinct (`poste-fini-reprise-v2/v3.json` dans `runs/`). Ses répertoires vides arrivent par git, donc sont perdus, et aucune liste n'est demandée. (b) Pour la relance par le chemin de l'addendum 5, le poste de la relance n'écrit aucune liste. L'assemblage est fait avant la clôture, à partir de sources venues par git, alors que la recréation n'a lieu qu'« avant `--calculer-attendu` », donc après l'assemblage, et dans la sortie, qui n'est pas le dossier lu. Or des répertoires vides naissent justement dans les cas de panne qui mènent à une reprise ou à une relance : `rapatrier_fichier` crée `local.parent` avant le `scp`, et un `scp` en échec laisse `transfert-n/` ou `transfert-n/journal/` vide. `valider` en décide par `dossier_de_foi` (`transfert-2`), `pilotes` et `principal-relance`. La lecture peut alors différer de l'arbre produit, sans qu'aucune règle le dise. Pas de dépendance à un résultat, mais une règle incomplète sur deux chemins réels.

**Correction proposée.** l. 159-164, remplacer « Un dossier venu du poste arrive … dans l'arbre principal (geste technique, aucune note lue) ; » par : « Un dossier venu d'un poste arrive dans l'arbre principal par git, qui ne porte pas les répertoires vides, alors que `valider` décide aussi sur leur existence. Tout poste qui produit un dossier ensuite lu ou assemblé écrit, après la fin de sa conduite ou de sa reprise et avant sa marque de fin, la liste des répertoires vides de ce dossier, hors de ce dossier : `cd <dossier> && find . -mindepth 1 -type d -empty -printf '%P\n' | LC_ALL=C sort > <BASE>/repertoires-vides-<nom du dossier>-v1.txt`. Il la scelle, puis la pousse avec son compagnon. Ces postes sont : le poste v13 et celui d'une seconde tentative (sortie de la conduite), le poste d'une reprise de la lecture 38 (dossier de reprise), le poste d'une relance par le chemin de l'addendum 5 (sortie de sa conduite). Après avoir récupéré ces poussées, et avant tout assemblage et tout `--calculer-attendu`, la session applique chaque liste au dossier qu'elle nomme, dans l'arbre principal (règle ci-dessous ; geste technique, aucune note lue). L'assemblage d'une relance est joué ensuite, sur des sources qui portent ces répertoires. » Au § 6, étape 2, et dans les pièces neuves de l'addendum 5 et de la reprise, ajouter la même exigence pour leur poste.

### 3. à corriger — l. 161-164 (« `find <sortie> -type d -empty`, chemins relatifs » ; « crée ces répertoires, et eux seuls » ; « liste vide … liste absente … »)

**Constat.** Telle qu'écrite, la règle n'est pas applicable à la lettre. (1) `find <sortie> -type d -empty` rend des chemins absolus, pas relatifs (essai dans /tmp). (2) `find -empty` ne liste que les feuilles. Pour `pilote-reprise/transfert-1/journal/` vide, seule la feuille est listée ; `pilote-reprise/` et `transfert-1/`, absents de git, ne le sont pas. Créer « eux seuls » est donc impossible : un `mkdir` sans `-p` échoue, et `-p` crée des répertoires non listés. Or c'est l'existence de `pilote-reprise/` qui décide dans `valider`. (3) Rien ne dit ce qui se passe si une entrée existe déjà (répertoire ou fichier), si elle est absolue, contient `..` ou une ligne vide, ou si le compagnon manque ou ne concorde pas. (4) Le moment où la liste est « absente » n'est pas fixé : la session choisit quand cesser d'attendre. C'est une décision qui change ce qui est lu, sans dépendre d'un résultat puisqu'aucune note n'est connue, mais elle doit être mécanique.

**Correction proposée.** Remplacer « (`find <sortie> -type d -empty`, chemins relatifs) » par « (`cd <sortie> && find . -mindepth 1 -type d -empty -printf '%P\n' | LC_ALL=C sort`, chemins relatifs à la sortie) ». Remplacer « la session crée ces répertoires, et eux seuls, dans l'arbre principal (geste technique, aucune note lue) ; la note de clôture cite cette liste et son empreinte (liste vide : rien n'est créé ; liste absente : rien n'est créé, et c'est rapporté) » par : « la session vérifie la liste par `scellement verifier`, puis crée sous le dossier, dans l'arbre principal, chaque répertoire qu'elle nomme, avec ses parents absents (`mkdir -p`), et rien d'autre ; une entrée déjà présente comme répertoire est laissée telle quelle. Si une entrée est absolue, contient `..`, est vide, ou existe comme autre chose qu'un répertoire, ou si la liste n'est pas scellée ou que son compagnon ne concorde pas, rien n'est créé de cette liste, et c'est rapporté. La liste est absente si elle n'est pas sur la branche quand la marque de fin du poste y est, ou, sans marque de fin, quand la session constate la clôture : rien n'est créé, et c'est rapporté. Ce geste ne lit aucune note. La note de clôture cite chaque liste, son empreinte et ce qui a été créé. »

### 4. à corriger — § 6, étape 2, l. 389-393 ; § 4, l. 329-333 (pièces de lancement)

**Constat.** Le lecteur des pièces doit vérifier qu'elles « ne diffèrent … que par ce que cet addendum nomme ». La liste ne nomme pas : (a) les noms neufs (R12) des sorties de la conduite v15 et des fichiers du poste. Ils sont nécessaires : la conduite refuse une sortie non neuve (`lanceur_v21`, l. 1654-1655, « dossier de sortie de la conduite non neuf »). Le poste v12 lit et écrit `offre-choisie-v12.json`, `lancement-v13.pid`, `poste-fini-v12.json` et `poste-hetzner-v12-etat.txt`, tous déjà sur la branche. Si `offre-choisie-v12.json` garde son nom, le test `[ -s … ]` (l. 151) passe après 24 h sans offre conforme, et `OFFRE` devient l'offre suédoise de la relance (58516569), hors du filtre du § 2.4, au lieu de « rien ne tourne ». (b) La vérification d'empreinte de la l. 104 du poste (`lancer-conduite-v13.py.sha256`, `manifeste-local-v6.json.sha256` → v15, v7). (c) Le moment et le nom de la liste des répertoires vides. Le § 4, l. 332-333, définit le poste v13 sans cette liste, que nomme le § 6 : les deux paragraphes ne concordent pas.

**Correction proposée.** § 6, étape 2 : après « … garde du commit du code (§ 4 : … `git diff --quiet … HEAD -- src/`), », insérer : « noms neufs (R12), absents de la branche avant le lancement, de la sortie de la conduite et de chaque fichier écrit ou poussé par le poste (offre choisie, ordre, sorties et PID du lancement, bilan, état, journal, marque de fin), empreintes vérifiées par le poste à la ligne de la l. 104 du v12 portées sur la conduite v15 et le manifeste v7, ». Remplacer « liste des répertoires vides écrite, poussée et scellée par le poste (§ 3) » par « liste des répertoires vides de la sortie, écrite après la fin de la conduite et avant la marque de fin, au nom fixé au § 3, scellée, puis poussée avec son compagnon ». § 4, l. 332-333 : remplacer « = le poste v12 avec la conduite v15, le filtre du § 2.4 et la garde du commit du code (`a904aa39`) » par « = le poste v12 avec la conduite v15, le filtre du § 2.4, la garde du commit du code (`a904aa39`), la liste des répertoires vides (§ 3) et des noms neufs (R12 ; § 6, étape 2) ».

### 5. remarque — l. 172-176 (« la même pour `--calculer-attendu`, la lecture et `--controler` … le code refuse sans ces trois réglages »)

**Constat.** Le chemin `--controler` de `principal` (l. 266-271 du code) n'appelle pas `garde_commande` : il ne refuse pas une commande sans `-B`, sans `-P` ou sans `PYTHONPYCACHEPREFIX`. Sans effet sur une lecture, puisque `controler` ne calcule aucune empreinte de code, de dossier ni d'environnement, mais le texte prête au code une garde qu'il n'a pas.

**Correction proposée.** Remplacer « le code refuse sans ces trois réglages » par « `--calculer-attendu` et la lecture refusent sans ces trois réglages ; `--controler`, qui ne calcule aucune empreinte de code, de dossier ni d'environnement, ne les vérifie pas ».

### 6. remarque — l. 178-182 (interdit du premier attendu au dernier contrôle final) et l. 201 (commande dans les 24 h)

**Constat.** Les répertoires recréés, le `.venv` et l'interpréteur n'existent que sur la machine de la session : git ne les porte pas. Si l'arbre principal est recloné, par exemple avec un conteneur neuf entre deux sessions (R14 impose une passation à chaque fin de session), la lecture rend « refus : empreintes ». `--controler` devient injouable avec « la même commande », puisque `<racine>/.venv/bin/python` est absent et qu'aucune installation n'est permise. Le texte ne dit pas ce que vaut alors le contrôle. Le conteneur actuel a gardé son `.venv` depuis le 11 novembre, d'où une remarque.

**Correction proposée.** Après « … `add`, `commit` et `push` hors de `src/` restent permis. », ajouter : « Le calcul des attendus, l'essai factice, la note de clôture et chaque commande sur un dossier réel sont joués dans le même arbre principal, sans re-clonage. Si, après la dernière commande sur un dossier réel, `--controler` ne peut être joué faute de l'interpréteur du dépôt, la session réinstalle `requirements-cpu.txt` pour lui seul, sans toucher à `src/`, et c'est rapporté. Un contrôle qui ne peut être joué vaut « écart ». »

### 7. remarque — § 5 (f), l. 359-363 (renvoi du § 3, l. 165-166)

**Constat.** Le § 3 lit `lecture-assemblee-v1` dans l'état de l'arbre principal, sans les répertoires vides des postes des séries 1 à 3 et de la relance, qui sont inconnus. C'est pourtant le verdict retenu dans tous les cas sauf K′ ≥ 71. Ce risque, qui peut faire différer sa lecture de celle des arbres des postes, n'est pas déclaré au § 5.

**Correction proposée.** À la fin du § 5 (f), ajouter : « ; `lecture-assemblee-v1` est lu sans les répertoires vides des postes des séries 1 à 3 et de la relance, que git n'a pas portés et qui ne sont pas connus (§ 3) : sa lecture peut différer de celle des arbres des postes, ce qui est rapporté avec le verdict à 36 tours ».

## Retour 2 — angle « code v3 » — bloquant : oui

Angle « code lecture_scellee_v3 et essais ». Le code tient sur le vrai chemin : je n'ai trouvé aucune voie qui donne « aboutie » d'un code ou d'un dossier modifié par négligence, ni aucun refus à tort sur un dossier et un code intacts quand on joue la commande du § 3 telle qu'écrite. Un bloquant subsiste dans le texte, sur le chemin « retour perdu » qu'il décrit lui-même.

Essais faits (dépôt minimal sous /tmp/r2v3/depot, arbre src/ = e3f066a9…, identique à a904aa39:src et à HEAD:src du dépôt réel ; .venv du dépôt ; dossier factice construit avec T3.poste_local) :
- 33 essais de la v3 passés sous `python -B`.
- `--calculer-attendu` joué depuis six répertoires courants (/, racine, src/, le dossier lu, un de ses sous-dossiers, /tmp), dossier écrit avec une barre finale : six attendus identiques octet pour octet.
- Lecture jouée depuis src/controle_ia, dossier avec barre finale : « aboutie ». Contrôle joué depuis /, sans barre finale : « conforme ».
- Avec -B, aucun répertoire PYTHONPYCACHEPREFIX n'est créé ni ne grandit, que ce soit à l'attendu, à la lecture ou au contrôle.
- Empreinte de l'environnement inchangée après une exécution de une_execution : ni sys.path ni les distributions ne bougent.
- `git status` marche même avec un .git/index.lock présent.
- Dans le dépôt réel, src/ ne porte aujourd'hui que des fichiers ignorés sous __pycache__/.
- Les 87 échecs des essais v21 et reprise viennent de mon dépôt minimal, qui n'a pas docs/ (versions figées absentes) ; ils ne disent rien du code.

Bloquant démontré : `python -m controle_ia.scellement verifier` n'imprime que 12 chiffres de l'empreinte suivis de « … ». Or `--controler` exige les 64 chiffres. Sur une sortie intacte, appliquer le texte tel qu'écrit donne donc « écart », soit « pas de verdict ».

Trois points à corriger :
- La liste des répertoires vides ne couvre ni la reprise ni l'assemblage.
- L'interdit d'écrire sous src/ contredit la routine R14 et la construction du dossier factice.
- Un renvoi de la puce « La lecture est faite par le code » ne correspond pas au code pour une sortie présente sans compagnon.

Une remarque sur les répertoires PYTHONPYCACHEPREFIX et les chemins d'attendu et de sortie.

À signaler : en voulant monter mon dépôt d'essai, j'ai d'abord écrit par erreur dans un clone qui existait déjà dans le dossier de travail temporaire (scratchpad/depot, hors du dépôt). J'y ai ajouté puis retiré un commit (`git reset --hard 3e14ff29`), et sa configuration git locale reçoit désormais user.name et user.email. Rien n'a été écrit dans /home/user/controle-ia-travail.

### 1. bloquant — l. 203-205 (puce « La lecture est faite par le code ») et l. 236-237 (puce « Cloison de la session »)

**Constat.** Retour perdu. Le texte fait consigner « l'empreinte que rend `python -m controle_ia.scellement verifier <sortie>` », puis passer cette empreinte à `--controler` (« ou, retour perdu, celle du compagnon, consignée de même »). Or `scellement._main` imprime `OK {verifier(a)[:12]}…  {a}`, soit 12 chiffres et une ellipse, alors que `controler` compare `scellement.verifier(sortie) != empreinte` sur les 64 chiffres. Démontré sur dossier factice : la commande imprime « OK cf4522e8b65e…  …/sortie.json », et `--controler … --empreinte cf4522e8b65e…` rend {"controle": "écart"} (code 2) sur une sortie intacte. C'est une règle inapplicable telle qu'écrite, sur un chemin que le texte décrit. Elle fait tomber à tort ce run en « pas de verdict », sans faute de la session : une ligne de retour perdue suffit.

**Correction proposée.** l. 203-205, remplacer « la session consigne l'empreinte que rend `python -m controle_ia.scellement verifier <sortie>`, sans ouvrir la sortie, et l'issue « non lue » » par : « la session joue `PYTHONPATH=<racine>/src <racine>/.venv/bin/python -B -c "from controle_ia import scellement; print(scellement.verifier('<sortie>'))"` (chemin absolu) et consigne l'empreinte entière qu'il imprime (64 chiffres hexadécimaux, égale à celle du compagnon `<sortie>.sha256`), sans ouvrir la sortie, et l'issue « non lue » ; la commande `python -m controle_ia.scellement verifier`, qui n'imprime que 12 chiffres, ne sert pas à cette fin ». l. 237, remplacer « (ou, retour perdu, celle du compagnon, consignée de même) » par « (ou, retour perdu, l'empreinte entière, 64 chiffres, consignée comme ci-dessus) ».

### 2. à corriger — l. 160-164 (liste des répertoires vides du poste v13)

**Constat.** La liste ne couvre que « la sortie de la conduite », écrite par le poste v13 « après son dernier transfert ». Deux cas restent dehors.

1. Reprise de la lecture 38. `Reprise.reprendre` (lanceur_v21, l. 2347-2352) écrit `reprise-v10*/` sous la sortie de la conduite, sur un poste, puisque la session ne peut pas ouvrir de connexion ssh. Ce dossier revient par git, qui ne porte pas les répertoires vides, et aucune liste ne le couvre.

2. Relance par le chemin de l'addendum 5. Si l'assemblage précède la recréation dans les dossiers sources, `assembler_lecture` copie des sources privées de leurs répertoires vides.

Or un répertoire vide peut décider. `rapatrier_fichier` (l. 470) crée `transfert-n/` avant scp ; si un scp échoue, il reste un `transfert-1/` vide. Avec lui, `dossier_de_foi` passe à `transfert-2` ; sans lui, la boucle s'arrête dès n = 1, aucun dossier de foi, d'où un autre état. La lecture serait fausse sans aucun refus, alors que l'empreinte tient (elle est prise sur l'arbre principal).

**Correction proposée.** Remplacer « le poste v13 écrit, après son dernier transfert, la liste des répertoires vides de la sortie de la conduite (`find <sortie> -type d -empty`, chemins relatifs), la pousse et la scelle ; avant `--calculer-attendu`, la session crée ces répertoires, et eux seuls, dans l'arbre principal » par : « tout poste qui écrit dans un dossier destiné à la lecture, ou dans une source d'assemblage (poste v13 de la conduite ; poste d'une reprise de la lecture 38, qui écrit `reprise-v10*/` sous la sortie de la conduite ; poste d'une relance par le chemin de l'addendum 5), écrit, après sa dernière écriture dans ce dossier, la liste de ses répertoires vides (`cd <dossier> && find . -type d -empty`), la pousse et la scelle ; pour chaque dossier, la dernière liste écrite fait foi ; avant tout assemblage et avant `--calculer-attendu`, la session crée ces répertoires, et eux seuls, dans chaque dossier source de l'arbre principal ». À la suite, remplacer « la note de clôture cite cette liste et son empreinte » par « la note de clôture cite chaque liste et son empreinte ».

### 3. à corriger — l. 178-180 (« ne crée ni ne modifie de fichier sous `src/` »)

**Constat.** L'interdit ne tient pas tel qu'écrit. La routine de reprise R14, obligatoire à chaque session de la fenêtre (qui dure 24 h et plus), joue `python -m pytest -q` sans -B : elle écrit des .pyc sous src/**/__pycache__/. La construction du dossier factice, que le texte place après le calcul des attendus réels, importe aussi src/ et en écrit. Le code tolère ces fichiers (`arbre_src_propre` filtre « !! » et « /__pycache__/ ») : le verdict n'est pas touché. Mais la règle est violée par les étapes mêmes qu'imposent CLAUDE.md et ce texte, sans dire ce que vaut cette violation.

**Correction proposée.** Remplacer « ne crée ni ne modifie de fichier sous `src/` ou sous un dossier donné à une lecture » par « ne crée ni ne modifie de fichier sous `src/` (hors des `.pyc` sous `__pycache__/`, que le code tolère ; la routine de reprise et la construction du dossier factice se jouent de préférence avec `python -B`) ni sous un dossier donné à une lecture ».

### 4. à corriger — l. 206-209 (puce « La lecture est faite par le code », exécution sans sortie scellée)

**Constat.** Le cas « sortie présente sans son compagnon » ne correspond pas au code. Le texte dit que le code « refuse alors de la remplacer ». C'est vrai, mais il laisse une voie ouverte : si `scellement.sceller(s)` n'a pas abouti, la sortie existe sans compagnon. Rejouer la commande sous le même nom rend alors « refus : sortie déjà présente (R12) », code 3, sans rien écrire. Le texte constate l'absence de sortie, ce qui est cohérent. Il ne dit pas que le rejeu à l'identique, permis seulement « si aucune sortie n'est présente », ne doit pas être tenté pour constater ce refus. Une session qui le tenterait n'obtiendrait qu'une ligne R12, qui n'est pas l'une des trois issues.

**Correction proposée.** Après « une sortie présente sans son compagnon n'est ni ouverte ni scellée après coup, et le code refuse alors de la remplacer », ajouter : « (la commande n'est pas rejouée : une ligne « refus : sortie déjà présente (R12) » n'est pas une issue) ».

### 5. remarque — l. 172-173, l. 186 et l. 206 (PYTHONPYCACHEPREFIX « neuf et vide à chaque exécution »)

**Constat.** Trois écarts mineurs autour de ce réglage.
- Contradiction avec « rejouée une fois, à l'identique » (l. 206) et avec « jouée telle quelle, aux seuls chemins du dossier, de l'attendu et de la sortie près » (essai factice) : le préfixe change lui aussi.
- Le code n'exige pas que le répertoire soit neuf ni vide.
- Avec -B rien n'y est écrit. Vérifié : le répertoire n'est même pas créé après l'attendu, la lecture et le contrôle. Un préfixe absent ou vide réutilisé est donc sans effet.

**Correction proposée.** l. 172-173, remplacer « PYTHONPYCACHEPREFIX=<répertoire neuf et vide à chaque exécution> » par « PYTHONPYCACHEPREFIX=<répertoire absent ou vide, hors de `src/` et des dossiers donnés à une lecture ; avec `-B` rien n'y est écrit, le même sert à toutes les exécutions> ». Dans la phrase de l'essai factice, remplacer « aux seuls chemins du dossier, de l'attendu et de la sortie près » par « aux seuls chemins du dossier, de l'attendu, de la sortie et du répertoire `PYTHONPYCACHEPREFIX` près ».

### 6. remarque — l. 176-178 (rien écrit sous un dossier lu) ; code : principal(), _sous

**Constat.** Le code ne vérifie l'emplacement de l'attendu et de la sortie que par rapport au dossier de l'appel en cours. Il ne regarde ni l'autre dossier lu, ni src/. Exemples : la sortie de la lecture à 36 tours placée sous le dossier de la confirmation, ou un attendu placé sous src/. La lecture suivante tomberait alors en « refus : empreintes » (src/ non suivi, ou dossier changé). Il faut une seule faute, déjà interdite par le texte ; la note de clôture peut la fermer par programme.

**Correction proposée.** Ajouter après « (le code refuse un attendu ou une sortie sous le dossier lu) » : « ; avant la première lecture, la session vérifie par programme (chemins résolus, `Path.resolve().is_relative_to`) qu'aucun chemin d'attendu, de sortie ni de `PYTHONPYCACHEPREFIX` nommé par la note de clôture n'est sous `<racine>/src` ni sous aucun des dossiers donnés à une lecture, et la note le cite ».

## Retour 3 — angle « application des constats du rapport v8 » — bloquant : oui

Vérifié par programme, au commit 4d02db6f :
- Empreintes citées exactes : rapport v8 b4d37901… (compagnon égal), lecture_scellee_v3 a367853b…, essais 728a02e0…, répétition v3 ea4ed578… (compagnon égal) ; v1 et v2 inchangées (1b6f365e…, 5b2e7859…).
- Le commit a904aa39 porte ces deux fichiers de code avec les mêmes empreintes, et il est sur la branche du témoin.
- `git diff --stat 873ab00c a904aa39 -- src` ne porte que l'ajout des trois lectures scellées. L'arbre src/ de 4d02db6f est celui de a904aa39 (e3f066a9…).
- Les fichiers de `lanceur_v21.CHEMINS_ARCHIVE` sont tous sous src/ et hors des lectures scellées : ils sont donc identiques à 873ab00c.
- Texte : aucune marque @@, chaque nouveau texte présent une seule fois, aucune phrase répétée ni cassée. Plus aucune mention de la v2 comme code en service, ni de 91132fd0 comme commit du code.

Essais, dans une copie sous le répertoire temporaire, avec le .venv et `python -B` :
- tests/test_temoin_bailey_lecture_scellee_v3.py : 33 passés, reproduit.
- Lectures v1, v2 et v3 plus compléments : 80 passés (15 + 28 + 33 + 4).
- Ensemble annoncé : 305 passés et 3 sautés. Les 2 sauts de plus sont « structure réelle absente », dus à ma copie partielle ; le total de 308 concorde avec les 307 + 1 annoncés.

Rapport v8 : les 18 constats sont appliqués en substance, sauf trois :
- (a) Retour 1, constat 5 (repris par le retour 2, constat 7) : appliqué avec un défaut (constat bloquant ci-dessous).
- (b) Retour 1, constat 3 : la partie « attendu calculé une fois le dossier complet, poste arrêté, dernière récupération » n'est pas reprise.
- (c) Retour 1, constat 2 : les remplacements de « telle quelle » et « à l'identique », au sujet de `PYTHONPYCACHEPREFIX`, ne sont pas repris.
Le dernier paragraphe de « Contre-lecture » est exact par ailleurs (traitement v3, gel de src/ limité à la branche, formulations v7), mais « Aucun autre constat écarté » ne l'est pas.

Critère central : il tient. Aucune décision nouvelle ne dépend d'une note ni d'un verdict lu, et le code v3 ferme bien les deux bloquants v8 : chemins normalisés au contrôle, et environnement sans répertoire courant grâce à -P.

Un bloquant, démontré sur un dossier factice : le chemin « retour perdu » du § 3 fait tomber une lecture saine en « écart ».

Cloisons tenues :
- Aucun fichier de runs/ ouvert hors les deux permis.
- Lecture scellée jouée sur dossier factice seulement, sous le répertoire temporaire.
- Rien écrit dans le dépôt, aucune commande réseau.

### 1. bloquant — addendum § 3 l. 202-205 (retour perdu) et l. 237 ; Contre-lecture l. 527 (« retour perdu (empreinte du compagnon) »)

**Constat.** Le texte fait consigner, en cas de retour perdu, « l'empreinte que rend `python -m controle_ia.scellement verifier <sortie>` ». Or cette commande n'imprime que `OK <12 premiers chiffres>…  <chemin>` (scellement.py l. 126 : `verifier(a)[:12]`). `--controler` compare `scellement.verifier(sortie) != empreinte`, sur 64 chiffres. Je l'ai démontré dans une copie au commit, sur un dossier factice (T3.poste_local, 21 tours), avec la commande consignée (-B -P, PYTHONPYCACHEPREFIX neuf, trois répertoires courants) : lecture « aboutie » ; puis `--controler` avec l'empreinte rendue par `verifier` donne {"controle": "écart"}, code 2 ; avec l'empreinte entière du compagnon, « conforme ». Sur ce chemin décrit par le texte, une lecture saine tombe donc en « pas de verdict », sans aucune faute de la session. La l. 237 (« celle du compagnon ») contredit en outre la l. 204, si bien que la règle n'est pas applicable telle qu'écrite. Ce défaut vient du texte proposé par le retour 1, constat 5 ; le retour 2, constat 7 proposait, lui, le compagnon.

**Correction proposée.** L. 203-205, remplacer « la session consigne l'empreinte que rend `python -m controle_ia.scellement verifier <sortie>`, sans ouvrir la sortie, et l'issue « non lue » » par « la session joue `python -m controle_ia.scellement verifier <sortie>`, qui doit rendre « OK » (il n'imprime que les 12 premiers chiffres), puis consigne l'empreinte entière (64 chiffres hexadécimaux) lue dans le compagnon `<sortie>.sha256`, sans ouvrir la sortie, et l'issue « non lue » ; si `verifier` ne rend pas « OK », l'absence de sortie scellée est constatée ». L. 237, remplacer « (ou, retour perdu, celle du compagnon, consignée de même) » par « (ou, retour perdu, l'empreinte entière lue dans le compagnon, consignée de même) ».

### 2. à corriger — addendum § 3 l. 160-165 (liste des répertoires vides), l. 157-159 et 256-260 (assemblage), l. 178-182 (interdit de `git pull`) ; § 6 étape 2 l. 393

**Constat.** Trois défauts autour de la liste des répertoires vides.
- Moment du calcul. Le retour 1, constat 3, demandait que l'attendu ne soit calculé qu'une fois le dossier complet : après le dernier état poussé par le poste (poste arrêté, instance détruite) et après la dernière récupération de la branche. Ce n'est pas repris. Le texte prévoit même « liste absente : rien n'est créé ». Une session peut donc calculer l'attendu avant la dernière poussée du poste. Elle ne peut ensuite plus récupérer la liste, puisque `pull`, `merge` et `rebase` lui sont interdits. Elle ne peut plus non plus pousser ses passations : le distant a avancé, et `push` serait refusé. La lecture porte alors sur un dossier incomplet, sans répertoires vides (valider en décide, l. 473, 522, 546 de lecture_v8). La copie lue n'est pas celle du run, par un choix d'horaire qui ne dépend d'aucun résultat.
- Libellé. « après son dernier transfert » : le poste ne fait pas de transfert ; c'est la conduite qui en fait.
- Assemblage. `assembler_lecture` décide lui aussi sur l'existence de répertoires dans ses sources (lanceur_v21 l. 2681-2694). Or la liste n'est recréée qu'« avant `--calculer-attendu` », donc après un assemblage fait avant la clôture. La sortie du poste d'une relance par le chemin de l'addendum 5, ou d'une reprise, n'est pas couverte.

**Correction proposée.** L. 160-163, remplacer « le poste v13 écrit, après son dernier transfert, la liste des répertoires vides de la sortie de la conduite (`find <sortie> -type d -empty`, chemins relatifs), la pousse et la scelle ; avant `--calculer-attendu`, la session crée ces répertoires » par « tout poste dont la sortie est lue ou assemblée (poste v13 ; poste d'une relance par le chemin de l'addendum 5 ou d'une reprise) écrit, une fois sa conduite finie, la liste des répertoires vides de sa sortie (`find <sortie> -type d -empty`, chemins relatifs), la scelle et la pousse dans sa dernière poussée ; la session ne joue un assemblage ni un `--calculer-attendu` qu'après avoir récupéré cette dernière poussée, poste arrêté et instance détruite constatés ; avant l'assemblage et avant `--calculer-attendu`, elle crée ces répertoires ». § 6 étape 2, remplacer « liste des répertoires vides écrite, poussée et scellée par le poste (§ 3) » par « liste des répertoires vides écrite après la fin de la conduite, scellée et poussée dans la dernière poussée du poste (§ 3) ».

### 3. à corriger — addendum § 3 l. 183 (« telle quelle, aux seuls chemins du dossier, de l'attendu et de la sortie près ») et l. 206 (« rejouée une fois, à l'identique ») ; Contre-lecture l. 532 (« Aucun autre constat écarté »)

**Constat.** Le retour 1, constat 2, demandait deux remplacements. D'abord, ajouter le répertoire de `PYTHONPYCACHEPREFIX` aux différences permises de l'essai factice. Ensuite, préciser « à l'identique » au rejeu (mêmes variables, répertoire neuf). Aucun des deux n'est fait. Or la commande exige un `PYTHONPYCACHEPREFIX` « neuf et vide à chaque exécution » : un essai joué « telle quelle, aux seuls chemins du dossier, de l'attendu et de la sortie près », ou un rejeu « à l'identique », le contredit à la lettre. Le paragraphe de contre-lecture, qui dit « Aucun autre constat écarté », est donc inexact sur ce point. Il l'est aussi pour la partie « dossier complet » du retour 1, constat 3 (constat précédent).

**Correction proposée.** L. 183, remplacer « aux seuls chemins du dossier, de l'attendu et de la sortie près » par « aux seuls chemins du dossier, de l'attendu, de la sortie et du répertoire neuf de `PYTHONPYCACHEPREFIX` près ». L. 206, remplacer « est rejouée une fois, à l'identique, » par « est rejouée une fois, à l'identique (mêmes arguments et variables, répertoire de `PYTHONPYCACHEPREFIX` neuf), ». L. 532, remplacer « Aucun autre constat écarté. » par « Aucun autre constat écarté ; repris après la v9 : « telle quelle » et « à l'identique » au regard de `PYTHONPYCACHEPREFIX`, attendu et assemblage après la dernière poussée du poste (retour 1, constats 2 et 3), empreinte entière du compagnon au retour perdu. »

### 4. remarque — addendum § 3 l. 178-180 (« ne crée ni ne modifie de fichier sous `src/` »)

**Constat.** Prise à la lettre, la règle est violée par des gestes ordinaires, entre le premier attendu et le dernier contrôle :
- la routine de reprise R14 (`verifier-arbre` et `pytest`, sans -B) ;
- la construction par programme du dossier factice, qui importe controle_ia.
Ces gestes écrivent ou réécrivent des `.pyc` sous `src/**/__pycache__/`. Le code les tolère (arbre_src_propre filtre `/__pycache__/`), et -B avec un `PYTHONPYCACHEPREFIX` neuf empêche de les relire : aucun verdict n'en dépend. Mais la règle ne peut pas être tenue telle qu'écrite par une session qui suit R14.

**Correction proposée.** L. 179, remplacer « ne crée ni ne modifie de fichier sous `src/` ou sous un dossier donné à une lecture » par « ne crée ni ne modifie de fichier sous `src/` (hors `__pycache__`, que le code tolère et que la commande ne relit pas) ou sous un dossier donné à une lecture ».
