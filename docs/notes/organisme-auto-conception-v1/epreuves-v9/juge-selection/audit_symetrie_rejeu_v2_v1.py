"""Audit de symétrie (règle R4) du rejeu à blanc des critères de sélection v2, course v9 — programme v1.

Question : l'absence, parmi les 28 cartes à 12 de l'assemblage des deux rejeux (lecteurs F et O),
de toute carte que les lignes GO attribuent à Astra, Argon ou Opus vient-elle de la famille des
lecteurs (préférence pour soi) ou d'un trait de surface (longueur, citations, champs, voie,
question, « non vérifié », style) ?

Hors ligne, processeur seul, aucun appel de modèle. numpy et bibliothèque standard.
Le champ `meta` des cartes n'est JAMAIS lu : seul `contenu` est pris, et seulement compté
(longueurs, occurrences) ; aucun texte de carte n'est imprimé ni écrit.

Les traits de surface sont déclarés ici, AVANT tout calcul (liste TRAITS) ; aucun n'a été ajouté
après lecture d'un résultat.

Usage :
  python3 -B -I audit_symetrie_rejeu_v2_v1.py SEL_F SEL_O FICHES GO_MD ESPECES_MD REEXAMEN_MD SORTIE_JSON
"""

import hashlib
import json
import re
import sys

import numpy as np

ATTENDU = {
    "sel_f": "e42b5f05d0f9b2c8423fc0d005e5d5c414c1023208e049201074ecf91ec69fc6",
    "sel_o": "8bd435b98f1b81abf3a4e201977b2b1bf9a72cbe464dfb9127243d1a93e0b7d3",
    "fiches": "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481",
    "go": "72e52540c4b25997d0aa6057ea880bdc765e0cd09c5650b65a0b084da174f558",
    "especes": "2af9e67fce5b8edb3a3cc197347ab35f08e5f1731f5dcc3b3ef11c1fc6c44beb",
    "reexamen": "de7ed04d06903c507ace3a16130fccf9f22d88e6e16143c3f8f3e0530837d063",
}

# ---------------------------------------------------------------- espèces, par les seules pièces de la mère
# (source, espèce) ; « famille des lecteurs » = Opus ou Fable (contre-lecture c75a9abc…, lecteurs déclarés
# de la même famille).
NOMMEES = {
    # GO-2026-11-19-57 (Carbon, Argon)
    "GO-57": {
        "Carbon": ["f7782e931911d", "fb45c8739b3d2", "f01d286e78e83", "f9a517d00f493", "f4250eb75fbba"],
        "Argon": ["f1c19731ccffb", "fa38f9faa24e0", "f1d7c5f2e47d7", "f6caf922edbf1", "fb9e8ae1b97b8",
                  "f5662015db5bf", "f4b85ff3c1033"],
    },
    # GO-2026-11-19-59 (Astra)
    "GO-59": {
        "Astra": ["f89c771e3ac68", "f6bb348e95955", "fec2307cbabb1", "fd81c25c080e8", "fdcf828b0dc80",
                  "fd9bbc7b19deb", "f19c4c823d67c", "fcd56a5ce3c1c", "f1675a6c453a9", "f14a90c4535dd"],
    },
    # GO-2026-11-19-61 (Astra, Opus, Fable, Carbon)
    "GO-61": {
        "Astra": ["f327b86c669cc", "fe15813583b5c"],
        "Opus": ["f232221730a16", "f562951db6c70", "f772b4c18818b"],
        "Fable": ["f76714f1ddda4", "ff60dbc7baa6f", "ff99ce570c638"],
        "Carbon": ["f91a7a590c8fe", "f0a8378953d43", "f17603c39bc32", "ff76aee57bba1", "f7cc0003c4b2c"],
    },
    # GO-2026-11-19-63, point 2 (Argon : cinq gardées, quatre non gardées)
    "GO-63": {
        "Argon": ["f5ee3a75faea3", "f71350282d0c0", "fdafe4598caad", "f38a6ed2f7434", "f68f93bac44e8",
                  "f4a47f030c829", "fcf27198b7462", "f98b6974fb1dd", "fbac0bab50a65"],
    },
    # especes-et-originalite-cartes-v9-v1.md (2af9e67f…), § (b) et § (c) : espèce écrite à côté de l'identifiant
    "especes-2af9e67f": {
        "Carbon": ["fe887ca5cb62c"],
        "Argon": ["f1373c384a771", "f7b38afebd589"],
        "Astra": ["f319823a86ea7", "f9c8c39740352", "fbae5b702558e", "f2e3582b5fa97", "f4cbf7e62ff7b"],
        "Fable": ["fcfa3d98b90f8"],
    },
}
# Déduites au niveau de la famille seulement (Opus ou Fable, sans savoir laquelle) :
# especes-2af9e67f, § (a) : porteuses des huit lignes retenues = Opus 4, Fable 2, Astra 1, Carbon 1, Argon 0 ;
# instruments transversaux = Opus 2, Fable 1. Les porteuses sont celles que GO-55 et GO-56 nomment ; l'Astra est
# f89c771e3ac68 (GO-59), la Carbon f7782e931911d (GO-57) : les six autres porteuses et les trois instruments
# sont donc Opus ou Fable.
DEDUITES_FAMILLE = {
    "porteuses GO-55": ["f169420b8d1d8", "fcc96538bff00", "fb3a2cc87251c", "f856659046065"],
    "porteuses GO-56": ["f5373a31410ab", "f8c05bffe7cb1"],
    "instruments GO-56": ["f6e7646851ba5", "fc36c3c3125ac", "fd688912a8667"],
}
# Totaux par espèce sur les 94 cartes (especes-2af9e67f, § (a), colonne « cartes »).
TOTAUX = {"Opus": 22, "Fable": 15, "Argon": 21, "Astra": 20, "Carbon": 16}
FAMILLE_LECTEURS = {"Opus", "Fable", "Opus|Fable"}

