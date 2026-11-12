"""Essais R5 de l'installateur v2 et du pilote v7 de l'essai Lean D-1a (R-2415) : garde de lisibilité par `bac` (cas sain et
artefact, sur de vrais fichiers 0644 et 0600 d'un dossier temporaire), ordre des commandes de l'installateur, emploi de
l'installateur v2 par le pilote, et aucun autre changement que ceux déclarés par rapport à la v1 et à la v6. Aucun réseau,
aucune machine ; rien n'est lancé en root hors du dossier temporaire."""
import os
import re
import shutil
import stat
import subprocess
import tempfile
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
INST_V1 = RACINE / "scripts" / "lean_essai_d1a_v1" / "installer_chaine_v1.sh"
INST_V2 = RACINE / "scripts" / "lean_essai_d1a_v2" / "installer_chaine_v2.sh"
PIL_V6 = RACINE / "scripts" / "lean_essai_d1a_v6" / "piloter_poste_v6.sh"
PIL_V7 = RACINE / "scripts" / "lean_essai_d1a_v7" / "piloter_poste_v7.sh"
DEBUT, FIN = "# --- garde de lisibilité par bac (v2) : début ---", "# --- garde de lisibilité par bac (v2) : fin ---"


def fonctions_garde() -> str:
    t = INST_V2.read_text(encoding="utf-8")
    assert t.count(DEBUT) == 1 and t.count(FIN) == 1
    return t[t.index(DEBUT):t.index(FIN) + len(FIN)]


def appeler(fonction: str, *args: str) -> subprocess.CompletedProcess:
    code = "set -euo pipefail\n" + fonctions_garde() + f'\n{fonction} "$@"\n'
    return subprocess.run(["bash", "-c", code, "garde", *args], capture_output=True, text=True, timeout=60)


def arbre_sain(base: Path) -> Path:
    """Arbre à l'image de /opt/mathlib : dossiers 0755, fichiers 0644, un exécutable 0755."""
    r = base / "mathlib"
    (r / ".lake" / "build" / "lib" / "lean").mkdir(parents=True)
    for d in [r, *r.rglob("*")]:
        d.chmod(0o755)
    olean = r / ".lake" / "build" / "lib" / "lean" / "Mathlib.olean"
    olean.write_bytes(b"olean")
    olean.chmod(0o644)
    lean = r / "lean"
    lean.write_text("#!/bin/sh\n")
    lean.chmod(0o755)
    return r


def lignes_code(chemin: Path) -> list[str]:
    return [x for x in chemin.read_text(encoding="utf-8").splitlines() if not x.lstrip().startswith("#")]


# ---- garde par les bits de mode (sans root) --------------------------------------------------------------------------------

def test_garde_arbres_cas_sain(tmp_path):
    r = arbre_sain(tmp_path)
    p = appeler("arbres_lisibles_par_tous", str(r))
    assert p.returncode == 0 and p.stdout == "", p.stdout + p.stderr


def test_garde_arbres_artefact_olean_0600(tmp_path):
    """L'artefact de l'incident : Mathlib.olean en -rw------- (cache de Mathlib), dossiers traversables."""
    r = arbre_sain(tmp_path)
    olean = r / ".lake" / "build" / "lib" / "lean" / "Mathlib.olean"
    olean.chmod(0o600)
    p = appeler("arbres_lisibles_par_tous", str(r))
    assert p.returncode == 1 and "Mathlib.olean" in p.stdout and "1 chemin(s)" in p.stdout


@pytest.mark.parametrize("quoi, mode", [("dossier", 0o750), ("dossier", 0o754), ("executable", 0o744)])
def test_garde_arbres_autres_artefacts(tmp_path, quoi, mode):
    r = arbre_sain(tmp_path)
    cible = r / ".lake" / "build" if quoi == "dossier" else r / "lean"
    cible.chmod(mode)
    try:
        p = appeler("arbres_lisibles_par_tous", str(r))
    finally:
        cible.chmod(0o755)
    assert p.returncode == 1 and str(cible) in p.stdout


