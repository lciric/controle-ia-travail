"""Essais ajoutés après la contre-lecture du code (rapport `contre-lecture-code-lentille-publique-v1.md`, § 2 et § 7) : un
artefact pour chaque garde réelle qu'aucun essai ne voyait, dont le libellé des pôles après repli (bloquant), et les essais
des ajouts de la version 2 (essai hors ligne du tokeniseur, fiche des entrées, renvoi au montage, note des pôles)."""
from __future__ import annotations

import json
import struct
from collections import namedtuple

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v3 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import entrees_v2 as en  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v3 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v2 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, FormeMalComprise  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

Disque = namedtuple("Disque", "total used free")


# --- libellé des pôles après repli (bloquant) ----------------------------------------------------------------------------------------
def _direction_apres_repli(p_par_direction: float, p_remplacee: float, p_signes: float) -> tuple[dict, dict]:
    def nul(p):
        return {"p_concentration": p, "p_part": p, "familles": {}}
    signes = {s: {"premiers_par_score": {"ids": [5, 6]}, "familles": {},
                  "nuls": {K.NUL_ISOTROPE: nul(0.5) | {"remplacee": True}, K.NUL_ISOTROPE_PAR_DIRECTION: nul(0.5),
                           K.NUL_SIGNES: nul(0.5)}} for s in ("+", "-")}
    d = {"sonde": "P-S75/e1/sonde", "role": "sonde", "vecteur": "w", "couche": 7,
         "lectures": {l: {"signes": json.loads(json.dumps(signes))} for l in K.LENTILLES},
         "poles": {"p": {K.NUL_ISOTROPE + "_remplacee": p_remplacee, K.NUL_ISOTROPE_PAR_DIRECTION: p_par_direction,
                         K.NUL_SIGNES: p_signes}}}
    tenue = {"tenue": True}
    couches = {"7": {"repli_nuls_par_direction": True, "lentilles": {l: {"calibration": {
        K.NUL_ISOTROPE: tenue, K.NUL_ISOTROPE_PAR_DIRECTION: tenue, K.NUL_SIGNES: tenue}} for l in K.LENTILLES}}}
    return d, couches


@pytest.mark.parametrize("p_par_direction,p_remplacee,attendu", [
    (0.0005, 0.9, st.LIBELLE_CONCENTREE),          # le nul refait par direction décide, non le nul partagé « remplacé »
    (0.9, 0.0005, st.LIBELLE_NON_DISTINCTE),
    (0.02, 0.0005, st.LIBELLE_INTERMEDIAIRE)])
def test_libelle_des_poles_apres_repli_pris_au_nul_refait_par_direction(p_par_direction, p_remplacee, attendu):
    d, couches = _direction_apres_repli(p_par_direction, p_remplacee, 0.0005)
    la._etiqueter([d], couches, ["a", "b"], np.array([5, 6]))
    assert d["poles"]["libelle"] == attendu and d["poles"]["nul_isotrope_en_vigueur"] == K.NUL_ISOTROPE_PAR_DIRECTION
    assert st.libelle(p_remplacee, 0.0005) != attendu          # l'artefact (valeur du nul remplacé) donnerait un autre libellé


def test_libelle_des_poles_sans_repli_pris_au_nul_partage():
    d, couches = _direction_apres_repli(0.9, 0.9, 0.0005)
    d["poles"]["p"] = {K.NUL_ISOTROPE: 0.0005, K.NUL_SIGNES: 0.0005}
    couches["7"]["repli_nuls_par_direction"] = False
    for l in K.LENTILLES:
        for t in d["lectures"][l]["signes"].values():
            del t["nuls"][K.NUL_ISOTROPE_PAR_DIRECTION], t["nuls"][K.NUL_ISOTROPE]["remplacee"]
    la._etiqueter([d], couches, ["a", "b"], np.array([5, 6]))
    assert d["poles"]["libelle"] == st.LIBELLE_CONCENTREE and d["poles"]["nul_isotrope_en_vigueur"] == K.NUL_ISOTROPE


