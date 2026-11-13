"""Mesure principale du pilote d'une génération (brouillon 1 du préenregistrement, `pilote-v1/`) : probabilité qu'un vrai
proposeur propose une composante **conditionnelle** de la famille MR-2 avant que sa condition soit connue. Programme pur :
mêmes entrées → même sortie ; aucun tirage d'issue ; aucun appel. Lit les mondes privés ; n'écrit **aucun coefficient**.

Usages :
  python3 -I -B mesure_pilote_v1.py puissance SORTIE.json
  python3 -I -B mesure_pilote_v1.py mesurer MONDES.json CARTES.json SORTIE.json
  python3 -I -B mesure_pilote_v1.py essai SORTIE.json            (cas sain et artefacts sur un monde de développement)

Définitions (gelées ici) :
- une carte **porte** la composante i si son attribution par l'oracle (Δ_i = gain sous W − gain sous W₋ᵢ, oracle de 12 000
  instances, graine `cle("oracle-pilote", monde)`) atteint τ_i = max(0,005 ; 0,75 · I_i) (règle de capture de la v3) ; τ'_i =
  max(0,005 ; 0,25 · I_i) en sensibilité (rapportée, ne décide pas) ;
- **unité principale : l'appel** (une session d'un proposeur sur un monde et un bras, au plus 6 cartes) : l'appel « trouve » i si
  au moins une de ses cartes admises au gardien porte i. q̂ = appels qui trouvent / appels répondus ; p_éq = 1 − (1 − q)^(1/6)
  (probabilité par carte équivalente, celle du modèle synthétique) ; intervalle : Clopper-Pearson 95 % bilatéral sur q, transformé.
  Raison : les cartes d'un même appel ne sont pas indépendantes ; une seule carte suffit à capter ; la survie après une
  génération de 4 appels vaut (1 − q)^4, comme dans le modèle (1 − p)^24 ;
- en sensibilité, l'unité **carte** : p̂ = cartes qui portent / emplacements (6 par appel répondu ; carte absente, refusée au gardien
  ou non évaluable = ne porte pas) ; Clopper-Pearson 95 % ;
- **bras A** (archive {K1}) : toutes les conditionnelles (leur condition n'est jamais dans l'archive) → **p_c** ;
  **bras B** (archive {K1, V-K1+B}, B condition de la première conditionnelle) : conditionnelles de condition B → **p_v** ;
  la seconde d'une chaîne, en bras B, rapportée à part ;
- **règle** (préenregistrement, §8) : borne basse de p_c (unité appel) > **p_max = 0,051** (`seuil_pilote_v1.py`, recalculé
  ici, refus s'il diffère) → issue **P-1** « MR-2 ne sert pas telle quelle » (nœud de Lazar) ; aucune conditionnelle jugeable
  (aucun appel répondu en bras A) → **P-0** « non concluant » (nœud) ; sinon **P-2** : banc de 24 mondes avec P_CACHÉE := p_éq
  ponctuel du bras A, P_VUE := p_éq ponctuel du bras B s'il est joué (0,25 sinon, dit).
"""
import datetime
import hashlib
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
OUTILS = os.path.join(os.path.dirname(os.path.dirname(ICI)), "outils-v4")
for p in (OUTILS, ICI):
    if p not in sys.path:
        sys.path.insert(0, p)
import monde_riche_v4 as V4  # noqa: E402  (famille MR-2 ; installe la sorte `interaction_xor` dans le compilateur)
import seuil_pilote_v1 as S  # noqa: E402

M, P1 = V4.M, V4.P1
P_MAX = 0.051  # sortie `sorties/seuil-pilote-v1.json` ; vérifié à chaque lancement
ALPHA_IC = 0.05
EMPLACEMENTS = 6
SYNTHETIQUE = {"forte": 0.5, "moyenne": 0.25, "latente": 0.25, "faible": 0.1, "conditionnelle_cachee": 0.02, "conditionnelle_vue": 0.25}
CLES_CARTE = {"monde", "bras", "proposeur", "emplacement", "etat", "loi"}
CLES_APPEL = {"monde", "bras", "proposeur", "etat"}


