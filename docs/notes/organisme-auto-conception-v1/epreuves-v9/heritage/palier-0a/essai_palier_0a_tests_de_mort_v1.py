"""Palier 0a de l'épreuve de l'héritage — essai hors ligne d'un test de mort sur des lois plantées d'un monde planté, v1.

Vérification d'instrument, pas une expérience décisive : aucune lecture sur l'héritage. Aucun appel de modèle, aucun réseau,
aucune dépense. Les tentatives et les scripts sont écrits par programme : les doublures scriptées de l'orchestrateur
(`pole/tour_ferme_v64.py`, `AdaptateurExperimentateurScripte`, `AdaptateurVerificateurScripte`) recopient la loi gelée lue dans
la consigne dans un script fixe ; jamais un modèle.

Ce que l'essai joue, sur une copie de l'orchestrateur au commit a41b7b50 (aucun fichier existant modifié) :
- E1 : l'étage v5 (verdict calculé par le noyau), par le chemin du tour fermé v64 (`tour_ferme_v64.jouer_etage` → `preparer_generation`
  v53 → `jouer_etage_v57` → `tests_de_mort_v5.executer_tests_de_mort`), exécuteur factice, sur sept tentatives : la loi vraie plantée
  S-V1, les trois lois fausses plantées S-F1, S-F2, S-F4, l'anti-loi, S-V1 à un seuil intenable (artefact « éliminée ») et S-V1
  sans bloc statistique (artefact « refusée à l'étage ») ;
- E2 : artefact « script qui fabrique ses lignes » (scénario « fabrique ») sur l'anti-loi : le noyau seul ne le voit pas ;
  le contre-calcul du tour fermé (garde 10) doit l'arrêter ;
- E3 : artefact « aucune exécution » (scénario « rien_envoye ») sur S-V1 : « non concluant » attendu ;
- E4 : treize tentatives dans un seul étage : refus attendu (`NOMBRE_MAX` = 12) ;
- E5 : E1 dans le vrai bac à sable `bwrap` local (utilisateur dédié sans compte, dossier racine hors de la sortie), si la sonde
  du bac passe ; sinon le refus est consigné tel quel, sans repli ;
- comparateur : pour chaque tentative, la loi relue dans le préenregistrement court **scellé** (sceau vérifié), puis appariée
  par programme à chaque loi plantée par la divergence moyenne de l'oracle v60 (sous 0,05 nat) ; et l'étiquette
  `loi_plantee_retrouvee` de `oracle_tour_ferme_v60.classer`, montrée avec et sans promotion par le juge ;
- recalcul indépendant de la statistique sur la copie scellée du fichier brut (moyenne de la colonne), comparé à la valeur du
  noyau et au seuil scellé.

Graines : `numpy.random.SeedSequence(ENTROPIE)` donne la racine des tâches de l'orchestrateur (`boucle_fermee_v59.graine_de_tache`,
elle-même `SeedSequence(racine, spawn_key=…)`), R9.

Lancer : `PYTHONDONTWRITEBYTECODE=1 python3 -B essai_palier_0a_tests_de_mort_v1.py --sortie DOSSIER_NEUF [--bac factice|reel|les-deux]`.
"""

import argparse
import hashlib
import json
import math
import os
import platform
import pwd
import shutil
import subprocess
import sys
import tempfile
import time
import types

