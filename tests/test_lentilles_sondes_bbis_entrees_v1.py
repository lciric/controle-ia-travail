"""Essais des entrées (texte scellé, « Code neuf », essais « entrées ») : chaque garde, un cas sain et un artefact (R5)."""
from __future__ import annotations

import json
import subprocess

import numpy as np
import pytest

pytest.importorskip("torch")

import lentilles_sondes_bbis_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import entrees_v1 as en  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, FormeMalComprise, Refus  # noqa: E402


def ouvrir(m):
    return en.ouvrir_entrees(m.racine, m.registre_bbis, m.registre_propre, J.LARGEUR)


def test_sain_vingt_sondes_forme_c(tmp_path):
    m = J.monde_entrees(tmp_path)
    e = ouvrir(m)
    assert len(e.sondes) == 20 and all(s.lue for s in e.sondes)
    for s in e.sondes:
        objet = m.objets[(s.cellule, s.pli, s.role)]
        assert np.array_equal(s.w, objet.w) and s.b == objet.b and s.empreinte == objet.empreinte()
        assert (s.q is not None) == (s.famille == "attention")
    assert e.sha256_e2 == m.sha_e2 and e.course.run == J.RUN_BBIS


# --- liste blanche --------------------------------------------------------------------------------------------------------------------
def test_liste_blanche_champs_permis(tmp_path):
    m = J.monde_entrees(tmp_path)
    vue = en.VueE2(m.doc)
    assert vue.champ("run_id") == J.RUN_BBIS
    assert vue.champ("sources", "P-S25", "e0", "famille") == "lineaire"
    assert vue.present("sources", "P-S25", "e0", "echec") is False
    assert vue.cles("sources") == sorted(K.CELLULES)


@pytest.mark.parametrize("chemin", [
    ("sources", "P-S25", "e0", "l2"), ("sources", "P-S25", "e0", "reglage"), ("sources", "P-S25", "e0", "taches_lues"),
    ("sources", "P-S25", "e0", "ordre2"), ("sources", "P-S25", "e0", "ordre2", "famille"),
    ("sources", "P-S25", "e0", "enc", "reglage"), ("sources", "P-S25", "e0", "enc", "echecs_internes"),
    ("sources", "P-S25", "e0", "echec"), ("sources", "P-S25", "e0", "enc", "echec"), ("sources", "P-S25", "e0", "enc"),
    ("fichiers_scores",), ("graines_derivees",), ("dispersion_ordres_calcul",), ("journal",), ("sources",), ("texte",)])
def test_liste_blanche_refuse_champ_exclu_valeur_d_echec_et_ordre2(tmp_path, chemin):
    m = J.monde_entrees(tmp_path, formes={("P-S25", "e0"): "c"})
    with pytest.raises(Refus):
        en.VueE2(m.doc).champ(*chemin)


def test_liste_blanche_presence_et_cles_refusees_hors_liste(tmp_path):
    vue = en.VueE2(J.monde_entrees(tmp_path).doc)
    with pytest.raises(Refus):
        vue.present("sources", "P-S25", "e0", "ordre2")
    with pytest.raises(Refus):
        vue.cles("sources", "P-S25", "e0")
    with pytest.raises(Refus):
        vue.cles("fichiers_scores")


def test_extrait_ne_porte_aucun_champ_exclu_ni_regularisation(tmp_path):
    m = J.monde_entrees(tmp_path, formes={("P-S25", "e1"): "a", ("P-S50", "e0"): "b"})
    texte = json.dumps(ouvrir(m).extrait, ensure_ascii=False)
    for interdit in ("l2", "0.001", "0.01", "taches_lues", "ordre2", "plis_internes", "noms_deux_premieres", "motif jamais lu",
                     "perte non finie", "reglage", "n_plancher", "journal"):
        assert interdit not in texte


