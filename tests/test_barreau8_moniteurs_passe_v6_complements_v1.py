"""Essais complémentaires de la passe de recalcul v6 (barreau 8), demandés par la contre-lecture de conformité
(Sonnet 5.5, `docs/notes/barreau8-code-passe-additif-2-v1/contre-lecture-conformite-passe-v6-comparaison-v2-sonnet-v1.md`,
constats 5, 6 et 9). Le code de la passe n'est pas changé ; les essais de `test_barreau8_moniteurs_passe_v6.py` restent
tels quels (R12). Monde jouet seulement."""
from __future__ import annotations

import dataclasses

import numpy as np
import pytest

from test_barreau8_moniteurs_passe_v6 import (  # noqa: F401  (le monde jouet et ses aides)
    P, VERSIONS, compagnon, ecrire_code, ecrire_scelle, empreinte, monde, refus, trace_d_arret, TEXTE_PREREG)


def _registre_retouche(monde, nom: str, remplacer) -> "Path":
    sain = monde.chemins["registre"].read_text(encoding="utf-8")
    registre = monde.racine / "registres" / f"sondes-iib-v1-{nom}.md"
    texte = remplacer(sain)
    assert texte != sain
    registre.write_text(texte, encoding="utf-8")
    return registre


# --- constat 5 : « strictement postérieure » éprouvé à heure égale -----------------------------------------------

def test_ligne_de_code_a_la_meme_seconde_que_l_additif_2_ne_compte_pas(monde):
    registre = _registre_retouche(monde, "code-meme-seconde", lambda s: s.replace(
        "| CODE-PASSE-IIB | 2026-11-19T03:00:00Z |", "| CODE-PASSE-IIB | 2026-11-19T02:20:00Z |"))
    refus(lambda: monde.passe(registre=registre), "0 ligne.s. CODE-PASSE-IIB strictement postérieure")


def test_additif_2_a_la_meme_seconde_que_l_additif_1_refuse(monde):
    registre = _registre_retouche(monde, "additif-2-meme-seconde", lambda s: s.replace(
        "| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-19T02:20:00Z |", "| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-19T02:10:00Z |"))
    refus(lambda: monde.passe(registre=registre), "SCELLEMENT-ADDITIF-2-SONDES-IIB n'est pas strictement postérieure")


def test_additif_1_a_la_meme_seconde_que_le_texte_refuse(monde):
    registre = _registre_retouche(monde, "additif-1-meme-seconde", lambda s: s.replace(
        "| SCELLEMENT-ADDITIF-1-SONDES-IIB | 2026-11-19T02:10:00Z |", "| SCELLEMENT-ADDITIF-1-SONDES-IIB | 2026-11-19T02:00:00Z |"))
    refus(lambda: monde.passe(registre=registre), "n'est pas la première des lignes de clé|n'est pas strictement postérieure")


def test_posterieure_unitaire():
    a = {"rang": 3, "secondes": 100.0}
    assert P._posterieure({"rang": 4, "secondes": 101.0}, a)
    assert not P._posterieure({"rang": 4, "secondes": 100.0}, a)          # même seconde
    assert not P._posterieure({"rang": 3, "secondes": 101.0}, a)          # même rang
    assert not P._posterieure({"rang": 2, "secondes": 101.0}, a)


# --- constat 6 : la garde E = 1 de la clause (a), éprouvée seule ----------------------------------------------------

def test_garde_p3_structure_refuse_e_different_de_1(monde):
    t = P.TraceGardes()
    refus(lambda: P.garde_p3_structure(dataclasses.replace(monde.spec, episodes_par_tache=2),
                                       P.lire_identifiants(monde.chemins["ids"]), monde.taches, t), "E ≠ 1")
    assert t.etat("P3") == "non tenue"


# --- constat 9 : variantes symétriques ------------------------------------------------------------------------------

def test_additif_2_altere_apres_sa_ligne(monde):
    copie = monde.racine / "prereg" / "additif-2-copie-v1.md"
    ecrire_scelle(copie, TEXTE_PREREG.replace("Texte jouet de la section.", "Additif 2 copie.", 1))
    registre = ecrire_code(monde.racine, "additif-2-copie", additif_2=copie)
    assert monde.passe(registre=registre, mode="entrees")["entrees"] == "conformes"           # sain avant l'altération
    copie.write_text(copie.read_text(encoding="utf-8") + "\nAjout.\n", encoding="utf-8")
    refus(lambda: monde.passe(registre=registre), "empreinte .* ≠ scellée")


def test_cle_transformers_seule_absente_de_l_extrait(monde):
    course = monde.course_modifiee("v-sans-transformers", modifier_extrait=lambda e: e.update(
        versions=dict(sorted({"numpy": np.__version__, "tokenizers": VERSIONS["tokenizers"]}.items()))))
    chargeur = monde.chargeur()
    p = monde.params(extrait=course["extrait"])
    refus(lambda: P.executer_passe(p, monde.spec_de(p.extrait), chargeur), "clé transformers absente")
    assert trace_d_arret(p.sortie)["gardes"]["P3"]["actions_controlees"] == 0 and chargeur.tok is None


@pytest.mark.parametrize("adaptateur", ["eleve", "temoin-jumeau"])
def test_adaptateur_d_une_autre_empreinte_que_l_extrait(monde, adaptateur):
    nom = P.SPECIFICATION_TEXTE.fichiers_adaptateurs
    fichier = dict(nom)[adaptateur]
    course = monde.course_modifiee(f"adaptateur-autre-{adaptateur}", modifier_extrait=lambda e: e["fichiers_de_la_passe"].update(
        {k: "a" * 64 for k in e["fichiers_de_la_passe"] if k.endswith(fichier)}))
    refus(lambda: monde.passe(extrait=course["extrait"]), f"{fichier} : empreinte sur disque ≠ empreinte de l'extrait")


def test_adaptateur_sans_compagnon(monde):
    course = monde.course_modifiee("adaptateur-sans-compagnon")
    compagnon(course["adaptateur_temoin_jumeau"]).unlink()
    refus(lambda: monde.passe(extrait=course["extrait"]), "empreinte compagnon .* absente")
