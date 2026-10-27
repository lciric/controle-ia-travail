"""Duel des proposeurs (v7, version 10) : un proposeur à modèle (Opus 5.5, avec et sans la partie de développement) contre
les références gratuites (chercheur mécanique, lois aléatoires), sur des mondes hors de l'espace du mécanique (grammaire v2,
structures « trois traits » et « seuil décalé »). Devis et lecture : `../../demonstration-proposeurs-v7/devis-duel-proposeurs-v1.md`.

Deux moteurs :
- `--moteur simule` (sans dépense) : les bras « à modèle » sont joués par le proposeur scripté du pôle (répétition de la
  plomberie et de la lecture ; ce n'est pas le duel) ;
- `--moteur claude-sdk --url-relais URL` (dépense, chez session-depot, sous GO) : les bras M-expl et M-aveugle lancent
  `pole` en sous-processus avec `--roles-reels proposeur` (seul le proposeur est un vrai agent ; bac à sable exigé par v7).

Lecture L1 à L5 (fixée dans le devis) : témoins faux promus ; pari apparié borné sur les mondes (forme « parts » seule,
mélange de mises sur Λ, α = 0,05 ; conception v2) pour M-expl contre mécanique (L2), M-aveugle contre aléatoire (L3), M-expl contre M-aveugle (L4) ; coût
par structure retrouvée (L5, rapporté). Règle d'arrêt : après `--arret-apres` mondes, si M-expl n'a rien retrouvé, la
suite est annulée.

Usage : python -I -B demonstrations/duel_proposeurs_v7.py DOSSIER_NEUF [--mondes 20] [--moteur simule|claude-sdk]
        [--url-relais URL] [--arret-apres 10] [--budget-par-monde 6]
"""

import argparse
import json
import os
import subprocess
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)
sys.path.insert(0, os.path.join(RACINE, "exemples"))
sys.path.insert(0, ICI)

import generer_monde_grammaire_v2 as g2  # noqa: E402
from demo_proposeurs_v7 import _traits_de, traits_de_la_structure  # noqa: E402
from generer_monde_grammaire_v1 import fiches_de_temoins  # noqa: E402
from pole.cycle import ConfigGeneration  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.outils import ecrire_json_scelle, graine_derivee  # noqa: E402
from pole.pole import executer_pole  # noqa: E402
from pole.proposeur import valider_proposition  # noqa: E402
from pole.proposeurs_references import propositions_aleatoires  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

D, K, MONITEURS = 4, 3, 3
GRAINE_BASE = 20261200
LAMBDAS = (0.1, 0.3, 0.6, 0.9)
ALPHA = 0.05
BRAS_MODELE = {"M-expl": True, "M-aveugle": False}
BRAS_REFERENCE = {"mecanique": {"proposeur": "mecanique", "exploration": True},
                  "aleatoire": {"proposeur": "aleatoire", "exploration": False}}


def pari_apparie(valeurs):
    """Richesse du pari apparié borné, **forme « parts » seule** (conception v2, après le constat C1 de la contre-lecture :
    la forme « signe » teste un autre nul et son mélange n'est pas une surmartingale sous E[v] ≤ 0) : mélange sur Λ de
    Π(1 + λ·v) sur une suite de contrastes v ∈ [−1 ; 1] ; promotion au seuil 1/α."""
    import math
    wv = [1.0] * len(LAMBDAS)
    traj, promu_a = [], None
    for t, v in enumerate(valeurs, 1):
        if not -1.0 <= v <= 1.0:
            raise ValueError(f"contraste hors de [-1 ; 1] : {v}")
        wv = [w * (1 + lam * v) for w, lam in zip(wv, LAMBDAS)]
        richesse = sum(wv) / len(LAMBDAS)
        traj.append(round(math.log(richesse), 6))
        if promu_a is None and richesse >= 1 / ALPHA:
            promu_a = t
    return {"trajectoire_log_w": traj, "log_w_max": max(traj) if traj else 0.0, "seuil_log": math.log(1 / ALPHA),
            "promu": promu_a is not None, "instant_de_promotion": promu_a, "n": len(valeurs)}