# ---------------------------------------------------------------- traits de surface, déclarés avant calcul
TRAITS = [
    "longueur_totale",          # caractères, tous les champs de `contenu`
    "longueur_refuterait",      # caractères du champ « ce qui la réfuterait »
    "champs_remplis",           # champs non vides
    "id_noeuds_N",              # occurrences de « N-ddd » (nœuds du programme, catalogue servi)
    "id_noeuds_N_distincts",
    "annees_citees",            # occurrences d'une année 19xx ou 20xx (travaux cités)
    "et_al",                    # occurrences de « et al »
    "non_verifie",              # occurrences de « non vérifi »
    "predit",                   # occurrences de « prédit » (prédit, prédite, prédits)
    "prediction",               # occurrences de « prédiction »
    "gras",                     # paires de « ** »
    "budget_egal",              # « budget égal », « à budget », « apparié »
    "pourquoi_compte",          # « pourquoi cela compte »
    "mots_par_phrase",          # mots / (signes . ; ! ? + 1)
    "suffit_refuterait",        # « suffit » dans « ce qui la réfuterait »
    "base_refuterait",          # « base » dans « ce qui la réfuterait »
    "abandon_refuterait",       # « abandon », « retir », « coup », « renonc » dans « ce qui la réfuterait »
]
CATEGORIES = ["voie_F", "strate_F", "voie_O", "strate_O", "axe"]


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def traits_de(contenu):
    # `contenu` seul ; rien n'est renvoyé que des nombres.
    vals = [str(v) for v in contenu.values()]
    t = " ".join(vals)
    tl = t.lower()
    r = str(contenu.get("ce_qui_la_refuterait", "")).lower()
    n_ph = len(re.findall(r"[.;!?]", t)) + 1
    ids_n = re.findall(r"\bN-\d{3}\b", t)
    return {
        "longueur_totale": len(t),
        "longueur_refuterait": len(r),
        "champs_remplis": sum(1 for v in vals if v.strip()),
        "id_noeuds_N": len(ids_n),
        "id_noeuds_N_distincts": len(set(ids_n)),
        "annees_citees": len(re.findall(r"\b(?:19|20)\d\d\b", t)),
        "et_al": tl.count("et al"),
        "non_verifie": tl.count("non vérifi"),
        "predit": tl.count("prédit"),
        "prediction": tl.count("prédiction"),
        "gras": t.count("**") // 2,
        "budget_egal": len(re.findall(r"budget égal|à budget|apparié", tl)),
        "pourquoi_compte": tl.count("pourquoi cela compte"),
        "mots_par_phrase": len(t.split()) / n_ph,
        "suffit_refuterait": r.count("suffit"),
        "base_refuterait": len(re.findall(r"\bbases?\b", r)),
        "abandon_refuterait": len(re.findall(r"abandon|retir|coup|renonc", r)),
    }


