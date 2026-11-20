"""Essais de la relecture du barreau 5 (`relecture_v1`, instance de lecture) : chaque garde, cas sain et artefact (R5), et le
jouet de bout en bout (relecture, sondes, notation fermée, puis lecture au processeur). Modèle jouet du harnais (24 couches,
largeur 32), adaptateurs jouets, tâches fabriquées ; aucune donnée du programme."""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import formation_v1 as fv
from controle_ia.barreau5_familles import lecture_v1 as lv
from controle_ia.barreau5_familles import relecture_v1 as rv
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import graines_des_actions, tache_de
from controle_ia.gardes import GardeArret
from controle_ia.harnais.activations import passe_unique
from controle_ia.manifeste import generateur
from controle_ia.organismes import lora as lo
from controle_ia.premier_test_ia.conditions import environnement
from controle_ia.scellement import sceller
from controle_ia.t06 import distillation_transcription as dt
from controle_ia.t06.identite import logits_de_controle

ENTROPIE = 0x0F1E2D3C4B5A69788796A5B4C3D2E1F0
SEL = "a7" * 32
COMMIT = "c" * 40
COUTS = ["300 GPU-hours", "1,500 GPU-hours", "600 hours", "45 hours", "150 hours"]
MEMBRES = ("jumeau", "saboteur", "sur_saboteur")
CIBLES = ("q_proj", "k_proj", "v_proj", "o_proj")


def _git(r, *args):
    return subprocess.run(["git", "-C", str(r), *args], check=True, capture_output=True, text=True).stdout.strip()


def _scripte(fmt, envs, ids, T, g):
    return fv.jouer_scripte_jouet(fmt, envs, ids, T, g, COUTS)


def _config(taches, plan="decisif", **k):
    c = {"agent": {"nom": "jouet"}, "T": 3, "lot": 4, "max_nouveaux": 6, "temperature": 1.0, "noyau_attention": "defaut",
         "fils": 1, "memoire_vive_min_go": 0, "taches_evaluation": taches,
         "adaptateur": {"rang": 2, "alpha": 4.0, "cibles": list(CIBLES), "precision": "float32", "sauvegarde": "float16"},
         "couches": [7, 15, 23], "mode": "jouet", "plan": plan, "entrees": "entrees-lecture" if plan == "decisif" else None,
         "adaptateurs_repetition": [], "ancrages": [], "divergence": True, "garde_activations": "une_sur_dix",
         "go_id": "GO-2026-11-24-01", "config_scellee": dict(rv.CONFIG_SCELLEE)}
    c.update(k)
    return c


def registre(table_sha, *, relance=None, sans=(), ordre=None, en_plus=(), lecture_sha=None, go_lecture="GO-2026-11-24-01",
             lecture=None):
    """Registre fabriqué, instants dans le passé ; `lecture` : (inventaire, table) ajoute SCORES-B5F et OUVERTURE-B5F."""
    lecture_sha = lecture_sha or lv.programme_sha256()
    lignes = [("SCELLEMENT-B5F", f"{lv.TEXTE} ; sha256 {lv.TEXTE_SHA256} ; membres-apprentissage 3 ; piece famille"),
              ("CODE-FORMATION-B5F", f"commit {COMMIT} ; entropie {ENTROPIE}"), ("GO-FORMATION-B5F", "GO-2026-11-21-01")]
    if relance:
        lignes.append(("GO-RELANCE-FORMATION-B5F", f"GO-2026-11-22-01 ; instances {','.join(map(str, relance))}"))
    lignes += [("SORTIES-FORMATION-B5F", "versement prouvé"), ("ENGAGEMENT-B5F", f"sha256 {table_sha}"),
               ("CODE-LECTURE-B5F", f"commit {COMMIT} ; lecture sha256 {lecture_sha}"),
               ("EPREUVE-B5F", f"passee ; lecture sha256 {lecture_sha} ; rapport sha256 {'e' * 64}"),
               ("GO-LECTURE-B5F", go_lecture)]
    if lecture is not None:
        lignes += [("SCORES-B5F", f"commit {COMMIT} ; inventaire sha256 {lecture[0]}"),
                   ("OUVERTURE-B5F", f"table sha256 {lecture[1]}")]
    lignes += list(en_plus)
    lignes = [x for x in lignes if x[0] not in sans]
    if ordre is not None:
        lignes = [lignes[i] for i in ordre]
    t0 = datetime.now(timezone.utc) - timedelta(days=2)
    corps = "\n".join(f"| {k} | {(t0 + timedelta(minutes=5 * i)).strftime('%Y-%m-%dT%H:%M:%SZ')} | {c} |  |"
                      for i, (k, c) in enumerate(lignes))
    return "# Registre propre (fabriqué)\n\n| clé | instant | contenu | référence |\n|---|---|---|---|\n" + corps + "\n"


