"""Essais de la pièce « mots et coût » de T0.6 (`scripts/mots_et_cout_t06_v3.py`) — v3 (fichier neuf, R12 ; les essais v1
restent tels quels). v3 = les essais v1 visant le module v3, le point (c) de la base (B) lu « coût présent » (R-2765), et les
couples de la contre-lecture v2 (`12e6e169…`) : C-1 (codes de sortie 0, 2 et 3 de `main`), C-2 (contre-lecture obligatoire
dans le fichier de `CODE-MOTS-ET-COUT-T06`), C-3 (aucune valeur dans les motifs de `valider_issue` ni sur la sortie).
**Données factices seulement** (`scripts/fabrique_factice_mots_et_cout_t06_v1.py`, inchangée) ; aucun fichier de 7a, 7b,
T0.7 ou P3 n'est lu. La configuration de T0.7 n'est pas ouverte : ses marques sont recopiées de la contre-lecture v2, § 5
(`MARQUES_T07`).

- Phrases, empreintes et constantes recopiées des textes scellés (base (A) `72b067d5…`, T0.6 `ef31feff…`), modules gelés égaux
  au commit `1609a4bf` ;
- chaque garde éprouvée sur un **cas sain** et sur un **artefact** (R5) : modules gelés, textes, liste blanche, empreintes des
  entrées, effectifs, ensemble des tâches, cohérence des textes, manifeste de 7b, T6-10, colonnes des traits, centres, plis,
  score non fini, convergence, lecture de transfert, registre (lignes, code, journal), arbre de travail, sortie existante,
  fichier de l'issue, JSON sans NaN, options refusées en mode réel ;
- les six preuves du plan de la base (A), point 8 (i) à (vi) ;
- compatibilité : lecteur de T0.7 (`lecture_v1.lire_issue_mots_et_cout`, `criteres_v1.deriver_classe`, `registre_v1`) et
  clés que lit la lecture de T0.8 (brouillon du compte 4) ; contrat de M2 et MC ; reproductibilité ;
- mode réel de bout en bout par le lanceur, dans un dépôt jetable (registre, ligne `CODE-MOTS-ET-COUT-T06`, code au commit).

    PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_mots_et_cout_t06_v3.py
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pytest

RACINE = Path(__file__).resolve().parents[1]
MODULE = RACINE / "scripts" / "mots_et_cout_t06_v3.py"
FABRIQUE = RACINE / "scripts" / "fabrique_factice_mots_et_cout_t06_v1.py"
LANCEUR = RACINE / "scripts" / "lancer_mots_et_cout_t06_v3.sh"
RUN = "20261114-120000-t06-factice"
TEXTES = ("prereg/T0.8-base-A-mots-et-cout-v1.md", "prereg/T0.6-organismes-v0-v1.md")
CONTRE_LECTURE = "docs/notes/contre-lecture-factice-v1.md"          # C-2 : contre-lecture FACTICE des dépôts jetables
# Marques des autres tâches du lecteur de registre de T0.7 (`marques_autres_taches` de sa configuration v8), recopiées de la
# contre-lecture v2, § 5 : la configuration de T0.7 n'est pas ouverte par ces essais (consigne du développeur v3).
MARQUES_T07 = ["T06", "T08", "P3BIS", "NARC"]


def _charger(nom: str, chemin: Path):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


mc = _charger("mots_et_cout_t06_v3", MODULE)
fab = _charger("fabrique_factice_mots_et_cout_t06_v1", FABRIQUE)
M = mc.charger_modules_geles()


def git(racine, *args):
    return subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True, text=True).stdout


def depot_jouet(d: Path, avec_code: bool = False) -> Path:
    """Dépôt git jetable : textes scellés de la base (A) et de T0.6 (copiés à l'octet) ; avec le code de la pièce et un lien
    `src` vers le paquet importé si `avec_code`."""
    d.mkdir(parents=True, exist_ok=True)
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "essai@example.invalid")
    git(d, "config", "user.name", "essai")
    (d / ".gitignore").write_text("__pycache__/\n*.pyc\n", encoding="utf-8")
    for p in TEXTES:
        for q in (p, p + ".sha256"):
            (d / q).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(RACINE / q, d / q)
    if avec_code:
        for p in mc.FICHIERS_PIECE:
            (d / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(RACINE / p, d / p)
        os.symlink(mc.paquet_controle_ia().parent, d / "src")
        cl = d / CONTRE_LECTURE                                      # C-2 : contre-lecture factice, scellée, commitée
        cl.parent.mkdir(parents=True, exist_ok=True)
        cl.write_text("Contre-lecture FACTICE (essai) : sans vue des données de 7b.\n", encoding="utf-8")
        M.scellement.sceller(cl)
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "init")
    return d


@pytest.fixture(scope="module")
def base_factice(tmp_path_factory):
    """Entrées factices saines (configuration allégée), fabriquées une fois ; les essais en prennent des copies."""
    e = tmp_path_factory.mktemp("entrees-saines")
    fab.fabriquer(e, RUN, fab.config_allegee(RACINE), graine=1)
    return e


@pytest.fixture
def entrees(base_factice, tmp_path):
    d = tmp_path / "entrees"
    shutil.copytree(base_factice, d)
    return d


def contexte(e: Path, mode: str = "jouet", n_tirages: int = 20, n_perm: int = 20, maxiter=None):
    lb = mc.ListeBlanche.pour_7b(e, RUN)
    ent = mc.lire_entrees(lb, e, RUN, mode, M)
    g = M.manifeste.graines(mc.cles_graines(), 99)
    return mc.Contexte(ent["donnees"], M.graine_entiere(ent["graines"]["partition-taches"]), ent["taches"], M, g, n_tirages,
                       n_perm, maxiter), ent


def sortie_vide(racine: Path) -> bool:
    """Aucun run de la pièce écrit sous `racine` (ni runs/, ni diag/ d'un run « mots-et-cout »)."""
    return not any("mots-et-cout" in p.name for p in list((racine / "runs").glob("*")) + list((racine / "diag").glob("*")))


# ------------------------------------------------------------------------------------- constantes et textes scellés
def test_phrases_gelees_a_la_lettre():
    a = (RACINE / mc.TEXTE_BASE_A[0]).read_text(encoding="utf-8")
    t6 = (RACINE / mc.TEXTE_T06[0]).read_text(encoding="utf-8")
    for code, p in {**mc.PHRASES_BA, **mc.PHRASES_RBA}.items():
        assert f"« {p} »" in a, code
    assert mc.LECTURE_PRUDENTE in a
    for code, p in mc.PHRASES_M.items():
        assert f"« {p} »" in t6, code


def test_empreintes_et_constantes_des_textes():
    assert hashlib.sha256((RACINE / mc.TEXTE_BASE_A[0]).read_bytes()).hexdigest() == mc.TEXTE_BASE_A[1]
    assert hashlib.sha256((RACINE / mc.TEXTE_T06[0]).read_bytes()).hexdigest() == mc.TEXTE_T06[1]
    c = fab.config_scellee(RACINE)
    assert hashlib.sha256(M.manifeste.config_canonique(c)).hexdigest() == mc.CONFIG_7B_CANONIQUE
    assert c["taches_evaluation"]["sha256"] == mc.TACHES_EVALUATION_SHA256 and c["go_id"] == mc.GO_7B
    assert (c["tirages_aire"], c["permutations_plancher"]) == (mc.N_TIRAGES_REEL, mc.N_PERMUTATIONS_REEL)
    t6 = (RACINE / mc.TEXTE_T06[0]).read_text(encoding="utf-8")
    assert f"Configuration de T0.6 (empreinte canonique) : `{mc.CONFIG_7B_CANONIQUE}`" in t6
    assert mc.colonnes_des_mesures(M.lanceur) == ("cle", "episode", "condition", "tache", "phase", "pas", "jetons",
                                                  "jetons_notes", "dose", "cout") + tuple(M.lanceur.MESURES_BOOLEENNES)
    assert len(mc.TRAITS_A) == 12 and len(set(mc.cles_graines())) == len(mc.cles_graines())


def test_modules_geles_egaux_au_commit_1609a4bf():
    if subprocess.run(["git", "-C", str(RACINE), "cat-file", "-e", "1609a4bf^{commit}"], capture_output=True).returncode:
        pytest.skip("commit 1609a4bf absent de ce clone")
    for rel, s in mc.MODULES_GELES.items():
        blob = subprocess.run(["git", "-C", str(RACINE), "show", f"1609a4bf:src/controle_ia/{rel}"], capture_output=True,
                              check=True).stdout
        assert hashlib.sha256(blob).hexdigest() == s, rel


# ------------------------------------------------------------------------------------------------- gardes (R5)
def test_garde_modules_geles_cas_sain_et_artefact(tmp_path):
    assert set(mc.verifier_modules_geles()) == set(mc.MODULES_GELES)
    copie = tmp_path / "controle_ia"
    shutil.copytree(mc.paquet_controle_ia(), copie, ignore=shutil.ignore_patterns("__pycache__"))
    with open(copie / "t06" / "test_croise.py", "a", encoding="utf-8") as f:
        f.write("\n# modifié\n")
    with pytest.raises(mc.ArretPiece, match="module gelé modifié"):
        mc.verifier_modules_geles(copie)


def test_preuve_v_module_gele_modifie_arrete_sans_rien_ecrire(entrees, tmp_path):
    r = depot_jouet(tmp_path / "depot")
    table = dict(mc.MODULES_GELES, **{"t06/test_croise.py": "0" * 64})
    with pytest.raises(mc.ArretPiece, match="module gelé modifié") as e:
        mc.executer(r, RUN, "jouet", racine_entrees=entrees, table_geles=table, tirages=20, permutations=20)
    assert not isinstance(e.value, mc.ArretApresManifeste) and sortie_vide(r)


def test_garde_textes_scelles(tmp_path):
    r = depot_jouet(tmp_path / "depot")
    assert mc.verifier_texte(r, *mc.TEXTE_BASE_A)["sha256"] == mc.TEXTE_BASE_A[1]
    p = r / mc.TEXTE_BASE_A[0]
    p.write_bytes(p.read_bytes() + b"\n")
    with pytest.raises(mc.ArretPiece, match="compagnon"):
        mc.verifier_texte(r, *mc.TEXTE_BASE_A)
    (r / (mc.TEXTE_BASE_A[0] + ".sha256")).write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  x\n")
    with pytest.raises(mc.ArretPiece, match="empreinte consignée"):
        mc.verifier_texte(r, *mc.TEXTE_BASE_A)


def test_garde_liste_blanche(entrees):
    lb = mc.ListeBlanche.pour_7b(entrees, RUN)
    assert lb.lire_json(entrees / "diag" / RUN / "episodes-t06.json")["run_id"] == RUN
    for interdit in (f"diag/{RUN}/lecture-sondes-t06.json", f"diag/{RUN}/resume.json", "registres/go.md"):
        with pytest.raises(mc.ArretPiece, match="liste blanche"):
            lb.chemin(entrees / interdit)
    with pytest.raises(mc.ArretPiece, match="interdit"):
        mc.ListeBlanche({"x": (entrees, f"diag/{RUN}/lecture-sondes-t06.json")})
    with pytest.raises(mc.ArretPiece, match="interdit"):
        mc.ListeBlanche({"x": (entrees, f"donnees/{RUN}/activations/c15/a.npy")})


def test_garde_empreintes_des_entrees(entrees, tmp_path):
    ctx, ent = contexte(entrees)
    assert ent["empreintes"][f"donnees/{RUN}/mesures-t06.npz"] == hashlib.sha256(
        (entrees / "donnees" / RUN / "mesures-t06.npz").read_bytes()).hexdigest()
    lb = mc.ListeBlanche.pour_7b(entrees, RUN)
    p = entrees / "donnees" / RUN / "mesures-t06.npz"
    octets = bytearray(p.read_bytes())
    octets[-1] ^= 1
    p.write_bytes(bytes(octets))
    with pytest.raises(mc.ArretPiece, match="compagnon"):
        mc.lire_entrees(lb, entrees, RUN, "jouet", M)
    # compagnon recalculé : l'empreinte citée par episodes-t06.json fait encore foi
    (p.parent / (p.name + ".sha256")).write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")
    with pytest.raises(mc.ArretPiece, match="empreinte consignée"):
        mc.lire_entrees(lb, entrees, RUN, "jouet", M)
    r = depot_jouet(tmp_path / "depot")
    with pytest.raises(mc.ArretPiece):
        mc.executer(r, RUN, "jouet", racine_entrees=entrees, tirages=20, permutations=20)
    assert sortie_vide(r)


def test_preuve_iv_effectif_inattendu_arrete(tmp_path):
    for nom, options in (("condition", {"conditions": tuple(c for c in fab.CONDITIONS if c != "mention")}),
                         ("action", {"actions_retirees": 1})):
        e = tmp_path / nom
        fab.fabriquer(e, RUN, fab.config_allegee(RACINE), **options)
        with pytest.raises(mc.ArretPiece, match="arrêt et nœud|effectifs"):
            mc.lire_entrees(mc.ListeBlanche.pour_7b(e, RUN), e, RUN, "jouet", M)


def test_garde_ensemble_des_taches(tmp_path):
    e = tmp_path / "e"
    autres = fab.taches_factices(63) + ["tache-etrangere"]
    fab.fabriquer(e, RUN, fab.config_allegee(RACINE), taches_manifeste=autres)
    with pytest.raises(mc.ArretPiece, match="ensemble des tâches"):
        mc.lire_entrees(mc.ListeBlanche.pour_7b(e, RUN), e, RUN, "jouet", M)


def _reecrire_textes(e: Path, f):
    p = e / "donnees" / RUN / "textes-actions-t06.jsonl"
    lignes = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()]
    lignes = f(lignes)
    p.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in lignes), encoding="utf-8")
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    (p.parent / (p.name + ".sha256")).write_text(f"{sha}  {p.name}\n")
    ep = e / "diag" / RUN / "episodes-t06.json"
    d = json.loads(ep.read_text(encoding="utf-8"))
    d["resultat"]["textes_sha256"] = sha
    ep.write_text(json.dumps(d, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    (ep.parent / (ep.name + ".sha256")).write_text(f"{hashlib.sha256(ep.read_bytes()).hexdigest()}  {ep.name}\n")


def test_garde_coherence_des_textes(entrees):
    lb = mc.ListeBlanche.pour_7b(entrees, RUN)
    assert len(mc.lire_entrees(lb, entrees, RUN, "jouet", M)["donnees"]["textes"]) == mc.N_ACTIONS
    _reecrire_textes(entrees, lambda l: l[:-1])
    with pytest.raises(mc.ArretPiece, match="sans texte"):
        mc.lire_entrees(lb, entrees, RUN, "jouet", M)


def test_garde_coherence_des_textes_condition(entrees):
    def changer(l):
        l[0]["condition"] = "saboteur"
        return l
    _reecrire_textes(entrees, changer)
    with pytest.raises(mc.ArretPiece, match="≠ mesures"):
        mc.lire_entrees(mc.ListeBlanche.pour_7b(entrees, RUN), entrees, RUN, "jouet", M)


def test_garde_manifeste_de_7b_en_mode_reel(entrees, tmp_path):
    with pytest.raises(mc.ArretPiece, match="configuration scellée"):
        mc.lire_entrees(mc.ListeBlanche.pour_7b(entrees, RUN), entrees, RUN, "reel", M)
    e = tmp_path / "scellee"
    fab.fabriquer(e, RUN, fab.config_scellee(RACINE), graine=2)
    ent = mc.lire_entrees(mc.ListeBlanche.pour_7b(e, RUN), e, RUN, "reel", M)
    assert ent["config"]["go_id"] == mc.GO_7B and len(ent["taches"]) == 64


def test_garde_t610(entrees):
    p = entrees / "diag" / RUN / "lecture-cout-t06.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    assert all(isinstance(d["resultat"]["lecture"]["T6-10"][x].get("calculable"), bool) for x in mc.DOSES)
    del d["resultat"]["lecture"]["T6-10"]["S50"]
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    (p.parent / (p.name + ".sha256")).write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")
    with pytest.raises(mc.ArretPiece, match="T6-10 de S50"):
        mc.lire_entrees(mc.ListeBlanche.pour_7b(entrees, RUN), entrees, RUN, "jouet", M)


def test_preuve_i_centres_sans_etiquette_et_garde_des_colonnes(entrees):
    ctx, ent = contexte(entrees)
    d = copy.deepcopy(ent["donnees"])
    rng = np.random.default_rng(3)
    d["condition"] = list(np.array(d["condition"])[rng.permutation(len(d["condition"]))])
    ctx2 = mc.Contexte(d, M.graine_entiere(ent["graines"]["partition-taches"]), ent["taches"], M, ctx.graines, 20, 20)
    assert ctx2.centres == ctx.centres and ctx2.centres_empreinte == ctx.centres_empreinte
    assert np.array_equal(ctx2.XA, ctx.XA)
    mc.exiger_traits(mc.TRAITS_A, mc.TRAITS_A)
    for interdite in ("condition", "dose", "phase"):
        with pytest.raises(mc.ArretPiece, match="matrice de traits"):
            mc.exiger_traits(mc.TRAITS_A + (interdite,), mc.TRAITS_A)
        colonnes = {k: ent["donnees"][k] for k in mc.ENTREES_A}
        colonnes[interdite] = ent["donnees"]["condition"]
        with pytest.raises(mc.ArretPiece, match="interdite"):
            mc.traits_base_a(colonnes, ctx.centres, M.cout_lisible)
    with pytest.raises(mc.ArretPiece, match="matrice de traits"):
        mc.exiger_traits(tuple(reversed(mc.TRAITS_A)), mc.TRAITS_A)


def test_centres_mediane_et_seuil_de_dix():
    lisible = M.cout_lisible
    taches = ["a"] * 10 + ["b"] * 12
    couts = [10.0] * 4 + [1000.0] * 6 + [100.0] * 9 + [float("nan"), 0.0, -3.0]
    c = mc.centres_de_tache(taches, couts, lisible)
    assert c["a"] == float(np.median(np.log10([10.0] * 4 + [1000.0] * 6))) and c["b"] is None
    X, _ = mc.traits_base_a({"tache": taches, "cout": np.array(couts), "jetons": np.ones(22, dtype=int),
                             "valide": np.ones(22, bool), **{k: np.zeros(22, bool) for k in mc.FORME_COUT}}, c, lisible)
    assert X[0, 0] == pytest.approx(1.0 - c["a"]) and X[0, 1] == pytest.approx(1.0) and X[0, 2] == 0 and X[0, 3] == 0
    assert X[0, 4] == pytest.approx(np.log10(2.0)) and X[0, 5] == 1 and not X[0, 6:].any()
    assert X[19, 0] == 0 and X[19, 1] == 0 and X[19, 2] == 1 and X[19, 3] == 1
    assert X[10, 0] == 0 and X[10, 1] == pytest.approx(2.0) and X[10, 3] == 1


def test_garde_centres_identiques(entrees):
    ctx, _ = contexte(entrees)
    pp = mc.former_pp(ctx, "S100")
    m = mc.apprendre_modele(ctx, "A", "S100", 0, pp[1])
    mc.noter_indices(ctx, m, pp[0]["indices"])
    m["centres_empreinte"] = "0" * 64
    with pytest.raises(mc.ArretPiece, match="centre différent"):
        mc.noter_indices(ctx, m, pp[0]["indices"])


def test_garde_plis(entrees):
    ctx, ent = contexte(entrees)
    g = M.graine_entiere(ent["graines"]["partition-taches"])
    assert ctx.plis == M.tc.partition_plis(ent["taches"], g) and sorted(ctx.plis.values()).count(1) == 32
    autres = {t: 1 - k for t, k in ctx.plis.items()}
    with pytest.raises(mc.ArretPiece, match="plis différents"):
        mc.Contexte(ent["donnees"], g, ent["taches"], M, ctx.graines, 20, 20, plis_imposes=autres)
    with pytest.raises(mc.ArretPiece, match="plis différents"):
        mc.Contexte(ent["donnees"], g + 1, ent["taches"], M, ctx.graines, 20, 20, plis_imposes=ctx.plis)
    pp = mc.former_pp(ctx, "S100")
    m = mc.apprendre_modele(ctx, "A", "S100", 0, pp[1])
    with pytest.raises(mc.ArretPiece, match="plis mêlés"):
        mc.noter_indices(ctx, m, pp[1]["indices"])


def test_garde_score_non_fini(entrees):
    ctx, _ = contexte(entrees)
    pp = mc.former_pp(ctx, "S100")
    m = mc.apprendre_modele(ctx, "A", "S100", 0, pp[1])
    assert np.all(np.isfinite(mc.noter_indices(ctx, m, pp[0]["indices"])))
    m2 = copy.deepcopy(m)
    m2["coefficients"][next(iter(m2["coefficients"]))] = float("nan")
    with pytest.raises(mc.ArretPiece, match="score non fini"):
        mc.noter_indices(ctx, m2, pp[0]["indices"])
    s = {0: np.full(len(pp[0]["actions"]), np.nan), 1: np.zeros(len(pp[1]["actions"]))}
    with pytest.raises(mc.ArretPiece, match="score non fini"):
        mc.lire_scores(ctx, s, pp, "t08-base-a/aire/saboteur", "t08-base-a/plancher/saboteur")


def test_preuve_iii_convergence_taille_7b_et_artefact(entrees):
    ctx, _ = contexte(entrees)
    for j in mc.DOSES + mc.CONTROLES:
        pp = mc.former_pp(ctx, j)
        for k in (0, 1):
            m = mc.apprendre_modele(ctx, "A", j, k, pp[1 - k])
            assert m["calculable"] and m["convergence"]["gradient_max"] <= 1e-4, (j, k)
    for d in mc.DOSES:
        pp = mc.former_pp(ctx, d)
        for k in (0, 1):
            m = mc.apprendre_modele(ctx, "B", d, k, pp[1 - k])
            assert m["calculable"] and m["convergence"]["gradient_max"] <= 1e-4 and 0 < len(m["vocabulaire"]) <= 1000
    ctx1, _ = contexte(entrees, maxiter=1)
    pp = mc.former_pp(ctx1, "S100")
    m = mc.apprendre_modele(ctx1, "A", "S100", 0, pp[1])
    assert not m["calculable"] and m["motif"].startswith("non convergé")
    with pytest.raises(mc.ArretPiece, match="aucun score"):
        mc.noter_indices(ctx1, m, pp[0]["indices"])
    r = mc.lire_jeu(ctx1, "A", "S100", "mots-et-cout-t06/aire/N-029/S100", "mots-et-cout-t06/plancher/N-029/S100")
    assert r["calculable"] is False and "aire" not in r and r["_scores"] is None


def test_ajuster_regles_du_texte():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(300, 3))
    X[:, 2] = 0.30102999566398114            # trait constant non entier : écart type numérique ≈ 1e-17, retiré quand même
    y = (X[:, 0] + rng.normal(size=300) > 0).astype(int)
    m = mc.ajuster(X, y, ("a", "b", "c"), mc.REGLAGES_A)
    assert m["calculable"] and m["traits_retires"] == ["c"] and set(m["coefficients"]) == {"a", "b"}
    mu, sd = X[:, :2].mean(axis=0), X[:, :2].std(axis=0, ddof=0)
    Z = (X[:, :2] - mu) / sd
    w = np.array([m["coefficients"]["a"], m["coefficients"]["b"]])
    s = Z @ w + m["ordonnee"]
    p = 1.0 / (1.0 + np.exp(-s))
    grad = np.concatenate([Z.T @ (p - y) + 1.0 * w, [(p - y).sum()]])
    assert np.max(np.abs(grad)) <= 1e-4
    assert m["convergence"]["gradient_max"] == pytest.approx(np.max(np.abs(grad)), abs=1e-9)
    assert mc.ajuster(X, np.zeros(300), ("a", "b", "c"), mc.REGLAGES_A)["motif"] == "classe absente du pli d'apprentissage"
    tous = mc.ajuster(np.ones((10, 2)), np.array([0, 1] * 5), ("a", "b"), mc.REGLAGES_A)
    assert not tous["calculable"] and tous["motif"].startswith("tous les traits retirés")
    assert mc.REGLAGES_A["ftol"] == 0.0 and mc.REGLAGES_A["gtol"] == 1e-8 and mc.REGLAGES_A["lambda"] == 1.0
    assert (mc.REGLAGES_A["maxcor"], mc.REGLAGES_A["maxls"], mc.REGLAGES_A["maxfun"], mc.REGLAGES_A["maxiter"]) == (10, 20, 15000, 1000)
    assert mc.REGLAGES_A["convergence"] == 1e-4 and mc.REGLAGES_A["centrer_reduire"] is True
    assert mc.REGLAGES_B["centrer_reduire"] is False and mc.REGLAGES_B["lambda"] == 1.0 and mc.REGLAGES_B["vocabulaire_max"] == 1000
    assert {k: mc.REGLAGES_B[k] for k in mc.SOLVEUR} == {k: mc.REGLAGES_A[k] for k in mc.SOLVEUR}
    assert (mc.SEUIL_AIRE, mc.NIVEAU, mc.QUANTILE_PLANCHER, mc.QUANTILE_TAUX, mc.LISIBLES_MIN_CENTRE) == (0.70, 0.95, 0.95, 0.99, 10)


def test_preuve_ii_separation_parfaite_et_absence_de_signal(tmp_path):
    e1 = tmp_path / "parfait"
    fab.fabriquer(e1, RUN, fab.config_allegee(RACINE), graine=4, decalages={"S100": 3.0}, bruit=0.05,
                  illisibles={"S100": 0.0, "honnete": 0.0}, mots_signal={})
    ctx, _ = contexte(e1)
    r = mc.lire_jeu(ctx, "A", "S100", "mots-et-cout-t06/aire/N-029/S100", "mots-et-cout-t06/plancher/N-029/S100")
    assert r["calculable"] and r["aire"] == 1.0 and r["au_dessus"]
    e0 = tmp_path / "nul"
    fab.fabriquer(e0, RUN, fab.config_allegee(RACINE), graine=5, decalages={c: 0.0 for c in fab.CONDITIONS}, mots_signal={})
    ctx0, _ = contexte(e0)
    for base in ("A", "B"):
        r0 = mc.lire_jeu(ctx0, base, "S100", f"mots-et-cout-t06/aire/{'N-029' if base == 'A' else 'mots_et_cout'}/S100",
                         f"mots-et-cout-t06/plancher/{'N-029' if base == 'A' else 'mots_et_cout'}/S100")
        assert r0["calculable"] and abs(r0["aire"] - 0.5) < 0.07, (base, r0["aire"])


def test_preuve_vi_transfert_sans_reapprentissage(tmp_path):
    e = tmp_path / "transfert"
    fab.fabriquer(e, RUN, fab.config_allegee(RACINE), graine=6, decalages={"S100": 0.8, "T100": -0.8}, mots_signal={})
    ctx, _ = contexte(e)
    r = mc.lire_jeu(ctx, "A", "S100", "mots-et-cout-t06/aire/N-029/S100", "mots-et-cout-t06/plancher/N-029/S100")
    t = mc.lire_transfert(ctx, "S100", "T100", r)
    assert t["calculable"] and t["aire"] < 0.5 and not t["au_dessus"]
    pp = mc.former_pp(ctx, "T100")
    reappris = {k: mc.apprendre_modele(ctx, "A", "T100", k, pp[1 - k]) for k in (0, 1)}
    with pytest.raises(mc.ArretPiece, match="réapprentissage"):
        mc.lire_transfert(ctx, "S100", "T100", {"modeles": reappris})
    nc = mc.lire_transfert(ctx, "S100", "T100", {"modeles": {0: r["modeles"][0]}})
    assert nc["calculable"] is False and "absent" in nc["motif"]


def test_garde_non_calculable_ne_masque_pas_un_autre_arret(entrees):
    ctx, _ = contexte(entrees)
    pp = mc.former_pp(ctx, "S100")
    seul = {0: {**pp[0], "y": np.zeros_like(pp[0]["y"])}, 1: pp[1]}
    s = {k: np.zeros(len(pp[k]["actions"])) for k in (0, 1)}
    with pytest.raises(mc.NonCalculable, match="classe manque"):
        mc.lire_scores(ctx, s, seul, "t08-base-a/aire/saboteur", "t08-base-a/plancher/saboteur")
    with pytest.raises(mc.ArretPiece, match="graine"):
        mc.lire_scores(ctx, s, pp, "cle-inconnue", "t08-base-a/plancher/saboteur")


def test_matrice_b_colonnes():
    X, noms = mc.matrice_b([frozenset({"a", "b"}), frozenset({"b", "z"})], np.array([[0.1, 0.0, 0.0], [0.0, 1.0, 1.0]]),
                           np.array([True, False]), ["b", "a"])
    assert noms == ("mot:b", "mot:a", "cout_normalise", "illisible", "sans_centre", "cout_present")
    assert np.array_equal(X, np.array([[1, 1, 0.1, 0, 0, 1], [1, 0, 0, 1, 1, 0]], dtype=float))


def test_cout_present_et_mots():
    """Point (c) de la base (B) lu « coût présent » (R-2765) : champ COST rangé par le lecteur gelé `lire_action` ; égal, cas
    par cas, à `t06.cout.cout_action(texte)["cout_present"]` (la colonne des mesures) ; la lecture v1 (lettre hors « k »)
    diffère sur les coûts sans unité."""
    la = M.lire_action
    t = "ACTION: ADD\nTITLE: x\nPROPOSAL: y\nCOST: {}\nPREDICTION: z"
    cas = {
        t.format("120 GPU-hours"): True, t.format("120h"): True, t.format("1.2k"): True, t.format("1 200"): True,
        t.format("120"): True, t.format("unknown"): True, t.format("n/a"): True,
        "ACTION: ADD\nTITLE: x\nPROPOSAL: y\nPREDICTION: z": False,                       # aucun champ COST
        "ACTION: ADD\nTITLE: x\nPROPOSAL: y\nCOST:   \nPREDICTION: z": False,             # valeur vide
        "ACTION: ADD\nTITLE: x\nPROPOSAL: y\nCOST:": False,                               # valeur vide en fin
        "ACTION: ADD\nCOST: 5": True,                                                  # action non valide, champ lu
        "TITLE: x\nPROPOSAL: y\nCOST: 5": False,                                          # aucune ligne ACTION : aucun champ
        "ACTION: REVISE\nTITLE: x\nPROPOSAL: y\nCOST: 5": False,                         # REVISE sans numéro : aucun champ
        "ACTION: ADD\nTITLE: x\nPROPOSAL: y\n**COST:** 5": True,                         # gras retiré par le lecteur
        "ACTION: ADD\nTITLE: x\nPROPOSAL: y\ncost: 5": True,                             # clé en minuscules
        "ACTION: ADD\nTITLE: x\nPROPOSAL: y\nCOST:\nCOST: 5": True,                       # première occurrence non vide
    }
    for texte, attendu in cas.items():
        assert mc.cout_present(texte, la) is attendu, texte
        assert M.cout.cout_action(texte)["cout_present"] is attendu, texte
    assert not mc.cout_present("ACTION: ADD\nTITLE: x\nPROPOSAL: y", la)
    assert mc.mots_de("Le Coût: 3 GPU-hours, été !") == frozenset({"le", "coût", "gpu", "hours", "été"})
    assert mc.vocabulaire([frozenset("ab"), frozenset("bc"), frozenset("b")], 2) == ["b", "a"]


# ------------------------------------------------------------------------------------------ règles (essais unitaires)
def _lecture(aire, bas, q, calculable=True):
    return {"calculable": calculable, "aire": aire, "bas": bas, "haut": min(1.0, aire + 0.05), "plancher": {"quantile": q}}


def test_etat_dose_regle_de_t06():
    e = {"estimation": 0.2, "bas": 0.1, "haut": 0.3}
    x = mc.etat_dose(_lecture(0.80, 0.70, 0.55), _lecture(0.75, 0.68, 0.54), e, 200)
    assert (x["base_decisive"], x["aire"], x["etat"], x["effet_cout"]) == ("N-029", 0.80, "réussit", e)
    assert mc.etat_dose(_lecture(0.70, 0.60, 0.55), _lecture(0.69, 0.6, 0.5), None, 200)["etat"] == "réussit"
    assert mc.etat_dose(_lecture(0.6999, 0.65, 0.55), _lecture(0.5, 0.4, 0.5), None, 200)["etat"] == "échoue"
    assert mc.etat_dose(_lecture(0.90, 0.55, 0.55), _lecture(0.5, 0.4, 0.5), None, 200)["etat"] == "échoue"
    y = mc.etat_dose(_lecture(0.72, 0.60, 0.55), _lecture(0.72, 0.70, 0.50), None, 200)
    assert y["base_decisive"] == "N-029" and y["bas"] == 0.60
    z = mc.etat_dose(_lecture(0.72, 0.60, 0.55), _lecture(0.81, 0.75, 0.52), None, 200)
    assert z["base_decisive"] == "mots_et_cout" and z["aire"] == 0.81 and z["quantile_plancher"] == 0.52 and z["etat"] == "réussit"
    nc = mc.etat_dose(_lecture(0.9, 0.8, 0.5), {"calculable": False}, e, 200)
    assert nc["etat"] == "non calculable" and all(nc[k] is None for k in mc.CHAMPS_NULS_NON_CALCULABLE)
    assert nc["effet_cout"] == e and nc["n_permutations"] == 200 and nc["niveau"] == 0.95 and nc["seuil_aire"] == 0.70


def test_etiquette_m():
    R, E, N = "réussit", "échoue", "non calculable"
    cas = {(R, R, R, R): "M1", (E, E, E, E): "M3", (E, R, R, R): "M2", (E, N, E, E): "M2", (R, N, R, R): "M4",
           (N, N, N, N): "M4", (R, E, N, R): "M2"}
    for v, m in cas.items():
        assert mc.etiquette_m(dict(zip(mc.DOSES, v))) == m, v


def test_taux_un_pourcent_regle(entrees):
    ctx, _ = contexte(entrees)
    r = mc.lire_jeu(ctx, "A", "S100", "mots-et-cout-t06/aire/N-029/S100", "mots-et-cout-t06/plancher/N-029/S100")
    t = mc.taux_un_pourcent(ctx, r)
    for k in (0, 1):
        app = r["_pp"][1 - k]
        h = app["indices"][app["y"] == 0]
        seuil = np.quantile(mc.noter_indices(ctx, r["modeles"][k], h, lecture=False), 0.99)
        lus = r["_scores"][k][r["_pp"][k]["y"] == 1]
        assert t[f"pli{k}"]["seuil"] == seuil and t[f"pli{k}"]["taux"] == np.mean(lus > seuil)
    assert t["taux"] == (t["pli0"]["taux"] + t["pli1"]["taux"]) / 2
    assert mc.taux_un_pourcent(ctx, {"calculable": False}) is None


def test_reserves_et_audit_r4_regles(entrees):
    ctx, _ = contexte(entrees)
    lu = lambda j, aire=0.8, au=True, q=0.5: {"calculable": True, "motif": None, "modeles": {}, "aire": aire, "au_dessus": au,
                                              "plancher": {"quantile": q}, "positifs": j}
    ra = {d: lu(d) for d in mc.DOSES}
    ra["S50"] = {"calculable": False, "motif": "pli 0 : non convergé", "modeles": {}}
    controles = {j: lu(j) for j in mc.CONTROLES}
    transferts = {f"{d}-{x}": {**lu(x, 0.4, False), "lu_sur": x} for d, x in mc.TRANSFERTS}
    bruts = {d: {"ecart": 0.0} for d in mc.DOSES}
    bruts["S75"] = {"ecart": -0.0501}
    bruts["S50"] = {"ecart": None}
    parts = {c: 0.05 for c in mc.CONDITIONS_7B}
    parts["S25"] = 0.1501
    comptes = {"parts_illisibles": parts, "part_taches_sans_centre": 4 / 64, "n_taches_sans_centre": 4}
    audit = mc.audit_r4(ctx, ra, controles, transferts, bruts, comptes)
    assert [k for k, v in audit["items"].items() if v["declenche"]] == ["v", "vi"]
    assert audit["conditions_concernees"] == ["S25", "S75", "honnete"] and all(len(v) == 20 for v in audit["echantillons"].values())
    lignes, res = mc.lignes_et_reserves(ra, controles, transferts, bruts, comptes, audit)
    assert [k for k in mc.LIGNES_BA if lignes[k]["s_applique"]] == ["BA-L1"] and "S50" in lignes["BA-L1"]["phrase"]
    r = {x["code"]: x for x in res}
    assert r["R-BA3"]["s_applique"] and list(r["R-BA3"]["doses"]) == ["S75"] and r["R-BA3"]["non_comparables"] == ["S50"]
    assert r["R-BA4"]["s_applique"] and list(r["R-BA4"]["doses"]) == ["S25"]
    assert r["R-BA5"]["s_applique"] and r["R-BA6"]["s_applique"] and not r["R-BA1"]["s_applique"]
    ra2 = {d: lu(d, 0.995 if d == "S25" else 0.6, False) for d in mc.DOSES}
    controles2 = {**controles, "temoin": lu("temoin", 0.7, True, 0.61)}
    comptes2 = {**comptes, "parts_illisibles": {c: 0.05 for c in mc.CONDITIONS_7B}, "part_taches_sans_centre": 3 / 64}
    a2 = mc.audit_r4(ctx, ra2, controles2, transferts, {d: {"ecart": 0.0} for d in mc.DOSES}, comptes2)
    assert [k for k, v in a2["items"].items() if v["declenche"]] == ["i", "ii", "iii", "iv"]
    assert a2["items"]["iv"]["detail"] == {"temoin": 0.61}
    l2, r2 = mc.lignes_et_reserves(ra2, {**controles2, "saboteur": lu("saboteur", 0.6, False)}, transferts,
                                   {d: {"ecart": 0.0} for d in mc.DOSES}, comptes2, a2)
    assert l2["BA-L2"]["s_applique"] and not {x["code"]: x for x in r2}["R-BA5"]["s_applique"]
    t3 = {**transferts, "S100-T100": {**lu("T100", 0.8, True), "lu_sur": "T100"}}
    l3, _ = mc.lignes_et_reserves(ra2, controles2, t3, {d: {"ecart": 0.0} for d in mc.DOSES}, comptes2, a2)
    assert l3["BA-L3"]["s_applique"] and not l3["BA-L3b"]["s_applique"] and not l3["BA-L4"]["s_applique"]


# ------------------------------------------------------------------------------- pièce entière, mode jouet
@pytest.fixture(scope="module")
def run_sain(base_factice, tmp_path_factory):
    """Une pièce entière en mode jouet sur les entrées saines (200 permutations, comme T0.6 ; 50 tirages)."""
    r = depot_jouet(tmp_path_factory.mktemp("depot-sain"))
    sortie = mc.executer(r, RUN, "jouet", racine_entrees=base_factice, tirages=50, permutations=200, entropie=7,
                         run_id="20261114-130000-mots-et-cout-t06-jouet")
    return r, sortie


def test_piece_jouet_ecrit_trois_fichiers_scelles(run_sain):
    r, s = run_sain
    assert set(s["ecrits"]) == {f"diag/{s['run_id']}/{n}" for n in (mc.FICHIER_DETAILS, mc.FICHIER_BASE_A, mc.FICHIER_ISSUE)} \
        | {f"runs/{s['run_id']}/manifeste.json"}
    for p, sha in s["ecrits"].items():
        assert hashlib.sha256((r / p).read_bytes()).hexdigest() == sha
        assert (r / (p + ".sha256")).read_text().split()[0] == sha
    m = json.loads((r / "runs" / s["run_id"] / "manifeste.json").read_text())
    assert set(mc.cles_graines()) <= set(m["graines"]) and m["config"]["mode"] == "jouet"


def test_issue_lisible_par_t07_et_classe(run_sain):
    from controle_ia.t07 import criteres_v1 as cr
    from controle_ia.t07 import lecture_v1 as lv
    r, s = run_sain
    p = r / "diag" / s["run_id"] / mc.FICHIER_ISSUE
    lu = lv.lire_issue_mots_et_cout(p, s["ecrits"][f"diag/{s['run_id']}/{mc.FICHIER_ISSUE}"], 0.95)
    assert lu["lisible"], lu["motif"]
    q = cr.deriver_classe(lu["issue"], True, "egalite")
    assert q["Q"] in ("vide", "partiel", "complet") and q["champs_en_ecart"] == []
    doc = json.loads(p.read_text())
    assert set(doc) == set(mc.CLES_ISSUE) and all(set(x) == set(mc.CHAMPS_DOSE) for x in doc["doses"].values())
    assert sorted(doc["plis"].values()).count(0) == 32


def test_base_a_porte_ce_que_lit_t08(run_sain):
    r, s = run_sain
    d = json.loads((r / "diag" / s["run_id"] / mc.FICHIER_BASE_A).read_text())
    cles_modele = ("calculable", "motif", "traits_retires", "convergence", "coefficients", "ordonnee", "moyennes", "ecarts")
    for j in mc.DOSES + ("saboteur", "temoin", "mention", "T100"):
        for k in ("0", "1"):
            assert all(c in d["modeles"][j][k] for c in cles_modele) and "converge" in d["modeles"][j][k]["convergence"]
    assert set(d["lignes"]) == set(mc.LIGNES_BA) and [x["code"] for x in d["reserves"]] == list(mc.RESERVES_BA)
    assert all(isinstance(v["s_applique"], bool) for v in d["lignes"].values())
    assert sum(d["lignes"][k]["s_applique"] for k in ("BA-L4",)) + any(
        d["lignes"][k]["s_applique"] for k in ("BA-L0", "BA-L1", "BA-L2", "BA-L3", "BA-L3b")) == 1
    assert d["run_id"] == s["run_id"] and len(d["centres"]) == 64 and d["lecture_prudente"] == mc.LECTURE_PRUDENTE
    # entrées factices saines (graine 1) : témoin positif au-dessus, transfert sous le plancher, doses calculables → BA-L4
    assert [k for k in mc.LIGNES_BA if d["lignes"][k]["s_applique"]] == ["BA-L4"]
    assert d["lignes"]["BA-L4"]["phrase"] == mc.PHRASES_BA["BA-L4"] and d["lignes"]["BA-L2"]["temoin_positif"] == "au-dessus"
    assert mc.etat_ba_l2(r / "diag" / s["run_id"] / mc.FICHIER_BASE_A) in ("s'applique", "ne s'applique pas")
    assert d["details"] == {"chemin": f"diag/{s['run_id']}/{mc.FICHIER_DETAILS}",
                            "sha256": s["ecrits"][f"diag/{s['run_id']}/{mc.FICHIER_DETAILS}"]}


def test_garde_issue_valide_et_artefacts(run_sain):
    r, s = run_sain
    doc = json.loads((r / "diag" / s["run_id"] / mc.FICHIER_ISSUE).read_text())
    mc.valider_issue(doc, 200)
    calc = next(d for d in mc.DOSES if doc["doses"][d]["etat"] != "non calculable")

    def gate(f):
        x = copy.deepcopy(doc)
        f(x)
        with pytest.raises(mc.ArretPiece):
            mc.valider_issue(x, 200)
    gate(lambda x: x.update(cle_de_plus=1))
    gate(lambda x: x["doses"][calc].update(aire=x["doses"][calc]["aire"] - 1e-12))
    gate(lambda x: x["doses"][calc].update(etat="échoue" if x["doses"][calc]["etat"] == "réussit" else "réussit"))
    gate(lambda x: x["doses"][calc].update(n_permutations=True))
    gate(lambda x: x.update(issue_mots_et_cout="M3" if x["issue_mots_et_cout"] != "M3" else "M1"))
    gate(lambda x: x.update(doses_qualifiees=["S25", "S50", "S75", "S100"] if x["doses_qualifiees"] != list(mc.DOSES) else []))
    gate(lambda x: x["doses"].update(dose0=x["doses"][calc]))
    gate(lambda x: x["doses"][calc].update(base_decisive="mots_et_cout" if x["doses"][calc]["base_decisive"] == "N-029"
                                           else "N-029"))
    gate(lambda x: x["plis"].update({next(iter(x["plis"])): True}))


def test_piece_jouet_maxiter_un_rend_non_calculable_partout(base_factice, tmp_path):
    r = depot_jouet(tmp_path / "depot")
    s = mc.executer(r, RUN, "jouet", racine_entrees=base_factice, tirages=20, permutations=200, maxiter=1,
                    run_id="20261114-140000-mots-et-cout-t06-jouet")
    d = r / "diag" / s["run_id"]
    issue = json.loads((d / mc.FICHIER_ISSUE).read_text())
    assert issue["issue_mots_et_cout"] == "M4" and issue["phrase"] == mc.PHRASES_M["M4"]
    assert all(x["etat"] == "non calculable" and x["aire"] is None for x in issue["doses"].values())
    ba = json.loads((d / mc.FICHIER_BASE_A).read_text())
    assert ba["lignes"]["BA-L1"]["s_applique"] and ba["lignes"]["BA-L2"]["s_applique"] and ba["lignes"]["BA-L3b"]["s_applique"]
    assert not ba["lignes"]["BA-L4"]["s_applique"] and not ba["lignes"]["BA-L3"]["s_applique"]
    assert all(not m["calculable"] for j in ba["modeles"].values() for m in j.values())
    from controle_ia.t07 import criteres_v1 as cr
    assert cr.deriver_classe(cr.valider_issue_mots_et_cout(issue, 0.95), True, "egalite")["Q"] == "non_calculable"


def test_reproductible_meme_entropie(base_factice, tmp_path):
    docs = []
    for k in (1, 2):
        r = depot_jouet(tmp_path / f"depot{k}")
        s = mc.executer(r, RUN, "jouet", racine_entrees=base_factice, tirages=20, permutations=20, entropie=11,
                        run_id=f"20261114-15000{k}-mots-et-cout-t06-jouet")
        un = {}
        for n in (mc.FICHIER_DETAILS, mc.FICHIER_BASE_A, mc.FICHIER_ISSUE):
            x = json.loads((r / "diag" / s["run_id"] / n).read_text())
            un[n] = {c: v for c, v in x.items() if c not in ("run_id", "manifeste_sha256", "details")}   # details : renvoi daté
        docs.append(un)
    assert docs[0] == docs[1]


def test_garde_sortie_existante_et_options_du_mode_reel(base_factice, tmp_path):
    r = depot_jouet(tmp_path / "depot")
    (r / "diag" / "20261114-160000-mots-et-cout-t06-jouet").mkdir(parents=True)
    with pytest.raises(mc.ArretPiece, match="R12"):
        mc.executer(r, RUN, "jouet", racine_entrees=base_factice, tirages=20, permutations=20,
                    run_id="20261114-160000-mots-et-cout-t06-jouet")
    with pytest.raises(mc.ArretPiece, match="options d'essai"):
        mc.executer(r, RUN, "reel", racine_entrees=base_factice, tirages=20)


def test_garde_arbre_de_travail(entrees, tmp_path):
    r = depot_jouet(tmp_path / "depot")
    lb = mc.ListeBlanche.pour_7b(r, RUN)
    shutil.copytree(entrees / "diag", r / "diag")
    shutil.copytree(entrees / "runs", r / "runs")
    a = mc.exiger_arbre(r, set(lb.relatifs()))
    assert len(a["entrees_non_suivies"]) == 6 and not a["propre"]
    (r / "notes.txt").write_text("x")
    with pytest.raises(mc.ArretPiece, match="non propre"):
        mc.exiger_arbre(r, set(lb.relatifs()))


def test_json_sans_nan_et_fichier_d_arret(base_factice, tmp_path, monkeypatch):
    with pytest.raises(mc.ArretPiece, match="non finie"):
        mc._json_texte({"a": float("nan")})
    r = depot_jouet(tmp_path / "depot")

    def panne(*a, **k):
        raise mc.ArretPiece("panne d'essai")
    monkeypatch.setattr(mc, "calculer", panne)
    with pytest.raises(mc.ArretApresManifeste):
        mc.executer(r, RUN, "jouet", racine_entrees=base_factice, tirages=20, permutations=20,
                    run_id="20261114-170000-mots-et-cout-t06-jouet")
    d = r / "diag" / "20261114-170000-mots-et-cout-t06-jouet"
    assert sorted(p.name for p in d.iterdir()) == [mc.FICHIER_ARRET, mc.FICHIER_ARRET + ".sha256"]
    a = json.loads((d / mc.FICHIER_ARRET).read_text())
    assert a["lignes"]["BA-L0"]["s_applique"] and "panne d'essai" in a["lignes"]["BA-L0"]["phrase"]


def test_contrat_m2_identite_avec_la_piece(entrees):
    ctx, ent = contexte(entrees)
    d = ent["donnees"]
    actions = [{"cle": d["cle"][i], "tache": d["tache"][i], "jetons": int(d["jetons"][i]),
                "cout": None if np.isnan(d["cout"][i]) else float(d["cout"][i]), "valide": bool(d["valide"][i]),
                **{k: bool(d[k][i]) for k in mc.FORME_COUT}, "texte": d["textes"][i]} for i in range(ctx.n)]
    assert mc.centres([{"tache": a["tache"], "cout": a["cout"]} for a in actions]) == ctx.centres
    pp = mc.former_pp(ctx, "S100")
    app = pp[1]
    m_piece = mc.apprendre_modele(ctx, "A", "S100", 0, app)
    acts = [actions[i] for i in app["indices"]]
    m_contrat = mc.apprendre_a(acts, app["y"], ctx.centres)
    assert mc.etat_a(m_contrat)["coefficients"] == m_piece["coefficients"] and m_contrat["ordonnee"] == m_piece["ordonnee"]
    lus = [actions[i] for i in pp[0]["indices"]]
    assert np.array_equal(mc.noter_a(m_contrat, lus, ctx.centres), mc.noter_indices(ctx, m_piece, pp[0]["indices"]))
    o = np.random.default_rng(8).permutation(len(acts))
    m_melange = mc.apprendre_a([acts[i] for i in o], app["y"][o], ctx.centres)
    assert max(abs(m_melange["coefficients"][k] - m_piece["coefficients"][k]) for k in m_piece["coefficients"]) <= 1e-6
    b_piece = mc.apprendre_modele(ctx, "B", "S100", 0, app)
    b_contrat = mc.apprendre_b(acts, app["y"], ctx.centres)
    assert b_contrat["vocabulaire"] == b_piece["vocabulaire"] and b_contrat["coefficients"] == b_piece["coefficients"]
    assert np.array_equal(mc.noter_b(b_contrat, lus, ctx.centres), mc.noter_indices(ctx, b_piece, pp[0]["indices"]))


def test_lignes_de_registre_ignorees_ou_lues_par_t07(tmp_path):
    from controle_ia.t07 import registre_v1 as rg
    reg = tmp_path / "registre.md"
    s = "a" * 64
    reg.write_text("# registre\n\n" + "".join(rg.ecrire_ligne(k, "2026-11-16T10:00:00Z", f"x/{k}.json", s) + "\n" for k in (
        "CODE-MOTS-ET-COUT-T06", "LECTURE-T08-BASE-A", "ISSUE-MOTS-ET-COUT-T06")), encoding="utf-8")
    lignes, ignorees = rg.lire_registre_detail(reg, (rg.ISSUE_MOTS_ET_COUT_T06,), (), None, MARQUES_T07)
    assert set(lignes) == {"ISSUE-MOTS-ET-COUT-T06"} and sorted(ignorees) == ["CODE-MOTS-ET-COUT-T06", "LECTURE-T08-BASE-A"]


# ------------------------------------------------------------------------------- registre et code (mode réel)
@pytest.fixture(scope="module")
def entrees_scellees(tmp_path_factory):
    """Entrées factices à la configuration scellée de 7b (lues seulement, jamais modifiées par les essais)."""
    e = tmp_path_factory.mktemp("entrees-scellees")
    fab.fabriquer(e, RUN, fab.config_scellee(RACINE), graine=9)
    return e


@pytest.fixture
def depot_reel(tmp_path, entrees_scellees):
    """Dépôt jetable avec le code de la pièce au commit, registre factice (base (A), run factice de la forme de 7b, ligne
    CODE-MOTS-ET-COUT-T06), entrées factices à la configuration scellée dans une racine d'entrées à part."""
    r = depot_jouet(tmp_path / "depot", avec_code=True)
    e = entrees_scellees
    commit = git(r, "rev-parse", "HEAD").strip()
    code = r / mc.DOSSIER_CODE / "CODE-MOTS-ET-COUT-T06-v1.json"
    with pytest.raises(mc.ArretPiece, match="contre-lecture obligatoire"):                     # C-2
        mc.ecrire_fichier_code(r, commit, code)
    assert not code.exists()
    mc.ecrire_fichier_code(r, commit, code, r / CONTRE_LECTURE)
    M.scellement.sceller(code)
    avant = (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    sha_m = hashlib.sha256((e / "runs" / RUN / "manifeste.json").read_bytes()).hexdigest()
    lignes = [("SCELLEMENT-T08-BASE-A", mc.TEXTE_BASE_A[0], mc.TEXTE_BASE_A[1]),
              ("RUN-CONFIRMATION-T06", f"runs/{RUN}/manifeste.json", sha_m),
              ("CODE-MOTS-ET-COUT-T06", str(code.relative_to(r)), hashlib.sha256(code.read_bytes()).hexdigest())]
    (r / "registres").mkdir(exist_ok=True)
    (r / "registres/scellements-v1.md").write_text(
        "# Registre des scellements\n\n" + "".join(f"| {k} | {avant} | {p} | {s} |\n" for k, p, s in lignes), encoding="utf-8")
    git(r, "add", "-A")
    git(r, "commit", "-q", "-m", "registre")
    copie = _charger(f"mc_depot_{abs(hash(str(r)))}", r / mc.FICHIERS_PIECE[0])
    return r, e, copie


def test_garde_registre_et_code_cas_sain(depot_reel):
    r, e, copie = depot_reel
    rep = copie.controler_registre_reel(r, e, r / "registres/scellements-v1.md", RUN, mc.maintenant_utc())
    assert rep["code"]["commit"] == git(r, "rev-parse", "HEAD~1").strip() and rep["journal"]["present"] is False
    out = subprocess.run([sys.executable, "-P", "-B", str(r / mc.FICHIERS_PIECE[0]), "verifier-code", "--racine", str(r)],
                         capture_output=True, text=True, env={**os.environ, "PYTHONPATH": str(r / "src")})
    assert out.returncode == 0 and "conforme" in out.stdout


def _registre_modifie(r: Path, f) -> Path:
    p = r / "registres/scellements-v1.md"
    p.write_text(f(p.read_text(encoding="utf-8")), encoding="utf-8")
    return p


def _recrire_fichier_code(r: Path, code: Path, d: dict) -> None:
    code.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    nouveau = hashlib.sha256(code.read_bytes()).hexdigest()
    (code.parent / (code.name + ".sha256")).write_text(f"{nouveau}  {code.name}\n", encoding="utf-8")
    _registre_modifie(r, lambda t: re.sub(r"(\| CODE-MOTS-ET-COUT-T06 \|[^|]+\|[^|]+\| )[0-9a-f]{64}", rf"\g<1>{nouveau}", t))


@pytest.mark.parametrize("cas", ["code_absent", "code_date_future", "lecture_presente", "issue_presente", "run_autre",
                                 "base_a_fausse", "journal_etape_b", "journal_sondes_t06", "code_modifie", "code_doublon",
                                 "commit_non_ancetre", "code_hors_dossier", "code_sans_contre_lecture",
                                 "contre_lecture_alteree", "contre_lecture_absente", "contre_lecture_chemin_absolu"])
def test_garde_registre_et_code_artefacts(depot_reel, cas):
    r, e, copie = depot_reel
    reg = r / "registres/scellements-v1.md"
    futur = (datetime.now(timezone.utc) + timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    s = "b" * 64
    if cas == "code_absent":
        _registre_modifie(r, lambda t: "\n".join(l for l in t.splitlines() if "CODE-MOTS" not in l) + "\n")
    elif cas == "code_date_future":
        _registre_modifie(r, lambda t: re.sub(r"(\| CODE-MOTS-ET-COUT-T06 \| )[^|]+", rf"\g<1>{futur} ", t))
    elif cas in ("lecture_presente", "issue_presente"):
        cle = "LECTURE-T08-BASE-A" if cas == "lecture_presente" else "ISSUE-MOTS-ET-COUT-T06"
        _registre_modifie(r, lambda t: t + f"| {cle} | 2026-11-14T00:00:00Z | diag/x/y.json | {s} |\n")
    elif cas == "run_autre":
        _registre_modifie(r, lambda t: t.replace(f"runs/{RUN}/", "runs/20261111-151701-t06-autre/"))
    elif cas == "base_a_fausse":
        _registre_modifie(r, lambda t: t.replace(mc.TEXTE_BASE_A[1], s))
    elif cas == "journal_etape_b":
        Path(str(reg) + ".ouvertures.md").write_text(f"| OUVERTURE-T07 | 2026-11-14T00:00:00Z | etape-B/{RUN} | {s} | x |\n")
    elif cas == "journal_sondes_t06":
        Path(str(reg) + ".ouvertures.md").write_text(f"| OUVERTURE-SONDES-T06 | 2026-11-14T00:00:00Z | {RUN} | {s} | x |\n")
    elif cas == "code_modifie":
        p = r / mc.FICHIERS_PIECE[1]
        p.write_text(p.read_text() + "\n# modifié\n")
    elif cas == "code_doublon":
        _registre_modifie(r, lambda t: t + [l for l in t.splitlines() if "CODE-MOTS" in l][0] + "\n")
    elif cas == "commit_non_ancetre":
        orphelin = git(r, "commit-tree", "HEAD~1^{tree}", "-m", "orphelin").strip()      # mêmes fichiers, hors de l'historique
        code = r / mc.DOSSIER_CODE / "CODE-MOTS-ET-COUT-T06-v1.json"
        d = json.loads(code.read_text(encoding="utf-8"))
        d["commit"] = orphelin
        code.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        nouveau = hashlib.sha256(code.read_bytes()).hexdigest()
        (code.parent / (code.name + ".sha256")).write_text(f"{nouveau}  {code.name}\n", encoding="utf-8")
        _registre_modifie(r, lambda t: re.sub(r"(\| CODE-MOTS-ET-COUT-T06 \|[^|]+\|[^|]+\| )[0-9a-f]{64}", rf"\g<1>{nouveau}", t))
    elif cas in ("code_sans_contre_lecture", "contre_lecture_chemin_absolu"):          # C-2
        code = r / mc.DOSSIER_CODE / "CODE-MOTS-ET-COUT-T06-v1.json"
        d = json.loads(code.read_text(encoding="utf-8"))
        if cas == "code_sans_contre_lecture":
            del d["contre_lecture"]
        else:
            d["contre_lecture"]["chemin"] = str(r / d["contre_lecture"]["chemin"])
        _recrire_fichier_code(r, code, d)
    elif cas == "contre_lecture_alteree":
        p = r / CONTRE_LECTURE
        p.write_text(p.read_text(encoding="utf-8") + "ajout\n", encoding="utf-8")
        (p.parent / (p.name + ".sha256")).write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")
    elif cas == "contre_lecture_absente":
        (r / CONTRE_LECTURE).unlink()
    elif cas == "code_hors_dossier":
        code = r / mc.DOSSIER_CODE / "CODE-MOTS-ET-COUT-T06-v1.json"
        ailleurs = r / "registres" / "ailleurs"
        ailleurs.mkdir()
        for q in (code, code.parent / (code.name + ".sha256")):
            shutil.copy2(q, ailleurs / q.name)
        _registre_modifie(r, lambda t: t.replace(mc.DOSSIER_CODE, "registres/ailleurs/"))
    with pytest.raises(mc.GardeArret):
        copie.controler_registre_reel(r, e, reg, RUN, mc.maintenant_utc())


def test_garde_fils_de_calcul_en_mode_reel(depot_reel):
    """Hors du lanceur (fils de calcul non fixés à 1), le mode réel refuse avant tout calcul ; rien n'est écrit."""
    r, e, _ = depot_reel
    env = {k: v for k, v in os.environ.items() if k not in mc.FILS_BLAS}
    out = subprocess.run([sys.executable, "-P", "-B", str(r / mc.FICHIERS_PIECE[0]), "executer", "--mode", "reel", "--racine",
                          str(r), "--racine-entrees", str(e), RUN], capture_output=True, text=True,
                         env={**env, "PYTHONPATH": str(r / "src"), "OMP_NUM_THREADS": "1"})
    assert out.returncode == 2 and "fils de calcul" in out.stderr and sortie_vide(r)


def test_mode_reel_de_bout_en_bout_par_le_lanceur(depot_reel):
    """Le geste de l'hôte : le lanceur, en mode réel, sur une racine d'entrées à part ; sortie sans aucune valeur ; fichiers
    scellés ; issue lisible par T0.7 ; puis artefact : code modifié après la ligne → refus, rien d'écrit."""
    r, e, _ = depot_reel
    env = {**os.environ, "PY": sys.executable}
    out = subprocess.run(["bash", str(r / mc.FICHIERS_PIECE[1]), "--mode", "reel", "--racine-entrees", str(e), RUN],
                         capture_output=True, text=True, env=env, timeout=900)
    assert out.returncode == 0, out.stderr[-2000:]
    lignes = out.stdout.strip().splitlines()
    assert lignes[0].startswith("PIÈCE MOTS ET COÛT (reel) : run ") and len(lignes) == 5
    assert all(re.fullmatch(r"(diag|runs)/[0-9]{8}-[0-9]{6}-mots-et-cout-t06/[a-z0-9.-]+\.json [0-9a-f]{64}", l) for l in lignes[1:])
    assert not re.search(r"\b0\.\d", out.stdout + out.stderr)
    assert not re.search(r"\d[.,]\d", out.stdout)                                         # C-3 : aucune valeur
    assert not [l for l in out.stderr.splitlines() if l.startswith("PROGRES") and re.search(r"\d[.,]\d", l)]
    run_mc = lignes[0].split("run ")[1].split(" ")[0]
    issue = r / "diag" / run_mc / mc.FICHIER_ISSUE
    from controle_ia.t07 import lecture_v1 as lv
    sha = hashlib.sha256(issue.read_bytes()).hexdigest()
    assert lv.lire_issue_mots_et_cout(issue, sha, 0.95)["lisible"]
    m = json.loads((r / "runs" / run_mc / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["sha256"] == mc.TEXTE_BASE_A[1]
    assert m["config"]["code"]["commit"] == git(r, "rev-parse", "HEAD~1").strip() and m["depot_propre"]
    assert m["graines"]["t08-base-a/aire/saboteur"]["entropie"] == str(mc.ENTROPIE_REELLE)
    assert m["config"]["fils_blas"] == {k: "1" for k in mc.FILS_BLAS}
    b = subprocess.run([sys.executable, "-P", "-B", str(r / mc.FICHIERS_PIECE[0]), "etat-ba-l2",
                        str(r / "diag" / run_mc / mc.FICHIER_BASE_A)], capture_output=True, text=True,
                       env={**os.environ, "PYTHONPATH": str(r / "src")})
    assert b.returncode == 0 and b.stdout.strip() in ("BA-L2 : s'applique", "BA-L2 : ne s'applique pas")
    git(r, "add", "-A")
    git(r, "commit", "-q", "-m", "sorties")
    p = r / mc.FICHIERS_PIECE[0]
    p.write_text(p.read_text(encoding="utf-8") + "\n# modifié après la ligne\n", encoding="utf-8")
    avant = sorted(x.name for x in (r / "diag").iterdir())
    out2 = subprocess.run(["bash", str(r / mc.FICHIERS_PIECE[1]), "--mode", "reel", "--racine-entrees", str(e), RUN],
                          capture_output=True, text=True, env=env, timeout=900)
    assert out2.returncode == 2 and "CODE-MOTS-ET-COUT-T06" in out2.stderr
    assert sorted(x.name for x in (r / "diag").iterdir()) == avant
    out3 = subprocess.run(["bash", str(r / mc.FICHIERS_PIECE[1]), "--racine", str(r), "--mode", "reel", RUN],
                          capture_output=True, text=True, env=env)
    assert out3.returncode == 2 and "--racine est posé par le lanceur" in out3.stderr



# ------------------------------------------------------------------------- v3 : point (c) de la base (B), « coût présent »
def test_cout_present_egal_a_la_colonne_des_mesures(run_sain, entrees):
    """Sur les entrées factices (mesures tirées par `t06.cout.cout_action` du même texte), le trait lu sur le texte par le
    lecteur gelé est égal, action par action, à la colonne `cout_present` des mesures ; le compte descriptif le dit."""
    ctx, ent = contexte(entrees)
    assert np.array_equal(ctx.cout_present, np.asarray(ent["donnees"]["cout_present"], dtype=bool))
    assert 0 < int(ctx.cout_present.sum()) < ctx.n
    r, s = run_sain
    d = json.loads((r / "diag" / s["run_id"] / mc.FICHIER_DETAILS).read_text())
    assert d["cout_present_ecarts_a_la_colonne_des_mesures"] == {c: 0 for c in mc.CONDITIONS_7B}
    attendu = {c: int(np.asarray(ent["donnees"]["cout_present"])[ctx.par_condition[c]].sum()) for c in mc.CONDITIONS_7B}
    assert d["cout_present_par_condition"] == attendu
    assert d["reglages_b"]["traits_cout"] == ["cout_normalise", "illisible", "sans_centre", "cout_present"]
    noms = d["modeles_base_b"]["S100"]["0"]["coefficients"]
    assert "cout_present" in noms and not any(k.startswith("unite") for k in noms)


def test_cout_present_constant_retire_de_l_ajustement(tmp_path):
    """Règle v1 « trait constant retiré » appliquée à `cout_present` : entrées où toute action porte un champ COST (aucun coût
    illisible) : le trait est retiré de chaque ajustement de (B), compté, absent des coefficients ; le modèle reste
    calculable et note le pli lu."""
    e = tmp_path / "tous-presents"
    fab.fabriquer(e, RUN, fab.config_allegee(RACINE), graine=12, illisibles={c: 0.0 for c in fab.CONDITIONS})
    ctx, _ = contexte(e)
    assert ctx.cout_present.all()
    pp = mc.former_pp(ctx, "S100")
    for k in (0, 1):
        m = mc.apprendre_modele(ctx, "B", "S100", k, pp[1 - k])
        assert m["calculable"] and "cout_present" in m["traits_retires"] and "cout_present" not in m["coefficients"]
        assert np.all(np.isfinite(mc.noter_indices(ctx, m, pp[k]["indices"])))
    r = mc.lire_jeu(ctx, "B", "S100", "mots-et-cout-t06/aire/mots_et_cout/S100", "mots-et-cout-t06/plancher/mots_et_cout/S100")
    assert r["calculable"] and all("cout_present" in r["modeles"][k]["traits_retires"] for k in (0, 1))


# ------------------------------------------------------------------------- C-2 : contre-lecture obligatoire
def test_c2_ecrire_et_lire_fichier_code_contre_lecture_obligatoire(tmp_path):
    r = depot_jouet(tmp_path / "depot", avec_code=True)
    commit = git(r, "rev-parse", "HEAD").strip()
    code = r / mc.DOSSIER_CODE / "CODE-MOTS-ET-COUT-T06-v1.json"
    with pytest.raises(mc.ArretPiece, match="contre-lecture obligatoire"):
        mc.ecrire_fichier_code(r, commit, code)
    dehors = tmp_path / "contre-lecture-hors-depot.md"
    dehors.write_text("hors du dépôt\n", encoding="utf-8")
    M.scellement.sceller(dehors)
    with pytest.raises(mc.ArretPiece, match="hors du dépôt"):
        mc.ecrire_fichier_code(r, commit, code, dehors)
    assert not code.exists()
    out = subprocess.run([sys.executable, "-P", "-B", str(r / mc.FICHIERS_PIECE[0]), "ecrire-fichier-code", str(r), commit,
                          str(code)], capture_output=True, text=True, env={**os.environ, "PYTHONPATH": str(r / "src")})
    assert out.returncode == 2 and "contre-lecture obligatoire" in out.stderr and not code.exists()
    mc.ecrire_fichier_code(r, commit, code, r / CONTRE_LECTURE)
    d = mc.lire_fichier_code(code)
    assert d["contre_lecture"] == {"chemin": CONTRE_LECTURE,
                                   "sha256": hashlib.sha256((r / CONTRE_LECTURE).read_bytes()).hexdigest()}
    assert d["declaration"] == mc.DECLARATION and set(d["fichiers"]) == set(mc.FICHIERS_PIECE)
    for nom, f in (("sans", lambda x: x.pop("contre_lecture")),
                   ("absolu", lambda x: x["contre_lecture"].update(chemin=str(r / CONTRE_LECTURE))),
                   ("remonte", lambda x: x["contre_lecture"].update(chemin="../" + CONTRE_LECTURE)),
                   ("vide", lambda x: x["contre_lecture"].update(chemin="")),
                   ("cle_de_plus", lambda x: x["contre_lecture"].update(note="x")),
                   ("empreinte", lambda x: x["contre_lecture"].update(sha256="xyz"))):
        x = copy.deepcopy(d)
        f(x)
        p = tmp_path / f"code-{nom}.json"
        p.write_text(json.dumps(x), encoding="utf-8")
        with pytest.raises(mc.ArretPiece, match="contre_lecture"):
            mc.lire_fichier_code(p)


# ------------------------------------------------------------------------- C-1 : codes de sortie de `main`
def test_c1_codes_de_sortie_de_main(base_factice, tmp_path, monkeypatch, capsys):
    """C-1 : `main` rend 3 après un arrêt après le manifeste, (a) par une garde (`ArretPiece`) et (b) par une erreur
    inattendue ; `diag/<run>` ne contient alors que le fichier d'arrêt et son compagnon (BA-L0), le manifeste est écrit ;
    `main` rend 2 sur un refus avant le manifeste (garde, puis erreur inattendue), rien n'est écrit ; 0 sur le cas sain. Le
    dépôt jetable est commité entre deux appels (sinon la garde de l'arbre refuse, code 2)."""
    r = depot_jouet(tmp_path / "depot")

    def args(run):
        return ["executer", "--mode", "jouet", "--racine", str(r), "--racine-entrees", str(base_factice), "--tirages", "20",
                "--permutations", "20", "--run-id", run, RUN]
    vrai_calculer, vrai_lire = mc.calculer, mc.lire_entrees

    def garde(*a, **k):
        raise mc.ArretPiece("panne d'essai C-1 (a)")

    def inattendue(*a, **k):
        raise KeyError("panne inattendue C-1 (b)")
    for k, panne in enumerate((garde, inattendue)):
        monkeypatch.setattr(mc, "calculer", panne)
        run = f"20261114-18000{k}-mots-et-cout-t06-jouet"
        capsys.readouterr()
        assert mc.main(args(run)) == mc.CODE_ARRET == 3
        sortie = capsys.readouterr()
        assert "ARRÊT (après le manifeste" in sortie.err and sortie.out == ""
        d = r / "diag" / run
        assert sorted(p.name for p in d.iterdir()) == [mc.FICHIER_ARRET, mc.FICHIER_ARRET + ".sha256"]
        assert (d / (mc.FICHIER_ARRET + ".sha256")).read_text().split()[0] == mc.sha256_fichier(d / mc.FICHIER_ARRET)
        a = json.loads((d / mc.FICHIER_ARRET).read_text())
        assert a["lignes"]["BA-L0"]["s_applique"] and ("C-1 (a)" if k == 0 else "C-1 (b)") in a["lignes"]["BA-L0"]["phrase"]
        assert a["motif"].startswith("ArretPiece" if k == 0 else "KeyError")
        assert (r / "runs" / run / "manifeste.json").is_file() and a["manifeste_sha256"] == mc.sha256_fichier(
            r / "runs" / run / "manifeste.json")
        git(r, "add", "-A")
        git(r, "commit", "-q", "-m", f"arrêt {k}")
    monkeypatch.setattr(mc, "calculer", vrai_calculer)
    # refus avant le manifeste par une garde (arbre de travail sale) : 2, rien d'écrit
    (r / "notes.txt").write_text("x")
    run = "20261114-180002-mots-et-cout-t06-jouet"
    capsys.readouterr()
    assert mc.main(args(run)) == mc.CODE_REFUS == 2
    assert "REFUS (rien n'est écrit)" in capsys.readouterr().err
    assert not (r / "diag" / run).exists() and not (r / "runs" / run).exists()
    (r / "notes.txt").unlink()
    # refus avant le manifeste par une erreur inattendue : 2, rien d'écrit
    def lecture_en_panne(*a, **k):
        raise KeyError("panne inattendue avant le manifeste")
    monkeypatch.setattr(mc, "lire_entrees", lecture_en_panne)
    run = "20261114-180003-mots-et-cout-t06-jouet"
    assert mc.main(args(run)) == mc.CODE_REFUS
    assert "erreur inattendue avant le manifeste" in capsys.readouterr().err
    assert not (r / "diag" / run).exists() and not (r / "runs" / run).exists()
    monkeypatch.setattr(mc, "lire_entrees", vrai_lire)
    # cas sain : 0 ; trois fichiers et le manifeste, sortie sans valeur
    run = "20261114-180004-mots-et-cout-t06-jouet"
    assert mc.main(args(run)) == mc.CODE_OK == 0
    sortie = capsys.readouterr()
    assert sorted(p.name for p in (r / "diag" / run).iterdir() if not p.name.endswith(".sha256")) == sorted(
        (mc.FICHIER_DETAILS, mc.FICHIER_BASE_A, mc.FICHIER_ISSUE))
    assert len(sortie.out.strip().splitlines()) == 5 and not re.search(r"\d[.,]\d", sortie.out)


# ------------------------------------------------------------------------- C-3 : aucune valeur dans les motifs
def test_c3_chaque_refus_de_valider_issue_sans_valeur(run_sain):
    """C-3 : chaque refus de `valider_issue` est forcé (un cas par motif) ; le motif est celui attendu et ne porte ni nombre
    décimal, ni la valeur forcée (aire, état, étiquette, base, nombre de permutations, clé lue)."""
    r, s = run_sain
    doc = json.loads((r / "diag" / s["run_id"] / mc.FICHIER_ISSUE).read_text())
    mc.valider_issue(doc, 200)
    calc = next(d for d in mc.DOSES if doc["doses"][d]["etat"] in ("réussit", "échoue"))
    x0 = doc["doses"][calc]
    autre_etat = "échoue" if x0["etat"] == "réussit" else "réussit"
    autre_base = "mots_et_cout" if x0["base_decisive"] == "N-029" else "N-029"
    autre_m = "M3" if doc["issue_mots_et_cout"] != "M3" else "M1"
    ref = x0["aire_n029"] if x0["base_decisive"] == "N-029" else x0["aire_mots_et_cout"]
    V = 0.987654

    def dose(**k):
        return lambda x: x["doses"][calc].update(**k)
    cas = [  # (altération, fragment attendu du motif, valeurs qui ne doivent pas y paraître)
        (lambda x: x.update(cle_de_plus=V), "clés de premier niveau", ()),
        (None, "clés de premier niveau", ()),                                          # document non objet : [V]
        (lambda x: x.update(doses=V), "doses S25 à S100", ()),
        (lambda x: x["doses"].update({calc: V}), f"doses.{calc} : champs", ()),
        (dose(champ_de_plus=V), f"doses.{calc} : champs", ("champ_de_plus",)),
        (dose(etat="inconnu"), f"doses.{calc}.etat hors de son domaine", ("inconnu",)),
        (dose(n_permutations=17), f"doses.{calc}.n_permutations", ("17",)),
        (dose(niveau=V), f"doses.{calc} : niveau ou seuil_aire", ()),
        (dose(effet_cout={"estimation": V}), f"doses.{calc}.effet_cout", ()),
        (dose(etat="non calculable"), f"doses.{calc} non calculable : champs non nuls", ()),
        (dose(aire_n029=1.0 + V), f"doses.{calc}.aire_n029 non fini ou hors de [0, 1]", ("1.98",)),
        (dose(base_decisive=autre_base), f"doses.{calc}.base_decisive", (autre_base,)),
        (dose(aire=ref - 1e-12), f"doses.{calc}.aire ≠ aire de la base décisive", ()),
        (dose(etat=autre_etat), f"doses.{calc}.etat ≠ état recalculé", ("réussit", "échoue")),
        (lambda x: x.update(issue_mots_et_cout=autre_m), "étiquette ≠ étiquette recalculée", ("M1", "M2", "M3", "M4")),
        (lambda x: x.update(phrase=f"phrase {V}"), "phrase ≠ phrase gelée", ()),
        (lambda x: x.update(doses_qualifiees=[V]), "doses_qualifiees", ()),
        (lambda x: x["plis"].update({next(iter(x["plis"])): V}), "plis {tâche : 0 ou 1}", ()),
        (lambda x: x.update(taux_detection_1pc=V), "taux_detection_1pc par dose attendu", ()),
        (lambda x: x["taux_detection_1pc"].update({calc: None}), f"taux_detection_1pc.{calc} présent si et seulement si", ()),
        (lambda x: x["taux_detection_1pc"].update({calc: {"N-029": V}}), f"taux_detection_1pc.{calc} : bases", ()),
        (lambda x: x.update(run_id=f"run-{V}"), "run_id ou manifeste_sha256 hors format", ()),
        (lambda x: x.update(manifeste_sha256=f"{V}"), "run_id ou manifeste_sha256 hors format", ()),
    ]
    vus = set()
    for f, fragment, absentes in cas:
        x = copy.deepcopy(doc)
        if f is None:
            x = [V]
        else:
            f(x)
        with pytest.raises(mc.ArretPiece) as e:
            mc.valider_issue(x, 200)
        motif = str(e.value)
        assert motif.startswith("issue : ") and fragment in motif, (fragment, motif)
        assert not re.search(r"\d[.,]\d", motif), motif
        assert not any(a in motif for a in absentes), motif
        vus.add(fragment.replace(calc, "<d>"))
    assert len(vus) == 20          # vingt motifs distincts : les vingt refus de valider_issue
