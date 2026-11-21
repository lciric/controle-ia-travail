"""Essais du lanceur de la première passe, version 5 : messages d'arrêt cloisonnés (GO-2026-11-20-56).

Ce que la version 5 change, et rien d'autre : le message entier d'un arrêt d'égalité au vingtième rang d'une direction lue
(`EgaliteDirectionLue`, addendum de concentration, EC-6, étage (i)) ou d'un arrêt des directions nulles
(`EgaliteNulleDecisive`, étage (ii)) va dans le seul `arret.json` ; la ligne de commande (sortie d'erreur et sortie standard)
n'affiche que le nom de l'arrêt et le chemin de ce fichier.

R5 : chaque garde a son cas sain et son artefact. Les artefacts sont des copies jetables du lanceur, tenues en mémoire (aucun
fichier écrit sous `src/`), qui défont une ligne de la version 5 : l'essai du cas sain, rejoué sur la copie, doit tomber.
Aucune donnée du programme : jouets seulement ; les identifiants de jeton, la valeur commune et les bornes de valeur p des
essais rapides sont inventés ici.
"""
from __future__ import annotations

import json
import subprocess
import sys
import traceback
import types
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v4 as J4  # noqa: E402
import lentilles_sondes_bbis_jouets_v7 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v4 as la4  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v7 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, Refus  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

PAQUET = Path(la.__file__).resolve().parent
OUTIL = J.RACINE / "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-v5-v1.py"
CONTEXTE = {"cellule": "P-S50", "pli": "e1", "role": "sonde", "vecteur": "w", "signe": "+", "lentille": K.LENTILLE_PUBLIQUE,
            "couche": 15}
JETONS, VALEUR = (89123, 77001), float(np.float32(0.4170219898223877))
P_BAS, P_HAUT = 0.000999000999000999, 0.001998001998001998       # 1/1001 et 2/1001 : de part et d'autre du seuil 0,001
STATISTIQUE = "part au-dessus du nul"


def _arret_lue() -> st.EgaliteDirectionLue:
    return st.EgaliteDirectionLue(st.LISTE_PAR_SCORE, JETONS, VALEUR, CONTEXTE)


def _arret_nulle() -> st.EgaliteNulleDecisive:
    return st.EgaliteNulleDecisive(STATISTIQUE, {K.NUL_ISOTROPE: {"p_bas": P_BAS, "p_haut": P_HAUT, "marquees": 1},
                                                 K.NUL_SIGNES: {"p_bas": 0.003996003996003996, "p_haut": 0.003996003996003996,
                                                                "marquees": 0}},
                                   st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, CONTEXTE)


# Pour chaque arrêt cloisonné : sa fabrique, son nom affiché, ce que `arret.json` doit porter, ce que la ligne de commande ne
# doit jamais porter.
CAS = {
    "direction-lue": SimpleNamespace(
        arret=_arret_lue, nom="EgaliteDirectionLue", exiges=(str(JETONS[0]), str(JETONS[1]), repr(VALEUR), st.MESSAGE_EGALITE_LUE),
        interdits=(str(JETONS[0]), str(JETONS[1]), repr(VALEUR), st.MESSAGE_EGALITE_LUE, "identifiants", "valeur commune",
                   st.LISTE_PAR_SCORE, "cellule", "P-S50")),
    "direction-nulle": SimpleNamespace(
        arret=_arret_nulle, nom="EgaliteNulleDecisive", exiges=(repr(P_BAS), repr(P_HAUT), st.MESSAGE_EGALITE_NULLE, STATISTIQUE),
        interdits=(repr(P_BAS), repr(P_HAUT), st.MESSAGE_EGALITE_NULLE, "p_bas", "p_haut", STATISTIQUE, "statistique",
                   st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, "cellule", "P-S50", "marquée")),
}


def _dossiers(tmp: Path) -> SimpleNamespace:
    """Dossier de travail marqué (un fichier à verser, un fichier jamais copié) et dossier de sortie vide."""
    travail, sortie = tmp / "travail", tmp / "sortie"
    (travail / "tenseurs").mkdir(parents=True, exist_ok=True)
    (travail / la.MARQUE).write_text("marque\n")
    (travail / "journal-jouet.txt").write_text("journal\n")
    (travail / "tenseurs" / "poids-jouet.bin").write_bytes(b"jamais copie")
    return SimpleNamespace(travail=travail, sortie=sortie, fichier=sortie / "versement" / J.RUN / "calcul-interrompu" / "arret.json")


def _faux_calcul(arret: BaseException, parti: bool = True):
    """Tient lieu de `_calculer` : marque le départ, range un tableau déjà calculé, puis lève l'arrêt donné."""
    def calcul(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat):
        if parti:
            etat["parti"] = True
            tableaux["scores__jouet"] = np.arange(6, dtype=np.float32)
        raise arret
    return calcul


def _ligne_de_commande(lanceur, d: SimpleNamespace, capsys) -> tuple[int, object]:
    capsys.readouterr()
    code = lanceur.principal(["calcul", "--travail", str(d.travail), "--sortie", str(d.sortie), "--run", J.RUN, "--depot",
                              str(d.sortie.parent), "--registre-propre", str(d.sortie.parent / "propre.md"), "--entrees",
                              str(d.sortie.parent), "--registre-bbis", str(d.sortie.parent / "bbis.md")])
    return code, capsys.readouterr()


