#!/usr/bin/env python3
"""Contrôle sans dépense, avant le GO (contre-lecture n° 2, CLY-13), lignée « session-depot », 27 octobre 2026 : les
deux modèles, à leurs révisions, mettent-ils les 3 072 stimuli en jetons avec le même gabarit de dialogue et le même
dernier jeton ? Seuls les fichiers du jeton-iseur sont téléchargés (quelques Mo, jeton Hugging Face lu dans
l'environnement, jamais affiché). Sinon, la garde de l'analyse arrêterait tout après la dépense.
Sortie : `gabarits-echelle-v3.json` (+ `.sha256`).
    python -I -B verifier_gabarits_v3.py STIMULI_JSON CACHE_DOSSIER SORTIE_DOSSIER
"""
import hashlib
import json
import pathlib
import sys

MODELES = {"petit": ("meta-llama/Llama-3.1-8B-Instruct", "0e9e39f249a16976918f6564b8830bc894c89659"),
           "grand": ("meta-llama/Llama-3.1-70B-Instruct", "1605565b47bb9346c5515c34102e054115b4f98b")}
FICHIERS = ("tokenizer.json", "tokenizer_config.json", "special_tokens_map.json", "config.json")


def principal(argv):
    stimuli, cache, sortie = (pathlib.Path(a) for a in argv)
    if sortie.exists():
        sys.exit(f"{sortie} existe déjà (R12)")
    from huggingface_hub import hf_hub_download
    from transformers import AutoTokenizer
    st = json.loads(stimuli.read_text(encoding="utf-8"))["stimuli"]
    res = {}
    for nom, (depot, rev) in MODELES.items():
        dossier = None
        for f in FICHIERS:
            chemin = pathlib.Path(hf_hub_download(depot, f, revision=rev, cache_dir=str(cache)))
            if chemin.parent.name != rev:
                sys.exit(f"{depot} : révision résolue ailleurs ({chemin.parent.name})")
            dossier = chemin.parent
        tok = AutoTokenizer.from_pretrained(str(dossier))
        derniers, longueurs, premier = set(), [], None
        for s in st:
            enc = tok.apply_chat_template(s["messages"], tokenize=True, add_generation_prompt=True)
            ids = list(enc["input_ids"] if hasattr(enc, "keys") else enc)
            if premier is None:
                premier = tok.decode(ids)
            derniers.add(ids[-1])
            longueurs.append(len(ids))
        res[nom] = {"depot": depot, "revision": rev, "derniers_jetons": sorted(derniers),
                    "dernier_jeton": tok.decode([sorted(derniers)[0]]), "longueur_min_max": [min(longueurs), max(longueurs)],
                    "rendu_premier_sha256": hashlib.sha256(premier.encode("utf-8")).hexdigest(), "rendu_premier": premier}
    verdict = {"dernier_jeton_constant_petit": len(res["petit"]["derniers_jetons"]) == 1,
               "dernier_jeton_constant_grand": len(res["grand"]["derniers_jetons"]) == 1,
               "rendu_premier_identique": res["petit"]["rendu_premier"] == res["grand"]["rendu_premier"],
               "dernier_jeton_identique": res["petit"]["derniers_jetons"] == res["grand"]["derniers_jetons"]}
    sortie.mkdir(parents=True)
    f = sortie / "gabarits-echelle-v3.json"
    f.write_text(json.dumps({"version": "gabarits-echelle-v3", "stimuli_sha256": hashlib.sha256(stimuli.read_bytes()).hexdigest(),
                             **res, "verdict": verdict}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (sortie / (f.name + ".sha256")).write_text(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n",
                                               encoding="utf-8")
    print(json.dumps(verdict, ensure_ascii=False))
    return 0 if all(verdict.values()) else 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
