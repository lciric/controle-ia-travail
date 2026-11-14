# Contre-lecture de la commande de reprise au compte 2 (verdict de P3-bis après perte de la session hôte) — v1

- **Objet** : `docs/procedures/P3-bis-commande-compte-2-v1/commande-reprise-verdict-p3bis-compte-2-v1.md`
  (`fdc043c26547…`, égale à son compagnon), sa répétition `repetition_reprise_jouet_v1.sh` (`f70bae22…`) et sa sortie
  (`98f4f9cd…`) ; R-2696 (mot de Lazar), R-2699 (versement et quatre décisions de la mère).
- **Contre-lecteur** : sous-agent neuf de la session mère, **modèle B** (autre que le modèle A du rédacteur ; identités
  dites en conversation seulement, R-2598), le même que pour la commande d'ouverture v1 ; du 2026-11-14T10:10:43Z au
  2026-11-14T10:16:05Z (heures relevées par `date -u`). Ni lecteur ni auteur du verdict.
- **Lu** : la commande de reprise en entier ; le script de répétition et sa sortie ; la commande d'ouverture v2
  (`04ea3325…`) aux passages qui fixent l'état de la branche (sections 11 et 13) ; le module de S (`4a54a437…`) :
  `lire_paquets`, `extraire`, `inscrire`, `ouvrir`, `relire_run`, `lire_prealables`, `date_de_la_mise_en_paquet`,
  `exposer_issue` ; le texte scellé de P3-bis, l. 1981-1983 ; la consigne du lecteur, sections 2, 3 et 7 ; R-2690 à R-2699.
- **Non fait** : aucun appel de `ouvrir` ; aucun paquet ouvert ; rien récupéré de `calcul/p3bis-reel-v2` ; aucun fichier
  de la liste des interdits.
- **Sigles** : comme la contre-lecture de la commande d'ouverture ; « reprise, l. » = le fichier contre-lu ; « v2, l. » =
  la commande d'ouverture version 2.

## 0. Verdict

**Prête après corrections.** Aucun constat bloquant, deux majeurs, tous deux sur la question (2) : le « constat de
perte par programme » n'établit pas la perte. Il établit seulement « ouverture poussée, aucun verdict poussé », état que
partagent une session perdue, une session **vivante** dont le lecteur travaille encore, et une session qui a **rendu
un arrêt**. Le second cas est démontré sur le jouet. Les corrections R1 et R2 ferment les deux.

Sur les quatre autres questions, la commande tient : elle ne peut ni écrire au journal ni rouvrir ; les paquets sont
vérifiés à l'égalité, trois fois ; l'isolement est tenu ; l'écart est celui de R-2696, étendu des seuls points que la
mère a tranchés en R-2699.

## 1. Ce que j'ai rejoué

| contrôle | résultat |
|---|---|
| Empreintes des trois pièces contre leurs compagnons et contre la table (reprise, l. 25-27) | égales |
| Répétition rejouée, 2026-11-14T10:11:56Z → 10:12:50Z | « BILAN : 24 conformes sur 24 », « RÉPÉTITION : TOUT CONFORME » ; empreinte des huit blocs `575ecdd1…5ef6f3`, celle de l'annexe B ; dépôt donné inchangé, aucun journal créé |
| Crochet `garde_calcul.py` sur le texte de chacun des huit blocs ; `bash -n` | les huit passent ; syntaxe saine |
| Renvois au module de S (reprise, l. 31-40, 256-257) | exacts : l. 205-213, 503-535, 851-872, 1237-1259, 1262-1273, 1286-1287, 1304, 1308, 1306-1307, 1319-1320 |
| Texte scellé, l. 1981-1983 (reprise, l. 41-44) | recopié à l'octet |
| **Artefact ajouté par moi** : même répétition, où la branche de l'ouverture porte en plus un fichier de `registres-provisoires/` (ce que la v2 pousse après un arrêt du lecteur) | le bloc 2 imprime « conforme : perte établie (ouverture poussée, aucun verdict) » : **faux positif démontré** (constat M1) |
| Couple proposé en R1, sur un dépôt d'essai (branche au journal seul ; branche au journal plus une passation ; `main` avancé et journal déjà recopié dans `main`) | journal seul : permis ; avec passation : arrêt |

