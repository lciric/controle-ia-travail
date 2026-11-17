# Vérification adverse de l'addendum 7 du témoin de Bailey — v10 (corrections de texte après la v9)

Workflow `verification-v10-addendum-7-bailey`, run `wf_27029292-039`, deux relecteurs neufs, sur l'addendum au commit `27306ea4`
(différence `4d02db6f..27306ea4`). Retours consignés tels quels, dans l'ordre du journal ; l'angle de chaque retour est déduit de son résumé.

## Retour 1 — angle « application des constats du rapport v9 » — bloquant : non

Rien n'empêche de sceller l'addendum 7 au commit 27306ea4. Je n'ai trouvé aucune voie par laquelle une décision qui change le verdict retenu dépendrait d'un résultat lu : les règles nouvelles jouent toutes avant la clôture ou sans aucune note connue.

Constats du rapport v9 :
- Le bloquant commun aux trois retours est fermé. Au retour perdu, la session lit l'empreinte entière dans le compagnon, après un `verifier` qui rend « OK », aux l. 221-225 et 258. C'est conforme à `scellement._main` et à `controler`.
- Les autres constats sont appliqués en substance : liste des répertoires vides étendue, commande exacte, `mkdir -p`, entrées invalides, un seul `PYTHONPYCACHEPREFIX`, `__pycache__` toléré, garde de commande, sortie sans compagnon, noms neufs, § 4 et § 5 (f).

Vérifié par programme :
- Chaque ligne ajoutée est présente une seule fois ; aucune marque @@ ; aucune phrase répétée.
- L. 104 du poste v12 : elle vérifie bien `lancer-conduite-v13.py.sha256` et `manifeste-local-v6.json.sha256`. L. 143 : c'est bien le filtre.
- Les 10 fichiers de `CHEMINS_ARCHIVE` sont identiques à 873ab00c, a904aa39 et 27306ea4. L'arbre `src/` est le même (e3f066a9…) à a904aa39 et à 27306ea4.
- L'empreinte du rapport v9 vaut f898d1b1…, égale à son compagnon au commit.
- La commande `find` du § 3 marche, essayée dans /tmp : chemins relatifs, feuilles imbriquées recréées avec leurs parents.

Restent deux points à corriger et des remarques :
- Constat 1 : sans marque de fin, l'absence d'une liste se constate à la clôture, alors que les listes doivent être appliquées avant l'assemblage et l'attendu, qui précèdent la note de clôture.
- Constat 2 : la réinstallation permise pour le contrôle contredit l'interdit d'installer.
- Constat 7 : le dernier paragraphe de « Contre-lecture » est exact, sauf « Aucun constat écarté ». Trois propositions v9 ont été reprises autrement, et le paragraphe v8, jugé inexact par la v9 (retour 3), n'a pas été corrigé.

### 1. à corriger — l. 166-167 et 172-174 (§ 3, liste absente sans marque de fin)

**Constat.** « Une liste est absente si […] sans marque de fin, quand la session constate la clôture ». Or les listes sont appliquées « avant tout assemblage et tout `--calculer-attendu` », et ces deux gestes précèdent la note de clôture, qui nomme les attendus et, en cas de relance par le chemin de l'addendum 5, n'est écrite qu'« après l'assemblage » (l. 155). L'absence se décide donc après le geste qu'elle conditionne : la règle est circulaire, et inapplicable telle qu'écrite pour un poste sans marque de fin. Ce cas est réel dans le poste v12 : `pousser` en échec à la dernière poussée (l. 80-84), sortie anticipée par `exit 3`, machine perdue. Sans marque de fin, « dernière poussée » et « poste arrêté » ne sont pas définis non plus. La machine Hetzner est détruite par la session (poste v12, l. 42), qui choisirait seule ce moment. Aucun résultat n'est lu, mais ce qui est lu dépend d'un horaire qui n'est fixé par aucune règle.

