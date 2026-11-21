"""Essais de `phrases_v2`, `reproduction_v1` et `audits_v2` (texte de lecture v2 scellé, `a2bbed7a…`, « Code neuf », essais
« phrases », « reproduction », déclencheurs d'audit des comparaisons, et, des brouillons 5 et 6 : phrase du déclencheur (vi)
recopiée, première passe lancée et non achevée, une lentille à chaque palier). Cas sain et artefact pour chacun (R5)."""
from __future__ import annotations

import json
import re

import numpy as np
import pytest

torch = pytest.importorskip("torch")

import lentilles_sondes_bbis_seconde_passe_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import audits_v2 as au  # noqa: E402
from controle_ia.lentilles_sondes_bbis import comparaisons_lentilles_v1 as co  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v2 as K2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nos_lentilles_v1 as nl  # noqa: E402
from controle_ia.lentilles_sondes_bbis import phrases_v1 as ph1  # noqa: E402
from controle_ia.lentilles_sondes_bbis import phrases_v2 as ph  # noqa: E402
from controle_ia.lentilles_sondes_bbis import reproduction_v1 as rp  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v4 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, Refus  # noqa: E402

TEXTE = (J.RACINE / K2.TEXTE_V2).read_text(encoding="utf-8")
C, I, N = st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, st.LIBELLE_NON_DISTINCTE
VI = ["(vi) trop propre au deuxième palier : 31 matrices égales ou série inchangée à zéro exact"]
PLUS_REJOUEE = ("avertissement", "lecture_seconde_course")


# === phrases permises : égales, octet pour octet, à celles du texte ========================================================================
def test_le_code_cite_le_texte_scelle_de_la_seconde_passe():
    import hashlib
    assert hashlib.sha256((J.RACINE / K2.TEXTE_V2).read_bytes()).hexdigest() == K2.EMPREINTE_TEXTE_V2


@pytest.mark.parametrize("forme", sorted(ph.FORMES_CI))
def test_chacune_des_six_formes_des_phrases_permises_egale_octet_pour_octet_a_celle_du_texte(forme):
    assert len(ph.FORMES_CI) == 6
    assert f"« {ph.FORMES_CI[forme]} »" in TEXTE


def test_la_phrase_de_notre_s_seule_construite_par_la_regle_du_critere_egale_celle_que_le_texte_ecrit():
    assert ph.CI_S_SEULE_AU_DEUXIEME_PALIER != ph.CI_R_SEULE_AU_DEUXIEME_PALIER
    assert ph.REMPLACEMENT_POUR_S in ph.CI_S_SEULE_AU_DEUXIEME_PALIER and "deux séries" not in ph.CI_S_SEULE_AU_DEUXIEME_PALIER
    assert f"« {ph.CI_S_SEULE_AU_DEUXIEME_PALIER} »" in TEXTE


def test_phrase_de_tete_et_phrases_fixes_egales_a_celles_du_texte():
    sans_gras = TEXTE.replace("**", "")
    assert re.sub(r"\s+", " ", ph.PHRASE_DE_TETE_V2) in re.sub(r"\s+", " ", sans_gras)
    for phrase in (ph.PHRASE_SANS_MESURE, ph.PHRASE_DOMAINE_D_USAGE, ph.PHRASE_REPRODUCTION_NON_FAITE):
        assert re.sub(r"\s+", " ", phrase) in re.sub(r"\s+", " ", sans_gras)
    assert "code de lecture différent de celui de la première passe : " in TEXTE


# --- la forme choisie d'après le couple des deux verdicts, un cas par couple ---------------------------------------------------------------
def _conditions(tmp_path, r, s, plus=PLUS_REJOUEE, variante=K2.VARIANTE_COURSE_REJOUEE, seconde=K2.SECONDE_COURSE_ENTIERE):
    fiche = J.fiche(r=r, s=s, variante=variante, seconde_course=seconde,
                    lecture_seconde_course={"chemin": "docs/l2.md", "sha256": "8" * 64, "ligne_d_ensemble": "« partiel », seconde course"})
    registre = J.monde(tmp_path, fiche, plus=plus)
    etat = nl.exiger_registre_v2(registre)
    fiche = nl.lire_fiche(tmp_path, etat)
    return nl.condition_de_lecture(fiche, etat, tmp_path), fiche


def _lentille(lettre, sorte):
    if sorte == "p1":
        return J.lentille(lettre)
    if sorte == "p2":
        return J.lentille(lettre, verdict=K2.PALIER_2)
    if sorte == "autre":
        return J.lentille(lettre, verdict=K2.DIFFERENTE)
    return J.lentille(lettre, verdict=None)


COUPLES = {("p1", "p1"): ("deux au premier palier", "deux au premier palier"),
           ("p1", "p2"): ("une seule au premier palier", "S seule au deuxième palier"),
           ("p2", "p1"): ("R seule au deuxième palier", "une seule au premier palier"),
           ("p2", "p2"): ("deux au deuxième palier", "deux au deuxième palier"),
           ("p1", "autre"): ("une seule au premier palier", "tout autre verdict"),
           ("autre", "p2"): ("tout autre verdict", "S seule au deuxième palier"),
           ("p2", "autre"): ("R seule au deuxième palier", "tout autre verdict"),
           ("autre", "autre"): ("tout autre verdict", "tout autre verdict"),
           ("p1", "sans"): ("une seule au premier palier", None)}


