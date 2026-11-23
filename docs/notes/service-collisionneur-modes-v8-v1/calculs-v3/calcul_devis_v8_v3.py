"""Calcul du devis v2 du service de la question v8 au collisionneur (étage III seul), sans réseau.
v3 du calcul (devis v2) : copie de la logique de calcul_devis_v8_v2.py (8bfdbca7…), sur la VERSION SERVIE ; ajoute,
pour les défauts D-1, D-4, D-5 et D-7 de la contre-lecture (230c7b4e…) :
- le coût « haut » par cellule (90e centile des sorties, pièces au maximum relevé) et l'ordre des envois ;
- le scénario des pannes du 22 novembre (deux coupures de Carbon, aux tours III.1 et III.2, comptées au pire ; un refus
  d'Argon au tour III.1, qui remplace la cellule réussie et n'ajoute rien) sur le chemin haut, et la lecture du plafond
  envoi par envoi : dépense comptée avant l'envoi + marge exigée ; nombre de coupures de Carbon de plus tolérées ;
- le rapprochement empirique : dépense comptée des deux dossiers « conscience et anesthésie » (journaux), plus le
  surcroît d'entrée de la v8 servie, cellule par cellule, à partir de leurs comptes d'entrée relevés ;
- l'option (b′) : Fable seul espèce Claude, par l'abonnement, après le 29 novembre ;
- aucune écriture hors du dossier donné par --sortie (D-7 : jamais dans le dossier versé).
Usage : python3 calcul_devis_v8_v3.py MOTEUR_V8M.py QUESTION_SERVIE.md RELEVE_V2.json DOSSIER_SORTIE"""
import importlib.util, json, math, sys, tempfile, shutil, subprocess
from pathlib import Path
moteur, question, releve, sortie = sys.argv[1:5]
sortie = Path(sortie); sortie.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location("v8m", moteur); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
R = json.load(open(releve, encoding="utf-8"))
TAUX_PANNE = {"argon": 5 / 62, "astra": 0.0, "carbon": 7 / 56, "neon": 1 / 26, "opus": 2 / 52, "fable": 2 / 62}
DEPOT = "/home/user/controle-ia-travail"
BR = "origin/runs/collisionneurs-reprise-v8d-v1"
DOSSIERS_22 = ["runs/collisionneur-protocole-x-conscience-anesthesie-neutre-abonnement-v1-20261122-153110",
               "runs/collisionneur-protocole-x-conscience-anesthesie-v3-reserve-abonnement-v1-20261122-153110"]


