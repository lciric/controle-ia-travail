"""Essais R5 de la chaîne de l'instance de B bis, ajoutés après la contre-lecture du code (modèle C,
`brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-code-modele-c-v1.md`), chacun avec son cas sain et son artefact :
B1 (commit de la fiche de `CODE-BBIS` ancêtre de la tête, `marche_v1.gardes_d_entree`) ; B2 (motifs d'extraction de l'amorce
couvrant tous les chemins que les essais de l'instance lisent) ; M1 (commit local des entrées, arbre propre, branche de sortie
créée depuis COMMIT) ; M2 (codes fermés de `marche_v1.main`) ; M3 (compte des essais passés lu sur la ligne de pytest) ; m5
(essai local de l'amorce sans aucune écriture, garde d'offre de `lancer commande`) ; m7 (boucle de copie des fichiers cités par le
registre propre). Dépôts jetables seulement ; aucune donnée de 7a, 7b, T0.7 ni de P3-bis."""
from __future__ import annotations

import json
import os
import re
import subprocess
import time
from pathlib import Path

import pytest

import aide_t07bbis_depot_v1 as ad
from controle_ia.gardes import GardeArret
from controle_ia.t07bbis import marche_v1 as ma
from controle_ia.t07bbis import registre_bbis_v1 as rb

RACINE = ad.RACINE_DEPOT


# ------------------------------------------------------------------------------------------------------------ B1

def test_gardes_d_entree_commit_de_la_fiche_ancetre_cas_sain_et_artefacts(tmp_path, monkeypatch):
    monkeypatch.setenv("BBIS_INSTANCE", "1")
    x = ad.depot_code(tmp_path / "sain")
    g = ma.gardes_d_entree(x["d"], ad.RUN_7B)                         # cas sain : fiche → C0, tête C1 qui porte les lignes
    assert g["tete"] == x["c1"] != x["c0"] == g["fiche"]["commit"]
    assert set(g["lignes"]) == {"SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"}
    ad.ecrire(x["d"], "local.txt")                                    # tête = commit local des entrées (descendant de C1)
    ad.committer(x["d"], "entrées locales", "local.txt")
    assert ma.gardes_d_entree(x["d"], ad.RUN_7B)["fiche"]["commit"] == x["c0"]
    # (i) fiche citant un commit d'une branche voisine (non ancêtre), ou un commit absent du dépôt
    with pytest.raises(GardeArret, match="n'est pas un ancêtre de la tête"):
        ma.gardes_d_entree(ad.depot_code(tmp_path / "voisine", cite="voisine")["d"], ad.RUN_7B)
    with pytest.raises(GardeArret, match="absent du dépôt"):
        ma.gardes_d_entree(ad.depot_code(tmp_path / "absent", cite="absent")["d"], ad.RUN_7B)
    # (ii) fichier du code modifié après C0 (commit postérieur), puis retiré
    ad.ecrire(x["d"], "src/x.py", "print('code modifié')\n")
    ad.committer(x["d"], "code modifié", "src/x.py")
    with pytest.raises(GardeArret, match="empreinte ≠ fiche de CODE-BBIS"):
        ma.gardes_d_entree(x["d"], ad.RUN_7B)
    (x["d"] / "src" / "x.py").unlink()
    with pytest.raises(GardeArret, match="absent : arrêt"):
        ma.gardes_d_entree(x["d"], ad.RUN_7B)
    # (iii) tête = C0, sans les lignes du registre propre
    y = ad.depot_code(tmp_path / "c0")
    ad.git(y["d"], "checkout", "-q", y["c0"])
    with pytest.raises(GardeArret, match="absent"):
        ma.gardes_d_entree(y["d"], ad.RUN_7B)
    # même garde, appelée par la session (`registre_bbis_v1 ancetre RACINE COMMIT`, jouée par `lancer commande`)
    z = ad.depot_code(tmp_path / "session")
    assert rb.exiger_ancetre_de_la_fiche(z["d"], z["c1"])["tete"] == z["c1"]
    with pytest.raises(GardeArret, match="n'est pas un ancêtre"):
        rb.exiger_ancetre_de_la_fiche(z["d"], z["v"])
    with pytest.raises(GardeArret, match="40 caractères"):
        rb.exiger_ancetre(z["d"], "c0ffee")


# ------------------------------------------------------------------------------------------------------------ B2

