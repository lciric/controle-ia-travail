"""Épreuves (R5) du programme de la preuve après coup `scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py` (complément au
quatrième addendum d'écart de l'étape B bis de T0.7, § 6, « Programme de la preuve après coup » ; GO-2026-11-18-64). **Tout est
jouet** : dépôts git, registres, dossiers « de la course » et sorties imprimées fabriqués dans le dossier temporaire de l'essai.
Le programme n'est jamais joué sur le dépôt réel ; le seul fichier du dépôt lu est son code.

**Environnement fixé par les essais** : chaque essai retire toute variable `GIT_*` de son environnement et pose un dossier
personnel vide ; les commandes git qui fabriquent les dépôts jouets reçoivent un environnement écrit ici.

Le commit des sorties de la course est épinglé dans le programme (aucune option ne le change) : les essais vérifient la valeur
épinglée, puis la remplacent, dans le module chargé, par le commit « des sorties » du dépôt jouet.

- Cas sain : les trois points et les sorties conformes, pièce écrite et scellée, « relance permise sur preuve », code 0.
- Artefacts de (A1), de (A2), de (A3), des sorties gardées : pièce écrite, non conforme, « nœud » ou « lecture consommée », code 1.
- Fichiers gardés cités par une ligne de panne inscrite : tolérés à l'empreinte citée seulement.
- Garde des variables d'environnement de git ; R12 ; aucun module de `controle_ia` importé ; rien de décodé.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "preuve_aucune_ouverture_apres_coup_bbis_v1.py"
RUN_B, RUN_L = "20261018-090000-bbis-jouet", "20261119-090000-lecture-bbis-jouet"
PROPRE = "registres/t07-etape-b-bis-v1.md"
JOURNAL = PROPRE + ".ouvertures.md"
VOISIN = "registres/t07-etape-b-bis-v1-addenda-v1.md"
DOSSIER = "registres/t07-etape-b-bis/lecture-v1"
PIECE = DOSSIER + "/preuve-aucune-ouverture-apres-coup-bbis-{n}-v1.json"
SONDES = f"diag/{RUN_B}/sondes-bbis.json"
SCORES = f"donnees/{RUN_B}/sondes-bbis.npz"
SEUIL = "BBIS LECTURE ENTREES OUVERTES"


@pytest.fixture(autouse=True)
def environnement(monkeypatch, tmp_path_factory):
    for k in [k for k in os.environ if k.startswith("GIT_")]:
        monkeypatch.delenv(k, raising=False)
    maison = tmp_path_factory.mktemp("maison")
    monkeypatch.setenv("HOME", str(maison))
    monkeypatch.setenv("XDG_CONFIG_HOME", str(maison / "config"))


@pytest.fixture
def pc(monkeypatch):
    """Le programme, chargé comme module depuis son fichier (jamais lancé sur le dépôt réel)."""
    spec = importlib.util.spec_from_file_location("preuve_apres_coup_bbis_v1", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git(d: Path, *args) -> str:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
           "GIT_CONFIG_GLOBAL": os.devnull, "GIT_AUTHOR_NAME": "essai", "GIT_AUTHOR_EMAIL": "essai@example.invalid",
           "GIT_COMMITTER_NAME": "essai", "GIT_COMMITTER_EMAIL": "essai@example.invalid", "LC_ALL": "C"}
    r = subprocess.run(["git", "-c", "protocol.file.allow=always", "-C", str(d), *args], capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} : {r.stderr.strip()}")
    return r.stdout.strip()


def _commit(d: Path, message: str) -> str:
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "--allow-empty", "-m", message)
    return _git(d, "rev-parse", "HEAD")


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _poser(d: Path, rel: str, contenu, sceau: bool = True) -> str:
    octets = contenu if isinstance(contenu, bytes) else contenu.encode("utf-8")
    p = d / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(octets)
    if sceau:
        Path(str(p) + ".sha256").write_text(f"{_sha(octets)}  {p.name}\n", encoding="utf-8")
    return _sha(octets)


def _l(*colonnes) -> str:
    return "| " + " | ".join(colonnes) + " |\n"


@pytest.fixture
def h(tmp_path, pc, monkeypatch):
    """Arbre de lecture jouet : (1) commit « des sorties de la course » ; (2) registre propre, dont la ligne des scores ; (3) la
    sortie imprimée, gardée et scellée, d'un lancement arrêté avant le seuil."""
    d = tmp_path / "arbre"
    d.mkdir()
    _git(d, "init", "-q", "-b", "main")
    sha_sondes = _poser(d, SONDES, '{"jouet": "sondes, jamais décodé"}\n')
    _poser(d, f"diag/{RUN_B}/relecture-bbis.json", '{"jouet": "relecture"}\n')
    _poser(d, SCORES, bytes(range(256)) * 64)
    _poser(d, f"runs/{RUN_B}/manifeste.json", '{"jouet": "manifeste"}\n')
    c_sorties = _commit(d, "sorties de la course jouet")
    _poser(d, PROPRE, "# registre propre jouet\n\n" + _l("SCELLEMENT-BBIS", "2026-10-01T08:00:00Z", "prereg/texte.md", "a" * 64)
           + _l("SCORES-BBIS", "2026-10-04T12:00:00Z", SONDES, sha_sondes), sceau=False)
    _poser(d, VOISIN, "# registre voisin jouet\n\n| clé | heure (UTC) | chemin | sha256 | décision |\n|---|---|---|---|---|\n"
           + _l("ADDENDUM-ECART-4-BBIS", "2026-10-02T00:00:00Z", "prereg/addendum.md", "b" * 64, "jouet"), sceau=False)
    sortie = f"{DOSSIER}/sortie-lancement-1-jouet.txt"
    sha_sortie = _poser(d, sortie, "BBIS LECTURE ARRET : arbre de travail non propre (jouet)\n")
    _commit(d, "registres et sortie gardée du premier lancement")
    monkeypatch.setattr(pc, "COMMIT_SORTIES", c_sorties)
    return SimpleNamespace(d=d, c_sorties=c_sorties, sha_sondes=sha_sondes, sorties=[(sortie, sha_sortie)])


