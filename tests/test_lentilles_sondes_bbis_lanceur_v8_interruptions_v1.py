"""Essais du lanceur de la première passe, version 6 : une interruption du clavier qui tombe pendant le traitement d'un arrêt
cloisonné n'en porte pas le message dans sa trace (correction 1 de la contre-lecture du lanceur version 5, `d821cf66…`).

Cinq points d'injection, chacun avec son cas sain (`lanceur_v8` : la trace ne porte que l'interruption) et son artefact (une
copie jetable, tenue en mémoire, qui remet la forme de la version 5 à cet endroit : la trace porte le message entier, et le
contrôle du cas sain tombe) :
1. dans `ligne_d_arret_cloisonne` ;
2. dans `nom_d_arret_cloisonne`, à son appel de l'enveloppe du calcul, puis à son appel de la ligne de commande ;
3. dans l'impression (`print`) de la ligne de commande ;
4. entre le versement et le relevé de l'arrêt, dans `calculer` ;
5. sur la première ligne de `verser_arret_cloisonne`.
Plus : les mots fixes de la ligne affichée, tenus par des constantes ; l'outil de fabrique rejoué ; les lignes retirées.
Les aides (arrêts inventés, dossiers, faux calcul, copies jetables) sont celles du fichier des essais repris de la version 5.
"""
from __future__ import annotations

import difflib
import subprocess
import sys
import traceback
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import test_lentilles_sondes_bbis_lanceur_v8_v1 as base  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v8 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402

J, CAS, PAQUET = base.J, base.CAS, base.PAQUET
OUTIL = J.RACINE / "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-v6-v1.py"
SORTES = sorted(CAS)

# Les trois corrections de la version 6, et ce que chaque copie jetable remet à la place (la forme de la version 5).
PRINCIPAL_V6 = ("    except Arret as e:\n"
                "        arret = e                           # version 6 : rien d'autre dans ce bloc ; hors de lui, aucun arrêt n'est « en cours »\n"
                "    if arret is not None:\n"
                "        print(f\"ARRÊT : {arret}\" if nom_d_arret_cloisonne(arret) is None else ligne_d_arret_cloisonne(arret), file=sys.stderr)\n"
                "        return 3\n")
PRINCIPAL_V5 = ("    except Arret as e:\n"
                "        print(f\"ARRÊT : {e}\" if nom_d_arret_cloisonne(e) is None else ligne_d_arret_cloisonne(e), file=sys.stderr)\n"
                "        return 3\n")
ENVELOPPE_V6 = ("        try:                                # version 6 : le tri et le versement sous la coupure de l'enchaînement\n"
                "            cloisonne = nom_d_arret_cloisonne(arret) is not None\n"
                "            if cloisonne:\n"
                "                verser_arret_cloisonne(ctx, arret, tableaux, etat[\"parti\"])\n"
                "        except BaseException as e:          # interruption entre l'arrêt et son relevé : sa trace ne porte pas le message\n"
                "            raise e from None\n"
                "        if cloisonne:\n"
                "            raise\n")
ENVELOPPE_V5 = ("        if nom_d_arret_cloisonne(arret) is not None:\n"
                "            verser_arret_cloisonne(ctx, arret, tableaux, etat[\"parti\"])\n"
                "            raise\n")
PREMIERE_LIGNE_V6 = ("    try:                                    # version 6 : rien de cette fonction n'est hors de la coupure, première ligne comprise\n"
                     "        arret.fichier_d_arret, arret.versement_en_echec = None, False\n")
PREMIERE_LIGNE_V5 = ("    arret.fichier_d_arret, arret.versement_en_echec = None, False\n"
                     "    try:\n")


def _interrompre(*a, **k):
    raise KeyboardInterrupt()


def _interrompre_au_rang(origine, rang: int):
    """Rend une fonction qui appelle `origine`, sauf à son `rang`-ième appel, où l'interruption tombe."""
    appels = {"n": 0}

    def f(*a, **k):
        appels["n"] += 1
        if appels["n"] == rang:
            raise KeyboardInterrupt()
        return origine(*a, **k)
    return f


def _trace(lanceur, d) -> str:
    """Le calcul par la ligne de commande, où une interruption doit tomber : rend la trace que Python afficherait."""
    with pytest.raises(KeyboardInterrupt) as e:
        lanceur.principal(["calcul", "--travail", str(d.travail), "--sortie", str(d.sortie), "--run", J.RUN, "--depot",
                           str(d.sortie.parent), "--registre-propre", str(d.sortie.parent / "p.md"), "--entrees",
                           str(d.sortie.parent), "--registre-bbis", str(d.sortie.parent / "b.md")])
    return "".join(traceback.format_exception(e.value))


def _exiger_fuite(trace: str, cas) -> None:
    """Contrôle de l'artefact : la copie jetable fuit bien (le message entier est dans la trace), et le contrôle du cas sain
    tombe sur elle."""
    assert cas.exiges[0] in trace and "During handling of the above exception" in trace
    with pytest.raises(AssertionError):
        base._exiger_trace_sans_message(trace, cas)


