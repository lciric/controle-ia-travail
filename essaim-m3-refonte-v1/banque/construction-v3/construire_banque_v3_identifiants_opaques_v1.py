"""Banque `confrontation-v3` : la banque `confrontation-v1` sous des identifiants opaques, la clé gardée secrète et
chaque part triée par identifiant nouveau — v1 de ce script.

Remplace la v2 (`banque-confrontation-v2.json`, 52beb637…, jamais servie), sur la contre-lecture
`CONTRE-LECTURE-banque-v2-v1.md` (5ee8df41…) : BC1-01 (l'entropie de la v2 était publiée et l'ordre de la v1, rangé par
vérité, gardé : qui a l'entropie retrouve toutes les vérités) et BC1-06 (cet ordre n'est pas nécessaire à la référence
de surface).

Ce que fait ce script, et rien d'autre : mêmes 200 tâches, mêmes champs (`famille`, `texte`, `etiquettes`, `verite`,
`source`), mêmes parts ; `id` change et **chaque part est triée par identifiant nouveau**. Les tâches, prises dans
l'ordre du fichier v1 (train, test, test_final), reçoivent `t-0001` à `t-0200` selon
`numpy.random.default_rng(numpy.random.SeedSequence(E)).permutation(200)` (la tâche de rang i reçoit
`t-{permutation[i] + 1:04d}`). **L'entropie E n'est écrite que dans le fichier de clé** (`…-cle.json`, secret comme le
fichier secret) ; le manifeste n'en garde que l'empreinte sha256 de son écriture décimale (engagement vérifiable). Le
fichier secret v3 garde, pour chaque identifiant nouveau, le dossier secret v1 et l'ancien identifiant (`id_v1`).

Usage : python3 -I construire_banque_v3_identifiants_opaques_v1.py BANQUE_V1 SECRET_V1 DOSSIER_SORTIE [--entropie E]
Refuse : numpy < 1.25 ; empreintes de la v1 ou de son secret autres que celles attendues ; compagnons absents ou
différents ; fichier de sortie existant (R12) ; tout écart de forme. N'imprime jamais E (seulement son empreinte).
"""
import datetime
import hashlib
import json
import pathlib
import secrets
import sys

import numpy as np

SHA_V1 = "f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc"
SHA_SECRET_V1 = "c68d7d4ba34b49b85a9327adfe21d30cc8118f1d100a47db2a47e97329715caf"
PARTS = ("train", "test", "test_final")
CHAMPS = ("id", "famille", "texte", "etiquettes", "verite", "source")
NOM, NOM_SECRET, NOM_CLE = "banque-confrontation-v3.json", "banque-confrontation-v3-secret.json", "banque-confrontation-v3-cle.json"


def refus(msg: str) -> None:
    sys.exit(f"REFUS : {msg}")


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def lire_scelle(p: pathlib.Path, attendu: str) -> dict:
    if sha(p) != attendu:
        refus(f"{p.name} : empreinte {sha(p)[:16]}… au lieu de {attendu[:16]}…")
    c = p.with_name(p.name + ".sha256")
    if not c.exists() or c.read_text(encoding="utf-8").split()[0] != attendu:
        refus(f"{p.name} : compagnon .sha256 absent ou différent")
    return json.loads(p.read_text(encoding="utf-8"))


