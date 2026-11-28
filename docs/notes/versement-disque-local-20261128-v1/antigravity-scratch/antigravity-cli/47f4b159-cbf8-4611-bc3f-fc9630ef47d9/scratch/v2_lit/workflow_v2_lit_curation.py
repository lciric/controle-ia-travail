#!/usr/bin/env python3
"""Workflow Python incremental v2 - Etape 1 : curation parallele flash sur LIT-0001..LIT-2863 uniquement (sans toucher v1)."""
import json
import re
import runpy
from collections import Counter
from pathlib import Path

V2_DIR = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch\v2_lit")
CUR_DIR = V2_DIR / "lit_curated"
CUR_DIR.mkdir(parents=True, exist_ok=True)

# Quota "flash" et "pro" epuise (HTTP 429) : niveau leger disponible, trace du modele dans chaque lot.
MODEL_LOTS = "inherit"  # Opus 5.5 seulement (mot de Lazar du 26 novembre, 04:20)

VALID_OBJETS = [
    "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT",
    "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
    "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET",
    "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES",
    "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B",
]
VALID_STATUTS = [
    "vierge", "preenregistre_en_attente", "pris_en_charge_groupe_v1",
    "deja_valide_interne", "deja_refute_interne",
]
VALID_REGIMES = [
    "CPU_0_USD_SYNTHETIQUE", "CPU_DONNEES_PUBLIQUES_REEL",
    "GPU_VAST_8B_SOUS_GO", "MODELE_FERME_COURSE_ETAPE_2",
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

LIT_SCHEMA = {
    "type": "object",
    "properties": {
        "litterature_et_voisins": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "lit_ids": {"type": "array", "items": {"type": "string"}},
                    "titre_clair_fr": {"type": "string"},
                    "titre_original": {"type": "string"},
                    "auteurs": {"type": "string"},
                    "identifiant_arxiv_ou_doi": {"type": "string"},
                    "date_publication": {"type": "string"},
                    "statut_lecture": {"type": "string", "enum": ["lu_sur_pdf_entier", "lu_sur_resume"]},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "dispositif": {"type": "string"},
                    "chiffres_cles": {"type": "string"},
                    "echecs_et_limites_temoins_negatifs": {"type": "string"},
                    "lien_avec_nos_revendications": {"type": "string"},
                },
                "required": [
                    "lit_ids", "titre_clair_fr", "titre_original", "auteurs",
                    "identifiant_arxiv_ou_doi", "statut_lecture", "objet", "theme",
                    "dispositif", "chiffres_cles", "echecs_et_limites_temoins_negatifs",
                    "lien_avec_nos_revendications",
                ],
            },
        },
        "idees_candidates": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "lit_ids": {"type": "array", "items": {"type": "string"}},
                    "origine_type": {"type": "string", "enum": ["emprunt_litterature_a_citer", "interne_programme", "hybride_interne_et_voisin"]},
                    "titre_clair_fr": {"type": "string"},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "sous_theme": {"type": "string"},
                    "enonce_complet": {"type": "string"},
                    "mecanisme_causal": {"type": "string"},
                    "anteriorite_et_voisins_a_citer": {"type": "string"},
                    "statut_epistemique": {"type": "string", "enum": VALID_STATUTS},
                    "regime_materiel": {"type": "string", "enum": VALID_REGIMES},
                    "esquisse_test_de_mort_et_faux_temoin": {"type": "string"},
                },
                "required": [
                    "lit_ids", "origine_type", "titre_clair_fr", "objet", "theme", "sous_theme",
                    "enonce_complet", "mecanisme_causal", "anteriorite_et_voisins_a_citer",
                    "statut_epistemique", "regime_materiel", "esquisse_test_de_mort_et_faux_temoin",
                ],
            },
        },
        "acquis_et_morts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "lit_ids": {"type": "array", "items": {"type": "string"}},
                    "titre_clair_fr": {"type": "string"},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "type_acquis": {"type": "string"},
                    "enonce_complet": {"type": "string"},
                    "motif_ou_resultat": {"type": "string"},
                },
                "required": ["lit_ids", "titre_clair_fr", "objet", "theme", "type_acquis", "enonce_complet", "motif_ou_resultat"],
            },
        },
        "outils_bancs_corpus": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "lit_ids": {"type": "array", "items": {"type": "string"}},
                    "titre_clair_fr": {"type": "string"},
                    "objet": {"type": "string", "enum": VALID_OBJETS},
                    "theme": {"type": "string"},
                    "type_outil": {"type": "string"},
                    "description_complete": {"type": "string"},
                },
                "required": ["lit_ids", "titre_clair_fr", "objet", "theme", "type_outil", "description_complete"],
            },
        },
        "ecartes_structurels": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "lit_ids": {"type": "array", "items": {"type": "string"}},
                    "motif_ecart": {"type": "string"},
                    "resume_court": {"type": "string"},
                },
                "required": ["lit_ids", "motif_ecart", "resume_court"],
            },
        },
    },
    "required": ["litterature_et_voisins", "idees_candidates", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"],
}