# Points d'injection joués par la ligne de commande : (nom, pose de l'interruption sur le lanceur, copie jetable qui fuit).
def _poser_ligne(lanceur, monkeypatch):
    monkeypatch.setattr(lanceur, "ligne_d_arret_cloisonne", _interrompre)


def _poser_nom_dans_l_enveloppe(lanceur, monkeypatch):
    monkeypatch.setattr(lanceur, "nom_d_arret_cloisonne", _interrompre_au_rang(lanceur.nom_d_arret_cloisonne, 1))


def _poser_nom_dans_la_ligne_de_commande(lanceur, monkeypatch):
    monkeypatch.setattr(lanceur, "nom_d_arret_cloisonne", _interrompre_au_rang(lanceur.nom_d_arret_cloisonne, 2))


def _poser_impression(lanceur, monkeypatch):
    monkeypatch.setattr(lanceur, "print", _interrompre, raising=False)       # le nom `print` du module, lu avant celui de Python


def _poser_apres_le_versement(lanceur, monkeypatch):
    origine = lanceur.verser_arret_cloisonne

    def verser_puis_interrompre(*a, **k):
        origine(*a, **k)                                                      # le versement est fait, `arret.json` est écrit
        raise KeyboardInterrupt()
    monkeypatch.setattr(lanceur, "verser_arret_cloisonne", verser_puis_interrompre)


POINTS = {
    "ligne-affichee": (_poser_ligne, (PRINCIPAL_V6, PRINCIPAL_V5)),
    "nom-dans-l-enveloppe-du-calcul": (_poser_nom_dans_l_enveloppe, (ENVELOPPE_V6, ENVELOPPE_V5)),
    "nom-dans-la-ligne-de-commande": (_poser_nom_dans_la_ligne_de_commande, (PRINCIPAL_V6, PRINCIPAL_V5)),
    "impression": (_poser_impression, (PRINCIPAL_V6, PRINCIPAL_V5)),
    "entre-le-versement-et-le-releve": (_poser_apres_le_versement, (ENVELOPPE_V6, ENVELOPPE_V5)),
}


@pytest.mark.parametrize("sorte", SORTES)
@pytest.mark.parametrize("point", sorted(POINTS))
def test_interruption_pendant_le_traitement_d_un_arret_cloisonne_la_trace_ne_porte_pas_le_message(point, sorte, tmp_path, monkeypatch, capsys):
    cas, d = CAS[sorte], base._dossiers(tmp_path)
    monkeypatch.setattr(la, "_calculer", base._faux_calcul(cas.arret()))
    POINTS[point][0](la, monkeypatch)
    trace = _trace(la, d)
    base._exiger_trace_sans_message(trace, cas)
    sortie = capsys.readouterr()
    assert sortie.out == "" and sortie.err == ""
    if point != "nom-dans-l-enveloppe-du-calcul":                             # ailleurs, le versement a eu lieu avant l'interruption
        base._exiger_fichier_d_arret(d.fichier, cas.arret(), cas)


@pytest.mark.parametrize("sorte", SORTES)
@pytest.mark.parametrize("point", sorted(POINTS))
def test_artefact_forme_de_la_version_5_la_meme_interruption_porte_le_message(point, sorte, tmp_path, monkeypatch):
    """R5 : la copie jetable remet, à l'endroit de l'injection, la forme de la version 5 ; la trace porte le message entier."""
    cas, d = CAS[sorte], base._dossiers(tmp_path)
    copie = base._copie_jetable(*POINTS[point][1])
    monkeypatch.setattr(copie, "_calculer", base._faux_calcul(cas.arret()))
    POINTS[point][0](copie, monkeypatch)
    _exiger_fuite(_trace(copie, d), cas)


# --- la première ligne de `verser_arret_cloisonne` ---------------------------------------------------------------------------------------------
def _arret_qui_interrompt_a_sa_premiere_ecriture(cas):
    """Un arrêt de la classe éprouvée, dont la première écriture d'un champ (la première ligne de `verser_arret_cloisonne`)
    est interrompue."""
    origine = cas.arret()

    class Interrompu(type(origine)):
        def __init__(self):                                   # mêmes champs, même message que l'arrêt d'origine
            Arret.__init__(self, str(origine))

        def __setattr__(self, nom, valeur):
            if nom == "fichier_d_arret":
                raise KeyboardInterrupt()
            super().__setattr__(nom, valeur)
    return Interrompu()


def _trace_du_versement_seul(lanceur, cas, d) -> str:
    """`verser_arret_cloisonne` appelée seule, pendant le traitement de l'arrêt (comme dans l'enveloppe), sans la coupure de
    l'enveloppe : seule sa propre coupure peut tenir le message hors de la trace."""
    ctx = lanceur.Contexte(d.travail, d.sortie, J.RUN, d.sortie.parent, d.sortie.parent / "p.md")
    arret = _arret_qui_interrompt_a_sa_premiere_ecriture(cas)
    assert str(arret) == str(cas.arret()) and lanceur.nom_d_arret_cloisonne(arret) == cas.nom
    with pytest.raises(KeyboardInterrupt) as e:
        try:
            raise arret
        except Arret as en_cours:
            lanceur.verser_arret_cloisonne(ctx, en_cours, {}, True)
    return "".join(traceback.format_exception(e.value))


