#!/usr/bin/env python3
"""Comptes mécaniques pour l'état des faits « trois règles de la course à plusieurs générations » — v1.

Lecture seule. Aucun appel de modèle, aucun réseau, aucune clé. Bibliothèque standard seulement.

Ce programme lit, dans le dépôt de travail, les seuls journaux bruts de courses de l'organisme d'idéation à plus d'une
génération qui s'y trouvent (deux essais à blanc à proposeurs scriptés et bac à sable factice), et compte, pour chacune des
trois règles :

  règle 1 — sort de la fiche non concluante : verdicts des tests de mort par bras et par génération (survit, éliminée,
            non concluant), et ce que deviennent à la génération suivante les fiches qui ne sont pas retenues ;
  règle 2 — note ou rang du juge montré aux proposeurs : contenu exact du texte servi aux proposeurs à chaque génération
            (clés, ordre des lois retenues, recherche des chiffres du juge dans le texte) ;
  règle 3 — cache entre exécutions dans le bac à sable : nombre d'exécutions par fiche, dossier de travail de chaque
            exécution, fichiers produits (noms, empreintes), réemploi d'un fichier d'une exécution à l'autre.

Il compare aussi, par empreinte, la copie du code de l'organisme présente au dépôt (commit 94bfd92) aux empreintes de code
consignées par les manifestes des courses réelles à une génération des 13 et 14 novembre.

Usage : python3 -I compter_trois_regles_v1.py RACINE_DU_DEPOT SORTIE.json
"""

import collections
import hashlib
import json
import os
import re
import sys

ESSAI_V64 = "docs/notes/organisme-boucle-reelle-v1/essai-a-blanc-v1/sorties-completes/v64-factice-g2"
RELEVE_V64 = ESSAI_V64 + "/tour-ferme-v1-etage1.json"
ESSAI_V66 = "docs/notes/organisme-boucle-reelle-v1/code-v66/essai-a-blanc-v66"
RELEVES_V66 = ("releve-course.json", "releve-course-arret.json", "releve-course-etage.json")
COPIE_CODE = "docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole"
MANIFESTES_REELS = (
    "runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--manifeste-fin.json",
    "runs/course-ideation-regard-ou-raisons-v1/20261114-100746-course-ideation-regard-ou-raisons-v1-g1/copies/sortie--manifeste-fin.json",
)
FICHIERS_DE_CODE_SUIVIS = ("tests_de_mort.py", "tests_de_mort_v4.py", "tests_de_mort_v5.py", "etage_entre_generations_v57.py",
                           "boucle_fermee_v59.py", "tour_ferme_v64.py")
# Clés qui, dans un texte servi à un proposeur, porteraient une information du juge (liste du code v59, plus des synonymes).
CLES_DU_JUGE = {"verdict", "verdict_final", "verdict_noyau", "promue", "promues", "log_richesse", "log_richesse_max", "richesse",
                "trajectoire_log_w", "multiplicite", "motif", "motif_verdict", "exclues", "comptes", "pari", "evaluation",
                "evaluations", "juge", "membre_dominant_final", "log_e", "rang", "score", "note", "classement", "gain_nat",
                "delta_gain_nat", "divergence_nat", "valeur_noyau"}
