"""Mesure de temps et de mémoire de l'étape 8 sous la couche « essai-de-forme » (permission de la mère, 17:41Z) — aucun tirage
décisif, processeur seul, aucune sortie lue au-delà de son existence et de sa taille en octets.

Arguments : nombre de tirages par case du mode « tirages », nombre de sources par case du mode « sources », dossier de travail
neuf, fichier JSON de résultat neuf. Lancé depuis une copie du code v6 (dossier courant : celui qui porte `src/`), avec
`PYTHONPATH=src` et `-B`. Le programme :
1. éprouve d'abord le verrou : une graine de chacune des couches « decisif » et « confirmation », demandée sans autorisation,
   doit être refusée (`GraineRefusee`), sans rien dériver ;
2. écrit des fichiers gelés factices (fréquences d'essai ; réglages plantés, toutes cibles atteignables : 89 cases) — jamais
   ceux des étapes 5 et 6 ;
3. joue `etapes.etape_8` sous la couche « essai-de-forme », la seule qu'il accepte, aux tailles réduites données (`tailles`) ;
4. mesure le temps écoulé de l'appel (`time.perf_counter`) et la mémoire résidente maximale du processus
   (`resource.getrusage(RUSAGE_SELF).ru_maxrss`, en Kio sous Linux), avant et après ;
5. relève, sans les ouvrir, la taille en octets des fichiers écrits (`os.path.getsize`), séparément pour les cases du mode
   « tirages », celles du mode « sources » (nom en `-sources`) et le manifeste ;
6. contrôle qu'aucune couche autre que « essai-de-forme » n'a été dérivée.

Version 2 : relève en plus l'état du cache de la loi exacte du test des rangs signés (`rangs_signes._loi_exacte.cache_info()` :
nombre d'entrées, plafond, succès, échecs) — un état interne du code, non une sortie de l'étape 8 —, parce que la première
série (version 1) a montré une mémoire résidente qui croît avec le nombre de tirages.
"""

import json
import os
import resource
import sys
import time

from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import rangs_signes as RS
from controle_ia.heritage_etage_processeur_v1.constantes import CLASSES

COUCHE = "essai-de-forme"
TIRAGES, SOURCES, TRAVAIL, RESULTAT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
FREQUENCES = {"p_tient_vraie_source": 1.0, "p_tient_vraie_cible": 1.0, "p_tient_fausse": 0.15, "p_tient_non_plantee_base": 0.02,
              "p_tient_non_plantee_composition": 0.8, "p_tient_non_plantee_copie": 0.05, "p_passage_vraie": 1.0,
              "p_faux_passage": 0.4}
VALEURS = {"K": lambda t: 32.0 * t, "tau": lambda t: 0.9 * t, "phi": lambda t: {0.5: 0.4, 1.0: 0.9, 1.5: 1.5}[t],
           "gamma": lambda t: {0.25: 0.1, 0.5: 0.2, 1.0: 0.5, 1.5: 0.9}[t]}


def rss_kio():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


def main():
    if COUCHE != "essai-de-forme" or TIRAGES > 200 or TIRAGES < 1 or SOURCES < 2:
        raise SystemExit("couche ou tailles hors de la mesure permise")
    # 1. le verrou refuse les couches décisives, sans rien dériver
    g0 = GR.Graines()
    for couche in GR.COUCHES_DECISIVES:
        try:
            g0.g(couche=couche, famille="mesure-etape-8", role="verrou")
            raise SystemExit(f"le verrou n'a pas refusé la couche {couche} : arrêt")
        except GR.GraineRefusee:
            pass
    if g0.etiquettes or set(GR.couches_derivees()) - {COUCHE}:
        raise SystemExit("une graine a été dérivée hors de la couche « essai-de-forme » : arrêt")
    # 2. fichiers gelés factices
    os.makedirs(TRAVAIL)
    geles = os.path.join(TRAVAIL, "geles-factices")
    os.makedirs(geles)
    comptes = {"vraie-source": {"engagees": 4, "tiennent": 4},
               "criblage": {"vraies_examinees": 2, "vraies_retenues": 2, "autres_examinees": 5, "autres_passees": 2},
               "tentatives_par_classe": {c: 1 for c in CLASSES}}
    cf, cr = os.path.join(geles, "frequences-factices.json"), os.path.join(geles, "reglages-factices.json")
    sf = FR.geler(cf, FREQUENCES, comptes, {"factice": True})
    lignes = [{"proposeur": nom, "nom_du_reglage": r, "dose": dose, "cible": cible, "reglage": VALEURS[r](cible),
               "atteignable": True, "statut": "atteint"} for nom, r, dose, cible in EP.cibles_d_etalonnage()]
    sr = ET.geler_reglages(cr, lignes, {"factice": True})
    # 3. et 4. l'étape 8, mesurée
    g = GR.Graines()
    dossier = os.path.join(TRAVAIL, "etape-8")
    rss_avant = rss_kio()
    t0 = time.perf_counter()
    r = EP.etape_8(g, dossier, "0" * 40, cf, sf, cr, sr, couche=COUCHE, tailles={"tirages": TIRAGES, "sources": SOURCES})
    duree = time.perf_counter() - t0
    rss_apres = rss_kio()
    # 5. tailles en octets, sans rien ouvrir
    octets = {"tirages": 0, "sources": 0, "manifeste": 0}
    fichiers = 0
    for racine, _, noms in os.walk(dossier):
        rel = os.path.relpath(racine, dossier)
        cle = "manifeste" if rel == "." else ("sources" if rel.split(os.sep)[0].endswith("-sources") else "tirages")
        for n in noms:
            octets[cle] += os.path.getsize(os.path.join(racine, n))
            fichiers += 1
    # 6. aucune autre couche dérivée
    couches = GR.couches_derivees()
    if couches != [COUCHE]:
        raise SystemExit(f"couches dérivées inattendues : {couches} : arrêt")
    cases = sorted(r["cases"])
    out = {"couche": COUCHE, "tirages_par_case": TIRAGES, "sources_par_case": SOURCES, "cases": len(cases),
           "cases_tirages": sum(1 for c in cases if not c.endswith("-sources")),
           "cases_sources": sum(1 for c in cases if c.endswith("-sources")), "duree_etape_8_s": round(duree, 2),
           "rss_max_avant_kio": rss_avant, "rss_max_apres_kio": rss_apres, "octets": octets, "fichiers": fichiers,
           "etiquettes": len(g.etiquettes), "couches_derivees": couches,
           "cache_loi_exacte": RS._loi_exacte.cache_info()._asdict()}
    with open(RESULTAT, "x", encoding="utf-8") as fh:
        fh.write(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    print(json.dumps(out, ensure_ascii=False, sort_keys=True))


main()
