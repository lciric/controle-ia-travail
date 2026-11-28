import ast
import hashlib
import importlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import types
from pathlib import Path

sys.dont_write_bytecode = True

racine_repo = Path("C:/Users/lciri/controle-ia-travail").resolve()
source_v621 = (racine_repo / "recu-v6-2-1" / "organisme").resolve()
cible_org = (racine_repo / "organisme").resolve()

if not (source_v621 / "CORRECTIONS-v5.md").exists():
    print(f"ERREUR : La source v6.2.1 est introuvable dans {source_v621}")
    sys.exit(1)

# 1. Copie propre de la base v6.2.1 (26 fichiers) dans organisme/
if cible_org.exists():
    shutil.rmtree(cible_org)
shutil.copytree(
    source_v621,
    cible_org,
    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
)
print(f"=== 1. BASE V6.2.1 RESTAUREE PROPREMENT DANS {cible_org} ===")


def remplacer_fonction_ast(chemin_fichier: Path, nom_fonction: str, nouveau_code_src: str) -> None:
    """Remplace une fonction de premier niveau par son nom exact via l'AST Python."""
    src = chemin_fichier.read_text(encoding="utf-8")
    lignes = src.splitlines()
    arbre = ast.parse(src)
    for noeud in arbre.body:
        if isinstance(noeud, ast.FunctionDef) and noeud.name == nom_fonction:
            debut = noeud.lineno - 1
            fin = noeud.end_lineno
            nouvelles_lignes = (
                lignes[:debut]
                + nouveau_code_src.strip("\n").splitlines()
                + lignes[fin:]
            )
            chemin_fichier.write_text("\n".join(nouvelles_lignes) + "\n", encoding="utf-8")
            return
    raise RuntimeError(f"Fonction {nom_fonction} introuvable dans {chemin_fichier}")


# =====================================================================================================================
# 2. BRIQUE M-01 DANS memoire_isvd.py : SIMHASH SUR N-GRAMMES + CENTRAGE EXACT DU BLOC QUADRATIQUE v^2
# =====================================================================================================================
p_isvd = cible_org / "memoire_isvd.py"

code_vectoriser_m01 = '''
def _extraire_ngrammes_morphologiques(mot: str) -> list:
    """M-01 (v6.3.0) : SimHash morphologique sur préfixe et 4-grammes de caractères."""
    m = mot.strip().lower()
    if len(m) <= 4:
        return [m]
    grams = [m[:6]]
    for i in range(len(m) - 3):
        grams.append(m[i : i + 4])
    return grams[:6]


def _vectoriser_texte_base(texte: str, dim_base: int = DIM_BASE) -> list:
    vec = [0.0] * dim_base
    mots = re.findall(r"[a-zA-Z0-9_-]{3,}", (texte or "").lower())
    if not mots:
        return vec
    for m in mots:
        poids_mot = 1.5 if len(m) >= 7 else 1.0
        grams = _extraire_ngrammes_morphologiques(m)
        poids_g = poids_mot / float(len(grams))
        for g in grams:
            h = hashlib.sha256(g.encode("utf-8")).digest()
            idx = h[0] % dim_base
            signe = 1.0 if (h[1] % 2 == 0) else -1.0
            vec[idx] += signe * poids_g
    norme = math.sqrt(sum(x * x for x in vec))
    if norme > 1e-12:
        vec = [x / norme for x in vec]
    return vec
'''

code_koopman_m01 = '''
def relever_observables_koopman(texte: str) -> list:
    """M-01 (v6.3.0, rectificatif conv-audit) : Le bloc quadratique v^2 = (v_1^2, ..., v_d^2) étant
    strictement positif de somme 1, il créait une direction moyenne commune responsable de l'inflation
    de sigma_1. On soustrait la moyenne exacte 1/d de chaque composante quadratique (somme nulle)
    puis on normalise le vecteur d'observables."""
    v = _vectoriser_texte_base(texte, DIM_BASE)
    mots_uniques = set(re.findall(r"[a-zA-Z0-9_-]{4,}", (texte or "").lower()))
    if not mots_uniques:
        return [0.0] * (DIM_BASE * 3)
    echelle = min(1.35, 0.75 + 0.12 * math.log1p(len(mots_uniques)))
    moy_v2 = sum(x * x for x in v) / float(DIM_BASE)
    obs = []
    for x in v:
        obs.append(x)
    for x in v:
        obs.append(math.sin(x))
    for x in v:
        obs.append((x * x) - moy_v2)
    norme_obs = math.sqrt(sum(z * z for z in obs))
    if norme_obs > 1e-12:
        obs = [(z / norme_obs) * echelle for z in obs]
    return obs
'''

