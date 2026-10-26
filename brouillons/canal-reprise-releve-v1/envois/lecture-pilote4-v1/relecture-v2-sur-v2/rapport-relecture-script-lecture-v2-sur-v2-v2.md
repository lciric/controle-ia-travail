# Seconde relecture du script de lecture contre le bruit du pilote 4 : la v2 — rapport, deuxième écriture

Même sous-agent relecteur que pour la v1 (rapport `rapport-relecture-script-lecture-v2.md`,
`9c15930dc242b2885557d81c6560f8b1aee54ebf03314699c353ced8f2959e3e`) ; il n'a écrit ni le script, ni ses essais, ni le
texte du pilote, ni le noyau. 26 octobre 2026 ; cet en-tête est écrit à 05:46:08 UTC (heure lue sur `date -u` dans la
commande même qui écrit ce fichier). Demande : message du coordinateur (séparation `test` / `test_final`, courses M et S,
traitement de RSL-01 à RSL-17, commandes du LISEZMOI § 5, rejeu sous 3.11, 3.12 et 3.13, au moins trois artefacts de
séparation). Mêmes interdits qu'au premier brief, tenus (§ 6).

Cette écriture remplace `rapport-relecture-script-lecture-v2-sur-v2.md`
(`d8fe59c1a8c05b5761d94a36e380e06fa23cddc75fff16152b0c0e28c82a3eaa`, gardé tel quel, R12). En recoupant ses renvois
(`journaux/verification-renvois-rapport-v1.log`), la relecture y a trouvé le périmètre de trois vérifications dit trop
largement (instantanés et trace d'audit : pas sur chaque cas ; commandes du § 5 : lancées avec la variable d'essai de la
banque ; ordre « M puis S » : vérifié par la batterie de l'auteur rejouée, non par le harnais de la relecture) et quatre
imprécisions (§ 1, RSL2-04, RSL2-08, ligne RSL-02 du § 3) ; elle ajoute à la correction de RSL2-02 la question des
« faits mécaniques » et reprend dans celle de RSL2-01 la dernière clause du texte v5. Ni le verdict, ni un constat, ni une
gravité ne changent.

## Verdict

**utilisable après corrections**

Les calculs sont ceux de la v1, inchangés et justes ; la séparation des fichiers tient (non-interférence vérifiée dans les
deux sens) ; gardes, noms, appariement et commandes sont conformes sous Python 3.11.17, 3.12.3 et 3.13.17. Deux
corrections d'une ligne avant usage : RSL2-01 (la phrase (iv) doit suivre le texte v5 : « aucune comparaison entre les
deux courses ») et RSL2-02 (la ligne d'état compte des signalements propres à `test_final`). Le reste est mineur.

## 1. Pièces relues

Copie : `/var/tmp/relecture-script-lecture-pilote4-v2/copie/` (lecture seule ; empreintes vérifiées, égales à celles du
coordinateur et des compagnons) :

| fichier | sha256 |
|---|---|
| `lire_pilote4_v2.py` | `a23613207175b1dbd89784215ececc2a8458332e3e11f1346179c254e099ae2a` |
| `essais_lire_pilote4_v2.py` | `dee7e0fec8951c4abbbc0a30100f4b0962854946beea6b0708b600985cee6308` |
| `essais-lire-pilote4-v2.log` | `4aa9de04d77a201981fa46c21c59c3ca2acb8bfa8dc835aab50f3ddf7b4c2555` |
| `LISEZMOI-script-lecture-v2.md` | `2f328fee182a4f2522fc771d236dd1c636dcad6ce72caa3d91fb7a9d9d646b33` |
| `fournis/decision-N-taches-fraiches-et-lecture-test-final-v1.md` (N-049, N-050) | `4b23e00fda02cef897f9d73b4274a0bed59bdab8a8f156f37a7966fb80d7a034` |
| `fournis/rapport-relecture-script-lecture-v2.md` (copie à l'octet de mon rapport sur la v1) | `9c15930dc242b2885557d81c6560f8b1aee54ebf03314699c353ced8f2959e3e` |

Lu en plus, en lecture seule, parce que la v2 en dépend : le texte du pilote v5 (`pilote4-gemini-organisme-v5.md`,
`1943f39ada61db7d21e53b7e0c02c6e826b86e1467687eedbe56617877ab7f87`, égal à son compagnon : table de correspondance,
§ Plan points 1 à 4) et le lanceur v11 (`lancer_pilote4_gemini_v11.sh`, `21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7`,
l'empreinte que donne la v5 : course S `pilote4-gemini-v6-2-s-v1`, lignée `gemini-organisme-v6-2-s`, l. 79–93 ; `$PILOTE`
et `-tentativeN`, l. 181 ; même archive, l. 763 et 889–895 ; bloc de la liste fermée et `permis_re` identiques à l'octet à
ceux du v10, de « # 9. Ce qui est poussé » à la fin), et le texte v4 (`pilote4-gemini-organisme-v4.md`,
`782b858c537222245fd757c23ea6d75abae142df029eed3e53af36d8c78cfa95`, égal à son compagnon : parts de 36 et 24 tâches,
l. 96 et 405–406 ; « (ii) y est impossible par construction », l. 402). Les fonctions de calcul de la v2 (`wilson`,
`borne_basse_maximale`, `compter`, `mcnemar_exact`, `holm`, la règle « catégorie absente du train », la lecture de la
banque et des réponses) sont celles de la v1 au caractère près, hors chaînes de documentation, `affichable` dans les motifs
de `verifier_liste`, un paramètre inutilisé retiré (`taille`, `depuis_reponses_brutes`) et une ligne rejointe
(`tests_mcnemar`) (`journaux/comparaison-fonctions-v1-v2-v1.txt`).

## 2. Constats

**RSL2-01** — `lire_pilote4_v2.py` l. 118–120 (`PHRASE_IV`, écrite dans les deux fichiers : l. 1018, 1030, 913) ;
LISEZMOI v2 § 4, l. 93–94 — **à corriger avant usage**.
Faux : la phrase (iv) est celle du texte v4 (« à une course par objet, […] aucune comparaison entre les deux objets n'est
faite ») ; le texte v5 (table de correspondance, l. 65) la remplace par « aucune comparaison entre les deux courses : mêmes
tâches, même objet, questions différentes, une graine chacune ; un écart entre elles tient à la question, à la graine ou au
bruit, sans moyen de les séparer ; les verdicts des agents de la boucle extérieure restent tenus par cet interdit ». Avec un
seul objet, l'interdit que la sortie écrit est vide : il n'interdit plus de comparer les courses M et S, alors que le
fichier `test`, ouvert aux agents dès la fin de chaque course (sous la retenue de lecture en cours), est le seul texte du
script qu'ils voient avant la fin du compteur. Le LISEZMOI voit l'écart (§ 4) et le garde. Correction : (iv) au texte v5,
par exemple « tout le reste est « dans le bruit » : à une graine par course, le bruit entre graines n'est pas mesuré ;
aucune comparaison entre les deux courses n'est faite (mêmes tâches, même objet, questions différentes : un écart entre
elles tient à la question, à la graine ou au bruit, sans moyen de les séparer ; les verdicts des agents de la boucle
extérieure restent tenus par cet interdit) ; un changement au-delà du bruit des tâches dans une course peut tenir à sa
graine » (libellé à fixer par conv-audit) ; citer la v5 à côté de « point 4 bis du texte v4 » (l. 933, 1010).

**RSL2-02** — `lire_pilote4_v2.py` l. 1088–1090 ; essai `art_score_noyau_altere`, `essais_lire_pilote4_v2.py` l. 1228 —
**à corriger avant usage**.
Faux : la ligne d'état écrit `signalements : len(communs + sig_t + sig_f)` : les signalements propres à `test_final` (écart
avec le noyau sur `test_final`, `score-final.json` absent, illisible ou sans la famille, test (iii) impossible, générations
de la seconde course) passent sur la sortie standard dès la fin de la course, alors que N-050 et le texte v5 (§ Plan,
point 3) ferment `test_final` jusqu'à la fin du compteur de rondes. Essai de la relecture, trois interpréteurs : deux
courses identiques sauf une altération de `score-final.json` de g2 ; fichiers `test` identiques (heure et empreintes à
part) ; ligne d'état « signalements : 0 » contre « signalements : 1 ». Ce n'est ni un score, ni une borne, ni une valeur
p, ni un verdict, mais un indice de `test_final` (une anomalie y existe), lu par l'opérateur et recopiable dans ses
messages ; l'essai de l'auteur exige ce mélange (« signalements : 2 »). Correction : ne compter sur la ligne d'état que les
signalements du fichier `test` (`communs + sig_t`), par exemple « signalements (fichier test) : N » ; ceux de `test_final`
restent dans son fichier ; adapter l'essai. Question pour conv-audit : N-050 (l. 53) et le texte v5 (l. 108) ouvrent dès la
fin de course « les faits mécaniques » ; si certains signalements que le script range dans `test_final` sont tenus pour
tels (`score-final.json` absent ou illisible, générations notées de la seconde course), les ranger avec les signalements
communs, écrits dans les deux fichiers, plutôt que de les laisser compter seuls sur la ligne d'état ; l'écart avec le
noyau sur `test_final` et le test (iii) impossible restent à `test_final`.

