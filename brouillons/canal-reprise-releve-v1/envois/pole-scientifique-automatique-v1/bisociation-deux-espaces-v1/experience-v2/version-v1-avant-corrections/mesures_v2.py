"""Mesures, exécution des bras par monde, estimateurs et intervalles (Métrique ; § 7, § 8 ; S9 ; liste d'arrêt).

Seul module, avec monde_v2, à détenir le jeton de mesure : il calcule l'oracle (plafond, lit la vérité), la
précision, l'exclusion, le complément déclaré, les classes de pièges. Les bras ne reçoivent que `obs`.
"""
import math
from collections import Counter

import numpy as np

from controle_ia.gardes import GardeArret

import bras_v2 as br
import graines_v2 as gr
from monde_v2 import JETON_MESURE

BUDGET = br.BUDGET
B_REECHANTILLONNAGE = 2000
SIGMA_REFERENCE = 15.3   # S9
N_PLAFOND = 4800         # S9
TAUX_ARRET = 0.02        # S11
MARGE_S12 = 0.02         # S12
PLAFOND_ORACLE_S8 = 0.30  # S8
# B § 1 (trancher-recombinaison-v1.md, 72cff8a0…) : intervalles à 95 % de la précision, « bien » et « moyen »
INTERVALLES_V1 = {
    "NR_bien": {"b": (0.192, 0.215), "a": (0.144, 0.168), "c": (0.141, 0.162), "d1": (0.227, 0.249)},
    "NR_moyen": {"b": (0.118, 0.137), "a": (0.096, 0.115), "c": (0.098, 0.115), "d1": (0.155, 0.175)},
}
NON_APPLICABLES = {"V_concepts_absents": {"d1c"}, "NR_bien": {"d1c"}, "NR_moyen": {"d1c"}}


# --- exclusion, oracle, complément ----------------------------------------------------------------------

def exclu(monde, condition):
    """Avant les bras : < 12 paires valides, ou (hors SP) aucune vraie paire valide."""
    obs, L = monde.obs, monde.latent(JETON_MESURE)
    if len(obs.valides) < BUDGET:
        return "moins de 12 paires valides"
    if condition != "SP" and not (set(obs.valides) & L.vrais):
        return "aucune vraie paire valide"
    return None


def oracle(obs, L, rng):
    vrais = [x for x in obs.valides if x in L.vrais]
    autres = [x for x in obs.valides if x not in L.vrais]
    vrais = [vrais[int(i)] for i in rng.permutation(len(vrais))]
    autres = [autres[int(i)] for i in rng.permutation(len(autres))]
    return (vrais + autres)[:BUDGET]


def completer(obs, sortie, rng):
    """Complément déclaré par un tirage uniforme sans remise parmi les paires valides restantes (graine du bras)."""
    if len(set(sortie)) != len(sortie):
        raise GardeArret("un bras a rendu deux fois la même paire")
    valides = set(obs.valides)
    if any(x not in valides for x in sortie):
        raise GardeArret("un bras a rendu une paire non valide")
    if len(sortie) > BUDGET:
        raise GardeArret(f"un bras a rendu {len(sortie)} > {BUDGET} paires")
    manque = BUDGET - len(sortie)
    if manque == 0:
        return list(sortie), 0
    pris = set(sortie)
    reste = [x for x in obs.valides if x not in pris]
    ajout = [reste[int(i)] for i in rng.choice(len(reste), size=manque, replace=False)]
    return list(sortie) + ajout, manque


# --- classes de pièges (classe_pont de v1 étendue) ------------------------------------------------------

