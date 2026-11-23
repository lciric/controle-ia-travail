"""Essais des chargeurs des trois formats des sessions habilitées (formats_v1) : chaque garde sur un cas sain et sur un
artefact (R5), fichiers fabriqués seulement."""
import copy
import csv
import json

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.sondes_v2 import formats_v1 as fm
from controle_ia.sondes_v2 import programme_monde_plante_v4 as prog
from controle_ia.sondes_v2 import statistiques_v2 as st

H = "a" * 64


def _ecrire(chemin, texte):
    chemin.write_text(texte, encoding="utf-8")
    sceller(chemin)
    return chemin


# --------------------------------------------------------------------------------------------- note des effectifs

def _pli(pli, taches, controle=0, actions_ctrl=0):
    return {"pli": pli, "taches_tenues": taches,
            "actions": {c: 3 * taches for c in fm.CASES},
            "chemins": {"adaptateur|saboteur": "origine", "nu|saboteur": "relu", "adaptateur|honnete": "relu",
                        "nu|honnete": "origine"},
            "actions_en_origine_et_en_relu": actions_ctrl, "taches_avec_controle_du_chemin": controle}


def _note():
    return {
        "format": "note-effectifs-sondes-v2-v1", "redigee_par": "session_essai", "date_utc": "2026-11-23T00:00:00Z",
        "aveuglement": {"activations": "non ouvertes", "scores": "non ouverts", "table_de_l_ouvreur": "non ouverte",
                        "verdict_adaptateurs_jumeaux": "non ouvert"},
        "activations": {
            "dossier_run": "runs/x", "inventaire_sha256": H, "garde_sha256": H, "regle_garde": "une_sur_dix",
            "couches_gardees": [15],
            "chemin_de_calcul": {"programme": "p@0", "precision": "bf16", "mode": "relu à texte imposé",
                                 "gabarit": "g", "source": "manifeste", "identique_pour_toutes_les_series": True},
            "series": [{"nom": "nu", "categorie": "nu", "cles": 50}, {"nom": "a1", "categorie": "adaptateur", "cles": 50}],
            "cles_communes": {"definition": "clés de la série nu", "actions": 50, "taches": 20,
                              "taches_par_nombre_d_actions": {"1": 0, "2": 10, "3": 10, "4_ou_plus": 0},
                              "distinctes_des_cles_propres": True},
            "nu_relit_les_cles_communes": True},
        "scores_bbis": {"table": {"chemin": "t.jsonl", "sha256": H, "ligne_registre": "SCORES-BBIS 1"},
                        "colonnes": ["dose", "pli"],
                        "doses": [{"dose": "1", "plis": [_pli("0", 6), _pli("1", 6)]},
                                  {"dose": "2", "plis": [_pli("0", 5), _pli("1", 6)]}],
                        "nombre_de_doses": 2},
        "cases_de_l_epreuve_plantee": {"etalon": {"taches": 20, "actions": 2},  # 50/20 = 2,5 → 2 (moitié vers le bas)
                                       "complet": {"paires": 8, "taches": 11, "actions": 3, "doses_holm": 2},
                                       "extension_taches_actions": False},
        "minimums": {"cles_communes": "atteints", "rejeu_par_dose": {"1": "atteints", "2": "atteints"}},
        "reserves": []}


def _note_md(tmp_path, n, nom="note.md"):
    return _ecrire(tmp_path / nom, "# Note\n\nEn-tête.\n\n```json\n" + json.dumps(n, ensure_ascii=False, indent=1)
                   + "\n```\n\nRéserves : aucune.\n")


def test_note_cas_sain(tmp_path):
    r = fm.charger_note_effectifs(_note_md(tmp_path, _note()))
    assert r["doses_holm"] == 2 and r["controle_du_chemin"] == "contrôle absent" and len(r["sha256"]) == 64
    assert fm.arrondi_moitie_bas(2.5) == 2 and fm.arrondi_moitie_bas(2.6) == 3 and fm.arrondi_moitie_bas(3.5) == 3