## 2. Réponses aux cinq questions

### 2.1 La reprise peut-elle écrire au journal ou rouvrir ? Non

- Le journal n'est écrit que par `inscrire` (module, l. 851-872), appelée à deux endroits seulement, tous deux dans
  `ouvrir` (l. 1304 et 1308). Le bloc 4 n'appelle que `lire_paquets`, `extraire`, `lire_prealables` et
  `date_de_la_mise_en_paquet` : quatre fonctions qui lisent (la dernière lance un `git log` sur le clone des paquets,
  l. 1230). Le bloc 7 appelle `exposer-issue`, qui lit (l. 1325-1353).
- `lire_paquets` lève `RefusOuverture` sur un défaut sans rien écrire : hors de `ouvrir`, personne ne rattrape ce refus
  pour le journaliser. L'artefact « morceau altéré » de la répétition le montre : arrêt, rien de redéplié.
- Le bloc 4 prend en plus l'empreinte du journal avant et après, et la répétition vérifie le même blob.
- Aucune seconde ouverture n'est possible de toute façon (`deja-ouverte`, l. 1142-1144) ; la commande interdit `ouvrir`
  et le redit à la section 4.

### 2.2 Le constat de perte est-il sûr ? Non, en l'état (M1, M2)

Le bloc 2 (reprise, l. 158-173) vérifie : branche et journal présents, une seule ligne d'ouverture, la dernière, en mode
`pleine`, à l'appui et au paquet attendus ; aucun fichier de verdict sur la branche ni sur `main` ; aucune ligne
`VERDICT-P3BIS` ; journal de `main` absent ou identique. Tout cela est juste, et nécessaire. Ce n'est pas suffisant :

- **session qui a rendu un arrêt** : selon la v2 (l. 657-658), sur un rapport « STATUT : arret … » du lecteur, la
  session ne commite aucun verdict mais joue le bloc 13, qui pousse le journal provisoire et la passation. La branche
  porte alors une ouverture et aucun verdict ; le bloc 2 dit « perte établie ». Ce cas est un nœud de Lazar déjà ouvert
  (un arrêt du lecteur), pas une perte ;
- **session vivante** : entre la poussée du journal (v2, bloc 9) et celle du verdict (bloc 12), la session d'origine ne
  pousse rien pendant que son lecteur travaille. Vue du dépôt, elle est indiscernable d'une session perdue. Aucun
  programme ne peut trancher ; seul Lazar le sait.

### 2.3 Mêmes paquets, vérifiés à l'égalité ? Oui

Trois contrôles indépendants, tous à l'égalité entière : (i) le paquet des lectures contre la constante de R-2684, contre
son compagnon et contre la ligne du journal (bloc 2, l. 165 ; bloc 3, l. 243-245) ; (ii) l'empreinte de l'index du second
paquet contre celle de la ligne (l. 164-167, 246-247) ; (iii) la cellule rendue par `lire_paquets` contre la cellule de
la ligne (bloc 4, l. 272-274), `relire_run` ayant exigé que les morceaux réunis égalent l'index (module, l. 528-529). La
tête `2aaaaf87…` est exigée entière. L'extraction de la seconde empreinte par `awk` (l. 164) est revalidée par le motif
entier de la ligne (l. 165) et par sa forme (l. 167).

### 2.4 Isolement du compte 2 et du lecteur neuf : tenu

- Aucun fichier de T0.7 n'est touché, pas même par empreinte : la garde n'étant pas appelée, ni le texte de T0.7 ni les
  deux compagnons ne servent ; `lire_prealables` lit les lignes du registre sans hacher le fichier qu'elles citent.
- Le lecteur reçoit les mêmes pièces que sous la v2, à une différence près, déclarée : `sortie-de-la-garde-reconstituee-v1.txt`
  à la place de `sortie-de-la-garde-v1.txt` (décision 1 de R-2699). Le fichier est au bordereau, donc dans ce que la
  consigne lui permet de lire.
