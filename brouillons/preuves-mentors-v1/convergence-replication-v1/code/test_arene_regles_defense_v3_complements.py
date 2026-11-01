"""Essais complémentaires du code v3 demandés par la contre-lecture 1 du préenregistrement de réplication (CL-06).

Ce fichier n'en remplace aucun (R12) : il s'ajoute à `test_arene_regles_defense_v3.py` (empreinte
d1afa9db925af7265c8aad1b238288229fb5b6f2977803a43411e27c4b96c849), dont il réemploie les aides, et porte sur
`arene_regles_defense_v3.py` (empreinte 3519123b7297df93ea07ec3ef72ca1f84947e2d8c9950094acaeddf8288d24d9 ; les deux
empreintes sont vérifiées par le premier essai : un code ou un fichier d'essais changé fait échouer ce fichier).

Ce que chaque essai ajoute à ceux du fichier principal (numérotation du brouillon 2 du préenregistrement, § Plan 2) :
- E5 étendu : inventaire de TOUS les nœuds de niveau module de v2 et v3 par type (fonctions, affectations, affectations
  annotées, boucles, conditions, assertions, imports, docstring), chacun retrouvé à l'identique (arbre et texte) sauf la
  liste fermée C1 à C12 ; diff unifié imprimé pour chaque entrée de la liste (lu par le contre-lecteur dans le journal,
  option `-rP` de pytest) ; preuve mécanique pour C10 : `finale_regle` et `executer_tache_regles` de v3, une fois
  retirés le paramètre de sortie, les blocs `if` qui en dépendent et le mot-clé transmis, ont l'arbre de v2 ;
- E6 (lent, chemin de production, budget 1,6 compris) : v3 rejoue les tâches (δ 1,6 ; instance 0), (δ 1,4 ;
  instance 0) et (δ 1,4 ; instance 1) de la course originale sur leurs racines d'origine, sérialisation active ;
  égalité au bit avec `resultats-regles-defense.json` ; si elle échoue, repli écrit d'avance : v2 inchangé rejoue la
  même tâche sur cette machine (copie miroir temporaire, processus neuf) ; v3 = v2 ici → différence de plate-forme
  consignée avec sa taille ; v3 ≠ v2 → échec ;
- E6 repli (rapide) : le repli lui-même, cas sain et artefacts (R5), et v3 = v2 au bit sur une tâche réduite du
  budget 1,6 avec les racines d'essai du gel v2 ;
- E8 : la statistique de A (`analyser_regles`) contre la spécification indépendamment du fichier d'analyse : les
  indices du générateur (§ 5.5), le tableau de contrôle (§ 12, 10 lignes × 6 nombres), les 16 libellés × 2 budgets,
  les classes des Tables B et C (§ 12) recalculées ici ; analyse sur une racine de plus de 2⁶³ ;
- E9 : la garde de l'étape C8 dans de VRAIS processus de travail neufs (pool `spawn`) : racine de tâche décalée d'une
  unité, racine tenue décalée d'une unité, racines originales → arrêt, aucune tâche, aucun processus orphelin ;
- E10 : bout en bout `main decision` sur une configuration réduite (2 instances, T = 2), texte temporaire scellé dont
  les deux racines dérivées dépassent 2⁶³, dépôt git temporaire propre, deux processus `spawn` : manifeste, PID,
  résultats et analyse écrits et scellés ; racines relues exactement (entiers et chaînes) ; analyse = recalcul au bit.

Racines : celles des essais du gel v2 (20266511, 20266512) ; seuls E6 et E8 posent eux-mêmes l'autorisation des
racines de la course originale (20266201, 20266202), sur des résultats déjà scellés et lus ; E9 et E10 tirent sur des
racines dérivées de textes SYNTHÉTIQUES scellés dans le dossier temporaire de pytest (jamais le texte de réplication ni
un de ses brouillons). Aucun fichier écrit hors du dossier temporaire de pytest.

Lancement :
    cd <dossier de ce fichier> && PYTHONPATH=<dépôt>/src OMP_NUM_THREADS=1 REGLES_ESSAIS_LENTS=1 \
        <dépôt>/.venv/bin/python -B -m pytest -q -rP -p no:cacheprovider test_arene_regles_defense_v3_complements.py
"""
from __future__ import annotations

import ast
import copy
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import Counter
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
if str(ICI) not in sys.path:
    sys.path.insert(0, str(ICI))

import arene_regles_defense_v3 as m  # noqa: E402
import test_arene_regles_defense_v3 as base  # noqa: E402
from test_arene_regles_defense_v3 import sans_autorisation  # noqa: E402,F401  (fixture réemployée)

from controle_ia import manifeste as man  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.scellement import sceller, verifier  # noqa: E402