@pytest.mark.parametrize("abimer,motif", [
    (lambda n: n.pop("reserves"), "manquants"),
    (lambda n: n.update(en_trop=1), "en trop"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["etalon"].update(taches=20.0), "entier"),
    (lambda n: n["scores_bbis"]["doses"][0]["plis"][0]["actions"].update({"nu|saboteur": "3"}), "entier"),
    (lambda n: n["activations"].update(famille_des_series="x"), "rôle"),
    (lambda n: n["activations"]["series"].append({"nom": "jumeau-1", "categorie": "adaptateur", "cles": 50}), "rôle"),
    (lambda n: n["scores_bbis"]["doses"][0]["plis"][0]["chemins"].update({"nu|saboteur": "autre"}), "origine"),
    (lambda n: n["cases_de_l_epreuve_plantee"].update(extension_taches_actions=True), "extension"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["complet"].update(doses_holm=1), "doses"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["etalon"].update(actions=3), "étalon"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["complet"].update(taches=12), "minimum"),
    (lambda n: n["aveuglement"].update(scores="ouverts"), "non ouvert"),
])
def test_note_artefacts(tmp_path, abimer, motif):
    n = _note()
    abimer(n)
    with pytest.raises(GardeArret, match=motif):
        fm.charger_note_effectifs(_note_md(tmp_path, n))


def test_note_compagnon_faux_et_cas_mixte(tmp_path):
    c = _note_md(tmp_path, _note())
    c.write_text(c.read_text(encoding="utf-8").replace("Réserves : aucune.", "Réserves : une."), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        fm.charger_note_effectifs(c)
    n = _note()
    n["scores_bbis"]["doses"][0]["plis"][0].update(actions_en_origine_et_en_relu=4, taches_avec_controle_du_chemin=2)
    assert fm.charger_note_effectifs(_note_md(tmp_path, n, "m.md"))["controle_du_chemin"].startswith("cas mixte")
    n = _note()
    for d in n["scores_bbis"]["doses"]:
        for p in d["plis"]:
            p.update(actions_en_origine_et_en_relu=1, taches_avec_controle_du_chemin=p["taches_tenues"])
    assert fm.charger_note_effectifs(_note_md(tmp_path, n, "t.md"))["controle_du_chemin"] == \
        "toutes les tâches contrôlées"
    deux = _ecrire(tmp_path / "deux.md", "```json\n{}\n```\n```json\n{}\n```\n")
    with pytest.raises(GardeArret, match="blocs JSON"):
        fm.charger_note_effectifs(deux)


def test_note_dans_le_programme(tmp_path):
    c = _note_md(tmp_path, _note())
    n = fm.charger_note_effectifs(c)["note"]
    from controle_ia.sondes_v2 import monde_plante_v4 as mp
    gr = mp.charger_verites()[0]["grille_etalon"]
    cas, D = prog.cas_depuis_note(n, "complet", gr)
    assert cas == [(8, 11, 3)] and D == 2
    cas, _ = prog.cas_depuis_note(n, "etalon", gr)
    assert len(cas) == 52 and {(t, a) for _, _, t, a in cas} == {(20, 2)}
    with pytest.raises(GardeArret, match="contredit"):
        prog.main(["--sortie", str(tmp_path / "s"), "--note-effectifs", str(c), "--mode", "complet",
                   "--doses-rejeu", "3"])
    with pytest.raises(GardeArret, match="--mode"):
        prog.main(["--sortie", str(tmp_path / "s"), "--note-effectifs", str(c)])


# ------------------------------------------------------------------------- table des scores et correspondance

def _lignes_brutes(n_taches=8):
    out = []
    for t in range(n_taches):
        for so, so_b in (("saboteur", "S"), ("honnete", "H")):
            for a in range(3):
                for po, po_b in (("adaptateur", "A"), ("nu", "N")):
                    out.append({"d": "1", "f": str(t % 2), "src": so_b, "w": po_b, "task": f"t{t}",
                                "key": f"t{t}-{so}-{a}", "s": float(t + a + (po == "adaptateur")),
                                "len": 10 + a, "step": a, "probe": "dm", "held": "oui"})
    return out


def _corr(sha, fmt="jsonl", **change):
    c = {"format": "correspondance-rejeu-croise-v1", "redigee_par": "session_essai", "date_utc": "2026-11-23T00:00:00Z",
         "attestation": "aucune colonne de score lue", "selection": {"probe": "dm"},
         "table_source": {"chemin": "t", "sha256": sha, "ligne_registre": "SCORES-BBIS 1", "format_fichier": fmt},
         "colonnes": {"dose": "d", "pli": "f", "source": "src", "poids": "w",
                      "chemin": {"regle": "quatre_cases_du_texte_scelle"}, "tache": "task", "cle": "key", "score": "s",
                      "longueur": "len", "pas": "step", "valeur_declaree": {"absente": True}, "tache_tenue": "held"},
         "valeurs": {"source": {"S": "saboteur", "H": "honnete"}, "poids": {"A": "adaptateur", "N": "nu"},
                     "tache_tenue": {"oui": "true", "non": "false"}}}
    for k, v in change.items():
        c[k] = v
    return c


def _fichiers(tmp_path, lignes, corr=None, fmt="jsonl"):
    tmp_path = tmp_path / f"cas-{len(list(tmp_path.iterdir()))}"  # un dossier par fabrication (R12 au scellement)
    tmp_path.mkdir()
    t = tmp_path / f"table.{fmt}"
    if fmt == "jsonl":
        t.write_text("".join(json.dumps(l) + "\n" for l in lignes), encoding="utf-8")
    else:
        with open(t, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(lignes[0]))
            w.writeheader()
            w.writerows(lignes)
    sha = sceller(t)
    c = corr(sha) if callable(corr) else _corr(sha, fmt)
    cc = _ecrire(tmp_path / "corr.json", json.dumps(c, ensure_ascii=False))
    return t, cc


@pytest.mark.parametrize("fmt", ["jsonl", "csv"])
def test_bbis_cas_sain(tmp_path, fmt):
    t, c = _fichiers(tmp_path, _lignes_brutes(), fmt=fmt)
    lignes, meta = fm.charger_table_bbis(t, c)
    assert len(lignes) == 8 * 2 * 3 * 2 and meta["regles"]["chemin"] == "quatre_cases_du_texte_scelle"
    assert meta["variables_absentes"] == ["valeur_declaree"] and meta["cles_sans_jumelle"] == 0
    assert {(l["poids"], l["source"], l["chemin"]) for l in lignes} == {
        ("adaptateur", "saboteur", "origine"), ("nu", "honnete", "origine"), ("adaptateur", "honnete", "relu"),
        ("nu", "saboteur", "relu")}
    r = st.rejeu_croise(lignes, {n: __import__("numpy").random.default_rng(0) for n in st.GRAINES_NOMMEES},
                        {"alpha": 0.05}, n_tirages=20)["doses"]["1"]
    assert r["motif"] == "aucun" and r["controle_chemin"] == st.CONTROLE_ABSENT


def test_bbis_artefacts(tmp_path):
    t, c = _fichiers(tmp_path, _lignes_brutes())
    t.write_text(t.read_text() + "\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        fm.charger_table_bbis(t, c)
    l = _lignes_brutes()
    l[5]["src"] = "X"
    t, c = _fichiers(tmp_path, l)
    with pytest.raises(GardeArret, match="non prévue"):
        fm.charger_table_bbis(t, c)
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr(sha, colonnes={
        **_corr(sha)["colonnes"], "tache": "absente"}))
    with pytest.raises(GardeArret, match="absente du fichier"):
        fm.charger_table_bbis(t, c)
    l = _lignes_brutes()
    l.append(dict(l[0]))  # une action en double : hors des quatre cases à un seul chemin
    t, c = _fichiers(tmp_path, l)
    with pytest.raises(GardeArret, match="quatre cases"):
        fm.charger_table_bbis(t, c)
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr("b" * 64))
    with pytest.raises(GardeArret, match="table source"):
        fm.charger_table_bbis(t, c)
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr(sha, colonnes={
        **_corr(sha)["colonnes"], "score": {"absente": True}}))
    with pytest.raises(GardeArret, match="non permise"):
        fm.charger_table_bbis(t, c)


