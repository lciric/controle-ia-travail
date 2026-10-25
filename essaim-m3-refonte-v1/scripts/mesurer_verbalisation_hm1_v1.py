#!/usr/bin/env python3
"""Mesure principale du test H-M1, v1 (lignée « session-depot », 25 octobre 2026, R-447) : pour chaque stimulus, la
préférence du modèle pour « Yes » plutôt que « No » quand on lui demande s'il pense que le message fait partie d'un
test ou d'une évaluation, lue sur les logits du premier jeton de sa réponse (aucune génération, aucun échantillonnage).

Dialogue : [système = celui du stimulus, utilisateur = message du stimulus + deux sauts de ligne + question de
verbalisation (constante, même texte pour les 192 stimuli)], gabarit de dialogue du modèle avec invite de génération.
V = logit(« Yes ») − logit(« No ») au premier jeton ; on consigne aussi les log-probabilités et le jeton le plus probable.
Sortie : `verbalisation-hm1-v1.json` (+ `.sha256`), et un manifeste. Graines : aucune (déterministe).

    python mesurer_verbalisation_hm1_v1.py --stimuli stimuli-hm1-v1.json --sortie DOSSIER \
        --modele meta-llama/Llama-3.1-8B-Instruct --revision <commit>
"""
import argparse
import datetime as _dt
import hashlib
import json
import pathlib
import platform
import sys
import time

import numpy as np


def empreinte(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(p):
    p = pathlib.Path(p)
    p.with_name(p.name + ".sha256").write_text(f"{empreinte(p)}  {p.name}\n", encoding="utf-8")


def jetons(rendu):
    ids = rendu["input_ids"] if hasattr(rendu, "keys") else rendu
    if ids and isinstance(ids[0], list):
        if len(ids) != 1:
            sys.exit("gabarit : un seul dialogue attendu")
        ids = ids[0]
    if not ids or not all(isinstance(i, int) for i in ids):
        sys.exit("gabarit : jetons illisibles")
    return list(ids)


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--stimuli", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--modele", default="meta-llama/Llama-3.1-8B-Instruct")
    p.add_argument("--revision", default=None)
    p.add_argument("--type-nombre", default="bfloat16", choices=["bfloat16", "float16", "float32"])
    p.add_argument("--processeur-permis", action="store_true")
    a = p.parse_args()
    sortie = pathlib.Path(a.sortie)
    if sortie.exists() and any(sortie.iterdir()):
        sys.exit(f"{sortie} existe et n'est pas vide (R12)")
    sortie.mkdir(parents=True, exist_ok=True)
    doc = json.loads(pathlib.Path(a.stimuli).read_text(encoding="utf-8"))
    question = doc["question_verbalisation"]
    stimuli = doc["stimuli"]
    if len(stimuli) != 192 or len({s["id"] for s in stimuli}) != 192:
        sys.exit("stimuli : 192 identifiants distincts attendus")
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
    tok = AutoTokenizer.from_pretrained(a.modele, revision=a.revision)
    modele = AutoModelForCausalLM.from_pretrained(a.modele, revision=a.revision, dtype=dtype)
    modele.to(appareil)
    modele.eval()
    oui = tok("Yes", add_special_tokens=False)["input_ids"]
    non = tok("No", add_special_tokens=False)["input_ids"]
    if len(oui) != 1 or len(non) != 1:
        sys.exit(f"« Yes » ou « No » n'est pas un jeton unique ({oui}, {non}) : arrêt (liste d'arrêt)")
    oui, non = oui[0], non[0]
    resolue = getattr(modele.config, "_commit_hash", None)
    if not local and resolue not in (None, a.revision):
        sys.exit(f"révision résolue {resolue} ≠ {a.revision}")
    debut = time.time()
    resultats = []
    with torch.no_grad():
        for k, s in enumerate(stimuli):
            messages = [{"role": "system", "content": s["systeme"]},
                        {"role": "user", "content": s["utilisateur"] + "\n\n" + question}]
            entree = jetons(tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True))
            x = torch.tensor([entree], device=appareil)
            logits = modele(x, logits_to_keep=1).logits[0, -1].float()
            lp = torch.log_softmax(logits, dim=-1)
            v = float(logits[oui] - logits[non])
            if not np.isfinite(v):
                sys.exit(f"{s['id']} : valeur non finie")
            top = int(torch.argmax(logits))
            resultats.append({"id": s["id"], "item": s["item"], "gabarit": s["gabarit"], "style": s["style"],
                              "V": v, "logprob_yes": float(lp[oui]), "logprob_no": float(lp[non]),
                              "jeton_le_plus_probable": tok.decode([top]), "n_jetons": len(entree)})
            if k % 32 == 0:
                print(f"{k + 1}/192 ; {time.time() - debut:.0f} s", flush=True)
    f = sortie / "verbalisation-hm1-v1.json"
    f.write_text(json.dumps(resultats, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(f)
    m = {"quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "stimuli": a.stimuli,
         "sha256_stimuli": empreinte(a.stimuli), "modele": a.modele, "revision": a.revision, "revision_resolue": resolue,
         "type_nombre": a.type_nombre, "jeton_yes": oui, "jeton_no": non, "question": question,
         "script": pathlib.Path(__file__).name, "sha256_script": empreinte(__file__), "python": platform.python_version(),
         "torch": torch.__version__, "transformers": transformers.__version__,
         "carte": (torch.cuda.get_device_name(0) if appareil.type == "cuda" else None),
         "duree_s": round(time.time() - debut, 1), "sha256_sortie": empreinte(f)}
    (sortie / "manifeste-verbalisation.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(sortie / "manifeste-verbalisation.json")
    print(json.dumps({k: m[k] for k in ("modele", "revision_resolue", "carte", "duree_s")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
