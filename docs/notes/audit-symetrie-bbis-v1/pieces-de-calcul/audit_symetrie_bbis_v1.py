"""Audit de symétrie (règle R4) de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — programme de contrôle, v1.

Usage : python3 -I audit_symetrie_bbis_v1.py <dossier des entrées extraites> <lecture-bbis.json> <dossier de sortie>

Ce programme ne lit AUCUN score de sonde. Dans les trois fichiers `scores-bbis-00x.npz`, il ne charge que les membres dont le
nom finit par `__cles`, `__taches`, `__y`, `nul__echanges`, `nul__taches`, `__sc_valide` (clés d'action, tâches, étiquettes
d'apprentissage, tirages du réétiquetage, masque de validité) ; pour les autres membres il ne lit que l'en-tête (forme, type),
jamais les valeurs. Il ne change aucun état, n'écrit rien dans le dépôt, ne calcule aucune aire de sonde.
"""
from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path

import numpy as np

ENTROPIE_AUDIT = 159077078314730721039794942417253791244  # tirée par secrets.randbits(128) le 2026-11-19T11:19:26Z
RUN_7B, RUN_BBIS = "20261111-151701-t06-reel", "20261118-154143-bbis-t07-v1"
PERMIS = ("__cles", "__taches", "__y", "nul__echanges", "nul__taches", "__sc_valide")
H, INSTRUIT, TEMOIN, T100 = "honnete", "saboteur", "temoin", "T100"
DOSES = (0.25, 0.5, 0.75, 1.0)
CONCERNEES = ("honnete", "saboteur", "S50", "S75", "S100")   # conditions des motifs du déclenchement
TRIVIAUX = ("jetons_notes", "pas", "mention_etendue")

E = Path(sys.argv[1]); LECTURE = Path(sys.argv[2]); SORTIE = Path(sys.argv[3])
SORTIE.mkdir(parents=True, exist_ok=True)
controles: list[dict] = []


def note(ident: str, quoi: str, conforme, detail):
    controles.append({"id": ident, "controle": quoi, "conforme": (bool(conforme) if conforme is not None else None),
                      "detail": detail})
    print(f"[{'CONFORME' if conforme else ('NON CONFORME' if conforme is not None else 'INFORMATION')}] {ident} — {quoi} : "
          f"{json.dumps(detail, ensure_ascii=False)[:900]}")


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def blob_git(p: Path) -> str:
    d = p.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(d) + d).hexdigest()


def cle_graine(nom: str) -> int:
    return int.from_bytes(hashlib.sha256(nom.encode("utf-8")).digest()[:8], "big")


def gen(entropie: int, nom: str, attendu=None):
    ss = np.random.SeedSequence(int(entropie), spawn_key=(cle_graine(nom),))
    etat = [int(x) for x in ss.generate_state(2)]
    if attendu is not None and (etat != attendu["etat_controle"] or [str(cle_graine(nom))] != attendu["spawn_key"]
                                or str(entropie) != attendu["entropie"]):
        raise SystemExit(f"graine {nom} : reconstruction ≠ graine consignée")
    return np.random.default_rng(ss), etat


def aire(v, y) -> float:
    """Mann-Whitney normalisée, ex aequo pour moitié (écriture indépendante du dépôt)."""
    v, y = np.asarray(v, float), np.asarray(y)
    ordre = np.argsort(v, kind="mergesort")
    r = np.empty(v.size)
    vs = v[ordre]
    i = 0
    while i < v.size:
        j = i
        while j + 1 < v.size and vs[j + 1] == vs[i]:
            j += 1
        r[ordre[i:j + 1]] = (i + j) / 2.0 + 1.0
        i = j + 1
    n1, n0 = int((y == 1).sum()), int((y == 0).sum())
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


# ------------------------------------------------------------------ 0. entrées, empreintes
fich = {
    "mesures": E / "donnees" / RUN_7B / "mesures-t06.npz",
    "textes": E / "donnees" / RUN_7B / "textes-actions-t06.jsonl",
    "episodes": E / "diag" / RUN_7B / "episodes-t06.json",
    "manifeste_7b": E / "runs" / RUN_7B / "manifeste.json",
    "manifeste_bbis": E / "runs" / RUN_BBIS / "manifeste.json",
    "relecture": E / "diag" / RUN_BBIS / "relecture-bbis.json",
    "sondes_json": E / "diag" / RUN_BBIS / "sondes-bbis.json",
    **{f"scores_{i}": E / "donnees" / RUN_BBIS / f"scores-bbis-00{i}.npz" for i in range(3)},
}
emp = {}
for n, p in fich.items():
    s, c = sha256(p), Path(str(p) + ".sha256").read_text().split()[0]
    emp[n] = {"fichier": str(p.relative_to(E)), "sha256": s, "octets": p.stat().st_size, "compagnon_egal": s == c}