def _exiger_ligne_cloisonnee(code: int, sortie, cas: SimpleNamespace, fichier: Path | None, echec: bool = False) -> None:
    """La garde éprouvée : code 3, rien sur la sortie standard, et sur la sortie d'erreur une seule ligne, faite de mots fixes,
    du nom de l'arrêt et du chemin du fichier d'arrêt ; aucun mot du message."""
    attendu = f"ARRÊT : {cas.nom} ; " + (f"fichier d'arrêt : {fichier}" if fichier is not None else "fichier d'arrêt non écrit")
    attendu += " ; versement à l'arrêt en échec : rien n'est supprimé" if echec else ""
    assert code == 3
    assert sortie.out == ""
    assert sortie.err == attendu + "\n"
    for mot in cas.interdits:
        assert mot not in sortie.err and mot not in sortie.out, mot


def _exiger_fichier_d_arret(fichier: Path, arret: Arret, cas: SimpleNamespace) -> dict:
    """La garde éprouvée : `arret.json`, fermé et scellé, porte le message entier de l'arrêt."""
    verifier(fichier)
    lu = json.loads(fichier.read_text(encoding="utf-8"))
    assert lu["motif"] == str(arret) and lu["run"] == J.RUN
    for mot in cas.exiges:
        assert mot in lu["motif"], mot
    return lu


def _copie_jetable(avant: str, apres: str, n: int = 1):
    """Artefact : le lanceur de la version 6 dont un passage, trouvé `n` fois exactement, est remplacé ; tenu en mémoire,
    jamais écrit sous `src/`. Le module est inscrit le temps de son chargement (les classes de données le demandent)."""
    source = Path(la.__file__).read_text(encoding="utf-8")
    assert source.count(avant) == n, (avant[:60], source.count(avant))
    nom = "controle_ia.lentilles_sondes_bbis.lanceur_v7_copie_jetable"
    module = types.ModuleType(nom)
    module.__file__, module.__package__ = la.__file__, la.__package__
    sys.modules[nom] = module
    try:
        exec(compile(source.replace(avant, apres), "<copie jetable de lanceur_v7>", "exec"), module.__dict__)
    finally:
        del sys.modules[nom]
    return module


LIGNE_DU_TRI = ("        print(f\"ARRÊT : {arret}\" if nom_d_arret_cloisonne(arret) is None else ligne_d_arret_cloisonne(arret), "
                "file=sys.stderr)\n")
BRANCHE_DE_L_ENVELOPPE = ("            cloisonne = nom_d_arret_cloisonne(arret) is not None\n"
                          "            if cloisonne:\n"
                          "                verser_arret_cloisonne(ctx, arret, tableaux, etat[\"parti\"])\n")


def _copie_qui_imprime_le_message():
    return _copie_jetable(LIGNE_DU_TRI, "        print(f\"ARRÊT : {arret}\", file=sys.stderr)\n")


def _copie_a_l_enveloppe_de_la_version_4():
    return _copie_jetable(BRANCHE_DE_L_ENVELOPPE, "            cloisonne = False\n")


# --- la liste des noms d'arrêt ----------------------------------------------------------------------------------------------------------
def test_noms_des_arrets_cloisonnes_codes_fixes_egaux_aux_noms_des_classes():
    assert la.ARRETS_CLOISONNES == ((st.EgaliteDirectionLue, "EgaliteDirectionLue"), (st.EgaliteNulleDecisive, "EgaliteNulleDecisive"))
    assert all(classe.__name__ == nom and issubclass(classe, Arret) for classe, nom in la.ARRETS_CLOISONNES)
    assert la.nom_d_arret_cloisonne(_arret_lue()) == "EgaliteDirectionLue"
    assert la.nom_d_arret_cloisonne(_arret_nulle()) == "EgaliteNulleDecisive"
    # cas contraires : tout autre arrêt n'est pas cloisonné, sa sortie est celle de la version 4
    assert la.nom_d_arret_cloisonne(Arret("valeur non finie dans un nul : arrêt")) is None
    assert la.nom_d_arret_cloisonne(Refus("VERDICT-BBIS absente")) is None and la.nom_d_arret_cloisonne(OSError("disque")) is None


def test_tout_arret_nomme_du_module_des_statistiques_est_cloisonne():
    """Artefact visé : une classe d'arrêt nommé ajoutée à `statistiques_v3` et oubliée ici sortirait son message entier."""
    nommes = {c for c in vars(st).values() if isinstance(c, type) and issubclass(c, Arret) and c is not Arret}
    assert nommes == {classe for classe, _ in la.ARRETS_CLOISONNES}


