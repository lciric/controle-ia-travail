# Vérification courte de la procédure du pilote MR-2 — v9 (passage v8 → v9) — et contre-lecture du programme d'épreuve des clés — v1

- **Lecteur** : instance neuve, qui n'a écrit aucune version de la procédure, ni le programme d'épreuve, ni aucune de leurs
  vérifications. Ce rapport n'écrit aucun nom de modèle (seules les étiquettes de la configuration v12 : `opus55`, `fable52`,
  `argon`, `astra` ; les fournisseurs sont dits « premier », « deuxième », « troisième », dans cet ordre).
- **Pièces** (copie `/home/user/verif-pilote-v9`, tête détachée `0714cc59`, arbre propre avant écriture ; toutes les empreintes
  recalculées et égales à leurs compagnons) :
  - procédure v9 `e71b66983ace4badff1695d885aa3714f7adf805c2eb834e8c688c23103bb288` ; v8
    `56ccdb5a398acb8faa2588dd448ec42b446b7264e22d82cd3f975e5393f4054d` ;
  - programme `epreuve_cles_pilote_v1.py` `f56eaecbe6f79aef7b4d40e794a0f317c8306326d8665ae532bf02efa0d8221f` ; devis
    `5ea76fad7562f5b93a908967d4bdd472f6437d35281f82f3e2655d65a67b566e` ; essai local : doublure `57a761f6…`, sortie `64246013…` ;
  - paquet de l'arbre `e3d83e47…` (tête `605e0f60…`), configuration v12 `f69503dd4ba5e57a8bde230b3861571549d9598382808a8f3c0f4fa664ea818b` ;
  - corrections attendues : vérification de la v8 `fbf07c0409e64339e9f773f5911314f2ba84a780b988bd435ca58cb5e69c59a5` (dépôt de travail,
    égale à son compagnon) ; ligne GO-2026-11-15-02 (`registres/go.md` l. 335 du dépôt de travail) ; R-2856 (`registres/decisions.md`
    l. 2816).
- **Fin** : 2026-11-15T08:20:57Z (sortie de `date -u` dans la commande qui écrit ce fichier).
- **Aucun appel réel, aucune clé lue, aucune machine, ni `env` ni `printenv`.** Tout ce qui a été joué l'a été contre la boucle
  locale, avec des clés factices écrites en clair dans la commande d'essai.

## Verdicts

- **Procédure v9 : jouable après corrections** — 0 bloquant, **2 majeurs** (MP1, MP2), 8 mineurs.
- **Programme d'épreuve v1 : jouable après corrections** — 0 bloquant, **2 majeurs** (ME1, ME2), 7 mineurs.

Le différentiel v8 → v9 est **entièrement déclaré** (aucun changement ni retrait caché) ; **M1 et M2 de la v8 sont fermés**, m2 à m9
portés ; **m1 est porté dans la forme mais rend la ligne de création injouable à la lettre** (MP1, échec du côté sûr : rien n'est
créé). Aucune régression sur l'argent, les plafonds, les nœuds, l'heure limite, les arrêts, la destruction, les clés. Le programme
d'épreuve tient ses promesses de silence (aucune clé, aucun corps, aucun identifiant, dans aucun des cas d'erreur éprouvés) et
d'appel unique sans reprise ; ses deux majeurs portent sur **ce qu'il déclare valide** (règle du modèle servi plus lâche que celle
du pilote) et sur **l'argent** (aucun contrôle de la dépense lue contre la ligne).

Les quatre majeurs, une ligne chacun :

