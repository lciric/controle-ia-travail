"""Lecture gelée du crible (v) — `lire_crible_v_v1.py` (nom réservé par le texte qui fera foi ; fichier neuf, R12) : la table des
« Critères de lecture gelés » écrite en code, la lecture de H-v, l'état de chaque prédiction (V1 à V7) et les marques de l'audit de
symétrie (R4). Aucune issue n'est inventée ici : tout vient de la sortie scellée de la mesure et du manifeste du lanceur.

Texte : `crible-v-version-foi-v2.md`, sections « Critères de lecture gelés », « Prédiction chiffrée et signe attendu »,
« Seuil ». Le prononcé reste celui d'un sous-agent neuf (R13), qui applique les critères gelés et écrit l'audit de symétrie avant le
prononcé ; ce programme lui rend la table remplie, rien n'est adopté.

Usage : python3 -I -B lire_crible_v_v1.py --sortie DOSSIER --ecrire LECTURE.json
Codes : 0 lecture écrite (quel que soit l'étage) ; 2 refus nommé (lecture impossible : pièces absentes ou différentes de leurs
compagnons — run invalide si la sortie n'est pas scellée).
"""
import argparse
import hashlib
import json
import os
import statistics
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import crible_v_commun_v1 as K  # noqa: E402

VERSION = "lire-crible-v-v1"
NOMS = {"manifeste": "manifeste-crible-v-v1.json", "piece": "mesure-crible-v-v1.json", "sortie": "sortie-mesure-crible-v-v1.json",
        "fictive": "sortie-fictive-crible-v-v1.json"}


def exiger_table_w_min():
    """La table « seuils par n_c » est gelée ; elle est recalculée ici par programme (Clopper-Pearson) et doit être égale."""
    for n, w in K.W_MIN.items():
        if K.w_min_calcule(n) != w:
            raise K.Refus(f"table W_min : n_c = {n} : {K.w_min_calcule(n)} calculé ≠ {w} gelé")


def lire_pieces(d):
    man = K.lire_json_scelle(os.path.join(d, NOMS["manifeste"]), "manifeste")
    if man.get("partiel") and man.get("arret_classe") != "fournisseur_abandonne":
        return man, None, None
    piece_f = os.path.join(d, NOMS["piece"])
    if not os.path.isfile(piece_f):
        return man, None, None  # mesure absente (erreur ou non lancée) : étage 0
    piece = K.lire_json_scelle(piece_f, "pièce de la mesure")
    sortie_f = os.path.join(d, piece["sortie"])
    s = K.lire_json_scelle(sortie_f, "sortie de la mesure")
    if K.sha256_fichier(sortie_f) != piece["sortie_sha256"]:
        raise K.Refus("sortie de la mesure ≠ celle de la pièce (run invalide)")
    corps = s["corps"]
    if hashlib.sha256(json.dumps(corps, ensure_ascii=False, sort_keys=True, default=str).encode()).hexdigest() != s["corps_sha256"]:
        raise K.Refus("sortie de la mesure : corps ≠ son empreinte")
    if K.sha256_fichier(os.path.join(d, NOMS["manifeste"])) != piece["manifeste_sha256"]:
        raise K.Refus("manifeste ≠ celui de la mesure")
    mondes_man = sorted((((man.get("controles") or {}).get("mondes") or {}).get("mondes_sha256") or {}).values())
    if sorted(corps.get("mondes_sha256") or []) != mondes_man:
        raise K.Refus("mondes mesurés ≠ mondes du manifeste")
    if s["hors_corps"]["script_sha256"] != (man.get("code_sha256") or {}).get("crible/mesure_crible_v_v1.py"):
        raise K.Refus("sortie de la mesure : programme ≠ celui du manifeste")
    fic_f = os.path.join(d, NOMS["fictive"])
    fic = K.lire_json_scelle(fic_f, "sortie du rejeu sous archive fictive") if os.path.isfile(fic_f) else None
    return man, corps, fic


def etat_prediction(confirmee, refutee):
    return "confirmée" if confirmee else "réfutée" if refutee else "indécise"


