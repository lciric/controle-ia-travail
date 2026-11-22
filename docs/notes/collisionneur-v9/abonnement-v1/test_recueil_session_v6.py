"""Essais du recueil v6 (copie des v5 ; essais v6 en fin). Essais du recueil v5 (copie des v4, accordés : ouverture = SERVI ; essais v5 en fin). Essais du recueil v4 (copie des essais v3 ; essais v4 en fin). Essais du recueil v3 (copie des essais v2, accordés ; essais v3 en fin). Essais du recueil v2 : pages d'événements synthétiques, aucun réseau. Lecture permise, couverture, outils refusés,
second modèle refusé, versement hors dossier."""
import importlib.util
import json
import os
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
CHEMIN = Path(os.environ.get("RECUEIL_MODULE") or ICI / "recueil_session_v6.py")


def charger():
    s = importlib.util.spec_from_file_location("recueil_essai", CHEMIN)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


INVITE = "Lis texte-servi.md en entier, puis réponds à ce qu'il demande."
SERVI = "".join(f"ligne {k} du texte servi\n" for k in range(1, 11))


def rendu(texte, debut=1, n=2000, fleche=False):
    ls = texte.split("\n")[:-1][debut - 1:debut - 1 + n]
    return "\n".join(f"{k:>6}{'→' if fleche else chr(9)}{l}" for k, l in enumerate(ls, start=debut))


def page(tmp, outils=(), tours=None, modeles=("claude-opus-5-5",), fin="end_turn", texte="Réponse. FIN-DE-CELLULE",
         retours=None, ouverture="DEFAUT"):
    evs = []
    if ouverture is not None:
        evs.append({"user": {"internal_anthropic_catchall": {"message": {
            "content": (INVITE if any(n == "Read" for n, _ in outils) else SERVI) if ouverture == "DEFAUT"
            else ouverture}}}})
    for j, (n, i) in enumerate(outils):
        evs.append({"assistant": {"internal_anthropic_catchall": {"message": {"content": [
            {"type": "tool_use", "id": f"t{j}", "name": n, "input": i}]}}}})
        if retours is not None and j < len(retours) and retours[j] is not None:
            contenu, err = retours[j]
            evs.append({"user": {"internal_anthropic_catchall": {"message": {"content": [
                {"type": "tool_result", "tool_use_id": f"t{j}", "content": contenu, "is_error": err}]}}}})
    evs.append({"assistant": {"internal_anthropic_catchall": {"message": {"content": [{"type": "text", "text": texte}]}}}})
    evs.append({"result": {"internal_anthropic_catchall": {
        "result": texte, "stop_reason": fin, "subtype": "success", "is_error": False,
        "num_turns": tours if tours is not None else len(outils) + 1,
        "modelUsage": {m: {} for m in modeles}, "usage": {"server_tool_use": {}}, "total_cost_usd": 1.0}}})
    f = tmp / f"page-{len(list(tmp.glob('page-*')))}.txt"
    f.write_text("en-tête\n" + json.dumps({"ccr": {"data": evs}}), encoding="utf-8")
    return f


def lecture(nom="texte-servi.md", offset=None, limit=None):
    i = {"file_path": f"/home/user/depot/{nom}"}
    if offset:
        i["offset"] = offset
    if limit:
        i["limit"] = limit
    return ("Read", i)


def test_sans_outil_sain(tmp_path):
    m = charger()
    _, fin, modele, ecarts, _ = m.lire(page(tmp_path), texte_servi=SERVI)
    assert ecarts == [] and fin == "end_turn" and modele == "claude-opus-5-5"


def test_outil_refuse_sans_lecture_permise(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, [lecture()]))[3]


def test_lecture_permise_couverte(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture(limit=5), lecture(offset=6, limit=5)],
             retours=[(rendu(SERVI, 1, 5), False), (rendu(SERVI, 6, 5), False)])
    assert m.lire(f, "texte-servi.md", 10, SERVI)[3] == []


