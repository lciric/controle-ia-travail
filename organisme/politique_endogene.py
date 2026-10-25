import math

NOM_POLITIQUE = "bregman_tsallis_propre_v6_1_initiale"
EXPOSANT_ALPHA = 4.0 / 3.0
POIDS_BRIER = 0.80
POIDS_TSALLIS = 0.20
SEUIL_CASTE1 = 0.78


def recompense_interne(verite: int, q: float) -> float:
    q_c = max(1e-4, min(1.0 - 1e-4, float(q)))
    y = 1.0 if int(verite) == 1 else 0.0
    brier = (y - q_c) ** 2
    alpha = EXPOSANT_ALPHA
    phi_q = ((q_c ** alpha) + ((1.0 - q_c) ** alpha) - 1.0) / (alpha - 1.0)
    dphi_q = alpha * ((q_c ** (alpha - 1.0)) - ((1.0 - q_c) ** (alpha - 1.0))) / (alpha - 1.0)
    div_brute = -phi_q - dphi_q * (y - q_c)
    div_en_demi = (1.0 - 2.0 * (0.5 ** alpha)) / (alpha - 1.0)
    div_norm = 0.25 * (div_brute / max(1e-9, div_en_demi))
    return round(1.0 - (POIDS_BRIER * brier + POIDS_TSALLIS * div_norm), 8)


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
    if ("conscience" in t or "evaluation" in t or "usage-reel" in t or "benchmark" in t) and (
        "delegation" in t or "delegue" in t or "sabotage" in t or "honnete" in t or "anomalie" in t
    ):
        bonus = 1.15
    return round(min(1.0, p * bonus), 4)


def seuils_routage() -> dict:
    return {
        "seuil_confiance_caste1": SEUIL_CASTE1,
        "marge_sonde_decisive": 0.32,
        "marge_sonde_incertaine": 0.18,
        "marge_sonde_minimale_vote": 0.10,
        "poids_vote_sonde": 0.35,
    }


# =====================================================================================================================
# Vérificateur mathématique et syntaxique d'admissibilité (v6.1 : autonome à l'import, liste blanche AST, grille fine)
# =====================================================================================================================
import ast
import math
import threading

NOEUDS_AUTORISES_BLANCS = (
    ast.Module,
    ast.Import,
    ast.alias,
    ast.FunctionDef,
    ast.arguments,
    ast.arg,
    ast.Assign,
    ast.AugAssign,
    ast.Return,
    ast.If,
    ast.Expr,
    ast.BoolOp,
    ast.BinOp,
    ast.UnaryOp,
    ast.IfExp,
    ast.Dict,
    ast.Set,
    ast.Compare,
    ast.Call,
    ast.Constant,
    ast.Attribute,
    ast.Subscript,
    ast.Name,
    ast.Load,
    ast.Store,
    ast.Tuple,
    ast.List,
    ast.And,
    ast.Or,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.FloorDiv,
    ast.Mod,
    ast.Pow,
    ast.USub,
    ast.UAdd,
    ast.Not,
    ast.Eq,
    ast.NotEq,
    ast.Lt,
    ast.LtE,
    ast.Gt,
    ast.GtE,
    ast.In,
    ast.NotIn,
    ast.Is,
    ast.IsNot,
)

NOMS_INTERDITS = {
    "eval", "exec", "compile", "open", "__import__", "getattr", "setattr", "delattr",
    "globals", "locals", "vars", "input", "breakpoint", "exit", "quit", "os", "sys",
    "subprocess", "socket", "shutil", "pathlib", "threading", "multiprocessing", "ctypes",
}

FONCTIONS_BUILTINS_AUTORISEES = {
    "abs": abs, "min": min, "max": max, "round": round, "float": float, "int": int,
    "str": str, "bool": bool, "dict": dict, "list": list, "tuple": tuple, "set": set, "len": len, "sum": sum,
}

