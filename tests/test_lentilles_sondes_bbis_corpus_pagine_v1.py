"""Essais du correctif de la pagination de l'arbre du corpus (`corpus_pagine_v1`, `lanceur_v8`).

Le défaut : l'arbre d'un jeu de données du corpus des jetons gardés est servi par pages (lien de la page suivante dans
l'en-tête `Link`) ; la première page ne porte que des dossiers ; `montage_v1.cibles_corpus` ne lit que cette page et s'arrête
sur « aucun fichier de données dans l'arbre ».

R5 : chaque garde a son cas sain et son artefact. Toutes les réponses sont fabriquées ici : aucune requête ne sort, aucune
clé n'est lue (la seule clé des essais est la fausse clé des jouets). Les noms de dossiers et de fichiers des arbres
fabriqués sont inventés pour ces essais.
"""
from __future__ import annotations

import difflib
import inspect
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v7 as J7  # noqa: E402
import lentilles_sondes_bbis_jouets_v8 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import corpus_pagine_v1 as cp  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v7 as la7  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v8 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, Refus  # noqa: E402

PAQUET = Path(la.__file__).resolve().parent
ESSAIS = Path(__file__).resolve().parent
OUTIL = J.RACINE / "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-v8-v1.py"
DEPOTS = {"dclm": ("jouet/dclm", "rdclm"), "zh": ("jouet/zh", "rzh"), "code": ("jouet/code", "rcode"), "chat": ("jouet/chat", "rchat")}
FICHIER_ZH = "data/langue_jouet/train/000_00000.parquet"
PHRASE_AUCUN = "jeu de données de la tranche zh : aucun fichier de données dans l'arbre : arrêt ; nœud"


# --- réponses fabriquées --------------------------------------------------------------------------------------------------------------------
def _voisin(tmp: Path, sans: str | None = None) -> Path:
    """Dossier du code voisin réduit à ses provenances du corpus (une par tranche ; `sans` : tranche dont la provenance manque)."""
    corpus = tmp / "voisin" / "data" / "corpus"
    corpus.mkdir(parents=True)
    for tranche, (depot, revision) in DEPOTS.items():
        nom = f"act-{tranche}.provenance.json" if tranche != "chat" else "act-chat-llama-3.1-8b-instruct.provenance.json"
        if tranche != sans:
            (corpus / nom).write_text(json.dumps({"repo": depot, "revision": revision}), encoding="utf-8")
    return tmp / "voisin"


def _arbre(tranche: str) -> str:
    return mo.url_arbre(*DEPOTS[tranche], jeu=True, recursif=True)


def _suite(tranche: str, rang: int) -> str:
    """Adresse fabriquée de la page de rang `rang` (≥ 2) de l'arbre d'une tranche : la même cible, un curseur en plus."""
    return f"{_arbre(tranche)}&cursor=curseur-{rang}"


def _dossiers(n: int, rang: int = 1) -> bytes:
    return json.dumps([{"type": "directory", "path": f"data/dossier-{rang}-{i:04d}"} for i in range(n)]).encode()


def _fichiers(*chemins: str) -> bytes:
    return json.dumps([{"type": "file", "path": c} for c in chemins]).encode()


class TransportPages:
    """Hôte simulé qui sert des pages : `pages` (URL → (octets, URL de la page suivante ou `None`)) ; `refus` : URL refusées.
    `octets` rend la page seule, sans son lien de suite : c'est tout ce que `montage_v1.cibles_corpus` peut voir."""

    def __init__(self, pages: dict, refus=()):
        self.pages, self.refus, self.appels = dict(pages), set(refus), []

    def _lire(self, url):
        if url in self.refus or url not in self.pages:
            raise mo.RefusReseau(f"requête refusée par {url.split('?')[0]} (code 403)")
        return self.pages[url]

    def page(self, url):
        self.appels.append(("page", url))
        return self._lire(url)

    def octets(self, url, cle=None, debut=None, fin=None):
        self.appels.append(("octets", url, cle is not None))
        return self._lire(url)[0]


