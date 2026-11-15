"""Essais de la répétition sur carte v3 (quatrième passe, suffixe unique v4 ; R-2919, m1, m3, m8, m9) :
`scripts/repetition_carte_bbis_v3.py`, `scripts/amorce_repetition_bbis_v3.sh`, `scripts/lancer_repetition_bbis_v3.sh`.

- Chaque v3 = la v2 + un différentiel déclaré (`aide_t07bbis_differentiels_v3.COUPLES`), refait et comparé ; les essais des v1 et
  v2 valent hors de ces lignes.
- Partie carte sur processeur : cas sain (code 0 ; contrôle de la course v3 sur un **lot reconstruit**, égal au premier au bit
  près ; lecture de la passe « la course part sans nœud » ; résumé de l'amorce v3 qui l'écrit) ; écart entre 10⁻⁵ et 10⁻⁴ : code 0
  et « nœud écrit à la mère avant la course » ; passe qui ne compte pas (écart non numérique, égalité absente) : code 9 ; poids de
  l'attention à 3 époques altérés de 1 % : code 9 ; règle de lecture éprouvée seule sur ses cas limites.
Données synthétiques seulement ; aucune entrée de 7b."""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

import aide_t07bbis_differentiels_v3 as dif

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "repetition_carte_bbis_v3.py"
AMORCE_REP = RACINE / "scripts" / "amorce_repetition_bbis_v3.sh"
LANCER_REP = RACINE / "scripts" / "lancer_repetition_bbis_v3.sh"
FICHIERS = ("scripts/repetition_carte_bbis_v3.py", "scripts/amorce_repetition_bbis_v3.sh", "scripts/lancer_repetition_bbis_v3.sh")


@pytest.mark.parametrize("neuf", FICHIERS)
def test_v3_egale_a_la_v2_plus_le_differentiel_declare(neuf):
    ancien, couples = dif.COUPLES[neuf]
    assert (RACINE / neuf).read_text(encoding="utf-8") == dif.appliquer((RACINE / ancien).read_text(encoding="utf-8"), couples)


def test_suffixe_unique_v4_et_noms_de_la_v3():
    a = AMORCE_REP.read_text(encoding="utf-8")
    assert re.findall(r"^BR_SORTIE=(.*)$", a, re.M) == ["calcul/t07bbis-repetition-v4"]
    assert 'T="$R/bbis-t07-repetition-v4"' in a and "XT=traces/bbis-t07-repetition-v4\n" in a
    assert "repetition_carte_bbis_v3.py" in a and "scripts/amorce_bbis_v3.sh" in a
    assert not re.search(r"repetition_carte_bbis_v[12]|amorce_bbis_v[12]\.sh|bbis-t07-repetition-v[123]\b(?! :)", a.split("\n", 6)[6])
    lanceur = LANCER_REP.read_text(encoding="utf-8")
    assert "ETIQUETTE=bbis-t07-repetition-v4\n" in lanceur and "amorce_repetition_bbis_v3.sh" in lanceur
    assert not re.search(r"repetition_carte_bbis_v[12]|amorce_repetition_bbis_v[12]|lancer_repetition_bbis_v[12]", lanceur)
    assert 'ETIQUETTE = "bbis-t07-repetition-v4"' in SCRIPT.read_text(encoding="utf-8")


@pytest.fixture
def torch_restaure():
    import torch
    fils, det = torch.get_num_threads(), torch.are_deterministic_algorithms_enabled()
    yield
    torch.set_num_threads(fils)
    torch.use_deterministic_algorithms(det)


