"""Analyse principale de R1-R2, code v2 : même calcul et même issue que `lecture_v1` (repris sans modification), avec deux
changements décidés par conv-audit (R-1091) :
- Q9 : racine des graines = 128 premiers bits de l'empreinte de **ce** préenregistrement scellé (mode décisif) ; en mode
  non décisif (essais), une entropie explicite est exigée ;
- Q8 : la combinaison « W − J3s supérieure, mention contraire » s'écrit « nœud de lecture (décision de Lazar) », sans
  verdict.

Commande décisive (depuis la racine de l'arbre de travail de l'étape 0) :
    PYTHONPATH=src python -m controle_ia.analyse_principale_r1_r2.lecture_v2 --fiche <fiche> --run-analyse <run> \
        --prereg prereg/analyse-principale-r1-r2-v1.md
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
from . import lecture_v1 as L1
from .entrees_v1 import charger_juge, charger_p3, charger_r1, lire_fiche, longueurs_textes

RACINE_CODE = L1.RACINE_CODE
FICHIERS_PAQUET = L1.FICHIERS_PAQUET + tuple(f"src/controle_ia/analyse_principale_r1_r2/{n}.py"
                                             for n in ("constantes_v2", "lecture_v2"))
FICHIERS_ESSAIS = ("tests/test_analyse_principale_r1_r2_v1.py", "tests/test_analyse_principale_r1_r2_v2.py")
FICHIERS_REUTILISES = L1.FICHIERS_REUTILISES
CITATION_CONSTANTES = re.compile(r"Empreinte des constantes \(analyse principale, code v2\) : `([0-9a-f]{64})`")
PHRASE_Q8_V1 = ("aucune ligne gelée ne s'applique (la ligne « au-dessus » exige mention conforme) : Δ rapporté, nœud de "
                "lecture porté à Lazar")


def exiger_code_cite(texte: str, racine_code: Path = RACINE_CODE) -> dict:
    cites = {}
    for m in L1.CITATION.finditer(texte):
        if m.group(1) in cites and cites[m.group(1)] != m.group(2):
            raise GardeArret(f"{m.group(1)} cité avec deux empreintes")
        cites[m.group(1)] = m.group(2)
    attendus = set(FICHIERS_PAQUET) | set(FICHIERS_ESSAIS) | set(FICHIERS_REUTILISES)
    if set(cites) != attendus:
        raise GardeArret(f"code cité ≠ liste fermée : manquants {sorted(attendus - set(cites))}, "
                         f"en trop {sorted(set(cites) - attendus)}")
    for chemin, sha in sorted(cites.items()):
        p = Path(racine_code) / chemin
        if not p.is_file() or empreinte(p) != sha:
            raise GardeArret(f"{chemin} : empreinte ≠ empreinte citée par le préenregistrement")
    m = CITATION_CONSTANTES.search(texte)
    if m is None or m.group(1) != K2.empreinte_constantes():
        raise GardeArret("constantes gelées ≠ empreinte citée par le préenregistrement")
    return {"fichiers": cites, "constantes": m.group(1)}


def issue(r: dict) -> dict:
    """Issue de `lecture_v1` ; seule la phrase de la combinaison non couverte (Q8) change de libellé."""
    i = L1.issue(r)
    i["lignes"] = [x.replace(PHRASE_Q8_V1, K2.MOTIF_Q8) for x in i["lignes"]]
    return i


def analyser(racine, fiche: str, run_analyse: str, prereg: str | None, entropie: int | None = None,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    lien = None
    if prereg is not None:
        sha_p = exiger_prereg_scelle(racine / prereg)
        L1.exiger_code_importe_sous(racine)
        cite = exiger_code_cite((racine / prereg).read_text(encoding="utf-8"))
        attendue = K2.entropie_de(sha_p)
        if entropie is not None and int(entropie) != attendue:
            raise GardeArret(f"entropie {entropie} ≠ entropie dérivée de l'empreinte du préenregistrement scellé")
        entropie = attendue
        lien = {"preenregistrement": prereg, "sha256": sha_p, "code_cite": cite,
                "passages": L1.exiger_premier_passage(racine, str(Path(prereg)), sha_p),
                "versions": L1.exiger_versions()}
    elif entropie is None:
        raise GardeArret("mode non décisif : entropie explicite exigée")
    f, sha_f = lire_fiche(racine, fiche, scellee=prereg is not None)
    src = r1 = j3 = j8 = longueurs = None
    if f["R1"] is not None:
        src = charger_p3(racine)
        longueurs = longueurs_textes(racine, src["tables"])
        r1 = charger_r1(racine, f["R1"], src["tables"])
        if f["R2"] is not None:
            j3 = charger_juge(racine, f["R2"]["juge3b"], src["tables"], "J3")
            if f["R2"]["juge8b"] is not None:
                j8 = charger_juge(racine, f["R2"]["juge8b"], src["tables"], "J8")
    config = {"fiche": fiche, "fiche_sha256": sha_f, "prereg_fournisseur": K.PREREG_FOURNISSEUR,
              "constantes": K2.constantes_courantes(), "constantes_sha256": K2.empreinte_constantes()}
    chemin_m, manifeste = creer_manifeste(racine, run_analyse, config, list(K.CLES_GRAINES), entropie=int(entropie),
                                          decisif=prereg is not None,
                                          prereg=None if prereg is None else str(racine / prereg),
                                          autoriser_depot_sale=autoriser_depot_sale, commande=K2.COMMANDE)
    graines = manifeste["graines"]
    if any(int(g["entropie"]) != int(entropie) for g in graines.values()):
        raise GardeArret("graines du manifeste non dérivées de l'entropie exigée")
    resultat = {"version": K2.VERSION, "statut": "décisif" if prereg is not None else "non décisif (essai)",
                "lien_au_preenregistrement": lien, "entropie": str(entropie), "regle_entropie": K2.REGLE_ENTROPIE,
                "motif_R1": f["motif_R1"], "motif_R2": f["motif_R2"],
                "entrees": {"fiche": {"chemin": fiche, "sha256": sha_f, "redaction": f["redaction"]},
                            "R1": None if r1 is None else r1["empreintes"],
                            "R2": None if j3 is None else {"J3": j3["empreintes"],
                                                           "J8": None if j8 is None else j8["empreintes"]}}}
    if r1 is None:
        resultat["mode"] = "rejeu non validé"
    else:
        resultat["mode"] = "complet" if j3 is not None else "sans R2"
        resultat["calcul"] = L1.calculer(src, r1, j3, j8, longueurs, graines)
    resultat["issue"] = issue(resultat)
    resultat = L1._json(resultat)
    chemin_j = ecrire_resultat(racine, chemin_m, K2.NOM_SORTIE, resultat)
    md = Path(chemin_j).with_suffix(".md")
    if md.exists():
        raise GardeArret(f"{md} existe déjà (R12)")
    md.write_text(L1.rendre(resultat, empreinte(chemin_j)), encoding="utf-8")
    sceller(md)
    lire_manifeste(chemin_m)
    return resultat


def _main(argv) -> int:
    ap = argparse.ArgumentParser(prog=K2.COMMANDE)
    ap.add_argument("--fiche", required=True)
    ap.add_argument("--run-analyse", required=True)
    ap.add_argument("--prereg", required=True)
    a = ap.parse_args(argv)
    s = analyser(Path("."), a.fiche, a.run_analyse, a.prereg)
    print(json.dumps({"issue": s["issue"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