CHAMPS_CHIFFRES_DU_JUGE = ("log_e", "log_richesse_max", "gain_nat", "delta_gain_nat", "divergence_nat")


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def lire_json(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def verifier_compagnons(dossier):
    """Chaque fichier a-t-il un compagnon `.sha256` égal ? Rend les comptes."""
    n = egaux = sans = 0
    ecarts = []
    for racine, _, fichiers in os.walk(dossier):
        for nom in fichiers:
            if nom.endswith(".sha256"):
                continue
            n += 1
            chemin = os.path.join(racine, nom)
            comp = chemin + ".sha256"
            if not os.path.exists(comp):
                sans += 1
                continue
            attendu = open(comp, encoding="utf-8").read().split()[0]
            if attendu == sha256_fichier(chemin):
                egaux += 1
            else:
                ecarts.append(os.path.relpath(chemin, dossier))
    return {"fichiers": n, "compagnons_egaux": egaux, "sans_compagnon": sans, "ecarts": ecarts}


def cles_a_toute_profondeur(o):
    trouvees = set()
    pile = [o]
    while pile:
        x = pile.pop()
        if isinstance(x, dict):
            trouvees |= set(x)
            pile.extend(x.values())
        elif isinstance(x, list):
            pile.extend(x)
    return trouvees


def formes_d_un_chiffre(v):
    """Écritures plausibles d'un chiffre du juge dans un texte : repr, 6, 4, 3 et 2 décimales (au moins 4 chiffres
    significatifs écrits, pour ne pas compter les coïncidences sur « 0.5 » ou « 1.0 »)."""
    formes = {repr(v)}
    for d in (6, 4, 3, 2):
        formes.add(f"{v:.{d}f}")
    return {s for s in formes if len(re.sub(r"[^0-9]", "", s)) >= 4}


# ---------------------------------------------------------------------------------------------------------------------
# Essai à blanc v64 (arbre complet au dépôt)
# ---------------------------------------------------------------------------------------------------------------------

def essai_v64(depot):
    base = os.path.join(depot, ESSAI_V64)
    releve_complet = lire_json(os.path.join(depot, RELEVE_V64))
    releve = releve_complet["releve"]
    sortie = {"chemin": ESSAI_V64, "releve_sha256": sha256_fichier(os.path.join(depot, RELEVE_V64)),
              "version": releve_complet.get("version"), "mode": releve_complet.get("mode"),
              "fin_utc": releve_complet.get("fin_utc"), "generations_jouees": releve.get("generations_jouees"),
              "compagnons": verifier_compagnons(base)}

    # --- règle 1 : verdicts par bras et génération, d'après le relevé, puis d'après les fichiers de verdict du noyau
    par_groupe = collections.OrderedDict()
    for c in releve["cartes"]:
        cle = (c["bras"], c["generation"], "temoin plante" if c.get("temoin") else "carte de proposeur")
        g = par_groupe.setdefault(cle, collections.Counter())
        g["proposees"] += 1
        if c.get("gardien") != "passe":
            g["refusees_au_gardien"] += 1
        elif not c.get("promue"):
            g["non_promues_par_le_juge_donc_jamais_testees"] += 1
        else:
            g["promues_par_le_juge"] += 1
            g["test_de_mort:" + str(c.get("verdict"))] += 1
        if c.get("retenue"):
            g["retenues"] += 1
    sortie["regle_1_releve"] = [{"bras": b, "generation": g, "sorte": s, **dict(v)} for (b, g, s), v in par_groupe.items()]

    verdicts_disque = collections.Counter()
    fiches_test = []
    for racine, dossiers, fichiers in os.walk(base):
        if "verdict-noyau-v5.json" in fichiers:
            v = lire_json(os.path.join(racine, "verdict-noyau-v5.json"))
            rel = os.path.relpath(racine, base).split(os.sep)
            bras, generation, etage = rel[0], rel[1], rel[2]
            verdicts_disque[(bras, generation, etage, v.get("verdict"))] += 1
            fiches_test.append(racine)
    sortie["regle_1_fichiers_de_verdict"] = [{"bras": b, "generation": g, "etage": e, "verdict": v, "fiches": n}
                                             for (b, g, e, v), n in sorted(verdicts_disque.items())]
    sortie["regle_1_total_par_verdict"] = dict(collections.Counter(
        v for (_, _, _, v), n in verdicts_disque.items() for _ in range(n)))
    sortie["regle_1_journal_comptes"] = [
        {"tache": e.get("tache"), "dossier": e.get("dossier"), "comptes": e.get("comptes"), "bac_a_sable": e.get("bac_a_sable")}
        for e in releve_complet["journal"] if e.get("evenement") == "etage-tests-de-mort"]

    # règle de sélection écrite dans les fichiers de sélection eux-mêmes
    regles = set()
    exclues_total = 0
    for racine, _, fichiers in os.walk(base):
        for nom in fichiers:
            if nom == "selection-entre-generations-v57.json":
                s = lire_json(os.path.join(racine, nom))
                regles.add(s.get("regle"))
                exclues_total += len(s.get("exclues") or [])
    sortie["regle_1_regle_ecrite_dans_les_selections"] = sorted(regles)
    sortie["regle_1_exclues_listees_dans_les_selections"] = exclues_total

    # devenir à la génération suivante des cartes non retenues (cartes de proposeur seulement)
    lois = {}        # (bras, generation) -> {identifiant servi: loi}
    archives = {}    # (bras, generation) -> ensemble des identifiants de l'archive écrite au bilan
    for bras in sorted(os.listdir(base)):
        if not bras.startswith("bras-"):
            continue
        for gen in sorted(os.listdir(os.path.join(base, bras))):
            d = os.path.join(base, bras, gen)
            g = int(gen.split("-")[1])
            cartes = lire_json(os.path.join(d, "cartes-generation-v59.json"))
            lois[(bras[5:], g)] = {c["identifiant"]: c.get("loi_predictive") for c in cartes["cartes"]}
            bilan = lire_json(os.path.join(d, "bilan-generation-v59.json"))
            archives[(bras[5:], g)] = set(bilan.get("archive") or {})
    devenir = collections.Counter()
    for c in releve["cartes"]:
        if c.get("temoin") or c.get("retenue"):
            continue
        bras, g = c["bras"], c["generation"]
        if c.get("gardien") != "passe":
            statut = "refusée au gardien"
        elif not c.get("promue"):
            statut = "non promue par le juge (jamais testée)"
        else:
            statut = "test de mort : " + str(c.get("verdict"))
        ident = c.get("identifiant_servi")
        loi = lois.get((bras, g), {}).get(ident)
        suivante = (bras, g + 1)
        if suivante not in lois:
            devenir[(bras, g, statut, "pas de génération suivante jouée dans ce bras")] += 1
            continue
        dans_archive = ident in archives.get((bras, g), set())
        reproposee = loi is not None and any(canon(loi) == canon(l) for l in lois[suivante].values())
        devenir[(bras, g, statut,
                 ("dans l'archive servie ensuite" if dans_archive else "absente de l'archive servie ensuite")
                 + (" ; même loi reproposée à la génération suivante" if reproposee
                    else " ; loi non reproposée à la génération suivante"))] += 1
    sortie["regle_1_devenir_des_non_retenues"] = [{"bras": b, "generation": g, "statut": s, "devenir": d, "cartes": n}
                                                  for (b, g, s, d), n in sorted(devenir.items())]

    # --- règle 2 : textes servis aux proposeurs
    chiffres = collections.defaultdict(set)  # (bras, generation) -> écritures des chiffres du juge de cette génération
    log_e = {}
    for c in releve["cartes"]:
        for champ in CHAMPS_CHIFFRES_DU_JUGE:
            v = c.get(champ)
            if isinstance(v, (int, float)):
                chiffres[(c["bras"], c["generation"])] |= formes_d_un_chiffre(v)
        if isinstance(c.get("log_e"), (int, float)) and c.get("identifiant_servi"):
            log_e[(c["bras"], c["generation"], c["identifiant_servi"])] = c["log_e"]
    vues = []
    racine_prop = os.path.join(base, "proposeurs")
    for proposeur in sorted(os.listdir(racine_prop)):
        for tache in sorted(os.listdir(os.path.join(racine_prop, proposeur))):
            m = re.search(r"bras=([a-z_]+)\|generation=(\d+)", tache)
            bras, g = m.group(1), int(m.group(2))
            for nom in sorted(os.listdir(os.path.join(racine_prop, proposeur, tache))):
                if nom.endswith(".sha256"):
                    continue
                chemin = os.path.join(racine_prop, proposeur, tache, nom)
                texte = open(chemin, encoding="utf-8").read()
                contexte = None
                for ligne in texte.split("\n"):
                    if ligne.startswith("{"):
                        contexte = json.loads(ligne)
                retenues = [x.get("identifiant") for x in (contexte or {}).get("lois_retenues", [])]
                cles_entrees = sorted({k for x in (contexte or {}).get("lois_retenues", []) for k in x})
                precedents = chiffres.get((bras, g - 1), set())
                # comparaison nombre à nombre (un chiffre du juge n'est compté que s'il est écrit en entier dans le texte,
                # jamais comme début d'un nombre plus long : « 0.020 » ne compte pas dans « 0.020123 »)
                nombres_du_texte = set(re.findall(r"(?<![0-9.])-?[0-9]+\.[0-9]+(?![0-9])", texte))
                nombres_du_texte |= {s.lstrip("-") for s in nombres_du_texte}
                touches = sorted(s for s in precedents if s.lstrip("-") in nombres_du_texte)
                touches_en_sous_chaine = sorted(s for s in precedents if s in texte)
                par_log_e = sorted(retenues, key=lambda i: (-(log_e.get((bras, g - 1, i), -1e9)), i))
                vues.append({
                    "proposeur": proposeur, "bras": bras, "generation": g, "fichier": os.path.relpath(chemin, base),
                    "sha256": sha256_fichier(chemin), "caracteres": len(texte),
                    "cles_du_contexte": sorted(contexte or {}),
                    "lois_retenues_servies": len(retenues), "cles_de_chaque_loi_retenue": cles_entrees,
                    "cles_du_juge_trouvees_a_toute_profondeur": sorted(cles_a_toute_profondeur(contexte) & CLES_DU_JUGE),
                    "ordre_des_lois_retenues_egal_a_l_ordre_des_identifiants": retenues == sorted(retenues),
                    "ordre_des_lois_retenues_egal_a_l_ordre_decroissant_du_log_e": (retenues == par_log_e) if len(retenues) > 1 else None,
                    "chiffres_du_juge_de_la_generation_precedente_cherches": len(precedents),
                    "chiffres_du_juge_retrouves_dans_le_texte": touches,
                    "chiffres_du_juge_presents_seulement_comme_debut_d_un_nombre_plus_long": [s for s in touches_en_sous_chaine if s not in touches],
                    "mots_verdict_rang_score_note_classement_dans_la_consigne": sorted(
                        w for w in ("verdict", "rang", "score", "note", "classement", "richesse", "log e", "promu")
                        if re.search(r"\b" + re.escape(w), texte.split("```json")[0], flags=re.I)),
                })
    sortie["regle_2_textes_servis_aux_proposeurs"] = vues

    # --- règle 3 : exécutions dans le bac
    executions_par_fiche = collections.Counter()
    produits = collections.defaultdict(list)   # empreinte -> [(fiche, exécution, nom)]
    scripts = collections.defaultdict(list)
    dossiers_travail = collections.defaultdict(list)
    reemplois = []
    tours = collections.Counter()
    champs_de_date = set()
    for d in sorted(fiches_test):
        fiche = os.path.relpath(d, base)
        res = lire_json(os.path.join(d, "resultat.json"))
        ex = res.get("executions") or []
        executions_par_fiche[len(ex)] += 1
        tours[len([x for x in os.listdir(os.path.join(d, "experimentateur")) if x.startswith("traces-tour-")])] += 1
        vus_dans_la_fiche = {}
        for e in ex:
            champs_de_date |= {k for k in e if any(w in k.lower() for w in ("utc", "date", "heure", "debut", "fin_"))}
            scripts[e.get("script_sha256")].append((fiche, e.get("numero")))
            detail = os.path.join(d, f"execution-{e.get('numero'):02d}", "resultat.json")
            if os.path.exists(detail):
                cmd = lire_json(detail).get("commande") or []
                if cmd:
                    dossiers_travail[os.path.dirname(cmd[-1])].append((fiche, e.get("numero")))
            for p in e.get("fichiers_produits") or []:
                produits[p.get("sha256")].append((fiche, e.get("numero"), p.get("chemin")))
                if p.get("sha256") in vus_dans_la_fiche:
                    reemplois.append({"fiche": fiche, "fichier": p.get("chemin"), "sha256": p.get("sha256"),
                                      "executions": [vus_dans_la_fiche[p.get("sha256")], e.get("numero")]})
                vus_dans_la_fiche[p.get("sha256")] = e.get("numero")
    sortie["regle_3"] = {
        "bac_a_sable": sorted({e.get("bac_a_sable") for e in releve_complet["journal"] if e.get("evenement") == "etage-tests-de-mort"}),
        "fiches_testees": len(fiches_test),
        "fiches_par_nombre_d_executions": dict(sorted(executions_par_fiche.items())),
        "fiches_par_nombre_de_tours_de_l_experimentateur": dict(sorted(tours.items())),
        "fiches_a_plus_d_une_execution": sum(n for k, n in executions_par_fiche.items() if k > 1),
        "fichier_produit_de_meme_empreinte_dans_deux_executions_d_une_meme_fiche": reemplois,
        "dossiers_de_travail_distincts": len(dossiers_travail),
        "dossiers_de_travail_employes_par_plus_d_une_execution": [
            {"dossier": k, "executions": v} for k, v in sorted(dossiers_travail.items()) if len(v) > 1],
        "noms_des_fichiers_produits": dict(collections.Counter(n for v in produits.values() for (_, _, n) in v)),
        "empreintes_de_produits_distinctes": len(produits),
        "empreintes_de_produits_partagees_entre_fiches": [
            {"sha256": k, "fichier": sorted({n for (_, _, n) in v}), "fiches": [f for (f, _, _) in v]}
            for k, v in sorted(produits.items()) if len(v) > 1],
        "scripts_distincts": len(scripts),
        "scripts_partages_entre_fiches": sum(1 for v in scripts.values() if len(v) > 1),
        "champs_de_date_par_execution": sorted(champs_de_date),
        "tranche_par_tache": sorted({(e.get("tache"), e.get("tranche_index_sha256"))
                                     for e in releve_complet["journal"] if e.get("evenement") == "etage-tests-de-mort"}),
    }
    return sortie


# ---------------------------------------------------------------------------------------------------------------------
# Essai à blanc v66 (relevés seuls au dépôt, sans l'arbre des exécutions ni les textes servis)
# ---------------------------------------------------------------------------------------------------------------------

def essai_v66(depot):
    sortie = []
    for nom in RELEVES_V66:
        chemin = os.path.join(depot, ESSAI_V66, nom)
        o = lire_json(chemin)
        r = o["releve"]
        s = {"fichier": ESSAI_V66 + "/" + nom, "sha256": sha256_fichier(chemin), "version": r.get("version"), "mode": o.get("mode"),
             "generations_jouees": r.get("generations_jouees"), "arret": (r.get("arret") or "")[:200] or None,
             "complet": r.get("complet")}
        comptes = collections.OrderedDict()
        for sorte, liste in (("carte de proposeur", r.get("cartes") or []), ("loi plantée", r.get("plantees") or [])):
            for c in liste:
                g = comptes.setdefault((c.get("generation"), sorte), collections.Counter())
                g["proposees"] += 1
                if c.get("gardien") != "passe":
                    g["refusees_au_gardien"] += 1
                elif not c.get("promue"):
                    g["non_promues_par_le_juge_donc_jamais_testees"] += 1
                else:
                    g["promues_par_le_juge"] += 1
                    g["test_de_mort:" + str(c.get("verdict"))] += 1
                if c.get("retenue"):
                    g["retenues"] += 1
        s["regle_1"] = [{"generation": g, "sorte": so, **dict(v)} for (g, so), v in comptes.items()]
        s["regle_1_journal_comptes"] = [{"tache": e.get("tache"), "dossier": e.get("dossier"), "comptes": e.get("comptes"),
                                         "bac_a_sable": e.get("bac_a_sable")}
                                        for e in (o.get("journal") or []) if e.get("evenement") == "etage-tests-de-mort"]
        s["retenues_par_generation"] = {g: len(v) for g, v in (r.get("retenues") or {}).items()}
        # devenir : une carte de génération 1 non retenue est-elle servie en génération 2 ?
        retenues_1 = set((r.get("retenues") or {}).get("1") or [])
        vues = r.get("vues_servies") or {}
        s["regle_2"] = []
        for g, v in sorted(vues.items()):
            ids = v.get("identifiants") or []
            s["regle_2"].append({
                "generation": int(g), "identifiants_servis": len(ids),
                "identifiants_servis_egaux_aux_attendus": ids == (v.get("attendus") or []),
                "ordre_egal_a_l_ordre_des_identifiants": ids == sorted(ids),
                "servis_hors_archive_de_depart_et_retenues": sorted(set(ids) - retenues_1 - set((r.get("heritage_depart") or {}).get("archive") or [])),
                "texte_recu_par_chaque_proposeur_egal_au_texte_ecrit": all(a.get("texte_recu_sha256") == v.get("texte_sha256") for a in v.get("appels") or []),
                "texte_sha256": v.get("texte_sha256"),
                "texte_present_au_depot": False,
            })
        s["regle_3"] = {"bac_a_sable": sorted({e.get("bac_a_sable") for e in (r.get("etages") or [])}),
                        "arbre_des_executions_present_au_depot": False}
        sortie.append(s)
    return sortie


def code(depot):
    copie = os.path.join(depot, COPIE_CODE)
    locales = {n: sha256_fichier(os.path.join(copie, n)) for n in FICHIERS_DE_CODE_SUIVIS}
    comparaisons = []
    for m in MANIFESTES_REELS:
        o = lire_json(os.path.join(depot, m))
        consignees = o.get("code_sha256") or {}
        comparaisons.append({"manifeste": m, "manifeste_sha256": sha256_fichier(os.path.join(depot, m)),
                             "fichiers": {n: {"copie_du_depot": locales[n], "consignee_par_la_course": consignees.get(n),
                                              "egales": consignees.get(n) == locales[n] if n in consignees else None}
                                          for n in FICHIERS_DE_CODE_SUIVIS}})
    return {"copie": COPIE_CODE, "empreintes": locales, "comparaison_aux_courses_reelles_a_une_generation": comparaisons}


def main():
    depot, cible = sys.argv[1], sys.argv[2]
    resultat = {"programme": "compter_trois_regles_v1.py", "programme_sha256": sha256_fichier(os.path.abspath(__file__)),
                "essai_a_blanc_v64": essai_v64(depot), "essai_a_blanc_v66": essai_v66(depot), "code": code(depot)}
    with open(cible, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")

    a = resultat["essai_a_blanc_v64"]
    print("== Essai à blanc v64, deux générations, trois bras (proposeurs scriptés, bac factice) ==")
    print("relevé", a["releve_sha256"], "| fin", a["fin_utc"], "| générations jouées", a["generations_jouees"])
    print("compagnons .sha256 :", a["compagnons"])
    print("-- règle 1 : cartes par bras, génération et sorte (relevé)")
    for l in a["regle_1_releve"]:
        print("  ", l)
    print("-- règle 1 : fichiers verdict-noyau-v5.json comptés sur disque")
    for l in a["regle_1_fichiers_de_verdict"]:
        print("  ", l)
    print("   total par verdict :", a["regle_1_total_par_verdict"])
    print("   exclues listées dans les fichiers de sélection :", a["regle_1_exclues_listees_dans_les_selections"])
    for r in a["regle_1_regle_ecrite_dans_les_selections"]:
        print("   règle écrite :", r)
    print("-- règle 1 : devenir des cartes de proposeur non retenues")
    for l in a["regle_1_devenir_des_non_retenues"]:
        print("  ", l)
    print("-- règle 2 : textes servis aux proposeurs")
    for v in a["regle_2_textes_servis_aux_proposeurs"]:
        print("  ", {k: v[k] for k in ("proposeur", "bras", "generation", "caracteres", "cles_du_contexte", "lois_retenues_servies",
                                       "cles_de_chaque_loi_retenue", "cles_du_juge_trouvees_a_toute_profondeur",
                                       "ordre_des_lois_retenues_egal_a_l_ordre_des_identifiants",
                                       "ordre_des_lois_retenues_egal_a_l_ordre_decroissant_du_log_e",
                                       "chiffres_du_juge_de_la_generation_precedente_cherches",
                                       "chiffres_du_juge_retrouves_dans_le_texte",
                                       "chiffres_du_juge_presents_seulement_comme_debut_d_un_nombre_plus_long",
                                       "mots_verdict_rang_score_note_classement_dans_la_consigne")})
        print("      fichier", v["fichier"], v["sha256"])
    print("-- règle 3 : exécutions dans le bac")
    for k, v in a["regle_3"].items():
        if k == "empreintes_de_produits_partagees_entre_fiches":
            print("  ", k, ":", len(v), "empreinte(s) partagée(s)")
            for x in v:
                print("      ", x["sha256"], x["fichier"], "dans", len(x["fiches"]), "fiches :", x["fiches"])
        else:
            print("  ", k, ":", v)
    print()
    print("== Essai à blanc v66 (relevés seuls) ==")
    for s in resultat["essai_a_blanc_v66"]:
        print(s["fichier"], s["sha256"])
        print("   générations jouées", s["generations_jouees"], "| complet", s["complet"], "| arrêt", s["arret"])
        for l in s["regle_1"]:
            print("   règle 1", l)
        for l in s["regle_1_journal_comptes"]:
            print("   règle 1, journal", l)
        print("   retenues par génération", s["retenues_par_generation"])
        for l in s["regle_2"]:
            print("   règle 2", l)
        print("   règle 3", s["regle_3"])
    print()
    print("== Code : copie du dépôt (commit 94bfd92) contre les empreintes consignées par les courses réelles à une génération ==")
    for c in resultat["code"]["comparaison_aux_courses_reelles_a_une_generation"]:
        print(c["manifeste"])
        for n, d in c["fichiers"].items():
            print("  ", n, d)


if __name__ == "__main__":
    main()