# --- analyse de enc.reglage ------------------------------------------------------------------------------------------------------------
def test_reglage_du_lecteur_famille_et_couche_seules(tmp_path):
    doc = J.monde_entrees(tmp_path).doc
    doc["sources"]["P-S25"]["e0"]["enc"]["reglage"] = "attention-c15-l2_0.01"
    rendu = en.VueE2(doc).reglage_lecteur("P-S25", "e0")
    assert rendu == ("attention", 15) and "0.01" not in repr(rendu)


@pytest.mark.parametrize("chaine", ["attention-15-l2_0.01", "perceptron-c15-l2_0.01", "attention-c15", "c15-attention-l2_0.5", 15, None])
def test_reglage_mal_forme_arret_sans_imprimer_la_chaine(tmp_path, chaine):
    doc = J.monde_entrees(tmp_path).doc
    doc["sources"]["P-S25"]["e0"]["enc"]["reglage"] = chaine
    with pytest.raises(FormeMalComprise) as e:
        en.VueE2(doc).reglage_lecteur("P-S25", "e0")
    assert "forme mal comprise" in str(e.value) and "0.01" not in str(e.value) and "0.5" not in str(e.value)


# --- E-1 clé par clé -------------------------------------------------------------------------------------------------------------------
def test_e1_seules_les_entrees_sonde_et_enc_sont_decodees(tmp_path, monkeypatch):
    m = J.monde_entrees(tmp_path)
    lues = []
    original = np.lib.npyio.NpzFile.__getitem__
    monkeypatch.setattr(np.lib.npyio.NpzFile, "__getitem__", lambda self, cle: (lues.append(cle), original(self, cle))[1])
    e = ouvrir(m)
    assert lues and all("__sonde_" in n or "__enc_" in n for n in lues)
    assert not any("direction" in n for n in lues) and not any("direction" in n for n in e.entrees_decodees)
    assert any("direction0_w" in n for n in e.entrees_non_decodees) and any("direction1_b" in n for n in e.entrees_non_decodees)
    assert set(e.entrees_decodees) == set(lues)


def test_e1_demande_d_une_entree_direction_refus(tmp_path):
    m = J.monde_entrees(tmp_path)
    archive = en.ArchiveE1(m.e1)
    assert archive.lire("P-S25__e0__sonde_w").shape == (J.LARGEUR,)
    for nom in ("P-S25__e0__direction0_w", "P-S25__e0__direction1_b", "P-S25__e0__plancher_W"):
        with pytest.raises(Refus):
            archive.lire(nom)
    archive.fermer()


def test_e1_nom_d_entree_inconnu_arret(tmp_path):
    m = J.monde_entrees(tmp_path, modifier_archive=lambda t: t.update({"P-S25__e0__o2_w": np.zeros(3)}))
    with pytest.raises(FormeMalComprise, match="nom d'entrée inconnu"):
        ouvrir(m)


# --- ouverture avant VERDICT-BBIS et lignes de registre ---------------------------------------------------------------------------------
def test_refus_avant_verdict_bbis_sans_rien_ouvrir(tmp_path):
    bbis, propre = J.ecrire_registres(tmp_path / "registres", verdict=False)
    with pytest.raises(Refus, match="VERDICT-BBIS absente"):
        en.ouvrir_entrees(tmp_path / "dossier-qui-n-existe-pas", bbis, propre, J.LARGEUR)
    with pytest.raises(Refus, match="VERDICT-BBIS absente"):
        en.recuperer_entrees("url-jamais-contactee", tmp_path / "dest", bbis, propre)
    assert not (tmp_path / "dest").exists()


def test_scores_bbis_absente_ou_multiple_refus(tmp_path):
    for n, motif in ((0, "SCORES-BBIS absente"), (2, "plusieurs lignes")):
        bbis, propre = J.ecrire_registres(tmp_path / f"r{n}", scores=n)
        with pytest.raises(Refus, match=motif):
            en.ouvrir_entrees(tmp_path, bbis, propre, J.LARGEUR)