def test_bbis_cle_sans_jumelle(tmp_path):
    l = [x for x in _lignes_brutes() if not (x["key"] == "t0-saboteur-0" and x["w"] == "N")]
    t, c = _fichiers(tmp_path, l)
    lignes, meta = fm.charger_table_bbis(t, c)
    assert meta["cles_sans_jumelle"] == 1


# ------------------------------------------------------------------------------------------- table de l'ouvreur

def _garde(tmp_path, series):
    g = {"regle": "une_sur_dix", "fichiers": [f"activations/{s}/c15/t0__p0.npy" for s in series]}
    return _ecrire(tmp_path / "garde-activations.json", json.dumps(g))


def _ouvreur(sha_garde, familles=(("f1", "r1", 0.5, 4), ("f2", "r2", 0.5, 7))):
    series = {"nu": {"type": "nu"}}
    k = 0
    for fam, rec, dose, n in familles:
        for q in range(n):
            for role in ("saboteur", "jumeau"):
                series[f"a{k}"] = {"type": "adaptateur", "empreinte_adaptateur": f"{k:064x}", "dose": dose,
                                   "recette": rec, "famille": fam, "paire": f"{fam}-{q:02d}", "role": role}
                k += 1
    series[f"a{k}"] = {"type": "adaptateur", "empreinte_adaptateur": f"{k:064x}", "dose": 0.5, "recette": "r1",
                       "famille": "f1", "paire": None, "role": "hors_paire"}
    series["propre-a0"] = {"type": "propre", "producteur": "a0"}
    return {"format": "table-ouvreur-sondes-v2-v1", "redigee_par": "session_essai", "date_utc": "2026-11-23T00:00:00Z",
            "sources": {"table_de_l_ouvreur": {"chemin": "x", "sha256": H},
                        "fichier_ferme_des_empreintes": {"chemin": "y", "sha256": H},
                        "verdict_scelle": {"chemin": "v", "sha256": H, "inscrit_au_registre": "R-4242"},
                        "garde_des_activations": {"chemin": "garde-activations.json", "sha256": sha_garde}},
            "series": series}


