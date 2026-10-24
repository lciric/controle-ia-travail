#!/usr/bin/env python3
"""Extraction des traits (activations) de Llama-3.1-8B-Instruct pour la banque de tâches — étape 1 du programme
« gradient conçu par l'essaim » (sondes). À lancer sur l'instance GPU du programme, sous GO, par le lanceur de la
lignée qui tient la clé Vast.ai ; jamais depuis une session sans GO.

Entrée : la banque scellée (`banque-<nom>.json`, clés train / test / test_final ; seuls `id` et `texte` sont lus —
le script ne lit jamais `verite`). Sortie : un fichier `.npz` par vue (couche × agrégation), `ids` + `X`, et un
manifeste (modèle, révision, type de nombre, couches, agrégations, gabarit de consigne et son empreinte, empreinte de
la banque, nombre de jetons par tâche, durée) ; chaque fichier reçoit son `.sha256` (R6). Graines : aucune (déterministe).

    python extraire_activations_v1.py --banque banque/banque-confrontation-v1.json --sortie traits/ \
        --modele meta-llama/Llama-3.1-8B-Instruct --couches 8 12 16 20 24 --agregations dernier moyenne --max-jetons 2048

`--factice` : pas de modèle, traits aléatoires de même forme (test de la chaîne sans carte). Le gabarit de consigne
est fixe : le texte de la tâche est présenté comme message d'utilisateur du gabarit de dialogue du modèle, sans
réponse ; les activations sont prises sur le flux résiduel en sortie des couches demandées, au dernier jeton
(`dernier`) et en moyenne sur les jetons du texte de la tâche (`moyenne`).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import pathlib
import sys
import time

import numpy as np

GABARIT_SYSTEME = "Tu lis une trace ou un extrait d'interaction. Réponds ensuite aux questions posées."


def empreinte_fichier(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def sceller(p: pathlib.Path) -> None:
    p.with_name(p.name + ".sha256").write_text(f"{empreinte_fichier(p)}  {p.name}\n", encoding="utf-8")


def charger_taches(banque: pathlib.Path) -> list[tuple[str, str]]:
    b = json.loads(banque.read_text(encoding="utf-8"))
    taches = []
    for n in ("train", "test", "test_final"):
        for t in b.get(n, []):
            taches.append((str(t["id"]), str(t["texte"])))  # jamais la vérité
    ids = [i for i, _ in taches]
    if len(set(ids)) != len(ids):
        sys.exit("identifiants en double dans la banque")
    return taches


def principal() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--banque", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--modele", default="meta-llama/Llama-3.1-8B-Instruct")
    p.add_argument("--revision", default=None)
    p.add_argument("--couches", type=int, nargs="+", default=[8, 12, 16, 20, 24])
    p.add_argument("--agregations", nargs="+", default=["dernier", "moyenne"], choices=["dernier", "moyenne"])
    p.add_argument("--max-jetons", type=int, default=2048)
    p.add_argument("--type-nombre", default="bfloat16", choices=["bfloat16", "float16", "float32"])
    p.add_argument("--factice", action="store_true", help="aucun modèle : traits aléatoires de même forme (test de chaîne)")
    args = p.parse_args()
    banque = pathlib.Path(args.banque)
    sortie = pathlib.Path(args.sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    taches = charger_taches(banque)
    debut = time.time()
    manifeste = {"quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "banque": str(banque),
                 "sha256_banque": empreinte_fichier(banque), "n_taches": len(taches), "modele": (None if args.factice else args.modele),
                 "revision": args.revision, "type_nombre": args.type_nombre, "couches": args.couches, "agregations": args.agregations,
                 "max_jetons": args.max_jetons, "gabarit_systeme": GABARIT_SYSTEME, "sha256_gabarit": hashlib.sha256(GABARIT_SYSTEME.encode("utf-8")).hexdigest(),
                 "factice": bool(args.factice), "jetons_par_tache": {}, "fichiers": {}}
    vues = {f"couche{c}-{a}": [] for c in args.couches for a in args.agregations}
    ids = []
    if args.factice:
        rng = np.random.default_rng(0)
        for ident, texte in taches:
            ids.append(ident)
            manifeste["jetons_par_tache"][ident] = len(texte.split())
            for nom in vues:
                vues[nom].append(rng.normal(0, 1, 4096).astype(np.float32))
    else:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        dtype = {"bfloat16": torch.bfloat16, "float16": torch.float16, "float32": torch.float32}[args.type_nombre]
        tok = AutoTokenizer.from_pretrained(args.modele, revision=args.revision)
        modele = AutoModelForCausalLM.from_pretrained(args.modele, revision=args.revision, torch_dtype=dtype, device_map="auto")
        modele.eval()
        manifeste["config_modele"] = {"n_couches": int(modele.config.num_hidden_layers), "dimension": int(modele.config.hidden_size),
                                      "nom_ou_chemin": str(getattr(modele.config, "_name_or_path", args.modele))}
        for c in args.couches:
            if not (0 <= c <= modele.config.num_hidden_layers):
                sys.exit(f"couche {c} hors de [0, {modele.config.num_hidden_layers}]")
        with torch.no_grad():
            for k, (ident, texte) in enumerate(taches):
                messages = [{"role": "system", "content": GABARIT_SYSTEME}, {"role": "user", "content": texte}]
                prefixe = tok.apply_chat_template(messages[:1], tokenize=True, add_generation_prompt=False)
                entree = tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
                if len(entree) > args.max_jetons:
                    # on tronque le texte de la tâche par la fin, en gardant la structure du gabarit
                    texte_tok = tok(texte, add_special_tokens=False)["input_ids"][: max(16, args.max_jetons - len(prefixe) - 64)]
                    texte = tok.decode(texte_tok)
                    messages[1]["content"] = texte
                    entree = tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
                x = torch.tensor([entree], device=modele.device)
                sortie_modele = modele(x, output_hidden_states=True)
                hs = sortie_modele.hidden_states  # tuple (n_couches + 1) de [1, T, d] ; hs[0] = plongement
                # positions du texte de la tâche : après le préfixe système ; approximation par la longueur du préfixe
                debut_texte = min(len(prefixe), x.shape[1] - 1)
                ids.append(ident)
                manifeste["jetons_par_tache"][ident] = int(x.shape[1])
                for c in args.couches:
                    h = hs[c][0].float()
                    for a in args.agregations:
                        v = h[-1] if a == "dernier" else h[debut_texte:].mean(0)
                        vues[f"couche{c}-{a}"].append(v.cpu().numpy().astype(np.float32))
                if k % 20 == 0:
                    print(f"{k + 1}/{len(taches)} tâches ; {time.time() - debut:.0f} s", flush=True)
    for nom, liste in vues.items():
        f = sortie / f"traits-{nom}.npz"
        np.savez(f, ids=np.array(ids), X=np.stack(liste))
        sceller(f)
        manifeste["fichiers"][nom] = {"chemin": str(f), "sha256": empreinte_fichier(f), "forme": [len(ids), int(liste[0].shape[0])]}
    manifeste["duree_s"] = round(time.time() - debut, 1)
    m = sortie / "manifeste-traits.json"
    m.write_text(json.dumps(manifeste, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(m)
    print(json.dumps({k: v for k, v in manifeste.items() if k != "jetons_par_tache"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
