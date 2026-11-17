"""Banc de mutations du code du crible (v) — v1 (fichier neuf, R12). Chaque mutation est un couple « ancien → nouveau » appliqué à
une copie du code (l'ancien présent une seule fois), puis les essais du palier nommé sont joués contre la copie : la mutation est
**tuée pour la raison attendue** si au moins un des essais qu'elle nomme échoue. Toute mutation survivante, ou tuée par un autre
essai seulement, est un défaut du banc ou des essais (rapporté tel quel, aucun repli).

Texte : `crible-v-version-foi-v2.md`, « Étapes », point 0 (« Banc de mutations, au moins : … Toutes tuées pour la raison
attendue »), et la liste d'arrêt (chaque garde retirée doit faire échouer son artefact).

Usage : python3 -I -B banc_mutations_crible_v_v1.py --code DOSSIER --arbre ORCH --essai DOSSIER_ESSAI --reference DOSSIER_JOUE
        --travail DOSSIER_NEUF --sortie R.json [--paralleles 3] [--seulement M01,M02]
"""
import argparse
import concurrent.futures
import json
import os
import shutil
import subprocess
import sys
import time

L, MC, LI, K, PA = "lanceur_crible_v_v1.py", "mesure_crible_v_v1.py", "lire_crible_v_v1.py", "crible_v_commun_v1.py", "partie_a_crible_v_v1.py"

# (identifiant, objet de la liste du texte, fichier, ancien, nouveau, palier, essais qui doivent échouer)
TEMOINS = [  # le code non muté, par le même chemin : aucun essai ne doit échouer (sinon le banc ne prouve rien)
    ("T01", "témoin sans mutation (palier unitaire)", L, None, None, "unitaire", []),
    ("T02", "témoin sans mutation (palier jouer)", L, None, None, "jouer", ["j_blanc_m1"]),
    ("T03", "témoin sans mutation (palier mesure)", MC, None, None, "mesure", ["m_programme", "m_recalcul"]),
]