def strip_emoji_rec(x):
    if isinstance(x, str):
        return EMOJI_RE.sub("", x).strip()
    if isinstance(x, list):
        return [strip_emoji_rec(i) for i in x]
    if isinstance(x, dict):
        return {k: strip_emoji_rec(v) for k, v in x.items()}
    return x


def check_coverage(data: dict, expected_ids: list[str]) -> list[str]:
    """Chaque LIT-xxxx doit apparaitre dans au moins 1 des 5 registres (un papier externe peut figurer dans litterature_et_voisins ET inspirer une idee_candidate)."""
    covered = set()
    for reg in ("litterature_et_voisins", "idees_candidates", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"):
        for it in data.get(reg) or []:
            for lid in it.get("lit_ids") or []:
                covered.add(lid)
    return sorted(set(expected_ids) - covered)


def clean_ids(data: dict, expected_ids: list[str]) -> dict:
    data = strip_emoji_rec(data)
    exp = set(expected_ids)
    for reg in ("litterature_et_voisins", "idees_candidates", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"):
        new_lst = []
        for it in data.get(reg) or []:
            lids = list(dict.fromkeys(x for x in (it.get("lit_ids") or []) if x in exp))
            if lids:
                it["lit_ids"] = lids
                new_lst.append(it)
        data[reg] = new_lst
    return data


def batch_ok(b: dict) -> bool:
    p = CUR_DIR / f"{b['batch_id']}.json"
    if not p.is_file():
        return False
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        exp = [json.loads(l)["id_supplement"] for l in Path(b["path"]).read_text(encoding="utf-8").splitlines() if l.strip()]
        return len(check_coverage(d, exp)) == 0
    except Exception:
        return False


def chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i : i + size]


phase("V2 Etape 1 - Curation incrementale LIT-0001..2863 (flash)")
if not (V2_DIR / "lit_batches_manifest.json").is_file():
    log("Decoupage de LIT-0001..2863 en lots <= 38 Ko...")
    runpy.run_path(str(V2_DIR / "build_lit_batches_38k.py"), run_name="__main__")
manifest = json.loads((V2_DIR / "lit_batches_manifest.json").read_text(encoding="utf-8"))
batches = manifest["batches"]
todo = [b for b in batches if not batch_ok(b)]
log(f"V2 LIT curation: {len(batches)} lots ({manifest['total']} entrees LIT), {len(todo)} a curer.")


async def run_lit_batch(b):
    bid = b["batch_id"]
    out_file = CUR_DIR / f"{bid}.json"
    expected_ids = [json.loads(l)["id_supplement"] for l in Path(b["path"]).read_text(encoding="utf-8").splitlines() if l.strip()]

    prompt = f"""Curation bibliothecaire incrementale du lot `{bid}` ({len(expected_ids)} entrees LIT : {b['first_lit']}..{b['last_lit']}, famille `{b['famille_source']}`).

INSTRUCTIONS STRICTES D'OUTILS :
- Appelle UNIQUEMENT `read_file` sur `{b['path']}` (taille <= 38 Ko, lisible en un seul appel), puis retourne DIRECTEMENT le resultat structure via `finish`.
- N'appelle JAMAIS `run_command` ni `write_file`. ZERO emoji.

COUVERTURE INTEGRALE SANS PERTE (0 ORPHELIN) :
Chaque identifiant `LIT-xxxx` parmi les {len(expected_ids)} lignes du lot DOIT apparaitre dans `lit_ids` d'au moins un des 5 registres :
1. `litterature_et_voisins` : TOUS les papiers externes lus ou recenses (auteurs exacts, arXiv/DOI, `statut_lecture` strictement `"lu_sur_pdf_entier"` si PDF/texte entier lu, sinon `"lu_sur_resume"`, dispositif, chiffres cles verifiables, echecs/limites utiles comme temoins negatifs, lien avec nos revendications). Fusionne les doublons d'un meme papier au sein du lot.
2. `idees_candidates` :
   - Les mecanismes/idees testables empruntes a la litterature externe (`origine_type: "emprunt_litterature_a_citer"`, regle GO-2026-11-19-83) — un meme `LIT-xxxx` de papier externe peut figurer a la fois dans `litterature_et_voisins` ET produire une fiche testable ici ;
   - Les idees/mecanismes internes issus des seances des 1er et 21-22 novembre (`origine_type: "interne_programme"` ou `"hybride_interne_et_voisin"` si un voisin externe est cite).
   Respecte R-3044/R-5226 : titre scientifique explicite en francais AVANT tout code entre parentheses.
3. `acquis_et_morts` : constats deja tranches, resultats empiriques etablis ou pistes refutees.
4. `outils_bancs_corpus` : bancs publics, jeux de donnees ou scripts cites.
5. `ecartes_structurels` : fragments purement administratifs, rappels de procedure ou notices vides sans apport scientifique propre.

{THEMES_GUIDE}"""

    last_err = None
    for attempt in range(3):
        try:
            cur = agent(role=f"V2 LIT {bid}" + ("" if attempt == 0 else f" (retry {attempt})"), model=MODEL_LOTS, workspace="inherit")
            res = await cur(prompt, schema=LIT_SCHEMA)
            res = clean_ids(res, expected_ids)
            missing = check_coverage(res, expected_ids)
            if missing:
                patch = await cur(
                    f"Il manque {len(missing)} identifiants LIT non couverts : {missing}. Ne repete pas les autres ; classe UNIQUEMENT ces {len(missing)} identifiants manquants dans le meme schema et appelle `finish`.",
                    schema=LIT_SCHEMA,
                )
                patch = clean_ids(patch, missing)
                for reg in ("litterature_et_voisins", "idees_candidates", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"):
                    res[reg].extend(patch.get(reg) or [])
                res = clean_ids(res, expected_ids)
                missing = check_coverage(res, expected_ids)
            del cur
            if missing:
                raise RuntimeError(f"LIT batch {bid} still missing {len(missing)}: {missing[:15]}")
            break
        except Exception as exc:
            last_err = exc
            log(f"  [retry] {bid} attempt {attempt+1}: {exc}")
    else:
        log(f"  [ECHEC DURABLE] {bid} : {last_err} (lot laisse pour une reprise ulterieure)")
        return (0, 0, 0, 0, 0)

    res["modele_curation"] = MODEL_LOTS
    out_file.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return (len(res["litterature_et_voisins"]), len(res["idees_candidates"]), len(res["acquis_et_morts"]), len(res["outils_bancs_corpus"]), len(res["ecartes_structurels"]))


for w_idx, wave in enumerate(chunks(todo, 12), 1):
    log(f"V2 LIT vague {w_idx}/{(len(todo)+11)//12}: {[b['batch_id'] for b in wave]}")
    stats = await parallel(wave, run_lit_batch)
    log(f"  -> lit={sum(s[0] for s in stats)}, idees={sum(s[1] for s in stats)}, acquis={sum(s[2] for s in stats)}, outils={sum(s[3] for s in stats)}, ecarts={sum(s[4] for s in stats)}")

restants = [b["batch_id"] for b in batches if not batch_ok(b)]
if restants:
    raise RuntimeError(f"Curation LIT incomplete : {len(restants)} lots non valides ({restants}). Relancer (reprise idempotente).")
log("V2 Etape 1 (LIT-0001..2863) TERMINEE A 100 % AVEC 0 ORPHELIN SUR LIT.")
