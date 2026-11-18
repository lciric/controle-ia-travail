# Contre-lecture de la procédure pas à pas du pilote MR-2 sur la machine jetable (code v74, texte scellé candidat 6) — v4

Contre-lecteur : modèle B, neuf, autre modèle que l'auteur (modèle A)

- Procédure relue : `procedure-pilote-v74-compte-organisme/procedure-pilote-mr2-v74-machine-v4.md`, empreinte
  `3c0e6627ea6732dd89e73d4fbc196d3853bcf8671e7f7c2f3f20a8995ef909c4` (égale à son compagnon `.sha256`).
- Début : 2026-11-14T23:23:59Z (sortie de `date -u` de ma première commande, recopiée par programme depuis l'argument de la commande d'écriture).
  Fin : 2026-11-14T23:31:08Z (`date -u` dans la commande qui écrit ce fichier). Rapport non scellé.
- Empreintes vérifiées, toutes égales aux valeurs attendues : texte scellé `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` ;
  paquet `e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1` ; relevé de la sonde
  `f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529` ; contre-lecture de la v3 `f07f9604…` (début égal à la ligne 7) ;
  les sept compagnons de `repetition-locale/` (« OK »). Les sept fichiers de code lus dans l'arbre local sont égaux, octet pour octet,
  à ceux du paquet dépaqueté.

## Verdict : jouable après corrections

