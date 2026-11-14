rédigé sans vue des données de 7b

# Contre-lecture « revue adverse de sûreté » de la répétition sur carte de B bis (T0.7), v1 — modèle C

- **Heures (`date -u`)** : du 2026-11-14 23:05 à 23:15 UTC. **Copie lue** : `/home/user/relecture-bbis-repetition-v1`, commit
  `c880f36f9b02b2129cf0c33a9b455445650952a6` (vérifié par `git rev-parse HEAD`).
- **Lu** : `rapport-developpeur-repetition-carte-v1.md` (commande de la mère, § 3, gestes 0 à 10), `rapport-developpeur-corrections-v4.md`,
  `scripts/repetition_carte_bbis_v1.py`, `scripts/amorce_repetition_bbis_v1.sh`, `scripts/lancer_repetition_bbis_v1.sh`,
  `scripts/lancer_bbis_v1.sh` (comparaison), `git diff f4427fb6 bbc2e1c8`, `registre_bbis_v1.py` (lignes 195-275), les essais de
  destruction et de minuterie (`tests/test_t07bbis_chaine_instance_v1.py`, `tests/test_repetition_bbis_v1.py`, passages cités),
  `.claude/hooks/garde_calcul.py` et `.claude/settings.json`, et du préenregistrement « Calcul et dépense » et « Liste d'arrêt »
  (la sortie de la recherche de la liste d'arrêt a été tronquée par l'outil et gardée dans un fichier du harnais, que je n'ai pas lu).
- **Fait de mon côté** : lecture seule, plus deux appels de Python avec `-B` (aucun fichier d'octets écrit) qui importent le script de
  la répétition et évaluent ses fonctions pures (durée maximale, garde d'identifiant). Aucun essai lancé, aucun réseau, aucune clé
  lue, aucun `vastai`, aucun `git` autre que lecture, aucune écriture hors de ce rapport. **Aucun refus de permission ni du
  classifieur** dans ce tour.
- **Rien d'ouvert** dans `/home/user/controle-ia-travail` (hors l'interpréteur) ni sous `diag/`, `runs/`, `donnees/`, `essai/`.

## Verdict : **feu possible après corrections**

Aucun constat bloquant. La conception tient : minuterie armée avant toute passe, destruction jamais jugée par un code de sortie,
refus des six identifiants, jetons par leur nom, aucune entrée de 7b sur la machine. Mais trois constats **majeurs** demandent, avant
le geste 4 (création), des corrections **par consigne** (aucun changement de code requis ; M1 admet une version avec code) : M1
(instance 60671759 non protégée), M2 (le plafond de 3 USD repose sur une destruction par minuterie jamais jouée pour de vrai et sur
la cadence de la mère), M3 (le jeton GitHub donne à une machine louée l'accès à tout le dépôt privé ; la liste des instances peut le
porter). Les mineurs m1 à m8 se traitent en consigne ou en une ligne.

## (a) Le plafond de 3 USD peut-il être dépassé ?

**Arithmétique vérifiée** (évaluation de `duree_max_h`, geste 3) : échéance à `duree_max_h × 3600 − 600` s ; à 1,09 USD/h, 118 min ;
à 1,30, 95 min ; à 1,40, 86 min. Coût plafonné calculé par la garde, `(durée + ¼ h) × prix + 0,40`, à l'échéance : 2,82 ; 2,78 ; 2,77 USD.
La garde de commande refuse donc toute échéance plus lointaine (essayé : `duree_max_h` exacte rend 2,9997, au-dessus rend un refus ; la
marge de 10 min du geste 3 ramène à 2,8). L'échéance étant **absolue**, une commande jouée en retard ou rejouée après un échec ne peut
que raccourcir la durée : sens sûr. L'offre à plus de 1,40 USD/h est refusée.

**Ce qui reste exposé** :

- **M2 (majeur) — la butée repose sur une chaîne jamais jouée en réel.** Le plafond « par construction » suppose que la minuterie
  (`DELETE` avec `CONTAINER_API_KEY` sur `console.vast.ai/api/v0/instances/<id>/`) détruit à l'échéance. Cette voie n'a été
  éprouvée que contre des simulacres (fonction `curl` factice, six `DELETE` « 200 ») : ni l'adresse, ni l'autorisation de la clé de
  conteneur, ni l'effet réel n'ont été vus, et le même jour `destroy instance` sans `-y` avait « réussi » sans rien détruire
  (R-2789). Marge au-delà de l'échéance : le coût réel à l'échéance est d'environ `durée × prix + stockage` (≈ 2,2 à 2,4 USD), donc il
  reste **de l'ordre de 25 à 35 minutes de carte** avant 3 USD. Si le `DELETE` échoue et que la mère ne détruit pas dans ce délai, le
  plafond est dépassé ; après la 5ᵉ tentative l'amorce demande « stopped » (stockage seul, ≤ 0,08 USD/h), ce qui limite la pente mais
  ne la supprime pas. **Correction (consigne, couple M2)** : la mère se fixe son **propre arrêt dur à l'échéance moins 5 minutes**
  (destruction jouée, preuve par la liste avec témoin), indépendant de la minuterie ; la minuterie est traitée comme **non prouvée**
  jusqu'à ce que la répétition elle-même montre, dans `vastai logs`, un `DELETE` réel (impossible sans la déclencher : donc ne
  jamais compter dessus pour le plafond). Écrire dans le registre des dépenses l'heure d'échéance et l'heure d'arrêt dur avant le geste 4.
- **M2 bis — fins sans filet.** (i) Les refus d'arguments **avant** la minuterie (variable absente, échéance hors de ]maintenant, + 3 h]
  — notamment si l'image tarde à se charger et que l'échéance est déjà passée —, identifiant d'instance illisible) font `exit 2` : le
  conteneur s'arrête sans minuterie, l'instance reste listée (stockage facturé) jusqu'à destruction par la mère. (ii) À la fin normale
  (`fin_instance`), la demande « stopped » **tue aussi la minuterie** : l'instance arrêtée n'a plus de filet et coûte son stockage
  (jusqu'à environ 1,9 USD par jour de disque à 0,08 USD/h) tant que le geste 9 n'est pas joué. (iii) Un échec de `set -u` après
  l'armement de la minuterie fait sortir le script, donc le conteneur, donc la minuterie. Les trois cas se ferment par la même
  consigne : **geste 8 puis geste 9 dans les 15 minutes qui suivent « fin, code N »**, et la mère ne clôt pas sa session avec une
  instance listée (la routine de reprise, étape 4, le rattrape ensuite, mais seulement à la session suivante).
- **m4 (mineur) — prix et carte déclarés, non lus.** `OFFRE.json` est écrit à la main : la garde compare le prix déclaré au prix
  déclaré. Une faute de transcription (ou un prix modifié par l'hôte entre la recherche et la création) passe. Le grep `A100` de
  l'amorce admet une A100 PCIe 40 Go. **Correction** : construire `OFFRE.json` par un petit programme à partir de la sortie de la
  recherche (clés lues, jamais retapées) ; après le geste 4, relire l'instance créée (`vastai show instances --raw`, lire les clés
  `gpu_name`, `dph_total`, `label` seulement) : prix > 1,40 ou carte autre que A100 SXM4 80 Go → destruction aussitôt. Vérifier aussi
  que le `dph_total` de la recherche est calculé pour le disque de 60 Go demandé (la forme de la requête est déjà « à confirmer » au geste 2).
- **m8 (mineur) — sens du « cumul » du geste 6.** Le texte dit « heures facturées × prix, plus stockage » de **l'instance** ; la garde
  l'applique à la coupure de 3 USD. Si la mère passait le cumul de la ligne de GO (autres dépenses comprises), la garde refuserait
  sans raison (sens sûr) ; si elle passait un cumul incomplet (sans stockage), elle sous-estimerait. Dire dans la consigne : cumul de la
  répétition seule, stockage compris, relevé dans `vastai show user`/`show instances` filtré.
- **Relance.** Le texte ne prévoit aucune seconde machine : la branche de sortie neuve fait refuser (code 2) toute relance après un
  arrêt ayant poussé ses traces ; une relance suppose donc un nouveau nom (R12) et un nouveau devis. Aucune faille, mais la consigne
  doit écrire « aucune seconde création avant l'absence prouvée de la première ».

## (b) Destruction : `-y`, preuve par l'absence, instances d'autres sessions

**Ce qui tient** : `detruire` n'imprime que `GO_ID=… vastai destroy instance <ID> -y` pour un identifiant accepté (essai : la ligne
est exactement cette forme) ; `verifier-destruction` lit la liste (`show instances --raw`, code de sortie vérifié, liste d'objets
portant `id`), exige un témoin présent différent de l'instance, et refuse (code 2) témoin absent, liste illisible, lecture en échec ;
le cas « sans `-y` : Aborted., code 0 » est essayé contre un faux outil ; les six identifiants sont refusés comme cibles (essayé : 60670453
refusée) et permis comme témoins ; la liste de la répétition **est** celle de la course (v4).

- **M1 (majeur) — 60671759 n'est pas protégée, et ce risque est réel.** L'instance 60671759 (course Neuron Lens, même compte, en
  cours) est acceptée par `exiger_identifiant` (essayé : rend « 60671759 ») ; `detruire 60671759` imprimerait la ligne de destruction ;
  et le crochet `garde_calcul.py` ne couvre que `create|launch|start` : **la destruction n'est gardée par aucun crochet**. Les voies
  d'erreur concrètes : (1) un identifiant copié d'une liste plutôt que de `new_contract` (les numéros se suivent : la nouvelle instance
  aura un numéro voisin) ; (2) **la routine de reprise de la consigne permanente, étape 4**, qui ordonne d'arrêter « toute instance sans
  tâche en cours » : une session de la mère qui reprend pendant la répétition voit 60671759 sans tâche à elle et la détruirait ; (3)
  une liste d'exclusion fermée est structurellement en retard : 60670453 a manqué hier soir, 60671759 manque aujourd'hui, d'autres
  apparaîtront.
  **Fermer sans changer le code (consigne, couple M1)** : (i) la mère ne détruit **que** l'identifiant lu dans `new_contract` de la
  sortie de création, qu'elle écrit au registre des dépenses **dans la minute** ; (ii) **avant** chaque `destroy`, elle relit
  `vastai show instances --raw` et vérifie par programme que l'identifiant porte l'étiquette `bbis-t07-repetition-v1` (clés `id` et
  `label` seulement affichées) ; sinon elle ne détruit pas ; (iii) elle inscrit « 60671759 : autre session, ne pas arrêter » (et toute
  instance sans l'étiquette de la répétition) dans `registres/etat.md` au titre de l'étape 4 de la routine, **avant** le geste 4 ; (iv)
  le témoin du geste 9 est 60480302 ou 60670453, jamais 60671759 (instance qui peut disparaître : refus sûr mais inutile).
  **Avec code (version préférable, non exigée)** : remplacer la liste d'exclusion par une garde **positive** dans `detruire` et
  `verifier-destruction` de la répétition : identifiant égal à celui du fichier écrit à la création **et** étiquette lue dans la liste ;
  au minimum, ajouter 60671759 par une liste locale à la répétition (le script de la répétition change donc d'empreinte, recalculée par
  `commande` ; le code de la course et `MIN_ESSAIS` ne bougent pas ; ne pas toucher à `registre_bbis_v1.py`, sinon `MIN_ESSAIS` change).
- **m1 (mineur) — la garde d'identifiant se contourne par la forme, et la preuve d'absence aussi.** `exiger_identifiant` utilise
  `str.isdigit()` et compare des chaînes : `060670453` et la même suite en chiffres pleine largeur sont **acceptées** (essayé),
  alors que `int()` les lit 60670453 ; l'argument `int` de l'outil de location les lirait de même, donc détruirait une instance
  protégée. Dans `exiger_absence` de la course, l'absence est cherchée dans `{str(i["id"])}` : un identifiant écrit `060670453` ou
  `０６…` n'y est jamais trouvé, donc « DESTRUCTION PROUVEE » pour une instance qui existe. Entrée fautive de la mère seulement
  (pas d'attaque), mais c'est le seul endroit où la preuve « par l'absence » peut être fausse. **Correction** : consigne (ne jamais
  retaper l'identifiant : copier `new_contract` d'un fichier) ; avec code : expression `^[1-9][0-9]*$` en ASCII et comparaison en entiers,
  dans la répétition d'abord (la même correction dans `registre_bbis_v1.py` change `MIN_ESSAIS` : à décider pour la course).
- **m7 (mineur) — version de l'outil.** `requirements-pilotage.txt` fixe `vastai==1.8.3`, les gardes citent 1.11.0 (comportement sans
  `-y`). Faire `vastai --version` et lire `vastai destroy instance --help` (présence de `-y`) avant le geste 1, sans autre appel.

## (c) Jetons : par le nom, jamais écrits ?

**Ce qui tient** : la ligne imprimée porte `-e GH_TOKEN=\$GH_TOKEN` (écrit `$GH_TOKEN` littéral, développé par le shell de la mère au moment de
jouer ; l'essai vérifie la forme) ; **aucun `HF_TOKEN`** n'est passé ; la clé du loueur n'apparaît dans aucune ligne ; l'amorce ne
contient ni `set -x`, ni impression de l'environnement ; l'aide d'identification de git ne contient que `${GH_TOKEN}` en texte (la
valeur n'est lue qu'à l'appel) ; `curl` de la minuterie porte `CONTAINER_API_KEY` en en-tête avec `-sS … 2>/dev/null` et le journal
n'écrit que le code HTTP ; les traces poussées sont une liste fermée (journal, `nvidia-smi`, `pip-verbeux`, `pip-freeze`, `essais`,
`carte*`, `repetition-carte.json`), copiée par `cp "$X"/*`, et le commit de traces est fait par index à part (le `.git/config` n'y
entre pas). Les essais exécutés sur l'instance définissent `curl` et `sleep` en fonctions de shell avant de jouer la minuterie : ils
ne frappent pas l'interface réelle avec l'identifiant et la clé de l'instance.

- **M3 (majeur) — portée du jeton et fuite par la liste.** (1) `GH_TOKEN` est un jeton qui **lit et écrit le dépôt privé entier**
  (7a, 7b, brouillons, registres), posé dans l'environnement d'une machine louée à un tiers, où `pip install -r requirements-gpu.txt`
  exécute du code de paquets. Ce risque est celui de la course, accepté par construction, mais la répétition en double l'exposition
  pour des données qui sont synthétiques : l'indifférence aux données ne vaut pas pour le jeton. (2) La liste des instances écrite par
  `verifier-destruction` (`mktemp -d`, fichier `instances.json`, chemin imprimé) et le fichier du geste 1 peuvent contenir l'environnement de
  l'instance (valeurs d'`-e` comprises) ; **à vérifier sans l'afficher**. **Correction (consigne, couple M3)** : jeton à portée fine
  (dépôt `controle-ia-travail` seul, contenu seulement, expiration ≤ 24 h), **révoqué après le geste 9** ; aucune règle de dépôt ne
  doit lui permettre d'écrire sur `main` (sinon : règle de protection, ou branche seule) ; ne jamais afficher les listes (`cat`) :
  compter par programme, sans rien imprimer, les occurrences d'un préfixe de jeton, afficher seulement les **noms de clés** ; supprimer
  `$DL` et le fichier du geste 1 après lecture ; si un préfixe de jeton est trouvé dans une liste, **révoquer aussitôt**.
