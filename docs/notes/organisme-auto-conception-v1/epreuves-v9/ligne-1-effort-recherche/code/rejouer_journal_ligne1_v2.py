"""Rejeu du journal scellé du banc A, ligne 1 (version 2 du code) — garde A16.

Version 2 (recommandation (a) de la contre-lecture retenue ; réserve « recoupement de M1-nul » de l'autre contre-lecture) :
en plus du rejeu au bit près, chaque journal est **recoupé** avec la sortie brute de la même course et de la même classe
(celle que lit l'analyse) : (i) le `m` de chaque décision de promotion e-BH est celui que la décision de registre de la
même génération et du même bras a calculé pour la définition donnée (porté à m_s), et le nombre de cartes de chaque
promotion vaut m_s ; (ii) les promotions et lignées en course de chaque bras, à chaque génération, lues dans les décisions
d'arrêt du journal, sont celles de la sortie brute, et elles suivent la sortie de la décision de promotion ; (iii) l'effet
de chaque lignée jugée (type de la loi du monde dans la table des objets du journal) est celui de la sortie brute.
Pour les courses de l'audit de symétrie (0, 300, 599), M1-nul de chaque bras est recalculé depuis les seules décisions du
journal et comparé à celui que l'analyse calcule sur la sortie brute ; **seule la concordance est écrite, jamais la
valeur** (aucune lecture de résultat avant l'analyse). Un écart lève `GardeA16Recoupement` (lecture refusée, comme A16).

Préenregistrement qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`,
sha256 523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9 (« Journal scellé des décisions du banc », point
« Rejeu » ; garde A16 ; audit de symétrie, rejeu des courses 0, 300 et 599).

Programme à part : il relit chaque journal (chaîne d'empreintes et table des objets vérifiées), puis réexécute chaque
décision depuis ses **seules entrées journalisées** et compare la sortie au bit près (JSON canonique). Une décision qui
diffère, une chaîne rompue ou un objet absent lèvent `GardeA16Rejeu` (lecture refusée). `surcharges` rejoue sous un
mécanisme modifié (essai 10 : seuil de la mémoire changé) ; c'est l'usage que le rang 13 de l'ordre de passage en fera.
"""

import glob
import os

import banc_ligne1_v1 as B
import journal_ligne1_v1 as JL

VERSION = "rejouer-journal-ligne1-v2"


class GardeA16Rejeu(B.ArretBanc):
    pass


class GardeA16Recoupement(GardeA16Rejeu):
    """Le journal et la sortie brute de la même course ne se recoupent pas (m, promotions, effet des lignées, M1-nul)."""


