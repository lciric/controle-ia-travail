# ------------------------------------------------------------------------------------------------ tables synthétiques

def noms_sondes(n_plancher=N_PLANCHER):
    noms = [PRINCIPALES["tromperie"], PRINCIPALES["enjeux"], "tromperie-lineaire-c15"]
    for c in ("tromperie", "enjeux"):
        noms += [f"{PRINCIPALES[c]}-plancher-plancher-{k}" for k in range(n_plancher)]
    return noms


def source_synthetique(effet_d=1.5, effet_b=0.0, bruit_d=0.0, plancher_signal=0.0, signes="alternes", m5=3.0,
                       m5_enjeux=3.0, exclues=0, h_egale_d=False, graine=0, n_taches=N_TACHES, pas=T, n_plancher=N_PLANCHER):
    """Run source chargé et complet, construit à la main. Scores par action et par sonde : une base commune aux cinq
    bras (même action, mêmes jetons) ; D = base + `effet_d` sur les deux sondes principales (+ bruit) ; B = base +
    `effet_b` sur la sonde de tromperie ; H, B′ = base. Planchers : `plancher_signal` ajouté aux directions sur les lignes
    de D (signe alterné ou toujours positif). Validation : 20 groupes de deux exemples par concept."""
    rng = np.random.default_rng(graine)
    noms = noms_sondes(n_plancher)
    jt, je = noms.index(PRINCIPALES["tromperie"]), noms.index(PRINCIPALES["enjeux"])
    pl = {c: [noms.index(f"{PRINCIPALES[c]}-plancher-plancher-{k}") for k in range(n_plancher)] for c in PRINCIPALES}
    taches = [f"t{k:02d}" for k in range(n_taches)]
    n = n_taches * pas
    base = rng.standard_normal((n, len(noms)))
    signe = np.array([1.0 if (signes == "positifs" or k % 2 == 0) else -1.0 for k in range(n_plancher)])
    par_bras = {}
    for bras in ip.BRAS:
        S = base.copy()
        if bras == "D":
            S[:, [jt, je]] += effet_d + bruit_d * rng.standard_normal((n, 2))
            for c in PRINCIPALES:
                S[:, pl[c]] += plancher_signal * signe + bruit_d * rng.standard_normal((n, n_plancher))
        if bras == "B":
            S[:, jt] += effet_b
        par_bras[bras] = S
    if h_egale_d:
        par_bras["H"] = par_bras["D"].copy()
    lignes = [(b, t, k) for b in ip.BRAS for t in taches for k in range(pas)]
    scores = np.concatenate([par_bras[b] for b in ip.BRAS])
    tables = {"noms_sondes": np.array(noms), "scores": scores, "bras": np.array([x[0] for x in lignes]),
              "episode": np.array([f"{x[0]}/{x[1]}/e0" for x in lignes]), "tache": np.array([x[1] for x in lignes]),
              "pas": np.array([x[2] for x in lignes], dtype=np.int64),
              "jetons": np.array([31] * len(lignes), dtype=np.int64), "jetons_notes": np.array([30] * len(lignes), dtype=np.int64)}
    longueur = 3
    jetons = {"principales": np.array([PRINCIPALES["tromperie"], PRINCIPALES["enjeux"]]),
              "rang": np.arange(len(lignes), dtype=np.int64), "longueur": np.full(len(lignes), longueur, dtype=np.int64),
              "debut": np.arange(len(lignes), dtype=np.int64) * longueur}
    for k, j in enumerate((jt, je)):
        jetons[f"scores_{k}"] = np.concatenate([[s - 1.0, s, s - 0.5] for s in scores[:, j]])
    vy, vg, vc, vs = [], [], [], []
    for c, signal in (("tromperie", m5), ("enjeux", m5_enjeux)):
        for g in range(20):
            for y in (0, 1):
                ligne = rng.standard_normal(len(noms))
                ligne[noms.index(PRINCIPALES[c])] += signal * y
                vy.append(y), vg.append(f"{'fait' if c == 'tromperie' else 'paire'}-{g}"), vc.append(c), vs.append(ligne)
    validation = {"noms_sondes": np.array(noms), "scores": np.array(vs), "concept": np.array(vc), "y": np.array(vy),
                  "groupe": np.array(vg)}
    actions = [{"tache": t, "pas": k, "gardee": True, "motif": None} for t in taches for k in range(pas)]
    for x in actions[:exclues]:
        x.update(gardee=False, motif="scores")
    ident = {"taches": taches, "actions": actions, "total": n, "exclues": exclues,
             "exclusions_par_motif": {"longueur": 0, "bornes": 0, "scores": exclues, "niveau 2 désactivé": 0},
             "episodes_niveau_1": n_taches, "actions_niveau_2": 0, "niveau_2_actif": True, "reserve_tolerance_c": False,
             "reserve_scores_non_reproduits": False, "ecarts_par_sonde": {}, "ecarts_au_dela_niveau_1": 0,
             "epreuve": {"conforme": True}, "alignement": {b: {"conforme": True} for b in ip.PERSONAS},
             "longueurs_phrases": {"seules": {"D": 14, "H": 14, "B": 14, "Bprime": 14}}}
    resume = {"principales": dict(PRINCIPALES),
              "planchers": {c: [f"{PRINCIPALES[c]}-plancher-plancher-{k}" for k in range(n_plancher)] for c in PRINCIPALES}}
    return {"etat": "complet", "config": dict(CFG, T=pas), "resume": resume, "identite": ident,
            "tables": {"scores": tables, "jetons_principales": jetons, "validation": validation}}


def desaligner(source, bras):
    """Artefact : une ligne du bras n'a plus la longueur notée du bras I (alignement rompu)."""
    t = source["tables"]["scores"]
    r = int(np.flatnonzero(t["bras"] == bras)[0])
    t["jetons_notes"] = t["jetons_notes"].copy()
    t["jetons_notes"][r] += 1
    return source


