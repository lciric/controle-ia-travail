"""Essais du moteur v9-v8q (option --cle-gemini), sans réseau.

Lancement : `PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/test_collisionneur_v9_v8q.py` (ou par pytest).
Chaque garde est éprouvée sur un cas sain et sur un cas fautif (R5). Aucune valeur de clé réelle n'est lue : les essais
posent des valeurs factices dans l'environnement et interceptent le transport (TRANSPORT, TRANSPORT_COMPTE).
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[2]
MOTEUR = ICI / "collisionneur_v9_v8q.py"
ANCIEN = ICI / "collisionneur_v9_v8m.py"
NOMS_GOOGLE = ("GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3", "GEMINI_API_KEY_FREE")


def charger():
    sys.path.insert(0, str(RACINE / "src"))
    spec = importlib.util.spec_from_file_location("moteur_v8q_essai", MOTEUR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Environnement:
    """Remplace les variables de Google par des valeurs factices, puis rétablit l'environnement d'origine."""

    def __init__(self, **valeurs):
        self.valeurs = valeurs

    def __enter__(self):
        self.avant = {n: os.environ.get(n) for n in NOMS_GOOGLE}
        for n in NOMS_GOOGLE:
            os.environ.pop(n, None)
        os.environ.update(self.valeurs)
        return self

    def __exit__(self, *a):
        for n, v in self.avant.items():
            if v is None:
                os.environ.pop(n, None)
            else:
                os.environ[n] = v


class Coupure(Exception):
    pass


def intercepteur(captures):
    def transport(requete, delai, locale=False):
        captures.append(dict(requete.header_items()))
        raise Coupure("transport intercepté par l'essai")
    return transport


def attendre_arret(mod, appel):
    try:
        appel()
    except mod.Arret as e:
        return e
    raise AssertionError("aucun arrêt nommé")


def test_defaut_inchange():
    mod = charger()
    mod.fixer_composition(["argon", "carbon", "neon"])
    assert {mod.MODELES[l]["nom_cle"] for l in mod.LETTRES} == {"GEMINI_API_KEY"}


def test_option_donne_le_nom_aux_seules_especes_de_google():
    mod = charger()
    mod.fixer_composition(["fable", "argon", "astra", "carbon", "neon"], nom_cle_anthropic="ANTHROPIC_FACTICE",
                          nom_cle_gemini="GEMINI_API_KEY_2")
    par_espece = {mod.MODELES[l]["espece"]: mod.MODELES[l]["nom_cle"] for l in mod.LETTRES}
    assert par_espece["argon"] == par_espece["carbon"] == par_espece["neon"] == "GEMINI_API_KEY_2"
    assert par_espece["astra"] == "OPENAI_API_KEY"
    assert par_espece["fable"] == "ANTHROPIC_FACTICE"


def test_refus_autre_fournisseur():
    mod = charger()
    e = attendre_arret(mod, lambda: mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="OPENAI_API_KEY"))
    assert e.code == mod.CODE_USAGE and "--cle-gemini" in str(e)


def test_refus_cle_epuisee():
    mod = charger()
    e = attendre_arret(mod, lambda: mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_3"))
    assert e.code == mod.CODE_USAGE and "GEMINI_API_KEY_3" in str(e)


def test_refus_nom_mal_forme():
    mod = charger()
    e = attendre_arret(mod, lambda: mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="gemini_api_key"))
    assert e.code == mod.CODE_USAGE


def test_envoi_en_flux_lit_la_variable_nommee():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_2")
    m = mod.MODELES["A"]
    captures = []
    mod.TRANSPORT = intercepteur(captures)
    with Environnement(GEMINI_API_KEY="valeur-defaut-factice", GEMINI_API_KEY_2="valeur-deux-factice"):
        try:
            mod.appeler_gemini(m, "bonjour", m["max"])
        except Coupure:
            pass
    assert captures, "aucune requête n'est partie vers le transport"
    entetes = {k.lower(): v for k, v in captures[0].items()}
    assert entetes["x-goog-api-key"] == "valeur-deux-factice"


def test_envoi_en_flux_sans_option_lit_la_cle_par_defaut():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"])
    m = mod.MODELES["A"]
    captures = []
    mod.TRANSPORT = intercepteur(captures)
    with Environnement(GEMINI_API_KEY="valeur-defaut-factice", GEMINI_API_KEY_2="valeur-deux-factice"):
        try:
            mod.appeler_gemini(m, "bonjour", m["max"])
        except Coupure:
            pass
    entetes = {k.lower(): v for k, v in captures[0].items()}
    assert entetes["x-goog-api-key"] == "valeur-defaut-factice"


def test_variable_nommee_absente_rien_ne_part():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_2")
    m = mod.MODELES["A"]
    captures = []
    mod.TRANSPORT = intercepteur(captures)
    with Environnement(GEMINI_API_KEY="valeur-defaut-factice"):
        r = mod.appeler_gemini(m, "bonjour", m["max"])
        r_lot = mod.appeler_gemini_lot(m, "bonjour", m["max"])
    assert not captures
    assert "GEMINI_API_KEY_2 absente" in r.echec and "GEMINI_API_KEY_2 absente" in r_lot.echec
    assert "valeur-defaut-factice" not in r.echec


def test_comptage_lit_la_variable_nommee():
    mod = charger()
    mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_FREE")
    m = mod.MODELES["B"]
    captures = []
    mod.TRANSPORT_COMPTE = intercepteur(captures)
    with Environnement(GEMINI_API_KEY="valeur-defaut-factice", GEMINI_API_KEY_FREE="valeur-libre-factice"):
        try:
            mod.compter_gemini(m, "bonjour")
        except (Coupure, mod.RefusCompte):
            pass
    entetes = {k.lower(): v for k, v in captures[0].items()}
    assert entetes["x-goog-api-key"] == "valeur-libre-factice"


def test_journal_du_nom_de_cle():
    mod = charger()
    with tempfile.TemporaryDirectory() as t:
        d = Path(t)
        lire = lambda: [e["nom_cle_gemini"] for e in mod.lire_journal(d) if "nom_cle_gemini" in e]
        mod.fixer_composition(["argon", "carbon"])
        mod.declarer_cle_gemini(d)
        assert lire() == []  # clé par défaut au premier lancement : rien de neuf à journaliser
        mod.fixer_composition(["argon", "carbon"], nom_cle_gemini="GEMINI_API_KEY_2")
        mod.declarer_cle_gemini(d)
        mod.declarer_cle_gemini(d)
        assert lire() == ["GEMINI_API_KEY_2"]  # une seule ligne pour deux lancements identiques
        mod.fixer_composition(["argon", "carbon"])
        mod.declarer_cle_gemini(d)
        assert lire() == ["GEMINI_API_KEY_2", "GEMINI_API_KEY"]  # le retour au défaut est journalisé
        texte = (d / "journal.jsonl").read_text(encoding="utf-8")
        assert "factice" not in texte
        mod.fixer_composition(["fable", "opus"], nom_cle_anthropic="ANTHROPIC_FACTICE")
        mod.declarer_cle_gemini(d)
        assert lire() == ["GEMINI_API_KEY_2", "GEMINI_API_KEY"]  # aucune espèce de Google : rien


def lancer(*args, env_extra=None):
    env = {k: v for k, v in os.environ.items() if k not in NOMS_GOOGLE}
    env.update(env_extra or {})
    env["PYTHONPATH"] = str(RACINE / "src")
    return subprocess.run([sys.executable, "-B", str(MOTEUR), *args], capture_output=True, text=True, env=env,
                          cwd=str(RACINE), timeout=120)


def test_ligne_de_commande_refuse_la_cle_epuisee_sans_reseau():
    with tempfile.TemporaryDirectory() as t:
        q = Path(t) / "q.md"
        q.write_text("question\n", encoding="utf-8")
        r = lancer("etage3", "--argon", "--carbon", "--cle-gemini", "GEMINI_API_KEY_3", "--sortie", str(Path(t) / "d"),
                   "--faits", str(q), "--question", str(q), env_extra={"GEMINI_API_KEY_3": "factice"})
        assert r.returncode == 1, (r.returncode, r.stderr[-500:])
        assert "GEMINI_API_KEY_3" in (r.stdout + r.stderr)
        assert not (Path(t) / "d" / "journal.jsonl").exists()


def test_ligne_de_commande_refuse_une_cle_nommee_absente_sans_reseau():
    with tempfile.TemporaryDirectory() as t:
        q = Path(t) / "q.md"
        q.write_text("question\n", encoding="utf-8")
        r = lancer("etage3", "--argon", "--carbon", "--cle-gemini", "GEMINI_API_KEY_2", "--sortie", str(Path(t) / "d"),
                   "--faits", str(q), "--question", str(q), env_extra={"GEMINI_API_KEY": "factice"})
        assert r.returncode == 1, (r.returncode, r.stderr[-500:])
        assert "GEMINI_API_KEY_2" in (r.stdout + r.stderr)
        assert not (Path(t) / "d" / "journal.jsonl").exists()


def test_devis_identique_a_la_v8m():
    with tempfile.TemporaryDirectory() as t:
        q = Path(t) / "q.md"
        q.write_text("Une question de quelques mots, pour le devis.\n", encoding="utf-8")
        args = ["devis", "--argon", "--carbon", "--neon", "--faits", str(q), "--question", str(q)]
        env = {k: v for k, v in os.environ.items() if k not in NOMS_GOOGLE}
        env["PYTHONPATH"] = str(RACINE / "src")
        nouveau = subprocess.run([sys.executable, "-B", str(MOTEUR), *args], capture_output=True, text=True, env=env,
                                 cwd=str(RACINE), timeout=120)
        ancien = subprocess.run([sys.executable, "-B", str(ANCIEN), *args], capture_output=True, text=True, env=env,
                                cwd=str(RACINE), timeout=120)
        assert nouveau.returncode == ancien.returncode == 0
        assert nouveau.stdout == ancien.stdout


def test_aucune_lecture_fixe_de_la_cle_de_google():
    texte = MOTEUR.read_text(encoding="utf-8")
    assert 'os.environ.get("GEMINI_API_KEY")' not in texte
    assert texte.count('os.environ.get(nom_cle)') >= 3


if __name__ == "__main__":
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