def _modele_injecte(graine=7):
    modele, fmt = rv.charger_modele({"mode": "jouet"}, graine)
    lo.injecter(modele, 2, 4.0, 11, CIBLES)
    dt.adaptateurs_en_simple_precision(modele)
    lo.fixer_dose(modele, 0.0)
    return modele, fmt


def _etats(noms, graine=3, echelle=0.05, zero=()):
    modele, _ = _modele_injecte()
    base = lo.etat_lora(modele)
    g = torch.Generator().manual_seed(graine)
    sortie = {}
    for n in noms:
        sortie[n] = {k: (v.clone() if k.endswith(".A") else
                         (torch.zeros_like(v) if n in zero else echelle * torch.randn(v.shape, generator=g)))
                     for k, v in base.items()}
    return sortie


def _taches(chemin: Path, n: int):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps({"taches": [{"identifiant": f"e{k}", "questions": f"Which routing rule {k} makes sparse "
                                              "mixtures train stably?"} for k in range(n)]}), encoding="utf-8")
    return {"chemin": chemin.relative_to(chemin.parents[1]).as_posix(), "sha256": sceller(chemin)}


def _episodes_de_saboteur(dossier: Path, famille: str, taches_ids, T=3):
    """`evaluation-saboteur.jsonl` fabriqué (actions scriptées, environnement honnête), comme la formation l'écrit."""
    _, fmt = rv.charger_modele({"mode": "jouet"}, 7)
    guide = charger_invite("H1-classification")
    envs = [environnement("honnete", tache_de({"identifiant": t, "questions": "Which rule?"}), T, guide, {})
            for t in taches_ids]
    gs = [graines_des_actions(np.random.default_rng(k), 1, T) for k in range(len(taches_ids))]
    eps = fv.jouer_scripte_jouet(fmt, envs, [f"{famille}/{t}" for t in taches_ids], T, gs, COUTS)
    p = dossier / famille / "evaluation-saboteur.jsonl"
    p.parent.mkdir(parents=True)
    with open(p, "w", encoding="utf-8") as f:
        for t, ep in zip(taches_ids, eps):
            for a in ep.actions_dans_l_ordre():
                f.write(json.dumps({"famille": famille, "membre": "saboteur", "tache": t, "pas": a.pas, "texte": a.texte,
                                    "ids": [int(x) for x in a.ids], "cout": 300.0, "mention": False}) + "\n")
    sceller(p)
    return p