def _monde(zh: dict | None = None, **autres) -> dict:
    """Pages des quatre jeux : sans pagination par défaut (un fichier dès la première page) ; `zh` remplace celles de la tranche zh."""
    pages = {_arbre(t): (_fichiers("README.md", "data/train-00000.parquet"), None) for t in DEPOTS}
    if zh is not None:
        del pages[_arbre("zh")]
        pages |= zh
    return pages | autres


def _zh_pagine(pages_de_dossiers: int = 1, fichier: str | None = FICHIER_ZH) -> dict:
    """Arbre de la tranche zh : `pages_de_dossiers` pages de dossiers seulement, puis (si `fichier`) une page qui porte le fichier."""
    urls = [_arbre("zh")] + [_suite("zh", r) for r in range(2, pages_de_dossiers + 2)]
    pages = {}
    for i in range(pages_de_dossiers):
        dernier = i == pages_de_dossiers - 1 and fichier is None
        pages[urls[i]] = (_dossiers(1000, i + 1), None if dernier else urls[i + 1])
    if fichier is not None:
        pages[urls[pages_de_dossiers]] = (_fichiers("data/langue_jouet/train/000_00001.parquet", fichier, "data/langue_jouet/LISEZ.md"), None)
    return pages


# --- le défaut et sa correction --------------------------------------------------------------------------------------------------------------
def test_sain_arbre_pagine_fichier_en_deuxieme_page_trouve(tmp_path):
    """Première page : 1 000 dossiers et aucun fichier ; le fichier de données est en deuxième page : il est trouvé, et la
    cible de l'essai d'un octet est le plus petit chemin de cette page."""
    t = TransportPages(_monde(_zh_pagine()))
    cibles = cp.cibles_corpus(_voisin(tmp_path), t)
    assert [c.nom for c in cibles] == [f"jeu de données de la tranche {x}" for x in K.TRANCHES_CORPUS]
    assert cibles[1].url == mo.url_fichier(*DEPOTS["zh"], FICHIER_ZH, jeu=True)
    assert all(not c.avec_cle and c.sorte == "octet" for c in cibles)
    assert t.appels == [("page", _arbre("dclm")), ("page", _arbre("zh")), ("page", _suite("zh", 2)), ("page", _arbre("code")),
                        ("page", _arbre("chat"))]


def test_artefact_la_meme_reponse_lue_par_l_ancien_code_donne_l_arret_nomme(tmp_path):
    """Le défaut : `montage_v1.cibles_corpus`, sur la même réponse paginée, ne voit que la première page et s'arrête."""
    voisin = _voisin(tmp_path)
    with pytest.raises(Arret) as e:
        mo.cibles_corpus(voisin, TransportPages(_monde(_zh_pagine())))
    assert str(e.value) == PHRASE_AUCUN
    assert cp.cibles_corpus(voisin, TransportPages(_monde(_zh_pagine())))[1].url.endswith(FICHIER_ZH)      # cas sain, même réponse


def test_arbre_sans_pagination_meme_resultat_que_l_ancien_code(tmp_path):
    """Un fichier dès la première page : les cibles sont celles de `montage_v1.cibles_corpus`, et une seule page est lue par jeu."""
    voisin, t = _voisin(tmp_path), TransportPages(_monde())
    assert cp.cibles_corpus(voisin, t) == mo.cibles_corpus(voisin, TransportPages(_monde()))
    assert t.appels == [("page", _arbre(x)) for x in K.TRANCHES_CORPUS]


def test_premiere_page_qui_porte_un_fichier_les_pages_suivantes_ne_sont_pas_lues(tmp_path):
    pages = _monde({_arbre("zh"): (_fichiers("data/b.parquet", "data/a.parquet"), _suite("zh", 2)),
                    _suite("zh", 2): (_fichiers("data/0.parquet"), None)})
    t = TransportPages(pages)
    assert cp.cibles_corpus(_voisin(tmp_path), t)[1].url == mo.url_fichier(*DEPOTS["zh"], "data/a.parquet", jeu=True)
    assert ("page", _suite("zh", 2)) not in t.appels


