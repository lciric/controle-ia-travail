"""Essais R5 de la chaîne de lancement v6 de la course de l'étape B bis (apprentissage des sondes sur la tâche) :
`scripts/amorce_bbis_v6.sh` et `scripts/lancer_bbis_v6.sh`, écrits pour lever les trois arrêts certains de R-3160
(`docs/notes/prealables-course-etape-b-bis-v1/rapport-portillon-et-pilote-v1.md`). Chaque garde neuve a son cas sain et son
artefact :

- amorce : différence avec la v5 bornée aux six écarts déclarés ; plancher d'essais égal au compte mesuré ; motifs d'extraction
  (les 63 fichiers de la fiche de code en vigueur extraits, les interdits toujours absents ; artefact : motifs de la v5, onze
  manquants) ; bloc « fiche-sur-l-arbre » (contrôle avancé du registre et de la fiche) ; clé d'interface du conteneur exigée
  avant la minuterie ; essai local sans écriture ;
- lanceur : garde « commit de la course » (arbre extrait à COMMIT, garde d'entrée de la marche rejouée par le code de l'arbre ;
  artefacts : commit sans les lignes d'inscription — que la v5 laisse passer —, fichier de la fiche hors des motifs, empreinte
  autre) ; garde « commit joignable » ; image ; plafond de prix ; sous-commande `essais-du-commit` (plancher franchi, manqué
  d'un essai, essai en échec).

Ce fichier ne s'appelle pas `test_t07bbis_*` exprès : l'amorce n'extrait et ne joue sur la machine que `tests/test_t07bbis_*` ;
le compte d'essais de la machine ne dépend donc pas de lui. Dépôts jetables seulement, aucun réseau ; aucune donnée ni aucun
résultat de 7a, 7b, T0.6, T0.7 ou P3-bis."""
from __future__ import annotations

import difflib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import pytest

import aide_t07bbis_depot_v1 as ad
from controle_ia.scellement import empreinte, sceller
from controle_ia.t07bbis import commun_v1 as cm
from controle_ia.t07bbis import registre_bbis_v2 as rb

RACINE = ad.RACINE_DEPOT
AMORCE_V5 = RACINE / "scripts" / "amorce_bbis_v5.sh"
AMORCE = RACINE / "scripts" / "amorce_bbis_v6.sh"
LANCER_V5 = RACINE / "scripts" / "lancer_bbis_v5.sh"
LANCER = RACINE / "scripts" / "lancer_bbis_v6.sh"
FICHE_EN_VIGUEUR = RACINE / "registres" / "t07-etape-b-bis" / "code-bbis-v2.json"
# compte mesuré sur l'arbre extrait par les motifs de la v6 (`lancer_bbis_v6.sh essais-du-commit`, sans réseau) ; la sortie de
# la mesure et son empreinte sont dans le brouillon d'addendum (brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon1.md)
PLANCHER_MESURE = 151
ONZE = ["scripts/amorce_bbis_v5.sh", "scripts/lancer_bbis_v5.sh"] + [
    f"scripts/{nom}_bbis_v{k}.{ext}" for nom, ext in (("amorce_repetition", "sh"), ("lancer_repetition", "sh"),
                                                     ("repetition_carte", "py")) for k in (1, 2, 3)]
INTERDITS = ["docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json", "docs/notes/x/y.md", "scripts/mots_et_cout_t06_v3.py",
             "scripts/extraire_mesures_epreuve_t06_v1.py", "scripts/fabrique_factice_mots_et_cout_t06_v1.py",
             "diag/r/lecture-sondes-t06.json", "scripts/amorce_bbis_v6.sh", "scripts/lancer_bbis_v6.sh",
             "scripts/lancer_repetition_bbis_v4.sh", "brouillons/x.md", "runs/r/manifeste.json", "donnees/r/x.npz"]


def _motifs(amorce: Path) -> list[str]:
    m = re.findall(r"^MOTIFS='(.*?)'$", amorce.read_text(encoding="utf-8"), re.S | re.M)
    assert len(m) == 1
    return m[0].split("\n")


def _extrait(chemin: Path, nom: str) -> str:
    m = re.findall(rf"^# >>> {re.escape(nom)}\b[^\n]*\n(.*?)^# <<< {re.escape(nom)}$", chemin.read_text(encoding="utf-8"),
                   re.S | re.M)
    assert len(m) == 1, (nom, len(m))
    return m[0]


