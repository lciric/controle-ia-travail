# Contre-lecture, tour 1, de l'addendum de relance de l'idée 1.1 (brouillon 1) — v1

- **Pièce relue** : `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon1.md`
  (`009d8bbf5acd5c5ff48b6adcf5cca3e2232d33a94f6e69ebc2facec105148ee1`, égale à son compagnon ; `scellement verifier` : OK).
- **Lecteur** : modèle C, lecteur neuf (R2) ; je n'ai écrit ni la pièce, ni [T], ni [AE], ni le code, ni l'étape 0. Rédacteur : modèle A.
- **Dates (UTC, `date -u`)** : 2026-11-16, de 20:28:53Z à 20:33Z. Dépôt : `main`, tête `a6bc9938`, celle que cite la pièce.
- **Lu** : la pièce en entier (808 lignes) ; [AE] §§ 5 et 6 et les lignes citées ; [T] l. 603-624, 655-662 et les lignes citées ; l'addendum de
  relance de l'idée 1.2 (§ 4 et § 5) et les rapports de ses tours 1 et 2 (titres) ; `scripts/jouer_idee_1_1_v5.py` l. 50-170 ;
  `execution_idee_1_1_v5.py` l. 28-60, 100-160, 205-254, 335-351 ; `banc_idee_1_1_v2.py` l. 95-120, 1102-1125 et recherches ;
  `etape0_idee_1_1_v5.py` (recherches des clés) ; `registres/decisions.md` R-2988, R-3000, R-3010 (par clé) ; `registres/go.md` l. 342 et 348.
