"""Somme du reste net comptable par clé, au 2026-11-20 (estimation, non relevé).

Chaque montant porte sa source (registre sur origin/main, ligne ou identifiant).
Aucun fichier n'est lu ; aucune valeur de clé ; aucune dépense.
"""
import json

R = lambda x: round(x, 6)

# ---------- Minuit : 200 USD déclarés (R-3228, 2026-11-18 vers 06:59Z) ----------
minuit_borne = 200.0
minuit_depenses = {
    "sonde GO-2026-11-19-06 (depenses l.528, R-3617)": 0.000108,
    "épreuve des témoins v9, part Minuit (depenses l.532, GO-2026-11-19-20)": 0.980399,
    "course v9, Claude sur Minuit (depenses l.536, GO-2026-11-19-19)": 36.457056,
}
minuit_reste = minuit_borne - sum(minuit_depenses.values())

# ---------- Luc : 214 USD déclarés (R-4088, 2026-11-20 vers 05:02Z) ----------
luc_borne = 214.0
luc_depenses = {"sonde GO-2026-11-20-13 (depenses l.548, R-4091)": 0.000002}
luc_reste = luc_borne - sum(luc_depenses.values())

# ---------- Rigaud : 124 USD déclarés (R-3224, 2026-11-18 vers 06:49Z) ----------
rigaud_borne = 124.0
# Chaîne du registre (R-3304, R-3342, R-3479, R-3554), puis R-3611 et R-4089
rig_chaine = {
    "bornes hautes au 18 nov 15:58Z (R-3304) + témoins v4 (R-3342)": 7.479689,
    "course auto-conception v4, Claude (depenses l.522)": 24.789486,
    "témoins v6, Claude (depenses l.525, R-3554)": 0.972429,
    "course auto-conception v6, Claude (depenses l.526)": 24.716609,
}
rig_comptes_par_le_compte = 75.6  # R-3611, compte de l'organisme
rig_chaine_somme = sum(rig_chaine.values())
# Hypothèse de lecture : 75,6 = 32,269175 + 0,972429 + 42,36 (course v6 entière,
# part hors Claude 17,64 comprise : depenses l.526)
hyp_75_6 = 32.269175 + 0.972429 + 42.36
rig_apres = {
    "bras A, vérification de clé (depenses l.534, GO-2026-11-19-32)": 0.0000015,
    "bras A, essai de mesure, file Claude (depenses l.546, GO-2026-11-19-34)": 0.904303,
}
rig_non_attribue = {
    "« Raisons ou regard ? », appels Opus 4.6 (R-3536, 18 nov 23:45Z)": 0.93,
}
rig_reste_A = rigaud_borne - rig_comptes_par_le_compte - sum(rig_apres.values())
rig_reste_B = (rigaud_borne - rig_chaine_somme - sum(rig_apres.values())
               - sum(rig_non_attribue.values()))
rig_lots_en_cours_max = 45.0  # R-4170
rig_X = 8.35  # GO-2026-11-20-22, réserve de l'essai du bras A (9,25 - 0,904)

# ---------- Kimi (Moonshot) : solde lu 32,24463 (R-3277, 18 nov 09:21Z) ----------
kimi_releve = 32.24463
kimi_depenses = {}  # aucune ligne postérieure (depenses, decisions)
kimi_reste = kimi_releve - sum(kimi_depenses.values())

# ---------- OpenAI (Astra) : 30 USD sur OPENAI_API_KEY_2 (R-3356, mot rapporté, 18 nov 18:06Z) ----------
openai_borne = 30.0
openai_depenses = {
    "course auto-conception v4, Astra (depenses l.522 ; partiellement avant 18:06Z, comptée entière)": 7.30824,
    "bras du juge d'Astra GO-2026-11-18-32 (depenses l.521, 18:32Z)": 0.2903,
    "second bras du juge d'Astra GO-2026-11-18-54 (depenses l.524)": 0.3979,
    "course auto-conception v6, OpenAI (depenses l.526)": 4.80336,
    "sonde d'Astra (depenses l.532)": 0.00041,
    "course v9, Astra (depenses l.536)": 4.74571,
    "bras A, file GPT (depenses l.537, compteur)": 0.48776,
    "revendication 14, Astra (depenses l.550)": 0.46,
}
openai_appels_coupes_max = 2.6  # R-4204, facturation inconnue
openai_reste = openai_borne - sum(openai_depenses.values())
openai_reste_bas = openai_reste - openai_appels_coupes_max

