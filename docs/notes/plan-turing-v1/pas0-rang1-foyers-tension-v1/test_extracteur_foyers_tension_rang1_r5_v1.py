"""Essais unitaires R5 (cas sains et artefacts / témoins « doit mourir ») pour l'extracteur Rang 1 v1."""
from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import pytest

DOSSIER_COURANT = Path(__file__).resolve().parent
if str(DOSSIER_COURANT) not in sys.path:
    sys.path.insert(0, str(DOSSIER_COURANT))

import extracteur_foyers_tension_rang1_v1 as ext  # noqa: E402


def test_r5_garde1_prereg_sain_et_artefact(tmp_path: Path) -> None:
    """Teste la garde n° 1 sur le vrai préenregistrement scellé (sain) et sur un fichier altéré (artefact)."""
    vrai_prereg = DOSSIER_COURANT / "prereg-pas0-rang1-retrodiction-foyers-tension-2024-vers-2025-2026-v1.md"
    sha = ext.verifier_prereg_scelle(vrai_prereg, ext.EMPREINTE_PREREG_ATTENDUE)
    assert sha == ext.EMPREINTE_PREREG_ATTENDUE

    # Artefact 1 : fichier altéré d'un caractère par rapport à son compagnon .sha256
    copie = tmp_path / vrai_prereg.name
    copie_sha = tmp_path / (vrai_prereg.name + ".sha256")
    copie.write_text(vrai_prereg.read_text(encoding="utf-8") + "\naltération\n", encoding="utf-8")
    copie_sha.write_text(Path(str(vrai_prereg) + ".sha256").read_text(encoding="utf-8"), encoding="utf-8")
    with pytest.raises(ext.ErreurGardeRang1, match="Garde n° 1"):
        ext.verifier_prereg_scelle(copie, ext.EMPREINTE_PREREG_ATTENDUE)

    # Artefact 2 : empreinte attendue incorrecte
    with pytest.raises(ext.ErreurGardeRang1, match="différente de l'empreinte attendue"):
        ext.verifier_prereg_scelle(vrai_prereg, "0" * 64)


def test_r5_garde2_orthogonalite_sain_et_artefacts() -> None:
    """Teste la garde n° 2 sur les vocabulaires sains puis sur trois types d'artefacts de collision."""
    # Cas sain : aucune exception
    ext.verifier_orthogonalite_lexicale()

    # Artefact A : inclusion directe tension -> axes ("superficial unlearning" active "unlearning")
    tension_fautive = {k: list(v) for k, v in ext.TENSION.items()}
    tension_fautive["S4"] = tension_fautive["S4"] + ["superficial unlearning"]
    with pytest.raises(ext.ErreurGardeRang1, match="Garde n° 2"):
        ext.verifier_orthogonalite_lexicale(tension=tension_fautive)

    # Artefact B : recouvrement suffixe-préfixe ("vulnerable to adaptive" + "adaptive attack")
    tension_chevauchante = {k: list(v) for k, v in ext.TENSION.items()}
    tension_chevauchante["S4"] = tension_chevauchante["S4"] + ["vulnerable to adaptive"]
    with pytest.raises(ext.ErreurGardeRang1, match="recouvrement suffixe-préfixe"):
        ext.verifier_orthogonalite_lexicale(tension=tension_chevauchante)

    # Artefact C : inclusion croisée inter-axes ("automated jailbreak" dans AXE_15 vs "jailbreak" dans AXE_06)
    axes_fautifs = {k: list(v) for k, v in ext.AXES.items()}
    axes_fautifs["AXE_15"] = axes_fautifs["AXE_15"] + ["automated jailbreak"]
    with pytest.raises(ext.ErreurGardeRang1, match="inclusion inter-axes"):
        ext.verifier_orthogonalite_lexicale(axes=axes_fautifs)


def test_r5_cesures_preuves_f1_et_troncature_bibliographique() -> None:
    """Vérifie le recollage de césures, le motif F1 sur 'Proof of Theorem 2.1.' et l'exclusion de References."""
    analyseur = ext.AnalyseurLexicalCompile()
    remplissage = " ".join(["empirical analysis of neural network representation"] * 80)

    # Cas sain : césures en fin de ligne + Proof of Theorem 2.1. + pièges après References
    flux = (
        "Title: Language model interpretability with linear probes and sparse autoencoders.\n"
        "We study game-\ntheoretic framework and ad-\nhoc heuristics that fail to general-\nize.\n"
        "Theorem 2.1.1. Every minimax bound holds.\n"
        "Proof of Theorem 2.1.1. Direct calculation.\n"
        f"{remplissage}\n"
        "References\n"
        "Smith (2023). Impossibility theorem and canonical decomposition with workaround and paradox.\n"
    )
    entree = {
        "cle_canonique": "arxiv:2401.00001",
        "chemin_relatif": "2401.00001v1.pdf",
        "sha256": "a" * 64,
        "annee_nominale": 2024,
        "rang_version": 1.0,
        "source_annee": "arxiv_moderne",
    }
    doc = analyseur.analyser_document(entree, flux)
    assert doc["biblio_tronquee"] is True
    assert doc["eligible_primaire"] is True
    # "ad-hoc" et "heuristics" dans S1, "fail to generalize" dans S2, mais PAS "workaround" ni "paradox" (dans References)
    assert doc["densites_s"]["S1"] > 0.0
    assert doc["densites_s"]["S2"] > 0.0
    assert doc["densites_s"]["S3"] == 0.0
    # Theorem 2.1.1 + Proof of Theorem 2.1.1. = 2 correspondances F1 ; "game-theoretic framework" + "minimax" = 2 dans F2 ; F3 = 0 (car canonical decomposition est après References)
    assert doc["details_termes_f"]["F1_enonces_et_preuves"] == 2
    assert doc["densites_f"]["F2"] > 0.0
    assert doc["densites_f"]["F3"] == 0.0

    # Artefact : faux en-tête "References" dans le sommaire tout au début (< 35 % du texte) -> ne doit PAS tronquer !
    flux_sommaire = (
        "Contents\nReferences\n"
        "Language model safety and jailbreak defense with guardrails.\n"
        f"{remplissage}\n"
        "We observe a puzzling paradox in our experiments.\n"
    )
    dec = ext.normaliser_et_decouper_texte(flux_sommaire, 2024)
    assert dec["biblio_tronquee"] is False
    assert "puzzling paradox" in dec["corps_principal"]


