"""Contrôle de non-régression « aucune règle sur l'identifiant ni sur l'ordre ne prédit la vérité » — v2.

Remplace la v1 (`construction-v2/verifier_identifiants_opaques_v1.py`) sur la contre-lecture
`CONTRE-LECTURE-banque-v2-v1.md` (BC1-03, BC1-08) : refus dès qu'**une** case (famille × part) dépasse son seuil ; seuils
**calibrés par tirages au hasard** ; règles de **rang dans la part** ; recalcul des identifiants depuis la clé. Ce n'est
qu'un test de non-régression de la construction : la garantie vient du tirage uniforme et du secret de la clé, qu'aucune
règle ne peut voir.

Règles, par famille :
- **transférées** (apprises sur `train`, où l'organisme voit identifiant et vérité, notées sur `test` et `test_final`) :
  les 50 de la v1 — suffixes de 1 à 3 caractères, préfixes de 1 à 6, caractère à chaque position, longueur, segments,
  numéro modulo 2 à 10, numéro à seuil ;
- **dans la part** (apprises et notées dans la même part, train compris) : rang dans l'ordre du fichier et rang du numéro
  de l'identifiant, chacun à seuil (seuil et sens au mieux), pair ou impair, modulo 3 et 4.
Statistique d'une case : le maximum des exactitudes équilibrées de ses règles. Seuil d'une case : le quantile 0,995 du
même maximum sur 2 000 banques tirées comme le constructeur (identifiants permutés au hasard, parts triées par
identifiant), graine de calibration fixe (`SeedSequence(20261025)`), arrondi au centième supérieur. Refus si une case
atteint son seuil.

Usage : python3 -I verifier_identifiants_opaques_v2.py BANQUE [--v1 BANQUE_V1 --secret-v1 SECRET_V1 --secret SECRET
         --cle CLE] [--racine DOSSIER] [--tirages N]
Code de sortie : 0 aucune case au seuil ; 1 au moins une ; 2 erreur de forme ou d'équivalence. N'imprime jamais la clé.
"""
import hashlib
import json
import pathlib
import re
import sys

import numpy as np

PARTS = ("train", "test", "test_final")
NOTEES = ("test", "test_final")
QUANTILE = 0.995
GRAINE_CALIBRATION = 20261025


def ee(pred, vrai, pos) -> float:
    pred, vrai = np.asarray(pred), np.asarray(vrai)
    p = vrai == pos
    sens = float((pred[p] == pos).mean()) if p.any() else 0.0
    spec = float((pred[~p] != pos).mean()) if (~p).any() else 0.0
    return (sens + spec) / 2


def nombre(s: str):
    d = "".join(ch for ch in s if ch.isdigit())
    return int(d) if d else -1


def cat_traits(s: str) -> dict:
    f = {f"suffixe_{k}": s[-k:] for k in (1, 2, 3)}
    f.update({f"prefixe_{k}": s[:k] for k in range(1, 7)})
    f.update({f"caractere_{i:02d}": (s[i] if i < len(s) else "") for i in range(24)})
    f["longueur"] = len(s)
    seg = s.split("-")
    f["segment_premier"], f["segment_dernier"] = seg[0], seg[-1]
    f.update({f"segment_{j}": (seg[j] if j < len(seg) else "") for j in range(4)})
    n = nombre(s)
    f.update({f"nombre_mod_{m}": n % m for m in range(2, 11)})
    return f


def regle_cat(valeurs, verites, etiquettes):
    compte = {}
    for v, y in zip(valeurs, verites):
        compte.setdefault(v, {e: 0 for e in etiquettes})[y] += 1
    tot = {e: list(verites).count(e) for e in etiquettes}
    defaut = max(etiquettes, key=lambda e: (tot[e], -etiquettes.index(e)))
    r = {v: max(etiquettes, key=lambda e: (c[e], -etiquettes.index(e))) for v, c in compte.items()}
    return lambda v: r.get(v, defaut)


