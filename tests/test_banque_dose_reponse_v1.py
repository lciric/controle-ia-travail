"""Essais du portage de la sélection et de l'extraction à la banque de 64 tâches neuves de la course de dose–réponse
de l'organisme à consigne cachée (rang de départ 125, cible de 64 tâches) : chaque garde nouvelle sur un cas sain et
sur un artefact (R5), et un déroulé complet dans un dépôt jetable."""
import hashlib
import json
import shutil
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.environnements import corpus_arxiv_banque_dose_reponse_v1 as sel
from controle_ia.environnements import extraire_banque_dose_reponse_v1 as eb
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, lire_manifeste
from controle_ia.scellement import sceller

import test_extraire_t05 as t05

RACINE = Path(__file__).resolve().parents[1]


# --- sélection ---------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("brut, attendu", [("2604.12086v1", "2604.12086"), ("2508.12726v6", "2508.12726"),
                                          ("2604.12086", "2604.12086"), ("2510.02779v12", "2510.02779")])
def test_sans_version(brut, attendu):
    assert sel.sans_version(brut) == attendu


def test_garde_par_papier_cas_sain_et_artefacts():
    sel.exiger_hors_banque_initiale(125, "2601.00001", {"2601.99999"}, {"2601.88888"})
    with pytest.raises(GardeArret, match="inférieur à 125"):
        sel.exiger_hors_banque_initiale(124, "2601.00001", set(), set())
    with pytest.raises(GardeArret, match="banque initiale"):
        sel.exiger_hors_banque_initiale(130, "2601.99999", {"2601.99999"}, set())
    with pytest.raises(GardeArret, match="banque initiale"):
        sel.exiger_hors_banque_initiale(130, "2601.88888", set(), {"2601.88888"})


def _traiter_factice(exclus=()):
    vus = []

    def traiter(entree, racine_donnees, filtre, journal=None):
        vus.append(entree["id"])
        statut = "exclu" if entree["id"] in exclus else "gardé"
        return {"id": entree["id"], "version": 1, "statut": statut, **({"motif": "source PDF seulement"}
                                                                      if statut == "exclu" else {})}
    return traiter, vus


def test_constituer_depuis_commence_au_rang_125_et_s_arrete_au_besoin(tmp_path):
    ordre = [f"2601.{k:05d}" for k in range(200)]
    entrees = {p: {"id": p, "version": 1} for p in ordre}
    traiter, vus = _traiter_factice(exclus={ordre[126]})
    fiches = sel.constituer_depuis(ordre, entrees, 3, tmp_path, tmp_path / "f.lua", set(), set(), traiter=traiter,
                                   dormir=lambda s: None)
    assert vus == ordre[125:129]                                  # aucun papier lu avant son tour, ni au-delà
    assert [f["rang_tirage"] for f in fiches] == [125, 126, 127, 128]
    assert [f.get("rang_garde") for f in fiches] == [0, None, 1, 2]


def test_constituer_depuis_candidats_epuises(tmp_path):
    ordre = [f"2601.{k:05d}" for k in range(127)]
    traiter, _ = _traiter_factice()
    fiches = sel.constituer_depuis(ordre, {p: {"id": p, "version": 1} for p in ordre}, 5, tmp_path, tmp_path / "f.lua", set(),
                                   set(), traiter=traiter, dormir=lambda s: None)
    assert len(fiches) == 2                                       # plus court que le besoin : constaté par l'appelant


def test_constituer_depuis_arrete_sur_un_papier_initial(tmp_path):
    ordre = [f"2601.{k:05d}" for k in range(200)]
    traiter, vus = _traiter_factice()
    with pytest.raises(GardeArret, match="banque initiale"):
        sel.constituer_depuis(ordre, {p: {"id": p, "version": 1} for p in ordre}, 5, tmp_path, tmp_path / "f.lua",
                              {ordre[126]}, set(), traiter=traiter, dormir=lambda s: None)
    assert vus == [ordre[125]]                                    # arrêt avant tout téléchargement du papier fautif


