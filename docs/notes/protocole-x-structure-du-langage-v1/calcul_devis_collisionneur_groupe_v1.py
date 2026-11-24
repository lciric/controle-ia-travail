#!/usr/bin/env python3
"""Passage mécanique de la garde de motifs (R-5214) et chiffrage du collisionneur groupé (Option B, étage 3 seul).

Exécution recommandée :
  PYTHONDONTWRITEBYTECODE=1 python3 calcul_devis_collisionneur_groupe_v1.py
"""
import contextlib
import io
import json
import math
import pathlib
import sys
import tempfile

DEPOT = pathlib.Path("/home/antigravity/lciric/controle-ia-travail")
SORTIE_DIR = pathlib.Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-structure-langage-et-groupe"
)

sys.path.insert(0, str(DEPOT / "docs/notes/collisionneur-v9"))
sys.path.insert(0, str(DEPOT / "src"))

import collisionneur_v9_v8d as col
from controle_ia import garde_google_v3 as g3

RELEVE_PATH = DEPOT / "docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json"
R = json.loads(RELEVE_PATH.read_text(encoding="utf-8"))
TAUX_PANNE = {"argon": 5 / 62, "astra": 0.0, "carbon": 7 / 56, "neon": 1 / 26, "opus": 2 / 52, "fable": 2 / 62}


def verifier_motifs_dossier(nom, faits_p, question_p):
    """Vérifie motifs_trouves sur les deux fichiers bruts et sur les 3 prompts assemblés du tour E3-T1."""
    txt_f = col.lire_entree(faits_p)
    txt_q = col.lire_entree(question_p)
    mf = col.motifs_trouves(txt_f)
    mq = col.motifs_trouves(txt_q)
    prompts_res = {}
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
        col.ecrire_neuf(td / "faits.md", txt_f)
        col.ecrire_neuf(td / "question-etage3.md", txt_q)
        for l in col.LETTRES:
            esp = col.MODELES[l]["espece"]
            prompt, _ = col.construire_prompt(td, "E3-T1", l, [], set())
            prompts_res[f"E3-T1-{l}({esp})"] = col.motifs_trouves(prompt)
    return {
        "nom": nom,
        "faits": {"nom": faits_p.name, "octets": len(faits_p.read_bytes()), "chars": len(txt_f), "mots": len(txt_f.split()), "motifs": mf},
        "question": {"nom": question_p.name, "octets": len(question_p.read_bytes()), "chars": len(txt_q), "mots": len(txt_q.split()), "motifs": mq},
        "prompts_E3_T1": prompts_res,
    }


