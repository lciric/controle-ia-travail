"""Essais unitaires selon la règle numéro 5 pour `remplir_additif_commit_sondes_v2_v1.py` et pour
`diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon1.md` :
- cas sain complet (déterminisme octet pour octet, conformité à `controle_ia.prereg.exiger_prereg_scelle`, modes
  `jonction_tardive`, `rejeu_non_calculable` et brouillon déjà contre-lu) ;
- artefact 1 : marqueur résiduel (`<MARQUEUR_OUBLIE_TEST>`, `<<GABARIT_OUBLIE>>`, `À REMPLIR`, ou marqueur obligatoire
  manquant) rejeté par `GardeArret` sans écriture sur disque ;
- artefact 2 : empreinte invalide (compagnon `.sha256` corrompu de la note des effectifs, du brouillon, du rapport de
  contre-lecture ou de la table de correspondance, ou `attendu_sha256_note` mal formé / discordant) rejetée par
  `GardeArret` sans écriture sur disque ;
- gardes complémentaires : cas mixte du contrôle du chemin non tranché, refus d'écrasement (règle numéro 12), refus de
  chemin absolu dans le dépôt.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from controle_ia import prereg
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
import remplir_additif_commit_sondes_v2_v1 as rac

DOSSIER_SCRATCH = Path(__file__).resolve().parent
BROUILLON_REEL = DOSSIER_SCRATCH / "diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon1.md"


def _fabriquer_note_effectifs(chemin: Path, *, cas_mixte: bool = False) -> str:
    taches_ctrl = 4 if cas_mixte else 0
    actions_ctrl = 8 if cas_mixte else 0
    bloc = {
        "format": "note-effectifs-sondes-v2-v1",
        "redigee_par": "session-test-synthetique",
        "date_utc": "2026-11-23T21:40:00Z",
        "aveuglement": {
            "activations": "non ouvertes",
            "scores": "non ouverts",
            "table_de_l_ouvreur": "non ouverte",
            "verdict_adaptateurs_jumeaux": "non ouvert",
        },
        "activations": {
            "dossier_run": "runs/synthetique-test",
            "inventaire_sha256": "a" * 64,
            "garde_sha256": "b" * 64,
            "regle_garde": "une_sur_dix",
            "couches_gardees": [15],
            "chemin_de_calcul": {
                "programme": "relecture_test@0000000",
                "precision": "float16",
                "mode": "relu à texte imposé",
                "gabarit": "defaut",
                "source": "manifeste",
                "identique_pour_toutes_les_series": True,
            },
            "series": [
                {"nom": "nu", "categorie": "nu", "cles": 48},
                {"nom": "s01", "categorie": "adaptateur", "cles": 48},
                {"nom": "propre-s01", "categorie": "propre", "cles": 12},
            ],
            "cles_communes": {
                "definition": "clés de la série nu, identiques dans toute série non propre",
                "actions": 48,
                "taches": 16,
                "taches_par_nombre_d_actions": {"1": 0, "2": 0, "3": 16, "4_ou_plus": 0},
                "distinctes_des_cles_propres": True,
            },
            "nu_relit_les_cles_communes": True,
        },
        "scores_bbis": {
            "table": {
                "chemin": "donnees/synthetique/scores.jsonl",
                "sha256": "c" * 64,
                "ligne_registre": "SCORES-BBIS-SYNTHETIQUE",
            },
            "colonnes": ["dose", "pli", "source", "poids", "tache", "cle", "score", "longueur", "pas"],
            "doses": [
                {
                    "dose": "0.5",
                    "plis": [
                        {
                            "pli": "0",
                            "taches_tenues": 12,
                            "actions": {
                                "adaptateur|saboteur": 36,
                                "nu|saboteur": 36,
                                "adaptateur|honnete": 36,
                                "nu|honnete": 36,
                            },
                            "chemins": {
                                "adaptateur|saboteur": "origine",
                                "nu|saboteur": "relu",
                                "adaptateur|honnete": "relu",
                                "nu|honnete": "origine",
                            },
                            "actions_en_origine_et_en_relu": actions_ctrl,
                            "taches_avec_controle_du_chemin": taches_ctrl,
                        }
                    ],
                },
                {
                    "dose": "1.0",
                    "plis": [
                        {
                            "pli": "0",
                            "taches_tenues": 12,
                            "actions": {
                                "adaptateur|saboteur": 36,
                                "nu|saboteur": 36,
                                "adaptateur|honnete": 36,
                                "nu|honnete": 36,
                            },
                            "chemins": {
                                "adaptateur|saboteur": "origine",
                                "nu|saboteur": "relu",
                                "adaptateur|honnete": "relu",
                                "nu|honnete": "origine",
                            },
                            "actions_en_origine_et_en_relu": 0,
                            "taches_avec_controle_du_chemin": 0,
                        }
                    ],
                },
            ],
            "nombre_de_doses": 2,
        },
        "cases_de_l_epreuve_plantee": {
            "etalon": {"taches": 16, "actions": 3},
            "complet": {"paires": 8, "taches": 12, "actions": 3, "doses_holm": 2},
            "extension_taches_actions": False,
        },
        "minimums": {
            "cles_communes": "atteints",
            "rejeu_par_dose": {"0.5": "atteints", "1.0": "atteints"},
        },
        "reserves": [],
    }
    md = (
        "# Note des effectifs synthétique (essai R5)\n\n"
        "```json\n"
        + json.dumps(bloc, ensure_ascii=False, indent=1)
        + "\n```\n"
    )
    chemin.write_text(md, encoding="utf-8")
    return sceller(chemin)


def _fabriquer_correspondance(chemin: Path) -> str:
    corps = {
        "format": "correspondance-rejeu-croise-v1",
        "redigee_par": "session-test-synthetique",
        "date_utc": "2026-11-23T21:41:00Z",
        "attestation": "aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes",
        "table_source": {
            "chemin": "donnees/synthetique/scores.jsonl",
            "sha256": "c" * 64,
            "ligne_registre": "SCORES-BBIS-SYNTHETIQUE",
            "format_fichier": "jsonl",
        },
        "selection": {},
        "colonnes": {
            "dose": "dose",
            "pli": "pli",
            "source": "source",
            "poids": "poids",
            "chemin": {"regle": "quatre_cases_du_texte_scelle"},
            "tache": "tache",
            "cle": "cle",
            "score": "score",
            "longueur": "longueur",
            "pas": "pas",
            "valeur_declaree": {"absente": True},
            "tache_tenue": {"constante": True},
        },
        "valeurs": {
            "source": {"sab": "saboteur", "hon": "honnete"},
            "poids": {"adap": "adaptateur", "nu": "nu"},
        },
    }
    chemin.write_text(json.dumps(corps, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return sceller(chemin)


def _fabriquer_rapport_cl(chemin: Path, titre: str) -> str:
    chemin.write_text(f"# {titre}\n\nVerdict : conforme, scellable en l'état.\n", encoding="utf-8")
    return sceller(chemin)


def test_cas_sain_jonction_tardive_determinisme_et_conformite_prereg(tmp_path: Path) -> None:
    note_p = tmp_path / "note-des-effectifs-sondes-v2-v1.md"
    sha_note = _fabriquer_note_effectifs(note_p)
    corr_p = tmp_path / "correspondance-rejeu-croise-v1.json"
    sha_corr = _fabriquer_correspondance(corr_p)
    cl_corr_p = tmp_path / "contre-lecture-correspondance-v1.md"
    _fabriquer_rapport_cl(cl_corr_p, "Contre-lecture de la correspondance synthétique")
    cl_add_p = tmp_path / "contre-lecture-additif-commit-v1.md"
    _fabriquer_rapport_cl(cl_add_p, "Contre-lecture de l'additif de commit")

    sortie_1 = tmp_path / "diagnostics-prealables-sondes-v1-additif-commit-v1.md"
    sortie_2 = tmp_path / "copie-deterministe" / "diagnostics-prealables-sondes-v1-additif-commit-v1.md"

    kwargs = dict(
        brouillon=BROUILLON_REEL,
        note_effectifs=note_p,
        chemin_note_depot="docs/notes/sondes-v2-effectifs-v1/note-des-effectifs-sondes-v2-v1.md",
        date_scellement_utc="2026-11-23T22:00:00Z",
        option_rejeux_nuls=39,
        mode_correspondance="jonction_tardive",
        attendu_sha256_note=sha_note,
        attendu_doses_d=2,
        go_correspondance="GO-2026-11-23-99",
        fichier_correspondance=corr_p,
        chemin_correspondance_depot="docs/notes/sondes-v2-correspondance-v1/correspondance-rejeu-croise-v1.json",
        rapport_cl_correspondance=cl_corr_p,
        chemin_rapport_cl_correspondance_depot="docs/notes/sondes-v2-correspondance-v1/contre-lecture-v1.md",
        rapport_contre_lecture=cl_add_p,
        chemin_rapport_contre_lecture_depot="docs/notes/sondes-v2-additif-commit-v1/contre-lecture-v1.md",
        verdict_contre_lecture="scellable en l'état, aucune remarque bloquante ni majeure.",
    )
    r1 = rac.remplir_et_sceller(sortie=sortie_1, **kwargs)
    r2 = rac.remplir_et_sceller(sortie=sortie_2, **kwargs)

    # Déterminisme strict octet pour octet
    assert sortie_1.read_bytes() == sortie_2.read_bytes()
    assert r1["sha256"] == r2["sha256"]

    # Conformité complète au validateur officiel controle_ia.prereg
    assert prereg.problemes(sortie_1) == []
    assert prereg.exiger_prereg_scelle(sortie_1) == r1["sha256"]

    texte_scelle = sortie_1.read_text(encoding="utf-8")
    assert re.findall(r"<[^>\n]+>", texte_scelle) == []
    assert re.findall(r"<<[^>\n]+>>", texte_scelle) == []
    assert "À REMPLIR" not in texte_scelle
    assert sha_note in texte_scelle
    assert sha_corr in texte_scelle
    assert "au seuil α / D du premier pas de Holm sur les D doses de la note des effectifs" in texte_scelle
    assert "8351e49b4a16a01ffd0a6c6a4d1ffc7bc0f46685" in texte_scelle
    assert "305159624078239919914131004197200342142" in texte_scelle

    # Essai via main() en mode rejeu_non_calculable et option 199, sur un brouillon2 déjà contre-lu
    brouillon2 = tmp_path / "brouillon2.md"
    texte_b2 = BROUILLON_REEL.read_text(encoding="utf-8").replace(
        "<ENTREE_CONTRE_LECTURE_ADDITIF>",
        f"- **Contre-lecture 1** : agent neuf. Brouillon 1 : `{'1'*64}`. Rapport : `{'2'*64}`. Conforme.",
    )
    brouillon2.write_text(texte_b2, encoding="utf-8")
    sceller(brouillon2)
    sortie_3 = tmp_path / "additif-mode-b.md"
    code = rac.main([
        "--brouillon", str(brouillon2),
        "--sortie", str(sortie_3),
        "--note-effectifs", str(note_p),
        "--chemin-note-depot", "docs/notes/sondes-v2-effectifs-v1/note-des-effectifs-sondes-v2-v1.md",
        "--date-scellement-utc", "2026-11-23T22:05:00Z",
        "--option-rejeux-nuls", "199",
        "--mode-correspondance", "rejeu_non_calculable",
    ])
    assert code == 0
    assert prereg.exiger_prereg_scelle(sortie_3)


def test_artefact_marqueur_residuel_ou_manquant(tmp_path: Path) -> None:
    note_p = tmp_path / "note.md"
    _fabriquer_note_effectifs(note_p)
    cl_add_p = tmp_path / "cl.md"
    _fabriquer_rapport_cl(cl_add_p, "Contre-lecture")

    base_texte = BROUILLON_REEL.read_text(encoding="utf-8")

    # 1a. Marqueur résiduel en simples chevrons <MARQUEUR_OUBLIE_TEST>
    b_simple = tmp_path / "brouillon_marqueur_simple.md"
    b_simple.write_text(base_texte + "\nLigne fautive : <MARQUEUR_OUBLIE_TEST>\n", encoding="utf-8")
    sceller(b_simple)
    cible_a = tmp_path / "sortie_interdite_a.md"
    with pytest.raises(GardeArret, match="marqueurs résiduels"):
        rac.remplir_et_sceller(
            brouillon=b_simple,
            sortie=cible_a,
            note_effectifs=note_p,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )
    assert not cible_a.exists()
    assert not cible_a.with_name(cible_a.name + ".sha256").exists()

    # 1b. Marqueur résiduel en doubles chevrons <<GABARIT_OUBLIE>>
    b_double = tmp_path / "brouillon_marqueur_double.md"
    b_double.write_text(base_texte + "\nLigne fautive : <<GABARIT_OUBLIE>>\n", encoding="utf-8")
    sceller(b_double)
    cible_b = tmp_path / "sortie_interdite_b.md"
    with pytest.raises(GardeArret, match="marqueurs résiduels"):
        rac.remplir_et_sceller(
            brouillon=b_double,
            sortie=cible_b,
            note_effectifs=note_p,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )
    assert not cible_b.exists()

    # 1c. Mention prohibée « À REMPLIR »
    b_ar = tmp_path / "brouillon_a_remplir.md"
    b_ar.write_text(base_texte + "\nEncore À REMPLIR ici.\n", encoding="utf-8")
    sceller(b_ar)
    cible_c = tmp_path / "sortie_interdite_c.md"
    with pytest.raises(GardeArret, match="À REMPLIR"):
        rac.remplir_et_sceller(
            brouillon=b_ar,
            sortie=cible_c,
            note_effectifs=note_p,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )
    assert not cible_c.exists()

    # 1d. Marqueur obligatoire absent du brouillon
    b_incomplet = tmp_path / "brouillon_incomplet.md"
    b_incomplet.write_text(base_texte.replace("<SHA256_NOTE_DES_EFFECTIFS>", "texte_ecrase"), encoding="utf-8")
    sceller(b_incomplet)
    with pytest.raises(GardeArret, match="marqueurs obligatoires absents"):
        rac.remplir_et_sceller(
            brouillon=b_incomplet,
            sortie=tmp_path / "sortie_interdite_d.md",
            note_effectifs=note_p,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )


def test_artefact_empreinte_invalide(tmp_path: Path) -> None:
    note_p = tmp_path / "note.md"
    _fabriquer_note_effectifs(note_p)
    cl_add_p = tmp_path / "cl.md"
    _fabriquer_rapport_cl(cl_add_p, "Contre-lecture")

    # 2a. Empreinte attendue mal formée (non hexadécimale 64 signes)
    cible_1 = tmp_path / "sortie_sha_mal_forme.md"
    with pytest.raises(GardeArret, match="64 signes"):
        rac.remplir_et_sceller(
            brouillon=BROUILLON_REEL,
            sortie=cible_1,
            note_effectifs=note_p,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            attendu_sha256_note="empreinte-invalide-courte",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )
    assert not cible_1.exists()

    # 2b. Empreinte attendue de 64 hexadécimaux mais discordante avec la note scellée
    cible_2 = tmp_path / "sortie_sha_discordant.md"
    with pytest.raises(GardeArret, match="différente de l'empreinte vérifiée"):
        rac.remplir_et_sceller(
            brouillon=BROUILLON_REEL,
            sortie=cible_2,
            note_effectifs=note_p,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            attendu_sha256_note="0" * 64,
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )
    assert not cible_2.exists()

    # 2c. Compagnon .sha256 de la note des effectifs altéré sur disque
    note_corrompue = tmp_path / "note_corrompue.md"
    _fabriquer_note_effectifs(note_corrompue)
    note_corrompue.with_name("note_corrompue.md.sha256").write_text(
        f"{'f' * 64}  note_corrompue.md\n", encoding="utf-8"
    )
    cible_3 = tmp_path / "sortie_compagnon_faux.md"
    with pytest.raises(GardeArret):
        rac.remplir_et_sceller(
            brouillon=BROUILLON_REEL,
            sortie=cible_3,
            note_effectifs=note_corrompue,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )
    assert not cible_3.exists()


def test_gardes_cas_mixte_r12_et_chemin_absolu(tmp_path: Path) -> None:
    note_mixte = tmp_path / "note_mixte.md"
    _fabriquer_note_effectifs(note_mixte, cas_mixte=True)
    cl_add_p = tmp_path / "cl.md"
    _fabriquer_rapport_cl(cl_add_p, "Contre-lecture")

    # Cas mixte non tranché : arrêt obligatoire
    with pytest.raises(GardeArret, match="cas mixte détecté"):
        rac.remplir_et_sceller(
            brouillon=BROUILLON_REEL,
            sortie=tmp_path / "sortie_mixte_refusee.md",
            note_effectifs=note_mixte,
            chemin_note_depot="docs/notes/note_mixte.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )

    # Chemin absolu interdit dans chemin_note_depot
    note_saine = tmp_path / "note_saine.md"
    _fabriquer_note_effectifs(note_saine)
    with pytest.raises(GardeArret, match="chemin relatif propre"):
        rac.remplir_et_sceller(
            brouillon=BROUILLON_REEL,
            sortie=tmp_path / "sortie_abs_refusee.md",
            note_effectifs=note_saine,
            chemin_note_depot="/abs/interdit/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )

    # Règle numéro 12 : refus d'écraser une sortie existante
    deja_la = tmp_path / "deja_la.md"
    deja_la.write_text("existant\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="existe déjà"):
        rac.remplir_et_sceller(
            brouillon=BROUILLON_REEL,
            sortie=deja_la,
            note_effectifs=note_saine,
            chemin_note_depot="docs/notes/note.md",
            date_scellement_utc="2026-11-23T22:00:00Z",
            option_rejeux_nuls=39,
            mode_correspondance="rejeu_non_calculable",
            rapport_contre_lecture=cl_add_p,
            chemin_rapport_contre_lecture_depot="docs/notes/cl.md",
            verdict_contre_lecture="conforme",
        )