Aucun bloquant, 4 majeurs, 13 mineurs. Le bloquant de la v3 (clonage du paquet) est corrigé et rejoué ; l'ordre du texte scellé est
suivi ; toutes les commandes du lanceur existent ; le bloc gelé est égal ; le script de lancement détaché est juste et éprouvé.
Les quatre majeurs sont tous **hors du lanceur** : la location (lecture de l'identifiant), la reprise après un refus nommé qui
laisse un dossier, la durée de la machine face à sa part de 3 USD, et la conduite quand un refus tombe alors que la machine est louée.
Chacun se corrige par quelques lignes de la procédure, sans toucher ni au code ni au texte.

**Limites de cette contre-lecture.** Aucun appel au loueur (interdit) : la syntaxe de `vastai destroy instance ID -y`, la forme de
la sortie de la création et celle de `vastai show instances` ne sont **pas vérifiées par moi** ; le constat M1 repose sur ma
connaissance de l'outil, à confirmer par son aide locale. Non lus (hors de ma liste) : `registres/go.md` (lignes 332-333), la
vérification courte cumulée `35d4216b…`, le crochet de garde, le contenu du dossier `repetition-locale/rapatrie/` (seul son
nom de premier niveau a été listé). Non lancés : `secret`, `generer`, `preparer`, `jouer`, `mesurer`, `lire` du lanceur réel ;
aucune connexion sortante (le contrôle de joignabilité n'a eu que sa syntaxe analysée). Aucun refus d'outil, de crochet ni de
classifieur rencontré.

## a. Constats de la contre-lecture de la v3 : corrigés ?

| constat v3 | verdict | lignes de la v4 | remarque |
|---|---|---|---|
| B1 clonage impossible | **corrigé**, rejoué | 66-68, 106-109 | dépaquetage éprouvé (point e) ; « complete history » dit trompeur |
| M1 lancement sans persistance | **corrigé**, éprouvé | 204-226 | script, `setsid nohup`, code dans un fichier, clés effacées : essai factice conforme (point d). Neuf, mineur : pas de `cd … \|\| exit` (m10) ; suivi sans borne (M3) |
| M2 lecture non rapatriée | **corrigé** dans le texte | 242, 246-248, 259 | nom dans `PERMIS`. Mais l'épreuve dite « sur la répétition » (l. 247-248, 310) n'a **aucune pièce déposée** (m3) |
| M3 clé absente | **corrigé**, éprouvé | 195, 199 | `${NOM:?}` arrête le shell (code 1, message sans valeur). Le code exige aussi `cle_presente` en mode réel (`controler_etat_relais`), refus avant le registre des lancements |
| M4 arrêts sans destruction | **corrigé en partie** | 43-47 ; appels l. 86, 87, 99, 118, 138, 151, 160, 193, 234, 246 | (A) manque à la section 8, à `lire` et à `rapatrier` (m1) ; la commande de rapatriement de la section 11 ne sert pas un arrêt précoce (m2) ; refus d'outil non couvert (M4) |
| M5 joignabilité | **corrigé** | 182-188, 191 | trois hôtes égaux à ceux des `url_amont` de la configuration v12 ; syntaxe juste ; ne prouve pas la validité des clés (m13) |
| m1 | corrigé | 12-13 | citée en tête, empreinte tronquée, pas de commande qui la vérifie à l'étape 1 |
| m2 | corrigé | 150 | barrière écrite |
| m3 | corrigé | 126-138 | qui inscrit l'empreinte de la phrase, et avant quelle étape, n'est pas dit (m12) |
| m4 | corrigé | 52-61, 76, 95-96, 179-181 | `E` supprimé ; forme d'appel de `O` sur la machine non dite (m8) ; contrôle de ports propre à bash (m5) |
| m5 | corrigé | 230-235, 246 | — |
| m6 | corrigé | 227-228 | parts 12, 8, 9,36, 9,36 égales à la configuration v12 ; `lancer_relais` : `plafond = part_usd` |
| m7 | corrigé | 87-88 | la borne d'une heure pèse sur la part machine (M3) |
| m8 | **dit, non essayé** | 44-45 | `CARTES-partiel.json` est dans `PERMIS` (essai synthétique de `rapatrier` : copié avec son compagnon) ; `rapatrier` sur un vrai dossier partiel reste non éprouvé |

Constats neufs créés par les corrections : M2 ci-dessous (le contrôle `test ! -e /root/pilote/reel` de la ligne 179 contredit la
reprise permise après un code 2, l. 231-233) ; m4 (`lire … > /dev/null 2>&1` avale la cause d'un refus) ; m5 ; m6.

## b. Exigences de la mère sur la machine

| exigence | présente | exacte | à la bonne étape | remarque |
|---|---|---|---|---|
| destruction avec `-y`, absence prouvée par la liste avec témoin | oui (l. 272-277) | oui dans sa lettre ; syntaxe non vérifiée par moi | oui (après `rapatrier`, et par (A)) | la preuve est une relecture à l'œil de deux listes ; un contrôle par programme serait plus sûr (m9) |
| identifiant tiré de `new_contract`, relu avec l'étiquette avant tout `destroy`, jamais retapé | oui (l. 80-82, 270-271, 278-279) | **en partie** | oui | la sortie « telle quelle » de la création n'est un JSON que sous `--raw` ; la commande de création n'est pas écrite ; aucun repli si le champ est illisible alors que l'instance existe (**M1**) ; `ID` vide non gardé |
| instances intouchables listées, jamais nommées dans une commande | oui (l. 16-17) | oui : les sept identifiants, et eux seuls, n'apparaissent qu'à la ligne 16 (recherche par programme) | sans objet | le témoin (l. 76-77, 273) doit se lire sans commande qui nomme un identifiant, pas même un filtre local : à dire (m9) |
| crédit et moyen de paiement relevés avant la création | oui (l. 75) | **imprécis** | oui (étape 2.2, avant 2.4) | ni commande, ni acteur (le moyen de paiement se lit à la console : Lazar ?), ni seuil, ni arrêt (m7) |
| aucune seconde création avant l'absence prouvée de la première | oui (l. 85-86, 280) | oui | oui | une création qui échoue sans rien créer : absence prouvée par l'inventaire égal à l'inventaire d'avant, à dire |

## c. Ordre et préalables du texte scellé

Suivis dans l'ordre de la section « Ordre » (l. 356-369 du texte) et des « Préalables » (l. 623-629) :

- lignes π1 et π2 inscrites : l. 14-15, 66 (relues au montant exact par le lanceur, `lire_go_du_pilote`) : conforme ;
- secret engagé et poussé avant la phrase : l. 123-128 (« Ensuite seulement ») : conforme à « Mondes et secret » ;
- mondes générés et vérifiés, empreintes inscrites avant C-16 : l. 143-151 (barrière) : conforme ;
- C-16 et C-17 : l. 156-160 : conforme (clés de sortie égales à celles du code ; gabarit `e77d3041…` retrouvé dans `preparer.txt`) ;
- essai à blanc avec les vraies pièces servies, rapatriement essayé : l. 165-172 : conforme ; aucune phrase d'arrêt (m1) ;
- relais avec leur part comme plafond ; dossier de la sonde à côté du relevé : l. 33, 96, 227 : conforme ;
- commande du mode réel : l. 214, égale option pour option à celle des « Préalables » (l. 626-628 du texte) ;
- un seul lancement réel : l. 179, 204-205 (registre hors dépôt, écrit par le code avant le premier appel) : conforme ;
- une seule mesure : l. 240, 246 ; issue lue par un sous-agent neuf : l. 248-249 : conforme ;
- rapatriement sans les mondes, puis destruction : l. 254-280 : conforme ;
- liste d'arrêt : code 3 → ni relance, ni mesure, ni lecture, pas même P-0 (l. 46-47, 233-235) ; panne tolérée, minimum 12 sur 16 et
  3 par monde (l. 230-231, égal à la « Règle », l. 221 du texte) ; refus nommé corrigé sans regarder d'attribution (l. 232) : conformes.

Ajouts qui ne changent pas la lecture : attente bornée (l. 87), contrôle TLS sans clé (l. 182-188), sortie de `lire` non affichée
et écrite dans `reel/` (l. 242, après la mesure, sans effet sur elle). Manques mineurs : le point 1 du « Plan d'analyse »
(empreintes vérifiées, liste `modules_importes` comparée au bloc gelé par le lecteur) n'est pas reporté dans ce que reçoit le
sous-agent (m11).

## d. Commandes

- **Analyseur** (`principal`, l. 643-699 du lanceur) : `secret CHEMIN` ; `generer --secret --phrase-fichier --texte --texte-sha256
  --sortie` ; `preparer --mondes --mondes-sha256` ; `jouer --mode --mondes --mondes-sha256 --sortie --go-pi1 --go-pi2 --registre-go
  --texte --texte-sha256 --mondes-shas --registre-lancements --releve-sonde` ; `mesurer --sortie --mondes --mondes-sha256` ;
  `lire --sortie --ecrire` ; `rapatrier --source --destination --mondes --mondes-sha256` ; `bloc --releve-sonde`. Toutes
  existent, noms exacts. Codes 0, 2, 3 : conformes (un secret déjà présent rend toutefois une exception, code 1, et non un refus : m10).
- **`lecture-pilote-v70.json`** : présent dans `PERMIS` (`audit_pilote_v70.py`, l. 35-37, compagnon compris). Essai synthétique
  (`essai_rapatrier.py`, depuis le paquet dépaqueté) : `lecture-pilote-v70.json` et son compagnon copiés, `aucun_monde` vrai,
  un `lecture.json` (ancien nom) laissé.
- **Ports et hôtes** : 8811, 8812, 8813, 8814 = `port` des quatre proposeurs de la configuration v12 ; les trois hôtes de la ligne
  184 = hôtes des quatre `url_amont`. Conformes.
- **Script de la section 9**, copié tel quel par un document au délimiteur entre guillemets : `bash -n` juste ; marques `@H@` et
  `@S@` remplacées par la commande `sed` de la ligne 218 (aucune marque restante) ; lancé par `setsid nohup … &`. Avec une commande
  factice et un faux fichier de clés : 25 arguments, tous justes et dans l'ordre ; noms exportés vus par le processus : les trois
  noms de la ligne 199 (deux finissent par `KEY`, le troisième par un suffixe), `HOME`, `PATH`, `PWD`, `SHLVL`, rien d'autre ;
  code 0 écrit ; fichier des clés effacé (mode 600 avant). La garde `${NOM:?}` arrête bien sur un nom absent.
- **`git archive … | tar … --strip-components=6`** : codes 0 et 0 ; le dossier obtenu porte `releve-sonde-pilote-v74.json`
  (`f56d9c0e…`, égal à son compagnon), les quatre dossiers de relais et les quatre journaux avec compagnons. Conforme à la ligne 69.

## e. Rejeu sans clé ni réseau (`/tmp/claude-0/contre-lecture-procedure-v4/`)

`git init -q arbre` ; `git bundle unbundle PAQUET` ; `git checkout -q 605e0f60…` : code 0 ; `git rev-parse HEAD` =
`605e0f60f3eed0948948e6a4eb15cb73de1d03de` ; `git status --porcelain --ignored` : vide, avant et après. `bloc --releve-sonde`
(relevé extrait par la commande de la section 1), sous `env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B`
(Python 3.13.18, numpy 2.5.3) : code 0, 5345 octets. Programme de la section 4 (chemins adaptés seulement) : **« bloc égal »**.

## f. Sécurité

- Clés : `printf` interne du shell vers l'entrée standard de ssh, fichier 0600 dans un dossier 0700, lu sous `env -i`, effacé par
  le script et par (A) : jamais en argument ni à l'écran. Le relais ne reçoit que sa clé, par son nom (`env_du_relais`) ; la
  commande d'un proposeur n'en reçoit aucune. Réserve : le fichier est lu par « . » (m6).
- Secret, phrase, mondes : restent dans `prive/` ; textes servis dans `reel/prive/`, hors de `PERMIS` (répétition : `laisses` =
  les six fichiers de `prive/`). La section 11 ne copie que `rapatrie-*`, les journaux, le code, le registre des lancements et
  l'engagement (empreintes seules). La ligne 32 (« rien n'en sort ») est à nuancer pour l'engagement (l. 258). Conforme.
- Arrêt commun (A) : mène à la destruction prouvée (l. 43-46, 267-280) ; appelé par les arrêts des sections 2, 3, 4, 5, 6, 7, 9
  et 10 (`mesurer`) ; **pas** par la section 8, ni par un `lire` ou un `rapatrier` différent de 0, ni par un refus d'outil (m1, M4).

## g. Constats classés

### Bloquant

Aucun.

### Majeur

- **M1 — Identifiant de la machine : sortie de création non lisible, et aucun repli** (l. 80-82, 85-86, 270). La procédure écrit la
  sortie « telle quelle » dans `creation.json` puis la lit par `json.load`. À ma connaissance de l'outil du loueur, la création
  n'imprime un JSON que sous l'option de sortie brute ; sinon une phrase suivie d'un dictionnaire entre apostrophes, que
  `json.load` refuse. La commande de création n'est pas écrite (ni option de sortie, ni option d'étiquette). Si la lecture échoue,
  l'instance existe et coûte, `ID` est vide, et la consigne de la ligne 86 (« destruction par l'identifiant lu ») est inapplicable :
  l'exécutant n'a plus que l'écran, donc un identifiant retapé (interdit). Correction : (1) écrire la commande de création entière,
  avec la sortie brute et l'étiquette, sa forme vérifiée par l'aide locale de l'outil avant l'étape 2 ; (2) garder `ID` :
  `: "${ID:?}"` après chaque lecture (l. 81, 270) ; (3) écrire le repli : si `new_contract` est illisible, `ID` = l'unique
  identifiant présent dans `instances-apres-creation.txt`, absent de `instances-avant.txt` **et** portant l'étiquette, tiré par
  programme ; s'il n'y en a pas exactement un : aucune destruction, nœud immédiat.
