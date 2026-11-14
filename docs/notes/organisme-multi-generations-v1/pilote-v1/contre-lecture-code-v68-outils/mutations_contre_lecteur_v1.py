"""Mutations du contre-lecteur sur le code v68 du pilote MR-2 (hors de la liste des 43 du développeur) — v1.

Outil de la contre-lecture `contre-lecture-code-pilote-v68-v1.md` (lecteur : Claude Fable 5.2). Aucun réseau hors de la boucle
locale des essais (relais à amont factice), aucune clé, aucun appel de modèle. Pour chaque mutation : copie neuve de
`orchestrator/` (clone en lecture du contre-lecteur) dans un dossier provisoire du bac à sable, un remplacement textuel présent
**une seule fois** dans le fichier visé (sinon défaut de l'outil), empreinte de la commande ou du relais recopiée dans la
configuration de la copie quand l'un d'eux est muté, puis **la suite entière** des essais du pilote (51 essais), pas une
sélection : « survit » veut dire qu'aucun des 51 essais ne la voit. Un seul processus à la fois.

  ulimit -v 6000000 ; OMP_NUM_THREADS=2 python3 -I -B mutations_contre_lecteur_v1.py --orchestrateur CLONE/orchestrator \
      --travail BAC --python PYTHON --sortie RESULTAT.json
Codes : 0 exécution complète (lire le bilan) ; 2 défaut de l'outil (essais sains en échec sur la copie non mutée, texte absent).
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

T = "essais/test_pilote_mr2_v68.py"
PC, PR, AU, LA = "pole/pilote_mr2_v68.py", "pole/proposeurs_pilote_v68.py", "pole/audit_pilote_v68.py", "demonstrations/pilote_mr2_v68.py"
CO, RE = "exemples/pilote-mr2-v68/commandes/commande_pilote_v68.py", "exemples/pilote-mr2-v68/commandes/relais_pilote_v68.py"
CONF = "exemples/pilote-mr2-v68/configuration-pilote-mr2-v9.json"


def M(ident, fichier, avant, apres, garde):
    return {"id": ident, "fichier": fichier, "avant": avant, "apres": apres, "garde": garde}


MUTATIONS = [
    M("N1-go-non-lus-en-mode-reel", LA,
      "        go = PR.lire_go_du_pilote(conf, args.registre_go, args.go_pi1, args.go_pi2)\n", "        go = None\n",
      "mode réel : les deux lignes de GO sont lues et vérifiées avant tout appel (C-9, C-11)"),
    M("N2-empreinte-du-texte-scelle-non-comparee", LA,
      "        if sha256_fichier(args.texte) != args.texte_sha256:\n", "        if False:\n",
      "mode réel : le texte scellé égale l'empreinte donnée au lancement (liste d'arrêt, première ligne)"),
    M("N3-relais-non-branche-admis", PR,
      "        if not e.get(\"branche\"):\n", "        if False:\n",
      "avant tout appel : chaque relais est branché (le mode réel refuse tant que la voie de Claude ne l'est pas)"),
    M("N4-relais-plafond-modele-appels-non-controles", PR,
      "        if e.get(\"modele\") != p[\"modele\"] or abs(float(e.get(\"plafond_usd\", -1)) - p[\"part_usd\"]) > 1e-9 \\\n"
      "                or e.get(\"appels\") != 0 or e.get(\"regle_usd\") != 0.0 or e.get(\"relais\") != f\"relais-pilote-v68-{nom}\":\n",
      "        if False:\n",
      "avant tout appel : relais sur le bon modèle, plafond égal à la part, aucun appel ni dépense déjà faits (C-7, C-9)"),
    M("N5-relais-usage-absent-compte-zero", RE,
      "                if u is not None:\n                    cout = (u[0] * a.prix_entree + u[1] * a.prix_sortie) / 1e6\n",
      "                cout = (u[0] * a.prix_entree + u[1] * a.prix_sortie) / 1e6 if u is not None else 0.0\n",
      "relais : une réponse sans usage lisible est réglée au pire cas, jamais à zéro (plafond dur du relais)"),
    M("N6-commande-cout-au-dessus-du-pire-cas-admis", CO,
      "    if cout > pire + 1e-9:\n", "    if False:\n",
      "commande : un coût lu au-dessus du pire cas est un échec (code 5)"),
    M("N7-temoin-outils-non-controles", PR,
      " and temoin[\"outils\"] == [] and temoin[\"messages\"] == 1", " and temoin[\"messages\"] == 1",
      "témoin d'isolement : aucun outil envoyé à l'amont (C-10), contrôlé par l'adaptateur"),
    M("N8-rapatriement-marques-de-monde-ignorees", AU,
      "    return any(m in texte for m in MARQUES_DE_MONDE)\n", "    return False\n",
      "rapatriement : un fichier dont le contenu dit un devis de monde est refusé, même sans l'empreinte du fichier des mondes (C-18)"),
]


def preparer_copie(source, d, m=None):
    orch = os.path.join(d, "orchestrator")
    shutil.copytree(source, orch, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    if m is None:
        return orch
    f = os.path.join(orch, m["fichier"])
    with open(f, encoding="utf-8") as h:
        t = h.read()
    if t.count(m["avant"]) != 1:
        raise RuntimeError(f"{m['id']} : texte avant présent {t.count(m['avant'])} fois")
    with open(f, "w", encoding="utf-8") as h:
        h.write(t.replace(m["avant"], m["apres"]))
    if m["fichier"] in (CO, RE):
        c = os.path.join(orch, CONF)
        with open(c, encoding="utf-8") as h:
            conf = json.load(h)
        cle = "commande" if m["fichier"] == CO else "relais"
        with open(f, "rb") as h:
            conf[cle]["sha256"] = hashlib.sha256(h.read()).hexdigest()
        with open(c, "w", encoding="utf-8") as h:
            json.dump(conf, h, ensure_ascii=False, indent=1)
    return orch


def jouer(orch, python, tmp):
    r = subprocess.run([python, "-I", "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", T, "-rfE"], cwd=orch,
                       capture_output=True, text=True, timeout=1500,
                       env={"PATH": "/usr/bin:/bin", "OMP_NUM_THREADS": "2", "HOME": tmp, "TMPDIR": tmp})
    echecs = sorted(set(re.findall(r"(?:SUBFAILED\[[^\]]*\]|FAILED|ERROR) \S+::(\w+)(?:::(\w+))?", r.stdout)))
    derniere = (r.stdout.strip().splitlines() or [""])[-1]
    return r.returncode, [b or a for a, b in echecs], derniere


def principal(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--orchestrateur", required=True)
    a.add_argument("--travail", required=True)
    a.add_argument("--python", required=True)
    a.add_argument("--sortie", required=True)
    a.add_argument("--seulement", default=None)
    args = a.parse_args(argv)
    if os.path.exists(args.sortie):
        print("sortie existante", file=sys.stderr)
        return 2
    tmp = os.path.join(args.travail, "tmp-essais")
    os.makedirs(tmp, exist_ok=True)
    choisies = [m for m in MUTATIONS if not args.seulement or m["id"].split("-")[0] in args.seulement.split(",")]
    res = {"outil": "mutations_contre_lecteur_v1", "debut_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "suite": T + " (entière, 51 essais)", "mutations": []}
    d = os.path.join(args.travail, "copie-saine")
    shutil.rmtree(d, ignore_errors=True)
    orch = preparer_copie(args.orchestrateur, d)
    code, echecs, derniere = jouer(orch, args.python, tmp)
    shutil.rmtree(d, ignore_errors=True)
    res["sain"] = {"code": code, "echecs": echecs, "derniere_ligne": derniere}
    print(f"sain : code {code} ; {derniere}", flush=True)
    code_sortie = 0
    if code != 0:
        res["defaut"] = "essais sains en échec sur la copie non mutée"
        code_sortie = 2
    else:
        for m in choisies:
            d = os.path.join(args.travail, "copie-" + m["id"].split("-")[0])
            shutil.rmtree(d, ignore_errors=True)
            try:
                orch = preparer_copie(args.orchestrateur, d, m)
            except RuntimeError as e:
                res["mutations"].append(dict(m, issue="défaut de l'outil", detail=str(e)))
                code_sortie = 2
                continue
            code, echecs, derniere = jouer(orch, args.python, tmp)
            shutil.rmtree(d, ignore_errors=True)
            issue = "survit" if code == 0 else "tuée"
            res["mutations"].append(dict(m, issue=issue, code=code, echecs=echecs, derniere_ligne=derniere))
            print(f"{m['id']} : {issue} {echecs} ; {derniere}", flush=True)
    res["fin_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    res["bilan"] = {i: sum(1 for x in res["mutations"] if x["issue"] == i) for i in sorted({x["issue"] for x in res["mutations"]})}
    with open(args.sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(json.dumps(res["bilan"], ensure_ascii=False))
    return code_sortie


if __name__ == "__main__":
    sys.exit(principal())
