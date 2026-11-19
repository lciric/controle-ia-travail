"""Essais du lanceur du bras du juge externe différé, version 6 (second bras d'Astra, juge d'origine) : gardes (cas sains et artefacts, R5) et bras joué de bout
en bout, hors réseau, avec un juge factice local, sur une recomposition jetable des trois courses."""
import datetime as dt
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
CLONE = Path("/home/user/lciric/ideation-organism/orchestrator")
JOUR = dt.date(2026, 11, 18)
EN_TETE = "| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n"


@pytest.fixture()
def lb():
    spec = importlib.util.spec_from_file_location("lanceur_bras_v6_essai", RACINE / "scripts" / "lancer_bras_juge_ideation_organismes_discrets_v6.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def ligne(lignee, ident="GO-2026-11-18-90", plafond="4 USD", typ="calcul", par="Lazar", echeance="2026-11-25", plus=""):
    modele = ", second bras, juge d'origine gpt-6-astra" if lignee == "astra" else ""
    return (f"| {ident} | 2026-11-18 | {typ} | **Organisme d'idéation sur les organismes discrets, lignée {lignee} : bras du "
            f"juge externe différé{modele}**{plus} | {plafond} | {echeance} | {par} | R-0000 |")


def registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(EN_TETE + "\n".join(lignes) + "\n", encoding="utf-8")
    return p


@pytest.mark.parametrize("lignee", ["astra"])
def test_go_sain(lb, tmp_path, lignee):
    go = lb.verifier_go(registre(tmp_path, ligne("carbon", "GO-2026-11-18-90"), ligne("astra", "GO-2026-11-18-91"),
                                 ligne("argon", "GO-2026-11-18-92")), JOUR, lignee)
    assert go["plafond_usd"] == 4.0 and go["par"] == "Lazar"


@pytest.mark.parametrize("lignes, motif", [
    ([], "0 ligne"),
    ([ligne("astra"), ligne("astra", "GO-2026-11-18-91")], "2 ligne"),
    ([ligne("astra", plus=" et lignée argon")], "une ligne par lignée"),
    ([ligne("astra", plafond="2,7 USD")], "sous le pire cas"),
    ([ligne("astra", ident="GO-٢٠٢٦-١١-١٨-٩٠")], "0 ligne"),
    ([ligne("astra", typ="forme")], "calcul"),
    ([ligne("astra", par="la mère")], "Lazar exigé"),
    ([ligne("astra", echeance="2026-11-17")], "hors de sa période"),
    ([ligne("astra"), "| GO-2026-11-18-93 | 2026-11-18 | révocation | révoque GO-2026-11-18-90 | — | — | Lazar | R-1 |"], "révoqué"),
    ([ligne("astra").replace(", second bras", "")], "0 ligne"),          # la ligne du premier bras n'est pas candidate
    ([ligne("astra").replace("gpt-6-astra", "gpt-6.2-astra")], "0 ligne"),
    ([ligne("carbon")], "0 ligne"),
])
def test_go_artefacts(lb, tmp_path, lignes, motif):
    with pytest.raises(lb.Refus, match=motif):
        lb.verifier_go(registre(tmp_path, *lignes), JOUR, "astra")


def test_go_du_registre_reel(lb):
    """Aucune ligne de GO du bras n'est inscrite au moment où ce lanceur est écrit : le registre réel fait refuser, ou
    donne une ligne conforme une fois inscrite par la mère (les deux issues sont saines)."""
    for lignee in lb.LIGNEES:
        try:
            go = lb.verifier_go(RACINE / "registres" / "go.md", JOUR, lignee)
        except lb.Refus:
            continue
        assert go["plafond_usd"] >= lb.pire_cas_usd(lignee)


def sceller(chemin, objet):
    t = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    chemin.write_bytes(t)
    Path(str(chemin) + ".sha256").write_text(f"{hashlib.sha256(t).hexdigest()}  {chemin.name}\n", encoding="utf-8")


def attestation(lb, lignee, **ecarts):
    l = lb.LIGNEES[lignee]
    a = {"lecteur": "Lazar", "lu_le": "2026-11-18", "fiches_validees_sha256": l["fiches"],
         "consignes_en_attente_sha256": {l["etiquette"]: l["consigne"]}}
    a.update(ecarts)
    return a


def test_attestation_saine_et_artefacts(lb, tmp_path, monkeypatch):
    chemin = tmp_path / "att.json"
    monkeypatch.setattr(lb, "chemin_attestation", lambda lignee: chemin)
    monkeypatch.setattr(lb, "DEPOT", tmp_path)
    with pytest.raises(lb.Refus, match="absente"):
        lb.verifier_attestation("astra")
    sceller(chemin, attestation(lb, "astra"))
    assert lb.verifier_attestation("astra")["lecteur"] == "Lazar"
    for ecarts, motif in (({"lecteur": "une session"}, "Lazar"), ({"lu_le": "hier"}, "date ISO"),
                          ({"fiches_validees_sha256": "0" * 64}, "fiches validées"),
                          ({"consignes_en_attente_sha256": {"astra-juge": "0" * 64}}, "consigne en attente"),
                          ({"consignes_en_attente_sha256": {"argon-juge": lb.LIGNEES["astra"]["consigne"]}}, "consigne en attente"),
                          ({"en_trop": 1}, "ni plus ni moins")):
        sceller(chemin, attestation(lb, "astra", **ecarts))
        with pytest.raises(lb.Refus, match=motif):
            lb.verifier_attestation("astra")
    sceller(chemin, attestation(lb, "astra"))
    chemin.write_text(chemin.read_text(encoding="utf-8") + " ", encoding="utf-8")   # sceau faux
    with pytest.raises(lb.Refus, match="sceau"):
        lb.verifier_attestation("astra")


def test_arguments(lb):
    assert lb.principal([]) == 2 and lb.principal(["kimi"]) == 2 and lb.principal(["astra", "carbon"]) == 2


def test_commande(lb, tmp_path):
    a = lb.commande_bras("astra", tmp_path, tmp_path / "sortie", "h", "GO-2026-11-18-91")
    assert a[3] == "demonstrations/ideation_v8.py" and "--remplacement-modele-juge" not in a
    assert a[a.index("--juge-externe") + 1] == "astra-juge=gpt-6-astra"
    assert a[a.index("--commande-externe") + 1].endswith("appel-astra-v1.sh")
    assert a[a.index("--budget-controle-usd") + 1] == "0.3" and lb.pire_cas_usd("astra") == 2.8
    assert a[a.index("--moteur") + 1] == "claude-sdk" and a[a.index("--modele-commande-externe") + 1] == "gpt-6-astra"
    assert list(lb.LIGNEES) == ["astra"] and lb.LIGNEES["astra"]["modele_joue"] == lb.LIGNEES["astra"]["modele_course"]
    lb.garde_drapeaux(a)
    lb.garde_modeles_claude(a)


JUGE_FACTICE = '''import sys, json, os, re
consigne = sys.stdin.read()
servi = os.environ.get("MODELE_DEMANDE_POLE")
if "exactement OK" in consigne:
    print(json.dumps({"texte": "OK", "cout_usd": 0.001, "modele_servi": servi})); sys.exit(0)
bloc = json.loads(re.search(r"```json\\n(\\[.*\\])\\n```", consigne, re.S).group(1))
notes = [{"identifiant": f["identifiant"], "criteres": {k: 1 for k in ("avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}, "justifications": {}} for f in bloc]
print(json.dumps({"texte": "```json\\n" + json.dumps({"notes": notes, "doublons": []}) + "\\n```", "cout_usd": 0.3, "modele_servi": servi}))
'''


@pytest.mark.skipif(not CLONE.is_dir(), reason="clone public de l'orchestrateur absent")
@pytest.mark.skipif(sys.executable != "/usr/local/bin/python3", reason="le lanceur exige /usr/local/bin/python3")
@pytest.mark.parametrize("lignee", ["astra"])
def test_bras_de_bout_en_bout_juge_factice(lb, tmp_path, monkeypatch, lignee):
    """Aucun réseau, aucune dépense : enveloppe remplacée par un juge factice local ; ligne de GO et attestation d'essai.
    Les gardes de pièces, d'orchestrateur et de copies, la recomposition, l'assemblage et le bras sont les vrais."""
    script = tmp_path / "juge_factice.py"
    script.write_text(JUGE_FACTICE, encoding="utf-8")
    enveloppe = tmp_path / "enveloppe.sh"
    enveloppe.write_text(f'#!/bin/sh\nexec /usr/local/bin/python3 -I "{script}"\n', encoding="utf-8")
    monkeypatch.setitem(lb.LIGNEES[lignee], "enveloppe", (str(enveloppe), hashlib.sha256(enveloppe.read_bytes()).hexdigest()))
    att = tmp_path / "attestation-ESSAI.json"
    sceller(att, attestation(lb, lignee))
    monkeypatch.setattr(lb, "chemin_attestation", lambda _l: att)
    monkeypatch.setattr(lb, "verifier_attestation", lambda _l: {"chemin": str(att), "essai": True})
    go = registre(tmp_path, ligne(lignee, "GO-2026-11-18-90"))
    vrai_go = lb.verifier_go
    monkeypatch.setattr(lb, "verifier_go", lambda _r, jour, l: vrai_go(go, JOUR, l))
    monkeypatch.setattr(lb, "verifier_relais", lambda _l: {"essai": "relais non vérifié (juge factice local)"})
    monkeypatch.setattr(lb, "DOSSIER_SORTIES", tmp_path / "sorties")
    monkeypatch.setattr(lb, "RACINE_RUNS", tmp_path / "runs")
    code = lb.principal([lignee])
    sorties = list((tmp_path / "sorties").iterdir())
    err = (sorties[0] / "bras.stderr.txt").read_text(encoding="utf-8") if sorties else ""
    assert code in (0, 4), err[-1500:]
    run = next((tmp_path / "runs").iterdir())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text(encoding="utf-8"))
    assert fin["code"] == code and not fin["echec_lanceur"]
    for nom in ("manifeste-bras-rapporte.json", "classement.json", "lecture.json", "notes-bras-rapporte.json"):
        assert nom in fin["copies"], sorted(fin["copies"])
        assert (run / "copies" / ("sortie--" + nom + ".sha256")).is_file()
    bras = json.loads((run / "copies" / "sortie--manifeste-bras-rapporte.json").read_text(encoding="utf-8"))["reglages"]
    lecture = json.loads((run / "copies" / "sortie--lecture.json").read_text(encoding="utf-8"))
    l = lb.LIGNEES[lignee]
    assert bras["juges"][0][:2] == [l["etiquette"], l["modele_joue"]]
    assert lecture["auto_preference"][l["etiquette"]]["modele"] == l["modele_joue"]
    assert "remplacements_modele_juge" not in bras and "remplacement" not in json.dumps(lecture)
    assert lecture["auto_preference"]["astra-juge"]["n_propre_modele"] > 0
    assert "lanceur/bras.stderr.txt" in fin["copies"] and "lanceur/RECOMPOSITION.json" in fin["copies"]
    assert (run / "copies" / "lanceur--bras.stdout.txt.sha256").is_file()
    assert not (tmp_path / "runs" / f"verrou-lancement-{lignee}").exists()
    assert bras["commande_externe"]["controle_modele_servi"].startswith("exigé")
    time.sleep(1.1)
    assert lb.principal([lignee]) == 2        # un seul bras payé par lignée : refus sur le run antérieur, avant tout appel
    assert len([d for d in (tmp_path / "runs").iterdir() if d.name != f"verrou-lancement-{lignee}"]) == 1
    with pytest.raises(lb.Refus, match="déjà été joué"):
        lb.verifier_bras_jamais_joue(lignee)


