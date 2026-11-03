#!/usr/bin/env python3
"""Devis de la course Kirchner Q2 (trois variantes) et construction des trois configurations — v1.
(Kit Kirchner Q2, v1, dérivé à l'octet près des substitutions de nom du kit Heimersheim — branche outils/course-heimersheim-v1 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions antérieures ci-dessous sont celles du kit Heimersheim.)

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel, aucune dépense. Une seule source de calcul : le plan
d'appels et les pires cas de `course_kirchner_v1.py`.

Hypothèses (chaque nombre est marqué) :
- jetons d'entrée attendus = caractères / r, r **mesuré** au second tour réel (journaux des relais du run
  `donnees/mini-course-kimi-argon-v1/run-20261101-2146/`, branche `donnees/recuperation-collisionneur-v8-v1`, empreintes
  vérifiées ci-dessous) : médiane des appels d'Argon (caractères / jetons d'entrée) ; transposé à Claude et Astra : SUPPOSÉ ;
- pire cas d'entrée = caractères / 3 (formule des commandes) ; Kimi : (octets + 1024), octets ≤ 2 × caractères ;
- une fiche servie : 2 500 caractères attendus (calcul : entrées des lecteurs du second tour moins leur consigne, médiane),
  12 000 au pire cas (SUPPOSÉ, borne des plafonds de session) ;
- jetons de sortie attendus par rôle : SUPPOSÉ (réflexion adaptative, effort « high »), mis en regard des mesures du second
  tour (Argon et Kimi) imprimées à côté ; pire cas = sortie maximale du rôle (options des commandes) ;
- toutes les fiches reçoivent un passeport (pire cas), chaque bras a ses k paires, chaque fusion est aiguillée et jugée ;
- contrôles d'avant course : un par modèle, plafond de session 0,05 USD chacun (pire cas).

S17 (plafond TECHNIQUE, garde contre une boucle ; Lazar n'a pas de plafond) : 60 USD, ou l'entier supérieur à 1,2 fois le
plus grand pire cas des trois variantes s'il dépasse 60 ; le même S17 pour les trois (une seule ligne de GO sert la variante
retenue). Arrêt d'étape : 0,9 × S17 (proportion de la mini-course). Plafonds propres des relais : 1,2 × la part au pire cas
de chaque relais, arrondie au dixième supérieur, au moins 2 USD pour Kimi et 3 USD pour Argon (et au plus 5 et 10), le
relais Claude prenant le reste de S17.

  python3 -I -B calcul_devis_course_kirchner_v1.py devis --second-tour DOSSIER --sortie-texte F.txt --sortie-json F.json
  python3 -I -B calcul_devis_course_kirchner_v1.py configurations --second-tour DOSSIER --dossier DOSSIER_DES_CONFIGURATIONS
DOSSIER (second tour) : les trois journaux, extraits sans texte par `git show` (commande au LISEZMOI).
"""

import argparse
import hashlib
import json
import math
import os
import statistics
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)
sys.path.insert(0, ICI)
import course_kirchner_v1 as ch  # noqa: E402

VERSION = "devis-course-kirchner-v1"
JOURNAUX = {"relais-argon-journal.jsonl": "2d43023df6de2934a4e2a96702a33912522339b826fbafced247983d4a98d9fb",
            "relais-kimi-journal.jsonl": "47e3643d28be481b2c5c00eda4ab9dbc544545ff9f0266739430b246b774fb8d",
            "registre-depense-cumulee-v1.jsonl": "5f3c6e0ceccda73c72d3f97a78e34ec7375825b41563de606158b10ca470d265"}