def _rejouer_une(d, objets, entete, surcharges):
    e, s, mec = d["entrees"], d["sortie"], d["mecanisme"]
    o = objets.__getitem__
    if mec == "reception":
        loi, texte = o(e["loi"]), o(e["texte"])
        sortie = {"identifiant": B.identifiant_reception(e["course"], e["classe"], e["lignee"], e["generation"], e["rang"]),
                  "empreinte": JL.empreinte({"loi": loi, "texte": texte})}
        if B.texte_carte(loi) != texte:
            sortie["texte_incoherent"] = True
        return sortie
    if mec == "memoire":
        seuil = surcharges.get("memoire_seuil", e["seuil"])
        smax, refusee = B.decider_memoire(o(e["texte"]), [o(k) for k in e["comparees"]], seuil, e["taille_bardeau"], e["epsilon"])
        return {"similarite_max": smax, "refusee": refusee}
    if mec == "affinage":
        d_, refusee = B.decider_affinage(o(e["loi"]), [o(k) for k in e["jugees_eliminees"]], e["rayon"], e["deja_une_dans_l_appel"])
        return {"derive": d_, "refusee": refusee}
    if mec == "quota":
        pris, ecartes = B.decider_quota(e["restantes"], e["quota"])
        return {"jugees": pris, "ecartees": ecartes}
    if mec == "jugement":
        ev, det = B.juger(o(e["loi"]), o(e["loi_monde"]), e["archive"], e["racine"], e["tache"], tirages=e["tirages"],
                          alpha=e["alpha"], entrainement=e["entrainement"], nombre_instants=e["instants"])
        return {"issue": JL.empreinte(ev), "empreinte_engagement": det["empreinte_engagement"]}
    if mec == "registre":
        recs = [{"id": i, "l": l, "empreinte_loi": el, "refus_memoire": rm} for i, l, el, rm in e["receptions"]]
        numeros, m_r = B.numeroter(recs, e["n_var"], e["lignees_en_course"], e["m_s"])
        return {"numeros": numeros, "m_r": m_r, "m": B.m_par_definition(recs, e["cumul_precedent"])}
    if mec == "promotion_e_bh":
        cartes = [(i, o(k)) for i, k in e["cartes"]]
        promues, _ = B.regle_e_bh(cartes, e["alpha"], e["m"], e["m"])
        return {"promues": promues}
    if mec == "promotion_bonferroni":
        return {"promues": B.regle_bonferroni([(i, o(k)) for i, k in e["cartes"]], e["alpha"], e["G"], e["m_s"])}
    if mec == "promotion_seule":
        return {"promues": B.regle_seule([(i, o(k)) for i, k in e["cartes"]])}
    if mec == "choix_c":
        return {"choisie": B.choisir_c([(i, o(k)) for i, k in e["cartes"]], e["instant"])}
    if mec == "promotion_c":
        return {"promue": any(v >= e["seuil_log"] for v in o(e["issue"])["trajectoire_log_w"])}
    if mec == "arret":
        arretees = sorted({l for _, l in e["promues"]})
        return {"arretees": arretees, "en_course_suivante": [l for l in e["en_course"] if l not in arretees]}
    raise GardeA16Rejeu(f"mécanisme inconnu dans le journal : {mec!r}")


def sortie_de_journal(chemin_journal):
    """Chemin de la sortie brute de la même course et de la même classe."""
    d, n = os.path.split(chemin_journal)
    if not (n.startswith("journal-") and n.endswith(".jsonl.xz")):
        raise GardeA16Recoupement(f"garde A16 : nom de journal inattendu : {n}")
    return os.path.join(d, "sortie-" + n[len("journal-"):-len(".jsonl.xz")] + ".json.xz")


def _bras_de(partie):
    return partie.split("=", 1)[1] if partie.startswith("bras=") else None


