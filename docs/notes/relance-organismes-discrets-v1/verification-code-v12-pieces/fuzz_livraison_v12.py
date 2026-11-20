"""Fouille : livraisons altérées au hasard (graine fixe). Tout refus d'une livraison doit être l'événement nommé,
jamais une garde ordinaire ni une autre exception (sinon l'arrêt n'est pas consigné et l'issue n'a pas de constat)."""
import collections, copy, json, sys, tempfile
from pathlib import Path
import numpy as np
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v12 as A
from controle_ia.organismes_discrets import analyse_bras_a_v12 as an, arrets_bras_a_v12 as ar
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
rng = np.random.default_rng(np.random.SeedSequence(20261119))
JUNK = [None, True, False, -1, 0, 1, 2000, 2000.0, 1.5, float("nan"), "texte", "", [], {}, [1, 2], {"a": 1}, 0.5, "dose-1.00", 10**30]
pass
base = A.sortie()
issues = collections.Counter(); exemples = {}; passes = set()
for k in range(400):
    s = copy.deepcopy(base)
    niveau = rng.integers(0, 3)
    if niveau == 0:
        cle = sorted(s)[rng.integers(0, len(s))]; s[cle] = JUNK[rng.integers(0, len(JUNK))]; ou = f"sortie.{cle}"
    elif niveau == 1:
        cle = sorted(s["reglages"])[rng.integers(0, 9)]; s["reglages"][cle] = JUNK[rng.integers(0, len(JUNK))]; ou = f"reglages.{cle}"
    else:
        d = sorted(s["lectures"])[rng.integers(0, 4)]; m = sorted(s["lectures"][d])[rng.integers(0, 5)]
        cle = sorted(s["lectures"][d][m])[rng.integers(0, 18)]; s["lectures"][d][m][cle] = JUNK[rng.integers(0, len(JUNK))]; ou = f"lecture.{cle}"
    try:
        p = A.piece(T, json.dumps(s, allow_nan=True))
    except Exception as e:
        continue
    try:
        conf = A.fichier_de_configuration(T); A.constat(T, conf)
        an.regle_de_discretion(p, conf, go_de_la_reprise=None, registre_fige=None); r = "PASSE"
    except ar.ArretDeLaLectureDeLaDiscretion:
        r = "ARRET"
    except GardeArret as e:
        r = "GARDE ORDINAIRE"; exemples.setdefault((r, ou), str(e)[:120])
    except Exception as e:
        r = f"ERREUR {type(e).__name__}"; exemples.setdefault((r, ou), str(e)[:120])
    issues[r] += 1
    if r == "PASSE": passes.add(ou + ("" if niveau < 2 else f"@{d}")) 
print(dict(issues)); print("PASSE sur :", sorted(passes))
for (r, ou), m in exemples.items():
    print(r, "|", ou, "|", m)
