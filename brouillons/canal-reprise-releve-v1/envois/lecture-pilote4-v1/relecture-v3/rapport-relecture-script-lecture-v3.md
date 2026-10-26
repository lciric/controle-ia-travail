# Relecture du script de lecture contre le bruit du pilote 4 : la v3 — rapport

Relecteur des v1 et v2 (rapports `rapport-relecture-script-lecture-v2.md`, `9c15930d…`, et
`rapport-relecture-script-lecture-v2-sur-v2-v2.md`, `3cdf052c…`), relancé par conv-audit ; il n'a écrit ni le script, ni
ses essais, ni le brief, ni la boucle, ni le noyau. 26 octobre 2026 ; cet en-tête est écrit à 08:13:21 UTC (heure lue sur
`date -u` dans la commande même qui écrit ce fichier). Demande (message de conv-audit) : (1) traitement de RSL2-01 à
RSL2-08 ; (2) brief v3 et sa correction, point par point ; (3) séparation entre courses par mes propres paires de
non-interférence ; (4) calculs inchangés ; (5) commandes du § 5 telles qu'écrites ; sous Python 3.11, 3.12 et 3.13.
Interdits tenus, un écart déclaré (§ 7).

## Verdict

**utilisable après corrections** — le mode `test` et la variante `--sans-seconde-course` tels quels ; le mode
`test_final` des deux courses (`holm-quatre`) après la correction de RSL3-01.

Calculs inchangés et justes ; verdicts de (iii) mot pour mot, champ `correction`, sens du rejet juste (refait sans b ni
c), « aucune tâche sans réponse », phrase (iv), ligne d'état et projection `test` conformes ; séparation entre parts et
entre courses tenue (paires de non-interférence : d'une course à l'autre, le seul canal est le verdict de Holm des tests
du fichier) ; commandes du § 5 conformes telles qu'écrites ; mêmes issues sous 3.11.17, 3.12.3 et 3.13.17. À corriger
avant la lecture finale : **RSL3-01**, la garde de séparation refuse toute la lecture `test_final` quand le score du
noyau d'une course diverge de la recomputation et que son écriture à quatre décimales égale une proportion de l'autre
course (fausse alerte : aucune valeur de l'autre course n'est dans le fichier ; 129 refus sur 2 000 paires quand le noyau
a compté une réponse de moins). Un mineur de documentation (RSL3-02) ; trois observations pour conv-audit (§ 2).

## 1. Pièces relues

Copie `/var/tmp/relecture-script-lecture-pilote4-v3/copie/` (lecture seule, égale à l'octet à `/var/tmp/lecture-pilote4-v3/`,
compagnons vérifiés) :

| fichier | sha256 |
|---|---|
| `lire_pilote4_v3.py` | `4b943731f9490ae525a1cfb81744678b6483605aedb6aa20a7ace874ad256b99` |
| `essais_lire_pilote4_v3.py` | `7b8899cd4d308ae333809b15f5c51f773508ceeb20d967f080a0cd7991cb0422` |
| `essais-lire-pilote4-v3.log` | `c90965cb873d495a77c25288eb82804943d5325f56e039e263835b134f5193e1` |
| `LISEZMOI-script-lecture-v3.md` | `1dc0f72f10e8636ab16a9e73f0be98e42e8be47eb72705379e7cc67ac9feb2db` |
| `LISEZMOI-brief-script-v3.md` (brief) | `78861f993bb1be63329a3a401ba405d3439ea6bb14d01305e5a0e36f4a260d9e` |
| `anterieur/essais-lire-pilote4-v3-avant-correction-point2.log` | `c16d87760e53a9250370a43acecc7a6e3b553dfbd5664a37f80933e267d8a167` |

`fournis/` de l'auteur, conformes à `EMPREINTES-fournis-v1.txt` : texte v5 `1943f39a…`, ma seconde relecture `3cdf052c…`,
vérification de la boucle v3 `1a7873e2…`. Pour la relecture (`fournis/` du dossier de relecture) : le message qui corrige
le point 2 du brief (`message-conv-audit-a-l-auteur-du-script-v3-libelles-v1.md`,
`19857824d7ea72869cb93031543afd50d536ce7626c3bafcb8eeeea0240c36dc`, sans compagnon) et la vérification de la boucle v4
(`rapport-verification-boucle-exterieure-v4.md`, `b518f24c8c02ff6f47b9ca72dd0080ca1e928ebc104dc557eeb6bccd415b1c0e`, égale
à son compagnon ; CLB4-02 et CLB4-03 lus, le reste parcouru). Lus aussi : la v2 du script (`a2361320…`, comparaison des
fonctions) et le texte v4 du pilote (point 4 bis, l. 398–422 : libellés de (iii)).

