# Vérification adverse de l'addendum 7 du témoin de Bailey — v7 (lecture confiée au code scellé)

Workflow `verification-lecture-scellee-addendum-7-bailey`, run `wf_546ead87-990`, trois relecteurs neufs, sur
`prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md`, `src/controle_ia/temoin_bailey/lecture_scellee_v1.py`
et `tests/test_temoin_bailey_lecture_scellee_v1.py` au commit `f8263a75`. Retours consignés tels quels depuis le journal du run.

## Angle « code » — bloquant : oui

J'ai lu en entier lecture_scellee_v1.py (sha 1b6f365e…, identique entre a91ba8cf et f8263a75) et ses essais. Avec PYTHONPATH=src:tests et le .venv, les 15 essais passent. Mes essais adverses sont dans /tmp/claude-0/r2ls/essai1.py à essai5.py, tous sur des dossiers factices construits par poste_local.

Ce qui tient :
- La sortie est identique à valider+lire joués directement. J'ai comparé tout le contenu de « lecture » après aller-retour JSON, pas seulement le verdict : égal.
- La sortie est déterministe : même condensat sous PYTHONHASHSEED 0, 1, 7 et 123 et sous OMP_NUM_THREADS 1 à 3.
- L'empreinte d'environnement est stable d'un appel à l'autre, avec ou sans tests dans PYTHONPATH, et même sous python -I.
- La sortie de lire ne contient aucun type non sérialisable ni aucune clé autre qu'une chaîne. La graine (SeedSequence) n'y figure pas.
- Aucune valeur ne sort sur la sortie standard : il n'y a aucun print dans lecture_v8, analyse_v3, conventions_v3 ou journaliseur_v3, et le message d'une exception autre qu'une GardeArret n'est jamais écrit.
- L'ouverture en mode « x » interdit tout écrasement.

Deux défauts du code rendent le scellement impossible en l'état. Chacun permet d'obtenir une sortie scellée d'un dossier ou d'un code modifié, avec des empreintes qui restent égales à l'attendu :
1. L'empreinte du dossier ignore les dossiers, vides compris, et le contenu des dossiers atteints par lien symbolique. Or valider décide sur la seule existence de dossiers. Démonstration : retirer un dossier vide `pilote-reprise` fait passer « Pas de run principal, pas de verdict » à « Effet reproduit… » sans changer l'empreinte. Ajouter un dossier vide `principal-relance` fait passer « aboutie » à « refus ou erreur ».
2. empreinte_code ne refuse pas un src/ modifié, contrairement à sa docstring et à la règle 2. Elle rend la chaîne « src/ modifié hors commit », qui sert alors de valeur comparable : deux codes modifiés différents obtiennent la même empreinte.

S'y ajoute une lacune de l'addendum : rien ne vérifie que l'empreinte « code » de l'attendu est celle du commit nommé, ni que --calculer-attendu est joué dans l'arbre de travail et avec l'interpréteur de la lecture.

Toute correction du code change l'empreinte et le commit cités au § 4, l. 266-272, ainsi que le décompte des essais : ces lignes sont à mettre à jour, et le code doit être re-contre-lu (R2) avant le scellement.

### 1. bloquant — src/controle_ia/temoin_bailey/lecture_scellee_v1.py l. 56-62 (empreinte_dossier) ; docstring l. 10-11

**Constat.** Seuls les fichiers entrent dans l'empreinte. Les dossiers vides n'y entrent pas, et rglob (Python 3.11) ne descend pas dans un dossier atteint par lien symbolique, alors que valider le suit (is_dir, is_file). Or valider décide sur la seule existence de dossiers : `(racine/'principal-relance').is_dir()` et les pilotes `(racine/e).is_dir()`. Essai (/tmp/claude-0/r2ls/essai5.py) : avec un dossier vide `pilote-reprise`, le verdict est « Pas de run principal, pas de verdict (exécution du pilote sans journaux…) » ; une fois ce dossier retiré, il devient « Effet reproduit sur le banc des auteurs… », avec la même empreinte du dossier. Inversement (essai4.py), un dossier vide `principal-relance` ajouté après l'attendu donne l'issue « refus ou erreur » et non « refus : empreintes ». Le contenu d'un dossier atteint par lien change de même sans changer l'empreinte (essai3.py). On obtient donc une sortie « aboutie » scellée d'un dossier modifié après la clôture.

**Correction proposée.** Remplacer la fonction par :

def empreinte_dossier(d: Path) -> str:
    """Empreinte de la liste triée de toutes les entrées de `d` : dossiers (vides compris) par leur chemin relatif,
    fichiers par (chemin relatif, sha256 des octets) ; lien symbolique ou entrée d'un autre type : refus. Ne décode rien."""
    d = Path(d)
    if not d.is_dir():
        raise GardeArret(f"lecture scellée : dossier absent ({d})")
    lignes = []
    for p in sorted(d.rglob("*")):
        rel = p.relative_to(d).as_posix()
        if p.is_symlink():
            raise GardeArret(f"lecture scellée : lien symbolique dans le dossier ({rel})")
        if p.is_dir():
            lignes.append(["d", rel])
        elif p.is_file():
            lignes.append(["f", rel, _sha(p.read_bytes())])
        else:
            raise GardeArret(f"lecture scellée : entrée d'un type inattendu ({rel})")
    return _sha(json.dumps(lignes, ensure_ascii=False).encode())

