"""Essais du moteur v9-v8r (option --cle-gemini, corrigée), sans réseau.

Lancement : `PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/test_collisionneur_v9_v8r.py`.
- Le script se relance d'abord dans un environnement vidé : il ne garde que PATH, HOME, la langue, PYTHONPATH et TMPDIR.
  Aucune valeur de clé réelle n'est donc lue, affichée ni envoyée. Les essais posent des valeurs factices.
- Tout passe dans le même processus. Le transport du moteur (TRANSPORT, TRANSPORT_COMPTE) est remplacé par un
  intercepteur qui relève chaque requête puis lève une exception : un essai qui ne doit rien envoyer exige zéro requête.
- Chaque garde est éprouvée sur un cas sain et sur un cas fautif (R5).
"""
import ast
import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[2]
MOTEUR = ICI / "collisionneur_v9_v8r.py"
ANCIEN = ICI / "collisionneur_v9_v8m.py"
GARDEES = ("PATH", "HOME", "LANG", "LC_ALL", "PYTHONPATH", "TMPDIR")
NOMS_GOOGLE = ("GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3", "GEMINI_API_KEY_FREE")


def charger(chemin=None, nom="moteur_v8r_essai"):
    sys.path.insert(0, str(RACINE / "src"))
    spec = importlib.util.spec_from_file_location(nom, chemin or MOTEUR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Environnement:
    """Pose des valeurs factices pour les variables de Google, retire les autres, puis rétablit (valeurs factices)."""

    def __init__(self, **valeurs):
        self.valeurs = valeurs

    def __enter__(self):
        self.avant = {n: os.environ.pop(n, None) for n in NOMS_GOOGLE}
        os.environ.update(self.valeurs)
        return self

    def __exit__(self, *a):
        for n in NOMS_GOOGLE:
            os.environ.pop(n, None)
        os.environ.update({n: v for n, v in self.avant.items() if v is not None})


class Coupure(Exception):
    pass


class Reponse:
    def __init__(self, corps):
        self.octets = json.dumps(corps).encode("utf-8")

    def read(self):
        return self.octets

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def couper(mod, reponses=None):
    """Remplace les deux transports : chaque requête est relevée (méthode, adresse, en-têtes) ; sans réponse prévue, elle
    lève Coupure."""
    releves = []
    file = list(reponses or [])

    def transport(requete, delai, locale=False):
        releves.append({"methode": requete.get_method(), "adresse": requete.full_url,
                        "entetes": {k.lower(): v for k, v in requete.header_items()}})
        if file:
            return Reponse(file.pop(0))
        raise Coupure("transport coupé par l'essai")
    mod.TRANSPORT = transport
    mod.TRANSPORT_COMPTE = transport
    mod.DORMIR = lambda s: None
    return releves


def lancer(mod, argv):
    sortie, erreurs = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreurs):
        try:
            code = mod.principal(argv)
        except SystemExit as e:
            code = e.code
    return code, sortie.getvalue() + erreurs.getvalue()


def attendre_arret(mod, appel):
    try:
        appel()
    except mod.Arret as e:
        return e
    raise AssertionError("aucun arrêt nommé")


def question(dossier):
    q = Path(dossier) / "q.md"
    q.write_text("question\n", encoding="utf-8")
    return str(q)


# ---------- composition ----------

def test_defaut_inchange():
    mod = charger()
    mod.fixer_composition(["argon", "carbon", "neon"])
    assert {mod.MODELES[l]["nom_cle"] for l in mod.LETTRES} == {"GEMINI_API_KEY"}


def test_nom_donne_aux_seules_especes_de_google():
    mod = charger()
    mod.fixer_composition(["fable", "argon", "astra", "carbon", "neon"], nom_cle_anthropic="ANTHROPIC_FACTICE",
                          nom_cle_gemini="GEMINI_API_KEY_2")
    par_espece = {mod.MODELES[l]["espece"]: mod.MODELES[l]["nom_cle"] for l in mod.LETTRES}
    assert par_espece["argon"] == par_espece["carbon"] == par_espece["neon"] == "GEMINI_API_KEY_2"
    assert par_espece["astra"] == "OPENAI_API_KEY" and par_espece["fable"] == "ANTHROPIC_FACTICE"


def test_refus_autre_fournisseur():
    mod = charger()
    e = attendre_arret(mod, lambda: mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="OPENAI_API_KEY"))
    assert e.code == mod.CODE_USAGE and "doit commencer par GEMINI_API_KEY" in str(e)