- **MP1** (procédure l. 183-184) : la ligne de création dit son préambule « joué dans la commande d'avant », or la session ne garde
  aucun état d'une commande à l'autre (l. 40-41) : `ETIQ` et `ENV` sont vides, la ligne échoue toujours (rien n'est créé).
- **MP2** (procédure l. 144-150) : l'empreinte du programme d'épreuve est affichée mais ne conditionne pas l'exécution ; un
  `git show` en échec laisse un programme vide qui rend `code=0`, le code attendu.
- **ME1** (programme l. 90, 95) : « modèle servi conforme » = simple préfixe, et l'usage absent est accepté ; le pilote, lui, exige
  l'identifiant exact ou un suffixe de date réelle et abandonne le proposeur sur l'une ou l'autre cause : l'épreuve peut rendre 0 là
  où le pilote abandonnera.
- **ME2** (programme l. 62-65, 95-100) : aucune comparaison de la dépense lue au montant de la ligne ; avec une réflexion non bornée
  chez `argon` (réserve du devis), le programme rend `code=0` au-dessus de 0,10 USD (éprouvé : 1,60 USD, code 0, aucun signal).

**Conséquence de forme à trancher par la mère (nœud)** : corriger le programme change son empreinte et, par R12, son nom
(`epreuve_cles_pilote_v2.py`) ; la ligne GO-2026-11-15-02 nomme `epreuve_cles_pilote_v1.py`, et R-2856 son empreinte `f56eaecb…`.
Je ne tranche pas ; voir « Ce qui se passe si le programme est joué tel quel ».

## Limites

- Non vérifiable ici, sans appel : que la borne de sortie passée à `argon` borne aussi sa réflexion (réserve du devis, entière) ;
  qu'une borne de 16 jetons rende bien 200 chez chacun des trois fournisseurs (une réponse coupée à la borne) plutôt qu'un refus ;
  que le mandataire de la session qui lance laisse passer les trois adresses (un refus du mandataire donnerait
  `erreur:URLError` ou `erreur:OSError`, code 4 : arrêt sans location, épreuve consommée).
- Bibliothèque cliente : `urllib` de la bibliothèque standard, Python 3.13.18 (celui de `/usr/bin/python3` ici) ; lue dans son
  comportement par essais sur doublure, non dans son code.
- Crochet de garde : lu (`73be0638…`, égal dans la copie et dans le dépôt de travail) et joué sur quatre entrées factices.
- Arbre du paquet lu dans le dossier temporaire de la session (tête `605e0f60…`, propre) ; rien n'en a été exécuté sauf la fonction
  `modele_conforme` de `commande_pilote_v70.py`, appelée sur des chaînes factices.
- Aucun refus d'outil, de crochet ni de classifieur rencontré.

---

# Partie A — procédure, v8 → v9

## A1. Différentiel exact

`diff` : 19 blocs. Relecture mot à mot des retraits (`git diff --no-index --word-diff=porcelain`) : chaque groupe de mots retiré
appartient à une ligne que la section 12 sexies dit changée ou retirée.

| lignes de la v9 | changement | point déclaré (12 sexies) |
|---|---|---|
| 1 | titre « v9 » | m8 (« en-tête changé déclaré ici ») |
| 5 | « après une vérification « jouable » du différentiel v8 → v9 » | m8 |
| 7-11 | versions ; « la v9 remplace la v8 » ; renvoi à 12 sexies | m8 |
| 24-25 | rapport `4be9e744…` cité pour les champs neufs de l'outil | m8 |
| 49 | `REEL` ajouté à la liste de `variables.sh` | m8 |
| 86-87 | « NON LANCÉ » inattendu : conduite | m3 |
| 89-90 | constat « aucun `jouer` ne tourne » | m5 |
| 136-157 | étape d'épreuve des clés | épreuve (R-2856) |
| 167-168 | repli « solde à l'interface » retiré | m8 (retrait dit) |
| 172 | `isinstance(l,list)` | m9 |
| 183-184 | `GO_ID=` en tête, `${ETIQ:?}` dans l'option, retrait du `: "${ETIQ:?}";` | m1 (retrait dit) |
| 227-229, 233-238 | attente du montage : trois tours, sept commandes, `running`, hôte non nul, `if … else`, reprise du premier ssh | m2, m4 |
| 379-385 | risque des clés réécrit ; phrase « aucune épreuve sans appel… » retirée | M1 ; retrait dit |
| 400 | `REEL=reel` dès « lancé » | M2 |
| 431-433 | `REEL=reel-2` dès le « lancé » de la relance ; retrait de « après un code 0 du premier essai » | M2, m7 (retrait dit) |
| 466, 473 | `${REEL:?}` dans les lignes de `ls` et de `lire` | m6 |
| 486-488 | garde de tête retirée ; consigne de saut ; garde dans la ligne de `rapatrier` | M2 (retrait dit) |
| 648-668 | section 12 sexies | déclaré |

- **Changement non déclaré : aucun. Retrait non déclaré : aucun.** Aucun bloc dans les sections 4, 5, 6, 7, 8, 12, 12 bis, 12 ter,
  12 quater, 12 quinquies, 13 (bornes de sections relues : l. 254 à 342, 524 à 647), comme le dit la dernière ligne de 12 sexies.
- Deux inexactitudes de la déclaration, sans effet (p8) : la phrase de la v8 « Les commandes des sections 10 et 11 commencent par
  `: "${REEL:?}" "${H:?}"` », remplacée l. 432-433, n'est pas nommée parmi les retraits ; les mots « réserve levée ; ancien texte :
  nom du champ à confirmer dans le code de l'outil », retirés l. 167, ne le sont pas non plus (seul le repli l'est).

## A2. M1 : fermé

L. 379-385 : le texte « nouveau » de la vérification de la v8 est repris mot pour mot (proposeur abandonné, code 0, lancement
consommé ; clé du premier fournisseur seule → P-0 ; 9,36 USD chacun ; minimum sans marge), suivi de « réduit par l'épreuve des clés
de la section 1, qui ne couvre pas un changement de clé entre l'épreuve et le lancement (≈ 2 h) ». Reste de rédaction : p6.

## A3. M2 : fermé — rapatriement suivi pas à pas (commandes `ssh` et `scp` remplacées par des fonctions factices)