class Refus(Exception):
    pass


# --- intervalles (bibliothèque standard) ---------------------------------------------------------------------------------

def _cdf(k, n, p):
    if p <= 0:
        return 1.0
    if p >= 1:
        return 0.0 if k < n else 1.0
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(0, k + 1))


def clopper_pearson(x, n, a=ALPHA_IC):
    if n == 0:
        return (0.0, 1.0)

    def biss(f):
        lo, hi = 0.0, 1.0
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if f(mid) else (lo, mid)
        return 0.5 * (lo + hi)
    bas = 0.0 if x == 0 else biss(lambda p: 1 - _cdf(x - 1, n, p) < a / 2)
    haut = 1.0 if x == n else biss(lambda p: _cdf(x, n, p) > a / 2)
    return (bas, haut)


def q_vers_p(q):
    return 1 - (1 - q) ** (1 / EMPLACEMENTS)


def verifier_p_max():
    grille = [round(0.0005 * i, 4) for i in range(0, 601)]
    p = next(x for x in grille if S.p_tenue(x) <= 0.05)
    if abs(p - P_MAX) > 1e-12:
        raise Refus(f"p_max recalculé {p} ≠ {P_MAX} (seuil_pilote_v1.py a changé)")
    return p


def puissance():
    q_max = 1 - (1 - P_MAX) ** EMPLACEMENTS
    out = {}
    for n in (8, 10, 12, 16):
        ligne = {}
        for p in (0.0, 0.01, 0.02, 0.03, 0.051, 0.075, 0.1, 0.15, 0.25):
            q = 1 - (1 - p) ** EMPLACEMENTS
            pr = sum(math.comb(n, x) * q ** x * (1 - q) ** (n - x) for x in range(n + 1) if clopper_pearson(x, n)[0] > q_max)
            ligne[f"{p}"] = round(pr, 4)
        out[f"appels={n}"] = ligne
    seuil_x = {f"appels={n}": next((x for x in range(n + 1) if clopper_pearson(x, n)[0] > q_max), None) for n in (8, 10, 12, 16)}
    return {"p_max": P_MAX, "q_max": round(q_max, 4), "probabilite_issue_P1_selon_p_vrai": out,
            "appels_qui_trouvent_minimum_pour_P1": seuil_x,
            "lecture": "probabilité que la règle rende P-1 (nœud) si la vraie probabilité par carte vaut p, appels indépendants"}


# --- mesure ------------------------------------------------------------------------------------------------------------

def _evaluable(loi, Z, G):
    try:
        P = M.probas(loi, Z, G)
    except (KeyError, ValueError, TypeError, IndexError):
        return False
    return bool(np.all(np.isfinite(P)) and P.shape == (len(Z), 3) and np.allclose(P.sum(axis=1), 1.0))


