"""Essais du lanceur de la course d'affinage des idées des mentors (v4 : porte des relais persistants, registre dérivé, prix du jour, garde de crédit v4, constats de la contre-lecture de la v3) — relais et orchestrateur **simulés**, aucun appel réel,
aucun réseau, aucune clé. Chaque garde est essayée sur un cas sain et sur un artefact (R5)."""
import datetime as dt
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v4.py"
_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v4", CHEMIN_LANCEUR)
L = importlib.util.module_from_spec(_spec)
sys.modules["lancer_course_affinage_mentors_v4"] = L
_spec.loader.exec_module(L)

AUJOURD_HUI = dt.date(2026, 11, 18)

FAUX_V8 = r'''
import json, os, sys
ici = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
comp = json.load(open(os.path.join(ici, "comportement.json")))
a = sys.argv[1:]
conf = json.load(open(a[a.index("--course-2") + 1]))
sortie = a[a.index("--course-2") + 2]
if "--verifier-seulement" in a:
    print(json.dumps({"montant_requis_go_usd": comp.get("montant", conf["budget"]["plafond_usd"]), "generations": 1, "go": None,
                      "specification": {"conforme": comp.get("spec", True)}, "configuration_sha256": "f" * 64}))
    sys.exit(comp.get("code_verif", 0))
arrete = False
if comp.get("executer"):
    import signal, subprocess, time
    etat = {"stop": False}
    signal.signal(signal.SIGTERM, lambda n, f: etat.__setitem__("stop", True))
    subprocess.run(conf["fournisseurs"][comp["executer"]]["commande"], input=b"consigne", capture_output=True)
    for _ in range(100):
        if etat["stop"]:
            break
        time.sleep(0.1)
    arrete = etat["stop"]
g = os.path.join(sortie, "generation-1")
os.makedirs(g)
cons = [{"fournisseur": f, "role": r, "cout_usd": c, "etape": "x"} for f, r, c in comp["couts"]]
cons.append({"fournisseur": "claude", "role": "plafond-relais", "cout_usd": 0.0, "etape": "x"})
json.dump({"consommations": cons}, open(os.path.join(g, "consommations.json"), "w"))
json.dump({"etapes": {"proposition": "jouee", "passe_tableau": "retiree"}, "noeud": None, "arret": None,
           "budget": {"cumul_usd": sum(c for _, _, c in comp["couts"])}}, open(os.path.join(g, "manifeste-fin.json"), "w"))
json.dump({"f1": {}, "f2": {}}, open(os.path.join(g, "fiches.json"), "w"))
json.dump(sorted(os.environ), open(os.path.join(sortie, "env-noms.json"), "w"))
json.dump({"cases": len(conf["cases"]), "proposeurs": [p["etiquette"] for p in conf["proposeurs"]],
           "interdites": conf["etiquettes_interdites"], "fournisseurs": sorted(conf["fournisseurs"]), "argv": a},
          open(os.path.join(sortie, "vu.json"), "w"))
sys.exit(2 if arrete else comp.get("code", 0))
'''

FAUX_ADAPTATEURS = r'''
import json, os
def etat_bac_a_sable_detaille():
    ici = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    comp = json.load(open(os.path.join(ici, "comportement.json")))
    return {"actif": comp.get("bac", True), "proc_neuf": comp.get("bac", True), "motif": "faux bac (essai)"}
'''

COUTS_SAINS = [("claude", "prop-opus", 2.0), ("claude", "prop-fable", 5.0), ("claude", "aiguilleur", 4.0),
               ("claude", "juge-opus", 5.0), ("argon", "prop-argon", 4.0), ("argon", "juge-argon", 5.0)]


def sceller(chemin: Path) -> None:
    h = hashlib.sha256(chemin.read_bytes()).hexdigest()
    Path(str(chemin) + ".sha256").write_text(f"{h}  {chemin.name}\n", encoding="utf-8")


def ecrire_scelle(chemin: Path, contenu) -> Path:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    texte = contenu if isinstance(contenu, str) else json.dumps(contenu, ensure_ascii=False, indent=1)
    chemin.write_text(texte, encoding="utf-8")
    sceller(chemin)
    return chemin


