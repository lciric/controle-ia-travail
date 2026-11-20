"""Contre-lecteur, modèle S : vérifications indépendantes du générateur (copie du dossier G), sur les fragments factices
seulement, racine des essais. Aucune ouverture du fichier des cartes ; aucune écriture hors de la sortie standard."""
import itertools
import json
import sys
from collections import Counter
from fractions import Fraction

sys.path.insert(0, "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-generateur-etage-2/copie-G")
import numpy as np
import generer_temoins_ligne_3_v1 as G

ICI = "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-generateur-etage-2/copie-G/"
FR = ICI + "fragments-exemple-essais-v1.json"
h = G.sha256_fichier(FR)
conf = G.lire_configuration()
INTERDITES = conf["etiquettes_interdites_fixes"]
fr, _ = G.charger_fragments(FR, h, INTERDITES)
ctx = G.Contexte("essais")
banque, journal = G.composer(fr, ctx, G.ITEMS, INTERDITES)
G.verifier_proportions(banque, journal)
sortie = {}

# 1. proportions, recomptées à la main sur la banque et le journal
bons = [t for t in banque if t["classe"] == "bon"]
mauv = [t for t in banque if t["classe"] == "mauvais"]
sortie["n"] = [len(banque), len(bons), len(mauv)]
sortie["citants_bons_mauvais"] = [sum(t["citation"] for t in bons), sum(t["citation"] for t in mauv)]
sortie["par_item"] = {it: dict(Counter((t["niveau"], t["citation"]) for t in mauv if t["item"] == it)) for it in G.ITEMS}
sortie["par_item"] = {it: {str(k): v for k, v in d.items()} for it, d in sortie["par_item"].items()}
sortie["niveaux_par_item"] = {it: dict(Counter(t["niveau"] for t in mauv if t["item"] == it)) for it in G.ITEMS}
sortie["citants_par_item"] = {it: sum(t["citation"] for t in mauv if t["item"] == it) for it in G.ITEMS}
jb = [j for j in journal if j["classe"] == "bon"]
sortie["types_bons"] = {str(k): v for k, v in Counter((j["type_bon"], j["citation"]) for j in jb).items()}
sortie["pieges"] = {str(k): v for k, v in Counter((j["piege"], j["citation"]) for j in jb).items()}

# 2. longueurs : plage, entrelacement par classe (effectif par bande), longueur recalculée
sortie["longueur_min_max"] = [min(j["longueur"] for j in journal), max(j["longueur"] for j in journal)]
ok_long = all(len(json.dumps(t["contenu"], ensure_ascii=False, indent=1)) == j["longueur"]
              for t, j in zip(sorted(banque, key=lambda x: x["identifiant_interne"]), sorted(journal, key=lambda x: x["identifiant_interne"])))
sortie["longueur_du_journal_egale_recalcul"] = ok_long
for cl in ("bon", "mauvais"):
    sortie["bandes_" + cl] = dict(sorted(Counter(j["bande"] for j in journal if j["classe"] == cl).items()))
sortie["moyennes_longueur_par_classe"] = {cl: float(np.mean([j["longueur"] for j in journal if j["classe"] == cl])) for cl in ("bon", "mauvais")}
# longueur moyenne par niveau (confusion éventuelle niveau / bande)
sortie["longueur_moyenne_par_niveau"] = {n: float(np.mean([j["longueur"] for j in journal if j["niveau"] == n])) for n in G.NIVEAUX}

# 3. partage : par strate, comptes lecture / étalonnage, écart maximal
strates = {}
for t in banque:
    cle = (t["classe"], t["item"], t["niveau"], t["citation"])
    strates.setdefault(cle, Counter())[t["moitie"]] += 1
sortie["strates_ecart_max"] = max(abs(c["lecture"] - c["etalonnage"]) for c in strates.values())
sortie["moities"] = dict(Counter(t["moitie"] for t in banque))
sortie["moities_par_classe"] = {cl: dict(Counter(t["moitie"] for t in banque if t["classe"] == cl)) for cl in ("bon", "mauvais")}
sortie["moities_par_item"] = {it: dict(Counter(t["moitie"] for t in mauv if t["item"] == it)) for it in G.ITEMS}
sortie["moities_bons_citants"] = dict(Counter(t["moitie"] for t in bons if t["citation"]))
sortie["moities_par_niveau_item"] = {f"{it}/{n}": dict(Counter(t["moitie"] for t in mauv if t["item"] == it and t["niveau"] == n))
                                     for it in G.ITEMS for n in G.NIVEAUX}

# 4. entrelacement des identifiants : classe selon le rang de l'identifiant
rang_bons = [int(t["identifiant_interne"][-3:]) for t in bons]
sortie["identifiants_bons_moyenne"] = float(np.mean(rang_bons))

