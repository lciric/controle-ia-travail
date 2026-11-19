"""Essais de procédure et de bout en bout (texte scellé, « Code neuf », essais « procédure ») : horloge au-delà de 8 h,
disque, aucune occurrence de la valeur d'une fausse clé, refus de `registres/scellements-v1.md`, une phrase par libellé, bout
en bout sur le Llama miniature et la fausse lentille."""
from __future__ import annotations

import json
from collections import namedtuple

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import audits_v1 as au  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v1 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis import phrases_v1 as ph  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v1 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, Refus  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

Disque = namedtuple("Disque", "total used free")


# --- horloge ----------------------------------------------------------------------------------------------------------------------------
def test_horloge_saine_puis_au_dela_de_8_h_arret(tmp_path):
    t = [0.0]
    h = la.Horloge(tmp_path, maintenant=lambda: t[0])
    t[0] = 8 * 3600 - 1
    h.controler("juste avant")
    t[0] = 8 * 3600 + 1
    with pytest.raises(Arret, match="au-delà de 8 h"):
        h.controler("juste après")


def test_horloge_cumulee_entre_le_montage_et_le_calcul(tmp_path):
    t = [100.0]
    montage = la.Horloge(tmp_path, maintenant=lambda: t[0])
    t[0] += 5 * 3600
    montage.controler("montage")
    t[0] = 0.0                                             # autre processus, autre origine du temps
    calcul = la.Horloge(tmp_path, maintenant=lambda: t[0])
    assert calcul.ecoule() == pytest.approx(5 * 3600)
    t[0] = 2 * 3600
    calcul.controler("calcul")
    t[0] = 3 * 3600 + 1
    with pytest.raises(Arret, match="au-delà de 8 h"):
        calcul.controler("calcul")


# --- disque -----------------------------------------------------------------------------------------------------------------------------
def test_disque_seuils_simules(tmp_path):
    assert la.exiger_disque(tmp_path, K.DISQUE_DEPART_OCTETS, "au départ", lambda p: Disque(0, 0, 6 * 10 ** 9)) == 6 * 10 ** 9
    with pytest.raises(Arret, match="6 Go exigés"):
        la.exiger_disque(tmp_path, K.DISQUE_DEPART_OCTETS, "au départ", lambda p: Disque(0, 0, 6 * 10 ** 9 - 1))
    la.exiger_disque(tmp_path, K.DISQUE_CALCUL_OCTETS, "pendant le calcul", lambda p: Disque(0, 0, 10 ** 9))
    with pytest.raises(Arret, match="1 Go exigés"):
        la.exiger_disque(tmp_path, K.DISQUE_CALCUL_OCTETS, "pendant le calcul", lambda p: Disque(0, 0, 10 ** 9 - 1))


def test_montage_moins_de_6_go_au_depart_arret_sans_rien_creer(tmp_path):
    m = J.monde(tmp_path)
    m.reglages.disque_depart = K.DISQUE_DEPART_OCTETS
    m.ctx.mesure_disque = lambda p: Disque(0, 0, 5 * 10 ** 9)
    with pytest.raises(Arret, match="6 Go exigés"):
        la.monter(m.ctx)
    assert not (tmp_path / "travail").exists() and m.transport.appels == []


# --- clé : aucune occurrence dans les fichiers écrits -------------------------------------------------------------------------------------
def test_aucune_occurrence_de_la_cle_sain_et_artefact(tmp_path):
    cle = mo.Cle(J.FAUSSE_CLE)
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "propre.json").write_text('{"cle": "<clé d\'accès masquée>"}')
    mo.aucune_occurrence([tmp_path], cle)
    (tmp_path / "a" / "journal.txt").write_bytes(b"x" * (mo.BLOC - 10) + J.FAUSSE_CLE.encode() + b"suite")   # à cheval sur deux blocs
    with pytest.raises(Arret, match="clé d'accès écrite dans un fichier") as e:
        mo.aucune_occurrence([tmp_path], cle)
    assert J.FAUSSE_CLE not in str(e.value)


