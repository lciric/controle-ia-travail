"""Banque `confrontation-v5` : la sélection de la v4 (une trace par paire de `controle-delegation` en test et en test
final) sous des **identifiants neufs**, avec un manifeste juste — v1 de ce script.

Sur la contre-lecture de la v4 (`contre-lectures/banque-v4-cl1/CONTRE-LECTURE-banque-v4-v1.md`, ea2916af…) : BC4-02 (la
v3, servie au pilote 4, porte les deux traces de chaque paire aux mêmes identifiants : des identifiants neufs coupent ce
lien), BC4-08 (manifeste hérité de la v3 : `comptes_par_strate` et `regle` faux pour la v4), BC4-06 (le tirage de la
sélection doit se recalculer depuis sa clé : fait ici avant tout).

Ce que fait ce script, et rien d'autre :
1. relit la v3 et son secret, la v4 et son secret et sa clé (empreintes attendues) ; **recalcule la sélection de la v4
   depuis sa clé** (même code que `construction-v4/construire_banque_v4_une_trace_par_paire_v1.py`) et refuse si elle
   diffère des tâches de la v4 ;
2. garde exactement les 176 tâches de la v4 (mêmes champs `famille`, `texte`, `etiquettes`, `verite`, `source`, mêmes
   parts) et leur donne des identifiants neufs `q-0001` à `q-0176` par
   `numpy.random.default_rng(numpy.random.SeedSequence(E5)).permutation(176)` sur les tâches prises dans l'ordre du
   fichier v4 (train, test, test_final) ; chaque part triée par identifiant neuf ; E5 neuve, dans le seul fichier de clé
   `banque-confrontation-v5-cle.json` (secret) ;
3. secret v5 = secret v3 de chaque tâche, plus `id_v3` (et `id_v1`, déjà présent) ;
4. manifeste recalculé : `n`, `comptes_par_strate` (famille|vérité|source|mode × part, comme la v1), règle, dérivation,
   empreinte de la clé.

Usage : python3 -I construire_banque_v5_v1.py DOSSIER_BANQUE DOSSIER_SORTIE
Refuse : numpy < 1.25 ; une empreinte inattendue ; une sélection v4 non retrouvée depuis sa clé ; une sortie existante
(R12). N'imprime jamais une clé.
"""
import datetime, hashlib, json, pathlib, secrets, sys
import numpy as np

ATTENDU = {
    "banque-confrontation-v3.json": "157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d",
    "banque-confrontation-v3-secret.json": "a13217b8c72da77a89d871f012272dff778478dbaeb67607535d26254ea6a427",
    "banque-confrontation-v4.json": "6504045cea95c698f4ba3c702bd30e2ee12fe1e4a79d2ead868a2a438579107d",
    "banque-confrontation-v4-secret.json": "ccf3c3739ab2afbe3806710c19011bef897a44b7e221a12ae3cfc5086eb1ad1b",
    "banque-confrontation-v4-cle.json": "694c358ff7b29dcc468f77fe76ebef75e853f491d9dbb02f092d55ea885ba554",
}
PARTS = ("train", "test", "test_final")
FAM = "controle-delegation"
NOM, NOM_SECRET, NOM_CLE = "banque-confrontation-v5.json", "banque-confrontation-v5-secret.json", "banque-confrontation-v5-cle.json"


