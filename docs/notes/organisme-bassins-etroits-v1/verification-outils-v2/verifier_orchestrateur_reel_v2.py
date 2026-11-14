#!/usr/bin/env python3
"""Vérification courte du lanceur v2 — outil 1 : contre l'orchestrateur réel, SANS APPEL.

Écrit par le contre-lecteur (Claude Fable 5.2), 13 novembre 2026. Aucun modèle, aucun réseau, aucune course ni bras lancé ;
rien n'est écrit dans le clone (`-B`, préfixe de cache hors du clone) ni dans le dépôt (tout va au dossier de travail).

Usage : /usr/local/bin/python3 -I -B verifier_orchestrateur_reel_v2.py DOSSIER_DE_TRAVAIL_NEUF

 A. commande du bras du v2 (avec `--moteur claude-sdk --confirmer-moteur-reel`, m6) : analyseur réel, contrôles d'arguments
    de `principal` rejoués à la main, lecture de la branche du bras de `_principal` ;
 B. liste blanche par l'orchestrateur réel à travers `construire_liste_blanche` du v2 (B1) ;
 C. témoins v2 : chargés par le chargeur réel (`charger_temoins`, liste blanche de B), longueurs servies, garde lexicale ;
    recherche, dans la question et les faits servis, des mots de l'idée du témoin vrai (M9) ;
 D. empreintes de l'orchestrateur épinglées par le v2 comparées à celles du v1.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


def main():
    travail = Path(sys.argv[1]).resolve()
    if travail.exists():
        raise SystemExit("le dossier de travail doit être neuf")
    travail.mkdir(parents=True)
    assert sys.dont_write_bytecode, "lancer avec -B"
    lc = charger("lanceur_v2_verification", DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v2.py")
    v1 = charger("lanceur_v1_verification", DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v1.py")
    r = lc.Reglages.production()
    out = {"lanceur_v2_sha256": lc.sha256_fichier(DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v2.py")}

    # --- A -------------------------------------------------------------------------------------------------------------
    pfx = travail / "pycache-fictif"
    bras = lc.commande_bras(r, Path("/x/sortie"), Path("/x/lb.json"), Path("/x/att.json"), "Fri Nov 13 16:00:00 UTC 2026", pfx)
    course = lc.commande_course(r, Path("/x/sortie"), Path("/x/lb.json"), "h", pfx, DEPOT / lc.RECOUPEMENT, 1)
    v2 = charger("ideation_v2_verification", r.orchestrateur / "demonstrations" / "ideation_v2.py")
    b, inconnus = v2.construire_analyseur().parse_known_args(bras[6:])
    c, inconnus_c = v2.construire_analyseur().parse_known_args(course[6:])
    prop, juges, juges_ext, prop_ext, budgets = v2.roles_et_budgets(b)
    controles = {
        "tests_de_mort_0_et_options_d_etage_absentes": b.tests_de_mort == 0 and not any(
            (b.tranche_exploratoire, b.experimentateur, b.experimentateur_externe, b.lecteur_test, b.utilisateur_bac,
             b.dossier_travail_bac, b.userns_imbriques_permis, b.memoire_bac_non_bornee_permise,
             b.commande_externe_accepte_experimentateur)) and b.executeur_tests == "bwrap",
        "moisson_aucune_sans_options": b.moisson == "aucune" and not any(
            (b.url_relais_moisson, b.cache_moisson, b.registre_bardeaux, b.confirmer_moisson_reelle)),
        "ni_mesure_ni_liste_blanche_a_construire": not b.mesurer_consignes and not b.construire_liste_blanche,
        "taille_max_consigne_externe_absente_au_bras": b.taille_max_consigne_externe is None,
        "sortie_donnee": bool(b.sortie),
        "juge_externe_et_attestation": bool(b.juge_externe and b.attestation_lecture_humaine),
        "pas_de_proposeur_externe_au_bras": not b.proposeur_externe,
        "commande_externe_avec_bras": bool(b.commande_externe and b.bras_rapporte_differe),
        "commande_externe_lit_modele_absent": not b.commande_externe_lit_modele,
        "nombre_dans_les_bornes": 1 <= b.nombre <= v2.idn.MAX_FICHES_ABSOLU,
        "delais_positifs": (b.delai_session_s is None or b.delai_session_s > 0) and b.delai_commande_s > 0,
        "budget_passe_2_absent": b.budget_passe_2_externe_usd is None,
        "dossier_ferme_absent": not b.dossier_ferme and not b.outils_par_protocole and b.max_demandes_lecture is None,
    }
    # `verifier_commande_externe_reelle` est une fonction pure (aucun appel) : jouée telle quelle sur l'espace de noms
    try:
        v2.verifier_commande_externe_reelle(b, prop_ext, juges_ext)
        verif = "passe (modèle du juge externe = modèle que la commande demande)"
    except Exception as e:  # noqa: BLE001
        verif = f"refus : {type(e).__name__} : {e}"
    out["bras"] = {
        "commande": bras, "arguments_inconnus": inconnus, "moteur": b.moteur, "confirmer_moteur_reel": b.confirmer_moteur_reel,
        "url_relais": b.url_relais, "controles_de_principal_rejoues": controles, "tous_tenus": all(controles.values()),
        "branche_claude_sdk_prise_au_bras": b.moteur == "claude-sdk" and (not b.bras_rapporte_differe or bool(b.tests_de_mort)),
        "verifier_commande_externe_reelle": verif,
        "exiger_modele_servi_de_l_adaptateur": b.moteur == "claude-sdk",
        "besoin_du_bras_usd": budgets[("juge_ideation", "gemini-4-argon")] + b.budget_controle_usd,
        "juges_externes": juges_ext}
    pc, jc, jec, pec, bc = v2.roles_et_budgets(c)
    t, origine, detail, prov = v2.garde_de_la_course(c, bc, pec)
    out["course"] = {"arguments_inconnus": inconnus_c, "budget_controle_externe_usd": c.budget_controle_externe_usd,
                     "garde_de_la_course": {"taille": t, "provision": prov},
                     "sommes_du_lanceur": {k: v for k, v in lc.garde_sommes(course).items() if k.startswith(("somme", "externe"))}}

    # --- B -------------------------------------------------------------------------------------------------------------
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(travail), "LANG": "C.UTF-8"}
    fichiers = {str(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "faits", "temoins")}
    try:
        lb = lc.construire_liste_blanche(r, travail / "liste-blanche.json", env, travail / "pycache-lb", fichiers)
        out["liste_blanche_reelle"] = {"issue": "rendue", "sha256": lb["sha256"], "compagnon": lb["compagnon"],
                                       "fichiers": sorted(p.name for p in travail.iterdir() if p.name.startswith("liste-blanche"))}
    except BaseException as e:  # noqa: BLE001
        out["liste_blanche_reelle"] = {"issue": "exception", "type": type(e).__name__, "message": str(e)[:300]}

    # --- C -------------------------------------------------------------------------------------------------------------
    idn = v2.idn
    try:
        liste = idn.charger_liste_blanche(str(travail / "liste-blanche.json"))
        temoins = idn.charger_temoins(str(r.depot / r.pieces["temoins"][0]), liste)
        out["temoins_v2"] = {"charges_par_le_chargeur_reel": len(temoins), "detail": [
            {"classe": t_["temoin"]["classe"], "attendu": t_["temoin"]["attendu"], "note_max": t_["temoin"]["note_max"],
             "nom": t_["nom"][:70], "longueur_vue_servie": len(idn.texte_plat(idn.vue_servie(t_))),
             "signaux_niveau_methode": idn.signaux_niveau_methode(idn.vue_servie(t_))} for t_ in temoins]}
    except BaseException as e:  # noqa: BLE001
        out["temoins_v2"] = {"issue": "exception", "type": type(e).__name__, "message": str(e)[:300]}
    mots = ["chao", "espèce", "espece", "richesse", "good-turing", "good–turing", "non vu", "f1", "capture", "masse manquante",
            "doublons", "nombre de groupes", "composantes plantées couvertes"]
    pieces = {}
    for nom in ("question", "faits"):
        texte = (r.depot / r.pieces[nom][0]).read_text(encoding="utf-8").lower()
        pieces[nom] = {m: len(re.findall(re.escape(m), texte)) for m in mots}
    out["mots_du_temoin_vrai_dans_les_pieces_fixes"] = pieces

    # --- D -------------------------------------------------------------------------------------------------------------
    out["empreintes_orchestrateur_v2_egales_au_v1"] = lc.EMPREINTES_ORCHESTRATEUR == v1.EMPREINTES_ORCHESTRATEUR
    out["plafonds"] = {"reglage_v2": lc.PLAFONDS, "controle_externe": lc.CONTROLE_EXTERNE_USD, "passe_2": lc.PASSE_2_EXTERNE_USD,
                       "controle_bras": lc.CONTROLE_BRAS_USD,
                       "claude_pire": 2 * 0.2 + 2 * (2.0 + 2.0) + 1.5,
                       "externe_pire": lc.CONTROLE_EXTERNE_USD + 1.3 + lc.PASSE_2_EXTERNE_USD + 2.5 + lc.CONTROLE_BRAS_USD}
    out["plafonds"]["generation_pire"] = round(out["plafonds"]["claude_pire"] + out["plafonds"]["externe_pire"], 6)
    out["plafonds"]["trois_generations_pire"] = round(3 * out["plafonds"]["generation_pire"], 6)
    out["planchers_argon_a_3"] = {n: round(lc.plancher_argon(c_, 3.0), 6) for n, c_ in
                                  (("controle_322793", 322793), ("controle_332856", 332856), ("passe_1_56691", 56691),
                                   ("passe_2_104745", 104745), ("juge_600000", 600000), ("controle_court_200", 200))}
    print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