def test_relire_tirage_et_banque_initiale_du_depot():
    t = sel.relire_tirage(RACINE)
    assert len(t["ordre"]) == 1836 and len(t["deja_examines"]) == 125
    initiaux = sel.identifiants_initiaux(RACINE)
    assert len(initiaux) == 96 and initiaux <= t["deja_examines"]
    assert not {sel.sans_version(p) for p in t["ordre"][125:]} & initiaux


def _copie_tirage(dest: Path) -> None:
    for rel in (sel.REGLE, sel.MANIFESTE_TIRAGE):
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        for suffixe in ("", ".sha256"):
            shutil.copyfile(RACINE / (rel + suffixe), dest / (rel + suffixe))
    shutil.copytree(RACINE / sel.RUN_TIRAGE, dest / sel.RUN_TIRAGE)


def test_relire_tirage_artefact_candidats(tmp_path):
    _copie_tirage(tmp_path)
    sel.relire_tirage(tmp_path)                                   # cas sain sur la copie
    chemin = tmp_path / sel.RUN_TIRAGE / "candidats.json"
    corps = json.loads(chemin.read_text())
    corps["resultat"]["candidats"] = corps["resultat"]["candidats"][1:]
    chemin.write_text(json.dumps(corps))
    (chemin.parent / (chemin.name + ".sha256")).unlink()          # artefact resscellé (le sceau ne le rattrape pas)
    sceller(chemin)
    with pytest.raises(GardeArret, match="candidats scellés"):
        sel.relire_tirage(tmp_path)


def test_relire_tirage_artefact_ordre(tmp_path):
    _copie_tirage(tmp_path)
    chemin = tmp_path / sel.RUN_TIRAGE / "tirage.json"
    corps = json.loads(chemin.read_text())
    o = corps["resultat"]["ordre"]
    o[0], o[1] = o[1], o[0]
    chemin.write_text(json.dumps(corps))
    (chemin.parent / (chemin.name + ".sha256")).unlink()          # artefact resscellé (le sceau ne le rattrape pas)
    sceller(chemin)
    with pytest.raises(GardeArret, match="ordre scellé"):
        sel.relire_tirage(tmp_path)


def test_relire_tirage_artefact_sceau(tmp_path):
    _copie_tirage(tmp_path)
    chemin = tmp_path / sel.RUN_TIRAGE / "api-page-01.xml"
    chemin.write_bytes(chemin.read_bytes() + b" ")
    with pytest.raises(Exception):                                # R11 : empreinte différente, arrêt sans rien écrire
        sel.relire_tirage(tmp_path)


# --- extraction : dépôt jetable ----------------------------------------------------------------------------------

def _taches_initiales(depot: Path, n: int = 96) -> None:
    for rel, debut, compte in ((sel.TACHES_INITIALES[0], 0, 64), (sel.TACHES_INITIALES[1], 64, n - 64)):
        chemin = depot / rel
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(json.dumps({"resultat": {"taches": [{"identifiant": f"2501.{k:05d}v1"}
                                                              for k in range(debut, debut + compte)]}}))
        sceller(chemin)