FICHE_ATTENDUE = 2500
SORTIE_ATTENDUE = {"proposeur": 12000, "aiguilleur": 1500, "juge": 2000, "lecteur": 1500, "fusion": 6000}  # SUPPOSÉ
SORTIE_ATTENDUE_KIMI_PROPOSEUR = None   # calcul sur mesure (8 / 6 du proposeur Kimi du second tour), posé par mesures()
SORTIE_ATTENDUE_ARGON_PROPOSEUR = None  # idem pour Argon
K_PAIRES = 4
CONTROLE_USD = 0.05
PLANCHER_RELAIS = {"kimi": 2.0, "argon": 3.0}  # marge au-dessus de la part au pire cas (Kimi ≤ 5, Argon ≤ 10)
PIECES = os.path.join(ICI, "pieces")


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def mesures(dossier):
    """Mesures du second tour réel (aucun texte lu : jetons, caractères, octets seulement)."""
    for nom, attendu in JOURNAUX.items():
        p = os.path.join(dossier, nom)
        if not os.path.isfile(p) or sha(p) != attendu:
            raise SystemExit(f"journal du second tour absent ou modifié : {nom} (empreinte {attendu[:12]}… exigée) : refus")
    lire = lambda n: [json.loads(l) for l in open(os.path.join(dossier, n), encoding="utf-8") if l.strip()]  # noqa: E731
    reg = lire("registre-depense-cumulee-v1.jsonl")
    debuts = [r for r in reg if r.get("type") == "debut"]
    arg, kim = lire("relais-argon-journal.jsonl"), lire("relais-kimi-journal.jsonl")
    etapes = {"argon": [d for d in debuts if d["fournisseur"] == "argon"], "kimi": [d for d in debuts if d["fournisseur"] == "kimi"]}
    if len(etapes["argon"]) != len(arg) or len(etapes["kimi"]) != len(kim):
        raise SystemExit("registre et journaux des relais ne s'apparient pas un pour un : refus")
    par = {}
    for four, journal in (("argon", arg), ("kimi", kim)):
        for d, j in zip(etapes[four], journal):
            cle = (four, d["etape"], d["role"])
            u = j.get("usage") or {}
            entree = u.get("entree", u.get("prompt_tokens"))
            sortie = u.get("sortie", u.get("completion_tokens"))
            taille = j.get("caracteres", j.get("octets_corps"))
            par.setdefault(cle, []).append((taille, entree, sortie))
    ratio_argon = statistics.median(t / e for (f, et, _), v in par.items() if f == "argon" and et != "controle" for t, e, _ in v)
    ratio_kimi = statistics.median(t / e for (f, et, _), v in par.items() if f == "kimi" and et != "controle" for t, e, _ in v)
    lect = [t for t, _, _ in par.get(("argon", "etiquettes", "juge_ideation"), [])]
    resume = {f"{f}/{et}/{ro}": {"appels": len(v), "sortie_mediane": statistics.median(s for _, _, s in v),
                                  "sortie_max": max(s for _, _, s in v), "entree_mediane": statistics.median(e for _, e, _ in v)}
              for (f, et, ro), v in sorted(par.items())}
    prop_kimi = par[("kimi", "proposition", "proposeur_ideation")][0][2]
    prop_argon = par[("argon", "proposition", "proposeur_ideation")][0][2]
    return {"ratio_caracteres_par_jeton_argon": round(ratio_argon, 3), "ratio_octets_par_jeton_kimi": round(ratio_kimi, 3),
            "entree_lecteur_argon_mediane_caracteres": statistics.median(lect) if lect else None,
            "par_role": resume, "proposeur_kimi_6_fiches": prop_kimi, "proposeur_argon_6_fiches": prop_argon,
            "sortie_attendue_kimi_proposeur_8_fiches": round(prop_kimi * 8 / 6),
            "sortie_attendue_argon_proposeur_8_fiches": round(prop_argon * 8 / 6),
            "source": "run-20261101-2146 (second tour réel), journaux des relais et registre cumulé, sans texte"}


def longueurs_pieces():
    def lg(nom):
        with open(os.path.join(PIECES, nom), encoding="utf-8") as f:
            return len(f.read())
    concepts = json.load(open(os.path.join(PIECES, "concepts-kirchner-v1.json"), encoding="utf-8"))
    src = json.load(open(os.path.join(PIECES, "source-gu-krenn-kirchner-v1.json"), encoding="utf-8"))
    vocab = sorted({c for o in src["oeuvres"] for c in o["concepts"]})
    return {"consigne_proposeur": lg("consigne-proposeur-kirchner-v1.md"), "consigne_aiguilleur": lg("consigne-aiguilleur-kirchner-v1.md"),
            "consigne_juge": lg("consigne-juge-kirchner-v1.md"), "consigne_lecteur": lg("consigne-lecteur-kirchner-v1.md"),
            "consigne_fusion": lg("consigne-metteur-kirchner-v1.md"),
            "liste_la_plus_longue": max(len(json.dumps(concepts, ensure_ascii=False)), len(json.dumps(vocab, ensure_ascii=False)))}


