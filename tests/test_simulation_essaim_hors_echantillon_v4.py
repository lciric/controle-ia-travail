"""Brouillon 4 du préenregistrement hors échantillon (voie B après la contre-lecture 3) : le texte qui sera scellé.
Texte seulement : aucun calcul, aucune cellule de la grille. Code et grille inchangés depuis v3.
"""
import re
from pathlib import Path

from controle_ia.prereg import problemes
from controle_ia.simulation_essaim import lecture_hors_echantillon_v3 as L3
from controle_ia.simulation_t03.run_t03 import COMMIT_CITE

DOSSIER = Path(__file__).resolve().parents[1] / "brouillons" / "preuves-mentors-v1" / "essaim-hors-echantillon-v1"
BROUILLON4 = DOSSIER / "preenregistrement-essaim-hors-echantillon-v1-brouillon4.md"
CL3 = DOSSIER / "contre-lecture-3-preenregistrement-essaim-hors-echantillon-v1.md"


def test_brouillon4_recopie_marqueur_unique_et_validateur(tmp_path):
    texte = BROUILLON4.read_text(encoding="utf-8")
    assert L3.table_E_md() in texte and L3.PHRASE_PORTEE in texte
    assert re.findall(r"<<[A-Z0-9_]+>>", texte) == ["<<COMMIT_CITE>>"] and texte.count("`<<COMMIT_CITE>>`") == 1
    assert "-m controle_ia.simulation_essaim.run_essaim_hors_echantillon_v3 " in texte
    assert problemes(BROUILLON4) == ["marqueurs de gabarit restants : <<COMMIT_CITE>>"]
    commit = "0123456789abcdef0123456789abcdef01234567"
    copie = tmp_path / "scelle.md"
    copie.write_text(texte.replace("<<COMMIT_CITE>>", commit), encoding="utf-8")
    assert problemes(copie) == [] and COMMIT_CITE.search(copie.read_text(encoding="utf-8")).group(1) == commit
    entrees = re.findall(r"^- \*\*Contre-lecture (\d)\*\* \(R2\) — .*$", texte, flags=re.M)
    assert entrees == ["1", "2", "3"]
    cl3 = next(l for l in texte.splitlines() if l.startswith("- **Contre-lecture 3**"))
    assert len(set(re.findall(r"\b[0-9a-f]{64}\b", cl3))) == 3 and "rapport-redaction-v4.md" in cl3
    assert "exactement un marqueur de gabarit" in texte and "exactement deux marqueurs" not in texte


def test_brouillon4_porte_chaque_nouveau_texte_de_la_contre_lecture_3():
    texte = BROUILLON4.read_text(encoding="utf-8")
    corps = CL3.read_text(encoding="utf-8").split("## 8. Textes de remplacement", 1)[1].split("\n## 9.", 1)[0]
    blocs = re.split(r"^#### ", corps, flags=re.M)[1:]
    assert len(blocs) == 13
    for b in blocs:
        ancien, nouveau = re.findall(r"^````\n(.*?)\n````$", b, flags=re.M | re.S)
        assert texte.count(nouveau) == 1, b.split("\n", 1)[0]