@pytest.mark.parametrize("couple", sorted(COUPLES))
def test_la_forme_choisie_d_apres_le_couple_des_deux_verdicts(tmp_path, couple):
    conditions, fiche = _conditions(tmp_path, _lentille("R", couple[0]), _lentille("S", couple[1]))
    formes = ph.formes_des_phrases_permises(conditions)
    assert (formes["R"], formes["S"]) == COUPLES[couple]
    lignes = ph.phrases_permises(conditions, fiche, conditions["course"], True)
    for ligne in lignes:
        for phrase in ligne["phrases"]:
            assert "[" not in phrase and "…" not in phrase       # tous les crochets sont remplis
    ecrites = [l["forme"] for l in lignes]
    assert len(ecrites) == (1 if COUPLES[couple][0] == COUPLES[couple][1] and couple[0] != "autre" else 2)


def test_artefact_la_forme_au_pluriel_ecrite_alors_qu_une_seule_lentille_est_a_ce_palier_refus(tmp_path):
    conditions, _ = _conditions(tmp_path, _lentille("R", "p1"), _lentille("S", "p2"))
    with pytest.raises(Refus, match="ne convient pas"):
        ph.exiger_forme("deux au premier palier", "R", conditions)
    with pytest.raises(Refus, match="ne convient pas"):
        ph.exiger_forme("deux au deuxième palier", "S", conditions)
    ph.exiger_forme("une seule au premier palier", "R", conditions)


def test_seuls_les_crochets_se_remplissent_aucun_autre_mot_ne_change(tmp_path):
    conditions, fiche = _conditions(tmp_path, _lentille("R", "p2"), _lentille("S", "p2"))
    phrase = ph.phrases_permises(conditions, fiche, conditions["course"], True)[0]["phrases"][0]
    gabarit = ph.CI_DEUX_AU_DEUXIEME_PALIER
    motif = re.escape(gabarit)
    for crochet in ("[écart mesuré]", "[valeur]"):
        motif = motif.replace(re.escape(crochet), r"[0-9,e+\-]+")
    motif = motif.replace(re.escape(ph.CROCHET_REFAITES["elles"][0]), re.escape(ph.CROCHET_REFAITES["elles"][2]))
    assert re.fullmatch(motif, phrase)
    assert "3,5e-05" in phrase and "0,00015 et 0,00025" in phrase and "de 0,069 à 1,2" in phrase
    un, fiche1 = _conditions(tmp_path / "b", _lentille("R", "p1"), _lentille("S", "p1"))
    premier = ph.phrases_permises(un, fiche1, un["course"], True)[0]["phrases"][0]
    assert premier == ph.CI_DEUX_AU_PREMIER_PALIER.replace("…", f"{K2.EMPREINTE_18_NOVEMBRE['R']}, {K2.EMPREINTE_18_NOVEMBRE['S']}")


def test_dernier_crochet_selon_la_course_et_phrase_gelee_de_la_lentille_sans_mesure(tmp_path):
    assert ph.dernier_crochet(nl.COURSE_REJOUEE, True) is True and ph.dernier_crochet(nl.COURSE_AJUSTEMENT_SEUL, False) is False
    assert ph.dernier_crochet(nl.COURSE_REJOUEE_INCOMPLETE, True) is False
    assert ph.dernier_crochet(nl.COURSE_REJOUEE_MUETTE, True) is None and ph.dernier_crochet(nl.COURSE_REJOUEE, False) is None
    conditions, fiche = _conditions(tmp_path, _lentille("R", "p2"), _lentille("S", "autre"),
                                    plus=("avertissement", J.ligne_du_noeud(tmp_path)), variante=K2.VARIANTE_AJUSTEMENT_SEUL, seconde=None)
    ligne = ph.phrases_permises(conditions, fiche, conditions["course"], False)[0]
    assert ligne["phrases"][0].endswith("Les mesures du 18 novembre n'ont pas été refaites sur elle.")
    assert ligne["phrases"][-1] == ph.PHRASE_SANS_MESURE
    muette, fiche_m = _conditions(tmp_path / "m", _lentille("R", "p2"), _lentille("S", "autre"), seconde=None)
    ligne = ph.phrases_permises(muette, fiche_m, muette["course"], True)[0]
    assert ligne["phrases"] == [] and ligne["notes"] == [ph.NOTE_DERNIER_CROCHET] and "fiche muette" in ligne["non_lues"][0]


def test_une_lentille_non_lue_recoit_la_phrase_de_son_verdict_suivie_de_sa_ligne_non_lue(tmp_path):
    conditions, fiche = _conditions(tmp_path, _lentille("R", "autre"), J.lentille("S", audit=None))
    lignes = {tuple(l["lentilles"]): l for l in ph.phrases_permises(conditions, fiche, conditions["course"], True)}
    assert lignes[("R",)]["phrases"] == ["Lentille R : verdict d'identité « différente » ; elle n'est pas lue ici."]
    assert lignes[("R",)]["non_lues"] == ["Non lue : notre lentille R au verdict d'identité « différente »"]
    assert lignes[("S",)]["phrases"][0].startswith("Le fichier d'ajustement réajusté de la lentille S est identique")
    assert lignes[("S",)]["non_lues"] == ["Non lue : notre lentille S au premier palier sans audit versé"]
    assert ph.ligne_du_verdict_d_identite(conditions, conditions["course"]) == (
        f"Verdict d'identité : notre R : différente ; notre S : {K2.PALIER_1}. Course du réajustement : course rejouée.")