# ---------- Google (Argon, Carbon) : aucune borne ni relevé (R-3222) ----------
google_depenses_depuis_18 = {
    "témoins v3+v4, Argon (depenses l.519)": 0.132289 + 0.204902,
    "course v4, Google (depenses l.522)": 12.682766,
    "témoins v6, Argon (depenses l.525)": 0.205566,
    "course v6, Google (depenses l.526)": 12.84088,
    "sonde Carbon (depenses l.531)": 1.3574733,
    "témoins v9, part hors Minuit (depenses l.532)": 1.183434 - 0.980399,
    "course v9, Carbon + Argon (depenses l.536)": 24.719127 + 6.580577,
    "bras A, file Carbon (depenses l.538)": 0.59612,
    "revendication 14, Carbon (depenses l.550)": 0.43,
    "« Raisons ou regard ? », Gemini E5 + diagnostic (depenses l.502, l.508)": 1.62 + 0.33,
}
google_appels_coupes_max = 1.0  # R-4204

# ---------- Engagements ----------
na = {  # course « nouvelles attaques », devis v4 620de369…, six espèces, sur la course
    "Minuit (juge espèce 3)": {"bas": 24.70, "haut": 126.06, "part": 162.56},
    "Luc (aiguilleur + proposeur espèce 4)": {"bas": 69.26, "haut": 136.63, "part": 214.0},
    "Rigaud (proposeur espèce 3)": {"bas": 22.29, "haut": 26.61, "pire_role": 199.65},
    "Google, relais 2 (juge et proposeur espèce 1, proposeur espèce 5)": {"bas": 95.35, "haut": 147.77, "pire": 570.0},
    "OpenAI, relais 3 (proposeur espèce 2)": {"bas": 14.25, "haut": 17.01, "pire_role": 199.65},
    "Kimi, relais 4 (proposeur espèce 6, coût non mesuré)": {"bas": 35.19, "haut": 88.55, "pire_role": 199.65},
}
na_lignes_a_part = {"témoins": 5.0, "sonde refus 1-5": 1.0, "sonde Kimi": 0.01}

coll = {  # collisionneur, devis v3 fadb7d09…, base à cinq espèces, deux questions
    "Rigaud (Fable 5.1)": {"bas": 6.00, "haut": 8.42, "pire": 14.72 + 14.71},
    "Google (Carbon + Argon)": {"bas": 3.13 * 2 + 1.57 * 2, "haut": 22.19,
                                "pire": 12.52 * 2 + 11.77 * 2, "epreuve_carbon": 2.16},
    "OpenAI (Astra)": {"bas": 1.33 * 2, "haut": 4.22, "pire": 7.82 + 7.81},
    "Kimi": {"bas": 0.61 * 2, "haut": 2.28, "pire": 3.29 * 2},
    "plafond demandé": 52.16,
}

# étage 2 de la ligne 3 : devis v7 donne la part par clé à 100 témoins ; 200 = proportion
e100 = {"claude": (10.84, 14.75, 29.10), "argon": (5.69, 7.74, 15.27)}
e200_tot = (32.90, 44.78, 88.36)
fac = [e200_tot[i] / (e100["claude"][i] + e100["argon"][i]) for i in range(3)]
etage2 = {
    "Claude (juge Opus, clé à désigner, GO-2026-11-20-49)":
        [R(e100["claude"][i] * fac[i]) for i in range(3)],
    "Google (juge Argon)": [R(e100["argon"][i] * fac[i]) for i in range(3)],
}

# ---------- Ce qui tient ----------
def tient(reste, besoin):
    return "tient" if reste >= besoin else "ne tient pas"