v4 = m.v4
DEPOT = m.DEPOT
CODE_V3_SHA256 = "3519123b7297df93ea07ec3ef72ca1f84947e2d8c9950094acaeddf8288d24d9"
ESSAIS_V3_SHA256 = "d1afa9db925af7265c8aad1b238288229fb5b6f2977803a43411e27c4b96c849"
R, RT = m.RACINE_TESTS, m.RACINE_TESTS_TENUE
DEUX_63 = 2 ** 63


def test_pieces_epinglees():
    """Le code et le fichier d'essais principal sont ceux que ce fichier complète ; la référence v2 est intacte."""
    assert m.empreinte_fichier(m.__file__) == CODE_V3_SHA256
    assert m.empreinte_fichier(base.__file__) == ESSAIS_V3_SHA256
    assert m.empreinte_fichier(m.CODE_V2) == m.CODE_V2_SHA256
    assert m.empreinte_fichier(m.ARENE_V4) == m.ARENE_V4_SHA256 and m.empreinte_fichier(m.GEL) == m.GEL_SHA256


# ---------------------------------------------------------------------------------------------------------------
# E5 étendu : tous les nœuds de niveau module, diffs imprimés, preuve mécanique pour C10
# ---------------------------------------------------------------------------------------------------------------
INVENTAIRE_V2 = {"Expr": 1, "Import": 11, "ImportFrom": 5, "For": 2, "If": 2, "Assert": 2, "Assign": 33,
                 "AnnAssign": 2, "FunctionDef": 37}
AJOUTS_V3 = {("assign", n) for n in ("DOSSIER_V2", "CODE_V2", "CODE_V2_SHA256", "REGLE_D", "RACINES_INTERDITES_REGLE_D",
                                      "PLAGE_INTERDITE_REGLE_D", "VECTEURS_ESSAI_REGLE_D", "_RACINES_VECTEURS_ESSAI")} | \
            {("def", n) for n in ("etat_regle_D", "exiger_racines_regle_D", "deriver_racines_regle_D",
                                   "serialiser_moniteur", "serialiser_variante")}
INVENTAIRE_V3 = {**INVENTAIRE_V2, "Assign": 33 + 8, "FunctionDef": 37 + 5}
PARAMETRES_SORTIE = frozenset({"rendre_attaques", "serialiser"})     # C10 : options de sortie seulement


def _corps(chemin: Path) -> list[ast.stmt]:
    return ast.parse(chemin.read_text(encoding="utf-8")).body


class RetirerSortieC10(ast.NodeTransformer):
    """Retire d'une fonction ce que C10 ajoute : docstring, annotation de retour, paramètres de sortie et leurs
    valeurs par défaut, blocs `if <paramètre de sortie>:`, mots-clés `<paramètre de sortie>=…`, et le retour
    conditionnel `(…) if <paramètre de sortie> else x` remplacé par `x`."""

    def visit_FunctionDef(self, n):
        self.generic_visit(n)
        if n.body and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant) and \
                isinstance(n.body[0].value.value, str):
            n.body = n.body[1:]
        n.returns = None
        a = n.args
        k = len(a.args) - len(a.defaults)
        gardes = [(x, a.defaults[i - k] if i >= k else None) for i, x in enumerate(a.args)
                  if x.arg not in PARAMETRES_SORTIE]
        a.args = [x for x, _ in gardes]
        a.defaults = [d for _, d in gardes if d is not None]
        return n

    def visit_If(self, n):
        if isinstance(n.test, ast.Name) and n.test.id in PARAMETRES_SORTIE:
            return None
        return self.generic_visit(n)

    def visit_keyword(self, n):
        return None if n.arg in PARAMETRES_SORTIE else self.generic_visit(n)

    def visit_Return(self, n):
        self.generic_visit(n)
        if isinstance(n.value, ast.IfExp) and isinstance(n.value.test, ast.Name) and \
                n.value.test.id in PARAMETRES_SORTIE:
            n.value = n.value.orelse
        return n


def _fonction(corps: list[ast.stmt], nom: str) -> ast.FunctionDef:
    (f,) = [x for x in corps if isinstance(x, ast.FunctionDef) and x.name == nom]
    return copy.deepcopy(f)