remplacer_fonction_ast(p_isvd, "_vectoriser_texte_base", code_vectoriser_m01)
remplacer_fonction_ast(p_isvd, "relever_observables_koopman", code_koopman_m01)
print("=== 2. M-01 APPLIQUE DANS memoire_isvd.py (SimHash n-grammes + Centrage exact de v^2) ===")

# =====================================================================================================================
# 3. BRIQUE M-02 DANS mitose_spectrale.py : LISTE RIGOUREUSE DE MOTS VIDES BILINGUES FR/EN ET METALANGAGE
# =====================================================================================================================
p_mitose = cible_org / "mitose_spectrale.py"
src_mitose = p_mitose.read_text(encoding="utf-8")

mots_vides_enrichis = '''MOTS_VIDES_SPECTRAUX_V63 = {
    "dans", "pour", "avec", "sans", "plus", "moins", "comme", "cette", "sont", "mais",
    "tout", "tous", "toute", "toutes", "une", "des", "les", "aux", "sur", "par", "que",
    "qui", "est", "pas", "son", "ses", "leur", "leurs", "entre", "vers", "sous", "tres",
    "meme", "aussi", "donc", "ainsi", "alors", "apres", "avant", "depuis", "contre",
    "the", "and", "for", "with", "from", "that", "this", "have", "which", "their",
    "are", "was", "were", "been", "being", "into", "over", "under", "between", "through",
    "confiance", "incertitude", "position", "caste", "castes", "question", "reponse",
    "etiquette", "constat", "article", "articles", "modele", "modeles", "analyse",
    "attaque", "colmatage", "faille", "failles", "protocole", "seuil", "metrique",
    "aire", "aires", "angles", "canisme", "canique", "cha", "art", "auto", "bruit",
}
'''

if "MOTS_VIDES_SPECTRAUX_V63" not in src_mitose:
    src_mitose = mots_vides_enrichis + "\n" + src_mitose
    src_mitose = src_mitose.replace(
        'if m not in ("dans", "pour", "avec", "sans", "plus", "moins", "comme", "cette", "sont")',
        "if m not in MOTS_VIDES_SPECTRAUX_V63 and len(m) >= 5",
    )
    src_mitose = src_mitose.replace(
        'stop = {"dans", "pour", "avec", "sans", "plus", "moins", "comme", "cette", "sont", "mais", "tout", "tous"}',
        "stop = MOTS_VIDES_SPECTRAUX_V63",
    )
    p_mitose.write_text(src_mitose, encoding="utf-8")
print("=== 3. M-02 APPLIQUE DANS mitose_spectrale.py (Filtrage strict des mots-outils FR/EN et metalangage) ===")

# =====================================================================================================================
# 4. BRIQUES M-03 & M-04 DANS principal.py : DPP PSD (DOMAINE DANS LE NOYAU, OPERATEUR DANS LA QUALITE) + FILTRE DE CONTRAINTES
# =====================================================================================================================
p_prin = cible_org / "principal.py"
src_prin = p_prin.read_text(encoding="utf-8")
src_prin = src_prin.replace('VERSION = "organisme-gemini-m3-v6-2-1"', 'VERSION = "organisme-gemini-m3-v6-3-0"', 1)

