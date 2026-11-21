"""Essais du lanceur v11 (correction du filtre « programme à épingler » ; noms propres à la version).

Ce que ces essais montrent (aucun appel réel, aucune clé, aucune dépense ; jamais `registres/`) :
1. **filtre** : une commande d'Astra `[interpréteur courant, -I, -B, script]` dont seul le script est épinglé passe la
   déclaration, que l'interpréteur soit sous `/usr/` ou un lien hors de `/usr/` (environnement virtuel, simulé par un lien dans le
   dossier d'essai pour que l'essai dise la même chose sous les deux interpréteurs) ; la cible résolue de l'interpréteur est
   écartée de même ; **artefacts** : un autre programme non épinglé hors de `/usr/`, un autre lien vers le même interpréteur, et
   une commande sans aucun programme épinglé restent refusés ; **contraste** : la v10, au même cas, refuse ; **mutation** : le
   filtre de la v10 remis dans la v11 refait le refus ;
2. **noms propres à la version** : `VERSION`, dossier de sortie, suffixe, v10 comptée parmi les versions déjà lancées ;
3. **le reste de la v10, inchangé** : hors de la chaîne de documentation du module, les seules lignes changées sont celles
   des substitutions nommées ;
4. **essai à blanc éteint** de la v11 (moteur simulé), s'il y a la matière v3 : code 0, run au suffixe v11.
"""
import ast
import difflib
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
V10 = RACINE / "scripts/lancer_course_auto_conception_v10.py"
V11 = RACINE / "scripts/lancer_course_auto_conception_v11.py"


def _charger(nom, chemin: Path, source: str | None = None):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    if source is None:
        spec.loader.exec_module(m)
    else:
        exec(compile(source, str(chemin), "exec"), m.__dict__)
    return m


L = _charger("lancer_course_auto_conception_v11", V11)
L10 = _charger("lancer_course_auto_conception_v10_pour_v11", V10)

FILTRE_V10 = ('            fichiers = [x for x in b["commande"] if isinstance(x, str) and os.path.isfile(x) and not '
              'x.startswith(("/usr/", "/bin/"))]')
FILTRE_V11 = ('            interpretes = {sys.executable, os.path.realpath(sys.executable)}  # v11 : l\'interpréteur qui joue '
              'le lanceur, et sa cible\n'
              '            fichiers = [x for x in b["commande"] if isinstance(x, str) and os.path.isfile(x) and not '
              'x.startswith(("/usr/", "/bin/"))\n'
              '                        and x not in interpretes]')


# --- 1. filtre -------------------------------------------------------------------------------------------------------------


def _fixe():
    rel, sha = L.PIECES["configuration"]
    octets = (RACINE / rel).read_bytes()
    assert hashlib.sha256(octets).hexdigest() == sha
    return json.loads(octets)


def _declaration(commande_astra: list) -> dict:
    return {"version": "essai", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": L.CLE_CLAUDE_TENTATIVE,
                   "porte_plafond": {"type": "commande", "commande": ["porte-d-essai"], "delai_s": 5}},
        "argon": {"type": "commande_externe", "commande": ["bash", "enveloppe-d-essai.sh"], "nom_cle": "CLE_ESSAI_A",
                  "porte_plafond": {"type": "environnement"}, "url_etat_relais": f"http://127.0.0.1:{L.PORT_RELAIS_ARGON}"},
        "astra": {"type": "commande_externe", "commande": commande_astra, "modele_propose": "modele-essai-astra",
                  "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"},
                  "url_etat_relais": "http://127.0.0.1:8790"}}}


def _depart(*empreintes) -> dict:
    return {"variable_cle_claude": L.CLE_CLAUDE_TENTATIVE,
            "commandes_epinglees": {"astra": {"empreintes": list(empreintes), "epreuve": "R-essai"}},
            "especes_optionnelles": {"astra": {"declaree": True}}}


def _script(d: Path, nom="astra.py") -> Path:
    s = d / nom
    s.write_text("import sys\nsys.stdin.read()\nprint('{}')\n", encoding="utf-8")
    return s


def _cmd(prog, script: Path) -> list:
    return [str(prog), "-I", "-B", str(script), "--url-relais", "http://127.0.0.1:8790"]


@pytest.fixture
def interprete_hors_usr(tmp_path, monkeypatch):
    """Interpréteur courant vu comme un lien hors de `/usr/` (le cas de `.venv/bin/python`), quel que soit l'interpréteur qui
    joue l'essai : `sys.executable` devient un lien du dossier d'essai vers la cible résolue de l'interpréteur réel."""
    lien = tmp_path / "venv" / "bin" / "python"
    lien.parent.mkdir(parents=True)
    lien.symlink_to(os.path.realpath(sys.executable))
    monkeypatch.setattr(sys, "executable", str(lien))
    return lien