def test_r5_datation_dedoublonnage_et_fuite_revision_post_2024(tmp_path: Path) -> None:
    """Teste la priorité des versions v1 vs v3, le max d'en-tête hors prospectif et le masque arXiv:2403.02025."""
    # 1. En-tête citant 2017 et une mention prospective "by 2026" mais publié en 2025
    entete = "Following Christiano et al. (2017), published in ICML 2025, safety roadmap by 2026."
    assert ext.inferer_millesime_entete(entete) == 2025

    # 2. Faux positif potentiel arXiv:2403.02025 vs vraie révision 2025
    sain_24 = ext.normaliser_et_decouper_texte("arXiv:2403.02025v1 [cs.LG] 4 Mar 2024\n" + "mot " * 300, 2024)
    assert sain_24["revision_post_2024"] is False

    rev_25 = ext.normaliser_et_decouper_texte("arXiv:2410.12345v3 [cs.AI] 18 Feb 2025\n" + "mot " * 300, 2024)
    assert rev_25["revision_post_2024"] is True

    # 3. Dédoublonnage arXiv : v1 retenue pour <=2024, v3 retenue pour >=2025
    for nom in ("2405.11111v1.pdf", "2405.11111v3.pdf", "2506.22222v1.pdf", "2506.22222v3.pdf"):
        (tmp_path / nom).write_bytes(nom.encode("utf-8"))
    retenus, res_inv = ext.inventorier_et_dedoublonner_pdfs(tmp_path)
    par_cle = {r["cle_canonique"]: r["chemin_relatif"] for r in retenus}
    assert res_inv["documents_canoniques_uniques"] == 2
    assert par_cle["arxiv:2405.11111"] == "2405.11111v1.pdf"
    assert par_cle["arxiv:2506.22222"] == "2506.22222v3.pdf"


def test_r5_cas_limites_statistiques_et_gardes_4_et_5() -> None:
    """Teste le plateau médian, le témoin nul sain/artefact et la garde d'effectif minimal n° 4."""
    # 1. Plateau supérieur atteignant la médiane : [0, 0, 0, 0, 0.25 x 6] -> repli >= médiane
    arr_plateau = np.array([0.0, 0.0, 0.0, 0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
    z_bin, med, mode = ext.binariser_mediane_avec_repli(arr_plateau)
    assert med == 0.25
    assert mode == "repli_superieur_ou_egal_plateau"
    assert int(np.sum(z_bin)) == 6

    # 2. Témoin nul sain sur 14 sous-domaines
    rng = np.random.default_rng(np.random.SeedSequence(2026112401).spawn(1)[0])
    x_sain = np.linspace(-1.0, 1.5, 14)
    y_sain = np.array([0.0, 0.1, 0.15, 0.2, 0.2, 0.25, 0.3, 0.05, 0.4, 0.35, 0.1, 0.5, 0.25, 0.3])
    res_nul = ext.verifier_temoin_nul_doit_mourir(x_sain, y_sain, rng, n_sim=2000, n_perm_interne=300)
    assert 0.47 <= res_nul["auc_moyenne_nul"] <= 0.53
    assert res_nul["taux_erreur_premiere_espece"] <= 0.070

    # 3. Artefact garde n° 4 : moins de 40 documents éligibles -> lève ErreurGardeRang1
    with pytest.raises(ext.ErreurGardeRang1, match="Garde n° 4"):
        ext.evaluer_protocole_sur_documents([], executer_gardes_4_et_5=True)

    # 4. Artefact garde n° 5 (« doit mourir ») : fuite simulée biaisant A(X, Z) sous H0 -> lève ErreurGardeRang1
    vrai_auc = ext.aire_sous_courbe_exacte
    try:
        ext.aire_sous_courbe_exacte = lambda s, c: 0.68  # fuite simulée sous H0
        with pytest.raises(ext.ErreurGardeRang1, match="Garde n° 5"):
            ext.verifier_temoin_nul_doit_mourir(x_sain, y_sain, rng, n_sim=200, n_perm_interne=100)
    finally:
        ext.aire_sous_courbe_exacte = vrai_auc


def test_r5_garde3_panne_massive_extraction_pdf(tmp_path: Path) -> None:
    """Teste la garde n° 3 lorsqu'un dossier de faux PDF corrompus échoue à plus de 15 % dans pdftotext."""
    vrai_prereg = DOSSIER_COURANT / "prereg-pas0-rang1-retrodiction-foyers-tension-2024-vers-2025-2026-v1.md"
    faux_dossier_pdf = tmp_path / "pdfs_corrompus"
    faux_dossier_pdf.mkdir()
    for idx in range(5):
        (faux_dossier_pdf / f"2401.0000{idx}v1.pdf").write_bytes(b"NOT_A_VALID_PDF_BINARY")
    sortie = tmp_path / "out.json"
    with pytest.raises(ext.ErreurGardeRang1, match="Garde n° 3"):
        ext.executer_pipeline_complet(vrai_prereg, faux_dossier_pdf, sortie, nb_travailleurs=2)


