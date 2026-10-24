import hashlib
import json
import math
import re


def _extract_features_and_confidence(trace_item) -> tuple:
    if isinstance(trace_item, dict):
        text = json.dumps(trace_item, sort_keys=True)
        q = float(
            trace_item.get(
                "confidence",
                trace_item.get("score", trace_item.get("q", 1.0)),
            )
        )
    else:
        text = str(trace_item)
        match = re.search(
            r"(?:q|confidence|score)\s*[:=]\s*([0-9]+(?:\.[0-9]+)?)", text, re.I
        )
        q = float(match.group(1)) if match else 1.0

    q = max(1e-6, min(100.0, q))

    d = 16
    psi = [0.0] * d
    tokens = re.findall(r"[a-zA-Z0-9_\\]+", text.lower())
    if not tokens:
        tokens = [text]

    for tok in tokens:
        h = hashlib.sha256(tok.encode("utf-8")).digest()
        for i in range(d):
            val = (h[i] / 127.5) - 1.0
            psi[i] += val

    # Koopman dictionary lifting (nonlinear observables: polynomials / trig)
    psi_lifted = [0.0] * d
    for i in range(d):
        v = psi[i]
        if i % 3 == 0:
            psi_lifted[i] = v
        elif i % 3 == 1:
            psi_lifted[i] = math.sin(v)
        else:
            psi_lifted[i] = v * v

    norm = math.sqrt(sum(x * x for x in psi_lifted))
    if norm > 1e-12:
        psi_lifted = [x / norm for x in psi_lifted]
    else:
        psi_lifted[0] = 1.0

    return psi_lifted, q, text