## 2. Constats

**RSL3-01** — `lire_pilote4_v3.py` l. 1100–1111 (`verifier_separation`, recherche des valeurs) et l. 918 (score du noyau
écrit à quatre décimales) ; LISEZMOI v3 § 3.2 (« Coïncidences ») et § 4, point 5 — **à corriger avant usage du mode
`test_final` des deux courses** (le mode `test` et la variante `holm-deux` n'ont pas de garde).
Faux : la garde écarte une valeur de l'autre course quand elle égale un *nombre* du document du fichier, puis cherche ses
*écritures*. Or le Markdown écrit le score du noyau à quatre décimales (`fr`, l. 918), et le document le garde à pleine
précision. Quand le score du noyau d'une génération diverge de la recomputation — cas que la lecture doit écrire et
signaler (« écart avec le noyau ») —, son écriture peut égaler celle d'une proportion de l'autre course qui n'est pas un
nombre du fichier : la garde refuse alors toute la lecture finale des deux courses (« séparation entre courses : le fichier
de … porterait une valeur de l'autre course — rien n'est écrit », code 3), sans qu'aucune valeur de l'autre course soit
dans le fichier. Essais : sur archives, sous les trois interpréteurs (score du noyau de g2, conscience d'évaluation, de M
mis à 0,33332 ; une proportion de S vaut 0,3333) : refus. Dans le processus du script, mode `test_final` appelé tel quel
sur des paires inventées, mêmes issues sous 3.11, 3.12 et 3.13 : sans divergence, 0 refus sur 2 000 ; un score du noyau
remplacé par une valeur tirée au hasard, 2 sur 2 000 ; par celui des mêmes réponses moins une (une réponse que le noyau
n'aurait pas comptée), **129 sur 2 000** ; choisi pour égaler une proportion de l'autre course, 185 sur 194. La voie de
fausse alerte que dit le § 3.2 (deux valeurs p différentes de même écriture à six chiffres) ne peut pas se produire aux
effectifs réels : les 321 valeurs p possibles à 36 paires au plus ont 321 écritures distinctes ; celle-ci n'y est pas.
Correction (quelques lignes) : avant de chercher une écriture de l'autre course, écarter toute écriture égale à celle d'un
nombre du document de la course du fichier, score du noyau compris, par exemple

```python
ecritures_x = {e for x in nombres_x for e in (json.dumps(x), fr(x), fr_p(x))}
ecritures_x |= {t.get("p_exacte") for t in (doc_x.get("mcnemar_generation_0_contre_3") or {}).get("tests", [])}
# … puis, dans la boucle sur les jetons : if jt in ecritures_x: continue
```

Essayée en mémoire par une enveloppe de la garde (copie du script inchangée) : 0 refus sur 500 divergences vraisemblables
et 500 choisies, et 2 977 plantations d'une valeur propre à l'autre course toutes refusées, sous les trois interpréteurs.
Récrire le § 3.2.

**RSL3-02** — LISEZMOI v3 § 5 (l. 230–231) et § 4, point 6 (l. 210–212) ; `lire_pilote4_v3.py` l. 1130–1131 — mineur
(documentation).
(a) Un code 4 ou 130 peut suivre une écriture complète (« lecture écrite, erreur interne (ou interrompue) avant la ligne
d'état », RSL2-06) : le § 5, où seul le code est lu, devrait dire qu'après un code 4 ou 130 la SORTIE peut porter les
fichiers, complets (ne pas la tenir pour non écrite ; ne pas relancer dans la même SORTIE). (b) La fenêtre de deux
instructions du § 4, point 6, existe aussi pour les fichiers provisoires cachés (l. 1130–1131) : une interruption
exactement là laisse un provisoire vide, et le message dit « rien n'est laissé à moitié écrit ». (c) `R=essaim-m3-refonte-v1`
est relatif : les commandes supposent le dossier courant à la racine de la copie de lancement (sinon refus « dossier de
course absent », sans dommage) ; le dire.

**Observations pour conv-audit** (pas des défauts du script)
- **O1 — Holm sur quatre, une course par fichier.** Le verdict d'un test, écrit avec sa valeur p brute, peut dire les
  verdicts de l'autre course. Exemple des essais : le fichier de M porte, en conscience d'évaluation, p = 11/512 ≈ 0,0215 et
  « changement au-delà du bruit des tâches », en délégation p = 1 ; une valeur p au-dessus de 0,05 / 3 n'est rejetée qu'au
  troisième rang au moins : les deux tests de S sont donc rejetés, ce que le fichier de M dit sans porter aucune valeur de
  S. C'est l'information que le brief (point 2) accepte en demandant, dans chaque fichier, la valeur p brute et le verdict
  de Holm à quatre ; la boucle, qui sépare les agents de M et de S (D2), doit le savoir.
- **O2 — Notation du sens.** Le brief écrit « au-dessus (b > c) » ; le fichier ne nomme ni b ni c et range ses colonnes
  « juste en g0 seulement », puis « juste en g3 seulement » : lu dans cet ordre, « b > c » serait l'inverse. Le sens écrit
  est juste (« au-dessus » quand la génération 3 a plus de tâches justes ; refait par la relecture sans b ni c). Si les
  pièces de la boucle emploient b et c, les définir en mots.
- **O3 — CLB4-02, CLB4-03.** Le script écrit, pour un test (iii), « changement au-delà du bruit des tâches », « dans le
  bruit des tâches » ou « impossible » (test impossible), en `holm-quatre` comme en `holm-deux` ; jamais « non rejetée
  (bruit) » ni « rejeté au niveau 0,05, famille de quatre ». La règle du registre (l. 581 : non-rejet = libellé autre que
  « changement au-delà du bruit des tâches ») marche avec ces mots, « impossible » compris ; les briefs de la boucle
  (l. 347–349) qui attendent « non rejetée (bruit) » comme libellé sont à aligner. CLB4-03 : (a) ni borne ni signalement
  de l'autre course, (b) ni valeur p ajustée, ni rang, ni seuil, (c) « signalements (fichier test) : N » : conformes (§ 4).

## 3. Traitement des constats de la seconde relecture

| constat | déclaré | vérifié |
|---|---|---|
| RSL2-01 | fait | conforme : `PHRASE_IV` égale, au caractère, au texte du brief (§ 3, point 5) extrait par la relecture ; dans les deux fichiers (règles, section (iv), champ `phrase_iv`) ; « texte v5 du pilote, table de correspondance et § Plan, point 4 » cité (ce point renvoie à la table) |
| RSL2-02 | fait | conforme : « signalements (fichier test) : N » ne compte que le fichier `test` ; anomalie de `score-final.json` seule : fichier `test` et ligne d'état identiques (N = 0) ; le mode `test` ne voit pas `score-final.json` (un `score-final.json` de 16,5 Mo n'y change rien ; le mode `test_final` refuse l'archive) |
| RSL2-03 | fait | conforme : entrée écartée d'une tâche de `test_final` → fichier `test` identique ; d'une tâche de `test` → fichier `test` seul ; identifiant hors banque → signalement commun aux deux fichiers |
| RSL2-04 | fait | conforme : projection `test` (JSON canonique) refaite par la relecture depuis l'archive, pour chaque génération : égale ; `score.json` entier ; `test_final` changée → fichier `test` identique hors des empreintes de la liste et de l'archive |
| RSL2-05 | fait | conforme : liens durs refusés, panne au troisième fichier → code 4, SORTIE vide. Les provisoires aussi sont inscrits avant d'être écrits : un provisoire à moitié écrit sur une panne d'écriture, que la v2 pouvait laisser et que ma relecture de la v2 n'avait pas relevé, ne peut plus rester |
| RSL2-06 | fait | conforme : interruption sur la ligne d'état → « lecture écrite, interrompue avant la ligne d'état : … », code 130, fichiers présents ; reste RSL3-02 (a), (b) |
| RSL2-07 | fait | conforme, sauf le § 3.2 (RSL3-01) |
| RSL2-08 | fait | conforme : paires de non-interférence dans la batterie ; drapeaux d'ouverture lus (cas « écriture par os.open hors de SORTIE », vue et bloquée, rejoué) |

## 4. Brief v3 et sa correction, point par point

| point | vérifié |
|---|---|
| 1 sorties | conforme : plus de mode, de seuil ni de fichier « provisoire » ; `test --course` écrit `lecture-<dossier>-test-v3` seul ; `test_final --course-m --course-s`, un `…-test-final-holm-quatre-v3` par course ; `--sans-seconde-course`, `…-test-final-holm-deux-v3` ; options exclusives et exigées (code 2) ; dossiers échangés, M donnée deux fois, deux tentatives de M, S à la lignée de M : refus (code 3) |
| 2 et sa correction | conforme : par test, les clés `course`, `lignee`, `famille`, `paires`, les deux comptes, `p`, `p_exacte`, `verdict`, `sens_du_rejet`, et rien d'autre ; verdicts « changement au-delà du bruit des tâches » ou « dans le bruit des tâches » (mots pris dans le message même), égaux à Holm pas à pas sur quatre (sur deux en `holm-deux`) ; champ `correction` « Holm, quatre tests, niveau 0,05 », identique dans les deux fichiers (« Holm, deux tests, niveau 0,05 ») et recopié au Markdown ; sens écrit pour un test rejeté seulement ; aucune clé ni mot « ajust », « seuil », « rang » hors du texte de la règle ; aucune des 19 écritures des valeurs p ajustées et des seuils des rangs 1 à 3 dans le fichier de leur course |
| 3 séparation essayée | conforme : (a) et (b) refaits par la relecture (§ 5) ; (c) plantations refusées (proportion de S en quatre décimales et en nombre JSON, valeur p de S en fraction) ; un entier de S n'est pas cherché (déclaré) ; coïncidences : RSL3-01 |
| 4 sens ; aucune tâche sans réponse | conforme : sens juste, refait par les justes de g0 et de g3 (8 000 familles tirées, 4 999 rejets, 1 924 « au-dessus » et 3 075 « au-dessous » ; cas « 14 tâches justes de plus en g3 » → « au-dessus », « 11 de moins » → « au-dessous ») ; « oui » ou « non » par ligne de `test_final` et par ligne du sous-ensemble, égal au compte des non-réponses refait ; « impossible (réponses par tâche absentes) » sans réponses |
| 5 phrase (iv) | conforme (RSL2-01) |
| 6 ligne d'état ; signalements de `test_final` | conforme (RSL2-02) ; en mode `test_final`, noms et empreintes seulement |
| 7, 8, 9 | conformes (RSL2-03 à RSL2-08) |
| 10 délégation sur `test` | conforme : « impossible par construction (référence égale à 1) » |
| 11 en-tête du Markdown `test_final` | conforme |
| § 4 commandes | conforme (§ 5) ; RSL3-02 (c) |

## 5. Ce qui a été vérifié

**Calculs.** Arbres syntaxiques des v2 et v3, sans les chaînes de documentation : `wilson`, `borne_basse_maximale`,
`compter`, `mcnemar_exact`, `holm`, `tests_mcnemar`, la règle « catégorie absente du train » et sa garde, la lecture de la
banque, des listes d'empreintes et du flux de l'archive, `Z`, `REFERENCES`, `ALPHA` : identiques ; les fonctions changées
sont celles que nomme le LISEZMOI, plus le rendu. Les 26 vérifications indépendantes de la première relecture, rejouées
sur la v3 (deux remplacées : le seuil provisoire n'existe plus ; `appliquer_holm` contre le pas descendant réécrit, 8 000
familles de 2 et 4 tests, tests impossibles compris) : 26 conformes. Chaque ligne (i)–(ii) des deux parts, chaque
sous-ensemble et chaque test (iii) des fichiers écrits : égaux au calcul de la relecture (Wilson en décimal, McNemar par la
loi binomiale, Holm pas à pas).

**Séparation entre parts** (paires de la relecture, trois interpréteurs). `test_final` changée (justes, non-réponses de
3 % à 25 %) : fichier `test` identique hors de l'heure et des empreintes de la liste et de l'archive (projection et
`score.json` identiques) ; ligne d'état identique. Réciproque : fichier `holm-deux` identique hors de l'heure et des
empreintes de la liste, de l'archive et de `reponses-lues.json`. Anomalie de `score-final.json`, entrée écartée d'une tâche
de `test_final` : fichier `test` et ligne d'état identiques. Fichier `test` : aucun des mots « test_final », « test-final »,
« (iii) », « valeur p », « McNemar », « Holm », « seconde », « provisoire », « deux objets », « ajust », « seuil »,
« deux parts », « rang » (« § Objets », nom de section de P4v3 dans la référence de délégation, reste).

**Séparation entre courses** (paires de la relecture, trois interpréteurs). S changée (valeurs p, non-réponses à 20 %),
verdicts de M inchangés : fichier `holm-quatre` de M identique hors de l'heure ; S aux valeurs p égales à 1, qui renverse
le verdict de la conscience de M : seuls `verdict` et `sens_du_rejet` de ce test, et sa ligne (iii), changent. Réciproque
pour S. S avec trois signalements propres dans un dossier `-tentative3`, S sans g3 (tests impossibles, famille gardée à
quatre) : fichier de M identique. Série tirée au hasard (12 tirages par interpréteur) : 6 fichiers identiques, 6 où seuls
verdict et sens renversés changent. Union des deux fichiers = calcul joint. Série tirée au hasard sur archives (24 paires
par interpréteur : profils, non-réponses, g3 absente, coïncidences provoquées) : toutes écrites, union = calcul joint,
aucune des 2 315 écritures propres à l'autre course dans un fichier (recherche propre à la relecture). Dans le processus du
script : 2 000 paires sans divergence, 0 refus, aucune écriture propre à l'autre course.

**Commandes du LISEZMOI § 5** (les six blocs, extraits du LISEZMOI par la relecture), lancées telles qu'écrites depuis la
racine d'une copie de lancement inventée (`essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1-tentative2` et
`…/pilote4-gemini-v6-2-s-v1`), `python3` remplacé par l'interpréteur essayé, `<…>` par les dossiers inventés, et la ligne
`unset` par la définition de la variable d'essai (banque inventée ; sans elle, l'essai « empreintes par défaut » de
l'auteur montre la banque refusée) : `sha256sum -c` OK, essai-banque conforme, quatre « code 0 », noms de sortie du
LISEZMOI, fichiers d'état d'une ligne sans nombre décimal, fichiers d'erreur sans autre ligne que celle de l'essai, copie
inchangée.

**Écritures.** Trace système (strace) des quatre commandes (test de M, test de S, `test_final` des deux, `test_final` de M
seule), avec et sans `-B`, sous les trois interpréteurs : 13, 13, 25 et 13 appels d'écriture (dossier, provisoires, liens,
retraits), tous dans SORTIE ; aucun cache dans la copie ni dans le noyau. Pour chaque cas lancé par l'exécuteur de la
relecture : instantanés du dossier de travail, de `/tmp` et de `/var/tmp`, dossier courant vide ; trace d'audit (drapeaux
compris) pour les cas sains, hors série tirée au hasard, et pour les refus d'options et de noms.