# --- la ligne de commande n'affiche que le nom de l'arrêt et le chemin du fichier d'arrêt ---------------------------------------------------
@pytest.mark.parametrize("sorte", sorted(CAS))
def test_arret_cloisonne_la_ligne_de_commande_n_affiche_que_le_nom_et_le_chemin(sorte, tmp_path, monkeypatch, capsys):
    cas, d = CAS[sorte], _dossiers(tmp_path)
    arret = cas.arret()
    monkeypatch.setattr(la, "_calculer", _faux_calcul(arret))
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, d.fichier)
    assert sortie.err.count("\n") == 1


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_arret_cloisonne_le_fichier_d_arret_porte_le_message_entier_et_le_versement(sorte, tmp_path, monkeypatch, capsys):
    cas, d = CAS[sorte], _dossiers(tmp_path)
    arret = cas.arret()
    monkeypatch.setattr(la, "_calculer", _faux_calcul(arret))
    _ligne_de_commande(la, d, capsys)
    lu = _exiger_fichier_d_arret(d.fichier, arret, cas)
    assert set(lu) == {"run", "motif", "morceaux", "travail"}                 # la forme de la version 4, sans champ de plus
    assert [m["tableaux"] for m in lu["morceaux"]] == [["scores__jouet"]]
    for morceau in lu["morceaux"]:
        verifier(d.fichier.parent / morceau["fichier"])
    inventaire = json.loads((d.sortie / lu["travail"]["chemin"]).read_text(encoding="utf-8"))
    assert verifier(d.sortie / lu["travail"]["chemin"]) == lu["travail"]["sha256"]
    assert {f["chemin"] for f in inventaire["fichiers"]} == {la.MARQUE, "journal-jouet.txt", "tenseurs/poids-jouet.bin"}
    assert (d.travail / "tenseurs" / "poids-jouet.bin").is_file()                 # rien n'est supprimé
    # le message n'est écrit nulle part ailleurs sous le dossier de sortie
    for p in d.sortie.rglob("*"):
        if p.is_file() and p != d.fichier and p.suffix != ".npz":
            assert cas.exiges[0] not in p.read_text(encoding="utf-8", errors="replace"), p


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_arret_cloisonne_releve_tel_quel_pour_l_appelant_python(sorte, tmp_path, monkeypatch):
    """`calculer` relève l'arrêt d'origine, de sa classe, avec ses champs : seul l'affichage de la ligne de commande change."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    arret = cas.arret()
    monkeypatch.setattr(la, "_calculer", _faux_calcul(arret))
    ctx = la.Contexte(d.travail, d.sortie, J.RUN, tmp_path, tmp_path / "propre.md")
    with pytest.raises(type(arret)) as e:
        la.calculer(ctx, tmp_path, tmp_path / "bbis.md")
    assert e.value is arret and e.value.fichier_d_arret == d.fichier and e.value.versement_en_echec is False
    assert e.value.__cause__ is None and e.value.__context__ is None


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_artefact_copie_jetable_qui_imprime_le_message_entier_fait_tomber_l_essai(sorte, tmp_path, monkeypatch, capsys):
    """R5, artefact de la garde de la ligne de commande : la copie imprime le message entier, comme `lanceur_v4`."""
    cas, d, copie = CAS[sorte], _dossiers(tmp_path), _copie_qui_imprime_le_message()
    arret = cas.arret()
    monkeypatch.setattr(copie, "_calculer", _faux_calcul(arret))
    code, sortie = _ligne_de_commande(copie, d, capsys)
    assert code == 3 and sortie.err == f"ARRÊT : {arret}\n"                    # la copie fait bien ce que faisait la version 4
    with pytest.raises(AssertionError):
        _exiger_ligne_cloisonnee(code, sortie, cas, d.fichier)
    _exiger_fichier_d_arret(d.fichier, arret, cas)                                # le fichier d'arrêt, lui, reste entier


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_artefact_copie_jetable_dont_le_fichier_d_arret_ne_porte_que_le_nom_fait_tomber_l_essai(sorte, tmp_path, monkeypatch, capsys):
    """R5, artefact de la garde du fichier d'arrêt : la copie écrit le nom de l'arrêt à la place du message entier."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    copie = _copie_jetable('contenu = {"run": ctx.run, "motif": str(arret), "morceaux": [], "travail": None}',
                           'contenu = {"run": ctx.run, "motif": nom_d_arret_cloisonne(arret), "morceaux": [], "travail": None}')
    arret = cas.arret()
    monkeypatch.setattr(copie, "_calculer", _faux_calcul(arret))
    code, sortie = _ligne_de_commande(copie, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, d.fichier)
    with pytest.raises(AssertionError):
        _exiger_fichier_d_arret(d.fichier, arret, cas)


# --- les autres arrêts gardent leur sortie -----------------------------------------------------------------------------------------------
def test_autre_arret_registre_sans_la_ligne_de_l_addendum_meme_sortie_qu_a_la_version_4(tmp_path, capsys):
    """Un registre propre sans la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` : refus, message entier sur la sortie d'erreur,
    octet pour octet celui de `lanceur_v4`."""
    bbis, propre = J.ecrire_registres(tmp_path / "r", propres=("ABSENCE-VERDICT-LENTILLES-BBIS", "SCELLEMENT-LENTILLES-BBIS",
                                                               "GO-LENTILLES-BBIS", "CODE-LENTILLES-BBIS"))
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    rendus = []
    for lanceur in (la4, la):
        capsys.readouterr()
        code = lanceur.principal(["recuperer", "--url", "url-jamais-contactee", "--entrees", str(tmp_path / "e"),
                                  "--registre-bbis", str(bbis), "--registre-propre", str(propre), "--depot", str(tmp_path / "depot")])
        sortie = capsys.readouterr()
        rendus.append((code, sortie.out, sortie.err))
    assert rendus[0] == rendus[1]
    code, out, err = rendus[1]
    assert code == 3 and out == "" and err.startswith("ARRÊT : ") and "ADDENDUM-CONCENTRATION-LENTILLES-BBIS" in err
    assert "fichier d'arrêt" not in err
    assert not (tmp_path / "e").exists()


@pytest.mark.parametrize("parti", [True, False])
def test_autre_arret_dans_le_calcul_meme_sortie_et_meme_fichier_d_arret_qu_a_la_version_4(parti, tmp_path, monkeypatch, capsys):
    """Un arrêt qui n'est pas cloisonné, après le départ (versé) ou avant (rien n'est versé) : sortie d'erreur et `arret.json`
    égaux à ceux de `lanceur_v4`."""
    message = "valeur non finie dans une lecture : arrêt"
    rendus = []
    for nom, lanceur in (("v4", la4), ("v5", la)):
        d = _dossiers(tmp_path / nom)
        monkeypatch.setattr(lanceur, "_calculer", _faux_calcul(Arret(message), parti))
        code, sortie = _ligne_de_commande(lanceur, d, capsys)
        lu = json.loads(d.fichier.read_text(encoding="utf-8")) if d.fichier.is_file() else None
        rendus.append((code, sortie.out, sortie.err, None if lu is None else (lu["run"], lu["motif"], sorted(lu))))
        assert d.fichier.is_file() is parti and (d.sortie / "versement").exists() is parti
    assert rendus[0] == rendus[1] and rendus[1][:3] == (3, "", f"ARRÊT : {message}\n")
    if parti:
        assert rendus[1][3] == (J.RUN, message, ["morceaux", "motif", "run", "travail"])