- **m3 (mineur) — fichier du geste 1.** `vastai show user --raw > /tmp/repetition-utilisateur-avant.json` peut porter des champs
  privés (adresse, clé du loueur). Écrire sous `umask 077`, lire seulement les champs de crédit par programme, ne jamais le montrer, le
  supprimer ; même consigne pour le fichier « après » du geste 10.
- **m5 (mineur) — jeton vide.** Si `GH_TOKEN` n'existe pas dans le shell de la mère, la ligne passe `-e GH_TOKEN=` : la machine est
  louée, puis l'amorce s'arrête (code 2) sur « GH_TOKEN absent », minuterie armée, mais minutes payées. Avant le geste 4 :
  `[ -n "${GH_TOKEN:-}" ] && echo présent` (le nom seulement, jamais la valeur ; jamais `env`, `printenv`, `export -p`).

## (d) La ligne `vastai create instance` imprimée

Forme lue dans `lancer_repetition_bbis_v1.sh` (l. 56) : `GO_ID=GO-2026-11-14-09 vastai create instance <OFFRE> --raw --image <IMAGE>
--disk 60 --cancel-unavail --label bbis-t07-repetition-v1 --env "-e COMMIT=… -e BRANCHE_CODE=… -e ECHEANCE_UTC_S=… -e GO_ID=… -e
SCRIPT_SHA256=… -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo <base64> | base64 -d > /root/amorce_repetition_bbis_v1.sh &&
bash /root/amorce_repetition_bbis_v1.sh"`. Identique en structure à la course (comparée à `lancer_bbis_v1.sh`) moins `HF_TOKEN` et
les trois variables de 7b (`RUN_7B`, `BRANCHE_7B`, `RUN_BBIS`) : **rien d'inattendu** — pas de prix d'enchère (donc ni interruptible ni
`--bid_price`), pas de port ouvert, pas de `--ssh` ni `--jupyter`, disque 60 Go, variables en liste fermée, l'amorce transportée
par le corps de la commande (base64 à alphabet sans guillemets) et son empreinte comparée à celle du commit avant impression ;
`--args` est bien le dernier argument.