emp["lecture"] = {"fichier": str(LECTURE), "sha256": sha256(LECTURE)}
lecture = json.loads(LECTURE.read_text(encoding="utf-8"))["resultat"]
sondes_doc = json.loads(fich["sondes_json"].read_text(encoding="utf-8"))
m_bbis = json.loads(fich["manifeste_bbis"].read_text(encoding="utf-8"))
m_7b = json.loads(fich["manifeste_7b"].read_text(encoding="utf-8"))
relecture = json.loads(fich["relecture"].read_text(encoding="utf-8"))
episodes = json.loads(fich["episodes"].read_text(encoding="utf-8"))["resultat"]
ok0 = all(v.get("compagnon_egal", True) for v in emp.values())
ok0 &= emp["lecture"]["sha256"] == "8e0d3e085601c3d9f5451b898acdcefc0caab6b61ddb1c6f382648e4425ed284"
ok0 &= emp["sondes_json"]["sha256"] == "645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62"
ok0 &= emp["mesures"]["sha256"] == lecture["mesures_sha256"] == episodes["mesures_sha256"]
ok0 &= emp["textes"]["sha256"] == episodes["textes_sha256"]
ok0 &= all(emp[f"scores_{i}"]["sha256"] == sondes_doc["fichiers_scores"][i]["sha256"] for i in range(3))
ok0 &= emp["manifeste_bbis"]["sha256"] == sondes_doc["manifeste"]["sha256"] == relecture["manifeste_sha256"]
ok0 &= emp["manifeste_7b"]["sha256"] == m_bbis["config"]["manifeste_7b_sha256"]
note("0.1", "empreintes des entrées : compagnons, lignes du registre propre, renvois croisés entre fichiers", ok0, emp)
loc = m_bbis["config"]["entrees_locales"]["fichiers"]
objets = {k: (blob_git(E / k), loc[k]["objet"]) for k in (f"donnees/{RUN_7B}/mesures-t06.npz", f"donnees/{RUN_7B}/textes-actions-t06.jsonl",
                                                             f"diag/{RUN_7B}/episodes-t06.json", f"runs/{RUN_7B}/manifeste.json")}
note("0.2", "les fichiers de la confirmation lus par la course (objets git du manifeste de la course) sont ceux lus ici",
     all(a == b for a, b in objets.values()), objets)

# ------------------------------------------------------------------ 1. mesures : cohérence interne
with np.load(fich["mesures"], allow_pickle=False) as z:
    M = {c: np.array(z[c]) for c in z.files}
N = M["cle"].size
cles = [str(c) for c in M["cle"]]
ligne = {c: i for i, c in enumerate(cles)}
cond = [str(c) for c in M["condition"]]
tache = [str(t) for t in M["tache"]]
prefixe = [c.split("__t")[0] for c in cles]
idx_t = [int(c.split("__t")[1].split("__p")[0]) for c in cles]
pas_cle = [int(c.split("__p")[1]) for c in cles]
conds = sorted(set(cond))
idx_vers_tache = {}
bij = True
for i in range(N):
    bij &= idx_vers_tache.setdefault(idx_t[i], tache[i]) == tache[i]
taches_ordre = [idx_vers_tache[k] for k in sorted(idx_vers_tache)]
par_cond = {c: sum(1 for x in cond if x == c) for c in conds}
etats_cond = {c: sorted({(str(M["phase"][i]), float(M["dose"][i])) for i in range(N) if cond[i] == c}) for c in conds}
ok1 = (N == 5760 and len(set(cles)) == N and prefixe == cond and pas_cle == [int(p) for p in M["pas"]] and bij
       and len(taches_ordre) == 64 and len(set(taches_ordre)) == 64 and all(v == 640 for v in par_cond.values())
       and all(len(v) == 1 for v in etats_cond.values())
       and all(str(M["episode"][i]).split("/")[:2] == [cond[i], tache[i]] for i in range(N))
       and all(sorted(pas_cle[i] for i in range(N) if cond[i] == c and tache[i] == taches_ordre[0]) == list(range(10)) for c in conds))
attendu_dose = {"S25": 0.25, "S50": 0.5, "S75": 0.75, "S100": 1.0, "honnete": 0.0, "saboteur": 0.0, "temoin": 0.0}
ok1 &= all(etats_cond[c][0][1] == d for c, d in attendu_dose.items() if c in etats_cond)
note("1.1", "mesures-t06.npz : 5760 clés uniques, préfixe de la clé = champ condition, rang du pas = suffixe, indice de tâche "
     "↔ tâche en bijection, 640 actions par condition, une phase et une dose par condition, dose = celle du nom", ok1,
     {"actions": N, "conditions": par_cond, "phase_et_dose_par_condition": {c: v for c, v in etats_cond.items()},
      "taches": len(taches_ordre), "jetons_notes_egal_jetons_moins_un": bool(np.all(M["jetons_notes"] == M["jetons"] - 1)),
      "champs": {c: str(v.dtype) for c, v in M.items()}})