def test_garde_arbres_arbre_absent(tmp_path):
    p = appeler("arbres_lisibles_par_tous", str(tmp_path / "absent"))
    assert p.returncode == 2 and "find en échec" in p.stdout


def test_garde_arbres_plusieurs_arbres(tmp_path):
    a, b = arbre_sain(tmp_path / "a"), arbre_sain(tmp_path / "b")
    (b / "lean").chmod(0o700)
    p = appeler("arbres_lisibles_par_tous", str(a), str(b))
    assert p.returncode == 1 and str(b / "lean") in p.stdout


# ---- garde par l'utilisateur (runuser) : seulement en root, avec `nobody` à la place de `bac` --------------------------------

def _runuser_possible() -> bool:
    if os.geteuid() != 0 or shutil.which("runuser") is None:
        return False
    try:
        import pwd
        pwd.getpwnam("nobody")
    except KeyError:
        return False
    return True


@pytest.mark.skipif(not _runuser_possible(), reason="runuser exige root et l'utilisateur nobody")
def test_garde_runuser_cas_sain_et_artefact():
    base = Path(tempfile.mkdtemp(prefix="garde-lisibilite-", dir="/tmp"))
    try:
        base.chmod(0o755)   # /tmp est traversable ; le dossier temporaire doit l'être aussi pour nobody
        r = arbre_sain(base)
        olean = r / ".lake" / "build" / "lib" / "lean" / "Mathlib.olean"
        sain = appeler("lisibles_par", "nobody", str(r), str(r / ".lake"), str(olean))
        assert sain.returncode == 0, sain.stdout + sain.stderr
        olean.chmod(0o600)
        art = appeler("lisibles_par", "nobody", str(r), str(olean))
        assert art.returncode == 1 and "Mathlib.olean : non lisible par nobody" in art.stdout
        olean.chmod(0o644)
        (r / ".lake").chmod(0o744)
        dos = appeler("lisibles_par", "nobody", str(r / ".lake"))
        assert dos.returncode == 1 and "dossier non traversable" in dos.stdout
    finally:
        for d in [base, *base.rglob("*")]:
            if d.is_dir():
                d.chmod(0o755)
        shutil.rmtree(base)


# ---- installateur v2 : ordre et changement minimal ----------------------------------------------------------------------------

def test_installateur_v2_ordre():
    t = INST_V2.read_text(encoding="utf-8")
    assert subprocess.run(["bash", "-n", str(INST_V2)], capture_output=True, timeout=30).returncode == 0
    i_gow = t.index("chmod -R go-w /opt/elan /opt/mathlib /opt/pybac\n")
    i_arx = t.index("chmod -R a+rX /opt/elan /opt/mathlib /opt/pybac\n")
    i_arb = t.index("if ! F=$(arbres_lisibles_par_tous /opt/elan /opt/mathlib /opt/pybac); then")
    i_bac = t.index('if ! F=$(lisibles_par bac "${ECHANTILLON[@]}"); then')
    i_fst = t.index("/etc/fstab", i_gow)
    assert i_gow < i_arx < i_arb < i_bac < i_fst
    assert "/opt/mathlib/.lake/build/lib/lean/Mathlib.olean" in t and '"$OLEAN"' in t
    for chemin in ("/opt ", "/opt/harnais ", "/opt/pybac/bin/python"):
        assert chemin in t[t.index("ECHANTILLON=("):i_bac]
    assert 'runuser -u bac -- test -x "$x"' in t and 'for x in "$LEAN" /opt/pybac/bin/python; do' in t
    assert t.count("exit 5") >= 4


def test_installateur_v2_rien_d_autre():
    """Toute ligne de code de la v1 reste, dans le même ordre ; les ajouts sont la garde et ses appels."""
    v1, v2 = lignes_code(INST_V1), lignes_code(INST_V2)
    it = iter(v2)
    assert all(any(x == y for y in it) for x in v1), "une ligne de la v1 a changé ou a bougé"
    ajouts = [x for x in v2 if x not in v1]
    assert len(ajouts) <= 40
    assert not re.search(r"(?<![./-])\b(rm|curl|apt-get|chown|useradd|mount|umount|git|lake|pip)\b", "\n".join(ajouts))