La sérialisation JSON supprime au passage l'ambiguïté d'un nom contenant une tabulation ou un saut de ligne. Docstring, règle 2 : remplacer « liste des empreintes des fichiers du dossier » par « liste des entrées du dossier (dossiers, vides compris ; fichiers avec l'empreinte de leurs octets ; un lien symbolique ou une autre entrée : refus) ». Essais à ajouter : dans test_empreinte_dossier_octets_et_ordre, `(b / 'vide').mkdir()` change l'empreinte, et un `os.symlink` dans le dossier lève GardeArret ; un essai poste_local + `(racine/'pilote-reprise').mkdir()` après l'attendu doit donner l'issue « refus : empreintes ».

### 2. bloquant — src/controle_ia/temoin_bailey/lecture_scellee_v1.py l. 65-72 (empreinte_code) ; tests l. 159-170

**Constat.** La docstring et la règle 2 disent « refus si src/ porte une modification non commitée ». Le code, lui, rend la chaîne « src/ modifié hors commit », que jouer compare à l'attendu comme n'importe quelle empreinte. Essai (essai4.py) : deux modifications différentes de src/ rendent la même valeur. Si --calculer-attendu est joué sur un arbre sale, l'attendu porte cette chaîne, et toute lecture jouée ensuite sur un arbre sale, quel que soit le code modifié, passe le contrôle et rend une sortie « aboutie » scellée. L'essai l. 159-170 consacre ce comportement au lieu de le refuser.

**Correction proposée.** Remplacer le corps par :

    statut = subprocess.run(["git", "-C", str(depot), "status", "--porcelain", "--untracked-files=all", "--", "src"],
                            capture_output=True, text=True, check=True).stdout
    if statut.strip():
        raise GardeArret("lecture scellée : src/ modifié hors commit")
    return subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD:src"], capture_output=True, text=True,
                          check=True).stdout.strip()

L'exception passe par la branche « empreintes incalculables » de jouer (issue « refus : empreintes »), et --calculer-attendu échoue sans rien imprimer. Dans l'essai, remplacer les deux `assert ls.empreinte_code(depot) == "src/ modifié hors commit"` par `with pytest.raises(GardeArret): ls.empreinte_code(depot)`. Dans jouer, refuser en plus un attendu dont `code` n'est pas une chaîne de 40 chiffres hexadécimaux : `if not re.fullmatch(r"[0-9a-f]{40}", str(attendu.get("code", "")))` donne l'issue ISSUE_EMPREINTES sans exécution.

### 3. à corriger — addendum 7, l. 159-162 (note de clôture) et l. 202-204 (contrôle par programme)

**Constat.** Rien ne relie l'empreinte « code » de l'attendu au commit nommé, et rien n'impose de jouer --calculer-attendu dans l'arbre de travail neuf avec l'interpréteur de la lecture. Deux suites sont possibles. Un attendu calculé dans la copie principale, sur un autre commit ou un autre src/, mène à « refus : empreintes » dans l'arbre neuf, donc à « pas de verdict » sans recours, et l'essai sur le dossier factice ne le révèle pas puisqu'il a son propre attendu. À l'inverse, une lecture jouée hors de l'arbre nommé mais conforme à cet attendu aboutit sur un code qui n'est pas celui du commit nommé. Enfin, la règle « elle ne change plus avant la clôture » (l. 272) n'a aucun contrôle mécanique pour lecture_v8, analyse_v3 et les modules qu'ils appellent.

**Correction proposée.** L. 159-160 : remplacer « dans un fichier écrit par `lecture_scellee_v1 --calculer-attendu`, qui ne fait que des empreintes d'octets et ne lit aucune note » par « dans un fichier écrit par `lecture_scellee_v1 --calculer-attendu`, joué dans l'arbre de travail neuf au commit nommé, avec l'interpréteur et les variables de la commande, qui ne fait que des empreintes d'octets et ne lit aucune note ; la note vérifie par programme, et cite, que le champ `code` de ce fichier est `git rev-parse <commit nommé>:src` et que `git diff --quiet a91ba8cf <commit nommé> -- src/controle_ia/temoin_bailey/lecture_scellee_v1.py src/controle_ia/temoin_bailey/lecture_v8.py src/controle_ia/temoin_bailey/analyse_v3.py src/controle_ia/temoin_bailey/conventions_v3.py src/controle_ia/temoin_bailey/journaliseur_v3.py src/controle_ia/gardes.py src/controle_ia/scellement.py` réussit (commit à remplacer par celui du code corrigé) ». L. 203 : remplacer « son champ `attendu` au fichier que nomme la note de clôture et son empreinte à celle qu'a rendue le lecteur » par « son champ `attendu` au fichier que nomme la note de clôture, le champ `code` de ce fichier à `git rev-parse <commit nommé>:src`, et son empreinte à celle qu'a rendue le lecteur ».