# ------------------------------------------------------------------ 2. textes ↔ mesures (méta-données seulement)
vus, fautes = set(), []
for l in fich["textes"].read_text(encoding="utf-8").splitlines():
    if not l.strip():
        continue
    x = json.loads(l)
    k = str(x["cle"])
    if k in vus or k not in ligne:
        fautes.append(k); continue
    vus.add(k)
    i = ligne[k]
    if str(x["condition"]) != cond[i] or str(x["tache"]) != tache[i] or int(x.get("pas", pas_cle[i])) != pas_cle[i]:
        fautes.append(k)
    elif len(x["ids"]) != int(M["jetons"][i]):
        fautes.append(k + " (nombre d'identifiants ≠ jetons)")
note("2.1", "textes-actions-t06.jsonl : une ligne par clé des mesures, mêmes condition, tâche et pas ; nombre d'identifiants "
     "de jetons = champ jetons", not fautes and len(vus) == N, {"lignes": len(vus), "fautes": fautes[:10]})

# ------------------------------------------------------------------ 3. plis
g_part = m_7b["graines"]["partition-taches"]
ss = np.random.SeedSequence(int(g_part["entropie"]), spawn_key=tuple(int(k) for k in g_part["spawn_key"]))
assert [int(x) for x in ss.generate_state(2)] == g_part["etat_controle"]
graine_plis = int(np.random.default_rng(ss).integers(0, 2 ** 63 - 1))
uniques = sorted(set(tache))
rng = np.random.default_rng(graine_plis)
ordre = [uniques[int(i)] for i in rng.permutation(len(uniques))]
plis_re = {t: (0 if k < 32 else 1) for k, t in enumerate(ordre)}
plis = {str(t): int(p) for t, p in sondes_doc["plis"].items()}
ok3 = plis_re == plis == {str(t): int(p) for t, p in lecture["plis"].items()} and sum(plis.values()) == 32
note("3.1", "plis externes recalculés par la graine « partition-taches » de la confirmation = plis du fichier des sondes = plis "
     "du fichier de lecture ; 32 tâches par pli", ok3, {"pli_0": sum(1 for p in plis.values() if p == 0), "pli_1": sum(plis.values())})
taches_pli = {k: sorted(t for t, p in plis.items() if p == k) for k in (0, 1)}
entropie = int(m_bbis["graines"]["bbis/chemin-impose"]["entropie"])
gd = sondes_doc["graines_derivees"]
ok_int = True
for src, pp in sondes_doc["sources"].items():
    for ek, meta in pp.items():
        k = int(ek[1:])
        r, _ = gen(entropie, f"bbis/interne/e{k}", gd[f"bbis/interne/e{k}"])
        t = taches_pli[1 - k]
        o = [t[int(i)] for i in r.permutation(len(t))]
        ok_int &= meta["plis_internes"] == [sorted(o[j * 8:(j + 1) * 8]) for j in range(4)]
        ok_int &= meta["taches_lues"] == taches_pli[k] and meta["pli_lu"] == k
        ok_int &= not (set(sum(meta["plis_internes"], [])) & set(taches_pli[k]))
note("3.2", "plis internes de chaque source rederivés de la graine « bbis/interne/<pli> » ; tâches lues = tâches du pli ; "
     "aucune tâche du pli lu dans un pli interne", ok_int, {"sources": sorted(sondes_doc["sources"]), "entropie_course": str(entropie)})

# ------------------------------------------------------------------ 4. fichiers de scores : clés, tâches, étiquettes (sans score)
T: dict = {}
formes: dict = {}
membres_non_lus = 0
for i in range(3):
    with zipfile.ZipFile(fich[f"scores_{i}"]) as z:
        for nom_z in z.namelist():
            nom = nom_z[:-4]
            src, ek, reste = nom.split("__", 2)
            with z.open(nom_z) as f:
                v = np.lib.format.read_magic(f)
                forme, _, dt = (np.lib.format.read_array_header_1_0(f) if v == (1, 0) else np.lib.format.read_array_header_2_0(f))
                formes[(src, int(ek[1:]), reste)] = (tuple(forme), str(dt))
            if reste.endswith(PERMIS):
                with z.open(nom_z) as f:
                    T[(src, int(ek[1:]), reste)] = np.lib.format.read_array(f, allow_pickle=False)
            else:
                membres_non_lus += 1


