"""Essais des corrections de la seconde passe après contre-lecture (`lanceur_seconde_passe_v2`, `nos_lentilles_v2`,
`phrases_v3`) : mandat `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-seconde-passe-lentilles-v2.md`
(`a2132568…`), contre-lecture `…/contre-lectures/contre-lecture-code-seconde-passe-v1.md` (`0c90e0f6…`).

Pour chaque correction, un cas sain et un artefact (R5) ; là où c'est possible, l'artefact est **le code d'avant** joué sur le
même monde (le défaut y est vu, la correction ne l'a plus) :
- B1 : module exécuté hors de la liste de la fiche du code ; arbre du corpus servi en deux pages, par la seconde passe ;
- B2 : cache du tokeniseur ; refus du dépôt à porte (code 401) reproduit par le vrai chargement dans un processus enfant, en
  ligne et sans clé, contre une porte simulée locale ; cause nommée quand l'essai en ligne échoue ;
- N2, N2 bis, N3, N4, N5 ; l'essai dépendant de l'ordre (point 6 du mandat).
Tout sur jouets : aucun modèle réel, aucune lentille réelle, aucune requête hors de la machine (la porte simulée écoute sur
127.0.0.1), aucune clé lue (la seule « clé » est la fausse clé des jouets).

Repris tels quels du fichier d'essais du correctif du tokeniseur de la première passe
(`test_lentilles_sondes_bbis_cache_tokeniseur_v2.py`, importé) : le tokeniseur jouet de cinq jetons et la porte simulée.
"""
from __future__ import annotations

import ast
import copy
import dataclasses
import difflib
import inspect
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v9 as J9  # noqa: E402
import lentilles_sondes_bbis_seconde_passe_jouets_v1 as J1  # noqa: E402
import lentilles_sondes_bbis_seconde_passe_jouets_v2 as J2  # noqa: E402
import lentilles_sondes_bbis_seconde_passe_jouets_v3 as J3  # noqa: E402
import test_lentilles_sondes_bbis_cache_tokeniseur_v2 as TC  # noqa: E402
from controle_ia.lentilles_sondes_bbis import cache_tokeniseur_v2 as ct  # noqa: E402
from controle_ia.lentilles_sondes_bbis import comparaisons_lentilles_v1 as co  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v2 as K2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_seconde_passe_v1 as la1  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_seconde_passe_v2 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v7 as l7  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v9 as l9  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v2 as m2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nos_lentilles_v1 as nl  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nos_lentilles_v2 as n2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import phrases_v2 as p2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import phrases_v3 as p3  # noqa: E402
from controle_ia.lentilles_sondes_bbis import reproduction_v1 as rp  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, FormeMalComprise, Refus  # noqa: E402

porte = TC.porte                                    # la porte simulée locale (fixture), reprise telle quelle
PAQUET = Path(la.__file__).resolve().parent
ESSAIS = Path(__file__).resolve().parent
OUTIL = J9.RACINE / "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-seconde-passe-v2-v1.py"
R, S, PUB, LOG = K2.LENTILLE_NOTRE_R, K2.LENTILLE_NOTRE_S, K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS
H = J1.H
NEUFS = ("corpus_pagine_v1", "cache_tokeniseur_v2", "nos_lentilles_v2", "phrases_v3")
PHRASE_AUCUN_FICHIER = "jeu de données de la tranche zh : aucun fichier de données dans l'arbre : arrêt ; nœud"
LIGNE_SECONDE = "« partiel », seconde course"       # la ligne d'ensemble que portent les fiches des jouets
# Le chargement du tokeniseur tel que le catalogue du voisin le fait (essai d'égalité plus bas) : le catalogue des jouets ne
# charge aucun tokeniseur réel ; pour reproduire le refus du dépôt à porte, l'enfant joue ce chargement-ci.
SCRIPT_REEL = ("import os\n"
               "from transformers import AutoTokenizer\n"
               "tok = AutoTokenizer.from_pretrained(os.environ['NEURON_LENS_MODEL'])\n"
               "assert isinstance(tok.decode([0]), str)\n")


@pytest.fixture(scope="module")
def mp():
    patch = pytest.MonkeyPatch()
    yield patch
    patch.undo()


class _Fin(Arret):
    """Arrêt jouet levé juste après les essais du tokeniseur, pour ne pas jouer la suite du montage (flux de poids)."""


def _finir_apres_les_essais_du_tokeniseur(monkeypatch) -> None:
    def leve(*a, **k):
        raise _Fin("fin de l'essai : les essais du tokeniseur sont passés")
    monkeypatch.setattr(m2, "exiger_plongements_dans_l_index", leve)


def _dossiers(n: int) -> bytes:
    return json.dumps([{"type": "directory", "path": f"dossier-{i:04d}"} for i in range(n)]).encode()


def _paginer_zh(m) -> None:
    """Sert l'arbre du jeu de données de la tranche zh en deux pages : des dossiers seulement, puis le fichier de données."""
    arbre = mo.url_arbre(J9.DEPOT_ZH, "rzh", jeu=True, recursif=True)
    suite = arbre + "&cursor=curseur-2"
    m.transport.fichiers[suite] = m.transport.fichiers[arbre]
    m.transport.fichiers[arbre] = _dossiers(1000)
    if hasattr(m.transport, "suites"):
        m.transport.suites[arbre] = suite


# =============================================================================================================================================
# B1 — tout module exécuté est dans la liste de la fiche du code
# =============================================================================================================================================
def _importes_du_paquet(module: str) -> set:
    """Modules du paquet qu'un module importe, où que soit l'import (en tête ou dans une fonction : un import paresseux est
    exécuté tout de même)."""
    arbre = ast.parse((PAQUET / f"{module}.py").read_text(encoding="utf-8"))
    noms = set()
    for n in ast.walk(arbre):
        if isinstance(n, ast.ImportFrom) and n.level == 1:
            noms |= {n.module.split(".")[0]} if n.module else {a.name for a in n.names}
    return {x for x in noms if (PAQUET / f"{x}.py").is_file()}


def _fermeture(module: str) -> set:
    vus, a_voir = set(), [module]
    while a_voir:
        m = a_voir.pop()
        if m not in vus:
            vus.add(m)
            a_voir += sorted(_importes_du_paquet(m))
    return vus | {"__init__"}


def test_b1_tout_module_du_paquet_que_le_lanceur_v2_execute_est_dans_sa_liste_et_l_ancien_lanceur_en_laissait_un_dehors():
    """Sain : la fermeture des imports du lanceur v2 (imports paresseux compris) tient dans `MODULES`, et `MODULES` ne porte
    rien d'autre. Artefact : la même mesure sur le lanceur v1 trouve exactement le module que la contre-lecture a trouvé."""
    assert _fermeture("lanceur_seconde_passe_v2") == set(la.MODULES)
    assert _fermeture("lanceur_seconde_passe_v1") - set(la1.MODULES) == {"corpus_pagine_v1"}
    assert len(set(la.MODULES)) == len(la.MODULES)


def test_b1_modules_de_la_fiche_du_code_ceux_de_la_v1_plus_les_quatre_modules_neufs():
    assert set(la.MODULES) - set(la1.MODULES) == set(NEUFS) | {"lanceur_seconde_passe_v2"}
    assert set(la1.MODULES) - set(la.MODULES) == {"lanceur_seconde_passe_v1"}
    assert la.MODULES_DIFFERENTS == ("statistiques_v4", "lanceur_seconde_passe_v2")
    assert set(la.empreintes_du_code()) == {f"{m}.py" for m in la.MODULES}
    for m in NEUFS:
        assert la.empreintes_du_code()[f"{m}.py"] == J1.sha((PAQUET / f"{m}.py").read_bytes())


@pytest.fixture(scope="module")
def nu_monde(tmp_path_factory, mp):
    return J3.monde(tmp_path_factory.mktemp("non-monte"), mp)


def _avec_la_fiche(m, fichiers: dict, jouer) -> None:
    """Réécrit la fiche jouet du code avec ces empreintes, accorde la ligne du registre, joue, puis remet tout en place."""
    fiche, texte = m.depot / J3.FICHE_CODE, m.registre_propre.read_text(encoding="utf-8")
    origine = fiche.read_bytes()
    try:
        sha = J3.ecrire_fiche_code(m.depot, fichiers=fichiers)
        ligne = next(l for l in texte.splitlines() if l.startswith(f"| {K2.CLE_CODE_V2} |"))
        m.registre_propre.write_text(texte.replace(ligne, f"| {K2.CLE_CODE_V2} | {H['code_v2']} | {J3.FICHE_CODE} | {sha} |"), encoding="utf-8")
        jouer()
    finally:
        fiche.write_bytes(origine)
        m.registre_propre.write_text(texte, encoding="utf-8")


