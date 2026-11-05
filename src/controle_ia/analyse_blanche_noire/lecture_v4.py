"""Lecture appariée, version 4 du code (texte scellé `analyse-blanche-noire-v3`, inchangé ; addendum 1 « gardes des
analyses », relance v4 de R1). Version 4 = version 3 reprise sans modification (`lecture_v3.calculer_p3`,
`lecture_v3.calculer_r4`, `lecture_v3.issue_v3`, `rendu_v3.rendre_v3`, chargeurs `entrees_v3`), plus les trois gardes
de réception de la relance v4 de R1 (`entrees_v4.exiger_reception_v4` : `texte`, `table-comparee`, `provenance`),
exigées par l'addendum v4 de R1. Ce que l'addendum unique impose au mode décisif, et rien d'autre :
- le texte scellé qui gouverne est inchangé (`constantes_v4.TEXTE`, 1f6a6da2…) : passé à `--prereg`, vérifié scellé,
  conforme et égal au texte attendu ; ses graines, sa liste fermée v3, son calcul, son issue et sa liste d'arrêt ne
  bougent pas ;
- l'addendum unique (`constantes_v4.ADDENDUM`), scellé et conforme, porte la liste fermée de la version 4 dans un bloc
  propre à cette analyse (`constantes_v4.TITRE_LISTE`) et l'empreinte des constantes (v4) ;
- premier passage sous l'addendum : aucun manifeste sous `runs/` ne cite l'addendum (chemin ou empreinte) avec la
  commande de ce code ; les passages du texte sous la version 3 (course v3 de R1) et ceux des deux autres analyses sous
  le même addendum ne comptent pas (ils sont comptés et écrits).
Les gardes du mode décisif sont recopiées de `analyse_principale_r1_r2.lecture_v6` (le paquet secondaire ne charge aucun
module du paquet principal).
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
from . import constantes as C
from . import constantes_v3 as C3
from . import constantes_v4 as C4
from . import lecture as L1
from . import lecture_v3 as L3
from .entrees import pointeur
from .entrees_v3 import charger_activations_v3, charger_juge, charger_run_v3, exiger_juge_3b, lire_fiche_v3
from .entrees_v4 import exiger_reception_v4
from .rendu_v3 import rendre_v3

RACINE_CODE = L1.RACINE_CODE
FICHIERS_PAQUET = L3.FICHIERS_PAQUET + tuple(f"src/controle_ia/analyse_blanche_noire/{n}.py"
                                             for n in ("constantes_v4", "entrees_v4", "lecture_v4"))
FICHIERS_ESSAIS = L3.FICHIERS_ESSAIS + ("tests/test_analyse_blanche_noire_v4.py",)
FICHIERS_REUTILISES = L1.FICHIERS_REUTILISES
CITATION = L1.CITATION
CITATION_CONSTANTES = re.compile(r"Empreinte des constantes \(analyse secondaire, code v4\) : `([0-9a-f]{64})`")
calculer_p3 = L3.calculer_p3
calculer_r4 = L3.calculer_r4
issue_v4 = L3.issue_v3                                     # issue de la version 3, inchangée
ligne_comparaison = L3.ligne_comparaison
exiger_versions = L3.exiger_versions


# --------------------------------------------------------------------------------------------- gardes du mode décisif
def exiger_texte(prereg: str, sha_prereg: str, texte: dict) -> None:
    """Le texte passé à `--prereg` est le texte scellé qui gouverne cette analyse (chemin et empreinte) : l'addendum
    unique ne le change pas."""
    if str(Path(prereg)) != texte["chemin"] or sha_prereg != texte["sha256"]:
        raise GardeArret(f"texte passé ({prereg}, {sha_prereg[:12]}…) ≠ texte scellé qui gouverne cette analyse "
                         f"({texte['chemin']}, {texte['sha256'][:12]}…) : l'addendum ne le change pas")


def liste_fermee_de(texte: str, titre: str) -> str:
    """Bloc de l'addendum unique qui porte la liste fermée de cette analyse : de la ligne de titre (entière) à la ligne
    de titre suivante (`## ` ou `### `). Les listes des deux autres analyses, dans leurs blocs, ne sont pas lues."""
    lignes = texte.splitlines()
    try:
        debut = lignes.index(titre)
    except ValueError:
        raise GardeArret(f"liste fermée absente de l'addendum : titre « {titre} » introuvable") from None
    fin = len(lignes)
    for i in range(debut + 1, len(lignes)):
        if lignes[i].startswith("## ") or lignes[i].startswith("### "):
            fin = i
            break
    return "\n".join(lignes[debut:fin])


def exiger_code_cite(texte: str, racine_code: Path = RACINE_CODE) -> dict:
    """Liste fermée de la version 4, lue dans le bloc de cette analyse dans l'addendum unique (même citation et même
    règle que `lecture.exiger_code_cite`) ; empreinte des constantes (v4), citée une fois dans l'addendum."""
    bloc = liste_fermee_de(texte, C4.TITRE_LISTE)
    cites = {}
    for m in CITATION.finditer(bloc):
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
            raise GardeArret(f"{chemin} : empreinte ≠ empreinte citée par l'addendum")
    m = CITATION_CONSTANTES.search(texte)
    if m is None or m.group(1) != C4.empreinte_constantes():
        raise GardeArret("constantes gelées ≠ empreinte citée par l'addendum")
    return {"fichiers": cites, "constantes": m.group(1)}


