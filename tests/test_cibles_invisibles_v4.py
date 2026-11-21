"""[v4 : erratum 1 de la liste figée de tests/test_cibles_invisibles_v3.py (mot de Lazar, GO-2026-11-21-69 : « Inventaire
figé des cibles invisibles complété par un erratum, contre-lu par Opus »). Le v3 reste tel quel et échoue sur main : il
n'est ni modifié ni copié. Cet essai le relit avec la liste complétée, écrite dans un fichier à part,
`tests/liste_cibles_invisibles_v4.json` : la liste du v3 reprise sans changement, plus quarante constructeurs d'invite et
deux faux lecteurs de la clé `cibles`, chacun avec sa raison et sa source. Note : `docs/notes/papier-dopamine-moniteur-v1/
erratum-1-liste-cibles-invisibles-v3.md`.]

Cibles invisibles (N-060 v3) : ni l'agent ni les moniteurs ne voient jamais la référence cachée d'une tâche (`cibles`,
et les coûts rapportés de l'article). Les essais à marqueur du v3 (six collecteurs) ne sont pas rejoués ici : ils passent
dans le v3. Ce fichier porte :

1. la liste : scellée, égale au v3 pour ce qu'elle reprend, ajouts neufs, sourcés et bien formés, fichiers examinés
   inchangés depuis l'examen (une empreinte par fichier : un fichier qui change se réexamine) ;
2. les quatre essais d'inventaire du v3 et sa garde à module planté, joués tels quels sous la liste complétée ;
3. la mutation : chaque ligne ajoutée est nécessaire (la retirer fait échouer l'inventaire) ;
4. deux collecteurs à marqueur de plus, sur des chemins réels neufs (début d'épisode de la passe de recalcul du barreau 8 ;
   tirage du saboteur instruit de la formation des familles du barreau 5), avec leur fuite plantée (R5) ;
5. les preuves par l'arbre syntaxique des raisons d'exemption, chacune éprouvée sur un artefact (R5) : tout environnement
   des modules ajoutés est bâti sur `tache_de(...)` ; les lectures de `cibles` ajoutées sont celles de la configuration
   de l'adaptateur ; les clés « role » exemptées ne sont pas des messages de dialogue ; les textes de contrôle sont fixes ;
   les rendus ne lisent que des environnements reçus ; le bras du papier dopamine n'importe aucune tâche du banc.
"""
from __future__ import annotations

import ast
import hashlib
import importlib
import json
import re
from pathlib import Path

import pytest

import test_cibles_invisibles_v3 as v3
from controle_ia.environnements.invites import charger_invite
from controle_ia.manifeste import graines

LISTE = Path(__file__).with_name("liste_cibles_invisibles_v4.json")
ACCORD = "GO-2026-11-21-69"
DONNEE = "ligne de données"
GABARIT = "rendu générique d'un gabarit de dialogue"
TACHE_DE = "environnement sur tache_de"
RENDU = "rendu d'un environnement reçu"
FIXE = "texte fixe sans tâche"
CATEGORIES = {DONNEE, GABARIT, TACHE_DE, RENDU, FIXE}
PAQUET_DOPAMINE = "controle_ia/dopamine_exploratoire/"
IMPORTS_ADMIS_DOPAMINE = {"gardes", "scellement", "manifeste", "dopamine_exploratoire"}


# --- La liste ---------------------------------------------------------------------------------------------------------

def lire_liste(chemin: Path = LISTE) -> dict:
    return json.loads(chemin.read_text(encoding="utf-8"))


def registre(liste: dict) -> dict:
    """Registre complété, à la forme du v3 : clé -> (statut, raison)."""
    return {**{k: tuple(v) for k, v in liste["registre_repris_de_v3"].items()},
            **{k: (e["statut"], e["raison"]) for k, e in liste["registre_ajoute"].items()}}


def lecteurs_admis(liste: dict) -> dict:
    admis = {k: set(v) for k, v in liste["lecteurs_de_cibles_repris_de_v3"].items()}
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        admis[rel] = admis.get(rel, set()) | set(e["fonctions"])
    return admis