@pytest.mark.parametrize("module", NEUFS + ("lanceur_seconde_passe_v2",))
def test_b1_fiche_du_code_sans_l_empreinte_d_un_module_neuf_ou_alteree_d_un_octet_rien_ne_part(nu_monde, module):
    m = nu_monde
    assert la.exiger_fiche_code(m.depot, m.registre_propre)["sha256"]                                    # cas sain
    fichiers = {f"{la.CHEMIN_PAQUET}/{x}.py": J1.sha((PAQUET / f"{x}.py").read_bytes()) for x in la.MODULES}
    nom = f"{la.CHEMIN_PAQUET}/{module}.py"
    vraie = fichiers[nom]
    alteree = ("0" if vraie[0] != "0" else "1") + vraie[1:]                                               # un caractère de l'empreinte

    def refus():
        with pytest.raises(Refus, match=rf"{module}\.py : empreinte absente de la fiche CODE-LENTILLES-BBIS-V2 ou différente"):
            la.exiger_fiche_code(m.depot, m.registre_propre)
        ctx = dataclasses.replace(m.ctx, travail=m.tmp / f"travail-{module}", sortie=m.tmp / f"sortie-{module}")
        with pytest.raises(Refus, match="rien de la seconde passe ne part"):
            la.monter(ctx)
        assert not ctx.travail.exists() and not ctx.sortie.exists()
    for artefact in ({k: v for k, v in fichiers.items() if k != nom}, fichiers | {nom: alteree}):
        _avec_la_fiche(m, artefact, refus)
    _avec_la_fiche(m, fichiers, lambda: la.exiger_fiche_code(m.depot, m.registre_propre))                 # sain : les seuls modules de la liste
    assert la.exiger_fiche_code(m.depot, m.registre_propre)["sha256"]


def test_b1_le_lanceur_v2_prend_les_cibles_du_corpus_de_la_lecture_paginee_sans_point_de_branchement():
    source = (PAQUET / "lanceur_seconde_passe_v2.py").read_text(encoding="utf-8")
    code = source[source.index('"""', 3) + 3:]
    assert code.count("cp.cibles_corpus(voisin, transport)") == 1
    assert "cibles_du_corpus" not in code and "mo.cibles_corpus" not in code and "cibles_corpus:" not in code
    assert not hasattr(la.Reglages(), "cibles_corpus") and hasattr(la1.Reglages(), "cibles_corpus")
    assert "from . import corpus_pagine_v1 as cp" in code


# =============================================================================================================================================
# Bout en bout par le lanceur v2 : arbre du corpus en deux pages (B1), cache du tokeniseur (B2), une seule lentille au premier
# palier avec la lecture de la seconde course inscrite (N2), première passe en cours au montage et achevée depuis (N4)
# =============================================================================================================================================
@pytest.fixture(scope="module")
def bout_en_bout(tmp_path_factory, mp):
    m = J3.monde(tmp_path_factory.mktemp("bout-en-bout"), mp, r="p1", s="autre", variante=K2.VARIANTE_COURSE_REJOUEE,
                 seconde_course=K2.SECONDE_COURSE_ENTIERE, plus=("lecture_seconde_course",), premiere_passe="entrees")
    _paginer_zh(m)
    montage = la.monter(m.ctx)
    rapport = json.loads(Path(montage["chemin"]).read_text(encoding="utf-8"))
    appels_du_montage = list(m.transport.appels)
    journaux = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in m.ctx.travail.glob("journal-essai-*.txt")}
    marqueurs = sorted(p.name for p in (ct.base_du_cache(m.ctx.travail / "hf", m.reglages.depot_llama) / ".no_exist"
                                        / m.reglages.revision_llama).iterdir())
    # la première passe, en cours au montage de la seconde, s'achève : sa ligne de tables est inscrite avant le calcul
    J3.ajouter_lignes(m.registre_propre, [(K2.CLE_TABLES_V1, H["tables_v1"], "diag/x/tables-lentilles-bbis.json", "1" * 64)])
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis, None)
    tables = json.loads((m.ctx.sortie / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    return dict(m=m, rapport=rapport, appels=appels_du_montage, journaux=journaux, marqueurs=marqueurs, tables=tables,
                phrases=la.rendre_phrases(tables))


def test_b1_bout_en_bout_la_seconde_passe_suit_les_deux_pages_de_l_arbre_du_corpus(bout_en_bout):
    rapport, appels = bout_en_bout["rapport"], bout_en_bout["appels"]
    corpus = [e for e in rapport["essais_un_octet"] if e["cible"].startswith("jeu de données de la tranche ")]
    assert [e["cible"] for e in corpus] == [f"jeu de données de la tranche {x}" for x in K.TRANCHES_CORPUS]
    assert all(e["tenu"] and not e["avec_cle"] for e in corpus)
    pages = [a for a in appels if a[0] == "page"]
    assert len(pages) == 5 and all(a[2] is False for a in pages)                                         # cinq pages, toutes sans clé
    assert sum("cursor=curseur-2" in a[1] for a in pages) == 1                                           # la seconde page de zh est lue
    premier_flux = next(i for i, a in enumerate(appels) if a[0] == "flux")
    assert max(i for i, a in enumerate(appels) if a[0] == "page") < premier_flux                         # avant tout flux long
    assert rapport["gardes"]["toutes_tenues"] and set(rapport["code"]["empreintes"]) == {f"{x}.py" for x in la.MODULES}


def test_b1_artefact_l_ancien_lanceur_de_la_seconde_passe_sur_le_meme_arbre_en_deux_pages_s_arrete(tmp_path, mp):
    """Le défaut : `lanceur_seconde_passe_v1`, dont les jouets branchaient `montage_v1.cibles_corpus`, ne lit que la première
    page et s'arrête sur « aucun fichier de données » alors que l'arbre en porte un à la seconde page."""
    m = J2.monde(tmp_path, mp)
    _paginer_zh(m)
    with pytest.raises(Arret) as e:
        la1.monter(m.ctx)
    assert str(e.value) == PHRASE_AUCUN_FICHIER
    assert not any(a[0] == "flux" for a in m.transport.appels)


class _SansPage:
    """Réseau simulé qui ne sait pas lire une page avec son lien de suite (il n'a que `octets` et `flux`)."""

    def __init__(self, transport):
        self.octets, self.flux, self.appels = transport.octets, transport.flux, transport.appels


def test_b1_artefact_transport_sans_lecture_de_page_arret_jamais_de_repli_sur_la_premiere_page(tmp_path, mp):
    m = J3.monde(tmp_path, mp)
    ctx = dataclasses.replace(m.ctx, transport=_SansPage(m.transport))
    with pytest.raises(Arret, match="transport sans lecture de page"):
        la.monter(ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_b1_artefact_arbre_du_corpus_sans_fichier_sur_ses_deux_pages_arret_avant_tout_flux(tmp_path, mp):
    m = J3.monde(tmp_path, mp)
    _paginer_zh(m)
    arbre = mo.url_arbre(J9.DEPOT_ZH, "rzh", jeu=True, recursif=True)
    m.transport.fichiers[arbre + "&cursor=curseur-2"] = _dossiers(3)
    with pytest.raises(Arret) as e:
        la.monter(m.ctx)
    assert str(e.value) == PHRASE_AUCUN_FICHIER
    assert sum(a[0] == "page" and "datasets/" + J9.DEPOT_ZH in a[1] for a in m.transport.appels) == 2    # les deux pages ont été lues
    assert not any(a[0] == "flux" for a in m.transport.appels)


# =============================================================================================================================================
# B2 — cache du tokeniseur, essai en ligne et sans clé, cause nommée
# =============================================================================================================================================
def test_b2_bout_en_bout_cache_marque_deux_essais_du_tokeniseur_avant_tout_flux_et_deux_champs_neufs(bout_en_bout):
    rapport, appels, r = bout_en_bout["rapport"], bout_en_bout["appels"], bout_en_bout["m"].reglages
    poses = sorted(n for n in r.petits if n.endswith(".json") and n != K.INDEX_LLAMA)
    cache = rapport["cache_du_tokeniseur"]
    assert sorted(cache["fichiers_poses"]) == poses == ["config.json", "tokenizer.json"]
    assert cache["marqueurs_d_absence"] == sorted(ct.ABSENTS_CONNUS) == bout_en_bout["marqueurs"] and cache["revision"] == r.revision_llama
    assert "original" in cache["racine_du_depot"] and not set(ct.ABSENTS_CONNUS) & set(cache["racine_du_depot"])
    assert rapport["essai_du_tokeniseur_hors_ligne"] == {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}
    assert rapport["essai_du_tokeniseur_en_ligne_sans_cle"] == {"tenu": True, "journal": la.JOURNAL_ESSAI_EN_LIGNE}
    assert set(bout_en_bout["journaux"]) == {"journal-essai-tokeniseur.txt", la.JOURNAL_ESSAI_EN_LIGNE}
    for garde in ("tokeniseur lu du cache hors ligne",
                  "fichiers absents du dépôt du modèle vérifiés sur son arbre et marqués absents dans le cache",
                  "tokeniseur lu par le voisin, en ligne et sans clé"):
        assert rapport["gardes"]["liste"].count(garde) == 1
    assert [g for g in rapport["gardes"]["liste"] if g not in (
        "fichiers absents du dépôt du modèle vérifiés sur son arbre et marqués absents dans le cache",
        "tokeniseur lu par le voisin, en ligne et sans clé")] == _gardes_de_la_v1()
    arbre = mo.url_arbre(r.depot_llama, r.revision_llama)
    lectures = [i for i, a in enumerate(appels) if a[1] == arbre]
    premier_flux = next(i for i, a in enumerate(appels) if a[0] == "flux")
    assert len(lectures) == 2 and lectures[0] < premier_flux and all(appels[i][2] for i in lectures)      # avec la clé, avant tout flux
    m = bout_en_bout["m"]
    for p in m.ctx.sortie.rglob("*"):
        if p.is_file() and not p.is_symlink():
            assert J9.FAUSSE_CLE.encode() not in p.read_bytes(), p


def _gardes_de_la_v1() -> list:
    """La liste des gardes que le rapport du montage de `lanceur_seconde_passe_v1` porte, lue dans sa source."""
    source = (PAQUET / "lanceur_seconde_passe_v1.py").read_text(encoding="utf-8")
    marque = 'rapport["gardes"] = {"toutes_tenues": True, "liste": '
    bloc = source[source.index(marque) + len(marque):]
    return ast.literal_eval(bloc[:bloc.index("]}") + 1])


def test_b2_les_deux_essais_du_tokeniseur_un_hors_ligne_puis_un_en_ligne_tous_deux_sans_cle(tmp_path, mp, monkeypatch):
    m = J3.monde(tmp_path, mp)
    trace = tmp_path / "trace.txt"
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", l7.SCRIPT_TOKENISEUR + (
        "import os\n"
        f"open({str(trace)!r}, 'a').write(repr((os.environ.get('HF_HUB_OFFLINE'), {K.NOM_CLE!r} in os.environ,"
        " os.environ.get('HF_HUB_DISABLE_IMPLICIT_TOKEN'), os.environ.get('NEURON_LENS_MODEL'))) + '\\n')\n"))
    _finir_apres_les_essais_du_tokeniseur(monkeypatch)
    with pytest.raises(_Fin):
        la.monter(m.ctx)
    assert trace.read_text().splitlines() == [repr(("1", False, "1", K.DEPOT_LLAMA)), repr((None, False, "1", K.DEPOT_LLAMA))]
    assert not any(a[0] == "flux" for a in m.transport.appels)                                            # les deux essais précèdent tout flux


def test_b2_artefact_un_fichier_a_marquer_existe_a_la_racine_arret_avant_tout_flux(tmp_path, mp):
    m = J3.monde(tmp_path, mp)
    arbre = mo.url_arbre(m.reglages.depot_llama, m.reglages.revision_llama)
    m.transport.fichiers[arbre] = json.dumps(json.loads(m.transport.fichiers[arbre])
                                             + [{"type": "file", "path": "tokenizer.model", "oid": "0" * 40, "size": 9}]).encode()
    with pytest.raises(Arret, match=r"\['tokenizer.model'\] existe\(nt\) à la racine du dépôt du modèle") as e:
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels) and J9.FAUSSE_CLE not in str(e.value)
    assert not ct.base_du_cache(m.ctx.travail / "hf", m.reglages.depot_llama).exists()
    assert not (m.ctx.travail / "journal-essai-tokeniseur.txt").exists()