def mesurer(mondes, cartes, appels):
    verifier_p_max()
    par_monde = {}
    for w in mondes:
        if set(w) != {"monde", "spec", "spec_sha256"}:
            raise Refus("monde : clés {monde, spec, spec_sha256} exigées")
        sha = hashlib.sha256(M.json_canonique(w["spec"])).hexdigest()
        if sha != w["spec_sha256"]:
            raise Refus(f"monde {w['monde']} : empreinte du devis différente")
        spec = w["spec"]
        loi = M.compiler_monde(spec)
        o = M.Oracle(loi, spec["dimension"], spec["sous_populations"], n=12000, graine=P1.cle("oracle-pilote", w["monde"]))
        _, eid_k1, infos = M.k1_du_monde(spec, o)
        cond = {e["id"]: e["composante_condition"] for e in spec["effets"] if e["type"] == "interaction_xor"}
        if eid_k1 in cond.values():
            raise Refus(f"monde {w['monde']} : la condition d'une conditionnelle est l'effet de K1")
        premiere = next((c for c, b in cond.items() if b not in cond), None)
        par_monde[w["monde"]] = {"spec": spec, "o": o, "infos": infos, "eid_k1": eid_k1, "cond": cond,
                                 "classe": {e["id"]: e["classe"] for e in spec["effets"]},
                                 "condition_bras_b": cond.get(premiere)}
    for a in appels:
        if set(a) != CLES_APPEL or a["etat"] not in ("repondu", "echec") or a["bras"] not in ("A", "B") or a["monde"] not in par_monde:
            raise Refus("appel : clés, état (repondu|echec), bras (A|B) ou monde invalides")
    cles = [(a["monde"], a["bras"], a["proposeur"]) for a in appels]
    if len(set(cles)) != len(cles):
        raise Refus("appel en double (un appel par proposeur, monde et bras)")
    repondus = {k for k, a in zip(cles, appels) if a["etat"] == "repondu"}
    vus = set()
    for c in cartes:
        if set(c) != CLES_CARTE or c["etat"] not in ("admise", "refusee") or not (1 <= c["emplacement"] <= EMPLACEMENTS):
            raise Refus("carte : clés, état (admise|refusee) ou emplacement (1 à 6) invalides")
        k = (c["monde"], c["bras"], c["proposeur"])
        if k not in repondus:
            raise Refus(f"carte d'un appel non répondu ou inconnu : {k}")
        if (k, c["emplacement"]) in vus:
            raise Refus(f"emplacement en double : {k}, {c['emplacement']}")
        vus.add((k, c["emplacement"]))
    # attribution de chaque carte admise
    porte, porte_large, non_evaluables = {}, {}, 0
    for c in cartes:
        k = (c["monde"], c["bras"], c["proposeur"], c["emplacement"])
        pm = par_monde[c["monde"]]
        if c["etat"] != "admise" or not _evaluable(c["loi"], pm["o"].Z[:64], pm["o"].G[:64]):
            non_evaluables += c["etat"] == "admise"
            porte[k], porte_large[k] = set(), set()
            continue
        att = pm["o"].attribution(c["loi"], pm["spec"])
        porte[k] = {i for i, d in att.items() if d >= max(0.005, 0.75 * pm["infos"][i])}
        porte_large[k] = {i for i, d in att.items() if d >= max(0.005, 0.25 * pm["infos"][i])}

    def compter(bras, choix, table):
        """choix(monde) → composantes comptées dans ce monde et ce bras ; rend (appels, appels qui trouvent, emplacements, cartes)."""
        n_app = x_app = n_emp = x_cartes = 0
        for (w, b, prop) in sorted(repondus):
            if b != bras:
                continue
            for i in choix(w):
                n_app += 1
                n_emp += EMPLACEMENTS
                x = sum(1 for e in range(1, EMPLACEMENTS + 1) if i in table.get((w, b, prop, e), set()))
                x_cartes += x
                x_app += x > 0
        return n_app, x_app, n_emp, x_cartes

    def resume(n_app, x_app, n_emp, x_cartes):
        if n_app == 0:
            return {"appels": 0}
        q = x_app / n_app
        lo, hi = clopper_pearson(x_app, n_app)
        lo_c, hi_c = clopper_pearson(x_cartes, n_emp)
        return {"appels": n_app, "appels_qui_trouvent": x_app, "q": round(q, 4),
                "p_eq": round(q_vers_p(q), 4), "ic95_p_eq": [round(q_vers_p(lo), 4), round(q_vers_p(hi), 4)],
                "cartes": {"emplacements": n_emp, "qui_portent": x_cartes, "p": round(x_cartes / n_emp, 4),
                           "ic95": [round(lo_c, 4), round(hi_c, 4)]}}

    cond_a = lambda w: sorted(par_monde[w]["cond"])  # noqa: E731
    cond_b = lambda w: sorted(c for c, b in par_monde[w]["cond"].items() if b == par_monde[w]["condition_bras_b"])  # noqa: E731
    cond_b2 = lambda w: sorted(c for c, b in par_monde[w]["cond"].items() if b != par_monde[w]["condition_bras_b"])  # noqa: E731
    res = {"p_c_bras_A": resume(*compter("A", cond_a, porte)),
           "p_v_bras_B": resume(*compter("B", cond_b, porte)),
           "chaine_seconde_bras_B": resume(*compter("B", cond_b2, porte)),
           "sensibilite_tau_0_25": {"p_c_bras_A": resume(*compter("A", cond_a, porte_large)),
                                    "p_v_bras_B": resume(*compter("B", cond_b, porte_large))},
           "par_classe_bras_A": {}, "par_proposeur_bras_A": {}, "non_evaluables": non_evaluables,
           "appels": {"repondus": len(repondus), "echecs": len(appels) - len(repondus)},
           "cartes_admises": sum(1 for c in cartes if c["etat"] == "admise"),
           "cartes_refusees_au_gardien": sum(1 for c in cartes if c["etat"] == "refusee"),
           "modele_synthetique_pour_comparaison": SYNTHETIQUE, "p_max": P_MAX}
    for cl in ("forte", "moyenne", "faible", "latente"):
        ch = lambda w, cl=cl: sorted(i for i, x in par_monde[w]["classe"].items() if x == cl and i != par_monde[w]["eid_k1"])  # noqa: E731
        res["par_classe_bras_A"][cl] = resume(*compter("A", ch, porte))
    for prop in sorted({p for (_, _, p) in repondus}):
        n_app = x_app = 0
        for (w, b, pr) in sorted(repondus):
            if b == "A" and pr == prop:
                for i in cond_a(w):
                    n_app += 1
                    x_app += any(i in porte.get((w, b, pr, e), set()) for e in range(1, EMPLACEMENTS + 1))
        res["par_proposeur_bras_A"][prop] = {"appels": n_app, "appels_qui_trouvent": x_app}
    a = res["p_c_bras_A"]
    if a.get("appels", 0) == 0:
        issue = {"issue": "P-0", "texte": "non concluant : aucun appel répondu en bras A ; nœud de Lazar"}
    elif a["ic95_p_eq"][0] > P_MAX:
        issue = {"issue": "P-1", "texte": "MR-2 ne sert pas telle quelle : borne basse de p_c au-dessus de p_max ; nœud de Lazar"}
    else:
        b = res["p_v_bras_B"]
        issue = {"issue": "P-2", "texte": "banc de 24 mondes avec les probabilités mesurées",
                 "P_CACHEE_banc": a["p_eq"], "P_VUE_banc": b["p_eq"] if b.get("appels", 0) else 0.25,
                 "P_VUE_source": "bras B mesuré" if b.get("appels", 0) else "0,25 de la conception (bras B non joué)"}
    res["regle"] = issue
    return res


