"""Essais R5 du pilote v9 (réparation R-2439, troisième essai) de l'essai Lean D-1a : copie de
`test_lean_essai_pilote_v8.py` (inchangé, R12), portée sur `piloter_poste_v9.sh` (mêmes essais de l'installateur v2, de
l'essai « bac lit Mathlib.olean » et du pilote), plus l'essai R5 « le vérificateur compile sur la machine »
(`essai_compilation_verificateur_v1.sh` : ordre dans le pilote, cas sain et artefacts sur un faux `lean` lu par `nobody`,
et, avec la chaîne épinglée (`LEAN_ESSAI_D1A_CHAINE`), sur le vrai vérificateur v5 et sur la v4), le passage aux v5 de
l'exécuteur, de l'épreuve et du vérificateur, et le contrôle `cmp` du vérificateur après la coupure. Texte de la v8 :
Essais R5 de l'installateur v2 et du pilote v8 (harnais v7, second tour) de l'essai Lean D-1a (R-2415). Copie de
`test_lean_essai_installer_v2.py` (inchangé, R12 : il éprouve le pilote v7 du premier tour), étendue au pilote v8 et à
l'essai « bac lit Mathlib.olean ». Texte d'origine : Essais R5 de l'installateur v2 et du pilote v7 de l'essai Lean D-1a (R-2415) : garde de lisibilité par `bac` (cas sain et
artefact, sur de vrais fichiers 0644 et 0600 d'un dossier temporaire), ordre des commandes de l'installateur, emploi de
l'installateur v2 par le pilote, et aucun autre changement que ceux déclarés par rapport à la v1 et à la v6. Aucun réseau,
aucune machine ; rien n'est lancé en root hors du dossier temporaire."""
import json
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
PIL_V8 = RACINE / "scripts" / "lean_essai_d1a_v8" / "piloter_poste_v8.sh"
PIL_V7 = RACINE / "scripts" / "lean_essai_d1a_v9" / "piloter_poste_v9.sh"   # nom gardé dans les essais : le pilote éprouvé
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
    assert "procedure-poste-local-d1a-v10.md" in t


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
    i_son = next(i for i, x in enumerate(code) if "sonde_reseau_v2.py --attendu fermee" in x)
    assert len(i_vid) == 1 and i_cou < i_vid[0] < i_son


def test_pilote_v7_sondes_v2():
    """Les sondes du pilote (avant, après coupure, fin) sont la v2 ; l'exécuteur garde la v1 dans /opt/harnais."""
    code = "\n".join(lignes_code(PIL_V7))
    assert code.count("python3 -B /root/sonde_reseau_v2.py --attendu") == 3
    assert "/root/sonde_reseau_v1.py" not in code
    assert '"$PAQ/sonde_reseau_v2.py"' in code and '"$PAQ/sonde_reseau_v1.py" \\\n      "root@$IP:/opt/harnais/"' in code


def test_pilote_v7_dossier_ssh():
    code = lignes_code(PIL_V7)
    lignes = [x for x in code if ".ssh" in x]
    assert lignes == ['[ -d "$HOME/.ssh" ] || install -d -m 700 "$HOME/.ssh"']
    i_ssh = code.index(lignes[0])
    assert all(i_ssh < i for i, x in enumerate(code) if '"${C[@]}"' in x or '"${S[@]}"' in x)


def test_pilote_v7_essai_lecture_bac_avant_la_coupure():
    code = lignes_code(PIL_V7)
    i_ins = next(i for i, x in enumerate(code) if "bash /root/installer_chaine_v2.sh" in x)
    i_ess = [i for i, x in enumerate(code) if x.strip() == '"${S[@]}" timeout 120 bash /root/essai_lecture_bac_v1.sh']
    i_apr = next(i for i, x in enumerate(code) if x.startswith("elif [ \"$PHASE\" = apres ]"))
    i_cou = next(i for i, x in enumerate(code) if "/root/couper_reseau_v1.sh" in x and "timeout" in x)
    assert len(i_ess) == 1 and i_ins < i_ess[0] < i_apr < i_cou
    assert '"$V8/essai_lecture_bac_v1.sh"' in "\n".join(code)