# ---- pilote v7 -------------------------------------------------------------------------------------------------------------------

def test_pilote_v7_emploie_installateur_v2():
    t = PIL_V7.read_text(encoding="utf-8")
    code = "\n".join(lignes_code(PIL_V7))
    assert "installer_chaine_v1" not in code
    assert '"$V2/installer_chaine_v2.sh"' in code and "timeout 5400 bash /root/installer_chaine_v2.sh" in code
    assert 'V2="$ICI/../lean_essai_d1a_v2"' in code
    assert (PIL_V7.parent / "../lean_essai_d1a_v2/installer_chaine_v2.sh").resolve() == INST_V2
    assert "procedure-poste-local-d1a-v7.md" in t


def test_pilote_v7_bornes_ssh():
    texte = PIL_V7.read_text(encoding="utf-8")
    appels = [x for x in texte.splitlines() if '"${S[@]}"' in x and not x.lstrip().startswith("#") and "S=(" not in x]
    assert len(appels) >= 10 and all('"${S[@]}" timeout ' in x for x in appels)
    assert "ConnectTimeout=" in texte and "ServerAliveInterval=" in texte and "ServerAliveCountMax=" in texte
    assert subprocess.run(["bash", "-n", str(PIL_V7)], capture_output=True, timeout=30).returncode == 0


def test_pilote_v7_cle_d_hote_pour_scp():
    """Rapport du poste, incident 5 : la première copie précède tout ssh ; scp doit enregistrer la clé d'hôte lui-même."""
    code = lignes_code(PIL_V7)
    c = [x for x in code if x.startswith("C=(scp ")]
    s = [x for x in code if x.startswith("S=(ssh ")]
    assert len(c) == 1 and len(s) == 1
    assert "-o StrictHostKeyChecking=accept-new" in c[0] and "-o StrictHostKeyChecking=accept-new" in s[0]
    assert "StrictHostKeyChecking=no" not in "\n".join(code)
    premier = next(x for x in code if '"${C[@]}"' in x or '"${S[@]}"' in x)
    assert '"${C[@]}"' in premier   # c'est bien scp qui touche le serveur en premier


def test_pilote_v7_cache_du_resolveur_vide_avant_la_sonde():
    """Rapport du poste, incident 6 : faux « ouverte » du résolveur système lu dans le cache rempli par la sonde « avant »."""
    code = lignes_code(PIL_V7)
    i_cou = next(i for i, x in enumerate(code) if "/root/couper_reseau_v1.sh" in x)
    i_vid = [i for i, x in enumerate(code) if x.strip() == '"${S[@]}" timeout 60 resolvectl flush-caches']
    i_son = next(i for i, x in enumerate(code) if "sonde_reseau_v1.py --attendu fermee" in x)
    assert len(i_vid) == 1 and i_cou < i_vid[0] < i_son


def test_pilote_v7_rien_d_autre():
    v6 = [x.replace("installer_chaine_v1.sh", "installer_chaine_v2.sh").replace('"$V1/installer', '"$V2/installer')
          .replace('C=(scp -i "$CLE" "${O[@]}")', 'C=(scp -i "$CLE" -o StrictHostKeyChecking=accept-new "${O[@]}")')
          for x in lignes_code(PIL_V6)]
    v7 = lignes_code(PIL_V7)
    ajouts = ('V2="$ICI/../lean_essai_d1a_v2"', '  "${S[@]}" timeout 60 resolvectl flush-caches')
    assert [x for x in v7 if x not in ajouts] == v6
    assert all(v7.count(a) == 1 for a in ajouts)
    assert stat.S_IMODE(PIL_V7.stat().st_mode) & 0o100 and stat.S_IMODE(INST_V2.stat().st_mode) & 0o100
