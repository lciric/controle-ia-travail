#!/usr/bin/env python3
"""Assemble catalogue-canonique-v2/ de facon purement incrementale (v1 intact + supplement LIT-0001..2863)."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(r"C:\Users\lciri\wt-organisme-boucle-fermee")
V1_DIR = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v1"
V2_DIR = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v2"
V2_RAYONS = V2_DIR / "rayons"
V2_RAYONS.mkdir(parents=True, exist_ok=True)
V2_SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch\v2_lit")

EMOJI_RE = re.compile("[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+")

OBJETS_META = {
    "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT": (
        "Objet 1 : Metrologie, attelage du Plan Turing, criteres sans juge et tests de mort",
        "01-metrologie-attelage-et-tests-de-mort.md",
    ),
    "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION": (
        "Objet 2 : Architecture de l'organisme d'ideation, memoire negative, selection et auto-conception",
        "02-architecture-organisme-memoire-et-autoconception.md",
    ),
    "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET": (
        "Objet 3 : Mathematiques nouvelles, modele a trois graphes, reification hors alphabet et Lean 4",
        "03-mathematiques-nouvelles-3-graphes-et-hors-alphabet.md",
    ),
    "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES": (
        "Objet 4 : Controle de l'intelligence artificielle, menaces diffuses, audit et sondes internes",
        "04-controle-ia-menaces-diffuses-et-sondes.md",
    ),
    "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B": (
        "Objet 5 : Etalonnages empiriques sur corpus reels dates (PubTator 3, Gu et Krenn, cit-HepTh) et GPU 8B (dopamine H10, compression T4)",
        "05-etalonnages-corpus-reels-et-gpu-8b.md",
    ),
}
VALID_OBJETS = set(OBJETS_META.keys())
VALID_STATUTS = {"vierge", "preenregistre_en_attente", "pris_en_charge_groupe_v1", "deja_valide_interne", "deja_refute_interne"}
VALID_REGIMES = {"CPU_0_USD_SYNTHETIQUE", "CPU_DONNEES_PUBLIQUES_REEL", "GPU_VAST_8B_SOUS_GO", "MODELE_FERME_COURSE_ETAPE_2"}


def strip_emoji(s: str) -> str:
    return EMOJI_RE.sub("", str(s or "")).strip()


def load_jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def build_lit_genealogie(lit_ids: list[str], lit_master: dict[str, dict]) -> list[dict]:
    out = []
    for lid in sorted(set(lit_ids)):
        raw = lit_master[lid]
        en = raw.get("enonce_complet", "")
        ref_m = re.search(r"(https?://[^\s\)\],;]+|arxiv[:\s]*\d{4}\.\d{4,5}(?:v\d+)?)", en, re.I)
        ref_url = ref_m.group(1) if ref_m else ""
        out.append({
            "id_bib": lid,
            "id_origine": strip_emoji(raw.get("id_origine", "")),
            "auteur_ou_modele": strip_emoji(raw.get("auteurs_ou_modele", "")) or "Litterature / veille",
            "famille_source": strip_emoji(raw.get("famille_source", "")),
            "source_chemin": strip_emoji(raw.get("source_chemin", "")).replace("\\", "/"),
            "source_branche": strip_emoji(raw.get("source_branche", "main")),
            "reference_arxiv_ou_url": ref_url,
        })
    return out


def categorie_modele_croise_v2(auteur: str, fam: str) -> str:
    a = (auteur or "").lower()
    f = (fam or "").lower()
    if f.startswith("l01_") or f.startswith("l02_") or f.startswith("l03_") or f.startswith("l04_") or f.startswith("l09_"):
        return "Litterature externe et lectures PDF (v2)"
    if "lazar" in a or "directeur" in a:
        return "Lazar (directeur)"
    if "fable 5.2" in a or ("fable" in a and "5.1" not in a):
        return "Fable 5.2"
    if "fable 5.1" in a:
        return "Fable 5.1"
    if "opus" in a:
        return "Opus 5.5"
    if "carbon" in a:
        return "Carbon"
    if "neon" in a:
        return "Neon"
    if "argon" in a:
        return "Argon"
    if "astra" in a:
        return "Astra"
    if "kimi" in a:
        return "Kimi"
    if "veille arxiv" in a or "veille litterature" in a:
        return "Litterature externe et lectures PDF (v2)"
    if "collisionneur" in a:
        return "Collisionneurs multi-modeles"
    return "Syntheses internes et registres"


def main() -> None:
    lit_master = {r["id_supplement"]: r for r in load_jsonl(V2_SCRATCH / "supplement-litterature-et-lectures-v1.jsonl")}
    agg = json.loads((V2_SCRATCH / "v2_lit_aggregated.json").read_text(encoding="utf-8"))
    dec_path = V2_SCRATCH / "v2_conservator_decisions.json"
    dec = json.loads(dec_path.read_text(encoding="utf-8")) if dec_path.is_file() else {}

    # 1. Charger les 4 registres de v1 SANS les modifier sur disque
    v1_idees = load_jsonl(V1_DIR / "idees-et-mecanismes-canoniques.jsonl")
    v1_acquis = load_jsonl(V1_DIR / "acquis-empiriques-et-morts-connus.jsonl")
    v1_outils = load_jsonl(V1_DIR / "outils-bancs-et-corpus.jsonl")
    v1_ecarts = load_jsonl(V1_DIR / "ecartes-structurels-et-glossaires.jsonl")

    # Initialiser v2 idees a partir de v1 (en preservant les IDEE-CANON-xxxx existants !)
    v2_idees_map: dict[str, dict] = {}
    for it in v1_idees:
        rec = dict(it)
        ant_old = strip_emoji(rec.get("anteriorite_connue", ""))
        rec["anteriorite_et_voisins_a_citer"] = ant_old
        # Determiner origine_type initial de v1
        has_arxiv = any("veille arxiv" in g.get("auteur_ou_modele", "").lower() or "veille litterature" in g.get("auteur_ou_modele", "").lower() for g in rec.get("genealogie_sources", []))
        has_int = any("veille arxiv" not in g.get("auteur_ou_modele", "").lower() and "veille litterature" not in g.get("auteur_ou_modele", "").lower() for g in rec.get("genealogie_sources", []))
        if has_arxiv and has_int:
            rec["origine_type"] = "hybride_interne_et_voisin"
        elif has_arxiv and not has_int:
            rec["origine_type"] = "emprunt_litterature_a_citer"
        else:
            rec["origine_type"] = "interne_programme"
        v2_idees_map[rec["id_canonique"]] = rec

    # 2. Registre 5 : litterature-et-voisins-lus.jsonl
    papers_sorted = sorted(
        agg["papers"],
        key=lambda p: (0 if p.get("statut_lecture") == "lu_sur_pdf_entier" else 1, p.get("objet", ""), p.get("theme", ""), p.get("titre_clair_fr", "").lower()),
    )
    final_papers = []
    temp_pap_to_id = {}
    for idx, p in enumerate(papers_sorted, 1):
        pid = f"LIT-PAPIER-{idx:04d}"
        temp_pap_to_id[p["temp_lit_id"]] = pid
        final_papers.append({
            "id_papier": pid,
            "titre_clair_fr": strip_emoji(p.get("titre_clair_fr", "")),
            "titre_original": strip_emoji(p.get("titre_original", "")),
            "auteurs": strip_emoji(p.get("auteurs", "")),
            "identifiant_arxiv_ou_doi": strip_emoji(p.get("identifiant_arxiv_ou_doi", "")),
            "date_publication": strip_emoji(p.get("date_publication", "")),
            "statut_lecture": "lu_sur_pdf_entier" if p.get("statut_lecture") == "lu_sur_pdf_entier" else "lu_sur_resume",
            "objet": p["objet"] if p.get("objet") in VALID_OBJETS else "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
            "theme": strip_emoji(p.get("theme", "")),
            "dispositif": strip_emoji(p.get("dispositif", "")),
            "chiffres_cles": strip_emoji(p.get("chiffres_cles", "")),
            "echecs_et_limites_temoins_negatifs": strip_emoji(p.get("echecs_et_limites_temoins_negatifs", "")),
            "lien_avec_nos_revendications": strip_emoji(p.get("lien_avec_nos_revendications", "")),
            "genealogie_sources": build_lit_genealogie(p["lit_ids"], lit_master),
        })

    # Enrichir automatiquement les fiches v1 avec les papiers externes tres proches (sim >= 0.34)
    pap_by_id = {p["id_papier"]: p for p in final_papers}
    for lnk in agg.get("paper_v1_links_auto") or []:
        pid = temp_pap_to_id.get(lnk["temp_lit_id"])
        if not pid:
            continue
        p = pap_by_id[pid]
        citation_str = f"{p['titre_original']} ({p['auteurs']}, {p['identifiant_arxiv_ou_doi']}, {pid}, {p['statut_lecture']})"
        for m in lnk.get("v1_matches") or []:
            if m["sim"] >= 0.35 and m["v1_id"] in v2_idees_map:
                rec = v2_idees_map[m["v1_id"]]
                if pid not in rec["anteriorite_et_voisins_a_citer"]:
                    base_ant = rec["anteriorite_et_voisins_a_citer"]
                    if "Aucune anteriorite" in base_ant:
                        rec["anteriorite_et_voisins_a_citer"] = citation_str
                    else:
                        rec["anteriorite_et_voisins_a_citer"] = f"{base_ant} ; {citation_str}".strip(" ;")
                    rec["anteriorite_connue"] = rec["anteriorite_et_voisins_a_citer"]
                    if rec["origine_type"] == "interne_programme":
                        rec["origine_type"] = "hybride_interne_et_voisin"

    # 3. Appliquer les fusions intra-LIT et rattachements a v1 decides par le conservateur v2
    cand_map = {x["temp_id"]: dict(x) for x in agg["cand_idees"]}
    redirect = {}

    def resolve(tid: str) -> str:
        seen = set()
        while tid in redirect and tid not in seen:
            seen.add(tid)
            tid = redirect[tid]
        return tid

    for m in dec.get("intra_lit_merges") or []:
        keep = resolve(str(m.get("keep_id", "")))
        if keep not in cand_map:
            continue
        for mid_raw in m.get("merge_ids") or []:
            mid = resolve(str(mid_raw))
            if mid == keep or mid not in cand_map:
                continue
            other = cand_map.pop(mid)
            redirect[mid] = keep
            cand_map[keep]["lit_ids"] = list(dict.fromkeys(cand_map[keep]["lit_ids"] + other["lit_ids"]))
            if other.get("anteriorite_et_voisins_a_citer") and other["anteriorite_et_voisins_a_citer"] not in cand_map[keep].get("anteriorite_et_voisins_a_citer", ""):
                cand_map[keep]["anteriorite_et_voisins_a_citer"] = f"{cand_map[keep].get('anteriorite_et_voisins_a_citer','')} ; {other['anteriorite_et_voisins_a_citer']}".strip(" ;")

    # Rattachements aux fiches IDEE-CANON-xxxx existantes de v1
    attached_count = 0
    for att in dec.get("attach_to_v1") or []:
        tid = resolve(str(att.get("temp_id", "")))
        v1_id = str(att.get("v1_id", ""))
        if tid not in cand_map or v1_id not in v2_idees_map:
            continue
        other = cand_map.pop(tid)
        rec = v2_idees_map[v1_id]
        # Ajouter la genealogie LIT sans doublon
        existing_bibs = {g["id_bib"] for g in rec["genealogie_sources"]}
        for g in build_lit_genealogie(other["lit_ids"], lit_master):
            if g["id_bib"] not in existing_bibs:
                rec["genealogie_sources"].append(g)
                existing_bibs.add(g["id_bib"])
        note_voisin = strip_emoji(att.get("voisin_a_citer") or other.get("anteriorite_et_voisins_a_citer") or other.get("titre_clair_fr", ""))
        if note_voisin and note_voisin not in rec["anteriorite_et_voisins_a_citer"]:
            if "Aucune anteriorite" in rec["anteriorite_et_voisins_a_citer"]:
                rec["anteriorite_et_voisins_a_citer"] = note_voisin
            else:
                rec["anteriorite_et_voisins_a_citer"] = f"{rec['anteriorite_et_voisins_a_citer']} ; {note_voisin}".strip(" ;")
            rec["anteriorite_connue"] = rec["anteriorite_et_voisins_a_citer"]
        if att.get("set_hybride", True) and other.get("origine_type") in ("emprunt_litterature_a_citer", "hybride_interne_et_voisin"):
            rec["origine_type"] = "hybride_interne_et_voisin"
        attached_count += 1

    # Ajouter les nouvelles idees canoniques (IDEE-CANON-(K_v1+1)..K_v2)
    next_idee_num = len(v1_idees) + 1
    new_idees_sorted = sorted(
        cand_map.values(),
        key=lambda x: (x.get("objet", ""), x.get("theme", ""), x.get("sous_theme", ""), x.get("titre_clair_fr", "").lower()),
    )
    new_idees_added = []
    for it in new_idees_sorted:
        cid = f"IDEE-CANON-{next_idee_num:04d}"
        next_idee_num += 1
        ant = strip_emoji(it.get("anteriorite_et_voisins_a_citer", "")) or "Source externe ou seance de novembre (voir genealogie_sources)."
        rec = {
            "id_canonique": cid,
            "titre_clair_fr": strip_emoji(it.get("titre_clair_fr", "")),
            "objet": it["objet"] if it.get("objet") in VALID_OBJETS else "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
            "theme": strip_emoji(it.get("theme", "")),
            "sous_theme": strip_emoji(it.get("sous_theme", "")) or "Apport litterature et seances novembre",
            "enonce_complet": strip_emoji(it.get("enonce_complet", "")),
            "mecanisme_causal": strip_emoji(it.get("mecanisme_causal", "")),
            "genealogie_sources": build_lit_genealogie(it["lit_ids"], lit_master),
            "anteriorite_connue": ant,
            "anteriorite_et_voisins_a_citer": ant,
            "origine_type": it.get("origine_type") if it.get("origine_type") in ("emprunt_litterature_a_citer", "interne_programme", "hybride_interne_et_voisin") else "emprunt_litterature_a_citer",
            "statut_epistemique": it["statut_epistemique"] if it.get("statut_epistemique") in VALID_STATUTS else "vierge",
            "regime_materiel": it["regime_materiel"] if it.get("regime_materiel") in VALID_REGIMES else "CPU_0_USD_SYNTHETIQUE",
            "esquisse_test_de_mort_et_faux_temoin": strip_emoji(it.get("esquisse_test_de_mort_et_faux_temoin", "")),
        }
        v2_idees_map[cid] = rec
        new_idees_added.append(rec)

    final_idees = [v2_idees_map[k] for k in sorted(v2_idees_map.keys())]

    # 4. Acquis, outils, ecarts : v1 intact + ajouts LIT numerotes a la suite
    final_acquis = list(v1_acquis)
    n_acq = len(final_acquis)
    for it in agg["cand_acquis"]:
        n_acq += 1
        final_acquis.append({
            "id_acquis": f"ACQUIS-{n_acq:04d}",
            "titre_clair_fr": strip_emoji(it.get("titre_clair_fr", "")),
            "objet": it["objet"] if it.get("objet") in VALID_OBJETS else "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
            "theme": strip_emoji(it.get("theme", "")),
            "type_acquis": strip_emoji(it.get("type_acquis", "")) or "constat_tranche",
            "enonce_complet": strip_emoji(it.get("enonce_complet", "")),
            "motif_ou_resultat": strip_emoji(it.get("motif_ou_resultat", "")),
            "genealogie_sources": build_lit_genealogie(it["lit_ids"], lit_master),
        })

    final_outils = list(v1_outils)
    n_out = len(final_outils)
    for it in agg["cand_outils"]:
        n_out += 1
        final_outils.append({
            "id_outil": f"OUTIL-{n_out:04d}",
            "titre_clair_fr": strip_emoji(it.get("titre_clair_fr", "")),
            "objet": it["objet"] if it.get("objet") in VALID_OBJETS else "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
            "theme": strip_emoji(it.get("theme", "")),
            "type_outil": strip_emoji(it.get("type_outil", "")) or "banc_experimental",
            "description_complete": strip_emoji(it.get("description_complete", "")),
            "genealogie_sources": build_lit_genealogie(it["lit_ids"], lit_master),
        })

    final_ecarts = list(v1_ecarts)
    n_eca = len(final_ecarts)
    for it in agg["cand_ecarts"]:
        n_eca += 1
        final_ecarts.append({
            "id_ecart": f"ECART-{n_eca:04d}",
            "motif_ecart": strip_emoji(it.get("motif_ecart", "")) or "Entree structurelle supplement litterature",
            "resume_court": strip_emoji(it.get("resume_court", "")),
            "genealogie_sources": build_lit_genealogie(it["lit_ids"], lit_master),
        })

    # 5. Ecrire les 5 registres .jsonl dans catalogue-canonique-v2/
    (V2_DIR / "idees-et-mecanismes-canoniques.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in final_idees) + "\n", encoding="utf-8")
    (V2_DIR / "litterature-et-voisins-lus.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in final_papers) + "\n", encoding="utf-8")
    (V2_DIR / "acquis-empiriques-et-morts-connus.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in final_acquis) + "\n", encoding="utf-8")
    (V2_DIR / "outils-bancs-et-corpus.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in final_outils) + "\n", encoding="utf-8")
    (V2_DIR / "ecartes-structurels-et-glossaires.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in final_ecarts) + "\n", encoding="utf-8")

    # 6. Generer litterature-et-voisins-lus.md & CATALOGUE-LITTERATURE-ET-VOISINS-PAR-THEME-v2.md
    n_pdf = sum(1 for p in final_papers if p["statut_lecture"] == "lu_sur_pdf_entier")
    n_res = len(final_papers) - n_pdf
    lit_md = [
        "# Registre de la litterature externe et des voisins lus (version 2)",
        "",
        f"Ce registre rassemble **{len(final_papers)} travaux externes distincts** (dont **{n_pdf} lus sur PDF ou texte entier** et **{n_res} lus sur resume/notice**), avec leurs auteurs, identifiants arXiv/DOI, dispositifs, chiffres cles, limites utiles comme temoins negatifs et liens avec nos revendications.",
        "",
    ]
    cat_lit = [
        "# Catalogue de la litterature externe et des voisins par Objet et par Theme (version 2)",
        "",
        f"Vue thematique de **{len(final_papers)} papiers externes** (`lu_sur_pdf_entier` : **{n_pdf}** ; `lu_sur_resume` : **{n_res}**).",
        "",
    ]
    pap_by_obj = defaultdict(lambda: defaultdict(list))
    for p in final_papers:
        pap_by_obj[p["objet"]][p["theme"]].append(p)

    for obj_key, (obj_label, _) in OBJETS_META.items():
        n_o = sum(len(v) for v in pap_by_obj[obj_key].values())
        lit_md.append(f"## {obj_label} ({n_o} travaux)")
        lit_md.append("")
        cat_lit.append(f"## {obj_label} ({n_o} travaux)")
        cat_lit.append("")
        for th in sorted(pap_by_obj[obj_key]):
            items = pap_by_obj[obj_key][th]
            lit_md.append(f"### {th} ({len(items)} travaux)")
            lit_md.append("")
            cat_lit.append(f"### {th} ({len(items)} travaux)")
            cat_lit.append("")
            cat_lit.append("| ID papier | Titre en clair | Auteurs | arXiv / DOI | Statut lecture | Lien avec nos revendications |")
            cat_lit.append("|---|---|---|---|---|---|")
            for p in items:
                lids = ", ".join(g["id_bib"] for g in p["genealogie_sources"])
                lit_md.append(f"#### {p['titre_clair_fr']} ({p['id_papier']})")
                lit_md.append(f"- **Titre original** : {p['titre_original']} | **Auteurs** : {p['auteurs']} | **Date** : {p['date_publication']} | **Identifiant** : `{p['identifiant_arxiv_ou_doi']}` | **Statut de lecture** : `{p['statut_lecture']}`")
                lit_md.append(f"- **Dispositif** : {p['dispositif']}")
                lit_md.append(f"- **Chiffres cles** : {p['chiffres_cles']}")
                lit_md.append(f"- **Echecs et limites (temoins negatifs utiles)** : {p['echecs_et_limites_temoins_negatifs']}")
                lit_md.append(f"- **Lien avec nos revendications** : {p['lien_avec_nos_revendications']}")
                lit_md.append(f"- **Occurrences supplement (`LIT`)** : `{lids}`")
                lit_md.append("")
                cat_lit.append(
                    f"| `{p['id_papier']}` | {p['titre_clair_fr'].replace('|','/')} | {p['auteurs'].replace('|','/')[:60]} | `{p['identifiant_arxiv_ou_doi'].replace('|','/')[:40]}` | `{p['statut_lecture']}` | {p['lien_avec_nos_revendications'].replace('|','/')[:140]} |"
                )
            cat_lit.append("")
    (V2_DIR / "litterature-et-voisins-lus.md").write_text("\n".join(lit_md), encoding="utf-8")
    (V2_DIR / "CATALOGUE-LITTERATURE-ET-VOISINS-PAR-THEME-v2.md").write_text("\n".join(cat_lit), encoding="utf-8")

    # 7. Acquis & Outils MD v2
    for fname, title_h, rows, id_k, body_k in (
        ("acquis-empiriques-et-morts-connus.md", "Acquis empiriques, theoremes prouves et pistes deja refutees (v2)", final_acquis, "id_acquis", "enonce_complet"),
        ("outils-bancs-et-corpus.md", "Outils, bancs experimentaux, scripts et corpus publics (v2)", final_outils, "id_outil", "description_complete"),
    ):
        md = [f"# {title_h}", "", f"Total : **{len(rows)} fiches**.", ""]
        by_o = defaultdict(list)
        for r in rows:
            by_o[r["objet"]].append(r)
        for obj_key, (obj_label, _) in OBJETS_META.items():
            lst = by_o[obj_key]
            md.append(f"## {obj_label} ({len(lst)} fiches)")
            md.append("")
            for r in lst:
                bibs = ", ".join(g["id_bib"] for g in r["genealogie_sources"])
                md.append(f"### {r['titre_clair_fr']} ({r[id_k]})")
                md.append(f"- **Theme** : {r['theme']}")
                md.append(f"- **Description** : {r[body_k]}")
                if r.get("motif_ou_resultat"):
                    md.append(f"- **Resultat ou motif** : {r['motif_ou_resultat']}")
                md.append(f"- **Occurrences ({len(r['genealogie_sources'])})** : `{bibs}`")
                md.append("")
        (V2_DIR / fname).write_text("\n".join(md), encoding="utf-8")

    # 8. Les 5 rayons complets sans troncature v2
    idees_by_obj = defaultdict(list)
    for x in final_idees:
        idees_by_obj[x["objet"]].append(x)

    for obj_key, (obj_label, filename) in OBJETS_META.items():
        lst = idees_by_obj[obj_key]
        rmd = [
            f"# {obj_label} (version 2 enrichie litterature)",
            "",
            f"Ce rayon rassemble **{len(lst)} fiches canoniques** (fusionnant **{sum(len(x['genealogie_sources']) for x in lst)} occurrences brutes**) sans aucune troncature.",
            "",
        ]
        by_th = defaultdict(lambda: defaultdict(list))
        for x in lst:
            by_th[x["theme"]][x["sous_theme"]].append(x)
        for th in sorted(by_th):
            n_th = sum(len(v) for v in by_th[th].values())
            rmd.append(f"## {th} ({n_th} fiches canoniques)")
            rmd.append("")
            for st in sorted(by_th[th]):
                rmd.append(f"### Sous-theme : {st} ({len(by_th[th][st])} fiches)")
                rmd.append("")
                for x in by_th[th][st]:
                    rmd.append(f"#### {x['titre_clair_fr']} ({x['id_canonique']})")
                    rmd.append("")
                    rmd.append(f"- **Origine** : `{x['origine_type']}` | **Statut epistemique** : `{x['statut_epistemique']}` | **Regime materiel** : `{x['regime_materiel']}` | **Occurrences** : **{len(x['genealogie_sources'])}**")
                    rmd.append(f"- **Enonce complet** : {x['enonce_complet']}")
                    rmd.append(f"- **Mecanisme causal** : {x['mecanisme_causal']}")
                    rmd.append(f"- **Anteriorite et voisins a citer** : {x['anteriorite_et_voisins_a_citer']}")
                    rmd.append(f"- **Esquisse de test de mort et faux temoin (1b)** : {x['esquisse_test_de_mort_et_faux_temoin']}")
                    rmd.append("- **Genealogie complete des sources** :")
                    for g in x["genealogie_sources"]:
                        ref_p = f" | Ref : {g['reference_arxiv_ou_url']}" if g.get("reference_arxiv_ou_url") else ""
                        rmd.append(f"  - `{g['id_bib']}` (`{g['id_origine']}`) — **{g['auteur_ou_modele']}** | `{g['famille_source']}` | `{g['source_branche']}:{g['source_chemin']}`{ref_p}")
                    rmd.append("")
        (V2_RAYONS / filename).write_text("\n".join(rmd), encoding="utf-8")

    # 9. CATALOGUE-GENERAL-PAR-SUJET-ET-THEME-v2.md
    c_orig = Counter(x["origine_type"] for x in final_idees)
    cat_gen = [
        "# Catalogue general de la Bibliotheque scientifique canonique par sujet, theme et sous-theme (version 2)",
        "",
        f"Fusion incrementale de `catalogue-canonique-v1` ({len(v1_idees)} fiches v1 conservees) et du supplement litterature/PDF `LIT-0001..2863` : **{len(final_idees)} fiches canoniques** (`interne_programme`: **{c_orig['interne_programme']}**, `hybride_interne_et_voisin`: **{c_orig['hybride_interne_et_voisin']}**, `emprunt_litterature_a_citer`: **{c_orig['emprunt_litterature_a_citer']}**), plus **{len(final_papers)} papiers externes** dans `litterature-et-voisins-lus.jsonl`.",
        "",
        "| Objet scientifique | Fiches canoniques v2 | Rayon complet |",
        "|---|---:|---|",
    ]
    for obj_key, (obj_label, filename) in OBJETS_META.items():
        cat_gen.append(f"| {obj_label} | **{len(idees_by_obj[obj_key])}** | `rayons/{filename}` |")
    cat_gen.append("")
    for obj_key, (obj_label, filename) in OBJETS_META.items():
        lst = idees_by_obj[obj_key]
        cat_gen.append(f"## {obj_label} ({len(lst)} fiches)")
        cat_gen.append("")
        by_th = defaultdict(lambda: defaultdict(list))
        for x in lst:
            by_th[x["theme"]][x["sous_theme"]].append(x)
        for th in sorted(by_th):
            cat_gen.append(f"### {th}")
            cat_gen.append("")
            for st in sorted(by_th[th]):
                cat_gen.append(f"#### {st}")
                cat_gen.append("")
                cat_gen.append("| ID canonique | Titre scientifique en clair | Origine | Statut | Regime | Occurrences |")
                cat_gen.append("|---|---|---|---|---|---:|")
                for x in by_th[th][st]:
                    cat_gen.append(f"| `{x['id_canonique']}` | {x['titre_clair_fr'].replace('|','/')} | `{x['origine_type']}` | `{x['statut_epistemique']}` | `{x['regime_materiel']}` | {len(x['genealogie_sources'])} |")
                cat_gen.append("")
    (V2_DIR / "CATALOGUE-GENERAL-PAR-SUJET-ET-THEME-v2.md").write_text("\n".join(cat_gen), encoding="utf-8")

    # 10. CATALOGUE-CROISE-PAR-SOURCE-ET-MODELE-v2.md
    mod_tot, mod_ex, mod_co = defaultdict(list), defaultdict(list), defaultdict(list)
    for x in final_idees:
        mods = sorted(set(categorie_modele_croise_v2(g["auteur_ou_modele"], g["famille_source"]) for g in x["genealogie_sources"]))
        for m in mods:
            mod_tot[m].append(x)
            (mod_ex[m] if len(mods) == 1 else mod_co[m]).append(x)

    croise = [
        "# Catalogue croise par source, modele et litterature externe (version 2)",
        "",
        "Vue croisee distinguant les idees exclusives, co-inventees et hybrides (interne + voisin publie) sur l'union complete `v1 + LIT-0001..2863`.",
        "",
    ]
    if dec.get("synthese_v2_editoriale"):
        croise += ["## Synthese du conservateur v2", "", strip_emoji(dec["synthese_v2_editoriale"]), ""]
    croise += [
        "## 1. Repartition par origine epistemique",
        "",
        "| Origine (`origine_type`) | Nombre d'idees canoniques |",
        "|---|---:|",
        f"| `interne_programme` | **{c_orig['interne_programme']}** |",
        f"| `hybride_interne_et_voisin` | **{c_orig['hybride_interne_et_voisin']}** |",
        f"| `emprunt_litterature_a_citer` (GO-2026-11-19-83) | **{c_orig['emprunt_litterature_a_citer']}** |",
        "",
        "## 2. Repartition par auteur / modele / litterature",
        "",
        "| Source / Modele | Idees totales | Exclusives | Co-inventees / hybrides | Part exclusive |",
        "|---|---:|---:|---:|---:|",
    ]
    for m in sorted(mod_tot, key=lambda k: -len(mod_tot[k])):
        t, e, c = len(mod_tot[m]), len(mod_ex[m]), len(mod_co[m])
        croise.append(f"| {m} | **{t}** | **{e}** | {c} | {100.0*e/t:.1f} % |")
    croise += ["", "## 3. Detail des apports exclusifs et hybrides par source", ""]
    for m in sorted(mod_tot, key=lambda k: -len(mod_tot[k])):
        croise.append(f"### {m} ({len(mod_tot[m])} idees : {len(mod_ex[m])} exclusives, {len(mod_co[m])} partagees)")
        croise.append("")
        for x in mod_ex[m]:
            croise.append(f"- [Exclusive] `{x['id_canonique']}` — **{x['titre_clair_fr']}** (`{x['origine_type']}`, `{x['statut_epistemique']}`)")
        for x in mod_co[m]:
            croise.append(f"- [Partagee, {len(x['genealogie_sources'])} occ.] `{x['id_canonique']}` — **{x['titre_clair_fr']}** (`{x['origine_type']}`)")
        croise.append("")
    (V2_DIR / "CATALOGUE-CROISE-PAR-SOURCE-ET-MODELE-v2.md").write_text("\n".join(croise), encoding="utf-8")

    # 11. LISEZMOI-BIBLIOTHEQUE-CANONIQUE-v2.md
    lisez = [
        "# Bibliotheque scientifique canonique du programme — version 2 (incrementale avec litterature et lectures PDF)",
        "",
        "Construite de facon purement incrementale sous `GO-2026-11-25-06` et la regle `R12` (`catalogue-canonique-v1/` intact, aucun recalcul de `BIB-0001..7007`), en integrant les **2 863 entrees** de `supplement-litterature-et-lectures-v1.jsonl` (`LIT-0001` a `LIT-2863`).",
        "",
        "## Chiffres cles v2",
        "",
        f"- **Idees et mecanismes canoniques** : **{len(final_idees)}** ({len(v1_idees)} heritees de `v1` dont **{attached_count} enrichies par rattachement direct LIT** + **{len(new_idees_added)} nouvelles fiches** `emprunt_litterature_a_citer` ou seances 1er et 21-22 nov.).",
        f"- **Litterature et voisins lus** (`litterature-et-voisins-lus.jsonl` / `.md`) : **{len(final_papers)} travaux externes** (**{n_pdf}** `lu_sur_pdf_entier`, **{n_res}** `lu_sur_resume`).",
        f"- **Acquis empiriques et morts connus** : **{len(final_acquis)}** fiches.",
        f"- **Outils, bancs et corpus** : **{len(final_outils)}** ressources.",
        f"- **Ecarts structurels et glossaires** : **{len(final_ecarts)}** groupes.",
        "- **Verification mecanique `0 orphelin`** : voir `verifier_couverture_bibliotheque_v2.py` et `CERTIFICAT-ZERO-ORPHELIN-v2.json`.",
        "",
    ]
    (V2_DIR / "LISEZMOI-BIBLIOTHEQUE-CANONIQUE-v2.md").write_text("\n".join(lisez), encoding="utf-8")
    print(f"V2 ASSEMBLED: idees={len(final_idees)} (v1={len(v1_idees)}, new={len(new_idees_added)}, attached={attached_count}), papers={len(final_papers)}, acquis={len(final_acquis)}, outils={len(final_outils)}, ecarts={len(final_ecarts)}")


if __name__ == "__main__":
    main()
