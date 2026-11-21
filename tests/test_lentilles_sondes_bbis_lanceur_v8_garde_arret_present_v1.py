"""Essais du lanceur de la première passe, version 7 : garde du fichier d'arrêt déjà présent (mot de Lazar, GO-2026-11-21-06).

La garde : au départ de la sous-commande `calcul`, si un `arret.json` existe déjà au chemin où l'arrêt de cette course serait
écrit (`<sortie>/versement/<run>/calcul-interrompu/arret.json`), le lanceur refuse de partir, avant toute lecture de registre,
toute requête, tout chargement et tout calcul ; rien n'est écrit, rien n'est supprimé.

R5 : cas sain (sans `arret.json`, le calcul part), artefact de l'entrée (avec `arret.json`, refus), et artefact du code (une
copie jetable du lanceur sans la garde : le contrôle du refus tombe). Les copies jetables sont tenues en mémoire.
Les aides sont celles du fichier des essais repris du lanceur.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import test_lentilles_sondes_bbis_lanceur_v8_v1 as base  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v6 as la6  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v8 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

J, CAS, PAQUET = base.J, base.CAS, base.PAQUET
OUTIL = J.RACINE / "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-v7-v1.py"
APPEL_DE_LA_GARDE = "    exiger_aucun_fichier_d_arret(ctx)\n"


def _copie_sans_la_garde():
    """Artefact : le lanceur de la version 7 sans l'appel de la garde (la forme de la version 6)."""
    return base._copie_jetable(APPEL_DE_LA_GARDE, "")


def _etat_du_disque(racine: Path) -> dict:
    """Tout ce qui existe sous `racine` : chemin → empreinte du contenu (ou « dossier »)."""
    return {str(p.relative_to(racine)): ("dossier" if p.is_dir() else hashlib.sha256(p.read_bytes()).hexdigest())
            for p in sorted(racine.rglob("*"))}


def _message(fichier: Path) -> str:
    return f"un fichier d'arrêt existe déjà pour cette course ({fichier}) : rien ne part ; rien n'est écrit, rien n'est supprimé"


def _exiger_refus(code: int, sortie, fichier: Path, avant: dict, racine: Path, appels: list) -> None:
    """La garde éprouvée : code 3, le message de la garde sur la sortie d'erreur (comme tout arrêt ordinaire), rien sur la
    sortie standard ; le calcul n'est pas entré (aucun appel) ; le disque est tel qu'avant, octet pour octet."""
    assert code == 3 and sortie.out == ""
    assert sortie.err == f"ARRÊT : {_message(fichier)}\n"
    assert appels == []
    assert _etat_du_disque(racine) == avant


def _calcul_suivi(appels: list, arret: BaseException | None = None):
    """Tient lieu de `_calculer` : note qu'il est entré ; lève l'arrêt donné, ou rend un rendu vide."""
    def calcul(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat):
        appels.append("_calculer")
        if arret is not None:
            return base._faux_calcul(arret)(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat)
        return {"morceaux": []}
    return calcul


# --- le chemin gardé est celui où l'arrêt est écrit ---------------------------------------------------------------------------------------------
def test_le_chemin_garde_est_celui_ou_l_enveloppe_ecrit_l_arret(tmp_path, monkeypatch, capsys):
    d = base._dossiers(tmp_path)
    ctx = la.Contexte(d.travail, d.sortie, J.RUN, tmp_path, tmp_path / "p.md")
    assert la.chemin_du_fichier_d_arret(ctx) == d.fichier == d.sortie / "versement" / J.RUN / "calcul-interrompu" / "arret.json"
    for nom, arret in (("cloisonne", CAS["direction-lue"].arret()), ("ordinaire", Arret("valeur non finie dans un nul : arrêt"))):
        dd = base._dossiers(tmp_path / nom)
        monkeypatch.setattr(la, "_calculer", base._faux_calcul(arret))
        base._ligne_de_commande(la, dd, capsys)
        assert dd.fichier.is_file() and dd.fichier == la.chemin_du_fichier_d_arret(
            la.Contexte(dd.travail, dd.sortie, J.RUN, tmp_path, tmp_path / "p.md"))