# --- phrase du déclencheur (vi), recopiée après la phrase permise ----------------------------------------------------------------------------
@pytest.mark.parametrize("s", ["autre", "p2"], ids=["notre R seule", "nos deux lentilles"])
def test_phrase_du_declencheur_vi_recopiee_apres_la_phrase_permise_sans_un_mot_de_plus(tmp_path, s):
    vi = nl.VI_DEBUT + "31 matrices des moitiés égales sur 31 et séries des écarts inchangées" + nl.VI_FIN
    r = J.lentille("R", verdict=K2.PALIER_2, declencheurs=VI, phrase_du_declencheur_vi=vi)
    conditions, fiche = _conditions(tmp_path, r, _lentille("S", s))
    ligne = ph.phrases_permises(conditions, fiche, conditions["course"], True)[0]
    assert "R" in ligne["lentilles"] and ligne["phrases"][1] == vi and len(ligne["phrases"]) == 2
    sans, fiche_s = _conditions(tmp_path / "sans", _lentille("R", "p2"), _lentille("S", s))
    assert len(ph.phrases_permises(sans, fiche_s, sans["course"], True)[0]["phrases"]) == 1      # champ « aucune » : rien n'est ajouté


# --- verdict d'ensemble ---------------------------------------------------------------------------------------------------------------------
def test_premier_palier_nos_deux_lentilles_une_ligne_et_les_reserves_r_a_a_r_e(tmp_path):
    conditions, fiche = _conditions(tmp_path, _lentille("R", "p1"), _lentille("S", "p1"))
    lignes = ph.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])
    assert len(lignes) == 1 and lignes[0]["texte"].startswith("Verdict d'ensemble de la tranche de nos lentilles : ")
    assert K2.EMPREINTE_VERDICT_TRANCHE in lignes[0]["texte"] and "(R-a) à (R-e)" in lignes[0]["texte"]
    assert "désaccord entre les deux mesures de la tranche, nœud de Lazar" in lignes[0]["texte"]


def test_cas_mixte_au_premier_palier_forme_ne_se_transportent_pas_tels_quels_et_les_seules_reserves_de_la_lentille(tmp_path):
    conditions, fiche = _conditions(tmp_path, _lentille("R", "autre"), _lentille("S", "p1"))
    lignes = ph.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])
    assert len(lignes) == 1 and "ne se transportent pas tels quels : seules les mesures faites sur notre lentille S la décrivent" in lignes[0]["texte"]
    assert "(R-d) et (R-e)" in lignes[0]["texte"] and "(R-a)" not in lignes[0]["texte"] and "(R-c)" not in lignes[0]["texte"]


def test_deuxieme_palier_le_verdict_ne_se_transporte_pas_et_les_mesures_sont_celles_de_la_seconde_course(tmp_path):
    conditions, fiche = _conditions(tmp_path, _lentille("R", "p2"), _lentille("S", "p2"))
    ligne = ph.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])[0]["texte"]
    assert "Ce verdict ne se transporte pas à la lentille lue ici." in ligne
    assert "Ses mesures sont celles de la seconde course : « partiel », seconde course" in ligne and K2.AUCUNE_LIMITE in ligne
    assert "rappelées pour contexte ; elles ne décrivent pas la lentille lue : [(R-a) à (R-e)]." in ligne


@pytest.mark.parametrize("premier, deuxieme", [("R", "S"), ("S", "R")])
def test_une_lentille_a_chaque_palier_les_deux_lignes_chacune_nomme_sa_lentille(tmp_path, premier, deuxieme):
    sortes = {premier: "p1", deuxieme: "p2"}
    conditions, fiche = _conditions(tmp_path, _lentille("R", sortes["R"]), _lentille("S", sortes["S"]))
    lignes = ph.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])
    assert [l["palier"] for l in lignes] == [1, 2] and [l["lentilles"] for l in lignes] == [[premier], [deuxieme]]
    assert f"seules les mesures faites sur notre lentille {premier} la décrivent" in lignes[0]["texte"]
    assert f"Ce verdict ne se transporte pas à notre lentille {deuxieme}." in lignes[1]["texte"]
    assert f"elles ne décrivent pas notre lentille {deuxieme} : {ph.RESERVES_DE[deuxieme]}." in lignes[1]["texte"]
    assert "(R-a) à (R-e)" not in lignes[1]["texte"]
    autres = {"R": "(R-d)", "S": "(R-c)"}
    assert autres[deuxieme] not in lignes[1]["texte"]