def _env(**k) -> dict:
    e = {c: v for c, v in os.environ.items() if not c.startswith("GIT_")}       # jamais les variables GIT_* de la session
    e.update({"PYTHON_BBIS": sys.executable})
    e.update(k)
    return e


# ------------------------------------------------------------------------------------------ amorce : différence avec la v5

def test_amorce_v6_ne_differe_de_la_v5_que_par_les_ecarts_declares():
    v5, v6 = (p.read_text(encoding="utf-8").split("\n") for p in (AMORCE_V5, AMORCE))
    retires = [l[2:] for l in difflib.ndiff(v5, v6) if l.startswith("- ")]
    assert len(retires) == 2 and retires[0] == "MIN_ESSAIS=176" and "lancer_bbis_v4.sh verifier-destruction" in retires[1]
    ajoutes = [l[2:] for l in difflib.ndiff(v5, v6) if l.startswith("+ ")]
    hors_commentaires = [l for l in ajoutes if l.strip() and not l.lstrip().startswith("#")]
    bloc = _extrait(AMORCE, "fiche-sur-l-arbre").split("\n")
    reste = [l for l in hors_commentaires if l not in bloc]
    # hors du bloc neuf : le plancher, les onze motifs, la garde de la clé, la ligne d'empreinte, les deux lignes d'appel du
    # bloc, la ligne de fin d'instance (nom du lanceur)
    assert len(reste) == 1 + 11 + 1 + 1 + 2 + 1, reste
    assert sorted(l[1:-1] for l in reste if l.startswith("/scripts/")) == sorted(ONZE)
    for nom in ("arret-et-traces", "cuda-du-pilote", "minuterie", "carte-et-cuda", "copie-des-fichiers-cites",
                "commit-local-des-entrees", "compte-des-essais"):                # blocs marqués : texte inchangé
        assert _extrait(AMORCE, nom) == _extrait(AMORCE_V5, nom) or nom == "arret-et-traces"
    assert subprocess.run(["bash", "-n", str(AMORCE)]).returncode == 0
    # la branche de sortie, le dépôt, l'accord de calcul et la marche sont ceux de la v5
    for motif in (r"^BR_SORTIE=(.*)$", r"^DEPOT_URL_OFFICIEL=(.*)$", r"^GO_ATTENDU=(.*)$", r"-m (controle_ia\.t07bbis\.marche_v\d+)"):
        a, b = (re.findall(motif, p.read_text(encoding="utf-8"), re.M) for p in (AMORCE_V5, AMORCE))
        assert a == b and len(a) == 1, motif


def test_plancher_d_essais_egal_au_compte_mesure_et_ligne_d_essais_commune():
    texte = AMORCE.read_text(encoding="utf-8")
    m = re.findall(r"^MIN_ESSAIS=(\d+)$", texte, re.M)
    assert m == [str(PLANCHER_MESURE)]                                # cas sain : une seule ligne, le compte mesuré
    assert AMORCE_V5.read_text(encoding="utf-8").count("MIN_ESSAIS=176") == 1          # artefact : le plancher de la v5
    assert PLANCHER_MESURE < 176
    ligne = 'PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py --basetemp='
    assert texte.count(ligne) == 1 and LANCER.read_text(encoding="utf-8").count(ligne) == 1   # même ligne des deux côtés


# ------------------------------------------------------------------------------------------------ amorce : motifs d'extraction

def _arbre_jouet(d: Path, motifs: list[str]) -> tuple[list, list]:
    fiche = sorted(json.loads(FICHE_EN_VIGUEUR.read_text(encoding="utf-8"))["fichiers"])
    assert len(fiche) == 63 and set(ONZE) <= set(fiche)
    ad.depot_vide(d)
    for p in fiche + INTERDITS:
        ad.ecrire(d, p, f"{p}\n")
        ad.ecrire(d, p + ".sha256", "x\n")
    ad.committer(d, "arbre jouet")
    ad.appliquer_motifs(d, motifs)
    return [p for p in fiche if not (d / p).is_file()], [p for p in INTERDITS if (d / p).exists() or (d / (p + ".sha256")).exists()]