@pytest.mark.parametrize("pages_de_dossiers", [1, 3])
def test_arbre_sans_fichier_sur_toutes_les_pages_la_phrase_d_arret_de_l_ancien_code(pages_de_dossiers, tmp_path):
    """Arbre fini, aucune page ne porte de fichier de données : la phrase d'arrêt est celle de `montage_v1`, mot pour mot."""
    voisin = _voisin(tmp_path)
    t = TransportPages(_monde(_zh_pagine(pages_de_dossiers, fichier=None)))
    with pytest.raises(Arret) as e:
        cp.cibles_corpus(voisin, t)
    assert str(e.value) == PHRASE_AUCUN
    assert sum(a[1].startswith(_arbre("zh")) for a in t.appels) == pages_de_dossiers          # toutes les pages lues avant l'arrêt
    with pytest.raises(Arret) as ancien:                                                       # la même phrase, par l'ancien code
        mo.cibles_corpus(voisin, TransportPages(_monde({_arbre("zh"): (_dossiers(5), None)})))
    assert str(ancien.value) == str(e.value)


def test_fichiers_qui_ne_sont_pas_des_donnees_ne_comptent_pas(tmp_path):
    """Une page de fichiers sans extension de données (et une entrée qui n'est pas un objet) ne satisfait pas la recherche."""
    pages = {_arbre("zh"): (json.dumps([{"type": "file", "path": "LISEZ.md"}, "entrée inattendue",
                                        {"type": "directory", "path": "data/dossier.parquet"}]).encode(), None)}
    with pytest.raises(Arret, match="aucun fichier de données dans l'arbre"):
        cp.cibles_corpus(_voisin(tmp_path), TransportPages(_monde(pages)))


# --- borne du nombre de pages ------------------------------------------------------------------------------------------------------------------
class TransportSansFin(TransportPages):
    """Chaque page de l'arbre de la tranche zh ne porte que des dossiers et renvoie à une page suivante, sans fin."""

    def page(self, url):
        if not url.startswith(_arbre("zh")):
            return super().page(url)
        self.appels.append(("page", url))
        rang = int(url.rsplit("-", 1)[1]) if "cursor=" in url else 1
        return _dossiers(3, rang), _suite("zh", rang + 1)


def test_pages_sans_fin_arret_a_la_borne():
    t = TransportSansFin({})
    with pytest.raises(Arret, match=r"plus de 100 pages d'arbre lues sans fichier de données \(borne du nombre de pages\)") as e:
        cp.premier_fichier_de_donnees(t, *DEPOTS["zh"], "zh")
    assert cp.BORNE_PAGES == 100 and len(t.appels) == 100 and "tranche zh" in str(e.value)
    assert "cursor" not in str(e.value) and "http" not in str(e.value)


def test_pages_sans_fin_arret_a_la_borne_par_cibles_corpus(tmp_path):
    t = TransportSansFin(_monde())
    with pytest.raises(Arret, match=r"plus de 7 pages d'arbre lues"):
        cp.cibles_corpus(_voisin(tmp_path), t, borne=7)
    assert sum(a[1].startswith(_arbre("zh")) for a in t.appels) == 7


@pytest.mark.parametrize("pages_de_dossiers, trouve", [(4, True), (5, False)])
def test_borne_sain_et_artefact_au_bord(pages_de_dossiers, trouve):
    """Borne de 5 pages : un fichier en cinquième page est trouvé (cas sain) ; en sixième page, arrêt à la borne (artefact)."""
    t = TransportPages(_zh_pagine(pages_de_dossiers))
    if trouve:
        assert cp.premier_fichier_de_donnees(t, *DEPOTS["zh"], "zh", borne=5) == FICHIER_ZH
        assert len(t.appels) == 5
    else:
        with pytest.raises(Arret, match="borne du nombre de pages"):
            cp.premier_fichier_de_donnees(t, *DEPOTS["zh"], "zh", borne=5)
        assert len(t.appels) == 5 and ("page", _suite("zh", 6)) not in t.appels


