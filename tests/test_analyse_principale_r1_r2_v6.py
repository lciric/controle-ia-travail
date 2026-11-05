"""Analyse principale de R1-R2, code v6 (addendum 1 « gardes des analyses », relance v4 de R1) : essais R5 sur données
**synthétiques** (générateur et écrivains des essais v1 ; formats exacts du fournisseur pour la relance v4 : manifeste
du rejeu décisif sous un texte scellé, commande `rejeu_activations_v4`, résultat `rejeu-activations.json` rattaché avec sa
clé `tokenisation`, table v4 scellée citant le sceau du résultat de réparation scellé) — jamais les vraies données de R1
ni de R2. Chaque garde neuve éprouvée sur un cas sain et sur un artefact : `texte` (autre texte qui gouverne ; même
chemin, autre empreinte), `table-comparee` (table_sha256 ≠ sceau de la table ; table qui cite un autre résultat de
réparation ; sceau de la table absent), `provenance` (addendum de la table ≠ ; commande du rejeu ≠) ; clé tokenisation
absente ; même calcul et même issue que le code v2 à entropie égale ; rejeu non validé ; mode décisif (texte qui gouverne
inchangé, exigé par chemin et empreinte ; addendum unique, bloc propre à l'analyse, liste fermée v6, constantes v6 ;
passages antérieurs du texte et manifestes des autres analyses sous l'addendum tolérés ; second passage refusé ;
manifeste illisible) ; liste fermée v6."""
import json
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v2 as K2
from controle_ia.analyse_principale_r1_r2 import constantes_v6 as K6
from controle_ia.analyse_principale_r1_r2 import entrees_v1 as EN
from controle_ia.analyse_principale_r1_r2 import entrees_v4 as EN4
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as LP
from controle_ia.analyse_principale_r1_r2 import lecture_v2 as LP2
from controle_ia.analyse_principale_r1_r2 import lecture_v6 as LP6
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, graines
from controle_ia.scellement import empreinte, sceller
from test_analyse_principale_r1_r2_v1 import D, RUN, _donnees, _ecrire_juge, _ecrire_p3, _npz

RACINE = Path(__file__).resolve().parents[1]
RUN_REJEU = "20261105-021737-r1-v4-rejeu-reel"
ADDENDUM_R1 = "prereg/R1-addendum-relance-v4.md"
SECTIONS = ["## Hypothèse", "h", "## Prédiction chiffrée et signe attendu", "p", "## Métrique", "m", "## Seuil", "s",
            "## Plan d'analyse", "a", "## Critères de lecture gelés", "c", "## Liste d'arrêt", "l",
            "## Contre-lecture", f"relu `{'a' * 64}`, rapport `{'b' * 64}`"]


@pytest.fixture(autouse=True)
def constantes_reduites(monkeypatch):
    for nom, v in (("DIMENSION", D), ("TIRAGES", 300), ("N_PLANCHER", 50), ("RUN_P3", RUN)):
        monkeypatch.setattr(K, nom, v)


# ------------------------------------------------------------------------------------------------ textes jouets
def _texte_jouet(depot, chemin, *lignes) -> str:
    """Préenregistrement jouet conforme (huit sections), scellé ; `lignes` en tête (empreintes des constantes, blocs de
    listes fermées) ; rend l'empreinte."""
    p = depot / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n\n".join(["# Préenregistrement jouet", *lignes, *SECTIONS]) + "\n", encoding="utf-8")
    return sceller(p)


def _bloc(titre, fichiers, alterer=False) -> str:
    lignes = [f"- `{c}` : `{empreinte(RACINE / c)}`" for c in fichiers]
    if alterer:
        lignes[-1] = lignes[-1][:-3] + ("0" if lignes[-1][-3] != "0" else "1") + lignes[-1][-2:]
    return "\n".join([titre, *lignes])


def _addendum_jouet(depot, chemin=K6.ADDENDUM, fichiers=None, alterer=False, constantes=None, blocs=()) -> str:
    """Addendum unique jouet : bloc de la principale (liste fermée v6, titre gelé), empreinte des constantes v6, et
    d'autres blocs (autres analyses) que le code de la principale ne doit pas lire."""
    fichiers = LP6.FICHIERS_PAQUET + LP6.FICHIERS_ESSAIS + LP6.FICHIERS_REUTILISES if fichiers is None else fichiers
    c = K6.empreinte_constantes() if constantes is None else constantes
    return _texte_jouet(depot, chemin, f"Empreinte des constantes (analyse principale, code v6) : `{c}`",
                        _bloc(K6.TITRE_LISTE, fichiers, alterer), *blocs)


