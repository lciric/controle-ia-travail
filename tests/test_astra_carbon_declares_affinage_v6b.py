"""Essais : le lanceur v6 de la course d'affinage (`bf2abdc6…`, **inchangé**) accepte la déclaration du gabarit v6b (Astra et
Carbon déclarés, Kimi non déclaré, limite de débit non comptée comme soupçon — R-3279) avec les commandes **réelles**
extraites de `refs/remotes/origin/main`, et le rapport au format v2 écrit par la **sonde commune**
(`scripts/sonde_astra_courses_v1.py`) devant le relais factice (code du relais épinglé) ; il refuse la sonde échouée, la sonde
faite sur le relais de la course et un relais de course d'Astra non neuf. Monde simulé : celui des essais du lanceur v6,
importé tel quel. Aucun appel réel."""
import datetime as dt
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]


def _charger(nom, rel):
    spec = importlib.util.spec_from_file_location(nom, RACINE / rel)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


T = _charger("essais_lanceur_affinage_v6_pour_v6b", "tests/test_lancer_course_affinage_mentors_v6.py")
TS = _charger("essais_sonde_astra_courses_v1_pour_v6b", "tests/test_sonde_astra_courses_v1.py")
L = T.L
monde = T.monde  # noqa: F811 — fixture des essais du lanceur v6, réemployée telle quelle

GABARIT = RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v6/declaration-relais-gabarit-course-affinage-v6b.json"
COMMANDES_MAIN = {"astra": ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py",
                            "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"),
                  "carbon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",
                             "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75")}


def _de_main(rel, sha):
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == sha else None


OCTETS = {n: _de_main(*v) for n, v in COMMANDES_MAIN.items()}
pytestmark = pytest.mark.skipif(any(v is None for v in OCTETS.values()), reason="commandes absentes de origin/main")


def declaration_remplie(m) -> dict:
    o = json.loads(GABARIT.read_text(encoding="utf-8"))
    del o["gabarit"]
    o["redige_utc"] = "2026-11-18T11:00:00Z"
    f = o["fournisseurs"]
    for n in ("astra", "carbon"):
        p = m["tmp"] / Path(COMMANDES_MAIN[n][0]).name
        p.write_bytes(OCTETS[n])
        f[n]["commande"][0], f[n]["commande"][3] = sys.executable, str(p)
        assert f[n]["commande"][4:] == L.ARGUMENTS_COMMANDES[n]          # arguments du gabarit = arguments épinglés
    ref = T.declaration(m["depot"])["fournisseurs"]                       # chemins et adresses du monde d'essai
    f["claude"].update(porte_plafond=ref["claude"]["porte_plafond"], url_relais=ref["claude"]["url_relais"], pid_relais=T.PID_CLAUDE)
    f["argon"].update(commande=ref["argon"]["commande"], nom_cle="CLE_ESSAI_A", pid_relais=T.PID_ARGON)
    f["carbon"].update(nom_cle="CLE_ESSAI_G", pid_relais=T.PID_CARBON)
    f["astra"].update(nom_cle="CLE_ESSAI_S", pid_relais=T.PID_ASTRA)
    return o


def sonde_commune_v2(m, reserve=0.01) -> int:
    """Joue la sonde commune devant le relais factice ; son rapport v2 est écrit au chemin que lit le lanceur v6."""
    p_cmd = m["tmp"] / "sonde" / "commande_astra_v1.py"
    p_cmd.parent.mkdir(exist_ok=True)
    p_cmd.write_bytes(OCTETS["astra"])
    relais_copie = m["tmp"] / "sonde" / "relais_kimi_v4.py"
    relais_copie.write_bytes(TS.CHEMIN_RELAIS.read_bytes())
    amont = TS.FauxAmont()
    relais = TS.RelaisFactice(amont, reserve=reserve)
    try:
        sortie_v2 = m["depot"] / L.SONDE_ASTRA
        sortie_v2.unlink(missing_ok=True)
        Path(str(sortie_v2) + ".sha256").unlink(missing_ok=True)
        code = TS.S.sonder(p_cmd, relais.url, os.getpid(), m["tmp"] / "sonde" / "sonde-commune.json", sortie_v2,
                           lire_cmd=lambda pid: [sys.executable, str(relais_copie), "--port", str(relais.port)], amont=amont.url)
    finally:
        relais.fermer()
    if sortie_v2.is_file():
        jour = json.loads(sortie_v2.read_text())["horodatage_utc"][:10]
        m["r"].aujourd_hui = dt.date.fromisoformat(jour)          # la sonde v2 date par `date -u` : le jour de l'essai
    return code


def _ecrire_tout(m, decl):
    T._decl(m, decl)
    T._releve(m, dict(T.releve(CLE_ESSAI_G={"non_lisible": True, "motif": "illisible"},
                               CLE_ESSAI_S={"non_lisible": True, "motif": "illisible"}),
                      dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A", "CLE_ESSAI_G", "CLE_ESSAI_S"]}))


def test_declaration_v6b_verifiee_astra_et_carbon_actifs_kimi_absent(monde):
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    d = L.verifier_declaration(declaration_remplie(monde), fixe, monde["r"])
    actives = [e["etiquette"] for e in d["especes_actives"]]
    assert len(actives) == 5 and {"prop-astra", "prop-carbon", "prop-argon"} <= set(actives)
    assert not any("kimi" in e for e in actives) and d["carbon"]["active"] is True
    assert d["compter_limite_de_debit_comme_soupcon"] is False and d["kimi_autorise_par_la_mere"] is None


def test_bout_en_bout_avec_la_sonde_commune(monde):
    assert sonde_commune_v2(monde) == 0
    _ecrire_tout(monde, declaration_remplie(monde))
    assert T.lancer(monde["r"]) == 0
    run = T.un_run(monde["r"])
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    texte = json.dumps(dep, ensure_ascii=False)
    assert "prop-astra" in texte and "prop-carbon" in texte and "prop-kimi" not in json.dumps(dep.get("especes_actives"))
    assert dep["sonde_astra"]["cout_usd"] <= 0.05


def test_sonde_commune_echouee_astra_refusee(monde, capsys):
    assert sonde_commune_v2(monde, reserve=0.40) == 1         # échec de configuration : aucun rapport v2 écrit
    _ecrire_tout(monde, declaration_remplie(monde))
    assert T.lancer(monde["r"]) == 2                           # Astra déclarée sans sonde réussie : refus
    assert "sonde d'Astra" in capsys.readouterr().err


def test_sonde_sur_le_relais_de_la_course_refusee(monde, capsys):
    assert sonde_commune_v2(monde) == 0
    decl = declaration_remplie(monde)
    v2 = json.loads((monde["depot"] / L.SONDE_ASTRA).read_text())
    decl["fournisseurs"]["astra"]["pid_relais"] = v2["relais_pid"]   # le relais de la course serait celui de la sonde
    monde["cmdlines"][v2["relais_pid"]] = monde["cmdlines"][T.PID_ASTRA]
    _ecrire_tout(monde, decl)
    assert T.lancer(monde["r"]) == 2
    assert "relais de la course" in capsys.readouterr().err


def test_relais_de_course_d_astra_non_neuf_refuse(monde, capsys):
    assert sonde_commune_v2(monde) == 0
    _ecrire_tout(monde, declaration_remplie(monde))
    monde["etats"]["8790"]["appels"] = 1
    assert T.lancer(monde["r"]) == 2
    err = capsys.readouterr().err
    assert "astra" in err and "neuf" in err, err
    monde["etats"]["8790"]["appels"] = 0
    assert T.lancer(monde["r"]) == 0