def meilleur_seuil(valeurs, verites, pos, neg):
    """Seuil et sens au mieux sur (valeurs, vérités) ; rend la règle et son exactitude équilibrée."""
    v = np.asarray(valeurs, dtype=float)
    vs = np.unique(v)
    cands = np.concatenate([[vs[0] - 0.5], (vs[:-1] + vs[1:]) / 2, [vs[-1] + 0.5]])
    best = (-1.0, None)
    for s in cands:
        for sens in (1, -1):
            pred = np.where((v - s) * sens > 0, pos, neg)
            x = ee(pred, verites, pos)
            if x > best[0]:
                best = (x, (s, sens))
    s, sens = best[1]
    return (lambda w: np.where((np.asarray(w, dtype=float) - s) * sens > 0, pos, neg)), best[0]


def statistiques(b: dict, detail: bool = False) -> dict:
    """Maximum des exactitudes équilibrées par case (famille × part notée pour les règles transférées ; famille × part,
    train compris, pour les règles dans la part)."""
    out = {}
    for fam in sorted({t["famille"] for t in b["train"]}):
        et = list(next(t["etiquettes"] for t in b["train"] if t["famille"] == fam))
        pos, neg = et[0], et[1]
        parts = {p: [t for t in b[p] if t["famille"] == fam] for p in PARTS}
        tr = parts["train"]
        cats_tr = [cat_traits(t["id"]) for t in tr]
        ytr = [t["verite"] for t in tr]
        res = {p: [] for p in NOTEES}
        for nom in sorted(cats_tr[0]):
            r = regle_cat([c[nom] for c in cats_tr], ytr, et)
            for p in NOTEES:
                res[p].append((ee([r(cat_traits(t["id"])[nom]) for t in parts[p]], [t["verite"] for t in parts[p]], pos), "transférée " + nom))
        r, _ = meilleur_seuil([nombre(t["id"]) for t in tr], ytr, pos, neg)
        for p in NOTEES:
            res[p].append((ee(r([nombre(t["id"]) for t in parts[p]]), [t["verite"] for t in parts[p]], pos), "transférée nombre à seuil"))
        dans = {}
        for p in PARTS:
            te = parts[p]
            y = [t["verite"] for t in te]
            rang_fichier = np.arange(len(te))
            rang_numero = np.argsort(np.argsort([nombre(t["id"]) for t in te], kind="stable"), kind="stable")
            liste = []
            for nom_r, rg in (("rang dans le fichier", rang_fichier), ("rang du numéro", rang_numero)):
                _, x = meilleur_seuil(rg, y, pos, neg)
                liste.append((x, f"dans la part : {nom_r} à seuil"))
                for m in (2, 3, 4):
                    rr = regle_cat(list(rg % m), y, et)
                    liste.append((ee([rr(v) for v in rg % m], y, pos), f"dans la part : {nom_r} modulo {m}"))
            dans[p] = liste
        cases = {}
        for p in NOTEES:
            tout = res[p] + dans[p]
            cases[p] = max(tout)
        cases["train"] = max(dans["train"])
        out[fam] = {p: {"max": round(float(cases[p][0]), 4), "regle": cases[p][1]} for p in PARTS}
        if detail:
            out[fam]["meilleures"] = {p: sorted(res.get(p, []) + dans[p], reverse=True)[:3] for p in PARTS}
    return out


def calibrer(b: dict, tirages: int) -> dict:
    """Seuils par case : quantile QUANTILE du maximum sur des banques tirées comme le constructeur (mêmes tâches, mêmes
    parts ; identifiants t-0001… permutés au hasard ; parts triées par identifiant)."""
    rng = np.random.default_rng(np.random.SeedSequence(GRAINE_CALIBRATION))
    # ordre canonique (part, famille, vérité, empreinte du texte) : les seuils ne dépendent que de la composition
    taches = sorted(((p, t) for p in PARTS for t in b[p]), key=lambda x: (PARTS.index(x[0]), x[1]["famille"], x[1]["verite"], hashlib.sha256(x[1]["texte"].encode("utf-8")).hexdigest()))
    n = len(taches)
    maxima = {}
    for _ in range(tirages):
        perm = rng.permutation(n)
        bb = {p: [] for p in PARTS}
        for i, (p, t) in enumerate(taches):
            bb[p].append({**t, "id": f"t-{int(perm[i]) + 1:04d}"})
        for p in PARTS:
            bb[p].sort(key=lambda x: x["id"])
        for fam, cases in statistiques(bb).items():
            for p, c in cases.items():
                maxima.setdefault((fam, p), []).append(c["max"])
    seuils = {}
    for (fam, p), xs in maxima.items():
        q = float(np.quantile(xs, QUANTILE))
        seuils.setdefault(fam, {})[p] = {"seuil": float(min(1.0, np.ceil(q * 100) / 100)), "quantile": round(q, 4),
                                         "mediane": round(float(np.median(xs)), 4)}
    return seuils