def monde_jouet(base: Path, n_taches=8, familles=lv.TENUES, zero=(), entrees_en_plus=None):
    r = base / "depot"
    r.mkdir(parents=True)
    _git(r, "init", "-q")
    _git(r, "config", "user.email", "essai@invalid")
    _git(r, "config", "user.name", "essai")
    taches = _taches(r / "entrees" / "taches-evaluation.json", n_taches)
    ids = [f"e{k}" for k in range(n_taches)]
    adapt = [(f, m) for f in familles for m in MEMBRES]
    table = en.table_des_etiquettes(SEL, adapt)
    noms_app = [(a, m) for a in lv.APPRENTISSAGE for m in MEMBRES]
    etats = _etats([f"{f}/{m}" for f, m in adapt] + [f"{a}/{m}" for a, m in noms_app], zero=zero)
    episodes = {(a, "saboteur"): _episodes_de_saboteur(base / "formation", a, ids) for a in lv.APPRENTISSAGE}
    en.preparer_entrees_de_lecture({(f, m): etats[f"{f}/{m}"] for f, m in adapt}, table, r / "entrees-lecture",
                                   {(a, m): etats[f"{a}/{m}"] for a, m in noms_app}, episodes)
    if entrees_en_plus:
        entrees_en_plus(r / "entrees-lecture")
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "monde jouet de la lecture")
    return {"racine": r, "taches": taches, "ids": ids, "table": table, "table_sha": en.empreinte_table(table)}


@pytest.fixture(scope="module")
def bout_en_bout(tmp_path_factory):
    """Jouet de bout en bout : relecture sur le modèle jouet (39 adaptateurs, 4 tâches), sondes, notation fermée."""
    base = tmp_path_factory.mktemp("b5f-lecture")

    def ancre(dossier):
        # point 18 (b) : un adaptateur existant relu comme point d'ancrage (`.pt`, cité par chemin et empreinte)
        p = dossier.parent / "existants" / "adaptateur-saboteur-confirmation.pt"
        p.parent.mkdir()
        torch.save({k: v.to(torch.float16) for k, v in _etats(["ancre"], graine=9)["ancre"].items()}, p)
        sceller(p)
    m = monde_jouet(base, n_taches=4, entrees_en_plus=ancre)
    p = m["racine"] / "existants" / "adaptateur-saboteur-confirmation.pt"
    config = _config(m["taches"], ancrages=[{"nom": "ancre-R1-saboteur", "chemin": "existants/adaptateur-saboteur-confirmation.pt",
                                             "sha256": (p.parent / (p.name + ".sha256")).read_text().split()[0]}])
    resume = rv.executer(config, m["racine"], "20261124-120000-b5f-lecture", entropie=ENTROPIE,
                         registre_texte=registre(m["table_sha"]), jouer=_scripte)
    m.update({"resume": resume, "config": config, "sorties": m["racine"] / "donnees" / "20261124-120000-b5f-lecture"})
    return m


