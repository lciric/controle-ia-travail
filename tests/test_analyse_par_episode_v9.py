"""Lecture complémentaire « par épisode » de R1-R2, code v9 (addendum 1 « gardes des analyses », relance v4 de R1,
après la contre-lecture 1 : K1, K2, K3) : essais R5 sur données **synthétiques** (générateur et écrivains des essais v1
de la principale ; pièces de la relance v4 des essais v6 et v8) — jamais les vraies données de R1, R2 ni de P3. Même
calcul, même concordance et même issue que le code v5 ; **K1** : aucun `.npz` ouvert avant les gardes de réception
(piège sur `numpy.load` : artefact de provenance arrêté sans appel, cas sain appelé après) ; rejeu non validé ; mode
décisif sous l'addendum unique, après la principale sous le code v8 (texte qui gouverne inchangé, plis de la principale,
bloc propre à cette lecture, **K2** liste close : manifeste de la course v3 gelé toléré, principale v8 sous l'addendum
tolérée, second passage refusé ; **K3** : principale d'un autre code, d'un autre addendum ou d'un autre rejeu refusée) ;
liste fermée v9."""
import hashlib
import json
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.analyse_blanche_noire import constantes_v5 as C5
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v2 as K2
from controle_ia.analyse_principale_r1_r2 import constantes_v4 as K4
from controle_ia.analyse_principale_r1_r2 import constantes_v5 as K5
from controle_ia.analyse_principale_r1_r2 import constantes_v7 as K7
from controle_ia.analyse_principale_r1_r2 import constantes_v8 as K8
from controle_ia.analyse_principale_r1_r2 import constantes_v9 as K9
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as LP
from controle_ia.analyse_principale_r1_r2 import lecture_v2 as LP2
from controle_ia.analyse_principale_r1_r2 import lecture_v5 as LE5
from controle_ia.analyse_principale_r1_r2 import lecture_v7 as LE7
from controle_ia.analyse_principale_r1_r2 import lecture_v8 as LP8
from controle_ia.analyse_principale_r1_r2 import lecture_v9 as LE9
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.scellement import empreinte
from test_analyse_par_episode_v1 import E_PLIS, _principale
from test_analyse_principale_r1_r2_v1 import D, RUN, _donnees
from test_analyse_principale_r1_r2_v6 import RUN_REJEU, _bloc, _ecrire_r1_v4, _fiche, _texte_jouet
from test_analyse_principale_r1_r2_v8 import _manifeste_v3_jouet, _piege_npz, _source_v8

RACINE = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def constantes_reduites(monkeypatch):
    for nom, v in (("DIMENSION", D), ("TIRAGES", 300), ("N_PLANCHER", 50), ("RUN_P3", RUN)):
        monkeypatch.setattr(K, nom, v)
    for nom, v in (("TIRAGES", 300), ("N_PLANCHER", 50)):
        monkeypatch.setattr(K4, nom, v)


def _episode9(depot, principale, run="20261105-061000-episode-v9", entropie=99, entropie_plis=E_PLIS, fiche="fiche.json"):
    return LE9.analyser(depot, fiche, principale, run, None, entropie=entropie, entropie_plis=entropie_plis,
                        autoriser_depot_sale=True)


