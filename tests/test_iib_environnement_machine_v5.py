"""Environnement de la machine louée, reproduit sur le poste (correctif 0011) : accord posé (`IIB_GO_ID`), carte simulée (un
`nvidia-smi` factice en tête du chemin ; un torch factice qui voit une carte tant que `CUDA_VISIBLE_DEVICES` n'est pas vide,
dans l'interpréteur de l'amorce), python3 du système sans numpy (environnement virtuel vide ; `python3 -I -S`). Chaque
condition sur un cas sain et un artefact (R5). La première tentative de l'étalonnage s'est arrêtée sur la machine, pendant la
suite ciblée, avant tout chargement du modèle : « 5 failed, 263 passed, 3 errors » ; ces essais en reproduisent les deux causes.
Aucune machine, aucun loueur, aucun réseau."""
import os
import re
import shutil
import subprocess
import sys
import types
from pathlib import Path

import pytest
from iib_v5_outils import environnement_sans_carte, python_sans_numpy
from test_iib_lanceur_v5 import _depot_jouet, _monde

from controle_ia.gardes import GardeArret
from controle_ia.iib import lanceur_v5 as la
from controle_ia.iib.jouet_v5 import ModeleJouetDeLangue

DEPOT = Path(__file__).resolve().parents[1]
SRC = str(DEPOT / "src")
GO = "GO-2099-01-01-01"                         # accord factice, de la forme de ceux que le lanceur de session pose sur la machine
VOIR_LA_CARTE = "from controle_ia.iib.lanceur_v5 import carte_visible; print(carte_visible())"
# la commande même par laquelle la surveillance du lanceur de session appelle la règle de coupure de l'étalonnage
SESSION = re.search(r'^SESSION="(.+)"$', (DEPOT / "scripts" / "lancer_iib_v3.sh").read_text(encoding="utf-8"), re.M).group(1).replace("$DEPOT", str(DEPOT))
NVIDIA_SMI_FACTICE = "#!/bin/sh\necho 'NVIDIA A100-SXM4-80GB, 595.91.07, 81920 MiB (carte simulée par les essais du correctif 0011)'\n"
TORCH_FACTICE = '''"""torch factice des essais du correctif 0011 : une carte est visible, comme sur la machine louée, tant que
CUDA_VISIBLE_DEVICES n'est pas vide (contrat de CUDA : vide, aucune carte n'est visible du processus)."""
import os


class cuda:  # noqa: N801
    @staticmethod
    def is_available():
        return os.environ.get("CUDA_VISIBLE_DEVICES") != ""
'''
# « 5 failed, 263 passed, 3 errors » : les huit essais arrêtés sur la machine louée (traces de l'exécutante, tests.txt, 21 novembre)
ARRETES_SUR_LA_MACHINE = (
    "tests/test_iib_lanceur_v5.py::test_second_passage_des_conditions_refuse",
    "tests/test_iib_lanceur_v5.py::test_essai_a_blanc_de_bout_en_bout_par_le_point_d_entree",
    "tests/test_iib_lanceur_v5.py::test_surveillance_cas_sain_depense_sous_12_rien",
    "tests/test_iib_lanceur_v5.py::test_surveillance_artefact_depense_a_12_coupure_motif_ecrit_arret_par_l_identifiant",
    "tests/test_iib_lanceur_v5.py::test_surveillance_hors_etalonnage_la_regle_ne_joue_pas_et_phase_illisible_arrete",
    "tests/test_iib_distillation_bout_en_bout_v5.py::test_course_entiere_distillation_et_evaluation_scellees",
    "tests/test_iib_distillation_bout_en_bout_v5.py::test_evaluation_quatre_conditions_deux_oracles_modele_rendu_a_dose_nulle",
    "tests/test_iib_distillation_bout_en_bout_v5.py::test_course_refusee_avant_le_premier_tour_si_la_lecture_de_la_premiere_action_est_vide",
)


def machine_simulee(dossier: Path) -> dict:
    """Pièces de la carte simulée : `bin/nvidia-smi` factice, exécutable ; `site/torch/` factice."""
    d = Path(dossier)
    (d / "bin").mkdir(parents=True)
    smi = d / "bin" / "nvidia-smi"
    smi.write_text(NVIDIA_SMI_FACTICE, encoding="utf-8")
    smi.chmod(0o755)
    (d / "site" / "torch").mkdir(parents=True)
    (d / "site" / "torch" / "__init__.py").write_text(TORCH_FACTICE, encoding="utf-8")
    return {"bin": d / "bin", "site": d / "site"}


