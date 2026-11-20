"""Essais du programme des étapes 3, 4, 5 et 6 (`lancer_etapes_3_5_6_v1.py`), sous la couche « essai-de-forme » seule, sur une
racine factice (texte présenté, registre des GO, pièce d'autorisation du verrou, pièce de contrôle de la mère, tous factices,
dans un dossier temporaire) ; la copie du code de l'organisme est celle que donne `HERITAGE_COPIE_ORGANISME`. Chaque garde a
son cas sain et son artefact (règle R5) : pièces absentes ou incomplètes, couche interdite, tailles réduites sous les couches
des étapes, dossier déjà présent, copie de l'organisme absente ou altérée, arrêt de l'étape 3, fichier gelé de l'étape 5
altéré après son scellement, arrêt de l'étape 6. Les arrêts d'étape sont plantés (fonctions du code v6 remplacées, le temps d'un
essai, par des fonctions qui arrêtent), jamais tirés. L'essai final contrôle qu'aucune graine d'une autre couche que
« essai-de-forme » n'a été dérivée. Lancement : dossier courant, une copie du code v6 ; `PYTHONPATH=src`."""

import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys

import pytest

from controle_ia.heritage_etage_processeur_v1 import constantes as K
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1 import organisme as OR
from controle_ia.heritage_etage_processeur_v1 import tirages as TI

CHEMIN_PROGRAMME = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "lancer_etapes_3_5_6_v1.py")
_spec = importlib.util.spec_from_file_location("lancer_etapes_3_5_6_v1", CHEMIN_PROGRAMME)
PR = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(PR)

COMMIT = "0123456789abcdef0123456789abcdef01234567"
GO = "GO-2099-01-01-01"
COUCHE = "essai-de-forme"
REDUIT = dict(couche=COUCHE, suites_par_dose=4, permutations=20, doses_etape_4=(0.5,), proposeurs=("lecteur-heritage", "copieur"),
              sources_etape_4=1, sous_ensemble=1, sources_etalonnage=2000)
FREQUENCES = {"p_tient_vraie_source": 1.0, "p_tient_vraie_cible": 1.0, "p_tient_fausse": 0.15, "p_tient_non_plantee_base": 0.02,
              "p_tient_non_plantee_composition": 0.8, "p_tient_non_plantee_copie": 0.05, "p_passage_vraie": 1.0,
              "p_faux_passage": 0.4}
COMPTES = {"vraie-source": {"engagees": 4, "tiennent": 4},
           "criblage": {"vraies_examinees": 2, "vraies_retenues": 2, "autres_examinees": 5, "autres_passees": 2},
           "tentatives_par_classe": {c: 1 for c in K.CLASSES}}


def _copie():
    v = os.environ.get("HERITAGE_COPIE_ORGANISME")
    if not v or not os.path.isdir(v):
        pytest.fail("HERITAGE_COPIE_ORGANISME absente : l'essai ne se joue pas sans elle (R5)")
    return v


def _sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _ecrire(chemin, texte, sceller=True):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(texte)
    if sceller:
        with open(chemin + ".sha256", "w", encoding="utf-8") as f:
            f.write(f"{_sha(chemin)}  {os.path.basename(chemin)}\n")
    return _sha(chemin)


def _table_des_modules():
    paquet = os.path.dirname(os.path.abspath(GR.__file__))
    lignes = [f"  {_sha(os.path.join(paquet, f))}  src/controle_ia/heritage_etage_processeur_v1/{f}"
              for f in sorted(os.listdir(paquet)) if f.endswith(".py")]
    return lignes + [f"  {_sha(os.path.join(os.path.dirname(paquet), '__init__.py'))}  src/controle_ia/__init__.py"]


