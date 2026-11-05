"""Lecture complémentaire « par épisode » de R1-R2, code v7 (addendum 1 « gardes des analyses », relance v4 de R1) :
essais R5 sur données **synthétiques** (générateur et écrivains des essais v1 de la principale ; pièces de la relance
v4 des essais v6 de la principale) — jamais les vraies données de R1, R2 ni de P3. Même calcul, même concordance et
même issue que le code v5 ; gardes de réception écrites, artefact de bout en bout (provenance), rejeu non validé ; mode
décisif sous l'addendum unique, après la principale sous le code v6 (texte qui gouverne inchangé, plis de la principale,
bloc propre à cette lecture, manifeste de la principale sous l'addendum toléré, second passage refusé, liste v5 et
constantes v5 refusées) ; liste fermée v7."""
import json
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v2 as K2
from controle_ia.analyse_principale_r1_r2 import constantes_v4 as K4
from controle_ia.analyse_principale_r1_r2 import constantes_v5 as K5
from controle_ia.analyse_principale_r1_r2 import constantes_v6 as K6
from controle_ia.analyse_principale_r1_r2 import constantes_v7 as K7
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as LP
from controle_ia.analyse_principale_r1_r2 import lecture_v2 as LP2
from controle_ia.analyse_principale_r1_r2 import lecture_v5 as LE5
from controle_ia.analyse_principale_r1_r2 import lecture_v6 as LP6
from controle_ia.analyse_principale_r1_r2 import lecture_v7 as LE7
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.scellement import empreinte
from test_analyse_par_episode_v1 import E_PLIS, _principale
from test_analyse_principale_r1_r2_v1 import D, RUN, _donnees
from test_analyse_principale_r1_r2_v6 import RUN_REJEU, _bloc, _ecrire_r1_v4, _fiche, _source_v4, _texte_jouet

RACINE = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def constantes_reduites(monkeypatch):
    for nom, v in (("DIMENSION", D), ("TIRAGES", 300), ("N_PLANCHER", 50), ("RUN_P3", RUN)):
        monkeypatch.setattr(K, nom, v)
    for nom, v in (("TIRAGES", 300), ("N_PLANCHER", 50)):
        monkeypatch.setattr(K4, nom, v)


def _episode7(depot, principale, run="20261105-061000-episode-v7", entropie=99, entropie_plis=E_PLIS, fiche="fiche.json"):
    return LE7.analyser(depot, fiche, principale, run, None, entropie=entropie, entropie_plis=entropie_plis,
                        autoriser_depot_sale=True)


def test_constantes_v7_gelees_et_liste_fermee():
    assert K7.TEXTE == {"chemin": "prereg/analyse-par-episode-v1.md",
                        "sha256": "26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4"}
    assert empreinte(RACINE / K7.TEXTE["chemin"]) == K7.TEXTE["sha256"]                 # texte scellé, inchangé
    assert K7.ADDENDUM == K6.ADDENDUM and K7.NOM_SORTIE == K5.NOM_SORTIE
    assert K7.entropie_principale() == K5.entropie_principale() == K4.entropie_principale()
    assert K7.empreinte_constantes() != K5.empreinte_constantes()
    assert K7.constantes_courantes()["v6"] == K6.constantes_courantes()["v6"]
    assert K7.constantes_courantes()["v1_v2_v4_v5"] == K5.constantes_courantes()
    for c in LE7.FICHIERS_PAQUET + LE7.FICHIERS_ESSAIS + LE7.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LE5.FICHIERS_PAQUET) < set(LE7.FICHIERS_PAQUET) and set(LE5.FICHIERS_ESSAIS) < set(LE7.FICHIERS_ESSAIS)
    assert set(LP6.FICHIERS_PAQUET) < set(LE7.FICHIERS_PAQUET)
    assert len(set(LE7.FICHIERS_PAQUET) | set(LE7.FICHIERS_ESSAIS) | set(LE7.FICHIERS_REUTILISES)) == 33
    assert LE7.calculer is LE5.calculer and LE7.issue is LE5.issue and LE7.rendre is LE5.rendre
    assert LE7.lire_principale is LE5.lire_principale
    assert LE7.exiger_concordance_principale is LE5.exiger_concordance_principale
    with pytest.raises(GardeArret, match="titre"):
        LE7.exiger_code_cite("rien")


