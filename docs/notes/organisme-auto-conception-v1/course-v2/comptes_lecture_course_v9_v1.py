"""Comptes descriptifs de la course d'auto-conception v9 de l'organisme d'idéation (lecture de la mère, v1).

Gouverné par le préenregistrement v2 de la course (0d51e0b3…), sections « Métrique », « Plan d'analyse »,
« Critères de lecture gelés ». Processeur seul, aucun appel extérieur, aucune dépense.

Deux étapes, jouées dans cet ordre et écrites chacune avant la suivante :
  --etape audit    audit de symétrie (R4) sur les champs seuls (passeports, items des juges, redites, notables),
                   sans lire le contenu des cartes ;
  --etape comptes  comptes de la « Métrique » ; part des cartes dont le voisin cite un identifiant qui existe
                   dans la matière v3, par ID_CATALOGUE et controles_statiques du programme d'épreuve v2,
                   importés (non recopiés) ; répartition par axe, valeurs telles quelles.

Usage : python3 -I -B comptes_lecture_course_v9_v1.py --racine ARBRE --matiere MATIERE_V3 --etape audit|comptes --sortie F.json
"""
from __future__ import annotations

import argparse
import collections
import glob
import hashlib
import importlib.util
import json
import os
import re
import sys

RUN = "runs/20261119-094145-course-auto-conception-v9"
A = "archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie"
G = A + "/generation-1"
# Empreintes données par le mandat (préfixes de 8 caractères) : vérifiées avant toute lecture.
EMPREINTES = {
    "docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md": "0d51e0b3",
    RUN + "/manifeste-lanceur-fin.json": "28bc36df",
    A + "/bilan-course.json": "b88bfcb9",
    G + "/manifeste-fin.json": "d3548fed",
    G + "/fiches.json": "ba65c411",
    G + "/aiguillage/journal-aiguillage.json": "e2ba2a33",
    G + "/classement.json": "fa6ee4a0",
    G + "/memoire.json": "f018b701",
    G + "/consommations.json": "a8a58571",
    G + "/empreintes-sortie.txt": "522c83a9",
    "scripts/epreuve_temoins_auto_conception_v2.py": "19d03876",
}
MATIERE_SHA = "11f4b69ba42147c428090e4805948a708d0ed266da0c0cd07f194723eaba742d"
ITEMS = ["module_nomme", "voisin_nomme", "epreuve_plantee", "aucun_modele_ne_decide", "reserves_tenues"]
JUGES = ["juge-opus", "juge-argon"]
ETIQUETTES_A4 = ["Opus", "Fable", "Argon", "Astra", "Kimi", "Carbon"]  # configuration v5, « etiquettes_interdites_fixes »


def sha(chemin: str) -> str:
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def verifier(racine: str) -> dict:
    vu = {}
    for rel, pref in EMPREINTES.items():
        h = sha(os.path.join(racine, rel))
        if not h.startswith(pref):
            raise SystemExit(f"ARRÊT : empreinte de {rel} = {h}, attendue {pref}…")
        vu[rel] = h
    # les 94 verdicts, contre la liste d'empreintes de la sortie
    liste = {}
    with open(os.path.join(racine, G, "empreintes-sortie.txt"), encoding="utf-8") as f:
        for ligne in f:
            h, nom = ligne.rstrip("\n").split("  ", 1)
            liste[nom] = h
    fichiers = sorted(glob.glob(os.path.join(racine, G, "coffre", "verdicts-passe1-*.json")))
    for p in fichiers:
        nom = "coffre/" + os.path.basename(p)
        if liste.get(nom) != sha(p):
            raise SystemExit(f"ARRÊT : verdict {nom} hors de la liste d'empreintes")
    vu["verdicts_passe1_verifies"] = len(fichiers)
    return vu