# --- refus du réseau, provenance ----------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("page_refusee", [1, 2])
def test_requete_refusee_sur_une_page_la_phrase_d_arret_de_l_ancien_code(page_refusee, tmp_path):
    voisin = _voisin(tmp_path)
    url = _arbre("zh") if page_refusee == 1 else _suite("zh", 2)
    with pytest.raises(Arret) as e:
        cp.cibles_corpus(voisin, TransportPages(_monde(_zh_pagine()), refus={url}))
    assert str(e.value) == (f"essai d'un octet refusé (jeu de données de la tranche zh) : requête refusée par {_arbre('zh').split('?')[0]} "
                            "(code 403) : arrêt avant tout téléchargement long ; nœud")
    if page_refusee == 1:                                                                       # la même phrase, par l'ancien code
        with pytest.raises(Arret) as ancien:
            mo.cibles_corpus(voisin, TransportPages(_monde(_zh_pagine()), refus={url}))
        assert str(ancien.value) == str(e.value)
    assert cp.cibles_corpus(voisin, TransportPages(_monde(_zh_pagine())))                       # cas sain : sans refus


def test_provenance_absente_ou_illisible_la_phrase_d_arret_de_l_ancien_code(tmp_path):
    voisin = _voisin(tmp_path / "absente", sans="chat")
    with pytest.raises(Arret) as e:
        cp.cibles_corpus(voisin, TransportPages(_monde()))
    with pytest.raises(Arret) as ancien:
        mo.cibles_corpus(voisin, TransportPages(_monde()))
    assert str(e.value) == str(ancien.value) and "provenance du corpus act-chat-llama-3.1-8b-instruct.provenance.json" in str(e.value)
    illisible = _voisin(tmp_path / "illisible")
    (illisible / "data" / "corpus" / "act-code.provenance.json").write_text("{", encoding="utf-8")
    with pytest.raises(Arret, match="provenance du corpus act-code.provenance.json absente ou illisible"):
        cp.cibles_corpus(illisible, TransportPages(_monde()))


# --- lien de page suivante hors de l'arbre demandé ------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("ailleurs", [
    "https://autre-hote.example/api/datasets/jouet/zh/tree/rzh?recursive=true&cursor=x",
    "https://huggingface.co.autre-hote.example/api/datasets/jouet/zh/tree/rzh?recursive=true&cursor=x",
    "http://huggingface.co/api/datasets/jouet/zh/tree/rzh?recursive=true&cursor=x",
    mo.url_arbre("jouet/autre", "rzh", jeu=True, recursif=True) + "&cursor=x",
    mo.url_arbre("jouet/zh-autre", "rzh", jeu=True, recursif=True) + "&cursor=x",
    mo.url_arbre("jouet/zh", "rzh", jeu=False, recursif=True) + "&cursor=x",
    mo.url_fichier("jouet/zh", "rzh", "data/autre.parquet", jeu=True)])
def test_lien_de_page_suivante_hors_de_l_arbre_du_jeu_demande_jamais_suivi(ailleurs):
    t = TransportPages({_arbre("zh"): (_dossiers(3), ailleurs), ailleurs: (_fichiers("data/a.parquet"), None)})
    with pytest.raises(Arret, match="le lien de la page suivante sort de l'arbre du jeu demandé") as e:
        cp.premier_fichier_de_donnees(t, *DEPOTS["zh"], "zh")
    assert t.appels == [("page", _arbre("zh"))]                                                 # l'adresse proposée n'est jamais demandée
    assert "autre" not in str(e.value) and "cursor" not in str(e.value) and "http" not in str(e.value)


def test_lien_de_page_suivante_dans_l_arbre_du_jeu_demande_suivi():
    """Cas sain de la garde : même hôte, même jeu, requête différente (curseur) : le lien est suivi ; il l'est aussi quand
    l'hôte écrit la révision autrement dans son lien (la révision du lien n'est pas comparée)."""
    t = TransportPages(_zh_pagine())
    assert cp.premier_fichier_de_donnees(t, *DEPOTS["zh"], "zh") == FICHIER_ZH
    assert t.appels[-1] == ("page", _suite("zh", 2))
    autrement = mo.url_arbre("jouet/zh", "revision-ecrite-en-entier", jeu=True, recursif=True) + "&cursor=x"
    t = TransportPages({_arbre("zh"): (_dossiers(3), autrement), autrement: (_fichiers(FICHIER_ZH), None)})
    assert cp.premier_fichier_de_donnees(t, *DEPOTS["zh"], "zh") == FICHIER_ZH
    assert t.appels == [("page", _arbre("zh")), ("page", autrement)]


