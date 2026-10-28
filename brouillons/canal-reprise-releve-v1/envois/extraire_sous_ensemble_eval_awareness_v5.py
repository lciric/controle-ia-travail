"""Extrait un sous-ensemble stratifié du jeu du papier « Large Language Models Often Know When They Are Being
Evaluated » (arXiv 2505.23836) pour la banque « conscience d'évaluation ». v4 (24 octobre 2026) = v3 plus :
(1) le mot de passe du zip est lu automatiquement dans `scripts/decrypt.sh` du dépôt (mesure publique
anti-contamination des auteurs, pas un secret) et jamais affiché ; `--mot-de-passe` reste possible ;
(2) `--local CHEMIN` lit un `dataset.zip` / `dataset.json` déjà téléchargé (navigateur), sans jeton ;
(3) les champs imbriqués sous `metadata` sont remontés au premier niveau (`eval_category`, `scaffold`, …) ;
(4) l'empreinte SHA-256 du fichier source est consignée dans la sortie (provenance).
Jeton lu dans `HF_TOKEN`, jamais affiché. Écriture en octets (empreinte exacte sous Windows). Licence CC BY-NC-SA 4.0 ;
lignes GAIA exclues et non redistribuées.

    pip install pandas pyarrow huggingface_hub numpy pyzipper
    python extraire_sous_ensemble_eval_awareness_v5.py --inspecter                    # 1. montre les clés, sans rien écrire
    python extraire_sous_ensemble_eval_awareness_v5.py --par-strate 30 --sortie eval-awareness-sous-ensemble-v1.json
Options : `--depot jjpn2/eval_awareness` (défaut) ; `--local DOSSIER_OU_FICHIER` ; `--mot-de-passe …` ;
`--champ-texte input --champ-evaluation eval_category --champ-scaffold scaffold` si les noms diffèrent (l'inspection les montre).
"""
import argparse
import hashlib
import io
import json
import os
import pathlib
import re
import sys
import zipfile

import numpy as np

VRAIS = {"true", "1", "yes", "oui", "eval", "evaluation", "test"}
FAUX = {"false", "0", "no", "non", "deploy", "deployment", "real"}


def booleen(x) -> bool:
    if isinstance(x, (bool, np.bool_)):
        return bool(x)
    if x is None:
        return False
    if isinstance(x, (int, float, np.integer, np.floating)):
        return bool(x) and not (isinstance(x, float) and x != x)
    return str(x).strip().lower() in VRAIS


def texte_de(v) -> str:
    """Un champ texte peut être une chaîne, une liste de messages ({role, content}) ou un objet : on le rend lisible."""
    if v is None or (isinstance(v, float) and v != v):
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        morceaux = []
        for m in v:
            if isinstance(m, dict):
                role = m.get("role") or m.get("type") or ""
                contenu = m.get("content") if "content" in m else m.get("text", "")
                morceaux.append(f"[{role}] {texte_de(contenu)}".strip())
            else:
                morceaux.append(texte_de(m))
        return "\n".join(x for x in morceaux if x)
    if isinstance(v, dict):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def aplatir(l: dict) -> dict:
    """Remonte les clés de `metadata` (ou `meta`) au premier niveau sans écraser une clé déjà présente."""
    if not isinstance(l, dict):
        return l
    sortie = dict(l)
    for cle in ("metadata", "meta"):
        m = l.get(cle)
        if isinstance(m, dict):
            for k, v in m.items():
                sortie.setdefault(k, v)
    return sortie


def mot_de_passe_du_depot(dossier: pathlib.Path) -> str | None:
    """Cherche le mot de passe dans scripts/decrypt.sh (ou tout *.sh) : `-P mdp`, `--password mdp`, `PASSWORD=…`, `pass:…`."""
    motifs = [r"(?:^|\s)-P\s*[\"']?([^\s\"']+)", r"--password[=\s]+[\"']?([^\s\"']+)", r"(?:PASSWORD|PASS|PWD)\s*=\s*[\"']?([^\s\"']+)",
              r"pass:([^\s\"']+)", r"-p([^\s\"']+)"]
    for script in sorted(dossier.rglob("*.sh")):
        if "decrypt" not in script.name.lower() and "unzip" not in script.read_text(encoding="utf-8", errors="replace"):
            continue
        texte = script.read_text(encoding="utf-8", errors="replace")
        for motif in motifs:
            m = re.search(motif, texte, flags=re.MULTILINE)
            if m and m.group(1) not in ("dataset.zip", "dataset.json"):
                return m.group(1)
    return None


