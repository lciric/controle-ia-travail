"""Différentiels déclarés des fichiers neufs du second addendum de B bis (marche v4, lecture v3, registre v2, lanceur et
amorce v4) : pour chaque fichier neuf, (fichier précédent, couples « ancien, nouveau, nombre d'occurrences exigé »). Ce
sont les couples mêmes qui ont produit les fichiers neufs (programme de la rédaction) ; les essais refont chaque fichier neuf
depuis le précédent et exigent l'égalité exacte : aucun autre changement n'existe. `validation_imbriquee_v4` est un module
neuf (il importe la v3) : son différentiel avec la proposition du diagnostic est écrit dans `diff-v3-v4.txt`."""

MIN_ESSAIS_V4 = 148


def appliquer(texte: str, couples) -> str:
    for ancien, nouveau, n in couples:
        assert texte.count(ancien) == n, (ancien[:70], texte.count(ancien), n)
        texte = texte.replace(ancien, nouveau)
    return texte


COUPLES = {'scripts/amorce_bbis_v4.sh': ('scripts/amorce_bbis_v3.sh',
                               [("# Amorce de l'instance de l'étape B bis de T0.7, v3 (la v2, dont la marche est "
                                 '`controle_ia.t07bbis.marche_v3` : contrôle\n'
                                 "# carte-processeur sans issue « sans objet », R-2919 ; minimum d'essais relevé au compte neuf "
                                 '; blocs marqués identiques à ceux de\n'
                                 '# la v1 ; les v1 et v2 restent, R12) (prereg/T0.7-etape-B-bis-v1.md, plan, points 1 à 8 ; « '
                                 'Calcul et dépense » ;\n',
                                 "# Amorce de l'instance de l'étape B bis de T0.7, v4 (la v3, dont la marche est "
                                 '`controle_ia.t07bbis.marche_v4` : contrôle\n'
                                 '# carte-processeur v4 et mesure de dispersion du second addendum ; branche de sortie neuve '
                                 'donnees/t07-etape-b-bis-v2 (la v1 porte\n'
                                 "# la course arrêtée, R12) ; minimum d'essais relevé ; blocs marqués identiques à ceux de la v1 "
                                 '; les v1 à v3 restent, R12)\n'
                                 '# (prereg/T0.7-etape-B-bis-v1.md, plan, points 1 à 8 ; « Calcul et dépense » ;\n',
                                 1),
                                ('controle_ia.t07bbis.marche_v3', 'controle_ia.t07bbis.marche_v4', 2),
                                ('passée par scripts/lancer_bbis_v3.sh', 'passée par scripts/lancer_bbis_v4.sh', 1),
                                ('(lancer_bbis_v3.sh verifier-destruction)', '(lancer_bbis_v4.sh verifier-destruction)', 1),
                                ('donnees/t07-etape-b-bis-v1', 'donnees/t07-etape-b-bis-v2', 2),
                                ('/scripts/lancer_bbis_v3.sh*\n',
                                 '/scripts/lancer_bbis_v3.sh*\n/scripts/amorce_bbis_v4.sh*\n/scripts/lancer_bbis_v4.sh*\n',
                                 1),
                                ('MIN_ESSAIS=115\n',
                                 '# v4 (second addendum) : 115 de la v3 plus les essais neufs du second addendum qui passent '
                                 'sans docs/notes ni brouillons\n'
                                 "# (rapport-second-addendum-bbis-v1.md, § 3 ; à recompter sur l'arbre de l'instance simulé "
                                 'avant le feu)\n'
                                 'MIN_ESSAIS=148\n',
                                 1)]),
 'scripts/lancer_bbis_v4.sh': ('scripts/lancer_bbis_v3.sh',
                               [("# Chaîne de session de l'étape B bis de T0.7, v3 (la v2, qui passe l'amorce v3 : marche v3, "
                                 'contrôle carte-processeur\n'
                                 '# sans issue « sans objet », R-2919 ; les v1 et v2 restent, R12) '
                                 "(prereg/T0.7-etape-B-bis-v1.md, « Calcul et dépense », « Liste d'arrêt » ; ligne\n",
                                 "# Chaîne de session de l'étape B bis de T0.7, v4 (la v3, qui passe l'amorce v4 : marche v4, "
                                 'contrôle carte-processeur v4 et\n'
                                 '# mesure de dispersion du second addendum ; gardes de registre v2 : CODE-BBIS remplacée une '
                                 'fois, une course de plus accordée par\n'
                                 '# GO-2026-11-16-11 ; les v1 à v3 restent, R12) (prereg/T0.7-etape-B-bis-v1.md, « Calcul et '
                                 "dépense », « Liste d'arrêt » ; ligne\n",
                                 1),
                                ('#                                    GO-2026-11-14-09, une relance au plus, échéance, relance '
                                 'après le 21 novembre 12:00 UTC refusée ;\n',
                                 '#                                    GO-2026-11-14-09, une relance au plus, plus une course '
                                 '(RELANCES=2) si le feu porte aussi\n'
                                 '#                                    GO-2026-11-16-11 et CODE-BBIS est remplacée, échéance, '
                                 'relance après le 21 novembre 12:00 UTC refusée ;\n',
                                 1),
                                ('amorce_bbis_v3.sh', 'amorce_bbis_v4.sh', 7),
                                ('lancer_bbis_v3.sh', 'lancer_bbis_v4.sh', 3),
                                ('-m controle_ia.t07bbis.registre_bbis_v1 "$@"; }',
                                 '-m controle_ia.t07bbis.registre_bbis_v2 "$@"; }',
                                 1)]),
 'src/controle_ia/t07bbis/lecture_v3.py': ('src/controle_ia/t07bbis/lecture_v2.py',
                                           [("10 ; « Critères de lecture gelés » A, B, D ; « Seuil » ; « Liste d'arrêt »), v2 : "
                                             'la v1, plus la réserve **R-PILE** (règle et\n'
                                             "phrase du brouillon 6 : écrite dès qu'une sonde finale lue est de la famille « "
                                             'attention »), le point (7) de la section D, et la\n'
                                             'lecture du champ `controle_carte_processeur` du fichier fermé des sondes (marche '
                                             'v3 : un écart numérique ≤ 10⁻⁴ par famille, le\n'
                                             "déterminisme de l'attention au bit près ; une trace « sans objet », un champ "
                                             'absent ou non numérique arrête la lecture) ; majeur M1\n'
                                             'de `contre-lecture-brouillon5-et-code-v2-v1.md`, R-2919 ; la v1 reste (R12).\n',
                                             "10 ; « Critères de lecture gelés » A, B, D ; « Seuil » ; « Liste d'arrêt »), v3 : "
                                             'la v2, modifiée par le **second addendum\n'
                                             "d'écart** (`brouillon-second-addendum-bbis-v1.md`) : réserve **R-PILE étendue à la "
                                             "linéaire** (écrite dès qu'une sonde finale lue,\n"
                                             "linéaire ou « attention », source ou ENC, l'est) et portant le résumé de la "
                                             '**mesure de dispersion entre deux ordres de calcul**\n'
                                             '(`dispersion_ordres`, information seulement, aucun état ne change) ; point (7) de '
                                             'la section D réécrit ; lecture du champ\n'
                                             '`controle_carte_processeur` de la marche v4 (version « v4 », écart ≤ 10⁻⁴ à 3 '
                                             'époques par famille, déterminisme au bit près de\n'
                                             'chaque famille, information à 300 époques de la linéaire, phrase du discriminant) '
                                             '; ligne `CODE-BBIS` remplacée une seule fois\n'
                                             'lue au registre propre (`lire_lignes`, `exiger_ordre_propre`) ; les v1 et v2 '
                                             'restent (R12).\n',
                                             1),
                                            ('posée par `scripts/amorce_bbis_v3.sh`), liste blanche des entrées',
                                             'posée par `scripts/amorce_bbis_v4.sh`), liste blanche des entrées',
                                             1),
                                            ('    "R-PILE": ("R-PILE : sonde « attention » reproductible au bit près sur la même '
                                             'pile de calcul seulement (carte, pilote, versions "\n'
                                             '               "de torch et de numpy) ; sur une autre pile, l\'apprentissage peut '
                                             'rendre une autre sonde, surtout quand elle "\n'
                                             '               "n\'apprend rien"),\n',
                                             '    "R-PILE": ("R-PILE : sonde finale (linéaire ou « attention ») reproductible au '
                                             'bit près sur la même pile de calcul seulement "\n'
                                             '               "(carte, pilote, versions de torch et de numpy) ; sur une autre '
                                             'pile ou dans un autre ordre de calcul, l\'apprentissage "\n'
                                             '               "peut rendre une autre sonde, surtout quand elle ajuste mal, et le '
                                             'réglage retenu peut changer (ex aequo à 0,005)"),\n',
                                             1),
                                            ('             "(7) une aire de la famille « attention » est celle d\'une sonde '
                                             'parmi celles que rendrait le même apprentissage sous "\n'
                                             '             "d\'autres arrondis (réserve R-PILE) : sur données synthétiques, la '
                                             'dispersion est négligeable quand la sonde apprend "\n'
                                             '             "un signal, de l\'ordre de 0,007 quand elle n\'apprend rien ; sur de '
                                             'vraies activations, elle n\'est pas mesurée.")\n',
                                             '             "(7) une aire de sonde, linéaire ou « attention », est celle d\'une '
                                             'sonde parmi celles que rendrait le même apprentissage "\n'
                                             '             "sous d\'autres arrondis (réserve R-PILE) : sur données fabriquées, '
                                             'la dispersion va de négligeable, quand la sonde "\n'
                                             '             "apprend un signal, à plusieurs centièmes quand elle ajuste mal '
                                             '(0,007 à 0,047 entre deux ordres de calcul) ; sur les "\n'
                                             '             "vraies activations, elle est mesurée entre deux ordres de calcul de '
                                             'la carte, comme information seulement "\n'
                                             '             "(« dispersion entre ordres de calcul ») ; elle n\'est pas mesurée '
                                             'entre la carte et une autre pile.")\n',
                                             1),
                                            ('def reserve_pile(sondes_doc: dict) -> list[str]:\n'
                                             '    """R-PILE (brouillon 6, qualifications toujours écrites) : écrite dès qu\'une '
                                             'sonde finale lue est de la famille « attention »\n'
                                             "    (sonde finale d'une source et d'un pli, `famille` du fichier fermé des sondes "
                                             "; sonde finale d'ENC, réglage « attention- » ;\n"
                                             '    interprétation déclarée : ENC est une sonde finale lue) ; les sondes '
                                             'concernées sont nommées."""\n'
                                             '    lues = []\n'
                                             '    for src, par_pli in sorted((sondes_doc.get("sources") or {}).items()):\n'
                                             '        for ek, m in sorted(par_pli.items()):\n'
                                             '            if "echec" in m:\n'
                                             '                continue\n'
                                             '            if m.get("famille") == "attention":\n'
                                             '                lues.append(f"{src} {ek}")\n'
                                             '            enc = m.get("enc") or {}\n'
                                             '            if "echec" not in enc and str(enc.get("reglage", '
                                             '"")).startswith("attention-"):\n'
                                             '                lues.append(f"{src} {ek} (ENC)")\n'
                                             '    return [f"{RESERVES_FIXES[\'R-PILE\']} (sondes « attention » lues : {\', '
                                             '\'.join(lues)})"] if lues else []\n',
                                             'NOMS_FAMILLES = {"lineaire": "linéaires", "attention": "« attention »"}\n'
                                             'EPOQUES_CONTROLE_V4 = 3                 # = '
                                             "validation_imbriquee_v4.EPOQUES_CONTROLE (essai ; la lecture n'importe pas torch)\n"
                                             'CHAMP_O2 = "sonde_o2"                   # = validation_imbriquee_v4.CHAMP_O2 '
                                             '(essai)\n'
                                             'DISCRIMINANT = {\n'
                                             '    "accord": ("information à 300 époques au plus 10⁻⁴ sur le couple contrôlé : '
                                             'carte et processeur s\'accordent aussi à 300 "\n'
                                             '               "époques sur ce couple (aucune amplification vue sur ce couple ; '
                                             'rien n\'est dit des autres couples)"),\n'
                                             '    "ecart": ("information à 300 époques au-dessus de 10⁻⁴, ou non finie, sur le '
                                             'couple contrôlé, contrôle à 3 époques passé : "\n'
                                             '              "amplification d\'arrondi ou erreur de chaîne qui ne commence '
                                             'qu\'après la troisième époque, indiscernables par ce "\n'
                                             '              "contrôle (réserve R-B du second addendum)"),\n'
                                             '}\n'
                                             '\n'
                                             '\n'
                                             'def phrase_dispersion(d: dict | None) -> str:\n'
                                             '    """Résumé de la mesure de dispersion entre deux ordres de calcul (second '
                                             'addendum ; information, aucun état ne change)."""\n'
                                             '    tete = "dispersion des aires entre deux ordres de calcul de la carte '
                                             '(information du second addendum, aucun état ne change)"\n'
                                             '    if not isinstance(d, dict):\n'
                                             '        return f"{tete} : non lue"\n'
                                             '    if "non_faite" in d:\n'
                                             '        return f"{tete} : mesure non faite ({d[\'non_faite\']})"\n'
                                             '    if not d.get("cellules_lues"):\n'
                                             '        return f"{tete} : aucune cellule calculable"\n'
                                             '    return (f"{tete} : écart absolu maximal {_f(d[\'ecart_max\'])} '
                                             '({d[\'cellule_ecart_max\']}) sur {d[\'cellules_lues\']} cellules "\n'
                                             '            f"lues ; réglage retenu changé dans {d[\'plis_reglage_change\']} plis '
                                             'sur {d[\'plis_compares\']}")\n'
                                             '\n'
                                             '\n'
                                             'def reserve_pile(sondes_doc: dict, dispersion: dict | None = None) -> list[str]:\n'
                                             '    """R-PILE (second addendum, EC-2 révisé ; qualifications toujours écrites) : '
                                             "écrite dès qu'une sonde finale est lue, de la\n"
                                             "    famille linéaire ou « attention » (sonde finale d'une source et d'un pli, "
                                             '`famille` du fichier fermé des sondes ; sonde finale\n'
                                             "    d'ENC, famille lue au début de son réglage ; ENC est une sonde finale lue) ; "
                                             'les sondes lues sont nommées par famille ; la\n'
                                             '    mesure de dispersion entre deux ordres de calcul y est résumée '
                                             '(`phrase_dispersion`)."""\n'
                                             '    lues = {"lineaire": [], "attention": []}\n'
                                             '    for src, par_pli in sorted((sondes_doc.get("sources") or {}).items()):\n'
                                             '        for ek, m in sorted(par_pli.items()):\n'
                                             '            if "echec" in m:\n'
                                             '                continue\n'
                                             '            if m.get("famille") in lues:\n'
                                             '                lues[m["famille"]].append(f"{src} {ek}")\n'
                                             '            enc = m.get("enc") or {}\n'
                                             '            f = str(enc.get("reglage", "")).split("-", 1)[0]\n'
                                             '            if "echec" not in enc and f in lues:\n'
                                             '                lues[f].append(f"{src} {ek} (ENC)")\n'
                                             '    if not any(lues.values()):\n'
                                             '        return []\n'
                                             '    noms = " ; ".join(f"{NOMS_FAMILLES[f]} : {\', \'.join(v)}" for f, v in '
                                             'lues.items() if v)\n'
                                             '    return [f"{RESERVES_FIXES[\'R-PILE\']} (sondes finales lues — {noms}) ; '
                                             '{phrase_dispersion(dispersion)}"]\n',
                                             1),
                                            ('def exiger_controle_carte(sondes_doc: dict) -> dict:\n'
                                             '    """Champ `controle_carte_processeur` du fichier fermé des sondes (marche v3) : '
                                             'chaque famille de la marche porte un écart\n'
                                             "    numérique fini ≤ 10⁻⁴ ; l'attention, le déterminisme au bit près ; une trace « "
                                             'sans objet », un champ absent ou non numérique :\n'
                                             '    arrêt de la lecture (`RefusLecture`). Rend les écarts lus."""\n',
                                             'def exiger_controle_carte(sondes_doc: dict) -> dict:\n'
                                             '    """Champ `controle_carte_processeur` du fichier fermé des sondes (marche v4, '
                                             'second addendum) : `version_controle` « v4 » ;\n'
                                             '    chaque famille de la marche porte un écart numérique fini ≤ 10⁻⁴ **à 3 '
                                             'époques** et le déterminisme au bit près à 300 époques ;\n'
                                             "    la linéaire porte l'écart à 300 époques écrit comme information "
                                             '(`ecart_300_information`, `decide` faux) ; une trace « sans\n'
                                             '    objet », un champ absent ou non numérique : arrêt de la lecture '
                                             "(`RefusLecture`). Rend les écarts lus, l'information et la\n"
                                             '    phrase du discriminant (réserve R-B), sans aucun effet sur un état."""\n',
                                             1),
                                            ('        ecarts[f] = float(e)\n'
                                             '    sortie = {"ecarts": ecarts, "tolerance": TOLERANCE_CARTE, "couple": '
                                             '[c.get("cellule"), c.get("pli")]}\n'
                                             '    if "attention" in familles:\n'
                                             '        d = c.get("determinisme_attention")\n'
                                             '        if not (isinstance(d, dict) and d.get("egal_au_bit") is True):\n'
                                             '            raise RefusLecture("contrôle carte-processeur : déterminisme de '
                                             'l\'attention absent ou faux : arrêt de la lecture")\n'
                                             '        sortie["determinisme_attention"] = True\n'
                                             '    return sortie\n',
                                             '        ecarts[f] = float(e)\n'
                                             '        if c[f].get("epoques") != EPOQUES_CONTROLE_V4:\n'
                                             '            raise RefusLecture(f"contrôle carte-processeur : horizon de « {f} » '
                                             '{c[f].get(\'epoques\')!r} ≠ "\n'
                                             '                               f"{EPOQUES_CONTROLE_V4} époques (second addendum) : '
                                             'arrêt de la lecture")\n'
                                             '    if c.get("version_controle") != "v4":\n'
                                             '        raise RefusLecture("contrôle carte-processeur : version_controle autre que '
                                             '« v4 » (second addendum) : arrêt de la lecture")\n'
                                             '    sortie = {"ecarts": ecarts, "tolerance": TOLERANCE_CARTE, "couple": '
                                             '[c.get("cellule"), c.get("pli")],\n'
                                             '              "epoques": EPOQUES_CONTROLE_V4, "version_controle": "v4", '
                                             '"determinisme": {}}\n'
                                             '    for f in familles:\n'
                                             '        d = c.get(f"determinisme_{f}")\n'
                                             '        if not (isinstance(d, dict) and d.get("egal_au_bit") is True):\n'
                                             '            nom = "de l\'attention" if f == "attention" else "de la linéaire"\n'
                                             '            raise RefusLecture(f"contrôle carte-processeur : déterminisme {nom} '
                                             'absent ou faux : arrêt de la lecture")\n'
                                             '        sortie["determinisme"][f] = True\n'
                                             '    if "attention" in familles:\n'
                                             '        sortie["determinisme_attention"] = True\n'
                                             '    info = c["lineaire"].get("ecart_300_information")\n'
                                             '    if not (isinstance(info, dict) and info.get("decide") is False\n'
                                             '            and ("refus" in info or isinstance(info.get("ecart_relatif_max"), '
                                             '(int, float)))\n'
                                             '            and not isinstance(info.get("ecart_relatif_max"), bool)):\n'
                                             '        raise RefusLecture("contrôle carte-processeur : information à 300 époques '
                                             'de la linéaire absente ou mal formée : arrêt "\n'
                                             '                           "de la lecture")\n'
                                             '    e300 = info.get("ecart_relatif_max")\n'
                                             '    accord = "refus" not in info and np.isfinite(float(e300)) and float(e300) <= '
                                             'TOLERANCE_CARTE\n'
                                             '    sortie["information_300"] = info\n'
                                             '    sortie["discriminant"] = DISCRIMINANT["accord" if accord else "ecart"]\n'
                                             '    return sortie\n',
                                             1),
                                            ('ORDRE_PROPRE = ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS", "SCORES-BBIS")\n',
                                             'ORDRE_PROPRE = ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS", "SCORES-BBIS")\n'
                                             'REMPLACABLES_PROPRES = ("CODE-BBIS",)\n',
                                             1),
                                            ('def lire_lignes(registre: Path, cles, exigees, propre: bool) -> dict:\n'
                                             '    """Lignes `| clé | date | chemin | sha256 |` des clés demandées (une '
                                             'exactement pour chaque clé présente ; exigée absente →\n'
                                             '    refus) ; registre propre : toute autre clé de forme valide → refus (seules les '
                                             'clés de B bis y sont permises)."""\n',
                                             'def lire_lignes(registre: Path, cles, exigees, propre: bool, remplacables=()) -> '
                                             'dict:\n'
                                             '    """Lignes `| clé | date | chemin | sha256 |` des clés demandées (une '
                                             'exactement pour chaque clé présente ; exigée absente →\n'
                                             '    refus) ; registre propre : toute autre clé de forme valide → refus (seules les '
                                             'clés de B bis y sont permises). Second\n'
                                             '    addendum : une clé de `remplacables` (`REMPLACABLES_PROPRES` : `CODE-BBIS` '
                                             'seulement) peut porter **deux** lignes, la seconde\n'
                                             '    strictement postérieure, qui fait foi (« ligne `CODE-BBIS` remplacée une seule '
                                             "fois », liste d'arrêt) ; la première est rendue\n"
                                             '    sous `remplace` ; trois lignes ou plus, ou une seconde ligne non postérieure : '
                                             'refus."""\n',
                                             1),
                                            ('        if len(ls) != 1 or len(ls[0]) != 4 or not rg.DATE.fullmatch(ls[0][1]) or '
                                             'not rg.SHA.fullmatch(ls[0][3]):\n'
                                             '            fautes.append(f"ligne {k} en double ou mal formée")\n'
                                             '            continue\n'
                                             '        _, date, chemin, sha = ls[0]\n'
                                             '        if chemin.startswith("/") or ".." in Path(chemin).parts:\n'
                                             '            fautes.append(f"ligne {k} : chemin {chemin!r}")\n'
                                             '            continue\n'
                                             '        sortie[k] = {"date": date, "instant": rg.instant_utc(date), "chemin": '
                                             'chemin, "sha256": sha}\n',
                                             '        permis = 2 if k in tuple(remplacables) else 1\n'
                                             '        if (len(ls) > permis or any(len(l) != 4 or not rg.DATE.fullmatch(l[1]) or '
                                             'not rg.SHA.fullmatch(l[3]) for l in ls)):\n'
                                             '            fautes.append(f"ligne {k} en double ou mal formée")\n'
                                             '            continue\n'
                                             '        mauvais = [l[2] for l in ls if l[2].startswith("/") or ".." in '
                                             'Path(l[2]).parts]\n'
                                             '        if mauvais:\n'
                                             '            fautes.append(f"ligne {k} : chemin {mauvais[0]!r}")\n'
                                             '            continue\n'
                                             '        lus = [{"date": d, "instant": rg.instant_utc(d), "chemin": ch, "sha256": '
                                             's} for _, d, ch, s in ls]\n'
                                             '        if len(lus) == 2 and not lus[0]["instant"] < lus[1]["instant"]:\n'
                                             '            fautes.append(f"ligne {k} remplacée : la seconde ligne n\'est pas '
                                             'strictement postérieure à la première")\n'
                                             '            continue\n'
                                             '        sortie[k] = {**lus[1], "remplace": lus[0]} if len(lus) == 2 else lus[0]\n',
                                             1),
                                            ('def exiger_ordre_propre(lignes: dict) -> None:\n'
                                             '    for a, b in zip(ORDRE_PROPRE, ORDRE_PROPRE[1:]):\n'
                                             '        if a in lignes and b in lignes and not lignes[a]["instant"] < '
                                             'lignes[b]["instant"]:\n'
                                             '            raise RefusLecture(f"ligne {a} ({lignes[a][\'date\']}) pas strictement '
                                             'antérieure à {b} ({lignes[b][\'date\']})")\n',
                                             'def exiger_ordre_propre(lignes: dict) -> None:\n'
                                             '    """Ordre du plan, point 2 ; second addendum : une ligne `CODE-BBIS` remplacée '
                                             'se lit SCELLEMENT-BBIS < CODE-BBIS (première)\n'
                                             '    < GO-BBIS < CODE-BBIS (remplacement) < SCORES-BBIS."""\n'
                                             '    lignes, chaine = dict(lignes), list(ORDRE_PROPRE)\n'
                                             '    if "CODE-BBIS" in lignes and "remplace" in lignes["CODE-BBIS"]:\n'
                                             '        lignes["CODE-BBIS (première)"] = lignes["CODE-BBIS"]["remplace"]\n'
                                             '        chaine = ["SCELLEMENT-BBIS", "CODE-BBIS (première)", "GO-BBIS", '
                                             '"CODE-BBIS", "SCORES-BBIS"]\n'
                                             '    for a, b in zip(chaine, chaine[1:]):\n'
                                             '        if a in lignes and b in lignes and not lignes[a]["instant"] < '
                                             'lignes[b]["instant"]:\n'
                                             '            raise RefusLecture(f"ligne {a} ({lignes[a][\'date\']}) pas strictement '
                                             'antérieure à {b} ({lignes[b][\'date\']})")\n',
                                             1),
                                            ('def _essai(f, *a, **k):\n',
                                             'def dispersion_ordres(asms: dict, specs: dict, sondes_doc: dict) -> dict:\n'
                                             '    """Mesure d\'information du second addendum (MD) : pour chaque cellule '
                                             '(plafond et transfert), aire du jeu décisif (O[positifs]\n'
                                             '    contre O[H], tâches du pli lu, moyenne des deux plis) par la sonde lue (ordre '
                                             "1) et par la sonde de l'ordre 2 de la même source\n"
                                             '    (`<groupe>__sonde_o2`) ; différence (ordre 2 − ordre 1), aires par pli, '
                                             'réglages retenus des deux ordres par pli ; résumé :\n'
                                             '    écart absolu maximal, plis dont le réglage retenu change. Aucun intervalle, '
                                             'aucun état, aucun seuil ; rien d\'autre ne change."""\n'
                                             '    d = sondes_doc.get("dispersion_ordres_calcul")\n'
                                             '    if not isinstance(d, dict):\n'
                                             '        return {"non_faite": "champ dispersion_ordres_calcul absent du fichier des '
                                             'sondes", "decide": False}\n'
                                             '    if "non_faite" in d:\n'
                                             '        return {"non_faite": str(d["non_faite"]), "ordre": d.get("ordre"), '
                                             '"decide": False}\n'
                                             '    sortie = {}\n'
                                             '    for nom, spec in {**specs["plafond"], **specs["transfert"]}.items():\n'
                                             '        src = spec.get("source") or nom\n'
                                             '        meta = (sondes_doc.get("sources") or {}).get(src, {})\n'
                                             '        reglages = {ek: {"ordre1": m.get("reglage"), "ordre2": (m.get("ordre2") or '
                                             '{}).get("reglage")}\n'
                                             '                    for ek, m in sorted(meta.items())}\n'
                                             '        if src not in asms:\n'
                                             '            sortie[nom] = {"source": src, "non_calculable": "source non lisible", '
                                             '"reglages": reglages}\n'
                                             '            continue\n'
                                             '        dp, dn = f"O-{spec[\'positifs\']}", f"O-{H}"\n'
                                             '        j1, m1 = _essai(asms[src].jeu, dp, dn, "sonde")\n'
                                             '        j2, m2 = _essai(asms[src].jeu, dp, dn, CHAMP_O2)\n'
                                             '        if j1 is None or j2 is None:\n'
                                             '            sortie[nom] = {"source": src, "non_calculable": m1 or m2, "reglages": '
                                             'reglages}\n'
                                             '            continue\n'
                                             '        a1, a2 = j1.aires_plis[:, 0], j2.aires_plis[:, 0]\n'
                                             '        sortie[nom] = {"source": src, "aire_ordre1": float(a1.mean()), '
                                             '"aire_ordre2": float(a2.mean()),\n'
                                             '                       "difference": float(a2.mean() - a1.mean()),\n'
                                             '                       "par_pli": {f"e{k}": {"aire_ordre1": float(a1[k]), '
                                             '"aire_ordre2": float(a2[k])} for k in range(len(a1))},\n'
                                             '                       "reglages": reglages}\n'
                                             '    lues = sorted(((abs(c["difference"]), n) for n, c in sortie.items() if '
                                             '"difference" in c), reverse=True)\n'
                                             '    compares = [(m.get("reglage"), m["ordre2"]["reglage"]) for par in '
                                             '(sondes_doc.get("sources") or {}).values()\n'
                                             '                for m in par.values() if "echec" not in m and '
                                             'isinstance(m.get("ordre2"), dict) and m["ordre2"].get("reglage")\n'
                                             '                and "echec" not in m["ordre2"]]\n'
                                             '    return {"ordre": d.get("ordre"), "decide": False, "cellules": sortie, '
                                             '"cellules_lues": len(lues),\n'
                                             '            "ecart_max": lues[0][0] if lues else None, "cellule_ecart_max": '
                                             'lues[0][1] if lues else None,\n'
                                             '            "plis_compares": len(compares), "plis_reglage_change": sum(1 for a, b '
                                             'in compares if a != b)}\n'
                                             '\n'
                                             '\n'
                                             'def _essai(f, *a, **k):\n',
                                             1),
                                            ('        propres = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, '
                                             'EXIGEES_PROPRES_LECTURE, propre=True)\n',
                                             '        propres = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, '
                                             'EXIGEES_PROPRES_LECTURE, propre=True,\n'
                                             '                              remplacables=REMPLACABLES_PROPRES)\n',
                                             1),
                                            ('    res["issue"] = (issue_complete({}, {}, None, motif_i0="marche sans scores") if '
                                             'not tabs\n'
                                             '                    else issue_complete(p_ii, t_ii, marque))\n',
                                             '    res["issue"] = (issue_complete({}, {}, None, motif_i0="marche sans scores") if '
                                             'not tabs\n'
                                             '                    else issue_complete(p_ii, t_ii, marque))\n'
                                             '    res["dispersion_ordres_calcul"] = dispersion_ordres(asms, specs, sondes_doc)\n',
                                             1),
                                            ('    reserves += reserve_pile(sondes_doc)\n',
                                             '    reserves += reserve_pile(sondes_doc, res["dispersion_ordres_calcul"])\n',
                                             1),
                                            ('                                  commande="python -m '
                                             'controle_ia.t07bbis.lecture_v2")\n',
                                             '                                  commande="python -m '
                                             'controle_ia.t07bbis.lecture_v3")\n',
                                             1),
                                            ('    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src '
                                             'python -m controle_ia.t07bbis.lecture_v2 --racine\n',
                                             '    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src '
                                             'python -m controle_ia.t07bbis.lecture_v3 --racine\n',
                                             1),
                                            ('        propres = lire_lignes(racine / REGISTRE_PROPRE, ("CODE-BBIS",), '
                                             '("CODE-BBIS",), propre=False)\n',
                                             '        propres = lire_lignes(racine / REGISTRE_PROPRE, ("CODE-BBIS",), '
                                             '("CODE-BBIS",), propre=False,\n'
                                             '                              remplacables=REMPLACABLES_PROPRES)\n',
                                             1)]),
 'src/controle_ia/t07bbis/marche_v4.py': ('src/controle_ia/t07bbis/marche_v3.py',
                                          [('"""Marche de l\'étape B bis sur l\'instance (`prereg/T0.7-etape-B-bis-v1.md`, plan, '
                                            "points 1 à 8 et 12 ; « Données gardées »), v3 : la v2, dont l'apprentissage appelle "
                                            '`validation_imbriquee_v3` (contrôle\n'
                                            'carte-processeur aux deux horizons sans issue « sans objet », joué à la fin de '
                                            "l'apprentissage sur un couple tiré parmi les sondes\n"
                                            "finales finies ; brouillon 6 du texte, plan, point 5 ; R-2919) ; rien d'autre ne "
                                            'change (les v1 et v2 restent, R12).\n',
                                            '"""Marche de l\'étape B bis sur l\'instance (`prereg/T0.7-etape-B-bis-v1.md`, plan, '
                                            "points 1 à 8 et 12 ; « Données gardées »), v4 : la v3, dont l'apprentissage appelle "
                                            '`validation_imbriquee_v4` (second\n'
                                            "addendum d'écart : contrôle carte-processeur à 3 époques dans les deux familles, "
                                            'déterminisme à 300 époques dans les deux, écart\n'
                                            'linéaire à 300 époques écrit comme information ; mesure de dispersion entre deux '
                                            'ordres de calcul, information seulement), dont les\n'
                                            "gardes d'entrée lisent le registre propre par `lecture_v3` (ligne `CODE-BBIS` "
                                            "remplacée une seule fois) ; rien d'autre ne change\n"
                                            '(les v1, v2 et v3 restent, R12).\n',
                                            1),
                                           ('   finale est finie (`ControleCarte.jouer` de la v3 ; aucun : arrêt)) ; garde de '
                                            'débit déclenchée : arrêt de\n',
                                            '   finale est finie (`ControleCarte.jouer` de la v4 ; aucun : arrêt)), puis '
                                            '**mesure de dispersion entre deux ordres de calcul**\n'
                                            '   (`validation_imbriquee_v4.mesurer_dispersion` : recette de la sonde rejouée dans '
                                            "l'ordre inverse des actions, scores fermés,\n"
                                            '   aucune aire ; ses apprentissages sont comptés par la garde de débit) ; garde de '
                                            'débit déclenchée : arrêt de\n',
                                            1),
                                           ('validation interne, jamais écrites) ; le journal ne porte que des durées. La '
                                            'poussée vers la branche `donnees/t07-etape-b-bis-v1`\n'
                                            'est faite par `scripts/amorce_bbis_v3.sh`, jamais par ce module.\n',
                                            'validation interne, jamais écrites) ; le journal ne porte que des durées. La '
                                            'poussée vers la branche `donnees/t07-etape-b-bis-v2`\n'
                                            'est faite par `scripts/amorce_bbis_v4.sh`, jamais par ce module.\n',
                                            1),
                                           ('    from .lecture_v1 import CLES_PROPRES, RefusLecture, lire_lignes\n',
                                            '    from .lecture_v3 import CLES_PROPRES, REMPLACABLES_PROPRES, RefusLecture, '
                                            'lire_lignes\n',
                                            1),
                                           ('        raise GardeArret("marche réelle hors de l\'instance (BBIS_INSTANCE absente, '
                                            'posée par scripts/amorce_bbis_v3.sh) : refus")\n',
                                            '        raise GardeArret("marche réelle hors de l\'instance (BBIS_INSTANCE absente, '
                                            'posée par scripts/amorce_bbis_v4.sh) : refus")\n',
                                            1),
                                           ('        tout = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, '
                                            '("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"), propre=True)\n',
                                            '        tout = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, '
                                            '("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"), propre=True,\n'
                                            '                           remplacables=REMPLACABLES_PROPRES)\n',
                                            1),
                                           ('                                  commande="python -m '
                                            'controle_ia.t07bbis.marche_v3")\n',
                                            '                                  commande="python -m '
                                            'controle_ia.t07bbis.marche_v4")\n',
                                            1),
                                           ('    from . import validation_imbriquee_v3 as vi\n',
                                            '    from . import validation_imbriquee_v4 as vi\n',
                                            1),
                                           ('    total = vi.apprentissages_prevus(len(specs), len(grille(couches, familles)), '
                                            'n_int, n_reet)\n',
                                            '    total = (vi.apprentissages_prevus(len(specs), len(grille(couches, familles)), '
                                            'n_int, n_reet)\n'
                                            '             + vi.apprentissages_mesure(len(specs), len(grille(couches, familles)), '
                                            'n_int))\n',
                                            1),
                                           ('    if controle.resultat is None:\n'
                                            '        raise GardeArret("contrôle carte-processeur non joué : arrêt")\n'
                                            '    etape["nom"] = "écriture des fichiers fermés"\n',
                                            '    if controle.resultat is None:\n'
                                            '        raise GardeArret("contrôle carte-processeur non joué : arrêt")\n'
                                            '    etape["nom"] = "mesure de dispersion entre ordres de calcul"\n'
                                            '    dispersion = vi.mesurer_dispersion(ctx, sources, plis, doses)\n'
                                            '    etape["nom"] = "écriture des fichiers fermés"\n',
                                            1),
                                           ('                          {"controle_carte_processeur": controle.resultat, '
                                            '"couple_controle": list(controle.couple),\n',
                                            '                          {"controle_carte_processeur": controle.resultat, '
                                            '"couple_controle": list(controle.couple),\n'
                                            '                           "dispersion_ordres_calcul": dispersion,\n',
                                            1),
                                           ('    """`python -m controle_ia.t07bbis.marche_v3 --racine R --run-7b RUN --run-bbis '
                                            'RUNB --travail DOSSIER` (marche réelle : la\n',
                                            '    """`python -m controle_ia.t07bbis.marche_v4 --racine R --run-7b RUN --run-bbis '
                                            'RUNB --travail DOSSIER` (marche réelle : la\n',
                                            1)]),
 'src/controle_ia/t07bbis/registre_bbis_v2.py': ('src/controle_ia/t07bbis/registre_bbis_v1.py',
                                                 [("(`prereg/T0.7-etape-B-bis-v1.md`, « Lignes de registre », « Liste d'arrêt », "
                                                   '« Calcul et dépense », « Seuil »), v1.\n',
                                                   "(`prereg/T0.7-etape-B-bis-v1.md`, « Lignes de registre », « Liste d'arrêt », "
                                                   '« Calcul et dépense », « Seuil »), v2 : la v1, modifiée\n'
                                                   "par le **second addendum d'écart** (`brouillon-second-addendum-bbis-v1.md`) "
                                                   'en trois points seulement : (1) la ligne `CODE-BBIS`\n'
                                                   "peut être **remplacée une seule fois** au registre propre (liste d'arrêt "
                                                   'scellée : « ligne `CODE-BBIS` remplacée une seule fois »),\n'
                                                   'par une seconde ligne ajoutée après `GO-BBIS` et avant `SCORES-BBIS`, jamais '
                                                   'réécrite ; la lecture de la fiche passe par\n'
                                                   '`lecture_v3.lire_lignes` (la seconde ligne fait foi) ; (2) la garde de '
                                                   'création admet **une course de plus** (relances = 2),\n'
                                                   'accordée par GO-2026-11-16-11, seulement si le feu écrit de la mère porte '
                                                   'aussi ce numéro et si `CODE-BBIS` est remplacée ;\n'
                                                   '(3) la limite du samedi 21 novembre 12:00 UTC vaut pour toute relance. Tout '
                                                   'le reste est celui de la v1 (la v1 reste, R12).\n',
                                                   1),
                                                  ('GO_ID = "GO-2026-11-14-09"\n',
                                                   'GO_ID = "GO-2026-11-14-09"\n'
                                                   'GO_ACCORD = "GO-2026-11-16-11"     # second addendum et nouvelle course (une '
                                                   'seule), sous GO-2026-11-14-09\n',
                                                   1),
                                                  ('        if cle in cles_bbis_presentes(registre):\n'
                                                   '            raise GardeArret(f"registre propre : ligne {cle} déjà présente, '
                                                   'jamais réécrite")\n',
                                                   '        vues = cles_bbis_presentes(registre)\n'
                                                   '        if cle in vues and not (cle == "CODE-BBIS" and '
                                                   'vues.count("CODE-BBIS") == 1 and "GO-BBIS" in vues\n'
                                                   '                                and "SCORES-BBIS" not in vues):\n'
                                                   '            raise GardeArret(f"registre propre : ligne {cle} déjà présente, '
                                                   'jamais réécrite (seule CODE-BBIS se remplace, une seule "\n'
                                                   '                             "fois, après GO-BBIS et avant SCORES-BBIS : '
                                                   'second addendum)")\n',
                                                   1),
                                                  ('    from .lecture_v1 import CLES_PROPRES, RefusLecture, lire_lignes\n'
                                                   '    racine = Path(racine)\n'
                                                   '    try:\n'
                                                   '        ligne = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, '
                                                   '("CODE-BBIS",), propre=True)["CODE-BBIS"]\n',
                                                   '    from .lecture_v3 import CLES_PROPRES, REMPLACABLES_PROPRES, '
                                                   'RefusLecture, lire_lignes\n'
                                                   '    racine = Path(racine)\n'
                                                   '    try:\n'
                                                   '        ligne = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, '
                                                   '("CODE-BBIS",), propre=True,\n'
                                                   '                            '
                                                   'remplacables=REMPLACABLES_PROPRES)["CODE-BBIS"]\n',
                                                   1),
                                                  ('    numéro de la ligne de GO ; une relance au plus ; échéance de la ligne de '
                                                   'GO ; relance après le samedi 21 novembre 12:00 UTC :\n'
                                                   '    nœud."""\n',
                                                   '    numéro de la ligne de GO ; une relance au plus, plus **une course** '
                                                   'accordée par GO-2026-11-16-11 (relances = 2 : feu écrit\n'
                                                   '    portant aussi ce numéro, ligne `CODE-BBIS` remplacée) ; échéance de la '
                                                   'ligne de GO ; relance après le samedi 21 novembre\n'
                                                   '    12:00 UTC : nœud."""\n',
                                                   1),
                                                  ('    if int(relances) > 1:\n'
                                                   '        raise GardeArret("une seconde relance est exclue (ligne de GO : une '
                                                   'relance au plus)")\n',
                                                   '    if int(relances) > 2:\n'
                                                   '        raise GardeArret("une troisième relance est exclue (ligne de GO : '
                                                   'une relance au plus ; GO-2026-11-16-11 : une course de "\n'
                                                   '                         "plus, une seule)")\n'
                                                   '    if int(relances) == 2 and (GO_ACCORD not in feu_ecrit\n'
                                                   '                               or cles_bbis_presentes(Path(racine) / '
                                                   'REGISTRE_PROPRE).count("CODE-BBIS") != 2):\n'
                                                   '        raise GardeArret(f"seconde relance : seulement sous le second '
                                                   'addendum (feu écrit portant {GO_ACCORD} et ligne CODE-BBIS "\n'
                                                   '                         "remplacée au registre propre) : refus")\n',
                                                   1),
                                                  ('    if int(relances) == 1 and int(maintenant) > _instant(LIMITE_RELANCE):\n',
                                                   '    if int(relances) >= 1 and int(maintenant) > _instant(LIMITE_RELANCE):\n',
                                                   1)])}
