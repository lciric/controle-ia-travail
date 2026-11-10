"""Gardes de la lecture complémentaire de P3-bis (`premier_test_ia.lecture_p3bis_v1`, inchangée) et chaîne fermée en mode
décisif (`premier_test_ia.ouverture_p3bis_v2 lectures-fermees`) : essais neufs de la contre-lecture du code v1 (`7a074ad1…`),
CP-09 ; texte de P3-bis, brouillon 9 (`eb65773f…`), plan, points 3, 4 et 6.
- Cas sain en mode décisif (texte scellé factice qui cite le commit du code, la configuration et l'entropie ; run source
  décisif lancé sous ce texte ; lecture de P3 décisive) et ses artefacts : entropie absente ou autre, lecture de P3 non
  décisive, arbre gelé modifié depuis le commit cité ; aucune garde ne laisse de run.
- Gardes sans cas d'artefact dans les essais de la v1 : `max_nouveaux` illisible au manifeste du run source, sondes
  principales de la lecture de P3 autres que celles des sondes figées, deux lignes d'audit pour un même jeu, état sans aire.
- Bout en bout décisif de la chaîne fermée, dans un clone qui porte le code (garde d'import réelle) : dépliage, lecture de
  P3 et lecture complémentaire décisives dans des processus à part, mise en paquet ; codes 0 ; manifestes décisifs dans le
  paquet ; durées écrites (CP-05)."""
import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import config_canonique
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.premier_test_ia import lecture_p3bis_v1 as lb
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob
from controle_ia.prereg import SECTIONS
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("essai_fermeture_p3bis_v2", RACINE / "scripts" / "essai_fermeture_p3bis_v2.py")
ev2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev2)

RUN = "20261120-120000-p3bis-reel"
LECTURE, LC = "20261120-130000-p3bis-lecture", "20261120-130100-p3bis-lecture-complementaire"
ENTROPIE = 4242
PREREG = "prereg/P3-bis-temoin-positif-v1.md"
CONFIG = {"mode": "reel", "max_nouveaux": 64}


def _git(d, *args):
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True).stdout.strip()


def _prereg(depot: Path, commit: str, config: dict, nom: str = PREREG, entropie: int = ENTROPIE) -> Path:
    """Texte scellé factice, conforme à R1 et R2 dans sa forme, qui cite le commit du code, la configuration et l'entropie."""
    p = depot / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    corps = ["# P3-bis factice (essai de bout en bout décisif)", "", f"- Commit du code d'analyse : `{commit}`",
             f"- Configuration de P3 (empreinte canonique) : `{hashlib.sha256(config_canonique(config)).hexdigest()}`",
             f"- Entropie : `{entropie}`", ""]
    for s in SECTIONS[:-1]:
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def _monter_decisif(depot: Path, issue: str = "vu", committer_le_run: bool = True) -> str:
    """Commit du code (cité), texte scellé, run source décisif lancé sous ce texte, chacun committé (arbre propre) ; sans
    `committer_le_run`, le run reste à fermer en second paquet avant tout commit (chemin de l'instance)."""
    gi = depot / ".gitignore"
    gi.write_text((gi.read_text(encoding="utf-8") if gi.exists() else "") + "donnees/\n__pycache__/\n", encoding="utf-8")
    committer(depot)
    commit = _git(depot, "rev-parse", "HEAD")
    p = _prereg(depot, commit, CONFIG)
    committer(depot)
    ev2.fabriquer_run(depot, RUN, issue, ev2.graine(issue), config=CONFIG, decisif=True, prereg=str(p), entropie=ENTROPIE)
    if committer_le_run:
        committer(depot)
    return commit


@pytest.fixture
def decisif(depot, monkeypatch):
    """Dépôt jetable en mode décisif ; la garde d'import est remplacée en processus (le code est celui du vrai dépôt :
    elle est jouée réelle par le bout en bout de la chaîne fermée, plus bas)."""
    appels = []
    monkeypatch.setattr(lp, "exiger_code_importe_sous", appels.append)
    commit = _monter_decisif(depot)
    lp.analyser(depot, RUN, LECTURE, PREREG, entropie=ENTROPIE)
    committer(depot)
    return {"d": depot, "commit": commit, "appels": appels}