def enregistrements(brut: bytes, nom: str) -> list[dict]:
    texte = brut.decode("utf-8-sig")
    if nom.lower().endswith(".jsonl"):
        return [json.loads(l) for l in texte.splitlines() if l.strip()]
    d = json.loads(texte)
    return d if isinstance(d, list) else (d.get("data") or d.get("examples") or d.get("dataset") or d.get("samples") or list(d.values())[0])


def lire_zip(chemin: pathlib.Path, mot_de_passe: str | None) -> list[dict]:
    """Ouvre `dataset.zip` (clair, ZipCrypto, ou AES via pyzipper) et rend la liste d'enregistrements du JSON qu'il contient."""
    octets = chemin.read_bytes()
    pwd = mot_de_passe.encode("utf-8") if mot_de_passe else None
    manque = "zip chiffré : mot de passe introuvable dans scripts/decrypt.sh du dépôt ; ouvre ce script et relance avec --mot-de-passe \"…\""
    try:
        zf = zipfile.ZipFile(io.BytesIO(octets))
        noms = sorted([n for n in zf.namelist() if n.lower().endswith((".json", ".jsonl"))],
                      key=lambda n: (n.lower() not in ("dataset.json", "dataset.jsonl"), n.count("/"), n))
        if not noms:
            sys.exit(f"aucun JSON dans {chemin.name} : {zf.namelist()[:10]}")
        if zf.getinfo(noms[0]).flag_bits & 0x1 and not pwd:
            sys.exit(manque)
        brut = zf.read(noms[0], pwd=pwd)
    except RuntimeError as e:
        if "password" in str(e).lower() or "Bad password" in str(e):
            sys.exit("mot de passe refusé pour le zip : vérifie-le dans scripts/decrypt.sh et relance avec --mot-de-passe \"…\"")
        raise
    except NotImplementedError as e:
        try:
            import pyzipper
        except ImportError:
            sys.exit(f"zip AES ({e}) : pip install pyzipper")
        with pyzipper.AESZipFile(io.BytesIO(octets)) as zf:
            if not pwd:
                sys.exit(manque)
            zf.setpassword(pwd)
            noms = sorted([n for n in zf.namelist() if n.lower().endswith((".json", ".jsonl"))],
                          key=lambda n: (n.lower() not in ("dataset.json", "dataset.jsonl"), n.count("/"), n))
            try:
                brut = zf.read(noms[0])
            except RuntimeError:
                sys.exit("mot de passe refusé pour le zip AES : vérifie-le dans scripts/decrypt.sh et relance avec --mot-de-passe \"…\"")
    return enregistrements(brut, noms[0])