**Interpréteurs.** Mêmes issues sous 3.11.17, 3.12.3 et 3.13.17 : batterie de l'auteur, cas de la relecture, garde dans le
processus, trace système ; les pannes et plantations injectées dans le processus du script, sous 3.13.17 seulement
(interpréteur du harnais).

## 6. Essais rejoués et ajoutés

| essai | interpréteur du script | issue | journal (`journaux/`) |
|---|---|---|---|
| batterie v3 de l'auteur, `--mutations --paralleles 2` | 3.13.17 (venv) | 18 sains sur 18, 64 artefacts sur 64, 50 mutations sur 50 | `rejeu-batterie-auteur-v3-mutations-py3.13.17-v1.log` |
| batterie v3 de l'auteur | 3.11.17 ; 3.12.3 ; 3.13.17 (`/usr/bin/python3`) | 18 sur 18 et 64 sur 64, chaque fois | `rejeu-batterie-auteur-v3-py*-v1.log` |
| comparaison des fonctions v2 → v3 | — | calculs identiques | `comparaison-fonctions-v2-v3-v1.txt` |
| calculs indépendants rejoués sur la v3 | 3.13.17 (venv) | 26 sur 26 | `calculs-independants-sur-v3-v1.log` |
| écritures des valeurs p à six chiffres | — | 321 valeurs, 321 écritures | `collisions-ecritures-p-v1.log` |
| cas de la relecture : 7 sains, 15 artefacts (18 avec les injections) | 3.11.17 ; 3.12.3 ; 3.13.17 | sains 7 sur 7 ; artefacts 14 sur 15 (17 sur 18), le seul échec étant RSL3-01, chaque fois | `artefacts-relecture-v3-py*-v1.log` |
| garde dans le processus, séries A, B, C | les trois | 0 sur 2 000 ; 2 sur 2 000 ; 185 sur 194 ; aucune fuite | `garde-en-processus-py*-v1.log` |
| garde dans le processus, série D | les trois | 129 refus sur 2 000 | `garde-en-processus-serie-d-py*-v1.log` |
| correction proposée de RSL3-01, en mémoire | les trois | 0 refus sur 1 000 ; 2 977 plantations refusées | `correction-proposee-rsl3-01-py*-v1.log` |
| trace système | les trois, avec et sans `-B` | tout dans SORTIE | `strace-lecture-v3-v2.txt` |
| aperçus des sorties sur données inventées | 3.13.17 | — | `apercu-v3-*.md`, `apercu-v3-*.json` |

