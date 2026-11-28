#!/usr/bin/env python3
"""Fusionne BIB-0001..BIB-6213 + supplement Phase 1 (BIB-6214..BIB-N) et decoupe en lots <= 160 entrees pour Phase 2A."""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(r"C:\Users\lciri\wt-organisme-boucle-fermee")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")
OUT_DIR = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v1"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MOTIFS_INTERDITS = (
    "coffre/", "docs/verdicts/", "/verdict/", "verdict/", "reponses-ne-pas-servir",
    "protocole-x-attaquant-v1", "evasion-moniteurs", "modes-et-attaques", "modes-attaque",
    "modes-v8", "organismes-discrets", "lot-quarantaine", "taches-sabotage",
    "conscience-anesthesie-v3-reserve", "verite-dommage", "tableau-partage", "questions-fortes",
    "bras-attaque", "attaque-goodhart", "barreau8", "barreau5", "dose-reponse",
    "sondes-iib", "versant-honnete", "sondes-v2", "modes-attaque-reponse-24",
)

EMOJI_RE = re.compile("[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+")


def clean_no_emoji(s: str) -> str:
    s = EMOJI_RE.sub("", s or "")
    return re.sub(r"\s+", " ", s).strip()


def est_interdit(s: str) -> bool:
    t = (s or "").replace("\\", "/").lower()
    return any(m in t for m in MOTIFS_INTERDITS)