def test_lecture_permise_trou_refuse(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture(limit=5), lecture(offset=7, limit=5)],
             retours=[(rendu(SERVI, 1, 5), False), (rendu(SERVI, 7, 4), False)])
    e = m.lire(f, "texte-servi.md", 10, SERVI)[3]
    assert any("jamais lues" in x for x in e)


def test_autre_fichier_ou_autre_outil_refuse(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, [lecture(), lecture("CLAUDE.md")]), "texte-servi.md", 10)[3]
    assert m.lire(page(tmp_path, [lecture(), ("WebSearch", {"query": "x"})]), "texte-servi.md", 10)[3]
    assert m.lire(page(tmp_path, [lecture("autre-texte-servi.md")]), "texte-servi.md", 10)[3]  # suffixe sans « / »


def test_aucune_lecture_refusee(tmp_path):
    m = charger()
    assert any("aucune lecture" in x for x in m.lire(page(tmp_path), "texte-servi.md", 10)[3])


def test_second_modele_refuse(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, modeles=("claude-fable-5-2", "claude-haiku-5-5")))[3]


def test_tours_en_trop_refuses(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, [lecture()], tours=4), "texte-servi.md", 10)[3]


def test_lecture_permise_exige_lignes(tmp_path):
    m = charger()
    with pytest.raises(SystemExit):
        m.principal([str(page(tmp_path, [lecture()])), str(tmp_path / "d"), "C", "s", "--lecture-permise",
                     "texte-servi.md", "--commit-branche", "abc"])


def test_hors_dossier(tmp_path):
    m = charger()
    f = page(tmp_path, [("WebSearch", {"query": "x"})], modeles=("claude-fable-5-2", "claude-haiku-5-5"))
    assert m.principal([str(f), str(tmp_path / "d"), "E3-T1-conception-A", "session_x", "--refusee-avec-outils"]) == 0
    h = tmp_path / "d" / "abonnement" / "hors-dossier"
    assert (h / "E3-T1-conception-A-session_x-avec-outils.md").exists()
    assert not (tmp_path / "d" / "abonnement" / "reponses").exists()


# ---------- v3 ----------

def test_v3_lecture_en_erreur_ne_compte_pas(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture(), lecture(limit=10)], retours=[("fichier trop grand", True), (rendu(SERVI), False)])
    assert m.lire(f, "texte-servi.md", 10, SERVI)[3] == []  # la relecture couvre tout
    f2 = page(tmp_path, [lecture()], retours=[("fichier trop grand", True)])
    assert any("absentes ou différentes" in x for x in m.lire(f2, "texte-servi.md", 10, SERVI)[3])


def test_v3_contenu_different_refuse(tmp_path):
    m = charger()
    autre = SERVI.replace("ligne 4 du", "ligne 4 changée du")
    f = page(tmp_path, [lecture()], retours=[(rendu(autre), False)])
    assert any("absentes ou différentes" in x for x in m.lire(f, "texte-servi.md", 10, SERVI)[3])
    f2 = page(tmp_path, [lecture()], retours=[(rendu(SERVI, fleche=True), False)])
    assert m.lire(f2, "texte-servi.md", 10, SERVI)[3] == []  # forme à flèche admise


def test_v3_retour_absent_refuse(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture()], retours=None)
    assert any("sans retour" in x for x in m.lire(f, "texte-servi.md", 10, SERVI)[3])


def test_v3_retour_en_liste_de_blocs(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture()], retours=[([{"type": "text", "text": rendu(SERVI)}], False)])
    assert m.lire(f, "texte-servi.md", 10, SERVI)[3] == []


def test_v3_kit_absent_refuse(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture()], retours=[(rendu(SERVI), False)])
    assert any("absent" in x for x in m.lire(f, "texte-servi.md", 10, None)[3])


def test_v3_hors_dossier_exige_un_ecart(tmp_path):
    m = charger()
    k = tmp_path / "d" / "abonnement" / "kits" / "C"  # v5 : kit présent, sinon « kit absent » serait un écart
    k.mkdir(parents=True)
    (k / "texte-servi.md").write_text(SERVI, encoding="utf-8")
    with pytest.raises(SystemExit):
        m.principal([str(page(tmp_path)), str(tmp_path / "d"), "C", "s", "--refusee-avec-outils"])