@pytest.mark.parametrize("manquante", K.CLES_EXIGEES_AVANT_TOUT)
def test_cle_du_registre_propre_absente_refus(tmp_path, manquante):
    presentes = tuple(c for c in K.CLES_EXIGEES_AVANT_TOUT if c != manquante)
    bbis, propre = J.ecrire_registres(tmp_path / "registres", propres=presentes)
    with pytest.raises(Refus, match=manquante):
        en.ouvrir_entrees(tmp_path, bbis, propre, J.LARGEUR)


def test_registres_seules_les_cles_nommees_sortent(tmp_path):
    bbis, _ = J.ecrire_registres(tmp_path / "registres")
    lignes = en.lignes_par_cle(bbis, ("SCORES-BBIS", "VERDICT-BBIS"))
    assert set(lignes) == {"SCORES-BBIS", "VERDICT-BBIS"}
    verdict = lignes["VERDICT-BBIS"][0]
    assert verdict.chemin is None and verdict.sha256 is None           # clé et heure seulement, jamais le fichier du verdict
    assert "LIGNE-JAMAIS-LUE" not in repr(lignes) and "secret" not in repr(lignes)
    with pytest.raises(Refus):
        en.lignes_par_cle(tmp_path / "registres" / "scellements-v1.md", ("SCORES-BBIS",))


# --- empreintes des sondes --------------------------------------------------------------------------------------------------------------
def test_poids_altere_arret(tmp_path):
    def alterer(t):
        t["P-S25__e0__sonde_w"] = t["P-S25__e0__sonde_w"].copy()
        t["P-S25__e0__sonde_w"][3] += 1e-9
    with pytest.raises(FormeMalComprise, match="empreinte recalculée de la sonde apprise"):
        ouvrir(J.monde_entrees(tmp_path, modifier_archive=alterer))


def test_nom_du_lecteur_honnete_mal_reconstruit_arret(tmp_path, monkeypatch):
    m = J.monde_entrees(tmp_path)
    assert len(ouvrir(m).sondes) == 20                                              # sain : nom « enc-<cellule>-e<k> »
    original = en.empreinte_sonde
    monkeypatch.setattr(en, "empreinte_sonde", lambda f, nom, *a: original(f, nom.replace("enc-", "ENC-"), *a))
    with pytest.raises(FormeMalComprise, match="lecteur honnête"):
        ouvrir(m)


def test_empreinte_recalculee_egale_celle_du_code_des_sondes(tmp_path):
    m = J.monde_entrees(tmp_path)
    for (cellule, pli, role), s in m.objets.items():
        assert en.empreinte_sonde(s.famille, s.nom, s.couche, s.agregation, s.w, s.b, s.q) == s.empreinte()


# --- couche, famille, agrégation hors de l'ensemble --------------------------------------------------------------------------------------
@pytest.mark.parametrize("champ,valeur,motif", [("couche", 8, "couche"), ("couche", True, "couche"), ("famille", "perceptron", "famille"),
                                                ("agregation", "attention", "agrégation"), ("agregation", "moyenne", "agrégation")])
def test_couche_famille_agregation_hors_de_l_ensemble_arret(tmp_path, champ, valeur, motif):
    def modifier(doc):
        doc["sources"]["P-S75"]["e0"][champ] = valeur
    with pytest.raises(FormeMalComprise, match=motif):
        ouvrir(J.monde_entrees(tmp_path, modifier=modifier))


def test_couche_du_lecteur_hors_de_l_ensemble_arret(tmp_path):
    def modifier(doc):
        doc["sources"]["P-S75"]["e0"]["enc"]["reglage"] = "lineaire-c9-l2_0.01"
    with pytest.raises(FormeMalComprise, match="couche"):
        ouvrir(J.monde_entrees(tmp_path, modifier=modifier))


