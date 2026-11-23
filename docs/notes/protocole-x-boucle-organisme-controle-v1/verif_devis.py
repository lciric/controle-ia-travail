import json
import math
import pathlib
import sys
import tempfile

sys.path.insert(0, "/home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9")
sys.path.insert(0, "/home/antigravity/lciric/controle-ia-travail/src")
import collisionneur_v9_v8d as col
from controle_ia import garde_google_v3 as g3

base = pathlib.Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle"
)
faits_p = base / "faits-neutres-boucle-organisme-controle-v1.md"
q_p = base / "question-neutre-collisionneur-boucle-organisme-controle-v1.md"
qt_p = base / "question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md"

print("=== 0. TAILLE DES FICHIERS D'ENTREE ===")
for p in [faits_p, q_p, qt_p]:
    raw = p.read_bytes()
    txt = col.lire_entree(p)
    print(f"{p.name}: bytes={len(raw)}, chars={len(txt)}, words={len(txt.split())}")

print("\n=== 1. GARDE GOOGLE V3 ET REGLAGES ===")
col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
for esp in ["carbon", "neon"]:
    m = [col.MODELES[l] for l in col.LETTRES if col.MODELES[l]["espece"] == esp][0]
    for tour in ["E3-T1", "E3-T2", "E3-T3"]:
        mots = col.TOURS[tour]["mots"]
        corps = col.demande_gemini(m, "test", m["max"])
        probs = g3.verifier_reglages_google(esp, corps, m["provision"], mots=mots, mode="flux")
        texte_dispo = m["max"] - m["provision"]
        ratio = g3.JETONS_PAR_MOT_MESURES[esp]
        mots_jetons = math.ceil(mots * ratio)
        print(
            f"{esp} {tour}: mots={mots}, max={m['max']}, prov={m['provision']}, "
            f"texte={texte_dispo} (>=16000: {texte_dispo >= 16000}), "
            f"ratio={ratio}, ceil={mots_jetons} (<texte: {mots_jetons < texte_dispo}), probs={probs}"
        )
    lim_nd = g3.LIMITES_SORTIE[esp]["non_diffuse"]
    print(f"{esp} non_diffuse limit={lim_nd}, min_required={m['provision'] + 16000}, ok={lim_nd >= m['provision'] + 16000}")

print("\n=== 2. DEVIS NATIF collisionneur_v9_v8d ===")
for label, qp in [("Bras principal", q_p), ("Bras temoin", qt_p)]:
    print(f"--- {label} ---")
    st = col.devis(faits_p, qp, jev=False)
    print(f"E3 natif total: {st[3]:.6f}")

print("\n=== 3. RECALCUL PAR FORMULE EMPIRIQUE (releve-journaux-v2.json) ===")
R = json.load(
    open(
        "/home/antigravity/lciric/controle-ia-travail/docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json"
    )
)
TAUX_PANNE = {"argon": 5 / 62, "astra": 0.0, "carbon": 7 / 56, "neon": 1 / 26, "opus": 2 / 52, "fable": 2 / 62}


def calc_arm(qp, abonnement=True, label=""):
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
        col.ecrire_neuf(td / "faits.md", col.lire_entree(faits_p))
        col.ecrire_neuf(td / "question-etage3.md", col.lire_entree(qp))
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
                gratuit = abonnement and m["fournisseur"] == "anthropic"
                in_att = car_att / ratio
                in_max = car_max / ratio
                out_att = r["sortie_med"]
                out_p90 = r["sortie_p90"]
                att = 0.0 if gratuit else in_att / 1e6 * m["prix"][0] + out_att / 1e6 * m["prix"][1]
                haut = 0.0 if gratuit else in_max / 1e6 * m["prix"][0] + out_p90 / 1e6 * m["prix"][1]
                garde = math.ceil(math.ceil(car_max / 2.5) * 1.01) + 32
                pire = col.cout_pire_garde(m, garde, m["max"])
                pire_rel = col.cout_pire_garde(m, garde, m["max_relance"])
                relances = 2 if (m["fournisseur"] == "gemini" and col.reglage_de_relance(m)[1]) else 1
                avec = pire + relances * pire_rel
                panne = TAUX_PANNE[esp] * pire
                if gratuit:
                    pire_c, avec_c, panne_c = 0.0, 0.0, 0.0
                else:
                    pire_c, avec_c, panne_c = pire, avec, panne
                tot["att"] += att
                tot["haut"] += haut
                tot["pire"] += pire_c
                tot["pire_rel"] += avec_c
                tot["panne"] += panne_c
                rows.append(
                    (
                        col.id_cellule(tour, l),
                        esp,
                        round(in_att),
                        out_att,
                        out_p90,
                        att,
                        haut,
                        pire_c,
                        avec_c,
                        panne_c,
                        garde,
                        pire,
                        relances,
                    )
                )
        print(f"--- {label} (abonnement={abonnement}) ---")
        for row in rows:
            print(
                f"  {row[0]:24s} in_att={row[2]:5d} out_med={row[3]:7.1f} out_p90={row[4]:7.1f} "
                f"att={row[5]:.4f} haut={row[6]:.4f} pire={row[7]:.4f} pire_rel={row[8]:.4f} (rel={row[12]}) "
                f"panne={row[9]:.4f} raw_pire={row[11]:.4f}"
            )
        print(
            f"  SUM: att={tot['att']:.4f} panne={tot['panne']:.4f} att+panne={tot['att']+tot['panne']:.4f} "
            f"haut={tot['haut']:.4f} pire={tot['pire']:.4f} pire_rel={tot['pire_rel']:.4f}"
        )
        # Check scenario haut + 2 coupures Carbon (T1 et T2)
        pire_c_t1 = rows[1][11]
        pire_c_t2 = rows[4][11]
        pire_c_t3 = rows[7][11]
        scen_haut_2_coup = tot["haut"] + pire_c_t1 + pire_c_t2
        # Pointe avant envoi T3-B (si tout avant T3-B a coûté haut + 2 coupures, et T3-A gratuit ou haut)
        dep_avant_t3b = sum(r[6] for r in rows[:7]) + pire_c_t1 + pire_c_t2
        pointe_t3b = dep_avant_t3b + pire_c_t3
        print(
            f"  SCEN_HAUT_2_COUP_CARBON (T1+T2={pire_c_t1+pire_c_t2:.4f}): {scen_haut_2_coup:.4f} | "
            f"dep_avant_t3b={dep_avant_t3b:.4f} + pire_c_t3({pire_c_t3:.4f}) = {pointe_t3b:.4f}"
        )
        # Check tarif 2/10 pour Carbon avant 1er decembre
        return rows, tot


calc_arm(q_p, True, "Bras principal Option A")
calc_arm(qt_p, True, "Bras temoin Option A")
calc_arm(q_p, False, "Bras principal Option B")
calc_arm(qt_p, False, "Bras temoin Option B")