def test_bout_en_bout_poles_apres_repli_libelle_egal_a_la_regle_sur_les_p_en_vigueur(tmp_path):
    m = J.monde(tmp_path, echelles={("P-S75", "e1", "sonde"): 1e-5})
    la.monter(m.ctx)
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis)
    tables = json.loads((tmp_path / "sortie" / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    vus = 0
    for d in tables["directions"]:
        p = d["poles"]["p"]
        if d["couche"] == 7:
            vus += 1
            assert set(p) == {K.NUL_ISOTROPE + "_remplacee", K.NUL_ISOTROPE_PAR_DIRECTION, K.NUL_SIGNES}
            assert d["poles"]["libelle"] == st.libelle(p[K.NUL_ISOTROPE_PAR_DIRECTION], p[K.NUL_SIGNES])
            assert all(K.NUL_ISOTROPE_PAR_DIRECTION in x["rang_parmi_maxima_nuls"] for x in d["poles"]["poles"])
        else:
            assert d["poles"]["libelle"] == st.libelle(p[K.NUL_ISOTROPE], p[K.NUL_SIGNES])
    assert vus >= 4
    # ajouts de la version 2 : fiche fermée des entrées, renvoi au rapport du montage, ligne proposée
    fiche = tmp_path / "sortie" / "diag" / J.RUN / "entrees-lentilles-bbis.json"
    contenu = json.loads(fiche.read_text(encoding="utf-8"))
    assert contenu["e1"]["sha256"] == J.sha(m.sondes.e1.read_bytes()) and contenu["e2"]["sha256"] == m.sondes.sha_e2
    assert contenu["empreinte_de_l_extrait_de_la_liste_blanche"] == rendu["empreinte_extrait"]
    assert rendu["lignes_proposees"][0] == la.ligne_registre(
        "ENTREES-LENTILLES-BBIS", f"diag/{J.RUN}/entrees-lentilles-bbis.json", verifier(fiche),
        rendu["lignes_proposees"][0].split(" | ")[1])
    manifeste = json.loads((tmp_path / "sortie" / "runs" / J.RUN / "manifeste.json").read_text(encoding="utf-8"))
    assert manifeste["rapport_du_montage"]["sha256"] == verifier(tmp_path / "sortie" / "diag" / J.RUN / "montage-lentilles-bbis.json")
    assert manifeste["entrees_sha256"] == verifier(fiche)


# --- entrées : forme de `…_b` ------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("valeur", [np.array([0.1, 0.2]), np.array(0.1), np.array([[0.1]]), np.array([1])])
def test_biais_d_une_autre_forme_qu_un_tableau_d_un_element_arret(tmp_path, valeur):
    m = J.monde_entrees(tmp_path, modifier_archive=lambda t: t.update({"P-S75__e0__sonde_b": valeur}))
    with pytest.raises(FormeMalComprise, match="tableau d'un élément"):
        en.ouvrir_entrees(m.racine, m.registre_bbis, m.registre_propre, J.LARGEUR)


# --- montage : longueur de l'essai d'un octet, commit du voisin, tailles des tenseurs, jetons gardés ----------------------------------------
def test_essai_d_un_octet_d_une_autre_longueur_arret():
    class Bavard(J.TransportSimule):
        def octets(self, url, cle=None, debut=None, fin=None):
            return self.fichiers[url]                              # ignore l'intervalle demandé
    t = Bavard({"u": b"ab", "vide": b""})
    with pytest.raises(Arret, match="2 octet"):
        mo.essais_un_octet(t, mo.Cle(J.FAUSSE_CLE), [mo.Cible("fichier", "u")])
    with pytest.raises(Arret, match="0 octet"):
        mo.essais_un_octet(t, mo.Cle(J.FAUSSE_CLE), [mo.Cible("dépôt", "vide", sorte="en-tête")])
    assert mo.essais_un_octet(t, mo.Cle(J.FAUSSE_CLE), [mo.Cible("dépôt", "u", sorte="en-tête")])[0]["octets"] == 2


def test_voisin_extrait_par_un_nom_de_branche_et_non_par_le_commit_arret(tmp_path):
    v = J.construire_voisin(tmp_path)
    with pytest.raises(Arret, match="au lieu de main"):            # l'extraction réussit, mais HEAD n'est pas la chaîne demandée
        mo.cloner_voisin(tmp_path / "voisin", v.url, "main")


def test_tenseur_extrait_d_une_autre_taille_que_son_en_tete_arret(tmp_path):
    """Faux fichier dont l'en-tête annonce 100 octets pour un tenseur et qui n'en porte que 50 : taille et SHA-256 du flux
    sont ceux attendus, seule la taille du tenseur extrait trahit le fichier."""
    def fichier(annonce: int, portes: int) -> bytes:
        en_tete = json.dumps({"t": {"dtype": "F32", "shape": [annonce // 4], "data_offsets": [0, annonce]}}).encode()
        return struct.pack("<Q", len(en_tete)) + en_tete + bytes(portes)
    sain, faux = fichier(100, 100), fichier(100, 50)
    d = mo.lire_poids_en_flux(J.TransportSimule({"u": sain}), "u", None, ("t",), tmp_path / "sain", len(sain), J.sha(sain))
    assert d["t"]["octets"] == 100 and (tmp_path / "sain" / "t.brut").stat().st_size == 100
    with pytest.raises(Arret, match="taille ou SHA-256"):
        mo.lire_poids_en_flux(J.TransportSimule({"u": faux}), "u", None, ("t",), tmp_path / "faux", len(faux), J.sha(faux))
    assert not list((tmp_path / "faux").glob("*.brut"))


@pytest.mark.parametrize("script,motif", [
    ("import json, sys\njson.dump({'modele': 'Qwen/Qwen3-8B', 'ids': [1], 'chaines': ['a']}, open(sys.argv[1], 'x'))\n", "modèle ou longueurs"),
    ("import json, sys\njson.dump({'modele': '%s', 'ids': [1, 2], 'chaines': ['a']}, open(sys.argv[1], 'x'))\n" % K.DEPOT_LLAMA,
     "modèle ou longueurs")])
def test_jetons_gardes_d_un_autre_modele_ou_de_longueurs_inegales_arret(tmp_path, monkeypatch, script, motif):
    v = J.construire_voisin(tmp_path)
    mo.cloner_voisin(tmp_path / "voisin", v.url, v.commit)
    mo.appliquer_correctifs(tmp_path / "voisin", v.depot, v.correctifs)
    (tmp_path / "travail").mkdir()
    monkeypatch.setattr(mo, "SCRIPT_JETONS", script)
    with pytest.raises(Arret, match=motif):
        mo.calculer_jetons_gardes(tmp_path / "voisin", tmp_path / "hf", tmp_path / "travail", env={})


def test_w_u_d_une_autre_precision_arret():
    g = torch.Generator().manual_seed(0)
    v, gamma, wu = torch.randn(16, 2, generator=g), torch.ones(16), torch.randn(30, 16, generator=g)
    le.lire(v, None, gamma, wu)
    for autre in (wu.double(), wu.half()):
        with pytest.raises(Arret, match="simple précision"):
            le.lire(v, None, gamma, autre)


# --- procédure : dossiers existants (R12), montage absent, disque à chaque direction, clé écrite au montage ---------------------------------
def test_montage_dossier_de_travail_deja_existant_refus(tmp_path):
    m = J.monde(tmp_path)
    (tmp_path / "travail").mkdir()
    (tmp_path / "travail" / "reste-d-une-autre-course.txt").write_text("à garder")
    with pytest.raises(Arret, match="existe déjà"):
        la.monter(m.ctx)
    assert m.transport.appels == [] and (tmp_path / "travail" / "reste-d-une-autre-course.txt").read_text() == "à garder"


@pytest.fixture()
def monte(tmp_path):
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    return m


@pytest.mark.parametrize("relatif", ["diag/{run}/tables-lentilles-bbis.json", "runs/{run}/manifeste.json",
                                     "diag/{run}/entrees-lentilles-bbis.json"])
def test_calcul_sortie_deja_existante_refus(monte, relatif):
    p = monte.tmp / "sortie" / relatif.format(run=J.RUN)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("déjà là")
    with pytest.raises(Arret, match="existe déjà"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)
    assert p.read_text() == "déjà là" and (monte.tmp / "travail" / "tenseurs").exists()


def test_calcul_etat_du_montage_absent_arret(monte):
    (monte.tmp / "travail" / "etat-montage.json").unlink()             # la marque du dossier est là, le montage non
    with pytest.raises(Arret, match="montage absent"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)


def test_calcul_disque_controle_a_chaque_direction(monte):
    """Assez d'espace au départ du calcul, plus assez ensuite : l'arrêt vient du contrôle joué à chaque direction."""
    appels = []

    def mesure(chemin):
        appels.append(chemin)
        return Disque(0, 0, 10 ** 10 if len(appels) <= 3 else 10 ** 9 - 1)
    monte.reglages.disque_calcul = K.DISQUE_CALCUL_OCTETS
    monte.ctx.mesure_disque = mesure
    with pytest.raises(Arret, match="pendant le calcul"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)
    assert len(appels) == 4
    assert (monte.tmp / "travail" / "tenseurs").exists()                # rien n'est supprimé
    arret = monte.tmp / "sortie" / "versement" / J.RUN / "calcul-interrompu" / "arret.json"
    assert "pendant le calcul" in json.loads(arret.read_text(encoding="utf-8"))["motif"] and verifier(arret)


def test_montage_cle_ecrite_dans_un_fichier_arret(tmp_path, monkeypatch):
    """Artefact : une valeur relevée au montage porte la clé ; la recherche dans les fichiers écrits arrête."""
    m = J.monde(tmp_path)
    monkeypatch.setattr(la, "_versions", lambda: {"python": "3", "fuite": J.FAUSSE_CLE})
    with pytest.raises(Arret, match="clé d'accès écrite dans un fichier") as e:
        la.monter(m.ctx)
    assert J.FAUSSE_CLE not in str(e.value)


# --- ajouts de la version 2 ------------------------------------------------------------------------------------------------------------
def test_essai_du_tokeniseur_hors_ligne_sain_avant_tout_flux_et_sans_cle(tmp_path, monkeypatch):
    m = J.monde(tmp_path)
    flux_avant_l_essai = []
    original = la.essayer_tokeniseur_du_cache

    def espion(ctx, voisin, hf_home):
        flux_avant_l_essai.append(sum(a[0] == "flux" for a in m.transport.appels))
        return original(ctx, voisin, hf_home)
    monkeypatch.setattr(la, "essayer_tokeniseur_du_cache", espion)
    la.monter(m.ctx)
    assert flux_avant_l_essai == [0]
    rapport = json.loads((tmp_path / "sortie" / "diag" / J.RUN / "montage-lentilles-bbis.json").read_text(encoding="utf-8"))
    assert rapport["essai_du_tokeniseur_hors_ligne"]["tenu"] is True and (tmp_path / "travail" / "journal-essai-tokeniseur.txt").is_file()


def test_essai_du_tokeniseur_en_echec_arret_avant_tout_flux(tmp_path, monkeypatch):
    m = J.monde(tmp_path)
    monkeypatch.setattr(la, "SCRIPT_TOKENISEUR", "import os\nassert os.environ.get('HF_HUB_OFFLINE') == '1'\n"
                                                 "assert 'HF_TOKEN' not in os.environ\nraise SystemExit('dépôt à porte')\n")
    with pytest.raises(Arret, match="ne lit pas le tokeniseur du cache posé") as e:
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)
    journal = (tmp_path / "travail" / "journal-essai-tokeniseur.txt").read_text()
    assert "dépôt à porte" in journal and "AssertionError" not in journal and J.FAUSSE_CLE not in str(e.value)


def test_note_explicite_pour_les_poles_intermediaires():
    def table(libelle):
        return {"independance_a_la_norme_non_tenue": [], "sondes": [], "comparaisons": [], "directions": [{
            "sonde": "P-S25/e0/sonde", "cellule": "P-S25", "pli": "e0", "role": "sonde", "vecteur": "w", "couche": 15, "lectures": {},
            "poles": {"libelle": libelle, "nul_isotrope_en_vigueur": K.NUL_ISOTROPE, "p": {K.NUL_ISOTROPE: 0.02, K.NUL_SIGNES: 0.03},
                      "poles": [{"neurone": 1, "signe": "+", "cosinus": 0.2, "lecture_publique": {"chaines_echappees": [" a"]}}]}}]}
    inter = la.rendre_phrases(table(st.LIBELLE_INTERMEDIAIRE))["directions"][0]
    assert inter["phrases"] == [] and inter["note"] == "pôles intermédiaires : aucune phrase gelée ; valeurs en table"
    for libelle in (st.LIBELLE_CONCENTREE, st.LIBELLE_NON_DISTINCTE):
        ligne = la.rendre_phrases(table(libelle))["directions"][0]
        assert len(ligne["phrases"]) == 1 and "note" not in ligne
