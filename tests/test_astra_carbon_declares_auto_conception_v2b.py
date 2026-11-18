"""Essais : le lanceur v2 de la course d'auto-conception (`d8fbb42a…`, **inchangé**) accepte la pièce de départ du gabarit v2b
(Astra et Carbon déclarés sur le mot du directeur, sonde d'Astra du jour, R-3274 pour Carbon) avec les commandes **réelles**
d'Astra et de Carbon extraites de `refs/remotes/origin/main` (empreintes du gabarit), et la refuse sans sonde, sans risque
accepté, ou avec un relais de course d'Astra qui n'est plus neuf. Monde, relais et orchestrateur simulés : ceux des essais du
lanceur v2 (`tests/test_lancer_course_auto_conception_v2.py`, importés tels quels). Aucun appel réel."""
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("essais_lanceur_auto_conception_v2_pour_v2b",
                                               RACINE / "tests" / "test_lancer_course_auto_conception_v2.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)
L = T.L
monde = T.monde  # noqa: F811 — fixture des essais du lanceur v2, réemployée telle quelle

GABARIT = RACINE / "docs/notes/organisme-auto-conception-v1/course-v2/piece-de-depart-gabarit-auto-conception-v2b.json"
COMMANDES_MAIN = {"astra": ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py",
                            "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"),
                  "carbon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",
                             "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75")}


def _de_main(rel, sha):
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == sha else None


OCTETS = {n: _de_main(*v) for n, v in COMMANDES_MAIN.items()}
pytestmark = pytest.mark.skipif(any(v is None for v in OCTETS.values()), reason="commandes absentes de origin/main")


def piece_remplie(**especes) -> dict:
    o = json.loads(GABARIT.read_text(encoding="utf-8"))
    o.update(statut="rempli pour l'essai", go_course="GO-2026-11-18-30", go_epreuve="GO-2026-11-18-31", variable_cle_claude=T.CLE,
             credit_declare_cle_claude_usd=300.0, ecrit_le="2026-11-18T11:00:00Z")
    o["especes_optionnelles"]["astra"]["sonde_du_jour"] = ("docs/notes/organisme-auto-conception-v1/course-v2/"
                                                          "sonde-astra-2026-11-18-v1.json (sha256 " + "a" * 64 + ", ok vrai)")
    for nom, modifs in especes.items():
        o["especes_optionnelles"][nom].update(modifs)
        for k in [k for k, v in modifs.items() if v is None]:
            del o["especes_optionnelles"][nom][k]
    return o


