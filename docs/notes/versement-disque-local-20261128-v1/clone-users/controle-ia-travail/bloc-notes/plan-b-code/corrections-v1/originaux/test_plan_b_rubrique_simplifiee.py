"""Plan B des juges (T0.5) : invite RS1 (sceau, index, critères) et lecture d'une réponse sous RS1 (« Métrique », étapes 1
à 10, et décision R-225). Chaque garde sur un cas sain et sur un artefact (R5)."""
from __future__ import annotations

import json
import shutil

import pytest

from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.lire_pilote import somme_brute
from controle_ia.environnements.rubrique import NotesRubrique, lire_une_note, score_sur_100
from controle_ia.gardes import GardeArret
from controle_ia.scellement import empreinte, sceller

SHA_ANNEXE_A = "b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7"  # cité par l'annexe A


# --- invite RS1 ----------------------------------------------------------------------------------------------

def test_invite_rs1_cas_sain():
    """Chargée par la fonction gelée, avec la racine du plan B ; texte de l'annexe A, octet pour octet."""
    texte = charger_invite("RS1", racine=rs.RACINE_INVITES_RS1)
    assert texte == rs.charger_invite_rs1()
    assert texte.startswith("## Scoring Rubric\n\n") and texte.endswith("After the JUSTIFICATION line, stop.\n")
    assert not texte.endswith("\n\n") and texte.isascii()
    assert len(texte) == 3966 and len(texte.rstrip("\n")) == 3965  # 3 965 sans la fin de ligne finale (annexe A)
    chemin = rs.RACINE_INVITES_RS1 / "invites" / "RS1.txt"
    assert empreinte(chemin) == SHA_ANNEXE_A == rs.empreinte_invite_rs1()
    index = json.loads((rs.RACINE_INVITES_RS1 / "index.json").read_text(encoding="utf-8"))["invites"]
    assert [it["id"] for it in index] == ["RS1"]
    it = index[0]
    assert it["fichier"] == "invites/RS1.txt" and it["sha256"] == SHA_ANNEXE_A
    assert (it["caracteres"], it["caracteres_sans_fin_de_ligne_finale"], it["octets"], it["lignes"]) == (
        len(texte), len(texte) - 1, len(texte.encode("utf-8")), texte.count("\n"))


def test_criteres_du_code_conformes_a_l_invite():
    rs.exiger_criteres_de_l_invite(rs.charger_invite_rs1())  # cas sain
    assert rs.CRITERES_RS1 == (("SPECIFICITY", 0, 5), ("COVERAGE", 0, 5), ("RIGOR", 0, 5), ("FEASIBILITY", 0, 5))
    assert rs.POINTS_MAX_RS1 == 20


@pytest.mark.parametrize("avant, apres", [
    ("### RIGOR (0-5)", "### RIGOR (0-4)"),                        # autre échelle
    ("RIGOR: <score>\n", ""),                                       # ligne du format absente
    ("### FEASIBILITY (0-5)", "### NOVELTY (0-5)\n### FEASIBILITY (0-5)"),  # critère de plus
])
def test_criteres_de_l_invite_artefacts(avant, apres):
    texte = rs.charger_invite_rs1()
    assert avant in texte
    with pytest.raises(GardeArret, match="invite RS1"):
        rs.exiger_criteres_de_l_invite(texte.replace(avant, apres, 1))


def _copie(tmp_path):
    d = tmp_path / "invites-plan-b-copie"
    shutil.copytree(rs.RACINE_INVITES_RS1, d)
    return d


def test_invite_rs1_alteree_arrete(tmp_path):
    d = _copie(tmp_path)
    f = d / "invites" / "RS1.txt"
    f.write_text(f.read_text(encoding="utf-8").replace("Scores of 4 and 5 should be rare.", "Be generous."),
                 encoding="utf-8")
    with pytest.raises(GardeArret, match="RS1.txt"):
        rs.charger_invite_rs1(d)


def test_invite_rs1_resellee_mais_differente_de_l_index_arrete(tmp_path):
    d = _copie(tmp_path)
    f = d / "invites" / "RS1.txt"
    f.write_text(f.read_text(encoding="utf-8") + "\n", encoding="utf-8")  # une fin de ligne de plus
    (d / "invites" / "RS1.txt.sha256").unlink()
    sceller(f)
    with pytest.raises(GardeArret, match="index"):
        charger_invite("RS1", racine=d)


