"""Mise à disposition : de la fabrication (identifiants internes) aux cas servis aveugles, clé au coffre.

    python -m controle_ia.sparks_exp7_nul_v1.mise_a_disposition preparer --fabrication F/fabrication-v1.json \
        --modeles F/modeles --depart DOSSIER_DU_MODELE_DE_DEPART --servi S --coffre /home/claude/coffre-sparks-exp7-nul-v1 \
        --engagement E.json                         (puis, cas par cas : servir --nom cas_<hex> … ; retirer --nom …)

Écrit : `S/cas_<hex>/{A,B}` (contrôle de fuite passé pour chaque cas, sinon arrêt), `S/ordres-lecteurs-v1.json`
(ordre propre à chaque lecteur, noms seulement), le coffre (clé, secret, empreintes des fichiers servis) et
`E.json` (pour le manifeste : engagement du secret, empreinte de la clé, liste des noms ; rien d'autre).
Les deux paires pilotes (étalonnage) sont servies sous des noms tirés comme les autres et marquées « pilote » au coffre
seulement ; leurs réponses sont scellées et jamais lues ni comptées.
"""
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

from . import aveugle, plan as planmod, recette


def cas_a_servir(fab: dict, pl: dict) -> list[dict]:
    """(identifiant interne, cas du plan servi, type, modèle 1, modèle 2) pour le bras principal, l'ancre et deux paires
    pilotes d'étalonnage (une vraie, une nulle, tirées d'avance : premières de la liste du plan)."""
    out = []
    for ident, c in fab["cas"].items():
        if c["groupe"] not in ("principal", "ancre"):
            continue
        mods = c.get("modeles_remplacement") if not c["ok"] else c["modeles"]
        if mods is None:
            raise aveugle.GardeFuite(f"cas {ident} sans modèles dans les bornes ni remplacement : liste d'arrêt")
        cas_plan = c.get("remplace_par", ident)
        ids = [mods[m.ident] for m in pl[cas_plan].modeles]
        out.append({"cas": ident, "cas_plan": cas_plan, "type": c["type"], "modeles": ids, "pilote": False})
    paires = planmod.paires_etalonnage(pl)
    for t in ("vraie", "hh"):
        _, a, b = next(p for p in paires if p[0] == t)
        fa, fb = fab["modeles"][a]["final"], fab["modeles"][b]["final"]
        if fa and fb:
            out.append({"cas": f"pilote-{t}", "cas_plan": pl[a.rsplit("-", 1)[0]].ident, "type": t, "modeles": [fa, fb],
                        "pilote": True})
    return out