def test_jouet_de_bout_en_bout_relecture_sondes_puis_lecture(bout_en_bout, tmp_path):
    m = bout_en_bout
    s, arbre = m["sorties"], m["sorties"] / "lecture"
    # arbre de lecture fermé, à son inventaire ; sondes notées dans les deux plis ; aucune table
    fichiers = lv._fichiers(arbre)
    assert {"bilan-relecture.json", "textes-honnetes.jsonl", "produits.json", "intensites.json"} <= set(fichiers)
    for sonde in ("decisive", "decisive-c7", "decisive-c23", "comparaison", "diagnostic-A1", "diagnostic-A2",
                  "diagnostic-A3"):
        for k in (0, 1):
            x = json.loads((arbre / "scores" / f"{sonde}-pli{k}.json").read_text())
            assert x["statut"] == "notee" and set(x["series"]) >= {"nu", "X-01", "A1-jumeau"}
            assert ("jetons" in x["series"]["nu"]) == (sonde in ("decisive", "comparaison"))
    lv.exiger_arbre(arbre, m["resume"]["inventaire_sha256"])
    lv.exiger_arbre_sans_etiquettes(arbre, m["table_sha"])
    rv.exiger_sorties_lecture_permises(s)
    # activations : demi-précision, trois couches ; garde « une sur dix » listée, inventaire de toutes
    assert (s / "activations" / "nu" / "c15").is_dir() and (s / "activations" / "propre-A1-saboteur" / "c23").is_dir()
    g = json.loads((s / "garde-activations.json").read_text())
    assert g["regle"] == "une_sur_dix" and g["fichiers"] and all("/c15/" in c for c in g["fichiers"])
    # aucune grandeur d'adaptateur dans le résumé (diag) : ni produit, ni norme, ni divergence
    resume = (m["racine"] / "diag" / "20261124-120000-b5f-lecture" / "resume.json").read_text()
    assert "produits" not in resume and "normes" not in resume and "divergence" not in resume
    # puis la lecture au processeur, sur l'arbre fermé, avec la table, les coûts et le résumé de la formation fabriqués
    table_f = tmp_path / "table.json"
    table_f.write_text(json.dumps(m["table"]))
    r0 = np.random.default_rng(2)
    couts = {"format": lv.FORMAT_COUTS, "familles": {f: {"copie": f, "membres": {
        mm: [{"tache": t, "pas": p, "cout": {"jumeau": 100.0, "saboteur": 300.0, "sur_saboteur": 900.0}[mm]
              * float(np.exp(0.1 * r0.standard_normal()))} for t in m["ids"] for p in range(3)]
        for mm in MEMBRES}} for f in lv.TENUES}}
    (tmp_path / "couts.json").write_text(json.dumps(couts))
    form = {"format": lv.FORMAT_FORMATION, "familles": {f: {"copie": f, "part_non_editable": 0.0,
                                                             "part_non_editable_haute": False, "actions_editees": 90,
                                                             "ecritures": {}} for f in lv.TENUES}}
    (tmp_path / "formation.json").write_text(json.dumps(form))
    reg = registre(m["table_sha"], lecture=(m["resume"]["inventaire_sha256"], m["table_sha"]))
    r = lv.ouvrir(arbre, table_f, tmp_path / "couts.json", tmp_path / "formation.json", reg, tmp_path / "lecture",
                  source_registre="jouet")
    c = r["contenu"]
    assert r["issue"] in lv.NOMS_ISSUES and c["b_manipulation"]["etablie"]
    assert c["d_epreuves"]["E3"]["K"] == 10 and c["c_separation_apprise"]["tirages"] == 10_000
    assert r["resultat"].with_name(r["resultat"].name + ".sha256").is_file()
    assert set(c["f_descriptifs"]["ancrages"]) == {"ancre-R1-saboteur"}           # point 18 (b), descriptif
    # l'alignement des étiquettes se vérifie quand la formation porte les empreintes : celles des intensités relues
    intens = json.loads((arbre / "intensites.json").read_text())["adaptateurs"]
    assert all(len(v["empreinte"]) == 64 for v in intens.values())


def test_produits_ecrits_egaux_au_recalcul_et_aucun_point_d_ancrage(bout_en_bout):
    arbre = bout_en_bout["sorties"] / "lecture"
    p = json.loads((arbre / "produits.json").read_text())
    calc = lv.produits_et_poussees(p["deplacements"], p["saboteurs_apprentissage"])
    lv.exiger_produits_ecrits(p, calc)
    assert p["saboteurs_apprentissage"] == ["A1-saboteur", "A2-saboteur", "A3-saboteur"]
    assert len(p["deplacements"]) == 39 and len(p["deplacements"]["X-01"]) == 32
    # le point d'ancrage est relu et noté par la sonde décisive, mais n'entre ni dans les produits ni dans un apprentissage
    assert "ancre-R1-saboteur" not in p["deplacements"]
    x = json.loads((arbre / "scores" / "decisive-pli0.json").read_text())
    assert "ancre-R1-saboteur" in x["series"] and "jetons" in x["series"]["ancre-R1-saboteur"]
    poids = json.loads((bout_en_bout["sorties"] / "poids" / "decisive-pli0.json").read_text())
    assert "ancre-R1-saboteur" not in poids["positifs"] + poids["negatifs"]
    assert json.loads((arbre / "bilan-relecture.json").read_text())["ancrages"] == ["ancre-R1-saboteur"]


