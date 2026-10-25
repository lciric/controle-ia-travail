"""Essais complémentaires de la reprise par segments du noyau `8e5e2f7b` — v1 (conv-audit, 25 octobre 2026 ; contre-lecture 3
du pilote 4, constat P4C3-03) : trois refus de `reprendre()` lus dans le code et non essayés sur un artefact par
`tests/test_reprise_segments.py`, chacun ici sur un cas sain (reprise acceptée) et sur un artefact (refus, rien d'écrit) :

- le dernier événement de la course n'est pas l'arrêt sur `STOP` de l'état (`boucle.py` l. 1037–1039) ;
- la ronde de génération en cours est incohérente avec l'état (l. 1063–1064) ;
- la vue figée de la ronde en cours est introuvable dans l'espace de la course, en mémoire partagée (l. 1065–1068 ; sans
  objet pour le pilote 4, qui ne partage pas la mémoire).

Hors de la suite du noyau : ses 169 essais, que le lanceur du pilote 4 compte, ne changent pas. Réutilise les aides de
`tests/test_reprise_segments.py` (organismes d'essai du noyau, espèces simulées, aucun réseau).

Usage, depuis la racine `essaim-m3-refonte-v1` d'une copie du noyau `8e5e2f7b` :
  ESSAIM_M3_RACINE="$PWD" python -B -m pytest -q -p no:cacheprovider CHEMIN/test_reprise_refus_complementaires_v1.py
"""
import json
import os
import pathlib
import sys

import pytest

RACINE = pathlib.Path(os.environ.get("ESSAIM_M3_RACINE", ".")).resolve()
sys.path.insert(0, str(RACINE))
sys.path.insert(0, str(RACINE / "tests"))

import test_reprise_segments as t  # noqa: E402
from essaim_m3.noyau import boucle  # noqa: E402

assert boucle.ETAT_REPRISE_VERSION == 1, "noyau inattendu : ces essais visent le format d'état v1 (noyau 8e5e2f7b)"


def _arretee_en_ronde_de_generation(racine, memoire_partagee=False):
    """Deux lignées, aucune ronde de conception : `STOP` posé après la première lignée de la ronde de génération 1, donc
    entre deux unités d'une même ronde ; l'état garde la ronde en cours (phase génération, ordre tiré, une lignée faite)."""
    n = t._noyau(racine, t.DEUX, generations=2, rondes=0, memoire_partagee=memoire_partagee)
    n.amorcer()
    origine = n.executer_generation

    def unite(lignee, conception=None):
        r = origine(lignee, conception=conception)
        (pathlib.Path(racine) / "STOP").write_text("stop", encoding="utf-8")
        return r
    n.executer_generation = unite
    n.boucler()
    (pathlib.Path(racine) / "STOP").unlink()
    etat = json.loads(t._etats(racine)[-1].read_text(encoding="utf-8"))
    r = etat["ronde_inachevee"]
    assert r["phase"] == "generation" and len(r["faites"]) == 1 and len(r["ordre"]) == 2, r
    assert r["ronde"] == etat["ronde"] and etat["conception_faite"] is True, (r, etat["ronde"], etat["conception_faite"])
    return pathlib.Path(racine)


def _params(memoire_partagee=False):
    return dict(imposes=t.DEUX, generations=2, rondes=0, memoire_partagee=memoire_partagee)


def _accepte(racine, **params):
    n = t._noyau(racine, **params)
    n.reprendre()
    dernier = t._journal(racine)[-1]
    assert dernier["etape"] == "reprise" and dernier["segment"] == 2, dernier


# ---------- dernier événement ----------

def test_sain_dernier_evenement_arret_sur_stop(tmp_path):
    racine = t._course_arretee(tmp_path / "course")
    assert t._journal(racine)[-1]["etape"] == "arret" and t._journal(racine)[-1]["raison"] == "fichier STOP"
    _accepte(racine)


def test_refus_dernier_evenement_autre_que_l_arret_sur_stop(tmp_path):
    racine = t._course_arretee(tmp_path / "course")
    j = racine / "evenements.jsonl"
    lignes = [x for x in j.read_text(encoding="utf-8").splitlines() if x.strip()]
    n_avant = len(lignes)
    dernier = json.loads(lignes[-1])
    dernier["raison"] = "aucune lignée active"  # même nombre d'événements : la garde du nombre ne joue pas, celle-ci seule
    lignes[-1] = json.dumps(dernier, ensure_ascii=False)
    j.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    assert len([x for x in j.read_text(encoding="utf-8").splitlines() if x.strip()]) == n_avant
    t._refus(racine, "le dernier événement de la course n'est pas l'arrêt sur STOP de l'état")


# ---------- ronde de génération en cours ----------

def test_sain_ronde_de_generation_en_cours_coherente(tmp_path):
    racine = _arretee_en_ronde_de_generation(tmp_path / "course")
    _accepte(racine, **_params())


@pytest.mark.parametrize("changer", [
    lambda e: e["ronde_inachevee"].update(ronde=e["ronde"] + 1),   # ronde de la ronde en cours ≠ ronde de l'état
    lambda e: e.update(conception_faite=False),                     # ronde de génération alors que la conception n'est pas faite
], ids=["ronde-autre", "conception-non-faite"])
def test_refus_ronde_de_generation_en_cours_incoherente(tmp_path, changer):
    racine = _arretee_en_ronde_de_generation(tmp_path / "course")
    t._resceller(t._etats(racine)[-1], changer)
    t._refus(racine, "ronde de génération en cours incohérente avec l'état", **_params())


# ---------- vue figée (mémoire partagée) ----------

def test_sain_vue_figee_dans_l_espace(tmp_path):
    racine = _arretee_en_ronde_de_generation(tmp_path / "course", memoire_partagee=True)
    vue = json.loads(t._etats(racine)[-1].read_text(encoding="utf-8"))["ronde_inachevee"]["vue_figee"]
    assert vue and pathlib.Path(vue).is_dir()
    _accepte(racine, **_params(memoire_partagee=True))


@pytest.mark.parametrize("vue", ["absente", "hors-espace", "vide"])
def test_refus_vue_figee_introuvable(tmp_path, vue):
    racine = _arretee_en_ronde_de_generation(tmp_path / "course", memoire_partagee=True)
    ailleurs = tmp_path / "ailleurs"
    ailleurs.mkdir()
    valeur = {"absente": str(tmp_path / "nulle-part"), "hors-espace": str(ailleurs), "vide": ""}[vue]
    t._resceller(t._etats(racine)[-1], lambda e: e["ronde_inachevee"].update(vue_figee=valeur))
    t._refus(racine, "vue figée de la ronde en cours introuvable", **_params(memoire_partagee=True))
