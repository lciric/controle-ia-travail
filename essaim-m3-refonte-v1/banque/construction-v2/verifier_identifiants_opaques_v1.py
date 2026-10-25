"""Contrôle « aucune règle sur l'identifiant ne prédit la vérité » d'une banque de tâches — v1.

Pour chaque famille, des règles qui ne lisent que l'identifiant sont apprises sur `train` (où l'organisme voit
identifiant et vérité) et notées sur `test` et sur `test_final` (exactitude équilibrée) :
- catégorielles (valeur → vérité majoritaire sur train ; valeur jamais vue → classe majoritaire de la famille sur
  train ; égalités → la première étiquette) : suffixes de 1 à 3 caractères, préfixes de 1 à 6, caractère à chaque
  position, longueur, chaque segment séparé par « - » (premier, dernier, rang 0 à 3), nombre formé des chiffres modulo
  m (m = 2 à 10) ;
- à seuil : le nombre formé des chiffres de l'identifiant, seuil et sens choisis au mieux sur train.
Une règle est **prédictive** si son exactitude équilibrée est ≥ 0,80 sur `test` **et** sur `test_final` pour une même
famille. Code de sortie : 0 si aucune règle prédictive, 1 sinon, 2 sur erreur de forme.

Avec `--v1 BANQUE_V1 --secret-v1 SECRET_V1 --secret SECRET` (banque dérivée par `construire_banque_v2_…`) : contrôle
d'équivalence — mêmes parts, même ordre, mêmes `famille`, `texte`, `etiquettes`, `verite`, `source` à chaque rang ;
`id_v1` du secret = identifiant v1 au même rang ; dossiers secrets égaux à ceux de la v1 à `id_v1` près.
Avec `--racine DOSSIER` (racine `essaim-m3-refonte-v1` du code) : `essaim_m3.banque.verifier_banque` sur la banque, et
`reference_traits_texte` comparée entre la banque et la v1 (champs `banque` et `sha256` mis à part).

Usage : python3 -I verifier_identifiants_opaques_v1.py BANQUE [--v1 … --secret-v1 … --secret …] [--racine …]
"""
import hashlib
import json
import pathlib
import re
import sys

PARTS = ("train", "test", "test_final")
SEUIL = 0.80


def exactitude_equilibree(pred: list, vrai: list, pos: str) -> float:
    tp = sum(1 for p, v in zip(pred, vrai) if v == pos and p == pos)
    tn = sum(1 for p, v in zip(pred, vrai) if v != pos and p != pos)
    npos = sum(1 for v in vrai if v == pos)
    nneg = len(vrai) - npos
    return ((tp / npos if npos else 0.0) + (tn / nneg if nneg else 0.0)) / 2


def nombre(s: str):
    d = "".join(ch for ch in s if ch.isdigit())
    return int(d) if d else None


def traits_categoriels(s: str) -> dict:
    f = {}
    for k in (1, 2, 3):
        f[f"suffixe_{k}"] = s[-k:]
    for k in range(1, 7):
        f[f"prefixe_{k}"] = s[:k]
    for i in range(24):
        f[f"caractere_{i:02d}"] = s[i] if i < len(s) else ""
    f["longueur"] = len(s)
    seg = s.split("-")
    f["segment_premier"], f["segment_dernier"] = seg[0], seg[-1]
    for j in range(4):
        f[f"segment_{j}"] = seg[j] if j < len(seg) else ""
    n = nombre(s)
    for m in range(2, 11):
        f[f"nombre_mod_{m}"] = (n % m) if n is not None else None
    return f


def apprendre_categoriel(valeurs: list, verites: list, etiquettes: list):
    compte = {}
    for v, y in zip(valeurs, verites):
        compte.setdefault(v, {e: 0 for e in etiquettes})[y] += 1
    tot = {e: verites.count(e) for e in etiquettes}
    defaut = max(etiquettes, key=lambda e: (tot[e], -etiquettes.index(e)))
    regle = {v: max(etiquettes, key=lambda e: (c[e], -etiquettes.index(e))) for v, c in compte.items()}
    return lambda v: regle.get(v, defaut)


def apprendre_seuil(valeurs: list, verites: list, pos: str, neg: str):
    vus = sorted({v for v in valeurs if v is not None})
    if not vus:
        return None, None
    candidats = [vus[0] - 0.5] + [(a + b) / 2 for a, b in zip(vus, vus[1:])] + [vus[-1] + 0.5]
    meilleur = (-1.0, None)
    for s in candidats:
        for sens in (1, -1):
            pred = [(pos if (v is not None and (v - s) * sens > 0) else neg) for v in valeurs]
            ex = exactitude_equilibree(pred, verites, pos)
            if ex > meilleur[0]:
                meilleur = (ex, (s, sens))
    s, sens = meilleur[1]
    return (lambda v: pos if (v is not None and (v - s) * sens > 0) else neg), f"seuil {s} sens {sens}"


