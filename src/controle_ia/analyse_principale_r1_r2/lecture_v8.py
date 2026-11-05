"""Analyse principale de R1-R2, code v8 : même calcul, même issue et même rendu que le code v2 (`lecture_v1.calculer`,
`lecture_v2.issue`, `lecture_v1.rendre`, repris sans modification), plus les trois gardes de réception de la relance v4
de R1 (`entrees_v5.exiger_reception_v4` : `texte`, `table-comparee`, `provenance`), exigées par l'addendum v4 de R1 et
mises en place par l'addendum 1 « gardes des analyses » (texte unique des trois analyses, scellé). Le code v8 remplace
le code v6 après la contre-lecture 1 (corrections K1 et K2) ; le code v6 n'est pas chargé. Ce que l'addendum unique
impose au mode décisif, et rien d'autre :
- le texte scellé qui gouverne est inchangé (`constantes_v8.TEXTE`, 8e267952…) : il est passé à `--prereg`, vérifié
  scellé, conforme et égal au texte attendu ; ses graines (Q9), sa liste fermée v2, son calcul, son issue et sa liste
  d'arrêt ne bougent pas ;
- l'addendum unique (`constantes_v8.ADDENDUM`), scellé et conforme, porte la liste fermée du code v8 dans un bloc propre
  à cette analyse (`constantes_v8.TITRE_LISTE`) et l'empreinte des constantes v8 ;
- K1 : les trois gardes de réception sont appelées juste après la lecture de la fiche, avant tout chargeur (aucun
  `.npz` ouvert si la chaîne du fournisseur est fausse) ;
- K2, premier passage par liste close : tout manifeste sous `runs/` qui cite le texte (chemin ou empreinte, dans ses
  octets) ou l'addendum arrête (`PassageHorsListe`, code de fin 2, message qui nomme le manifeste), sauf les trois
  manifestes de la course v3 (`constantes_v8.PASSAGES_V3`, run et empreinte gelés) et les manifestes des deux autres
  versions neuves sous l'addendum (`constantes_v8.COMMANDES_ADDENDUM`) ; les tolérés sont comptés et écrits, par nom.

Commande décisive (depuis la racine de l'arbre de travail, après la fiche de réception de la relance v4) :
    PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v8 --fiche <fiche> \
        --run-analyse <run> --prereg prereg/analyse-principale-r1-r2-v1.md
"""
from __future__ import annotations

import argparse
import hashlib
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
from . import constantes_v8 as K8
from . import lecture_v1 as L1
from . import lecture_v2 as L2
from .entrees_v1 import charger_juge, charger_p3, charger_r1, lire_fiche, longueurs_textes
from .entrees_v5 import exiger_reception_v4

RACINE_CODE = L1.RACINE_CODE
FICHIERS_PAQUET = L2.FICHIERS_PAQUET + tuple(f"src/controle_ia/analyse_principale_r1_r2/{n}.py"
                                             for n in ("constantes_v8", "entrees_v5", "lecture_v8"))
FICHIERS_ESSAIS = L2.FICHIERS_ESSAIS + ("tests/test_analyse_principale_r1_r2_v8.py",)
FICHIERS_REUTILISES = L1.FICHIERS_REUTILISES
CITATION_CONSTANTES = re.compile(r"Empreinte des constantes \(analyse principale, code v8\) : `([0-9a-f]{64})`")
CODE_FIN_PASSAGE = 2                                        # code de fin distinct de l'arrêt « passage hors liste close »
issue = L2.issue                                           # issue du code v2 (celle de v1, phrase de Q8), inchangée


class PassageHorsListe(GardeArret):
    """Arrêt distinct (K2) : un manifeste sous `runs/` cite le texte ou l'addendum hors de la liste close des passages
    tolérés (second passage, commande inconnue, manifeste illisible, passage antérieur non gelé ou altéré)."""


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


