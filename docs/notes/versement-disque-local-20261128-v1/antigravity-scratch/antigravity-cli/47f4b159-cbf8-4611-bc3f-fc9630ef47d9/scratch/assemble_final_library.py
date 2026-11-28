#!/usr/bin/env python3
"""Applique Phase 3 (dedoublonnage transversal), renumerote IDEE-CANON-0001..K, construit la genealogie exacte et genere tous les fichiers de docs/notes/bibliotheque/catalogue-canonique-v1/."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(r"C:\Users\lciri\wt-organisme-boucle-fermee")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")
OUT_DIR = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v1"
RAYONS_DIR = OUT_DIR / "rayons"
RAYONS_DIR.mkdir(parents=True, exist_ok=True)

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
VALID_STATUTS = {
    "vierge", "preenregistre_en_attente", "pris_en_charge_groupe_v1",
    "deja_valide_interne", "deja_refute_interne",
}
VALID_REGIMES = {
    "CPU_0_USD_SYNTHETIQUE", "CPU_DONNEES_PUBLIQUES_REEL",
    "GPU_VAST_8B_SOUS_GO", "MODELE_FERME_COURSE_ETAPE_2",
}


def strip_emoji(s: str) -> str:
    return EMOJI_RE.sub("", str(s or "")).strip()


def normaliser_auteur_et_ref(raw: dict) -> tuple[str, str]:
    """Retourne (auteur_ou_modele_exact, reference_arxiv_ou_url)."""
    esp = strip_emoji(raw.get("espece_auteur", ""))
    fam = strip_emoji(raw.get("famille_source", ""))
    ch = strip_emoji(raw.get("source_chemin", ""))
    ant = strip_emoji(raw.get("anteriorite_brute", ""))
    txt = f"{esp} {ch} {ant} {raw.get('titre','')}".lower()

    # Extraire reference arXiv / URL si presente
    ref_m = re.search(r"(https?://[^\s\)\],;]+|arxiv[:\s]*\d{4}\.\d{4,5}(?:v\d+)?)", f"{ant} {esp} {raw.get('enonce_complet_brut','')}", re.I)
    ref_url = ref_m.group(1) if ref_m else ""

    if fam == "S09_Matiere_Premiere_Auto_Conception_21_Lots" or "arxiv" in ant.lower() or "arxiv.org" in ref_url.lower():
        if ref_url:
            return f"Veille arXiv / litterature ({ref_url})", ref_url
        if ant:
            return f"Veille litterature ({ant[:90]})", ""
        return "Veille litterature (21 lots)", ""

    # Detection auteur / modele exact
    if "lazar" in esp.lower() or "directeur" in esp.lower() or "question posée par lazar" in txt:
        return "Lazar", ref_url
    if "fable 5.2" in txt or "fable-5-2" in txt or "fable max" in txt or "reponse-fable" in ch.lower() or "conception-fable" in ch.lower() or "avis-fable" in ch.lower():
        return "Fable 5.2", ref_url
    if "fable 5.1" in txt or "fable-5-1" in txt:
        return "Fable 5.1", ref_url
    if "fable" in esp.lower():
        return "Fable 5.2", ref_url
    if "opus 5.5" in txt or "opus-5-5" in txt or "opus55" in ch.lower() or "opus-max" in ch.lower() or "opus" in esp.lower():
        return "Opus 5.5", ref_url
    if "carbon" in esp.lower() or "reponse-carbon" in ch.lower():
        return "Carbon", ref_url
    if "neon" in esp.lower() or "reponse-neon" in ch.lower():
        return "Neon", ref_url
    if "argon" in esp.lower() or "reponse-argon" in ch.lower() or "argon-seul" in ch.lower():
        return "Argon", ref_url
    if "astra" in esp.lower() or "gpt-6-astra" in txt or "reponse-astra" in ch.lower():
        return "Astra", ref_url
    if "kimi" in esp.lower() or "kimi-k3" in txt:
        return "Kimi", ref_url
    if "gemini" in esp.lower() or "gemini" in ch.lower():
        return "Gemini (Carbon/Neon/Argon)", ref_url
    if "5/5" in esp or "4/5" in esp or "3/5" in esp or "2/5" in esp or "multi" in esp.lower():
        return f"Collisionneur multi-modeles ({esp})", ref_url
    if "veille-de-cap" in esp.lower() or fam.startswith("S04_"):
        return "Veille de cap (registre interne)", ref_url
    if fam.startswith("S05_") or "bibliothecaire" in txt:
        return "Bibliothecaire (synthese programme)", ref_url
    if fam.startswith("S07_") or fam.startswith("S01_"):
        return "Plan Turing / Attelage (synthese multi-modeles)", ref_url
    if fam.startswith("S10_"):
        return "Cartographie des 18 verrous mathematiques", ref_url
    if esp and esp != "non_specifie":
        return esp[:90], ref_url
    return f"Source interne ({fam})", ref_url


def categorie_modele_croise(auteur: str) -> str:
    a = auteur.lower()
    if a == "lazar":
        return "Lazar (directeur)"
    if a.startswith("fable 5.2"):
        return "Fable 5.2"
    if a.startswith("fable 5.1"):
        return "Fable 5.1"
    if a.startswith("opus 5.5"):
        return "Opus 5.5"
    if a == "carbon":
        return "Carbon"
    if a == "neon":
        return "Neon"
    if a == "argon":
        return "Argon"
    if a == "astra":
        return "Astra"
    if a == "kimi":
        return "Kimi"
    if "veille arxiv" in a or "veille litterature" in a:
        return "Veille arXiv et litterature publiee"
    if "collisionneur" in a:
        return "Collisionneurs multi-modeles"
    return "Syntheses internes et registres (Veille de cap, Bibliothecaire, Plan Turing)"


def categorie_gisement(fam: str, auteur: str, ch: str) -> str:
    cl = ch.lower()
    if fam == "S01_Collisionneur_Attelage_Plan_Turing" or fam.startswith("S07_"):
        return "Plan Turing et Attelage (U01..U31, 101 pieces, pistes)"
    if fam == "S09_Matiere_Premiere_Auto_Conception_21_Lots":
        return "Veille arXiv et 21 lots de matiere premiere auto-conception"
    if fam.startswith("S04_"):
        return "Veille de cap et pistes d'octobre"
    if fam.startswith("S03_") or fam.startswith("S02_"):
        return "99 collisionneurs et Protocole X (361 propositions + cellules T1/T3)"
    if fam == "S11_Reponses_Directes_Fable_Amont_et_Modeles_Hors_Collisionneur":
        if "carbon" in auteur.lower() or "carbon" in cl:
            return "Carbon seul / consultations Google directes"
        if "opus" in auteur.lower() or "opus" in cl:
            return "Opus 5.5 direct hors collisionneur"
        if "fable" in auteur.lower() or "fable" in cl:
            return "Fable amont hors collisionneur"
        return "Autres reponses directes hors collisionneur (Neon, Argon, Kimi, Protocole X)"
    if fam.startswith("S12_") or "phase1" in fam.lower() or "supplement" in fam.lower():
        return "Branches brutes supplementaires Phase 1 (v8, brainstorm v9, courses mentors, visees maths)"
    if fam == "S05_Bibliothecaire_Registre_Idees_Pistes" or fam == "S08_Inventaire_Organisme_Complet_v7_10_Familles":
        return "Bibliothecaire et Inventaire v7 de l'organisme"
    if fam == "S06_Registre_62_Idees_Naissance_Idees_Fecondes":
        return "Registre des 62 idees (naissance des idees fecondes, 23 nov.)"
    if fam == "S10_Cartographie_18_Verrous_Mathematiques":
        return "Cartographie des 18 verrous mathematiques"
    return fam


def build_genealogie(bib_ids: list[str], master: dict[str, dict]) -> list[dict]:
    out = []
    for bid in sorted(set(bib_ids)):
        raw = master[bid]
        auteur, ref_url = normaliser_auteur_et_ref(raw)
        out.append({
            "id_bib": bid,
            "id_origine": strip_emoji(raw.get("id_origine", "")),
            "auteur_ou_modele": auteur,
            "famille_source": strip_emoji(raw.get("famille_source", "")),
            "source_chemin": strip_emoji(raw.get("source_chemin", "")).replace("\\", "/"),
            "source_branche": strip_emoji(raw.get("source_branche", "")),
            "reference_arxiv_ou_url": ref_url,
        })
    return out


def ensure_clear_title(title: str) -> str:
    """Verifie R-3044 / R-5226 : jamais de code nu en tete avant un titre scientifique explicite."""
    t = strip_emoji(title)
    # Si un titre commence par un code du type "[U01] ..." ou "U01 : ..." ou "MP-lot-01-..."
    m = re.match(r"^[\[\(]?([A-Z]{1,4}[-_]\d+[A-Za-z0-9._-]*|[UP]\d{1,3})[\]\)]?\s*[:\-—|]\s*(.+)$", t)
    if m and len(m.group(2).strip()) >= 12:
        t = f"{m.group(2).strip()} ({m.group(1)})"
    return t


def main() -> None:
    master = {
        json.loads(l)["id_unifie"]: json.loads(l)
        for l in (SCRATCH / "corpus_total_enrichi.jsonl").read_text(encoding="utf-8").splitlines()
        if l.strip()
    }
    state = json.loads((SCRATCH / "phase2b_post_state.json").read_text(encoding="utf-8"))

    idees_map = {x["temp_id"]: x for x in state["idees"]}
    acquis_list = list(state["acquis"])
    outils_list = list(state["outils"])
    ecarts_list = list(state["ecarts"])

    p3_dec_path = SCRATCH / "phase3_decisions.json"
    p3_dec = json.loads(p3_dec_path.read_text(encoding="utf-8")) if p3_dec_path.is_file() else {}

    # Appliquer les fusions inter-rayons Phase 3
    redirect = {}

    def resolve(tid: str) -> str:
        seen = set()
        while tid in redirect and tid not in seen:
            seen.add(tid)
            tid = redirect[tid]
        return tid

    for m in p3_dec.get("cross_merges") or []:
        keep = resolve(str(m.get("keep_id", "")))
        if keep not in idees_map:
            continue
        k_item = idees_map[keep]
        for mid_raw in m.get("merge_ids") or []:
            mid = resolve(str(mid_raw))
            if mid == keep or mid not in idees_map:
                continue
            other = idees_map.pop(mid)
            redirect[mid] = keep
            k_item["bib_ids"] = list(dict.fromkeys(k_item["bib_ids"] + other["bib_ids"]))
            if other.get("anteriorite_connue") and "Aucune" not in other["anteriorite_connue"]:
                if not k_item.get("anteriorite_connue") or "Aucune" in k_item["anteriorite_connue"]:
                    k_item["anteriorite_connue"] = other["anteriorite_connue"]
                elif other["anteriorite_connue"] not in k_item["anteriorite_connue"]:
                    k_item["anteriorite_connue"] = f"{k_item['anteriorite_connue']} ; {other['anteriorite_connue']}"
        for src_k, dst_k in (
            ("upgraded_titre_clair_fr", "titre_clair_fr"),
            ("upgraded_theme", "theme"),
            ("upgraded_sous_theme", "sous_theme"),
            ("upgraded_enonce_complet", "enonce_complet"),
            ("upgraded_mecanisme_causal", "mecanisme_causal"),
            ("upgraded_anteriorite_connue", "anteriorite_connue"),
            ("upgraded_esquisse_test_de_mort_et_faux_temoin", "esquisse_test_de_mort_et_faux_temoin"),
        ):
            if isinstance(m.get(src_k), str) and m[src_k].strip():
                k_item[dst_k] = m[src_k].strip()
        if m.get("upgraded_objet") in VALID_OBJETS:
            k_item["objet"] = m["upgraded_objet"]
        if m.get("upgraded_statut_epistemique") in VALID_STATUTS:
            k_item["statut_epistemique"] = m["upgraded_statut_epistemique"]
        if m.get("upgraded_regime_materiel") in VALID_REGIMES:
            k_item["regime_materiel"] = m["upgraded_regime_materiel"]

    for mv in p3_dec.get("moves") or []:
        tid = resolve(str(mv.get("temp_id", "")))
        if tid in idees_map:
            if mv.get("objet") in VALID_OBJETS:
                idees_map[tid]["objet"] = mv["objet"]
            if mv.get("theme"):
                idees_map[tid]["theme"] = mv["theme"]
            if mv.get("sous_theme"):
                idees_map[tid]["sous_theme"] = mv["sous_theme"]

    # Trier proprement les idees canoniques par (objet, theme, sous_theme, -len(bib_ids), titre)
    idees_sorted = sorted(
        idees_map.values(),
        key=lambda x: (
            x.get("objet", ""),
            x.get("theme", ""),
            x.get("sous_theme", ""),
            -len(x["bib_ids"]),
            x.get("titre_clair_fr", "").lower(),
        ),
    )

    # Construire les 4 registres finaux numerotes
    final_idees = []
    for idx, it in enumerate(idees_sorted, 1):
        gen = build_genealogie(it["bib_ids"], master)
        # Completer anteriorite a partir de la genealogie si vide
        ant = strip_emoji(it.get("anteriorite_connue", ""))
        refs_ant = [g["reference_arxiv_ou_url"] for g in gen if g["reference_arxiv_ou_url"]]
        if (not ant or ant.lower() in ("aucune", "n/a", "none", "-")) and refs_ant:
            ant = "References identifiees dans la veille : " + ", ".join(dict.fromkeys(refs_ant))
        elif not ant:
            ant = "Aucune anteriorite publiee identifiee dans le corpus interne (a verifier sur PDF avant revendication, R7/R8)."

        rec = {
            "id_canonique": f"IDEE-CANON-{idx:04d}",
            "titre_clair_fr": ensure_clear_title(it.get("titre_clair_fr", "")),
            "objet": it["objet"] if it.get("objet") in VALID_OBJETS else "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
            "theme": strip_emoji(it.get("theme", "")),
            "sous_theme": strip_emoji(it.get("sous_theme", "")) or "Axe general",
            "enonce_complet": strip_emoji(it.get("enonce_complet", "")),
            "mecanisme_causal": strip_emoji(it.get("mecanisme_causal", "")),
            "genealogie_sources": gen,
            "anteriorite_connue": ant,
            "statut_epistemique": it["statut_epistemique"] if it.get("statut_epistemique") in VALID_STATUTS else "vierge",
            "regime_materiel": it["regime_materiel"] if it.get("regime_materiel") in VALID_REGIMES else "CPU_0_USD_SYNTHETIQUE",
            "esquisse_test_de_mort_et_faux_temoin": strip_emoji(it.get("esquisse_test_de_mort_et_faux_temoin", "")),
        }
        final_idees.append(rec)

    acquis_sorted = sorted(acquis_list, key=lambda x: (x.get("objet", ""), x.get("theme", ""), x.get("titre_clair_fr", "").lower()))
    final_acquis = []
    for idx, it in enumerate(acquis_sorted, 1):
        final_acquis.append({
            "id_acquis": f"ACQUIS-{idx:04d}",
            "titre_clair_fr": ensure_clear_title(it.get("titre_clair_fr", "")),
            "objet": it.get("objet") if it.get("objet") in VALID_OBJETS else "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
            "theme": strip_emoji(it.get("theme", "")),
            "type_acquis": strip_emoji(it.get("type_acquis", "")) or "constat_tranche",
            "enonce_complet": strip_emoji(it.get("enonce_complet", "")),
            "motif_ou_resultat": strip_emoji(it.get("motif_ou_resultat", "")),
            "genealogie_sources": build_genealogie(it["bib_ids"], master),
        })

    outils_sorted = sorted(outils_list, key=lambda x: (x.get("objet", ""), x.get("theme", ""), x.get("titre_clair_fr", "").lower()))
    final_outils = []
    for idx, it in enumerate(outils_sorted, 1):
        final_outils.append({
            "id_outil": f"OUTIL-{idx:04d}",
            "titre_clair_fr": ensure_clear_title(it.get("titre_clair_fr", "")),
            "objet": it.get("objet") if it.get("objet") in VALID_OBJETS else "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
            "theme": strip_emoji(it.get("theme", "")),
            "type_outil": strip_emoji(it.get("type_outil", "")) or "banc_experimental",
            "description_complete": strip_emoji(it.get("description_complete", "")),
            "genealogie_sources": build_genealogie(it["bib_ids"], master),
        })

    final_ecarts = []
    for idx, it in enumerate(ecarts_list, 1):
        final_ecarts.append({
            "id_ecart": f"ECART-{idx:04d}",
            "motif_ecart": strip_emoji(it.get("motif_ecart", "")) or "Entree structurelle sans idee scientifique autonome",
            "resume_court": strip_emoji(it.get("resume_court", "")),
            "genealogie_sources": build_genealogie(it["bib_ids"], master),
        })

    # Ecrire les 4 JSONL
    (OUT_DIR / "idees-et-mecanismes-canoniques.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in final_idees) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "acquis-empiriques-et-morts-connus.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in final_acquis) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "outils-bancs-et-corpus.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in final_outils) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "ecartes-structurels-et-glossaires.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in final_ecarts) + "\n", encoding="utf-8"
    )

    # Generer acquis-empiriques-et-morts-connus.md
    acq_md = [
        "# Acquis empiriques, theoremes prouves et pistes deja refutees (memoire des morts)",
        "",
        f"Ce registre rassemble **{len(final_acquis)} fiches** couvrant **{sum(len(x['genealogie_sources']) for x in final_acquis)} occurrences brutes** de constats deja tranches, theoremes demontres ou pistes deja refutees dans le programme, afin d'eviter toute relance redondante.",
        "",
    ]
    acq_by_obj = defaultdict(list)
    for x in final_acquis:
        acq_by_obj[x["objet"]].append(x)
    for obj_key, (obj_label, _) in OBJETS_META.items():
        lst = acq_by_obj[obj_key]
        acq_md.append(f"## {obj_label} ({len(lst)} fiches)")
        acq_md.append("")
        for x in lst:
            bibs = ", ".join(g["id_bib"] for g in x["genealogie_sources"])
            auteurs = ", ".join(sorted(set(g["auteur_ou_modele"] for g in x["genealogie_sources"])))
            acq_md.append(f"### {x['titre_clair_fr']} ({x['id_acquis']})")
            acq_md.append(f"- **Type** : `{x['type_acquis']}` | **Theme** : {x['theme']}")
            acq_md.append(f"- **Enonce complet** : {x['enonce_complet']}")
            if x["motif_ou_resultat"]:
                acq_md.append(f"- **Resultat ou motif de refutation** : {x['motif_ou_resultat']}")
            acq_md.append(f"- **Sources fusionnees ({len(x['genealogie_sources'])})** : {auteurs} — `{bibs}`")
            acq_md.append("")
    (OUT_DIR / "acquis-empiriques-et-morts-connus.md").write_text("\n".join(acq_md), encoding="utf-8")

    # Generer outils-bancs-et-corpus.md
    out_md = [
        "# Outils, bancs experimentaux, scripts et corpus publics",
        "",
        f"Ce registre rassemble **{len(final_outils)} ressources operationnelles** couvrant **{sum(len(x['genealogie_sources']) for x in final_outils)} occurrences brutes** (jeux de donnees publics, scripts, logiciels et bancs experimentaux existants).",
        "",
    ]
    out_by_obj = defaultdict(list)
    for x in final_outils:
        out_by_obj[x["objet"]].append(x)
    for obj_key, (obj_label, _) in OBJETS_META.items():
        lst = out_by_obj[obj_key]
        out_md.append(f"## {obj_label} ({len(lst)} ressources)")
        out_md.append("")
        for x in lst:
            bibs = ", ".join(g["id_bib"] for g in x["genealogie_sources"])
            chemins = ", ".join(sorted(set(f"`{g['source_chemin']}`" for g in x["genealogie_sources"] if g["source_chemin"]))[:6])
            out_md.append(f"### {x['titre_clair_fr']} ({x['id_outil']})")
            out_md.append(f"- **Categorie** : `{x['type_outil']}` | **Theme** : {x['theme']}")
            out_md.append(f"- **Description complete** : {x['description_complete']}")
            out_md.append(f"- **Occurrences ({len(x['genealogie_sources'])})** : `{bibs}` | Chemins : {chemins}")
            out_md.append("")
    (OUT_DIR / "outils-bancs-et-corpus.md").write_text("\n".join(out_md), encoding="utf-8")

    # Generer les 5 rayons complets sans troncature
    idees_by_obj = defaultdict(list)
    for x in final_idees:
        idees_by_obj[x["objet"]].append(x)

    for obj_key, (obj_label, filename) in OBJETS_META.items():
        lst = idees_by_obj[obj_key]
        rmd = [
            f"# {obj_label}",
            "",
            f"Ce rayon rassemble **{len(lst)} fiches canoniques** (fusionnant **{sum(len(x['genealogie_sources']) for x in lst)} occurrences brutes**) classees par theme et sous-theme, sans aucune troncature.",
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
                st_items = by_th[th][st]
                rmd.append(f"### Sous-theme : {st} ({len(st_items)} fiches)")
                rmd.append("")
                for x in st_items:
                    rmd.append(f"#### {x['titre_clair_fr']} ({x['id_canonique']})")
                    rmd.append("")
                    rmd.append(f"- **Statut epistemique** : `{x['statut_epistemique']}` | **Regime materiel** : `{x['regime_materiel']}` | **Occurrences fusionnees** : **{len(x['genealogie_sources'])}**")
                    rmd.append(f"- **Enonce complet** : {x['enonce_complet']}")
                    rmd.append(f"- **Mecanisme causal** : {x['mecanisme_causal']}")
                    rmd.append(f"- **Anteriorite connue** : {x['anteriorite_connue']}")
                    rmd.append(f"- **Esquisse de test de mort et faux temoin (1b)** : {x['esquisse_test_de_mort_et_faux_temoin']}")
                    rmd.append("- **Genealogie complete des sources** :")
                    for g in x["genealogie_sources"]:
                        ref_part = f" | Ref : {g['reference_arxiv_ou_url']}" if g["reference_arxiv_ou_url"] else ""
                        rmd.append(
                            f"  - `{g['id_bib']}` (`{g['id_origine']}`) — **{g['auteur_ou_modele']}** | `{g['famille_source']}` | `{g['source_branche']}:{g['source_chemin']}`{ref_part}"
                        )
                    rmd.append("")
        (RAYONS_DIR / filename).write_text("\n".join(rmd), encoding="utf-8")

    # Generer CATALOGUE-GENERAL-PAR-SUJET-ET-THEME-v1.md
    cat_gen = [
        "# Catalogue general de la Bibliotheque scientifique canonique par sujet, theme et sous-theme (version 1)",
        "",
        f"Ce catalogue inventorie l'integralite des **{len(final_idees)} fiches canoniques d'idees et mecanismes** issues de **{len(master)} entrees brutes** (`BIB-0001` a `BIB-{len(master):04d}`), sans aucun orphelin.",
        "",
        "## Vue synthetique par Objet",
        "",
        "| Objet scientifique | Fiches canoniques | Occurrences brutes fusionnees | Rayon complet |",
        "|---|---:|---:|---|",
    ]
    for obj_key, (obj_label, filename) in OBJETS_META.items():
        lst = idees_by_obj[obj_key]
        cat_gen.append(f"| {obj_label} | **{len(lst)}** | {sum(len(x['genealogie_sources']) for x in lst)} | `rayons/{filename}` |")
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
                cat_gen.append("| ID canonique | Titre scientifique en clair | Statut | Regime materiel | Sources fusionnees | Auteurs / modeles |")
                cat_gen.append("|---|---|---|---|---:|---|")
                for x in by_th[th][st]:
                    auteurs = ", ".join(sorted(set(categorie_modele_croise(g["auteur_ou_modele"]) for g in x["genealogie_sources"])))
                    titre_safe = x["titre_clair_fr"].replace("|", "/")
                    cat_gen.append(
                        f"| `{x['id_canonique']}` | {titre_safe} | `{x['statut_epistemique']}` | `{x['regime_materiel']}` | {len(x['genealogie_sources'])} | {auteurs.replace('|','/')} |"
                    )
                cat_gen.append("")
    (OUT_DIR / "CATALOGUE-GENERAL-PAR-SUJET-ET-THEME-v1.md").write_text("\n".join(cat_gen), encoding="utf-8")

    # Generer CATALOGUE-CROISE-PAR-SOURCE-ET-MODELE-v1.md (exclusives vs co-inventees par modele et par gisement)
    mod_total = defaultdict(list)
    mod_excl = defaultdict(list)
    mod_co = defaultdict(list)
    gis_total = defaultdict(list)
    gis_excl = defaultdict(list)
    gis_co = defaultdict(list)

    for x in final_idees:
        mods = sorted(set(categorie_modele_croise(g["auteur_ou_modele"]) for g in x["genealogie_sources"]))
        giss = sorted(set(categorie_gisement(g["famille_source"], g["auteur_ou_modele"], g["source_chemin"]) for g in x["genealogie_sources"]))
        for m in mods:
            mod_total[m].append(x)
            if len(mods) == 1:
                mod_excl[m].append(x)
            else:
                mod_co[m].append(x)
        for gi in giss:
            gis_total[gi].append(x)
            if len(giss) == 1:
                gis_excl[gi].append(x)
            else:
                gis_co[gi].append(x)

    croise = [
        "# Catalogue croise par source, auteur, modele et gisement (version 1)",
        "",
        "Ce catalogue distingue, pour chaque auteur ou modele et pour chaque gisement documentaire du programme, les **idees canoniques exclusives** (apportees uniquement par cette source) et les **idees co-inventees ou convergees** (presentes chez au moins deux auteurs/modeles ou gisements distincts).",
        "",
    ]
    if p3_dec.get("synthese_croisee_editoriale"):
        croise.append("## Note analytique du conservateur en chef")
        croise.append("")
        croise.append(strip_emoji(p3_dec["synthese_croisee_editoriale"]))
        croise.append("")

    croise += [
        "## 1. Tableau synoptique par auteur ou modele",
        "",
        "| Auteur / Modele | Idees canoniques totales | Idees exclusives | Idees co-inventees / convergees | Part exclusive |",
        "|---|---:|---:|---:|---:|",
    ]
    for m in sorted(mod_total, key=lambda k: -len(mod_total[k])):
        tot = len(mod_total[m])
        ex = len(mod_excl[m])
        co = len(mod_co[m])
        pct = f"{100.0 * ex / tot:.1f} %" if tot else "0.0 %"
        croise.append(f"| {m} | **{tot}** | **{ex}** | {co} | {pct} |")

    croise += [
        "",
        "## 2. Tableau synoptique par gisement documentaire",
        "",
        "| Gisement source | Idees canoniques totales | Idees exclusives au gisement | Idees partagees inter-gisements | Part exclusive |",
        "|---|---:|---:|---:|---:|",
    ]
    for gi in sorted(gis_total, key=lambda k: -len(gis_total[k])):
        tot = len(gis_total[gi])
        ex = len(gis_excl[gi])
        co = len(gis_co[gi])
        pct = f"{100.0 * ex / tot:.1f} %" if tot else "0.0 %"
        croise.append(f"| {gi} | **{tot}** | **{ex}** | {co} | {pct} |")

    croise += ["", "## 3. Detail complet des apports par auteur ou modele", ""]
    for m in sorted(mod_total, key=lambda k: -len(mod_total[k])):
        croise.append(f"### {m} ({len(mod_total[m])} idees : {len(mod_excl[m])} exclusives, {len(mod_co[m])} co-inventees)")
        croise.append("")
        if mod_excl[m]:
            croise.append("#### Idees exclusives")
            croise.append("")
            for x in mod_excl[m]:
                croise.append(f"- `{x['id_canonique']}` — **{x['titre_clair_fr']}** (`{x['objet']}`, `{x['statut_epistemique']}`, `{x['regime_materiel']}`)")
            croise.append("")
        if mod_co[m]:
            croise.append("#### Idees co-inventees ou convergees avec d'autres sources")
            croise.append("")
            for x in mod_co[m]:
                autres = ", ".join(sorted(set(categorie_modele_croise(g["auteur_ou_modele"]) for g in x["genealogie_sources"]) - {m}))
                croise.append(f"- `{x['id_canonique']}` — **{x['titre_clair_fr']}** (avec : {autres} ; {len(x['genealogie_sources'])} occurrences)")
            croise.append("")

    croise += ["## 4. Detail complet par gisement documentaire", ""]
    for gi in sorted(gis_total, key=lambda k: -len(gis_total[gi])):
        croise.append(f"### {gi} ({len(gis_total[gi])} idees : {len(gis_excl[gi])} exclusives, {len(gis_co[gi])} partagees)")
        croise.append("")
        for x in gis_excl[gi]:
            croise.append(f"- [Exclusive] `{x['id_canonique']}` — **{x['titre_clair_fr']}** (`{x['statut_epistemique']}`)")
        for x in gis_co[gi]:
            croise.append(f"- [Partagee, {len(x['genealogie_sources'])} occ.] `{x['id_canonique']}` — **{x['titre_clair_fr']}**")
        croise.append("")

    (OUT_DIR / "CATALOGUE-CROISE-PAR-SOURCE-ET-MODELE-v1.md").write_text("\n".join(croise), encoding="utf-8")

    # Generer LISEZMOI-BIBLIOTHEQUE-CANONIQUE-v1.md
    c_stat = Counter(x["statut_epistemique"] for x in final_idees)
    c_reg = Counter(x["regime_materiel"] for x in final_idees)
    n_supp = len(master) - 6213
    lisez = [
        "# Bibliotheque scientifique canonique du programme (version 1)",
        "",
        "Piece de travail de reference (classe C) construite sous l'accord `GO-2026-11-25-06`, dans le respect strict des regles de cloisonnement (`CLAUDE.md` : aucun coffre, aucun verdict sous embargo, aucune reponse des questions temoins, aucun run actif des moniteurs/sondes/saboteurs ni `protocole-x-attaquant-v1` ouvert) et des regles de clarte scientifique (`R-3044`, `R-5226`).",
        "",
        "## Chiffres cles certifies (porte mecanique 0 orphelin)",
        "",
        f"- **Fonds brut total ingere** : **{len(master)} entrees brutes** (`BIB-0001` a `BIB-6213` du corpus unifie v1 enrichi sans troncature + **{n_supp} entrees supplementaires** `BIB-6214` a `BIB-{len(master):04d}` extraites des branches brutes restantes).",
        f"- **Registre 1 — Idees et mecanismes canoniques** (`idees-et-mecanismes-canoniques.jsonl`) : **{len(final_idees)} fiches canoniques** (`IDEE-CANON-0001` a `IDEE-CANON-{len(final_idees):04d}`), fusionnant **{sum(len(x['genealogie_sources']) for x in final_idees)} occurrences brutes**.",
        f"- **Registre 2 — Acquis empiriques et morts connus** (`acquis-empiriques-et-morts-connus.jsonl` et `.md`) : **{len(final_acquis)} fiches** couvrant **{sum(len(x['genealogie_sources']) for x in final_acquis)} occurrences brutes**.",
        f"- **Registre 3 — Outils, bancs et corpus** (`outils-bancs-et-corpus.jsonl` et `.md`) : **{len(final_outils)} ressources** couvrant **{sum(len(x['genealogie_sources']) for x in final_outils)} occurrences brutes**.",
        f"- **Registre 4 — Ecarts structurels et glossaires** (`ecartes-structurels-et-glossaires.jsonl`) : **{len(final_ecarts)} groupes** couvrant **{sum(len(x['genealogie_sources']) for x in final_ecarts)} occurrences brutes** sans idee scientifique autonome.",
        f"- **Orphelins certifies** : **0** (preuve mecanique dans `CERTIFICAT-ZERO-ORPHELIN-v1.json` produit par `verifier_couverture_bibliotheque_v1.py`).",
        "",
    ]
    if p3_dec.get("synthese_lisezmoi_editoriale"):
        lisez.append("## Architecture et mode d'emploi scientifique")
        lisez.append("")
        lisez.append(strip_emoji(p3_dec["synthese_lisezmoi_editoriale"]))
        lisez.append("")

    lisez += [
        "## Repartition des idees canoniques par statut epistemique et regime materiel",
        "",
        "| Statut epistemique | Nombre d'idees canoniques |",
        "|---|---:|",
    ]
    for st in ("vierge", "preenregistre_en_attente", "pris_en_charge_groupe_v1", "deja_valide_interne", "deja_refute_interne"):
        lisez.append(f"| `{st}` | **{c_stat[st]}** |")
    lisez += [
        "",
        "| Regime materiel d'epreuve | Nombre d'idees canoniques |",
        "|---|---:|",
    ]
    for rg in ("CPU_0_USD_SYNTHETIQUE", "CPU_DONNEES_PUBLIQUES_REEL", "GPU_VAST_8B_SOUS_GO", "MODELE_FERME_COURSE_ETAPE_2"):
        lisez.append(f"| `{rg}` | **{c_reg[rg]}** |")

    lisez += [
        "",
        "## Plan des fichiers de la Bibliotheque",
        "",
        "- `CATALOGUE-GENERAL-PAR-SUJET-ET-THEME-v1.md` : index complet en 5 Objets, themes et sous-themes.",
        "- `CATALOGUE-CROISE-PAR-SOURCE-ET-MODELE-v1.md` : vue croisee par auteur/modele et par gisement (exclusives contre co-inventees).",
        "- `rayons/01-metrologie-attelage-et-tests-de-mort.md` a `rayons/05-etalonnages-corpus-reels-et-gpu-8b.md` : fiches canoniques integrales sans troncature.",
        "- `idees-et-mecanismes-canoniques.jsonl` : registre machine maitre pour l'organisme en boucle fermee.",
        "- `acquis-empiriques-et-morts-connus.jsonl` et `.md` : memoire des resultats tranches et pistes refutees.",
        "- `outils-bancs-et-corpus.jsonl` et `.md` : inventaire des bancs, corpus publics et scripts disponibles.",
        "- `ecartes-structurels-et-glossaires.jsonl` : journal integral des entrees ecartees avec motif.",
        "- `supplement-branches-brutes-v1.jsonl` : complement d'ingestion brute issu des branches restantes (`BIB-6214` et suivants).",
        "- `verifier_couverture_bibliotheque_v1.py` et `CERTIFICAT-ZERO-ORPHELIN-v1.json` : verification mecanique reproductible.",
        "",
    ]
    (OUT_DIR / "LISEZMOI-BIBLIOTHEQUE-CANONIQUE-v1.md").write_text("\n".join(lisez), encoding="utf-8")

    print(
        f"ASSEMBLED FINAL LIBRARY: total_raw={len(master)}, idees={len(final_idees)}, "
        f"acquis={len(final_acquis)}, outils={len(final_outils)}, ecarts={len(final_ecarts)}"
    )


if __name__ == "__main__":
    main()