def test_motifs_v6_extraient_les_63_fichiers_de_la_fiche_et_aucun_interdit(tmp_path):
    manque, present = _arbre_jouet(tmp_path / "sain", _motifs(AMORCE))
    assert manque == [] and present == []                             # cas sain : toute la fiche, aucun interdit
    manque, present = _arbre_jouet(tmp_path / "artefact", _motifs(AMORCE_V5))
    assert manque == sorted(ONZE) and present == []                   # artefact : motifs de la v5, les onze manquent
    v5, v6 = _motifs(AMORCE_V5), _motifs(AMORCE)
    assert [l for l in v6 if l not in v5] == [f"/{p}*" for p in ONZE] and [l for l in v5 if l not in v6] == []
    assert [l for l in v6 if l.startswith("!")] == [l for l in v5 if l.startswith("!")]        # exclusions inchangées
    assert not any("docs/notes" in l for l in v6)
    assert AMORCE.read_text(encoding="utf-8").count("docs/notes/*) arret") == 2    # les deux interdits de citation restent


# ------------------------------------------------------------------------------------------ amorce : fiche sur l'arbre extrait

DATES = ("2026-11-14T12:00:00Z", "2026-11-16T12:00:00Z", "2026-11-17T12:00:00Z", "2026-11-17T12:00:01Z")


def _arbre_fiche(d: Path, lignes=("SCELLEMENT-BBIS", "CODE-BBIS", "CODE-BBIS", "GO-BBIS")) -> Path:
    for p in ("src/a.py", "scripts/b.sh"):
        ad.ecrire(d, p, f"code {p}\n")
    fiches = []
    for v in (1, 2):
        f = ad.ecrire(d, f"registres/t07-etape-b-bis/code-v{v}.json", json.dumps(
            {"fichiers": {"src/a.py": empreinte(d / "src/a.py"), **({"scripts/b.sh": empreinte(d / "scripts/b.sh")} if v == 2 else
                                                                   {"scripts/absent-de-la-premiere-fiche.sh": "0" * 64})}}))
        fiches.append((f"registres/t07-etape-b-bis/code-v{v}.json", sceller(f)))
    t = ad.ecrire(d, "prereg/texte.md", "texte\n")
    g = ad.ecrire(d, "registres/t07-etape-b-bis/go.txt", "accord\n")
    cites = {"SCELLEMENT-BBIS": [("prereg/texte.md", sceller(t))], "CODE-BBIS": fiches, "GO-BBIS": [("registres/t07-etape-b-bis/go.txt", sceller(g))]}
    corps = "# registre propre jouet\n\n"
    for date, k in zip(DATES, lignes):
        chemin, sha = cites[k].pop(0) if len(cites[k]) > 1 else cites[k][0]
        corps += f"| {k} | {date} | {chemin} | {sha} |\n"
    ad.ecrire(d, "registres/t07-etape-b-bis-v1.md", corps)
    return d


def _fiche_sur_l_arbre(d: Path) -> subprocess.CompletedProcess:
    return ad.jouer(_extrait(AMORCE, "fiche-sur-l-arbre") + 'fiche_sur_l_arbre "$1"\n', d)