def lecteurs_hors_liste(admis: dict) -> dict:
    """Fonctions qui portent une clé cachée en constante et que la liste n'admet pas (même balayage que le v3)."""
    hors = {}
    for rel, f in v3._modules():
        for nom, n in v3._fonctions(f):
            if (any(isinstance(m, ast.Constant) and m.value in v3.CLES_CACHEES for m in ast.walk(n))
                    and nom not in admis.get(rel, set())):
                hors.setdefault(rel, []).append(nom)
    return {rel: sorted(noms) for rel, noms in hors.items()}


def _source(rel: str) -> str:
    return (v3.SRC / rel).read_text(encoding="utf-8")


def _fonction(rel: str, nom: str) -> ast.AST:
    return dict(v3._fonctions(v3.SRC / rel))[nom]


def _entrees(liste: dict, categorie: str) -> list[tuple[str, str]]:
    return sorted(tuple(k.split("::")) for k, e in liste["registre_ajoute"].items() if e["categorie"] == categorie)


@pytest.fixture(scope="module")
def liste() -> dict:
    return lire_liste()


@pytest.fixture(scope="module")
def trouves() -> dict:
    return v3._constructeurs()


def test_liste_scellee_par_son_compagnon():
    """R6 : l'empreinte compagnon de la liste est celle du fichier lu."""
    attendu = LISTE.with_name(LISTE.name + ".sha256").read_text(encoding="utf-8").split()[0]
    assert hashlib.sha256(LISTE.read_bytes()).hexdigest() == attendu


def test_la_liste_reprend_le_v3_sans_rien_changer(liste):
    """Un erratum ajoute : rien de la liste du v3 n'est retiré ni réécrit."""
    assert {k: tuple(v) for k, v in liste["registre_repris_de_v3"].items()} == v3.REGISTRE
    assert {k: set(v) for k, v in liste["lecteurs_de_cibles_repris_de_v3"].items()} == v3.LECTEURS_DE_CIBLES_ADMIS
    assert liste["base"]["essai"] == "tests/test_cibles_invisibles_v3.py" and ACCORD in liste["accord"]


def test_les_ajouts_sont_neufs_sources_et_bien_formes(liste):
    ajouts, sources = liste["registre_ajoute"], liste["sources"]
    assert ajouts and not set(ajouts) & set(liste["registre_repris_de_v3"])
    for cle, e in ajouts.items():
        rel = cle.split("::")[0]
        assert e["statut"] in (v3.COUVERT, v3.EXEMPT) and e["categorie"] in CATEGORIES and e["raison"].strip(), cle
        assert rel in sources and e["source"].strip() and e["source"] == sources[rel]["source"], cle
        assert (e["statut"] == v3.COUVERT) == ("collecteur" in e), cle
        if e["statut"] == v3.COUVERT:
            assert e["collecteur"] in COLLECTEURS_V4 and e["raison"].startswith(e["collecteur"]), cle
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        assert rel in sources and e["fonctions"] and e["raison"].strip() and e["source"] == sources[rel]["source"], rel
        assert not set(e["fonctions"]) & v3.LECTEURS_DE_CIBLES_ADMIS.get(rel, set()), rel
    for rel, s in sources.items():
        assert re.fullmatch(r"[0-9a-f]{40}", s["commit"]) and re.fullmatch(r"[0-9a-f]{64}", s["sha256"]), rel
        assert s["source"].strip() and s["ce_que_c_est"].strip() and s["verification"].strip(), rel
        assert any(k.startswith(rel + "::") for k in ajouts), f"source sans ligne : {rel}"


def test_les_fichiers_examines_n_ont_pas_change(liste):
    """Une raison d'exemption vaut pour le fichier lu : s'il change (R12 l'interdit), il se réexamine."""
    changes = [rel for rel, s in liste["sources"].items()
               if hashlib.sha256((v3.SRC / rel).read_bytes()).hexdigest() != s["sha256"]]
    assert not changes, f"fichier(s) modifié(s) depuis l'examen de l'erratum : {changes}"


# --- Les essais d'inventaire du v3, joués sous la liste complétée -----------------------------------------------------

