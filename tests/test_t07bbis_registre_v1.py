"""Essais R5 de `t07bbis.registre_bbis_v1` et des scripts de session (B bis, « Lignes de registre », « Liste d'arrêt », « Calcul et
dépense », « Code neuf », épreuves : clé de B bis dans `registres/scellements-v1.md` (refus) ; arrêt au cumul plus un quart d'heure ;
plus la garde d'offre et de création, la fiche de `CODE-BBIS` (épreuve de niveau absente ou réduite : `CODE-BBIS` refusée) et les
sous-commandes de `scripts/lancer_bbis_v1.sh` et de l'amorce en essai local)."""
from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t07bbis import registre_bbis_v1 as rb

RACINE = Path(__file__).resolve().parents[1]
E = 2 ** 127 + 4242


def test_registre_propre_et_refus_du_registre_partage(tmp_path):
    l = rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, "CODE-BBIS", 1789000000, "docs/x.json", "b" * 64)
    assert l.startswith("| CODE-BBIS | 2026-") and (tmp_path / rb.REGISTRE_PROPRE).read_text(encoding="utf-8").count("CODE-BBIS") == 1
    with pytest.raises(GardeArret, match="déjà présente"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, "CODE-BBIS", 1789000001, "docs/x.json", "b" * 64)
    with pytest.raises(GardeArret, match="scellements-v1.md"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PARTAGE, "SCORES-BBIS", 1789000000, "diag/x.json", "c" * 64)
    with pytest.raises(GardeArret, match="seul"):
        rb.ajouter_ligne_propre(tmp_path, "registres/autre-v1.md", "SCORES-BBIS", 1789000000, "diag/x.json", "c" * 64)
    with pytest.raises(GardeArret, match="hors des clés"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, "SCORES-T07", 1789000000, "diag/x.json", "c" * 64)
    partage = tmp_path / rb.REGISTRE_PARTAGE
    partage.write_text("| RUN-CONFIRMATION-T06 | 2026-11-12T05:00:00Z | runs/x/manifeste.json | " + "d" * 64 + " |\n",
                       encoding="utf-8")
    rb.exiger_partage_sans_bbis(partage)
    with open(partage, "a", encoding="utf-8") as f:
        f.write("| SCELLEMENT-BBIS | 2026-11-16T05:00:00Z | prereg/x.md | " + "e" * 64 + " |\n")
    with pytest.raises(GardeArret, match="la garde de T0.7"):
        rb.exiger_partage_sans_bbis(partage)
    with pytest.raises(GardeArret, match="la garde de T0.7"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, "GO-BBIS", 1789000002, "registres/go-extraits/x.md", "f" * 64)


def test_garde_de_depense_au_cumul_plus_un_quart_d_heure():
    assert rb.garde_depense(30.0, 2.0)["projete"] == 30.5
    assert rb.garde_depense(39.0, 1.9)["projete"] == pytest.approx(39.475)
    with pytest.raises(GardeArret, match="destruction par identifiant"):
        rb.garde_depense(39.0, 2.0)
    with pytest.raises(GardeArret, match="coupure"):
        rb.garde_depense(39.5, 0.0)


def test_garde_d_offre_et_de_creation(tmp_path):
    offre = {"carte": "A100 SXM4 80GB", "coeurs": 32, "memoire_vive_mo": 256000, "disque_go": 200, "stockage_usd_h": 0.05,
             "etiquette": "bbis-t07-v1"}
    rb.exiger_offre(offre)
    for faute in ({"carte": "H200 SXM 141GB"}, {"carte": "A100 PCIE 40GB"}, {"disque_go": 100}, {"coeurs": 8},
                  {"memoire_vive_mo": None}, {"etiquette": "t07-x"}, {"stockage_usd_h": 0.2}):
        with pytest.raises(GardeArret, match="hors des bornes"):
            rb.exiger_offre({**offre, **faute})
    t = 1789700000
    with pytest.raises(GardeArret, match="absente"):
        rb.exiger_creation(tmp_path, "feu GO-2026-11-14-09", t)
    for k in ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, k, t - 100, "x", "f" * 64)
    assert rb.exiger_creation(tmp_path, "feu de la mère : GO-2026-11-14-09", 1795003200)["relances"] == 0
    with pytest.raises(GardeArret, match="feu écrit"):
        rb.exiger_creation(tmp_path, "feu sans numéro", 1795003200)
    with pytest.raises(GardeArret, match="seconde relance"):
        rb.exiger_creation(tmp_path, "GO-2026-11-14-09", 1795003200, relances=2)
    with pytest.raises(GardeArret, match="21 novembre"):
        rb.exiger_creation(tmp_path, "GO-2026-11-14-09", 1795262401, relances=1)
    with pytest.raises(GardeArret, match="échéance"):
        rb.exiger_creation(tmp_path, "GO-2026-11-14-09", 1795478400)