def test_fiche_sur_l_arbre_cas_sain_et_artefacts(tmp_path):
    r = _fiche_sur_l_arbre(_arbre_fiche(tmp_path / "sain"))
    assert r.returncode == 0 and "2 fichiers de la fiche présents" in r.stdout, r.stdout + r.stderr   # la seconde fiche fait foi
    d = _arbre_fiche(tmp_path / "sans-lignes", lignes=("SCELLEMENT-BBIS",))        # arrêt 2 de R-3160 : commit sans inscriptions
    r = _fiche_sur_l_arbre(d)
    assert r.returncode == 1 and "ligne CODE-BBIS absente" in r.stdout
    d = _arbre_fiche(tmp_path / "sans-go", lignes=("SCELLEMENT-BBIS", "CODE-BBIS", "CODE-BBIS"))
    assert "ligne GO-BBIS absente" in _fiche_sur_l_arbre(d).stdout
    d = _arbre_fiche(tmp_path / "absent")                                          # arrêt 3 : fichier de la fiche non extrait
    (d / "scripts/b.sh").unlink()
    r = _fiche_sur_l_arbre(d)
    assert r.returncode == 1 and "scripts/b.sh : fichier du code cité par la fiche absent" in r.stdout
    d = _arbre_fiche(tmp_path / "empreinte")
    (d / "src/a.py").write_text("autre\n", encoding="utf-8")
    r = _fiche_sur_l_arbre(d)
    assert r.returncode == 1 and "src/a.py : empreinte autre" in r.stdout
    d = _arbre_fiche(tmp_path / "compagnon")
    (d / "registres/t07-etape-b-bis/code-v2.json.sha256").unlink()
    r = _fiche_sur_l_arbre(d)
    assert r.returncode == 1 and "code-v2.json (ligne CODE-BBIS)" in r.stdout
    d = _arbre_fiche(tmp_path / "trois")
    with open(d / "registres/t07-etape-b-bis-v1.md", "a", encoding="utf-8") as f:
        f.write(f"| CODE-BBIS | 2026-11-18T12:00:00Z | registres/t07-etape-b-bis/code-v2.json | {'a' * 64} |\n")
    r = _fiche_sur_l_arbre(d)                       # une troisième ligne de fiche : la marche la refuse, ce contrôle aussi
    assert r.returncode == 1 and "CODE-BBIS en 3 exemplaires" in r.stdout
    r = _fiche_sur_l_arbre(tmp_path / "vide")
    assert r.returncode == 1 and "registre propre absent" in r.stdout
    texte = AMORCE.read_text(encoding="utf-8")       # le contrôle est joué après le commit local, avant les paquets et le modèle
    assert texte.index("\ncommit_local_entrees\n") < texte.index('FS=$(fiche_sur_l_arbre "$D") || arret') < texte.index("# 4. paquets")


def test_fiche_sur_l_arbre_jamais_plus_severe_que_la_marche_sur_l_arbre_reel(tmp_path):
    """Sur la fiche et le registre en vigueur du dépôt (copie des seuls fichiers cités), le contrôle avancé passe."""
    d = tmp_path / "arbre"
    fiche = json.loads(FICHE_EN_VIGUEUR.read_text(encoding="utf-8"))["fichiers"]
    reg = (RACINE / "registres/t07-etape-b-bis-v1.md").read_text(encoding="utf-8")
    cites = [c[3].strip() for c in (l.split("|") for l in reg.splitlines()) if len(c) >= 6 and "/" in c[3]]
    for p in list(fiche) + cites + [c + ".sha256" for c in cites]:
        ad.ecrire(d, p, "").write_bytes((RACINE / p).read_bytes())
    ad.ecrire(d, "registres/t07-etape-b-bis-v1.md", reg)
    r = _fiche_sur_l_arbre(d)
    assert r.returncode == 0 and "63 fichiers de la fiche présents" in r.stdout, r.stdout + r.stderr


# ------------------------------------------------------------------------- amorce : clé du conteneur, essai local sans écriture

def test_cle_d_interface_du_conteneur_exigee_avant_la_minuterie():
    texte = AMORCE.read_text(encoding="utf-8")
    garde = [l for l in texte.split("\n") if l.startswith('[ -n "${CONTAINER_API_KEY:-}" ] || ')]
    assert len(garde) == 1
    assert texte.index(garde[0]) < texte.index("minuterie < /dev/null &")          # avant l'armement
    jouer = lambda env: subprocess.run(["bash", "-c", "set -uo pipefail\n" + garde[0] + "\necho ARMEE\n"], capture_output=True,
                                       text=True, env={"PATH": os.environ["PATH"], **env})
    r = jouer({"CONTAINER_API_KEY": "valeur-factice"})
    assert r.returncode == 0 and r.stdout.strip() == "ARMEE" and "valeur-factice" not in r.stdout     # cas sain, valeur jamais affichée
    for env in ({}, {"CONTAINER_API_KEY": ""}):                                    # artefacts : absente, vide
        r = jouer(env)
        assert r.returncode == 2 and "clé d'interface du conteneur absente" in r.stdout and "ARMEE" not in r.stdout
    assert 'CONTAINER_API_KEY' not in "".join(l for l in AMORCE_V5.read_text(encoding="utf-8").split("\n") if l.startswith("[ -n"))


