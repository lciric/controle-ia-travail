"""Essais du code v2 de la formation du barreau 5 : l'additif 1 au texte scellé, « relance des six instances »
(mot de Lazar, GO-2026-11-20-51). Cas sain et artefact pour chaque garde changée ou neuve (R5) :
- la clé neuve CODE-RELANCE-FORMATION-B5F du registre propre (commit du code des relances, sans entropie) ;
- la ligne de relance, qui exige cette clé et cite l'accord de GO-FORMATION-B5F ;
- le code comparé au commit de la ligne qui vaut pour la marche (première marche ou relance) ;
- les lignes exactes de l'additif.
Les bornes (six instances, 147 USD) et le compteur commun sont éprouvés dans tests/test_barreau5_familles_formation_v1.py
(essais retouchés), la commande de création dans tests/test_lancer_b5f_formation_v1.py. Chaque essai de ce fichier échoue
sur le code v1 (épreuve par retrait, rapport du développeur)."""
from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import formation_v1 as fv
from controle_ia.gardes import GardeArret

RACINE_DEPOT = Path(__file__).resolve().parents[1]
SHA = "f" * 64
V1, V2 = "a" * 40, "b" * 40
GO = "GO-2026-11-19-86"
TEXTE = "prereg/barreau5-texte-v1.md"