def jouer(pc, capsys, h, sorties="celles du dépôt jouet", numero="1", run_l=RUN_L, run_b=RUN_B):
    """Joue `main` sur l'arbre jouet ; rend le code de sortie, les lignes imprimées et la pièce (si elle est écrite)."""
    sorties = h.sorties if sorties == "celles du dépôt jouet" else sorties
    argv = ["--racine", str(h.d), "--run-lecture", run_l, "--run-bbis", run_b, "--numero", numero]
    for chemin, sha in sorties:
        argv += ["--sortie-lancement", chemin, sha]
    capsys.readouterr()
    code = pc.main(argv)
    lignes = capsys.readouterr().out.splitlines()
    piece = h.d / PIECE.format(n=numero)
    doc = None
    if piece.is_file() and code in (0, 1):
        sha = _sha(piece.read_bytes())
        assert Path(str(piece) + ".sha256").read_text(encoding="utf-8") == f"{sha}  {piece.name}\n"       # pièce scellée
        doc = json.loads(piece.read_text(encoding="utf-8"))
        assert lignes == [f"BBIS PREUVE APRES COUP ECRITE {PIECE.format(n=numero)} {sha} "
                          f"conforme={'oui' if doc['conforme'] else 'non'} classement={doc['classement']}"]
        assert code == (0 if doc["conforme"] else 1)
    return code, lignes, doc


def fichiers(d: Path) -> dict:
    return {str(p.relative_to(d)): _sha(p.read_bytes()) for p in sorted(d.rglob("*"))
            if p.is_file() and ".git" not in p.relative_to(d).parts}


def exiger_noeud(doc: dict, point: str, motif: str | None = None) -> None:
    """Un seul point (A1) à (A3) en défaut, sorties conformes : « nœud »."""
    assert doc["conforme"] is False and doc["classement"] == "nœud"
    assert [p for p in ("A1", "A2", "A3", "sorties") if not doc[p]["conforme"]] == [point], doc
    if motif is not None:
        assert motif in json.dumps(doc[point], ensure_ascii=False), doc[point]