def faux_run(lb, tmp_path, lignee, fin, tentative=None):
    run = tmp_path / "runs" / ("20261118-000000" + lb.SUFFIXE_RUN + lignee)
    (run / "copies").mkdir(parents=True)
    if fin is not None:
        (run / "manifeste-lanceur-fin.json").write_text(json.dumps(fin), encoding="utf-8")
    if tentative is not None:
        (run / "copies" / "sortie--bras-tentative-1.json").write_text(json.dumps({"reglages": {"journal": tentative}}), encoding="utf-8")
    return run


@pytest.mark.parametrize("fin, tentative, motif", [
    (None, None, "état du bras inconnu"),
    ({"copies": {}, "code": -9, "echec_lanceur": None}, None, "état du bras inconnu"),          # orchestrateur tué après l'envoi
    ({"copies": {}, "code": 0, "echec_lanceur": "KeyboardInterrupt: "}, None, "état du bras inconnu"),
    ({"copies": {}, "code": 0}, None, "état du bras inconnu"),                                  # manifeste incomplet
    ({"copies": {"manifeste-bras-rapporte.json": "x"}, "code": 0, "echec_lanceur": None}, None, "déjà été joué"),
    ({"copies": {"bras-tentative-1.json": "x"}, "code": 2, "echec_lanceur": None},
     {"cout_total_usd": 0.05, "consigne_envoyee": None}, "déjà été joué"),                      # contrôle payé
    ({"copies": {"bras-tentative-1.json": "x"}, "code": 2, "echec_lanceur": None},
     {"cout_total_usd": 1e-06, "consigne_envoyee": "x"}, "déjà été joué"),
    ({"copies": {"bras-tentative-1.json": "x"}, "code": 2, "echec_lanceur": None}, None, "déjà été joué"),   # tentative illisible
])
def test_verrou_artefacts(lb, tmp_path, monkeypatch, fin, tentative, motif):
    monkeypatch.setattr(lb, "RACINE_RUNS", tmp_path / "runs")
    faux_run(lb, tmp_path, "astra", fin, tentative)
    with pytest.raises(lb.Refus, match=motif):
        lb.verifier_bras_jamais_joue("astra")


