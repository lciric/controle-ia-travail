"""Calcul du devis du service de la question v8 au collisionneur (étage III seul), sans réseau.
Invites de l'étage III construites par le moteur v8m (copie extraite de la branche runs/collisionneurs-reprise-v8d-v1,
420394f9…) dans un dossier temporaire ; pièces des tours III.2 et III.3 de tailles relevées (médiane : attendu ;
maximum : borne réaliste) sur les journaux (releve-journaux-v2.json) ; sorties attendues = médiane relevée par espèce et
par tour ; pire cas = formule du moteur (garde d'entrée à 2,5 caractères par jeton, tolérance 1 % + 32, plafond plus
provision au prix de sortie). Usage : python calcul_devis_v8_v2.py MOTEUR.py QUESTION_SERVIE.md RELEVE.json"""
import importlib.util, json, math, sys, tempfile
from pathlib import Path
moteur, question, releve = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("v8m", moteur); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
R = json.load(open(releve, encoding="utf-8"))
TAUX_PANNE = {"argon": 5 / 62, "astra": 0.0, "carbon": 7 / 56, "neon": 1 / 26, "opus": 2 / 52, "fable": 2 / 62}
def calcul(especes, sortie_max, abonnement, etiquette):
    tmp = Path(tempfile.mkdtemp(dir=str(Path(releve).parent)))
    v.fixer_composition(especes, nom_cle_anthropic="X", sortie_max=sortie_max)
    texte = v.lire_entree(question)
    v.ecrire_neuf(tmp / "faits.md", texte); v.ecrire_neuf(tmp / "question-etage3.md", texte)
    lignes, tot = [], {"att": 0.0, "pire": 0.0, "pire_rel": 0.0, "panne": 0.0, "max_cell": 0.0}
    for tour in ("E3-T1", "E3-T2", "E3-T3"):
        for l in v.LETTRES:
            m = v.MODELES[l]; esp = m["espece"]
            ids = v.entrees(tour, l, [])
            prompt, _ = v.construire_prompt(tmp, tour, l, [], set(ids))
            base = len(prompt) - sum(len(v.bloc_absent(c, "jamais lancée")) for c in ids)
            enveloppe = sum(len(v.bloc_piece(c, "", "0" * 64)) for c in ids)
            def taille(cid, cle):
                lettre_p = cid[-1]; esp_p = v.MODELES[lettre_p]["espece"]
                return R[f"{esp_p}|{cid[:5]}"][cle]
            car_att = base + enveloppe + sum(taille(c, "car_cellule_med") for c in ids)
            car_max = base + enveloppe + sum(taille(c, "car_cellule_max") for c in ids)
            r = R[f"{esp}|{tour}"]
            ratio = r["car_par_jeton_entree_med"]
            gratuit = abonnement and m["fournisseur"] == "anthropic"
            in_att = car_att / ratio
            out_att = r["sortie_med"]
            att = 0.0 if gratuit else in_att / 1e6 * m["prix"][0] + out_att / 1e6 * m["prix"][1]
            haut = 0.0 if gratuit else (car_max / ratio) / 1e6 * m["prix"][0] + r["sortie_p90"] / 1e6 * m["prix"][1]
            tot["haut"] = tot.get("haut", 0.0) + haut
            cle = {"gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY_2", "anthropic": "clé d'Anthropic"}[m["fournisseur"]]
            tot.setdefault("par_cle", {}); tot["par_cle"][cle] = tot["par_cle"].get(cle, 0.0) + att
            garde = math.ceil(math.ceil(car_max / 2.5) * 1.01) + 32
            pire = v.cout_pire_garde(m, garde, m["max"])
            pire_relance = v.cout_pire_garde(m, garde, m["max_relance"])
            if m["fournisseur"] == "gemini":
                relances = 2 if v.reglage_de_relance(m)[1] else 1
            else:
                relances = 1
            avec = pire + relances * pire_relance
            panne = TAUX_PANNE.get(esp, 0) * pire
            if gratuit:
                pire_compte, avec, panne = 0.0, 0.0, 0.0
                pire_kit = max(pire, pire_relance)   # contrôle avant le kit : marge exigée, jamais dépensée
            else:
                pire_compte, pire_kit = pire, max(pire, pire_relance)
            tot["att"] += att; tot["pire"] += pire_compte; tot["pire_rel"] += avec; tot["panne"] += panne
            tot["max_cell"] = max(tot["max_cell"], pire_kit)
            lignes.append((v.id_cellule(tour, l), m["id"], car_att, car_max, round(in_att), out_att, att, pire_compte,
                           avec, panne, pire_kit, gratuit))
    print(f"\n### {etiquette}")
    print("cellule | modèle | car. attendus | car. bornés | entrée attendue (jetons) | sortie attendue (jetons) | attendu USD | pire sans relance | pire avec relances | espérance de panne | marge exigée avant envoi")
    for x in lignes:
        print(f"{x[0]} | {x[1]}{' (abonnement)' if x[11] else ''} | {x[2]} | {x[3]} | {x[4]} | {x[5]} | {x[6]:.2f} | {x[7]:.2f} | {x[8]:.2f} | {x[9]:.2f} | {x[10]:.2f}")
    print(f"TOTAL attendu (réussites) {tot['att']:.2f} ; espérance des pannes comptées au pire {tot['panne']:.2f} ; "
          f"attendu avec pannes {tot['att'] + tot['panne']:.2f} ; pire sans relance {tot['pire']:.2f} ; "
          f"pire avec relances {tot['pire_rel']:.2f} ; plus grande marge exigée avant un envoi {tot['max_cell']:.2f} ; haut (90e centile des sorties, pièces maximales) {tot['haut']:.2f} ; attendu par clé " + str({k: round(x, 2) for k, x in tot['par_cle'].items()}))
    return tot
r = {}
r["a-sortie-max"] = calcul(["opus", "argon", "astra", "carbon", "neon"], True, True, "(a) cinq espèces, Opus par l'abonnement, --sortie-max")
r["a-sans"] = calcul(["opus", "argon", "astra", "carbon", "neon"], False, True, "(a') cinq espèces, Opus par l'abonnement, sans --sortie-max")
r["b-sortie-max"] = calcul(["fable", "opus", "argon", "astra", "carbon", "neon"], True, True, "(b) six espèces, Fable et Opus par l'abonnement, --sortie-max")
r["c-v8d"] = calcul(["fable", "opus", "argon", "astra", "carbon", "neon"], False, False, "(c) six espèces, Fable et Opus par l'interface, réglages du v8d (sans --sortie-max)")
json.dump(r, open(Path(releve).parent / "calcul-devis-v8-v1-totaux.json", "w"), indent=1)