# --- transport sans lecture de page ---------------------------------------------------------------------------------------------------------------
def test_transport_sans_lecture_de_page_arret_jamais_de_repli_sur_la_premiere_page(tmp_path):
    """Le transport simulé de la version 7 des jouets ne sait rendre que des octets : arrêt nommé, aucune requête ; le même
    monde servi par le transport de la version 8 des jouets (méthode `page`) donne les cibles."""
    voisin = _voisin(tmp_path)
    fichiers = {_arbre(x): _fichiers("data/train-00000.parquet") for x in DEPOTS}
    ancien = J7.TransportSimule(fichiers)
    assert not hasattr(ancien, "page")
    with pytest.raises(Arret, match="transport sans lecture de page"):
        cp.cibles_corpus(voisin, ancien)
    assert ancien.appels == []
    neuf = J.TransportSimule(fichiers)
    assert cp.cibles_corpus(voisin, neuf) == mo.cibles_corpus(voisin, J7.TransportSimule(fichiers))
    assert [a[:3] for a in neuf.appels] == [("page", _arbre(x), False) for x in K.TRANCHES_CORPUS]


# --- en-tête `Link` ------------------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("en_tete, attendu", [
    (None, None), ("", None),
    ('<https://h/api/datasets/d/tree/r?recursive=true&cursor=abc%3D>; rel="next"', "https://h/api/datasets/d/tree/r?recursive=true&cursor=abc%3D"),
    ('<https://h/a?cursor=1>; rel="prev", <https://h/a?cursor=3>; rel="next"', "https://h/a?cursor=3"),
    ('<https://h/a?cursor=1>; rel="prev"', None),
    ("<https://h/a?cursor=2>; rel=next", "https://h/a?cursor=2"),
    ('<https://h/a?cursor=2>; title="suite"; REL="last next"', "https://h/a?cursor=2"),
    ('<https://h/a?x=1,2&cursor=2>; rel="next"', "https://h/a?x=1,2&cursor=2"),
    ('<https://h/a?cursor=2>; rel="nextpage"', None),
    ('<https://h/a?cursor=2>; title="rel=next"', None),
    ('</api/datasets/d/tree/r?cursor=2>; rel="next"', "https://h/api/datasets/d/tree/r?cursor=2"),
    ("sans chevrons; rel=next", None)])
def test_lien_suivant_lu_dans_l_en_tete_link(en_tete, attendu):
    assert cp.lien_suivant(en_tete, "https://h/api/datasets/d/tree/r?recursive=true") == attendu


# --- transport réel, sur une session fabriquée (aucune requête ne sort) ---------------------------------------------------------------------------
class ReponseFabriquee:
    def __init__(self, contenu: bytes, lien: str | None = None, code: int = 200, rupture: Exception | None = None):
        self._contenu, self.status_code, self._rupture, self.fermee = contenu, code, rupture, False
        self.headers = {} if lien is None else {"Link": f'<{lien}>; rel="next"'}

    @property
    def content(self):
        if self._rupture is not None:
            raise self._rupture
        return self._contenu

    def close(self):
        self.fermee = True


class SessionFabriquee:
    """Tient lieu de `requests.Session` : rend les réponses fabriquées, relève chaque appel avec ses en-têtes."""

    def __init__(self, reponses: dict):
        self.reponses, self.appels = dict(reponses), []

    def get(self, url, headers=None, stream=False, timeout=None, allow_redirects=True):
        self.appels.append((url, dict(headers or {})))
        r = self.reponses.get(url)
        if isinstance(r, Exception):
            raise r
        return r if r is not None else ReponseFabriquee(b"", code=404)


def _transport_reel(reponses: dict) -> tuple:
    pytest.importorskip("requests")
    t = mo.TransportRequests()
    t._session.close()
    t._session = SessionFabriquee(reponses)
    return t, t._session


def _reponses(pages: dict) -> dict:
    return {url: ReponseFabriquee(octets, suivant) for url, (octets, suivant) in pages.items()}