**RSL2-03** — `lire_pilote4_v2.py` l. 436–445 et 668–669 — mineur (théorique).
Faux : le signalement commun « gNNN : N entrée(s) de reponses-lues.json écartée(s) » compte les entrées des deux parts (et
les identifiants inconnus) et s'écrit dans le fichier `test`. Essai, trois interpréteurs : une entrée d'une tâche de
`test_final`, que la règle du juge écarte, fait paraître ce signalement dans le fichier `test`. Le noyau n'écrit jamais
d'entrée écartée (même règle que le juge, `boucle.py` l. 728–731 et 785) : le cas suppose un fichier du noyau défectueux.
Correction : compter les entrées écartées par part, les identifiants inconnus à part.

**RSL2-04** — `lire_pilote4_v2.py` l. 109–110 et 641–648 — mineur (empreinte croisée).
Le fichier `test` porte l'empreinte de `reponses-lues.json` (et du repli `reponses_test.json`), qui contient aussi les
réponses de `test_final`. Essai : deux courses qui ne diffèrent que par les réponses de `test_final` donnent des fichiers
`test` identiques hors de l'heure, des empreintes du dossier et de l'archive, et de ces empreintes-là. Une empreinte ne se
renverse pas (il faudrait deviner l'état de chacune des 60 tâches de `test_final`, 36 et 24 selon le texte v4, parmi
trois : l'une ou l'autre étiquette, ou aucune réponse ; 3^60 possibilités pour cette seule part, celles de `test` en plus) :
aucune fuite pratique ; mais le fichier `test` n'est pas fonction de la seule part `test`. Correction (facultative) : n'y garder
que `score.json` et laisser `reponses-lues.json` au fichier `test_final`, ou y mettre l'empreinte de la seule projection
`test` des réponses.