| état | joué | résultat |
|---|---|---|
| arrêt (A) avant la section 6 (ni `H` ni `REEL`), bloc joué **entier** | l. 488 | « REEL: parameter null or not set », code 1, rien d'autre n'est joué — d'où la consigne |
| même état, consigne des l. 486-487 suivie (lignes 488, 491, 495 sautées) | l. 489, 490, 492, 493, 494 | les quatre copies se jouent (journaux, codes, registre, engagement, `sortie-lire-non-ouverte`), code 0 |
| `H` écrit, `REEL` non écrit (arrêt entre les sections 6 et 9) | idem | même conduite, même résultat |
| après « lancé » (`REEL=reel` écrit l. 400), puis code 3 | bloc entier | `rapatrier --source /root/pilote/reel`, puis toutes les copies : le cas que la v8 perdait est couvert |
| après le « lancé » de la relance (`REEL=reel-2` ajouté) | bloc entier | `rapatrier --source /root/pilote/reel-2` (la dernière ligne de `variables.sh` l'emporte : éprouvé) |
| section 10 sans `REEL` (l. 448, 466, 473) | chaque ligne | arrêt de la commande, code 127, rien n'est envoyé |

La garde de tête de la section 10 (l. 448) est restée, à raison (après un code 0, `REEL` est écrit). La destruction (l. 504-515)
n'emploie ni `REEL` ni `H` : rien ne peut la retenir. Restes : p1 (l'écriture de `REEL` est donnée en commentaire, et un
« lancé » non vu la fait manquer), p2 (`REEL` écrit mais dossier absent).

## A4. m1 à m9