# ------------------------------------------------------------------------------------------------------------- cas sain

def test_cas_sain_les_trois_points_et_les_sorties_conformes_piece_scellee(pc, capsys, h):
    avant = fichiers(h.d)
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 0 and doc["conforme"] is True and doc["classement"] == "relance permise sur preuve"
    assert all(doc[p]["conforme"] is True for p in ("A1", "A2", "A3", "sorties"))
    assert doc["A1"]["disque"] == {"etat": "absent du disque", "lignes_ouverture": 0}
    assert doc["A1"]["commits_portant_une_ligne_d_ouverture"] == []
    assert doc["A2"]["fautes"] == [] and doc["A2"]["fichiers_gardes_cites"] == [] and doc["A2"]["references_relevees"] >= 2
    assert doc["A3"]["commit_des_sorties"] == h.c_sorties and doc["A3"]["sha256_de_la_ligne_SCORES-BBIS"] == h.sha_sondes
    assert doc["A3"]["dossiers"] == {f"diag/{RUN_B}": {"fichiers_au_commit": 4, "fichiers_sur_le_disque": 4},
                                     f"donnees/{RUN_B}": {"fichiers_au_commit": 2, "fichiers_sur_le_disque": 2},
                                     f"runs/{RUN_B}": {"fichiers_au_commit": 2, "fichiers_sur_le_disque": 2}}
    assert doc["sorties"]["sorties"] == [{"chemin": h.sorties[0][0], "sha256_donnee": h.sorties[0][1], "etat": "conforme"}]
    assert doc["numero"] == 1 and doc["run_de_lecture"] == RUN_L and doc["run_de_la_course"] == RUN_B
    apres = fichiers(h.d)                                                           # rien d'autre n'est écrit ni corrigé
    assert {k: v for k, v in apres.items() if "preuve-aucune-ouverture-apres-coup" not in k} == avant
    assert len(apres) == len(avant) + 2


def test_cas_sain_journal_present_sans_ligne_d_ouverture(pc, capsys, h):
    _poser(h.d, JOURNAL, "# journal des ouvertures de B bis\n", sceau=False)
    _commit(h.d, "journal créé, à sa seule ligne d'en-tête")
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 0 and doc["A1"]["disque"]["etat"] == "présent" and doc["A1"]["disque"]["lignes"] == 1
    assert doc["A1"]["disque"]["sha256"] == _sha((h.d / JOURNAL).read_bytes()) and doc["A1"]["commits_de_l_histoire_du_journal"] == 1


def test_le_commit_des_sorties_est_epingle_et_aucune_option_ne_le_change(pc, capsys, h, monkeypatch):
    source = SCRIPT.read_text(encoding="utf-8")
    assert source.count('COMMIT_SORTIES = "7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9"') == 1
    assert source.count("COMMIT_SORTIES") == 2 and source.count("add_argument") == 2      # la définition, un seul usage
    assert "--commit" not in source
    monkeypatch.setattr(pc, "COMMIT_SORTIES", "7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9")  # valeur épinglée : absente du jouet
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 1
    exiger_noeud(doc, "A3", "absent du dépôt")
    assert "non_faisable" in doc["A3"]


# --------------------------------------------------------------------------------------------------- artefacts de (A1)

def test_A1_journal_portant_une_ligne_d_ouverture_sur_le_disque(pc, capsys, h):
    _poser(h.d, JOURNAL, _l("OUVERTURE-BBIS", "2026-10-05T00:00:00Z", "lecture B bis (x)", "e" * 64), sceau=False)
    code, _lignes, doc = jouer(pc, capsys, h)                                       # non suivi par git : vu sur le disque
    assert code == 1
    exiger_noeud(doc, "A1")
    assert doc["A1"]["disque"]["lignes_ouverture"] == 1 and doc["A1"]["commits_portant_une_ligne_d_ouverture"] == []


