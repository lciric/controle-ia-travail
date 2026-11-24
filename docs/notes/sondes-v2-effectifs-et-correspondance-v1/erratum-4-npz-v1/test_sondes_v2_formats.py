"""Essais des chargeurs des trois formats des sessions habilitées (formats_v1) : chaque garde sur un cas sain et sur un
artefact (R5), fichiers fabriqués seulement."""
import copy
import csv
import json

import numpy as np
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
            "nu_relit_les_cles_communes": True,
            "series_publiques": {"propre": 3, "ancre": 2, "autres_a_nom_public": 0},
            "attestation_series_publiques": fm.ATTESTATION_SERIES_PUBLIQUES,
            "non_propres_aux_cles_communes": True},
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
    assert r["doses_holm"] == 2 and r["cas_mixte"] == "contrôle absent"
    assert r["controle_du_chemin"] == "contrôle absent" and len(r["sha256"]) == 64
    assert r["cas_mixte_par_dose"] == {"1": "contrôle absent", "2": "contrôle absent"}
    assert fm.arrondi_moitie_bas(2.5) == 2 and fm.arrondi_moitie_bas(2.6) == 3 and fm.arrondi_moitie_bas(3.5) == 3


def _note_petite_dose1():
    n = _note()
    # dose 1 à 10 tâches et 1 action par case (20 actions appariées < 40) -> non atteints
    for p in n["scores_bbis"]["doses"][0]["plis"]:
        p["taches_tenues"] = 5
        p["actions"] = {c: 5 for c in fm.CASES}
    n["cases_de_l_epreuve_plantee"]["complet"].update(taches=10, actions=1)
    n["minimums"]["rejeu_par_dose"]["1"] = "non atteints"
    return n