def test_b2_artefact_arbre_du_depot_du_modele_sans_les_petits_fichiers_poses_arret(tmp_path, mp):
    """Les jouets de la seconde passe listent les petits fichiers posés par l'arbre du dépôt du modèle ; un arbre qui ne liste
    que les poids (celui des jouets d'avant) est arrêté par le témoin de la lecture de l'arbre."""
    m = J3.monde(tmp_path, mp)
    arbre = mo.url_arbre(m.reglages.depot_llama, m.reglages.revision_llama)
    chemins = {e["path"] for e in json.loads(m.transport.fichiers[arbre])}
    assert {"config.json", "tokenizer.json", K.INDEX_LLAMA} <= chemins                                    # sain : ils y sont
    m.transport.fichiers[arbre] = json.dumps([e for e in json.loads(m.transport.fichiers[arbre]) if "lfs" in e]).encode()
    with pytest.raises(Arret, match="posé\\(s\\) dans le cache mais absent\\(s\\) de l'arbre"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_b2_artefact_essai_en_ligne_en_echec_arret_avant_tout_flux_et_le_cache_relu_est_dit_inchange(tmp_path, mp, monkeypatch):
    """Le chargement réussit hors ligne et échoue en ligne : arrêt avant tout flux long ; la relecture du cache ne trouve
    rien, et l'arrêt le dit (la cause est alors dans le journal)."""
    m = J3.monde(tmp_path, mp)
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", l7.SCRIPT_TOKENISEUR + (
        f"import os\nassert {K.NOM_CLE!r} not in os.environ\n"
        "if os.environ.get('HF_HUB_OFFLINE') != '1':\n    raise SystemExit('refus du dépôt à porte (jouet)')\n"))
    with pytest.raises(Arret, match="ne lit pas le tokeniseur en ligne et sans clé") as e:
        la.monter(m.ctx)
    message = str(e.value)
    assert message == (f"le code voisin ne lit pas le tokeniseur en ligne et sans clé ({la.JOURNAL_ESSAI_EN_LIGNE}) ; "
                       f"{la.CAUSE_CACHE_INCHANGE} : arrêt avant tout flux long ; nœud")
    assert "cause relue dans le cache" not in message and J9.FAUSSE_CLE not in message
    assert not any(a[0] == "flux" for a in m.transport.appels)
    assert (m.ctx.travail / "journal-essai-tokeniseur.txt").read_text() == ""                              # l'essai hors ligne a tenu
    journal = (m.ctx.travail / la.JOURNAL_ESSAI_EN_LIGNE).read_text()
    assert "refus du dépôt à porte (jouet)" in journal and "AssertionError" not in journal
    assert "refus du dépôt à porte (jouet)" not in message                                                 # le journal n'entre pas dans le message


def test_b2_artefact_la_branche_du_depot_a_bouge_l_essai_en_ligne_echoue_et_l_arret_nomme_la_cause(tmp_path, mp, monkeypatch):
    """Correction non bloquante 1 de la contre-lecture du correctif du tokeniseur. La branche principale du dépôt a bougé :
    la bibliothèque la réécrit dans le cache, ne lit plus les fichiers posés et échoue (jouet : le script fait les deux).
    L'arrêt de l'essai en ligne porte la cause, relue dans le cache."""
    m = J3.monde(tmp_path, mp)
    ref = ct.base_du_cache(m.ctx.travail / "hf", m.reglages.depot_llama) / "refs" / "main"
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", l7.SCRIPT_TOKENISEUR + (
        f"import os\nif os.environ.get('HF_HUB_OFFLINE') != '1':\n    open({str(ref)!r}, 'w').write({TC.AUTRE_REV!r})\n"
        "    raise SystemExit('refus du dépôt à porte (jouet)')\n"))
    with pytest.raises(Arret, match="ne lit pas le tokeniseur en ligne et sans clé") as e:
        la.monter(m.ctx)
    message = str(e.value)
    assert "cause relue dans le cache : « cache du tokeniseur : la branche principale n'y désigne pas la révision du texte" in message
    assert la.CAUSE_CACHE_INCHANGE not in message and message.endswith("arrêt avant tout flux long ; nœud")
    assert TC.AUTRE_REV not in message and J9.FAUSSE_CLE not in message
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_b2_artefact_l_essai_en_ligne_reussit_mais_a_reecrit_la_branche_du_cache_la_relecture_arrete(tmp_path, mp, monkeypatch):
    """La relecture du cache qui suit un essai en ligne réussi reste jouée (comme dans `lanceur_v9`)."""
    m = J3.monde(tmp_path, mp)
    ref = ct.base_du_cache(m.ctx.travail / "hf", m.reglages.depot_llama) / "refs" / "main"
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", l7.SCRIPT_TOKENISEUR + (
        f"import os\nif os.environ.get('HF_HUB_OFFLINE') != '1':\n    open({str(ref)!r}, 'w').write({TC.AUTRE_REV!r})\n"))
    with pytest.raises(Arret) as e:
        la.monter(m.ctx)
    assert str(e.value).startswith("cache du tokeniseur : la branche principale n'y désigne pas la révision du texte")
    assert not any(a[0] == "flux" for a in m.transport.appels)