def lot_de(fiche: dict) -> str:
    tete = fiche["meta"]["case"][0].split("\n", 1)[0]
    m = re.match(r"Lot (\d+) sur 11 du catalogue des mécanismes publiés : (.*?) \(catalogue sha256", tete)
    return f"{int(m.group(1)):02d} {m.group(2)}" if m else "inconnu"


def charger(racine: str) -> dict:
    j = lambda rel: json.load(open(os.path.join(racine, rel), encoding="utf-8"))
    verdicts = {}
    for p in sorted(glob.glob(os.path.join(racine, G, "coffre", "verdicts-passe1-*.json"))):
        v = json.load(open(p, encoding="utf-8"))
        verdicts[v["ident"]] = v
    return {"fiches": j(G + "/fiches.json"), "aiguillage": j(G + "/aiguillage/journal-aiguillage.json"),
            "classement": j(G + "/classement.json"), "memoire": j(G + "/memoire.json"),
            "consommations": j(G + "/consommations.json"), "verdicts": verdicts,
            "manifeste_fin": j(G + "/manifeste-fin.json"), "manifeste_lanceur_fin": j(RUN + "/manifeste-lanceur-fin.json"),
            "bilan": j(A + "/bilan-course.json")}


def tout_vrai(v: dict) -> bool:
    return all(v["verdicts"][jg]["items"][i] is True for jg in JUGES for i in ITEMS)


