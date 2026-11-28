#!/usr/bin/env python3
"""Workflow Python orchestre (/run-workflow) v2 : pure read_file + finish(schema) + sauvegarde/validation Python in-process."""
import hashlib
import json
import math
import re
import runpy
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(r"C:\Users\lciri\wt-organisme-boucle-fermee")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")

P1_OUT = SCRATCH / "phase1_outputs"
P2_OUT = SCRATCH / "phase2_curated"
P2B_DEC = SCRATCH / "phase2b_decisions"
P1_OUT.mkdir(parents=True, exist_ok=True)
P2_OUT.mkdir(parents=True, exist_ok=True)
P2B_DEC.mkdir(parents=True, exist_ok=True)

# Quota des niveaux "flash" et "pro" epuise (HTTP 429, remise a zero vers le 1er decembre) : les lots restants
# passent au niveau leger disponible ; chaque lot garde la trace du modele qui l'a cure.
MODEL_LOTS = "inherit"  # Opus 5.5 seulement (mot de Lazar du 26 novembre, 04:20)

VALID_OBJETS = [
    "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT",
    "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
    "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET",
    "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES",
    "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B",
]
VALID_STATUTS = [
    "vierge",
    "preenregistre_en_attente",
    "pris_en_charge_groupe_v1",
    "deja_valide_interne",
    "deja_refute_interne",
]
VALID_REGIMES = [
    "CPU_0_USD_SYNTHETIQUE",
    "CPU_DONNEES_PUBLIQUES_REEL",
    "GPU_VAST_8B_SOUS_GO",
    "MODELE_FERME_COURSE_ETAPE_2",
]
EMOJI_RE = re.compile("[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+")

THEMES_GUIDE = """OBJETS ET THEMES CANONIQUES :
- OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT :
  * 1A. Certification d'etroitesse, borne de handicap et controles actifs (CN-1, CN-2)
  * 1B. Profondeur par resolveur mecanique, micromondes plantes et tests de mort
  * 1C. Canonicalisation, nomination scellee, intersection-union et calibration bayesienne
  * 1D. Gouvernance experimentale, neutralisation des juges et audit du Protocole X
- OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION :
  * 2A. Auto-conception, greffons d'architecture et porte transactionnelle
  * 2B. Memoire negative des morts, heritage inter-generations et controle 2x2
  * 2C. Cinetique des collisions d'idees, catalyse, percolation et recombinaison
  * 2D. Allocation de budget, melange defensif sans modele et diversite fabriquee
  * 2E. Topologie des roles (cartographe, proposeurs, refutateurs, experimentateurs)
- OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET :
  * 3A. Sortie de l'alphabet, obstructions d'alignement et reification sur les trois graphes
  * 3B. Operateur de scission conceptuelle et detection des faux amalgames
  * 3C. Compression inter-bassins (MDL / Stitch), macros et arbres d'operateurs
  * 3D. Recherche de correspondances en puits etroit (spectral, transport optimal, typage)
  * 3E. Verification formelle Lean 4 et cibles mathematiques ouvertes
  * 3F. Hypergraphe fusionne a quatre couches et couche des problemes ouverts
- OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES :
  * 4A. Dynamique d'entrainement, ecriture de poids et tenue des garanties
  * 4B. Sondes internes, lentilles et sas de reapprentissage sous adversaire
  * 4C. Surveillance d'essaims, copies a memes poids et alea partage
  * 4D. Audit sequentiel, dommages plantes et architecture du controle diffus
- OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B :
  * 5A. Graphes biomedicaux dates et polarites causales (PubTator 3)
  * 5B. Surface contre structure sur notes d'experts et graphe dynamique (Gu et Krenn 2026)
  * 5C. Signal interne d'erreur de prediction (dopamine H10) et compression 8B sur GPU Vast.ai (T4)
  * 5D. Retrodictions sur archives scientifiques datees (cit-HepTh, OpenAlex, arXiv)
"""


def chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i : i + size]


def strip_emoji_recursive(obj):
    if isinstance(obj, str):
        return EMOJI_RE.sub("", obj).strip()
    if isinstance(obj, list):
        return [strip_emoji_recursive(x) for x in obj]
    if isinstance(obj, dict):
        return {k: strip_emoji_recursive(v) for k, v in obj.items()}
    return obj


# ==============================================================================
# PHASE 1 : Complement d'ingestion brute sans perte (model="flash" en parallele)
# ==============================================================================
phase("Phase 1 - Ingestion branches brutes restantes (flash)")

P1_SCHEMA = {
    "type": "object",
    "properties": {
        "pack_id": {"type": "string"},
        "entrees": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id_origine": {"type": "string"},
                    "titre": {"type": "string"},
                    "enonce": {"type": "string"},
                    "anteriorite": {"type": "string"},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "espece_auteur": {"type": "string"},
                    "source_chemin": {"type": "string"},
                    "source_branche": {"type": "string"},
                    "statut": {"type": "string"},
                    "regime_execution": {"type": "string"},
                },
                "required": ["id_origine", "titre", "enonce", "objet", "theme", "espece_auteur", "source_chemin", "source_branche"],
            },
        },
    },
    "required": ["pack_id", "entrees"],
}

p1_manifest = json.loads((SCRATCH / "phase1_38k_manifest.json").read_text(encoding="utf-8"))
todo_p1 = [m for m in p1_manifest if not (P1_OUT / f"{m['pack_id']}.json").is_file()]
log(f"Phase 1: {len(p1_manifest)} packs total (<=38Ko), {len(todo_p1)} a extraire.")


async def run_p1_pack(m):
    pid = m["pack_id"]
    out_file = P1_OUT / f"{pid}.json"
    prompt = f"""Extraction brute sans perte pour Phase 1 de la Bibliotheque scientifique canonique ({pid}).

INSTRUCTIONS STRICTES D'OUTILS :
- Appelle UNIQUEMENT `read_file` sur `{m['path']}` (taille <= 38 Ko, lisible en un seul appel), puis retourne DIRECTEMENT le resultat structure via l'outil `finish`.
- N'appelle JAMAIS `run_command` ni `write_file`.

TA MISSION :
Pour chaque document de `{m['path']}` ({m['n_docs']} documents du groupe `{m['groupe']}`), extrais les idees scientifiques, hypotheses, mecanismes, architectures, criteres testables ou constats/outils distincts qui y figurent (sans dupliquer mot pour mot a l'interieur du pack ; garde des enonces fideles, clairs et complets en francais scientifique, ZERO emoji).
- Recopie exactement `source_branche` et `source_chemin` de chaque document.
- Identifie l'auteur ou modele exact dans `espece_auteur` (Fable 5.2, Fable 5.1, Opus 5.5, Carbon, Neon, Argon, Astra, Kimi, Lazar, ou espece exacte indiquee).
- Titre scientifique clair en francais avant tout code entre parentheses.

{THEMES_GUIDE}"""

    last_err = None
    for attempt in range(2):
        try:
            res = await agent(
                prompt,
                schema=P1_SCHEMA,
                role=f"Phase 1 {pid}" + ("" if attempt == 0 else " (retry)"),
                model="flash",
                workspace="inherit",
            )
            break
        except Exception as exc:
            last_err = exc
            log(f"  [retry] {pid} attempt {attempt+1} failed: {exc}")
    else:
        raise last_err
    res = strip_emoji_recursive(res)
    for e in res.get("entrees", []):
        e["famille_source"] = f"S12_Supplement_{m['groupe']}"
    out_file.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(res.get("entrees", []))