def test_constantes_v9_gelees_et_liste_fermee():
    assert K9.TEXTE == K7.TEXTE == {"chemin": "prereg/analyse-par-episode-v1.md",
                                    "sha256": "26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4"}
    assert empreinte(RACINE / K9.TEXTE["chemin"]) == K9.TEXTE["sha256"]                 # texte scellé, inchangé
    assert K9.ADDENDUM == K8.ADDENDUM and K9.NOM_SORTIE == K5.NOM_SORTIE
    assert K9.VERSION == "analyse-par-episode-v1 (code v9)" and K9.TITRE_LISTE.endswith("(code v9)")
    assert K9.COMMANDE == "python -m controle_ia.analyse_principale_r1_r2.lecture_v9" and K9.COMMANDE in K8.COMMANDES_ADDENDUM
    assert K9.entropie_principale() == K5.entropie_principale() == K4.entropie_principale()
    assert K9.empreinte_constantes() not in (K5.empreinte_constantes(), K7.empreinte_constantes())
    assert K9.constantes_courantes()["v8"] == K8.constantes_courantes()["v8"]
    assert K9.constantes_courantes()["v1_v2_v4_v5"] == K5.constantes_courantes()
    for c in LE9.FICHIERS_PAQUET + LE9.FICHIERS_ESSAIS + LE9.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LE5.FICHIERS_PAQUET) < set(LE9.FICHIERS_PAQUET) and set(LE5.FICHIERS_ESSAIS) < set(LE9.FICHIERS_ESSAIS)
    assert set(LP8.FICHIERS_PAQUET) < set(LE9.FICHIERS_PAQUET)
    assert not any("_v6" in c or "_v7" in c or "entrees_v4" in c for c in LE9.FICHIERS_PAQUET + LE9.FICHIERS_ESSAIS)
    assert len(set(LE9.FICHIERS_PAQUET) | set(LE9.FICHIERS_ESSAIS) | set(LE9.FICHIERS_REUTILISES)) == 33
    assert LE9.calculer is LE5.calculer and LE9.issue is LE5.issue and LE9.rendre is LE5.rendre
    assert LE9.lire_principale is LE5.lire_principale
    assert LE9.exiger_concordance_principale is LE5.exiger_concordance_principale
    assert LE9.PassageHorsListe is LP8.PassageHorsListe and LE9.CODE_FIN_PASSAGE == 2
    with pytest.raises(GardeArret, match="titre"):
        LE9.exiger_code_cite("rien")
    # K3, sur des résultats jouets
    rp = {"version": K8.VERSION, "lien_au_preenregistrement": {"addendum": {"sha256": "a" * 64}},
          "reception_v4": {"run_rejeu": "r"}}
    assert LE9.exiger_principale_sous_addendum(rp, "a" * 64, {"run_rejeu": "r"}) == {
        "version": K8.VERSION, "addendum_sha256": "a" * 64, "run_rejeu": "r"}
    assert LE9.exiger_principale_sous_addendum(dict(rp, reception_v4=None), "a" * 64, None)["run_rejeu"] is None
    with pytest.raises(GardeArret, match="version .*K3"):
        LE9.exiger_principale_sous_addendum(dict(rp, version=K7.VERSION), "a" * 64, {"run_rejeu": "r"})
    with pytest.raises(GardeArret, match="addendum unique scellé"):
        LE9.exiger_principale_sous_addendum(rp, "b" * 64, {"run_rejeu": "r"})
    with pytest.raises(GardeArret, match="rejeu reçu par la principale"):
        LE9.exiger_principale_sous_addendum(rp, "a" * 64, {"run_rejeu": "autre"})
    with pytest.raises(GardeArret, match="rejeu reçu par la principale"):
        LE9.exiger_principale_sous_addendum(dict(rp, reception_v4=None), "a" * 64, {"run_rejeu": "r"})


