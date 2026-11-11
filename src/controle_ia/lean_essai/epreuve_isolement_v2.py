"""Épreuve d'isolement et essais R5 des gardes sur la chaîne installée — essai Lean (D-1a), v2.

v2 (contre-lecture `2077ae26…`, R-2300) : exécuteur et gardes v2 ; artefacts `artefacts_r5_v2/` (CLL-01 à CLL-04) ; le
bac exige un réseau sortant éprouvé fermé (CLL-13) ; champ « observer » des attendus : garde relevée sans être jugée (comportement
de Lean à établir sur la machine, par exemple l'exécution d'un initialiseur à l'import, CLL-04) ; processus résiduels de
`bac` relevés à la fin sans arrêt global (CLL-07). La v1 reste telle quelle (R12).

Tourne **sur la machine**, en root, **après** la coupure du réseau sortant et sa sonde (brouillon 3, § 4.5, VL-05 ; A1). Autonome
(bibliothèque standard, `executeur_bac_v2`, `gardes_lean_v2`, `sonde_reseau_v1`). Lit `artefacts_r5_v2/attendus-v2.json` et,
pour chaque cas :
- Lean (gardes G-L1 à G-L7) : verdict des gardes contre l'attendu (accepté ou non ; gardes qui doivent échouer ; gardes qui
  doivent passer ; contenus des énoncés et impressions ; axiomes ; sortie de l'agent ignorée) ;
- isolement (Lean et Python) : chaque tentative écrite par l'artefact (« ISOLEMENT <nom> ECHEC|REUSSI … ») contre l'attendu ;
- limites (Python, avec des limites réduites) : arrêt par le bac.
Contrôles côté hôte, indépendants des artefacts : jeton du fichier leurre absent de toutes les sorties ; manifeste de
`/opt/elan`, `/opt/mathlib`, `/opt/pybac`, `/opt/harnais` identique avant et après ; aucun fichier piège sur l'hôte ;
`/srv/items`, `/srv/sorties` vides à la fin ; aucun processus résiduel de `bac`.
Code 0 si tout est conforme, 1 sinon ; le rapport JSON est écrit sur la sortie standard.

`mesurer` : temps et mémoire de l'item sain, trois fois de suite puis trois en parallèle (parallélisme du pilote, § 3.3).
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import secrets
import sys
import time
from dataclasses import replace
from pathlib import Path

if __package__:
    from . import executeur_bac_v2 as X
else:
    sys.dont_write_bytecode = True  # aucun .pyc dans /opt/harnais (manifeste de l'épreuve)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import executeur_bac_v2 as X  # noqa: E402

VERSION = "epreuve_isolement_v2"
LEURRE = Path("/srv/leurre/leurre-v1.txt")
RACINES_MANIFESTE = ("/opt/elan", "/opt/mathlib", "/opt/pybac", "/opt/harnais")
PIEGES_HOTE = ("/opt/mathlib/Piege-v1.txt", "/opt/mathlib/.lake/build/lib/lean/Piege.olean", "/opt/elan/Piege-v1.txt",
               "/usr/Piege-v1.txt", "/opt/harnais/Piege-v1.txt", "/srv/controle/piege.lean", "/tmp/persistance-v1.txt",
               "/tmp/persistance-py-v1.txt")
RE_TENTATIVE = re.compile(r"ISOLEMENT (\S+) (ECHEC|REUSSI)")
LIMITES_ESSAI = {"memoire_max": "512M", "taches_max": 32, "cpu_max_s": 5, "duree_max_s": 10}


def manifeste(racines=RACINES_MANIFESTE) -> str:
    h = hashlib.sha256()
    for racine in racines:
        for dossier, sous, fichiers in os.walk(racine, followlinks=False):
            sous.sort()
            for nom in sorted(fichiers) + sorted(sous):
                p = os.path.join(dossier, nom)
                st = os.lstat(p)
                h.update(f"{p}\0{st.st_size}\0{st.st_mtime_ns}\0{st.st_mode}\n".encode("utf-8", "surrogateescape"))
    return h.hexdigest()


def tentatives(texte: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in RE_TENTATIVE.finditer(texte)}


def juger_lean(cas: dict, res: dict) -> list[str]:
    v = res["verdict"]
    ecarts = []
    if v["accepte_gardes"] != cas["accepte"]:
        ecarts.append(f"accepte_gardes {v['accepte_gardes']} ≠ {cas['accepte']} ; motifs "
                      f"{ {g: x['motifs'] for g, x in v['gardes'].items() if x['motifs']} }")
    for g in cas.get("echecs", []):
        if v["gardes"][g]["ok"]:
            ecarts.append(f"{g} devait échouer")
    for g in cas.get("passent", []):
        if not v["gardes"][g]["ok"]:
            ecarts.append(f"{g} devait passer : {v['gardes'][g]['motifs']}")
    for nom, morceaux in cas.get("enonce_contient", {}).items():
        texte = v["enonces_imprimes"].get(nom, "")
        ecarts += [f"énoncé de {nom} sans « {x} » : {texte!r}" for x in morceaux if x not in texte]
    for nom, morceaux in cas.get("impression_contient", {}).items():
        texte = v["impressions"].get(nom, "")
        ecarts += [f"impression de {nom} sans « {x} » : {texte!r}" for x in morceaux if x not in texte]
    for nom, axiomes in cas.get("axiomes_contient", {}).items():
        lus = v["axiomes"].get(nom) or []
        ecarts += [f"axiomes de {nom} sans {a} : {lus}" for a in axiomes if a not in lus]
    for x in cas.get("sortie_agent_contient", []):
        if x not in res["sortie_compilation"]:
            ecarts.append(f"sortie de l'agent sans « {x} »")
    for nom, morceaux in cas.get("enonce_sans_notation_contient", {}).items():
        texte = v["enonces_sans_notation"].get(nom, "")
        ecarts += [f"énoncé sans notation de {nom} sans « {x} » : {texte!r}" for x in morceaux if x not in texte]
    return ecarts


def observer(cas: dict, res: dict) -> dict:
    """Gardes relevées sans être jugées (comportement de Lean à établir sur la machine)."""
    v = res["verdict"]["gardes"]
    return {g: {"ok": v[g]["ok"], "motifs": v[g]["motifs"][:5]} for g in cas.get("observer", [])}


def juger_tentatives(cas: dict, texte: str) -> list[str]:
    vues = tentatives(texte)
    return [f"tentative {nom} : {vues.get(nom, 'absente')}, {attendu} attendu"
            for nom, attendu in cas["tentatives"].items() if vues.get(nom) != attendu]


def juger_python(cas: dict, res: dict) -> list[str]:
    ecarts = []
    code = res["execution"]["code"]
    if "code" in cas and code != cas["code"]:
        ecarts.append(f"code {code} ≠ {cas['code']} ; stderr {res['stderr'][-300:]!r}")
    if cas.get("code_non_nul") and code == 0:
        ecarts.append("code nul, arrêt par le bac attendu")
    ecarts += [f"stdout sans « {x} »" for x in cas.get("stdout_contient", []) if x not in res["stdout"]]
    ecarts += [f"stdout avec « {x} »" for x in cas.get("stdout_absent", []) if x in res["stdout"]]
    if "incident_attendu" in cas and res.get("incident_bac") != cas["incident_attendu"]:
        ecarts.append(f"incident du bac {res.get('incident_bac')!r}, {cas['incident_attendu']!r} attendu")
    if "duree_max_s" in cas and (res["execution"]["duree_murale_s"] or 0) > cas["duree_max_s"]:
        ecarts.append(f"durée murale {res['execution']['duree_murale_s']} > {cas['duree_max_s']}")
    return ecarts


def epreuve(cfg: X.Config, artefacts: Path) -> dict:
    if cfg.mode != "bac":
        raise X.ErreurBac("l'épreuve d'isolement n'a de sens qu'en mode « bac » (lanceur isolé)")
    attendus = json.loads((artefacts / "attendus-v2.json").read_text(encoding="utf-8"))
    LEURRE.parent.mkdir(mode=0o700, exist_ok=True)
    jeton = "leurre-" + secrets.token_hex(16)
    LEURRE.write_text(jeton + "\n", encoding="utf-8")
    os.chmod(LEURRE, 0o600)
    avant = manifeste()
    bac = X.Bac(cfg)
    cas_rendus, sorties = [], []

    def noter(genre, cas, res, ecarts):
        sorties.append(json.dumps(res, ensure_ascii=False))
        if res.get("processus_residuels"):
            ecarts.append(f"processus résiduels {res['processus_residuels']}")
        if res.get("dossiers_restants"):
            ecarts.append(f"dossiers restants {res['dossiers_restants']}")
        if not res.get("isolement"):
            ecarts.append("exécuté sans isolement")
        if res.get("incident_bac") and not cas.get("incident_attendu"):
            ecarts.append(f"incident du bac {res['incident_bac']}")
        cas_rendus.append({"genre": genre, "nom": cas.get("nom", cas["fichier"]), "ok": not ecarts, "ecarts": ecarts,
                           "temps": res.get("compilation") or res.get("execution"), "controle": res.get("controle"),
                           "incident_bac": res.get("incident_bac"),
                           "observe": observer(cas, res) if "verdict" in res else {}})

    for cas in attendus["lean"]:
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"),
                                cas["etapes"])
        noter("gardes Lean", cas, res, juger_lean(cas, res))
    for cas in attendus["isolement_lean"]:
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), 1)
        noter("isolement Lean", cas, res, juger_tentatives(cas, res["sortie_compilation"]))
    for cas in attendus["python"]:
        res = bac.executer_python(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"))
        ecarts = juger_python(cas, res) + (juger_tentatives(cas, res["stdout"]) if "tentatives" in cas else [])
        noter("Python", cas, res, ecarts)
    bac_limite = X.Bac(replace(cfg, **LIMITES_ESSAI))
    for cas in attendus["limites_python"]:
        res = bac_limite.executer_python(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"))
        noter("limites", cas, res, juger_python(cas, res))

    apres = manifeste()
    hote = []
    if avant != apres:
        hote.append("manifeste de la chaîne, de Mathlib, de l'environnement Python ou du harnais changé")
    if any(jeton in s for s in sorties):
        hote.append("jeton du leurre présent dans une sortie")
    hote += [f"fichier piège présent sur l'hôte : {p}" for p in PIEGES_HOTE if os.path.lexists(p)]
    for racine in (cfg.racine_items, cfg.racine_sorties):
        restes = list(racine.iterdir())
        if restes:
            hote.append(f"{racine} non vide : {[str(r) for r in restes][:5]}")
    residus = processus_de_bac(cfg)
    if residus:
        hote.append(f"processus de bac encore vivants à la fin : {residus}")
    return {"version": VERSION, "cas": cas_rendus, "controles_hote": hote, "manifeste_avant": avant,
            "manifeste_apres": apres, "conforme": all(c["ok"] for c in cas_rendus) and not hote}


def processus_de_bac(cfg: X.Config) -> list[int]:
    """Relevé (sans arrêt) des processus de l'utilisateur du bac, pour le contrôle de fin."""
    import subprocess
    p = subprocess.run(["ps", "-u", cfg.utilisateur, "-o", "pid="], capture_output=True, text=True)
    return [int(x) for x in p.stdout.split()]