def test_essai_local_de_l_amorce_v6_sans_ecriture(tmp_path):
    base = {"AMORCE_ESSAI_LOCAL": "1", "COMMIT": "c" * 40, "BRANCHE_CODE": "main", "RUN_7B": ad.RUN_7B, "BRANCHE_7B": "calcul/x",
            "RUN_BBIS": "20261118-090000-bbis-v2", "ECHEANCE_UTC_S": "1795000000", "GO_ID": "GO-2026-11-14-09",
            "RACINE_AMORCE": str(tmp_path / "r")}
    r = subprocess.run(["bash", str(AMORCE)], capture_output=True, text=True, env=_env(**base))
    assert r.returncode == 0 and "aucun dossier" in r.stdout and not (tmp_path / "r").exists()
    r = subprocess.run(["bash", str(AMORCE)], capture_output=True, text=True, env=_env(**{**base, "COMMIT": "abc"}))
    assert r.returncode == 2 and "COMMIT" in r.stdout and not (tmp_path / "r").exists()


# --------------------------------------------------------------------------------------- lanceur : dépôt jetable de la course

def _depot_course(d: Path, cites=("src/x.py", "scripts/amorce_bbis_v5.sh"), n_essais: int | None = None, echec: bool = False) -> dict:
    """Dépôt jetable : C0 porte le « code » (dont un lien `src/controle_ia` vers le code du dépôt de travail, pour que la garde
    d'entrée de la marche se rejoue depuis l'arbre extrait) ; C1 ajoute la fiche de code (qui cite C0 et les fichiers `cites`),
    l'extrait de l'accord et les lignes du registre propre ; C2 change un fichier de la fiche (empreinte autre). `origin` : dépôt
    nu nommé comme celui de l'amorce, qui porte `main` à C1 (C2 n'est pas poussé)."""
    ad.depot_vide(d)
    ad.ecrire(d, "src/x.py", "print('code jouet')\n")
    os.symlink(RACINE / "src" / "controle_ia", d / "src" / "controle_ia")
    for p in ("scripts/amorce_bbis_v5.sh", "scripts/hors_des_motifs.sh"):
        ad.ecrire(d, p, f"# {p}\n")
    if n_essais is not None:
        ad.ecrire(d, "tests/test_t07bbis_jouet.py", "import pytest\n\n\n@pytest.mark.parametrize('k', range(%d))\n"
                  "def test_jouet(k):\n    assert %s\n" % (n_essais, "k != 0" if echec else "True"))
    (d / "prereg").mkdir()
    for nom in ("T0.7-etape-B-bis-v1.md", "T0.7-etape-B-bis-v1.md.sha256"):
        (d / "prereg" / nom).write_bytes((RACINE / "prereg" / nom).read_bytes())
    rb.ajouter_ligne_propre(d, rb.REGISTRE_PROPRE, "SCELLEMENT-BBIS", 1789000000, cm.TEXTE, cm.TEXTE_SHA256)
    c0 = ad.committer(d, "code et ligne de scellement du texte (aucune ligne d'inscription de la fiche ni de l'accord)")
    ep = ad.epreuve(d)
    fiche = rb.ecrire_fiche_code(d, "registres/t07-etape-b-bis/code-bbis-v1.json", c0, {p: empreinte(d / p) for p in cites}, ad.E, ep)
    g = ad.ecrire(d, "registres/go-extraits/GO-BBIS-v1.md", "| GO-2026-11-14-09 | extrait jouet |\n")
    for k, t, chemin, sha in (("CODE-BBIS", 1789000100, "registres/t07-etape-b-bis/code-bbis-v1.json", fiche["sha256"]),
                              ("GO-BBIS", 1789000200, "registres/go-extraits/GO-BBIS-v1.md", sceller(g))):
        rb.ajouter_ligne_propre(d, rb.REGISTRE_PROPRE, k, t, chemin, sha)
    c1 = ad.committer(d, "lignes du registre propre")
    ad.distant_officiel(d, d.parent / (d.name + "-distant"), branches=("main",))
    ad.git(d, "fetch", "-q", "origin")
    ad.ecrire(d, "src/x.py", "print('code jouet, changé après la fiche')\n")
    c2 = ad.committer(d, "fichier de la fiche changé")
    ad.git(d, "checkout", "-q", "--detach", c1)
    return {"d": d, "c0": c0, "c1": c1, "c2": c2}


def _offre(chemin: Path, **k) -> Path:
    o = {"id": 99, "carte": "A100 SXM4 80GB", "coeurs": 32, "memoire_vive_mo": 256000, "disque_go": 200, "stockage_usd_h": 0.05,
         "etiquette": "bbis-t07-v1", "cuda_max_good": 13.0, "prix_usd_h": 1.1}
    o.update(k)
    chemin.write_text(json.dumps({c: v for c, v in o.items() if v is not None}), encoding="utf-8")
    return chemin