def test_v9_meme_calcul_que_v5_k1_et_rejeu_non_valide(depot, monkeypatch):
    d = _donnees(6, w=2.0)
    f, pieces = _source_v8(depot, monkeypatch, d)
    pr = _principale(depot)
    with monkeypatch.context() as mp:                                                   # K1, cas sain
        etat = _piege_npz(mp, LE9)
        r9 = _episode9(depot, pr)
        assert etat["garde_faite"] and etat["appels_npz"] > 0 and etat["appels_npz_avant_garde"] == 0
    r5 = LE5.analyser(depot, "fiche.json", pr, "20261105-061001-episode-v5", None, entropie=99, entropie_plis=E_PLIS,
                      autoriser_depot_sale=True)
    assert r9["calcul"] == r5["calcul"] and r9["issue"] == r5["issue"] and r9["version"] == K9.VERSION
    assert r9["concordance_principale"] == r5["concordance_principale"] and r9["concordance_principale"]["seuils"] == "identiques"
    assert r9["reception_v4"]["table"]["sha256"] == pieces["table"] and r9["reception_v4"]["run_rejeu"] == RUN_REJEU
    assert r9["principale"]["sous_addendum"] is None                                   # K3 : mode décisif seulement
    man = json.loads((depot / "runs" / "20261105-061000-episode-v9" / "manifeste.json").read_text(encoding="utf-8"))
    assert man["commande"] == K9.COMMANDE and man["config"]["constantes_sha256"] == K9.empreinte_constantes()
    assert (depot / "diag" / "20261105-061000-episode-v9" / f"{K9.NOM_SORTIE}.md.sha256").exists()
    # artefact (K1) : provenance fausse → arrêt avant la principale, aucun .npz ouvert, rien d'écrit
    _fiche(depot, dict(f, R1=_ecrire_r1_v4(depot, d, K.EMPREINTES_P3["textes"], pieces["table"], run=RUN_REJEU + "-p",
                                           addendum_tok="prereg/R1-addendum-relance-v3.md")), "fiche-p.json")
    LP2.analyser(depot, "fiche-p.json", "20261105-061002-principale-p", None, entropie=E_PLIS, autoriser_depot_sale=True)
    with monkeypatch.context() as mp:
        etat = _piege_npz(mp, LE9)
        with pytest.raises(GardeArret, match="garde provenance"):
            _episode9(depot, f"diag/20261105-061002-principale-p/{K2.NOM_SORTIE}.json", run="20261105-061003-x",
                      fiche="fiche-p.json")
        assert etat == {"garde_faite": False, "appels_npz": 0, "appels_npz_avant_garde": 0}
    assert not (depot / "runs" / "20261105-061003-x").exists()
    # rejeu non validé : rien n'est lu, aucune garde de réception
    _fiche(depot, {"format": K.FORMAT_FICHE, "redaction": "essai", "R1": None, "motif_R1": "rejeu_non_conforme",
                   "R2": None, "motif_R2": "sorties_non_livrees"}, "fiche-nv.json")
    LP2.analyser(depot, "fiche-nv.json", "20261105-061004-principale-nv", None, entropie=E_PLIS, autoriser_depot_sale=True)
    r = _episode9(depot, f"diag/20261105-061004-principale-nv/{K2.NOM_SORTIE}.json", run="20261105-061005-episode-nv",
                  fiche="fiche-nv.json")
    assert r["mode"] == "rejeu non validé" and r["reception_v4"] is None and "calcul" not in r