def git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def faux_orchestrateur(tmp: Path, **comportement) -> tuple:
    o = tmp / "orchestrateur"
    (o / "demonstrations").mkdir(parents=True)
    (o / "pole").mkdir()
    (o / "demonstrations" / "ideation_v8.py").write_text(FAUX_V8, encoding="utf-8")
    (o / "pole" / "adaptateurs.py").write_text(FAUX_ADAPTATEURS, encoding="utf-8")
    (o / "pole" / "__init__.py").write_text("", encoding="utf-8")
    comportement.setdefault("couts", COUTS_SAINS)
    (o / "comportement.json").write_text(json.dumps(comportement), encoding="utf-8")
    git(o, "init", "-q", "-b", "main")
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "add", "-A")
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "-m", "faux")
    commit = subprocess.run(["git", "-C", str(o), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    empreintes = {rel: hashlib.sha256((o / rel).read_bytes()).hexdigest() for rel in ("demonstrations/ideation_v8.py", "pole/adaptateurs.py")}
    return o, commit, empreintes


from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading

FIXE = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
MODELES_CLAUDE = [e["modele"] for e in FIXE["especes"] if e["famille"] == "claude"]
CONTEXTE: dict = {}
PID_CLAUDE, PID_KIMI = 424242, 424243


def serveur(etat: dict) -> ThreadingHTTPServer:
    """Relais factice local : ne sert que GET /relais/etat (aucune clé, aucun amont)."""
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            corps = json.dumps(etat).encode()
            self.send_response(200 if self.path == "/relais/etat" else 404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(corps)

        def log_message(self, *a):
            pass
    s = ThreadingHTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s


def porte_commande(depot: Path, url: str, modeles: list) -> dict:
    return {"type": "commande", "delai_s": 10,
            "commande": [sys.executable, "-I", "-B", str(depot / L.PIECES["porte_plafond"][0]), "--url", url, "--modeles-permis",
                         ",".join(modeles), "--plafond-ligne", "150"]}


def declaration(depot: Path, **modifs) -> dict:
    url = CONTEXTE["url_claude"]
    porte = porte_commande(depot, url, MODELES_CLAUDE)
    d = {"version": "essai", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": url, "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "porte_plafond": porte,
                   "pid_relais": PID_CLAUDE},
        "argon": {"type": "commande_externe", "commande": ["bash", str(depot / L.PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_ESSAI_A", "porte_plafond": {"type": "environnement"}}}}
    d["fournisseurs"].update(modifs)
    return d


def releve(**cles) -> dict:
    base = {"RR_ANTHROPIC_API_KEY_MINUIT": {"credit_usd": 1000.0, "reste_usd": 900.0, "source": "essai"},
            "CLE_ESSAI_A": {"credit_usd": 1000.0, "reste_usd": 800.0, "source": "essai"}}
    base.update(cles)
    return {"releve_utc": "2026-11-18T07:00:00Z", "cles": base}


def contre_lecture(prereg_sha: str, lanceur_sha: str, verdict="Scellable.", suite="") -> str:
    return (f"# Contre-lecture d'essai, par le modèle K\n\nPréenregistrement : {prereg_sha}\nLanceur : {lanceur_sha}\n\n"
            f"## Verdict\n\n**{verdict}**\n" + suite)


def ligne_go(plafond="150 USD", perimetre="course d'affinage des idées des mentors (organisme d'idéation)"):
    return (f"| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\n|---|---|---|---|---|---|---|---|\n"
            f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\n")


def releve_prix(**modifs) -> dict:
    prix = {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}
    prix.update(modifs)
    return {"releve_utc": "2026-11-18T06:55:00Z", "source": "essai : barème du relais", "prix": prix}


@pytest.fixture
def monde(tmp_path):
    """Dépôt d'essai : vraies pièces copiées (mêmes empreintes que les épingles), faux orchestrateur, relais simulés."""
    depot = tmp_path / "depot"
    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, depot / rel)
    prereg = depot / L.PREREG
    shutil.copy2(RACINE / L.PREREG, prereg)
    sceller(prereg)
    etat_claude = {"plafond_usd": 150.0, "depense_usd": 0.0, "appels": 0, "modeles_permis": list(MODELES_CLAUDE)}
    etat_kimi = {"plafond_usd": 6.0, "depense_usd": 0.0, "appels": 0, "modeles_permis": ["kimi-k3.1-pro"]}
    s_claude, s_kimi = serveur(etat_claude), serveur(etat_kimi)
    CONTEXTE.update(url_claude=f"http://127.0.0.1:{s_claude.server_address[1]}", url_kimi=f"http://127.0.0.1:{s_kimi.server_address[1]}")
    progs = tmp_path / "progs"
    progs.mkdir()
    (progs / "relais_reel.py").write_text("# relais factice\n", encoding="utf-8")
    (progs / "relais_kimi_v4.py").write_text("# relais factice kimi\n", encoding="utf-8")
    cmdlines = {PID_CLAUDE: [sys.executable, "-I", "-B", str(progs / "relais_reel.py"), "--variable-cle", "RR_ANTHROPIC_API_KEY_MINUIT",
                             "--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "150", "--modeles-permis",
                             ",".join(MODELES_CLAUDE)],
                PID_KIMI: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--variable-cle", "CLE_ESSAI_K",
                           "--port", CONTEXTE["url_kimi"].rsplit(":", 1)[1], "--plafond-usd", "6"]}
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    lanceur_sha = hashlib.sha256(CHEMIN_LANCEUR.read_bytes()).hexdigest()
    ecrire_scelle(depot / L.CONTRE_LECTURE, contre_lecture(L.PREREG_SHA256, lanceur_sha))
    ecrire_scelle(depot / L.DECLARATION_RELAIS, declaration(depot))
    ecrire_scelle(depot / L.RELEVE_CREDITS, releve())
    ecrire_scelle(depot / L.RELEVE_PRIX, releve_prix())
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text(ligne_go(), encoding="utf-8")
    r = L.Reglages(depot=depot, orchestrateurs=(o,), commit_orchestrateur=commit, empreintes_orchestrateur=empreintes,
                   pieces=dict(L.PIECES), prereg=(prereg, L.PREREG_SHA256), contre_lecture=depot / L.CONTRE_LECTURE,
                   declaration=depot / L.DECLARATION_RELAIS, releve=depot / L.RELEVE_CREDITS,
                   registre_go=depot / "registres" / "go.md", procedure_relais=depot / L.PROCEDURE_RELAIS,
                   releve_prix=depot / L.RELEVE_PRIX, dossier_runs=depot / "runs", dossier_sorties=tmp_path / "sorties",
                   depot_attendu_par_l_enveloppe=depot, python=sys.executable, lanceur=CHEMIN_LANCEUR, moteur="reel",
                   environnement={"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "RR_ANTHROPIC_API_KEY_MINUIT": "valeur-secrete-essai-1",
                                  "RR_ANTHROPIC_API_KEY_RIGAUD": "valeur-secrete-essai-2"},
                   aujourd_hui=AUJOURD_HUI, horodatage=lambda: "Wed Nov 18 07:00:00 UTC 2026",
                   sorties_courses=tuple(tmp_path / f"sorties-anciennes-v{k}" for k in (1, 2, 3, 4)),
                   programmes_relais={"claude": ("relais_reel.py", hashlib.sha256((progs / "relais_reel.py").read_bytes()).hexdigest()),
                                      "kimi": ("relais_kimi_v4.py", hashlib.sha256((progs / "relais_kimi_v4.py").read_bytes()).hexdigest())},
                   lire_cmdline=lambda pid: list(cmdlines[pid]))
    yield {"r": r, "tmp": tmp_path, "depot": depot, "orch": o, "lanceur_sha": lanceur_sha, "etat_claude": etat_claude,
           "etat_kimi": etat_kimi, "cmdlines": cmdlines}
    s_claude.shutdown()
    s_kimi.shutdown()


def lancer(r):
    return L.principal([], reglages=r)


def un_run(r):
    runs = [p for p in r.dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]
    assert len(runs) == 1
    return runs[0]


def remplacer_orchestrateur(m, **comportement):
    shutil.rmtree(m["orch"])
    o, commit, empreintes = faux_orchestrateur(m["tmp"], **comportement)
    m["r"].orchestrateurs, m["r"].commit_orchestrateur, m["r"].empreintes_orchestrateur = (o,), commit, empreintes


# --- bout en bout (cas sain de toutes les gardes) ------------------------------------------------------------------------------


def test_bout_en_bout_sain_manifestes_couts_ecart(monde):
    r = monde["r"]
    assert lancer(r) == 0
    run = un_run(r)
    for nom in ("manifeste-lanceur-depart.json", "manifeste-lanceur-fin.json", "acte-de-gel.md", "configuration-orchestrateur.json"):
        assert L.scelle(run / nom), nom
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    # (4) R9 : configuration et empreinte, graines, versions, commit
    assert dep["configuration"]["sha256"] == L.sha256_fichier(run / "configuration-orchestrateur.json")
    assert dep["graines"]["racine"] == 2026111814 and "SeedSequence" in dep["graines"]["regle"]
    assert dep["versions"]["numpy"] and dep["versions"]["python"]
    assert "commit" in dep["depot_travail"] and dep["orchestrateur"]["commit"] == r.commit_orchestrateur
    assert dep["preenregistrement"]["sha256"] == L.PREREG_SHA256 and dep["go"]["plafond_lu"] == 150.0
    # espèces : Claude et Argon seuls déclarés → Kimi, Astra absentes ; Carbon non active
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon"]
    assert dep["carbon"]["active"] is False
    # (5) coût réel par relais, écart au devis
    assert fin["cout_reel"]["par_relais_usd"] == {"claude": 16.0, "argon": 9.0}
    assert fin["ecart_au_devis_v5"]["par_role"]["prop-opus"]["devis_usd"] == pytest.approx(0.141)
    assert fin["releve_credits_apres"]["RR_ANTHROPIC_API_KEY_MINUIT"]["reste_estime_usd"] == pytest.approx(884.0)
    assert fin["alertes_apres"] == [] and fin["plafond_arret"]["depasse"] is False
    # l'orchestrateur a reçu seize cases, les retraits en étiquettes interdites, aucun nom de clé dans son environnement
    vu = json.loads((Path(dep["sortie"]) / "vu.json").read_text())
    assert vu["cases"] == 16 and "S3" in vu["interdites"] and "fc62b4ca23035" in vu["interdites"]
    assert "--confirmer-moteur-reel" in vu["argv"] and "--registre-go" in vu["argv"]
    noms = json.loads((Path(dep["sortie"]) / "env-noms.json").read_text())
    assert "RR_ANTHROPIC_API_KEY_MINUIT" not in noms and "RR_ANTHROPIC_API_KEY_RIGAUD" not in noms and "GO_ID" in noms
    # aucune valeur de clé écrite nulle part
    for p in list(run.iterdir()) + list(Path(dep["sortie"]).parent.rglob("*")):
        if p.is_file():
            assert "valeur-secrete-essai" not in p.read_text(errors="replace"), p


def test_course_deja_lancee_refusee(monde):
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2


# --- (1) plafond d'arrêt -----------------------------------------------------------------------------------------------------


def test_go_plafond_autre_refuse(monde):
    monde["r"].registre_go.write_text(ligne_go("140 USD"), encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_go_autre_perimetre_refuse(monde):
    monde["r"].registre_go.write_text(ligne_go(perimetre="collisionneur"), encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_configuration_fixe_sain_et_artefacts():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    L.garde_configuration_fixe(fixe)
    for modif in (lambda f: f["budget"].__setitem__("plafond_usd", 151.0),
                  lambda f: f["budget"]["etapes"][3].__setitem__("plafond_relais_usd", 100.0),
                  lambda f: f["budget"]["etapes"][0].__setitem__("plafond_relais_usd", 120.0),
                  lambda f: f.__setitem__("etage_tests_de_mort", {"nombre": 1}),
                  lambda f: f.__setitem__("generations", 2)):
        f = json.loads(json.dumps(fixe))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_configuration_fixe(f)


def test_verification_orchestrateur_montant_autre_refuse(monde):
    remplacer_orchestrateur(monde, montant=140.0)
    assert lancer(monde["r"]) == 2
    assert not (un_run(monde["r"]) / "manifeste-lanceur-depart.json").exists()


def test_specification_non_conforme_refusee(monde):
    remplacer_orchestrateur(monde, spec=False)
    assert lancer(monde["r"]) == 2


def test_cumul_au_dela_du_plafond_alerte_code_4(monde):
    remplacer_orchestrateur(monde, couts=[("claude", "prop-opus", 100.0), ("argon", "juge-argon", 51.0)])
    assert lancer(monde["r"]) == 4
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-credits-apres.json")
    assert json.loads((run / "manifeste-lanceur-fin.json").read_text())["plafond_arret"]["depasse"] is True


# --- (2) crédits ---------------------------------------------------------------------------------------------------------------


def _releve(monde, objet):
    p = monde["r"].releve
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    ecrire_scelle(p, objet)


def test_credit_non_lisible_sans_dispense_refuse(monde):
    _releve(monde, releve(CLE_ESSAI_A={"non_lisible": True, "motif": "interface fermée"}))
    assert lancer(monde["r"]) == 2


def test_credit_non_lisible_avec_dispense_part(monde):
    objet = releve(CLE_ESSAI_A={"non_lisible": True, "motif": "interface fermée"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["releve_credits_avant"]["cles"]["CLE_ESSAI_A"]["lisible"] is False


def test_credit_sous_un_cinquieme_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"credit_usd": 5000.0, "reste_usd": 900.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3
    alertes = [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith("-alerte-credits-affinage-mentors-v4")]
    assert len(alertes) == 1 and L.scelle(alertes[0] / "alerte-credits-avant.json")
    assert not [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]
    _releve(monde, releve())
    assert lancer(monde["r"]) == 0  # l'alerte ne bloque pas une course une fois la clé rechargée


def test_credit_sous_le_plafond_alerte_code_3(monde):
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": 160.0, "reste_usd": 149.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3


def test_releve_perime_refuse(monde):
    objet = releve()
    objet["releve_utc"] = "2026-11-17T23:00:00Z"
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def test_releve_cle_omise_refuse(monde):
    objet = releve()
    del objet["cles"]["CLE_ESSAI_A"]
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def test_alerte_apres_si_reste_estime_sous_le_seuil(monde):
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": 1000.0, "reste_usd": 205.0, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["alertes_apres"] and fin["alertes_apres"][0]["cle"] == "CLE_ESSAI_A"
    assert L.scelle(run / "alerte-credits-apres.json")


# --- (3) préenregistrement, contre-lecture, retraits ----------------------------------------------------------------------------


def test_preenregistrement_autre_empreinte_refuse(monde):
    p = monde["r"].prereg[0]
    p.write_text(p.read_text() + "\nun octet de plus\n", encoding="utf-8")
    sceller(p)
    assert lancer(monde["r"]) == 2


def test_preenregistrement_non_scelle_refuse(monde):
    Path(str(monde["r"].prereg[0]) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2


def _cl(monde, texte):
    c = monde["r"].contre_lecture
    c.unlink()
    Path(str(c) + ".sha256").unlink()
    ecrire_scelle(c, texte)


def test_contre_lecture_absente_refusee(monde):
    monde["r"].contre_lecture.unlink()
    assert lancer(monde["r"]) == 2


def test_contre_lecture_defavorable_refusee(monde):
    for verdict in ("Scellable après corrections.", "Non scellable.", "Scellable sous réserve."):
        _cl(monde, contre_lecture(L.PREREG_SHA256, monde["lanceur_sha"], verdict))
        assert lancer(monde["r"]) == 2, verdict


def test_contre_lecture_qui_ne_cite_pas_le_lanceur_refusee(monde):
    _cl(monde, contre_lecture(L.PREREG_SHA256, "0" * 64))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_non_scellee_refusee(monde):
    Path(str(monde["r"].contre_lecture) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2


def test_verdicts():
    assert L.verdict_favorable("**Scellable.**") and L.verdict_favorable("Scellable.")
    for v in ("**Scellable après corrections.**", "Non scellable.", "Scellable sous réserve", "", None, "À sceller",
              "Scellable : rien à corriger", "Scellable", "Scellable. Deux remarques."):
        assert not L.verdict_favorable(v), v


def test_liste_sain_et_entree_servie_dans_les_retraits():
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    c = L.verifier_liste(liste)
    assert c["fils"] == 16 and len(c["idees_retirees"]) == 14
    art = json.loads(json.dumps(liste))
    art["fils"][0]["idees_servies"].append({"numero": "S3", "texte_servi": "x"})
    with pytest.raises(L.Refus):
        L.verifier_liste(art)
    art = json.loads(json.dumps(liste))
    art["fils"][0]["idees_servies"][0]["texte_servi"] += " fe2f9cb3b665c"
    with pytest.raises(L.Refus):
        L.verifier_liste(art)


def test_piece_modifiee_refusee(monde):
    p = monde["depot"] / L.PIECES["consigne_juge"][0]
    p.write_text(p.read_text() + " ", encoding="utf-8")
    assert lancer(monde["r"]) == 2


# --- déclaration des relais, Carbon ---------------------------------------------------------------------------------------------


def _decl(monde, objet):
    p = monde["r"].declaration
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    ecrire_scelle(p, objet)


def test_declaration_valeur_de_cle_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "sk-ant-" + "a" * 30
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_declaration_sans_claude_refusee(monde):
    d = declaration(monde["depot"])
    del d["fournisseurs"]["claude"]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_declaration_adresse_hors_boucle_locale_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["url_relais"] = "http://10.0.0.5:8787"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_declaration_commande_argon_autre_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"] = ["bash", "/tmp/autre.sh"]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def epingler(monkeypatch, nom: str, script: Path) -> None:
    """Essais seulement : épingle une commande d'essai d'Astra ou de Carbon (la table du lanceur est vide en v4)."""
    monkeypatch.setitem(L.COMMANDES_EPINGLEES, nom, {"essai": hashlib.sha256(script.read_bytes()).hexdigest()})


def script_commande(dossier: Path, nom: str, ligne: dict) -> Path:
    script = dossier / f"{nom}.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps(" + repr(ligne) + "))\n", encoding="utf-8")
    return script


def test_carbon_sans_inscription_inactive_et_avec_inscription_active(tmp_path, monkeypatch):
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    r = L.Reglages.production()
    CONTEXTE.setdefault("url_claude", "http://127.0.0.1:18787")
    sc = script_commande(tmp_path, "carbon", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "carbon", sc)
    carbon = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(sc)], "modele_propose": "modele-essai-carbon", "nom_cle": "CLE_ESSAI_G",
              "porte_plafond": {"type": "environnement"}}
    d = L.verifier_declaration(declaration(r.depot, carbon=dict(carbon)), fixe, r)
    assert d["carbon"]["active"] is False and "carbon" not in d["fournisseurs"]
    d = L.verifier_declaration(declaration(r.depot, carbon=dict(carbon, inscription="R-3217")), fixe, r)
    assert d["carbon"]["active"] is True and d["cles"]["carbon"] == "CLE_ESSAI_G"
    assert [e["etiquette"] for e in d["especes_actives"]][-1] == "prop-carbon"
    d = L.verifier_declaration(declaration(r.depot), fixe, r)
    assert d["carbon"]["active"] is False and "non nommés" in d["carbon"]["motif"]
    with pytest.raises(L.Refus):
        L.verifier_declaration(declaration(r.depot, carbon=dict(carbon, inscription="R-3217", modele_propose="modele-autre")), fixe, r)


def test_espece_kimi_declaree_active(monde):
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde)))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-kimi" in dep["especes_actives"] and dep["cles_employees"]["kimi"] == "CLE_ESSAI_K"


# --- orchestrateur, bac à sable ---------------------------------------------------------------------------------------------------


def test_orchestrateur_modifie_refuse(monde):
    (monde["orch"] / "non-suivi.txt").write_text("x", encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_orchestrateur_autre_commit_refuse(monde):
    monde["r"].commit_orchestrateur = "0" * 40
    assert lancer(monde["r"]) == 2


def test_bac_a_sable_inactif_refuse(monde):
    remplacer_orchestrateur(monde, bac=False)
    assert lancer(monde["r"]) == 2


def test_arguments_refuses():
    assert L.principal(["--autre"]) == 2


# --- liste des fils : reconstruite par programme depuis le relevé, si `main` est là ------------------------------------------------


def test_liste_reconstruite_identique(tmp_path):
    p = subprocess.run(["git", "-C", str(RACINE), "show", "origin/main:" + "docs/notes/quatre-lectures-inventaire-v1/mentors-releve-d-ensemble-v1.md"],
                       capture_output=True)
    if p.returncode != 0:
        pytest.skip("relevé d'ensemble non disponible (origin/main non récupéré)")
    releve_ = tmp_path / "releve.md"
    releve_.write_bytes(p.stdout)
    sortie = tmp_path / "liste.json"
    q = subprocess.run([sys.executable, "-I", "-B", str(RACINE / "scripts" / "construire_fils_course_affinage_mentors_v1.py"),
                        str(releve_), str(sortie)], capture_output=True, text=True)
    assert q.returncode == 0, q.stderr
    assert hashlib.sha256(sortie.read_bytes()).hexdigest() == L.PIECES["liste_fils"][1]


# --- (1) plafond d'arrêt, sur le vrai orchestrateur (moteur simulé, appels fictifs chers) ----------------------------------------


def test_plafond_arret_coupe_la_course_avant_150_vrai_orchestrateur_simule(monde):
    """Artefact R5 de la garde (1) : chaque appel simulé coûte jusqu'à 1 USD (fictif, borné par le plafond de session) ; quatre
    espèces : proposition 64, aiguillage 32 ; les juges ne reçoivent qu'un plafond dur de 54 USD (150 − 96), sont coupés,
    la course s'arrête en nœud ; le cumul ne dépasse pas 150 et le lanceur écrit ce qui a été fait. Sauté si l'orchestrateur
    épinglé n'est pas sur cette machine."""
    presents = [o for o in L.ORCHESTRATEURS_CANDIDATS if (o / L.LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        pytest.skip("orchestrateur épinglé absent")
    r, depot = monde["r"], monde["depot"]
    conf = depot / L.PIECES["configuration"][0]
    fixe = json.loads(conf.read_text())
    fixe["simulation"]["cout_par_appel_usd"] = 1.0
    conf.write_text(json.dumps(fixe, ensure_ascii=False), encoding="utf-8")
    r.pieces = dict(r.pieces, configuration=(L.PIECES["configuration"][0], L.sha256_fichier(conf)))
    r.orchestrateurs, r.commit_orchestrateur = tuple(presents), L.COMMIT_ORCHESTRATEUR
    r.empreintes_orchestrateur = dict(L.EMPREINTES_ORCHESTRATEUR)
    r.moteur, r.verifier_go, r.exiger_bac_a_sable = "simule", False, False
    kimi = {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:18788", "modele": "kimi-k3.1-pro", "prix_entree": 1.0,
            "prix_sortie": 2.0, "max_sortie_jetons": 1000, "sortie_min_jetons": 100, "delai_s": 60, "nom_cle": "CLE_ESSAI_K",
            "porte_plafond": {"type": "commande", "commande": ["/bin/true"], "delai_s": 5}}
    _decl(monde, declaration(depot, kimi=kimi))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
    assert lancer(r) == 2  # nœud de l'orchestrateur : code 2, manifeste de fin écrit
    fin = json.loads((un_run(r) / "manifeste-lanceur-fin.json").read_text())
    fait = fin["ce_qui_a_ete_fait"]
    assert fait["etapes"]["proposition"] == "jouee" and fait["etapes"]["aiguillage"] == "jouee"
    assert fait["etapes"]["juges"] == "non_mesuree_budget" and fait["noeud"]
    assert fin["cout_reel"]["total_usd"] <= 150.0 and fin["plafond_arret"]["depasse"] is False
    assert fin["cout_reel"]["coupures"] == ["juges"]
    assert not subprocess.run(["git", "-C", str(presents[0]), "status", "--porcelain", "--ignored"], capture_output=True,
                              text=True).stdout.strip()


# --- v2 : clé Minuit, Rigaud exclue, contre-lecture du modèle K ----------------------------------------------------------------


def test_variable_minuit_absente_arret_au_depart(monde):
    r = monde["r"]
    r.environnement = {k: v for k, v in r.environnement.items() if k != L.CLE_CLAUDE}
    assert lancer(r) == 2
    assert not r.dossier_runs.exists()
    r.environnement[L.CLE_CLAUDE] = "x"  # cas sain : présente par son nom
    assert lancer(r) == 0


def test_relais_claude_sur_rigaud_refuse(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_RIGAUD"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_relais_claude_sur_une_autre_cle_refuse(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_3"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_cle_claude_sur_un_autre_relais_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_MINUIT"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_configuration_cles_sain_et_artefacts():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    L.garde_cles_configuration(fixe)
    for modif in (lambda f: f["cles"].__setitem__("claude", "RR_ANTHROPIC_API_KEY_RIGAUD"),
                  lambda f: f.__setitem__("cles_interdites", []),
                  lambda f: f["especes"][1].__setitem__("cle", "RR_ANTHROPIC_API_KEY_RIGAUD")):
        f = json.loads(json.dumps(fixe))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_cles_configuration(f)


def test_minuit_non_lisible_compte_au_prix_releve(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"non_lisible": True, "depense_anterieure_usd": 0.0}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["reste_usd"] == 200.0 and "compté" in c["source"]
    assert dep["cle_par_espece"]["prop-opus"] == L.CLE_CLAUDE and dep["cle_par_role_interne"]["aiguilleur"] == L.CLE_CLAUDE


def test_minuit_compte_sous_le_plafond_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"non_lisible": True, "depense_anterieure_usd": 60.0}))
    assert lancer(monde["r"]) == 3


def test_minuit_non_lisible_sans_depense_anterieure_refuse(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"non_lisible": True}))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_qui_dit_n_avoir_pas_relu_refusee(monde):
    _cl(monde, contre_lecture(L.PREREG_SHA256, monde["lanceur_sha"], suite="\nLimite : je n'ai pas relu le lanceur en entier.\n"))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_sans_modele_k_refusee(monde):
    _cl(monde, contre_lecture(L.PREREG_SHA256, monde["lanceur_sha"]).replace("par le modèle K", "par un relecteur"))
    assert lancer(monde["r"]) == 2


def test_course_v1_deja_lancee_bloque_la_v2(monde):
    d = monde["r"].dossier_runs / "20261118-000000-course-affinage-mentors-v1"
    d.mkdir(parents=True)
    (d / "manifeste-lanceur-depart.json").write_text("{}", encoding="utf-8")
    assert lancer(monde["r"]) == 2


# --- v3 : règle de clé par part, Kimi, dispense R-3237, arrêt au premier refus pour crédit, procédure des relais ----------------

KIMI = {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:18788", "modele": "kimi-k3.1-pro", "prix_entree": 1.0,
        "prix_sortie": 2.0, "max_sortie_jetons": 1000, "sortie_min_jetons": 100, "delai_s": 60, "nom_cle": "CLE_ESSAI_K",
        "porte_plafond": {"type": "commande", "commande": ["PROCEDURE"], "delai_s": 5}}


def kimi(monde, **prix):
    k = dict(KIMI, **prix)
    k["url_relais"] = CONTEXTE["url_kimi"]
    k["pid_relais"] = PID_KIMI
    k["porte_plafond"] = porte_commande(monde["depot"], CONTEXTE["url_kimi"], ["kimi-k3.1-pro"])
    return k


def test_parts_au_pire(tmp_path, monkeypatch):
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    r = L.Reglages.production()
    CONTEXTE.setdefault("url_claude", "http://127.0.0.1:18787")
    pieces = {n: {"absolu": str(RACINE / rel)} for n, (rel, _) in L.PIECES.items()}
    sa = script_commande(tmp_path, "astra", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "astra", sa)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(sa)], "modele_propose": "modele-essai-astra", "nom_cle": "CLE_ESSAI_S",
             "porte_plafond": {"type": "environnement"}}
    k = dict(KIMI, prix_entree=10.0, prix_sortie=20.0, max_sortie_jetons=40000)
    d = L.verifier_declaration(declaration(r.depot, kimi=k, astra=astra), fixe, r)
    parts = L.parts_au_pire(fixe, liste, pieces, d)
    assert parts["claude"]["part_au_pire_usd"] == 150.0 and parts["argon"]["part_au_pire_usd"] == 150.0
    assert parts["astra"]["part_au_pire_usd"] == 24.0
    entree = len((RACINE / L.PIECES["consigne_proposeur"][0]).read_bytes()) + max(
        len(L.texte_de_case(f).encode()) for f in liste["fils"]) + 200
    attendu = ((entree + 1024) * 10.0 + 40000 * 20.0) / 1e6
    assert parts["kimi"]["par_appel_usd"] == pytest.approx(attendu) and parts["kimi"]["part_au_pire_usd"] == pytest.approx(16 * attendu)


def test_kimi_part_et_course_suivante_sain_et_artefact(monde):
    # sain : 16 × (8949 × 1 + 50 000 × 20) / 1e6 ≈ 16,14 ; + 11,3 = 27,44 ≤ 0,9 × 32,25 = 29,03
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde, prix_sortie=20.0, max_sortie_jetons=50000)))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 32.25, "reste_usd": 32.25, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["parts_au_pire"]["kimi"]["part_au_pire_usd"] < 17.73