def test_A1_un_commit_de_l_histoire_du_journal_porte_une_ligne_puis_le_journal_est_vide(pc, capsys, h):
    _poser(h.d, JOURNAL, _l("OUVERTURE-BBIS", "2026-10-05T00:00:00Z", "lecture B bis (x)", "e" * 64), sceau=False)
    fautif = _commit(h.d, "journal portant une ligne")
    _poser(h.d, JOURNAL, "# journal\n", sceau=False)
    _commit(h.d, "journal vidé")
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 1
    exiger_noeud(doc, "A1")
    assert doc["A1"]["disque"]["lignes_ouverture"] == 0 and doc["A1"]["commits_portant_une_ligne_d_ouverture"] == [fautif]


def test_A1_journal_retire_apres_avoir_porte_une_ligne_et_sur_une_autre_branche(pc, capsys, h):
    _git(h.d, "checkout", "-q", "-b", "a-part")
    _poser(h.d, JOURNAL, _l("OUVERTURE-BBIS", "2026-10-05T00:00:00Z", "lecture B bis (x)", "e" * 64), sceau=False)
    fautif = _commit(h.d, "journal portant une ligne, sur une autre branche")
    _git(h.d, "checkout", "-q", "main")
    assert not (h.d / JOURNAL).exists()
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 1
    exiger_noeud(doc, "A1")
    assert doc["A1"]["commits_portant_une_ligne_d_ouverture"] == [fautif]


# --------------------------------------------------------------------------------------------------- artefacts de (A2)

@pytest.mark.parametrize("nom", [f"runs/{RUN_L}/manifeste.json", f"diag/{RUN_L}/autre.json", f"diag/{RUN_L}/lecture-bbis.json",
                                 "diag/20261119-080000-autre-run/lecture-bbis.json", "ailleurs/preuve-aucune-ouverture-bbis.json",
                                 "lecture-bbis.json"])
@pytest.mark.parametrize("ou", ["disque, non suivi", "tête", "autre branche"])
def test_A2_dossier_du_run_de_lecture_ou_fichier_de_lecture_present(pc, capsys, h, nom, ou):
    if ou == "autre branche":
        _git(h.d, "checkout", "-q", "-b", "a-part")
    _poser(h.d, nom, "{}\n", sceau=False)
    if ou != "disque, non suivi":
        _commit(h.d, "fichier d'un run de lecture")
    if ou == "autre branche":
        _git(h.d, "checkout", "-q", "main")
        assert not (h.d / nom).exists()
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 1
    exiger_noeud(doc, "A2", str(Path(nom).parent) if f"/{RUN_L}/" in nom else nom)
    lieux = {f["ou"] for f in doc["A2"]["fautes"]}
    assert lieux == {"disque, non suivi": {"disque"}, "tête": {"disque", "HEAD", "refs/heads/main"},
                     "autre branche": {"refs/heads/a-part"}}[ou]


def _panne(h, n: int, cites: dict, sha_declaration: str | None = None) -> None:
    """Déclaration de panne jouet, scellée, qui cite des fichiers gardés par chemin et empreinte, et sa ligne au registre voisin."""
    rel = f"{DOSSIER}/declaration-panne-mise-en-place-bbis-{n}-v1.md"
    sha = _poser(h.d, rel, "# déclaration jouet\n\n" + "".join(f"- `{c}` (`{s}`)\n" for c, s in cites.items()))
    with open(h.d / VOISIN, "a", encoding="utf-8") as f:
        f.write(_l(f"PANNE-MISE-EN-PLACE-BBIS-{n}", "2026-10-06T00:00:00Z", rel, sha_declaration or sha, "jouet"))