def environnement_de_la_machine(m: dict) -> dict:
    """L'environnement des essais, plus ce que porte la machine louée : l'accord posé, une carte que `nvidia-smi` voit en tête
    du chemin ; aucun masque de CUDA."""
    env = {k: v for k, v in os.environ.items() if k != "CUDA_VISIBLE_DEVICES"}
    env.update({"IIB_GO_ID": GO, "PATH": f"{m['bin']}{os.pathsep}{os.environ.get('PATH', '')}"})
    return env


def python_carte_simulee(dossier: Path, site: Path) -> Path:
    """Interpréteur d'un environnement virtuel dont le torch (factice) voit la carte, et qui voit les paquets de l'interpréteur
    des essais (numpy, pytest) par un fichier `.pth` : l'environnement de l'amorce sur la machine louée. Vérifié avant emploi
    (R5) : torch factice chargé, carte vue sans masque, masquée par `CUDA_VISIBLE_DEVICES` vide ; sinon l'essai s'arrête."""
    v = Path(dossier) / "environnement-de-l-amorce"
    v.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, "-m", "venv", "--without-pip", str(v)], check=True, capture_output=True, timeout=120)
    py = v / "bin" / "python"
    paquets = Path(subprocess.run([str(py), "-I", "-c", "import sysconfig; print(sysconfig.get_paths()['purelib'])"], check=True,
                                  capture_output=True, text=True, timeout=60).stdout.strip())
    shutil.copytree(Path(site) / "torch", paquets / "torch")
    parents = [p for p in sys.path if p and Path(p).is_dir() and Path(p).name in ("site-packages", "dist-packages")]
    (paquets / "paquets-des-essais.pth").write_text("".join(p + "\n" for p in parents), encoding="utf-8")
    sonde = "import os, numpy, pytest, torch; print(os.path.realpath(torch.__file__)); print(torch.cuda.is_available())"
    env = {k: v for k, v in os.environ.items() if k != "CUDA_VISIBLE_DEVICES"}
    vu = subprocess.run([str(py), "-c", sonde], env=env, capture_output=True, text=True, timeout=120)
    masque = subprocess.run([str(py), "-c", sonde], env={**env, "CUDA_VISIBLE_DEVICES": ""}, capture_output=True, text=True, timeout=120)
    factice = str((paquets / "torch" / "__init__.py").resolve())
    if vu.returncode or masque.returncode or vu.stdout.splitlines()[-2:] != [factice, "True"] or masque.stdout.splitlines()[-2:] != [factice, "False"]:
        raise RuntimeError(f"interpréteur de la carte simulée non conforme : {vu.stdout!r} {vu.stderr[-400:]!r} / {masque.stdout!r}")
    return py


def _module_torch_factice() -> types.ModuleType:
    t = types.ModuleType("torch")
    exec(TORCH_FACTICE, t.__dict__)                                  # noqa: S102 (texte constant de ce fichier)
    return t