def recouper(entete, objets, decisions, sortie):
    """Recoupement d'un journal avec sa sortie brute (recommandation (a)). Rend la liste des écarts (vide si tout
    concorde) et le nombre de contrôles faits. Ne rend aucune valeur de métrique."""
    ecarts, controles = [], 0

    def verifier(condition, quoi):
        nonlocal controles
        controles += 1
        if not condition:
            ecarts.append(quoi)

    verifier((sortie.get("course"), sortie.get("classe")) == (entete.get("course"), entete.get("classe")),
             "course ou classe de la sortie différente de l'en-tête du journal")
    # (iii) effet des lignées : type de la loi du monde (« fixe » : monde sans effet) contre la sortie brute
    lignee_de = {d["sortie"]["identifiant"]: d["entrees"]["lignee"] for d in decisions if d["mecanisme"] == "reception"}
    effet_journal = {}
    for d in decisions:
        if d["mecanisme"] == "jugement":
            l = lignee_de.get(d["entrees"]["identifiant"])
            verifier(l is not None, f"jugement d'une carte sans réception : {d['entrees']['identifiant']}")
            effet_journal.setdefault(l, set()).add(objets[d["entrees"]["loi_monde"]]["type"] != "fixe")
    effet_sortie = {x["l"]: x["a_effet"] for x in sortie.get("lignees", [])}
    for l, v in sorted(effet_journal.items(), key=lambda x: str(x[0])):
        verifier(len(v) == 1 and effet_sortie.get(l) == next(iter(v)), f"effet de la lignée {l} : journal et sortie diffèrent")
    # (i) m de chaque promotion contre le registre ; (ii) arrêts contre la décision de promotion
    registre, derniere = {}, {}
    arrets = {}
    for d in decisions:
        nom, e, mec = _bras_de(d["partie"]), d["entrees"], d["mecanisme"]
        if nom is None:
            continue
        if mec == "registre":
            registre[nom] = d
            derniere.pop(nom, None)
            continue
        reg = registre.get(nom)
        if mec in ("promotion_e_bh", "promotion_bonferroni", "promotion_seule", "choix_c"):
            verifier(reg is not None and reg["entrees"]["generation"] == e["generation"],
                     f"{nom} : décision {mec} sans registre de la génération {e.get('generation')}")
            if reg is None:
                continue
            m_s = reg["entrees"]["m_s"]
            verifier(len(e["cartes"]) == m_s, f"{nom}, génération {e['generation']} : {len(e['cartes'])} cartes pour m_s = {m_s}")
            if mec == "promotion_e_bh":
                definition = e["definition_essai"]
                m_brut = m_s if definition == "cartes_jugees" else reg["sortie"]["m"].get(definition)
                verifier(e["m_s"] == m_s and e["m_brut"] == m_brut and e["m"] == max(m_brut if m_brut is not None else -1, m_s),
                         f"{nom}, génération {e['generation']} : m de la promotion ({e['m']}) ≠ m du registre "
                         f"pour la définition {definition}")
            if mec == "promotion_bonferroni":
                verifier(e["m_s"] == m_s, f"{nom}, génération {e['generation']} : m_s de la promotion ≠ m_s du registre")
            if mec != "choix_c":
                derniere[nom] = list(d["sortie"]["promues"])
            else:
                derniere[nom] = []
                derniere["choix|" + nom] = d["sortie"]["choisie"]
        elif mec == "promotion_c":
            derniere[nom] = [derniere.get("choix|" + nom)] if d["sortie"]["promue"] else []
        elif mec == "arret":
            verifier(nom in derniere, f"{nom}, génération {e['generation']} : arrêt sans décision de promotion")
            verifier([i for i, _ in e["promues"]] == derniere.get(nom),
                     f"{nom}, génération {e['generation']} : promues de l'arrêt ≠ sortie de la promotion")
            verifier(reg is not None and e["en_course"] == reg["entrees"]["lignees_en_course"],
                     f"{nom}, génération {e['generation']} : lignées en course de l'arrêt ≠ registre")
            arrets.setdefault(nom, []).append({"g": e["generation"], "en_course": list(e["en_course"]),
                                               "promues": [i for i, _ in e["promues"]]})
            derniere.pop(nom, None)
    # (ii) arrêts du journal contre la sortie brute (promotions, lignées en course, m), bras par bras
    bras_sortie = sortie.get("bras", {})
    verifier(sorted(arrets) == sorted(bras_sortie), "bras du journal ≠ bras de la sortie brute")
    for nom in sorted(set(arrets) & set(bras_sortie)):
        gens = bras_sortie[nom]["generations"]
        brut = [{"g": g["g"], "en_course": list(g["en_course"]), "promues": list(g["promues"])} for g in gens]
        verifier(arrets[nom] == brut, f"{nom} : promotions ou lignées en course du journal ≠ sortie brute")
    for d in decisions:
        nom = _bras_de(d["partie"])
        if d["mecanisme"] == "promotion_e_bh" and nom in bras_sortie:
            g = d["entrees"]["generation"]
            gen = next((x for x in bras_sortie[nom]["generations"] if x["g"] == g), {})
            verifier(gen.get("m") == d["entrees"]["m"] and gen.get("m_brut") == d["entrees"]["m_brut"],
                     f"{nom}, génération {g} : m de la sortie brute ≠ m du journal")
    return ecarts, controles


def m1_nul_depuis_journal(objets, decisions):
    """M1-nul de chaque bras recalculé depuis les seules décisions du journal : promues des décisions d'arrêt ; une carte
    est « sans effet » si la loi du monde de son jugement est de type « fixe ». Rend {bras: (V, R)} (pour comparaison
    seulement ; jamais écrit)."""
    lignee_de = {d["sortie"]["identifiant"]: d["entrees"]["lignee"] for d in decisions if d["mecanisme"] == "reception"}
    sans = set()
    for d in decisions:
        if d["mecanisme"] == "jugement" and objets[d["entrees"]["loi_monde"]]["type"] == "fixe":
            sans.add(lignee_de[d["entrees"]["identifiant"]])
    out = {}
    for d in decisions:
        nom = _bras_de(d["partie"])
        if nom is not None and d["mecanisme"] == "arret":
            V, R = out.get(nom, (0, 0))
            out[nom] = (V + sum(1 for _, l in d["entrees"]["promues"] if l in sans), R + len(d["entrees"]["promues"]))
    return out


