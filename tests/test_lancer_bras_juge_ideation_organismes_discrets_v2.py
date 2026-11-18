"""Essais du lanceur du bras du juge externe différé, version 2 : gardes (cas sains et artefacts, R5) et bras joué de bout
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
    spec = importlib.util.spec_from_file_location("lanceur_bras_v2_essai", RACINE / "scripts" / "lancer_bras_juge_ideation_organismes_discrets_v2.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def ligne(lignee, ident="GO-2026-11-18-90", plafond="4 USD", typ="calcul", par="Lazar", echeance="2026-11-25", plus=""):
    modele = " en gpt-6.2-astra" if lignee == "astra" else ""
    return (f"| {ident} | 2026-11-18 | {typ} | **Organisme d'idéation sur les organismes discrets, lignée {lignee} : bras du "
            f"juge externe différé{modele}**{plus} | {plafond} | {echeance} | {par} | R-0000 |")


def registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(EN_TETE + "\n".join(lignes) + "\n", encoding="utf-8")
    return p


@pytest.mark.parametrize("lignee", ["carbon", "astra", "argon"])
def test_go_sain(lb, tmp_path, lignee):
    go = lb.verifier_go(registre(tmp_path, ligne("carbon", "GO-2026-11-18-90"), ligne("astra", "GO-2026-11-18-91"),
                                 ligne("argon", "GO-2026-11-18-92")), JOUR, lignee)
    assert go["plafond_usd"] == 4.0 and go["par"] == "Lazar"


@pytest.mark.parametrize("lignes, motif", [
    ([], "0 ligne"),
    ([ligne("astra"), ligne("astra", "GO-2026-11-18-91")], "2 ligne"),
    ([ligne("astra", plus=" et lignée argon")], "une ligne par lignée"),
    ([ligne("astra", plafond="2 USD")], "sous le pire cas"),
    ([ligne("astra", typ="forme")], "calcul"),
    ([ligne("astra", par="la mère")], "Lazar exigé"),
    ([ligne("astra", echeance="2026-11-17")], "hors de sa période"),
    ([ligne("astra"), "| GO-2026-11-18-93 | 2026-11-18 | révocation | révoque GO-2026-11-18-90 | — | — | Lazar | R-1 |"], "révoqué"),
    ([ligne("astra").replace(" en gpt-6.2-astra", "")], "ne nomme pas le modèle joué"),
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
        assert go["plafond_usd"] >= lb.PIRE_CAS_USD


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
    assert a[3] == "demonstrations/ideation_v9.py" and "astra-juge=gpt-6.2-astra" in a
    assert "astra-juge=gpt-6-astra=gpt-6.2-astra=GO-2026-11-18-91" in a and "astra-juge=go 6.2" in a
    c = lb.commande_bras("carbon", tmp_path, tmp_path / "sortie", "h", "GO-2026-11-18-90")
    assert c[3] == "demonstrations/ideation_v8.py" and "--remplacement-modele-juge" not in c
    for argv in (a, c):
        lb.garde_drapeaux(argv)
        lb.garde_modeles_claude(argv)
    with pytest.raises(lb.Refus):
        lb.garde_drapeaux(a + ["--tolerer-somme-plafonds-externe"])
    with pytest.raises(lb.Refus):
        lb.garde_modeles_claude(["--juge-externe", "x=claude-opus-5-5"])


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
@pytest.mark.parametrize("lignee", ["carbon", "astra", "argon"])
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
    monkeypatch.setattr(lb, "sonder_bac_a_sable", lambda env: {"actif": None, "essai": "sonde non jouée"})
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
    if lignee == "astra":
        assert bras["remplacements_modele_juge"] == {"astra-juge": {"modele_course": "gpt-6-astra", "modele_joue": "gpt-6.2-astra",
                                                                    "go": "GO-2026-11-18-90", "mot": "go 6.2"}}
        assert lecture["remplacement_modele_juge"]["mention"].startswith("juge externe joué avec un autre modèle")
        assert lecture["auto_preference"]["astra-juge"]["n_propre_modele"] == 0
    else:
        assert "remplacements_modele_juge" not in bras and "remplacement_modele_juge" not in lecture
    time.sleep(1.1)
    assert lb.principal([lignee]) == 2        # un seul bras payé par lignée : refus sur le run antérieur, avant tout appel
    assert len(list((tmp_path / "runs").iterdir())) == 1
    with pytest.raises(lb.Refus, match="déjà été joué"):
        lb.verifier_bras_jamais_joue(lignee)
    (run / "manifeste-lanceur-fin.json").unlink()
    with pytest.raises(lb.Refus, match="état du bras inconnu"):
        lb.verifier_bras_jamais_joue(lignee)
    (run / "manifeste-lanceur-fin.json").write_text(json.dumps({"copies": {"manifeste-bras-non-joue-1.json": "x"}}), encoding="utf-8")
    assert lb.verifier_bras_jamais_joue(lignee) == {"runs_anterieurs_non_joues": [run.name]}