- **m2 (mineur) — l'image n'est pas épinglée et ne peut pas l'être.** Le texte du geste 4 dit « `<image de la course>` » sans la nommer
  (l'exemple des essais est `python:3.11-bookworm`) ; le filtre d'image `[A-Za-z0-9._:/-]` **refuse `@`**, donc une image par empreinte
  (`nom@sha256:…`) est impossible, et une étiquette peut bouger entre la répétition et la course (représentativité) ; l'image
  exécute du code avec `GH_TOKEN`. **Correction** : la mère écrit l'image exacte au feu écrit (une image officielle, par étiquette),
  relève après création le champ image de l'instance et le consigne ; décision de code pour la course : autoriser `@` dans le filtre.
- **Premier emploi réel** : la forme `--entrypoint bash --args -c "…"` et la clé `new_contract` n'ont jamais été jouées sur le vrai
  service ; si le premier `create` rend autre chose qu'un `new_contract` numérique, **ne pas deviner un identifiant** : lire
  `show instances` filtré par l'étiquette.

## (e) Que reste-t-il sur `calcul/t07bbis-repetition-v1`, et rien de privé n'y part-il ?

**Contenu** : un seul commit posé sur `COMMIT` (parent = `COMMIT`), d'arbre « arbre de `COMMIT` plus `traces/bbis-t07-repetition-v1/` »
(index à part, `add --sparse -f` du seul dossier de traces) ; fichiers au plus 94 000 000 octets ; poussé une fois (trois essais), sur une
branche vérifiée absente avant et dont toute sortie pousse ses traces. Les traces sont la liste fermée du (c). **Aucune donnée de 7b** :
l'amorce refuse (code 2) tout `runs/`, `diag/`, `donnees/`, `essai/` dans l'arbre extrait, ne récupère qu'une branche, et la
répétition tire elle-même ses jetons. Le dépôt cible est codé en dur : `https://github.com/lciric/controle-ia-travail.git`.

- **M4 (majeur, consigne) — geste 0, la poussée de départ n'est pas gardée.** `git push origin prep/t07bbis-code-v1` suppose que
  `origin` est `controle-ia-travail`. Après le renommage, l'ancien nom `lciric/controle-ia` est destiné à devenir la copie **publique**
  expurgée ; si `origin` pointait encore sur l'ancien nom, la branche (et tous ses ancêtres non encore poussés : brouillons,
  registres) partirait vers un dépôt qui peut devenir public. **Correction (couple M4)** : avant le geste 0, `git remote get-url origin`
  doit rendre `…/controle-ia-travail(.git)` ; sinon pousser par l'URL explicite ; lister ce qui part
  (`git log --oneline origin/main..prep/t07bbis-code-v1` et `git diff --stat origin/main prep/t07bbis-code-v1`) et n'envoyer que du
  code et des notes déjà prévus pour ce dépôt. Le commit est vérifié par `ls-remote` ensuite (déjà écrit).