def test_mode_decisif_v9_liste_close_et_principale_v8_sous_l_addendum(depot, monkeypatch):
    d = _donnees(15)
    f, pieces = _source_v8(depot, monkeypatch, d)
    monkeypatch.setattr(LP, "exiger_code_importe_sous", lambda r: None)
    monkeypatch.setattr(K, "VERSIONS_EXIGEES", {k: v for k, v in LP.versions().items() if k in ("python", "numpy", "scipy")})
    f2 = LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS + LP2.FICHIERS_REUTILISES
    sha_pr = _texte_jouet(depot, K8.TEXTE["chemin"],
                          f"Empreinte des constantes (analyse principale, code v2) : `{K2.empreinte_constantes()}`",
                          _bloc("## Code", f2))
    monkeypatch.setattr(K8, "TEXTE", {"chemin": K8.TEXTE["chemin"], "sha256": sha_pr})
    monkeypatch.setattr(K4, "PREREG_PRINCIPALE", dict(K4.PREREG_PRINCIPALE, sha256=sha_pr))   # plis de la principale
    f5 = LE5.FICHIERS_PAQUET + LE5.FICHIERS_ESSAIS + LE5.FICHIERS_REUTILISES
    sha_ep = _texte_jouet(depot, K9.TEXTE["chemin"],
                          f"Empreinte des constantes (analyse par épisode, code v5) : `{K5.empreinte_constantes()}`",
                          _bloc("## Code", f5))
    monkeypatch.setattr(K9, "TEXTE", {"chemin": K9.TEXTE["chemin"], "sha256": sha_ep})
    _texte_jouet(depot, C5.TEXTE["chemin"], "texte jouet secondaire")
    # course v3 simulée : les trois manifestes gelés (K2) ; celui de la lecture par épisode cite aussi le texte principal
    runs_v3 = list(K8.PASSAGES_V3)
    passages = {runs_v3[0]: _manifeste_v3_jouet(depot, runs_v3[0], K8.TEXTE["chemin"], K2.COMMANDE),
                runs_v3[1]: _manifeste_v3_jouet(depot, runs_v3[1], K9.TEXTE["chemin"], K5.COMMANDE,
                                                {"constantes": {"PREREG_PRINCIPALE": K8.TEXTE}}),
                runs_v3[2]: _manifeste_v3_jouet(depot, runs_v3[2], C5.TEXTE["chemin"], "python -m controle_ia.analyse_blanche_noire.lecture_v3")}
    monkeypatch.setattr(K8, "PASSAGES_V3", passages)
    # addendum unique jouet : les deux blocs (principale, code v8 ; par épisode, code v9) dans le même texte
    f9 = LE9.FICHIERS_PAQUET + LE9.FICHIERS_ESSAIS + LE9.FICHIERS_REUTILISES
    bloc9 = _bloc(K9.TITRE_LISTE, f9)
    ligne9 = f"Empreinte des constantes (analyse par épisode, code v9) : `{K9.empreinte_constantes()}`"
    sha_a = _texte_jouet(depot, K8.ADDENDUM,
                         f"Empreinte des constantes (analyse principale, code v8) : `{K8.empreinte_constantes()}`",
                         ligne9, _bloc(K8.TITRE_LISTE, LP8.FICHIERS_PAQUET + LP8.FICHIERS_ESSAIS + LP8.FICHIERS_REUTILISES),
                         bloc9)
    committer(depot)
    LP8.analyser(depot, "fiche.json", "20261105-070000-analyse-principale-r1-r2-v1", K8.TEXTE["chemin"])   # principale d'abord
    pr = f"diag/20261105-070000-analyse-principale-r1-r2-v1/{K8.NOM_SORTIE}.json"
    committer(depot)
    with pytest.raises(GardeArret, match="texte passé"):                               # texte de la principale passé ici
        LE9.analyser(depot, "fiche.json", pr, "20261105-071001-x", K8.TEXTE["chemin"])
    with pytest.raises(GardeArret, match="entropie des plis"):
        LE9.analyser(depot, "fiche.json", pr, "20261105-071002-x", K9.TEXTE["chemin"], entropie_plis=7)
    with pytest.raises(GardeArret, match="entropie"):
        LE9.analyser(depot, "fiche.json", pr, "20261105-071003-x", K9.TEXTE["chemin"], entropie=7)
    corps = json.loads((depot / pr).read_text(encoding="utf-8"))
    lus = len(list((depot / "runs").glob("*/manifeste.json")))
    r = LE9.analyser(depot, "fiche.json", pr, "20261105-071004-analyse-par-episode-v1", K9.TEXTE["chemin"])
    assert r["statut"] == "décisif" and int(r["entropie"]) == K2.entropie_de(sha_ep)
    assert int(r["entropie_plis"]) == K2.entropie_de(sha_pr) != int(r["entropie"])
    assert r["concordance_principale"]["seuils"] == "identiques" and r["concordance_principale"]["aires"] == "identiques"
    assert r["reception_v4"]["table"]["sha256"] == pieces["table"]
    assert r["principale"]["sous_addendum"] == {"version": K8.VERSION, "addendum_sha256": sha_a, "run_rejeu": RUN_REJEU}   # K3
    lien = r["lien_au_preenregistrement"]
    assert lien["sha256"] == sha_ep and lien["addendum"] == {"chemin": K8.ADDENDUM, "sha256": sha_a,
                                                             "code_cite": lien["addendum"]["code_cite"]}
    assert set(lien["addendum"]["code_cite"]["fichiers"]) == set(f9)
    assert lien["passages"] == {"manifestes_lus": lus, "autres_analyses_sous_l_addendum": 1,   # la principale v8, tolérée
                                "passages_anterieurs_du_texte_hors_addendum": 1,          # la course v3, gelée
                                "toleres": [runs_v3[1], "20261105-070000-analyse-principale-r1-r2-v1"]}
    man = json.loads((depot / "runs" / "20261105-071004-analyse-par-episode-v1" / "manifeste.json")
                     .read_text(encoding="utf-8"))
    assert man["decisif"] and man["commande"] == K9.COMMANDE and man["preenregistrement"]["sha256"] == sha_ep
    assert man["config"]["addendum"] == {"chemin": K8.ADDENDUM, "sha256": sha_a}
    ref = graines(list(K4.CLES_GRAINES), K2.entropie_de(sha_ep))
    assert all(man["graines"][k] == ref[k] for k in K4.CLES_GRAINES)
    committer(depot)
    with pytest.raises(LP8.PassageHorsListe, match="second passage : 20261105-071004-analyse-par-episode-v1"):
        LE9.analyser(depot, "fiche.json", pr, "20261105-071005-x", K9.TEXTE["chemin"])
    # K2, artefacts vus de cette lecture : le manifeste gelé de la course v3 altéré (empreinte gelée autre, ou octets
    # réécrits) → arrêt, nommé ; un quatrième manifeste qui cite ce texte → arrêt, nommé
    garde = lambda **k: LP8.exiger_premier_passage_sous(depot, K9.ADDENDUM, sha_a, "autre commande", K9.TEXTE, **k)
    assert garde()["toleres"] == [runs_v3[1], "20261105-070000-analyse-principale-r1-r2-v1",
                                  "20261105-071004-analyse-par-episode-v1"]
    with pytest.raises(LP8.PassageHorsListe, match=f"hors liste close : {runs_v3[1]} cite le texte"):
        garde(passages_v3={**passages, runs_v3[1]: "0" * 64})
    p1 = depot / "runs" / runs_v3[1] / "manifeste.json"
    octets = p1.read_bytes()
    p1.write_bytes(octets + b"\n")
    with pytest.raises(LP8.PassageHorsListe, match=runs_v3[1]):
        LE9.analyser(depot, "fiche.json", pr, "20261105-071006-x", K9.TEXTE["chemin"])
    p1.write_bytes(octets)
    quatrieme = "20261104-000000-analyse-par-episode-v1"
    _manifeste_v3_jouet(depot, quatrieme, K9.TEXTE["chemin"], K5.COMMANDE)
    with pytest.raises(LP8.PassageHorsListe, match=f"hors liste close : {quatrieme} cite le texte"):
        garde()
    import shutil
    shutil.rmtree(depot / "runs" / quatrieme)
    # K3, artefacts sur le résultat scellé de la principale v8 (version d'un autre code, autre addendum, autre rejeu)
    with pytest.raises(GardeArret, match="K3"):
        LE9.exiger_principale_sous_addendum(dict(corps["resultat"], version=K7.VERSION), sha_a, {"run_rejeu": RUN_REJEU})
    with pytest.raises(GardeArret, match="K3"):
        LE9.exiger_principale_sous_addendum(corps["resultat"], "0" * 64, {"run_rejeu": RUN_REJEU})
    with pytest.raises(GardeArret, match="K3"):
        LE9.exiger_principale_sous_addendum(corps["resultat"], sha_a, {"run_rejeu": RUN_REJEU + "-autre"})
    assert LE9.exiger_principale_sous_addendum(corps["resultat"], sha_a, {"run_rejeu": RUN_REJEU})["version"] == K8.VERSION
    with pytest.raises(GardeArret, match="liste fermée"):                               # liste v5 dans le bloc v9
        LE9.exiger_code_cite("\n\n".join(["# a", ligne9, _bloc(K9.TITRE_LISTE, f5)]))
    with pytest.raises(GardeArret, match="liste fermée"):                               # liste v7 dans le bloc v9
        LE9.exiger_code_cite("\n\n".join(["# a", ligne9, _bloc(K9.TITRE_LISTE, LE7.FICHIERS_PAQUET + LE7.FICHIERS_ESSAIS
                                                             + LE7.FICHIERS_REUTILISES)]))
    with pytest.raises(GardeArret, match="constantes gelées"):                         # constantes v7 citées
        LE9.exiger_code_cite("\n\n".join(["# a", f"Empreinte des constantes (analyse par épisode, code v9) : "
                                          f"`{K7.empreinte_constantes()}`", bloc9]))
    with pytest.raises(GardeArret, match="empreinte citée"):
        LE9.exiger_code_cite("\n\n".join(["# a", ligne9, _bloc(K9.TITRE_LISTE, f9, alterer=True)]))
