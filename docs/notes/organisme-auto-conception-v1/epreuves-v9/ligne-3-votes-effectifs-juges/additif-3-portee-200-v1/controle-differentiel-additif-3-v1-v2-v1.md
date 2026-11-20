# Contrôle du différentiel v1 → v2 de l'additif 3 de la ligne 3 (portée à 200 témoins) — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel, `date -u` : 10:03Z), sur le mandat `mandat-controle-differentiel-additif-3-v1-v2-v1.md` (`be683994045559b50e396a03eca00e75390f98cc1bc9c7f2ccc6bb6da60f9a5b`, égale à son compagnon, contrôle par `sha256sum -c` avant tout autre geste), sous GO-2026-11-20-26 et GO-2026-11-20-36 (point 2), règle R2. Je fais, à la place du contre-lecteur de la v1, la vérification de ses corrections. Contrôleur neuf, modèle O : je n'ai écrit ni le préenregistrement de la ligne 3, ni ses additifs, ni le code, ni le verdict de l'étage 1.

**Règle d'aveugle tenue.** Aucune mesure de l'étage 1 ouverte : rien sous `execution-etage-1-v1/`, `verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`. Ce que je sais de l'étage 1 est ce que la contre-lecture et l'additif en disent.

## Verdict

**À corriger**, pour une seule phrase, au § 7, nœud 1. La v2 est fidèle : rejeu égal à l'octet, corrections 1 à 3 portées mot pour mot, rien d'autre ne change que la tenue, et la tenue est juste. Mais une phrase du nœud 1 renvoie la décision de partir en issue B « au verdict scellé de la mesure », alors que GO-2026-11-20-36 (point 2) l'a prise avant la mesure : « partir dans les deux issues ». Sceller cette phrase écrirait dans un texte scellé qu'un choix de départ reste à faire après lecture. Les nœuds 2, 3, 4 et le point de procédure sont compatibles avec la lettre des décisions, tels quels.

## 1. Pièces vérifiées

Toutes par `env -C DOSSIER sha256sum -c F.sha256` (dossier D du mandat), chacune « OK », et compagnons lus égaux aux empreintes attendues :

| pièce | sha256 |
|---|---|
| additif 3, v1 | `9e189f1af673e07460e96fe17537727f445ee3e415c53cb24429787e9a898915` |
| additif 3, v2 | `bea75ff2b970f9cb344c241bccc63335289b27a97868b7543f5a6dd69a896b94` |
| contre-lecture de la v1 | `f264cf9e8c8fca02a308e6831963ab55672f77017e522c653fa2ac2c08b57082` |
| remplacements v1 → v2 (JSON) | `78d3c674c88c2b3de0c8d0ac06ef7d5e51a8d220ca68c058779f307c9fba0084` (compagnon : OK) |
| journal des remplacements | `e76d9fbc5add9ee459c0354d3be9ba54d8e1257026ca5a3000c0d9a1c30590b8` (compagnon : OK) |
| différentiel v1 → v2 | `2da6bdd61c52d89dde9df7fd34bf954d83bfbebde979a589a517449e0e5b6308` (compagnon : OK) |
| rapport du rédacteur, v2 | compagnon : OK |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

Tirées de main (`git fetch origin main`, tête `da0d389cad376ad492d0255b42d7e633fea09f5a`, `git show FETCH_HEAD:… >` mon dossier `main/`) : `registres/go.md` (`21f8f1847565c41f9e448746b826ef821575fcf65c267b319ed7ee5acba19356`), lignes 557 (GO-2026-11-20-26) et 567 (GO-2026-11-20-36) ; `registres/decisions.md` (`47ed2a0b17f38472948bd6dfe0c9cebe74212dec9d87bf2a4d2262e9b236099a`), lignes 4310 (R-4172) et 4312 (R-4174). Hors liste, pour juger le nœud 3 et la correction 2 seulement : le texte, version 7 (`4e3680d9…d5a0`, égale à l'attendue de l'additif), l. 232 à 242 et 301 à 315 ; le devis, version 7 (`382ea448…8270`, égale), § 7.

La ligne 7 de la v2 (sans son chevron) est égale à l'octet à la ligne 557 de `registres/go.md` sur la tête actuelle (`cmp` de deux extraits par `sed`).

## 2. Rejeu