def recouper_m1_nul(objets, decisions, sortie):
    """Pour l'audit de symétrie : M1-nul depuis le journal contre M1-nul de l'analyse (`analyse_ligne1_v2.mesures_course`)
    sur la sortie brute, bras par bras. Rend {bras: concordance (booléen)} ; aucune valeur."""
    import analyse_ligne1_v2 as AN
    du_journal = m1_nul_depuis_journal(objets, decisions)
    concorde = {}
    for nom in sorted(sortie.get("bras", {})):
        V, R = du_journal.get(nom, (0, 0))
        m1_j = V / R if R else 0.0
        concorde[nom] = (nom in du_journal) and m1_j == AN.mesures_course(sortie, nom, 0.0)["M1_nul"]
    return concorde


def rejouer_fichier(chemin, surcharges=None, *, lever=True, sortie=None, m1_nul=False):
    """Rejoue toutes les décisions d'un journal. Rend un compte rendu ; lève `GardeA16Rejeu` à la première différence si
    `lever` (sinon les différences sont comptées et rendues : essai 10). Si `sortie` (chemin de la sortie brute scellée)
    est donné, recoupe le journal avec elle (`GardeA16Recoupement` au premier écart) ; si `m1_nul`, recoupe aussi M1-nul."""
    surcharges = dict(surcharges or {})
    try:
        entete, objets, decisions = JL.lire(chemin)
    except JL.JournalRompu as e:
        raise GardeA16Rejeu(f"garde A16 : {e}") from e
    differentes, par_mecanisme = [], {}
    for d in decisions:
        try:
            rejouee = _rejouer_une(d, objets, entete, surcharges)
        except KeyError as e:
            raise GardeA16Rejeu(f"garde A16 : {os.path.basename(chemin)} : objet absent de la table ({e})") from e
        par_mecanisme[d["mecanisme"]] = par_mecanisme.get(d["mecanisme"], 0) + 1
        if JL.canonique(rejouee) != JL.canonique(d["sortie"]):
            differentes.append({"n": d["n"], "mecanisme": d["mecanisme"], "partie": d["partie"]})
            if lever:
                raise GardeA16Rejeu(f"garde A16 : {os.path.basename(chemin)}, ligne {d['n']} ({d['mecanisme']}, "
                                    f"{d['partie']}) : la décision rejouée diffère de la sortie journalisée")
    compte = {"fichier": os.path.basename(chemin), "course": entete["course"], "classe": entete["classe"],
              "decisions": len(decisions), "objets": len(objets), "par_mecanisme": par_mecanisme,
              "differentes": len(differentes), "premieres_differences": differentes[:20], "surcharges": surcharges}
    if sortie is not None:
        if not B.verifier_scelle_fichier(sortie):
            raise GardeA16Recoupement(f"garde A16 : sortie brute {os.path.basename(sortie)} absente ou non scellée")
        brute = B.lire_json_xz_verifie(sortie)
        ecarts, controles = recouper(entete, objets, decisions, brute)
        if ecarts:
            raise GardeA16Recoupement(f"garde A16 : {os.path.basename(chemin)} et {os.path.basename(sortie)} ne se recoupent "
                                      f"pas : {ecarts[:5]}")
        compte["recoupement"] = {"sortie": os.path.basename(sortie), "sortie_sha256": B.sha256_fichier(sortie),
                                 "controles": controles, "ecarts": 0}
        if m1_nul:
            concorde = recouper_m1_nul(objets, decisions, brute)
            if not all(concorde.values()):
                raise GardeA16Recoupement(f"garde A16 : M1-nul recalculé depuis le journal {os.path.basename(chemin)} ≠ "
                                          f"M1-nul de l'analyse, bras {sorted(k for k, v in concorde.items() if not v)}")
            compte["recoupement"]["m1_nul_concorde"] = concorde
    return compte


