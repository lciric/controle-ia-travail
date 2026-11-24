"""Réunion de la branche de la formation du barreau 5 (mot de Lazar du 24 novembre : « réunion des sept commits ok »).

Pour chaque instance de la pièce des sorties de la formation (41e51f99…, commit 3dff7bed…) : commit prouvé ancêtre de la
tête citée ; empreinte de traces-b5f/inventaire-final.json au commit prouvé égale à celle de la pièce ; nombre de fichiers
égal ; extraction des seuls fichiers de l'inventaire sous donnees/, diag/ et runs/ (un dossier par marche), chacun vérifié
à sa taille et à son empreinte. N'affiche que des comptes et des empreintes ; n'ouvre aucun contenu pour le lire.
Usage : python3 -I reunion-formation-v1.py DEPOT SORTIE
"""
import hashlib, json, subprocess, sys
from pathlib import Path

PIECE = [  # instance, branche, commit prouvé, tête, marche, fichiers, inventaire sha256 (pièce 41e51f99…)
    ("1-x1", "eb4b946c333be96515f3c36fa9537816259673ac", "b5b5917946221e09f7b56ba664f4635cd54df34d", "20261121-055443-b5f-formation-1-x1", 53, "c9f9310df9f1efcf60334c9dab2070ad871a1fc8ad10c28e5eb1e794c8e8f293"),
    ("2-x1", "7b0e19b928d76c1f655dc512eea72440a570ebce", "e6923e7250b369b02489ee29d0aacdc4233abf83", "20261121-060152-b5f-formation-2-x1", 53, "1a30355a2834da19093e614c708b81ba5007f27c8e7d32b9adde2495879c7eae"),
    ("3-x1", "f74795a16c609eb00cc86c5043bf211805c428bb", "8615f2aab048cce9418a9fce8084e601997a8bae", "20261121-071239-b5f-formation-3-x1", 53, "01031f467a5f2d59c808adbf9c407b78efa0bfc8ee8c862d001efe0b0241f057"),
    ("4-x1", "75814afec793814f44afff946344e94d46ea8f0e", "c23e6a03d957b77c783cf13d303def63e2590c84", "20261121-072248-b5f-formation-4-x1", 53, "a0cb97cbc13c15f2de10306638b6b4d2bf4c70660db69fc28745b22bd40e4ea6"),
    ("5-x1", "e37790479d51c4f5fd7d68f11037254f15749de5", "33431bf85975f10c195b5964bf2c09dc3ea439e4", "20261120-144431-b5f-formation-5-x1", 53, "436675e2a567213910038c796f4d39400055dcce32cea2289508fd180c6137b3"),
    ("6", "0a6af341244900da047ea850a966bf137dee279b", "85a4942b02178edb2bf228a0b995bee2dcf4e97d", "20261120-012937-b5f-formation-6", 53, "6d80070c2c7ec895a87b599e720fb3b12e93bc1fd1758d01481480a96bddcf88"),
    ("7-x1", "7714b0ac6a9a11cd2b1644a747bda0dcccec513a", "a7bc1faea6edce7780ef0a693c2388c6c102b976", "20261120-144552-b5f-formation-7-x1", 35, "1e82f1d92528c81fca0aed1c25b1f8980a05d9ad478777ffe246bc408190087c"),
]


def git(depot, *a, binaire=False):
    r = subprocess.run(["git", "-C", depot, *a], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"ARRET : git {' '.join(a[:2])} : {r.stderr.decode()[:200]}")
    return r.stdout if binaire else r.stdout.decode()


def main(depot, sortie):
    sortie = Path(sortie)
    if sortie.exists():
        raise SystemExit(f"ARRET : {sortie} existe déjà (R12)")
    rapport = []
    for inst, prouve, tete, marche, n, inv_sha in PIECE:
        b = f"origin/donnees/barreau5-familles-jumelles-v1-formation-instance-{inst}"
        if git(depot, "rev-parse", b).strip() != tete:
            raise SystemExit(f"ARRET : instance {inst} : tête distante ≠ tête de la pièce")
        if subprocess.run(["git", "-C", depot, "merge-base", "--is-ancestor", prouve, tete]).returncode != 0:
            raise SystemExit(f"ARRET : instance {inst} : commit prouvé non ancêtre de la tête")
        inv = git(depot, "show", f"{prouve}:traces-b5f/inventaire-final.json", binaire=True)
        if hashlib.sha256(inv).hexdigest() != inv_sha:
            raise SystemExit(f"ARRET : instance {inst} : empreinte de l'inventaire ≠ pièce")
        d = json.loads(inv)
        if d.get("run_id") != marche or len(d["fichiers"]) != n:
            raise SystemExit(f"ARRET : instance {inst} : marche ou nombre de fichiers ≠ pièce")
        extraits = 0
        for f in d["fichiers"]:
            ch = f["chemin"]
            if ch.startswith("traces-b5f/"):
                continue
            if not (ch.startswith(f"donnees/{marche}/") or ch.startswith(f"diag/{marche}/") or ch.startswith(f"runs/{marche}/")):
                raise SystemExit(f"ARRET : instance {inst} : chemin hors de la marche dans l'inventaire")
            octets = git(depot, "show", f"{prouve}:{ch}", binaire=True)
            if hashlib.sha256(octets).hexdigest() != f["sha256"] or ("octets" in f and len(octets) != f["octets"]):
                raise SystemExit(f"ARRET : instance {inst} : fichier différent de l'inventaire")
            p = sortie / ch
            if p.exists():
                raise SystemExit(f"ARRET : instance {inst} : chemin déjà écrit par une autre instance")
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(octets)
            extraits += 1
        rapport.append({"instance": inst, "commit_prouve": prouve, "marche": marche, "inventaire_sha256": inv_sha,
                        "fichiers_inventaire": n, "fichiers_extraits": extraits})
        print(f"instance {inst} : inventaire égal à la pièce ; {extraits} fichiers extraits et vérifiés")
    (sortie.parent / "journal").mkdir(exist_ok=True)
    out = sortie.parent / "journal" / "reunion-formation-v1.json"
    out.write_text(json.dumps({"piece": "docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/sorties-formation-b5f-v1.md",
                               "piece_sha256": "41e51f9970eda5f4351cac01a41a97296741d5f2ce5e62ba46d56e8af9fc04e6",
                               "piece_commit": "3dff7bed46ce62def89dddf835a372f6e2b23b72", "instances": rapport},
                              indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("réunion faite :", sum(r["fichiers_extraits"] for r in rapport), "fichiers")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
