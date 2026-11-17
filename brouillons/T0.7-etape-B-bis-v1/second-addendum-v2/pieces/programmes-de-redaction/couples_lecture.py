ANCIEN_PILE = '''def reserve_pile(sondes_doc: dict) -> list[str]:
    """R-PILE (brouillon 6, qualifications toujours écrites) : écrite dès qu'une sonde finale lue est de la famille « attention »
    (sonde finale d'une source et d'un pli, `famille` du fichier fermé des sondes ; sonde finale d'ENC, réglage « attention- » ;
    interprétation déclarée : ENC est une sonde finale lue) ; les sondes concernées sont nommées."""
    lues = []
    for src, par_pli in sorted((sondes_doc.get("sources") or {}).items()):
        for ek, m in sorted(par_pli.items()):
            if "echec" in m:
                continue
            if m.get("famille") == "attention":
                lues.append(f"{src} {ek}")
            enc = m.get("enc") or {}
            if "echec" not in enc and str(enc.get("reglage", "")).startswith("attention-"):
                lues.append(f"{src} {ek} (ENC)")
    return [f"{RESERVES_FIXES['R-PILE']} (sondes « attention » lues : {', '.join(lues)})"] if lues else []
'''

NOUVEAU_PILE = '''NOMS_FAMILLES = {"lineaire": "linéaires", "attention": "« attention »"}
EPOQUES_CONTROLE_V4 = 3                 # = validation_imbriquee_v4.EPOQUES_CONTROLE (essai ; la lecture n'importe pas torch)
CHAMP_O2 = "sonde_o2"                   # = validation_imbriquee_v4.CHAMP_O2 (essai)
DISCRIMINANT = {
    "accord": ("information à 300 époques au plus 10⁻⁴ sur le couple contrôlé : carte et processeur s'accordent aussi à 300 "
               "époques sur ce couple (aucune amplification vue sur ce couple ; rien n'est dit des autres couples)"),
    "ecart": ("information à 300 époques au-dessus de 10⁻⁴, ou non finie, sur le couple contrôlé, contrôle à 3 époques passé : "
              "amplification d'arrondi ou erreur de chaîne qui ne commence qu'après la troisième époque, indiscernables par ce "
              "contrôle (réserve R-B du second addendum)"),
}


def phrase_dispersion(d: dict | None) -> str:
    """Résumé de la mesure de dispersion entre deux ordres de calcul (second addendum ; information, aucun état ne change)."""
    tete = "dispersion des aires entre deux ordres de calcul de la carte (information du second addendum, aucun état ne change)"
    if not isinstance(d, dict):
        return f"{tete} : non lue"
    if "non_faite" in d:
        return f"{tete} : mesure non faite ({d['non_faite']})"
    if not d.get("cellules_lues"):
        return f"{tete} : aucune cellule calculable"
    return (f"{tete} : écart absolu maximal {_f(d['ecart_max'])} ({d['cellule_ecart_max']}) sur {d['cellules_lues']} cellules "
            f"lues ; réglage retenu changé dans {d['plis_reglage_change']} plis sur {d['plis_compares']}")


def reserve_pile(sondes_doc: dict, dispersion: dict | None = None) -> list[str]:
    """R-PILE (second addendum, EC-2 révisé ; qualifications toujours écrites) : écrite dès qu'une sonde finale est lue, de la
    famille linéaire ou « attention » (sonde finale d'une source et d'un pli, `famille` du fichier fermé des sondes ; sonde finale
    d'ENC, famille lue au début de son réglage ; ENC est une sonde finale lue) ; les sondes lues sont nommées par famille ; la
    mesure de dispersion entre deux ordres de calcul y est résumée (`phrase_dispersion`)."""
    lues = {"lineaire": [], "attention": []}
    for src, par_pli in sorted((sondes_doc.get("sources") or {}).items()):
        for ek, m in sorted(par_pli.items()):
            if "echec" in m:
                continue
            if m.get("famille") in lues:
                lues[m["famille"]].append(f"{src} {ek}")
            enc = m.get("enc") or {}
            f = str(enc.get("reglage", "")).split("-", 1)[0]
            if "echec" not in enc and f in lues:
                lues[f].append(f"{src} {ek} (ENC)")
    if not any(lues.values()):
        return []
    noms = " ; ".join(f"{NOMS_FAMILLES[f]} : {', '.join(v)}" for f, v in lues.items() if v)
    return [f"{RESERVES_FIXES['R-PILE']} (sondes finales lues — {noms}) ; {phrase_dispersion(dispersion)}"]
'''