def test_E5_etendu_inventaire_de_tous_les_noeuds_diffs_imprimes_et_C10_mecanique():
    v2, v3 = m.CODE_V2, Path(m.__file__)
    c2, c3 = _corps(v2), _corps(v3)
    inv2, inv3 = Counter(type(x).__name__ for x in c2), Counter(type(x).__name__ for x in c3)
    print(f"inventaire v2 ({len(c2)} nœuds) : {dict(sorted(inv2.items()))}")
    print(f"inventaire v3 ({len(c3)} nœuds) : {dict(sorted(inv3.items()))}")
    assert dict(inv2) == INVENTAIRE_V2 and dict(inv3) == INVENTAIRE_V3
    # chaque nœud de v2, quel que soit son type, est retrouvé à l'identique (arbre ET texte source) dans v3, sauf la
    # liste fermée ; v3 n'ajoute que les nœuds nommés ; l'ordre relatif des nœuds de v2 est gardé
    assert base.ecarts_diff_restreint(v3) == base.SANS_ECART
    a2, o2, t2 = base._carte(v2)
    a3, o3, t3 = base._carte(v3)
    assert set(a3) - set(a2) == AJOUTS_V3 and AJOUTS_V3 <= set(base.CHANGEMENTS_C1_C12)
    assert set(a2) <= set(a3)
    par_type = Counter()
    for noeud, cle in zip(c2, o2):
        if cle not in base.CHANGEMENTS_C1_C12:
            assert a2[cle] == a3[cle] and t2[cle] == t3[cle], cle
            par_type[type(noeud).__name__] += 1
    print(f"nœuds de v2 retrouvés à l'identique dans v3, par type : {dict(sorted(par_type.items()))} "
          f"(total {sum(par_type.values())} sur {len(c2)})")
    assert sum(par_type.values()) == len(c2) - len([k for k in o2 if k in base.CHANGEMENTS_C1_C12])
    imports2 = [ast.dump(x) for x in c2 if isinstance(x, (ast.Import, ast.ImportFrom))]
    imports3 = [ast.dump(x) for x in c3 if isinstance(x, (ast.Import, ast.ImportFrom))]
    assert imports2 == imports3 and len(imports2) == 16
    # diffs imprimés de chaque entrée de la liste fermée (le contre-lecteur les lit dans le journal)
    lignes_changees = {}
    for cle, motif in base.CHANGEMENTS_C1_C12.items():
        avant = (t2.get(cle) or "").splitlines()
        apres = (t3.get(cle) or "").splitlines()
        d = list(difflib.unified_diff(avant, apres, f"v2 {cle}", f"v3 {cle}", n=1, lineterm=""))
        lignes_changees[cle] = sum(1 for x in d if x[:1] in "+-" and x[:3] not in ("+++", "---"))
        print(f"\n===== {motif} — {cle} : {lignes_changees[cle]} lignes changées =====")
        print("\n".join(d) if d else "(aucune différence)")
    assert all(n > 0 for n in lignes_changees.values())
    # C10, preuve mécanique : retirer l'option de sortie de v3 rend l'arbre de v2
    for nom in ("finale_regle", "executer_tache_regles"):
        f2 = RetirerSortieC10().visit(_fonction(c2, nom))
        f3 = RetirerSortieC10().visit(_fonction(c3, nom))
        assert ast.dump(f2, include_attributes=False) == ast.dump(f3, include_attributes=False), nom
        assert ast.dump(_fonction(c2, nom)) != ast.dump(_fonction(c3, nom))        # le changement existe
    # artefact (R5) : une ligne de calcul ajoutée sous l'option de sortie hors d'un bloc `if` est vue
    source = v3.read_text(encoding="utf-8")
    ancien = '    res["exploitabilite_finale"] = exploitabilite(res["V_iii_final"])\n'
    assert source.count(ancien) == 1
    altere = ast.parse(source.replace(ancien, ancien.replace('res["V_iii_final"]', 'res["V_iii_standard"]'))).body
    assert ast.dump(RetirerSortieC10().visit(_fonction(altere, "finale_regle")), include_attributes=False) != \
        ast.dump(RetirerSortieC10().visit(_fonction(c2, "finale_regle")), include_attributes=False)


# ---------------------------------------------------------------------------------------------------------------
# E6 : chemin de production, budget 1,6, et repli de plate-forme écrit d'avance
# ---------------------------------------------------------------------------------------------------------------
CODE_REJEU_V2 = r"""
import json, sys
sys.path.insert(0, sys.argv[1])
import arene_regles_defense_v2 as v2
a = json.loads(open(sys.argv[2], encoding="utf-8").read())
if a["autorisation"] is not None:
    v2._AUTORISATION_DECISION["prereg_sha256"] = a["autorisation"]
cfg = v2.v4.Config(**{k: tuple(v) if isinstance(v, list) else v for k, v in a["cfg"].items()})
r = v2.executer_tache_regles(a["instance"], a["cd"], a["racine"], a["racine_tenue"], cfg, tuple(a["regles"]),
                             tuple(a["lambdas"]), tuple(a["references"]), False)
open(sys.argv[3], "w", encoding="utf-8").write(json.dumps(r))
print("v2", v2.VERSION, v2.empreinte_fichier(v2.__file__))
"""


