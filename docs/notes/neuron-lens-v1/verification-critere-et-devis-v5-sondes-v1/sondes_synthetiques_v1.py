"""Sondes synthétiques du programme de comparaison v3 (c8fc6203…), sans aucune pièce de `diag/` ni de `runs/`.

Les pièces du 18 sont remplacées par des dictionnaires inventés ; les empreintes de référence sont posées égales aux constantes du
programme (on appelle `comparer` directement, sans lire de fichier). But : vérifier ce que le programme fait et ne fait pas, à la
lecture du code, pour la vérification des versions 5 du critère et du devis. Aucune écriture hors de ce dossier.
"""
import copy
import importlib.util
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cmp3", ICI / "comparer_reajustement_v3.py")
cmp3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cmp3)
REF = cmp3.REFERENCES
H = "ab" * 32  # empreinte bien formée quelconque


def base(lentille="R", octets_egaux=False):
    diffs64 = {"mid": [0.05 + 0.001 * i for i in range(32)], "out": [0.04 + 0.001 * i for i in range(31 if lentille == "R" else 32)]}
    diffs32 = copy.deepcopy(diffs64)
    meta = {"lens": lentille, "model": "m", "docs": 932}
    ref = {"sha256": "11" * 32, "taille": 100, "finies": True, "diffs_float64": diffs64, "diffs": diffs32, "meta": meta,
           "n_docs": [466, 466], "next_doc": 932, "fichier": "f.pt", "debut_utc": "2026-11-18T18:03:15Z", "etape": f"ajustement-{lentille}"}
    neuf = copy.deepcopy(ref)
    neuf["debut_utc"] = "2026-11-20T10:00:00Z"
    if not octets_egaux:
        neuf["sha256"] = "22" * 32
        neuf["diffs_float64"]["mid"][0] += 1e-4
        neuf["diffs"]["mid"][0] += 1e-4
    config = {"ajustement": "a", "correctifs": ["c1", "c2"], "graines": "g", "modele": "m", "revision": "r", "corpus": "k",
              "commit_voisin": "v", "drowse": {"version": "6.1.4", "sha256": "w"}, "precision": "p", "lentilles": ["npR"]}
    mref = {"run_id": "ref", "commit": "5e5", "depot_propre": True, "config": config, "versions": {"python": "3.12.16", "torch": "2.14.1", "plateforme": "x"},
            "graines": {"t": {"entropie": "1"}}, "commande": "c18", "preenregistrement": {"chemin": "p"}}
    mneuf = copy.deepcopy(mref)
    mneuf["commit"] = "neuf"
    mneuf["commande"] = "c20"
    c = {"ref": ref, "neuf": neuf, "env_ref": {"run_id": "run18", "manifeste_sha256": REF["manifeste"]},
         "env_neuf": {"run_id": "run20", "manifeste_sha256": "33" * 32}, "mref": mref, "mneuf": mneuf, "lentille": lentille,
         "sha_pieces": {"ajustement_ref": REF[f"ajustement-{lentille}"], "ajustement_neuf": "44" * 32, "manifeste_ref": REF["manifeste"],
                        "manifeste_neuf": "33" * 32, "lanceur_neuf": "55" * 32},
         "commit_resultats": "n'importe quoi", "correctifs_ref": {"c1": H, "c2": H}, "correctifs_neuf": {"c1": H, "c2": H},
         "fref": REF["fonction"], "fneuf": REF["fonction"], "eref": None, "eneuf": None, "env_eneuf": None}
    if lentille == "R":
        mm = {str(k): [H, "cd" * 32] for k in range(31)}
        val = {"npR_notre_R": {str(k): 0.1 + 0.01 * k for k in range(28)}, "identite_notre_R": {str(k): 1.0 + 0.01 * k for k in range(28)}}
        c["eref"] = {"matrices_moities": mm, "valeurs": val}
        e2 = {"matrices_moities": copy.deepcopy(mm), "valeurs": copy.deepcopy(val)}
        if not octets_egaux:
            e2["matrices_moities"]["0"] = ["ef" * 32, "cd" * 32]
            e2["valeurs"]["npR_notre_R"]["0"] += 0.002
            e2["valeurs"]["identite_notre_R"]["0"] += 0.003
        c["eneuf"] = e2
        c["env_eneuf"] = {"run_id": "run20", "manifeste_sha256": "33" * 32, "resultat": e2}
        c["sha_pieces"]["export_ref"] = REF["export-R"]
        c["sha_pieces"]["export_neuf"] = "66" * 32
    return c