def _depot_banque(depot: Path, n_pilote=3, n_reserve=3, rang0=125, papier_initial=False, graine_autre=False,
                  exclu_au_rang=None, tirage_faux=False, besoin=None):
    """Dépôt jetable : celui de l'essai de l'extraction des 96 (procédure, fichiers, invites), plus les modules portés,
    les deux fichiers de tâches initiaux (96 identifiants), un tirage scellé factice (rangs 0 à rang0 - 1 occupés par
    des papiers déjà examinés), un manifeste de l'extraction initiale à la même graine, et la sélection (fiches aux
    rangs consécutifs depuis rang0 ; `exclu_au_rang` : une fiche exclue de la sélection à cette position)."""
    (depot / ".gitignore").write_text("donnees/\n")
    dp = depot / "docs" / "procedures" / "T0.5-extraction-v1"
    dp.mkdir(parents=True)
    for nom in eb.FICHIERS_PROCEDURE.values():
        shutil.copyfile(t05.PROC / nom, dp / nom)
        sceller(dp / nom)
    (depot / "docs" / "procedures" / "T0.5-extraction-v1.md").write_text("procédure de test\n")
    proc_sha = sceller(depot / "docs" / "procedures" / "T0.5-extraction-v1.md")
    for m in eb.Chemins().modules:
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RACINE / m, depot / m)
    shutil.copytree(RACINE / "docs" / "sources" / "invites-2606.08892-v1", depot / "invites")
    _taches_initiales(depot)
    textes = depot / "donnees" / "textes"
    textes.mkdir(parents=True)
    fiches, k_garde = [], 0
    for k in range(n_pilote + n_reserve + (exclu_au_rang is not None)):
        rang = rang0 + k
        if exclu_au_rang is not None and k == exclu_au_rang:
            fiches.append({"id": f"2602.{k:05d}", "version": 1, "statut": "exclu", "motif": "source PDF seulement",
                           "rang_tirage": rang})
            continue
        pid = "2501.00000" if (papier_initial and k_garde == 1) else f"2601.{k:05d}"
        contenu = t05.TEXTE.replace("routers", f"routers ({k})")
        (textes / f"{pid}v1.md").write_text(contenu, encoding="utf-8")
        fiches.append({"id": pid, "version": 1, "statut": "gardé", "rang_garde": k_garde, "rang_tirage": rang,
                       "texte_sha256": hashlib.sha256(contenu.encode()).hexdigest()})
        k_garde += 1
    ordre = [f"2400.{k:05d}" for k in range(rang0)] + [f["id"] for f in fiches] + ["2700.00001", "2700.00002"]
    if tirage_faux:
        ordre[rang0], ordre[rang0 + 1] = ordre[rang0 + 1], ordre[rang0]
    committer(depot)
    m_t, _ = creer_manifeste(depot, "20261006-134235-t05-corpus", {"x": 1}, [])
    ecrire_resultat(depot, m_t, "tirage", {"ordre": ordre, "graine": {}})
    committer(depot)
    entropie = int(proc_sha[:32], 16) + (1 if graine_autre else 0)
    creer_manifeste(depot, "20261007-082440-t05-extraction", {"x": 1}, [eb.TACHE_GRAINE], entropie=entropie)
    committer(depot)
    chemin_m, _ = creer_manifeste(depot, "20260101-000000-corpus", {
        "rang_depart": 125, "besoin": n_pilote + n_reserve if besoin is None else besoin}, [])
    ecrire_resultat(depot, chemin_m, "corpus", {"fiches": fiches})
    committer(depot)
    return eb.Chemins(corpus="diag/20260101-000000-corpus/corpus.json", textes="donnees/textes",
                      invites=depot / "invites")


def _tirage_factice(depot):
    """Ordre scellé du dépôt jetable, et entrées des « pages » (version 1), pour le contrôle final."""
    ordre = sel.ordre_scelle(depot)
    return {"ordre": ordre, "entrees": {p: {"version": 1} for p in ordre}}


def _petit(monkeypatch, echantillon=2, seuil=1, audit=1):
    monkeypatch.setattr(eb, "TAILLE_PILOTE", 3)
    monkeypatch.setattr(eb, "TAILLE_RESERVE", 3)
    monkeypatch.setattr(eb, "TAILLE_ECHANTILLON", echantillon)
    monkeypatch.setattr(eb, "SEUIL_ECHECS", seuil)
    monkeypatch.setattr(eb, "TAILLE_AUDIT", audit)


RUN = "20260102-000000-extraction"