ANCIEN_CTRL = '''def exiger_controle_carte(sondes_doc: dict) -> dict:
    """Champ `controle_carte_processeur` du fichier fermé des sondes (marche v3) : chaque famille de la marche porte un écart
    numérique fini ≤ 10⁻⁴ ; l'attention, le déterminisme au bit près ; une trace « sans objet », un champ absent ou non numérique :
    arrêt de la lecture (`RefusLecture`). Rend les écarts lus."""
'''
NOUVEAU_CTRL = '''def exiger_controle_carte(sondes_doc: dict) -> dict:
    """Champ `controle_carte_processeur` du fichier fermé des sondes (marche v4, second addendum) : `version_controle` « v4 » ;
    chaque famille de la marche porte un écart numérique fini ≤ 10⁻⁴ **à 3 époques** et le déterminisme au bit près à 300 époques ;
    la linéaire porte l'écart à 300 époques écrit comme information (`ecart_300_information`, `decide` faux) ; une trace « sans
    objet », un champ absent ou non numérique : arrêt de la lecture (`RefusLecture`). Rend les écarts lus, l'information et la
    phrase du discriminant (réserve R-B), sans aucun effet sur un état."""
'''

ANCIEN_CTRL_FIN = '''        ecarts[f] = float(e)
    sortie = {"ecarts": ecarts, "tolerance": TOLERANCE_CARTE, "couple": [c.get("cellule"), c.get("pli")]}
    if "attention" in familles:
        d = c.get("determinisme_attention")
        if not (isinstance(d, dict) and d.get("egal_au_bit") is True):
            raise RefusLecture("contrôle carte-processeur : déterminisme de l'attention absent ou faux : arrêt de la lecture")
        sortie["determinisme_attention"] = True
    return sortie
'''
NOUVEAU_CTRL_FIN = '''        ecarts[f] = float(e)
        if c[f].get("epoques") != EPOQUES_CONTROLE_V4:
            raise RefusLecture(f"contrôle carte-processeur : horizon de « {f} » {c[f].get('epoques')!r} ≠ "
                               f"{EPOQUES_CONTROLE_V4} époques (second addendum) : arrêt de la lecture")
    if c.get("version_controle") != "v4":
        raise RefusLecture("contrôle carte-processeur : version_controle autre que « v4 » (second addendum) : arrêt de la lecture")
    sortie = {"ecarts": ecarts, "tolerance": TOLERANCE_CARTE, "couple": [c.get("cellule"), c.get("pli")],
              "epoques": EPOQUES_CONTROLE_V4, "version_controle": "v4", "determinisme": {}}
    for f in familles:
        d = c.get(f"determinisme_{f}")
        if not (isinstance(d, dict) and d.get("egal_au_bit") is True):
            nom = "de l'attention" if f == "attention" else "de la linéaire"
            raise RefusLecture(f"contrôle carte-processeur : déterminisme {nom} absent ou faux : arrêt de la lecture")
        sortie["determinisme"][f] = True
    if "attention" in familles:
        sortie["determinisme_attention"] = True
    info = c["lineaire"].get("ecart_300_information")
    if not (isinstance(info, dict) and info.get("decide") is False
            and ("refus" in info or isinstance(info.get("ecart_relatif_max"), (int, float)))
            and not isinstance(info.get("ecart_relatif_max"), bool)):
        raise RefusLecture("contrôle carte-processeur : information à 300 époques de la linéaire absente ou mal formée : arrêt "
                           "de la lecture")
    e300 = info.get("ecart_relatif_max")
    accord = "refus" not in info and np.isfinite(float(e300)) and float(e300) <= TOLERANCE_CARTE
    sortie["information_300"] = info
    sortie["discriminant"] = DISCRIMINANT["accord" if accord else "ecart"]
    return sortie
'''