def audit(d: dict) -> dict:
    """Champs seuls : classe de l'aiguilleur, items des juges, notable, redites. Aucun champ de contenu n'est lu."""
    fiches, verdicts, aig = d["fiches"], d["verdicts"], d["aiguillage"]
    notable = {l["ident"]: l["notable"] for l in d["classement"]["lignes"]}
    redites = d["memoire"]["redites"]
    retenues = aig["retenues"]
    rendues = len(fiches) + len(retenues)

    def bloc(idents: list, n_retenues: int, n_redites: int) -> dict:
        tous_items = all(tout_vrai(verdicts[i]) for i in idents) if idents else False
        n_not = sum(bool(notable.get(i)) for i in idents)
        propre = (n_retenues == 0) and tous_items and n_redites == 0 and len(idents) > 0
        return {"cartes_rendues": len(idents) + n_retenues, "passeports": len(idents), "retenues": n_retenues,
                "tous_items_vrais_chez_les_deux_juges": tous_items,
                "cartes_tous_items_vrais": sum(tout_vrai(verdicts[i]) for i in idents),
                "redites": n_redites, "notables": n_not, "trop_propre": propre, "trop_sale": n_not == 0}

    sortie = {"niveau_lot_de_la_generation": bloc(list(fiches), len(retenues), len(redites))}
    par_case = collections.defaultdict(list)
    for i, f in fiches.items():
        par_case[lot_de(f)].append(i)
    # les deux retenues ne portent pas de case au journal : comptées au niveau de la génération seulement
    sortie["niveau_case_du_catalogue"] = {c: bloc(ids, 0, 0) for c, ids in sorted(par_case.items())}
    sortie["note_case"] = ("au niveau de la case, les deux cartes retenues (journal de l'aiguilleur, sans case) ne sont pas "
                           "rattachées ; aucune redite n'existe à aucun niveau (memoire.redites vide)")
    # contrôles de l'audit (R4), mêmes contrôles quel que soit le sens de l'alerte
    ctrl = {}
    ctrl["juges_items_vrais_par_item"] = {jg: {it: sum(v["verdicts"][jg]["items"][it] is True for v in verdicts.values())
                                               for it in ITEMS} for jg in JUGES}
    ctrl["juges_notables"] = {jg: sum(v["verdicts"][jg]["notable"] is True for v in verdicts.values()) for jg in JUGES}
    ctrl["items_non_booleens"] = sum(not isinstance(v["verdicts"][jg]["items"][it], bool)
                                     for v in verdicts.values() for jg in JUGES for it in ITEMS)
    ctrl["notes_vides"] = {jg: sum(not v["verdicts"][jg].get("note", "").strip() for v in verdicts.values()) for jg in JUGES}
    ctrl["accord_des_juges_par_item"] = {it: sum(v["verdicts"]["juge-opus"]["items"][it] == v["verdicts"]["juge-argon"]["items"][it]
                                                 for v in verdicts.values()) for it in ITEMS}
    ctrl["notable_du_juge_egal_cinq_items"] = {jg: sum(v["verdicts"][jg]["notable"] == all(v["verdicts"][jg]["items"][i] for i in ITEMS)
                                                       for v in verdicts.values()) for jg in JUGES}
    ctrl["classement_notable_egal_unanimite"] = sum(notable[i] == all(verdicts[i]["verdicts"][jg]["notable"] for jg in JUGES)
                                                    for i in fiches)
    ctrl["empreinte_verdict_egale_empreinte_carte"] = sum(verdicts[i]["empreinte"] == fiches[i]["empreinte"] for i in fiches)
    ctrl["verdicts_sans_carte"] = sorted(set(verdicts) - set(fiches))
    ctrl["cartes_sans_verdict"] = sorted(set(fiches) - set(verdicts))
    # audit déclenché (R4) par toute case « trop propre » ou « trop sale » : mêmes contrôles dans les deux sens
    from math import comb
    n_tot, n_not = len(fiches), sum(bool(notable.get(i)) for i in fiches)
    alertes = {}
    esperance_propres = 0.0
    for c, ids in sorted(par_case.items()):
        k = len(ids)
        p_propre = comb(n_not, k) / comb(n_tot, k)
        p_sale = comb(n_tot - n_not, k) / comb(n_tot, k)
        esperance_propres += p_propre
        b = sortie["niveau_case_du_catalogue"][c]
        if b["trop_propre"] or b["trop_sale"]:
            alertes[c] = {"sens": "trop_propre" if b["trop_propre"] else "trop_sale",
                          "especes": dict(sorted(collections.Counter(fiches[i]["meta"]["proposeur"] for i in ids).items())),
                          "probabilite_hypergeometrique_tout_notable": round(p_propre, 4),
                          "probabilite_hypergeometrique_aucun_notable": round(p_sale, 6),
                          "longueur_des_notes_des_juges_min_max": {jg: [min(len(verdicts[i]["verdicts"][jg]["note"]) for i in ids),
                                                                        max(len(verdicts[i]["verdicts"][jg]["note"]) for i in ids)]
                                                                   for jg in JUGES},
                          "longueur_des_notes_des_juges_ailleurs_min_max": {jg: [min(len(verdicts[i]["verdicts"][jg]["note"]) for i in fiches if i not in ids),
                                                                                 max(len(verdicts[i]["verdicts"][jg]["note"]) for i in fiches if i not in ids)]
                                                                            for jg in JUGES},
                          "longueur_des_cartes_min_max": [min(len(json.dumps(fiches[i]["contenu"], ensure_ascii=False)) for i in ids),
                                                          max(len(json.dumps(fiches[i]["contenu"], ensure_ascii=False)) for i in ids)],
                          "longueur_des_cartes_ailleurs_min_max": [min(len(json.dumps(fiches[i]["contenu"], ensure_ascii=False)) for i in fiches if i not in ids),
                                                                   max(len(json.dumps(fiches[i]["contenu"], ensure_ascii=False)) for i in fiches if i not in ids)]}
    ctrl["alertes_par_case"] = alertes
    ctrl["esperance_de_cases_trop_propres_si_notables_repartis_au_hasard"] = round(esperance_propres, 3)
    ctrl["items_a_plafond"] = {jg: [it for it in ITEMS if ctrl["juges_items_vrais_par_item"][jg][it] == len(verdicts)] for jg in JUGES}
    ctrl["notables_opus_inclus_dans_argon"] = all(v["verdicts"]["juge-argon"]["notable"] for v in verdicts.values()
                                                  if v["verdicts"]["juge-opus"]["notable"])
    ctrl["notables_bilan"] = d["bilan"]["generations"][0]["notables"]
    ctrl["cartes_rendues_total"] = rendues
    sortie["controles"] = ctrl
    return sortie


