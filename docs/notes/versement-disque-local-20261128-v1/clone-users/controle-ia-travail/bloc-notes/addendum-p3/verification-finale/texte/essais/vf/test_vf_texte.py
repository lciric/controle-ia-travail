"""Essais de la vérification finale « texte face au code » (VF1), sur une copie octet pour octet du module final et de
ses tests (`../base/`). Chaque essai PASSE quand il reproduit le constat qu'il porte (écart entre le texte final et le
code) ; les aides de données sont celles des tests du module (importées, jamais copiées)."""
import copy
import hashlib
import sys
from pathlib import Path

import pytest

BASE = Path(__file__).resolve().parent.parent / "base"
sys.path.insert(0, str(BASE))

import test_complements_p3_v1 as T  # noqa: E402
from test_complements_p3_v1 import G, P, _c, _D, cp, lp  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402


@pytest.fixture(autouse=True)
def tirages_reduits(monkeypatch):
    monkeypatch.setattr(cp, "TIRAGES_AIRE", T.TIRAGES_TESTS)
    monkeypatch.setattr(cp, "TIRAGES_COUT", 2000)


def test_copie_egale_au_module_final():
    assert hashlib.sha256((BASE / "complements_p3_v1.py").read_bytes()).hexdigest() == (
        "2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996")
    assert hashlib.sha256((BASE / "test_complements_p3_v1.py").read_bytes()).hexdigest() == (
        "7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d")


def _vides():
    return {a: ({"etat": "calculé", "controles": []} if a in cp.SANS_SONDE else
                {p: {"etat": "calculé", "controles": []} for p in P}) for a in cp.ANALYSES}


def test_precision_8_aucune_reserve_possible_et_declencheur_vrai():
    """Précision 8 : « sans aucune réserve possible, le déclencheur est faux ». La synthèse le tient pour « toutes »,
    pas pour « aucune » : zéro réserve possible, trois conclusions établies, audit R4 déclenché → déclencheur vrai."""
    etablies = ["P3-P1", _c("P3-P3"), _c("P3-P4")]
    s = cp.synthese(_vides(), etablies, True)
    a = s["audit_symetrie_addendum"]
    print("audit :", a)
    assert a["reserves_possibles"] == 0 and a["declencheur"] is True
    # garde-fou : sans audit R4, faux (la règle « aucune » seule est en cause)
    assert cp.synthese(_vides(), etablies, False)["audit_symetrie_addendum"]["declencheur"] is False


def test_precision_17_non_lu_ajoute_alors_que_tous_les_controles_sont_faits(monkeypatch):
    """Précision 17 : « seuls les contrôles non faits deviennent « non lus » ». Une `GardeArret` levée hors d'un calcul
    APRÈS les sept contrôles de A1 (placebo, descriptif) : aucun contrôle n'est « non fait », pourtant chaque cible visée
    par A1 reçoit un contrôle « non lu » et la recommandation dit « non contrôlée par l'addendum » pour P3-P3."""
    D = _D("a1_plancher")
    sain = cp._executer_entree("A1", P[0], D, G)
    faits = {(c["test"], c["cible"]) for c in sain["controles"]}
    assert len(sain["controles"]) == 7 and all(c["controle_contraire"] != "non lu" for c in sain["controles"])
    monkeypatch.setattr(cp.lp, "_permuter_dans_les_taches",
                        lambda *a: (_ for _ in ()).throw(GardeArret("échec simulé après les contrôles")))
    x = cp._executer_entree("A1", P[0], D, G)
    ajoutes = [c for c in x["controles"] if (c["test"], c["cible"]) not in faits]
    print("contrôles ajoutés :", [(c["test"], c["cible"], c["controle_contraire"], c.get("reserve")) for c in ajoutes])
    assert x["controles"][:7] == sain["controles"]
    assert ajoutes and all(c["controle_contraire"] in ("non lu", "sans objet") for c in ajoutes)
    assert any(c["controle_contraire"] == "non lu" and c["cible"] == _c("P3-P3") for c in ajoutes)
    analyses = _vides()
    analyses["A1"][P[0]] = x
    s = cp.synthese(analyses, D["etablies"], False)
    rec = [r for r in s["recommandation_au_verdict_R13"] if r.startswith(_c("P3-P3") + " :")]
    print("recommandation P3-P3 :", rec)
    assert any("non contrôlée par l'addendum (réserves : reserve_A1_non_lue)" in r for r in rec)