**Correction proposée.** Remplacer « Une liste est absente si elle n'est pas sur la branche quand la marque de fin du poste y est, ou, sans marque de fin, quand la session constate la clôture : rien n'est créé, et c'est rapporté. » par « Une liste est absente si elle n'est pas sur la branche quand la marque de fin du poste y est ; sans marque de fin, la dernière poussée du poste est l'état de la branche quand la session a constaté l'instance détruite puis détruit la machine du poste (ou constaté sa perte), et une liste qui n'y est pas est absente : rien n'est créé, et c'est rapporté. Ce constat précède tout assemblage et tout `--calculer-attendu`. »

### 2. à corriger — l. 191-192 (interdit d'installer) et l. 198-199 (réinstallation)

**Constat.** Contradiction nouvelle. La l. 191 dit : « Entre le premier `--calculer-attendu` et le dernier contrôle final, aucune session n'installe ni ne retire de distribution ». La l. 198, plus bas dans la même fenêtre, dit : « la session réinstalle `requirements-cpu.txt` ». Le texte appliqué a aussi perdu la borne de la proposition v9 (retour 1, constat 6) : « après la dernière commande sur un dossier réel ». La réinstallation ne compte plus seulement après les lectures, donc hors de tout calcul d'empreinte d'environnement. Sans effet sur un verdict aujourd'hui, puisque `--controler` ne joue qu'après les deux verdicts. Mais les deux phrases se contredisent à la lettre.

**Correction proposée.** L. 191-192 : remplacer « aucune session n'installe ni ne retire de distribution, » par « aucune session n'installe ni ne retire de distribution (hors la réinstallation pour le seul contrôle final, ci-dessous), ». L. 198 : remplacer « si `--controler` ne peut être joué faute de l'interpréteur du dépôt » par « si, après la dernière commande sur un dossier réel, `--controler` ne peut être joué faute de l'interpréteur du dépôt ».

### 3. remarque — l. 182-183 (commande consignée)