def miroir_v2(dossier: Path) -> Path:
    """Copie miroir minimale où le code v2 INCHANGÉ (octet pour octet) se charge : v2 lit l'arène sous
    `<dépôt>/donnees/argon-seul-convergence-v1/` (dossier ignoré par git, absent ici) et le gel à côté de lui ; on y
    copie la copie suivie de l'arène (même empreinte) et le gel. Renvoie le dossier du code v2 dans le miroir."""
    d = dossier / "docs" / "notes" / "convergence-defense-v1" / "regles-defense-v1"
    d.mkdir(parents=True)
    shutil.copyfile(m.CODE_V2, d / m.CODE_V2.name)
    shutil.copyfile(m.GEL, d / m.GEL.name)
    a = dossier / "donnees" / "argon-seul-convergence-v1"
    a.mkdir(parents=True)
    shutil.copyfile(m.ARENE_V4, a / "arene_melange_v4.py")
    assert m.empreinte_fichier(d / m.CODE_V2.name) == m.CODE_V2_SHA256
    assert m.empreinte_fichier(a / "arene_melange_v4.py") == m.ARENE_V4_SHA256
    return d


def rejouer_v2(dossier: Path, instance: int, cd: int, racines: tuple, cfg, autorisation=None) -> dict:
    """Une tâche rejouée par v2 inchangé, dans un processus neuf (aucun état partagé avec v3)."""
    code_v2 = miroir_v2(dossier / "miroir")
    entree, sortie = dossier / "entree-v2.json", dossier / "sortie-v2.json"
    entree.write_text(json.dumps({"instance": instance, "cd": cd, "racine": racines[0], "racine_tenue": racines[1],
                                  "cfg": asdict(cfg), "regles": list(m.REGLES), "lambdas": [0.3],
                                  "references": ["moyenne"], "autorisation": autorisation}), encoding="utf-8")
    env = {**os.environ, "PYTHONPATH": str(DEPOT / "src"), "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
           "MKL_NUM_THREADS": "1"}
    r = subprocess.run([sys.executable, "-B", "-c", CODE_REJEU_V2, str(code_v2), str(entree), str(sortie)],
                       capture_output=True, text=True, env=env, cwd=dossier)
    assert r.returncode == 0, r.stderr[-3000:]
    assert f"v2 arene_regles_defense_v2 {m.CODE_V2_SHA256}" in r.stdout
    return json.loads(sortie.read_text(encoding="utf-8"))


def ecart_numerique_max(x, y) -> float:
    """Plus grand écart absolu entre feuilles numériques alignées (structures supposées de même forme)."""
    if isinstance(x, dict):
        return max([ecart_numerique_max(x[k], y[k]) for k in x if k in y] or [0.0])
    if isinstance(x, list):
        return max([ecart_numerique_max(a, b) for a, b in zip(x, y)] or [0.0])
    if isinstance(x, (int, float)) and not isinstance(x, bool) and isinstance(y, (int, float)):
        return abs(float(x) - float(y)) if x == x and y == y else 0.0
    return 0.0


def comparer_E6(calc: dict, ref: dict, rejouer) -> dict:
    """Règle écrite d'avance (brouillon 2, § Plan 2, E6) : v3 = fichier original au bit → « égal au fichier » ;
    sinon v2 inchangé rejoue la tâche ici : v3 = v2 au bit → « différence de plate-forme » (écart au fichier consigné) ;
    v3 ≠ v2 → échec (arrêt). `rejouer` n'est appelé que si nécessaire."""
    v3 = base.au_bit(base.sans_temps(calc, base.CHAMPS_V3))
    if v3 == base.au_bit(base.sans_temps(ref)):
        return {"issue": "égal au fichier original"}
    v2 = rejouer()
    if v3 != base.au_bit(base.sans_temps(v2)):
        raise AssertionError("E6 : v3 ≠ v2 sur cette machine : arrêt (pas une différence de plate-forme)")
    return {"issue": "différence de plate-forme (v3 = v2 ici)",
            "ecart_max_au_fichier": ecart_numerique_max(base.sans_temps(calc, base.CHAMPS_V3), base.sans_temps(ref))}