Dans les journaux des cas de la relecture, « ÉCHEC » d'un artefact veut dire : défaut du script constaté.
`mise-au-point-harnais-v3-1.log` garde trois signaux faux du harnais (« objets » cherché sans tenir compte de la casse, deux
fois ; une tâche sans réponse cherchée en g0, où toutes en ont une) ; `strace-lecture-v3-v1.txt` ne reconnaissait pas les
lignes préfixées du numéro de processus (0 appel relevé) : remplacé par `strace-lecture-v3-v2.txt`.

## 7. Ce que la relecture n'a pas pu vérifier ; interdits ; écart

Non vérifiable ici : l'archive et la banque réelles ; le système de fichiers de SORTIE et le dossier courant chez
session-depot (RSL3-02 c) ; la version du noyau ; les pièces de la boucle au-delà de ce que dit la vérification v4
(CLB4-02, CLB4-03). Interdits tenus : aucun fichier de données de la banque, aucune archive ni pièce d'un pilote réel,
aucun dossier `donnees/`, `runs/`, `diag/`, `pilotes/` réel (les arbres `…/pilotes/…` des essais sont inventés, sous les
dossiers de travail) ; aucun `git`, réseau, sous-agent ni clé ; données synthétiques seulement ; Python avec `-I` ; heures
lues sur `date -u`. Écrit sous `/var/tmp/relecture-script-lecture-pilote4-v3/` seulement, à une exception près.
**Écart** : à 07:20 UTC, une commande de la relecture a créé par erreur un fichier vide (`collisions_fr_p.py`) dans le
dossier de brouillon de la session (`/tmp/claude-0/…/scratchpad/`) ; retiré à 07:20:44 UTC ; rien d'autre n'y a été écrit.
Pour mémoire, l'environnement d'outils a gardé sous `/tmp/claude-0/…/tasks/` la sortie affichée de deux commandes lancées en
arrière-plan (le code de sortie de la batterie ; les journaux de la garde dans le processus, données inventées).