# --- cas sain : sans `arret.json`, le calcul part ------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("deja_la", ["rien", "dossier-de-sortie-vide", "dossier-calcul-interrompu-sans-fichier-d-arret", "autre-course"])
def test_sain_sans_fichier_d_arret_le_calcul_part(deja_la, tmp_path, monkeypatch, capsys):
    """Sans `arret.json` au chemin gardé, la garde laisse partir : dossier de sortie absent, vide, dossier `calcul-interrompu`
    présent sans `arret.json`, ou `arret.json` d'une autre course (autre identifiant) dans le même dossier de sortie."""
    d, appels = base._dossiers(tmp_path), []
    if deja_la == "dossier-de-sortie-vide":
        d.sortie.mkdir()
    elif deja_la == "dossier-calcul-interrompu-sans-fichier-d-arret":
        d.fichier.parent.mkdir(parents=True)
        (d.fichier.parent / "autre-fichier.txt").write_text("autre\n")
    elif deja_la == "autre-course":
        autre = d.sortie / "versement" / "20261119-000000-autre-course" / "calcul-interrompu" / "arret.json"
        autre.parent.mkdir(parents=True)
        autre.write_text("{}\n")
    monkeypatch.setattr(la, "_calculer", _calcul_suivi(appels))
    code, sortie = base._ligne_de_commande(la, d, capsys)
    assert code == 0 and appels == ["_calculer"] and sortie.err == "" and json.loads(sortie.out) == {"morceaux": []}


# --- artefact de l'entrée : avec `arret.json`, le lanceur refuse -------------------------------------------------------------------------------
@pytest.mark.parametrize("forme", ["fichier", "fichier-vide", "lien-casse"])
def test_fichier_d_arret_present_refus_sans_rien_ecrire_ni_supprimer_avant_toute_requete(forme, tmp_path, monkeypatch, capsys):
    """Un `arret.json` au chemin gardé (plein, vide, ou lien symbolique cassé, que l'écriture « sans écraser » refuserait
    aussi) : refus. Avant toute requête : ni la fiche du code ni aucun registre n'est lu (`exiger_fiche_code` et les fonctions
    des entrées sont piégées), et `_calculer` n'est pas appelé. Rien n'est écrit ni supprimé : le disque est égal avant et après."""
    d, appels = base._dossiers(tmp_path), []
    d.fichier.parent.mkdir(parents=True)
    if forme == "lien-casse":
        d.fichier.symlink_to(tmp_path / "cible-absente.json")
    else:
        d.fichier.write_text("" if forme == "fichier-vide" else json.dumps({"run": J.RUN, "motif": "arrêt d'avant"}) + "\n")
    avant = _etat_du_disque(tmp_path) if forme != "lien-casse" else None
    monkeypatch.setattr(la, "_calculer", _calcul_suivi(appels))
    for nom in ("exiger_fiche_code", "charger_montage", "verser_travail", "ecrire_morceaux", "_ecrire_ferme", "nettoyer"):
        monkeypatch.setattr(la, nom, lambda *a, _n=nom, **k: appels.append(_n))
    for nom in ("exiger_registre_propre", "exiger_scores_et_verdict", "ouvrir_entrees", "exiger_addendum"):
        monkeypatch.setattr(la.en, nom, lambda *a, _n=nom, **k: appels.append(_n))
    code, sortie = base._ligne_de_commande(la, d, capsys)
    if forme == "lien-casse":
        assert code == 3 and sortie.err == f"ARRÊT : {_message(d.fichier)}\n" and appels == [] and d.fichier.is_symlink()
    else:
        _exiger_refus(code, sortie, d.fichier, avant, tmp_path, appels)
    assert (d.travail / la.MARQUE).is_file() and (d.travail / "tenseurs" / "poids-jouet.bin").is_file()


def test_fichier_d_arret_present_refus_pour_l_appelant_python_arret_ordinaire_non_cloisonne(tmp_path, monkeypatch):
    """Pour l'appelant Python : un `Arret` ordinaire, levé avant l'enveloppe ; ce n'est pas un arrêt cloisonné."""
    d, appels = base._dossiers(tmp_path), []
    d.fichier.parent.mkdir(parents=True)
    d.fichier.write_text("{}\n")
    monkeypatch.setattr(la, "_calculer", _calcul_suivi(appels))
    ctx = la.Contexte(d.travail, d.sortie, J.RUN, tmp_path, tmp_path / "p.md")
    with pytest.raises(Arret) as e:
        la.calculer(ctx, tmp_path, tmp_path / "b.md")
    assert str(e.value) == _message(d.fichier) and type(e.value) is Arret and la.nom_d_arret_cloisonne(e.value) is None
    assert appels == [] and not hasattr(e.value, "fichier_d_arret")