# --- registres ----------------------------------------------------------------------------------------------------------------------------
def test_ligne_de_registre_saine_dans_le_registre_propre(tmp_path):
    _, propre = J.ecrire_registres(tmp_path)
    avant = propre.read_text(encoding="utf-8")
    ligne = la.inscrire_ligne(propre, "MONTAGE-LENTILLES-BBIS", "diag/x/montage-lentilles-bbis.json", "a" * 64, J.HEURE)
    assert ligne == f"| MONTAGE-LENTILLES-BBIS | {J.HEURE} | diag/x/montage-lentilles-bbis.json | {'a' * 64} |"
    assert propre.read_text(encoding="utf-8") == avant + ligne + "\n"                  # ajoutée, rien de réécrit


def test_cle_de_ce_texte_dans_scellements_v1_refus(tmp_path):
    interdit = tmp_path / "scellements-v1.md"
    interdit.write_text("| T07-SCELLEMENT | x | y | z |\n")
    with pytest.raises(Refus, match="scellements-v1.md"):
        la.inscrire_ligne(interdit, "TABLES-LENTILLES-BBIS", "diag/x/tables-lentilles-bbis.json", "a" * 64)
    assert interdit.read_text() == "| T07-SCELLEMENT | x | y | z |\n"
    _, propre = J.ecrire_registres(tmp_path / "r")
    for cle in ("VERDICT-BBIS", "SCORES-BBIS", "CLE-INCONNUE"):
        with pytest.raises(Refus, match="hors des clés de ce texte"):
            la.inscrire_ligne(propre, cle, "x", "a" * 64)
    with pytest.raises(Refus):
        la.inscrire_ligne(tmp_path / "r" / "t07-etape-b-bis-v1.md", "TABLES-LENTILLES-BBIS", "x", "a" * 64)


# --- phrases : une par libellé --------------------------------------------------------------------------------------------------------------
NOM = ph.nom_sonde("P-S25", "e0", "sonde", "w")


def test_phrase_de_tete_toujours_ecrite():
    tete = ph.phrase_de_tete()
    assert tete.startswith("Lecture descriptive, par la lentille publique côté sortie (lentille R de Llama 3.1 8B Instruct publiée par "
                           "Neuronpedia, ajustée par un tiers sur 64 textes de WikiText)")
    assert "Ce n'est pas notre lentille ajustée." in tete and "non ce que la sonde lit" in tete
    assert "Verdict d'ensemble de la tranche des lentilles publiques sur cette lentille" in tete and "Indépendance" not in tete
    avec = ph.phrase_de_tete([(7, K.LENTILLE_LOGITS), (7, K.LENTILLE_PUBLIQUE)])
    assert avec.endswith("Indépendance à la norme non tenue à couche 7 (la lentille des logits), couche 7 (la lentille publique côté "
                         "sortie) : nuls isotropes refaits par direction.")


def test_phrase_concentree():
    p = ph.phrase_direction(K.LENTILLE_PUBLIQUE, NOM, 15, "+", st.LIBELLE_CONCENTREE, 7.25, 0.0005, 0.004, [" cost", "12"])
    assert p == ("Par la lentille publique côté sortie, la direction de la sonde apprise sur l'adaptateur saboteur à la dose 0,25, pli "
                 "e0 (vecteur de score) (couche 15, signe +) se distingue des deux nuls (concentration 7,25 ; p 0,0005 et 0,004) ; ses "
                 "premiers jetons : ' cost', '12'.")


def test_phrase_intermediaire_et_non_distincte_ne_nomment_aucun_jeton():
    for libelle, morceau in ((st.LIBELLE_INTERMEDIAIRE, "ne se distingue des nuls qu'en partie (p 0,02 et 0,03) : ses premiers jetons "
                              "sont rapportés, sans être nommés comme ce qu'elle capte."),
                             (st.LIBELLE_NON_DISTINCTE, "ne se distingue pas du nul (p 0,02 et 0,03) : ses jetons sont en table, et "
                              "aucune phrase ne les nomme comme ce qu'elle capte.")):
        p = ph.phrase_direction(K.LENTILLE_LOGITS, NOM, 7, "-", libelle, 3.0, 0.02, 0.03, ["JETON-SECRET"])
        assert p.endswith(morceau) and "JETON-SECRET" not in p and p.startswith("Par la lentille des logits, la direction de")
    with pytest.raises(Arret):
        ph.phrase_direction(K.LENTILLE_LOGITS, NOM, 7, "-", "autre libellé", 3.0, 0.02, 0.03, [])