code_dpp_et_contraintes_v63 = '''
MOTS_OPERATEURS_MATH_V63 = {
    "martingale", "bound", "theorem", "lemma", "eigenvalue", "covariance", "minimax", "divergence",
    "wasserstein", "entropy", "orthogonal", "kernel", "variance", "stopping", "conformal", "rank",
    "spectrum", "projection", "gradient", "convex", "inequality", "asymptotic", "likelihood", "subspace",
    "laplacian", "cohomology", "sheaf", "symplectic", "signature", "ricci", "hashimoto", "schrodinger",
}

CONTRAINTES_REGIMES_V63 = {
    "echantillon_fini": ("finite-sample", "non-asymptotic", "small-batch", "short-horizon", "finite blocklength"),
    "asymptotique": ("asymptotic", "infinite-horizon", "large-sample", "ergodic", "stationary"),
    "boite_blanche": ("activation", "residual", "probe", "layer", "kv-cache", "attention", "gradient", "jacobian"),
    "boite_noire": ("black-box", "density-free", "query-only", "text-only", "api"),
}


def _extraire_profil_article_v63(article: dict, question: str = "", mission: str = "") -> dict:
    """M-03 & M-04 (v6.3.0, rectificatif conv-audit) :
    - Calcule la qualité d'opérateur q_i normalisée par la racine de la longueur (sans biais pour les textes bavards) ;
    - Extrait le vecteur unitaire de domaine v_dom (hors mots d'opérateurs) pour construire le noyau de Gram PSD ;
    - Extrait les contraintes de régime pour filtrer les incompatibilités axiomatiques."""
    texte = f"{article.get('titre', '')} {article.get('resume', '')}".lower()
    mots = re.findall(r"[a-z][a-z0-9_-]{3,}", texte)
    stop_dom = {
        "with", "from", "that", "this", "have", "which", "their", "paper", "show", "model",
        "models", "data", "using", "based", "method", "results", "approach", "proposed",
    } | MOTS_OPERATEURS_MATH_V63

    v_dom = {}
    ops_presents = set()
    for m in mots:
        if m in MOTS_OPERATEURS_MATH_V63:
            ops_presents.add(m)
        elif m not in stop_dom and len(m) >= 5:
            v_dom[m] = v_dom.get(m, 0.0) + 1.0

    norme_dom = math.sqrt(sum(val * val for val in v_dom.values())) or 1.0
    v_dom_unit = {k: val / norme_dom for k, val in v_dom.items()}

    nb_mots_utiles = max(8, len(mots))
    densite_op = len(ops_presents) / math.sqrt(float(nb_mots_utiles))
    pertinence_base = _score_pertinence_texte(texte, question, mission)
    qualite_q = max(0.15, min(2.5, 0.40 * pertinence_base + 1.20 * densite_op))

    regimes = set()
    for nom_reg, marqueurs in CONTRAINTES_REGIMES_V63.items():
        if any(mq in texte for mq in marqueurs):
            regimes.add(nom_reg)

    return {
        "qualite_q": round(qualite_q, 6),
        "v_dom": v_dom_unit,
        "ops": sorted(ops_presents),
        "regimes": regimes,
    }


def construire_noyau_dpp_domaine_operateur(articles: list, question: str = "", mission: str = "") -> list:
    """M-03 (v6.3.0, rectificatif conv-audit) :
    Dans un DPP de matrice L_ij = q_i * Phi_ij * q_j, maximiser det(L_S) répousse les paires où Phi_ij est grand.
    On place donc :
    - la pertinence des opérateurs mathématiques dans le poids de qualité q_i ;
    - la ressemblance des domaines Phi_ij = <v_dom(i), v_dom(j)> dans le noyau de Gram (trivialement PSD car Phi = V V^T).
    Ainsi, l'élimination de Cholesky sélectionne des articles à forte densité d'opérateurs (q_i grand)
    et de domaines mutuellement éloignés (Phi_ij petit)."""
    n = len(articles)
    if n == 0:
        return []
    profils = [_extraire_profil_article_v63(a, question, mission) for a in articles]
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        qi = profils[i]["qualite_q"]
        vi = profils[i]["v_dom"]
        for j in range(i, n):
            qj = profils[j]["qualite_q"]
            vj = profils[j]["v_dom"]
            phi_ij = 1.0 if i == j else sum(val * vj.get(cle, 0.0) for cle, val in vi.items())
            val_l = qi * phi_ij * qj
            if i == j:
                val_l += 0.05 * (qi * qi)
            L[i][j] = round(val_l, 8)
            L[j][i] = round(val_l, 8)
    return L


def selectionner_articles_dpp_et_filtrer_contraintes(
    articles: list, question: str = "", mission: str = "", k: int = 12
) -> tuple:
    """M-03 & M-04 (v6.3.0) : Sélection gloutonne MAP-DPP par Cholesky sur L_ij = q_i <v_dom_i, v_dom_j> q_j,
    suivie du filtre de compatibilité des contraintes de régimes entre articles de domaines éloignés."""
    n = len(articles)
    if n == 0:
        return [], []
    k_eff = min(k, n)
    L = construire_noyau_dpp_domaine_operateur(articles, question=question, mission=mission)
    profils = [_extraire_profil_article_v63(a, question, mission) for a in articles]

    diags = [max(1e-12, L[i][i]) for i in range(n)]
    C = [[0.0] * n for _ in range(k_eff)]
    selection = []
    restants = set(range(n))

    for etape in range(k_eff):
        best_i = max(restants, key=lambda idx: (diags[idx], -idx))
        if diags[best_i] <= 1e-11 and selection:
            break
        selection.append(best_i)
        restants.remove(best_i)
        racine_d = math.sqrt(max(1e-12, diags[best_i]))
        for j in restants:
            s = sum(C[p][best_i] * C[p][j] for p in range(etape))
            c_ej = (L[best_i][j] - s) / racine_d
            C[etape][j] = c_ej
            diags[j] = max(0.0, diags[j] - (c_ej * c_ej))

    articles_retenus = [articles[i] for i in selection]

    paires_compatibles = []
    for idx_a in range(len(selection)):
        for idx_b in range(idx_a + 1, len(selection)):
            i, j = selection[idx_a], selection[idx_b]
            pi, pj = profils[i], profils[j]
            sim_dom = sum(val * pj["v_dom"].get(cle, 0.0) for cle, val in pi["v_dom"].items())
            if sim_dom > 0.35:
                continue
            reg_i, reg_j = pi["regimes"], pj["regimes"]
            incompatibles = (
                ("boite_blanche" in reg_i and "boite_noire" in reg_j and "boite_blanche" not in reg_j)
                or ("boite_noire" in reg_i and "boite_blanche" in reg_j and "boite_noire" not in reg_j)
                or ("echantillon_fini" in reg_i and "asymptotique" in reg_j and "echantillon_fini" not in reg_j)
                or ("asymptotique" in reg_i and "echantillon_fini" in reg_j and "asymptotique" not in reg_j)
            )
            if incompatibles:
                continue
            ops_partages = sorted(set(pi["ops"]) & set(pj["ops"]))
            score_couple = (1.0 - sim_dom) * min(pi["qualite_q"], pj["qualite_q"]) * (1.0 + 0.25 * len(ops_partages))
            paires_compatibles.append((
                score_couple,
                {
                    "article_A": str(articles[i].get("titre", ""))[:65],
                    "article_B": str(articles[j].get("titre", ""))[:65],
                    "distance_domaine": round(1.0 - sim_dom, 4),
                    "operateurs_partages": ops_partages[:4],
                    "regimes_compatibles": sorted(reg_i | reg_j),
                },
            ))
    paires_compatibles.sort(key=lambda x: x[0], reverse=True)
    return articles_retenus, [p for _, p in paires_compatibles[:3]]
'''