- **Non fait** : aucun fichier du run invalide ouvert (leurs octets ne passent que par `sha256sum` dans le programme de l'annexe) ; rien écrit dans
  `/home/user/jeu-idee-1-1-copie-v1` ; ni jeu, ni `pytest`, ni calcul lourd, ni réseau, ni clone ; aucun `env`.
- **Verdict : « corrections »** — 0 majeure, 4 mineures (4 couples exigés), plus des remarques facultatives. **La conception n'est pas en cause.**

## 1. Résultat des sept points

1. **Cause et qualification « run invalide » : conformes.** [AE] l. 392-400 nomme « conteneur repris », « machine arrêtée », « processus tué » et
   dit « rend le run invalide, sans aucune lecture » ; [T] l. 620 donne la relance « seulement sous un texte ou un addendum neuf ». R-3010 (l. 2970)
   dit bien : reprise vers 20:11Z, PID 12750, parti à 17:17:27Z, dernière écriture 20:10:49Z, sans `arret.json`, fichiers non ouverts. La pièce
   écrit « ≈ 2 h 36 min de jeu depuis le départ » là où R-3010 écrit « ≈ 2 h 53 » : les deux sont exacts (17:34:28Z contre 17:17:27Z, les
   contrôles d'avant jeu y comptant ou non) ; la pièce dit pourquoi le nom porte 17:34:28 (§ 2). La limite de la preuve (§ 2, point 3 : l'état
   sur disque ne distingue pas la reprise d'une autre cause dans les 18 secondes) est honnête, et la phrase « aucun arrêt par une garde n'est
   consigné » est la forme correcte (leçon du tour 1 de l'idée 1.2).
2. **Preuves : confirmées par rejeu.** Programme (lignes 589-807) et sortie (lignes 373-583) extraits de la pièce : empreintes
   `b9664f768a67…` et `f457df14c95f…`, égales à celles que la pièce déclare. Programme rejoué par moi à 20:29:08Z-20:29:11Z
   (`python3 -I -B`, 2,5 s, sortie d'erreur vide) : sortie identique à la recopie, aux trois seules lignes d'heure près (début, fin, `/proc/uptime`).
   Chiffres confirmés : 234 fichiers (109 tranches, 6 journaux, manifeste, `depart.json`, tous avec compagnon), 117 compagnons sur 117
   conformes, 0 sans compagnon, `sortie.json` et `arret.json` absents, liste triée `ff75355f…`, manifeste `d56d4114…`, `depart.json`
   `bc278be6…`, 46 sur 46 sur les trois arbres, bloc des 46 lignes `f1f1eb41…`, `git status` de la copie : 234 lignes non suivies, `.git`
   de la copie toujours à 17:34:28,389Z après mon rejeu (`GIT_OPTIONAL_LOCKS=0` : rien écrit). `ps -p 12750` : aucun processus. Les trois
   empreintes de code du § 8 (`c116a4bf…`, `8542a484…`, `c3d77494…`) sont exactes et égales à `main`. [T], [AE], [R12], `decisions.md`
   (`17f8672b…`, aussi égal à l'objet de `main`) et `go.md` (`55d4d2cb…`) : empreintes exactes. Les 32 lignes citées de [T] et [AE] (annexe A, [7])
   sont bien celles du texte. Aucun fichier du run n'est ouvert par le programme au-delà de `sha256sum`.
3. **« Mêmes tirages » : confirmé par le code, avec deux précisions (corrections c-1 et c-3).** Racine `int(EMPREINTE_PREREG, 16)` (banc l. 47, 123-126),
   générateurs `default_rng(SeedSequence(entropy=racine, spawn_key=clé))` (l. 129-132), clés `(i_ligne, r, 0|1)` (l. 478, 481, 636) ;
   `jouer_repetition(V, racine, i, r, reductions=…)` : rien d'autre ; nom du run formé après les essais (lanceur l. 145), jamais passé à une
   graine ; PID, heure et commit absents du banc. Dans le banc, les seuls ensembles (`set`, `frozenset`, `actifs_pour`) ne servent
   qu'à tester l'appartenance, donc l'ordre d'itération des chaînes (aléa de hachage de Python, qu'`-I` laisse actif) n'y entre pas. Précisions :
   (a) la clé de l'essai d'égalité E0 `(98, r)` manque à l'énumération du § 4.2 alors que [T] l. 492 et `etape0_idee_1_1_v5.py` l. 174 la donnent ;
   (b) chaque enregistrement de répétition porte aussi ses temps de calcul (`rec["temps_s"]`, banc l. 694), ce qui rend la liste de ce qui
   diffère d'un run à l'autre (§ 4.2 dernier alinéa, et § 3 dernière puce) incomplète : les tranches ne portent pas « les mêmes répétitions »
   à l'octet, seulement aux temps près.
4. **Conditions de la relance : complètes et exactes**, hors c-1 à c-4. Copie neuve et commit noté (4.4, avec `sha256sum -c` du compagnon), versions
   (4.2, commande rejouée : `3.13.18 2.4.6 1.17.1`), espace (4.4 ; 7,44 Go libres vérifiés à 20:30Z), PID (4.5), commande (4.6, interpréteur
   nommé par son chemin : nécessaire, la copie n'a pas de `.venv`), borne de 48 heures comptée depuis `depart.json` du run neuf (4.7 ; lanceur
   l. 154-155, `execution_idee_1_1_v5.py` l. 32, 139, 218 : vérifié), tous les contrôles d'avant jeu rejoués (le départ neuf passe par les
   essais, les mutations, les essais d'égalité : lanceur l. 137-144). Refus d'un départ neuf dans la copie du run invalide, deux fois
   (arbre non propre, l. 113 ; sorties existantes, l. 137) : exact. **Branche `--reprendre` non refusée par le code** : exact (`exiger_depot_propre_sauf_run`
   ne tolère que les deux dossiers du run, qui contiennent les 234 fichiers ; `executer` ne refuse qu'un `arret.json` ou une `sortie.json`,
   absents, et saute les tranches écrites, l. 214-221) ; la pièce fait bien de l'interdiction une règle écrite (AE l. 392-400 et 4.4).
5. **Consigne de tâche active et seconde interruption : conformes** à [R12] § 5, avec le constat nouveau et vrai que la consigne tenue n'a
   pas évité la reprise (R-3010) ; limites déclarées ; l'ajout « après une seconde interruption, le lieu revient au mot de Lazar » est cohérent
   avec 4.10.
6. **Valable pour les deux lieux sans rien changer d'autre : oui, sous c-4.** Lecture de [T] confirmée : l. 629 « toute dépense, instance payante,
   appel réseau ou appel de modèle | interdit (R-2851) » et l. 660 « Aucune machine louée » ; R-2851 : « sur processeur, sans dépense ». Une
   machine louée est donc bien un écart de lettre, nœud de Lazar en plus du devis et du GO ; la pièce ne l'accepte pas, ce qui est juste. Le nom
   « D7 » n'entre en collision avec rien dans l'idée 1.1 ([AE] : D1 à D5, D6 évité). Ce que la pièce ne dit pas : que sans ce mot rien ne part sur
   une machine louée (c-4).
7. **Format et hygiène : conformes.** Aucune ligne de la pièce n'a la forme `^[0-9a-f]{64}  \S+\s*$` (expression de `execution_v1.py` l. 106 :
   0 ligne) ni ne commence par 64 caractères hexadécimaux (0) ; aucun identifiant de modèle (recherche de Claude, Opus, Sonnet, Fable, Haiku, GPT :
   rien) ; lettres A, C seulement. À recompter sur la copie sous `prereg/` (la pièce le dit, § 7 point 4).

## 2. Corrections exigées (toutes mineures)

Chaque « ancien » figure une seule fois dans la pièce (vérifié par `grep -cF`).

**c-1 — § 4.2, dernier alinéa : les temps de calcul de chaque répétition diffèrent aussi.**

- ancien : `manifeste et sa durée (`execution_idee_1_1_v5.py` l. 150-151), `sortie.json` les durées et le journal.`
- nouveau : `manifeste et sa durée (`execution_idee_1_1_v5.py` l. 150-151), et chaque répétition ses temps de calcul (`temps_s`, `banc_idee_1_1_v2.py` l. 694) ; `sortie.json` porte les durées et le journal.`

**c-2 — § 3, dernière puce : « durées » précisées, pour ne pas laisser croire à des tranches identiques à l'octet.**

- ancien : `hors du nom du run, de l'empreinte du manifeste et des durées, une tranche du`
- nouveau : `hors du nom du run, de l'empreinte du manifeste et des durées (celle de la tranche et les `temps_s` de chaque répétition), une tranche du`

**c-3 — § 4.2, première puce : la clé `(98, r)` de l'essai d'égalité E0 manque.**

- ancien : `` `(97, k, …)` et `(99, b)` pour les essais, mutations et rééchantillonnages ``
- nouveau : `` `(98, r, 0)` et `(98, r, 1)` pour l'essai d'égalité E0 ([T] l. 492 ; `etape0_idee_1_1_v5.py` l. 174), `(97, k, …)` et `(99, b)` pour les essais, mutations et rééchantillonnages ``

**c-4 — § 4.10, lieu (ii) : écrire que sans le mot de Lazar rien ne part sur une machine louée, et où ce mot se consigne.** Sans cette phrase,
« valable pour les deux lieux » laisse croire que le scellement de l'addendum suffit pour (ii).

- ancien : `ce lieu serait retenu. Aucun appel réseau`
- nouveau : `ce lieu serait retenu. **Sans le mot de Lazar sur D7, consigné à `registres/go.md` (comme D5, GO-2026-11-16-07), aucune machine louée ne part sous cet addendum.** Aucun appel réseau`

## 3. Remarques facultatives (la pièce peut être scellée sans)

- **f-1 — « par élimination » (§ 4.2).** L'argument porte sur « les sept interpréteurs relevés » ; il tient (le lanceur exige numpy, scipy via le juge, et
  pytest ; seul `.venv` les porte), mais une formule « parmi les sept relevés, seul… » serait plus exacte que « le run invalide l'a employé ».
- **f-2 — Disque (§ 4.4).** Le « ≈ 2,90 Go hors `.git` » ne dit pas ce que coûte `.git`. Mesuré par moi (`du`, noms et tailles seulement) : `.git` de la copie
  du run invalide = 2,77 Go, mais ses paquets sont en liens durs (compte de liens 3 à 8), donc un clone local sur le même disque ne les recopie pas. Si
  l'opérateur copiait sans liens, le libre tomberait à ≈ 1,8 Go avant la sortie (≈ 1,5 Go après) : le seuil de 1 Go tient encore, de justesse. Une phrase
  « un clone local sur le même disque lie les objets ; sinon, compter 2,8 Go de plus » éviterait la surprise.
- **f-3 — Aléa de hachage de Python.** Non traité par la pièce ; `-I` ne fixe pas `PYTHONHASHSEED`. Je n'ai trouvé aucune itération sur un ensemble de
  chaînes dans le banc (§ 1 point 3) ; le code du juge n'a pas été lu en entier. Les essais d'égalité et de rejeu de l'étape 0 sont, de toute façon, des
  contrôles d'égalité de résultats entre processus. À ajouter si la mère veut la garantie complète.
- **f-4 — Charge de la machine.** [R12] 4.10 décrivait la charge partagée ; la pièce n'en parle pas. Sans effet sur les tirages ni sur la borne de 48 heures
  (D = 15,667 h, marge triple), mais l'état vivant montre d'autres jeux et la course de B bis (R-3010 : machine distante) : une ligne « la charge ne change
  ni graine ni borne » suffirait.

## 4. Points pour la mère

1. **Écart à un texte scellé, mot du directeur nécessaire pour le lieu (ii).** Une machine louée est un écart de lettre à [T] l. 629 et 660 (« Aucune machine
   louée »), en plus du devis et du GO. La question à Lazar (R-3010) doit le dire en toutes lettres (écart D7), sinon son « go » sur la dépense ne couvrira pas
   l'écart. Le lieu (i) n'en demande aucun.
2. **PID 4953 (idée 1.2, relance) : absent à 20:31Z** (`ps -p 4953`, aucun processus), alors que `registres/etat.md` le donne en cours depuis 14:09Z. À établir sur
   les noms, tailles et heures de sa sortie : fini, ou tué par la même reprise de 20:11Z. S'il a été tué, la règle de « seconde interruption » de son addendum
   joue (second addendum de relance, lieu à rendre à Lazar) ; la pièce de l'idée 1.1 n'en parle pas et n'a pas à en parler, mais le risque est le même.
3. **Risque du lieu (i) :** une reprise imposée malgré une tâche active a déjà eu lieu ; 15,7 h de jeu sur le conteneur s'y exposent à nouveau. La pièce le déclare et
   sa consigne ne l'exclut pas ; c'est le fond de la question de R-3010.
4. **`--reprendre` reste accepté par le code** dans la copie du run invalide ; seule la règle écrite l'interdit. L'opérateur ne doit jamais le passer.
5. **Égalité au bit près sur un autre processeur** : limite déclarée en 4.2, sans effet sur la validité ; elle peut peser, à la marge, pour le lieu (ii) (le processeur
   du run invalide n'est pas relevé).
6. **Suite** : après application de c-1 à c-4, un tour 2 par un lecteur neuf ; à la recopie sous `prereg/`, recompter les lignes au format du lanceur (attendu 0) et
   recalculer les empreintes du § 8.
7. Ligne à ajouter à la section de contre-lecture : mon tour (modèle C, lecture entière du brouillon 1, ce rapport, son empreinte, verdict « corrections »,
   0 majeure, 4 mineures) ; lettre inscrite par toi.

## 5. Incidents et gestes de ma main

- Aucun incident. Gestes : `sha256sum` et `scellement verifier` de la pièce ; extraction du programme et de la sortie de la pièce ; rejeu du programme de l'annexe
  (`python3 -I -B`, sorties dans le bloc-notes de la session) ; lectures de code et de registres listées plus haut ; `ps -p 12750` et `ps -p 4953` ; `du -sb` sur les
  deux dossiers `.git` et `stat -c '%h %s'` sur trois paquets de la copie du run invalide (liens, tailles : aucun contenu lu) ; `df`. Aucun `pytest`, aucun
  jeu, aucun appel réseau, aucun clone ; rien écrit hors de ce rapport et du bloc-notes ; aucun git avec `GIT_DIR`, `GIT_WORK_TREE` ou `GIT_INDEX_FILE` ; aucun commit.