# --- le refus du dépôt à porte (code 401), par le vrai chargement, dans la seconde passe ------------------------------------------------------
def test_b2_le_chargement_joue_par_ces_essais_est_celui_de_la_copie_versee_du_catalogue_du_voisin():
    catalogue = TC.COPIE_CATALOGUE.read_text(encoding="utf-8")
    assert TC.TOKENISEUR_DU_VOISIN in catalogue and 'MODEL = os.environ.get("NEURON_LENS_MODEL", "Qwen/Qwen3-8B")\n' in catalogue
    assert "    return AutoTokenizer.from_pretrained(model)\n" in TC.TOKENISEUR_DU_VOISIN
    assert "tok = AutoTokenizer.from_pretrained(os.environ['NEURON_LENS_MODEL'])\n" in SCRIPT_REEL
    assert l7.SCRIPT_TOKENISEUR == l9.SCRIPT_TOKENISEUR and "catalog.tokenizer(catalog.MODEL)" in l7.SCRIPT_TOKENISEUR


def _env(port: int | None) -> dict:
    """Environnement du lanceur pour ces essais : celui de la machine sans mandataire, sans variable de la plateforme de
    modèles ni nom de clé, plus la fausse clé des jouets ; l'hôte des téléchargements des enfants est la porte simulée."""
    env = {k: v for k, v in os.environ.items()
           if not k.lower().endswith("_proxy") and not k.startswith("HF_") and "TOKEN" not in k.upper()}
    return env | {K.NOM_CLE: J9.FAUSSE_CLE, "NO_PROXY": "127.0.0.1", "no_proxy": "127.0.0.1",
                  "HF_ENDPOINT": f"http://127.0.0.1:{9 if port is None else port}"}


def _avec_un_vrai_tokeniseur(m, port: int | None):
    """Rend le contexte du monde où les petits fichiers du tokeniseur sont ceux d'un vrai tokeniseur de cinq jetons (mêmes
    noms que ceux du dépôt du modèle), servis par le réseau simulé et listés par l'arbre du dépôt."""
    r = m.reglages
    petits = {K.INDEX_LLAMA: r.petits[K.INDEX_LLAMA]}
    for nom, contenu in TC.FICHIERS.items():
        url = mo.url_fichier(r.depot_llama, r.revision_llama, nom)
        m.transport.fichiers[url] = contenu
        m.transport.a_porte.add(url)
        petits[nom] = (len(contenu), mo.identifiant_git(contenu))
    arbre = mo.url_arbre(r.depot_llama, r.revision_llama)
    entrees = [e for e in json.loads(m.transport.fichiers[arbre]) if e["path"] not in TC.FICHIERS]
    entrees += [{"type": "file", "path": n, "oid": mo.identifiant_git(c), "size": len(c)} for n, c in TC.FICHIERS.items()]
    m.transport.fichiers[arbre] = json.dumps(entrees).encode()
    reglages = dataclasses.replace(r, petits=petits, sha256_tokeniseur=J1.sha(TC.FICHIERS["tokenizer.json"]))
    return dataclasses.replace(m.ctx, reglages=reglages, env=_env(port))


def _charger_en_ligne(hf_home: Path, port: int, tmp: Path) -> tuple[bool, str]:
    """Le chargement du script du corpus, dans l'environnement que le montage donne à ses enfants : en ligne, sans clé."""
    voisin = tmp / "voisin-vide"
    voisin.mkdir()
    enfant = mo.environnement_enfant(voisin, hf_home, False, _env(port))
    assert K.NOM_CLE not in enfant and "HF_HUB_OFFLINE" not in enfant
    journal = tmp / "journal-chargement-en-ligne.txt"
    try:
        mo.jouer_script([sys.executable, "-c", SCRIPT_REEL], voisin, enfant, journal)
        return True, journal.read_text(encoding="utf-8", errors="replace")
    except Arret:
        return False, journal.read_text(encoding="utf-8", errors="replace")


def test_b2_artefact_l_ancien_lanceur_de_la_seconde_passe_pose_un_cache_que_le_chargement_en_ligne_refuse_par_401(tmp_path, mp,
                                                                                                             monkeypatch, porte):
    """Le défaut hérité, reproduit : `lanceur_seconde_passe_v1` pose le cache par `montage_v1.poser_cache_tokeniseur` et ne
    l'essaie que hors ligne (l'essai tient, par le vrai chargement) ; le même chargement, en ligne et sans clé, demande
    `tokenizer.model` à l'hôte et s'arrête sur le refus du dépôt à porte (code 401)."""
    port, appels = porte()
    m = J2.monde(tmp_path, mp)
    ctx = _avec_un_vrai_tokeniseur(m, port)
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", SCRIPT_REEL)
    _finir_apres_les_essais_du_tokeniseur(monkeypatch)
    with pytest.raises(_Fin):                                                                              # l'essai hors ligne a tenu
        la1.monter(ctx)
    assert appels == []                                                                                    # hors ligne : rien n'est demandé
    hf_home = ctx.travail / "hf"
    assert not (ct.base_du_cache(hf_home, ctx.reglages.depot_llama) / ".no_exist").exists()
    assert not (ctx.travail / la.JOURNAL_ESSAI_EN_LIGNE).exists()                                          # aucun essai en ligne
    reussi, journal = _charger_en_ligne(hf_home, port, tmp_path)
    assert not reussi and "gated repo" in journal and f"/resolve/{TC.REV}/tokenizer.model" in journal and "401" in journal
    assert TC._fichiers_demandes(appels) == [f"{TC.REV}/tokenizer.model"]
    assert appels and not any(avec_cle for _, _, avec_cle in appels) and J9.FAUSSE_CLE not in journal


def test_b2_sain_le_lanceur_v2_pose_un_cache_que_le_vrai_chargement_lit_en_ligne_et_sans_cle_sans_demander_un_fichier(
        tmp_path, mp, monkeypatch, porte):
    port, appels = porte()
    m = J3.monde(tmp_path, mp)
    ctx = _avec_un_vrai_tokeniseur(m, port)
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", SCRIPT_REEL)
    _finir_apres_les_essais_du_tokeniseur(monkeypatch)
    with pytest.raises(_Fin):                                                                              # les deux essais ont tenu
        la.monter(ctx)
    assert (ctx.travail / "journal-essai-tokeniseur.txt").is_file() and (ctx.travail / la.JOURNAL_ESSAI_EN_LIGNE).is_file()
    assert TC._fichiers_demandes(appels) == []                                                             # aucun fichier demandé à l'hôte
    assert appels and not any(avec_cle for _, _, avec_cle in appels)                                       # l'interface seule, jamais la clé
    attendus = {n: ctx.reglages.petits[n] for n in TC.FICHIERS}
    releve = ct.exiger_cache(ctx.travail / "hf", attendus, ctx.reglages.depot_llama, ctx.reglages.revision_llama)
    assert releve["marqueurs_d_absence"] == sorted(ct.ABSENTS_CONNUS) and sorted(releve["fichiers_poses"]) == sorted(TC.FICHIERS)
    assert not any(a[0] == "flux" for a in m.transport.appels)
    reussi, _ = _charger_en_ligne(ctx.travail / "hf", port, tmp_path)                                      # et le script du corpus le lira
    assert reussi and TC._fichiers_demandes(appels) == []


def test_b2_artefact_le_refus_401_arrete_le_lanceur_v2_avant_tout_flux_quand_le_cache_est_pose_a_l_ancienne(tmp_path, mp, monkeypatch,
                                                                                                     porte):
    """Le refus du dépôt à porte reproduit **dans le montage de la seconde passe v2** : si le cache y était posé comme avant
    (sans marqueur d'absence), l'essai en ligne le verrait avant tout flux long, et l'arrêt nommerait ce que la relecture du
    cache trouve."""
    port, appels = porte()
    m = J3.monde(tmp_path, mp)
    ctx = _avec_un_vrai_tokeniseur(m, port)
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", SCRIPT_REEL)

    def pose_a_l_ancienne(transport, cle, hf_home, fichiers, attendus, depot, revision):
        mo.poser_cache_tokeniseur(hf_home, fichiers, depot, revision)
        return {}
    monkeypatch.setattr(ct, "poser_cache_tokeniseur", pose_a_l_ancienne)
    with pytest.raises(Arret, match="ne lit pas le tokeniseur en ligne et sans clé") as e:
        la.monter(ctx)
    journal = (ctx.travail / la.JOURNAL_ESSAI_EN_LIGNE).read_text(encoding="utf-8", errors="replace")
    assert "gated repo" in journal and f"/resolve/{TC.REV}/tokenizer.model" in journal and "401" in journal
    assert TC._fichiers_demandes(appels) == [f"{TC.REV}/tokenizer.model"] and not any(avec_cle for _, _, avec_cle in appels)
    assert "cause relue dans le cache : « cache du tokeniseur : les marqueurs d'absence ne sont pas exactement ceux attendus" in str(e.value)
    assert (ctx.travail / "journal-essai-tokeniseur.txt").read_text() == ""                                # hors ligne : tenu
    assert not any(a[0] == "flux" for a in m.transport.appels) and J9.FAUSSE_CLE not in str(e.value) + journal


