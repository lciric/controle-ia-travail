"""Sonde du concepteur pour le brouillon 4 du préenregistrement du pilote « oracles plantés ».

Nature : sonde d'instrument (classe B, à vérifier par le contre-lecteur du code avant d'être citée dans un texte
scellé). Processeur seul, aucun appel de modèle, aucun réseau, 0 USD. **Racines d'essai seulement** (0 à 39 et
20261122 : 41 racines distinctes ; la racine 11 figure deux fois dans `v6-aires.json`) : aucune banque réelle, aucune
clé réelle. Code sondé : `src/controle_ia/oracles_plantes_v6/` (commit 35ac9e10738ccaac486ec9b9684fe70441f6371a),
importé tel quel, non modifié.

Ce que la sonde mesure, sur chaque racine d'essai :

1. **Plancher « instances aveugles »** de la lecture de H3 par contre-exemples vérifiés. Règle écrite AVANT le premier
   lancement de cette sonde, sans regarder aucun taux : pour tout énoncé, sans l'évaluer, avancer au plus trois
   instances ; dans la k-ième, chaque variable NAT du préfixe universel de tête vaut a_k, avec (a_1, a_2, a_3) =
   (B, 1, N + 1), B = 3N le plafond de vérification ; chaque variable à domaine borné (intervalle ou domaine nommé)
   prend la plus petite valeur de son domaine, évalué sous les variables précédentes ; une instance dont un domaine est
   vide ou non évaluable est abandonnée ; les doublons sont retirés. Une instance « touche » si `verifier_instance`
   (le chemin de T6) la rend « verifie » au plafond 3N. Compté sur les 96 faux de la banque (48 faux tôt, 48 pièges) et
   sur les 75 faux de la sous-banque servie aux bras S et N (rôle « analyse »), par strate et par gabarit ; contrôle :
   aucune touche sur les vérités.
2. **Textes de vérités répétés d'un monde à l'autre** (écart 16 contre 17 relevé par la contre-lecture du brouillon 3).
3. **Précision de la base « grammaire aléatoire »** (24 énoncés par monde, enfant [9]) : vivantes, vraies-bornées, non
   triviales et non redites (T5 contre les vivantes antérieures de la base dans le même monde), sur les valides.

Lancer depuis la racine du dépôt :
  PYTHONPATH=src python -I prereg/mathematiques-nouvelles-v1/calculs-v4/sonde_instances_aveugles_v1.py \
      prereg/mathematiques-nouvelles-v1/calculs-v4/sonde-instances-aveugles-v1.json \
      > prereg/mathematiques-nouvelles-v1/calculs-v4/sortie-sonde-instances-aveugles-v1.txt
(`-I` ignore PYTHONPATH : donner alors le chemin par `sys.path`, voir la fin du fichier.)
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from controle_ia.oracles_plantes_v6 import banque, parametres  # noqa: E402
from controle_ia.oracles_plantes_v6.base_aleatoire import tirer_base  # noqa: E402
from controle_ia.oracles_plantes_v6.evaluation import prefixe  # noqa: E402
from controle_ia.oracles_plantes_v6.exact import HorsCapacite, Indefini  # noqa: E402
from controle_ia.oracles_plantes_v6.forme_seule import regle_forme_seule  # noqa: E402
from controle_ia.oracles_plantes_v6.graines import generateur  # noqa: E402
from controle_ia.oracles_plantes_v6.sous_banque import identifiants_opaques, tirer_sous_banque  # noqa: E402
from controle_ia.oracles_plantes_v6.tests_de_mort import appliquer_batterie, sortie_de_texte, verifier_instance  # noqa: E402

RACINES = list(range(40)) + [20261122]          # 41 racines d'essai distinctes
NOMS = ("B", "1", "N+1")


def instances_aveugles(monde, arbre) -> list[tuple[str, dict]]:
    """Au plus trois instances, sans évaluer l'énoncé (règle de l'en-tête)."""
    pre, _ = prefixe(arbre)
    sortie, vues = [], []
    for nom, a in zip(NOMS, (monde.borne_verification(), 1, monde.N + 1)):
        env, inst, ok = {}, {}, True
        for var, dom in pre:
            if dom[0] == "NAT":
                x = a
            else:
                try:
                    vals = monde.ev.valeurs_domaine(dom, env, borne=None)
                except (Indefini, HorsCapacite):
                    ok = False
                    break
                if len(vals) == 0:
                    ok = False
                    break
                x = vals[0]
            inst[var] = int(x)
            env[var] = Fraction(int(x))
        if ok and inst not in vues:
            vues.append(inst)
            sortie.append((nom, inst))
    return sortie


def touches(monde, texte: str) -> dict:
    """Pour un énoncé : quelles instances aveugles sont vérifiées exactement (chemin de T6, plafond 3N)."""
    arbre = monde.analyser(texte)
    r = {n: False for n in NOMS}
    for nom, inst in instances_aveugles(monde, arbre):
        statut, _ = verifier_instance(arbre, monde, inst, monde.borne_verification())
        r[nom] = statut == "verifie"
    r["une_au_moins"] = any(r[n] for n in NOMS)
    r["forme_seuil"] = bool(regle_forme_seule(arbre))
    return r


def ajouter(compte: dict, cle, t: dict):
    c = compte.setdefault(cle, {"n": 0, "une_au_moins": 0, "B": 0, "1": 0, "N+1": 0})
    c["n"] += 1
    for k in ("une_au_moins",) + NOMS:
        c[k] += int(t[k])


def sonder(racine: int, params: dict) -> dict:
    bq = banque.construire_banque(racine, params)
    ids = identifiants_opaques(generateur(racine, 3, 0), len(bq), "monde-")
    monde_de = {i: m for i, (m, _pl) in zip(ids, bq)}
    # 1a. banque entière
    b_strate, b_gabarit, verites_touchees = {}, {}, 0
    for m, plantes in bq:
        for p in plantes:
            if p.etiquette == "VERITE_PLANTEE":
                verites_touchees += int(touches(m, p.texte)["une_au_moins"])
            elif p.etiquette in ("FAUX_TOT", "PIEGE"):
                t = touches(m, p.texte)
                ajouter(b_strate, p.etiquette, t)
                ajouter(b_strate, p.etiquette + ("/seuil" if t["forme_seuil"] else "/non-seuil"), t)
                ajouter(b_gabarit, f"{m.famille}/{p.etiquette}/{p.gabarit}", t)
    # 1b. sous-banque servie aux bras S et N (items analysés, premier service)
    servie, cle = tirer_sous_banque(bq, ids, racine, params["sous_banque"])
    enonce = {x["identifiant"]: x["enonce"] for x in servie["items"]}
    s_strate = {}
    for it in cle["items"]:
        if it["role"] != "analyse" or it["etiquette"] not in ("FAUX_TOT", "PIEGE"):
            continue
        t = touches(monde_de[it["identifiant_monde"]], enonce[it["identifiant"]])
        ajouter(s_strate, it["etiquette"], t)
        ajouter(s_strate, "FAUX (75)", t)
    # 2. textes identiques entre mondes
    mondes_du_texte = {}
    for w, (_m, plantes) in enumerate(bq):
        for p in plantes:
            mondes_du_texte.setdefault((p.etiquette, p.texte), set()).add(w)
    repetes = {}
    for (et, _t), ws in mondes_du_texte.items():
        if len(ws) > 1:
            repetes[et] = repetes.get(et, 0) + 1
    # 3. base « grammaire aléatoire »
    base = {"enonces": 0, "valides": 0, "vivantes": 0, "vvnt": 0, "vvnt_non_redites": 0}
    for m, _pl in bq:
        anterieures = []
        for texte in tirer_base(generateur(racine, 9, m.indice), m, params["base_aleatoire"]):
            r = appliquer_batterie(sortie_de_texte(texte), m, anterieures=anterieures)
            base["enonces"] += 1
            if r.statut == "informe":
                continue
            base["valides"] += 1
            if r.statut == "vivante":
                base["vivantes"] += 1
                ok = r.vraie_bornee and not r.triviale
                base["vvnt"] += int(ok)
                base["vvnt_non_redites"] += int(ok and not r.redite)
                anterieures.append(r.forme)
    return {"racine": racine, "banque_par_strate": b_strate, "banque_par_gabarit": b_gabarit,
            "verites_touchees": verites_touchees, "sous_banque_par_strate": s_strate,
            "textes_repetes_entre_mondes": repetes, "base_grammaire_aleatoire": base}


def taux(c: dict, k: str = "une_au_moins") -> str:
    return f"{c[k]}/{c['n']} = {c[k] / c['n']:.3f}" if c["n"] else "—"


def main(chemin_json: str | None) -> int:
    params, sha_params = parametres.charger()
    print("Sonde « instances aveugles » — racines d'essai seulement — code oracles_plantes_v6 (35ac9e10…)")
    print(f"paramètres : parametres_v6.json sha256 {sha_params}")
    print(f"règle : au plus trois instances par énoncé, variables NAT à (B = 3N, 1, N + 1), domaines bornés à leur "
          f"plus petite valeur ; aucune évaluation de l'énoncé")
    print()
    resultats = []
    for r in RACINES:
        x = sonder(r, params)
        resultats.append(x)
        sb, bs, ba = x["sous_banque_par_strate"], x["banque_par_strate"], x["base_grammaire_aleatoire"]
        print(f"racine {r:>8} | sous-banque, 75 faux : {taux(sb['FAUX (75)'])} "
              f"(faux tôt {taux(sb['FAUX_TOT'])} ; pièges {taux(sb['PIEGE'])}) | banque, 96 faux : "
              f"faux tôt {taux(bs['FAUX_TOT'])} ; pièges {taux(bs['PIEGE'])} | vérités touchées {x['verites_touchees']} "
              f"| vérités répétées {x['textes_repetes_entre_mondes'].get('VERITE_PLANTEE', 0)} "
              f"| base : {ba['vvnt_non_redites']}/{ba['valides']} = {ba['vvnt_non_redites'] / ba['valides']:.3f}",
              flush=True)
    print()
    # synthèse
    sbt = [x["sous_banque_par_strate"]["FAUX (75)"]["une_au_moins"] / x["sous_banque_par_strate"]["FAUX (75)"]["n"]
           for x in resultats]
    print(f"Synthèse sur {len(resultats)} racines d'essai distinctes")
    print(f"  plancher aveugle sur les 75 faux de la sous-banque : min {min(sbt):.3f}, médiane "
          f"{sorted(sbt)[len(sbt) // 2]:.3f}, max {max(sbt):.3f}")
    for strate in ("FAUX_TOT", "PIEGE"):
        v = [x["sous_banque_par_strate"][strate]["une_au_moins"] / x["sous_banque_par_strate"][strate]["n"]
             for x in resultats]
        print(f"    dont {strate} : min {min(v):.3f}, médiane {sorted(v)[len(v) // 2]:.3f}, max {max(v):.3f}")
    cumul = {}
    for x in resultats:
        for k, c in x["banque_par_strate"].items():
            d = cumul.setdefault(k, {"n": 0, "une_au_moins": 0, "B": 0, "1": 0, "N+1": 0})
            for kk in d:
                d[kk] += c[kk]
    print("  banque entière, cumul des racines, par strate (une au moins ; par B ; par 1 ; par N + 1) :")
    for k in sorted(cumul):
        c = cumul[k]
        print(f"    {k:22s} {taux(c)} ; B {taux(c, 'B')} ; 1 {taux(c, '1')} ; N+1 {taux(c, 'N+1')}")
    cumul_g = {}
    for x in resultats:
        for k, c in x["banque_par_gabarit"].items():
            d = cumul_g.setdefault(k, {"n": 0, "une_au_moins": 0, "B": 0, "1": 0, "N+1": 0})
            for kk in d:
                d[kk] += c[kk]
    print("  banque entière, cumul des racines, par gabarit :")
    for k in sorted(cumul_g):
        print(f"    {k:55s} {taux(cumul_g[k])}")
    print(f"  vérités touchées (doit être 0) : {sum(x['verites_touchees'] for x in resultats)}")
    rep = [x["textes_repetes_entre_mondes"].get("VERITE_PLANTEE", 0) for x in resultats]
    print(f"  textes de vérités répétés d'un monde à l'autre : min {min(rep)}, max {max(rep)} ; "
          f"répartition {dict(sorted((v, rep.count(v)) for v in set(rep)))}")
    repp = [x["textes_repetes_entre_mondes"].get("PIEGE", 0) for x in resultats]
    print(f"  textes de pièges répétés : max {max(repp)}")
    bp = [x["base_grammaire_aleatoire"]["vvnt_non_redites"] / x["base_grammaire_aleatoire"]["valides"]
          for x in resultats]
    bp0 = [x["base_grammaire_aleatoire"]["vvnt"] / x["base_grammaire_aleatoire"]["valides"] for x in resultats]
    print(f"  précision de la base « grammaire aléatoire » (non redites) : min {min(bp):.3f}, médiane "
          f"{sorted(bp)[len(bp) // 2]:.3f}, max {max(bp):.3f} ; sans la condition de redite : min {min(bp0):.3f}, "
          f"max {max(bp0):.3f}")
    if chemin_json:
        Path(chemin_json).write_text(json.dumps(resultats, ensure_ascii=False, sort_keys=True, indent=1) + "\n",
                                     encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