def test_transport_reel_les_pages_sont_suivies_par_l_en_tete_link_sans_cle(tmp_path):
    t, session = _transport_reel(_reponses(_monde(_zh_pagine(2))))
    cibles = cp.cibles_corpus(_voisin(tmp_path), t)
    assert cibles[1].url == mo.url_fichier(*DEPOTS["zh"], FICHIER_ZH, jeu=True)
    assert [u for u, _ in session.appels] == [_arbre("dclm"), _arbre("zh"), _suite("zh", 2), _suite("zh", 3), _arbre("code"), _arbre("chat")]
    assert all(en_tetes == {"Accept-Encoding": "identity"} for _, en_tetes in session.appels)   # ni clé ni intervalle
    assert all(r.fermee for r in session.reponses.values())


def test_transport_reel_artefact_l_ancien_code_s_arrete_sur_la_premiere_page(tmp_path):
    t, _ = _transport_reel(_reponses(_monde(_zh_pagine(2))))
    with pytest.raises(Arret) as e:
        mo.cibles_corpus(_voisin(tmp_path), t)
    assert str(e.value) == PHRASE_AUCUN


def test_transport_reel_refus_et_rupture_messages_sans_en_tete_ni_texte_d_exception(tmp_path):
    secret = "texte-d-exception-qui-ne-doit-pas-sortir"
    cas = {"code 403": ReponseFabriquee(b"", code=403), "requête impossible": ConnectionError(secret),
           "lecture interrompue": ReponseFabriquee(b"", rupture=OSError(secret))}
    for mot, reponse in cas.items():
        reponses = _reponses(_monde(_zh_pagine()))
        reponses[_suite("zh", 2)] = reponse
        t, _ = _transport_reel(reponses)
        with pytest.raises(Arret) as e:
            cp.cibles_corpus(_voisin(tmp_path / mot.replace(" ", "-")), t)
        message = str(e.value)
        assert message.startswith("essai d'un octet refusé (jeu de données de la tranche zh) : ") and mot in message
        assert message.endswith(" : arrêt avant tout téléchargement long ; nœud")
        assert secret not in message and "cursor" not in message and _arbre("zh").split("?")[0] in message
        if isinstance(reponse, ReponseFabriquee):
            assert reponse.fermee


def test_transport_reel_sans_en_tete_link_une_seule_page(tmp_path):
    t, session = _transport_reel({_arbre("zh"): ReponseFabriquee(_dossiers(4))})
    assert cp.page_requests(t, _arbre("zh")) == (_dossiers(4), None)
    with pytest.raises(Arret) as e:
        cp.premier_fichier_de_donnees(t, *DEPOTS["zh"], "zh")
    assert str(e.value) == PHRASE_AUCUN and len(session.appels) == 2


def test_la_cle_n_entre_dans_aucune_fonction_du_module():
    """Aucune fonction du module ne reçoit la clé, et le module ne la lit pas."""
    fonctions = [f for _, f in inspect.getmembers(cp, inspect.isfunction) if f.__module__ == cp.__name__]
    assert {f.__name__ for f in fonctions} == {"lien_suivant", "page_requests", "lire_page", "fichiers_de_donnees", "dans_l_arbre_du_jeu",
                                                "premier_fichier_de_donnees", "cibles_corpus"}
    assert all("cle" not in inspect.signature(f).parameters for f in fonctions)
    source = (PAQUET / "corpus_pagine_v1.py").read_text(encoding="utf-8")
    for interdit in ("lire_cle", "Cle(", "environ", "NOM_CLE", "Authorization", "valeur()", "print(", "logging"):
        assert interdit not in source, interdit


# --- le lanceur de la version 8 ---------------------------------------------------------------------------------------------------------------------
def _paginer_zh(m) -> None:
    """Dans un monde des jouets, sert l'arbre du jeu de la tranche zh en deux pages : dossiers seulement, puis le fichier."""
    arbre = mo.url_arbre(J.DEPOT_ZH, "rzh", jeu=True, recursif=True)
    suite = arbre + "&cursor=curseur-2"
    m.transport.fichiers[suite] = m.transport.fichiers[arbre]
    m.transport.fichiers[arbre] = _dossiers(1000)
    if hasattr(m.transport, "suites"):
        m.transport.suites[arbre] = suite


