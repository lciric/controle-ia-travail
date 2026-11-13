#!/usr/bin/env python3
"""Contre-lecture du lanceur `lancer_course_ideation_bassins_etroits_v1.py` — outil 1 : contre l'orchestrateur réel, SANS APPEL.

Écrit par le contre-lecteur (Claude Fable 5.2), 13 novembre 2026. Aucun modèle appelé, aucun réseau, aucune course ni bras
lancé ; rien n'est écrit dans le clone de l'orchestrateur (`-B`, préfixe de cache hors du clone) ni dans le dépôt de travail
(toute écriture va dans le dossier de travail donné en argument).

Usage (cwd quelconque) :
    /usr/local/bin/python3 -I -B verifier_orchestrateur_reel_v1.py DOSSIER_DE_TRAVAIL_NEUF

Ce qu'il fait :
 A. charge l'analyseur d'arguments réel (`demonstrations/ideation_v2.py`, `construire_analyseur`) et lui donne les trois
    commandes que le lanceur construit (course, mesure, bras), telles quelles : acceptées ou non, valeurs lues ;
    rejoue à la main les contrôles d'arguments que `principal` fait après l'analyse pour le bras (lecture du code) ;
 B. fait construire une liste blanche par l'orchestrateur réel **à travers la fonction du lanceur**
    (`construire_liste_blanche`), dans le dossier de travail : mode sans appel de l'orchestrateur ;
 C. passe la garde lexicale « niveau méthode » de l'orchestrateur (`signaux_niveau_methode`) sur des phrases d'essai de
    vocabulaire mathématique écrites par le contre-lecteur, et sur les paragraphes des pièces servies (faits, question) ;
 D. liste les modules `pole.*` chargés par la chaîne et dit lesquels sont épinglés par empreinte dans le lanceur.
Sortie : un objet JSON sur la sortie standard.
"""
import importlib.util
import json
import os
import sys
import traceback
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
LANCEUR = DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v1.py"


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
    lc = charger("lanceur_v1_contre_lecture", LANCEUR)
    r = lc.Reglages.production()
    out = {"lanceur_sha256": lc.sha256_fichier(LANCEUR), "python": sys.executable, "version_python": sys.version.split()[0]}

    # --- A. analyseur réel --------------------------------------------------------------------------------------------
    pfx = travail / "pycache-fictif"
    sortie = Path("/x/sortie")
    course = lc.commande_course(r, sortie, Path("/x/liste-blanche.json"), "Fri Nov 13 14:00:00 UTC 2026", pfx,
                                DEPOT / lc.RECOUPEMENT, 1)
    mesure = lc.commande_mesure(r, Path("/x/liste-blanche.json"), pfx, DEPOT / lc.RECOUPEMENT)
    bras = lc.commande_bras(r, sortie, Path("/x/liste-blanche.json"), Path("/x/attestation.json"),
                            "Fri Nov 13 16:00:00 UTC 2026", pfx)
    out["commandes"] = {"course": course, "mesure": mesure, "bras": bras}
    v2 = charger("ideation_v2_contre_lecture", r.orchestrateur / "demonstrations" / "ideation_v2.py")
    analyses = {}
    for nom, argv in (("course", course), ("mesure", mesure), ("bras", bras)):
        assert argv[:5] == [r.python, "-I", "-B", "-X", f"pycache_prefix={pfx}"] and argv[5] == lc.LANCEUR_ORCHESTRATEUR
        a = v2.construire_analyseur()
        try:
            ns, inconnus = a.parse_known_args(argv[6:])
        except SystemExit as e:
            analyses[nom] = {"accepte": False, "code": e.code}
            continue
        d = vars(ns)
        prop, juges, juges_ext, prop_ext, budgets = v2.roles_et_budgets(ns)
        analyses[nom] = {
            "accepte": not inconnus, "arguments_inconnus": inconnus,
            "valeurs": {k: d[k] for k in ("sortie", "moteur", "bras_rapporte_differe", "attestation_lecture_humaine",
                                          "juge_externe", "proposeur_externe", "commande_externe", "liste_blanche", "budget",
                                          "budget_controle_usd", "budget_controle_externe_usd", "budget_passe_2_externe_usd",
                                          "budget_total_usd", "budget_externe_usd", "nombre", "graine", "seconde_passe",
                                          "confirmer_moteur_reel", "url_relais", "mesurer_consignes", "tests_de_mort",
                                          "moisson", "taille_max_consigne_externe", "taille_max_consigne_externe_bras",
                                          "accepter_sans_bac_a_sable", "prix_entree_usd_par_million_jetons", "horodatage")},
            "budget_externe_usd_explicite": bool(getattr(ns, "budget_externe_usd_explicite", False)),
            "roles": {"proposeurs": prop, "juges": juges, "juges_externes": juges_ext, "proposeurs_externes": prop_ext},
            "budgets_argon": {f"{k[0]}|{k[1]}": v for k, v in budgets.items() if "argon" in k[1]},
        }
        if nom in ("course", "mesure"):
            t, origine, detail, prov = v2.garde_de_la_course(ns, budgets, prop_ext)
            analyses[nom]["garde_de_la_course"] = {"taille": t, "origine": origine, "provision": prov}
    # contrôles d'arguments de `principal` après l'analyse, pour le bras (demonstrations/ideation_v2.py, l. 1005-1133),
    # rejoués ici à la main sur l'espace de noms analysé — aucune fonction de lancement n'est appelée
    b = v2.construire_analyseur().parse_args(bras[6:])
    controles = {
        "construire_liste_blanche_absent": not b.construire_liste_blanche,
        "mesurer_consignes_absent": not b.mesurer_consignes,
        "tests_de_mort_0_et_options_d_etage_absentes": b.tests_de_mort == 0 and not any(
            (b.tranche_exploratoire, b.experimentateur, b.experimentateur_externe, b.lecteur_test, b.utilisateur_bac,
             b.dossier_travail_bac, b.userns_imbriques_permis, b.memoire_bac_non_bornee_permise,
             b.commande_externe_accepte_experimentateur)) and b.executeur_tests == "bwrap",
        "moisson_aucune_sans_options": b.moisson == "aucune" and not any(
            (b.url_relais_moisson, b.cache_moisson, b.registre_bardeaux, b.confirmer_moisson_reelle)),
        "taille_max_consigne_externe_absente_au_bras": b.taille_max_consigne_externe is None,
        "sortie_donnee": bool(b.sortie),
        "juge_externe_et_attestation": bool(b.juge_externe and b.attestation_lecture_humaine),
        "pas_de_proposeur_externe_au_bras": not b.proposeur_externe,
        "commande_externe_avec_bras": bool(b.commande_externe and b.bras_rapporte_differe),
        "nombre_dans_les_bornes": 1 <= b.nombre <= v2.idn.MAX_FICHES_ABSOLU,
        "delais_positifs": (b.delai_session_s is None or b.delai_session_s > 0) and b.delai_commande_s > 0,
        "budget_passe_2_absent": b.budget_passe_2_externe_usd is None,
        "dossier_ferme_absent": not b.dossier_ferme and not b.outils_par_protocole and b.max_demandes_lecture is None,
    }
    analyses["bras"]["controles_de_principal_rejoues"] = controles
    analyses["bras"]["tous_tenus"] = all(controles.values())
    # ce que la branche du bras de `_principal` ferait de ces arguments (lecture du code, l. 1180-1259) :
    analyses["bras"]["lecture_de_la_branche"] = {
        "moteur": b.moteur,
        "branche_claude_sdk_prise": b.moteur == "claude-sdk" and (not b.bras_rapporte_differe or bool(b.tests_de_mort)),
        "verifier_commande_externe_reelle_agit": b.moteur == "claude-sdk" and bool(b.commande_externe),
        "exiger_modele_servi_de_l_adaptateur": b.moteur == "claude-sdk",
        "budget_controle_usd_transmis_au_bras": b.budget_controle_usd,
        "budget_externe_usd_transmis_au_bras": (b.budget_externe_usd if getattr(b, "budget_externe_usd_explicite", False)
                                                else None),
        "besoin_du_bras_usd": dict(v2.roles_et_budgets(b)[4])[("juge_ideation", "gemini-4-argon")] + b.budget_controle_usd,
    }
    out["analyseur_reel"] = analyses

    # --- B. liste blanche construite par l'orchestrateur réel à travers la fonction du lanceur --------------------------
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(travail), "LANG": "C.UTF-8"}
    chemin = travail / "liste-blanche.json"
    fichiers = {str(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "faits", "temoins")}
    essai = {"fichiers": sorted(fichiers)}
    try:
        res = lc.construire_liste_blanche(r, chemin, env, travail / "pycache-liste-blanche", fichiers)
        essai.update({"issue": "rendue", "sha256": res["sha256"]})
    except lc.Refus as e:
        essai.update({"issue": "Refus (garde du lanceur)", "message": str(e)[:600]})
    except BaseException as e:  # noqa: BLE001 — c'est l'objet de l'essai : toute autre exception est un arrêt non gardé
        essai.update({"issue": "exception non gardée par le lanceur", "type": type(e).__name__, "message": str(e)[:300],
                      "est_un_Refus": isinstance(e, lc.Refus),
                      "derniere_ligne_de_trace": traceback.format_exc().strip().splitlines()[-3:]})
    essai["fichiers_ecrits_par_l_orchestrateur"] = sorted(p.name for p in travail.iterdir() if p.name.startswith("liste-blanche"))
    out["liste_blanche_reelle"] = essai

    # --- C. garde lexicale « niveau méthode » de l'orchestrateur ---------------------------------------------------------
    idn = v2.idn
    phrases = [  # écrites par le contre-lecteur : vocabulaire ordinaire d'une fiche de mathématiques sur cette question
        "On construit une injection de l'espace des cartes dans un espace de Hilbert à noyau reproduisant.",
        "La méthode consiste à exploiter la structure conditionnelle du monde planté.",
        "Pour éviter que le juge statistique ne perde sa garantie, la sélection se fait sur une tranche à part.",
        "Étape 1 : estimer la masse du bassin sur un échantillon scellé. Étape 2 : comparer à la courbe nulle.",
        "Première étape : tirer les propositions ; seconde : mesurer la couverture.",
        "Afin de contourner la limite connue du juge (classe que son nul ne couvre pas), on élargit le nul.",
        "L'orchestrateur lance un script de regroupement des doublons sur les cartes.",
        "Un processus ponctuel déterminantal repousse les propositions voisines et favorise les bassins rares.",
        "La borne de dilution impose une lecture par strates de la distance entre lois.",
        "Le témoin à coût égal est la courbe 1 − (1 − r)^n des tirages indépendants.",
    ]
    out["garde_niveau_methode"] = {
        "phrases_d_essai_du_contre_lecteur": [{"phrase": p, "signaux": idn.signaux_niveau_methode(p)} for p in phrases],
        "phrases_signalees": sum(1 for p in phrases if idn.signaux_niveau_methode(p)), "phrases": len(phrases)}
    pieces = {}
    for nom in ("faits", "question"):
        texte = (r.depot / r.pieces[nom][0]).read_text(encoding="utf-8")
        paragraphes = [p for p in texte.split("\n\n") if p.strip()]
        touches = [{"debut": p.strip()[:70], "signaux": idn.signaux_niveau_methode(p)} for p in paragraphes
                   if idn.signaux_niveau_methode(p)]
        pieces[nom] = {"paragraphes": len(paragraphes), "signales": len(touches), "detail": touches}
    out["garde_niveau_methode"]["pieces_servies"] = pieces
    temoins = json.loads((r.depot / r.pieces["temoins"][0]).read_text(encoding="utf-8"))["temoins"]
    out["temoins"] = [{"classe": t["classe"], "nom": t["fiche"]["nom"][:60],
                       "longueur_vue_servie": len(idn.texte_plat(t["fiche"])),
                       "signaux_niveau_methode": idn.signaux_niveau_methode(t["fiche"])} for t in temoins]

    # --- D. modules chargés et épinglage ---------------------------------------------------------------------------------
    racine = str(r.orchestrateur)
    charges = sorted(os.path.relpath(m.__file__, racine) for n, m in list(sys.modules.items())
                     if (n == "pole" or n.startswith("pole.")) and getattr(m, "__file__", None))
    epingles = set(lc.EMPREINTES_ORCHESTRATEUR)
    out["modules_pole_charges_par_ideation_v2"] = {
        "nombre": len(charges), "epingles_par_empreinte": [c for c in charges if c in epingles],
        "tenus_par_le_commit_seul": [c for c in charges if c not in epingles]}
    print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
