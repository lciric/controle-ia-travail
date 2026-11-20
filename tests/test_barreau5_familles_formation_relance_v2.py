"""Essais du code v2 de la formation du barreau 5 : l'additif 1 au texte scellé, « relance des six instances »
(mot de Lazar, GO-2026-11-20-51), corrigés après la contre-lecture du code (couples 1 à 4). Cas sain et artefact pour
chaque garde changée ou neuve (R5) :
- aucune clé neuve au registre propre : le fichier `engagement_v1.py` est celui du code de lecture figé, à l'octet, et le
  registre final se lit par son lecteur ;
- le commit du code des relances, écrit une seule fois dans la colonne de référence de la ligne de relance ;
- la ligne de relance : accord de GO-FORMATION-B5F, instances tombées seulement ;
- le code comparé au commit qui vaut pour la marche (première marche ou relance), et la filiation du code des relances.
Les bornes (six instances, 147 USD) et le compteur commun sont éprouvés dans tests/test_barreau5_familles_formation_v1.py
(essais retouchés), la commande de création dans tests/test_lancer_b5f_formation_v1.py. Chaque essai de ce fichier échoue
sur le code v1 (épreuve par retrait, rapport du développeur)."""
from __future__ import annotations

import hashlib
import shutil
import subprocess
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
CONTENU = f"{GO} ; instances 1,2,3,4,5,7"
REF = f"mot de Lazar GO-2026-11-20-51 ; additif 1 ; code des relances commit {V2} ; cumul commun relevé"
# empreinte de `engagement_v1.py` au commit de CODE-FORMATION-B5F et au commit de CODE-LECTURE-B5F (même fichier)
ENGAGEMENT_FIGE_SHA256 = "565d4e51eccd82562f3f00e7bd020beba525ac09b782905151a38e72ca536396"