def test_A2_fichiers_gardes_cites_par_une_ligne_de_panne_inscrite_toleres_a_l_empreinte_citee(pc, capsys, h):
    ancien = "20261119-070000-lecture-bbis-jouet"
    gardes = {f"diag/{ancien}/lecture-bbis.json": _poser(h.d, f"diag/{ancien}/lecture-bbis.json", '{"issue": "I0"}\n'),
              f"diag/{ancien}/preuve-aucune-ouverture-bbis.json":
                  _poser(h.d, f"diag/{ancien}/preuve-aucune-ouverture-bbis.json", '{"conforme": true}\n')}
    _poser(h.d, f"runs/{ancien}/manifeste.json", "{}\n")
    _panne(h, 1, gardes)
    _commit(h.d, "fichiers gardés du premier refus, déclaration, ligne de panne")
    code, _lignes, doc = jouer(pc, capsys, h, run_l=ancien + "-relance1")
    assert code == 0 and doc["conforme"] is True and doc["A2"]["fautes"] == []
    assert {(t["nom"], t["sha256"]) for t in doc["A2"]["fichiers_gardes_cites"]} == set(gardes.items())
    assert doc["A2"]["lignes_de_panne"] == [{"cle": "PANNE-MISE-EN-PLACE-BBIS-1", "etat": "déclaration à l'empreinte de la ligne",
                                             "declaration": f"{DOSSIER}/declaration-panne-mise-en-place-bbis-1-v1.md"}]


@pytest.mark.parametrize("artefact", ["fichier gardé d'une autre empreinte", "fichier non cité", "déclaration d'une autre empreinte",
                                      "déclaration absente", "ligne non inscrite"])
def test_A2_fichier_garde_non_tolere(pc, capsys, h, artefact):
    ancien = "20261119-070000-lecture-bbis-jouet"
    nom = f"diag/{ancien}/lecture-bbis.json"
    sha = _poser(h.d, nom, '{"issue": "I0"}\n')
    if artefact == "fichier gardé d'une autre empreinte":
        _panne(h, 1, {nom: sha})
        _poser(h.d, nom, '{"issue": "autre"}\n')                                  # changé après la déclaration
    elif artefact == "fichier non cité":
        _panne(h, 1, {f"diag/{ancien}/preuve-aucune-ouverture-bbis.json": sha})   # la déclaration cite un autre chemin
    elif artefact == "déclaration d'une autre empreinte":
        _panne(h, 1, {nom: sha}, sha_declaration="d" * 64)
    elif artefact == "déclaration absente":
        _panne(h, 1, {nom: sha})
        (h.d / f"{DOSSIER}/declaration-panne-mise-en-place-bbis-1-v1.md").unlink()
    _commit(h.d, artefact)
    code, _lignes, doc = jouer(pc, capsys, h, run_l=ancien + "-relance1")
    assert code == 1
    exiger_noeud(doc, "A2", nom)
    assert doc["A2"]["fichiers_gardes_cites"] == []


# --------------------------------------------------------------------------------------------------- artefacts de (A3)

def _modifier(h, rel):
    (h.d / rel).write_bytes((h.d / rel).read_bytes() + b"\n")


A3 = {
    "fichier de scores modifié": (lambda h: _modifier(h, SCORES), SCORES, "octets autres que ceux du commit des sorties"),
    "compagnon d'un fichier de scores modifié": (lambda h: _modifier(h, SCORES + ".sha256"), SCORES + ".sha256",
                                                 "octets autres que ceux du commit des sorties"),
    "fichier des sondes modifié": (lambda h: _modifier(h, SONDES), SONDES, "empreinte autre que celle de la ligne SCORES-BBIS"),
    "manifeste de la course modifié": (lambda h: _modifier(h, f"runs/{RUN_B}/manifeste.json"), f"runs/{RUN_B}/manifeste.json",
                                       "octets autres que ceux du commit des sorties"),
    "fichier de plus, non suivi": (lambda h: _poser(h.d, f"donnees/{RUN_B}/copie.npz", b"x", sceau=False),
                                   f"donnees/{RUN_B}/copie.npz", "fichier de plus que le commit des sorties"),
    "fichier de plus, dans un sous-dossier": (lambda h: _poser(h.d, f"diag/{RUN_B}/notes/vu.txt", "x", sceau=False),
                                              f"diag/{RUN_B}/notes/vu.txt", "fichier de plus que le commit des sorties"),
    "fichier de moins": (lambda h: (h.d / f"diag/{RUN_B}/relecture-bbis.json").unlink(), f"diag/{RUN_B}/relecture-bbis.json",
                         "fichier de moins que le commit des sorties"),
    "fichier remplacé par un lien": (lambda h: ((h.d / SCORES).unlink(), (h.d / SCORES).symlink_to("/dev/null")), SCORES,
                                     "ni fichier ordinaire ni absent"),
}