def test_kimi_part_trop_haute_refus_les_courses_se_suivent(monde, capsys):
    # artefact : 16 × (8949 + 55 000 × 20) / 1e6 ≈ 17,74 ; + 11,3 = 29,04 > 29,03
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde, prix_sortie=20.0, max_sortie_jetons=55000)))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 32.25, "reste_usd": 32.25, "source": "essai"}))
    assert lancer(monde["r"]) == 3
    assert "les deux courses doivent se suivre" in capsys.readouterr().err


def test_part_au_pire_et_non_plafond_global(monde, monkeypatch):
    # une clé d'Astra à 30 USD : sous 150 (v2 : refus) mais au-dessus de sa part au pire (24) et de son cinquième → départ
    script = monde["tmp"] / "astra.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': '', 'cout_usd': 0.01}))\n", encoding="utf-8")
    epingler(monkeypatch, "astra", script)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script)], "modele_propose": "modele-essai-astra",
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 30.0, "reste_usd": 30.0, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 30.0, "reste_usd": 23.0, "source": "essai"}))
    monde["r"].dossier_runs = monde["tmp"] / "runs-bis"
    assert lancer(monde["r"]) == 3


def test_dispense_autre_reference_refusee(monde):
    objet = releve(CLE_ESSAI_A={"non_lisible": True})
    objet["dispense"] = {"par": "mère", "reference": "R-9999", "cles": ["CLE_ESSAI_A"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def test_dispense_sur_une_cle_non_dispensable_refusee(monde):
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde)))
    objet = releve(CLE_ESSAI_K={"non_lisible": True})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_K"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def _astra_dispensee(monde, ligne, monkeypatch):
    script = monde["tmp"] / "astra.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps(" + repr(ligne) + "))\n", encoding="utf-8")
    epingler(monkeypatch, "astra", script)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script)], "modele_propose": "modele-essai-astra",
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    objet = releve(CLE_ESSAI_S={"non_lisible": True, "motif": "solde illisible (R-3222)"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S"]}
    _releve(monde, objet)
    remplacer_orchestrateur(monde, executer="astra")


def test_premier_refus_pour_credit_arrete_la_course_code_5(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "", "cout_usd": 0.01, "erreur": "HTTP 402 payment required : credit balance too low"}, monkeypatch)
    assert lancer(monde["r"]) == 5
    run = un_run(monde["r"])
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["arret_au_premier_refus_pour_credit"][0]["relais"] == "astra" and fin["code"] == 2
    assert L.scelle(run / "alerte-arret-credit.json")  # constat 12


def test_limite_de_debit_n_arrete_pas_la_course(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "", "cout_usd": 0.01, "erreur": "429 RESOURCE_EXHAUSTED: rate limit per minute"}, monkeypatch)
    assert lancer(monde["r"]) == 0