def exiger_code_cite_sous(texte: str, titre: str, attendus: set, citation_constantes, empreinte_attendue: str,
                          racine_code: Path = RACINE_CODE) -> dict:
    """Liste fermée d'une analyse, lue dans son bloc de l'addendum unique (même citation et même règle que
    `lecture_v1.exiger_code_cite`) ; empreinte des constantes, citée une fois dans l'addendum (motif propre à l'analyse)."""
    bloc = liste_fermee_de(texte, titre)
    cites = {}
    for m in L1.CITATION.finditer(bloc):
        if m.group(1) in cites and cites[m.group(1)] != m.group(2):
            raise GardeArret(f"{m.group(1)} cité avec deux empreintes")
        cites[m.group(1)] = m.group(2)
    if set(cites) != set(attendus):
        raise GardeArret(f"code cité ≠ liste fermée : manquants {sorted(set(attendus) - set(cites))}, "
                         f"en trop {sorted(set(cites) - set(attendus))}")
    for chemin, sha in sorted(cites.items()):
        p = Path(racine_code) / chemin
        if not p.is_file() or empreinte(p) != sha:
            raise GardeArret(f"{chemin} : empreinte ≠ empreinte citée par l'addendum")
    m = citation_constantes.search(texte)
    if m is None or m.group(1) != empreinte_attendue:
        raise GardeArret("constantes gelées ≠ empreinte citée par l'addendum")
    return {"fichiers": cites, "constantes": m.group(1)}


def exiger_code_cite(texte: str, racine_code: Path = RACINE_CODE) -> dict:
    return exiger_code_cite_sous(texte, K8.TITRE_LISTE, set(FICHIERS_PAQUET) | set(FICHIERS_ESSAIS) | set(FICHIERS_REUTILISES),
                                 CITATION_CONSTANTES, K8.empreinte_constantes(), racine_code)


def exiger_premier_passage_sous(racine: Path, addendum_rel: str, sha_addendum: str, commande: str, texte: dict,
                                commandes_addendum=K8.COMMANDES_ADDENDUM, passages_v3: dict | None = None) -> dict:
    """K2, premier passage par liste close. Pour chaque manifeste sous `runs/` (octets lus) :
    - ne cite ni le texte (`texte["chemin"]` ou `texte["sha256"]` dans ses octets, règle des textes) ni l'addendum
      (chemin ou empreinte) : ignoré ;
    - illisible et cite l'un des deux : arrêt ;
    - cite l'addendum : sa commande est celle de ce code → arrêt (second passage) ; une commande sœur gelée
      (`commandes_addendum`) → toléré ; toute autre commande → arrêt ;
    - cite le texte sans l'addendum : toléré seulement si son run est dans `passages_v3` avec la même empreinte sha256
      du fichier `manifeste.json` (les trois manifestes de la course v3, gelés) ; sinon arrêt.
    Les tolérés sont comptés et écrits par nom. Chaque arrêt est un `PassageHorsListe` (code de fin 2) qui nomme le
    manifeste."""
    passages_v3 = K8.PASSAGES_V3 if passages_v3 is None else passages_v3
    lus, autres, anterieurs, toleres = 0, 0, 0, []
    for p in sorted((Path(racine) / "runs").glob("*/manifeste.json")):
        brut = p.read_bytes()
        lus += 1
        run = p.parent.name
        cite_addendum = sha_addendum.encode("ascii") in brut or addendum_rel.encode("utf-8") in brut
        cite_texte = texte["sha256"].encode("ascii") in brut or texte["chemin"].encode("utf-8") in brut
        if not (cite_addendum or cite_texte):
            continue
        try:
            m = json.loads(brut.decode("utf-8"))
        except ValueError:
            m = None
        if not isinstance(m, dict):
            raise PassageHorsListe(f"passage hors liste close : manifeste illisible {run} qui cite "
                                   f"{'l’addendum ' + addendum_rel if cite_addendum else 'le texte ' + texte['chemin']}"
                                   f" — nœud de Lazar")
        if cite_addendum:
            c = m.get("commande")
            if c == commande:
                raise PassageHorsListe(f"second passage : {run} a déjà été lancé sous l'addendum {addendum_rel} avec la "
                                       f"commande « {commande} » — nœud de Lazar")
            if c not in commandes_addendum:
                raise PassageHorsListe(f"passage hors liste close : {run} cite l'addendum {addendum_rel} avec une commande "
                                       f"hors des trois commandes gelées (« {c} ») — nœud de Lazar")
            autres += 1
            toleres.append(run)
            continue
        if passages_v3.get(run) != hashlib.sha256(brut).hexdigest():
            raise PassageHorsListe(f"passage hors liste close : {run} cite le texte {texte['chemin']} et n'est pas un des "
                                   f"trois manifestes gelés de la course v3 (run absent de la liste, ou empreinte du "
                                   f"manifeste ≠ empreinte gelée) — nœud de Lazar")
        anterieurs += 1
        toleres.append(run)
    return {"manifestes_lus": lus, "autres_analyses_sous_l_addendum": autres,
            "passages_anterieurs_du_texte_hors_addendum": anterieurs, "toleres": toleres}


