"""[v6 : lecteurs admis de la clé de la référence cachée, complétés de trois fonctions examinées. Les essais v3, v4 et v5
et leurs listes restent tels quels (scellés, R12). Auteur : Claude Opus 5.5, développeur neuf, pièce de classe B, à
contre-lire par un autre modèle. Rapport : `docs/notes/reparation-inventaire-cibles-et-sceaux-v1/rapport-v1.md`.]

Cibles invisibles (N-060 v3) : aucun module hors des mesures et de l'extraction ne lit la référence cachée d'une tâche.
L'essai du v3 (`test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`) relève toute fonction qui porte la constante
`cibles` ou `couts_rapportes`. Trois fonctions entrées sur `main` après la liste v5 la portent sans lire la référence :

- `barreau8_moniteurs/passe_recalcul_v6.py::_table_en_specification` : homonyme, `cibles` y est le champ de forme des
  projections visées par l'adaptateur ;
- `t08/rendu_juges_v1.py::exiger_tache_projetee` : la nomme pour la refuser (garde exigée par le texte scellé de T0.8) ;
- `t08/fabrique_jouet_v1.py::taches_factices` : l'écrit dans des tâches jouets, pour éprouver ce refus.

Ce fichier porte : la liste v6 scellée, qui reprend la v5 intacte ; ses ajouts sourcés, textes et fichiers à leur
empreinte, objets git égaux au commit nommé ; l'essai du v3 joué sous la liste complétée ; la mutation (chaque fonction
ajoutée est nécessaire) ; une preuve par l'arbre syntaxique par catégorie, chacune éprouvée sur des artefacts (R5).
"""
from __future__ import annotations

import ast
import hashlib
import json
import subprocess
import textwrap
from pathlib import Path

import pytest

import test_cibles_invisibles_v3 as v3
import test_cibles_invisibles_v5 as v5
from controle_ia.gardes import GardeArret

LISTE = Path(__file__).with_name("liste_cibles_invisibles_v6.json")
LISTE_V5 = Path(__file__).with_name("liste_cibles_invisibles_v5.json")
EMPREINTE_V5 = "37bcbb01372114d373ab2ec3be011f211aeb96c2fa038aa39f2eb4a136234081"
RACINE = Path(__file__).resolve().parents[1]
PASSE = "controle_ia/barreau8_moniteurs/passe_recalcul_v6.py"
RENDU = "controle_ia/t08/rendu_juges_v1.py"
FABRIQUE = "controle_ia/t08/fabrique_jouet_v1.py"
CATEGORIES = {"homonyme de l'adaptateur": PASSE, "nommée pour refuser": RENDU, "fabrique jouet": FABRIQUE}


def lire_liste(chemin: Path = LISTE) -> dict:
    return json.loads(chemin.read_text(encoding="utf-8"))


def lecteurs_admis(liste: dict) -> dict:
    admis = v5.lecteurs_admis(v5.lire_liste(LISTE_V5))
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        admis[rel] = admis.get(rel, set()) | set(e["fonctions"])
    return admis


@pytest.fixture(scope="module")
def liste() -> dict:
    return lire_liste()


# --- La liste ---------------------------------------------------------------------------------------------------------

def test_liste_scellee_par_son_compagnon():
    attendu = LISTE.with_name(LISTE.name + ".sha256").read_text(encoding="utf-8").split()[0]
    assert hashlib.sha256(LISTE.read_bytes()).hexdigest() == attendu


def test_la_v5_est_intacte_et_nommee(liste):
    empreinte = hashlib.sha256(LISTE_V5.read_bytes()).hexdigest()
    compagnon = LISTE_V5.with_name(LISTE_V5.name + ".sha256").read_text(encoding="utf-8").split()[0]
    assert empreinte == compagnon == EMPREINTE_V5 == liste["liste_precedente"]["sha256"]
    assert liste["liste_precedente"]["chemin"] == "tests/" + LISTE_V5.name