@pytest.mark.parametrize("abimer,motif", [
    (lambda n: n.pop("reserves"), "manquants"),
    (lambda n: n.update(en_trop=1), "en trop"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["etalon"].update(taches=20.0), "entier"),
    (lambda n: n["scores_bbis"]["doses"][0]["plis"][0]["actions"].update({"nu|saboteur": "3"}), "entier"),
    (lambda n: n["activations"].update(famille_des_series="x"), "rôle"),
    (lambda n: n["activations"]["series"].append({"nom": "jumeau-1", "categorie": "adaptateur", "cles": 50}), "rôle"),
    # option A de la garde des mots de rôle : séries publiques comptées, jamais nommées
    (lambda n: n["activations"]["series"].append({"nom": "propre-A1-saboteur", "categorie": "propre", "cles": 5}),
     "rôle"),
    (lambda n: n["activations"].pop("series_publiques"), "manquants"),
    (lambda n: n["activations"]["series_publiques"].update(propre=1.5), "entier"),
    (lambda n: n["activations"]["series_publiques"].update(propre_a1_saboteur=1), "rôle"),
    (lambda n: n["activations"]["series_publiques"].pop("ancre"), "manquants"),
    (lambda n: n["activations"].update(attestation_series_publiques="oui"), "attestation"),
    (lambda n: n["activations"]["series_publiques"].update(autres=1), "en trop"),
    (lambda n: n["activations"].update(non_propres_aux_cles_communes="oui"), "booléen"),
    (lambda n: n["activations"].update(non_propres_aux_cles_communes=False), "sans réserve"),
    (lambda n: n["activations"].pop("non_propres_aux_cles_communes"), "manquants"),
    (lambda n: n["activations"]["series_publiques"].update(propre=-1), "entier"),
    (lambda n: n["activations"]["series_publiques"].update(ancre=True), "entier"),
    (lambda n: n["activations"].pop("attestation_series_publiques"), "manquants"),
    (lambda n: n["activations"]["cles_communes"].update(definition="clés du saboteur"), "valeur textuelle"),
    (lambda n: n["activations"]["chemin_de_calcul"].update(gabarit="gabarit-jumeau"), "valeur textuelle"),
    (lambda n: n["scores_bbis"]["doses"][0]["plis"][0]["chemins"].update({"nu|saboteur": "autre"}), "origine"),
    (lambda n: n["cases_de_l_epreuve_plantee"].update(extension_taches_actions=True), "extension"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["complet"].update(doses_holm=1), "doses"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["etalon"].update(actions=3), "étalon"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["complet"].update(taches=12), "minimum"),
    (lambda n: n["aveuglement"].update(scores="ouverts"), "non ouvert"),
    # M1 : cohérence de la case complète (actions et paires == 8)
    (lambda n: n["cases_de_l_epreuve_plantee"]["complet"].update(actions=2), "actions de la case complète"),
    (lambda n: n["cases_de_l_epreuve_plantee"]["complet"].update(paires=6), "paires de la case complète"),
    # m4 : contrôles de valeur de la note
    (lambda n: n["minimums"].update(cles_communes="oui"), "atteints"),
    (lambda n: n["minimums"].update(cles_communes="non atteints"), "contredit la règle"),
    (lambda n: n["minimums"]["rejeu_par_dose"].pop("2"), "manquants"),
    (lambda n: n["minimums"]["rejeu_par_dose"].update({"1": "non atteints"}), "contredit les effectifs"),
    (lambda n: n["activations"]["chemin_de_calcul"].update(source="devinette"), "source"),
    (lambda n: n["activations"]["chemin_de_calcul"].update(identique_pour_toutes_les_series="oui"), "booléen"),
    (lambda n: n["activations"]["chemin_de_calcul"].update(identique_pour_toutes_les_series=False), "sans réserve"),
    (lambda n: n["activations"].update(nu_relit_les_cles_communes="oui"), "booléen"),
    (lambda n: n["activations"].update(nu_relit_les_cles_communes=False), "sans réserve"),
    (lambda n: n["activations"]["series"].append({"nom": "nu-bis", "categorie": "nu", "cles": 50}), "une série « nu »"),
    (lambda n: n["scores_bbis"]["doses"][1].update(dose="1"), "dose en double"),
    (lambda n: n["scores_bbis"]["doses"][0]["plis"][0].update(actions_en_origine_et_en_relu=3, taches_avec_controle_du_chemin=0), "incohérence"),
    (lambda n: n["scores_bbis"]["doses"][0]["plis"][0].update(actions_en_origine_et_en_relu=0, taches_avec_controle_du_chemin=1), "incohérence"),
    # m9 : empreinte hexadécimale mal formée et nombre_de_doses différent du nombre de doses listées
    (lambda n: n["activations"].update(inventaire_sha256="zz" * 32), "64 hexadécimaux"),
    (lambda n: n["scores_bbis"].update(nombre_de_doses=3), "nombre de doses listées"),
    (lambda n: n["activations"]["cles_communes"]["taches_par_nombre_d_actions"].update({"1": 1}), "somme de taches_par_nombre_d_actions"),
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
    # cas sain avec minimums non atteints sur la dose 1
    assert fm.charger_note_effectifs(_note_md(tmp_path, _note_petite_dose1(), "petite.md"))["note"]["minimums"]["rejeu_par_dose"]["1"] == "non atteints"
    # m5 : dose 1 entièrement contrôlée et dose 2 sans contrôle -> pas de cas mixte (E-8 se lit par dose)
    n_pures = _note()
    for p in n_pures["scores_bbis"]["doses"][0]["plis"]:
        p.update(actions_en_origine_et_en_relu=2, taches_avec_controle_du_chemin=p["taches_tenues"])
    res_pures = fm.charger_note_effectifs(_note_md(tmp_path, n_pures, "pures.md"))
    assert res_pures["cas_mixte"] == "par dose : contrôle absent ou toutes les tâches contrôlées (aucun cas mixte)"
    assert res_pures["cas_mixte_par_dose"] == {"1": "toutes les tâches contrôlées", "2": "contrôle absent"}
    # Cas mixte véritable dans une dose
    n = _note()
    n["scores_bbis"]["doses"][0]["plis"][0].update(actions_en_origine_et_en_relu=4, taches_avec_controle_du_chemin=2)
    res_m = fm.charger_note_effectifs(_note_md(tmp_path, n, "m.md"))
    assert res_m["cas_mixte"].startswith("cas mixte")
    assert res_m["cas_mixte_par_dose"]["1"].startswith("cas mixte")
    assert res_m["cas_mixte_par_dose"]["2"] == "contrôle absent"
    n = _note()
    for d in n["scores_bbis"]["doses"]:
        for p in d["plis"]:
            p.update(actions_en_origine_et_en_relu=1, taches_avec_controle_du_chemin=p["taches_tenues"])
    assert fm.charger_note_effectifs(_note_md(tmp_path, n, "t.md"))["cas_mixte"] == \
        "toutes les tâches contrôlées"
    # m4 : identique_pour_toutes_les_series faux avec réserve inscrite passe
    n_res = _note()
    n_res["activations"]["chemin_de_calcul"]["identique_pour_toutes_les_series"] = False
    n_res["reserves"].append("a1 a un chemin différent")
    assert fm.charger_note_effectifs(_note_md(tmp_path, n_res, "res.md"))["cas_mixte"] == "contrôle absent"
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


def test_bbis_valeur_declaree_presente_avec_vides(tmp_path):
    l = _lignes_brutes()
    for i, r in enumerate(l):
        r["vd"] = "" if i % 2 == 0 else float(i)
    t, c = _fichiers(tmp_path, l, corr=lambda sha: _corr(sha, colonnes={
        **_corr(sha)["colonnes"], "valeur_declaree": "vd"}))
    lignes, meta = fm.charger_table_bbis(t, c)
    assert meta["variables_absentes"] == [] and any(np.isnan(x["valeur_declaree"]) for x in lignes)
    l[0]["vd"] = "nan_txt"
    t2, c2 = _fichiers(tmp_path, l, corr=lambda sha: _corr(sha, colonnes={
        **_corr(sha)["colonnes"], "valeur_declaree": "vd"}))
    with pytest.raises(GardeArret, match="non numérique"):
        fm.charger_table_bbis(t2, c2)


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
    with pytest.raises(GardeArret, match="demande une colonne"):
        fm.charger_table_bbis(t, c)
    # m3 : valeurs non finies ou non numériques pour longueur, pas, score
    for champ, val in (("len", float("nan")), ("len", float("inf")), ("len", "abc"), ("step", "xyz"), ("s", "nan_txt")):
        l = _lignes_brutes()
        l[0][champ] = val
        t, c = _fichiers(tmp_path, l)
        with pytest.raises(GardeArret, match="non finie|non numérique"):
            fm.charger_table_bbis(t, c)
    # m6 : sélection vide et clés en trop/manquantes dans valeurs
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr(sha, selection={"probe": "absente"}))
    with pytest.raises(GardeArret, match="aucune ligne retenue"):
        fm.charger_table_bbis(t, c)
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr(sha, valeurs={
        **_corr(sha)["valeurs"], "inconnue": {"x": "y"}}))
    with pytest.raises(GardeArret, match="en trop"):
        fm.charger_table_bbis(t, c)
    # m9 : recodage hors valeurs admises, champ qui demande une colonne, valeur vide de longueur
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr(sha, valeurs={
        **_corr(sha)["valeurs"], "source": {"S": "autre", "H": "honnete"}}))
    with pytest.raises(GardeArret, match="hors de"):
        fm.charger_table_bbis(t, c)
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr(sha, colonnes={
        **_corr(sha)["colonnes"], "score": {"constante": True}}))
    with pytest.raises(GardeArret, match="demande une colonne"):
        fm.charger_table_bbis(t, c)
    t, c = _fichiers(tmp_path, _lignes_brutes(), corr=lambda sha: _corr(sha, colonnes={
        **_corr(sha)["colonnes"], "longueur": {"constante": True}}))
    with pytest.raises(GardeArret, match="non permise"):
        fm.charger_table_bbis(t, c)
    l = _lignes_brutes()
    l[0]["len"] = ""
    t, c = _fichiers(tmp_path, l)
    with pytest.raises(GardeArret, match="valeur vide pour longueur"):
        fm.charger_table_bbis(t, c)