def _commande(lanceur: Path, x: dict, offre: Path, commit: str, tmp: Path, image: str = "python:3.11-bookworm", branche: str = "main"):
    tmp.mkdir(exist_ok=True)
    r = subprocess.run(["bash", str(lanceur), "commande", str(x["d"]), str(offre), "99", commit, branche, ad.RUN_7B, "calcul/x",
                        "20261118-090000-bbis-v2", "1795000000", "feu GO-2026-11-14-09", "0", image],
                       capture_output=True, text=True, env=_env(TMPDIR=str(tmp)))
    assert list(tmp.iterdir()) == [], list(tmp.iterdir())            # aucun dossier jetable laissé (essai local, arbre du commit)
    return r


avant_l_echeance = pytest.mark.skipif(time.time() > rb._instant(rb.ECHEANCE_GO),
                                      reason="échéance de la ligne d'accord de calcul dépassée : la garde de création refuse tout")


@avant_l_echeance
def test_commande_v6_commit_de_la_course_cas_sain_et_artefacts(tmp_path):
    x = _depot_course(tmp_path / "depot")
    offre = _offre(tmp_path / "offre.json")
    avant = ad.git(x["d"], "status", "--porcelain", "--untracked-files=all") + ad.git(x["d"], "for-each-ref")
    r = _commande(LANCER, x, offre, x["c1"], tmp_path / "tmp")
    assert r.returncode == 0 and "vastai create instance 99" in r.stdout and f"-e COMMIT={x['c1']}" in r.stdout, r.stdout + r.stderr
    assert "/root/amorce_bbis_v6.sh" in r.stdout and empreinte(AMORCE)[:16] in r.stdout     # cas sain : l'amorce v6, son empreinte
    # artefact, arrêt 2 de R-3160 : COMMIT antérieur aux lignes d'inscription ; la tête de la mère les porte
    r = _commande(LANCER, x, offre, x["c0"], tmp_path / "tmp")
    assert r.returncode == 2 and "commit de la course" in r.stdout and "CODE-BBIS absente" in r.stdout, r.stdout
    assert "vastai create" not in r.stdout
    r5 = _commande(LANCER_V5, x, offre, x["c0"], tmp_path / "tmp")                 # la v5 ne voyait pas cette faute
    assert r5.returncode == 0 and "vastai create instance 99" in r5.stdout
    apres = ad.git(x["d"], "status", "--porcelain", "--untracked-files=all") + ad.git(x["d"], "for-each-ref")
    assert avant == apres and not (x["d"] / ".git" / "worktrees").exists()   # rien d'écrit dans le dépôt de la mère par le lanceur
    # artefact : fichier de la fiche changé après elle (C2, poussé pour passer la garde « commit joignable »)
    ad.git(x["d"], "push", "-q", "origin", f"{x['c2']}:refs/heads/main")
    ad.git(x["d"], "fetch", "-q", "origin")
    r = _commande(LANCER, x, offre, x["c2"], tmp_path / "tmp")
    assert r.returncode == 2 and "src/x.py : empreinte ≠ fiche" in r.stdout and "vastai create" not in r.stdout, r.stdout


@avant_l_echeance
def test_commande_v6_fichier_de_la_fiche_hors_des_motifs(tmp_path):
    x = _depot_course(tmp_path / "depot", cites=("src/x.py", "scripts/hors_des_motifs.sh"))      # arrêt 3 de R-3160
    r = _commande(LANCER, x, _offre(tmp_path / "offre.json"), x["c1"], tmp_path / "tmp")
    assert r.returncode == 2 and "scripts/hors_des_motifs.sh : fichier du code cité par la fiche de CODE-BBIS absent" in r.stdout
    assert "vastai create" not in r.stdout
    r5 = _commande(LANCER_V5, x, _offre(tmp_path / "offre.json"), x["c1"], tmp_path / "tmp")
    assert r5.returncode == 0                                         # la v5 imprimait la commande