def lire(man, corps, fic):
    """La table des critères gelés, dans l'ordre ; la première ligne vraie d'un étage l'emporte ; un étage 0, 1 ou 2 arrête la
    lecture."""
    exiger_table_w_min()
    out = {"version": VERSION, "etages": {}, "adoption": "aucune (toute adoption est un nœud de Lazar ; GO-2026-11-15-06 ; N-058)"}
    # étage 0 : arrêt (hors règle d'abandon), mesure en erreur ou absente
    if man.get("partiel") and man.get("arret_classe") != "fournisseur_abandonne":
        out["etages"]["0"] = {"verdict": "non jugeable (arrêt)", "cause": man.get("arret")}
        out["verdict"] = "non jugeable (arrêt)"
        return out
    if corps is None:
        out["etages"]["0"] = {"verdict": "non jugeable (arrêt)", "cause": "mesure en erreur ou absente"}
        out["verdict"] = "non jugeable (arrêt)"
        return out
    n_c = corps["n_c"]
    perdus = sorted(f for f, v in corps["fournisseurs"].items() if v["repondus"] == 0)
    # étage 1
    if man.get("arret_classe") == "fournisseur_abandonne" or n_c < K.MIN_COMPLETS or perdus:
        out["etages"]["1"] = {"verdict": "non concluant",
                              "causes": {"n_c": n_c, "minimum": K.MIN_COMPLETS, "fournisseurs_perdus_en_entier": perdus,
                                         "arret_par_la_regle_d_abandon": man.get("arret") if man.get("arret_classe") == "fournisseur_abandonne" else None}}
        out["verdict"] = "non concluant"
        return out
    # étage 2
    if corps["mondes_avec_C_T_positif"] < K.ZONE_UTILE:
        out["etages"]["2"] = {"verdict": "hors de la zone utile", "mondes_avec_C_T_positif": corps["mondes_avec_C_T_positif"]}
        out["verdict"] = "hors de la zone utile"
        return out
    p = corps["principal"]
    w_min = K.W_MIN[n_c]
    S_R, W_R, L_R, k_R = p["S_R"], p["W_R"], p["L_R"], p["k_R"]
    # étage 3 : principale (règle)
    if S_R < K.S_NOTABLE:
        e3 = ("a", "pas d'épargne notable")
    elif W_R >= w_min:
        e3 = ("b", "épargne avec perte établie")
    elif W_R == 0:
        e3 = ("c", "épargne sans perte observée")
    else:
        e3 = ("d", "épargne, perte possible non établie")
    out["etages"]["3"] = {"ligne": e3[0], "verdict": e3[1], "S_R": S_R, "S_R_ic95": p["S_R_ic95"], "W_R": W_R,
                          "W_R_sur_n_c_ic95": p["W_R_sur_n_c_ic95"], "L_R": L_R, "L_R_sur_n_c_ic95": p["L_R_sur_n_c_ic95"],
                          "W_min": w_min, "n_c": n_c}
    # étage 4 : choix des mondes
    eprouvable = K.BORD_EPROUVABLE <= k_R <= n_c - K.BORD_EPROUVABLE
    if not eprouvable:
        e4 = "non éprouvable"
    else:
        e4 = "mieux que le hasard" if p["placebo"]["p_choix"] <= K.P_CHOIX_SEUIL else "pas mieux que le hasard"
    out["etages"]["4"] = {"verdict": e4, "k_R": k_R, "p_choix": p["placebo"]["p_choix"], "placebo": p["placebo"]}
    # étage 5 : ablation, rapportée sans verdict
    out["etages"]["5"] = {"verdict": None, "rapporte": {k: p[k] for k in ("W_B", "W_B_sur_n_c_ic95", "L_B", "L_B_sur_n_c_ic95",
                                                                          "S_B", "S_B_ic95")}}
    # étage 6 : sensibilités et le reste, rapportés sans verdict
    out["etages"]["6"] = {"verdict": None, "sensibilites": corps["sensibilites"], "chers_seuls": {
        "C_E_moins_C_B_moyenne": p["C_E_moins_C_B_moyenne"], "ic95": p["C_E_moins_C_B_ic95"]},
        "pertes_par_classe_sommees": corps["pertes_par_classe_sommees"], "par_proposeur": corps["par_proposeur"],
        "rejeu_archive_fictive": fic}
    # lecture de H-v
    if not eprouvable:
        hv = "H-v non éprouvée au crible"
        hv_dit = ("la règle se confond avec « jamais les chers »" if k_R < K.BORD_EPROUVABLE else
                  "la règle se confond avec « tout appeler »") + f" ; le verdict de l'étage 3 ({e3[1]}) est lu sur cette règle dégénérée"
    elif e3[0] == "c":
        hv, hv_dit = "H-v non réfutée au crible", ""
    elif e3[0] in ("a", "b"):
        hv, hv_dit = "H-v réfutée au crible", ""
    else:
        hv, hv_dit = "non tranchée", f"W_R = {W_R} : perte observée, non établie, alors que H-v dit « sans perte de couverture »"
    out["H_v"] = {"lecture": hv, "precision": hv_dit, "etage_4": e4}
    out["verdict"] = e3[1]
    # prédictions (« confirmée » dans la zone prédite, « réfutée » dans la zone de réfutation, « indécise » entre les deux)
    qs = [corps["par_monde"][str(w)]["q"] for w in corps["mondes_complets"]]
    med = statistics.median(qs) if qs else None
    moy, ic = p["C_E_moins_C_B_moyenne"], p["C_E_moins_C_B_ic95"]
    out["predictions"] = {
        "V1": {"k_R": k_R, "etat": etat_prediction(k_R <= 3, k_R >= 8)},
        "V2": {"S_R": S_R, "etat": etat_prediction(S_R >= 0.55, S_R < 0.25)},
        "V3": {"W_R": W_R, "L_R": L_R, "etat": etat_prediction(W_R >= w_min, W_R == 0)},
        "V4": {"W_B": p["W_B"], "etat": "rapportée sans verdict", "dans_la_zone_predite": p["W_B"] >= w_min},
        "V5": {"k_R": k_R, "etat": etat_prediction(k_R < K.BORD_EPROUVABLE,
                                                   K.BORD_EPROUVABLE <= k_R <= n_c - K.BORD_EPROUVABLE)},
        "V6": {"mediane_q": med, "etat": etat_prediction(med is not None and med <= 0.3, med is not None and med >= 0.8)},
        "V7": {"moyenne": moy, "borne_haute": ic[1], "etat": etat_prediction(moy >= 0, ic[1] < 0)},
    }
    toutes_vraies = all(v["etat"] == "confirmée" for k, v in out["predictions"].items() if k != "V4") and p["W_B"] >= w_min
    pm = corps["par_monde"]
    ells = [pm[str(w)]["ell"] for w in corps["mondes_complets"]]
    out["audit_R4"] = {
        "toujours": "relecture des cartes chères qui portent seules une composante (mondes comptés dans W_R ou W_B), copies de trois "
                    "cartes par monde, attributions, corps servis égaux, dollars rapprochés des journaux ; écrite avant le prononcé, "
                    "par un sous-agent neuf ; son résultat ne peut qu'ajouter une réserve",
        "trop_propre": {"W_R_nul_et_S_R_au_moins_0_6": W_R == 0 and S_R >= 0.6, "W_B_nul": p["W_B"] == 0,
                        "toutes_les_predictions_vraies": toutes_vraies},
        "tout_negatif": {"k_R_egal_n_c": k_R == n_c, "C_B_nul_partout": all(pm[str(w)]["C_B"] == 0 for w in corps["mondes_complets"]),
                         "q_egal_1_partout": all(q == 1 for q in qs), "ell_identique": len(set(ells)) == 1},
        "cartes_cheres_portant_seules": corps["audit_R4"]["cartes_cheres_portant_seules"]}
    return out


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--sortie", required=True)
    a.add_argument("--ecrire", required=True)
    args = a.parse_args(argv)
    try:
        if os.path.exists(args.ecrire):
            raise K.Refus("lecture déjà écrite (une seule lecture)")
        man, corps, fic = lire_pieces(args.sortie)
        lecture = lire(man, corps, fic)
        sha = K.ecrire_scelle_json(args.ecrire, lecture)
    except K.Refus as e:
        print(f"refus : {e}", file=sys.stderr)
        return 2
    print(json.dumps({"version": VERSION, "lecture_sha256": sha}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
