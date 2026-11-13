"""Mutations neuves du contre-lecteur sur le code v69 du pilote MR-2 (hors des 88 du banc du développeur) — v1.

Outil de la contre-lecture `contre-lecture-differentiel-code-pilote-v69-v1.md` (lecteur : Claude Fable 5.2). Aucun réseau hors de la boucle
locale des essais (relais à amont factice), aucune clé, aucun appel de modèle. Pour chaque mutation : copie neuve de
`orchestrator/` (clone en lecture du contre-lecteur) dans un dossier provisoire du bac à sable, un remplacement textuel présent
**une seule fois** dans le fichier visé (sinon défaut de l'outil), empreinte de la commande ou du relais recopiée dans la
configuration de la copie quand l'un d'eux est muté, puis **la suite entière** des essais du pilote (88 essais), pas une
sélection : « survit » veut dire qu'aucun des 88 essais ne la voit. Un seul processus à la fois.

  ulimit -v 6000000 ; OMP_NUM_THREADS=2 python3 -I -B mutations_contre_lecteur_v69_v1.py --orchestrateur CLONE/orchestrator \
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

T = "essais/test_pilote_mr2_v69.py"
PC, PR, AU, LA = "pole/pilote_mr2_v69.py", "pole/proposeurs_pilote_v69.py", "pole/audit_pilote_v69.py", "demonstrations/pilote_mr2_v69.py"
CO, RE = "exemples/pilote-mr2-v69/commandes/commande_pilote_v69.py", "exemples/pilote-mr2-v69/commandes/relais_pilote_v69.py"
CONF = "exemples/pilote-mr2-v69/configuration-pilote-mr2-v10.json"


def M(ident, fichier, avant, apres, garde):
    return {"id": ident, "fichier": fichier, "avant": avant, "apres": apres, "garde": garde}


MUTATIONS = [
    M("W1-environnement-entier-passe-au-relais", PR,
      "    env = {k: environ[k] for k in ENV_FILTRE if k in environ}\n", "    env = dict(environ)\n",
      "environnement du relais bâti par filtrage des noms (aucune autre variable, aucune autre clé, ne passe au relais)"),
    M("W2-engagement-non-lie-au-fichier-des-mondes", PC,
      "    if e.get(\"texte_sha256\") != texte_sha256 or e.get(\"fichier_mondes_sha256\") != sha_fichier:\n",
      "    if e.get(\"texte_sha256\") != texte_sha256:\n",
      "mode réel : l'engagement lie le fichier des mondes, pas seulement le texte (m-3)"),
    M("W3-temoin-consigne-de-la-commande-non-controlee", PR,
      "\"consigne_commande\": temoin[\"consigne_commande_sha256\"] == sha_texte,", "\"consigne_commande\": True,",
      "témoin d'isolement : l'empreinte de la consigne lue par la commande égale celle du texte servi"),
    M("W4-gabarit-du-texte-servi-non-relu", PC,
      "    if ctx.get(\"gabarit\") != json.loads(json.dumps(gabarit()[\"gabarit\"])):\n", "    if False:\n",
      "relecture du texte servi : le gabarit du contexte est le gabarit gelé (M-6)"),
    M("W5-manifeste-altere-admis-a-la-mesure", LA,
      " or not PR._compagnon_egal(man):\n", ":\n",
      "mesurer : le manifeste égale son compagnon avant la mesure (M-5)"),
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
                       capture_output=True, text=True, timeout=2400,
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
    res = {"outil": "mutations_contre_lecteur_v69_v1", "debut_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "suite": T + " (entière, 88 essais)", "mutations": []}
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
