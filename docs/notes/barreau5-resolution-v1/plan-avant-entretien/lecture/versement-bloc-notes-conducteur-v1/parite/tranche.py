"""Joue `test_parite_entree_figee_sur_le_monde_nu_ouverture_recomposee_sur_le_jumeau` (fonction du fichier d'essais
commité, appelée telle quelle) sur une tranche de `liste_mondes()`, un dossier jetable par monde, effacé après le monde
(pytest garde tous les dossiers d'une session sous --basetemp : 7 269 mondes rempliraient le disque).
Usage : tranche.py K N SORTIE.jsonl (mondes d'indice i tel que i % N == K)."""
import json
import shutil
import sys
import tempfile
import time
import traceback
from pathlib import Path

R = Path("/home/user/controle-ia-travail/.claude/worktrees/agent-a89be1d2701a117b9")
sys.path[:0] = [str(R / "tests"), str(R / "src")]
import test_ouverture_suffixes_v1 as to  # noqa: E402
from controle_ia.barreau5_familles import epreuve_verite_plantee_v1 as ev  # noqa: E402

k, n, sortie = int(sys.argv[1]), int(sys.argv[2]), Path(sys.argv[3])
base = Path(sys.argv[4])
mondes = [m for i, m in enumerate(ev.liste_mondes()) if i % n == k]
with open(sortie, "a", encoding="utf-8") as f:
    for m in mondes:
        d = Path(tempfile.mkdtemp(prefix=f"{m}-", dir=base))
        t0 = time.time()
        try:
            to.test_parite_entree_figee_sur_le_monde_nu_ouverture_recomposee_sur_le_jumeau(d, m)
            etat, motif = "passe", ""
        except Exception as e:  # noqa: BLE001
            etat, motif = "echec", f"{type(e).__name__}: {e}"[:500] + " | " + traceback.format_exc()[-500:]
        finally:
            shutil.rmtree(d, ignore_errors=True)
        f.write(json.dumps({"monde": m, "etat": etat, "motif": motif, "s": round(time.time() - t0, 2)},
                           ensure_ascii=False) + "\n")
        f.flush()
print(k, len(mondes))