ESSAI_LECTURE = PIL_V8.parent / "essai_lecture_bac_v1.sh"


@pytest.mark.skipif(not _runuser_possible(), reason="runuser exige root et l'utilisateur nobody")
@pytest.mark.parametrize("mode, code_attendu", [(0o644, 0), (0o600, 1)])
def test_essai_lecture_bac_sain_et_artefact(mode, code_attendu):
    """Essai R5 joué tel quel sur un faux Mathlib.olean, `nobody` à la place de `bac` : 0644 lu (code 0), 0600 refusé
    (code 1) ; l'artefact interne 0600 est toujours refusé et le témoin 0644 toujours lu."""
    base = Path(tempfile.mkdtemp(prefix="essai-lecture-", dir="/tmp"))
    try:
        base.chmod(0o755)
        olean = base / "Mathlib.olean"
        olean.write_bytes(b"olean")
        olean.chmod(mode)
        p = subprocess.run(["bash", str(ESSAI_LECTURE), str(olean), "nobody"], capture_output=True, text=True, timeout=60)
    finally:
        shutil.rmtree(base)
    lignes = [json.loads(x) for x in p.stdout.splitlines()]
    par_cas = {x["cas"]: x for x in lignes}
    assert p.returncode == code_attendu, p.stdout + p.stderr
    assert par_cas["sain"]["conforme"] is (mode == 0o644)
    assert par_cas["temoin-0644"]["conforme"] is True and par_cas["temoin-0644"]["lu"] is True
    assert par_cas["artefact-0600"]["conforme"] is True and par_cas["artefact-0600"]["lu"] is False
    assert par_cas["bilan"]["conforme"] is (code_attendu == 0)
    assert not list(Path("/tmp").glob("essai-lecture-bac-*"))   # dossier temporaire du script retiré


def test_essai_lecture_bac_texte():
    assert subprocess.run(["bash", "-n", str(ESSAI_LECTURE)], capture_output=True, timeout=30).returncode == 0
    t = ESSAI_LECTURE.read_text(encoding="utf-8")
    assert "OLEAN=${1:-/opt/mathlib/.lake/build/lib/lean/Mathlib.olean}" in t and "U=${2:-bac}" in t
    assert stat.S_IMODE(ESSAI_LECTURE.stat().st_mode) & 0o100


def test_pilote_v9_rien_d_autre():
    """Lignes de code du v8 toutes gardées, dans l'ordre, sauf les remplacements déclarés ; ajouts déclarés seulement."""
    remplacements = {
        '  "${C[@]}" "$V2/installer_chaine_v2.sh" "$V1/couper_reseau_v1.sh" "$PAQ/sonde_reseau_v2.py" "$ICI/essai_lecture_bac_v1.sh" \\':
        '  "${C[@]}" "$V2/installer_chaine_v2.sh" "$V1/couper_reseau_v1.sh" "$PAQ/sonde_reseau_v2.py" "$V8/essai_lecture_bac_v1.sh" \\',
    }
    v8 = [remplacements.get(x, x).replace("executeur_bac_v4.py", "executeur_bac_v5.py")
          .replace("epreuve_isolement_v4.py", "epreuve_isolement_v5.py")
          .replace("verificateur_noyau_v4.lean", "verificateur_noyau_v5.lean") for x in lignes_code(PIL_V8)]
    v9 = lignes_code(PIL_V7)
    ajouts = ('V8="$ICI/../lean_essai_d1a_v8"',
              '      "$ICI/essai_compilation_verificateur_v1.sh" "$PAQ/verificateur_noyau_v5.lean" \\',
              '  "${S[@]}" timeout 900 bash /root/essai_compilation_verificateur_v1.sh /root/verificateur_noyau_v5.lean',
              '  "${S[@]}" timeout 60 cmp /root/verificateur_noyau_v5.lean /opt/harnais/noyau/verificateur_noyau_v5.lean')
    assert [x for x in v9 if x not in ajouts] == v8
    assert all(v9.count(a) == 1 for a in ajouts)
    assert stat.S_IMODE(PIL_V7.stat().st_mode) & 0o100