def test_autre_arret_echec_du_versement_message_enchaine_inchange(tmp_path, monkeypatch, capsys):
    """Pour un arrêt qui n'est pas cloisonné, le message enchaîné d'un échec du versement reste celui de `lanceur_v4`."""
    rendus = []
    for nom, lanceur in (("v4", la4), ("v5", la)):
        d = _dossiers(tmp_path / nom)
        monkeypatch.setattr(lanceur, "_calculer", _faux_calcul(Arret("espace disque : arrêt")))
        monkeypatch.setattr(lanceur, "verser_travail", _lever(Arret("inventaire existe déjà (R12)")))
        code, sortie = _ligne_de_commande(lanceur, d, capsys)
        rendus.append((code, sortie.out, sortie.err))
    assert rendus[0] == rendus[1] == (3, "", "ARRÊT : espace disque : arrêt ; versement à l'arrêt en échec (inventaire existe "
                                             "déjà (R12)) : rien n'est supprimé\n")


# --- un échec du versement ne fait pas sortir le message entier ---------------------------------------------------------------------------
def _lever(erreur: BaseException):
    def f(*a, **k):
        raise erreur
    return f


@pytest.mark.parametrize("sorte", sorted(CAS))
@pytest.mark.parametrize("erreur", [Arret("versement/…/travail-arret existe déjà (R12)"), OSError(28, "No space left on device")],
                         ids=["arret-R12", "erreur-du-disque"])