**RSL2-05** — `lire_pilote4_v2.py` l. 966–975 — mineur (RSL-16 incomplet).
Faux : quand les liens durs sont refusés (EPERM, EXDEV, EMLINK, ENOTSUP), le fichier définitif est créé directement ; si
l'écriture échoue, il n'est pas encore dans `definitifs` et le nettoyage le laisse. Essai dans le processus du script
(liens durs refusés ; au troisième fichier, moitié des octets écrite, puis « plus de place ») : code 4, `lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-provisoire-v2.json`
laissé à moitié écrit ; R12 bloque alors toute reprise dans cette SORTIE. Sur un système de fichiers à liens durs, ce chemin
n'est pas pris. Correction : ajouter le chemin à `definitifs` dès la création du fichier, avant d'écrire.

**RSL2-06** — `lire_pilote4_v2.py` l. 1086–1090 et 1126–1129 — mineur (RSL-12).
Une interruption qui tombe après `ecrire_sorties` et avant la ligne d'état fait écrire « lecture non écrite :
interrompue » et « rien n'est laissé à moitié écrit », code 130, alors que les huit fichiers sont écrits et complets (essai
par injection dans le processus du script). Fenêtre étroite. Correction : retenir que l'écriture est faite et le dire.

**RSL2-07** — `LISEZMOI-script-lecture-v2.md` l. 29–32, 75, 163–164 — mineur (documentation).
Inexact : le fichier `test` porte « (iii) » dans le texte de la règle (ii) (« seul (iii) peut séparer… », l. 121–124) et
« deux parts » : du texte, aucune valeur ; l'essai de séparation compare des valeurs décimales, pas les comptes, les
signalements ni la ligne d'état (RSL2-02, RSL2-03) ; « toute erreur en cours retire ce que l'appel a créé » est faux sans
liens durs (RSL2-05). Correction : dire exactement ce que la séparation et l'essai couvrent.