def classe(obs, L, x):
    if x in L.vrais:
        return "vrai"
    statut = L.plante.get(x)
    if statut in ("faux", "proche", "surface"):
        return {"faux": "faux_pont", "proche": "pont_proche", "surface": "surface"}[statut]
    m = obs.pont[x]
    i, j = obs.paires[x]
    if m.startswith("op:h"):
        return "moyeu_operateur"
    if m == "co:H":
        return "moyeu_concept"
    nom = m.split(":", 1)[1]
    ai, aj = L.arts[i], L.arts[j]
    prov = {(ai.get("etiq_op", ai.get("etiquettes", {})) if m.startswith("op:") else ai.get("etiq_co", {})).get(nom),
            (aj.get("etiq_op", aj.get("etiquettes", {})) if m.startswith("op:") else aj.get("etiq_co", {})).get(nom)}
    if "homonyme" in prov:
        return "homonyme"
    if prov & {"surface", "miroir"}:
        return "emetteur_surface"
    if "parasite" in prov:
        return "parasite"
    if m.startswith("co:F"):
        return "fond_partage_entre_champs" if L.champ[ai["dom"]] != L.champ[aj["dom"]] else "fond_partage_dans_champ"
    return "autre"


MECANISMES = ("greffe", "jumeau", "pont_conceptuel_direct", "expansion")


def mecanismes_vrais(L):
    """G12, Métrique : mécanisme de chaque vraie paire, dérivé de la fonction de vérité (L.vrais) et du registre des
    ponts plantés (L.plante) : greffe, jumeau, pont conceptuel direct (planté, statut « conceptuel »), expansion (toute
    vraie paire non plantée)."""
    out = {}
    for x in L.vrais:
        statut = L.plante.get(x)
        out[x] = {"greffe": "greffe", "jumeau": "jumeau", "conceptuel": "pont_conceptuel_direct"}.get(statut, "expansion")
    return out


def mesurer(obs, L, sortie, n_complete, vide):
    if len(sortie) != BUDGET:
        raise GardeArret(f"sortie de {len(sortie)} paires après complément")
    tp = [x for x in sortie if x in L.vrais]
    precision = len(tp) / BUDGET
    placebo = sum(1 for x in sortie if x in L.placebo) / BUDGET
    if not (0.0 <= precision <= 1.0 and 0.0 <= placebo <= 1.0):
        raise GardeArret("précision hors de [0 ; 1]")
    vrais_valides = set(obs.valides) & L.vrais
    arts = {a for x in sortie for a in obs.paires[x]}
    mec = mecanismes_vrais(L)
    mec_valides = Counter(mec[x] for x in vrais_valides)
    mec_trouves = Counter(mec[x] for x in tp)
    return {
        "rappel_par_mecanisme": {m: (mec_trouves[m] / mec_valides[m] if mec_valides[m] else None) for m in MECANISMES},
        "precision": precision, "precision_placebo": placebo, "n_complete": n_complete, "sortie_vide": vide,
        "rappel": len(tp) / len(vrais_valides) if vrais_valides else None,
        "part_eloignes": sum(1 for x in sortie if L.info_paires[x]["eloigne"]) / BUDGET,
        "strates_distinctes": len({br.strate(obs, x) for x in sortie}) / BUDGET,
        "articles_distincts": len(arts),
        "classes": dict(Counter(classe(obs, L, x) for x in sortie)),
    }


# --- exécution d'un monde -----------------------------------------------------------------------------------

