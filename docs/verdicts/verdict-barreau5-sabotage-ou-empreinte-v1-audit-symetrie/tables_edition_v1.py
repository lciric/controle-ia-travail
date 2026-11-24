"""Audit de symétrie (R4) du barreau 5, point 3 : tables d'édition de 20 actions tirées par famille (champ du coût seulement).

Tirage d'audit (écart déclaré : le texte ne fixe pas la clé) : pour la famille T<n> (n = 1 … 10), parmi les actions
éditables de `textes-distillation.jsonl` de la copie lue, dans l'ordre du fichier (épisode, puis pas), 20 indices tirés
sans remise par `numpy.random.default_rng(numpy.random.SeedSequence([ENTROPIE, n])).choice(N, 20, replace=False)`.

Pour chaque action tirée : coût d'origine relu par le lecteur gelé (`t06.cout.cout_action`) sur le texte d'origine (celui
du saboteur) ; valeurs de la table ; texte de chaque membre édité ; contrôles : saboteur = origine ; jumeau et
sur-saboteur = origine × 1/3 et × 3 ramenés à la grille de la famille (grille recalculée ici depuis les textes du tirage,
comparée à celle du résultat de la famille) ; log10 du rapport ; lecteur gelé relit la valeur de la table sur le texte
édité ; texte modifié seulement dans l'empan du nombre ; écriture (séparateur de milliers, signe décimal, suffixe « k »,
unité) ; autres champs de l'action identiques ; écritures propres à un sens. Aucun score, aucune activation.
Joué avec PYTHONPATH=<racine>/src (lecteur gelé du paquet).
"""
import hashlib
import json
import math
import re
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

import numpy as np

from controle_ia.barreau5_familles import edition_cout_v1 as ec
from controle_ia.barreau5_familles import lecture_v1 as le
from controle_ia.environnements.propositions import lire_action
from controle_ia.t06.cout import NOMBRE, cout_action, cout_lisible

BN = Path(sys.argv[1])
SORTIE = Path(sys.argv[2])
ENTROPIE = 46741009118464776202533721588817709894
TIRES = 20
DEPOT = Path("/home/user/controle-ia-travail")
COMMIT = "8c758785d2d618b3666e909aa206a503b4a9f77a"
BASE = (1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0)
CIBLE = math.log10(3.0)
SIGNES_DU_NOMBRE = set("0123456789.,    ")