- **M2 — Reprise après un refus nommé (code 2) qui laisse le dossier de sortie** (l. 179, 193, 231-233). Fondement : dans `jouer`,
  `os.makedirs(args.sortie)` (l. 295 du lanceur) précède le lancement des relais ; un refus de `lancer_relais` ou de
  `exiger_relais_prets` (port pris, relais non démarré, `cle_presente` faux) remonte en code 2 (l. 349-352), rien n'est appelé, le
  registre des lancements n'est pas écrit — mais `/root/pilote/reel` existe, avec `prive/`. La procédure permet de corriger et de
  relancer après un code 2, mais son contrôle « juste avant » exige `reel` absent et commande l'arrêt (A) sinon, et le lanceur
  refuse un dossier existant. L'exécutant doit donc choisir seul entre effacer, renommer ou détruire la machine (mondes, secret et
  phrase perdus pour une cause bénigne). Même cas à l'essai à blanc (`blanc/`). Correction : écrire la règle — après un code 2,
  le dossier laissé est gardé tel quel (R12), la relance prend un nom neuf (`reel-2`, `blanc-2`), les contrôles de la ligne 179
  portent sur ce nom et sur le registre des lancements toujours absent, les clés sont renvoyées (le script les a effacées), le
  script est récrit avec le nom neuf ; les sections 10 et 11 suivent ce nom ; nombre de relances borné (une), sinon (A).