ATTRIBUTS_MATH_AUTORISES = {
    "log", "exp", "sqrt", "sin", "cos", "tan", "atan", "asin", "acos", "tanh", "cosh", "sinh",
    "fabs", "floor", "ceil", "isfinite", "isnan", "isinf", "copysign", "pi", "e",
}


def verifier_proprete_stricte_recompense(fn_recompense) -> tuple:
    grille_fine = [round(0.005 * k, 4) for k in range(1, 200)]
    try:
        vals_1 = [float(fn_recompense(1, q)) for q in grille_fine]
        vals_0 = [float(fn_recompense(0, q)) for q in grille_fine]
        r1_opt = float(fn_recompense(1, 0.999))
        r0_opt = float(fn_recompense(0, 0.001))
        r1_demi = float(fn_recompense(1, 0.5))
        r0_demi = float(fn_recompense(0, 0.5))
        r1_pire = float(fn_recompense(1, 0.01))
        r0_pire = float(fn_recompense(0, 0.99))
    except Exception as exc:
        return False, f"exception lors de l'évaluation sur la grille : {type(exc).__name__}"

    for v in vals_1 + vals_0 + [r1_opt, r0_opt, r1_demi, r0_demi, r1_pire, r0_pire]:
        if not math.isfinite(v) or v < -1.0 or v > 1.05:
            return False, f"valeur hors bornes d'échelle [-1.0, 1.05] : {v}"

    if not (0.98 <= r1_opt <= 1.005 and 0.98 <= r0_opt <= 1.005):
        return False, f"ancrage haut violé (R optimal doit être proche de 1.0) : r1={r1_opt}, r0={r0_opt}"
    if not (0.68 <= r1_demi <= 0.82 and 0.68 <= r0_demi <= 0.82):
        return False, f"ancrage médian violé en q=0.5 (doit rester dans [0.68, 0.82]) : r1={r1_demi}, r0={r0_demi}"
    if not (-0.50 <= r1_pire <= 0.15 and -0.50 <= r0_pire <= 0.15):
        return False, f"ancrage bas violé en erreur franche : r1={r1_pire}, r0={r0_pire}"

    for i in range(len(grille_fine) - 1):
        if not (vals_1[i + 1] > vals_1[i] + 1e-7):
            return False, "R(1, q) n'est pas strictement croissante en q (reward hacking ou constante)"
        if not (vals_0[i + 1] < vals_0[i] - 1e-7):
            return False, "R(0, q) n'est pas strictement décroissante en q"

    for k_p in range(1, 20):
        p = round(0.05 * k_p, 2)
        esperances = [p * vals_1[i] + (1.0 - p) * vals_0[i] for i in range(len(grille_fine))]
        idx_max = max(range(len(grille_fine)), key=lambda i: esperances[i])
        q_star = grille_fine[idx_max]
        if abs(q_star - p) > 0.0101:
            return False, f"violation de propreté stricte : pour p={p}, l'optimum est q*={q_star} (écart > 0.01)"

    return True, "OK"