| mineur | porté | où (v9) | reste |
|---|---|---|---|
| m1 | dans la forme | 183-184 | **MP1** : injouable à la lettre |
| m2 | oui | 233-238 | éprouvé sur six scénarios (jamais montée ; hôte rempli avant `running` ; hôte nul et port présent ; montée au troisième tour ; outil en panne ; reste d'un passage d'avant puis panne) : aucune marque remplacée à tort, plus de `HostName None`, le reste d'avant n'est plus repris ; bloc rejoué après réussite : sans effet |
| m3 | oui | 86-87 | — |
| m4 | oui | 227-229, 234, 238 | p7 (attente inutile après le troisième tour) |
| m5 | oui | 89-90 | p3 (une erreur de l'outil se lit « aucun processus ») |
| m6 | oui | 466, 473 | — |
| m7 | oui | 400, 431 | p1 |
| m8 | oui | 5, 24-25, 49, 167-168 | — |
| m9 | oui | 172 | — |

## A5. Étape d'épreuve (l. 136-157) contre R-2856 et la ligne

| exigence | constat |
|---|---|
| à la fin de la section 1, avant toute location | oui : l. 136-157, la section 2 commence l. 160 ; elle suit le dépaquetage de `arbre-local` (l. 125-126), dont elle lit la configuration |
| depuis la session qui lance | oui (l. 138-139) ; les clés sont celles de l'environnement de cette session, passées par leur nom sous `env -i` |
| une seule exécution | dite (l. 139, 156-157) ; garde mécanique : `test ! -e "$ENV/epreuve-cles.json"` (éprouvé : seconde fois → `code=1`, rien n'est joué). **Faible dans un cas** : le programme n'écrit sa sortie qu'à la fin ; une commande coupée par le délai de la session (trois appels à 120 s au plus chacun, soit 360 s, contre 120 s de délai par défaut d'une commande) ne laisse aucune sortie et la garde laisserait rejouer (p4) |
| programme tiré de la branche | oui (l. 145) ; la référence `refs/remotes/origin/lot/compte-organisme-v1` rend aujourd'hui, dans le dépôt de travail, un fichier d'empreinte `f56eaecb…` (lu sans `fetch`) |
| contrôlé par empreinte | **affiché seulement** (l. 146, attendu en commentaire) : **MP2** |
| sortie absente avant | oui (`test ! -e`) |
| montant de la ligne passé | `0.10` (l. 150) ; pire cas recalculé 0,027168 (l. 153) : juste |
| conduite sur chaque code | 0 et la ligne JSON : on continue ; 4 **ou tout autre code** : arrêt, aucune location, aucune reprise, nœud (l. 154-155) : conforme à R-2856. Les refus sans appel du programme rendent 1 (clé absente, pire cas, sortie existante) : ils tombent sous « tout autre code », ce qui est le choix prudent de R-2856 |
| écart au texte scellé « à porter au journal du pilote comme préalable d'exécution » (R-2856, point 2) | l'écart est dit (l. 137-138) ; **où et quand il est porté au journal n'est pas écrit** (p5) |
| crochet | la commande d'épreuve ne porte aucun motif de lancement d'instance : le crochet la laisse passer avec ou sans `GO_ID` (éprouvé) ; `GO_ID=GO-2026-11-15-02` y est une citation, non une garde. Il n'atteint pas le programme (`env -i` : éprouvé) |

## A6. Régressions : aucune

- **Argent, plafonds** : lignes GO-2026-11-14-13 (20 USD) et GO-2026-11-14-14 (21,72 USD), parts 12 / 8 / 9,36 / 9,36 USD, part
  machine 3 USD, prix horaire au plus 0,20 USD, pire cas 14 h : aucun bloc du différentiel n'y touche (l. 30-31, 177-180, 407-408).
- **Nœud à 2,70 USD, heure limite, arrêt par PID sur le mot de la mère** : l. 92-97, inchangées.
- **Destruction** : l. 504-522, inchangées (identifiant relu et exigé entier, étiquette comparée par programme devant
  `destroy … -y`, preuve d'absence par la liste relue, témoin, témoin vide dit).
- **Clés** : les commandes neuves n'affichent qu'un code, trois champs JSON, un compte, une adresse et un port, une ligne de
  commande de processus. `pgrep -a` affiche la ligne de commande du pilote : elle ne porte que des chemins et des empreintes (les
  clés entrent par `. cles.env` puis `exec`, l. 394), aucune clé.
- **`GO_ID=`** : la ligne de création commence de nouveau par `GO_ID=` (l. 183) ; l'aide reste « sous le même préfixe »
  (l. 163-164). Crochet joué sur entrée factice : création sans identifiant → bloquée ; création avec GO-2026-11-14-14 → bloquée
  **dans cette copie**, parce que le registre de la branche du compte ne porte pas la ligne (elle est dans celui de `main`) ;
  remarque hors différentiel : le « cas sain » de l'étape 2.1 doit être joué par la session qui lance avec cet identifiant même,
  avant de choisir une offre.
- **R10** : le constat par `pgrep` est une lecture ; le crochet l'admet (éprouvé).

## A7. Constats de la procédure

### Bloquant

Aucun.

### Majeurs

**MP1 — La ligne de création est injouable à la lettre** (l. 183-184). La v9 écrit : « pour cette seule ligne, le préambule de la
section 0 est joué dans la commande d'avant : la ligne commence par GO_ID= ». Or la section 0 pose (l. 40-41) : « Une session
d'agent ne garde pas l'état de son interpréteur d'une commande à l'autre ». Jouée dans une commande à part, la ligne n'a ni `ENV`
ni `ETIQ` (constaté sur cette session même : une variable exportée dans une commande est vide dans la suivante). Éprouvé avec un
outil factice : « ETIQ: parameter null or not set », code 127, **rien n'est créé, aucun fichier écrit** — échec du côté sûr, mais
l'exécutant est arrêté devant la seule ligne qui loue, et doit alors improviser une forme.
Ancien (l. 183-184) :
« `GO_ID=GO-2026-11-14-14 vastai create instance OFFRE --image python:3.13-bookworm --disk 20 --label "${ETIQ:?}" --raw > "$ENV/creation.json"` »
« `# (pour cette seule ligne, le préambule de la section 0 est joué dans la commande d'avant : la ligne commence par GO_ID=)` » ;
nouveau : une commande de deux lignes, le préambule sur la première, la création sur la seconde, qui commence par `GO_ID=` :
« `ENV=/home/user/pilote-mr2-v74-envoi; : "${ENV:?}"; cd "$ENV" 2>/dev/null; test -e "$ENV/variables.sh" && . "$ENV/variables.sh"` »
« `GO_ID=GO-2026-11-14-14 vastai create instance OFFRE --image python:3.13-bookworm --disk 20 --label "${ETIQ:?}" --raw > "${ENV:?}/creation.json"` »
« `# (le préambule occupe la ligne d'avant de la même commande ; la ligne de création commence par GO_ID=)` ».
Éprouvé sous cette forme avec un outil factice : étiquette lue de `variables.sh`, `creation.json` écrit, code 0.

**MP2 — L'empreinte du programme d'épreuve ne conditionne pas son exécution** (l. 144-150). Le bloc tire le programme (l. 145),
affiche son empreinte (l. 146, attendu en commentaire), puis le joue (l. 147-150) : rien n'arrête la suite si l'empreinte diffère.
Si `git show` échoue (référence absente ou non rafraîchie), le fichier est **vide**, et un programme vide rend **`code=0`**
(éprouvé, sortie absente, aucune ligne JSON), c'est-à-dire le code attendu ; seule l'absence de la ligne JSON le trahit. C'est le
seul contrôle de contenu d'une commande qui dépense sous une ligne à usage unique.
Ancien (l. 146-147) :
« `sha256sum "$ENV/epreuve_cles_pilote_v1.py"            # attendu f56eaecb…` »
« `test ! -e "$ENV/epreuve-cles.json" && GO_ID=GO-2026-11-15-02 env -i …` » ;
nouveau :
« `echo "f56eaecbe6f79aef7b4d40e794a0f317c8306326d8665ae532bf02efa0d8221f  $ENV/epreuve_cles_pilote_v1.py" | sha256sum -c - && test ! -e "$ENV/epreuve-cles.json" && GO_ID=GO-2026-11-15-02 env -i …` » (l'empreinte devient celle de la version jouée) ;
et, l. 152 : « Attendu : `code=0` **et** la ligne JSON ; un `code=0` sans cette ligne vaut « tout autre code » ».
Éprouvé : fichier vide → « rien n'est joué » ; fichier d'empreinte égale → la suite se joue.

### Mineurs

- **p1 — L'écriture de `REEL` est un commentaire, et un « lancé » non vu la fait manquer** (l. 400-401). L'instruction
  « `# dès que « lancé » s'affiche : echo REEL=reel >> …` » est dans un bloc de commandes, sous forme de commentaire ; et la ligne
  suivante dit que si la commande de lancement ne rend pas la main, on passe au suivi : alors « lancé » n'a pas été vu, `REEL`
  n'est pas écrit, et un code 3 ramène au défaut M2 de la v8 (consigne « sauter `rapatrier` » alors qu'un dossier existe).
  Ancien : la ligne 400 ; nouveau, hors du bloc, après « Attendu » (l. 404) : « **Dès que « lancé » s'affiche, ou dès que le suivi
  montre `journal-09-reel.txt` ou `code-09-reel.txt`** : `echo REEL=reel >> "$ENV/variables.sh"` (une fois) » ; même règle pour
  `reel-2` l. 431.
- **p2 — `REEL` écrit mais dossier absent** (l. 486-487) : après un code 97, ou un code 2 rendu avant la création du dossier puis
  un second code 2, `rapatrier` rend un code non nul. Ancien : « dans un arrêt (A) où REEL n'est pas écrit (aucun dossier de
  sortie réel) : sauter… » ; nouveau : ajouter « ; si `REEL` est écrit mais que `/root/pilote/$REEL` n'existe pas, `rapatrier`
  rend un code non nul : c'est attendu, les autres copies se jouent ».
- **p3 — Le constat « aucun `jouer` ne tourne » confond l'absence et l'erreur** (l. 89). Éprouvé : processus factice présent →
  listé ; absent → « aucun processus du pilote » ; **outil `pgrep` introuvable → « aucun processus du pilote » aussi**.
  Ancien : « `ssh M 'pgrep -af "[p]ilote_mr2_v74.py" || echo "aucun processus du pilote"'` » ;
  nouveau : « `ssh M 'pgrep -af "[p]ilote_mr2_v74.py"; c=$?; test $c -eq 1 && echo "aucun processus du pilote"; test $c -gt 1 && echo "constat illisible (code $c)"'` »
  (« illisible » vaut « un `jouer` tourne peut-être » : pas d'effacement des clés sur ce seul constat).
- **p4 — Épreuve : exécution unique et délai** (l. 147-150). Ajouter une marque écrite **avant** l'appel et le délai de la
  commande. Ancien : « `test ! -e "$ENV/epreuve-cles.json" && GO_ID=…` » ; nouveau : « `test ! -e "$ENV/epreuve-cles.lancee"
  && test ! -e "$ENV/epreuve-cles.json" && date -u +%Y-%m-%dT%H:%M:%SZ > "$ENV/epreuve-cles.lancee" && GO_ID=…` », et la
  phrase « commande jouée avec un délai de 600 s ; si elle est coupée ou ne rend pas la main : ne pas la rejouer, nœud ». (Sans
  objet si le programme réserve sa sortie avant les appels : e2.)
- **p5 — Conduites non écrites de l'épreuve** (l. 152-157). (i) `depense_usd` au-dessus de 0,10 : nœud (lié à ME2) ; (ii) la
  dépense proposée à la mère « depuis `depense_usd` » vaut 0 pour un appel parti dont l'usage n'a pas été lu (délai, corps
  illisible) : proposer alors le pire cas de la clé ; (iii) où l'écart au texte scellé est porté au journal du pilote (R-2856,
  point 2).
- **p6 — Section 9, phrases restées de la v8** (l. 377-379) : « La validité des clés n'est prouvée par aucun appel avant le
  lancement unique » et « Risque résiduel à trancher par la mère » précèdent encore la mention de l'épreuve, alors que R-2856 a
  tranché. Nouveau : « La validité des clés est éprouvée une fois à la section 1 (GO-2026-11-15-02, R-2856). Risque restant : … »,
  en ajoutant ce que l'épreuve ne couvre pas, outre le changement de clé : **le modèle de `fable52`** (même clé, même adresse,
  modèle différent : l'épreuve n'appelle que `opus55`, la ligne disant « un appel par clé ») ; un quota suffisant pour 16 jetons
  et non pour un appel du pilote ; le chemin de réseau (l'épreuve part de la session, le pilote de la machine louée).
- **p7 — Attente après le troisième tour** (l. 236) : la commande dure ≈ 95 s plus trois appels de l'outil, près du délai par
  défaut d'une commande. Ancien : « `…; rm -f "$ENV/adresse-port.txt"; sleep 30; done` » ; nouveau :
  « `…; rm -f "$ENV/adresse-port.txt"; test $k -lt 3 && sleep 30; done` ».
- **p8 — Déclaration** : les deux inexactitudes de A1, à porter dans la section du différentiel suivant.

---

# Partie B — programme `epreuve_cles_pilote_v1.py`

## B1. Ce qui est vérifié et tient

| question | constat (ligne du programme ; essai) |
|---|---|
| clés lues par leur nom | l. 67, 76 : `os.environ[conf["proposeurs"][n]["variable_cle"]]` ; les trois noms sont ceux de la configuration v12 |
| refus avant tout appel | sortie existante (l. 58-59), pire cas au-dessus de la ligne (l. 64-65), une clé absente ou vide — **les trois contrôlées avant le premier appel** (l. 66-68) ; adresse d'essai non locale (l. 55-56). Éprouvé : quatre refus, code 1, aucune sortie écrite (par lecture : chaque refus précède la boucle d'appels). Une adresse d'essai à nom d'usager (`http://127.0.0.1:1@…`) passe le contrôle de préfixe mais n'aboutit pas (`erreur:URLError` pour les trois clés, code 4) |
| un seul appel par clé, aucune reprise | une boucle, un `urlopen` par clé (l. 73-80), aucune boucle de reprise. Bibliothèque : `urllib` ne reprend pas ; éprouvé sur doublure avec en-têtes `Retry-After` et `x-should-retry` : **une requête par clé exactement** sur 401, 429, 500, 529, corps illisible, 307, port fermé. **Une exception** : e1 (redirection 302) |
| borne de sortie réellement passée | éprouvé, corps reçus par la doublure : `max_tokens=16` (premier fournisseur), `generationConfig.maxOutputTokens=16` (`argon`), `max_completion_tokens=16` (`astra`) : mêmes champs que le relais du pilote (`relais_pilote_v70.py` l. 80-87). Pour `argon`, que ce champ borne la réflexion reste **non vérifié** (ME2) |
| pire cas recalculé | 28 octets de consigne ; (28 + 1024) × prix d'entrée + 16 × prix de sortie : `opus55` 0,004528 ; `argon` 0,011320 ; `astra` 0,011320 ; **total 0,027168 USD** : égal au devis, à la ligne et à la procédure |
| adresses et modèles | pris de la configuration elle-même (`url_amont`, `modele`, l. 75-76), rien en dur ; pour `argon` le modèle est dans l'adresse, égal au champ `modele` (contrôlé par programme) ; en-têtes égaux à ceux du relais (l. 28, 31, 34 contre relais l. 191-197), hors flux |
| aucune clé, aucun corps, aucun identifiant affiché ni écrit | sortie : statut, vrai ou faux, deux entiers, un coût, le **nom** de la variable (l. 77, 94) ; écran : trois champs (l. 99). Erreur HTTP : seul le code (l. 83-84), le corps n'est pas lu. Autre erreur : seul le **nom du type** (l. 86-87). Éprouvé : corps d'erreur et clés marqués, recherchés dans tous les écrans et toutes les sorties de douze scénarios : **aucune occurrence**. Clé à saut de ligne → `erreur:ValueError`, clé non latine → `erreur:UnicodeEncodeError`, sans afficher la valeur. Traces de pile non rattrapées (configuration illisible, arguments manquants, sortie non inscriptible) : elles ne citent que des lignes du programme et un chemin, jamais une valeur de variable |
| codes de sortie | 0 : trois statuts 200 et trois « conforme » ; 4 : sinon, après les appels ; 1 : refus avant appel (`sys.exit` d'un texte) **et** erreur non rattrapée ; 2 : usage de l'interprète. Le devis et l'en-tête ne disent que « 0, 4 sinon » (e5) |
| « modèle servi conforme » | `str(servi).startswith(p["modele"])` (l. 90), `servi` lu dans `model` ou `modelVersion` (l. 41, 45, 47) : **ME1** |

## B2. Essai local rejoué (doublure versée, port 8899 de la boucle locale, clés factices, aucun réseau)

Commande : la doublure `essai-local/doublure-essai.py` lancée puis arrêtée par son PID ; le programme sous
`env -i PATH=/usr/bin:/bin HOME=/root` avec trois clés factices, configuration v12, montant 0.05, `--amont-essai http://127.0.0.1:8899`.

```
{"toutes_valides": true, "depense_usd": 0.00068, "pire_cas_usd": 0.027168}
code=0
```

Sortie écrite : égale, champ pour champ, à `essai-local/sortie-essai-doublure.json` (`64246013…`) ; aucune clé factice dedans.
Refus rejoués : « REFUS : sortie existante » (1) ; « REFUS : clé … absente (nom seul) » (1, aucune sortie) ; « REFUS : pire cas
0.027168 > ligne 0.02 » (1) ; « REFUS : --amont-essai n'admet que la boucle locale » (1).

**À noter dans l'essai versé lui-même** : la doublure sert pour `astra` l'identifiant demandé suivi de `-2026`, et le programme
le dit « conforme ». La règle du pilote, sur la même forme, dit « non conforme » (ME1).

Scénarios ajoutés par ce lecteur (seconde doublure, dossier temporaire) :

| scénario | écran | code | requêtes |
|---|---|---|---|
| 401, 429, 500, 529 (corps d'erreur marqué) | `toutes_valides` faux, dépense 0 | 4 | 3 |
| 200, corps non JSON | faux (`erreur:JSONDecodeError`) | 4 | 3 |
| 200, **usage absent** | **vrai**, dépense 0 | **0** | 3 |
| 200, modèle servi = demandé + `-mini` | **vrai** | **0** | 3 |
| 200, modèle servi = demandé + date réelle | vrai | 0 | 3 |
| 200, modèle servi préfixé `models/` | faux | 4 | 3 |
| 200, **32 000 jetons de réflexion chez `argon`** | **vrai, `depense_usd` 1.60068**, ligne 0.10 | **0** | 3 |
| 302 vers une autre adresse | faux | 4 | **6** (trois `GET` de plus, **clé présente**) |
| 307 | faux (statut 307) | 4 | 3 |
| dossier de sortie absent | trace de pile, **rien d'écrit après trois appels** | 1 | 3 |
| port fermé | faux (`erreur:URLError`) | 4 | 0 |
| montant `nan` | aucun refus | 0 | 3 |

## B3. Constats du programme

### Bloquant

Aucun.

### Majeurs

**ME1 — « Modèle servi conforme » est plus lâche que la règle du pilote, et l'usage absent passe** (l. 90, 95). Le pilote
(`commande_pilote_v70.py` l. 113-126, 255-262) n'admet que l'identifiant exact ou suivi d'un suffixe de **date réelle**, et rend
« echec » sur `modele_servi` comme sur `usage_absent` — les deux causes d'**abandon du proposeur**
(`proposeurs_pilote_v70.py` l. 41). L'épreuve admet tout identifiant qui **commence par** le demandé, et un 200 sans usage.
Comparé sur chaînes factices (fonction du pilote contre règle de l'épreuve) : exact, date compacte, date à tirets → vrai / vrai ;
`-2026`, `-mini`, `-preview`, date impossible → **faux pour le pilote, vrai pour l'épreuve**. L'épreuve peut donc rendre 0 dans
le cas même qu'elle doit écarter : un proposeur abandonné au premier appel du lancement unique.
Ancien (l. 89-90) : « `if servi is not None:` / `ligne["modele_servi_conforme"] = str(servi).startswith(p["modele"])` » ;
nouveau : la règle du pilote recopiée (le programme est joué hors de l'arbre, sous `-I`) :
« `SUFFIXE = re.compile(r"-(?:(\d{4})(\d{2})(\d{2})|(\d{4})-(\d{2})-(\d{2}))")` » ;
« `def conforme(demande, servi):` / `    if not isinstance(servi, str): return False` / `    if servi == demande: return True` /
`    m = SUFFIXE.fullmatch(servi[len(demande):]) if servi.startswith(demande) else None` / `    if m is None: return False` /
`    a, mo, j = [int(x) for x in m.groups() if x is not None]` /
`    try: datetime.date(a, mo, j)` / `    except ValueError: return False` / `    return 2000 <= a <= 2099` » ;
« `ligne["modele_servi_conforme"] = conforme(p["modele"], servi)` » (posé aussi quand `servi` est nul : faux) ;
et l. 95 : « `all(l["statut"] == 200 and l["modele_servi_conforme"] and l["cout_usd"] is not None for l in …)` ».
Cette fonction, éprouvée ici sur quinze chaînes factices, rend partout le même résultat que celle du pilote.
La doublure de l'essai local est à aligner (`-2026` → une date réelle), avec un cas « non conforme » versé.

**ME2 — La dépense lue n'est jamais comparée à la ligne** (l. 62-65, 95-100). Le refus d'avant appel ne compte que 16 jetons de
sortie par clé. Chez `argon`, la configuration dit la réflexion comptée **hors** de la sortie (`reflexion_comprise` faux) et le
devis réserve que la borne ne la limite peut-être pas ; le programme additionne bien les jetons de réflexion (l. 44), mais ne fait
rien du total : éprouvé, **`depense_usd` 1,60068 sous une ligne de 0,10, `toutes_valides` vrai, code 0**. La borne propre du
pilote pour `argon` (36 000 jetons) donne l'ordre de grandeur du pire cas non borné : 1,80 USD. Peu probable sur une consigne d'un
mot (le devis cite 786 jetons observés sur un calcul, soit 0,0393 USD, couverts par la ligne), mais c'est exactement la réserve, et
rien ne la signale.
Ancien (l. 100) : « `sys.exit(0 if res["toutes_valides"] else 4)` » ;
nouveau : avant l'écriture, « `res["depassement"] = res["depense_usd"] > montant` », `depassement` ajouté aux champs imprimés
(l. 99), puis « `sys.exit(5 if res["depassement"] else 0 if res["toutes_valides"] else 4)` » ; la procédure traite déjà « tout
autre code » par l'arrêt et le nœud. (Borner la réflexion dans le corps envoyé changerait la forme de l'appel par rapport à celle
du pilote et n'est pas vérifiable sans appel : je ne le propose pas.)

### Mineurs

- **e1 — Une redirection 302 fait partir une seconde requête, clé comprise** (l. 79). `urllib` suit 301, 302 et 303 d'un `POST`
  par un `GET` qui garde les en-têtes : éprouvé, trois `GET` de plus, clé présente. Aucun des trois fournisseurs ne redirige en
  temps normal, mais « un seul appel par clé » n'est alors plus vrai. Nouveau : un ouvreur sans redirection,
  « `class SansRedirection(urllib.request.HTTPRedirectHandler):` / `    def redirect_request(self, *a, **k): return None` »,
  « `ouvreur = urllib.request.build_opener(SansRedirection, urllib.request.HTTPSHandler(context=ctx))` », `ouvreur.open(…)` à la
  place de `urlopen` (un 3xx devient un statut rendu, code 4).
- **e2 — La sortie n'est écrite qu'à la fin** (l. 97-98). Dossier absent ou commande coupée : trois appels payés, **aucune trace**,
  et la garde « sortie absente » de la procédure laisse rejouer. Nouveau : réserver la sortie avant les appels —
  « `f = open(sortie, "x", encoding="utf-8")` » à la place du contrôle des l. 58-59 (un fichier présent lève, à rendre en
  « REFUS : sortie existante »), y écrire tout de suite `{"version": …, "etat": "appels en cours"}`, puis le résultat à la fin.
- **e3 — Montant non fini** (l. 57, 64) : `nan` ne déclenche pas le refus (éprouvé). Nouveau : « `if not (math.isfinite(montant)
  and montant > 0): sys.exit("REFUS : montant illisible")` ».
- **e4 — Dépense comptée 0 pour un appel parti sans usage lu** (l. 85, 88, 96) : délai dépassé pendant la lecture, corps illisible,
  usage absent. Nouveau : dans ces cas (tout sauf une erreur HTTP et une erreur d'avant envoi), `cout_usd` = pire cas de la clé,
  avec « `"cout_origine": "pire_cas"` », comme le fait le pilote.
- **e5 — Codes** : le refus d'avant appel et l'erreur non rattrapée rendent tous deux 1 ; l'en-tête (l. 5-8) et le devis ne
  nomment que 0 et 4. Nouveau : refus → `sys.exit(2)` après le message, et la liste des codes dans l'en-tête.
- **e6 — Délai** (l. 79) : 120 s par appel, 360 s au pire pour le programme, au-dessus du délai par défaut d'une commande de
  session. Nouveau : 60 s par appel, ou le délai de 600 s écrit dans la procédure (p4).
- **e7 — Portée, à dire dans l'en-tête** : l'épreuve prouve une clé et un modèle par clé ; elle ne prouve pas l'accès au modèle de
  `fable52` (un appel de plus coûterait au pire 0,009056 USD, total 0,036224, mais la ligne dit « un appel par clé » : hors de
  la ligne, à la mère). Elle n'envoie pas non plus le réglage `output_config` que le pilote envoie aux deux premiers proposeurs.

## B4. Ce qui se passe si le programme est joué tel quel (v1, empreinte de R-2856)

- Clés, corps, identifiants : rien ne fuit (éprouvé).
- Appels : un par clé, sauf redirection 302 (non attendue).
- Argent : pire cas 0,027168 USD si la borne de `argon` tient ; sinon la dépense réelle est lue dans `depense_usd`, que
  l'exécutant doit alors **comparer lui-même à 0,10** (le code reste 0).
- Verdict : un `code=0` prouve trois clés acceptées ; il ne prouve pas que le modèle servi passera la règle du pilote si
  l'identifiant servi n'est ni exact ni daté : l'exécutant ne peut pas le vérifier, la sortie ne portant jamais l'identifiant.

Les deux majeurs ne se rattrapent donc pas tous deux par la seule procédure : ME2 oui (une phrase), ME1 non.

## Pièces

- Essais : dossier temporaire de la session du lecteur, hors de tout dépôt
  (`/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/lecteur-v9/` : `e1` à `e3` pour le programme, `f1` à `f4` pour la
  procédure, `doublure2.py`).
- Rien d'autre n'a été écrit dans la copie que ce rapport et son compagnon ; aucun commit, aucune poussée.
