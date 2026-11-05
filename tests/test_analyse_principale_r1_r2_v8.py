"""Analyse principale de R1-R2, code v8 (addendum 1 « gardes des analyses », relance v4 de R1, après la contre-lecture
1 : K1, K2) : essais R5 sur données **synthétiques** (générateur, écrivains et pièces jouets des essais v1 et v6) —
jamais les vraies données de R1 ni de R2. Éprouvés, sur un cas sain et un artefact chacun : les trois gardes de réception
(`texte`, `table-comparee`, `provenance`, lues par `entrees_v5` sur les constantes v8) ; **K1** : aucun `.npz` ouvert
avant les gardes (`numpy.load` remplacé par un piège : l'artefact arrête sans qu'il soit appelé, le cas sain l'appelle
seulement après les gardes) ; même calcul et même issue que le code v2 à entropie égale ; rejeu non validé ; **K2** :
liste close des passages tolérés (les trois manifestes de la course v3, run et empreinte gelés ; commandes sœurs sous
l'addendum), quatrième manifeste qui cite le texte → arrêt, manifeste toléré à l'empreinte altérée → arrêt, commande
inconnue sous l'addendum → arrêt, manifeste illisible → arrêt, second passage → arrêt, arrêt distinct
(`PassageHorsListe`, code de fin 2) qui nomme le manifeste ; liste fermée v8 et constantes v8 (empreintes des trois
manifestes réels de la course v3, lues sur `runs/` du dépôt, manifestes seuls)."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.analyse_blanche_noire import constantes_v5 as C5
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v2 as K2
from controle_ia.analyse_principale_r1_r2 import constantes_v5 as K5
from controle_ia.analyse_principale_r1_r2 import constantes_v6 as K6
from controle_ia.analyse_principale_r1_r2 import constantes_v8 as K8
from controle_ia.analyse_principale_r1_r2 import constantes_v9 as K9
from controle_ia.analyse_principale_r1_r2 import entrees_v5 as EN5
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as LP
from controle_ia.analyse_principale_r1_r2 import lecture_v2 as LP2
from controle_ia.analyse_principale_r1_r2 import lecture_v6 as LP6
from controle_ia.analyse_principale_r1_r2 import lecture_v8 as LP8
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, graines
from controle_ia.scellement import empreinte, sceller
from test_analyse_principale_r1_r2_v1 import D, RUN, _donnees, _ecrire_juge, _ecrire_p3
from test_analyse_principale_r1_r2_v1 import _npz  # noqa: F401  (gardé : les écrivains v6 l'emploient)
from test_analyse_principale_r1_r2_v6 import ADDENDUM_R1, RUN_REJEU, _bloc, _ecrire_r1_v4, _fiche, _pieces_v4, _texte_jouet

RACINE = Path(__file__).resolve().parents[1]
PASSAGES_V3_ATTENDUS = {
    "20261103-072723-analyse-principale-r1-r2-v1": "0587c398cc05f279251bbe747c3deaff1dee29cb191c94ce30090ce50a5e4643",
    "20261103-072805-analyse-par-episode-v1": "79f2a758e0c36f1d4aaa54a78e039ffc802074fe03e222120aff81a78f1a2083",
    "20261103-072840-analyse-blanche-noire-v3": "91f711c6eb903ca470b972a953ac12cdde31f211412a5629725895537d550adf",
}


@pytest.fixture(autouse=True)
def constantes_reduites(monkeypatch):
    for nom, v in (("DIMENSION", D), ("TIRAGES", 300), ("N_PLANCHER", 50), ("RUN_P3", RUN)):
        monkeypatch.setattr(K, nom, v)


def _addendum_jouet(depot, chemin=K8.ADDENDUM, fichiers=None, alterer=False, constantes=None, blocs=()) -> str:
    fichiers = LP8.FICHIERS_PAQUET + LP8.FICHIERS_ESSAIS + LP8.FICHIERS_REUTILISES if fichiers is None else fichiers
    c = K8.empreinte_constantes() if constantes is None else constantes
    return _texte_jouet(depot, chemin, f"Empreinte des constantes (analyse principale, code v8) : `{c}`",
                        _bloc(K8.TITRE_LISTE, fichiers, alterer), *blocs)


def _source_v8(depot, monkeypatch, d, r1=True, r2=True, j8=True, fiche="fiche.json", r1_kw=None, j3_kw=None):
    """Comme `_source_v4` des essais v6, les pièces de la relance v4 étant liées aux constantes v8 (`entrees_v5`)."""
    sha = _ecrire_p3(depot, d)
    monkeypatch.setattr(K, "EMPREINTES_P3", sha)
    from controle_ia.analyse_principale_r1_r2 import entrees_v1 as EN
    monkeypatch.setattr(K, "IDENTITE_SHA256", EN.empreinte_identite(d["tables"]))
    pieces = _pieces_v4(depot, monkeypatch, module=K8)
    f = {"format": K.FORMAT_FICHE, "redaction": "essai synthétique", "R1": None, "motif_R1": None, "R2": None,
         "motif_R2": None}
    if r1:
        f["R1"] = _ecrire_r1_v4(depot, d, sha["textes"], pieces["table"], **(r1_kw or {}))
    else:
        f["motif_R1"] = "rejeu_non_conforme"
    if r2:
        f["R2"] = {"juge3b": _ecrire_juge(depot, d, "J3", **(j3_kw or {})),
                   "juge8b": _ecrire_juge(depot, d, "J8") if j8 else None, "motif_juge8b": None if j8 else "non_livre"}
    else:
        f["motif_R2"] = "sorties_non_livrees"
    _fiche(depot, f, fiche)
    return f, pieces


def _piege_npz(monkeypatch, module_lecture):
    """`numpy.load` remplacé par un piège (K1) : il lève tant que `exiger_reception_v4` du module n'a pas rendu ; il
    compte ses appels. `exiger_reception_v4` est enveloppée pour poser le drapeau après son succès."""
    etat = {"garde_faite": False, "appels_npz": 0, "appels_npz_avant_garde": 0}
    vrai_load = np.load
    garde = module_lecture.exiger_reception_v4

    def piege(*a, **k):
        if not etat["garde_faite"]:
            etat["appels_npz_avant_garde"] += 1
            raise AssertionError("K1 : numpy.load appelé avant les gardes de réception")
        etat["appels_npz"] += 1
        return vrai_load(*a, **k)

    def garde_enveloppee(*a, **k):
        r = garde(*a, **k)
        etat["garde_faite"] = True
        return r
    monkeypatch.setattr(np, "load", piege)
    monkeypatch.setattr(module_lecture, "exiger_reception_v4", garde_enveloppee)
    return etat


def _manifeste_v3_jouet(depot, run, prereg_rel, commande, config=None):
    """Manifeste décisif jouet d'un passage de la course v3 ; rend l'empreinte sha256 de ses octets."""
    creer_manifeste(depot, run, config or {"mode": "jouet"}, ["x"], entropie=1, decisif=True,
                    prereg=depot / prereg_rel, commande=commande, autoriser_depot_sale=True)
    return hashlib.sha256((depot / "runs" / run / "manifeste.json").read_bytes()).hexdigest()


# ------------------------------------------------------------------------------------------------ constantes, liste fermée
def test_constantes_v8_gelees_liste_close_et_bloc_de_l_addendum():
    assert K8.ADDENDUM_V4 == K6.ADDENDUM_V4 == {"chemin": "prereg/R1-addendum-relance-v4.md",
                                                "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"}
    assert K8.TEXTE == {"chemin": "prereg/analyse-principale-r1-r2-v1.md",
                        "sha256": "8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537"}
    assert empreinte(RACINE / K8.TEXTE["chemin"]) == K8.TEXTE["sha256"]                 # texte scellé, inchangé
    assert (K8.COMMANDE_REJEU_V4, K8.TABLE_V4, K8.RESULTAT_REPARATION_V4, K8.ADDENDUM) == (
        K6.COMMANDE_REJEU_V4, K6.TABLE_V4, K6.RESULTAT_REPARATION_V4, K6.ADDENDUM)
    assert K8.VERSION == "analyse-principale-r1-r2-v1 (code v8)" and K8.TITRE_LISTE.endswith("(code v8)")
    assert K8.COMMANDE == "python -m controle_ia.analyse_principale_r1_r2.lecture_v8"
    # K2 : liste close gelée = les trois manifestes de la course v3, empreintes lues sur `runs/` du dépôt (manifestes seuls)
    assert K8.PASSAGES_V3 == PASSAGES_V3_ATTENDUS
    for run, sha in K8.PASSAGES_V3.items():
        assert empreinte(RACINE / "runs" / run / "manifeste.json") == sha, run
    assert K8.COMMANDES_ADDENDUM == (K8.COMMANDE, K9.COMMANDE, C5.COMMANDE) and len(set(K8.COMMANDES_ADDENDUM)) == 3
    assert C5.PASSAGES_V3 == K8.PASSAGES_V3 and C5.COMMANDES_ADDENDUM == K8.COMMANDES_ADDENDUM
    assert "PASSAGES_V3" in K8.constantes_courantes()["v8"] and "COMMANDES_ADDENDUM" in K8.constantes_courantes()["v8"]
    assert K8.NOM_SORTIE == K2.NOM_SORTIE and LP8.issue is LP2.issue
    assert K8.empreinte_constantes() not in (K2.empreinte_constantes(), K6.empreinte_constantes())
    assert K8.constantes_courantes()["v1_v2"] == K2.constantes_courantes()
    for c in LP8.FICHIERS_PAQUET + LP8.FICHIERS_ESSAIS + LP8.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LP2.FICHIERS_PAQUET) < set(LP8.FICHIERS_PAQUET) and set(LP2.FICHIERS_ESSAIS) < set(LP8.FICHIERS_ESSAIS)
    assert not any("_v6" in c or "entrees_v4" in c for c in LP8.FICHIERS_PAQUET + LP8.FICHIERS_ESSAIS)   # v6 remplacé
    assert len(set(LP8.FICHIERS_PAQUET) | set(LP8.FICHIERS_ESSAIS) | set(LP8.FICHIERS_REUTILISES)) == 22
    assert issubclass(LP8.PassageHorsListe, GardeArret) and LP8.CODE_FIN_PASSAGE == 2
    with pytest.raises(GardeArret, match="titre"):
        LP8.exiger_code_cite("rien")
    with pytest.raises(GardeArret, match="liste fermée"):                               # bloc présent, liste v6 seulement
        LP8.exiger_code_cite("\n\n".join(["# t", _bloc(K8.TITRE_LISTE, LP6.FICHIERS_PAQUET + LP6.FICHIERS_ESSAIS
                                                      + LP6.FICHIERS_REUTILISES)]))
    texte = "\n\n".join(["# t", _bloc(K6.TITRE_LISTE, LP6.FICHIERS_PAQUET), K8.TITRE_LISTE, f"- `src/a.py` : `{'1' * 64}`",
                         "## Hypothèse", "h"])
    bloc = LP8.liste_fermee_de(texte, K8.TITRE_LISTE)                                   # bloc propre à l'analyse
    assert "src/a.py" in bloc and "lecture_v6" not in bloc and "Hypothèse" not in bloc


# ------------------------------------------------------------------------------------------------ gardes de réception (v5)
def test_reception_v5_cas_sain_et_artefacts(depot, monkeypatch):
    d = _donnees(21)
    f, pieces = _source_v8(depot, monkeypatch, d)
    sha_t = K.EMPREINTES_P3["textes"]
    r = EN5.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])                   # cas sain
    assert r["table"]["sha256"] == pieces["table"] and r["reparation"]["sha256"] == pieces["reparation"]
    assert r["texte"] == K8.ADDENDUM_V4 and r["commande"] == K8.COMMANDE_REJEU_V4 and r["run_rejeu"] == RUN_REJEU
    _texte_jouet(depot, "prereg/R1-addendum-relance-v3.md", "addendum v3 jouet de R1")
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-a", prereg_run="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="garde texte"):                                # texte : autre texte qui gouverne
        EN5.exiger_reception_v4(depot, e["resultat"]["chemin"])
    with monkeypatch.context() as mp:
        mp.setattr(K8, "ADDENDUM_V4", dict(K8.ADDENDUM_V4, sha256="0" * 64))           # même chemin, autre empreinte
        with pytest.raises(GardeArret, match="garde texte"):
            EN5.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-b", table_sha_tok="0" * 64)
    with pytest.raises(GardeArret, match="table_sha256"):                               # table-comparee
        EN5.exiger_reception_v4(depot, e["resultat"]["chemin"])
    rep = depot / K8.RESULTAT_REPARATION_V4
    comp = Path(str(rep) + ".sha256")
    octets, sceau = rep.read_bytes(), comp.read_text(encoding="utf-8")
    comp.unlink()
    rep.write_bytes(octets + b"\n")
    sceller(rep)
    with pytest.raises(GardeArret, match="resultat_reparation_sha256"):                # table qui cite un autre résultat
        EN5.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])
    rep.write_bytes(octets)
    comp.write_text(sceau, encoding="utf-8")
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-c", addendum_tok="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="tokenisation.addendum"):                     # provenance
        EN5.exiger_reception_v4(depot, e["resultat"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-d",
                      commande="python -m controle_ia.runs_nuit.rejeu_activations_v3")
    with pytest.raises(GardeArret, match="commande du manifeste"):
        EN5.exiger_reception_v4(depot, e["resultat"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-e", tokenisation=False)
    with pytest.raises(GardeArret, match="sans clé tokenisation"):
        EN5.exiger_reception_v4(depot, e["resultat"]["chemin"])


# ------------------------------------------------------------------------------------------------ K1, bout en bout
def test_k1_aucun_npz_avant_les_gardes_meme_calcul_que_v2_et_rejeu_non_valide(depot, monkeypatch):
    d = _donnees(22, w=3.0, j=0.5)
    f, pieces = _source_v8(depot, monkeypatch, d)
    _fiche(depot, dict(f, R1=_ecrire_r1_v4(depot, d, K.EMPREINTES_P3["textes"], pieces["table"], run=RUN_REJEU + "-p",
                                           addendum_tok="prereg/R1-addendum-relance-v3.md")), "fiche-p.json")
    with pytest.raises(GardeArret, match="entropie explicite"):
        LP8.analyser(depot, "fiche.json", "20261105-030000-x", None, autoriser_depot_sale=True)
    # artefact (K1) : provenance fausse → la garde arrête ; le piège sur numpy.load n'a jamais été appelé ; rien d'écrit
    with monkeypatch.context() as mp:
        etat = _piege_npz(mp, LP8)
        with pytest.raises(GardeArret, match="garde provenance"):
            LP8.analyser(depot, "fiche-p.json", "20261105-030003-x", None, entropie=K.entropie_racine(),
                         autoriser_depot_sale=True)
        assert etat == {"garde_faite": False, "appels_npz": 0, "appels_npz_avant_garde": 0}
        assert not (depot / "runs" / "20261105-030003-x").exists()
    # cas sain (K1) : les gardes rendent, puis seulement les chargeurs ouvrent les .npz
    with monkeypatch.context() as mp:
        etat = _piege_npz(mp, LP8)
        r8 = LP8.analyser(depot, "fiche.json", "20261105-030001-v8", None, entropie=K.entropie_racine(),
                          autoriser_depot_sale=True)
        assert etat["garde_faite"] and etat["appels_npz"] > 0 and etat["appels_npz_avant_garde"] == 0
    r2 = LP2.analyser(depot, "fiche.json", "20261105-030002-v2", None, entropie=K.entropie_racine(),
                      autoriser_depot_sale=True)
    assert r8["calcul"] == r2["calcul"] and r8["issue"] == r2["issue"] and r8["version"] == K8.VERSION
    assert r8["reception_v4"]["table"]["sha256"] == pieces["table"] and r8["reception_v4"]["run_rejeu"] == RUN_REJEU
    corps = json.loads((depot / "diag" / "20261105-030001-v8" / f"{K8.NOM_SORTIE}.json").read_text(encoding="utf-8"))
    assert corps["resultat"]["reception_v4"] == r8["reception_v4"]
    assert (depot / "diag" / "20261105-030001-v8" / f"{K8.NOM_SORTIE}.md.sha256").exists()
    man = json.loads((depot / "runs" / "20261105-030001-v8" / "manifeste.json").read_text(encoding="utf-8"))
    assert man["commande"] == K8.COMMANDE and man["config"]["addendum"] is None and not man["decisif"]
    assert man["config"]["constantes_sha256"] == K8.empreinte_constantes()
    assert man["config"]["constantes"]["v8"]["PASSAGES_V3"] == PASSAGES_V3_ATTENDUS
    # rejeu non validé : rien n'est lu, aucune garde de réception, aucun .npz
    _fiche(depot, {"format": K.FORMAT_FICHE, "redaction": "essai", "R1": None, "motif_R1": "rejeu_non_conforme",
                   "R2": None, "motif_R2": "sorties_non_livrees"}, "fiche-nv.json")
    with monkeypatch.context() as mp:
        etat = _piege_npz(mp, LP8)
        r = LP8.analyser(depot, "fiche-nv.json", "20261105-030004-v8", None, entropie=K.entropie_racine(),
                         autoriser_depot_sale=True)
        assert etat == {"garde_faite": False, "appels_npz": 0, "appels_npz_avant_garde": 0}
    assert r["mode"] == "rejeu non validé" and r["reception_v4"] is None and "calcul" not in r


# ------------------------------------------------------------------------------------------------ K2, mode décisif
def test_mode_decisif_v8_liste_close_des_passages(depot, monkeypatch):
    d = _donnees(15)
    f, pieces = _source_v8(depot, monkeypatch, d)
    monkeypatch.setattr(LP, "exiger_code_importe_sous", lambda r: None)          # vraie garde éprouvée en v1
    monkeypatch.setattr(K, "VERSIONS_EXIGEES", {k: v for k, v in LP.versions().items() if k in ("python", "numpy", "scipy")})
    f2 = LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS + LP2.FICHIERS_REUTILISES
    ligne_v2 = f"Empreinte des constantes (analyse principale, code v2) : `{K2.empreinte_constantes()}`"
    sha_t = _texte_jouet(depot, K8.TEXTE["chemin"], ligne_v2, _bloc("## Code", f2))
    texte = {"chemin": K8.TEXTE["chemin"], "sha256": sha_t}
    monkeypatch.setattr(K8, "TEXTE", texte)
    _texte_jouet(depot, "prereg/autre-texte.md", ligne_v2, _bloc("## Code", f2))     # même liste, autre texte : refusé
    _texte_jouet(depot, K9.TEXTE["chemin"], "texte jouet par épisode")
    _texte_jouet(depot, C5.TEXTE["chemin"], "texte jouet secondaire")
    # course v3 de R1 simulée : les trois manifestes, gelés par run et empreinte (K2) ; celui de la lecture par épisode
    # cite le texte de la principale dans sa configuration (comme le vrai, par ses constantes), celui de la secondaire non
    runs_v3 = list(K8.PASSAGES_V3)
    passages = {runs_v3[0]: _manifeste_v3_jouet(depot, runs_v3[0], K8.TEXTE["chemin"], K2.COMMANDE),
                runs_v3[1]: _manifeste_v3_jouet(depot, runs_v3[1], K9.TEXTE["chemin"], K5.COMMANDE,
                                                {"constantes": {"PREREG_PRINCIPALE": texte}}),
                runs_v3[2]: _manifeste_v3_jouet(depot, runs_v3[2], C5.TEXTE["chemin"], "python -m controle_ia.analyse_blanche_noire.lecture_v3")}
    monkeypatch.setattr(K8, "PASSAGES_V3", passages)
    autre = _bloc(K9.TITRE_LISTE, LP8.FICHIERS_PAQUET + ("src/controle_ia/analyse_principale_r1_r2/lecture_v9.py",))
    sha_a = _addendum_jouet(depot, blocs=(autre,))
    _addendum_jouet(depot, "prereg/add-altere.md", alterer=True)
    _addendum_jouet(depot, "prereg/add-v6.md", fichiers=LP6.FICHIERS_PAQUET + LP6.FICHIERS_ESSAIS + LP6.FICHIERS_REUTILISES)
    # un manifeste d'une autre version neuve sous l'addendum (commande sœur gelée) est toléré
    creer_manifeste(depot, "20261105-040000-analyse-par-episode-v1", {"addendum": {"chemin": K8.ADDENDUM, "sha256": sha_a}},
                    ["x"], entropie=2, decisif=True, prereg=depot / K9.TEXTE["chemin"], commande=K9.COMMANDE,
                    autoriser_depot_sale=True)
    committer(depot)
    with pytest.raises(GardeArret, match="texte passé"):
        LP8.analyser(depot, "fiche.json", "20261105-041001-x", "prereg/autre-texte.md")
    with pytest.raises(GardeArret, match="empreinte citée"):
        LP8.exiger_code_cite((depot / "prereg/add-altere.md").read_text(encoding="utf-8"))
    with pytest.raises(GardeArret, match="liste fermée"):
        LP8.exiger_code_cite((depot / "prereg/add-v6.md").read_text(encoding="utf-8"))
    with pytest.raises(GardeArret, match="entropie"):
        LP8.analyser(depot, "fiche.json", "20261105-041002-x", K8.TEXTE["chemin"], entropie=5)
    # cas sain : les trois tolérés présents (deux citent ce texte, un non), la sœur sous l'addendum tolérée
    lus = len(list((depot / "runs").glob("*/manifeste.json")))
    r = LP8.analyser(depot, "fiche.json", "20261105-041003-analyse-principale-r1-r2-v1", K8.TEXTE["chemin"])
    assert r["statut"] == "décisif" and int(r["entropie"]) == K2.entropie_de(sha_t)   # graines du texte, inchangées
    lien = r["lien_au_preenregistrement"]
    assert lien["sha256"] == sha_t and lien["addendum"]["chemin"] == K8.ADDENDUM and lien["addendum"]["sha256"] == sha_a
    assert set(lien["addendum"]["code_cite"]["fichiers"]) == set(LP8.FICHIERS_PAQUET + LP8.FICHIERS_ESSAIS
                                                                 + LP8.FICHIERS_REUTILISES)
    assert lien["passages"] == {"manifestes_lus": lus, "autres_analyses_sous_l_addendum": 1,
                                "passages_anterieurs_du_texte_hors_addendum": 2,
                                "toleres": [runs_v3[0], runs_v3[1], "20261105-040000-analyse-par-episode-v1"]}
    assert r["reception_v4"]["table"]["sha256"] == pieces["table"]
    man = json.loads((depot / "runs" / "20261105-041003-analyse-principale-r1-r2-v1" / "manifeste.json")
                     .read_text(encoding="utf-8"))
    assert man["decisif"] and man["preenregistrement"] == {"chemin": K8.TEXTE["chemin"], "sha256": sha_t}
    assert man["commande"] == K8.COMMANDE and man["config"]["addendum"] == {"chemin": K8.ADDENDUM, "sha256": sha_a}
    ref = graines(list(K.CLES_GRAINES), K2.entropie_de(sha_t))
    assert all(man["graines"][k] == ref[k] for k in K.CLES_GRAINES)
    committer(depot)
    # second passage : arrêt distinct, le manifeste est nommé
    with pytest.raises(LP8.PassageHorsListe, match="second passage : 20261105-041003-analyse-principale-r1-r2-v1"):
        LP8.analyser(depot, "fiche.json", "20261105-041004-x", K8.TEXTE["chemin"])
    assert not (depot / "runs" / "20261105-041004-x").exists()
    garde = lambda **k: LP8.exiger_premier_passage_sous(depot, K8.ADDENDUM, sha_a, k.pop("commande", "autre commande"),
                                                        texte, **k)
    assert garde()["autres_analyses_sous_l_addendum"] == 2                             # sain, vu d'une commande sœur
    # artefact : un quatrième manifeste qui cite le texte (course antérieure non gelée) → arrêt, nommé
    quatrieme = "20261104-000000-analyse-principale-r1-r2-v1"
    _manifeste_v3_jouet(depot, quatrieme, K8.TEXTE["chemin"], K2.COMMANDE)
    with pytest.raises(LP8.PassageHorsListe, match=f"hors liste close : {quatrieme} cite le texte"):
        garde()
    with pytest.raises(LP8.PassageHorsListe, match=quatrieme):
        LP8.analyser(depot, "fiche.json", "20261105-041006-x", K8.TEXTE["chemin"])
    import shutil
    shutil.rmtree(depot / "runs" / quatrieme)
    assert garde()["passages_anterieurs_du_texte_hors_addendum"] == 2
    # artefact : un toléré à l'empreinte altérée (manifeste réécrit, ou empreinte gelée autre) → arrêt, nommé
    with pytest.raises(LP8.PassageHorsListe, match=f"hors liste close : {runs_v3[0]} cite le texte"):
        garde(passages_v3={**passages, runs_v3[0]: "0" * 64})
    p0 = depot / "runs" / runs_v3[0] / "manifeste.json"
    octets = p0.read_bytes()
    p0.write_bytes(octets + b"\n")
    with pytest.raises(LP8.PassageHorsListe, match=runs_v3[0]):
        garde()
    p0.write_bytes(octets)
    assert garde()["manifestes_lus"] == lus + 1
    # artefact : une commande hors des trois gelées sous l'addendum → arrêt, nommé
    creer_manifeste(depot, "20261105-041007-inconnue", {"addendum": {"chemin": K8.ADDENDUM, "sha256": sha_a}}, ["x"],
                    entropie=3, decisif=True, prereg=depot / K9.TEXTE["chemin"], commande="python -m controle_ia.autre",
                    autoriser_depot_sale=True)
    with pytest.raises(LP8.PassageHorsListe, match="20261105-041007-inconnue cite l'addendum .* commande"):
        garde()
    shutil.rmtree(depot / "runs" / "20261105-041007-inconnue")
    # artefact : manifeste illisible qui cite le texte, puis l'addendum → arrêt, nommé
    (depot / "runs" / "20261105-041008-illisible").mkdir()
    (depot / "runs" / "20261105-041008-illisible" / "manifeste.json").write_text("{{" + K8.TEXTE["chemin"], encoding="utf-8")
    with pytest.raises(LP8.PassageHorsListe, match="illisible 20261105-041008-illisible"):
        garde()
    (depot / "runs" / "20261105-041008-illisible" / "manifeste.json").write_text("{{" + K8.ADDENDUM, encoding="utf-8")
    with pytest.raises(LP8.PassageHorsListe, match="illisible 20261105-041008-illisible"):
        garde()
    shutil.rmtree(depot / "runs" / "20261105-041008-illisible")
    # un manifeste qui ne cite ni le texte ni l'addendum, même illisible, est ignoré
    (depot / "runs" / "20261105-041009-etranger").mkdir()
    (depot / "runs" / "20261105-041009-etranger" / "manifeste.json").write_text("{{rien", encoding="utf-8")
    assert garde()["manifestes_lus"] == lus + 2
    monkeypatch.setattr(K8, "TABLE_V4", "prereg/autre-table.json")                 # constantes ≠ empreinte citée
    with pytest.raises(GardeArret, match="constantes gelées"):
        LP8.exiger_code_cite((depot / K8.ADDENDUM).read_text(encoding="utf-8"))
