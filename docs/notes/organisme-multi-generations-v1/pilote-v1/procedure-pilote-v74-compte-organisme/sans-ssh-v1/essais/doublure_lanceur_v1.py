"""Doublure du lanceur v74 pour les essais de l'amorce sans ssh — v1. Jamais sur la machine louée (le programme machine refuse
ESSAI_LANCEUR hors essai). `bloc` et `secret` sont délégués au vrai lanceur de l'arbre (même dossier de travail) ; les autres
sous-commandes imitent les sorties attendues (formes lues dans repetition-locale/) et suivent le scénario écrit à côté de ce fichier
(`scenario.json`) : {"jouer_reel": [code, …] (un code par lancement réel successif), "jouer_reel_comptes": {…},
"fuite_cle": bool (écrit la valeur de la clé du premier fournisseur dans un journal de relais : le balayage doit refuser la poussée),
"duree_jouer_s": n, "generer_code": n}.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
SC = json.load(open(os.path.join(ICI, "scenario.json"), encoding="utf-8"))
H64 = lambda s: hashlib.sha256(s.encode()).hexdigest()  # noqa: E731


def ecrire(chemin, objet):
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(objet, f, sort_keys=True)
    s = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{s}  {os.path.basename(chemin)}\n")
    return s


def arg(a, n):
    return a[a.index(n) + 1]


def main(a):
    c = a[0]
    if c in ("bloc", "secret"):
        return subprocess.call([sys.executable, "-I", "-B", "demonstrations/pilote_mr2_v74.py"] + a)
    if c == "generer":
        if SC.get("generer_code", 0):
            print("refus : monde non conforme (doublure)", file=sys.stderr)
            return SC["generer_code"]
        sortie = arg(a, "--sortie")
        open(sortie, "x").write(json.dumps({"mondes": "doublure"}))
        h = hashlib.sha256(open(sortie, "rb").read()).hexdigest()
        json.dump({"fichier_mondes_sha256": h, "mondes_sha256": [H64(f"monde{k}") for k in range(1, 5)], "texte_sha256": arg(a, "--texte-sha256")},
                  open(sortie + ".engagement.json", "x"))
        print(json.dumps({"controles": [{"conforme": True, "monde": k, "spec_sha256": H64(f"spec{k}"), "tirages_refuses": []} for k in range(1, 5)],
                          "fichier_mondes_sha256": h}))
        return 0
    if c == "preparer":
        print(json.dumps({"c16": {"1:k1": {"admise": True, "loi_sha256": H64("l")}}, "c17": {}, "episodes_servis": {},
                          "gabarit_sha256": "e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2", "heritages_sha256": {},
                          "mondes": {}, "textes_servis": {}}))
        return 0
    if c == "jouer":
        mode, sortie = arg(a, "--mode"), arg(a, "--sortie")
        if os.path.exists(sortie):
            print("refus : dossier de sortie existant", file=sys.stderr)
            return 2
        code, comptes = 0, {"complet": 16, "echec": 0, "tronque": 0}
        if mode == "reel":
            n = len([x for x in os.listdir(os.path.dirname(sortie)) if x.startswith("journal-09-")]) - 1
            codes = SC.get("jouer_reel", [0])
            code = codes[min(n, len(codes) - 1)]
            comptes = SC.get("jouer_reel_comptes", comptes)
            if code == 2:
                print("refus : port occupé (doublure)", file=sys.stderr)
                return 2
            with open(arg(a, "--registre-lancements"), "a") as f:
                f.write(json.dumps({"texte_sha256": arg(a, "--texte-sha256"), "sortie": sortie}) + "\n")
        os.makedirs(os.path.join(sortie, "prive"))
        open(os.path.join(sortie, "prive", "texte-servi-monde-1.txt"), "w").write("texte servi privé (doublure)")
        time.sleep(SC.get("duree_jouer_s", 0) if mode == "reel" else 0)
        j = os.path.join(sortie, "journal-relais-opus55.jsonl")
        with open(j, "w") as f:
            f.write(json.dumps({"appel": 1, "doublure": True}) + "\n")
            if mode == "reel" and SC.get("fuite_cle"):
                f.write(os.environ.get("RR_ANTHROPIC_API_KEY_RIGAUD", "") + "\n")
        partiel = code == 3
        sc = ecrire(os.path.join(sortie, "CARTES-partiel.json" if partiel else "CARTES.json"), {"cartes": []})
        ecrire(os.path.join(sortie, "manifeste-pilote-v70.json"), {"partiel": partiel})
        print(json.dumps({"lanceur": "doublure", "mode": mode, "cartes_sha256": sc, "comptes": comptes, "abandonnes": {},
                          "arret": "ArretPilote : doublure" if partiel else None}))
        return code
    if c == "mesurer":
        sortie = arg(a, "--sortie")
        ecrire(os.path.join(sortie, "sortie-mesure-pilote-v70.json"), {"doublure": True})
        print(json.dumps({"programme_sha256": "676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365", "sortie": "sortie-mesure-pilote-v70.json"}))
        return SC.get("mesurer_code", 0)
    if c == "lire":
        ecrire(arg(a, "--ecrire"), {"issue": "doublure"})
        print(json.dumps({"issue": "doublure (non ouverte)"}))
        return 0
    if c == "rapatrier":
        src, dst = arg(a, "--source"), arg(a, "--destination")
        os.makedirs(dst)
        copies = []
        for n in sorted(os.listdir(src)):
            p = os.path.join(src, n)
            if os.path.isfile(p):
                open(os.path.join(dst, n), "wb").write(open(p, "rb").read())
                copies.append(n)
        print(json.dumps({"aucun_monde": True, "copies": copies}))
        return 0
    print("doublure : sous-commande inconnue", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