def test_v7_meme_calcul_que_v5_reception_artefact_et_rejeu_non_valide(depot, monkeypatch):
    d = _donnees(6, w=2.0)
    f, pieces = _source_v4(depot, monkeypatch, d)
    pr = _principale(depot)
    r7 = _episode7(depot, pr)
    r5 = LE5.analyser(depot, "fiche.json", pr, "20261105-061001-episode-v5", None, entropie=99, entropie_plis=E_PLIS,
                      autoriser_depot_sale=True)
    assert r7["calcul"] == r5["calcul"] and r7["issue"] == r5["issue"] and r7["version"] == K7.VERSION
    assert r7["concordance_principale"] == r5["concordance_principale"] and r7["concordance_principale"]["seuils"] == "identiques"
    assert r7["reception_v4"]["table"]["sha256"] == pieces["table"] and r7["reception_v4"]["run_rejeu"] == RUN_REJEU
    man = json.loads((depot / "runs" / "20261105-061000-episode-v7" / "manifeste.json").read_text(encoding="utf-8"))
    assert man["commande"] == K7.COMMANDE and man["config"]["constantes_sha256"] == K7.empreinte_constantes()
    assert (depot / "diag" / "20261105-061000-episode-v7" / f"{K7.NOM_SORTIE}.md.sha256").exists()
    # artefact de bout en bout : provenance fausse (fiche propre, principale sous le code v2 qui ne la garde pas)
    _fiche(depot, dict(f, R1=_ecrire_r1_v4(depot, d, K.EMPREINTES_P3["textes"], pieces["table"], run=RUN_REJEU + "-p",
                                           addendum_tok="prereg/R1-addendum-relance-v3.md")), "fiche-p.json")
    LP2.analyser(depot, "fiche-p.json", "20261105-061002-principale-p", None, entropie=E_PLIS, autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="garde provenance"):
        _episode7(depot, f"diag/20261105-061002-principale-p/{K2.NOM_SORTIE}.json", run="20261105-061003-x",
                  fiche="fiche-p.json")
    assert not (depot / "runs" / "20261105-061003-x").exists()
    # rejeu non validé : rien n'est lu, aucune garde de réception
    _fiche(depot, {"format": K.FORMAT_FICHE, "redaction": "essai", "R1": None, "motif_R1": "rejeu_non_conforme",
                   "R2": None, "motif_R2": "sorties_non_livrees"}, "fiche-nv.json")
    LP2.analyser(depot, "fiche-nv.json", "20261105-061004-principale-nv", None, entropie=E_PLIS, autoriser_depot_sale=True)
    r = _episode7(depot, f"diag/20261105-061004-principale-nv/{K2.NOM_SORTIE}.json", run="20261105-061005-episode-nv",
                  fiche="fiche-nv.json")
    assert r["mode"] == "rejeu non validé" and r["reception_v4"] is None and "calcul" not in r


