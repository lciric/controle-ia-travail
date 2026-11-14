# Rapport du développeur — code v74 du pilote MR-2 (réflexion absente sans effet) — v1

- **Développeur** : modèle A (session du compte organisme) ; écrit à 2026-11-14T13:09:09Z (`date -u`).
- **Mandat** : mot de Lazar « Option (a) : code v74, réflexion absente sans effet » ; R-2731 ; R-2738 (« aucun champ de réflexion
  aux deux appels et total d'usage égal à entrée plus sortie » vaut l'état « aucune réflexion cachée », qui rend la règle de
  comptage sans effet sur le coût ; le pilote s'arrête si un champ de réflexion apparaît en cours de course ; ajouts seuls ; essais
  et banc ; contre-lecture jamais sur le modèle Fable avant le 20 novembre 15:00 UTC).
- **Aucune dépense, aucun appel de modèle** : la sonde complète v74 n'est pas jouée ; elle attend ses deux lignes.

## 0. Verdict

Code v74 écrit et gelé en paquet contre `e7daf32` ; **ajouts seuls** (quatre fichiers neufs depuis la v73, `ce8c696`). **Essais :
147 passés** (v74, tête `605e0f6`) ; **les 115 de la v71 passent** sur la même tête. **Banc v74 : 54 mutations sur 54 tuées pour la
raison attendue** au premier passage (jalon 3), et **G10** (réserve R2, jalon 4) **tuée**. Contre-lecture (modèle C ≠ A, ni
Fable) : « autorisable pour la sonde » au jalon 1, constats 1a, 5, 6 corrigés au jalon 3 ; relecture courte du jalon 3 :
« autorisable pour la sonde complète v74 », réserves R1 (acceptée, consignée) et R2 (essai et mutation ajoutés).

## 1. Branche, paquet, fichiers

- Branche de l'organisme `prep/organisme-v74-pilote-mr2-compte-organisme-v1`, partie de `ce8c696` (v73), jalons `8459b7a`
  (code, essais), `671035d` (banc), `05323ea` (jalon 3 : constats 1a, 5, 6), `605e0f6` (jalon 4 : réserve R2 ; code inchangé).
- Paquet `organisme-v74-pilote-mr2-compte-organisme-v1.bundle` (`1cda2feb88e297d758bed7d0bb30d93cbe9b196ac3ab789826d39cfa4506d48b`), tête `605e0f6`, prérequis `e7daf32`,
  `git bundle verify` conforme. Liste des ajouts avec empreintes : `ajouts-organisme-v74-contre-e7daf32.txt`. Différentiel par paires
  v73 → v74 : `differentiel-v73-v74.patch`. Bloc gelé provisoire : `EMPREINTES-code-pilote-v74.txt` (`3a07668db516940f71763957c5422a182129a45792c47d307d6f06345360b50e`, sans identifiant de
  modèle ; « relevé de la sonde absent »). Le patch textuel complet n'est pas versé (R-2690).
- Fichiers neufs depuis la v73 : `pole/sonde_pilote_v74.py` (`f5671de9c6e5843552c3375d9666f944292df666795acd5a6af71a9e67e431ea`), `demonstrations/pilote_mr2_v74.py` (`5dc01676c1b525d97ed5a58729ceb4c8fd479d8957beb9ff39357b16df9bcf88`),
  `essais/test_pilote_mr2_v74.py` (`cd86b56949e784300f29e11ce5174ede0a27aa8dbd159b5e11c8e91e13794b38`), `essais/mutations_pilote_mr2_v74.py` (`48d907b87d4def7af386ed3913952ed2411f8905f3883edde8e56caf27d6ffa7`).

## 2. Ce qui change

1. **Module de la sonde v74** : pour Argon (dialecte gemini) seulement, `reflexion_sans_effet` = aucun champ `thoughtsTokenCount`
   aux deux appels (un champ présent, même à 0, ne vaut pas) et `totalTokenCount` entier égal à entrée + sortie ;
   `regle_confirmee_ou_sans_effet` = règle confirmée ou réflexion sans effet ; exigée à la place de `verdict_egal_a_la_regle` ;
   `reflexion_observee` n'est plus exigée pour Argon. Astra et Claude : exigences de la v72, inchangées. Relevé
   `releve-sonde-pilote-v74.json`. Sur les faits réels d'Argon de la sonde v73 (`35afab77…`, recopiés dans un essai), toutes les
   conclusions exigées sont vraies.
2. **Lanceur v74** : en mode réel, les proposeurs « sans réflexion » (lus au relevé) sont gardés : le pilote s'arrête (code 3, l'appel
   porté une fois au relevé partiel, sa dépense comptée une fois) si un champ de réflexion apparaît dans l'usage brut de l'appel
   (corps du relais), si la commande compte une réflexion non nulle, ou si le total d'usage d'Argon n'est pas entrée + sortie (jalon
   3). Le dossier de l'appel est calculé une fois (jalon 3) ; le manifeste porte la liste des proposeurs « sans réflexion ».

## 3. Essais et banc

- Essais v74 : 147 passés (228 sous-essais), dont la classe `V74` (8) et l'essai de bout en bout « sonde sans réflexion admise,
  puis arrêt du pilote quand le champ apparaît ». Deux essais portés de la v73 adaptés au sens neuf (l'artefact du refus nommé
  compte désormais des jetons cachés). v71 sur la tête v74 : 115 passés.
- Banc v74 : 54 mutations (v73 reciblées ; S01 à S09 ; G01 à G05, G07 à G09 ; M01 ; L02, L03) : **54 tuées pour la raison attendue** ;
  G10 ajoutée au jalon 4 : tuée. G06 sans objet (dossier calculé une fois).

## 4. Réserves dites

1. **R1** (relecture courte du jalon 3) : un appel d'Argon vide qui omettrait `candidatesTokenCount` arrêterait le pilote (arrêt
   prudent, sans repli silencieux, dépense comptée une fois). Accepté.
2. Un essai sain de bout en bout « pilote complet avec Argon sans réflexion » n'existe pas : la doublure des fournisseurs rend une
   réflexion à Argon aux appels du pilote. La garde est essayée en unitaire sur le cas sain.
3. Si Argon réfléchit à la sonde v74, sa règle est jugée par les votes de la v71 (relevé refusé si elle est démentie).
4. Le relevé de la sonde et les pièces brutes portent l'identifiant servi des modèles (R-2731 : restent sur la branche du lot).