def _epreuve(tmp_path, entropie=E, complete=True, taux_nul=0.004, retenu=None):
    from controle_ia.manifeste import cle_de_tache
    doc = {"cellules": {"nul": {"taux": taux_nul}, "signal-commun": {"taux": 0.003}}, "seuil_taux": 0.01,
           "niveau_decisif_retenu": retenu if retenu is not None else (0.995 if taux_nul > 0.01 else 0.99),
           "graine": {"cle": "bbis/epreuve-niveau", "spawn_key": [str(cle_de_tache("bbis/epreuve-niveau"))],
                      "entropie": str(entropie)}, "complete": complete, "cout": {"secondes_murales": 1.0}}
    p = tmp_path / "epreuve.json"
    p.write_text(json.dumps(doc), encoding="utf-8")
    sceller(p)
    return "epreuve.json"


def test_fiche_de_code_bbis_saine_et_refus_sans_epreuve_complete(tmp_path):
    fichiers = {"src/controle_ia/t07bbis/plis_v1.py": "a" * 64}
    with pytest.raises(GardeArret, match="absente"):
        rb.ecrire_fiche_code(tmp_path, "registres/t07-etape-b-bis/code-bbis-v1.json", "c" * 40, fichiers, E, "epreuve.json")
    ep = _epreuve(tmp_path, complete=False)
    with pytest.raises(GardeArret, match="réduite"):
        rb.ecrire_fiche_code(tmp_path, "registres/t07-etape-b-bis/code-bbis-v1.json", "c" * 40, fichiers, E, ep)
    (tmp_path / "epreuve.json").unlink()
    (tmp_path / "epreuve.json.sha256").unlink()
    ep = _epreuve(tmp_path, entropie=E + 1)
    with pytest.raises(GardeArret, match="autre entropie"):
        rb.ecrire_fiche_code(tmp_path, "registres/t07-etape-b-bis/code-bbis-v1.json", "c" * 40, fichiers, E, ep)
    for faute in ({"taux_nul": 0.02, "retenu": 0.99}, {"taux_nul": 0.004, "retenu": 0.995}):
        (tmp_path / "epreuve.json").unlink()
        (tmp_path / "epreuve.json.sha256").unlink()
        ep = _epreuve(tmp_path, **faute)
        with pytest.raises(GardeArret, match="règle du texte"):
            rb.ecrire_fiche_code(tmp_path, "registres/t07-etape-b-bis/code-bbis-v1.json", "c" * 40, fichiers, E, ep)
    for taux, attendu in ((0.004, 0.99), (0.011, 0.995)):
        (tmp_path / "epreuve.json").unlink()
        (tmp_path / "epreuve.json.sha256").unlink()
        ep = _epreuve(tmp_path, taux_nul=taux)
        chemin = f"registres/t07-etape-b-bis/code-bbis-{attendu}.json"
        f = rb.ecrire_fiche_code(tmp_path, chemin, "c" * 40, fichiers, E, ep)
        assert f["niveau_decisif"] == attendu
        lu = rb.lire_fiche_code(tmp_path / chemin)
        assert lu["entropie"] == E and lu["niveau_decisif"] == attendu
        with pytest.raises(GardeArret, match="existe déjà"):
            rb.ecrire_fiche_code(tmp_path, chemin, "c" * 40, fichiers, E, ep)
    with pytest.raises(GardeArret, match="40 caractères"):
        rb.ecrire_fiche_code(tmp_path, "x.json", "c" * 39, fichiers, E, ep)
    with pytest.raises(GardeArret, match="64 bits"):
        rb.ecrire_fiche_code(tmp_path, "x.json", "c" * 40, fichiers, 12345, ep)
    faux = tmp_path / "faux.json"
    faux.write_text(json.dumps({"entropie": "1", "niveau_decisif": 0.98, "commit": "c" * 40,
                                "epreuve_niveau": {"niveau_decisif_retenu": 0.98, "sha256": "a" * 64}}), encoding="utf-8")
    with pytest.raises(GardeArret, match="0,99 ou 0,995"):
        rb.lire_fiche_code(faux)


def _bash(*args, env=None):
    e = dict(os.environ)
    e.update({"PYTHON_BBIS": str(Path(os.sys.executable))})
    e.update(env or {})
    return subprocess.run(["bash", str(RACINE / "scripts" / "lancer_bbis_v1.sh"), *args], capture_output=True, text=True, env=e)


