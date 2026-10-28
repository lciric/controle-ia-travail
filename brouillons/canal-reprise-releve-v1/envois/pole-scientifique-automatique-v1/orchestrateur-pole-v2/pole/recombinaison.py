"""Recombinaison bisociative des survivantes — forme corrigée (relecture méta-conception v6.3, brique 2).

Diversité de domaine dans le noyau, S_ij = ⟨d_i, d_j⟩² (produit de Schur d'une matrice de Gram par elle-même : semi-défini
positif), qualité dans la diagonale, q_i = aptitude, L = diag(q) S diag(q) + γI (défini positif pour γ > 0, vérifié par
une décomposition de Cholesky en pur Python), tirage glouton du déterminant maximal de taille k ; puis, pour chaque paire
tirée qui partage un opérateur (le pont) et passe le filtre de compatibilité des contraintes, une consigne de fusion.
La fille doit porter ses deux parents et prédire plus qu'eux (`ce_que_la_fille_predit_de_plus` non vide, prédiction
différente de celles des parents). Les témoins n'entrent jamais dans la recombinaison.
"""

import itertools
import json
import math
import os
import re

from .caviardage import caviarder
from .fiche import Fiche, FicheInvalide
from .memoire import signature_prediction
from .outils import ecrire_scelle, extraire_bloc_json, json_canonique, normaliser_texte

MARQUEURS = {
    "lineaire": r"(?<!non )\blineaires?\b",
    "non lineaire": r"\bnon lineaires?\b",
    "stationnaire": r"(?<!non )\bstationnaires?\b",
    "transitoire": r"\btransitoires?\b|\bnon stationnaires?\b",
    "discret": r"\bdiscrete?s?\b",
    "continu": r"\bcontinue?s?\b",
    "convexe": r"(?<!non )\bconvexes?\b",
    "non convexe": r"\bnon convexes?\b",
    "independant": r"\bindependante?s?\b|\bnon dependante?s?\b",
    "dependant": r"(?<!non )\bdependante?s?\b",
}
PAIRES_CONTRADICTOIRES = (("lineaire", "non lineaire"), ("stationnaire", "transitoire"), ("discret", "continu"),
                          ("convexe", "non convexe"), ("independant", "dependant"))


class NonDefiniePositive(ValueError):
    pass


# --- filtre de compatibilité ------------------------------------------------------------------------------------
def marqueurs(contraintes):
    texte = " | ".join(normaliser_texte(c) for c in contraintes)
    return {nom for nom, motif in MARQUEURS.items() if re.search(motif, texte)}


def conflits(contraintes_a, contraintes_b):
    ma, mb = marqueurs(contraintes_a), marqueurs(contraintes_b)
    return [(p, q) for p, q in PAIRES_CONTRADICTOIRES if (p in ma and q in mb) or (q in ma and p in mb)]


def compatibles(a, b):
    return not conflits(a.contraintes, b.contraintes)


# --- noyau corrigé, Cholesky, tirage glouton --------------------------------------------------------------------
def vecteurs_domaine(listes):
    vocabulaire = sorted({normaliser_texte(x) for liste in listes for x in liste})
    position = {v: i for i, v in enumerate(vocabulaire)}
    vecteurs = []
    for liste in listes:
        v = [0.0] * len(vocabulaire)
        etiquettes = {normaliser_texte(x) for x in liste}
        for e in etiquettes:
            v[position[e]] = 1.0 / math.sqrt(len(etiquettes))
        vecteurs.append(v)
    return vecteurs


def produit(u, v):
    return sum(a * b for a, b in zip(u, v))


def noyau_diversite(vecteurs):
    return [[produit(u, v) ** 2 for v in vecteurs] for u in vecteurs]


def noyau_corrige(s, q, gamma=1e-3):
    n = len(s)
    return [[q[i] * s[i][j] * q[j] + (gamma if i == j else 0.0) for j in range(n)] for i in range(n)]


def noyau_fautif(vecteurs_operateurs, vecteurs_domaines):
    """Forme du rapport relu (« DPP bilinéaire ») : ⟨o_i,o_j⟩² ∘ (1 − ⟨d_i,d_j⟩²) — non garantie semi-définie positive."""
    return [[produit(oi, oj) ** 2 * (1 - produit(di, dj) ** 2) for oj, dj in zip(vecteurs_operateurs, vecteurs_domaines)]
            for oi, di in zip(vecteurs_operateurs, vecteurs_domaines)]