@pytest.fixture
def sous_la_liste_completee(liste, monkeypatch):
    monkeypatch.setattr(v3, "REGISTRE", registre(liste))
    monkeypatch.setattr(v3, "LECTEURS_DE_CIBLES_ADMIS", lecteurs_admis(liste))


def test_inventaire_tout_constructeur_d_invite_est_examine(sous_la_liste_completee):
    v3.test_inventaire_tout_constructeur_d_invite_est_examine()


def test_inventaire_registre_a_jour(sous_la_liste_completee):
    v3.test_inventaire_registre_a_jour()


def test_base_h12_absente_du_code_ou_couverte(sous_la_liste_completee):
    v3.test_base_h12_absente_du_code_ou_couverte()


def test_aucun_module_hors_mesures_ne_lit_la_cle_cibles(sous_la_liste_completee):
    v3.test_aucun_module_hors_mesures_ne_lit_la_cle_cibles()


def test_garde_de_l_inventaire_voit_un_constructeur_et_un_lecteur_plantes(sous_la_liste_completee, tmp_path,
                                                                          monkeypatch):
    """Artefact (R5), sous la liste complétée : la garde du v3, appelée telle quelle, voit toujours le module planté
    (constructeur non examiné et lecteur hors liste). Elle remplace `SRC` dans les globales du module v3, rendues à la
    fin de l'essai."""
    v3.test_garde_de_l_inventaire_voit_un_constructeur_et_un_lecteur_plantes(tmp_path, monkeypatch)
    assert v3.SRC == tmp_path


def test_chaque_ligne_ajoutee_est_necessaire(liste, trouves, monkeypatch):
    """Mutation : retirer une ligne ajoutée, quelle qu'elle soit, laisse exactement cette fonction non examinée ; la
    retirer d'un lecteur ajouté la rend hors liste. Aucune ligne de trop, aucune ligne qui en cache une autre."""
    complet = registre(liste)
    assert set(trouves) == set(complet)
    for cle in liste["registre_ajoute"]:
        assert set(trouves) - (set(complet) - {cle}) == {cle}
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        for nom in e["fonctions"]:
            admis = lecteurs_admis(liste)
            admis[rel] = admis[rel] - {nom}
            assert lecteurs_hors_liste(admis) == {rel: [nom]}
    assert lecteurs_hors_liste(lecteurs_admis(liste)) == {}
    # la même mutation, par l'essai du v3 lui-même, sur la première et la dernière ligne ajoutées
    for cle in (min(liste["registre_ajoute"]), max(liste["registre_ajoute"])):
        mute = {k: v for k, v in complet.items() if k != cle}
        monkeypatch.setattr(v3, "REGISTRE", mute)
        with pytest.raises(AssertionError, match="non examiné"):
            v3.test_inventaire_tout_constructeur_d_invite_est_examine()


# --- Deux collecteurs à marqueur de plus ------------------------------------------------------------------------------

def collecter_passe_recalcul_debut(tache: dict) -> list[str]:
    """`barreau8_moniteurs.passe_recalcul_v5.debut_d_episode` : consigne et première observation de l'épisode d'une
    tâche, telles que la passe les rend pour lire le gabarit."""
    from types import SimpleNamespace
    passe = importlib.import_module("controle_ia.barreau8_moniteurs.passe_recalcul_v5")
    spec = SimpleNamespace(pas_par_episode=len(v3.ACTIONS), invite="H1-classification")
    return list(passe.debut_d_episode(spec, tache))


def collecter_formation_tirage_saboteur(tache: dict) -> list[str]:
    """`barreau5_familles.formation_v1.tirer_famille` : environnements du saboteur instruit bâtis depuis le
    dictionnaire de tâche entier (cibles comprises), interceptés à l'entrée du générateur par le crochet `jouer`."""
    formation = importlib.import_module("controle_ia.barreau5_familles.formation_v1")
    envs, k = [], 2

    def capture(fmt, environnements, identifiants, T, graines_du_lot):
        envs.extend(environnements)
        raise v3._Capture

    cles = [f"b5f/famille/fam/distillation/tache/{tache['identifiant']}/e{j}" for j in range(k)]
    config = {"T": len(v3.ACTIONS), "lot": 8, "episodes_par_tache_distillation": k}
    with pytest.raises(v3._Capture):
        formation.tirer_famille(None, None, "fam", [tache], config, v3.CONSIGNES_P3,
                                charger_invite("H1-classification"), graines(cles, 12345), 0, jouer=capture)
    assert len(envs) == k and all(e.instructions_cachees for e in envs)      # la consigne privée du saboteur y est
    return [x for e in envs for x in v3._invites_d_environnement(e)]


