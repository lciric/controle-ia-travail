"""Lecteur des résultats de la brique 1, version 1 : imprime les tableaux du rapport (markdown)
à partir de sortie/resultats/*-v1.json, avec l'empreinte de chaque fichier lu.
Usage : python3 -I -B lire_resultats_v1.py > resultats/tableaux-v1.md
"""
import hashlib
import json
from pathlib import Path

ICI = Path(__file__).resolve().parent
RES = ICI / "resultats"


def lire(nom):
    chemin = RES / nom
    emp = hashlib.sha256(chemin.read_bytes()).hexdigest()
    print(f"\n<!-- source : resultats/{nom} sha256 {emp} -->")
    return json.loads(chemin.read_text(encoding="utf-8"))


def f(x, n=2):
    if x is None:
        return "—"
    if isinstance(x, float) and (x != x or x in (float("inf"), float("-inf"))):
        return str(x)
    return f"{x:.{n}f}"


def m(d, cle, n=2):
    return f(d[cle]["moyenne"], n) if cle in d else "—"


def main():
    v = lire("verifications-v1.json")["resultat"]
    print("\n### Vérifications")
    for k, x in v.items():
        print(f"- `{k}` : {x}")

    r = lire("reel-v1.json")["resultat"]
    print("\n### Spectre réel (json, génération 18) et corpus réel d'ancrage")
    print(f"- σ1/σ6 = {f(r['json_ratio'], 3)} ; σ1/σ2 = {f(r['json_ratio_1_2'], 3)} ; σ1/σ5 = {f(r['json_ratio_1_5'], 3)} ;"
          f" σ5/σ6 = {f(r['json_ratio_5_6'], 3)}")
    print(f"- rang effectif exp(H) : sur σ/Σσ = {f(r['json_entropie_effective_sigma'], 3)} ;"
          f" sur σ²/Σσ² = {f(r['json_entropie_effective_sigma_carre'], 3)}")
    print("- part de chaque vecteur propre réel sur (lin, sin, car) : " + " ; ".join(
        f"u{k + 1} ({f(c['lin'])}, {f(c['sin'])}, {f(c['car'])})" for k, c in enumerate(r["json_classes_vecteurs_propres"])))
    print(f"- composantes de u1 sur les 5 coordonnées carrées : {[round(x, 3) for x in r['json_signes_u1_sur_carres']]}")
    print(f"- trajectoire σ1/σ6 (archive) : { {k: round(x, 2) for k, x in r['json_trajectoire_ratio'].items()} }")
    cu = r["json_exemplaires_cos_u1"]
    print(f"- 12 exemplaires réels : ⟨ψ,u1⟩ moyen {f(sum(cu) / len(cu), 3)} (min {f(min(cu), 3)}) ;"
          f" part de |ψ|² sur les carrés {f(sum(c['car'] for c in r['json_exemplaires_classes_psi']) / 12, 4)}")
    print(f"- corpus d'ancrage : {r['n_textes']} textes ({r['n_json']} du json, {r['n_textes'] - r['n_json']} du rapport),"
          f" jetons par texte {min(r['jetons_par_texte'])} à {max(r['jetons_par_texte'])}")
    print("\n| variante | σ1/σ6 code | σ1/σ6 exact | σ1/σ2 | σ5/σ6 | W‖μ‖²/σ1 | R@1 (hasard) | R@1 rang 6 | Spearman | Spearman rang 6 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for nom, a in r["variantes"].items():
        print(f"| {nom} | {f(a['ratio_code'])} | {f(a['ratio_exact'])} | {f(a['ratio_1_2_exact'])} | {f(a['ratio_5_6_exact'])} |"
              f" {f(a['W_mu2_sur_sigma1'], 3)} | {f(a['R1'], 3)} ({f(a['R1_hasard'], 3)}) | {f(a['R1_rang6_code'], 3)} |"
              f" {f(a['spearman_cos_jaccard'], 3)} | {f(a['spearman_rang6_code'], 3)} |")

    e1 = lire("essai1-v1.json")["resultat"]
    print("\n### Essai 1 — balayage en longueur (N = 50, p_commun = 0,3, 10 graines)")
    print("| jetons | part car. de ψ (i) | σ1/σ6 (i) | σ1/σ5 (i) | σ5/σ6 (i) | W‖μ‖²/σ1 (i) | ⟨ψ,μ̂⟩ (i) | σ1/σ6 (ii) | σ1/σ6 (iii) | σ1/σ6 (iv) |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for n, b in e1["par_longueur"].items():
        print(f"| {n} | {f(b['classes_psi_i']['car'], 4)} | {m(b['i'], 'ratio_exact', 1)} | {m(b['i'], 'ratio_1_5_exact', 1)} |"
              f" {m(b['i'], 'ratio_5_6_exact', 1)} | {m(b['i'], 'W_mu2_sur_sigma1', 3)} | {m(b['i'], 'cos_moyen_psi_moyenne', 3)} |"
              f" {m(b['ii'], 'ratio_exact', 1)} | {m(b['iii'], 'ratio_exact', 1)} | {m(b['iv'], 'ratio_exact', 1)} |")
    print("\n| jetons | R@1 (i) | R@1 (ii) | R@1 (iii) | R@1 (iv) | hasard | Spearman (i) | Spearman (ii) | Spearman (iii) | Spearman (iv) |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for n, b in e1["par_longueur"].items():
        print(f"| {n} | {m(b['i'], 'R1', 3)} | {m(b['ii'], 'R1', 3)} | {m(b['iii'], 'R1', 3)} | {m(b['iv'], 'R1', 3)} |"
              f" {m(b['i'], 'R1_hasard', 3)} | {m(b['i'], 'spearman_cos_jaccard', 3)} | {m(b['ii'], 'spearman_cos_jaccard', 3)} |"
              f" {m(b['iii'], 'spearman_cos_jaccard', 3)} | {m(b['iv'], 'spearman_cos_jaccard', 3)} |")

    e2 = lire("essai2-v1.json")["resultat"]
    print("\n### Essai 2 — variantes sur 180 corpus statiques (N ∈ {12, 25, 50}, p_commun ∈ {0 ; 0,3 ; 0,6}, 30 à 300 jetons, 20 graines par cellule)")
    print("| variante | σ1/σ6 exact moy. | min | max | part ≤ 12 | écart rel. max Jacobi-120 | R@1 | R@1 rang 6 | hasard | Spearman | Spearman rang 6 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for nom, a in e2["tous"].items():
        print(f"| {nom} | {m(a, 'ratio_exact', 1)} | {f(a['ratio_exact']['min'], 1)} | {f(a['ratio_exact']['max'], 1)} |"
              f" {f(a['ratio_exact']['part_inf_egal_12'], 2)} | {f(a['ecart_rel_max_sigma_code']['max'], 4)} | {m(a, 'R1', 3)} |"
              f" {m(a, 'R1_rang6_code', 3)} | {m(a, 'R1_hasard', 3)} | {m(a, 'spearman_cos_jaccard', 3)} |"
              f" {m(a, 'spearman_rang6_code', 3)} |")
    print("\nDifférences appariées de R@1 contre (i) (moyenne, IC 95 % par rééchantillonnage) :")
    for nom, d in e2["differences_R1_vs_i"].items():
        print(f"- {nom} − i : {f(d['moyenne'], 3)} [{f(d['ic95'][0], 3)} ; {f(d['ic95'][1], 3)}] (n = {d['n']})")
    print("\nDifférences appariées de R@1 rang 6 contre (i) :")
    for nom, d in e2["differences_R1_rang6_vs_i"].items():
        print(f"- {nom} − i : {f(d['moyenne'], 3)} [{f(d['ic95'][0], 3)} ; {f(d['ic95'][1], 3)}]")
    print("\nDifférences appariées de R@1 contre (ii) :")
    for nom, d in e2["differences_R1_vs_ii"].items():
        print(f"- {nom} − ii : {f(d['moyenne'], 3)} [{f(d['ic95'][0], 3)} ; {f(d['ic95'][1], 3)}]")
    print("\nσ1/σ6 exact par cellule (moyenne ; part ≤ 12) :")
    print("| cellule | i | ii | iii | iv | v | vi | nul |")
    print("|---|---|---|---|---|---|---|---|")
    for cel, b in e2["cellules"].items():
        print(f"| {cel} | " + " | ".join(f"{m(b[x], 'ratio_exact', 1)} ; {f(b[x]['ratio_exact']['part_inf_egal_12'], 2)}"
                                        for x in ["i", "ii", "iii", "iv", "v", "vi", "nul"]) + " |")
    print("\nR@1 par cellule (i / ii / iii / iv / v / nul ; hasard) :")
    print("| cellule | i | ii | iii | iv | v | nul | hasard |")
    print("|---|---|---|---|---|---|---|---|")
    for cel, b in e2["cellules"].items():
        print(f"| {cel} | " + " | ".join(m(b[x], "R1", 3) for x in ["i", "ii", "iii", "iv", "v", "nul"])
              + f" | {m(b['i'], 'R1_hasard', 3)} |")
    ex = e2["cellules"]["N=50|p_commun=0.3"]["exemple_graine0"]
    print("\nStructure des vecteurs propres (N = 50, p_commun = 0,3, graine 0), part sur (lin, sin, car) :")
    for nom in ["i", "ii", "iii", "iv"]:
        print(f"- {nom} : " + " ; ".join(f"u{k + 1} ({f(c['lin'])}, {f(c['sin'])}, {f(c['car'])})"
                                         for k, c in enumerate(ex[nom]["classes_vecteurs_propres"])))
    fl = e2["flexion"]
    print("\nCorpus fléchi (p_flexion = 0,5 ; N = 50 ; p_commun = 0,3 ; 20 graines) :")
    print("| variante | R@1 étalon jetons | R@1 étalon lemmes | Spearman jetons | Spearman lemmes |")
    print("|---|---|---|---|---|")
    for nom in fl["etalon_jetons"]:
        print(f"| {nom} | {m(fl['etalon_jetons'][nom], 'R1', 3)} | {m(fl['etalon_lemmes'][nom], 'R1', 3)} |"
              f" {m(fl['etalon_jetons'][nom], 'spearman_cos_jaccard', 3)} | {m(fl['etalon_lemmes'][nom], 'spearman_cos_jaccard', 3)} |")
    for cle in ("diff_R1_lemmes_v_moins_ii", "diff_R1_lemmes_vi_moins_iv"):
        d = fl[cle]
        print(f"- {cle} : {f(d['moyenne'], 3)} [{f(d['ic95'][0], 3)} ; {f(d['ic95'][1], 3)}]")

    e3 = lire("essai3-v1.json")["resultat"]
    print("\n### Essai 3 — paires de mots (30 fléchies, 30 sans rapport, 30 de même suffixe)")
    print("| représentation | fléchies | sans rapport | même suffixe | aire fl./sans | aire fl./suff. | d′ fl./sans | d′ fl./suff. |")
    print("|---|---|---|---|---|---|---|---|")
    for nom, a in e3["representations"].items():
        st = a["statistiques"]
        print(f"| {nom} | {f(st['flechies']['moyenne'], 3)} ± {f(st['flechies']['ecart'], 3)} |"
              f" {f(st['sans_rapport']['moyenne'], 3)} ± {f(st['sans_rapport']['ecart'], 3)} |"
              f" {f(st['meme_suffixe']['moyenne'], 3)} ± {f(st['meme_suffixe']['ecart'], 3)} |"
              f" {f(a['aire_flechies_vs_sans_rapport'], 3)} | {f(a['aire_flechies_vs_meme_suffixe'], 3)} |"
              f" {f(a['dprime_flechies_vs_sans_rapport'], 2)} | {f(a['dprime_flechies_vs_meme_suffixe'], 2)} |")
    for nom in ("simhash_projection", "simhash_binaire", "sha256_par_jeton"):
        print(f"- Spearman avec le cosinus exact des 3-grammes, {nom} : {f(e3['representations'][nom]['spearman_avec_etalon_3grammes'], 3)}")
    print(f"- table de signes : {e3['table_signes']}")

    e5 = lire("essai5-v1.json")["resultat"]
    print("\n### Essai 5 — corpus structurés (N = 50, 200 à 300 jetons, sans ponts, 10 graines)")
    print("| cellule | σ1/σ6 (iv) ; part ≤ 12 | Spearman (iv) | σ1/σ6 (vi) ; part ≤ 12 | σ1/σ6 nul ; part ≤ 12 | Spearman nul | R@1 (iv) | R@1 nul | hasard |")
    print("|---|---|---|---|---|---|---|---|---|")
    for cel, b in e5["cellules"].items():
        print(f"| {cel} | {m(b['iv'], 'ratio_exact', 1)} ; {f(b['iv']['ratio_exact']['part_inf_egal_12'], 2)} |"
              f" {m(b['iv'], 'spearman_cos_jaccard', 3)} | {m(b['vi'], 'ratio_exact', 1)} ; {f(b['vi']['ratio_exact']['part_inf_egal_12'], 2)} |"
              f" {m(b['nul'], 'ratio_exact', 1)} ; {f(b['nul']['ratio_exact']['part_inf_egal_12'], 2)} |"
              f" {m(b['nul'], 'spearman_cos_jaccard', 3)} | {m(b['iv'], 'R1', 3)} | {m(b['nul'], 'R1', 3)} | {m(b['iv'], 'R1_hasard', 3)} |")

    g = lire("generations-v1.json")["resultat"]
    print("\n### Générations (50 cycles × 40 traces, 20 à 100 jetons, 10 graines par niveau de vocabulaire partagé)")
    for pc, b in g["par_p_commun"].items():
        print(f"\n**p_commun = {pc}** — chemin du pilote égal à l'organisme sur tous les flux : {b['module_egal_pilote_i_tous_flux']} ;"
              f" exemplaires retenus (module) : {sorted(set(b['n_exemplaires_module']))}")
        print("| variante | σ1/σ6 g18 | σ1/σ6 g50 | part ≤ 12 (g50) | σ1/σ5 g18 | σ5/σ6 g18 | Σσ g18 | σ1/σ6 sans troncature g50 |"
              " perte par lot | recouvr. mémoire/vrai g50 | S0‖μ‖²/σ1 g18 | |⟨u1,μ̂⟩| g18 |")
        print("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for nom, a in b["variantes"].items():
            print(f"| {nom} | {f(a['ratio_g18']['moyenne'], 1)} ± {f(a['ratio_g18']['ecart'], 1)} | {f(a['ratio_g50']['moyenne'], 1)} |"
                  f" {f(a['ratio_g50']['part_inf_egal_12'], 2)} | {f(a['ratio_1_5_g18'], 2)} | {f(a['ratio_5_6_g18'], 2)} |"
                  f" {f(a['somme_sigma_g18'], 0)} | {f(a['ratio_vrai_g50'], 1)} | {f(a['perte_lot_moyenne_g2_g50'], 3)} |"
                  f" {f(a['recouvrement_memoire_vrai_g50'], 3)} | {f(a['S0_mu2_sur_sigma1_g18'], 3)} | {f(a['alignement_u1_moyenne_g18'], 3)} |")
        print("\nVecteurs propres à g18, (i), moyenne sur graines, part (lin, sin, car) : " + " ; ".join(
            f"u{k + 1} ({f(c['lin'])}, {f(c['sin'])}, {f(c['car'])})"
            for k, c in enumerate(b["variantes"]["i"]["classes_vecteurs_propres_g18_moyennes"])))
        print("\nCritère de Cauchy (deux d(g) < ε consécutifs) — génération de déclenchement par graine :")
        print("| variante | ε = 0,02 | ε = 0,01 | ε = 0,005 | ε = 0,002 | d(5) | d(10) | d(18) | d(50) |")
        print("|---|---|---|---|---|---|---|---|---|")
        for nom, a in b["variantes"].items():
            if nom.endswith("_exact"):
                continue
            dec = a["cauchy_declenchement"]
            dm = a["cauchy_d_moyen"]
            cel = []
            for eps in ("0.02", "0.01", "0.005", "0.002"):
                gs = [x for x in dec[eps]["generations"] if x is not None]
                med = sorted(gs)[len(gs) // 2] if gs else None
                cel.append(f"méd. {med} [{min(gs) if gs else '—'}–{max(gs) if gs else '—'}]"
                           + (f", jamais {dec[eps]['jamais']}" if dec[eps]["jamais"] else ""))
            print(f"| {nom} | " + " | ".join(cel) + f" | {f(dm['5'], 4)} | {f(dm['10'], 4)} | {f(dm['18'], 4)} | {f(dm['50'], 4)} |")
    t = g["par_p_commun"]["0.3"]["variantes"]["i"]["trajectoire_ratio_moyenne"]
    print("\nTrajectoire moyenne σ1/σ6 sous (i), p_commun = 0,3, générations 13 à 18 : " + ", ".join(f(x, 1) for x in t[12:18]))


if __name__ == "__main__":
    main()
