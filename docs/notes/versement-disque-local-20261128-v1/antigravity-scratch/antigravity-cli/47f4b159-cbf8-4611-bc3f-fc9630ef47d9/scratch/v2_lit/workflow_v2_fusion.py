#!/usr/bin/env python3
"""Workflow Python incremental v2 - Etape 2 : Conservateur v2 (model='inherit') + assemblage catalogue-canonique-v2 + verification 0 orphelin."""
import json
import re
import runpy
import shutil
from pathlib import Path

RACINE = Path(r"C:\Users\lciri\wt-organisme-boucle-fermee")
V2_DIR = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v2"
V2_DIR.mkdir(parents=True, exist_ok=True)
V2_SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch\v2_lit")

EMOJI_RE = re.compile("[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+")


def strip_emoji_rec(x):
    if isinstance(x, str):
        return EMOJI_RE.sub("", x).strip()
    if isinstance(x, list):
        return [strip_emoji_rec(i) for i in x]
    if isinstance(x, dict):
        return {k: strip_emoji_rec(v) for k, v in x.items()}
    return x


phase("V2 Etape 2 - Preparation des rapprochements v1 <-> LIT")
runpy.run_path(str(V2_SCRATCH / "prepare_v2_conservator.py"), run_name="__main__")

phase("V2 Etape 2 - Conservateur v2 (model='inherit')")
dec_path = V2_SCRATCH / "v2_conservator_decisions.json"
if not dec_path.is_file():
    man = json.loads((V2_SCRATCH / "conservator_manifest.json").read_text(encoding="utf-8"))
    files_list = "\n".join(f"- `{f}`" for f in man["files"])

    V2_DEC_SCHEMA = {
        "type": "object",
        "properties": {
            "attach_to_v1": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "temp_id": {"type": "string"},
                        "v1_id": {"type": "string"},
                        "voisin_a_citer": {"type": "string"},
                        "set_hybride": {"type": "boolean"},
                    },
                    "required": ["temp_id", "v1_id", "voisin_a_citer"],
                },
            },
            "intra_lit_merges": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "keep_id": {"type": "string"},
                        "merge_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["keep_id", "merge_ids"],
                },
            },
            "synthese_v2_editoriale": {"type": "string"},
        },
        "required": ["attach_to_v1", "intra_lit_merges", "synthese_v2_editoriale"],
    }

    prompt = f"""Role : Conservateur scientifique senior (`model="inherit"`) pour la fusion incrementale de `catalogue-canonique-v2/`.

INSTRUCTIONS STRICTES D'OUTILS :
- Lis UNIQUEMENT via `read_file` (en parallele) les fichiers ci-dessous (tous <= 36 Ko).
- N'appelle JAMAIS `run_command` ni `write_file`. Retourne DIRECTEMENT ton JSON via `finish`. ZERO emoji.

FICHIERS A LIRE :
{files_list}

TA MISSION :
1. `attach_to_v1` : parmi les candidats de rapprochement `01_v1_matches_*.json`, rattache aux fiches `IDEE-CANON-xxxx` existantes de `v1` les idees issues de `LIT-0001..2863` qui representent la MEME idee ou le MEME mecanisme (pour enrichir `anteriorite_et_voisins_a_citer` et passer `origine_type` a `"hybride_interne_et_voisin"`). Ne rattache PAS deux mecanismes reellement distincts (ils resteront de nouvelles fiches `emprunt_litterature_a_citer` ou `interne_programme`).
2. `intra_lit_merges` : parmi `02_intra_lit_dups.json`, fusionne les doublons veritables entre nouvelles idees candidates issues de lots `LIT` differents.
3. `synthese_v2_editoriale` : redige 2 a 3 paragraphes clairs en francais scientifique (conformes a R-3044/R-5226, ZERO emoji) sur l'apport de cette version 2 incrementale (papier externes lus sur PDF entier contre resume, hybrides interne+voisin, emprunts a citer sous GO-2026-11-19-83, temoins negatifs issus des limites de la litterature)."""

    res = await agent(prompt, schema=V2_DEC_SCHEMA, role="Conservateur v2 (inherit)", model="inherit", workspace="inherit")
    res = strip_emoji_rec(res)
    dec_path.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"Conservateur v2: attach_to_v1={len(res['attach_to_v1'])}, intra_lit_merges={len(res['intra_lit_merges'])}")

phase("V2 Etape 3 - Assemblage catalogue-canonique-v2 et verification 0 orphelin")
runpy.run_path(str(V2_SCRATCH / "assemble_v2_library.py"), run_name="__main__")

verif_dst = V2_DIR / "verifier_couverture_bibliotheque_v2.py"
shutil.copyfile(str(V2_SCRATCH / "verifier_couverture_bibliotheque_v2.py"), str(verif_dst))
runpy.run_path(str(verif_dst), run_name="__main__")

cert = json.loads((V2_DIR / "CERTIFICAT-ZERO-ORPHELIN-v2.json").read_text(encoding="utf-8"))
log(f"VERDICT V2: {cert['verdict']} | attendues={cert['total_entrees_attendues_union']} | couvertes={cert['total_entrees_couvertes']} | orphelins={cert['orphelins']}")
if cert["verdict"] != "VALIDE_ZERO_ORPHELIN":
    raise RuntimeError(f"V2 certification failed: {cert['erreurs']}")
