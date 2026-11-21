"""Essais des corrections demandées par la contre-lecture du code de la lecture des sondes de l'étape B bis par la lentille
publique (cas sain et artefact pour chaque garde neuve, R5), et des gardes dont le retrait n'était vu par aucun essai."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")
sys.path.insert(0, str(Path(__file__).resolve().parent))

import lentilles_sondes_bbis_jouets_v3 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import entrees_v2 as en  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v3 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, FormeMalComprise, Refus  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402


# --- fiche CODE-LENTILLES-BBIS ------------------------------------------------------------------------------------------------------
def _ligne(propre):
    return en.exiger_registre_propre(propre)["CODE-LENTILLES-BBIS"]


def test_fiche_code_saine(tmp_path):
    _, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    rendu = la.exiger_fiche_code(tmp_path / "depot", _ligne(propre))
    assert rendu["fiche"] == J.CHEMIN_FICHE_CODE


def test_fiche_code_absente_ou_d_une_autre_empreinte_refus(tmp_path):
    _, propre = J.ecrire_registres(tmp_path / "r")
    with pytest.raises(Refus, match="absente ou d'une autre empreinte"):          # ligne jouet sans fiche
        la.exiger_fiche_code(tmp_path / "depot", _ligne(propre))
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    p = tmp_path / "depot" / J.CHEMIN_FICHE_CODE
    p.write_text(p.read_text() + " ")
    with pytest.raises(Refus, match="absente ou d'une autre empreinte"):
        la.exiger_fiche_code(tmp_path / "depot", _ligne(propre))


def test_fiche_code_module_d_une_autre_empreinte_ou_absent_refus(tmp_path):
    _, propre = J.ecrire_registres(tmp_path / "r")
    paquet = J.RACINE / "src" / "controle_ia" / "lentilles_sondes_bbis"
    fichiers = {f"src/controle_ia/lentilles_sondes_bbis/{f.name}": J.sha(f.read_bytes()) for f in paquet.glob("*.py")}
    fichiers["src/controle_ia/lentilles_sondes_bbis/lecture_v1.py"] = "6" * 64
    J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers)
    with pytest.raises(Refus, match="lecture_v1.py : empreinte"):
        la.exiger_fiche_code(tmp_path / "depot", _ligne(propre))
    del fichiers["src/controle_ia/lentilles_sondes_bbis/lecture_v1.py"]
    J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers)
    with pytest.raises(Refus, match="lecture_v1.py : empreinte"):
        la.exiger_fiche_code(tmp_path / "depot", _ligne(propre))


def test_fiche_code_d_une_autre_forme_refus(tmp_path):
    _, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    p = tmp_path / "depot" / J.CHEMIN_FICHE_CODE
    fiche = json.loads(p.read_text())
    del fiche["contre_lecture"]
    p.write_text(json.dumps(fiche))
    lignes = [l for l in propre.read_text().splitlines() if not l.startswith("| CODE-LENTILLES-BBIS |")]
    propre.write_text("\n".join(lignes + [f"| CODE-LENTILLES-BBIS | {J.HEURE} | {J.CHEMIN_FICHE_CODE} | {J.sha(p.read_bytes())} |"]) + "\n")
    with pytest.raises(Refus, match="autre forme"):
        la.exiger_fiche_code(tmp_path / "depot", _ligne(propre))


def test_montage_sans_fiche_code_refus_avant_toute_requete(tmp_path):
    m = J.monde(tmp_path)
    lignes = [l for l in m.registre_propre.read_text().splitlines() if not l.startswith("| CODE-LENTILLES-BBIS |")]
    m.registre_propre.write_text("\n".join(lignes + [f"| CODE-LENTILLES-BBIS | {J.HEURE} | registres/absente.json | {'7' * 64} |"]) + "\n")
    with pytest.raises(Refus, match="CODE-LENTILLES-BBIS"):
        la.monter(m.ctx)
    assert not m.transport.appels
    assert not (tmp_path / "travail").exists()


# --- scellement antérieur au verdict (liste d'arrêt, ligne 1) ----------------------------------------------------------------------------
def test_verdict_anterieur_au_scellement_ou_relevé_d_absence_manquant_refus(tmp_path):
    w = J.monde_entrees(tmp_path)
    en.ouvrir_entrees(w.racine, w.registre_bbis, w.registre_propre, J.LARGEUR)                # cas sain : verdict postérieur
    texte = w.registre_bbis.read_text().replace(J.HEURE_VERDICT, "2026-11-18T23:00:00Z")
    w.registre_bbis.write_text(texte)
    with pytest.raises(Refus, match="déjà présente"):
        en.ouvrir_entrees(w.racine, w.registre_bbis, w.registre_propre, J.LARGEUR)
    _, propre = J.ecrire_registres(tmp_path / "r2", propres=("SCELLEMENT-LENTILLES-BBIS", "GO-LENTILLES-BBIS", "CODE-LENTILLES-BBIS"))
    with pytest.raises(Refus, match="ABSENCE-VERDICT"):
        en.exiger_scellement_avant_verdict(propre, en.exiger_scores_et_verdict(J.ecrire_registres(tmp_path / "r3")[0]))


# --- gardes des entrées dont le retrait n'était vu par aucun essai -----------------------------------------------------------------
def _e2(w):
    return Path(w.racine) / f"diag/{J.RUN_BBIS}/sondes-bbis.json"


def _reecrire_e2(w, changer):
    p = _e2(w)
    doc = json.loads(p.read_text())
    changer(doc)
    p.write_text(json.dumps(doc))
    J.compagnon(p)
    bbis, propre = J.ecrire_registres(Path(w.racine).parent / "reg-neuf", J.sha(p.read_bytes()))
    J.ecrire_fiche_code(Path(w.racine).parent / "depot-neuf", propre)
    return bbis, propre


@pytest.mark.parametrize("changer, motif", [
    (lambda d: d.__setitem__("run_id", "autre-course"), "run_id"),
    (lambda d: d["fichier_sondes"].__setitem__("fichier", "donnees/autre/sondes-bbis.npz"), "fichier_sondes.fichier"),
    (lambda d: d["sources"]["P-S75"]["e0"].__setitem__("cellule", "P-S50"), "cellule ou pli_lu"),
    (lambda d: d["sources"]["P-S75"]["e0"].__setitem__("pli_lu", 1), "cellule ou pli_lu"),
])
def test_entrees_champs_de_concordance_artefacts_arret(tmp_path, changer, motif):
    w = J.monde_entrees(tmp_path)
    bbis, propre = _reecrire_e2(w, changer)
    with pytest.raises(FormeMalComprise, match=motif):
        en.ouvrir_entrees(w.racine, bbis, propre, J.LARGEUR)


def test_scellement_qui_ne_cite_pas_ce_texte_refus(tmp_path):
    _, propre = J.ecrire_registres(tmp_path / "r")
    propre.write_text(propre.read_text().replace(K.EMPREINTE_TEXTE, "8" * 64))
    with pytest.raises(Refus, match="ne cite pas le texte"):
        en.exiger_registre_propre(propre)


def test_chemin_de_scores_bbis_autre_que_e2_attendu_arret(tmp_path):
    w = J.monde_entrees(tmp_path)
    texte = w.registre_bbis.read_text().replace(f"diag/{J.RUN_BBIS}/sondes-bbis.json", "diag/autre-course/sondes-bbis.json")
    w.registre_bbis.write_text(texte)
    with pytest.raises(Arret):
        en.ouvrir_entrees(w.racine, w.registre_bbis, w.registre_propre, J.LARGEUR)


# --- versement avant le nettoyage et à l'arrêt ; sorties hors du dossier de travail ------------------------------------------------
def test_sortie_dans_le_dossier_de_travail_refus(tmp_path):
    m = J.monde(tmp_path)
    for sortie in (tmp_path / "travail" / "sortie", tmp_path / "travail"):
        with pytest.raises(Arret, match="emboîtés"):
            la.Contexte(tmp_path / "travail", sortie, J.RUN, m.ctx.racine_depot, m.registre_propre)
    with pytest.raises(Arret, match="emboîtés"):
        la.Contexte(tmp_path / "sortie" / "travail", tmp_path / "sortie", J.RUN, m.ctx.racine_depot, m.registre_propre)


def test_calcul_verse_le_travail_avant_de_le_supprimer(tmp_path):
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis)
    v = rendu["versement_du_travail"]
    inventaire = json.loads((tmp_path / "sortie" / v["chemin"]).read_text())
    assert verifier(tmp_path / "sortie" / v["chemin"]) == v["sha256"]
    noms = {f["chemin"] for f in inventaire["fichiers"]}
    assert "jetons-gardes.json" in noms and any(n.startswith("tenseurs/") for n in noms)
    assert "jetons-gardes.json" in inventaire["copies"] and not any(c.startswith(("tenseurs", "lentille", "hf")) for c in inventaire["copies"])
    copie = tmp_path / "sortie" / f"versement/{J.RUN}/travail-fin/fichiers/jetons-gardes.json"
    verifier(copie)
    assert not (tmp_path / "sortie" / f"versement/{J.RUN}/travail-fin/fichiers/tenseurs").exists()
    assert not (tmp_path / "travail").exists()
    for p in (tmp_path / "sortie").rglob("*"):
        if p.is_file():
            assert J.FAUSSE_CLE.encode() not in p.read_bytes(), p


def test_arret_en_cours_de_calcul_verse_ce_qui_existe_sans_rien_supprimer(tmp_path):
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    appels = {"n": 0}

    def disque(chemin):
        appels["n"] += 1
        libre = 10 ** 12 if appels["n"] < 4 else 0                      # l'espace manque après la première direction
        return la.shutil._ntuple_diskusage(10 ** 12, 0, libre)
    m.ctx.mesure_disque = disque
    m.reglages.disque_calcul = 10 ** 9
    with pytest.raises(Arret, match="1 Go exigés"):
        la.calculer(m.ctx, m.entrees, m.registre_bbis)
    assert (tmp_path / "travail" / "tenseurs").exists()                  # rien n'est supprimé
    arret = tmp_path / "sortie" / f"versement/{J.RUN}/calcul-interrompu/arret.json"
    verifier(arret)
    lu = json.loads(arret.read_text())
    assert "1 Go exigés" in lu["motif"] and lu["morceaux"]
    for morceau in lu["morceaux"]:
        verifier(arret.parent / morceau["fichier"])
    verifier(tmp_path / "sortie" / lu["travail"]["chemin"])


def test_refus_avant_le_depart_du_calcul_ne_verse_rien(tmp_path):
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    bbis, _ = J.ecrire_registres(tmp_path / "sans-verdict", m.sondes.sha_e2, verdict=False)
    with pytest.raises(Refus):
        la.calculer(m.ctx, m.entrees, bbis)
    assert not (tmp_path / "sortie" / "versement").exists()


def test_ligne_de_commande_du_calcul_n_imprime_pas_les_noms_des_tableaux(tmp_path, capsys, monkeypatch):
    rendu = {"tables": {}, "morceaux": [{"fichier": "x-000.npz", "sha256": "9" * 64, "tableaux": ["scores__P-S25__e0__sonde__q__publique"]}]}
    monkeypatch.setattr(la, "calculer", lambda *a, **k: rendu)
    monkeypatch.setattr(la, "Contexte", lambda *a, **k: None)
    assert la.principal(["calcul", "--travail", str(tmp_path / "t"), "--sortie", str(tmp_path / "s"), "--run", J.RUN,
                         "--registre-propre", str(tmp_path / "r.md"), "--entrees", str(tmp_path), "--registre-bbis",
                         str(tmp_path / "b.md")]) == 0
    sortie = capsys.readouterr().out
    assert "x-000.npz" in sortie and "scores__" not in sortie