OBLIGATOIRES = ["scripts/lancer_bbis_v1.sh", "scripts/amorce_bbis_v1.sh", "scripts/enumerer_issues_bbis_v1.py",
                "scripts/epreuve_niveau_deux_plis_bbis_v1.py", "prereg/T0.7-etape-B-bis-v1.md",
                "prereg/T0.7-etape-B-bis-v1.md.sha256", "prereg/P3-consignes-v1.md", "prereg/P3-consignes-v1.md.sha256",
                "tests/conftest.py", "src/controle_ia/t06/test_croise.py", "requirements-gpu.txt",
                "registres/t07-etape-b-bis-v1.md", "registres/t07-etape-b-bis/code-bbis-v1.json", "registres/scellements-v1.md",
                "registres/scellements-v1.md.sha256", "registres/go-extraits/GO-BBIS-v1.md"]
INTERDITS = ["diag/r/lecture-sondes-t06.json", "diag/r/lecture-sondes-t06.json.sha256", "scripts/extraire_mesures_epreuve_t06_v1.py",
             "scripts/mots_et_cout_t06_v3.py", "docs/notes/piece-mots-et-cout-v1/x.md", "docs/notes/g0/config.json",
             "runs/r/manifeste.json", "donnees/r/mesures-t06.npz", "registres/autre-v1.md", "docs/procedures/x.md"]


def _chemins_du_paquet() -> list[str]:
    """Code et essais du paquet (dossiers exacts du dépôt de travail) : tout ce que la fiche de `CODE-BBIS` peut citer et tout ce
    que `tests/test_t07bbis_*.py` importe ou ouvre."""
    rel = lambda p: str(p.relative_to(RACINE))
    return sorted({rel(p) for p in (RACINE / "src" / "controle_ia" / "t07bbis").glob("*.py")}
                  | {rel(p) for p in (RACINE / "tests").glob("test_t07bbis_*.py")}
                  | {rel(p) for p in (RACINE / "tests").glob("aide_t07bbis_*.py")})


def _manquants(d: Path, lignes: list[str]) -> tuple[list, list]:
    ad.depot_vide(d)
    for p in OBLIGATOIRES + INTERDITS + _chemins_du_paquet():
        ad.ecrire(d, p, f"{p}\n")
    ad.committer(d, "arbre jouet")
    ad.appliquer_motifs(d, lignes)
    manque = [p for p in OBLIGATOIRES + _chemins_du_paquet() if not (d / p).is_file()]
    present = [p for p in INTERDITS if (d / p).exists()]
    return manque, present


def test_motifs_de_l_amorce_couvrent_les_chemins_des_essais(tmp_path):
    m = ad.motifs()
    assert "/scripts/lancer_bbis_v1.sh*" in m
    assert len(_chemins_du_paquet()) >= 20
    manque, present = _manquants(tmp_path / "sain", m)
    assert manque == [] and present == []                             # cas sain : tout présent, rien d'interdit
    manque, _ = _manquants(tmp_path / "artefact", [l for l in m if "lancer_bbis_v1" not in l])
    assert manque == ["scripts/lancer_bbis_v1.sh"]                    # artefact : motif de lancer retiré → l'essai échoue


# ------------------------------------------------------------------------------------------------------------ m7

REGISTRE = "registres/t07-etape-b-bis-v1.md"


def _depot_registre(d: Path, cites: list[str]) -> Path:
    ad.depot_vide(d)
    for p in ("prereg/T0.7-etape-B-bis-v1.md", "prereg/T0.7-etape-B-bis-v1.md.sha256", "docs/verdicts/issue-jouet.json",
              "docs/verdicts/issue-jouet.json.sha256", "registres/t07-etape-b-bis/fiche.json"):
        ad.ecrire(d, p, f"contenu de {p}\n")
    ad.ecrire(d, REGISTRE, "# registre propre jouet\n\n" + "".join(
        f"| CLE-{k}-BBIS | 2026-11-14T12:00:0{k}Z | {c} | {'a' * 64} |\n" for k, c in enumerate(cites)))
    ad.committer(d, "registre jouet")
    ad.appliquer_motifs(d, ad.motifs())
    return d


