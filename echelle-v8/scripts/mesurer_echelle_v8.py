#!/usr/bin/env python3
"""Mesure v8 de la comparaison d'échelle 8B contre 70B (lignée « session-depot », 27 octobre 2026 ; préenregistrement
`prereg/test-echelle-conscience-eval-v9.md`). Copie de `mesurer_echelle_v7.py` (elle-même copie de la v6, de la v5 et
de la v4) sous un nom nouveau (R12), sans changement de calcul : l'analyse v8 relit le nom et
l'empreinte de ce script dans chaque manifeste (CLW-04). Depuis la v4 (contre-lecture n° 3, CLZ-11), la garde de délestage (CLY-13) relit l'appareil de **chaque paramètre**. La v3 ne lisait
que `hf_device_map`, que transformers 5.18 ne remplit que pour une répartition sur plusieurs appareils : sur un seul
appareil, la garde passait en silence. Un paramètre délesté sur le processeur ou le disque par accelerate apparaît sur
l'appareil « cpu » ou « meta » (vérifié sur le modèle minuscule local, délestage forcé sur le disque) ; avec au moins
une carte, tout paramètre hors d'un appareil « cuda » arrête. Comme la v3 : toutes les entrées sont d'abord mises en
jetons, et le dernier jeton est contrôlé avant le chargement des poids ; gardes isolées en fonctions testées. Une passe avant par stimulus, sans
génération, sans échantillonnage (déterministe), lot de un (aucun remplissage). Aucune lecture des résultats ici :
formes, nombres finis, empreintes.

Flux résiduel au dernier jeton de l'entrée (jeton constant : fin de l'en-tête de réponse), aux profondeurs relatives
0,25 ; 0,375 ; 0,5 ; 0,625 (indice de `hidden_states` = round(r × nombre de couches), au moins 1) : 8, 12, 16, 20 pour
32 couches ; 20, 30, 40, 50 pour 80. Une matrice par couche, en float16 (`activations-L<couche>.npy`, lignes dans
l'ordre de `ids.json`), pour rester sous 100 Mo par fichier à 70B.

Révision : dossier d'instantané du cache, modèle chargé depuis ce dossier (R-456) ; `_commit_hash` contraire : arrêt.
Plusieurs cartes : répartition automatique des couches (`device_map="auto"`).

    python mesurer_echelle_v8.py --stimuli echelle-v2.json --sortie DOSSIER \
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
FLOAT16_MAX = 65000.0


class ArretMesure(SystemExit):
    pass


def empreinte(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{empreinte(f)}  {f.name}\n", encoding="utf-8")


def couches_relatives(n_couches):
    return sorted({max(1, round(r * n_couches)) for r in PROFONDEURS})


def resoudre_source(modele, revision, chercher):
    """Dossier d'instantané du cache pour (modèle, révision) ; `chercher` = try_to_load_from_cache (injectable)."""
    if not revision:
        raise ArretMesure("modèle du Hub sans --revision : refusé")
    config = chercher(modele, "config.json", revision=revision)
    if not isinstance(config, str) or pathlib.Path(config).parent.name != revision:
        raise ArretMesure(f"révision {revision} absente du cache ou résolue ailleurs ({config}) (R-456)")
    return str(pathlib.Path(config).parent)


def verifier_hachage(hachage, revision):
    if hachage not in (None, revision):
        raise ArretMesure(f"_commit_hash {hachage} ≠ {revision} : arrêt")


def controle_dernier_jeton(entrees):
    """Le dernier jeton de toutes les entrées doit être le même (fin de l'en-tête de réponse)."""
    derniers = {int(e[-1]) for e in entrees}
    if len(derniers) != 1:
        raise ArretMesure(f"dernier jeton de l'entrée non constant ({sorted(derniers)[:5]}) : arrêt avant toute passe")
    return next(iter(derniers))


def verifier_repartition(types_appareils, carte_des_couches=None):
    """Aucune couche délestée par `device_map="auto"` (CLY-13, CLZ-11) : tous les paramètres sur un appareil « cuda »
    (un paramètre délesté est sur « cpu » ou sur « meta ») ; et, si la carte des couches existe, aucune entrée « cpu »
    ni « disk »."""
    types = sorted({str(t) for t in types_appareils})
    if types != ["cuda"]:
        raise ArretMesure(f"paramètres sur les appareils {types}, pas tous sur les cartes : délestage ou chargement "
                          f"inattendu, arrêt")
    delestees = sorted({str(v) for v in (carte_des_couches or {}).values() if str(v) in ("cpu", "disk")})
    if delestees:
        raise ArretMesure(f"couches délestées sur {delestees} : la mémoire des cartes ne suffit pas, arrêt")