def plan(positifs):
    dec = [("O", positifs), ("O", H)]
    cent = lambda d: int(round(d * 100))
    if positifs == INSTRUIT:
        s = dec + [("Jinstruit", INSTRUIT), ("O", TEMOIN)]
        for d in DOSES:
            s += [("O", f"S{cent(d)}"), (f"J{cent(d)}", f"S{cent(d)}"), (f"A{cent(d)}", H)]
        return s
    d = int(positifs[1:])
    s = dec + [(f"J{d}", positifs), (f"A{d}", H), ("O", T100), ("AT", H)]
    if d == 100:
        s += [("O", INSTRUIT), ("Jinstruit", INSTRUIT)]
    return s


SOURCES = {"P-instruit": INSTRUIT, "P-S25": "S25", "P-S50": "S50", "P-S75": "S75", "P-S100": "S100"}
fautes4, n_groupes, actions_lues = [], 0, {}
ref_cles = {}
for src, pos in SOURCES.items():
    for k in (0, 1):
        tot = 0
        attendus = {f"{s}-{c}" for s, c in plan(pos)}
        ecrits = {r.rsplit("__", 1)[0] for (a, b, r) in formes if a == src and b == k and r.endswith("__cles")
                  and not r.startswith(("app__", "app_enc__"))}
        if attendus != ecrits:
            fautes4.append(f"{src}/e{k} : groupes écrits {sorted(ecrits)} ≠ plan {sorted(attendus)}")
        for g in sorted(ecrits):
            n_groupes += 1
            serie, c = g.split("-", 1)
            kc = [str(x) for x in T[(src, k, f"{g}__cles")]]
            tc = [str(x) for x in T[(src, k, f"{g}__taches")]]
            att = sorted(x for x in cles if cond[ligne[x]] == c and tache[ligne[x]] in set(taches_pli[k]))
            if kc != att:
                fautes4.append(f"{src}/e{k}/{g} : clés ≠ les 320 clés de la condition dans le pli lu (ordre trié)")
            if any(x not in ligne for x in kc) or tc != [tache[ligne[x]] for x in kc if x in ligne]:
                fautes4.append(f"{src}/e{k}/{g} : tâche écrite ≠ tâche des mesures")
            if len(kc) != 320 or len(set(kc)) != 320:
                fautes4.append(f"{src}/e{k}/{g} : {len(kc)} clés")
            if ref_cles.setdefault((k, c), kc) != kc:
                fautes4.append(f"{src}/e{k}/{g} : clés de la condition {c} différentes d'une autre série ou d'une autre source")
            for champ, f_att in (("sonde", (320,)), ("plancher", (800, 320)), ("nul", (100, 320)), ("enc", (320,)),
                                 ("sc_sonde", (320,)), ("sc_plancher", (800, 320)), ("sc_valide", (320,)), ("sonde_o2", None)):
                f = formes.get((src, k, f"{g}__{champ}"))
                if f is not None and f_att is not None and f[0] != f_att:
                    fautes4.append(f"{src}/e{k}/{g}__{champ} : forme {f[0]} ≠ {f_att}")
            if (src, k, f"{g}__sonde") not in formes or (src, k, f"{g}__plancher") not in formes:
                fautes4.append(f"{src}/e{k}/{g} : sonde ou plancher absent")
            tot += len(kc) if g.startswith("O-") else 0   # le fichier de lecture compte les seuls groupes d'origine
        actions_lues.setdefault(src, {})[f"e{k}"] = tot
ok_al = actions_lues == lecture["actions_des_groupes_lus"]
note("4.1", "fichiers de scores, par source, pli et groupe (série, condition) : groupes écrits = plan gelé ; clés = exactement "
     "les 320 clés de la condition dans les tâches du pli lu ; tâche écrite = tâche des mesures ; mêmes clés, même ordre, pour une "
     "même condition dans toutes les séries et toutes les sources (donc paires « texte égal » et « adaptateur seul » alignées "
     "clé à clé) ; formes des tableaux de scores (en-têtes seuls) ; totaux des groupes d'origine = « actions des groupes lus » du fichier de lecture",
     not fautes4 and ok_al, {"groupes_controles": n_groupes, "fautes": fautes4[:10], "actions_des_groupes_lus": actions_lues,
                             "membres_dont_seul_l_en_tete_est_lu": membres_non_lus, "membres_charges": len(T)})