# --- artefact du code : une copie jetable sans la garde fait tomber l'essai ----------------------------------------------------------------------
def test_artefact_copie_jetable_sans_la_garde_le_calcul_part_et_l_essai_tombe(tmp_path, monkeypatch, capsys):
    """R5 : sans l'appel de la garde (la forme de la version 6), le calcul part malgré le fichier d'arrêt présent."""
    d, appels, copie = base._dossiers(tmp_path), [], _copie_sans_la_garde()
    d.fichier.parent.mkdir(parents=True)
    d.fichier.write_text(json.dumps({"run": J.RUN, "motif": "arrêt d'avant"}) + "\n")
    avant = _etat_du_disque(tmp_path)
    monkeypatch.setattr(copie, "_calculer", _calcul_suivi(appels))
    code, sortie = base._ligne_de_commande(copie, d, capsys)
    assert code == 0 and appels == ["_calculer"]
    with pytest.raises(AssertionError):
        _exiger_refus(code, sortie, d.fichier, avant, tmp_path, appels)


# --- relance après un premier arrêt cloisonné dans le même dossier de sortie ----------------------------------------------------------------------
@pytest.mark.parametrize("sorte", sorted(CAS))
def test_relance_apres_un_premier_arret_cloisonne_la_seconde_course_refuse_de_partir(sorte, tmp_path, monkeypatch, capsys):
    """Première course : arrêt cloisonné, message entier dans `arret.json`, nom et chemin sur la ligne de commande. Seconde
    course, même dossier de sortie, même identifiant : la garde refuse avant que le calcul n'entre ; le premier `arret.json`
    et tout le versement restent tels quels ; le message de la garde ne porte que le chemin, aucun mot du premier arrêt."""
    cas, d, appels = CAS[sorte], base._dossiers(tmp_path), []
    premier = cas.arret()
    monkeypatch.setattr(la, "_calculer", base._faux_calcul(premier))
    code, sortie = base._ligne_de_commande(la, d, capsys)
    base._exiger_ligne_cloisonnee(code, sortie, cas, d.fichier)
    empreinte, avant = verifier(d.fichier), _etat_du_disque(tmp_path)
    monkeypatch.setattr(la, "_calculer", _calcul_suivi(appels, cas.arret()))
    code, sortie = base._ligne_de_commande(la, d, capsys)
    _exiger_refus(code, sortie, d.fichier, avant, tmp_path, appels)
    for mot in cas.interdits:
        assert mot not in sortie.err, mot
    assert verifier(d.fichier) == empreinte
    base._exiger_fichier_d_arret(d.fichier, premier, cas)


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_artefact_relance_sans_la_garde_le_second_arret_ne_peut_pas_ecrire_son_message(sorte, tmp_path, monkeypatch, capsys):
    """R5 : la copie jetable sans la garde laisse repartir la seconde course ; son arrêt ne peut pas écrire son `arret.json`
    (« fichier d'arrêt non écrit ») : c'est le message perdu que la garde évite, et le contrôle du refus tombe."""
    cas, d, appels, copie = CAS[sorte], base._dossiers(tmp_path), [], _copie_sans_la_garde()
    monkeypatch.setattr(copie, "_calculer", base._faux_calcul(cas.arret()))
    base._ligne_de_commande(copie, d, capsys)
    avant = _etat_du_disque(tmp_path)
    monkeypatch.setattr(copie, "_calculer", _calcul_suivi(appels, cas.arret()))
    code, sortie = base._ligne_de_commande(copie, d, capsys)
    assert appels == ["_calculer"] and "fichier d'arrêt non écrit" in sortie.err
    with pytest.raises(AssertionError):
        _exiger_refus(code, sortie, d.fichier, avant, tmp_path, appels)