def test_b2_artefact_la_branche_du_depot_a_bouge_par_le_vrai_chargement_l_arret_du_lanceur_v2_nomme_la_cause(tmp_path, mp, monkeypatch,
                                                                                                        porte):
    """L'interface du dépôt (porte simulée) désigne un autre commit que la révision épinglée : le vrai chargement réécrit la
    branche dans le cache, demande ses fichiers à l'autre commit et reçoit le refus 401 ; l'arrêt nomme la cause."""
    port, appels = porte(TC.AUTRE_REV)
    m = J3.monde(tmp_path, mp)
    ctx = _avec_un_vrai_tokeniseur(m, port)
    monkeypatch.setattr(l7, "SCRIPT_TOKENISEUR", SCRIPT_REEL)
    with pytest.raises(Arret, match="ne lit pas le tokeniseur en ligne et sans clé") as e:
        la.monter(ctx)
    demandes = TC._fichiers_demandes(appels)
    assert demandes and all(f.startswith(TC.AUTRE_REV + "/") for f in demandes)
    assert "cause relue dans le cache : « cache du tokeniseur : la branche principale n'y désigne pas la révision du texte" in str(e.value)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_b2_la_fonction_de_l_essai_en_ligne_est_celle_du_lanceur_v9_plus_la_relecture_a_l_echec():
    """Recopie déclarée : les lignes de `lanceur_v9.essayer_tokeniseur_en_ligne` sont toutes dans celle du lanceur v2, à la
    signature, au script (celui de `lanceur_v7`, égal) et au message près ; le seul enfant en ligne du lanceur est celui-ci."""
    v9 = inspect.getsource(l9.essayer_tokeniseur_en_ligne)
    v2 = inspect.getsource(la.essayer_tokeniseur_en_ligne)
    assert "mo.jouer_script([ctx.python, \"-c\", SCRIPT_TOKENISEUR], voisin, mo.environnement_enfant(voisin, hf_home, False, ctx.env)," in v9
    assert "mo.jouer_script([ctx.python, \"-c\", l7.SCRIPT_TOKENISEUR], voisin, mo.environnement_enfant(voisin, hf_home, False, ctx.env)," in v2
    assert "ctx.travail / JOURNAL_ESSAI_EN_LIGNE)" in v9 and "ctx.travail / JOURNAL_ESSAI_EN_LIGNE)" in v2
    assert la.JOURNAL_ESSAI_EN_LIGNE == l9.JOURNAL_ESSAI_EN_LIGNE and "ct.exiger_cache(" in v2 and "ct.exiger_cache(" not in v9
    source = (PAQUET / "lanceur_seconde_passe_v2.py").read_text(encoding="utf-8")
    assert source.count("mo.environnement_enfant(voisin, hf_home, False, ctx.env)") == 1
    assert "mo.poser_cache_tokeniseur" not in source and source.count("ct.poser_cache_tokeniseur(") == 1


# =============================================================================================================================================
# N5 — une seule ligne « Lentille nommée : … » dans la pièce du nœud
# =============================================================================================================================================
def _palier_2(lettre="R", **plus):
    return J1.lentille(lettre, verdict=K2.PALIER_2, **plus)


def _condition(module, racine: Path, fiche: dict, plus: tuple = ()) -> dict:
    registre = J1.monde(racine, fiche, plus=plus)
    etat = nl.exiger_registre_v2(registre)
    return module.condition_de_lecture(nl.lire_fiche(racine, etat), etat, racine)


def _piece_du_noeud(racine: Path, texte: str, heure: str | None = None) -> tuple:
    chemin = "docs/mot-lazar-noeud-jouet.md"
    return (K2.CLE_NOEUD_AJUSTEMENT_SEUL, heure or H["noeud"], chemin, J1.ecrire(racine, chemin, texte))


def _tables(conditions: dict) -> dict:
    return {l: conditions[l].table() for l in K2.NOS_LENTILLES} | {"course": conditions["course"]}


@pytest.mark.parametrize("nommees", ["R", "S", "R et S"])
def test_n5_sain_une_seule_ligne_qui_nomme_la_condition_est_celle_de_nos_lentilles_v1(tmp_path, nommees):
    f = J1.fiche(r=_palier_2(), s=_palier_2("S"))
    neuve = _condition(n2, tmp_path / "a", f, ("avertissement", J1.ligne_du_noeud(tmp_path / "a", nommees)))
    ancienne = _condition(nl, tmp_path / "b", f, ("avertissement", J1.ligne_du_noeud(tmp_path / "b", nommees)))
    assert _tables(neuve) == _tables(ancienne)
    assert {l for l in K2.NOS_LENTILLES if neuve[l].lue} == set(nommees.replace(" et ", " ").split())


def test_n5_artefact_une_citation_de_la_forme_ailleurs_dans_la_piece_arret_la_ou_l_ancien_code_ouvrait_la_lecture(tmp_path):
    f = J1.fiche(r=_palier_2(), s=_palier_2("S"))
    texte = ("# Mot de Lazar (jouet)\n\n- Lentille nommée : R\n\nRappel de la forme attendue, pour une autre pièce :\n\n"
             "Lentille nommée : S\n")
    ancienne = _condition(nl, tmp_path / "a", f, ("avertissement", _piece_du_noeud(tmp_path / "a", texte)))
    assert ancienne["R"].lue and ancienne["S"].lue                         # le défaut : la citation ouvrait la lecture de notre S
    with pytest.raises(FormeMalComprise, match="2 lignes de la forme « Lentille nommée : … » ; une seule est attendue") as e:
        _condition(n2, tmp_path / "b", f, ("avertissement", _piece_du_noeud(tmp_path / "b", texte)))
    assert "docs/mot-lazar-noeud-jouet.md" in str(e.value) and "la forme est mal comprise" in str(e.value)
    assert n2.lignes_qui_nomment(texte) == ["R", "S"]
    meme = "- Lentille nommée : R\n- Lentille nommée : R\n"                # la même ligne deux fois : deux lignes tout de même
    with pytest.raises(FormeMalComprise, match="une seule est attendue"):
        _condition(n2, tmp_path / "c", f, ("avertissement", _piece_du_noeud(tmp_path / "c", meme)))
    # la pièce est jugée aussi quand la lentille consultée en sort non lue (notre S au deuxième palier, la pièce ne nomme que R)
    seule = J1.fiche(s=_palier_2("S"))
    assert not _condition(nl, tmp_path / "d", seule, ("avertissement", _piece_du_noeud(tmp_path / "d", meme)))["S"].lue
    with pytest.raises(FormeMalComprise, match="une seule est attendue"):
        _condition(n2, tmp_path / "e", seule, ("avertissement", _piece_du_noeud(tmp_path / "e", meme)))


def test_n5_une_piece_sans_ligne_de_la_forme_ne_nomme_personne_la_lentille_reste_non_lue_sans_arret(tmp_path):
    f = J1.fiche(r=_palier_2(), s=_palier_2("S"))
    c = _condition(n2, tmp_path, f, ("avertissement", _piece_du_noeud(tmp_path, "go\n\nla lentille nommée : R, dans une phrase\n")))
    assert not c["R"].lue and not c["S"].lue
    assert c["R"].motif == "Non lue : notre lentille R au deuxième palier, sans mesure propre ; aucune lecture sans nœud de Lazar"


def test_n5_la_piece_n_est_jugee_que_si_la_condition_l_a_consultee_et_seulement_pour_les_lignes_retenues(tmp_path):
    deux = "- Lentille nommée : R\n- Lentille nommée : S\n"
    # premier palier : la règle du nœud N12 n'est pas atteinte, la pièce n'est pas lue (comme avant), aucun arrêt
    c = _condition(n2, tmp_path / "a", J1.fiche(), ("avertissement", _piece_du_noeud(tmp_path / "a", deux)))
    assert c["R"].lue and c["S"].lue and not n2.a_consulte_la_piece_du_noeud(c)
    # ligne du nœud antérieure à l'avertissement : non retenue par `nos_lentilles_v1`, donc non jugée ; la lentille reste non lue
    f = J1.fiche(r=_palier_2())
    anterieure = _piece_du_noeud(tmp_path / "b", deux, heure="2026-11-22T09:30:00Z")
    c = _condition(n2, tmp_path / "b", f, (anterieure, "avertissement"))
    assert not c["R"].lue and n2.a_consulte_la_piece_du_noeud(c)
    etat = nl.exiger_registre_v2(tmp_path / "b" / J1.REGISTRE)
    assert n2.exiger_une_seule_ligne_qui_nomme(tmp_path / "b", etat) == {}
    # deux lignes du registre, chacune d'une pièce d'une seule ligne : réunies comme avant
    un = (K2.CLE_NOEUD_AJUSTEMENT_SEUL, H["noeud"], "docs/mot-r.md", J1.ecrire(tmp_path / "c", "docs/mot-r.md", "Lentille nommée : R\n"))
    autre = (K2.CLE_NOEUD_AJUSTEMENT_SEUL, H["entrees_v1"], "docs/mot-s.md", J1.ecrire(tmp_path / "c", "docs/mot-s.md", "Lentille nommée : S\n"))
    c = _condition(n2, tmp_path / "c", J1.fiche(r=_palier_2(), s=_palier_2("S")), ("avertissement", un, autre))
    assert c["R"].lue and c["S"].lue
    etat = nl.exiger_registre_v2(tmp_path / "c" / J1.REGISTRE)
    assert n2.exiger_une_seule_ligne_qui_nomme(tmp_path / "c", etat) == {"docs/mot-r.md": "R", "docs/mot-s.md": "S"}


