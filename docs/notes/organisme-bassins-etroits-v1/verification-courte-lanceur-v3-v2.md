# Vérification courte du différentiel v2 → v3 du lanceur de l'atelier d'idées sur les bassins étroits — v2

Vérificateur neuf : **Claude Fable 5.2** (`claude-fable-5-2`). Je n'ai écrit ni le lanceur v1, ni le v2, ni le v3, ni leurs
contre-lectures. 13 novembre 2026, de 17:59 à 18:19 UTC (heures relevées par `date -u`). Vérification refaite en entier ;
rien repris de la première, interrompue. **Aucune dépense, aucun appel à un fournisseur de modèles, aucune machine créée,
aucune opération git, aucune valeur de clé lue ; le lanceur n'a jamais été lancé avec ses réglages de production ;
`.claude/` lu et non modifié ; rien corrigé.** Aucun refus de permission ni de classifieur.

## Verdict

**« Non autorisable » en l'état : le lanceur v3 scellé (`3fabd71e…`) refuse, dans ce conteneur, la relance pour laquelle il
a été écrit** (constat B1). Le conteneur a été remplacé après le rendu du préparateur (fichiers du dépôt datés de 17:45
UTC) : le dossier de sortie hors dépôt de la course du v2 (`/home/user/sorties-course-ideation-bassins-etroits-v2/…`) a
disparu, et le v3 y lisait la fin propre du superviseur et la dépense de 0,275477 USD. Sans lui, il compte le plafond entier
(20 USD), dit la dépense « illisible » et refuse la relance. **Le refus est sûr (rien ne part, rien n'est dépensé), mais
épingler le v3 ne servirait à rien : il faut un v4**, ou une décision écrite sur la manière d'attester une course dont les
traces hors dépôt sont perdues. Reconstituer ce dossier à la main serait fabriquer des pièces de course : à ne pas faire.

Hors de ce point, le différentiel est sain : la cause du 401 est établie et je l'ai reproduite ; le v3 la supprime ;
l'environnement passe par une liste de noms ; la relance est étroite ; le verrou et l'orphelin tiennent ; le plafond de
60 USD est tenu par la garde de cumul. **1 bloquant (d'emploi, sans risque d'argent), 2 majeurs, 9 mineurs.**
Si le dossier hors dépôt existait encore ailleurs, intact, le verdict serait « autorisable sous conditions » (M1, M2).

## Ce que j'ai fait

- Empreintes vérifiées contre leurs compagnons avant lecture : lanceur v2 `c6d82d8c…`, lanceur v3 `3fabd71e…`, essais du
  v3 `6ab6ec5d…`, rapport du préparateur v3 `348a5208…`, ses cinq outils et résultats (tous « OK »), contre-lecture du v1
  `3aaf9981…`, vérification courte du v2 `ff33dd99…`, deux fichiers d'essais du crochet. Le crochet
  `.claude/hooks/garde_calcul.py` (`73be0638…`) et `.claude/settings.json` (`701169ae…`) n'ont pas de compagnon.
- Lanceur v3 lu en entier (1 518 lignes). Différentiel recalculé par `diff -u` : **égal, octet pour octet hors les deux
  lignes d'en-tête datées, au différentiel scellé** (`b2951d17…`) ; 203 lignes ajoutées, 81 retirées, toutes lues.
- Registre lu : R-2530, R-2535 à R-2545, R-2549 ; ligne GO-2026-11-13-03 ; compte rendu d'opération de la génération 1
  (`operation-g1-v1.md`) ; manifeste de fin du run du v2 ; enveloppe d'Argon v5 (`37c0205e…`).
- Essais du v3 rejoués deux fois ; banc de mutations du préparateur rejoué tel quel ; douze épreuves à moi sur le faux
  orchestrateur des essais scellés ; rejeu réduit de l'épreuve d'authentification dans un espace réseau isolé.
- **Installé par le gestionnaire de paquets du système** (routine, R-2536) : `bubblewrap` 0.9.0 (après `apt-get update`),
  pour le seul rejeu de l'épreuve d'authentification. `socat` non installé : aucun essai ne l'a exigé.

## Constats

### Bloquant

**B1 — Dans ce conteneur, le v3 refuse la relance de la génération 1.** Épreuve P1 (lecture seule, réglages de production,
fonctions `runs_du_lanceur`, `depense_run`, `relance_permise`) : le run du v2 est bien lu dans le dépôt (manifeste de fin :
code 2, « fin propre »), mais `depense_run` lit le code scellé du superviseur dans
`<dossier hors dépôt>/superviseur-course/code.json` (`lire_code`, lanceur l. 711 et 881) et la dépense dans
`<dossier hors dépôt>/sortie-controle/tentative-1.json` (l. 793-834). Les deux ont disparu avec le conteneur. Résultat :
`course_usd` 20,0, `course_lisible` faux, « processus mort sans fin propre, ou en marche : plafond entier compté » ;
`relance_permise` rend « dépense illisible » ; la garde de cumul compte 20 USD au lieu de 0,275477. L'essai scellé
`test_run_reel_du_v2_reconnu` échoue ici pour la même raison. **Sens du défaut : fermé** (refus, aucun lancement).
*Ce qu'il faut* (nœud pour la mère, peut-être pour Lazar puisque c'est la règle « dépense lisible » qui change) : un v4 qui
admet, pour ce run nommé et lui seul, un relevé scellé dans le dépôt (0,275477 USD, aucune fiche ; source :
`operation-g1-v1.md` `3beef39e…` et `manifeste-lanceur-fin.json` `24c5d6ae…`, qui porte déjà le code scellé), épinglé par
son empreinte dans le lanceur. Plus largement : toute preuve dont dépend une relance ou le cumul devrait vivre dans le dépôt
(copie scellée du code et de la tentative de contrôle à la clôture), puisque le conteneur peut être remplacé à tout moment.

