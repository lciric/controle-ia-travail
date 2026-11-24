"""Essais de l'amorce du rejeu des activations, voie (A), v2 (R5 : chaque garde sur un cas sain et sur un faux cas).

Aucune location, aucun réseau : Vast simulé par un fichier, dépôts git locaux, passe remplacée par un bouchon qui écrit des
fichiers de zéros aux noms de la notice v6 (le vrai code de la passe n'est ni ouvert ni lancé ici)."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import signal
import subprocess
import sys
import textwrap
import time
from pathlib import Path

import pytest

from controle_ia import rejeu_activations_voie_a_v2 as R

RACINE = Path(__file__).resolve().parents[1]
RELEVE = RACINE / "docs/notes/rejeu-activations-saboteur-voie-a-v1/releve-offres-vast-2026-11-24-v1.json"
GABARIT = RACINE / "docs/notes/rejeu-activations-saboteur-voie-a-v1/amorce-executante-v8/ordre-lancement-rejeu-voie-a-v1-gabarit.json"
SECRET = "ghp_FAUXsecretPourEssai1234567890"
ARCHIVES = ["scores-par-action-passe-barreau8-v1.npz", "scores-par-jeton-passe-barreau8-v1.npz",
            "activite-brute-c7-passe-barreau8-v1.npz", "activite-brute-c15-passe-barreau8-v1.npz",
            "activite-brute-c23-passe-barreau8-v1.npz"]
FICHIERS = ["index-passe-barreau8-v1.jsonl", "trace-gardes-passe-barreau8-v1.json", "bordereau-livraison-passe-barreau8-v1.json"]


def offres():
    return json.loads(RELEVE.read_text())["offers"]


def offre(ident):
    return dict(next(o for o in offres() if o["id"] == ident))


# --- 1. Filtre bloquant des offres (devis § 2.3) --------------------------------------------------------------------------

def test_filtre_releve_scelle_objets_du_devis():
    assert R.motifs_offre(offre(29019348)) == []          # A100 SXM4 80 Go, 1,136 USD/h, stockage 0,24
    assert R.motifs_offre(offre(59588540)) == []          # A100 PCIe 80 Go (repli)
    assert any("storage_cost" in m for m in R.motifs_offre(offre(60992141)))   # stockage 1,00 > 0,40
    m = R.motifs_offre(offre(61733634))
    assert any("dph_total" in x for x in m) and any("reliability2" in x for x in m)
    assert any("gpu_ram" in x for x in R.motifs_offre(offre(54218901)))       # A100 de 40 Go
    choix = R.choisir_offre(offres())
    assert choix["id"] == 29019348 and choix["gpu_name"] == "A100 SXM4"


@pytest.mark.parametrize("champ,valeur", [("is_bid", True), ("verification", "unverified"), ("cuda_max_good", 12.8),
                                          ("cpu_ram", 32000), ("cpu_cores_effective", 8), ("inet_down_cost", 0.05),
                                          ("num_gpus", 2), ("gpu_name", "L40S"), ("dph_total", None)])
def test_filtre_refuse_chaque_borne(champ, valeur):
    o = offre(29019348)
    o[champ] = valeur
    assert R.motifs_offre(o)


def test_filtre_repli_pcie_puis_refus():
    sxm = [o for o in offres() if o["gpu_name"] == "A100 SXM4"]
    reste = [o for o in offres() if o["gpu_name"] != "A100 SXM4"]
    assert R.choisir_offre(reste)["id"] == 59588540
    with pytest.raises(R.Refus):
        R.choisir_offre([o for o in reste if o["gpu_name"] != "A100 PCIE"] + [o for o in sxm if o["id"] != 29019348])


# --- 2. Garde de l'accord (crochet du dépôt appelé tel quel) --------------------------------------------------------------

def registre(tmp_path, typ, plafond="11,00 USD", echeance="2026-11-30"):
    p = tmp_path / f"go-{typ}-{plafond.split()[0]}-{echeance}.md"
    p.write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n|---|---|---|---|---|---|---|---|\n"
                 f"| {R.GO_ATTENDU} | 2026-11-24 | {typ} | rejeu | {plafond} | {echeance} | Lazar | mot direct |\n")
    return p


def test_garde_go_sain_et_faux(tmp_path):
    garde = RACINE / ".claude/hooks/garde_calcul.py"
    jour = dt.date(2026, 11, 24)
    assert R.verifier_go(registre(tmp_path, "calcul"), garde, R.GO_ATTENDU, jour)["lignes"] == 1
    for p, motif in ((registre(tmp_path, "dépense"), "calcul"), (registre(tmp_path, "calcul", "15 USD"), "plafond"),
                     (registre(tmp_path, "calcul", echeance="2026-11-23"), "validité")):
        with pytest.raises(R.Refus, match=motif):
            R.verifier_go(p, garde, R.GO_ATTENDU, jour)
    with pytest.raises(R.Refus):
        R.verifier_go(registre(tmp_path, "calcul"), garde, "GO-2026-11-24-99", jour)


# --- 3. Surveillance externe : horloge et dépense ------------------------------------------------------------------------

def test_decision_surveillance():
    t0, p = 1_000_000.0, 1.17
    assert R.decision_surveillance(t0, t0 + 3600, p, 19.8, 18.5)["decision"] == "POURSUIVRE"
    d = R.decision_surveillance(t0, t0 + 4.5 * 3600, p, None, None)
    assert d["decision"] == "COUPER" and "horloge" in d["raison"]
    d = R.decision_surveillance(t0, t0 + 3600, p, 19.8, 19.8 - 9.6)     # crédit lu plus bas que l'estimée
    assert d["decision"] == "COUPER" and "dépense" in d["raison"]
    d = R.decision_surveillance(t0, t0 + 3600, 9.0, None, None)          # estimée seule
    assert d["decision"] == "COUPER"
    assert R.decision_surveillance(t0, t0 + 10, None, None, None)["decision"] == "COUPER"
    # garantie du devis : un hôte au plafond du filtre, à 4,49 h, reste sous le déclenchement (donc sous 11 USD)
    pire = 1.35 + 0.40 * 100 / 720
    assert R.decision_surveillance(t0, t0 + 4.49 * 3600, pire, None, None)["depense"] < R.DECLENCHEMENT_USD


# --- 4. Garde d'écriture et place libre ----------------------------------------------------------------------------------

def test_garde_ecriture(tmp_path):
    assert R.garde_ecriture(tmp_path / "sorties", place_min=1, taille_sonde=100_000) == []
    assert not list((tmp_path / "sorties").iterdir())                    # la sonde est retirée
    fichier = tmp_path / "pas-un-dossier"
    fichier.write_text("x")
    assert R.garde_ecriture(fichier / "sorties", place_min=1, taille_sonde=1000)
    assert any("place libre" in m for m in R.garde_ecriture(tmp_path / "s2", place_min=10 ** 18, taille_sonde=1000))


# --- 5. Garde « activations écrites » ------------------------------------------------------------------------------------

def ecrire_livraison(sortie: Path, archives=ARCHIVES, fichiers=FICHIERS, taille=120_000):
    liv = sortie / "livraison"
    liv.mkdir(parents=True, exist_ok=True)
    for a in archives:
        donnees = b"\0" * taille
        morceaux = []
        for k in range(0, taille, 50_000):
            m = liv / f"{a}.morceau-{k // 50_000:03d}"
            m.write_bytes(donnees[k:k + 50_000])
            morceaux.append({"nom": m.name, "taille": m.stat().st_size, "sha256": R.ecrire_compagnon(m)})
        d = liv / f"{a}.morceaux.json"
        d.write_text(json.dumps({"fichier": a, "taille": taille, "sha256": hashlib.sha256(donnees).hexdigest(),
                                 "morceaux": morceaux}))
        R.ecrire_compagnon(d)
    for f in fichiers:
        (liv / f).write_text("{}\n")
        R.ecrire_compagnon(liv / f)
    return liv


ATTENDU = {"sous_dossier": "livraison", "archives": ARCHIVES, "fichiers": FICHIERS}


def test_garde_activations_saine(tmp_path):
    ecrire_livraison(tmp_path)
    assert R.garde_activations(tmp_path, 0, ATTENDU) == []


@pytest.mark.parametrize("faute", ["code", "c15", "morceau-altere", "morceau-manquant", "bordereau", "trace-arret"])
def test_garde_activations_fausses(tmp_path, faute):
    liv = ecrire_livraison(tmp_path)
    code = 0
    if faute == "code":
        code = 1
    elif faute == "c15":
        for f in liv.glob("activite-brute-c15-*"):
            f.unlink()
    elif faute == "morceau-altere":
        (liv / "activite-brute-c7-passe-barreau8-v1.npz.morceau-001").write_bytes(b"\1" * 50_000)
    elif faute == "morceau-manquant":
        (liv / "activite-brute-c23-passe-barreau8-v1.npz.morceau-002").unlink()
    elif faute == "bordereau":
        (liv / "bordereau-livraison-passe-barreau8-v1.json").unlink()
    elif faute == "trace-arret":
        (liv / "trace-arret-passe-barreau8-v1.json").write_text("{}")
    assert R.garde_activations(tmp_path, code, ATTENDU)


def test_garde_rapport_essai(tmp_path):
    r = tmp_path / "rapport.json"

    def ecrire(contenu, sceller=True):
        r.write_text(json.dumps(contenu))
        c = Path(str(r) + ".sha256")
        if sceller:
            R.ecrire_compagnon(r)
        elif c.exists():
            c.unlink()
    ecrire({"tailles": {a: 10 for a in ARCHIVES}})
    assert R.garde_rapport_essai(r, ARCHIVES) == []
    ecrire({"fichiers": [{"nom": a, "taille_octets": 10} for a in ARCHIVES]})        # autre forme admise
    assert R.garde_rapport_essai(r, ARCHIVES) == []
    ecrire({"tailles": {a: 10 for a in ARCHIVES if "activite" not in a}})
    assert len(R.garde_rapport_essai(r, ARCHIVES)) == 3
    ecrire({"non_ecrits": ARCHIVES, "tailles": {a: 10 for a in ARCHIVES if "activite" not in a}})  # nommé sans taille
    assert len(R.garde_rapport_essai(r, ARCHIVES)) == 3
    ecrire({"tailles": {a: 0 for a in ARCHIVES}})
    assert len(R.garde_rapport_essai(r, ARCHIVES)) == 3
    ecrire({"tailles": {a: 10 for a in ARCHIVES}}, sceller=False)
    assert R.garde_rapport_essai(r, ARCHIVES)                                        # compagnon absent
    assert R.garde_rapport_essai(tmp_path / "absent.json", ARCHIVES)


def test_garde_activations_morceaux_mal_formes(tmp_path):
    liv = ecrire_livraison(tmp_path)
    d = liv / "activite-brute-c7-passe-barreau8-v1.npz.morceaux.json"
    d.write_text(json.dumps({"fichier": "x", "taille": 10, "morceaux": [1, 2]}))
    R.ecrire_compagnon(d)
    assert any("mal formée" in m for m in R.garde_activations(tmp_path, 0, ATTENDU))


# --- 6. Ordre de lancement -----------------------------------------------------------------------------------------------

def test_gabarit_refuse_tant_qu_il_n_est_pas_rempli():
    with pytest.raises(R.Refus, match="A_FIXER"):
        R.lire_ordre(GABARIT, R.sha256_fichier(GABARIT))


def ordre_rempli(tmp_path, **retouches) -> tuple[Path, str]:
    o = json.loads(GABARIT.read_text())
    o["go"] = R.GO_ATTENDU                     # le gabarit porte l'accord d'avant (GO-2026-11-24-06)
    o["tirages"] = [o["tirages"][0]]

    def sans(argv):
        return [x if "A_FIXER" not in x else "valeur-remplie" for x in argv]
    for k in ("verifier_entrees", "essai_a_blanc", "passe"):
        o[k]["argv"] = sans(o[k]["argv"])
    for k, f in retouches.items():
        f(o)
    p = tmp_path / "ordre.json"
    p.write_text(json.dumps(o, ensure_ascii=False))
    return p, R.sha256_fichier(p)


def test_ordre_sain_et_faux(tmp_path):
    p, s = ordre_rempli(tmp_path)
    assert R.lire_ordre(p, s)["go"] == R.GO_ATTENDU
    with pytest.raises(R.Refus, match="empreinte"):
        R.lire_ordre(p, "0" * 64)

    def remplacer(cle, option, valeur):
        def f(o):
            a = o[cle]["argv"]
            a[a.index(option) + 1] = valeur
        return f
    cas = [remplacer("passe", "--depense-max-usd", "10.00"), remplacer("passe", "--duree-max-heures", "6"),
           remplacer("passe", "--appareil", "cpu"), remplacer("essai_a_blanc", "--sortie", "/root/sorties/x"),
           remplacer("passe", "--sortie", "{INCONNUE}"),
           lambda o: o["livraison_attendue"]["archives"].remove("activite-brute-c15-passe-barreau8-v1.npz"),
           lambda o: o.__setitem__("branche_versement", "main"),
           lambda o: o["tirages"][0]["fichiers"].append("../hors"),
           lambda o: o["preparation"].append({"nom": "x", "argv": "bash -c tout", "delai_s": 5})]
    for k, f in enumerate(cas):
        (tmp_path / str(k)).mkdir()
        p, s = ordre_rempli(tmp_path / str(k), x=f)
        with pytest.raises(R.Refus):
            R.lire_ordre(p, s)


# --- 7. Destruction par l'identifiant (R10) ------------------------------------------------------------------------------

def jouet(tmp_path, ident=91000001, label=R.ETIQUETTE):
    c = R.ClientVastJouet(tmp_path / "vast.json")
    for i in sorted(R.INTOUCHABLES):
        c.ajouter(i, "autre chantier", "exited")
    c.ajouter(ident, label)
    return c


def test_destruction_saine_et_fausses(tmp_path):
    j = R.Journal(tmp_path / "j.txt", {}, echo=False)
    fiche = {"identifiant": 91000001, "etiquette": R.ETIQUETTE}
    att = tmp_path / "att.txt"
    att.write_text("RAPATRIEMENT_VERIFIE=oui\ninstance=91000001\n")
    c = jouet(tmp_path)
    for ident, raison, attestation, motif in ((58936096, "rapatriement-verifie", att, "intouchable"),
                                              (91000002, "rapatriement-verifie", att, "pas la mienne"),
                                              (91000001, "rapatriement-verifie", None, "non attesté"),
                                              (91000001, "au-hasard", att, "liste fermée"),
                                              (91000001, "refus-depart", None, "liste fermée")):
        with pytest.raises(R.Refus, match=motif):
            R.detruire(c, ident, fiche, raison, attestation, j, 0)
    att_non = tmp_path / "att-non.txt"
    att_non.write_text("RAPATRIEMENT_VERIFIE=non\ninstance=91000001\n")
    with pytest.raises(R.Refus):
        R.detruire(c, 91000001, fiche, "rapatriement-verifie", att_non, j, 0)
    assert [g for g in json.loads((tmp_path / "vast.json").read_text())["gestes"]] == []   # aucun geste jusqu'ici
    r = R.detruire(c, 91000001, fiche, "rapatriement-verifie", att, j, 0)
    assert r["etat"] == "detruite" and r["relectures"] == 2
    e = json.loads((tmp_path / "vast.json").read_text())
    assert e["gestes"] == [["detruire", 91000001]] and {i["id"] for i in e["instances"]} == set(R.INTOUCHABLES)


def test_destruction_refuse_une_etiquette_etrangere(tmp_path):
    c = jouet(tmp_path, label="autre")
    with pytest.raises(R.Refus, match="étiquette"):
        R.detruire(c, 91000001, {"identifiant": 91000001, "etiquette": R.ETIQUETTE}, "coupure-horloge", None,
                   R.Journal(tmp_path / "j.txt", {}, echo=False), 0)


def test_surveillance_coupe_et_detruit(tmp_path):
    c = jouet(tmp_path)
    fiche = {"identifiant": 91000001, "etiquette": R.ETIQUETTE, "creation_demandee_s": time.time() - 5 * 3600,
             "prix_horaire_usd": 1.17, "credit_avant": 20.0}
    r = R.surveiller(fiche, c, R.Journal(tmp_path / "s.txt", {}, echo=False), periode_s=0, tours_max=3,
                     attente_destruction_s=0)
    assert r["fin"] == "coupee" and "horloge" in r["raison"] and r["destruction"]["etat"] == "detruite"
    (tmp_path / "b").mkdir()
    c2 = jouet(tmp_path / "b")
    fiche2 = {**fiche, "creation_demandee_s": time.time() - 600}
    r2 = R.surveiller(fiche2, c2, R.Journal(tmp_path / "s2.txt", {}, echo=False), periode_s=0, tours_max=2)
    assert r2["fin"] == "tours" and any(i["id"] == 91000001 for i in c2.instances())


# --- 8. Machine en mode jouet : bout en bout -----------------------------------------------------------------------------

BOUCHON = textwrap.dedent('''
    import hashlib, json, os, sys, time
    from pathlib import Path
    a = sys.argv[1:]
    action, mode = a[0], a[a.index("--mode-bouchon") + 1]
    def opt(k): return a[a.index(k) + 1]
    sortie, run = Path(opt("--sortie")), opt("--run-id")
    def sceller(p):
        Path(str(p) + ".sha256").write_text(hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.name + "\\n")
    if action == "verifier-entrees":
        sys.exit(1 if mode == "entrees-fausses" else 0)
    sortie.mkdir(parents=True)
    for base in ("runs", "diag"):
        (Path(base) / run).mkdir(parents=True)
        (Path(base) / run / "journal.json").write_text("{}")
    ARCH = ["scores-par-action-passe-barreau8-v1.npz", "scores-par-jeton-passe-barreau8-v1.npz",
            "activite-brute-c7-passe-barreau8-v1.npz", "activite-brute-c15-passe-barreau8-v1.npz",
            "activite-brute-c23-passe-barreau8-v1.npz"]
    if action == "essai-a-blanc":
        noms = [x for x in ARCH if not (mode == "essai-sans-activations" and "activite" in x)]
        r = sortie / "rapport-essai-a-blanc-passe-barreau8-v1.json"
        r.write_text(json.dumps({"tailles": {n: 1000 for n in noms}}))
        sceller(r)
        sys.exit(0)
    (sortie / "environnement.txt").write_text("GH_TOKEN present" if "GH_TOKEN" in os.environ else "aucun secret")
    if mode == "passe-lente":
        time.sleep(120)
    if mode == "gros-fichier":
        (sortie / "archive-entiere-laissee.bin").write_bytes(b"\\0" * 120000)
    liv = sortie / "livraison"
    liv.mkdir()
    for x in ARCH:
        if mode == "passe-sans-activations" and "activite" in x:
            continue
        m = liv / (x + ".morceau-000"); m.write_bytes(b"\\0" * 1000); sceller(m)
        d = liv / (x + ".morceaux.json")
        d.write_text(json.dumps({"fichier": x, "taille": 1000, "sha256": "0" * 64,
                                 "morceaux": [{"nom": m.name, "taille": 1000, "sha256": "0" * 64}]}))
        sceller(d)
    for x in ["index-passe-barreau8-v1.jsonl", "trace-gardes-passe-barreau8-v1.json",
              "bordereau-livraison-passe-barreau8-v1.json"]:
        (liv / x).write_text("{}"); sceller(liv / x)
    print("LIVRAISON ÉCRITE")
''')


def git_(args, cwd):
    subprocess.run(["git", "-c", "user.name=e", "-c", "user.email=e@x", *args], cwd=cwd, check=True, capture_output=True)


@pytest.fixture
def banc(tmp_path, monkeypatch):
    monkeypatch.setenv("GH_TOKEN", SECRET)
    monkeypatch.setenv("HF_TOKEN", "hf_FAUXsecretPourEssai987654")
    distant = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(distant)], check=True)
    clone = tmp_path / "clone"
    clone.mkdir()
    git_(["init", "-q"], clone)
    (clone / ".gitignore").write_text("donnees/\n__pycache__/\n")
    (clone / "README").write_text("x")
    git_(["add", "-A"], clone)
    git_(["commit", "-q", "-m", "a"], clone)
    git_(["remote", "add", "origin", str(distant)], clone)
    git_(["push", "-q", "origin", "HEAD:refs/heads/main"], clone)
    # branche d'entrées : un fichier en trois morceaux et son compagnon
    git_(["checkout", "-q", "--orphan", "donnees/entrees-essai"], clone)
    d = clone / "donnees" / "e"
    d.mkdir(parents=True)
    entier = os.urandom(3000)
    (d / "f.bin.sha256").write_text(hashlib.sha256(entier).hexdigest() + "  f.bin\n")
    for k in range(3):
        (d / f"f.bin.morceau-{k:03d}").write_bytes(entier[k * 1000:(k + 1) * 1000])
    git_(["add", "-f", "-A", "donnees/e"], clone)
    git_(["commit", "-q", "-m", "entrees"], clone)
    git_(["push", "-q", "origin", "HEAD:refs/heads/donnees/entrees-essai"], clone)
    git_(["checkout", "-q", "main"], clone)
    subprocess.run(["git", "branch", "-D", "donnees/entrees-essai"], cwd=clone, capture_output=True)
    bouchon = tmp_path / "bouchon.py"
    bouchon.write_text(BOUCHON)
    machines = []

    def lancer(mode="sain", echeance_s=3600, marge_s=60, tirage_faux=False, branche=None, **retouches):
        o = json.loads(GABARIT.read_text())
        o["go"] = R.GO_ATTENDU

        def cmd(action, sortie, run, debut):
            return [sys.executable, str(bouchon), action, "--sortie", sortie, "--run-id", run, "--debut-location", debut,
                    "--depense-max-usd", "7.00", "--duree-max-heures", "4.5", "--identifiant-instance",
                    "{IDENTIFIANT_INSTANCE}", "--prix-horaire-usd", "{PRIX_HORAIRE_USD}", "--appareil", "cuda",
                    "--mode-bouchon", mode]
        temoin = ("import os, sys; open(sys.argv[1], 'a').write(sys.argv[2] + ':' + "
                  "('HF' if os.environ.get('HF_TOKEN') else '-') + ('GH' if os.environ.get('GH_TOKEN') else '-') + '\\n')")
        o["preparation"] = [{"nom": n, "argv": [sys.executable, "-c", temoin, str(tmp_path / "secrets-preparation.txt"), n],
                             "delai_s": 60} for n in ("bibliotheques", "modele")]
        o["tirages"] = [{"branche": "donnees/entrees-essai", "fichiers": [f"donnees/e/f.bin.morceau-00{k}" for k in range(3)] +
                         ["donnees/e/f.bin.sha256"], "assembler": [{"cible": "donnees/e/f.bin", "morceaux":
                         [f"donnees/e/f.bin.morceau-00{k}" for k in (range(3) if not tirage_faux else (0, 2, 1))]}],
                         "verifier": ["donnees/e/f.bin.sha256"]}]
        o["branche_versement"] = branche or f"donnees/versement-essai-{len(machines)}"
        o["verifier_entrees"]["argv"] = cmd("verifier-entrees", "{SORTIE_VERIF}", "{RUN_ID_VERIF}", "{DEBUT_COMMANDE}")
        o["essai_a_blanc"]["argv"] = cmd("essai-a-blanc", "{SORTIE_ESSAI}", "{RUN_ID_ESSAI}", "{DEBUT_COMMANDE}")
        o["passe"]["argv"] = cmd("passe", "{SORTIE_PASSE}", "{RUN_ID_PASSE}", "{DEBUT_LOCATION}")
        travail = tmp_path / f"travail-{len(machines)}"
        travail.mkdir()
        po = travail / "ordre.json"
        po.write_text(json.dumps(o))
        vast = R.ClientVastJouet(travail / "vast.json")
        vast.ajouter(91000001, R.ETIQUETTE)
        s = tmp_path / f"sorties-{len(machines)}"
        valeurs = {"CLONE": str(clone), "CACHE_MODELE": str(tmp_path / "cache"), "PYTHON": sys.executable,
                   "SORTIE_VERIF": str(s / "v"), "SORTIE_ESSAI": str(s / "e"), "SORTIE_PASSE": str(s / "p"),
                   "RUN_ID_VERIF": "20261124-000000-verification-barreau8", "RUN_ID_ESSAI": "20261124-000000-essai-barreau8",
                   "RUN_ID_PASSE": "20261124-000000-passe-barreau8", "DEBUT_LOCATION": "2026-11-24T00:00:00Z",
                   "IDENTIFIANT_INSTANCE": "91000001", "PRIX_HORAIRE_USD": "1.17"}
        m = R.Machine({"travail": travail, "clone": clone, "ordre_chemin": po, "ordre_sha256": R.sha256_fichier(po),
                       "identifiant_instance": 91000001, "echeance_utc_s": time.time() + echeance_s, "marge_s": marge_s,
                       "depot_url": str(distant), "valeurs": valeurs, "etiquette_course": "essai-rejeu",
                       "vast_jouet": travail / "vast.json", "jouet": True, "place_min": 1, "taille_sonde": 10_000,
                       "attente_poussee_s": 0, "pas_minuterie_s": 0.2, "temps_min_passe_s": 0, **retouches})
        machines.append(m)
        code = m.executer()
        return m, code, o["branche_versement"]

    yield {"lancer": lancer, "distant": distant, "tmp": tmp_path}
    for m in machines:  # minuteries arrêtées par leur PID (R10)
        f = m.travail / "minuterie.pid"
        if f.is_file():
            try:
                os.kill(int(f.read_text()), signal.SIGTERM)
            except ProcessLookupError:
                pass


def gestes(m):
    return json.loads((m.travail / "vast.json").read_text())["gestes"]


def test_machine_saine_bout_en_bout(banc):
    m, code, br = banc["lancer"]("sain")
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 0 and "ÉTAT LIVRAISON VERSÉE" in journal and "VERSEMENT POUSSÉ" in journal
    assert ["arreter", 91000001] in gestes(m)
    assert SECRET not in journal
    commit = journal.split("VERSEMENT POUSSÉ commit=")[1].split()[0]
    j = R.Journal(banc["tmp"] / "rap.txt", {}, echo=False)
    r = R.rapatrier(str(banc["distant"]), br, banc["tmp"] / "rapatriement", commit, 91000001, j)
    assert r["verifie"], r["motifs"]
    base = next((banc["tmp"] / "rapatriement").glob("versement/*"))
    assert (base / "sortie-passe/environnement.txt").read_text() == "aucun secret"   # la passe ne voit aucun secret
    assert (base / "runs/20261124-000000-essai-barreau8").is_dir()                    # runs/ de l'essai récupérés
    att = Path(r["attestation"])
    fiche = {"identifiant": 91000001, "etiquette": R.ETIQUETTE}
    d = R.detruire(R.ClientVastJouet(m.travail / "vast.json"), 91000001, fiche, "rapatriement-verifie", att, j, 0)
    assert d["etat"] == "detruite"


def test_rapatriement_refuse_une_alteration(banc):
    m, code, br = banc["lancer"]("sain")
    t = banc["tmp"]
    w = t / "alteration"
    subprocess.run(["git", "clone", "-q", "--branch", br, str(banc["distant"]), str(w)], check=True)
    f = next(w.glob("versement/*/sortie-passe/environnement.txt"))
    f.write_text("altéré")
    git_(["commit", "-qam", "alteration"], w)
    git_(["push", "-q", "origin", f"HEAD:refs/heads/{br}"], w)
    j = R.Journal(t / "rap.txt", {}, echo=False)
    r = R.rapatrier(str(banc["distant"]), br, t / "rap2", None, 91000001, j)
    assert not r["verifie"] and "RAPATRIEMENT_VERIFIE=non" in Path(r["attestation"]).read_text()
    with pytest.raises(R.Refus):
        R.detruire(R.ClientVastJouet(m.travail / "vast.json"), 91000001, {"identifiant": 91000001, "etiquette": R.ETIQUETTE},
                   "rapatriement-verifie", Path(r["attestation"]), j, 0)


@pytest.mark.parametrize("mode,etat", [("essai-sans-activations", "REFUS DE DÉPART"),
                                       ("entrees-fausses", "REFUS DE DÉPART"),
                                       ("passe-sans-activations", "ACTIVATIONS NON ÉCRITES")])
def test_machine_refuse_ou_signale(banc, mode, etat):
    m, code, br = banc["lancer"](mode)
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 1 and f"ÉTAT {etat}" in journal and "VERSEMENT POUSSÉ" in journal    # récupéré quand même
    assert ["arreter", 91000001] in gestes(m)
    if etat == "REFUS DE DÉPART":
        assert "passe : lancée" not in journal                                          # la passe n'est jamais partie


def test_tirage_faux_refuse_le_depart(banc):
    m, code, br = banc["lancer"]("sain", tirage_faux=True)
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 1 and "REFUS DE DÉPART" in journal and "empreinte" in journal and "passe : lancée" not in journal


def test_minuterie_coupe_la_passe_puis_detruit(banc):
    m, code, br = banc["lancer"]("passe-lente", echeance_s=6, marge_s=4)
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 1 and "COUPURE À L'ÉCHÉANCE" in journal and "VERSEMENT POUSSÉ" in journal
    fin = time.time() + 20
    while time.time() < fin and ["detruire", 91000001] not in gestes(m):
        time.sleep(0.3)
    assert ["detruire", 91000001] in gestes(m)
    assert "SIGTERM" in (m.travail / "minuterie.txt").read_text()


def test_branche_de_versement_existante_refuse_le_depart(banc):
    m1, c1, br = banc["lancer"]("sain")
    assert c1 == 0
    m2, c2, br2 = banc["lancer"]("sain", branche=br)      # même nom : refus (R12, nom neuf exigé)
    journal = (m2.travail / "journal-machine.txt").read_text()
    assert c2 == 1 and "REFUS DE DÉPART" in journal and "déjà présente" in journal and "passe : lancée" not in journal
    assert "VERSEMENT POUSSÉ" in journal and f"branche={br}-refus-" in journal              # récupéré sous un nom neuf


def test_redemarrage_ne_relance_rien(banc):
    m, code, br = banc["lancer"]("sain")
    (m.travail / "versement.verrou").unlink()
    m.r["ordre"] = {**m.r["ordre"], "branche_versement": br + "-redemarrage"}
    code2 = m.executer()
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code2 == 1 and "REDÉMARRAGE 2" in journal and journal.count("passe : lancée") == 1


def test_script_de_demarrage_sans_secret():
    s = R.script_de_demarrage("a" * 40, "docs/x/ordre.json", "b" * 64)
    assert "GH_TOKEN}" in s and SECRET not in s and "rejeu_activations_voie_a_v2.py machine" in s
    for args in (("a" * 39, "o.json", "b" * 64), ("a" * 40, "../o.json", "b" * 64), ("a" * 40, "o.json; rm", "b" * 64)):
        with pytest.raises(R.Refus):
            R.script_de_demarrage(*args)


# --- 9. Faux cas ajoutés après la contre-lecture (B1 à B3, M1 à M7, m3, m5) -------------------------------------------------

def test_minuterie_detruit_meme_avec_un_pid_illisible(tmp_path):
    c = jouet(tmp_path)
    (tmp_path / "passe.pid").write_text("")
    code = R.minuterie(tmp_path, time.time() + 1.0, 0.5, 91000001, 0.1, c)
    assert code == 0 and ["detruire", 91000001] in json.loads((tmp_path / "vast.json").read_text())["gestes"]
    assert "illisible" in (tmp_path / "minuterie.txt").read_text()


def test_minuterie_refuse_une_intouchable(tmp_path):
    c = jouet(tmp_path)
    assert R.minuterie(tmp_path, time.time() + 0.2, 0.1, 58936096, 0.05, c) == 3
    assert json.loads((tmp_path / "vast.json").read_text())["gestes"] == []


def test_minuterie_morte_refuse_le_depart(banc):
    m, code, br = banc["lancer"]("sain", minuterie_executable="/bin/false")
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 1 and "REFUS DE DÉPART" in journal and "minuterie non vivante" in journal
    assert "passe : lancée" not in journal and ["arreter", 91000001] in gestes(m)


def test_sans_cle_d_instance_refuse_le_depart(banc, monkeypatch):
    monkeypatch.delenv("CONTAINER_API_KEY", raising=False)
    m, code, br = banc["lancer"]("sain", vast_jouet=None)
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 1 and "CONTAINER_API_KEY" in journal and "passe : lancée" not in journal


def test_filet_erreur_inattendue(banc, monkeypatch):
    def casse(self, t):
        raise OSError("disque perdu")
    monkeypatch.setattr(R.Machine, "tirer", casse)
    m, code, br = banc["lancer"]("sain")
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 1 and "ÉTAT ERREUR INATTENDUE" in journal and "VERSEMENT POUSSÉ" in journal
    assert ["arreter", 91000001] in gestes(m)


def test_passe_trop_tardive_ne_part_pas(banc):
    m, code, br = banc["lancer"]("sain", temps_min_passe_s=10 ** 6)
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 1 and "trop peu pour la passe" in journal and "passe : lancée" not in journal


def test_gros_fichier_coupe_pour_le_versement(banc, monkeypatch):
    monkeypatch.setattr(R, "FICHIER_MAX_OCTETS", 50_000)
    monkeypatch.setattr(R, "MORCEAU_OCTETS", 20_000)
    m, code, br = banc["lancer"]("gros-fichier")
    journal = (m.travail / "journal-machine.txt").read_text()
    assert code == 0 and "archive-entiere-laissee.bin coupé en" in journal
    commit = journal.split("VERSEMENT POUSSÉ commit=")[1].split()[0]
    j = R.Journal(banc["tmp"] / "rap.txt", {}, echo=False)
    r = R.rapatrier(str(banc["distant"]), br, banc["tmp"] / "rap-gros", commit, 91000001, j)
    assert r["verifie"] and r["etat_verse"] == "LIVRAISON VERSÉE"
    base = next((banc["tmp"] / "rap-gros").glob("versement/*/sortie-passe"))
    assert not (base / "archive-entiere-laissee.bin").exists() and (base / "archive-entiere-laissee.bin.decoupe.json").is_file()


class VastCapricieux:
    """Relevés en erreur, puis destruction qui échoue une fois : la surveillance doit retenter."""

    def __init__(self, interne, erreurs_releve=0, echecs_destruction=0, vide_une_fois=False):
        self.i, self.er, self.ed, self.vide = interne, erreurs_releve, echecs_destruction, vide_une_fois

    def instances(self):
        if self.er > 0:
            self.er -= 1
            raise R.Refus("HTTP 500")
        if self.vide:
            self.vide = False
            return []
        return self.i.instances()

    def credit(self):
        raise R.Refus("HTTP 500")

    def detruire(self, ident):
        if self.ed > 0:
            self.ed -= 1
            raise R.Refus("HTTP 502")
        self.i.detruire(ident)


def test_surveillance_releve_vide_n_est_pas_une_absence(tmp_path):
    c = VastCapricieux(jouet(tmp_path), vide_une_fois=True)
    fiche = {"identifiant": 91000001, "etiquette": R.ETIQUETTE, "creation_demandee_s": time.time() - 60,
             "prix_horaire_usd": 1.17, "credit_avant": 20.0}
    r = R.surveiller(fiche, c, R.Journal(tmp_path / "s.txt", {}, echo=False), periode_s=0, tours_max=3)
    assert r["fin"] == "tours"


def test_surveillance_coupe_l_horloge_malgre_releves_en_erreur_et_retente(tmp_path):
    interne = jouet(tmp_path)
    c = VastCapricieux(interne, erreurs_releve=3, echecs_destruction=1)
    fiche = {"identifiant": 91000001, "etiquette": R.ETIQUETTE, "creation_demandee_s": time.time() - 5 * 3600,
             "prix_horaire_usd": 1.17, "credit_avant": 20.0}
    r = R.surveiller(fiche, c, R.Journal(tmp_path / "s.txt", {}, echo=False), periode_s=0, tours_max=8,
                     attente_destruction_s=0)
    texte = (tmp_path / "s.txt").read_text()
    assert r["fin"] == "coupee" and "ALARME : coupure non obtenue" in texte
    assert ["detruire", 91000001] in json.loads((tmp_path / "vast.json").read_text())["gestes"]


class VastCreationIncertaine(R.ClientVastJouet):
    def creer(self, offre_id, corps, secrets=None):
        super().creer(offre_id, corps, secrets)
        raise R.Refus("délai dépassé")


def args_creation(tmp_path, **k):
    import argparse
    o, sha = ordre_rempli(tmp_path)
    offres_f = tmp_path / "offres.json"
    offres_f.write_text(json.dumps({"offers": offres()}))
    base = dict(fiche=str(tmp_path / "fiche.json"), feu=R.FEU_ATTENDU, go=R.GO_ATTENDU,
                registre=str(registre(tmp_path, "calcul")), garde=str(RACINE / ".claude/hooks/garde_calcul.py"),
                ordre=str(o), ordre_rel="docs/ordre.json", ordre_sha256=sha, offres=str(offres_f), commit="a" * 40,
                outil="vastai", verifier_seulement=False, attente_s=0.0, jouet=None)
    base.update(k)
    return argparse.Namespace(**base)


def test_creation_saine_et_refus(tmp_path, monkeypatch):
    monkeypatch.setenv("GO_ID", R.GO_ATTENDU)
    monkeypatch.setenv("GH_TOKEN", SECRET)
    monkeypatch.setenv("HF_TOKEN", "hf_FAUXsecretPourEssai987654")
    jour = dt.date(2026, 11, 24)
    c = R.ClientVastJouet(tmp_path / "vast.json")
    assert R.creer(args_creation(tmp_path, feu="feu"), c, jour) == 2                     # mot de feu inexact
    assert R.creer(args_creation(tmp_path), c, jour) == 0
    fiche = json.loads((tmp_path / "fiche.json").read_text())
    assert fiche["identifiant"] and fiche["offre"] == 29019348 and SECRET not in (tmp_path / "fiche.json").read_text()
    inst = c.instances()[0]
    assert inst["label"] == R.ETIQUETTE and "GH_TOKEN" in inst["env"]                    # noms seulement dans le jouet
    assert R.creer(args_creation(tmp_path), c, jour) == 2                                # fiche déjà présente (R12)
    (tmp_path / "fiche.json").unlink()
    assert R.creer(args_creation(tmp_path), c, jour) == 2                                # étiquette déjà prise


def test_creation_incertaine_retrouvee_par_l_etiquette(tmp_path, monkeypatch):
    monkeypatch.setenv("GO_ID", R.GO_ATTENDU)
    monkeypatch.setenv("GH_TOKEN", SECRET)
    monkeypatch.setenv("HF_TOKEN", "hf_FAUXsecretPourEssai987654")
    c = VastCreationIncertaine(tmp_path / "vast.json")
    assert R.creer(args_creation(tmp_path), c, dt.date(2026, 11, 24)) == 2
    fiche = json.loads((tmp_path / "fiche.json").read_text())
    assert fiche["identifiant"] == c.instances()[0]["id"] and fiche["etat"] == "retrouvée par l'étiquette"


def test_script_de_demarrage_porte_une_minuterie_de_secours():
    s = R.script_de_demarrage("a" * 40, "docs/x/ordre.json", "b" * 64)
    assert s.index("minuterie-secours") < s.index("git -c credential.helper") and "method='DELETE'" in s


def test_fiche_sans_identifiant_resolue_ou_refusee(tmp_path):
    fiche = {"identifiant": None, "etiquette": R.ETIQUETTE, "creation_demandee_s": time.time() - 5 * 3600,
             "prix_horaire_usd": 1.17, "credit_avant": 20.0}
    c = jouet(tmp_path)
    r = R.surveiller(fiche, c, R.Journal(tmp_path / "s.txt", {}, echo=False), periode_s=0, tours_max=3,
                     attente_destruction_s=0)
    assert r["fin"] == "coupee" and r["destruction"]["identifiant"] == 91000001
    (tmp_path / "b").mkdir()
    c2 = jouet(tmp_path / "b", label="autre")                    # aucune instance à l'étiquette : refus, aucun geste
    with pytest.raises(R.Refus, match="vérifier à la main"):
        R.surveiller(fiche, c2, R.Journal(tmp_path / "s2.txt", {}, echo=False), periode_s=0, tours_max=3)
    assert json.loads((tmp_path / "b/vast.json").read_text())["gestes"] == []


def test_surveillance_detruit_sans_releve_apres_trois_echecs(tmp_path):
    interne = jouet(tmp_path)
    c = VastCapricieux(interne, erreurs_releve=10 ** 6)
    fiche = {"identifiant": 91000001, "etiquette": R.ETIQUETTE, "creation_demandee_s": time.time() - 5 * 3600,
             "prix_horaire_usd": 1.17, "credit_avant": 20.0}
    R.surveiller(fiche, c, R.Journal(tmp_path / "s.txt", {}, echo=False), periode_s=0, tours_max=4, attente_destruction_s=0)
    assert ["detruire", 91000001] in json.loads((tmp_path / "vast.json").read_text())["gestes"]
    assert "sans relevé" in (tmp_path / "s.txt").read_text()


ORDRE = RACINE / "docs/notes/rejeu-activations-saboteur-voie-a-v1/amorce-executante-v8/ordre-lancement-rejeu-voie-a-v1.json"


def test_ordre_rempli_refuse_tant_que_le_module_est_a_fixer_et_passe_sinon(tmp_path):
    with pytest.raises(R.Refus, match="A_FIXER"):
        R.lire_ordre(ORDRE, R.sha256_fichier(ORDRE))
    texte = ORDRE.read_text()
    assert texte.count("A_FIXER") == 3
    copie = tmp_path / "ordre.json"
    copie.write_text(texte.replace("A_FIXER : module de la passe conforme aux deux additifs (ligne CODE-PASSE-IIB)",
                                   "controle_ia.barreau8_moniteurs.module_essai"))
    o = R.lire_ordre(copie, R.sha256_fichier(copie))
    assert o["go"] == "GO-2026-11-24-13" and o["preparation"][0]["nom"] == "fichiers-course"


def test_controle_des_fichiers_de_la_course(tmp_path):
    o = json.loads(ORDRE.read_text())
    argv = o["preparation"][0]["argv"]
    d = tmp_path / "diag/20261122-202132-iib-reel"
    d.mkdir(parents=True)
    r = subprocess.run([sys.executable, *argv[1:]], cwd=tmp_path, capture_output=True, text=True)
    assert r.returncode == 1 and "NON CONFORMES" in r.stdout          # fichiers absents : refus (le cas sain se joue
    (d / "ids-actions-evaluation-iib-v5.json").write_text("{}")         # sur la machine, aux vrais fichiers)
    (d / "ids-actions-evaluation-iib-v5.json.sha256").write_text("7eceb1615c6e00dc028fcbf42d4f32a83e2673d0a033a94b30820c32f198aea2  x\n")
    r = subprocess.run([sys.executable, *argv[1:]], cwd=tmp_path, capture_output=True, text=True)
    assert r.returncode == 1                                             # empreinte fausse : refus


def test_seul_le_telechargement_du_modele_voit_le_jeton(banc):
    m, code, br = banc["lancer"]("sain")
    assert code == 0
    assert (banc["tmp"] / "secrets-preparation.txt").read_text().split() == ["bibliotheques:--", "modele:HF-"]
