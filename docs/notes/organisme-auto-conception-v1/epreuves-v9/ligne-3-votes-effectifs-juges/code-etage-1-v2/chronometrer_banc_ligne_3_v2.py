"""Chronométrage de l'étage 1 de la ligne 3 — n'imprime que des durées — v2.

Version 2 : charge le banc v2 (correction C2 de la contre-lecture, sans effet sur les durées) ; manifeste nommé en v2.
Aucun autre changement.

Joue, pour chaque pièce du banc, un échantillon de répliques à la taille de rééchantillonnage de la configuration
décisive, mesure la durée, et l'extrapole au nombre de cellules et de répliques de l'exécution décisive. Il n'imprime
que des lignes « duree_<pièce>_secondes: <durée> » ; aucun résultat, aucun chiffre du banc. Il écrit un manifeste
(R9) dans le dossier donné.

Usage :
  chronométrage décisif (racine 2026111931 ; geste 4 seulement, après l'additif de code scellé ; jamais lancé par le
  développeur) :
    python3 -B chronometrer_banc_ligne_3_v2.py --autorisation-additif CHEMIN --empreinte-additif HEX --manifeste DOSSIER
  essai du code (racine des essais 2026111930, tailles réduites permises) :
    python3 -B chronometrer_banc_ligne_3_v2.py --essai --manifeste DOSSIER [--repliques-echantillon K] [--tirages-essai B]
Développeur, modèle L′.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import os
import sys
import time
from pathlib import Path

NOM_BANC = "banc_juges_scriptes_ligne_3_v2"


def charger_banc():
    if NOM_BANC in sys.modules:
        return sys.modules[NOM_BANC]
    chemin = Path(os.environ.get("BANC_LIGNE_3_CHEMIN", str(Path(__file__).resolve().parent / f"{NOM_BANC}.py")))
    spec = importlib.util.spec_from_file_location(NOM_BANC, chemin)
    module = importlib.util.module_from_spec(spec)
    sys.modules[NOM_BANC] = module
    spec.loader.exec_module(module)
    return module


def _mesurer(fonction):
    debut = time.perf_counter()
    fonction()
    return time.perf_counter() - debut


def chronometrer(banc, contexte, r, B):
    """Rend une liste ordonnée (nom, durée en secondes) : durées mesurées et durées extrapolées."""
    cfg = banc.CONFIGURATION_DECISIVE
    R_plein = cfg["repliques"]
    facteur = R_plein / r
    durees = []

    # Estimateur et agrégation : une cellule par (J, loi, n), ρ = 0,45, profil de la règle (ou le seul joué).
    cellules = banc.enumerer_cellules_estimateur(cfg)
    familles = sorted({(J, loi, n) for (J, loi, _nom, _rho, n) in cellules})
    gt = contexte.tirages("estimateur_et_agregation", len(familles))
    gr = contexte.reechantillonnage("reechantillonnage_estimateur_et_agregation", len(familles))
    total_e = 0.0
    for i, (J, loi, n) in enumerate(familles):
        d = _mesurer(lambda: banc.cellule_estimateur_agregation(gt[i], gr[i], loi, J, "egal_0.2", 0.45, n, r, B))
        nombre = sum(1 for c in cellules if (c[0], c[1], c[4]) == (J, loi, n))
        total_e += d * facteur * nombre
    durees.append(("estimee_estimateur_et_agregation", total_e))

    # Monde de puissance : une cellule faisable, extrapolée au nombre de cellules faisables.
    cp = cfg["puissance"]
    faisables = 0
    for (comp, ec, loi, rho, rp) in banc.enumerer_cellules_puissance(cp):
        d_ = banc.resoudre_dissymetrie(comp, ec, rho, rp)
        if d_ is None:
            continue
        if loi == 3 and not (banc.loi_3_jouable(0.2 + d_, rho) and banc.loi_3_jouable(0.2 - d_, rho)):
            continue
        faisables += 1
    gt = contexte.tirages("monde_de_puissance", 1)
    gr = contexte.reechantillonnage("reechantillonnage_monde_de_puissance", 1)
    d = _mesurer(lambda: banc.cellule_puissance(gt[0], gr[0], "unanimite", 0.10, 1, 0.0, 0.0, r, B))
    durees.append(("estimee_monde_de_puissance", d * facteur * faisables))

    cr = cfg["ecart_rho_prime"]
    nombre_r = sum(1 for ec in cr["ecarts"] for rho in cr["rhos"] if rho + ec <= 1.0 + 1e-12)
    gt = contexte.tirages("ecart_rho_prime_moins_rho", 1)
    gr = contexte.reechantillonnage("reechantillonnage_ecart_rho_prime_moins_rho", 1)
    d = _mesurer(lambda: banc.cellule_ecart_rho_prime(gt[0], gr[0], 0.3, 0.3, r, B))
    durees.append(("estimee_ecart_rho_prime_moins_rho", d * facteur * nombre_r))

    cd = cfg["double_rendu"]
    gt = contexte.tirages("double_rendu", len(cd["n"]))
    gr = contexte.reechantillonnage("reechantillonnage_double_rendu", len(cd["n"]))
    total_d = 0.0
    for i, n in enumerate(cd["n"]):
        d = _mesurer(lambda: banc.cellule_double_rendu(gt[i], gr[i], n, 0.5, 0.5, r, B))
        total_d += d * facteur * len(cd["s"]) * len(cd["deltas"])
    durees.append(("estimee_double_rendu", total_d))

    cc = cfg["cadrage"]
    gt = contexte.tirages("garde_de_cadrage", len(cc["t"]))
    total_c = 0.0
    for i, t in enumerate(cc["t"]):
        d = _mesurer(lambda: banc.cellule_cadrage(gt[i], t, 0.5, r))
        total_c += d * facteur * len(cc["deltas"])
    durees.append(("estimee_garde_de_cadrage", total_c))

    ca = cfg["alarme"]
    gt = contexte.tirages("alarme", len(ca["m"]))
    total_a = 0.0
    for i, m in enumerate(ca["m"]):
        d = _mesurer(lambda: banc.cellule_alarme(gt[i], m, max(4, r)))
        total_a += d * ca["suites"] / max(4, r)
    durees.append(("estimee_alarme", total_a))

    durees.append(("estimee_totale", sum(x for _, x in durees)))
    return durees


def main(argv=None):
    banc = charger_banc()
    parser = argparse.ArgumentParser(description="Chronométrage de l'étage 1 (n'imprime que des durées).")
    parser.add_argument("--essai", action="store_true")
    parser.add_argument("--autorisation-additif")
    parser.add_argument("--empreinte-additif")
    parser.add_argument("--manifeste", required=True)
    parser.add_argument("--repliques-echantillon", type=int, default=20)
    parser.add_argument("--tirages-essai", type=int, default=None)
    args = parser.parse_args(argv)
    if args.essai:
        contexte = banc.Contexte("essais")
        B = args.tirages_essai or banc.CONFIGURATION_DECISIVE["tirages_reechantillonnage"]
    else:
        if args.tirages_essai is not None:
            raise banc.RefusExecution("--tirages-essai n'est permis qu'en essai")
        autorisation = banc.Autorisation(args.autorisation_additif or "", args.empreinte_additif)
        banc.verifier_autorisation(autorisation, banc.RACINE_CHRONOMETRAGE)
        contexte = banc.Contexte("chronometrage", autorisation)
        B = banc.CONFIGURATION_DECISIVE["tirages_reechantillonnage"]
    dossier = Path(args.manifeste)
    if dossier.exists():
        raise banc.RefusExecution(f"dossier du manifeste déjà présent : {dossier}")
    r = args.repliques_echantillon
    if r < 1:
        raise banc.RefusExecution("--repliques-echantillon doit être au moins 1")
    debut = datetime.datetime.now(datetime.timezone.utc)
    t0 = time.perf_counter()
    durees = chronometrer(banc, contexte, r, B)
    mesuree = time.perf_counter() - t0
    fin = datetime.datetime.now(datetime.timezone.utc)
    dossier.mkdir(parents=True, exist_ok=False)
    cfg = {"repliques_echantillon": r, "tirages_reechantillonnage": B,
           "configuration_decisive_sha256": banc.sha256_json(banc._nettoyer(banc.CONFIGURATION_DECISIVE))}
    manifeste = banc.construire_manifeste(contexte, cfg, debut, fin, {})
    manifeste["programme_chronometrage_sha256"] = banc.sha256_fichier(Path(__file__).resolve())
    banc.ecrire_json_exclusif(dossier / "manifeste-chronometrage-ligne-3-v2.json", manifeste)
    print(f"duree_mesuree_du_chronometrage_secondes: {mesuree:.3f}")
    for nom, valeur in durees:
        print(f"duree_{nom}_secondes: {valeur:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
