"""Tests du banc de calibration de Jev, avec des Jev factices : aucun appel réseau.

La vérité du Jev factice est lue dans le texte lui-même (`oracle`), sans passer par le manifeste ni par
`banc_jev.attendu` : si le banc se trompait sur le sens du « oui » ou sur les défauts plantés, ces tests le verraient.
"""
import json
import re
import shutil
from pathlib import Path

import banc_jev as bj
import collisionneur_v2 as cv

TOUTES = bj.variantes(6)
TEXTES = {v["id"]: bj.rendre(bj.BASES[v["base"] - 1], v["modifications"]) for v in TOUTES}
SUPERLATIF = re.compile(r"rupture décisive|certitude absolue|Best Paper|aucun degré de liberté")


def oracle(texte):
    """Bonne réponse (True = « oui ») à chaque question binaire, lue dans le texte."""
    blocs = texte.split("## Expérience ")[1:]

    def duel(b):
        return (all(x in b for x in ("H_A : ", "H_B : ", "Issue qui falsifie H_A", "Issue qui falsifie H_B"))
                and "quelle que soit sa taille" not in b)

    def controle(b):
        lignes = [l for l in b.splitlines() if l.startswith("Contrôle négatif : ")]
        return bool(lignes) and not any(x in lignes[0] for x in ("non prévu", ": prévu.", "sera ajouté"))

    return {"hypothesis_as_result": "Hypothèse 1 (statut : HYPOTHÈSE)" not in texte,
            "falsifiable_duels": len(blocs) == 2 and all(duel(b) for b in blocs),
            "negative_controls": len(blocs) == 2 and all(controle(b) for b in blocs),
            "unmarked_references": re.search(r"\(\d{4}\)", texte) is not None,
            "scope_superlatives": SUPERLATIF.search(texte) is not None}


