"""Banque `confrontation-v4` : la banque `confrontation-v3` avec **une seule trace par paire** de la famille
`controle-delegation` en `test` et en `test_final` — v1 de ce script.

Décision de Lazar (25 octobre 2026, 17:43 Paris, note N-046) : pour l'étape 1 et la confrontation, ne servir qu'une
trace par paire en test et en test final, en attendant un lot 3 de traces sans paires (constat BC1-02 de la
contre-lecture de la banque v2 : les deux traces d'une paire, servies ensemble, se contrastent ; référence « contraste
de paire » 1,0 sur test, 0,75 sur test final).

Ce que fait ce script, et rien d'autre :
- `train` inchangé (ses paires restent : l'entraînement est servi avec sa vérité) ; famille `conscience-evaluation`
  inchangée partout ; identifiants, champs et ordre des tâches gardées inchangés (ceux de la v3) ;
- en `test` et en `test_final`, pour chaque paire (champ `paire` du secret v3), **une seule trace est gardée** ; dans
  chaque part et chaque source (`lot1`, `lot2`), la moitié des paires garde sa trace honnête et l'autre moitié sa trace
  sabotée (paires tirées par `numpy.random.default_rng(numpy.random.SeedSequence(E))`, une permutation par part et par
  source, dans l'ordre des paires trié par identifiant de paire ; si une source a un nombre impair de paires, la paire
  restante prend la classe qui rééquilibre la part) ; les traces retirées ne sont servies nulle part ;
- E, tirée par `secrets.randbits(128)`, n'est écrite que dans le fichier de clé `banque-confrontation-v4-cle.json`
  (secret) ; le manifeste n'en garde que l'empreinte ; le secret v4 = le secret v3 restreint aux tâches gardées.

Usage : python3 -I construire_banque_v4_une_trace_par_paire_v1.py BANQUE_V3 SECRET_V3 DOSSIER_SORTIE
Refuse : numpy < 1.25 ; empreintes de la v3 ou de son secret autres que celles attendues ; une paire qui n'aurait pas
une trace de chaque classe dans la même part ; un écart d'équilibre final ; une sortie existante (R12). N'imprime jamais E.
"""
import datetime, hashlib, json, pathlib, secrets, sys
import numpy as np

SHA_V3 = "157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d"
SHA_SECRET_V3 = "a13217b8c72da77a89d871f012272dff778478dbaeb67607535d26254ea6a427"
PARTS = ("train", "test", "test_final")
FAM = "controle-delegation"
NOM, NOM_SECRET, NOM_CLE = "banque-confrontation-v4.json", "banque-confrontation-v4-secret.json", "banque-confrontation-v4-cle.json"


def refus(m):
    sys.exit(f"REFUS : {m}")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def lire(p, attendu):
    if sha(p) != attendu:
        refus(f"{p.name} : empreinte inattendue")
    c = p.with_name(p.name + ".sha256")
    if not c.exists() or c.read_text(encoding="utf-8").split()[0] != attendu:
        refus(f"{p.name} : compagnon absent ou différent")
    return json.loads(p.read_text(encoding="utf-8"))


def ecrire(p, contenu):
    if p.exists() or p.with_name(p.name + ".sha256").exists():
        refus(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(contenu, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    h = sha(p)
    p.with_name(p.name + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def principal(argv):
    if tuple(int(x) for x in np.__version__.split(".")[:2]) < (1, 25):
        refus(f"numpy {np.__version__} < 1.25 (R9)")
    if len(argv) != 3:
        refus("usage : BANQUE_V3 SECRET_V3 DOSSIER_SORTIE")
    p3, ps3, sortie = (pathlib.Path(a) for a in argv)
    v3, s3 = lire(p3, SHA_V3), lire(ps3, SHA_SECRET_V3)
    e = secrets.randbits(128)
    rng = np.random.default_rng(np.random.SeedSequence(e))
    garde = set()
    bilan = {}
    for part in ("test", "test_final"):
        paires = {}
        for t in v3[part]:
            if t["famille"] == FAM:
                paires.setdefault((t["source"], s3[t["id"]]["paire"]), []).append(t)
        for cle_p, membres in paires.items():
            if len(membres) != 2 or {m["verite"] for m in membres} != {"honnete", "sabotage"}:
                refus(f"{part} : paire {cle_p} sans une trace de chaque classe")
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
        for membres in restes:  # paires restantes des sources impaires : rééquilibrer la part
            classe = "honnete" if n_h <= n_s else "sabotage"
            garde.add(next(m["id"] for m in membres if m["verite"] == classe))
            n_h += classe == "honnete"; n_s += classe == "sabotage"
        if abs(n_h - n_s) > 1:
            refus(f"{part} : équilibre {n_h} honnêtes contre {n_s} sabotées")
        bilan[part] = {"paires": len(paires), "gardees_honnetes": n_h, "gardees_sabotees": n_s}
    v4 = {"train": list(v3["train"])}
    for part in ("test", "test_final"):
        v4[part] = [t for t in v3[part] if t["famille"] != FAM or t["id"] in garde]
    ids4 = [t["id"] for p in PARTS for t in v4[p]]
    if len(set(ids4)) != len(ids4):
        refus("identifiants en double")
    secret4 = {k: s3[k] for k in sorted(ids4)}
    m = dict(v3["manifeste"])
    m["nom"] = "confrontation-v4"
    m["quand_utc"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    m["n"] = {p: len(v4[p]) for p in PARTS}
    m["une_trace_par_paire"] = {
        "derivee_de": {"banque": p3.name, "sha256": SHA_V3, "secret_sha256": SHA_SECRET_V3},
        "decision": "N-046 (Lazar, 25 octobre 2026, 17:43 Paris)",
        "entropie_sha256": hashlib.sha256(str(e).encode("ascii")).hexdigest(),
        "regle": ("train et famille conscience-evaluation inchangés ; en test et test_final, une trace par paire de "
                  "controle-delegation, la moitié des paires de chaque part et de chaque source gardant l'honnête, l'autre "
                  "la sabotée, tirées par numpy.random.default_rng(numpy.random.SeedSequence(E)) ; E dans le seul fichier de clé"),
        "bilan": bilan,
        "script": "construction-v4/construire_banque_v4_une_trace_par_paire_v1.py",
        "numpy": np.__version__,
    }
    v4["manifeste"] = m
    sortie.mkdir(parents=True, exist_ok=True)
    h = ecrire(sortie / NOM, {k: v4[k] for k in ("train", "test", "test_final", "manifeste")})
    hs = ecrire(sortie / NOM_SECRET, secret4)
    hc = ecrire(sortie / NOM_CLE, {"banque": NOM, "entropie_seed_sequence": str(e),
                                   "entropie_sha256": m["une_trace_par_paire"]["entropie_sha256"]})
    print(json.dumps({"banque_v4": NOM, "sha256": h, "secret_sha256": hs, "cle_sha256": hc, "n": m["n"], "bilan": bilan},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