@pytest.mark.parametrize("artefact", sorted(A3))
@pytest.mark.parametrize("suivi", ["non commité", "commité"])
def test_A3_fichier_de_la_course_change_ajoute_ou_retire(pc, capsys, h, artefact, suivi):
    geste, nom, motif = A3[artefact]
    geste(h)
    if suivi == "commité":
        _commit(h.d, artefact)                                                    # commité ou non : comparé au commit des sorties
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 1
    exiger_noeud(doc, "A3", motif)
    assert nom in {f["nom"] for f in doc["A3"]["fautes"]}


@pytest.mark.parametrize("artefact", ["ligne des scores absente", "ligne des scores en double", "ligne d'une autre empreinte",
                                      "ligne d'un autre chemin", "registre propre absent", "dépôt superficiel"])
def test_A3_ligne_des_scores_ou_depot_en_defaut(pc, capsys, h, artefact, tmp_path):
    texte = (h.d / PROPRE).read_text(encoding="utf-8")
    ligne = next(l for l in texte.splitlines(True) if l.startswith("| SCORES-BBIS"))
    attendu = None
    if artefact == "ligne des scores absente":
        (h.d / PROPRE).write_text(texte.replace(ligne, ""), encoding="utf-8")
    elif artefact == "ligne des scores en double":
        (h.d / PROPRE).write_text(texte + ligne, encoding="utf-8")
    elif artefact == "ligne d'une autre empreinte":
        (h.d / PROPRE).write_text(texte.replace(h.sha_sondes, "c" * 64), encoding="utf-8")
        attendu = "empreinte autre que celle de la ligne SCORES-BBIS"
    elif artefact == "ligne d'un autre chemin":
        (h.d / PROPRE).write_text(texte.replace(SONDES, f"diag/{RUN_B}/relecture-bbis.json"), encoding="utf-8")
    elif artefact == "registre propre absent":
        (h.d / PROPRE).unlink()
    _commit(h.d, artefact)
    if artefact == "dépôt superficiel":
        clone = tmp_path / "clone"
        _git(tmp_path, "clone", "-q", "--depth", "1", h.d.as_uri(), str(clone))
        h = SimpleNamespace(**{**vars(h), "d": clone})
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 1 and doc["conforme"] is False and doc["classement"] == "nœud" and doc["A3"]["conforme"] is False
    assert ("non_faisable" in doc["A3"]) == (attendu is None)
    if attendu:
        assert attendu in json.dumps(doc["A3"], ensure_ascii=False)
    if artefact == "dépôt superficiel":                                           # l'histoire incomplète rend les trois points non faisables
        assert all("dépôt superficiel" in doc[p]["non_faisable"] for p in ("A1", "A2", "A3"))


def test_A3_au_commit_des_sorties_le_fichier_des_sondes_n_a_pas_l_empreinte_de_la_ligne(pc, capsys, h, monkeypatch):
    _modifier(h, SONDES)
    autre = _commit(h.d, "un autre commit, où le fichier des sondes diffère")
    monkeypatch.setattr(pc, "COMMIT_SORTIES", autre)                              # disque = ce commit, mais ≠ ligne SCORES-BBIS
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 1
    exiger_noeud(doc, "A3", "au commit des sorties, empreinte autre que celle de la ligne SCORES-BBIS")


# ------------------------------------------------------------------------------------ artefacts des sorties gardées

@pytest.mark.parametrize("artefact", ["aucune sortie donnée", "sortie absente", "compagnon absent", "compagnon différent",
                                      "empreinte donnée autre", "empreinte mal formée", "la sortie porte la ligne du seuil",
                                      "une des deux sorties porte la ligne du seuil"])