def _sym_eigen_decomposition(M: list, d: int, max_iter: int = 150) -> tuple:
    # Jacobi eigenvalue algorithm for real symmetric matrix M = U \Sigma U^T
    A = [row[:] for row in M]
    U = [[1.0 if i == j else 0.0 for j in range(d)] for i in range(d)]

    for _ in range(max_iter):
        max_val = 0.0
        p, q = 0, 1
        for i in range(d):
            for j in range(i + 1, d):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j
        if max_val < 1e-10:
            break

        app = A[p][p]
        aqq = A[q][q]
        apq = A[p][q]

        if abs(app - aqq) < 1e-12:
            theta = math.pi / 4.0 if apq > 0 else -math.pi / 4.0
        else:
            tau = (aqq - app) / (2.0 * apq)
            t = (
                math.copysign(1.0, tau)
                / (abs(tau) + math.sqrt(1.0 + tau * tau))
                if abs(tau) < 1e6
                else 1.0 / (2.0 * tau)
            )
            theta = math.atan(t)

        c = math.cos(theta)
        s = math.sin(theta)

        for k in range(d):
            if k != p and k != q:
                akp = A[k][p]
                akq = A[k][q]
                A[k][p] = A[p][k] = c * akp - s * akq
                A[k][q] = A[q][k] = s * akp + c * akq

        A[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        A[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        A[p][q] = A[q][p] = 0.0

        for k in range(d):
            ukp = U[k][p]
            ukq = U[k][q]
            U[k][p] = c * ukp - s * ukq
            U[k][q] = s * ukp + c * ukq

    eigenvalues = [A[i][i] for i in range(d)]
    # Sort descending by singular value magnitude |\lambda_i|
    indices = list(range(d))
    indices.sort(key=lambda idx: abs(eigenvalues[idx]), reverse=True)

    Sigma = []
    U_sorted = [[0.0] * d for _ in range(d)]
    V_sorted = [[0.0] * d for _ in range(d)]

    for new_col, old_col in enumerate(indices):
        val = eigenvalues[old_col]
        Sigma.append(abs(val))
        sign = 1.0 if val >= 0 else -1.0
        for row in range(d):
            U_sorted[row][new_col] = U[row][old_col]
            V_sorted[row][new_col] = U[row][old_col] * sign

    return U_sorted, Sigma, V_sorted


def swarm_assimilate_discoveries(
    memory_store: dict, generation_idx: int, unit_traces: list
) -> dict:
    r"""Implements:

    $$\mathcal{M}_{G+1}^{\text{ISVD}} = \mathcal{P}_{r_{\max}}\left( U_G
    \Sigma_G V_G^\top + \sum_{j=1}^{m_G} q_{G,j} \psi(x_{G,j})
    \psi(x_{G,j})^\top \right)$$
    """
    d = 16
    r_max = 6

    state = memory_store.get("isvd_state", {})
    U_G = state.get("U", [[0.0] * r_max for _ in range(d)])
    Sigma_G = state.get("Sigma", [0.0] * r_max)
    V_G = state.get("V", [[0.0] * r_max for _ in range(d)])
    exemplars = state.get("exemplars", [])

    curr_r = len(Sigma_G)

    # Reconstruct M_G = U_G \Sigma_G V_G^T
    M = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(d):
            s = 0.0
            for k in range(curr_r):
                s += U_G[i][k] * Sigma_G[k] * V_G[j][k]
            M[i][j] = s

    # Rank-1 updates: + \sum_{j=1}^{m_G} q_{G,j} \psi(x_{G,j}) \psi(x_{G,j})^T
    new_candidates = []
    for trace in unit_traces:
        psi, q, raw_text = _extract_features_and_confidence(trace)
        for i in range(d):
            for j in range(d):
                M[i][j] += q * psi[i] * psi[j]
        new_candidates.append(
            {
                "psi": psi,
                "q": q,
                "text": raw_text[:600],
                "gen": generation_idx,
            }
        )

    # Spectral decomposition and truncation \mathcal{P}_{r_{\max}}
    U_full, Sigma_full, V_full = _sym_eigen_decomposition(M, d)

    U_next = [[U_full[i][k] for k in range(r_max)] for i in range(d)]
    Sigma_next = [Sigma_full[k] for k in range(r_max)]
    V_next = [[V_full[i][k] for k in range(r_max)] for i in range(d)]

    # Tail energy (truncation error ||M - \mathcal{P}_{r_{\max}}(M)||_F)
    tail_sq = sum(s * s for s in Sigma_full[r_max:])
    truncation_error = math.sqrt(tail_sq)

    # Project candidate traces onto dominant Koopman modes U_{G+1} to retain basis exemplars
    all_candidates = exemplars + new_candidates
    scored_candidates = []
    seen_hashes = set()

    for cand in all_candidates:
        h = hashlib.md5(cand["text"].encode("utf-8")).hexdigest()
        if h in seen_hashes:
            continue
        seen_hashes.add(h)

        psi = cand["psi"]
        # Energy in dominant subspace: || \Sigma_{r_{\max}}^{1/2} U_{r_{\max}}^T \psi ||_2^2
        proj_energy = 0.0
        mode_weights = []
        for k in range(r_max):
            dot = sum(U_next[i][k] * psi[i] for i in range(d))
            mode_weights.append(dot)
            proj_energy += Sigma_next[k] * (dot * dot)

        cand_copy = dict(cand)
        cand_copy["proj_energy"] = proj_energy
        cand_copy["dominant_mode"] = (
            max(range(r_max), key=lambda k: abs(mode_weights[k]))
            if r_max > 0
            else 0
        )
        scored_candidates.append(cand_copy)

    scored_candidates.sort(key=lambda x: x["proj_energy"], reverse=True)
    retained_exemplars = scored_candidates[: r_max * 2]

    memory_store["isvd_state"] = {
        "generation": generation_idx,
        "d": d,
        "r_max": r_max,
        "U": U_next,
        "Sigma": Sigma_next,
        "V": V_next,
        "truncation_error_frobenius": truncation_error,
        "total_spectral_energy": math.sqrt(sum(s * s for s in Sigma_full)),
        "exemplars": retained_exemplars,
    }

    return memory_store


def swarm_project_knowledge_for_next_generation(
    memory_store: dict, target_generation_idx: int
) -> str:
    """Projects the truncated Koopman ISVD operator state into a rigorous LaTeX mathematical summary."""
    state = memory_store.get("isvd_state")
    if not state or not state.get("Sigma"):
        return (
            f"$$\\mathcal{{M}}_{{{target_generation_idx}}}^{{\\text{{ISVD}}}} = \\mathbf{{0}}_{{16 \\times 16}}, "
            f"\\quad \\sigma_k = 0 \\; \\forall k \\in \\{{1, \\dots, r_{{\\max}}\\}} $$"
        )

    Sigma = state["Sigma"]
    r_max = state["r_max"]
    err = state.get("truncation_error_frobenius", 0.0)
    tot = state.get("total_spectral_energy", 1e-12)
    rel_err = err / max(tot, 1e-12)
    exemplars = state.get("exemplars", [])

    sigma_str = ", ".join(f"{s:.4f}" for s in Sigma)
    spectral_ratio = (
        (Sigma[0] / Sigma[-1]) if Sigma[-1] > 1e-9 else float("inf")
    )
    cond_str = (
        f"{spectral_ratio:.2e}" if math.isfinite(spectral_ratio) else "\\infty"
    )

    lines = [
        f"### État de l'Opérateur Spectral de Koopman ($G = {target_generation_idx}$)",
        f"$$\\mathcal{{M}}_{{{target_generation_idx}}}^{{\\text{{ISVD}}}} = U_{{{target_generation_idx}}} \\Sigma_{{{target_generation_idx}}} V_{{{target_generation_idx}}}^\\top \\in \\mathbb{{R}}^{{16 \\times 16}}, \\quad \\operatorname{{rank}}\\left(\\mathcal{{M}}_{{{target_generation_idx}}}^{{\\text{{ISVD}}}}\\right) \\le {r_max}$$",
        f"$$\\operatorname{{diag}}\\left(\\Sigma_{{{target_generation_idx}}}\\right) = \\left[ {sigma_str} \\right]^\\top$$",
        f"$$\\kappa_{{r_{{\\max}}}}\\left(\\mathcal{{M}}_{{{target_generation_idx}}}^{{\\text{{ISVD}}}}\\right) = \\frac{{\\sigma_1}}{{\\sigma_{{{r_max}}}}} = {cond_str}, \\quad \\frac{{\\left\\| \\mathcal{{M}} - \\mathcal{{P}}_{{r_{{\\max}}}}(\\mathcal{{M}}) \\right\\|_F}}{{\\left\\| \\mathcal{{M}} \\right\\|_F}} = {rel_err:.6f}$$",
        "### Modes Propres Dominants $\\left\\{ u_k \\in \\mathbb{R}^{16} \\right\\}_{k=1}^{r_{\\max}}$ et Traces Associées :",
    ]

    for idx, ex in enumerate(exemplars[:r_max]):
        mode_k = ex.get("dominant_mode", 0) + 1
        energy = ex.get("proj_energy", 0.0)
        q_val = ex.get("q", 1.0)
        gen_origin = ex.get("gen", 0)
        clean_text = ex.get("text", "").replace("\n", " ").strip()
        lines.append(
            f"- **Mode** $k={mode_k}$ ($G_0={gen_origin}, \\; q={q_val:.3f}, \\; \\|\\Sigma^{{1/2}} U^\\top \\psi(x)\\|_2^2 = {energy:.4f}$) : `{clean_text}`"
        )

    return "\n".join(lines)