def test_montage_entier_de_la_version_8_arbre_pagine_les_sept_essais_d_un_octet_tenus(tmp_path):
    m = J.monde(tmp_path)
    _paginer_zh(m)
    la.monter(m.ctx)
    rapport = json.loads((tmp_path / "sortie" / "diag" / J.RUN / "montage-lentilles-bbis.json").read_text(encoding="utf-8"))
    assert rapport["gardes"]["toutes_tenues"] and len(rapport["essais_un_octet"]) == 7
    assert [e["cible"] for e in rapport["essais_un_octet"][3:]] == [f"jeu de données de la tranche {x}" for x in K.TRANCHES_CORPUS]
    assert all(e["tenu"] and not e["avec_cle"] for e in rapport["essais_un_octet"][3:])
    pages = [a for a in m.transport.appels if a[0] == "page"]
    assert len(pages) == 5 and all(a[2] is False for a in pages)                               # cinq pages, toutes sans clé
    premier_flux = next(i for i, a in enumerate(m.transport.appels) if a[0] == "flux")
    assert max(i for i, a in enumerate(m.transport.appels) if a[0] == "page") < premier_flux    # avant tout flux long
    assert set(rapport["code"]["empreintes"]) == {f"{x}.py" for x in la.MODULES}
    for dossier in (tmp_path / "sortie", tmp_path / "travail"):
        for p in dossier.rglob("*"):
            if p.is_file():
                assert J.FAUSSE_CLE.encode() not in p.read_bytes(), p


def test_artefact_montage_entier_de_la_version_7_meme_arbre_pagine_arret_nomme(tmp_path):
    """Le défaut au niveau du lanceur : `lanceur_v7`, sur le même arbre paginé, s'arrête avant tout téléchargement long."""
    m = J7.monde(tmp_path)
    _paginer_zh(m)
    with pytest.raises(Arret) as e:
        la7.monter(m.ctx)
    assert str(e.value) == PHRASE_AUCUN
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_modules_de_la_fiche_du_code_quatorze_dont_le_module_du_correctif():
    assert la.MODULES == la7.MODULES[:-1] + ("corpus_pagine_v1", "lanceur_v8") and la7.MODULES[-1] == "lanceur_v7"
    assert len(la.MODULES) == 14 and set(la.empreintes_du_code()) == {f"{m}.py" for m in la.MODULES}
    assert la.empreintes_du_code()["corpus_pagine_v1.py"] == J.sha((PAQUET / "corpus_pagine_v1.py").read_bytes())


def test_fiche_du_code_sans_l_empreinte_du_module_du_correctif_rien_ne_part(tmp_path):
    """La fiche du code doit porter `corpus_pagine_v1.py` : sans lui, ou avec une autre empreinte, rien ne part."""
    _, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    assert la.exiger_fiche_code(tmp_path / "depot", propre)["sha256"]                                  # cas sain
    fichiers = {f"{la.CHEMIN_PAQUET}/{m}.py": J.sha((PAQUET / f"{m}.py").read_bytes()) for m in la.MODULES}
    nom = f"{la.CHEMIN_PAQUET}/corpus_pagine_v1.py"
    for artefact in ({k: v for k, v in fichiers.items() if k != nom}, fichiers | {nom: "0" * 64}):
        J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers=artefact)
        with pytest.raises(Refus, match=r"corpus_pagine_v1\.py : empreinte absente de la fiche"):
            la.exiger_fiche_code(tmp_path / "depot", propre)