# --- essai (cas sain et artefacts, R5) ---------------------------------------------------------------------------------

def essai():
    spec = V4.generer_monde_v4(P1.cle("pilote-essai-developpement", 0))
    sha = hashlib.sha256(M.json_canonique(spec)).hexdigest()
    cond = {e["id"]: e["composante_condition"] for e in spec["effets"] if e["type"] == "interaction_xor"}
    ids = [e["id"] for e in spec["effets"] if e["classe"] != "latente"]
    rng = P1.rng_de("pilote-essai-cartes")
    cartes, appels, attendu = [], [], {}
    plans = {"prop1": True, "prop2": False, "prop3": False, "prop4": True}  # l'appel porte-t-il une conditionnelle (carte 1) ?
    for bras in ("A", "B"):
        for prop, avec in plans.items():
            appels.append({"monde": 0, "bras": bras, "proposeur": prop, "etat": "repondu"})
            for e in range(1, EMPLACEMENTS + 1):
                S_ = sorted({i for i in ids if i not in cond and rng.random() < 0.5} | (set(cond) if (avec and e == 1) else set()))
                cartes.append({"monde": 0, "bras": bras, "proposeur": prop, "emplacement": e, "etat": "admise",
                               "loi": P1._bruiter(spec, S_ or [ids[0]], 0.05, rng)})
    appels.append({"monde": 0, "bras": "A", "proposeur": "prop5", "etat": "echec"})
    cas_sain = mesurer([{"monde": 0, "spec": spec, "spec_sha256": sha}], cartes, appels)
    attendu = {"p_c_bras_A_appels_qui_trouvent": 2 * len(cond), "p_c_bras_A_appels": 4 * len(cond)}
    sain_ok = (cas_sain["p_c_bras_A"]["appels_qui_trouvent"] == attendu["p_c_bras_A_appels_qui_trouvent"]
               and cas_sain["p_c_bras_A"]["appels"] == attendu["p_c_bras_A_appels"])
    artefacts = {}
    for nom, (m_, c_, a_) in {
            "empreinte_du_monde_fausse": ([{"monde": 0, "spec": spec, "spec_sha256": "0" * 64}], cartes, appels),
            "carte_d_un_appel_en_echec": ([{"monde": 0, "spec": spec, "spec_sha256": sha}],
                                          cartes + [dict(cartes[0], proposeur="prop5")], appels),
            "emplacement_en_double": ([{"monde": 0, "spec": spec, "spec_sha256": sha}], cartes + [cartes[0]], appels),
            "appel_en_double": ([{"monde": 0, "spec": spec, "spec_sha256": sha}], cartes, appels + [appels[0]])}.items():
        try:
            mesurer(m_, c_, a_)
            artefacts[nom] = "NON REFUSÉ (défaut)"
        except Refus as x:
            artefacts[nom] = f"refusé : {x}"
    # carte non évaluable (loi à mémoire) : comptée « ne porte pas », comptée à part
    c2 = [dict(c) for c in cartes]
    c2[0] = dict(c2[0], loi={"type": "moyenne_glissante", "nombre_issues": 3, "fenetre": 5})
    r2 = mesurer([{"monde": 0, "spec": spec, "spec_sha256": sha}], c2, appels)
    artefacts["carte_non_evaluable"] = {"non_evaluables": r2["non_evaluables"], "attendu": 1}
    # pente du trait de la conditionnelle **sans** condition (la carte « voit » z_t marginalement) : ne doit pas porter
    o = M.Oracle(M.compiler_monde(spec), spec["dimension"], spec["sous_populations"], n=12000, graine=P1.cle("oracle-pilote", 0))
    infos = {e["id"]: o.information_effet(spec, e["id"]) for e in spec["effets"]}
    sans_cond = {}
    for c in sorted(cond):
        s2 = json.loads(json.dumps(spec))
        for e in s2["effets"]:
            if e["id"] == c:
                for k in ("trait_condition", "composante_condition"):
                    e.pop(k)
                e["type"] = "principal"
        att = o.attribution(M.compiler_monde(s2), spec)
        sans_cond[c] = {"delta_sur_information": round(att[c] / infos[c], 4), "porte": att[c] >= max(0.005, 0.75 * infos[c])}
    artefacts["pente_sans_condition"] = sans_cond
    return {"monde_de_developpement": {"conditionnelles": cond, "spec_sha256": sha}, "cas_sain": cas_sain, "attendu": attendu,
            "cas_sain_conforme": sain_ok, "artefacts": artefacts,
            "artefacts_conformes": all(isinstance(v, str) and v.startswith("refusé") for k, v in artefacts.items() if k not in ("carte_non_evaluable", "pente_sans_condition"))
            and r2["non_evaluables"] == 1 and not any(v["porte"] for v in sans_cond.values())}


def main(argv):
    if len(argv) < 3 or os.path.exists(argv[-1]):
        print(__doc__)
        return 2
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    try:
        if argv[1] == "puissance":
            res = puissance()
        elif argv[1] == "essai":
            res = essai()
        elif argv[1] == "mesurer" and len(argv) == 5:
            mondes = json.load(open(argv[2], encoding="utf-8"))
            donnees = json.load(open(argv[3], encoding="utf-8"))
            res = mesurer(mondes, donnees["cartes"], donnees["appels"])
        else:
            print(__doc__)
            return 2
    except Refus as x:
        print(f"refus : {x}", file=sys.stderr)
        return 2
    with open(argv[-1], "x", encoding="utf-8") as f:
        json.dump({"version": "mesure-pilote-v1", "commande": argv[1], "debut_utc": debut,
                   "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "resultat": res}, f, ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print(json.dumps(res, ensure_ascii=False, default=str)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