if "construire_noyau_dpp_domaine_operateur" not in src_prin:
    src_prin = src_prin.replace("def _score_pertinence_texte(", code_dpp_et_contraintes_v63 + "\n\ndef _score_pertinence_texte(", 1)
    src_prin = re.sub(
        r"articles_uniques\.sort\(\s*key=lambda x: _score_pertinence_texte\([^)]+\),\s*reverse=True,\s*\)\s*retenus = articles_uniques\[:12\]",
        "retenus, paires_compatibles_v63 = selectionner_articles_dpp_et_filtrer_contraintes(articles_uniques, question=question, mission=mission, k=12)",
        src_prin,
        count=1,
    )
    src_prin = src_prin.replace(
        "for idx, art in enumerate(retenus[:8], start=1):",
        '''if paires_compatibles_v63:
        lignes_extrait.append("Paires inter-domaines compatibles sous filtre de contraintes (M-03/M-04) :")
        for idx_p, pt in enumerate(paires_compatibles_v63, start=1):
            lignes_extrait.append(
                f"  * Couple #{idx_p} (dist_dom={pt['distance_domaine']}, ops={pt['operateurs_partages']}, regimes={pt['regimes_compatibles']}) : "
                f"[{pt['article_A']}] <--> [{pt['article_B']}]"
            )
    for idx, art in enumerate(retenus[:8], start=1):''',
        1,
    )
    p_prin.write_text(src_prin, encoding="utf-8")
print("=== 4. M-03 & M-04 APPLIQUES DANS principal.py (DPP PSD + Filtre de compatibilite des contraintes) ===")