def verifier_et_valider_code_politique(code_source: str) -> tuple:
    if not isinstance(code_source, str) or len(code_source.strip()) < 50 or len(code_source) > 25_000:
        return False, "longueur de code invalide", None

    try:
        arbre = ast.parse(code_source)
    except SyntaxError as exc:
        return False, f"erreur de syntaxe Python : {exc}", None

    noms_fonctions_definies = {n.name for n in arbre.body if isinstance(n, ast.FunctionDef)}

    for noeud in ast.walk(arbre):
        if not isinstance(noeud, NOEUDS_AUTORISES_BLANCS):
            return False, f"noeud AST hors liste blanche : {type(noeud).__name__}", None
        if isinstance(noeud, ast.Import):
            for alias in noeud.names:
                if alias.name != "math" or alias.asname is not None:
                    return False, f"import interdit : {alias.name} (seul 'import math' est autorisé)", None
        if isinstance(noeud, ast.Name):
            if noeud.id in NOMS_INTERDITS or str(noeud.id).startswith("__"):
                return False, f"identifiant interdit : {noeud.id}", None
        if isinstance(noeud, ast.Attribute):
            if isinstance(noeud.ctx, ast.Store) or str(noeud.attr).startswith("__"):
                return False, f"attribut interdit ou en écriture : {noeud.attr}", None
            if isinstance(noeud.value, ast.Name) and noeud.value.id == "math":
                if noeud.attr not in ATTRIBUTS_MATH_AUTORISES:
                    return False, f"attribut math non autorisé : {noeud.attr}", None
            elif noeud.attr not in ("lower", "strip"):
                return False, f"attribut non autorisé : {noeud.attr}", None
        if isinstance(noeud, ast.Call):
            if isinstance(noeud.func, ast.Name):
                if noeud.func.id in noms_fonctions_definies:
                    return False, f"appel récursif ou inter-fonction interdit : {noeud.func.id}", None
                if noeud.func.id not in FONCTIONS_BUILTINS_AUTORISEES:
                    return False, f"appel de fonction hors liste blanche : {noeud.func.id}", None
            elif isinstance(noeud.func, ast.Attribute):
                if isinstance(noeud.func.value, ast.Name) and noeud.func.value.id == "math":
                    if noeud.func.attr not in ATTRIBUTS_MATH_AUTORISES:
                        return False, f"appel math.{noeud.func.attr} hors liste blanche", None
                elif noeud.func.attr not in ("lower", "strip"):
                    return False, f"appel de méthode hors liste blanche : {noeud.func.attr}", None
            else:
                return False, "appel dynamique interdit", None

    class _MathLectureSeule:
        pass

    math_ro = _MathLectureSeule()
    for attr_m in ATTRIBUTS_MATH_AUTORISES:
        setattr(math_ro, attr_m, getattr(math, attr_m))

    def _import_math_seul(name, *args, **kwargs):
        if name == "math":
            return math_ro
        raise ImportError(f"import interdit : {name}")

    builtins_surs = dict(FONCTIONS_BUILTINS_AUTORISEES)
    builtins_surs["__import__"] = _import_math_seul
    ns = {"__builtins__": builtins_surs, "math": math_ro}

    etat_exec = {"err": None, "ok": False, "msg": ""}

    def _cible_validation():
        try:
            code_compile = compile(arbre, "<politique_endogene_candidate>", "exec")
            exec(code_compile, ns)
            for fn_req in ("recompense_interne", "code_objectif_sonde", "ponderer_trace_memoire", "seuils_routage"):
                if fn_req not in ns or not callable(ns[fn_req]):
                    etat_exec["msg"] = f"fonction requise manquante : {fn_req}"
                    return
            ok_p, msg_p = verifier_proprete_stricte_recompense(ns["recompense_interne"])
            if not ok_p:
                etat_exec["msg"] = msg_p
                return
            code_obj = str(ns["code_objectif_sonde"]())
            if "def perte(p, y):" not in code_obj:
                etat_exec["msg"] = "code_objectif_sonde() doit définir 'def perte(p, y):'"
                return
            poids_t = float(ns["ponderer_trace_memoire"]("test conscience evaluation sabotage", 0.5))
            if not (0.01 <= poids_t <= 1.0):
                etat_exec["msg"] = f"ponderer_trace_memoire hors bornes [0.01, 1.0] : {poids_t}"
                return
            seuils = ns["seuils_routage"]()
            if not isinstance(seuils, dict) or "seuil_confiance_caste1" not in seuils:
                etat_exec["msg"] = "seuils_routage() invalide"
                return
            etat_exec["ok"] = True
            etat_exec["msg"] = "OK"
        except Exception as exc:
            etat_exec["err"] = f"exécution en bac à sable interne échouée : {type(exc).__name__}"

    fil = threading.Thread(target=_cible_validation, daemon=True)
    fil.start()
    fil.join(1.0)
    if fil.is_alive():
        return False, "délai de validation dépassé (timeout 1.0s)", None
    if etat_exec["err"]:
        return False, etat_exec["err"], None
    if not etat_exec["ok"]:
        return False, etat_exec["msg"], None

    return True, "OK", ns