def test_E6_repli_de_plate_forme_sain_et_artefacts_et_v3_egal_v2_budget_1_6(tmp_path):
    """Rapide : v3 et v2 inchangé (processus neuf, copie miroir) rendent au bit la même tâche réduite (δ 1,6 ;
    instance 1 ; racines d'essai du gel v2), v3 sérialisation active ; puis la règle de repli sur cas sain et artefacts."""
    cfg = base.CFG_PETITE
    calc = json.loads(json.dumps(m.executer_tache_regles(1, 2, R, RT, cfg, m.REGLES, (0.3,), ("moyenne",),
                                                         False, serialiser=True)))
    v2 = rejouer_v2(tmp_path, 1, 2, (R, RT), cfg)
    assert v2["version"] == "arene_regles_defense_v2" and calc["version"] == "arene_regles_defense_v3"
    assert base.au_bit(base.sans_temps(calc, base.CHAMPS_V3)) == base.au_bit(base.sans_temps(v2))
    appels = []

    def rejouer(x):
        return lambda: appels.append(1) or x

    # sain : égal au « fichier » → v2 n'est pas rejoué
    assert comparer_E6(calc, v2, rejouer(v2)) == {"issue": "égal au fichier original"} and not appels
    # artefact 1 : le « fichier » diffère de 1e-12 sur un champ, v2 rejoué ici = v3 → plate-forme, écart consigné
    fichier = copy.deepcopy(v2)
    fichier["regles"]["R3"]["V_iii_final"] += 1e-12
    issue = comparer_E6(calc, fichier, rejouer(v2))
    assert issue["issue"].startswith("différence de plate-forme") and 0 < issue["ecart_max_au_fichier"] < 1e-11
    assert len(appels) == 1
    # artefact 2 : v2 rejoué ici ≠ v3 → échec, sans repli silencieux
    v2_faux = copy.deepcopy(v2)
    v2_faux["regles"]["R0"]["ii_final"] += 1e-12
    with pytest.raises(AssertionError, match="v3 ≠ v2"):
        comparer_E6(calc, fichier, rejouer(v2_faux))


@base.LENT
@pytest.mark.parametrize("cd, instance", [(2, 0), (1, 0), (1, 1)])
def test_lent_E6_chemin_de_production_trois_taches_de_la_course_originale_avec_repli(tmp_path, sans_autorisation,
                                                                                     cd, instance):
    """v3 rejoue (δ 1,6 ; instance 0), (δ 1,4 ; instance 0) et (δ 1,4 ; instance 1) de la course originale sur leurs
    racines d'origine, sérialisation active (chemin de production), autorisation posée par l'essai ; égalité au bit
    (champs du préenregistrement puis toute la tâche) ; repli de plate-forme écrit d'avance (`comparer_E6`) pour les
    trois tâches (les deux tâches du budget 1,4 sont aussi rejouées, sans repli, par le fichier principal)."""
    originaux = base._resultats_originaux()
    ref = next(x for x in originaux if x["code_delta"] == cd and x["instance"] == instance)
    assert (ref["racine"], ref["racine_tenue"]) == base.RACINES_ORIGINALES and ref["delta"] == (1.4, 1.6)[cd - 1]
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "prereg_sha256", base.PREREG_ORIGINAL_SHA256)
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "racines", base.RACINES_ORIGINALES)
    t0 = time.process_time()
    calc = json.loads(json.dumps(m.executer_tache_regles(instance, cd, *base.RACINES_ORIGINALES, v4.CONFIG_V4,
                                                         m.REGLES, (0.3,), ("moyenne",), False, serialiser=True)))
    nom_tache = f"δ {(1.4, 1.6)[cd - 1]} ; instance {instance}"
    print(f"E6 ({nom_tache}) : {time.process_time() - t0:.1f} s de processeur")
    issue = comparer_E6(calc, ref, lambda: rejouer_v2(tmp_path, instance, cd, base.RACINES_ORIGINALES, v4.CONFIG_V4,
                                                      autorisation=base.PREREG_ORIGINAL_SHA256))
    print(f"E6 ({nom_tache}) : {issue}")
    if issue["issue"] == "égal au fichier original":
        for nom, x in ref["regles"].items():
            y = calc["regles"][nom]
            for champ in base.CHAMPS_E6:
                assert y[champ] == x[champ], (nom, champ)
            assert y["par_tour"]["iii"] == x["par_tour"]["iii"] and y["par_tour"]["ii"] == x["par_tour"]["ii"]
            assert [d["poids"] for d in y["serialisation"]["defense_finale"]] == x["poids_finaux"]
    assert set(calc) - set(ref) == {"loi_cible"} and all("serialisation" in x for x in calc["regles"].values())


# ---------------------------------------------------------------------------------------------------------------
# E8 : la statistique de A contre la spécification (indépendamment du fichier d'analyse)
# ---------------------------------------------------------------------------------------------------------------
# spécification statistique § 5.5 et § 12, recopiées ici depuis le texte (pas depuis le code ni l'analyse)
INDICES_SPEC = {(1, 203): ([80, 79, 39, 86, 45, 87, 54, 22, 58, 80], [56, 63, 4, 66, 85]),
                (2, 200): ([73, 34, 66, 88, 64, 92, 23, 55, 84, 31], [10, 38, 20, 60, 51])}