COLLECTEURS_V4 = {"passe_recalcul_debut": collecter_passe_recalcul_debut,
                  "formation_tirage_saboteur": collecter_formation_tirage_saboteur}


@pytest.mark.parametrize("nom", sorted(COLLECTEURS_V4))
def test_aucune_invite_ne_porte_les_cibles(nom):
    invites = COLLECTEURS_V4[nom](v3.tache_factice())
    assert invites and all(isinstance(x, str) and x.strip() for x in invites)
    fuites = [k for k, x in enumerate(invites) if v3._fuit(x)]
    assert not fuites, f"{nom} : la référence cachée apparaît dans {len(fuites)} invite(s) (n° {fuites[:5]})"


@pytest.mark.parametrize("nom", sorted(COLLECTEURS_V4))
def test_garde_la_collecte_voit_une_fuite_plantee(nom):
    """Artefact (R5) : l'énoncé recopie les cibles ; la collecte doit trouver le marqueur dans ce chemin."""
    invites = COLLECTEURS_V4[nom](v3.tache_factice(fuite=True))
    assert any(v3._fuit(x) for x in invites), f"{nom} : fuite plantée non vue : la collecte ne voit pas les invites"


def test_tout_collecteur_neuf_couvre_une_ligne(liste):
    couverts = {e["collecteur"] for e in liste["registre_ajoute"].values() if e["statut"] == v3.COUVERT}
    assert couverts == set(COLLECTEURS_V4)


# --- Preuves par l'arbre syntaxique des raisons d'exemption -----------------------------------------------------------

def _nom_d_appel(appel: ast.Call):
    return appel.func.attr if isinstance(appel.func, ast.Attribute) else getattr(appel.func, "id", None)


def _racine(noeud: ast.AST):
    """Nom à la racine d'une expression (`envs[b].x` -> `envs`, `*debut` -> `debut`), ou None."""
    while isinstance(noeud, (ast.Subscript, ast.Attribute, ast.Starred)):
        noeud = noeud.value
    return noeud.id if isinstance(noeud, ast.Name) else None


def _parametres(f: ast.AST) -> set[str]:
    a = f.args
    return {x.arg for x in a.posonlyargs + a.args + a.kwonlyargs}


def appels_d_environnement(source: str) -> tuple[int, list[int]]:
    """(nombre d'appels à `premier_test_ia.conditions.environnement`, sous le nom que le module lui donne ; lignes
    fautives). Fautif : un appel dont la tâche, deuxième argument, n'est pas écrite `tache_de(...)`, `tache_de` étant
    celle de `environnements.pilote_a`, importée sans autre nom et jamais redéfinie ; ou une construction directe de
    `EnvironnementPropositions`, que cette preuve ne suit pas."""
    arbre = ast.parse(source)
    noms, importee = set(), False
    for n in ast.walk(arbre):
        if isinstance(n, ast.ImportFrom) and n.module:
            for a in n.names:
                if n.module.endswith("premier_test_ia.conditions") and a.name == "environnement":
                    noms.add(a.asname or a.name)
                if n.module.endswith("environnements.pilote_a") and a.name == "tache_de" and a.asname is None:
                    importee = True
    redefinie = any((isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.name == "tache_de")
                    or (isinstance(n, ast.Name) and n.id == "tache_de" and isinstance(n.ctx, ast.Store))
                    or (isinstance(n, ast.arg) and n.arg == "tache_de")
                    or (isinstance(n, ast.alias) and (n.asname == "tache_de"))
                    for n in ast.walk(arbre))
    total, fautifs = 0, []
    for n in ast.walk(arbre):
        if not isinstance(n, ast.Call):
            continue
        if _nom_d_appel(n) == "EnvironnementPropositions":
            fautifs.append(n.lineno)
        elif ((isinstance(n.func, ast.Name) and n.func.id in noms)
              or (isinstance(n.func, ast.Attribute) and n.func.attr == "environnement")):
            total += 1
            tache = n.args[1] if len(n.args) > 1 else None
            if not (importee and not redefinie and isinstance(tache, ast.Call) and isinstance(tache.func, ast.Name)
                    and tache.func.id == "tache_de"):
                fautifs.append(n.lineno)
    return total, fautifs


