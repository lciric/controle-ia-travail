"""Essais du lanceur de la course d'affinage des idées des mentors (v3 : règle de clé par part, dispense R-3237, garde de crédit, procédure des relais persistants) — relais et orchestrateur **simulés**, aucun appel réel,
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
CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v3.py"
_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v3", CHEMIN_LANCEUR)
L = importlib.util.module_from_spec(_spec)
sys.modules["lancer_course_affinage_mentors_v3"] = L
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


def declaration(depot: Path, **modifs) -> dict:
    porte = {"type": "commande", "commande": [str(depot.parent / "procedure-relais.sh")], "delai_s": 5}
    d = {"version": "essai", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:18787", "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "porte_plafond": porte},
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
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    lanceur_sha = hashlib.sha256(CHEMIN_LANCEUR.read_bytes()).hexdigest()
    ecrire_scelle(depot / L.CONTRE_LECTURE, contre_lecture(L.PREREG_SHA256, lanceur_sha))
    ecrire_scelle(depot / L.DECLARATION_RELAIS, declaration(depot))
    ecrire_scelle(depot / L.RELEVE_CREDITS, releve())
    proc = tmp_path / "procedure-relais.sh"
    proc.write_text("#!/bin/sh\n# procédure d'essai\n", encoding="utf-8")
    import hashlib as _h
    ecrire_scelle(depot / L.PROCEDURE_RELAIS, {"chemin": str(proc), "sha256": _h.sha256(proc.read_bytes()).hexdigest()})
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text(ligne_go(), encoding="utf-8")
    r = L.Reglages(depot=depot, orchestrateurs=(o,), commit_orchestrateur=commit, empreintes_orchestrateur=empreintes,
                   pieces=dict(L.PIECES), prereg=(prereg, L.PREREG_SHA256), contre_lecture=depot / L.CONTRE_LECTURE,
                   declaration=depot / L.DECLARATION_RELAIS, releve=depot / L.RELEVE_CREDITS,
                   registre_go=depot / "registres" / "go.md", procedure_relais=depot / L.PROCEDURE_RELAIS, dossier_runs=depot / "runs", dossier_sorties=tmp_path / "sorties",
                   depot_attendu_par_l_enveloppe=depot, python=sys.executable, lanceur=CHEMIN_LANCEUR, moteur="reel",
                   environnement={"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "RR_ANTHROPIC_API_KEY_MINUIT": "valeur-secrete-essai-1",
                                  "RR_ANTHROPIC_API_KEY_RIGAUD": "valeur-secrete-essai-2"},
                   aujourd_hui=AUJOURD_HUI, horodatage=lambda: "Wed Nov 18 07:00:00 UTC 2026")
    return {"r": r, "tmp": tmp_path, "depot": depot, "orch": o, "lanceur_sha": lanceur_sha}


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
    alertes = [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith("-alerte-credits-affinage-mentors-v3")]
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


def test_carbon_sans_inscription_inactive_et_avec_inscription_active():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    r = L.Reglages.production()
    carbon = {"type": "commande_externe", "commande": ["/bin/true"], "modele_propose": "modele-essai-carbon", "nom_cle": "CLE_ESSAI_G",
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
    k["porte_plafond"] = {"type": "commande", "commande": [str(monde["tmp"] / "procedure-relais.sh")], "delai_s": 5}
    return k


def test_parts_au_pire():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    r = L.Reglages.production()
    pieces = {n: {"absolu": str(RACINE / rel)} for n, (rel, _) in L.PIECES.items()}
    astra = {"type": "commande_externe", "commande": ["/bin/true"], "modele_propose": "modele-essai-astra", "nom_cle": "CLE_ESSAI_S",
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


def test_part_au_pire_et_non_plafond_global(monde):
    # une clé d'Astra à 30 USD : sous 150 (v2 : refus) mais au-dessus de sa part au pire (24) et de son cinquième → départ
    script = monde["tmp"] / "astra.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': '', 'cout_usd': 0.01}))\n", encoding="utf-8")
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


def _astra_dispensee(monde, ligne):
    script = monde["tmp"] / "astra.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps(" + repr(ligne) + "))\n", encoding="utf-8")
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script)], "modele_propose": "modele-essai-astra",
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    objet = releve(CLE_ESSAI_S={"non_lisible": True, "motif": "solde illisible (R-3222)"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S"]}
    _releve(monde, objet)
    remplacer_orchestrateur(monde, executer="astra")


def test_premier_refus_pour_credit_arrete_la_course_code_5(monde):
    _astra_dispensee(monde, {"texte": "", "cout_usd": 0.01, "erreur": "429 RESOURCE_EXHAUSTED : insufficient quota"})
    assert lancer(monde["r"]) == 5
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["arret_au_premier_refus_pour_credit"][0]["relais"] == "astra" and fin["code"] == 2


def test_appel_sans_refus_pour_credit_ne_s_arrete_pas(monde):
    _astra_dispensee(monde, {"texte": "réponse", "cout_usd": 0.01, "modele_servi": "modele-essai-astra"})
    assert lancer(monde["r"]) == 0
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["arret_au_premier_refus_pour_credit"] == []


def test_garde_credit_motifs():
    spec = importlib.util.spec_from_file_location("garde_v3", RACINE / "scripts" / "garde_credit_relais_v3.py")
    G = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G)
    assert G.motif_credit('{"texte": "", "cout_usd": 0.01, "erreur": "insufficient_quota"}', "")
    assert G.motif_credit('{"texte": "", "cout_usd": 0.01, "erreur": "HTTP 402 payment required"}', "")
    assert G.motif_credit("", "billing hard limit reached")
    assert not G.motif_credit('{"texte": "une carte sur le crédit d\'une idée", "cout_usd": 0.2}', "")
    assert not G.motif_credit('{"texte": "", "cout_usd": 0.01, "erreur": "délai dépassé"}', "")


def _procedure(monde, objet=None, texte=None):
    p = monde["depot"] / L.PROCEDURE_RELAIS
    p.unlink()
    Path(str(p) + ".sha256").unlink()
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