ANCIEN_LIRE = '''def lire_lignes(registre: Path, cles, exigees, propre: bool) -> dict:
    """Lignes `| clé | date | chemin | sha256 |` des clés demandées (une exactement pour chaque clé présente ; exigée absente →
    refus) ; registre propre : toute autre clé de forme valide → refus (seules les clés de B bis y sont permises)."""
'''
NOUVEAU_LIRE = '''def lire_lignes(registre: Path, cles, exigees, propre: bool, remplacables=()) -> dict:
    """Lignes `| clé | date | chemin | sha256 |` des clés demandées (une exactement pour chaque clé présente ; exigée absente →
    refus) ; registre propre : toute autre clé de forme valide → refus (seules les clés de B bis y sont permises). Second
    addendum : une clé de `remplacables` (`REMPLACABLES_PROPRES` : `CODE-BBIS` seulement) peut porter **deux** lignes, la seconde
    strictement postérieure, qui fait foi (« ligne `CODE-BBIS` remplacée une seule fois », liste d'arrêt) ; la première est rendue
    sous `remplace` ; trois lignes ou plus, ou une seconde ligne non postérieure : refus."""
'''

ANCIEN_BOUCLE = '''        if len(ls) != 1 or len(ls[0]) != 4 or not rg.DATE.fullmatch(ls[0][1]) or not rg.SHA.fullmatch(ls[0][3]):
            fautes.append(f"ligne {k} en double ou mal formée")
            continue
        _, date, chemin, sha = ls[0]
        if chemin.startswith("/") or ".." in Path(chemin).parts:
            fautes.append(f"ligne {k} : chemin {chemin!r}")
            continue
        sortie[k] = {"date": date, "instant": rg.instant_utc(date), "chemin": chemin, "sha256": sha}
'''
NOUVEAU_BOUCLE = '''        permis = 2 if k in tuple(remplacables) else 1
        if (len(ls) > permis or any(len(l) != 4 or not rg.DATE.fullmatch(l[1]) or not rg.SHA.fullmatch(l[3]) for l in ls)):
            fautes.append(f"ligne {k} en double ou mal formée")
            continue
        mauvais = [l[2] for l in ls if l[2].startswith("/") or ".." in Path(l[2]).parts]
        if mauvais:
            fautes.append(f"ligne {k} : chemin {mauvais[0]!r}")
            continue
        lus = [{"date": d, "instant": rg.instant_utc(d), "chemin": ch, "sha256": s} for _, d, ch, s in ls]
        if len(lus) == 2 and not lus[0]["instant"] < lus[1]["instant"]:
            fautes.append(f"ligne {k} remplacée : la seconde ligne n'est pas strictement postérieure à la première")
            continue
        sortie[k] = {**lus[1], "remplace": lus[0]} if len(lus) == 2 else lus[0]
'''

ANCIEN_ORDRE = '''def exiger_ordre_propre(lignes: dict) -> None:
    for a, b in zip(ORDRE_PROPRE, ORDRE_PROPRE[1:]):
        if a in lignes and b in lignes and not lignes[a]["instant"] < lignes[b]["instant"]:
            raise RefusLecture(f"ligne {a} ({lignes[a]['date']}) pas strictement antérieure à {b} ({lignes[b]['date']})")
'''
NOUVEAU_ORDRE = '''def exiger_ordre_propre(lignes: dict) -> None:
    """Ordre du plan, point 2 ; second addendum : une ligne `CODE-BBIS` remplacée se lit SCELLEMENT-BBIS < CODE-BBIS (première)
    < GO-BBIS < CODE-BBIS (remplacement) < SCORES-BBIS."""
    lignes, chaine = dict(lignes), list(ORDRE_PROPRE)
    if "CODE-BBIS" in lignes and "remplace" in lignes["CODE-BBIS"]:
        lignes["CODE-BBIS (première)"] = lignes["CODE-BBIS"]["remplace"]
        chaine = ["SCELLEMENT-BBIS", "CODE-BBIS (première)", "GO-BBIS", "CODE-BBIS", "SCORES-BBIS"]
    for a, b in zip(chaine, chaine[1:]):
        if a in lignes and b in lignes and not lignes[a]["instant"] < lignes[b]["instant"]:
            raise RefusLecture(f"ligne {a} ({lignes[a]['date']}) pas strictement antérieure à {b} ({lignes[b]['date']})")
'''