def regles_identifiant(b: dict) -> dict:
    sortie = {}
    for fam in sorted({t["famille"] for t in b["train"]}):
        etiquettes = list(next(t["etiquettes"] for t in b["train"] if t["famille"] == fam))
        pos, neg = etiquettes[0], etiquettes[1]
        tr = [t for t in b["train"] if t["famille"] == fam]
        resultats = []
        noms = sorted(traits_categoriels(tr[0]["id"]))
        for nom in noms:
            r = apprendre_categoriel([traits_categoriels(t["id"])[nom] for t in tr], [t["verite"] for t in tr], etiquettes)
            res = {"regle": nom}
            for part in ("test", "test_final"):
                te = [t for t in b[part] if t["famille"] == fam]
                res[part] = round(exactitude_equilibree([r(traits_categoriels(t["id"])[nom]) for t in te], [t["verite"] for t in te], pos), 4)
            resultats.append(res)
        r, desc = apprendre_seuil([nombre(t["id"]) for t in tr], [t["verite"] for t in tr], pos, neg)
        if r is not None:
            res = {"regle": f"nombre_{desc}"}
            for part in ("test", "test_final"):
                te = [t for t in b[part] if t["famille"] == fam]
                res[part] = round(exactitude_equilibree([r(nombre(t["id"])) for t in te], [t["verite"] for t in te], pos), 4)
            resultats.append(res)
        resultats.sort(key=lambda x: (-min(x["test"], x["test_final"]), x["regle"]))
        predictives = [x for x in resultats if x["test"] >= SEUIL and x["test_final"] >= SEUIL]
        sortie[fam] = {"n_regles": len(resultats), "meilleures": resultats[:3], "predictives": predictives,
                       "max_test": max(x["test"] for x in resultats), "max_test_final": max(x["test_final"] for x in resultats)}
    return sortie


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def principal(argv: list[str]) -> int:
    args = list(argv)
    opts = {}
    for cle in ("--v1", "--secret-v1", "--secret", "--racine"):
        if cle in args:
            i = args.index(cle)
            opts[cle] = pathlib.Path(args[i + 1])
            del args[i:i + 2]
    if len(args) != 1:
        print("usage : BANQUE [--v1 … --secret-v1 … --secret …] [--racine …]")
        return 2
    p = pathlib.Path(args[0])
    b = json.loads(p.read_text(encoding="utf-8"))
    rapport = {"banque": p.name, "sha256": sha(p), "seuil": SEUIL}
    ids = [t["id"] for part in PARTS for t in b[part]]
    rapport["identifiants"] = {"n": len(ids), "uniques": len(set(ids)) == len(ids),
                               "formes": sorted({re.sub(r"\d", "9", re.sub(r"[a-z]", "a", i)) for i in ids})[:6]}
    rapport["regles"] = regles_identifiant(b)
    erreurs = []
    if not rapport["identifiants"]["uniques"]:
        erreurs.append("identifiants en double")
    if all(k in opts for k in ("--v1", "--secret-v1", "--secret")):
        v1 = json.loads(opts["--v1"].read_text(encoding="utf-8"))
        s1 = json.loads(opts["--secret-v1"].read_text(encoding="utf-8"))
        s2 = json.loads(opts["--secret"].read_text(encoding="utf-8"))
        eq = {"v1": opts["--v1"].name, "v1_sha256": sha(opts["--v1"]), "secret_sha256": sha(opts["--secret"])}
        for part in PARTS:
            if len(b[part]) != len(v1[part]):
                erreurs.append(f"{part} : {len(b[part])} tâches au lieu de {len(v1[part])}")
                continue
            for t2, t1 in zip(b[part], v1[part]):
                for k in ("famille", "texte", "etiquettes", "verite", "source"):
                    if t2.get(k) != t1.get(k):
                        erreurs.append(f"{part} {t2['id']} : champ {k} différent de la v1 ({t1['id']})")
                if sorted(t2) != sorted(t1):
                    erreurs.append(f"{part} {t2['id']} : champs {sorted(t2)} au lieu de {sorted(t1)}")
                d2 = dict(s2.get(t2["id"], {}))
                if d2.pop("id_v1", None) != t1["id"]:
                    erreurs.append(f"{part} {t2['id']} : id_v1 du secret différent de {t1['id']}")
                if d2 != s1.get(t1["id"]):
                    erreurs.append(f"{part} {t2['id']} : dossier secret différent de celui de {t1['id']}")
        if set(s2) != set(ids):
            erreurs.append("le secret ne couvre pas exactement les tâches de la banque")
        if set(ids) & {t["id"] for part in PARTS for t in v1[part]}:
            erreurs.append("identifiants communs avec la v1")
        eq["conforme"] = not erreurs
        rapport["equivalence_v1"] = eq
    if "--racine" in opts:
        sys.path.insert(0, str(opts["--racine"]))
        from essaim_m3.banque import reference_traits_texte, verifier_banque
        rapport["verifier_banque"] = verifier_banque(p)
        if rapport["verifier_banque"]:
            erreurs.extend("verifier_banque : " + x for x in rapport["verifier_banque"])
        ref = reference_traits_texte(p)
        rapport["reference_traits_texte"] = ref["par_famille"]
        if "--v1" in opts:
            ref1 = reference_traits_texte(opts["--v1"])
            rapport["reference_identique_a_v1"] = ref1["par_famille"] == ref["par_famille"]
            if not rapport["reference_identique_a_v1"]:
                erreurs.append("référence de surface différente de celle de la v1")
    rapport["erreurs"] = erreurs
    rapport["regles_predictives"] = {f: len(r["predictives"]) for f, r in rapport["regles"].items()}
    print(json.dumps(rapport, ensure_ascii=False, indent=1))
    if erreurs:
        return 2
    return 1 if any(rapport["regles_predictives"].values()) else 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