TABLEAU_12 = {   # (budget, libellé) : moyenne, écart-type, q0.003125, q0.00625, q0.99375, q0.996875
    (1, "R3 - R2 (V_iii_final)"): (0.10448042252007811, 0.05656582805294246, 0.08961294692052145, 0.09061967064630756, 0.11847919936691555, 0.1195334438923409),
    (1, "R0 - R2 (V_iii_final)"): (0.002372737273727372, 0.0437743214432734, -0.009994891676667669, -0.00881441894189419, 0.013423389213921407, 0.014486709608460841),
    (1, "R4[moyenne,λ=0.3] - R2 (V_iii_final)"): (0.0201960196019602, 0.04239267589358395, 0.010168702807780781, 0.010856548154815484, 0.031763698244824494, 0.033126912691269106),
    (1, "R0 - R2 (ii_final)"): (0.05159014753688421, 0.06098120554786593, 0.03629339475493873, 0.03746680951487873, 0.06743716460365097, 0.06881969804951228),
    (1, "R1 - R2 (exploitabilite_moyenne_tours)"): (0.026169991999199924, 0.023547075573731077, 0.020106790171204626, 0.020531546123362335, 0.032298407184468476, 0.03288676562968797),
    (2, "R3 - R2 (V_iii_final)"): (0.12355560350045353, 0.042688591197885796, 0.11167459572805016, 0.1127024328599859, 0.13408309749193276, 0.13491261731301288),
    (2, "R0 - R2 (V_iii_final)"): (0.003718371837183717, 0.0383691164326799, -0.00656942100460046, -0.005623565481548155, 0.013332498874887548, 0.014550762888788865),
    (2, "R4[moyenne,λ=0.3] - R2 (V_iii_final)"): (0.014203420342034203, 0.03305933727569008, 0.006422642264226423, 0.006941184743474348, 0.0231068294329433, 0.023962247787278703),
    (2, "R0 - R2 (ii_final)"): (0.059960640160040005, 0.06029064838824576, 0.043867641754188544, 0.045420316329082264, 0.07563060796449118, 0.0770858519317329),
    (2, "R1 - R2 (exploitabilite_moyenne_tours)"): (0.016226997699769964, 0.018280298925448104, 0.011546889454570441, 0.011899875534428422, 0.020956909753475347, 0.021426363339458934),
}
M_MARGE, S5 = 0.02, 0.02


def classe_table_B(c: dict) -> str:
    q = c["quantiles"]
    b8, e8 = (q["q0.003125"], q["q0.996875"]), (q["q0.00625"], q["q0.99375"])
    if b8[0] > M_MARGE:
        return "k > R2"
    if b8[1] < -M_MARGE:
        return "R2 > k"
    if e8[0] > -M_MARGE and e8[1] < M_MARGE:
        return "≈"
    if b8[0] > 0:
        return "k ≳ R2"
    if b8[1] < 0:
        return "R2 ≳ k"
    return "?"


def ligne_table_C(c: dict) -> int:
    bas, haut = c["quantiles"]["q0.003125"], c["quantiles"]["q0.996875"]
    for ligne, cond in ((1, haut < -S5), (2, haut < 0 and bas > -S5), (3, haut < 0), (4, bas > 0), (5, bas > -S5)):
        if cond:
            return ligne
    return 6


