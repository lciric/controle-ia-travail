# Contre-lecture du programme d'enchaînement de la lecture de la discrétion, bras A, version 1 — version 1

Contre-lecture de code (classe B), par un agent neuf (Claude Sonnet 5.5), le 22 novembre 2026, sur processeur seul, sans réseau, sans commit.
Objet : `src/controle_ia/organismes_discrets/enchainement_discretion_bras_a_v1.py` (`c2f452d9714333f823da36cf9d8d6c04d94b909682c862097baca8b21ddc84e3`, vérifiée), `tests/test_enchainement_discretion_bras_a_v1.py` (`f5c800d2c8d4b5db95f8f2a137087c08062bb3082b4b5f557162d05d17f131b8`, vérifiée), note `code-enchainement-discretion-bras-a-v1-note.md`.
Texte de référence : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md` — 8.7, ligne « programme d'enchaînement » de 13.2, 6.3 (m) et (n), 6.9 (dont conventions et « Panne pendant une lecture »), 6.10, 8.4, 8.5.
Cloisonnement tenu : aucun fichier interdit ouvert ; les sorties synthétiques ne sont lues que par les essais eux-mêmes (extraction du commit `82cfd8ba`).
L'arrêt actuel de l'étape (n) (code 6) est connu et n'est pas relevé. Une version 2 est en cours.

## Verdict : à corriger

Rien de bloquant en dehors de l'arrêt de l'étape (n), connu. L'ordre des étapes, le versement avant tout rendu, le commit du seul dossier de course, le poussage vérifié sur le distant et les arrêts versés suivent le texte. Mais **trois défauts majeurs** (commande citée fausse ; entrée de l'enchaînement ni versée ni liée d'une exécution à l'autre ; livraison refusée non versée) et plusieurs écarts mineurs sont à corriger avant l'épreuve de forme de bout en bout, qui est la pièce que le contre-lecteur du manifeste de course confrontera à l'arbre versé.

## Ce qui a été rejoué

- Les 30 essais : 30 réussis (22 s), sur le fichier et l'essai aux empreintes ci-dessus.
- La garde statique de la version 13 sur le dépôt, jouée à part : aucune violation (16 s). **La réserve 1 de la note est périmée** : le faux positif de `scripts/chef_essais_admission_bras_a_v2.py` a été levé par le commit `5d6bc4380`.
- Empreintes des neuf modules joués, comparées à celles de 13.1 : toutes égales (`a7ebf29f…`, `ae656289…`, `fa915de2…`, `8373851e…`, `cc632df3…`, `db0aa22f…`, `381878cd…`, `7a1e6aab…`, `20b78a8a…`) ; programme du constat v5 `fd5fddcd…` égal.
- Quatre essais à moi, dans le bloc-notes (non versés, aucun fichier du dépôt touché) : contrôle malsain au rejeu ; second passage après un succès complet ; entrée changée entre l'étape (m) et l'étape (n) ; clé en double dans l'entrée ; plus la lecture de la couverture des essais par instrumentation de lignes.

## Conformité, point par point

| point | constat |
|---|---|
| constat de lancement par la commande du programme, jamais à la main (conventions) | conforme (ligne 270 à 297) ; mode de constat sans constat existant, mode de contrôle sinon ; huit champs exigés ; code 2 : garde ordinaire ; malsain : sa ligne rendue, rien ne part |
| contrôle malsain avant un rejeu : le rejeu ne part pas | **conforme, vérifié par moi** (une ligne neuve citant l'empreinte de la configuration après une panne : « contrôle malsain », aucune trace de rejeu, aucun fichier de l'étape (m), contrôle versé) ; **mais aucun essai ne le couvre** (défaut D7) |
| ordre : entrée, garde statique, versement d'ouverture, constat, versement, étape (m), versement, étape (n), versement | conforme ; le constat part juste avant la lecture, après les gardes lentes ; l'étape (n) seule et la reprise de l'étape (n) avec acte existant sont sans constat, ce que 6.9 et la ligne « le rejeu de l'étape (n) interrompue, sans contrôle : rejoué » de 8.4 écrivent |
| versement avant tout rendu | conforme : `del` du résultat, `verser`, puis seulement la relecture du fichier scellé pour le déclencheur ; distant qui refuse : `EchecDuVersement`, rien de rendu, (n) non partie ; relancé, le versement d'ouverture pousse d'abord |
| commit du dossier de course entier et de lui seul, poussage, vérification sur le distant | conforme (lignes 161 à 184), y compris fichier ignoré, reste non versé, `push` ou `commit` sans effet |
| arrêts versés avant d'être rendus ; exception rendue sans cause ni contexte ; erreur inattendue par son type | conforme (lignes 380 à 401) ; l'exception levée hors du bloc qui l'attrape |
| aucune relecture après succès | conforme : un second passage est refusé par l'analyse (« l'étape (n) a abouti… n'est pas rejouée »), versé |
| déterminisme | conforme : deux courses neuves à horloge et dates git fixées rendent mêmes pièces, empreintes et commits ; rien d'aléatoire dans le programme |
| aucun repli silencieux | **quatre exceptions** : D5, D6, D8, D9 ci-dessous |
| cas sain et artefact par garde (R5) | **incomplet** : D7 |

## Défauts

### Majeurs

**D1 — La commande citée au compte rendu est fausse (lignes 515 et 521).**
`["python", "-m", __name__, *argv]` : sous `python -m …`, `__name__` vaut `"__main__"` (vérifié). Le compte rendu cite donc `python -m __main__ …`, alors que 8.7 exige que le manifeste de course cite « la commande et l'empreinte de chaque programme joué » et s'appuie sur elle pour borner la limite qui reste (« la lecture ne se lance que par l'enchaînement, dont le manifeste de course cite la commande »). L'essai ne le voit pas : il appelle `main` en l'important (`__name__` y est le nom du module) et ne compare que la queue `cr["commande"][3:] == argv`.
Correction : écrire le nom du module en constante (`MODULE = "controle_ia.organismes_discrets.enchainement_discretion_bras_a_v1"`), citer `sys.executable` (ou le dire « python » et consigner la version), et faire comparer l'essai à la liste entière, en lançant en plus la commande par `subprocess` sur un cas court (constat malsain, code 5) pour éprouver le chemin `-m`.

**D2 — L'entrée de l'enchaînement n'est ni versée ni liée d'une exécution à l'autre (lignes 195 à 251, 355 à 366, 435 à 436, 467 à 469).**
Deux faces du même défaut.
(a) *Aucune liaison.* L'entrée décide les lignes de la table C (états de la base, coût apparié, lignes de la table B) à l'étape (m), puis l'état de la base, les comptes désappariés, les seize tâches et l'entropie des vingt aires à l'étape (n), mais elle est relue à chaque exécution, et rien ne vérifie que c'est la même. **Essai à moi** : étape (m) jouée avec « la base ne détecte pas », l'étape (n) s'arrête (lecteur absent), puis rejouée avec une autre entrée (« détecte », autre entropie) : elle aboutit sans un mot ; le fichier des grandeurs écrit « détecte » aux quatre doses, la table C scellée de l'étape (m) porte les lignes C4 obtenues avec l'autre entrée. Le constat de l'étape (m) ne garde que le journal, le renvoi et les effectifs, non les états de la base ni les lignes de la table B. Le scénario n'est pas rare : c'est la reprise normale après l'arrêt de l'étape (n) actuel, après un poussage en échec, ou après une panne.
(b) *Non versée.* L'empreinte de l'entrée est dans le compte rendu (`cr["entree"]`), mais le fichier est exigé hors du dossier de course (règle « non écrite » n° 3) : le contre-lecteur du manifeste, qui « confronte chaque ligne à l'arbre versé et à son historique » (8.7), n'a rien à confronter, et personne ne peut vérifier que les lignes de la table C découlent des états de la base annoncés. De plus, l'entropie et les seize tâches doublent ce que porte la configuration du bras scellée (6.3 (a) ; 13.2) sans recoupement.
Correction : (1) avant l'étape (m), sceller dans le dossier de course une pièce `entree-de-l-enchainement-<rang>.sha256` (ou une copie de l'entrée, si Lazar juge que ses lignes de la table B ne gênent pas le cloisonnement du côté habilité : question à lui poser, 8.7 ligne « table B ») versée avec le premier versement d'ouverture ; (2) à chaque exécution suivante, refuser toute entrée dont l'empreinte diffère de la pièce versée (garde ordinaire) ; (3) recouper entropie et tâches avec la configuration quand elle les porte, sinon le dire dans la note ; (4) essais : entrée changée entre (m) et (n), cas sain et artefact.

**D3 — La livraison refusée n'est pas versée par l'enchaînement (lignes 348 à 351 et 398 à 401).**
6.9 (« Ce qui vaut pour tout arrêt »), la ligne « issue d'un arrêt » de 8.4 et 8.5 disent que la livraison refusée est « versée et scellée sans être relue » ; la note écrit « tout arrêt est versé avant d'être rendu ». Or la sortie de la lecture commune est exigée hors du dossier de course (essai : `RegleNonEcrite` si elle est dessous) et `verser` ne prend que le dossier de course : sur un arrêt, seul le fichier d'arrêt part ; la pièce refusée, dont le fichier d'arrêt cite l'empreinte, n'est versée par personne, et le compte rendu ne le dit pas. La destruction d'une pièce refusée avant versement serait invisible (8.7, deuxième ligne).
Correction : soit verser la sortie refusée dans le dossier de course (un sous-dossier dédié, hors du dossier des arrêts, à autoriser expressément : cela change la règle n° 3 pour la seule sortie, que le texte dit versée), soit consigner dans le compte rendu et dans la note, noir sur blanc, que le versement de la livraison refusée (8.5, `diag/…`) reste une garde de procédure tenue par la session, avec sa trace, et l'ajouter à la liste de ce que le contre-lecteur du manifeste vérifie. À trancher par Lazar si le texte doit être précisé.

**D4 — La liste des « règles que le texte n'écrit pas » est inexacte pour deux des trois (note ; lignes 344 à 351).**
- Règle n° 1 (étape (n) contre la garde statique) : **vraiment non écrite** — 13.2 fait jouer l'étape (n) par l'enchaînement, 6.9 et 8.4 réservent la lecture du fichier des unités au seul programme de l'aire conditionnelle, et rien ne dit comment les deux se concilient. Exacte.
- Règle n° 2 (dossier des arrêts hors du dossier de course) : **écrite**. 8.7 (troisième ligne) range « dossier des arrêts » dans « le dossier de course entier » versé, et la première ligne donne « un seul dossier des arrêts » au dossier de course. Le refus est donc une application de 8.7, non une règle neuve ; il se range en garde ordinaire (code 4), non « règle non écrite » (code 6).
- Règle n° 3 (pièce d'entrée sous le dossier de course) : **partiellement écrite**. Pour le fichier des unités, 8.4 (« fichier rangé dans le dossier des arrêts ou sous lui : refusé ») et 13.2 (« les outils de version n'en prennent que l'empreinte ») disent déjà qu'il ne se verse pas par son contenu ; le refus est conforme, mais il est écrit. Pour la sortie de la lecture commune, le texte dit au contraire qu'une livraison refusée est versée (D3) : la règle n° 3 la contredit. Pour l'entrée de l'enchaînement, elle est vraiment non écrite (D2).
Correction : reclasser dans la note et dans le code (type d'exception et code de sortie), citer le passage qui fonde chaque refus.

### Mineurs

**D5 — Le déclencheur « au moins une dose en C6 » disparaît du compte rendu après une reprise de l'étape (n) seule (lignes 446 à 449, 395 à 396).**
Il n'est calculé que dans la branche qui joue l'étape (m). Après un poussage en échec (essai : « versement refait avant l'étape (n) »), l'exécution suivante joue l'étape (n) seule et rend un compte rendu sans la clé : absence silencieuse, alors que 6.3 (m) fait suivre la table C du déclencheur puis de l'audit de symétrie (ligne A11). Correction : le recalculer du fichier scellé de l'étape (m) dans toutes les branches (la fonction existe), ou écrire explicitement `"non recalculé"`.

**D6 — Une clé en double dans l'entrée est acceptée en silence (ligne 200).**
`json.loads` garde la dernière valeur ; essai à moi : `"renvoi_de_la_base"` écrit deux fois, la dernière (« vérifié ») est retenue. Le texte tient une clé en double pour une pièce illisible (6.9) et l'analyse a un `_sans_doublon`. Correction : `object_pairs_hook` qui refuse tout doublon, à tous les niveaux ; essai.

**D7 — Gardes sans cas sain et artefact (R5).**
Relevé par instrumentation des lignes jouées par les 30 essais ; instructions jamais exécutées : lignes 142 (git absent ou délai dépassé), 149 à 156 (dossier de course hors de tout dépôt), 202 (entrée illisible), 207, 211, 220, 225, 228, 231, 235 (cinq formes de l'entrée et les deux premières gardes des actions désappariées), 293 à 295 (programme du constat dont la sortie n'est pas une ligne à huit champs), 453 (reprise de l'étape (n) sans sortie d'origine — le titre de l'essai la dit couverte, son corps ne la joue pas), 464 (fichier des unités non donné), et dans `main` les chemins de sortie 0, 4 et 7 (lignes 512 à 513, 519 à 523). Aussi sans essai : le contrôle malsain au rejeu (comportement juste, voir plus haut), l'entrée sans doublon (D6), le registre courant, le registre figé et la sortie d'origine rangés sous le dossier de course (seuls trois des six noms de `_exiger_hors_du_dossier_de_course` sont éprouvés), `commit_du_registre_courant` vide. La campagne de mutations (37 sur 38) n'a donc pas touché ces gardes. Correction : un essai sain et un artefact par garde, avec l'essai de la commande réelle pour les codes 0, 4 et 7.

**D8 — Erreurs avant la première étape, ou après la dernière, rendues en trace brute (lignes 364, 394 à 396, 400).**
Hors du bloc qui attrape : `_sha256(sortie)` (essai à moi : `--sortie` inexistante, `FileNotFoundError` non attrapée, pas de code de sortie du jeu 0 à 8), `compte_des_livraisons` après le succès de l'étape (n), `_pieces_du_dossier_de_course` sur le chemin d'arrêt. Une exception à ces endroits sort d'`enchainer` après des versements, sans compte rendu et sans code. Aucune valeur de la livraison n'y passe (trace sans variables), mais la règle « aucun repli silencieux » veut un code défini. Correction : envelopper en `GardeArret` les lectures de pièces d'entrée ; pour la fin, attraper et rendre par son type, versement fait.

**D9 — `motif = str(x)` d'une garde ordinaire rend le message de l'analyse tel quel (lignes 388 à 389).**
6.9 : le programme qui refuse ne rend « jamais un nombre de la livraison ». Les gardes de forme passent par `ArretDeLaLecture…` (constat seul), mais certains messages de l'analyse gardent une valeur (`holm`, ligne 352 de l'analyse : « valeur p {p!r} … hors de [0, 1] »). Je n'ai pas montré qu'un chemin de la livraison y arrive ; le risque est que le texte du message passe au compte rendu. Correction : rendre, pour une garde ordinaire issue de la lecture, le type et le nom de la garde seuls, ou prouver par essai que les messages de la liste n'emportent aucune valeur.

**D10 — Citations et réglages non vérifiés.**
`commit_du_registre_courant` est donné au constat sans être confronté au dépôt (le texte laisse à la session de s'assurer que le registre était le dernier : limite écrite, mais le compte rendu ne dit pas « non vérifié ») ; `"python"` en dur dans la commande citée ; poussage de `HEAD` (réserve 5 de la note, juste). Correction : le dire dans le compte rendu.

**D11 — La note est périmée ou en écart sur deux points.**
(a) Réserve 1 : la violation de la garde statique n'existe plus (commit `5d6bc4380`) ; le texte « la commande réelle s'arrête avant tout constat (code 4) » est faux aujourd'hui. (b) 13.2 écrit le programme « écrit par le rédacteur du code de la relance, Claude Fable 5.2 ; contre-lu par un agent neuf d'un autre modèle, Claude Opus 5.5 » ; la note dit qu'il a été écrit par Opus 5.5, et la présente contre-lecture est faite par Sonnet 5.5, ni l'un ni l'autre des modèles que la ligne désigne. Écart de procédure à porter à Lazar (nœud : écart au texte), ou à régler par la version 2 en changeant la ligne de 13.2.

## Forme de l'entrée : cohérence avec 8.7 et 13.2

- 13.2 ne dit rien d'une entrée ; 8.7 ne la range ni parmi les pièces du dossier de course ni parmi celles du manifeste. Les onze clés sont donc un choix du développeur, déclaré, et comme tel acceptable ; elle est placée du côté de l'instance d'analyse, ce qui ne heurte pas la ligne de 8.4 sur la liste des épisodes retenus (« jamais transmise au lanceur de l'étape de discrétion ou du module des moniteurs »).
- Trois des onze clés doublent ou précèdent des pièces que le texte place ailleurs : journal de la table A et réglages (aussi écrits aux constats de l'étape (m), qui les rejouent : bien), états de la base et table B (dérivés d'étapes que le texte confie au lanceur et à la base : provenance non vérifiable, réserve 4 de la note), entropie et seize tâches (à lire de la configuration du bras). Voir D2.
- Les clés `journal…` et `renvoi…` sont recontrôlées par l'analyse via les constats de l'étape (m), mais **non** les états de la base, le coût et les comptes désappariés.

## Fait à la lettre

Étape (m) : règle de discrétion, garde de sortie, table C aux seules doses en B8, fichier de l'étape (m) et constats, déclencheur après le poussage (6.3 (m) ; 7.6). Étape (n) : aires conditionnelles tirées par l'analyse, état de la base écrit comme en 7.5 aux quatre doses ; les aires des cinq moniteurs à la dose ¼ et hors de B8 sont recomposées par l'analyse de la pièce, non données par l'appelant (6.3 (n)). Reprise de l'étape (n) : confrontation des vingt lectures, acte versé avant la lecture du fichier des unités. Rejeu par étape : respecté (trace de rejeu, contrôle sain exigé, étape (n) seule après (m) scellé).

## Ordre de correction proposé

D1, D2 et D3 d'abord (le manifeste de course les confrontera) ; puis D5, D6, D8 ; puis D7 (les essais de ce qui précède) ; D4, D9, D10, D11 à régler avec la version 2.