def test_sorties_gardees_en_defaut_lecture_consommee(pc, capsys, h, artefact):
    chemin, sha = h.sorties[0]
    sorties = list(h.sorties)
    if artefact == "aucune sortie donnée":
        sorties = []
    elif artefact == "sortie absente":
        (h.d / chemin).unlink()
    elif artefact == "compagnon absent":
        (h.d / (chemin + ".sha256")).unlink()
    elif artefact == "compagnon différent":
        (h.d / (chemin + ".sha256")).write_text("f" * 64 + "  x\n", encoding="utf-8")
    elif artefact == "empreinte donnée autre":
        sorties = [(chemin, "0" * 64)]
    elif artefact == "empreinte mal formée":
        sorties = [(chemin, sha[:12])]
    elif artefact == "la sortie porte la ligne du seuil":
        sorties = [(chemin, _poser(h.d, chemin, SEUIL + "\nBBIS LECTURE ARRET : arrêt après ouverture (jouet)\n"))]
    else:
        autre = f"{DOSSIER}/sortie-lancement-2-jouet.txt"
        sorties.append((autre, _poser(h.d, autre, SEUIL + "\nBBIS LECTURE ARRET : arrêt après ouverture (jouet)\n")))
    _commit(h.d, artefact)
    code, _lignes, doc = jouer(pc, capsys, h, sorties=sorties)
    assert code == 1 and doc["conforme"] is False and doc["classement"] == "lecture consommée"
    assert all(doc[p]["conforme"] is True for p in ("A1", "A2", "A3")) and doc["sorties"]["conforme"] is False


def test_la_lecture_consommee_prime_sur_le_noeud(pc, capsys, h):
    chemin, _sha_sortie = h.sorties[0]
    _poser(h.d, JOURNAL, _l("OUVERTURE-BBIS", "2026-10-05T00:00:00Z", "lecture B bis (x)", "e" * 64), sceau=False)
    sorties = [(chemin, _poser(h.d, chemin, SEUIL + "\n"))]
    code, _lignes, doc = jouer(pc, capsys, h, sorties=sorties)
    assert code == 1 and doc["A1"]["conforme"] is False and doc["classement"] == "lecture consommée"


def test_deux_sorties_gardees_conformes(pc, capsys, h):
    autre = f"{DOSSIER}/sortie-lancement-2-jouet.txt"
    sorties = h.sorties + [(autre, _poser(h.d, autre, "BBIS LECTURE ARRET : variable(s) d'environnement de git (jouet)\n"))]
    _commit(h.d, "seconde sortie gardée")
    code, _lignes, doc = jouer(pc, capsys, h, sorties=sorties, numero="2")
    assert code == 0 and doc["numero"] == 2 and [x["etat"] for x in doc["sorties"]["sorties"]] == ["conforme", "conforme"]


# -------------------------------------------------------- garde des variables de git, R12, arrêts sans rien écrire

@pytest.fixture
def aucun_processus(monkeypatch):
    lances = []

    def interdit(*a, **k):
        lances.append(a)
        raise AssertionError(f"processus lancé : {a}")

    for nom in ("run", "Popen", "call", "check_call", "check_output"):
        monkeypatch.setattr(subprocess, nom, interdit)
    return lances


@pytest.mark.parametrize("variables", [("GIT_DIR",), ("GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0"), ("GIT_",)])
def test_garde_des_variables_de_git_artefact_refus_avant_toute_commande_git_sans_rien_ecrire(pc, capsys, h, monkeypatch,
                                                                                            aucun_processus, variables):
    secret = "/chemin/secret/a-ne-jamais-ecrire"
    for k in variables:
        monkeypatch.setenv(k, secret)
    avant, env = fichiers(h.d), dict(os.environ)
    code, lignes, doc = jouer(pc, capsys, h)
    assert code == 2 and doc is None and len(lignes) == 1 and lignes[0].startswith("BBIS PREUVE APRES COUP ARRET : ")
    assert all(k in lignes[0] for k in variables) and secret not in lignes[0]      # le nom, jamais la valeur
    assert aucun_processus == [] and fichiers(h.d) == avant and dict(os.environ) == env
    assert pc.main([]) == 2                                                        # avant la ligne de commande même