for wave_idx, wave in enumerate(chunks(todo_p1, 10), 1):
    log(f"Phase 1 vague {wave_idx}/{(len(todo_p1)+9)//10}: {len(wave)} packs")
    counts = await parallel(wave, run_p1_pack)
    log(f"  -> extraites dans cette vague: {sum(counts)} entrees")

# Fusionner BIB-0001..BIB-6213 + supplement BIB-6214..BIB-N et decouper en lots <= 72 entrees (<= 38 Ko chacun!)
if not (SCRATCH / "phase2_manifest.json").is_file():
    log("Construction de supplement-branches-brutes-v1.jsonl et decoupage en lots <= 72 entrees (<= 38 Ko)...")
    runpy.run_path(str(SCRATCH / "build_phase2_batches_38k.py"), run_name="__main__")
else:
    log("Reprise : phase2_manifest.json et supplement-branches-brutes-v1.jsonl deja presents.")


# ==============================================================================
# PHASE 2A : Curation et dedoublonnage par lots <= 72 entrees (model="flash")
# ==============================================================================
phase("Phase 2A - Curation par lots <= 72 entrees (flash)")

P2_SCHEMA = {
    "type": "object",
    "properties": {
        "idees_canoniques": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "bib_ids": {"type": "array", "items": {"type": "string"}},
                    "titre_clair_fr": {"type": "string"},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "sous_theme": {"type": "string"},
                    "enonce_complet": {"type": "string"},
                    "mecanisme_causal": {"type": "string"},
                    "anteriorite_connue": {"type": "string"},
                    "statut_epistemique": {"type": "string", "enum": VALID_STATUTS},
                    "regime_materiel": {"type": "string", "enum": VALID_REGIMES},
                    "esquisse_test_de_mort_et_faux_temoin": {"type": "string"},
                },
                "required": [
                    "bib_ids", "titre_clair_fr", "objet", "theme", "sous_theme",
                    "enonce_complet", "mecanisme_causal", "anteriorite_connue",
                    "statut_epistemique", "regime_materiel", "esquisse_test_de_mort_et_faux_temoin",
                ],
            },
        },
        "acquis_et_morts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "bib_ids": {"type": "array", "items": {"type": "string"}},
                    "titre_clair_fr": {"type": "string"},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "type_acquis": {"type": "string"},
                    "enonce_complet": {"type": "string"},
                    "motif_ou_resultat": {"type": "string"},
                },
                "required": ["bib_ids", "titre_clair_fr", "objet", "theme", "type_acquis", "enonce_complet", "motif_ou_resultat"],
            },
        },
        "outils_bancs_corpus": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "bib_ids": {"type": "array", "items": {"type": "string"}},
                    "titre_clair_fr": {"type": "string"},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "type_outil": {"type": "string"},
                    "description_complete": {"type": "string"},
                },
                "required": ["bib_ids", "titre_clair_fr", "objet", "theme", "type_outil", "description_complete"],
            },
        },
        "ecartes_structurels": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "bib_ids": {"type": "array", "items": {"type": "string"}},
                    "motif_ecart": {"type": "string"},
                    "resume_court": {"type": "string"},
                },
                "required": ["bib_ids", "motif_ecart", "resume_court"],
            },
        },
    },
    "required": ["idees_canoniques", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"],
}