def test_artefact_une_seule_ligne_ecrite_ou_la_liste_entiere_des_reserves_refus():
    lues = {"R": 1, "S": 2}
    saines = [{"palier": 1, "lentilles": ["R"], "texte": "… notre lentille R …", "reserves": ph.RESERVES_DE["R"]},
              {"palier": 2, "lentilles": ["S"], "texte": "… notre lentille S …", "reserves": ph.RESERVES_DE["S"]}]
    ph.exiger_lignes_du_verdict_d_ensemble(saines, lues)
    with pytest.raises(Refus, match="exige les deux lignes"):
        ph.exiger_lignes_du_verdict_d_ensemble(saines[:1], lues)
    entiere = [saines[0], dict(saines[1], reserves="[(R-a) à (R-e)]")]
    with pytest.raises(Refus, match="d'autres réserves que les siennes"):
        ph.exiger_lignes_du_verdict_d_ensemble(entiere, lues)
    sans_nom = [saines[0], dict(saines[1], texte="… la lentille lue ici …")]
    with pytest.raises(Refus, match="ne nomme pas sa lentille"):
        ph.exiger_lignes_du_verdict_d_ensemble(sans_nom, lues)


# --- paraphrases interdites -------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("phrase", ["La lentille réajustée est équivalente à celle du 18 novembre.", "Elle en est proche.",
                                    "C'est la même à la précision près.", "Elle est couverte par concordance.",
                                    "La lentille est rattachée au verdict.", "Elle a été réajustée à l'identique."])
def test_une_paraphrase_interdite_injectee_refus(phrase):
    with pytest.raises(Refus, match="phrase interdite du critère d'identité"):
        ph.exiger_sans_paraphrase_interdite(phrase)


def test_les_phrases_du_code_ne_portent_aucune_paraphrase_interdite_et_une_limite_recopiee_qui_en_porte_une_est_refusee(tmp_path):
    for phrase in list(ph.FORMES_CI.values()) + [ph.PHRASE_DE_TETE_V2, ph.PHRASE_SANS_MESURE, ph.PHRASE_DOMAINE_D_USAGE]:
        ph.exiger_sans_paraphrase_interdite(phrase)
    ph.exiger_sans_paraphrase_interdite("loi de référence approchée")          # « approchée » n'est pas « proche »
    limites = {str(c): {"limite": "lentille équivalente à celle du 18 novembre", "ecartee": False} for c in K.COUCHES}
    conditions, fiche = _conditions(tmp_path, J.lentille("R", verdict=K2.PALIER_2, seconde_course_par_couche=limites), _lentille("S", "autre"))
    with pytest.raises(Refus, match="phrase interdite"):
        ph.lignes_du_verdict_d_ensemble(conditions, fiche, conditions["course"])


# --- phrases par direction --------------------------------------------------------------------------------------------------------------------
SONDE = ph.nom_sonde("P-S50", "e1", "sonde", "w")
JETONS = ["cost", "42"]


def test_phrases_de_notre_r_celles_de_la_premiere_passe_avec_le_nom_de_la_lentille():
    for libelle in (C, I, N):
        v1 = ph1.phrase_direction(K.LENTILLE_PUBLIQUE, SONDE, 15, "+", libelle, 7.5, 0.0005, 0.004, JETONS)
        assert ph.phrase_direction(K.LENTILLE_PUBLIQUE, SONDE, 15, "+", libelle, 7.5, 0.0005, 0.004, JETONS) == v1
        r = ph.phrase_direction(K2.LENTILLE_NOTRE_R, SONDE, 15, "+", libelle, 7.5, 0.0005, 0.004, JETONS)
        assert r == v1.replace("Par la lentille publique côté sortie,", "Par notre lentille R,")
    poles = [{"neurone": 3, "signe": "+", "cosinus": 0.5}]
    v1 = ph1.phrase_poles(C, poles, 0.0005, 0.004, [["a"]])
    assert ph.phrase_poles(K2.LENTILLE_NOTRE_R, C, poles, 0.0005, 0.004, [["a"]]) == v1.replace("la lentille publique les lit", "notre lentille R les lit")
    assert ph.phrase_poles(K.LENTILLE_PUBLIQUE, C, poles, 0.0005, 0.004, [["a"]]) == v1
    with pytest.raises(Arret, match="notre S ne lit pas les pôles"):
        ph.phrase_poles(K2.LENTILLE_NOTRE_S, C, poles, 0.0005, 0.004, [["a"]])


def test_phrases_de_notre_s_une_par_libelle_font_monter_jamais_la_sonde_detecte():
    phrases = {l: ph.phrase_direction(K2.LENTILLE_NOTRE_S, SONDE, 7, "-", l, 7.5, 0.0005, 0.004, JETONS) for l in (C, I, N)}
    assert phrases[C].startswith("Par notre lentille S côté entrée, les jetons d'entrée qui font monter en moyenne la direction de")
    assert phrases[C].endswith("; ces jetons : 'cost', '42'.") and "(couche 7, signe -)" in phrases[C]
    assert "sans être nommés comme ce qui la fait monter" in phrases[I] and "aucune phrase ne les nomme." in phrases[N]
    assert len(set(phrases.values())) == 3 and not any("détecte" in p or "capte" in p for p in phrases.values())
    assert "'cost'" not in phrases[I] and "'cost'" not in phrases[N]
    with pytest.raises(Arret, match="libellé"):
        ph.phrase_direction(K2.LENTILLE_NOTRE_S, SONDE, 7, "-", "autre", 1.0, 0.1, 0.1, [])