def sha_fichier(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def mantisse(v: float) -> float:
    d = Decimal(repr(float(v)))
    return float(f"{float(d.scaleb(-d.adjusted())):.12g}")


def plus_proche(v: float, phi: float, grille) -> float:
    """Écrit ici, sans le module : v × φ ramené en logarithme à la valeur de grille la plus proche (égalité : la plus petite)."""
    lx = math.log10(v * phi)
    cands = sorted({float(Decimal(repr(m)).scaleb(e)) for e in range(math.floor(lx) - 1, math.floor(lx) + 2) for m in grille})
    return min(cands, key=lambda c: (round(abs(math.log10(c) - lx), 12), c))


def diff_empan(a: str, b: str) -> tuple[int, int, int]:
    """Préfixe commun, puis suffixe commun : rend (début, fin dans a, fin dans b)."""
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    j = 0
    while j < min(len(a), len(b)) - i and a[len(a) - 1 - j] == b[len(b) - 1 - j]:
        j += 1
    return i, len(a) - j, len(b) - j


def nombre_a(texte: str, pos: int):
    """Correspondance du motif gelé `NOMBRE` qui recouvre la position `pos` du texte."""
    for nb in NOMBRE.finditer(texte):
        if nb.start("n") <= pos <= nb.end("n"):
            return nb
    return None


def conventions(n: str) -> dict:
    sep = None
    for s in (",", " ", " ", " ", " "):
        if re.fullmatch(rf"\d{{1,3}}(?:{re.escape(s)}\d{{3}})+(?:[.,]\d+)?", n):
            sep = s
            break
    dec = None
    if sep == ",":
        dec = "." if "." in n else None
    elif "." in n or "," in n:
        reste = n.replace(sep, "") if sep else n
        dec = "," if "," in reste else ("." if "." in reste else None)
    chiffres_entiers = len(re.sub(r"\D", "", n.split(dec)[0] if dec else n))
    return {"sep": sep, "dec": dec, "chiffres_entiers": chiffres_entiers}


def main() -> None:
    texte_reg = subprocess.run(["git", "-C", str(DEPOT), "show", f"{COMMIT}:registres/barreau5-familles-jumelles-v1.md"],
                               capture_output=True, text=True, check=True).stdout
    relance = le.relance_du_registre(texte_reg)
    resume = json.loads((BN / "retenus/formation.json").read_text(encoding="utf-8"))["familles"]
    total = {"actions": 0, "saboteur_egal_origine": 0, "origine_relue_egale_table": 0, "jumeau_sur_grille_recalculee": 0,
             "sur_sur_grille_recalculee": 0, "jumeau_egal_module": 0, "sur_egal_module": 0,
             "lecteur_relit_jumeau": 0, "lecteur_relit_sur": 0, "empan_seulement_nombre": 0, "conventions_gardees": 0,
             "suffixe_k_et_unite_en_place": 0, "autres_champs_identiques": 0, "operation_numero_identiques": 0,
             "jumeau_log10_dans_0_08": 0, "sur_log10_dans_0_08": 0}
    propres = {"quatre_chiffres_nes_de_trois_sur": 0, "quatre_chiffres_nes_de_trois_jumeau": 0,
               "decimales_perdues_jumeau": 0, "decimales_perdues_sur": 0, "arrondi_inegal": 0,
               "au_moins_une": 0, "accord_drapeaux_table": 0, "decimales_ajoutees_jumeau": 0,
               "decimales_ajoutees_sur": 0, "au_moins_une_ajoutees_comprises": 0}
    par_famille = {}
    lr_j, lr_s = [], []
    exemples = []
    deja = set()
    grilles_ok = 0
    fichiers_ok = 0
    for n_fam, f in enumerate(le.TENUES, start=1):
        n = le.instance_de(f)
        suffixe = "-x1" if relance and n in relance else ""
        prefixe = le.prefixe_de_copie(f, relance)
        marche = [p for p in (BN / "formation/donnees").glob(f"*-b5f-formation-{n}{suffixe}") if p.is_dir()]
        assert len(marche) == 1
        dossier = [d for d in (marche[0] / prefixe, marche[0] / f"{prefixe}-r1") if d.is_dir()]
        assert len(dossier) == 1
        dossier = dossier[0]
        fichier = dossier / "textes-distillation.jsonl"
        diag = json.loads((BN / "formation/diag" / marche[0].name / f"famille-{prefixe}.json").read_text(encoding="utf-8"))
        tirage = diag["resultat"]["tirages"][-1]
        s = sha_fichier(fichier)
        fichiers_ok += (s == (dossier / "textes-distillation.jsonl.sha256").read_text().split()[0]
                        and s == tirage["textes_sha256"])
        episodes = [json.loads(x) for x in fichier.read_bytes().decode("utf-8").split("\n") if x.strip()]
        couts = [cout_action(t)["cout"] for ep in episodes for t in ep["textes"]]
        grille = tuple(sorted({float(f"{m:.12g}") for m in BASE} | {mantisse(c) for c in couts if cout_lisible(c)}))
        grilles_ok += list(grille) == [float(x) for x in tirage["grille"]]
        editables = [(e, p) for e, ep in enumerate(episodes) for p, a in enumerate(ep["edition"]["actions"]) if a["editable"]]
        rng = np.random.default_rng(np.random.SeedSequence([ENTROPIE, n_fam]))
        idx = rng.choice(len(editables), size=TIRES, replace=False)
        pf = {"editables": len(editables), "editables_egal_resume": resume[f]["actions_editees"] == len(editables), "actions": 0, "propres": {k: 0 for k in propres}, "controles_manques": 0}
        for i in idx:
            e, p = editables[int(i)]
            ep = episodes[e]
            a = ep["edition"]["actions"][p]
            assert a["pas"] == p
            texte = ep["textes"][p]
            total["actions"] += 1
            pf["actions"] += 1
            ok = True
            o = cout_action(texte)["cout"]
            total["origine_relue_egale_table"] += o == a["valeur_origine"]
            total["saboteur_egal_origine"] += a["valeurs"]["saboteur"] == o and "saboteur" not in a["textes"]
            ok &= a["valeurs"]["saboteur"] == o
            ecr = {}
            for m, phi, cle in (("jumeau", 1 / 3, "jumeau"), ("sur_saboteur", 3.0, "sur")):
                v = a["valeurs"][m]
                total[f"{cle}_sur_grille_recalculee"] += v == plus_proche(o, phi, grille)
                total[f"{cle}_egal_module"] += v == ec.valeur_sur_grille(o, phi, grille)
                lr = math.log10(v / o)
                (lr_j if m == "jumeau" else lr_s).append(lr)
                total[f"{cle}_log10_dans_0_08"] += abs(abs(lr) - CIBLE) <= 0.08 and (lr < 0) == (m == "jumeau")
                te = a["textes"][m]
                c = cout_action(te)
                relit = cout_lisible(c["cout"]) and abs(c["cout"] - v) <= 1e-9 * max(1.0, v)
                total[f"lecteur_relit_{cle}"] += relit
                d, fa, fb = diff_empan(texte, te)
                vieux, neuf = texte[d:fa], te[d:fb]
                seul = set(vieux) <= SIGNES_DU_NOMBRE and set(neuf) <= SIGNES_DU_NOMBRE
                nb0, nb1 = nombre_a(texte, d), nombre_a(te, d)
                seul &= nb0 is not None and nb1 is not None and nb0.start("n") == nb1.start("n")
                total["empan_seulement_nombre"] += seul
                if seul:
                    n0, n1 = nb0["n"], nb1["n"]
                    k0, k1 = nb0["k"], nb1["k"]
                    total["suffixe_k_et_unite_en_place"] += (bool(k0) == bool(k1)
                                                             and texte[nb0.end():] == te[nb1.end():])
                    c0, c1 = conventions(n0), conventions(n1)
                    garde = True
                    if c0["sep"] and c1["chiffres_entiers"] >= 4:
                        garde &= c1["sep"] == c0["sep"]
                    if not c0["sep"]:
                        garde &= c1["sep"] is None
                    if c0["dec"] and c1["dec"]:
                        garde &= c1["dec"] == c0["dec"]
                    # décimales ajoutées à un nombre entier (grille aux mantisses longues) : comptées à part, hors des
                    # conventions que le texte nomme (séparateur, signe décimal, suffixe « k », unité)
                    ajoutees = c0["dec"] is None and c1["dec"] is not None
                    total["conventions_gardees"] += garde
                    quatre = c0["sep"] is None and not k0 and c0["chiffres_entiers"] == 3 and c1["chiffres_entiers"] >= 4
                    perdues = c0["dec"] is not None and c1["dec"] is None
                    ecr[m] = {"quatre": quatre, "perdues": perdues, "ajoutees": ajoutees, "vieux": n0 + (k0 or ""), "neuf": n1 + (k1 or "")}
                    ok &= garde
                else:
                    ok = False
                a0, a1 = lire_action(texte), lire_action(te)
                total["operation_numero_identiques"] += (a0.operation, a0.numero) == (a1.operation, a1.numero)
                autres = ({k: x for k, x in a0.champs.items() if k != "COST"} == {k: x for k, x in a1.champs.items()
                                                                                   if k != "COST"})
                total["autres_champs_identiques"] += autres
                ok &= relit and autres
            # écritures propres à un sens
            lj, ls = math.log10(a["valeurs"]["jumeau"] / o), math.log10(a["valeurs"]["sur_saboteur"] / o)
            inegal = abs(lj + ls) > 1e-6
            fl = {"quatre_chiffres_nes_de_trois_sur": ecr.get("sur_saboteur", {}).get("quatre", False),
                  "quatre_chiffres_nes_de_trois_jumeau": ecr.get("jumeau", {}).get("quatre", False),
                  "decimales_perdues_jumeau": ecr.get("jumeau", {}).get("perdues", False),
                  "decimales_perdues_sur": ecr.get("sur_saboteur", {}).get("perdues", False),
                  "arrondi_inegal": inegal}
            fl["au_moins_une"] = any(fl.values())
            fl["decimales_ajoutees_jumeau"] = ecr.get("jumeau", {}).get("ajoutees", False)
            fl["decimales_ajoutees_sur"] = ecr.get("sur_saboteur", {}).get("ajoutees", False)
            fl["au_moins_une_ajoutees_comprises"] = fl["au_moins_une"] or fl["decimales_ajoutees_jumeau"] or \
                fl["decimales_ajoutees_sur"]
            table_fl = {m: a["ecritures"].get(m, {}) for m in ("jumeau", "sur_saboteur")}
            accord = (bool(table_fl["sur_saboteur"].get("milliers_sans_separateur")) == fl["quatre_chiffres_nes_de_trois_sur"]
                      and bool(table_fl["jumeau"].get("milliers_sans_separateur")) == fl["quatre_chiffres_nes_de_trois_jumeau"]
                      and bool(table_fl["jumeau"].get("decimales_perdues")) == fl["decimales_perdues_jumeau"]
                      and bool(table_fl["sur_saboteur"].get("decimales_perdues")) == fl["decimales_perdues_sur"])
            fl["accord_drapeaux_table"] = accord
            for k, x in fl.items():
                propres[k] += bool(x)
                pf["propres"][k] += bool(x)
            pf["controles_manques"] += not ok
            genre = next((g for g in ("quatre_chiffres_nes_de_trois_sur", "decimales_ajoutees_jumeau", "arrondi_inegal")
                          if fl[g] and g not in deja), None)
            if genre is not None and len(exemples) < 3 and "jumeau" in ecr and "sur_saboteur" in ecr:
                deja.add(genre)
                exemples.append({"origine": ecr["jumeau"]["vieux"], "jumeau": ecr["jumeau"]["neuf"],
                                 "sur_saboteur": ecr["sur_saboteur"]["neuf"],
                                 "log10_jumeau": round(lj, 3), "log10_sur": round(ls, 3),
                                 "traces": [k for k, x in fl.items() if x and not k.startswith("au_moins")
                                            and k != "accord_drapeaux_table"]})
        par_famille[f"famille {n_fam:02d}"] = pf
    r = {"regle_du_tirage": "default_rng(SeedSequence([46741009118464776202533721588817709894, n])).choice(N_editables, 20, "
                             "replace=False), n = numéro de la famille, actions éditables dans l'ordre du fichier",
         "fichiers_textes_egaux_compagnon_et_resultat": fichiers_ok, "grilles_recalculees_egales": grilles_ok,
         "comptes": total, "ecritures_propres_a_un_sens": propres, "par_famille": par_famille,
         "log10_jumeau": {"min": min(lr_j), "mediane": float(np.median(lr_j)), "max": max(lr_j)},
         "log10_sur": {"min": min(lr_s), "mediane": float(np.median(lr_s)), "max": max(lr_s)},
         "exemples": exemples}
    SORTIE.write_text(json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
