"""Gardes du choix d'offre (`choisir_offre_v2.py`, CLX-07) et de la surveillance (`surveiller_echelle_v2.sh`, R10), sur
des offres fabriquées et un faux outil vastai (R5). Aucun appel réseau, aucune instance réelle.
Lancement : python -m pytest -q echelle-v2/tests
"""
import json
import os
import pathlib
import stat
import subprocess
import sys

import pytest

SCRIPTS = pathlib.Path(__file__).resolve().parent.parent / "scripts"


def offre(i, **kw):
    o = {"id": i, "machine_id": 1, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 2, "cuda_max_good": 13.2,
         "dph_base": 2.3, "dph_total": 2.4, "storage_total_cost": 0.1, "inet_down": 5000.0, "inet_down_cost": 0.004}
    o.update(kw)
    return o


def choisir(tmp_path, offres, plafond="8.00", prix_max="3.50", descente_max="0.005"):
    brut = tmp_path / "brut.json"
    brut.write_text(json.dumps(offres) if not isinstance(offres, str) else offres)
    r = subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "choisir_offre_v2.py"), str(brut),
                        str(tmp_path / "offre.json"), prix_max, descente_max, plafond, str(tmp_path / "journal.txt"),
                        str(tmp_path / "relues.json")], capture_output=True, text=True)
    return r.returncode, r.stdout.split()


def test_offre_saine_moins_chere_et_plafonnee(tmp_path):
    code, sortie = choisir(tmp_path, [offre(1, dph_total=3.0), offre(2, dph_total=2.4), offre(3, num_gpus=1)])
    assert code == 0 and sortie[0] == "2"
    duree, pire = int(sortie[3]), float(sortie[4])
    assert duree <= 7200 and pire <= 8.0


def test_offre_plafond_de_duree_calcule(tmp_path):
    # à 3,4 USD/h, 2 h dépasseraient 8 USD avec la descente et le stockage : la durée est raccourcie
    code, sortie = choisir(tmp_path, [offre(1, dph_total=3.4, inet_down_cost=0.005, storage_total_cost=0.3)])
    assert code == 0 and int(sortie[3]) < 7200 and float(sortie[4]) <= 8.0


@pytest.mark.parametrize("artefact", [
    {"dph_total": 3.9},                      # au-delà du prix maximal
    {"inet_down_cost": 0.04},                # descente trop chère
    {"num_gpus": 1},                         # une seule carte
    {"gpu_ram": 80},                         # unités en Go au lieu de Mo : refusée
    {"cuda_max_good": 12.4},                 # CUDA trop ancien
    {"storage_total_cost": None},            # stockage illisible
    {"dph_total": 3.5, "inet_down_cost": 0.005, "storage_total_cost": 1.2},  # plafond de durée < 4 500 s
])
def test_offre_artefacts(tmp_path, artefact):
    assert choisir(tmp_path, [offre(1, **artefact)])[0] == 3


def test_offre_illisible_ou_ambigue(tmp_path):
    assert choisir(tmp_path, "pas du json")[0] == 2
    assert choisir(tmp_path, [offre(1), offre(1)])[0] == 2


FAUX_VASTAI = r"""#!/usr/bin/env bash
# faux vastai : l'état vit dans $ETAT_FAUX (running|stopped), les journaux dans $JOURNAL_FAUX, les arrêts dans $ARRETS_FAUX
case "$1 $2" in
  "show instance") echo "{\"actual_status\": \"$(cat "$ETAT_FAUX")\", \"cur_state\": \"$(cat "$ETAT_FAUX")\", \"dph_total\": 2.4, \"status_msg\": \"\"}" ;;
  "logs "*) cat "$JOURNAL_FAUX" ;;
  "stop instance") echo "$3" >> "$ARRETS_FAUX"; [ -n "$ARRET_EFFECTIF" ] && echo stopped > "$ETAT_FAUX"; echo "arrêt demandé" ;;
esac
"""


def surveiller(tmp_path, journal, duree="7200", effectif="1"):
    faux = tmp_path / "vastai"
    faux.write_text(FAUX_VASTAI)
    faux.chmod(faux.stat().st_mode | stat.S_IEXEC)
    (tmp_path / "etat").write_text("running")
    (tmp_path / "journal").write_text(journal)
    env = dict(os.environ, VASTAI=str(faux), ETAT_FAUX=str(tmp_path / "etat"), JOURNAL_FAUX=str(tmp_path / "journal"),
               ARRETS_FAUX=str(tmp_path / "arrets"), ARRET_EFFECTIF=effectif, DUREE_MAX_S=duree, PAS_S="1",
               ATTENTE_ARRET_S="0")
    import time
    creation = str(int(time.time()))
    r = subprocess.run(["bash", str(SCRIPTS / "surveiller_echelle_v2.sh"), "12345678", creation, str(tmp_path / "s")],
                       env=env, capture_output=True, text=True, timeout=60)
    arrets = (tmp_path / "arrets").read_text().split() if (tmp_path / "arrets").exists() else []
    return r.returncode, arrets


def test_surveillance_fin_saine(tmp_path):
    code, arrets = surveiller(tmp_path, "ECHELLE 2026 : fini\nAMORCE 2026 : fin, code 0\n")
    assert code == 0 and arrets == ["12345678"]          # arrêt par identifiant (R10)


def test_surveillance_plafond(tmp_path):
    code, arrets = surveiller(tmp_path, "ECHELLE 2026 : mesure\n", duree="2")
    assert code == 5 and arrets == ["12345678"]


def test_surveillance_arret_non_relu(tmp_path):
    code, arrets = surveiller(tmp_path, "AMORCE 2026 : fin, code 0\n", effectif="")
    assert code == 6 and arrets == ["12345678"]


def test_surveillance_plafond_refuse_au_dela_de_deux_heures(tmp_path):
    code, arrets = surveiller(tmp_path, "AMORCE 2026 : fin, code 0\n", duree="9000")
    assert code == 2 and arrets == []
