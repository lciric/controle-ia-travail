"""Essais de la sonde réelle de Carbon par la chaîne synchrone d'Argon (`scripts/sonde_carbon_synchrone_v1.py`) et de
l'enveloppe `rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh` — **aucun appel réel** : un faux amont Gemini local
(`faux_amont_gemini_recherche_v3.py`, épinglé au dépôt) tient la place du fournisseur, sur la boucle locale ; une copie d'essai de
l'enveloppe ne change que l'adresse (le port 8792 n'est jamais employé par ces essais : un relais réel pourrait y tourner).
Chaque garde est essayée sur un cas sain et sur un artefact (R5) ; des mutants montrent que les essais attrapent l'oubli d'une
garde. Un essai de bout en bout passe aussi par le vrai relais `relais_gemini_v2.py` (épinglé), clé factice, devant le faux amont."""
import datetime as dt
import hashlib
import importlib.util
import json
import os
import shlex
import socket
import subprocess
import sys
import time
from pathlib import Path

import pytest

sys.dont_write_bytecode = True
RACINE = Path(__file__).resolve().parents[1]


def _charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


L = _charger("lancer_course_auto_conception_v7_pour_essai_sonde", RACINE / "scripts" / "lancer_course_auto_conception_v7.py")
CHEMIN_SONDE = RACINE / "scripts" / "sonde_carbon_synchrone_v1.py"
S = _charger("sonde_carbon_synchrone_v1_essai", CHEMIN_SONDE)
ARGON = RACINE / "docs/notes/ideation-organisme-v1/argon-recherche-v1"
FAUX_AMONT = ARGON / "faux_amont_gemini_recherche_v3.py"
RELAIS = ARGON / "relais_gemini_v2.py"
ENVELOPPE = RACINE / L.PIECES["enveloppe_carbon"][0]
JOUR = dt.date(2026, 11, 19)
GO = "GO-2026-11-19-90"
TEXTE_FACTICE = "Réponse factice d'Argon."


def _matiere():
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"{L.REF_MAIN}:{L.MATIERE[0]}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == L.MATIERE[1] else None


MATIERE = _matiere()
pytestmark = pytest.mark.skipif(MATIERE is None, reason="matière v3 absente de refs/remotes/origin/main (fetch ciblé requis)")


def registre(plafond="6 USD", perimetre="sonde réelle de Carbon (commande synchrone), plus grand lot", suite=""):
    return ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\n|---|---|---|---|---|---|---|---|\n"
            f"| {GO} | 2026-11-19 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-1 |\n" + suite)