**Constat.** Phrase cassée au rendu. Des accents graves sont emboîtés dans le bloc de code de la commande (`src/` et `-B` à l'intérieur de « `PYTHONPATH=… …lecture_scellee_v3 …` »). Le bloc se coupe en trois morceaux, et la commande rendue n'est plus lisible d'un seul tenant. Le texte brut reste compréhensible.

**Correction proposée.** Remplacer « `PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<répertoire absent ou vide, hors de `src/` et des dossiers lus ; avec `-B` rien n'y est écrit, le même sert à toutes les exécutions> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 …` » par « `PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<cache> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 …`, où `<cache>` est un répertoire absent ou vide, hors de `src/` et des dossiers lus (avec `-B` rien n'y est écrit ; le même sert à toutes les exécutions) ».

### 4. remarque — l. 189-191 (contrôle par programme des chemins)

**Constat.** La vérification est placée « avant la première lecture », alors que la note de clôture, écrite avant les lectures, doit la citer. Rien ne dit non plus ce que vaut un échec. Un attendu déjà écrit sous `src/` ne peut plus être retiré, puisque la l. 192 interdit d'y toucher. La session devrait donc improviser, sans dépendre d'un résultat, mais sans règle.

**Correction proposée.** Remplacer « avant la première lecture, la session vérifie par programme » par « avant la note de clôture, la session vérifie par programme ». Après « et la note le cite », ajouter : « ; si cette vérification échoue, la note le dit, aucun chemin n'est changé, et la puce « Refus ou erreur à la lecture » s'applique ensuite sans exception ».

### 5. remarque — l. 165 (nom de la liste) et l. 168 (« le dossier qu'elle nomme »)

**Constat.** La liste ne nomme son dossier que par son nom de base. Le dossier de reprise s'appelle `reprise-v10` sous la sortie de la conduite (lanceur_v21, l. 2348-2351), et ce nom existe déjà sous d'autres sorties (`…/sortie-conduite-v11/reprise-v10-2`, § 1). Deux tentatives avec reprise produiraient deux listes de même nom (`repertoires-vides-reprise-v10-v1.txt`) : collision R12 au scellement, et dossier cible ambigu. Ce défaut demande plusieurs incidents cumulés.

**Correction proposée.** Remplacer « > <BASE>/repertoires-vides-<nom du dossier>-v1.txt` » par « > <BASE>/repertoires-vides-<chemin>-v1.txt`, où `<chemin>` est le chemin du dossier relatif à `<BASE>`, chaque « / » remplacé par « -- » ».

### 6. remarque — l. 161-163 (énumération des postes)

**Constat.** L'énumération entre parenthèses omet le poste d'une mise en place refaite (§ 2.1 ; l. 363 : conduite et script de poste neufs). Sa sortie serait pourtant lue. La règle générale « Tout poste qui produit un dossier ensuite lu » la couvre, mais l'énumération semble complète.

**Correction proposée.** Après « poste v13 et celui d'une seconde tentative : sortie de la conduite ; », insérer « poste d'une mise en place refaite (§ 2.1 ; l. 363) : sortie de sa conduite ; ».

### 7. remarque — l. 573-574 (dernier paragraphe de « Contre-lecture », « Aucun constat écarté. »)

**Constat.** Le paragraphe est exact dans son relevé : empreinte f898d1b1… égale au compagnon, commit 4d02db6f, essais du retour 2, bloquant commun aux trois retours, liste des reprises conforme au texte. Mais « Aucun constat écarté » ne l'est pas tout à fait :
(a) Retour 2, constat 2 : « la dernière liste écrite fait foi » est remplacé par un nom fixe en `-v1`.
(b) Retour 1, constat 3 : la note devait citer « ce qui a été créé » ; elle ne cite que chaque liste et son empreinte (l. 174).
(c) Retour 1, constat 2 : l'exigence n'est pas ajoutée aux pièces neuves de l'addendum 5 et de la reprise ; seule la règle générale du § 3 la porte.
(d) Retour 3, constat 3 : le paragraphe v8 garde « Aucun autre constat écarté », que la v9 a jugé inexact. Le paragraphe v9 ne dit pas que deux constats v8 (« telle quelle » et « à l'identique » ; attendu après la dernière poussée) sont repris seulement maintenant.

**Correction proposée.** Remplacer le dernier « Aucun constat écarté. » par : « Repris autrement : une liste par dossier, à nom fixe (`-v1`), au lieu de « la dernière liste écrite fait foi » (retour 2, constat 2) ; la note cite chaque liste et son empreinte, non ce qui a été créé (retour 1, constat 3) ; l'exigence pour les pièces de l'addendum 5 et de la reprise est portée par la règle générale du § 3, non par le § 6 (retour 1, constat 2). Deux constats de la v8, dits repris au paragraphe précédent sans l'avoir été (retour 1, constats 2 et 3 : « telle quelle » et « à l'identique » au regard de `PYTHONPYCACHEPREFIX` ; attendu après la dernière poussée du poste), le sont ici (v9, retour 3, constats 2 et 3). Aucun autre constat écarté. »

## Retour 2 — angle « corrections » — bloquant : oui

Je ne peux pas sceller l'addendum 7 au commit 27306ea4 en l'état : il reste un bloquant, d'ordre textuel. Au retour perdu, la commande `verifier` telle qu'elle est écrite échoue sur le vrai chemin, et le texte en tire une perte de verdict sans retour. Le cœur des corrections tient. Retour perdu rejoué sur une sortie factice (`verifier`, puis compagnon, puis `--controler`) : « conforme ». Commande `find` exacte jouée sur des répertoires vides imbriqués, recréation par `mkdir -p` dans une copie git : l'empreinte du dossier redevient celle d'origine, et l'existence des répertoires que `valider` teste aussi. `PYTHONPYCACHEPREFIX` absent, avec `-B` : rien n'est créé. Le `src/__pycache__` laissé par un `verifier` sans `-B` est toléré. Aucune voie trouvée par laquelle une décision qui change le verdict retenu dépendrait d'un résultat lu. Les points à corriger restants sont des règles inapplicables ou circulaires : moment de la dernière poussée, contrôle des chemins sans suite, contrôle final après un re-clonage, noms neufs absents de la définition de la conduite au § 4. Essais faits dans /tmp/claude-0 avec le .venv du dépôt, depuis supprimés.

### 1. bloquant — l. 221-225 (retour perdu) ; l. 168 (vérification des listes)

**Constat.** La commande prescrite, `python -m controle_ia.scellement verifier <sortie>`, n'a ni `PYTHONPATH` ni interpréteur du dépôt. Jouée telle quelle, depuis la racine ou d'ailleurs, elle rend `ModuleNotFoundError: No module named 'controle_ia'` (démontré ; `python` est ici l'interpréteur système /usr/local/bin/python). Le texte dit alors : « si `verifier` ne rend pas « OK », l'absence de sortie scellée est constatée ». Sur le chemin réel du retour perdu (une ligne perdue est déjà arrivée à la répétition v2), une erreur de lancement vaut donc constat irréversible d'absence, et le run passe en « pas de verdict » alors que la sortie est scellée et intacte. Même défaut, moins grave, pour la vérification des listes (l. 168) : on ne sait pas si un `verifier` qui ne démarre pas vaut « liste non scellée ». Sans `-B`, ce même appel peut aussi écrire des `.pyc` dans le `PYTHONPYCACHEPREFIX` s'il est passé, qui cesse alors d'être « vide ».

**Correction proposée.** L. 221-225, remplacer « la session joue `python -m controle_ia.scellement verifier <sortie>`, qui doit rendre « OK » (il n'imprime que les 12 premiers chiffres), » par « la session joue `PYTHONPATH=<racine>/src <racine>/.venv/bin/python -B -P -m controle_ia.scellement verifier <sortie>` (chemins absolus), qui doit rendre une ligne « OK … » (il n'imprime que les 12 premiers chiffres), ». Remplacer « si `verifier` ne rend pas « OK », l'absence de sortie scellée est constatée. » par « si `verifier` rend « ARRÊT : … » (sortie ou compagnon absent, illisible ou discordant), l'absence de sortie scellée est constatée ; un `verifier` qui ne démarre pas (interpréteur ou module introuvable) ne constate rien : il est rejoué, corrigé dans ses seuls chemins et variables, et c'est rapporté. ». L. 168, remplacer « elle vérifie chaque liste par `scellement verifier`, » par « elle vérifie chaque liste par la même commande `verifier` (un `verifier` qui ne démarre pas est rejoué de même, et ne vaut pas « liste non scellée »), ».

### 2. à corriger — l. 166-167 et 172-174 (moment de l'attendu, liste absente)

**Constat.** (a) « qu'après avoir récupéré cette dernière poussée » désigne la poussée prévue, celle qui porte la liste. Or la fonction `pousser` du poste v12 peut échouer après quatre essais (« poussée en échec », l. 84) : cette poussée n'arrive alors jamais, et, lue à la lettre, la règle interdit pour toujours tout `--calculer-attendu`, y compris celui de `lecture-assemblee-v1`. (b) Sans marque de fin, la liste est dite absente « quand la session constate la clôture ». Mais la recréation doit précéder `--calculer-attendu`, qui précède la note de clôture : la condition est circulaire. (c) Après une reprise, l'instance peut être légitimement « remise à l'arrêt et gardée (nœud) » (lanceur_v21, C-2) : « instance détruite constatée » peut alors ne jamais arriver.

**Correction proposée.** L. 166-167, remplacer « La session ne joue un assemblage ni un `--calculer-attendu` qu'après avoir récupéré cette dernière poussée, poste arrêté et instance détruite constatés. » par « La session ne joue un assemblage ni un `--calculer-attendu` qu'après avoir récupéré la branche une fois constatés, pour chacun de ces postes, son arrêt (marque de fin sur la branche, ou machine détruite par la session) et la destruction de son instance de calcul (ou sa mise à l'arrêt gardée, consignée) ; la dernière poussée d'un poste est alors la dernière de ses poussées qui soit sur la branche. ». L. 172-174, remplacer « Une liste est absente si elle n'est pas sur la branche quand la marque de fin du poste y est, ou, sans marque de fin, quand la session constate la clôture : » par « Une liste est absente si elle n'est pas sur la branche à cette récupération : ».

### 3. à corriger — l. 196-200 (même arbre, réinstallation, contrôle injouable) ; l. 192-193 (interdit d'installer)

**Constat.** Le texte ajoute « et le contrôle final » à la liste des gestes joués « dans le même arbre principal, sans re-clonage ». La correction proposée par la v9 (constat 6) ne le faisait pas. Le contrôle final a lieu après les lecteurs (24 h, plus 24 h, plus un remplacement), donc probablement dans une autre session. Le cas que vise la réinstallation (« faute de l'interpréteur du dépôt » : le `.venv` est dans l'arbre) est justement celui d'un arbre recloné. Un exécutant à la lettre conclut « contrôle injouable = écart », donc « pas de verdict » pour les deux runs. Pourtant `--controler` ne lit pas le dossier : il ne compare que la chaîne résolue du chemin, l'attendu et l'empreinte de la sortie. Il rend donc « conforme » dans un clone au même chemin absolu. Par ailleurs, l'interdit des l. 192-193 (« aucune session n'installe … jusqu'au dernier contrôle final ») ne nomme pas cette exception. Enfin, `requirements-cpu.txt` comprend torch et transformers (plusieurs gigaoctets), alors que `--controler` n'importe que numpy. Une réinstallation complète peut échouer, faute de disque (2 Go libres ici), et le run tombe alors en « écart » pour une raison mécanique.

**Correction proposée.** L. 196-200, remplacer « Le calcul des attendus, l'essai factice, la note de clôture, chaque commande sur un dossier réel et le contrôle final sont joués dans le même arbre principal, sans re-clonage ; si `--controler` ne peut être joué faute de l'interpréteur du dépôt, la session réinstalle `requirements-cpu.txt` pour lui seul, sans toucher à `src/`, et c'est rapporté ; un contrôle qui ne peut être joué vaut « écart ». » par « Le calcul des attendus, l'essai factice, la note de clôture et chaque commande sur un dossier réel sont joués dans le même arbre principal, sans re-clonage. Le contrôle final peut l'être dans un arbre recloné au même chemin absolu (`--controler` ne lit pas le dossier), après récupération par git de chaque sortie, de son compagnon et de son attendu, vérifiés par `scellement verifier`. Si `<racine>/.venv/bin/python` manque, la session y installe la seule distribution que `--controler` importe (`numpy==2.4.6`, version de `requirements-cpu.txt`), sans toucher à `src/`, et c'est rapporté. Un contrôle qui ne peut être joué ainsi vaut « écart ». ». L. 192, après « aucune session n'installe ni ne retire de distribution », ajouter « (hors l'installation permise ci-dessous pour le seul contrôle final) ».

### 4. à corriger — l. 189-191 (contrôle des chemins)

**Constat.** La vérification par programme se fait « avant la première lecture », donc après l'écriture des attendus et de l'essai factice, et aucune suite n'est prévue si elle échoue. Exemple : l'attendu A2 écrit sous le dossier D1 de l'autre verdict. La vérification le voit, mais D1 est déjà modifié, ce qui donnera « refus : empreintes ». Retirer A2 est interdit (« ne crée ni ne modifie de fichier sous un dossier donné à une lecture »). La session reste sans règle. La vérification ne couvre pas non plus le dossier factice, son attendu et sa sortie, ni la note de clôture, que la même phrase interdit pourtant sous un dossier lu.

**Correction proposée.** Remplacer « avant la première lecture, la session vérifie par programme (chemins résolus, `is_relative_to`) qu'aucun chemin d'attendu, de sortie ni de `PYTHONPYCACHEPREFIX` nommé par la note de clôture n'est sous `<racine>/src` ni sous aucun des dossiers donnés à une lecture, et la note le cite » par « avant le premier `--calculer-attendu`, la session fixe ces chemins et vérifie par programme (chemins résolus, `Path.resolve().is_relative_to`) qu'aucun chemin d'attendu, de sortie, de `PYTHONPYCACHEPREFIX`, du dossier factice, de son attendu et de sa sortie, ni de la note de clôture n'est sous `<racine>/src` ni sous aucun des dossiers donnés à une lecture ; un chemin qui échoue est remplacé avant toute écriture ; la note de clôture cite la vérification et ses chemins ».

### 5. à corriger — l. 350-351 (§ 4, conduite v15) contre § 6, étape 2

**Constat.** Le § 6, étape 2, demande des « noms neufs … de la sortie de la conduite » et des « sorties et PID du lancement, bilan ». Ces noms sont fixés dans la conduite, qui refuse une sortie non neuve (`lanceur_v21`, l. 1654-1655, `self.sortie`) ; le poste v12 lit `lancement-v13.pid`, que la conduite écrit. Or l'égalité du § 4 pour la conduite (« = `lancer-conduite-v13.py` sans `relance_seule`, avec `lanceur_v21`, `t_max_pilote_s=1800`, aucune instance antérieure, le manifeste v7 et le GO neuf ») ne permet pas ce changement. Seule la ligne du poste a été complétée. Le lecteur des pièces ne sait pas s'il doit refuser le changement de nom dans la conduite.

**Correction proposée.** L. 351, remplacer « aucune instance antérieure, le manifeste v7 et le GO neuf ; » par « aucune instance antérieure, le manifeste v7, le GO neuf et des noms neufs pour sa sortie et pour chaque fichier qu'elle écrit (R12 ; § 6, étape 2) ; ».

### 6. remarque — l. 164-165 (commande find)

**Constat.** `-empty` ne liste que les répertoires vides sur le poste. Un répertoire qui ne contient que des fichiers que git ne porte pas (motifs de .gitignore : `__pycache__/`, `*.pyc`, `build/`, `donnees/`…) n'est pas vide sur le poste, n'est pas listé, et manque dans l'arbre principal : l'existence que `valider` teste diffère. Ce cas demande un nom de répertoire peu probable dans une sortie. Lister tous les répertoires ferme ce cas sans autre règle, puisqu'une entrée déjà présente est laissée telle quelle. Par ailleurs, la commande de scellement de la liste sur le poste n'est pas fixée : `sha256sum <chemin absolu>` écrit le chemin entier dans le compagnon, que `lire_compagnon` refuse (« nom … au lieu de … »). Toute la liste serait alors écartée.

**Correction proposée.** Remplacer « `cd <dossier> && find . -mindepth 1 -type d -empty -printf '%P\n' | LC_ALL=C sort > <BASE>/repertoires-vides-<nom du dossier>-v1.txt` ; il la scelle, » par « `cd <dossier> && find . -mindepth 1 -type d -printf '%P\n' | LC_ALL=C sort > <BASE>/repertoires-vides-<nom du dossier>-v1.txt` (tous les répertoires : ceux que git porte existent déjà et sont laissés tels quels) ; il la scelle par `python -m controle_ia.scellement sceller <chemin absolu de la liste>`, ».

### 7. remarque — l. 165 (nom de la liste) ; dossier de reprise

**Constat.** Le dossier de reprise est `<sortie>/reprise-v10/` (lanceur_v21, sous-commande `reprendre`). Son nom de base est le même d'une tentative à l'autre. La liste `<BASE>/repertoires-vides-reprise-v10-v1.txt` d'une reprise de la seconde tentative heurterait donc celle de la première (R12). De plus, ce nom ne dit pas sous quel dossier la recréer. La collision demande deux reprises.

**Correction proposée.** Remplacer « `<BASE>/repertoires-vides-<nom du dossier>-v1.txt` » par « `<BASE>/repertoires-vides-<chemin du dossier relatif à <BASE>, chaque « / » remplacé par « -- »>-v1.txt` » et, l. 168, « crée sous le dossier qu'elle nomme » par « crée sous le dossier que nomme la liste ».

### 8. remarque — l. 182-183 (commande consignée)

**Constat.** Dans le gabarit de la commande, les accents graves intérieurs (`src/`, `-B`) coupent le bloc de code en trois : le texte qui doit être copié « tel quel » n'est plus d'un seul tenant au rendu.

**Correction proposée.** Remplacer « `PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<répertoire absent ou vide, hors de `src/` et des dossiers lus ; avec `-B` rien n'y est écrit, le même sert à toutes les exécutions> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 …` » par « `PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<P> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 …`, où `<P>` est un répertoire absent ou vide, hors de `src/` et des dossiers lus, le même pour toutes les exécutions (avec `-B`, rien n'y est écrit) ».
