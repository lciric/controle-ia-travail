#!/usr/bin/env python3
"""Mesures de l'étape 0 (porte de certification à l'aveugle) du test H-M1 v4 (lignée « session-depot », 26 octobre 2026,
R-476). Une passe avant par dialogue, sans génération, sans échantillonnage (déterministe).

Voie verbale (`e0-hm1-v4.json`, clé `verbal`) : au premier jeton de la réponse, pour la question du dialogue,
  questions Yes/No (eval_yn, eval_yn_conv, meta_yn, disc_yn) : variantes unijeton de « Yes » et de « No » ;
  choix forcé (eval_fc_tu, eval_fc_ut) : variantes unijeton de « test » et de « user » ;
  lp_pos = log Σ p(variantes positives), lp_neg = log Σ p(variantes négatives), masse = p_pos + p_neg, jetons de tête.
**À l'aveugle (C1)** : pour les questions d'évaluation (eval_*), le fichier principal ne garde que la masse et les cinq
jetons de tête, sans probabilité ; lp_pos et lp_neg vont dans `valeurs-eval-scellees.json`, scellé, que l'analyse de
l'étape 0 ne lit jamais. Pour meta_yn et disc_yn, tout est dans le fichier principal (disc_yn est lu en exactitude).
Sonde (clé `sonde`) : flux résiduel en sortie des couches 8, 12, 16, 20, 24, au dernier jeton de l'entrée (après l'en-tête
de réponse, position constante, C12) ; `activations-sonde.npz` (`ids`, `X<couche>`).

Révision : comme `mesurer_verbalisation_hm1_v3.py` (R-456) : dossier d'instantané du cache, modèle chargé depuis ce dossier.

    python mesurer_e0_hm1_v4.py --stimuli e0-hm1-v4.json --sortie DOSSIER \
        --modele meta-llama/Llama-3.1-8B-Instruct --revision 0e9e39f249a16976918f6564b8830bc894c89659
"""
import argparse
import datetime as _dt
import hashlib
import json
import math
import pathlib
import platform
import sys
import time

COUCHES = (8, 12, 16, 20, 24)
VARIANTES = {"yn": (("Yes", "yes", "YES"), ("No", "no", "NO")), "fc": (("test", "Test", "TEST"), ("user", "User", "USER"))}


