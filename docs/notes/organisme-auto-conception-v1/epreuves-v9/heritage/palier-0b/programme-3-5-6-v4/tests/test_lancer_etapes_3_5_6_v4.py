"""Essais v4 du programme des étapes 3, 4, 5 et 6, version 2 (vérification des essais v3, `59907a0d…`, point 4) : les essais v3,
plus `test_le_programme_charge_est_le_v2`, qui exige que le programme chargé ait l'empreinte du programme v2 ; il échoue chaque
fois que la variable `PROGRAMME_3_5_6_MUTANT` est posée (elle n'est plus une porte dérobée : tout lancement où elle est posée a au
moins un essai en échec), et un message est écrit à l'import quand elle l'est.

Essais v3 (repris) du programme des étapes 3, 4, 5 et 6, version 2 (`lancer_etapes_3_5_6_v2.py`, inchangé, empreinte
1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14, contrôlée au chargement). Essais v3 (vérification du programme
v2, `beeaf621…`, point 3) : le retour de `lancer` (`frequences`, `reglages` : (chemin, empreinte), chemin existant, empreinte égale
à celle du fichier ; `manifestes` : clés 3 à 6, chacune l'empreinte du manifeste de son étape) est éprouvé sur le cas sain planté ;
sur l'arrêt au point 5, `lancer` ne rend rien et `main` n'imprime aucun fichier gelé ; la sortie imprimée de `main` sur le cas
sain planté est relue et doit porter les mêmes valeurs que les fichiers. La variable `PROGRAMME_3_5_6_MUTANT`, pour la seule preuve
par défaut planté, fait charger une copie mutée à la place du programme, sans contrôle de son empreinte.

Essais v2 (repris) : version 2 : la condition 5 de la liste
d'arrêt après l'étape 6 (cas sain et artefacts, sur des réglages plantés), et les cinq arrêts nommés de l'étape 4 (un essai
chacun), sur la vérification du programme v1 (`5dae3b94…`) ; le reste est repris de la version 1.

Sous la couche « essai-de-forme » seule, sur une
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

EMPREINTE_DU_PROGRAMME_V2 = "1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14"
# le programme v2, inchangé : la copie du bloc-notes du développeur, d'empreinte contrôlée égale à celle du programme versé
CHEMIN_PROGRAMME = os.environ.get("PROGRAMME_3_5_6_MUTANT") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, "programme-3-5-6-v2", "lancer_etapes_3_5_6_v2.py")
if not os.environ.get("PROGRAMME_3_5_6_MUTANT"):
    with open(CHEMIN_PROGRAMME, "rb") as _fh:
        assert hashlib.sha256(_fh.read()).hexdigest() == EMPREINTE_DU_PROGRAMME_V2, "programme v2 d'empreinte inattendue"
else:  # essais v4 : la variable posée est dite à l'import, et `test_le_programme_charge_est_le_v2` échouera
    sys.stderr.write(f"\nATTENTION : PROGRAMME_3_5_6_MUTANT est posée ; programme chargé sans contrôle à l'import : "
                     f"{CHEMIN_PROGRAMME} ; l'essai test_le_programme_charge_est_le_v2 échouera si ce n'est pas le v2\n")
_spec = importlib.util.spec_from_file_location("lancer_etapes_3_5_6_v2", CHEMIN_PROGRAMME)
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


def test_le_programme_charge_est_le_v2():
    """Essai v4 (vérification des essais v3, point 4) : le programme chargé par ces essais est le programme v2, d'empreinte
    `EMPREINTE_DU_PROGRAMME_V2`, recalculée par le programme lui-même (`empreinte_du_programme`, sur son propre fichier) et sur le
    fichier chargé. Cas sain : variable `PROGRAMME_3_5_6_MUTANT` absente, programme v2 chargé : passe. Artefact : la variable posée
    sur une autre copie (mutant, ou simple commentaire ajouté) : échoue, si bien qu'aucun lancement des essais avec une autre copie
    ne passe en entier."""
    with open(CHEMIN_PROGRAMME, "rb") as fh:
        sur_disque = hashlib.sha256(fh.read()).hexdigest()
    assert PR.empreinte_du_programme() == sur_disque == EMPREINTE_DU_PROGRAMME_V2, (
        f"programme chargé ({CHEMIN_PROGRAMME}) d'empreinte {sur_disque}, et non le programme v2 ({EMPREINTE_DU_PROGRAMME_V2})"
        + (" — PROGRAMME_3_5_6_MUTANT est posée" if os.environ.get("PROGRAMME_3_5_6_MUTANT") else ""))


@pytest.fixture(scope="module")
def chaine(tmp_path_factory):
    """La chaîne entière, réduite, sous la couche « essai-de-forme » (étape 3 : quatre suites par dose, 20 permutations ;
    étape 4 : deux proposeurs, dose 0,5, une source, garde 17 jouée sur elle, et le jeu de la garde 27 ; étape 6 : 2 000 sources
    d'étalonnage)."""
    base = tmp_path_factory.mktemp("chaine")
    racine, texte = _racine(base)
    g_avant = len(GR.JOURNAL)
    d = str(base / "sortie")
    try:
        PR.lancer(texte, racine, _copie(), d, **REDUIT)
        arret = None
    except PR.ArretProgramme as e:  # version 2 : seul l'arrêt du point 5 est admis ici (contrôlé par l'essai)
        arret = str(e)
    return {"dossier": d, "arret": arret, "texte": texte, "journal": GR.JOURNAL[g_avant:]}


def test_chaine_entiere_reduite_sous_essai_de_forme(chaine):
    """Cas sain : les étapes 3, 4, 5 et 6 dans cet ordre, chacune avec son manifeste scellé et vérifié (commit de la pièce,
    empreinte du programme) ; les étapes 3 à 5 « tenue » ; rapport de l'audit scellé ; résultat de l'étape 4 scellé (garde 17
    jouée) ; fichier des fréquences gelé, relu sous contrôle de son empreinte, inscrit aux manifestes des étapes 5 et 6 ; fichier
    des réglages gelé avec son compagnon et inscrit au manifeste de l'étape 6 ; toutes les étiquettes de la couche
    « essai-de-forme », dans l'ordre des étapes. Version 2 : sur ces tailles réduites et ces fréquences d'essai, la condition 5
    de la liste d'arrêt peut être vraie (son verdict y est sans portée) ; l'étape 6 est alors close « arrêt », par la seule cause
    du point 5, écrite et scellée, et rien d'autre n'arrête ; sinon elle est close « tenue ». Les deux lectures de la garde sont
    éprouvées à part, sur des réglages plantés (`test_v2_point_5_*`)."""
    d = chaine["dossier"]
    assert sorted(x for x in os.listdir(d)) == ["etape-3", "etape-4", "etape-5", "etape-6"]
    for e in ("3", "4", "5", "6"):
        m, n = _manifeste(os.path.join(d, f"etape-{e}"))
        assert m["configuration"]["etape"] == e and m["commit"] == COMMIT
        assert m["configuration"]["issue"] == ("tenue" if e != "6" or chaine["arret"] is None else "arrêt")
        assert m["configuration"]["programme_sha256"] == PR.empreinte_du_programme() and m["texte_sha256"] == _sha(chaine["texte"])
        assert (n == 0) == (e == "5") and m["etiquettes"]["couches"] == ([] if e == "5" else ["couche=essai-de-forme"])
        assert os.path.exists(os.path.join(d, f"etape-{e}", "arret.txt")) == (e == "6" and chaine["arret"] is not None)
    if chaine["arret"] is not None:
        assert "étape 6 arrêtée" in chaine["arret"] and "ArretListeDArretPoint5" in chaine["arret"]
        cause = os.path.join(d, "etape-6", "arret.txt")
        assert open(cause, encoding="utf-8").read().startswith("ArretListeDArretPoint5 : liste d'arrêt, point 5")
        assert _sha(cause) == open(cause + ".sha256").read().split()[0]
    chemin_f = os.path.join(d, "etape-5", PR.FICHIER_DES_FREQUENCES)
    chemin_r = os.path.join(d, "etape-6", PR.FICHIER_DES_REGLAGES)
    sha_f, sha_r = _sha(chemin_f), _sha(chemin_r)
    assert open(chemin_f + ".sha256").read().split()[0] == sha_f
    assert open(chemin_r + ".sha256").read().split()[0] == sha_r
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


# --- version 2 ---------------------------------------------------------------------------------------------------------------


def _reglages(k=(0.25, 0.5), tau=(0.25, 0.5), phi=True):
    """Réglages plantés au format de `etapes.reglages_pour_le_plan` : K et τ atteignables à la taille 1 aux seules doses `k` et
    `tau` (non atteignables, None, aux autres) ; φ à la force 1 atteignable ou non ; les autres tailles et forces atteignables."""
    r = {"K": {(d, t): 32.0 * t for d in K.DOSES_NON_NULLES for t in K.TAILLES},
         "tau": {(d, t): 0.9 * t for d in K.DOSES_NON_NULLES for t in K.TAILLES},
         "phi": {0.5: 0.4, 1.0: 0.9, 1.5: 1.5}, "gamma": {0.25: 0.1, 0.5: 0.2, 1.0: 0.5, 1.5: 0.9}}
    for d in K.DOSES_NON_NULLES:
        if d not in k:
            r["K"][(d, K.TAILLE_REFERENCE)] = None
        if d not in tau:
            r["tau"][(d, K.TAILLE_REFERENCE)] = None
    if not phi:
        r["phi"][K.FORCE_REFERENCE_SUIVEUR] = None
    return r


def test_v2_liste_d_arret_point_5_a_la_lettre():
    """Cas sain : la taille de référence atteignable à une seule dose non nulle pour chaque contraste, et la force de référence
    du suiveur atteignable : condition fausse. Artefacts : K de référence non atteignable aux deux doses ; τ de même ; φ de
    référence non atteignable ; une cible absente : condition vraie, chaque cause nommée. Les autres tailles et forces ne
    comptent pas."""
    assert PR.liste_d_arret_point_5(_reglages()) == []
    assert PR.liste_d_arret_point_5(_reglages(k=(0.5,), tau=(0.25,))) == []
    assert ["héritage" in c for c in PR.liste_d_arret_point_5(_reglages(k=()))] == [True]
    assert ["tenue" in c for c in PR.liste_d_arret_point_5(_reglages(tau=()))] == [True]
    assert ["suiveur" in c for c in PR.liste_d_arret_point_5(_reglages(phi=False))] == [True]
    assert len(PR.liste_d_arret_point_5(_reglages(k=(), tau=()))) == 2
    r = _reglages()
    del r["phi"][K.FORCE_REFERENCE_SUIVEUR]
    assert len(PR.liste_d_arret_point_5(r)) == 1
    autres = _reglages()
    autres["K"] = {k: (None if k[1] != K.TAILLE_REFERENCE else v) for k, v in autres["K"].items()}
    autres["gamma"] = {f: None for f in autres["gamma"]}
    assert PR.liste_d_arret_point_5(autres) == []


def _etape_6_plantee(reglages):
    """`etapes.etape_6` remplacée : elle gèle, par la fonction du code v6, un fichier de réglages vide et rend les réglages
    plantés ; rien n'est tiré."""
    from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET

    def etape_6(graines, couche, f, sources, chemin, configuration):
        return [], reglages, ET.geler_reglages(chemin, [], configuration)
    return etape_6


def test_v2_point_5_artefact_k_et_tau_non_atteignables_arrete_l_etape_6(tmp_path, monkeypatch):
    """Artefact (celui de la vérification) : K et τ de référence non atteignables aux deux doses, φ atteignable : l'étape 6 rend
    ses réglages, la condition 5 est vraie, l'arrêt est écrit et scellé avec le manifeste de l'étape 6 « arrêt », qui inscrit les
    fréquences et le fichier des réglages déjà gelé ; le programme s'arrête."""
    _etapes_rapides(monkeypatch, etape_6=_etape_6_plantee(_reglages(k=(), tau=())))
    racine, texte = _racine(tmp_path)
    d = tmp_path / "sortie"
    with pytest.raises(PR.ArretProgramme, match="étape 6 arrêtée"):
        PR.lancer(texte, racine, _copie(), str(d), **REDUIT)
    cause = (d / "etape-6" / "arret.txt").read_text(encoding="utf-8")
    assert cause.startswith("ArretListeDArretPoint5 : liste d'arrêt, point 5") and "héritage" in cause and "tenue" in cause
    assert _sha(str(d / "etape-6" / "arret.txt")) == open(d / "etape-6" / "arret.txt.sha256").read().split()[0]
    m, _ = _manifeste(str(d / "etape-6"))
    assert m["configuration"]["issue"] == "arrêt" and set(m["fichiers_geles"]) == {"frequences"}
    assert m["configuration"]["reglages_sha256"] == _sha(str(d / "etape-6" / PR.FICHIER_DES_REGLAGES))


def test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue(tmp_path, monkeypatch):
    """Cas sain planté : référence atteignable à une seule dose pour chaque contraste, φ atteignable : l'étape 6 se clôt
    « tenue », sans fichier d'arrêt (le cas sain tiré est la chaîne entière)."""
    _etapes_rapides(monkeypatch, etape_6=_etape_6_plantee(_reglages(k=(0.25,), tau=(0.5,))))
    racine, texte = _racine(tmp_path)
    r = PR.lancer(texte, racine, _copie(), str(tmp_path / "sortie"), **REDUIT)
    m, _ = _manifeste(os.path.join(r["dossier"], "etape-6"))
    assert m["configuration"]["issue"] == "tenue" and not os.path.exists(os.path.join(r["dossier"], "etape-6", "arret.txt"))
    _verifier_le_retour(r)


def _verifier_le_retour(r):
    """Essais v3 : le retour de `lancer` — `frequences` et `reglages` de la forme (chemin, empreinte), le chemin celui du
    fichier gelé de son étape, existant, l'empreinte égale au SHA-256 du fichier et à son compagnon ; `manifestes` de clés 3 à 6,
    chacune l'empreinte du manifeste de son étape."""
    d = r["dossier"]
    for cle, etape, nom in (("frequences", "etape-5", PR.FICHIER_DES_FREQUENCES), ("reglages", "etape-6", PR.FICHIER_DES_REGLAGES)):
        valeur = r[cle]
        assert isinstance(valeur, tuple) and len(valeur) == 2, (cle, valeur)
        chemin, empreinte = valeur
        assert chemin == os.path.join(d, etape, nom) and os.path.isfile(chemin), (cle, valeur)
        assert empreinte == _sha(chemin) == open(chemin + ".sha256", encoding="ascii").read().split()[0], (cle, valeur)
    assert sorted(r["manifestes"]) == ["3", "4", "5", "6"]
    for e, sha in r["manifestes"].items():
        assert sha == _sha(os.path.join(d, f"etape-{e}", "manifeste.json")), e


def _lancer_reduit_par_main(monkeypatch):
    """`main` appelle `lancer` sans couche ni taille (couches des étapes) : le temps d'un essai, `lancer` est remplacé par le
    même `lancer`, sous la couche « essai-de-forme » et aux tailles réduites, pour que `main` ne dérive aucune graine d'une
    couche des étapes. Rend le `lancer` d'origine."""
    origine = PR.lancer
    monkeypatch.setattr(PR, "lancer", lambda texte, racine, copie, dossier: origine(texte, racine, copie, dossier, **REDUIT))
    return origine


def _lire_la_sortie_de_main(texte_imprime):
    """La sortie de `main`, relue ligne à ligne, dans sa forme (programme v2) : « étape N : manifeste EMPREINTE »,
    « fréquences gelées : CHEMIN EMPREINTE », « réglages gelés : CHEMIN EMPREINTE ». Rend un dictionnaire de la forme du retour
    de `lancer`."""
    out = {"manifestes": {}}
    for ligne in texte_imprime.strip().split("\n"):
        tete, _, reste = ligne.partition(" : ")
        mots = reste.split(" ")
        if tete.startswith("étape ") and mots[0] == "manifeste" and len(mots) == 2:
            out["manifestes"][tete[len("étape "):]] = mots[1]
        elif tete in ("fréquences gelées", "réglages gelés") and len(mots) == 2:
            out["frequences" if tete.startswith("fréquences") else "reglages"] = (mots[0], mots[1])
        else:
            raise AssertionError(f"ligne de sortie hors de la forme : {ligne!r}")
    return out


def test_v3_main_imprime_le_retour_de_lancer(tmp_path, monkeypatch, capsys):
    """Essai v3, cas sain planté : la sortie de `main`, relue, porte exactement les valeurs du retour de `lancer` et des fichiers
    — l'empreinte du manifeste de chaque étape, et, pour les fréquences et les réglages gelés, le chemin puis l'empreinte du
    fichier (l'ordre que reçoivent les programmes des étapes 6 bis et 7, et 8 et 9)."""
    _etapes_rapides(monkeypatch, etape_6=_etape_6_plantee(_reglages(k=(0.25,), tau=(0.5,))))
    _lancer_reduit_par_main(monkeypatch)
    racine, texte = _racine(tmp_path)
    d = str(tmp_path / "sortie")
    PR.main([texte, racine, _copie(), d])
    lu = _lire_la_sortie_de_main(capsys.readouterr().out)
    _verifier_le_retour(dict(lu, dossier=d))
    assert sorted(lu) == ["frequences", "manifestes", "reglages"]


def test_v3_arret_au_point_5_aucun_retour_ni_gele_imprime(tmp_path, monkeypatch, capsys):
    """Essai v3, arrêt au point 5 (K et τ de référence non atteignables aux deux doses, planté) : `lancer` s'arrête sans rien
    rendre ; `main` s'arrête de même et n'imprime ni fichier gelé ni manifeste ; seuls les manifestes écrits sur disque portent
    les empreintes, celui de l'étape 6 avec l'issue « arrêt »."""
    _etapes_rapides(monkeypatch, etape_6=_etape_6_plantee(_reglages(k=(), tau=())))
    _lancer_reduit_par_main(monkeypatch)
    racine, texte = _racine(tmp_path)
    d = tmp_path / "sortie"
    rendu = []
    with pytest.raises(PR.ArretProgramme, match="ArretListeDArretPoint5"):
        rendu.append(PR.main([texte, racine, _copie(), str(d)]))
    assert rendu == [] and capsys.readouterr().out == ""
    assert _manifeste(str(d / "etape-6"))[0]["configuration"]["issue"] == "arrêt"
    assert _manifeste(str(d / "etape-5"))[0]["fichiers_geles"] == {"frequences": _sha(str(d / "etape-5" / PR.FICHIER_DES_FREQUENCES))}


@pytest.mark.parametrize("classe", ["MC.ArretMecanique", "FR.ArretFrequences", "OR.DesaccordOrganisme", "MO.ArretGenerateur",
                                    "EP.ArretEtapes"])
def test_v2_arrets_nommes_de_l_etape_4(classe, tmp_path, monkeypatch):
    """Artefacts : chacun des cinq arrêts nommés de l'étape 4 (planté) est écrit et scellé avec le manifeste de l'étape 4
    « arrêt » ; les étapes 5 et 6 ne se jouent pas ; le programme s'arrête. Cas sain : la chaîne entière."""
    from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
    module, nom = classe.split(".")
    exc = getattr({"MC": MC, "FR": FR, "OR": OR, "MO": MO, "EP": EP}[module], nom)

    def arret(*a, **k):
        raise exc(f"{nom} planté")
    _etapes_rapides(monkeypatch, etape_4=arret)
    racine, texte = _racine(tmp_path)
    d = tmp_path / "sortie"
    with pytest.raises(PR.ArretProgramme, match="étape 4 arrêtée"):
        PR.lancer(texte, racine, _copie(), str(d), **REDUIT)
    assert sorted(os.listdir(d)) == ["etape-3", "etape-4"]
    assert (d / "etape-4" / "arret.txt").read_text(encoding="utf-8") == f"{nom} : {nom} planté\n"
    assert _manifeste(str(d / "etape-4"))[0]["configuration"]["issue"] == "arrêt"
    assert not (d / "etape-4" / "resultat-etape-4.json").exists()


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