def test_echec_du_versement_simule_le_message_entier_ne_sort_pas(sorte, erreur, tmp_path, monkeypatch, capsys):
    """Le versement du dossier de travail échoue (R12, ou erreur du système qui n'est pas un arrêt) : la ligne de commande
    garde le nom, le chemin et des mots fixes ; `arret.json` porte le message entier et la raison de l'échec ; aucune trace."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    arret = cas.arret()
    monkeypatch.setattr(la, "_calculer", _faux_calcul(arret))
    monkeypatch.setattr(la, "verser_travail", _lever(erreur))
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, d.fichier, echec=True)
    assert "Traceback" not in sortie.err and str(erreur) not in sortie.err
    lu = _exiger_fichier_d_arret(d.fichier, arret, cas)
    assert lu["versement_en_echec"] == f"{type(erreur).__name__} : {erreur}" and lu["travail"] is None
    assert [m["tableaux"] for m in lu["morceaux"]] == [["scores__jouet"]]      # les tableaux écrits avant l'échec restent cités
    assert (d.travail / la.MARQUE).is_file()                                    # rien n'est supprimé


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_echec_du_versement_reel_second_arret_dans_le_meme_dossier_de_sortie(sorte, tmp_path, monkeypatch, capsys):
    """Échec non simulé, défense du versement : un `arret.json` et un versement sont déjà là quand le second arrêt est versé,
    comme s'ils étaient apparus après la garde du départ (version 7 : la garde, qui refuse la relance, est ici mise de côté ;
    elle a son propre fichier d'essais). Rien n'est réécrit (R12) : le premier `arret.json` reste, entier ; la seconde sortie
    d'erreur dit par des mots fixes que le fichier d'arrêt n'a pas été écrit et que le versement a échoué, sans un mot du message."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    premier = cas.arret()
    monkeypatch.setattr(la, "_calculer", _faux_calcul(premier))
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, d.fichier)
    empreinte = verifier(d.fichier)
    monkeypatch.setattr(la, "_calculer", _faux_calcul(cas.arret()))
    monkeypatch.setattr(la, "exiger_aucun_fichier_d_arret", lambda ctx: None)       # le fichier apparu après la garde du départ
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, None, echec=True)
    assert "Traceback" not in sortie.err and "existe déjà" not in sortie.err
    assert verifier(d.fichier) == empreinte
    _exiger_fichier_d_arret(d.fichier, premier, cas)


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_fichier_d_arret_impossible_a_ecrire_dit_par_des_mots_fixes(sorte, tmp_path, monkeypatch, capsys):
    """Le versement tient, mais `arret.json` ne peut pas être écrit (erreur du disque) : « fichier d'arrêt non écrit »."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    origine = la._ecrire_ferme

    def ecrire(chemin, contenu):
        if chemin.name == "arret.json":
            raise OSError(28, "No space left on device")
        return origine(chemin, contenu)
    monkeypatch.setattr(la, "_calculer", _faux_calcul(cas.arret()))
    monkeypatch.setattr(la, "_ecrire_ferme", ecrire)
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, None)
    assert "Traceback" not in sortie.err and not d.fichier.exists()


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_artefact_enveloppe_de_la_version_4_le_message_enchaine_fait_tomber_l_essai(sorte, tmp_path, monkeypatch, capsys):
    """R5, artefact de la garde de l'échec du versement : la copie jetable a l'enveloppe de `lanceur_v4`, dont le message
    enchaîné (« versement à l'arrêt en échec ») reprend le message d'origine, et qui n'est plus un arrêt cloisonné."""
    cas, d, copie = CAS[sorte], _dossiers(tmp_path), _copie_a_l_enveloppe_de_la_version_4()
    arret = cas.arret()
    monkeypatch.setattr(copie, "_calculer", _faux_calcul(arret))
    monkeypatch.setattr(copie, "verser_travail", _lever(Arret("versement/…/travail-arret existe déjà (R12)")))
    code, sortie = _ligne_de_commande(copie, d, capsys)
    assert code == 3 and str(arret) in sortie.err and "versement à l'arrêt en échec" in sortie.err
    with pytest.raises(AssertionError):
        _exiger_ligne_cloisonnee(code, sortie, cas, d.fichier, echec=True)


# --- aucune trace d'exception ne porte le message ------------------------------------------------------------------------------------------
def _trace_d_une_interruption(lanceur, cas, d, monkeypatch) -> str:
    """Une interruption du clavier tombe pendant le versement d'un arrêt cloisonné : rend la trace que Python afficherait."""
    monkeypatch.setattr(lanceur, "_calculer", _faux_calcul(cas.arret()))
    monkeypatch.setattr(lanceur, "verser_travail", _lever(KeyboardInterrupt()))
    with pytest.raises(KeyboardInterrupt) as e:
        lanceur.principal(["calcul", "--travail", str(d.travail), "--sortie", str(d.sortie), "--run", J.RUN, "--depot",
                           str(d.sortie.parent), "--registre-propre", str(d.sortie.parent / "p.md"), "--entrees",
                           str(d.sortie.parent), "--registre-bbis", str(d.sortie.parent / "b.md")])
    return "".join(traceback.format_exception(e.value))


def _exiger_trace_sans_message(trace: str, cas: SimpleNamespace) -> None:
    assert "KeyboardInterrupt" in trace
    assert "During handling of the above exception" not in trace and cas.nom not in trace
    for mot in cas.interdits:
        assert mot not in trace, mot


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_trace_d_une_interruption_pendant_le_versement_sans_le_message(sorte, tmp_path, monkeypatch, capsys):
    """La seule exception qui puisse quitter la ligne de commande pendant le traitement d'un arrêt cloisonné (une
    interruption, qui n'est pas de la classe `Exception`) n'enchaîne pas l'arrêt : sa trace n'en porte pas le message."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    _exiger_trace_sans_message(_trace_d_une_interruption(la, cas, d, monkeypatch), cas)
    sortie = capsys.readouterr()
    assert sortie.out == "" and sortie.err == ""


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_artefact_interruption_enchainee_a_l_arret_la_trace_porte_le_message(sorte, tmp_path, monkeypatch):
    """R5, artefact de la garde des traces : la copie jetable relève l'interruption sans couper l'enchaînement ; la trace
    porte alors le message entier de l'arrêt, et l'essai du cas sain tombe."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    copie = _copie_jetable("raise e from None\n", "raise\n", 2)          # les deux coupures : le versement, l'enveloppe
    trace = _trace_d_une_interruption(copie, cas, d, monkeypatch)
    assert cas.exiges[0] in trace
    with pytest.raises(AssertionError):
        _exiger_trace_sans_message(trace, cas)


@pytest.mark.parametrize("sorte", sorted(CAS))
def test_ligne_de_commande_en_processus_separe_aucune_trace_aucun_message(sorte, tmp_path):
    """La ligne de commande réelle (`python -m …lanceur_v7 calcul`), dans un processus séparé dont `_calculer` est remplacé
    par un amorçage : code 3, sortie standard vide, sortie d'erreur d'une seule ligne, sans trace ni message."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    fabrique = "_arret_lue" if sorte == "direction-lue" else "_arret_nulle"
    amorce = ("import sys\n"
              f"sys.path.insert(0, {str(Path(__file__).resolve().parent)!r})\n"
              "import test_lentilles_sondes_bbis_lanceur_v7_v1 as essais\n"
              "from controle_ia.lentilles_sondes_bbis import lanceur_v7 as la\n"
              f"la._calculer = essais._faux_calcul(essais.{fabrique}())\n"
              "sys.exit(la.principal(sys.argv[1:]))\n")
    r = subprocess.run([sys.executable, "-B", "-c", amorce, "calcul", "--travail", str(d.travail), "--sortie", str(d.sortie), "--run",
                        J.RUN, "--depot", str(tmp_path), "--registre-propre", str(tmp_path / "p.md"), "--entrees", str(tmp_path),
                        "--registre-bbis", str(tmp_path / "b.md")], capture_output=True, text=True, cwd=tmp_path,
                       env={"PYTHONPATH": str(J.RACINE / "src"), "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8",
                            "PATH": "/usr/bin:/bin"})
    _exiger_ligne_cloisonnee(r.returncode, SimpleNamespace(out=r.stdout, err=r.stderr), cas, d.fichier)
    assert "Traceback" not in r.stderr
    _exiger_fichier_d_arret(d.fichier, cas.arret(), cas)


# --- avant le départ du calcul ---------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("sorte", sorted(CAS))
def test_arret_cloisonne_avant_le_depart_ecrit_quand_meme_son_fichier_d_arret(sorte, tmp_path, monkeypatch, capsys):
    """Défense : aucun chemin du code ne lève un arrêt cloisonné avant le départ (essai suivant) ; s'il en venait un, son
    message entier irait quand même dans `arret.json`, sans rien verser du dossier de travail, et la ligne de commande n'en
    afficherait que le nom et le chemin."""
    cas, d = CAS[sorte], _dossiers(tmp_path)
    arret = cas.arret()
    monkeypatch.setattr(la, "_calculer", _faux_calcul(arret, parti=False))
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, d.fichier)
    lu = _exiger_fichier_d_arret(d.fichier, arret, cas)
    assert lu["avant_le_depart_du_calcul"] is True and lu["morceaux"] == [] and lu["travail"] is None
    assert not (d.sortie / "versement" / J.RUN / "travail-arret").exists()


def test_arret_cloisonne_hors_du_calcul_la_ligne_de_commande_n_affiche_que_le_nom(tmp_path, monkeypatch, capsys):
    """Défense : un arrêt cloisonné qui viendrait d'une autre sous-commande (aucun chemin du code n'y mène) n'afficherait que
    son nom, et dirait par des mots fixes qu'aucun fichier d'arrêt n'a été écrit."""
    cas = CAS["direction-lue"]
    monkeypatch.setattr(la, "exiger_fiche_code", _lever(cas.arret()))
    capsys.readouterr()
    code = la.principal(["recuperer", "--url", "url-jamais-contactee", "--entrees", str(tmp_path / "e"), "--registre-bbis",
                         str(tmp_path / "b.md"), "--registre-propre", str(tmp_path / "p.md")])
    _exiger_ligne_cloisonnee(code, capsys.readouterr(), cas, None)