def config_servie(depart_dossier: Path) -> bytes:
    cfg = json.loads((depart_dossier / "config.json").read_text(encoding="utf-8"))
    for k in ("_name_or_path", "name_or_path"):
        cfg.pop(k, None)
    return (json.dumps(cfg, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _tokeniseur_et_config(depart_dossier: Path, tmp: Path):
    from transformers import AutoTokenizer

    AutoTokenizer.from_pretrained(str(depart_dossier)).save_pretrained(str(tmp))
    return {f: aveugle.sha256_fichier(tmp / f) for f in aveugle.FICHIERS_TOKENISEUR}, config_servie(depart_dossier)


def servir_un(nom: str, entree: dict, modeles: Path, depart, depart_dossier: Path, servi: Path, coffre: Path,
              taille: int | None = None) -> dict:
    """Assemble et sert un seul cas (A et B selon la clé), passe le contrôle de fuite, écrit les empreintes des fichiers
    servis au coffre seul (`empreintes-servies-v1/<nom>.json`). Sert à la mise à disposition cas par cas (le disque de
    la session ne tient pas tous les cas à la fois : 53 × 1,74 Go ≈ 92 Go, calcul)."""
    with tempfile.TemporaryDirectory() as tmp:
        ref, cfg = _tokeniseur_et_config(depart_dossier, Path(tmp))
        tA = recette.assembler_point_complet(depart, Path(modeles) / entree["A"] / "final" / "couches.safetensors")
        tB = recette.assembler_point_complet(depart, Path(modeles) / entree["B"] / "final" / "couches.safetensors")
        dest = Path(servi) / nom
        emp = aveugle.servir_cas(dest, tA, tB, cfg, Path(tmp))
    r = aveugle.controle_fuite(dest, sha_tokeniseur_reference=ref, taille_attendue=taille)
    d = Path(coffre) / "empreintes-servies-v1"
    d.mkdir(mode=0o700, exist_ok=True)
    f = d / f"{nom}.json"
    if f.exists() and json.loads(f.read_text(encoding="utf-8")) != emp:
        raise aveugle.GardeFuite(f"{nom} : fichiers servis différents de la première mise à disposition")
    f.write_text(json.dumps(emp, indent=1), encoding="utf-8")
    os.chmod(f, 0o600)
    return r


def lire_cle_preparation(coffre: Path, sha256_cle: str) -> dict:
    """Lecture de la clé par le code de mise à disposition seulement (jamais par le harnais ni l'outil d'attention) ;
    rien n'est imprimé."""
    c = Path(coffre) / "cle-v1.json"
    if aveugle.sha256_fichier(c) != sha256_cle:
        raise aveugle.GardeCoffre("clé du coffre altérée")
    with open(Path(coffre) / "journal-v1.txt", "a", encoding="utf-8") as j:
        j.write(f"{aveugle.datetime.now(aveugle.timezone.utc).isoformat(timespec='seconds')} lecture par la mise à disposition\n")
    return json.loads(c.read_text(encoding="utf-8"))["cle"]["cle"]


def mettre_a_disposition(fabrication: Path, modeles: Path, depart_dossier: Path, servi: Path, coffre: Path,
                         engagement_sortie: Path, *, depot: Path | None = None, secret: int | None = None,
                         servir_tout: bool = True) -> dict:
    """Tire le secret et l'attribution, écrit la clé au coffre et les ordres des lecteurs ; sert tous les cas
    (`servir_tout`) ou aucun (service ensuite cas par cas par `servir_un`)."""
    import torch
    from transformers import AutoModelForCausalLM

    fab = json.loads(Path(fabrication).read_text(encoding="utf-8"))
    if fab.get("arrets"):
        raise aveugle.GardeFuite(f"fabrication arrêtée : {fab['arrets']}")
    pl = planmod.construire_plan()
    liste = cas_a_servir(fab, pl)
    interdits = [Path(servi), Path(modeles).parent] + ([Path(depot)] if depot else [])
    aveugle.verifier_emplacement_coffre(Path(coffre), interdits)
    secret = secret if secret is not None else aveugle.tirer_secret()
    attribution = aveugle.tirer_attribution(secret, [x["cas"] for x in liste])
    roles = {mid: r["role"] for r in fab["modeles"].values() for mid in [r["final"]] if mid}
    comp = {e["ident"]: e["mesure"] for r in fab["modeles"].values() for e in r["essais"]}
    cle, noms = {}, []
    for x in liste:
        a = attribution[x["cas"]]
        m1, m2 = x["modeles"]
        mA, mB = (m1, m2) if a["premier_en_A"] else (m2, m1)
        cle[a["nom"]] = {"cas": x["cas"], "cas_plan": x["cas_plan"], "type": x["type"], "pilote": x["pilote"],
                         "A": mA, "B": mB, "roles": {mA: roles[mA], mB: roles[mB]},
                         "comportement": {mA: comp.get(mA), mB: comp.get(mB)}}
        noms.append((a["nom"], x["pilote"], x["type"] == "ancre"))
    sortie_coffre = aveugle.ecrire_coffre(Path(coffre), secret, {"cle": cle}, interdits=interdits)
    Path(servi).mkdir(parents=True, exist_ok=True)
    if servir_tout:
        depart = AutoModelForCausalLM.from_pretrained(str(depart_dossier), dtype=torch.float32)
        taille = None
        for nom, entree in cle.items():
            taille = servir_un(nom, entree, modeles, depart, depart_dossier, servi, coffre, taille)["taille"]
    ordres = {}
    principaux = [n for n, p, an in noms if not p and not an]
    for l in planmod.LECTEURS:
        ordres[l] = {"principal": aveugle.ordre_lecteur(principaux, planmod.generateur_tache(f"ordre-des-cas-{l}")),
                     "ancre": sorted(n for n, p, an in noms if an), "pilotes": sorted(n for n, p, an in noms if p)}
    (Path(servi) / "ordres-lecteurs-v1.json").write_text(json.dumps(ordres, indent=1), encoding="utf-8")
    eng = {**sortie_coffre, "n_cas": len(noms)}
    Path(engagement_sortie).write_text(json.dumps(eng, indent=1), encoding="utf-8")
    return eng


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="mise_a_disposition")
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("preparer", help="secret, clé au coffre, ordres ; --tout pour servir aussi tous les cas")
    for k in ("fabrication", "modeles", "depart", "servi", "coffre", "engagement"):
        p.add_argument(f"--{k}", required=True)
    p.add_argument("--depot", default=str(Path(__file__).resolve().parents[3]))
    p.add_argument("--tout", action="store_true")
    u = sp.add_parser("servir", help="sert un cas, contrôle de fuite compris")
    for k in ("nom", "modeles", "depart", "servi", "coffre", "engagement"):
        u.add_argument(f"--{k}", required=True)
    r_ = sp.add_parser("retirer", help="retire un cas servi après ses lecteurs")
    r_.add_argument("--nom", required=True)
    r_.add_argument("--servi", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "preparer":
        r = mettre_a_disposition(Path(a.fabrication), Path(a.modeles), Path(a.depart), Path(a.servi), Path(a.coffre),
                                 Path(a.engagement), depot=Path(a.depot), servir_tout=a.tout)
        print(f"PREPARATION : {r['n_cas']} cas ; engagement {r['engagement_secret'][:12]}…")
    elif a.cmd == "servir":
        import torch
        from transformers import AutoModelForCausalLM

        if not aveugle.NOM_CAS.match(a.nom):
            raise SystemExit("nom de cas invalide")
        eng = json.loads(Path(a.engagement).read_text(encoding="utf-8"))
        cle = lire_cle_preparation(Path(a.coffre), eng["sha256_cle"])
        depart = AutoModelForCausalLM.from_pretrained(a.depart, dtype=torch.float32)
        servir_un(a.nom, cle[a.nom], Path(a.modeles), depart, Path(a.depart), Path(a.servi), Path(a.coffre))
        print(f"SERVI {a.nom} : contrôle de fuite passé")
    else:
        import shutil

        if not aveugle.NOM_CAS.match(a.nom):
            raise SystemExit("nom de cas invalide")
        shutil.rmtree(Path(a.servi) / a.nom)
        print(f"RETIRE {a.nom}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