def check_batch_partition(data: dict, expected_ids: list[str]) -> tuple[list[str], list[str], list[str]]:
    exp_set = set(expected_ids)
    seen = []
    for reg in ("idees_canoniques", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"):
        for it in data.get(reg) or []:
            seen.extend(it.get("bib_ids") or [])
    c = Counter(seen)
    missing = sorted(exp_set - set(c.keys()))
    extra = sorted(set(c.keys()) - exp_set)
    dups = sorted(k for k, v in c.items() if v > 1)
    return missing, extra, dups


def sanitize_and_repair_minor(data: dict, expected_ids: list[str]) -> dict:
    """Nettoie emojis, retire les extra/dups eventuels (garde premiere occurrence) sans rien inventer."""
    data = strip_emoji_recursive(data)
    exp_set = set(expected_ids)
    used = set()
    for reg in ("idees_canoniques", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"):
        cleaned_list = []
        for it in data.get(reg) or []:
            new_bids = []
            for b in it.get("bib_ids") or []:
                if b in exp_set and b not in used:
                    used.add(b)
                    new_bids.append(b)
            if new_bids:
                it["bib_ids"] = new_bids
                cleaned_list.append(it)
        data[reg] = cleaned_list
    return data


def batch_file_ok(b: dict) -> bool:
    p = P2_OUT / f"{b['batch_id']}.json"
    if not p.is_file():
        return False
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        exp = [json.loads(l)["id_unifie"] for l in Path(b["path"]).read_text(encoding="utf-8").splitlines() if l.strip()]
        m, e, dp = check_batch_partition(d, exp)
        return not m and not e and not dp
    except Exception:
        return False


p2_manifest = json.loads((SCRATCH / "phase2_manifest.json").read_text(encoding="utf-8"))
batches = p2_manifest["batches"]
todo_p2 = [b for b in batches if not batch_file_ok(b)]
log(f"Phase 2A: {len(batches)} lots total ({p2_manifest['total_all']} entrees brutes), {len(todo_p2)} a curer.")


async def run_p2_batch(b):
    bid = b["batch_id"]
    out_file = P2_OUT / f"{bid}.json"
    expected_ids = [json.loads(l)["id_unifie"] for l in Path(b["path"]).read_text(encoding="utf-8").splitlines() if l.strip()]

    prompt = f"""Curation scientifique et dedoublonnage semantique du lot `{bid}` ({len(expected_ids)} entrees brutes).

INSTRUCTIONS STRICTES D'OUTILS :
- Appelle UNIQUEMENT `read_file` sur `{b['path']}` (taille <= 38 Ko, lisible en un seul appel), puis retourne DIRECTEMENT le JSON structure via l'outil `finish`.
- N'appelle JAMAIS `run_command` ni `write_file`.

PARTITION STRICTE SANS PERTE (0 ORPHELIN) :
Chaque identifiant `id_unifie` ({', '.join(expected_ids[:5])} ... {expected_ids[-1]}, soit EXACTEMENT {len(expected_ids)} identifiants) doit apparaitre dans `bib_ids` d'EXACTEMENT UN des 4 registres :
1. `idees_canoniques` : vraies idees, hypotheses, operateurs, architectures ou criteres testables. FUSIONNE toutes les reformulations/repetitions d'une meme idee dans ce lot en UNE SEULE fiche.
   - `titre_clair_fr` : titre scientifique explicite en francais AVANT tout code entre parentheses (R-3044, R-5226).
   - `objet` : reclassifie dans le VRAI Objet parmi les 5 Objets (corrige les erreurs du corpus brut !).
   - `theme` : un des themes canoniques exacts ci-dessous.
   - `sous_theme` : sous-theme scientifique concis en francais (2 a 7 mots).
   - `enonce_complet` : enonce scientifique complet, propre, non tronque en francais.
   - `mecanisme_causal` : mecanisme causal clair expliquant comment/pourquoi l'idee agit.
   - `anteriorite_connue` : travaux publies / references arXiv cites (ou "" si aucun).
   - `statut_epistemique` : `vierge` | `preenregistre_en_attente` | `pris_en_charge_groupe_v1` | `deja_valide_interne` | `deja_refute_interne`.
   - `regime_materiel` : `CPU_0_USD_SYNTHETIQUE` | `CPU_DONNEES_PUBLIQUES_REEL` | `GPU_VAST_8B_SOUS_GO` | `MODELE_FERME_COURSE_ETAPE_2`.
   - `esquisse_test_de_mort_et_faux_temoin` : test de mort mecanique + faux temoin `1b`.
2. `acquis_et_morts` : constats deja tranches, theoremes deja prouves ou pistes deja refutees (`type_acquis`: `constat_tranche` | `theoreme_prouve` | `piste_refutee`).
3. `outils_bancs_corpus` : jeux de donnees publics, scripts, logiciels ou bancs existants (`type_outil`: `jeu_de_donnees` | `script_ou_code` | `banc_experimental`).
4. `ecartes_structurels` : glossaires, en-tetes de tableaux, rappels administratifs ou fragments sans idee scientifique propre (tu peux grouper plusieurs BIB au meme `motif_ecart`).

ZERO emoji nulle part. Verifie mentalement que les {len(expected_ids)} `BIB-...` sont TOUS inclus avant d'appeler `finish`.

{THEMES_GUIDE}"""

    last_err = None
    for attempt in range(3):
        try:
            cur = agent(role=f"Phase 2A {bid}" + ("" if attempt == 0 else f" (retry {attempt})"), model=MODEL_LOTS, workspace="inherit")
            res = await cur(prompt, schema=P2_SCHEMA)
            res = sanitize_and_repair_minor(res, expected_ids)
            missing, extra, dups = check_batch_partition(res, expected_ids)

            # Si des BIB manquent, un tour de complement cible uniquement sur les manquants !
            if missing:
                miss_prompt = (
                    f"Il manque EXACTEMENT {len(missing)} identifiants BIB dans ta sortie : {missing}. "
                    f"Ne repete PAS les autres. Classe UNIQUEMENT ces {len(missing)} identifiants manquants dans le meme schema JSON (les autres listes peuvent etre vides) et appelle `finish`."
                )
                patch = await cur(miss_prompt, schema=P2_SCHEMA)
                patch = sanitize_and_repair_minor(patch, missing)
                for reg in ("idees_canoniques", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"):
                    res[reg].extend(patch.get(reg) or [])
                res = sanitize_and_repair_minor(res, expected_ids)
                missing, extra, dups = check_batch_partition(res, expected_ids)

            del cur
            if missing:
                raise RuntimeError(f"Batch {bid} still missing {len(missing)} BIBs after complement turn: {missing[:15]}")
            break
        except Exception as exc:
            last_err = exc
            log(f"  [retry] {bid} attempt {attempt+1} failed: {exc}")
    else:
        log(f"  [ECHEC DURABLE] {bid} : {last_err} (lot laisse pour une reprise ulterieure)")
        return (0, 0, 0, 0)

    res["modele_curation"] = MODEL_LOTS
    out_file.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return (len(res["idees_canoniques"]), len(res["acquis_et_morts"]), len(res["outils_bancs_corpus"]), len(res["ecartes_structurels"]))


for wave_idx, wave in enumerate(chunks(todo_p2, 14), 1):
    log(f"Phase 2A vague {wave_idx}/{(len(todo_p2)+13)//14}: {[b['batch_id'] for b in wave]}")
    stats = await parallel(wave, run_p2_batch)
    log(f"  -> idees={sum(s[0] for s in stats)}, acquis={sum(s[1] for s in stats)}, outils={sum(s[2] for s in stats)}, ecarts={sum(s[3] for s in stats)}")

restants = [b["batch_id"] for b in batches if not batch_file_ok(b)]
if restants:
    raise RuntimeError(f"Phase 2A incomplete : {len(restants)} lots non valides ({restants}). Relancer le workflow (reprise idempotente).")

# Agreger Phase 2A et preparer Phase 2B (fichiers <= 38 Ko par morceaux pour lecture directe)
log("Agregation Phase 2A et calcul des paires de doublons Phase 2B...")
runpy.run_path(str(SCRATCH / "build_phase2b_inputs.py"), run_name="__main__")


# ==============================================================================
# PHASE 2B : Conservateur par Objet (model="inherit", 5 agents en parallele)
# ==============================================================================
phase("Phase 2B - Conservateurs par Objet (inherit)")

P2B_SCHEMA = {
    "type": "object",
    "properties": {
        "objet": {"type": "string"},
        "merges_idees": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "keep_id": {"type": "string"},
                    "merge_ids": {"type": "array", "items": {"type": "string"}},
                    "upgraded_titre_clair_fr": {"type": "string"},
                    "upgraded_sous_theme": {"type": "string"},
                    "upgraded_enonce_complet": {"type": "string"},
                    "upgraded_mecanisme_causal": {"type": "string"},
                    "upgraded_statut_epistemique": {"type": "string"},
                    "upgraded_regime_materiel": {"type": "string"},
                    "upgraded_esquisse_test_de_mort_et_faux_temoin": {"type": "string"},
                },
                "required": ["keep_id", "merge_ids"],
            },
        },
        "merges_acquis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"keep_id": {"type": "string"}, "merge_ids": {"type": "array", "items": {"type": "string"}}},
                "required": ["keep_id", "merge_ids"],
            },
        },
        "merges_outils": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"keep_id": {"type": "string"}, "merge_ids": {"type": "array", "items": {"type": "string"}}},
                "required": ["keep_id", "merge_ids"],
            },
        },
        "reclassifications": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "temp_id": {"type": "string"},
                    "target_register": {"type": "string"},
                    "objet": {"type": "string"},
                    "theme": {"type": "string"},
                    "motif": {"type": "string"},
                },
                "required": ["temp_id", "target_register"],
            },
        },
        "upgrades": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "temp_id": {"type": "string"},
                    "titre_clair_fr": {"type": "string"},
                    "sous_theme": {"type": "string"},
                    "theme": {"type": "string"},
                },
                "required": ["temp_id"],
            },
        },
    },
    "required": ["objet", "merges_idees", "merges_acquis", "merges_outils", "reclassifications", "upgrades"],
}

