#!/usr/bin/env python3
"""Porte mecanique 0 orphelin pour la Bibliotheque scientifique canonique v2 (union complete v1 + LIT-0001..2863)."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
RACINE = DOSSIER.parents[3]
CORPUS_BASE = RACINE / "docs/notes/bibliotheque/corpus-unifie-idees-v1/corpus-unifie-idees-v1.jsonl"
SUPP_V1 = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v1/supplement-branches-brutes-v1.jsonl"
SUPP_LIT = RACINE / "docs/notes/bibliotheque/supplement-litterature-et-lectures-v1/supplement-litterature-et-lectures-v1.jsonl"

REG_IDEES = DOSSIER / "idees-et-mecanismes-canoniques.jsonl"
REG_LIT = DOSSIER / "litterature-et-voisins-lus.jsonl"
REG_ACQUIS = DOSSIER / "acquis-empiriques-et-morts-connus.jsonl"
REG_OUTILS = DOSSIER / "outils-bancs-et-corpus.jsonl"
REG_ECARTS = DOSSIER / "ecartes-structurels-et-glossaires.jsonl"
CERTIFICAT = DOSSIER / "CERTIFICAT-ZERO-ORPHELIN-v2.json"

FORBIDDEN_WIN_CHARS = set('<>:"|?*')
EMOJI_RE = re.compile("[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+")
MOTIFS_INTERDITS = ("coffre/", "docs/verdicts/", "/verdict/", "verdict/", "reponses-ne-pas-servir", "sequestre", "protocole-x-attaquant-v1", "barreau8", "dose-reponse-consigne-cachee", "sondes-iib")


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def main() -> int:
    erreurs: list[str] = []
    base_rows = load_jsonl(CORPUS_BASE)
    v1_supp_rows = load_jsonl(SUPP_V1) if SUPP_V1.is_file() else []
    lit_rows = load_jsonl(SUPP_LIT)

    expected_bib = {r["id_unifie"] for r in base_rows} | {r["id_unifie"] for r in v1_supp_rows}
    expected_lit = {r["id_supplement"] for r in lit_rows}
    expected_all = expected_bib | expected_lit

    idees = load_jsonl(REG_IDEES)
    papers = load_jsonl(REG_LIT)
    acquis = load_jsonl(REG_ACQUIS)
    outils = load_jsonl(REG_OUTILS)
    ecarts = load_jsonl(REG_ECARTS)

    covered_by_reg: dict[str, set[str]] = {}
    all_covered: Counter = Counter()
    blacklisted: list[str] = []

    for rname, rows in (
        ("idees_et_mecanismes_canoniques", idees),
        ("litterature_et_voisins_lus", papers),
        ("acquis_empiriques_et_morts_connus", acquis),
        ("outils_bancs_et_corpus", outils),
        ("ecartes_structurels_et_glossaires", ecarts),
    ):
        s = set()
        for idx, r in enumerate(rows):
            gen = r.get("genealogie_sources") or []
            if not gen:
                erreurs.append(f"{rname}[{idx}] : genealogie_sources vide")
            for g in gen:
                bid = g.get("id_bib")
                if bid:
                    s.add(bid)
                    all_covered[bid] += 1
                ch = f"{g.get('source_branche','')}/{g.get('source_chemin','')}".lower().replace("\\", "/")
                for m in MOTIFS_INTERDITS:
                    if m in ch:
                        blacklisted.append(f"{bid}:{ch}")
        covered_by_reg[rname] = s

    covered_set = set(all_covered.keys())
    orphelins = sorted(expected_all - covered_set)
    orphelins_bib = sorted(expected_bib - covered_set)
    orphelins_lit = sorted(expected_lit - covered_set)
    fantomes = sorted(covered_set - expected_all)

    if orphelins:
        erreurs.append(f"ORPHELINS TOTAL: {len(orphelins)} (BIB={len(orphelins_bib)}, LIT={len(orphelins_lit)}) ex: {orphelins[:20]}")
    if fantomes:
        erreurs.append(f"FANTOMES: {len(fantomes)} ex: {fantomes[:20]}")
    if blacklisted:
        erreurs.append(f"LISTE NOIRE: {len(blacklisted)} ex: {blacklisted[:10]}")

    bad_paths, emoji_files = [], []
    for p in sorted(DOSSIER.rglob("*")):
        rel = p.relative_to(DOSSIER)
        if any(any(c in FORBIDDEN_WIN_CHARS for c in part) for part in rel.parts):
            bad_paths.append(str(rel))
        if p.is_file() and p.suffix in (".md", ".jsonl", ".json", ".py") and p.name != "verifier_couverture_bibliotheque_v2.py":
            if EMOJI_RE.search(p.read_text(encoding="utf-8")):
                emoji_files.append(str(rel))
    if bad_paths:
        erreurs.append(f"CHEMINS WINDOWS INTERDITS: {bad_paths}")
    if emoji_files:
        erreurs.append(f"EMOJIS DETECTES: {emoji_files}")

    requis = [
        "LISEZMOI-BIBLIOTHEQUE-CANONIQUE-v2.md",
        "CATALOGUE-GENERAL-PAR-SUJET-ET-THEME-v2.md",
        "CATALOGUE-LITTERATURE-ET-VOISINS-PAR-THEME-v2.md",
        "CATALOGUE-CROISE-PAR-SOURCE-ET-MODELE-v2.md",
        "litterature-et-voisins-lus.md",
        "acquis-empiriques-et-morts-connus.md",
        "outils-bancs-et-corpus.md",
        "rayons/01-metrologie-attelage-et-tests-de-mort.md",
        "rayons/02-architecture-organisme-memoire-et-autoconception.md",
        "rayons/03-mathematiques-nouvelles-3-graphes-et-hors-alphabet.md",
        "rayons/04-controle-ia-menaces-diffuses-et-sondes.md",
        "rayons/05-etalonnages-corpus-reels-et-gpu-8b.md",
    ]
    for rm in requis:
        if not (DOSSIER / rm).is_file():
            erreurs.append(f"LIVRABLE ABSENT: {rm}")

    cert = {
        "version": "v2",
        "accord": "GO-2026-11-25-06",
        "horodatage_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "verdict": "VALIDE_ZERO_ORPHELIN" if not erreurs else "ECHEC",
        "total_entrees_bib_v1": len(expected_bib),
        "total_entrees_lit_supplement": len(expected_lit),
        "total_entrees_attendues_union": len(expected_all),
        "total_entrees_couvertes": len(covered_set),
        "orphelins": len(orphelins),
        "orphelins_bib": len(orphelins_bib),
        "orphelins_lit": len(orphelins_lit),
        "identifiants_fantomes": len(fantomes),
        "comptes_registres": {
            "idees_et_mecanismes_canoniques": {"fiches": len(idees), "occurrences_uniques": len(covered_by_reg["idees_et_mecanismes_canoniques"])},
            "litterature_et_voisins_lus": {"fiches": len(papers), "occurrences_uniques": len(covered_by_reg["litterature_et_voisins_lus"])},
            "acquis_empiriques_et_morts_connus": {"fiches": len(acquis), "occurrences_uniques": len(covered_by_reg["acquis_empiriques_et_morts_connus"])},
            "outils_bancs_et_corpus": {"fiches": len(outils), "occurrences_uniques": len(covered_by_reg["outils_bancs_et_corpus"])},
            "ecartes_structurels_et_glossaires": {"fiches": len(ecarts), "occurrences_uniques": len(covered_by_reg["ecartes_structurels_et_glossaires"])},
        },
        "controles_conformite": {
            "chemins_windows_interdits": len(bad_paths),
            "fichiers_avec_emojis": len(emoji_files),
            "sources_liste_noire": len(blacklisted),
            "livrables_obligatoires_presents": all((DOSSIER / rm).is_file() for rm in requis),
        },
        "empreintes_registres_sha256": {
            "idees_et_mecanismes_canoniques": sha256_file(REG_IDEES),
            "litterature_et_voisins_lus": sha256_file(REG_LIT),
            "acquis_empiriques_et_morts_connus": sha256_file(REG_ACQUIS),
            "outils_bancs_et_corpus": sha256_file(REG_OUTILS),
            "ecartes_structurels_et_glossaires": sha256_file(REG_ECARTS),
        },
        "erreurs": erreurs,
    }
    CERTIFICAT.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(cert, ensure_ascii=False, indent=2))
    return 0 if not erreurs else 1


if __name__ == "__main__":
    sys.exit(main())
