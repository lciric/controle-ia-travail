# Rapport — script de vérification du jeu de phrases des concepts de T0.7, version 2 (voie « réécriture d'un concept entier », garde de l'assemblage) — v1

- **Auteur** : Claude Opus 5.5, sous-agent neuf (développeur) de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; n'a écrit
  ni la consigne des concepts, ni le script v1, ni sa contre-lecture, ni aucune phrase ; n'est ni écrivain ni lecteur.
  **A lu des fichiers de T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis.**
- **Heures** (relevées par `date -u`) : début le 2026-11-10 vers 09:46 UTC (09:46:21) ; branche créée vers 09:50 ; premier
  jalon commis vers 10:01 ; essais complets de 10:05:01 à 10:09:51 UTC ; rapport écrit à partir de 10:10:57 UTC.
- **Consigne suivie** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-script-concepts-v2-reecriture-v1.md`
  (`6801069b5a41463d3d66318193e1dcb962cb81896c0f1395c57cbdbded6fe573`, vérifiée avant lecture) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en entier, règle 9 comprise.
- **Pièces lues** (empreintes vérifiées) : consigne des concepts v2 (`79f2c89c…`), sections 0, 2, 3, 6, 7, 8 et 9 ; rapport du
  script v1 (`74984a39…`) ; contre-lecture du script v1 (`25bce60e…`) ; script v1 (`6bc2665a…`) et ses essais (`c8f3d11a…`)
  au commit `1b87dfe1`, lus en entier ; dans `donnees/t07-concepts-v1/` : journal et JSON du décompte v1, en-tête et
  résumé de `selection-v1.json`, début de `cle-echantillon-v1.json`, annexes A et B (mots seulement). Aucune phrase de
  l'écrivain neuf n'a été lue (rien sous `/home/user/lot3-concepts/remise-ecrivain-2/`).

## 1. Livré (branche `prep/t07-concepts-script-v2`, partie de `1b87dfe1`, arbre `/home/user/wt-concepts`)

| fichier | sha256 | commit |
|---|---|---|
| `scripts/verifier_phrases_concepts_t07_v2.py` (2468 lignes) | `a858c40c13a588a14108c0615a41fcc6aed8498da8473d2377ff6485562dc86d` | `4759a4fd` |
| `tests/test_verifier_phrases_concepts_t07_v2.py` (1657 lignes) | `a4668d5b492354281170a5e0e80eee022f50ef1a1ead82fdb29675687b33cc39` | `f3d46c1e` |
| ce rapport (compagnon `.sha256`) | voir le compagnon | jalon 3 |

Le script v1 et ses essais ne sont pas touchés (empreinte du v1 vérifiée par un essai). Le v2 reprend tous les modes du v1
(`extraire`, `verifier`, `echantillon`, `decompter`, `assembler`, `rejouer-c12`), à l'identique sur un dossier sans
réécriture, sauf les corrections nommées en section 3. **Les règles des contrôles C0 à C13 ne changent pas d'un
caractère** : le code de C1 à C13 est celui du v1 ; seule la plomberie (concepts d'une remise, paires gardées en C8),
l'application de la règle de conflit au second passage (D-4) et les gardes changent.

## 2. Voie « réécriture d'un concept entier » (consigne des concepts, sections 3 et 7)

Option neuve `--tour 2` des modes `verifier`, `echantillon`, `decompter` (refusée pour les autres modes).

- **Amont, vérifié à chaque mode du second tour** : `selection-v1.json` (code 0), `decompte-contre-verification-v1.json`
  et `cle-echantillon-v1.json`, scellés et liés entre eux (le décompte porte sur cette sélection et cette clé) ; clé tirée
  sur une entropie neuve (sinon `--essai`) ; `selection-v2.json` absent. Concepts réécrits = ceux que le premier décompte
  envoie en réécriture (aujourd'hui `chats`, `geographie`) ; refus si aucun, ou si un concept attend le second lecteur de
  Q4 (voie non écrite). **Paires gardées** des concepts acceptés : prises et réserve de `selection-v1.json`, moins les
  paires non conformes de la contre-vérification (aujourd'hui `meteo` 71, `sports` 71, `meteo/10` et `sports/55` exclues ;
  le contrôle « retraits en attente = paires non conformes » est fait). Le second passage, l'échantillon et le décompte
  exigent que cet amont soit égal, à l'octet près des empreintes, à celui du premier passage.
- **Remise versionnée** (`--remise`) : seuls les concepts réécrits, 72 paires chacun, indices 1 à 72 (C1 inchangé ; une
  ligne d'un autre concept est une ligne rejetée) ; une remise égale à une remise du premier tour est refusée.
- **Passes 1 et 2** : mêmes contrôles C1 à C9 et C13 ; **C8 entre les paires neuves et contre les paires gardées** : une
  paire neuve en conflit avec une paire gardée est en défaut (choix déclaré : les gardées ont passé le premier tour et la
  contre-vérification ; la règle du rang de la section 3 mettrait sinon en défaut une paire de `meteo` acceptée) ; entre
  paires neuves, la règle de la section 3 (rang au premier passage ; D-4 au second) ; deux gardées en conflit, ou une
  gardée en défaut : refus d'incohérence. Les paires de l'ancienne remise des concepts réécrits et les paires retirées
  n'entrent pas dans la comparaison. Renvoi unique, retraits, réserve, plancher : ceux du v1.
- **Échantillon** : `⌈n/10⌉` paires par concept réécrit de `selection-reecriture-v2.json`, entropie neuve
  (`SeedSequence().entropy`), mêmes clés de graines (`echantillon-<concept>`, `ordre-echantillon`), clé à part.
- **Décompte** : même règle par concept. Plus d'une paire non conforme = **second échec : code 3**, décision « arrêt du lot
  pour ce concept », `decompte-contre-verification-v2.json` écrit (avec `arrets`), ligne `[ARRÊT]` au journal, **rien
  d'autre** (ni `selection-v2.json`, ni assemblage possible). Un « oui » à Q4 : code 1, rien écrit au-delà du décompte (second
  lecteur non écrit). Sinon : `selection-v2.json`.
- **Sélection finale `selection-v2.json`** (écrite une fois, R12) : concepts acceptés au premier tour recalculés depuis
  `selection-v1.json`, paire non conforme retirée et remplacée par la réserve valide suivante (CC-15) ; concepts réécrits
  depuis `selection-reecriture-v2.json`, avec le même remplacement s'ils ont une paire non conforme ; chaque paire porte
  `remise` (`remise-1` ou `remise-2`) ; par concept, `table_indices` (indice de remise → indice du fichier) et
  `provenance` (tour, remise, sélection source) ; `decomptes` (chemins et empreintes des deux décomptes),
  `retraits_contre_verification`, `reserves_c13` des deux tours. La même forme est écrite par le premier tour quand il
  n'y a qu'un retrait CC-15.

## 3. Gardes et corrections de la contre-lecture (`25bce60e…`)

| point | traitement |
|---|---|
| **D-1** (bloquant) | `assembler` refuse (code 2, avant toute écriture) : sans `--selection` ; si la sélection nommée n'est pas la `selection-v<k>.json` de plus haut k du dossier ; s'il n'y a aucun décompte ; si le **dernier décompte de chacun des quatre concepts** (v2 sur v1) n'est pas « accepté » ; si une sélection `v ≥ 2` n'est pas liée aux décomptes présents ; si une paire retirée (second passage, contre-vérification, de chaque tour) ou une paire de l'ancienne remise d'un concept réécrit y figure ; si une clé est tirée sur une entropie imposée hors `--essai`. Le nom final n'est créé qu'après tous les contrôles, par lien d'un fichier temporaire relu (ci-dessous). |
| **D-2** | **choix : refus propre**. Au second passage (des deux tours), une ligne rejetée (dont une ligne vide en fin) ou un enregistrement d'une paire non renvoyée dans la remise des renvois est un refus, code 2, motif écrit au journal de refus, **avant toute écriture** de `journal-verification-passe2-*` et de la sélection : le second passage se rejoue sur une remise des renvois corrigée, versionnée (nom neuf). Éprouvé : refus puis rejeu en code 0. |
| **D-3** | voie de réécriture écrite (section 2). Toujours non écrits : second lecteur de Q4, remise complémentaire (CC-17) ; échec fermé. |
| **D-4** | C8 du second passage : (0) conflit interne d'une paire, retirée ; (a) réécrite contre non réécrite ou gardée : la réécrite retirée ; (b) entre réécrites restantes, par rang croissant, une réécrite n'entre que sans conflit avec une réécrite déjà entrée. La sonde de la contre-lecture (`chats/3` retirée contre `chats/20`, `chats/7` en conflit avec `chats/3` seule) garde désormais `chats/7`. L'essai CC-16 du v1 garde son résultat. |
| **D-5** | **non traité, déclaré** : l'ordre des clés de la remise reste une information (en faire un défaut changerait la lecture de C1 entre les deux tours). |
| **D-6** | chaque module `controle_ia*` chargé est nommé au journal avec son chemin et son empreinte. Ce qui lie l'arbre à un commit déclaré par `--commit-module` reste les quatre empreintes données (non corrigeable sans git : déclaré). |
| **D-7** | essais ajoutés : chemin `--commit-module` + `--empreintes-module` (sain et artefact) ; double espace ; espace en fin ; refus de C12 au niveau du mode par la `GardeArret` du paquet chargé (toujours simulé : aucun fichier qui passe C2 à C11 n'échoue à C12 au code `8dc1cb09`). |
| **D-8** | `decompter` refuse une clé à entropie imposée sans `--essai` (écart écrit, `"essai": true` au décompte) ; `assembler` aussi. Écriture du fichier final : octets écrits sous `.phrases-concepts-v1.jsonl.<pid>.tmp`, relus, comparés, puis nom final créé par `os.link` (exclusif) ; le temporaire est ôté dans tous les cas ; un lien impossible est un refus, sans repli. |

## 4. Choix et écarts déclarés (consigne des concepts v2)

1. **Nom** : `…_v2.py` (R12) contre `…_v1.py` fixé par la section 6 — écart déclaré par la consigne de la mère.
2. **Code 3** (second échec) : hors des codes 0/1/2 de la section 6 ; exigé par la consigne de la mère (« code de sortie
   distinct »).
3. **D-2** : un défaut de forme de la remise des renvois (C1, « seules des paires renvoyées ») devient un refus (code 2)
   au lieu d'un code 1 sans voie : écart de code, règle inchangée.
4. **Noms du second tour** : `journal-verification-passe1-v2.txt`, `renvois-passe1-v2.json`,
   `journal-verification-passe2-v2.txt`, `selection-reecriture-v2.json`, `echantillon-lecteur-v2.json`,
   `cle-echantillon-v2.json`, `journal-echantillon-v2.txt`, `reponses-lecteur-v2.json` (écrit par la mère),
   `decompte-contre-verification-v2.json`, `journal-decompte-v2.txt`, `selection-v2.json` ; refus : `journal-refus-<mode>-tour2-<horodatage>.txt`.
   `phrases-concepts-v1.jsonl` et `journal-assemblage-v1.txt` gardent les noms des sections 2 et 8 (un seul assemblage ;
   le premier est le chemin de la ligne `SCELLEMENT-CONCEPTS-T07`). Aucun fichier du premier tour n'est réécrit (essai).
5. **C8 du second tour** : « neuve contre gardée → la neuve en défaut » (section 2 ci-dessus) ; « gardées » = prises et
   réserve des concepts acceptés, moins les paires non conformes, ma lecture de « leur sélection après le décompte v1,
   retraits et réserves compris ».
6. **Constat, règle inchangée** : l'alphabet fermé de C2 (`^[A-Z][A-Za-z ,'-]*\.$`) admet un espace avant le point final
   (« … pantry . ») ; essai qui l'atteste. À la mère de dire si cela compte.
7. Le format des réponses du lecteur ne change pas (`reponses-lecteur-v2.json` : même forme que `reponses-lecteur-v1.json`).

## 5. Essais (interpréteur du dépôt, suites lancées seules ; suite complète non lancée, règle 5)

- **v2** : `tests/test_verifier_phrases_concepts_t07_v2.py`, **153 passés sur 153**, de 10:05:01 à 10:08:03 UTC (181 s) :
  les **116 cas du v1 rejoués sur le v2** (dont 12 adaptés, dits dans leur texte ou leur nom : assembler depuis un décompte et avec
  `--selection` (D-1), `--essai` aux décomptes à entropie imposée (D-8), refus D-2 de la paire non renvoyée) et **37 neufs** :
  second tour de bout en bout (jusqu'à l'assemblage, fichiers du premier tour intacts), C8 contre gardées (prise, réserve)
  et hors comparaison (retirée, ancienne remise), ligne d'un concept non réécrit, 71 paires, retrait au second passage
  contre une gardée, quatre refus d'amont, premier décompte en attente de Q4, second échec (code 3, rien d'assemblé), une
  non conforme remplacée par la réserve de la remise 2, Q4 au second tour, sélection d'échantillon imposée, `--tour 2`
  hors des trois modes ; D-1 (sans nom, pas la dernière, sans décompte, décompte en code 1, paire retirée, sélection non
  liée, ancienne remise avec et sans champ `remise`) ; D-2 (ligne vide, paire non renvoyée, puis rejeu sain) ; D-4 (sonde
  et unités) ; D-6 ; D-7 ; D-8 (décompte et assemblage sans `--essai`, chemin sain à entropie neuve, écriture finale :
  lien impossible, relecture fausse, nom existant) ; v1 intact.