### 4. remarque — src/controle_ia/temoin_bailey/lecture_scellee_v1.py l. 75-77 (empreinte_environnement)

**Constat.** L'empreinte est stable : même valeur entre appels et entre processus, avec ou sans tests dans PYTHONPATH, et sous -I. Mais elle ne couvre que les noms et versions des distributions. Un fichier de numpy modifié dans site-packages, un module placé devant site-packages par PYTHONPATH, ou un .pyc forgé sous src/__pycache__ (fichiers ignorés, invisibles à git status) passeraient. Il faudrait pour cela une falsification délibérée, ce qui n'est pas une voie accidentelle. Par ailleurs, le .venv du dépôt est partagé : un pip install fait par une autre session entre la clôture et la lecture ferait tomber la lecture en « refus : empreintes », donc en « pas de verdict ».

**Correction proposée.** Ajouter à l'empreinte `sys.executable`, `sys.prefix` et `[str(Path(p).resolve()) for p in sys.path]` (ce sont des valeurs stables ; ne pas hacher sys.modules, qui grandit entre la première et la seconde exécution). Jouer la commande avec `python -B`, pour qu'aucun .pyc ne soit écrit ni relu. Dans l'addendum, l. 162, après « avec l'interpréteur du dépôt », ajouter « ; aucune session n'installe ni ne retire de distribution dans cet environnement entre la note de clôture et la dernière sortie scellée ».

### 5. remarque — src/controle_ia/temoin_bailey/lecture_scellee_v1.py l. 163-166 ; addendum l. 206-210

**Constat.** Si le processus meurt entre l'écriture (« x ») et sceller, une sortie complète ou partielle reste sans compagnon. Le remplaçant joue alors la commande, qui refuse (code 3). La règle aboutit bien à « pas de verdict », mais elle n'interdit pas de sceller après coup ce fichier non scellé, ni de l'ouvrir.