def exiger_premier_passage_v4(racine: Path, addendum_rel: str, sha_addendum: str, sha_texte: str) -> dict:
    """Premier passage de cette analyse sous l'addendum unique : aucun manifeste sous `runs/` ne cite l'addendum (chemin
    ou empreinte) avec la commande de ce code ; un manifeste illisible qui cite l'addendum arrête aussi. Les manifestes
    des deux autres analyses sous le même addendum (autre commande) et les passages antérieurs du texte sous ses codes
    antérieurs (course v3 de R1, déclarés par l'addendum) ne comptent pas : ils sont comptés et écrits."""
    lus, autres, anterieurs = 0, 0, 0
    for p in sorted((Path(racine) / "runs").glob("*/manifeste.json")):
        brut = p.read_bytes()
        lus += 1
        cite_addendum = sha_addendum.encode("ascii") in brut or addendum_rel.encode("utf-8") in brut
        try:
            m = json.loads(brut.decode("utf-8"))
        except ValueError:
            m = None
        if not isinstance(m, dict):
            if cite_addendum:
                raise GardeArret(f"second passage possible : manifeste illisible {p.parent.name} qui cite l'addendum "
                                 f"{addendum_rel} — nœud de Lazar")
            continue
        if cite_addendum and m.get("commande") == C4.COMMANDE:
            raise GardeArret(f"second passage : {p.parent.name} a déjà été lancé sous l'addendum {addendum_rel} avec la "
                             f"commande « {C4.COMMANDE} » — nœud de Lazar")
        if cite_addendum:
            autres += 1
        elif ((m.get("preenregistrement") or {}).get("sha256")) == sha_texte:
            anterieurs += 1
    return {"manifestes_lus": lus, "autres_analyses_sous_l_addendum": autres,
            "passages_anterieurs_du_texte_hors_addendum": anterieurs}


