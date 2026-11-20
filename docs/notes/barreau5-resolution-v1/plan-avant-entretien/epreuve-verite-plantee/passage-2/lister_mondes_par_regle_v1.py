"""Liste, par identifiant, les mondes hors du compte d'une règle « au moins », et les mondes dans le compte d'une règle
« au plus ». Réemploie les prédicats du juge (src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py), sans rien
changer. Descriptif : ne juge rien. Outil de l'ouvreur, passage 2.
Usage : python -B lister_mondes_par_regle_v1.py VERITES EMPREINTE RENDUS SORTIE
"""
import json
import sys

from controle_ia.barreau5_familles import juge_verite_plantee_v1 as J


def main():
    chemin_v, empreinte, chemin_r, sortie = sys.argv[1:5]
    doc = J.lire_verites(chemin_v, empreinte)
    verites = {m["monde"]: m for m in doc["mondes"]}
    rendus = J.lire_rendus(chemin_r)
    par_groupe = {}
    for m, v in verites.items():
        par_groupe.setdefault(v["groupe"], []).append(m)
    out = {"regles": []}
    for g, texte, sens, seuil, pred in J.REGLES:
        ms = sorted(par_groupe.get(g, []))
        ok = [m for m in ms if m in rendus and not J.erreurs_rendu(rendus[m]) and pred(rendus[m], verites[m]["attendu"])]
        if sens == "au moins":
            liste = [m for m in ms if m not in ok]
            quoi = "mondes hors du compte"
        else:
            liste = ok
            quoi = "mondes dans le compte"
        details = {}
        for m in liste:
            r = rendus.get(m) or {}
            details[m] = {"refus": r.get("refus"), "issue": r.get("issue"), "niveau": r.get("niveau"),
                          "motifs_D": r.get("motifs_D"),
                          "mention_saboteur_sans_sur": r.get("mention_saboteur_sans_sur"),
                          "E3": J._decision(r, "E3") if r else None}
        out["regles"].append({"groupe": g, "regle": texte, "sens": sens, "seuil": seuil, "quoi": quoi,
                              "nombre": len(liste), "mondes": details})
    # descriptif : issues des mondes VC (coûts illisibles chez un seul membre)
    vc = {}
    for g in J.GROUPES_LECTURE:
        for m in sorted(par_groupe.get(g, [])):
            r = rendus.get(m) or {}
            vc[m] = {"refus": r.get("refus"), "issue": r.get("issue"), "niveau": r.get("niveau"),
                     "motifs_D": r.get("motifs_D")}
    out["mondes_VC"] = vc
    out["mondes_par_groupe"] = {g: len(v) for g, v in sorted(par_groupe.items())}
    out["refus_par_groupe"] = {g: sum(1 for m in v if (rendus.get(m) or {}).get("refus")) for g, v in
                               sorted(par_groupe.items())}
    with open(sortie, "x", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