def preparer(m) -> None:
    cmds = {}
    for n, b in OCTETS.items():
        p = m["tmp"] / Path(COMMANDES_MAIN[n][0]).name
        p.write_bytes(b)
        cmds[n] = str(p)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", cmds["astra"], "--url-relais", "http://127.0.0.1:8790",
                                                      "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50"],
             "modele_propose": "gpt-6-astra", "nom_cle": "CLE_ESSAI_S", "pid_relais": T.PID_ASTRA,
             "url_etat_relais": "http://127.0.0.1:8790", "porte_plafond": {"type": "environnement"}}
    carbon = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", cmds["carbon"], "--url-base",
                                                       "http://127.0.0.1:8792/v1beta", "--modele", "gemini-4-carbon",
                                                       "--prix-entree", "8.3", "--prix-sortie", "41.5"],
              "modele_propose": "gemini-4-carbon", "nom_cle": "CLE_ESSAI_C", "pid_relais": T.PID_CARBON,
              "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}
    T._ecrire(m, L.DECLARATION_RELAIS, T.declaration(m["depot"], astra=astra, carbon=carbon))
    T._ecrire(m, L.RELEVE_CREDITS, dict(T.releve(CLE_ESSAI_S={"non_lisible": True, "motif": "illisible"},
                                                 CLE_ESSAI_C={"non_lisible": True, "motif": "illisible"}),
                                        dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S", "CLE_ESSAI_C"]}))
    c = m["cmdlines"]
    c[T.PID_ASTRA][c[T.PID_ASTRA].index("--modeles-permis") + 1] = "gpt-6-astra"
    c[T.PID_CARBON][c[T.PID_CARBON].index("--modele") + 1] = "gemini-4-carbon"
    c[T.PID_ARGON][c[T.PID_ARGON].index("--max-appels") + 1] = "280"   # commandes v2b : 231 au pire avec Astra et Carbon
    m["etat_argon"]["max_appels"] = 280


def test_relais_argon_sous_231_appels_refuse(monde, capsys):
    preparer(monde)
    T._ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    c = monde["cmdlines"][T.PID_ARGON]
    c[c.index("--max-appels") + 1] = "200"
    assert T.lancer(monde["r"]) == 2 and "231" in capsys.readouterr().err


def test_gabarit_brut_refuse_tant_qu_il_n_est_pas_rempli(monde):
    T.ecrire_scelle(monde["depot"] / L.PIECE_DE_DEPART, GABARIT.read_text(encoding="utf-8"))
    with pytest.raises(L.Refus, match="À REMPLIR"):
        L.verifier_piece_de_depart(monde["r"])


def test_gabarit_rempli_astra_et_carbon_declares_actifs(monde):
    preparer(monde)
    T._ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    depart = L.verifier_piece_de_depart(monde["r"])
    assert depart["especes_optionnelles"]["astra"]["declaree"] and depart["especes_optionnelles"]["carbon"]["declaree"]
    assert T.lancer(monde["r"]) == 0
    dep = json.loads((T.un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    actives = dep["especes_actives"]
    assert {"prop-astra", "prop-carbon", "prop-argon"} <= set(actives) and len(actives) == 5 and not any("kimi" in e for e in actives)
    vivants = dep["procedure_relais_persistants"]["relais_vivants"]
    assert vivants["astra"]["port"] == "8790" and vivants["carbon"]["port"] == "8792"


@pytest.mark.parametrize("espece,modifs", [
    ("astra", {"sonde_du_jour": None}), ("astra", {"sonde_du_jour": "  "}), ("astra", {"risque_accepte": False}),
    ("carbon", {"sonde_du_jour": None}), ("carbon", {"risque_accepte": None})])
def test_sans_sonde_ou_sans_risque_accepte_refuse(monde, espece, modifs):
    preparer(monde)
    T._ecrire(monde, L.PIECE_DE_DEPART, piece_remplie(**{espece: modifs}))
    with pytest.raises(L.Refus, match="sonde_du_jour"):
        L.verifier_piece_de_depart(monde["r"])
    assert T.lancer(monde["r"]) == 2


def test_espece_retiree_de_la_piece_mais_declaree_aux_relais_refusee(monde):
    preparer(monde)
    o = piece_remplie(astra={"declaree": False})
    T._ecrire(monde, L.PIECE_DE_DEPART, o)
    assert T.lancer(monde["r"]) == 2                    # déclaration des relais sans mot de la mère


def test_commande_d_une_autre_empreinte_refusee(monde):
    preparer(monde)
    o = piece_remplie()
    o2 = copy.deepcopy(o)
    o2["commandes_epinglees"]["astra"]["empreintes"] = ["b" * 64]
    T._ecrire(monde, L.PIECE_DE_DEPART, o2)
    assert T.lancer(monde["r"]) == 2


def test_relais_de_course_d_astra_non_neuf_refuse(monde, capsys):
    preparer(monde)
    T._ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    monde["etat_astra"]["appels"] = 1                   # la sonde faite sur le relais de la course : il n'est plus neuf
    assert T.lancer(monde["r"]) == 2
    assert "relais astra : relais neuf" in capsys.readouterr().err
    monde["etat_astra"]["appels"] = 0
    assert T.lancer(monde["r"]) == 0
