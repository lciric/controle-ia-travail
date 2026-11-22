"""Complément des essais de l'admission (version 2) : la course appelle la garde C14.

Écrit après le jeu des mutations : la mutation « garde C14 non appelée » survivait au
fichier `test_devin_v2_admission.py`, parce que l'ordre des lignes est juste et que la
garde ne s'y voit pas. Racines fixes, dérivées de RACINE.
"""
import numpy as np

from controle_ia.devin_v2 import admission
from controle_ia.devin_v2.admission import ConfigurationCourse, InventaireSimule, jouer_course
from controle_ia.devin_v2.graines import graine_tache
from controle_ia.devin_v2.monde_plante import Fuite

RACINE = 0x7F4A_7C15_9E37_79B9_F39C_C060_5CED_C834


def source_essai(nom):
    g = graine_tache(RACINE, nom)
    return int.from_bytes(g.generate_state(4, dtype=np.uint32).tobytes(), "big") | (1 << 127)


def test_course_appelle_la_garde_apres_scellement(monkeypatch):
    vraie = admission.exiger_epreuve_apres_scellement
    appels = []

    def espionne(racines, familles):
        racines, familles = list(racines), list(familles)
        appels.append((racines, familles))
        return vraie(racines, familles)

    monkeypatch.setattr(admission, "exiger_epreuve_apres_scellement", espionne)
    c = ConfigurationCourse(devin="piece", temoin_fuite=Fuite("horodatage", 1.5, "temoin"),
                            n_apprentissage=100, n_epreuve=100, B=999, etages=("0",))
    v = jouer_course(c, [], InventaireSimule(outils=()), source_racines=source_essai)
    assert len(appels) == 1
    racines, familles = appels[0]
    assert {r.empreinte for r in racines} == set(v["empreintes_racines"]["course:epreuve"].values())
    # trois familles (secret, factice, témoin) et la famille de l'épreuve à part
    assert len(familles) == 4 and all(f.empreinte is not None for f in familles)