- **v1** : `tests/test_verifier_phrases_concepts_t07_v1.py`, **116 passés sur 116**, de 10:08:03 à 10:09:51 UTC (106 s).
- **Sonde sur le dossier réel** (copie dans le bloc-notes, effacée ensuite ; remise factice de mes gabarits, jamais une phrase
  de l'écrivain) : `verifier --tour 2 --passe 1` puis `--passe 2`, code 0 et 0 ; amont lu et lié (empreintes
  `193d5e94…`, `2828c2a4…`, `8f725b61…`), concepts réécrits `['chats', 'geographie']`, gardées `meteo` 71 et `sports` 71,
  C8 contre 142 paires gardées. Le dossier réel n'a pas changé (36 fichiers, tous égaux à leurs compagnons).

## 6. Mode d'emploi exact du second tour

Depuis `/home/user/controle-ia-travail` (le premier tour y a été joué ainsi), avec :

```
PY=/home/user/controle-ia-travail/.venv/bin/python
S=/home/user/wt-concepts/scripts/verifier_phrases_concepts_t07_v2.py
C="--consigne docs/procedures/consigne-concepts-sans-lien-T0.7-v2.md --dossier donnees/t07-concepts-v1"
M="--module-src /home/user/lot3-concepts/module-8dc1cb09/src"
T="--tokeniseur /home/user/lot3-concepts/tokeniseur"
R2=<remise de l'écrivain neuf : chats et geographie seuls, 72 paires chacun, indices 1 à 72>
```

