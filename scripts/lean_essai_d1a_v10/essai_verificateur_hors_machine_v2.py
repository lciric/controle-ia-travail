"""Essai hors machine du vérificateur du noyau contre la chaîne épinglée — essai Lean D-1a, v2 (R-2464, sous R-2439).

Copie de `scripts/lean_essai_d1a_v9/essai_verificateur_hors_machine_v1.py` (inchangé, R12) ; changements : vérificateur,
exécuteur et épreuve v6 ; attendus `attendus-v5.json` (simproc hors noyau en pré-procédure) ; nom de version ; un seul
passage Lean à la fois par défaut (`--paralleles 1`, R-2464 : mémoire du conteneur).

Texte de la v1 : Essai hors machine du vérificateur du noyau contre la chaîne épinglée — essai Lean D-1a, réparation R-2439 (v1).

Cause (R-2438) : `verificateur_noyau_v4.lean`, écrit de mémoire, ne compilait pas sous Lean 4.35.0 ; les essais du harnais ne
le compilaient jamais (faux transport), et le défaut n'a paru que sur la machine louée. Cet essai le compile et le joue contre
la **chaîne épinglée** (Lean 4.35.0, commit `eb6cafb7…` ; Mathlib `56a00585…` et son cache), installée à part, hors de la
machine :
1. **chaîne** : `lean --version` porte `version 4.35.0,` et le commit `eb6cafb7…` ; Mathlib (dépôt git) est au commit épinglé.
   Sinon : code 2, rien d'autre.
2. **compilation** du vérificateur (`lean FICHIER`) : code 0 **et aucun message**. Un avertissement (dépréciation…) sortirait
   sur la sortie standard de `lean --run` et ferait échouer G-L7 sur la machine ; il est donc refusé ici aussi. Non conforme :
   **arrêt avant toute suite** (aucun artefact joué), code 1.
3. **artefacts R5** de `scripts/lean_essai_d1a_v4/artefacts_r5_v4/attendus-v5.json` (v2) qui éprouvent le vérificateur et les
   gardes Lean : groupe `noyau` (rejoué avec et sans G-L3+, jugé par `juger_noyau`), `lean` (jugé par `juger_lean`),
   `observations_noyau` (relevées, sans jugement, comme sur la machine). Ils passent par l'exécuteur v5 en mode
   « essai-local » (sans isolement) et par les jugements de l'épreuve v5, inchangés. Les groupes `isolement_lean`, `python`
   et `limites_python` éprouvent le bac (isolement, limites), pas le vérificateur : ils ne se jouent que sur la machine
   (joués ici sans isolement, ils écriraient sur l'hôte).
Le journal ne porte aucun chemin local : le dépôt devient `<depot>`, la chaîne `<chaine>`, le dossier de travail `<travail>`.

Usage :
  PYTHONPATH=src python3 -B scripts/lean_essai_d1a_v10/essai_verificateur_hors_machine_v2.py jouer --chaine CHAINE.json \
      [--journal SORTIE.json] [--verificateur FICHIER.lean] [--paralleles 3]
  … decrire-chaine --chaine-lean DOSSIER_DE_LA_CHAINE_LEAN --mathlib DOSSIER_DE_MATHLIB --sortie CHAINE.json
CHAINE.json : {"lean": chemin de `lean`, "lean_path": valeur de LEAN_PATH (`lake env printenv LEAN_PATH` dans Mathlib),
"mathlib": dossier du dépôt de Mathlib}. Codes : 0 conforme ; 1 non conforme ; 2 chaîne non épinglée ou usage.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
if str(RACINE / "src") not in sys.path:
    sys.path.insert(0, str(RACINE / "src"))
from controle_ia.lean_essai import epreuve_isolement_v6 as E  # noqa: E402
from controle_ia.lean_essai import executeur_bac_v6 as X  # noqa: E402

VERSION = "essai_verificateur_hors_machine_v2"
ATTENDUS = "attendus-v5.json"
LEAN_VERSION = "version 4.35.0,"
LEAN_COMMIT = "eb6cafb7290e8bd5f2937522d8d804f58f02bafc"
MATHLIB_COMMIT = "56a005855ea17e0b0958f73ec801ae140b0a1679"
VERIFICATEUR = RACINE / "src" / "controle_ia" / "lean_essai" / "verificateur_noyau_v6.lean"
ARTEFACTS = RACINE / "scripts" / "lean_essai_d1a_v4" / "artefacts_r5_v4"
GROUPES = ("noyau", "observations_noyau", "lean")
EXCLUS = {"isolement_lean": "isolement du bac : sur la machine seulement", "python": "bras S dans le bac : sur la machine seulement",
          "limites_python": "limites du bac : sur la machine seulement"}
DELAI_COMPILATION_S = 900


class ChaineNonEpinglee(RuntimeError):
    """La chaîne donnée n'est pas la chaîne épinglée : rien n'est joué (code 2)."""


def maintenant() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def env_lean(chaine: dict) -> dict[str, str]:
    return {"HOME": "/tmp", "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LEAN_PATH": chaine["lean_path"]}


def charger_chaine(chemin: str | Path) -> dict:
    d = json.loads(Path(chemin).read_text(encoding="utf-8"))
    for cle in ("lean", "lean_path", "mathlib"):
        if not isinstance(d.get(cle), str) or not d[cle]:
            raise ChaineNonEpinglee(f"{Path(chemin).name} : clé {cle!r} absente ou vide")
    p = subprocess.run([d["lean"], "--version"], capture_output=True, text=True, timeout=60)
    version = p.stdout.strip()
    if p.returncode != 0 or LEAN_VERSION not in version or LEAN_COMMIT not in version:
        raise ChaineNonEpinglee(f"Lean non épinglé : {version!r} (attendu {LEAN_VERSION} commit {LEAN_COMMIT})")
    g = subprocess.run(["git", "-C", d["mathlib"], "rev-parse", "HEAD"], capture_output=True, text=True, timeout=60)
    commit = g.stdout.strip()
    if g.returncode != 0 or commit != MATHLIB_COMMIT:
        raise ChaineNonEpinglee(f"Mathlib non épinglé : {commit!r} (attendu {MATHLIB_COMMIT})")
    return {"lean": d["lean"], "lean_path": d["lean_path"], "mathlib": d["mathlib"], "version_lean": version,
            "commit_mathlib": commit}


def masquer(texte: str, chaine: dict | None = None, travail: Path | None = None) -> str:
    paires = [(str(RACINE), "<depot>")]
    if travail is not None:
        paires.append((str(travail), "<travail>"))
    if chaine is not None:
        lean = Path(chaine["lean"]).resolve()
        paires += [(str(lean.parents[1]), "<chaine>/lean"), (str(Path(chaine["mathlib"]).resolve()), "<chaine>/mathlib")]
    for brut, masque in sorted(paires, key=lambda x: len(x[0]), reverse=True):
        texte = texte.replace(brut, masque)
    return texte


def compiler(chaine: dict, fichier: Path, delai: int = DELAI_COMPILATION_S) -> dict:
    """`lean FICHIER` : conforme si code 0 et aucun message (sortie standard et erreurs vides)."""
    with tempfile.TemporaryDirectory(prefix="compilation-verificateur-") as d:
        p = subprocess.run([chaine["lean"], str(fichier)], capture_output=True, text=True, env=env_lean(chaine), cwd=d,
                           timeout=delai)
    sortie = (p.stdout + p.stderr).strip()
    return {"fichier": masquer(str(fichier), chaine), "sha256": sha256(fichier), "code": p.returncode,
            "messages": masquer(sortie, chaine)[:8000], "conforme": p.returncode == 0 and not sortie}


def configurer(chaine: dict, travail: Path, verificateur: Path) -> X.Config:
    for d in ("items", "sorties"):
        (travail / d).mkdir(mode=0o700, parents=True, exist_ok=True)
    return X.Config(lean=chaine["lean"], lean_path=chaine["lean_path"], verificateur=str(verificateur),
                    verificateur_sha256=sha256(verificateur), mode="essai-local", racine_items=travail / "items",
                    racine_sorties=travail / "sorties")


def taches(attendus: dict, groupes=GROUPES) -> list[tuple[str, str, dict]]:
    t = []
    for groupe in groupes:
        passages = ("avec G-L3+", "sans G-L3+") if groupe == "noyau" else ("avec G-L3+",)
        for passage in passages:
            t += [(groupe, passage, cas) for cas in attendus[groupe]]
    return t


def faits_noyau(sortie: str) -> dict:
    """Faits bruts du vérificateur (lignes JSON de sa sortie) : imports, rejeu, et pour chaque nom attendu l'aller-retour."""
    lignes = []
    for x in sortie.splitlines():
        try:
            o = json.loads(x)
        except json.JSONDecodeError:
            continue
        if isinstance(o, dict):
            lignes.append(o)
    par = {t: [o for o in lignes if o.get("type") == t] for t in ("imports", "rejeu", "attendu")}
    return {"imports": par["imports"][0] if len(par["imports"]) == 1 else None,
            "rejeu": par["rejeu"][0] if len(par["rejeu"]) == 1 else None,
            "attendus": {o.get("nom"): {"present": o.get("present"), "aller_retour": o.get("aller_retour"),
                                        "raison": str(o.get("raison", ""))[:200], "constantes_agent": o.get("constantes_agent"),
                                        "axiomes": o.get("axiomes")} for o in par["attendu"]}}