def test_relance_apres_un_arret_ordinaire_la_seconde_course_refuse_aussi(tmp_path, monkeypatch, capsys):
    """Le chemin gardé est le même pour un arrêt ordinaire versé après le départ : la relance est refusée de la même façon."""
    d, appels = base._dossiers(tmp_path), []
    monkeypatch.setattr(la, "_calculer", base._faux_calcul(Arret("valeur non finie dans un nul : arrêt")))
    code, sortie = base._ligne_de_commande(la, d, capsys)
    assert code == 3 and sortie.err == "ARRÊT : valeur non finie dans un nul : arrêt\n" and d.fichier.is_file()
    avant = _etat_du_disque(tmp_path)
    monkeypatch.setattr(la, "_calculer", _calcul_suivi(appels))
    code, sortie = base._ligne_de_commande(la, d, capsys)
    _exiger_refus(code, sortie, d.fichier, avant, tmp_path, appels)


def test_bout_en_bout_relance_apres_un_arret_d_une_direction_lue_refus_avant_toute_lecture(tmp_path, monkeypatch, capsys):
    """Calcul entier sur le monde miniature : première course arrêtée par une égalité d'une direction lue (déclarée par la
    garde d'égalité elle-même, la quarantième liste relevée) ; seconde course, même dossier, sans plus aucune égalité : le
    lanceur refuse de partir, sans lire ni registre ni entrée, et le disque ne change pas."""
    m = base._monde_monte(tmp_path)
    origine, appels = st.premiers_gardes, {"n": 0}

    def garde_qui_voit_une_egalite(valeurs, k):
        g = origine(valeurs, k)
        appels["n"] += 1
        if appels["n"] == 40:
            g |= {"egalite": True, "rangs_a_egalite": (int(g["rangs"][-1]), int(g["rangs"][-2])), "valeur_commune": float(g["valeurs"][-1])}
        return g
    monkeypatch.setattr(st, "premiers_gardes", garde_qui_voit_une_egalite)
    code, sortie, arret = base._calcul_par_la_ligne_de_commande(m, monkeypatch, capsys)
    fichier = la.chemin_du_fichier_d_arret(m.ctx)
    assert code == 3 and isinstance(arret, st.EgaliteDirectionLue) and sortie.err == f"ARRÊT : EgaliteDirectionLue ; fichier d'arrêt : {fichier}\n"
    monkeypatch.setattr(st, "premiers_gardes", origine)
    avant, lus = _etat_du_disque(tmp_path), []
    monkeypatch.setattr(la, "exiger_fiche_code", lambda *a, **k: lus.append("fiche du code"))
    code, sortie, arret = base._calcul_par_la_ligne_de_commande(m, monkeypatch, capsys)
    assert type(arret) is Arret
    _exiger_refus(code, sortie, fichier, avant, tmp_path, lus)


# --- sans fichier d'arrêt, la version 7 rend ce que rend la version 6 ----------------------------------------------------------------------------
def test_sans_fichier_d_arret_memes_sorties_qu_a_la_version_6(tmp_path, monkeypatch, capsys):
    """Arrêt cloisonné, arrêt ordinaire, refus avant le départ : sortie de la ligne de commande et `arret.json` égaux à ceux de
    `lanceur_v6`, octet pour octet (les chemins sont rendus relatifs)."""
    for nom, arret, parti in (("lue", CAS["direction-lue"].arret, True), ("nulle", CAS["direction-nulle"].arret, True),
                              ("ordinaire", lambda: Arret("valeur non finie dans un nul : arrêt"), True),
                              ("avant-le-depart", lambda: Arret("dossier de travail monté absent : rien ne part"), False)):
        rendus = []
        for version, lanceur in (("v6", la6), ("v7", la)):
            d = base._dossiers(tmp_path / f"{nom}-{version}")
            monkeypatch.setattr(lanceur, "_calculer", base._faux_calcul(arret(), parti))
            code, sortie = base._ligne_de_commande(lanceur, d, capsys)
            lu = json.loads(d.fichier.read_text(encoding="utf-8"))["motif"] if d.fichier.is_file() else None
            rendus.append((code, sortie.out, sortie.err.replace(str(tmp_path / f"{nom}-{version}"), "<racine>"), lu))
        assert rendus[0] == rendus[1], nom
