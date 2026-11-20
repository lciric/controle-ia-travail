"""Essais du programme des étapes 6 bis et 7 (`lancer_etapes_6bis_et_7_v1.py`), sous la couche « essai-de-forme » seule, sur une
racine factice (texte présenté, registre des GO, pièce d'autorisation du verrou, pièce de contrôle de la mère, tous factices,
dans un dossier temporaire) et des fichiers gelés factices (jamais ceux des étapes 5 et 6). Chaque garde a son cas sain et son
artefact (règle R5) : pièces absentes ou incomplètes, empreinte d'un fichier gelé fausse, couche interdite, tailles réduites
sous la couche des étapes, dossier déjà présent, garde S8 en échec. L'essai final contrôle qu'aucune graine décisive, ni
d'aucune autre couche que « essai-de-forme », n'a été dérivée. Lancement : dossier courant, une copie du code v6 ;
`PYTHONPATH=src`."""

import hashlib
import importlib.util
import json
import os
import subprocess
import sys

import pytest

from controle_ia.heritage_etage_processeur_v1 import constantes as K
from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1 import equivalence as EQ
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
from controle_ia.heritage_etage_processeur_v1 import tirages as TI

CHEMIN_PROGRAMME = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "lancer_etapes_6bis_et_7_v1.py")
_spec = importlib.util.spec_from_file_location("lancer_etapes_6bis_et_7_v1", CHEMIN_PROGRAMME)
PR = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(PR)

COMMIT = "0123456789abcdef0123456789abcdef01234567"
GO = "GO-2099-01-01-01"
FREQUENCES = {"p_tient_vraie_source": 1.0, "p_tient_vraie_cible": 1.0, "p_tient_fausse": 0.15, "p_tient_non_plantee_base": 0.02,
              "p_tient_non_plantee_composition": 0.8, "p_tient_non_plantee_copie": 0.05, "p_passage_vraie": 1.0,
              "p_faux_passage": 0.4}
VALEURS = {"K": lambda t: 32.0 * t, "tau": lambda t: 0.9 * t, "phi": lambda t: {0.5: 0.4, 1.0: 0.9, 1.5: 1.5}[t],
           "gamma": lambda t: {0.25: 0.1, 0.5: 0.2, 1.0: 0.5, 1.5: 0.9}[t]}
COUCHE = "essai-de-forme"
REDUIT = dict(couche=COUCHE, sources_mecaniques=1, sources_statistiques=200, seulement=[("sourd-egal", 0.25)])


