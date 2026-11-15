"""Essais de la répétition sur carte v2 (quatrième passe ; contrôle carte-processeur aux deux horizons de la course v2, R-2917) :
`scripts/repetition_carte_bbis_v2.py`, `scripts/amorce_repetition_bbis_v2.sh`, `scripts/lancer_repetition_bbis_v2.sh`.

- Chaque version neuve est **la v1 plus un différentiel déclaré ici** (couples « ancien, nouveau, nombre d'occurrences ») :
  l'essai refait la v2 depuis la v1 et exige l'égalité exacte ; les essais de la v1 (`test_repetition_bbis_v1.py` : blocs marqués,
  faux outils, gardes de destruction, de dépense, d'offre) valent donc pour la v2 hors de ces lignes.
- Partie carte sur processeur : cas sain (code 0 ; contrôle linéaire à 300 époques, attention à 3 époques, déterminisme ; résumé
  de l'amorce v2 lisible) ; artefacts : poids de l'attention à 3 époques altérés de 1 % sur la « carte » (code 9, motif écrit),
  autre graine pour l'attention à 3 époques (code 9), non-déterminisme simulé (code 9).
Données synthétiques seulement ; aucune entrée de 7b."""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
from pathlib import Path

import numpy as np
import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "repetition_carte_bbis_v2.py"
AMORCE_REP = RACINE / "scripts" / "amorce_repetition_bbis_v2.sh"