def caracteres_attendus(role_plaf, lg):
    f = FICHE_ATTENDUE
    return {"proposeur": lg["consigne_proposeur"] + 120, "aiguilleur": lg["consigne_aiguilleur"] + f,
            "juge": lg["consigne_juge"] + f, "lecteur": lg["consigne_lecteur"] + lg["liste_la_plus_longue"] // 2 + f + 60,
            "fusion": lg["consigne_fusion"] + 2 * f}[role_plaf]


def cout_attendu(modele, role_plaf, lg, m):
    pe, ps = ch.PRIX[modele]
    four = ch.FOURNISSEUR_DE[modele]
    c = caracteres_attendus(role_plaf, lg)
    entree = (2 * c * 0.55) / m["ratio_octets_par_jeton_kimi"] if four == "kimi" else c / m["ratio_caracteres_par_jeton_argon"]
    sortie = SORTIE_ATTENDUE[role_plaf]
    if role_plaf == "proposeur" and four == "kimi":
        sortie = m["sortie_attendue_kimi_proposeur_8_fiches"]
    if role_plaf == "proposeur" and four == "argon":
        sortie = m["sortie_attendue_argon_proposeur_8_fiches"]
    return entree * pe / 1e6 + sortie * ps / 1e6, round(entree), sortie


def devis_variante(variante, lg, m, k=K_PAIRES):
    lignes = []
    for etape, role, modele, n in ch.plan_appels(variante, k):
        rp = ch.role_plafond(role)
        att, e_att, s_att = cout_attendu(modele, rp, lg, m)
        pire = ch.pire_cas_appel(modele, ch.caracteres_pire(rp, lg), rp in ("proposeur", "fusion"))
        lignes.append({"etape": etape, "role": role, "modele": modele, "fournisseur": ch.FOURNISSEUR_DE[modele], "appels": n,
                       "jetons_entree_attendus": e_att, "jetons_sortie_attendus": s_att,
                       "jetons_sortie_pire_cas": ch.MAX_SORTIE[ch.FOURNISSEUR_DE[modele]][0 if rp in ("proposeur", "fusion") else 1],
                       "attendu_usd": round(att * n, 4), "pire_cas_usd": round(pire * n, 4)})
    modeles = sorted({ch.PROPOSEURS[p] for p in ch.VARIANTES[variante]} | {"claude-opus-5-5", "gpt-6-astra", "claude-fable-5-1"})
    controles = {mo: CONTROLE_USD for mo in modeles}
    par_etape, par_four, par_modele = {}, {}, {}
    for l in lignes:
        for d, k_ in ((par_etape, l["etape"]), (par_four, l["fournisseur"]), (par_modele, l["modele"])):
            x = d.setdefault(k_, {"appels": 0, "attendu_usd": 0.0, "pire_cas_usd": 0.0})
            x["appels"] += l["appels"]
            x["attendu_usd"] += l["attendu_usd"]
            x["pire_cas_usd"] += l["pire_cas_usd"]
    for mo, c in controles.items():
        f = ch.FOURNISSEUR_DE[mo]
        x = par_four.setdefault(f, {"appels": 0, "attendu_usd": 0.0, "pire_cas_usd": 0.0})
        x["appels"] += 1
        x["pire_cas_usd"] += c
        x["attendu_usd"] += 0.002
    arr = lambda d: {k_: {a: (round(b, 4) if isinstance(b, float) else b) for a, b in v.items()} for k_, v in d.items()}  # noqa: E731
    total_att = sum(l["attendu_usd"] for l in lignes) + 0.002 * len(controles)
    total_pire = sum(l["pire_cas_usd"] for l in lignes) + sum(controles.values())
    return {"variante": variante, "proposeurs": list(ch.VARIANTES[variante]), "k_paires": k, "lignes": lignes,
            "controles_usd": controles, "par_etape": arr(par_etape), "par_fournisseur": arr(par_four), "par_modele": arr(par_modele),
            "appels_course": sum(l["appels"] for l in lignes), "appels_controle": len(controles),
            "total_attendu_usd": round(total_att, 2), "total_pire_cas_usd": round(total_pire, 2)}