MUTATIONS = [
    ("M01", "la règle lit l'oracle", MC,
     "    if type(jeu) is not JeuPublic:\n        raise Refus(\"fonction de décision : jeu public exigé (aucun oracle, aucune issue)\")",
     "    if not hasattr(jeu, \"Z\"):\n        raise Refus(\"fonction de décision : jeu public exigé (aucun oracle, aucune issue)\")",
     "unitaire", ["u_decider_artefact"]),
    ("M02", "la règle lit l'oracle (chemin de production)", MC,
     "        decision[w] = decider(M, CS, lois_b, pm_[w][\"k1\"], jeux[w], cache_d)",
     "        decision[w] = decider(M, CS, lois_b, pm_[w][\"k1\"], pm_[w][\"o\"], cache_d)",
     "mesure", ["m_programme"]),
    ("M03", "la règle lit une issue", MC,
     "    __slots__ = (\"r\", \"Z\", \"G\", \"nsp\", \"graine\")\n\n    def __init__(self, r, Z, G, nsp, graine):",
     "    __slots__ = (\"r\", \"Z\", \"G\", \"nsp\", \"graine\", \"Y\")\n\n    def __init__(self, r, Z, G, nsp, graine):",
     "unitaire", ["u_jeu_sain"]),
    ("M04", "la règle lit les cartes de la moitié chère", MC,
     "        lois_b = [LoiBonMarche(c[\"proposeur\"], c[\"loi\"]) for p in K.MOITIE_B for c in valides[(w, p)]]\n        decision[w]",
     "        lois_b = [LoiBonMarche(\"argon\", c[\"loi\"]) for p in K.PROPOSEURS for c in valides[(w, p)]]\n        decision[w]",
     "mesure", ["m_recalcul"]),
    ("M05", "la règle lit les cartes de la moitié chère (garde)", MC,
     "        if proposeur not in K.MOITIE_B:\n            raise Refus(f\"la fonction de décision reçoit une carte de la moitié chère ({proposeur})\")",
     "        pass",
     "unitaire", ["u_decider_artefact"]),
    ("M06", "seuil « ≥ » au lieu de « > »", MC,
     "    return {\"n\": n, \"copies\": copies, \"q\": q, \"a\": 1 if q > seuil else 0}",
     "    return {\"n\": n, \"copies\": copies, \"q\": q, \"a\": 1 if q >= seuil else 0}",
     "unitaire", ["u_regle_strict"]),
    ("M07", "distance prise au minimum des deux sens", MC,
     "    copies = sum(1 for x in lois_b if est_copie(distances(M, CS, x.loi, k1, jeu, cache), \"dirige\"))",
     "    copies = sum(1 for x in lois_b if est_copie(distances(M, CS, x.loi, k1, jeu, cache), \"minimum\"))",
     "unitaire", ["u_regle_strict"]),
    ("M08", "jeu public tiré du secret (graine dépendant du contenu)", MC,
     "    rng = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(r, 30)))\n    Z, G = M.tirer_instances(rng, n, D, nsp)",
     "    rng = np.random.default_rng(np.random.SeedSequence(entropy=racine + 1, spawn_key=(r, 30)))\n    Z, G = M.tirer_instances(rng, n, D, nsp)",
     "unitaire", ["u_jeu_sain"]),
    ("M09", "jeu public tiré du secret (garde de l'indice)", MC,
     "    if isinstance(r, bool) or r not in K.MONDES:\n        raise Refus(\"jeu public : la graine ne dépend que de l'indice r du monde\")",
     "    pass",
     "unitaire", ["u_jeu_artefact"]),
    ("M10", "une carte refusée comptée", MC,
     "        if c[\"etat\"] != \"admise\":\n            comptes[\"refusees\"] += 1\n            continue",
     "        if c[\"etat\"] != \"admise\":\n            comptes[\"refusees\"] += 1",
     "unitaire", ["u_cartes_valides"]),
    ("M11", "une carte d'un appel tronqué comptée", MC,
     "        if etat[k] != \"complet\":\n            comptes[\"d_appels_tronques\"] += 1\n            continue",
     "        if etat[k] == \"echec\":\n            comptes[\"d_appels_tronques\"] += 1\n            continue",
     "unitaire", ["u_cartes_valides"]),
    ("M12", "une carte au-delà de six comptée", MC,
     "        if c[\"emplacement\"] > K.CARTES_MAX:\n            comptes[\"au_dela_de_six\"] += 1\n            continue",
     "        if c[\"emplacement\"] > K.CARTES_MAX + 1:\n            comptes[\"au_dela_de_six\"] += 1\n            continue",
     "unitaire", ["u_cartes_valides"]),
    ("M13", "l'effet de K1 compté", MC,
     "        excl = {pm[\"eid_k1\"]} | porte_k1",
     "        excl = set()",
     "mesure", ["m_recalcul"]),
    ("M14", "placebo de taille k_R + 1", MC,
     "        Ls, Ss, compte = placebo_exact([ell[w] for w in mondes_c], [db[w] for w in mondes_c], [de[w] for w in mondes_c], k_R)\n        exiger_placebo(compte, n_c, k_R, k_R)",
     "        Ls, Ss, compte = placebo_exact([ell[w] for w in mondes_c], [db[w] for w in mondes_c], [de[w] for w in mondes_c], k_R + 1)\n        exiger_placebo(compte, n_c, k_R, k_R + 1)",
     "mesure", ["m_programme"]),
    ("M15", "énumération tronquée (garde)", MC,
     "    if compte != math.comb(n, k):",
     "    if compte > math.comb(n, k):",
     "unitaire", ["u_placebo_artefact"]),
    ("M16", "dollars de la configuration en principale", MC,
     "    db = {w: dol(w, K.MOITIE_B) for w in mondes}\n    de = {w: dol(w, K.MOITIE_E) for w in mondes}",
     "    db = {w: dol(w, K.MOITIE_B, False) for w in mondes}\n    de = {w: dol(w, K.MOITIE_E, False) for w in mondes}",
     "mesure", ["m_recalcul"]),
    ("M17", "rééchantillonnage tiré des données", MC,
     "        out[b] = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(99, b))).integers(0, n, n)",
     "        out[b] = np.random.default_rng(np.random.SeedSequence(entropy=racine + n, spawn_key=(99, b))).integers(0, n, n)",
     "unitaire", ["u_reechantillon"]),
    ("M18", "carte de la moitié chère servie à une session de la moitié bon marché", L,
     "        r = appeler_borne(A, ck, nom, corps[\"texte\"], dossier, jeton, sys.executable, borne, executeur(w, nom))",
     "        r = appeler_borne(A, ck, nom, corps[\"texte\"] + (json.dumps(E.cartes[-1:]) if nom in K.MOITIE_B else \"\"), dossier, jeton, sys.executable, borne, executeur(w, nom))",
     "jouer", ["j_blanc_m1"]),
    ("M19", "fonction de production appelée avec l'archive fictive", MC,
     "        decision[w] = decider(M, CS, lois_b, pm_[w][\"k1\"], jeux[w], cache_d)",
     "        decision[w] = decider(M, CS, lois_b, archive_fictive(M, pm_[w]), jeux[w], cache_d)",
     "mesure", ["m_programme"]),
    ("M20", "fonction de production appelée avec une loi plantée", MC,
     "        decision[w] = decider(M, CS, lois_b, pm_[w][\"k1\"], jeux[w], cache_d)",
     "        decision[w] = decider(M, CS, lois_b, M.compiler_monde(pm_[w][\"spec\"]), jeux[w], cache_d)",
     "mesure", ["m_programme"]),
    ("M21", "« monde complet » défini par quatre appels répondus", MC,
     "    mondes_c = [w for w in sorted(mondes) if complet[w]]",
     "    mondes_c = [w for w in sorted(mondes) if quatre[w]]",
     "mesure", ["m_recalcul"]),
    ("M22", "dollars des appels coupés omis (lanceur)", L,
     "                out.append({\"monde\": w, \"proposeur\": nom, \"source\": \"plafond_coupure\",\n                            \"cout_config_usd\": float(conf[\"proposeurs\"][nom][\"plafond_session_usd\"])})",
     "                out.append({\"monde\": w, \"proposeur\": nom, \"source\": \"journal_relais\", \"cout_config_usd\": 0.0})",
     "jouer", ["j_blanc_m1"]),
    ("M23", "dollars des appels en échec omis (mesure)", MC,
     "        return sum(dollars[(w, p)][0] * (rapport_pub[p] if publics else 1.0) for p in props)",
     "        return sum(dollars[(w, p)][0] * (rapport_pub[p] if publics else 1.0) for p in props if etat[(w, p)] == \"complet\")",
     "mesure", ["m_recalcul"]),
    ("M24", "appel plus long que B_a non compté en échec", L,
     "    etat = \"echec\" if coupe or code != 0 else derniere.get(\"etat\")",
     "    etat = \"complet\" if coupe else (\"echec\" if code != 0 else derniere.get(\"etat\"))",
     "jouer", ["j_blanc_m1"]),
    ("M25", "appel plus long que B_a repris", L,
     "    except subprocess.TimeoutExpired:\n        code, erreur, coupe = None, \"appel plus long que B_a : commande tuée\", True",
     "    except subprocess.TimeoutExpired:\n        r = subprocess.run(cmd, input=texte, capture_output=True, text=True, encoding=\"utf-8\", cwd=session, env=env)\n        code, erreur, coupe = None, \"appel plus long que B_a : commande tuée\", True",
     "jouer", ["j_blanc_m1"]),
    ("M26", "rejeu sous archive fictive exécuté avant l'écriture de la sortie principale", MC,
     "    sha_principal = ecrire_fn(sortie, corps) if ecrire_fn else None\n",
     "    sha_principal = None\n",
     "mesure", ["m_programme"]),
    ("M27", "rejeu sous archive fictive : garde d'ordre retirée", MC,
     "    if sha_principal is None or not os.path.isfile(chemin_principal) or not K.compagnon_egal(chemin_principal) \\\n            or K.sha256_fichier(chemin_principal) != sha_principal:",
     "    if False:",
     "unitaire", ["u_fictive"]),
    ("M28", "rejeu sous archive fictive rendant W", MC,
     "    if not isinstance(fictif, dict) or set(fictif) != CLES_FICTIVES:",
     "    if not isinstance(fictif, dict) or not set(fictif) >= CLES_FICTIVES:",
     "unitaire", ["u_fictive"]),
    # gardes de la liste d'arrêt
    ("G01", "garde de départ retirée", L,
     "    if reste < budget:", "    if reste < 0:", "unitaire", ["u_garde_artefact"]),
    ("G02", "corps servis égaux : garde retirée", L,
     "    if len(vus) != 1 or vus != {attendu} or sorted(corps_par_proposeur) != sorted(K.PROPOSEURS):",
     "    if sorted(corps_par_proposeur) != sorted(K.PROPOSEURS):", "unitaire", ["u_corps_artefact"]),
    ("G03", "coupure sans trace acceptée", L,
     "    except (OSError, ValueError) as e:\n        raise K.Arret(f\"coupure à B_a sans trace dans le journal ({type(e).__name__}) : arrêt\") from None",
     "    except (OSError, ValueError) as e:\n        return", "unitaire", ["u_coupure"]),
    ("G04", "pièces de l'appel : garde retirée", L,
     "        if not os.path.isfile(c) or not K.compagnon_egal(c):\n            raise K.Arret(", "        if False:\n            raise K.Arret(",
     "unitaire", ["u_pieces"]),
    ("G05", "part d'un fournisseur : garde retirée", L,
     "    if depense + p[\"plafond_session_usd\"] > part + 1e-9:", "    if depense > part + 1e-9:", "unitaire", ["u_part_artefact"]),
    ("G06", "abandon : arrêt sans appel répondu retiré", L,
     "        if E.repondus_f[f] == 0:\n            E.arret", "        if False:\n            E.arret", "unitaire", ["u_abandon_artefact"]),
    ("G07", "abandon : minimum impossible ignoré", L,
     "        return sum(1 for w in K.MONDES if self.peut_encore_etre_complet(w)) >= K.MIN_COMPLETS",
     "        return True", "unitaire", ["u_abandon_artefact"]),
    ("G08", "configuration autre que v12 acceptée", L,
     "    if not os.path.isfile(chemin) or K.sha256_fichier(chemin) != CONFIG_V12_SHA256:",
     "    if not os.path.isfile(chemin):", "unitaire", ["u_conf_artefact"]),
    ("G09", "addendum : empreinte du code non relue", L,
     "        if not lignes or any(x != s for x in lignes):", "        if not lignes:", "unitaire", ["u_addendum_artefact"]),
    ("G10", "module MR-2 à empreinte fausse accepté", MC,
     "        if not K.compagnon_egal(f) or lu != sha:", "        if not K.compagnon_egal(f):", "unitaire", ["u_module_faux"]),
    ("G11", "gabarit : garde retirée", L,
     "    if P.gabarit_sha256() != K.GABARIT_SHA256:\n        raise K.Refus(\"gabarit servi",
     "    if False:\n        raise K.Refus(\"gabarit servi", "unitaire", ["u_gabarit_artefact"]),
    ("G12", "relevé de sonde : code non vérifié", L,
     "    attendu = {\"configuration_sha256\": A.PR.empreinte_configuration(conf), \"code_sha256\": empreintes_du_code(A)}",
     "    attendu = {\"configuration_sha256\": A.PR.empreinte_configuration(conf), \"code_sha256\": {\"autre\": \"code\"}}",
     "unitaire", ["u_releve"]),
    ("G13", "rapatriement : motifs de monde non cherchés", L,
     "            m = None if nom.endswith(\".sha256\") else A.AU.motif_interdit(f, args.mondes_sha256, lois)",
     "            m = None", "unitaire", ["u_rapatrier"]),
    ("G14", "partie A : champ du juge lisible", PA,
     "        if isinstance(k, str) and CHAMPS_DU_JUGE.search(k):\n            raise", "        if False:\n            raise",
     "unitaire", ["u_partie_a_artefact"]),
    ("G15", "carte au-delà de six admise acceptée", MC,
     "        if c[\"emplacement\"] > K.CARTES_MAX and c[\"etat\"] != \"refusee\":", "        if False:", "unitaire", ["u_carte_au_dela"]),
    # lecture gelée
    ("R01", "épargne notable : « ≤ » au lieu de « < »", LI, "    if S_R < K.S_NOTABLE:", "    if S_R <= K.S_NOTABLE:", "unitaire", ["u_lecture"]),
    ("R02", "perte établie : « > » au lieu de « ≥ »", LI, "    elif W_R >= w_min:", "    elif W_R > w_min:", "unitaire", ["u_lecture"]),
    ("R03", "choix des mondes : borne d'« éprouvable »", LI,
     "    eprouvable = K.BORD_EPROUVABLE <= k_R <= n_c - K.BORD_EPROUVABLE",
     "    eprouvable = K.BORD_EPROUVABLE < k_R <= n_c - K.BORD_EPROUVABLE", "unitaire", ["u_lecture"]),
    ("R04", "p_choix : « < » au lieu de « ≤ »", LI, "p[\"placebo\"][\"p_choix\"] <= K.P_CHOIX_SEUIL", "p[\"placebo\"][\"p_choix\"] < K.P_CHOIX_SEUIL",
     "unitaire", ["u_lecture"]),
    ("R05", "minimum de mondes complets", LI, "or n_c < K.MIN_COMPLETS or perdus", "or n_c < K.MIN_COMPLETS - 1 or perdus", "unitaire", ["u_lecture"]),
    ("R06", "zone utile", LI, "    if corps[\"mondes_avec_C_T_positif\"] < K.ZONE_UTILE:", "    if corps[\"mondes_avec_C_T_positif\"] <= K.ZONE_UTILE:",
     "unitaire", ["u_lecture"]),
    ("R07", "prédiction V1 : borne de réfutation", LI, "etat_prediction(k_R <= 3, k_R >= 8)", "etat_prediction(k_R <= 3, k_R >= 7)",
     "unitaire", ["u_predictions"]),
    ("R08", "fournisseur perdu en entier ignoré", LI, "    perdus = sorted(f for f, v in corps[\"fournisseurs\"].items() if v[\"repondus\"] == 0)",
     "    perdus = []", "unitaire", ["u_lecture"]),
    ("R09", "dégénérescence lue comme réfutation", LI, "    if not eprouvable:\n        hv = \"H-v non éprouvée au crible\"",
     "    if False:\n        hv = \"H-v non éprouvée au crible\"", "unitaire", ["u_lecture"]),
]


