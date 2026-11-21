"""La règle composée de désignation de l'oracle de la règle, v5 (texte scellé, section 5.1 ; section 13, `designation_v5.py`).

Scellée avec le texte avant l'étalonnage ; aucune liberté après lui. `designer` est une **fonction pure de ses entrées, sans
paramètre et sans état : elle seule nomme l'issue.**

1. Si l'étalonnage est non calculable : issue `non_calculable` ; aucune thèse, aucun nombre de tours.
2. Si l'oracle à contexte réécrit (N) remplit ses conditions : issue `N` ; thèse « excès borné en niveau » ; variante N de la
   consigne ; nombre de tours de N.
3. Sinon, si l'oracle au contexte de l'agent (P) remplit les siennes : issue `P` ; thèse « petit ajout à chaque pas, sachant les
   précédents » ; variante P de la consigne ; nombre de tours de P.
4. Sinon : issue `ne_part_pas` ; une phrase par oracle (« non faisable » avec son motif, ou « en défaut » avec son épreuve).
L'ordre est fixe : N d'abord. Si N est en défaut et P sain, l'issue est P et le message de l'épreuve de N accompagne toute
citation. Si la coupe est en échec, les deux oracles sont en défaut : `ne_part_pas`.

Entrées : le résultat **scellé** de `branches_v5` (chemin ; son sceau est vérifié, et il doit citer l'étalonnage attendu) et les
empreintes des deux variantes de la consigne du maître. Le refus d'un second passage n'est pas dans la fonction : c'est le
lanceur qui refuse de l'appeler dès que le résultat scellé existe (`ecrire` refuse d'écraser, par surcroît).
`configuration_de_course` est le seul endroit du code qui écrit `oracle_de_la_regle` dans une configuration.
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import configuration_v5 as cf
from .branches_v5 import CLAUSE_DU_PREMIER_COUT

ISSUES = ("N", "P", "ne_part_pas", "non_calculable")
_SHA = re.compile(r"[0-9a-f]{64}")


def designer(chemin_branches, empreinte_etalonnage: str, variantes_consigne: dict) -> dict:
    """Issue de la règle composée. `empreinte_etalonnage` : empreinte du fichier scellé de l'étalonnage attendu ;
    `variantes_consigne` : {"N": empreinte, "P": empreinte} des deux variantes scellées de la consigne du maître."""
    chemin_branches = Path(chemin_branches)
    sha_b = verifier(chemin_branches)                                 # résultat non scellé : refus
    b = json.loads(chemin_branches.read_text(encoding="utf-8"))
    if b.get("schema") != cf.SCHEMA_BRANCHES:
        raise GardeArret("désignation : l'entrée n'est pas un résultat des conditions de départ (schéma)")
    if not isinstance(empreinte_etalonnage, str) or not _SHA.fullmatch(empreinte_etalonnage):
        raise GardeArret("désignation : empreinte de l'étalonnage attendu illisible")
    if (b.get("references") or {}).get("etalonnage", {}).get("sha256") != empreinte_etalonnage:
        raise GardeArret("désignation : le résultat des conditions de départ est celui d'un autre étalonnage (refus)")
    if not isinstance(variantes_consigne, dict) or set(variantes_consigne) != {"N", "P"} or \
            any(not isinstance(v, str) or not _SHA.fullmatch(v) for v in variantes_consigne.values()):
        raise GardeArret("désignation : une variante de la consigne du maître est absente (les deux empreintes, N et P, sont exigées avant "
                         "l'étalonnage) : refus")
    if variantes_consigne["N"] == variantes_consigne["P"]:
        raise GardeArret("désignation : les deux variantes de la consigne ont la même empreinte (refus)")
    sortie = {"schema": cf.SCHEMA_DESIGNATION, "avertissement": cf.AVERTISSEMENT, "branches": {"nom": chemin_branches.name, "sha256": sha_b},
              "etalonnage": {"sha256": empreinte_etalonnage}, "issue": None, "these": None, "variante_consigne": None, "tours": None,
              "phrases": [], "message_epreuve_de_N": None}
    if b.get("non_calculable") is not None:
        sortie.update({"issue": "non_calculable", "motif": b["non_calculable"],
                       "phrases": [f"Étalonnage non calculable (motif : {b['non_calculable']}) ; aucune thèse éprouvée."]})
        return sortie
    n, p = b["oracles"]["N"], b["oracles"]["P"]
    if n["motif"] == "en_defaut":
        sortie["message_epreuve_de_N"] = n["epreuve"]
    autre = "L'autre oracle, calculé sur les mêmes épisodes, aurait rendu : "
    if n["remplit"]:
        tete = f"Sous la thèse « {cf.THESES['N']} », désignée par la règle scellée avant l'étalonnage (issue [N]) : "
        sortie.update({"issue": "N", "these": cf.THESES["N"], "variante_consigne": {"variante": "N", "sha256": variantes_consigne["N"]},
                       "tours": int(n["tours"]),
                       "phrases": [tete + n["phrase"], autre + p["phrase"], CLAUSE_DU_PREMIER_COUT]})
    elif p["remplit"]:
        motif_n = n["epreuve"] if n["motif"] == "en_defaut" else n["motif"].replace("_", " ")
        tete = (f"Sous la thèse « {cf.THESES['P']} », désignée par la règle scellée avant l'étalonnage (issue [P]) : l'oracle à contexte "
                f"réécrit n'a pas rempli ses conditions de départ (motif : {motif_n}) ; la thèse d'un excès borné en niveau n'a pas été "
                "éprouvée. ")
        sortie.update({"issue": "P", "these": cf.THESES["P"], "variante_consigne": {"variante": "P", "sha256": variantes_consigne["P"]},
                       "tours": int(p["tours"]),
                       "phrases": [tete + p["phrase"], autre + n["phrase"], CLAUSE_DU_PREMIER_COUT]})
    else:
        sortie.update({"issue": "ne_part_pas",
                       "phrases": [f"Oracle [N] : {n['phrase']}", f"Oracle [P] : {p['phrase']}", CLAUSE_DU_PREMIER_COUT]})
    sortie["motifs"] = {"N": n["motif"], "P": p["motif"]}
    return sortie


def ecrire(resultat: dict, chemin) -> str:
    """Écrit et scelle le résultat de la désignation ; refuse d'écraser (un second résultat n'existe pas)."""
    if resultat.get("schema") != cf.SCHEMA_DESIGNATION or resultat.get("issue") not in ISSUES:
        raise GardeArret("désignation : résultat mal formé")
    chemin = Path(chemin)
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : la désignation ne se joue qu'une fois (second passage refusé)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(resultat, indent=1, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return sceller(chemin)


def configuration_de_course(config_etalonnage: dict, racine, chemin_designation: str) -> dict:
    """Configuration de la course : celle de l'étalonnage, où `oracle_de_la_regle` porte l'issue et l'empreinte du résultat scellé
    de la désignation. Refus si l'issue n'est ni N ni P (la course ne part pas), ou si la configuration en porte déjà un."""
    if config_etalonnage["oracle_de_la_regle"] != {"valeur": None, "designation": None}:
        raise GardeArret("configuration de course : la configuration porte déjà un oracle de la règle (refus)")
    chemin = Path(racine) / chemin_designation
    sha = verifier(chemin)
    r = json.loads(chemin.read_text(encoding="utf-8"))
    if r.get("schema") != cf.SCHEMA_DESIGNATION or r.get("issue") not in ("N", "P"):
        raise GardeArret(f"pas de course sans résultat de désignation scellé « part » (issue lue : {r.get('issue')!r})")
    c = copy.deepcopy(config_etalonnage)
    c["oracle_de_la_regle"] = {"valeur": r["issue"], "designation": {"chemin": str(chemin_designation), "sha256": sha}}
    cf.exiger_oracle_de_la_regle(c, racine)
    return c