**Correction proposée.** Addendum, l. 208 : après « si la sortie scellée existe déjà », insérer « (une sortie présente sans son compagnon `.sha256` n'est pas une sortie scellée : elle n'est ni ouverte ni scellée après coup, et le remplaçant la traite comme absente ; le code refusant alors la commande, l'absence est constatée) ».

### 6. remarque — tests/test_temoin_bailey_lecture_scellee_v1.py l. 187-188

**Constat.** Le bout en bout ne compare que le verdict. J'ai vérifié que toute la lecture est égale à valider+lire joués directement (essai1.py) ; l'essai pourrait l'exiger, à l'appui de la phrase du § 4 « la sortie porte le verdict même que valider et lire joués directement ».

**Correction proposée.** Remplacer les l. 187-188 par :
    direct = json.loads(json.dumps(ls.une_execution(racine), default=ls._en_json))
    assert d["lecture"] == direct and code == 0

## Angle « critère central » — bloquant : oui

Le § 3 réécrit confie bien la lecture à un code scellé. La règle mécanique tient dans les cas déroulés : 72 tours finis, run tronqué, refus à 36 tours, refus à la confirmation, refus aux deux, erreur passagère, lecteur muet puis remplaçant, rapport contraire à la sortie, commande factice en échec. Mais deux défauts du code `lecture_scellee_v1` cassent la liaison sur laquelle repose tout le traitement du bloquant v6. Je les ai démontrés sur des dossiers factices, dans une copie du dépôt sous le répertoire de travail temporaire.

(1) `empreinte_code` ne refuse pas un `src/` modifié : elle rend la valeur fixe « src/ modifié hors commit ». Si l'attendu a été calculé dans un arbre sale, cette valeur est égale à elle-même. J'ai alors pu modifier `lecture_v8`, et la sortie « aboutie » a porté le verdict « VERDICT MODIFIE ».

(2) `empreinte_dossier` ignore les répertoires. Pourtant `valider` change de branche selon leur seule existence. Un `pilote-reprise/` vide fait passer le verdict de « Effet reproduit » à « Pas de run principal, pas de verdict », avec une empreinte inchangée. Le texte ne dit pas non plus si le dossier lu est celui de l'arbre principal ou sa copie dans l'arbre de lecture, où git perd les répertoires vides.

À corriger :
- qui crée l'arbre de lecture, quand, à quel chemin ; où se calcule l'attendu ; l'essai factice n'éprouve ni le code ni l'environnement réels ; le commit reste au choix de la session ;
- la source de K′ pour la confirmation (bilan ou lecture), qui reste au choix de la session une fois les verdicts ouverts, au seuil de 71 ;
- le contrôle par programme ne dit ni qui le joue ni à quoi il se compare quand aucun lecteur n'a rendu d'empreinte ;
- le rejeu « à l'identique » de l'assemblage échoue toujours après une erreur en cours de copie (cible déjà présente).

Cloisons tenues : aucun fichier sous runs/ ouvert ; seul un comptage de noms par `git ls-files | wc -l` a été fait. valider et lire n'ont été joués que sur des dossiers factices du répertoire de travail temporaire. Rien n'a été modifié dans le dépôt, aucun réseau. Les 15 essais passent dans une copie du dépôt sous le répertoire de travail temporaire.

### 1. bloquant — code : src/controle_ia/temoin_bailey/lecture_scellee_v1.py l. 65-72 (empreinte_code) ; addendum § 3 l. 159-160 et 169-170, § 4 l. 266-274

**Constat.** Quand `git status --porcelain -- src` n'est pas vide, `empreinte_code` ne refuse pas : elle rend la chaîne « src/ modifié hors commit ». Si `--calculer-attendu` est joué dans un arbre où `src/` porte un fichier non suivi ou modifié (un `__pycache__` hors .gitignore, un brouillon), l'attendu porte cette chaîne. Toute lecture faite ensuite avec un `src/` modifié, quel qu'il soit, rend alors la même chaîne et passe la vérification. Le contrôle par programme de la session compare l'attendu de la sortie au fichier de la note ; les deux portent la même chaîne, donc il passe aussi. Démontré dans une copie du dépôt sous le répertoire de travail temporaire : attendu calculé avec un `src/brouillon.py` non suivi, `lecture_v8` modifié pour rendre un verdict constant, puis commande jouée. Issue « aboutie », verdict « VERDICT MODIFIE ». C'est exactement la voie du bloquant v6 (code modifié, puis lecture), rouverte par une garde que sa propre valeur d'échec satisfait. Aucun essai ne couvre cet artefact (R5). Dans l'autre sens, un attendu sale et une lecture dans un arbre propre donnent « refus : empreintes » pour les deux runs. La règle mécanique en fait « pas de verdict » pour toute l'étape 1, et l'essai factice ne le détecte pas.

**Correction proposée.** Code (version neuve `lecture_scellee_v2.py`, R12) : remplacer
    if statut.strip():
        return "src/ modifié hors commit"
par
    if statut.strip():
        raise GardeArret("lecture scellée : src/ modifié hors commit")
Dans `jouer`, l'exception est déjà prise comme « refus : empreintes ». Avec `--calculer-attendu`, le script sort alors en erreur. Faire écrire l'attendu par le script lui-même (option `--vers F`, ouverture en mode « x »), seulement en cas de succès, et non par une redirection du shell, qui laisserait un fichier vide. Ajouter deux essais d'artefact : `--calculer-attendu` sur un `src/` sale échoue sans rien écrire ; une lecture sur un `src/` sale donne « refus : empreintes ». Mettre à jour au § 4 le nom, l'empreinte, le commit et le nombre d'essais.
Texte, l. 159-160 : remplacer « les empreintes attendues (code, dossier, environnement), dans un fichier écrit par `lecture_scellee_v1 --calculer-attendu`, » par « les empreintes attendues (code, dossier, environnement), dans un fichier écrit par `lecture_scellee_v2 --calculer-attendu`, dont le champ `code` est vérifié par programme, avant la note, égal à `git rev-parse <commit nommé>:src`, ».

### 2. bloquant — code : lecture_scellee_v1.py l. 56-62 (empreinte_dossier) ; addendum § 3 l. 156-162

**Constat.** L'empreinte du dossier ne porte que les fichiers. `valider` décide pourtant sur l'existence de répertoires : `pilote-reprise`, `principal-relance` et `transfert-N` (lecture_v8 l. 473, 519, 545 et 369). Démontré sur un dossier factice (`poste_local`) : ajouter un répertoire vide `pilote-reprise/` laisse l'empreinte égale et fait passer le verdict de « Effet reproduit … (K = 21) » à « Pas de run principal, pas de verdict (exécution du pilote sans journaux transférés) ». Deux voies en découlent.
(a) Le texte ne dit pas si le dossier lu est celui de l'arbre principal ou sa copie dans l'« arbre de travail neuf au commit nommé ». Lue dans cet arbre, avec un chemin relatif `runs/…`, la copie git a perdu les répertoires vides de la sortie de la conduite. Un répertoire d'étape lancée sans transfert disparaît ainsi, par exemple un `principal-relance/` vide : `valider` lit alors la première exécution au lieu de lever la garde, ce qui fausse la lecture alors que l'attendu, calculé sur la même copie, passe.
(b) Il suffit de créer ou d'ôter un répertoire vide, puis d'effacer la sortie et de la rejouer : le verdict change sans écart d'empreinte.

**Correction proposée.** Code (`lecture_scellee_v2`) : remplacer le corps de `empreinte_dossier` après le contrôle d'existence par
    lignes = []
    for p in sorted(d.rglob("*")):
        r = p.relative_to(d).as_posix()
        if p.is_symlink():
            raise GardeArret(f"lecture scellée : lien symbolique dans le dossier ({r})")
        if p.is_dir():
            lignes.append(f"D\t{r}")
        elif p.is_file():
            lignes.append(f"F\t{r}\t{_sha(p.read_bytes())}")
        else:
            raise GardeArret(f"lecture scellée : entrée ni fichier ni répertoire ({r})")
    return _sha("\n".join(lignes).encode())
Ajouter un essai d'artefact : un répertoire vide ajouté change l'empreinte.
Texte, l. 156-158 : remplacer « le dossier donné à la lecture (pour la confirmation : la sortie de la conduite ; » par « le dossier donné à la lecture, par son chemin absolu dans l'arbre de travail principal du dépôt, jamais par sa copie dans un autre arbre de travail (git n'y garde pas les répertoires vides) ; entre la note de clôture et le scellement des deux sorties, aucun changement de branche, `git checkout`, `git clean` ni `git stash` n'est fait dans cet arbre (pour la confirmation : la sortie de la conduite ; ».

### 3. à corriger — § 3 l. 159-164 (note de clôture, arbre de travail, essai factice) ; § 4 l. 266-267

**Constat.** Le texte ne dit ni qui crée l'arbre de travail neuf, ni quand, ni à quel chemin. Il ne dit pas non plus où se calcule l'attendu, et « le commit du code » est laissé au choix de la session.
(a) Si la commande consignée contient `git worktree add` à un chemin fixe, l'essai factice (« telle quelle », hors chemins du dossier, de l'attendu et de la sortie) crée cet arbre. La vraie commande échoue alors (chemin déjà présent), et la commande rejouée par le remplaçant échoue de même. Les deux finissent sans sortie, donc « pas de verdict », par simple collision de chemins.
(b) L'attendu de l'essai est recalculé sur le dossier factice. L'essai n'éprouve donc ni les champs `code` et `environnement` de l'attendu réel, ni l'arbre où celui-ci a été calculé. Un attendu réel calculé ailleurs (arbre principal, autre interpréteur) passe l'essai puis donne « refus : empreintes » sur les deux runs.
(c) Rien ne lie le commit nommé à `lecture_scellee_v1` (1b6f365e…) ni à `lecture_v8` et `analyse_v3` inchangés : un commit postérieur où ils ont changé serait accepté par l'attendu.