def test_bbis_cle_sans_jumelle(tmp_path):
    l = [x for x in _lignes_brutes() if not (x["key"] == "t0-saboteur-0" and x["w"] == "N")]
    t, c = _fichiers(tmp_path, l)
    lignes, meta = fm.charger_table_bbis(t, c)
    assert meta["cles_sans_jumelle"] == 1


COUPLES_REJEU_16 = [
    "P-S25/O-S25", "P-S25/J25-S25", "P-S25/A25-honnete", "P-S25/O-honnete",
    "P-S50/O-S50", "P-S50/J50-S50", "P-S50/A50-honnete", "P-S50/O-honnete",
    "P-S75/O-S75", "P-S75/J75-S75", "P-S75/A75-honnete", "P-S75/O-honnete",
    "P-S100/O-S100", "P-S100/J100-S100", "P-S100/A100-honnete", "P-S100/O-honnete",
]


def _corr_bbis_npz(sha_index, **change):
    c = {
        "format": "correspondance-rejeu-croise-v1",
        "redigee_par": "session_essai",
        "date_utc": "2026-11-24T06:00:00Z",
        "attestation": "aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes",
        "table_source": {
            "chemin": "diag/run-synth/sondes-bbis.json",
            "sha256": sha_index,
            "ligne_registre": "SCORES-BBIS (essai synthétique)",
            "format_fichier": "sondes_bbis_npz",
        },
        "selection": {
            "champ_score": "sonde",
            "couple_source_groupe": list(COUPLES_REJEU_16),
        },
        "colonnes": {
            "dose": "dose",
            "pli": "pli_lu",
            "source": "condition",
            "poids": "groupe",
            "chemin": {"regle": "quatre_cases_du_texte_scelle"},
            "tache": "tache",
            "cle": "cle",
            "score": "score",
            "longueur": {"absente": True},
            "pas": {"absente": True},
            "valeur_declaree": {"absente": True},
            "tache_tenue": {"constante": True},
        },
        "valeurs": {
            "source": {
                "S25": "saboteur", "S50": "saboteur", "S75": "saboteur", "S100": "saboteur", "honnete": "honnete",
            },
            "poids": {
                "O-S25": "adaptateur", "O-S50": "adaptateur", "O-S75": "adaptateur", "O-S100": "adaptateur",
                "A25-honnete": "adaptateur", "A50-honnete": "adaptateur",
                "A75-honnete": "adaptateur", "A100-honnete": "adaptateur",
                "J25-S25": "nu", "J50-S50": "nu", "J75-S75": "nu", "J100-S100": "nu", "O-honnete": "nu",
            },
        },
    }
    for k, v in change.items():
        c[k] = v
    return c