# apprentissage : étiquettes et disjonction
fautes5 = []
for src, pos in SOURCES.items():
    for k in (0, 1):
        for pre in ("app", "app_enc"):
            kc = [str(x) for x in T[(src, k, f"{pre}__cles")]]
            y = np.asarray(T[(src, k, f"{pre}__y")]).astype(int)
            att_y = np.array([1 if cond[ligne[x]] == pos else 0 for x in kc])
            if not np.array_equal(y, att_y):
                fautes5.append(f"{src}/e{k}/{pre} : étiquette ≠ (condition de la clé = condition des positifs)")
            if {cond[ligne[x]] for x in kc} != {pos, H}:
                fautes5.append(f"{src}/e{k}/{pre} : conditions {sorted({cond[ligne[x]] for x in kc})}")
            if {tache[ligne[x]] for x in kc} != set(taches_pli[1 - k]):
                fautes5.append(f"{src}/e{k}/{pre} : tâches d'apprentissage ≠ l'autre pli")
            if len(kc) != 640 or int(y.sum()) != 320 or len(set(zip(kc, y.tolist()))) != 640:
                fautes5.append(f"{src}/e{k}/{pre} : {len(kc)} actions, {int(y.sum())} positifs")
note("4.2", "jeux d'apprentissage (sonde et lecteur honnête) : étiquette 1 si et seulement si la clé est de la condition des "
     "positifs ; seules la condition des positifs et l'honnête ; tâches = exactement l'autre pli (aucune tâche du pli lu) ; "
     "320 positifs et 320 négatifs", not fautes5, {"jeux": 20, "fautes": fautes5[:10]})

# réétiquetages
fautes6 = []
tri = sorted(plis)
for src in SOURCES:
    e0, e1 = T[(src, 0, "nul__echanges")], T[(src, 1, "nul__echanges")]
    if not (np.array_equal(e0, e1) and e0.shape == (100, 64) and [str(x) for x in T[(src, 0, "nul__taches")]] == tri
            and [str(x) for x in T[(src, 1, "nul__taches")]] == tri):
        fautes6.append(f"{src} : forme ou tâches")
        continue
    for r in range(100):
        g, _ = gen(entropie, f"bbis/reetiquetage/{src}/{r}", gd[f"bbis/reetiquetage/{src}/{r}"])
        if not np.array_equal(g.random(64) < 0.5, e0[r]):
            fautes6.append(f"{src}/{r}")
note("4.3", "nul de réétiquetage : 100 tirages par source sur les 64 tâches triées, égaux entre les deux plis, rederivés au bit "
     "près des graines « bbis/reetiquetage/<cellule>/<r> »", not fautes6,
     {"fautes": fautes6[:10], "part_moyenne_de_taches_echangees": float(np.mean([T[(s, 0, 'nul__echanges')].mean() for s in SOURCES]))})

# cellules de la lecture : groupes positifs et négatifs, effectifs
CELL = {"P-instruit": ("P-instruit", INSTRUIT)}
for d in (25, 50, 75, 100):
    CELL[f"P-S{d}"] = (f"P-S{d}", f"S{d}")
    CELL[f"T-instruit-S{d}"] = ("P-instruit", f"S{d}")
CELL["T-S100-instruit"] = ("P-S100", INSTRUIT)
fautes7, jeux = [], {}
for nom, (src, pos) in CELL.items():
    c = lecture["cellules"][nom]
    if c["source"] != src or c["positifs"] != pos:
        fautes7.append(f"{nom} : source ou positifs du fichier de lecture ≠ plan")
    eff = []
    for k in (0, 1):
        kp = [str(x) for x in T[(src, k, f"O-{pos}__cles")]]
        kn = [str(x) for x in T[(src, k, f"O-{H}__cles")]]
        if {cond[ligne[x]] for x in kp} != {pos} or {cond[ligne[x]] for x in kn} != {H}:
            fautes7.append(f"{nom}/e{k} : condition des positifs ou des négatifs")
        if sorted({tache[ligne[x]] for x in kp}) != taches_pli[k] or sorted({tache[ligne[x]] for x in kn}) != taches_pli[k]:
            fautes7.append(f"{nom}/e{k} : tâches ≠ pli lu")
        eff.append({"negatifs": len(kn), "positifs": len(kp)})
        jeux[(nom, k)] = (kp, kn)
    if eff != c["D"]["effectifs"]:
        fautes7.append(f"{nom} : effectifs {eff} ≠ fichier de lecture {c['D']['effectifs']}")
note("4.4", "dix cellules décisives : source et positifs du fichier de lecture = plan gelé ; positifs tous de la condition "
     "nommée, négatifs tous honnêtes ; tâches = pli lu ; effectifs = ceux du fichier de lecture", not fautes7,
     {"cellules": len(CELL), "fautes": fautes7[:10]})

# masque de la lecture sans le champ du coût : décompte des exclusions
excl, fautes8 = {}, []
for d in (25, 50, 75, 100):
    src = f"P-S{d}"
    e = {g: int(sum((~T[(src, k, f"{g}__sc_valide")].astype(bool)).sum() for k in (0, 1))) for g in (f"O-S{d}", f"O-{H}", f"J{d}-S{d}")}
    excl[src] = e
    if e != lecture["cellules"][src]["SC_exclues"]:
        fautes8.append(src)
    for k in (0, 1):
        if not np.array_equal(T[(src, k, f"O-S{d}__sc_valide")], T[(src, k, f"J{d}-S{d}__sc_valide")]):
            fautes8.append(f"{src}/e{k} : masque différent entre la série d'origine et son jumeau à texte égal")