def test_v3_lecture_permise_exige_commit(tmp_path):
    m = charger()
    with pytest.raises(SystemExit):
        m.principal([str(page(tmp_path, [lecture()])), str(tmp_path / "d"), "C", "s", "--lecture-permise",
                     "texte-servi.md", "--lignes", "10"])


# ---------- v4 ----------

def test_v4_premier_tour_ignore_les_suivants(tmp_path):
    m = charger()
    f = page(tmp_path)
    d = json.loads(f.read_text(encoding="utf-8").split("\n", 1)[1])
    d["ccr"]["data"].append({"user": {"internal_anthropic_catchall": {"message": {"content": "message tardif"}}}})
    d["ccr"]["data"].append({"assistant": {"internal_anthropic_catchall": {"message": {"content": [
        {"type": "tool_use", "id": "z", "name": "Bash", "input": {}}]}}}})
    d["ccr"]["data"].append({"result": {"internal_anthropic_catchall": {
        "result": "autre", "stop_reason": "end_turn", "subtype": "success", "is_error": False, "num_turns": 2,
        "modelUsage": {"claude-haiku-5-5": {}, "claude-opus-5-5": {}}, "usage": {}}}})
    f.write_text("x\n" + json.dumps(d), encoding="utf-8")
    with pytest.raises(SystemExit, match="2 résultats"):
        m.lire(f)
    texte, fin, modele, ecarts, r = m.lire(f, texte_servi=SERVI, premier_tour=True)
    assert ecarts == [] and texte == "Réponse. FIN-DE-CELLULE" and r["_tours_ignores"] == 1


def test_v4_sans_option_deux_resultats_refuses(tmp_path):
    m = charger()
    f = page(tmp_path)
    d = json.loads(f.read_text(encoding="utf-8").split("\n", 1)[1])
    d["ccr"]["data"].append(d["ccr"]["data"][-1])
    f.write_text("x\n" + json.dumps(d), encoding="utf-8")
    with pytest.raises(SystemExit):
        m.lire(f)


def test_v4_premier_tour_avec_outil_reste_refuse(tmp_path):
    m = charger()
    f = page(tmp_path, [("WebSearch", {"query": "x"})])
    assert m.lire(f, premier_tour=True)[3]


# ---------- v5 ----------

def test_v5_ouverture_absente_ou_differente_refusee(tmp_path):
    m = charger()
    assert any("aucun message d'ouverture" in x for x in m.lire(page(tmp_path, ouverture=None), texte_servi=SERVI)[3])
    assert any("différent du texte servi" in x
               for x in m.lire(page(tmp_path, ouverture="autre texte"), texte_servi=SERVI)[3])
    assert any("kit absent" in x for x in m.lire(page(tmp_path))[3])
    assert m.lire(page(tmp_path), texte_servi=SERVI)[3] == []  # cas sain


def test_v5_page_commencant_apres_le_premier_tour_refusee(tmp_path):
    m = charger()
    f = page(tmp_path, ouverture="message humain tardif")
    assert m.lire(f, texte_servi=SERVI, premier_tour=True)[3]


# ---------- v6 ----------

def test_v6_voie_fichier_invite_fixee(tmp_path):
    m = charger()
    assert m.INVITE_FICHIER == INVITE
    f = page(tmp_path, [lecture()], retours=[(rendu(SERVI), False)])
    assert m.lire(f, "texte-servi.md", 10, SERVI)[3] == []  # cas sain
    f2 = page(tmp_path, [lecture()], retours=[(rendu(SERVI), False)], ouverture="Lis le fichier et fais autre chose.")
    assert any("invite fixée" in x for x in m.lire(f2, "texte-servi.md", 10, SERVI)[3])
    f3 = page(tmp_path, [lecture()], retours=[(rendu(SERVI), False)], ouverture=None)
    assert any("aucun message d'ouverture" in x for x in m.lire(f3, "texte-servi.md", 10, SERVI)[3])