- **Résidu** : la branche garde l'arbre complet de `COMMIT` plus les traces ; elle n'ajoute rien de privé au dépôt privé, mais **n'est
  pas** destinée à la copie publique : la liste d'exclusion de `scripts/depot_expurge.py` doit l'ignorer (à noter, non vérifié ici :
  ce script est hors de mon périmètre). Aucune suppression automatique : la branche reste jusqu'à décision de Lazar.
- **m6 (mineur) — poussée depuis un clone partiel.** Le commit est fait sur un clone `--filter=blob:none` extrait en partie ; l'essai
  de poussée n'a été joué que contre un dépôt nu local. Si la poussée échoue sur le service réel, l'amorce écrit « traces non poussées »
  et s'arrête : la mère lit alors `vastai logs` avant la destruction (geste 9 après lecture), pour ne pas perdre le résultat de 30 à
  45 minutes de carte ; coût du retard : celui du rythme du geste 6.

## Couples de corrections (pour le feu)

| couple | à faire avant le geste 4 | par |
|---|---|---|
| M1 | seul `new_contract` désigne l'instance à détruire, relevé au registre dans la minute ; étiquette relue avant tout `destroy` ; 60671759 écrite « ne pas arrêter » dans `registres/etat.md` (étape 4 de la routine) | consigne (code facultatif) |
| M2 | arrêt dur de la mère à l'échéance − 5 min ; minuterie traitée comme non prouvée ; gestes 8-9 dans les 15 min après « fin » ; aucune seconde création avant l'absence prouvée | consigne |
| M3 | jeton à portée fine, ≤ 24 h, révoqué après le geste 9 ; listes jamais affichées, comptées par programme, supprimées | consigne |
| M4 | `git remote get-url origin` = `controle-ia-travail` ; liste de ce qui part avant `git push` | consigne |
| m1 à m8 | une ligne chacun au feu écrit (identifiant non retapé, image nommée, fichier utilisateur filtré, `GH_TOKEN` présent, offre construite par programme, version de l'outil, cumul de la répétition seule, lecture des journaux avant destruction) | consigne ; m1 et m2 aussi en code, à décider |

## Ce que cette lecture ne dit pas

Elle ne prouve pas que `DELETE` et `PUT stopped` avec la clé de conteneur marchent sur le service réel, ni que `show instances --raw`
porte ou non les valeurs d'environnement (je n'avais ni réseau ni l'outil, et c'était interdit) ; ni que la forme de requête de recherche du
geste 2 convient à l'outil installé ; ni que `scripts/depot_expurge.py` ignore la branche de sortie ; ni la justesse des durées du
devis (non mesurées : c'est l'objet de la répétition). Aucune sortie de 7a, 7b, T0.7 ou P3-bis n'a été lue.