def test_garde_des_variables_de_git_cas_sain_un_autre_nom_ne_refuse_pas(pc, capsys, h, monkeypatch):
    for nom in ("GITHUB_TOKEN", "MON_GIT_DIR", "GIT"):
        monkeypatch.setenv(nom, "valeur-a-ne-pas-ecrire")
    code, _lignes, doc = jouer(pc, capsys, h)
    assert code == 0 and "valeur-a-ne-pas-ecrire" not in json.dumps(doc, ensure_ascii=False)


def test_R12_la_piece_n_est_jamais_ecrasee(pc, capsys, h, monkeypatch):
    code, _lignes, _doc = jouer(pc, capsys, h)
    assert code == 0
    avant = fichiers(h.d)
    for nom in ("run", "Popen"):
        monkeypatch.setattr(subprocess, nom, lambda *a, **k: (_ for _ in ()).throw(AssertionError("processus lancé")))
    capsys.readouterr()
    argv = ["--racine", str(h.d), "--run-lecture", RUN_L, "--run-bbis", RUN_B, "--numero", "1",
            "--sortie-lancement", *h.sorties[0]]
    assert pc.main(argv) == 2 and "existe déjà" in capsys.readouterr().out and fichiers(h.d) == avant


@pytest.mark.parametrize("argv", [{"--numero": "0"}, {"--numero": "un"}, {"--run-lecture": "lecture"},
                                  {"--run-bbis": "../ailleurs"}, {"--racine": "/dossier/absent/jouet"}])
def test_arguments_en_defaut_arret_sans_rien_ecrire_ni_lancer(pc, capsys, h, aucun_processus, argv):
    avant = fichiers(h.d)
    a = {"--racine": str(h.d), "--run-lecture": RUN_L, "--run-bbis": RUN_B, "--numero": "1", **argv}
    capsys.readouterr()
    assert pc.main([x for k, v in a.items() for x in (k, v)]) == 2
    assert capsys.readouterr().out.startswith("BBIS PREUVE APRES COUP ARRET : ")
    assert aucun_processus == [] and fichiers(h.d) == avant


def test_le_programme_n_importe_aucun_module_du_depot_et_ne_decode_aucun_resultat(pc):
    import ast
    source = SCRIPT.read_text(encoding="utf-8")
    importes = set()
    for n in ast.walk(ast.parse(source)):
        if isinstance(n, ast.Import):
            importes |= {a.name.split(".")[0] for a in n.names}
        elif isinstance(n, ast.ImportFrom):
            importes.add((n.module or "").split(".")[0])
    assert importes == {"__future__", "argparse", "hashlib", "json", "os", "re", "subprocess", "sys", "datetime", "pathlib"}
    assert "json.load" not in source and "numpy" not in source and "np.load" not in source     # `json` ne sert qu'à écrire
    # commandes git : en lecture seulement
    lues = {"rev-parse", "log", "show", "ls-tree", "for-each-ref", "cat-file"}
    appels = {n.args[1].value for n in ast.walk(ast.parse(source))
              if isinstance(n, ast.Call) and getattr(n.func, "id", None) in ("git", "texte_git") and len(n.args) > 1
              and isinstance(n.args[1], ast.Constant)}
    assert appels and appels <= lues
    assert '"cat-file", "blob"' in source and '"ls-tree", "-r"' in source
    assert pc.SEUIL == "BBIS LECTURE ENTREES OUVERTES" and pc.JOURNAL == "registres/t07-etape-b-bis-v1.md.ouvertures.md"
    assert pc.SORTIE == "registres/t07-etape-b-bis/lecture-v1/preuve-aucune-ouverture-apres-coup-bbis-{n}-v1.json"