def preparer_monde(dossier, graine):
    structures = ["trois_traits", "seuil_decale", "trois_traits"] if graine % 2 else ["seuil_decale", "trois_traits", "seuil_decale"]
    banque, temoins, verite = g2.generer_monde(graine, structures=structures)
    os.makedirs(dossier, exist_ok=True)
    chemin_banque = os.path.join(dossier, "banque.json")
    ecrire_json_scelle(chemin_banque, banque)
    monde = MondeBanque(chemin_banque, graine)
    population = [valider_proposition(p, monde, ALPHA, f"P{i:02d}", "reference-aleatoire", references=True)
                  for i, p in enumerate(propositions_aleatoires(monde.description_publique(), 6, graine_derivee(graine, "population"), 0), 1)]
    chemin_pop, chemin_tem = os.path.join(dossier, "population.json"), os.path.join(dossier, "temoins.json")
    ecrire_json_scelle(chemin_pop, [f.vers_dict() for f in population])
    ecrire_json_scelle(chemin_tem, [f.vers_dict() for f in fiches_de_temoins(temoins, D, K)])
    ecrire_json_scelle(os.path.join(dossier, "verite.json"), {n: {k: v for k, v in x.items() if k != "loi"} for n, x in verite.items()})
    return chemin_banque, chemin_pop, chemin_tem, verite


def lire_course(dossier, verite):
    with open(os.path.join(dossier, "archive", "index.json"), encoding="utf-8") as f:
        index = json.load(f)
    with open(os.path.join(dossier, "bilan.json"), encoding="utf-8") as f:
        bilan = json.load(f)
    retrouvees, sans_lien, faux_promus = set(), 0, 0
    for ident, e in index.items():
        if e["temoin"]:
            faux_promus += e["temoin"] == "fausse" and e["statut"] == "survit"
            continue
        if e["statut"] != "survit":
            continue
        with open(os.path.join(dossier, "archive", "fiches", ident, "etat-final.json"), encoding="utf-8") as f:
            etat = json.load(f)
        moniteur = (etat.get("espace_instances") or {}).get("moniteur")
        v = verite.get(moniteur)
        if v and _traits_de(etat["loi_predictive"]) & traits_de_la_structure(v):
            retrouvees.add(moniteur)
        else:
            sans_lien += 1
    return {"structures_retrouvees": sorted(retrouvees), "nombre": len(retrouvees), "sans_lien": sans_lien,
            "temoins_faux_promus": faux_promus, "depense_usd": bilan.get("depense_totale", 0.0)}


def course_reference(nom, graine, dossier, chemin_banque, chemin_pop, chemin_tem):
    from pole.fiche import charger_fiches
    reglages = BRAS_REFERENCE[nom]
    monde = MondeBanque(chemin_banque, graine)
    config = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, graine=graine, taille_plan=150,
                              taille_plan_filles=150, instants_filles=6, part_calibrage=12, budget_generation_usd=500.0,
                              multiplicite="e-bh", temoins_sans_agent=True, nul_archive=True, nul_archive_ajuste=True,
                              propositions_par_generation=12, exploration_developpement=reglages["exploration"],
                              proposeur=reglages["proposeur"]).valider()
    executer_pole(charger_fiches(chemin_pop), charger_fiches(chemin_tem), AdaptateurSimule(graine, MondeSimule(graine)), config,
                  3, 5000.0, dossier, memoire_active=True, horodatage_fourni="duel des proposeurs", temoins_par_generation=MONITEURS,
                  k_recombinaison=4, max_paires=2, monde_noyau=monde)


def commande_modele(nom, graine, dossier, chemins, moteur, url_relais, budget):
    banque, pop, tem = chemins
    cmd = [sys.executable, "-I", "-B", os.path.join(RACINE, "pole"), "--selection", "pari", "--monde-banque", banque, "--sans-urne",
           "--temoins-sans-agent", "--temoins-par-generation", str(MONITEURS), "--population", pop, "--temoins", tem,
           "--generations", "3", "--propositions-par-generation", "12", "--proposeur", "agent", "--graine", str(graine),
           "--budget-usd", str(budget), "--sortie", dossier, "--horodatage", "duel des proposeurs", "--taille-plan", "150",
           "--taille-plan-filles", "150"]
    if BRAS_MODELE[nom]:
        cmd.append("--exploration-developpement")
    if moteur == "claude-sdk":
        cmd += ["--moteur", "claude-sdk", "--confirmer-moteur-reel", "--url-relais", url_relais, "--roles-reels", "proposeur",
                "--modele-proposeur", "claude-opus-5-5"]
    return cmd


