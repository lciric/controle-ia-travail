"""Lecture complémentaire « par épisode » de R1-R2, code v7 : même calcul, même garde de concordance avec la principale,
même issue et même rendu que le code v5 (`lecture_v5.calculer`, `lecture_v5.exiger_concordance_principale`,
`lecture_v5.issue`, `lecture_v5.rendre`, `lecture_v4.lire_principale`, repris sans modification), plus les trois gardes
de réception de la relance v4 de R1 (`entrees_v4.exiger_reception_v4` : `texte`, `table-comparee`, `provenance`),
exigées par l'addendum v4 de R1 et mises en place par l'addendum 1 « gardes des analyses » (texte unique des trois
analyses, scellé). Ce que l'addendum unique impose au mode décisif, comme pour la principale (`lecture_v6`) :
- le texte scellé qui gouverne est inchangé (`constantes_v7.TEXTE`, 26a3ff72…) : passé à `--prereg`, vérifié scellé,
  conforme et égal au texte attendu ; ses graines, ses plis (ceux de la principale scellée, 8e267952…), sa liste fermée
  v5, son calcul, son issue et sa liste d'arrêt ne bougent pas ;
- l'addendum unique, scellé et conforme, porte la liste fermée du code v7 dans un bloc propre à cette lecture
  (`constantes_v7.TITRE_LISTE`) et l'empreinte des constantes v7 ;
- premier passage sous l'addendum : aucun manifeste sous `runs/` ne cite l'addendum avec la commande de ce code.

Commande décisive (depuis la racine de l'arbre de travail, après la principale sous le code v6) :
    PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v7 --fiche <fiche de la principale> \
        --principale diag/<run principal>/analyse-principale-r1-r2-v1.json --run-analyse <run> \
        --prereg prereg/analyse-par-episode-v1.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste
from ..prereg import exiger_prereg_scelle
from ..scellement import empreinte, sceller
from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import constantes_v4 as K4
from . import constantes_v5 as K5
from . import constantes_v6 as K6
from . import constantes_v7 as K7
from . import lecture_v1 as L1
from . import lecture_v5 as L5
from . import lecture_v6 as L6
from .entrees_v1 import charger_juge, charger_p3, charger_r1, lire_fiche, longueurs_textes
from .entrees_v4 import exiger_reception_v4

RACINE_CODE = L1.RACINE_CODE
FICHIERS_PAQUET = L5.FICHIERS_PAQUET + tuple(f"src/controle_ia/analyse_principale_r1_r2/{n}.py"
                                             for n in ("constantes_v6", "entrees_v4", "lecture_v6", "constantes_v7",
                                                       "lecture_v7"))
FICHIERS_ESSAIS = L5.FICHIERS_ESSAIS + ("tests/test_analyse_principale_r1_r2_v6.py", "tests/test_analyse_par_episode_v7.py")
FICHIERS_REUTILISES = L1.FICHIERS_REUTILISES
CITATION_CONSTANTES = re.compile(r"Empreinte des constantes \(analyse par épisode, code v7\) : `([0-9a-f]{64})`")
A1, A2, A5 = L5.A1, L5.A2, L5.A5
ALPHAS_PRINCIPALE = L5.ALPHAS_PRINCIPALE
lire_principale = L5.lire_principale                     # garde reprise des codes v4 et v5 (résultat intact, rattaché, lié)
exiger_concordance_principale = L5.exiger_concordance_principale
calculer = L5.calculer
issue = L5.issue
rendre = L5.rendre


def exiger_code_cite(texte: str, racine_code: Path = RACINE_CODE) -> dict:
    return L6.exiger_code_cite_sous(texte, K7.TITRE_LISTE,
                                    set(FICHIERS_PAQUET) | set(FICHIERS_ESSAIS) | set(FICHIERS_REUTILISES),
                                    CITATION_CONSTANTES, K7.empreinte_constantes(), racine_code)


# --------------------------------------------------------------------------------------------- point d'entrée
def analyser(racine, fiche: str, principale: str, run_analyse: str, prereg: str | None, entropie: int | None = None,
             entropie_plis: int | None = None, autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    lien = addendum = None
    if prereg is not None:
        sha_p = exiger_prereg_scelle(racine / prereg)
        L6.exiger_texte(prereg, sha_p, K7.TEXTE)
        L1.exiger_code_importe_sous(racine)
        cite_texte = L5.exiger_code_cite((racine / prereg).read_text(encoding="utf-8"))     # liste fermée v5 du texte
        sha_a = exiger_prereg_scelle(racine / K7.ADDENDUM)
        cite = exiger_code_cite((racine / K7.ADDENDUM).read_text(encoding="utf-8"))          # liste fermée v7, addendum
        attendue = K2.entropie_de(sha_p)
        if entropie is not None and int(entropie) != attendue:
            raise GardeArret(f"entropie {entropie} ≠ entropie dérivée de l'empreinte du préenregistrement scellé")
        if entropie_plis is not None and int(entropie_plis) != K7.entropie_principale():
            raise GardeArret("entropie des plis ≠ celle de la principale scellée (8e267952…)")
        entropie, entropie_plis = attendue, K7.entropie_principale()
        addendum = {"chemin": K7.ADDENDUM, "sha256": sha_a}
        lien = {"preenregistrement": prereg, "sha256": sha_p, "code_cite": cite_texte,
                "addendum": {**addendum, "code_cite": cite},
                "passages": L6.exiger_premier_passage_sous(racine, K7.ADDENDUM, sha_a, K7.COMMANDE, sha_p),
                "versions": L1.exiger_versions()}
    elif entropie is None or entropie_plis is None:
        raise GardeArret("mode non décisif : entropie et entropie des plis explicites exigées")
    f, sha_f = lire_fiche(racine, fiche, scellee=prereg is not None)
    rp = lire_principale(racine, principale, sha_f, entropie_plis, prereg is not None)
    src = r1 = j3 = j8 = longueurs = reception = None
    if f["R1"] is not None:
        src = charger_p3(racine)
        longueurs = longueurs_textes(racine, src["tables"])
        r1 = charger_r1(racine, f["R1"], src["tables"])
        reception = exiger_reception_v4(racine, f["R1"]["resultat"]["chemin"])   # texte, table-comparee, provenance
        if f["R2"] is not None:
            j3 = charger_juge(racine, f["R2"]["juge3b"], src["tables"], "J3")
            if f["R2"]["juge8b"] is not None:
                j8 = charger_juge(racine, f["R2"]["juge8b"], src["tables"], "J8")
    config = {"fiche": fiche, "fiche_sha256": sha_f, "principale": principale, "principale_sha256":
              empreinte(racine / principale), "addendum": addendum, "constantes": K7.constantes_courantes(),
              "constantes_sha256": K7.empreinte_constantes(), "entropie_plis": str(entropie_plis)}
    chemin_m, manifeste = creer_manifeste(racine, run_analyse, config, list(K4.CLES_GRAINES), entropie=int(entropie),
                                          decisif=prereg is not None,
                                          prereg=None if prereg is None else str(racine / prereg),
                                          autoriser_depot_sale=autoriser_depot_sale, commande=K7.COMMANDE)
    g = manifeste["graines"]
    if any(int(x["entropie"]) != int(entropie) for x in g.values()):
        raise GardeArret("graines du manifeste non dérivées de l'entropie exigée")
    resultat = {"version": K7.VERSION, "statut": "décisif" if prereg is not None else "non décisif (essai)",
                "lien_au_preenregistrement": lien, "entropie": str(entropie), "entropie_plis": str(entropie_plis),
                "regle_entropie": K4.REGLE_ENTROPIE, "motif_R1": f["motif_R1"], "motif_R2": f["motif_R2"],
                "reception_v4": reception,
                "principale": {"chemin": principale, "sha256": empreinte(racine / principale)}}
    if r1 is None:
        resultat["mode"] = "rejeu non validé"
        resultat["concordance_principale"] = exiger_concordance_principale(rp, None, {}, {}, resultat["mode"])
    else:
        resultat["mode"] = "complet" if j3 is not None else "sans R2"
        calc = calculer(src, r1, j3, j8, longueurs, g, entropie_plis)
        resultat["concordance_principale"] = exiger_concordance_principale(rp, calc["plis"], calc.pop("_act"),
                                                                           calc.pop("_non_lus"), resultat["mode"])
        resultat["calcul"] = calc
        resultat["classes_principale"] = rp["issue"].get("classes", {})
        resultat["reserves_principale"] = list(rp["issue"].get("reserves", []))
    resultat["issue"] = issue(resultat)
    resultat = L1._json(resultat)
    chemin_j = ecrire_resultat(racine, chemin_m, K7.NOM_SORTIE, resultat)
    md = Path(chemin_j).with_suffix(".md")
    if md.exists():
        raise GardeArret(f"{md} existe déjà (R12)")
    md.write_text(rendre(resultat, empreinte(chemin_j)), encoding="utf-8")
    sceller(md)
    lire_manifeste(chemin_m)
    return resultat


def _main(argv) -> int:
    ap = argparse.ArgumentParser(prog=K7.COMMANDE)
    ap.add_argument("--fiche", required=True)
    ap.add_argument("--principale", required=True)
    ap.add_argument("--run-analyse", required=True)
    ap.add_argument("--prereg", required=True)
    a = ap.parse_args(argv)
    s = analyser(Path("."), a.fiche, a.principale, a.run_analyse, a.prereg)
    print(json.dumps({"issue": s["issue"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