ANCIEN_DISP = '''def _essai(f, *a, **k):
'''
NOUVEAU_DISP = '''def dispersion_ordres(asms: dict, specs: dict, sondes_doc: dict) -> dict:
    """Mesure d'information du second addendum (MD) : pour chaque cellule (plafond et transfert), aire du jeu décisif (O[positifs]
    contre O[H], tâches du pli lu, moyenne des deux plis) par la sonde lue (ordre 1) et par la sonde de l'ordre 2 de la même source
    (`<groupe>__sonde_o2`) ; différence (ordre 2 − ordre 1), aires par pli, réglages retenus des deux ordres par pli ; résumé :
    écart absolu maximal, plis dont le réglage retenu change. Aucun intervalle, aucun état, aucun seuil ; rien d'autre ne change."""
    d = sondes_doc.get("dispersion_ordres_calcul")
    if not isinstance(d, dict):
        return {"non_faite": "champ dispersion_ordres_calcul absent du fichier des sondes", "decide": False}
    if "non_faite" in d:
        return {"non_faite": str(d["non_faite"]), "ordre": d.get("ordre"), "decide": False}
    sortie = {}
    for nom, spec in {**specs["plafond"], **specs["transfert"]}.items():
        src = spec.get("source") or nom
        meta = (sondes_doc.get("sources") or {}).get(src, {})
        reglages = {ek: {"ordre1": m.get("reglage"), "ordre2": (m.get("ordre2") or {}).get("reglage")}
                    for ek, m in sorted(meta.items())}
        if src not in asms:
            sortie[nom] = {"source": src, "non_calculable": "source non lisible", "reglages": reglages}
            continue
        dp, dn = f"O-{spec['positifs']}", f"O-{H}"
        j1, m1 = _essai(asms[src].jeu, dp, dn, "sonde")
        j2, m2 = _essai(asms[src].jeu, dp, dn, CHAMP_O2)
        if j1 is None or j2 is None:
            sortie[nom] = {"source": src, "non_calculable": m1 or m2, "reglages": reglages}
            continue
        a1, a2 = j1.aires_plis[:, 0], j2.aires_plis[:, 0]
        sortie[nom] = {"source": src, "aire_ordre1": float(a1.mean()), "aire_ordre2": float(a2.mean()),
                       "difference": float(a2.mean() - a1.mean()),
                       "par_pli": {f"e{k}": {"aire_ordre1": float(a1[k]), "aire_ordre2": float(a2[k])} for k in range(len(a1))},
                       "reglages": reglages}
    lues = sorted(((abs(c["difference"]), n) for n, c in sortie.items() if "difference" in c), reverse=True)
    compares = [(m.get("reglage"), m["ordre2"]["reglage"]) for par in (sondes_doc.get("sources") or {}).values()
                for m in par.values() if "echec" not in m and isinstance(m.get("ordre2"), dict) and m["ordre2"].get("reglage")
                and "echec" not in m["ordre2"]]
    return {"ordre": d.get("ordre"), "decide": False, "cellules": sortie, "cellules_lues": len(lues),
            "ecart_max": lues[0][0] if lues else None, "cellule_ecart_max": lues[0][1] if lues else None,
            "plis_compares": len(compares), "plis_reglage_change": sum(1 for a, b in compares if a != b)}


def _essai(f, *a, **k):
'''