def calculer(dossier):
    m = mesures(dossier)
    lg = longueurs_pieces()
    variantes = {v: devis_variante(v, lg, m) for v in ch.VARIANTES}
    pire_max = max(d["total_pire_cas_usd"] for d in variantes.values())
    s17 = 60 if 1.2 * pire_max <= 60 else int(math.floor(1.2 * pire_max)) + 1
    relais = {}
    for v, d in variantes.items():
        r = {}
        for f, x in d["par_fournisseur"].items():
            r[f] = math.ceil(1.2 * x["pire_cas_usd"] * 10 - 1e-9) / 10
            if f in PLANCHER_RELAIS:
                r[f] = max(r[f], PLANCHER_RELAIS[f])
            if f in ch.PLAFOND_RELAIS_MAX:
                r[f] = min(r[f], ch.PLAFOND_RELAIS_MAX[f])
            if r[f] < x["pire_cas_usd"]:
                raise SystemExit(f"{v} : relais {f} : plafond {r[f]} sous sa part au pire cas {x['pire_cas_usd']} : refus")
        autres = sum(x for f, x in r.items() if f != "claude")
        r["claude"] = round(s17 - autres, 1)
        if r["claude"] < d["par_fournisseur"]["claude"]["pire_cas_usd"]:
            raise SystemExit(f"{v} : le reste de S17 ne couvre pas le pire cas du relais Claude : refus")
        relais[v] = {f: {"port": ch.PORTS[f], "plafond_usd": r[f],
                         "max_appels": d["par_fournisseur"][f]["appels"] + 5} for f in sorted(r)}
    ps = ch.pire_cas_par_role(lg, "cinq_especes")
    plafonds_session = {k_: math.ceil(v[0] * 1.05 * 10) / 10 for k_, v in ps.items()}
    return {"version": VERSION, "mesures_second_tour": m, "longueurs_pieces": lg, "hypotheses": {
        "fiche_attendue_caracteres": FICHE_ATTENDUE, "fiche_pire_cas_caracteres": ch.FICHE_MAX_CARACTERES,
        "sortie_attendue_par_role_supposee": SORTIE_ATTENDUE, "prix_usd_par_million": ch.PRIX, "source_prix": ch.SOURCE_PRIX,
        "sortie_maximale": ch.MAX_SORTIE, "passeport": "toutes les fiches (pire cas comme attendu)", "k_paires": K_PAIRES},
        "variantes": variantes, "plafond_technique_usd": s17, "arret_etape_usd": round(0.9 * s17, 2), "relais": relais,
        "plafonds_session": plafonds_session, "pire_cas_appel_par_role": {k_: [round(v[0], 4), v[1]] for k_, v in ps.items()}}