- Rien de la session perdue n'entre : la branche de reprise part de la tête de la branche d'ouverture, qui ne porte que
  le journal (une fois R1 appliquée, c'est vérifié).
- La seule lecture que l'hôte fait dans le verdict est un `grep -q` d'une chaîne fixe (l. 381), sans affichage : déclarée.
- Réserves : m3, m5.

### 2.5 L'écart est-il exactement celui que Lazar a accepté ? Oui, avec les extensions tranchées par la mère

R-2696 : session neuve du compte 2 ; mêmes paquets vérifiés aux empreintes de la ligne ; `lire_paquets` et `extraire`
de S ; ni `ouvrir` ni ligne neuve ; lecteur neuf ; écart au verdict et au registre. La commande fait cela et rien de
plus large : elle refuse le cas, non couvert, où le journal n'a pas été poussé (l. 158-161). Elle va au-delà sur trois
points, tous écrits à son annexe A et tranchés en R-2699 : sortie de la garde reconstituée (deux fonctions de lecture
de plus) ; réserve « exposé avant les scores de T0.7 » laissée au lecteur ; inscription de la session perdue hors du
tableau. « l. 1981-1983 » au lieu de « l. 1981-1982 » : même phrase, qui tient sur trois lignes.

## 3. Constats

### Majeurs

**M1 — Une session d'origine qui a rendu un arrêt est prise pour une session perdue.** Reprise, l. 168-173 ; v2,
l. 657-658 et 722-757. Démontré sur le jouet (section 1). Conséquence : un second lecteur serait lancé par-dessus un
arrêt que Lazar doit trancher, avec un redépliage hors de la garde que R-2696 ne couvre pas (il ne couvre que la
perte). → **R1** : la branche de l'ouverture ne doit porter, depuis sa base, que le journal.

**M2 — La perte d'une session vivante ne se constate pas par programme, et la commande dit le contraire.** Reprise,
l. 7 (« Le bloc 2 établit ce cas par programme »), l. 142-145, l. 173. Si la reprise part pendant que le premier
lecteur travaille, deux lecteurs écrivent deux verdicts, et la session d'origine poussera le sien sur sa branche sans
rien savoir de la reprise (la v2, déjà remise, ne regarde pas la branche de reprise). → **R2** : (a) dire ce que le
programme établit et exiger le mot de Lazar ; (b) revérifier, juste avant de commiter le verdict de reprise, que la
branche de l'ouverture n'a pas bougé ; (c) pousser la branche de reprise dès le bloc 2, comme marque visible et comme
épreuve de la poussée.

### Mineurs

**m1 — Bloc 4 : ordre des opérations.** Reprise, l. 273-283. Les réserves sont calculées après `extraire` : si
`lire_prealables` ou `date_de_la_mise_en_paquet` échoue, les fichiers sont déjà redépliés, le bloc s'arrête et n'est plus
relançable (sortie présente). Calculer les réserves avant `extraire`. → **R3**.

**m2 — Bloc 4 interrompu : dossier caché laissé.** Module, l. 1265-1273. Un appel tué pendant `extraire` laisse un
dossier `.ouverture-…` dans l'espace fermé, avec des fichiers des paquets en clair. La relance passe (sortie absente),
mais ce dossier reste à côté des pièces du lecteur. → **R3** (arrêt si un tel dossier existe).

**m3 — Réserve « exposé avant les scores de T0.7 » : issue prévisible à connaître.** Reprise, l. 343 ; consigne du
lecteur, section 7 (« toute ouverture hors de la garde consignée au registre : réserve … »). La consigne ne reprend pas
le « avant une ouverture autorisée » du texte : un lecteur qui la suit à la lettre écrira sans doute la réserve, dont
l'énoncé serait ici inexact (les scores de T0.7 sont scellés depuis 01:55:05Z, c'est l'appui même de l'ouverture), et
elle se transmet à T0.7. La mère a choisi de laisser le lecteur juger (décision 2) : je ne propose pas de couple, mais
le verdict de reprise est à relire sur ce point avant d'inscrire quoi que ce soit côté T0.7.