COUPLES = {"src/controle_ia/t07bbis/lecture_v3.py": [
    ('''10 ; « Critères de lecture gelés » A, B, D ; « Seuil » ; « Liste d'arrêt »), v2 : la v1, plus la réserve **R-PILE** (règle et
phrase du brouillon 6 : écrite dès qu'une sonde finale lue est de la famille « attention »), le point (7) de la section D, et la
lecture du champ `controle_carte_processeur` du fichier fermé des sondes (marche v3 : un écart numérique ≤ 10⁻⁴ par famille, le
déterminisme de l'attention au bit près ; une trace « sans objet », un champ absent ou non numérique arrête la lecture) ; majeur M1
de `contre-lecture-brouillon5-et-code-v2-v1.md`, R-2919 ; la v1 reste (R12).
''',
     '''10 ; « Critères de lecture gelés » A, B, D ; « Seuil » ; « Liste d'arrêt »), v3 : la v2, modifiée par le **second addendum
d'écart** (`brouillon-second-addendum-bbis-v1.md`) : réserve **R-PILE étendue à la linéaire** (écrite dès qu'une sonde finale lue,
linéaire ou « attention », source ou ENC, l'est) et portant le résumé de la **mesure de dispersion entre deux ordres de calcul**
(`dispersion_ordres`, information seulement, aucun état ne change) ; point (7) de la section D réécrit ; lecture du champ
`controle_carte_processeur` de la marche v4 (version « v4 », écart ≤ 10⁻⁴ à 3 époques par famille, déterminisme au bit près de
chaque famille, information à 300 époques de la linéaire, phrase du discriminant) ; ligne `CODE-BBIS` remplacée une seule fois
lue au registre propre (`lire_lignes`, `exiger_ordre_propre`) ; les v1 et v2 restent (R12).
''', 1),
    ('''posée par `scripts/amorce_bbis_v3.sh`), liste blanche des entrées''',
     '''posée par `scripts/amorce_bbis_v4.sh`), liste blanche des entrées''', 1),
    ('''    "R-PILE": ("R-PILE : sonde « attention » reproductible au bit près sur la même pile de calcul seulement (carte, pilote, versions "
               "de torch et de numpy) ; sur une autre pile, l'apprentissage peut rendre une autre sonde, surtout quand elle "
               "n'apprend rien"),
''',
     '''    "R-PILE": ("R-PILE : sonde finale (linéaire ou « attention ») reproductible au bit près sur la même pile de calcul seulement "
               "(carte, pilote, versions de torch et de numpy) ; sur une autre pile ou dans un autre ordre de calcul, l'apprentissage "
               "peut rendre une autre sonde, surtout quand elle ajuste mal, et le réglage retenu peut changer (ex aequo à 0,005)"),
''', 1),
    ('''             "(7) une aire de la famille « attention » est celle d'une sonde parmi celles que rendrait le même apprentissage sous "
             "d'autres arrondis (réserve R-PILE) : sur données synthétiques, la dispersion est négligeable quand la sonde apprend "
             "un signal, de l'ordre de 0,007 quand elle n'apprend rien ; sur de vraies activations, elle n'est pas mesurée.")
''',
     '''             "(7) une aire de sonde, linéaire ou « attention », est celle d'une sonde parmi celles que rendrait le même apprentissage "
             "sous d'autres arrondis (réserve R-PILE) : sur données fabriquées, la dispersion va de négligeable, quand la sonde "
             "apprend un signal, à plusieurs centièmes quand elle ajuste mal (0,007 à 0,047 entre deux ordres de calcul) ; sur les "
             "vraies activations, elle est mesurée entre deux ordres de calcul de la carte, comme information seulement "
             "(« dispersion entre ordres de calcul ») ; elle n'est pas mesurée entre la carte et une autre pile.")
''', 1),
    (ANCIEN_PILE, NOUVEAU_PILE, 1),
    (ANCIEN_CTRL, NOUVEAU_CTRL, 1),
    (ANCIEN_CTRL_FIN, NOUVEAU_CTRL_FIN, 1),
    ('''ORDRE_PROPRE = ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS", "SCORES-BBIS")
''', '''ORDRE_PROPRE = ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS", "SCORES-BBIS")
REMPLACABLES_PROPRES = ("CODE-BBIS",)
''', 1),
    (ANCIEN_LIRE, NOUVEAU_LIRE, 1),
    (ANCIEN_BOUCLE, NOUVEAU_BOUCLE, 1),
    (ANCIEN_ORDRE, NOUVEAU_ORDRE, 1),
    (ANCIEN_DISP, NOUVEAU_DISP, 1),
    ('''        propres = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, EXIGEES_PROPRES_LECTURE, propre=True)
''', '''        propres = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, EXIGEES_PROPRES_LECTURE, propre=True,
                              remplacables=REMPLACABLES_PROPRES)
''', 1),
    ('''    res["issue"] = (issue_complete({}, {}, None, motif_i0="marche sans scores") if not tabs
                    else issue_complete(p_ii, t_ii, marque))
''', '''    res["issue"] = (issue_complete({}, {}, None, motif_i0="marche sans scores") if not tabs
                    else issue_complete(p_ii, t_ii, marque))
    res["dispersion_ordres_calcul"] = dispersion_ordres(asms, specs, sondes_doc)
''', 1),
    ('''    reserves += reserve_pile(sondes_doc)
''', '''    reserves += reserve_pile(sondes_doc, res["dispersion_ordres_calcul"])
''', 1),
    ('''                                  commande="python -m controle_ia.t07bbis.lecture_v2")
''', '''                                  commande="python -m controle_ia.t07bbis.lecture_v3")
''', 1),
    ('''    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v2 --racine
''', '''    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v3 --racine
''', 1),
    ('''        propres = lire_lignes(racine / REGISTRE_PROPRE, ("CODE-BBIS",), ("CODE-BBIS",), propre=False)
''', '''        propres = lire_lignes(racine / REGISTRE_PROPRE, ("CODE-BBIS",), ("CODE-BBIS",), propre=False,
                              remplacables=REMPLACABLES_PROPRES)
''', 1),
]}