def test_n5_le_lanceur_v2_s_arrete_sur_une_piece_a_deux_lignes_le_lanceur_v1_la_lisait(tmp_path, mp):
    texte = "- Lentille nommée : R\n\n> exemple : Lentille nommée : S\n\nLentille nommée : S\n"
    m = J3.monde(tmp_path, mp, r="p2", s="p2", plus=("avertissement",))
    J3.ajouter_lignes(m.registre_propre, [_piece_du_noeud(m.depot, texte)])
    conditions = la1._lecture(m.ctx, m.registre_propre)[3]
    assert conditions["R"].lue and conditions["S"].lue                     # le lanceur v1 : les deux lentilles lues
    with pytest.raises(FormeMalComprise, match="une seule est attendue"):
        la._lecture(m.ctx, m.registre_propre)
    with pytest.raises(Arret, match="une seule est attendue"):
        la.monter(m.ctx)
    assert not m.ctx.travail.exists()                                      # avant toute requête, avant tout dossier


# =============================================================================================================================================
# N2 et N2 bis — ligne d'ensemble de la lecture de la seconde course au premier palier
# =============================================================================================================================================
def _conditions(tmp_path, r, s, plus=("avertissement", "lecture_seconde_course"), variante=K2.VARIANTE_COURSE_REJOUEE,
                seconde=K2.SECONDE_COURSE_ENTIERE, ligne=LIGNE_SECONDE):
    fiche = J1.fiche(r=r, s=s, variante=variante, seconde_course=seconde,
                     lecture_seconde_course={"chemin": "docs/l2.md", "sha256": "8" * 64, "ligne_d_ensemble": ligne})
    registre = J1.monde(tmp_path, fiche, plus=plus)
    etat = nl.exiger_registre_v2(registre)
    fiche = nl.lire_fiche(tmp_path, etat)
    return n2.condition_de_lecture(fiche, etat, tmp_path), fiche, etat


def _lentille(lettre, sorte):
    return J1.lentille(lettre, verdict={"p1": K2.PALIER_1, "p2": K2.PALIER_2, "autre": K2.DIFFERENTE}[sorte])


SUITE = p3.SUITE_SECONDE_COURSE.format(ligne=LIGNE_SECONDE)


@pytest.mark.parametrize("lue, autre", [("R", "S"), ("S", "R")])
def test_n2_une_seule_lentille_au_premier_palier_la_ligne_de_la_seconde_course_est_recopiee_a_cote_de_celle_du_verdict(tmp_path, lue, autre):
    sortes = {lue: "p1", autre: "autre"}
    conditions, fiche, etat = _conditions(tmp_path, _lentille("R", sortes["R"]), _lentille("S", sortes["S"]))
    ligne = la._ligne_de_la_seconde_course(fiche, conditions["course"], etat)
    assert ligne == LIGNE_SECONDE
    neuves = p3.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"], ligne)
    anciennes = p2.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])
    assert len(neuves) == len(anciennes) == 1 and "seconde course" not in anciennes[0]["texte"]          # le défaut : rien n'était recopié
    texte = neuves[0]["texte"]
    assert texte == anciennes[0]["texte"].replace(" Réserves qui portent", SUITE + " Réserves qui portent")   # aucun autre mot ne change
    assert texte.index("la décrivent.") < texte.index("Ligne d'ensemble de la lecture de la seconde course") < texte.index("Réserves qui portent")
    assert "désaccord entre les deux mesures de la tranche, nœud de Lazar" in texte
    assert {k: v for k, v in neuves[0].items() if k != "texte"} == {k: v for k, v in anciennes[0].items() if k != "texte"}


def test_n2_bis_nos_deux_lentilles_au_premier_palier_la_ligne_n_est_recopiee_que_si_la_lecture_est_inscrite(tmp_path):
    # sain : lecture inscrite, seconde course menée en entier — le texte est celui d'avant, à l'octet près
    conditions, fiche, etat = _conditions(tmp_path / "a", _lentille("R", "p1"), _lentille("S", "p1"))
    ligne = la._ligne_de_la_seconde_course(fiche, conditions["course"], etat)
    assert ligne == LIGNE_SECONDE
    assert p3.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"], ligne) == p2.lignes_du_verdict_d_ensemble(
        conditions, fiche, conditions["course"])
    # artefact : la fiche porte la ligne, la lecture n'est pas inscrite au registre propre
    conditions, fiche, etat = _conditions(tmp_path / "b", _lentille("R", "p1"), _lentille("S", "p1"), plus=("avertissement",))
    assert not etat.presentes(K2.CLE_LECTURE_SECONDE_COURSE) and fiche["lecture_seconde_course"]["ligne_d_ensemble"] == LIGNE_SECONDE
    ligne = la._ligne_de_la_seconde_course(fiche, conditions["course"], etat)
    assert ligne is None
    ancien = p2.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])[0]["texte"]
    neuf = p3.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"], ligne)[0]["texte"]
    assert "seconde course" in ancien and "seconde course" not in neuf                                   # le défaut, et sa correction
    assert neuf == ancien.replace(SUITE, "") and "(R-a) à (R-e)" in neuf


def test_n2_deuxieme_palier_inchange_et_cas_d_une_lentille_a_chaque_palier(tmp_path):
    conditions, fiche, etat = _conditions(tmp_path / "a", _lentille("R", "p2"), _lentille("S", "p2"))
    ligne = la._ligne_de_la_seconde_course(fiche, conditions["course"], etat)
    assert p3.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"], ligne) == p2.lignes_du_verdict_d_ensemble(
        conditions, fiche, conditions["course"])
    conditions, fiche, etat = _conditions(tmp_path / "b", _lentille("R", "p1"), _lentille("S", "p2"))
    ligne = la._ligne_de_la_seconde_course(fiche, conditions["course"], etat)
    neuves = p3.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"], ligne)
    anciennes = p2.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])
    assert [l["palier"] for l in neuves] == [1, 2] and neuves[1] == anciennes[1]                         # la ligne du deuxième palier, telle quelle
    assert SUITE in neuves[0]["texte"] and SUITE not in anciennes[0]["texte"]
    assert p3.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"], None) == anciennes   # sans ligne donnée : comme avant


def test_n2_la_tete_de_phrases_v3_est_celle_de_phrases_v2_hors_le_verdict_d_ensemble_et_la_reproduction(tmp_path):
    conditions, fiche, etat = _conditions(tmp_path / "a", _lentille("R", "p1"), _lentille("S", "autre"))
    reproduction = rp.sans_comparaison(nl.PREMIERE_PASSE_JAMAIS_LANCEE)
    arguments = (conditions, fiche, conditions["course"], True, reproduction, la.MODULES_DIFFERENTS, ["phrase d'un nœud"], [(7, PUB)])
    ancienne, neuve = p2.tete(*arguments), p3.tete(*arguments, LIGNE_SECONDE)
    assert list(neuve) == list(ancienne)                                                                 # mêmes clés, même ordre
    assert {k for k in neuve if neuve[k] != ancienne[k]} == {"verdict_d_ensemble"}
    assert p3.tete(*arguments) == ancienne                                                               # sans ligne : la tête d'avant
    # une ligne de la fiche qui porte une paraphrase interdite : refusée quand elle serait écrite, sans effet quand elle ne l'est pas
    conditions, fiche, etat = _conditions(tmp_path / "b", _lentille("R", "p1"), _lentille("S", "p1"), plus=("avertissement",),
                                          ligne="lentilles équivalentes")
    arguments = (conditions, fiche, conditions["course"], False, reproduction, la.MODULES_DIFFERENTS, [], [])
    with pytest.raises(Refus, match="phrase interdite"):
        p2.tete(*arguments)
    assert "équivalentes" not in json.dumps(p3.tete(*arguments, None), ensure_ascii=False)
    with pytest.raises(Refus, match="phrase interdite"):
        p3.tete(*arguments, "lentilles équivalentes")