(conseil : la remise est d'abord copiée et scellée sous `donnees/t07-concepts-v1/remise-ecrivain-v2.jsonl`, la remise des
renvois sous `remise-ecrivain-renvois-v2.jsonl`, section 8 ; le script lit `--remise` où qu'elle soit.)

1. **Premier passage** : `$PY $S verifier --tour 2 --passe 1 $C $M $T --remise $R2`
   → `journal-verification-passe1-v2.txt`, `renvois-passe1-v2.json` (+ `.sha256`). Code 0 : aucun renvoi ; code 1 : renvois
   (motifs et valeurs, paires en conflit avec une paire gardée nommées `… (gardée, remise-1)`) ; code 2 : refus, motif
   au `journal-refus-verifier-tour2-*.txt`.
2. **Renvois** (si code 1) : l'écrivain reçoit `remise-a-l-ecrivain-v1.md` et les seules paires renvoyées ; il rend `R2R`
   (un fichier vide s'il ne rend rien ; **aucune ligne vide**, aucune paire non renvoyée).
3. **Second passage** : `$PY $S verifier --tour 2 --passe 2 $C $M $T --remise $R2 $R2R` (sans `$R2R` s'il n'y a eu aucun
   renvoi) → `journal-verification-passe2-v2.txt`, `selection-reecriture-v2.json`. Code 0 exigé pour la suite. Refus « D-2 » :
   faire rendre une remise des renvois corrigée sous un nom neuf et rejouer ce même pas (aucun nom définitif n'a été écrit).
4. **Échantillon** : `$PY $S echantillon --tour 2 $C $M` → `echantillon-lecteur-v2.json`, `cle-echantillon-v2.json`,
   `journal-echantillon-v2.txt` (14 items pour deux concepts à 64 paires). La mère vérifie `"entropie_imposee": false` et
   consigne l'empreinte de `cle-echantillon-v2.json` **avant** que le lecteur commence.
5. **Lecteur neuf** (section 0) : reçoit `echantillon-lecteur-v2.json` et `remise-au-lecteur-v1.md` seuls ; rend
   `reponses-lecteur-v2.json` (même format que v1), que la mère scelle (`.sha256`, format `sha256sum`) dans le dossier.
6. **Décompte** : `$PY $S decompter --tour 2 $C` → `decompte-contre-verification-v2.json`, `journal-decompte-v2.txt` ;
   **code 0** : `selection-v2.json` écrit ; **code 1** : un « oui » à Q4 (second lecteur non écrit : rapport à la mère) ou
   sélection sous le plancher ; **code 3** : second échec, **arrêt du lot pour ce concept, rapport à la mère, rien
   d'assemblé**.
7. **Assemblage** (si code 0) : `$PY $S assembler --selection selection-v2.json $C $M $T`
   → `phrases-concepts-v1.jsonl` (+ `.sha256`), `journal-assemblage-v1.txt`. Toute faute de la garde D-1, de C11 ou de C12 :
   refus, code 2, nom final absent.
8. Puis, hors du script : scellement des fichiers de la section 8, provenance (`provenance-v1.md`, écrite par la mère :
   paires entrées par la réserve non relues, deux tours, deux écrivains, deux lecteurs), versement, ligne de registre.

## 7. Points ouverts (à la mère)

1. Second lecteur de Q4 et remise complémentaire : toujours non écrits (échec fermé).
2. La remise des renvois est désormais refusée à la moindre ligne hors de forme (D-2) : la consigne de l'écrivain neuf peut
   le lui dire (fichier sans ligne vide, seules les paires renvoyées).
3. Constat C2 (espace avant le point final admis par la lettre de la règle) : rapporté, non changé.
4. Contre-lecture courte et neuve du v2 et de ses essais avant usage réel (comme pour le v1) : regarder d'abord
   `amont_tour2`, `c8_second_passage`, `garde_assemblage`, la branche « second tour » de `mode_decompter`.

## 8. Gestes déclarés, interdits tenus, refus

- Git : `switch -c prep/t07-concepts-script-v2 1b87dfe1` dans `/home/user/wt-concepts` ; trois commits locaux sur cette
  seule branche (garde des secrets à 0 avant chacun) ; un seul `push`, `git push origin prep/t07-concepts-script-v2` ;
  aucun `fetch`, rien sur `main`, rien vers `lciric/controle-ia`. Les essais lisent, comme au v1, `git show` et
  `git archive` sur `f9fee3a8`, `03e3cbd9` (dossier du tokeniseur) et `8dc1cb09`.
- Parcours : aucune recherche récursive ; `ls` non récursifs ; `grep` sur des fichiers nommés. `docs/notes/bras-attaque/` et
  `docs/sources/` absents de l'arbre (vérifié par `test -e`). Un `ls` de `/home/user/lot3-concepts/` a montré le nom du
  dossier `remise-ecrivain-2` : rien n'a été ouvert dessous.
- Jamais ouverts : tout `lecture-sondes-t06.json` ; la lecture B et sa branche ; tout `diag/` et `runs/` de 7a ;
  `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; l'étiqueteur ;
  `scripts/extraire_mesures_epreuve_t06_v1.py` ; les textes d'actions de P3 ; aucun fichier de P3-bis ; aucune activation.
- Aucun `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucune valeur de clé ; aucun appel externe,
  aucune dépense. Écrits : la branche (script, essais, ce rapport et son compagnon), le bloc-notes de la session (sonde,
  effacée), les dossiers temporaires de pytest.
- **Refus rencontrés** : aucun refus de permission ni de classifieur.