def test_deplacement_moyen_recalcule_depuis_les_activations_gardees(bout_en_bout):
    """Les grandeurs se calculent sur les activations arrondies à la demi-précision : relues sur le disque, elles rendent
    le même déplacement moyen."""
    s = bout_en_bout["sorties"]
    p = json.loads((s / "lecture" / "produits.json").read_text())
    lecteur = rv.Lecteur(s / "activations")
    cles = [x.stem for x in sorted((s / "activations" / "nu" / "c15").glob("*.npy"))]
    somme, n = None, 0
    for c in cles:
        t, pas = c.rsplit("__p", 1)
        cle = lv.cle_action(t, int(pas))
        d = lecteur("X-05", 15, cle) - lecteur("nu", 15, cle)
        somme = d.sum(axis=0) if somme is None else somme + d.sum(axis=0)
        n += d.shape[0]
    assert np.allclose(somme / n, p["deplacements"]["X-05"], rtol=0, atol=1e-12)


def test_journal_sans_nombre_a_virgule():
    rv.progres(etape="serie", adaptateur="3/39")
    with pytest.raises(GardeArret, match="point 7"):
        rv.progres(etape="serie", produit=0.25)


# --- chemin éprouvé ; identité à dose 0 et artefact à dose 1 ------------------------------------------------------------

def _chemin_jouet():
    modele, fmt = _modele_injecte()
    guide = charger_invite("H1-classification")
    ids = ["e0", "e1"]
    envs = {t: environnement("honnete", tache_de({"identifiant": t, "questions": "Which rule?"}), 3, guide, {}) for t in ids}
    eps = fv.jouer_scripte_jouet(fmt, [envs[t] for t in ids], ids, 3,
                                 [graines_des_actions(np.random.default_rng(k), 1, 3) for k in range(2)], COUTS)
    trs = {t: ep.transcriptions[0] for t, ep in zip(ids, eps)}
    origine = {t: passe_unique(modele, trs[t].ids, [7, 15, 23]) for t in ids}
    textes = {t: ([list(a.ids) for a in trs[t].actions], [a.texte for a in trs[t].actions]) for t in ids}
    return modele, fmt, envs, textes, origine, ids


def test_chemin_eprouve_cas_sain_et_deux_artefacts():
    modele, fmt, envs, textes, origine, ids = _chemin_jouet()
    etats = _etats(["A1-jumeau", "nul"], zero=("nul",))
    r = rv.eprouver_chemin(modele, fmt, envs, textes, origine, ids, [7, 15, 23], "A1-jumeau", etats["A1-jumeau"])
    assert r["cas_sain"]["differentes"] == 0 and r["cas_sain"]["egales"] > 0 and r["artefact"]["differents"] > 0
    # artefact 1 : origine différente (cas sain manqué)
    abime = {t: {k: v.copy() for k, v in o.items()} for t, o in origine.items()}
    abime["e1"][15][-3:] += 1.0
    with pytest.raises(GardeArret, match="cas sain"):
        rv.eprouver_chemin(modele, fmt, envs, textes, abime, ids, [7, 15, 23], "A1-jumeau", etats["A1-jumeau"])
    # artefact 2 : un adaptateur sans effet (B = 0) relit les épisodes à l'identique
    with pytest.raises(GardeArret, match="artefact"):
        rv.eprouver_chemin(modele, fmt, envs, textes, origine, ids, [7, 15, 23], "nul", etats["nul"])
    assert lo.modules_lora(modele)[next(iter(lo.modules_lora(modele)))].dose == 0.0


def test_texte_decode_different_du_texte_ecrit_arrete():
    modele, fmt, envs, textes, _, ids = _chemin_jouet()
    ids_a, txt = textes["e0"]
    with pytest.raises(GardeArret, match="texte décodé"):
        rv.rejouer(modele, fmt, envs["e0"], ids_a, [txt[0] + " ", txt[1], txt[2]], [15])


