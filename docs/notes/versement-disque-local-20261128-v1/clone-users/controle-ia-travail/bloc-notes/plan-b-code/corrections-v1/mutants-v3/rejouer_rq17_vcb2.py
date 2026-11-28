"""RQ-17 (graine du témoin non posée) rejoué contre `test_temoin_graine_posee_avant_chaque_appel` (l'espion), repris de
`verification-v2/mutants/rejouer_rq17_v3.py` : seul ; après les autres tests du témoin ; avant eux ; puis dans l'ordre
du fichier depuis les trois tests neufs des échéances (VCB2-01), qui changent l'état du générateur global avant les
tests du témoin (dans la rejoue complète, RQ-17 est mort d'abord sur l'égalité de deux appels de
`test_temoin_configuration_remplacee_cas_sain_et_artefact`). Le test de l'espion doit échouer chaque fois, pour la
raison écrite (l'espion), et passer chaque fois sur le code non muté. Copie `wR`, effacée après usage par l'appelant
(`rm -r`)."""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import muter_vcb2 as M  # noqa: E402

(_, module, ancien, nouveau, _, _), = [m for m in M.MUTANTS if m[0] == "RQ-17"]
w = M.ICI / "wR"
M.preparer(w)
cible = w / module
t = (M.CLONE / module).read_text(encoding="utf-8")
assert t.count(ancien) == 1
T = "tests/test_plan_b_requalifier.py::"
seul = T + "test_temoin_graine_posee_avant_chaque_appel"
autres = [T + x for x in ("test_temoin_configuration_remplacee_cas_sain_et_artefact",
                          "test_temoin_impossible_et_pannes_propagees")]
neufs = [T + x for x in ("test_echeance_avant_la_conversion_et_le_repere", "test_echeance_avant_l_ancrage",
                         "test_echeance_avant_le_rechargement_pour_le_temoin")]
for etiquette, texte in (("code non muté", t), ("RQ-17", t.replace(ancien, nouveau, 1))):
    cible.write_text(texte, encoding="utf-8")
    try:
        for nom, tests in (("seul", [seul]), ("après les autres tests du témoin", autres + [seul]),
                           ("avant les autres tests du témoin", [seul] + autres),
                           ("après les trois tests neufs des échéances, puis le témoin dans l'ordre du fichier",
                            neufs + [autres[0], seul])):
            p = M.pytest(w, tests, x=False)
            lignes = p.stdout.splitlines()
            print(f"--- {etiquette}, {nom} : {[x for x in lignes if x.strip()][-1]}")
            print("\n".join(x for x in lignes if x.startswith("E ") or x.startswith("FAILED"))[:1200])
    finally:
        shutil.copy(M.CLONE / module, cible)
        assert cible.read_bytes() == (M.CLONE / module).read_bytes()