def verifier_source(cfg: X.Config, source: str, etapes: int, supplementaires: bool = True) -> dict:
    """Un item (texte Lean) par l'exécuteur v5 en mode « essai-local » : résultat brut de `Bac.verifier_lean`."""
    cfg_p = replace(cfg, supplementaires=supplementaires)
    return X.Bac(cfg_p, lanceur=X.LanceurEssaiLocal(cfg_p)).verifier_lean(X.nouvel_item(), source, etapes)


def jouer_cas(cfg: X.Config, groupe: str, passage: str, cas: dict) -> dict:
    supplementaires = passage == "avec G-L3+"
    c = dict(cas, **cas.get("sans_suppl", {})) if not supplementaires else cas
    res = verifier_source(cfg, (ARTEFACTS / cas["fichier"]).read_text(encoding="utf-8"), cas["etapes"], supplementaires)
    v = res["verdict"]
    if groupe == "noyau":
        ecarts = E.juger_noyau(c, res)
    elif groupe == "lean":
        ecarts = E.juger_lean(c, res)
    else:
        ecarts = []
    if res.get("dossiers_restants"):
        ecarts.append(f"dossiers restants {res['dossiers_restants']}")
    return {"groupe": groupe, "passage": passage, "nom": cas["nom"], "fichier": cas["fichier"],
            "juge": groupe != "observations_noyau", "ok": not ecarts, "ecarts": ecarts,
            "accepte": v["accepte_gardes"], "rejeu_ok": v["rejeu_ok"],
            "gardes_en_echec": {g: x["motifs"][:3] for g, x in v["gardes"].items() if not x["ok"]},
            "observe": E.observer(cas, res) if groupe == "observations_noyau" else {},
            "axiomes": v["axiomes"], "enonces_imprimes": v["enonces_imprimes"], "noyau": faits_noyau(res["sortie_noyau"]),
            "code_noyau": res["noyau"]["code"],
            "duree_compilation_s": res["compilation"]["duree_murale_s"], "duree_noyau_s": res["noyau"]["duree_murale_s"]}