def comptes(d: dict, racine: str, matiere_chemin: str) -> dict:
    fiches, verdicts, aig, mf, mlf = d["fiches"], d["verdicts"], d["aiguillage"], d["manifeste_fin"], d["manifeste_lanceur_fin"]
    C = collections.Counter
    out = {}
    out["cartes_par_espece"] = dict(sorted(C(f["meta"]["proposeur"] for f in fiches.values()).items()))
    out["cartes_par_lot"] = dict(sorted(C(lot_de(f) for f in fiches.values()).items()))
    tab = collections.defaultdict(lambda: collections.Counter())
    for f in fiches.values():
        tab[lot_de(f)][f["meta"]["proposeur"]] += 1
    out["cartes_par_lot_et_espece"] = {k: dict(sorted(v.items())) for k, v in sorted(tab.items())}
    out["retenues_par_fournisseur"] = dict(C(r["fournisseur"] for r in aig["retenues"]))
    out["retenues_categories"] = [r["categorie"] for r in aig["retenues"]]
    roles = mf["suivi_roles"]["roles"]
    out["appels_proposition_par_espece"] = {r: {"appels": v["appels"], "inexploitables": v["inexploitables"]}
                                            for r, v in sorted(roles.items()) if r.startswith("prop-")}
    out["refus_au_format_evenements"] = C((e["role"], e["motif"]) for e in mf["evenements"] if e["evenement"] == "appel-inexploitable")
    out["refus_au_format_evenements"] = {f"{k[0]} | {k[1]}": v for k, v in out["refus_au_format_evenements"].items()}
    out["cartes_par_appel_exploitable"] = {r: round(out["cartes_par_espece"].get(r, 0) / max(1, v["appels"] - v["inexploitables"]), 3)
                                           for r, v in out["appels_proposition_par_espece"].items()}
    out["champs_hors_des_dix"] = dict(C(k for f in fiches.values() for k in f["contenu"]
                                        if k not in ("titre", "axe", "mecanisme", "module_change", "plus_proche_voisin",
                                                     "ce_qui_distingue", "epreuve_monde_plante", "cout", "ce_qui_la_refuterait", "limites")))
    out["classes_aiguilleur"] = {"niveau_methode (passeport)": aig["passeports"],
                                 "a_corriger (retenue)": sum(r["classe"] == "a_corriger" for r in aig["retenues"]),
                                 "concret": sum(r["classe"] == "concret" for r in aig["retenues"]),
                                 "refus_aiguilleur": aig["refus_aiguilleur"]}
    out["exclusions_a4"] = {"manifeste_orchestrateur": mf["exclues_a4"], "manifeste_lanceur": mlf["ce_qui_a_ete_fait"]["exclues_a4"]}
    motif = re.compile(r"\b(" + "|".join(ETIQUETTES_A4) + r")\b", re.I)
    out["etiquettes_a4_en_mot_entier_dans_les_cartes_rendues"] = sum(
        bool(motif.search(" ".join(str(x) for x in f["contenu"].values()))) for f in fiches.values())
    # verdicts des items
    out["items_vrais_par_juge"] = {jg: {it: sum(v["verdicts"][jg]["items"][it] is True for v in verdicts.values()) for it in ITEMS}
                                   for jg in JUGES}
    out["notables_par_juge"] = {jg: sum(v["verdicts"][jg]["notable"] for v in verdicts.values()) for jg in JUGES}
    notable = {l["ident"]: l["notable"] for l in d["classement"]["lignes"]}
    out["notables_unanimite"] = sum(notable.values())
    out["notables_unanimite_par_espece"] = dict(sorted(C(fiches[i]["meta"]["proposeur"] for i, n in notable.items() if n).items()))
    out["notables_unanimite_par_lot"] = dict(sorted(C(lot_de(fiches[i]) for i, n in notable.items() if n).items()))
    out["items_faux_par_juge_et_espece"] = {jg: {it: dict(sorted(C(fiches[i]["meta"]["proposeur"] for i, v in verdicts.items()
                                                                   if v["verdicts"][jg]["items"][it] is False).items()))
                                                 for it in ITEMS} for jg in JUGES}
    out["accord_des_juges_par_item"] = {it: sum(v["verdicts"]["juge-opus"]["items"][it] == v["verdicts"]["juge-argon"]["items"][it]
                                                for v in verdicts.values()) for it in ITEMS}
    out["redites"] = {"nombre": len(d["memoire"]["redites"]), "idees_distinctes": d["memoire"]["idees_distinctes"],
                      "taille_lot": d["memoire"]["taille_lot"], "seuil": d["memoire"]["seuil"], "bardeau": d["memoire"]["taille_bardeau"]}
    out["roles_arretes"] = {"orchestrateur": mf["roles_arretes"], "a2": mf["roles_arretes_a2"], "lanceur": mlf["ce_qui_a_ete_fait"]["roles_arretes"]}
    cr = mlf["cout_reel"]
    out["couts"] = {"total_usd": cr["total_usd"], "par_relais_usd": cr["par_relais_usd"], "par_role_usd": cr["par_role_usd"],
                    "appels_par_role": cr["appels_par_role"], "ecart_au_devis_v1": mlf["ecart_au_devis_v1"],
                    "releve_credits_apres": mlf["releve_credits_apres"], "journal_budget": mf["budget"]["journal"]}
    cons = d["consommations"]["consommations"]
    acc = collections.defaultdict(float)
    for x in cons:
        acc[x["role"]] += x["cout_usd"]
    out["couts"]["recalcul_consommations_par_role_usd"] = {k: round(v, 6) for k, v in sorted(acc.items())}
    out["couts"]["recalcul_consommations_total_usd"] = round(sum(acc.values()), 6)
    # complément descriptif (hors « Métrique ») : titres identiques à la casse et à la ponctuation près, modules nommés
    norm = lambda s: re.sub(r"[^\w]+", " ", s.lower()).replace(" k ", " ").strip()
    titres = collections.defaultdict(list)
    for i, f in fiches.items():
        titres[norm(f["contenu"].get("titre", ""))].append(f"{i} {f['meta']['proposeur']} {lot_de(f)[:2]}")
    out["complement_titres_identiques"] = {t: v for t, v in titres.items() if len(v) > 1}
    modules = ["proposeurs", "aiguilleur", "juges croisés", "juge statistique", "tests de mort", "témoins plantés",
               "mémoire anti-redite", "sélection entre générations", "bisociateur", "noyau et budget", "dossier fermé",
               "coffre", "moisson de nouveauté"]
    out["complement_modules_nommes_dans_module_change"] = dict(C(m for f in fiches.values() for m in modules
                                                                 if m in f["contenu"].get("module_change", "").lower()).most_common())
    # axes, valeurs telles quelles
    out["axes_tels_quels"] = dict(C(f["contenu"].get("axe", "") for f in fiches.values()).most_common())
    out["axes_tels_quels_par_espece"] = {k: dict(C(f["contenu"].get("axe", "") for f in fiches.values()
                                                   if f["meta"]["proposeur"] == k).most_common())
                                         for k in sorted(out["cartes_par_espece"])}
    # identifiants du catalogue : programme d'épreuve v2 importé, non recopié
    spec = importlib.util.spec_from_file_location("epreuve_v2", os.path.join(racine, "scripts/epreuve_temoins_auto_conception_v2.py"))
    ep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ep)
    with open(matiere_chemin, "rb") as f:
        matiere = f.read()
    if hashlib.sha256(matiere).hexdigest() != MATIERE_SHA:
        raise SystemExit("ARRÊT : matière v3 d'une autre empreinte")

    def servir(seul_voisin: bool) -> dict:
        t = {}
        for i, f in fiches.items():
            c = dict(f["contenu"])
            c.setdefault("ce_qui_distingue", "")
            c.setdefault("titre", "")
            if seul_voisin:
                c["ce_qui_distingue"] = ""
            t[i] = {"contenu": c, "classe": "bon", "item_plante": None}
        return t

    res = {}
    for nom, seul in (("champ_plus_proche_voisin_seul", True), ("fonction_telle_quelle_voisin_et_ce_qui_distingue", False)):
        s = ep.controles_statiques(servir(seul), ITEMS, "", matiere)
        cites, absents = s["identifiants_cites"], s["identifiants_absents_de_la_matiere"]
        abs_par = collections.defaultdict(set)
        for a in absents:
            i, ident = a.split(":", 1)
            abs_par[i].add(ident)
        au_moins_un_existant = {i for i, ids in cites.items() if any(x not in abs_par[i] for x in ids)}
        tous_existants = {i for i, ids in cites.items() if ids and not abs_par[i]}
        aucun_cite = {i for i, ids in cites.items() if not ids}
        par_esp = {}
        for e in sorted(out["cartes_par_espece"]):
            ids_e = [i for i in fiches if fiches[i]["meta"]["proposeur"] == e]
            par_esp[e] = {"cartes": len(ids_e), "au_moins_un_identifiant_existant": sum(i in au_moins_un_existant for i in ids_e),
                          "aucun_identifiant_cite": sum(i in aucun_cite for i in ids_e),
                          "un_identifiant_absent_au_moins": sum(bool(abs_par[i]) for i in ids_e)}
        res[nom] = {"cartes": len(fiches), "au_moins_un_identifiant_existant": len(au_moins_un_existant),
                    "part_au_moins_un_existant": round(len(au_moins_un_existant) / len(fiches), 4),
                    "tous_les_identifiants_cites_existent": len(tous_existants),
                    "aucun_identifiant_cite": len(aucun_cite),
                    "cartes_avec_un_identifiant_absent": sum(bool(v) for v in abs_par.values()),
                    "identifiants_absents": sorted(absents), "par_espece": par_esp,
                    "matiere_sha256": s["matiere_sha256"]}
    out["identifiants_du_catalogue"] = res
    out["identifiants_du_catalogue"]["note"] = (
        "controles_statiques lit plus_proche_voisin + ' ' + ce_qui_distingue ; la mesure de la « Métrique » (champ "
        "plus_proche_voisin) est obtenue en servant à la fonction une copie de chaque carte où ce_qui_distingue est vide ; "
        "la lecture de la fonction telle quelle est rapportée à côté. Un identifiant « existe » s'il figure parmi les titres "
        "de regroupement « **famille n° N — » de la matière v3 (règle de la fonction).")
    return out


def principal() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--racine", required=True)
    p.add_argument("--matiere", required=True)
    p.add_argument("--etape", choices=["audit", "comptes"], required=True)
    p.add_argument("--sortie", required=True)
    a = p.parse_args()
    vu = verifier(a.racine)
    d = charger(a.racine)
    if a.etape == "audit":
        r = {"etape": "audit", "empreintes_verifiees": vu, "audit": audit(d)}
    else:
        r = {"etape": "comptes", "empreintes_verifiees": vu, "comptes": comptes(d, a.racine, a.matiere)}
    with open(a.sortie, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1, sort_keys=False)
    print(json.dumps(r, ensure_ascii=False, indent=1)[:200000])
    return 0


if __name__ == "__main__":
    sys.exit(principal())
