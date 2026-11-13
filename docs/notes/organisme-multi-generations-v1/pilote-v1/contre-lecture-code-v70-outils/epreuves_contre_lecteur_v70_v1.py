"""Épreuves directes du contre-lecteur du code v70 (aucun réseau, aucune clé, aucun appel) : le relevé de la sonde et la règle
de comptage de la réflexion. Usage : python -I -B epreuves_contre_lecteur_v70_v1.py RACINE_ORCHESTRATOR DOSSIER_NEUF"""
import json, os, sys
RACINE, D = sys.argv[1], sys.argv[2]
sys.path.insert(0, RACINE)
from pole import pilote_mr2_v70 as P, proposeurs_pilote_v70 as PR, sonde_pilote_v70 as S
conf, _ = PR.lire_configuration(os.path.join(RACINE, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v11.json"))
os.makedirs(D)

def usage(d, entree, visibles, pensee, comprise_en_vrai):
    if d == "claude":
        return {"input_tokens": entree, "output_tokens": visibles + pensee}
    if d == "gemini":
        c = visibles + pensee if comprise_en_vrai else visibles
        return {"promptTokenCount": entree, "candidatesTokenCount": c, "thoughtsTokenCount": pensee,
                "totalTokenCount": entree + visibles + pensee}
    c = visibles + pensee if comprise_en_vrai else visibles
    return {"prompt_tokens": entree, "completion_tokens": c, "reasoning_tokens": pensee, "total_tokens": entree + visibles + pensee}

def faits(vrai, astra=None, argon_brut=None):
    """vrai : {proposeur: la réflexion est-elle comprise dans le champ de sortie, dans le monde simulé}.
    astra : [(visibles, pensée) appel 1, (visibles, pensée) appel 2] pour Astra ; sinon (2, 300) et (56, 200)."""
    out = []
    for nom in P.PROPOSEURS:
        p = conf["proposeurs"][nom]
        d = p["dialecte"]
        for quoi, (vis, pen) in zip(S.APPELS, (astra if (astra and nom == "astra") else [(2, 300), (56, 200)])):
            borne = p["borne_sortie_jetons"] if quoi == "borne_gelee" else 256
            u = usage(d, 12, vis, pen, vrai[nom])
            if argon_brut and nom == "argon":
                u = argon_brut[quoi]
            f = {"proposeur": nom, "appel": quoi, "borne": borne, "etat": "complet" if quoi == "borne_gelee" else "tronque",
                 "code": 0, "cause": None, "raison_arret": "x", "modele_servi": p["modele"], "modele_servi_conforme": True,
                 "statut_amont": 200, "type_erreur": None, "usage_brut": u, "usage_entier": True, "verdict_reflexion": None,
                 "sortie_comptee": None, "cout_usd": 0.01, "au_dessus_du_pire_cas": False, "pieces": {}}
            if d == "claude":
                f["flux"] = {"egal": True}
            out.append(f)
    return out

def essai(nom, f):
    chemin = os.path.join(D, nom + ".json")
    rel = S.releve(conf, f, True, "d", "f", False, None, {})
    PR.ecrire_scelle_json(chemin, rel)
    try:
        sha = S.exiger_releve(conf, chemin)
        issue = "ADMIS " + sha[:8]
    except P.Refus as e:
        issue = "REFUS : " + str(e)[:150]
    print(f"{nom} : verdicts {{{', '.join(n + ': ' + rel['conclusions'][n]['verdict_reflexion'] for n in P.PROPOSEURS)}}} → {issue}")

regle = {n: conf["proposeurs"][n]["reflexion_comprise"] for n in P.PROPOSEURS}
print("règle gelée :", regle)
try:
    S.exiger_releve(conf, os.path.join(D, "absent.json"))
except P.Refus as e:
    print("E1a relevé absent → REFUS :", e)
essai("E1b-monde-conforme-a-la-regle", faits(regle))
essai("E1c-astra-reflexion-ajoutee-en-vrai", faits(dict(regle, astra=False)))
essai("E1d-argon-reflexion-comprise-en-vrai", faits(dict(regle, argon=True)))
essai("E1e-astra-sans-reflexion-aux-deux-appels", faits(regle, astra=[(2, 0), (256, 0)]))
# Zone de fausse confirmation : monde où la réflexion d'Astra est AJOUTÉE (non comprise), règle gelée « comprise ».
essai("E2a-astra-ajoutee-en-vrai-petite-reflexion (visibles 3, pensée 2 ; puis visibles 130, pensée 126)",
      faits(dict(regle, astra=False), astra=[(3, 2), (130, 126)]))
essai("E2b-astra-ajoutee-en-vrai-aucune-reflexion-a-l-appel-1 (visibles 2, pensée 0 ; puis visibles 130, pensée 126)",
      faits(dict(regle, astra=False), astra=[(2, 0), (130, 126)]))
essai("E2c-astra-ajoutee-en-vrai-reflexion-nette (visibles 2, pensée 300 ; puis visibles 130, pensée 126) : contradictoire attendu",
      faits(dict(regle, astra=False), astra=[(2, 300), (130, 126)]))
# Argon sans totalTokenCount : même heuristique qu'Astra
sans_total = {"borne_gelee": {"promptTokenCount": 12, "candidatesTokenCount": 3, "thoughtsTokenCount": 2, "totalTokenCount": None},
              "borne_courte": {"promptTokenCount": 12, "candidatesTokenCount": 100, "thoughtsTokenCount": 150, "totalTokenCount": None}}
essai("E2d-argon-sans-total-petite-reflexion (candidats 3, pensées 2 : lu « comprise », règle gelée « ajoutée »)",
      faits(regle, argon_brut=sans_total))
for d, u in (("astra", {"completion_tokens": 3, "reasoning_tokens": 2}), ("astra", {"completion_tokens": 130, "reasoning_tokens": 126}),
             ("astra", {"completion_tokens": 2, "reasoning_tokens": 300}), ("astra", {"completion_tokens": 302, "reasoning_tokens": 300})):
    print("verdict_reflexion", d, u, "→", S.verdict_reflexion(d, u))