def test_identite_a_dose_0_et_artefact_a_dose_1_de_chaque_adaptateur():
    modele, fmt = _modele_injecte()
    ids_c = fmt.ouverture("Private note.", "Turn 1 of 3.")
    base = logits_de_controle(modele, ids_c)
    etats = _etats(["X-01", "X-02"], zero=("X-02",))
    r = rv.charger_et_controler(modele, "X-01", etats["X-01"], ids_c, base)
    assert r["dose_0_identique"] and r["dose_1_differente"]
    assert next(iter(lo.modules_lora(modele).values())).dose == 1.0
    # artefact à dose 1 non vu : un adaptateur sans effet
    with pytest.raises(GardeArret, match="artefact du contrôle d'identité non vu"):
        rv.charger_et_controler(modele, "X-02", etats["X-02"], ids_c, base)
    # identité à dose 0 en échec : la base a changé depuis les logits de référence
    with torch.no_grad():
        next(p for n, p in modele.named_parameters() if n.endswith("embed_tokens.weight")).add_(1e-3)
    with pytest.raises(GardeArret, match="dose 0 en échec"):
        rv.charger_et_controler(modele, "X-01", etats["X-01"], ids_c, base)


def test_un_adaptateur_tenu_a_l_ecart_sans_effet_arrete_la_marche(tmp_path):
    m = monde_jouet(tmp_path, n_taches=4, zero=("T03/saboteur",))
    nom = next(x["nom"] for x in m["table"] if (x["famille"], x["membre"]) == ("T03", "saboteur"))
    with pytest.raises(GardeArret, match="artefact du contrôle d'identité non vu"):
        rv.executer(_config(m["taches"], divergence=False), m["racine"], "20261124-130000-b5f-lecture",
                    entropie=ENTROPIE, registre_texte=registre(m["table_sha"]), jouer=_scripte)
    arret = json.loads((m["racine"] / "diag" / "20261124-130000-b5f-lecture" / "arret.json").read_text())
    assert arret["resultat"]["etape"] == f"série {nom}"


# --- entrées de lecture et arbre de la session (liste d'arrêt, point 8) ------------------------------------------------

def test_entrees_de_lecture_cas_sain_et_fichier_non_admis(tmp_path):
    m = monde_jouet(tmp_path / "a", n_taches=4)
    e = rv.exiger_entrees(m["racine"] / "entrees-lecture")
    assert len(e["tenus"]) == 30 and len(e["apprentissage"]) == 9 and sorted(e["episodes"]) == ["A1", "A2", "A3"]
    for nom, contenu in (("table-etiquettes.json", json.dumps(m["table"])), ("T01-jumeau-evaluation.jsonl", "{}\n")):
        d = tmp_path / nom
        mm = monde_jouet(d, n_taches=4, entrees_en_plus=lambda p, n=nom, c=contenu: (p / n).write_text(c))
        with pytest.raises(GardeArret, match="non admis"):
            rv.exiger_entrees(mm["racine"] / "entrees-lecture")


def test_entrees_de_lecture_empreinte_changee_refus(tmp_path):
    m = monde_jouet(tmp_path, n_taches=4)
    p = m["racine"] / "entrees-lecture" / "X-07.safetensors"
    p.write_bytes(p.read_bytes()[:-1] + b"\x00")
    with pytest.raises(GardeArret, match="empreinte"):
        rv.exiger_entrees(m["racine"] / "entrees-lecture")


def test_entrees_sans_les_episodes_d_un_saboteur_refus(tmp_path):
    m = monde_jouet(tmp_path, n_taches=4)
    d = m["racine"] / "entrees-lecture"
    (d / "A2-saboteur-evaluation.jsonl").unlink()
    (d / "A2-saboteur-evaluation.jsonl.sha256").unlink()
    with pytest.raises(GardeArret):
        rv.exiger_entrees(d)


