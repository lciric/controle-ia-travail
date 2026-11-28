#!/usr/bin/env python3
"""Porte mecanique de verification 0 orphelin et conformite de la Bibliotheque scientifique canonique v1.

Verifie :
1. Couverture integrale (orphelins == 0) de tous les identifiants BIB-0001..BIB-N
   (corpus-unifie-idees-v1.jsonl + supplement-branches-brutes-v1.jsonl) dans les 4 registres.
2. Absence de tout identifiant fantome et coherence stricte des champs obligatoires.
3. Absence de tout caractere Windows NTFS interdit (< > : " | ? *) dans tous les chemins crees.
4. Absence d'emoji dans les fichiers scelles.
5. Absence de toute source issue de la liste noire de cloisonnement.
6. Produit CERTIFICAT-ZERO-ORPHELIN-v1.json.
"""
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
SUPP_FILE = DOSSIER / "supplement-branches-brutes-v1.jsonl"

REG_IDEES = DOSSIER / "idees-et-mecanismes-canoniques.jsonl"
REG_ACQUIS = DOSSIER / "acquis-empiriques-et-morts-connus.jsonl"
REG_OUTILS = DOSSIER / "outils-bancs-et-corpus.jsonl"
REG_ECARTS = DOSSIER / "ecartes-structurels-et-glossaires.jsonl"

CERTIFICAT = DOSSIER / "CERTIFICAT-ZERO-ORPHELIN-v1.json"

FORBIDDEN_WIN_CHARS = set('<>:"|?*')
EMOJI_RE = re.compile("[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+")

MOTIFS_INTERDITS = (
    "coffre/", "docs/verdicts/", "/verdict/", "verdict/", "reponses-ne-pas-servir",
    "protocole-x-attaquant-v1", "barreau8", "dose-reponse-consigne-cachee", "sondes-iib",
)

REQ_FIELDS_IDEE = (
    "id_canonique",
    "titre_clair_fr",
    "objet",
    "theme",
    "sous_theme",
    "enonce_complet",
    "mecanisme_causal",
    "genealogie_sources",
    "anteriorite_connue",
    "statut_epistemique",
    "regime_materiel",
    "esquisse_test_de_mort_et_faux_temoin",
)

