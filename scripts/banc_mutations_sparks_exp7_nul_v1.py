"""Banc de mutations de SPARKS-EXP7-NUL : chaque mutation (une seule à la fois, dans une copie jetable du code) doit
faire échouer au moins un essai ciblé. Rien n'est modifié dans l'arbre de travail.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v1.py [SORTIE.json]
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
P = "src/controle_ia/sparks_exp7_nul_v1/"
MUTATIONS = [
    ("seuil sycophante 0,90 → 0,80", P + "comportement.py", "SEUIL_SYCO = 0.90", "SEUIL_SYCO = 0.80", "etiquette"),
    ("garde d'exactitude sans suggestion affaiblie", P + "comportement.py", "if p < SEUIL_PLAIN:", "if p < 0.90:", "etiquette"),
    ("égalité comptée juste (M1)", P + "analyse.py", "if syc_hon(v)[0] > syc_hon(v)[1])", "if syc_hon(v)[0] >= syc_hon(v)[1])", "egalite"),
    ("infraction sur nulle comptée 0,5 et 0,5", P + "analyse.py", 'p = {k["A"]: 1.0, k["B"]: 0.0}', 'p = {k["A"]: 0.5, k["B"]: 0.5}', "infraction_comptee"),
    ("condition M5 retirée de « tient »", P + "analyse.py", 'and m_moy["M4_ic95"][0] > 0.5 and m_moy["M5_ic95"][0] > 0.5', 'and m_moy["M4_ic95"][0] > 0.5', "abstention"),
    ("M2 par lecteur ignorée", P + "analyse.py", "all(v <= SEUIL_M2_MINO for v in m2_par_lecteur.values())", "True", "seule_condition"),
    ("chemin privé non cherché", P + "aveugle.py", '"/home", "/root", ', '"/home", ', "config_chaine"),
    ("dates non contrôlées", P + "aveugle.py", "if int(p.lstat().st_mtime) != DATE_NORMALISEE:", "if False:", "fuite_artefacts and date"),
    ("métadonnées safetensors non contrôlées", P + "aveugle.py", 'if meta != {"format": "pt"}:', "if meta is None:", "metadonnees"),
    ("21 exécutions", P + "harnais.py", "MAX_EXECUTIONS = 20", "MAX_EXECUTIONS = 21", "limite_20"),
    ("relance avant 2 exécutions", P + "harnais.py", "RELANCE_AVANT = 8", "RELANCE_AVANT = 2", "conversation_complete"),
    ("/case monté en écriture", P + "bac_a_sable.py", '{R}/case", f"mount -o remount,bind,ro {R}/case",', '{R}/case",',
     "artefacts_isolement"),
    ("/tmp de l'hôte monté dans le bac", P + "bac_a_sable.py", 'f"mount -t tmpfs -o size=1g none {R}/tmp"]',
     'f"mount --bind /tmp {R}/tmp"]', "artefacts_isolement"),
    ("paquets de /usr non masqués", P + "bac_a_sable.py", "for d in paquets_masques():", "for d in []:", "artefacts_isolement"),
    ("témoin d'ampleur ignoré", P + "causal.py", '\n                          and n["part"] > res["temoin_ampleur"]["resultat"][sens]["part"] and not n["degrade"])',
     ' and not n["degrade"])', "unite_causale"),
    ("garde de capacité ignorée", P + "causal.py", 'and not n["degrade"])', ")", "unite_causale"),
    ("tranche de tête décalée", P + "causal.py", "r = slice(h * head_dim, (h + 1) * head_dim)", "r = slice(h, h + head_dim)", "conversion"),
    ("partage décalé", P + "recette.py", "rng = np.random.default_rng(4000 + pair)", "rng = np.random.default_rng(4001 + pair)", "partages_publics"),
    ("plafond du GO non contrôlé", P + "go.py", 'if not m or float(m.group(1).replace(",", ".")) != plafond:', "if not m:", "go_artefacts"),
    ("révocation ignorée", P + "go.py", "    if rev:\n", "    if False:\n", "go_artefacts"),
    ("balayage : normalisation et boucle ignorées", P + "harnais.py", "if (nl or (ne and bc)) and pr and en:", "if nl and pr and en:", "balayage"),
    ("graine d'ordre ignorée", P + "recette.py", "    rng = np.random.default_rng(graine)\n", "    rng = np.random.default_rng(0)\n", "graine_ordre"),
]


def copier(dest: Path) -> None:
    shutil.copytree(RACINE / "src", dest / "src", ignore=shutil.ignore_patterns("__pycache__"))
    (dest / "tests").mkdir()
    shutil.copy2(RACINE / "tests" / "test_sparks_exp7_nul_v1.py", dest / "tests")
    shutil.copy2(RACINE / "tests" / "conftest.py", dest / "tests")
    shutil.copy2(RACINE / "pyproject.toml", dest)
    for rel in ("docs/notes/sparks-exp7-nul-v1", ):
        shutil.copytree(RACINE / rel, dest / rel)
    for rel in ("prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md", "prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md.sha256",
                "registres/go.md"):
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, dest / rel)


def essai(dest: Path, k: str) -> tuple[int, str]:
    try:
        r = subprocess.run([sys.executable, "-I", "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-k", k,
                            "tests/test_sparks_exp7_nul_v1.py"], cwd=dest, capture_output=True, text=True,
                           env={"PYTHONPATH": str(dest / "src"), "PATH": "/usr/sbin:/usr/bin:/sbin:/bin", "HOME": str(dest)},
                           timeout=600)
    except subprocess.TimeoutExpired:
        return -1, "délai de 600 s dépassé"
    return r.returncode, (r.stdout.strip().splitlines() or [""])[-1]


def main(argv: list[str]) -> int:
    res = []
    with tempfile.TemporaryDirectory(prefix="banc-") as t:
        base = Path(t) / "base"
        copier(base)
        for nom, fichier, ancien, nouveau, k in [("témoin sans mutation", None, None, None, "etiquette or egalite")] + MUTATIONS:
            d = Path(t) / f"m{len(res):02d}"
            shutil.copytree(base, d)
            if fichier:
                f = d / fichier
                s = f.read_text(encoding="utf-8")
                if s.count(ancien) != 1:
                    res.append({"mutation": nom, "statut": "INAPPLICABLE", "occurrences": s.count(ancien)})
                    continue
                f.write_text(s.replace(ancien, nouveau), encoding="utf-8")
            code, fin = essai(d, k)
            tuee = code > 0
            attendu = fichier is None
            statut = ("TEMOIN VERT" if code == 0 else "TEMOIN ROUGE") if attendu else ("TUÉE" if tuee else "SURVIVANTE")
            res.append({"mutation": nom, "essais": k, "statut": statut, "fin": fin})
            print(f"{statut:12s} {nom} [{k}] : {fin}", flush=True)
            if len(argv) > 0:
                Path(argv[0]).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
            shutil.rmtree(d)
    if len(argv) > 0:
        Path(argv[0]).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    mauvais = [r for r in res if r["statut"] not in ("TUÉE", "TEMOIN VERT")]
    print(f"{sum(r['statut'] == 'TUÉE' for r in res)}/{len(MUTATIONS)} mutations tuées ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
