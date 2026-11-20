"""Chronométrage de la mesure de la portée à 200 de la ligne 3 — n'imprime que des durées — v1.

Additif 3 v3 (`prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md`, 71b7a876…),
§ 5, point 7 : il précède l'exécution décisive, dérive la seule racine 2026112031 (clés 2 et 12, `.spawn(210)`),
n'imprime et n'écrit que des durées, aucune puissance. La durée n'est ni un critère ni une garde d'arrêt (additif 1,
point J). Fait sur le modèle de `chronometrer_banc_ligne_3_v3.py` (partie « monde de puissance »), avec le banc v4.

Il joue une cellule faisable du monde de puissance (la première faisable à l'écart de 0,10 dans l'ordre gelé :
unanimité, loi 1, ρ = 0), à n = 200, sur un échantillon de répliques et à la taille de rééchantillonnage de la
configuration gelée, avec l'enfant de rang fixe de cette cellule ; il extrapole la durée au nombre de cellules
faisables de la configuration gelée et à son nombre de répliques. Il n'imprime que des lignes
« duree_<pièce>_secondes: <durée> » ; aucun résultat, aucun chiffre du banc. Il écrit un manifeste (R9) dans le
dossier donné, qui n'existe pas encore et n'est pas sous le dossier du code.

Usage :
  chronométrage (racine 2026112031 ; après l'additif de code de la mesure scellé ; jamais lancé par le développeur ;
  depuis le dossier du code, avec PYTHONDONTWRITEBYTECODE=1, sans variable d'environnement de chemin) :
    python3 -B chronometrer_portee_200_ligne_3_v1.py --autorisation-additif CHEMIN --empreinte-additif HEX \
        --manifeste DOSSIER
  essai du code (racine des essais 2026111930, tailles réduites permises) :
    python3 -B chronometrer_portee_200_ligne_3_v1.py --essai --manifeste DOSSIER [--repliques-echantillon K] \
        [--tirages-essai B]
Hors essai, avant toute dérivation : variables d'environnement de chemin non posées ; autorisation juste ; dossier du
code propre (git status --porcelain borné au dossier, dépôt git, manifeste hors du dossier du code) ; dossier du
manifeste neuf.

Développeur, modèle O.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import os
import sys
import time
from pathlib import Path

NOM_BANC = "banc_juges_scriptes_ligne_3_v4"
FICHIER_MANIFESTE = "manifeste-chronometrage-portee-200-ligne-3-v1.json"


def charger_banc():
    """Le banc v4 à côté de ce fichier ; la variable BANC_LIGNE_3_CHEMIN n'est lue qu'en essai (hors essai, elle
    doit être absente : refus avant tout)."""
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


def cellules_faisables(banc, cfg_puissance):
    """Rangs, dans l'ordre gelé, des cellules faisables (formule seule, aucun tirage)."""
    rangs = []
    for rang, (comp, ec, loi, rho, rp) in enumerate(banc.enumerer_cellules_puissance(cfg_puissance)):
        if banc.faisabilite_cellule_puissance(comp, ec, loi, rho, rp)[0]:
            rangs.append(rang)
    return rangs


def chronometrer(banc, contexte, r, B):
    """Rend une liste ordonnée (nom, durée en secondes) : durée mesurée d'une cellule et durée extrapolée."""
    cfg = banc.CONFIGURATION_PORTEE_200
    cp = cfg["puissance"]
    cellules = banc.enumerer_cellules_puissance(cp)
    faisables = cellules_faisables(banc, cp)
    rang = next(i for i in faisables if abs(cellules[i][1] - banc.ECART_QUI_DECIDE) <= banc.EPS)
    comp, ec, loi, rho, rp = cellules[rang]
    gt = contexte.tirages("monde_de_puissance", len(cellules))
    gr = contexte.reechantillonnage("reechantillonnage_monde_de_puissance", len(cellules))
    d = _mesurer(lambda: banc.cellule_puissance(gt[rang], gr[rang], comp, ec, loi, rho, rp, r, B, n=cp["n"]))
    facteur = cfg["repliques"] / r
    return [("mesuree_d_une_cellule_echantillon", d),
            ("estimee_monde_de_puissance_portee_200", d * facteur * len(faisables))]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Chronométrage de la mesure de la portée à 200 (n'imprime que des "
                                                 "durées).")
    parser.add_argument("--essai", action="store_true")
    parser.add_argument("--autorisation-additif")
    parser.add_argument("--empreinte-additif")
    parser.add_argument("--manifeste", required=True)
    parser.add_argument("--repliques-echantillon", type=int, default=20)
    parser.add_argument("--tirages-essai", type=int, default=None)
    args = parser.parse_args(argv)
    banc = charger_banc()
    dossier = Path(args.manifeste)
    code = Path(__file__).resolve().parent
    if args.essai:
        contexte = banc.Contexte("essais")
        B = args.tirages_essai or banc.CONFIGURATION_PORTEE_200["tirages_reechantillonnage"]
    else:
        if args.tirages_essai is not None:
            raise banc.RefusExecution("--tirages-essai n'est permis qu'en essai")
        banc.verifier_variables_de_chemin_non_posees()
        autorisation = banc.Autorisation(args.autorisation_additif or "", args.empreinte_additif)
        n = len(banc.enumerer_cellules_puissance(banc.CONFIGURATION_PORTEE_200["puissance"]))
        for tache in ("monde_de_puissance", "reechantillonnage_monde_de_puissance"):
            banc.verifier_racine(banc.RACINE_CHRONOMETRAGE_PORTEE_200, tache, n, autorisation)
        if Path(banc.__file__).resolve().parent != code:
            raise banc.RefusExecution("le banc chargé n'est pas celui du dossier du chronométrage")
        banc.verifier_dossier_du_code_propre(code, dossier)
        contexte = banc.Contexte("chronometrage_portee_200", autorisation)
        B = banc.CONFIGURATION_PORTEE_200["tirages_reechantillonnage"]
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
           "configuration_portee_200_sha256": banc.sha256_json(banc._nettoyer(banc.CONFIGURATION_PORTEE_200))}
    manifeste = banc.construire_manifeste(contexte, cfg, debut, fin, {},
                                          dossier_du_code=None if args.essai else code)
    manifeste["programme_chronometrage_sha256"] = banc.sha256_fichier(Path(__file__).resolve())
    manifeste["additif_qui_fait_foi_sha256"] = banc.EMPREINTE_ADDITIF_3_PORTEE_200
    banc.ecrire_json_exclusif(dossier / FICHIER_MANIFESTE, manifeste)
    print(f"duree_mesuree_du_chronometrage_secondes: {mesuree:.3f}")
    for nom, valeur in durees:
        print(f"duree_{nom}_secondes: {valeur:.3f}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # refus du banc : message seul, code 2 ; aucune durée imprimée
        nom = type(exc).__name__
        if nom in ("RefusGraine", "RefusExecution", "BancInvalide", "RegleInconnue"):
            print(f"refus : {exc}", file=sys.stderr)
            sys.exit(2)
        raise