VALID_STATUTS = {
    "vierge", "preenregistre_en_attente", "pris_en_charge_groupe_v1",
    "deja_valide_interne", "deja_refute_interne",
}
VALID_REGIMES = {
    "CPU_0_USD_SYNTHETIQUE", "CPU_DONNEES_PUBLIQUES_REEL",
    "GPU_VAST_8B_SOUS_GO", "MODELE_FERME_COURSE_ETAPE_2",
}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_jsonl(p: Path) -> list[dict]:
    if not p.is_file():
        raise FileNotFoundError(f"Fichier requis absent : {p}")
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def main() -> int:
    erreurs: list[str] = []

    base_rows = load_jsonl(CORPUS_BASE)
    supp_rows = load_jsonl(SUPP_FILE) if SUPP_FILE.is_file() else []

    expected_ids = [r["id_unifie"] for r in base_rows] + [r["id_unifie"] for r in supp_rows]
    expected_set = set(expected_ids)
    if len(expected_ids) != len(expected_set):
        erreurs.append(f"Doublon d'identifiants BIB dans l'entree ({len(expected_ids)} vs {len(expected_set)})")

    idees = load_jsonl(REG_IDEES)
    acquis = load_jsonl(REG_ACQUIS)
    outils = load_jsonl(REG_OUTILS)
    ecarts = load_jsonl(REG_ECARTS)

    # 1. Verifier couverture des BIB-xxxx dans les 4 registres
    occurrences_by_reg: dict[str, set[str]] = {
        "idees_et_mecanismes_canoniques": set(),
        "acquis_empiriques_et_morts_connus": set(),
        "outils_bancs_et_corpus": set(),
        "ecartes_structurels_et_glossaires": set(),
    }
    all_bib_counts: Counter = Counter()
    blacklisted_hits: list[str] = []

    for reg_name, rows in (
        ("idees_et_mecanismes_canoniques", idees),
        ("acquis_empiriques_et_morts_connus", acquis),
        ("outils_bancs_et_corpus", outils),
        ("ecartes_structurels_et_glossaires", ecarts),
    ):
        for idx, r in enumerate(rows):
            gen = r.get("genealogie_sources")
            if not isinstance(gen, list) or not gen:
                erreurs.append(f"{reg_name}[{idx}] : genealogie_sources vide ou absente")
                continue
            for g in gen:
                bid = g.get("id_bib")
                if not bid:
                    erreurs.append(f"{reg_name}[{idx}] : entree genealogie sans id_bib")
                    continue
                occurrences_by_reg[reg_name].add(bid)
                all_bib_counts[bid] += 1
                ch = f"{g.get('source_branche','')}/{g.get('source_chemin','')}".lower().replace("\\", "/")
                for m in MOTIFS_INTERDITS:
                    if m in ch:
                        blacklisted_hits.append(f"{bid}:{ch}")

    # 2. Verifier schema obligatoire sur idees canoniques
    for idx, it in enumerate(idees):
        for f in REQ_FIELDS_IDEE:
            val = it.get(f)
            if val is None or (isinstance(val, str) and not val.strip()):
                erreurs.append(f"IDEE[{idx}] ({it.get('id_canonique','?')}) : champ '{f}' vide ou absent")
        if it.get("statut_epistemique") not in VALID_STATUTS:
            erreurs.append(f"IDEE[{idx}] : statut_epistemique invalide {it.get('statut_epistemique')!r}")
        if it.get("regime_materiel") not in VALID_REGIMES:
            erreurs.append(f"IDEE[{idx}] : regime_materiel invalide {it.get('regime_materiel')!r}")

    covered_set = set(all_bib_counts.keys())
    orphelins = sorted(expected_set - covered_set)
    fantomes = sorted(covered_set - expected_set)
    multi_rattaches = sorted(k for k, v in all_bib_counts.items() if v > 1)

    if orphelins:
        erreurs.append(f"ORPHELINS DETECTES : {len(orphelins)} ({orphelins[:20]})")
    if fantomes:
        erreurs.append(f"IDENTIFIANTS FANTOMES : {len(fantomes)} ({fantomes[:20]})")
    if blacklisted_hits:
        erreurs.append(f"SOURCES LISTE NOIRE DETECTEES : {len(blacklisted_hits)} ({blacklisted_hits[:10]})")

    # 3. Verifier Windows NTFS paths & zero emojis dans le dossier
    bad_paths: list[str] = []
    emoji_files: list[str] = []
    for p in sorted(DOSSIER.rglob("*")):
        rel = p.relative_to(DOSSIER)
        for part in rel.parts:
            if any(c in FORBIDDEN_WIN_CHARS for c in part):
                bad_paths.append(str(rel))
        if p.is_file() and p.suffix in (".md", ".jsonl", ".json", ".py"):
            if p.name == "verifier_couverture_bibliotheque_v1.py":
                continue
            txt = p.read_text(encoding="utf-8")
            if EMOJI_RE.search(txt):
                emoji_files.append(str(rel))

    if bad_paths:
        erreurs.append(f"CHEMINS WINDOWS INTERDITS : {bad_paths}")
    if emoji_files:
        erreurs.append(f"EMOJIS DETECTES DANS : {emoji_files}")

    # 4. Verifier presence des fichiers Markdown obligatoires
    requis_md = [
        "LISEZMOI-BIBLIOTHEQUE-CANONIQUE-v1.md",
        "CATALOGUE-GENERAL-PAR-SUJET-ET-THEME-v1.md",
        "CATALOGUE-CROISE-PAR-SOURCE-ET-MODELE-v1.md",
        "acquis-empiriques-et-morts-connus.md",
        "outils-bancs-et-corpus.md",
        "rayons/01-metrologie-attelage-et-tests-de-mort.md",
        "rayons/02-architecture-organisme-memoire-et-autoconception.md",
        "rayons/03-mathematiques-nouvelles-3-graphes-et-hors-alphabet.md",
        "rayons/04-controle-ia-menaces-diffuses-et-sondes.md",
        "rayons/05-etalonnages-corpus-reels-et-gpu-8b.md",
    ]
    for rm in requis_md:
        if not (DOSSIER / rm).is_file():
            erreurs.append(f"LIVRABLE OBLIGATOIRE ABSENT : {rm}")

    certificat_data = {
        "version": "v1",
        "accord": "GO-2026-11-25-06",
        "horodatage_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "verdict": "VALIDE_ZERO_ORPHELIN" if not erreurs else "ECHEC",
        "total_entrees_corpus_base": len(base_rows),
        "total_entrees_supplement_branches": len(supp_rows),
        "total_entrees_attendues": len(expected_set),
        "total_entrees_couvertes": len(covered_set),
        "orphelins": len(orphelins),
        "identifiants_fantomes": len(fantomes),
        "entrees_rattachees_multi_fiches": len(multi_rattaches),
        "partition_strictement_disjointe": len(multi_rattaches) == 0 and len(orphelins) == 0 and len(fantomes) == 0,
        "comptes_registres": {
            "idees_et_mecanismes_canoniques": {
                "fiches": len(idees),
                "occurrences_bib_uniques": len(occurrences_by_reg["idees_et_mecanismes_canoniques"]),
            },
            "acquis_empiriques_et_morts_connus": {
                "fiches": len(acquis),
                "occurrences_bib_uniques": len(occurrences_by_reg["acquis_empiriques_et_morts_connus"]),
            },
            "outils_bancs_et_corpus": {
                "fiches": len(outils),
                "occurrences_bib_uniques": len(occurrences_by_reg["outils_bancs_et_corpus"]),
            },
            "ecartes_structurels_et_glossaires": {
                "fiches": len(ecarts),
                "occurrences_bib_uniques": len(occurrences_by_reg["ecartes_structurels_et_glossaires"]),
            },
        },
        "controles_conformite": {
            "chemins_windows_interdits": len(bad_paths),
            "fichiers_avec_emojis": len(emoji_files),
            "sources_liste_noire": len(blacklisted_hits),
            "livrables_obligatoires_presents": all((DOSSIER / rm).is_file() for rm in requis_md),
        },
        "empreintes_registres_sha256": {
            "corpus_base": sha256_file(CORPUS_BASE),
            "supplement_branches_brutes": sha256_file(SUPP_FILE) if SUPP_FILE.is_file() else "",
            "idees_et_mecanismes_canoniques": sha256_file(REG_IDEES),
            "acquis_empiriques_et_morts_connus": sha256_file(REG_ACQUIS),
            "outils_bancs_et_corpus": sha256_file(REG_OUTILS),
            "ecartes_structurels_et_glossaires": sha256_file(REG_ECARTS),
        },
        "erreurs": erreurs,
    }

    CERTIFICAT.write_text(json.dumps(certificat_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(certificat_data, ensure_ascii=False, indent=2))
    return 0 if not erreurs else 1


if __name__ == "__main__":
    sys.exit(main())