def calcul(especes, sortie_max, abonnement):
    tmp = Path(tempfile.mkdtemp(dir=str(sortie)))
    try:
        v.fixer_composition(especes, nom_cle_anthropic="X", sortie_max=sortie_max)
        texte = v.lire_entree(question)
        v.ecrire_neuf(tmp / "faits.md", texte); v.ecrire_neuf(tmp / "question-etage3.md", texte)
        cellules = []
        for tour in ("E3-T1", "E3-T2", "E3-T3"):
            for l in v.LETTRES:
                m = v.MODELES[l]; esp = m["espece"]
                ids = v.entrees(tour, l, [])
                prompt, _ = v.construire_prompt(tmp, tour, l, [], set(ids))
                base = len(prompt) - sum(len(v.bloc_absent(c, "jamais lancée")) for c in ids)
                env = sum(len(v.bloc_piece(c, "", "0" * 64)) for c in ids)
                taille = lambda c, cle: R[f"{v.MODELES[c[-1]]['espece']}|{c[:5]}"][cle]
                car_att = base + env + sum(taille(c, "car_cellule_med") for c in ids)
                car_max = base + env + sum(taille(c, "car_cellule_max") for c in ids)
                r = R[f"{esp}|{tour}"]; ratio = r["car_par_jeton_entree_med"]
                gratuit = abonnement and m["fournisseur"] == "anthropic"
                pin, pout = m["prix"]
                att = 0.0 if gratuit else car_att / ratio / 1e6 * pin + r["sortie_med"] / 1e6 * pout
                haut = 0.0 if gratuit else car_max / ratio / 1e6 * pin + r["sortie_p90"] / 1e6 * pout
                garde = math.ceil(math.ceil(car_max / 2.5) * 1.01) + 32
                pire = v.cout_pire_garde(m, garde, m["max"]); pire_rel = v.cout_pire_garde(m, garde, m["max_relance"])
                relances = (2 if v.reglage_de_relance(m)[1] else 1) if m["fournisseur"] == "gemini" else 1
                marge = max(pire, pire_rel)
                cellules.append(dict(cellule=v.id_cellule(tour, l), espece=esp, id=m["id"], gratuit=gratuit,
                                     car_att=car_att, car_max=car_max, entree_att=round(car_att / ratio),
                                     sortie_med=r["sortie_med"], sortie_p90=r["sortie_p90"], att=att, haut=haut,
                                     pire=0.0 if gratuit else pire, pire_avec=0.0 if gratuit else pire + relances * pire_rel,
                                     panne=0.0 if gratuit else TAUX_PANNE.get(esp, 0) * pire, marge=marge))
        return cellules
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def scenario_22(cellules, plafonds):
    """Chemin haut + pannes du 22 novembre ; lecture du plafond envoi par envoi."""
    pannes = {"E3-T1-conception": "carbon", "E3-T2-critique-croisee": "carbon"}
    depense, lignes, pire_carbon = 0.0, [], []
    for c in cellules:
        prefixe = c["cellule"][:-2]
        if pannes.get(prefixe) == c["espece"]:  # premier essai coupé, compté au pire, puis relance réussie
            lignes.append((c["cellule"] + " (coupure)", depense, c["marge"], depense + c["marge"]))
            depense += c["pire"]; pire_carbon.append(c["pire"])
        lignes.append((c["cellule"], depense, c["marge"], depense + c["marge"]))
        depense += c["haut"]  # un refus d'Argon au tour III.1 remplace la cellule réussie : rien n'est ajouté
    pointe = max(lignes, key=lambda x: x[3])
    coupure = max(c["pire"] for c in cellules if c["espece"] == "carbon")
    tolerees = {p: math.floor((p - pointe[3]) / coupure + 1e-9) for p in plafonds}
    return dict(total=depense, pointe=pointe, lignes=lignes, coupure_carbon=coupure, tolerees=tolerees)


def empirique(cellules):
    """Dépense comptée des deux dossiers du 22 novembre, plus le surcroît d'entrée de la v8 servie (comptes relevés)."""
    rendu = []
    for d in DOSSIERS_22:
        j = subprocess.run(["git", "-C", DEPOT, "show", f"{BR}:{d}/journal.jsonl"], capture_output=True, text=True,
                           check=True).stdout
        tot, entrees = 0.0, {}
        for x in j.splitlines():
            if not x.strip():
                continue
            e = json.loads(x); tot += e.get("cout_usd", 0) or 0
            if "essai" in e and e.get("id_reponse") != "abonnement" and e.get("statut") == "OK":
                entrees[(e["espece"], e["cellule"][:5])] = e.get("compte_entree") or 0
        delta = 0.0
        for c in cellules:
            if c["gratuit"]:
                continue
            k = (c["espece"], c["cellule"][:5])
            if k in entrees:
                prix = v.CATALOGUE[c["espece"]]["prix"][0]
                delta += (c["entree_att"] - entrees[k]) / 1e6 * prix
        rendu.append(dict(dossier=d.split("/")[-1], depense=round(tot, 2), surcroit_entree=round(delta, 2),
                          ramene_a_la_v8=round(tot + delta, 2)))
    return rendu


