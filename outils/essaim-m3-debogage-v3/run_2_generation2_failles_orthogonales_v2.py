# -*- coding: utf-8 -*-
"""
run_2_generation2_failles_orthogonales_v2 — version déboguée de `finish_gen2_and_publication_swarm.py` (dossier 17).

Plantages d'origine : (1) `AttributeError: module ... has no attribute 'format_live_blackboard_context'` (la fonction
n'existe pas dans le moteur ; ici elle est dans `m3_commun.Tableau.contexte`) ; (2) `SyntaxError` sur
`def run_orthogonal_ swarm_unit` (espace dans le nom) ; (3) à la troisième tentative, 1 réponse sur 36 et aucun bloc
LaTeX : les 35 échecs d'interface étaient avalés et le script continuait comme si l'essaim avait répondu.

Ce que fait ce script : la « génération 2 » (chasse aux failles d'autres classes) avec 36 castes, 6 sondes d'écart,
analyse spectrale calculée, extraction JSON, synthèse par l'arbitre, assimilation dans la mémoire spectrale.

Retiré par rapport à l'original :
  * les « spécifications G=2 » (`GEN_2_MASSIVE_ORTHOGONAL_RLCR_PROTOCOL`, `GEN_2_KOOPMAN_ISVD_SPECTRAL_SHIELD`)
    étaient écrites en dur dans le script puis rangées dans le substrat comme si l'essaim les avait conçues ;
    ici, seul ce que l'extraction tire des posts entre au substrat, avec sa provenance ;
  * la stratégie de publication, le manuscrit arXiv et le billet de forum (nœud N-037, dépense sans mesure).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import m3_commun as m3  # noqa: E402
import memoire_isvd_plugin_revu as memoire  # noqa: E402

MISSION_G2 = (
    "MISSION GÉNÉRATION G=2 — RECHERCHE DE FAILLES ET D'ÉNONCÉS D'AUTRES CLASSES :\n"
    "Les failles de stéganographie (SVG vers PNG, Voronoï E_8, variétés de drapeaux de Schubert) et les failles de "
    "canaux temporels matériels (cache, conditionnement Cholesky IEEE 754) ont déjà été discutées à la génération 1.\n"
    "Ne propose pas de simples extensions de ces deux classes.\n\n"
    "Cherche des failles d'autres classes contre l'architecture à cinq volets décrite et contre les protocoles de "
    "récompense de calibration :\n"
    "1. Failles de l'opérateur causal « Do-Clamp » $P_{\\text{do}}^2 = P_{\\text{do}}$ et du dictionnaire quadratique "
    "de Koopman $\\psi(h) = [h; h^2]$ (singularités algébriques du relèvement, illusions d'orthogonalité, annulations "
    "croisées entre $h$ et $h^2$).\n"
    "2. Failles statistiques contre le volet V (trois modèles croisés 3 × 3, test stratifié de Cochran-Mantel-Haenszel, "
    "homogénéité de Breslow-Day) : une politique adverse coordonnée ou un paradoxe de Simpson peut-il annuler la "
    "statistique globale tout en gardant un biais par strate ?\n"
    "3. Failles de martingales et d'arrêt optimal (temps d'arrêt de Doob, filtrations $\\mathcal{F}_t$) contre le "
    "CUSUM pré-blanchi AR(1) du volet IV et la rétraction radiale $\\mathcal{C}^1$ sous K = 1..6 rejets.\n"
    "4. Failles d'empoisonnement de la mémoire spectrale tronquée $\\mathcal{M}_{G+1} = \\mathcal{P}_{r_{\\max}}(U_G "
    "\\Sigma_G V_G^\\top + \\sum q_{G,j} \\psi(x)\\psi(x)^\\top)$ (rotation lente des vecteurs propres dominants par "
    "injection de vecteurs à forte confiance près du seuil de troncature).\n"
    "Pour chaque faille : l'équation de l'attaque, l'opérateur proposé pour la fermer, et ce qui reste conjectural."
)
CLES_G2 = ["new_rlcr_blackboard_and_uncertainty_mechanisms", "new_math_concepts_discovered",
           "new_loop_topologies_and_rlcr_laws", "new_anti_cover_up_reward_encodings",
           "literature_and_forum_flaws_found", "novel_beyond_labs_flaws_found",
           "epigenetic_axiom_for_next_generations"]


def main(argv=None) -> int:
    p = m3.analyseur_arguments("Génération 2 : failles d'autres classes — version déboguée v2")
    p.add_argument("--n-castes", type=int, default=36)
    p.add_argument("--n-sondes-ecart", type=int, default=6)
    args = p.parse_args(argv)
    config = m3.config_depuis_arguments(args, "generation2-failles", __file__)
    journal, budget, client = m3.preparer(config)
    substrat = m3.charger_substrat(config.substrat)
    store = m3.magasin(substrat)
    castes = m3.castes_du_substrat(substrat)
    reponses: list = []
    arret = None
    try:
        projection = memoire.projeter(store, 2)
        deja_concepts = store.get("discovered_mathematical_concepts", [])
        deja_failles = store.get("novel_beyond_labs_flaws_eliminated", [])
        journal.dire(f"=== [ÉTAPE 1/1] GÉNÉRATION 2 : {args.n_castes} castes, {args.n_sondes_ecart} sondes d'écart ===")
        tableau = m3.Tableau()
        castes_sel = m3.selectionner_castes(castes, args.n_castes)
        reps = m3.executer_vague(
            client, tableau, castes_sel,
            lambda c, ctx: (f"{MISSION_G2}\n\n=== MÉMOIRE DES RUNS PRÉCÉDENTS ===\n{projection[:2000]}\n\n{ctx}\n\n"
                            f"Concepts déjà rangés ({len(deja_concepts)}) : {deja_concepts[-10:]}\n"
                            f"Failles déjà rangées ({len(deja_failles)}) : {deja_failles[-10:]}\n\n"
                            f"Publie une contribution nouvelle avec ses équations LaTeX $$...$$.\n"
                            f"Focus (#{c['slot']}) : {c.get('focus') or 'libre'}"),
            "G2", journal)
        reponses += reps
        spectre = m3.analyse_spectrale([p_["content"] for p_ in tableau.posts])
        journal.dire(f"  * analyse spectrale : {json.dumps(spectre, ensure_ascii=False)[:300]}")
        reps_m2 = m3.sondes_orthogonales(
            client, tableau, args.n_sondes_ecart, "G2",
            "Démontre un énoncé d'impossibilité ou une faille structurelle d'une classe différente de tout ce qui "
            "précède au tableau, avec ses équations LaTeX, et dis ce qui reste conjectural.",
            journal, spectre.get("structures_saturees", []))
        reponses += reps_m2
        joint = "\n\n".join(f"=== {p_['author']} ===\n{p_['content'][:900]}" for p_ in tableau.posts)
        ext = m3.extraire_json_structure(
            client, f"Contributions de {len(tableau.posts)} agents :\n\n{joint[:18000]}\n\n"
                    "Extrais fidèlement, sans rien inventer : les mécanismes de tableau et de calibration proposés, les "
                    "concepts mathématiques, les topologies de boucles, les encodages de récompense, les failles tirées de "
                    "la littérature, les failles nouvelles d'autres classes, et un éventuel axiome pour la génération "
                    "suivante. Cite l'étiquette de l'agent source entre crochets pour chaque élément.", CLES_G2, "G2")
        journal.dire(f"  * extraction M1 : {'ok' if ext['ok'] else 'ÉCHEC'} ; "
                     + " ; ".join(f"{k[:24]}={len(v)}" for k, v in ext["donnees"].items()))
        synthese = client.appeler(
            config.arbitre,
            f"Blocs LaTeX du tableau ({len(tableau.blocs)}) :\n" + "\n".join(f"- $${b}$$" for b in tableau.blocs[:25])
            + f"\n\nExtraction :\n{json.dumps(ext['donnees'], ensure_ascii=False, indent=2)[:8000]}\n\n"
            "Rédige la synthèse mathématique consolidée (énoncés, preuves esquissées, opérateurs, conditions de "
            "stabilité, et ce qui reste conjectural), en LaTeX $$...$$, sans rien ajouter aux éléments extraits.",
            0.25, "G2_M0")
        reponses.append(synthese)

        if ext["ok"]:
            d = ext["donnees"]
            store["discovered_mathematical_concepts"] = m3.fusionner_uniques(
                store.get("discovered_mathematical_concepts", []), d["new_math_concepts_discovered"])
            store["invented_rlcr_blackboard_mechanisms"] = m3.fusionner_uniques(
                store.get("invented_rlcr_blackboard_mechanisms", []), d["new_rlcr_blackboard_and_uncertainty_mechanisms"])
            store["invented_loop_topologies_and_rlcr_laws"] = m3.fusionner_uniques(
                store.get("invented_loop_topologies_and_rlcr_laws", []), d["new_loop_topologies_and_rlcr_laws"])
            store["invented_anti_cover_up_reward_encodings"] = m3.fusionner_uniques(
                store.get("invented_anti_cover_up_reward_encodings", []), d["new_anti_cover_up_reward_encodings"])
            store["literature_and_forum_flaws_eliminated"] = m3.fusionner_uniques(
                store.get("literature_and_forum_flaws_eliminated", []), d["literature_and_forum_flaws_found"])
            store["novel_beyond_labs_flaws_eliminated"] = m3.fusionner_uniques(
                store.get("novel_beyond_labs_flaws_eliminated", []), d["novel_beyond_labs_flaws_found"])
            if d["new_rlcr_blackboard_and_uncertainty_mechanisms"]:
                substrat.setdefault("endogenous_rlcr_blackboard_protocols_designed", []).append({
                    "generation": 2, "provenance": f"extrait des posts par l'arbitre, run {config.nom_run}",
                    "mecanismes": d["new_rlcr_blackboard_and_uncertainty_mechanisms"]})
            substrat["current_generation"] = 2
        if synthese.ok:
            memoire.assimiler(store, 2, [synthese.texte])
            substrat["evolved_architecture_spec"] = (
                str(substrat.get("evolved_architecture_spec", "")) + "\n\n=== SYNTHÈSE G=2 (run "
                f"{config.nom_run}, {'à blanc' if config.a_blanc else 'réel'}, non auditée) ===\n\n" + synthese.texte)
        store.setdefault("historique_runs_debogage", []).append({
            "run": config.nom_run, "script": Path(__file__).name, "a_blanc": config.a_blanc,
            "unites": {"G2": m3.resumer_reponses(reps + reps_m2)}, "extraction_ok": ext["ok"],
            "synthese_M0": {"statut": synthese.statut, "modele_servi": synthese.modele_servi,
                            "empreinte": synthese.empreinte_texte}, "spectre": spectre})
        sections = [
            ("Comptes", f"- agents (appels) : {m3.resumer_reponses(reponses)}\n- blocs LaTeX : {len(tableau.blocs)}\n"
                        f"- analyse spectrale : `{json.dumps(spectre, ensure_ascii=False)}`\n"
                        f"- extraction M1 : {'ok' if ext['ok'] else 'ÉCHEC'}"),
        ] + [(f"Extraction : {k}", "\n".join(f"{i + 1}. {x}" for i, x in enumerate(v)) or "(rien)")
             for k, v in ext["donnees"].items()] + [
            ("Synthèse de l'arbitre (M0)", synthese.texte if synthese.ok else f"(échec : {synthese.statut} {synthese.erreur})"),
            ("Mémoire spectrale après assimilation", memoire.projeter(store, 3)),
        ]
        m3.ecrire_rapport(config.dossier_run / "rapport_generation2.md",
                          "Génération 2 : failles d'autres classes — rapport de run (exploratoire)", sections)
        m3.ecrire_json(config.dossier_run / "extraction_m1.json", ext)
    except m3.BudgetDepasse as exc:
        arret = f"arrêt sur plafond : {exc}"
        journal.dire("!!! " + arret)
    finally:
        m3.sauver_substrat(config.substrat, substrat)
        m3.sceller(config.journal) if config.journal.exists() else None
        m3.resume_final(config, budget, reponses, {"arret": arret})
        journal.dire(f"fin ; budget : {budget.etat()} ; sorties dans {config.dossier_run}")
    return 3 if arret else 0


if __name__ == "__main__":
    sys.exit(main())