ANCIEN_CONTROLE = '''        etape = "contrôle carte-processeur"
        doc["controle_carte_processeur"] = {}
        for f, (r, g, s) in sondes.items():
            t0 = time.perf_counter()
            try:
                c = ac.controle_carte_processeur(s, seqs, y, r, g, ctrl, tolerance=tol)
            except GardeArret as e:
                doc["controle_carte_processeur"][f] = {"refus": str(e), "duree_s": time.perf_counter() - t0}
                return ecrire("controle", CODES["controle"], f"{f} : {e}")
            c["duree_s"] = time.perf_counter() - t0
            doc["controle_carte_processeur"][f] = c
'''
NOUVEAU_CONTROLE = '''        etape = "contrôle carte-processeur"
        t0 = time.perf_counter()
        l2_c = float(reglages[0]["l2"])                    # premier réglage de chaque famille (couche 15), comme la v1

        def graine_de(f):
            return int(_graine(f"bbis/repetition/sonde/{f}/{l2_c}").generate_state(1)[0])
        try:                                               # la fonction de la course v2, telle quelle
            c = vi.controle_deux_horizons(lot, seqs, y, COUCHE, l2_c, graine_de, ctrl, familles=FAMILLES,
                                          sondes_300={f: s for f, (r, g, s) in sondes.items() if r["l2"] == l2_c},
                                          tolerance=tol, nom="repetition")
        except GardeArret as e:
            doc["controle_carte_processeur"] = {"arret": {"refus": str(e), "duree_s": time.perf_counter() - t0}}
            return ecrire("controle", CODES["controle"], str(e))
        doc["controle_carte_processeur"] = {f: c[f] for f in ("lineaire", "attention") if f in c}
        if "determinisme_attention" in c:                  # égalité au bit près : écart nul (lu par le résumé de l'amorce)
            doc["controle_carte_processeur"]["determinisme_attention"] = {**c["determinisme_attention"], "ecart_relatif_max": 0.0}
        doc["controle_parametres"] = {k: c[k] for k in ("tolerance", "couche", "l2", "familles")}
        doc["controle_parametres"]["duree_s"] = time.perf_counter() - t0
'''
COUPLES = {
    "scripts/repetition_carte_bbis_v2.py": ("scripts/repetition_carte_bbis_v1.py", [
        ("une seule machine), v1.\n",
         "une seule machine), v2 : la v1, dont\nle contrôle carte-processeur est celui de la course v2 "
         "(`t07bbis.validation_imbriquee_v2.controle_deux_horizons` : linéaire à\n300 époques, attention à 3 époques, déterminisme "
         "de l'attention à 300 époques ; brouillon 4, plan, point 5 ; R-2917) ; quatrième\npasse ; la v1 reste (R12).\n", 1),
        ("`harnais.modeles.regler_determinisme` et les constantes de la garde de débit (`t07bbis.validation_imbriquee_v1`,",
         "`harnais.modeles.regler_determinisme`, le contrôle aux deux horizons et les constantes de la garde de débit\n"
         "(`t07bbis.validation_imbriquee_v2`, qui reprend la v1,", 1),
        ("scripts/amorce_repetition_bbis_v1.sh", "scripts/amorce_repetition_bbis_v2.sh", 1),
        ("scripts/lancer_repetition_bbis_v1.sh", "scripts/lancer_repetition_bbis_v2.sh", 1),
        ("**contrôle carte-processeur** de chaque famille au seuil du texte (10⁻⁴, 256 actions de contrôle tirées à part) ;",
         "**contrôle carte-processeur** au seuil du texte (10⁻⁴, 256 actions de contrôle tirées à part), aux deux horizons de la\n"
         "  course v2 (linéaire à 300 époques, attention à 3 époques, déterminisme de l'attention à 300 époques) ;", 1),
        ("        from controle_ia.t07bbis import validation_imbriquee_v1 as vi\n",
         "        from controle_ia.t07bbis import validation_imbriquee_v2 as vi\n", 1),
        (ANCIEN_CONTROLE, NOUVEAU_CONTROLE, 1)]),
    "scripts/amorce_repetition_bbis_v2.sh": ("scripts/amorce_repetition_bbis_v1.sh", [
        ("# Amorce de la répétition sur carte de l'étape B bis de T0.7, v1 (",
         "# Amorce de la répétition sur carte de l'étape B bis de T0.7, v2 (quatrième passe : la v1, qui joue\n"
         "# scripts/repetition_carte_bbis_v2.py et lit scripts/amorce_bbis_v2.sh ; contrôle carte-processeur aux deux horizons,\n"
         "# R-2917 ; blocs marqués identiques à ceux de la v1 hors les noms ; la v1 reste, R12) (", 1),
        ("Passée par scripts/lancer_repetition_bbis_v1.sh", "Passée par scripts/lancer_repetition_bbis_v2.sh", 1),
        ("#   calcul/t07bbis-repetition-v2 (commit des seules traces", "#   calcul/t07bbis-repetition-v3 (commit des seules traces", 1),
        ("XT=traces/bbis-t07-repetition-v1\n", "XT=traces/bbis-t07-repetition-v2\n", 1),
        ("# R12 : nouvelle passe, nouveau nom (calcul/t07bbis-repetition-v1 porte les traces de la passe du 15 novembre, 56f5b8b8)\n"
         "BR_SORTIE=calcul/t07bbis-repetition-v2\n",
         "# R12 : nouvelle passe, nouveau nom (calcul/t07bbis-repetition-v1 : passe du 15 novembre, 56f5b8b8 ;\n"
         "# calcul/t07bbis-repetition-v2 : troisième passe, 3528a2e8, arrêt en code 9)\nBR_SORTIE=calcul/t07bbis-repetition-v3\n", 1),
        ("scripts/amorce_bbis_v1.sh", "scripts/amorce_bbis_v2.sh", 3),
        ("repetition_carte_bbis_v1.py", "repetition_carte_bbis_v2.py", 2)]),
    "scripts/lancer_repetition_bbis_v2.sh": ("scripts/lancer_repetition_bbis_v1.sh", [
        ("# Chaîne de session de la répétition sur carte de l'étape B bis de T0.7, v1 (",
         "# Chaîne de session de la répétition sur carte de l'étape B bis de T0.7, v2 (quatrième passe : la v1, qui passe\n"
         "# l'amorce et le script de la répétition v2 ; R-2917 ; la v1 reste, R12) (", 1),
        ("repetition_carte_bbis_v1.py", "repetition_carte_bbis_v2.py", 2),
        ("amorce_repetition_bbis_v1.sh", "amorce_repetition_bbis_v2.sh", 8),
        ("scripts/amorce_bbis_v1.sh", "scripts/amorce_bbis_v2.sh", 1),
        ("lancer_repetition_bbis_v1.sh", "lancer_repetition_bbis_v2.sh", 3)]),
}


def appliquer(texte: str, couples) -> str:
    for ancien, nouveau, n in couples:
        assert texte.count(ancien) == n, (ancien[:70], texte.count(ancien), n)
        texte = texte.replace(ancien, nouveau)
    return texte


