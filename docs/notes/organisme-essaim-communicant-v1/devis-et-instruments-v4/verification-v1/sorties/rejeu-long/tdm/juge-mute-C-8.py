#!/usr/bin/env python3
"""Juge du test de mort par programme, en processus isolé — v2 (contre-lecture de la v3 : l'évaluateur de la grammaire,
`monde_riche_outils_v1.py`, est vérifié à son empreinte écrite ici AVANT son import ; sinon sortie 6, aucun verdict).
Texte de la v1 : Lancé par `test_de_mort_programme_v2.py` (qui vérifie
d'abord l'empreinte de ce fichier), il ne reçoit que deux fichiers : les cartes (lois proposées) et les tranches tenues à
l'écart (épisodes z, g, y tirés par le fournisseur), plus l'empreinte attendue des tranches. Il ne voit ni la loi plantée, ni le
devis du monde, ni l'archive, ni l'oracle : ils n'existent pas dans ce processus, qui démarre vide (`python -I`).

Règle (celle de `monde_riche_outils_v1.test_de_mort`, recopiée par la v1 du test de mort par programme) : s = moyenne sur les
épisodes de la tranche de [log p_carte(y | z, g) − log m̂(y)], m̂ = marginale empirique de la tranche (comptes + 0,5),
plancher 1e-12 ; « survit » si s ≥ 0,02, « éliminée » sinon ; « refus » si la loi n'est pas évaluable ou non finie.

Garde interne (crochet d'audit posé après les imports) : toute ouverture de fichier autre que les deux entrées et le code
(bibliothèque de Python, numpy, `outils-v1`) est refusée ; tout import d'un module du monde, tout sous-processus, tout appel
système d'exécution et toute connexion réseau aussi. Une violation ⇒ aucun verdict, sortie 3. Une carte qui a la forme d'un
devis de monde (clés `effets` ou `distracteurs`, à tout niveau) ⇒ sortie 4. Empreinte des tranches fausse ⇒ sortie 5.

Usage : python -I -B juge_test_de_mort_isole_v1.py CARTES.json TRANCHES.json SHA256_TRANCHES
Sortie : JSON sur la sortie standard {"verdicts": {carte: {tranche: {"verdict", "statistique", "n"}}}}.
"""
import hashlib
import json
import os
import sys

ICI = '/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4'  # juge muté écrit hors de son dossier : il importe la racine depuis le dossier du juge
sys.path.insert(0, ICI)
import racine_depot_v1 as R  # noqa: E402

OUTILS = R.chemin("docs/notes/organisme-multi-generations-v1/outils-v1")
EVALUATEUR_SHA256 = "1825b956eed638fe4daf3d7395a169fdbdf7c9679076d9ba3fb4a15cfd7ec85e"  # monde_riche_outils_v1.py, écrite à la main
_ev = hashlib.sha256(open(os.path.join(OUTILS, "monde_riche_outils_v1.py"), "rb").read()).hexdigest()
if _ev != EVALUATEUR_SHA256:
    print(json.dumps({"refus": "évaluateur d'empreinte différente", "empreinte": _ev}))
    sys.exit(6)
sys.path.insert(0, OUTILS)
import numpy as np  # noqa: E402
import monde_riche_outils_v1 as MO  # noqa: E402  (évaluateur de la grammaire : seule fonction utilisée, `probas`)

SEUIL = 0.02
MODULES_INTERDITS = {"monde_riche_v4", "generateur_mondes_v1", "generateur_mondes_v2", "verifier_monde_v2", "verifier_monde_kimi_v1",
                     "puissance_monde_riche_v1", "puissance_monde_riche_v2", "puissance_monde_riche_v3", "bases_sans_modele_v1",
                     "base_gloutonne_renforcee_v1", "test_de_mort_programme_v1", "test_de_mort_programme_v2", "test_de_mort_programme_v3", "subprocess", "socket"}
EVENEMENTS_INTERDITS = ("subprocess.Popen", "os.system", "os.exec", "os.posix_spawn", "os.spawn", "socket.connect", "socket.getaddrinfo",
                        "urllib.Request", "ctypes.dlopen")