SAIN_ENV = ("from ..environnements.pilote_a import tache_de\nfrom ..premier_test_ia.conditions import environnement\n"
            "def f(t, T, g):\n    return environnement('honnete', tache_de(t), T, g, {})\n")


def test_tout_environnement_des_modules_ajoutes_passe_par_tache_de(liste, trouves):
    """Raison « environnement sur tache_de » : dans chaque module concerné, tout environnement est bâti par
    `conditions.environnement` (couvert par le v3, agent_p3) sur `tache_de(...)`, qui ne transmet qu'identifiant,
    questions et classification (v3, `test_la_tache_de_l_agent_n_a_aucun_champ_pour_les_cibles`)."""
    modules = sorted({rel for rel, _ in _entrees(liste, TACHE_DE)})
    assert len(modules) == 4
    for rel in modules:
        total, fautifs = appels_d_environnement(_source(rel))
        assert total >= 1 and not fautifs, (rel, total, fautifs)
    # aucune fonction ajoutée, d'aucune catégorie, n'appelle `environnement` hors de ces modules
    for cle in liste["registre_ajoute"]:
        if trouves[cle] & {"environnement", "EnvironnementPropositions"}:
            assert cle.split("::")[0] in modules and liste["registre_ajoute"][cle]["categorie"] == TACHE_DE, cle


@pytest.mark.parametrize("plante", [
    SAIN_ENV.replace("tache_de(t), T", "t, T"),
    SAIN_ENV.replace("tache_de(t), T", "dict(t), T"),
    SAIN_ENV.replace("'honnete', tache_de(t), T, g, {}", "'honnete', tache=t, T=T, guide=g, consignes={}"),
    SAIN_ENV + "def tache_de(t):\n    return t\n",
    SAIN_ENV.replace("import tache_de\n", "import tache_de\nfrom ..environnements.pilote_a import identite as tache_de\n"),
    SAIN_ENV.replace("from ..environnements.pilote_a import tache_de\n", "tache_de = lambda t: t\n"),
    SAIN_ENV + "def g(pr, t):\n    return pr.EnvironnementPropositions(t, 1, 4)\n",
    SAIN_ENV + "def g(conditions, t, T, g):\n    return conditions.environnement('honnete', t, T, g, {})\n",
    SAIN_ENV.replace("import environnement\n", "import environnement as env_de\n").replace(
        "environnement('honnete', tache_de(t)", "env_de('honnete', t"),
])
def test_garde_la_preuve_voit_un_environnement_sur_la_tache_entiere(plante):
    """Artefact (R5) : tâche passée entière, `tache_de` redéfinie ou construction directe ; cas sain à côté."""
    assert appels_d_environnement(SAIN_ENV) == (1, [])
    assert appels_d_environnement(plante)[1]