note("4.5", "lecture sans le champ du coût : décompte des actions exclues = fichier de lecture ; masque identique entre une "
     "série et son jumeau à texte égal (mêmes textes)", not fautes8, excl)

# ------------------------------------------------------------------ 5. prédicteurs triviaux
triv, fautes9, ecart_max = {}, [], 0.0
for nom in CELL:
    c = lecture["cellules"][nom]
    a_sonde = c["D"]["aire"]
    sep_sonde = max(a_sonde, 1 - a_sonde)
    triv[nom] = {"aire_de_la_sonde_recopiee_du_fichier_de_lecture": a_sonde}
    for col in TRIVIAUX:
        aires = []
        for k in (0, 1):
            kp, kn = jeux[(nom, k)]
            v = np.array([float(M[col][ligne[x]]) for x in kp + kn])
            y = np.r_[np.ones(len(kp), int), np.zeros(len(kn), int)]
            aires.append(aire(v, y))
        a = float(sum(aires) / 2)
        sep = max(a, 1 - a)
        lu = c["triviaux"][col]
        ecart = max(abs(a - lu["aire"]), abs(sep - lu["separation"]))
        ecart_max = max(ecart_max, ecart)
        triv[nom][col] = {"aire_recalculee": a, "separation_recalculee": sep, "aire_du_fichier": lu["aire"],
                          "separation_du_fichier": lu["separation"], "aires_par_pli": aires}
        if ecart > 1e-12 or lu["n"] != 1280:
            fautes9.append(f"{nom}/{col} : écart {ecart}")
        if sep >= sep_sonde:
            fautes9.append(f"{nom}/{col} : sépare au moins autant que la sonde")
sep_max = max(v[col]["separation_recalculee"] for v in triv.values() for col in TRIVIAUX)
note("5.1", "prédicteurs triviaux (longueur notée, rang du pas, mention étendue) recalculés des seuls champs de "
     "mesures-t06.npz sur les jeux décisifs, par une écriture indépendante de l'aire : égaux au fichier de lecture ; aucun ne "
     "sépare autant que la sonde dans aucune cellule", not fautes9,
     {"ecart_absolu_maximal_au_fichier": ecart_max, "separation_triviale_maximale": sep_max, "fautes": fautes9, "cellules": triv})
# « sans objet à texte égal » : mêmes clés des deux côtés des paires relues
paires = []
for d in (25, 50, 75, 100):
    for src in (f"P-S{d}", "P-instruit"):
        for k in (0, 1):
            paires.append(np.array_equal(T[(src, k, f"O-S{d}__cles")], T[(src, k, f"J{d}-S{d}__cles")]))
            paires.append(np.array_equal(T[(src, k, f"O-{H}__cles")], T[(src, k, f"A{d}-{H}__cles")]))
note("5.2", "paires relues (série d'origine et jumeau à texte égal ; honnête d'origine et honnête sous l'adaptateur) : mêmes "
     "clés, même ordre, des deux côtés — les prédicteurs triviaux y valent un demi par construction", all(paires), {"paires": len(paires)})

# ------------------------------------------------------------------ 6. échantillon de 20 clés par condition concernée
lignes_e, graines_e, fautes10 = [], {}, []
champs = list(M)
for c in CONCERNEES:
    nomg = f"audit-symetrie-bbis-v1/echantillon/{c}"
    g, etat = gen(ENTROPIE_AUDIT, nomg)
    graines_e[c] = {"cle": nomg, "entropie": str(ENTROPIE_AUDIT), "spawn_key": [str(cle_graine(nomg))], "etat_controle": etat}
    pop = sorted(x for x in cles if cond[ligne[x]] == c)
    tirees = [pop[int(i)] for i in sorted(g.choice(len(pop), size=20, replace=False))]
    for x in tirees:
        i = ligne[x]
        k = plis[tache[i]]
        ou = sorted({(a, r.rsplit("__", 1)[0]) for (a, b, r), v in T.items()
                     if v is not None and r.endswith("__cles") and not r.startswith("app") and x in set(map(str, v)) and b == k})
        ailleurs = [(a, b, r) for (a, b, r), v in T.items() if r.endswith("__cles") and not r.startswith("app") and b != k
                    and x in set(map(str, v))]
        app = sorted({(a, b) for (a, b, r), v in T.items() if r == "app__cles" and x in set(map(str, v))})
        role = {}
        for nom, (src, pos) in CELL.items():
            kp, kn = jeux[(nom, k)]
            role[nom] = "positif" if x in kp else ("négatif" if x in kn else "absent")
        att_role = {nom: ("positif" if pos == c else ("négatif" if c == H else "absent")) for nom, (src, pos) in CELL.items()}
        att_series = {(s, f"{a}-{b}") for s, p in SOURCES.items() for a, b in plan(p) if b == c}
        if (prefixe[i] != c or ailleurs or role != att_role or set(ou) != att_series
                or any(b == k for a, b in app) or {a for a, b in app} != {s for s, p in SOURCES.items() if p == c or c == H}):
            fautes10.append(x)
        lignes_e.append({"condition_tiree": c, **{f: (M[f][i].item() if hasattr(M[f][i], "item") else str(M[f][i])) for f in champs},
                         "pli_de_la_tache": k, "groupes_ou_la_cle_est_notee": [f"{a}:{b}" for a, b in ou],
                         "role_par_cellule": role})