def test_cellule_ou_pli_manquant_arret(tmp_path):
    with pytest.raises(FormeMalComprise, match="cellule"):
        ouvrir(J.monde_entrees(tmp_path / "a", modifier=lambda d: d["sources"].pop("P-S100")))
    with pytest.raises(FormeMalComprise, match="plis"):
        ouvrir(J.monde_entrees(tmp_path / "b", modifier=lambda d: d["sources"]["P-S100"].pop("e1")))


# --- chemins jamais ouverts ----------------------------------------------------------------------------------------------------------------
def test_ouvrir_un_fichier_de_scores_refus(tmp_path):
    permis = en.chemins_permis(J.RUN_BBIS)
    assert en.exiger_chemin_permis(permis["e1"], J.RUN_BBIS) == f"donnees/{J.RUN_BBIS}/sondes-bbis.npz"
    for chemin in (f"donnees/{J.RUN_BBIS}/scores-bbis-000.npz", f"donnees/{J.RUN_BBIS}/planchers-bbis-000.npz",
                   f"diag/{J.RUN_BBIS}/relecture-bbis.json", f"runs/{J.RUN_BBIS}/manifeste.json", f"diag/{J.RUN_BBIS}/lecture-bbis.json",
                   "diag/autre-course/sondes-bbis.json"):
        with pytest.raises(Refus):
            en.exiger_chemin_permis(chemin, J.RUN_BBIS)
        with pytest.raises(Refus):
            en._octets(tmp_path, chemin, J.RUN_BBIS)


# --- formes (a), (b), (c) -------------------------------------------------------------------------------------------------------------------
def test_forme_a_sonde_et_lecteur_non_lus_sans_arret(tmp_path):
    e = ouvrir(J.monde_entrees(tmp_path, formes={("P-S25", "e1"): "a"}))
    non_lues = {s.role: s for s in e.sondes if (s.cellule, s.pli) == ("P-S25", "e1")}
    assert not non_lues["sonde"].lue and non_lues["sonde"].motif == "échec à l'apprentissage"
    assert not non_lues["enc"].lue and non_lues["enc"].motif == "non appris, la sonde apprise ayant échoué"
    assert sum(s.lue for s in e.sondes) == 18 and "motif jamais lu" not in json.dumps(e.extrait)


def test_forme_b_lecteur_non_lu_sans_arret(tmp_path):
    e = ouvrir(J.monde_entrees(tmp_path, formes={("P-S50", "e0"): "b"}))
    paire = {s.role: s for s in e.sondes if (s.cellule, s.pli) == ("P-S50", "e0")}
    assert paire["sonde"].lue and not paire["enc"].lue and paire["enc"].motif == "échec à l'apprentissage"
    assert sum(s.lue for s in e.sondes) == 19


def test_artefact_enc_absent_sans_echec(tmp_path):
    with pytest.raises(FormeMalComprise, match="forme mal comprise"):
        ouvrir(J.monde_entrees(tmp_path, modifier=lambda d: d["sources"]["P-S75"]["e0"].pop("enc")))


def test_artefact_entree_enc_w_presente_alors_que_enc_echec_existe(tmp_path):
    def archive(t):
        t["P-S50__e0__enc_w"], t["P-S50__e0__enc_b"] = np.ones(J.LARGEUR), np.array([0.0])
    with pytest.raises(FormeMalComprise, match="enc.echec présente"):
        ouvrir(J.monde_entrees(tmp_path, formes={("P-S50", "e0"): "b"}, modifier_archive=archive))


def test_artefact_sonde_q_absente_pour_la_famille_attention(tmp_path):
    with pytest.raises(FormeMalComprise, match="sonde_q absente"):
        ouvrir(J.monde_entrees(tmp_path, modifier_archive=lambda t: t.pop("P-S50__e0__sonde_q")))


