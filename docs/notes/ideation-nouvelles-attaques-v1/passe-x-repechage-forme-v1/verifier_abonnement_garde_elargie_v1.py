"""Garde de coupure (v4, règle de forme élargie v1) appliquée aux réponses de l'abonnement de la passe X, lues par
`git show` depuis les branches de quarantaine rapatriées sous refs/abonnement/<unité> ; sans rien afficher du texte.
Limite déclarée : une session de l'abonnement ne rend pas de raison d'arrêt ; la garde est appliquée avec fin
« end_turn » ; les contrôles de forme (titres, ordre, longueur, ligne finale) restent entiers. Pour l'exploration,
présence, taille et empreinte seulement (la garde des groupes ne s'y applique pas)."""
import argparse, hashlib, importlib.util, json, os, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
R = importlib.util.spec_from_file_location("rejeu", os.path.join(ICI, "rejouer_garde_elargie_v1.py"))
rejeu = importlib.util.module_from_spec(R); R.loader.exec_module(rejeu)
UNITES = ["fable51-groupe-2", "fable51-groupe-3", "opus46-groupe-2", "opus46-groupe-3", "opus55-groupe-3",
          "sonnet46-groupe-2", "sonnet46-groupe-3"]
EXPLO = ["exploration-opus46", "exploration-sonnet46"]


def montrer(arbre, ref, chemin):
    r = subprocess.run(["git", "-C", arbre, "show", f"{ref}:{chemin}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def main(argv=None):
    a = argparse.ArgumentParser(); a.add_argument("--arbre", required=True); a.add_argument("--sortie", required=True)
    o = a.parse_args(argv)
    if os.path.exists(o.sortie):
        sys.exit("REFUS : sortie déjà présente")
    if hashlib.sha256(open(rejeu.REGLE, "rb").read()).hexdigest() != rejeu.E_REGLE:
        sys.exit("REFUS : règle élargie différente de celle qui est scellée")
    lot = rejeu.charger("diagnostic", rejeu.DIAG).charger_lot()
    res = []
    for u in UNITES:
        b = montrer(o.arbre, f"refs/abonnement/passe-x-abonnement-{u}", f"flux-abonnement/{u}.md")
        g = "groupe-" + u.rsplit("-", 1)[1]
        if b is None:
            res.append({"unite": u, "present": False}); continue
        c, al, co = lot.garde_coupure(rejeu.elargir(b.decode("utf-8", "replace")), lot.RANGS_TEXTES[g], "end_turn", None, 128000)
        res.append({"unite": u, "present": True, "octets": len(b), "sha256": hashlib.sha256(b).hexdigest(),
                    "cause": c, "alertes": al, "comptes": co, "issue": "admise" if c is None else "défaut de forme"})
    for u in EXPLO:
        b = montrer(o.arbre, f"refs/abonnement/{u.replace('exploration-', 'exploration-allumage-')}", f"flux-abonnement/{u}.md")
        res.append({"unite": u, "present": b is not None, **({"octets": len(b), "sha256": hashlib.sha256(b).hexdigest()} if b else {})})
    out = {"version": "garde-abonnement-elargie-v1", "regle_sha256": rejeu.E_REGLE, "unites": res}
    with open(o.sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print(json.dumps([(x["unite"], x.get("issue", "présent" if x["present"] else "absent"), x.get("octets"))
                      for x in res], ensure_ascii=False))


if __name__ == "__main__":
    main()