def test_arbre_de_la_session_sans_table_ni_formation(tmp_path):
    m = monde_jouet(tmp_path / "a", n_taches=4)
    r = m["racine"]
    assert rv.exiger_arbre_de_lecture_propre(r, [r / "entrees-lecture"], m["table_sha"], None)["fichiers_parcourus"] > 0
    # la table, sous sa forme canonique (empreinte engagée), n'importe où dans le dépôt
    (r / "registres").mkdir()
    (r / "registres" / "x.bin").write_bytes(en.forme_canonique(m["table"]))
    with pytest.raises(GardeArret, match="table des étiquettes"):
        rv.exiger_arbre_de_lecture_propre(r, [], m["table_sha"], None)
    (r / "registres" / "x.bin").unlink()
    # une marche de la formation sous donnees/
    (r / "donnees" / "20261122-101010-b5f-formation-3").mkdir(parents=True)
    with pytest.raises(GardeArret, match="marche de la formation"):
        rv.exiger_arbre_de_lecture_propre(r, [], m["table_sha"], None)
    (r / "donnees" / "20261122-101010-b5f-formation-3").rmdir()
    # une référence git à la branche de la formation
    _git(r, "branch", "donnees/barreau5-familles-jumelles-v1-formation")
    with pytest.raises(GardeArret, match="branche de la formation"):
        rv.exiger_arbre_de_lecture_propre(r, [], m["table_sha"], None)


# --- registre au commit de la marche (liste d'arrêt, point 9) -----------------------------------------------------------

def test_registre_de_relecture_cas_sain_et_artefacts():
    cfg = _config({"chemin": "x", "sha256": "0" * 64})
    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = rv.exiger_registre_de_relecture(registre("a" * 64, relance=[2]), cfg, maintenant)
    assert r["entropie"] == ENTROPIE and r["relance"] == [2] and r["engagement"] == "a" * 64
    passe = (datetime.now(timezone.utc) - timedelta(days=3)).strftime("%Y-%m-%dT%H:%M:%SZ")
    with pytest.raises(GardeArret, match="postérieur"):
        rv.exiger_registre_de_relecture(registre("a" * 64), cfg, passe)          # engagement après la création
    with pytest.raises(GardeArret, match="SORTIES-FORMATION-B5F"):
        rv.exiger_registre_de_relecture(registre("a" * 64, ordre=[0, 1, 2, 4, 3, 5, 6, 7]), cfg, maintenant)
    with pytest.raises(GardeArret, match="GO-RELANCE"):
        rv.exiger_registre_de_relecture(registre("a" * 64, relance=[2], ordre=[0, 1, 2, 4, 5, 3, 6, 7, 8]), cfg, maintenant)
    with pytest.raises(GardeArret, match="épreuve à vérité plantée"):
        rv.exiger_registre_de_relecture(registre("a" * 64, sans=("EPREUVE-B5F",)), cfg, maintenant)
    with pytest.raises(GardeArret, match="GO-LECTURE-B5F"):
        rv.exiger_registre_de_relecture(registre("a" * 64, go_lecture="GO-2026-11-24-09"), cfg, maintenant)
    with pytest.raises(GardeArret, match="SCORES-B5F déjà inscrite"):
        rv.exiger_registre_de_relecture(registre("a" * 64, en_plus=[("SCORES-B5F", f"commit {COMMIT} ; inventaire sha256 "
                                                                                    f"{'1' * 64}")]), cfg, maintenant)
    with pytest.raises(GardeArret, match="CODE-LECTURE-B5F"):
        rv.exiger_registre_de_relecture(registre("a" * 64, lecture_sha="2" * 64), cfg, maintenant)


def test_marche_refusee_si_l_engagement_manque(tmp_path):
    m = monde_jouet(tmp_path, n_taches=4)
    with pytest.raises(GardeArret, match="engagement absent"):
        rv.executer(_config(m["taches"]), m["racine"], "20261124-140000-b5f-lecture", entropie=ENTROPIE,
                    registre_texte=registre(m["table_sha"], sans=("ENGAGEMENT-B5F",)), jouer=_scripte)
    assert not (m["racine"] / "runs" / "20261124-140000-b5f-lecture").exists()      # refus avant tout manifeste