def sha16(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def main() -> None:
    base_rows = [
        json.loads(l)
        for l in (SCRATCH / "corpus_enrichi_6213.jsonl").read_text(encoding="utf-8").splitlines()
        if l.strip()
    ]
    assert len(base_rows) == 6213, f"Expected 6213 base rows, got {len(base_rows)}"

    seen_keys = {r["cle_contenu"] for r in base_rows}
    seen_titles = {clean_no_emoji(r.get("titre", "")).lower()[:120] for r in base_rows}

    p1_dir = SCRATCH / "phase1_outputs"
    supp_rows = []
    next_idx = 6214
    skipped_dup = 0
    skipped_bad = 0

    for pf in sorted(p1_dir.glob("p1_*.json")):
        data = json.loads(pf.read_text(encoding="utf-8"))
        entries = data.get("entrees", []) if isinstance(data, dict) else data
        for it in entries:
            if not isinstance(it, dict):
                continue
            chemin = clean_no_emoji(it.get("source_chemin", ""))
            branche = clean_no_emoji(it.get("source_branche", ""))
            titre = clean_no_emoji(it.get("titre", ""))
            enonce = clean_no_emoji(it.get("enonce", ""))
            if not titre and not enonce:
                continue
            if est_interdit(chemin) or est_interdit(branche) or est_interdit(titre) or est_interdit(enonce[:200]):
                skipped_bad += 1
                continue
            cle = sha16(f"{branche}|{chemin}|{titre[:120]}|{enonce[:240]}")
            tkey = titre.lower()[:120]
            if cle in seen_keys or (len(tkey) > 35 and tkey in seen_titles):
                skipped_dup += 1
                continue
            seen_keys.add(cle)
            seen_titles.add(tkey)

            bib_id = f"BIB-{next_idx:04d}"
            next_idx += 1
            rec = {
                "id_unifie": bib_id,
                "cle_contenu": cle,
                "id_origine": clean_no_emoji(it.get("id_origine", "")) or f"SUPP-{next_idx-1}",
                "titre": titre[:280],
                "enonce": enonce,
                "enonce_complet_brut": enonce,
                "anteriorite_brute": clean_no_emoji(it.get("anteriorite", "")),
                "objet": it.get("objet") or "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
                "theme": it.get("theme") or "2E. Topologie des roles (cartographe, proposeurs, refutateurs, experimentateurs)",
                "famille_source": it.get("famille_source") or "S12_Supplement_Branches_Brutes_Phase1",
                "espece_auteur": clean_no_emoji(it.get("espece_auteur", "")) or "non_specifie",
                "source_chemin": chemin,
                "source_branche": branche,
                "statut": clean_no_emoji(it.get("statut", "")) or "extrait_branche_brute",
                "regime_execution": it.get("regime_execution") or "CPU_0_USD_SYNTHETIQUE",
            }
            supp_rows.append(rec)

    # Ecrire supplement-branches-brutes-v1.jsonl dans catalogue-canonique-v1/
    supp_path = OUT_DIR / "supplement-branches-brutes-v1.jsonl"
    supp_out_lines = []
    for r in supp_rows:
        pub = {
            "id_unifie": r["id_unifie"],
            "cle_contenu": r["cle_contenu"],
            "id_origine": r["id_origine"],
            "titre": r["titre"],
            "enonce": r["enonce"],
            "objet": r["objet"],
            "theme": r["theme"],
            "famille_source": r["famille_source"],
            "espece_auteur": r["espece_auteur"],
            "source_chemin": r["source_chemin"],
            "source_branche": r["source_branche"],
            "statut": r["statut"],
            "regime_execution": r["regime_execution"],
        }
        supp_out_lines.append(json.dumps(pub, ensure_ascii=False))
    supp_path.write_text("\n".join(supp_out_lines) + ("\n" if supp_out_lines else ""), encoding="utf-8")

    all_rows = base_rows + supp_rows
    master_path = SCRATCH / "corpus_total_enrichi.jsonl"
    master_path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in all_rows) + "\n", encoding="utf-8")

    # Regrouper par (objet, theme) et decouper en lots <= 160 entrees
    by_ot = defaultdict(list)
    for r in all_rows:
        by_ot[(r["objet"], r["theme"])].append(r)

    batches_dir = SCRATCH / "phase2_batches"
    batches_dir.mkdir(parents=True, exist_ok=True)
    for old in batches_dir.glob("batch_*.jsonl"):
        old.unlink()

    MAX_BATCH = 155
    manifest = []
    b_idx = 0
    for (obj, th), items in sorted(by_ot.items()):
        # Trier par famille_source puis titre pour rapprocher les doublons dans le meme lot
        items.sort(key=lambda x: (x.get("famille_source", ""), x.get("titre", "").lower()))
        for start in range(0, len(items), MAX_BATCH):
            chunk = items[start : start + MAX_BATCH]
            b_idx += 1
            bid = f"batch_{b_idx:03d}"
            bp = batches_dir / f"{bid}.jsonl"
            compact_lines = []
            for r in chunk:
                c = {
                    "id_unifie": r["id_unifie"],
                    "id_origine": r.get("id_origine", ""),
                    "objet": r.get("objet", ""),
                    "theme": r.get("theme", ""),
                    "famille_source": r.get("famille_source", ""),
                    "espece_auteur": r.get("espece_auteur", ""),
                    "anteriorite": r.get("anteriorite_brute", ""),
                    "titre": clean_no_emoji(r.get("titre", "")),
                    "enonce_complet": clean_no_emoji(r.get("enonce_complet_brut") or r.get("enonce", "")),
                    "statut": r.get("statut", ""),
                    "regime_execution": r.get("regime_execution", ""),
                    "source_chemin": r.get("source_chemin", ""),
                    "source_branche": r.get("source_branche", ""),
                }
                compact_lines.append(json.dumps(c, ensure_ascii=False))
            bp.write_text("\n".join(compact_lines) + "\n", encoding="utf-8")
            manifest.append({
                "batch_id": bid,
                "objet": obj,
                "theme": th,
                "count": len(chunk),
                "path": str(bp),
                "first_bib": chunk[0]["id_unifie"],
                "last_bib": chunk[-1]["id_unifie"],
            })

    (SCRATCH / "phase2_manifest.json").write_text(
        json.dumps(
            {
                "total_base": len(base_rows),
                "total_supplement": len(supp_rows),
                "total_all": len(all_rows),
                "skipped_dup": skipped_dup,
                "skipped_bad": skipped_bad,
                "n_batches": len(manifest),
                "batches": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"PHASE 2 BATCHES READY: base={len(base_rows)} + supp={len(supp_rows)} = {len(all_rows)} entries -> {len(manifest)} batches (dup={skipped_dup}, bad={skipped_bad})")


if __name__ == "__main__":
    main()
