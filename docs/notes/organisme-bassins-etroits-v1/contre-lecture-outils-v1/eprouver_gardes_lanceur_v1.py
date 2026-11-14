#!/usr/bin/env python3
"""Contre-lecture du lanceur `lancer_course_ideation_bassins_etroits_v1.py` — outil 2 : épreuves ciblées des gardes, sur des
états de disque factices, sans orchestrateur, sans appel, sans réseau.

Écrit par le contre-lecteur (Claude Fable 5.2), 13 novembre 2026. Tout est écrit dans le dossier de travail donné.

Usage : /usr/local/bin/python3 -I -B eprouver_gardes_lanceur_v1.py DOSSIER_DE_TRAVAIL_NEUF

Épreuves (chacune rend ce que le lanceur fait, sans jugement ; le jugement est dans la contre-lecture) :
 E1  dépense d'une course dont le contrôle d'Argon a été interrompu brutalement (dossier `tentative-1-externe-argon` seul) ;
 E2  même état, vu par `etat_generation` et `garde_cumul` quand le lanceur a survécu (manifeste de fin, code −9) ;
 E3  règle de passage quand les mesures de convergence de l'orchestrateur sont en erreur (repli) ;
 E4  règle de passage : l'appariement « texte le plus proche » vaut « même fiche » sans seuil ;
 E5  règle de passage : taille de la pièce écrite contre le plafond de 50 000 caractères ;
 E6  ligne de GO : révocation mal formée (9 colonnes), type sans accent ;
 E7  bras joué hors du lanceur (manifeste du bras de l'orchestrateur présent, aucun manifeste de bras du lanceur) ;
 E8  après un bras fini en code 4 ou 5 (classement illisible ou sans juge externe) : que rend `etat_generation` ?
 E9  planchers de la commande d'Argon (formule du lanceur) : contrôle court, contrôle externe du v3, sessions du v1 ;
 E10 fidélité de la question : cœur et contraintes du collisionneur retrouvés mot pour mot (espaces normalisés) ;
 E11 dépenses non finies ou mal typées dans un manifeste (lecture de `_cout`).
"""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
LANCEUR = DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v1.py"


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


def sceller(p: Path, objet=None, texte=None):
    p.parent.mkdir(parents=True, exist_ok=True)
    t = texte if texte is not None else json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    p.write_text(t, encoding="utf-8")
    Path(str(p) + ".sha256").write_text(hashlib.sha256(t.encode("utf-8")).hexdigest() + "  " + p.name + "\n")


def essayer(f):
    try:
        return {"rendu": f()}
    except BaseException as e:  # noqa: BLE001
        return {"exception": type(e).__name__, "message": str(e)[:400]}


def fiche(ident, taille=200):
    return {"identifiant_auteur": ident, "auteur": ident.split("-p")[0], "passe": int(ident.split("-p")[1][0]),
            "nom": "Idée " + ident, "enonce": "é" * taille, "questions_servies": ["Q2", "nouvelle"],
            "empreinte": hashlib.sha256(ident.encode()).hexdigest()}


def sortie_de_bras(s: Path, ids, convergence, doublons_opus=(), doublons_argon=(), tailles=None):
    """Sortie factice d'une course et de son bras, aux noms de fichiers réels de l'orchestrateur."""
    tailles = tailles or {}
    sceller(s / "fiches-validees.json", [fiche(i, tailles.get(i, 200)) for i in ids])
    cle = {f"T{k:02d}": i for k, i in enumerate(ids, 1)}
    sceller(s / "noyau" / "cles-anonymisation-par-juge.json", {"opus-juge": cle, "argon-juge": cle})
    sceller(s / "doublons-par-juge.json", {"opus-juge": list(doublons_opus)})
    sceller(s / "doublons-bras-rapporte.json", {"argon-juge": list(doublons_argon)})
    sceller(s / "classement.json", {"lisible_L2_L4": True, "lignes": [
        {"rang": k, "identifiant_auteur": i, "auteur": i.split("-p")[0], "eligible": True} for k, i in enumerate(ids, 1)]})
    sceller(s / "manifeste-fin.json", {"reglages": {"mesures_convergence": convergence}})