def test_boucle_de_copie_des_fichiers_cites_sain_et_artefact(tmp_path):
    corps = "D=\"$1\"\nCOPIES=()\n" + ad.extrait("copie-des-fichiers-cites") + 'printf "COPIE %s\\n" "${COPIES[@]+"${COPIES[@]}"}"\n'
    d = _depot_registre(tmp_path / "sain", ["prereg/T0.7-etape-B-bis-v1.md", "docs/verdicts/issue-jouet.json",
                                            "registres/t07-etape-b-bis/fiche.json", "diag/x/absent-de-la-tete.json"])
    assert not (d / "docs" / "verdicts" / "issue-jouet.json").exists()   # hors des motifs : absent avant la copie
    r = ad.jouer(corps, d)
    assert r.returncode == 0, r.stdout + r.stderr
    copies = [l[len("COPIE "):] for l in r.stdout.splitlines() if l.startswith("COPIE ")]
    assert copies == ["docs/verdicts/issue-jouet.json", "docs/verdicts/issue-jouet.json.sha256", "prereg/T0.7-etape-B-bis-v1.md",
                      "prereg/T0.7-etape-B-bis-v1.md.sha256", "registres/t07-etape-b-bis/fiche.json"]
    for p in copies:
        assert (d / p).read_text(encoding="utf-8") == f"contenu de {p}\n"
    assert not (d / "diag" / "x").exists()                            # cité mais absent de la tête : rien n'est écrit
    for interdit in ("docs/notes/g0/x.json", "diag/r/lecture-sondes-t06.json", "donnees/bras-attaque-v1/x.json"):
        d = _depot_registre(tmp_path / interdit.replace("/", "-"), ["prereg/T0.7-etape-B-bis-v1.md", interdit])
        r = ad.jouer(corps, d)
        assert r.returncode == 2 and f"chemin interdit cité : {interdit}" in r.stdout, interdit


# ------------------------------------------------------------------------------------------------------------ M1

def _depot_entrees(d: Path) -> tuple[Path, str, list]:
    """Dépôt à la manière de l'instance : COMMIT (code, .gitignore avec `donnees/`), extraction partielle par les motifs de
    l'amorce, puis entrées de 7b copiées non suivies (`runs/`, `diag/`) ou ignorées (`donnees/`), hors des motifs."""
    ad.depot_vide(d)
    ad.ecrire(d, ".gitignore", "donnees/\n")
    ad.ecrire(d, "src/controle_ia/x.py")
    ad.ecrire(d, "registres/t07-etape-b-bis-v1.md", "# registre\n")
    commit = ad.committer(d, "code")
    ad.appliquer_motifs(d, ad.motifs())
    copies = [f"runs/{ad.RUN_7B}/manifeste.json", f"runs/{ad.RUN_7B}/manifeste.json.sha256",
              f"diag/{ad.RUN_7B}/episodes-t06.json", f"donnees/{ad.RUN_7B}/mesures-t06.npz"]
    for p in copies:
        ad.ecrire(d, p, f"entrée {p}\n")
    return d, commit, copies


def test_commit_local_des_entrees_arbre_propre_et_branche_de_sortie(tmp_path):
    corps = ("D=\"$1\"; COMMIT=\"$2\"; shift 2; COPIES=(\"$@\")\n" + ad.extrait("commit-local-des-entrees")
             + "commit_local_entrees\necho \"ENTREES $ENTREES_LOCALES\"\n")
    d, commit, copies = _depot_entrees(tmp_path / "sain")
    from controle_ia.gardes import etat_git
    assert not etat_git(d)["propre"]                                  # avant : entrées non suivies
    r = ad.jouer(corps, d, commit, *copies)
    assert r.returncode == 0, r.stdout + r.stderr
    tete = ad.git(d, "rev-parse", "HEAD")
    assert f"ENTREES {tete}" in r.stdout and ad.git(d, "rev-parse", "HEAD^") == commit
    assert etat_git(d)["propre"]                                      # cas sain : arbre propre après le commit local
    assert set(ad.git(d, "diff-tree", "-r", "--no-commit-id", "--name-only", commit, tete).splitlines()) == set(copies)
    el = ma.entrees_locales(d, exiger=True)                           # ce que la marche écrit au manifeste
    assert el["commit"] == tete and el["parent"] == commit and set(el["fichiers"]) == set(copies)
    assert el["fichiers"][copies[3]]["objet"] == ad.git(d, "rev-parse", f"HEAD:{copies[3]}")
    # après la marche : sorties non suivies, branche de sortie créée depuis COMMIT ; le commit local n'y entre pas
    ad.ecrire(d, "runs/20261118-090000-bbis-t07/manifeste.json", "sortie\n")
    ad.ecrire(d, "donnees/20261118-090000-bbis-t07/scores-bbis-000.npz", "sortie\n")
    ad.git(d, "checkout", "-q", "-b", "donnees/t07-etape-b-bis-v1", commit)
    assert ad.git(d, "rev-parse", "HEAD") == commit
    assert subprocess.run(["git", "-C", str(d), "merge-base", "--is-ancestor", tete, "HEAD"]).returncode == 1
    assert (d / "runs" / "20261118-090000-bbis-t07" / "manifeste.json").is_file()
    assert (d / "donnees" / "20261118-090000-bbis-t07" / "scores-bbis-000.npz").is_file()
    assert not (d / copies[0]).exists()                               # entrées de 7b retirées de l'arbre, jamais poussées
    # artefacts : un fichier non suivi resté hors des copies ; aucune copie ; parent autre que COMMIT
    d, commit, copies = _depot_entrees(tmp_path / "reste")
    ad.ecrire(d, f"diag/{ad.RUN_7B}/autre-non-copie.json")
    r = ad.jouer(corps, d, commit, *copies)
    assert r.returncode == 2 and "arbre non propre après le commit local des entrées" in r.stdout
    d, commit, copies = _depot_entrees(tmp_path / "vide")
    r = ad.jouer(corps, d, commit)
    assert r.returncode == 2 and "aucune entrée copiée" in r.stdout
    d, commit, copies = _depot_entrees(tmp_path / "parent")
    r = ad.jouer(corps, d, "e" * 40, *copies)
    assert r.returncode == 2 and "parent du commit local des entrées ≠ COMMIT" in r.stdout
    with pytest.raises(GardeArret, match="illisible"):
        ma.entrees_locales(ad.depot_vide(tmp_path / "sans-commit"), exiger=True)
    assert ma.entrees_locales(tmp_path / "sans-commit", exiger=False) is None