Autres états de ce conteneur qui arrêteraient aussi le lanceur, par ses gardes et à bon droit (routine, pas des défauts) :
clone de l'orchestrateur au commit `65101990…` au lieu de `be6b5af9…` (l'objet épinglé n'y est même pas présent) ; `socat`
absent (bac à sable) ; relais à relancer.

### Majeurs

**M1 — Le crochet n'est pas chargé, et le lanceur ne garde pas lui-même ce que l'épingle garde** (détail : réponse au
point 8). Sans crochet, rien ne vérifie que le fichier lancé est celui que j'ai lu, ni que la commande est la commande exacte.
Condition d'emploi tant que le crochet n'est pas chargé : la procédure du point 8.

**M2 — Point R3, non corrigé : la fenêtre entre le détachement et le manifeste de départ contient un sous-processus.**
Après `lancer_detache` (l. 1433), le lanceur calcule encore `sha256_fichier(mesure-consignes.json)` et surtout
`_depot_git(r)` (l. 1450) : deux commandes git sur le dépôt de travail, délai de 60 secondes chacune ; `_depot_git` ne
rattrape que `Refus`, pas `subprocess.TimeoutExpired`. Un git lent, une erreur d'écriture, un signal : le lanceur sort par
une trace Python, sans imprimer l'identifiant de processus du superviseur. Épreuve P2 (panne simulée à l'écriture du
manifeste de départ) : la course tourne, non suivie ; le dossier de run n'a ni manifeste de départ ni de refus ; **toute
invocation suivante, pour toute génération, rend « état inconnu » (code 2)**, y compris le compte rendu « en marche » et la
clôture ; cela ne se lève jamais seul. Le défaut déclaré est donc exact, à une précision près : « sans dépense » veut dire
« sans dépense de plus » ; la course partie, elle, peut dépenser jusqu'à ses plafonds (20 USD, dans le GO), sans manifeste
de départ, et son PID ne se trouve que dans `<sorties>/<identifiant>/superviseur-course/pid-orchestrateur.json`. Majeur parce
que la fenêtre n'est pas de quelques instructions, que la relance est la dernière permise, et que la correction est simple :
calculer avant le détachement tout ce qui peut échouer, et, si l'écriture du manifeste échoue, imprimer au moins le PID et la
commande d'arrêt. À faire dans le v4 que B1 impose de toute façon. *Emploi, en attendant* : si la commande de lancement finit
par une trace, lire ce fichier et arrêter ce PID (`kill -TERM`, par PID).