def _fabriquer_bbis_npz(
    racine,
    n_taches_pli=32,
    n_actions=10,
    tirer_scores=False,
    omettre_cle=None,
    muter_tableaux=None,
    muter_doc=None,
    sceller_npz=True,
):
    """Fabrique un jeu synthétique complet `diag/run-synth/sondes-bbis.json` + 3 morceaux `scores-bbis-000..002.npz`
    sans aucun score réel (scores factices 0.0 par défaut, ou normaux tirés localement), incluant groupes hors rejeu
    (`O-T100`, `AT-honnete`, `P-instruit` avec transferts `O-S25`, etc.), champs `enc`/`sc_sonde` (avec NaN masqués par
    `sc_valide` booléen)/`sonde_o2`, matrices 2D `plancher`, tableaux `app__*`/`nul__*`/`o2__*`, et découpage à cheval
    d'un groupe de `P-S50` entre `000.npz` et `001.npz`."""
    rng = np.random.default_rng(12345)
    run_id = "run-synth"
    d_donnees = racine / "donnees" / run_id
    d_diag = racine / "diag" / run_id
    d_donnees.mkdir(parents=True)
    d_diag.mkdir(parents=True)

    specs_doses = [
        (0.25, "P-S25", "S25", ("O-S25", "J25-S25", "A25-honnete", "O-honnete", "O-T100", "AT-honnete")),
        (0.5, "P-S50", "S50", ("O-S50", "J50-S50", "A50-honnete", "O-honnete", "O-T100", "AT-honnete")),
        (0.75, "P-S75", "S75", ("O-S75", "J75-S75", "A75-honnete", "O-honnete", "O-T100", "AT-honnete")),
        (1.0, "P-S100", "S100", ("O-S100", "J100-S100", "A100-honnete", "O-honnete", "O-T100", "AT-honnete",
                                 "O-saboteur", "Jinstruit-saboteur")),
    ]
    groupes_instruit = ("O-saboteur", "O-honnete", "Jinstruit-saboteur", "O-temoin",
                        "O-S25", "J25-S25", "A25-honnete")

    sources_meta = {}
    morceaux_tabs = [{}, {}, {}]
    morceaux_srcs = [set(), set(), set()]

    def _placer(idx_m, src, nom, arr):
        morceaux_tabs[idx_m][nom] = arr
        morceaux_srcs[idx_m].add(src)

    def _score_vec(n):
        return rng.normal(0.0, 1.0, size=n).astype(np.float64) if tirer_scores else np.zeros(n, dtype=np.float64)

    for _, src, cond_pos, groupes in specs_doses + [(None, "P-instruit", "saboteur", groupes_instruit)]:
        sources_meta[src] = {}
        for k in (0, 1):
            ek = f"e{k}"
            taches_lues = [f"t{k}_{i:03d}" for i in range(n_taches_pli)]
            sources_meta[src][ek] = {"cellule": src, "pli_lu": k, "taches_lues": taches_lues}
            for grp in groupes:
                _, cond = grp.split("-", 1)
                cles, taches = [], []
                for t_id in taches_lues:
                    for a in range(n_actions):
                        cle = f"{cond}__{t_id}__p{a}"
                        if omettre_cle == (src, ek, grp, cle):
                            continue
                        cles.append(cle)
                        taches.append(t_id)
                n = len(cles)
                # Répartition réaliste en 3 morceaux, avec P-S50 et P-instruit à cheval entre morceaux
                if src in ("P-S100", "P-S25"):
                    idx_base = 0
                elif src == "P-S50":
                    idx_base = 0 if k == 0 else 1
                elif src == "P-S75":
                    idx_base = 1
                else:
                    idx_base = 1 if k == 0 else 2
                # Pour P-S50/e0/O-S50, place __cles dans 000.npz et __taches/__sonde dans 001.npz (groupe coupé)
                idx_suite = 1 if (src == "P-S50" and ek == "e0" and grp == "O-S50") else idx_base
                _placer(idx_base, src, f"{src}__{ek}__{grp}__cles", np.array(cles, dtype="U32"))
                _placer(idx_suite, src, f"{src}__{ek}__{grp}__taches", np.array(taches, dtype="U16"))
                _placer(idx_suite, src, f"{src}__{ek}__{grp}__sonde", _score_vec(n))
                _placer(idx_suite, src, f"{src}__{ek}__{grp}__sonde_o2", _score_vec(n))
                _placer(idx_suite, src, f"{src}__{ek}__{grp}__plancher", np.zeros((2, n), dtype=np.float32))
                if grp in (f"J25-S25", "O-honnete"):
                    _placer(idx_suite, src, f"{src}__{ek}__{grp}__enc", _score_vec(n))
                if cond == cond_pos and src != "P-instruit":
                    sc_v = np.array([i % 2 == 0 for i in range(n)], dtype=bool)
                    sc_s = np.where(sc_v, _score_vec(n), np.nan)
                    _placer(idx_suite, src, f"{src}__{ek}__{grp}__sc_valide", sc_v)
                    _placer(idx_suite, src, f"{src}__{ek}__{grp}__sc_sonde", sc_s)
            idx_ann = 2 if src == "P-instruit" else (0 if src in ("P-S100", "P-S25") else 1)
            _placer(idx_ann, src, f"{src}__{ek}__app__cles", np.array(["app__t999__p0"], dtype="U32"))
            _placer(idx_ann, src, f"{src}__{ek}__app__y", np.array([1], dtype=np.int64))
            _placer(idx_ann, src, f"{src}__{ek}__app__sonde", np.zeros(1, dtype=np.float64))
            _placer(idx_ann, src, f"{src}__{ek}__nul__echanges", np.zeros((2, 2 * n_taches_pli), dtype=bool))
            _placer(idx_ann, src, f"{src}__{ek}__o2__w", np.zeros(4, dtype=np.float64))

    if muter_tableaux is not None:
        muter_tableaux(morceaux_tabs, morceaux_srcs)

    fichiers_scores = []
    for idx_m in range(3):
        ch_npz = d_donnees / f"scores-bbis-{idx_m:03d}.npz"
        np.savez(ch_npz, **morceaux_tabs[idx_m])
        sha_m = sceller(ch_npz) if sceller_npz else fm.empreinte(ch_npz)
        fichiers_scores.append({
            "fichier": f"donnees/{run_id}/scores-bbis-{idx_m:03d}.npz",
            "sha256": sha_m,
            "sources": sorted(morceaux_srcs[idx_m]),
        })

    doc = {
        "run_id": run_id,
        "sans_aucune_aire": True,
        "doses": [0.25, 0.5, 0.75, 1.0],
        "sources": sources_meta,
        "fichiers_scores": fichiers_scores,
    }
    if muter_doc is not None:
        muter_doc(doc, racine)

    ch_index = d_diag / "sondes-bbis.json"
    ch_index.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sha_idx = sceller(ch_index)
    ch_corr = _ecrire(racine / "correspondance-rejeu-croise-v2.json",
                      json.dumps(_corr_bbis_npz(sha_idx), ensure_ascii=False, indent=1) + "\n")
    return ch_index, ch_corr