def test_famille_par_notre_s_phrase_de_q_distincte_de_celle_de_w_et_aux_couches_15_et_23_rapporte_sans_conclusion():
    arg = ("nombres", 6, 0.4, 0.0005, 0.004, True)
    w, q = (ph.phrase_famille(K2.LENTILLE_NOTRE_S, v, 7, *arg) for v in ("w", "q"))
    assert w != q and "soupçon que la sonde monte avec des nombres dans le texte qu'elle lit" in w
    assert "dans les vingt premiers jetons d'entrée de la requête" in q and "l'attention de la sonde se porte sur les positions" in q
    for couche in (15, 23):
        for v in ("w", "q"):
            p = ph.phrase_famille(K2.LENTILLE_NOTRE_S, v, couche, *arg)
            assert f"rapporté sans conclusion, la couche {couche} étant hors du domaine d'usage" in p and "soupçon" not in p
    non = ph.phrase_famille(K2.LENTILLE_NOTRE_S, "w", 7, "cout", 1, 0.4, 0.3, 0.2, False)
    assert non == "La famille coût n'est pas sur-représentée parmi ses jetons d'entrée par notre lentille S (1 ; p 0,3 et 0,2) : cela ne blanchit pas la sonde."
    assert ph.phrase_famille(K2.LENTILLE_NOTRE_R, "w", 23, *arg) == ph1.phrase_famille(*arg)      # notre R : phrase de la première passe


def test_une_phrase_par_libelle_neuf_de_comparaison_entre_lentilles():
    base = {"recouvrement": 14, "mediane": 9.5, "p": (0.0005, 0.004), "moities": 18}
    commune = ph.phrase_comparaison_entre_lentilles(SONDE, 23, "+", base | {"libelle": co.LECTURE_COMMUNE})
    assert "tient d'une lentille R à l'autre" in commune and commune.endswith("cela ne dit pas que toute lentille lirait de même.")
    assert "14 sur vingt (médiane des directions nulles : 9,5 sur vingt ; p 0,0005 et 0,004 ; les deux moitiés de notre R : 18 sur vingt)" in commune
    propre = ph.phrase_comparaison_entre_lentilles(SONDE, 23, "+", base | {"libelle": co.LECTURE_PROPRE, "lentille": K2.LENTILLE_NOTRE_R,
                                                                         "autre": K.LENTILLE_PUBLIQUE})
    assert "notre lentille R la distingue des nuls, la lentille publique côté sortie non" in propre
    assert propre.endswith("Ce que notre lentille R lui associe est en table, sans être tenu pour ce que la direction pousse.")
    aucune = ph.phrase_comparaison_entre_lentilles(SONDE, 23, "+", base | {"libelle": co.DEUX_NON_DISTINCTES})
    assert aucune.startswith("Aucune des deux lentilles R ne distingue la direction de") and "médiane des directions nulles : 9,5" in aucune
    mixte = ph.phrase_comparaison_entre_lentilles(SONDE, 23, "+", base | {"libelle": co.MIXTE, "libelles": (C, I)})
    assert f"par les deux lentilles R : {C} et {I} ; recouvrement 14 sur vingt" in mixte and mixte.endswith("rapporté sans conclusion.")
    non = ph.phrase_comparaison_entre_lentilles(SONDE, 23, "+", co.non_calculable(co.MOTIF_LIBELLE_DIFFERENT))
    assert non == f"Comparaison entre lentilles non faite pour {SONDE} : {co.MOTIF_LIBELLE_DIFFERENT}."
    assert len({commune, propre, aucune, mixte, non}) == 5
    for p in (commune, propre, aucune, mixte):
        assert not any(mot in p for mot in ("a raison", "se trompe", "valide", "blanchit", "accuse"))


def test_renvois_aux_reserves():
    assert ph.renvois(K2.LENTILLE_NOTRE_R, 7, 1) == ["(R-c)"] and ph.renvois(K2.LENTILLE_NOTRE_R, 15, 1) == ["(R-c)"]
    assert ph.renvois(K2.LENTILLE_NOTRE_R, 23, 1) == [] and ph.renvois(K.LENTILLE_PUBLIQUE, 7, None) == []
    assert ph.renvois(K2.LENTILLE_NOTRE_S, 23, 1) == ["(R-d)", "(R-u)"]
    assert ph.renvois(K2.LENTILLE_NOTRE_S, 7, 2) == ["(R-d) — mesurée sur la lentille du 18 novembre, non refaite sur la lentille lue", "(R-u)"]
    assert ph.renvois(K2.LENTILLE_NOTRE_R, 15, 2, "« partiel »") == ["(R-c) — voir la lecture de la seconde course : « partiel »"]


# === reproduction ==============================================================================================================================
def _tables(libelle=C, ids=None, sonde="P-S50/e1/sonde"):
    ids = list(range(20)) if ids is None else ids
    signe = {"libelle": libelle, "premiers_par_score": {"ids": ids}}
    return {"entrees": {"e1_sha256": "1" * 64, "e2_sha256": "2" * 64},
            "directions": [{"sonde": sonde, "vecteur": "w", "couche": 15,
                            "lectures": {K.LENTILLE_PUBLIQUE: {"signes": {"+": dict(signe), "-": dict(signe)}},
                                         K.LENTILLE_LOGITS: {"signes": {"+": dict(signe), "-": dict(signe)}}}}]}


