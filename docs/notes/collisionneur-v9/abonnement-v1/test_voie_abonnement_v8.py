"""Essais de la voie abonnement v8 (moteur v8r admis, --cle-gemini réservée au v8r), sans réseau.

Lancement : `PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/abonnement-v1/test_voie_abonnement_v8.py`.
- Le script se relance dans un environnement vidé (PATH, HOME, langue, PYTHONPATH, TMPDIR seulement) : aucune valeur
  de clé réelle n'est lue.
- Les moteurs sont chargés par la voie elle-même (empreinte contrôlée), puis leur transport est coupé avant tout
  lancement : un essai qui ne doit rien envoyer exige zéro requête.
"""
import contextlib
import hashlib
import importlib.util
import io
import os
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[3]
GARDEES = ("PATH", "HOME", "LANG", "LC_ALL", "PYTHONPATH", "TMPDIR")


def charger_voie(version):
    sys.path.insert(0, str(RACINE / "src"))
    spec = importlib.util.spec_from_file_location(f"voie_{version}_essai", ICI / f"voie_abonnement_{version}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Coupure(Exception):
    pass


def couper(moteur):
    releves = []

    def transport(requete, delai, locale=False):
        releves.append(requete.full_url)
        raise Coupure("transport coupé par l'essai")
    moteur.TRANSPORT = transport
    moteur.TRANSPORT_COMPTE = transport
    moteur.DORMIR = lambda s: None
    return releves


def capter(appel):
    sortie = io.StringIO()
    with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(sortie):
        try:
            code = appel()
        except SystemExit as e:
            code = e.code
    return code, sortie.getvalue()


def test_table_des_moteurs():
    voie = charger_voie("v8")
    chemin, sha = voie.MOTEURS["v8r"]
    assert hashlib.sha256(Path(chemin).read_bytes()).hexdigest() == sha
    assert "v8q" not in voie.MOTEURS and {"v8m", "v8p", "v8r"} <= set(voie.MOTEURS)


def test_copie_modifiee_refusee():
    voie = charger_voie("v8")
    chemin, sha = voie.MOTEURS["v8r"]
    with tempfile.TemporaryDirectory() as t:
        copie = Path(t) / "collisionneur_v9_v8r.py"
        copie.write_bytes(Path(chemin).read_bytes() + b"\n# modification\n")
        try:
            voie.charger(copie, sha, "moteur_v8r_modifie")
        except SystemExit as e:
            assert "empreinte" in str(e)
        else:
            raise AssertionError("une copie modifiée a été chargée")


def test_devis_identique_par_les_voies_v6_et_v8():
    v6, v8 = charger_voie("v6"), charger_voie("v8")
    m_ancien = v6.charger(*v6.MOTEURS["v8m"], "moteur_v8m_essai_voie")
    m_nouveau = v8.charger(*v8.MOTEURS["v8r"], "moteur_v8r_essai_voie")
    r_ancien, r_nouveau = couper(m_ancien), couper(m_nouveau)
    with tempfile.TemporaryDirectory() as t:
        q = Path(t) / "q.md"
        q.write_text("Une question de quelques mots, pour le devis.\n", encoding="utf-8")
        argv = ["devis", "--fable", "--opus", "--argon", "--carbon", "--neon", "--faits", str(q), "--question", str(q)]
        c1, t1 = capter(lambda: v6.lancer_moteur("v8m", v6.BRANCHE_DEFAUT, argv, v=m_ancien, effort="high"))
        c2, t2 = capter(lambda: v8.lancer_moteur("v8r", v8.BRANCHE_DEFAUT, argv, v=m_nouveau, effort="high"))
    assert c1 == c2 == 0 and t1 == t2, (c1, c2)
    assert not r_ancien and not r_nouveau


def test_nom_refuse_a_travers_la_voie():
    v8 = charger_voie("v8")
    moteur = v8.charger(*v8.MOTEURS["v8r"], "moteur_v8r_essai_refus")
    releves = couper(moteur)
    avant = {n: os.environ.pop(n, None) for n in ("GEMINI_API_KEY_3", "ABONNEMENT_CLE_FACTICE")}
    os.environ.update(GEMINI_API_KEY_3="trois-factice", ABONNEMENT_CLE_FACTICE="factice")
    try:
        with tempfile.TemporaryDirectory() as t:
            q = Path(t) / "q.md"
            q.write_text("question\n", encoding="utf-8")
            argv = ["etage3", "--argon", "--carbon", "--cle-gemini", "GEMINI_API_KEY_3",
                    "--cle-anthropic", "ABONNEMENT_CLE_FACTICE", "--sortie", str(Path(t) / "d"),
                    "--faits", str(q), "--question", str(q), "--plafond-usd", "1", "--ligne-usd", "1"]
            code, texte = capter(lambda: v8.lancer_moteur("v8r", v8.BRANCHE_DEFAUT, argv, v=moteur, effort="high"))
            assert code == 1 and "est refusée" in texte and "trois-factice" not in texte, (code, texte[-300:])
            assert not releves and not (Path(t) / "d" / "journal.jsonl").exists()
    finally:
        for n in ("GEMINI_API_KEY_3", "ABONNEMENT_CLE_FACTICE"):
            os.environ.pop(n, None)
        os.environ.update({n: v for n, v in avant.items() if v is not None})


def test_cle_gemini_refusee_hors_du_v8r():
    v8 = charger_voie("v8")
    for forme in (["--cle-gemini", "GEMINI_API_KEY_2"], ["--cle-gemini=GEMINI_API_KEY_2"]):
        for commande in ("v8m", "v8p", "essaim"):
            argv = [commande, "--effort", "high", "--", "etage3", "--argon", "--carbon", *forme]
            code, texte = capter(lambda: v8.principal(argv))
            assert code == 1 and "n'est admise qu'avec le moteur v8r" in texte, (commande, code, texte[-200:])


def relancer_dans_un_environnement_vide():
    if os.environ.get("ESSAIS_VOIE_V8_ENVIRONNEMENT_VIDE") == "1":
        return
    env = {k: v for k, v in os.environ.items() if k in GARDEES}
    env["ESSAIS_VOIE_V8_ENVIRONNEMENT_VIDE"] = "1"
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
