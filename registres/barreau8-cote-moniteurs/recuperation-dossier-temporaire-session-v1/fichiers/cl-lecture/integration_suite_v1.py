"""Suite de l'essai d'intégration : sur la livraison déjà produite par le code de la passe (dossier de travail), refait la
garde de réception, puis joue la lecture mécanique ENTIÈRE en remplaçant le seul essai A0 par un essai réputé tenu
(remplacement déclaré, pour éprouver le reste de la chaîne sur une vraie livraison ; jamais un résultat)."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
sys.path[:0] = [str(DEPOT / "src")]

import numpy as np  # noqa: E402

from controle_ia import manifeste  # noqa: E402
from controle_ia.barreau8_moniteurs import lecture_sondes_v1 as L  # noqa: E402
from controle_ia.premier_test_ia.figees import lire_sondes  # noqa: E402
from controle_ia.scellement import empreinte, sceller  # noqa: E402

base = Path(sys.argv[1])
n_taches, n_plancher = int(sys.argv[2]), int(sys.argv[3])
racine = base / "depot"
chemins = {r: racine / "donnees" / "sondes" / f"{r}.npz" for r in ("legeres", "planchers", "neuves")}
sha = {r: empreinte(c) for r, c in chemins.items()}
listes = {r: lire_sondes(c, sha[r])[0] for r, c in chemins.items()}


def ident(nom, role, role_p, prefixe):
    k = [s.nom for s in listes[role]].index(nom)
    s = listes[role][k]
    return L.IdentiteSonde(nom, role, f"s{k}_w", hashlib.sha256(np.ascontiguousarray(s.w).tobytes()).hexdigest(), s.empreinte(),
                           role_p, prefixe)


identites = L.Identites(fichiers=sha, sondes=(
    ident("tromperie-difference_moyennes-c15", "legeres", "planchers", "tromperie-difference_moyennes-c15-t07"),
    ident("enjeux-lineaire-c15", "legeres", "planchers", "enjeux-lineaire-c15-t07"),
    ident("dissimulation-lineaire-c15", "neuves", "neuves", None)), couches_7_23=dict(L.IDENTITES_DU_TEXTE.couches_7_23))
t = L.Tailles(n_taches=n_taches, n_pas=3, largeur=32, n_plancher=n_plancher, max_jetons=12, pas_c15=2, pas_c7_c23=8, n_tirages=400,
              n_permutations=60, taille_max=2_000_000_000, taille_morceau=30_000)
cadre = L.Cadre(tailles=t, identites=identites, recette=L.Recette(), modele={"nom": "jouet", "revision": "jouet-0"})
code_passe = json.loads((racine / "registres" / "bordereau-code-sain.json").read_text(encoding="utf-8"))
modules_passe = {n: m["sha256"] for n, m in code_passe["modules"].items()}
bordereau = racine / "livraisons" / "sortie-1" / "livraison" / L.NOM_BORDEREAU
d = L.garde_de_reception(bordereau, empreinte(bordereau), modules_passe, chemins, cadre)
print("réception tenue ; repère de couche :", json.dumps({k: v for k, v in d.repere_de_couche.items() if k != "controles"},
                                                         ensure_ascii=False)[:600])
p = base / "etats-2" / "etats-lectures-iib-v1.json"
p.parent.mkdir(exist_ok=True)
paire = {"cout": "réussit", "traits": "échoue", "mots_et_cout": "échoue"}
p.write_text(json.dumps({"avertissement": L.AVERTISSEMENT_EXTRAIT, "run_id": "20261119-010203-course-jouet",
                         "lecture_dommage": {"phrase": L.DOMMAGE_VU},
                         "lecture_diffusion": {"par_paire": {"B100-H": {**paire, "unite": "échoue"}, "B50-H": {**paire, "unite": "échoue"},
                                                             "TJ100-H": {**paire, "unite": "réussit"}, "B100-TJ100": {"mots_et_cout": "échoue"}},
                                               "phrase": None}}, ensure_ascii=False), encoding="utf-8")
etats = L.verifier_extrait_etats(p, sceller(p))
graines = manifeste.graines(L.cles_de_graines(d.sondes_lues, d.sondes_7_23), 123456789)
vrai_a0 = L.essai_de_la_chaine
L.essai_de_la_chaine = lambda d_, g_, t_: {**vrai_a0(d_, g_, t_), "echec": False, "motifs": ["remplacé par l'essai d'intégration"]}
sortie = L.calculer_lecture(d, etats, graines, cadre, {"par_fraction": {}})
print("lignes :", [l["ligne"] for l in sortie["lignes_declenchees"]])
print("états :", json.dumps(sortie["etats"], ensure_ascii=False)[:800])
print("réserves en tête :", json.dumps(sortie["en_tete"]["reserves"], ensure_ascii=False)[:1500])
print("déclencheurs :", json.dumps(sortie["declencheurs_de_l_audit"], ensure_ascii=False)[:800])
print("descriptif : dose", len(sortie["descriptif"]["dose (B8-P3)"]), "placebo", len(sortie["descriptif"]["placebo (B8-P4)"]),
      "couches 7/23", len(sortie["descriptif"]["couches 7 et 23 (B8-P5)"]), "diagnostic", len(sortie["diagnostic_moyenne"]),
      "hors jugement", len(sortie["descriptif"]["conditions hors jugement"]))
print("production :", [(l["sonde"][:10], l["jeu"], l["clause"], l["etat"], round(l.get("aire", float("nan")), 3)) for l in sortie["production"]])
if sortie["declencheurs_de_l_audit"].get("audit_de_symetrie_declenche"):
    a = L.audit_mecanique(d, json.loads(json.dumps(sortie, default=str)), etats, graines, cadre)
    print("audit :", a["ligne"], a["defauts_etablis"], a["relectures"])