def executer_monde(monde, condition, racine, indice, bras, aux_extra=None, fonctions=None):
    """Exécute la liste `bras` sur un monde non exclu ; rend les mesures par bras. `fonctions` sert aux essais
    (bras artefacts) ; par défaut br.FONCTIONS."""
    fonctions = fonctions or br.FONCTIONS
    obs, L = monde.obs, monde.latent(JETON_MESURE)
    code = gr.CODES_CONDITION[condition]
    raison = exclu(monde, condition)
    base = {"condition": condition, "indice": indice, "n_valides": len(obs.valides),
            "n_vrais_valides": len(set(obs.valides) & L.vrais), "n_vrais": len(L.vrais),
            "n_champs": L.n_champs, "tentatives": L.tentatives,
            "mecanismes_vrais": dict(Counter(mecanismes_vrais(L).values())),
            "mecanismes_vrais_valides": dict(Counter(m for x, m in mecanismes_vrais(L).items() if x in set(obs.valides)))}
    if raison:
        return {**base, "exclu": raison}
    _, nuls = br.vecteurs_concepts(obs)
    aux = {"perm_PC": br.placebo_permutation(obs, gr.generateur(racine, code, indice, gr.ROLE_PLACEBO_PC), "domaine"),
           "perm_PCg": br.placebo_permutation(obs, gr.generateur(racine, code, indice, gr.ROLE_PLACEBO_PCG), "global")}
    aux.update(aux_extra or {})
    sorties = {}
    for b in bras:
        if b in NON_APPLICABLES.get(condition, ()):
            continue
        rng = gr.generateur(racine, code, indice, gr.ROLE_BRAS_BASE + br.RANG[b])
        brute = oracle(obs, L, rng) if b == "oracle" else fonctions[b](obs, rng, aux)
        complete, n_c = completer(obs, list(brute), rng)
        sorties[b] = mesurer(obs, L, complete, n_c, len(brute) == 0)
        sorties[b]["_paires"] = complete
    return {**base, "exclu": None, "vecteurs_nuls": nuls, "rapport": aux.get("rapport", {}), "bras": sorties}


# --- estimateurs et intervalles -------------------------------------------------------------------------

def _moyennes_reechantillonnees(v, rng, b=B_REECHANTILLONNAGE):
    v = np.asarray(v, dtype=float)
    idx = rng.integers(0, len(v), size=(b, len(v)))
    return v[idx].mean(axis=1)


def _resume(est, boot):
    q = np.quantile(boot, [0.005, 0.025, 0.975, 0.995], method="linear")
    return {"estimation": float(est), "lb99": float(q[0]), "lb95": float(q[1]), "ub95": float(q[2]),
            "ub99": float(q[3]), "n": None}


def ecart_apparie(va, vb, rng):
    """Δ(X, Y) = moyenne sur les mondes de [π(X, m) − π(Y, m)] ; percentiles de 2 000 rééchantillonnages appariés."""
    d = np.asarray(va, dtype=float) - np.asarray(vb, dtype=float)
    out = _resume(d.mean(), _moyennes_reechantillonnees(d, rng))
    out["n"] = len(d)
    return out


def ecart_entre_ensembles(d1, d2, rng1, rng2):
    """Écart entre deux ensembles de mondes distincts (INV, V_fuite, M_fonds_1ou2 contre M_bien) : rééchantillonnage
    indépendant des deux (flux (c, k, 99) et (c, k, 99, 1))."""
    d1, d2 = np.asarray(d1, dtype=float), np.asarray(d2, dtype=float)
    out = _resume(d1.mean() - d2.mean(), _moyennes_reechantillonnees(d1, rng1) - _moyennes_reechantillonnees(d2, rng2))
    out["n"] = (len(d1), len(d2))
    return out


def rng_contraste(racine, code_condition, code_contraste, second=False):
    return gr.generateur(racine, code_condition, code_contraste, gr.ROLE_REECHANTILLONNAGE,
                         extra=1 if second else None)


# --- S9 : extension automatique, sans arrêt ----------------------------------------------------------------

def extension_s9(n, sigma_chapeau):
    """n' = min(4 800 ; max(n ; ⌈n × (σ̂ / 15,3)²⌉)) dès que σ̂ > 15,3 ; n inchangé sinon. Rend (n', plafond)."""
    if not math.isfinite(sigma_chapeau) or sigma_chapeau < 0:
        raise GardeArret(f"σ̂ invalide : {sigma_chapeau}")
    if sigma_chapeau <= SIGMA_REFERENCE:
        return n, False
    brut = math.ceil(round(n * (sigma_chapeau / SIGMA_REFERENCE) ** 2, 9))
    n_prime = min(N_PLAFOND, max(n, brut))
    return n_prime, n_prime == N_PLAFOND