def jouer(chaine: dict, travail: Path, verificateur: Path = VERIFICATEUR, groupes=GROUPES, paralleles: int = 1) -> dict:
    debut = maintenant()
    compilation = compiler(chaine, verificateur)
    res = {"version": VERSION, "debut": debut, "chaine": {"version_lean": chaine["version_lean"],
                                                           "commit_mathlib": chaine["commit_mathlib"]},
           "verificateur": {"fichier": masquer(str(verificateur), chaine), "sha256": sha256(verificateur)},
           "compilation": compilation, "groupes": list(groupes), "exclus": EXCLUS, "cas": []}
    if not compilation["conforme"]:
        res.update({"fin": maintenant(), "conforme": False,
                    "arret": "le vérificateur ne compile pas sans message : arrêt avant toute suite"})
        return res
    attendus = json.loads((ARTEFACTS / ATTENDUS).read_text(encoding="utf-8"))
    cfg = configurer(chaine, travail, verificateur)
    liste = taches(attendus, groupes)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, paralleles)) as ex:
        rendus = list(ex.map(lambda t: jouer_cas(cfg, *t), liste))
    for r in rendus:
        r["ecarts"] = [masquer(x, chaine, travail) for x in r["ecarts"]]
        r["gardes_en_echec"] = {g: [masquer(x, chaine, travail) for x in m] for g, m in r["gardes_en_echec"].items()}
    res["cas"] = rendus
    res["fin"] = maintenant()
    res["conforme"] = all(r["ok"] for r in rendus if r["juge"])
    res["bilan"] = {"cas_juges": sum(r["juge"] for r in rendus), "cas_conformes": sum(r["ok"] for r in rendus if r["juge"]),
                    "observations": sum(not r["juge"] for r in rendus)}
    return res


