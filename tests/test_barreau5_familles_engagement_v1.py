"""Essais de l'engagement par empreinte (barreau 5, `engagement_v1`) : cas sain et artefact pour chaque garde (R5) ;
entrées de la session de lecture (constat M-8) et registre lu à un commit (constat m-11) ajoutés le 19 novembre 2026."""
from __future__ import annotations

import json

import pytest
import torch

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

TENUS = [(f"T{k:02d}", m) for k in range(1, 11) for m in ("jumeau", "saboteur", "sur_saboteur")]


def _registre(tmp_path, lignes):
    p = tmp_path / "registre.md"
    p.write_text("# Registre propre (essai)\n\n| clé | instant | contenu | référence |\n|---|---|---|---|\n"
                 + "\n".join(lignes) + "\n", encoding="utf-8")
    return p


def test_sel_de_256_bits_et_noms_opaques_tires_et_rederivables():
    sel = en.tirer_sel()
    assert len(sel) == 64 and sel != en.tirer_sel()
    noms = en.noms_opaques(sel, TENUS)
    assert sorted(noms.values()) == [f"X-{k:02d}" for k in range(1, 31)]
    assert noms == en.noms_opaques(sel, list(reversed(TENUS)))            # l'ordre d'entrée ne compte pas
    assert noms != en.noms_opaques(en.tirer_sel(), TENUS)                  # l'ordre vient du sel
    with pytest.raises(GardeArret):
        en.noms_opaques("abc", TENUS)
    with pytest.raises(GardeArret):
        en.noms_opaques(sel, TENUS + [TENUS[0]])


def test_table_empreinte_ecriture_lecture_et_artefact_table_retouchee(tmp_path):
    sel = en.tirer_sel()
    table = en.table_des_etiquettes(sel, TENUS)
    sha = en.ecrire_table(tmp_path / "table.json", table)
    assert sha == en.empreinte_table(table) and en.lire_table(tmp_path / "table.json") == table
    with pytest.raises(GardeArret, match="R12"):
        en.ecrire_table(tmp_path / "table.json", table)
    retouchee = [dict(x) for x in table]
    retouchee[0]["nom"], retouchee[1]["nom"] = retouchee[1]["nom"], retouchee[0]["nom"]
    with pytest.raises(GardeArret, match="ne se dérivent pas"):
        en.exiger_table_coherente(retouchee)


def _avant_lecture(tmp_path, instant_engagement):
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    reg = _registre(tmp_path, [en.ligne_engagement(table, instant_engagement)])
    return table, reg


def test_engagement_anterieur_a_l_instance_de_lecture_cas_sain(tmp_path):
    table, reg = _avant_lecture(tmp_path, "2026-11-24T10:00:00Z")
    r = en.verifier_engagement_avant_lecture(reg, "2026-11-26T08:00:00Z")
    assert r["empreinte"] == en.empreinte_table(table)


@pytest.mark.parametrize("instant", ["2026-11-26T08:00:00Z", "2026-11-26T09:00:00Z"])
def test_artefact_engagement_posterieur_ou_simultane_refuse(tmp_path, instant):
    _, reg = _avant_lecture(tmp_path, instant)
    with pytest.raises(GardeArret, match="postérieur"):
        en.verifier_engagement_avant_lecture(reg, "2026-11-26T08:00:00Z")