def _sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _sceller(chemin):
    with open(str(chemin) + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{_sha(chemin)}  {os.path.basename(chemin)}\n")
    return _sha(chemin)


def _ecrire(chemin, texte, sceller=True):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(texte)
    return _sceller(chemin) if sceller else None


def _table_des_modules():
    paquet = os.path.dirname(os.path.abspath(GR.__file__))
    lignes = [f"  {_sha(os.path.join(paquet, f))}  src/controle_ia/heritage_etage_processeur_v1/{f}"
              for f in sorted(os.listdir(paquet)) if f.endswith(".py")]
    return lignes + [f"  {_sha(os.path.join(os.path.dirname(paquet), '__init__.py'))}  src/controle_ia/__init__.py"]


def _racine(base, controle=None, piece=True, controle_scelle=True):
    """Racine factice saine par défaut. `controle` : le texte de la pièce de contrôle (par défaut : commit et empreinte du
    programme). Rend (racine, texte présenté)."""
    racine = str(base / "racine")
    texte = os.path.join(racine, "prereg", "texte-factice-v1.md")
    sha_texte = _ecrire(texte, "\n".join(["# Texte factice", "", f"- Commit du code d'analyse : **`{COMMIT}`** (factice).", "",
                                          "  ```"] + _table_des_modules() + ["  ```", ""]))
    _ecrire(os.path.join(racine, "registres", "go.md"),
            f"# Registre factice\n\n| id | quoi |\n|---|---|\n| {GO} | essai du programme des étapes 6 bis et 7 |\n", False)
    if piece:
        _ecrire(os.path.join(racine, K.CHEMIN_PIECE_D_AUTORISATION),
                f"identifiant du GO : {GO}\ncommit du code : {COMMIT}\nempreinte du texte scellé : {sha_texte}\n"
                "heure : 2026-11-20T18:30:00Z\n")
    if controle is None:
        controle = (f"| point | attendu | constaté |\n|---|---|---|\n| commit du code | {COMMIT} | {COMMIT} |\n"
                    f"| programme des étapes 6 bis et 7 | {PR.empreinte_du_programme()} | idem |\n")
    if controle is not False:
        _ecrire(os.path.join(racine, PR.CHEMIN_PIECE_DE_CONTROLE), controle, controle_scelle)
    return racine, texte


def _lignes(non_atteignables=()):
    return [{"proposeur": nom, "nom_du_reglage": r, "dose": dose, "cible": cible, "reglage": VALEURS[r](cible),
             "atteignable": (r, dose, cible) not in non_atteignables,
             "statut": "non atteignable" if (r, dose, cible) in non_atteignables else "atteint"}
            for nom, r, dose, cible in EP.cibles_d_etalonnage()]


def _geles(base):
    d = str(base / "geles")
    os.makedirs(d)
    comptes = {"vraie-source": {"engagees": 4, "tiennent": 4},
               "criblage": {"vraies_examinees": 2, "vraies_retenues": 2, "autres_examinees": 5, "autres_passees": 2},
               "tentatives_par_classe": {c: 1 for c in K.CLASSES}}
    cf, cr = os.path.join(d, "frequences-factices.json"), os.path.join(d, "reglages-factices.json")
    return cf, FR.geler(cf, FREQUENCES, comptes, {"factice": True}), cr, ET.geler_reglages(cr, _lignes(), {"factice": True})


def test_configurations_aux_reglages_geles_proposition():
    """Cas sain : toutes cibles atteignables, 22 couples (proposeur, dose), soit 66 comparaisons sur trois bras ; chacun à la
    configuration de référence que le plan des cases lui donne (taille 1, force 1, ou sans réglage). Artefact : une cible de
    référence non atteignable retire ses couples, et seulement eux."""
    c = PR.configurations_aux_reglages_geles(_lignes())
    assert len(c) == 22 and 3 * len(c) == 66
    assert c[("lecteur-heritage", 0.25)] == P.configuration("lecteur-heritage", K=32.0)
    assert c[("lecteur-heritage", 0.0)] == P.configuration("lecteur-heritage", K=32.0)  # famille C : K de la dose 0,5
    assert c[("lecteur-tenue", 0.5)] == P.configuration("lecteur-tenue", tau=0.9)
    assert c[("suiveur", 0.5)] == c[("suiveur", 0.0)] == P.configuration("suiveur", phi=0.9)
    assert c[("generaliste", 0.0)] == P.configuration("generaliste", gamma=0.5)
    assert {d for p, d in c if p == "sourd-paie"} == {0.0, 0.25, 0.5} and ("lecteur-tenue", 0.0) not in c
    c2 = PR.configurations_aux_reglages_geles(_lignes(non_atteignables=(("K", 0.25, 1.0),)))
    assert set(c) - set(c2) == {("lecteur-heritage", 0.25), ("lecteur-deux", 0.25)}


def test_cas_sain_reduit_sous_essai_de_forme(tmp_path):
    """Cas sain : racine factice conforme, fichiers gelés factices ; les étapes 6 bis et 7, réduites (une source mécanique, 200
    sources statistiques, un couple), sous la couche « essai-de-forme » : détail de la garde scellé, manifeste scellé et vérifié,
    qui porte les fichiers gelés vérifiés, le commit de la pièce et l'empreinte du programme ; étiquettes de la seule couche
    « essai-de-forme », familles « etape-6-bis » et « etape-7 »."""
    racine, texte = _racine(tmp_path)
    cf, sf, cr, sr = _geles(tmp_path)
    d = str(tmp_path / "sortie")
    r = PR.lancer(texte, racine, cf, sf, cr, sr, d, **REDUIT)
    assert sorted(r["detail"]) == [("sourd-egal", b, 0.25) for b in ("1", "2", "3")]
    assert open(os.path.join(d, PR.FICHIER_DU_DETAIL + ".sha256")).read().split()[0] == _sha(os.path.join(d, PR.FICHIER_DU_DETAIL))
    m = json.load(open(r["manifeste"], encoding="utf-8"))
    assert TI.verifier_manifeste(r["manifeste"]) == m["etiquettes"]["nombre"] > 0
    assert m["commit"] == COMMIT and m["fichiers_geles"] == {"frequences": sf, "reglages": sr}
    assert m["configuration"]["programme_sha256"] == PR.empreinte_du_programme() and m["configuration"]["issue"] == "tenue"
    assert m["texte_sha256"] == _sha(texte) and m["etiquettes"]["couches"] == ["couche=essai-de-forme"]
    etiquettes = open(os.path.join(d, "manifeste-etiquettes.txt"), encoding="utf-8").read().split("\n")
    assert {e.split("|")[1] for e in etiquettes} == {"famille=etape-6-bis", "famille=etape-7"}
    assert not os.path.exists(os.path.join(d, PR.FICHIER_DE_L_ARRET))


@pytest.mark.parametrize("cas", ["piece-d-autorisation-absente", "piece-de-controle-absente", "piece-de-controle-non-scellee",
                                 "controle-sans-empreinte-du-programme", "controle-sans-commit"])
def test_pieces_absentes_ou_incompletes(cas, tmp_path):
    """Artefacts : chaque pièce absente, la pièce de contrôle non scellée, ou sans l'empreinte du programme, ou sans le commit :
    refus avant tout geste, aucun dossier, aucune graine."""
    if cas == "piece-d-autorisation-absente":
        racine, texte = _racine(tmp_path, piece=False)
    elif cas == "piece-de-controle-absente":
        racine, texte = _racine(tmp_path, controle=False)
    elif cas == "piece-de-controle-non-scellee":
        racine, texte = _racine(tmp_path, controle_scelle=False)
    elif cas == "controle-sans-empreinte-du-programme":
        racine, texte = _racine(tmp_path, controle=f"| commit du code | {COMMIT} |\n")
    else:
        racine, texte = _racine(tmp_path, controle=f"| programme | {PR.empreinte_du_programme()} |\n")
    cf, sf, cr, sr = _geles(tmp_path)
    journal = list(GR.JOURNAL)
    with pytest.raises((GR.GraineRefusee, PR.ArretProgramme)):
        PR.lancer(texte, racine, cf, sf, cr, sr, str(tmp_path / "sortie"), **REDUIT)
    assert not os.path.exists(tmp_path / "sortie") and GR.JOURNAL == journal


def test_empreinte_d_un_gele_fausse(tmp_path):
    """Artefacts : l'empreinte attendue des fréquences, puis celle des réglages, n'est pas la leur ; un fichier gelé absent :
    arrêt avant tout tirage, aucun dossier."""
    racine, texte = _racine(tmp_path)
    cf, sf, cr, sr = _geles(tmp_path)
    d = str(tmp_path / "sortie")
    with pytest.raises(FR.ArretFrequences):
        PR.lancer(texte, racine, cf, "0" * 64, cr, sr, d, **REDUIT)
    with pytest.raises(ET.ArretEtalonnage):
        PR.lancer(texte, racine, cf, sf, cr, "1" * 64, d, **REDUIT)
    with pytest.raises(EP.ArretEtapes, match="R11"):
        PR.lancer(texte, racine, cf + ".absent", sf, cr, sr, d, **REDUIT)
    assert not os.path.exists(d)


@pytest.mark.parametrize("couche", ["decisif", "confirmation", "essai", "mecanique", "etalonnage", "audit", "inconnue"])
def test_couche_interdite(couche, tmp_path):
    """Artefacts : toute couche autre que « mecanique-reglages » (et « essai-de-forme » pour les essais) est refusée avant tout
    geste — ni pièce lue, ni graine dérivée, ni refus consigné, ni dossier."""
    racine, texte = _racine(tmp_path)
    cf, sf, cr, sr = _geles(tmp_path)
    journal, refus = list(GR.JOURNAL), list(GR.REFUS)
    with pytest.raises(PR.ArretProgramme, match="interdite"):
        PR.lancer(texte, racine, cf, sf, cr, sr, str(tmp_path / "sortie"), **dict(REDUIT, couche=couche))
    assert not os.path.exists(tmp_path / "sortie") and GR.JOURNAL == journal and GR.REFUS == refus


def test_tailles_reduites_refusees_sous_la_couche_des_etapes(tmp_path):
    """Artefact : sous la couche « mecanique-reglages », une taille réduite ou un sous-ensemble est refusé avant tout geste (la
    couche des étapes n'est jamais jouée par les essais)."""
    racine, texte = _racine(tmp_path)
    cf, sf, cr, sr = _geles(tmp_path)
    journal = list(GR.JOURNAL)
    for kw in ({"sources_mecaniques": 1}, {"sources_statistiques": 200}, {"seulement": [("sourd-egal", 0.25)]}):
        with pytest.raises(PR.ArretProgramme, match="aucune taille réduite"):
            PR.lancer(texte, racine, cf, sf, cr, sr, str(tmp_path / "sortie"), couche=PR.COUCHE_DES_ETAPES, **kw)
    assert not os.path.exists(tmp_path / "sortie") and GR.JOURNAL == journal


def test_dossier_deja_present(tmp_path):
    """Artefact : un dossier de sortie déjà présent arrête avant tout geste ; il n'est pas touché."""
    racine, texte = _racine(tmp_path)
    cf, sf, cr, sr = _geles(tmp_path)
    d = tmp_path / "sortie"
    d.mkdir()
    (d / "temoin.txt").write_text("témoin\n", encoding="utf-8")
    with pytest.raises(PR.ArretProgramme, match="déjà présent"):
        PR.lancer(texte, racine, cf, sf, cr, sr, str(d), **REDUIT)
    assert sorted(os.listdir(d)) == ["temoin.txt"]


def test_garde_s8_en_echec_ecrite_scellee_puis_arret(tmp_path, monkeypatch):
    """Artefact : une garde S8 en échec (l'arrêt planté dans la fonction du code v6, non tiré) est écrite et scellée avec le
    manifeste (issue « arrêt »), puis le programme s'arrête ; aucun détail de garde tenue n'est écrit. Le cas sain est
    `test_cas_sain_reduit_sous_essai_de_forme`."""
    def arret(*a, **k):
        raise EQ.ArretEquivalence("S8 (ii) : arrêt planté par l'essai")
    monkeypatch.setattr(EP, "etape_6_bis_et_7", arret)
    racine, texte = _racine(tmp_path)
    cf, sf, cr, sr = _geles(tmp_path)
    d = str(tmp_path / "sortie")
    with pytest.raises(PR.ArretProgramme, match="liste d'arrêt, point 4"):
        PR.lancer(texte, racine, cf, sf, cr, sr, d, **REDUIT)
    assert open(os.path.join(d, PR.FICHIER_DE_L_ARRET), encoding="utf-8").read().startswith("S8 (ii) : arrêt planté")
    assert _sha(os.path.join(d, PR.FICHIER_DE_L_ARRET)) == open(os.path.join(d, PR.FICHIER_DE_L_ARRET + ".sha256")).read().split()[0]
    m = json.load(open(os.path.join(d, "manifeste.json"), encoding="utf-8"))
    assert m["configuration"]["issue"] == "arrêt" and TI.verifier_manifeste(os.path.join(d, "manifeste.json")) == 0
    assert not os.path.exists(os.path.join(d, PR.FICHIER_DU_DETAIL))


def test_ligne_de_commande_refusee_sur_racine_factice_sans_pieces(tmp_path):
    """La ligne de commande (couche des étapes, tailles du code v6), sur une racine factice sans pièce d'autorisation ni pièce de
    contrôle : refus du verrou avant tout geste, code non nul, aucun dossier ; un nombre d'arguments faux rend l'usage."""
    racine, texte = _racine(tmp_path, piece=False, controle=False)
    cf, sf, cr, sr = _geles(tmp_path)
    d = str(tmp_path / "sortie")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "-B", CHEMIN_PROGRAMME, texte, racine, cf, sf, cr, sr, d], capture_output=True, text=True,
                       env=env)
    assert r.returncode != 0 and "autorisation refusée" in r.stderr and not os.path.exists(d)
    u = subprocess.run([sys.executable, "-B", CHEMIN_PROGRAMME, texte], capture_output=True, text=True, env=env)
    assert u.returncode != 0 and "NON LANCÉ" in u.stderr


def test_zz_aucune_graine_decisive_ni_d_autre_couche():
    """Essai final de ce fichier : aucune graine des couches décisives, ni d'aucune couche autre que « essai-de-forme », n'a été
    dérivée dans ce processus ; tout refus consigné est d'une couche décisive."""
    assert set(GR.couches_derivees()) <= {COUCHE}
    assert all(GR.couche_de(e) == COUCHE for _, e in GR.JOURNAL)
    assert all(r.split("|", 1)[0] in ("couche=decisif", "couche=confirmation") for r in GR.REFUS)