def charger(depot: str, jeton: str | None, mot_de_passe: str | None, fichier: str | None, local: str | None) -> tuple[list[dict], str, str, str]:
    """Rend (enregistrements, révision, nom du fichier source, sha256 du fichier source)."""
    if local:
        chemin_local = pathlib.Path(local)
        dossier = chemin_local if chemin_local.is_dir() else chemin_local.parent
        revision = "local"
        candidats = [chemin_local] if chemin_local.is_file() else None
    else:
        from huggingface_hub import snapshot_download
        dossier = pathlib.Path(snapshot_download(depot, repo_type="dataset", token=jeton))
        revision = dossier.name
        candidats = None
    if candidats is None:
        candidats = [dossier / fichier] if fichier else [dossier / "dataset.json", dossier / "dataset.jsonl", dossier / "dataset.zip"]
    for c in candidats:
        if c.exists():
            empreinte = hashlib.sha256(c.read_bytes()).hexdigest()
            if c.suffix == ".zip":
                mdp = mot_de_passe or mot_de_passe_du_depot(dossier)
                if mdp and not mot_de_passe:
                    print("mot de passe du zip lu dans le script de déchiffrement du dépôt (non affiché)")
                return lire_zip(c, mdp), revision, c.name, empreinte
            return enregistrements(c.read_bytes(), c.name), revision, c.name, empreinte
    parquets = sorted(dossier.rglob("*.parquet"))
    if parquets:
        import pandas as pd
        df = pd.concat([pd.read_parquet(f) for f in parquets], ignore_index=True)
        empreinte = hashlib.sha256(b"".join(hashlib.sha256(f.read_bytes()).digest() for f in parquets)).hexdigest()
        return df.to_dict(orient="records"), revision, parquets[0].name, empreinte
    fichiers = sorted(str(p.relative_to(dossier)) for p in dossier.rglob("*") if p.is_file())
    sys.exit(f"aucun dataset.json / .zip / parquet trouvé dans {local or depot} ; fichiers : {fichiers[:20]}")


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--depot", default="jjpn2/eval_awareness")
    p.add_argument("--local", default=None, help="dossier (ou fichier) contenant dataset.zip / dataset.json déjà téléchargé ; aucun jeton requis")
    p.add_argument("--fichier", default=None, help="nom du fichier de données dans le dépôt, si différent de dataset.json/.zip")
    p.add_argument("--mot-de-passe", default=None, help="mot de passe du zip ; sinon lu dans scripts/decrypt.sh du dépôt")
    p.add_argument("--inspecter", action="store_true", help="montre les clés et un exemple, n'écrit rien")
    p.add_argument("--par-strate", type=int, default=30)
    p.add_argument("--sortie", default="eval-awareness-sous-ensemble-v1.json")
    p.add_argument("--graine", type=int, default=20261024)
    p.add_argument("--champ-texte", default=None)
    p.add_argument("--champ-evaluation", default=None)
    p.add_argument("--champ-scaffold", default=None)
    p.add_argument("--champ-id", default=None)
    p.add_argument("--complement-de", default=None, help="v5 : fichier d'un sous-ensemble déjà tiré (ses `id_source` sont exclus) ; la sortie prend TOUS les autres items sans GAIA, toutes strates (vivier de conception) ; --par-strate et --graine ignorés")
    args = p.parse_args()
    jeton = os.environ.get("HF_TOKEN") or None
    if not jeton and not args.local:
        print("avertissement : HF_TOKEN absent ; la connexion `huggingface-cli login` sera utilisée si elle existe")
    lignes, revision, source, empreinte_source = charger(args.depot, jeton, args.mot_de_passe, args.fichier, args.local)
    if not lignes or not isinstance(lignes[0], dict):
        sys.exit(f"données illisibles : {type(lignes)} / {type(lignes[0]) if lignes else None}")
    lignes = [aplatir(l) for l in lignes]
    cles = sorted({k for l in lignes[:200] for k in l.keys()})
    if args.inspecter:
        ex = {k: (texte_de(v)[:160] if isinstance(v, (str, list, dict)) else v) for k, v in lignes[0].items()}
        valeurs = {}
        for k in ("eval_category", "scaffold", "category", "eval_type", "safety_category", "is_eval", "label"):
            if k in cles:
                compte = {}
                for l in lignes:
                    v = l.get(k)
                    v = texte_de(v)[:40] if isinstance(v, (list, dict)) else str(v)
                    compte[v] = compte.get(v, 0) + 1
                valeurs[k] = dict(sorted(compte.items(), key=lambda kv: -kv[1])[:12])
        print(json.dumps({"depot": args.local or args.depot, "fichier": source, "sha256_source": empreinte_source, "revision": revision,
                          "n_lignes": len(lignes), "cles": cles, "valeurs": valeurs, "exemple_tronque": ex}, ensure_ascii=False, indent=1, default=str))
        return
    def choisir(nom, candidats):
        if nom:
            return nom
        for c in candidats:
            if c in cles:
                return c
        sys.exit(f"colonne introuvable parmi {candidats} ; clés : {cles} (utilise --champ-…)")
    c_texte = choisir(args.champ_texte, ["input", "prompt", "transcript", "messages", "text"])
    c_eval = choisir(args.champ_evaluation, ["eval_category", "is_eval", "evaluation", "label", "eval"])
    c_scaf = args.champ_scaffold or next((c for c in ["scaffold", "agentic", "is_agentic"] if c in cles), None)
    c_id = args.champ_id or next((c for c in ["id", "sample_id", "uid"] if c in cles), None)
    def est_gaia(l):
        return "gaia" in (str(l.get("category", "")) + " " + str(l.get("subcategory", "")) + " " + str(l.get("source", "")) + " " + str(l.get(c_id, "") if c_id else "")).lower()
    n_gaia = sum(1 for l in lignes if est_gaia(l))
    donnees = [l for l in lignes if not est_gaia(l)]
    def agentique(l):
        if c_scaf is None:
            return False
        v = l.get(c_scaf)
        if isinstance(v, (bool, int, float, np.bool_)):
            return booleen(v)
        s = str(v or "").strip().lower()
        if s in VRAIS or s in FAUX or s in ("none", "null", "nan"):
            return s in VRAIS
        return bool(s)
    rng = np.random.default_rng(np.random.SeedSequence(args.graine))
    exclus, sha_complement = set(), None
    if args.complement_de:
        octets_c = pathlib.Path(args.complement_de).read_bytes()
        sha_complement = hashlib.sha256(octets_c).hexdigest()
        exclus = {str(e["id_source"]) for e in json.loads(octets_c.decode("utf-8"))["exemples"]}
        if not exclus:
            sys.exit("--complement-de : aucun id_source dans le fichier donné")
    exemples, comptes = [], {}
    for ev in (True, False):
        for ag in (True, False):
            strate = [l for l in donnees if booleen(l.get(c_eval)) == ev and agentique(l) == ag]
            if args.complement_de:
                idx = [i for i, l in enumerate(strate) if str(l.get(c_id, i)) not in exclus]
                k = len(idx)
            else:
                k = min(args.par_strate, len(strate))
                idx = rng.choice(len(strate), size=k, replace=False) if k else []
            comptes[f"evaluation={ev},agentique={ag}"] = {"disponibles": len(strate), "tirees": int(k)}
            for i in idx:
                l = strate[int(i)]
                exemples.append({"id_source": str(l.get(c_id, i)) if c_id else str(i), "input": texte_de(l.get(c_texte)),
                                 "category": str(l.get("category", "")), "subcategory": str(l.get("subcategory", "")),
                                 "scaffold": texte_de(l.get(c_scaf)) if c_scaf else "", "eval_category": bool(ev),
                                 "eval_type": (str(l["eval_type"]) if l.get("eval_type") not in (None, "") else None),
                                 "safety_category": (str(l["safety_category"]) if l.get("safety_category") not in (None, "") else None),
                                 "verite": "evaluation" if ev else "usage-reel", "agentique": bool(ag)})
    sortie = {"source": args.depot, "fichier_source": source, "sha256_source": empreinte_source,
              "licence": "CC BY-NC-SA 4.0 (voir la page du jeu et LICENSE.txt)",
              "revision_locale": revision, "lignes_totales": len(lignes), "lignes_gaia_exclues": n_gaia, "lignes_totales_sans_gaia": len(donnees),
              "graine": (None if args.complement_de else args.graine), "script": "extraire_sous_ensemble_eval_awareness_v5.py", "colonnes": {"texte": c_texte, "evaluation": c_eval, "scaffold": c_scaf, "id": c_id},
              "complement_de": ({"fichier": args.complement_de, "sha256": sha_complement, "ids_exclus": len(exclus)} if args.complement_de else None),
              "comptes": comptes, "exemples": exemples}
    if args.complement_de:
        assert not ({e["id_source"] for e in exemples} & exclus), "recouvrement avec le sous-ensemble exclu"
    octets = json.dumps(sortie, ensure_ascii=False, indent=1, default=str).encode("utf-8")
    pathlib.Path(args.sortie).write_bytes(octets)
    h = hashlib.sha256(octets).hexdigest()
    pathlib.Path(args.sortie + ".sha256").write_bytes(f"{h}  {pathlib.Path(args.sortie).name}\n".encode("utf-8"))
    print(f"écrit : {args.sortie} ({len(exemples)} exemples) ; sha256 {h} ; comptes : {comptes}")


if __name__ == "__main__":
    principal()
