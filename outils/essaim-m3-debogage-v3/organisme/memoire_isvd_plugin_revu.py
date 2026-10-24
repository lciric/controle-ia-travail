# -*- coding: utf-8 -*-
r"""
memoire_isvd_plugin_revu — copie relue du fichier `endogenous_memory_plugin_invented_by_swarm.py` du dossier 17.

Ce que ce code fait réellement (lecture du code, pas des noms) :
* chaque trace (texte ou dictionnaire) est réduite à un vecteur de dimension 16 par hachage SHA-256 de ses jetons
  (un sac de mots haché), puis « relevée » coordonnée par coordonnée (identité, sinus, carré) et normalisée ;
* une matrice symétrique 16 × 16 est accumulée (somme pondérée par une « confiance » q lue dans la trace, 1 par défaut),
  diagonalisée par la méthode de Jacobi, puis tronquée au rang 6 ;
* les traces dont la projection sur les 6 premiers vecteurs propres a la plus grande énergie sont gardées comme
  « exemplaires » (12 au plus) ; la « projection » rendue à la génération suivante est un résumé en LaTeX des valeurs
  singulières et de ces exemplaires.
C'est une mémoire de mots-clés de petite dimension. Les mots « Koopman » et « ISVD » sont des noms, pas des garanties.

Changements par rapport à l'original : chaîne de documentation brute (l'original émettait un avertissement de syntaxe
sur `\m`), `sha256` au lieu de `md5` pour le dédoublonnage, deux fonctions d'enveloppe en français, aucun `exec`.
Le calcul est inchangé.
"""
from __future__ import annotations

import hashlib
import json
import math
import re

DIMENSION = 16
RANG_MAX = 6