def empreinte(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{empreinte(f)}  {f.name}\n", encoding="utf-8")


def genre(question):
    return "fc" if question.startswith("eval_fc") else "yn"


def principal(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--stimuli", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--modele", required=True)
    p.add_argument("--revision", default=None)
    p.add_argument("--type-nombre", default="bfloat16", choices=["bfloat16", "float16", "float32"])
    p.add_argument("--processeur-permis", action="store_true")
    p.add_argument("--limite", type=int, default=None, help="essais seulement : n premiers dialogues de chaque voie")
    a = p.parse_args(argv)
    sortie = pathlib.Path(a.sortie)
    if sortie.exists() and any(sortie.iterdir()):
        sys.exit(f"{sortie} existe et n'est pas vide (R12)")
    sortie.mkdir(parents=True, exist_ok=True)
    doc = json.loads(pathlib.Path(a.stimuli).read_text(encoding="utf-8"))
    if doc.get("version") != "e0-hm1-v4":
        sys.exit("stimuli : version e0-hm1-v4 attendue")
    verbal, sonde = doc["verbal"], doc["sonde"]
    if a.limite is not None:
        verbal, sonde = verbal[:a.limite], sonde[:a.limite]
    import numpy as np
    import torch
    import transformers
    from transformers import AutoModelForCausalLM, AutoTokenizer
    local = pathlib.Path(a.modele).is_dir()
    if not local and not a.revision:
        sys.exit("modèle du Hub sans --revision : refusé")
    if torch.cuda.is_available():
        appareil = torch.device("cuda")
    elif a.processeur_permis:
        appareil = torch.device("cpu")
    else:
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
    modele = AutoModelForCausalLM.from_pretrained(source, dtype=dtype)
    modele.to(appareil)
    modele.eval()
    resolue = None if local else pathlib.Path(source).name
    hachage = getattr(modele.config, "_commit_hash", None)
    if not local and hachage not in (None, a.revision):
        sys.exit(f"_commit_hash {hachage} ≠ {a.revision} : arrêt")
    n_couches = modele.config.num_hidden_layers
    couches = [c for c in COUCHES if c <= n_couches] or [n_couches]

    def unijeton(m):
        ids = tok(m, add_special_tokens=False)["input_ids"]
        return ids[0] if len(ids) == 1 else None

    jetons = {}
    for g, (pos, neg) in VARIANTES.items():
        if unijeton(pos[0]) is None or unijeton(neg[0]) is None:
            sys.exit(f"« {pos[0]} » ou « {neg[0]} » n'est pas un jeton unique : arrêt (liste d'arrêt)")
        jetons[g] = (sorted({j for j in map(unijeton, pos) if j is not None}),
                     sorted({j for j in map(unijeton, neg) if j is not None}))

    def entree(messages):
        enc = tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return torch.tensor([list(ids)], device=appareil)

    debut = time.time()
    principal_v, scellees, rendus = [], [], {}
    with torch.no_grad():
        for k, s in enumerate(verbal):
            x = entree(s["messages"])
            logits = modele(x, logits_to_keep=1).logits[0, -1].float()
            lp = torch.log_softmax(logits, dim=-1)
            g = genre(s["question"])
            ip, ineg = jetons[g]
            lp_pos = float(torch.logsumexp(lp[ip], 0))
            lp_neg = float(torch.logsumexp(lp[ineg], 0))
            masse = math.exp(lp_pos) + math.exp(lp_neg)
            if not all(map(math.isfinite, (lp_pos, lp_neg, masse))):
                sys.exit(f"{s['id']} : valeur non finie")
            tete = torch.topk(lp, 5)
            jetons_tete = [tok.decode([int(i)]) for i in tete.indices]
            ligne = {"id": s["id"], "item": s["item"], "format": s["format"], "contexte": s["contexte"], "style": s["style"],
                     "precedent": s["precedent"], "question": s["question"], "nombre_deux_chiffres": s["nombre_deux_chiffres"],
                     "masse": masse, "jetons_tete": jetons_tete, "n_jetons": int(x.shape[1])}
            if s["question"].startswith("eval"):
                scellees.append({"id": s["id"], "lp_pos": lp_pos, "lp_neg": lp_neg})
            else:
                ligne.update({"lp_pos": lp_pos, "lp_neg": lp_neg, "p_tete": [float(v) for v in tete.values.exp()]})
            principal_v.append(ligne)
            cle = (s["precedent"], s["question"])
            if cle not in rendus and s["item"] is not None:
                rendus[cle] = tok.decode(x[0])
            if k % 1000 == 0:
                print(f"verbal {k + 1}/{len(verbal)} ; {time.time() - debut:.0f} s", flush=True)
        ids_s, X = [], {c: [] for c in couches}
        for k, s in enumerate(sonde):
            x = entree(s["messages"])
            hs = modele(x, output_hidden_states=True, logits_to_keep=1).hidden_states
            for c in couches:
                v = hs[c][0, -1].float().cpu().numpy()
                if not np.all(np.isfinite(v)):
                    sys.exit(f"{s['id']} : activation non finie")
                X[c].append(v)
            ids_s.append(s["id"])
            if k % 100 == 0:
                print(f"sonde {k + 1}/{len(sonde)} ; {time.time() - debut:.0f} s", flush=True)
    f_v = sortie / "verbal-e0-hm1-v4.json"
    f_v.write_text(json.dumps(principal_v, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    sceller(f_v)
    f_s = sortie / "valeurs-eval-scellees.json"
    f_s.write_text(json.dumps(scellees, ensure_ascii=False) + "\n", encoding="utf-8")
    sceller(f_s)
    f_a = sortie / "activations-sonde.npz"
    np.savez(f_a, ids=np.array(ids_s), **{f"X{c}": np.stack(X[c]).astype(np.float32) for c in couches})
    sceller(f_a)
    m = {"quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "stimuli": a.stimuli,
         "sha256_stimuli": empreinte(a.stimuli), "modele": a.modele, "revision": a.revision, "revision_resolue": resolue,
         "commit_hash_config": hachage, "type_nombre": a.type_nombre, "couches": couches,
         "jetons": {g: {"pos": v[0], "neg": v[1]} for g, v in jetons.items()}, "n_verbal": len(principal_v),
         "n_sonde": len(ids_s), "limite": a.limite,
         "rendus_premiers": {f"{p}|{q}": t for (p, q), t in rendus.items()},
         "script": pathlib.Path(__file__).name, "sha256_script": empreinte(__file__), "python": platform.python_version(),
         "torch": torch.__version__, "transformers": transformers.__version__,
         "carte": (torch.cuda.get_device_name(0) if appareil.type == "cuda" else None),
         "duree_s": round(time.time() - debut, 1),
         "sha256_sorties": {f.name: empreinte(f) for f in (f_v, f_s, f_a)}}
    (sortie / "manifeste-e0.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(sortie / "manifeste-e0.json")
    print(json.dumps({k: m[k] for k in ("modele", "revision_resolue", "carte", "duree_s", "n_verbal", "n_sonde")},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