def lectures_de_cibles(source: str) -> list[tuple[str, int, bool]]:
    """(fonction, ligne, admise) de chaque constante « cibles » ou « couts_rapportes » d'un module ; admise seulement
    si c'est l'indice d'un nom que la même fonction lie à `config["adaptateur"]` (configuration de l'adaptateur LoRA),
    une seule fois et à rien d'autre. Règle de tests/test_t06_cibles_invisibles_v2.py::_lectures_de_cibles, récrite ici
    pour ne rien importer, et durcie : un nom relié ensuite à autre chose n'est plus admis."""
    sortie = []
    for f in [n for n in ast.walk(ast.parse(source)) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]:
        lies = {c.targets[0].id for c in ast.walk(f) if isinstance(c, ast.Assign) and len(c.targets) == 1
                and isinstance(c.targets[0], ast.Name) and isinstance(c.value, ast.Subscript)
                and isinstance(c.value.value, ast.Name) and c.value.value.id == "config"
                and isinstance(c.value.slice, ast.Constant) and c.value.slice.value == "adaptateur"}
        ecrits = [n.id for n in ast.walk(f) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)]
        surs = {x for x in lies if ecrits.count(x) == 1 and x not in _parametres(f)}
        indices = {id(s.slice) for s in ast.walk(f) if isinstance(s, ast.Subscript) and isinstance(s.value, ast.Name)
                   and s.value.id in surs}
        for c in ast.walk(f):
            if isinstance(c, ast.Constant) and c.value in v3.CLES_CACHEES:
                sortie.append((f.name, c.lineno, c.value == "cibles" and id(c) in indices))
    return sortie


def test_les_lecteurs_ajoutes_ne_lisent_que_la_configuration_de_l_adaptateur(liste):
    """Raison « faux lecteur » : dans chaque module ajouté aux lecteurs, la seule lecture de la clé `cibles` est
    `a["cibles"]` avec `a = config["adaptateur"]` dans la même fonction : les modules visés par l'adaptateur."""
    assert len(liste["lecteurs_de_cibles_ajoutes"]) == 2
    for rel, e in liste["lecteurs_de_cibles_ajoutes"].items():
        lectures = lectures_de_cibles(_source(rel))
        assert lectures and all(admise for _, _, admise in lectures), (rel, lectures)
        assert {f for f, _, _ in lectures} == set(e["fonctions"]) and len(lectures) == len(e["fonctions"]), rel


@pytest.mark.parametrize("plante", [
    'def f(config, tache):\n    a = config["adaptateur"]\n    return tache["cibles"]\n',
    'def f(config, taches):\n    a = config["adaptateur"]\n    return a["cibles"], [t["cibles"] for t in taches]\n',
    'def f(config, t):\n    a = t\n    return a["cibles"]\n',
    'def f(config, t):\n    a = config["adaptateur"]\n    a = t\n    return a["cibles"]\n',
    'def f(config, t):\n    a = config["adaptateur"]\n    a, b = t, 1\n    return a["cibles"]\n',
    'def f(config):\n    a = config["adaptateur"]\n    return config["taches"][0]["couts_rapportes"]\n',
])
def test_garde_la_preuve_voit_une_lecture_de_tache_plantee(plante):
    """Artefact (R5) : une lecture qui ne passe pas par la configuration de l'adaptateur, ou par un nom relié ensuite
    à autre chose, n'est pas admise ; cas sain à côté."""
    assert lectures_de_cibles('def f(config):\n    a = config["adaptateur"]\n    return tuple(a["cibles"])\n') == [
        ("f", 3, True)]
    assert not all(admise for _, _, admise in lectures_de_cibles(plante))


def messages_de_dialogue(f: ast.AST) -> list[int]:
    """Lignes des dictionnaires de la fonction qui portent à la fois les clés « role » et « content »."""
    return sorted(d.lineno for d in ast.walk(f) if isinstance(d, ast.Dict)
                  and {"role", "content"} <= {k.value for k in d.keys if isinstance(k, ast.Constant)})


def test_les_cles_role_exemptees_ne_sont_pas_des_messages(liste, trouves):
    """Raison « ligne de données » : la fonction n'est vue par l'inventaire que pour une clé « role », et aucun de ses
    dictionnaires n'est un message de dialogue (« role » avec « content »). Témoin positif pris dans le code réel : le
    gabarit du bras du papier dopamine, lui, bâtit des messages, et le même détecteur les voit."""
    donnees = _entrees(liste, DONNEE)
    assert len(donnees) == 28
    for rel, nom in donnees:
        assert trouves[f"{rel}::{nom}"] == {"{role}"} and not messages_de_dialogue(_fonction(rel, nom)), (rel, nom)
    plante = ast.parse("def f(t):\n    return [{'role': 'user', 'content': str(t)}]\n").body[0]
    assert messages_de_dialogue(plante) == [2]
    (rel, nom), = _entrees(liste, GABARIT)
    assert messages_de_dialogue(_fonction(rel, nom))