def _fichiers_ouvreur(tmp_path, abimer=None, series_garde=None):
    o = _ouvreur("0" * 64)
    g = _garde(tmp_path, series_garde or sorted(o["series"]))
    o = _ouvreur((tmp_path / "garde-activations.json.sha256").read_text().split()[0])
    if abimer:
        abimer(o)
    return _ecrire(tmp_path / "ouvreur.json", json.dumps(o)), g


def test_ouvreur_cas_sain(tmp_path):
    t, g = _fichiers_ouvreur(tmp_path)
    reg = tmp_path / "registre.md"
    reg.write_text("… R-4242 : verdict scellé …", encoding="utf-8")
    r = fm.charger_table_ouvreur(t, g, reg)
    assert r["P"] == {"f1": 4, "f2": 7} and r["F"] == 2 and r["cases_etalon"] == {"f1": (4, 2), "f2": (7, 2)}
    assert r["hors_paire"] == 1 and r["propres"] == 1 and r["cases_hors_grille"] == []
    assert r["familles"]["f1"][0] == ("a0", "a1") and r["poids_par_serie"]["nu"] == {"type": "nu"}
    assert r["poids_par_serie"]["a0"]["empreinte_adaptateur"] == f"{0:064x}"
    assert r["testables"] == ["f2"]  # 7 paires : 2^-5 ≤ 0,05 ; 4 paires jamais testables


@pytest.mark.parametrize("abimer,motif", [
    (lambda o: o["series"]["a1"].update(role="saboteur"), "un saboteur et un jumeau"),
    (lambda o: o["series"]["a1"].update(famille="f2", recette="r2"), "à cheval"),
    (lambda o: o["series"]["a2"].update(dose=0.7), "mêlées"),
    (lambda o: o["series"]["a1"].update(role="témoin"), "hors de la liste"),
    (lambda o: o["sources"]["verdict_scelle"].update(inscrit_au_registre=""), "non inscrit"),
    (lambda o: o["series"].pop("a3"), "manquantes"),
    (lambda o: o["series"].update({"a99": dict(o["series"]["a0"])}), "en trop"),
    (lambda o: o["series"]["a1"].update(paire=None), "sans paire"),
])
def test_ouvreur_artefacts(tmp_path, abimer, motif):
    t, g = _fichiers_ouvreur(tmp_path, abimer)
    with pytest.raises(GardeArret, match=motif):
        fm.charger_table_ouvreur(t, g)


def test_ouvreur_empreinte_et_registre(tmp_path):
    t, g = _fichiers_ouvreur(tmp_path)
    t.write_text(t.read_text().replace("R-4242", "R-4243"), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        fm.charger_table_ouvreur(t, g)
    t, g = _fichiers_ouvreur(tmp_path)
    reg = tmp_path / "registre.md"
    reg.write_text("R-42420 seulement", encoding="utf-8")
    with pytest.raises(GardeArret, match="absent"):
        fm.charger_table_ouvreur(t, g, reg)
    o = json.loads(t.read_text())
    o2 = copy.deepcopy(o)
    o2["sources"]["garde_des_activations"]["sha256"] = "c" * 64
    t2 = _ecrire(tmp_path / "o2.json", json.dumps(o2))
    with pytest.raises(GardeArret, match="garde des activations"):
        fm.charger_table_ouvreur(t2, g)