**m4 — Répétition : la reconstitution des réserves n'est éprouvée qu'à zéro.** Sortie, l. 42 : « 0 réserve(s)
reconstituée(s) », alors que le cas réel en attend trois (reprise, l. 287). Le jouet commite son paquet après les
lignes d'écrit. Le calcul est celui du module (l. 1306-1307), mais le cas positif n'est pas montré. De même, le constat
de perte compte huit arrêts et la répétition n'en éprouve qu'un (règle R5). À ajouter à la répétition de la version 2 :
un paquet jouet daté avant les lignes d'écrit (par `--date` au commit), et les artefacts « passation sur la branche »,
« deux lignes d'ouverture », « dernière ligne un refus », « journal de `main` différent ».

**m5 — Rien n'empêche de coller la reprise dans la conversation d'origine.** Reprise, l. 8. Une « perte » peut être
celle du seul conteneur, la conversation survivant. Le programme ne peut pas le voir (le commit du journal ne porte pas
l'identifiant de session). La commande dit « session neuve » ; le redire au mode d'emploi comme condition d'arrêt, et
faire noter par la mère l'identifiant de la session perdue quand Lazar le donne. → dans **R2 (a)**.

**m6 — Contrôle du texte collé absent.** La v2 demandait, avant le bloc 1, de vérifier que le texte collé est le
fichier scellé dont Lazar donne le chemin et l'empreinte ; la reprise ne le demande pas. → dans **R2 (a)**.

## 4. Corrections (couples ancien texte / nouveau texte)

### R1 — bloc 2 : la branche de l'ouverture ne porte que le journal (M1)

Ancien (reprise, l. 168) :

```text
[ "$(git ls-tree -r --name-only "$O" -- docs/verdicts | grep -c '^docs/verdicts/verdict-P3-bis-v1')" = 0 ] || arret "un verdict est déjà sur $BRANCHE_OUV : pas de perte"
```

Nouveau :

```text
[ "$(git ls-tree -r --name-only "$O" -- docs/verdicts | grep -c '^docs/verdicts/verdict-P3-bis-v1')" = 0 ] || arret "un verdict est déjà sur $BRANCHE_OUV : pas de perte"
B0=$(git merge-base refs/remotes/origin/main "$O") || arret "base de $BRANCHE_OUV introuvable"
[ "$(git diff --name-only "$B0" "$O")" = "$J" ] && echo "conforme : $BRANCHE_OUV ne porte que le journal depuis sa base" \
    || arret "$BRANCHE_OUV porte autre chose que le journal : la session d'origine a rendu (arrêt du lecteur, passation) ; ce n'est pas une perte"
```

### R2 — la perte se dit par Lazar ; la branche d'origine est revérifiée ; la branche de reprise est poussée tôt (M2, m5, m6)

(a) Ancien (reprise, l. 7) :

```text
  la poussée du verdict. Le bloc 2 établit ce cas par programme ; hors de lui, elle s'arrête. À coller par Lazar comme
```

Nouveau :

```text
  la poussée du verdict. Le bloc 2 établit par programme que l'ouverture est poussée et qu'aucun verdict ni aucune
  passation ne l'est ; **il ne peut pas établir que la session d'origine est perdue** : une session vivante, dont le
  lecteur travaille encore, donne le même état. La perte se dit par Lazar, en conversation, en te remettant cette
  commande (session close ou conteneur détruit, et depuis quand) : sans ce mot, tu ne commences pas ; tu le recopies mot
  pour mot au bloc 8. Si ta conversation est celle qui a exécuté la commande d'ouverture, tu t'arrêtes : il faut une
  session neuve. Avant le bloc 1, vérifie que le texte collé est le fichier scellé dont Lazar te donne le chemin et
  l'empreinte. À coller par Lazar comme
```

et, au bloc 8, ancien (reprise, l. 419) :

```text
CROCHET='<bloquée | passée>'
```

Nouveau :

```text
CROCHET='<bloquée | passée>'
PERTE='<mots de Lazar qui disent la session d origine perdue, recopiés tels quels, sans apostrophe droite>'
```

avec `$PERTE` ajouté au contrôle des variables de tête (l. 421) et à la ligne P2R-002 du journal provisoire (l. 431).

(b) Ancien (reprise, l. 383) :

```text
cd "$DEPOT"
```

Nouveau (première occurrence du bloc 7 seulement) :

```text
cd "$DEPOT"
git fetch --no-tags -q origin "+refs/heads/$BRANCHE_OUV:refs/remotes/origin/$BRANCHE_OUV" || arret "récupération de $BRANCHE_OUV"
[ "$(git rev-parse "refs/remotes/origin/$BRANCHE_OUV")" = "$(cat "$BAC/c-base-v1.txt")" ] \
    || arret "$BRANCHE_OUV a bougé depuis le constat : la session d'origine n'était pas perdue ; rien n'est commité ; nœud de Lazar"
```

(c) Ancien (reprise, l. 181) :

```text
echo "branche $BRANCHE créée sur $BRANCHE_OUV $(cat "$BAC/c-base-v1.txt")"
```

Nouveau :

```text
echo "branche $BRANCHE créée sur $BRANCHE_OUV $(cat "$BAC/c-base-v1.txt")"
git push -q origin "refs/heads/$BRANCHE:refs/heads/$BRANCHE" || arret "poussée de $BRANCHE refusée : rien n'est récupéré ni redéplié"
echo "branche $BRANCHE poussée (marque de reprise en cours, encore égale à $BRANCHE_OUV)"
```

(Le contrôle « la branche existe déjà au distant », l. 178, doit alors être passé quand le bloc est relancé : le mettre
dans la branche « sinon » de la ligne 179-180.)

Règle à écrire par la mère, hors de la commande : si, malgré tout, les deux branches finissent par porter un verdict,
aucun n'est inscrit sans un mot de Lazar (la décision 4 de R-2699 dit déjà qu'un conteneur revenu n'est ni lu ni repris).

### R3 — bloc 4 : réserves avant l'extraction, aucun dossier caché laissé (m1, m2)

Ancien (reprise, l. 271) :

```text
assert not sortie.exists() and sortie.parent.is_dir() and not reconst.exists(), "sortie déjà présente ou parent absent"
```

Nouveau :

```text
assert not sortie.exists() and sortie.parent.is_dir() and not reconst.exists(), "sortie déjà présente ou parent absent"
assert not list(sortie.parent.glob(".ouverture-*")), "dossier caché d'un redépliage interrompu : rapport à la mère"
```

Ancien (reprise, l. 275-279) :

```text
o.extraire({**p["lectures"], **p["run"]}, sortie)   # dossier caché du même parent, renommé en sortie
assert hashlib.sha256(journal.read_bytes()).hexdigest() == avant, "le journal a changé"
pre = o.lire_prealables(depot / o.REGISTRE_PREALABLES)
date_paquet = o.date_de_la_mise_en_paquet(clone, run, None)
reserves = [f"{k} : écrit après la lecture fermée : sa cécité repose sur la fermeture" for k, l in pre["ecrits"].items() if l["instant"] > date_paquet]
```

Nouveau :

```text
pre = o.lire_prealables(depot / o.REGISTRE_PREALABLES)
date_paquet = o.date_de_la_mise_en_paquet(clone, run, None)
reserves = [f"{k} : écrit après la lecture fermée : sa cécité repose sur la fermeture" for k, l in pre["ecrits"].items() if l["instant"] > date_paquet]
o.extraire({**p["lectures"], **p["run"]}, sortie)   # dossier caché du même parent, renommé en sortie
assert hashlib.sha256(journal.read_bytes()).hexdigest() == avant, "le journal a changé"
```

## 5. Limites

Les corrections changent les blocs 2, 4, 7 et 8 : la répétition est à rejouer sur la version 2 de la reprise
(l'empreinte des blocs changera). Je n'ai éprouvé que le couple R1 (dépôt d'essai) ; R2 et R3 sont écrits, non joués.
Comme pour l'ouverture, les vrais paquets, leur taille et la poussée réelle ne sont éprouvés que le jour même ; ici
aucune de ces inconnues n'est irréversible, la reprise n'écrivant rien au journal.
