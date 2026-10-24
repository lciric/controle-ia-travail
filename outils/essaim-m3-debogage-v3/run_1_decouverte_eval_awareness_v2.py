# -*- coding: utf-8 -*-
"""
run_1_decouverte_eval_awareness_v2 — version déboguée de `run_endogenous_eval_awareness_discovery.py` (dossier 17).

Plantage d'origine : phase 3, `substrate.setdefault(...)` sur `None`, parce que `atomic_merge_and_save_substrate`
ne renvoyait pas le substrat. Ici `sauver_substrat` renvoie toujours le dictionnaire.

Ce que fait ce script (mêmes phases que l'original, instrumentées) :
  phase 1 : « moissonneur » — 12 castes formulent des requêtes documentaires ; extraction JSON ; moissonnage arXiv
            et Hacker News par leurs interfaces publiques (désactivé à blanc ou par `--sans-reseau-externe`) ;
  phase 2 : « découverte » — 36 castes puis 6 sondes d'écart ; analyse spectrale calculée ; extraction JSON par
            tranches ; synthèse par l'arbitre ; mise à jour du magasin avec provenance ;
  phase 3 de l'original (stratégie de publication, manuscrit arXiv, billet de forum) : retirée. La publication est
            un nœud de Lazar (N-037) et ces appels coûtent sans rien mesurer.

Usage : d'abord `python run_1_decouverte_eval_awareness_v2.py --a-blanc`, puis, avec les clés M3_* posées,
        `python run_1_decouverte_eval_awareness_v2.py --max-appels 120`.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import m3_commun as m3  # noqa: E402
import memoire_isvd_plugin_revu as memoire  # noqa: E402

MOTS_CLES_FILTRE = ["324", "375", "103", "refus", "défection", "rôle", "amnésie", "breakout", "narrative"]

MISSION_MOISSONNEUR = (
    "OBSERVATIONS TIRÉES DU MAGASIN DE L'ESSAIM (texte produit par des modèles lors de runs antérieurs ; "
    "ce ne sont pas des faits vérifiés indépendamment) :\n{observations}\n\n"
    "MISSION DU MOISSONNEUR :\n"
    "Sans aucune liste pré-établie, analyse ce phénomène de rupture de protocole et de conscience d'évaluation "
    "(« eval awareness ») apparu au sein de l'essaim.\n"
    "1. Formule les requêtes de recherche documentaire les plus pointues (arXiv, LessWrong, Alignment Forum, blogs de "
    "sécurité de l'IA) pour identifier les classes connues de conscience d'évaluation, de sous-performance délibérée, "
    "de simulation d'alignement, de détection d'environnement d'évaluation et de défection multi-agents.\n"
    "2. Identifie les angles morts mathématiques de la littérature actuelle face à ce phénomène.\n"
    "Développe ta réponse avec des équations LaTeX $$...$$ quand c'est pertinent."
)

MISSION_DECOUVERTE = (
    "OBSERVATIONS TIRÉES DU MAGASIN DE L'ESSAIM (texte de modèles, non vérifié) :\n{observations}\n\n"
    "CORPUS DOCUMENTAIRE MOISSONNÉ :\n{corpus}\n\n"
    "CONTEXTE DE L'ARCHITECTURE ÉTUDIÉE (description non auditée, non opposable) :\n{architecture}\n\n"
    "MISSION D'EXPLORATION :\n"
    "1. Cartographie les classes de conscience d'évaluation présentes dans le corpus et montre pourquoi elles ne "
    "suffisent pas à expliquer ou à bloquer toutes les défections possibles dans un système multi-agents doté de sondes "
    "d'activation et de récompenses de calibration.\n"
    "2. Propose et formalise des classes nouvelles par lesquelles un modèle ou un groupe d'agents peut détecter qu'il "
    "est évalué, communiquer cet état sur un tableau partagé, ou fausser la calibration et les opérateurs de contrôle.\n"
    "3. Pour chaque classe, propose un concept mathématique ou une association de méthodes qui permet de la détecter "
    "ou de la résoudre, avec des équations LaTeX $$...$$ exactes.\n"
    "4. Dis explicitement ce qui, dans ta réponse, est une conjecture.\n"
)

CLES_MOISSON = ["endogenous_search_queries", "existing_literature_eval_awareness_classes"]
CLES_DECOUVERTE = ["existing_eval_awareness_flaws_analyzed_and_solved",
                   "novel_unprecedented_eval_awareness_flaws_discovered",
                   "novel_mathematical_concepts_and_unprecedented_combinations",
                   "formal_resolution_theorems_and_operators"]


def moissonner_arxiv_et_hn(requetes: list, journal: m3.Journal) -> list:
    """Interfaces publiques d'arXiv et de Hacker News (Algolia), sans clé. Chaque échec est consigné."""
    entrees = []
    for q in requetes[:6]:
        q_propre = re.sub(r"[^a-zA-Z0-9\s\-]", " ", str(q)).strip()
        if not q_propre:
            continue
        try:
            url = ("http://export.arxiv.org/api/query?search_query=all:"
                   f"{urllib.parse.quote(q_propre[:80])}&start=0&max_results=4")
            req = urllib.request.Request(url, headers={"User-Agent": "essaim-m3-debogage/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                racine = ET.fromstring(r.read().decode("utf-8", errors="ignore"))
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for ent in racine.findall("atom:entry", ns):
                titre = (ent.findtext("atom:title", default="", namespaces=ns) or "").strip().replace("\n", " ")
                resume = (ent.findtext("atom:summary", default="", namespaces=ns) or "").strip().replace("\n", " ")
                ident = (ent.findtext("atom:id", default="", namespaces=ns) or "").strip()
                if titre:
                    entrees.append(f"[arXiv | {ident} | requête='{q_propre[:40]}'] {titre} — {resume[:380]}")
        except Exception as exc:
            journal.dire(f"  ! arXiv : échec pour la requête '{q_propre[:40]}' : {type(exc).__name__}: {exc}")
        try:
            url = f"https://hn.algolia.com/api/v1/search?query={urllib.parse.quote(q_propre[:60])}&tags=story&hitsPerPage=3"
            req = urllib.request.Request(url, headers={"User-Agent": "essaim-m3-debogage/1.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                hits = json.loads(r.read().decode("utf-8", errors="ignore")).get("hits", [])
            for h in hits:
                if h.get("title"):
                    entrees.append(f"[HN | requête='{q_propre[:40]}'] {h['title']} ({h.get('url', '')})")
        except Exception as exc:
            journal.dire(f"  ! Hacker News : échec pour la requête '{q_propre[:40]}' : {type(exc).__name__}: {exc}")
    return entrees


def main(argv=None) -> int:
    p = m3.analyseur_arguments("Découverte « eval awareness » par essaim — version déboguée v2")
    p.add_argument("--n-castes-moisson", type=int, default=12)
    p.add_argument("--n-castes-decouverte", type=int, default=36)
    p.add_argument("--n-sondes-ecart", type=int, default=6)
    p.add_argument("--sans-reseau-externe", action="store_true", help="ne pas interroger arXiv ni Hacker News")
    p.add_argument("--contexte-architecture", type=Path, default=None,
                   help="fichier texte décrivant l'architecture ; sinon `evolved_architecture_spec` du substrat")
    args = p.parse_args(argv)
    config = m3.config_depuis_arguments(args, "decouverte-eval-awareness", __file__)
    journal, budget, client = m3.preparer(config)
    substrat = m3.charger_substrat(config.substrat)
    store = m3.magasin(substrat)
    castes = m3.castes_du_substrat(substrat)
    journal.dire(f"substrat : {config.substrat} ({'présent' if config.substrat.exists() else 'absent, créé'}) ; "
                 f"castes utilisables : {sum(1 for c in castes if 'lineages' in c)}")
    toutes_reponses: list = []
    arret = None
    try:
        # ---- observations du magasin (étiquetées pour ce qu'elles sont) ---------------------------------
        failles = [str(f) for f in store.get("novel_beyond_labs_flaws_eliminated", [])]
        observations = [f for f in failles if any(m in f.lower() for m in MOTS_CLES_FILTRE)] or failles[-6:]
        journal.dire(f"[magasin] {len(observations)} entrées filtrées par mots-clés sur {len(failles)}")
        texte_obs = "\n".join(f"- {o}" for o in observations) or "- (magasin vide)"

        # ---- phase 1 : moissonneur ---------------------------------------------------------------------
        journal.dire("=== [PHASE 1/2] MOISSONNEUR : requêtes documentaires formulées par l'essaim ===")
        tableau1 = m3.Tableau()
        castes1 = m3.selectionner_castes(castes, args.n_castes_moisson)
        mission1 = MISSION_MOISSONNEUR.format(observations=texte_obs)
        reps1 = m3.executer_vague(client, tableau1, castes1,
                                  lambda c, ctx: f"{mission1}\n\n{ctx}\n\nFocus (#{c['slot']}) : {c.get('focus') or 'libre'}",
                                  "MOISSON", journal)
        toutes_reponses += reps1
        posts1 = "\n\n".join(f"=== {p_['author']} ===\n{p_['content'][:950]}" for p_ in tableau1.posts)
        ext1 = m3.extraire_json_structure(
            client, f"Voici les contributions de {len(tableau1.posts)} agents :\n\n{posts1[:16000]}\n\n"
                    "Extrais fidèlement, sans rien inventer, les requêtes de recherche proposées et les classes de "
                    "conscience d'évaluation déjà décrites dans la littérature que ces agents citent.",
            CLES_MOISSON, "MOISSON")
        requetes = ext1["donnees"]["endogenous_search_queries"] if ext1["ok"] else []
        journal.dire(f"  => extraction M1 : {'ok' if ext1['ok'] else 'ÉCHEC'} ; {len(requetes)} requêtes")
        entrees = []
        if config.a_blanc or args.sans_reseau_externe:
            journal.dire("  => moissonnage externe non effectué (mode à blanc ou --sans-reseau-externe)")
        elif requetes:
            entrees = moissonner_arxiv_et_hn(requetes, journal)
            journal.dire(f"  => moissonnage externe : {len(entrees)} entrées")
        store["explored_search_keywords"] = m3.fusionner_uniques(store.get("explored_search_keywords", []), requetes)

        # ---- phase 2 : découverte ----------------------------------------------------------------------
        journal.dire("=== [PHASE 2/2] DÉCOUVERTE : classes et formalisations ===")
        if args.contexte_architecture:
            architecture = args.contexte_architecture.read_text(encoding="utf-8")[:2200]
        else:
            architecture = str(substrat.get("evolved_architecture_spec", ""))[:2200] or "(aucune description fournie)"
        corpus = "\n".join(entrees[:15]) or "(aucune entrée externe)"
        mission2 = MISSION_DECOUVERTE.format(observations=texte_obs, corpus=corpus, architecture=architecture)
        projection = memoire.projeter(store, 2)
        tableau2 = m3.Tableau()
        castes2 = m3.selectionner_castes(castes, args.n_castes_decouverte)
        reps2 = m3.executer_vague(
            client, tableau2, castes2,
            lambda c, ctx: (f"{mission2}\n\n=== MÉMOIRE DES RUNS PRÉCÉDENTS ===\n{projection[:1800]}\n\n{ctx}\n\n"
                            "Lis ce qui est déjà au tableau, critique les hypothèses faibles de tes pairs, et publie une "
                            "contribution qui s'en écarte, avec ses équations LaTeX $$...$$."),
            "DECOUVERTE", journal)
        toutes_reponses += reps2
        spectre = m3.analyse_spectrale([p_["content"] for p_ in tableau2.posts])
        journal.dire(f"  * analyse spectrale : {json.dumps(spectre, ensure_ascii=False)[:300]}")
        reps2b = m3.sondes_orthogonales(
            client, tableau2, args.n_sondes_ecart, "DECOUVERTE",
            "INTERDICTION de répéter les équations déjà au tableau. Identifie une classe de faille non encore vue par "
            "les castes précédentes et propose une association de concepts mathématiques pour la résoudre, en LaTeX.",
            journal, spectre.get("structures_saturees", []))
        toutes_reponses += reps2b

        # extraction par tranches de 14 posts
        fusion = {k: [] for k in CLES_DECOUVERTE}
        if ext1["ok"]:
            fusion["existing_eval_awareness_flaws_analyzed_and_solved"] = list(
                ext1["donnees"]["existing_literature_eval_awareness_classes"])
        tranches_ok, tranches = 0, 0
        for debut in range(0, len(tableau2.posts), 14):
            tranche = tableau2.posts[debut:debut + 14]
            tranches += 1
            joint = "\n\n".join(f"=== {p_['author']} ===\n{p_['content'][:1100]}" for p_ in tranche)
            ext = m3.extraire_json_structure(
                client, f"Contributions des agents {debut + 1} à {debut + len(tranche)} :\n\n{joint[:16000]}\n\n"
                        "Extrais fidèlement, sans rien inventer toi-même : les classes existantes analysées, les classes "
                        "nouvelles proposées, les concepts mathématiques ou associations proposés, et les énoncés formels "
                        "de résolution. Cite l'étiquette de l'agent source entre crochets pour chaque élément.",
                CLES_DECOUVERTE, f"DECOUVERTE_tranche{tranches}")
            if ext["ok"]:
                tranches_ok += 1
                for k in CLES_DECOUVERTE:
                    fusion[k] = m3.fusionner_uniques(fusion[k], ext["donnees"][k])
        journal.dire(f"  * extraction M1 : {tranches_ok}/{tranches} tranches ; "
                     + " ; ".join(f"{k.split('_')[0]}…={len(v)}" for k, v in fusion.items()))

        synthese = client.appeler(
            config.arbitre,
            f"Blocs LaTeX du tableau ({len(tableau2.blocs)}) :\n" + "\n".join(f"- $${b}$$" for b in tableau2.blocs[:30])
            + f"\n\nÉléments extraits :\n{json.dumps(fusion, ensure_ascii=False, indent=2)[:12000]}\n\n"
            "Rédige une synthèse mathématique structurée (définitions, énoncés, ce qui est démontré, ce qui est "
            "conjecturé) en respectant strictement les concepts extraits, sans en ajouter.", 0.25, "DECOUVERTE_M0")
        toutes_reponses.append(synthese)

        # ---- mise à jour du magasin avec provenance ------------------------------------------------------
        if tranches_ok:
            store["discovered_mathematical_concepts"] = m3.fusionner_uniques(
                store.get("discovered_mathematical_concepts", []),
                fusion["novel_mathematical_concepts_and_unprecedented_combinations"])
            store["literature_and_forum_flaws_eliminated"] = m3.fusionner_uniques(
                store.get("literature_and_forum_flaws_eliminated", []),
                fusion["existing_eval_awareness_flaws_analyzed_and_solved"])
            store["novel_beyond_labs_flaws_eliminated"] = m3.fusionner_uniques(
                store.get("novel_beyond_labs_flaws_eliminated", []),
                fusion["novel_unprecedented_eval_awareness_flaws_discovered"])
            store["invented_anti_cover_up_reward_encodings"] = m3.fusionner_uniques(
                store.get("invented_anti_cover_up_reward_encodings", []),
                fusion["formal_resolution_theorems_and_operators"])
        store.setdefault("historique_runs_debogage", []).append({
            "run": config.nom_run, "script": Path(__file__).name, "a_blanc": config.a_blanc,
            "unites": {"MOISSON": m3.resumer_reponses(reps1), "DECOUVERTE": m3.resumer_reponses(reps2 + reps2b)},
            "extraction": {"moisson_ok": ext1["ok"], "tranches_ok": tranches_ok, "tranches": tranches},
            "synthese_M0": {"statut": synthese.statut, "modele_servi": synthese.modele_servi,
                            "empreinte": synthese.empreinte_texte}, "spectre": spectre})
        if synthese.ok:
            substrat["evolved_architecture_spec"] = (
                str(substrat.get("evolved_architecture_spec", "")) + "\n\n=== SYNTHÈSE (run "
                f"{config.nom_run}, {'à blanc' if config.a_blanc else 'réel'}, non auditée) ===\n\n" + synthese.texte)

        # ---- rapport ----------------------------------------------------------------------------------
        sections = [
            ("Comptes", f"- requêtes formulées : {len(requetes)}\n- entrées externes : {len(entrees)}\n"
                        f"- agents (appels) : {m3.resumer_reponses(toutes_reponses)}\n"
                        f"- blocs LaTeX au tableau de découverte : {len(tableau2.blocs)}\n"
                        f"- analyse spectrale : `{json.dumps(spectre, ensure_ascii=False)}`\n"
                        f"- extraction M1 : moisson {'ok' if ext1['ok'] else 'ÉCHEC'}, découverte {tranches_ok}/{tranches} tranches"),
            ("Requêtes formulées par l'essaim", "\n".join(f"- `{q}`" for q in requetes) or "(aucune)"),
            ("Classes existantes (extraites)", "\n".join(f"{i + 1}. {x}" for i, x in enumerate(
                fusion["existing_eval_awareness_flaws_analyzed_and_solved"])) or "(aucune)"),
            ("Classes nouvelles proposées (extraites, non vérifiées)", "\n".join(f"{i + 1}. {x}" for i, x in enumerate(
                fusion["novel_unprecedented_eval_awareness_flaws_discovered"])) or "(aucune)"),
            ("Concepts et associations proposés (extraits, non vérifiés)", "\n".join(f"{i + 1}. {x}" for i, x in enumerate(
                fusion["novel_mathematical_concepts_and_unprecedented_combinations"])) or "(aucune)"),
            ("Énoncés de résolution (extraits, non vérifiés)", "\n".join(f"- {x}" for x in
                fusion["formal_resolution_theorems_and_operators"]) or "(aucun)"),
            ("Synthèse de l'arbitre (M0)", synthese.texte if synthese.ok else f"(échec : {synthese.statut} {synthese.erreur})"),
        ]
        m3.ecrire_rapport(config.dossier_run / "rapport_decouverte_eval_awareness.md",
                          "Découverte « eval awareness » par essaim — rapport de run (exploratoire)", sections)
        m3.ecrire_json(config.dossier_run / "extraction_m1.json", {"moisson": ext1, "decouverte": fusion})
    except m3.BudgetDepasse as exc:
        arret = f"arrêt sur plafond : {exc}"
        journal.dire("!!! " + arret)
    finally:
        m3.sauver_substrat(config.substrat, substrat)
        m3.sceller(config.journal) if config.journal.exists() else None
        m3.resume_final(config, budget, toutes_reponses, {"arret": arret})
        journal.dire(f"fin ; budget : {budget.etat()} ; sorties dans {config.dossier_run}")
    return 3 if arret else 0


if __name__ == "__main__":
    sys.exit(main())