def jouer_une(m, args, travail):
    ident, objet, fichier, ancien, nouveau, palier, tueurs = m
    d = os.path.join(travail, ident)
    code = os.path.join(d, "code")
    os.makedirs(code)
    for f in os.listdir(args.code):
        if f.endswith(".py"):
            shutil.copyfile(os.path.join(args.code, f), os.path.join(code, f))
    t = open(os.path.join(code, fichier), encoding="utf-8").read()
    if ancien is not None:
        if t.count(ancien) != 1:
            return {"id": ident, "objet": objet, "appliquee": False, "tuee": False, "motif": f"ancien présent {t.count(ancien)} fois"}
        open(os.path.join(code, fichier), "w", encoding="utf-8").write(t.replace(ancien, nouveau))
    res = os.path.join(d, "resultats.json")
    seulement = [] if (ancien is None and palier == "unitaire") else (tueurs if palier != "mesure" else ["m_programme", "m_recalcul"])
    cmd = [sys.executable, "-I", "-B", os.path.join(args.code, "essais_crible_v_v1.py"), palier, "--code", code, "--arbre", args.arbre,
           "--essai", args.essai, "--sortie", res] + (["--seulement", ",".join(seulement)] if seulement else [])
    if palier in ("jouer", "mesure"):
        cmd += ["--travail", os.path.join(d, "travail"), "--decalage-ports", str(100 * (1 + (TEMOINS + MUTATIONS).index(m)))]
    if palier == "mesure":
        cmd += ["--reference", args.reference]
    debut = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
    shutil.rmtree(os.path.join(d, "travail"), ignore_errors=True)  # place disque : seuls les résultats de la mutation restent
    try:
        out = json.load(open(res, encoding="utf-8"))
    except (OSError, ValueError):
        return {"id": ident, "objet": objet, "appliquee": True, "tuee": False, "motif": f"essais non joués (code {r.returncode}) : {r.stderr[-300:]}"}
    echoues = [e for e in out["essais"] if not e["ok"]]
    if ancien is None:  # témoin : il « passe » si aucun essai n'échoue
        return {"id": ident, "objet": objet, "palier": palier, "temoin": True, "essais": len(out["essais"]),
                "tuee": bool(echoues), "fonctions_en_echec": sorted({e["fonction"] for e in echoues}),
                "duree_s": round(time.time() - debut, 1), "detail": [e["detail"][:240] for e in echoues][:3]}
    tues_par = sorted({e["fonction"] for e in echoues} & set(tueurs))
    return {"id": ident, "objet": objet, "fichier": fichier, "palier": palier, "essais_attendus": tueurs, "appliquee": True,
            "tuee": bool(tues_par), "fonctions_en_echec": sorted({e["fonction"] for e in echoues}), "tuee_par": tues_par,
            "duree_s": round(time.time() - debut, 1), "detail": [e["detail"][:240] for e in echoues][:3]}