### Mineurs

- **m1 — Perte partielle du dossier hors dépôt** (P3b) : si le sous-dossier `sortie` disparaît seul après une course qui a
  produit des fiches (4,5 USD dans l'épreuve) alors que `superviseur-course/code.json` reste, le v3 lit « rien parti », 0 USD,
  aucune fiche, et **permet la relance** ; le cumul perd la dépense. La perte entière, elle, ferme (P3a, B1). Même famille
  que B1 : « sortie absente » vaut preuve d'absence de fiches (`fiches_produites`, l. 969). Demande une suppression à la
  main ; à fermer par la même correction (preuves dans le dépôt).
- **m2 — Orphelin non vu si le superviseur meurt avant d'écrire `pid-orchestrateur.json`** (P6, artefact) : clôture « mort
  sans fin propre », code 0, orchestrateur vivant non signalé. L'argent reste gardé (plafond compté, génération
  verrouillée). Fenêtre : entre le lancement de l'orchestrateur et l'écriture du fichier, dans le superviseur.
- **m3 — Une relance par génération, pas une sur la ligne** (P5) : la génération 2 et la génération 3 peuvent chacune être
  relancées une fois aux mêmes conditions, soit trois relances au plus. Le plafond reste tenu par la garde de cumul. À dire à
  Lazar si son mot visait « une seule relance » en tout.
- **m4 — Quatre essais du v3 dépendent de l'état de la machine** et échouent au lieu d'être sautés : trois exigent le clone
  de l'orchestrateur au commit épinglé, un exige le dossier hors dépôt. Le seul essai qui tue le mutant W11 (runs du v2 non
  lus) est celui-là : W11 n'est pas décidable ici.
- **m5 — Les noms des 195 variables d'environnement de la session sont écrits au manifeste de départ** (`noms_exclus`), donc
  dans le dépôt. Aucune valeur (P4, P4b). Des noms peuvent décrire l'hôte ; à garder hors de la copie publique expurgée.
- **m6 — L'épreuve d'authentification ne prouve pas la suite** (dit par le préparateur) : ni que le vrai relais accepte la
  requête, ni que le kit tourne dans le bac à sable réel de l'orchestrateur avec un HOME neuf. Un second défaut au contrôle
  coûterait de nouveau le contrôle d'Argon (≈ 0,28 USD) et verrouillerait la génération 1 pour de bon. Avec le v3, le kit
  envoie aussi un `HEAD /api/hello` sans en-tête au relais (sonde de connectivité, non un appel).
- **m7 — Phrase inexacte du rapport** (§ 5) : « le v2 relancé verrouillerait la génération 1 et rejouerait le 401 ». Le v2
  ne rejoue rien : il refuse la génération 1 (dépense relevée au-dessus de son seuil, ou plafond compté ici). Le v2 est inerte
  tant que son dossier de run reste dans le dépôt. Le retirer de la règle reste juste.
- **m8 — `LANG` n'est pas dans l'environnement de cette session** : le v3 ne transmet ici que `PATH`, plus `GO_ID`, `HOME` et
  `PYTHONPYCACHEPREFIX`. C'est aussi ce que l'épreuve « V3 » a joué. À savoir.
- **m9 — Verrou propre au v3** : il n'exclut pas une invocation du v2 (qui n'a pas de verrou et ne voit pas les runs du v3).
  Sans effet tant que le v2 est inerte (m7) ; raison de plus de retirer sa règle.

## Les neuf points de la demande

**(1) Différentiel ligne à ligne.** Conforme à la liste du rapport (§ 4), rien de plus. Les gardes d'entrée du v2 (GO,
orchestrateur, pièces, sommes, tailles, règle de passage, attestations, commandes) sont inchangées au caractère près.
`SEUIL_SANS_DEPENSE_USD` et la boucle des trois tentatives gratuites du v2 sont remplacés par `relance_permise`. Aucune garde
du v2 n'est affaiblie, sauf ce changement voulu : une relance devient possible après une dépense lue.