def main():
    w = Path(sys.argv[1]).resolve()
    if w.exists():
        raise SystemExit("le dossier de travail doit être neuf")
    w.mkdir(parents=True)
    assert sys.dont_write_bytecode, "lancer avec -B"
    lc = charger("lanceur_v1_contre_lecture", LANCEUR)
    out = {"lanceur_sha256": lc.sha256_fichier(LANCEUR)}

    # --- E1, E2 ----------------------------------------------------------------------------------------------------------
    s = w / "e1" / "sortie"
    (w / "e1" / "sortie-controle" / "tentative-1-externe-argon" / "controle" / "gemini-4-argon").mkdir(parents=True)
    out["E1_controle_argon_interrompu_sans_tentative_scellee"] = {
        "etat": "sortie-controle/tentative-1-externe-argon/ seul : ni tentative-1.json, ni sortie",
        "depense_course": essayer(lambda: list(lc.depense_course(s))),
        "plafond_du_controle_externe_usd": lc.CONTROLE_EXTERNE_USD}
    runs = w / "e2" / "runs"
    nom = "20261113-140001" + lc.SUFFIXE_RUN + "1"
    sceller(runs / nom / "manifeste-lanceur-depart.json",
            {"generation": 1, "lanceur": {"version": lc.VERSION}, "sortie": str(s), "temps": "course"})
    sceller(runs / nom / "manifeste-lanceur-fin.json", {"generation": 1, "code": -9, "temps": "course"})
    r = lc.Reglages.production()
    r.dossier_runs = runs
    lus = lc.runs_du_lanceur(r)
    out["E2_meme_etat_lanceur_survivant_code_moins_9"] = {
        "depense_run": essayer(lambda: lc.depense_run(lus[0])),
        "garde_cumul_avant_une_course": essayer(lambda: {k: v for k, v in lc.garde_cumul(lus, lc.PLAFOND_COURSE_USD, 60.0).items()
                                                         if k != "par_run"}),
        "etat_generation_1": essayer(lambda: {k: (v if k == "temps" else None) for k, v in lc.etat_generation(lus, 1).items()})}

    # --- E3 --------------------------------------------------------------------------------------------------------------
    ids = ["opus-p1-01", "opus-p2-01", "fable-p1-01", "fable-p2-01", "argon-p1-01", "argon-p2-01"]
    conv_ok = {"par_proposeur": {a: {f"{a}-p1-01": {"identifiant_passe_1": f"{a}-p1-01", "identifiant_passe_2": f"{a}-p2-01",
                                                    "appariement": "même nom", "distance_edition": 0.1}}
                                 for a in ("opus", "fable", "argon")}}
    sortie_de_bras(w / "e3a", ids, conv_ok)
    sortie_de_bras(w / "e3b", ids, {"erreur": "ValueError : mesure en échec (forme réelle de l'orchestrateur, ecrire_fin)"})
    a, b = lc.choisir_fiches_recues(w / "e3a", 1), lc.choisir_fiches_recues(w / "e3b", 1)
    out["E3_mesures_de_convergence_en_erreur"] = {
        "avec_mesures": {"ordre_de_prise": a["ordre_de_prise"], "sautees": a["sautees"]},
        "mesures_en_erreur": {"ordre_de_prise": b["ordre_de_prise"], "sautees": b["sautees"],
                              "cles_rendues": sorted(k for k in b if k != "texte")},
        "trace_du_repli_dans_le_rendu": any("convergence" in json.dumps(v, ensure_ascii=False) for k, v in b.items() if k != "texte")}

    # --- E4 --------------------------------------------------------------------------------------------------------------
    conv_loin = {"par_proposeur": {"opus": {"opus-p1-01": {"identifiant_passe_1": "opus-p1-01", "identifiant_passe_2": "opus-p2-01",
                                                           "appariement": "texte le plus proche", "distance_edition": 0.97}}}}
    sortie_de_bras(w / "e4", ["opus-p1-01", "opus-p2-01", "fable-p1-01"], conv_loin)
    c = lc.choisir_fiches_recues(w / "e4", 1)
    out["E4_appariement_texte_le_plus_proche_sans_seuil"] = {
        "appariement_servi": "texte le plus proche, distance d'édition 0,97 (deux textes presque sans mot commun)",
        "ordre_de_prise": c["ordre_de_prise"], "sautees": c["sautees"]}

    # --- E5 --------------------------------------------------------------------------------------------------------------
    cinq = ["opus-p1-01", "fable-p1-01", "argon-p1-01", "opus-p1-02", "fable-p1-02"]
    base = lc.taille_servie(fiche("opus-p1-01", 0))
    cible = lc.TAILLE_MAX_FICHES_RECUES // 5 - base            # chaque fiche servie fait exactement 10 000 caractères
    sortie_de_bras(w / "e5", cinq, {"par_proposeur": {}}, tailles={i: cible for i in cinq})
    d = lc.choisir_fiches_recues(w / "e5", 1)
    fiches5 = {f["identifiant_auteur"]: f for f in json.loads((w / "e5" / "fiches-validees.json").read_text())}
    out["E5_taille_de_la_piece"] = {"somme_des_tailles_servies": sum(lc.taille_servie(fiches5[i]) for i in d["ordre_de_prise"]),
                                    "fiches_prises": len(d["ordre_de_prise"]), "taille_de_la_piece_ecrite": d["taille_caracteres"],
                                    "plafond": lc.TAILLE_MAX_FICHES_RECUES,
                                    "piece_au_dela_du_plafond": d["taille_caracteres"] > lc.TAILLE_MAX_FICHES_RECUES}

    # --- E6 --------------------------------------------------------------------------------------------------------------
    import datetime as dt
    entete = "| id | accordé | type | périmètre | plafond | échéance | par | référence |\n|---|---|---|---|---|---|---|---|\n"
    go = ("| GO-2026-11-13-03 | 2026-11-13 | calcul | Organisme d'idéation, atelier d'idées, bassins : trois générations | 60 USD "
          "| 2026-11-30 | Lazar | R-2530 |\n")
    cas = {
        "sain_sans_revocation": "",
        "revocation_bien_formee": "| GO-2026-11-14-01 | 2026-11-14 | révocation | révoque GO-2026-11-13-03 | — | — | Lazar | R-x |\n",
        "revocation_a_9_colonnes": "| GO-2026-11-14-01 | 2026-11-14 | révocation | révoque GO-2026-11-13-03 | motif | — | — | Lazar | R-x |\n",
        "revocation_type_sans_accent": "| GO-2026-11-14-01 | 2026-11-14 | revocation | révoque GO-2026-11-13-03 | — | — | Lazar | R-x |\n",
        "revocation_type_majuscule": "| GO-2026-11-14-01 | 2026-11-14 | Révocation | révoque GO-2026-11-13-03 | — | — | Lazar | R-x |\n",
        "extension_a_100_usd": "| GO-2026-11-13-03 | 2026-11-14 | calcul | extension : plafond relevé | 100 USD | 2026-11-30 | Lazar | R-y |\n",
        "plafond_principal_a_100_usd": None,
    }
    e6 = {}
    for nom_cas, ligne in cas.items():
        p = w / "e6" / (nom_cas + ".md")
        p.parent.mkdir(exist_ok=True)
        p.write_text(entete + (go.replace("60 USD", "100 USD") if ligne is None else go + ligne), encoding="utf-8")
        res = essayer(lambda: lc.verifier_go(p, dt.date(2026, 11, 14)))
        e6[nom_cas] = ({"passe": True, "plafond_usd": res["rendu"]["plafond_usd"]} if "rendu" in res else
                       {"passe": False, "motif": res["message"][:120]})
    e6["borne_du_cumul_si_plafond_lu_100"] = lc.garde_cumul([], 20.0, 100.0)["borne_usd"]
    out["E6_ligne_de_GO"] = e6

    # --- E7, E8 ----------------------------------------------------------------------------------------------------------
    def monde(nom_dossier, code_bras, lisible, avec_bras_lanceur=True, avec_manifeste_bras=True):
        base_ = w / nom_dossier
        so = base_ / "sorties" / ("20261113-140001" + lc.SUFFIXE_RUN + "1") / "sortie"
        ru = base_ / "runs" / ("20261113-140001" + lc.SUFFIXE_RUN + "1")
        sceller(ru / "manifeste-lanceur-depart.json", {"generation": 1, "lanceur": {"version": lc.VERSION}, "sortie": str(so)})
        sceller(ru / "manifeste-lanceur-fin.json", {"generation": 1, "code": 0})
        sceller(so / "manifeste-fin.json", {"reglages": {"journal": {"cout_total_usd": 2.0, "cout_externe_usd": 2.5},
                                                         "en_attente_bras": True, "statut_course": {"statut": "ok"}}})
        if avec_manifeste_bras:
            sceller(so / "manifeste-bras-rapporte.json", {"reglages": {"journal": {"cout_total_usd": 1.2}}})
            sceller(so / ("classement.json" if code_bras in (0, 4) else "classement-sans-bras.json"),
                    {"lisible_L2_L4": lisible, "lignes": []})
        if avec_bras_lanceur:
            sceller(ru / "manifeste-lanceur-bras-depart-1.json", {"generation": 1, "numero": 1})
            sceller(ru / "manifeste-lanceur-bras-fin-1.json", {"generation": 1, "numero": 1, "code": code_bras})
        rr = lc.Reglages.production()
        rr.dossier_runs = base_ / "runs"
        return lc.runs_du_lanceur(rr)
    m7 = monde("e7", 0, True, avec_bras_lanceur=False)
    out["E7_bras_joue_hors_du_lanceur"] = {
        "etat": "manifeste-bras-rapporte.json de l'orchestrateur (1,2 USD) présent ; aucun manifeste de bras du lanceur",
        "depense_run": essayer(lambda: lc.depense_run(m7[0])), "bras_reussi": lc.bras_reussi(m7[0]),
        "etat_generation_1": essayer(lambda: lc.etat_generation(m7, 1)["temps"])}
    e8 = {}
    for etiquette, code, lisible in (("code_4_classement_illisible", 4, False), ("code_5_sans_juge_externe", 5, False)):
        m8 = monde("e8-" + etiquette, code, lisible)
        e8[etiquette] = {"bras_reussi": lc.bras_reussi(m8[0]),
                         "etat_generation_1": essayer(lambda: lc.etat_generation(m8, 1)["temps"]),
                         "etat_generation_2": essayer(lambda: lc.etat_generation(m8, 2)["temps"]),
                         "depense_run": essayer(lambda: lc.depense_run(m8[0]))}
    out["E8_apres_un_bras_fini_sans_classement_lisible"] = e8

    # --- E9 --------------------------------------------------------------------------------------------------------------
    def pl(car, cpj=4.0):
        return round(lc.plancher_argon(car, cpj), 6)
    out["E9_planchers_de_la_commande_d_argon"] = {
        "formule": "⌈⌈caractères / c⌉ × 1,05⌉ × 8,3e-6 + (4 096 + 8 192) × 41,5e-6 (lue dans commande_argon_v3d.py, l. 818-853)",
        "controle_court_41_caracteres": {"plancher": pl(41), "plafond_v1": lc.CONTROLE_BRAS_USD, "passe_v1": lc.CONTROLE_BRAS_USD >= pl(41),
                                         "defaut_de_l_orchestrateur_0_2_passerait": 0.2 >= pl(41)},
        "v3_controle_externe_415253_caracteres": {"plancher_a_4": pl(415253), "plafond_v3": 1.25, "passerait": 1.25 >= pl(415253)},
        "v3_controle_du_bras_defaut_0_2": {"plancher": pl(41), "passerait": 0.2 >= pl(41)},
        "v1_controle_externe_322793": {"plancher_a_4": pl(322793), "plancher_a_3": pl(322793, 3.0), "plafond": lc.CONTROLE_EXTERNE_USD,
                                       "caracteres_par_jeton_au_plus_bas_qui_passe": round(next(
                                           c / 100 for c in range(400, 100, -1) if pl(322793, c / 100) > lc.CONTROLE_EXTERNE_USD) + 0.01, 2)},
        "v1_controle_externe_generations_2_3_333000": {"plancher_a_4": pl(333000), "plancher_a_3": pl(333000, 3.0)},
        "v1_passe_1_56691": {"plancher_a_4": pl(56691), "plafond": lc.PLAFONDS["proposeur_ideation|gemini-4-argon"]},
        "v1_passe_2_fiches_8000": {"plancher_a_4": pl(56691 + 6 * 8009), "plafond": lc.PASSE_2_EXTERNE_USD},
        "v1_juge_a_la_garde_600000": {"plancher_a_4": pl(600000), "plancher_a_3": pl(600000, 3.0),
                                      "plafond": lc.PLAFONDS["juge_ideation|gemini-4-argon"],
                                      "sortie_laissee_au_juge_jetons_a_4": int((2.5 - (pl(600000) - (4096 + 8192) * 41.5e-6)) / 41.5e-6) - 8192},
    }

    # --- E10 -------------------------------------------------------------------------------------------------------------
    def norm(t):
        return re.sub(r"\s+", " ", t).strip()
    q_org = norm((DEPOT / lc.PIECES["question"][0]).read_text(encoding="utf-8"))
    q_col = (DEPOT / "docs/notes/collisionneur-bassins-etroits-v1/question-v1.md").read_text(encoding="utf-8")
    coeur = norm(q_col.split("## Question (étage III)", 1)[1])
    contraintes = norm(q_col.split("**Contraintes qui ne se discutent pas ici** :", 1)[1].split("## Question", 1)[0])
    contraintes_org = contraintes[0].upper() + contraintes[1:]
    out["E10_fidelite_de_la_question"] = {
        "coeur_mot_pour_mot": coeur in q_org, "longueur_du_coeur": len(coeur),
        "contraintes_mot_pour_mot_a_la_majuscule_initiale_pres": contraintes_org in q_org, "longueur_des_contraintes": len(contraintes),
        "caracteres_de_la_question_de_l_organisme": len(q_org),
        "mots_a_risque_dans_la_question": {m: len(re.findall(m, q_org, re.I)) for m in
                                           ("graine", "loi plantée", "seuil", "température", "tournoi de juges")}}

    # --- E11 -------------------------------------------------------------------------------------------------------------
    def cout_fin(valeur_json):
        d_ = w / "e11" / hashlib.sha256(valeur_json.encode()).hexdigest()[:8] / "sortie"
        sceller(d_ / "manifeste-fin.json", texte='{"reglages": {"journal": {"cout_total_usd": ' + valeur_json
                + ', "cout_externe_usd": 1.0}}}\n')
        return list(lc.depense_course(d_))
    out["E11_couts_mal_formes_au_manifeste_de_fin"] = {v: essayer(lambda: cout_fin(v)) for v in
                                                       ("2.5", "-1", "NaN", "Infinity", "true", '"2.5"', "null", "25.0")}
    print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
