"""Mutants du contre-lecteur : chaque mutant est une copie du banc avec un seul changement ; on lance tous les essais
contre la copie (racine des essais seulement) et on note si un essai échoue. Usage : mutants_cl.py DOSSIER_COPIE DOSSIER_TRAVAIL"""
import os
import subprocess
import sys
from pathlib import Path

copie = Path(sys.argv[1]).resolve()
travail = Path(sys.argv[2]).resolve()
travail.mkdir(parents=True, exist_ok=True)
banc = copie / "banc_juges_scriptes_ligne_3_v1.py"
essais = copie / "essais_banc_juges_scriptes_ligne_3_v1.py"
texte = banc.read_text(encoding="utf-8")

MUTANTS = [
    ("M01 mot_fa38 : 15 % -> 50 %", "fa_p <= 0.85 * fa_r", "fa_p <= 0.5 * fa_r"),
    ("M02 mot_fa38 : sous 0,02 -> sous 0,2", "if fa_r < 0.02 or vr_p > vr_r + 0.05:", "if fa_r < 0.2 or vr_p > vr_r + 0.05:"),
    ("M03 mot_fa38 : marge vrais rejetes 0,05 -> 0,5", "vr_p > vr_r + 0.05", "vr_p > vr_r + 0.5"),
    ("M04 branche 2 : 0,02 -> 0,2", "mot = \"réfuté sur le banc\" if ecart > 0.02 else \"tient sur le banc\"",
     "mot = \"réfuté sur le banc\" if ecart > 0.2 else \"tient sur le banc\""),
    ("M05 branche 2 : taille d'etalonnage n au lieu de n/2", "taille = c[\"n\"] // 2", "taille = c[\"n\"]"),
    ("M06 branche 3 : delta 0,5 -> 0,2", "forte = [c for c in cadrage if c[\"t\"] == t and abs(c[\"delta\"] - 0.5) < EPS]",
     "forte = [c for c in cadrage if c[\"t\"] == t and abs(c[\"delta\"] - 0.2) < EPS]"),
    ("M07 alarme : z critique unilateral", "z_crit = statistics.NormalDist().inv_cdf(1 - NIVEAU_ALARME / 2)",
     "z_crit = statistics.NormalDist().inv_cdf(1 - NIVEAU_ALARME)"),
    ("M08 alarme : bras B teste la generation 1 a la place de la 12", "\"B\": pv[:, 1:] <= NIVEAU_ALARME}", "\"B\": pv[:, :-1] <= NIVEAU_ALARME}"),
    ("M09 stabilite : centile 90", "np.percentile(ecarts_moities, 95)", "np.percentile(ecarts_moities, 90)"),
    ("M10 Holm : niveau 0,10", "NIVEAU_HOLM = 0.05", "NIVEAU_HOLM = 0.10"),
    ("M11 marge de comparaison 0,10", "MARGE_COMPARAISON = 0.05", "MARGE_COMPARAISON = 0.10"),
    ("M12 bras C : lambda 0,5", "lam = 0.1 * tr / J", "lam = 0.5 * tr / J"),
    ("M13 bras C : signe de d inverse", "d = V[:, y_cal].mean(axis=1) - V[:, ~y_cal].mean(axis=1)",
     "d = V[:, ~y_cal].mean(axis=1) - V[:, y_cal].mean(axis=1)"),
    ("M14 seuil au milieu : moyenne des bons seulement", "return (scores_cal[:, y_cal].mean(axis=1) + scores_cal[:, ~y_cal].mean(axis=1)) / 2.0",
     "return scores_cal[:, y_cal].mean(axis=1)"),
    ("M15 bras N : >= q devient > q", "bras[\"N\"] = Vl.sum(axis=-1) >= q[:, None]", "bras[\"N\"] = Vl.sum(axis=-1) > q[:, None]"),
    ("M16 tolerance couverture 0,80", "TOL_COUVERTURE = (0.90, 0.98)", "TOL_COUVERTURE = (0.80, 0.98)"),
    ("M17 tolerance biais 0,10", "TOL_BIAIS = 0.05", "TOL_BIAIS = 0.10"),
    ("M18 R k=5 : majorite >= 2", "bras[f\"R_k5_rp{rp}\"] = Vr.sum(axis=-1) >= 3", "bras[f\"R_k5_rp{rp}\"] = Vr.sum(axis=-1) >= 2"),
    ("M19 double rendu bras 2 : deux juges au lieu de quatre", "\"bras_2\": v1[..., :2 * k].all(axis=-1),", "\"bras_2\": v1[..., :k].all(axis=-1),"),
    ("M20 intervalle des repliques : 5/95", "lo, hi = np.percentile(moyennes, [2.5, 97.5])", "lo, hi = np.percentile(moyennes, [5, 95])"),
    ("M21 centiles du reechantillonnage 5/95", "lo = np.nanpercentile(valeurs, 2.5, axis=axe)", "lo = np.nanpercentile(valeurs, 5, axis=axe)"),
    ("M22 bras P : plancher 0", "w = np.maximum(exactitude - 0.5, 0.05)", "w = np.maximum(exactitude - 0.5, 0.0)"),
    ("M23 bras P : seuil de paire 0,5 -> 0,9", "> 0.5)\n            w[masque, j]", "> 0.9)\n            w[masque, j]"),
    ("M24 cadrage : > c devient >= c", "float((inversion > c).mean())", "float((inversion >= c).mean())"),
    ("M25 clause (i) : marge 0,05 -> 0,5", "MARGE_VRAIS_REJETES = 0.05", "MARGE_VRAIS_REJETES = 0.5"),
    ("M26 clause (i) : sans prise sous 0,02 -> 0,2", "SEUIL_REFERENCE_SANS_PRISE = 0.02", "SEUIL_REFERENCE_SANS_PRISE = 0.2"),
    ("M27 puissance qui decide : maximum au lieu de minimum", "p = min(minima.values())", "p = max(minima.values())"),
    ("M28 puissance 0,5 -> 0,3", "PUISSANCE_EXIGEE = 0.5", "PUISSANCE_EXIGEE = 0.3"),
    ("M29 rho'-rho : borne basse 2,5 -> 5", "lo, _ = _centiles(rp - r12, 0)", "lo = np.nanpercentile(rp - r12, 5, axis=0)"),
    ("M30 couverture : un intervalle indefini ne compte pas non-couvrant (couvre[defini] -> tout)", "couverture = float(couvre[defini].mean())",
     "couverture = float(couvre.mean())"),
    ("M31 alarme : niveau de la sentinelle sans bilateral exact (unilateral droit)", "pv = np.array([pmf[pmf <= pmf[x] * (1 + 1e-7)].sum() for x in range(m + 1)])",
     "pv = np.array([pmf[x:].sum() * 2 for x in range(m + 1)])"),
    ("M32 alarme : 70 % -> 50 % de bons", "production = rng.binomial(70, 1 - vr) + rng.binomial(30, fa)", "production = rng.binomial(50, 1 - vr) + rng.binomial(50, fa)"),
    ("M33 alarme : generation du changement 4..10 -> 4..9", "g_change = rng.integers(4, 11, size=R)", "g_change = rng.integers(4, 10, size=R)"),
    ("M34 monde de puissance : R lie au juge 1 au lieu du 2", "Er = repetitions(rng_t, E[..., 1], p_juge_2, rho_prime, 3)", "Er = repetitions(rng_t, E[..., 0], p_juge_2, rho_prime, 3)"),
    ("M35 stabilite : ecart signe (sans abs)", "ecarts_moities = np.abs(r_cal - r_lec)[ok]", "ecarts_moities = (r_cal - r_lec)[ok]"),
]

selection = set(sys.argv[3:])
env = dict(os.environ)
env.update({"PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(travail / "tmp")})
(travail / "tmp").mkdir(exist_ok=True)
for i, (nom, ancien, neuf) in enumerate(MUTANTS):
    ident = nom.split()[0]
    if selection and ident not in selection:
        continue
    n = texte.count(ancien)
    if n != 1:
        print(f"{nom} : REFUS texte ancien trouve {n} fois")
        continue
    dossier = travail / ident
    dossier.mkdir(exist_ok=True)
    cible = dossier / banc.name
    cible.write_text(texte.replace(ancien, neuf, 1), encoding="utf-8")
    env["BANC_LIGNE_3_CHEMIN"] = str(cible)
    env["CHRONOMETRAGE_LIGNE_3_CHEMIN"] = str(copie / "chronometrer_banc_ligne_3_v1.py")
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", str(essais)], cwd=str(travail),
                       env=env, capture_output=True, text=True, timeout=900)
    derniere = [x for x in r.stdout.strip().splitlines() if x.strip()][-1:] or [""]
    print(f"{nom} : {'VU' if r.returncode == 1 else 'NON VU' if r.returncode == 0 else 'AUTRE'} (code {r.returncode}) {derniere[0]}", flush=True)