def _premiere_passe(tmp_path, tables, plus=("entrees_v1",), **monde_plus):
    """Écrit des tables jouets de la première passe et leur ligne de registre."""
    run = "20261122-000000-jouet-v1"
    scores = {f"scores__P-S50__e1__sonde__w__{l}": np.arange(30, dtype=np.float32) for l in rp.LENTILLES_REPRODUITES}
    (tmp_path / "donnees" / run).mkdir(parents=True)
    np.savez(tmp_path / "donnees" / run / "lectures-lentilles-bbis-000.npz", **scores)
    morceau = {"fichier": "lectures-lentilles-bbis-000.npz", "tableaux": sorted(scores),
               "sha256": J.sha((tmp_path / "donnees" / run / "lectures-lentilles-bbis-000.npz").read_bytes())}
    chemin = f"diag/{run}/tables-lentilles-bbis.json"
    s = J.ecrire(tmp_path, chemin, json.dumps(tables | {"fichiers_des_lectures": [morceau]}))
    ligne = (K2.CLE_TABLES_V1, J.H["tables_v1"], chemin, s)
    registre = J.monde(tmp_path, plus=plus + (ligne,), **monde_plus)
    return registre, nl.exiger_registre_v2(registre), scores


def test_reproduction_tables_jouets_egales_aucune_reserve(tmp_path):
    registre, etat, scores = _premiere_passe(tmp_path, _tables())
    un = rp.ouvrir_tables_premiere_passe(tmp_path, registre, etat)
    assert rp.exiger_memes_entrees(un, "1" * 64, "2" * 64)["egales_entre_les_deux_passes"]
    r = rp.comparer(un, _tables(), rp.scores_premiere_passe(tmp_path, un), scores)
    assert r["nombre_de_lectures_differentes"] == 0 and r["lectures_comparees"] == 4 and not r["audit_de_symetrie_a_jouer"]
    assert r["ecart_relatif_maximal_des_scores"] == 0.0 and r["directions_au_libelle_de_la_lentille_publique_different"] == []
    assert ph.phrases_de_la_reproduction(r, ("statistiques_v4",)) == [
        "Reproduction de la première passe : aucune.", "code de lecture différent de celui de la première passe : statistiques_v4"]


def test_reproduction_un_libelle_change_reserve_sans_arret_comparaisons_non_calculables_audit_joue(tmp_path):
    registre, etat, scores = _premiere_passe(tmp_path, _tables())
    un = rp.ouvrir_tables_premiere_passe(tmp_path, registre, etat)
    deux = _tables()
    deux["directions"][0]["lectures"][K.LENTILLE_PUBLIQUE]["signes"]["+"] = {"libelle": I, "premiers_par_score": {"ids": list(range(20))}}
    r = rp.comparer(un, deux, rp.scores_premiere_passe(tmp_path, un), {k: v * 1.01 for k, v in scores.items()})
    assert r["nombre_de_lectures_differentes"] == 1 and r["audit_de_symetrie_a_jouer"] and r["issue"] == "réserve écrite, sans arrêt"
    assert rp.libelle_public_different(r, "P-S50/e1/sonde", "w", "+") and not rp.libelle_public_different(r, "P-S50/e1/sonde", "w", "-")
    assert r["ecart_relatif_maximal_des_scores"] == pytest.approx(0.01, rel=1e-3)
    assert ph.phrases_de_la_reproduction(r, ())[0] == "Reproduction de la première passe : 1."
    assert au.declencheurs([], [], [], r)["incoherent"]["reproduction_de_la_premiere_passe_differente"]


def test_reproduction_jetons_changes_ou_seulement_reordonnes(tmp_path):
    registre, etat, _ = _premiere_passe(tmp_path, _tables())
    un = rp.ouvrir_tables_premiere_passe(tmp_path, registre, etat)
    autres = rp.comparer(un, _tables(ids=list(range(1, 21))))
    assert autres["nombre_de_lectures_differentes"] == 4 and autres["directions_au_libelle_de_la_lentille_publique_different"] == []
    ordre = rp.comparer(un, _tables(ids=list(range(19, -1, -1))))
    assert ordre["nombre_de_lectures_differentes"] == 0 and ordre["lectures_aux_memes_jetons_dans_un_autre_ordre"] == 4


def test_artefact_tables_de_la_premiere_passe_d_une_autre_empreinte_que_leur_ligne_arret(tmp_path):
    registre, etat, _ = _premiere_passe(tmp_path, _tables())
    chemin = tmp_path / etat.derniere(K2.CLE_TABLES_V1).chemin
    chemin.write_bytes(chemin.read_bytes() + b" ")        # un octet de plus
    with pytest.raises(Arret, match="autre empreinte que celle de la ligne TABLES-LENTILLES-BBIS"):
        rp.ouvrir_tables_premiere_passe(tmp_path, registre, etat)


