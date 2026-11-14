"""Épreuve X9 du contre-lecteur sur le code v69 : `mesurer` accepte-t-il un fichier des mondes autre que celui du manifeste ?

Un essai à blanc (relais factices) est joué sur les mondes de développement ; puis `mesurer` est lancé avec un **autre** fichier
de quatre mondes **publics d'essai** (étiquette publique des essais du développeur, écrits dans un dossier privé du bac à sable,
supprimés à la fin). Rien d'un monde n'est écrit dans la sortie : codes, booléens, empreintes.

  ulimit -v 6000000 ; env -i PATH=/usr/bin:/bin OMP_NUM_THREADS=2 python3 -I -B epreuve_mesure_autres_mondes_v69_v1.py \
      ORCHESTRATEUR MONDES.json SHA BAC SORTIE.json
"""

import contextlib
import importlib.util
import io
import json
import os
import shutil
import sys

ORCH, MONDES, SHA_MONDES, BAC, SORTIE = sys.argv[1:6]
sys.path.insert(0, ORCH)
from pole import pilote_mr2_v69 as P  # noqa: E402

s = importlib.util.spec_from_file_location("lanceur_v69_x9", os.path.join(ORCH, "demonstrations", "pilote_mr2_v69.py"))
L = importlib.util.module_from_spec(s)
s.loader.exec_module(L)
V4, M, MP = P.charger_mr2()


def lancer(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = L.principal(argv)
    return code, err.getvalue().strip()[-300:]


os.makedirs(BAC, exist_ok=True)
sortie = os.path.join(BAC, "a-blanc")
res = {}
code, err = lancer(["jouer", "--mode", "a_blanc", "--mondes", MONDES, "--mondes-sha256", SHA_MONDES, "--sortie", sortie])
res["jouer_a_blanc"] = {"code": code, "erreur": err}
prive = os.path.join(BAC, "prive-x9")
os.makedirs(prive, mode=0o700)
try:
    autres = []
    for r in P.MONDES_PILOTE:
        spec = V4.generer_monde_v4(V4.P1.cle("pilote-v68-essai-developpement", r))
        autres.append({"monde": r, "spec": spec, "spec_sha256": P.sha_spec(spec)})
    chemin = os.path.join(prive, "AUTRES-MONDES.json")
    sha = P.ecrire_prive(chemin, autres, [prive])
    with open(os.path.join(sortie, "manifeste-pilote-v69.json"), encoding="utf-8") as f:
        man = json.load(f)
    res["fichier_des_mondes_du_manifeste_egal_a_l_autre"] = man["controles"]["mondes"]["fichier_mondes_sha256"] == sha
    res["mondes_du_manifeste_egaux_aux_autres"] = sorted(man["controles"]["mondes"]["mondes_sha256"].values()) == sorted(
        w["spec_sha256"] for w in autres)
    code, err = lancer(["mesurer", "--sortie", sortie, "--mondes", chemin, "--mondes-sha256", sha])
    res["mesurer_avec_un_autre_fichier_des_mondes"] = {"code": code, "erreur": err}
    code, err = lancer(["lire", "--sortie", sortie])
    res["lire_ensuite"] = {"code": code, "erreur": err}
    if os.path.isfile(os.path.join(sortie, "sortie-mesure-pilote-v69.json")):
        with open(os.path.join(sortie, "sortie-mesure-pilote-v69.json"), encoding="utf-8") as f:
            corps = json.load(f)["corps"]
        res["mondes_mesures_egaux_a_ceux_du_manifeste"] = sorted(corps["mondes_sha256"]) == sorted(
            man["controles"]["mondes"]["mondes_sha256"].values())
finally:
    shutil.rmtree(prive, ignore_errors=True)
res["dossier_des_autres_mondes_supprime"] = not os.path.exists(prive)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    f.write("\n")
print(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
