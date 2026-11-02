"""Essai hors réseau du registre de dépense cumulée v1 : une étape commune contre une étape par fournisseur.
Cas « A1 » (étape commune « attaque_goodhart_v2 », part de 40 USD transmise à chacun) : le second fournisseur est refusé
avant d'atteindre sa part. Cas corrigé (étape « <étape>/<fournisseur> ») : chacun atteint sa part ; le plafond cumulé (80)
tient le total."""
import importlib.util, os, sys, tempfile
spec = importlib.util.spec_from_file_location("reg", sys.argv[1]); reg = importlib.util.module_from_spec(spec); spec.loader.exec_module(reg)

def course(etape_de):
    d = tempfile.mkdtemp(); chemin = os.path.join(d, "registre.jsonl")
    depense = {"argon": 0.0, "kimi": 0.0}; refus = {"argon": 0, "kimi": 0}
    for tour in range(200):
        for f in ("argon", "kimi"):
            try:
                i = reg.reserver(chemin, plafond_cumule_usd=80.0, pire_cas_usd=0.7, fournisseur=f, role="proposeur",
                                 modele="m", etape=etape_de(f), plafond_etape_usd=40.0)
            except reg.PlafondCumule:
                refus[f] += 1; continue
            reg.regler(chemin, i, cout_usd=0.5, pire_cas_usd=0.7, statut="ok", code=0, cout_origine="lu")
            depense[f] += 0.5
    return depense, refus

commune = course(lambda f: "attaque_goodhart_v2")
corrigee = course(lambda f: f"attaque_goodhart_v3/{f}")
print("étape commune   :", commune)
print("étape par fourn.:", corrigee)
assert commune[0]["argon"] + commune[0]["kimi"] <= 40.0 + 1e-9, commune      # défaut d'A1 : total borné à la part
assert corrigee[0]["argon"] > 39 and corrigee[0]["kimi"] > 39, corrigee        # chacun atteint sa part
assert corrigee[0]["argon"] + corrigee[0]["kimi"] <= 80.0 + 1e-9, corrigee     # le plafond cumulé tient
print("ESSAI RÉUSSI : l'étape par fournisseur suffit, rien à changer au registre")