# Decouper chaque OBJ-X.json en tranches <= 36 Ko (paires + index des fiches) pour lecture 100% par read_file
p2b_chunks_dir = SCRATCH / "phase2b_chunks"
p2b_chunks_dir.mkdir(parents=True, exist_ok=True)
obj_files_map = {}
for obj_key in VALID_OBJETS:
    raw = json.loads((SCRATCH / "phase2b_inputs" / f"{obj_key}.json").read_text(encoding="utf-8"))
    parts = []
    # Part 0 : compteurs + toutes les paires near_duplicate (en 1 ou plusieurs fichiers <= 36 Ko)
    pairs_payload = {
        "objet": obj_key,
        "counts": raw["counts"],
        "near_duplicate_pairs_idees": raw["near_duplicate_pairs_idees"],
        "near_duplicate_pairs_acquis": raw["near_duplicate_pairs_acquis"],
        "near_duplicate_pairs_outils": raw["near_duplicate_pairs_outils"],
    }
    p0 = p2b_chunks_dir / f"{obj_key}_00_pairs.json"
    p0.write_text(json.dumps(pairs_payload, ensure_ascii=False, indent=1), encoding="utf-8")
    parts.append(str(p0))

    # Parts 1..k : liste compacte de toutes les idees (titre + theme + sous_theme + n_bibs) en tranches <= 36 Ko
    slim_idees = [
        {
            "temp_id": x["temp_id"],
            "theme": x["theme"],
            "sous_theme": x["sous_theme"],
            "titre_clair_fr": x["titre_clair_fr"],
            "statut": x["statut_epistemique"],
            "regime": x["regime_materiel"],
            "n_bibs": x["n_bibs"],
        }
        for x in raw["idees"]
    ]
    cur, p_idx = [], 1
    for it in slim_idees:
        cand = cur + [it]
        if cur and len(json.dumps(cand, ensure_ascii=False).encode("utf-8")) > 35000:
            pf = p2b_chunks_dir / f"{obj_key}_{p_idx:02d}_idees.json"
            pf.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
            parts.append(str(pf))
            p_idx += 1
            cur = [it]
        else:
            cur = cand
    if cur:
        pf = p2b_chunks_dir / f"{obj_key}_{p_idx:02d}_idees.json"
        pf.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
        parts.append(str(pf))
    obj_files_map[obj_key] = parts