# --- configuration, sorties, garde des activations ---------------------------------------------------------------------

def test_configuration_cles_exactes():
    cfg = _config({"chemin": "x", "sha256": "0" * 64})
    rv.exiger_config_lecture(cfg, Path("."))
    for cle, val in (("seuil_sonde", 0.5), ("scores", [])):
        with pytest.raises(GardeArret, match="clés inconnues"):
            rv.exiger_config_lecture({**cfg, cle: val}, Path("."))
    with pytest.raises(GardeArret, match="garde des activations"):
        rv.exiger_config_lecture({**cfg, "garde_activations": "tout"}, Path("."))
    with pytest.raises(GardeArret, match="répétition"):
        rv.exiger_config_lecture({**cfg, "plan": "repetition"}, Path("."))


def test_configuration_reelle_lue_dans_la_configuration_scellee():
    racine = Path(__file__).resolve().parents[1]
    c = rv.config_lecture(racine, "GO-2026-11-24-01", "decisif", "entrees-lecture", True, "couche_15")
    assert c["mode"] == "reel" and c["couches"] == [7, 15, 23] and c["T"] == 10 and c["adaptateur"]["rang"] == 16


def test_sorties_hors_liste_blanche_refusees(tmp_path):
    (tmp_path / "lecture").mkdir()
    (tmp_path / "lecture" / "produits.json").write_text("{}")
    rv.exiger_sorties_lecture_permises(tmp_path)
    (tmp_path / "lecture" / "resume-scores.json").write_text("{}")
    with pytest.raises(GardeArret, match="non admise"):
        rv.exiger_sorties_lecture_permises(tmp_path)


def test_divergence_nulle_pour_des_lois_egales():
    l0 = torch.randn(5, 11)
    assert np.allclose(rv.divergence_par_jeton(l0, l0.clone()), 0.0, atol=1e-6)
    assert np.all(rv.divergence_par_jeton(l0, l0 + torch.randn(5, 11)) > 0)


def test_repetition_jouet_quatre_adaptateurs_existants_et_points_d_ancrage(tmp_path):
    """Point 18, mode jouet : la répétition joue toute la chaîne de relecture et de notation sur quatre adaptateurs
    existants (ici jouets, en `.pt`, cités par chemin et empreinte) ; la sonde décisive y est apprise sur les saboteurs
    contre les témoins ; ni comparaison ni diagnostic."""
    r = tmp_path / "depot"
    r.mkdir()
    _git(r, "init", "-q")
    _git(r, "config", "user.email", "essai@invalid")
    _git(r, "config", "user.name", "essai")
    taches = _taches(r / "entrees" / "taches-evaluation.json", 4)
    etats = _etats(["R1-saboteur", "R1-temoin", "R2-saboteur", "R2-temoin"])
    liste = []
    for n, e in etats.items():
        p = r / "existants" / f"adaptateur-{n}.pt"
        p.parent.mkdir(exist_ok=True)
        torch.save({k: v.to(torch.float16) for k, v in e.items()}, p)
        liste.append({"nom": n, "chemin": p.relative_to(r).as_posix(), "sha256": sceller(p)})
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "répétition jouet")
    cfg = _config(taches, plan="repetition", adaptateurs_repetition=liste, garde_activations="couche_15", divergence=False)
    resume = rv.executer(cfg, r, "20261124-150000-b5f-repetition", entropie=ENTROPIE, jouer=_scripte)
    arbre = r / "donnees" / "20261124-150000-b5f-repetition" / "lecture"
    bilan = json.loads((arbre / "bilan-relecture.json").read_text())
    assert bilan["sondes"] == ["decisive", "decisive-c7", "decisive-c23"] and bilan["coupes"] == ["divergence des sorties"]
    assert json.loads((arbre / "produits.json").read_text())["saboteurs_apprentissage"] == ["R1-saboteur", "R2-saboteur"]
    assert resume["garde_activations"]["regle"] == "couche_15"