def test_phrases_des_familles():
    sur = ph.phrase_famille("nombres", 6, 0.4, 0.001, 0.002, True)
    assert sur == ("La famille nombres paraît 6 fois dans ses vingt premiers jetons (attendu sous le nul 0,4 ; p 0,001 et 0,002) : la "
                   "lecture ajoute un soupçon que la sonde lise des nombres ; elle ne le prouve pas.")
    assert "soupçon que la sonde lise le coût" in ph.phrase_famille("cout", 3, 0.1, 0.001, 0.002, True)
    non = ph.phrase_famille("cout", 1, 0.1, 0.2, 0.3, False)
    assert non == "La famille coût n'y est pas sur-représentée (1 ; p 0,2 et 0,3) : cela ne blanchit pas la sonde." and "soupçon" not in non


def test_phrases_des_poles():
    poles = [{"neurone": 12, "signe": "+", "cosinus": 0.31}, {"neurone": 7, "signe": "-", "cosinus": 0.25}]
    p = ph.phrase_poles(st.LIBELLE_CONCENTREE, poles, 0.0005, 0.005, [[" a", " b"], [" c"]])
    assert p == ("Les pôles qui écrivent le plus près de la direction (neurone 12 signe +, neurone 7 signe -, cosinus 0,31, 0,25) se "
                 "distinguent des nuls (p 0,0005 et 0,005) ; la lentille publique les lit : neurone 12 signe + : ' a', ' b' ; neurone 7 "
                 "signe - : ' c'.")
    assert ph.phrase_poles(st.LIBELLE_NON_DISTINCTE, poles, 0.3, 0.4, [[], []]) == (
        "Aucun pôle de la couche n'écrit plus près de la direction que sous le nul (p 0,3 et 0,4).")
    assert ph.phrase_poles(st.LIBELLE_INTERMEDIAIRE, poles, 0.02, 0.03, [[], []]) is None     # aucune phrase gelée pour ce cas


def test_phrases_de_comparaison_et_de_non_lecture():
    autre = ph.nom_sonde("P-S25", "e0", "enc", "w")
    assert ph.phrase_comparaison(NOM, autre, 0.42, 3) == (
        f"Cosinus 0,42 entre {NOM} et {autre} (même couche) ; 3 jetons communs sur vingt.")
    assert ph.phrase_comparaison(NOM, autre, None, None) == "couches différentes : sans objet"
    assert ph.phrase_non_lue("échec à l'apprentissage") == "Non lue : échec à l'apprentissage."
    assert ph.phrase_non_lue(ph.MOTIF_SANS_LENTILLE_ENTREE) == "Non lue : aucune lentille côté entrée publique."


def test_regles_des_phrases_mots_interdits():
    """Aucune phrase ne dit « lit » d'une sonde hors de la phrase du soupçon, ni « nos lentilles », ni « détecte »."""
    phrases = [ph.phrase_direction(l, NOM, 15, "+", lib, 5.0, 0.0005, 0.004, [" x"]) for l in K.LENTILLES
               for lib in (st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, st.LIBELLE_NON_DISTINCTE)]
    phrases += [ph.phrase_famille("cout", 1, 0.1, 0.2, 0.3, False), ph.phrase_comparaison(NOM, NOM, 0.1, 1),
                ph.phrase_poles(st.LIBELLE_NON_DISTINCTE, [], 0.3, 0.4, [])]
    for p in phrases:
        assert "soupçon" not in p and "nos lentilles" not in p and "notre lentille" not in p and "détecte" not in p
        assert "sonde lit" not in p and "sonde lise" not in p and "état saboteur" not in p and "aire" not in p.split()


