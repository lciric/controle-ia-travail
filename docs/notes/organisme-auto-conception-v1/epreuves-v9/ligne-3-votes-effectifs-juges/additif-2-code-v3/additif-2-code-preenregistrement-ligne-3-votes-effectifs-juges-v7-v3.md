# Additif 2 (additif de code) au préenregistrement de la ligne 3 (version 7) — commit et empreintes du code d'analyse de l'étage 1, commande de lancement, racines autorisées — v3

**Statut : version 3, non scellée. À sceller par la mère avant tout calcul de l'étage 1, chronométrage compris.** Écrit le 2026-11-20 (temps universel, `date -u` : 05:21Z à la première heure relevée), sur le mandat `code-etage-1-v3/mandat-redacteur-additif-de-code-ligne-3-v1.md` (`65f9873ca725df1cdfb2aeb69807c66cfcfb613b80f987662efb0791361fdf38`, égale à son compagnon). Version 2, même jour : elle porte à la lettre les corrections A, B et C de la contre-lecture `contre-lecture-additif-2-code-ligne-3-v1.md` (`7cf5a2c99e678ab0c3a3580121ac1d2be388cfcbf22fc959958cd3ec2546fc41`) sur la version 1 (`656094057c4ea3ebdd08049883531180be1f91572600b03d0a8738734ee330ae`), au § 6 et au § 7 ; hors le numéro de version (titre, ligne de statut), rien d'autre ne change. Version 3, même jour : elle porte à la lettre les corrections 1 et 2 du contrôle `controle-differentiel-additif-2-code-v1-v2-v1.md` (`97f51ce83649aade410ca0c586e651caf853da6164e99cbc211824e0538ae6e3`) sur la version 2 (`186501571b1e6cf03e3abff1991a987f86ed591a0bda00864e3df77f851c0ce5`), à cette ligne de statut et au § 9 ; hors le numéro de version (titre, ligne de statut) et cette phrase, rien d'autre ne change.