**Correction proposée.** l. 159-164 : remplacer « le commit du code ; les empreintes attendues (code, dossier, environnement), dans un fichier écrit par `lecture_scellee_v1 --calculer-attendu`, qui ne fait que des empreintes d'octets et ne lit aucune note ; le chemin de la sortie ; la commande. Ils ne changent plus. La commande est celle du § 4 (`lecture_scellee_v1`), jouée dans un arbre de travail neuf au commit nommé (`git worktree add`), avec l'interpréteur du dépôt. Avant la note de clôture, elle est jouée telle quelle, aux seuls chemins du dossier, de l'attendu et de la sortie près, sur un dossier factice de même forme, » par « le commit du code, celui que nomme le § 4 et aucun autre ; l'arbre de travail de lecture, créé par la session avant la note par `git worktree add <chemin absolu> <ce commit>`, un seul pour les deux verdicts, où rien n'est écrit ensuite hors les sorties ; les empreintes attendues (code, dossier, environnement), dans un fichier écrit par `--calculer-attendu`, joué par la session dans cet arbre, avec l'interpréteur et les variables de la commande, sur le chemin absolu du dossier, qui ne fait que des empreintes d'octets et ne lit aucune note ; le chemin de la sortie ; la commande, qui ne crée aucun arbre. Ils ne changent plus. La commande est celle du § 4, jouée dans cet arbre de travail, avec l'interpréteur du dépôt, tous chemins absolus. Avant la note de clôture, elle est jouée telle quelle, aux seuls chemins du dossier, de l'attendu et de la sortie près, sur un dossier factice de même forme ; l'attendu de l'essai est l'attendu réel dont seul le champ `dossier` est remplacé par l'empreinte du dossier factice, de sorte que le code, l'arbre et l'environnement réels sont éprouvés, ».

### 4. à corriger — § 3 l. 213-214 (K′ de la confirmation), avec l. 233-236 (verdict retenu)

**Constat.** Pour le run à 36 tours, K′ est « établi par la lecture ». Pour la confirmation, K′ est « le nombre de tours complets de l'exécution qui porte son verdict », sans source : le bilan de la conduite, connu avant la clôture, ou le `k_prime` de la sortie. Or `valider` peut compter un tour de moins que le bilan, par exemple quand la dernière ligne d'un journal est coupée, puisque les lignes coupées sont écartées. Le choix entre « K′ ≥ 71 : confirmation retenue » et « K′ ≤ 70 : verdict à 36 tours » se ferait alors après l'ouverture des deux verdicts, selon la source que la session prend. C'est une décision qui change le verdict retenu et dépend d'un résultat lu (à la frontière 70/71 seulement).