def _carte_vue(python, env: dict) -> str:
    r = subprocess.run([str(python), "-c", VOIR_LA_CARTE], env={**env, "PYTHONPATH": SRC}, capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr[-800:]
    return r.stdout.strip()


def test_accord_pose_et_carte_simulee_dans_le_processus_la_garde_refuse_l_essai_isole_passe(tmp_path, monkeypatch):
    """Dans le processus des essais, chaque condition de la machine — accord posé, carte vue par `nvidia-smi`, carte vue par
    torch — sur un artefact (sans isolement explicite, la garde refuse le mode jouet : son effet en production est intact) et un
    cas sain (avec l'isolement que l'essai écrit, la garde laisse passer et c'est le contrôle suivant qui parle)."""
    racine = tmp_path / "depot"
    config = _monde(racine)
    modele, monde = ModeleJouetDeLangue(), la.MondeJouet()
    deja = racine / "deja"
    (deja / "lots").mkdir(parents=True)                             # un étalonnage déjà joué ici : le contrôle qui suit la garde
    m = machine_simulee(tmp_path / "machine")
    vide = tmp_path / "chemin-vide"
    vide.mkdir()
    monkeypatch.setitem(sys.modules, "torch", _module_torch_factice())          # torch du processus : le factice (sur la machine, il masque le vrai)
    monkeypatch.setenv("PATH", str(vide))
    monkeypatch.setenv("CUDA_VISIBLE_DEVICES", "")
    monkeypatch.delenv("IIB_GO_ID", raising=False)
    assert not la.carte_visible()                                    # point de départ : ni carte ni accord
    # 1. accord posé dans l'environnement du processus, comme sur la machine
    monkeypatch.setenv("IIB_GO_ID", GO)
    with pytest.raises(GardeArret, match="mode jouet sur une machine payante"):  # artefact : le point d'entrée lit l'environnement
        la.executer("etalonnage", config, racine, "20991231-000009-iib-jouet", modele, monde, carte=False)
    assert not (racine / "runs").exists() and not (racine / "diag").exists()
    with pytest.raises(GardeArret, match="déjà joué"):               # cas sain : l'essai isole l'accord ({} explicite)
        la.phase_etalonnage(config, racine, deja, modele, monde, {}, carte=False)
    monkeypatch.delenv("IIB_GO_ID")
    # 2. carte vue par nvidia-smi (factice, en tête du chemin)
    monkeypatch.setenv("PATH", f"{m['bin']}{os.pathsep}{vide}")
    assert la.carte_visible()
    with pytest.raises(GardeArret, match="mode jouet sur une machine payante"):  # artefact : la carte est détectée
        la.phase_etalonnage(config, racine, deja, modele, monde)
    with pytest.raises(GardeArret, match="déjà joué"):               # cas sain : carte=False explicite
        la.phase_etalonnage(config, racine, deja, modele, monde, carte=False)
    # 3. carte vue par torch, aucun nvidia-smi sur le chemin
    monkeypatch.setenv("PATH", str(vide))
    monkeypatch.delenv("CUDA_VISIBLE_DEVICES")
    assert la.carte_visible()
    with pytest.raises(GardeArret, match="mode jouet sur une machine payante"):
        la.phase_course(config, racine, "course", modele, monde)
    with pytest.raises(GardeArret, match="pas de course sans résultat"):
        la.phase_course(config, racine, "course", modele, monde, carte=False)
    monkeypatch.setenv("CUDA_VISIBLE_DEVICES", "")                  # le masque de CUDA que pose l'isolement des sous-processus
    assert not la.carte_visible()


def test_point_d_entree_sous_la_machine_simulee_l_isolement_masque_la_carte_la_garde_refuse_sans_lui(tmp_path, tmp_path_factory):
    """Sous-processus, comme le point d'entrée que l'essai à blanc appelle : la machine simulée est vue ; l'ancien isolement
    des essais (`/usr/bin:/bin`, sans accord) ne masquait pas la carte que voit torch (l'arrêt de la machine) ; l'isolement
    écrit par les essais la masque, à l'interpréteur simulé comme au vrai interpréteur des essais (sur la machine louée : le
    vrai torch et la vraie carte) ; sans lui, le point d'entrée refuse le mode jouet avant tout manifeste."""
    m = machine_simulee(tmp_path_factory.mktemp("machine"))
    py = python_carte_simulee(tmp_path_factory.mktemp("interpreteur"), m["site"])
    machine = environnement_de_la_machine(m)
    assert _carte_vue(py, machine) == "True"                         # artefact de la simulation : la carte est vue
    ancien = {**{k: v for k, v in machine.items() if k != "IIB_GO_ID"}, "PATH": "/usr/bin:/bin"}
    assert _carte_vue(py, ancien) == "True"                          # l'ancien isolement de l'essai à blanc ne la masquait pas
    isole = environnement_sans_carte(tmp_path_factory.mktemp("poste"), machine)
    assert "IIB_GO_ID" not in isole and isole["CUDA_VISIBLE_DEVICES"] == "" and not shutil.which("nvidia-smi", path=isole["PATH"])
    assert _carte_vue(py, isole) == "False" and _carte_vue(sys.executable, isole) == "False"      # cas sain
    _depot_jouet(tmp_path)
    carte_seule = {k: v for k, v in machine.items() if k != "IIB_GO_ID"}
    for n, env in enumerate((machine, carte_seule, {**isole, "IIB_GO_ID": GO})):     # accord et carte ; carte seule ; accord seul
        run = f"20991231-00002{n}-iib-jouet"
        r = subprocess.run([str(py), "-m", "controle_ia.iib.lanceur_v5", "--config", "entrees/config-iib-v5-jouet.json", "--run-id", run,
                            "--phase", "etalonnage"], cwd=tmp_path, env={**env, "PYTHONPATH": SRC}, capture_output=True, text=True, timeout=300)
        assert r.returncode == 1 and "mode jouet sur une machine payante" in r.stderr and not (tmp_path / "runs" / run).exists(), (n, r.stderr[-800:])


def test_regle_de_coupure_sous_le_python3_du_systeme_sans_numpy_cas_sain_artefact_phase_illisible(tmp_path):
    """La règle de coupure de l'étalonnage à 12 USD, appelée comme la surveillance l'appelle, sous le python3 du système de la
    machine louée (sans numpy) : environnement virtuel vide, puis `-I -S` (aucun paquet tiers). Cas sain (sous 12 USD : rien),
    artefact (à 12 USD : arrêt), autre phase (la règle ne joue pas), phase illisible (refus, aucun repli)."""
    sans_numpy = python_sans_numpy(tmp_path / "python-du-systeme")
    # la simulation reproduit la machine (R5) : le module de configuration, qui a besoin de numpy (lois exactes), ne s'y charge
    # pas — c'est la trace de la machine ; la règle de coupure, elle, doit s'y charger sans lui
    r = subprocess.run([str(sans_numpy / "python3"), "-I", "-B", "-c", f"import sys; sys.path.insert(0, {SRC!r}); from controle_ia.iib import configuration_v5"],
                       capture_output=True, text=True, timeout=120)
    assert r.returncode != 0 and "No module named 'numpy'" in r.stderr
    from datetime import datetime, timezone

    cree = 1_795_000_000
    progres = tmp_path / "progres.txt"
    instant = datetime.fromtimestamp(cree + 600, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    progres.write_text(f"AMORCE IIB v1 DEMARRAGE 1 : {instant}, machine m, commit c\nPROGRES {instant} phase=etalonnage lot=1\n", encoding="utf-8")

    def h(heures):
        return str(int(cree + 600 + heures * 3600))
    for interpreteur in ([str(sans_numpy / "python3"), "-I", "-B"], [sys.executable, "-I", "-S", "-B"]):
        def regle(phase, maintenant):
            return subprocess.run([*interpreteur, "-c", SESSION, "coupure-etalonnage", phase, str(progres), maintenant, "1.30", "0.08", str(cree)],
                                  capture_output=True, text=True, timeout=120)
        sain = regle("etalonnage", h(8))                             # 8 h à 1,38 USD/h : 11,04 USD
        assert sain.returncode == 0, (interpreteur, sain.stderr[-1500:])
        assert sain.stdout.startswith("RIEN : dépense comptée de l'étalonnage 11.04 USD < 12 USD (depuis : début de l'amorce)"), sain.stdout
        art = regle("etalonnage", h(9))                              # 9 h : 12,42 USD
        assert art.returncode == 0 and art.stdout.startswith("ARRET coupure de l'étalonnage : dépense comptée 12.42 USD ≥ 12 USD"), art.stdout
        autre = regle("course", h(30))
        assert autre.returncode == 0 and "ne joue pas" in autre.stdout, autre.stderr[-800:]
        illisible = regle("illisible", h(1))
        assert illisible.returncode == 1 and "REFUS : coupure de l'étalonnage : phase 'illisible' illisible" in illisible.stderr, illisible.stderr[-800:]
        assert "No module named" not in sain.stderr + art.stderr + autre.stderr + illisible.stderr


def test_les_huit_essais_arretes_sur_la_machine_passent_sous_la_machine_simulee(tmp_path):
    """Reproduction de l'arrêt de la machine : les huit essais en échec ou en erreur sur la machine louée, rejoués par un pytest
    enfant dans l'environnement de la machine simulée — accord posé, carte que voient `nvidia-smi` (en tête du chemin) et
    torch (interpréteur de l'amorce simulé), python3 du système sans numpy (celui que la surveillance trouve, posé par
    `_surveiller`). Sans le correctif 0011 ils échouent comme sur la machine ; avec lui, ils passent."""
    m = machine_simulee(tmp_path / "machine")
    py = python_carte_simulee(tmp_path / "interpreteur", m["site"])
    env = environnement_de_la_machine(m)
    assert _carte_vue(py, env) == "True"                             # la simulation est en place (R5)
    r = subprocess.run([str(py), "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no", f"--basetemp={tmp_path / 'essais-enfants'}",
                        *ARRETES_SUR_LA_MACHINE], cwd=DEPOT, env=env, capture_output=True, text=True, timeout=1200)
    lignes = r.stdout.strip().splitlines()
    assert r.returncode == 0 and lignes and re.fullmatch(r"8 passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?", lignes[-1]), \
        r.stdout[-6000:] + r.stderr[-1500:]