def principal(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("dossier")
    a.add_argument("--mondes", type=int, default=20)
    a.add_argument("--moteur", choices=("simule", "claude-sdk"), default="simule")
    a.add_argument("--url-relais")
    a.add_argument("--arret-apres", type=int, default=10)
    a.add_argument("--budget-par-monde", type=float, default=6.0)
    args = a.parse_args(argv)
    if args.moteur == "claude-sdk" and not args.url_relais:
        raise ValueError("--moteur claude-sdk exige --url-relais")
    if os.path.exists(args.dossier) and os.listdir(args.dossier):
        raise FileExistsError(args.dossier)
    os.makedirs(args.dossier, exist_ok=True)
    debut, resultats, arret = time.time(), [], None
    for s in range(1, args.mondes + 1):
        graine = GRAINE_BASE + s
        dossier_monde = os.path.join(args.dossier, f"monde-{s:02d}")
        chemins = preparer_monde(os.path.join(dossier_monde, "monde"), graine)
        verite = chemins[3]
        par_bras = {}
        for nom in BRAS_MODELE:
            sortie = os.path.join(dossier_monde, nom)
            env = {"PATH": os.environ.get("PATH", ""), "HOME": os.environ.get("HOME", "")}
            res = subprocess.run(commande_modele(nom, graine, sortie, chemins[:3], args.moteur, args.url_relais, args.budget_par_monde),
                                 env=env if args.moteur == "claude-sdk" else None, capture_output=True, text=True, timeout=7200, check=False)
            with open(os.path.join(dossier_monde, f"sortie-{nom}.txt"), "w", encoding="utf-8") as f:
                f.write(res.stdout + "\n--- stderr ---\n" + res.stderr)
            par_bras[nom] = lire_course(sortie, verite) if res.returncode == 0 else {"erreur": res.returncode, "nombre": 0,
                                                                                      "sans_lien": 0, "temoins_faux_promus": 0,
                                                                                      "depense_usd": 0.0, "structures_retrouvees": []}
        for nom in BRAS_REFERENCE:
            sortie = os.path.join(dossier_monde, nom)
            course_reference(nom, graine, sortie, *chemins[:3])
            par_bras[nom] = lire_course(sortie, verite)
        resultats.append({"graine": graine, "structures": {m: v["structure"] for m, v in verite.items()}, "bras": par_bras})
        if s == args.arret_apres and sum(r["bras"]["M-expl"]["nombre"] for r in resultats) == 0:
            arret = f"arrêt après {s} mondes : M-expl n'a retrouvé aucune structure"
            break
    lecture = lire(resultats)
    rapport = {"mondes": len(resultats), "moteur": args.moteur, "arret": arret, "duree_s": round(time.time() - debut, 1),
               "lecture": lecture, "resultats": resultats}
    ecrire_json_scelle(os.path.join(args.dossier, "duel-proposeurs-v7.json"), rapport)
    print(json.dumps({"lecture": lecture, "arret": arret, "duree_s": rapport["duree_s"]}, ensure_ascii=False, indent=1))
    return 0


def lire(resultats):
    def contraste(a, b):
        return [(r["bras"][a]["nombre"] - r["bras"][b]["nombre"]) / MONITEURS for r in resultats]
    lecture = {"L1_temoins_faux_promus": {b: sum(r["bras"][b]["temoins_faux_promus"] for r in resultats) for b in resultats[0]["bras"]},
               "L1_promues_sans_lien": {b: sum(r["bras"][b]["sans_lien"] for r in resultats) for b in resultats[0]["bras"]},
               "structures_retrouvees": {b: sum(r["bras"][b]["nombre"] for r in resultats) for b in resultats[0]["bras"]},
               "structures_total": MONITEURS * len(resultats),
               "L2_M-expl_contre_mecanique": pari_apparie(contraste("M-expl", "mecanique")),
               "L3_M-aveugle_contre_aleatoire": pari_apparie(contraste("M-aveugle", "aleatoire")),
               "L4_M-expl_contre_M-aveugle": pari_apparie(contraste("M-expl", "M-aveugle"))}
    depenses = {b: sum(r["bras"][b]["depense_usd"] for r in resultats) for b in resultats[0]["bras"]}
    lecture["L5_usd_par_structure"] = {b: (round(depenses[b] / lecture["structures_retrouvees"][b], 3)
                                           if lecture["structures_retrouvees"][b] else None) for b in depenses}
    lecture["depense_usd"] = depenses
    return lecture


if __name__ == "__main__":
    sys.exit(principal())
