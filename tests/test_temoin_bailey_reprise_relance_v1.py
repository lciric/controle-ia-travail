"""Essai sur processeur du chemin « relance seule coupée, reprise (lecture 38), assemblage, lecture » (addendum 6, risque
(d) ; contre-lecture de l'addendum 6, L-6). Aucun code du lanceur ne change (`lanceur_v20`) : on éprouve le chemin.

Cas sain : relance seule dont le run s'interrompt après 25 tours complets (processus mort), poste éteint avant la
destruction ; la reprise transfère, compare, scelle et détruit ; l'assemblage de la première conduite et du dossier de
reprise se lit comme un run tronqué de 25 tours (K′ ≥ 20, l. 338, 372), interruptions rapportées.
Artefact : même chemin coupé à 12 tours : la lecture ne donne pas de verdict (seconde erreur avant 20 tours, l. 371).
"""
from __future__ import annotations

import json

import pytest

import test_temoin_bailey_condition6_v20 as T
from controle_ia import scellement
from controle_ia.temoin_bailey import analyse_v3 as an
from controle_ia.temoin_bailey import instance_v16 as inst
from controle_ia.temoin_bailey import lanceur_v20 as la
from controle_ia.temoin_bailey import lecture_v8 as lc

ETIQ = T.ETIQ
LOIN = T.LOIN


def _relance_coupee(tmp_path, monkeypatch, k_coupe: int):
    """Première conduite interrompue (3 tours) ; relance seule dont `principal-relance` écrit `k_coupe` tours puis
    meurt ; destruction impossible (poste éteint) ; instance factice arrêtée, prête pour la reprise."""
    premiere = T._premiere_interrompue(tmp_path, monkeypatch)
    scen = T.scenario(30, T.principal_fini(30))

    def relance_morte(f):
        k2 = json.loads(f.local("/root/manifeste-v3-relance.json").read_text())["regle_tours"]["K"]
        x = f.execution("principal-relance", k_coupe, {"k": k2})
        (x / T.cv.ETAT_EXECUTION).unlink()
        return "mort"
    scen["principal-relance"] = relance_morte
    c, f = T._relance(tmp_path, monkeypatch, premiere, scen=scen)
    f.detruire = lambda ident: (_ for _ in ()).throw(RuntimeError("poste éteint"))
    bilan = c.conduire()
    assert bilan["detruite"] is False, bilan
    del f.detruire
    vrai = f.executer
    f.etat, f.demarrages, f.arrets, f.minuteries, f.en_cours = "stopped", [], [], [], []

    def executer(ident, commande, delai_s=None):
        if f.etat != "running":
            return 255, ""
        if commande.startswith("ls -1 /root/x"):
            return 0, "\n".join(sorted(p.name for p in f.local("/root/x").iterdir())) + "\n"
        if f"{inst.MINUTERIE}.pid" in commande:
            f.minuteries.append(commande)
            return 0, "LANCE 999\n"
        if " en-cours" in commande:
            return 0, "ETAT " + json.dumps({"commande": "en-cours", "en_cours": f.en_cours}) + "\n"
        return vrai(ident, commande, delai_s)
    f.executer = executer
    f.inventaire = lambda e: ["77"] if e == ETIQ else ["99"]
    f.statut = lambda ident: f.etat
    f.demarrer = lambda ident: (f.demarrages.append(ident), setattr(f, "etat", "running"))
    f.arreter = lambda ident: (f.arrets.append(ident), setattr(f, "etat", "stopped"))
    f.detruites.clear()
    f.veilleurs, f.veilleurs_arretes = [], []
    monkeypatch.setattr(la, "lancer_veilleur_arret_processus",
                        lambda *a: (f.veilleurs.append(a), 5000 + len(f.veilleurs))[1], raising=False)
    monkeypatch.setattr(la, "verifier_veilleur", lambda pid, journal, **kw: True)
    monkeypatch.setattr(la, "arreter_veilleur", lambda pid: f.veilleurs_arretes.append(pid))
    return premiere, c, f


def test_relance_coupee_apres_20_tours_reprise_assemblage_lecture(tmp_path, monkeypatch):
    premiere, c, f = _relance_coupee(tmp_path, monkeypatch, 25)
    bilan = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert bilan["detruite"] is True and f.detruites == ["77"] and bilan["transfert_complet"] is True, bilan
    assert "principal-relance" in bilan["transferts"]
    rep = c.sortie / "reprise-v10"
    scellement.verifier(rep / "bilan-reprise-v10.json")
    cible = tmp_path / "lecture"
    la.assembler_lecture(premiere, rep, cible)
    v = lc.valider(cible)
    assert v["etat"] is None and v["k_prime"] == 25 and v["dossier"].endswith("principal-relance/transfert-1"), v
    roles = sorted(i["role"] for i in v["interruptions"])
    assert len(roles) == 2 and any(r.startswith("première exécution") for r in roles), roles
    res = lc.lire(v, an.graines()["reechantillonnage"])
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 25)"), res


def test_relance_coupee_avant_20_tours_pas_de_verdict(tmp_path, monkeypatch):
    """Artefact : coupure à 12 tours : seconde erreur avant 20 tours (l. 371) : la lecture ne donne pas de verdict."""
    premiere, c, f = _relance_coupee(tmp_path, monkeypatch, 12)
    bilan = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert bilan["detruite"] is True and bilan["transfert_complet"] is True
    cible = tmp_path / "lecture"
    la.assembler_lecture(premiere, c.sortie / "reprise-v10", cible)
    v = lc.valider(cible)
    assert v["etat"] is not None and "pas de verdict" in v["etat"].lower(), v