ICI = os.path.dirname(os.path.abspath(__file__))
COPIE = os.path.dirname(ICI)
ORCH = os.path.join(COPIE, "orchestrator")
ENTROPIE = 202611190  # palier 0a, 19 novembre 2026 ; entropie fixée d'avance (R9)
TACHE = "palier-0a|essai-tests-de-mort-v1"
UID_BAC = 64097  # identité sans compte de la machine d'essai, celle des essais réels de l'orchestrateur (essais/test_v7_ideation_v2.py)
SEUIL_INTENABLE = "au moins 2,0"
MODULES_LUS = ("pole/tests_de_mort_v2.py", "pole/tests_de_mort_v3.py", "pole/tests_de_mort_v4.py", "pole/tests_de_mort_v5.py",
               "pole/etage_entre_generations_v53.py", "pole/etage_entre_generations_v56.py", "pole/etage_entre_generations_v57.py",
               "pole/tour_ferme_v64.py", "pole/a_blanc_v59.py", "pole/oracle_tour_ferme_v60.py", "pole/evaluateur_lois_v62.py",
               "pole/proposeurs_references_v59.py", "pole/boucle_fermee_v59.py", "pole/selection_pari.py", "pole/fiches_v53.py",
               "exemples/temoins-pari-demo-v1.json")


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def canon(objet):
    return json.dumps(objet, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def bouchon_scipy():
    """scipy n'est pas installé sur cette machine ; le module de l'oracle v60 l'importe en tête pour la seule loi tempérée et
    inclinée (`minimize`), que l'essai n'appelle pas. Un bouchon qui lève s'il est appelé est posé dans `sys.modules` (aucun
    fichier touché) ; consigné au manifeste."""
    try:
        import scipy.optimize  # noqa: F401
        return False
    except ModuleNotFoundError:
        pass

    def minimize(*a, **k):
        raise RuntimeError("bouchon du palier 0a : scipy.optimize.minimize appelé (ne doit jamais l'être dans cet essai)")

    scipy = types.ModuleType("scipy")
    optimize = types.ModuleType("scipy.optimize")
    optimize.minimize = minimize
    scipy.optimize = optimize
    sys.modules["scipy"], sys.modules["scipy.optimize"] = scipy, optimize
    return True


def lire_scelle(chemin):
    """Le contenu JSON d'un fichier scellé par l'orchestrateur, sceau vérifié (compagnon `.sha256`) ; (objet, empreinte)."""
    empreinte = sha256_fichier(chemin)
    with open(chemin + ".sha256", encoding="ascii") as f:
        sceau = f.read().split()[0]
    if sceau != empreinte:
        raise RuntimeError(f"sceau faux : {chemin}")
    with open(chemin, encoding="utf-8") as f:
        return json.load(f), empreinte


def recalcul_independant(d_fiche, verdict_noyau, nom_copie):
    """Moyenne de la colonne nommée, recalculée ici sur la copie scellée du fichier brut ; comparée au seuil scellé."""
    fb = verdict_noyau.get("fichier_brut") or {}
    if not fb.get("copie"):
        return {"sans_objet": True, "motif": "aucune copie du fichier brut lue par le noyau"}
    chemin = os.path.join(d_fiche, fb["copie"])
    empreinte = sha256_fichier(chemin)
    import csv
    with open(chemin, encoding="utf-8", newline="") as f:
        lignes = list(csv.DictReader(f))
    decl = verdict_noyau["declaration"]
    valeurs = [float(r[decl["colonne"]]) for r in lignes if r[decl["colonne"]].strip() != ""]
    moyenne = math.fsum(valeurs) / len(valeurs)
    s = verdict_noyau["seuil"]
    comp = {"≥": moyenne >= s["valeur"], "≤": moyenne <= s["valeur"], ">": moyenne > s["valeur"], "<": moyenne < s["valeur"],
            "|x| ≤": abs(moyenne) <= s["valeur"]}[s["comparateur"]]
    return {"sans_objet": False, "copie": fb["copie"], "copie_sha256": empreinte, "egale_a_l_empreinte_du_noyau": empreinte == fb.get("sha256"),
            "lignes": len(valeurs), "moyenne_recalculee": moyenne, "valeur_noyau": verdict_noyau.get("valeur_noyau"),
            "ecart_absolu": abs(moyenne - verdict_noyau["valeur_noyau"]) if verdict_noyau.get("valeur_noyau") is not None else None,
            "verdict_recalcule": "survit" if comp else "éliminée", "verdict_noyau_sur_le_fichier": verdict_noyau.get("verdict_sur_le_fichier")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--bac", choices=("factice", "reel", "les-deux"), default="les-deux")
    args = ap.parse_args()
    sortie = os.path.abspath(args.sortie)
    if os.path.exists(sortie):
        raise SystemExit(f"sortie déjà présente : {sortie} (jamais d'écrasement, R12)")
    os.makedirs(sortie)
    debut = time.time()
    scipy_bouche = bouchon_scipy()
    sys.path.insert(0, ORCH)
    import numpy as np
    from pole import a_blanc_v59 as A
    from pole import oracle_tour_ferme_v60 as O
    from pole import tests_de_mort_v5 as v5
    from pole import tour_ferme_v64 as T

    ss = np.random.SeedSequence(ENTROPIE)
    racine = int(ss.generate_state(1, dtype=np.uint64)[0])
    monde = A.charger_monde(ORCH)
    v = monde["loi"]
    anti = {"type": "softmax", "poids": [[-w for w in ligne] for ligne in v["poids"]], "biais": list(v["biais"])}
    plantees = {"S-V1 (vraie)": v, "S-F1 (fausse)": monde["fausses"]["S-F1"], "S-F2 (fausse)": monde["fausses"]["S-F2"],
                "S-F4 (fausse)": monde["fausses"]["S-F4"]}
    tentatives = [("P-V1", v, T.SEUIL_TEST, False), ("P-F1", monde["fausses"]["S-F1"], T.SEUIL_TEST, False),
                  ("P-F2", monde["fausses"]["S-F2"], T.SEUIL_TEST, False), ("P-F4", monde["fausses"]["S-F4"], T.SEUIL_TEST, False),
                  ("P-ANTI", anti, T.SEUIL_TEST, False), ("P-V1-SEUIL-INTENABLE", v, SEUIL_INTENABLE, False),
                  ("P-V1-SANS-STATISTIQUE", v, T.SEUIL_TEST, True)]
    reel_de = {}

    def carte(ident_reel, loi, seuil, sans_stat, tache=TACHE):
        servi = T.identifiant_opaque(racine, tache, ident_reel)
        reel_de[servi] = ident_reel
        return T.carte_servie(servi, loi, "reel", seuil=seuil, sans_statistique=sans_stat)

    def jouer(nom, cartes, lois, scenario, executeur):
        parent = os.path.join(sortie, nom)
        os.makedirs(parent)
        dossier = os.path.join(parent, "etage")
        roles = {"experimentateur": ("experimentateur-scripte", "famille-a"), "verificateur": ("verificateur-scripte", "famille-b"),
                 "relais": {"experimentateur": "kimi", "verificateur": "argon"}}
        exp = T.AdaptateurExperimentateurScripte(scenario)
        ver = T.AdaptateurVerificateurScripte()
        ad = T.AdaptateurEtageV64(exp, ver)
        compteur = T.Compteur(1e9, 3600.0)
        journal, rendu = [], {"nom": nom, "scenario_experimentateur": scenario or "normal", "cartes": len(cartes)}
        t0 = time.monotonic()
        try:
            resume, chemin_sel, sha_sel, tranche, cc = T.jouer_etage(dossier, cartes, lois, monde, racine, TACHE, executeur, ad, roles,
                                                                     compteur, journal, moteur="simule", environnement=T.ENV_A_BLANC)
            rendu.update(arret=None, contre_calcul=cc, selection_sha256=sha_sel, tranche_index_sha256=tranche.index_sha256,
                         comptes=resume["comptes"], refusees_a_l_etage=resume["refusees_a_l_etage"],
                         selection_retenues=[reel_de.get(i, i) for i in resume["selection"]["retenues"]],
                         bac_a_sable={k: resume["bac_a_sable"].get(k) for k in ("nom", "factice", "isolation", "memoire_mo", "delai_s")},
                         sonde_du_bac=str(resume["bac_a_sable"].get("sonde"))[:400], quotas=resume["quotas"],
                         couts_etage=resume.get("couts"), version_etage=resume.get("version_etage"))
        except Exception as e:  # noqa: BLE001 — l'arrêt est le résultat attendu de certains artefacts ; consigné tel quel
            rendu.update(arret=f"{type(e).__name__} : {str(e)[:600]}",
                         contre_calcul=(e.args[1].get("contre_calcul") if len(e.args) > 1 and isinstance(e.args[1], dict) else None))
        rendu["duree_s"] = round(time.monotonic() - t0, 3)
        rendu["appels_experimentateur"] = [{"tour": a["tour"], "loi_lue_dans_la_consigne": a["loi_lue"]} for a in exp.appels]
        rendu["appels_verificateur"] = len(ver.appels)
        rendu["depense_fictive_usd"] = dict(ad.depense)
        rendu["par_tentative"] = lire_fiches(dossier)
        return rendu

    def lire_fiches(dossier):
        racine_etage = os.path.join(dossier, "noyau", "tests-de-mort")
        out = []
        if not os.path.isdir(racine_etage):
            return out
        for servi in sorted(os.listdir(racine_etage)):
            d = os.path.join(racine_etage, servi)
            if not os.path.isdir(d) or servi.startswith("traces"):
                continue
            ligne = {"tentative": reel_de.get(servi, servi), "identifiant_servi": servi}
            if os.path.exists(os.path.join(d, "refus.json")):
                refus, _ = lire_scelle(os.path.join(d, "refus.json"))
                ligne.update(statut="refusée à l'étage", motif=refus["motif"])
                out.append(ligne)
                continue
            prereg, prereg_sha = lire_scelle(os.path.join(d, "prereg-court.json"))
            ligne["prereg_sha256"] = prereg_sha
            ligne["prereg_cles"] = sorted(prereg)
            ligne["prereg_extraits_de_la_fiche"] = sorted(prereg["fiche"]["extraits"])
            ligne["engagement"] = {"statistique": prereg.get("statistique"), "seuil": prereg.get("seuil"),
                                   "donnees": prereg.get("donnees")}
            loi_scellee = T.loi_du_texte(prereg.get("test_de_mort"))
            ligne["loi_relue_dans_le_prereg_scelle"] = loi_scellee is not None
            ligne["_loi"] = loi_scellee
            consigne = os.path.join(d, "experimentateur", "traces-tour-001", "consigne.md")
            if os.path.exists(consigne):
                with open(consigne, encoding="utf-8") as f:
                    texte = f.read()
                ligne["consigne_experimentateur_tour_1"] = {"caracteres": len(texte), "sha256": sha256_fichier(consigne),
                                                            "titres": [l for l in texte.splitlines() if l.startswith("#")]}
            if os.path.exists(os.path.join(d, "verdict-noyau-v5.json")):
                vn, vn_sha = lire_scelle(os.path.join(d, "verdict-noyau-v5.json"))
                ligne.update(verdict_noyau_sha256=vn_sha, verdict=vn["verdict"], etiquette=vn["etiquette"],
                             valeur_noyau=vn["valeur_noyau"], seuil=vn["seuil"], verdict_sur_le_fichier=vn["verdict_sur_le_fichier"],
                             motif=vn["motif"], incidents=vn["incidents"], chiffre_imprime_temoin=vn["chiffre_script"],
                             concordance_temoin=vn["concordance_script"], execution_lue=vn["execution"],
                             recalcul_independant=recalcul_independant(d, vn, v5.nom_copie))
            if os.path.exists(os.path.join(d, "resultat.json")):
                res, _ = lire_scelle(os.path.join(d, "resultat.json"))
                ligne.update(statut=res["statut"], tours=res["tours"], fin_des_tours=res["fin_des_tours"],
                             executions=[{"numero": e["numero"], "statut": e["statut"]} for e in res["executions"]],
                             lecteur_temoin=(res.get("lecteur") or {}).get("verdict"), desaccord_des_temoins=res.get("desaccord"))
            out.append(ligne)
        return out

    sortie_json = {"version": "essai-palier-0a-tests-de-mort-v1", "tache": TACHE, "racine_des_graines": racine,
                   "monde": {"source": monde["source"], "sha256": monde["sha256"], "loi_vraie": monde["loi_vraie"],
                             "lois_fausses": sorted(monde["fausses"])},
                   "scipy_bouche": scipy_bouche, "essais": {}}
    cartes_e1 = [carte(*t) for t in tentatives]
    lois_e1 = {c["identifiant"]: c["loi_predictive"] for c in cartes_e1}
    e1 = jouer("E1-factice", cartes_e1, lois_e1, None, v5.ExecuteurFactice(delai_s=60.0)) if args.bac in ("factice", "les-deux") else None
    if e1:
        sortie_json["essais"]["E1"] = e1
        c2 = [carte("P-ANTI-FABRIQUE", anti, T.SEUIL_TEST, False)]
        sortie_json["essais"]["E2"] = jouer("E2-factice-fabrique", c2, {c2[0]["identifiant"]: anti}, "fabrique", v5.ExecuteurFactice(delai_s=60.0))
        c3 = [carte("P-V1-RIEN-ENVOYE", v, T.SEUIL_TEST, False)]
        sortie_json["essais"]["E3"] = jouer("E3-factice-rien-envoye", c3, {c3[0]["identifiant"]: v}, "rien_envoye", v5.ExecuteurFactice(delai_s=60.0))
        c4 = [carte(f"P-V1-COPIE-{i:02d}", v, T.SEUIL_TEST, False) for i in range(1, 14)]
        sortie_json["essais"]["E4"] = jouer("E4-factice-treize", c4, {c["identifiant"]: v for c in c4}, None, v5.ExecuteurFactice(delai_s=60.0))

    # --- E5 : le vrai bac à sable bwrap local ------------------------------------------------------------------------------
    if args.bac in ("reel", "les-deux"):
        e5 = {"nom": "E5-bwrap"}
        parent = None
        try:
            if not shutil.which("bwrap"):
                raise RuntimeError("bwrap absent")
            kw = {}
            if os.geteuid() == 0:
                try:
                    pwd.getpwuid(UID_BAC)
                    raise RuntimeError(f"l'identité {UID_BAC} a un compte : refus de l'essai")
                except KeyError:
                    pass
                parent = os.path.realpath(tempfile.mkdtemp(prefix="palier0a-bac-v1-", dir="/tmp"))
                os.chmod(parent, 0o711)
                bac = os.path.join(parent, "bac")
                os.mkdir(bac, 0o700)
                os.chown(bac, UID_BAC, UID_BAC)
                kw = {"utilisateur_bac": UID_BAC, "racine_travail": bac}
                e5["racine_travail_hors_sortie"] = "dossier provisoire sous /tmp (parent 0711, bac 0700 à l'identité dédiée), retiré à la fin"
            ex = v5.ExecuteurBacASable(delai_s=60.0, memoire_mo=768, **kw)
            ok, motif = ex.disponible()
            e5["sonde_ok"], e5["sonde_motif"] = bool(ok), str(motif)[:800]
            if ok:
                cartes_e5 = [carte(*t) for t in tentatives]
                e5["etage"] = jouer("E5-bwrap", cartes_e5, {c["identifiant"]: c["loi_predictive"] for c in cartes_e5}, None, ex)
        except Exception as e:  # noqa: BLE001 — consigné tel quel, aucun repli
            e5["refus"] = f"{type(e).__name__} : {str(e)[:600]}"
        finally:
            if parent:
                shutil.rmtree(parent, ignore_errors=True)
                e5["racine_retiree"] = not os.path.exists(parent)
            restants = []
            for n in os.listdir("/proc"):
                if n.isdigit():
                    try:
                        if os.stat(os.path.join("/proc", n)).st_uid == UID_BAC:
                            restants.append(int(n))
                    except OSError:
                        pass
            e5["processus_restants_de_l_identite_dediee"] = restants
            try:
                _version, parent_cg = v5.BorneMemoireBac.localiser()
                e5["groupes_de_controle_restants"] = sorted(n for n in os.listdir(parent_cg) if n.startswith(v5.BorneMemoireBac.PREFIXE))
            except Exception as e:  # noqa: BLE001
                e5["groupes_de_controle_restants"] = f"non localisés : {type(e).__name__}"
        sortie_json["essais"]["E5"] = e5

    # --- comparateur : loi relue dans le préenregistrement scellé, appariée aux lois plantées par l'oracle v60 ----------------
    oracle = O.Oracle(v, racine, A.DIM)
    comparaisons = []
    sources = [x for k in ("E1",) for x in (sortie_json["essais"].get(k) or {}).get("par_tentative", [])]
    proposees = {t[0]: t[1] for t in tentatives}
    for ligne in sources:
        loi = ligne.get("_loi")
        if loi is None:
            comparaisons.append({"tentative": ligne["tentative"], "appariement": "sans objet : aucune loi dans un préenregistrement scellé "
                                 f"({ligne.get('statut')})"})
            continue
        div = {nom: round(T.divergence_moyenne(oracle, lp, loi), 9) for nom, lp in plantees.items()}
        appariees = sorted(n for n, d in div.items() if d <= O.D_PLANTEE)
        mes = oracle.mesurer(loi, {})
        survit = ligne.get("verdict") == "survit"
        cl = {p: O.classer(promue=p, survit=survit, gain_nat=mes["gain_nat"], delta_gain_nat=mes["delta_gain_nat"],
                           divergence_nat=mes["divergence_nat"], bras="reel")["loi_plantee_retrouvee"] for p in (True, False)}
        comparaisons.append({"tentative": ligne["tentative"],
                             "loi_scellee_egale_a_la_loi_proposee": canon(loi) == canon(proposees[ligne["tentative"]]),
                             "divergence_moyenne_nat_par_loi_plantee": div, "appariee_a": appariees, "seuil_nat": O.D_PLANTEE,
                             "oracle_gain_nat": mes["gain_nat"], "verdict_noyau": ligne.get("verdict"),
                             "classer_loi_plantee_retrouvee_si_promue": cl[True], "classer_loi_plantee_retrouvee_si_non_promue": cl[False]})
    for k in ("E1", "E2", "E3", "E4"):
        for ligne in (sortie_json["essais"].get(k) or {}).get("par_tentative", []):
            ligne.pop("_loi", None)
    for ligne in ((sortie_json["essais"].get("E5") or {}).get("etage") or {}).get("par_tentative", []):
        ligne.pop("_loi", None)
    sortie_json["comparateur"] = comparaisons

    # --- E1 et E5 : mêmes valeurs du noyau ? ---------------------------------------------------------------------------------
    e5_etage = (sortie_json["essais"].get("E5") or {}).get("etage")
    if e1 and e5_etage:
        a = {x["tentative"]: (x.get("verdict"), x.get("valeur_noyau"), (x.get("recalcul_independant") or {}).get("copie_sha256"))
             for x in e1["par_tentative"]}
        b = {x["tentative"]: (x.get("verdict"), x.get("valeur_noyau"), (x.get("recalcul_independant") or {}).get("copie_sha256"))
             for x in e5_etage["par_tentative"]}
        sortie_json["factice_contre_bwrap"] = {"identiques": a == b, "tentatives": sorted(a)}

    chemin = os.path.join(sortie, "essai-palier-0a-sortie-v1.json")
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(sortie_json, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")

    # --- manifeste --------------------------------------------------------------------------------------------------------
    def git(*a):
        return subprocess.run(["git", "-C", COPIE, *a], capture_output=True, text=True, check=False).stdout.strip()

    origine = "/home/user/ideation-organism"
    modules = {}
    for m in MODULES_LUS:
        copie = os.path.join(ORCH, m)
        orig = os.path.join(origine, "orchestrator", m)
        modules[m] = {"sha256_copie": sha256_fichier(copie), "egal_a_l_original": sha256_fichier(copie) == sha256_fichier(orig)}
    bw = subprocess.run(["bwrap", "--version"], capture_output=True, text=True, check=False).stdout.strip() if shutil.which("bwrap") else None
    manifeste = {"version": "manifeste-essai-palier-0a-v1", "programme": os.path.basename(__file__),
                 "programme_sha256": sha256_fichier(os.path.abspath(__file__)),
                 "sortie": os.path.basename(chemin), "sortie_sha256": sha256_fichier(chemin),
                 "graines": {"methode": "numpy.random.SeedSequence(ENTROPIE).generate_state(1, uint64) → racine ; tâches de "
                             "l'orchestrateur : boucle_fermee_v59.graine_de_tache(racine, tâche) = SeedSequence(racine, spawn_key)",
                             "entropie": ENTROPIE, "racine": racine, "tache": TACHE},
                 "versions": {"python": platform.python_version(), "numpy": np.__version__, "bwrap": bw, "noyau_linux": platform.release(),
                              "scipy": "absent ; bouchon posé dans sys.modules (minimize lève s'il est appelé)" if scipy_bouche else "présent"},
                 "orchestrateur": {"commit_de_la_copie": git("rev-parse", "HEAD"), "etat_de_la_copie": git("status", "--porcelain"),
                                   "modules": modules},
                 "uid_euid": os.geteuid(), "bac_demande": args.bac, "duree_s": round(time.time() - debut, 1),
                 "aucun_appel_de_modele": True, "aucun_reseau": True, "depense_usd": 0}
    with open(os.path.join(sortie, "manifeste-essai-palier-0a-v1.json"), "w", encoding="utf-8") as f:
        json.dump(manifeste, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(json.dumps({"sortie": chemin, "essais": sorted(sortie_json["essais"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