def calcul_bras(faits_txt, question_txt, prix_carbon=(4.0, 20.0)):
    """Calcule un bras d'étage 3 (Opus + Carbon + Neon, Option B interface) selon releve-journaux-v2.json."""
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
        for l in col.LETTRES:
            if col.MODELES[l]["espece"] == "carbon":
                col.MODELES[l]["prix"] = prix_carbon
        f_p = td / "faits.md"
        q_p = td / "question-etage3.md"
        col.ecrire_neuf(f_p, faits_txt)
        col.ecrire_neuf(q_p, question_txt)

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            st_natif = col.devis(f_p, q_p, jev=False)
        natif_e3 = st_natif[3]

        tot = {"att": 0.0, "haut": 0.0, "pire": 0.0, "pire_rel": 0.0, "panne": 0.0}
        rows = []
        for tour in ("E3-T1", "E3-T2", "E3-T3"):
            for l in col.LETTRES:
                m = col.MODELES[l]
                esp = m["espece"]
                ids = col.entrees(tour, l, [])
                prompt, _ = col.construire_prompt(td, tour, l, [], set(ids))
                base_len = len(prompt) - sum(len(col.bloc_absent(c, "jamais lancée")) for c in ids)
                enveloppe = sum(len(col.bloc_piece(c, "", "0" * 64)) for c in ids)

                def taille(cid, cle):
                    lp = cid[-1]
                    ep = col.MODELES[lp]["espece"]
                    return R[f"{ep}|{cid[:5]}"][cle]

                car_att = base_len + enveloppe + sum(taille(c, "car_cellule_med") for c in ids)
                car_max = base_len + enveloppe + sum(taille(c, "car_cellule_max") for c in ids)
                r = R[f"{esp}|{tour}"]
                ratio = r["car_par_jeton_entree_med"]
                in_att = car_att / ratio
                in_max = car_max / ratio
                out_att = r["sortie_med"]
                out_p90 = r["sortie_p90"]
                att = in_att / 1e6 * m["prix"][0] + out_att / 1e6 * m["prix"][1]
                haut = in_max / 1e6 * m["prix"][0] + out_p90 / 1e6 * m["prix"][1]
                garde = math.ceil(math.ceil(car_max / 2.5) * 1.01) + 32
                pire = col.cout_pire_garde(m, garde, m["max"])
                pire_rel = col.cout_pire_garde(m, garde, m["max_relance"])
                relances = 2 if (m["fournisseur"] == "gemini" and col.reglage_de_relance(m)[1]) else 1
                avec = pire + relances * pire_rel
                panne = TAUX_PANNE[esp] * pire
                tot["att"] += att
                tot["haut"] += haut
                tot["pire"] += pire
                tot["pire_rel"] += avec
                tot["panne"] += panne
                rows.append({
                    "cellule": col.id_cellule(tour, l),
                    "espece": esp,
                    "in_att": round(in_att),
                    "out_med": out_att,
                    "out_p90": out_p90,
                    "att": att,
                    "haut": haut,
                    "pire": pire,
                    "pire_rel": avec,
                    "panne": panne,
                    "relances": relances,
                })
        # Scénario haut avec 2 coupures de Carbon (T1 et T2) et pointe avant envoi de la dernière cellule E3-T3-reponse-C
        pire_c_t1 = rows[1]["pire"]
        pire_c_t2 = rows[4]["pire"]
        pire_c_t3 = rows[7]["pire"]
        pire_n_t3 = rows[8]["pire"]
        scen_haut_2c = tot["haut"] + pire_c_t1 + pire_c_t2
        dep_avant_t3c = sum(x["haut"] for x in rows[:8]) + pire_c_t1 + pire_c_t2
        pointe_t3c = dep_avant_t3c + pire_n_t3
        plafond_reco = math.ceil(pointe_t3c + 2 * pire_c_t3)
        return {
            "natif_e3": natif_e3,
            "tot": tot,
            "att_avec_pannes": tot["att"] + tot["panne"],
            "scen_haut_2c": scen_haut_2c,
            "pointe_t3c": pointe_t3c,
            "pire_c_t3": pire_c_t3,
            "plafond_reco": plafond_reco,
            "rows": rows,
        }