def test_artefacts_autres_combinaisons(tmp_path):
    def echec_avec_entrees(d):
        d["sources"]["P-S75"]["e0"]["echec"] = "motif"
    with pytest.raises(FormeMalComprise, match="clé echec présente"):
        ouvrir(J.monde_entrees(tmp_path / "a", modifier=echec_avec_entrees))
    with pytest.raises(FormeMalComprise, match="champ de la liste blanche absent"):
        ouvrir(J.monde_entrees(tmp_path / "b", modifier=lambda d: d["sources"]["P-S75"]["e0"].pop("nom_sonde")))
    with pytest.raises(FormeMalComprise, match="enc_q présente"):
        ouvrir(J.monde_entrees(tmp_path / "c", modifier_archive=lambda t: t.update({"P-S75__e0__enc_q": np.ones(J.LARGEUR)})))
    with pytest.raises(FormeMalComprise, match="enc_b absente"):
        ouvrir(J.monde_entrees(tmp_path / "d", modifier_archive=lambda t: t.pop("P-S75__e0__enc_b")))


# --- empreintes de E-1 et de E-2 contre leurs compagnons --------------------------------------------------------------------------------------
@pytest.mark.parametrize("quoi", ["e1", "e2"])
def test_un_octet_change_arret(tmp_path, quoi):
    m = J.monde_entrees(tmp_path)
    assert len(ouvrir(m).sondes) == 20
    p = getattr(m, quoi)
    octets = bytearray(p.read_bytes())
    octets[len(octets) // 2] ^= 1
    p.write_bytes(bytes(octets))
    with pytest.raises(Arret, match="R11"):
        ouvrir(m)


def test_e2_egal_a_son_compagnon_mais_pas_a_scores_bbis_arret(tmp_path):
    m = J.monde_entrees(tmp_path)
    bbis, _ = J.ecrire_registres(tmp_path / "autres", sha_e2="a" * 64)
    with pytest.raises(Arret, match="SCORES-BBIS"):
        en.ouvrir_entrees(m.racine, bbis, m.registre_propre, J.LARGEUR)


# --- récupération par clone partiel ------------------------------------------------------------------------------------------------------------
def test_recuperation_seuls_les_quatre_chemins_sont_telecharges(tmp_path):
    m = J.monde_entrees(tmp_path)
    (m.racine / "donnees" / J.RUN_BBIS / "scores-bbis-000.npz").write_bytes(b"scores jamais telecharges" * 100)
    (m.racine / "diag" / J.RUN_BBIS / "relecture-bbis.json").write_text('{"jamais": "lu"}')
    J._git(["init", "-q", "-b", en.BRANCHE_DONNEES], m.racine)
    J._git(["add", "-A"], m.racine)
    J._git(["commit", "-q", "-m", "donnees jouets"], m.racine)
    subprocess.run(["git", "config", "uploadpack.allowFilter", "true"], cwd=m.racine, check=True)
    subprocess.run(["git", "config", "uploadpack.allowAnySHA1InWant", "true"], cwd=m.racine, check=True)
    dest = en.recuperer_entrees(f"file://{m.racine}", tmp_path / "recupere", m.registre_bbis, m.registre_propre)
    assert len(en.ouvrir_entrees(dest, m.registre_bbis, m.registre_propre, J.LARGEUR).sondes) == 20
    assert not list(dest.glob("**/scores-bbis-*")) or all("clone" in str(p) for p in dest.glob("**/scores-bbis-*"))
    manquants = subprocess.run(["git", "rev-list", "--objects", "--missing=print", "HEAD"], cwd=dest / "clone-sans-contenus",
                               capture_output=True, text=True).stdout
    absents = [l[1:] for l in manquants.splitlines() if l.startswith("?")]
    scores = subprocess.run(["git", "rev-parse", f"HEAD:donnees/{J.RUN_BBIS}/scores-bbis-000.npz"], cwd=m.racine,
                            capture_output=True, text=True).stdout.strip()
    relecture = subprocess.run(["git", "rev-parse", f"HEAD:diag/{J.RUN_BBIS}/relecture-bbis.json"], cwd=m.racine,
                               capture_output=True, text=True).stdout.strip()
    assert scores in absents and relecture in absents                 # jamais téléchargés : absents du clone partiel