def _lignes(contenu=CONTENU, ref=REF, instant_relance="2026-11-20T15:00:00Z", sha=SHA, lecture=True):
    """Registre propre de la course, à trois membres : les cinq lignes déjà inscrites (formation, puis code de lecture et
    épreuve à vérité plantée), puis, si son contenu est donné, la ligne de relance."""
    lignes = [en.ligne_du_registre("SCELLEMENT-B5F", "2026-11-19T23:47:32Z",
                                   f"{TEXTE} ; sha256 {sha} ; membres-apprentissage 3 ; piece famille", ""),
              en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-20T00:42:04Z", f"commit {V1} ; entropie 123", ""),
              en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-20T00:42:06Z", GO, "")]
    if lecture:
        lignes += [en.ligne_du_registre("CODE-LECTURE-B5F", "2026-11-20T07:43:13Z",
                                        "commit " + "c" * 40 + " ; lecture sha256 " + "e" * 64, ""),
                   en.ligne_du_registre("EPREUVE-B5F", "2026-11-20T11:28:24Z",
                                        "passee ; lecture sha256 " + "e" * 64 + " ; rapport sha256 " + "d" * 64, "")]
    if contenu is not None:
        lignes.append(en.ligne_du_registre("GO-RELANCE-FORMATION-B5F", instant_relance, contenu, ref))
    return "\n".join(lignes) + "\n"


def _lire(**k):
    return fv.lire_code_et_accord(None, _lignes(**k))


def test_aucune_cle_neuve_le_registre_final_se_lit_par_le_lecteur_du_code_de_lecture_fige():
    """Couple 1 de la contre-lecture : `engagement_v1.py` est, à l'octet, le fichier du code de lecture figé ; son lecteur
    accepte le registre final (cinq lignes inscrites, plus la ligne de relance et sa référence) et y lit le contenu
    inchangé ; une clé du code des relances, elle, ferait refuser le registre entier."""
    fichier = Path(en.__file__)
    assert hashlib.sha256(fichier.read_bytes()).hexdigest() == ENGAGEMENT_FIGE_SHA256
    assert "CODE-RELANCE-FORMATION-B5F" not in en.CLES_REGISTRE
    lues = en.lignes_du_registre(_lignes())
    assert list(lues) == ["SCELLEMENT-B5F", "CODE-FORMATION-B5F", "GO-FORMATION-B5F", "CODE-LECTURE-B5F", "EPREUVE-B5F",
                          "GO-RELANCE-FORMATION-B5F"]
    assert lues["GO-RELANCE-FORMATION-B5F"]["contenu"] == CONTENU and lues["GO-RELANCE-FORMATION-B5F"]["ref"] == REF
    assert fv.lire_code_et_accord(None, _lignes())["relance"] == {"go_id": GO, "instances": [1, 2, 3, 4, 5, 7],
                                                                  "commit": V2}
    with pytest.raises(GardeArret, match="clé CODE-RELANCE-FORMATION-B5F inconnue"):
        fv.lire_code_et_accord(None, _lignes() + f"| CODE-RELANCE-FORMATION-B5F | 2026-11-20T15:00:01Z | commit {V2} | |\n")


def test_ligne_exacte_de_l_additif_les_six_instances_tombees():
    """La ligne de l'additif 1, lue à la lettre : six instances, 147 USD de coupures à trois membres, accord de la
    formation, code des relances en référence ; le commit et l'entropie des premières marches ne changent pas ; les
    lignes du code de lecture et de l'épreuve ne gênent pas (couple 2)."""
    lu = _lire()
    assert lu["relance"] == {"go_id": GO, "instances": [1, 2, 3, 4, 5, 7], "commit": V2}
    assert (lu["commit"], lu["entropie"], lu["go_id"]) == (V1, 123, GO)
    assert _lire(lecture=False) == lu
    assert sum(fv.coupure_usd(n, 3) for n in lu["relance"]["instances"]) == fv.ENVELOPPE_RELANCE_USD == 147.0
    assert fv.RELANCES_MAX == 6 == len(lu["relance"]["instances"])
    assert tuple(lu["relance"]["instances"]) == fv.INSTANCES_TOMBEES
    sans = _lire(contenu=None)
    assert sans["relance"] is None and (sans["commit"], sans["entropie"]) == (V1, 123)


def test_instances_tombees_seulement_cas_sain_et_artefacts():
    """Couple 3 : la ligne de relance ne cite que des instances tombées (1, 2, 3, 4, 5, 7) ; l'instance 6, finie et
    versée, ne se relance pas."""
    for instances in ("1,2,3,4,5,7", "7,3", "1", "7"):
        assert _lire(contenu=f"{GO} ; instances {instances}")["relance"]["instances"] == [int(x) for x in
                                                                                         instances.split(",")]
    for instances in ("6", "6,7", "1,6", "6,1,2,3,4"):
        with pytest.raises(GardeArret, match=r"instance non tombée citée \[6\]"):
            _lire(contenu=f"{GO} ; instances {instances}")
    for instances, motif in (("6,1,2,3,4,5,7", "7 instances citées, 6 au plus"), ("6,1,2,3,4,5", "158 USD > enveloppe")):
        with pytest.raises(GardeArret, match=motif):
            _lire(contenu=f"{GO} ; instances {instances}")


def test_code_des_relances_dans_la_reference_cas_sain_et_artefacts():
    """Couple 1 : la référence de la ligne de relance porte, une et une seule fois, « code des relances commit <40
    signes> », entre « ; » ou aux bords ; ce commit n'est pas celui de CODE-FORMATION-B5F."""
    for ref in (f"code des relances commit {V2}", f"code des relances commit {V2} ; additif 1",
                f"GO-2026-11-20-51 ; code des relances commit {V2}", REF):
        assert _lire(ref=ref)["relance"]["commit"] == V2
    artefacts = ["", "mot de Lazar GO-2026-11-20-51 ; additif 1",                                  # aucune mention
                 f"code des relances commit {V2} ; code des relances commit {V2}",                 # deux mentions
                 f"code des relances commit {V2} ; code des relances commit {'c' * 40}",
                 f"code des relances commit {V2} ; voir le code des relances",                     # une mention de trop
                 f"code des relances commit {'b' * 39}", f"code des relances commit {'b' * 41}",   # 39 et 41 signes
                 f"code des relances commit {'B' * 40}",                                           # majuscules
                 f"code des relances {V2}", f"code des relances commit  {V2}",                     # sans « commit » ; espace
                 f"additif 1, code des relances commit {V2}",                                      # hors des « ; »
                 f"code des relances commit {V2}, additif 1",
                 f"commit {V2}"]
    for ref in artefacts:
        with pytest.raises(GardeArret, match="une et une seule mention « code des relances commit"):
            _lire(ref=ref)
    with pytest.raises(GardeArret, match="le code des relances est celui des premières marches"):
        _lire(ref=f"code des relances commit {V1}")
    with pytest.raises(GardeArret, match="GO-RELANCE-FORMATION-B5F illisible"):                     # dans le contenu : refus
        _lire(contenu=f"{CONTENU} ; code des relances commit {V2}", ref="")


def test_ligne_de_relance_cite_l_accord_de_la_formation_cas_sain_et_artefacts():
    """GO-RELANCE-FORMATION-B5F cite l'accord de GO-FORMATION-B5F (la relance entre sous le plafond commun de cet
    accord), après lui."""
    assert _lire(contenu=f"{GO} ; instances 3")["relance"] == {"go_id": GO, "instances": [3], "commit": V2}
    with pytest.raises(GardeArret, match="GO-2026-11-19-87 ≠ accord de GO-FORMATION-B5F GO-2026-11-19-86"):
        _lire(contenu="GO-2026-11-19-87 ; instances 3")
    with pytest.raises(GardeArret, match="illisible"):                           # un accord de décision n'est pas un contenu
        _lire(contenu="GO-2026-11-19-86, GO-2026-11-20-51 ; instances 3")
    with pytest.raises(GardeArret, match="GO-RELANCE-FORMATION-B5F avant GO-FORMATION-B5F"):
        _lire(instant_relance="2026-11-20T00:42:06Z", lecture=False)


def test_commit_du_code_premiere_marche_et_relance_cas_sain_et_artefacts():
    """Une première marche joue le code de CODE-FORMATION-B5F ; une relance, le code des relances de la ligne de
    relance."""
    lu = _lire()
    assert fv.commit_du_code(lu, False) == (V1, "CODE-FORMATION-B5F")
    assert fv.commit_du_code(lu, True) == (V2, "GO-RELANCE-FORMATION-B5F (code des relances)")
    sans = _lire(contenu=None)
    assert fv.commit_du_code(sans, False) == (V1, "CODE-FORMATION-B5F")
    with pytest.raises(GardeArret, match="relance non accordée"):
        fv.commit_du_code(sans, True)
    for valeur in (1, 0, None, "1"):
        with pytest.raises(GardeArret, match="vrai ou faux"):
            fv.commit_du_code(lu, valeur)


def _git(r, *args):
    return subprocess.run(["git", "-C", str(r), *args], check=True, capture_output=True, text=True).stdout.strip()


def test_filiation_du_code_des_relances_cas_sain_et_artefacts(tmp_path):
    """Couple 4 : le commit de CODE-FORMATION-B5F est un ancêtre du code des relances ; un commit d'une autre lignée, un
    ordre inversé ou un commit absent sont refusés."""
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "essai@invalid")
    _git(tmp_path, "config", "user.name", "essai")
    commits = {}
    for nom in ("v1", "v2"):
        (tmp_path / "code.py").write_text(f"VERSION = '{nom}'\n", encoding="utf-8")
        _git(tmp_path, "add", "-A")
        _git(tmp_path, "commit", "-q", "-m", nom)
        commits[nom] = _git(tmp_path, "rev-parse", "HEAD")
    _git(tmp_path, "checkout", "-q", "--orphan", "ailleurs")
    _git(tmp_path, "commit", "-q", "-m", "autre lignée")
    commits["ailleurs"] = _git(tmp_path, "rev-parse", "HEAD")

    def lu(v1, v2):
        return {"commit": commits.get(v1, v1), "relance": {"commit": commits.get(v2, v2)}}

    fv.exiger_filiation_du_code_des_relances(tmp_path, lu("v1", "v2"))
    for v1, v2 in (("v2", "v1"), ("v1", "ailleurs"), ("v1", V2), (V1, "v2")):
        with pytest.raises(GardeArret, match="ne descend pas du code de CODE-FORMATION-B5F"):
            fv.exiger_filiation_du_code_des_relances(tmp_path, lu(v1, v2))
    with pytest.raises(GardeArret, match="relance non accordée"):
        fv.exiger_filiation_du_code_des_relances(tmp_path, {"commit": commits["v1"], "relance": None})