# 5. Mise à jour de manifeste.json, CORRECTIONS-v6-meta.md et tests/test_meta_conception_v6_3.py
p_man = cible_org / "manifeste.json"
man_data = json.loads(p_man.read_text(encoding="utf-8"))
man_data["version"] = "6.3.0"
man_data["description"] = (
    "Organisme Auto-Architecte v6.3.0 (lignee assistee, issu de la v6.2.1 7ea3270 + rectificatifs de conv-audit sur la Meta-Conception) : "
    "C-01 a C-17 conservees + M-01 (SimHash morphologique sur n-grammes et centrage exact du bloc quadratique v^2 de Koopman), "
    "M-02 (filtrage rigoureux des mots-outils FR/EN et du metalangage dans mitose_spectrale), "
    "M-03 (noyau DPP strictement PSD avec eloignement des domaines dans le noyau de Gram et pertinence des operateurs dans le poids de qualite), "
    "M-04 (filtre de compatibilite des contraintes de regimes normalise contre les textes bavards)."
)
p_man.write_text(json.dumps(man_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

doc_v63 = """# Corrections et améliorations de Méta-Conception v6.3.0 (intégrant la relecture de `conv-audit`)

Base de départ : la **v6.2.1** (`7ea32705c5437d91ed071dd95fb3209bb0b0035e`, 26 fichiers, empreinte d'arbre `4f13647a...`).
Toutes les corrections **C-01 à C-17** (`CORRECTIONS-v1.md` à `CORRECTIONS-v5.md`) et leurs **68 essais** sont intégralement conservés sans aucune retouche.

| Brique | Fichier | Diagnostic rectifié avec `conv-audit` | Implémentation en `v6.3.0` | Essais (`tests/test_meta_conception_v6_3.py`) |
|---|---|---|---|---|
| **M-01** | `memoire_isvd.py` | `_vectoriser_texte_base` normait déjà `v` à 1 ; l'inflation de $\\sigma_1 = 269$ provenait du bloc quadratique $v^2 \\ge 0$ qui donnait à tous les vecteurs une direction moyenne positive commune | SimHash sur n-grammes (`_extraire_ngrammes_morphologiques`) + soustraction de la moyenne exacte $\\frac{1}{d}\\sum v_i^2$ sur chaque coordonnée quadratique de `relever_observables_koopman` | `test_m01_simhash_morphologique_racines_proches` ; `test_m01_centrage_bloc_quadratique_koopman_moyenne_nulle` |
| **M-02** | `mitose_spectrale.py` | Les `termes_satures` réels observés dans les traces étaient des mots-outils bilingues FR/EN et du métalangage (`article`, `dans`, `avec`, `and`) | Ajout de `MOTS_VIDES_SPECTRAUX_V63` (mots-outils FR/EN et métalangage) et seuil de longueur $\\ge 5$ caractères | `test_m02_mots_outils_bilingues_exclus_des_termes_satures` ; `test_m02_termes_techniques_reels_detectes` |
| **M-03** | `principal.py` | Dans un DPP $L_{ij} = q_i \\Phi_{ij} q_j$, maximiser $\\det(L_S)$ répousse les grandes valeurs de $\\Phi_{ij}$ : il faut donc mettre la **ressemblance des domaines** dans le noyau de Gram PSD $\\Phi_{ij} = \\langle v_{\\text{dom}}(i), v_{\\text{dom}}(j)\\rangle$ et la **pertinence des opérateurs** dans la qualité $q_i$ | `construire_noyau_dpp_domaine_operateur` : noyau de Gram PSD sur les domaines + qualité $q_i$ sur la densité d'opérateurs normalisée par $\\sqrt{\\text{longueur}}$ | `test_m03_noyau_dpp_strictement_psd_cholesky` ; `test_m03_dpp_favorise_eloignement_domaines_et_qualite_operateurs` |
| **M-04** | `principal.py` | Le score de pushout naïf récompensait les textes bavards ; la vraie brique utile est le filtre de compatibilité des contraintes de régimes | `selectionner_articles_dpp_et_filtrer_contraintes` : rejette les paires aux régimes mutuellement exclusifs (`boite_blanche` vs `boite_noire`, `echantillon_fini` vs `asymptotique`) et normalise $q_i$ contre le bavardage | `test_m04_filtre_incompatibilite_regimes_exclusifs` ; `test_m04_normalisation_anti_bavardage_et_integration_executer` |
"""
(cible_org / "CORRECTIONS-v6-meta.md").write_text(doc_v63, encoding="utf-8")

tests_v63 = '''"""Essais unitaires des 4 briques rectifiées M-01 à M-04 de la v6.3.0."""
import importlib
import math
import sys
import types
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))

import memoire_isvd
import mitose_spectrale
import principal


def test_m01_simhash_morphologique_racines_proches():
    v1 = memoire_isvd._vectoriser_texte_base("conformal prediction sequential martingale calibration")
    v2 = memoire_isvd._vectoriser_texte_base("conformalized predicting sequentially martingales calibrated")
    v3 = memoire_isvd._vectoriser_texte_base("ribosome protein transcription cellular metabolism")
    sim_12 = sum(a * b for a, b in zip(v1, v2))
    sim_13 = sum(a * b for a, b in zip(v1, v3))
    assert sim_12 > 0.65 and sim_12 > sim_13 + 0.30


def test_m01_centrage_bloc_quadratique_koopman_moyenne_nulle():
    obs = memoire_isvd.relever_observables_koopman("martingale sequential bound theorem covariance eigenvalue")
    d = memoire_isvd.DIM_BASE
    bloc_quadratique = obs[2 * d : 3 * d]
    assert abs(sum(bloc_quadratique)) < 1e-9


def test_m02_mots_outils_bilingues_exclus_des_termes_satures():
    textes = [
        "Dans cet article the model with pour avec sans martingale",
        "Dans cet article the model with pour avec sans martingale",
    ]
    bilan = mitose_spectrale.calculer_capacite_shannon_gram(textes)
    for mot_outil in ("dans", "article", "avec", "pour", "with", "that", "model"):
        assert mot_outil not in bilan["termes_satures"]
    assert "martingale" in bilan["termes_satures"]


def test_m02_termes_techniques_reels_detectes():
    textes = [
        "operateur symplectique cohomologie faisceau martingale",
        "operateur symplectique cohomologie faisceau wasserstein",
    ]
    bilan = mitose_spectrale.calculer_capacite_shannon_gram(textes)
    assert "symplectique" in bilan["termes_satures"] or "cohomologie" in bilan["termes_satures"]


def test_m03_noyau_dpp_strictement_psd_cholesky():
    articles = [
        {"id": "a1", "source": "arxiv", "titre": "Radar Detection", "resume": "radar sonar antenna martingale bound theorem covariance", "lien": ""},
        {"id": "a2", "source": "arxiv", "titre": "Radar Array", "resume": "radar sonar array martingale bound eigenvalue", "lien": ""},
        {"id": "a3", "source": "openalex", "titre": "Optics Laser", "resume": "laser photon cavity martingale bound wasserstein", "lien": ""},
    ]
    L = principal.construire_noyau_dpp_domaine_operateur(articles, question="martingale bound", mission="detection")
    n = len(L)
    chol = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(chol[i][k] * chol[j][k] for k in range(j))
            if i == j:
                assert L[i][i] - s > 1e-9
                chol[i][j] = math.sqrt(L[i][i] - s)
            else:
                chol[i][j] = (L[i][j] - s) / chol[j][j]


def test_m03_dpp_favorise_eloignement_domaines_et_qualite_operateurs():
    articles = [
        {"id": "domA_1", "source": "arxiv", "titre": "Radar Clutter 1", "resume": "radar clutter doppler antenna sonar martingale theorem bound covariance", "lien": ""},
        {"id": "domA_2", "source": "arxiv", "titre": "Radar Clutter 2", "resume": "radar clutter doppler antenna sonar martingale theorem bound", "lien": ""},
        {"id": "domB_1", "source": "openalex", "titre": "Genomic Sequencing", "resume": "genome nucleotide chromosome allele martingale theorem bound covariance", "lien": ""},
    ]
    retenus, _ = principal.selectionner_articles_dpp_et_filtrer_contraintes(articles, question="martingale bound", mission="control", k=2)
    ids_ret = {a["id"] for a in retenus}
    assert ids_ret == {"domA_1", "domB_1"}


def test_m04_filtre_incompatibilite_regimes_exclusifs():
    articles = [
        {"id": "wb", "source": "arxiv", "titre": "White-Box Probe", "resume": "activation residual layer jacobian martingale theorem", "lien": ""},
        {"id": "bb", "source": "openalex", "titre": "Black-Box API", "resume": "black-box query-only text-only api martingale theorem", "lien": ""},
        {"id": "wb2", "source": "arxiv", "titre": "Optics White-Box", "resume": "photon cavity laser activation residual layer martingale theorem", "lien": ""},
    ]
    _, paires = principal.selectionner_articles_dpp_et_filtrer_contraintes(articles, question="martingale", mission="control", k=3)
    for p in paires:
        assert not ("White-Box Probe" in p["article_A"] and "Black-Box API" in p["article_B"])
        assert not ("Black-Box API" in p["article_A"] and "White-Box Probe" in p["article_B"])


def test_m04_normalisation_anti_bavardage_et_integration_executer(tmp_path, monkeypatch):
    court_dense = {"titre": "Concise Theorem", "resume": "martingale bound theorem eigenvalue covariance wasserstein"}
    long_bavard = {"titre": "Verbose Text", "resume": "martingale bound " + " ".join(["blabla_filler_word"] * 200)}
    p_court = principal._extraire_profil_article_v63(court_dense)
    p_long = principal._extraire_profil_article_v63(long_bavard)
    assert p_court["qualite_q"] > p_long["qualite_q"]

    module = types.ModuleType("noyau_client")
    module.especes = lambda: ["CLAUDE_FABLE_5_1", "GEMINI_4_ARGON"]
    module.budget = lambda: {
        "appels_restants": 10, "usd_restants": 5.0, "recherches_restantes": 2,
        "sources": ["arxiv"], "telechargements_restants": 1, "octets_restants": 100000,
        "entrainements_restants": 0, "max_tokens_appel": 4096,
    }
    module.rechercher = lambda req, n=5, role="", source="arxiv": {
        "statut": "OK", "source": source, "identifiant": "r1", "echec": None,
        "resultats": [
            {"source": source, "id": "a1", "titre": "Radar Sequential", "auteurs": "A", "date": "2026", "resume": "radar sonar antenna finite-sample martingale theorem bound", "lien": "https://arxiv.org/abs/2501.00001"},
            {"source": source, "id": "a2", "titre": "Optics Cavity", "auteurs": "B", "date": "2026", "resume": "laser photon optics finite-sample martingale theorem bound", "lien": "https://arxiv.org/abs/2501.00002"},
        ],
    }
    module.telecharger = lambda ref, role="": {"statut": "OK", "identifiant": "t1", "adresse": ref, "genre": "article", "titre": "T", "octets": 30, "sha256_brut": "h", "sha256_texte": "h", "texte": "Contenu.", "tronque": False, "caracteres_texte": 8, "fichier_texte": None, "echec": None}
    module.appeler = lambda esp, pr, max_tokens=None, role="": {
        "statut": "OK",
        "texte": '{"requetes": ["q1"]}' if role == "moissonneur_formulation_requetes" else 'Analyse.\n{"position": "OK", "confiance": 0.9, "incertitude": "ras"}',
        "modele_servi": esp, "fin": "stop", "usage": {}, "cout_usd": 0.01, "identifiant": "c1", "echec": None,
    }
    monkeypatch.setitem(sys.modules, "noyau_client", module)
    importlib.reload(principal)
    bilan = principal.executer({
        "generation": 1, "phase": "generation", "lignee": "v6-3", "mission": "Mission.",
        "dossier_travail": str(tmp_path / "run_v63"), "dossier_archive": "",
        "taches_entrainement": [], "taches_test": [], "question_ouverte": "Question programme ?",
        "budget": {"appels_max": 10, "usd_max": 5.0, "temps_max_s": 120, "recherches_max": 2, "telechargements_max": 1, "octets_max": 100000},
        "historique": [],
    })
    assert bilan["version"] == "organisme-gemini-m3-v6-3-0"
'''
(cible_org / "tests" / "test_meta_conception_v6_3.py").write_text(tests_v63, encoding="utf-8")

# 6. Exécution de pytest sur les 76 essais (68 de v6.2.1 + 8 de v6.3.0)
print("=== 5. EXECUTION DE PYTEST SUR LES 76 ESSAIS DE organisme/ ===")
res_pytest = subprocess.run([sys.executable, "-m", "pytest", str(cible_org / "tests"), "-q"], capture_output=True, text=True)
print(res_pytest.stdout)
if res_pytest.returncode != 0:
    print(res_pytest.stderr)
    sys.exit(res_pytest.returncode)

# Nettoyage des __pycache__ et .pytest_cache avant calcul des empreintes
for d_cache in list(cible_org.rglob("__pycache__")) + list(cible_org.rglob(".pytest_cache")):
    if d_cache.exists():
        shutil.rmtree(d_cache, ignore_errors=True)

# 7. Calcul des empreintes SHA-256 des 28 fichiers de organisme/
fichiers_org = sorted([p for p in cible_org.rglob("*") if p.is_file()], key=lambda x: x.relative_to(racine_repo).as_posix())
lignes_emp = []
for f_p in fichiers_org:
    rel = f_p.relative_to(racine_repo).as_posix()
    sha = hashlib.sha256(f_p.read_bytes()).hexdigest().lower()
    lignes_emp.append(f"{sha}  {rel}")

dossier_livraison = racine_repo / "brouillons" / "livraison-claude-organisme-v6-3-0"
dossier_livraison.mkdir(parents=True, exist_ok=True)
(dossier_livraison / "EMPREINTES-organisme-v6-3-0.txt").write_text("\n".join(lignes_emp) + "\n", encoding="utf-8")

lisezmoi_claude = """# Livraison de l'organisme `v6.3.0` pour Claude (`conv-audit`)

- **Point de départ** : la `v6.2.1` (`7ea32705c5437d91ed071dd95fb3209bb0b0035e`, 26 fichiers, empreinte d'arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`).
- **Préservation intégrale** : `CORRECTIONS-v1.md` à `CORRECTIONS-v5.md` (`C-01` à `C-17`) et leurs **68 essais** sont intégralement conservés sans aucune retouche.
- **Ajouts de la `v6.3.0` (`VERSION = "organisme-gemini-m3-v6-3-0"`, 28 fichiers, 76 essais `OK`)** intégrant les 5 rectifications de `conv-audit` (`relecture-meta-conception-v6-3-v1.md`) :
  1. **M-01 (`memoire_isvd.py`)** : SimHash morphologique sur n-grammes (`_extraire_ngrammes_morphologiques`) et **centrage exact du bloc quadratique** $v_i^2 - \\frac{1}{d}\\sum_j v_j^2$ dans `relever_observables_koopman` (qui élimine la direction moyenne positive commune dans $\\mathbb{R}_+^d$ responsable de l'inflation de $\\sigma_1$).
  2. **M-02 (`mitose_spectrale.py`)** : Liste de mots vides bilingues FR/EN et de métalangage (`MOTS_VIDES_SPECTRAUX_V63`) + seuil de longueur $\\ge 5$, éliminant les mots-outils (`article`, `dans`, `avec`, `and`) de `termes_satures` sans machinerie de graphe de ligne.
  3. **M-03 (`principal.py`)** : `construire_noyau_dpp_domaine_operateur` : le noyau de Gram $\\Phi_{ij} = \\langle v_{\\text{dom}}(i), v_{\\text{dom}}(j)\\rangle$ mesure la ressemblance des domaines (trivialement PSD puisque $\\Phi = V V^\\top$, de sorte que maximiser $\\det(L_S)$ par Cholesky favorise l'éloignement des domaines) tandis que la pertinence des opérateurs mathématiques entre dans le poids de qualité $q_i$ (normalisé par $\\sqrt{\\text{longueur}}$ contre le bavardage).
  4. **M-04 (`principal.py`)** : `selectionner_articles_dpp_et_filtrer_contraintes` : filtre de compatibilité des contraintes de régimes (`boite_blanche` vs `boite_noire`, `echantillon_fini` vs `asymptotique`) entre articles de domaines éloignés.
  5. **Essais (`tests/test_meta_conception_v6_3.py`)** : 8 nouveaux essais vérifiant M-01 à M-04 (total : **76 passed**).
"""
(dossier_livraison / "LISEZMOI-pour-claude-v6-3-0.md").write_text(lisezmoi_claude, encoding="utf-8")
print(f"=== 6. {len(fichiers_org)} FICHIERS VERIFIES ET EMPREINTES ECRITES DANS {dossier_livraison / 'EMPREINTES-organisme-v6-3-0.txt'} ===")