def main():
    print("=== 1. GARDE DE MOTIFS (collisionneur_v9_v8d.motifs_trouves) ===")
    dossiers_a_verifier = [
        (
            "Dossier 1 — Structure du langage (bras principal)",
            SORTIE_DIR / "faits-neutres-structure-du-langage-v1.md",
            SORTIE_DIR / "question-neutre-collisionneur-structure-du-langage-v1.md",
        ),
        (
            "Dossier 1 — Structure du langage (bras témoin)",
            SORTIE_DIR / "faits-neutres-structure-du-langage-v1.md",
            SORTIE_DIR / "question-temoin-neutre-structure-du-langage-v1.md",
        ),
        (
            "Dommages plantés par un tiers (collisionneur-v2, constat R-5214)",
            DEPOT / "docs/notes/protocole-x-dommages-plantes-tiers-v1/collisionneur-v2/faits-dommages-plantes-tiers-v2.md",
            DEPOT / "docs/notes/protocole-x-dommages-plantes-tiers-v1/collisionneur-v2/question-dommages-plantes-tiers-v2.md",
        ),
        (
            "Marge asymétrique (collisionneur-v2, constat R-5214)",
            DEPOT / "docs/notes/protocole-x-marge-asymetrique-v1/collisionneur-v2/faits-marge-asymetrique-v2.md",
            DEPOT / "docs/notes/protocole-x-marge-asymetrique-v1/collisionneur-v2/question-marge-asymetrique-v2.md",
        ),
        (
            "Programmation de poids (collisionneur-v2, contrôle complémentaire)",
            DEPOT / "docs/notes/protocole-x-programmation-de-poids-v1/collisionneur-v2/faits-programmation-de-poids-v2.md",
            DEPOT / "docs/notes/protocole-x-programmation-de-poids-v1/collisionneur-v2/question-programmation-de-poids-v2.md",
        ),
    ]
    for nom, fp, qp in dossiers_a_verifier:
        res = verifier_motifs_dossier(nom, fp, qp)
        print(f"- {nom}")
        print(f"  faits    : {res['faits']['nom']} ({res['faits']['octets']} o, {res['faits']['chars']} car., {res['faits']['mots']} mots) -> motifs={res['faits']['motifs']}")
        print(f"  question : {res['question']['nom']} ({res['question']['octets']} o, {res['question']['chars']} car., {res['question']['mots']} mots) -> motifs={res['question']['motifs']}")
        print(f"  prompts E3-T1 : {res['prompts_E3_T1']}")

    # Vérification de la synthèse (non envoyée au collisionneur mais contrôlée par transparence)
    synth_p = SORTIE_DIR / "synthese-structure-du-langage-v1.md"
    synth_txt = col.lire_entree(synth_p)
    print(f"- Synthèse Dossier 1 ({synth_p.name}, {len(synth_p.read_bytes())} o, {len(synth_txt)} car., {len(synth_txt.split())} mots) -> motifs={col.motifs_trouves(synth_txt)}")

    # Témoin positif synthétique
    temoin = "Test témoin positif : accord GO-2026-11-24-03, registre R-5214, dossier docs/notes/test.md."
    print(f"- Témoin positif synthétique -> motifs={col.motifs_trouves(temoin)}")

    print("\n=== 2. GARDE GOOGLE V3 (Carbon + Neon, mode flux, étage 3) ===")
    col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
    for esp in ("carbon", "neon"):
        m = [col.MODELES[l] for l in col.LETTRES if col.MODELES[l]["espece"] == esp][0]
        for tour in ("E3-T1", "E3-T2", "E3-T3"):
            mots = col.TOURS[tour]["mots"]
            corps = col.demande_gemini(m, "test", m["max"])
            probs = g3.verifier_reglages_google(esp, corps, m["provision"], mots=mots, mode="flux")
            texte_dispo = m["max"] - m["provision"]
            ratio = g3.JETONS_PAR_MOT_MESURES[esp]
            print(f"  {esp:6s} {tour} : max={m['max']} prov={m['provision']} texte={texte_dispo} ceil({mots}*{ratio})={math.ceil(mots*ratio)} probs={probs}")

    print("\n=== 3. DEVIS OPTION B (Opus 5.5 + Carbon + Neon, étage 3 seul) — DOSSIER 1 ===")
    f1 = col.lire_entree(SORTIE_DIR / "faits-neutres-structure-du-langage-v1.md")
    q1 = col.lire_entree(SORTIE_DIR / "question-neutre-collisionneur-structure-du-langage-v1.md")
    qt1 = col.lire_entree(SORTIE_DIR / "question-temoin-neutre-structure-du-langage-v1.md")

    b1_p = calcul_bras(f1, q1, prix_carbon=(4.0, 20.0))
    b1_t = calcul_bras(f1, qt1, prix_carbon=(4.0, 20.0))
    b1_p_nov = calcul_bras(f1, q1, prix_carbon=(2.0, 10.0))
    b1_t_nov = calcul_bras(f1, qt1, prix_carbon=(2.0, 10.0))

    print("--- Détail cellule par cellule (Bras principal, tarif plein 4/20 Carbon) ---")
    for r in b1_p["rows"]:
        print(
            f"  {r['cellule']:24s} {r['espece']:6s} in_att={r['in_att']:5d} out_med={r['out_med']:7.1f} "
            f"out_p90={r['out_p90']:7.1f} att={r['att']:.4f} haut={r['haut']:.4f} "
            f"pire={r['pire']:.4f} pire_rel={r['pire_rel']:.4f} (rel={r['relances']}) panne={r['panne']:.4f}"
        )

    def resume_couple(label, bp, bt, bp_nov, bt_nov):
        print(f"\n--- {label} ---")
        print(f"  Natif E3 (tarif plein)   : principal={bp['natif_e3']:.4f} + témoin={bt['natif_e3']:.4f} = {bp['natif_e3']+bt['natif_e3']:.4f} USD")
        print(f"  Attendu hors pannes      : {bp['tot']['att']:.4f} + {bt['tot']['att']:.4f} = {bp['tot']['att']+bt['tot']['att']:.4f} USD (avant 1er déc.: {bp_nov['tot']['att']+bt_nov['tot']['att']:.4f} USD)")
        print(f"  Espérance de pannes      : {bp['tot']['panne']:.4f} + {bt['tot']['panne']:.4f} = {bp['tot']['panne']+bt['tot']['panne']:.4f} USD (avant 1er déc.: {bp_nov['tot']['panne']+bt_nov['tot']['panne']:.4f} USD)")
        print(f"  Attendu avec pannes      : {bp['att_avec_pannes']:.4f} + {bt['att_avec_pannes']:.4f} = {bp['att_avec_pannes']+bt['att_avec_pannes']:.4f} USD (avant 1er déc.: {bp_nov['att_avec_pannes']+bt_nov['att_avec_pannes']:.4f} USD)")
        print(f"  Haut hors pannes (p90)   : {bp['tot']['haut']:.4f} + {bt['tot']['haut']:.4f} = {bp['tot']['haut']+bt['tot']['haut']:.4f} USD")
        print(f"  Haut + 2 coupures Carbon : {bp['scen_haut_2c']:.4f} + {bt['scen_haut_2c']:.4f} = {bp['scen_haut_2c']+bt['scen_haut_2c']:.4f} USD (avant 1er déc.: {bp_nov['scen_haut_2c']+bt_nov['scen_haut_2c']:.4f} USD)")
        print(f"  Pointe + marge E3-T3-C   : principal={bp['pointe_t3c']:.4f} ; témoin={bt['pointe_t3c']:.4f} ; pire C-T3={bp['pire_c_t3']:.4f}")
        print(f"  Pire sans relance        : {bp['tot']['pire']:.4f} + {bt['tot']['pire']:.4f} = {bp['tot']['pire']+bt['tot']['pire']:.4f} USD")
        print(f"  Pire avec toutes relances: {bp['tot']['pire_rel']:.4f} + {bt['tot']['pire_rel']:.4f} = {bp['tot']['pire_rel']+bt['tot']['pire_rel']:.4f} USD")
        print(f"  Plafond recommandé/bras  : {bp['plafond_reco']} USD/bras -> {bp['plafond_reco']+bt['plafond_reco']} USD le couple apparié")

    resume_couple("Dossier 1 — Structure du langage (1 couple apparié, 18 cellules)", b1_p, b1_t, b1_p_nov, b1_t_nov)

    print("\n=== 4. SENSIBILITÉ ENTRÉE GROUPÉE (12 000 car. faits + 4 500 car. question) ===")
    f_grp = "a" * 12000
    q_grp = "b" * 4500
    qt_grp = "c" * 4200
    bg_p = calcul_bras(f_grp, q_grp, prix_carbon=(4.0, 20.0))
    bg_t = calcul_bras(f_grp, qt_grp, prix_carbon=(4.0, 20.0))
    bg_p_nov = calcul_bras(f_grp, q_grp, prix_carbon=(2.0, 10.0))
    bg_t_nov = calcul_bras(f_grp, qt_grp, prix_carbon=(2.0, 10.0))
    resume_couple("Scénario G1 — Collisionneur groupé unifié (1 couple apparié, 12k+4,5k car., 18 cellules)", bg_p, bg_t, bg_p_nov, bg_t_nov)

    print("\n=== 5. COMPARAISON DES ARCHITECTURES DU COLLISIONNEUR GROUPÉ (LOT 8 + DOSSIERS 1 À 6) ===")
    for nom, nb_couples, ref_p, ref_t, ref_pn, ref_tn in [
        ("G1 — 1 couple apparié unifié (2 bras, 18 cellules)", 1, bg_p, bg_t, bg_p_nov, bg_t_nov),
        ("G2 — 2 couples appariés par axe (4 bras, 36 cellules, RECOMMANDÉ)", 2, bg_p, bg_t, bg_p_nov, bg_t_nov),
        ("G3 — 6 couples appariés séparés sans regroupement (12 bras, 108 cellules)", 6, b1_p, b1_t, b1_p_nov, b1_t_nov),
    ]:
        att_p = nb_couples * (ref_p["att_avec_pannes"] + ref_t["att_avec_pannes"])
        att_nov = nb_couples * (ref_pn["att_avec_pannes"] + ref_tn["att_avec_pannes"])
        haut_2c = nb_couples * (ref_p["scen_haut_2c"] + ref_t["scen_haut_2c"])
        pire = nb_couples * (ref_p["tot"]["pire"] + ref_t["tot"]["pire"])
        plaf = nb_couples * (ref_p["plafond_reco"] + ref_t["plafond_reco"])
        print(
            f"  {nom}\n"
            f"    Attendu avec pannes : {att_p:6.2f} USD (avant 1er déc.: {att_nov:6.2f} USD) | "
            f"Haut+2C : {haut_2c:6.2f} USD | Pire sans relance : {pire:6.2f} USD | Plafond cumulé : {plaf:3d} USD ({ref_p['plafond_reco']} USD/bras)"
        )

    print("\n=== 6. REPÈRE SUR DOSSIERS EXISTANTS (collisionneur-v2) ===")
    for label, fp, qp in [
        ("Dommages plantés v2", DEPOT / "docs/notes/protocole-x-dommages-plantes-tiers-v1/collisionneur-v2/faits-dommages-plantes-tiers-v2.md", DEPOT / "docs/notes/protocole-x-dommages-plantes-tiers-v1/collisionneur-v2/question-dommages-plantes-tiers-v2.md"),
        ("Marge asymétrique v2", DEPOT / "docs/notes/protocole-x-marge-asymetrique-v1/collisionneur-v2/faits-marge-asymetrique-v2.md", DEPOT / "docs/notes/protocole-x-marge-asymetrique-v1/collisionneur-v2/question-marge-asymetrique-v2.md"),
        ("Programmation de poids v2", DEPOT / "docs/notes/protocole-x-programmation-de-poids-v1/collisionneur-v2/faits-programmation-de-poids-v2.md", DEPOT / "docs/notes/protocole-x-programmation-de-poids-v1/collisionneur-v2/question-programmation-de-poids-v2.md"),
    ]:
        ft = col.lire_entree(fp)
        qt = col.lire_entree(qp)
        r_f = calcul_bras(ft, qt, prix_carbon=(4.0, 20.0))
        r_n = calcul_bras(ft, qt, prix_carbon=(2.0, 10.0))
        print(
            f"  {label:26s} (1 bras) : natif={r_f['natif_e3']:.2f} | att+pannes={r_f['att_avec_pannes']:.2f} "
            f"(avant 1er déc.: {r_n['att_avec_pannes']:.2f}) | pire={r_f['tot']['pire']:.2f} | plafond={r_f['plafond_reco']} USD/bras"
        )


if __name__ == "__main__":
    main()