def test_deroule_complet_banque(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = eb.preparer(depot, RUN, travail, 1, ch=ch)
    m, _ = lire_manifeste(depot / "runs" / RUN / "manifeste.json")
    initiale, _ = lire_manifeste(depot / "runs" / "20261007-082440-t05-extraction" / "manifeste.json")
    assert m["graines"] == initiale["graines"]                    # aucune graine neuve
    assert m["config"]["corpus"] == ch.corpus and eb.chemins_du_run(depot, RUN).textes == ch.textes
    assert m["config"]["rang_depart"] == 125
    ids = sorted(prep["papiers"])
    for pid in ids:                                               # le 2e papier du « pilote » est « theory_only »
        h10 = t05._avec(t05.H10, theory_experiment="theory_only") if pid == ids[1] else t05.H10
        t05._repondre(prep["papiers"][pid]["dossier"], h10=h10)
    eb.valider(depot, RUN, 1, t05._retours(prep), ch=ch)
    ech = eb.echantillonner(depot, RUN, ch=ch)
    cv = eb.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    th = eb.preparer_contre_verification(depot, RUN, travail, "theorie", ch=ch)
    for pid in ech["echantillon"]:
        t05._juger(cv["papiers"][pid]["dossier"])
    t05._juger(th["papiers"][ids[1]]["dossier"],                  # « theory_only » confirmé : exclu
               t05._avec(t05.AVIS, theory_experiment_expected="theory_only"))
    eb.lire_contre_verification(depot, RUN, 1, t05._retours(cv), ch=ch)
    eb.lire_contre_verification(depot, RUN, 2, t05._retours(th), ch=ch)
    au = eb.preparer_contre_verification(depot, RUN, travail, "audit", ch=ch)   # côté propre : audit R4
    for pid in au["papiers"]:
        t05._juger(au["papiers"][pid]["dossier"])
    eb.lire_contre_verification(depot, RUN, 3, t05._retours(au), ch=ch)
    bilan = eb.assembler(depot, RUN, ch=ch)
    assert bilan["audit"]["cote"] == "propre"
    assert bilan["exclus"] == {ids[1]: "theory_only (confirmé)"}
    # la banque : les 3 premiers retenus dans l'ordre du tirage (le module scellé met le remplaçant à la place de
    # l'exclu ; ici l'ordre du tirage est rétabli)
    assert bilan["evaluation"] == [ids[0], ids[2], ids[3]]
    assert bilan["remplacements"] == [{"exclu": ids[1], "remplacant": ids[3]}]
    assert bilan["entrainement"] == [ids[4], ids[5]]
    d = depot / "donnees" / RUN
    banque = json.loads((d / "taches-banque.json").read_text())["resultat"]
    assert [t["identifiant"] for t in banque["taches"]] == bilan["evaluation"]
    hors = json.loads((d / "taches-hors-banque.json").read_text())["resultat"]
    assert [t["identifiant"] for t in hors["taches"]] == [ids[4], ids[5]]
    assert not (d / "taches-evaluation.json").exists()
    assert set(eb.fichiers_consignes(depot, RUN)) >= {"taches-banque.json", "taches-hors-banque.json"}
    assert bilan["entrainement_insuffisant"] is None
    monkeypatch.setattr(eb, "relire_tirage_scelle", _tirage_factice)
    controle = eb.controler_banque(depot, RUN, ch=ch)
    assert controle["conforme"] and controle["taches"] == 3 and controle["rangs"] == [125, 127, 128]
    assert m["config"]["modele_sous_agents"].startswith("non nommé")
    assert "module:corpus_arxiv_banque_dose_reponse_v1.py" in m["config"]["fichiers_scelles"]


def test_graine_differente_de_l_extraction_initiale_arrete(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot, graine_autre=True)
    with pytest.raises(GardeArret, match="aucune graine neuve"):
        eb.preparer(depot, RUN, tmp_path_factory.mktemp("travail"), 1, ch=ch)
    assert not (depot / "runs" / RUN).exists()                    # arrêt avant le manifeste


def test_corpus_avec_un_papier_initial_arrete(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot, papier_initial=True)
    with pytest.raises(GardeArret, match="banque initiale"):
        eb.preparer(depot, RUN, tmp_path_factory.mktemp("travail"), 1, ch=ch)


def test_corpus_avec_un_rang_inferieur_a_125_arrete(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot, rang0=120)
    with pytest.raises(GardeArret, match="non confrontables au tirage"):
        eb.preparer(depot, RUN, tmp_path_factory.mktemp("travail"), 1, ch=ch)


def test_chemins_non_fixes_arrete(depot):
    with pytest.raises(GardeArret, match="non fixés"):
        eb.papiers_du_corpus(depot, eb.Chemins())


def test_banque_dans_l_ordre_du_tirage_cas_sain_et_artefact(monkeypatch):
    monkeypatch.setattr(eb, "TAILLE_PILOTE", 3)
    st = {p: {"statut": s} for p, s in zip("abcde", ("retenu", "exclu", "retenu", "retenu", "retenu"))}
    rangs = {p: 125 + k for k, p in enumerate("abcde")}
    assert eb.banque_dans_l_ordre_du_tirage(list("abcde"), rangs, st, ["a", "d", "c"]) == ["a", "c", "d"]
    with pytest.raises(GardeArret, match="64 premiers"):
        eb.banque_dans_l_ordre_du_tirage(list("abcde"), rangs, st, ["a", "c", "e"])
    with pytest.raises(GardeArret, match="non strictement croissant"):
        eb.banque_dans_l_ordre_du_tirage(list("abdce"), rangs, st, ["a", "d", "c"])


def test_ligne_de_commande_exige_les_chemins_a_la_tentative_1(depot):
    with pytest.raises(GardeArret, match="--corpus et --textes requis"):
        eb._main(["preparer", "--run-id", RUN, "--travail", "/tmp/x", "--tentative", "1"])


# --- corrections de la contre-lecture du code (remarques CL-1 à CL-12) ------------------------------------------

def test_constantes_de_la_portee_a_leur_valeur_reelle():
    assert (sel.RANG_DEPART, sel.CIBLE_TACHES, sel.MARGE, sel.BESOIN) == (125, 64, 16, 80)
    assert (eb.RANG_DEPART, eb.TAILLE_PILOTE, eb.TAILLE_RESERVE) == (125, 64, 16)
    assert eb.TAILLE_ECHANTILLON == 16 and eb.SEUIL_ECHECS == 4 and eb.TAILLE_AUDIT == 4     # inchangés


def test_parite_de_la_chaine_avec_le_6_octobre():
    m, _ = lire_manifeste(RACINE / sel.MANIFESTE_TIRAGE)
    sel.exiger_parite_de_la_chaine(m["config"])
    with pytest.raises(GardeArret, match="pause_s"):
        sel.exiger_parite_de_la_chaine(dict(m["config"], pause_s=1.0))


def test_pannes_d_acces_arretent_une_exclusion_isolee_reste(tmp_path):
    ordre = [f"2601.{k:05d}" for k in range(200)]
    entrees = {p: {"id": p, "version": 1} for p in ordre}

    def traiter_motifs(indisponibles):
        def traiter(entree, racine_donnees, filtre, journal=None):
            if entree["id"] in indisponibles:
                return {"id": entree["id"], "version": 1, "statut": "exclu", "motif": "source indisponible (HTTP 404)"}
            return {"id": entree["id"], "version": 1, "statut": "gardé"}
        return traiter
    au_fil = tmp_path / "fiches.jsonl"
    fiches = sel.constituer_depuis(ordre, entrees, 3, tmp_path, tmp_path / "f.lua", set(), set(),
                                   traiter=traiter_motifs({ordre[126]}), dormir=lambda s: None, au_fil=au_fil)
    assert [f["statut"] for f in fiches] == ["gardé", "exclu", "gardé", "gardé"]
    assert len(au_fil.read_text().splitlines()) == 4                    # fiches écrites au fil de l'eau
    with pytest.raises(GardeArret, match="panne d'accès"):
        sel.constituer_depuis(ordre, entrees, 3, tmp_path, tmp_path / "f.lua", set(), set(),
                              traiter=traiter_motifs(set(ordre[125:130])), dormir=lambda s: None)


def test_version_des_pages_exigee(tmp_path):
    ordre = [f"2601.{k:05d}" for k in range(200)]
    traiter, _ = _traiter_factice()                                    # rend la version 1
    with pytest.raises(GardeArret, match="version des pages"):
        sel.constituer_depuis(ordre, {p: {"id": p, "version": 2} for p in ordre}, 3, tmp_path, tmp_path / "f.lua",
                              set(), set(), traiter=traiter, dormir=lambda s: None)


@pytest.mark.parametrize("besoin", ["63", "100"])
def test_selection_exige_le_besoin_de_la_portee(tmp_path, besoin):
    with pytest.raises(GardeArret, match="portée fixe 80"):
        sel._main(["selectionner", "--run-id", "20260101-000000-x", "--donnees", str(tmp_path / "neuf"),
                   "--besoin", besoin])


def test_relire_tirage_artefact_cinquieme_page(tmp_path):
    _copie_tirage(tmp_path)
    shutil.copyfile(tmp_path / sel.RUN_TIRAGE / "api-page-00.xml", tmp_path / sel.RUN_TIRAGE / "api-page-04.xml")
    with pytest.raises(GardeArret, match="plus de pages"):
        sel.relire_tirage(tmp_path)


def test_relire_tirage_artefact_corpus_initial(tmp_path):
    _copie_tirage(tmp_path)
    chemin = tmp_path / sel.RUN_TIRAGE / "corpus.json"
    corps = json.loads(chemin.read_text())
    corps["resultat"]["fiches"] = corps["resultat"]["fiches"][:-1]
    chemin.write_text(json.dumps(corps))
    (chemin.parent / (chemin.name + ".sha256")).unlink()
    sceller(chemin)
    with pytest.raises(GardeArret, match="rangs 0 à 124"):
        sel.relire_tirage(tmp_path)


def test_corpus_au_besoin_autre_arrete(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot, besoin=80)
    with pytest.raises(GardeArret, match="besoin de la portée"):
        eb.preparer(depot, RUN, tmp_path_factory.mktemp("travail"), 1, ch=ch)


def test_corpus_hors_du_tirage_arrete(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot, tirage_faux=True)
    with pytest.raises(GardeArret, match="non confrontables au tirage"):
        eb.preparer(depot, RUN, tmp_path_factory.mktemp("travail"), 1, ch=ch)


def test_module_de_selection_epingle_et_corpus_fixe(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot, exclu_au_rang=1)                          # une exclusion de la sélection : cas sain
    eb.preparer(depot, RUN, tmp_path_factory.mktemp("travail"), 1, ch=ch)
    with pytest.raises(GardeArret, match="corpus de la sélection différent"):
        eb.echantillonner(depot, RUN, ch=eb.Chemins(corpus=ch.corpus, textes="donnees/autres", invites=ch.invites))
    mod = depot / "src" / "controle_ia" / "environnements" / "corpus_arxiv_banque_dose_reponse_v1.py"
    mod.write_text(mod.read_text() + "\n# modifié\n")
    with pytest.raises(GardeArret, match="modules de décision changés"):
        eb.echantillonner(depot, RUN, ch=ch)


def _ecarts(**changes):
    ordre = [f"2400.{k:05d}" for k in range(125)] + [f"2601.{k:05d}" for k in range(6)]
    entrees = {p: {"version": 1} for p in ordre}
    banque = ["2601.00000v1", "2601.00002v1", "2601.00003v1"]
    hors = ["2601.00004v1"]
    rangs = {f"2601.{k:05d}v1": 125 + k for k in range(6)}
    statuts = {p: {"statut": "retenu"} for p in rangs} | {"2601.00001v1": {"statut": "exclu"}}
    args = dict(banque=banque, hors_banque=hors, statuts=statuts, rangs=rangs, ordre=ordre, entrees=entrees,
                initiaux={"2400.00000"})
    args.update(changes)
    return eb.ecarts_de_la_banque(**args)


def test_controle_final_de_la_banque_cas_sain_et_artefacts(monkeypatch):
    monkeypatch.setattr(eb, "TAILLE_PILOTE", 3)
    assert _ecarts() == []
    assert any("tâches" in e for e in _ecarts(banque=["2601.00000v1", "2601.00002v1"]))
    assert any("banque initiale" in e for e in _ecarts(initiaux={"2601.00002"}))
    ordre_bas = [f"2400.{k:05d}" for k in range(124)] + [f"2601.{k:05d}" for k in range(6)]
    assert any("inférieur à 125" in e for e in _ecarts(ordre=ordre_bas))
    assert any("non strictement croissants" in e for e in _ecarts(banque=["2601.00002v1", "2601.00000v1",
                                                                         "2601.00003v1"]))
    assert any("version" in e for e in _ecarts(banque=["2601.00000v2", "2601.00002v1", "2601.00003v1"]))
    assert any("hors banque" in e for e in _ecarts(hors_banque=["2601.00001v1"]))
    st = {p: {"statut": "retenu"} for p in [f"2601.{k:05d}v1" for k in range(6)]}
    assert any("ni dans la banque ni exclu" in e for e in _ecarts(statuts=st))
    assert any("au manifeste" in e for e in _ecarts(rangs={"2601.00000v1": 999, "2601.00002v1": 127,
                                                           "2601.00003v1": 128, "2601.00001v1": 126}))


def test_reserve_epuisee_arret_consigne(depot, tmp_path_factory, monkeypatch):
    _petit(monkeypatch)
    ch = _depot_banque(depot)
    travail = tmp_path_factory.mktemp("travail")
    prep = eb.preparer(depot, RUN, travail, 1, ch=ch)
    ids = sorted(prep["papiers"])
    theoriques = set(ids[:4])                                           # 4 exclus pour 3 places de réserve
    for pid in ids:
        h10 = t05._avec(t05.H10, theory_experiment="theory_only") if pid in theoriques else t05.H10
        t05._repondre(prep["papiers"][pid]["dossier"], h10=h10)
    eb.valider(depot, RUN, 1, t05._retours(prep), ch=ch)
    ech = eb.echantillonner(depot, RUN, ch=ch)
    cv = eb.preparer_contre_verification(depot, RUN, travail, "echantillon", ch=ch)
    th = eb.preparer_contre_verification(depot, RUN, travail, "theorie", ch=ch)
    for pid in ech["echantillon"]:
        t05._juger(cv["papiers"][pid]["dossier"])
    for pid in theoriques:
        t05._juger(th["papiers"][pid]["dossier"], t05._avec(t05.AVIS, theory_experiment_expected="theory_only"))
    eb.lire_contre_verification(depot, RUN, 1, t05._retours(cv), ch=ch)
    eb.lire_contre_verification(depot, RUN, 2, t05._retours(th), ch=ch)
    au = eb.preparer_contre_verification(depot, RUN, travail, "audit", ch=ch)
    for pid in au["papiers"]:
        t05._juger(au["papiers"][pid]["dossier"])
    eb.lire_contre_verification(depot, RUN, 3, t05._retours(au), ch=ch)
    with pytest.raises(GardeArret, match="réserve épuisée"):
        eb.assembler(depot, RUN, ch=ch)
    arret = json.loads((depot / "diag" / RUN / "arret-assemblage.json").read_text())["resultat"]
    assert "suite du tirage existant" in arret["suite"]