def journaux_du_dossier(dossier, courses=None):
    chemins = sorted(glob.glob(os.path.join(dossier, "journal-c*-*.jsonl.xz")))
    if courses is not None:
        voulues = {f"journal-c{c:04d}-" for c in courses}
        chemins = [c for c in chemins if os.path.basename(c)[:14] in voulues]
    return chemins


def _travail(args):
    chemin, surcharges, recouper_sortie, m1_nul = args
    if not B.verifier_scelle_fichier(chemin):
        raise GardeA16Rejeu(f"garde A16 : {os.path.basename(chemin)} non scellé ou modifié")
    return rejouer_fichier(chemin, surcharges, sortie=sortie_de_journal(chemin) if recouper_sortie else None, m1_nul=m1_nul)


def rejouer_dossier(dossier, processus=1, courses=None, attendus=None, recouper_sortie=True, m1_nul=False):
    """Rejoue tous les journaux d'un dossier (ou ceux des `courses` données). `attendus` : nombre de journaux attendu
    (deux par course) ; un journal manquant lève `GardeA16Rejeu`. Chaque journal est recoupé avec sa sortie brute
    (`recouper_sortie`, défaut vrai : une sortie absente lève `GardeA16Recoupement`) ; `m1_nul` recoupe aussi M1-nul
    (courses de l'audit de symétrie). Rend le compte rendu (à sceller par l'appelant)."""
    import concurrent.futures
    import multiprocessing
    chemins = journaux_du_dossier(dossier, courses)
    if attendus is not None and len(chemins) != attendus:
        raise GardeA16Rejeu(f"garde A16 : {len(chemins)} journaux trouvés, {attendus} attendus")
    taches = [(c, None, recouper_sortie, m1_nul) for c in chemins]
    if processus > 1:
        with concurrent.futures.ProcessPoolExecutor(processus, mp_context=multiprocessing.get_context("fork")) as ex:
            comptes = list(ex.map(_travail, taches, chunksize=4))
    else:
        comptes = [_travail(t) for t in taches]
    rapport = {"version": VERSION, "journaux": len(comptes), "decisions": sum(c["decisions"] for c in comptes),
               "differentes": sum(c["differentes"] for c in comptes), "par_fichier": comptes,
               "verdict": "identique au bit près" if all(c["differentes"] == 0 for c in comptes) else "différences"}
    if recouper_sortie:
        rapport["recoupement"] = {"journaux": sum(1 for c in comptes if "recoupement" in c),
                                  "controles": sum(c.get("recoupement", {}).get("controles", 0) for c in comptes),
                                  "verdict": "concordant" if all(c.get("recoupement", {}).get("ecarts") == 0 for c in comptes)
                                  else "non recoupé"}
        if m1_nul:
            rapport["recoupement"]["m1_nul"] = "concordant" if all(
                all(c["recoupement"].get("m1_nul_concorde", {"?": False}).values()) for c in comptes) else "non recoupé"
    return rapport


def main(argv=None):
    import argparse
    import etalonnage_ligne1_v2 as E          # chemin de la configuration v2 et liste des fichiers du code v2
    p = argparse.ArgumentParser(description="Rejeu du journal scellé du banc A, ligne 1 (garde A16), code v2.")
    p.add_argument("--dossier", required=True)
    p.add_argument("--organisme", required=True, help="dossier orchestrator/ du dépôt de l'organisme (lecture seule)")
    p.add_argument("--courses", default=None, help="liste de courses, par exemple 0,300,599 (audit de symétrie)")
    p.add_argument("--processus", type=int, default=1)
    p.add_argument("--sortie", required=True, help="compte rendu JSON, nom neuf, scellé")
    a = p.parse_args(argv)
    B.verifier_preenregistrement()
    config, _ = B.charger_configuration(E.CHEMIN_CONFIGURATION)
    B.charger_organisme(a.organisme, config)
    courses = [int(x) for x in a.courses.split(",")] if a.courses else None
    rapport = rejouer_dossier(a.dossier, a.processus, courses, m1_nul=courses is not None)
    B.ecrire_json_scelle(a.sortie, rapport)
    print(rapport["verdict"], rapport["journaux"], "journaux", rapport["decisions"], "décisions")


if __name__ == "__main__":
    main()