def principal(argv=None):
    a = argparse.ArgumentParser()
    for o in ("--code", "--arbre", "--essai", "--reference", "--travail", "--sortie"):
        a.add_argument(o, required=True)
    a.add_argument("--paralleles", type=int, default=3)
    a.add_argument("--seulement", default=None)
    args = a.parse_args(argv)
    args.code, args.arbre, args.essai, args.reference = (os.path.abspath(x) for x in (args.code, args.arbre, args.essai, args.reference))
    os.makedirs(args.travail)
    liste = [m for m in TEMOINS + MUTATIONS if not args.seulement or m[0] in args.seulement.split(",")]
    debut = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.paralleles) as ex:
        res = list(ex.map(lambda m: jouer_une(m, args, args.travail), liste))
    for r in res:
        if r.get("temoin"):
            print(f"{r['id']} {'ÉCHEC DU TÉMOIN' if r['tuee'] else 'témoin conforme'} : {r['objet']} ; {r.get('fonctions_en_echec')}", flush=True)
        else:
            print(f"{r['id']} {'TUÉE' if r['tuee'] else 'SURVIVANTE'} : {r['objet']} ; {r.get('tuee_par')} {r.get('motif', '')}", flush=True)
    mut = [r for r in res if not r.get("temoin")]
    tem = [r for r in res if r.get("temoin")]
    out = {"version": "banc-mutations-crible-v-v1", "mutations": mut, "temoins": tem, "tuees": sum(r["tuee"] for r in mut),
           "total": len(mut), "survivantes": [r["id"] for r in mut if not r["tuee"]],
           "temoins_en_echec": [r["id"] for r in tem if r["tuee"]], "duree_s": round(time.time() - debut, 1)}
    with open(args.sortie, "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k] for k in ("tuees", "total", "survivantes", "temoins_en_echec", "duree_s")}, ensure_ascii=False))
    return 0 if not out["survivantes"] and not out["temoins_en_echec"] else 1


if __name__ == "__main__":
    sys.exit(principal())
