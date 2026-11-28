#!/usr/bin/env python3
"""Construction déterministe du supplément littérature, lectures approfondies et séances antérieures (v1).

Complète `corpus-unifie-idees-v1` (sans modifier ce dernier, règle R12) en ingérant sans troncature :
1. Les 7 lectures approfondies sur PDF (`docs/notes/lectures-approfondies-v1/`, dont Buehler 2026 arXiv:2607.20058
   et DiscoveryAgent arXiv:2611.21950) ainsi que `lecture-karkada-buehler-v1.md` ;
2. Les 630 travaux recensés dans `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json` ;
3. Les synthèses et fiches détaillées de veille (`veille-organismes-ideation-v2`, `veille-organismes-ideation-v3`
   incluant « A Society of AI Scientists », `veille-concurrentielle-v1`, `veille-yu-memoire-v1`,
   `veille-voisins-yu-v1`, `veille-spaceship-ram-v1`, `lecture-*.md`) ;
4. Les dossiers d'exploration, de mémoire de conception et de réponses API antérieures
   (`exploration-idees-fable-v1`, `memoire-conception-v1` dont la liste exhaustive du 22 novembre,
   `identites-tenues-pour-vraies-v1`, `demandes-fable-api-2026-11-22-v1` hors pièces séquestrées/attaques,
   `reponses-especes-seules-2026-11-01-v1`) ;
5. Les rapports de lecture de PDF de niveaux 1 et 2 (`docs/sources/lecture-pdf-niveau1` et `niveau2`,
   hors recettes d'évasion/attaque/sabotage).
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SORTIE = Path(__file__).resolve().parent

MOTIFS_INTERDITS = (
    "coffre/",
    "docs/verdicts/",
    "/verdict/",
    "verdict/",
    "reponses-ne-pas-servir",
    "sequestre",
    "protocole-x-attaquant-v1",
    "evasion-moniteurs",
    "evasion-sondes",
    "evasion-quorum",
    "bancs-attaque",
    "sabotage-recherche",
    "injection-etats-internes",
    "suffixes",
    "modes-et-attaques",
    "modes-attaque",
    "modes-v8",
    "organismes-discrets",
    "lot-quarantaine",
    "taches-sabotage",
    "conscience-anesthesie-v3-reserve",
    "verite-dommage",
    "tableau-partage",
    "questions-fortes",
    "bras-attaque",
    "attaque-goodhart",
    "barreau8",
    "barreau5",
    "dose-reponse-consigne-cachee",
    "versant-honnete",
    "sondes-v2",
)


def est_interdit(chemin: str) -> bool:
    c = chemin.replace("\\", "/").lower()
    return any(m in c for m in MOTIFS_INTERDITS)


def sha256_texte(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def nettoyer_espaces(s: str) -> str:
    return re.sub(r"[ \t]+", " ", (s or "").strip())


def classer_objet_et_regime(titre: str, texte: str, chemin: str, nature: str) -> tuple[str, str]:
    t = f"{titre} {texte[:1500]} {chemin}".lower()
    if any(k in t for k in ("open-weight", "gemma", "llama", "8b", "4b", "activations", "lentille", "steering", "pilotage", "dopamine")):
        regime = "GPU_VAST_8B_SOUS_GO"
    elif any(k in t for k in ("pubtator", "gu et krenn", "scimuse", "openalex", "arxiv 2000", "cit-hepth")):
        regime = "CPU_DONNEES_PUBLIQUES_REEL"
    else:
        regime = "CPU_0_USD_SYNTHETIQUE"

    if any(k in t for k in ("materials-science", "buehler", "dopamine", "pubtator", "scimuse", "gu et krenn")):
        obj = "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B"
    elif any(k in t for k in ("hypergraphe", "homomorphisme", "scission", "dreamcoder", "stitch", "macros", "lean", "symétrie", "symmetry", "karkada")):
        obj = "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET"
    elif any(k in t for k in ("sonde", "moniteur", "contrôle", "controle", "audit", "lie detector", "stéganographie", "steganographie")):
        obj = "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES"
    elif any(k in t for k in ("étroitesse", "handicap", "clopper", "juge", "popper", "falsification", "protocole x")):
        obj = "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT"
    else:
        obj = "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION"
    return obj, regime


def construire() -> None:
    entrees: list[dict] = []
    exclus = 0

    def ajouter(
        id_orig: str,
        titre: str,
        enonce_complet: str,
        nature_entree: str,
        famille_source: str,
        auteurs_ou_modele: str,
        source_chemin: str,
        statut_lecture: str,
    ) -> None:
        nonlocal exclus
        if est_interdit(source_chemin) or est_interdit(titre):
            exclus += 1
            return
        titre_c = nettoyer_espaces(titre)
        corps_c = (enonce_complet or "").strip()
        if not titre_c and not corps_c:
            return
        objet, regime = classer_objet_et_regime(titre_c, corps_c, source_chemin, nature_entree)
        cle = sha256_texte(f"{source_chemin}|{id_orig}|{titre_c}|{corps_c[:600]}")[:16]
        entrees.append(
            {
                "id_supplement": f"LIT-{len(entrees)+1:04d}",
                "cle_contenu": cle,
                "id_origine": id_orig,
                "nature_entree": nature_entree,
                "titre": titre_c,
                "enonce_complet": corps_c,
                "objet": objet,
                "famille_source": famille_source,
                "auteurs_ou_modele": nettoyer_espaces(auteurs_ou_modele) or "non_specifie",
                "source_chemin": source_chemin,
                "source_branche": "main",
                "statut_lecture": statut_lecture,
                "regime_execution": regime,
            }
        )

    # 1. Les 630 travaux de table-fusionnee-v1.json
    p_tf = RACINE / "docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json"
    if p_tf.is_file():
        tf = json.loads(p_tf.read_text(encoding="utf-8"))
        for idx, tr in enumerate(tf.get("travaux", []), 1):
            titre = tr.get("titre", "")
            auteurs = tr.get("auteurs", "") or tr.get("nature", "article")
            arxiv = tr.get("arxiv", "")
            adresse = tr.get("adresse", "")
            date_p = tr.get("date", "")
            fait = tr.get("fait", "")
            touche = tr.get("touche", "")
            verdict_adv = tr.get("verdict_adverse", "")
            lu = tr.get("lu", "")
            mesure = tr.get("mesure", "")
            corps = (
                f"Auteurs : {auteurs} | Date : {date_p} | Identifiant : {arxiv} ({adresse})\n"
                f"Statut de lecture : {lu} | Mesure : {mesure}\n"
                f"Ce que fait le papier : {fait}\n"
                f"Points du programme touchés : {touche}\n"
                f"Verdict recherche adverse : {verdict_adv}"
            )
            ajouter(
                f"TF-{idx:04d}",
                titre,
                corps,
                "papier_externe_veille",
                "L01_Table_Fusionnee_630_Travaux_Veille_Exploration",
                str(auteurs),
                "docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json",
                str(lu or "notice_veille"),
            )

    # 2. Lectures approfondies sur PDF (dont Buehler 2607.20058 et DiscoveryAgent 2611.21950) + lecture-karkada-buehler
    for md in sorted((RACINE / "docs/notes/lectures-approfondies-v1").glob("*.md")):
        rel = str(md.relative_to(RACINE))
        txt = md.read_text(encoding="utf-8")
        prem = txt.splitlines()[0].lstrip("#").strip() if txt.splitlines() else md.stem
        ajouter(
            f"LECT-PDF-{md.stem}",
            prem,
            txt,
            "lecture_approfondie_pdf_entier",
            "L02_Lectures_Approfondies_PDF_Complets",
            "Lecture PDF vérifiée du dépôt",
            rel,
            "lu_sur_pdf_entier",
        )

    p_kb = RACINE / "docs/notes/demandes-fable-api-2026-11-22-v1/lecture-karkada-buehler-v1.md"
    if p_kb.is_file():
        txt = p_kb.read_text(encoding="utf-8")
        for sec in re.split(r"(?m)^##\s+", txt)[1:]:
            lignes = sec.splitlines()
            t_sec = lignes[0].strip()
            ajouter(
                f"LECT-KB-{sha256_texte(t_sec)[:6]}",
                t_sec,
                "## " + sec.strip(),
                "lecture_papier_cible",
                "L02_Lectures_Approfondies_PDF_Complets",
                "Agent de lecture (22 nov. 2026)",
                str(p_kb.relative_to(RACINE)),
                "lu_en_html_puis_pdf",
            )

    # 3. Veille organismes d'idéation v3 (dont A Society of AI Scientists) et v2
    p_v3 = RACINE / "docs/notes/veille-organismes-ideation-v3/synthese-v1.md"
    if p_v3.is_file():
        txt = p_v3.read_text(encoding="utf-8")
        rel = str(p_v3.relative_to(RACINE))
        # Extraire à la fois le document complet par sections ET chaque papier numéroté **1. Titre**
        for m in re.finditer(r"(?ms)^\*\*(\d+\.\s+[^*]+)\*\*\s*—\s*(.+?)(?=^\*\*\d+\.\s+|\Z|^##\s+)", txt):
            t_pap = m.group(1).strip()
            c_pap = m.group(0).strip()
            ajouter(
                f"VOI3-PAP-{sha256_texte(t_pap)[:6]}",
                t_pap,
                c_pap,
                "papier_externe_voisin_lu",
                "L03_Veille_Organismes_Ideation_v2_v3",
                "Synthèse veille organismes d'idéation v3",
                rel,
                "lu_et_compare_aux_revendications",
            )
        ajouter(
            "VOI3-SYNTHESE-COMPLETE",
            "Synthèse complète de veille sur les organismes d'idéation (v3)",
            txt,
            "synthese_veille",
            "L03_Veille_Organismes_Ideation_v2_v3",
            "Veille organismes d'idéation v3",
            rel,
            "synthese_complete",
        )

    def ingerer_dossier_md(dossier_rel: str, famille: str, nature_defaut: str, filtre_nom=None) -> None:
        nonlocal exclus
        d = RACINE / dossier_rel
        if not d.exists():
            return
        fichiers = [d] if d.is_file() else sorted(d.rglob("*.md"))
        for md in fichiers:
            rel = str(md.relative_to(RACINE))
            if est_interdit(rel):
                exclus += 1
                continue
            if filtre_nom and not filtre_nom(md):
                continue
            txt = md.read_text(encoding="utf-8")
            if len(txt.strip()) < 80:
                continue
            prem = txt.splitlines()[0].lstrip("#").strip() if txt.splitlines() else md.stem
            # Découper en sections ## si le fichier dépasse 4 000 caractères afin de garder chaque idée/papier granulaire ET complet
            if len(txt) <= 4500:
                ajouter(
                    f"DOC-{sha256_texte(rel)[:8]}",
                    f"{md.stem} — {prem[:180]}",
                    txt,
                    nature_defaut,
                    famille,
                    dossier_rel,
                    rel,
                    "texte_integral",
                )
            else:
                blocs = re.split(r"(?m)^(#{2}\s+.+)$", txt)
                entete = blocs[0].strip()
                if len(entete) >= 120:
                    ajouter(
                        f"ENT-{sha256_texte(rel)[:8]}",
                        f"{md.stem} — En-tête et synthèse ({prem[:140]})",
                        entete,
                        nature_defaut,
                        famille,
                        dossier_rel,
                        rel,
                        "section_integrale",
                    )
                for i in range(1, len(blocs), 2):
                    st = blocs[i].lstrip("#").strip()
                    sc = (blocs[i] + "\n" + (blocs[i + 1] if i + 1 < len(blocs) else "")).strip()
                    if len(sc) < 80:
                        continue
                    ajouter(
                        f"SEC-{sha256_texte(rel + st)[:8]}",
                        f"{md.stem} — {st[:180]}",
                        sc,
                        nature_defaut,
                        famille,
                        dossier_rel,
                        rel,
                        "section_integrale",
                    )

    ingerer_dossier_md("docs/notes/veille-organismes-ideation-v2", "L03_Veille_Organismes_Ideation_v2_v3", "lecture_voisin_et_veille")
    ingerer_dossier_md("docs/notes/veille-concurrentielle-v1", "L04_Autres_Veilles_Yu_Spaceship_Concurrents", "veille_concurrentielle")
    ingerer_dossier_md("docs/notes/veille-yu-memoire-v1", "L04_Autres_Veilles_Yu_Spaceship_Concurrents", "lecture_voisin_memoire")
    ingerer_dossier_md("docs/notes/veille-voisins-yu-v1", "L04_Autres_Veilles_Yu_Spaceship_Concurrents", "lecture_voisin_memoire")
    ingerer_dossier_md("docs/notes/veille-spaceship-ram-v1", "L04_Autres_Veilles_Yu_Spaceship_Concurrents", "lecture_voisin_memoire")
    ingerer_dossier_md("docs/notes/exploration-idees-fable-v1", "L05_Exploration_Idees_Fable_et_Releve_Arxiv", "exploration_et_lecture_fable")
    ingerer_dossier_md("docs/notes/memoire-conception-v1", "L06_Memoire_Conception_21_22_Novembre", "synthese_hypotheses_et_memoire")
    ingerer_dossier_md("docs/notes/identites-tenues-pour-vraies-v1", "L07_Identites_Sommeil_Bisociation_Especes", "piste_directeur_et_mere")
    ingerer_dossier_md("docs/notes/demande-sommeil-consolidation-v1", "L07_Identites_Sommeil_Bisociation_Especes", "piste_sommeil_consolidation")
    ingerer_dossier_md("docs/notes/bisociation-litterature-reelle-v1", "L07_Identites_Sommeil_Bisociation_Especes", "bisociation_litterature")
    ingerer_dossier_md("docs/notes/reponses-especes-seules-2026-11-01-v1", "L07_Identites_Sommeil_Bisociation_Especes", "reponse_modele_seul_novembre")
    ingerer_dossier_md(
        "docs/notes/demandes-fable-api-2026-11-22-v1",
        "L08_Demandes_et_40_Reponses_API_22_Novembre",
        "reponse_modele_api_22_novembre",
        filtre_nom=lambda p: ("reponse" in str(p) or "synthese" in p.name or "demande-" in p.name),
    )
    ingerer_dossier_md("docs/sources/lecture-pdf-niveau1", "L09_Rapports_Lecture_PDF_Niveaux_1_et_2", "rapport_lecture_pdf_niveau1")
    ingerer_dossier_md("docs/sources/lecture-pdf-niveau2", "L09_Rapports_Lecture_PDF_Niveaux_1_et_2", "rapport_lecture_pdf_niveau2")

    for md_solo in sorted((RACINE / "docs/notes").glob("lecture-*.md")):
        ingerer_dossier_md(str(md_solo.relative_to(RACINE)), "L09_Rapports_Lecture_PDF_Niveaux_1_et_2", "lecture_voisin_cible")

    # Dédoublonnage exact sur cle_contenu
    vues: set[str] = set()
    uniques: list[dict] = []
    for e in entrees:
        if e["cle_contenu"] in vues:
            continue
        vues.add(e["cle_contenu"])
        e["id_supplement"] = f"LIT-{len(uniques)+1:04d}"
        uniques.append(e)

    p_jsonl = SORTIE / "supplement-litterature-et-lectures-v1.jsonl"
    p_jsonl.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in uniques) + "\n", encoding="utf-8")

    c_fam = Counter(e["famille_source"] for e in uniques)
    c_nat = Counter(e["nature_entree"] for e in uniques)
    c_obj = Counter(e["objet"] for e in uniques)

    manifeste = {
        "version": "v1",
        "total_entrees_uniques_sans_troncature": len(uniques),
        "exclus_par_liste_noire_cloisonnement_et_sequestre": exclus,
        "par_famille_source": dict(sorted(c_fam.items())),
        "par_nature_entree": dict(sorted(c_nat.items())),
        "par_objet": dict(sorted(c_obj.items())),
    }
    (SORTIE / "manifeste-supplement-litterature-v1.json").write_text(
        json.dumps(manifeste, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lignes_md = [
        "# Supplément Littérature, Lectures approfondies de PDF et Séances antérieures (v1)",
        "",
        "Complément scellé sans troncature à `corpus-unifie-idees-v1` (règle R12 : `v1` intact), couvrant l'intégralité des papiers externes lus ou recensés par la veille ainsi que les synthèses et réponses de modèles des 1er et 21-22 novembre.",
        "",
        f"- **Entrées complètes dédoublonnées** : **{len(uniques)}** (`LIT-0001` à `LIT-{len(uniques):04d}`)",
        f"- **Pièces filtrées par la liste noire de cloisonnement / séquestre** : **{exclus}**",
        "",
        "## Répartition par gisement ingéré",
        "",
        "| Gisement | Nombre d'entrées intégrales |",
        "|---|---:|",
    ]
    for fam, nb in sorted(c_fam.items()):
        lignes_md.append(f"| `{fam}` | **{nb}** |")
    lignes_md.append("")
    (SORTIE / "LISEZMOI-SUPPLEMENT-LITTERATURE-v1.md").write_text("\n".join(lignes_md), encoding="utf-8")
    print(f"OK : {len(uniques)} entrées écrites dans {p_jsonl.name} ({exclus} filtrées).")


if __name__ == "__main__":
    construire()