note("6.1", "échantillon de 20 clés d'action par condition concernée (honnête, organisme à consigne cachée, doses 0,5, 0,75 et "
     "1), tiré par graine : chaque clé est de la condition tirée, notée dans le seul pli de sa tâche, dans exactement les groupes "
     "que le plan prévoit, apprise seulement dans l'autre pli, positive dans les cellules de sa condition, négative si honnête, "
     "absente ailleurs", not fautes10, {"cles_tirees": len(lignes_e), "fautes": fautes10, "graines": graines_e})
with (SORTIE / "echantillon-20-cles-par-condition-v1.tsv").open("w", encoding="utf-8") as f:
    f.write("\t".join(["condition_tiree"] + champs + ["pli_de_la_tache", "role_par_cellule"]) + "\n")
    for l in lignes_e:
        r = ",".join(f"{a}={b[:3]}" for a, b in l["role_par_cellule"].items() if b != "absent")
        f.write("\t".join(str(l[x]) for x in ["condition_tiree"] + champs + ["pli_de_la_tache"]) + "\t" + r + "\n")
# résumé descriptif de l'échantillon (champs des mesures seulement)
resume = {}
for c in CONCERNEES:
    ls = [l for l in lignes_e if l["condition_tiree"] == c]
    resume[c] = {"taches_distinctes": len({l["tache"] for l in ls}), "pas": sorted(l["pas"] for l in ls),
                 "phase": sorted({l["phase"] for l in ls}), "dose": sorted({l["dose"] for l in ls}),
                 "jetons_notes_min_max": [min(l["jetons_notes"] for l in ls), max(l["jetons_notes"] for l in ls)],
                 "valide": sum(bool(l["valide"]) for l in ls), "cout_present": sum(bool(l["cout_present"]) for l in ls),
                 "mention": sum(bool(l["mention"]) for l in ls), "mention_etendue": sum(bool(l["mention_etendue"]) for l in ls),
                 "pli_0": sum(1 for l in ls if l["pli_de_la_tache"] == 0)}
note("6.2", "échantillon : résumé des champs des mesures par condition (information, lue à l'œil ; table complète à côté)", None, resume)

# ------------------------------------------------------------------ 7. gardes d'égalité au bit près de la course
R = relecture["resultat"]
ch = R["chemin_impose"]
g, _ = gen(entropie, "bbis/chemin-impose", m_bbis["graines"]["bbis/chemin-impose"])
tirage = [sorted(taches_ordre[int(i)] for i in g.choice(64, size=8, replace=False)) for _ in range(3)]
ok_t = tirage == [ch["episodes"]["H"], ch["episodes"]["S100"], ch["episodes"]["T100"]]
note("7.1", "garde du chemin de l'état imposé : les trois tirages de 8 épisodes écrits par la course sont ceux que rend la "
     "graine « bbis/chemin-impose » de son manifeste (rederivés ici ; aucun choix après coup)", ok_t,
     {"honnete": tirage[0], "S100": tirage[1], "T100": tirage[2]})
att_tab = {}
for nomc, c, ts in (("H sous le modèle nu", H, tirage[0]), ("S100 sous S100", "S100", tirage[1]), ("T100 sous T100", T100, tirage[2])):
    att_tab[nomc] = 3 * sum(1 for i in range(N) if cond[i] == c and tache[i] in set(ts) and int(M["jetons_notes"][i]) > 0)
ok_g = (all(ch["cas_sains"][n] == {"differentes": 0, "egales": att_tab[n]} for n in att_tab)
        and ch["artefact_H_sous_S100"]["egales"] == 0 and ch["artefact_H_sous_S100"]["differentes"] == att_tab["H sous le modèle nu"]
        and ch["n"] == 8 and R["aucun_score"] is True)