def texte(d):
    L = [f"# Devis de la course Kirchner Q2 — {VERSION} (aucun appel, aucune dépense)", ""]
    m = d["mesures_second_tour"]
    L += ["## Mesures du second tour réel (sans texte ; " + m["source"] + ")",
          f"- caractères par jeton d'entrée (Argon, médiane) : {m['ratio_caracteres_par_jeton_argon']} ; octets par jeton (Kimi, médiane) : "
          f"{m['ratio_octets_par_jeton_kimi']}",
          f"- proposeur Kimi, 6 fiches : {m['proposeur_kimi_6_fiches']} jetons de sortie ; proposeur Argon, 6 fiches : {m['proposeur_argon_6_fiches']}"]
    for k_, v in m["par_role"].items():
        L.append(f"- {k_} : {v['appels']} appels, sortie médiane {v['sortie_mediane']}, maximale {v['sortie_max']}, entrée médiane {v['entree_mediane']}")
    h = d["hypotheses"]
    L += ["", "## Hypothèses", f"- fiche servie : {h['fiche_attendue_caracteres']} caractères attendus (calcul), {h['fiche_pire_cas_caracteres']} au pire cas (SUPPOSÉ)",
          f"- sorties attendues (SUPPOSÉ, réflexion adaptative, effort high) : {h['sortie_attendue_par_role_supposee']} ; proposeur Kimi "
          f"{m['sortie_attendue_kimi_proposeur_8_fiches']}, Argon {m['sortie_attendue_argon_proposeur_8_fiches']} (calcul : mesure × 8 / 6)",
          f"- sorties maximales (pire cas) : {h['sortie_maximale']}", f"- prix : {h['prix_usd_par_million']}",
          f"- k_paires = {h['k_paires']} par bras, deux bras joués ; toutes les fiches admises ; un contrôle par modèle à 0,05 USD (pire cas)", ""]
    for v, x in d["variantes"].items():
        L += [f"## Variante {v} ({', '.join(x['proposeurs'])}) : {x['appels_course']} appels de course + {x['appels_controle']} contrôles",
              "| étape | rôle | modèle | appels | entrée att. | sortie att. | sortie pire | attendu USD | pire cas USD |", "|---|---|---|---|---|---|---|---|---|"]
        for l in x["lignes"]:
            L.append(f"| {l['etape']} | {l['role']} | {l['modele']} | {l['appels']} | {l['jetons_entree_attendus']} | {l['jetons_sortie_attendus']} | "
                     f"{l['jetons_sortie_pire_cas']} | {l['attendu_usd']:.4f} | {l['pire_cas_usd']:.4f} |")
        L.append("")
        for nom in ("par_etape", "par_fournisseur", "par_modele"):
            L.append(f"- {nom} : " + " ; ".join(f"{k_} {y['appels']} appels, attendu {y['attendu_usd']:.2f}, pire {y['pire_cas_usd']:.2f}"
                                                 for k_, y in x[nom].items()))
        L += [f"- **total attendu {x['total_attendu_usd']:.2f} USD ; pire cas {x['total_pire_cas_usd']:.2f} USD** (contrôles compris)",
              f"- relais : {d['relais'][v]}", ""]
    L += [f"## Plafond technique retenu : S17 = {d['plafond_technique_usd']} USD (arrêt d'étape {d['arret_etape_usd']})",
          f"- plafonds de session : {d['plafonds_session']} (pire cas d'un appel par rôle : {d['pire_cas_appel_par_role']})"]
    return "\n".join(L) + "\n"


def ecrire_neuf(chemin, contenu):
    if os.path.exists(chemin):
        raise SystemExit(f"{chemin} existe déjà (R12) : refus")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)