@pytest.fixture(scope="module")
def sans_inscription(tmp_path_factory, mp):
    """Bout en bout, nos deux lentilles au premier palier ; la fiche de rangement porte une ligne d'ensemble de la lecture de
    la seconde course, et cette lecture **n'est pas inscrite** au registre propre ; première passe jamais lancée."""
    m = J3.monde(tmp_path_factory.mktemp("sans-inscription"), mp)
    assert m.fiche["lecture_seconde_course"]["ligne_d_ensemble"] == LIGNE_SECONDE
    return J3.jouer(m)


def test_n2_bis_bout_en_bout_lecture_non_inscrite_la_ligne_de_la_fiche_n_est_pas_recopiee_par_le_lanceur_v2(sans_inscription):
    T = sans_inscription.tables
    assert T["nos_lentilles"]["ligne_de_la_lecture_de_la_seconde_course"] is None
    ensemble = T["tete"]["verdict_d_ensemble"]
    assert len(ensemble) == 1 and ensemble[0]["lentilles"] == ["R", "S"] and "seconde course" not in ensemble[0]["texte"]
    assert ensemble[0]["texte"].endswith(f"Réserves sur nos lentilles à ces couches : {p2.RESERVES_DES_DEUX}.")
    assert LIGNE_SECONDE not in json.dumps(T["tete"], ensure_ascii=False)
    assert T["tete"]["reproduction"][0] == p2.NOTE_PREMIERE_PASSE_REMPLACEE                              # jamais lancée : inchangé
    assert all("note" not in c for c in sans_inscription.phrases["comparaisons_entre_lentilles"])        # N3 : aucune note sans le cas


def test_n2_bout_en_bout_la_tete_des_tables_porte_la_ligne_de_la_seconde_course(bout_en_bout):
    T = bout_en_bout["tables"]
    assert T["nos_lentilles"]["ligne_de_la_lecture_de_la_seconde_course"] == LIGNE_SECONDE
    ensemble = T["tete"]["verdict_d_ensemble"]
    assert len(ensemble) == 1 and ensemble[0]["lentilles"] == ["R"] and SUITE in ensemble[0]["texte"]
    assert "seules les mesures faites sur notre lentille R la décrivent." + SUITE + " Réserves qui portent" in ensemble[0]["texte"]


# =============================================================================================================================================
# N4 — phrase de tête de la reproduction quand l'état de la première passe a changé depuis le montage (nœud N-dev-9, option (a))
# =============================================================================================================================================
JAMAIS, NON_ACHEVEE, ACHEVEE = nl.PREMIERE_PASSE_JAMAIS_LANCEE, nl.PREMIERE_PASSE_NON_ACHEVEE, nl.PREMIERE_PASSE_ACHEVEE


def _reproduction(montage, calcul):
    en_vigueur, note = la._premiere_passe_en_vigueur(montage, calcul)
    return rp.sans_comparaison(en_vigueur) | {"premiere_passe_au_montage": montage, "premiere_passe_au_calcul": calcul, "note": note}


def test_n4_le_sens_severe_du_lanceur_est_garde_tel_quel():
    for montage in (JAMAIS, NON_ACHEVEE, ACHEVEE):
        for calcul in (JAMAIS, NON_ACHEVEE, ACHEVEE):
            assert la._premiere_passe_en_vigueur(montage, calcul) == la1._premiere_passe_en_vigueur(montage, calcul)
    assert inspect.getsource(la._premiere_passe_en_vigueur) == inspect.getsource(la1._premiere_passe_en_vigueur)
    assert la._premiere_passe_en_vigueur(JAMAIS, ACHEVEE)[0] == NON_ACHEVEE          # jamais lancée au montage, lancée depuis : non remplacée
    assert la._premiere_passe_en_vigueur(NON_ACHEVEE, ACHEVEE)[0] == NON_ACHEVEE     # en cours au montage, achevée depuis : non reproduite


def test_n4_phrase_gelee_quand_la_passe_etait_lancee_et_non_achevee_au_montage_et_l_est_encore():
    r = _reproduction(NON_ACHEVEE, NON_ACHEVEE)
    assert p3.phrases_de_la_reproduction(r, la.MODULES_DIFFERENTS) == [p2.PHRASE_REPRODUCTION_NON_FAITE]
    assert p3.phrases_de_la_reproduction(rp.sans_comparaison(NON_ACHEVEE), la.MODULES_DIFFERENTS) == [p2.PHRASE_REPRODUCTION_NON_FAITE]


def test_n4_passe_en_cours_au_montage_et_achevee_depuis_la_phrase_gelee_inexacte_n_est_plus_ecrite():
    r = _reproduction(NON_ACHEVEE, ACHEVEE)
    assert r["etat"] == rp.ETAT_NON_FAITE
    assert p2.phrases_de_la_reproduction(r, la.MODULES_DIFFERENTS) == [p2.PHRASE_REPRODUCTION_NON_FAITE]   # le défaut
    assert "avant le nœud de la v1" in p2.PHRASE_REPRODUCTION_NON_FAITE
    neuves = p3.phrases_de_la_reproduction(r, la.MODULES_DIFFERENTS)
    assert neuves == [p3.NOTE_ACHEVEE_DEPUIS_LE_MONTAGE]
    note = neuves[0]
    assert note.startswith("Reproduction de la première passe : non faite ;") and "avant le nœud de la v1" not in note
    assert "il n'y a pas de nœud de la v1" in note and "sont celles de la première passe" in note and "lancée et non achevée" not in note
    assert "note du code, non une phrase gelée" in note and p2.exiger_sans_paraphrase_interdite(note) == note


@pytest.mark.parametrize("calcul", [NON_ACHEVEE, ACHEVEE])
def test_n4_passe_jamais_lancee_au_montage_et_lancee_depuis_non_remplacee_et_dit_ainsi(calcul):
    r = _reproduction(JAMAIS, calcul)
    assert r["etat"] == rp.ETAT_NON_FAITE and r["phrases_de_la_lentille_publique_et_des_logits_ecrites"] is False
    neuves = p3.phrases_de_la_reproduction(r, la.MODULES_DIFFERENTS)
    assert neuves == [p3.NOTE_LANCEE_DEPUIS_LE_MONTAGE]
    assert "jamais lancée au montage de la seconde passe et lancée depuis" in neuves[0] and "ne la remplace pas" in neuves[0]
    assert "avant le nœud de la v1" not in neuves[0] and "lancée et non achevée" not in neuves[0]
    assert p2.exiger_sans_paraphrase_interdite(neuves[0]) == neuves[0]


def test_n4_reproduction_faite_ou_premiere_passe_remplacee_les_phrases_de_phrases_v2():
    remplacee = _reproduction(JAMAIS, JAMAIS)
    assert remplacee["etat"] == rp.ETAT_REMPLACEE
    assert p3.phrases_de_la_reproduction(remplacee, la.MODULES_DIFFERENTS) == p2.phrases_de_la_reproduction(remplacee, la.MODULES_DIFFERENTS)
    assert p3.phrases_de_la_reproduction(remplacee, la.MODULES_DIFFERENTS)[0] == p2.NOTE_PREMIERE_PASSE_REMPLACEE
    faite = {"etat": rp.ETAT_FAITE, "nombre_de_lectures_differentes": 0, "premiere_passe_au_montage": ACHEVEE,
             "premiere_passe_au_calcul": ACHEVEE}
    assert p3.phrases_de_la_reproduction(faite, la.MODULES_DIFFERENTS) == [
        "Reproduction de la première passe : aucune.",
        "code de lecture différent de celui de la première passe : statistiques_v4, lanceur_seconde_passe_v2"]


def test_n4_bout_en_bout_passe_achevee_depuis_le_montage_tete_exacte_et_aucune_phrase_de_la_lentille_publique(bout_en_bout):
    T, p = bout_en_bout["tables"], bout_en_bout["phrases"]
    r = T["reproduction_de_la_premiere_passe"]
    assert r["etat"] == rp.ETAT_NON_FAITE and r["premiere_passe_au_montage"] == NON_ACHEVEE and r["premiere_passe_au_calcul"] == ACHEVEE
    assert "la reproduction n'est pas faite" in r["note"]
    assert T["tete"]["reproduction"] == [p3.NOTE_ACHEVEE_DEPUIS_LE_MONTAGE] == p["tete"]["reproduction"]
    assert not any(l.get("lentille") in (PUB, LOG) for l in p["directions"] + p["comparaisons"])
    texte = json.dumps([l.get("phrases") for l in p["directions"]] + [c["phrase"] for c in p["comparaisons"]], ensure_ascii=False)
    assert "Par la lentille publique" not in texte and "Par la lentille des logits" not in texte
    assert any(l.get("lentille") == R for l in p["directions"]) and p["comparaisons_entre_lentilles"]