def test_mode_decisif_v7_sous_l_addendum_unique_apres_la_principale(depot, monkeypatch):
    d = _donnees(15)
    f, pieces = _source_v4(depot, monkeypatch, d)
    monkeypatch.setattr(LP, "exiger_code_importe_sous", lambda r: None)
    monkeypatch.setattr(K, "VERSIONS_EXIGEES", {k: v for k, v in LP.versions().items() if k in ("python", "numpy", "scipy")})
    # textes jouets qui gouvernent, sous les noms réels : principale (liste v2) et par épisode (liste v5)
    f2 = LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS + LP2.FICHIERS_REUTILISES
    sha_pr = _texte_jouet(depot, K6.TEXTE["chemin"],
                          f"Empreinte des constantes (analyse principale, code v2) : `{K2.empreinte_constantes()}`",
                          _bloc("## Code", f2))
    monkeypatch.setattr(K6, "TEXTE", {"chemin": K6.TEXTE["chemin"], "sha256": sha_pr})
    monkeypatch.setattr(K4, "PREREG_PRINCIPALE", dict(K4.PREREG_PRINCIPALE, sha256=sha_pr))   # plis de la principale
    f5 = LE5.FICHIERS_PAQUET + LE5.FICHIERS_ESSAIS + LE5.FICHIERS_REUTILISES
    sha_ep = _texte_jouet(depot, K7.TEXTE["chemin"],
                          f"Empreinte des constantes (analyse par épisode, code v5) : `{K5.empreinte_constantes()}`",
                          _bloc("## Code", f5))
    monkeypatch.setattr(K7, "TEXTE", {"chemin": K7.TEXTE["chemin"], "sha256": sha_ep})
    # addendum unique jouet : les deux blocs (principale, code v6 ; par épisode, code v7) dans le même texte
    f7 = LE7.FICHIERS_PAQUET + LE7.FICHIERS_ESSAIS + LE7.FICHIERS_REUTILISES
    bloc7 = _bloc(K7.TITRE_LISTE, f7)
    ligne7 = f"Empreinte des constantes (analyse par épisode, code v7) : `{K7.empreinte_constantes()}`"
    sha_a = _texte_jouet(depot, K6.ADDENDUM,
                         f"Empreinte des constantes (analyse principale, code v6) : `{K6.empreinte_constantes()}`",
                         ligne7, _bloc(K6.TITRE_LISTE, LP6.FICHIERS_PAQUET + LP6.FICHIERS_ESSAIS + LP6.FICHIERS_REUTILISES),
                         bloc7)
    committer(depot)
    LP6.analyser(depot, "fiche.json", "20261105-070000-analyse-principale-r1-r2-v1", K6.TEXTE["chemin"])   # principale d'abord
    pr = f"diag/20261105-070000-analyse-principale-r1-r2-v1/{K6.NOM_SORTIE}.json"
    committer(depot)
    with pytest.raises(GardeArret, match="texte passé"):                               # texte de la principale passé ici
        LE7.analyser(depot, "fiche.json", pr, "20261105-071001-x", K6.TEXTE["chemin"])
    with pytest.raises(GardeArret, match="entropie des plis"):
        LE7.analyser(depot, "fiche.json", pr, "20261105-071002-x", K7.TEXTE["chemin"], entropie_plis=7)
    with pytest.raises(GardeArret, match="entropie"):
        LE7.analyser(depot, "fiche.json", pr, "20261105-071003-x", K7.TEXTE["chemin"], entropie=7)
    r = LE7.analyser(depot, "fiche.json", pr, "20261105-071004-analyse-par-episode-v1", K7.TEXTE["chemin"])
    assert r["statut"] == "décisif" and int(r["entropie"]) == K2.entropie_de(sha_ep)
    assert int(r["entropie_plis"]) == K2.entropie_de(sha_pr) != int(r["entropie"])
    assert r["concordance_principale"]["seuils"] == "identiques" and r["concordance_principale"]["aires"] == "identiques"
    assert r["reception_v4"]["table"]["sha256"] == pieces["table"]
    lien = r["lien_au_preenregistrement"]
    assert lien["sha256"] == sha_ep and lien["addendum"] == {"chemin": K6.ADDENDUM, "sha256": sha_a,
                                                             "code_cite": lien["addendum"]["code_cite"]}
    assert set(lien["addendum"]["code_cite"]["fichiers"]) == set(f7)
    assert lien["passages"]["autres_analyses_sous_l_addendum"] == 1          # la principale, sous le même addendum
    assert lien["passages"]["passages_anterieurs_du_texte_hors_addendum"] == 0
    man = json.loads((depot / "runs" / "20261105-071004-analyse-par-episode-v1" / "manifeste.json")
                     .read_text(encoding="utf-8"))
    assert man["decisif"] and man["commande"] == K7.COMMANDE and man["preenregistrement"]["sha256"] == sha_ep
    assert man["config"]["addendum"] == {"chemin": K6.ADDENDUM, "sha256": sha_a}
    ref = graines(list(K4.CLES_GRAINES), K2.entropie_de(sha_ep))
    assert all(man["graines"][k] == ref[k] for k in K4.CLES_GRAINES)
    committer(depot)
    with pytest.raises(GardeArret, match="second passage"):
        LE7.analyser(depot, "fiche.json", pr, "20261105-071005-x", K7.TEXTE["chemin"])
    with pytest.raises(GardeArret, match="liste fermée"):                               # liste v5 dans le bloc v7
        LE7.exiger_code_cite("\n\n".join(["# a", ligne7, _bloc(K7.TITRE_LISTE, f5)]))
    with pytest.raises(GardeArret, match="constantes gelées"):                         # constantes v5 citées
        LE7.exiger_code_cite("\n\n".join(["# a", f"Empreinte des constantes (analyse par épisode, code v7) : "
                                          f"`{K5.empreinte_constantes()}`", bloc7]))
    with pytest.raises(GardeArret, match="empreinte citée"):
        LE7.exiger_code_cite("\n\n".join(["# a", ligne7, _bloc(K7.TITRE_LISTE, f7, alterer=True)]))