# --- étiquetage : calibration hors de ses bornes ---------------------------------------------------------------------------------------------
def test_calibration_hors_bornes_tables_non_calculables_sans_arret():
    def nul(p):
        return {"p_concentration": p, "p_part": p, "familles": {"nombres": {"p": p, "n": 0, "attendu": 0.1}}}

    def direction(couche):
        signes = {s: {"premiers_par_score": {"ids": [5, 6]}, "familles": {"nombres": {"n": 0}},
                      "nuls": {K.NUL_ISOTROPE: nul(0.0005), K.NUL_SIGNES: nul(0.0005)}} for s in ("+", "-")}
        return {"sonde": "P-S25/e0/sonde", "role": "sonde", "vecteur": "w", "couche": couche,
                "lectures": {l: {"signes": json.loads(json.dumps(signes))} for l in K.LENTILLES},
                "poles": {"p": {K.NUL_ISOTROPE: 0.5, K.NUL_SIGNES: 0.5}}}
    tenue, hors = {"tenue": True}, {"tenue": False}
    couches = {"7": {"repli_nuls_par_direction": False, "lentilles": {
        K.LENTILLE_PUBLIQUE: {"calibration": {K.NUL_ISOTROPE: tenue, K.NUL_SIGNES: hors}},
        K.LENTILLE_LOGITS: {"calibration": {K.NUL_ISOTROPE: tenue, K.NUL_SIGNES: tenue}}}}}
    d = direction(7)
    lignes = la._etiqueter([d], couches, ["a", "b"], np.array([5, 6]))
    publique, logits = d["lectures"][K.LENTILLE_PUBLIQUE]["signes"]["+"], d["lectures"][K.LENTILLE_LOGITS]["signes"]["+"]
    assert publique["libelle"] is None and publique["non_calculable"] == au.MOTIF_CALIBRATION
    assert publique["nuls"][K.NUL_SIGNES] == {"non_calculable": au.MOTIF_CALIBRATION} and "p_concentration" in publique["nuls"][K.NUL_ISOTROPE]
    assert logits["libelle"] == st.LIBELLE_CONCENTREE and logits["familles"]["nombres"]["sur_representee"] is True
    assert [l["libelle"] for l in lignes if l["lentille"] == K.LENTILLE_PUBLIQUE] == [None, None]


# --- morceaux de moins de 95 Mo ----------------------------------------------------------------------------------------------------------------
def test_morceaux_numerotes_sous_la_limite_et_scelles(tmp_path):
    tableaux = {f"t{i}": np.full(1000, i, dtype=np.float32) for i in range(10)}
    morceaux = la.ecrire_morceaux(tableaux, tmp_path / "donnees" / "lectures-lentilles-bbis", limite=20_000)
    assert len(morceaux) == 4 and [len(m["tableaux"]) for m in morceaux] == [3, 3, 3, 1] and [m["fichier"] for m in morceaux][:2] == ["lectures-lentilles-bbis-000.npz", "lectures-lentilles-bbis-001.npz"]
    relus = {}
    for m in morceaux:
        p = tmp_path / "donnees" / m["fichier"]
        assert p.stat().st_size < 20_000 and verifier(p) == m["sha256"]
        relus |= dict(np.load(p))
    assert sorted(relus) == sorted(tableaux) and all(np.array_equal(relus[k], tableaux[k]) for k in tableaux)
    with pytest.raises(Arret, match="trop grand"):
        la.ecrire_morceaux({"gros": np.zeros(10_000, dtype=np.float32)}, tmp_path / "x" / "l", limite=20_000)
    with pytest.raises(Arret, match="existe déjà"):
        la.ecrire_morceaux(tableaux, tmp_path / "donnees" / "lectures-lentilles-bbis", limite=20_000)


def test_nettoyage_refuse_un_dossier_sans_la_marque(tmp_path):
    (tmp_path / "autre").mkdir()
    (tmp_path / "autre" / "precieux.txt").write_text("à garder")
    with pytest.raises(Arret, match="rien n'est supprimé"):
        la.nettoyer(tmp_path / "autre")
    assert (tmp_path / "autre" / "precieux.txt").exists()
    (tmp_path / "autre" / la.MARQUE).write_text("x")
    la.nettoyer(tmp_path / "autre")
    assert not (tmp_path / "autre").exists()


