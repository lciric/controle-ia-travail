# Vérification courte de la procédure pas à pas du pilote MR-2 sur la machine jetable — v8 (passage v7 → v8) — v1

- **Lecteur** : instance neuve, qui n'a écrit aucune version de la procédure ni aucune de ses vérifications. Ce rapport n'écrit
  aucun nom de modèle (les quatre proposeurs sont dits « premier » à « quatrième », dans l'ordre de la configuration v12).
- **Pièce vérifiée** : `procedure-pilote-mr2-v74-machine-v8.md`, empreinte
  `56ccdb5a398acb8faa2588dd448ec42b446b7264e22d82cd3f975e5393f4054d`, égale à son compagnon et à l'empreinte attendue. Comparée à la
  v7 (`be688ec1eab8a91de7b12088f3e1f887f52ea9dac0fc7225c53371832e540c5d`, égale à son compagnon). Corrections attendues : la
  vérification de la v7 (`4be9e744ce1b1c53f6a835042f94c5ba510e63b8aeea492af046a3ef32cca3a2`, égale à son compagnon, lue dans le dépôt
  de travail).
- **Copie** : `/home/user/verif-pilote-v8`, tête détachée `ec563867`, arbre propre avant écriture.
- **Fin** : 2026-11-15T08:05:06Z (sortie de `date -u` dans la commande qui écrit ce fichier).
- **Aucune commande de la procédure n'a été jouée contre un service** : aucun appel au loueur, aucune machine, aucun modèle, aucune
  clé lue, ni `env` ni `printenv`.

## Verdict : jouable après corrections

0 bloquant, **2 majeurs**, 9 mineurs.

Le différentiel v7 → v8 est **entièrement déclaré** : aucun changement ni retrait caché (c'était le défaut de la v7). MA et MB sont
**fermés**, la forme de lancement éprouvée ici. a1 à a9 sont portés. Les deux majeurs sont neufs et se corrigent chacun par une ou
deux lignes :

- **M1** : le « risque résiduel à trancher par la mère » est décrit **en dessous de ce que fait le code** : une seule clé invalide,
  celle du premier fournisseur, suffit à mener à P-0 (elle sert deux proposeurs sur quatre, 8 appels sur 16), pendant que les appels
  des deux autres fournisseurs sont payés. La procédure écrit « jusqu'à P-0 si deux fournisseurs tombent ».
- **M2** : la garde `: "${REEL:?}" "${H:?}"` posée en tête du premier bloc de la section 11 (point a2) arrête tout le bloc de
  rapatriement, journaux compris, dans **tout arrêt (A) joué avant un code 0 de `jouer`** (où `REEL`, et avant la section 6 `H`,
  ne sont pas écrits), dont l'arrêt après un code 3 d'un pilote payé.

## Limites

- Texte scellé non lu (autre branche, interdite à ce lecteur) : la règle « 12 sur 16 et 3 par monde » est prise de la procédure
  elle-même (l. 370-371).
- Outil du loueur : lu dans son code installé, sans l'exécuter (`/home/user/vastai-env/lib/python3.13/site-packages/vastai/`,
  version 1.8.3 d'après ses métadonnées).
- Lanceur, commande et relais : lus dans le paquet de la copie, dépaqueté hors de tout dépôt, tête
  `605e0f60f3eed0948948e6a4eb15cb73de1d03de` ; rien n'en a été exécuté.
- Crochet de garde : lu (`73be0638…`, égal dans la copie et dans le dépôt de travail), non exécuté.
- Essais de forme, sur données factices, dans le dossier temporaire de la session : lancement détaché (script factice de 4 s,
  commande « ssh » simulée par un interpréteur non interactif dont la sortie et l'erreur sont un tube lu jusqu'à sa fermeture ;
  aucun service ssh réel ici) ; programmes du solde, du témoin, de l'inventaire d'après, de l'adresse et du port (outil du loueur
  remplacé par une fonction factice, attente neutralisée) ; gardes de variables ; constat du registre.
- Non vérifiable ici : que les champs `ssh_host` et `ssh_port` soient nuls pendant le montage (le code de l'outil ne le dit pas) ;
  l'image chez le loueur ; la clé ssh du compte.
- Aucun refus d'outil, de crochet ni de classifieur rencontré.

## 1. Différentiel exact v7 → v8

`diff` : 23 blocs. Relecture mot à mot des retraits (`git diff --no-index --word-diff`) : tous les mots retirés appartiennent aux
lignes que la section 12 quinquies dit remplacées.

| lignes de la v8 | changement | point déclaré |
|---|---|---|
| 1 | titre « v8 » | version (R12) |
| 7-10 | versions, « la v8 remplace la v7 pour l'usage », renvoi à 12 quinquies | version ; dit dans l'en-tête même |
| 81-83 | nœud à 2,70 USD ; arrêt d'un processus par son PID sur le mot de la mère | a4 (i), a4 (ii) |
| 134 | solde : `credit`, `balance`, seuil de 5 USD par programme ; réserve levée | a6 |
| 137-140 | témoin de l'inventaire d'avant, compté par programme | a4 (iv) |
| 150 | `: "${ETIQ:?}";` devant la création | a2 |
| 156-157 | offre choisie à la main, prix consigné | a8 |
| 169-170 | inventaire d'après : programme sans redirection, `\| diff -` | a3 |
| 192-205 | adresse et port par programme, attente bornée, clé ssh, `IdentityFile` ; `ssh-url` écarté | a5 |
| 263, 409 | `\|\| { echo 97 > code-… ; exit 97; }` | a1 |
| 267-268, 359-360, 385-386, 414-415 | quatre lignes de lancement, et « ne jamais la rejouer » | MA |
| 342-345 | « à trancher par la mère », risque décrit | a4 (iii) |
| 381-383 | relance : ligne des dossiers remplacée | MB |
| 390-391 | `REEL=reel` après un code 0 ; garde annoncée | a2 |
| 396-398 | constat du registre ; effacement des clés avant le nœud | a7 |
| 406, 444 | `: "${REEL:?}" "${H:?}"` | a2 (voir M2) |
| 422-423 | « `mesurer` muet » | a1 |
| 582-604 | section 12 quinquies | déclaré |

- **Changement non déclaré : aucun. Retrait non déclaré : aucun.** Aucun bloc ne tombe dans les sections 1, 4, 5, 7, 8, 12, 12 bis,
  12 ter, 12 quater, 13 ; dans la section 11, le seul bloc est la ligne 444, comme déclaré.
- Trois inexactitudes de la déclaration, sans effet (m8) : l'en-tête changé (l. 1, 7-10) n'est pas dans le tableau ; la mention
  « nom du champ à confirmer », dite remplacée, est encore dans le texte sous « ancien texte » (l. 134-135) ; la l. 5 dit toujours
  « jouée seulement après la vérification du différentiel v6 → v7 ».

## 2. MA : fermé

Les quatre lignes (l. 267, 359, 385, 414) ont exactement la forme corrigée : garde sur le code **et** sur le journal,
`{ setsid nohup bash … > /dev/null 2>&1 < /dev/null & echo lancé; } || echo "NON LANCÉ"`, chacune avec ses propres noms
(`06-generer`, `09-reel`, `09-reel-2`, `10-mesurer`), chacune suivie de « ne jamais la rejouer ; passer au suivi ».

Éprouvé ici (script factice : `cd`, puis `sleep 4` avec le journal en redirection, puis le code) :

| essai | affiché | retour |
|---|---|---|
| premier lancement | « lancé » | 0,005 s |
| second lancement pendant le premier (journal présent) | « NON LANCÉ » ; un seul processus | 0,005 s |
| après la fin (code 0 écrit) | « NON LANCÉ » ; aucun processus | 0,005 s |
| code présent, journal absent | « NON LANCÉ » | 0,004 s |
| `cd` impossible | « lancé », code 97 écrit ; rejoué : « NON LANCÉ » | 0,004 s |
| témoin : forme de la v7 | « lancé » | 4,0 s |

La forme passe aussi sous `sh`. Reste : aucune conduite n'est écrite pour un « NON LANCÉ » inattendu au premier lancement (m3).

## 3. MB : fermé

- **Refus avant la création de `reel/`** (gardes du mode réel, dossier, mondes) : le premier script a écrit le journal et le code 2,
  puis effacé les clés ; registre absent. Relance (l. 379-387) : les deux pièces renommées en `-essai1` ; `reel-2` et registre
  absents (« prêt ») ; contrôles rejoués, la ligne des dossiers remplacée (« absents ») ; clés renvoyées ; `lancer-reel-2.sh` rendu
  du modèle ; lancement gardé par `code-09-reel-2.txt` et `journal-09-reel-2.txt` ; suivi sur `code-09-reel-2.txt`. Cohérent.
- **Refus après la création de `reel/`** (lancement ou attente des relais ; lanceur l. 291-317 et 349-352 : le registre n'est écrit
  qu'une fois les relais prêts, et sur un refus sans appel les relais sont arrêtés par leur PID) : mêmes commandes ; la ligne
  remplacée (l. 382) n'exige plus `reel` absent ; le lanceur n'exige que `reel-2` absent (l. 291) ; les ports sont rendus par
  l'arrêt des relais, et le contrôle des ports rejoué le constate (sinon arrêt (A)). **La relance a lieu.** `reel/` reste, jamais
  rapatrié (l. 456-457).
- La phrase de la l. 330 (« arrêt (A) si un dossier existe ») se lit, à la relance, avec la ligne remplacée : `reel-2` présent →
  arrêt (A). Un second code 2 : arrêt (A) (l. 392).

## 4. a1 à a9

| mineur | porté | où (v8) | reste |
|---|---|---|---|
| a1 | oui | 263, 409, 422-423 | — |
| a2 | oui | 150, 390-391, 406, 444 | **M2** ; m1 (la ligne de création ne commence plus par `GO_ID=`) |
| a3 | oui | 169-170 | éprouvé : « seul ajouté, égal à l'identifiant » ; `identifiant.txt` intact |
| a4 (i) | oui | 81-82 | 2,70 / 0,20 = 13,5 h, après le nœud des 13 h : juste |
| a4 (ii) | oui | 82-83 | — |
| a4 (iii) | oui pour le mot | 342-345 | **M1** : la description du risque est inexacte |
| a4 (iv) | oui | 137-140 | éprouvé : liste vide refusée |
| a5 | oui | 192-205 | m2, m4 |
| a6 | oui | 134-136 | éprouvé ; m8 pour la phrase |
| a7 | oui | 396-398 | m5 (constater qu'aucun `jouer` ne tourne : commande non écrite) |
| a8 | oui | 156-157 | — |
| a9 | oui | 12 quinquies | rejoué ici, mêmes résultats |

## 5. Régressions

- **Argent, plafonds** : lignes, montants, parts (12, 8, 9,36, 9,36 USD), part machine 3 USD, prix horaire au plus 0,20 USD, pire
  cas 14 h : inchangés. Plafonds mécaniques des relais : inchangés (l. 366-367).
- **Nœud à 2,70 USD, heure limite** : nœud remis (l. 81-82) ; heure limite et sa conduite inchangées.
- **Arrêt d'un processus** : « aucun arrêt d'un processus du pilote sans le mot de la mère, et alors par son PID (R10) » remis
  (l. 82-83).
- **Destruction** : bloc inchangé (l. 461-479) : identifiant relu et exigé entier, étiquette comparée par programme devant
  `destroy … -y`, preuve d'absence par la liste relue, témoin, témoin vide dit. La garde de `REEL` n'est pas dans ce bloc : elle ne
  peut pas retenir une destruction.
- **Témoin de l'inventaire d'avant** : remis et défini.
- **Clés** : aucune valeur affichée ni écrite ; les commandes neuves n'affichent que le solde, des comptes, une adresse et un port.
  Une erreur du programme du solde n'affiche ni le corps reçu ni un champ personnel (éprouvé sur cinq entrées factices).
- **`GO_ID=`** : la ligne de création est maintenant `: "${ETIQ:?}"; GO_ID=GO-2026-11-14-14 vastai create instance …` (l. 150) : elle
  **ne commence plus par `GO_ID=`**. Sans effet sur le crochet, qui cherche l'identifiant n'importe où dans la commande (l. 190-194
  du crochet), ni sur l'outil ; écart de forme, m1. L'aide : « sous le même préfixe », inchangé.
- **Régression trouvée** : M2 (rapatriement des arrêts précoces).

## 6. Commandes neuves, dans le code de l'outil 1.8.3 et sur données factices

- **`show instances --raw`** (`cli/commands/instances.py` l. 1057-1064 ; `api/instances.py` l. 31-58) : sans `--limit` ni jeton de
  page, rend la **liste plate de toutes les pages**, lignes entières. Champs `ssh_host`, `ssh_port`, `actual_status`, `id`, `label`
  présents dans le code (`data/instance.py` l. 57, 83-84). Type de lancement par défaut de la création : ssh (`cli_runtype`), donc
  port = `ssh_port` sans décalage.
- **Programme de l'adresse et du port** (l. 198-202), éprouvé : champs nuls trois fois puis remplis → quatre relectures, fichier
  de configuration juste, « 0 » marque restante. Jamais monté → vingt relectures, message « arrêt (A) »… **puis la ligne suivante
  vide les deux marques et affiche le « 0 » attendu** (m2). Hôte nul et port présent → `HostName None` écrit (m2). Outil en échec
  après un premier passage → l'ancien `adresse-port.txt` est repris (m2).
- **Solde** (`api/billing.py` l. 225-240, `cli/main.py` l. 204-209, `cli/display.py` l. 343 et 355) : `show user --raw` rend l'objet
  du compte en JSON pur, sans `api_key` ; champs `credit` et `balance`. Éprouvé : 12,5 → affiché, code 0 ; 4,99 → refus ; nul,
  champ absent, sortie non JSON → refus, rien de personnel affiché.
- **Témoin de l'inventaire d'avant** : éprouvé (deux lignes → « 2 instances listées » ; liste vide → refus).
- **Constat du registre** (l. 396) : éprouvé, « absent » puis « présent » ; un échec de ssh n'affiche rien et rend un code non nul.
- **Gardes de variables** : sous bash non interactif, `: "${X:?}"` arrête la suite de la commande (code 127), que ce soit en tête
  de ligne ou de bloc ; elle ne protège rien si elle est jouée dans une commande à part de celle qui emploie la variable (m6).

## 7. Risque résiduel laissé à la mère (non tranché ici)

Ce que fait le code, à la lettre, si une clé est invalide au lancement unique (lanceur l. 311-345 ; `pole/proposeurs_pilote_v70.py`
l. 40-42 et 352 ; relais l. 405-406 ; commande l. 230-235 ; configuration v12) :

1. Le relais démarre : seule la **présence** de la clé est contrôlée (`cle_presente`). Le registre des lancements est écrit quand
   les relais sont prêts, **avant le premier appel** : le lancement unique est consommé.
2. Au premier appel d'un proposeur de cette clé, le fournisseur refuse ; le relais rend 502 ; la commande sort en code 3,
   « echec » ; ce code est une panne : le proposeur est **abandonné**, ses trois autres appels sont portés « echec » **sans être
   envoyés**. L'appel refusé est compté **au pire cas** dans le relevé de dépense du pilote (écriture comptable ; le fournisseur ne
   facture pas un refus).
3. Le pilote **continue** avec les autres proposeurs, dont les appels sont payés, et sort en **code 0** s'il n'y a pas d'autre
   arrêt. Aucune relance n'est permise (registre présent).
4. La clé du **premier fournisseur sert les premier et deuxième proposeurs** (8 appels sur 16) : invalide, elle laisse au plus 8
   appels complets, sous le minimum de 12 : **P-0 par cette seule clé**, pendant que les troisième et quatrième proposeurs
   dépensent jusqu'à leurs parts (9,36 USD chacun). La clé du deuxième ou du troisième fournisseur, invalide seule, laisse au plus
   12 appels sur 16 et 3 par monde : **exactement le minimum**, sans marge ; tout autre échec donne P-0.

La procédure (l. 341-345) dit : « les appels de ce fournisseur échouent tous (« echec », code 0, sans reprise) et consomment le
lancement unique, jusqu'à P-0 si deux fournisseurs tombent ». Juste sur : aucune preuve avant le lancement, « echec », code 0, sans
reprise, lancement consommé. **Inexact** sur le seuil (une clé suffit), et muet sur la dépense des autres fournisseurs : M1.

## 8. Constats classés

### Bloquant

Aucun.

### Majeurs

**M1 — Le risque résiduel soumis à la mère est sous-décrit** (l. 342-345). Voir la section 7. La mère tranche sur ce texte ; il
doit dire le cas le plus lourd.
Ancien : « … de sorte que les appels de ce fournisseur échouent tous (« echec », code 0, sans reprise) et consomment le lancement
unique, jusqu'à P-0 si deux fournisseurs tombent. »
Nouveau : « … de sorte que le premier appel de chaque proposeur de ce fournisseur échoue, que ce proposeur est abandonné (ses
autres appels portés « echec » sans être envoyés), que le pilote continue et sort en code 0, lancement unique consommé, sans
reprise. **La clé du premier fournisseur sert deux proposeurs sur quatre (8 appels sur 16) : invalide seule, elle mène à P-0**,
pendant que les appels des deux autres fournisseurs sont payés (jusqu'à 9,36 USD chacun). La clé du deuxième ou du troisième
fournisseur, invalide seule, laisse exactement le minimum (12 sur 16, 3 par monde), sans marge. »

**M2 — La garde de `REEL` et de `H` en tête du premier bloc de la section 11 arrête le rapatriement de tout arrêt (A) précoce**
(l. 444 ; même garde l. 406). L'arrêt (A) renvoie à ce bloc pour « rapatrier ce qui peut l'être (journaux, empreintes ; `rapatrier`
si un dossier de sortie existe, y compris après un code 3) » (l. 71-72). Or `REEL` n'est écrit qu'**après un code 0** du premier
essai ou après une relance (l. 390-391), et `H` à la section 6. Dans tout arrêt (A) des sections 3 à 9 — bloc différent, monde non
conforme, essai à blanc refusé, **code 3 de `jouer`**, « tout autre code » avec registre présent — la première ligne du bloc sort
en erreur (éprouvé : code 127, rien de la suite n'est joué), copies des journaux comprises. À la lettre, l'exécutant détruit la
machine à l'étape (4) sans avoir rien rapatrié — après un code 3, les pièces partielles et les journaux d'un pilote payé, qui
servent au rapprochement de la dépense — ou il choisit seul une valeur de `REEL`, machine louée. En v7 la garde n'existait pas :
les copies des journaux passaient.
Correction, deux lignes :
ancien (l. 444) : « `: "${REEL:?}" "${H:?}"` » en tête du bloc ;
nouveau : ligne retirée de la tête du bloc ; la garde portée par les seules lignes qui emploient ces variables : dans la ligne de
`rapatrier`, `--source /root/pilote/${REEL:?}` et `--mondes-sha256 ${H:?}` ; et la phrase « dans un arrêt (A) où `REEL` n'est pas
écrit (aucun dossier de sortie réel), sauter la ligne de `rapatrier`, la copie de `rapatrie-reel` et le contrôle du compagnon ; les
autres copies se jouent ».
ancien (l. 390-391) : « **Après un code 0 du premier essai** : `echo REEL=reel >> "$ENV/variables.sh"` » ;
nouveau : « **Dès que la ligne de lancement a affiché « lancé »** : `echo REEL=reel >> "$ENV/variables.sh"` (et `REEL=reel-2`
dès le « lancé » de la relance ; la dernière ligne écrite l'emporte) », pour que `REEL` existe dans un arrêt (A) après un code 3.

### Mineurs

- **m1 — La ligne de création ne commence plus par `GO_ID=`** (l. 150). Sans effet sur le crochet ni sur l'outil.
  Ancien : « `: "${ETIQ:?}"; GO_ID=GO-2026-11-14-14 vastai create instance OFFRE --image python:3.13-bookworm --disk 20 --label "$ETIQ" --raw > "$ENV/creation.json"` » ;
  nouveau : « `GO_ID=GO-2026-11-14-14 vastai create instance OFFRE --image python:3.13-bookworm --disk 20 --label "${ETIQ:?}" --raw > "$ENV/creation.json"` »
  (éprouvé sur une commande factice : étiquette vide → la commande n'est pas jouée). La l. 36 impose déjà un préambule devant
  chaque commande : dire que, pour cette ligne, le préambule est joué dans la commande d'avant, ou accepter l'écart en le disant.
- **m2 — Programme de l'adresse et du port : l'échec n'arrête pas la suite** (l. 198-202). Le message « arrêt (A) » est un simple
  `echo` ; la ligne suivante vide `ADRESSE` et `PORT` et affiche le « 0 » attendu. Un `adresse-port.txt` d'un passage d'avant est
  repris si l'outil échoue. Un hôte nul avec un port présent écrit `HostName None`.
  Ancien : « `test -s "$ENV/adresse-port.txt" || echo "machine non montée en dix minutes : arrêt (A)"` » puis « `read A PT < …; sed -i … && grep -c …` » ;
  nouveau : `rm -f "$ENV/adresse-port.txt"` devant la boucle ; dans le programme, `assert m[0]["ssh_host"]` ; puis
  « `if test -s "$ENV/adresse-port.txt" && read A PT < "$ENV/adresse-port.txt"; then sed -i "s/ADRESSE/$A/; s/PORT/$PT/" "$ENV/ssh_config"; grep -c -E 'ADRESSE|PORT$' "$ENV/ssh_config"; else echo "machine non montée en dix minutes : arrêt (A)"; fi` ».
- **m3 — « NON LANCÉ » inattendu au premier lancement : aucune conduite écrite** (l. 267, 359, 385, 414). Pour `jouer`, les clés
  resteraient sur la machine (le script qui les efface n'a pas tourné) et le suivi dirait « en cours », « clés encore là » sans
  fin. Nouveau : « « NON LANCÉ » alors qu'aucun lancement n'a été fait : ne rien relancer ; effacer les clés (étape (2) de (A)) ;
  nœud à la mère ».
- **m4 — Attente du montage** (l. 193-200). (i) La boucle dure dix minutes au moins (vingt fois 30 s, plus les appels) : plus que
  le délai d'une commande d'une session d'agent. La dire rejouable (elle ne fait que lire) et la couper, par exemple
  `seq 1 3` par commande, sept commandes au plus. (ii) « Champs nuls pendant le montage » n'est pas établi par le code de l'outil :
  si le loueur remplit `ssh_host` et `ssh_port` dès la création, la boucle sort au premier tour et le premier `ssh M` est refusé,
  sans conduite écrite. Nouveau : exiger aussi `m[0].get("actual_status")=="running"` dans le programme, ou écrire une reprise
  bornée du premier `ssh M true` (dix minutes au plus, puis arrêt (A)).
- **m5 — « Si aucun `jouer` ne tourne »** (l. 75, 84, 397) : la commande qui le constate n'est pas écrite. Nouveau :
  `ssh M 'pgrep -af "[p]ilote_mr2_v74.py" || echo "aucun processus du pilote"'` (les crochets évitent que la commande se trouve
  elle-même ; lecture seule, aucun arrêt par motif).
- **m6 — Portée de la garde de `REEL`** (l. 391, 424, 431). La phrase « les commandes des sections 10 et 11 commencent par » la
  garde n'est écrite que devant deux blocs ; les lignes de `ls` (l. 424) et de `lire` (l. 431), jouées à part, ne la portent pas.
  Nouveau : `${REEL:?}` à la place de `$REEL` dans ces deux lignes (même forme que la correction de M2).
- **m7 — `REEL=reel` est écrit sous l'issue « code 2 »** (l. 390-391), alors que l'issue « code 0 » (l. 370-371) renvoie à la
  section 10 sans le dire. Sans dommage (la garde de la l. 406 arrête), mais à déplacer ; réglé par la correction de M2.
- **m8 — Restes de rédaction.** L. 5 : « jouée seulement après la vérification du différentiel v6 → v7 (mère, R-2846) » → « v7 →
  v8 ». L. 134-136 : la parenthèse garde l'ancien texte et son repli (« sinon, lecture du seul solde à l'interface du loueur ») :
  dire si ce repli vaut encore quand le programme échoue, ou l'ôter (la l. 136 dit déjà « sinon, aucune création, nœud »). L. 44 :
  `REEL` manque à la liste des valeurs de `variables.sh`. L. 17-20 : les champs neufs sont lus dans le rapport `4be9e744…`, non cité
  à cet endroit. Section 12 quinquies : l'en-tête changé n'est pas au tableau.
- **m9 — Témoin de l'inventaire d'avant** (l. 139) : `len()` d'un objet qui ne serait pas une liste passerait. Nouveau :
  `l=json.load(…);assert isinstance(l,list) and len(l)>=1`. Le code de l'outil rend bien une liste : précaution seulement.

## Pièces

- Arbre dépaqueté et essais de forme : dossier temporaire de la session du lecteur, hors de tout dépôt (`arbre/`, `essais/`).
- Rien d'autre n'a été écrit dans la copie que ce rapport et son compagnon ; aucun commit, aucune poussée.