**RSL2-08** — `essais_lire_pilote4_v2.py` l. 462–488, 384–392 et 1228 — mineur (R5).
L'essai de séparation ne cherche, d'une part à l'autre, que des valeurs décimales : il ne peut voir une fuite de comptes, de
signalements ou de ligne d'état, et un essai exige le mélange (RSL2-02). La trace d'audit de l'auteur ne lit, pour
l'événement `open`, que la chaîne du mode (`args[1]`) : une ouverture par `os.open` avec des drapeaux d'écriture lui échappe (la trace de la
relecture lit aussi les drapeaux ; aucune écriture hors de SORTIE n'a été vue, trace système comprise). Correction : des
paires de non-interférence comme celles de la relecture ; lire les drapeaux dans la trace.

## 3. Traitement des constats de la première relecture

| constat | déclaré par l'auteur | vérifié |
|---|---|---|
| RSL-01 | fait | conforme : § 5 aux dossiers réels ; les quatre commandes lancées telles qu'écrites passent (trois interpréteurs) ; le motif de refus d'une liste sans archive renvoie au suffixe |
| RSL-02 | fait | conforme : `-I -B` partout ; drapeau l. 49 ; trace système avec et sans `-B` : 25 écritures, toutes dans SORTIE (trois interpréteurs) ; seuls `from __future__ import annotations` (l. 45) et `import sys` (module interne) précèdent le drapeau : sans effet avec `-B`, et aucune écriture vue sans `-B` ici (cache de la bibliothèque standard déjà présent) |
| RSL-03 | fait | conforme : un tar coupé net avant le dernier membre nécessaire (accepté par la v1) est refusé « fin d'archive absente » ; les deux coupes de l'auteur aussi |
| RSL-04 | fait (refus) | conforme : M + S accepté, M + M' (tentatives 2 et 3, archives distinctes) et S + S' refusés, dossier S à la lignée de M refusé ; noms `v5-3`, `-tentative0`, `s-v2`, à point refusés ; `-tentative1`, que le lanceur ne crée jamais (l. 181), accepté : sans conséquence |
| RSL-05 | fait | conforme ; reste : le fichier `test` d'une relecture « holm-deux » porte le nom de celui de la lecture provisoire (contenu égal à l'heure près ; autre SORTIE, dit au § 5) |
| RSL-06, RSL-07 | gardés | conformes à mes corrections proposées (aucune si la lecture du brief est retenue ; écart déclaré) |
| RSL-08 | sans objet | conforme |
| RSL-09 | fait | fait, mais le compte de signalements mêle `test_final` : RSL2-02 |
| RSL-10 | fait | conforme : récursion du décodeur sur `score-final.json` : « ligne 474 », l'appel `json.loads` du script |
| RSL-11 | fait | conforme (aide sans motif décimal ; nom décimal non recopié : essais de l'auteur rejoués) |
| RSL-12 | fait | conforme pendant la lecture ; message faux après l'écriture : RSL2-06 |
| RSL-13 | non fait (facultatif) | déclaré ; la sortie de chaque appel de décompression du contrôle est bornée à 1 Mio ; le coût en temps de tarfile en flux reste |
| RSL-14 | fait | conforme ; « impossible par construction » est le mot du texte |
| RSL-15 | fait | conforme (plus de tailles) ; reste l'empreinte croisée : RSL2-04 |
| RSL-16 | fait | conforme sur un système à liens durs ; jeu partiel possible sans : RSL2-05 |
| RSL-17 | fait | conforme ; manques de l'essai de séparation : RSL2-08 |

## 4. Ce qui a été vérifié

**Séparation** (outil `outils/artefacts_relecture_v2_sur_v2.py`, trois interpréteurs). Non-interférence : deux courses
qui ne diffèrent que par une part sont lues, et le fichier de l'autre part est comparé champ à champ (JSON) et texte à texte
(Markdown, heure et empreintes ôtées). (a) `test_final` différente (justes, et non-réponses de 3 % à 25 %) : fichiers `test`
identiques hors de l'heure, des empreintes du dossier, de l'archive et de `reponses-lues.json` ; ligne d'état identique en
générations lues et en signalements. (b) Réciproque : fichiers `test_final` identiques hors des mêmes champs. (c) Anomalie
propre à `test_final` : fichier `test` identique, ligne d'état différente (RSL2-02). (d) Entrée écartée d'une tâche de
`test_final` : signalement dans le fichier `test` (RSL2-03). (e) Course S lue avec deux courses M différentes : fichier
`test` de S identique, l'heure à part ; seul `test_final` change. (f) Mots : le fichier `test` ne porte ni « test_final »,
ni « McNemar », ni « Holm », ni la seconde course, ni « provisoire » ; il porte « (iii) » et « objets » (texte des règles).
Noms : le fichier `test` ne porte pas de règle, le fichier `test_final` la sienne (`provisoire`, `holm-deux`,
`holm-quatre`) : aucune valeur. Empreintes croisées : la ligne d'état porte celles des fichiers `test_final` (non
renversables) ; le fichier `test` ne porte aucune empreinte d'un fichier `test_final` ; RSL2-04 pour `reponses-lues.json`.
Valeurs : chaque ligne (i)–(ii), chaque sous-ensemble et chaque test (iii) des deux parts égaux au calcul indépendant de la
relecture (Wilson en décimal, McNemar par la loi binomiale, Holm pas à pas), réponses fabriquées par la relecture ; les
26 vérifications de calcul de la première relecture rejouées sur la v2 : 26 conformes.