# ------------------------------------------------------------------------------------------------ pièces de la relance v4
def _table_jouet(depot, sha_rep, chemin=K6.TABLE_V4) -> str:
    p = depot / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"version": 4, "regle_v4": "jouet", "table_v3_sha256": "0" * 64,
                             "resultat_reparation_sha256": sha_rep, "voie": "lot_fidele",
                             "temoin": {"chemin": "x", "sha256": "0" * 64, "lecture": "jouet"}, "comptes": {},
                             "corrections_verifiees": 0, "non_resolus_v4": [], "episodes": []},
                            sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return sceller(p)


def _pieces_v4(depot, monkeypatch, module=K6) -> dict:
    """Texte qui gouverne le rejeu jouet (sous le nom réel de l'addendum v4 ; son empreinte remplace celle gelée),
    résultat de réparation jouet scellé (jamais lu : haché), table v4 jouet scellée qui cite ce sceau."""
    sha_add = _texte_jouet(depot, ADDENDUM_R1, "addendum v4 jouet de R1")
    monkeypatch.setattr(module, "ADDENDUM_V4", {"chemin": ADDENDUM_R1, "sha256": sha_add})
    rep = depot / module.RESULTAT_REPARATION_V4
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text(json.dumps({"etape": "reparation", "version": "resolution_graine_lot_v3", "voie": "lot_fidele",
                               "episodes": []}) + "\n", encoding="utf-8")
    sha_rep = sceller(rep)
    return {"addendum": sha_add, "reparation": sha_rep, "table": _table_jouet(depot, sha_rep, module.TABLE_V4)}


def _ecrire_r1_v4(depot, d, sha_textes, sha_table, *, run=RUN_REJEU, prereg_run=ADDENDUM_R1,
                  commande=K6.COMMANDE_REJEU_V4, addendum_tok=ADDENDUM_R1, table_sha_tok=None, tokenisation=True,
                  fidele=None, contexte=None, repli=False, verdict="conforme"):
    """R1 au format du fournisseur pour la relance v4 : manifeste du rejeu décisif sous le texte `prereg_run`, commande
    du rejeu, résultat `rejeu-activations.json` rattaché, clé `tokenisation` (table_sha256, addendum)."""
    t = d["tables"]
    n = t["pas"].size
    ident = {k: t[k] for k in K.IDENTITE}
    notee = t["jetons_notes"] > 0
    fid = notee.copy() if fidele is None else fidele & notee
    ctx = np.ones(n, bool) if contexte is None else contexte
    commun = {**ident, "jetons_empan": t["jetons_notes"], "jetons_empan_rejeu": t["jetons_notes"],
              "couches": np.array(K.COUCHES), "conforme_longueur": notee, "contexte_conforme": ctx,
              "ecart_fidelite": np.where(notee, 0.0, np.nan), "fidele": fid, "trajectoire_identique": ctx,
              "activations_identiques": np.zeros(n, bool)}
    dd = depot / "donnees" / run
    fichiers, entree = {}, {}
    for cle, nom in K.FICHIERS_R1.items():
        fichiers[nom] = _npz(dd / nom, **{K.TABLEAU_R1[cle]: d["acts"][cle].astype(np.float16)}, **commun)
        entree[cle] = {"chemin": f"donnees/{run}/{nom}", "sha256": fichiers[nom]}
    m, _ = creer_manifeste(depot, run, {"mode": "jouet", "chemin_table_tokenisation": K6.TABLE_V4}, ["fidelite"],
                           entropie=12, decisif=True, prereg=depot / prereg_run, commande=commande,
                           autoriser_depot_sale=True)
    res = {"verdict_fidelite": verdict, "regle_repli_appliquee": repli, "lecture": "principale",
           "textes_sha256": sha_textes, "fichiers": fichiers, "identite_sha256": EN.empreinte_identite(t),
           "couches": list(K.COUCHES), "controle_negatif": {"lecture": "discriminant"},
           "fidelite_toutes": {"fideles": int(fid.sum()), "actions": n}}
    if tokenisation:
        res["tokenisation"] = {"version_table": 4, "table_sha256": sha_table if table_sha_tok is None else table_sha_tok,
                               "table_empreinte_citee": False, "addendum": addendum_tok, "non_conformes": 89,
                               "signales": 22}
    p = ecrire_resultat(depot, m, K.RESULTAT_R1, res)
    entree["resultat"] = {"chemin": str(p.relative_to(depot)), "sha256": empreinte(p)}
    return entree


