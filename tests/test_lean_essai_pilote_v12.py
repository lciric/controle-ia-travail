"""Pilote du poste v12 (essai Lean D-1a, quatrième essai, après la contre-lecture des corrections) : copie du v11 dont seuls
changent l'exécuteur et l'épreuve v8 dans la phase « apres », et l'en-tête."""
import subprocess
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
V11 = RACINE / "scripts" / "lean_essai_d1a_v11" / "piloter_poste_v11.sh"
V12 = RACINE / "scripts" / "lean_essai_d1a_v12" / "piloter_poste_v12.sh"


def corps(p):
    return [l for l in p.read_text(encoding="utf-8").splitlines() if not l.startswith("#")]


def test_pilote_v12_rien_d_autre():
    attendu = [l.replace("executeur_bac_v7.py", "executeur_bac_v8.py").replace("epreuve_isolement_v7.py", "epreuve_isolement_v8.py")
               for l in corps(V11)]
    assert corps(V12) == attendu


def test_pilote_v12_lance_les_v8():
    code = V12.read_text(encoding="utf-8")
    assert '"$PAQ/executeur_bac_v8.py" "$PAQ/epreuve_isolement_v8.py"' in code
    assert code.count("python3 -B /opt/harnais/epreuve_isolement_v8.py") == 4
    assert "epreuve_isolement_v7" not in "\n".join(corps(V12)) and "executeur_bac_v7" not in "\n".join(corps(V12))
    assert "verificateur_noyau_v6.lean" in code and '"$V4"/artefacts_r5_v4/*' in code
    assert subprocess.run(["bash", "-n", str(V12)]).returncode == 0