@pytest.fixture
def racine_reelle(tmp_path, monkeypatch):
    """Racine jetable d'une marche réelle : configuration scellée de la course de confirmation (copiée), texte, registre
    propre. Les entrées de la marche (tâches, consignes, invite) ne sont pas chargées ; la filiation et la comparaison du
    code sont remplacées par des témoins qui notent ce qu'on leur demande ; le second arrête la marche avant tout
    manifeste."""
    r = tmp_path / "depot"
    (r / "prereg").mkdir(parents=True)
    (r / "registres").mkdir()
    for f in (fv.CONFIG_SCELLEE["chemin"], fv.CONFIG_SCELLEE["chemin"] + ".sha256"):
        shutil.copy(RACINE_DEPOT / f, r / f)
    (r / TEXTE).write_text("# Texte scellé (essai)\n", encoding="utf-8")
    vus = []

    def temoin(racine, commit, cible="HEAD", cle="CODE-FORMATION-B5F"):
        vus.append(("code", commit, cible, cle))
        raise GardeArret("témoin : comparaison du code demandée")

    for nom in ("charger_taches_b5f", "charger_consignes", "charger_invite"):
        monkeypatch.setattr(fv, nom, lambda *a, **k: None)
    monkeypatch.setattr(fv, "exiger_filiation_du_code_des_relances",
                        lambda racine, lu: vus.append(("filiation", lu["commit"], lu["relance"]["commit"])))
    monkeypatch.setattr(fv, "exiger_code_au_commit", temoin)
    return r, vus