def _source_v4(depot, monkeypatch, d, r1=True, r2=True, j8=True, fiche="fiche.json", r1_kw=None, j3_kw=None):
    sha = _ecrire_p3(depot, d)
    monkeypatch.setattr(K, "EMPREINTES_P3", sha)
    monkeypatch.setattr(K, "IDENTITE_SHA256", EN.empreinte_identite(d["tables"]))
    pieces = _pieces_v4(depot, monkeypatch)
    f = {"format": K.FORMAT_FICHE, "redaction": "essai synthétique", "R1": None, "motif_R1": None, "R2": None,
         "motif_R2": None}
    if r1:
        f["R1"] = _ecrire_r1_v4(depot, d, sha["textes"], pieces["table"], **(r1_kw or {}))
    else:
        f["motif_R1"] = "rejeu_non_conforme"
    if r2:
        f["R2"] = {"juge3b": _ecrire_juge(depot, d, "J3", **(j3_kw or {})),
                   "juge8b": _ecrire_juge(depot, d, "J8") if j8 else None, "motif_juge8b": None if j8 else "non_livre"}
    else:
        f["motif_R2"] = "sorties_non_livrees"
    (depot / fiche).write_text(json.dumps(f, ensure_ascii=False), encoding="utf-8")
    sceller(depot / fiche)
    return f, pieces


def _fiche(depot, f, nom):
    (depot / nom).write_text(json.dumps(f, ensure_ascii=False), encoding="utf-8")
    sceller(depot / nom)


# ------------------------------------------------------------------------------------------------ constantes, liste fermée
def test_constantes_v6_gelees_liste_fermee_et_bloc_de_l_addendum():
    assert K6.ADDENDUM_V4 == {"chemin": "prereg/R1-addendum-relance-v4.md",
                              "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"}
    assert K6.TEXTE == {"chemin": "prereg/analyse-principale-r1-r2-v1.md",
                        "sha256": "8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537"}
    assert empreinte(RACINE / K6.TEXTE["chemin"]) == K6.TEXTE["sha256"]                 # texte scellé, inchangé
    assert K6.COMMANDE_REJEU_V4 == "python -m controle_ia.runs_nuit.rejeu_activations_v4"
    assert K6.TABLE_V4 == "prereg/R1-table-tokenisation-v4.json"
    assert K6.RESULTAT_REPARATION_V4 == ("diag/20261104-234729-r1-v4-reparation-reel/"
                                         "resolution-graine-lot-v3-reparation.json")
    assert K6.ADDENDUM == "prereg/addendum-1-gardes-analyses-r1-v4-v1.md"
    assert K6.NOM_SORTIE == K2.NOM_SORTIE and LP6.issue is LP2.issue and K6.empreinte_constantes() != K2.empreinte_constantes()
    assert K6.constantes_courantes()["v1_v2"] == K2.constantes_courantes()
    for c in LP6.FICHIERS_PAQUET + LP6.FICHIERS_ESSAIS + LP6.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LP2.FICHIERS_PAQUET) < set(LP6.FICHIERS_PAQUET) and set(LP2.FICHIERS_ESSAIS) < set(LP6.FICHIERS_ESSAIS)
    assert len(set(LP6.FICHIERS_PAQUET) | set(LP6.FICHIERS_ESSAIS) | set(LP6.FICHIERS_REUTILISES)) == 22
    with pytest.raises(GardeArret, match="titre"):
        LP6.exiger_code_cite("rien")
    autre = "\n".join(["### Liste fermée du code — autre analyse", f"- `src/x.py` : `{'0' * 64}`"])
    texte = "\n\n".join(["# t", autre, K6.TITRE_LISTE, f"- `src/a.py` : `{'1' * 64}`", "## Hypothèse", "h"])
    bloc = LP6.liste_fermee_de(texte, K6.TITRE_LISTE)                                   # bloc propre à l'analyse
    assert "src/a.py" in bloc and "src/x.py" not in bloc and "Hypothèse" not in bloc
    with pytest.raises(GardeArret, match="titre"):
        LP6.liste_fermee_de(autre, K6.TITRE_LISTE)
    with pytest.raises(GardeArret, match="liste fermée"):                               # bloc présent, liste v2 seulement
        LP6.exiger_code_cite("\n\n".join(["# t", _bloc(K6.TITRE_LISTE, LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS
                                                      + LP2.FICHIERS_REUTILISES)]))