def test_pilote_v9_aucun_v4_du_harnais():
    code = "\n".join(lignes_code(PIL_V7))
    for v4 in ("executeur_bac_v4", "epreuve_isolement_v4", "verificateur_noyau_v4"):
        assert v4 not in code
    assert code.count("python3 -B /opt/harnais/epreuve_isolement_v5.py") == 4
    assert '"$PAQ/executeur_bac_v5.py" "$PAQ/epreuve_isolement_v5.py"' in code
    assert '"${C[@]}" "$PAQ/verificateur_noyau_v5.lean" "root@$IP:/opt/harnais/noyau/"' in code


ESSAI_COMPIL = PIL_V7.parent / "essai_compilation_verificateur_v1.sh"


def test_pilote_v9_essai_compilation_avant_la_coupure():
    code = lignes_code(PIL_V7)
    i_lec = next(i for i, x in enumerate(code) if x.strip() == '"${S[@]}" timeout 120 bash /root/essai_lecture_bac_v1.sh')
    i_com = [i for i, x in enumerate(code) if "bash /root/essai_compilation_verificateur_v1.sh" in x]
    i_apr = next(i for i, x in enumerate(code) if x.startswith("elif [ \"$PHASE\" = apres ]"))
    i_cou = next(i for i, x in enumerate(code) if "/root/couper_reseau_v1.sh" in x and "timeout" in x)
    assert len(i_com) == 1 and i_lec < i_com[0] < i_apr < i_cou
    assert code[i_com[0]].startswith('  "${S[@]}" timeout ')
    # les deux fichiers de l'essai partent dans la première copie, avant tout ssh
    i_cop = next(i for i, x in enumerate(code) if '"$ICI/essai_compilation_verificateur_v1.sh"' in x)
    assert '"$PAQ/verificateur_noyau_v5.lean"' in code[i_cop] and i_cop < i_lec
    assert code[i_cop + 1] == '      "root@$IP:/root/"'


def test_pilote_v9_meme_verificateur_avant_et_apres_la_coupure():
    code = lignes_code(PIL_V7)
    i_cmp = [i for i, x in enumerate(code) if " cmp /root/verificateur_noyau_v5.lean /opt/harnais/noyau/verificateur_noyau_v5.lean" in x]
    i_cop = next(i for i, x in enumerate(code) if '"${C[@]}" "$PAQ/verificateur_noyau_v5.lean" "root@$IP:/opt/harnais/noyau/"' in x)
    i_epi = next(i for i, x in enumerate(code) if "epreuve_isolement_v5.py epingler-verificateur" in x)
    assert len(i_cmp) == 1 and i_cop < i_cmp[0] < i_epi
    assert code[i_cmp[0]].startswith('  "${S[@]}" timeout ')
    assert "|| " not in code[i_cmp[0]]   # set -e : une différence arrête le pilote


def test_essai_compilation_texte():
    assert subprocess.run(["bash", "-n", str(ESSAI_COMPIL)], capture_output=True, timeout=30).returncode == 0
    t = ESSAI_COMPIL.read_text(encoding="utf-8")
    assert "V=${1:-/root/verificateur_noyau_v5.lean}" in t and "CH=${2:-/opt/harnais/chaine-v1.json}" in t
    assert "U=${3:-bac}" in t and "set -euo pipefail" in t
    assert stat.S_IMODE(ESSAI_COMPIL.stat().st_mode) & 0o100


FAUX_LEAN = """#!/bin/sh
# faux lean des essais : exige d'être lancé par l'utilisateur du bac, lit le fichier (échoue s'il est illisible), puis
# se comporte selon MODE
f="$1"
[ "$f" = --version ] && { [ "{mode}" = sans-version ] && exit 1; echo "Lean (version 4.35.0, faux lean des essais)"; exit 0; }
[ "$(id -un)" = "{utilisateur}" ] || { echo "$f:1:1: error: lancé par $(id -un), {utilisateur} attendu"; exit 4; }
cat "$f" > /dev/null || exit 3
case "{mode}" in
  sain|sans-version) if grep -q identifiantInconnuEssaiR5V1 "$f"; then echo "$f:1:1: error: Unknown identifier"; exit 1; fi; exit 0 ;;
  avertit) echo "$f:1:1: warning: deprecated"; exit 0 ;;
  accepte-tout) exit 0 ;;
  refuse-tout) echo "$f:1:1: error: Unknown identifier"; exit 1 ;;
esac
"""