@avant_l_echeance
def test_commande_v6_commit_joignable_image_et_prix(tmp_path):
    x = _depot_course(tmp_path / "depot")
    offre = _offre(tmp_path / "offre.json")
    r = _commande(LANCER, x, offre, x["c2"], tmp_path / "tmp")        # C2 n'est pas poussé
    assert r.returncode == 2 and "absent de la branche main du dépôt distant" in r.stdout and "vastai create" not in r.stdout
    r = _commande(LANCER, x, offre, x["c1"], tmp_path / "tmp", branche="prep/absente")
    assert r.returncode == 2 and "branche prep/absente absente du dépôt distant" in r.stdout
    r = _commande(LANCER, x, offre, x["c1"], tmp_path / "tmp", image="python:3.12-bookworm")
    assert r.returncode == 2 and "image python:3.12-bookworm ≠ python:3.11-bookworm" in r.stdout
    for prix, code in ((1.4, 0), (1.41, 2), (None, 2), ("1.1", 2), (0, 2), (True, 2)):
        r = _commande(LANCER, x, _offre(tmp_path / f"offre-{prix}.json", prix_usd_h=prix), x["c1"], tmp_path / "tmp")
        assert r.returncode == code, (prix, r.stdout)
        assert ("vastai create" in r.stdout) == (code == 0) and (code == 0 or "prix de l'offre" in r.stdout)


def test_arbre_du_commit_reconstruit_l_extraction_de_l_amorce(tmp_path):
    x = _depot_course(tmp_path / "depot")
    corps = _extrait(LANCER, "arbre-du-commit") + 'arbre_du_commit "$1" "$2" "$3" "$4"\n'
    r = ad.jouer(corps, x["d"], x["c1"], AMORCE, tmp_path / "arbre")
    assert r.returncode == 0, r.stdout + r.stderr
    a = tmp_path / "arbre"
    assert (a / "src/x.py").is_file() and (a / "scripts/amorce_bbis_v5.sh").is_file() and (a / "registres/t07-etape-b-bis-v1.md").is_file()
    assert not (a / "scripts/hors_des_motifs.sh").exists()            # hors des motifs : non extrait
    assert ad.git(a, "rev-parse", "HEAD^") == x["c1"] and ad.git(a, "status", "--porcelain", "--untracked-files=all") == ""
    r = ad.jouer(corps, x["d"], x["c1"], AMORCE, tmp_path / "arbre")
    assert r.returncode == 2 and "déjà présent" in r.stdout          # artefacts : dossier présent, commit absent, amorce illisible
    r = ad.jouer(corps, x["d"], "d" * 40, AMORCE, tmp_path / "arbre-2")
    assert r.returncode == 2 and "absent du dépôt" in r.stdout
    r = ad.jouer(corps, x["d"], x["c1"], x["d"] / "src/x.py", tmp_path / "arbre-3")
    assert r.returncode == 2 and "illisibles dans l'amorce" in r.stdout


def test_essais_du_commit_plancher_franchi_manque_et_essai_en_echec(tmp_path):
    jouer = lambda x, dos: subprocess.run(["bash", str(LANCER), "essais-du-commit", str(x["d"]), x["c1"], str(dos)],
                                          capture_output=True, text=True, env=_env())
    x = _depot_course(tmp_path / "sain", n_essais=PLANCHER_MESURE)
    r = jouer(x, tmp_path / "mesure-sain")
    assert r.returncode == 0 and f"{PLANCHER_MESURE} passés ≥ {PLANCHER_MESURE}" in r.stdout, r.stdout + r.stderr
    assert (tmp_path / "mesure-sain" / "essais.txt").is_file() and (tmp_path / "mesure-sain" / "fichiers-de-l-arbre.txt").is_file()
    r = jouer(x, tmp_path / "mesure-sain")
    assert r.returncode == 2 and "déjà présent" in r.stdout          # R12 : une mesure n'est jamais réécrite
    x = _depot_course(tmp_path / "manque", n_essais=PLANCHER_MESURE - 1)
    r = jouer(x, tmp_path / "mesure-manque")
    assert r.returncode == 2 and f"{PLANCHER_MESURE - 1} passés < {PLANCHER_MESURE}" in r.stdout, r.stdout
    x = _depot_course(tmp_path / "echec", n_essais=PLANCHER_MESURE + 5, echec=True)
    r = jouer(x, tmp_path / "mesure-echec")
    assert r.returncode == 2 and "essais en échec" in r.stdout, r.stdout