todo_obj = [o for o in VALID_OBJETS if not (P2B_DEC / f"{o}.json").is_file()]


async def run_conservator(obj_key):
    out_path = P2B_DEC / f"{obj_key}.json"
    files_list = "\n".join(f"- `{p}`" for p in obj_files_map[obj_key])
    prompt = f"""Role : Conservateur scientifique senior (`model="inherit"`) pour `{obj_key}`.

INSTRUCTIONS STRICTES D'OUTILS :
- Lis UNIQUEMENT via `read_file` les fichiers ci-dessous (chacun <= 36 Ko, appelle `read_file` en parallele !).
- N'appelle JAMAIS `run_command` ni `write_file`. Retourne DIRECTEMENT ta decision JSON via `finish`.

FICHIERS A LIRE :
{files_list}

TA MISSION :
1. **Dedoublonnage semantique rigoureux intra-Objet** : examine `near_duplicate_pairs_idees` (et `acquis`/`outils`) ainsi que les listes de titres. Fusionne TOUTES les reformulations ou doublons d'une meme idee issus de lots differents dans `merges_idees` (`keep_id`, `merge_ids`, plus eventuellement `upgraded_titre_clair_fr`, `upgraded_sous_theme`). Ne fusionne PAS deux mecanismes reellement distincts qui ne font que partager du vocabulaire.
2. **Reclassification** : signale dans `reclassifications` toute fiche `temp_id` clairement mal placee (`target_register`: `"acquis"`, `"outil"`, `"ecart"`, ou `"move_objet"` avec le bon `objet` et `theme`).
3. **Clarte scientifique (R-3044, R-5226) et harmonisation des sous-themes** : dans `upgrades`, harmonise les sous-themes fragmentes et corrige tout titre obscur ou commencant par un code nu.

ZERO emoji. Appelle `finish` avec ton JSON complet."""

    res = await agent(
        prompt,
        schema=P2B_SCHEMA,
        role=f"Conservateur {obj_key[:5]}",
        model="inherit",
        workspace="inherit",
    )
    res = strip_emoji_recursive(res)
    out_path.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(res.get("merges_idees", []))