def _racine(base, controle=None, piece=True, controle_scelle=True):
    racine = str(base / "racine")
    texte = os.path.join(racine, "prereg", "texte-factice-v1.md")
    sha_texte = _ecrire(texte, "\n".join(["# Texte factice", "", f"- Commit du code d'analyse : **`{COMMIT}`** (factice).", "",
                                          "  ```"] + _table_des_modules() + ["  ```", ""]))
    _ecrire(os.path.join(racine, "registres", "go.md"),
            f"# Registre factice\n\n| id | quoi |\n|---|---|\n| {GO} | essai du programme des étapes 3 à 6 |\n", False)
    if piece:
        _ecrire(os.path.join(racine, K.CHEMIN_PIECE_D_AUTORISATION),
                f"identifiant du GO : {GO}\ncommit du code : {COMMIT}\nempreinte du texte scellé : {sha_texte}\n"
                "heure : 2026-11-20T18:40:00Z\n")
    if controle is None:
        controle = (f"| point | attendu | constaté |\n|---|---|---|\n| commit du code | {COMMIT} | {COMMIT} |\n"
                    f"| programme des étapes 3 à 6 | {PR.empreinte_du_programme()} | idem |\n")
    if controle is not False:
        _ecrire(os.path.join(racine, PR.CHEMIN_PIECE_DE_CONTROLE), controle, controle_scelle)
    return racine, texte


def _manifeste(d):
    m = os.path.join(d, "manifeste.json")
    return json.load(open(m, encoding="utf-8")), TI.verifier_manifeste(m)


@pytest.fixture(scope="module")
def chaine(tmp_path_factory):
    """La chaîne entière, réduite, sous la couche « essai-de-forme » (étape 3 : quatre suites par dose, 20 permutations ;
    étape 4 : deux proposeurs, dose 0,5, une source, garde 17 jouée sur elle, et le jeu de la garde 27 ; étape 6 : 2 000 sources
    d'étalonnage)."""
    base = tmp_path_factory.mktemp("chaine")
    racine, texte = _racine(base)
    g_avant = len(GR.JOURNAL)
    r = PR.lancer(texte, racine, _copie(), str(base / "sortie"), **REDUIT)
    return {"r": r, "texte": texte, "journal": GR.JOURNAL[g_avant:]}


def test_chaine_entiere_reduite_sous_essai_de_forme(chaine):
    """Cas sain : les étapes 3, 4, 5 et 6 dans cet ordre, chacune avec son manifeste scellé et vérifié (commit de la pièce,
    empreinte du programme, issue « tenue ») ; rapport de l'audit scellé ; résultat de l'étape 4 scellé (garde 17 jouée) ;
    fichier des fréquences gelé, relu sous contrôle de son empreinte, inscrit aux manifestes des étapes 5 et 6 ; fichier des
    réglages gelé avec son compagnon ; toutes les étiquettes de la couche « essai-de-forme », dans l'ordre des étapes."""
    r = chaine["r"]
    d = r["dossier"]
    assert sorted(x for x in os.listdir(d)) == ["etape-3", "etape-4", "etape-5", "etape-6"]
    for e in ("3", "4", "5", "6"):
        m, n = _manifeste(os.path.join(d, f"etape-{e}"))
        assert m["configuration"]["etape"] == e and m["configuration"]["issue"] == "tenue" and m["commit"] == COMMIT
        assert m["configuration"]["programme_sha256"] == PR.empreinte_du_programme() and m["texte_sha256"] == _sha(chaine["texte"])
        assert (n == 0) == (e == "5") and m["etiquettes"]["couches"] == ([] if e == "5" else ["couche=essai-de-forme"])
        assert not os.path.exists(os.path.join(d, f"etape-{e}", "arret.txt"))
    chemin_f, sha_f = r["frequences"]
    chemin_r, sha_r = r["reglages"]
    assert _sha(chemin_f) == sha_f and open(chemin_f + ".sha256").read().split()[0] == sha_f
    assert _sha(chemin_r) == sha_r and open(chemin_r + ".sha256").read().split()[0] == sha_r
    assert _manifeste(os.path.join(d, "etape-5"))[0]["fichiers_geles"] == {"frequences": sha_f}
    m6 = _manifeste(os.path.join(d, "etape-6"))[0]
    assert m6["fichiers_geles"] == {"frequences": sha_f} and m6["configuration"]["reglages_sha256"] == sha_r
    for f in ("etape-3/rapport-audit-du-generateur.json", "etape-4/resultat-etape-4.json"):
        assert _sha(os.path.join(d, f)) == open(os.path.join(d, f) + ".sha256").read().split()[0]
    assert json.load(open(os.path.join(d, "etape-4", "resultat-etape-4.json")))["garde_17"]["tentatives_comparees"] > 0
    familles = [e.split("|")[1] for _, e in chaine["journal"]]
    assert all(GR.couche_de(e) == COUCHE for _, e in chaine["journal"])
    premier = {f: familles.index(f) for f in ("famille=organisme", "famille=audit", "famille=etape-4", "famille=etalonnage")}
    assert premier["famille=organisme"] < premier["famille=audit"] < premier["famille=etape-4"] < premier["famille=etalonnage"]