def cholesky(a, tolerance=0.0):
    """Facteur triangulaire inférieur ; lève NonDefiniePositive si un pivot n'est pas strictement positif."""
    n = len(a)
    for i in range(n):
        for j in range(i):
            if abs(a[i][j] - a[j][i]) > 1e-12 * max(1.0, abs(a[i][j])):
                raise NonDefiniePositive("matrice non symétrique")
    bas = [[0.0] * n for _ in range(n)]
    for j in range(n):
        pivot = a[j][j] - sum(bas[j][k] ** 2 for k in range(j))
        if not pivot > tolerance:
            raise NonDefiniePositive(f"pivot {j} = {pivot:.3e}")
        bas[j][j] = math.sqrt(pivot)
        for i in range(j + 1, n):
            bas[i][j] = (a[i][j] - sum(bas[i][k] * bas[j][k] for k in range(j))) / bas[j][j]
    return bas


def est_definie_positive(a):
    try:
        cholesky(a)
    except NonDefiniePositive:
        return False
    return True


def log_determinant(a):
    return 2.0 * sum(math.log(bas[i]) for i, bas in enumerate(cholesky(a)))


def tirage_glouton(noyau, k):
    """Sélection gloutonne du déterminant maximal de taille k (égalités départagées par l'indice)."""
    choisis = []
    for _ in range(min(k, len(noyau))):
        meilleur, valeur = None, -math.inf
        for i in range(len(noyau)):
            if i in choisis:
                continue
            indices = choisis + [i]
            try:
                v = log_determinant([[noyau[a][b] for b in indices] for a in indices])
            except NonDefiniePositive:
                continue
            if v > valeur + 1e-12:
                meilleur, valeur = i, v
        if meilleur is None:
            break
        choisis.append(meilleur)
    return choisis


# --- paires, consigne de fusion, validation de la fille ---------------------------------------------------------
def ponts(a, b):
    return sorted({normaliser_texte(x) for x in a.operateurs} & {normaliser_texte(x) for x in b.operateurs})


def consigne_fusion(a, b, ponts_communs, texte_memoire="", selection="seuil", alpha=0.05):
    morceaux = [
        "Tu es l'agent de recombinaison du pôle. Fusionne les deux fiches survivantes ci-dessous (fichier `parents.json`) "
        f"par le pont commun « {', '.join(ponts_communs)} », en reliant leurs domaines ({', '.join(a.domaines)} ; "
        f"{', '.join(b.domaines)}).",
        "Fiche A :\n" + json.dumps(a.vue_publique(), ensure_ascii=False, sort_keys=True, indent=1),
        "Fiche B :\n" + json.dumps(b.vue_publique(), ensure_ascii=False, sort_keys=True, indent=1),
        "Exigences : la fille prédit plus que ses parents — champ `ce_que_la_fille_predit_de_plus` non vide, prédiction "
        "signée et chiffrée différente de celles de A et de B, seuil qui peut échouer, sévérité attendue dans ]0 ; 1[ ; "
        "ses contraintes ne contredisent pas celles des parents. Réponds par un bloc ```json {\"fille\": {...}}``` avec "
        "les champs de la fiche (sans identifiant ni parents : l'orchestrateur les pose).",
    ]
    if selection == "pari":
        morceaux.append(f"Sélection par pari : la fille engage une loi prédictive (`loi_predictive`) ; sa sévérité est "
                        f"l'α du pôle ({alpha}) ; elle ne sera promue que si elle bat ses parents et leurs enveloppes "
                        "(mélange, enveloppe harmonique, concaténations si/sinon) avec une marge par tirage.")
    if texte_memoire:
        morceaux.append("Mémoire du pôle :\n" + texte_memoire)
    return "\n\n".join(morceaux)


