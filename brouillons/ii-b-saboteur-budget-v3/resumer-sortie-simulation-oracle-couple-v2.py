"""Résumé par programme de la sortie brute de la simulation de l'oracle couplé (aucune donnée du programme).
Usage : python3 resumer-sortie-simulation-oracle-couple-v2.py SORTIE [SECTION]. Version 2 : sait lire une sortie à plusieurs sections de blocs B, C, D (script v3) ;
les colonnes « m=4 » du détail A2 de la v1 deviennent « m=2 »."""
import sys

TOUT = open(sys.argv[1]).read().split("\n")
MARQUES = [k for k, l in enumerate(TOUT) if l.startswith("##########")]
# argument 2 : numéro de la section de blocs B, C, D à résumer (0 : bloc retenu par la règle ; 1 : meilleur bloc couplé admis)
N_SEC = int(sys.argv[2]) if len(sys.argv) > 2 else 0
if MARQUES:
    fin = MARQUES[N_SEC + 1] if N_SEC + 1 < len(MARQUES) else len(TOUT)
    L = TOUT[:MARQUES[0]] + TOUT[MARQUES[N_SEC]:fin]
    print("SECTION :", TOUT[MARQUES[N_SEC]])
else:
    L = TOUT


def bloc(pref):
    i = [k for k, l in enumerate(L) if l.startswith(pref)][0]
    ent, rows, j = L[i + 1].split("\t"), [], i + 2
    while j < len(L) and L[j].strip() and not L[j].startswith("#"):
        rows.append(dict(zip(ent, L[j].split("\t"))))
        j += 1
    return ent, rows


def fl(r, c):
    return float(r[c])


def st(rs, c):
    v = [fl(r, c) for r in rs]
    return f"min {min(v):.3f} moy {sum(v) / len(v):.3f} max {max(v):.3f}"


print(L[0])
print(L[1])
print("\n".join(l for l in L if l.startswith("# CHOIX") or l.startswith("#   signal")))
ent, A = bloc("# A.")
print("\n== A1. oracle sain : arrets et derive, par bloc m (96 cellules) ==")
for m in (1, 2, 4, 8):
    print(f" m={m}")
    for c in ("arret_rangs", "arret_lisibilite", "arret_chaine_estimations_nue", "arret_chaine_estimations_clause", "arret_chaine_rangs_nue",
              "arret_epreuve(estimations+clause)", "arret_epreuve(rangs)"):
        print(f"   {c:36s} {st(A, c + f'[m={m}]')}")
    d = [fl(r, f"moy_e_honnete_pas9[m={m}]") - fl(r, f"moy_e_honnete_pas0[m={m}]") for r in A]
    print(f"   derive de l'exces honnete moyen (pas 9 moins pas 0) : min {min(d):+.3f} max {max(d):+.3f}")
    rap = [fl(r, f"ecart_type_e_honnete[m={m}]") / fl(r, "sigma") for r in A if r["rho"] == "0.9" and r["profil"].startswith("P0")]
    print(f"   ecart type de l'exces honnete / dispersion, ancrage 0,9, profil de reference : min {min(rap):.2f} max {max(rap):.2f}")
print("\n== A2. ce que l'exces mesure : exces mesure / exces vrai (par action, moyenne des cellules du profil de reference, ancre dernier), par ancrage ==")
for ag in ("modere", "modere_ancre", "excessif", "flagrant", "joueur"):
    print(f" {ag}")
    for rho in ("0.0", "0.5", "0.9", "1.0"):
        rs = [r for r in A if r["rho"] == rho and r["profil"].startswith("P0") and r["ancre"] == "dernier"]
        out = []
        for m in (1, 2, 4, 8):
            q = [fl(r, f"exces_mesure_par_action[m={m},{ag}]") / fl(r, f"exces_vrai_par_action[m={m},{ag}]") for r in rs]
            out.append(f"m={m}: {sum(q) / len(q):.2f} ({min(q):.2f} a {max(q):.2f})")
        print(f"   ancrage {rho} : " + " ; ".join(out))
print("\n   detail m=2, modere, profil de reference, ancre dernier : exces mesure / vrai par cellule")
for rho in ("0.0", "0.5", "0.9", "1.0"):
    rs = [r for r in A if r["rho"] == rho and r["profil"].startswith("P0") and r["ancre"] == "dernier"]
    print(f"   ancrage {rho} : " + " ; ".join(f"s{r['sigma']}: {fl(r, 'exces_mesure_par_action[m=2,modere]'):+.3f}/{fl(r, 'exces_vrai_par_action[m=2,modere]'):+.3f}" for r in rs))
print("\n   detail m=2, joueur : exces mesure / vrai par action")
for rho in ("0.0", "0.5", "0.9", "1.0"):
    rs = [r for r in A if r["rho"] == rho and r["profil"].startswith("P0") and r["ancre"] == "dernier"]
    print(f"   ancrage {rho} : " + " ; ".join(f"s{r['sigma']}: {fl(r, 'exces_mesure_par_action[m=2,joueur]'):+.3f}/{fl(r, 'exces_vrai_par_action[m=2,joueur]'):+.3f}" for r in rs))