@pytest.mark.parametrize("cas", ["piece-d-autorisation-absente", "piece-de-controle-absente", "piece-de-controle-non-scellee",
                                 "controle-sans-empreinte-du-programme", "controle-sans-commit"])
def test_pieces_absentes_ou_incompletes(cas, tmp_path):
    """Artefacts : refus avant tout geste, aucun dossier, aucune graine."""
    kw = {"piece-d-autorisation-absente": {"piece": False}, "piece-de-controle-absente": {"controle": False},
          "piece-de-controle-non-scellee": {"controle_scelle": False},
          "controle-sans-empreinte-du-programme": {"controle": f"| commit | {COMMIT} |\n"},
          "controle-sans-commit": {"controle": f"| programme | {PR.empreinte_du_programme()} |\n"}}[cas]
    racine, texte = _racine(tmp_path, **kw)
    journal = list(GR.JOURNAL)
    with pytest.raises((GR.GraineRefusee, PR.ArretProgramme)):
        PR.lancer(texte, racine, _copie(), str(tmp_path / "sortie"), **REDUIT)
    assert not os.path.exists(tmp_path / "sortie") and GR.JOURNAL == journal


@pytest.mark.parametrize("couche", ["audit", "mecanique", "etalonnage", "decisif", "confirmation", "essai", "inconnue"])
def test_couche_interdite(couche, tmp_path):
    """Artefacts : aucune couche n'est donnée par l'appelant, hors de « essai-de-forme » pour les essais : arrêt avant tout
    geste, ni pièce lue, ni graine, ni refus consigné, ni dossier."""
    racine, texte = _racine(tmp_path)
    journal, refus = list(GR.JOURNAL), list(GR.REFUS)
    with pytest.raises(PR.ArretProgramme, match="interdite"):
        PR.lancer(texte, racine, _copie(), str(tmp_path / "sortie"), **dict(REDUIT, couche=couche))
    assert not os.path.exists(tmp_path / "sortie") and GR.JOURNAL == journal and GR.REFUS == refus


def test_tailles_reduites_et_parametres_inconnus_refuses(tmp_path):
    """Artefacts : une taille réduite sous les couches des étapes, ou un paramètre inconnu : arrêt avant tout geste."""
    racine, texte = _racine(tmp_path)
    journal = list(GR.JOURNAL)
    with pytest.raises(PR.ArretProgramme, match="aucune taille réduite"):
        PR.lancer(texte, racine, _copie(), str(tmp_path / "sortie"), sources_etalonnage=2000)
    with pytest.raises(PR.ArretProgramme, match="inconnus"):
        PR.lancer(texte, racine, _copie(), str(tmp_path / "sortie"), couche=COUCHE, sources_decisives=10)
    assert not os.path.exists(tmp_path / "sortie") and GR.JOURNAL == journal