**Courses M et S.** Noms et lignées conformes au texte v5 et au lanceur v11. La garde « même course » n'exige pas deux
objets : M + S, même objet, est accepté dans les deux ordres (S puis M, ordre du LISEZMOI : harnais de la relecture ; M
puis S : batterie de l'auteur rejouée) ; elle refuse deux fois la même course (copie sous un autre nom : batterie de
l'auteur ; deux tentatives réelles de M, deux courses S : harnais de la relecture). Holm sur quatre : ajustées égales au
pas à pas refait par la relecture dans l'ordre S puis M ; dans l'autre ordre, égales au calcul de l'auteur, et mêmes
ajustées dans les deux ordres (batterie rejouée). Fichier `test` de S sans rien de M.

**Commandes du LISEZMOI § 5** (l. 113, 121, 132, 140), lancées telles qu'écrites depuis le dossier de la copie, `python3`
remplacé par l'interpréteur essayé, `<R>` et `<BANQUE_DIR>` par l'arbre et la banque synthétiques, et la variable d'essai
des empreintes de la banque définie (banque synthétique ; en réel, la l. 106 la retire et les empreintes du brief
s'appliquent, ce que vérifie l'essai de l'auteur « empreintes par défaut ») : les quatre passent, `-I -B` compris ; noms de
sortie `…-tentative2-test-final-provisoire-v2`, `…-v6-2-s-v1-test-final-holm-quatre-v2`,
`…-tentative2-test-final-holm-deux-v2` ; copie du script inchangée, sans sortie ni cache.

**Écritures.** Pour chaque cas lancé par l'exécuteur de la relecture (tous, sauf les quatre commandes du § 5 et les deux
pannes injectées dans le processus) : instantanés du dossier de travail, de `/tmp` et de `/var/tmp`, dossier courant
resté vide, et trace d'audit (drapeaux compris) dans une SORTIE jumelle : uniquement SORTIE. Trace système de la commande
de production : 25 écritures (dossier, huit provisoires, huit liens, huit retraits), toutes dans SORTIE, avec et sans
`-B`, sous les trois interpréteurs. Aucun fichier provisoire laissé ; aucun cache dans le noyau (`essaim_m3/__pycache__`
et `essaim_m3/noyau/__pycache__` absents à la fin).

**Interpréteurs.** Batterie de l'auteur et artefacts de la relecture : mêmes issues sous 3.11.17, 3.12.3 et 3.13.17.

## 5. Essais rejoués et ajoutés

| essai | interpréteur du script | issue | journal |
|---|---|---|---|
| batterie v2 de l'auteur, `--mutations` | 3.13.17 (venv) | 9 sains sur 9, 58 artefacts sur 58, 22 mutations sur 22 | `journaux/rejeu-batterie-auteur-v2-mutations-py3.13.17-v1.log` |
| batterie v2 de l'auteur | 3.11.17 ; 3.12.3 ; 3.13.17 (`python3`) | 9 sur 9 et 58 sur 58, chaque fois | `journaux/rejeu-batterie-auteur-v2-py*-v1.log` |
| calculs indépendants de la première relecture, sur la v2 | 3.13.17 (venv) | 26 sur 26 | `journaux/calculs-independants-sur-v2-v1.log` |
| artefacts de la relecture : 4 sains, 12 artefacts (dont 6 de séparation) | 3.11.17 ; 3.12.3 ; 3.13.17 | sains 4 sur 4 ; artefacts 10 sur 12, les deux en échec étant les fuites RSL2-02 et RSL2-03, chaque fois | `journaux/artefacts-relecture-v2-py*-v1.log` |
| pannes injectées dans le processus du script (`--en-processus`) | 3.13.17 | jeu partiel laissé (RSL2-05) ; message après écriture (RSL2-06) | `journaux/artefacts-relecture-v2-py3.13.17-v1.log` (il compte 10 artefacts sur 13 : la panne RSL2-05 y est le treizième ; l'observation RSL2-06 y est marquée « OK » : elle consigne sans juger) |
| trace système de la commande de production | les trois, avec et sans `-B` | 25 écritures, toutes dans SORTIE | `journaux/strace-lecture-v2-v1.txt` |
| renvois du rapport (lignes, empreintes, citations, lanceur v10 contre v11) | — | tous conformes | `journaux/verification-renvois-rapport-v1.log` |

Dans ces journaux, « ÉCHEC » d'un artefact de la relecture veut dire : défaut du script constaté. Le journal
`mise-au-point-harnais-v2-1.log` garde un faux signal de fuite dû au harnais (la paire (a) changeait aussi la probabilité de
justes de `test`) ; corrigé, `mise-au-point-harnais-v2-2.log` et les journaux finaux montrent la non-interférence des
fichiers.

## 6. Ce que la relecture n'a pas pu vérifier ; interdits

Non vérifiable ici : l'archive et la banque réelles (interdites) ; que le code du dépôt soit celui de `8e5e2f7b` (sans
`git`) ; le `python3`, le GNU tar et le système de fichiers de SORTIE chez session-depot (liens durs : RSL2-05) ; le
suffixe réel du dossier de la course S. Interdits tenus : aucun fichier de données de la banque, aucune archive ni pièce
d'un pilote réel, aucun dossier `donnees/`, `runs/`, `diag/`, `pilotes/` ; aucun `git`, sous-agent, réseau ni clé ; ni
lanceur, ni noyau, ni organisme exécutés (fonctions pures du noyau importées sans cache) ; écrit seulement sous
`/var/tmp/relecture-script-lecture-pilote4-v2/` (les essais de l'auteur y créent et effacent leurs dossiers dans `copie/`).

## 7. Pièces

Sous `/var/tmp/relecture-script-lecture-pilote4-v2/` : ce rapport et son compagnon ; `journal-essais-relecture-v2-sur-v2.log`
(`9826195dd0c82ade823495aed984a784696f3e700af9b3e06776ade25c050240`, recopie de tous les journaux, chacun sous son nom et
son empreinte) et son compagnon ; `EMPREINTES-relecture-v2-sur-v2.txt`
(`d9abed800f96648b3688cb8682b6cdac929c1f0cfb619e370146802e2387937f`, journaux et outils) et son compagnon ; `outils/`
(`artefacts_relecture_v2_sur_v2.py` `b559a9c6…` ; fabrication reprise de la première relecture, à l'octet, `9d6b65d7…` ;
trace `434d6311…` ; `calculs_independants_sur_v2.py` `9c5b1627…`) ; `journaux/verification-renvois-rapport-v1.log`
(`a3e1ac19baf652cb98db9f2204356f5028d3db4eb18b8cd057bc8dc9b0ef9339`) et son compagnon ; la première écriture de ce
rapport (`rapport-relecture-script-lecture-v2-sur-v2.md`, `d8fe59c1…`) et son compagnon, gardés ; `copie/` inchangée.
Données synthétiques seulement ; dossiers de travail effacés.