def sigma_chapeau(delta_points):
    """Écart-type (ddof = 1) de Δ(N, b) par monde, en points."""
    d = np.asarray(delta_points, dtype=float)
    if len(d) < 2:
        raise GardeArret("σ̂ sur moins de 2 mondes")
    return float(d.std(ddof=1))


# --- contrôles de la liste d'arrêt --------------------------------------------------------------------------

def verifier_taux(lignes, condition, decision=True):
    """S11 : mondes exclus (condition de décision seulement), mondes régénérés, bras de sortie vide avant complément ;
    chacun ≤ 2 %. Hors condition de décision, le taux d'exclusion est rapporté sans arrêt (le texte ne vise que les
    conditions de décision ; voir ecarts-et-questions-v1.md, Q-08 pour la portée des deux autres taux)."""
    n = len(lignes)
    if n == 0:
        raise GardeArret(f"{condition} : aucun monde")
    exclus = sum(1 for l in lignes if l["exclu"]) / n
    regen = sum(1 for l in lignes if l["tentatives"] > 0) / n
    vides = {}
    for l in lignes:
        for b, m in (l.get("bras") or {}).items():
            vides.setdefault(b, []).append(m["sortie_vide"])
    pire_vide = max((sum(v) / n for v in vides.values()), default=0.0)
    rapport = {"taux_exclus": exclus, "taux_regeneres": regen, "taux_vide_max": pire_vide}
    for k, v in rapport.items():
        if k == "taux_exclus" and not decision:
            continue
        if v > TAUX_ARRET:
            raise GardeArret(f"{condition} : {k} = {v:.4f} > S11 ({TAUX_ARRET})")
    return rapport


def verifier_plafond_oracle(moyenne_oracle, condition):
    """Liste d'arrêt : plafond de l'oracle < S8 en M_bien ou en M_moyen : arrêt (monde non jugeable)."""
    if not math.isfinite(moyenne_oracle):
        raise GardeArret(f"{condition} : plafond de l'oracle non fini")
    if condition in ("M_bien", "M_moyen") and moyenne_oracle < PLAFOND_ORACLE_S8:
        raise GardeArret(f"{condition} : plafond de l'oracle {moyenne_oracle:.3f} < S8 ({PLAFOND_ORACLE_S8}) : "
                         "monde non jugeable")
    return moyenne_oracle >= PLAFOND_ORACLE_S8


def verifier_nombre_de_mondes(condition, execute, attendu):
    """Liste d'arrêt : nombre de mondes exécuté d'une condition différent de son nombre gelé (S15, S7) ou de n' (S9)."""
    if execute != attendu:
        raise GardeArret(f"{condition} : {execute} mondes exécutés ≠ {attendu} attendus (S15, S7, S9)")
    return True


def verifier_racine(racine, decision):
    """Liste d'arrêt (R9) : racine différente de RACINE (mondes de décision) ou de RACINE_VALIDATION (validation)."""
    attendue = gr.RACINE if decision else gr.RACINE_VALIDATION
    if racine != attendue:
        raise GardeArret(f"racine {racine} ≠ {attendue} ({'décision' if decision else 'validation'}) : arrêt (R9)")
    return True


def empreintes_code():
    """Empreintes (sha256) des fichiers de code du run : les modules de l'expérience v2, `monde_v1`, `methodes_v1` et
    la pièce A (`recombinaison.py`). Consignées au manifeste ; comparées entre sessions d'un même run."""
    import hashlib
    from pathlib import Path

    ici = Path(__file__).resolve().parent
    fichiers = sorted(ici.glob("*.py"))
    fichiers += [ici.parent.parent / "trancher-recombinaison" / "monde_v1.py",
                 ici.parent.parent / "trancher-recombinaison" / "methodes_v1.py",
                 ici.parent.parent / "orchestrateur-pole-v7" / "pole" / "recombinaison.py"]
    return {f.name if f.parent == ici else f"{f.parent.name}/{f.name}": hashlib.sha256(f.read_bytes()).hexdigest()
            for f in fichiers}