@pytest.fixture(scope="module")
def monde_sain(tmp_path_factory):
    """Montage puis calcul entiers sur le monde miniature, sans arrêt ; les deux fonctions de `statistiques_v3` qui lèvent les
    arrêts cloisonnés sont suivies : à chaque appel, l'état « parti » de l'enveloppe est relevé."""
    tmp = tmp_path_factory.mktemp("lanceur-v5-sain")
    m = J.monde(tmp)
    m.ctx.maintenant = lambda: 0.0
    suivi = {"etape": "montage", "etat": None, "appels": []}
    origines = {"exiger_sans_egalite": st.exiger_sans_egalite, "libelle_sous_departage": st.libelle_sous_departage,
                "_calculer": la._calculer}

    def suivre(nom):
        def f(*a, **k):
            suivi["appels"].append((suivi["etape"], nom, None if suivi["etat"] is None else bool(suivi["etat"]["parti"])))
            return origines[nom](*a, **k)
        return f

    def calculer_suivi(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat):
        suivi["etape"], suivi["etat"] = "calcul", etat
        return origines["_calculer"](ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat)
    patch = pytest.MonkeyPatch()
    patch.setattr(st, "exiger_sans_egalite", suivre("exiger_sans_egalite"))
    patch.setattr(st, "libelle_sous_departage", suivre("libelle_sous_departage"))
    patch.setattr(la, "_calculer", calculer_suivi)
    try:
        montage = la.monter(m.ctx)
        rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis, nettoyage=False)
    finally:
        patch.undo()
    return SimpleNamespace(m=m, tmp=tmp, montage=montage, rendu=rendu, suivi=suivi)


def test_aucun_arret_cloisonne_ne_peut_survenir_avant_le_depart_du_calcul(monde_sain):
    """Les deux arrêts cloisonnés ne sont construits que dans `statistiques_v3.exiger_sans_egalite` et
    `statistiques_v3.libelle_sous_departage`. Sur un montage et un calcul entiers : aucune des deux n'est appelée pendant le
    montage, et chaque appel du calcul vient après le départ (« parti » vrai)."""
    appels = monde_sain.suivi["appels"]
    assert {nom for _, nom, _ in appels} == {"exiger_sans_egalite", "libelle_sous_departage"}        # l'essai voit les deux
    assert all(etape == "calcul" and parti is True for etape, _, parti in appels)
    # et, dans les sources : les deux classes ne sont construites qu'à ces deux endroits du paquet
    for classe, fonction in (("EgaliteDirectionLue", "exiger_sans_egalite"), ("EgaliteNulleDecisive", "libelle_sous_departage")):
        levees = [(p.name, ligne) for p in sorted(PAQUET.glob("*.py")) for ligne in p.read_text(encoding="utf-8").splitlines()
                  if f"raise {classe}(" in ligne]
        assert [nom for nom, _ in levees] == ["statistiques_v3.py"], classe
        source = (PAQUET / "statistiques_v3.py").read_text(encoding="utf-8")
        assert source.index(f"def {fonction}(") < source.index(f"raise {classe}(")
    # dans le lanceur : les fonctions qui y mènent ne sont appelées qu'après la ligne du départ
    source = Path(la.__file__).read_text(encoding="utf-8")
    corps = source[source.index("def _calculer("):source.index("STATISTIQUE_NULLE = ")]
    depart = corps.index('etat["parti"] = True')
    assert depart < corps.index("_Couche(") and depart < corps.index("_etiqueter(")
    assert source.count("_Couche(") == 1 and source.count("_etiqueter(") == 2      # un appel chacun (et la définition de `_etiqueter`)
    for mot in ("exiger_sans_egalite", "lecture_signe", "poles_alignes", "libelle_sous_departage"):
        hors = source[:source.index("class _Couche:")] + source[source.index("def _comparaisons("):]
        assert f"st.{mot}(" not in hors, mot


# --- bout en bout : les deux arrêts, par le chemin du code -------------------------------------------------------------------------------------
def _monde_monte(tmp: Path) -> SimpleNamespace:
    m = J.monde(tmp)
    la.monter(m.ctx)
    return m


def _calcul_par_la_ligne_de_commande(m, monkeypatch, capsys):
    """Le calcul entier par `principal`, sur le monde miniature monté ; rend le code, les sorties et l'arrêt relevé."""
    releve = {}
    origine = la.calculer

    def calculer(*a, **k):
        try:
            return origine(*a, **k)
        except Arret as e:
            releve["arret"] = e
            raise
    monkeypatch.setattr(la, "calculer", calculer)
    monkeypatch.setattr(la, "Contexte", lambda *a, **k: m.ctx)
    capsys.readouterr()
    code = la.principal(["calcul", "--travail", str(m.ctx.travail), "--sortie", str(m.ctx.sortie), "--run", J.RUN, "--depot",
                         str(m.ctx.racine_depot), "--registre-propre", str(m.registre_propre), "--entrees", str(m.entrees),
                         "--registre-bbis", str(m.registre_bbis)])
    return code, capsys.readouterr(), releve.get("arret")


