"""Essais (R5) de l'entrée de la lecture de T0.8 (`controle_ia.t08.lire_v1`), de l'entrée du passage à blanc
(`controle_ia.t08.passage_a_blanc_v1`) et du programme de la configuration réelle de la lecture
(`scripts/ecrire_configuration_lecture_t08_v1.py`). Données et registres factices."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat
from controle_ia.scellement import empreinte, sceller
from controle_ia.t08 import configuration_v1 as cf
from controle_ia.t08 import lire_v1, passage_a_blanc_v1

import test_t08_chaine_configuration_v1 as TC

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("lecture_t08", RACINE / "scripts" / "ecrire_configuration_lecture_t08_v1.py")
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)


def _sceller_json(p: Path, obj) -> str:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return sceller(p)


def _registre(p: Path, lignes):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("| CLÉ | date | chemin | empreinte |\n|---|---|---|---|\n"
                 + "".join(f"| {k} | {d} | {c} | {s} |\n" for k, d, c, s in lignes), encoding="utf-8")


# --- entrée de la lecture : n'appelle que executer_lecture, n'affiche que des chemins -------------------------------

NOMBRE_ISOLE = __import__("re").compile(r"(?<![0-9A-Za-z_./:-])[0-9]+(?:[.,][0-9]+)?(?![0-9A-Za-z_./:-])")


def sans_nombre_de_resultat(ligne: str) -> bool:
    """Une ligne imprimée ne porte aucun nombre isolé (hors chemins, empreintes et identifiants de run, où les chiffres
    font partie d'un mot) : critère de l'essai m-L1."""
    return NOMBRE_ISOLE.search(ligne) is None


def test_critere_sans_nombre_cas_sain_et_artefact():
    assert sans_nombre_de_resultat('{"lecture": "diag/20261128-120000-t08-lecture/lecture-t08.json", "lecture_sha256": "ab12"}')
    assert sans_nombre_de_resultat("PROGRES 2026-11-28T12:00:00Z etape=h bis")
    assert not sans_nombre_de_resultat('{"aire": 0.73}')                       # artefact : un nombre tiré des résultats
    assert not sans_nombre_de_resultat("table D : ligne D6, 12 alertes sur 64")


def test_lire_appelle_executer_lecture_et_n_affiche_aucun_resultat(tmp_path, monkeypatch, capsys):
    c = tmp_path / "config.json"
    _sceller_json(c, {"mode": "jouet", "entrees": {}})
    for nom in ("lecture-t08.json", "tables-d-f-t08.json"):
        _sceller_json(tmp_path / nom, {"resultat": {"audit_R4": {"declenche": False, "echantillon": None}, "aire": 0.73}})
    vus = {}

    def faux(config, racine, run_id, prereg=None, **k):
        vus.update(config=config, racine=racine, run_id=run_id, prereg=prereg, k=k)
        return {"manifeste": str(tmp_path / "manifeste.json"), "lecture": str(tmp_path / "lecture-t08.json"), "table_D": "D6",
                "tables_d_f": str(tmp_path / "tables-d-f-t08.json"), "duree_s": 1.0, "qualification": {"S25": "diffuse"}}

    import controle_ia.t08.lecture_v1 as lv
    monkeypatch.setattr(lv, "executer_lecture", faux)
    assert lire_v1._main(["--config", str(c), "--run-id", "20261128-120000-t08-lecture", "--prereg", "p.md"]) == 0
    sortie = capsys.readouterr()
    assert vus["run_id"] == "20261128-120000-t08-lecture" and vus["prereg"] == "p.md" and vus["k"] == {}
    assert vus["racine"] == Path(".") and vus["config"]["mode"] == "jouet"
    r = json.loads(sortie.out)
    assert sorted(r) == ["echantillon", "echantillon_sha256", "lecture", "lecture_sha256", "manifeste", "tables_d_f",
                         "tables_d_f_sha256"]
    assert r["echantillon"] is None                                             # audit non déclenché : aucun fichier
    assert "D6" not in sortie.out and "diffuse" not in sortie.out and "0.73" not in sortie.out
    assert all(sans_nombre_de_resultat(l) for l in (sortie.out + sortie.err).splitlines())


# --- échantillon de l'audit R4 (L-2) --------------------------------------------------------------------------------

class _LB:
    """Liste blanche minimale de l'essai : chemins et lecture du fichier des mesures (même interface que `ListeBlanche`)."""

    def __init__(self, racine, chemins):
        self.racine, self.entrees = racine, {n: {"chemin": c} for n, c in chemins.items()}

    def chemin(self, nom):
        return self.racine / self.entrees[nom]["chemin"]

    def lire_npz(self, nom):
        import numpy as np
        with np.load(self.chemin(nom), allow_pickle=False) as z:
            return {k: np.array(z[k]) for k in z.files}


def _monde_audit(tmp_path):
    import numpy as np
    cles = [f"S25__t00{i}__p0" for i in range(4)]
    (tmp_path / "textes.jsonl").write_text("".join(json.dumps({"cle": k, "texte": f"action {k} « é »"}, ensure_ascii=False)
                                                   + "\n" for k in cles), encoding="utf-8")
    np.savez(tmp_path / "mesures.npz", cle=np.array(cles), cout=np.array([10.0, float("nan"), 30.0, 40.0]))
    ch = {"textes_7b": "textes.jsonl", "mesures_7b": "mesures.npz"}
    for s, n in lire_v1.LECTURES.items():
        (tmp_path / f"{n}.jsonl").write_text("".join(json.dumps({"cle": k, "score": 50.0 + i, "texte_genere": f"{s} {i}"})
                                                     + "\n" for i, k in enumerate(cles)), encoding="utf-8")
        ch[n] = f"{n}.jsonl"
    res = {"audit_R4": {"declenche": True, "echantillon": {"S25": [
        {"cle": cles[1], "cout": None, "juges": {s: 51.0 for s in lire_v1.LECTURES}},
        {"cle": cles[3], "cout": 40.0, "juges": {"J8p": 53.0}}]}}}
    return _LB(tmp_path, ch), res, cles


def test_echantillon_cles_designees_seules_recopiees_a_l_octet(tmp_path):
    lb, res, cles = _monde_audit(tmp_path)
    e = lire_v1.extraire_echantillon(res, lb)
    assert [a["cle"] for a in e["actions"]] == [cles[1], cles[3]] and e["cles"] == 2
    a = e["actions"][0]
    brute = (tmp_path / "textes.jsonl").read_text(encoding="utf-8").splitlines()[1]
    assert a["ligne_texte"] == brute and a["cout_lu"] is None and a["condition"] == "S25"
    assert a["juges"]["J8r"]["ligne"] == (tmp_path / "lectures_J8_raisonnement.jsonl").read_text().splitlines()[1]
    assert e["actions"][1]["cout_lu"] == 40.0
    assert cles[0] not in json.dumps(e) and cles[2] not in json.dumps(e)


def test_echantillon_artefacts(tmp_path):
    lb, res, cles = _monde_audit(tmp_path)
    assert lire_v1.extraire_echantillon({"audit_R4": {"declenche": False, "echantillon": None}}, lb) is None
    with pytest.raises(GardeArret, match="hors de l'échantillon"):
        lire_v1.extraire_echantillon(res, lb, cles_demandees=[cles[0]])
    res["audit_R4"]["echantillon"]["S25"][1]["juges"]["J8p"] = 99.0
    with pytest.raises(GardeArret, match="≠ celui du résultat"):
        lire_v1.extraire_echantillon(res, lb)


def test_lire_refuse_une_configuration_non_scellee_ou_alteree(tmp_path):
    c = tmp_path / "config.json"
    c.write_text("{}\n")
    with pytest.raises(GardeArret):
        lire_v1._main(["--config", str(c), "--run-id", "20261128-120000-t08-lecture"])
    _sceller_json(tmp_path / "c2.json", {"mode": "jouet"})
    (tmp_path / "c2.json").write_text('{"mode": "reel"}\n')
    with pytest.raises(GardeArret):
        lire_v1._main(["--config", str(tmp_path / "c2.json"), "--run-id", "20261128-120000-t08-lecture"])


# --- passage à blanc sur un registre factice -------------------------------------------------------------------------

def _monde_passage(tmp_path, course_inscrite=False, sha_scel=None, jour="2026-11-20"):
    m = TC.marqueurs()
    texte = tmp_path / "texte.md"
    texte.write_text(TC.texte(m), encoding="utf-8")
    st = sceller(texte)
    c = tmp_path / "config.json"
    _sceller_json(c, {"mode": "reel", "marqueurs": m})
    lignes = [("SCELLEMENT-T08", f"{jour}T10:00:00Z", "prereg/T0.8.md", sha_scel or st),
              ("CODE-T08", f"{jour}T10:05:00Z", "registres/code-t08.md", m["COMMIT_CODE_T08"]),
              ("RUN-CONFIRMATION-T06", "2026-11-13T18:52:43Z", "runs/x/manifeste.json", m["RUN_7B"]["manifeste_sha256"]),
              ("CODE-MOTS-ET-COUT-T06", "2026-11-16T10:00:00Z", m["CODE_MOTS_ET_COUT_T06"]["fichier_inscription"],
               m["CODE_MOTS_ET_COUT_T06"]["sha256_inscription"])]
    if course_inscrite:
        lignes.append(("COURSE-T08", "2026-11-27T10:00:00Z", "diag/r/course-t08.json", "7" * 64))
    reg = tmp_path / "registre.md"
    _registre(reg, lignes)
    return ["--config", str(c), "--registre", str(reg), "--prereg", str(texte)]


def test_passage_a_blanc_cas_sain(tmp_path, capsys):
    assert passage_a_blanc_v1._main(_monde_passage(tmp_path)) == 0
    r = json.loads(capsys.readouterr().out)
    assert "SCELLEMENT-T08" in r and r["registre"]["lignes_lues"] == ["CODE-MOTS-ET-COUT-T06", "CODE-T08",
                                                                       "RUN-CONFIRMATION-T06", "SCELLEMENT-T08"]


@pytest.mark.parametrize("cas", ["course_deja_inscrite", "autre_texte", "scellement_posterieur"])
def test_passage_a_blanc_artefacts(tmp_path, cas):
    a = _monde_passage(tmp_path, course_inscrite=cas == "course_deja_inscrite",
                       sha_scel="5" * 64 if cas == "autre_texte" else None,
                       jour="2099-01-01" if cas == "scellement_posterieur" else "2026-11-20")
    with pytest.raises(GardeArret):
        passage_a_blanc_v1._main(a)


# --- configuration réelle de la lecture -----------------------------------------------------------------------------

def _monde_lecture(tmp_path, *, sha_course_registre=None, fichier_hors_run=False, sha_fichier="6" * 64):
    import subprocess

    r = tmp_path / "depot"
    r.mkdir()
    subprocess.run(["git", "-C", str(r), "init", "-q"], check=True)
    subprocess.run(["git", "-C", str(r), "-c", "user.email=e@invalid", "-c", "user.name=e", "commit", "-q",
                    "--allow-empty", "-m", "i"], check=True)
    m = TC.marqueurs()
    (r / "prereg").mkdir()
    (r / "prereg" / "texte.md").write_text(TC.texte(m), encoding="utf-8")
    sceller(r / "prereg" / "texte.md")
    _sceller_json(r / "prereg" / "config-course.json", {"mode": "reel", "marqueurs": m})
    run_c = "20261127-080000-t08-course"
    chemin_m, _ = creer_manifeste(r, run_c, {"mode": "jouet"}, ["t"], autoriser_depot_sale=True)
    fichiers = {}
    for k in L.FICHIERS_COURSE:
        d = f"donnees/{run_c if not (fichier_hors_run and k == 'mesures_etalonnage') else 'autre'}/{k}.jsonl"
        fichiers[k] = {"chemin": d, "sha256": sha_fichier if k == "mesures_etalonnage" else "6" * 64}
    ch = ecrire_resultat(r, chemin_m, "course-t08", {"fichiers": fichiers, "comptes": {"secret": 1}})
    base = r / "diag" / "20261116-000000-mots-et-cout" / "base-a-t08.json"
    sb = _sceller_json(base, {"x": 1})
    _registre(r / "registres" / "scellements-v1.md", [
        ("LECTURE-T08-BASE-A", "2026-11-16T21:01:43Z", str(base.relative_to(r)), sb),
        ("COURSE-T08", "2026-11-27T20:00:00Z", str(ch.relative_to(r)), sha_course_registre or empreinte(ch))])
    return r, run_c


def test_configuration_lecture_cas_sain(tmp_path, capsys):
    r, run_c = _monde_lecture(tmp_path)
    hd = tmp_path / "hd.json"
    hd.write_text(json.dumps({"index": "diag/hd/index.json", "mesures": "donnees/hd/mesures-hd.npz",
                              "textes": "donnees/hd/textes-actions-hd.jsonl", "manifeste": "runs/hd/manifeste.json"}))
    assert L.main(["--racine", str(r), "--texte", "prereg/texte.md", "--config-course", "prereg/config-course.json",
                   "--hd", str(hd), "--sortie", "prereg/T0.8-configuration-lecture-v1.json"]) == 0
    c = json.loads((r / "prereg" / "T0.8-configuration-lecture-v1.json").read_text(encoding="utf-8"))
    e = c["entrees"]
    from controle_ia.t08.lecture_v1 import ENTREES_LECTURE_REQUISES
    assert set(ENTREES_LECTURE_REQUISES) <= set(e)
    assert e["manifeste_course"]["chemin"] == f"runs/{run_c}/manifeste.json"
    assert e["lecture_cout_7b"] == {"chemin": "diag/20261111-151701-t06-reel/lecture-cout-t06.json", "sha256": "e" * 64,
                                    "phase": "lecture"}
    assert e["registre_vadapt"]["phase"] == "hd" and e["index_hd"]["sha256"] is None
    assert all(e[n]["sha256"] for n in e if e[n].get("scelle", True) and e[n]["phase"] != "hd")
    for k, v in cf.VALEURS_GELEES_LECTURE.items():
        assert c[k] == v
    assert "secret" not in json.dumps(c)                       # rien des comptes de la course n'est recopié


@pytest.mark.parametrize("cas", ["empreinte_course", "fichier_hors_run", "sortie_existante", "fichier_sans_empreinte",
                                 "empreinte_courte"])
def test_configuration_lecture_artefacts(tmp_path, capsys, cas):
    r, _ = _monde_lecture(tmp_path, sha_course_registre="0" * 64 if cas == "empreinte_course" else None,
                          fichier_hors_run=cas == "fichier_hors_run",
                          sha_fichier={"fichier_sans_empreinte": None, "empreinte_courte": "6" * 12}.get(cas, "6" * 64))
    s = r / "prereg" / "lecture.json"
    if cas == "sortie_existante":
        s.write_text("{}\n")
    assert L.main(["--racine", str(r), "--texte", "prereg/texte.md", "--config-course", "prereg/config-course.json",
                   "--sortie", "prereg/lecture.json"]) == 1
    assert "ARRÊT" in capsys.readouterr().err


def test_fichier_recompose_entre_a_l_empreinte_de_course_t08_seulement(tmp_path):
    """r-9 (GO-2026-11-22-134) : un fichier recomposé de ses morceaux entre à son chemin d'origine s'il est égal à l'octet
    à la sortie scellée (empreinte de `course-t08.json`) ; recomposé autrement, même avec un compagnon refait, il n'entre
    pas ; sans empreinte consignée, la configuration n'est pas écrite (essai des artefacts ci-dessus)."""
    from controle_ia.t08 import entrees_v1 as en

    r = tmp_path
    (r / "donnees" / "run").mkdir(parents=True)
    vrai = b"x" * 1000 + b"y" * 1000
    p = r / "donnees" / "run" / "lectures-J8-raisonnement-t08.jsonl"
    p.write_bytes(vrai)
    sha = sceller(p)
    lb = en.ListeBlanche(r, {"lectures_J8_raisonnement": {"chemin": "donnees/run/lectures-J8-raisonnement-t08.jsonl",
                                                          "sha256": sha, "phase": "lecture"}})
    lb.ouvrir_phase("lecture")
    morceaux = [vrai[:900], vrai[900:1500], vrai[1500:]]           # découpe et recomposition à l'octet
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    p.write_bytes(b"".join(morceaux))
    sceller(p)
    assert lb.controler("lectures_J8_raisonnement")[1]["etat"] == "conforme"
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    p.write_bytes(b"".join([morceaux[1], morceaux[0], morceaux[2]]))   # morceaux dans le désordre, compagnon refait
    sceller(p)
    assert lb.controler("lectures_J8_raisonnement")[1]["etat"] == "differe_de_la_consignee"
