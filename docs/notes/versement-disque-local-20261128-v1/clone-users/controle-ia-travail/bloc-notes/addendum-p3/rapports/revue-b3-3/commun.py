"""Aides communes aux essais de la revue b3-3 (relecteur adversarial, angle « pannes »).

Importe le module final et les aides du fichier de tests sans les copier ; rien n'est écrit hors de ce dossier.
Lancer avec PYTHONPATH=/home/user/controle-ia-travail/src et PYTHONDONTWRITEBYTECODE=1."""
import sys

sys.dont_write_bytecode = True
FINAL = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/final"
ICI = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/rapports/revue-b3-3"
for d in ("/home/user/controle-ia-travail/tests", FINAL):
    if d not in sys.path:
        sys.path.insert(0, d)

import hashlib  # noqa: E402
import json  # noqa: E402

import complements_p3_v1 as cp  # noqa: E402
import test_complements_p3_v1 as tc  # noqa: E402

# mêmes tirages réduits que les tests (paramètres propres au module, jamais le code gelé)
cp.TIRAGES_AIRE = tc.TIRAGES_TESTS
cp.TIRAGES_COUT = 2000


def empreinte_sortie(s) -> str:
    return hashlib.sha256(json.dumps(s, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
