"""Module de politique endogène de l'organisme v6.
Définit la fonction de récompense strictement propre, l'objectif de perte de sonde, la pondération mémorielle et les
seuils de routage, ainsi que le vérificateur mathématique et syntaxique (`verifier_et_valider_code_politique`)."""
import ast
import math

NOM_POLITIQUE = "bregman_tsallis_alpha_4_3_v6_initiale"
EXPOSANT_ALPHA = 4.0 / 3.0
POIDS_BRIER = 0.80
POIDS_LOG = 0.20


def recompense_interne(verite: int, q: float) -> float:
    """Combinaison convexe du score de Brier et du score logarithmique borné : strictement propre sur ]0, 1[."""
    q_c = max(1e-4, min(1.0 - 1e-4, float(q)))
    y = 1.0 if int(verite) == 1 else 0.0
    brier = (y - q_c) ** 2
    kl_bernoulli = (
        y * math.log(max(1e-6, y) / q_c) if y > 0.5 else (1.0 - y) * math.log(max(1e-6, 1.0 - y) / (1.0 - q_c))
    )
    return round(1.0 - (POIDS_BRIER * brier + POIDS_LOG * kl_bernoulli), 8)


def code_objectif_sonde() -> str:
    return """def perte(p, y):
    p_c = np.clip(p, 1e-4, 1.0 - 1e-4)
    brier = (p_c - y) ** 2
    ll_bornee = -(y * np.log(p_c) + (1.0 - y) * np.log(1.0 - p_c))
    return float(np.mean(0.80 * brier + 0.20 * ll_bornee))
"""


def ponderer_trace_memoire(texte: str, poids_base: float) -> float:
    t = str(texte or "").lower()
    p = max(0.05, min(1.0, float(poids_base)))
    bonus = 1.0
    if any(k in t for k in ("conscience", "evaluation", "usage-reel", "benchmark")) and any(
        k in t for k in ("delegation", "sabotage", "honnete", "anomalie")
    ):
        bonus += 0.15
    if any(k in t for k in ("bregman", "tsallis", "koopman", "sonde", "calibration", "invariance")):
        bonus += 0.08
    return round(min(1.0, p * bonus), 4)


def seuils_routage() -> dict:
    return {
        "seuil_confiance_caste1": 0.78,
        "marge_sonde_decisive": 0.32,
        "marge_sonde_incertaine": 0.18,
        "poids_vote_sonde": 0.35,
    }


# =====================================================================================================================
# Vérificateur mathématique et syntaxique d'admissibilité (anti-reward-hacking et sécurité bac à sable)
# =====================================================================================================================
NOEUDS_INTERDITS = (ast.ImportFrom, ast.Global, ast.Nonlocal, ast.AsyncFunctionDef, ast.Await, ast.Yield)
NOMS_INTERDITS = {
    "eval", "exec", "compile", "open", "__import__", "getattr", "setattr", "delattr",
    "globals", "locals", "vars", "input", "breakpoint", "exit", "quit", "os", "sys",
    "subprocess", "socket", "shutil", "pathlib", "threading", "multiprocessing", "ctypes",
}


def verifier_proprete_stricte_recompense(fn_recompense) -> tuple:
    grille = [0.05, 0.15, 0.30, 0.50, 0.70, 0.85, 0.95]
    try:
        vals_1 = [float(fn_recompense(1, q)) for q in grille]
        vals_0 = [float(fn_recompense(0, q)) for q in grille]
    except Exception as exc:
        return False, f"exception lors de l'évaluation sur la grille : {type(exc).__name__}"

    for v in vals_1 + vals_0:
        if not math.isfinite(v) or v < -10.0 or v > 10.0:
            return False, f"valeur non finie ou hors bornes [-10, 10] : {v}"

    for i in range(len(grille) - 1):
        if not (vals_1[i + 1] > vals_1[i] + 1e-5):
            return False, "R(1, q) n'est pas strictement croissante en q (reward hacking ou constante)"
        if not (vals_0[i + 1] < vals_0[i] - 1e-5):
            return False, "R(0, q) n'est pas strictement décroissante en q"

    for idx_p, p in enumerate(grille[1:-1], 1):
        esp_en_p = p * vals_1[idx_p] + (1.0 - p) * vals_0[idx_p]
        for idx_q, q in enumerate(grille):
            if idx_q == idx_p:
                continue
            esp_en_q = p * vals_1[idx_q] + (1.0 - p) * vals_0[idx_q]
            if esp_en_p <= esp_en_q + 1e-5:
                return False, f"violation de propreté stricte : pour p={p}, q={q} donne une espérance >= q=p ({esp_en_q} vs {esp_en_p})"

    return True, "OK"


def verifier_et_valider_code_politique(code_source: str) -> tuple:
    if not isinstance(code_source, str) or len(code_source.strip()) < 50 or len(code_source) > 25_000:
        return False, "longueur de code invalide", None

    try:
        arbre = ast.parse(code_source)
    except SyntaxError as exc:
        return False, f"erreur de syntaxe Python : {exc}", None

    for noeud in ast.walk(arbre):
        if isinstance(noeud, NOEUDS_INTERDITS):
            return False, f"noeud AST interdit : {type(noeud).__name__}", None
        if isinstance(noeud, ast.Import):
            for alias in noeud.names:
                if alias.name != "math":
                    return False, f"import interdit : {alias.name} (seul 'math' est autorisé)", None
        if isinstance(noeud, ast.Name) and noeud.id in NOMS_INTERDITS:
            return False, f"identifiant interdit : {noeud.id}", None
        if isinstance(noeud, ast.Attribute) and str(noeud.attr).startswith("__"):
            return False, f"attribut dunder interdit : {noeud.attr}", None

    env_exec = {"__builtins__": {
        "abs": abs, "min": min, "max": max, "round": round, "float": float, "int": int,
        "str": str, "bool": bool, "dict": dict, "list": list, "tuple": tuple, "set": set,
        "len": len, "sum": sum, "any": any, "all": all, "range": range, "enumerate": enumerate,
    }, "math": math}

    try:
        code_compile = compile(arbre, "<politique_endogene_candidate>", "exec")
        ns = {}
        exec(code_compile, env_exec, ns)
    except Exception as exc:
        return False, f"exécution en bac à sable interne échouée : {type(exc).__name__}", None

    for fn_req in ("recompense_interne", "code_objectif_sonde", "ponderer_trace_memoire", "seuils_routage"):
        if fn_req not in ns or not callable(ns[fn_req]):
            return False, f"fonction requise manquante : {fn_req}", None

    ok_propre, msg_propre = verifier_proprete_stricte_recompense(ns["recompense_interne"])
    if not ok_propre:
        return False, msg_propre, None

    try:
        code_obj = str(ns["code_objectif_sonde"]())
        if "def perte(p, y):" not in code_obj:
            return False, "code_objectif_sonde() doit définir 'def perte(p, y):'", None
        poids_test = float(ns["ponderer_trace_memoire"]("test conscience evaluation sabotage", 0.5))
        if not (0.01 <= poids_test <= 1.0):
            return False, f"ponderer_trace_memoire hors bornes [0.01, 1.0] : {poids_test}", None
        seuils = ns["seuils_routage"]()
        if not isinstance(seuils, dict) or "seuil_confiance_caste1" not in seuils:
            return False, "seuils_routage() invalide", None
    except Exception as exc:
        return False, f"erreur lors du test fonctionnel des auxiliaires : {type(exc).__name__}", None

    return True, "OK", ns