`python3 -B scripts/remplacer_texte_exact_v1.py --cible v1 --remplacements remplacements-additif-3-v1-v2.json --sortie MON_DOSSIER/rejeu-additif-3-v2.md` : « FAIT : 5 remplacement(s) », sortie `bea75ff2…6b94`. `cmp` avec la v2 du dossier D : **égales à l'octet**. Mon différentiel (`diff -u`, étiquettes neutres) a le même corps que celui du rédacteur (`cmp` après les deux lignes d'en-tête, qui ne portent que chemins et dates) : cinq lignes changées, quatre blocs (titre et statut ; § 0 ; § 4.2 ; § 6). Le journal du dépôt montre cinq zones uniques, sans chevauchement ni avertissement.

## 3. Fidélité

- **Corrections 1 à 3, mot pour mot.** Chaque texte ancien et chaque texte neuf du JSON a été compté par `grep -c -F -e` dans la contre-lecture : 1 chacun (les six, entre accents graves au § 9). Chaque texte neuf est compté 1 dans la v2. Les trois zones sont celles que la contre-lecture désigne (§ 0, deuxième puce ; § 4.2, ligne « l. 241, l. 305 (5) et (7) », colonne « lecture à 200 » ; § 6, audit de symétrie).
- **Rien d'autre ne change** : hors ces trois zones, seuls le titre (« v1 » → « v2 ») et la ligne de statut changent. Aucun chiffre, aucune graine, aucune règle de lecture, aucun montant.
- **Tenue, de la main du rédacteur, jugée juste.** Statut : « version 2, non scellée. Contre-lue (règle R2) ; à sceller par la mère, après contrôle du différentiel » — exact. Phrase de version : elle nomme la contre-lecture et la v1 par leurs empreintes (justes), les trois sections touchées (justes), et dit « hors le numéro de version (titre, cette ligne de statut) et cette phrase, rien d'autre ne change » — exact, vérifié sur le différentiel. Réserve du rédacteur (« Pièces lues » non complétée) : acceptable, la contre-lecture et l'outil sont nommés au statut.
- Lecture des corrections portées : la correction 2 reste compatible avec le texte (l. 305, geste (7) : « ligne de GO de la mère sur le devis, au montant du plafond » ; devis § 7, point 6) et avec « sans devis neuf » de GO-2026-11-20-36 : elle lit l'accord de Lazar sur la ligne « 200 témoins » du devis v7 et ne demande aucun devis de plus.

## 4. Les quatre nœuds et le point de procédure, devant GO-2026-11-20-36 (2) et R-4172

Lettre de GO-2026-11-20-36 (2) : « Ligne 3, additif 3 : partir dans les deux issues ; seuil de 40 témoins gardé ; conditions du plafond par calcul versionné sans devis neuf ; GO-2026-11-20-26 lève la clause « étage 2 seulement sur un oui ». » Lettre de R-4172 : « un second additif court pour le code et les racines, à côté de l'additif 3 ».

**Nœud 1 — partir dans les deux issues. Une phrase doit changer.** Le § 0 (« l'étage 2 garde sa taille dans les deux issues ») et le § 3 (« Dans les deux issues A et B, la taille de l'étage 2 reste 200 témoins […] elle ne déclenche ni dépense ni arrêt ») sont compatibles. Le § 7, nœud 1, ne l'est pas dans sa dernière phrase : « Partir quand même, attendre, ou viser une autre taille est une décision de Lazar, à prendre sur le verdict scellé de la mesure. » La décision est prise, et avant la mesure ; la laisser écrite « à prendre sur le verdict » ouvrirait un choix après lecture (ce que la contre-lecture, § 7, voulait éviter, et que la règle R3 interdit dans l'esprit). Ancre comptée par `grep -c -F -e` dans la v2 : 1.

- Ancien : `Partir quand même, attendre, ou viser une autre taille est une décision de Lazar, à prendre sur le verdict scellé de la mesure.`
- Neuf : `Lazar l'a tranché avant la mesure (GO-2026-11-20-36, point 2) : partir dans les deux issues. En B comme en A, l'étage 2 à 200 suit l'ordre des gestes que le § 4.1 garde, sous GO-2026-11-20-26 ; l'issue de la mesure ne rouvre pas la question du départ.`