def decrire_chaine(chaine_lean: Path, mathlib: Path, sortie: Path) -> dict:
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    lake = chaine_lean / "bin" / "lake"
    env = {"HOME": os.environ.get("HOME", "/tmp"), "PATH": f"{chaine_lean / 'bin'}:/usr/bin:/bin", "LANG": "C.UTF-8"}
    p = subprocess.run([str(lake), "env", "printenv", "LEAN_PATH"], capture_output=True, text=True, cwd=mathlib, env=env,
                       timeout=600)
    if p.returncode != 0 or not p.stdout.strip():
        raise SystemExit(f"LEAN_PATH illisible : {p.stderr[-300:]}")
    d = {"lean": str(chaine_lean / "bin" / "lean"), "lean_path": p.stdout.strip(), "mathlib": str(mathlib)}
    sortie.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return d


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = ap.add_subparsers(dest="action", required=True)
    j = sous.add_parser("jouer")
    j.add_argument("--chaine", required=True)
    j.add_argument("--journal")
    j.add_argument("--verificateur", default=str(VERIFICATEUR))
    j.add_argument("--paralleles", type=int, default=1)   # v2 : un passage Lean à la fois
    d = sous.add_parser("decrire-chaine")
    d.add_argument("--chaine-lean", required=True)
    d.add_argument("--mathlib", required=True)
    d.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    if a.action == "decrire-chaine":
        decrire_chaine(Path(a.chaine_lean).resolve(), Path(a.mathlib).resolve(), Path(a.sortie))
        return 0
    if a.journal and Path(a.journal).exists():
        print(f"{a.journal} existe déjà (R12)", file=sys.stderr)
        return 2
    try:
        chaine = charger_chaine(a.chaine)
    except ChaineNonEpinglee as e:
        print(f"chaîne non épinglée : {e}", file=sys.stderr)
        return 2
    with tempfile.TemporaryDirectory(prefix="essai-verificateur-") as t:
        res = jouer(chaine, Path(t), Path(a.verificateur).resolve(), paralleles=a.paralleles)
    texte = json.dumps(res, ensure_ascii=False, indent=1) + "\n"
    if a.journal:
        Path(a.journal).write_text(texte, encoding="utf-8")
    sys.stdout.write(texte)
    return 0 if res["conforme"] else 1


if __name__ == "__main__":
    sys.exit(main())