if todo_obj:
    m_counts = await parallel(todo_obj, run_conservator)
    log(f"Phase 2B fusions par Objet: {dict(zip(todo_obj, m_counts))}")

log("Application des decisions Phase 2B et preparation Phase 3...")
runpy.run_path(str(SCRATCH / "apply_phase2b_and_prepare_phase3.py"), run_name="__main__")


# ==============================================================================
# PHASE 3 : Dedoublonnage transversal inter-rayons et generation des catalogues
# ==============================================================================
phase("Phase 3 - Dedoublonnage transversal et catalogues (inherit)")

P3_SCHEMA = {
    "type": "object",
    "properties": {
        "cross_merges": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "keep_id": {"type": "string"},
                    "merge_ids": {"type": "array", "items": {"type": "string"}},
                    "upgraded_objet": {"type": "string"},
                    "upgraded_titre_clair_fr": {"type": "string"},
                    "upgraded_sous_theme": {"type": "string"},
                },
                "required": ["keep_id", "merge_ids"],
            },
        },
        "moves": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "temp_id": {"type": "string"},
                    "objet": {"type": "string"},
                    "theme": {"type": "string"},
                    "sous_theme": {"type": "string"},
                },
                "required": ["temp_id", "objet"],
            },
        },
        "synthese_lisezmoi_editoriale": {"type": "string"},
        "synthese_croisee_editoriale": {"type": "string"},
    },
    "required": ["cross_merges", "moves", "synthese_lisezmoi_editoriale", "synthese_croisee_editoriale"],
}