def test_artefact_archive_de_lectures_de_la_premiere_passe_alteree_arret(tmp_path):
    registre, etat, _ = _premiere_passe(tmp_path, _tables())
    un = rp.ouvrir_tables_premiere_passe(tmp_path, registre, etat)
    archive = next((tmp_path / "donnees").rglob("*.npz"))
    archive.write_bytes(archive.read_bytes() + b"\0")
    with pytest.raises(Arret, match="absente ou d'une autre empreinte"):
        rp.scores_premiere_passe(tmp_path, un)


@pytest.mark.parametrize("e1, e2", [("0" * 64, "2" * 64), ("1" * 64, "0" * 64)])
def test_artefact_empreinte_de_e1_ou_de_e2_differente_entre_les_passes_arret(tmp_path, e1, e2):
    with pytest.raises(Arret, match="différente entre les deux passes"):
        rp.exiger_memes_entrees(_tables(), e1, e2)


def test_ouverture_d_une_table_avant_le_scellement_de_la_v2_refus_et_apres_permise(tmp_path):
    registre, etat, _ = _premiere_passe(tmp_path / "apres", _tables())
    assert rp.ouvrir_tables_premiere_passe(tmp_path / "apres", registre, etat)["directions"]
    avant = J.monde(tmp_path / "avant", sans=(K2.CLE_SCELLEMENT_V2,), plus=("entrees_v1", "tables_v1"))
    with pytest.raises(Refus, match="ouverture d'une table par le code avant"):
        rp.ouvrir_tables_premiere_passe(tmp_path / "avant", avant, etat)


# --- première passe lancée et non achevée (registre jouet) -------------------------------------------------------------------------------------
def test_premiere_passe_jamais_lancee_la_seconde_la_remplace_et_c_est_ecrit(tmp_path):
    etat = nl.exiger_registre_v2(J.monde(tmp_path))
    r = rp.sans_comparaison(etat.premiere_passe)
    assert r["etat"] == rp.ETAT_REMPLACEE and r["phrases_de_la_lentille_publique_et_des_logits_ecrites"] is True
    assert ph.phrases_de_la_reproduction(r, ("statistiques_v4",))[0] == ph.NOTE_PREMIERE_PASSE_REMPLACEE


def test_artefact_premiere_passe_lancee_et_non_achevee_aucune_phrase_de_la_lentille_publique(tmp_path):
    """`ENTREES-LENTILLES-BBIS` présente, `TABLES-LENTILLES-BBIS` absente : la seconde passe ne remplace pas la première ; elle
    écrit la phrase « Reproduction de la première passe : non faite […] » ; un code qui la remplacerait est vu (drapeau)."""
    etat = nl.exiger_registre_v2(J.monde(tmp_path, plus=("entrees_v1",)))
    r = rp.sans_comparaison(etat.premiere_passe)
    assert r["etat"] == rp.ETAT_NON_FAITE and r["phrases_de_la_lentille_publique_et_des_logits_ecrites"] is False
    assert ph.phrases_de_la_reproduction(r, ("statistiques_v4",)) == [ph.PHRASE_REPRODUCTION_NON_FAITE]
    with pytest.raises(Arret, match="rien n'est ouvert"):
        rp.ouvrir_tables_premiere_passe(tmp_path, tmp_path / J.REGISTRE, etat)


# === déclencheurs d'audit de la seconde passe ===================================================================================================
def _lecture(sonde="s0", lentille=K.LENTILLE_PUBLIQUE, libelle=N, ids=None, couche=7, vecteur="w", signe="+"):
    return {"sonde": sonde, "vecteur": vecteur, "signe": signe, "couche": couche, "lentille": lentille, "libelle": libelle,
            "ids": list(range(20)) if ids is None else ids}


SANS_REPRODUCTION = {"audit_de_symetrie_a_jouer": False}


def test_declencheurs_non_leves_sur_un_cas_sain():
    lectures = [_lecture(lentille=l, libelle=I, ids=list(range(i * 30, i * 30 + 20))) for i, l in enumerate(K2.LENTILLES_V2)]
    recouvrements = [{"couche": 23, "publique_et_notre_r": 8, "moities": 15}, {"couche": 7, "publique_et_notre_r": 3, "moities": 12}]
    seuls = [{"sonde": "s0", "vecteur": "w", "signe": "+", "ids": list(range(500, 520))}]
    d = au.declencheurs(lectures, recouvrements, seuls, SANS_REPRODUCTION)
    assert not d["audit_a_jouer"] and not d["trop_beau_declenche"] and not d["tout_negatif_declenche"] and not d["incoherent_declenche"]


def test_declencheur_memes_vingt_jetons_a_la_couche_7_par_notre_r_et_la_lentille_publique():
    lectures = [_lecture(lentille=K.LENTILLE_PUBLIQUE, libelle=I), _lecture(lentille=K2.LENTILLE_NOTRE_R, libelle=I)]
    d = au.declencheurs(lectures, [], [], SANS_REPRODUCTION)
    assert d["trop_beau"]["memes_vingt_jetons_par_notre_r_et_la_lentille_publique_couche_7"] == ["s0/w/+"] and d["audit_a_jouer"]
    couche_23 = [dict(l, couche=23) for l in lectures]
    assert au.declencheurs(couche_23, [], [], SANS_REPRODUCTION)["trop_beau"]["memes_vingt_jetons_par_notre_r_et_la_lentille_publique_couche_7"] == []