def test_les_ajouts_sont_neufs_sources_et_bien_formes(liste):
    ajouts = liste["lecteurs_de_cibles_ajoutes"]
    precedents = v5.lecteurs_admis(v5.lire_liste(LISTE_V5))
    assert {e["categorie"]: rel for rel, e in ajouts.items()} == CATEGORIES
    for rel, e in ajouts.items():
        assert e["fonctions"] and not set(e["fonctions"]) & precedents.get(rel, set()), rel
        assert e["raison"].strip() and e["source"].strip() and e["textes"], rel
        assert len(e["commit"]) == 40 and len(e["sha256"]) == 64, rel
        for chemin, sha in e["textes"].items():
            assert hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest() == sha, (rel, chemin)
            assert sha[:8] in e["source"], (rel, chemin)


def test_les_fichiers_examines_n_ont_pas_change(liste):
    """Une raison d'admission vaut pour le fichier lu : s'il change (R12 l'interdit), il se réexamine."""
    changes = [rel for rel, e in liste["lecteurs_de_cibles_ajoutes"].items()
               if hashlib.sha256((v3.SRC / rel).read_bytes()).hexdigest() != e["sha256"]]
    assert not changes, f"fichier(s) modifié(s) depuis l'examen de la liste v6 : {changes}"


def _git(*args: str) -> tuple[int, str]:
    try:
        r = subprocess.run(["git", "-C", str(RACINE), *args], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return 1, ""
    return r.returncode, r.stdout.strip()


def test_les_objets_git_sont_ceux_du_commit_nomme(liste):
    code, haut = _git("rev-parse", "--show-toplevel")
    if code or Path(haut).resolve() != RACINE:
        pytest.skip("hors du dépôt git : égalité des objets non vérifiable ici")
    absents, differents = [], []
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        code, attendu = _git("rev-parse", "--verify", "--quiet", f"{e['commit']}:src/{rel}")
        if code or not attendu:
            absents.append(rel)
            continue
        if _git("hash-object", "--", f"src/{rel}")[1] != attendu:
            differents.append(rel)
    assert not differents, f"objet git différent de celui du commit nommé : {differents}"
    if absents:
        pytest.skip(f"commit nommé absent de l'historique local (tronqué) pour : {absents}")


# --- L'essai du v3, joué sous la liste complétée, et la mutation --------------------------------------------------------

def test_aucun_module_hors_mesures_ne_lit_la_cle_cibles(liste, monkeypatch):
    monkeypatch.setattr(v3, "LECTEURS_DE_CIBLES_ADMIS", lecteurs_admis(liste))
    v3.test_aucun_module_hors_mesures_ne_lit_la_cle_cibles()


def test_chaque_fonction_ajoutee_est_necessaire(liste):
    """Mutation : retirer une fonction ajoutée la rend exactement hors liste ; la liste complète n'en laisse aucune."""
    assert v5.lecteurs_hors_liste(lecteurs_admis(liste)) == {}
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        for nom in e["fonctions"]:
            admis = lecteurs_admis(liste)
            admis[rel] = admis[rel] - {nom}
            assert v5.lecteurs_hors_liste(admis) == {rel: [nom]}


def test_garde_du_v3_voit_toujours_un_lecteur_plante(liste, tmp_path, monkeypatch):
    """Artefact (R5) : sous la liste complétée, un module planté qui lit `tache["cibles"]` reste vu par l'essai du v3."""
    paquet = tmp_path / "controle_ia" / "plante"
    paquet.mkdir(parents=True)
    (paquet / "lecteur.py").write_text("def lire(tache):\n    return tache['cibles']\n", encoding="utf-8")
    monkeypatch.setattr(v3, "SRC", tmp_path)
    monkeypatch.setattr(v3, "LECTEURS_DE_CIBLES_ADMIS", lecteurs_admis(liste))
    with pytest.raises(AssertionError, match="plante/lecteur.py"):
        v3.test_aucun_module_hors_mesures_ne_lit_la_cle_cibles()


# --- Preuves par l'arbre syntaxique, une par catégorie, chacune éprouvée sur des artefacts (R5) -------------------------

def _constantes_cachees(n: ast.AST) -> list[ast.Constant]:
    return [m for m in ast.walk(n) if isinstance(m, ast.Constant) and m.value in v3.CLES_CACHEES]


def _parents(n: ast.AST) -> dict:
    return {id(e): p for p in ast.walk(n) for e in ast.iter_child_nodes(p)}


def _lit_une_cle_cachee(n: ast.AST) -> bool:
    """Lecture d'une clé cachée : `x["cibles"]` en lecture, `.get("cibles")`, `.pop("cibles")`, `getattr(x, "cibles")`."""
    for m in ast.walk(n):
        if (isinstance(m, ast.Subscript) and isinstance(m.slice, ast.Constant) and m.slice.value in v3.CLES_CACHEES
                and isinstance(m.ctx, ast.Load)):
            return True
        if isinstance(m, ast.Call) and any(isinstance(a, ast.Constant) and a.value in v3.CLES_CACHEES for a in m.args):
            nom = m.func.attr if isinstance(m.func, ast.Attribute) else getattr(m.func, "id", None)
            if nom in ("get", "pop", "getattr", "setdefault", "__getitem__"):
                return True
    return False


def preuve_homonyme_adaptateur(f: ast.AST) -> bool:
    """Chaque constante cachée est une clé de dictionnaire littéral dont la valeur est
    `tuple(<nom>["adaptateurs"]["projections"])` ; aucune lecture d'une clé cachée."""
    if _lit_une_cle_cachee(f):
        return False
    parents, consts = _parents(f), _constantes_cachees(f)
    for c in consts:
        d = parents.get(id(c))
        if not isinstance(d, ast.Dict) or not any(k is c for k in d.keys):
            return False
        v = d.values[[i for i, k in enumerate(d.keys) if k is c][0]]
        if not (isinstance(v, ast.Call) and getattr(v.func, "id", None) == "tuple" and len(v.args) == 1):
            return False
        a = v.args[0]
        if not (isinstance(a, ast.Subscript) and isinstance(a.slice, ast.Constant) and a.slice.value == "projections"
                and isinstance(a.value, ast.Subscript) and isinstance(a.value.slice, ast.Constant)
                and a.value.slice.value == "adaptateurs" and isinstance(a.value.value, ast.Name)):
            return False
    return bool(consts)


def preuve_nommee_pour_refuser(f: ast.AST) -> bool:
    """Chaque constante cachée est le membre gauche d'un test `in` d'un `if` dont le seul corps est un `raise` ; aucune
    lecture d'une clé cachée ; la fonction ne rend rien (aucun `return` porteur de valeur)."""
    if _lit_une_cle_cachee(f) or any(isinstance(m, ast.Return) and m.value is not None for m in ast.walk(f)):
        return False
    parents, consts = _parents(f), _constantes_cachees(f)
    for c in consts:
        cmp = parents.get(id(c))
        if not (isinstance(cmp, ast.Compare) and cmp.left is c and len(cmp.ops) == 1 and isinstance(cmp.ops[0], ast.In)):
            return False
        si = parents.get(id(cmp))
        if not (isinstance(si, ast.If) and si.test is cmp and len(si.body) == 1 and isinstance(si.body[0], ast.Raise)
                and not si.orelse):
            return False
    return bool(consts)


NOMS_DES_VALEURS_FACTICES = {"rng", "mots", "float", "int", "len", "MOTS"}
LECTURES_DE_FICHIER = {"open", "read_text", "read_bytes", "load", "loads"}


def preuve_fabrique_jouet(f: ast.AST) -> bool:
    """Chaque constante cachée est une clé de dictionnaire littéral dont la valeur n'est faite que du générateur, des
    mots fixes et de littéraux ; aucune lecture d'une clé cachée ; aucune lecture de fichier dans la fonction."""
    if _lit_une_cle_cachee(f):
        return False
    for m in ast.walk(f):
        if isinstance(m, ast.Call):
            nom = m.func.attr if isinstance(m.func, ast.Attribute) else getattr(m.func, "id", None)
            if nom in LECTURES_DE_FICHIER:
                return False
    parents, consts = _parents(f), _constantes_cachees(f)
    for c in consts:
        d = parents.get(id(c))
        if not isinstance(d, ast.Dict) or not any(k is c for k in d.keys):
            return False
        v = d.values[[i for i, k in enumerate(d.keys) if k is c][0]]
        noms = {m.id for m in ast.walk(v) if isinstance(m, ast.Name)}
        if not noms <= NOMS_DES_VALEURS_FACTICES:
            return False
    return bool(consts)


PREUVES = {"homonyme de l'adaptateur": preuve_homonyme_adaptateur, "nommée pour refuser": preuve_nommee_pour_refuser,
           "fabrique jouet": preuve_fabrique_jouet}


def _fonction_de_texte(source: str) -> ast.AST:
    return ast.parse(textwrap.dedent(source)).body[0]


def test_chaque_ajout_tient_sa_preuve(liste):
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        fonctions = dict(v3._fonctions(v3.SRC / rel))
        for nom in e["fonctions"]:
            assert PREUVES[e["categorie"]](fonctions[nom]), (rel, nom)


ARTEFACTS = {
    "homonyme de l'adaptateur": [
        "def f(c):\n    return {'cibles': tuple(c['cibles'])}\n",
        "def f(c, t):\n    return {'cibles': tuple(t['cibles']['controls'])}\n",
        "def f(c):\n    x = c['cibles']\n    return {'cibles': tuple(c['adaptateurs']['projections'])}\n",
        "def f(c):\n    return {'n': c.get('cibles')}\n",
    ],
    "nommée pour refuser": [
        "def f(t):\n    return t['cibles']\n",
        "def f(t):\n    if 'cibles' in t:\n        pass\n",
        "def f(t):\n    if 'cibles' in t:\n        return t\n",
        "def f(t):\n    if 'cibles' in t:\n        raise ValueError()\n    return t.get('cibles')\n",
        "def f(t):\n    if 'cibles' not in t:\n        raise ValueError()\n",
    ],
    "fabrique jouet": [
        "def f(racine, rng):\n    import json\n    v = json.loads((racine / 'x.json').read_text())\n"
        "    return {'cibles': v}\n",
        "def f(racine, rng, vraie):\n    return {'cibles': vraie}\n",
        "def f(racine, rng, t):\n    return {'cibles': t['cibles']}\n",
        "def f(racine, rng):\n    with open(racine) as h:\n        pass\n    return {'cibles': {'compute': 1.0}}\n",
    ],
}
SAINS = {
    "homonyme de l'adaptateur": "def f(c):\n    return {'cibles': tuple(c['adaptateurs']['projections'])}\n",
    "nommée pour refuser": "def f(t):\n    if 'cibles' in t:\n        raise ValueError('refusé')\n",
    "fabrique jouet": "def f(racine, rng):\n    mots = ['a']\n    return {'cibles': {'compute': float(rng.integers(1, 2)), "
                      "'controls': [mots[0]]}}\n",
}


@pytest.mark.parametrize("categorie", sorted(PREUVES))
def test_chaque_preuve_refuse_ses_artefacts_et_admet_le_cas_sain(categorie):
    assert PREUVES[categorie](_fonction_de_texte(SAINS[categorie]))
    for source in ARTEFACTS[categorie]:
        assert not PREUVES[categorie](_fonction_de_texte(source)), source


def test_la_garde_du_rendu_refuse_cibles_et_admet_une_tache_projetee():
    """Comportement de la fonction admise « nommée pour refuser » : refus d'un objet portant `cibles` ; cas sain admis."""
    from controle_ia.t08 import rendu_juges_v1 as rj

    rj.exiger_tache_projetee({"identifiant": "t", "questions": "q"})
    with pytest.raises(GardeArret, match="cibles"):
        rj.exiger_tache_projetee({"identifiant": "t", "questions": "q", "cibles": {"compute": 1.0}})