def _exiger_bout_en_bout(m, code, sortie, arret, nom: str, interdits: tuple, exiges: tuple) -> None:
    fichier = m.ctx.sortie / "versement" / J.RUN / "calcul-interrompu" / "arret.json"
    cas = SimpleNamespace(nom=nom, interdits=interdits, exiges=exiges)
    _exiger_ligne_cloisonnee(code, sortie, cas, fichier)
    lu = _exiger_fichier_d_arret(fichier, arret, cas)
    assert lu["morceaux"] and verifier(m.ctx.sortie / lu["travail"]["chemin"])
    assert not (m.ctx.sortie / "diag" / J.RUN / "tables-lentilles-bbis.json").exists()          # avant toute écriture de table
    assert not (m.ctx.sortie / "runs" / J.RUN / "manifeste.json").exists()
    assert (m.ctx.travail / la.MARQUE).is_file()                                                 # rien n'est supprimé


def test_bout_en_bout_arret_d_une_direction_lue_message_entier_dans_le_seul_fichier_d_arret(tmp_path, monkeypatch, capsys):
    """Étage (i), calcul entier (Llama miniature, fausse lentille) : l'égalité est déclarée par la garde elle-même (la
    quarantième liste relevée), le reste du chemin est celui du code. `arret.json` porte les deux identifiants de jeton et la
    valeur commune ; la ligne de commande, le nom et le chemin seulement."""
    m = _monde_monte(tmp_path)
    origine, appels = st.premiers_gardes, {"n": 0}

    def garde_qui_voit_une_egalite(valeurs, k):
        g = origine(valeurs, k)
        appels["n"] += 1
        if appels["n"] == 40:
            g |= {"egalite": True, "rangs_a_egalite": (int(g["rangs"][-1]), int(g["rangs"][-2])), "valeur_commune": float(g["valeurs"][-1])}
        return g
    monkeypatch.setattr(st, "premiers_gardes", garde_qui_voit_une_egalite)
    code, sortie, arret = _calcul_par_la_ligne_de_commande(m, monkeypatch, capsys)
    assert isinstance(arret, st.EgaliteDirectionLue) and len(set(arret.identifiants)) == 2
    morceaux = (f"identifiants {arret.identifiants[0]} et {arret.identifiants[1]}", f"valeur commune {arret.valeur!r}")
    _exiger_bout_en_bout(m, code, sortie, arret, "EgaliteDirectionLue",
                         interdits=morceaux + (st.MESSAGE_EGALITE_LUE, repr(arret.valeur), arret.liste, "cellule", "identifiants"),
                         exiges=morceaux + (st.MESSAGE_EGALITE_LUE, arret.liste, f"cellule {arret.contexte['cellule']}"))


def test_bout_en_bout_arret_des_directions_nulles_message_entier_dans_le_seul_fichier_d_arret(tmp_path, monkeypatch, capsys):
    """Étage (ii), calcul entier : les bornes des valeurs p rendues par la garde sont forcées de part et d'autre des seuils
    (p_bas au plancher, p_haut à 1), comme si des directions nulles marquées décidaient du libellé ; le reste du chemin est
    celui du code (`_etiqueter`, `libelle_sous_departage`). `arret.json` porte la borne basse et la borne haute de la valeur
    p ; la ligne de commande, le nom et le chemin seulement."""
    m = _monde_monte(tmp_path)
    bas = 1.0 / (m.reglages.m + 1)
    monkeypatch.setattr(st, "p_bornes", lambda s_min, s_max, valeur: (bas, 1.0))
    code, sortie, arret = _calcul_par_la_ligne_de_commande(m, monkeypatch, capsys)
    assert isinstance(arret, st.EgaliteNulleDecisive) and arret.libelle_bas != arret.libelle_haut
    assert {d["p_bas"] for d in arret.par_nul.values()} == {bas} and {d["p_haut"] for d in arret.par_nul.values()} == {1.0}
    morceaux = (f"p_bas {bas!r}", f"p_haut {1.0!r}")
    _exiger_bout_en_bout(m, code, sortie, arret, "EgaliteNulleDecisive",
                         interdits=morceaux + (st.MESSAGE_EGALITE_NULLE, repr(bas), "p_bas", "p_haut", arret.statistique,
                                               "statistique", "cellule", "libellé"),
                         exiges=morceaux + (st.MESSAGE_EGALITE_NULLE, f"statistique « {arret.statistique} »",
                                            f"cellule {arret.contexte['cellule']}"))


# --- le cas sain de bout en bout rend la même sortie que la version 4 ---------------------------------------------------------------------------
def _course_saine(lanceur, jouets, tmp: Path, capsys) -> SimpleNamespace:
    """Montage puis calcul par la ligne de commande, sur le monde miniature de mêmes graines, horloge figée."""
    m = jouets.monde(tmp)
    m.ctx.maintenant = lambda: 0.0
    lanceur.monter(m.ctx)
    patch = pytest.MonkeyPatch()
    patch.setattr(lanceur, "Contexte", lambda *a, **k: m.ctx)
    try:
        capsys.readouterr()
        code = lanceur.principal(["calcul", "--travail", str(m.ctx.travail), "--sortie", str(m.ctx.sortie), "--run", jouets.RUN,
                                  "--depot", str(m.ctx.racine_depot), "--registre-propre", str(m.registre_propre), "--entrees",
                                  str(m.entrees), "--registre-bbis", str(m.registre_bbis)])
        sortie = capsys.readouterr()
    finally:
        patch.undo()
    rendu = json.loads(sortie.out)
    lire = lambda chemin: json.loads((m.ctx.sortie / chemin).read_text(encoding="utf-8"))          # noqa: E731
    tableaux = {}
    for morceau in rendu["morceaux"]:
        with np.load(m.ctx.sortie / "donnees" / jouets.RUN / morceau["fichier"], allow_pickle=False) as z:
            tableaux |= {nom: z[nom] for nom in z.files}
    return SimpleNamespace(code=code, err=sortie.err, rendu=rendu, tables=lire(rendu["tables"]["chemin"]),
                           manifeste=lire(rendu["manifeste"]["chemin"]), tableaux=tableaux, m=m,
                           montage=lire(f"diag/{jouets.RUN}/montage-lentilles-bbis.json"))


