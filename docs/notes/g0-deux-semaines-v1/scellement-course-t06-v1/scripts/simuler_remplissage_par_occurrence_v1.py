"""Preuve d'un constat, non un remplissage : sur une COPIE JETABLE du candidat 12 r2 après couples, met des valeurs factices de
la bonne forme dans les seules occurrences « vivantes » des quatre marqueurs restants (lignes de citation de l'en-tête), puis
applique le contrôle de conformité du dépôt (`controle_ia.prereg.problemes`). Deux cas : (1) en-tête seul ; (2) trois marqueurs
remplacés partout (`str.replace`), `<<VALEURS_CITEES_T06>>` par occurrence (deux valeurs différentes : empreinte et chemin).
La copie est écrite dans DOSSIER_JETABLE (hors du rendu) ; la pièce du rendu n'est pas touchée. Aucune valeur réelle.

Usage : python -I -B simuler_remplissage_par_occurrence_v1.py ARBRE CANDIDAT_APRES_COUPLES DOSSIER_JETABLE
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ARBRE, CAND, JET = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(ARBRE / "src"))
from controle_ia import prereg  # noqa: E402

t = CAND.read_text(encoding="utf-8")
copie = JET / "candidat-rempli-factice.md"
JET.mkdir(parents=True, exist_ok=True)
VIVANTES = {219: ("<<COMMIT_CODE_T06>>", "0" * 40), 220: ("<<EMPREINTES_CODE_T06>>", "a" * 64),
            222: ("<<EMPREINTE_AMORCE_T06>>", "c" * 64), 232: ("<<VALEURS_CITEES_T06>>", "b" * 64),
            234: ("<<VALEURS_CITEES_T06>>", "prereg/config-factice.json")}
lignes = t.split("\n")
for n, (m, v) in VIVANTES.items():
    assert lignes[n - 1].count(m) == 1, n
    lignes[n - 1] = lignes[n - 1].replace(m, v)
copie.write_text("\n".join(lignes), encoding="utf-8")
print(json.dumps({"cas": "1 : valeurs factices aux seules lignes de citation de l'en-tête (l. 219, 220, 222, 232, 234)",
                  "problemes": prereg.problemes(copie)}, ensure_ascii=False))
t2 = t
for n in (232, 234):
    ligne = t.split("\n")[n - 1]
    t2 = t2.replace(ligne, ligne.replace(*VIVANTES[n]))
for m, v in (VIVANTES[219], VIVANTES[220], VIVANTES[222]):
    t2 = t2.replace(m, v)
copie.write_text(t2, encoding="utf-8")
restes = [i + 1 for i, l in enumerate(t2.split("\n")) if "<<VALEURS_CITEES_T06>>" in l]
print(json.dumps({"cas": "2 : trois marqueurs remplacés partout, VALEURS_CITEES_T06 aux lignes 232 et 234 seulement",
                  "problemes": prereg.problemes(copie), "lignes_qui_gardent_<<VALEURS_CITEES_T06>>": restes}, ensure_ascii=False))
copie.unlink()
