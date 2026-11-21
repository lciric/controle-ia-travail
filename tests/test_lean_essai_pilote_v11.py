"""Pilote du poste v11 (essai Lean D-1a, quatrième essai) : copie du v10 dont seuls changent l'exécuteur et l'épreuve v7 dans
la phase « apres », la ligne du code de l'épreuve et l'en-tête."""
import subprocess
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
V10 = RACINE / "scripts" / "lean_essai_d1a_v10" / "piloter_poste_v10.sh"
V11 = RACINE / "scripts" / "lean_essai_d1a_v11" / "piloter_poste_v11.sh"


def corps(p):
    return [l for l in p.read_text(encoding="utf-8").splitlines() if not l.startswith("#")]


def test_pilote_v11_rien_d_autre():
    attendu = [l.replace("executeur_bac_v6.py", "executeur_bac_v7.py").replace("epreuve_isolement_v6.py", "epreuve_isolement_v7.py")
               .replace("(0 = conforme ; 124", "(0 = conforme ; 1 = non conforme ; 3 = épreuve morte ; 124") for l in corps(V10)]
    assert corps(V11) == attendu


def test_pilote_v11_lance_les_v7():
    code = V11.read_text(encoding="utf-8")
    assert '"$PAQ/executeur_bac_v7.py" "$PAQ/epreuve_isolement_v7.py"' in code
    assert code.count("python3 -B /opt/harnais/epreuve_isolement_v7.py") == 4 and "epreuve_isolement_v6" not in "\n".join(corps(V11))
    assert "verificateur_noyau_v6.lean" in code   # vérificateur inchangé
    assert subprocess.run(["bash", "-n", str(V11)]).returncode == 0