# ----------------------------------------------------------------------------------------------------- analyse
def analyser_v4(racine, fiche: str, run_analyse: str, prereg: str | None, entropie: int | None = None,
                autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    lien = addendum = None
    if prereg is not None:
        sha_p = exiger_prereg_scelle(racine / prereg)
        exiger_texte(prereg, sha_p, C4.TEXTE)
        L1.exiger_code_importe_sous(racine)
        cite_texte = L3.exiger_code_cite((racine / prereg).read_text(encoding="utf-8"))     # liste fermée v3 du texte
        sha_a = exiger_prereg_scelle(racine / C4.ADDENDUM)
        cite = exiger_code_cite((racine / C4.ADDENDUM).read_text(encoding="utf-8"))          # liste fermée v4, addendum
        e = L1.entropie_de(sha_p)
        if entropie is not None and int(entropie) != e:
            raise GardeArret(f"entropie {entropie} ≠ entropie dérivée de l'empreinte du préenregistrement")
        entropie = e
        addendum = {"chemin": C4.ADDENDUM, "sha256": sha_a}
        lien = {"preenregistrement": prereg, "sha256": sha_p, "code_cite": cite_texte,
                "addendum": {**addendum, "code_cite": cite},
                "passages": exiger_premier_passage_v4(racine, C4.ADDENDUM, sha_a, sha_p),
                "versions": exiger_versions()}
    elif entropie is None:
        raise GardeArret("mode non décisif : entropie explicite exigée")
    f, sha_f = lire_fiche_v3(racine, fiche, scellee=prereg is not None)
    source = charger_run_v3(racine, C.RUN_P3, C.EMPREINTES_P3)
    acts = charger_activations_v3(racine, f["R1"], source) if f["R1"] is not None else None
    reception = exiger_reception_v4(racine, f["R1"]["manifeste"]["chemin"]) if f["R1"] is not None else None
    juge = charger_juge(racine, f["R2"], source) if f["R2"] is not None else None
    part_anomalie = exiger_juge_3b(racine, f["R2"], juge) if juge is not None else None
    mode = "complet" if juge is not None else "R1 seul"
    famille = C3.COMPARAISONS_HOLM if juge is not None else C3.COMPARAISONS_HOLM_R1_SEUL
    r4, source4, acts4, juge4, dose, echec4 = f["R4"], None, None, None, None, None
    if r4 is not None:
        try:
            source4 = charger_run_v3(racine, r4["run"], None)
            if not r4["empreintes"] or any(source4["empreintes"].get(k) != v for k, v in r4["empreintes"].items()):
                raise GardeArret("R4 : empreintes des données ≠ empreintes déclarées par la fiche")
            m4, _ = lire_manifeste(racine / "runs" / r4["run"] / "manifeste.json")
            dose = pointeur(m4, r4["pointeur_dose"])
            acts4 = charger_activations_v3(racine, r4["activations"], source4) if r4["activations"] else None
            juge4 = None                 # R-1086 : juge sur les seuls textes de P3 (R4.juge refusé par la fiche)
        except Exception as e:           # réplication non décisive : toute erreur sur ses entrées la met en échec
            echec4 = f"intégrité de R4 : {type(e).__name__} : {e}"
    config = {"fiche": fiche, "fiche_sha256": sha_f, "run_p3": C.RUN_P3, "addendum": addendum,
              "constantes": C4.constantes_courantes(), "constantes_sha256": C4.empreinte_constantes()}
    chemin_m, manifeste = creer_manifeste(racine, run_analyse, config, C4.cles_de_graines(), entropie=entropie,
                                          decisif=prereg is not None,
                                          prereg=None if prereg is None else str(racine / prereg),
                                          autoriser_depot_sale=autoriser_depot_sale, commande=C4.COMMANDE)
    graines = manifeste["graines"]
    if any(int(g["entropie"]) != int(entropie) for g in graines.values()):
        raise GardeArret("graines du manifeste non dérivées de l'entropie exigée")
    resultat = {"version": C4.VERSION, "mode": mode,
                "statut": "décisif" if prereg is not None else "non décisif (essai)",
                "lien_au_preenregistrement": lien, "entropie": str(entropie), "reception_v4": reception,
                "entrees": {"fiche": {"chemin": fiche, "sha256": sha_f, "redaction": f["redaction"]},
                            "P3": {"run": C.RUN_P3, "empreintes": source["empreintes"]},
                            "R1": None if acts is None else {"empreintes": acts["empreintes"], "faits": acts["faits"],
                                                             "dtype": acts["dtype"],
                                                             "motif_maximum": acts["motif_maximum"]},
                            "R2": None if juge is None else {"empreintes": juge["empreintes"], "faits": juge["faits"],
                                                             "autres_tableaux": juge["autres_tableaux"],
                                                             "part_anomalie": part_anomalie},
                            "motif_R1": f["motif_R1"], "motif_R2": f["motif_R2"],
                            "R4": None if r4 is None else {"run": r4["run"], "echec": echec4, "dose": dose,
                                                           "partiel": None if source4 is None else source4["partiel"],
                                                           "motif_partiel": None if source4 is None
                                                           else source4.get("motif_partiel")}},
                "constantes": C4.constantes_courantes()}
    resultat["P3"] = calculer_p3(source, acts, juge, graines, famille, f["motif_R2"])
    if r4 is None:
        resultat["R4"] = None
    elif echec4:
        resultat["R4"] = {"echec": echec4}
    else:
        etablies = [k for k, c in resultat["P3"]["comparaisons"].items() if ligne_comparaison(k, c)[0] == "etablie"]
        try:
            resultat["R4"] = calculer_r4(source, acts, source4, acts4, juge4, graines, etablies)
        except Exception as e:           # idem pour son calcul : la lecture de P3 n'est jamais perdue par R4
            resultat["R4"] = {"echec": f"calcul de R4 : {type(e).__name__} : {e}"}
    resultat["issue"] = issue_v4(resultat)
    resultat = L1._json(resultat)
    chemin_j = ecrire_resultat(racine, chemin_m, C4.NOM_SORTIE, resultat)
    md = Path(chemin_j).with_suffix(".md")
    if md.exists():
        raise GardeArret(f"{md} existe déjà (R12)")
    md.write_text(rendre_v3(resultat, empreinte(chemin_j)), encoding="utf-8")
    sceller(md)
    lire_manifeste(chemin_m)
    return resultat


def _main(argv) -> int:
    ap = argparse.ArgumentParser(prog=C4.COMMANDE)
    ap.add_argument("--fiche", required=True)
    ap.add_argument("--run-analyse", required=True)
    ap.add_argument("--prereg", required=True)
    a = ap.parse_args(argv)
    s = analyser_v4(Path("."), a.fiche, a.run_analyse, a.prereg)
    print(json.dumps({"issue": s["issue"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