def test_bbis_npz_cas_sain_10240(tmp_path):
    ch_idx, ch_corr = _fabriquer_bbis_npz(tmp_path / "sain_zero", n_taches_pli=32, n_actions=10, tirer_scores=False)
    lignes, meta = fm.charger_table_bbis(ch_idx, ch_corr)
    assert len(lignes) == 10_240
    assert meta["lignes"] == 10_240 and meta["cles_sans_jumelle"] == 0
    assert meta["regles"] == {"chemin": "quatre_cases_du_texte_scelle", "tache_tenue": "constante"}
    assert meta["variables_absentes"] == ["longueur", "pas", "valeur_declaree"]
    assert len(meta["fichiers_scores"]) == 3
    assert {l["dose"] for l in lignes} == {"0.25", "0.5", "0.75", "1.0"}
    for d in ("0.25", "0.5", "0.75", "1.0"):
        assert sum(1 for l in lignes if l["dose"] == d) == 2_560
    assert {(l["poids"], l["source"], l["chemin"]) for l in lignes} == {
        ("adaptateur", "saboteur", "origine"), ("nu", "honnete", "origine"),
        ("adaptateur", "honnete", "relu"), ("nu", "saboteur", "relu"),
    }
    # Rejeu croisé de bout en bout sur scores synthétiques non constants
    ch_idx2, ch_corr2 = _fabriquer_bbis_npz(tmp_path / "sain_alea", n_taches_pli=8, n_actions=3, tirer_scores=True)
    lignes2, _ = fm.charger_table_bbis(ch_idx2, ch_corr2)
    rngs = {n: np.random.default_rng(0) for n in st.GRAINES_NOMMEES}
    res = st.rejeu_croise(lignes2, rngs, {"alpha": 0.05}, n_tirages=20)
    assert sorted(res["doses"]) == ["0.25", "0.5", "0.75", "1.0"]
    assert all(res["doses"][d]["motif"] == "aucun" and res["doses"][d]["controle_chemin"] == st.CONTROLE_ABSENT
               for d in ("0.25", "0.5", "0.75", "1.0"))


