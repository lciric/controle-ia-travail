# Contre-lecture de conformité du code des lectures du dommage et de la diffusion sur la course version 5 (barreau 8, côté exposé)

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs ni à un concepteur de moniteur.

- **Verdict** : **`conforme sous corrections`** (aucun constat bloquant ; deux constats majeurs ; cinq constats mineurs).
- **Contre-lecteur** : contre-lecteur neuf de classe B, modèle Gemini 4 Neon (famille distincte du développeur Claude Opus 5.5).
- **Accord** : `GO-2026-11-24-37`.
- **Décision prise en compte** : `R-5383` (écart 3 du rapport du développeur tranché à l'option **(a)**, lettre de la spécification scellée : texte de citation nul dès que la part citée n'est pas calculable, quelle que soit la phrase).
- **Spécification scellée de référence** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md`, branche `barreau8/cote-expose-pieces-lecture-v1`, empreinte SHA-256 vérifiée `acce24e76e17bffb2938616f2204d068a1f61d5e71938ce8a33e1e6a83a7407e`.
- **Code contre-lu** : commit `c5d90370` de la branche `barreau8/code-lectures-v5-cote-expose-v1` (rapport du développeur `dcd7ca062f450381db70ccad373e83cf4f9d2901b23291b9a7f93b66e504cbb8` et les sept fichiers de code et d'essais).
- **Date** : 2026-11-24.

---

## 1. Synthèse du verdict

L'implémentation produite au commit `c5d90370` est d'excellente tenue générale et **conforme sur l'ensemble des exigences de fond** de la spécification scellée `acce24e7…` :

- **Calcul statistique inchangé** : les lectures appellent directement `lecture_v1.lecture_1` et `lecture_v1.lecture_2` sur les seules lignes de l'oracle désigné, présentées dans l'ordre canonique (conditions `H`, `B50`, `B100`, `TJ100`, tâches triées dans l'ordre des chaînes de Python, pas `0` à `9`), sans altérer ni les formules, ni les seuils, ni les clés attendues par le programme d'extrait des états.
- **Décision R-5383 (écart 3)** : le code **applique déjà l'option (a)** (`src/controle_ia/iib/lectures_v5.py`, lignes 166 à 168 : `texte` mis à `None` avec `motif` dès que `p_cite` vaut `None`, quelle que soit la phrase, y compris pour « dommage agrégé vu »). Aucune modification de logique métier n'est nécessaire pour `R-5383` (seul l'essai unitaire correspondant gagnerait à couvrir les quatre phrases, voir `CLN-06`).
- **Cloisonnement, intégrité et reproductibilité** : vérification par empreinte SHA-256 de la spécification scellée et des quinze modules d'origine, liste fermée à trois racines dans `ouvrir`, contrôle strict des fichiers JSON (clés répétées, constantes non finies et nombres débordants refusés), ordre d'exécution lecture du dommage → consignation et audit de symétrie éventuel → lecture de la diffusion, refus de seconde exécution avant création du manifeste, dérivation des graines par `numpy.random.SeedSequence` identique au bit près à `jumeau_v5.Graines` avec garde de collision, contrôle fermé des quatre fichiers du jetoniseur réel et garde de fidélité du décodage sur les neuf champs de l'action et sur `t06.cout.cout_action` avant toute création de manifeste.

Deux défauts majeurs reproductibles (`CLN-01` sur l'absence de bornes dans l'expression régulière des identifiants d'accord de l'audit, `CLN-02` sur le décodage du préfixe hors du bloc de gestion d'arrêt dans le script d'audit) et cinq défauts mineurs (`CLN-03` à `CLN-07`) justifient le verdict **`conforme sous corrections`**. Toutes les corrections sont ponctuelles, locales et sans effet sur les statistiques ni sur les sorties valides.

---

## 2. Vérification des empreintes SHA-256 des neuf pièces contre-lues

Les neuf pièces téléchargées directement depuis le dépôt GitHub (`lciric/controle-ia-travail`) et leurs neuf compagnons `.sha256` concordent tous à l'octet près :

| Pièce | Référence Git | Taille (octets) | Empreinte SHA-256 recalculée | Compagnon `.sha256` |
|---|---|---:|---|---|
| `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md` | `barreau8/cote-expose-pieces-lecture-v1` | 103 943 | `acce24e76e17bffb2938616f2204d068a1f61d5e71938ce8a33e1e6a83a7407e` | Concordant |
| `docs/notes/barreau8-cote-expose-pieces-lecture-v1/rapport-developpeur-code-lectures-v5-v1.md` | `c5d90370` | 15 759 | `dcd7ca062f450381db70ccad373e83cf4f9d2901b23291b9a7f93b66e504cbb8` | Concordant |
| `scripts/lecture_iib_1_dommage_v5.py` | `c5d90370` | 5 370 | `11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367` | Concordant |
| `scripts/lecture_iib_2_diffusion_v5.py` | `c5d90370` | 8 301 | `15ffa52fe475c8619c9c4a3439c2fbb7aed83f75e6fb546f68d9882acd324e1e` | Concordant |
| `scripts/lecture_iib_audit_r4_v5.py` | `c5d90370` | 5 966 | `92c5e0770e888245d6f76d542556d7adadb2329ff047dc10ce71fb147527a0f4` | Concordant |
| `src/controle_ia/iib/configuration_lectures_v5.py` | `c5d90370` | 15 882 | `3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f` | Concordant |
| `src/controle_ia/iib/entrees_lectures_v5.py` | `c5d90370` | 44 485 | `8e1846c3e76fe7e3eb7ad355c2eb05808f7605f2bf42dcc5e42aa99d603d4adf` | Concordant |
| `src/controle_ia/iib/lectures_v5.py` | `c5d90370` | 25 333 | `0f48f8ec5dbf5afd76d85b950eb6c7b10077544c688a3d8f77a98b5ce82659ca` | Concordant |
| `tests/test_lectures_iib_v5_v1.py` | `c5d90370` | 88 246 | `47c04f22516e7ae8a964a9b58641c154fbd4eb7a9f7ee660a0459eea643400bb` | Concordant |

De plus, l'exécution de `configuration_lectures_v5.exiger_specification()` et de `configuration_lectures_v5.exiger_modules_d_origine()` confirme l'égalité exacte de toutes les empreintes des quinze modules d'origine cités en section 19 de la spécification.

---

## 3. Constats de contre-lecture

### 3.1 Constats bloquants

Aucun constat bloquant.

### 3.2 Constats majeurs

#### `CLN-01` — Expression régulière d'identifiant d'accord sans bornes dans la garde de l'audit de symétrie (faux positif possible)

- **Gravité** : Majeur.
- **Fichier et lignes** : `src/controle_ia/iib/lectures_v5.py`, lignes 30 et 225 à 232.
- **Citation exacte** :
  ```python
  _ISSUE = re.compile(r"ISSUE=(SANS-DEFAUT|DEFAUT-AUTORISE|DEFAUT)(?![^\W\d_]|-)")
  _GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}")
  ...
        if issue == "DEFAUT-AUTORISE":
            gos = _GO.findall(l)
            if len(gos) != 1:
                raise GardeArret("lecture (2) refusée : ligne DEFAUT-AUTORISE sans un identifiant d'accord unique")
            accord = gos[0]
            if not ev.ouvrir("registres", cl.REGISTRE_ACCORDS, racines_registres, lecture="lignes_accord", cle=accord):
                raise GardeArret(...)
  ```
- **Analyse** : Contrairement à `_ISSUE` (qui comporte une négation de suivi sur lettre ou tiret), `_GO` ne comporte aucune borne à gauche ni à droite. Une ligne portant un identifiant mal formé tel que `GO-2026-11-24-370` (trois chiffres en fin, absent du registre des accords) ou `XGO-2026-11-24-37-bis` fait correspondre le sous-segment `GO-2026-11-24-37`. Si `GO-2026-11-24-37` figure dans `registres/go.md`, la garde valide à tort la ligne `ISSUE=DEFAUT-AUTORISE` et laisse partir la lecture de la diffusion. Ce défaut a été reproduit par notre script indépendant (`edge_CLN_go_regex_boundary`).
- **Correction attendue** : Borner l'expression régulière à gauche et à droite pour rejeter tout préfixe ou suffixe alphanumérique ou tiret :
  ```python
  _GO = re.compile(r"(?<![A-Za-z0-9-])GO-\d{4}-\d{2}-\d{2}-\d{2}(?![A-Za-z0-9-])")
  ```
  Ajouter dans `tests/test_lectures_iib_v5_v1.py` des cas d'artefact vérifiant le refus de `GO-2026-11-24-370` et `XGO-2026-11-24-37-bis`.

#### `CLN-02` — Décodage du préfixe jusqu'à la coupe exécuté hors du bloc `try … except GardeArret` après début d'affichage dans le script d'audit

- **Gravité** : Majeur.
- **Fichier et lignes** : `scripts/lecture_iib_audit_r4_v5.py`, lignes 67 à 79.
- **Citation exacte** :
  ```python
        decodes = ev.exiger_fidelite_du_decodage(jet, entrees)
    except GardeArret as e:
        print(f"ARRÊT (audit, rien d'écrit) : {e}", file=sys.stderr)
        return 1
    print(f"AUDIT R4 DE LA LECTURE (1) — course {a.run_id}, sortie sha256 {sha_1} ; EXPLORATOIRE, NON OPPOSABLE (R-522) ; "
          f"{len(retire)} actions ; rien n'est écrit sur disque")
    for k, x in enumerate(retire, start=1):
        c, t, pas = x["condition"], x["tache"], x["pas"]
        d = decodes[(c, t, pas)]
        lignes = {o: entrees["evaluation"][o][c][t][pas] for o in ("N", "P")}
        rang = lignes[entrees["oracle"]]["rang_coupe"]
        prefixe = ev.decoder(jet, d["ids"][:rang], f"evaluation-{c}/{t}#{pas}") if rang is not None else None
  ```
- **Analyse** : La garde 4 (`exiger_fidelite_du_decodage`) n'appelle `ev.decoder` que sur la liste entière `d["ids"]`, et non sur le préfixe tronqué `d["ids"][:rang]`. Or `ev.decoder` est rappelé à la ligne 78, **en dehors** du bloc `try ... except GardeArret` (clos ligne 68) et **après** le début de l'affichage sur la sortie standard (ligne 71). Si les deux décodages divergent sur le préfixe d'une action de l'échantillon (cas possible à la frontière de coupe `COST:`, reproduit par `edge_CLN_audit_r4_prefix_decode_outside_try`), `GardeArret` n'est pas interceptée : le programme échoue en trace d'exception Python brute après un affichage partiel, en écart avec la section 6.3 (« Gardes du script d'audit, dans cet ordre ; chacune refuse, code 1 »).
- **Correction attendue** : Précalculer les préfixes décodés des actions de l'échantillon **dans** le bloc `try` (juste après la ligne 67, avant toute impression sur la sortie standard), puis les afficher dans la boucle des lignes 73 à 89.

### 3.3 Constats mineurs

#### `CLN-03` — Date calendaire impossible au contrôle de l'ordre du temps (`T0`) levant `ValueError` au lieu de `GardeArret`

- **Gravité** : Mineur.
- **Fichier et lignes** : `src/controle_ia/iib/entrees_lectures_v5.py`, lignes 218 à 220.
- **Citation exacte** :
  ```python
            if not _HEURE.match(heure):
                raise GardeArret(f"{cle_t0} : heure illisible (AAAA-MM-JJTHH:MM:SSZ)")
            h = datetime.strptime(heure, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
  ```
- **Analyse** : Une chaîne satisfaisant l'expression régulière `_HEURE` mais représentant une date impossible (par exemple `2026-02-30T10:00:00Z`, reproduit par `edge_CLN_t0_invalid_calendar_date`) provoque une exception `ValueError` non convertie en `GardeArret`. Les scripts n'interceptant que `GardeArret` avant le manifeste, le programme termine sur une trace brute sans le motif exigé au contrôle `T0`.
- **Correction attendue** : Encadrer `datetime.strptime` d'un `try ... except ValueError` levant `GardeArret(f"{cle_t0} : heure illisible (AAAA-MM-JJTHH:MM:SSZ)") from None`.

#### `CLN-04` — En mode réel, `lecture_iib_2_diffusion_v5.py` et `lecture_iib_audit_r4_v5.py` ouvrent la sortie de lecture (1) sous `--racine` avant de vérifier l'égalité avec la racine du code

- **Gravité** : Mineur.
- **Fichiers et lignes** : `scripts/lecture_iib_2_diffusion_v5.py`, lignes 65 à 72 ; `scripts/lecture_iib_audit_r4_v5.py`, lignes 43 à 50.
- **Citation exacte** (`scripts/lecture_iib_audit_r4_v5.py`, lignes 43 à 50) :
  ```python
        R = ev.Racines(lecture=racine, run_id=a.run_id, etalonnage=a.etalonnage)
        rel_1 = f"diag/{a.run_id}/{cl.NOM_1}"
        sha_1 = ev.ouvrir("lecture", rel_1, R, lecture="scelle")
        l1 = ev.ouvrir("lecture", rel_1, R, lecture="json")
        if not (l1.get("audit_R4") or {}).get("declenche"):
            raise GardeArret("audit non déclenché : rien à relire")
        # (2)
        entrees = ev.charger(racine, a.run_id, a.etalonnage, avec_identifiants=True, mode=mode)
  ```
- **Analyse** : La garde de la section 2 (« En mode réel, la racine passée doit être la racine du code qui tourne (`bases_textuelles_v1.racine_du_code()`) ; sinon arrêt ») n'est appliquée qu'à l'entrée de `ev.charger` (`entrees_lectures_v5.py`, ligne 423). Les deux scripts ouvrent donc d'abord la sortie de lecture (1) dans un dossier `--racine` potentiellement étranger à l'arbre de code ; dans le script d'audit, si cette sortie étrangère porte `declenche == False`, le script s'arrête sur « audit non déclenché » sans avoir refusé la racine étrangère.
- **Correction attendue** : Contrôler `if mode == "reel" and racine != cl.racine_du_code().resolve(): raise GardeArret(...)` dès le début de `main()` dans les trois scripts.

#### `CLN-05` — Conversion booléenne implicite de `audit_R4.declenche` et champ `accord` nul en cas de `DEFAUT-AUTORISE` isolé

- **Gravité** : Mineur.
- **Fichier et lignes** : `src/controle_ia/iib/lectures_v5.py`, lignes 209 et 234 à 241.
- **Citation exacte** :
  ```python
    declenche = bool(l1["contenu"]["audit_R4"]["declenche"])
    ...
    defauts = [i for i, x in enumerate(issues) if x["issue"] == "DEFAUT"]
    autorise = None
    if defauts:
        apres = [x for x in issues[defauts[-1] + 1:] if x["issue"] == "DEFAUT-AUTORISE"]
        if not apres:
            raise GardeArret(...)
        autorise = apres[0]["accord"]
    return {"declenche": True, "issues": [x["issue"] for x in issues], "accords": [x["accord"] for x in issues], "accord": autorise}
  ```
- **Analyse** : Premièrement, `bool(...)` convertit silencieusement `None` en `False` (ce qui éviterait le contrôle de l'audit sur une sortie de lecture 1 mal formée) ou une chaîne non vide en `True`, contrairement au principe d'absence de repli silencieux (R5). Deuxièmement, si le registre porte une ligne `ISSUE=DEFAUT-AUTORISE GO-…` sans ligne `ISSUE=DEFAUT` antérieure, la garde passe mais consigne `"accord": None` alors qu'un identifiant d'accord est présent dans `"accords"` (confirmé par `edge_CLN_audit_bool_coercion_and_autorise_alone`).
- **Correction attendue** : Exiger `isinstance(declenche_brut, bool)` (sinon `GardeArret`), et soit renseigner `accord` avec l'identifiant d'accord lorsqu'une ligne `DEFAUT-AUTORISE` existe, soit refuser une ligne `DEFAUT-AUTORISE` sans défaut préalable.

#### `CLN-06` — Absence de garde sur signe ou finitude de l'effet minimal détectable dans `puissance`, et couverture partielle de la décision `R-5383` dans les essais unitaires

- **Gravité** : Mineur.
- **Fichiers et lignes** : `src/controle_ia/iib/lectures_v5.py`, lignes 99 à 107 ; `tests/test_lectures_iib_v5_v1.py`, lignes 957 à 958.
- **Citation exacte** (`src/controle_ia/iib/lectures_v5.py`, lignes 99 à 107) :
  ```python
    emd = gr.get("EMD")
    if emd is not None and (isinstance(emd, bool) or not isinstance(emd, (int, float))):
        raise GardeArret("puissance : effet minimal détectable illisible")
    honnete = gr.get("exces_moyen_honnete")
    tous, acc = x["exces_moyen_par_action_de_tous_les_episodes"], x["exces_moyen_par_action_des_acceptes"]
    moins = (tous - honnete) if (tous is not None and honnete is not None) else None

    def part(den):
        return None if (emd is None or emd == 0 or den is None or not den > 0) else float(emd) / float(den)
  ```
- **Analyse** : En lecture depuis le disque, `lire_json_strict` interdit déjà `NaN` et l'infini, mais en appel direct un `emd` non fini ou strictement négatif n'est pas refusé et produit une part `NaN` ou négative (reproduit par `edge_CLN_puissance_neg_or_nan_emd`), et `honnete` n'est pas contrôlé comme numérique non booléen. Par ailleurs, si le code de `citation_dommage` (lignes 166 à 168) respecte bien la décision `R-5383` (option **(a)**) sur les quatre phrases, l'essai `test_citation_artefacts` (ligne 957) ne vérifie `p_cite=None` que pour `"dommage non vu à cette puissance"`, et non pour `"dommage agrégé vu"`, `"dommage non distingué du témoin-jumeau"` et `"non calculable"`.
- **Correction attendue** : Ajouter `not math.isfinite(emd) or emd < 0` à la garde sur `emd` (et vérifier le type de `honnete` s'il n'est pas nul), et paramétrer l'essai `p_cite=None` sur les quatre phrases de la lecture du dommage.

#### `CLN-07` — Durcissements mineurs sur des entrées JSON mal typées (E8, E10 et précontrôle de `controle_premier_cout`)

- **Gravité** : Mineur.
- **Fichier et lignes** : `src/controle_ia/iib/entrees_lectures_v5.py`, lignes 380, 519 et 571.
- **Citations exactes** :
  - Ligne 380 (E8, lignes de `evaluation-iib-v5.json`) : `cle = (l["oracle"], l["phase"], l["episode"], l["pas"])` — contrairement à la ligne 351 (tranches par condition), `_entier(l["pas"])` n'est pas vérifié avant le hachage de `cle` ; un `pas` sous forme de liste lève `TypeError` non intercepté au lieu de `GardeArret` (reproduit par `edge_CLN_e8_unhashable_pas`).
  - Ligne 571 (E10, `_charger_identifiants`) : `if ens[k] != reunion[k]:` — en Python `1 == True == 1.0`, de sorte qu'un fichier d'ensemble contenant `True` ou `1.0` là où la tranche contient `1` passerait la comparaison alors que `exiger_identifiants` ne valide ensuite que `reunion`.
  - Ligne 519 (`charger`) : `"controle_premier_cout": evaluation.get("controle_premier_cout")` n'est pas validé avant la création du manifeste de la lecture (1) ; si cette clé est absente ou incomplète dans `evaluation-iib-v5.json`, la défaillance survient dans `lecture_1_v5` (ligne 199) **après** le manifeste (code 3, `arret.json`) au lieu d'un refus avant manifeste (code 1).
- **Correction attendue** : Ajouter `if not _entier(l["pas"]): raise GardeArret(...)` avant la ligne 380 ; vérifier les types exacts des éléments lors de la comparaison tranches/ensemble (ou passer `exiger_identifiants` sur `ens` également) ; valider la présence des quatre conditions et des clés `("phrase", "validite", "alerte")` dans `controle_premier_cout` dans `charger`.

---

## 4. Audit des écarts déclarés dans le rapport du développeur

Le rapport du développeur (`dcd7ca06…`, section 4) recense quatorze points (et non trois ; le troisième est l'objet de la décision `R-5383`). Tous ont été vérifiés dans le code :

| Numéro | Écart déclaré | Conformité et avis de contre-lecture |
|---:|---|---|
| 1 | Exception du seul fragment `sonde` sous la racine des registres pour `registres/sondes-iib-v1.md` et les trois textes cités en `T0` | **Justifié et minimal.** Résout une contradiction interne de la section 12 de la spécification ; `sonde` reste interdit sous la racine de lecture et sous le dossier du jetoniseur, et tous les autres fragments interdits restent refusés partout (vérifié sur `prereg/consigne-sondes.md`). |
| 2 | Détermination du mode avant `T0` : mode réel en ligne de commande, mode jouet uniquement via l'argument `essais` de `main(...)`, exigé égal au mode de la course | **Conforme et prudent.** Aucun drapeau de ligne de commande ne permet d'activer le mode jouet par erreur en exploitation réelle. |
| 3 | Citation de la lecture du dommage nulle quand `p_cite` n'est pas calculable, quelle que soit la phrase (`R-5383`) | **Conforme à la décision `R-5383` (option (a)).** Vérifié par lecture (`lectures_v5.py:166-168`) et par essai indépendant sur les huit couples `(oracle ∈ {N, P}) × (4 phrases)`. |
| 4 | Heures strictement croissantes au contrôle `T0` | **Conforme** (lecture stricte raisonnable de « croissantes dans cet ordre »). Voir toutefois `CLN-03` sur les dates calendaires impossibles. |
| 5 | Refus d'une ligne d'audit portant plusieurs `ISSUE=…` ou plusieurs `GO-…` | **Conforme et souhaitable.** Voir toutefois `CLN-01` sur les bornes de `_GO`. |
| 6 | Alias des graines restreint aux clés lues par chaque lecture (deux pour la lecture 1, quatre pour la lecture 2) | **Conforme** aux appels réels de `lecture_v1.lecture_1` et `lecture_v1.lecture_2` et à la table de la section 8. |
| 7 | Contrôle de la spécification et des modules d'origine en tête du script d'audit | **Durcissement pertinent**, sans effet de bord ni écriture sur disque. |
| 8 | Forme de `--etalonnage` contrôlée avant `E0` pour construire la liste fermée | **Nécessaire et conforme.** |
| 9 | Clé `entrees` limitée aux fichiers sous la racine de lecture (registres dans `ordre_du_temps`, jetoniseur dans `decodage`, code dans `lecture`) | **Cohérent** avec la structure des sections 6.2 et 7.5 ; toutes les empreintes sont tracées. |
| 10 | Refus avant manifeste si l'une des deux sorties de la lecture (2) ou son compagnon existe déjà (au lieu de « trois sorties ») | **Correction évidente** d'une coquille de la section 7.4 (la sortie de la lecture 1 devant précisément exister). |
| 11 | Durcissements : refus de `1e999` en JSON strict, égalité de types dans la fidélité, contrôle du modèle de l'agent et des versions chargée/installée, signature élargie de `ouvrir` | **Tous conformes et bénéfiques.** |
| 12 | Lectures effectuées par les modules d'origine hors de `ouvrir`, précédées d'une relecture JSON stricte et d'un passage par `ouvrir` | **Conforme** à la section 3 (« le code neuf relit donc en plus, de façon stricte, chaque fichier JSON qu'elles ouvrent, avant de les appeler »). |
| 13 | Arrêt après manifeste : toute exception écrit `arret.json` et rend le code 3 (et relève `KeyboardInterrupt` après écriture) | **Conforme** à la section 13. |
| 14 | Fichier d'essais nommé `tests/test_lectures_iib_v5_v1.py` au lieu de `tests/test_iib_lectures_v5.py` | **Justifié** par la règle de la section 14 (« aucun essai antérieur ne doit changer d'issue »), le motif `tests/test_iib_*_v5.py` étant contrôlé par un inventaire antérieur. |

---

## 5. Résultats des essais joués

### 5.1 Exécution de la suite du développeur (`tests/test_lectures_iib_v5_v1.py`, 153 essais)

1. **Exécution directe non modifiée** (`PYTHONDONTWRITEBYTECODE=1 python -m pytest -v tests/test_lectures_iib_v5_v1.py`) dans l'environnement local Windows Python 3.14.3 (`numpy 2.4.4`, `pytest 9.0.3`, branche locale `main` sans `src/controle_ia/iib/`) :
   - **Échec dès la collecte** (`0 collected / 1 error`) : `scipy` et `torch` ne sont pas installés dans cet interpréteur Windows (ni `transformers` ni `tokenizers`), `scipy.stats.rankdata` et `torch` étant importés transitivement par `controle_ia.iib.lecture_v1 -> t06.test_croise -> sondes.evaluation -> sondes.familles`.
2. **Exécution dans l'espace isolé avec les modules de code pur du commit `c5d90370` et un adaptateur en mémoire uniquement** (implémentation exacte en `numpy` de `scipy.stats.rankdata`, substitut vide `torch` jamais invoqué, et repli `os.link -> shutil.copy2` pour le bac à sable Windows, **sans aucune modification des fichiers contre-lus**) :
   - **Résultat exact** : **`83 passés, 12 sautés, 45 échecs, 13 erreurs`** (sur les 153 essais collectés, durée 429,6 s).
   - **Diagnostic exhaustif des écarts d'environnement Windows** :
     - **83/83 essais unitaires autonomes passés** (contrôle `T0`, `E6`, `E7`, `E8`, `E9`, spécification et quinze modules d'origine, configuration contre `configuration_v1`, graines `SeedSequence`, liste fermée, présentation, statistique de la lecture 1 sur lignes construites et quatre phrases, citations et puissance, garde d'audit, base « premier coût contre les suivants », mentions à côté).
     - **12 essais sautés** : gardes du jetoniseur réel (`dossier_jetoniseur`), sautés comme prévu en l'absence des objets Git du commit `e5677bbf` dans l'espace isolé.
     - **44 des 45 échecs et les 13 erreurs** : **tous** causés par la même raison propre à Windows dans le module antérieur gelé `src/controle_ia/iib/lanceur_v5.py` (ligne 469 : `str(chemin_d)` produit des séparateurs inversés `diag\20991231-000020-iib-jouet\designation-iib-v5.json` lors de la fabrication de la course jouet `monde` sous Windows, alors que `entrees_lectures_v5.py` ligne 479 attend le chemin POSIX `diag/.../designation-iib-v5.json`, ce qui déclenche légitimement la garde `E4`). Sur Linux (environnement de la course réelle et de la lecture), les chemins sont POSIX et ce phénomène n'existe pas.
     - **1 échec restant** (`test_fils_de_calcul`) : sous-processus Python nu ne disposant pas de `scipy`/`torch` ni du second chemin `PYTHONPATH`.
   - **Point non éprouvé localement** : la branche `lecture_2` appelant la pièce inscrite `scripts/mots_et_cout_t06_v3.py` (qui dépend de `scipy.optimize` et `scipy.special`) ainsi que le chargement réel par `transformers.AutoTokenizer` n'ont pas pu être exécutés faute de `scipy`, `transformers` et `tokenizers` sur cet environnement Windows ; ils ont été audités par lecture ligne à ligne contre `lecture_v1.py`, `bases_textuelles_v1.py` et `mots_et_cout_t06_v3.py`.

### 5.2 Suite indépendante de contre-lecture et cas limites (`verifier_contre_lecture.py`)

Quinze vérifications indépendantes dédiées ont été exécutées sur données factices et mutations ciblées :

| Vérification | Résultat | Observation |
|---|---|---|
| `spec_and_15_original_modules_sha256` | Passé | Spécification `acce24e7…`, quinze modules d'origine et six fichiers neufs vérifiés |
| `config_constants_and_pour` | Passé | Égalité exacte avec `configuration_v1` ; refus de toute option d'essai en mode réel et de `lecture_2_code` en mode jouet |
| `r5383_ecart_3_all_4_phrases_N_and_P` | Passé | Option **(a)** confirmée sur les 8 couples `(N, P) × (4 phrases)` : `texte is None` dès que `p_cite is None` |
| `edge_CLN_go_regex_boundary` | Reproduit (`CLN-01`) | `GO-2026-11-24-370` et `XGO-2026-11-24-37-bis` acceptés à tort comme `GO-2026-11-24-37` |
| `edge_CLN_t0_invalid_calendar_date` | Reproduit (`CLN-03`) | `2026-02-30T10:00:00Z` lève `ValueError` non intercepté |
| `edge_CLN_audit_r4_prefix_decode_outside_try` | Reproduit (`CLN-02`) | Ligne 78 hors `try/except GardeArret` et après impression de l'en-tête |
| `edge_CLN_puissance_neg_or_nan_emd` | Reproduit (`CLN-06`) | `EMD = -0.05` rend `p_cite = -0.2` ; `EMD = NaN` rend `p_cite = NaN` |
| `edge_CLN_audit_bool_coercion_and_autorise_alone` | Reproduit (`CLN-05`) | `declenche = None` converti en `False` ; `DEFAUT-AUTORISE` isolé rend `accord = None` |
| `edge_CLN_e8_unhashable_pas` | Reproduit (`CLN-07`) | `pas = [0]` dans `evaluation-iib-v5.json` lève `TypeError` non intercepté |
| `security_ouvrir_closed_list` | Passé | 10/10 vecteurs bloqués (antislash, `./`, `..`, majuscules `SONDE`/`Verdict`/`.PT`, fichiers exclus, `consigne` dans `cites`) |
| `math_premier_cout_and_base_and_acote` | Passé | Concordance exacte avec `rapportes_v5.discretion`, base sans clé `etat`, lecteur fenêtre commune suivi (non `ancien_lecteur`), aire sous la courbe `B100-H` = 0,900, seuils de `mention` exacts |
| `graines_seedsequence_bit_exact` | Passé | 15/15 flux `SeedSequence` identiques au bit près à `jumeau_v5.Graines` |
| `math_lecture_1_four_phrases` | Passé | Quatre phrases reproduites ; isolement strict vis-à-vis de l'oracle non désigné |
| `strict_json_all_artifacts` | Passé | 5/5 artefacts rejetés (clé répétée, `NaN`, `Infinity`, `-Infinity`, `1e999`) |
| `verbatim_constants_vs_sealed_spec` | Vérifié | 12/12 chaînes de la spécification exactes au caractère près (`FORME_2` est le symétrique exact de `FORME_1` visé par « mêmes champs qu'en 6.2 ») |

---

## 6. Qui a lu quoi (attestation stricte de cloisonnement)

Le contre-lecteur atteste un **cloisonnement absolu** pendant toute la contre-lecture :

- **Jamais ouverts, jamais consultés, jamais listés** :
  - aucune sortie réelle de la course (`diag/`, `runs/` de toute course réelle) ;
  - aucun épisode réel, aucun score, aucune activation, aucun adaptateur, aucun verdict, aucune lecture réelle ;
  - aucune branche `essai/iib-explo-*` ;
  - aucun fichier sous `donnees/`, `verdict/`, `docs/verdicts/`, `lecture/`, `coffre/`, `prereg/`, `registres/`, `consignes/` ;
  - aucune consigne privée.
- **Pièces du mandat récupérées depuis GitHub (`lciric/controle-ia-travail`) et lues intégralement** :
  1. `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md` (`barreau8/cote-expose-pieces-lecture-v1`, `acce24e7…`, et son `.sha256`) ;
  2. `docs/notes/barreau8-cote-expose-pieces-lecture-v1/rapport-developpeur-code-lectures-v5-v1.md` (`c5d90370`, `dcd7ca06…`, et son `.sha256`) ;
  3. `scripts/lecture_iib_1_dommage_v5.py` (`c5d90370`, `11b41164…`, et son `.sha256`) ;
  4. `scripts/lecture_iib_2_diffusion_v5.py` (`c5d90370`, `15ffa52f…`, et son `.sha256`) ;
  5. `scripts/lecture_iib_audit_r4_v5.py` (`c5d90370`, `92c5e077…`, et son `.sha256`) ;
  6. `src/controle_ia/iib/configuration_lectures_v5.py` (`c5d90370`, `3c823203…`, et son `.sha256`) ;
  7. `src/controle_ia/iib/entrees_lectures_v5.py` (`c5d90370`, `8e1846c3…`, et son `.sha256`) ;
  8. `src/controle_ia/iib/lectures_v5.py` (`c5d90370`, `0f48f8ec…`, et son `.sha256`) ;
  9. `tests/test_lectures_iib_v5_v1.py` (`c5d90370`, `47c04f22…`, et son `.sha256`).
- **Modules de code source pur du commit `c5d90370` récupérés dans l'espace de travail isolé du contre-lecteur uniquement pour exécuter `pytest` et vérifier les contrats d'appel** (les modules `src/controle_ia/iib/*.py` étant absents de la branche locale `main`) :
  - Lus en entier ou par passages pour vérification de contrat : `src/controle_ia/iib/lecture_v1.py` (`b8e904c0…`), `bases_textuelles_v1.py` (`e94064e3…`), `configuration_v1.py` (lignes 1 à 120, `d79f21b0…`), `configuration_v5.py` (`5e70ffec…`), `regle_v5.py` (`a81e88e5…`), `lecture_cout_v5.py` (`b753e8bb…`), `designation_v5.py` (`558c0402…`), `branches_v5.py` (`ed25ec41…`), `rapportes_v5.py` (`4015e193…`), `oracle_v5.py` (`d997c593…`), `controle_premier_cout_v5.py` (`71865c6e…`), `tours_v1.py` (`df6267f4…`), `lanceur_v5.py` (lignes 520 à 620, `3eb03c3b…`), `manifeste.py` (`1a5c7464…`), `scellement.py` (`93beeb1c…`), `t06/test_croise.py` (lignes 1 à 100, `0a627df9…`), `scripts/mots_et_cout_t06_v3.py` (lignes 1 à 80, `9dbcc55c…`).
  - Présents dans l'espace isolé uniquement pour résolution d'import Python et exécution de la course jouet de `pytest` (non ouverts) : les autres fichiers `.py` de `src/controle_ia/iib/` au commit `c5d90370`, `gardes.py`, `harnais/formats.py`, `harnais/run_harnais_factice.py`, `t06/cout.py`, `tests/iib_distillation_v5_outils.py`, `tests/iib_v5_outils.py`, `tests/test_iib_lanceur_v5.py`, ainsi que `src/controle_ia/environnements/`, `harnais/`, `t06/` et `sondes/` locaux (branche `main`, code source pur).
- **Toutes les données manipulées durant les essais** ont été exclusivement des données factices synthétiques créées en mémoire ou dans des dossiers temporaires.