def verifier_activation(v, ident, couche):
    import numpy as np
    if not np.all(np.isfinite(v)):
        raise ArretMesure(f"{ident} : activation non finie (couche {couche})")
    if np.max(np.abs(v)) >= FLOAT16_MAX:
        raise ArretMesure(f"{ident} : activation hors de l'étendue de float16 (couche {couche})")


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
        raise ArretMesure(f"{sortie} existe et n'est pas vide (R12)")
    doc = json.loads(pathlib.Path(a.stimuli).read_text(encoding="utf-8"))
    if doc.get("version") != "echelle-v2":
        raise ArretMesure("stimuli : version echelle-v2 attendue")
    stimuli = doc["stimuli"][:a.limite] if a.limite is not None else doc["stimuli"]
    import numpy as np
    import torch
    import transformers
    from transformers import AutoModelForCausalLM, AutoTokenizer
    local = pathlib.Path(a.modele).is_dir()
    n_cartes = torch.cuda.device_count() if torch.cuda.is_available() else 0
    if n_cartes == 0 and not a.processeur_permis:
        raise ArretMesure("aucune carte visible : refusé")
    dtype = {"bfloat16": torch.bfloat16, "float16": torch.float16, "float32": torch.float32}[a.type_nombre]
    if local:
        source = a.modele
    else:
        from huggingface_hub import try_to_load_from_cache
        source = resoudre_source(a.modele, a.revision, try_to_load_from_cache)
    tok = AutoTokenizer.from_pretrained(source)
    # mise en jetons de toutes les entrées et contrôle du dernier jeton AVANT le chargement des poids et toute passe
    entrees = []
    for s in stimuli:
        enc = tok.apply_chat_template(s["messages"], tokenize=True, add_generation_prompt=True)
        entrees.append(list(enc["input_ids"] if hasattr(enc, "keys") else enc))
    dernier = controle_dernier_jeton(entrees)
    rendu_premier = tok.decode(entrees[0])
    sortie.mkdir(parents=True, exist_ok=True)
    if n_cartes >= 1:
        modele = AutoModelForCausalLM.from_pretrained(source, dtype=dtype, device_map="auto")
        verifier_repartition({p.device.type for p in modele.parameters()}, getattr(modele, "hf_device_map", None))
        entree_appareil = modele.get_input_embeddings().weight.device
    else:
        modele = AutoModelForCausalLM.from_pretrained(source, dtype=dtype)
        entree_appareil = torch.device("cpu")
    modele.eval()
    resolue = None if local else pathlib.Path(source).name
    hachage = getattr(modele.config, "_commit_hash", None)
    if not local:
        verifier_hachage(hachage, a.revision)
    n_couches = modele.config.num_hidden_layers
    couches = couches_relatives(n_couches)
    debut = time.time()
    ids, X = [], {c: [] for c in couches}
    with torch.no_grad():
        for k, (s, e) in enumerate(zip(stimuli, entrees)):
            x = torch.tensor([e], device=entree_appareil)
            hs = modele(x, output_hidden_states=True, logits_to_keep=1).hidden_states
            if len(hs) != n_couches + 1:
                raise ArretMesure(f"{len(hs)} états cachés pour {n_couches} couches : arrêt")
            for c in couches:
                v = hs[c][0, -1].float().cpu().numpy()
                verifier_activation(v, s["id"], c)
                X[c].append(v.astype(np.float16))
            ids.append(s["id"])
            if k % 500 == 0:
                print(f"{k + 1}/{len(stimuli)} ; {time.time() - debut:.0f} s", flush=True)
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
    longueurs = [len(e) for e in entrees]
    m = {"quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "stimuli": a.stimuli,
         "sha256_stimuli": empreinte(a.stimuli), "modele": a.modele, "revision": a.revision, "revision_resolue": resolue,
         "commit_hash_config": hachage, "type_nombre": a.type_nombre, "n_couches": n_couches, "couches": couches,
         "dimension": int(X[couches[0]][0].shape[0]), "n_stimuli": len(ids), "limite": a.limite,
         "dernier_jeton": tok.decode([dernier]), "dernier_jeton_id": dernier,
         "longueur_min_max": [min(longueurs), max(longueurs)], "rendu_premier": rendu_premier,
         "script": pathlib.Path(__file__).name, "sha256_script": empreinte(__file__),
         "python": platform.python_version(), "torch": torch.__version__, "transformers": transformers.__version__,
         "numpy": np.__version__, "cartes": [torch.cuda.get_device_name(i) for i in range(n_cartes)],
         "repartition": sorted({str(v) for v in (getattr(modele, "hf_device_map", None) or {}).values()}),
         "duree_s": round(time.time() - debut, 1), "sha256_sorties": {f.name: empreinte(f) for f in fichiers}}
    (sortie / "manifeste-mesure.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(sortie / "manifeste-mesure.json")
    print(json.dumps({k: m[k] for k in ("modele", "revision_resolue", "cartes", "couches", "dimension", "n_stimuli",
                                        "duree_s")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