def test_declencheurs_des_comparaisons_leves_et_non_leves():
    plein = [{"couche": 7, "publique_et_notre_r": 20, "moities": 20}] * 3 + [{"couche": 7, "publique_et_notre_r": 5, "moities": 9}] * 2
    assert au.declencheurs([], plein, [], SANS_REPRODUCTION)["trop_beau"]["recouvrement_de_20_sur_20_pour_plus_de_la_moitie_des_directions"]
    moitie = plein[:2] + plein[3:]                               # deux sur quatre : pas « plus de la moitié »
    assert not au.declencheurs([], moitie, [], SANS_REPRODUCTION)["trop_beau"]["recouvrement_de_20_sur_20_pour_plus_de_la_moitie_des_directions"]
    vides = [{"couche": 23, "publique_et_notre_r": 0, "moities": 9}] * 2 + [{"couche": 23, "publique_et_notre_r": 4, "moities": 9},
                                                                           {"couche": 7, "publique_et_notre_r": 0, "moities": 9}]
    cle = "recouvrement_de_0_sur_20_pour_plus_de_la_moitie_des_directions_de_la_couche_23"
    assert au.declencheurs([], vides, [], SANS_REPRODUCTION)["tout_negatif"][cle]
    assert not au.declencheurs([], [dict(v, couche=7) for v in vides], [], SANS_REPRODUCTION)["tout_negatif"][cle]
    sous = [{"couche": 15, "publique_et_notre_r": 12, "moities": 6}] * 2 + [{"couche": 15, "publique_et_notre_r": 12, "moities": 18}]
    cle = "recouvrement_des_moities_inferieur_a_celui_des_deux_lentilles_r_pour_plus_de_la_moitie_des_directions"
    assert au.declencheurs([], sous, [], SANS_REPRODUCTION)["incoherent"][cle]
    assert not au.declencheurs([], sous[1:], [], SANS_REPRODUCTION)["incoherent"][cle]
    assert not au.declencheurs([], [dict(s, moities=None) for s in sous], [], SANS_REPRODUCTION)["incoherent"][cle]


def test_declencheur_des_plongements_seuls_et_de_notre_s_egale_a_notre_r():
    lectures = [_lecture(lentille=K2.LENTILLE_NOTRE_S, libelle=I, couche=15), _lecture(lentille=K2.LENTILLE_NOTRE_R, libelle=I, couche=15,
                                                                                    ids=list(range(100, 120)))]
    seuls = [{"sonde": "s0", "vecteur": "w", "signe": "+", "ids": list(range(19, -1, -1))}]
    d = au.declencheurs(lectures, [], seuls, SANS_REPRODUCTION)
    assert d["trop_beau"]["memes_vingt_jetons_par_notre_s_et_les_plongements_seuls"] == ["s0/w/+"] and d["trop_beau_declenche"]
    assert d["trop_beau"]["memes_vingt_jetons_par_notre_s_et_notre_r"] == []
    autres = [{"sonde": "s0", "vecteur": "w", "signe": "+", "ids": list(range(1, 21))}]
    assert au.declencheurs(lectures, [], autres, SANS_REPRODUCTION)["trop_beau"]["memes_vingt_jetons_par_notre_s_et_les_plongements_seuls"] == []
    memes = [lectures[0], dict(lectures[1], ids=list(range(20)))]
    assert au.declencheurs(memes, [], autres, SANS_REPRODUCTION)["trop_beau"]["memes_vingt_jetons_par_notre_s_et_notre_r"] == ["s0/w/+"]


def test_declencheurs_trop_beau_vingt_directions_concentrees_et_tout_negatif():
    sondes = [f"s{i}" for i in range(20)]
    toutes = [_lecture(sonde=s, lentille=K2.LENTILLE_NOTRE_S, libelle=C, ids=list(range(i * 30, i * 30 + 20))) for i, s in enumerate(sondes)]
    d = au.declencheurs(toutes, [], [], SANS_REPRODUCTION)
    assert d["trop_beau"]["vingt_directions_concentrees_par_notre_s"] and not d["trop_beau"]["vingt_directions_concentrees_par_notre_r"]
    assert not au.declencheurs(toutes[:19] + [dict(toutes[19], libelle=I)], [], [], SANS_REPRODUCTION)["trop_beau"]["vingt_directions_concentrees_par_notre_s"]
    negatif = [_lecture(lentille=l, libelle=N, ids=list(range(i * 30, i * 30 + 20))) for i, l in enumerate(K2.LENTILLES_V2)]
    cle = "aucune_lecture_concentree_ni_intermediaire_par_aucune_lentille"
    assert au.declencheurs(negatif, [], [], SANS_REPRODUCTION)["tout_negatif"][cle]
    assert not au.declencheurs(negatif[:3] + [dict(negatif[3], libelle=I)], [], [], SANS_REPRODUCTION)["tout_negatif"][cle]
    assert len(au.CONTENU_AUDIT_V2) == len(set(au.CONTENU_AUDIT_V2)) > 7