def _accepte(module, decl, depart):
    res = module.verifier_declaration(decl, _fixe(), depart)
    return "prop-astra" in [e["etiquette"] for e in res["especes_actives"]]


def test_cas_sain_interprete_reel(tmp_path):
    s = _script(tmp_path)
    assert _accepte(L, _declaration(_cmd(sys.executable, s)), _depart(L.sha256_fichier(s)))


def test_cas_sain_interprete_lien_hors_usr(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    assert not str(interprete_hors_usr).startswith(("/usr/", "/bin/"))
    assert _accepte(L, _declaration(_cmd(interprete_hors_usr, s)), _depart(L.sha256_fichier(s)))


def test_cas_sain_cible_resolue_de_l_interprete(tmp_path, monkeypatch):
    """La cible résolue est écartée même hors de `/usr/` : copie de l'interpréteur dans le dossier d'essai, liée."""
    cible = tmp_path / "py" / "python3-copie"
    cible.parent.mkdir()
    cible.write_bytes(Path(os.path.realpath(sys.executable)).read_bytes())
    lien = tmp_path / "venv-python"
    lien.symlink_to(cible)
    monkeypatch.setattr(sys, "executable", str(lien))
    s = _script(tmp_path)
    assert _accepte(L, _declaration(_cmd(cible, s)), _depart(L.sha256_fichier(s)))


def test_v10_refuse_le_meme_cas(tmp_path, interprete_hors_usr):
    """Contraste : le défaut du tri (§ 1) rejoué sur la v10 ; l'essai pouvait échouer."""
    s = _script(tmp_path)
    with pytest.raises(L10.Refus, match="programme non épinglé"):
        L10.verifier_declaration(_declaration(_cmd(interprete_hors_usr, s)), _fixe(), _depart(L10.sha256_fichier(s)))


def test_artefact_autre_programme_non_epingle(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    autre = _script(tmp_path, "autre.py")
    autre.write_text("print('autre programme')\n", encoding="utf-8")   # contenu propre : empreinte autre que celle du script
    assert L.sha256_fichier(autre) != L.sha256_fichier(s)
    cmd = _cmd(interprete_hors_usr, s) + [str(autre)]
    with pytest.raises(L.Refus, match="programme non épinglé"):
        L.verifier_declaration(_declaration(cmd), _fixe(), _depart(L.sha256_fichier(s)))


def test_artefact_autre_lien_vers_le_meme_interprete(tmp_path, interprete_hors_usr):
    """Seuls `sys.executable` et sa cible résolue sont écartés : un autre chemin vers le même interpréteur reste à épingler."""
    s = _script(tmp_path)
    autre_lien = tmp_path / "ailleurs" / "python"
    autre_lien.parent.mkdir()
    autre_lien.symlink_to(os.path.realpath(sys.executable))
    with pytest.raises(L.Refus, match="programme non épinglé"):
        L.verifier_declaration(_declaration(_cmd(autre_lien, s)), _fixe(), _depart(L.sha256_fichier(s)))


def test_artefact_script_non_epingle(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    with pytest.raises(L.Refus, match="programme non épinglé"):
        L.verifier_declaration(_declaration(_cmd(interprete_hors_usr, s)), _fixe(), _depart("0" * 64))


def test_artefact_commande_sans_programme(tmp_path, interprete_hors_usr):
    """L'interpréteur seul, sans fichier épinglé : `fichiers` vide, refus (comme sous `/usr/` en v10)."""
    cmd = [str(interprete_hors_usr), "-c", "print(1)", "--url-relais", "http://127.0.0.1:8790"]
    with pytest.raises(L.Refus, match="programme non épinglé"):
        L.verifier_declaration(_declaration(cmd), _fixe(), _depart(L.sha256_fichier(interprete_hors_usr)))


def test_mutation_filtre_v10_remis_attrape(tmp_path, interprete_hors_usr):
    source = V11.read_text(encoding="utf-8")
    assert source.count(FILTRE_V11) == 1
    mute = _charger("lancer_course_auto_conception_v11_mute", V11, source.replace(FILTRE_V11, FILTRE_V10))
    s = _script(tmp_path)
    with pytest.raises(mute.Refus, match="programme non épinglé"):
        mute.verifier_declaration(_declaration(_cmd(interprete_hors_usr, s)), _fixe(), _depart(mute.sha256_fichier(s)))


# --- 2. noms propres à la version --------------------------------------------------------------------------------------------


def test_noms_propres_v11():
    assert L.VERSION == "lancer_course_auto_conception_v11"
    assert L.DOSSIER_SORTIES == Path("/home/user/sorties-course-auto-conception-v11")
    assert L.SUFFIXE_RUN == "-course-auto-conception-v11"
    assert L.SUFFIXES_DEJA_LANCEE == L10.SUFFIXES_DEJA_LANCEE[:-1] + ("-course-auto-conception-v10", L.SUFFIXE_RUN)
    assert L.SORTIES_AUTRES_VERSIONS == L10.SORTIES_AUTRES_VERSIONS + (L10.DOSSIER_SORTIES,)
    assert L.DOSSIER_SORTIES not in L.SORTIES_AUTRES_VERSIONS


# --- 3. le reste de la v10, inchangé -----------------------------------------------------------------------------------------


def _corps(chemin: Path) -> list:
    texte = chemin.read_text(encoding="utf-8")
    doc = ast.parse(texte).body[0]
    assert isinstance(doc, ast.Expr) and isinstance(doc.value, ast.Constant)
    return texte.splitlines()[doc.end_lineno:]


CHANGEES = {
    "retirees": [
        'VERSION = "lancer_course_auto_conception_v10"',
        'DOSSIER_SORTIES = Path("/home/user/sorties-course-auto-conception-v10")     # v10 : dossier de sortie neuf (nom de version)',
        'SUFFIXE_RUN = "-course-auto-conception-v10"',
        '                        SUFFIXE_RUN)                                  # v10 : la v9 comptée parmi les versions déjà lancées',
        '                           Path("/home/user/sorties-course-auto-conception-v9"))',
        '        raise Refus(f"tentative v10 déjà lancée ({v7}) : une seule (une relance est une nouvelle version et un mot de la mère)")',
        '    texte = (f"# Registre des GO dérivé (course d\'auto-conception, lanceur v10) — lignes nommées seulement\\n\\n"',
        FILTRE_V10,
        '                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-auto-conception-v10"), parts, depart)',
    ],
    "ajoutees": [
        'VERSION = "lancer_course_auto_conception_v11"',
        'DOSSIER_SORTIES = Path("/home/user/sorties-course-auto-conception-v11")     # v11 : dossier de sortie neuf (nom de version)',
        'SUFFIXE_RUN = "-course-auto-conception-v11"',
        '                        "-course-auto-conception-v10",',
        '                        SUFFIXE_RUN)                                  # v11 : la v10 comptée parmi les versions déjà lancées',
        '                           Path("/home/user/sorties-course-auto-conception-v9"), Path("/home/user/sorties-course-auto-conception-v10"))',
        '        raise Refus(f"tentative v11 déjà lancée ({v7}) : une seule (une relance est une nouvelle version et un mot de la mère)")',
        '    texte = (f"# Registre des GO dérivé (course d\'auto-conception, lanceur v11) — lignes nommées seulement\\n\\n"',
    ] + FILTRE_V11.split("\n") + [
        '                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-auto-conception-v11"), parts, depart)',
    ],
}


def test_le_reste_de_la_v10_inchange():
    retirees, ajoutees = [], []
    for ligne in difflib.unified_diff(_corps(V10), _corps(V11), lineterm="", n=0):
        if ligne.startswith(("---", "+++", "@@")):
            continue
        (retirees if ligne.startswith("-") else ajoutees).append(ligne[1:])
    assert retirees == CHANGEES["retirees"]
    assert ajoutees == CHANGEES["ajoutees"]


def test_documentation_garde_le_texte_de_la_v10():
    doc10 = ast.get_docstring(ast.parse(V10.read_text(encoding="utf-8")), clean=False)
    doc11 = ast.get_docstring(ast.parse(V11.read_text(encoding="utf-8")), clean=False)
    tete, _, reste = doc11.partition("\n\nTexte de la v10 :\n\n")
    assert reste == doc10
    assert "ne lève aucun des blocages" in tete


# --- 4. essai à blanc éteint ---------------------------------------------------------------------------------------------------


def _matiere_v3():
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"{L.REF_MAIN}:{L.MATIERE[0]}"], capture_output=True)
    return p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == L.MATIERE[1]


@pytest.mark.skipif(not _matiere_v3(), reason="matière v3 absente de la référence de main")
def test_essai_a_blanc_eteint_v11(tmp_path):
    d = tmp_path / "ab"
    assert L.principal(["--a-blanc", str(d)]) == 0
    (run,) = list((d / "runs").iterdir())
    assert run.name.endswith(L.SUFFIXE_RUN)
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text(encoding="utf-8"))
    assert dep["lanceur"]["version"] == L.VERSION and dep["interrupteurs_v10"]