def test_E8_statistique_de_A_contre_la_specification(sans_autorisation):
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "prereg_sha256", base.PREREG_ORIGINAL_SHA256)
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "racines", base.RACINES_ORIGINALES)
    # générateur du rééchantillonnage de A (`gen_regles`, rôle 99) = vecteurs de la spécification § 5.5
    for (cd, code), (debut, fin) in INDICES_SPEC.items():
        I = m.gen_regles(20266201, cd, code, 0, 0, v4.ROLE_REECH).integers(0, 100, size=(20000, 100))
        assert v4.ROLE_REECH == 99 and I.dtype == np.int64 and I.shape == (20000, 100)
        assert I[0, :10].tolist() == debut and I[-1, -5:].tolist() == fin
    an = m.analyser_regles(base._resultats_originaux(), 20266201)
    noms = ["R0", "R1", "R3", "R4[moyenne,λ=0.3]"]
    mesures = ["V_iii_final", "ii_final", "exploitabilite_finale", "exploitabilite_moyenne_tours"]
    for cd in ("1", "2"):
        libelles = {k for k in an[cd]["contrastes_contre_R2"] if "standard seul" not in k}
        assert libelles == {f"{k} - R2 ({x})" for k in noms for x in mesures} and len(libelles) == 16
        for lib in libelles:
            c = an[cd]["contrastes_contre_R2"][lib]
            assert c["n"] == 100 and len(c["quantiles"]) == 10
    for (cd, lib), attendu in TABLEAU_12.items():
        c = an[str(cd)]["contrastes_contre_R2"][lib]
        q = c["quantiles"]
        assert (c["moyenne"], c["ecart_type"], q["q0.003125"], q["q0.00625"], q["q0.99375"], q["q0.996875"]) == \
            attendu, (cd, lib)
    # classes du § 12 recalculées ici à partir des nombres de A (Table B sur V, Table C sur (ii))
    attendu_B = {"R0": ("≈", "≈"), "R1": ("R2 ≳ k", "?"), "R3": ("k > R2", "k > R2"),
                 "R4[moyenne,λ=0.3]": ("k ≳ R2", "k ≳ R2")}
    attendu_C = {"R0": (4, 4), "R1": (4, 4), "R3": (1, 1), "R4[moyenne,λ=0.3]": (4, 4)}
    for k in noms:
        assert tuple(classe_table_B(an[cd]["contrastes_contre_R2"][f"{k} - R2 (V_iii_final)"])
                     for cd in ("1", "2")) == attendu_B[k], k
        assert tuple(ligne_table_C(an[cd]["contrastes_contre_R2"][f"{k} - R2 (ii_final)"])
                     for cd in ("1", "2")) == attendu_C[k], k
    # une racine de plus de 2⁶³ (comme celles de la règle D) passe exactement jusqu'au générateur
    grande = 2 ** 64 - 59
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "racines", (grande, grande - 1))
    I = m.gen_regles(grande, 1, 203, 0, 0, 99).integers(0, 100, size=(3, 100))
    J = np.random.default_rng(np.random.SeedSequence(entropy=grande, spawn_key=(1, 203, 0, 0, 99))).integers(
        0, 100, size=(3, 100))
    assert np.array_equal(I, J)
    an_g = m.analyser_regles([r for r in base._resultats_originaux() if r["code_delta"] == 1], grande, n_reech=500)
    c_g = an_g["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]
    c_o = an["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]
    assert c_g["moyenne"] == c_o["moyenne"] and c_g["ecart_type"] == c_o["ecart_type"]
    assert c_g["quantiles"] != c_o["quantiles"]


# ---------------------------------------------------------------------------------------------------------------
# E9 : la garde de C8 dans de vrais processus de travail neufs
# ---------------------------------------------------------------------------------------------------------------
CFG_E10 = m.replace(base.CFG_PETITE, T=2, n_instances=2)


def texte_grandes_racines(cfg) -> tuple[str, tuple[int, int]]:
    """Texte synthétique d'essai (jamais lancé comme réplication) dont les DEUX racines de la règle D dépassent 2⁶³ :
    recherche déterministe sur une ligne de remplissage, aucun tirage."""
    socle = base.texte_prereg_synthetique(cfg)
    for k in range(256):
        t = socle + f"\nLigne de recherche de l'essai E10 (racines de plus de 2⁶³) : {k}\n"
        r = m.etat_regle_D(hashlib.sha256(t.encode("utf-8")).hexdigest())
        if min(r) >= DEUX_63:
            m.exiger_racines_regle_D(*r)
            return t, r
    raise AssertionError("aucun texte trouvé")


def test_E9_garde_C8_dans_de_vrais_processus_de_travail_neufs(tmp_path, sans_autorisation):
    """Pool `spawn` de deux processus neufs (rien hérité de l'autorisation du parent) : chaque tâche dont une racine
    diffère de la règle D du texte scellé est refusée AVANT tout calcul ; PID consignés, aucun orphelin. Le cas sain dans
    de vrais processus est E10."""
    texte, (rho, rho_t) = texte_grandes_racines(CFG_E10)
    p = tmp_path / "prereg-e9.md"
    p.write_text(texte, encoding="utf-8")
    sceller(p)
    assert m._AUTORISATION_DECISION == {"prereg_sha256": None, "racines": None}
    voisin = rho - 1 if rho + 1 >= 2 ** 64 else rho + 1
    voisin_t = rho_t - 1 if rho_t + 1 >= 2 ** 64 else rho_t + 1
    for k, (r, rt) in enumerate(((voisin, rho_t), (rho, voisin_t), base.RACINES_ORIGINALES, (rho_t, rho))):
        taches = [(0, 1, r, rt, asdict(CFG_E10), m.REGLES, (0.3,), ("moyenne",), False, str(p), 0.3, "moyenne")]
        pids = tmp_path / f"pids-{k}.txt"
        t0 = time.perf_counter()
        with pytest.raises(GardeArret, match="≠ racines dérivées"):
            m._lancer(taches, 2, pids)
        consignes = v4.lire_pids(pids)
        assert len(consignes) == 2 and all(pid != os.getpid() for pid, _ in consignes)
        v4.exiger_aucun_orphelin(consignes)
        print(f"E9 artefact {k} ({r}, {rt}) : refusé dans un processus neuf en {time.perf_counter() - t0:.1f} s")
    assert m._AUTORISATION_DECISION == {"prereg_sha256": None, "racines": None}     # le parent n'a rien posé


# ---------------------------------------------------------------------------------------------------------------
# E10 : bout en bout `main decision`, racines de plus de 2⁶³, dépôt git temporaire propre
# ---------------------------------------------------------------------------------------------------------------
def _git(depot: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(depot), "-c", "user.name=essai-E10", "-c", "user.email=essai@localhost",
                        "-c", "commit.gpgsign=false", *args], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout


def test_E10_bout_en_bout_main_decision_racines_de_plus_de_2_63(tmp_path, sans_autorisation):
    depot = tmp_path / "depot"
    (depot / "src" / "controle_ia").mkdir(parents=True)
    for f in m.FICHIERS_BIBLIOTHEQUE:                      # empreintes de bibliothèque exigées par l'identité
        shutil.copyfile(DEPOT / f, depot / f)
    texte, (rho, rho_t) = texte_grandes_racines(CFG_E10)
    (depot / "prereg").mkdir()
    p = depot / "prereg" / "prereg-synthetique-e10.md"
    p.write_text(texte, encoding="utf-8")
    sha = sceller(p)
    assert sha == hashlib.sha256(texte.encode("utf-8")).hexdigest() and (rho, rho_t) == m.deriver_racines_regle_D(sha)
    _git(depot, "init", "-q")
    _git(depot, "add", "-A")
    _git(depot, "commit", "-q", "-m", "essai E10")
    commit = _git(depot, "rev-parse", "HEAD").strip()
    assert _git(depot, "status", "--porcelain", "--untracked-files=all") == ""
    sans_autorisation.setattr(m, "DEPOT", depot)
    sans_autorisation.setattr(v4, "CONFIG_V4", CFG_E10)
    run_id = "20261101-000000-essai-e10"
    t0 = time.perf_counter()
    assert m.main(["decision", "--prereg", str(p), "--instances", "0:2", "--run-id", run_id, "--lambda", "0.3",
                   "--reference", "moyenne", "--processus", "2"]) == 0
    print(f"E10 : course de bout en bout (4 tâches, 2 processus spawn) en {time.perf_counter() - t0:.1f} s de mur ; "
          f"ρ = {rho}, ρ_t = {rho_t}")
    chemin_m = depot / "runs" / run_id / "manifeste.json"
    diag = depot / "diag" / run_id
    for f in (chemin_m, chemin_m.parent / "pids-travail.txt", diag / "resultats-regles-defense.json",
              diag / "analyse-regles-defense.json"):
        verifier(f)                                         # écrits ET scellés
    # manifeste : racines exactes (entiers JSON, jamais en binaire64) et chaînes ; texte et commit
    brut = chemin_m.read_text(encoding="utf-8")
    assert re.search(rf'"racine": {rho},', brut) and re.search(rf'"racine_tenue": {rho_t},', brut)
    assert "e+19" not in brut and "E+19" not in brut
    man_, _ = man.lire_manifeste(chemin_m)
    cfgm = man_["config"]
    assert type(cfgm["racine"]) is int and (cfgm["racine"], cfgm["racine_tenue"]) == (rho, rho_t)
    assert (cfgm["racine_chaine"], cfgm["racine_tenue_chaine"]) == (str(rho), str(rho_t))
    assert cfgm["prereg_sha256"] == sha == man_["preenregistrement"]["sha256"]
    assert man_["preenregistrement"]["chemin"] == "prereg/prereg-synthetique-e10.md"
    assert man_["commit"] == commit and man_["depot_propre"] is True and man_["decisif"] is True
    assert man_["graines"]["regles-defense"]["entropie"] == str(rho)
    assert cfgm["config_sha256"] == CFG_E10.empreinte() and cfgm["regle_racines"] == m.REGLE_D
    # résultats : 4 tâches, racines exactes dans chacune, sérialisation, rattachement au manifeste
    corps = man.verifier_resultat(depot, diag / "resultats-regles-defense.json")
    res = corps["resultat"]["resultats"]
    assert sorted((r["code_delta"], r["instance"]) for r in res) == [(1, 0), (1, 1), (2, 0), (2, 1)]
    for r in res:
        assert type(r["racine"]) is int and (r["racine"], r["racine_tenue"]) == (rho, rho_t)
        assert r["version"] == "arene_regles_defense_v3" and "loi_cible" in r
        assert list(r["regles"]) == ["R0", "R1", "R2", "R3", "R4[moyenne,λ=0.3]"]
        assert all("serialisation" in x for x in r["regles"].values())
    brut_r = (diag / "resultats-regles-defense.json").read_text(encoding="utf-8")
    assert brut_r.count(f'"racine": {rho},') == 4 and brut_r.count(f'"racine_tenue": {rho_t},') == 4
    # analyse écrite = recalcul au bit sur ρ (autorisation posée par `main` dans ce processus)
    an = man.verifier_resultat(depot, diag / "analyse-regles-defense.json")["resultat"]
    assert base.au_bit(an) == base.au_bit(m.analyser_regles(res, rho))
    assert m._AUTORISATION_DECISION == {"prereg_sha256": sha, "racines": (rho, rho_t)}