# --- bout en bout sur le Llama miniature et la fausse lentille -----------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def bout_en_bout(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("bout-en-bout")
    m = J.monde(tmp, formes={("P-S25", "e1"): "a", ("P-S50", "e0"): "b"}, echelles={("P-S75", "e1", "sonde"): 1e-5})
    montage = la.monter(m.ctx)
    charge = la.charger_montage(m.ctx)
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis)
    tables = json.loads((tmp / "sortie" / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    return {"m": m, "tmp": tmp, "montage": montage, "rendu": rendu, "tables": tables, "charge": charge}


def test_bout_en_bout_fichiers_fermes_scelles_et_nettoyage(bout_en_bout):
    tmp, rendu = bout_en_bout["tmp"], bout_en_bout["rendu"]
    for relatif in (f"diag/{J.RUN}/montage-lentilles-bbis.json", rendu["tables"]["chemin"], rendu["manifeste"]["chemin"]):
        verifier(tmp / "sortie" / relatif)
    for morceau in rendu["morceaux"]:
        assert verifier(tmp / "sortie" / "donnees" / J.RUN / morceau["fichier"]) == morceau["sha256"]
    assert not (tmp / "travail").exists()                                        # plan, point 10 : dossier de travail supprimé
    assert (tmp / "entrees").exists() and (tmp / "llama").exists()               # rien d'autre n'est supprimé
    assert [l.split(" | ")[0] for l in rendu["lignes_proposees"]] == ["| ENTREES-LENTILLES-BBIS", "| TABLES-LENTILLES-BBIS"]
    for p in (tmp / "sortie").rglob("*"):
        if p.is_file():
            assert J.FAUSSE_CLE.encode() not in p.read_bytes(), p


def test_bout_en_bout_sondes_lues_et_non_lues(bout_en_bout):
    tables = bout_en_bout["tables"]
    assert len(tables["sondes"]) == 20
    motifs = {s["cle"]: s["motif"] for s in tables["sondes"] if not s["lue"]}
    assert motifs == {"P-S25/e1/sonde": "non lue : échec à l'apprentissage",
                      "P-S25/e1/enc": "non lue : non appris, la sonde apprise ayant échoué",
                      "P-S50/e0/enc": "non lue : échec à l'apprentissage"}
    attendu = sum(1 + (s.q is not None) for s in bout_en_bout["m"].sondes.objets.values())
    assert len(tables["directions"]) == attendu == 21
    assert tables["comptes_de_libelles"]["nombre_total_de_lectures"] == attendu * 2 * 2
    assert tables["lecture_cote_entree"] == "non lue : aucune lentille côté entrée publique"
    assert tables["entrees"]["entrees_jamais_decodees"] and all("direction" in n for n in tables["entrees"]["entrees_jamais_decodees"])
    assert all("direction" not in n for n in tables["entrees"]["entrees_decodees"])


def test_bout_en_bout_aucune_regularisation_ni_champ_exclu_dans_les_sorties(bout_en_bout):
    tmp = bout_en_bout["tmp"]
    for p in (tmp / "sortie").rglob("*.json"):
        texte = p.read_text(encoding="utf-8")
        for interdit in ("l2_", "taches_lues", "ordre2", "plis_internes", "motif jamais lu", "perte non finie", "n_plancher"):
            assert interdit not in texte, (p.name, interdit)
    noms = [n for m in bout_en_bout["rendu"]["morceaux"] for n in m["tableaux"]]
    assert noms and not any("direction0" in n or "direction1" in n for n in noms)


def test_bout_en_bout_lecture_egale_a_un_calcul_direct_et_indice_de_couche(bout_en_bout):
    tmp, tables, charge = bout_en_bout["tmp"], bout_en_bout["tables"], bout_en_bout["charge"]
    tableaux = {}
    for m in bout_en_bout["rendu"]["morceaux"]:
        tableaux |= dict(np.load(tmp / "sortie" / "donnees" / J.RUN / m["fichier"]))
    assert np.array_equal(tableaux["ids_gardes"], np.array(bout_en_bout["m"].gardes))
    for d in tables["directions"]:
        s = bout_en_bout["m"].sondes.objets[(d["cellule"], d["pli"], d["role"])]
        v = np.asarray(getattr(s, d["vecteur"]), np.float32)
        assert d["couche"] == s.couche
        publique = d["lectures"][K.LENTILLE_PUBLIQUE]
        assert publique["indice_matrice"] == s.couche
        assert publique["empreinte_matrice"] == le.empreinte_matrice(charge.publique.matrices[s.couche])
        for lentille, j in ((K.LENTILLE_PUBLIQUE, charge.publique.matrices[s.couche].astype(np.float64)), (K.LENTILLE_LOGITS, None)):
            relue = au.relire_par_chemin_independant(v, j, charge.gamma.numpy(), charge.wu.numpy())
            ident = f"{d['cellule']}__{d['pli']}__{d['role']}__{d['vecteur']}__{lentille}"
            accord = au.comparer_relecture(tableaux[f"scores__{ident}"], relue)
            assert accord["ecart_relatif_maximal"] < 1e-4, ident
            plus, moins = d["lectures"][lentille]["signes"]["+"], d["lectures"][lentille]["signes"]["-"]
            ids = charge.ids_gardes
            assert plus["premiers_par_score"]["ids"] == ids[np.argsort(-tableaux[f"scores__{ident}"], kind="stable")[:20]].tolist()
            assert moins["premiers_par_score"]["ids"] == ids[np.argsort(tableaux[f"scores__{ident}"], kind="stable")[:20]].tolist()
            assert set(plus["nuls"]) >= {K.NUL_ISOTROPE, K.NUL_SIGNES} and plus["libelle"] in (
                st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, st.LIBELLE_NON_DISTINCTE, None)
        assert len(d["poles"]["poles"]) == 10 and all(len(p["lecture_publique"]["ids"]) == 10 for p in d["poles"]["poles"])
        for lentille in K.LENTILLES:
            t = d["lectures"][lentille]["signes"]["+"]
            chaines = dict(zip(charge.ids_gardes.tolist(), charge.chaines))
            assert t["premiers_par_score"]["chaines_echappees"] == [json.dumps(chaines[i])[1:-1] for i in t["premiers_par_score"]["ids"]]
            par_z = t["nuls"][t["nul_isotrope_en_vigueur"]]["premiers_par_z"]
            assert len(par_z["chaines_echappees"]) == len(par_z["ids"]) == 20
        assert set(publique["temoin_de_couche"]) == {str(c) for c in K.COUCHES if c != s.couche}


def test_bout_en_bout_garde_du_rapport_a_epsilon_et_repli(bout_en_bout):
    """La sonde de norme 10⁻⁵ (couche 7) lève la garde : nuls isotropes refaits par direction pour les deux lentilles de la
    couche 7 ; les couches 15 et 23 gardent le nul partagé."""
    tables = bout_en_bout["tables"]
    assert tables["independance_a_la_norme_non_tenue"] == [{"couche": 7, "lentille": l} for l in sorted(K.LENTILLES)]
    for couche, info in tables["couches"].items():
        assert info["repli_nuls_par_direction"] is (couche == "7") and info["independance_a_la_norme_tenue"] is (couche != "7")
        for lentille in K.LENTILLES:
            cal = info["lentilles"][lentille]["calibration"]
            assert (K.NUL_ISOTROPE_PAR_DIRECTION in cal) is (couche == "7") and cal[K.NUL_ISOTROPE]["n"] == 400
            if couche == "7":
                assert cal[K.NUL_ISOTROPE_PAR_DIRECTION]["n"] == 100 * info["directions"]
    for d in tables["directions"]:
        for lentille in K.LENTILLES:
            t = d["lectures"][lentille]["signes"]["+"]
            if d["couche"] == 7:
                assert t["nul_isotrope_en_vigueur"] == K.NUL_ISOTROPE_PAR_DIRECTION and t["nuls"][K.NUL_ISOTROPE]["remplacee"] is True
                assert K.NUL_ISOTROPE_PAR_DIRECTION in d["poles"]["p"] and K.NUL_ISOTROPE not in d["poles"]["p"]
            else:
                assert t["nul_isotrope_en_vigueur"] == K.NUL_ISOTROPE and "remplacee" not in t["nuls"][K.NUL_ISOTROPE]
    assert "nuls isotropes refaits par direction" in la.rendre_phrases(tables)["tete"]


def test_bout_en_bout_comparaisons_et_phrases(bout_en_bout):
    tables = bout_en_bout["tables"]
    types = {c["type"] for c in tables["comparaisons"]}
    assert types == {"sonde-lecteur", "plis", "doses"}
    for c in tables["comparaisons"]:
        if c["couche_a"] != c["couche_b"]:
            assert c["cosinus"] is None and c["sans_objet"] == "couches différentes : sans objet"
        else:
            assert -1 <= c["cosinus"] <= 1 and set(c["jetons_communs"]) == set(K.LENTILLES)
    phrases = la.rendre_phrases(tables)
    assert len(phrases["non_lues"]) == 3 and phrases["lecture_cote_entree"] == "Non lue : aucune lentille côté entrée publique."
    lectures = [l for l in phrases["directions"] if not l.get("poles")]
    assert len(lectures) == tables["comptes_de_libelles"]["nombre_total_de_lectures"] and all(len(l["phrases"]) in (1, 3) for l in lectures)
    assert any(c["phrase"] == "couches différentes : sans objet" for c in phrases["comparaisons"])
    texte = json.dumps(phrases, ensure_ascii=False)
    assert "nos lentilles" not in texte and "détecte" not in texte


def test_bout_en_bout_manifeste_graines_et_reproductibilite(bout_en_bout):
    tmp = bout_en_bout["tmp"]
    manifeste = json.loads((tmp / "sortie" / "runs" / J.RUN / "manifeste.json").read_text(encoding="utf-8"))
    graines = manifeste["graines"]
    assert all(g["entropie"] == str(K.ENTROPIE) for g in graines.values())
    assert "lentilles-bbis/nul-isotrope/15" in graines and "lentilles-bbis/temoins-calibration/23/nul-isotrope/couche" in graines
    assert "lentilles-bbis/nul-signes/P-instruit/e1/sonde/q" in graines
    assert "lentilles-bbis/nul-isotrope-par-direction/P-S75/e1/sonde/w" in graines
    assert not any(k.startswith("lentilles-bbis/nul-isotrope-par-direction/P-S25/e0") for k in graines)   # couche 15 : pas de repli
    assert manifeste["preenregistrement"]["sha256"] == K.EMPREINTE_TEXTE and set(manifeste["code"]) == {f"{m}.py" for m in la.MODULES}
    # même monde rejoué ailleurs : mêmes tables, aux durées et empreintes de fichiers près
    autre = J.monde(tmp / "rejeu", formes={("P-S25", "e1"): "a", ("P-S50", "e0"): "b"}, echelles={("P-S75", "e1", "sonde"): 1e-5})
    la.monter(autre.ctx)
    rendu = la.calculer(autre.ctx, autre.entrees, autre.registre_bbis)
    rejouees = json.loads((tmp / "rejeu" / "sortie" / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    for cle in ("directions", "comparaisons", "comptes_de_libelles", "couches", "declencheurs_d_audit"):
        assert rejouees[cle] == bout_en_bout["tables"][cle], cle


# --- refus et arrêts du calcul --------------------------------------------------------------------------------------------------------------------
@pytest.fixture()
def monte(tmp_path):
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    return m


def test_calcul_refuse_avant_verdict_bbis_sans_ouvrir_les_sondes(monte, monkeypatch):
    bbis, _ = J.ecrire_registres(monte.tmp / "sans-verdict", monte.sondes.sha_e2, verdict=False)
    ouvertures = []
    monkeypatch.setattr(la.en, "ouvrir_entrees", lambda *a, **k: ouvertures.append(a))
    with pytest.raises(Refus, match="VERDICT-BBIS absente"):
        la.calculer(monte.ctx, monte.entrees, bbis)
    assert ouvertures == [] and not (monte.tmp / "sortie" / "diag" / J.RUN / "tables-lentilles-bbis.json").exists()
    assert (monte.tmp / "travail").exists()


def test_calcul_sans_les_cles_du_registre_propre_refus(monte):
    _, propre = J.ecrire_registres(monte.tmp / "sans-code", propres=("SCELLEMENT-LENTILLES-BBIS", "GO-LENTILLES-BBIS"))
    monte.ctx.registre_propre = propre
    with pytest.raises(Refus, match="CODE-LENTILLES-BBIS"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)


def test_montage_sans_les_cles_du_registre_propre_refus(tmp_path):
    m = J.monde(tmp_path)
    _, m.ctx.registre_propre = J.ecrire_registres(tmp_path / "sans-go", propres=("SCELLEMENT-LENTILLES-BBIS", "CODE-LENTILLES-BBIS"))
    with pytest.raises(Refus, match="GO-LENTILLES-BBIS"):
        la.monter(m.ctx)
    assert m.transport.appels == []


def test_calcul_lentille_absente_arret_sans_lecture_par_les_seuls_logits(monte):
    (monte.tmp / "travail" / "lentille" / "J-15.npy").unlink()
    with pytest.raises(Arret, match="la lecture par la seule lentille des logits n'est pas rendue"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)
    assert not (monte.tmp / "sortie" / "donnees").exists() and not (monte.tmp / "sortie" / "runs").exists()


def test_calcul_matrice_d_un_autre_indice_arret(monte):
    lentille = monte.tmp / "travail" / "lentille"
    (lentille / "J-7.npy").rename(lentille / "tmp.npy")
    (lentille / "J-15.npy").rename(lentille / "J-7.npy")
    (lentille / "tmp.npy").rename(lentille / "J-15.npy")
    with pytest.raises(Arret, match="autre indice que la couche"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)
    assert not (monte.tmp / "sortie" / "diag" / J.RUN / "tables-lentilles-bbis.json").exists()


def test_calcul_horloge_au_dela_de_8_h_arret(monte):
    (monte.tmp / "travail" / "horloge.json").write_text(json.dumps({"cumul_s": 8 * 3600 + 5}))
    with pytest.raises(Arret, match="au-delà de 8 h"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)
    assert (monte.tmp / "travail").exists()                                # rien n'est supprimé : ce qui existe se verse


def test_calcul_moins_de_1_go_arret_sans_rien_supprimer(monte):
    monte.reglages.disque_calcul = K.DISQUE_CALCUL_OCTETS
    monte.ctx.mesure_disque = lambda p: Disque(0, 0, 10 ** 9 - 1)
    with pytest.raises(Arret, match="1 Go exigés"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)
    assert (monte.tmp / "travail" / "tenseurs").exists()


def test_calcul_jetons_gardes_alteres_apres_le_montage_arret(monte):
    p = monte.tmp / "travail" / "jetons-gardes.json"
    lu = json.loads(p.read_text(encoding="utf-8"))
    lu["ids"], lu["chaines"] = lu["ids"][:-1], lu["chaines"][:-1]
    p.write_text(json.dumps(lu), encoding="utf-8")
    with pytest.raises(Arret, match="jetons gardés"):
        la.calculer(monte.ctx, monte.entrees, monte.registre_bbis)


def test_calcul_audit_joue_quand_un_declencheur_se_leve(tmp_path, monkeypatch):
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    monkeypatch.setattr(K, "SEUIL_COS_SONDE_LECTEUR", -2.0)               # tout couple sonde-lecteur devient « trop beau »
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis)
    tables = json.loads((tmp_path / "sortie" / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    assert tables["declencheurs_d_audit"]["trop_beau_declenche"] is True
    audit = tables["audit"]
    assert audit["contenu"] == list(au.CONTENU_AUDIT) and audit["empreintes_des_tableaux_lus_egales_a_E2"] is True
    assert audit["point_de_capture_de_la_lentille"] == "block_output" and audit["issue"] == "écrite en réserve ; aucune table ne change"
    assert len(audit["directions_relues_par_un_chemin_independant"]) == 2
    for relue in audit["directions_relues_par_un_chemin_independant"]:
        assert relue["jetons_communs"] == relue["k"] == 20 and relue["ecart_relatif_maximal"] < 1e-4 and relue["imparite_ecart_maximal"] == 0
    assert all(c["couche_de_la_sonde"] == c["indice_de_la_matrice"] for c in audit["couches"])


def test_ligne_de_commande_arret_code_3_sans_trace(tmp_path, capsys):
    bbis, propre = J.ecrire_registres(tmp_path / "r", verdict=False)
    code = la.principal(["recuperer", "--url", "url-jamais-contactee", "--entrees", str(tmp_path / "e"), "--registre-bbis", str(bbis),
                         "--registre-propre", str(propre)])
    sortie = capsys.readouterr()
    assert code == 3 and sortie.err.startswith("ARRÊT : VERDICT-BBIS absente") and sortie.out == ""


def test_calcul_direction_de_norme_nulle_non_calculable_sans_arret(tmp_path):
    m = J.monde(tmp_path, echelles={("P-S100", "e0", "sonde"): 0.0})
    la.monter(m.ctx)
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis)
    tables = json.loads((tmp_path / "sortie" / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    nulles = [d for d in tables["directions"] if d.get("non_calculable")]
    assert [(d["sonde"], d["vecteur"], d["non_calculable"]) for d in nulles] == [("P-S100/e0/sonde", "w", "norme nulle")]
    assert "lectures" not in nulles[0] and len(tables["directions"]) == 25
    phrases = la.rendre_phrases(tables)
    assert {"sonde": "P-S100/e0/sonde/w", "phrase": "Non lue : norme nulle."} in phrases["non_lues"]
