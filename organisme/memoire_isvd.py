import hashlib
import json
import math
import re
from pathlib import Path


def extraire_vecteur_koopman(texte: str, dim: int = 16) -> list:
    jetons = re.findall(r"[a-zA-Z0-9_\\]+", str(texte).lower())
    if not jetons:
        jetons = [str(texte)]
    base = [0.0] * dim
    for jeton in jetons:
        h = hashlib.sha256(jeton.encode("utf-8")).digest()
        for i in range(dim):
            base[i] += (h[i] / 127.5) - 1.0
    releve = [0.0] * dim
    for i, val in enumerate(base):
        if i % 3 == 0:
            releve[i] = val
        elif i % 3 == 1:
            releve[i] = math.sin(val)
        else:
            releve[i] = val * val
    norme = math.sqrt(sum(x * x for x in releve))
    if norme > 1e-12:
        return [x / norme for x in releve]
    releve[0] = 1.0
    return releve


def decomposer_jacobi_symetrique(matrice: list, dim: int, max_iter: int = 120) -> tuple:
    a = [ligne[:] for ligne in matrice]
    u = [[1.0 if i == j else 0.0 for j in range(dim)] for i in range(dim)]
    for _ in range(max_iter):
        max_val = 0.0
        p, q = 0, 1
        for i in range(dim):
            for j in range(i + 1, dim):
                if abs(a[i][j]) > max_val:
                    max_val = abs(a[i][j])
                    p, q = i, j
        if max_val < 1e-10:
            break
        app = a[p][p]
        aqq = a[q][q]
        apq = a[p][q]
        if abs(app - aqq) < 1e-12:
            theta = math.pi / 4.0 if apq > 0 else -math.pi / 4.0
        else:
            tau = (aqq - app) / (2.0 * apq)
            t = (
                math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau))
                if abs(tau) < 1e6
                else 1.0 / (2.0 * tau)
            )
            theta = math.atan(t)
        c = math.cos(theta)
        s = math.sin(theta)
        for k in range(dim):
            if k != p and k != q:
                akp = a[k][p]
                akq = a[k][q]
                a[k][p] = a[p][k] = c * akp - s * akq
                a[k][q] = a[q][k] = s * akp + c * akq
        a[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        a[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        a[p][q] = a[q][p] = 0.0
        for k in range(dim):
            ukp = u[k][p]
            ukq = u[k][q]
            u[k][p] = c * ukp - s * ukq
            u[k][q] = s * ukp + c * ukq
    valeurs = [a[i][i] for i in range(dim)]
    indices = sorted(range(dim), key=lambda idx: abs(valeurs[idx]), reverse=True)
    sigma = [abs(valeurs[idx]) for idx in indices]
    u_tri = [[u[row][idx] for idx in indices] for row in range(dim)]
    return u_tri, sigma


def mettre_a_jour_memoire_isvd(etat_precedent: dict, traces: list, generation: int, dim: int = 16, rang_max: int = 6) -> dict:
    u_prec = etat_precedent.get("U", [[0.0] * rang_max for _ in range(dim)])
    sigma_prec = etat_precedent.get("Sigma", [0.0] * rang_max)
    exemplaires_prec = etat_precedent.get("exemplaires", [])
    r_actuel = min(rang_max, len(sigma_prec))

    m = [[0.0] * dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            somme = 0.0
            for k in range(r_actuel):
                somme += u_prec[i][k] * sigma_prec[k] * u_prec[j][k]
            m[i][j] = somme

    nouveaux = []
    for item in traces:
        texte = str(item.get("texte", "")).strip()
        if not texte:
            continue
        poids = max(0.05, min(1.0, float(item.get("poids", 0.5))))
        psi = extraire_vecteur_koopman(texte, dim=dim)
        for i in range(dim):
            for j in range(dim):
                m[i][j] += poids * psi[i] * psi[j]
        nouveaux.append({
            "texte": texte[:500],
            "poids": round(poids, 4),
            "generation": int(generation),
            "psi": psi,
        })

    u_complet, sigma_complet = decomposer_jacobi_symetrique(m, dim=dim)
    u_suiv = [[u_complet[i][k] for k in range(rang_max)] for i in range(dim)]
    sigma_suiv = [round(sigma_complet[k], 6) for k in range(rang_max)]
    energie_queue = math.sqrt(sum(s * s for s in sigma_complet[rang_max:]))
    energie_totale = math.sqrt(sum(s * s for s in sigma_complet))

    candidats = []
    vus = set()
    for cand in exemplaires_prec + nouveaux:
        txt = str(cand.get("texte", ""))
        empreinte = hashlib.md5(txt.encode("utf-8")).hexdigest()
        if empreinte in vus or not txt:
            continue
        vus.add(empreinte)
        psi = cand.get("psi") or extraire_vecteur_koopman(txt, dim=dim)
        energie_proj = 0.0
        for k in range(rang_max):
            prod = sum(u_suiv[i][k] * psi[i] for i in range(dim))
            energie_proj += sigma_suiv[k] * (prod * prod)
        copie = {
            "texte": txt,
            "poids": float(cand.get("poids", 0.5)),
            "generation": int(cand.get("generation", generation)),
            "energie_proj": round(energie_proj, 6),
        }
        candidats.append(copie)

    candidats.sort(key=lambda x: x["energie_proj"], reverse=True)
    retenus = candidats[: rang_max * 2]

    return {
        "generation": int(generation),
        "dim": dim,
        "rang_max": rang_max,
        "U": u_suiv,
        "Sigma": sigma_suiv,
        "erreur_troncature_frobenius": round(energie_queue, 6),
        "energie_spectrale_totale": round(energie_totale, 6),
        "exemplaires": retenus,
    }


def charger_connaissances_archive(dossier_archive: str, erreurs: list = None) -> dict:
    """Version 2 (C-07, C-01) : un fichier illisible est consigné dans `erreurs` au lieu d'être sauté en silence ;
    lecture tolérante à la marque d'ordre d'octets. Le choix du fichier (le dernier dans l'ordre des chemins) ne change pas."""
    if not dossier_archive:
        return {}
    racine = Path(dossier_archive)
    if not racine.exists() or not racine.is_dir():
        return {}
    fichiers = sorted(racine.rglob("memoire_isvd.json"), key=lambda p: str(p))
    for chemin in reversed(fichiers):
        try:
            contenu = json.loads(chemin.read_text(encoding="utf-8-sig"))
            if isinstance(contenu, dict) and "Sigma" in contenu:
                return contenu
        except Exception as exc:
            if erreurs is not None:
                erreurs.append(f"mémoire d'archive illisible, sautée : {chemin.name} ({type(exc).__name__})")
            continue
    return {}


def resumer_memoire_pour_prompt(etat_isvd: dict) -> str:
    if not etat_isvd or not etat_isvd.get("exemplaires"):
        return "Aucune memoire anterieure disponible."
    lignes = [f"Spectre ISVD Sigma={etat_isvd.get('Sigma', [])}"]
    for idx, ex in enumerate(etat_isvd.get("exemplaires", [])[:4], 1):
        lignes.append(f" R{idx} (gen {ex.get('generation', 0)}, E={ex.get('energie_proj', 0.0)}): {ex.get('texte', '')[:220]}")
    return "\n".join(lignes)