def composition(b: dict) -> str:
    """Empreinte de la composition (part, famille, vérité, empreinte du texte), indépendante des identifiants et de l'ordre."""
    lignes = sorted(f"{p}|{t['famille']}|{t['verite']}|{hashlib.sha256(t['texte'].encode('utf-8')).hexdigest()}" for p in PARTS for t in b[p])
    return hashlib.sha256("\n".join(lignes).encode("utf-8")).hexdigest()


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def principal(argv: list[str]) -> int:
    args = list(argv)
    opts = {}
    for cle in ("--v1", "--secret-v1", "--secret", "--cle", "--racine", "--tirages", "--seuils"):
        if cle in args:
            i = args.index(cle)
            opts[cle] = args[i + 1]
            del args[i:i + 2]
    if len(args) != 1:
        print(__doc__)
        return 2
    p = pathlib.Path(args[0])
    b = json.loads(p.read_text(encoding="utf-8"))
    tirages = int(opts.get("--tirages", 2000))
    rapport = {"banque": p.name, "sha256": sha(p), "quantile": QUANTILE, "tirages": tirages,
               "graine_calibration": GRAINE_CALIBRATION}
    ids = [t["id"] for part in PARTS for t in b[part]]
    erreurs = []
    if len(set(ids)) != len(ids):
        erreurs.append("identifiants en double")
    rapport["formes"] = sorted({re.sub(r"\d", "9", re.sub(r"[a-z]", "a", i)) for i in ids})[:6]
    stats = statistiques(b)
    rapport["composition"] = composition(b)
    if "--seuils" in opts:  # seuils d'un rapport antérieur, à composition égale (essais)
        anterieur = json.loads(pathlib.Path(opts["--seuils"]).read_text(encoding="utf-8"))
        if anterieur.get("composition") != rapport["composition"]:
            print("refus : --seuils d'une autre composition"); return 2
        seuils = {}
        for c in anterieur["cases"]:
            seuils.setdefault(c["famille"], {})[c["part"]] = {"seuil": c["seuil"], "quantile": c["quantile_hasard"], "mediane": c["mediane_hasard"]}
        rapport["seuils_repris_de"] = {"fichier": pathlib.Path(opts["--seuils"]).name, "sha256": sha(pathlib.Path(opts["--seuils"])), "tirages": anterieur.get("tirages")}
        rapport["tirages"] = anterieur.get("tirages")
    else:
        seuils = calibrer(b, tirages)
    cases = []
    for fam in stats:
        for part in PARTS:
            s, c = seuils[fam][part]["seuil"], stats[fam][part]
            cases.append({"famille": fam, "part": part, "max": c["max"], "regle": c["regle"], "seuil": round(s, 2),
                          "quantile_hasard": seuils[fam][part]["quantile"], "mediane_hasard": seuils[fam][part]["mediane"],
                          "au_seuil": bool(c["max"] >= s - 1e-12)})
    rapport["cases"] = cases
    if all(k in opts for k in ("--v1", "--secret-v1", "--secret")):
        v1 = json.loads(pathlib.Path(opts["--v1"]).read_text(encoding="utf-8"))
        s1 = json.loads(pathlib.Path(opts["--secret-v1"]).read_text(encoding="utf-8"))
        s2 = json.loads(pathlib.Path(opts["--secret"]).read_text(encoding="utf-8"))
        par_v1 = {t["id"]: (part, t) for part in PARTS for t in v1[part]}
        for part in PARTS:
            if len(b[part]) != len(v1[part]):
                erreurs.append(f"{part} : {len(b[part])} tâches au lieu de {len(v1[part])}")
            for t in b[part]:
                d = dict(s2.get(t["id"], {}))
                ancien = d.pop("id_v1", None)
                if ancien not in par_v1:
                    erreurs.append(f"{t['id']} : id_v1 absent ou inconnu"); continue
                p1, t1 = par_v1[ancien]
                if p1 != part:
                    erreurs.append(f"{t['id']} : part {part} au lieu de {p1}")
                for k in ("famille", "texte", "etiquettes", "verite", "source"):
                    if t.get(k) != t1.get(k):
                        erreurs.append(f"{t['id']} : champ {k} différent de la v1 ({ancien})")
                if sorted(t) != sorted(t1):
                    erreurs.append(f"{t['id']} : champs {sorted(t)} au lieu de {sorted(t1)}")
                if d != s1.get(ancien):
                    erreurs.append(f"{t['id']} : dossier secret différent de celui de {ancien}")
            if [t["id"] for t in b[part]] != sorted(t["id"] for t in b[part]):
                erreurs.append(f"{part} : part non triée par identifiant")
        if set(s2) != set(ids):
            erreurs.append("le secret ne couvre pas exactement les tâches de la banque")
        if set(ids) & set(par_v1):
            erreurs.append("identifiants communs avec la v1")
        eq = {"v1_sha256": sha(pathlib.Path(opts["--v1"])), "secret_sha256": sha(pathlib.Path(opts["--secret"]))}
        if "--cle" in opts:
            cle = json.loads(pathlib.Path(opts["--cle"]).read_text(encoding="utf-8"))
            e = int(cle["entropie_seed_sequence"])
            eq["cle_sha256"] = sha(pathlib.Path(opts["--cle"]))
            if hashlib.sha256(str(e).encode("ascii")).hexdigest() != (b["manifeste"].get("identifiants_opaques") or {}).get("entropie_sha256"):
                erreurs.append("empreinte de la clé différente de celle du manifeste")
            ordre_v1 = [t["id"] for part in PARTS for t in v1[part]]
            perm = np.random.default_rng(np.random.SeedSequence(e)).permutation(len(ordre_v1))
            attendu = {f"t-{int(perm[i]) + 1:04d}": ordre_v1[i] for i in range(len(ordre_v1))}
            recalcule = {k: v.get("id_v1") for k, v in s2.items()}
            eq["identifiants_recalcules_depuis_la_cle"] = attendu == recalcule
            if attendu != recalcule:
                erreurs.append("identifiants non conformes à la règle et à la clé")
        texte_manifeste = json.dumps(b["manifeste"], ensure_ascii=False)
        if "--cle" in opts and str(int(json.loads(pathlib.Path(opts["--cle"]).read_text(encoding="utf-8"))["entropie_seed_sequence"])) in p.read_text(encoding="utf-8"):
            erreurs.append("la clé apparaît en clair dans la banque")
        eq["conforme"] = not erreurs
        rapport["equivalence_v1"] = eq
    if "--racine" in opts:
        sys.path.insert(0, opts["--racine"])
        from essaim_m3.banque import reference_traits_texte, verifier_banque
        rapport["verifier_banque"] = verifier_banque(p)
        erreurs.extend("verifier_banque : " + x for x in rapport["verifier_banque"])
        ref = reference_traits_texte(p)["par_famille"]
        rapport["reference_traits_texte"] = ref
        if "--v1" in opts:
            rapport["reference_identique_a_v1"] = reference_traits_texte(pathlib.Path(opts["--v1"]))["par_famille"] == ref
            if not rapport["reference_identique_a_v1"]:
                erreurs.append("référence de surface différente de celle de la v1")
    rapport["erreurs"] = erreurs
    rapport["cases_au_seuil"] = [f"{c['famille']} {c['part']} ({c['regle']} : {c['max']} ≥ {c['seuil']})" for c in cases if c["au_seuil"]]
    print(json.dumps(rapport, ensure_ascii=False, indent=1))
    if erreurs:
        return 2
    return 1 if rapport["cases_au_seuil"] else 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
