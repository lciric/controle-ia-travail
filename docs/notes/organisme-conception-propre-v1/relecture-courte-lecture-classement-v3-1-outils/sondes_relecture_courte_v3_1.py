#!/usr/bin/env python3
"""Sondes neuves du contre-lecteur (modèle B) — relecture courte de l'outil du lecteur v3.1.

Jouées sur une copie non modifiée de l'outil et du classement v3.1 (`LC_MODULES`, bloc-notes), avec les doublures et les
fiches factices des essais de l'auteur (importés comme bibliothèque). Aucune fiche réelle ni aucun témoin ouvert ou
affiché ; aucune clé réelle ; à lancer sous `unshare -n` (aucune sonde de ce fichier n'ouvre de connexion).

    LC_MODULES=… TMPDIR=… unshare -n .venv/bin/python -B sondes_relecture_courte_v3_1.py SORTIE.json
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import sys
import tempfile
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
V31 = ICI.parent / "lecture-classement-v3-1"


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


E = charger("essais_v3_1_bibliotheque_relecture", V31 / "essais_lecture_classement_v3_1.py")
O = E.O


class MP:
    def setenv(self, k, v):
        os.environ[k] = v


def plan(n):
    return {f"B{i}": ("propa", "levier:cout", "ajout", "processeur", {}) for i in range(n)}


# --- p1 : la garde au plafond de 9,30 USD, palier Flex, sur les hypothèses du devis v2 ------------------------------------

def p1(tmp):
    """Boucle de la garde rejouée avec les fonctions de l'outil (`pire_cas_usd`, `cout_usage`, prix Flex du code) sur les
    volumes du devis v2 (octets 49 900 et 45 850 ; entrée 15 000 et 13 800 jetons ; sortie `medium` 17 000 et 13 600),
    la sortie multipliée par un facteur f ; ordre du manifeste : sept lots de 5 puis deux de 4, deux fois."""
    prix = {**O.PRIX_LUS["flex"], "source": "sonde"}
    lots = ([5] * 7 + [4] * 2) * 2
    octets = {5: 49900, 4: 45850}
    entree = {5: 15000, 4: 13800}
    sortie = {5: 17000, 4: 13600}
    res = {"pire_cas_lot_de_5": round(O.pire_cas_usd(octets[5], prix), 6),
           "pire_cas_lot_de_4": round(O.pire_cas_usd(octets[4], prix), 6), "scenarios": {}}
    for plafond in (9.30, 14.20):
        for nom, f, cache in (("sortie_du_devis", 1.0, 0), ("sortie_plus_1_pour_cent", 1.01, 0),
                              ("sortie_plus_5_pour_cent", 1.05, 0), ("sortie_plus_20_pour_cent", 1.20, 0),
                              ("sortie_plus_50_pour_cent", 1.50, 0),
                              ("sortie_plus_5_pour_cent_preambule_en_cache", 1.05, 8900)):
            depense, partis, arret = 0.0, 0, None
            for k, n in enumerate(lots, 1):
                pire = O.pire_cas_usd(octets[n], prix)
                if depense + pire > plafond + 1e-12:
                    arret = k
                    break
                c = min(O.MAX_SORTIE, round(sortie[n] * f))
                u = {"prompt_tokens": entree[n], "completion_tokens": c, "total_tokens": entree[n] + c,
                     "prompt_tokens_details": {"cached_tokens": cache if k > 1 else 0},
                     "completion_tokens_details": {"reasoning_tokens": c - 400 * n}}
                cout, pb, _ = O.cout_usage(u, prix, octets[n], 1600 * n)
                assert pb is None, pb
                depense += round(cout, 6)
                partis += 1
            res["scenarios"][f"plafond_{plafond:.2f}_{nom}"] = {
                "appels_partis": partis, "arret_avant_l_appel": arret, "depense_comptee_usd": round(depense, 6),
                "lecture_complete": partis == 18}
    # seuil : plus grande dépense des 17 premiers appels qui laisse partir le 18e
    res["depense_maximale_des_17_premiers_pour_9_30"] = round(9.30 - O.pire_cas_usd(octets[4], prix), 6)
    res["depense_attendue_des_17_premiers_au_devis"] = round(
        sum((entree[n] * 5 + sortie[n] * 25) / 1e6 for n in lots[:17]), 6)
    return res


# --- p2 : bout en bout au palier Flex, plafond 9,30, pile de 43 fiches factices -------------------------------------------

def p2(tmp):
    env, man = E.preparer(tmp / "p2", E.fiches_factices(plan(23), hors=False), palier="flex", plafond_usd=9.30)
    corps = [json.loads((env / n).read_text(encoding="utf-8")) for n in man["ordre_d_envoi"]]
    ancien = dict(E.PLAN)
    E.PLAN.update(plan(23))  # le lecteur simulé des essais cherche chaque fiche factice dans ce plan
    try:
        r, d = E.envoyer(env, MP())
    finally:
        E.PLAN.clear()
        E.PLAN.update(ancien)
    b = O.bilan(env)
    v = E.classer(env)
    return {"pile": man["pile"]["fiches"], "lots": man["lots"]["tailles"], "palier_au_manifeste": man["palier"],
            "prix_au_manifeste": {k: man["garde_depense"]["prix_usd_par_million"][k] for k in ("entree", "cache", "sortie")},
            "plafond_au_manifeste": man["garde_depense"]["plafond_usd"],
            "service_tier_dans_les_18_corps": sorted({c.get("service_tier") for c in corps}),
            "cles_des_corps": sorted(set(corps[0])), "issue": r["issue"], "appels": r["appels"],
            "paliers_servis_consignes": sorted({c["palier_servi"] for c in b["clotures"]}),
            "pret_pour_verifier": b["pret_pour_verifier"], "verdict_commence_par": v["verdict"][:30],
            "lecture_complete": v["lecture_complete"]["complete"]}


# --- p3 : palier servi, formes ---------------------------------------------------------------------------------------------

def p3(tmp):
    res = {}
    for palier in ("flex", "standard"):
        prix = {**O.PRIX_LUS[palier], "source": "sonde"}
        for servi in ("flex", "default", None, "Flex", "flex ", "priority", ["flex"], "auto", "standard", "scale"):
            base = {"object": "chat.completion", "model": "gpt-6-astra",
                    "usage": {"prompt_tokens": 9000, "completion_tokens": 3000, "total_tokens": 12000},
                    "choices": [{"index": 0, "message": {"content": "x" * 4000, "refusal": None},
                                 "finish_reason": "stop"}]}
            if servi is not None:
                base["service_tier"] = servi
            a = O.analyser_reponse(200, json.dumps(base).encode(), 1.2, prix, 36000, palier)
            res[f"demande_{palier}_servi_{servi!r}"] = {"anomalies": a["anomalies"], "cout_usd": round(a["cout_usd"], 6),
                                                        "au_pire_cas": a["au_pire_cas"]}
    return res


# --- p4 : arrêt au premier appel (429 du palier Flex), puis tentatives de reprise -----------------------------------------

def p4(tmp):
    base = tmp / "p4"
    pf, h = E.ecrire_fiches(base, E.fiches_factices())
    pa = E.ecrire_attestation(base, h)
    rac = E.racine_de(base)
    fixe = E.envois_de(rac)
    E.opreparer(pf, pa, fixe, rac, palier="flex", plafond_usd=9.30)
    r1, d1 = E.envoyer(fixe, MP(), scenarios={1: "429"})
    res = {"premier_appel": {"issue": r1["issue"], "detail": r1["detail"], "depense_comptee_usd": r1["depense_comptee_usd"]},
           "tentatives": {}}

    def tente(nom, geste):
        try:
            r = geste()
            res["tentatives"][nom] = {"permis": True, "detail": str(r)[:100]}
        except O.Refus as e:
            res["tentatives"][nom] = {"refus": str(e)[:150]}
    tente("reprise_de_l_envoi", lambda: E.envoyer(fixe, MP())[0]["issue"])
    tente("seconde_preparation_au_meme_chemin", lambda: E.opreparer(pf, pa, fixe, rac, palier="flex", plafond_usd=9.30)["palier"])
    # dossier arrêté déplacé hors de docs/ et de runs/ (sous la racine), puis préparation neuve sans rien déclarer
    (rac / "archives").mkdir()
    shutil.move(str(fixe.parent), str(rac / "archives" / "lecture-g1-v3-1-arretee"))
    tente("preparation_apres_deplacement_hors_de_docs_sans_depense_declaree",
          lambda: E.opreparer(pf, pa, fixe, rac, palier="flex", plafond_usd=9.30)["garde_depense"]["depense_anterieure_usd"])
    if res["tentatives"]["preparation_apres_deplacement_hors_de_docs_sans_depense_declaree"].get("permis"):
        r2, d2 = E.envoyer(fixe, MP())
        res["apres_deplacement"] = {"issue": r2["issue"], "appels": r2["appels"],
                                    "depense_comptee_usd": r2["depense_comptee_usd"],
                                    "depense_du_dossier_arrete_comptee": False}
    return res


# --- p5 : filtre de la clé --------------------------------------------------------------------------------------------------

def p5(tmp):
    res = {}
    for nom, cle in (("propre", "sk-sonde-factice-0123456789"), ("513_caracteres", "k" * 513), ("512_caracteres", "k" * 512),
                     ("saut_de_ligne_interne", "sk-a\nb"), ("retour_chariot_final", "sk-a\r"), ("espace_initial", " sk-a"),
                     ("caractere_7f", "sk-a\x7f"), ("non_ascii", "sk-é"), ("vide", ""), ("guillemets", '"sk-a"')):
        os.environ["OPENAI_API_KEY"] = cle
        try:
            O.lire_cle()
            res[nom] = "acceptée"
        except O.Refus as e:
            res[nom] = "refusée" + (" (la clé est dans le message !)" if cle and cle.strip() and cle.strip() in str(e) else "")
        res[nom] += " ; retirée de l'environnement" if "OPENAI_API_KEY" not in os.environ else " ; restée dans l'environnement"
        os.environ.pop("OPENAI_API_KEY", None)
    return res


# --- p6 : unicité, formes de noms -------------------------------------------------------------------------------------------

def p6(tmp):
    res = {}
    for nom, rel in (("manifeste_v3_sous_runs", "runs/x/manifeste-envois-v3.json"),
                     ("manifeste_v3_1_sous_docs_ailleurs", "docs/y/manifeste-envois-v3-1.json"),
                     ("manifeste_v3_1_renomme_bak", "docs/y/manifeste-envois-v3-1.json.bak"),
                     ("manifeste_v3_1_sous_archives_hors_docs", "archives/z/manifeste-envois-v3-1.json")):
        base = tmp / f"p6-{nom}"
        env, _ = E.preparer(base)
        p = E.racine_de(base) / rel
        p.parent.mkdir(parents=True)
        p.write_text("{}", encoding="utf-8")
        try:
            O.bilan(env)
            res[nom] = "non vu (bilan rendu)"
        except O.Refus as e:
            res[nom] = "refus : " + str(e)[:70]
    return res


def main(sortie):
    res = {"sondes": "relecture courte de l'outil du lecteur v3.1, sondes neuves (contre-lecteur, modèle B)",
           "debut_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "outil_sha256": O.sha256_fichier(E.MODS / "outil_lecteur_conception_propre_v3_1.py"),
           "classer_sha256": O.sha256_fichier(E.MODS / "classer_conception_propre_v3_1.py"), "resultats": {}}
    with tempfile.TemporaryDirectory(prefix="sondes-rc-v3-1-") as tmp:
        for nom, f in (("p1_garde_a_9_30_palier_flex", p1), ("p2_bout_en_bout_flex_9_30", p2), ("p3_palier_servi", p3),
                       ("p4_arret_au_premier_appel_puis_reprise", p4), ("p5_filtre_de_la_cle", p5), ("p6_unicite", p6)):
            try:
                res["resultats"][nom] = f(Path(tmp))
            except Exception as ex:
                res["resultats"][nom] = {"sonde_en_echec": f"{type(ex).__name__}: {str(ex)[:300]}"}
            os.environ.pop("OPENAI_API_KEY", None)
    res["fin_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["resultats"], ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