# ------------------------------------------------------------------------------------------------------------ M2 (codes)

def test_codes_fermes_de_la_marche(monkeypatch):
    """`main` : 0 scores écrits ; 3 arrêt de débit ; 4 arrêt écrit (M2) ; 2 refus d'une garde d'entrée."""
    monkeypatch.setattr(ma, "gardes_d_entree", lambda racine, run: {"fiche": {"entropie": 2 ** 100}})
    args = ["--racine", ".", "--run-7b", ad.RUN_7B, "--run-bbis", "20261118-090000-bbis-t07", "--travail", "t"]
    for r, code in (({"scores_ecrits": True}, 0), ({"arret_debit": "x", "scores_ecrits": False}, 3),
                    ({"arret_marche": "RuntimeError: CUDA", "etape": "apprentissage et notation", "scores_ecrits": False}, 4)):
        monkeypatch.setattr(ma, "marche", lambda *a, _r=r, **k: _r)
        assert ma.main(args) == code

    def refus(racine, run):
        raise GardeArret("refus d'entrée")
    monkeypatch.setattr(ma, "gardes_d_entree", refus)
    assert ma.main(args) == 2
    texte = (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8")
    assert re.search(r"^    4\) traces; pousser .*ARRÊT ÉCRIT DE LA MARCHE", texte, re.M)


# ------------------------------------------------------------------------------------------------------------ M3

def test_compte_des_essais_passes_et_minimum(tmp_path):
    corps = ad.extrait("compte-des-essais") + 'compte_passes "$1"\n'
    for ligne, n in (("75 passed, 21 skipped, 4 warnings in 12.34s", 75), ("1 failed, 74 passed, 21 skipped in 9.1s", 74),
                     ("21 skipped in 1.0s", 0), ("no tests ran in 0.01s", 0), ("", 0), ("103 passed in 120.5s", 103)):
        r = ad.jouer(corps, ligne)
        assert r.returncode == 0 and r.stdout.strip() == str(n), (ligne, r.stdout)
    texte = (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8")
    m = re.findall(r"^MIN_ESSAIS=(\d+)$", texte, re.M)
    assert len(m) == 1 and int(m[0]) >= 60                            # minimum écrit (compte du rapport des corrections)
    assert "-rs" in texte and 'ligne de compte : $RES"' in texte      # ligne entière au journal, essais sautés nommés


# ------------------------------------------------------------------------------------------------------------ m5

def _offre(chemin: Path, **k) -> Path:
    o = {"id": 99, "carte": "A100 SXM4 80GB", "coeurs": 32, "memoire_vive_mo": 256000, "disque_go": 200, "stockage_usd_h": 0.05,
         "etiquette": "bbis-t07-v1"}
    o.update(k)
    chemin.write_text(json.dumps(o), encoding="utf-8")
    return chemin


def _lancer(*args, env=None):
    e = dict(os.environ)
    e.update({"PYTHON_BBIS": str(Path(os.sys.executable))})
    e.update(env or {})
    return subprocess.run(["bash", str(ad.LANCER), *map(str, args)], capture_output=True, text=True, env=e)


def test_essai_local_sans_ecriture_et_garde_d_offre_de_la_commande(tmp_path):
    base = {"AMORCE_ESSAI_LOCAL": "1", "COMMIT": "c" * 40, "BRANCHE_CODE": "main", "RUN_7B": ad.RUN_7B, "BRANCHE_7B": "calcul/x",
            "RUN_BBIS": "20261118-090000-bbis-t07", "ECHEANCE_UTC_S": "1795000000", "GO_ID": "GO-2026-11-14-09",
            "RACINE_AMORCE": str(tmp_path / "r")}
    r = subprocess.run(["bash", str(ad.AMORCE)], capture_output=True, text=True, env={**os.environ, **base})
    assert r.returncode == 0 and "aucun dossier" in r.stdout and not (tmp_path / "r").exists()   # rien n'est écrit
    x = ad.depot_code(tmp_path / "depot")
    tmp = tmp_path / "tmp"
    tmp.mkdir()
    arguments = lambda offre, commit: ("commande", x["d"], offre, "99", commit, "main", ad.RUN_7B, "calcul/x",
                                       "20261118-090000-bbis-t07", "1795000000", "feu GO-2026-11-14-09", "0",
                                       "python:3.11-bookworm")
    r = _lancer(*arguments(_offre(tmp_path / "offre.json"), x["c1"]), env={"TMPDIR": str(tmp)})
    assert list(tmp.iterdir()) == []                                  # dossier jetable de l'essai local retiré, vide
    if time.time() > rb._instant(rb.ECHEANCE_GO):                     # après l'échéance de la ligne de GO : refus
        assert r.returncode == 2 and "échéance" in r.stdout
    else:
        assert r.returncode == 0 and "vastai create instance 99" in r.stdout, r.stdout
        assert f"-e COMMIT={x['c1']}" in r.stdout
    for faute, motif in (({"id": 98}, "identifiant"), ({"carte": "H200 SXM 141GB"}, "H200"), ({"etiquette": "t07"}, "étiquette")):
        r = _lancer(*arguments(_offre(tmp_path / "faute.json", **faute), x["c1"]), env={"TMPDIR": str(tmp)})
        assert r.returncode == 2 and "hors des bornes" in r.stdout and motif in r.stdout, faute
    if time.time() <= rb._instant(rb.ECHEANCE_GO):
        r = _lancer(*arguments(_offre(tmp_path / "offre.json"), x["v"]), env={"TMPDIR": str(tmp)})
        assert r.returncode == 2 and "n'est pas un ancêtre" in r.stdout      # B1 côté session : COMMIT sans le code
    assert _lancer(*arguments(_offre(tmp_path / "offre.json"), x["c1"])[:-1]).returncode == 2   # douze arguments : refus


# ------------------------------------------------------------------------------------------------------------ m2

def test_sans_aire_identifiants_de_taches_commencant_par_aire():
    """Correction m2 : les clés de `plis` (identifiants de tâches de 7b) ne sont jamais lues comme des clés d'aire ; une vraie
    clé d'aire, partout ailleurs, arrête toujours."""
    doc = {"plis": {"aire-1": 0, "aire_2": 1, "t3": 0, "t4": 1}, "sources": {"P-S50": {"e0": {"reglage": "lineaire-c15"}}},
           "graines_derivees": {"bbis/interne/e0": "1"}}
    ma._sans_aire(doc)                                                # cas sain : tâche nommée « aire-1 », pas d'arrêt
    for faute, motif in (({**doc, "aire_validation": 0.7}, "une aire serait écrite"),
                         ({**doc, "sources": {"P-S50": {"e0": {"aire": 0.71}}}}, "une aire serait écrite"),
                         ({**doc, "sources": {"plis": {"aire-1": 0}}}, "une aire serait écrite"),   # « plis » exempté au sommet seul
                         ({**doc, "plis": {"aire-1": 0.83}}, "pli 0 ou 1"), ({**doc, "plis": {"t1": True}}, "pli 0 ou 1")):
        with pytest.raises(GardeArret, match=motif):
            ma._sans_aire(faute)
