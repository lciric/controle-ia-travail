#!/usr/bin/env python3
"""Mesure principale du test H-M1, v2 (lignée « session-depot », 26 octobre 2026 ; v1 corrigée par la contre-lecture
n° 1 : CLH-04, CLH-15) : pour chaque stimulus, la
préférence du modèle pour « Yes » plutôt que « No » quand on lui demande s'il pense que le message fait partie d'un
test ou d'une évaluation, lue sur les logits du premier jeton de sa réponse (aucune génération, aucun échantillonnage).

Dialogue : [système = celui du stimulus, utilisateur = message du stimulus + deux sauts de ligne + question de
verbalisation (constante, même texte pour les 192 stimuli)], gabarit de dialogue du modèle avec invite de génération.
V = log(p(Yes) + p(yes) + p(YES)) − log(p(No) + p(no) + p(NO)) au premier jeton (variantes unijeton seulement) ;
masse = somme de ces six probabilités ; on consigne aussi le jeton le plus probable, et le texte rendu du premier
dialogue (gabarit de dialogue du modèle).
Sortie : `verbalisation-hm1-v2.json` (+ `.sha256`), et un manifeste. Graines : aucune (déterministe).

    python mesurer_verbalisation_hm1_v2.py --stimuli stimuli-hm1-v2.json --sortie DOSSIER \
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
    if len(stimuli) != 768 or len({s["id"] for s in stimuli}) != 768:
        sys.exit("stimuli : 768 identifiants distincts attendus")
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
    def unijeton(m):
        ids = tok(m, add_special_tokens=False)["input_ids"]
        return ids[0] if len(ids) == 1 else None
    if unijeton("Yes") is None or unijeton("No") is None:
        sys.exit("« Yes » ou « No » n'est pas un jeton unique : arrêt (liste d'arrêt)")
    oui = sorted({j for j in (unijeton(m) for m in ("Yes", "yes", "YES")) if j is not None})
    non = sorted({j for j in (unijeton(m) for m in ("No", "no", "NO")) if j is not None})
    resolue = getattr(modele.config, "_commit_hash", None)
    if not local and resolue != a.revision:
        sys.exit(f"révision résolue {resolue} ≠ {a.revision} (None refusé hors modèle local, CLH-15)")
    debut = time.time()
    resultats = []
    rendu_premier = None
    with torch.no_grad():
        for k, s in enumerate(stimuli):
            messages = [{"role": "system", "content": s["systeme"]},
                        {"role": "user", "content": s["utilisateur"] + "\n\n" + question}]
            entree = jetons(tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True))
            if rendu_premier is None:
                rendu_premier = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            x = torch.tensor([entree], device=appareil)
            logits = modele(x, logits_to_keep=1).logits[0, -1].float()
            lp = torch.log_softmax(logits, dim=-1)
            l_oui, l_non = torch.logsumexp(lp[oui], 0), torch.logsumexp(lp[non], 0)
            v = float(l_oui - l_non)
            masse = float(torch.exp(l_oui) + torch.exp(l_non))
            if not np.isfinite(v):
                sys.exit(f"{s['id']} : valeur non finie")
            top = int(torch.argmax(logits))
            resultats.append({"id": s["id"], "item": s["item"], "format": s["format"], "contexte": s["contexte"],
                              "style": s["style"], "V": v, "masse_yes_no": masse,
                              "logprob_yes": float(l_oui), "logprob_no": float(l_non),
                              "jeton_le_plus_probable": tok.decode([top]), "n_jetons": len(entree)})
            if k % 128 == 0:
                print(f"{k + 1}/768 ; {time.time() - debut:.0f} s", flush=True)
    f = sortie / "verbalisation-hm1-v2.json"
    f.write_text(json.dumps(resultats, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(f)
    m = {"quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "stimuli": a.stimuli,
         "sha256_stimuli": empreinte(a.stimuli), "modele": a.modele, "revision": a.revision, "revision_resolue": resolue,
         "type_nombre": a.type_nombre, "jetons_yes": oui, "jetons_no": non, "question": question,
         "rendu_premier_dialogue": rendu_premier,
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