def _marche(r, en_relance, **registre):
    (r / fv.REGISTRE_PROPRE).write_text(_lignes(sha=fv.empreinte(r / TEXTE), **registre), encoding="utf-8")
    config = fv.config_instance(3, r, GO, 1.1, 3, "famille", en_relance)
    return fv.executer(config, r, "20261120-140000-b5f-formation-3" + ("-x1" if en_relance else ""), prereg=TEXTE)


def test_marche_reelle_compare_le_code_au_commit_de_sa_ligne_cas_sain_et_artefacts(racine_reelle):
    """Sur l'instance : la relance exige la filiation, puis compare son code au code des relances ; la première marche se
    compare au commit de CODE-FORMATION-B5F, sans filiation ; une relance que la ligne ne cite pas, ou sans ligne de
    relance, s'arrête avant."""
    r, vus = racine_reelle
    with pytest.raises(GardeArret, match="témoin"):
        _marche(r, True)
    assert vus == [("filiation", V1, V2), ("code", V2, "HEAD", "GO-RELANCE-FORMATION-B5F (code des relances)")]
    vus.clear()
    with pytest.raises(GardeArret, match="témoin"):
        _marche(r, False)
    assert vus == [("code", V1, "HEAD", "CODE-FORMATION-B5F")]
    vus.clear()
    with pytest.raises(GardeArret, match="relance de l'instance 3 non accordée"):
        _marche(r, True, contenu=f"{GO} ; instances 1,2")
    with pytest.raises(GardeArret, match="non accordée"):
        _marche(r, True, contenu=None)
    assert vus == [] and not (r / "runs").exists()


def test_message_de_la_comparaison_du_code_nomme_la_ligne(tmp_path):
    """Le refus nomme la ligne dont le commit est comparé (dépôt sans ce commit : refus dans les deux cas)."""
    subprocess.run(["git", "-C", str(tmp_path), "init", "-q"], check=True)
    with pytest.raises(GardeArret, match=r"celui de GO-RELANCE-FORMATION-B5F \(code des relances\) bbbbbbbbbbbb"):
        fv.exiger_code_au_commit(tmp_path, V2, cle=fv.CLE_CODE_RELANCE)
    with pytest.raises(GardeArret, match="celui de CODE-FORMATION-B5F aaaaaaaaaaaa"):
        fv.exiger_code_au_commit(tmp_path, V1)
    with pytest.raises(GardeArret, match=r"différent du code de GO-RELANCE-FORMATION-B5F \(code des relances\) bbbbbbbbbbbb"):
        fv.exiger_code_de_la_session(tmp_path, V2, fv.CLE_CODE_RELANCE)