# --------------------------------------------------------------------------------------------- point d'entrée
def analyser(racine, fiche: str, run_analyse: str, prereg: str | None, entropie: int | None = None,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    lien = addendum = None
    if prereg is not None:
        sha_p = exiger_prereg_scelle(racine / prereg)
        exiger_texte(prereg, sha_p, K8.TEXTE)
        L1.exiger_code_importe_sous(racine)
        cite_texte = L2.exiger_code_cite((racine / prereg).read_text(encoding="utf-8"))     # liste fermée v2 du texte
        sha_a = exiger_prereg_scelle(racine / K8.ADDENDUM)
        cite = exiger_code_cite((racine / K8.ADDENDUM).read_text(encoding="utf-8"))          # liste fermée v8, addendum
        attendue = K2.entropie_de(sha_p)
        if entropie is not None and int(entropie) != attendue:
            raise GardeArret(f"entropie {entropie} ≠ entropie dérivée de l'empreinte du préenregistrement scellé")
        entropie = attendue
        addendum = {"chemin": K8.ADDENDUM, "sha256": sha_a}
        lien = {"preenregistrement": prereg, "sha256": sha_p, "code_cite": cite_texte,
                "addendum": {**addendum, "code_cite": cite},
                "passages": exiger_premier_passage_sous(racine, K8.ADDENDUM, sha_a, K8.COMMANDE, K8.TEXTE),
                "versions": L1.exiger_versions()}
    elif entropie is None:
        raise GardeArret("mode non décisif : entropie explicite exigée")
    f, sha_f = lire_fiche(racine, fiche, scellee=prereg is not None)
    src = r1 = j3 = j8 = longueurs = reception = None
    if f["R1"] is not None:
        reception = exiger_reception_v4(racine, f["R1"]["resultat"]["chemin"])   # K1 : texte, table-comparee, provenance,
        src = charger_p3(racine)                                                 # avant tout chargeur (aucun .npz ouvert)
        longueurs = longueurs_textes(racine, src["tables"])
        r1 = charger_r1(racine, f["R1"], src["tables"])
        if f["R2"] is not None:
            j3 = charger_juge(racine, f["R2"]["juge3b"], src["tables"], "J3")
            if f["R2"]["juge8b"] is not None:
                j8 = charger_juge(racine, f["R2"]["juge8b"], src["tables"], "J8")
    config = {"fiche": fiche, "fiche_sha256": sha_f, "prereg_fournisseur": K.PREREG_FOURNISSEUR, "addendum": addendum,
              "constantes": K8.constantes_courantes(), "constantes_sha256": K8.empreinte_constantes()}
    chemin_m, manifeste = creer_manifeste(racine, run_analyse, config, list(K.CLES_GRAINES), entropie=int(entropie),
                                          decisif=prereg is not None,
                                          prereg=None if prereg is None else str(racine / prereg),
                                          autoriser_depot_sale=autoriser_depot_sale, commande=K8.COMMANDE)
    graines = manifeste["graines"]
    if any(int(g["entropie"]) != int(entropie) for g in graines.values()):
        raise GardeArret("graines du manifeste non dérivées de l'entropie exigée")
    resultat = {"version": K8.VERSION, "statut": "décisif" if prereg is not None else "non décisif (essai)",
                "lien_au_preenregistrement": lien, "entropie": str(entropie), "regle_entropie": K2.REGLE_ENTROPIE,
                "motif_R1": f["motif_R1"], "motif_R2": f["motif_R2"], "reception_v4": reception,
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
    chemin_j = ecrire_resultat(racine, chemin_m, K8.NOM_SORTIE, resultat)
    md = Path(chemin_j).with_suffix(".md")
    if md.exists():
        raise GardeArret(f"{md} existe déjà (R12)")
    md.write_text(L1.rendre(resultat, empreinte(chemin_j)), encoding="utf-8")
    sceller(md)
    lire_manifeste(chemin_m)
    return resultat


def _main(argv) -> int:
    ap = argparse.ArgumentParser(prog=K8.COMMANDE)
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
    except PassageHorsListe as e:
        print(f"ARRÊT (passage hors liste close) : {e}", file=sys.stderr)
        sys.exit(CODE_FIN_PASSAGE)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