def test_precision_17_valeur_non_finie_du_descriptif_apres_les_controles(monkeypatch):
    """Même écart par le chemin que la précision 17 nomme (valeur non finie du descriptif, `_propre`) : A8 a fait ses
    contrôles ; une valeur non finie du descriptif rend l'entrée « échec » et ajoute un « non lu » sur P3-P3."""
    D = _D("sain")
    vraie = cp.FONCTIONS["A8"]

    def a8_puis_nan(e, D_, g, p):
        vraie(e, D_, g, p)
        e.descriptif["valeur_non_finie"] = float("nan")

    sain = cp._executer_entree("A8", P[0], D, G)
    monkeypatch.setitem(cp.FONCTIONS, "A8", a8_puis_nan)
    x = cp._executer_entree("A8", P[0], D, G)
    n = len(sain["controles"])
    print("contrôles :", [(c["test"], c["controle_contraire"], c.get("reserve")) for c in x["controles"]])
    assert x["controles"][:n] == sain["controles"]
    assert [c["controle_contraire"] for c in x["controles"][n:]] == ["non lu"]


def test_garde_15_graines_controlees_apres_la_creation_du_manifeste(monkeypatch, tmp_path):
    """Plan, point 3, et liste d'arrêt : « gardes 1 à 10 et 12 à 16 avant la création du manifeste ». La partie
    « graines » de la garde 15 (`exiger_graines`) est appelée dans `analyser_addendum`, donc après `creer_manifeste` :
    un arrêt à cette garde est écrit dans la sortie et consomme le seul passage. Ordre relevé avec des remplaçants pour
    tout ce qui précède (aucune donnée), `exiger_graines` réelle."""
    ordre = []
    m = cp
    for nom in ("exiger_commande", "exiger_anteriorite", "charger_textes", "exiger_coherence", "familles_attention",
                "localisation"):
        monkeypatch.setattr(m, nom, (lambda n: (lambda *a, **k: ordre.append(n)))(nom))
    monkeypatch.setattr(m, "exiger_garde_1", lambda *a, **k: ordre.append("garde 1") or {
        "sha_prereg": "0", "sha_module": "0", "sha_tests": "0", "commit_cite": "0"})
    monkeypatch.setattr(m, "exiger_lecture_decisive", lambda *a, **k: ordre.append("garde 2") or {
        "commit_lecture": "0", "manifestes_ecartes": []})
    monkeypatch.setattr(m.lp, "charger_source", lambda *a, **k: ordre.append("garde 4") or {
        "sondes-figees": {"principales": {"tromperie": "p0", "enjeux": "p1"}}})
    monkeypatch.setattr(m, "verifier_resultat", lambda *a, **k: {"resultat": {"issue": {"ligne": "x"}}})
    monkeypatch.setattr(m, "controler_entrees", lambda *a, **k: ordre.append("gardes 5 à 8") or (
        {"principales": ["p0", "p1"]}, {}))
    monkeypatch.setattr(m, "exiger_premier_passage", lambda *a, **k: ordre.append("garde 9") or [])
    graines_alterees = m.graines_des_cles(m.cles_addendum(["p0", "p1"]), m.ENTROPIE_P3)
    k0 = next(iter(graines_alterees))
    graines_alterees[k0] = dict(graines_alterees[k0], spawn_key=["1"])
    monkeypatch.setattr(m, "creer_manifeste", lambda *a, **k: ordre.append("creer_manifeste") or (
        tmp_path / "manifeste.json", {"graines": graines_alterees}))
    monkeypatch.setattr(m, "verifier", lambda *a, **k: "0")
    monkeypatch.setattr(m, "_donnees", lambda source: {"principales": ["p0", "p1"]})
    vraie = m.exiger_graines

    def graines_tracees(*a, **k):
        ordre.append("garde 15 (graines)")
        return vraie(*a, **k)

    monkeypatch.setattr(m, "exiger_graines", graines_tracees)
    ecrit = {}
    monkeypatch.setattr(m, "ecrire_resultat", lambda r, c, nom, contenu: ordre.append("sortie écrite") or ecrit.update(
        contenu))
    with pytest.raises(GardeArret, match="garde 15 : graines de l'addendum autres que celles de leurs clés"):
        m.executer(tmp_path, "run", "lec", "20261020-120000-addendum-p3", m.PREREG_ADDENDUM, m.ENTROPIE_P3)
    print("ordre :", ordre)
    print("arrêt écrit :", ecrit.get("arret"))
    assert ordre.index("creer_manifeste") < ordre.index("garde 15 (graines)") < ordre.index("sortie écrite")
    assert "garde 15" in ecrit["arret"]