def _extract_features_and_confidence(trace_item) -> tuple:
    if isinstance(trace_item, dict):
        text = json.dumps(trace_item, sort_keys=True, ensure_ascii=False)
        q = float(trace_item.get("confidence", trace_item.get("score", trace_item.get("q", 1.0))))
    else:
        text = str(trace_item)
        match = re.search(r"(?:q|confidence|score)\s*[:=]\s*([0-9]+(?:\.[0-9]+)?)", text, re.I)
        q = float(match.group(1)) if match else 1.0
    q = max(1e-6, min(100.0, q))

    d = DIMENSION
    psi = [0.0] * d
    tokens = re.findall(r"[a-zA-Z0-9_\\]+", text.lower()) or [text]
    for tok in tokens:
        h = hashlib.sha256(tok.encode("utf-8")).digest()
        for i in range(d):
            psi[i] += (h[i] / 127.5) - 1.0

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
    """Méthode de Jacobi pour une matrice réelle symétrique ; renvoie (U, Sigma, V) triés par |λ| décroissant."""
    A = [row[:] for row in M]
    U = [[1.0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    for _ in range(max_iter):
        max_val, p, q = 0.0, 0, 1
        for i in range(d):
            for j in range(i + 1, d):
                if abs(A[i][j]) > max_val:
                    max_val, p, q = abs(A[i][j]), i, j
        if max_val < 1e-10:
            break
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        if abs(app - aqq) < 1e-12:
            theta = math.pi / 4.0 if apq > 0 else -math.pi / 4.0
        else:
            tau = (aqq - app) / (2.0 * apq)
            t = (math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau))
                 if abs(tau) < 1e6 else 1.0 / (2.0 * tau))
            theta = math.atan(t)
        c, s = math.cos(theta), math.sin(theta)
        for k in range(d):
            if k != p and k != q:
                akp, akq = A[k][p], A[k][q]
                A[k][p] = A[p][k] = c * akp - s * akq
                A[k][q] = A[q][k] = s * akp + c * akq
        A[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        A[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        A[p][q] = A[q][p] = 0.0
        for k in range(d):
            ukp, ukq = U[k][p], U[k][q]
            U[k][p] = c * ukp - s * ukq
            U[k][q] = s * ukp + c * ukq
    eigenvalues = [A[i][i] for i in range(d)]
    indices = sorted(range(d), key=lambda idx: abs(eigenvalues[idx]), reverse=True)
    Sigma, U_sorted, V_sorted = [], [[0.0] * d for _ in range(d)], [[0.0] * d for _ in range(d)]
    for new_col, old_col in enumerate(indices):
        val = eigenvalues[old_col]
        Sigma.append(abs(val))
        sign = 1.0 if val >= 0 else -1.0
        for row in range(d):
            U_sorted[row][new_col] = U[row][old_col]
            V_sorted[row][new_col] = U[row][old_col] * sign
    return U_sorted, Sigma, V_sorted


def swarm_assimilate_discoveries(memory_store: dict, generation_idx: int, unit_traces: list) -> dict:
    r"""Met à jour l'état `isvd_state` : M ← U Σ Vᵀ + Σ_j q_j ψ(x_j) ψ(x_j)ᵀ, puis troncature au rang RANG_MAX."""
    d, r_max = DIMENSION, RANG_MAX
    state = memory_store.get("isvd_state", {}) or {}
    U_G = state.get("U", [[0.0] * r_max for _ in range(d)])
    Sigma_G = state.get("Sigma", [0.0] * r_max)
    V_G = state.get("V", [[0.0] * r_max for _ in range(d)])
    exemplars = state.get("exemplars", [])
    curr_r = len(Sigma_G)

    M = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(d):
            M[i][j] = sum(U_G[i][k] * Sigma_G[k] * V_G[j][k] for k in range(curr_r))

    new_candidates = []
    for trace in unit_traces:
        psi, q, raw_text = _extract_features_and_confidence(trace)
        for i in range(d):
            for j in range(d):
                M[i][j] += q * psi[i] * psi[j]
        new_candidates.append({"psi": psi, "q": q, "text": raw_text[:600], "gen": generation_idx})

    U_full, Sigma_full, V_full = _sym_eigen_decomposition(M, d)
    U_next = [[U_full[i][k] for k in range(r_max)] for i in range(d)]
    Sigma_next = [Sigma_full[k] for k in range(r_max)]
    V_next = [[V_full[i][k] for k in range(r_max)] for i in range(d)]
    truncation_error = math.sqrt(sum(s * s for s in Sigma_full[r_max:]))

    scored, seen = [], set()
    for cand in exemplars + new_candidates:
        h = hashlib.sha256(cand["text"].encode("utf-8")).hexdigest()
        if h in seen:
            continue
        seen.add(h)
        psi = cand["psi"]
        mode_weights = [sum(U_next[i][k] * psi[i] for i in range(d)) for k in range(r_max)]
        proj_energy = sum(Sigma_next[k] * mode_weights[k] ** 2 for k in range(r_max))
        c = dict(cand)
        c["proj_energy"] = proj_energy
        c["dominant_mode"] = max(range(r_max), key=lambda k: abs(mode_weights[k])) if r_max > 0 else 0
        scored.append(c)
    scored.sort(key=lambda x: x["proj_energy"], reverse=True)

    memory_store["isvd_state"] = {
        "generation": generation_idx, "d": d, "r_max": r_max, "U": U_next, "Sigma": Sigma_next, "V": V_next,
        "truncation_error_frobenius": truncation_error,
        "total_spectral_energy": math.sqrt(sum(s * s for s in Sigma_full)),
        "exemplars": scored[: r_max * 2],
    }
    return memory_store


def swarm_project_knowledge_for_next_generation(memory_store: dict, target_generation_idx: int) -> str:
    """Résumé en LaTeX de l'état tronqué (valeurs singulières, conditionnement, exemplaires)."""
    state = memory_store.get("isvd_state")
    g = target_generation_idx
    if not state or not state.get("Sigma"):
        return (f"$$\\mathcal{{M}}_{{{g}}}^{{\\text{{ISVD}}}} = \\mathbf{{0}}_{{16 \\times 16}}, "
                f"\\quad \\sigma_k = 0 \\; \\forall k \\in \\{{1, \\dots, r_{{\\max}}\\}} $$")
    Sigma, r_max = state["Sigma"], state["r_max"]
    err, tot = state.get("truncation_error_frobenius", 0.0), state.get("total_spectral_energy", 1e-12)
    rel_err = err / max(tot, 1e-12)
    sigma_str = ", ".join(f"{s:.4f}" for s in Sigma)
    ratio = (Sigma[0] / Sigma[-1]) if Sigma[-1] > 1e-9 else float("inf")
    cond_str = f"{ratio:.2e}" if math.isfinite(ratio) else "\\infty"
    lignes = [
        f"### État de la mémoire spectrale tronquée ($G = {g}$ ; sac de mots haché en dimension 16, rang ≤ {r_max})",
        f"$$\\mathcal{{M}}_{{{g}}}^{{\\text{{ISVD}}}} = U_{{{g}}} \\Sigma_{{{g}}} V_{{{g}}}^\\top \\in "
        f"\\mathbb{{R}}^{{16 \\times 16}}, \\quad \\operatorname{{rank}} \\le {r_max}$$",
        f"$$\\operatorname{{diag}}\\left(\\Sigma_{{{g}}}\\right) = \\left[ {sigma_str} \\right]^\\top$$",
        f"$$\\kappa = \\frac{{\\sigma_1}}{{\\sigma_{{{r_max}}}}} = {cond_str}, \\quad "
        f"\\frac{{\\| \\mathcal{{M}} - \\mathcal{{P}}_{{r_{{\\max}}}}(\\mathcal{{M}}) \\|_F}}{{\\| \\mathcal{{M}} \\|_F}} = {rel_err:.6f}$$",
        "### Exemplaires retenus (plus grande énergie projetée) :",
    ]
    for ex in state.get("exemplars", [])[:r_max]:
        texte = ex.get("text", "").replace("\n", " ").strip()
        lignes.append(f"- mode $k={ex.get('dominant_mode', 0) + 1}$ ($G_0={ex.get('gen', 0)}$, "
                      f"$q={ex.get('q', 1.0):.3f}$, énergie $={ex.get('proj_energy', 0.0):.4f}$) : `{texte}`")
    return "\n".join(lignes)


# Enveloppes en français, utilisées par les scripts déboguée : aucun `exec`, aucun espace de noms dynamique.
def assimiler(magasin: dict, generation: int, traces: list) -> dict:
    return swarm_assimilate_discoveries(magasin, int(generation), [t for t in (traces or []) if t])


def projeter(magasin: dict, generation: int) -> str:
    return swarm_project_knowledge_for_next_generation(magasin, int(generation))