options = {
    "a": (["opus", "argon", "astra", "carbon", "neon"], True, True, "(a) cinq espèces maintenant, Opus par l'abonnement, --sortie-max"),
    "a-sans": (["opus", "argon", "astra", "carbon", "neon"], False, True, "(a) sans --sortie-max"),
    "b-prime": (["fable", "argon", "astra", "carbon", "neon"], True, True, "(b′) cinq espèces après le 29, Fable seul par l'abonnement, --sortie-max"),
    "b-six": (["fable", "opus", "argon", "astra", "carbon", "neon"], True, True, "(b) six espèces après le 29, Fable et Opus par l'abonnement, --sortie-max"),
    "c-cinq": (["opus", "argon", "astra", "carbon", "neon"], False, False, "(c) moteur v8d tel quel, cinq espèces par l'interface"),
    "c-six": (["fable", "opus", "argon", "astra", "carbon", "neon"], False, False, "(c) moteur v8d tel quel, six espèces par l'interface"),
}
resultats, lignes_txt = {}, []
for cle, (especes, smax, abo, nom) in options.items():
    cel = calcul(especes, smax, abo)
    T = {k: sum(c[k] for c in cel) for k in ("att", "haut", "pire", "pire_avec", "panne")}
    T["marge_max"] = max(c["marge"] for c in cel)
    T["attendu_avec_pannes"] = T["att"] + T["panne"]
    T["haut_avec_pannes"] = T["haut"] + T["panne"]
    sc = scenario_22(cel, (21, 25, 26, 28, 33))
    T["haut_pannes_22_novembre"] = sc["total"]
    T["pointe_22_novembre"] = sc["pointe"][3]
    T["plafond_formule_v1"] = math.ceil(T["haut_avec_pannes"] + T["marge_max"] + 2 * sc["coupure_carbon"] - 1e-9)
    T["plafond_formule_v2"] = math.ceil(sc["pointe"][3] + 2 * sc["coupure_carbon"] - 1e-9)
    T["coupures_carbon_de_plus_tolerees"] = sc["tolerees"]
    resultats[cle] = dict(nom=nom, totaux=T, cellules=cel, scenario=sc["lignes"], empirique=empirique(cel) if cle == "a" else None)
    lignes_txt.append(f"\n### {nom}")
    lignes_txt.append("cellule | modèle | entrée attendue | sortie médiane | sortie 90e centile | attendu | haut | pire sans relance | pire avec relances | espérance de panne | marge avant l'envoi")
    for c in cel:
        lignes_txt.append(f"{c['cellule']} | {c['id']}{' (abonnement)' if c['gratuit'] else ''} | {c['entree_att']} | {c['sortie_med']:.0f} | {c['sortie_p90']:.0f} | {c['att']:.2f} | {c['haut']:.2f} | {c['pire']:.2f} | {c['pire_avec']:.2f} | {c['panne']:.2f} | {c['marge']:.2f}")
    lignes_txt.append("TOTAUX " + json.dumps({k: (round(x, 2) if isinstance(x, float) else x) for k, x in T.items()}, ensure_ascii=False))
    lignes_txt.append("SCÉNARIO 22 NOVEMBRE (chemin haut ; envoi | dépense comptée avant | marge | somme) :")
    for n, dep, mar, s in sc["lignes"]:
        lignes_txt.append(f"  {n} | {dep:.2f} | {mar:.2f} | {s:.2f}")
    lignes_txt.append(f"  pointe : {sc['pointe'][0]} à {sc['pointe'][3]:.2f} ; coupure de Carbon comptée au plus {sc['coupure_carbon']:.2f} ; coupures de plus tolérées avant la pointe : {sc['tolerees']}")
    if cle == "a":
        lignes_txt.append("EMPIRIQUE (dossiers du 22 novembre ramenés à la v8 servie) : " + json.dumps(resultats[cle]["empirique"], ensure_ascii=False))
texte = "\n".join(lignes_txt) + "\n"
(sortie / "sortie-calcul-devis-v8-v3.txt").write_text(texte, encoding="utf-8")
(sortie / "calcul-devis-v8-v3-totaux.json").write_text(json.dumps({k: dict(nom=x["nom"], totaux=x["totaux"], empirique=x["empirique"]) for k, x in resultats.items()}, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
print(texte)