**Nœud 2 — seuil de 40 gardé. Compatible, tel quel.** § 4.2 (« **40, à la lettre** : c'est un critère gelé, je ne le change pas ») et § 7, nœud 2 (« Je le garde à 40, à la lettre ») disent déjà la décision.

**Nœud 3 — conditions du plafond par calcul versionné, sans devis neuf. Compatible, tel quel.** Le plafond est lu à 88,36 USD (§ 4.2, ligne l. 80) ; les chiffres dérivés sont renvoyés « à porter par un calcul versionné, non par ce texte » (ligne l. 366 à 367) ; le § 7, nœud 3, pose la question dont GO-2026-11-20-36 choisit la seconde branche ; la correction 2 ne demande aucun devis neuf. **Relève du second additif, non porté ici** : le calcul versionné lui-même (envois avant l'arrêt si tout est refusé, témoins complets au pire cas, multiples du tarif, issue écrite du pire cas), à sceller avec l'additif de code de l'étage 2.

**Nœud 4 — GO-2026-11-20-26 lève la clause « étage 2 seulement sur un oui ». Compatible, tel quel.** § 4.2, ligne l. 331 et l. 378 (« l'étage 2 à 200 ne part que par l'écart que Lazar a décidé (GO-2026-11-20-26) ») et § 7, nœud 4 (« Je lis GO-2026-11-20-26 comme l'écart qui lève cette clause pour 200 témoins ») sont la lecture que Lazar a confirmée.

**Point de procédure — second additif court (R-4172). Compatible, tel quel.** Le § 5, point 4, fixe déjà que « la pièce qui autorise est l'additif de code de cette mesure, court », scellé par la mère après la contre-lecture du code ; le § 7 décrit l'autre voie au conditionnel (« Si la mère préfère une seule pièce »), que R-4172 a écartée : pas de contradiction. **Relève du second additif, non porté ici** : le code, son commit et ses empreintes, les commandes complétées, l'autorisation des trois racines 2026112031 à 2026112033.

## 5. Ce que la v3 doit porter

1. Le remplacement du nœud 1 ci-dessus, et rien d'autre de fond.
2. La tenue : titre « — v3 » ; ligne de statut et phrase de version neuves, de la main du rédacteur, qui disent que la v3 porte sur la v2 (`bea75ff2…6b94`) le seul changement du § 7, nœud 1, demandé par ce contrôle (empreinte au compagnon) en application de GO-2026-11-20-36 (point 2). La phrase de version de la v2 (« elle porte à la lettre les corrections 1 à 3 […] rien d'autre ne change ») doit être remplacée ou complétée, sans quoi elle deviendrait inexacte.
3. Un contrôle du différentiel v2 → v3, puis le scellement par la mère.

Non exigé : inscrire aussi la décision aux nœuds 2 à 4 (« tranché : GO-2026-11-20-36 ») rendrait la v3 plus nette ; les textes actuels n'en sont pas faux.

## 6. Ce que j'ai fait, et mes écarts

- Commandes : `sha256sum -c` sur le mandat et chaque pièce ; `python3 --version` (3.13.18) ; `mkdir -p` de mon dossier ; un appel de l'outil de remplacement (sortie dans mon dossier) ; `cmp` ; `diff -u` redirigé, `tail -n +3` redirigé, `cmp` ; `grep -c -F -e` sur des fichiers nommés ; `git fetch origin main` ; `git rev-parse FETCH_HEAD` ; `git show FETCH_HEAD:CHEMIN >` fichier ; `sha256sum` sur des chemins nommés ; `sed -n` redirigé ; `date -u`. Recherche par l'outil de recherche du poste, chacune sur un seul fichier nommé et un motif étroit : identifiants GO-2026-11-20-26 et -36 dans ma copie de `go.md`, R-4172 et R-4174 dans ma copie de `decisions.md`, titre « ## 7 » dans ma copie du devis.
- **Écarts déclarés.** (a) Lecture de deux pièces hors de la liste du mandat (texte v7, extraits ; devis v7, § 7), tirées de main, empreintes vérifiées, pour juger la correction 2 et le nœud 3 ; aucune mesure n'y est. (b) Deux commandes refusées par leur programme pour une option inconnue (`diff --output`, `tail --output-delimiter`), sans effet ni écriture. Ce ne sont pas des refus de permission, de classifieur ou de garde.
- Aucune mesure de l'étage 1 ouverte ; banc ni lancé ni importé ; aucune graine dérivée ; aucun appel de modèle, aucune dépense ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/` ; aucune écriture dans le dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde.

Fichiers de mon dossier (`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/controle-additif-3-v2/`) : ce contrôle et son compagnon ; `rejeu-additif-3-v2.md` et ses trois fichiers d'accompagnement écrits par l'outil ; `mon-differentiel-v1-v2.diff` et les deux corps comparés ; les deux extraits de la ligne GO-2026-11-20-26 ; copies de main sous `main/`.

Contrôleur neuf, modèle O.
