#!/usr/bin/env python3
"""Mesure de la comparaison d'échelle 8B contre 70B (lignée « session-depot », 26 octobre 2026 ; préenregistrement
`prereg/test-echelle-conscience-eval-v2.md`). Une passe avant par stimulus, sans génération, sans échantillonnage
(déterministe), lot de un (aucun remplissage). Aucune lecture des résultats ici : formes, nombres finis, empreintes.

Flux résiduel au dernier jeton de l'entrée (après l'en-tête de réponse : position constante), aux profondeurs relatives
0,25 ; 0,375 ; 0,5 ; 0,625 (indice de `hidden_states` = round(r × nombre de couches), au moins 1) : 8, 12, 16, 20 pour
32 couches ; 20, 30, 40, 50 pour 80. Une matrice par couche, en float16 (`activations-L<couche>.npy`, lignes dans
l'ordre de `ids.json`), pour rester sous 100 Mo par fichier à 70B.

Révision : comme `mesurer_e0_hm1_v4.py` (R-456) : dossier d'instantané du cache, modèle chargé depuis ce dossier ;
`_commit_hash` contraire : arrêt. Plusieurs cartes : répartition automatique des couches (`device_map="auto"`).

    python mesurer_echelle_v1.py --stimuli echelle-v1.json --sortie DOSSIER \
        --modele meta-llama/Llama-3.1-70B-Instruct --revision 1605565b47bb9346c5515c34102e054115b4f98b
"""
import argparse
import datetime as _dt
import hashlib
import json
import pathlib
import platform
import sys
import time

PROFONDEURS = (0.25, 0.375, 0.5, 0.625)


def empreinte(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{empreinte(f)}  {f.name}\n", encoding="utf-8")


def couches_relatives(n_couches):
    return sorted({max(1, round(r * n_couches)) for r in PROFONDEURS})


def principal(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--stimuli", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--modele", required=True)
    p.add_argument("--revision", default=None)
    p.add_argument("--type-nombre", default="bfloat16", choices=["bfloat16", "float16", "float32"])
    p.add_argument("--processeur-permis", action="store_true")
    p.add_argument("--limite", type=int, default=None, help="essais seulement : n premiers stimuli")
    a = p.parse_args(argv)
    sortie = pathlib.Path(a.sortie)
    if sortie.exists() and any(sortie.iterdir()):
        sys.exit(f"{sortie} existe et n'est pas vide (R12)")
    sortie.mkdir(parents=True, exist_ok=True)
    doc = json.loads(pathlib.Path(a.stimuli).read_text(encoding="utf-8"))
    if doc.get("version") != "echelle-v1":
        sys.exit("stimuli : version echelle-v1 attendue")
    stimuli = doc["stimuli"][:a.limite] if a.limite is not None else doc["stimuli"]
    import numpy as np
    import torch
    import transformers
    from transformers import AutoModelForCausalLM, AutoTokenizer
    local = pathlib.Path(a.modele).is_dir()
    if not local and not a.revision:
        sys.exit("modèle du Hub sans --revision : refusé")
    n_cartes = torch.cuda.device_count() if torch.cuda.is_available() else 0
    if n_cartes == 0 and not a.processeur_permis:
        sys.exit("aucune carte visible : refusé")
    dtype = {"bfloat16": torch.bfloat16, "float16": torch.float16, "float32": torch.float32}[a.type_nombre]
    if local:
        source = a.modele
    else:
        from huggingface_hub import try_to_load_from_cache
        config = try_to_load_from_cache(a.modele, "config.json", revision=a.revision)
        if not isinstance(config, str) or pathlib.Path(config).parent.name != a.revision:
            sys.exit(f"révision {a.revision} absente du cache ou résolue ailleurs ({config}) (R-456)")
        source = str(pathlib.Path(config).parent)
    tok = AutoTokenizer.from_pretrained(source)
    if n_cartes >= 1:
        modele = AutoModelForCausalLM.from_pretrained(source, dtype=dtype, device_map="auto")
        entree_appareil = modele.get_input_embeddings().weight.device
    else:
        modele = AutoModelForCausalLM.from_pretrained(source, dtype=dtype)
        entree_appareil = torch.device("cpu")
    modele.eval()
    resolue = None if local else pathlib.Path(source).name
    hachage = getattr(modele.config, "_commit_hash", None)
    if not local and hachage not in (None, a.revision):
        sys.exit(f"_commit_hash {hachage} ≠ {a.revision} : arrêt")
    n_couches = modele.config.num_hidden_layers
    couches = couches_relatives(n_couches)

    def entree(messages):
        enc = tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return torch.tensor([list(ids)], device=entree_appareil)

    debut = time.time()
    ids, X, derniers, longueurs = [], {c: [] for c in couches}, set(), []
    rendu_premier = None
    with torch.no_grad():
        for k, s in enumerate(stimuli):
            x = entree(s["messages"])
            if rendu_premier is None:
                rendu_premier = tok.decode(x[0])
            derniers.add(int(x[0, -1]))
            longueurs.append(int(x.shape[1]))
            hs = modele(x, output_hidden_states=True, logits_to_keep=1).hidden_states
            if len(hs) != n_couches + 1:
                sys.exit(f"{len(hs)} états cachés pour {n_couches} couches : arrêt")
            for c in couches:
                v = hs[c][0, -1].float().cpu().numpy()
                if not np.all(np.isfinite(v)):
                    sys.exit(f"{s['id']} : activation non finie (couche {c})")
                if np.max(np.abs(v)) >= 65000:
                    sys.exit(f"{s['id']} : activation hors de l'étendue de float16 (couche {c})")
                X[c].append(v.astype(np.float16))
            ids.append(s["id"])
            if k % 500 == 0:
                print(f"{k + 1}/{len(stimuli)} ; {time.time() - debut:.0f} s", flush=True)
    if len(derniers) != 1:
        sys.exit(f"dernier jeton de l'entrée non constant ({sorted(derniers)[:5]}) : arrêt")
    fichiers = []
    for c in couches:
        f = sortie / f"activations-L{c}.npy"
        np.save(f, np.stack(X[c]))
        sceller(f)
        fichiers.append(f)
    f_ids = sortie / "ids.json"
    f_ids.write_text(json.dumps(ids) + "\n", encoding="utf-8")
    sceller(f_ids)
    fichiers.append(f_ids)
    m = {"quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "stimuli": a.stimuli,
         "sha256_stimuli": empreinte(a.stimuli), "modele": a.modele, "revision": a.revision, "revision_resolue": resolue,
         "commit_hash_config": hachage, "type_nombre": a.type_nombre, "n_couches": n_couches, "couches": couches,
         "dimension": int(X[couches[0]][0].shape[0]), "n_stimuli": len(ids), "limite": a.limite,
         "dernier_jeton": tok.decode([next(iter(derniers))]), "longueur_min_max": [min(longueurs), max(longueurs)],
         "rendu_premier": rendu_premier, "script": pathlib.Path(__file__).name, "sha256_script": empreinte(__file__),
         "python": platform.python_version(), "torch": torch.__version__, "transformers": transformers.__version__,
         "cartes": [torch.cuda.get_device_name(i) for i in range(n_cartes)], "duree_s": round(time.time() - debut, 1),
         "sha256_sorties": {f.name: empreinte(f) for f in fichiers}}
    (sortie / "manifeste-mesure.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(sortie / "manifeste-mesure.json")
    print(json.dumps({k: m[k] for k in ("modele", "revision_resolue", "cartes", "couches", "dimension", "n_stimuli",
                                        "duree_s")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