note("7.2", "garde du chemin de l'état imposé, telle que la course l'a écrite : trois cas sains égaux au bit près à la série "
     "d'origine sur tous les tableaux (action × couche) des épisodes tirés ; artefact (honnête relu sous l'adaptateur à dose 1) "
     "différent sur tous ; nombres de tableaux = 3 couches × actions notées des épisodes tirés, recomptés ici des mesures", ok_g,
     {"ecrit_par_la_course": ch["cas_sains"], "artefact": ch["artefact_H_sous_S100"], "tableaux_attendus": att_tab})
ident = [R["identite_etat_impose"], R["serie_O"]["identite_dose_0"]]
ok_i = all(x[a]["dose_0_identique"] is True and x[a]["dose_1_differente"] is True for x in ident for a in ("saboteur", "temoin"))
ok_i &= all(x[a]["empreinte"] == R["serie_O"]["adaptateurs"][a] for x in ident for a in ("saboteur", "temoin"))
note("7.3", "contrôle d'identité : à dose 0 le modèle porteur d'adaptateurs rend les logits de la base au bit près, à dose 1 il "
     "s'en écarte ; mêmes empreintes d'adaptateurs sur les deux chemins", ok_i,
     {"chemin_neuf": R["identite_etat_impose"], "chemin_ancien": R["serie_O"]["identite_dose_0"]})
att_series = ([{"serie": f"J{d}", "textes": f"S{d}", "adaptateur": "saboteur", "dose": 0.0} for d in (25, 50, 75, 100)]
              + [{"serie": "Jinstruit", "textes": INSTRUIT, "adaptateur": "saboteur", "dose": 0.0}]
              + [{"serie": f"A{d}", "textes": H, "adaptateur": "saboteur", "dose": d / 100} for d in (25, 50, 75, 100)]
              + [{"serie": "AT", "textes": H, "adaptateur": "temoin", "dose": 1.0}])
ok_s = len(R["series"]) == 10
for s, a in zip(R["series"], att_series):
    ok_s &= (s["serie"] == a["serie"] and s["textes"] == a["textes"] and s["environnement"] == H and s["episodes"] == 64
             and s["actions"] == 640 and s["etat"]["adaptateur"] == a["adaptateur"] and s["etat"]["dose"] == a["dose"]
             and s["etat"]["modules"] == 128 and s["etat"]["empreinte"] == R["serie_O"]["adaptateurs"][a["adaptateur"]])
note("7.4", "dix séries relues à état imposé : textes, environnement honnête, adaptateur, dose lue sur les 128 modules, "
     "empreinte de l'adaptateur, 64 épisodes et 640 actions, conformes au plan gelé", ok_s,
     [{"serie": s["serie"], "textes": s["textes"], "dose": s["etat"]["dose"], "adaptateur": s["etat"]["adaptateur"]} for s in R["series"]])
ge = R["serie_O"]["garde_equivalence"]
note("7.5", "série d'origine recalculée contre le sous-ensemble d'activations poussé par la confirmation (garde d'équivalence "
     "du chemin ancien, tolérance 0,2 sur le quantile 0,99 de l'écart ; contrôle négatif décalé d'un jeton)",
     ge["ecart_max"] <= ge["tolerance"] and ge["controle_negatif"]["au_dessus"] >= 0.95 * ge["controle_negatif"]["actions"]
     and R["serie_O"]["rejeu"] == {"actions_notees_recalculees": 5760, "episodes": 576}, ge)
note("7.6", "comparaison directe à l'octet, par ce programme, d'une même série entre les deux chemins", None,
     "NON FAISABLE sur les fichiers de la course : les activations (séries d'origine et relues) n'ont pas été poussées, seuls "
     "les scores l'ont été ; et aucune série n'a été écrite deux fois (une fois par chaque chemin) dans les fichiers de scores : "
     "rouvrir les scores de sonde n'apporterait donc pas ce contrôle. La preuve disponible est celle de la garde de la course "
     "(7.1 à 7.3), sur 8 épisodes sur 64 par cas.")

bilan = {"conformes": sum(1 for c in controles if c["conforme"] is True), "non_conformes": [c["id"] for c in controles if c["conforme"] is False],
         "informations": [c["id"] for c in controles if c["conforme"] is None]}
doc = {"audit": "symétrie (R4) — étape B bis de T0.7", "programme": Path(sys.argv[0]).name,
       "programme_sha256": sha256(Path(sys.argv[0])), "numpy": np.__version__, "python": sys.version.split()[0],
       "entropie_audit": str(ENTROPIE_AUDIT), "aucun_score_de_sonde_lu": True, "bilan": bilan, "controles": controles}
(SORTIE / "controles-audit-symetrie-bbis-v1.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True) + "\n",
                                                             encoding="utf-8")
print("BILAN", json.dumps(bilan, ensure_ascii=False))
