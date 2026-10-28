"""Contre-vérification v9, section G : une chaîne que chaque garde de la version 27 laisse passer.

(1) une copie renommée de la fiche (mêmes coefficients, autre nom de contraste : autre clé, `Lignees` l'accepte) ;
(2) la copie lit chaque tranche **une génération avant** la fiche (la fraîcheur n'est vérifiée que par fiche) ;
(3) quand la copie a trouvé la tranche défavorable, la fiche ne la lit pas : déclaration « fiche non lancée », vraie
    (aucune partie calculée, le journal est propre, `verifier_sans_partie` l'accepte).
Nul complet ; parties synthétiques de 20 unités v ∈ {−0,5 ; +0,5} équiprobables (espérance nulle) ; famille {fiche,
copie} entrée en génération 1 au niveau α = 0,05 (seuil 1/b = 40) ; lecture e-BH pondérée à chaque génération par la
`Course` du code. Comparaison : la même course honnête (la fiche lit toutes ses tranches).

Usage : REP=1000 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v9-chaine.py RACINE > sortie.json
"""

import hashlib
import json
import os
import random
import sys
import time

import numpy as np

RACINE = os.path.abspath(sys.argv[1])
REP = int(os.environ.get("REP", "1000"))
ENTROPIE = 2026102809
sys.path.insert(0, RACINE)
from pole import engagement_apparie as ea  # noqa: E402
from pole import monde_banque_scores as mbs  # noqa: E402
from pole import pari_apparie as pa  # noqa: E402


def graine(i, j):
    return int(np.random.SeedSequence(ENTROPIE, spawn_key=(9, i, j)).generate_state(1, dtype=np.uint64)[0])


def lignees_acceptent_la_copie():
    """Les deux engagements réels (mêmes coefficients, noms différents) sur une petite banque : clés distinctes."""
    rng = random.Random(graine(0, 0))
    eps = []
    for u in range(40):
        partie = "calibrage" if u < 30 else "epreuve"
        for k in range(4):
            for et in ("honnete", "sabote") if partie == "epreuve" else ("honnete",):
                eps.append({"id": f"{u}-{et}-{k}", "unite": f"u{u}", "etiquette": et, "partie": partie, "strates": {},
                            "scores": {"blanc": rng.gauss(0, 1), "juge": rng.gauss(0, 1)}})
    m = mbs.MondeBanqueScores({"cellules": ["blanc", "juge"], "strates": [], "episodes": eps}, 1)
    coef = {"blanc": 1, "juge": -1}
    e_f = ea.construire(m, {"fiche": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=2)
    e_c = ea.construire(m, {"copie": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=2)
    lg = ea.Lignees()
    lg.entrer("fiche", e_f)
    lg.entrer("copie", e_c)  # acceptée : autre clé
    return e_f["empreinte_cle"] != e_c["empreinte_cle"]


def course(rng, generations, tricheuse):
    c = pa.Course(alpha=0.05)
    c.entrer("g1", ["fiche", "copie"], 0.05)
    lg = ea.Lignees()
    tranches = {}

    def tranche(t):
        if t not in tranches:
            tranches[t] = [rng.choice((-0.5, 0.5)) for _ in range(20)]
        return tranches[t]

    def ids(t):
        return {("banque", "epreuve", f"t{t}-{u}") for u in range(20)}

    sans_partie_trace = 0
    for g in range(1, generations + 1):
        sans_partie = {}
        actives = [f for f in ("fiche", "copie") if f not in c.promues and f not in c.arretees and f not in c.gelees]
        if "copie" in actives:
            t = g + 1 if tricheuse else g  # la copie lit une tranche d'avance
            traj = pa.trajectoire_log_richesse(tranche(t))
            lg.journaliser(g, "copie", {"empreinte_unites": f"t{t}", "identifiants_unites": list(ids(t))})
            c.ajouter_trajectoire("copie", traj, unites=ids(t))
        if "fiche" in actives:
            vu = pa.trajectoire_log_richesse(tranche(g))[-1] if (tricheuse and g >= 2) else None  # lu par la copie en g − 1
            if vu is not None and vu <= 0.0:
                sans_partie["fiche"] = "fiche non lancée"
                sans_partie_trace += 1
            else:
                traj = pa.trajectoire_log_richesse(tranche(g))
                lg.journaliser(g, "fiche", {"empreinte_unites": f"t{g}", "identifiants_unites": list(ids(g))})
                c.ajouter_trajectoire("fiche", traj, unites=ids(g))
        lg.verifier_sans_partie(g, sans_partie)  # passe : aucune partie de la fiche n'a été calculée
        c.lire(sans_partie=sans_partie)
    return c, sans_partie_trace


def principal():
    t0 = time.time()
    sortie = {"manifeste": {"script": os.path.basename(__file__),
                            "sha256_script": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                            "sha256_pari_apparie": hashlib.sha256(open(os.path.join(RACINE, "pole/pari_apparie.py"), "rb").read()).hexdigest(),
                            "sha256_engagement_apparie": hashlib.sha256(open(os.path.join(RACINE, "pole/engagement_apparie.py"), "rb").read()).hexdigest(),
                            "python": sys.version.split()[0], "numpy": np.__version__, "REP": REP, "entropie": ENTROPIE},
              "lignees_acceptent_la_copie_renommee": lignees_acceptent_la_copie()}
    for gens in (10, 30):
        for nom, tricheuse in (("honnete", False), ("chaine", True)):
            promue_fiche, au_moins_une, decl = 0, 0, 0
            for r in range(REP):
                c, d = course(random.Random(graine(gens * 10 + tricheuse, r)), gens, tricheuse)
                promue_fiche += "fiche" in c.promues
                au_moins_une += bool(c.promues)
                decl += d
            sortie[f"{nom}_{gens}_generations"] = {"fiche_promue": promue_fiche / REP, "au_moins_une_promotion": au_moins_une / REP,
                                                   "declarations_sans_partie_par_course": decl / REP}
    sortie["manifeste"]["duree_secondes"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=True)
    print()


if __name__ == "__main__":
    principal()