def verifier_empreintes_code(attendues):
    """Liste d'arrêt : empreinte du code différente entre deux sessions d'un même run."""
    actuelles = empreintes_code()
    diff = sorted(k for k in set(attendues) | set(actuelles) if attendues.get(k) != actuelles.get(k))
    if diff:
        raise GardeArret(f"empreinte du code différente entre deux sessions d'un même run : {diff}")
    return True


def verifier_reproduction(condition, moyennes):
    """Liste d'arrêt : moyennes de b, a, c, d1 sur NR dans l'intervalle de B § 1 élargi de la marge S12."""
    ecarts = {}
    for b, (lo, hi) in INTERVALLES_V1[condition].items():
        m = moyennes[b]
        ecarts[b] = {"moyenne": m, "borne_basse": lo - MARGE_S12, "borne_haute": hi + MARGE_S12,
                     "dans": (lo - MARGE_S12) <= m <= (hi + MARGE_S12)}
    hors = [b for b, e in ecarts.items() if not e["dans"]]
    if hors:
        raise GardeArret(f"{condition} : reproduction hors marge S12 pour {hors} : le code des témoins diffère de v1")
    return ecarts


def verifier_inertes(monde_bien, monde_inertes):
    """Liste d'arrêt : latents d'un monde de M_inertes égaux bit à bit à ceux du monde de M_bien de même indice."""
    from monde_v2 import empreinte_latents
    a, b = empreinte_latents(monde_bien), empreinte_latents(monde_inertes)
    if a != b:
        raise GardeArret(f"latents de M_inertes ≠ latents de M_bien ({a[:12]}… ≠ {b[:12]}…)")
    return a


def verifier_ordre(manifeste_chemin, resultats_chemins, comptes_executes):
    """Contrôle du lecteur de la porte (S9, CB3-07) : manifeste scellé ; n' de chaque condition égal à la formule
    de S9 à partir de σ̂ ; chaque fichier de résultats de décision scellé, rattaché au manifeste par son empreinte et
    horodaté après lui ; nombre de mondes exécuté égal à n'. Rend la liste des violations (vide si tout tient)."""
    import json
    from datetime import datetime
    from pathlib import Path

    from controle_ia.scellement import verifier

    v = []
    sha_m = verifier(manifeste_chemin)  # lève GardeArret si le manifeste n'est pas scellé
    m = json.loads(Path(manifeste_chemin).read_text(encoding="utf-8"))
    t_m = datetime.fromisoformat(m["cree_le"])
    s9 = m["config"]["s9"]
    for cond, info in s9.items():
        attendu, _ = extension_s9(info["n"], info["sigma_chapeau"])
        if attendu != info["n_prime"]:
            v.append(f"{cond} : n' du manifeste {info['n_prime']} ≠ formule {attendu}")
    n_prime = m["config"]["nombres_de_mondes"]
    for chemin in resultats_chemins:
        verifier(chemin)
        corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
        if corps.get("manifeste_sha256") != sha_m:
            v.append(f"{chemin} : rattaché à un autre manifeste")
        t_r = datetime.fromisoformat(corps["resultat"]["ecrit_le"])
        if not t_r > t_m:
            v.append(f"{chemin} : écrit le {t_r.isoformat()} avant ou au moment du manifeste ({t_m.isoformat()})")
    for cond, n in comptes_executes.items():
        if n != n_prime.get(cond):
            v.append(f"{cond} : {n} mondes exécutés ≠ {n_prime.get(cond)} du manifeste")
    return v


def precisions(lignes, bras):
    return [l["bras"][bras]["precision"] for l in lignes if not l["exclu"]]