**(2) Cause du 401.** Établie, et reproduite par moi (18:07 à 18:09 UTC ; `rejouer_authentification_kit_reduit_v1.py`, qui
reprend telle quelle la fonction d'épreuve de l'outil scellé du préparateur ; espace réseau vérifié réduit à la boucle
locale avant de jouer ; kit `claude_agent_sdk` 0.2.172 ; faux amont local qui rend 401) :

| Environnement hérité | Appels au faux amont | Authentification présentée |
|---|---|---|
| A, celui du v2 | 1, plus `GET /v1/code/agent-proxy/ca-cert` | `Authorization: Bearer`, autre que le jeton factice |
| A moins `CLAUDE_CODE_REMOTE` seule | 1 | `x-api-key` égale au jeton factice ; message « <synthetic> » du kit sur le 401 |
| V3 (`environnement_permis` du lanceur `3fabd71e…`, HOME neuf) | 14 | `x-api-key` égale au jeton factice |

`CLAUDE_CODE_REMOTE` est présente dans ma session comme dans celle de la course. **Le v3 la supprime vraiment** : elle n'est
pas dans `NOMS_PERMIS`, la liste refuserait tout nom en `CLAUDE`, `ANTHROPIC` ou `CCR` (l. 608-610), et le faux orchestrateur
des essais ne la voit pas (P4b, `test_trois_generations_bout_en_bout`, mutant W10 tué). L'enveloppe d'Argon ne perd rien :
son contrat est l'environnement minimal posé par l'orchestrateur, clé factice, relais sur la boucle locale sans mandataire.
Non vérifié : le code de l'orchestrateur au commit épinglé (absent de ce conteneur) ; limites en m6.

**(3) Environnement par liste de noms permis.** Tenu. `environnement_permis` (l. 603-622) ne lit de valeur que pour les
noms de `NOMS_PERMIS` (PATH, LANG, LC_ALL, TZ, TMPDIR) ; fixe GO_ID, HOME (dossier neuf hors dépôt, par course et par
bras) et PYTHONPYCACHEPREFIX ; n'écrit au manifeste que des noms. Le lanceur ne lit aucune clé, par aucun chemin : les clés
vivent chez les relais. `prefixe_essais` vaut `None` en production et seul « FAUX_ » est admis.

**(4) Relance étroite.** Tenue par le code (`relance_permise`, l. 978-996 ; `etat_generation`, l. 1014-1016) : chaque
course précédente doit avoir un manifeste de fin avec un code scellé, aucun bras, une dépense lisible, aucune fiche prouvée ;
deux courses par génération au plus ; le run du v2 compte pour la première (`ANTERIEURS`). La dépense lue entre au cumul ;
la garde exige « dépense relevée + 20 ≤ 60 » avant toute course et « + 3,1 ≤ 60 » avant tout bras, tout illisible comptant
son plafond ; le verrou empêche deux gardes de passer avec le même cumul. **Plafond de 60 USD tenu.** Réserves : B1 (ici le
run du v2 compte 20 et non 0,275477 : la relance est refusée), m1, m3. Devis v3 non revérifié.

**(5) Verrou et orphelin.** Verrou : `fcntl.flock` exclusif non bloquant, pris avant toute lecture de l'état, rendu à la
sortie même brutale, descripteur non hérité par le superviseur (essais R1, mutant W7 tué). Orphelin : superviseur mort sans
code, orchestrateur vivant (PID et heure de départ du processus) → clôture « ORCHESTRATEUR ENCORE VIVANT », commande d'arrêt
par PID, **code 4** ; tant qu'il vit, toute invocation rend 4 et rien ne part ; mort, la génération reste verrouillée et son
plafond compté (essai R2, mutants W8 et W9 tués). Réserves : m2, m9.

**(6) Point R3 et défaut déclaré.** M2 ci-dessus. Le défaut déclaré est vrai ; sa portée est plus large que dit.

