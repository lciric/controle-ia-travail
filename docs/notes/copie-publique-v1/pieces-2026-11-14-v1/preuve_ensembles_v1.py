"""Preuve par ensembles (noms, modes et identifiants d'objets git seulement ; aucun contenu lu).
Usage : python3 -I preuve_ensembles.py LS_PUBLIC LS_NEUF LS_SOURCE  (sorties de `git ls-tree -r`)."""
import hashlib, json, sys

def lire(chemin):
    d = {}
    for l in open(chemin, encoding="utf-8"):
        meta, nom = l.rstrip("\n").split("\t", 1)
        mode, typ, ident = meta.split()
        assert typ == "blob" and nom not in d
        d[nom] = (mode, ident)
    return d

public, neuf, source = (lire(a) for a in sys.argv[1:4])
P, N = set(public), set(neuf)
res = {"fichiers_public_a043767": len(P), "fichiers_arbre_neuf": len(N)}
# (a) inclusion et identité
res["a_chemins_neufs_absents_du_public"] = sorted(N - P)
differents = sorted(n for n in N & P if neuf[n] != public[n])
res["a_gardes_identiques_mode_et_identifiant"] = len(N & P) - len(differents)
res["a_gardes_differents"] = [{"chemin": n, "public": public[n], "neuf": neuf[n]} for n in differents]
# (b) différence
D = P - N
vises = {n for n in P if n.startswith("brouillons/pain-axis-")}
res["b_difference_public_moins_neuf"] = len(D)
res["b_chemins_brouillons_pain_axis_du_public"] = len(vises)
res["b_difference_egale_ensemble_vise"] = (D == vises)
res["b_difference_hors_ensemble_vise"] = sorted(D - vises)
res["b_ensemble_vise_reste_dans_le_neuf"] = sorted(vises & N)
res["b_empreinte_de_la_liste_triee_des_chemins_retires"] = hashlib.sha256("\n".join(sorted(D)).encode() + b"\n").hexdigest()
res["b_par_dossier_ou_fichier_de_premier_niveau"] = {}
for n in sorted(D):
    k = "/".join(n.split("/")[:2])
    res["b_par_dossier_ou_fichier_de_premier_niveau"][k] = res["b_par_dossier_ou_fichier_de_premier_niveau"].get(k, 0) + 1
res["b_compagnons_sha256_dans_la_difference"] = sum(n.endswith(".sha256") for n in D)
# lien avec le commit source
S_vises = {n for n in source if n.startswith("brouillons/pain-axis-")}
res["source_chemins_brouillons_pain_axis"] = len(S_vises)
res["source_vises_absents_du_public"] = sorted(S_vises - vises)      # retirés dès la v6
res["public_vises_absents_de_la_source"] = sorted(vises - S_vises)
res["public_vises_meme_identifiant_qu_a_la_source"] = sum(public[n] == source[n] for n in vises & S_vises)
# (c) noms
res["c_chemins_neufs_contenant_pain_axis"] = sorted(n for n in N if "pain-axis" in n.lower())
res["c_chemins_neufs_contenant_regard_ou_raisons"] = sorted(n for n in N if "regard-ou-raisons" in n.lower())
ids_vises = {public[n][1] for n in vises} | {source[n][1] for n in S_vises}
res["c_fichiers_neufs_de_meme_identifiant_qu_un_fichier_vise"] = sorted(n for n in N if neuf[n][1] in ids_vises)
# tout fichier neuf vient de la source, à l'identique, sauf les régénérés
res["neufs_absents_de_la_source"] = sorted(N - set(source))
res["neufs_differents_de_la_source"] = sorted(n for n in N & set(source) if neuf[n] != source[n])
print(json.dumps(res, ensure_ascii=False, indent=1))