ent, B = bloc("# B bis")
print("\n== B. zone ou le maitre modere se distingue (1) ou non (0), constantes retenues ; h = taux honnete, m = modere, a = modere ancre, j = joueur ==")
for a in ("dernier", "maximum"):
    for p in ("P0 reference", "P3 ronds 1-2-5"):
        print(f" ancre {a}, profil {p}")
        for rho in ("0.0", "0.5", "0.9", "1.0"):
            rs = [r for r in B if r["ancre"] == a and r["profil"] == p and r["rho"] == rho]
            print(f"   ancrage {rho} : " + " | ".join(f"{r['sigma']}:{r['distingue']} h{fl(r, 'taux_honnete'):.2f} m{fl(r, 'taux_modere'):.2f} a{fl(r, 'taux_modere_ancre'):.2f} "
                                                         f"j{fl(r, 'taux_joueur'):.2f}" for r in rs))
print("   cellules distinguees :", sum(int(r["distingue"]) for r in B), "sur", len(B), "; avec les constantes v1 :", sum(int(r["distingue_v1"]) for r in B))
print("   taux maximal du flagrant :", max(fl(r, "taux_flagrant") for r in B), "; de l'excessif :", max(fl(r, "taux_excessif") for r in B))
print("   exces vrai total des episodes acceptes (decades), cellules distinguees : modere", st([r for r in B if r["distingue"] == "1"], "exces_vrai_total_des_acceptes_modere"),
      "; modere ancre", st([r for r in B if r["distingue"] == "1" and r["exces_vrai_total_des_acceptes_modere_ancre"] != "nan"], "exces_vrai_total_des_acceptes_modere_ancre"),
      "; joueur", st([r for r in B if r["distingue"] == "1" and r["exces_vrai_total_des_acceptes_joueur"] != "nan"], "exces_vrai_total_des_acceptes_joueur"))
ent, C = bloc("# C.")
print("\n== C. epreuve du centrage, m retenu : arret de l'epreuve entiere (statistique de chaine : rangs), par etat et dispersion (moyenne des ancrages 0,5 et 0,9) ==")
for etat in dict.fromkeys(r["etat"] for r in C):
    out = []
    for s in dict.fromkeys(r["sigma"] for r in C):
        rs = [r for r in C if r["etat"] == etat and r["sigma"] == s]
        out.append(f"s{s}: {sum(fl(r, 'arret_epreuve(rangs)') for r in rs) / len(rs):.2f} (chaine seule {sum(fl(r, 'arret_chaine_rangs_nue') for r in rs) / len(rs):.2f})")
    print(f"   {etat} : " + " ; ".join(out))
ent, D = bloc("# D.")
print("\n== D. etalonnage : branches (i)/(ii)/(iii), etat sain, par cellule (profil de reference) ; puis P(aboutit | part) modere / modere ancre ==")
for a in ("dernier", "maximum"):
    for p in ("P0 reference", "P3 ronds 1-2-5"):
        print(f" ancre {a}, profil {p}")
        for rho in ("0.0", "0.5", "0.9", "1.0"):
            rs = [r for r in D if r["ancre"] == a and r["profil"] == p and r["rho"] == rho and r["etat"] == "sain"]
            print(f"   ancrage {rho} : " + " | ".join(f"{r['sigma']}: {r['part_i']}/{r['part_ii']}/{r['part_iii']} ab {r['P(aboutit|part,modere)']}/{r['P(aboutit|part,modere_ancre)']}" for r in rs))
print("   motifs de la branche (iii), etat sain, moyenne par dispersion (k_H ; rapport ; puissance ; tours) :")
for s in dict.fromkeys(r["sigma"] for r in D):
    rs = [r for r in D if r["sigma"] == s and r["etat"] == "sain"]
    print(f"     s{s} : " + " ; ".join(f"{sum(fl(r, c) for r in rs) / len(rs):.2f}" for c in ("motif:k_H", "motif:rapport", "motif:puissance", "motif:tours")))
print("\n   epreuves de sensibilite et de rejet du flagrant : probabilite de passer, m retenu contre m = 8, par etat")
for etat in ("sain", "decalage d'instrument 1 F/T"):
    rs = [r for r in D if r["etat"] == etat]
    for c in ("P(sensibilite passe)", "P(rejet du flagrant passe)"):
        print(f"     {etat} | {c} : m retenu {st(rs, c)} ; m=8 {st(rs, c + '[m=8]')}")
    n = sum(1 for r in rs if fl(r, "P(sensibilite passe)") > fl(r, "P(sensibilite passe)[m=8]") + 0.05 or fl(r, "P(rejet du flagrant passe)") > fl(r, "P(rejet du flagrant passe)[m=8]") + 0.05)
    print(f"     {etat} : cellules ou l'une des deux passe plus souvent (de plus de 0,05) avec le m retenu qu'avec m = 8 : {n} sur {len(rs)}")
rs = [r for r in D if r["etat"] != "sain"]
print("   sous decalage d'instrument 1 F/T : part de la branche (iii)", st(rs, "part_iii"), "; taux honnete", st(rs, "taux_honnete"))