**(7) Épingle.** Couples ci-dessous, **non appliqués**, éprouvés sur une copie en mémoire (P9, P9b).

**(8) Crochet non chargé.** Réponse ci-dessous.

**(9) Comptes.** Ci-dessous.

## Réponse au point (8) : le v3 garde-t-il lui-même ce que l'épingle aurait gardé ?

Le crochet n'est pas chargé dans ma session non plus : à 17:59 UTC, mes commandes `sha256sum` citant le lanceur v2 sont
passées ; le même script, joué à la main avec la même commande, la bloque (P8, code 2). Le crochet actuel ne connaît pas le
v3 : même chargé, il laisserait passer toute commande qui le cite. Cause probable, non vérifiée : le dossier de projet de la
session est `/home/user` (pas de `/home/user/.claude/`), pas le dépôt.

| Ce que l'épingle garde | Le v3 le garde-t-il seul ? |
|---|---|
| **Empreinte du lanceur** | **Non.** Il écrit sa propre empreinte au manifeste (l. 1272, 1485) et ne la compare à rien, ni à son compagnon. Un fichier modifié se lance. |
| **Commande exacte** | **En partie.** Interpréteur : oui (`/usr/local/bin/python3` exigé, l. 336). Options `-I -B` : non (`sys.flags` jamais lu). Dossier courant : sans objet (chemins absolus, dépôt comparé à celui de l'enveloppe). Argument : `1`, `2` ou `3` ; l'épingle ne permet que `1`. Les générations 2 et 3 restent tenues par la confirmation scellée de la règle de passage et l'attestation. |
| **Ligne de GO** | **Oui, par son contenu** : une seule ligne principale, type calcul, accordée par Lazar, dans sa période, non révoquée, périmètre, plafond lu ≥ 60 (l. 281-327). L'empreinte de la ligne est écrite, non épinglée. C'est plus que le crochet, qui ne lit pas le GO pour ce lanceur. |
| **Plafond** | **Oui** : constantes du fichier, `garde_sommes`, `garde_cumul` à min(60, plafond du GO). |
| **Une seule relance** | **Oui**, depuis l'état du disque, sous le verrou ; sens fermé si les traces manquent (B1), sauf m1. |
| Refus d'édition du lanceur et de son compagnon | Non : règle de `settings.json`, pas chargée non plus. |

**Ce qui manque**, donc : l'intégrité du fichier lancé et l'exactitude de la commande. Trois manières, à cumuler :

1. *Dans le v4* (peu de lignes) : refuser si `sys.flags.isolated` ou `sys.flags.dont_write_bytecode` est faux ; refuser si sa
   propre empreinte diffère de son compagnon `.sha256` (garde contre l'accident, pas contre une réécriture des deux) ;
   refuser les générations 2 et 3 tant qu'une pièce scellée du dépôt ne les ouvre pas.
2. *Procédure, dès maintenant, crochet chargé ou non* : juste avant de lancer, l'opérateur **joue le crochet à la main** avec
   la commande exacte (`printf '%s' '{"tool_input":{"command":"<commande>"},"cwd":"/home/user/controle-ia-travail"}' |
   /usr/local/bin/python3 -I -B .claude/hooks/garde_calcul.py`, code 0 exigé, crochet d'empreinte consignée), puis lance la
   commande, sans rien entre les deux. Le crochet épinglé rend alors la même décision qu'en automatique : empreinte du
   fichier égale à l'épingle et au compagnon.
3. *Charger le crochet* : décision de Lazar (R-2545, R-2549), hors de mon mandat ; je n'ai rien touché.

## Couples de l'épingle (proposés, non appliqués)

Source unique, scellée : `verification-outils-v3-v2/couples-epingle-lanceur-v3-v1.json` (`7b77e1fe…`). Chaque texte d'origine
figure une seule fois dans son fichier (vérifié). Choix : **l'épingle du v2 est retirée en vidant la liste de ses commandes
permises**, non en supprimant sa garde ; ainsi plus aucune commande du v2 ne passe et toute citation de son nom reste
bloquée (sens fermé). L'épingle du v3 vaut pour la génération 1 seule, comme celle du v2. Si un v4 est écrit, mêmes couples
avec son nom et son empreinte.

### `.claude/hooks/garde_calcul.py` (empreinte avant : `73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850`)

**H1 — retrait de l'épingle du v2 (plus aucune commande du v2 ne passe ; toute citation reste bloquée)**

Texte d'origine (une seule occurrence) :

```python
COMMANDES_LANCEUR_BE2 = ("/usr/local/bin/python3 -I -B scripts/" + FICHIER_LANCEUR_BE2 + " 1",)
```

Texte neuf :

```python
COMMANDES_LANCEUR_BE2 = ()  # épingle du v2 retirée : aucune commande du v2 ne passe plus ; toute citation reste bloquée
```

**H2 — constantes de l'épingle du v3**

Texte d'origine (une seule occurrence) :

```python
CITE_LANCEUR_BE2 = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(NOM_LANCEUR_BE2) + r"(?![A-Za-z0-9_])")
```

Texte neuf :

```python
CITE_LANCEUR_BE2 = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(NOM_LANCEUR_BE2) + r"(?![A-Za-z0-9_])")

# --- 5. garde d'empreinte du lanceur de l'atelier d'idées « bassins étroits » v3 ; GO-2026-11-13-03, mots de Lazar R-2530
#        (« go règle de permission »), lanceur v3 (R-2549). Génération 1 seulement : les générations 2 et 3 attendent son mot.
NOM_LANCEUR_BE3 = "lancer_course_ideation_bassins_etroits_v3"
FICHIER_LANCEUR_BE3 = NOM_LANCEUR_BE3 + ".py"
EMPREINTE_LANCEUR_BE3 = "3fabd71e63bf9f3e830ed5128cd6a92f04ca91c0b13dabcc0ac7d316e5f44b36"
COMMANDES_LANCEUR_BE3 = ("/usr/local/bin/python3 -I -B scripts/" + FICHIER_LANCEUR_BE3 + " 1",)
CITE_LANCEUR_BE3 = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(NOM_LANCEUR_BE3) + r"(?![A-Za-z0-9_])")
```

**H3 — fonction sœur garder_lanceur_be3**

Texte d'origine (une seule occurrence) :

```python


def decider(commande: str, aujourd_hui: date, cwd=None) -> None:
```

Texte neuf :

```python


def garder_lanceur_be3(commande: str, cwd) -> None:
    """5. Même garde, pour le lanceur « bassins étroits » v3 : commande exacte parmi celles permises, depuis le dépôt,
    fichier non lien symbolique, empreinte égale à l'épingle et au compagnon. Rien en silence (R5)."""
    if not CITE_LANCEUR_BE3.search(commande):
        return
    m = "empreinte du lanceur « bassins étroits » v3 (R-2530, R-2549)"
    if commande not in COMMANDES_LANCEUR_BE3:
        bloquer(f"{m} : commande citant {NOM_LANCEUR_BE3} qui n'est pas exactement l'une de {list(COMMANDES_LANCEUR_BE3)}")
    if not isinstance(cwd, str) or not cwd:
        bloquer(f"{m} : dossier courant absent de l'entrée du crochet ; {DEPOT_COURSE} exigé")
    if os.path.realpath(cwd) != os.path.realpath(DEPOT_COURSE):
        bloquer(f"{m} : lancé depuis {cwd}, {DEPOT_COURSE} exigé")
    if os.path.realpath(RACINE) != os.path.realpath(DEPOT_COURSE):
        bloquer(f"{m} : crochet de {RACINE}, celui de {DEPOT_COURSE} exigé")
    chemin = DEPOT_COURSE / "scripts" / FICHIER_LANCEUR_BE3
    compagnon = Path(str(chemin) + ".sha256")
    if chemin.is_symlink() or not chemin.is_file():
        bloquer(f"{m} : {chemin} absent ou lien symbolique")
    lue = _sha256(chemin)
    if lue != EMPREINTE_LANCEUR_BE3:
        bloquer(f"{m} : empreinte du fichier {lue} ≠ empreinte épinglée dans le crochet {EMPREINTE_LANCEUR_BE3}")
    try:
        lignes = [x for x in compagnon.read_text(encoding="utf-8").splitlines() if x.strip()]
    except (OSError, UnicodeDecodeError) as e:
        bloquer(f"{m} : compagnon {compagnon.name} illisible ({type(e).__name__})")
    ligne = LIGNE_COMPAGNON.match(lignes[0]) if len(lignes) == 1 else None
    if ligne is None or ligne.group(2) != FICHIER_LANCEUR_BE3:
        bloquer(f"{m} : compagnon {compagnon.name} mal formé (une ligne « <empreinte>  {FICHIER_LANCEUR_BE3} » exigée)")
    if ligne.group(1) != lue:
        bloquer(f"{m} : empreinte du compagnon {ligne.group(1)} ≠ empreinte du fichier {lue}")


def decider(commande: str, aujourd_hui: date, cwd=None) -> None:
```

**H4 — appel dans decider**

Texte d'origine (une seule occurrence) :

```python
    garder_lanceur_be2(commande, cwd)
```

Texte neuf :

```python
    garder_lanceur_be2(commande, cwd)
    garder_lanceur_be3(commande, cwd)
```


### `.claude/settings.json` (empreinte avant : `701169aeed3b140121c46402dddb169890f2e2ab2fd04561450cbba80a02afb9`)

**S1 — règle d'autorisation : la seule commande du v3, génération 1**

Texte d'origine (une seule occurrence) :

```json
"Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py 1)"
```

Texte neuf :

```json
"Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py 1)"
```

**S2 — refus d'édition : v3, son compagnon et le crochet ajoutés ; ceux du v2 gardés**

Texte d'origine (une seule occurrence) :

```json
      "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v2.py.sha256)"
```

Texte neuf :

```json
      "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v2.py.sha256)",
      "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v3.py)",
      "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v3.py.sha256)",
      "Edit(//home/user/controle-ia-travail/.claude/hooks/garde_calcul.py)"
```


À savoir avant d'écrire : (a) après H1, le cas sain de `tests/test_garde_calcul_empreinte_lanceur_bassins_etroits_v2_v1.py`
échouera (c'est le but) ; il faut un fichier d'essais neuf pour l'épingle du v3 (cas sain ; argument 2 ; octet changé ;
compagnon faux ou absent ; deux arguments ; autre interpréteur ; autre dossier ; lien symbolique ; v2 désormais bloqué) et
retirer l'ancien de la suite sous un nom neuf (R12) ; (b) le dernier refus d'édition de S2 protège le crochet lui-même :
toute épingle suivante devra d'abord lever cette ligne ; (c) le crochet et `settings.json` n'ont pas de compagnon
d'empreinte (R6) ; (d) ces règles ne servent que dans une session qui les charge (point 8).

Épreuve P9 sur le crochet corrigé en mémoire : la commande exacte du v3, génération 1, depuis le dépôt, passe ; sont
bloqués l'argument 2 ou 3, l'absence d'argument, deux arguments, une espace finale, un autre interpréteur, l'absence de
`-I -B`, un `sha256sum` du lanceur, un `cd` devant, une commande ajoutée derrière, un autre dossier courant, un dossier
courant absent, une épingle différente du fichier, et toute commande citant le v2 ; les essais du lanceur ne sont pas pris
pour une citation ; la garde des arrêts par motif reste intacte.

## Comptes d'essais (heures par `date -u`, 13 novembre 2026)

| Quoi | Début | Fin | Compte |
|---|---|---|---|
| Essais du v3 (`tests/test_lancer_course_ideation_bassins_etroits_v3.py`, `6ab6ec5d…`), 1er passage | 18:01:01 | 18:01:59 | **135 passés, 4 échoués** |
| Les mêmes, 2e passage | 18:14:59 | 18:15:53 | **135 passés, 4 échoués** (les mêmes) |
| Banc de mutations du préparateur (`mutations_lanceur_v3.py`, `6d7d6c09…`), tel quel | 18:03:05 | 18:14:32 | base : 135 passés, 4 échoués ; **12 mutants tués au-delà de la base, 1 indécidable ici (W11)** |
| Mes épreuves (`eprouver_lanceur_v3_v1.py`) | 18:14:51 | 18:14:59 | 12 passées |
| Rejeu réduit de l'épreuve d'authentification | 18:07:24 | 18:09:08 | 3 cas, conformes au résultat scellé |
| Essais actuels du crochet (trois fichiers) | 18:09:18 | — | 92 passés |

Le rapport dit 139 passés et 13 mutations tuées sur 13. **Je ne retrouve ni l'un ni l'autre dans ce conteneur**, pour une
raison d'état de la machine et non de code : trois essais échouent parce que le clone de l'orchestrateur n'est pas au commit
épinglé (`test_b1_liste_blanche_et_mesure_contre_l_orchestrateur_reel`, `test_analyseur_reel_accepte_les_trois_commandes`,
`test_orchestrateur_sain_clone_reel`), un parce que le dossier hors dépôt du run du v2 est perdu
(`test_run_reel_du_v2_reconnu`, soit B1). Le banc du préparateur compte « tué » tout mutant dont un essai échoue : avec une
base en échec ce critère est vide, je n'ai donc compté que les essais échoués en plus de la base. Les douze mutants tués le
sont par les essais que nomme le rapport. Aucun essai n'a exigé `bubblewrap` ni `socat`.

## Ce que je n'ai pas vérifié

- Aucune course ni aucun bras réels ; l'orchestrateur réel n'a tourné dans aucun de mes essais (clone à un autre commit).
- Le vrai relais avec la vraie clé ; le kit dans le bac à sable réel de l'orchestrateur avec un HOME neuf (m6).
- Le devis v3 ; la conception ; les témoins ; le recoupement et son attestation.
- Le chargement du crochet dans une session ouverte sur le dépôt, et l'effet d'une règle écrite en cours de session.
- La survie du processus détaché entre deux tours de la session qui lancera.

## Outils (scellés, `docs/notes/organisme-bassins-etroits-v1/verification-outils-v3-v2/`)

| Fichier | Empreinte SHA-256 |
|---|---|
| `couples-epingle-lanceur-v3-v1.json` | `7b77e1feff83a37a9eb9478c5b78bae852df077bc08c03897e26eceb240f4ca8` |
| `eprouver_lanceur_v3_v1.py` | `ad945ab0fdf3ee5aa0196ac41b3a4df3566a45256700a22cf37a87470624c9b6` |
| `resultat-eprouver-lanceur-v3-v1.txt` | `badb74e77c0ed54d80fce68d8fd88367bdf4f736518e0e087a79811edb75e84c` |
| `rejouer_authentification_kit_reduit_v1.py` | `a7a6d72b61fee1c671e21c3d92c5c8c7d433d41f43b8f13af7ef7296faf3d215` |
| `resultat-rejouer-authentification-kit-reduit-v1.json` | `7455d838b771e438403d20a8c9b37065f71891334321059cff0eb899579c9e7f` |
| `resultat-rejeu-mutations-lanceur-v3-v1.json` | `6bb5c982afd1dd09992057e4ecd452c662e0d2dbfc9ba8f7b8f75dce94c768cd` |

Fichiers relus inchangés après mes outils : lanceur v2 `c6d82d8c…`, lanceur v3 `3fabd71e…`, essais du v3 `6ab6ec5d…`,
`.claude/hooks/garde_calcul.py` `73be0638…`, `.claude/settings.json` `701169ae…`. Restes : un cache d'octets du crochet
(`.claude/hooks/__pycache__/garde_calcul.cpython-313.pyc`), né d'un passage des essais du crochet, effacé par son chemin
exact ; mes dossiers de travail hors dépôt effacés ; `bubblewrap` reste installé. Une suite d'essais complète de la mère
tournait pendant mon travail ; je n'y ai pas touché.
