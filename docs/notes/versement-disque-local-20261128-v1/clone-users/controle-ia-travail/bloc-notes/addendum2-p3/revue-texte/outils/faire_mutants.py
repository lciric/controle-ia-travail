"""Mutants de la copie du module (jamais de l'original) : un dossier par mutant, module muté + tests inchangés."""
import shutil, sys
from pathlib import Path
base = Path(sys.argv[1]); copie = base / "copie"; src = (copie / "audit_verdict_p3_v1.py").read_text(encoding="utf-8")
MUTANTS = {
    "M1-garde7-comptes": ("        for k in COMPTES_EFFET:\n            if ici[k] != _cle(lecture, cle, k):\n"
                          "                raise GardeArret(f\"garde 7 : {cle}/{k} recalculé {ici[k]!r} ≠ lecture décisive \"\n"
                          "                                 f\"{_cle(lecture, cle, k)!r}\")\n", ""),
    "M2-calcul-avale-tout": ("    except GardeArret as e:\n        return {\"etat\": ECHEC, \"motif\": str(e)}\n",
                             "    except Exception as e:\n        return {\"etat\": ECHEC, \"motif\": str(e)}\n"),
    "M3-audit-esf-non-calculable": ("    elif any(e[\"etat\"] != CALCULE for e in esf.values()):\n"
                                    "        d2 = {\"etat\": NON_CALCULE, \"motif\": \"E_sf non calculable : \" + \", \".join(\n"
                                    "            f\"{k} ({e['etat']})\" for k, e in esf.items() if e[\"etat\"] != CALCULE)}\n", ""),
}
for nom, (avant, apres) in MUTANTS.items():
    assert src.count(avant) == 1, nom
    d = base / "mutants" / nom
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    (d / "audit_verdict_p3_v1.py").write_text(src.replace(avant, apres), encoding="utf-8")
    shutil.copy(copie / "test_audit_verdict_p3_v1.py", d / "test_audit_verdict_p3_v1.py")
    print(nom, "écrit")