def _jouer_faux(mode: str, utilisateur: str):
    base = Path(tempfile.mkdtemp(prefix="essai-compil-", dir="/tmp"))
    try:
        base.chmod(0o755)
        lean = base / "lean"
        lean.write_text(FAUX_LEAN.replace("{mode}", mode).replace("{utilisateur}", utilisateur))
        lean.chmod(0o755)
        verif = base / "verificateur_noyau_v5.lean"
        verif.write_text("-- vérificateur factice\n")
        verif.chmod(0o600)   # l'essai doit en faire une copie lisible par l'utilisateur du bac
        chaine = base / "chaine-v1.json"
        chaine.write_text(json.dumps({"lean": str(lean), "lean_path": "/inexistant"}))
        p = subprocess.run(["bash", str(ESSAI_COMPIL), str(verif), str(chaine), utilisateur], capture_output=True,
                           text=True, timeout=60)
    finally:
        shutil.rmtree(base)
    lignes = [json.loads(x) for x in p.stdout.splitlines()]
    return p, {x["cas"]: x for x in lignes}


@pytest.mark.skipif(not _runuser_possible(), reason="runuser exige root et l'utilisateur nobody")
@pytest.mark.parametrize("mode, code_attendu, sain_ok, artefact_ok", [
    ("sain", 0, True, True),           # cas sain : compile sans message ; copie cassée refusée
    ("avertit", 1, False, False),      # un avertissement (code 0) n'est pas « sans message » ; la copie « compile »
    ("accepte-tout", 1, True, False),  # l'essai doit voir que la copie cassée n'est pas refusée
    ("refuse-tout", 1, False, True),   # le vérificateur ne compile pas : arrêt (cause du second essai)
    ("sans-version", 1, True, True),   # `lean --version` en échec : arrêt dit, jamais muet
])
def test_essai_compilation_faux_lean(mode, code_attendu, sain_ok, artefact_ok):
    p, par_cas = _jouer_faux(mode, "nobody")
    assert p.returncode == code_attendu, p.stdout + p.stderr
    assert par_cas["sain"]["conforme"] is sain_ok and par_cas["artefact-copie-cassee"]["conforme"] is artefact_ok
    assert par_cas["bilan"]["conforme"] is (code_attendu == 0)
    assert not list(Path("/tmp").glob("essai-compilation-verificateur-*"))   # dossier temporaire du script retiré


CHAINE = os.environ.get("LEAN_ESSAI_D1A_CHAINE", "")


@pytest.mark.skipif(not CHAINE, reason="chaîne épinglée absente : LEAN_ESSAI_D1A_CHAINE non posée (essai sauté, pas réussi)")
@pytest.mark.parametrize("version, code_attendu", [("v5", 0), ("v4", 1)])
def test_essai_compilation_chaine_epinglee(version, code_attendu):
    """Le script tel que joué sur la machine, sur la chaîne épinglée hors machine (utilisateur courant) : la v5 passe, la v4
    (cause du second essai) arrête le pilote."""
    verif = RACINE / "src" / "controle_ia" / "lean_essai" / f"verificateur_noyau_{version}.lean"
    utilisateur = subprocess.run(["id", "-un"], capture_output=True, text=True).stdout.strip()
    p = subprocess.run(["bash", str(ESSAI_COMPIL), str(verif), CHAINE, utilisateur], capture_output=True, text=True,
                       timeout=900)
    par_cas = {x["cas"]: x for x in map(json.loads, p.stdout.splitlines())}
    assert p.returncode == code_attendu, p.stdout[-2000:] + p.stderr[-2000:]
    assert par_cas["artefact-copie-cassee"]["conforme"] is True
    assert par_cas["sain"]["conforme"] is (version == "v5")
    assert "version 4.35.0," in par_cas["bilan"]["version_lean"]
    if version == "v4":
        assert "CollectAxioms.collect" in par_cas["sain"]["messages"]
