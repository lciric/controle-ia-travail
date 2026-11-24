#!/usr/bin/env python3
"""Vérification indépendante R2 du devis du collisionneur groupé, de la garde de motifs (R-5214),
de la garde Google v3 et des fichiers d'entrée réels assemblés pour le Scénario G1.

Exécution :
  PYTHONDONTWRITEBYTECODE=1 python3 verif_r2_independant_v1.py
"""
import contextlib
import hashlib
import io
import json
import math
import pathlib
import sys
import tempfile

DEPOT = pathlib.Path("/home/antigravity/lciric/controle-ia-travail")
DOSSIER_DEPOT = DEPOT / "docs/notes/protocole-x-structure-du-langage-v1"
SCRATCH_AUTEUR = pathlib.Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-structure-langage-et-groupe"
)
OUT_DIR = pathlib.Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/verif-collisionneur-groupe-v1"
)

sys.path.insert(0, str(DEPOT / "docs/notes/collisionneur-v9"))
sys.path.insert(0, str(DEPOT / "src"))

import collisionneur_v9_v8d as col
from controle_ia import garde_google_v3 as g3

RELEVE = json.loads(
    (DEPOT / "docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json").read_text(encoding="utf-8")
)
TAUX_PANNE = {"argon": 5 / 62, "astra": 0.0, "carbon": 7 / 56, "neon": 1 / 26, "opus": 2 / 52, "fable": 2 / 62}