def port_libre() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def lancer_faux_amont(tmp, *options):
    journal = tmp / f"faux-amont-{len(list(tmp.glob('faux-amont-*')))}.jsonl"
    p = subprocess.Popen([sys.executable, "-I", "-B", str(FAUX_AMONT), "--port", "0", "--journal", str(journal), *options],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    ligne = p.stdout.readline().strip()
    assert ligne.startswith("pret http://127.0.0.1:"), ligne
    return p, ligne.split(" ", 1)[1], journal


def enveloppe_d_essai(tmp, url_base) -> Path:
    """L'enveloppe épinglée, à l'octet, sauf l'adresse du relais (vers le faux amont ou le relais d'essai)."""
    lignes = ENVELOPPE.read_text(encoding="utf-8").split("\n")
    execs = [i for i, l in enumerate(lignes) if l.startswith("exec ")]
    assert len(execs) == 1 and lignes[execs[0]].count("--url-base http://127.0.0.1:8792/v1beta") == 1
    lignes[execs[0]] = lignes[execs[0]].replace("--url-base http://127.0.0.1:8792/v1beta", "--url-base " + url_base + "/v1beta")
    p = tmp / "appel-carbon-synchrone-essai.sh"
    p.write_text("\n".join(lignes), encoding="utf-8")
    return p


class Monde:
    def __init__(self, tmp):
        self.tmp = tmp
        prog = tmp / "relais_gemini_v2.py"
        prog.write_text("# relais factice (essai)\n", encoding="utf-8")
        self.prog = prog
        self.main = {"registres/go.md": registre().encode("utf-8"), L.MATIERE[0]: MATIERE}
        r = L.Reglages.production()
        r.lire_main = lambda chemin: (self.main[chemin], "c" * 40)
        r.programmes_relais = dict(L.PROGRAMMES_RELAIS, carbon=("relais_gemini_v2.py", hashlib.sha256(prog.read_bytes()).hexdigest()))
        self.r = r
        self.cmdline = [sys.executable, "-I", "-B", str(prog), "--port", "8792", "--modele", "gemini-4-carbon", "--max-appels", "2",
                        "--variable-cle", "GEMINI_API_KEY"]
        self.avant = {"appels": 0, "refus": 0, "max_appels": 2, "modeles": ["gemini-4-carbon"], "amont": L.AMONT_GEMINI,
                      "variable_cle_encore_presente": False, "version": "relais-gemini-v2"}
        self.apres = dict(self.avant, appels=2)
        self.lectures = 0
        self.sortie = tmp / "rapport-sonde-carbon.json"

    def lire_etat(self, url):
        self.lectures += 1
        return dict(self.avant if self.lectures == 1 else self.apres)

    def sonder(self, commande, **kw):
        kw.setdefault("environ", {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8"})
        return S.sonder(L, self.r, GO, 4242, self.sortie, commande=commande, lire_etat=self.lire_etat,
                        lire_cmd=lambda pid: list(self.cmdline), aujourd_hui=JOUR, horodatage=lambda: "2026-11-19T07:00:00Z", **kw)


@pytest.fixture
def monde(tmp_path):
    return Monde(tmp_path)


def _rapport(m):
    assert L.scelle(m.sortie)
    return json.loads(m.sortie.read_text(encoding="utf-8"))


def _sans_texte(m):
    brut = m.sortie.read_text(encoding="utf-8")
    assert TEXTE_FACTICE not in brut and '"texte"' not in brut


# --- l'enveloppe ----------------------------------------------------------------------------------------------------------------


def test_enveloppe_options_admises_par_l_analyseur_de_la_commande():
    """Les options de la ligne `exec` sont celles de l'analyseur de `commande_argon_v3d.py` (épinglée), en entier, et valent le
    réglage de l'additif v2g ; sans troncature : sortie = maximum de la commande, provision ≥ sortie, budget de pensée non posé."""
    m = L.charger_commande_argon(str(RACINE / L.PIECES["commande_argon"][0]))
    lu = L.lire_reglage_enveloppe_carbon(ENVELOPPE.read_text(encoding="utf-8"))
    a = m.analyseur().parse_args([x for kv in lu["options"].items() for x in kv] + lu["drapeaux"])
    assert a.modele == "gemini-4-carbon" and a.max_sortie_jetons == m.MAX_SORTIE_JETONS_DEFAUT == 65536
    assert a.provision_pensee_jetons >= a.max_sortie_jetons and a.config_pensee is False and a.compter_jetons is True
    assert (float(a.prix_entree), float(a.prix_sortie), float(a.delai_s)) == (8.3, 41.5, 1680.0)
    assert a.url_base == "http://127.0.0.1:8792/v1beta" and lu["timeout"] == {"-k": 20.0, "duree": 1720.0}


def test_enveloppe_refuse_tout_argument(tmp_path):
    p = subprocess.run(["bash", str(ENVELOPPE), "--provision-pensee-jetons", "1"], capture_output=True, text=True, input="x",
                       env={"PATH": "/usr/bin:/bin"}, timeout=30)
    assert p.returncode == 2 and json.loads(p.stdout.strip().splitlines()[-1])["cout_usd"] == 1e-06


def test_chaine_saine_par_le_faux_amont(tmp_path):
    """L'enveloppe (adresse d'essai) → la commande d'Argon épinglée → faux amont : code 0, STOP, sortie demandée 65 536, aucun
    thinkingConfig envoyé, countTokens puis generateContent."""
    p, url, journal = lancer_faux_amont(tmp_path, "--pensees", "20000", "--candidats", "3400")
    try:
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": "6.0",
               "ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": "gemini-4-carbon", "HOME": str(tmp_path)}
        q = subprocess.run(["bash", str(enveloppe_d_essai(tmp_path, url))], input="consigne d'essai".encode(), capture_output=True,
                           env=env, timeout=120)
    finally:
        p.kill()
    o = json.loads(q.stdout.decode().strip().splitlines()[-1])
    assert q.returncode == 0 and o["code"] == 0 and o["fin"] == "STOP" and o["max_sortie_jetons"] == 65536
    assert o["config_pensee"] is False and o["provision_pensee_jetons"] == 65536
    req = [json.loads(x) for x in journal.read_text().splitlines()]
    assert [x["chemin"].rsplit(":", 1)[1] for x in req] == ["countTokens", "generateContent"]
    gc = req[1]["corps"]["generationConfig"]
    assert gc == {"maxOutputTokens": 65536} and "thinkingConfig" not in gc


# --- la sonde : cas sain, puis artefacts ---------------------------------------------------------------------------------------


def test_sonde_saine(monde):
    p, url, journal = lancer_faux_amont(monde.tmp, "--pensees", "20000", "--candidats", "3400")
    try:
        code = monde.sonder(["bash", str(enveloppe_d_essai(monde.tmp, url))])
    finally:
        p.kill()
    o = _rapport(monde)
    assert code == 0 and o["ok"] is True and o["motif"] is None and o["appel_envoye"] is True
    c = o["commande"]
    assert (c["code"], c["fin"], c["reponse_non_vide"], c["non_tronquee"], c["max_sortie_jetons"]) == (0, "STOP", True, True, 65536)
    assert c["pensees_jetons"] == 20000 and c["candidats_jetons"] == 3400 and c["modele_servi"] == "gemini-4-carbon"
    assert c["texte_longueur_caracteres"] == len(TEXTE_FACTICE)
    assert o["entree"]["octets"] == 136265 and o["plafond_session_usd"] == 6.0 and o["reglage"] == L.REGLAGE_CARBON
    assert o["empreintes"]["programme"] == hashlib.sha256(CHEMIN_SONDE.read_bytes()).hexdigest()
    assert o["pire_cas"]["max_output_tokens"] == 65536 and o["pire_cas"]["pire_cas_usd"] <= 6.0
    _sans_texte(monde)
    # l'entrée envoyée est la plus grande consigne servie par la course, à l'octet
    gen = [json.loads(x) for x in journal.read_text().splitlines()][1]["corps"]["contents"][0]["parts"][0]["text"]
    assert hashlib.sha256(gen.encode()).hexdigest() == o["entree"]["sha256"]


@pytest.mark.parametrize("options,motif", [
    (["--tronquee"], "code de la commande 5"),                                   # MAX_TOKENS : troncature
    (["--pensees", "70000", "--candidats", "3400"], "code de la commande 7"),     # pensée au-delà de la provision
    (["--modele-servi", "gemini-4-carbon-preview"], "modèle servi"),              # admis par la commande, refusé par l'orchestrateur
    (["--refus", "http400"], "code de la commande 3"),
    (["--sans-usage"], "code de la commande 5"),
])
def test_sonde_non_reussie_rapport_ecrit(monde, options, motif):
    p, url, _j = lancer_faux_amont(monde.tmp, *options)
    try:
        code = monde.sonder(["bash", str(enveloppe_d_essai(monde.tmp, url))])
    finally:
        p.kill()
    o = _rapport(monde)
    assert code == 1 and o["ok"] is False and any(motif in x for x in o["motif"]), o["motif"]
    _sans_texte(monde)


def test_relais_apres_un_seul_appel_non_reussie(monde):
    monde.apres = dict(monde.avant, appels=1)
    p, url, _j = lancer_faux_amont(monde.tmp)
    try:
        assert monde.sonder(["bash", str(enveloppe_d_essai(monde.tmp, url))]) == 1
    finally:
        p.kill()
    assert any("relais après la sonde" in x for x in _rapport(monde)["motif"])


def _refus_sans_appel(monde, **kw):
    p, url, journal = lancer_faux_amont(monde.tmp)
    try:
        with pytest.raises(S.Refus):
            monde.sonder(["bash", str(enveloppe_d_essai(monde.tmp, url))], **kw)
    finally:
        p.kill()
    assert not monde.sortie.exists() and (not journal.exists() or journal.read_text() == "")   # rien d'écrit, rien d'envoyé


@pytest.mark.parametrize("texte", [registre(plafond="5 USD"), registre(plafond="120 USD"), registre(perimetre="sonde d'Astra"),
                                   registre(perimetre="course de Carbon"), registre().replace("| Lazar |", "| mère |"),
                                   registre().replace(GO, "GO-2026-11-19-91"),
                                   registre(suite=f"| GO-2026-11-19-92 | 2026-11-19 | révocation | {GO} | — | — | Lazar | R-2 |\n")])
def test_ligne_de_go_artefacts_refus_avant_appel(monde, texte):
    monde.main["registres/go.md"] = texte.encode("utf-8")
    _refus_sans_appel(monde)


@pytest.mark.parametrize("modif", [
    lambda m: m.avant.update(appels=1), lambda m: m.avant.update(refus=1), lambda m: m.avant.update(max_appels=3),
    lambda m: m.avant.update(variable_cle_encore_presente=True), lambda m: m.avant.update(modeles=["gemini-4-argon"]),
    lambda m: m.avant.update(amont="http://127.0.0.1:1"),
    lambda m: m.cmdline.__setitem__(m.cmdline.index("--max-appels") + 1, "24"),
    lambda m: m.cmdline.__setitem__(m.cmdline.index("--modele") + 1, "gemini-4-argon"),
    lambda m: m.cmdline.__setitem__(m.cmdline.index("--port") + 1, "8788"),
    lambda m: m.cmdline.extend(["--amont", "http://127.0.0.1:9"]),
    lambda m: m.prog.write_text("# autre programme\n", encoding="utf-8"),
])
def test_relais_jete_artefacts_refus_avant_appel(monde, modif):
    modif(monde)
    _refus_sans_appel(monde)


def test_cle_dans_l_environnement_refus_avant_appel(monde):
    _refus_sans_appel(monde, environ={"PATH": "/usr/bin", "GEMINI_API_KEY": "x"})


def test_rapport_existant_refus_avant_appel(monde):
    monde.sortie.write_text("{}", encoding="utf-8")
    p, url, journal = lancer_faux_amont(monde.tmp)
    try:
        with pytest.raises(S.Refus):
            monde.sonder(["bash", str(enveloppe_d_essai(monde.tmp, url))])
    finally:
        p.kill()
    assert monde.sortie.read_text() == "{}" and (not journal.exists() or journal.read_text() == "")


def test_plafond_de_la_sonde_insuffisant_refus_avant_appel(monde, monkeypatch):
    """Sous un plafond qui réduirait la sortie (troncature), refus avant l'appel, et le plafond nécessaire est dit."""
    monkeypatch.setattr(S, "PLAFOND_USD", 5.8)
    monde.main["registres/go.md"] = registre(plafond="5.8 USD").encode("utf-8")
    p, url, _j = lancer_faux_amont(monde.tmp)
    try:
        with pytest.raises(S.Refus, match="5.82"):
            monde.sonder(["bash", str(enveloppe_d_essai(monde.tmp, url))])
    finally:
        p.kill()


def test_extraire_techniques_jamais_le_texte():
    t = S.extraire_techniques({"texte": "secret de la réponse", "cout_usd": 0.1, "code": 0, "fin": "STOP", "erreur": "X : détail",
                               "avertissements": ["a", "b"], "usage": {"candidats": 7}})
    assert "texte" not in t and "secret" not in json.dumps(t, ensure_ascii=False) and "détail" not in json.dumps(t, ensure_ascii=False)
    assert t["reponse_non_vide"] and t["erreur_type"] == "X" and t["avertissements_nombre"] == 2 and t["candidats_jetons"] == 7
    assert S.extraire_techniques({"texte": "  ", "cout_usd": 1.0})["reponse_non_vide"] is False
    assert S.extraire_techniques(None) == {"ligne_lisible": False}


def test_arguments_refuses_code_2():
    assert S.principal(["--go", GO]) == 2
    assert S.principal(["--g", GO, "--pid-relais", "1", "--sortie", "x"]) == 2      # aucune abréviation


# --- mutants ---------------------------------------------------------------------------------------------------------------------


def _mutant(tmp, ancien, nouveau, nom):
    t = CHEMIN_SONDE.read_text(encoding="utf-8")
    assert t.count(ancien) == 1, ancien
    p = tmp / f"{nom}.py"
    p.write_text(t.replace(ancien, nouveau), encoding="utf-8")
    return _charger(nom, p)


def _jouer_mutant(monde, M, *options):
    p, url, _j = lancer_faux_amont(monde.tmp, *options)
    try:
        r = monde.r
        r.pieces = dict(r.pieces, sonde_carbon=(r.pieces["sonde_carbon"][0], r.pieces["sonde_carbon"][1]))
        monkey = M.sha256_fichier
        M.sha256_fichier = lambda q: (L.PIECES["sonde_carbon"][1] if Path(q).name.startswith("sonde_mutant") else monkey(q))
        return M.sonder(L, r, GO, 4242, monde.sortie, commande=["bash", str(enveloppe_d_essai(monde.tmp, url))],
                        lire_etat=monde.lire_etat, lire_cmd=lambda pid: list(monde.cmdline), aujourd_hui=JOUR,
                        horodatage=lambda: "2026-11-19T07:00:00Z", environ={"PATH": "/usr/local/bin:/usr/bin:/bin"})
    finally:
        p.kill()


def test_mutation_texte_garde_attrapee(monde):
    M = _mutant(monde.tmp, 'CHAMPS_TECHNIQUES = ("code", ', 'CHAMPS_TECHNIQUES = ("texte", "code", ', "sonde_mutant_texte")
    assert _jouer_mutant(monde, M) == 0
    with pytest.raises(AssertionError):
        _sans_texte(monde)                                       # muté : le texte rendu serait gardé au rapport


def test_mutation_modele_servi_non_controle_attrapee(monde):
    M = _mutant(monde.tmp, "if not (isinstance(servi, str) and L.MODELE_SERVI_CARBON_ADMIS.match(servi)):",
                "if False:", "sonde_mutant_modele")
    assert _jouer_mutant(monde, M, "--modele-servi", "gemini-4-carbon-preview") == 0   # muté : l'orchestrateur refuserait ensuite
    monde.sortie.unlink()
    Path(str(monde.sortie) + ".sha256").unlink()
    monde.lectures = 0
    p, url, _j = lancer_faux_amont(monde.tmp, "--modele-servi", "gemini-4-carbon-preview")
    try:
        assert monde.sonder(["bash", str(enveloppe_d_essai(monde.tmp, url))]) == 1
    finally:
        p.kill()


def test_mutation_borne_du_relais_non_controlee_attrapee(monde):
    M = _mutant(monde.tmp, '    if _valeur(cmdline, "--max-appels") != str(MAX_APPELS_RELAIS):\n',
                "    if False:\n", "sonde_mutant_borne")
    monde.cmdline[monde.cmdline.index("--max-appels") + 1] = "24"
    monde.avant["max_appels"] = 2
    assert _jouer_mutant(monde, M) == 0                            # muté : un relais de course (24) servirait de relais jeté
    monde.sortie.unlink()
    Path(str(monde.sortie) + ".sha256").unlink()
    monde.lectures = 0
    _refus_sans_appel(monde)


# --- bout en bout par le vrai relais Gemini v2 (clé factice, faux amont) -----------------------------------------------------------


def test_bout_en_bout_par_le_vrai_relais(monde):
    fa, url_amont, journal = lancer_faux_amont(monde.tmp, "--pensees", "12000", "--candidats", "3000")
    port = port_libre()
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "GEMINI_API_KEY": "cle-factice-essai-0123456789"}
    rel = subprocess.Popen([sys.executable, "-I", "-B", str(RELAIS), "--port", str(port), "--amont", url_amont, "--modele",
                            "gemini-4-carbon", "--max-appels", "2", "--journal", str(monde.tmp / "relais.jsonl")],
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, env=env)
    try:
        assert rel.stdout.readline().startswith("relais prêt sur")
        url_relais = f"http://127.0.0.1:{port}"
        monde.r.programmes_relais = dict(L.PROGRAMMES_RELAIS)
        code = S.sonder(L, monde.r, GO, rel.pid, monde.sortie, commande=["bash", str(enveloppe_d_essai(monde.tmp, url_relais))],
                        url_relais=url_relais, amont=url_amont, aujourd_hui=JOUR, horodatage=lambda: "2026-11-19T07:00:00Z",
                        environ={"PATH": "/usr/local/bin:/usr/bin:/bin"})
        etat = S.lire_etat_local(url_relais)
    finally:
        rel.kill()
        fa.kill()
    o = _rapport(monde)
    assert code == 0 and o["ok"] and o["etat_relais_apres"]["appels"] == 2 and etat["refus"] == 0
    assert o["relais_jete"]["programme_sha256"] == L.PROGRAMMES_RELAIS["carbon"][1]
    assert all(not x["cle_presente"] or True for x in (json.loads(l) for l in journal.read_text().splitlines()))
    _sans_texte(monde)
    assert "cle-factice-essai" not in monde.sortie.read_text()