# =============================================================================================================================================
# N3 — « non calculable sur vingt » : une note accompagne la phrase gelée
# =============================================================================================================================================
def _forcer(tables: dict, libelle: str, moities_calculables: bool) -> tuple[dict, int]:
    """Une copie des tables où la première comparaison principale calculable reçoit ce libellé, et où le recouvrement des
    moitiés de la même lecture est, ou non, calculable. Rend (tables, rang de la comparaison dans les phrases)."""
    T, rang = copy.deepcopy(tables), 0
    for d in T["directions"]:
        for e in d.get("entre_lentilles", {}).values():
            c = e["principale"]
            if c.get("libelle") is None:
                continue
            if c["libelle"] != co.NON_CALCULABLE:
                c["libelle"] = libelle
                c |= {"lentille": R, "autre": PUB, "libelles": ["x", "y"]}
                e["moities"] = ({"libelle": "calculé", "recouvrement": 17} if moities_calculables
                                else co.non_calculable(co.MOTIF_NUL_REFAIT))
                return T, rang
            rang += 1
    raise AssertionError("aucune comparaison calculable dans les tables jouets")


@pytest.mark.parametrize("libelle", [co.LECTURE_COMMUNE, co.LECTURE_PROPRE])
def test_n3_recouvrement_des_moities_non_calculable_la_phrase_gelee_est_gardee_et_une_note_le_dit(bout_en_bout, libelle):
    T, rang = _forcer(bout_en_bout["tables"], libelle, False)
    ligne = la.rendre_phrases(T)["comparaisons_entre_lentilles"][rang]
    assert ligne["libelle"] == libelle and "les deux moitiés de notre R : non calculable sur vingt" in ligne["phrase"]
    assert ligne["note"] == la.NOTE_MOITIES_NON_CALCULABLES.format(motif=co.MOTIF_NUL_REFAIT)
    assert co.MOTIF_NUL_REFAIT in ligne["note"] and "note du code, non une phrase gelée" in ligne["note"]
    assert ligne["phrase"] == la1.rendre_phrases(T)["comparaisons_entre_lentilles"][rang]["phrase"]      # aucun mot gelé ne change
    assert "note" not in la1.rendre_phrases(T)["comparaisons_entre_lentilles"][rang]                     # le défaut : rien ne le disait
    sain, rang = _forcer(bout_en_bout["tables"], libelle, True)
    ligne = la.rendre_phrases(sain)["comparaisons_entre_lentilles"][rang]
    assert "note" not in ligne and "les deux moitiés de notre R : 17 sur vingt" in ligne["phrase"]


@pytest.mark.parametrize("libelle", [co.DEUX_NON_DISTINCTES, co.MIXTE])
def test_n3_aucune_note_pour_un_libelle_dont_la_phrase_ne_cite_pas_les_moities(bout_en_bout, libelle):
    T, rang = _forcer(bout_en_bout["tables"], libelle, False)
    ligne = la.rendre_phrases(T)["comparaisons_entre_lentilles"][rang]
    assert "note" not in ligne and "moitiés" not in ligne["phrase"]


def test_n3_les_phrases_sans_ce_cas_sont_celles_du_lanceur_v1(bout_en_bout):
    assert la.rendre_phrases(bout_en_bout["tables"]) == la1.rendre_phrases(bout_en_bout["tables"])


# =============================================================================================================================================
# Point 6 du mandat — l'essai dépendant de l'ordre
# =============================================================================================================================================
def test_point_6_l_entree_de_la_table_des_modules_ne_suffit_pas_il_faut_retirer_aussi_l_attribut_du_paquet(nu_monde, monkeypatch):
    """Pourquoi l'ancien essai tombe dès qu'un fichier chargé avant lui a importé `corpus_pagine_v1` : `from . import x` rend
    l'attribut du paquet s'il existe, sans consulter la table des modules. Ici le module est importé (le lanceur v2 l'importe) :
    avec la seule entrée de la table retirée, l'import réussit encore (l'ancien essai attendait un arrêt, d'où son échec) ;
    avec l'attribut retiré aussi, l'import échoue, et `montage_v2` arrête."""
    import controle_ia.lentilles_sondes_bbis as paquet
    assert hasattr(paquet, "corpus_pagine_v1")
    monkeypatch.setitem(sys.modules, "controle_ia.lentilles_sondes_bbis.corpus_pagine_v1", None)
    with pytest.raises(Arret) as e:                                        # l'import réussit : l'arrêt vient de la lecture des provenances
        m2.cibles_du_corpus(nu_monde.tmp, nu_monde.transport)
    assert "n'est pas branchée" not in str(e.value) and "provenance du corpus" in str(e.value)
    monkeypatch.delattr(paquet, "corpus_pagine_v1")
    with pytest.raises(Arret, match="n'est pas branchée"):
        m2.cibles_du_corpus(nu_monde.tmp, nu_monde.transport)


# =============================================================================================================================================
# La version 2 du lanceur est la version 1 plus ces seuls changements
# =============================================================================================================================================
COPIES = {"lentilles_sondes_bbis_seconde_passe_jouets_v2.py": "lentilles_sondes_bbis_seconde_passe_jouets_v3.py",
          "test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py": "test_lentilles_sondes_bbis_seconde_passe_lanceur_v2.py"}


def test_l_outil_de_fabrique_rejoue_rend_le_lanceur_v2_ses_jouets_et_ses_essais_a_l_octet_pres(tmp_path):
    paquet, essais = tmp_path / "paquet", tmp_path / "essais"
    paquet.mkdir()
    essais.mkdir()
    (paquet / "lanceur_seconde_passe_v1.py").write_bytes((PAQUET / "lanceur_seconde_passe_v1.py").read_bytes())
    for origine in COPIES:
        (essais / origine).write_bytes((ESSAIS / origine).read_bytes())
    r = subprocess.run([sys.executable, "-B", str(OUTIL), str(paquet), str(essais)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert (paquet / "lanceur_seconde_passe_v2.py").read_bytes() == (PAQUET / "lanceur_seconde_passe_v2.py").read_bytes()
    for copie in COPIES.values():
        assert (essais / copie).read_bytes() == (ESSAIS / copie).read_bytes(), copie


def test_lignes_du_lanceur_v1_toutes_gardees_hors_onze_lignes():
    """De `lanceur_seconde_passe_v1` à `lanceur_seconde_passe_v2` : onze lignes retirées, et aucune autre (les deux lignes des
    modules et celle des modules différents ; le point de branchement des réglages ; la condition de lecture ; les cibles du
    corpus ; les deux lignes de la pose du cache ; les deux lignes de la tête ; le second relevé de la ligne de la seconde
    course). Aucune ligne de calcul n'en fait partie."""
    v1 = (PAQUET / "lanceur_seconde_passe_v1.py").read_text(encoding="utf-8").splitlines()
    v2 = (PAQUET / "lanceur_seconde_passe_v2.py").read_text(encoding="utf-8").splitlines()
    diff = list(difflib.ndiff(v1, v2))
    assert [l[2:] for l in diff if l.startswith("- ")] == [
        '           "audits_v2", "phrases_v1", "phrases_v2", "nos_lentilles_v1", "comparaisons_lentilles_v1", "reproduction_v1",',
        '           "lanceur_v7", "lanceur_seconde_passe_v1")',
        'MODULES_DIFFERENTS = ("statistiques_v4", "lanceur_seconde_passe_v1")',
        '    cibles_corpus: object = None                        # point de branchement (nœud N-dev-1) : voir `montage_v2.cibles_du_corpus`',
        '    return etat, issue, fiche, nl.condition_de_lecture(fiche, etat, ctx.racine_depot)',
        '    rapport["essais_un_octet"] += mo.essais_un_octet(transport, cle, m2.cibles_du_corpus(voisin, transport, r.cibles_corpus))',
        '    mo.poser_cache_tokeniseur(hf_home, {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA},',
        '                              r.depot_llama, r.revision_llama)',
        '    tete = ph.tete(conditions, fiche, conditions["course"], bool(etat_registre.presentes(K2.CLE_LECTURE_SECONDE_COURSE)), reproduction,',
        '                   MODULES_DIFFERENTS, issue["phrases_de_tete"], non_tenues)',
        '                          "ligne_de_la_lecture_de_la_seconde_course": _ligne_de_la_seconde_course(fiche, conditions["course"], etat_registre),']
    for fonction in ("_Couche", "_etiqueter", "_comparaisons", "_libeller_les_comparaisons", "_comptes", "_audit", "calculer",
                     "charger_montage", "jouer_gardes_lecture", "exiger_fiche_code", "ligne_affichee", "_ligne_de_la_seconde_course",
                     "_premiere_passe_en_vigueur", "principal"):
        assert inspect.getsource(getattr(la, fonction)) == inspect.getsource(getattr(la1, fonction)), fonction
    assert la.st is la1.st and la.st.__name__.endswith("statistiques_v4")                                # le module des statistiques, inchangé