def mesurer(cfg: X.Config, artefacts: Path, fichier: str = "sain_v1.lean", etapes: int = 2) -> dict:
    source = (artefacts / fichier).read_text(encoding="utf-8")
    bac = X.Bac(cfg)

    def un():
        r = bac.verifier_lean(X.nouvel_item(), source, etapes)
        return {"accepte": r["verdict"]["accepte_gardes"], "compilation": r["compilation"], "controle": r["controle"]}

    suite = [un() for _ in range(3)]
    t0 = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        parallele = list(ex.map(lambda _: un(), range(3)))
    return {"fichier": fichier, "suite": suite, "parallele_3": parallele,
            "parallele_3_murale_s": round(time.monotonic() - t0, 3)}


PREFLIGHT = "theorem etape_1 : 1 + 1 = 2 := rfl\n\ntheorem enonce_item : 2 = 1 + 1 := rfl\n"


def choisir_variante(chemin_chaine: str | Path) -> dict:
    """Une fois, à l'installation (après la coupure) : première variante d'énumération des constantes (A, puis B) qui accepte
    l'item minimal sans Mathlib ; consignée dans `chaine-v1.json`. Aucune ⇒ arrêt (la garde G-L7 ne peut pas tenir)."""
    chemin = Path(chemin_chaine)
    d = json.loads(chemin.read_text(encoding="utf-8"))
    essais = {}
    for v in ("A", "B"):
        cfg = X.Config(lean=d["lean"], lean_path=d["lean_path"], variante_enumeration=v,
                       python=d.get("python", "/opt/pybac/bin/python"))
        res = X.Bac(cfg).verifier_lean(X.nouvel_item(), PREFLIGHT, 1)  # le bac exige le réseau fermé (CLL-13)
        verdict = res["verdict"]
        essais[v] = {g: x["motifs"] for g, x in verdict["gardes"].items() if x["motifs"]}
        if verdict["accepte_gardes"] and verdict["constantes"]:
            d["variante_enumeration"] = v
            chemin.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            return {"variante": v, "essais": essais, "constantes": verdict["constantes"]}
    raise X.ErreurBac(f"aucune variante d'énumération ne passe sur la chaîne installée : {essais}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["choisir-variante", "epreuve", "mesurer"])
    ap.add_argument("--chaine", default="/opt/harnais/chaine-v1.json")
    ap.add_argument("--artefacts", default=str(Path(__file__).resolve().parent / "artefacts_r5_v2"))
    a = ap.parse_args(argv)
    if a.action == "choisir-variante":
        res = choisir_variante(a.chaine)
        json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
        sys.stdout.write("\n")
        return 0
    cfg = X.charger_config(a.chaine)
    res = epreuve(cfg, Path(a.artefacts)) if a.action == "epreuve" else mesurer(cfg, Path(a.artefacts))
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")
    return 0 if res.get("conforme", True) else 1


if __name__ == "__main__":
    sys.exit(main())