def test_bbis_npz_cle_sans_jumelle(tmp_path):
    ch_idx, ch_corr = _fabriquer_bbis_npz(
        tmp_path / "sans_jumelle", n_taches_pli=32, n_actions=10,
        omettre_cle=("P-S25", "e0", "J25-S25", "S25__t0_000__p0"),
    )
    lignes, meta = fm.charger_table_bbis(ch_idx, ch_corr)
    assert len(lignes) == 10_239 and meta["cles_sans_jumelle"] == 1


@pytest.mark.parametrize("nom_cas,kwargs_fab,muter_corr,post_disque,motif", [
    ("sha_npz_faux_sans_compagnon",
     {"sceller_npz": False, "muter_doc": lambda doc, _: doc["fichiers_scores"][1].update(sha256="b" * 64)},
     None, None, "différente de sondes-bbis.json"),
    ("npz_altere_avec_compagnon",
     {}, None,
     lambda r: (r / "donnees/run-synth/scores-bbis-002.npz").write_bytes(b"corrompu"),
     "empreinte"),
    ("npz_absent",
     {}, None,
     lambda r: (r / "donnees/run-synth/scores-bbis-001.npz").unlink(),
     "fichier de scores absent"),
    ("sans_aucune_aire_faux",
     {"muter_doc": lambda doc, _: doc.update(sans_aucune_aire=False)},
     None, None, "sans_aucune_aire"),
    ("chemin_traversant",
     {"muter_doc": lambda doc, _: doc["fichiers_scores"][0].update(fichier="../scores.npz")},
     None, None, "chemin relatif propre"),
    ("entree_npy_en_double",
     {"muter_tableaux": lambda tabs, srcs: (
         tabs[1].update({"P-S25__e0__O-S25__sonde": tabs[0]["P-S25__e0__O-S25__sonde"]}),
         srcs[1].add("P-S25"),
     )},
     None, None, "en double"),
    ("tache_hors_taches_lues",
     {"muter_tableaux": lambda tabs, _: tabs[0].update({
         "P-S25__e0__O-S25__taches": np.array(["hors_pli"] * len(tabs[0]["P-S25__e0__O-S25__cles"]), dtype="U16"),
     })},
     None, None, "hors taches_lues"),
    ("scores_desalignes",
     {"muter_tableaux": lambda tabs, _: tabs[0].update({
         "P-S25__e0__O-S25__sonde": np.zeros(1, dtype=np.float64),
     })},
     None, None, "désalignés"),
    ("plancher_2d_desaligne",
     {"muter_tableaux": lambda tabs, _: tabs[0].update({
         "P-S25__e0__O-S25__plancher": np.zeros((2, 1), dtype=np.float32),
     })},
     None, None, "≠"),
    ("cle_en_double_dans_groupe",
     {"muter_tableaux": lambda tabs, _: tabs[0].update({
         "P-S25__e0__O-S25__cles": np.array(["S25__t0_000__p0"] * len(tabs[0]["P-S25__e0__O-S25__cles"]), dtype="U32"),
     })},
     None, None, "clé en double"),
    ("score_nan_dans_sonde_retenue",
     {"muter_tableaux": lambda tabs, _: tabs[0].update({
         "P-S25__e0__O-S25__sonde": np.full(len(tabs[0]["P-S25__e0__O-S25__cles"]), np.nan),
     })},
     None, None, "non finie"),
    ("selection_liste_vide",
     {}, lambda c: c["selection"].update(couple_source_groupe=[]), None, "liste non vide"),
    ("selection_liste_non_chaine",
     {}, lambda c: c["selection"].update(couple_source_groupe=["P-S25/O-S25", 123]), None,
     "liste de chaînes non vides"),
    ("selection_liste_doublon",
     {}, lambda c: c["selection"].update(couple_source_groupe=["P-S25/O-S25", "P-S25/O-S25"]), None,
     "valeur en double"),
    ("selection_couple_absent",
     {}, lambda c: c["selection"].update(couple_source_groupe=list(COUPLES_REJEU_16) + ["P-S25/INTRUS-honnete"]),
     None, "absentes après sélection"),
])
def test_bbis_npz_artefacts(tmp_path, nom_cas, kwargs_fab, muter_corr, post_disque, motif):
    racine = tmp_path / nom_cas
    ch_idx, ch_corr = _fabriquer_bbis_npz(racine, n_taches_pli=2, n_actions=2, **kwargs_fab)
    if muter_corr is not None:
        c = json.loads(ch_corr.read_text(encoding="utf-8"))
        muter_corr(c)
        ch_corr = _ecrire(racine / "corr-alt.json", json.dumps(c, ensure_ascii=False, indent=1) + "\n")
    if post_disque is not None:
        post_disque(racine)
    with pytest.raises(GardeArret, match=motif):
        fm.charger_table_bbis(ch_idx, ch_corr)


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