def _module():
    spec = importlib.util.spec_from_file_location("repetition_carte_bbis_v3", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _resume(sortie: Path) -> subprocess.CompletedProcess:
    t = AMORCE_REP.read_text(encoding="utf-8")
    bloc = re.findall(r"^# >>> lecture-de-la-course\b[^\n]*\n(.*?)^# <<< lecture-de-la-course$", t, re.S | re.M)
    assert len(bloc) == 1
    return subprocess.run(["bash", "-c", bloc[0] + '\nresume_carte "$0" "$1"', sys.executable, str(sortie)],
                          capture_output=True, text=True, timeout=60)


PETIT = dict(appareil="cpu", n_actions=24, largeur=32, par_famille=2)


def test_carte_v3_cas_sain_lot_reconstruit_lecture_et_resume(tmp_path, torch_restaure, monkeypatch):
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    lots = []
    vrai = ac.LotCarte

    class Espion(vrai):
        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            lots.append(self)
    monkeypatch.setattr(ac, "LotCarte", Espion)
    m = _module()
    assert m.jouer_carte(tmp_path / "sain.json", **PETIT) == 0
    d = json.loads((tmp_path / "sain.json").read_text(encoding="utf-8"))
    c = d["controle_carte_processeur"]
    assert len(lots) == 2 and lots[0] is not lots[1] and d["lot_reconstruit"] == {"egal_au_premier": True}
    assert c["lineaire"]["epoques"] == 300 and c["attention"]["epoques"] == 3 and c["determinisme_attention"]["egal_au_bit"]
    lp = d["lecture_de_la_passe"]
    assert lp["compte"] and lp["issue"] == "la course part sans nœud" and max(lp["ecarts"].values()) <= 1e-5
    assert d["controle_parametres"]["memoire_carte_max_octets"] is None                          # pas de carte ici
    r = _resume(tmp_path / "sain.json")
    assert r.returncode == 0 and "Traceback" not in r.stderr and "lecture de la passe" in r.stdout and "sans nœud" in r.stdout


def _ecarts_forces(monkeypatch, lin, att, egal=True):
    from controle_ia.t07bbis import validation_imbriquee_v3 as vi3
    vrai = vi3.controle_deux_horizons

    def faux(*a, **k):
        c = vrai(*a, **k)
        c["lineaire"]["ecart_relatif_max"], c["attention"]["ecart_relatif_max"] = lin, att
        if not egal:
            c["determinisme_attention"]["egal_au_bit"] = False
        return c
    monkeypatch.setattr(vi3, "controle_deux_horizons", faux)


def test_carte_v3_noeud_entre_1e5_et_1e4_et_passe_qui_ne_compte_pas(tmp_path, torch_restaure, monkeypatch):
    m = _module()
    _ecarts_forces(monkeypatch, 2e-8, 5e-5)
    assert m.jouer_carte(tmp_path / "noeud.json", **PETIT) == 0
    lp = json.loads((tmp_path / "noeud.json").read_text(encoding="utf-8"))["lecture_de_la_passe"]
    assert lp["compte"] and lp["issue"].startswith("nœud écrit à la mère avant la course")
    for nom, lin, att, egal in (("non-numerique", None, 3e-7, True), ("chaine", "2e-8", 3e-7, True), ("inegal", 2e-8, 3e-7, False)):
        _ecarts_forces(monkeypatch, lin, att, egal)
        assert m.jouer_carte(tmp_path / f"{nom}.json", **PETIT) == 9
        d = json.loads((tmp_path / f"{nom}.json").read_text(encoding="utf-8"))
        assert "la passe ne compte pas" in d["motif"] and not d["lecture_de_la_passe"]["compte"]


def test_carte_v3_poids_de_l_attention_alteres_code_9(tmp_path, torch_restaure, monkeypatch):
    from controle_ia.sondes.familles import SondeLineaireJetons
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    m = _module()
    vrai = ac.entrainer

    def altere_a_3(lot, famille, nom, *a, epoques=300, **k):
        s = vrai(lot, famille, nom, *a, epoques=epoques, **k)
        if famille == "attention" and epoques == 3:
            return SondeLineaireJetons(s.nom, s.couche, s.agregation, s.w * 1.01, s.b, s.q, s.famille)
        return s
    monkeypatch.setattr(ac, "entrainer", altere_a_3)
    assert m.jouer_carte(tmp_path / "alteree.json", **PETIT) == 9
    assert "attention à 3 époques" in json.loads((tmp_path / "alteree.json").read_text(encoding="utf-8"))["motif"]


def test_regle_de_lecture_de_la_passe_seule():
    m = _module()
    base = {"controle_carte_processeur": {"lineaire": {"ecart_relatif_max": 1e-5}, "attention": {"ecart_relatif_max": 1e-5},
                                          "determinisme_attention": {"egal_au_bit": True}},
            "deterministe": {"lineaire": True, "attention": True}, "lot_reconstruit": {"egal_au_premier": True}}
    assert m.lecture_de_la_passe(base)["issue"] == "la course part sans nœud"                    # 10⁻⁵ compris
    c = json.loads(json.dumps(base))
    c["controle_carte_processeur"]["attention"]["ecart_relatif_max"] = 1e-4                      # 10⁻⁴ compris : nœud
    assert m.lecture_de_la_passe(c)["compte"] and "nœud" in m.lecture_de_la_passe(c)["issue"]
    for chemin, valeur in ((("controle_carte_processeur", "attention", "ecart_relatif_max"), 1.0000001e-4),
                           (("controle_carte_processeur", "lineaire", "ecart_relatif_max"), float("nan")),
                           (("deterministe", "lineaire"), False), (("lot_reconstruit", "egal_au_premier"), False)):
        x = json.loads(json.dumps(base))
        y = x
        for k in chemin[:-1]:
            y = y[k]
        y[chemin[-1]] = valeur
        assert not m.lecture_de_la_passe(x)["compte"], chemin