def refus(m):
    sys.exit(f"REFUS : {m}")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ecrire(p, c):
    if p.exists() or p.with_name(p.name + ".sha256").exists():
        refus(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    h = sha(p)
    p.with_name(p.name + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def selection_v4(v3, s3, e4):
    """Le tirage du constructeur de la v4, refait à l'identique depuis sa clé."""
    rng = np.random.default_rng(np.random.SeedSequence(e4))
    garde = set()
    for part in ("test", "test_final"):
        paires = {}
        for t in v3[part]:
            if t["famille"] == FAM:
                paires.setdefault((t["source"], s3[t["id"]]["paire"]), []).append(t)
        n_h = n_s = 0
        par_source = {}
        for (src, pid), membres in sorted(paires.items()):
            par_source.setdefault(src, []).append(membres)
        restes = []
        for src in sorted(par_source):
            liste = par_source[src]
            ordre = rng.permutation(len(liste))
            moitie = len(liste) // 2
            for k, i in enumerate(ordre):
                if k < moitie:
                    classe = "honnete"
                elif k < 2 * moitie:
                    classe = "sabotage"
                else:
                    restes.append(liste[i]); continue
                garde.add(next(m["id"] for m in liste[i] if m["verite"] == classe))
                n_h += classe == "honnete"; n_s += classe == "sabotage"
        for membres in restes:
            classe = "honnete" if n_h <= n_s else "sabotage"
            garde.add(next(m["id"] for m in membres if m["verite"] == classe))
            n_h += classe == "honnete"; n_s += classe == "sabotage"
    return garde


def principal(argv):
    if tuple(int(x) for x in np.__version__.split(".")[:2]) < (1, 25):
        refus(f"numpy {np.__version__} < 1.25 (R9)")
    if len(argv) != 2:
        refus("usage : DOSSIER_BANQUE DOSSIER_SORTIE")
    d, sortie = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    lus = {}
    for nom, h in ATTENDU.items():
        p = d / nom
        if sha(p) != h or (d / (nom + ".sha256")).read_text(encoding="utf-8").split()[0] != h:
            refus(f"{nom} : empreinte ou compagnon inattendu")
        lus[nom] = json.loads(p.read_text(encoding="utf-8"))
    v3, s3 = lus["banque-confrontation-v3.json"], lus["banque-confrontation-v3-secret.json"]
    v4, s4, c4 = lus["banque-confrontation-v4.json"], lus["banque-confrontation-v4-secret.json"], lus["banque-confrontation-v4-cle.json"]
    garde = selection_v4(v3, s3, int(c4["entropie_seed_sequence"]))
    garde_v4 = {t["id"] for p in ("test", "test_final") for t in v4[p] if t["famille"] == FAM}
    if garde != garde_v4:
        refus("la sélection de la v4 ne se retrouve pas depuis sa clé")
    taches = [(p, t) for p in PARTS for t in v4[p]]
    n = len(taches)
    e5 = secrets.randbits(128)
    perm = np.random.default_rng(np.random.SeedSequence(e5)).permutation(n)
    nouveaux = [f"q-{int(perm[i]) + 1:04d}" for i in range(n)]
    if len(set(nouveaux)) != n:
        refus("identifiants neufs en double")
    v5 = {p: [] for p in PARTS}
    secret = {}
    for (p, t), nid in zip(taches, nouveaux):
        v5[p].append({"id": nid, **{k: t[k] for k in ("famille", "texte", "etiquettes", "verite", "source")}})
        dossier = dict(s4[t["id"]])
        if "id_v3" in dossier:
            refus("champ id_v3 déjà présent")
        dossier["id_v3"] = t["id"]
        secret[nid] = dossier
    for p in PARTS:
        v5[p].sort(key=lambda x: x["id"])
    secret = {k: secret[k] for k in sorted(secret)}
    # comptes par strate, comme la v1 (essaim_m3/banque.py l. 125) : famille|vérité|source|mode, mode d'après `agentique` du secret
    comptes = {}
    for p in PARTS:
        for t in v5[p]:
            s = secret[t["id"]]
            mode = "agentique" if s.get("agentique") else "conversation"  # comme essaim_m3/banque.py, l. 125
            cle = f"{t['famille']}|{t['verite']}|{t['source']}|{mode}"
            comptes.setdefault(cle, {q: 0 for q in PARTS})[p] += 1
    m = dict(v4["manifeste"])
    m.pop("une_trace_par_paire", None)
    m["nom"] = "confrontation-v5"
    m["quand_utc"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    m["n"] = {p: len(v5[p]) for p in PARTS}
    m["comptes_par_strate"] = {k: comptes[k] for k in sorted(comptes)}
    m["regle"] = ("dérivée de la v4 (sélection d'une trace par paire de controle-delegation en test et en test_final, "
                  "décision N-046), elle-même dérivée de la v3 puis de la v1 (partition par groupes, une paire ne se "
                  "sépare jamais) ; identifiants neufs q-0001…q-0176 tirés par graine, clé secrète ; chaque part triée "
                  "par identifiant ; train gardant ses paires ; les champs secrets sont dans le fichier secret")
    m["identifiants_opaques"] = {
        "derivee_de": {"v4": ATTENDU["banque-confrontation-v4.json"], "v3": ATTENDU["banque-confrontation-v3.json"]},
        "entropie_sha256": hashlib.sha256(str(e5).encode("ascii")).hexdigest(),
        "regle": ("tâches de la v4 dans l'ordre de son fichier (train, test, test_final) ; la tâche de rang i reçoit "
                  "q-{permutation[i] + 1:04d}, permutation = numpy.random.default_rng(numpy.random.SeedSequence(E5)).permutation(176) ; "
                  "E5 dans le seul fichier de clé"),
        "selection_v4_recalculee_depuis_sa_cle": True,
        "script": "construction-v5/construire_banque_v5_v1.py",
        "numpy": np.__version__,
    }
    v5["manifeste"] = m
    sortie.mkdir(parents=True, exist_ok=True)
    h = ecrire(sortie / NOM, {k: v5[k] for k in ("train", "test", "test_final", "manifeste")})
    hs = ecrire(sortie / NOM_SECRET, secret)
    hc = ecrire(sortie / NOM_CLE, {"banque": NOM, "entropie_seed_sequence": str(e5),
                                   "entropie_sha256": m["identifiants_opaques"]["entropie_sha256"]})
    print(json.dumps({"banque_v5": NOM, "sha256": h, "secret_sha256": hs, "cle_sha256": hc, "n": m["n"],
                      "strates": len(comptes)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