p3_dec_path = SCRATCH / "phase3_decisions.json"
if not p3_dec_path.is_file():
    # Split phase3_input.json if > 38 KB
    p3_raw = json.loads((SCRATCH / "phase3_input.json").read_text(encoding="utf-8"))
    p3_a = SCRATCH / "phase3_part_pairs.json"
    p3_b = SCRATCH / "phase3_part_taxonomy.json"
    p3_a.write_text(json.dumps({"counts": p3_raw["counts"], "cross_and_residual_duplicate_pairs": p3_raw["cross_and_residual_duplicate_pairs"][:200]}, ensure_ascii=False, indent=1), encoding="utf-8")
    p3_b.write_text(json.dumps({"all_sous_themes": p3_raw["all_sous_themes"]}, ensure_ascii=False, indent=1), encoding="utf-8")

    p3_prompt = f"""Role : Conservateur en chef de la Bibliotheque scientifique canonique (`model="inherit"`).

INSTRUCTIONS STRICTES D'OUTILS :
- Lis UNIQUEMENT via `read_file` (en parallele) :
  - `{p3_a}` (paires de doublons inter-rayons et residuels)
  - `{p3_b}` (taxonomie complete des sous-themes)
- N'appelle JAMAIS `run_command` ni `write_file`. Retourne DIRECTEMENT ta decision JSON via `finish`.

TA MISSION :
1. Decide dans `cross_merges` toutes les fusions inter-rayons ou residuelles veritables (place `keep_id` dans l'Objet le plus naturel scientifiquement ; ne fusionne pas des idees reellement distinctes).
2. Propose dans `moves` tout deplacement evident d'Objet ou harmonisation de sous-theme.
3. Redige deux textes editoriaux en francais scientifique clair (ZERO emoji, conformes a R-3044 et R-5226) :
   - `synthese_lisezmoi_editoriale` (2-3 paragraphes sur l'architecture canonique, la porte 0 orphelin et l'emploi par l'organisme en boucle fermee).
   - `synthese_croisee_editoriale` (2-3 paragraphes sur la complementarite des gisements : Lazar, Fable amont, Carbon seul, Opus 5.5, 99 collisionneurs, veille arXiv, pistes d'octobre, Plan Turing)."""

    p3_res = await agent(
        p3_prompt,
        schema=P3_SCHEMA,
        role="Conservateur en chef Phase 3",
        model="inherit",
        workspace="inherit",
    )
    p3_res = strip_emoji_recursive(p3_res)
    p3_dec_path.write_text(json.dumps(p3_res, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"Phase 3 decisions: cross_merges={len(p3_res.get('cross_merges', []))}, moves={len(p3_res.get('moves', []))}")

log("Assemblage final des 4 registres, 3 catalogues et 5 rayons sans troncature...")
runpy.run_path(str(SCRATCH / "assemble_final_library.py"), run_name="__main__")


# ==============================================================================
# PHASE 4 : Porte mecanique 0 orphelin
# ==============================================================================
phase("Phase 4 - Porte mecanique 0 orphelin")

verif_script = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v1/verifier_couverture_bibliotheque_v1.py"
runpy.run_path(str(verif_script), run_name="__main__")
cert = json.loads((RACINE / "docs/notes/bibliotheque/catalogue-canonique-v1/CERTIFICAT-ZERO-ORPHELIN-v1.json").read_text(encoding="utf-8"))
log(f"VERDICT CERTIFICAT: {cert['verdict']} | attendues={cert['total_entrees_attendues']} | couvertes={cert['total_entrees_couvertes']} | orphelins={cert['orphelins']}")
if cert["verdict"] != "VALIDE_ZERO_ORPHELIN":
    raise RuntimeError(f"Certification failed: {cert['erreurs']}")