def valider_fille(donnees, a, b, identifiant, source):
    """Rend (Fiche, None) si la fille est recevable, sinon (None, motif)."""
    if not isinstance(donnees, dict):
        return None, "bloc « fille » absent"
    champs = {k: v for k, v in donnees.items() if k not in ("identifiant", "parents", "statut", "temoin", "source")}
    champs.update(identifiant=identifiant, parents=[a.identifiant, b.identifiant], source=source, statut="proposee")
    try:
        fille = Fiche.depuis_dict(champs).valider()
    except (FicheInvalide, TypeError) as e:
        return None, str(e)
    if not fille.ce_que_la_fille_predit_de_plus.strip():
        return None, "la fille ne dit pas ce qu'elle prédit de plus"
    if signature_prediction(fille.vers_dict()) in (signature_prediction(a.vers_dict()), signature_prediction(b.vers_dict())):
        return None, "la prédiction de la fille est celle d'un parent"
    if conflits(fille.contraintes, a.contraintes) or conflits(fille.contraintes, b.contraintes):
        return None, "contraintes de la fille contradictoires avec un parent"
    return fille, None


def recombiner(pool, adaptateur, config, dossier, budget, generation, k=4, max_paires=3, gamma=1e-3, memoire=None,
               deja_fusionnees=None):
    """Tire, filtre, fait fusionner ; rend {"filles": [...], "refusees": [...], "rapport": {...}}."""
    deja = deja_fusionnees if deja_fusionnees is not None else set()
    candidates = sorted((f for f in pool if f.temoin is None and f.statut == "survit"), key=lambda f: f.identifiant)
    rapport = {"candidates": [f.identifiant for f in candidates], "paires": [], "ecartees": []}
    if len(candidates) < 2:
        return {"filles": [], "refusees": [], "rapport": dict(rapport, motif="moins de deux survivantes")}
    q = [f.aptitude() for f in candidates]
    s = noyau_diversite(vecteurs_domaine([f.domaines for f in candidates]))
    noyau = noyau_corrige(s, q, gamma)
    cholesky(noyau)
    choisis = tirage_glouton(noyau, k)
    rapport["tirage"] = [candidates[i].identifiant for i in choisis]
    paires = []
    for i, j in itertools.combinations(sorted(choisis), 2):
        a, b = candidates[i], candidates[j]
        cle = tuple(sorted((a.identifiant, b.identifiant)))
        pont, contradiction = ponts(a, b), conflits(a.contraintes, b.contraintes)
        if cle in deja or not pont or contradiction:
            rapport["ecartees"].append({"paire": cle, "deja_fusionnee": cle in deja, "pont": pont,
                                        "conflits": contradiction})
            continue
        paires.append((s[i][j], -q[i] * q[j], cle, a, b, pont))
    paires.sort(key=lambda p: p[:3])
    filles, refusees, texte_memoire = [], [], (memoire.texte_consigne("recombinaison") if memoire else "")
    for numero, (sij, _, cle, a, b, pont) in enumerate(paires[:max_paires], 1):
        if not budget.reserver(config.plafond_recombinaison_usd):
            rapport["arret_budget"] = True
            break
        sous = os.path.join(dossier, f"paire-{numero:02d}")
        os.makedirs(sous, exist_ok=False)
        ecrire_scelle(os.path.join(sous, "parents.json"), json_canonique(
            {"a": a.vue_publique(), "b": b.vue_publique(), "ponts": pont, "generation": generation,
             "selection": config.selection, "alpha": config.alpha}))
        consigne = consigne_fusion(a, b, pont, texte_memoire, config.selection, config.alpha)
        ecrire_scelle(os.path.join(sous, "consigne.txt"), consigne)
        res = adaptateur.lancer("recombinaison", consigne, sous, config.plafond_recombinaison_usd,
                                config.max_tours_recombinaison, modele=config.modele_recombinaison)
        budget.regler(config.plafond_recombinaison_usd, res.cout_declare_usd)
        ecrire_scelle(os.path.join(sous, "reponse.txt"), caviarder(res.texte_final)[0])
        deja.add(cle)
        bloc = extraire_bloc_json(res.texte_final, "fille") or {}
        fille, motif = valider_fille(bloc.get("fille"), a, b, f"fille-g{generation:02d}-{numero:02d}",
                                     f"recombinaison:{config.modele_recombinaison}")
        entree = {"paire": cle, "pont": pont, "similarite_domaine": round(sij, 6), "consigne": os.path.relpath(
            os.path.join(sous, "consigne.txt"), dossier), "cout": res.cout_declare_usd}
        if fille is None:
            refusees.append(dict(entree, motif=motif, proposition=bloc.get("fille")))
        else:
            filles.append(fille)
            entree["fille"] = fille.identifiant
        rapport["paires"].append(entree)
    return {"filles": filles, "refusees": refusees, "rapport": rapport}