# --- la version 8 est la version 7 plus ce seul changement -------------------------------------------------------------------------------------------
COPIES = {"lentilles_sondes_bbis_jouets_v7.py": "lentilles_sondes_bbis_jouets_v8.py",
          "test_lentilles_sondes_bbis_addendum_concentration_v5.py": "test_lentilles_sondes_bbis_addendum_concentration_v6.py",
          "test_lentilles_sondes_bbis_corrections_contre_lecture_v6.py": "test_lentilles_sondes_bbis_corrections_contre_lecture_v7.py",
          "test_lentilles_sondes_bbis_garde_egalite_v4.py": "test_lentilles_sondes_bbis_garde_egalite_v5.py",
          "test_lentilles_sondes_bbis_gardes_non_vues_v6.py": "test_lentilles_sondes_bbis_gardes_non_vues_v7.py",
          "test_lentilles_sondes_bbis_montage_v7.py": "test_lentilles_sondes_bbis_montage_v8.py",
          "test_lentilles_sondes_bbis_procedure_v7.py": "test_lentilles_sondes_bbis_procedure_v8.py",
          "test_lentilles_sondes_bbis_lanceur_v7_v1.py": "test_lentilles_sondes_bbis_lanceur_v8_v1.py",
          "test_lentilles_sondes_bbis_lanceur_v7_interruptions_v1.py": "test_lentilles_sondes_bbis_lanceur_v8_interruptions_v1.py",
          "test_lentilles_sondes_bbis_lanceur_v7_garde_arret_present_v1.py": "test_lentilles_sondes_bbis_lanceur_v8_garde_arret_present_v1.py"}


def test_l_outil_de_fabrique_rejoue_rend_le_lanceur_de_la_version_8_a_l_octet_pres(tmp_path):
    paquet, essais = tmp_path / "paquet", tmp_path / "essais"
    paquet.mkdir()
    essais.mkdir()
    (paquet / "lanceur_v7.py").write_bytes((PAQUET / "lanceur_v7.py").read_bytes())
    for origine in COPIES:
        (essais / origine).write_bytes((ESSAIS / origine).read_bytes())
    r = subprocess.run([sys.executable, "-B", str(OUTIL), str(paquet), str(essais)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert (paquet / "lanceur_v8.py").read_bytes() == (PAQUET / "lanceur_v8.py").read_bytes()
    for copie in COPIES.values():
        assert (essais / copie).read_bytes() == (ESSAIS / copie).read_bytes(), copie
    importent = {p.name for p in ESSAIS.glob("*lentilles_sondes_bbis_*.py")
                 if any(ligne.split("#")[0].rstrip().endswith("import lanceur_v7 as la")
                        for ligne in p.read_text(encoding="utf-8").splitlines())}
    assert importent == set(COPIES)


def test_lignes_de_la_version_7_toutes_gardees_hors_la_liste_des_modules_et_l_appel():
    """De `lanceur_v7` à `lanceur_v8` : deux lignes retirées seulement (la ligne des modules ; l'appel à
    `montage_v1.cibles_corpus`). Lignes ajoutées hors de l'en-tête : l'import du module neuf, la ligne des modules, l'appel à
    `corpus_pagine_v1.cibles_corpus`. Aucune autre ligne ne change."""
    v7 = (PAQUET / "lanceur_v7.py").read_text(encoding="utf-8").splitlines()
    v8 = (PAQUET / "lanceur_v8.py").read_text(encoding="utf-8").splitlines()
    diff = list(difflib.ndiff(v7, v8))
    assert [l[2:] for l in diff if l.startswith("- ")] == [
        '           "statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v7")',
        '    rapport["essais_un_octet"] += mo.essais_un_octet(transport, cle, mo.cibles_corpus(voisin, transport))']
    ajoutees = [l[2:] for l in diff if l.startswith("+ ")]
    assert [l for l in ajoutees[ajoutees.index("from . import corpus_pagine_v1 as cp"):]] == [
        "from . import corpus_pagine_v1 as cp",
        '           "statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "corpus_pagine_v1", "lanceur_v8")',
        '    rapport["essais_un_octet"] += mo.essais_un_octet(transport, cle, cp.cibles_corpus(voisin, transport))']
    en_tete = ajoutees[:ajoutees.index("from . import corpus_pagine_v1 as cp")]
    assert len(en_tete) == 7 and en_tete[0] == "" and en_tete[1].startswith("Version 8 : correctif de la pagination")
    assert v8.index('"""', 1) == v7.index('"""', 1) + 7                                         # les sept lignes sont dans la docstring
    assert not any("mo.cibles_corpus" in l for l in v8) and sum("cp.cibles_corpus" in l for l in v8) == 1