def test_dossier_deja_present(tmp_path):
    """Artefact : un dossier de sortie déjà présent arrête avant tout geste ; il n'est pas touché."""
    racine, texte = _racine(tmp_path)
    d = tmp_path / "sortie"
    d.mkdir()
    (d / "temoin.txt").write_text("témoin\n", encoding="utf-8")
    with pytest.raises(PR.ArretProgramme, match="déjà présent"):
        PR.lancer(texte, racine, _copie(), str(d), **REDUIT)
    assert sorted(os.listdir(d)) == ["temoin.txt"]


def test_copie_de_l_organisme_absente_ou_alteree(tmp_path):
    """Artefacts : la copie du code de l'organisme absente, ou un de ses fichiers altéré : arrêt (garde 17) avant toute étape,
    aucun dossier."""
    racine, texte = _racine(tmp_path)
    with pytest.raises(OR.OrganismeIndisponible):
        PR.lancer(texte, racine, str(tmp_path / "absente"), str(tmp_path / "sortie"), **REDUIT)
    alteree = str(tmp_path / "alteree")
    shutil.copytree(_copie(), alteree)
    rel = sorted(OR.EMPREINTES_PALIER_0A)[0]
    with open(os.path.join(alteree, rel), "a", encoding="utf-8") as fh:
        fh.write("\n# altéré\n")
    with pytest.raises(OR.OrganismeIndisponible):
        PR.lancer(texte, racine, alteree, str(tmp_path / "sortie"), **REDUIT)
    assert not os.path.exists(tmp_path / "sortie")


def _etapes_rapides(monkeypatch, audit=None, etape_4=None, etape_6=None):
    """Remplace, le temps d'un essai, les fonctions lourdes du code v6 par des fonctions rapides (ou qui arrêtent), pour éprouver
    ce que le programme fait de leur issue ; aucune graine n'est dérivée par elles."""
    monkeypatch.setattr(MO, "audit_du_generateur", audit or (lambda *a, **k: {"presentation": {"arret": []}}))
    monkeypatch.setattr(EP, "lancer_etape_4", etape_4 or (lambda *a, **k: {
        "frequences": dict(FREQUENCES), "comptes": COMPTES, "garde_17": {"tentatives_comparees": 1, "desaccords": 0},
        "jeu_de_la_garde_27": {"dose": 0.25, "sources": 3, "proposeur": "lecteur-tenue"}}))
    if etape_6 is not None:
        monkeypatch.setattr(EP, "etape_6", etape_6)


def test_arret_de_l_etape_3_ecrit_scelle_puis_chaine_arretee(tmp_path, monkeypatch):
    """Artefact : un arrêt de l'audit du générateur (planté, son rapport joint) est écrit et scellé, avec le rapport joint et le
    manifeste de l'étape 3 (issue « arrêt ») ; les étapes 4 à 6 ne se jouent pas ; le programme s'arrête."""
    def arret(*a, **k):
        e = MO.ArretGenerateur("audit du générateur en échec : planté (liste d'arrêt, point 2)")
        e.rapport = {"presentation": {"arret": ["planté"]}}
        raise e
    _etapes_rapides(monkeypatch, audit=arret)
    racine, texte = _racine(tmp_path)
    d = tmp_path / "sortie"
    with pytest.raises(PR.ArretProgramme, match="étape 3 arrêtée"):
        PR.lancer(texte, racine, _copie(), str(d), **REDUIT)
    assert sorted(os.listdir(d)) == ["etape-3"]
    assert (d / "etape-3" / "arret.txt").read_text(encoding="utf-8").startswith("ArretGenerateur : audit du générateur en échec")
    assert json.load(open(d / "etape-3" / "rapport-joint-a-l-arret.json"))["presentation"]["arret"] == ["planté"]
    assert _manifeste(str(d / "etape-3"))[0]["configuration"]["issue"] == "arrêt"
    assert not (d / "etape-3" / "rapport-audit-du-generateur.json").exists()