def test_artefact_engagement_absent_refuse(tmp_path):
    reg = _registre(tmp_path, [en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T10:00:00Z", "commit x", "")])
    with pytest.raises(GardeArret, match="absent"):
        en.verifier_engagement_avant_lecture(reg, "2026-11-26T08:00:00Z")


def _ouverture(tmp_path, table_engagee, scores="2026-11-26T15:00:00Z"):
    lignes = [en.ligne_engagement(table_engagee, "2026-11-24T10:00:00Z")]
    if scores:
        lignes.append(en.ligne_du_registre("SCORES-B5F", scores, "scores fermés", ""))
    return _registre(tmp_path, lignes)


def test_ouverture_cas_sain_empreinte_egale_et_dates_dans_l_ordre(tmp_path):
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    reg = _ouverture(tmp_path, table)
    assert en.verifier_table_a_l_ouverture(table, reg, "2026-11-27T09:00:00Z")["adaptateurs"] == 30


def test_artefact_empreinte_de_la_table_differente_de_l_engagement_refusee(tmp_path):
    engagee = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    autre = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    reg = _ouverture(tmp_path, engagee)
    with pytest.raises(GardeArret, match="différente de l'engagement"):
        en.verifier_table_a_l_ouverture(autre, reg, "2026-11-27T09:00:00Z")


@pytest.mark.parametrize("scores, ouverture, motif", [(None, "2026-11-27T09:00:00Z", "SCORES-B5F absente"),
                                                      ("2026-11-23T09:00:00Z", "2026-11-27T09:00:00Z", "hors d'ordre"),
                                                      ("2026-11-26T15:00:00Z", "2026-11-26T14:00:00Z", "hors d'ordre")])
def test_artefacts_scores_absents_ou_dates_hors_d_ordre_refuses(tmp_path, scores, ouverture, motif):
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    reg = _ouverture(tmp_path, table, scores)
    with pytest.raises(GardeArret, match=motif):
        en.verifier_table_a_l_ouverture(table, reg, ouverture)


def test_registre_artefacts_cle_en_double_inconnue_ou_ligne_mal_formee(tmp_path):
    ligne = en.ligne_du_registre("SCORES-B5F", "2026-11-26T15:00:00Z", "x", "")
    with pytest.raises(GardeArret, match="double"):
        en.lire_registre(_registre(tmp_path, [ligne, ligne]))
    with pytest.raises(GardeArret, match="inconnue"):
        en.lignes_du_registre("| AUTRE-B5F | 2026-11-26T15:00:00Z | x | |")
    with pytest.raises(GardeArret, match="attendu"):
        en.lignes_du_registre("| SCORES-B5F | 2026-11-26T15:00:00Z | x |")
    with pytest.raises(GardeArret, match="illisible"):
        en.lignes_du_registre("| SCORES-B5F | 26 novembre | x | |")
    with pytest.raises(GardeArret):
        en.ligne_du_registre("SCORES-B5F", "2026-11-26T15:00:00Z", "a | b", "")


def _etat(v):
    return {"couche.A": torch.full((2, 3), float(v)), "couche.B": torch.zeros(3, 2)}


def test_entrees_de_lecture_noms_opaques_tenseurs_seuls_cas_sain(tmp_path):
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    adaptateurs = {cle: _etat(k) for k, cle in enumerate(TENUS)}
    sortie = en.preparer_entrees_de_lecture(adaptateurs, table, tmp_path / "entrees",
                                            {("A1", "saboteur"): _etat(99), ("A1", "jumeau"): _etat(98)})
    assert len(sortie) == 32
    for x in table:
        octets = (tmp_path / "entrees" / f"{x['nom']}.safetensors").read_bytes()
        assert x["famille"].encode() not in octets and x["membre"].encode() not in octets   # aucune étiquette dans le fichier
        k = TENUS.index((x["famille"], x["membre"]))
        assert torch.equal(en.charger_entree(tmp_path / "entrees" / f"{x['nom']}.safetensors")["couche.A"], _etat(k)["couche.A"])


def test_artefacts_entrees_de_lecture_adaptateur_manquant_intrus_ou_etiquete_hors_apprentissage(tmp_path):
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    adaptateurs = {cle: _etat(0) for cle in TENUS[:-1]}
    with pytest.raises(GardeArret, match="table des étiquettes"):
        en.preparer_entrees_de_lecture(adaptateurs, table, tmp_path / "e1")
    complets = {cle: _etat(0) for cle in TENUS}
    with pytest.raises(GardeArret, match="hors des familles d'apprentissage"):
        en.preparer_entrees_de_lecture(complets, table, tmp_path / "e2", {("T01", "saboteur"): _etat(1)})
    en.preparer_entrees_de_lecture(complets, table, tmp_path / "e3")
    (tmp_path / "e3" / "table.json").write_text(json.dumps(table), encoding="utf-8")     # la table glissée dans l'arbre
    with pytest.raises(GardeArret, match="non admis"):
        en.exiger_entrees_de_lecture_propres(tmp_path / "e3", [x["nom"] for x in table], [])


def _episodes(dossier, famille, membre, lignes_de=None):
    """Fichier `evaluation-<membre>.jsonl` de la formation, scellé ; `lignes_de` : (famille, membre) écrits dans les
    lignes, s'ils diffèrent (artefact)."""
    f, m = lignes_de or (famille, membre)
    dossier.mkdir(parents=True, exist_ok=True)
    p = dossier / f"evaluation-{membre}.jsonl"
    p.write_text("".join(json.dumps({"famille": f, "membre": m, "tache": f"e{k}", "pas": 0, "texte": "x", "cout": 300.0})
                         + "\n" for k in range(3)), encoding="utf-8")
    sceller(p)
    return p


def test_entrees_de_lecture_episodes_d_evaluation_des_saboteurs_d_apprentissage_cas_sain(tmp_path):
    """Constat M-8 (texte, point 7, deuxième tiret) : les épisodes d'évaluation des saboteurs d'apprentissage entrent dans
    la lecture, copiés à l'octet sous `A<k>-saboteur-evaluation.jsonl`, scellés ; nom de formation à suffixe admis."""
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    complets = {cle: _etat(0) for cle in TENUS}
    a1 = _episodes(tmp_path / "formation" / "A1", "A1", "saboteur")
    a2 = _episodes(tmp_path / "formation" / "A2-x1-r1", "A2", "saboteur", ("A2-x1-r1", "saboteur"))
    sortie = en.preparer_entrees_de_lecture(complets, table, tmp_path / "entrees", {("A1", "saboteur"): _etat(9)},
                                            {("A1", "saboteur"): a1, ("A2", "saboteur"): a2})
    assert {"A1-saboteur-evaluation.jsonl", "A2-saboteur-evaluation.jsonl"} <= set(sortie)
    assert (tmp_path / "entrees" / "A1-saboteur-evaluation.jsonl").read_bytes() == a1.read_bytes()
    en.exiger_entrees_de_lecture_propres(tmp_path / "entrees", [x["nom"] for x in table], [("A1", "saboteur")],
                                         [("A1", "saboteur"), ("A2", "saboteur")])
    with pytest.raises(GardeArret, match="non admis"):                       # sans les déclarer : refusés
        en.exiger_entrees_de_lecture_propres(tmp_path / "entrees", [x["nom"] for x in table], [("A1", "saboteur")])


@pytest.mark.parametrize("cas", ["jumeau", "tenue_a_l_ecart", "lignes_d_un_jumeau", "autre_famille", "non_scelle"])
def test_artefacts_entrees_de_lecture_episodes_hors_des_saboteurs_d_apprentissage_refuses(tmp_path, cas):
    """Constat M-8 : épisodes d'un jumeau, d'une famille tenue à l'écart (dont le coût ne doit jamais atteindre la
    lecture), lignes d'un autre membre ou d'une autre famille, fichier non scellé : refus, avant toute écriture."""
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    complets = {cle: _etat(0) for cle in TENUS}
    d = tmp_path / "formation"
    fabriquer = {"jumeau": lambda: {("A1", "jumeau"): _episodes(d / "A1", "A1", "jumeau")},
                 "tenue_a_l_ecart": lambda: {("T01", "saboteur"): _episodes(d / "T01", "T01", "saboteur")},
                 "lignes_d_un_jumeau": lambda: {("A1", "saboteur"): _episodes(d / "A1", "A1", "saboteur", ("A1", "jumeau"))},
                 "autre_famille": lambda: {("A1", "saboteur"): _episodes(d / "A1", "A1", "saboteur", ("A2", "saboteur"))},
                 "non_scelle": lambda: {("A1", "saboteur"): _episodes(d / "A1", "A1", "saboteur")}}
    episodes = fabriquer[cas]()
    if cas == "non_scelle":
        (d / "A1" / "evaluation-saboteur.jsonl.sha256").unlink()
    with pytest.raises(GardeArret):
        en.preparer_entrees_de_lecture(complets, table, tmp_path / "entrees", None, episodes)
    assert not (tmp_path / "entrees").exists()
    with pytest.raises(GardeArret, match="saboteurs d'apprentissage seulement"):
        en.exiger_entrees_de_lecture_propres(tmp_path, [], [], [("T01", "saboteur")])


def test_registre_lu_a_un_commit_et_non_dans_l_arbre_de_travail(tmp_path):
    """Constat m-11 : le registre lu au commit de la course, jamais dans l'arbre de travail ; une ligne retouchée dans
    l'arbre après le commit n'est pas vue."""
    import subprocess

    def git(*a):
        return subprocess.run(["git", "-C", str(tmp_path), *a], check=True, capture_output=True, text=True).stdout.strip()

    git("init", "-q")
    git("config", "user.email", "essai@invalid")
    git("config", "user.name", "essai")
    table = en.table_des_etiquettes(en.tirer_sel(), TENUS)
    reg = tmp_path / en.REGISTRE_PROPRE
    reg.parent.mkdir(parents=True)
    reg.write_text(en.ligne_engagement(table, "2026-11-24T10:00:00Z") + "\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "engagement")
    commit = git("rev-parse", "HEAD")
    reg.write_text(en.ligne_engagement(table, "2026-11-26T10:00:00Z") + "\n", encoding="utf-8")   # retouché, non commis
    lignes = en.lignes_au_commit(tmp_path, commit)
    assert en.verifier_engagement_avant_lecture(None, "2026-11-26T08:00:00Z", lignes=lignes)["empreinte"] == \
        en.empreinte_table(table)
    with pytest.raises(GardeArret, match="postérieur"):                        # l'arbre de travail dirait l'inverse
        en.verifier_engagement_avant_lecture(reg, "2026-11-26T08:00:00Z")
    with pytest.raises(GardeArret, match="absent du commit"):
        en.lignes_au_commit(tmp_path, "0" * 40)


def test_registre_cle_de_relance_admise():
    lignes = en.lignes_du_registre(en.ligne_du_registre("GO-RELANCE-FORMATION-B5F", "2026-11-25T08:00:00Z",
                                                        "GO-2026-11-25-01 ; instances 3", ""))
    assert lignes["GO-RELANCE-FORMATION-B5F"]["contenu"] == "GO-2026-11-25-01 ; instances 3"