@pytest.mark.parametrize("v2", sorted(COUPLES))
def test_v2_egale_a_la_v1_plus_le_differentiel_declare(v2):
    v1, couples = COUPLES[v2]
    assert (RACINE / v2).read_text(encoding="utf-8") == appliquer((RACINE / v1).read_text(encoding="utf-8"), couples)


def test_branche_de_sortie_neuve_et_noms_de_la_v2():
    a = AMORCE_REP.read_text(encoding="utf-8")
    assert re.findall(r"^BR_SORTIE=(.*)$", a, re.M) == ["calcul/t07bbis-repetition-v3"]
    assert "repetition_carte_bbis_v1" not in a and "scripts/amorce_bbis_v1.sh" not in a
    lanceur = (RACINE / "scripts" / "lancer_repetition_bbis_v2.sh").read_text(encoding="utf-8")
    assert "_v1.sh" not in lanceur.replace("registre_bbis_v1", "") and "repetition_carte_bbis_v1" not in lanceur


@pytest.fixture
def torch_restaure():
    import torch
    fils, det = torch.get_num_threads(), torch.are_deterministic_algorithms_enabled()
    yield
    torch.set_num_threads(fils)
    torch.use_deterministic_algorithms(det)


def _module():
    spec = importlib.util.spec_from_file_location("repetition_carte_bbis_v2", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _resume(sortie: Path) -> subprocess.CompletedProcess:
    t = AMORCE_REP.read_text(encoding="utf-8")
    bloc = re.findall(r"^# >>> lecture-de-la-course\b[^\n]*\n(.*?)^# <<< lecture-de-la-course$", t, re.S | re.M)
    assert len(bloc) == 1
    import sys
    return subprocess.run(["bash", "-c", bloc[0] + '\nresume_carte "$0" "$1"', sys.executable, str(sortie)],
                          capture_output=True, text=True, timeout=60)


PETIT = dict(appareil="cpu", n_actions=24, largeur=32, par_famille=2)


def test_carte_v2_sur_processeur_cas_sain_et_resume(tmp_path, torch_restaure):
    m = _module()
    assert m.jouer_carte(tmp_path / "sain.json", **PETIT) == 0
    d = json.loads((tmp_path / "sain.json").read_text(encoding="utf-8"))
    c = d["controle_carte_processeur"]
    assert d["etat"] == "reussie" and d["deterministe"] == {"lineaire": True, "attention": True}
    assert c["lineaire"]["epoques"] == 300 and c["attention"]["epoques"] == 3 and c["determinisme_attention"]["egal_au_bit"]
    assert max(c["lineaire"]["ecart_relatif_max"], c["attention"]["ecart_relatif_max"]) <= 1e-4
    assert d["controle_parametres"]["l2"] == 1e-3 and d["controle_parametres"]["couche"] == 15
    r = _resume(tmp_path / "sain.json")
    assert r.returncode == 0 and "Traceback" not in r.stderr and "écarts carte-processeur" in r.stdout, (r.stdout, r.stderr)
    assert "'determinisme_attention': 0.0" in r.stdout


def test_carte_v2_artefacts_codes_9(tmp_path, monkeypatch, torch_restaure):
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
    d = json.loads((tmp_path / "alteree.json").read_text(encoding="utf-8"))
    assert "attention à 3 époques" in d["motif"] and "erreur de chaîne" in d["motif"] and "arret" in d["controle_carte_processeur"]

    def autre_graine(lot, famille, nom, couche, y, l2, graine, *a, epoques=300, **k):
        return vrai(lot, famille, nom, couche, y, l2, graine + (1 if epoques == 3 else 0), *a, epoques=epoques, **k)
    monkeypatch.setattr(ac, "entrainer", autre_graine)
    assert m.jouer_carte(tmp_path / "graine.json", **PETIT) == 9
    assert "attention à 3 époques" in json.loads((tmp_path / "graine.json").read_text(encoding="utf-8"))["motif"]

    def instable(lot, famille, nom, *a, **k):
        s = vrai(lot, famille, nom, *a, **k)
        if nom.endswith("-bis"):
            s.w[0] = np.nextafter(s.w[0], np.inf)
        return s
    monkeypatch.setattr(ac, "entrainer", instable)
    assert m.jouer_carte(tmp_path / "instable.json", **PETIT) == 9
    assert "non déterministe" in json.loads((tmp_path / "instable.json").read_text(encoding="utf-8"))["motif"]