# 5. aire par rangs contre un décompte par paires, avec ex æquo
rng = np.random.default_rng(7)
for k in range(5):
    s = rng.integers(0, 6, size=60).astype(float)
    y = rng.integers(0, 2, size=60).astype(bool)
    pos, neg = s[y], s[~y]
    paires = sum(1 if a > b else 0.5 if a == b else 0 for a in pos for b in neg)
    assert G.aire_par_rangs(s, y) == Fraction(int(paires * 2), 2 * len(pos) * len(neg)), k
sortie["aire_par_rangs_contre_paires"] = "5 jeux avec ex aequo : egale"

# 6. régression : gradient de l'objectif pénalisé au point rendu, recodé à part
X = np.random.default_rng(11).normal(size=(90, 7))
yv = (X[:, 0] + 0.5 * X[:, 1] + np.random.default_rng(12).normal(size=90) > 0).astype(float)
w, b, it, conv = G.logistique(X, yv)
z = X @ w + b
p = 1 / (1 + np.exp(-z))
grad_w = X.T @ (p - yv) + 1.0 * w
grad_b = np.sum(p - yv)
sortie["logistique"] = {"iterations": it, "converge": conv, "norme_gradient": float(np.linalg.norm(np.append(grad_w, grad_b)))}

# 7. audit complet sur la banque factice, service rejoué à la main (même gabarit que le module de l'organisme lu)
consigne = G.lire_par_empreinte(G.DEPOT / G.CONSIGNE_JUGE[0], G.CONSIGNE_JUGE[1], "consigne").decode("utf-8")


def entree_une_fiche(consigne_figee, fiche, interdites, identifiant_servi=None):
    vue = json.loads(json.dumps(fiche["contenu"], ensure_ascii=False))
    if identifiant_servi is not None:
        vue = dict(vue, identifiant=identifiant_servi)
    corps = json.dumps(vue, ensure_ascii=False, indent=1)
    return consigne_figee.rstrip() + "\n\n## La fiche\n```json\n" + corps + "\n```\n"


def lire_verdict(texte, items):
    i = texte.rfind("```json")
    corps = texte[i + 7:].rsplit("```", 1)[0]
    bloc = json.loads(corps)
    if not isinstance(bloc.get("items"), dict) or set(bloc["items"]) != set(items):
        return None
    return {"items": bloc["items"]}


service = G.ServiceAudit(nature="essai", entree_une_fiche=entree_une_fiche, lire_verdict=lire_verdict, consigne=consigne,
                         items=conf["items_juge"], interdites=INTERDITES)
rapport = G.auditer(banque, G.Contexte("essais"), service)
sortie["audit"] = {"decision": rapport["decision"], "motifs": rapport["motifs_de_refus"],
                   "aire_qui_decide": rapport["aire_qui_decide"]["aire"], "aire_tous_traits": rapport["aire_a_tous_les_traits"]["aire"],
                   "convergence": [rapport["aire_qui_decide"]["convergence"], rapport["aire_a_tous_les_traits"]["convergence"]],
                   "max_iter_par_pli": [max(rapport["aire_qui_decide"]["iterations_par_pli"]), max(rapport["aire_a_tous_les_traits"]["iterations_par_pli"])],
                   "lettre": {k: [v["bons"], v["mauvais"], round(v["aire"], 4), v["dans_la_bande"]] for k, v in rapport["traits_de_la_lettre"].items()},
                   "juges": {g: [rapport["juges_scriptes_de_surface"][g]["erreur_equilibree"], rapport["juges_scriptes_de_surface"][g].get("dans_la_bande")]
                             for g in ("parfait", "longueur", "champ_lu", "citation")},
                   "plis": rapport["plis"]["effectifs"]}

# 8. aire qui décide recalculée en dehors du code : mêmes plis, même régression, scores bruts ; comparée à la sortie
y = np.array([t["classe"] == "mauvais" for t in banque], dtype=float)
Xp = np.array([G.traits_presentation(t["contenu"], t["citation"]) for t in banque])
plis = G.plis_stratifies(y, G.Contexte("essais").rng("plis-de-l-audit", audit=True))
sortie["plis_effectifs_exacts_10_10"] = all(int(((plis == f) & (y == v)).sum()) == 10 for f in range(10) for v in (0, 1))
sp, _, _ = G.scores_hors_pli(Xp, y, plis)
pos, neg = sp[y == 1], sp[y == 0]
paires = sum(1 if a > b else 0.5 if a == b else 0 for a in pos for b in neg)
sortie["aire_decide_par_paires"] = paires / (len(pos) * len(neg))
sortie["nombre_de_traits_presentation"] = Xp.shape[1]

# 9. citation : le drapeau de la banque contre la présence réelle de « non vérifié » dans le texte
ecarts = []
for t in banque:
    texte = " ".join(t["contenu"].values())
    present = G.compte_non_verifie(texte) > 0
    if present != t["citation"]:
        ecarts.append((t["classe"], t["item"], t["citation"], present))
sortie["citation_drapeau_contre_texte_ecarts"] = Counter(map(str, ecarts))
sortie["citation_drapeau_contre_texte_ecarts"] = dict(sortie["citation_drapeau_contre_texte_ecarts"])

print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True, default=str))
