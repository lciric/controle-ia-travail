"""Rejeu du journal scellé du banc A, ligne 1 (version 1) — garde A16.

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

VERSION = "rejouer-journal-ligne1-v1"


class GardeA16Rejeu(B.ArretBanc):
    pass


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


def rejouer_fichier(chemin, surcharges=None, *, lever=True):
    """Rejoue toutes les décisions d'un journal. Rend un compte rendu ; lève `GardeA16Rejeu` à la première différence si
    `lever` (sinon les différences sont comptées et rendues : essai 10)."""
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
    return {"fichier": os.path.basename(chemin), "course": entete["course"], "classe": entete["classe"],
            "decisions": len(decisions), "objets": len(objets), "par_mecanisme": par_mecanisme,
            "differentes": len(differentes), "premieres_differences": differentes[:20], "surcharges": surcharges}


def journaux_du_dossier(dossier, courses=None):
    chemins = sorted(glob.glob(os.path.join(dossier, "journal-c*-*.jsonl.xz")))
    if courses is not None:
        voulues = {f"journal-c{c:04d}-" for c in courses}
        chemins = [c for c in chemins if os.path.basename(c)[:14] in voulues]
    return chemins


def _travail(args):
    chemin, surcharges = args
    if not B.verifier_scelle_fichier(chemin):
        raise GardeA16Rejeu(f"garde A16 : {os.path.basename(chemin)} non scellé ou modifié")
    return rejouer_fichier(chemin, surcharges)


def rejouer_dossier(dossier, processus=1, courses=None, attendus=None):
    """Rejoue tous les journaux d'un dossier (ou ceux des `courses` données). `attendus` : nombre de journaux attendu
    (deux par course) ; un journal manquant lève `GardeA16Rejeu`. Rend le compte rendu (à sceller par l'appelant)."""
    import concurrent.futures
    import multiprocessing
    chemins = journaux_du_dossier(dossier, courses)
    if attendus is not None and len(chemins) != attendus:
        raise GardeA16Rejeu(f"garde A16 : {len(chemins)} journaux trouvés, {attendus} attendus")
    if processus > 1:
        with concurrent.futures.ProcessPoolExecutor(processus, mp_context=multiprocessing.get_context("fork")) as ex:
            comptes = list(ex.map(_travail, [(c, None) for c in chemins], chunksize=4))
    else:
        comptes = [_travail((c, None)) for c in chemins]
    return {"version": VERSION, "journaux": len(comptes), "decisions": sum(c["decisions"] for c in comptes),
            "differentes": sum(c["differentes"] for c in comptes), "par_fichier": comptes,
            "verdict": "identique au bit près" if all(c["differentes"] == 0 for c in comptes) else "différences"}


def main(argv=None):
    import argparse
    p = argparse.ArgumentParser(description="Rejeu du journal scellé du banc A, ligne 1 (garde A16).")
    p.add_argument("--dossier", required=True)
    p.add_argument("--organisme", required=True, help="dossier orchestrator/ du dépôt de l'organisme (lecture seule)")
    p.add_argument("--courses", default=None, help="liste de courses, par exemple 0,300,599 (audit de symétrie)")
    p.add_argument("--processus", type=int, default=1)
    p.add_argument("--sortie", required=True, help="compte rendu JSON, nom neuf, scellé")
    a = p.parse_args(argv)
    B.verifier_preenregistrement()
    config, _ = B.charger_configuration()
    B.charger_organisme(a.organisme, config)
    courses = [int(x) for x in a.courses.split(",")] if a.courses else None
    rapport = rejouer_dossier(a.dossier, a.processus, courses)
    B.ecrire_json_scelle(a.sortie, rapport)
    print(rapport["verdict"], rapport["journaux"], "journaux", rapport["decisions"], "décisions")


if __name__ == "__main__":
    main()