C'est l'« additif de code » que le texte prévoit (en-tête, « Commit du code d'analyse » ; « Graines (règle R9), ordre des gestes », geste 3) et que l'additif 1 attend (« Ordre des gestes, complété »). **Il ne fait que nommer le code.**

- Texte complété, non réécrit : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, lu sur main par `git show` après `git fetch origin main` (tête `40b16f8a8a23af3dba48319d4137f4cb972631c7`), empreinte recalculée `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`. Dans la suite : « le texte ».
- Additif 1, scellé, non réécrit : `prereg/organisme-auto-conception-v9/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md`, lu de la même façon, empreinte recalculée `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` ; commit de main qui le porte : `4bbd36765af028012221114b33fb7d39f9786c00` (2026-11-20T04:50:07Z). La clé ADDITIF-1-ORGANISME-V9-LIGNE-3 et le numéro de registre R-4081 sont repris du mandat ; je n'ai pas relu le registre.
- Dossier de la ligne (noté LIGNE) : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.

## 1. Ce que cet additif fait, et ce qu'il ne fait pas

- Il porte le commit du code d'analyse de l'étage 1, l'empreinte de chacun de ses fichiers, la commande de lancement, les racines de graines qu'il autorise, la règle de lancement et ce que l'étage 1 rend.
- **Il ne change aucune hypothèse, aucune prédiction, aucun seuil, aucun critère de lecture gelé, aucune règle gelée, aucune racine, aucun montant.** Tout ce qui en changerait un est un nœud de Lazar. Là où cet additif se tait, le texte et l'additif 1 valent seuls ; là où il semblerait les contredire, ils priment et le point revient à la mère.
- **Aucun résultat n'a été lu** (règle R1) : aucun calcul de l'étage 1 n'existe. Je n'ai lancé ni le banc, ni le chronométrage, ni un essai, ni aucun programme ; je n'ai dérivé aucune graine. Je n'ai fait que lire et prendre des empreintes.
- Il ne porte aucune revendication. Rien ici ne touche l'étage 2, dont le code suivra son propre additif.
- Ce que ce résultat ne fera jamais reste entier : aucun mot de cet additif ne fait trancher une carte par un juge, scripté ou réel.

## 2. Commit du code d'analyse

**`380db35647746e2c1eae44a85d0f2969d19113b6`** (lu par `git rev-parse 380db356`), branche `lot/compte-organisme-v1`, 2026-11-20T03:46:24Z. Il est ancêtre de la tête de cette branche à l'heure d'écriture (`15cbb24f48874ff74e9927686adf655deba1980f` ; contrôle par `git merge-base --is-ancestor`).

Le code est sous `LIGNE/code-etage-1-v3/`. C'est le code v3 : le code v2 (`code-etage-1-v2/banc_juges_scriptes_ligne_3_v2.py`, `ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3`, recalculée), plus les deux ajouts que l'additif 1 demande (§ 5).

**La vérification du code v3 n'est pas dans ce commit**, et c'est normal : elle a été écrite après lui. Elle est portée par le commit `53689f0d18bd7f3e9202bbca34f0e777eaf9a236` de la même branche (2026-11-20T04:00:33Z). Verdict : « Conforme », aucune correction exigée.

## 3. Empreintes des fichiers du code v3

Toutes recalculées par moi sur disque, fichier par fichier, dans `LIGNE/code-etage-1-v3/`. Chacune est égale à celle du rapport du développeur (là où il donne une empreinte abrégée, les caractères donnés sont égaux). Pour chaque fichier du commit du code, l'identifiant git du fichier sur disque (`git hash-object`) est égal à celui du commit `380db356` (`git rev-parse 380db356:chemin`) : le disque et le commit portent les mêmes octets.

### 3.1 Les deux programmes que l'étage 1 exécute

| rôle | fichier | sha256 |
|---|---|---|
| banc (exécution décisive) | `banc_juges_scriptes_ligne_3_v3.py` | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` |
| chronométrage (n'imprime que des durées) | `chronometrer_banc_ligne_3_v3.py` | `8cb61afbdc6948197b756028d08df665725a2d3f99681c1e21c89b96eba5fa7e` |

### 3.2 Essais, contrôle des défauts réintroduits, preuve d'égalité

| rôle | fichier | sha256 |
|---|---|---|
| essais | `essais_banc_juges_scriptes_ligne_3_v3.py` | `28ad0e8987790ec5a7bef61076606598604903e006f36c27a8a6e778dd0a3f77` |
| contrôle des défauts réintroduits | `controle_defauts_reintroduits_ligne_3_v3.py` | `b4078e715fdacc0ff6831d67921d315e28d8189c911ab000daa2fc33421bf654` |
| comparaison des sorties v2 et v3 | `comparer_sorties_v2_v3_ligne_3_v1.py` | `4209748a9c8ac261cd53a4dab54c3415af9ff8c73372684548b2c6341309ea7a` |
| sortie de cette comparaison | `comparaison-sorties-v2-v3-ligne-3-v1.json` | `17ebe5557e8a1b81cb17cbc2b9922511a2363948ad7995c2a3ec8a2f5f5d44cd` |
| rapport des défauts, mode « visé » | `rapport-defauts-reintroduits-ligne-3-v3.json` | `343f0f779a13753666cd8f118e20b755ee49f055a2eeb2b21d945ec6e00c9ce7` |
| rapport des défauts, mode « complet » | `rapport-defauts-reintroduits-fichier-entier-ligne-3-v3.json` | `586e6f4561a918e0c4ea31917f6e07f8c086eb95f4943a6c3fe8c9be6f2d40fe` |

Décomptes, d'après le rapport du développeur et la vérification, non rejoués par moi : 115 essais passés sur 115 ; 93 défauts réintroduits vus sur 93, dans les deux modes ; sorties existantes du v2 égales à l'octet, sur la racine des essais seule.

### 3.3 Journaux de l'outil de remplacement et différentiels v2 → v3

| fichier | sha256 |
|---|---|
| `banc_juges_scriptes_ligne_3_v3.py.journal-remplacements-v1.json` | `5ef628f1c7a4c4952c75cccfa219cdce7aa8c28012c8567fb6db716d236de172` |
| `chronometrer_banc_ligne_3_v3.py.journal-remplacements-v1.json` | `4d3355ac869d65a4d42dd68bb61975edd2c12c074fcc9f4ba4af5f294384347b` |
| `essais_banc_juges_scriptes_ligne_3_v3.py.journal-remplacements-v1.json` | `2785e893895c9d4a0be37fd843ef7a1b90308aa0759b43c20095fb44c6d4d717` |
| `controle_defauts_reintroduits_ligne_3_v3.py.journal-remplacements-v1.json` | `28240b8f2ed0c89c3ffced332c3ca9662e17014d0017e61ed3a4273023736dd7` |
| `differentiels-v2-v3/banc-v2-v3.diff` | `d430702e374120c5eb1d55e32e9e0e7ff9df9db2b245bb04012348cc1d0e85ab` |
| `differentiels-v2-v3/essais-v2-v3.diff` | `a73d621b8678554672776944f2deb3bcc852e481d79b3cead430fbc31675583d` |
| `differentiels-v2-v3/chronometrage-v2-v3.diff` | `94dbf457501734d6de1ca2a1fcfb31b04c628ecfcfc76610b1bbacc8eefe012c` |
| `differentiels-v2-v3/controle-v2-v3.diff` | `98c781fb95e7734795b10429ef8264e897abb8d09345ed8decc1c5d08a86d662` |

### 3.4 Rapport et vérification

| pièce | fichier | sha256 | commit |
|---|---|---|---|
| rapport du développeur (modèle L′) | `rapport-developpeur-code-etage-1-ligne-3-v3.md` | `ae1fa1da825934ec2af942d2047825695804e526122e24038a7098a0f2ca9d9c` | `380db356…` |
| vérification, « Conforme » (modèle S) | `verification-code-etage-1-ligne-3-v3-v1.md` | `bd2773e29829ec9778aaaf2f3f4bb03796652f323f3bbb2c95e53ef24d6165f9` | `53689f0d…` |

### 3.5 Calcul de référence des essais (point H de l'additif 1)

Les essais se font contre la version 2 du calcul de référence, à la racine de LIGNE : `calcul_predictions_ligne_3_v2.py`, `802d4dd26d66ead35326cef2d77c8a55e12c11b89a4ddbce4d9a115927428dc6` ; sortie `calcul-predictions-ligne-3-v2.json`, `2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724`. Les deux sont recalculées et égales aux constantes que le fichier d'essais attend. L'exécution décisive ne lit ni l'un ni l'autre.

### 3.6 Écart de nom à l'annexe A du texte, déclaré

L'annexe A nomme les fichiers au suffixe `_v1` ; c'est un plan (additif 1, point H). Les noms réels sont ceux des tables ci-dessus, au suffixe `_v3` (règle R12). Les fichiers de sortie sont `resultat-etage-1-ligne-3-v3.json`, `manifeste-etage-1-ligne-3-v3.json` et `manifeste-chronometrage-ligne-3-v3.json`. C'est un écart de nom, sans effet sur ce qui est calculé ou lu.

## 4. Racines de graines autorisées, et ce qui les autorise

**Racine décisive : `2026111932`** (tirages de l'étage 1 décisif). Elle va avec **`2026111933`** (rééchantillonnage de l'étage 1), que la même exécution dérive. Le chronométrage, qui précède, dérive **`2026111931`**. Ce sont les racines du texte (« Graines (règle R9), ordre des gestes ») ; aucune ne change.

Ce qui les autorise :

1. **Le texte** : l'additif de code est « scellé par la mère avant tout tirage de l'étage 1 » (en-tête ; geste 3), puis l'étage 1 est joué sur processeur, une fois (geste 4).
2. **L'additif 1** : « l'autorisation des racines 2026111931 à 2026111933 est l'additif de code, par chemin et empreinte » (choix 18) ; ordre des gestes complété : additif de code scellé, chronométrage, puis l'étage 1, une fois.
3. **Le code** (`verifier_autorisation`, lue dans le banc) : il refuse de dériver ces trois racines sans une autorisation. L'autorisation est le chemin d'un fichier et une empreinte de 64 caractères ; le code calcule l'empreinte du fichier et refuse si elle diffère. L'autorisation est recopiée au manifeste de l'exécution.

**L'autorisation est donc cet additif, une fois scellé par la mère : son chemin scellé et l'empreinte de son compagnon.** Avant ce scellement, aucune de ces trois racines n'est dérivée.

Limite, dite : le code contrôle que le fichier donné a l'empreinte donnée ; il ne lit pas le contenu du fichier et ne peut pas savoir que c'est bien l'additif scellé. C'est la mère qui donne le chemin et l'empreinte scellés, et qui compare ensuite le champ `autorisation` du manifeste à ce qu'elle a scellé.

Racines jamais dérivées par ce code : `2026111934` à `2026111937` (étage 2), toujours refusées. La racine des essais, `2026111930`, est la seule dérivable sans autorisation ; d'après le rapport du développeur et la vérification, c'est la seule qui ait été dérivée à ce jour.

## 5. Les ajouts du code v3, nommés

Le code v3 porte les deux ajouts de l'additif 1 (« Ce que le code doit changer »), tous deux après les tirages, sur les tableaux déjà tirés :

1. **Silence 1**, par bras de l'alarme : la part (b), clé `part_des_suites_en_alarme_sur_changement_a_effet`, sa mention obligatoire, clé `mention_part_des_suites_en_alarme`, et les cinq comptes, clé `comptes_silence_1`. La part (a) garde son nom et sa valeur.
2. **Silence 2**, dans les critères mécaniques : l'aide `alarme_fcbf4a2dd1a57` (les deux clauses de P6 par m, avec leurs comptes ; le mot de P6 ; pour la carte, « mesurée, sans mot : aucune règle de mot gelée »). C'est une aide, jamais le verdict (règle R13).
3. **Une clé de plus, que l'additif 1 ne nomme pas : `comptes_du_melange_plante`.** La vérification demande que cet additif la nomme. Par cellule d'alarme, elle rend quatre entiers : suites qui changent, suites « à effet », suites « sans effet », suites sans changement. Ils sont lus sur les masques plantés, après les tirages ; ils ne viennent d'aucun tirage neuf.
   - *Son rôle.* Elle donne à l'aide de P6 ses dénominateurs : le nombre de suites sans changement pour la clause « fausse alarme », le nombre de suites « à effet » rapporté avec la clause « détection ». Sans elle, ces nombres seraient écrits en dur dans l'aide. Elle rend aussi lisible le mélange auquel renvoie la mention de la part (b).
   - *Ce qu'elle ne fait pas.* Elle n'entre dans aucun seuil, aucun mot de carte, aucune règle gelée. Elle ne change aucune mesure existante : la preuve d'égalité à l'octet la compte parmi les clés neuves déclarées.
   - *Valeurs attendues à la taille décisive*, par la règle D de l'additif 1 (2 000 suites) : 1 000, 500, 500 et 1 000. Une autre valeur serait une faute du banc, à rendre à la mère avant toute lecture.

Une remarque de la vérification est reportée telle quelle : l'aide de P6 ignore sans bruit une cellule dont m n'est ni 10, ni 20, ni 40. La configuration décisive ne joue que ces trois m, et un m manquant donne « incomplet ».

## 6. Commandes de lancement, sur processeur

Les deux commandes sont celles que le développeur a écrites en tête de chaque programme (« Usage »). **Le rapport du développeur de la version 3 ne les recopie pas** : il ne donne que la commande des essais. Je les prends donc dans le code même, aux empreintes du § 3.1 ; c'est un écart à la lettre du mandat, déclaré.

Ordre : le chronométrage d'abord, puis l'exécution décisive, une fois (texte, annexe A ; additif 1, point J).

**Chronométrage** (racine 2026111931) :

```
python3 -B chronometrer_banc_ligne_3_v3.py --autorisation-additif CHEMIN --empreinte-additif HEX --manifeste DOSSIER
```

**Étage 1 décisif** (racines 2026111932 et 2026111933) :

```
python3 -B banc_juges_scriptes_ligne_3_v3.py --decisif --autorisation-additif CHEMIN --empreinte-additif HEX --sortie DOSSIER_NEUF
```

- `CHEMIN` : le chemin **absolu** du fichier de cet additif scellé, tel qu'il existe sur la machine de l'exécution (le code ouvre le chemin par rapport au dossier courant, qui est le dossier du code ; un chemin relatif au dépôt serait refusé). La mère compare le champ `autorisation.chemin_additif` du manifeste à ce chemin et `autorisation.empreinte_additif` à `HEX`.
- `HEX` : l'empreinte sha256 de ce fichier scellé, celle de son compagnon. Un fichier ne peut pas porter sa propre empreinte : elle n'est pas écrite ici.
- `DOSSIER`, `DOSSIER_NEUF` : deux dossiers qui n'existent pas encore. Chaque programme refuse un dossier déjà présent : une exécution par dossier.
- Les commandes se lancent depuis le dossier du code (par exemple `env -C DOSSIER_DU_CODE …`). Les essais ont été joués avec `PYTHONDONTWRITEBYTECODE=1` et `python3 -B`, pour ne rien écrire dans ce dossier.
- Environnement des essais et de la vérification : Python 3.13.18 (c'est aussi ce que rend `python3 --version` sur ma machine), `numpy` et la bibliothèque standard, aucun réseau, aucun appel de modèle. Version de `numpy` relevée par le contre-lecteur : 2.5.3 ; le texte exige numpy ≥ 1.25 ; le manifeste de chaque exécution la consigne (`versions.numpy`), sans qu'une valeur précise soit imposée.

La configuration décisive est une constante du banc (`CONFIGURATION_DECISIVE`) : aucun argument ne la change. Son empreinte est écrite au manifeste.

## 7. Règle de lancement

1. **Le dossier d'où le banc est lancé ne contient pas `archives-reponses-modeles/`.** Le manifeste appelle `git rev-parse HEAD` et `git status --porcelain` bornés au dossier du fichier du banc (vérification, § 5). Lancé depuis `LIGNE/code-etage-1-v3/`, il ne lit l'état que des chemins sous ce dossier. **Ne jamais copier le banc dans un dossier qui contiendrait `archives-reponses-modeles/`**, ni à la racine du dépôt. Je n'ai lancé aucune commande de liste : je n'ai pas vérifié par moi-même ce que contient le dossier du code au-delà des fichiers nommés au § 3 ; aucune de ces pièces ne nomme un tel sous-dossier. **`DOSSIER` et `DOSSIER_NEUF` ne sont jamais placés sous le dossier du code** : le banc écrit son résultat avant son manifeste, et le manifeste du chronométrage resterait sous ce dossier ; dans les deux cas le champ `depot.dossier_du_code_propre` du manifeste de l'étage 1 vaudrait `false`.
2. **Le code lancé est celui du § 3.1.** Les variables d'environnement `BANC_LIGNE_3_CHEMIN` et `CHRONOMETRAGE_LIGNE_3_CHEMIN` ne sont pas posées : le chronométrage charge alors le banc qui est à côté de lui. Après chaque exécution, la mère compare `programme_sha256` du manifeste à `09bfe0db…` et, pour le chronométrage, `programme_chronometrage_sha256` à `8cb61afb…` ; un écart est une exécution nulle, rendue à la mère, sans lecture.
3. **Ce que le champ `depot` du manifeste dit, et ne dit pas.** Il porte la tête du dépôt à l'heure du lancement, qui ne sera pas le commit `380db356…` si la branche a avancé. L'identité du code tient à `programme_sha256`, non à ce champ. Le champ `depot.dossier_du_code_propre` vaut `true` si `git status --porcelain` borné au dossier du code ne rend rien ; la mère le lit à l'exécution : `false` ou `null` rend l'exécution suspecte et se rend à la mère, sans lecture des mesures ; l'identité du code tient toujours à `programme_sha256`.
4. **Une fois.** L'étage 1 est joué une fois. Une exécution interrompue avant d'avoir écrit son fichier de résultat n'a rien rendu : elle est relancée à l'identique, dans un dossier neuf, et l'interruption est écrite (additif 1, point J). Une exécution qui a écrit son résultat n'est jamais rejouée. Aucune relance après lecture, aucun changement de graine, de grille ou de tolérance (règle R3).
5. **Le chronométrage n'imprime que des durées.** La durée n'est ni un critère ni une garde d'arrêt (additif 1, point J).

## 8. Ce que l'étage 1 rend

Dans `DOSSIER_NEUF`, écrits une fois, chacun avec son compagnon `.sha256` :

- `resultat-etage-1-ligne-3-v3.json` : les mesures par cellule (`estimateur_et_agregation`, `monde_de_puissance`, `ecart_rho_prime_moins_rho`, `double_rendu`, `garde_de_cadrage`, `alarme`) et `criteres_mecaniques`, l'application mécanique des critères gelés par le code. **C'est une aide, jamais le verdict** : le verdict de l'étage 1 est prononcé par un agent neuf (règle R13 ; additif 1, point F), qui applique lui-même les critères gelés et l'additif 1 aux mesures, puis compare à l'aide ; tout désaccord est écrit et levé avant le scellement du verdict.
- `manifeste-etage-1-ligne-3-v3.json` (règle R9) : programme et empreinte, empreinte du texte, mode, autorisation, configuration et empreinte, versions, racines, table des clés, dérivations, tête du dépôt, heures, empreinte du résultat.

**Ce que l'étage 1 dit de la taille est rendu à la mère, avant toute demande de départ payant** (texte, geste 5). La règle gelée du nombre de témoins ne change pas : N = 100 si la tolérance tient à n = 100 aux treize cellules de la règle ; sinon, aucune dépense, et la table avec un devis à la taille voulue retournent à Lazar. L'aide du code sur ce point est sous `criteres_mecaniques.estimateur` (`tient_aux_cellules_de_la_regle_par_n`, `taille_retenue_par_la_regle`, `verdict_mecanique_estimateur`) ; elle porte aussi le cas « non prévu par la table gelée » de la règle E de l'additif 1. La puissance qui décide (règle gelée de portée) est sous `criteres_mecaniques.puissance`. L'étage 1 rend aussi à l'étage 2 ce que le texte liste à « Ce que l'étage 1 rend à l'étage 2 » ; rien n'y est ajouté ni retiré.

Aucun mot de ces sorties ne valide, n'écarte ni ne classe une carte.

## 9. Réserves propres à cet additif

1. Je n'ai rien rejoué : les décomptes d'essais et de défauts vus sont ceux du développeur et du vérificateur. Mon contrôle porte sur les empreintes, sur l'égalité du disque et du commit, et sur la lecture, dans le banc et dans le chronométrage, de l'en-tête, des constantes de graines, de `verifier_autorisation`, de `generateurs`, de `executer_etage_1`, de `criteres_estimateur`, de `criteres_alarme_p6`, de la fin de `cellule_alarme`, du manifeste et de `main`. Je n'ai pas relu le reste du code.
2. La garde des racines repose sur une empreinte donnée en argument (§ 4, limite).
3. Le lieu de dépôt des sorties n'est fixé ni par le texte ni par l'additif 1 ; cet additif ne le fixe pas (§ 7, point 1, pour les deux contraintes connues).

## 10. Pièces lues

| pièce | sha256 | lecture |
|---|---|---|
| mandat du rédacteur | `65f9873ca725df1cdfb2aeb69807c66cfcfb613b80f987662efb0791361fdf38` | en entier |
| texte, version 7 (main, `git show`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | de l'en-tête à « Hypothèse » ; bras « alarme », « Ce que l'étage 1 rend à l'étage 2 » et les deux règles gelées ; « Graines (règle R9), ordre des gestes » ; annexe A ; le reste non relu |
| additif 1, version 2 (main, `git show`) | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` | en entier |
| addendum 1 de la ligne 1, version 4 (main, `git show`), pour la forme seulement | `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67` | de l'en-tête au § 5.4 |
| rapport du développeur, code v3 | `ae1fa1da825934ec2af942d2047825695804e526122e24038a7098a0f2ca9d9c` | en entier |
| vérification du code v3 | `bd2773e29829ec9778aaaf2f3f4bb03796652f323f3bbb2c95e53ef24d6165f9` | en entier |
| `banc_juges_scriptes_ligne_3_v3.py` | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` | parties nommées à la réserve 1 |
| `chronometrer_banc_ligne_3_v3.py` | `8cb61afbdc6948197b756028d08df665725a2d3f99681c1e21c89b96eba5fa7e` | en entier |
| `essais_banc_juges_scriptes_ligne_3_v3.py` | `28ad0e8987790ec5a7bef61076606598604903e006f36c27a8a6e778dd0a3f77` | les lignes des chemins et des empreintes attendues seulement |

Les autres fichiers du § 3 n'ont pas été ouverts : empreintes seules. Rien sous `archives-reponses-modeles/` n'a été touché. Aucun gabarit d'additif de code n'est nommé par l'en-tête du texte : la forme suit l'addendum de la ligne 1.

Rédacteur neuf, modèle F.