def test_refus_nom_refuse():
    mod = charger()
    e = attendre_arret(mod, lambda: mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_3"))
    assert e.code == mod.CODE_USAGE and "consigne de la mère" in str(e)


def test_refus_nom_mal_forme():
    mod = charger()
    e = attendre_arret(mod, lambda: mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY-2"))
    assert e.code == mod.CODE_USAGE and "mal formé" in str(e)


def test_cle_restreinte_admise_pour_carbon_et_neon():
    mod = charger()
    mod.fixer_composition(["carbon", "neon"], nom_cle_gemini="GEMINI_API_KEY_FREE")
    assert {mod.MODELES[l]["nom_cle"] for l in mod.LETTRES} == {"GEMINI_API_KEY_FREE"}
    mod.fixer_composition(["fable", "carbon", "neon"], nom_cle_anthropic="ANTHROPIC_FACTICE",
                          nom_cle_gemini="GEMINI_API_KEY_FREE")  # une espèce hors de Google ne gêne pas


def test_cle_restreinte_refusee_avec_argon():
    mod = charger()
    e = attendre_arret(mod, lambda: mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_FREE"))
    assert e.code == mod.CODE_USAGE and "argon" in str(e)


def test_espace_anthropic_ne_nomme_pas_une_cle_de_google():
    mod = charger()
    mod.fixer_composition(["fable", "argon"], nom_cle_anthropic="ANTHROPIC_FACTICE")  # défaut : admis
    e = attendre_arret(mod, lambda: mod.fixer_composition(["fable", "argon"], nom_cle_anthropic="ANTHROPIC_FACTICE",
                                                          nom_espace_anthropic="GEMINI_API_KEY_2"))
    assert e.code == mod.CODE_USAGE and "--nom-espace-anthropic" in str(e)


# ---------- lecture de la clé ----------

def test_flux_lit_la_variable_nommee():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_2")
    m = mod.MODELES["A"]
    releves = couper(mod)
    with Environnement(GEMINI_API_KEY="defaut-factice", GEMINI_API_KEY_2="deux-factice"):
        try:
            mod.appeler_gemini(m, "bonjour", m["max"])
        except Coupure:
            pass
    assert [r["entetes"]["x-goog-api-key"] for r in releves] == ["deux-factice"]


def test_flux_sans_option_lit_le_defaut():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"])
    m = mod.MODELES["A"]
    releves = couper(mod)
    with Environnement(GEMINI_API_KEY="defaut-factice", GEMINI_API_KEY_2="deux-factice"):
        try:
            mod.appeler_gemini(m, "bonjour", m["max"])
        except Coupure:
            pass
    assert [r["entetes"]["x-goog-api-key"] for r in releves] == ["defaut-factice"]


def test_aucun_repli_sans_nom_de_composition():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"])
    m = dict(mod.MODELES["A"])
    del m["nom_cle"]
    releves = couper(mod)
    with Environnement(GEMINI_API_KEY="defaut-factice"):
        r = mod.appeler_gemini(m, "bonjour", m["max"])
        r_lot = mod.appeler_gemini_lot(m, "bonjour", m["max"])
        e = attendre_compte(mod, m)
    assert not releves
    assert "absent de la composition" in r.echec and "absent de la composition" in r_lot.echec
    assert "absent de la composition" in str(e)


def attendre_compte(mod, m):
    try:
        mod.compter_gemini(m, "bonjour")
    except mod.RefusCompte as e:
        return e
    raise AssertionError("aucun refus de comptage")


def test_nom_refuse_ne_part_jamais_meme_injecte():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"])
    m = dict(mod.MODELES["A"], nom_cle="GEMINI_API_KEY_3")
    releves = couper(mod)
    with Environnement(GEMINI_API_KEY_3="trois-factice"):
        r = mod.appeler_gemini(m, "bonjour", m["max"])
        r_lot = mod.appeler_gemini_lot(m, "bonjour", m["max"])
        e = attendre_compte(mod, m)
    assert not releves
    assert "consigne de la mère" in r.echec and "consigne de la mère" in r_lot.echec and "consigne" in str(e)


def test_variable_nommee_absente_rien_ne_part():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_2")
    m = mod.MODELES["A"]
    releves = couper(mod)
    with Environnement(GEMINI_API_KEY="defaut-factice"):
        r = mod.appeler_gemini(m, "bonjour", m["max"])
        r_lot = mod.appeler_gemini_lot(m, "bonjour", m["max"])
        e = attendre_compte(mod, m)
    assert not releves
    for texte in (r.echec, r_lot.echec, str(e)):
        assert "GEMINI_API_KEY_2 absente" in texte and "defaut-factice" not in texte


def test_comptage_lit_la_variable_nommee():
    mod = charger()
    mod.fixer_composition(["carbon", "neon"], nom_cle_gemini="GEMINI_API_KEY_FREE")
    m = mod.MODELES["A"]
    releves = couper(mod)
    with Environnement(GEMINI_API_KEY="defaut-factice", GEMINI_API_KEY_FREE="libre-factice"):
        try:
            mod.compter_gemini(m, "bonjour")
        except (Coupure, mod.RefusCompte):
            pass
    assert [r["entetes"]["x-goog-api-key"] for r in releves] == ["libre-factice"]


def test_lot_creation_releves_et_annulation_lisent_la_variable_nommee():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_2")
    m = mod.MODELES["A"]
    plafond = min(m["max"], mod.LIMITES_SORTIE[m["espece"]]["non_diffuse"])
    en_cours = {"name": "batches/essai", "done": False, "metadata": {"state": "BATCH_STATE_RUNNING"}}
    releves = couper(mod, reponses=[{"name": "batches/essai"}, en_cours, en_cours, {}])
    temps = iter([0, 0, 10 ** 9, 10 ** 9, 10 ** 9])
    mod.HORLOGE = lambda: next(temps)
    with Environnement(GEMINI_API_KEY="defaut-factice", GEMINI_API_KEY_2="deux-factice"):
        r = mod.appeler_gemini_lot(m, "bonjour", plafond)
    methodes = [(x["methode"], x["adresse"].rsplit("/", 1)[-1]) for x in releves]
    assert methodes[0][1].endswith(":batchGenerateContent") and methodes[-1][1].endswith(":cancel"), methodes
    assert any(x[0] == "GET" for x in methodes), methodes
    assert {x["entetes"]["x-goog-api-key"] for x in releves} == {"deux-factice"}
    assert r.interrompue and "deux-factice" not in (r.echec or "") + (r.texte or "")


def test_aucune_lecture_a_nom_fixe_de_la_cle_de_google():
    arbre = ast.parse(MOTEUR.read_text(encoding="utf-8"))
    fautes = []
    for n in ast.walk(arbre):
        cibles = []
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in ("get", "getenv") and n.args:
            cibles.append(n.args[0])
        if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Attribute) and n.value.attr == "environ":
            cibles.append(n.slice)
        for c in cibles:
            if isinstance(c, ast.Constant) and isinstance(c.value, str) and c.value.startswith("GEMINI_API_KEY"):
                fautes.append(n.lineno)
            if (isinstance(c, ast.Subscript) and isinstance(c.value, ast.Name) and c.value.id == "NOMS_CLES"
                    and isinstance(c.slice, ast.Constant) and c.slice.value == "gemini"):
                fautes.append(n.lineno)
    assert not fautes, fautes


# ---------- journal et écran ----------

def test_journal_et_ecran_ne_montrent_jamais_la_valeur():
    mod = charger()
    with tempfile.TemporaryDirectory() as t, Environnement(GEMINI_API_KEY="defaut-secret-factice",
                                                            GEMINI_API_KEY_2="deux-secret-factice"):
        d = Path(t)
        noms = lambda: [e["nom_cle_gemini"] for e in mod.lire_journal(d) if "nom_cle_gemini" in e]
        ecran = io.StringIO()
        with contextlib.redirect_stdout(ecran):
            mod.fixer_composition(["argon", "carbon"])
            mod.declarer_cle_gemini(d)
            assert noms() == []
            mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_2")
            mod.declarer_cle_gemini(d)
            mod.declarer_cle_gemini(d)
            assert noms() == ["GEMINI_API_KEY_2"]
            mod.fixer_composition(["argon", "carbon"])
            mod.declarer_cle_gemini(d)
            assert noms() == ["GEMINI_API_KEY_2", "GEMINI_API_KEY"]
            mod.fixer_composition(["fable", "opus"], nom_cle_anthropic="ANTHROPIC_FACTICE")
            mod.declarer_cle_gemini(d)
            assert noms() == ["GEMINI_API_KEY_2", "GEMINI_API_KEY"]
        journal = (d / "journal.jsonl").read_text(encoding="utf-8")
        for texte in (journal, ecran.getvalue()):
            assert "secret-factice" not in texte
        assert "GEMINI_API_KEY_2" in ecran.getvalue()


# ---------- ligne de commande, dans le même processus ----------

def test_ligne_de_commande_refuse_le_nom_refuse():
    mod = charger()
    releves = couper(mod)
    with tempfile.TemporaryDirectory() as t, Environnement(GEMINI_API_KEY_3="trois-factice"):
        q = question(t)
        code, texte = lancer(mod, ["etage3", "--argon", "--carbon", "--cle-gemini", "GEMINI_API_KEY_3",
                                   "--sortie", str(Path(t) / "d"), "--faits", q, "--question", q])
        assert code == mod.CODE_USAGE and "est refusée" in texte and "trois-factice" not in texte
        assert not releves and not (Path(t) / "d" / "journal.jsonl").exists()


def test_ligne_de_commande_refuse_une_variable_nommee_absente():
    mod = charger()
    releves = couper(mod)
    with tempfile.TemporaryDirectory() as t, Environnement(GEMINI_API_KEY="defaut-factice"):
        q = question(t)
        code, texte = lancer(mod, ["etage3", "--argon", "--carbon", "--cle-gemini", "GEMINI_API_KEY_2",
                                   "--sortie", str(Path(t) / "d"), "--faits", q, "--question", q])
        assert code == mod.CODE_USAGE and "GEMINI_API_KEY_2" in texte and "defaut-factice" not in texte
        assert not releves and not (Path(t) / "d" / "journal.jsonl").exists()


def test_ligne_de_commande_sans_option_ni_variable_nomme_le_defaut():
    mod = charger()
    releves = couper(mod)
    with tempfile.TemporaryDirectory() as t, Environnement():
        q = question(t)
        code, texte = lancer(mod, ["etage3", "--argon", "--carbon", "--sortie", str(Path(t) / "d"),
                                   "--faits", q, "--question", q])
        assert code == mod.CODE_USAGE and "['GEMINI_API_KEY']" in texte, texte[-300:]  # le nom exact du défaut
        assert not releves


def test_reprise_exigee_avant_tout_journal_du_nom():
    mod = charger()
    releves = couper(mod)
    with tempfile.TemporaryDirectory() as t, Environnement(GEMINI_API_KEY_2="deux-factice"):
        q = question(t)
        d = Path(t) / "d"
        d.mkdir()
        (d / "journal.jsonl").write_text(json.dumps({"essai": 1, "cellule": "E3-T1-conception-A", "statut": "OK",
                                                     "cout_usd": 0.0, "sha256_script": "0" * 64,
                                                     "modele_servi": "gemini-4-argon", "caracteres": 0,
                                                     "marqueur_fin": False}) + "\n",
                                         encoding="utf-8")
        code, texte = lancer(mod, ["etage3", "--argon", "--carbon", "--cle-gemini", "GEMINI_API_KEY_2",
                                   "--sortie", str(d), "--faits", q, "--question", q])
        assert code == mod.CODE_USAGE and "--reprise" in texte
        assert not any("nom_cle_gemini" in e for e in mod.lire_journal(d))
        assert not releves


def test_devis_identique_a_la_v8m():
    with tempfile.TemporaryDirectory() as t:
        q = Path(t) / "q.md"
        q.write_text("Une question de quelques mots, pour le devis.\n", encoding="utf-8")
        argv = ["devis", "--argon", "--carbon", "--neon", "--faits", str(q), "--question", str(q)]
        nouveau, ancien = charger(), charger(ANCIEN, "moteur_v8m_essai")
        r_nouveau, r_ancien = couper(nouveau), couper(ancien)
        c1, t1 = lancer(nouveau, argv)
        c2, t2 = lancer(ancien, argv)
        assert c1 == c2 == 0 and t1 == t2 and not r_nouveau and not r_ancien


def relancer_dans_un_environnement_vide():
    if os.environ.get("ESSAIS_V8R_ENVIRONNEMENT_VIDE") == "1":
        return
    env = {k: v for k, v in os.environ.items() if k in GARDEES}
    env["ESSAIS_V8R_ENVIRONNEMENT_VIDE"] = "1"
    env.setdefault("PYTHONPATH", str(RACINE / "src"))
    os.execve(sys.executable, [sys.executable, "-B", str(Path(__file__).resolve())], env)


if __name__ == "__main__":
    relancer_dans_un_environnement_vide()
    essais = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    echecs = 0
    for nom, f in essais:
        try:
            f()
            print(f"OK    {nom}")
        except Exception as e:  # noqa: BLE001
            echecs += 1
            print(f"ÉCHEC {nom} : {type(e).__name__} : {e}")
    print(f"{len(essais) - echecs} sur {len(essais)} essais passés")
    sys.exit(1 if echecs else 0)
