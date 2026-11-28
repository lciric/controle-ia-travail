"""Second passage, variables locales au point d'échec (`-l`), pour les mutants dont l'artefact neuf partage une boucle
avec des artefacts plus anciens (M09, M10, M12, M14, M19, M24) : quel artefact tue ? Copies mutées de `m/<id>/` (faites
par `lanceur_b.py`, empreinte du module muté relue dans `mutants-b-resultats.jsonl`). Deux processus au plus."""
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import lanceur_b as lb  # noqa: E402

CIBLES = ("M09", "M10", "M12", "M14", "M19", "M24")
VARIABLES = ("motif", "cle", "ecart", "nom", "ligne", "erreur", "run_add", "prereg")


def un(ident):
    m = next(x for x in lb.MUTANTS if x[0] == ident)
    d = os.path.join(ICI, "m", ident)
    attendu = next(json.loads(x)["module_mute_sha256"] for x in open(os.path.join(ICI, "mutants-b-resultats.jsonl"),
                                                                       encoding="utf-8") if json.loads(x)["id"] == ident)
    assert lb.sha(os.path.join(d, "complements_p3_v1.py")) == attendu
    code, duree, sortie = lb.pytest(d, (m[3],), os.path.join(d, "pytest-locaux.log"), extra=("-x", "-l"))
    vus = {}
    for v in VARIABLES:
        x = re.findall(rf"^{v}\s+= (.*)$", sortie, re.M)
        if x:
            vus[v] = x[-1][:160]
    return {"id": ident, "code": code, "duree_s": duree, "locaux": vus}


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as ex:
        for r in ex.map(un, CIBLES):
            print(json.dumps(r, ensure_ascii=False), flush=True)