def test_scripts_de_session_syntaxe_et_sous_commandes(tmp_path):
    for s in ("lancer_bbis_v1.sh", "amorce_bbis_v1.sh"):
        assert subprocess.run(["bash", "-n", str(RACINE / "scripts" / s)]).returncode == 0
    offre = tmp_path / "offre.json"
    offre.write_text(json.dumps({"carte": "A100 SXM4 80GB", "coeurs": 32, "memoire_vive_mo": 256000, "disque_go": 200,
                                 "stockage_usd_h": 0.05, "etiquette": "bbis-t07-v1"}), encoding="utf-8")
    r = _bash("offre", str(offre))
    assert r.returncode == 0 and "ACCEPTEE" in r.stdout
    offre.write_text(json.dumps({"carte": "H200"}), encoding="utf-8")
    assert _bash("offre", str(offre)).returncode == 2
    r = _bash("depense", "39.0", "2.0")
    assert r.returncode == 2 and "destruction" in r.stdout and "detruire" in r.stdout
    assert _bash("depense", "10", "1.3").returncode == 0
    r = _bash("detruire", "123456")
    assert r.returncode == 0 and r.stdout.strip() == "GO_ID=GO-2026-11-14-09 vastai destroy instance 123456"
    assert _bash("detruire", "inst*").returncode == 2
    assert _bash("creer").returncode == 2
    r = _bash("commande", str(tmp_path), "99", "c" * 40, "main", "20261111-151701-t06-reel", "calcul/x", "20261118-090000-bbis-t07",
              "1795000000", "feu GO-2026-11-14-09", "0", "python:3.11-bookworm")
    assert r.returncode == 2 and "absente" in r.stdout                        # aucune ligne au registre propre : refus
    for k in ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"):
        rb.ajouter_ligne_propre(tmp_path, rb.REGISTRE_PROPRE, k, 1789000000, "x", "f" * 64)
    r = _bash("commande", str(tmp_path), "99", "c" * 40, "main", "20261111-151701-t06-reel", "calcul/x", "20261118-090000-bbis-t07",
              "1795000000", "feu GO-2026-11-14-09", "0", "python:3.11-bookworm")
    if time.time() > rb._instant(rb.ECHEANCE_GO):                            # après l'échéance de la ligne de GO : refus
        assert r.returncode == 2 and "échéance" in r.stdout
    else:
        assert r.returncode == 0 and "vastai create instance 99" in r.stdout and "--label bbis-t07-v1" in r.stdout
        assert "HF_TOKEN=$HF_TOKEN" in r.stdout and "GO_ID=GO-2026-11-14-09 vastai" in r.stdout
    r = _bash("commande", str(tmp_path), "99", "c" * 39, "main", "20261111-151701-t06-reel", "calcul/x", "20261118-090000-bbis-t07",
              "1795000000", "feu GO-2026-11-14-09", "0", "python:3.11-bookworm")
    assert r.returncode == 2 and "amorce" in r.stdout


def test_amorce_en_essai_local_refuse_les_arguments_fautifs(tmp_path):
    base = {"AMORCE_ESSAI_LOCAL": "1", "COMMIT": "c" * 40, "BRANCHE_CODE": "main", "RUN_7B": "20261111-151701-t06-reel",
            "BRANCHE_7B": "calcul/x", "RUN_BBIS": "20261118-090000-bbis-t07", "ECHEANCE_UTC_S": "1795000000",
            "GO_ID": "GO-2026-11-14-09", "RACINE_AMORCE": str(tmp_path)}

    def jouer(**k):
        e = dict(os.environ)
        e.update(base)
        e.update(k)
        return subprocess.run(["bash", str(RACINE / "scripts" / "amorce_bbis_v1.sh")], capture_output=True, text=True, env=e)

    r = jouer()
    assert r.returncode == 0 and "ESSAI LOCAL" in r.stdout
    for faute in ({"GO_ID": "GO-2026-11-02-28"}, {"COMMIT": "xyz"}, {"RUN_BBIS": "bbis"}, {"ECHEANCE_UTC_S": "demain"}):
        r = jouer(**faute)
        assert r.returncode == 2 and "REFUS" in r.stdout


def test_commande_fiche_empreintes_lues_sur_le_disque(tmp_path, capsys):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "x.py").write_text("print(1)\n", encoding="utf-8")
    ep = _epreuve(tmp_path)
    assert rb.main(["fiche", str(tmp_path), "registres/t07-etape-b-bis/code-bbis-v1.json", "c" * 40, str(E), ep, "src/x.py"]) == 0
    assert "FICHE ECRITE" in capsys.readouterr().out
    from controle_ia.scellement import empreinte
    f = rb.lire_fiche_code(tmp_path / "registres/t07-etape-b-bis/code-bbis-v1.json")
    assert f["fichiers"] == {"src/x.py": empreinte(tmp_path / "src" / "x.py")} and f["niveau_decisif"] == 0.99
    assert rb.main(["fiche", str(tmp_path), "autre.json", "c" * 40, str(E), "absente.json", "src/x.py"]) == 2
