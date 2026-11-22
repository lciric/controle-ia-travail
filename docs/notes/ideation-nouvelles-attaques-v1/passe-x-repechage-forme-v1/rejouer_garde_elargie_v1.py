"""Rejeu de la garde de coupure avec la règle de forme élargie v1 (regle-de-forme-elargie-v1.md, ea9f4bd5…), sur les
seuls flux classés « défaut » par la garde v4 ; sans appel neuf ; sans rien afficher du texte. Changement unique : si la
dernière ligne non vide, marques retirées, vaut « FIN DES RÉPONSES. », le point final est retiré en mémoire, puis la
garde v4 (`garde_coupure`, inchangée) est appliquée."""
import argparse, hashlib, importlib.util, json, os, re, sys
ICI = os.path.dirname(os.path.abspath(__file__))
DIAG = os.path.join(ICI, "..", "passe-x-diagnostic-forme-v1", "diagnostic_forme_passe_x_v1.py")
REGLE = os.path.join(ICI, "regle-de-forme-elargie-v1.md")
E_REGLE = "ea9f4bd5ae30bd390225edd23335c0e835d783f74142b18f4afaade37f697ed1"
sha = lambda b: hashlib.sha256(b).hexdigest()


def charger(nom, chemin):
    b = open(chemin, "rb").read()
    if open(chemin + ".sha256").read().split()[0] != sha(b):
        sys.exit(f"REFUS : {nom} différent de son compagnon")
    s = importlib.util.spec_from_file_location(nom, chemin); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def elargir(texte):
    lignes = texte.rstrip("\n").split("\n")
    i = max((k for k, l in enumerate(lignes) if l.strip()), default=None)
    if i is None:
        return texte
    nu = lignes[i].strip(" \t*_#>")
    if nu == "FIN DES RÉPONSES.":
        lignes[i] = lignes[i].replace("FIN DES RÉPONSES.", "FIN DES RÉPONSES", 1)
    return "\n".join(lignes) + "\n"


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--journal", required=True); a.add_argument("--quarantaine", required=True); a.add_argument("--sortie", required=True)
    o = a.parse_args(argv)
    if sha(open(REGLE, "rb").read()) != E_REGLE:
        sys.exit("REFUS : règle élargie différente de celle qui est scellée")
    if os.path.exists(o.sortie):
        sys.exit("REFUS : sortie déjà présente")
    G = charger("diagnostic", DIAG)
    lot = G.charger_lot()
    par_sha = {sha(open(os.path.join(o.quarantaine, f), "rb").read()): f
               for f in sorted(os.listdir(o.quarantaine)) if f.endswith(".flux")}
    res = []
    for prop, texte_servi, fourn, h, cause in G.defauts(o.journal):
        if h not in par_sha:
            sys.exit("REFUS : flux introuvable par son empreinte")
        r = lot.lire_flux(fourn, G.evenements(open(os.path.join(o.quarantaine, par_sha[h]), "rb").read()))
        c2, alertes, comptes = lot.garde_coupure(elargir(r["texte"]), lot.RANGS_TEXTES[texte_servi], r["fin"],
                                                 r.get("sortie"), 96000 if fourn != "google" else 65536)
        res.append({"proposeur": prop, "texte_servi": texte_servi, "flux_sha256": h, "cause_v4": cause,
                    "cause_elargie": c2, "alertes": alertes, "comptes": comptes})
    unites = {}
    for x in res:
        g = x["texte_servi"].split("-moitie")[0]
        u = unites.setdefault((x["proposeur"], g), {})
        u[x["texte_servi"]] = x["cause_elargie"] is None
    bilan = []
    for (p, g), t in sorted(unites.items()):
        entier = t.get(g); moities = [t.get(g + "-moitie-a"), t.get(g + "-moitie-b")]
        admise = bool(entier) or (moities[0] is True and moities[1] is True)
        bilan.append({"proposeur": p, "groupe": g, "groupe_entier_passe": entier, "moities_passent": moities,
                      "issue": "admise par règle élargie" if admise else "sans réponse"})
    out = {"version": "rejeu-garde-elargie-v1", "regle_sha256": E_REGLE, "flux": res, "unites": bilan}
    with open(o.sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print(json.dumps([(b["proposeur"], b["groupe"], b["issue"]) for b in bilan], ensure_ascii=False))


if __name__ == "__main__":
    main()