# ------------------------------------------------------------------------------------------------ gardes de réception
def test_reception_v4_cas_sain_et_artefacts(depot, monkeypatch):
    d = _donnees(21)
    f, pieces = _source_v4(depot, monkeypatch, d)
    sha_t = K.EMPREINTES_P3["textes"]
    r = EN4.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])                   # cas sain
    assert r["table"]["sha256"] == pieces["table"] and r["reparation"]["sha256"] == pieces["reparation"]
    assert r["texte"] == K6.ADDENDUM_V4 and r["commande"] == K6.COMMANDE_REJEU_V4 and r["run_rejeu"] == RUN_REJEU
    assert r["tokenisation"] == {"addendum": ADDENDUM_R1, "table_sha256": pieces["table"]}
    # texte : rejeu gouverné par un autre texte (addendum v3 jouet) ; même chemin, autre empreinte
    _texte_jouet(depot, "prereg/R1-addendum-relance-v3.md", "addendum v3 jouet de R1")
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-a", prereg_run="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="garde texte"):
        EN4.exiger_reception_v4(depot, e["resultat"]["chemin"])
    with monkeypatch.context() as mp:
        mp.setattr(K6, "ADDENDUM_V4", dict(K6.ADDENDUM_V4, sha256="0" * 64))
        with pytest.raises(GardeArret, match="garde texte"):
            EN4.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])
    # table-comparee : table_sha256 du rejeu ≠ sceau de la table v4 versée
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-b", table_sha_tok="0" * 64)
    with pytest.raises(GardeArret, match="table_sha256"):
        EN4.exiger_reception_v4(depot, e["resultat"]["chemin"])
    # table-comparee : la table cite un autre résultat de réparation que celui versé (résultat altéré, rescellé)
    rep = depot / K6.RESULTAT_REPARATION_V4
    comp = Path(str(rep) + ".sha256")
    octets, sceau = rep.read_bytes(), comp.read_text(encoding="utf-8")
    comp.unlink()
    rep.write_bytes(octets + b"\n")
    sceller(rep)
    with pytest.raises(GardeArret, match="resultat_reparation_sha256"):
        EN4.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])
    rep.write_bytes(octets)
    comp.write_text(sceau, encoding="utf-8")
    # table-comparee : sceau de la table absent (R11)
    comp_table = depot / (K6.TABLE_V4 + ".sha256")
    sceau_table = comp_table.read_text(encoding="utf-8")
    comp_table.unlink()
    with pytest.raises(GardeArret, match="empreinte compagnon"):
        EN4.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])
    comp_table.write_text(sceau_table, encoding="utf-8")
    assert EN4.exiger_reception_v4(depot, f["R1"]["resultat"]["chemin"])["table"]["sha256"] == pieces["table"]
    # provenance : addendum de la table ≠ addendum v4 ; commande du rejeu ≠ rejeu_activations_v4
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-c", addendum_tok="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="tokenisation.addendum"):
        EN4.exiger_reception_v4(depot, e["resultat"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-d",
                      commande="python -m controle_ia.runs_nuit.rejeu_activations_v3")
    with pytest.raises(GardeArret, match="commande du manifeste"):
        EN4.exiger_reception_v4(depot, e["resultat"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-e", tokenisation=False)
    with pytest.raises(GardeArret, match="sans clé tokenisation"):
        EN4.exiger_reception_v4(depot, e["resultat"]["chemin"])


# ------------------------------------------------------------------------------------------------ bout en bout
def test_v6_meme_calcul_que_v2_reception_ecrite_artefact_et_rejeu_non_valide(depot, monkeypatch):
    d = _donnees(22, w=3.0, j=0.5)
    f, pieces = _source_v4(depot, monkeypatch, d)
    with pytest.raises(GardeArret, match="entropie explicite"):
        LP6.analyser(depot, "fiche.json", "20261105-030000-x", None, autoriser_depot_sale=True)
    r6 = LP6.analyser(depot, "fiche.json", "20261105-030001-v6", None, entropie=K.entropie_racine(),
                      autoriser_depot_sale=True)
    r2 = LP2.analyser(depot, "fiche.json", "20261105-030002-v2", None, entropie=K.entropie_racine(),
                      autoriser_depot_sale=True)
    assert r6["calcul"] == r2["calcul"] and r6["issue"] == r2["issue"] and r6["version"] == K6.VERSION
    assert r6["reception_v4"]["table"]["sha256"] == pieces["table"] and r6["reception_v4"]["run_rejeu"] == RUN_REJEU
    corps = json.loads((depot / "diag" / "20261105-030001-v6" / f"{K6.NOM_SORTIE}.json").read_text(encoding="utf-8"))
    assert corps["resultat"]["reception_v4"] == r6["reception_v4"]
    assert (depot / "diag" / "20261105-030001-v6" / f"{K6.NOM_SORTIE}.md.sha256").exists()
    man = json.loads((depot / "runs" / "20261105-030001-v6" / "manifeste.json").read_text(encoding="utf-8"))
    assert man["commande"] == K6.COMMANDE and man["config"]["addendum"] is None and not man["decisif"]
    assert man["config"]["constantes_sha256"] == K6.empreinte_constantes()
    # artefact de bout en bout : provenance fausse → arrêt après le chargement de R1, avant le manifeste
    _fiche(depot, dict(f, R1=_ecrire_r1_v4(depot, d, K.EMPREINTES_P3["textes"], pieces["table"], run=RUN_REJEU + "-p",
                                           addendum_tok="prereg/R1-addendum-relance-v3.md")), "fiche-p.json")
    with pytest.raises(GardeArret, match="garde provenance"):
        LP6.analyser(depot, "fiche-p.json", "20261105-030003-x", None, entropie=K.entropie_racine(),
                     autoriser_depot_sale=True)
    assert not (depot / "runs" / "20261105-030003-x").exists()
    # rejeu non validé : rien n'est lu, aucune garde de réception
    _fiche(depot, {"format": K.FORMAT_FICHE, "redaction": "essai", "R1": None, "motif_R1": "rejeu_non_conforme",
                   "R2": None, "motif_R2": "sorties_non_livrees"}, "fiche-nv.json")
    r = LP6.analyser(depot, "fiche-nv.json", "20261105-030004-v6", None, entropie=K.entropie_racine(),
                     autoriser_depot_sale=True)
    assert r["mode"] == "rejeu non validé" and r["reception_v4"] is None and "calcul" not in r


# ------------------------------------------------------------------------------------------------ mode décisif
def test_mode_decisif_v6_texte_inchange_addendum_unique_et_passages(depot, monkeypatch):
    d = _donnees(15)
    f, pieces = _source_v4(depot, monkeypatch, d)
    monkeypatch.setattr(LP, "exiger_code_importe_sous", lambda r: None)          # vraie garde éprouvée en v1
    monkeypatch.setattr(K, "VERSIONS_EXIGEES", {k: v for k, v in LP.versions().items() if k in ("python", "numpy", "scipy")})
    # texte jouet qui gouverne (liste fermée v2, constantes v2) sous le nom réel ; le code v6 l'exige par chemin et empreinte
    f2 = LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS + LP2.FICHIERS_REUTILISES
    ligne_v2 = f"Empreinte des constantes (analyse principale, code v2) : `{K2.empreinte_constantes()}`"
    sha_t = _texte_jouet(depot, K6.TEXTE["chemin"], ligne_v2, _bloc("## Code", f2))
    monkeypatch.setattr(K6, "TEXTE", {"chemin": K6.TEXTE["chemin"], "sha256": sha_t})
    _texte_jouet(depot, "prereg/autre-texte.md", ligne_v2, _bloc("## Code", f2))     # même liste, autre texte : refusé
    # course v3 de R1 simulée : un passage décisif du texte sous le code v2 ne bloque pas le code v6
    creer_manifeste(depot, "20261103-072723-analyse-principale-r1-r2-v1", {"mode": "jouet"}, ["x"], entropie=1,
                    decisif=True, prereg=depot / K6.TEXTE["chemin"], commande=K2.COMMANDE, autoriser_depot_sale=True)
    # addendum unique jouet : bloc de la principale (liste v6) et bloc d'une autre analyse (non lu par la principale)
    autre = _bloc("### Liste fermée du code — analyse par épisode (code v7)",
                  LP6.FICHIERS_PAQUET + ("src/controle_ia/analyse_principale_r1_r2/lecture_v7.py",))
    sha_a = _addendum_jouet(depot, blocs=(autre,))
    _addendum_jouet(depot, "prereg/add-altere.md", alterer=True)
    _addendum_jouet(depot, "prereg/add-v2.md", fichiers=f2)
    # un manifeste d'une autre analyse sous l'addendum (autre commande) ne bloque pas non plus
    creer_manifeste(depot, "20261105-040000-analyse-par-episode-v1", {"addendum": {"chemin": K6.ADDENDUM, "sha256": sha_a}},
                    ["x"], entropie=2, decisif=True, prereg=depot / K6.TEXTE["chemin"],
                    commande="python -m controle_ia.analyse_principale_r1_r2.lecture_v7", autoriser_depot_sale=True)
    committer(depot)
    with pytest.raises(GardeArret, match="texte passé"):
        LP6.analyser(depot, "fiche.json", "20261105-041001-x", "prereg/autre-texte.md")
    with pytest.raises(GardeArret, match="empreinte citée"):
        LP6.exiger_code_cite((depot / "prereg/add-altere.md").read_text(encoding="utf-8"))
    with pytest.raises(GardeArret, match="liste fermée"):
        LP6.exiger_code_cite((depot / "prereg/add-v2.md").read_text(encoding="utf-8"))
    with pytest.raises(GardeArret, match="entropie"):
        LP6.analyser(depot, "fiche.json", "20261105-041002-x", K6.TEXTE["chemin"], entropie=5)
    r = LP6.analyser(depot, "fiche.json", "20261105-041003-analyse-principale-r1-r2-v1", K6.TEXTE["chemin"])
    assert r["statut"] == "décisif" and int(r["entropie"]) == K2.entropie_de(sha_t)   # graines du texte, inchangées
    lien = r["lien_au_preenregistrement"]
    assert lien["sha256"] == sha_t and lien["addendum"]["chemin"] == K6.ADDENDUM and lien["addendum"]["sha256"] == sha_a
    assert set(lien["addendum"]["code_cite"]["fichiers"]) == set(LP6.FICHIERS_PAQUET + LP6.FICHIERS_ESSAIS
                                                                 + LP6.FICHIERS_REUTILISES)
    assert lien["passages"] == {"manifestes_lus": 6, "autres_analyses_sous_l_addendum": 1,
                                "passages_anterieurs_du_texte_hors_addendum": 1}
    assert r["reception_v4"]["table"]["sha256"] == pieces["table"]
    man = json.loads((depot / "runs" / "20261105-041003-analyse-principale-r1-r2-v1" / "manifeste.json")
                     .read_text(encoding="utf-8"))
    assert man["decisif"] and man["preenregistrement"] == {"chemin": K6.TEXTE["chemin"], "sha256": sha_t}
    assert man["commande"] == K6.COMMANDE and man["config"]["addendum"] == {"chemin": K6.ADDENDUM, "sha256": sha_a}
    ref = graines(list(K.CLES_GRAINES), K2.entropie_de(sha_t))
    assert all(man["graines"][k] == ref[k] for k in K.CLES_GRAINES)
    committer(depot)
    with pytest.raises(GardeArret, match="second passage"):
        LP6.analyser(depot, "fiche.json", "20261105-041004-x", K6.TEXTE["chemin"])
    assert LP6.exiger_premier_passage_sous(depot, K6.ADDENDUM, sha_a, "autre commande", sha_t)["autres_analyses_sous_l_addendum"] == 2
    (depot / "runs" / "20261105-041005-illisible").mkdir()
    (depot / "runs" / "20261105-041005-illisible" / "manifeste.json").write_text("{{" + K6.ADDENDUM, encoding="utf-8")
    with pytest.raises(GardeArret, match="illisible"):
        LP6.exiger_premier_passage_sous(depot, K6.ADDENDUM, sha_a, "autre commande", sha_t)
    monkeypatch.setattr(K6, "TABLE_V4", "prereg/autre-table.json")                 # constantes ≠ empreinte citée
    with pytest.raises(GardeArret, match="constantes gelées"):
        LP6.exiger_code_cite((depot / K6.ADDENDUM).read_text(encoding="utf-8"))