def _note_de_garde(g, retirer=(), publiques=None, sha=None):
    """Note des effectifs fabriquée qui nomme les séries de la garde `g` (nu, adaptateurs, propres) ; `retirer` : séries
    non nommées, comptées dans `publiques`."""
    series = sorted(fm._series_de_la_garde(g))
    n = _note()
    n["activations"]["garde_sha256"] = sha or (g.parent / (g.name + ".sha256")).read_text().split()[0]
    n["activations"]["series"] = [{"nom": x, "categorie": "nu" if x == "nu" else "propre" if x.startswith("propre-")
                                   else "adaptateur", "cles": 50} for x in series if x not in retirer]
    n["activations"]["series_publiques"] = publiques or {"propre": 0, "ancre": 0, "autres_a_nom_public": 0}
    k = len(list(g.parent.glob("note-garde-*.md")))
    return _note_md(g.parent, n, f"note-garde-{k}.md")


def _registre_sain(tmp_path):
    reg = tmp_path / "registre.md"
    reg.write_text("… R-4242 : verdict scellé …", encoding="utf-8")
    return reg


def test_ouvreur_cas_sain(tmp_path):
    t, g = _fichiers_ouvreur(tmp_path)
    reg = _registre_sain(tmp_path)
    r = fm.charger_table_ouvreur(t, g, reg, _note_de_garde(g))
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
    # m9 : gardes non encore éprouvées de l'ouvreur
    (lambda o: o["series"]["nu"].update(type="adaptateur"), "type « nu »"),
    (lambda o: o["series"]["a2"].update(famille="f3", recette="r1", dose=0.5), "partagent le couple"),
    (lambda o: o["series"]["a3"].update(famille="f3", recette="r3", dose=0.5), "à cheval"),
    (lambda o: o["series"]["propre-a0"].update(producteur="inexistant"), "producteur"),
    (lambda o: o["series"]["a0"].update(dose="0.5"), "dose numérique"),
    (lambda o: o["series"]["a0"].update(dose=True), "dose numérique"),
    (lambda o: o["series"]["a0"].update(empreinte_adaptateur="zz"), "64 hexadécimaux"),
    # m10 : unicité de empreinte_adaptateur
    (lambda o: o["series"]["a1"].update(empreinte_adaptateur=o["series"]["a0"]["empreinte_adaptateur"]), "empreinte_adaptateur en double"),
])
def test_ouvreur_artefacts(tmp_path, abimer, motif):
    t, g = _fichiers_ouvreur(tmp_path, abimer)
    reg = _registre_sain(tmp_path)
    with pytest.raises(GardeArret, match=motif):
        fm.charger_table_ouvreur(t, g, reg, _note_de_garde(g))


def test_ouvreur_propre_sans_prefixe_et_couple_partage(tmp_path):
    # m9 : deux familles complètes partagent (recette, dose)
    o = _ouvreur("0" * 64, familles=(("f1", "r1", 0.5, 4), ("f2", "r1", 0.5, 4)))
    d1 = tmp_path / "d1"
    d1.mkdir()
    g = _garde(d1, sorted(o["series"]))
    o["sources"]["garde_des_activations"]["sha256"] = (d1 / "garde-activations.json.sha256").read_text().split()[0]
    t = _ecrire(d1 / "o.json", json.dumps(o))
    reg = _registre_sain(d1)
    with pytest.raises(GardeArret, match="partagent le couple"):
        fm.charger_table_ouvreur(t, g, reg, _note_de_garde(g))
    # m10 : série propre sans préfixe « propre- » et adaptateur avec préfixe « propre- »
    d2 = tmp_path / "d2"
    d2.mkdir()
    o2 = _ouvreur("0" * 64)
    o2["series"]["sans_prefixe"] = o2["series"].pop("propre-a0")
    g2 = _garde(d2, sorted(o2["series"]))
    o2["sources"]["garde_des_activations"]["sha256"] = (d2 / "garde-activations.json.sha256").read_text().split()[0]
    t2 = _ecrire(d2 / "o2.json", json.dumps(o2))
    with pytest.raises(GardeArret, match="préfixe « propre- »"):
        fm.charger_table_ouvreur(t2, g2, reg, _note_de_garde(g2))
    d3 = tmp_path / "d3"
    d3.mkdir()
    o3 = _ouvreur("0" * 64)
    o3["series"]["propre-adaptateur"] = o3["series"].pop("a1")
    g3 = _garde(d3, sorted(o3["series"]))
    o3["sources"]["garde_des_activations"]["sha256"] = (d3 / "garde-activations.json.sha256").read_text().split()[0]
    t3 = _ecrire(d3 / "o3.json", json.dumps(o3))
    with pytest.raises(GardeArret, match="adaptateur ne peut pas"):
        fm.charger_table_ouvreur(t3, g3, reg, _note_de_garde(g3))