def imports_hors_liste_admise(source: str) -> list[str]:
    """Modules de `controle_ia` importés hors de la liste admise pour le bras du papier dopamine."""
    hors = []
    for n in ast.walk(ast.parse(source)):
        if isinstance(n, ast.ImportFrom):
            module = n.module or ""
            if n.level >= 2 or module.startswith("controle_ia"):
                premier = module.removeprefix("controle_ia").lstrip(".").split(".")[0]
                noms = [premier] if premier else [a.name for a in n.names]
                hors += [x for x in noms if x not in IMPORTS_ADMIS_DOPAMINE]
        elif isinstance(n, ast.Import):
            hors += [a.name for a in n.names if a.name.startswith("controle_ia")]
        elif isinstance(n, ast.Call) and _nom_d_appel(n) in ("import_module", "__import__"):
            hors.append(f"import dynamique (l. {n.lineno})")
    return hors


def test_le_bras_dopamine_n_importe_aucune_tache_du_banc(liste):
    """Raison « rendu générique d'un gabarit de dialogue » : `DecoupeurHF.gabarit` ne reçoit que deux textes, et son
    paquet n'importe du programme que les gardes, le scellement et le manifeste : ni les environnements, ni les tâches,
    ni leurs cibles ne peuvent y entrer (aucune clé cachée n'y est lue : essai des lecteurs)."""
    (rel, nom), = _entrees(liste, GABARIT)
    assert rel.startswith(PAQUET_DOPAMINE)
    f = _fonction(rel, nom)
    assert [a.arg for a in f.args.args] == ["self", "systeme", "utilisateur"] and not f.args.vararg and not f.args.kwarg
    for d in (d for d in ast.walk(f) if isinstance(d, ast.Dict)):
        contenu = dict(zip((k.value for k in d.keys), d.values))["content"]
        assert isinstance(contenu, ast.Name) and contenu.id in ("systeme", "utilisateur")
    modules = [(r, p) for r, p in v3._modules() if r.startswith(PAQUET_DOPAMINE)]
    assert len(modules) >= 2
    for r, p in modules:
        assert not imports_hors_liste_admise(p.read_text(encoding="utf-8")), r


@pytest.mark.parametrize("plante", [
    "from ..environnements.pilote_a import charger_taches\n",
    "from .. import environnements\n",
    "from controle_ia.environnements import pilote_a\n",
    "import controle_ia.environnements.pilote_a as p\n",
    "import importlib\nm = importlib.import_module('controle_ia.environnements.pilote_a')\n",
])
def test_garde_la_preuve_voit_un_import_du_banc_plante(plante):
    """Artefact (R5) ; cas sain : les imports réels du paquet."""
    assert not imports_hors_liste_admise("from ..gardes import GardeArret\nfrom . import jouet_v1\nimport numpy as np\n"
                                         "from controle_ia.manifeste import generateur\n")
    assert imports_hors_liste_admise(plante)


def textes_non_fixes(f: ast.AST) -> list[int]:
    """Lignes fautives d'une fonction dite « texte fixe sans tâche » : `conversation_de_controle` ou `charger_invite`
    appelés sur autre chose que des constantes, ou `ouverture` rendue sur autre chose que la conversation de contrôle."""
    fautifs, fixes = [], set()
    for c in ast.walk(f):
        if isinstance(c, ast.Assign) and isinstance(c.value, ast.Call) and _nom_d_appel(c.value) == "conversation_de_controle":
            fixes |= {t.id for t in ast.walk(c.targets[0]) if isinstance(t, ast.Name)}
    for c in ast.walk(f):
        if not isinstance(c, ast.Call):
            continue
        if _nom_d_appel(c) in ("conversation_de_controle", "charger_invite"):
            if c.keywords or not all(isinstance(a, ast.Constant) for a in c.args):
                fautifs.append(c.lineno)
        elif _nom_d_appel(c) == "ouverture":
            if c.keywords or not c.args or any(_racine(a) not in fixes for a in c.args):
                fautifs.append(c.lineno)
    return fautifs


