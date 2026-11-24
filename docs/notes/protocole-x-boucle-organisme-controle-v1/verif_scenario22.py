import json
import math
import pathlib
import sys
import tempfile

sys.path.insert(0, "/home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9")
import collisionneur_v9_v8d as col

base = pathlib.Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle"
)
faits_p = base / "faits-neutres-boucle-organisme-controle-v1.md"
q_p = base / "question-neutre-collisionneur-boucle-organisme-controle-v1.md"
qt_p = base / "question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md"
R = json.load(
    open(
        "/home/antigravity/lciric/controle-ia-travail/docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json"
    )
)
TAUX_PANNE = {"argon": 5 / 62, "astra": 0.0, "carbon": 7 / 56, "neon": 1 / 26, "opus": 2 / 52, "fable": 2 / 62}


def run_s22(qp, abo=True, carbon_prix=(4.0, 20.0), label=""):
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        col.fixer_composition(["opus", "carbon", "neon"], nom_cle_anthropic="X")
        for l in col.LETTRES:
            if col.MODELES[l]["espece"] == "carbon":
                col.MODELES[l]["prix"] = carbon_prix
        col.ecrire_neuf(td / "faits.md", col.lire_entree(faits_p))
        col.ecrire_neuf(td / "question-etage3.md", col.lire_entree(qp))
        cellules = []
        for tour in ("E3-T1", "E3-T2", "E3-T3"):
            for l in col.LETTRES:
                m = col.MODELES[l]
                esp = m["espece"]
                ids = col.entrees(tour, l, [])
                prompt, _ = col.construire_prompt(td, tour, l, [], set(ids))
                base_len = len(prompt) - sum(len(col.bloc_absent(c, "jamais lancée")) for c in ids)
                env = sum(len(col.bloc_piece(c, "", "0" * 64)) for c in ids)

                def taille(c, cle):
                    ep = col.MODELES[c[-1]]["espece"]
                    return R[f"{ep}|{c[:5]}"][cle]

                car_att = base_len + env + sum(taille(c, "car_cellule_med") for c in ids)
                car_max = base_len + env + sum(taille(c, "car_cellule_max") for c in ids)
                r = R[f"{esp}|{tour}"]
                ratio = r["car_par_jeton_entree_med"]
                gratuit = abo and m["fournisseur"] == "anthropic"
                pin, pout = m["prix"]
                att = 0.0 if gratuit else car_att / ratio / 1e6 * pin + r["sortie_med"] / 1e6 * pout
                haut = 0.0 if gratuit else car_max / ratio / 1e6 * pin + r["sortie_p90"] / 1e6 * pout
                garde = math.ceil(math.ceil(car_max / 2.5) * 1.01) + 32
                pire = col.cout_pire_garde(m, garde, m["max"])
                pire_rel = col.cout_pire_garde(m, garde, m["max_relance"])
                relances = (2 if col.reglage_de_relance(m)[1] else 1) if m["fournisseur"] == "gemini" else 1
                marge = max(pire, pire_rel)
                cellules.append(
                    dict(
                        cellule=col.id_cellule(tour, l),
                        espece=esp,
                        gratuit=gratuit,
                        att=att,
                        haut=haut,
                        pire=0.0 if gratuit else pire,
                        pire_avec=0.0 if gratuit else pire + relances * pire_rel,
                        panne=0.0 if gratuit else TAUX_PANNE[esp] * pire,
                        marge=marge,
                    )
                )
        pannes = {"E3-T1-conception": "carbon", "E3-T2-critique-croisee": "carbon"}
        depense, lignes = 0.0, []
        for c in cellules:
            prefixe = c["cellule"][:-2]
            if pannes.get(prefixe) == c["espece"]:
                lignes.append((c["cellule"] + " (coupure)", depense, c["marge"], depense + c["marge"]))
                depense += c["pire"]
            lignes.append((c["cellule"], depense, c["marge"], depense + c["marge"]))
            depense += c["haut"]
        pointe = max(lignes, key=lambda x: x[3])
        coupure = max(c["pire"] for c in cellules if c["espece"] == "carbon")
        plaf_v2 = math.ceil(pointe[3] + 2 * coupure - 1e-9)
        t_att = sum(c["att"] for c in cellules)
        t_pan = sum(c["att"] + c["panne"] for c in cellules)
        t_haut = sum(c["haut"] for c in cellules)
        t_pire = sum(c["pire"] for c in cellules)
        t_rel = sum(c["pire_avec"] for c in cellules)
        print(
            f"{label}:\n"
            f"  att={t_att:.4f}, att+pannes={t_pan:.4f}, haut={t_haut:.4f}, s22_total={depense:.4f},\n"
            f"  pire={t_pire:.4f}, pire_rel={t_rel:.4f}, pointe={pointe},\n"
            f"  coupure_carbon={coupure:.4f}, pointe+2*coup={pointe[3]+2*coupure:.4f}, plaf_v2={plaf_v2}"
        )


run_s22(q_p, True, (4.0, 20.0), "Principal Opt A (4/20)")
run_s22(qt_p, True, (4.0, 20.0), "Temoin Opt A (4/20)")
run_s22(q_p, False, (4.0, 20.0), "Principal Opt B (4/20)")
run_s22(qt_p, False, (4.0, 20.0), "Temoin Opt B (4/20)")
run_s22(q_p, True, (2.0, 10.0), "Principal Opt A (2/10 pre-1dec)")
run_s22(qt_p, True, (2.0, 10.0), "Temoin Opt A (2/10 pre-1dec)")