def test_appel_sans_refus_pour_credit_ne_s_arrete_pas(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "réponse", "cout_usd": 0.01, "modele_servi": "modele-essai-astra"}, monkeypatch)
    assert lancer(monde["r"]) == 0
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["arret_au_premier_refus_pour_credit"] == []


def test_garde_credit_v4_motifs():
    spec = importlib.util.spec_from_file_location("garde_v4", RACINE / "scripts" / "garde_credit_relais_v4.py")
    G = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G)
    j = lambda e: json.dumps({"texte": "", "cout_usd": 0.01, "erreur": e})  # noqa: E731
    for e in ("HTTP 402 payment required", "insufficient_quota: check your billing details", "crédits épuisés",
              "Your prepayment credits are depleted", "RESOURCE_EXHAUSTED: billing account quota", "credit balance is too low"):
        assert G.motif_credit(j(e), "", 1), e
    assert G.motif_credit("", "billing hard limit reached", 1)
    for e in ("429 RESOURCE_EXHAUSTED: rate limit per minute", "délai dépassé", "quota exceeded"):
        assert not G.motif_credit(j(e), "", 1), e
    assert not G.motif_credit(j(""), "appel en 402 ms", 1)
    assert not G.motif_credit(j(""), "note: billing metadata absent", 1)
    assert not G.motif_credit('{"texte": "ok", "cout_usd": 0.2}', "credit balance is too low", 0)  # code 0 : stderr non lue
    assert not G.motif_credit('{"texte": "une carte sur le crédit d\'une idée", "cout_usd": 0.2}', "", 0)