- **M3 — Durée de la machine et part de 3 USD sans garde** (l. 78-79, 87-88, 226-227). La location suppose « 2 h au plus ». Or la
  configuration v12 donne un délai de 3600 s à deux proposeurs et de 1800 s aux deux autres, par appel, et les 16 appels sont
  joués l'un après l'autre : pire cas 12 h, auquel s'ajoutent l'attente de la phrase (jusqu'à 1 h), la mise en place et les mondes
  (12 min). Au prix permis par la ligne 79 (1,5 USD par heure), la part machine de la ligne π2 serait dépassée, sans qu'aucune
  étape ne le voie ; le suivi (« toutes les quelques minutes, jusqu'au code ») n'a pas de borne ; il n'existe pas de ligne
  d'extension, et couper le pilote en cours brûle les mondes. Correction : fixer le prix horaire maximal sur le pire cas
  (3 USD ÷ 14 h, soit 0,21 USD par heure au plus, stockage compris — une offre à processeurs seuls y tient) ; consigner l'heure de
  location et l'heure limite = location + 3 USD ÷ prix, calculée par programme ; écrire quoi faire à l'approche de cette heure
  (nœud à la mère avant le dépassement, jamais d'arrêt du pilote de la main de l'exécutant sans son mot).
- **M4 — Refus d'un outil, du crochet ou d'un classifieur après la location : conduite non écrite** (l. 19-20, 43). La procédure
  interdit, à raison, de contourner ou de rejouer un refus ; mais l'arrêt commun (A) n'est appelé que par les arrêts « de
  l'étape ». Un refus d'une commande ssh, scp ou du loueur alors que la machine est louée laisse l'exécutant sans consigne, la
  machine continuant de coûter ; si le refus frappe la destruction elle-même, (A) ne peut pas finir. Cette lignée a déjà
  rencontré de tels refus (l. 302-304). Correction : ajouter à (A) : « tout refus après la location est une cause d'arrêt (A) ;
  si l'étape (2), (3) ou (4) de (A) est elle-même refusée, ne rien contourner : nœud immédiat à la mère et à Lazar, avec
  l'identifiant lu, l'étiquette, le prix horaire et l'heure, la machine restant louée jusqu'à sa destruction par une session qui
  le peut ; aucune création entre-temps ».

### Mineur

- m1 — (A) manquant : section 8 (essai à blanc ou rapatriement essayé différent de 0, ou comptes différents de 16 complets) ;
  section 10 (`lire` différent de 0) ; section 11 (`rapatrier` différent de 0 : `motif_interdit` refuse tout le lot si une
  réponse brute réelle porte un motif d'identifiant de fournisseur, cas jamais éprouvé à blanc). Écrire pour chacun : (A), et
  pour le dernier « aucune copie directe des pièces, nœud ».
- m2 — Rapatriement de (A) : la commande de la section 11 enchaîne par `&&` deux `scp` dont le premier échoue si `rapatrie-reel`
  manque, et `mkdir "$ENV/retour"` échoue s'il existe ; à un arrêt précoce, les journaux ne sortiraient pas. Écrire une commande
  propre à (A) : journaux, `code-09-reel.txt` et `lancements.jsonl` s'ils existent, `rapatrie-*` s'ils existent, chacun à part.
- m3 — Affirmation sans pièce (R6) : « la séquence `lire --ecrire` puis `rapatrier` est éprouvée sur la répétition » (l. 247-248,
  310). `repetition-locale/rapatrier.txt` ne cite aucun fichier de lecture (0 occurrence) et `lire.txt` est la sortie affichée.
  Mon essai synthétique confirme le nom et le compagnon, pas le contenu réel. Verser la sortie de cette épreuve, ou retirer le mot.
- m4 — `lire … > /dev/null 2>&1` (l. 242) : un refus (code 2) perd sa cause. La sortie d'erreur du lanceur ne porte que
  « refus : … » ou « arrêt : … », jamais l'issue : écrire `> /dev/null 2> /root/pilote/journal-10-lire-erreurs.txt`.
- m5 — Contrôle de ports (l. 181) : `/dev/tcp` n'existe que sous bash. Essai : sous bash, un port occupé est vu « OCCUPÉ » ; sous
  dash, le même port est dit « libre » (faux, sans message : R5). Écrire `ssh M "bash -c '…'"`, ou le faire en Python.
- m6 — Fichier des clés lu par « . » (l. 200-201, 214). Essai avec des valeurs factices : une valeur portant `$NOM` est
  développée, une valeur portant une espace est perdue (variable vide), sans arrêt. Correction : `printf 'NOM=%q\n'` (éprouvé :
  les trois valeurs reviennent intactes).
- m7 — Crédit et moyen de paiement (l. 75) : nommer la commande ou l'acteur (console : Lazar), le seuil (au moins la part
  machine) et l'arrêt si le relevé manque.
- m8 — Forme d'appel sur la machine : les sections 4, 6, 7, 8, 10 et 11 écrivent `O …` sans `ssh M '…'` ; une session d'agent n'a
  pas de terminal. `generer` (12 min) et `mesurer` (unique) tournent au premier plan : une coupure tue `generer` (relance
  possible si le fichier n'est pas écrit) et peut laisser une sortie de mesure qui interdit toute seconde mesure. Les lancer
  détachés comme l'étape 9, ou dire la conduite après une coupure (nœud, pas de relance de `mesurer`).
- m9 — Preuves de la section 11 à l'œil : ajouter un contrôle par programme qui lit `ID` dans `creation.json` et rend « présent
  avec l'étiquette » ou « absent » sur le fichier de la liste ; dire que le témoin se constate sans commande nommant un
  identifiant intouchable, pas même un filtre local.
- m10 — Détails : `: "${H:?}" "${S1:?}" …` avant le `sed` de la ligne 218 ; `cd … || exit 97` en tête du script ; un secret déjà
  présent rend une exception (code 1), pas un refus ; `ENV` est un nom que certains shells lisent au démarrage : préférer un autre nom.
- m11 — Sous-agent neuf (l. 248-249) : lui remettre tout `rapatrie-reel/` (la sortie de la mesure porte `modules_importes`, à
  comparer au bloc gelé, point 1 du « Plan d'analyse »), l'engagement et les empreintes inscrites au registre, pas le seul fichier
  de lecture ; dire si un audit qui demande les textes servis ou les mondes doit précéder la destruction (après elle, ils
  n'existent plus).
- m12 — Mise en place : port et clé publique de ssh, acceptation de la clé d'hôte sans dialogue, option de port de `scp`,
  présence de `git` sur l'image (non contrôlée), commande qui donne `M` ; qui inscrit l'empreinte de la phrase et avant quelle étape.
- m13 — Risque résiduel à dire : ni `${NOM:?}` ni le contrôle TLS ne prouvent qu'une clé est **valide** dans la session qui
  lance (la sonde a été jouée depuis une autre session). Une clé invalide donne quatre appels « échec » pour ce fournisseur, code
  0, lancement consommé ; deux fournisseurs ainsi perdus donnent P-0 et des mondes brûlés. Décision de la mère : l'accepter et
  l'écrire, ou prévoir un contrôle sans coût.

## Pièces

Rejeu : `/tmp/claude-0/contre-lecture-procedure-v4/` (`arbre/` dépôt dépaqueté ; `sonde/` extrait par `git archive` ;
`journal-04-bloc.txt`, `cmp.py`, `texte.md` copie du texte scellé ; `lancer-reel-tel-quel.sh`, `pilote/` essai du script,
`factice.sh` ; `essai2/` valeurs spéciales et syntaxe du contrôle de joignabilité ; `essai_rapatrier.py`, `essai3-*`).
