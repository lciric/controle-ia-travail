#!/usr/bin/env python3
"""Extraction des traits (activations) de Llama-3.1-8B-Instruct pour la banque de tâches — étape 1 du programme
« gradient conçu par l'essaim » (sondes). À lancer sur l'instance GPU du programme, sous GO (GO-2026-10-24-05), par le
lanceur de la lignée qui tient la clé Vast.ai ; jamais depuis une session sans GO.

v2, écrite par la lignée « session-depot » le 24 octobre 2026 depuis la v1 de « conv-audit »
(`extraire_activations_v1.py`, `e85313d8…`, branche `outils/essaim-m3-gradient-v1-travail`, `bc06466`), sous un nom
nouveau (R12). Conception inchangée : banque lue par `id` et `texte` seulement, jamais `verite` ; même gabarit de
consigne ; flux résiduel en sortie des couches demandées ; agrégations « dernier » (dernier jeton de l'entrée, après
l'en-tête de réponse) et « moyenne » (jetons qui suivent le préfixe système) ; troncature du texte par la fin ; mêmes
noms et formes de fichiers (`traits-couche<c>-<agrégation>.npz` : `ids`, `X`), même manifeste. Corrections (mesurées
sous les versions épinglées du dépôt, `requirements-cpu.txt` : torch 2.14.1, transformers 5.18.0) :
- D-1 : `apply_chat_template(..., tokenize=True)` rend un `BatchEncoding` sous transformers 5.18.0 ; la v1 prenait sa
  longueur (2 clés) pour un nombre de jetons et le passait à `torch.tensor` (échec à la première tâche ; troncature
  jamais déclenchée). La v2 lit `input_ids`.
- D-2 : `device_map="auto"` exige `accelerate`, absent des versions épinglées (échec au chargement, mesuré). La v2
  charge le modèle puis le place sur la carte (`.to`) ; sans carte, refus, sauf `--processeur-permis` (essais).
- D-3 : chaque troncature est consignée (`troncatures` : identifiant → [jetons avant, jetons après]) ; aucun repli
  silencieux (R5).
- D-4 : révision exigée pour un modèle du Hub (aucune révision implicite) ; révision résolue (`_commit_hash`),
  versions, carte et durée consignées au manifeste.
- D-5 : `logits_to_keep=1` : les logits de toutes les positions ne servent à rien ici (mémoire) ; états cachés
  inchangés.

    python extraire_activations_v2.py --banque banque/banque-confrontation-v1.json --sortie traits/ \
        --modele meta-llama/Llama-3.1-8B-Instruct --revision 0e9e39f249a16976918f6564b8830bc894c89659 \
        --couches 8 12 16 20 24 --agregations dernier moyenne --max-jetons 2048

`--factice` : pas de modèle, traits aléatoires de même forme (test de la chaîne sans carte). Graines : aucune
(déterministe ; le tirage factice prend `numpy.random.default_rng(0)` comme la v1).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import pathlib
import platform
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
    manquantes = [n for n in ("train", "test", "test_final") if not isinstance(b.get(n), list) or not b[n]]
    if manquantes:
        sys.exit(f"banque : parts absentes ou vides : {manquantes}")  # la v1 les sautait sans le dire
    taches = []
    for n in ("train", "test", "test_final"):
        for t in b[n]:
            taches.append((str(t["id"]), str(t["texte"])))  # jamais la vérité
    ids = [i for i, _ in taches]
    if len(set(ids)) != len(ids):
        sys.exit("identifiants en double dans la banque")
    return taches


def jetons(rendu) -> list[int]:
    """`apply_chat_template(tokenize=True)` : liste d'entiers (anciennes versions) ou `BatchEncoding` (5.x) — D-1."""
    ids = rendu["input_ids"] if hasattr(rendu, "keys") else rendu
    if ids and isinstance(ids[0], list):  # forme par lot [[…]]
        if len(ids) != 1:
            sys.exit("gabarit : un seul dialogue attendu")
        ids = ids[0]
    if not ids or not all(isinstance(i, int) for i in ids):
        sys.exit(f"gabarit : jetons illisibles ({type(rendu).__name__})")
    return list(ids)


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
    p.add_argument("--processeur-permis", action="store_true", help="essais seulement : modèle sur processeur sans carte")
    args = p.parse_args()
    banque = pathlib.Path(args.banque)
    sortie = pathlib.Path(args.sortie)
    if sortie.exists() and any(sortie.iterdir()):
        sys.exit(f"{sortie} existe et n'est pas vide (R12)")
    sortie.mkdir(parents=True, exist_ok=True)
    taches = charger_taches(banque)
    debut = time.time()
    manifeste = {"quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "banque": str(banque),
                 "sha256_banque": empreinte_fichier(banque), "n_taches": len(taches), "modele": (None if args.factice else args.modele),
                 "revision": args.revision, "type_nombre": args.type_nombre, "couches": args.couches, "agregations": args.agregations,
                 "max_jetons": args.max_jetons, "gabarit_systeme": GABARIT_SYSTEME, "sha256_gabarit": hashlib.sha256(GABARIT_SYSTEME.encode("utf-8")).hexdigest(),
                 "factice": bool(args.factice), "script": pathlib.Path(__file__).name, "sha256_script": empreinte_fichier(pathlib.Path(__file__)),
                 "python": platform.python_version(), "jetons_par_tache": {}, "troncatures": {}, "fichiers": {}}
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
        import transformers
        from transformers import AutoModelForCausalLM, AutoTokenizer
        local = pathlib.Path(args.modele).is_dir()
        if not local and not args.revision:
            sys.exit("modèle du Hub sans --revision : refusé (D-4)")
        if torch.cuda.is_available():
            appareil = torch.device("cuda")
        elif args.processeur_permis:
            appareil = torch.device("cpu")
        else:
            sys.exit("aucune carte visible (torch.cuda.is_available() faux) : refusé ; --processeur-permis pour un essai")
        dtype = {"bfloat16": torch.bfloat16, "float16": torch.float16, "float32": torch.float32}[args.type_nombre]
        tok = AutoTokenizer.from_pretrained(args.modele, revision=args.revision)
        modele = AutoModelForCausalLM.from_pretrained(args.modele, revision=args.revision, dtype=dtype)  # D-2 : sans device_map
        modele.to(appareil)
        modele.eval()
        manifeste["config_modele"] = {"n_couches": int(modele.config.num_hidden_layers), "dimension": int(modele.config.hidden_size),
                                      "nom_ou_chemin": str(getattr(modele.config, "_name_or_path", args.modele)),
                                      "revision_resolue": getattr(modele.config, "_commit_hash", None)}
        manifeste["environnement"] = {"torch": torch.__version__, "transformers": transformers.__version__, "numpy": np.__version__,
                                      "cuda": torch.version.cuda, "appareil": str(appareil),
                                      "carte": (torch.cuda.get_device_name(0) if appareil.type == "cuda" else None)}
        if not local and manifeste["config_modele"]["revision_resolue"] not in (None, args.revision):
            sys.exit(f"révision résolue {manifeste['config_modele']['revision_resolue']} ≠ révision demandée {args.revision}")
        for c in args.couches:
            if not (0 <= c <= modele.config.num_hidden_layers):
                sys.exit(f"couche {c} hors de [0, {modele.config.num_hidden_layers}]")
        with torch.no_grad():
            for k, (ident, texte) in enumerate(taches):
                messages = [{"role": "system", "content": GABARIT_SYSTEME}, {"role": "user", "content": texte}]
                prefixe = jetons(tok.apply_chat_template(messages[:1], tokenize=True, add_generation_prompt=False))
                entree = jetons(tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True))
                avant = len(entree)
                if len(entree) > args.max_jetons:
                    # on tronque le texte de la tâche par la fin, en gardant la structure du gabarit (comme la v1)
                    texte_tok = tok(texte, add_special_tokens=False)["input_ids"][: max(16, args.max_jetons - len(prefixe) - 64)]
                    texte = tok.decode(texte_tok)
                    messages[1]["content"] = texte
                    entree = jetons(tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True))
                    if len(entree) > args.max_jetons:
                        sys.exit(f"{ident} : {len(entree)} jetons après troncature, au-dessus de {args.max_jetons}")
                    manifeste["troncatures"][ident] = [avant, len(entree)]  # D-3
                x = torch.tensor([entree], device=appareil)
                sortie_modele = modele(x, output_hidden_states=True, logits_to_keep=1)  # D-5
                hs = sortie_modele.hidden_states  # tuple (n_couches + 1) de [1, T, d] ; hs[0] = plongement
                if len(hs) != modele.config.num_hidden_layers + 1 or hs[0].shape[1] != x.shape[1]:
                    sys.exit(f"{ident} : états cachés de forme inattendue")
                # positions du texte de la tâche : après le préfixe système ; approximation par la longueur du préfixe
                debut_texte = min(len(prefixe), x.shape[1] - 1)
                ids.append(ident)
                manifeste["jetons_par_tache"][ident] = int(x.shape[1])
                for c in args.couches:
                    h = hs[c][0].float()
                    for a in args.agregations:
                        v = h[-1] if a == "dernier" else h[debut_texte:].mean(0)
                        v = v.cpu().numpy().astype(np.float32)
                        if not np.all(np.isfinite(v)):
                            sys.exit(f"{ident} : trait non fini (couche {c}, {a})")
                        vues[f"couche{c}-{a}"].append(v)
                if k % 20 == 0:
                    print(f"{k + 1}/{len(taches)} tâches ; {time.time() - debut:.0f} s", flush=True)
    for nom, liste in vues.items():
        f = sortie / f"traits-{nom}.npz"
        np.savez(f, ids=np.array(ids), X=np.stack(liste))
        sceller(f)
        manifeste["fichiers"][nom] = {"chemin": str(f), "sha256": empreinte_fichier(f), "forme": [len(ids), int(liste[0].shape[0])]}
    manifeste["n_tronquees"] = len(manifeste["troncatures"])
    manifeste["duree_s"] = round(time.time() - debut, 1)
    m = sortie / "manifeste-traits.json"
    m.write_text(json.dumps(manifeste, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(m)
    print(json.dumps({k: v for k, v in manifeste.items() if k not in ("jetons_par_tache", "troncatures")}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