def _lignes(code_relance="commit " + V2, instant_code_relance="2026-11-20T13:30:00Z",
            relance=f"{GO} ; instances 1,2,3,4,5,7", instant_relance="2026-11-20T13:31:00Z", sha=SHA):
    """Registre propre de la course, à trois membres : les trois lignes des premières marches, puis, si données, la ligne
    du code des relances et la ligne de relance."""
    lignes = [en.ligne_du_registre("SCELLEMENT-B5F", "2026-11-19T23:47:32Z",
                                   f"{TEXTE} ; sha256 {sha} ; membres-apprentissage 3 ; piece famille", ""),
              en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-20T00:42:04Z", f"commit {V1} ; entropie 123", ""),
              en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-20T00:42:06Z", GO, "")]
    if code_relance is not None:
        lignes.append(en.ligne_du_registre("CODE-RELANCE-FORMATION-B5F", instant_code_relance, code_relance, ""))
    if relance is not None:
        lignes.append(en.ligne_du_registre("GO-RELANCE-FORMATION-B5F", instant_relance, relance, ""))
    return "\n".join(lignes) + "\n"


def _lire(**k):
    return fv.lire_code_et_accord(None, _lignes(**k))


def test_cle_du_code_des_relances_connue_du_registre_cas_sain_et_artefact():
    """La clé neuve est une clé du registre propre ; une clé « -B5F » inconnue arrête toujours le registre entier."""
    assert fv.CLE_CODE_RELANCE == "CODE-RELANCE-FORMATION-B5F" and fv.CLE_CODE_RELANCE in en.CLES_REGISTRE
    ligne = en.ligne_du_registre("CODE-RELANCE-FORMATION-B5F", "2026-11-20T13:30:00Z", "commit " + V2, "référence libre")
    assert en.lignes_du_registre(ligne)["CODE-RELANCE-FORMATION-B5F"]["contenu"] == "commit " + V2
    with pytest.raises(GardeArret, match="clé CODE-RELANCE-B5F inconnue"):
        en.lignes_du_registre(ligne.replace("CODE-RELANCE-FORMATION-B5F", "CODE-RELANCE-B5F"))
    with pytest.raises(GardeArret, match="en double"):
        en.lignes_du_registre(ligne + "\n" + ligne)


def test_lignes_exactes_de_l_additif_les_six_instances_tombees():
    """Les lignes de l'additif 1, lues à la lettre : six instances, 147 USD de coupures à trois membres, accord de la
    formation ; le commit et l'entropie des premières marches ne changent pas."""
    lu = _lire()
    assert lu["relance"] == {"go_id": GO, "instances": [1, 2, 3, 4, 5, 7], "commit": V2}
    assert (lu["commit"], lu["entropie"], lu["go_id"]) == (V1, 123, GO)
    assert sum(fv.coupure_usd(n, 3) for n in lu["relance"]["instances"]) == fv.ENVELOPPE_RELANCE_USD == 147.0
    assert fv.RELANCES_MAX == 6 == len(lu["relance"]["instances"])
    # l'instance 6, finie et versée, n'entre pas : avec elle, sept instances, ou plus de 147 USD
    for instances, motif in (("6,1,2,3,4,5,7", "7 instances citées, 6 au plus"), ("6,1,2,3,4,5", "158 USD > enveloppe")):
        with pytest.raises(GardeArret, match=motif):
            _lire(relance=f"{GO} ; instances {instances}")


def test_ligne_du_code_des_relances_cas_sain_et_artefacts():
    """CODE-RELANCE-FORMATION-B5F : « commit <40 signes> », sans entropie, après GO-FORMATION-B5F ; seule, sans ligne de
    relance, elle ne relance rien."""
    seule = _lire(relance=None)
    assert seule["relance"] is None and (seule["commit"], seule["entropie"]) == (V1, 123)
    assert _lire(code_relance=None, relance=None)["relance"] is None            # registre des premières marches : inchangé
    for contenu in (f"commit {V2} ; entropie 5", "commit " + "b" * 39, V2, "commit " + "B" * 40):
        with pytest.raises(GardeArret, match="CODE-RELANCE-FORMATION-B5F illisible"):
            _lire(code_relance=contenu)
    with pytest.raises(GardeArret, match="CODE-RELANCE-FORMATION-B5F avant GO-FORMATION-B5F"):
        _lire(instant_code_relance="2026-11-20T00:42:05Z", relance=None)


def test_ligne_de_relance_exige_le_code_des_relances_et_l_accord_de_la_formation():
    """GO-RELANCE-FORMATION-B5F : après CODE-RELANCE-FORMATION-B5F, qu'elle exige ; son accord est celui de
    GO-FORMATION-B5F (la relance entre sous le plafond commun de cet accord)."""
    assert _lire(relance=f"{GO} ; instances 3")["relance"] == {"go_id": GO, "instances": [3], "commit": V2}
    with pytest.raises(GardeArret, match="GO-RELANCE-FORMATION-B5F sans CODE-RELANCE-FORMATION-B5F"):
        _lire(code_relance=None)
    with pytest.raises(GardeArret, match="GO-RELANCE-FORMATION-B5F avant CODE-RELANCE-FORMATION-B5F"):
        _lire(instant_relance="2026-11-20T13:29:59Z")
    with pytest.raises(GardeArret, match="GO-RELANCE-FORMATION-B5F avant CODE-RELANCE-FORMATION-B5F"):
        _lire(instant_relance="2026-11-20T13:30:00Z")                            # même instant : l'ordre n'est pas prouvé
    with pytest.raises(GardeArret, match="GO-2026-11-19-87 ≠ accord de GO-FORMATION-B5F GO-2026-11-19-86"):
        _lire(relance="GO-2026-11-19-87 ; instances 3")
    with pytest.raises(GardeArret, match="illisible"):                           # un accord de décision n'est pas un contenu
        _lire(relance="GO-2026-11-19-86, GO-2026-11-20-51 ; instances 3")


def test_commit_du_code_premiere_marche_et_relance_cas_sain_et_artefacts():
    """Une première marche joue le code de CODE-FORMATION-B5F ; une relance, celui de CODE-RELANCE-FORMATION-B5F."""
    lu = _lire()
    assert fv.commit_du_code(lu, False) == (V1, "CODE-FORMATION-B5F")
    assert fv.commit_du_code(lu, True) == (V2, "CODE-RELANCE-FORMATION-B5F")
    sans = _lire(relance=None)
    assert fv.commit_du_code(sans, False) == (V1, "CODE-FORMATION-B5F")
    with pytest.raises(GardeArret, match="relance non accordée"):
        fv.commit_du_code(sans, True)
    for valeur in (1, 0, None, "1"):
        with pytest.raises(GardeArret, match="vrai ou faux"):
            fv.commit_du_code(lu, valeur)


@pytest.fixture
def racine_reelle(tmp_path, monkeypatch):
    """Racine jetable d'une marche réelle : configuration scellée de la course de confirmation (copiée), texte, registre
    propre. Les entrées de la marche (tâches, consignes, invite) ne sont pas chargées ; la comparaison du code est
    remplacée par un témoin qui note ce qu'on lui demande et arrête la marche avant tout manifeste."""
    r = tmp_path / "depot"
    (r / "prereg").mkdir(parents=True)
    (r / "registres").mkdir()
    for f in (fv.CONFIG_SCELLEE["chemin"], fv.CONFIG_SCELLEE["chemin"] + ".sha256"):
        shutil.copy(RACINE_DEPOT / f, r / f)
    (r / TEXTE).write_text("# Texte scellé (essai)\n", encoding="utf-8")
    vus = []

    def temoin(racine, commit, cible="HEAD", cle="CODE-FORMATION-B5F"):
        vus.append((commit, cible, cle))
        raise GardeArret("témoin : comparaison du code demandée")

    for nom in ("charger_taches_b5f", "charger_consignes", "charger_invite"):
        monkeypatch.setattr(fv, nom, lambda *a, **k: None)
    monkeypatch.setattr(fv, "exiger_code_au_commit", temoin)
    return r, vus


def _marche(r, en_relance, **registre):
    (r / fv.REGISTRE_PROPRE).write_text(_lignes(sha=fv.empreinte(r / TEXTE), **registre), encoding="utf-8")
    config = fv.config_instance(3, r, GO, 1.1, 3, "famille", en_relance)
    return fv.executer(config, r, "20261120-140000-b5f-formation-3" + ("-x1" if en_relance else ""), prereg=TEXTE)


def test_marche_reelle_compare_le_code_au_commit_de_sa_ligne_cas_sain_et_artefacts(racine_reelle):
    """Sur l'instance : la relance compare son code au commit de CODE-RELANCE-FORMATION-B5F, la première marche à celui de
    CODE-FORMATION-B5F ; une relance que la ligne ne cite pas, ou sans ligne de relance, s'arrête avant."""
    r, vus = racine_reelle
    with pytest.raises(GardeArret, match="témoin"):
        _marche(r, True)
    assert vus == [(V2, "HEAD", "CODE-RELANCE-FORMATION-B5F")]
    vus.clear()
    with pytest.raises(GardeArret, match="témoin"):
        _marche(r, False)
    assert vus == [(V1, "HEAD", "CODE-FORMATION-B5F")]
    vus.clear()
    with pytest.raises(GardeArret, match="relance de l'instance 3 non accordée"):
        _marche(r, True, relance=f"{GO} ; instances 1,2")
    with pytest.raises(GardeArret, match="non accordée"):
        _marche(r, True, relance=None)
    assert vus == [] and not (r / "runs").exists()


def test_message_de_la_comparaison_du_code_nomme_la_ligne(tmp_path):
    """Le refus nomme la ligne dont le commit est comparé (dépôt sans ce commit : refus dans les deux cas)."""
    import subprocess

    subprocess.run(["git", "-C", str(tmp_path), "init", "-q"], check=True)
    with pytest.raises(GardeArret, match="celui de CODE-RELANCE-FORMATION-B5F bbbbbbbbbbbb"):
        fv.exiger_code_au_commit(tmp_path, V2, cle=fv.CLE_CODE_RELANCE)
    with pytest.raises(GardeArret, match="celui de CODE-FORMATION-B5F aaaaaaaaaaaa"):
        fv.exiger_code_au_commit(tmp_path, V1)
    with pytest.raises(GardeArret, match="différent du code de CODE-RELANCE-FORMATION-B5F bbbbbbbbbbbb"):
        fv.exiger_code_de_la_session(tmp_path, V2, fv.CLE_CODE_RELANCE)