def configuration(d, variante):
    s17 = d["plafond_technique_usd"]
    x = d["variantes"][variante]
    etapes = []
    for nom in ("proposition", "aiguillage", "juges", "passe_tableau", "etiquettes", "fusions"):
        if nom == "passe_tableau":
            etapes.append({"nom": nom, "attendu_usd": 0, "plafond_relais_usd": 0, "role": "sacrifiable", "rang": 2})
            continue
        e = x["par_etape"][nom]
        ligne = {"nom": nom, "attendu_usd": round(e["attendu_usd"], 2), "plafond_relais_usd": math.ceil(e["pire_cas_usd"] * 100) / 100,
                 "role": "sacrifiable" if nom == "fusions" else "protegee"}
        if nom == "fusions":
            ligne["rang"] = 1
        etapes.append(ligne)
    def piece(nom):
        p = os.path.join("pieces", nom)
        return {"chemin": p, "sha256": sha(os.path.join(ICI, p))}
    c = lambda *a: ["/usr/bin/python3", "-I", "-B"] + list(a)  # noqa: E731
    commun = ["--registre", "{REGISTRE}", "--plafond-cumule-usd", f"{s17:g}"]
    fournisseurs = {
        "claude": c("{DEPOT}/donnees/course-kirchner-q2-v1/orchestrateur/kirchner/commande_claude_kirchner_v1.py",
                    "--url-relais", "http://127.0.0.1:8806", *commun, "--max-sortie-proposeur", "64000", "--max-sortie-court", "16000",
                    "--sortie-min-jetons", "2000", "--delai-s", "1750", "--effort", "high", "--reflexion", "adaptative"),
        "astra": c("{DEPOT}/docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_astra_a1bis_v1.py", "appeler", "--modele",
                   "gpt-6-astra", "--url-relais", "http://127.0.0.1:8807", *commun, "--max-sortie-proposeur", "32000",
                   "--max-sortie-court", "16000", "--sortie-min-jetons", "2000", "--delai-s", "1750"),
        "kimi": c("{DEPOT}/donnees/course-kirchner-q2-v1/orchestrateur/nuit/commande_kimi_v2.py", "--url-relais", "http://127.0.0.1:8804",
                  *commun, "--max-sortie-proposeur", "65536", "--max-sortie-court", "16000", "--sortie-min-jetons", "4096", "--delai-s", "1750"),
        "argon": c("{DEPOT}/donnees/course-kirchner-q2-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py", "appeler", "--url-relais",
                   "http://127.0.0.1:8805", *commun, "--max-sortie-proposeur", "32000", "--max-sortie-court", "4000",
                   "--sortie-min-jetons", "1000", "--delai-s", "1750")}
    utilises = sorted(d["relais"][variante])
    props = [{"etiquette": p, "modele": ch.PROPOSEURS[p], "fournisseur": ch.FOURNISSEUR_DE[ch.PROPOSEURS[p]],
              "consigne": "consigne_proposeur"} for p in ch.VARIANTES[variante]]
    return {
        "_lisez_moi": (f"Configuration de la course d'idéation Kirchner (question 2), variante {variante}, v1 — écrite par "
                       "calcul_devis_course_kirchner_v1.py le 3 novembre 2026 (sous-agent de session-depot). Course NON décisive "
                       "(démonstration, matière à réflexion pour Lazar). S17 = plafond TECHNIQUE (garde contre une boucle). Aucun "
                       "témoin planté. Bras joués : gu_krenn (substitut) et basique ; bras méta hors course. Jetons {DEPOT} et "
                       "{REGISTRE} remplacés par le lanceur. Spécification de conv-audit : specification-kirchner-q2-v1.md "
                       "(934f5dcb…) ; pièce « Kirchner » servie : v2 (6e7fb1c5…)."),
        "variante": variante, "racine_graines": 20261103, "graines": {"prefixe": "kq2"},
        "champs_fiche": ["titre", "probleme", "sous_estime", "hypothese", "axe", "premiere_experience", "changer_d_avis", "test_de_mort", "cout"],
        "champ_titre": "titre", "champ_axe": "axe",
        "budget": {"plafond_usd": float(s17), "arret_etape_usd": d["arret_etape_usd"], "portee_plafond": "course", "etapes": etapes},
        "proposeurs": props, "cases": [["kirchner-question-2", "niveau-methode"]],
        "aiguilleur": {"etiquette": "aiguilleur-opus", "modele": "claude-opus-5-5", "fournisseur": "claude", "consigne": "consigne_aiguilleur"},
        "juges": [{"etiquette": "juge-opus", "modele": "claude-opus-5-5", "fournisseur": "claude", "consigne": "consigne_juge"},
                  {"etiquette": "juge-astra", "modele": "gpt-6-astra", "fournisseur": "astra", "consigne": "consigne_juge"}],
        "items_juge": ["K1", "K2", "K3", "K4", "K5"], "agregation": {"regle": "unanimite"},
        "lecteurs_etiquettes": [{"etiquette": "lecteur-opus", "modele": "claude-opus-5-5", "fournisseur": "claude"},
                                {"etiquette": "lecteur-astra", "modele": "gpt-6-astra", "fournisseur": "astra"}],
        "garde_kimi": {"debordement_max": 0.5, "refus_aiguilleur": "technique", "arret_metteur_fusion": False},
        "tableau": {"longueur_max_titre": 80, "longueur_max_resume": 160, "champ_resume": "hypothese",
                    "consigne_passe": "sans objet (passe « tableau » retirée, aucun appel)", "juger_passe_tableau": False},
        "memoire": {"methode": "bardeaux", "taille_bardeau": 3, "seuil": 0.6},
        "bisociateur": {"bras": ["gu_krenn", "basique"], "k_paires": K_PAIRES, "fournisseurs_entree": ["*"],
                        "gu_krenn": {"mode": "substitut", "source": piece("source-gu-krenn-kirchner-v1.json"),
                                     "oeuvres_min_vocabulaire": 1, "date_debut": "2000-01-01", "date_coupure": "2026-11-03",
                                     "actif_depuis": "2000-01-01", "actif_min_oeuvres": 1},
                        "basique": {"exposant": 8.5, "decalage": 0.05, "liste_concepts": "liste_concepts"},
                        "consigne_fusion": "consigne_fusion", "consigne_lecteur_etiquettes": "consigne_lecteur",
                        "metteur_fusion": {"etiquette": "metteur-fable", "modele": "claude-fable-5-1", "fournisseur": "claude"}},
        "plafonds_session": d["plafonds_session"],
        "etiquettes_interdites": list(ch.ETIQUETTES_EXIGEES),
        "a4": {"mode": "prefixe", "action": "fiche_exclue"},
        "arrets": {"a3_echecs_consecutifs": 3, "a3_delai_s": {"*": 1800}, "a14_part_max": 0.25, "a11_modeles": []},
        "pieces": {"consigne_proposeur": piece("consigne-proposeur-kirchner-v1.md"),
                   "consigne_aiguilleur": piece("consigne-aiguilleur-kirchner-v1.md"),
                   "consigne_juge": piece("consigne-juge-kirchner-v1.md"),
                   "consigne_lecteur": piece("consigne-lecteur-kirchner-v1.md"),
                   "consigne_fusion": piece("consigne-metteur-kirchner-v1.md"),
                   "liste_concepts": piece("concepts-kirchner-v1.json"),
                   "source_gu_krenn": piece("source-gu-krenn-kirchner-v1.json"),
                   "question_servie": piece("conv-audit/question-ideation-kirchner-v1.md"),
                   "piece_kirchner": piece("conv-audit/piece-kirchner-v2.md"),
                   "piece_nos_resultats": piece("conv-audit/piece-nos-resultats-v1.md")},
        "canaris": {"consigne_proposeur": "KQ2-PROPOSEUR-59114cf4", "consigne_aiguilleur": "KQ2-AIGUILLEUR-ef3ab230",
                    "consigne_juge": "KQ2-JUGE-7f57b98e", "consigne_lecteur": "KQ2-LECTEUR-4b683a08",
                    "consigne_fusion": "KQ2-METTEUR-c16e2030"},
        "relais": d["relais"][variante],
        "fournisseurs": {f: {"type": "commande_externe", "delai_s": 1800, "porte_plafond": {"type": "environnement"},
                             "modeles_servis_permis": {}, "commande": fournisseurs[f]} for f in utilises},
        "simulation": {"cout_par_appel_usd": 0.01, "fiches_par_appel": ch.FICHES_PAR_PROPOSEUR}}


NOMS = {"sans_kimi": "configuration-course-kirchner-q2-v1-sans-kimi.json", "avec_kimi": "configuration-course-kirchner-q2-v1-avec-kimi.json",
        "cinq_especes": "configuration-course-kirchner-q2-v1-cinq-especes.json"}


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = a.add_subparsers(dest="mode", required=True)
    p = s.add_parser("devis")
    p.add_argument("--second-tour", required=True)
    p.add_argument("--sortie-texte", required=True)
    p.add_argument("--sortie-json", required=True)
    q = s.add_parser("configurations")
    q.add_argument("--second-tour", required=True)
    q.add_argument("--dossier", required=True)
    args = a.parse_args(argv)
    d = calculer(args.second_tour)
    if args.mode == "devis":
        ecrire_neuf(args.sortie_texte, texte(d))
        ecrire_neuf(args.sortie_json, json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        print(texte(d))
        return 0
    for v, nom in NOMS.items():
        ecrire_neuf(os.path.join(args.dossier, nom), json.dumps(configuration(d, v), ensure_ascii=False, indent=1) + "\n")
        print("écrit :", nom)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