def test_frequences_alterees_apres_gel_arretent_l_etape_5(tmp_path, monkeypatch):
    """Artefact : le fichier des fréquences, altéré après son gel (planté), n'est pas relu : l'étape 5 s'arrête, l'arrêt est écrit
    et scellé avec son manifeste, l'étape 6 ne se joue pas. Cas sain : la chaîne entière (essai précédent)."""
    _etapes_rapides(monkeypatch)
    geler = FR.geler

    def geler_puis_alterer(chemin, *a, **k):
        sha = geler(chemin, *a, **k)
        with open(chemin, "ab") as fh:
            fh.write(b" ")
        return sha
    monkeypatch.setattr(FR, "geler", geler_puis_alterer)
    racine, texte = _racine(tmp_path)
    d = tmp_path / "sortie"
    with pytest.raises(PR.ArretProgramme, match="étape 5 arrêtée"):
        PR.lancer(texte, racine, _copie(), str(d), **REDUIT)
    assert sorted(os.listdir(d)) == ["etape-3", "etape-4", "etape-5"]
    assert (d / "etape-5" / "arret.txt").read_text(encoding="utf-8").startswith("ArretFrequences")
    assert _manifeste(str(d / "etape-5"))[0]["configuration"]["issue"] == "arrêt"


def test_arret_de_l_etape_6_ecrit_scelle(tmp_path, monkeypatch):
    """Artefact : un arrêt de l'étalonnage (planté : cible non convergée) est écrit et scellé avec le manifeste de l'étape 6, qui
    porte les fréquences vérifiées ; aucun fichier des réglages n'est gelé."""
    def arret(*a, **k):
        raise EP.ArretEtapes("étalonnage non convergé : planté")
    _etapes_rapides(monkeypatch, etape_6=arret)
    racine, texte = _racine(tmp_path)
    d = tmp_path / "sortie"
    with pytest.raises(PR.ArretProgramme, match="étape 6 arrêtée"):
        PR.lancer(texte, racine, _copie(), str(d), **REDUIT)
    m, _ = _manifeste(str(d / "etape-6"))
    assert m["configuration"]["issue"] == "arrêt" and set(m["fichiers_geles"]) == {"frequences"}
    assert not (d / "etape-6" / PR.FICHIER_DES_REGLAGES).exists()


def test_ligne_de_commande_refusee_sur_racine_factice_sans_pieces(tmp_path):
    """La ligne de commande (couches des étapes, valeurs gelées), sur une racine factice sans pièces : refus du verrou avant tout
    geste, code non nul, aucun dossier ; un nombre d'arguments faux rend l'usage."""
    racine, texte = _racine(tmp_path, piece=False, controle=False)
    d = str(tmp_path / "sortie")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "-B", CHEMIN_PROGRAMME, texte, racine, _copie(), d], capture_output=True, text=True,
                       env=env)
    assert r.returncode != 0 and "autorisation refusée" in r.stderr and not os.path.exists(d)
    u = subprocess.run([sys.executable, "-B", CHEMIN_PROGRAMME, texte], capture_output=True, text=True, env=env)
    assert u.returncode != 0 and "NON LANCÉ" in u.stderr


def test_zz_aucune_graine_decisive_ni_d_autre_couche():
    """Essai final de ce fichier : seule la couche « essai-de-forme » a été dérivée dans ce processus ; tout refus consigné est
    d'une couche décisive."""
    assert set(GR.couches_derivees()) <= {COUCHE}
    assert all(GR.couche_de(e) == COUCHE for _, e in GR.JOURNAL)
    assert all(r.split("|", 1)[0] in ("couche=decisif", "couche=confirmation") for r in GR.REFUS)
