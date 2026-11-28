#!/usr/bin/env python3
"""Extraction lecture seule (git show) sous cloisonnement strict pour Phase 1 et enrichissement des 6 213 entrees."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(r"C:\Users\lciri\wt-organisme-boucle-fermee")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")
SCRATCH.mkdir(parents=True, exist_ok=True)

MOTIFS_INTERDITS = (
    "coffre/",
    "docs/verdicts/",
    "/verdict/",
    "verdict/",
    "reponses-ne-pas-servir",
    "protocole-x-attaquant-v1",
    "evasion-moniteurs",
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
    "dose-reponse",
    "sondes-iib",
    "versant-honnete",
    "sondes-v2",
    "modes-attaque-reponse-24",
)

BRANCHES_CIBLES = [
    ("runs_collisionneurs", "origin/runs/collisionneurs-partiels-passation-2026-11-24-0620"),
    ("runs_collisionneurs", "origin/runs/collisionneurs-reprise-2026-11-24-v1"),
    ("runs_collisionneurs", "origin/runs/collisionneurs-reprise-minuit-v1"),
    ("runs_collisionneurs", "origin/runs/collisionneurs-reprise-v8d-v1"),
    ("v8_runs_v2", "origin/donnees/collisionneur-v8-runs-v2"),
    ("v9_brainstorm", "origin/donnees/collisionneur-v9-brainstorm-v1"),
    ("v9_brainstorm", "origin/donnees/collisionneur-v9-brainstorm-v1-suite"),
    ("courses_mentors", "origin/donnees/course-colognese-ward-q2-v1-run"),
    ("courses_mentors", "origin/donnees/course-colognese-ward-q2-v2-run"),
    ("courses_mentors", "origin/donnees/course-heimersheim-v1-run"),
    ("courses_mentors", "origin/donnees/course-ibrahim-q1-seconde-v1-run"),
    ("courses_mentors", "origin/donnees/course-ibrahim-q1-v1-run"),
    ("courses_mentors", "origin/donnees/course-jang-feng-v1-run"),
    ("courses_mentors", "origin/donnees/course-kirchner-q2-v1-run"),
    ("courses_mentors", "origin/donnees/course-kirchner-q2-v1-run-seconde"),
    ("courses_mentors", "origin/donnees/course-scheurer-v1-run"),
    ("courses_mentors", "origin/donnees/course-scheurer-v2-run"),
    ("visees_math_et_edison", "origin/matiere-premiere/visees-mathematiques-v1"),
    ("visees_math_et_edison", "origin/claude/upbeat-edison-t3wegg"),
]


def est_interdit(texte: str) -> bool:
    t = texte.replace("\\", "/").lower()
    return any(m in t for m in MOTIFS_INTERDITS)


def git_show(ref_path: str) -> str:
    if est_interdit(ref_path):
        raise ValueError(f"Chemin interdit refuse: {ref_path}")
    out = subprocess.check_output(
        ["git", "show", ref_path],
        cwd=str(RACINE),
        stderr=subprocess.DEVNULL,
    )
    return out.decode("utf-8", errors="replace")


def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def nettoyer(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def enrichir_corpus_6213() -> tuple[list[dict], set[str], set[str]]:
    p_in = RACINE / "docs/notes/bibliotheque/corpus-unifie-idees-v1/corpus-unifie-idees-v1.jsonl"
    rows = [json.loads(l) for l in p_in.read_text(encoding="utf-8").splitlines() if l.strip()]

    # 1. Charger unites-v2.json depuis origin/audit/protocole-x-v1 pour restaurer les 123 S03 tronques
    unites_raw = json.loads(git_show("origin/audit/protocole-x-v1:docs/notes/audit-protocole-x-v1/sorties/unites-v2.json"))
    premiers_map: dict[str, dict] = {}
    for pr in unites_raw.get("premiers", []):
        key = f"PREM-{pr.get('racine','')}-{pr.get('lettre','')}-T{pr.get('tour','')}"
        premiers_map[key] = pr
    unites_map: dict[str, dict] = {}
    for u in unites_raw.get("unites", []):
        if u.get("id"):
            unites_map[u["id"]] = u

    # 2. Charger les 21 lots JSON locaux pour enrichir proprement les 1 098 entrees S09
    lots_map: dict[str, dict] = {}
    for lf in sorted((RACINE / "docs/notes/matiere-premiere-auto-conception-v1/lots").glob("lot-*.json")):
        items = json.loads(lf.read_text(encoding="utf-8"))
        for it in items:
            mecs = it.get("mecanismes") or []
            if isinstance(mecs, list):
                for idx_m, m in enumerate(mecs, 1):
                    mid = f"MP-{lf.stem}-{it.get('indice', 0)}-{idx_m}"
                    lots_map[mid] = {
                        "titre_travail": it.get("titre", ""),
                        "adresse": it.get("adresse", ""),
                        "date": it.get("date", ""),
                        "nature": it.get("nature", ""),
                        "profondeur_de_lecture": it.get("profondeur_de_lecture", ""),
                        "mesure_selon_la_table": it.get("mesure_selon_la_table", ""),
                        "mecanisme": m,
                    }

    # 3. Charger les 18 verrous locaux pour S10
    p_ver = RACINE / "docs/notes/cartographie-mathematiques-ouvertes-v1/catalogue-verrous-v1.json"
    verrous_map: dict[str, dict] = {}
    for v in json.loads(p_ver.read_text(encoding="utf-8")).get("fiches_maitresses", []):
        if v.get("id"):
            verrous_map[v["id"]] = v

    # 4. Charger les textes complets des fichiers S01 (U01..U31) si besoin
    enriched = []
    seen_paths = set()
    seen_hashes = set()
    restored_s03 = 0
    restored_s09 = 0
    restored_s10 = 0

    for r in rows:
        e = dict(r)
        src_path = (e.get("source_chemin") or "").replace("\\", "/")
        seen_paths.add(src_path.lower())
        e["anteriorite_brute"] = ""
        e["enonce_complet_brut"] = e.get("enonce", "")

        fam = e.get("famille_source", "")
        oid = e.get("id_origine", "")

        if fam == "S03_Cellules_Brutes_99_Collisionneurs_Premieres_Experiences" and oid in premiers_map:
            full_txt = nettoyer(premiers_map[oid].get("texte", ""))
            if len(full_txt) > len(e["enonce_complet_brut"]):
                e["enonce_complet_brut"] = full_txt
                restored_s03 += 1
        elif fam == "S03_Cellules_Brutes_99_Collisionneurs_Unites" and oid in unites_map:
            full_txt = nettoyer(unites_map[oid].get("extrait", ""))
            if len(full_txt) > len(e["enonce_complet_brut"]):
                e["enonce_complet_brut"] = full_txt
                restored_s03 += 1
        elif fam == "S09_Matiere_Premiere_Auto_Conception_21_Lots" and oid in lots_map:
            info = lots_map[oid]
            m = info["mecanisme"]
            if isinstance(m, dict):
                phrase = nettoyer(
                    m.get("mecanisme_en_une_phrase")
                    or m.get("mecanisme")
                    or m.get("description")
                    or json.dumps(m, ensure_ascii=False)
                )
                fam_m = m.get("famille", "")
                epr = m.get("eprouve_contre_le_reel", "")
                src_dep = m.get("source_dans_le_depot", "")
            else:
                phrase = nettoyer(str(m))
                fam_m, epr, src_dep = "", "", ""
            e["enonce_complet_brut"] = (
                f"[{fam_m} | {epr}] {phrase} "
                f"(Travail: {info['titre_travail']} ; Date: {info['date']} ; Nature: {info['nature']} ; "
                f"Mesure: {info['mesure_selon_la_table']})"
            ).strip()
            adr = info.get("adresse", "")
            if adr or info.get("titre_travail"):
                e["anteriorite_brute"] = f"{info['titre_travail']} ({info['date']}) {adr}".strip()
            if info.get("nature") and "arxiv" in info["nature"].lower():
                e["espece_auteur"] = f"Veille arXiv ({info['titre_travail'][:80]}, {adr})"
            elif adr.startswith("http"):
                e["espece_auteur"] = f"Veille litterature ({info['titre_travail'][:80]}, {adr})"
            else:
                e["espece_auteur"] = f"Matiere premiere interne ({info['nature']})"
            restored_s09 += 1
        elif fam == "S10_Cartographie_18_Verrous_Mathematiques" and oid in verrous_map:
            v = verrous_map[oid]
            mini = v.get("miniature_test_de_mort", "")
            mini_s = json.dumps(mini, ensure_ascii=False) if isinstance(mini, (dict, list)) else str(mini)
            e["enonce_complet_brut"] = nettoyer(
                f"Enonce formel: {v.get('enonce_formel_canonique','')} | "
                f"Noyau ouvert: {v.get('noyau_mathematique_ouvert','')} | "
                f"Test de mort miniature: {mini_s} | "
                f"Famille: {v.get('famille','')}"
            )
            restored_s10 += 1

        seen_hashes.add(sha256_str(nettoyer(e["enonce_complet_brut"])[:300])[:16])
        enriched.append(e)

    out_p = SCRATCH / "corpus_enrichi_6213.jsonl"
    out_p.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in enriched) + "\n", encoding="utf-8")
    print(f"ENRICHI 6213 -> {out_p} (restored S03={restored_s03}, S09={restored_s09}, S10={restored_s10})")
    return enriched, seen_paths, seen_hashes


def est_doc_scientifique_cible(branche: str, chemin: str) -> bool:
    c = chemin.replace("\\", "/").lower()
    if est_interdit(c) or est_interdit(branche):
        return False
    if c.endswith(".sha256"):
        return False
    # Exclure journaux techniques, essais bruts redondants, abonnements, configs, passations
    if any(skip in c for skip in ("/essais/", "/abonnement/", "journal.jsonl", "especes.json", "controle-", "registres/essaim/", "registres/passations/", "relais-kimi-", "configuration-", "contre-lecture-", "rapport-developpeur-", "verification-retroactive", "branches-kits-", "candidature-openai")):
        return False
    # Garder cellules T1/T3, notes de sortie, rapports de course, bilans/propositions, consultations externes
    if "/cellules/" in c and c.endswith(".md"):
        # Garder T1 (conception) et T3 (riposte/synthese), eviter T2 critique pure si deja redondant mais gardons T1+T3 (et si pas de T1/T3 garder md)
        if "-t2-" in c:
            return False
        return True
    if "note-sortie-" in c or "note-de-sortie-" in c:
        return c.endswith(".md")
    if "rapport-course-" in c or "rapport-suite-" in c or "epreuves-suite-" in c:
        return c.endswith(".md")
    if "consultation-externe-v1/reponse-" in c:
        return c.endswith(".md")
    if "/course/" in c and (c.endswith("bilan-course.json") or "propositions" in c or "accords" in c):
        return c.endswith(".json") or c.endswith(".md")
    return False


def extraire_branches_brutes(seen_paths: set[str]) -> None:
    main_files = set(
        subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "origin/main"], cwd=str(RACINE), text=True).splitlines()
    )
    # Normaliser les suffixes deja presents dans corpus 6213 (par exemple cellules de unites-v2.json)
    seen_suffixes = set()
    for sp in seen_paths:
        parts = sp.split("/")
        if len(parts) >= 3:
            seen_suffixes.add("/".join(parts[-3:]))

    docs_par_groupe: dict[str, list[dict]] = defaultdict(list)
    hashes_vus: set[str] = set()
    stats = Counter()

    for groupe, branche in BRANCHES_CIBLES:
        try:
            diff_files = subprocess.check_output(
                ["git", "diff", "--name-only", "--diff-filter=AM", f"origin/main...{branche}"],
                cwd=str(RACINE),
                text=True,
                stderr=subprocess.DEVNULL,
            ).splitlines()
        except subprocess.CalledProcessError:
            diff_files = [
                f
                for f in subprocess.check_output(["git", "ls-tree", "-r", "--name-only", branche], cwd=str(RACINE), text=True).splitlines()
                if f not in main_files
            ]

        for f in sorted(diff_files):
            if not est_doc_scientifique_cible(branche, f):
                continue
            fl = f.replace("\\", "/").lower()
            parts = fl.split("/")
            suf3 = "/".join(parts[-3:]) if len(parts) >= 3 else fl
            if fl in seen_paths or suf3 in seen_suffixes:
                stats["deja_dans_corpus_6213"] += 1
                continue
            try:
                txt = git_show(f"{branche}:{f}")
            except Exception:
                stats["erreur_lecture"] += 1
                continue
            if not txt.strip():
                continue
            # Verifier aussi le contenu contre la liste noire de dossiers sensibles
            if est_interdit(f) or "reponses-ne-pas-servir" in txt.lower():
                stats["filtre_liste_noire"] += 1
                continue
            h = sha256_str(txt)[:16]
            if h in hashes_vus:
                stats["doublon_inter_branches"] += 1
                continue
            hashes_vus.add(h)
            docs_par_groupe[groupe].append(
                {
                    "groupe": groupe,
                    "branche": branche.replace("origin/", ""),
                    "chemin": f,
                    "sha256_16": h,
                    "taille": len(txt),
                    "contenu": txt,
                }
            )
            stats[f"extrait_{groupe}"] += 1

    packs_dir = SCRATCH / "phase1_packs"
    packs_dir.mkdir(parents=True, exist_ok=True)
    # Nettoyer anciens packs si re-run
    for old in packs_dir.glob("pack_*.json"):
        old.unlink()

    manifest_packs = []
    pack_idx = 0
    for groupe, docs in sorted(docs_par_groupe.items()):
        # Decouper en packs de <= 45 000 caracteres et <= 10 documents pour une lecture parfaite par flash
        cur_docs = []
        cur_chars = 0
        for d in docs:
            # Tronquer un document monstrueux uniquement pour le pack si > 25 000 chars tout en gardant le debut+fin
            doc_copy = dict(d)
            if len(doc_copy["contenu"]) > 24000:
                doc_copy["contenu"] = doc_copy["contenu"][:18000] + "\n\n[... EXTRAIT INTERMEDIAIRE OMIS POUR TAILLE ...]\n\n" + doc_copy["contenu"][-5000:]
            if cur_docs and (cur_chars + len(doc_copy["contenu"]) > 42000 or len(cur_docs) >= 10):
                pack_idx += 1
                pp = packs_dir / f"pack_{pack_idx:03d}_{groupe}.json"
                pp.write_text(json.dumps(cur_docs, ensure_ascii=False, indent=1), encoding="utf-8")
                manifest_packs.append({"pack_id": f"pack_{pack_idx:03d}_{groupe}", "groupe": groupe, "path": str(pp), "n_docs": len(cur_docs), "chars": cur_chars})
                cur_docs, cur_chars = [], 0
            cur_docs.append(doc_copy)
            cur_chars += len(doc_copy["contenu"])
        if cur_docs:
            pack_idx += 1
            pp = packs_dir / f"pack_{pack_idx:03d}_{groupe}.json"
            pp.write_text(json.dumps(cur_docs, ensure_ascii=False, indent=1), encoding="utf-8")
            manifest_packs.append({"pack_id": f"pack_{pack_idx:03d}_{groupe}", "groupe": groupe, "path": str(pp), "n_docs": len(cur_docs), "chars": cur_chars})

    (SCRATCH / "phase1_manifest.json").write_text(
        json.dumps({"stats": dict(stats), "packs": manifest_packs}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("PHASE 1 STATS:", dict(stats))
    print(f"TOTAL PACKS: {len(manifest_packs)}")
    for mp in manifest_packs:
        print(f"  {mp['pack_id']}: {mp['n_docs']} docs, {mp['chars']} chars")


if __name__ == "__main__":
    _, seen_paths, _ = enrichir_corpus_6213()
    extraire_branches_brutes(seen_paths)