@pytest.mark.parametrize("fin, tentative", [
    ({"copies": {"manifeste-bras-non-joue-1.json": "x", "lanceur/bras.stderr.txt": "y"}, "code": 2, "echec_lanceur": None}, None),
    ({"copies": {"bras-tentative-1.json": "x"}, "code": 2, "echec_lanceur": None}, {"cout_total_usd": 1e-06, "consigne_envoyee": None}),
])
def test_verrou_relance_permise_sans_envoi(lb, tmp_path, monkeypatch, fin, tentative):
    monkeypatch.setattr(lb, "RACINE_RUNS", tmp_path / "runs")
    run = faux_run(lb, tmp_path, "astra", fin, tentative)
    assert lb.verifier_bras_jamais_joue("astra") == {"runs_anterieurs_sans_envoi": [run.name]}


def test_relais(lb, monkeypatch):
    import http.server
    import threading
    etat = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            corps = json.dumps(etat).encode()
            self.send_response(200 if self.path == "/relais/etat" else 404)
            self.end_headers()
            self.wfile.write(corps)

        def log_message(self, *a):
            pass
    serveur = http.server.HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    try:
        monkeypatch.setitem(lb.LIGNEES["astra"], "relais", dict(lb.LIGNEES["astra"]["relais"], port=serveur.server_address[1]))
        etat.update({"modeles_permis": ["gpt-6-astra"], "pid": 1, "appels_restants": 12, "restant_usd": 8.0})
        assert lb.verifier_relais("astra")["restes"] == {"appels_restants": 12, "restant_usd": 8.0}
        for epuise in ({"appels_restants": 1}, {"restant_usd": 0.05}, {"restant_usd": None}, {"appels_restants": True}):
            sain = dict(etat)
            etat.update(epuise)
            with pytest.raises(lb.Refus, match="capacité restante"):
                lb.verifier_relais("astra")
            etat.clear(); etat.update(sain)
        for autre in (["gpt-6.2-astra"], ["gpt-6-astra", "gpt-6.2-astra"]):
            etat["modeles_permis"] = autre
            with pytest.raises(lb.Refus, match="exigé"):
                lb.verifier_relais("astra")
        etat["modeles_permis"] = ["gpt-6-astra"]
        assert lb.verifier_relais("astra")["modeles"] == ["gpt-6-astra"]
        for mauvais in ([], None):
            etat["modeles_permis"] = mauvais
            with pytest.raises(lb.Refus, match="exigé"):
                lb.verifier_relais("astra")
    finally:
        serveur.shutdown()
    with pytest.raises(lb.Refus, match="injoignable"):
        lb.verifier_relais("astra")


def test_verrou_de_lancement(lb, tmp_path, monkeypatch):
    """Deux lancements simultanés : le second est refusé avant tout appel, le verrou n'est pas retiré par le refus."""
    monkeypatch.setattr(lb, "RACINE_RUNS", tmp_path / "runs")
    monkeypatch.setattr(lb, "verifier_go", lambda *_a: {"id": "GO-2026-11-18-90"})
    monkeypatch.setattr(lb, "verifier_attestation", lambda _l: {})
    monkeypatch.setattr(lb, "verifier_relais", lambda _l: {})
    appels = []
    monkeypatch.setattr(lb, "verifier_bras_jamais_joue", lambda _l: appels.append(_l))
    (tmp_path / "runs" / "verrou-lancement-astra").mkdir(parents=True)
    with pytest.raises(lb.Refus, match="en cours"):
        lb.executer("astra")
    assert appels == []                       # v4 : les runs antérieurs ne se lisent que sous le verrou
    assert (tmp_path / "runs" / "verrou-lancement-astra").is_dir()