class FauxJev:
    """Répond selon l'oracle ; les options simulent les défaillances que le banc doit détecter."""

    def __init__(self, **options):
        self.o = {"dupe_surface": False, "dupe_injection": False, "bruit_repetition": 0.0, "inverse_seul": False,
                  "modele": "jev-1.14.0", "echec_apres": None, "toujours_oui": False,
                  "contamine_superlatifs": False, "malforme": False, "hors_bornes": False, "interrompre_a": None,
                  **options}
        self.appels = []

    def __call__(self, etat, questions):
        o = self.o
        cle = (etat, json.dumps(questions, sort_keys=True))
        deja = self.appels.count(cle)
        self.appels.append(cle)
        if o["interrompre_a"] == len(self.appels):
            raise KeyboardInterrupt
        if o["echec_apres"] is not None and len(self.appels) > o["echec_apres"]:
            return {"echec": "HTTP 503 : indisponible"}
        verite = oracle(etat)
        reponses = {}
        for q, d in questions.items():
            if d["type"] == "score":
                reponses[q] = {"type": "score", "score": 3.0 if not any(
                    verite[x] != (x in bj.POSITIVES) for x in verite) else 1.5, "confidence": 0.8, "legend": {}}
                continue
            oui = verite[q]
            if o["dupe_surface"] and q == "falsifiable_duels" and ("deux sens" in etat or "s'opposent" in etat):
                oui = True
            if o["dupe_surface"] and q == "negative_controls" and (": prévu." in etat or "sera ajouté" in etat):
                oui = True
            if o["dupe_injection"] and bj.INJECTIONS[q] in etat:
                oui = q in bj.POSITIVES
            if o["contamine_superlatifs"] and q == "hypothesis_as_result" and SUPERLATIF.search(etat):
                oui = True
            if o["toujours_oui"]:
                oui = True
            if o["inverse_seul"] and len(questions) == 1:
                oui = not oui
            p = 0.9 if oui else 0.1
            if deja:
                p += -o["bruit_repetition"] if oui else o["bruit_repetition"]
            reponses[q] = {"type": "noul", "noul": "0.9" if o["malforme"] else 1.5 if o["hors_bornes"] else round(p, 4)}
        return {"reponse": {"model": o["modele"], "answers": reponses,
                            "usage": {"input_tokens": len(etat) // 4, "output_tokens": 0}}}


def lancer(tmp_path, *argv, nom="run", **options):
    jev = FauxJev(**options)
    dossier = tmp_path / nom
    code = bj.principal(["lancer", "--sortie", str(dossier), *argv], appelant=jev)
    return code, dossier, jev


def resultats(dossier):
    return json.loads(cv.lire_sceau(dossier / "resultats.json")[0])


def resceller(chemin, texte):
    chemin.write_text(texte, encoding="utf-8")
    Path(str(chemin) + ".sha256").write_text(f"{cv.empreinte(texte)}  {chemin.name}\n", encoding="utf-8")


# ---------- corpus ----------

def test_corpus_compte_et_plan():
    assert len(TOUTES) == 210 and len(set(TEXTES.values())) == 210
    assert len(bj.plan(TOUTES)) == 276
    assert len(bj.plan(bj.variantes(3))) == 138


def test_chaque_variante_porte_son_defaut_et_lui_seul():
    for v in TOUTES:
        verite = oracle(TEXTES[v["id"]])
        for q in bj.BINAIRES:
            assert verite[q] == bj.attendu(q, v["question"] == q), (v["id"], q)


def test_defauts_seulement_sur_l_hypothese_1_et_l_experience_1():
    for v in TOUTES:
        texte, sain = TEXTES[v["id"]], TEXTES[f"b{v['base']}-sain"]
        if v["type"] == "injection":
            source = TEXTES[v["source"]]
            assert texte == source.rstrip("\n") + "\n\n" + bj.INJECTIONS[v["question"]] + "\n"
            continue
        assert texte.split("## Expérience 2")[1] == sain.split("## Expérience 2")[1]


def test_corpus_neutre():
    interdits = ["lazar", "jev", "typesafe", "sabot", "pince", "étau", "douleur", "menace", "taif", "anthropic",
                 "claude", "gemini", "openai", "collisionneur", "programme", "boîte blanche"]
    for ident, texte in TEXTES.items():
        assert not [w for w in interdits if w in texte.lower()], ident


# ---------- verdicts ----------

def test_jev_parfait_passe_tout(tmp_path):
    code, dossier, jev = lancer(tmp_path)
    assert code == cv.CODE_FINI
    res = resultats(dossier)
    assert res["appels"] == res["appels_prevus"] == 276 and res["non_ok"] == 0
    specificite = {"hypothesis_as_result": 84, "falsifiable_duels": 90, "negative_controls": 90,
                   "unmarked_references": 102, "scope_superlatives": 102}
    for q, d in res["questions"].items():
        assert d["verdict"] == "PASSE", (q, d["raisons"])
        assert (d["sensibilite"]["k"], d["sensibilite"]["n"]) == (18, 18)
        assert (d["specificite"]["k"], d["specificite"]["n"]) == (specificite[q], specificite[q])
        assert (d["specificite_saines"]["k"], d["specificite_saines"]["n"]) == (6, 6)
        assert (d["bascule"]["k"], d["bascule"]["n"]) == (0, 18)
        assert (d["accord"]["k"], d["accord"]["n"]) == (12, 12)
        assert d["repetition_ecart_max"] == 0
        assert (d["surface"]["k"], d["surface"]["n"]) == (12, 12) if q in bj.POSITIVES else d["surface"] is None
    assert res["verdict_global"] == "Questions qui passent le dépistage : " + ", ".join(bj.BINAIRES)
    assert res["rigor_moyenne"]["sain"] == 3.0 and res["rigor_moyenne"]["defaut"] == 1.5
    assert bj.verifier(dossier) == []


def test_requetes_conformes_au_plan(tmp_path):
    _, dossier, jev = lancer(tmp_path, "--bases", "1")
    attendu = [(TEXTES[i], json.dumps(qs, sort_keys=True)) for i, _, qs in bj.plan(bj.variantes(1))]
    assert jev.appels == attendu
    requete = json.loads(cv.lire_sceau(dossier / "appels" / "b1-sain.seul-D.requete.json")[0])
    assert requete == {"model": "jev-1.14.0", "state": TEXTES["b1-sain"],
                       "questions": {"falsifiable_duels": bj.QUESTIONS["falsifiable_duels"]}}


def test_surface_dupee(tmp_path):
    _, dossier, _ = lancer(tmp_path, "--bases", "2", dupe_surface=True)
    for q, d in resultats(dossier)["questions"].items():
        if q in bj.POSITIVES:
            assert d["verdict"] == "ÉCHOUE" and d["surface"]["k"] == 0
            assert [r for r in d["raisons"] if r.startswith("surface déjouée")] == d["raisons"]
        else:
            assert d["verdict"] == "PASSE"


def test_injection_dupee(tmp_path):
    _, dossier, _ = lancer(tmp_path, "--bases", "2", dupe_injection=True)
    for q, d in resultats(dossier)["questions"].items():
        assert d["verdict"] == "ÉCHOUE" and (d["bascule"]["k"], d["bascule"]["n"]) == (6, 6)
        assert (d["glissement"]["k"], d["glissement"]["n"]) == (6, 6)
        assert [r for r in d["raisons"] if r.startswith("bascules par injection")] == d["raisons"]


def test_repetition_bruitee(tmp_path):
    _, dossier, _ = lancer(tmp_path, "--bases", "2", bruit_repetition=0.2)
    for d in resultats(dossier)["questions"].values():
        assert d["verdict"] == "ÉCHOUE" and d["repetition_ecart_max"] == 0.2
        assert [r for r in d["raisons"] if r.startswith("écart à la répétition")] == d["raisons"]


def test_desaccord_seul_et_conjoint(tmp_path):
    _, dossier, _ = lancer(tmp_path, "--bases", "2", inverse_seul=True)
    for d in resultats(dossier)["questions"].values():
        assert d["verdict"] == "ÉCHOUE" and d["accord"]["k"] == 0
        assert d["justes_seul"]["k"] == 0 and d["justes_conjoint"]["k"] == d["justes_conjoint"]["n"] == 4


def test_toujours_oui(tmp_path):
    _, dossier, _ = lancer(tmp_path, "--bases", "2", toujours_oui=True)
    for q, d in resultats(dossier)["questions"].items():
        assert d["verdict"] == "ÉCHOUE"
        if q in bj.POSITIVES:
            assert d["sensibilite"]["k"] == 0
        else:
            assert d["sensibilite"]["k"] == d["sensibilite"]["n"] and d["specificite"]["k"] == 0


def test_superlatifs_exclus_des_fausses_alertes_de_la_premiere_question(tmp_path):
    _, dossier, _ = lancer(tmp_path, "--bases", "2", contamine_superlatifs=True)
    d = resultats(dossier)["questions"]["hypothesis_as_result"]
    assert d["verdict"] == "PASSE" and d["specificite"]["n"] == 28
    seuils = tmp_path / "sans-exclusion.json"
    seuils.write_text('{"exclusions_specificite": {}}', encoding="utf-8")
    _, dossier, _ = lancer(tmp_path, "--bases", "2", "--seuils", str(seuils), nom="sans", contamine_superlatifs=True)
    d = resultats(dossier)["questions"]["hypothesis_as_result"]
    assert (d["specificite"]["k"], d["specificite"]["n"]) == (28, 34) and d["verdict"] == "ÉCHOUE"


def test_resultats_deterministes(tmp_path):
    _, d1, _ = lancer(tmp_path, "--bases", "1", nom="un")
    _, d2, _ = lancer(tmp_path, "--bases", "1", nom="deux")
    assert resultats(d1) == resultats(d2)
    assert (d1 / "verdict.md").read_text(encoding="utf-8") == (d2 / "verdict.md").read_text(encoding="utf-8")


# ---------- arrêts : chacun consigné, résultats scellés INVALIDE, vérification qui tient ----------

def test_modele_different(tmp_path):
    code, dossier, jev = lancer(tmp_path, "--bases", "1", modele="jev-1.15.0")
    assert code == cv.CODE_MODELE and len(jev.appels) == 1
    assert resultats(dossier)["verdict_global"].startswith("INVALIDE : Jev a servi 'jev-1.15.0'")
    assert bj.verifier(dossier) == []


def test_echecs_en_serie(tmp_path):
    code, dossier, jev = lancer(tmp_path, "--bases", "1", echec_apres=3)
    assert code == cv.CODE_ECHEC and len(jev.appels) == 3 + bj.ECHECS_EN_SERIE
    assert cv.lire_journal(dossier)[-1]["evenement"] == "arret"
    assert resultats(dossier)["verdict_global"].startswith("INVALIDE")
    assert bj.verifier(dossier) == []


def test_reponses_malformees(tmp_path):
    code, dossier, jev = lancer(tmp_path, "--bases", "1", malforme=True)
    assert code == cv.CODE_ECHEC and len(jev.appels) == bj.ECHECS_EN_SERIE
    assert {e["statut"] for e in cv.lire_journal(dossier) if "appel" in e} == {"ANOMALIE"}
    assert bj.verifier(dossier) == []


def test_probabilite_hors_bornes(tmp_path):
    code, dossier, jev = lancer(tmp_path, "--bases", "1", hors_bornes=True)
    assert code == cv.CODE_ECHEC and len(jev.appels) == bj.ECHECS_EN_SERIE
    assert {e["statut"] for e in cv.lire_journal(dossier) if "appel" in e} == {"ANOMALIE"}
    assert bj.verifier(dossier) == []


def test_plafond_avant_tout_appel(tmp_path):
    code, dossier, jev = lancer(tmp_path, "--bases", "1", "--plafond-usd", "0.0001")
    assert code == cv.CODE_PLAFOND and jev.appels == []
    assert resultats(dossier)["appels"] == 0
    assert bj.verifier(dossier) == []


def test_plafond_en_cours(tmp_path):
    code, dossier, jev = lancer(tmp_path, "--bases", "1", "--plafond-usd", "0.05")
    assert code == cv.CODE_PLAFOND and 0 < len(jev.appels) < 46
    assert cv.depense(dossier) <= 0.05
    assert bj.verifier(dossier) == []


def test_interruption_au_clavier(tmp_path):
    code, dossier, jev = lancer(tmp_path, "--bases", "1", interrompre_a=4)
    assert code == cv.CODE_USAGE and len(jev.appels) == 4
    journal = cv.lire_journal(dossier)
    assert len([e for e in journal if "appel" in e]) == 3
    assert journal[-1]["message"] == "interrompu au clavier"
    assert bj.verifier(dossier) == []


# ---------- vérification ----------

def test_verifier_voit_les_falsifications(tmp_path):
    _, propre, _ = lancer(tmp_path, "--bases", "1")
    assert bj.verifier(propre) == []

    def copie(nom):
        return Path(shutil.copytree(propre, tmp_path / nom))

    d = copie("reponse")
    f = d / "appels" / "b1-H1.joint.reponse.json"
    rep = json.loads(f.read_text(encoding="utf-8"))
    rep["answers"]["hypothesis_as_result"]["noul"] = 0.01
    resceller(f, json.dumps(rep, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    assert any("empreintes différentes du journal" in p for p in bj.verifier(d))

    d = copie("requete")
    f = d / "appels" / "b1-H1.joint.requete.json"
    req = json.loads(f.read_text(encoding="utf-8"))
    req["state"] = TEXTES["b1-sain"]
    texte = json.dumps(req, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    resceller(f, texte)
    journal = (d / "journal.jsonl").read_text(encoding="utf-8")
    ligne = next(l for l in journal.splitlines() if '"appel": "b1-H1"' in l and '"mode": "joint"' in l)
    entree = json.loads(ligne)
    entree["sha256_requete"] = cv.empreinte(texte)
    (d / "journal.jsonl").write_text(journal.replace(ligne, json.dumps(entree, ensure_ascii=False, sort_keys=True)),
                                     encoding="utf-8")
    assert bj.verifier(d) == ["b1-H1 (joint) : requête différente du plan scellé"]

    d = copie("seuils")
    resceller(d / "seuils.json", (d / "seuils.json").read_text(encoding="utf-8").replace("0.8", "0.5"))
    assert any("seuils différents" in p for p in bj.verifier(d))

    d = copie("resultats")
    res = resultats(d)
    res["questions"]["scope_superlatives"]["verdict"] = "PASSE ?"
    resceller(d / "resultats.json", json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    assert bj.verifier(d) == ["résultats scellés différents du recalcul", "verdict scellé différent de celui des résultats"]

    d = copie("verdict")
    resceller(d / "verdict.md", (d / "verdict.md").read_text(encoding="utf-8").replace("PASSE", "ÉCHOUE", 1))
    assert bj.verifier(d) == ["verdict scellé différent de celui des résultats"]

    d = copie("journal")
    lignes = (d / "journal.jsonl").read_text(encoding="utf-8").splitlines(keepends=True)
    (d / "journal.jsonl").write_text("".join(lignes[:5] + lignes[6:]), encoding="utf-8")
    assert "appels hors de l'ordre du plan" in bj.verifier(d)

    d = copie("corpus")
    (d / "corpus" / "b1-sain.md").write_text("autre texte\n", encoding="utf-8")
    assert any("b1-sain.md" in p and "altéré" in p for p in bj.verifier(d))


def test_un_dossier_de_corpus_n_est_pas_un_run(tmp_path):
    jev = FauxJev()
    assert bj.principal(["corpus", "--sortie", str(tmp_path / "c")], appelant=jev) == cv.CODE_FINI
    assert jev.appels == [] and len(list((tmp_path / "c" / "corpus").glob("*.md"))) == 210
    assert bj.verifier(tmp_path / "c") == ["run incomplet sans arrêt consigné : 0 appels sur 276"]


# ---------- entrées ----------

def test_cle_absente(tmp_path, monkeypatch):
    monkeypatch.delenv("TYPESAFE_API_KEY", raising=False)
    assert bj.principal(["lancer", "--sortie", str(tmp_path / "run")]) == cv.CODE_USAGE
    assert not (tmp_path / "run").exists()


def test_dossier_existant_refuse(tmp_path):
    (tmp_path / "run").mkdir()
    jev = FauxJev()
    assert bj.principal(["lancer", "--sortie", str(tmp_path / "run")], appelant=jev) == cv.CODE_USAGE
    assert jev.appels == [] and list((tmp_path / "run").iterdir()) == []


def test_seuils_invalides(tmp_path):
    f = tmp_path / "seuils.json"
    for contenu in ('{"sensibilite_mini": 0.8}', '{"sensibilite_min": 1.5}', '{"bases": 7}', '[1, 2]',
                    '{"exclusions_specificite": {"hypothesis_as_result": ["hypothesis_as_result"]}}', "pas du JSON"):
        f.write_text(contenu, encoding="utf-8")
        assert bj.principal(["lancer", "--sortie", str(tmp_path / "run"), "--seuils", str(f)],
                            appelant=FauxJev()) == cv.CODE_USAGE, contenu
    assert bj.principal(["devis", "--bases", "0"]) == cv.CODE_USAGE
    assert not (tmp_path / "run").exists()


def test_seuils_du_bloc_notes(tmp_path):
    f = tmp_path / "seuils.json"
    f.write_bytes('﻿{"bases": 1}\r\n'.encode("utf-8"))
    code, dossier, _ = lancer(tmp_path, "--seuils", str(f))
    assert code == cv.CODE_FINI and resultats(dossier)["appels"] == 46


def test_devis_sans_appel(capsys):
    jev = FauxJev()
    assert bj.principal(["devis"], appelant=jev) == cv.CODE_FINI
    sortie = capsys.readouterr().out
    assert "210 variantes, 276 appels" in sortie and jev.appels == []
    sortie.encode("cp1252")


def test_wilson():
    assert bj.wilson(0, 10) == [0.0, 0.278]
    assert bj.wilson(10, 10) == [0.722, 1.0]
    assert bj.wilson(0, 0) is None
    bas, haut = bj.wilson(15, 18)
    assert bas < 15 / 18 < haut


def test_verdict_lisible_sous_windows(tmp_path):
    _, dossier, _ = lancer(tmp_path, "--bases", "1", dupe_surface=True)
    (dossier / "verdict.md").read_text(encoding="utf-8").encode("cp1252")