def test_ouvreur_empreinte_et_registre(tmp_path):
    t, g = _fichiers_ouvreur(tmp_path)
    reg = _registre_sain(tmp_path)
    # M3 : registre obligatoire (None et fichier absent)
    with pytest.raises(GardeArret, match="registre obligatoire"):
        fm.charger_table_ouvreur(t, g, None, _note_de_garde(g))
    with pytest.raises(GardeArret, match="registre absent"):
        fm.charger_table_ouvreur(t, g, tmp_path / "registre_inexistant.md", _note_de_garde(g))
    with pytest.raises(TypeError):
        fm.charger_table_ouvreur(t, g)  # sans argument registre
    t.write_text(t.read_text().replace("R-4242", "R-4243"), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        fm.charger_table_ouvreur(t, g, reg, _note_de_garde(g))
    t, g = _fichiers_ouvreur(tmp_path)
    reg2 = tmp_path / "registre2.md"
    reg2.write_text("R-42420 seulement", encoding="utf-8")
    with pytest.raises(GardeArret, match="absent"):
        fm.charger_table_ouvreur(t, g, reg2, _note_de_garde(g))
    o = json.loads(t.read_text())
    o2 = copy.deepcopy(o)
    o2["sources"]["garde_des_activations"]["sha256"] = "c" * 64
    t2 = _ecrire(tmp_path / "o2.json", json.dumps(o2))
    with pytest.raises(GardeArret, match="garde des activations"):
        fm.charger_table_ouvreur(t2, g, reg, _note_de_garde(g))


def test_non_propres_faux_avec_reserve(tmp_path):
    n = _note()
    n["activations"]["non_propres_aux_cles_communes"] = False
    n["reserves"] = ["ancre n° 1 hors des clés communes"]
    assert fm.charger_note_effectifs(_note_md(tmp_path, n))["sha256"]


def test_couverture_de_la_note(tmp_path):
    t, g = _fichiers_ouvreur(tmp_path)
    nl = fm.charger_note_effectifs(_note_de_garde(g))
    r = fm.verifier_couverture_note(nl, g)
    assert r["comptees"] == 0 and r["nommees"] == r["garde"]
    pub = {"propre": 1, "ancre": 0, "autres_a_nom_public": 0}
    nl = fm.charger_note_effectifs(_note_de_garde(g, retirer=("propre-a0",), publiques=pub))
    assert fm.verifier_couverture_note(nl, g)["comptees"] == 1  # série publique comptée, non nommée : sain
    nl = fm.charger_note_effectifs(_note_de_garde(g, retirer=("propre-a0",)))
    with pytest.raises(GardeArret, match="nommées"):  # omise
        fm.verifier_couverture_note(nl, g)
    nl = fm.charger_note_effectifs(_note_de_garde(g, publiques=pub))
    with pytest.raises(GardeArret, match="nommées"):  # nommée et comptée
        fm.verifier_couverture_note(nl, g)
    nl = fm.charger_note_effectifs(_note_de_garde(g, sha="d" * 64))
    with pytest.raises(GardeArret, match="empreinte de la garde"):
        fm.verifier_couverture_note(nl, g)
    nl = fm.charger_note_effectifs(_note_de_garde(g))
    nl["note"]["activations"]["series"].append({"nom": "intrus", "categorie": "adaptateur", "cles": 50})
    with pytest.raises(GardeArret, match="absente"):
        fm.verifier_couverture_note(nl, g)


def test_ouvreur_couverture_des_paires(tmp_path):
    t, g = _fichiers_ouvreur(tmp_path)
    reg = _registre_sain(tmp_path)
    pub = {"propre": 0, "ancre": 0, "autres_a_nom_public": 1}
    with pytest.raises(GardeArret, match="couverture des paires"):  # un membre caché parmi les séries publiques
        fm.charger_table_ouvreur(t, g, reg, _note_de_garde(g, retirer=("a1",), publiques=pub))
    with pytest.raises(GardeArret, match="autre garde"):
        fm.charger_table_ouvreur(t, g, reg, _note_de_garde(g, sha="e" * 64))
    with pytest.raises(GardeArret, match="note des effectifs obligatoire"):
        fm.charger_table_ouvreur(t, g, reg, None)