def _procedure(monde, objet=None, texte=None):
    p = monde["depot"] / L.PROCEDURE_RELAIS
    p.unlink()
    Path(str(p) + ".sha256").unlink(missing_ok=True)
    ecrire_scelle(p, texte if texte is not None else objet)


def test_procedure_a_remplir_refusee(monde):
    _procedure(monde, texte='{"chemin": "À REMPLIR", "sha256": "À REMPLIR"}')
    assert lancer(monde["r"]) == 2


def test_procedure_absente_refusee(monde):
    p = monde["depot"] / L.PROCEDURE_RELAIS
    p.unlink()
    assert lancer(monde["r"]) == 2


def test_procedure_autre_empreinte_refusee(monde):
    _procedure(monde, {"chemin": str(monde["tmp"] / "procedure-relais.sh"), "sha256": "0" * 64})
    assert lancer(monde["r"]) == 2


def test_porte_qui_ne_lance_pas_la_procedure_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["porte_plafond"]["commande"] = ["/bin/true"]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


# --- v4 : constats de la contre-lecture de la v3 ------------------------------------------------------------------------------


def _orch_present():
    presents = [o for o in L.ORCHESTRATEURS_CANDIDATS if (o / L.LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        pytest.skip("orchestrateur épinglé absent")
    return presents[0]


def _classe_porte():
    o = _orch_present()
    sys.path.insert(0, str(o))
    ancien, sys.dont_write_bytecode = sys.dont_write_bytecode, True  # l'arbre de l'orchestrateur reste propre
    try:
        from pole.adaptateurs_v56 import PortePlafondCommande, RelaisSansPlafond
    finally:
        sys.path.remove(str(o))
        sys.dont_write_bytecode = ancien
    return PortePlafondCommande, RelaisSansPlafond


def test_porte_avec_la_vraie_classe_de_l_orchestrateur_sain_et_artefacts(monde):
    """Constat 1, R5 : la porte épinglée rejouée par `PortePlafondCommande` (classe réelle), relais factice local."""
    Porte, RelaisSansPlafond = _classe_porte()
    c = porte_commande(monde["depot"], CONTEXTE["url_claude"], MODELES_CLAUDE)["commande"]
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8"}
    assert Porte(c, 10, environnement=env).transmettre("proposition", 130.0)["plafond_usd"] == 130.0
    monde["etat_claude"]["depense_usd"] = 12.5  # en cours de course : accepté
    assert Porte(c, 10, environnement=env).transmettre("juges", 47.12)["plafond_usd"] == 47.12
    for modif in ({"plafond_usd": 200.0}, {"modeles_permis": ["autre-modele"]}, {"depense_usd": 151.0}):
        etat = dict(monde["etat_claude"])
        monde["etat_claude"].update(modif)
        with pytest.raises(RelaisSansPlafond):
            Porte(c, 10, environnement=env).transmettre("proposition", 130.0)
        monde["etat_claude"].clear()
        monde["etat_claude"].update(etat)
    with pytest.raises(RelaisSansPlafond):  # relais injoignable
        Porte(porte_commande(monde["depot"], "http://127.0.0.1:9", MODELES_CLAUDE)["commande"], 10,
              environnement=env).transmettre("proposition", 130.0)
    with pytest.raises(RelaisSansPlafond):  # la porte de la v3 (lanceur de relais) ne rend aucun accusé
        Porte([sys.executable, "-I", "-B", str(monde["depot"] / L.PIECES["lanceur_relais"][0])], 10,
              environnement=env).transmettre("proposition", 130.0)


def test_porte_a_blanc_relais_deja_employe_refusee_avant_le_depart(monde):
    monde["etat_claude"]["depense_usd"] = 0.5
    monde["etat_claude"]["appels"] = 1
    assert lancer(monde["r"]) == 2
    runs = [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]
    assert all(not (p / "manifeste-lanceur-depart.json").exists() for p in runs)  # tentative non brûlée


def test_porte_a_blanc_au_manifeste(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["porte_a_blanc"]["claude"]["accuse"]["etape"] == "porte-a-blanc"
    assert dep["procedure_relais_persistants"]["relais_vivants"]["claude"]["variable_cle"] == "RR_ANTHROPIC_API_KEY_MINUIT"
    assert dep["releve_prix_claude"]["egal_au_bareme"] is True
    assert dep["registre_go_derive"]["nombre_de_lignes"] == 1


def test_commande_de_porte_qui_ne_commence_pas_par_la_porte_refusee(monde):
    d = declaration(monde["depot"])
    c = d["fournisseurs"]["claude"]["porte_plafond"]["commande"]
    d["fournisseurs"]["claude"]["porte_plafond"]["commande"] = ["/bin/sh", "-c", "true", c[3]]  # cite le chemin sans le lancer
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_relais_vivant_sur_rigaud_refuse(monde):
    args = monde["cmdlines"][PID_CLAUDE]
    args[args.index("--variable-cle") + 1] = "RR_ANTHROPIC_API_KEY_RIGAUD"
    assert lancer(monde["r"]) == 2


def test_relais_vivant_plafond_autre_que_150_refuse(monde):
    args = monde["cmdlines"][PID_CLAUDE]
    args[args.index("--plafond-usd") + 1] = "100"
    assert lancer(monde["r"]) == 2


def test_relais_vivant_programme_d_une_autre_empreinte_refuse(monde):
    p = [a for a in monde["cmdlines"][PID_CLAUDE] if a.endswith("relais_reel.py")][0]
    Path(p).write_text("# autre programme\n", encoding="utf-8")
    assert lancer(monde["r"]) == 2


def _registre(monde, texte):
    monde["r"].registre_go.write_text(texte, encoding="utf-8")


REGISTRE_AVEC_DOUBLONS = (ligne_go() + "| GO-2026-10-24-07 | 2026-10-24 | calcul | essai | 10 USD | 2026-10-30 | Lazar | R-1 |\n"
                          "| GO-2026-10-24-07 | 2026-10-25 | calcul | extension de GO-2026-10-24-07 | 12 USD | 2026-10-31 | Lazar | R-2 |\n")


def test_registre_derive_accepte_par_l_orchestrateur_et_source_refusee(monde, tmp_path):
    """Constat 2, R5 : la vraie lecture de l'orchestrateur refuse le registre à doublons, accepte le registre dérivé, refuse un
    registre dérivé falsifié."""
    o = _orch_present()
    sys.path.insert(0, str(o))
    ancien, sys.dont_write_bytecode = sys.dont_write_bytecode, True  # l'arbre de l'orchestrateur reste propre
    try:
        from pole.configuration_v55 import verifier_go_v55
        from pole.configuration_v53 import GoRefuse
    finally:
        sys.path.remove(str(o))
        sys.dont_write_bytecode = ancien
    _registre(monde, REGISTRE_AVEC_DOUBLONS)
    with pytest.raises(GoRefuse):
        verifier_go_v55(L.GO_ID, str(monde["r"].registre_go), 150.0, aujourd_hui=AUJOURD_HUI)
    d = L.ecrire_registre_derive(monde["r"].registre_go, tmp_path / "derive.md")
    assert verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=AUJOURD_HUI)["plafond_lu_usd"] == 150.0
    faux = tmp_path / "derive-falsifie.md"
    faux.write_text(Path(d["derive"]).read_text().replace("| 150 USD |", "| 140 USD |"), encoding="utf-8")
    with pytest.raises(GoRefuse):
        verifier_go_v55(L.GO_ID, str(faux), 150.0, aujourd_hui=AUJOURD_HUI)
    assert lancer(monde["r"]) == 0  # le lanceur part avec le registre à doublons de main
    vu = json.loads((Path(json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())["sortie"]) / "vu.json").read_text())
    assert vu["argv"][vu["argv"].index("--registre-go") + 1].endswith("registre-go-derive.md")


def test_revocation_incluse_au_registre_derive(monde, tmp_path):
    _registre(monde, ligne_go() + f"| GO-2026-11-19-01 | 2026-11-19 | révocation | révoque {L.GO_ID} | — | — | Lazar | R-9 |\n")
    d = L.ecrire_registre_derive(monde["r"].registre_go, tmp_path / "derive.md")
    assert d["nombre_de_lignes"] == 2


def _prix(monde, objet):
    p = monde["r"].releve_prix
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    ecrire_scelle(p, objet)


def test_releve_prix_absent_refuse(monde):
    monde["r"].releve_prix.unlink()
    assert lancer(monde["r"]) == 2


def test_releve_prix_different_du_bareme_refuse(monde):
    _prix(monde, releve_prix(espece_claude_2={"entree": 12.0, "sortie": 60.0}))
    assert lancer(monde["r"]) == 2


def test_releve_prix_d_hier_refuse(monde):
    o = releve_prix()
    o["releve_utc"] = "2026-11-17T23:00:00Z"
    _prix(monde, o)
    assert lancer(monde["r"]) == 2


def test_variable_minuit_vide_refusee(monde):
    monde["r"].environnement[L.CLE_CLAUDE] = ""
    assert lancer(monde["r"]) == 2


def test_kimi_zeros_refuses(monde):
    for modif in ({"prix_entree": 0.0}, {"prix_sortie": 0}, {"max_sortie_jetons": 0}, {"sortie_min_jetons": 0}, {"delai_s": 0},
                  {"max_sortie_jetons": 1000.0}, {"sortie_min_jetons": 2000}):
        _decl(monde, declaration(monde["depot"], kimi=kimi(monde, **modif)))
        _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
        assert lancer(monde["r"]) == 2, modif


def test_astra_non_epinglee_refusee(monde):
    s = script_commande(monde["tmp"], "astra-non-epinglee", {"texte": "", "cout_usd": 0.01})
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)], "modele_propose": "modele-essai-astra",
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 30.0, "reste_usd": 30.0, "source": "essai"}))
    assert lancer(monde["r"]) == 2


def test_reste_egal_a_la_part_refuse(monde, monkeypatch):
    s = script_commande(monde["tmp"], "astra", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "astra", s)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)], "modele_propose": "modele-essai-astra",
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 100.0, "reste_usd": 24.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3


def test_sorties_hors_depot_d_une_course_anterieure_refusees(monde):
    d = monde["r"].sorties_courses[2]
    (d / "20261118-000000-course-affinage-mentors-v3").mkdir(parents=True)
    assert lancer(monde["r"]) == 2


def test_arbre_de_l_orchestrateur_reste_propre():
    o = _orch_present()
    assert not subprocess.run(["git", "-C", str(o), "status", "--porcelain", "--ignored"], capture_output=True, text=True).stdout.strip()
