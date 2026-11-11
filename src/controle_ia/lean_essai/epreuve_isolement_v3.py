"""Épreuve sur la machine — essai Lean (D-1a), v3 (contre-lecture courte `1fea30ab…`, décision R-2302).

Tourne **sur la machine**, en root, **après** la coupure du réseau sortant (le bac l'exige) et le dépôt du harnais. Autonome
(bibliothèque standard, `executeur_bac_v3`, `gardes_lean_v3`, `sonde_reseau_v1`). Trois commandes, dans cet ordre :
1. `epingler-verificateur` : empreinte de `/opt/harnais/noyau/verificateur_noyau_v3.lean` inscrite dans `chaine-v1.json`
   (avec la version de la chaîne déjà notée à l'installation) ; l'exécuteur refuse tout item si le fichier change ensuite.
2. `noyau` — **premier pas, ce qui ne s'éprouve pas sans Lean** : le vérificateur du noyau sur les items qui le prouvent
   (`artefacts_r5_v3/attendus-v3.json`, groupe `noyau`) : item sain (rejeu et aller-retour réussis) ; déclaration ajoutée hors
   du noyau par un `simproc` et par `run_cmd` (le rejeu doit la prendre) ; instance qui change le sens d'un énoncé (l'aller-retour
   doit la prendre) ; et, relevé sans jugement (« observer »), si le code d'un `simproc` ou d'une tactique d'Aesop s'exécute
   pendant la compilation (CLC2-02, chemins 1 et 2). Code 1 si un attendu du noyau manque : rien d'autre ne se lance.
3. `epreuve` : gardes G-L1 à G-L8 sur les autres artefacts, isolement Lean et Python, limites ; contrôles côté hôte (jeton du
   leurre, manifeste de la chaîne, fichiers pièges, dossiers vides, processus de `bac`).
`mesurer` : item sain trois fois de suite, puis trois en parallèle.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import time
from dataclasses import replace
from pathlib import Path

if __package__:
    from . import executeur_bac_v3 as X
else:
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import executeur_bac_v3 as X  # noqa: E402

VERSION = "epreuve_isolement_v3"
LEURRE = Path("/srv/leurre/leurre-v1.txt")
RACINES_MANIFESTE = ("/opt/elan", "/opt/mathlib", "/opt/pybac", "/opt/harnais")
PIEGES_HOTE = ("/opt/mathlib/Piege-v1.txt", "/opt/mathlib/.lake/build/lib/lean/Piege.olean", "/opt/elan/Piege-v1.txt",
               "/usr/Piege-v1.txt", "/opt/harnais/Piege-v1.txt", "/srv/controle/piege.lean", "/tmp/persistance-v1.txt",
               "/tmp/persistance-py-v1.txt")
RE_TENTATIVE = re.compile(r"ISOLEMENT (\S+) (ECHEC|REUSSI)")
LIMITES_ESSAI = {"memoire_max": "512M", "taches_max": 32, "cpu_max_s": 5, "duree_max_s": 10}
VERIFICATEUR = Path("/opt/harnais/noyau/verificateur_noyau_v3.lean")


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
                      f"{ {g: x['motifs'][:3] for g, x in v['gardes'].items() if x['motifs']} }")
    for g in cas.get("echecs", []):
        if v["gardes"][g]["ok"]:
            ecarts.append(f"{g} devait échouer")
    for g in cas.get("passent", []):
        if not v["gardes"][g]["ok"]:
            ecarts.append(f"{g} devait passer : {v['gardes'][g]['motifs'][:3]}")
    if "rejeu" in cas and v["rejeu_ok"] is not cas["rejeu"]:
        ecarts.append(f"rejeu {v['rejeu_ok']}, {cas['rejeu']} attendu")
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
    return ecarts


def observer(cas: dict, res: dict) -> dict:
    """Relevé sans jugement : gardes et traces de la compilation (comportement de Lean à établir)."""
    v = res["verdict"]["gardes"]
    obs = {g: {"ok": v[g]["ok"], "motifs": v[g]["motifs"][:5]} for g in cas.get("observer", [])}
    for x in cas.get("observer_sortie", []):
        obs[f"sortie contient « {x} »"] = x in res["sortie_compilation"]
    return obs


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


def _noter(rendus: list, sorties: list, genre: str, cas: dict, res: dict, ecarts: list) -> None:
    sorties.append(json.dumps(res, ensure_ascii=False))
    if res.get("processus_residuels"):
        ecarts.append(f"processus résiduels {res['processus_residuels']}")
    if res.get("dossiers_restants"):
        ecarts.append(f"dossiers restants {res['dossiers_restants']}")
    if not res.get("isolement"):
        ecarts.append("exécuté sans isolement")
    if res.get("incident_bac") and not cas.get("incident_attendu"):
        ecarts.append(f"incident du bac {res['incident_bac']}")
    rendus.append({"genre": genre, "nom": cas.get("nom", cas["fichier"]), "ok": not ecarts, "ecarts": ecarts,
                   "incident_bac": res.get("incident_bac"),
                   "observe": observer(cas, res) if "verdict" in res else {},
                   "temps": res.get("compilation") or res.get("execution"), "noyau": res.get("noyau")})


def epingler_verificateur(chemin_chaine: str | Path, verificateur: Path = VERIFICATEUR) -> dict:
    chemin = Path(chemin_chaine)
    d = json.loads(chemin.read_text(encoding="utf-8"))
    d["verificateur_noyau"] = str(verificateur)
    d["verificateur_noyau_sha256"] = hashlib.sha256(verificateur.read_bytes()).hexdigest()
    chemin.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"verificateur_noyau": d["verificateur_noyau"], "sha256": d["verificateur_noyau_sha256"],
            "version_lean": d.get("version_lean"), "commit_mathlib": d.get("commit_mathlib")}


def premier_pas_noyau(cfg: X.Config, artefacts: Path) -> dict:
    if cfg.mode != "bac":
        raise X.ErreurBac("le premier pas du noyau n'a de sens qu'en mode « bac »")
    attendus = json.loads((artefacts / "attendus-v3.json").read_text(encoding="utf-8"))
    bac = X.Bac(cfg)
    rendus, sorties = [], []
    for cas in attendus["noyau"]:
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), cas["etapes"])
        _noter(rendus, sorties, "noyau", cas, res, juger_lean(cas, res))
    return {"version": VERSION, "pas": "noyau", "cas": rendus, "conforme": all(c["ok"] for c in rendus)}


def epreuve(cfg: X.Config, artefacts: Path) -> dict:
    if cfg.mode != "bac":
        raise X.ErreurBac("l'épreuve d'isolement n'a de sens qu'en mode « bac » (lanceur isolé)")
    attendus = json.loads((artefacts / "attendus-v3.json").read_text(encoding="utf-8"))
    LEURRE.parent.mkdir(mode=0o700, exist_ok=True)
    jeton = "leurre-" + secrets.token_hex(16)
    LEURRE.write_text(jeton + "\n", encoding="utf-8")
    os.chmod(LEURRE, 0o600)
    avant = manifeste()
    bac = X.Bac(cfg)
    rendus, sorties = [], []
    for cas in attendus["lean"]:
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), cas["etapes"])
        _noter(rendus, sorties, "gardes Lean", cas, res, juger_lean(cas, res))
    for cas in attendus["isolement_lean"]:
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), 1)
        _noter(rendus, sorties, "isolement Lean", cas, res, juger_tentatives(cas, res["sortie_compilation"]))
    for cas in attendus["python"]:
        res = bac.executer_python(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"))
        _noter(rendus, sorties, "Python", cas, res,
               juger_python(cas, res) + (juger_tentatives(cas, res["stdout"]) if "tentatives" in cas else []))
    bac_limite = X.Bac(replace(cfg, **LIMITES_ESSAI))
    for cas in attendus["limites_python"]:
        res = bac_limite.executer_python(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"))
        _noter(rendus, sorties, "limites", cas, res, juger_python(cas, res))
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
    p = subprocess.run(["ps", "-u", cfg.utilisateur, "-o", "pid="], capture_output=True, text=True)
    if p.stdout.split():
        hote.append(f"processus de bac encore vivants à la fin : {p.stdout.split()}")
    return {"version": VERSION, "cas": rendus, "controles_hote": hote, "manifeste_avant": avant,
            "manifeste_apres": apres, "conforme": all(c["ok"] for c in rendus) and not hote}


def mesurer(cfg: X.Config, artefacts: Path, fichier: str = "sain_v1.lean", etapes: int = 2) -> dict:
    source = (artefacts / fichier).read_text(encoding="utf-8")
    bac = X.Bac(cfg)

    def un():
        r = bac.verifier_lean(X.nouvel_item(), source, etapes)
        return {"accepte": r["verdict"]["accepte_gardes"], "compilation": r["compilation"], "noyau": r["noyau"]}

    suite = [un() for _ in range(3)]
    t0 = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        parallele = list(ex.map(lambda _: un(), range(3)))
    return {"fichier": fichier, "suite": suite, "parallele_3": parallele,
            "parallele_3_murale_s": round(time.monotonic() - t0, 3)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["epingler-verificateur", "noyau", "epreuve", "mesurer"])
    ap.add_argument("--chaine", default="/opt/harnais/chaine-v1.json")
    ap.add_argument("--artefacts", default=str(Path(__file__).resolve().parent / "artefacts_r5_v3"))
    a = ap.parse_args(argv)
    if a.action == "epingler-verificateur":
        res = epingler_verificateur(a.chaine)
    else:
        cfg = X.charger_config(a.chaine)
        res = {"noyau": premier_pas_noyau, "epreuve": epreuve, "mesurer": mesurer}[a.action](cfg, Path(a.artefacts))
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")
    return 0 if res.get("conforme", True) else 1


if __name__ == "__main__":
    sys.exit(main())