VIOLATIONS = []


def _dossiers_de_code():
    d = {os.path.realpath(OUTILS), os.path.realpath(os.path.dirname(np.__file__))}
    for p in (sys.prefix, sys.base_prefix, sys.exec_prefix):
        d.add(os.path.realpath(p))
    return tuple(sorted(d))


def poser_garde(permis):
    code = _dossiers_de_code()
    permis = {os.path.realpath(p) for p in permis}

    def crochet(ev, args):
        if ev == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
            p = os.path.realpath(os.fsdecode(args[0]))
            if p in permis:
                return
            if p.startswith(tuple(d + os.sep for d in code)) and p.endswith((".py", ".pyc", ".so")):
                return
            VIOLATIONS.append(f"ouverture refusée : {p}")
            raise PermissionError(f"garde du juge : ouverture refusée ({p})")
        if ev == "import" and args and set(str(args[0]).split(".")) & MODULES_INTERDITS:
            VIOLATIONS.append(f"import refusé : {args[0]}")
            raise ImportError(f"garde du juge : import refusé ({args[0]})")
        if ev.startswith(EVENEMENTS_INTERDITS):
            VIOLATIONS.append(f"évènement refusé : {ev}")
            raise PermissionError(f"garde du juge : {ev} refusé")

    sys.addaudithook(crochet)


def forme_de_devis(x):
    if isinstance(x, dict):
        return bool({"effets", "distracteurs"} & set(x)) or any(forme_de_devis(v) for v in x.values())
    if isinstance(x, list):
        return any(forme_de_devis(v) for v in x)
    return False


def statistique(loi, Z, G, Y):
    try:
        P = MO.probas(loi, Z, G)
        if not np.all(np.isfinite(P)):
            return {"verdict": "refus", "motif": "loi non finie"}
    except (PermissionError, ImportError):
        raise
    except Exception as ex:  # noqa: BLE001
        return {"verdict": "refus", "motif": f"loi non évaluable : {type(ex).__name__}"}
    n, K = len(Y), P.shape[1]
    c = np.bincount(Y, minlength=K) + 0.5
    marg = c / c.sum()
    s = float(np.mean(np.log(np.maximum(P[np.arange(n), Y], MO.PLANCHER)) - np.log(marg[Y])))
    return {"verdict": "survit" if s >= SEUIL else "éliminée", "statistique": s, "n": n}


def main(argv):
    if len(argv) != 4:
        print(json.dumps({"refus": "arguments : CARTES.json TRANCHES.json SHA256 (rien de plus)"}))
        return 2
    cartes_ch, tranches_ch, sha_attendu = argv[1], argv[2], argv[3]
    poser_garde({cartes_ch, tranches_ch})
    try:
        # POINT-DE-MUTATION (épreuves de la garde interne)
        import os as _o
        _o.system('cat /home/user/controle-ia-travail/docs/notes/organisme-multi-generations-v1/sorties-v4/partie-v4-monde-8.json > /dev/null')
        octets = open(tranches_ch, "rb").read()
        if hashlib.sha256(octets).hexdigest() != sha_attendu:
            print(json.dumps({"refus": "empreinte des tranches"}))
            return 5
        tranches = json.loads(octets.decode("utf-8"))["tranches"]
        cartes = json.loads(open(cartes_ch, "rb").read().decode("utf-8"))
        if forme_de_devis(cartes):
            print(json.dumps({"refus": "carte en forme de devis de monde"}))
            return 4
        out = {}
        for c in cartes:
            out[c["nom"]] = {}
            for nom, t in tranches.items():
                Z, G, Y = np.asarray(t["Z"], float), np.asarray(t["G"], int), np.asarray(t["Y"], int)
                out[c["nom"]][nom] = statistique(c["loi"], Z, G, Y)
    except (PermissionError, ImportError) as ex:
        VIOLATIONS.append(f"{type(ex).__name__}")
    if VIOLATIONS:
        print(json.dumps({"refus": "lecture interdite", "violations": VIOLATIONS[:5]}, ensure_ascii=False))
        return 3
    print(json.dumps({"verdicts": out}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