def test_bout_en_bout_sain_meme_sortie_que_la_version_4(tmp_path, capsys):
    """Sans arrêt, `lanceur_v7` rend ce que rend `lanceur_v4` : même sortie standard (clés, lignes proposées, fichiers), mêmes
    tables, mêmes tableaux, mêmes phrases, même manifeste. Seules différences permises, toutes nommées ici : le nom du lanceur
    dans la liste des empreintes du code ; l'heure d'écriture ; et les empreintes qui en découlent (une archive `numpy` porte
    l'heure de son écriture)."""
    assert J.RUN == J4.RUN
    v4, v5 = _course_saine(la4, J4, tmp_path / "v4", capsys), _course_saine(la, J, tmp_path / "v5", capsys)
    assert v4.code == v5.code == 0 and v4.err == v5.err == ""
    # sortie standard : mêmes clés, mêmes chemins ; les empreintes diffèrent pour les seules raisons dites
    assert sorted(v4.rendu) == sorted(v5.rendu)
    for cle in ("empreinte_extrait", "e1_sha256"):
        assert v4.rendu[cle] == v5.rendu[cle]
    assert v4.rendu["tables"]["chemin"] == v5.rendu["tables"]["chemin"] and v4.rendu["manifeste"]["chemin"] == v5.rendu["manifeste"]["chemin"]
    assert [m["fichier"] for m in v4.rendu["morceaux"]] == [m["fichier"] for m in v5.rendu["morceaux"]]
    assert all(set(m) == {"fichier", "sha256"} for m in v5.rendu["morceaux"])
    assert v4.rendu["versement_du_travail"]["chemin"] == v5.rendu["versement_du_travail"]["chemin"]
    assert [l.split(" | ")[0] for l in v4.rendu["lignes_proposees"]] == [l.split(" | ")[0] for l in v5.rendu["lignes_proposees"]]
    assert v4.rendu["lignes_proposees"][0].split(" | ")[2:] == v5.rendu["lignes_proposees"][0].split(" | ")[2:]   # ligne des entrées
    # tableaux : mêmes noms, mêmes valeurs, octet pour octet
    assert sorted(v4.tableaux) == sorted(v5.tableaux) and len(v5.tableaux) > 100
    for nom, a in v4.tableaux.items():
        b = v5.tableaux[nom]
        assert a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes(), nom
    # tables : égales, une fois retirées les empreintes des archives (heure d'écriture)
    def sans_empreintes_des_archives(tables: dict) -> dict:
        return tables | {"fichiers_des_lectures": [{k: v for k, v in f.items() if k != "sha256"} for f in tables["fichiers_des_lectures"]]}
    assert sans_empreintes_des_archives(v4.tables) == sans_empreintes_des_archives(v5.tables)
    assert v5.tables["directions"] and v5.tables["egalites_au_vingtieme_rang"]["directions_lues_a_egalite"] == 0
    assert la4.rendre_phrases(v4.tables) == la.rendre_phrases(v5.tables)
    # manifeste : égal, hors l'heure, le nom du lanceur et l'empreinte des tables
    hors = ("cree_le", "code", "tables_sha256", "rapport_du_montage", "commit", "fiche_code")
    assert {k: v for k, v in v4.manifeste.items() if k not in hors} == {k: v for k, v in v5.manifeste.items() if k not in hors}
    assert set(v4.manifeste["code"]) ^ set(v5.manifeste["code"]) == {"lanceur_v4.py", "lanceur_v7.py"}
    communs = set(v4.manifeste["code"]) & set(v5.manifeste["code"])
    assert len(communs) == 12 and all(v4.manifeste["code"][n] == v5.manifeste["code"][n] for n in communs)
    assert v5.manifeste["code"]["lanceur_v7.py"] == J.sha((PAQUET / "lanceur_v7.py").read_bytes())
    assert v4.manifeste["fiche_code"]["addendum"] == v5.manifeste["fiche_code"]["addendum"]
    # rapport du montage : mêmes gardes, mêmes contrôles de la lentille, des poids et des jetons gardés
    for cle in ("gardes", "jetons_gardes", "lignes_de_sortie_egales", "garde_fonction_lecture", "graines", "texte", "addendum", "poids",
                "petits_fichiers"):
        assert v4.montage[cle] == v5.montage[cle], cle


# --- la version 5 est la version 4 plus ce seul changement -----------------------------------------------------------------------------------
def test_modules_de_la_fiche_du_code_treize_dont_le_lanceur_de_la_version_5():
    assert len(la.MODULES) == len(la4.MODULES) == 13
    assert la.MODULES == tuple("lanceur_v7" if m == "lanceur_v4" else m for m in la4.MODULES) and la.MODULES[-1] == "lanceur_v7"
    assert set(la.empreintes_du_code()) == {f"{m}.py" for m in la.MODULES}


def test_fiche_du_code_sans_l_empreinte_du_lanceur_de_la_version_5_rien_ne_part(tmp_path):
    """La fiche du code doit porter `lanceur_v7.py` : avec la liste de fichiers de la version 4 (cas contraire), rien ne part."""
    _, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    assert la.exiger_fiche_code(tmp_path / "depot", propre)["sha256"]                                  # cas sain
    fichiers_v4 = {f"{la.CHEMIN_PAQUET}/{m}.py": J.sha((PAQUET / f"{m}.py").read_bytes()) for m in la4.MODULES}
    J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers=fichiers_v4)
    assert la4.exiger_fiche_code(tmp_path / "depot", propre)["sha256"]
    with pytest.raises(Refus, match=r"lanceur_v7\.py : empreinte absente de la fiche"):
        la.exiger_fiche_code(tmp_path / "depot", propre)