def sha256_file(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verifier_couple_motifs_complet(label: str, fp: pathlib.Path, qp: pathlib.Path) -> dict:
    tf = col.lire_entree(fp)
    tq = col.lire_entree(qp)
    mf = col.motifs_trouves(tf)
    mq = col.motifs_trouves(tq)
    prompts_tous_tours = {}
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
        col.ecrire_neuf(td / "faits.md", tf)
        col.ecrire_neuf(td / "question-etage3.md", tq)
        # Vérifie E3-T1, puis crée des cellules factices saines pour vérifier E3-T2 et E3-T3
        for tour in ("E3-T1", "E3-T2", "E3-T3"):
            for l in col.LETTRES:
                esp = col.MODELES[l]["espece"]
                prompt, _ = col.construire_prompt(td, tour, l, [], set())
                prompts_tous_tours[f"{tour}-{l}({esp})"] = col.motifs_trouves(prompt)
            for l in col.LETTRES:
                cid = col.id_cellule(tour, l)
                col.ecrire_neuf(td / "cellules" / f"{cid}.md", f"Texte neutre de vérification pour {cid}.\n{col.MARQUEUR}\n")
    tous_vides = (mf == []) and (mq == []) and all(v == [] for v in prompts_tous_tours.values())
    return {
        "label": label,
        "faits_nom": fp.name,
        "faits_sha256": sha256_file(fp),
        "faits_octets": len(fp.read_bytes()),
        "faits_chars": len(tf),
        "faits_mots": len(tf.split()),
        "faits_motifs": mf,
        "question_nom": qp.name,
        "question_sha256": sha256_file(qp),
        "question_octets": len(qp.read_bytes()),
        "question_chars": len(tq),
        "question_mots": len(tq.split()),
        "question_motifs": mq,
        "prompts_9_cellules_vides": all(v == [] for v in prompts_tous_tours.values()),
        "statut_sain": tous_vides,
    }


def recalcul_bras_independant(faits_txt: str, question_txt: str, prix_carbon=(4.0, 20.0)) -> dict:
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
        for l in col.LETTRES:
            if col.MODELES[l]["espece"] == "carbon":
                col.MODELES[l]["prix"] = prix_carbon
        fp = td / "faits.md"
        qp = td / "question-etage3.md"
        col.ecrire_neuf(fp, faits_txt)
        col.ecrire_neuf(qp, question_txt)

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            st_natif = col.devis(fp, qp, jev=False)

        cells = []
        for tour in ("E3-T1", "E3-T2", "E3-T3"):
            for l in col.LETTRES:
                m = col.MODELES[l]
                esp = m["espece"]
                ids = col.entrees(tour, l, [])
                prompt, _ = col.construire_prompt(td, tour, l, [], set(ids))
                base = len(prompt) - sum(len(col.bloc_absent(c, "jamais lancée")) for c in ids)
                env = sum(len(col.bloc_piece(c, "", "0" * 64)) for c in ids)
                car_att = base + env + sum(RELEVE[f"{col.MODELES[c[-1]]['espece']}|{c[:5]}"]["car_cellule_med"] for c in ids)
                car_max = base + env + sum(RELEVE[f"{col.MODELES[c[-1]]['espece']}|{c[:5]}"]["car_cellule_max"] for c in ids)
                rel = RELEVE[f"{esp}|{tour}"]
                ratio = rel["car_par_jeton_entree_med"]
                in_att = car_att / ratio
                in_max = car_max / ratio
                pin, pout = m["prix"]
                att = in_att / 1e6 * pin + rel["sortie_med"] / 1e6 * pout
                haut = in_max / 1e6 * pin + rel["sortie_p90"] / 1e6 * pout
                garde = col.garde_entree(math.ceil(car_max / 2.5))
                assert garde == math.ceil(math.ceil(car_max / 2.5) * 1.01) + 32
                pire = garde / 1e6 * pin + (m["max"] + m["provision"]) / 1e6 * pout
                assert abs(pire - col.cout_pire_garde(m, garde, m["max"])) < 1e-12
                pire_rel = garde / 1e6 * pin + (m["max_relance"] + m["provision"]) / 1e6 * pout
                nb_rel = (2 if col.reglage_de_relance(m)[1] else 1) if m["fournisseur"] == "gemini" else 1
                pire_avec = pire + nb_rel * pire_rel
                panne = TAUX_PANNE[esp] * pire
                marge = max(pire, pire_rel)
                cells.append({
                    "cellule": col.id_cellule(tour, l),
                    "espece": esp,
                    "in_att_round": round(in_att),
                    "out_med": rel["sortie_med"],
                    "out_p90": rel["sortie_p90"],
                    "att": att,
                    "haut": haut,
                    "pire": pire,
                    "pire_avec": pire_avec,
                    "panne": panne,
                    "marge": marge,
                    "nb_rel": nb_rel,
                })

        # Simulation exacte envoi par envoi du scénario du 22 novembre (2 coupures Carbon en T1 et T2)
        pannes_22 = {"E3-T1-conception": "carbon", "E3-T2-critique-croisee": "carbon"}
        dep = 0.0
        etapes_22 = []
        for c in cells:
            pref = c["cellule"][:-2]
            if pannes_22.get(pref) == c["espece"]:
                etapes_22.append((c["cellule"] + " (coupure)", dep, c["marge"], dep + c["marge"]))
                dep += c["pire"]
            etapes_22.append((c["cellule"], dep, c["marge"], dep + c["marge"]))
            dep += c["haut"]
        pointe_max = max(etapes_22, key=lambda x: x[3])
        pire_carbon_max = max(c["pire"] for c in cells if c["espece"] == "carbon")
        plafond = math.ceil(pointe_max[3] + 2 * pire_carbon_max - 1e-9)

        tot = {k: sum(c[k] for c in cells) for k in ("att", "haut", "pire", "pire_avec", "panne")}
        return {
            "natif_e3": st_natif[3],
            "tot": tot,
            "att_avec_pannes": tot["att"] + tot["panne"],
            "scen_22_total": dep,
            "pointe_cellule": pointe_max[0],
            "pointe_val": pointe_max[3],
            "etapes_22": etapes_22,
            "pire_carbon_max": pire_carbon_max,
            "plafond": plafond,
            "cells": cells,
        }


def main():
    print("=== A. CONTRÔLE D'IDENTITÉ ENTRE DÉPÔT ET SCRATCH AUTEUR ===")
    for fn in (
        "calcul_devis_collisionneur_groupe_v1.py",
        "faits-neutres-structure-du-langage-v1.md",
        "question-neutre-collisionneur-structure-du-langage-v1.md",
        "question-temoin-neutre-structure-du-langage-v1.md",
        "rapport-garde-motifs-et-devis-collisionneur-groupe-v1.md",
        "sortie-calcul-devis-collisionneur-groupe-v1.txt",
        "synthese-structure-du-langage-v1.md",
    ):
        hd = sha256_file(DOSSIER_DEPOT / fn)
        hs = sha256_file(SCRATCH_AUTEUR / fn)
        assert hd == hs, f"Écart SHA-256 sur {fn}: {hd} != {hs}"
        print(f"  OK {fn} : {hd[:12]}… (identique dépôt == scratch)")

    print("\n=== B. VÉRIFICATION ÉTENDUE DE LA GARDE DE MOTIFS (TOUS TOURS E3-T1/T2/T3 + G1 ASSEMBLÉ + 7 TÉMOINS POSITIFS) ===")
    couples = [
        ("Dossier 1 — principal", DOSSIER_DEPOT / "faits-neutres-structure-du-langage-v1.md", DOSSIER_DEPOT / "question-neutre-collisionneur-structure-du-langage-v1.md"),
        ("Dossier 1 — témoin", DOSSIER_DEPOT / "faits-neutres-structure-du-langage-v1.md", DOSSIER_DEPOT / "question-temoin-neutre-structure-du-langage-v1.md"),
        ("Dommages plantés tiers v2", DEPOT / "docs/notes/protocole-x-dommages-plantes-tiers-v1/collisionneur-v2/faits-dommages-plantes-tiers-v2.md", DEPOT / "docs/notes/protocole-x-dommages-plantes-tiers-v1/collisionneur-v2/question-dommages-plantes-tiers-v2.md"),
        ("Marge asymétrique v2", DEPOT / "docs/notes/protocole-x-marge-asymetrique-v1/collisionneur-v2/faits-marge-asymetrique-v2.md", DEPOT / "docs/notes/protocole-x-marge-asymetrique-v1/collisionneur-v2/question-marge-asymetrique-v2.md"),
        ("Programmation de poids v2", DEPOT / "docs/notes/protocole-x-programmation-de-poids-v1/collisionneur-v2/faits-programmation-de-poids-v2.md", DEPOT / "docs/notes/protocole-x-programmation-de-poids-v1/collisionneur-v2/question-programmation-de-poids-v2.md"),
        ("Scénario G1 assemblé — principal", OUT_DIR / "faits-neutres-groupe-g1-v1.md", OUT_DIR / "question-neutre-collisionneur-groupe-g1-v1.md"),
        ("Scénario G1 assemblé — témoin", OUT_DIR / "faits-neutres-groupe-g1-v1.md", OUT_DIR / "question-temoin-neutre-collisionneur-groupe-g1-v1.md"),
    ]
    for lbl, fp, qp in couples:
        r = verifier_couple_motifs_complet(lbl, fp, qp)
        assert r["statut_sain"], f"MOTIF INTERDIT DÉTECTÉ dans {lbl}: {r}"
        print(
            f"  SAIN {lbl:32s} | faits={r['faits_octets']} o / {r['faits_chars']} car. / {r['faits_mots']} mots (motifs=[]) "
            f"| question={r['question_octets']} o / {r['question_chars']} car. / {r['question_mots']} mots (motifs=[]) | 9 prompts E3=[]"
        )

    # 7 témoins positifs (1 par catégorie de MOTIFS_INTERDITS)
    temoin_7 = (
        "Lazar Ciric session_0123456789abcdef 123e4567-e89b-12d3-a456-426614174000 "
        "a@b.org /home/user/x GO-2026-11-24-03 R-5214"
    )
    trouves_7 = col.motifs_trouves(temoin_7)
    assert len(trouves_7) == 7, f"Attendu 7 catégories détectées, obtenu {trouves_7}"
    print(f"  TÉMOIN POSITIF 7/7 CATÉGORIES ACTIVES : {[c for c, _ in trouves_7]}")

    print("\n=== C. GARDE GOOGLE V3 (MODE FLUX ET REJET ATTENDU DE CARBON EN LOT NON DIFFUSÉ) ===")
    col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
    for esp in ("carbon", "neon"):
        m = [col.MODELES[l] for l in col.LETTRES if col.MODELES[l]["espece"] == esp][0]
        for tour in ("E3-T1", "E3-T2", "E3-T3"):
            corps = col.demande_gemini(m, "invite test", m["max"])
            probs = g3.verifier_reglages_google(esp, corps, m["provision"], mots=col.TOURS[tour]["mots"], mode="flux")
            assert probs == [], f"Défaut garde_google_v3 sur {esp} {tour}: {probs}"
            print(f"  OK {esp:6s} {tour} flux : probs=[]")
    # Vérifie que Carbon en non_diffuse (lot 32768) est bien refusé par la règle des 16 000 jetons de texte
    m_carb = [col.MODELES[l] for l in col.LETTRES if col.MODELES[l]["espece"] == "carbon"][0]
    corps_lot = col.demande_gemini(m_carb, "invite test", 32768)
    probs_lot = g3.verifier_reglages_google("carbon", corps_lot, m_carb["provision"], mots=3500, mode="non_diffuse")
    assert len(probs_lot) >= 1
    print(f"  OK carbon non_diffuse (lot 32768) refusé comme attendu : {probs_lot}")

    print("\n=== D. RECALCUL R2 COMPLET — DOSSIER 1, G1 PARAMÉTRIQUE ET G1 RÉEL ASSEMBLÉ ===")
    f1 = col.lire_entree(DOSSIER_DEPOT / "faits-neutres-structure-du-langage-v1.md")
    q1 = col.lire_entree(DOSSIER_DEPOT / "question-neutre-collisionneur-structure-du-langage-v1.md")
    qt1 = col.lire_entree(DOSSIER_DEPOT / "question-temoin-neutre-structure-du-langage-v1.md")

    fg1 = col.lire_entree(OUT_DIR / "faits-neutres-groupe-g1-v1.md")
    qg1 = col.lire_entree(OUT_DIR / "question-neutre-collisionneur-groupe-g1-v1.md")
    qtg1 = col.lire_entree(OUT_DIR / "question-temoin-neutre-collisionneur-groupe-g1-v1.md")

    for titre, fa, qa, qta in [
        ("Dossier 1 (Structure du langage)", f1, q1, qt1),
        ("Scénario G1 paramétrique (12k + 4,5k / 4,2k car.)", "a" * 12000, "b" * 4500, "c" * 4200),
        ("Scénario G1 RÉEL ASSEMBLÉ (fichiers prêts au lancement)", fg1, qg1, qtg1),
    ]:
        bp = recalcul_bras_independant(fa, qa, prix_carbon=(4.0, 20.0))
        bt = recalcul_bras_independant(fa, qta, prix_carbon=(4.0, 20.0))
        bp_n = recalcul_bras_independant(fa, qa, prix_carbon=(2.0, 10.0))
        bt_n = recalcul_bras_independant(fa, qta, prix_carbon=(2.0, 10.0))
        print(f"\n--- {titre} ---")
        print(f"  Tailles normalisées (car.) : faits={len(fa)} | question_p={len(qa)} | question_t={len(qta)}")
        print(f"  Natif E3 (tarif plein)     : {bp['natif_e3']:.4f} + {bt['natif_e3']:.4f} = {bp['natif_e3']+bt['natif_e3']:.4f} USD")
        print(f"  Attendu hors pannes        : {bp['tot']['att']:.4f} + {bt['tot']['att']:.4f} = {bp['tot']['att']+bt['tot']['att']:.4f} USD (avant 1er déc.: {bp_n['tot']['att']+bt_n['tot']['att']:.4f} USD)")
        print(f"  Espérance de pannes        : {bp['tot']['panne']:.4f} + {bt['tot']['panne']:.4f} = {bp['tot']['panne']+bt['tot']['panne']:.4f} USD (avant 1er déc.: {bp_n['tot']['panne']+bt_n['tot']['panne']:.4f} USD)")
        print(f"  Attendu avec pannes        : {bp['att_avec_pannes']:.4f} + {bt['att_avec_pannes']:.4f} = {bp['att_avec_pannes']+bt['att_avec_pannes']:.4f} USD (avant 1er déc.: {bp_n['att_avec_pannes']+bt_n['att_avec_pannes']:.4f} USD)")
        print(f"  Haut p90 hors pannes       : {bp['tot']['haut']:.4f} + {bt['tot']['haut']:.4f} = {bp['tot']['haut']+bt['tot']['haut']:.4f} USD")
        print(f"  Scénario 22 nov. (Haut+2C) : {bp['scen_22_total']:.4f} + {bt['scen_22_total']:.4f} = {bp['scen_22_total']+bt['scen_22_total']:.4f} USD (avant 1er déc.: {bp_n['scen_22_total']+bt_n['scen_22_total']:.4f} USD)")
        print(f"  Cellule de pointe exacte   : {bp['pointe_cellule']} à {bp['pointe_val']:.4f} USD (témoin: {bt['pointe_val']:.4f} USD) ; + 2×{bp['pire_carbon_max']:.4f} = {bp['pointe_val']+2*bp['pire_carbon_max']:.4f} USD")
        print(f"  Pire sans relance          : {bp['tot']['pire']:.4f} + {bt['tot']['pire']:.4f} = {bp['tot']['pire']+bt['tot']['pire']:.4f} USD")
        print(f"  Pire avec toutes relances  : {bp['tot']['pire_avec']:.4f} + {bt['tot']['pire_avec']:.4f} = {bp['tot']['pire_avec']+bt['tot']['pire_avec']:.4f} USD")
        print(f"  Plafond recommandé         : {bp['plafond']} USD/bras -> {bp['plafond']+bt['plafond']} USD le couple apparié")


if __name__ == "__main__":
    main()