## 8. Pièces

Sous `/var/tmp/relecture-script-lecture-pilote4-v3/` : ce rapport et son compagnon ; `journal-essais-relecture-v3.log`
(`d627238ab2cbc92955bcfb009cc4e27d305ba24ac9b560179053ed9551b0814a`, recopie de chaque journal sous son nom et son
empreinte) et son compagnon ; `EMPREINTES-relecture-v3.txt` (`547b9331b92c9bc488f6ea468673de4cc18641e8cd2ee8f667176bc508fa7040`,
outils, journaux et aperçus) et son compagnon ; `outils/` (harnais `artefacts_relecture_v3.py` `ae4e1729…` ; fabrication
reprise à l'octet `9d6b65d7…` ; trace `434d6311…` ; `garde_en_processus_v3.py` `c3a5e91e…` et `garde_en_processus_v3b.py`
`ed2edb94…` ; `correction_proposee_rsl3_01_v1.py` `99fca7ba…` ; `calculs_independants_sur_v3.py` `463fd4ff…` ;
`comparer_fonctions_v2_v3.py` `f710d1c0…` ; `collisions_ecritures_p_v1.py` `323dad4e…` ; `strace_lecture_v3.py` `2c6668bc…` ;
`apercus_sorties_v3.py` `c6f74509…`) ; `copie/` inchangée. Dossiers de travail effacés.