def r2_point(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.std() == 0 or y.std() == 0:
        return 0.0, 0.0
    r = float(np.corrcoef(x, y)[0, 1])
    return r, r * r


def eta2(cat, y):
    y = np.asarray(y, float)
    tot = ((y - y.mean()) ** 2).sum()
    if tot == 0:
        return 0.0
    b = 0.0
    for c in set(cat):
        m = np.array([ci == c for ci in cat])
        b += m.sum() * (y[m].mean() - y.mean()) ** 2
    return float(b / tot)


def perm_p(stat_fn, labels, rng, n, obs, two_sided=True):
    labels = np.asarray(labels)
    cnt = 0
    for _ in range(n):
        s = stat_fn(rng.permutation(labels))
        if (abs(s) >= abs(obs) - 1e-12) if two_sided else (s >= obs - 1e-12):
            cnt += 1
    return (cnt + 1) / (n + 1)


def ols_r2(X, y):
    X = np.column_stack([np.ones(len(y))] + [np.asarray(c, float) for c in X])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    tot = ((y - y.mean()) ** 2).sum()
    return float(1 - (res ** 2).sum() / tot), beta


def main(argv):
    p_f, p_o, p_fiches, p_go, p_esp, p_reex, p_out = argv[1:8]
    emp = {"sel_f": sha(p_f), "sel_o": sha(p_o), "fiches": sha(p_fiches), "go": sha(p_go),
           "especes": sha(p_esp), "reexamen": sha(p_reex)}
    for k, v in emp.items():
        if v != ATTENDU[k]:
            raise SystemExit(f"empreinte inattendue pour {k} : {v}")

    sel_f = json.load(open(p_f, encoding="utf-8"))
    sel_o = json.load(open(p_o, encoding="utf-8"))
    fiches = json.load(open(p_fiches, encoding="utf-8"))
    go_txt = open(p_go, encoding="utf-8").read()
    esp_txt = open(p_esp, encoding="utf-8").read()
    reex_txt = open(p_reex, encoding="utf-8").read()

    # ---- espèces : chaque identifiant doit figurer dans sa source
    espece, source = {}, {}
    lignes_go = {n: next(l for l in go_txt.splitlines() if l.startswith(f"| GO-2026-11-19-{n} "))
                 for n in ("55", "56", "57", "59", "61", "63")}
    for src, par_esp in NOMMEES.items():
        texte = lignes_go[src[3:]] if src.startswith("GO-") else esp_txt
        for e, ids in par_esp.items():
            for i in ids:
                if i not in texte:
                    raise SystemExit(f"{i} absent de {src}")
                if i in espece and espece[i] != e:
                    raise SystemExit(f"conflit d'espèce pour {i}")
                espece.setdefault(i, e)
                source.setdefault(i, src)
    for src, ids in DEDUITES_FAMILLE.items():
        texte = lignes_go[src.split("GO-")[1][:2]]
        for i in ids:
            if i not in texte:
                raise SystemExit(f"{i} absent de {src}")
            if i in espece:
                raise SystemExit(f"{i} déjà nommée")
            espece[i] = "Opus|Fable"
            source[i] = src + " (déduite, famille seulement)"
    reex_mentionne_espece = any(e in reex_txt for e in ("Astra", "Argon", "Carbon"))

    ids = sorted(fiches.keys())
    assert len(ids) == 94
    # ---- traits : `contenu` seul
    tr = {i: traits_de(fiches[i]["contenu"]) for i in ids}
    axe = {i: str(fiches[i]["contenu"].get("axe", "")) for i in ids}

    # ---- notes des deux lecteurs
    f_c = {c["id"]: c for c in sel_f["cartes"]}
    o_c = {c["id"]: c for c in sel_o["cartes_notees"]}
    assert set(f_c) == set(ids) == set(o_c)
    excl_f = {i for i, c in f_c.items() if c.get("exclue")}
    excl_o = {i for i, c in o_c.items() if c.get("excl")}
    exclues = excl_f & excl_o
    garde = [i for i in ids if i not in exclues]
    fE = {i: f_c[i]["notes"]["E"] for i in garde}
    fQ = {i: f_c[i]["notes"]["Q"] for i in garde}
    fD = {i: f_c[i]["notes"]["D"] for i in garde}
    ft = {i: f_c[i]["notes"]["total"] for i in garde}
    ot = {i: o_c[i]["total"] for i in garde}
    oD = {i: o_c[i]["D"] for i in garde}
    somme = {i: ft[i] + ot[i] for i in garde}
    distrib = {s: sum(1 for i in garde if somme[i] == s) for s in sorted(set(somme.values()), reverse=True)}
    y12 = np.array([1 if somme[i] == 12 else 0 for i in garde])
    yFD = np.array([1 if fD[i] == 2 else 0 for i in garde])
    veto_f = [x["id"] for x in sel_f["veto_lecteur_F"]["liste_ordonnee"]]
    sup_f = [x["id"] for x in sel_f["veto_lecteur_F"]["suppleantes"]]
    veto_o = [x["id"] for x in sel_o["veto_declare"]["liste"]]
    sup_o = [x["id"] if isinstance(x, dict) else x for x in sel_o["veto_declare"]["suppleantes"]]

    def fam(i):
        e = espece.get(i)
        if e is None:
            return None
        return 1 if e in FAMILLE_LECTEURS else 0

    out = {
        "piece": "audit de symétrie du rejeu à blanc des critères v2 — sortie du programme v1",
        "empreintes_entrees": emp,
        "numpy": np.__version__,
        "assemblage": {"exclues_par_les_deux": sorted(exclues), "notees": len(garde),
                       "distribution_somme": distrib},
        "couverture_espece": {},
        "tables": {},
        "permutations": {},
        "traits": {},
        "modeles": {},
        "veto": {},
    }

    # ---- couverture
    nb = {}
    for i in ids:
        nb[espece.get(i, "inconnue")] = nb.get(espece.get(i, "inconnue"), 0) + 1
    restants = {e: TOTAUX[e] - nb.get(e, 0) for e in TOTAUX}
    restants_fam = TOTAUX["Opus"] + TOTAUX["Fable"] - nb.get("Opus", 0) - nb.get("Fable", 0) - nb.get("Opus|Fable", 0)
    out["couverture_espece"] = {
        "par_espece_connue": nb,
        "nommees": sum(v for k, v in nb.items() if k not in ("inconnue", "Opus|Fable")),
        "famille_seulement_deduites": nb.get("Opus|Fable", 0),
        "inconnues": nb.get("inconnue", 0),
        "totaux_de_la_piece_2af9e67f": TOTAUX,
        "restant_parmi_les_inconnues": {"Astra": restants["Astra"], "Argon": restants["Argon"],
                                         "Carbon": restants["Carbon"], "Opus|Fable": restants_fam},
        "piece_de7ed04d_donne_une_espece_par_carte": reex_mentionne_espece,
        "sources": {i: source[i] for i in sorted(source)},
    }

    # ---- tables espèce × note
    def table(score):
        tab = {}
        for i in garde:
            e = espece.get(i, "inconnue")
            tab.setdefault(e, {})
            tab[e][score[i]] = tab[e].get(score[i], 0) + 1
        return {e: dict(sorted(v.items(), reverse=True)) for e, v in sorted(tab.items())}
    out["tables"]["espece_x_somme"] = table(somme)
    out["tables"]["espece_x_total_F"] = table(ft)
    out["tables"]["espece_x_total_O"] = table(ot)
    out["tables"]["espece_x_D_F"] = table(fD)
    out["tables"]["exclues_par_les_deux"] = {i: espece.get(i, "inconnue") for i in sorted(exclues)}

    # ---- graines (R9)
    ent = int(hashlib.sha256(b"audit-symetrie-rejeu-v2-v1").hexdigest(), 16)
    ss = np.random.SeedSequence(ent)
    enfants = ss.spawn(6)
    out["graines"] = {"entropy": str(ent), "construction": "SeedSequence(int(sha256('audit-symetrie-rejeu-v2-v1'))) ; "
                      "spawn(6) : 0 famille, 1 famille nommées, 2 strate, 3 imputation, 4 traits, 5 modèles"}
    NP = 20000

    # ---- permutation de l'étiquette de famille
    def test_famille(sous, rng, strates=None):
        f = np.array([fam(i) for i in sous])
        y = np.array([1 if somme[i] == 12 else 0 for i in sous])

        def stat(lab):
            return y[lab == 1].mean() - y[lab == 0].mean()
        obs = stat(f)
        if strates is None:
            p = perm_p(stat, f, rng, NP, obs)
        else:
            st = np.array([strates[i] for i in sous])
            cnt = 0
            for _ in range(NP):
                lab = f.copy()
                for s in set(st):
                    m = st == s
                    lab[m] = rng.permutation(lab[m])
                if abs(stat(lab)) >= abs(obs) - 1e-12:
                    cnt += 1
            p = (cnt + 1) / (NP + 1)
        return {"n": int(len(sous)), "n_famille": int(f.sum()), "n_autres": int((1 - f).sum()),
                "a_12_famille": int(y[f == 1].sum()), "a_12_autres": int(y[f == 0].sum()),
                "part_12_famille": float(y[f == 1].mean()), "part_12_autres": float(y[f == 0].mean()),
                "difference": float(obs), "p_bilateral": float(p), "permutations": NP}

    lab_all = [i for i in garde if fam(i) is not None]
    lab_nom = [i for i in garde if espece.get(i) not in (None, "Opus|Fable")]
    voie_F = {i: f_c[i]["voie"] for i in garde}
    out["permutations"]["famille_etiquetees"] = test_famille(lab_all, np.random.default_rng(enfants[0]))
    out["permutations"]["famille_nommees_seules"] = test_famille(lab_nom, np.random.default_rng(enfants[1]))
    out["permutations"]["famille_etiquetees_dans_voie_F"] = test_famille(lab_all, np.random.default_rng(enfants[2]), voie_F)

    # même test sur D du lecteur F (la seule note qui varie) et sur le total O
    def test_y(sous, yd, rng):
        f = np.array([fam(i) for i in sous])
        y = np.array([yd[i] for i in sous], float)

        def stat(lab):
            return y[lab == 1].mean() - y[lab == 0].mean()
        obs = stat(f)
        return {"moy_famille": float(y[f == 1].mean()), "moy_autres": float(y[f == 0].mean()),
                "difference": float(obs), "p_bilateral": float(perm_p(stat, f, rng, NP, obs))}
    out["permutations"]["famille_sur_total_O"] = test_y(lab_all, ot, np.random.default_rng(enfants[0].spawn(1)[0]))

    # Confusion par le mode d'étiquetage : les neuf cartes déduites sont des porteuses ou instruments de lignes
    # retenues par la proposition v1 (dont le C5 est l'ancêtre de D). Strate « dans une ligne retenue » selon
    # les seules pièces : GO-57 et GO-59 (« déjà dans les lignes retenues »), pièce 2af9e67f § (b) et (c).
    retenues_nommees = {
        "f7782e931911d", "fb45c8739b3d2", "f01d286e78e83", "f9a517d00f493", "f4250eb75fbba",   # GO-57 Carbon
        "f1c19731ccffb", "fa38f9faa24e0", "f1d7c5f2e47d7", "f6caf922edbf1", "fb9e8ae1b97b8",   # GO-57 Argon
        "f89c771e3ac68", "f6bb348e95955", "fec2307cbabb1",                                     # GO-59 Astra
        "fe887ca5cb62c", "f1373c384a771", "f7b38afebd589", "fcfa3d98b90f8",                    # 2af9e67f
    } | {i for v in DEDUITES_FAMILLE.values() for i in v}
    statut = {i: ("retenue_v1" if i in retenues_nommees else "autre") for i in garde}
    out["permutations"]["famille_dans_statut_v1"] = test_famille(lab_all, np.random.default_rng(enfants[2].spawn(1)[0]), statut)
    out["permutations"]["famille_dans_strate_F"] = test_famille(
        lab_all, np.random.default_rng(enfants[2].spawn(2)[1]),
        {i: f"{f_c[i]['voie']}-{f_c[i].get('sous_strate')}" for i in garde})
    par_statut = {}
    for i in lab_all:
        k = (statut[i], "famille" if fam(i) else "autres")
        par_statut.setdefault(k, [0, 0])
        par_statut[k][0] += 1
        par_statut[k][1] += 1 if somme[i] == 12 else 0
    out["tables"]["statut_v1_x_famille_n_et_a_12"] = {f"{a} / {b}": v for (a, b), v in sorted(par_statut.items())}
    # lignée du lecteur F (Fable, d'après sa note) : Fable contre Opus, nommées seules
    out["tables"]["fable_contre_opus_nommees_D_F"] = {
        e: {"n": sum(1 for i in garde if espece.get(i) == e),
            "D_F_2": sum(1 for i in garde if espece.get(i) == e and fD[i] == 2)} for e in ("Fable", "Opus")}

    # ---- imputation des inconnues selon les totaux de la pièce 2af9e67f
    rng = np.random.default_rng(enfants[3])
    inconnues = [i for i in garde if fam(i) is None]
    # les inconnues hors assemblage (exclues) prennent aussi une part des totaux
    inconnues_toutes = [i for i in ids if espece.get(i) is None]
    sac = ["F"] * restants_fam + ["A"] * (restants["Astra"] + restants["Argon"] + restants["Carbon"])
    assert len(sac) == len(inconnues_toutes), (len(sac), len(inconnues_toutes))
    diffs, ps, n12f = [], [], []
    yg = np.array([1 if somme[i] == 12 else 0 for i in garde])
    base = np.array([fam(i) if fam(i) is not None else -1 for i in garde])
    pos = {i: k for k, i in enumerate(garde)}
    for _ in range(400):
        tirage = rng.permutation(sac)
        lab = base.copy()
        for i, t in zip(inconnues_toutes, tirage):
            if i in pos:
                lab[pos[i]] = 1 if t == "F" else 0
        d = yg[lab == 1].mean() - yg[lab == 0].mean()
        diffs.append(d)
        n12f.append(int(yg[lab == 1].sum()))
        cnt = 0
        for _ in range(500):
            pl = rng.permutation(lab)
            if abs(yg[pl == 1].mean() - yg[pl == 0].mean()) >= abs(d) - 1e-12:
                cnt += 1
        ps.append((cnt + 1) / 501)
    inc12 = int(sum(1 for i in inconnues if somme[i] == 12))
    # bornes : les 11 inconnues hors famille placées d'abord sur les cartes à 12 (pire cas pour « famille »),
    # puis d'abord hors des 12 (meilleur cas) ; les deux exclues inconnues prennent la famille dans le pire cas.
    n_autres_inc = len(sac) - restants_fam
    exc_inc = len(inconnues_toutes) - len(inconnues)
    kf, ka = int(sum(1 for i in lab_all if fam(i) and somme[i] == 12)), int(sum(1 for i in lab_all if not fam(i) and somme[i] == 12))
    nf, na = int(sum(1 for i in lab_all if fam(i))), int(sum(1 for i in lab_all if not fam(i)))
    a12_pire = min(n_autres_inc, inc12)
    autres_notees_pire = n_autres_inc  # exclues inconnues comptées famille
    fam_notees_pire = len(inconnues) - autres_notees_pire
    pire = (kf + inc12 - a12_pire) / (nf + fam_notees_pire) - (ka + a12_pire) / (na + autres_notees_pire)
    a12_mieux = max(0, n_autres_inc - (len(inconnues) - inc12))
    autres_notees_mieux = n_autres_inc - min(exc_inc, n_autres_inc)
    a12_mieux = max(0, autres_notees_mieux - (len(inconnues) - inc12))
    fam_notees_mieux = len(inconnues) - autres_notees_mieux
    mieux = (kf + inc12 - a12_mieux) / (nf + fam_notees_mieux) - (ka + a12_mieux) / (na + autres_notees_mieux)
    from math import comb as _comb
    N_, K_ = nf + fam_notees_pire + na + autres_notees_pire, kf + ka + inc12
    n_, k_ = nf + fam_notees_pire, kf + inc12 - a12_pire
    p_pire = sum(_comb(K_, j) * _comb(N_ - K_, n_ - j) for j in range(k_, min(K_, n_) + 1)) / _comb(N_, n_)
    out["permutations"]["bornes_sur_les_inconnues"] = {
        "pire_cas_pour_famille": {"difference": pire, "p_hypergeometrique_unilateral": p_pire, "a_12_autres": ka + a12_pire, "autres_notees": na + autres_notees_pire,
                                  "a_12_famille": kf + inc12 - a12_pire, "famille_notees": nf + fam_notees_pire},
        "meilleur_cas_pour_famille": {"difference": mieux},
    }
    out["permutations"]["imputation_totaux"] = {
        "imputations": 400, "permutations_par_imputation": 500,
        "inconnues_notees": len(inconnues), "inconnues_a_12": inc12,
        "difference_min_med_max": [float(np.min(diffs)), float(np.median(diffs)), float(np.max(diffs))],
        "a_12_famille_min_med_max": [int(np.min(n12f)), int(np.median(n12f)), int(np.max(n12f))],
        "p_min_med_max": [float(np.min(ps)), float(np.median(ps)), float(np.max(ps))],
        "part_des_imputations_p_inf_0_05": float(np.mean(np.array(ps) < 0.05)),
    }

    # ---- traits de surface : part de la note expliquée
    rng = np.random.default_rng(enfants[4])
    tt = {}
    yg_f = np.array([somme[i] for i in garde], float)
    for t in TRAITS:
        x = np.array([tr[i][t] for i in garde], float)
        r, r2 = r2_point(x, y12)
        rD, r2D = r2_point(x, yFD)
        obs = r

        def stat(xx, y=y12):
            return r2_point(xx, y)[0]
        p = perm_p(stat, x, rng, 5000, obs)
        xl = np.array([tr[i][t] for i in lab_all], float)
        fl = np.array([fam(i) for i in lab_all], float)
        rf, r2f = r2_point(xl, fl)
        tt[t] = {"moy_a_12": float(x[y12 == 1].mean()), "moy_sous_12": float(x[y12 == 0].mean()),
                 "r_avec_12": r, "r2_avec_12": r2, "p_perm_r": float(p),
                 "r2_avec_D_F": r2D, "r_avec_famille_etiquetees": rf, "r2_avec_famille": r2f}
    for c in CATEGORIES:
        if c == "voie_F":
            cat = [f_c[i]["voie"] for i in garde]
        elif c == "strate_F":
            cat = [f"{f_c[i]['voie']}-{f_c[i].get('sous_strate')}" for i in garde]
        elif c == "voie_O":
            cat = [o_c[i]["voie"] for i in garde]
        elif c == "strate_O":
            cat = [str(o_c[i].get("strate")) for i in garde]
        else:
            cat = [axe[i] for i in garde]
        e2 = eta2(cat, y12)
        cnt = 0
        for _ in range(5000):
            if eta2(list(rng.permutation(cat)), y12) >= e2 - 1e-12:
                cnt += 1
        par = {}
        for k, ci in enumerate(cat):
            par.setdefault(ci, [0, 0])
            par[ci][0] += 1
            par[ci][1] += int(y12[k])
        catl = [cat[garde.index(i)] for i in lab_all]
        fl = np.array([fam(i) for i in lab_all], float)
        tt[c] = {"eta2_avec_12": e2, "p_perm": (cnt + 1) / 5001,
                 "eta2_avec_famille": eta2(catl, fl),
                 "par_modalite_n_et_a_12": {k: v for k, v in sorted(par.items())}}
    fl = np.array([fam(i) for i in lab_all], float)
    yl = np.array([1 if somme[i] == 12 else 0 for i in lab_all], float)
    tt["famille_etiquetees"] = {"r2_avec_12": r2_point(fl, yl)[1], "n": len(lab_all)}
    out["traits"] = tt

    # ---- modèles linéaires simples (probabilité linéaire) sur les cartes étiquetées
    rng = np.random.default_rng(enfants[5])
    z = {t: np.array([tr[i][t] for i in lab_all], float) for t in TRAITS}
    for t in z:
        s = z[t].std()
        z[t] = (z[t] - z[t].mean()) / s if s > 0 else z[t] * 0
    classes = sorted(TRAITS, key=lambda t: -tt[t]["r2_avec_12"])
    meilleurs = classes[:3]
    r2_fam, _ = ols_r2([fl], yl)
    r2_tr, _ = ols_r2([z[t] for t in meilleurs], yl)
    r2_tout, beta = ols_r2([fl] + [z[t] for t in meilleurs], yl)
    # Freedman-Lane : résidus du modèle réduit (traits) permutés
    Xr = np.column_stack([np.ones(len(yl))] + [z[t] for t in meilleurs])
    br, *_ = np.linalg.lstsq(Xr, yl, rcond=None)
    fit_r = Xr @ br
    res_r = yl - fit_r
    cnt = 0
    for _ in range(NP):
        yp = fit_r + rng.permutation(res_r)
        r2p, _ = ols_r2([fl] + [z[t] for t in meilleurs], yp)
        r2rp, _ = ols_r2([z[t] for t in meilleurs], yp)
        if r2p - r2rp >= (r2_tout - r2_tr) - 1e-12:
            cnt += 1
    # l'inverse : les traits ajoutés à la famille
    out["modeles"] = {
        "n": len(lab_all), "trois_traits_les_plus_lies_a_12": meilleurs,
        "r2_famille_seule": r2_fam, "r2_trois_traits": r2_tr, "r2_famille_et_traits": r2_tout,
        "gain_r2_de_la_famille_a_traits_tenus": r2_tout - r2_tr,
        "p_freedman_lane_famille": (cnt + 1) / (NP + 1),
        "gain_r2_des_traits_a_famille_tenue": r2_tout - r2_fam,
        "coef_famille_traits_tenus": float(beta[1]),
    }

    # ---- veto : espèce des cartes de veto, comparée à la base
    def esp_liste(l):
        return [{"id": i, "espece": espece.get(i, "inconnue")} for i in l]
    tous_veto = veto_f + veto_o
    conn = [i for i in tous_veto if fam(i) is not None]
    k_fam = sum(fam(i) for i in conn)
    base_lab = np.mean([fam(i) for i in ids if fam(i) is not None])
    base_tot = (TOTAUX["Opus"] + TOTAUX["Fable"]) / 94
    from math import comb
    def binom_sup(n, k, p):
        return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))
    out["veto"] = {
        "veto_F": esp_liste(veto_f), "suppleantes_F": esp_liste(sup_f),
        "veto_O": esp_liste(veto_o), "suppleantes_O": esp_liste(sup_o),
        "titulaires_d_espece_connue": len(conn), "dont_famille_des_lecteurs": int(k_fam),
        "base_famille_parmi_etiquetees": float(base_lab), "base_famille_sur_94": base_tot,
        "p_binomial_au_moins_k_base_94": binom_sup(len(conn), int(k_fam), base_tot),
        "p_binomial_au_moins_k_base_etiquetees": binom_sup(len(conn), int(k_fam), float(base_lab)),
        "inconnues_parmi_titulaires": [i for i in tous_veto if fam(i) is None],
    }
    # traits moyens des cartes à 12 par sous-groupe, pour la note
    out["traits_par_groupe"] = {}
    for g, sel in (("12", [i for i in garde if somme[i] == 12]), ("11_et_moins", [i for i in garde if somme[i] < 12])):
        out["traits_par_groupe"][g] = {t: float(np.mean([tr[i][t] for i in sel])) for t in TRAITS}
    # cartes à 12 par espèce (identifiants seulement)
    out["cartes_a_12"] = {i: espece.get(i, "inconnue") for i in garde if somme[i] == 12}

    with open(p_out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=False)
        fh.write("\n")
    print(json.dumps({k: out[k] for k in ("assemblage", "couverture_espece")}, ensure_ascii=False)[:3000])


if __name__ == "__main__":
    main(sys.argv)