def ecrire_scelle(p: pathlib.Path, contenu) -> str:
    if p.exists() or p.with_name(p.name + ".sha256").exists():
        refus(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(contenu, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    h = sha(p)
    p.with_name(p.name + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def identifiants(entropie: int, n: int) -> list[str]:
    permutation = np.random.default_rng(np.random.SeedSequence(entropie)).permutation(n)
    return [f"t-{int(permutation[i]) + 1:04d}" for i in range(n)]


def principal(argv: list[str]) -> int:
    if tuple(int(x) for x in np.__version__.split(".")[:2]) < (1, 25):
        refus(f"numpy {np.__version__} < 1.25 (R9)")
    args = list(argv)
    entropie = None
    if "--entropie" in args:
        i = args.index("--entropie")
        entropie = int(args[i + 1])
        del args[i:i + 2]
    if len(args) != 3:
        refus("usage : BANQUE_V1 SECRET_V1 DOSSIER_SORTIE [--entropie E]")
    p_v1, p_s1, sortie = pathlib.Path(args[0]), pathlib.Path(args[1]), pathlib.Path(args[2])
    v1 = lire_scelle(p_v1, SHA_V1)
    s1 = lire_scelle(p_s1, SHA_SECRET_V1)
    if sorted(v1) != ["manifeste", "test", "test_final", "train"]:
        refus(f"clés de la v1 inattendues : {sorted(v1)}")
    taches = [(part, t) for part in PARTS for t in v1[part]]
    n = len(taches)
    ids_v1 = [t["id"] for _, t in taches]
    if len(set(ids_v1)) != n or set(ids_v1) != set(s1):
        refus("identifiants v1 en double, ou secret v1 qui ne couvre pas exactement les tâches")
    for _, t in taches:
        if tuple(sorted(t)) != tuple(sorted(CHAMPS)):
            refus(f"{t['id']} : champs {sorted(t)} au lieu de {sorted(CHAMPS)}")
    if entropie is None:
        entropie = secrets.randbits(128)
    nouveaux = identifiants(entropie, n)
    if len(set(nouveaux)) != n or set(nouveaux) & set(ids_v1):
        refus("identifiants nouveaux en double ou communs avec la v1")
    v3 = {part: [] for part in PARTS}
    secret = {}
    for (part, t), nid in zip(taches, nouveaux):
        v3[part].append({"id": nid, **{k: t[k] for k in CHAMPS if k != "id"}})
        dossier = dict(s1[t["id"]])
        if "id_v1" in dossier:
            refus(f"{t['id']} : champ id_v1 déjà présent dans le secret v1")
        dossier["id_v1"] = t["id"]
        secret[nid] = dossier
    for part in PARTS:
        v3[part].sort(key=lambda x: x["id"])
    secret = {k: secret[k] for k in sorted(secret)}
    empreinte_e = hashlib.sha256(str(entropie).encode("ascii")).hexdigest()
    manifeste = dict(v1["manifeste"])
    manifeste["nom"] = "confrontation-v3"
    manifeste["quand_utc"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifeste["identifiants_opaques"] = {
        "derivee_de": {"banque": p_v1.name, "sha256": SHA_V1, "secret": p_s1.name, "secret_sha256": SHA_SECRET_V1,
                       "nom": v1["manifeste"].get("nom"), "quand_utc": v1["manifeste"].get("quand_utc")},
        "entropie_sha256": empreinte_e,
        "regle": ("seuls `id` et l'ordre changent : les 200 tâches, dans l'ordre du fichier v1 (train, test, "
                  "test_final), reçoivent t-{permutation[i] + 1:04d}, permutation = numpy.random.default_rng("
                  "numpy.random.SeedSequence(E)).permutation(200) ; chaque part est triée par identifiant nouveau ; "
                  "E n'est écrite que dans le fichier de clé, secret ; ce manifeste n'en garde que l'empreinte sha256 "
                  "de son écriture décimale"),
        "script": "construction-v3/construire_banque_v3_identifiants_opaques_v1.py",
        "numpy": np.__version__,
    }
    v3["manifeste"] = manifeste
    sortie.mkdir(parents=True, exist_ok=True)
    h3 = ecrire_scelle(sortie / NOM, {k: v3[k] for k in ("train", "test", "test_final", "manifeste")})
    hs3 = ecrire_scelle(sortie / NOM_SECRET, secret)
    hc3 = ecrire_scelle(sortie / NOM_CLE, {"banque": NOM, "entropie_seed_sequence": str(entropie),
                                           "entropie_sha256": empreinte_e, "regle": manifeste["identifiants_opaques"]["regle"]})
    print(json.dumps({"banque_v3": NOM, "sha256": h3, "secret_v3": NOM_SECRET, "secret_sha256": hs3, "cle": NOM_CLE,
                      "cle_sha256": hc3, "entropie_sha256": empreinte_e, "n": n, "numpy": np.__version__}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