e2c = etage2["Claude (juge Opus, clé à désigner, GO-2026-11-20-49)"]
verif = {
    "Minuit, NA haut seul": (minuit_reste, 126.06),
    "Minuit, NA haut + étage 2 haut": (minuit_reste, 126.06 + e2c[1]),
    "Minuit, NA part + étage 2 pire": (minuit_reste, 162.56 + e2c[2]),
    "Luc, NA haut + étage 2 haut": (luc_reste, 136.63 + e2c[1]),
    "Luc, NA part + étage 2 pire": (luc_reste, 214.0 + e2c[2]),
    "Rigaud A, X + NA bas": (rig_reste_A, rig_X + 22.29),
    "Rigaud A, X + NA haut": (rig_reste_A, rig_X + 26.61),
    "Rigaud A, lots 45 + X + NA bas": (rig_reste_A, 45 + rig_X + 22.29),
    "Rigaud B, X + NA haut + collisionneur haut": (rig_reste_B, rig_X + 26.61 + 8.42),
    "Rigaud B, lots 45 + X + NA bas": (rig_reste_B, 45 + rig_X + 22.29),
    "Rigaud B, lots 45 + X + NA haut + coll haut": (rig_reste_B, 45 + rig_X + 26.61 + 8.42),
    "Kimi, NA bas": (kimi_reste, 35.19 + 0.01),
    "Kimi, coll haut seul": (kimi_reste, 2.28),
    "Kimi, NA haut + coll haut": (kimi_reste, 88.55 + 0.01 + 2.28),
    "OpenAI, NA bas": (openai_reste, 14.25),
    "OpenAI (appels coupés facturés), NA bas": (openai_reste_bas, 14.25),
    "OpenAI, coll haut seul": (openai_reste_bas, 4.22),
    "OpenAI, NA haut + coll haut": (openai_reste, 17.01 + 4.22),
}

sortie = {
    "minuit": {"borne": minuit_borne, "depenses": minuit_depenses,
               "somme": R(sum(minuit_depenses.values())), "reste": R(minuit_reste)},
    "luc": {"borne": luc_borne, "depenses": luc_depenses, "reste": R(luc_reste)},
    "rigaud": {"borne": rigaud_borne, "chaine": rig_chaine, "chaine_somme": R(rig_chaine_somme),
               "comptes_par_le_compte_R3611": rig_comptes_par_le_compte,
               "hypothese_75_6": R(hyp_75_6), "ecart_75_6_moins_chaine": R(75.6 - rig_chaine_somme),
               "apres": rig_apres, "non_attribue": rig_non_attribue,
               "reste_A_registre": R(rig_reste_A), "reste_B_corrige": R(rig_reste_B),
               "reste_A_apres_lots_max": R(rig_reste_A - rig_lots_en_cours_max),
               "reste_B_apres_lots_max": R(rig_reste_B - rig_lots_en_cours_max),
               "reste_A_apres_lots_max_et_X": R(rig_reste_A - rig_lots_en_cours_max - rig_X),
               "reste_B_apres_lots_max_et_X": R(rig_reste_B - rig_lots_en_cours_max - rig_X)},
    "kimi": {"releve": kimi_releve, "reste": R(kimi_reste)},
    "openai": {"borne": openai_borne, "depenses": openai_depenses,
               "somme": R(sum(openai_depenses.values())), "reste": R(openai_reste),
               "reste_si_appels_coupes_factures": R(openai_reste_bas)},
    "google": {"depenses_depuis_18": {k: R(v) for k, v in google_depenses_depuis_18.items()},
               "somme": R(sum(google_depenses_depuis_18.values())),
               "plus_appels_coupes_max": google_appels_coupes_max},
    "total_claude_A": R(minuit_reste + luc_reste + rig_reste_A),
    "total_claude_B": R(minuit_reste + luc_reste + rig_reste_B),
    "nouvelles_attaques": na, "na_lignes_a_part": na_lignes_a_part,
    "collisionneur": {k: ({kk: R(vv) for kk, vv in v.items()} if isinstance(v, dict) else v)
                      for k, v in coll.items()},
    "etage2_200_facteurs": [R(f) for f in fac], "etage2_par_cle_est_haut_pire": etage2,
    "verifications": {k: {"reste": R(a), "besoin": R(b), "verdict": tient(a, b),
                          "marge": R(a - b)} for k, (a, b) in verif.items()},
}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