def test_les_textes_fixes_le_sont(liste, trouves):
    fixes = _entrees(liste, FIXE)
    assert len(fixes) == 3
    for rel, nom in fixes:
        assert trouves[f"{rel}::{nom}"] <= {"conversation_de_controle", "ouverture", "charger_invite"}, (rel, nom)
        assert not textes_non_fixes(_fonction(rel, nom)), (rel, nom)
    # dans toute fonction ajoutée, de toute catégorie : conversation de contrôle sur des constantes, invite chargée par
    # un nom constant ou par le champ `invite` de la spécification de la passe
    for cle in liste["registre_ajoute"]:
        for c in ast.walk(_fonction(*cle.split("::"))):
            if isinstance(c, ast.Call) and _nom_d_appel(c) == "conversation_de_controle":
                assert not c.keywords and all(isinstance(a, ast.Constant) for a in c.args), cle
            if isinstance(c, ast.Call) and _nom_d_appel(c) == "charger_invite":
                assert not c.keywords and len(c.args) == 1 and (isinstance(c.args[0], ast.Constant) or (
                    isinstance(c.args[0], ast.Attribute) and c.args[0].attr == "invite"
                    and _racine(c.args[0]) == "spec")), cle
    sain = ast.parse("def f(fmt):\n    c, o, _ = conversation_de_controle('agent', None)\n    return fmt.ouverture(c, o[0])\n")
    assert not textes_non_fixes(sain.body[0])
    for plante in ("def f(fmt, t):\n    c, o, _ = conversation_de_controle('agent', t)\n    return fmt.ouverture(c, o[0])\n",
                   "def f(fmt, t):\n    c, o, _ = conversation_de_controle('agent', None)\n    return fmt.ouverture(c, t['questions'])\n",
                   "def f(t):\n    return charger_invite(t['cibles'])\n"):
        assert textes_non_fixes(ast.parse(plante).body[0]), plante


def rendus_hors_parametres(f: ast.AST) -> list[int]:
    """Lignes fautives d'une fonction dite « rendu d'un environnement reçu » : `consigne_privee` ou `observation`
    appelées sur autre chose qu'un paramètre de la fonction ; à défaut de tels appels, `ouverture` rendue sur autre
    chose qu'un paramètre."""
    params, fautifs, vus = _parametres(f), [], 0
    for c in ast.walk(f):
        if isinstance(c, ast.Call) and _nom_d_appel(c) in ("consigne_privee", "observation"):
            vus += 1
            if not isinstance(c.func, ast.Attribute) or _racine(c.func.value) not in params:
                fautifs.append(c.lineno)
    if not vus:
        for c in ast.walk(f):
            if isinstance(c, ast.Call) and _nom_d_appel(c) == "ouverture":
                vus += 1
                if c.keywords or not c.args or any(_racine(a) not in params for a in c.args):
                    fautifs.append(c.lineno)
    return fautifs if vus else [f.lineno]


def test_les_rendus_ne_lisent_que_des_environnements_recus(liste, trouves):
    rendus = _entrees(liste, RENDU)
    assert len(rendus) == 4
    for rel, nom in rendus:
        assert trouves[f"{rel}::{nom}"] <= {"consigne_privee", "observation", "ouverture", "generer_lot"}, (rel, nom)
        assert not rendus_hors_parametres(_fonction(rel, nom)), (rel, nom)
    sain = "def f(fmt, envs):\n    return fmt.ouverture(envs[0].consigne_privee(0), envs[0].observation(0, 0, []))\n"
    assert not rendus_hors_parametres(ast.parse(sain).body[0])
    for plante in ("def f(fmt, t):\n    env = fabriquer(t)\n    return fmt.ouverture(env.consigne_privee(0), env.observation(0, 0, []))\n",
                   "def f(fmt, t):\n    debut = (str(t), 'x')\n    return fmt.ouverture(*debut)\n",
                   "def f(fmt, t):\n    return 1\n"):
        assert rendus_hors_parametres(ast.parse(plante).body[0]), plante