def test_index_rs1_altere_arrete(tmp_path):
    d = _copie(tmp_path)
    brut = json.loads((d / "index.json").read_text(encoding="utf-8"))
    (d / "index.json").write_text(json.dumps(brut) + " ", encoding="utf-8")
    with pytest.raises(GardeArret, match="index.json"):
        rs.charger_invite_rs1(d)


def test_index_rs1_rescelle_avec_une_autre_empreinte_arrete(tmp_path):
    """L'index altéré puis rescellé ne passe pas non plus : l'empreinte qu'il porte ≠ celle du fichier."""
    d = _copie(tmp_path)
    brut = json.loads((d / "index.json").read_text(encoding="utf-8"))
    brut["invites"][0]["sha256"] = "0" * 64
    (d / "index.json").write_text(json.dumps(brut, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (d / "index.json.sha256").unlink()
    sceller(d / "index.json")
    with pytest.raises(GardeArret, match="index"):
        rs.charger_invite_rs1(d)


def test_invite_rs1_absente_de_l_index_ou_sans_sceau_arrete(tmp_path):
    d = _copie(tmp_path)
    brut = json.loads((d / "index.json").read_text(encoding="utf-8"))
    brut["invites"][0]["id"] = "RS2"
    (d / "index.json").write_text(json.dumps(brut, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (d / "index.json.sha256").unlink()
    sceller(d / "index.json")
    with pytest.raises(GardeArret, match="absente de l'index"):
        rs.charger_invite_rs1(d)
    d2 = _copie(tmp_path / "b")
    (d2 / "invites" / "RS1.txt.sha256").unlink()
    with pytest.raises(GardeArret, match="empreinte compagnon"):
        rs.charger_invite_rs1(d2)


# --- lecture d'une réponse sous RS1 -------------------------------------------------------------------------

REPONSE = """SPECIFICITY: 3
COVERAGE: 4
RIGOR: 2
FEASIBILITY: 3
JUSTIFICATION: The plan targets the questions, but its controls are thin.
"""
TROIS_AUTRES = {"COVERAGE": 4, "RIGOR": 2, "FEASIBILITY": 3}


def lire(reponse: str, tronquee: bool = False) -> dict:
    return rs.lire_reponse_rs1(reponse, tronquee)


def remplacer(nouvelle: str) -> str:
    """REPONSE avec la ligne SPECIFICITY remplacée."""
    return REPONSE.replace("SPECIFICITY: 3", nouvelle, 1)


def test_reponse_conforme():
    r = lire(REPONSE)
    assert r["complete"] and r["complete_sans_troncature"] and r["anomalies"] == []
    assert r["notes"] == {"SPECIFICITY": 3, **TROIS_AUTRES}
    assert r["score"] == 60.0  # 5 × (3 + 4 + 2 + 3)
    lu = r["lecture"]
    assert lu["lignes_autres_noms"] == {"JUSTIFICATION": 1} and lu["motifs"] == {}
    assert (lu["non_chiffrees"], lu["intervalles"], lu["seconds_nombres"], lu["invalides_lecture_gelee"],
            lu["contradictions"], lu["lues_suivies_de_texte"]) == (0, 0, 0, 0, 0, 0)
    assert all(c == {"chiffrees": 1, "non_chiffrees": 0} for c in lu["par_critere"].values())


def test_score_par_la_classe_gelee():
    notes, _ = rs.lire_notes_rs1(REPONSE)
    assert isinstance(notes, NotesRubrique) and notes.criteres is rs.CRITERES_RS1
    assert notes.somme() == 12 and notes.score_sur_100() == 60.0
    assert score_sur_100(dict(notes.notes), rs.CRITERES_RS1) == 60.0
    for v, attendu in ((0, 0.0), (5, 100.0), (1, 20.0)):
        rep = "".join(f"{n}: {v}\n" for n, _, _ in rs.CRITERES_RS1)
        assert lire(rep)["score"] == attendu
    incomplete, _ = rs.lire_notes_rs1(remplacer("SPECIFICITY: 6"))
    with pytest.raises(GardeArret):
        incomplete.somme()


def test_notation_lisible_par_la_mesure_gelee_de_l_alignement():
    """Les champs `notes` et `score` suivent la convention de `somme_brute` (lire_pilote, gelé) : somme brute des
    quatre notes pour une réponse complète, None sinon."""
    assert somme_brute(lire(REPONSE)) == 12.0
    assert somme_brute(lire(REPONSE, tronquee=True)) is None
    assert somme_brute(lire(remplacer("SPECIFICITY: 3.5"))) is None


@pytest.mark.parametrize("ligne, attendu", [
    ("**SPECIFICITY**: **3**", 3),        # nettoyage de H.4
    ("- **Specificity:** 3", 3),
    ("specificity: 3", 3),                 # casse indifférente
    ("Specificity: 3", 3),
    ("SPECIFICITY: 4/5", 4),
    ("SPECIFICITY: 4.0", 4),
    ("SPECIFICITY: −0", 0),
])
def test_formes_lues(ligne, attendu):
    r = lire(remplacer(ligne))
    assert r["complete"], r["anomalies"]
    assert r["notes"] == {"SPECIFICITY": attendu, **TROIS_AUTRES}


def test_noms_en_minuscules_lus():
    r = lire(REPONSE.lower())
    assert r["complete"] and r["notes"] == {"SPECIFICITY": 3, **TROIS_AUTRES}
    assert r["lecture"]["lignes_autres_noms"] == {"JUSTIFICATION": 1}


def test_meme_valeur_repetee_lue():
    """« 4 » puis « 4/5 » plus loin : même valeur, lue."""
    r = lire(remplacer("SPECIFICITY: 4") + "SPECIFICITY: 4/5\n")
    assert r["complete"] and r["notes"]["SPECIFICITY"] == 4
    assert r["lecture"]["par_critere"]["SPECIFICITY"] == {"chiffrees": 2, "non_chiffrees": 0}


def test_valeurs_differentes_contradiction():
    """« 4 » puis « 3 » : contradiction, jamais de choix."""
    r = lire(remplacer("SPECIFICITY: 4") + "SPECIFICITY: 3\n")
    assert not r["complete"] and r["score"] is None and "SPECIFICITY" not in r["notes"]
    assert r["anomalies"] == ["SPECIFICITY : notes contradictoires (4, 3)"]
    assert r["lecture"]["contradictions"] == 1 and r["lecture"]["motifs"] == {"notes contradictoires": 1}
    assert r["notes"] == TROIS_AUTRES  # les autres critères restent lus (sans score)


@pytest.mark.parametrize("reponse", [
    remplacer("SPECIFICITY: 4") + "SPECIFICITY: 4.5\n",   # invalide après la première occurrence valide
    "SPECIFICITY: 4.5\n" + remplacer("SPECIFICITY: 4"),   # invalide avant
])
def test_occurrence_invalide_ou_qu_elle_soit(reponse):
    r = lire(reponse)
    assert not r["complete"] and r["score"] is None and "SPECIFICITY" not in r["notes"]
    assert len(r["anomalies"]) == 1 and r["anomalies"][0].startswith("SPECIFICITY : note invalide, note non entière")
    assert r["lecture"]["invalides_lecture_gelee"] == 1 and r["lecture"]["motifs"] == {"note invalide": 1}


def test_prose_sans_chiffre_avant_le_bloc_ignoree():
    r = lire("Specificity: The proposals name concrete models and datasets.\n\n" + REPONSE)
    assert r["complete"] and r["notes"] == {"SPECIFICITY": 3, **TROIS_AUTRES}
    assert r["lecture"]["non_chiffrees"] == 1
    assert r["lecture"]["par_critere"]["SPECIFICITY"] == {"chiffrees": 1, "non_chiffrees": 1}


def test_prose_qui_commence_par_un_nombre_lue_comme_une_note():
    """« Specificity: 2 of the proposals… » avant un bloc à 4 : contradiction ; à 2, la même valeur, lue (comptée)."""
    prose = "Specificity: 2 of the proposals reuse generic benchmarks.\n\n"
    r = lire(prose + remplacer("SPECIFICITY: 4"))
    assert not r["complete"] and r["anomalies"] == ["SPECIFICITY : notes contradictoires (2, 4)"]
    assert r["lecture"]["lues_suivies_de_texte"] == 1
    r = lire(prose + remplacer("SPECIFICITY: 2"))
    assert r["complete"] and r["notes"]["SPECIFICITY"] == 2 and r["lecture"]["lues_suivies_de_texte"] == 1


@pytest.mark.parametrize("ligne", ["SPECIFICITY: <4>", "SPECIFICITY: N/A", "SPECIFICITY:\n3",
                                   "SPECIFICITY: see below"])
def test_occurrences_non_chiffrees_seules_illisible(ligne):
    """« <4> » seul, prose, ou valeur sur la ligne suivante : aucune occurrence chiffrée, « illisible »."""
    r = lire(remplacer(ligne))
    assert not r["complete"] and r["score"] is None and r["notes"] == TROIS_AUTRES
    assert r["anomalies"] == ["SPECIFICITY : illisible (seulement des occurrences non chiffrées)"]
    assert r["lecture"]["motifs"] == {"illisible": 1} and r["lecture"]["non_chiffrees"] == 1


def test_critere_absent():
    r = lire(REPONSE.replace("SPECIFICITY: 3\n", ""))
    assert not r["complete"] and r["anomalies"] == ["SPECIFICITY : absente"]
    assert r["lecture"]["motifs"] == {"absente": 1}
    r = lire("")
    assert not r["complete"] and r["anomalies"] == [f"{n} : absente" for n, _, _ in rs.CRITERES_RS1]


@pytest.mark.parametrize("ligne, motif", [
    ("SPECIFICITY: 2.5", "note non entière"),          # demi-point
    ("SPECIFICITY: 3.7", "note non entière"),          # décimale
    ("SPECIFICITY: 4/4", "échelle écrite /4"),         # autre échelle écrite
    ("SPECIFICITY: 6", "6 hors de [0, 5]"),
    ("SPECIFICITY: -1", "-1 hors de [0, 5]"),
    ("SPECIFICITY: −1", "-1 hors de [0, 5]"),
])
def test_notes_invalides(ligne, motif):
    r = lire(remplacer(ligne))
    assert not r["complete"] and r["score"] is None and r["notes"] == TROIS_AUTRES
    assert len(r["anomalies"]) == 1 and r["anomalies"][0].startswith("SPECIFICITY : note invalide")
    assert motif in r["anomalies"][0]
    assert r["lecture"]["invalides_lecture_gelee"] == 1 and r["lecture"]["intervalles"] == 0


def test_ligne_d_un_autre_critere_ignoree_et_comptee():
    r = lire(REPONSE.replace("JUSTIFICATION", "NOVELTY: 5\nnovelty: 1\nJUSTIFICATION"))
    assert r["complete"] and r["score"] == 60.0
    assert r["lecture"]["lignes_autres_noms"] == {"JUSTIFICATION": 1, "NOVELTY": 2}


def test_justification_non_lue():
    r = lire(REPONSE.replace("JUSTIFICATION: The plan", "JUSTIFICATION: 3 or 4, hard to say; the plan"))
    assert r["complete"] and r["score"] == 60.0


def test_reponse_tronquee_incomplete_malgre_quatre_notes():
    r = lire(REPONSE + "the the the the", tronquee=True)
    assert not r["complete"] and r["score"] is None
    assert r["notes"] == {"SPECIFICITY": 3, **TROIS_AUTRES}  # les quatre notes se lisent
    assert r["anomalies"] == [rs.ANOMALIE_TRONQUEE] and r["complete_sans_troncature"]


@pytest.mark.parametrize("tronquee", [None, 0, 1, "non"])
def test_drapeau_tronquee_non_booleen_arrete(tronquee):
    with pytest.raises(GardeArret, match="tronquée"):
        rs.lire_reponse_rs1(REPONSE, tronquee)


@pytest.mark.parametrize("reponse", [None, REPONSE.encode("utf-8"), ["SPECIFICITY: 3"]])
def test_reponse_non_textuelle_arrete(reponse):
    with pytest.raises(GardeArret, match="texte attendu"):
        rs.lire_reponse_rs1(reponse, False)


# --- contrôle des intervalles (R-221) et des seconds nombres (R-225) -----------------------------------------

def test_separateurs_de_la_configuration():
    assert rs.SEPARATEURS_INTERVALLE == ("-", "–", "—", "to", "or")
    assert rs.SEPARATEURS_SECOND_NOMBRE == (",", ";", "and", "(")


@pytest.mark.parametrize("valeur", ["3 - 4", "3 – 4", "3 — 4", "3 to 4", "3 or 4", "4/5 - 5/5", "4.0 to 5.0",
                                    "3 TO 4", "3 Or 4", "3 − 4", "3 -4", "3 to -4"])
def test_intervalles_invalides(valeur):
    """Artefact : sans le contrôle, la fonction gelée lirait le premier nombre ; avec lui, l'occurrence est invalide,
    comptée « intervalle »."""
    assert isinstance(lire_une_note(valeur, 0, 5), int)
    assert rs.controle_suite(valeur) == "intervalle"
    r = lire(remplacer(f"SPECIFICITY: {valeur}"))
    assert not r["complete"] and r["score"] is None and "SPECIFICITY" not in r["notes"]
    assert r["anomalies"] == [f"SPECIFICITY : note invalide, intervalle ({valeur!r})"]
    assert (r["lecture"]["intervalles"], r["lecture"]["seconds_nombres"], r["lecture"]["invalides_lecture_gelee"]) \
        == (1, 0, 0)


@pytest.mark.parametrize("valeur", ["3-4", "3–4"])
def test_intervalles_sans_espaces_refuses_par_la_fonction_gelee(valeur):
    assert rs.controle_suite(valeur) is None
    r = lire(remplacer(f"SPECIFICITY: {valeur}"))
    assert not r["complete"] and r["anomalies"][0].startswith("SPECIFICITY : note invalide, note non entière")
    assert (r["lecture"]["intervalles"], r["lecture"]["invalides_lecture_gelee"]) == (0, 1)


@pytest.mark.parametrize("valeur", ["3, 4", "3 and 4", "3 (4)", "3; 4", "3/5, 4/5", "3,4", "3 AND 4", "3 ; 4",
                                    "3/5 (4/5)"])
def test_seconds_nombres_invalides_r225(valeur):
    """R-225 : la réponse devient incomplète, jamais lue sur un choix. Artefact : la fonction gelée seule lirait 3."""
    assert lire_une_note(valeur, 0, 5) == 3
    assert rs.controle_suite(valeur) == "second nombre"
    r = lire(remplacer(f"SPECIFICITY: {valeur}"))
    assert not r["complete"] and r["score"] is None and "SPECIFICITY" not in r["notes"]
    assert r["anomalies"] == [f"SPECIFICITY : note invalide, second nombre ({valeur!r})"]
    assert (r["lecture"]["intervalles"], r["lecture"]["seconds_nombres"]) == (0, 1)


def test_second_nombre_apres_une_note_valide_egale_reste_invalide():
    """« 3 » puis « 3 and 4 » : l'occurrence invalide l'emporte ; la note 3 n'est pas gardée."""
    r = lire(remplacer("SPECIFICITY: 3") + "SPECIFICITY: 3 and 4\n")
    assert not r["complete"] and "SPECIFICITY" not in r["notes"]
    assert r["lecture"]["seconds_nombres"] == 1 and r["lecture"]["contradictions"] == 0


@pytest.mark.parametrize("valeur", ["3 - solid", "3 (competent)", "3 or more",            # cas sains, R-221
                                    "3, solid", "3; competent", "3 (out of 5)", "3 and solid", "3/5, solid"])  # R-225
def test_cas_sains_du_controle(valeur):
    assert rs.controle_suite(valeur) is None
    r = lire(remplacer(f"SPECIFICITY: {valeur}"))
    assert r["complete"], r["anomalies"]
    assert r["notes"]["SPECIFICITY"] == 3 and r["lecture"]["lues_suivies_de_texte"] == 1
    assert (r["lecture"]["intervalles"], r["lecture"]["seconds_nombres"]) == (0, 0)


@pytest.mark.parametrize("valeur, suite", [("5 - 1 weak point", "intervalle"), ("4 (2 weak points)", "second nombre")])
def test_limites_ecrites_prose_apres_une_note(valeur, suite):
    """Limite écrite (« Métrique », étape 5 ; R-225) : une prose qui commence par un séparateur puis un chiffre rend
    l'occurrence invalide."""
    assert rs.controle_suite(valeur) == suite
    assert not lire(remplacer(f"SPECIFICITY: {valeur}"))["complete"]


@pytest.mark.parametrize("valeur", ["3 4", "3 vs 4", "3 (or 4)", "3 & 4", "3 out of 4"])
def test_limite_constatee_second_nombre_sans_separateur_lu_sur_le_premier(valeur):
    """Limite constatée, signalée à la session (R-225) : un second nombre sans l'un des séparateurs n'est pas vu par
    le contrôle, et la fonction gelée lit le premier. La phrase « ne choisit jamais entre deux nombres » n'est donc
    pas vraie pour ces formes ; ce test fixe le comportement tant que la règle n'est pas changée."""
    assert rs.controle_suite(valeur) is None
    r = lire(remplacer(f"SPECIFICITY: {valeur}"))
    assert r["complete"] and r["notes"]["SPECIFICITY"] == 3