**Correction proposée.** l. 213-214 : remplacer « K′ de la confirmation : nombre de tours complets de l'exécution qui porte son verdict (sa relance, s'il y en a une, l. 371). » par « K′ de chaque run : le champ `k_prime` de sa sortie scellée « aboutie », établi par la lecture, pour la confirmation comme pour le run à 36 tours (exécution qui porte le verdict, sa relance s'il y en a une, l. 371), jamais le compte du bilan ni d'un autre fichier ; le compte du bilan est rapporté à côté, sans effet sur le verdict retenu. »

### 5. à corriger — § 3 l. 202-204 (contrôle par programme), avec l. 210-212 (sortie qui fait foi seule)

**Constat.** (a) La phrase ne dit pas qui joue le contrôle.
(b) Dans le cas où « la sortie scellée fait foi seule » (le remplaçant a échoué), aucun lecteur n'a rendu d'empreinte. Le cas d'un lecteur qui a scellé sa sortie et son rapport sans rien rendre n'est pas couvert non plus. « Son empreinte à celle qu'a rendue le lecteur » est alors inapplicable : l'absence d'empreinte rendue vaut-elle un écart, donc « pas de verdict » ? Cette question se tranche au moment où tout s'ouvre.
(c) Le scellement de la sortie n'est pas vérifié, ni son champ `dossier`.
(d) La comparaison à l'empreinte rendue ne détecte pas une sortie effacée puis refaite par le lecteur, qui rend alors l'empreinte de la nouvelle. Une fois les deux bloquants corrigés, cette voie n'est plus ouverte qu'à une fraude délibérée par l'environnement non empreinté (variables, fichiers des distributions installées), mais le texte prête au contrôle une portée qu'il n'a pas.

**Correction proposée.** l. 202-204 : remplacer « Ensuite, et avant d'ouvrir le reste, un contrôle par programme compare, pour chaque sortie, son champ `attendu` au fichier que nomme la note de clôture et son empreinte à celle qu'a rendue le lecteur : un écart vaut « pas de verdict » pour ce run. » par « Ensuite, et avant d'ouvrir le reste, la session joue un contrôle par programme qui, pour chaque sortie, vérifie son scellement (`scellement.verifier`), compare son champ `attendu` au fichier que nomme la note de clôture, son champ `dossier` au chemin nommé, et son empreinte à celle qu'a rendue le lecteur qui fait foi, s'il en a rendu une : un écart, ou un scellement qui ne tient pas, vaut « pas de verdict » pour ce run ; l'absence d'empreinte rendue n'est pas un écart. » Variante plus forte, à préférer si l'on veut que la sortie soit ancrée avant que quiconque la lise : la session joue elle-même la commande juste après la note de clôture. Le code ne rend que l'empreinte et l'issue, sans aucune valeur. Elle consigne les deux, puis lance les lecteurs sur la sortie scellée. La puce « Lecteur remplacé » perd alors la branche « sinon il joue la commande ».

### 6. à corriger — § 3 l. 221-224 (rejeu de l'assemblage d'une relance)

**Constat.** Le rejeu « à l'identique, sans rien modifier entre les deux exécutions » est inapplicable pour le cas qu'il vise. `lanceur_v21.assembler_lecture` crée la cible (`cible.mkdir`) avant de copier, et refuse toute cible déjà présente (« assemblage : dossier cible déjà présent (R12) »). Une erreur d'exécution pendant la copie (disque plein, coupure) laisse une cible partielle. La seconde exécution à l'identique tombe alors toujours sur ce refus, et effacer la cible partielle serait « modifier entre les deux exécutions ». La session doit donc choisir entre trois issues : constater « pas de verdict », effacer la cible, ou changer son nom. Ce choix fixe si la relance a un verdict, et il n'est pas mécanique.

**Correction proposée.** l. 223-224 : remplacer « est rejoué une seconde fois à l'identique par la session, sans rien modifier entre les deux exécutions ; » par « est rejoué une seconde fois par la session, mêmes sources et même code, vers une cible neuve au nom suivant (R12 ; le code refuse une cible déjà présente), la cible partielle de la première exécution étant laissée en place sans être lue ni effacée, sans rien modifier d'autre entre les deux exécutions ; la note de clôture nomme la cible de l'exécution qui a abouti ; ».

### 7. remarque — code : lecture_scellee_v1.py l. 75-77 (empreinte_environnement)

**Constat.** L'empreinte de l'environnement ne porte que la version de l'interpréteur et les couples nom==version des distributions. Elle ne porte ni l'interpréteur lui-même, ni `sys.path` : une entrée de PYTHONPATH qui masquerait un module sans métadonnées passe donc. Elle ne porte pas non plus le contenu des fichiers installés. Or la règle de l'essai permet de corriger les « variables » de la commande. Cela reste sans effet sur un lecteur qui suit sa consigne.

**Correction proposée.** Dans `lecture_scellee_v2`, remplacer `return _sha((platform.python_version() + "\n" + "\n".join(dists)).encode())` par `return _sha("\n".join([sys.executable, platform.python_version(), *sys.path, "--", *dists]).encode())`. L'attendu est alors calculé avec la commande exacte, ce que la correction du constat 3 exige déjà.

### 8. remarque — § 3 l. 176-177 (rapport de lecteur qui diffère de la sortie)

**Constat.** Quand le rapport du lecteur qui fait foi diffère de la sortie, la sortie fait foi et le rapport « n'est pas retenu ». Le verdict retenu n'a alors été prononcé par aucun sous-agent neuf. Le texte le dit pour le double échec de lecteur (« R13 non tenu, ce qui est rapporté »), mais pas ici. Cela ne change aucun verdict.

**Correction proposée.** l. 177 : remplacer « un rapport de lecteur qui en diffère n'est pas retenu. » par « un rapport de lecteur qui en diffère n'est pas retenu, sans remplacement du lecteur ; le verdict de la sortie est alors rapporté « R13 non tenu (rapport contraire à la sortie) ». »

## Angle « application des constats du rapport v6 » — bloquant : oui

J'ai vérifié par programme. Les empreintes citées sont exactes : rapport v6 11f135d8…, lecture_scellee_v1 1b6f365e…, essais bdc569a5…. Elles valent pour le commit f8263a75, pour a91ba8cf (qui contient les trois fichiers) et pour les compagnons. L'arbre src/ est le même aux deux commits : 201033da…. Rien n'a changé dans src/ depuis 873ab00c, sauf l'ajout de lecture_scellee_v1. Les textes insérés figurent chacun une seule fois. Je n'ai trouvé ni marque @@ ni phrase cassée. Les renvois au texte (l. 241-242, 329-338, 371) et les deux citations des § 5 (d) sont justes. Les 15 essais de lecture_scellee_v1 passent dans une copie /tmp. Les huit constats v6 sont appliqués en substance, le bloquant v6 par le transfert de la lecture au code scellé. Il reste un bloquant de code, démontré par un essai : quand src/ porte une modification non commitée, empreinte_code rend une chaîne témoin fixe au lieu de refuser. Un attendu calculé sur un arbre ainsi modifié rend donc la garde du code inopérante. Restent aussi une règle ambiguë (l. 167), une imprécision du contrôle final, et deux inexactitudes de traçabilité qui rendent « Aucun constat écarté » faux à la lettre.

### 1. bloquant — src/controle_ia/temoin_bailey/lecture_scellee_v1.py l. 65-72 (empreinte_code) et l. 119 (jouer) ; addendum § 3, l. 159-162

**Constat.** Quand src/ porte une modification non commitée, empreinte_code renvoie la chaîne fixe « src/ modifié hors commit » au lieu de lever une erreur. jouer compare ensuite cette chaîne à l'attendu, et --calculer-attendu l'écrit telle quelle dans l'attendu. Le texte ne dit ni où ni à quel commit l'attendu est calculé. Si la session le calcule dans un arbre dont src/ est modifié (par exemple la copie principale partagée avec d'autres chantiers), la garde du code devient inopérante : tout code modifié sans commit passe, puisque les deux côtés valent la même chaîne. C'est la voie (c) du bloquant v6, rouverte. Démontré dans /tmp (copie de src au commit f8263a75, dossier factice T3.poste_local) : lecture_v8 modifiée sans commit pour rendre « VERDICT FORGE », puis attendu calculé sur cet arbre ; la commande rend « aboutie », sa sortie scellée porte « VERDICT FORGE », et le contrôle par programme de la l. 202-204 ne voit aucun écart (champ attendu égal au fichier de la note). Second effet, sans malveillance : si l'attendu est calculé à un autre commit, ou sur un arbre modifié, alors que le lecteur joue la commande dans un arbre neuf, les deux runs finissent en « refus : empreintes ». L'essai sur dossier factice ne l'attrape pas, car il emploie son propre attendu (l. 163).

**Correction proposée.** Code : dans empreinte_code, remplacer `if statut.strip():\n        return "src/ modifié hors commit"` par `if statut.strip():\n        raise GardeArret("lecture scellée : src/ modifié hors commit")`. jouer range alors ce cas en « refus : empreintes » (except Exception, l. 115), et --calculer-attendu sort en erreur sans rien écrire. Dans jouer, avant la boucle, ajouter : `if not all(isinstance(v, str) and re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", v) for v in attendu.values()):` → `sortie["issue"] = ISSUE_EMPREINTES; return sortie` (import re). Essais : ajouter « src modifié : --calculer-attendu refuse » et « attendu non hexadécimal : refus : empreintes, aucune exécution » ; dans le bout en bout (l. 177), remplacer "c" et "e" par "c" * 40 et "e" * 64. Texte, l. 159-161 : remplacer « le commit du code ; les empreintes attendues (code, dossier, environnement), dans un fichier écrit par `lecture_scellee_v1 --calculer-attendu`, qui ne fait que des empreintes d'octets et ne lit aucune note ; » par « le commit du code, celui du § 4 sauf addendum neuf ; les empreintes attendues (code, dossier, environnement), dans un fichier écrit par `lecture_scellee_v1 --calculer-attendu`, joué dans l'arbre de travail neuf de la commande, au commit nommé et avec l'interpréteur du dépôt ; ce code ne fait que des empreintes d'octets, ne lit aucune note et refuse si `src/` porte une modification non commitée ; le champ `code` de cet attendu est l'arbre `src/` du commit nommé (`git rev-parse <commit>:src`), ce que la note constate ; ». l. 163 : remplacer « aux seuls chemins du dossier, de l'attendu et de la sortie près, » par « aux seuls chemins du dossier, de l'attendu et de la sortie près (l'attendu factice est calculé de même et ses champs `code` et `environnement` sont égaux à ceux de l'attendu réel, ce que la note constate), ». Ensuite, recalculer au § 4 (l. 266-272) l'empreinte de lecture_scellee_v1, celle des essais, le commit et les comptes d'essais.

### 2. à corriger — § 3, l. 165-167 (constat 2 de l'angle « critère central » du rapport v6)

**Constat.** La v6 proposait, après l'échec de l'essai factice : « les lecteurs sont lancés sur elle et la puce « Refus ou erreur à la lecture » s'applique ». Le texte dit « la règle mécanique s'applique ensuite sans exception ». Or trois puces du § 3 parlent de « règle mécanique » (l. 205, 215 et, implicitement, 168). Le texte ne dit pas si les lecteurs sont lancés sur la dernière commande essayée, ou si le run est déclaré « pas de verdict » sans lecteur. Les deux lectures donnent des issues différentes (une commande qui échoue sur le factice peut aboutir sur le dossier réel), et la règle n'est donc pas applicable telle qu'écrite.

**Correction proposée.** Remplacer « la note de clôture le dit et nomme la dernière commande essayée, et la règle mécanique s'applique ensuite sans exception. » par « la note de clôture le dit et nomme la dernière commande essayée ; les lecteurs sont lancés sur elle, et les puces « Lecteur remplacé » et « Refus ou erreur à la lecture » s'appliquent ensuite sans exception. »

### 3. à corriger — § 3, l. 202-204 (contrôle par programme après les verdicts)

**Constat.** Le contrôle compare l'empreinte de chaque sortie « à celle qu'a rendue le lecteur ». Le texte ne règle pas un cas pourtant prévu par la puce suivante : la sortie et le rapport sont scellés aux chemins nommés (donc aucun remplacement), mais le lecteur n'a rendu aucune empreinte (il a fini sans message, ou il a été arrêté à 24 h juste après le scellement). Il n'y a alors rien à comparer, et la session décide seule si c'est un « écart », donc si le run a un verdict. Elle le décide sans avoir rien lu, mais la règle n'est pas mécanique.

**Correction proposée.** Remplacer « et son empreinte à celle qu'a rendue le lecteur : un écart vaut « pas de verdict » pour ce run. » par « et son empreinte à celle qu'a rendue le lecteur ou, s'il n'en a rendu aucune, à celle de son compagnon `.sha256` (absence de rendu rapportée) : un écart vaut « pas de verdict » pour ce run. »

### 4. remarque — Contre-lecture, l. 409-411 (paragraphe v5) et l. 428 et 432 (paragraphe v6)

**Constat.** Le constat 2 (3) de l'angle « application » du rapport v6 n'est pas appliqué. Le paragraphe v5 affirme toujours que « l'en-tête « Ordre, sans autre étape… » du § 6 reste juste, la règle n'ajoutant aucune étape ». C'est faux depuis que l'en-tête (l. 331-332) nomme le rejeu de l'assemblage et l'essai factice. Le paragraphe v6 cite « en-tête du § 6 » parmi les points repris et conclut « Aucun constat écarté » sans dire que ce remplacement est omis. Il résume aussi l'essai par « chemins et arguments seulement », alors que la l. 165 permet « chemins, arguments et variables ».

**Correction proposée.** l. 409-411 : remplacer « et l'en-tête « Ordre, sans autre étape… » du § 6 reste juste, la règle n'ajoutant aucune étape ; » par « et l'en-tête « Ordre, sans autre étape… » du § 6 ne nommait alors aucune étape ajoutée (il nomme, depuis la vérification v6, le rejeu de l'assemblage et l'essai de la commande sur un dossier factice) ; ». l. 426 : remplacer « (chemins et arguments seulement, 24 h, jamais le code) » par « (chemins, arguments et variables seulement, 24 h, jamais le code) ».

### 5. remarque — Contre-lecture, l. 389-392 (paragraphe v4) et l. 429-431

**Constat.** La remarque 4 (a) de l'angle « application » du rapport v6 n'est pas appliquée et le texte ne le dit pas. Le renvoi aux deux § 5 (d) et sa conséquence au § 5 (f) relèvent du point 8 de l'angle « application » du rapport v4 (vérifié : v4, « ### 8. remarque — § 3, l. 177 (renvoi aux addenda 5 et 6, § 5 (d)) », sous l'angle « application des constats de la passe finale »). Le paragraphe v4 les range pourtant toujours sous le point 8 de l'angle « phase de lecture ». Le paragraphe v6 traite (b) et (c), mais pas (a), puis conclut « Aucun constat écarté ».

**Correction proposée.** l. 389-392 : remplacer « (angle « application », points 1 à 4 et 6 (b) ; angle « phase de lecture », points 1 (second remplacement), 2, 3 (mention « valeur de note vue » ; date du constat, sans objet faute de délai) et 8 (renvoi aux deux § 5 (d) retiré avec la dichotomie, conséquence portée au § 5 (f))) ; » par « (angle « application », points 1 à 4, 6 (b) et 8 (renvoi aux deux § 5 (d) retiré avec la dichotomie, conséquence portée au § 5 (f) ; le renvoi revient, cité exactement, au refus de l'assemblage, § 3, dont ce texte tranche le nœud) ; angle « phase de lecture », points 1 (second remplacement), 2, 3 (mention « valeur de note vue » ; date du constat, sans objet faute de délai) et 8) ; ».
