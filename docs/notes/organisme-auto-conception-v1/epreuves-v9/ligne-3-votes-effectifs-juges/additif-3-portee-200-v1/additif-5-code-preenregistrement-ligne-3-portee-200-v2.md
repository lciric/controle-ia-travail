# Additif 5 (additif de code) au préenregistrement de la ligne 3 (version 7) — commit et empreintes du code de la mesure « portée à 200 », racines autorisées, commandes de lancement — v2

**Statut : version 2, non scellée. À contre-lire par un autre modèle, puis à sceller par la mère avant tout calcul de la mesure « portée à 200 », chronométrage compris.** Écrit le 2026-11-20 (temps universel, `date -u` : 11:15Z à l'heure relevée), sur le mandat `mandat-redacteur-additif-5-code-racines-portee-200-v1.md` (`8a669690ac1c43b46d0c6bae9b02ce208783a9bd2b397b557de0ca7399d0d291`, égale à son compagnon). Version 2, même jour : elle porte à la lettre les corrections 1 à 6 de la contre-lecture `contre-lecture-additif-5-code-portee-200-v1.md` (`df30acc99ddadd29563edd61204e1f86a29e105616bc87bc0e0aac87ad69e84c`) sur la version 1 (`d1b237d602d68b488510ff0ba94f9519481984554ae6627807ce43f1a1c4233d`), au § 2, au § 4, au § 5, au titre et à cette ligne ; rien d'autre ne change.

C'est le second additif, court, que l'additif 3 demande (§ 5, point 4 ; § 7, point de procédure pour la mère) : « La pièce qui autorise est l'additif de code de cette mesure, court, qui ne fait que nommer le code (commit, empreinte de chaque fichier, commandes du point 8 complétées), scellé par la mère après la contre-lecture du code. » **Il ne fait que nommer le code.**

- « l'additif 3 » : `prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md`, lu en entier sur `origin/main` par `git show`, empreinte recalculée `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807`, égale à son compagnon.
- « l'additif 2 » : `prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md`, lu de la même façon, `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`, égale à son compagnon ; son § 6 est le modèle de forme.
- Accord de Lazar : GO-2026-11-20-26, cité à la lettre par l'additif 3 ; échéance **2026-11-30**. Je n'ai pas relu le registre.
- Dossier de la ligne (noté LIGNE) : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/` ; chemin absolu sur la machine de l'exécution : `/home/user/controle-ia-travail/` devant.

## 1. Ce que cet additif fait, et ce qu'il ne fait pas

- Il porte le dossier et le commit du code de la mesure, l'empreinte de chacun de ses fichiers, les racines de graines qu'il autorise, les deux commandes de lancement complétées, l'interpréteur, et la règle « dossier du code commité entièrement ».
- **Il ne change aucune règle, aucun seuil, aucune prédiction, aucune lecture, aucune hypothèse, aucune racine, aucun montant.** Tout le reste est l'additif 3. Là où cet additif se tait, le texte et ses additifs valent seuls ; là où il semblerait les contredire, ils priment et le point revient à la mère.
- **Aucun résultat n'a été lu** (règle R1) : aucun calcul de la mesure n'existe. Je n'ai lancé ni le banc, ni le chronométrage, ni un essai ; je n'ai dérivé aucune graine. Je n'ai ouvert aucune mesure de l'étage 1, ni ses dossiers d'exécution et de verdict. Je n'ai fait que lire et prendre des empreintes.
- Il ne porte aucune revendication. Rien ici ne touche l'étage 2, dont le code suivra son propre additif.

## 2. Le code : dossier, commit, empreintes

**Dossier du code : `LIGNE/code-portee-200-v4/`.**

**Commit de son versement : `af19ff8dbb0e1c990f7bb97f7e5a77a332dca14c`**, branche `lot/compte-organisme-v1` (lu par `git rev-parse`).

**Chemin et commit de lancement.** La mesure est lancée depuis ce dossier tel que la mère le recopie sur `main` au scellement, au même chemin, **à empreintes égales à la table ci-dessous**. Commit de `main` qui porte le dossier : **à écrire par la mère au scellement** (je ne peux pas le connaître). C'est le commit du versement du dossier sur `main`, fait avant que ce blanc soit écrit, donc avant le commit qui scelle cet additif ; c'est le seul blanc de cet additif. L'identité du code tient aux empreintes de la table et, à l'exécution, à `programme_sha256` ; non à la tête du dépôt, qui aura pu avancer.

Toutes les empreintes sont recalculées par moi sur disque, fichier par fichier ; chacune est égale à son compagnon `.sha256` du dossier et à celle du rapport du développeur. Pour chacun des quatorze fichiers, l'identifiant git du fichier sur disque (`git hash-object`) est égal à celui du commit `af19ff8d` (`git rev-parse af19ff8d:chemin`) : le disque et le commit portent les mêmes octets.

### 2.1 Les deux programmes que la mesure exécute

| rôle | fichier | sha256 |
|---|---|---|
| banc, mode « portée à 200 » (la mesure) | `banc_juges_scriptes_ligne_3_v4.py` | `79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7` |
| chronométrage (n'imprime que des durées) | `chronometrer_portee_200_ligne_3_v1.py` | `6b9d2cbfd9bbf638d30c0d314531de510d85a4a2b28c8da40100ec8c7be51b90` |

### 2.2 Essais, contrôle des défauts réintroduits, différentiels

| rôle | fichier | sha256 |
|---|---|---|
| essais | `essais_banc_juges_scriptes_ligne_3_v4.py` | `9b9141912f70c3296f1a90e201c7bef04c58d3b9e2837ebef47becc96a49a0e7` |
| contrôle des défauts réintroduits | `controle_defauts_reintroduits_ligne_3_v4.py` | `8e33404baa66a38f000922e054993e4641e65eb833773a0d14965061dfbffb81` |
| rapport des défauts, mode « visé » | `rapport-defauts-reintroduits-ligne-3-v4.json` | `85cec7ec5493c9dc11dc0d7b6c5ff701145d126997c7a0d07458ccb4ff5b4e9c` |
| rapport des défauts, mode « complet » | `rapport-defauts-reintroduits-fichier-entier-ligne-3-v4.json` | `261775ac578cf15f1adc1988f65b91763c4afe3f1bfc2dab58a8f6febe61fd26` |
| différentiel du banc, v3 → v4 | `differentiels-v3-v4/banc-v3-v4.diff` | `746974ccbae0f4585ac5011be62d559a9267a09a14b871f1a869560b71fb9a4e` |
| différentiel des essais | `differentiels-v3-v4/essais-v3-v4.diff` | `13e25b37c9970654123182f3ff3e05e8c5156a64bf783f7c240c0a2f2e16dfea` |
| différentiel du contrôle | `differentiels-v3-v4/controle-v3-v4.diff` | `7fb14d5d6bdc38dd2a6272e45689555491e30281ad968f7e40c9956d03c6158d` |
| différentiel du chronométrage (v3 → portée v1) | `differentiels-v3-v4/chronometrage-v3-portee-200-v1.diff` | `34fc9a2eb7cecb29214c55e88dbc92337f04a5f1669dcab526a0b4bf426b0f13` |

### 2.3 Copies sans changement du code v3 (preuve d'égalité ; jamais lancées par la mesure)

| fichier | sha256 |
|---|---|
| `banc_juges_scriptes_ligne_3_v3.py` | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` |
| `chronometrer_banc_ligne_3_v3.py` | `8cb61afbdc6948197b756028d08df665725a2d3f99681c1e21c89b96eba5fa7e` |
| `essais_banc_juges_scriptes_ligne_3_v3.py` | `28ad0e8987790ec5a7bef61076606598604903e006f36c27a8a6e778dd0a3f77` |
| `controle_defauts_reintroduits_ligne_3_v3.py` | `b4078e715fdacc0ff6831d67921d315e28d8189c911ab000daa2fc33421bf654` |

Ces quatre empreintes sont égales à celles de l'additif 2, § 3.1 et § 3.2.

Chacun des quatorze fichiers a son compagnon `.sha256` dans le dossier (quatorze contrôles « OK »). Je n'ai lancé aucune commande de liste : je n'ai pas vérifié que le dossier ne contient rien d'autre que ces quatorze fichiers et leurs compagnons (§ 6).

### 2.4 Rapport et contre-lecture du code

| pièce | fichier (sous `LIGNE/additif-3-portee-200-v1/`) | sha256 |
|---|---|---|
| rapport du développeur (modèle O) | `rapport-developpeur-banc-v4-portee-200-v1.md` | `117b768697de68e768cc4f2b463f50abb0abbf189a6dc59e2e6083ac9a078090` |
| contre-lecture, « Conforme » (modèle S) | `contre-lecture-banc-v4-portee-200-v1.md` | `ab19b31a1597f471b1ac057dbe92638bf29dd1a422c83af26ffe3dc6f613d2fd` |

Décomptes, d'après ces deux pièces, non rejoués par moi : 157 essais passés sur 157 ; 138 défauts réintroduits vus sur 138 (mode « visé » rejoué par le contre-lecteur) ; verdict « Conforme », aucune correction exigée.

## 3. Racines de graines autorisées, et elles seules

| rôle | racine | clé (table gelée du banc) | dérivation |
|---|---|---|---|
| chronométrage de la mesure (n'imprime que des durées) | **2026112031** | `monde_de_puissance` : 2 ; `reechantillonnage_monde_de_puissance` : 12 | `.spawn(210)` pour chaque clé |
| tirages décisifs de la mesure | **2026112032** | `monde_de_puissance` : 2 | `.spawn(210)` |
| rééchantillonnage de la mesure | **2026112033** | `reechantillonnage_monde_de_puissance` : 12 | `.spawn(210)` |

Ce sont les racines de l'additif 3, § 2 ; aucune ne change. **Toutes les autres racines sont refusées** : 2026111931 à 2026111937 (étage 1 et étage 2), avec ou sans autorisation ; toute autre clé, tout autre nombre d'enfants. La racine des essais, 2026111930, reste la seule dérivable sans autorisation ; elle ne sert à aucune des deux commandes du § 4.

**L'autorisation est cet additif, une fois scellé par la mère : son chemin scellé et l'empreinte de son compagnon.** Avant ce scellement, aucune des trois racines n'est dérivée. Limite, dite comme à l'additif 2, § 4 : le code contrôle que le fichier donné a l'empreinte donnée, il ne lit pas son contenu ; c'est la mère qui donne le chemin et l'empreinte scellés, et qui compare ensuite le champ `autorisation` du manifeste à ce qu'elle a scellé.

## 4. Les deux commandes de lancement, complétées

Gabarit de l'additif 3, § 5. Ordre : **le chronométrage d'abord, la mesure ensuite, une fois chacun**, avant l'échéance de GO-2026-11-20-26 (**2026-11-30**) ; passé cette date, rien ne part sans ligne neuve. Processeur seul : aucun appel de modèle, aucune dépense.

Valeurs :

- `DOSSIER_DU_CODE` = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-portee-200-v4`
- `CHEMIN` = `/home/user/controle-ia-travail/prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md` — le chemin **absolu** de cet additif scellé (un chemin relatif serait ouvert depuis le dossier du code).
- `HEX` = l'empreinte sha256 de cet additif scellé, celle de son compagnon, **qui n'est pas écrite ici** : un fichier ne porte pas sa propre empreinte. La mère la lit dans le compagnon scellé et la porte dans les deux commandes au lancement, sans rien écrire dans ce fichier.
- `DOSSIER` = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/chronometrage`
- `DOSSIER_NEUF` = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/mesure`

**Chronométrage** (racine 2026112031) :

```
env -C DOSSIER_DU_CODE -u BANC_LIGNE_3_CHEMIN -u CHRONOMETRAGE_LIGNE_3_CHEMIN PYTHONDONTWRITEBYTECODE=1 python3 -B chronometrer_portee_200_ligne_3_v1.py --autorisation-additif CHEMIN --empreinte-additif HEX --manifeste DOSSIER
```

**Mesure** (racines 2026112032 et 2026112033) :

```
env -C DOSSIER_DU_CODE -u BANC_LIGNE_3_CHEMIN -u CHRONOMETRAGE_LIGNE_3_CHEMIN PYTHONDONTWRITEBYTECODE=1 python3 -B banc_juges_scriptes_ligne_3_v4.py --portee-200 --autorisation-additif CHEMIN --empreinte-additif HEX --sortie DOSSIER_NEUF
```

- **Aucun autre argument** : ni `--essai`, ni `--repliques-echantillon`, ni `--tirages-essai` au chronométrage. La configuration de la mesure est une constante du banc (`CONFIGURATION_PORTEE_200`) qu'aucun argument ne change.
- **`DOSSIER` et `DOSSIER_NEUF` n'existent pas encore et sont hors du dossier du code** ; une exécution par dossier ; chaque programme refuse un dossier déjà présent et crée lui-même le dossier et ses parents. Leur parent `execution-portee-200-v1/` était absent du disque à 11:15Z (contrôle par `stat` sur ce seul chemin) ; ce nom n'est pas celui du dossier d'exécution de l'étage 1.
- **`PYTHONDONTWRITEBYTECODE=1`** et `-B` : rien ne s'écrit dans le dossier du code.
- **`BANC_LIGNE_3_CHEMIN` et `CHRONOMETRAGE_LIGNE_3_CHEMIN` ne sont pas posées** : les deux `-u` les retirent de l'environnement du lancement, ce qui est la même condition dite dans la commande ; le code refuse de toute façon si l'une est posée. Les `-u` sont un ajout à la lettre des commandes du développeur, déclaré.
- Sorties : `DOSSIER/manifeste-chronometrage-portee-200-ligne-3-v1.json` ; `DOSSIER_NEUF/resultat-portee-200-ligne-3-v1.json` et `DOSSIER_NEUF/manifeste-portee-200-ligne-3-v1.json`, chacun avec son compagnon. Avant toute lecture du résultat, la mère fait sur le seul manifeste le contrôle de l'additif 3, § 6 (« Aucune lecture avant le manifeste contrôlé par la mère »), avec : `programme_sha256` égal à `79865552…` du § 2.1 ; `programme_chronometrage_sha256` égal à `6b9d2cbf…` ; `autorisation` égale à `CHEMIN` et `HEX`.

## 5. L'interpréteur et la version de numpy

**Interpréteur retenu : `python3`**, soit `/usr/local/bin/python3` sur cette machine (`command -v python3`), Python 3.13.18 (`python3 --version`) ; **numpy 2.5.3**, version relevée par le contre-lecteur du code sous cet interpréteur, que je n'ai pas relevée moi-même. **Non retenu** : le Python de l'environnement du dépôt (`/home/user/controle-ia-travail/.venv/bin/python`, numpy 2.4.6), qui a servi aux essais du développeur.

Raisons :

1. c'est la lettre du gabarit scellé de l'additif 3, § 5 (`python3 -B …`), et de l'additif 2, § 6 ;
2. les 157 essais passent sous les deux interpréteurs (contre-lecture, § 3) : aucun des deux n'est écarté par un essai ;
3. l'additif 2, § 6, donne 2.5.3 comme la version de numpy relevée par le contre-lecteur dans l'environnement des essais et de la vérification du code de l'étage 1, non comme celle de l'exécution de l'étage 1 ; si l'étage 1 a tourné sous ce même interpréteur, le garder écarte une différence de version de numpy entre la mesure à 100 et la mesure à 200, que l'audit de symétrie de l'additif 3 compare cellule par cellule. Je n'ai pas lu le manifeste de l'étage 1 (règle d'aveugle) : sa version de numpy est à relire sur ce manifeste par l'agent qui prononce.

Le manifeste de chaque exécution consigne `versions.python`, `versions.numpy` et `versions.executable` ; la mère les compare à ce paragraphe au contrôle du manifeste.

**Remarque, non une règle.** L'additif 3 fixe `python3` par son gabarit et numpy ≥ 1.25 par son § 2 ; il n'impose aucune version précise de numpy. Cet additif nomme la version attendue ; il ne dit pas ce que vaut une exécution dont le manifeste en porterait une autre : ce cas revient à la mère, avant toute lecture des mesures (additif 3, § 6 : tout écart après scellement est un nœud).

## 6. Le dossier du code, commité entièrement avant le lancement

1. **Avant le lancement, tous les fichiers de `LIGNE/code-portee-200-v4/` sont suivis par git et commités, et rien d'autre ne s'y trouve** : programmes, essais, contrôle, rapports de défauts, différentiels, copies du v3, compagnons. La garde « dossier du code propre » (additif 3, § 5, point 6) est dure : le banc et le chronométrage refusent de tourner, sans dériver aucune graine, si `git status --porcelain` borné au dossier du code rend quelque chose, si le dossier est hors d'un dépôt, si le dossier de sortie est sous le dossier du code ou lui est égal, ou si le dossier du code contient `archives-reponses-modeles/`.
2. **Réserve de la contre-lecture, reprise telle quelle : un fichier ignoré par `.gitignore` passe la garde** (`git status --porcelain` ne le montre pas). Aucun fichier du dossier du code ne doit être ignoré sans que la mère le sache ; l'identité du code tient à `programme_sha256`. Je n'ai lancé aucune commande de liste ni lu `.gitignore` : ce contrôle est à la mère, au moment où elle recopie le dossier sur `main`.
3. Le chronométrage écrit son manifeste dans `DOSSIER` avant la mesure : `DOSSIER` étant hors du dossier du code, la garde de la mesure n'en est pas touchée.

## 7. Rien d'autre

Aucune règle, aucun seuil, aucune prédiction, aucune lecture ne change. La mesure, sa règle de lecture, ses gardes, l'exécution unique, la faute du banc, l'audit de symétrie, le verdict par un agent neuf et sa contre-lecture sont ceux de l'additif 3 (§ 1, § 3, § 6), sans un mot de plus ici. Ce qui reste à la mère par la contre-lecture du code (§ 4, points 7 et 8 : comparaison de `d`, a, b à l'étage 1 par l'agent qui prononce ; interruption écrite par la mère) n'est pas changé.

## 8. Réserves propres à cet additif

1. Je n'ai rien rejoué : les décomptes d'essais et de défauts sont ceux du développeur et du contre-lecteur. Mon contrôle porte sur les empreintes, sur l'égalité du disque et du commit `af19ff8d`, et sur une recherche bornée à chacun des deux programmes du § 2.1 (arguments de la ligne de commande, création du dossier de sortie, variables de chemin, champ `versions` du manifeste). Je n'ai pas relu le reste du code.
2. La version de numpy sous `python3` (2.5.3) est celle que la contre-lecture relève ; je ne l'ai pas relevée.
3. La garde des racines repose sur une empreinte donnée en argument (§ 3, limite).
4. Les deux dossiers de sortie du § 4 sont placés par moi, sous LIGNE ; ni l'additif 3 ni le mandat ne fixent leur lieu, hors « absents, hors du dossier du code ».

## 9. Pièces lues

| pièce | sha256 | lecture |
|---|---|---|
| mandat du rédacteur | `8a669690ac1c43b46d0c6bae9b02ce208783a9bd2b397b557de0ca7399d0d291` | en entier |
| additif 3, version 3 (`origin/main`, `git show`) | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` | en entier |
| additif 2, version 3 (`origin/main`, `git show`) | `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a` | en entier |
| rapport du développeur | `117b768697de68e768cc4f2b463f50abb0abbf189a6dc59e2e6083ac9a078090` | en entier |
| contre-lecture du code | `ab19b31a1597f471b1ac057dbe92638bf29dd1a422c83af26ffe3dc6f613d2fd` | en entier |
| `banc_juges_scriptes_ligne_3_v4.py` | `79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7` | lignes rendues par une recherche bornée à ce fichier (réserve 1) |
| `chronometrer_portee_200_ligne_3_v1.py` | `6b9d2cbfd9bbf638d30c0d314531de510d85a4a2b28c8da40100ec8c7be51b90` | de même |

Les autres fichiers du § 2 n'ont pas été ouverts : empreintes seules. Non lus : toute mesure de l'étage 1, son verdict, ses dossiers d'exécution et de verdict ; rien sous `archives-reponses-modeles/`. Aucun programme lancé, aucune graine dérivée, aucun appel de modèle, aucune dépense, aucune écriture dans le dépôt.

**Remarque pour la mère.** Le nom de ce fichier et son rang « 5 » sont ceux du mandat, à confirmer : s'ils changent, `CHEMIN` (§ 4) et le titre changent avec eux, par une version neuve contre-lue, avant le scellement.

Rédacteur neuf, modèle F.
