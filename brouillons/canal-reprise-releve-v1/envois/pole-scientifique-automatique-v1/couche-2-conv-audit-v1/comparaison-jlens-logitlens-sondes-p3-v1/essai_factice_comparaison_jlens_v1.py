"""Essai de bout en bout, sur tenseurs factices, de `comparaison_jlens_logitlens_sondes_p3_v1.py` — v1.

Largeur 64, vocabulaire 500, couches 7, 15 et 23. Aucun poids réel, aucune lecture de `donnees/`.

Le fichier de poids des sondes est écrit **par le code du dépôt** : `ecrire_sondes` de
`src/controle_ia/premier_test_ia/figees.py` et les classes de `src/controle_ia/sondes/familles.py`, extraites par l'arbre
syntaxique (le module importe torch, absent ici ; les fonctions extraites n'en ont pas besoin). Le format testé est donc
celui que P3 a réellement écrit, et `lire_sondes` du dépôt relit le fichier factice (contrôle croisé).

Signaux plantés (pour vérifier que la mesure voit ce qu'elle doit voir, et pas ce qu'elle ne doit pas voir, R5) :
- tromperie, couche 15 : w = J₁₅⁻¹ · (direction du concept) — visible par la lentille jacobienne seulement ;
- tromperie, couche 23 : J₂₃ ≈ identité, même plantation — les deux lentilles doivent s'accorder ;
- enjeux, couche 15 : w = direction du concept dans l'espace de sortie — visible par la lentille des logits seulement ;
- autres sondes et couche 7 : directions aléatoires — rien ne doit sortir.
Puis les refus nommés : entrée absente, couche absente de la lentille, poids de sondes altérés, sceau du JSON faux,
sortie existante, largeur discordante, lentille .pt sans torch.

Usage : python3 -I -B essai_factice_comparaison_jlens_v1.py --dossier <dossier neuf> [--depot <racine du dépôt>]
Graines : numpy.random.SeedSequence(20261029) dérivée par étiquette (R9).
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import struct
import subprocess
import sys
import types
from dataclasses import dataclass, field  # noqa: F401  (espace de noms des classes extraites)
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "comparaison_jlens_logitlens_sondes_p3_v1.py"
D, V = 64, 500
GRAINE = 20261029


def rng(etiquette):
    cle = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "little")
    return np.random.default_rng(np.random.SeedSequence(entropy=GRAINE, spawn_key=(cle,)))


# ---------------------------------------------------------------- code du dépôt, extrait sans torch
class GardeArret(Exception):
    pass


def extraire(chemin: Path, noms: set[str], espace: dict) -> None:
    arbre = ast.parse(chemin.read_text(encoding="utf-8"))
    garde = [n for n in arbre.body if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in noms)
             or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in noms for t in n.targets))]
    manquants = noms - {getattr(n, "name", None) or n.targets[0].id for n in garde}
    if manquants:
        raise SystemExit(f"extraction : {manquants} introuvables dans {chemin}")
    futur = [n for n in arbre.body if isinstance(n, ast.ImportFrom) and n.module == "__future__"]
    module = types.ModuleType(f"extrait_{chemin.stem}")       # module enregistré : exigé par dataclass
    module.__dict__.update(espace)
    sys.modules[module.__name__] = module
    exec(compile(ast.Module(body=futur + garde, type_ignores=[]), str(chemin), "exec"), module.__dict__)
    espace.update({k: v for k, v in module.__dict__.items() if not k.startswith("__")})


def code_du_depot(depot: Path) -> dict:
    esp = {"np": np, "hashlib": hashlib, "json": json, "Path": Path, "GardeArret": GardeArret,
           "dataclass": dataclass, "field": field, "__name__": "extrait"}
    extraire(depot / "src/controle_ia/sondes/familles.py",
             {"_empreinte", "SondeLineaireJetons", "SondePerceptron", "SondeMahalanobis"}, esp)
    esp["SondeLineaire"] = None
    esp["_empreinte_familles"] = esp["_empreinte"]

    def sceller(chemin):
        sha = hashlib.sha256(Path(chemin).read_bytes()).hexdigest()
        Path(str(chemin) + ".sha256").write_text(f"{sha}  {Path(chemin).name}\n", encoding="utf-8")
        return sha

    def verifier(chemin):
        return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()

    esp_f = dict(esp, sceller=sceller, verifier=verifier)
    extraire(depot / "src/controle_ia/premier_test_ia/figees.py", {"TABLEAUX", "_empreinte", "ecrire_sondes", "lire_sondes"},
             esp_f)
    esp_f["CLASSES"] = None
    return esp_f


# ---------------------------------------------------------------- vocabulaire byte-level et safetensors
def octets_vers_unicode():
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs, n = bs[:], 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, (chr(c) for c in cs)))


def encoder_bl(texte: str) -> str:
    t = octets_vers_unicode()
    return "".join(t[b] for b in texte.encode("utf-8"))


def ecrire_safetensors(chemin: Path, tenseurs: dict):
    entete, morceaux, pos = {"__metadata__": {"format": "pt"}}, [], 0
    for nom, (x, dt) in tenseurs.items():
        if dt == "BF16":
            u = np.ascontiguousarray(x, dtype=np.float32).view(np.uint32)
            octets = ((u + 0x7FFF + ((u >> 16) & 1)) >> 16).astype("<u2").tobytes()   # arrondi au plus proche pair
        else:
            octets = np.ascontiguousarray(x, dtype="<f4").tobytes()
        entete[nom] = {"dtype": dt, "shape": list(x.shape), "data_offsets": [pos, pos + len(octets)]}
        morceaux.append(octets)
        pos += len(octets)
    h = json.dumps(entete).encode()
    h += b" " * (-len(h) % 8)
    with open(chemin, "wb") as f:
        f.write(struct.pack("<Q", len(h)) + h + b"".join(morceaux))


def bf16(x):
    u = np.ascontiguousarray(x, dtype=np.float32).view(np.uint32)
    return (((u + 0x7FFF + ((u >> 16) & 1)) >> 16) << 16).astype(np.uint32).view(np.float32)


# ---------------------------------------------------------------- construction des entrées factices
def construire(e: Path, depot: Path, concepts: dict) -> dict:
    code = code_du_depot(depot)
    S, P = code["SondeLineaireJetons"], code["SondePerceptron"]
    e.mkdir(parents=True)
    (e / "modele").mkdir()

    # Vocabulaire : 3 spéciaux, mots des concepts (avec et sans espace), « café » (test des octets), syllabes, ponctuation
    jetons = ["<|begin_of_text|>", "<|eot_id|>", "<|reserved_special_token_0|>"]
    for c in ("tromperie", "enjeux"):
        for m in concepts[c][:14]:
            jetons += [" " + m, m]
    jetons += [" café", ",", ".", " the", "\n", "!!"]
    syll = ["ka", "lo", "mi", "ter", "sun", "pra", "vel", "dor", "qui", "zen", "bar", "fo", "nex", "ul", "ri"]
    r = rng("vocabulaire")
    tous = {m.lower() for c in concepts if not c.startswith("_") for m in concepts[c]}
    while len(jetons) < V:
        t = ("" if r.random() < 0.3 else " ") + "".join(r.choice(syll, size=r.integers(1, 4)))
        if t.strip().lower() not in tous and t not in jetons:
            jetons.append(t)
    vocab = {encoder_bl(t): i for i, t in enumerate(jetons) if i >= 3}
    tok = {"version": "1.0", "added_tokens": [{"id": i, "content": jetons[i], "special": True} for i in range(3)],
           "pre_tokenizer": {"type": "ByteLevel"}, "decoder": {"type": "ByteLevel"},
           "model": {"type": "BPE", "vocab": vocab, "merges": []}}
    (e / "modele" / "tokenizer.json").write_text(json.dumps(tok, ensure_ascii=False), encoding="utf-8")

    # Poids de sortie (désembedding en bf16 dans le second fragment, norme en f32 dans le premier)
    WU = bf16(rng("desembedding").normal(size=(V, D)) / 8.0)
    g = (1.0 + 0.1 * rng("norme").normal(size=D)).astype(np.float32)
    ecrire_safetensors(e / "modele" / "model-00001-of-00002.safetensors", {"model.norm.weight": (g, "F32")})
    ecrire_safetensors(e / "modele" / "model-00002-of-00002.safetensors", {"lm_head.weight": (WU, "BF16")})
    (e / "modele" / "model.safetensors.index.json").write_text(json.dumps({"weight_map": {
        "model.norm.weight": "model-00001-of-00002.safetensors", "lm_head.weight": "model-00002-of-00002.safetensors"}}))

    # Lentille : J7 orthogonale, J15 = 1,3 × orthogonale, J23 ≈ identité ; stockée en float16 (comme le dépôt)
    def ortho(et):
        q, rr = np.linalg.qr(rng(et).normal(size=(D, D)))
        return q * np.sign(np.diag(rr))
    J = {7: ortho("J7"), 15: 1.3 * ortho("J15"), 23: np.eye(D) + 0.03 * rng("J23").normal(size=(D, D))}
    J = {c: m.astype(np.float16) for c, m in J.items()}
    with open(e / "lentille-factice.npz", "wb") as f:
        np.savez(f, **{f"J_{c}": m for c, m in J.items()}, n_prompts=np.array(1000), d_model=np.array(D),
                 source_layers=np.arange(31))
    with open(e / "lentille-sans-c23.npz", "wb") as f:
        np.savez(f, J_7=J[7], J_15=J[15], n_prompts=np.array(1000), d_model=np.array(D))
    with open(e / "desembedding-largeur-fausse.npy", "wb") as f:
        np.save(f, WU[:, :48])
    (e / "lentille-vide.pt").write_bytes(b"")

    # Directions plantées
    Jf = {c: m.astype(np.float64) for c, m in J.items()}
    ids = {c: [i for i, t in enumerate(jetons) if t.strip().lower() in {m.lower() for m in concepts[c]}]
           for c in ("tromperie", "enjeux")}
    WU64 = WU.astype(np.float64)
    cible = {c: (WU64[ids[c]].mean(0) - WU64.mean(0)) / g for c in ids}       # u tel que g ⊙ u ∝ c̄ − m

    def bruit(et, echelle):
        x = rng(et).normal(size=D)
        return echelle * x / np.linalg.norm(x)
    plant = {
        ("tromperie", 15): np.linalg.solve(Jf[15], cible["tromperie"]),
        ("tromperie", 23): np.linalg.solve(Jf[23], cible["tromperie"]),
        ("enjeux", 15): cible["enjeux"].copy(),
    }
    sondes, aires, durees, pertes = [], {"tromperie": {}, "enjeux": {}}, {"tromperie": {}, "enjeux": {}}, {"tromperie": {}, "enjeux": {}}
    princ = {"tromperie": "tromperie-difference_moyennes-c15", "enjeux": "enjeux-lineaire-c15"}
    familles = ["difference_moyennes", "lineaire", "perceptron", "attention", "mahalanobis"]
    entrees_json = []
    for concept in ("tromperie", "enjeux"):
        for fam in familles:
            for c in (7, 15, 23):
                nom = f"{concept}-{fam}-c{c}"
                w0 = plant.get((concept, c)) if nom.rsplit("-", 1)[0] == princ[concept].rsplit("-", 1)[0] else None
                if w0 is not None:
                    w = w0 + bruit("bruit/" + nom, 0.15 * np.linalg.norm(w0))
                else:
                    w = rng("w/" + nom).normal(size=D)
                if fam == "mahalanobis":
                    classe = "SondeMahalanobis"           # absente du fichier léger, comme dans P3
                    emp = code["_empreinte_familles"](f"mahalanobis:{nom}", c, "max", np.zeros(D), np.eye(D))
                elif fam == "perceptron":
                    rr = rng("p/" + nom)
                    s = P(nom, c, "max", rr.normal(size=D), np.abs(rr.normal(size=D)) + 0.5, rr.normal(size=(4, D)),
                          rr.normal(size=4), rr.normal(size=4), float(rr.normal()), None, "perceptron")
                    sondes.append(s)
                    classe, emp = "SondePerceptron", s.empreinte()
                else:
                    q = rng("q/" + nom).normal(size=D) if fam == "attention" else None
                    s = S(nom, c, "attention" if fam == "attention" else "max", w, float(rng("b/" + nom).normal()), q, fam)
                    sondes.append(s)
                    classe, emp = "SondeLineaireJetons", s.empreinte()
                entrees_json.append({"agregation": "attention" if fam == "attention" else "max", "classe": classe,
                                     "couche": c, "empreinte": emp, "famille": fam, "nom": nom})
                aires[concept][nom] = 0.5
    planchers = {}
    for concept in ("tromperie", "enjeux"):
        L = rng("L/" + concept).normal(size=(D, D)) / 8.0
        planchers[concept] = []
        for k in range(20):
            nom = f"{princ[concept]}-plancher-plancher-{k}"
            s = S(nom, 15, "max", L @ rng(f"pl/{concept}/{k}").normal(size=D), 0.0, None, "plancher")
            sondes.append(s)
            planchers[concept].append(nom)
            entrees_json.append({"agregation": "max", "classe": "SondeLineaireJetons", "couche": 15,
                                 "empreinte": s.empreinte(), "famille": "plancher", "nom": nom})
    sha_leg = code["ecrire_sondes"](e / "sondes-figees-legeres.npz", sondes,
                                    {"principales": princ, "planchers": planchers, "complet": "0" * 64})
    relues, meta, _ = code["lire_sondes"](e / "sondes-figees-legeres.npz", sha_leg)      # contrôle croisé par le dépôt
    assert len(relues) == len(sondes) and meta["principales"] == princ
    fig = {"manifeste_sha256": "0" * 64, "run_id": "essai-factice-jlens-v1",
           "resultat": {"aires_validation": aires, "familles": familles, "principales": princ, "sondes": entrees_json,
                        "sondes_figees_sha256": "0" * 64, "sondes_legeres_sha256": sha_leg}}
    p = e / "sondes-figees.json"
    p.write_text(json.dumps(fig, ensure_ascii=False, indent=1), encoding="utf-8")
    p.with_name(p.name + ".sha256").write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")

    # Variantes facultatives : variances diagonales et activations moyennes factices
    with open(e / "variances-factices.npz", "wb") as f:
        np.savez(f, **{f"c{c}": 0.5 + rng(f"var{c}").random(D) for c in (7, 15, 23)})
    with open(e / "activations-moyennes-factices.npz", "wb") as f:
        np.savez(f, **{f"c{c}": 3.0 * rng(f"moy{c}").normal(size=D) for c in (7, 15, 23)})
    return {"ids": ids, "jetons": jetons}


# ---------------------------------------------------------------- exécution et contrôles
def lancer(args, journal, cwd):
    cmd = [sys.executable, "-I", "-B", str(SCRIPT), *args]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    journal.append(f"$ python3 -I -B {SCRIPT.name} {' '.join(args)}\n  code {r.returncode}\n  "
                   f"{(r.stdout + r.stderr).strip()}")
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--depot", default=str(ICI.parents[5]))
    a = ap.parse_args()
    dossier, depot = Path(a.dossier).resolve(), Path(a.depot).resolve()
    if dossier.exists():
        raise SystemExit(f"{dossier} existe déjà (R12)")
    concepts = json.loads((ICI / "concepts-sondes-p3-v1.json").read_text(encoding="utf-8"))
    e, s = dossier / "entrees", dossier / "sortie"
    info = construire(e, depot, concepts)
    s.mkdir(parents=True)
    journal, controles = [], []

    def ok(nom, cond, detail=""):
        controles.append(f"{'OK' if cond else 'KO'}  {nom}{' — ' + detail if detail else ''}")

    base = ["comparer", "--sondes-json", str(e / "sondes-figees.json"), "--sondes-npz", str(e / "sondes-figees-legeres.npz"),
            "--lentille", str(e / "lentille-factice.npz"),
            "--desembedding", f"{e / 'modele' / 'model.safetensors.index.json'}:lm_head.weight",
            "--norme-finale", f"{e / 'modele' / 'model.safetensors.index.json'}:model.norm.weight",
            "--vocabulaire", str(e / "modele" / "tokenizer.json"), "--concepts", str(ICI / "concepts-sondes-p3-v1.json")]

    def avec(liste, cle, valeur):
        l = list(liste)
        l[l.index(cle) + 1] = valeur
        return l

    cwd = str(dossier)       # lancé depuis un autre dossier que celui du script
    r = lancer(base + ["--sortie", str(s / "sortie-factice-v1.json")], journal, cwd)
    ok("run sain : code 0", r.returncode == 0, r.stderr.strip()[:300])
    out = json.loads((s / "sortie-factice-v1.json").read_text(encoding="utf-8"))
    par_nom = {x["nom"]: x for x in out["sondes"]}
    ok("sondes retenues : famille de la principale × 3 couches × 2 concepts", sorted(par_nom) == sorted(
        [f"tromperie-difference_moyennes-c{c}" for c in (7, 15, 23)] + [f"enjeux-lineaire-c{c}" for c in (7, 15, 23)]))

    def coh(nom, lentille, concept, var="direction"):
        return par_nom[nom]["variantes"][var][lentille]["coherence"][concept]

    t15j, t15l = coh("tromperie-difference_moyennes-c15", "jacobienne", "tromperie"), \
        coh("tromperie-difference_moyennes-c15", "logits", "tromperie")
    ok("tromperie c15 plantée sous J : lentille jacobienne la voit (p_haut ≤ 0,01 contre aléatoires et planchers, "
       "≥ 5 jetons du concept en tête)",
       t15j["aleatoires"]["p_haut"] <= 0.01 and t15j["planchers"]["p_haut"] <= 0.05 and t15j["n_concept_tete_plus"] >= 5,
       f"z={t15j['z']:.2f}, p={t15j['aleatoires']['p_haut']:.4f}, plancher p={t15j['planchers']['p_haut']:.3f}, "
       f"n={t15j['n_concept_tete_plus']}")
    ok("tromperie c15 : lentille des logits ne la voit pas (p_bilatéral > 0,05, ≤ 2 jetons en tête)",
       t15l["aleatoires"]["p_bilateral"] > 0.05 and t15l["n_concept_tete_plus"] <= 2,
       f"z={t15l['z']:.2f}, p={t15l['aleatoires']['p_bilateral']:.3f}, n={t15l['n_concept_tete_plus']}")
    e15j, e15l = coh("enjeux-lineaire-c15", "jacobienne", "enjeux"), coh("enjeux-lineaire-c15", "logits", "enjeux")
    ok("enjeux c15 plantée en sortie : lentille des logits la voit, la jacobienne non",
       e15l["aleatoires"]["p_haut"] <= 0.01 and e15j["aleatoires"]["p_bilateral"] > 0.05,
       f"logits z={e15l['z']:.2f} p={e15l['aleatoires']['p_haut']:.4f} ; jacobienne z={e15j['z']:.2f} "
       f"p_bil={e15j['aleatoires']['p_bilateral']:.3f}")
    rec23 = par_nom["tromperie-difference_moyennes-c23"]["variantes"]["direction"]["recouvrement"]
    ok("tromperie c23 (J ≈ identité) : les deux lentilles s'accordent (≥ 12/20 en tête +, cosinus > 0,9)",
       rec23["plus"]["intersection"] >= 12 and rec23["cosinus_logits_centres"] > 0.9,
       f"intersection {rec23['plus']['intersection']}, cosinus {rec23['cosinus_logits_centres']:.3f}")
    nuls = [coh(f"{c}-c7", l, k)["aleatoires"]["p_bilateral"] for c, k in
            (("tromperie-difference_moyennes", "tromperie"), ("enjeux-lineaire", "enjeux")) for l in ("logits", "jacobienne")]
    ok("couche 7 aléatoire : aucun p bilatéral ≤ 0,01", min(nuls) > 0.01, f"p = {[round(x, 3) for x in nuls]}")
    ok("planchers lus à la couche 15 (20), absents aux couches 7 et 23",
       t15j["planchers"]["n"] == 20 and "statut" in coh("tromperie-difference_moyennes-c7", "jacobienne", "tromperie")["planchers"])
    bloc = par_nom["enjeux-lineaire-c15"]["variantes"]["direction"]["logits"]
    ok("signe : têtes « plus » et « moins » disjointes, logits de tête de signes opposés",
       not ({t["id"] for t in bloc["plus"]["tete"]} & {t["id"] for t in bloc["moins"]["tete"]})
       and bloc["plus"]["tete"][-1]["logit"] > 0 and bloc["moins"]["tete"][-1]["logit"] > 0)
    voc_cafe = out["concepts"]["tromperie"]["jetons"]
    import importlib.util
    spec = importlib.util.spec_from_file_location("comparaison_v1", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    textes, _ = mod.lire_vocabulaire(e / "modele" / "tokenizer.json", V)
    toks = json.loads((e / "modele" / "tokenizer.json").read_text(encoding="utf-8"))
    cle_cafe = encoder_bl(" café")
    ok("décodage par octets : le jeton « ĠcafÃ© » de tokenizer.json est relu « café » (avec l'espace)",
       textes[toks["model"]["vocab"][cle_cafe]] == " café", f"{cle_cafe!r} → {textes[toks['model']['vocab'][cle_cafe]]!r}")
    ok("vocabulaire : jetons spéciaux relus, masque « mots » les exclut",
       textes[0] == "<|begin_of_text|>" and not mod.masque_mots(textes)[0] and mod.masque_mots(textes)[3])
    ok("concepts : jetons trouvés, mots absents listés", len(voc_cafe) > 0 and isinstance(out["concepts"]["tromperie"]["mots_sans_jeton"], list),
       f"{len(voc_cafe)} jetons tromperie, {len(out['concepts']['tromperie']['mots_sans_jeton'])} mots sans jeton")
    man = json.loads((s / "sortie-factice-v1-manifeste.json").read_text(encoding="utf-8"))
    ok("manifeste : empreinte de la sortie juste, entrées empreintées, graines consignées",
       man["sortie"]["sha256"] == hashlib.sha256((s / "sortie-factice-v1.json").read_bytes()).hexdigest()
       and "lentille" in man["entrees"] and "aleatoire/c15" in man["graines"])
    r2 = subprocess.run(["sha256sum", "-c", "sortie-factice-v1.json.sha256", "sortie-factice-v1-manifeste.json.sha256"],
                        cwd=s, capture_output=True, text=True)
    ok("empreintes compagnons vérifiables par sha256sum -c", r2.returncode == 0, r2.stdout.strip().replace("\n", " ; "))

    r = lancer(base + ["--sortie", str(s / "sortie-factice-v1-bis.json")], journal, cwd)
    ok("déterminisme : deuxième run, sortie identique octet pour octet", r.returncode == 0 and
       (s / "sortie-factice-v1.json").read_bytes() == (s / "sortie-factice-v1-bis.json").read_bytes())

    r = lancer(base + ["--covariances", str(e / "variances-factices.npz"), "--activations-moyennes",
                       str(e / "activations-moyennes-factices.npz"), "--sondes", "toutes-lineaires",
                       "--sortie", str(s / "sortie-factice-variantes-v1.json")], journal, cwd)
    ok("variantes « motif » et « autour », toutes les sondes linéaires : code 0", r.returncode == 0, r.stderr.strip()[:300])
    if r.returncode == 0:
        ov = json.loads((s / "sortie-factice-variantes-v1.json").read_text(encoding="utf-8"))
        ok("variantes : 18 sondes (3 familles linéaires × 3 couches × 2), trois variantes chacune",
           len(ov["sondes"]) == 18 and all(set(x["variantes"]) == {"direction", "motif", "autour"} for x in ov["sondes"]))

    # Refus nommés
    def refus(nom, args, code_attendu):
        r = lancer(args, journal, cwd)
        ok(f"refus {nom} : code 2 et « REFUS {code_attendu} »", r.returncode == 2 and f"REFUS {code_attendu}" in r.stderr,
           r.stderr.strip()[:200])
    refus("entrée absente", avec(base, "--lentille", str(e / "absente.npz")) + ["--sortie", str(s / "x1.json")],
          "entree-absente")
    refus("couche absente de la lentille", avec(base, "--lentille", str(e / "lentille-sans-c23.npz"))
          + ["--sortie", str(s / "x2.json")], "couche-absente-lentille")
    refus("lentille .pt sans torch", avec(base, "--lentille", str(e / "lentille-vide.pt")) + ["--sortie", str(s / "x3.json")],
          "torch-absent-pour-pt")
    refus("largeur discordante", avec(base, "--desembedding", str(e / "desembedding-largeur-fausse.npy"))
          + ["--sortie", str(s / "x4.json")], "dimension")
    refus("sortie existante", base + ["--sortie", str(s / "sortie-factice-v1.json")], "sortie-existe")
    alt = dossier / "altere"
    alt.mkdir()
    b = bytearray((e / "sondes-figees-legeres.npz").read_bytes())
    b[len(b) // 2] ^= 1
    (alt / "sondes-figees-legeres.npz").write_bytes(bytes(b))
    refus("poids de sondes altérés", avec(base, "--sondes-npz", str(alt / "sondes-figees-legeres.npz"))
          + ["--sortie", str(s / "x5.json")], "empreinte-sondes-npz")
    fj = json.loads((e / "sondes-figees.json").read_text(encoding="utf-8"))
    fj["resultat"]["principales"]["enjeux"] = "enjeux-difference_moyennes-c15"
    (alt / "sondes-figees.json").write_text(json.dumps(fj, ensure_ascii=False, indent=1), encoding="utf-8")
    (alt / "sondes-figees.json.sha256").write_text((e / "sondes-figees.json.sha256").read_text().replace(
        "sondes-figees.json", "sondes-figees.json"))
    refus("sceau du JSON faux (JSON modifié, sceau ancien)", avec(base, "--sondes-json", str(alt / "sondes-figees.json"))
          + ["--sortie", str(s / "x6.json")], "sceau-faux")
    absents = [p.name for p in s.iterdir() if p.name.startswith("x")]
    ok("aucun refus n'a laissé de sortie", not absents, str(absents))

    ko = [c for c in controles if c.startswith("KO")]
    texte = (f"Essai factice v1 — largeur {D}, vocabulaire {V}, graine {GRAINE}\n"
             f"Dépôt (code extrait) : {depot}\n\n" + "\n".join(controles)
             + f"\n\nBILAN : {len(controles) - len(ko)}/{len(controles)} contrôles OK\n\n--- commandes ---\n"
             + "\n".join(journal) + "\n")
    texte = texte.replace(str(dossier), "<essai>").replace(str(ICI), "<dossier>").replace(str(depot), "<depot>")
    (dossier / "journal-essai-factice-v1.txt").write_text(texte, encoding="utf-8")
    print(texte.split("--- commandes ---")[0])
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