def test_lecture_complementaire_cas_sain_en_mode_decisif(decisif):
    d = decisif["d"]
    s = lb.analyser(d, RUN, LECTURE, LC, PREREG, entropie=ENTROPIE)
    assert s["lien_au_preenregistrement"] == {"commit_cite": decisif["commit"], "entropie": ENTROPIE}
    assert s["issue_mecanique"] == {"issue": "vu", "ligne": 4} and decisif["appels"]                 # garde d'import jouée
    m = json.loads((d / "runs" / LC / "manifeste.json").read_text(encoding="utf-8"))
    assert m["decisif"] is True and m["preenregistrement"]["chemin"] == PREREG and m["depot_propre"] is True
    assert m["preenregistrement"]["sha256"] == (d / (PREREG + ".sha256")).read_text(encoding="utf-8").split()[0]


def test_lecture_complementaire_decisive_artefacts_aucun_run(decisif):
    d = decisif["d"]
    for entropie in (None, ENTROPIE + 1):
        with pytest.raises(GardeArret, match="R9"):
            lb.analyser(d, RUN, LECTURE, "20261120-130200-x", PREREG, entropie=entropie)
    lp.analyser(d, RUN, "20261120-130300-p3-non-decisive", None, entropie=ENTROPIE)                # lecture de P3 non décisive
    committer(d)
    with pytest.raises(GardeArret, match="non décisive"):
        lb.analyser(d, RUN, "20261120-130300-p3-non-decisive", "20261120-130301-x", PREREG, entropie=ENTROPIE)
    (d / "src").mkdir()
    (d / "src" / "modifie.py").write_text("x = 1\n", encoding="utf-8")                           # arbre gelé modifié
    committer(d)
    with pytest.raises(GardeArret, match="arbre gelé"):
        lb.analyser(d, RUN, LECTURE, "20261120-130302-x", PREREG, entropie=ENTROPIE)
    for r in ("20261120-130200-x", "20261120-130301-x", "20261120-130302-x"):
        assert not (d / "runs" / r).exists()                                                     # une garde ne laisse aucun run


def test_max_nouveaux_illisible_au_manifeste_du_run_source(depot):
    (depot / ".gitignore").write_text("donnees/\n", encoding="utf-8")
    committer(depot)
    for k, (config, ok) in enumerate((({"mode": "jouet", "max_nouveaux": 64}, True), ({"mode": "jouet"}, False),
                                      ({"mode": "jouet", "max_nouveaux": True}, False),
                                      ({"mode": "jouet", "max_nouveaux": 0}, False),
                                      ({"mode": "jouet", "max_nouveaux": "64"}, False))):
        run, lecture = f"20261120-12000{k}-jouet", f"20261120-13000{k}-lecture"
        ev2.fabriquer_run(depot, run, "vu", ev2.graine("vu"), config=config)
        lp.analyser(depot, run, lecture, None, entropie=ENTROPIE, autoriser_depot_sale=True)
        if ok:
            assert lb.analyser(depot, run, lecture, f"20261120-14000{k}-lc", None, entropie=ENTROPIE,
                               autoriser_depot_sale=True)["longueurs_PB-2"]["max_nouveaux"] == 64
        else:
            with pytest.raises(GardeArret, match="max_nouveaux"):
                lb.analyser(depot, run, lecture, f"20261120-14000{k}-lc", None, entropie=ENTROPIE, autoriser_depot_sale=True)
            assert not (depot / "runs" / f"20261120-14000{k}-lc").exists()


def test_sondes_principales_de_la_lecture_de_p3_autres_que_celles_des_sondes_figees(depot):
    (depot / ".gitignore").write_text("donnees/\n", encoding="utf-8")
    committer(depot)
    run, lecture = "20261120-120000-jouet", "20261120-130000-lecture"
    ev2.fabriquer_run(depot, run, "vu", ev2.graine("vu"))
    lp.analyser(depot, run, lecture, None, entropie=ENTROPIE, autoriser_depot_sale=True)
    source = lp.charger_source(depot, run)
    l3 = lb.exiger_lecture_de_p3(depot, lecture, run, None)
    textes = lb.charger_textes(depot, source)
    assert lb.preparer(source, l3, textes, 64)["sonde_p"] == lb.SONDE_P_ATTENDUE                  # cas sain
    autre = copy.deepcopy(l3)
    autre["principales"] = list(reversed(l3["principales"]))
    with pytest.raises(GardeArret, match="sondes principales"):
        lb.preparer(source, autre, textes, 64)


P = lb.SONDE_P_ATTENDUE


def _ligne_audit(jeu, separation=0.8):
    return {"sonde": P, "jeu": jeu, "aire": separation, "separation": separation, "triviaux": {}, "cout_seul": {}}