def jouer(nom, c, _t=False, **kw):
    try:
        r = cmp3.comparer(c, **kw)
        manques = [p["nom"] for p in r["preconditions"] if not p["tenu"]]
        print(f"{nom} : {r['mention']} | déclencheurs {r['declencheurs']} | audit_requis {r.get('audit_requis')} | manqués {manques}"
              + (f" | table manifestes {json.dumps(r['differences_des_manifestes_sans_critere'], ensure_ascii=False)}" if _t else ""))
    except Exception as ex:  # noqa: BLE001 — la sonde rapporte l'arrêt sur erreur
        print(f"{nom} : ARRÊT SUR ERREUR {type(ex).__name__}: {ex}")


print(f"programme v3, constantes : tolérance {cmp3.TOLERANCE}, cohérence {cmp3.COHERENCE_PALIER_1}, diffs {cmp3.DIFFS_PALIER_1}/{cmp3.DIFFS_PALIER_2}")
jouer("V0 témoin R, octets différents", base("R"))
jouer("V0b témoin S, octets différents", base("S"))
jouer("V0c témoin R, octets égaux", base("R", True))
c = base("R"); c["mneuf"]["depot_propre"] = False
jouer("V1 depot_propre faux", c)
c = base("R"); c["mneuf"]["graines"] = {"t": {"entropie": "2"}}; c["mneuf"]["preenregistrement"] = None
jouer("V2 graines du haut et préenregistrement changés", c)
c = base("R"); c["sha_pieces"]["lanceur_neuf"] = "77" * 32
jouer("V3 un autre lanceur neuf portant la même fonction", c)
c = base("R"); c["mneuf"]["versions"]["scipy"] = "1.0"
jouer("V4 clé neuve dans versions (un seul côté)", c)
c = base("R"); c["mneuf"]["versions"]["python"] = "3.12.17"
jouer("V4b valeur de versions changée (python)", c)
c = base("R"); c["neuf"]["diffs"]["mid"][3] += 2e-3
jouer("V5 diffs au-delà de 10⁻³ au deuxième palier", c)
c = base("R", True); c["eneuf"]["valeurs"]["npR_notre_R"]["5"] += 1e-7
jouer("V6 octets égaux, une série de R qui change de 10⁻⁷", c)
c = base("R"); c["eneuf"]["matrices_moities"]["0"] = c["eref"]["matrices_moities"]["0"]
jouer("V7 octets différents, 31 matrices égales sur 31 (audit_requis ?)", c)
c = base("R"); c["neuf"]["diffs_float64"]["mid"][0] = c["ref"]["diffs_float64"]["mid"][0] + 0.002
jouer("V8 « différente » (audit_requis ?)", c)
c = base("R", True)
jouer("V9 palier 1 (audit_requis ?)", c)
c = base("R"); c["mneuf"]["versions"] = ["torch"]
jouer("V10 versions en liste", c)
c = base("R"); c["mneuf"]["config"]["correctifs"] = [["c1"]]
jouer("V11 correctifs mal formés (liste de listes)", c)
c = base("R"); c["mneuf"]["config"] = ["x"]
jouer("V12 configuration en liste", c)
c = base("R"); c["env_eneuf"] = {"run_id": "run18", "manifeste_sha256": REF["manifeste"]}; c["sha_pieces"]["export_neuf"] = REF["export-R"]
jouer("V13 export du 18 passé comme export neuf", c)
c = base("R"); c["mneuf"]["config"]["lentilles"] = ["autre"]
jouer("V14 champ `lentilles` changé (ancre des séries)", c, _t=True)
c = base("R"); c["correctifs_neuf"] = None
jouer("V15 correctifs illisibles au commit neuf", c)
c = base("R"); c["fneuf"] = "88" * 32
jouer("V16 fonction du lanceur neuf modifiée", c)
c = base("R"); c["neuf"]["etape"] = "export"
jouer("V17 champ etape faux", c)
c = base("R"); c["eneuf"]["valeurs"]["npR_notre_R"] = {str(k + 1): 0.1 for k in range(28)}
jouer("V18 série décalée (couches 1 à 28)", c)
c = base("R"); c["eneuf"]["matrices_moities"] = {str(k + 1): [H, H] for k in range(31)}
jouer("V19 matrices décalées (couches 1 à 31)", c)
c = base("S"); c["sha_pieces"]["ajustement_ref"] = REF["ajustement-R"]
jouer("V20 S comparée à la pièce de référence de R", c)