@pytest.mark.parametrize("sorte", SORTES)
def test_interruption_sur_la_premiere_ligne_du_versement_la_trace_ne_porte_pas_le_message(sorte, tmp_path, monkeypatch):
    cas, d = CAS[sorte], base._dossiers(tmp_path)
    base._exiger_trace_sans_message(_trace_du_versement_seul(la, cas, d), cas)
    # et par la ligne de commande entière (les deux coupures ensemble)
    monkeypatch.setattr(la, "_calculer", base._faux_calcul(_arret_qui_interrompt_a_sa_premiere_ecriture(cas)))
    base._exiger_trace_sans_message(_trace(la, base._dossiers(tmp_path / "ligne-de-commande")), cas)


@pytest.mark.parametrize("sorte", SORTES)
def test_artefact_premiere_ligne_hors_du_bloc_la_meme_interruption_porte_le_message(sorte, tmp_path):
    """R5 : la copie jetable remet l'affectation initiale avant le `try`, comme à la version 5."""
    cas, d = CAS[sorte], base._dossiers(tmp_path)
    copie = base._copie_jetable(PREMIERE_LIGNE_V6, PREMIERE_LIGNE_V5)
    _exiger_fuite(_trace_du_versement_seul(copie, cas, d), cas)


# --- sans interruption, la version 6 rend ce que rendait la version 5 --------------------------------------------------------------------------
def test_mots_fixes_de_la_ligne_affichee_inchanges_et_tenus_par_des_constantes(tmp_path, monkeypatch, capsys):
    """Les quatre lignes de la version 5, mot pour mot ; et, pour n'afficher que le nom de l'arrêt, une seule constante à
    changer (nœud posé au directeur : la constante garde ici les mots fixes)."""
    from controle_ia.lentilles_sondes_bbis import lanceur_v5 as la5
    for sorte in SORTES:
        for fichier in (None, tmp_path / "versement" / "arret.json"):
            for echec in (False, True):
                arret = CAS[sorte].arret()
                arret.fichier_d_arret, arret.versement_en_echec = fichier, echec
                assert la.ligne_d_arret_cloisonne(arret) == la5.ligne_d_arret_cloisonne(arret)
    assert la.ligne_d_arret_cloisonne(CAS["direction-lue"].arret()) == "ARRÊT : EgaliteDirectionLue ; fichier d'arrêt non écrit"
    assert (la.LIGNE_ARRET_CLOISONNE, la.MOTS_FICHIER_D_ARRET_ECRIT, la.MOTS_FICHIER_D_ARRET_NON_ECRIT, la.MOTS_VERSEMENT_EN_ECHEC) == (
        "ARRÊT : {nom} ; {fichier}{echec}", "fichier d'arrêt : {chemin}", "fichier d'arrêt non écrit",
        " ; versement à l'arrêt en échec : rien n'est supprimé")
    # une seule constante changée : la ligne de commande n'affiche plus que le nom
    cas, d = CAS["direction-nulle"], base._dossiers(tmp_path)
    monkeypatch.setattr(la, "LIGNE_ARRET_CLOISONNE", "{nom}")
    monkeypatch.setattr(la, "_calculer", base._faux_calcul(cas.arret()))
    code, sortie = base._ligne_de_commande(la, d, capsys)
    assert (code, sortie.out, sortie.err) == (3, "", "EgaliteNulleDecisive\n")
    base._exiger_fichier_d_arret(d.fichier, cas.arret(), cas)


def test_autre_arret_meme_sortie_qu_aux_versions_4_et_5(tmp_path, monkeypatch, capsys):
    """Un arrêt qui n'est pas cloisonné : la sortie de la ligne de commande est celle des versions 4 et 5, octet pour octet,
    que le versement tienne ou qu'il échoue (message enchaîné)."""
    from controle_ia.lentilles_sondes_bbis import lanceur_v4 as la4
    from controle_ia.lentilles_sondes_bbis import lanceur_v5 as la5
    for echec in (False, True):
        rendus = []
        for nom, lanceur in (("v4", la4), ("v5", la5), ("v6", la)):
            d = base._dossiers(tmp_path / f"{nom}-{echec}")
            monkeypatch.setattr(lanceur, "_calculer", base._faux_calcul(Arret("valeur non finie dans un nul : arrêt")))
            if echec:
                monkeypatch.setattr(lanceur, "verser_travail", base._lever(Arret("inventaire existe déjà (R12)")))
            code, sortie = base._ligne_de_commande(lanceur, d, capsys)
            rendus.append((code, sortie.out, sortie.err))
        assert rendus[0] == rendus[1] == rendus[2] and rendus[2][0] == 3 and rendus[2][2].startswith("ARRÊT : valeur non finie")