def test_deux_lignes_d_audit_pour_un_meme_jeu():
    l3 = {"audit_R4": {"jeux": [_ligne_audit("saboteur-temoin"), _ligne_audit("saboteur-honnete")]}}
    assert lb._ligne_audit(l3, P, "saboteur-temoin")["jeu"] == "saboteur-temoin"                 # cas sain : une ligne
    assert lb._ligne_audit(l3, P, "mention-honnete") is None
    l3["audit_R4"]["jeux"].append(_ligne_audit("saboteur-temoin", 0.7))
    with pytest.raises(GardeArret, match="2 lignes d'audit"):
        lb._ligne_audit(l3, P, "saboteur-temoin")


def test_etat_sans_aire():
    import numpy as np
    c = np.array(["saboteur"] * 4 + ["temoin"] * 4)
    m = np.array([1, 0, 1, 0, 1, 0, 1, 0])
    l3 = {"etats_des_jeux": {P: {"saboteur-temoin": lp.AU_DESSUS}}, "jeux": {P: {"saboteur-temoin": {"aire": 0.8}}},
          "audit_R4": {"jeux": []}}
    assert lb.etat_decisif(l3, P, m, c)["E_prime"] == lp.AU_DESSUS                               # cas sain
    l3["jeux"][P]["saboteur-temoin"] = {"echec": "jeu en échec"}                                 # « au-dessus » sans aire
    with pytest.raises(GardeArret, match="sans aire"):
        lb.etat_decisif(l3, P, m, c)
    l3["etats_des_jeux"][P]["saboteur-temoin"] = lp.ECHEC                                        # « échec » : sans aire admis
    assert lb.etat_decisif(l3, P, m, c)["E_prime"] == lp.ECHEC


# ================================================================================================= chaîne fermée décisive
def test_chaine_fermee_de_bout_en_bout_en_mode_decisif(tmp_path, monkeypatch):
    """Clone qui porte une copie du code (`src/controle_ia`), commit cité par un texte scellé factice, run source décisif
    lancé sous ce texte, second paquet ; `lectures_fermees` joue les deux lectures décisives dans des processus à part,
    avec la vraie garde d'import (le code importé est celui du clone)."""
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))
    depot = ev2.depot_vide(tmp_path / "instance")
    shutil.copytree(RACINE / "src" / "controle_ia", depot / "src" / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    commit = _monter_decisif(depot, committer_le_run=False)
    ob.fermer_run(depot, RUN)
    _git(depot, "add", "-A")
    _git(depot, "commit", "-qm", "run et second paquet")
    ob.exiger_aucun_clair(depot, RUN)
    clone = tmp_path / "clone-ferme"
    subprocess.run(["git", "clone", "-q", str(depot), str(clone)], check=True, capture_output=True)
    monkeypatch.setenv("PYTHONPATH", str(clone / "src"))                                         # code importé du clone
    monkeypatch.setenv("PYTHONDONTWRITEBYTECODE", "1")
    sortie = []
    code = ob.lectures_fermees(clone, RUN, LECTURE, LC, prereg=PREREG, entropie=ENTROPIE, imprimer=sortie.append)
    assert code == 0, sortie
    assert sortie[:4] == ["code dépliage du second paquet : 0", "code lecture de P3 : 0", "code lecture complémentaire : 0",
                          "code mise en paquet : 0"] and len(sortie) == 5
    _, archive = ob.relire_paquet_lectures((clone / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES).read_bytes(), ENTROPIE)
    f = dict(ob.membres_de(archive))
    for lecture in (LECTURE, LC):
        m = json.loads(f[f"runs/{lecture}/manifeste.json"])
        assert m["decisif"] is True and m["preenregistrement"]["chemin"] == PREREG and m["depot_propre"] is True
    l3bis = json.loads(f[f"diag/{LC}/lecture-p3bis.json"])["resultat"]
    assert l3bis["lien_au_preenregistrement"] == {"commit_cite": commit, "entropie": ENTROPIE}
    assert l3bis["issue_mecanique"] == {"issue": "vu", "ligne": 4}
    assert f[f"{ob.ESPACE_DEFAUT}/lecture-p3bis.sortie"] == b"" and f[f"{ob.ESPACE_DEFAUT}/lecture-p3bis.erreurs"] == b""
    assert set(json.loads(f[f"{ob.ESPACE_DEFAUT}/{ob.DUREES}"])["durees"]) >= {"lecture-p3_s", "lecture-p3bis_s"}
    statut = _git(clone, "status", "--porcelain", "--untracked-files=all", "--ignored")
    assert sorted(x[3:] for x in statut.splitlines()) == sorted([f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}",
                                                                 f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}.sha256"])
