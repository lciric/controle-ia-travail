"""Tables du rapport, lues dans les résultats empreintés (aucun calcul nouveau) — rétrodiction Swanson v1.

python -I tables_rapport_v1.py > (copie à la main dans le rapport ; chaque table cite son fichier et son empreinte)
"""
import hashlib
import json

R = "/var/tmp/retrodiction-swanson-v1/sortie/resultats"
METHODES = ["S", "AA", "RA", "CN", "PA", "ST", "U", "S_AC", "S_CA"]


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def pc(x):
    return f"{100 * x:.2f}"


def table_methodes(dec, cle="ponctuel", cle_ic="intervalles"):
    lignes = ["| méthode | P@1 000 (%) [IC 95 %] | P@10 000 (%) [IC 95 %] | précision moyenne (%) [IC] | aire [IC] |",
              "|---|---|---|---|---|"]
    for m in METHODES:
        p, ic = dec[cle][m], dec[cle_ic][m]
        cell = []
        for k in ("P@1000", "P@10000", "PM"):
            if p[k] != p[k]:
                cell.append("non définie")
            else:
                cell.append(f"{pc(p[k])} [{pc(ic[k][0])} ; {pc(ic[k][1])}]")
        cell.append(f"{p['aire']:.4f} [{ic['aire'][0]:.4f} ; {ic['aire'][1]:.4f}]")
        lignes.append(f"| {m} | " + " | ".join(cell) + " |")
    return "\n".join(lignes)


def main():
    iss = json.load(open(f"{R}/issues-v1.json"))
    sc = json.load(open(f"{R}/scores-bilan-v1.json"))
    sy = json.load(open(f"{R}/synthese-v1.json"))
    print("empreintes :", "issues-v1.json", sha(f"{R}/issues-v1.json"), "| scores-bilan-v1.json",
          sha(f"{R}/scores-bilan-v1.json"), "| synthese-v1.json", sha(f"{R}/synthese-v1.json"))
    for nom in ("principal", "placebo"):
        dec, b = iss["decoupages"][nom], sc["decoupages"][nom]
        print(f"\n## {nom}\n")
        print(f"docs avant {b['n_docs_avant']} ; après {b['n_docs_apres']} ; V {b['V']} (bigrammes {b['n_bigrammes']}) ;"
              f" top1 {b['n_top1']} ; termes/doc {b['termes_par_document_moyen']:.1f} ;"
              f" spécifiques {b['specifiques_par_champ']} ; candidats {b['candidats_par_champ']} ;"
              f" ΣN_s {sum(b['N_s'])} ; paires {b['n_paires']} ; K nul {b['K_nul']} ; dominées {b['n_dominees']} ;"
              f" distincts avant {b['n_termes_distincts_avant']} ; borne conflit {b['borne_conflit_empreinte']:.2e}")
        print(f"positives {dec['n_positives']} / {dec['n_paires']} ; taux de base {pc(dec['taux_de_base'][0])} %"
              f" [{pc(dec['taux_de_base'][1])} ; {pc(dec['taux_de_base'][2])}]")
        print("\n| strate | N_s | n_s | cooccurrentes avant | taux de base (%) [Wilson] |\n|---|---|---|---|---|")
        for i, s in enumerate(b["strates"]):
            t = dec["taux_de_base_par_strate"].get(s)
            tb = f"{pc(t[0])} [{pc(t[1])} ; {pc(t[2])}] (n = {t[3]})" if t else "—"
            print(f"| {s} | {b['N_s'][i]} | {b['n_s'][i]} | {b['cooccurrentes_par_strate'][i]} | {tb} |")
        print("\n" + table_methodes(dec))
        print(f"\nmeilleur classique : {dec['meilleur_classique']} ; D1 {dec['D1']} ; D2 {dec['D2']}")
        print("différences P@10 000 (points) :")
        for k, v in dec["differences_P10000"]["ponctuel"].items():
            ic = dec["differences_P10000"]["intervalles"][k]
            print(f"  {k} : {100 * v:+.2f} [{100 * ic[0]:+.2f} ; {100 * ic[1]:+.2f}]")
        d = dec["domine"]
        print(f"\nstrate dominée : {d['n_paires']} paires ; taux de base {pc(d['taux_de_base'][0])} %"
              f" [{pc(d['taux_de_base'][1])} ; {pc(d['taux_de_base'][2])}]")
        print(table_methodes(d))
        pe = dec["permutations"]
        print(f"\npermutations : réussi {pe['reussi']} ; erreur-type P@10k {pe['erreur_type_P10000']:.5f} ;"
              f" aire {pe['erreur_type_aire']:.5f}")
        for m, v in pe["par_methode"].items():
            print(f"  {m} : P@10k moyen {pc(v['moyenne_P10000'])} % ({v['ecart_en_erreurs_types_P10000']:+.2f} e.-t.) ;"
                  f" aire {v['moyenne_aire']:.4f} ({v['ecart_en_erreurs_types_aire']:+.2f} e.-t.) ; réussi {v['reussi']}")
        print("\ntête S :")
        for e in dec["exemples_tete"]["S"][:15]:
            print(f"  {e['A']} — {e['C']} ({e['strate']}) n_après={e['n_apres']}")
        m = dec["meilleur_classique"]
        print(f"tête {m} :")
        for e in dec["exemples_tete"][m][:15]:
            print(f"  {e['A']} — {e['C']} ({e['strate']}) n_après={e['n_apres']}")
        print("distribution n_après (0..≥10) :", dec["n_apres_distribution"])
        print("contrôle de référence :", b["controle_reference"])
    print("\nsynthèse :", json.dumps({k: sy[k] for k in ("D1", "D2", "controle_a_permutations")}, ensure_ascii=False))
    print("placebo :", json.dumps(sy["controle_b_placebo"], ensure_ascii=False))


if __name__ == "__main__":
    main()
