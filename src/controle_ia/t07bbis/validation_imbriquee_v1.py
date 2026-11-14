"""Validation croisée imbriquée de l'étape B bis, sur l'instance (`prereg/T0.7-etape-B-bis-v1.md`, plan, points 4 à 9), v1.

- **Plis externes** : les deux plis par tâche de T0.6 (`t06.test_croise.partition_plis`, graine `partition-taches` du manifeste
  de 7b) ; la sonde « du pli k » (`e<k>`) est apprise sur les tâches de l'autre pli et lue sur le pli k.
- **Plis internes** (`plis_internes`) : quatre plis de huit tâches dans les 32 tâches d'apprentissage (graine `bbis/interne/e<k>`),
  les mêmes pour la sonde, LEX et ENC (écrits, sans aire, dans le fichier fermé des sondes).
- **Grille** : 18 réglages (famille × couche × régularisation, `commun_v1.grille`, ordre d'exécution qui entrelace les familles) ;
  critère : aire moyenne des quatre plis internes (`aire_apprentissage`, **seule aire calculée sur l'instance**, refusée si une
  tâche du pli lu y entre) ; ex aequo (écart ≤ 0,005) : linéaire avant attention, couche 15 puis 7 puis 23, régularisation la
  plus forte d'abord (`choisir_reglage`) ; les aires de validation interne ne sont **jamais écrites** (seul le réglage retenu
  l'est) ; **sonde finale** réapprise sur les 32 tâches.
- **Plancher** : 800 directions par sonde finale et par pli (`sondes.evaluation.plancher_apparie` sans modification : covariance
  de ses jetons d'apprentissage, couche retenue, même agrégation ; graine `bbis/plancher/<cellule>/e<k>`), noms
  `<sonde>-bbis-plancher-<j>`, notées par lots avec contrôle en ligne contre la boucle (`t07.plancher_v3.scores_plancher_vectorises`).
- **Nul de réétiquetage** : 100 réétiquetages par cellule plafond (`bbis/reetiquetage/<cellule>/<r>` : pour chaque tâche
  d'évaluation, dans l'ordre trié, échange des étiquettes des deux épisodes du jeu avec probabilité un demi ; même réétiquetage
  pour l'apprentissage et le test, et pour les deux plis) ; sondes du nul apprises au réglage retenu de la sonde du pli (capacité
  égale), notées sur le pli lu, sur les cibles des transferts et sur leurs tâches d'apprentissage (notation par lots, même
  contrôle en ligne).
- **ENC** : même recette (grille, plis internes, sonde finale) sur les séries du modèle nu (J_d ou J_instruit contre O[H]).
- **Garde de débit** (`GardeDebit`) : après les 20 premiers apprentissages de la marche (dix de chaque famille), médiane de leur
  durée écrite au journal (une durée, jamais une aire) ; (heures écoulées) + (apprentissages restants × médiane × 1,2) + 0,6 h
  > 11 h → `ArretDebit` (arrêt de l'apprentissage, nœud de Lazar sur (r1) ou (r2) ; la décision est hors du module).
- **Contrôle carte-processeur** (`ControleCarte`) : un (cellule, pli) tiré par la graine `bbis/egalite-carte` parmi les dix,
  **avant** tout apprentissage ; dès que ce couple est appris, sa sonde finale est réapprise sur le processeur par
  `sondes.familles` et comparée sur 256 actions tirées de son pli lu (même générateur) ; écart relatif > 10⁻⁴ : arrêt.
- **Notation** (`noter_source`) : scores d'action seulement (sonde, 800 directions, 100 sondes du nul, ENC, lecture sans le champ
  du coût), aucun résumé de score, aucune aire, aucun état.

Interprétations déclarées : une sonde de validation interne en échec (perte non finie) rend son réglage inéligible (compté,
jamais une aire) ; aucun réglage éligible, ou sonde finale en échec : la source est « échec » (lue « non calculable ») ; une
sonde d'ENC ou du nul en échec est écrite par des scores `NaN` (lus « non calculable ») ; la variante (r1) du nœud de débit se
joue par `familles=("lineaire",)` et `n_reetiquetages=50`, sous un texte qui la nomme.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal
from ..sondes.evaluation import aire_sous_courbe, plancher_apparie
from ..t07.plancher_v3 import scores_plancher_vectorises
from . import apprentissage_carte_v1 as ac
from .commun_v1 import (EPOQUES, EX_AEQUO, FAMILLES, H, INSTRUIT, N_ACTIONS_CONTROLE_CARTE, N_DIRECTIONS, N_PLIS_INTERNES,
                        N_REETIQUETAGES, N_TACHES_APPRENTISSAGE, T100, TEMOIN_INSTRUIT, centiemes, grille, nom_dose,
                        nom_jumeau, rang_ex_aequo)
from .plis_v1 import frontiere_jetons, position_champ_cout

LIMITE_H, MARGE_H, FACTEUR_DEBIT, N_PREMIERS = 11.0, 0.6, 1.2, 20


class ArretDebit(GardeArret):
    """Garde de débit : marche projetée au-delà de 11 h ; arrêt de l'apprentissage, nœud de Lazar ((r1) ou (r2))."""


# ------------------------------------------------------------------------------------------------------- plis, aire gardée

def plis_internes(taches_apprentissage, rng, n_plis: int = N_PLIS_INTERNES, reelle: bool = True) -> list[list[str]]:
    """Plis internes de même taille dans les tâches d'apprentissage (permutation par le générateur de la clé)."""
    t = sorted(set(str(x) for x in taches_apprentissage))
    if len(t) < n_plis or len(t) % n_plis:
        raise GardeArret(f"{len(t)} tâches d'apprentissage : multiple de {n_plis} attendu")
    if reelle and (len(t), n_plis) != (N_TACHES_APPRENTISSAGE, N_PLIS_INTERNES):
        raise GardeArret(f"marche réelle : 32 tâches d'apprentissage en quatre plis de huit attendues ({len(t)} lues)")
    ordre = [t[int(i)] for i in rng.permutation(len(t))]
    n = len(t) // n_plis
    return [sorted(ordre[j * n:(j + 1) * n]) for j in range(n_plis)]


def aire_apprentissage(scores, y, taches, taches_lues) -> float:
    """Seule aire calculée sur l'instance : sur des tâches d'apprentissage seulement ; un appel qui touche une tâche du pli lu est
    refusé (arrêt)."""
    touchees = set(map(str, taches)) & set(map(str, taches_lues))
    if touchees:
        raise GardeArret(f"aire sur l'instance demandée sur {len(touchees)} tâche(s) du pli lu : refus (liste d'arrêt)")
    return aire_sous_courbe(np.asarray(scores, dtype=np.float64), np.asarray(y))


def exiger_disjonction(taches_utilisees, taches_lues, quoi: str) -> None:
    """Aucune tâche du pli lu dans un apprentissage, un réglage, un vocabulaire ou une covariance de plancher : arrêt."""
    if set(map(str, taches_utilisees)) & set(map(str, taches_lues)):
        raise GardeArret(f"{quoi} : une tâche du pli lu y entre : arrêt (liste d'arrêt)")


def choisir_reglage(aires: dict, reglages: list, couches) -> dict:
    """Meilleure aire moyenne ; ex aequo (écart ≤ 0,005) départagés par `commun_v1.rang_ex_aequo`. `aires` : nom → aire, ou None
    si le réglage est inéligible."""
    eligibles = [r for r in reglages if aires.get(r["nom"]) is not None]
    if not eligibles:
        raise GardeArret("aucun réglage éligible (toutes les sondes de validation en échec)")
    meilleure = max(aires[r["nom"]] for r in eligibles)
    ex = [r for r in eligibles if aires[r["nom"]] >= meilleure - EX_AEQUO]
    return min(ex, key=lambda r: rang_ex_aequo(r, couches))


# ---------------------------------------------------------------------------------------------------------- garde de débit

@dataclass
class GardeDebit:
    total_prevu: int
    debut_marche: float
    horloge: object = time.time
    limite_h: float = LIMITE_H
    journal: list = field(default_factory=list)
    durees: list = field(default_factory=list)
    verifiee: bool = False

    def noter(self, duree_s: float, famille: str) -> None:
        self.durees.append((float(duree_s), str(famille)))
        if len(self.durees) == N_PREMIERS and not self.verifiee:
            self.verifier()

    def verifier(self) -> dict:
        self.verifiee = True
        premiers = self.durees[:N_PREMIERS]
        nb = {f: sum(1 for _, x in premiers if x == f) for f in sorted(set(x for _, x in premiers))}
        if len(premiers) < N_PREMIERS or (len(nb) > 1 and set(nb.values()) != {N_PREMIERS // len(nb)}):
            raise GardeArret(f"garde de débit : {len(premiers)} premiers apprentissages, familles {nb} (entrelacées attendues)")
        med = float(np.median([d for d, _ in premiers]))         # médiane de durées d'apprentissage (jamais de jetons)
        ecoulees = (float(self.horloge()) - float(self.debut_marche)) / 3600.0
        projete = ecoulees + (int(self.total_prevu) - N_PREMIERS) * med * FACTEUR_DEBIT / 3600.0 + MARGE_H
        self.journal.append({"garde_debit": {"mediane_s": med, "heures_ecoulees": ecoulees, "projete_h": projete,
                                             "limite_h": self.limite_h, "familles": nb}})
        if projete > self.limite_h:
            raise ArretDebit(f"garde de débit : marche projetée {projete:.2f} h > {self.limite_h:g} h (médiane {med:.2f} s) : "
                             "arrêt de l'apprentissage, instance gardée au plus 12 h, nœud de Lazar ((r1) ou (r2))")
        return self.journal[-1]


def apprentissages_prevus(n_sources: int, n_reglages: int, n_plis_internes: int, n_reetiquetages: int) -> int:
    """Par source et par pli externe : grille × plis internes + 1 (sonde), autant pour ENC, plus les sondes du nul."""
    return int(n_sources) * 2 * (2 * (n_reglages * n_plis_internes + 1) + int(n_reetiquetages))


# ------------------------------------------------------------------------------------------------------------- les données

def plan_de_notation(positifs: str, doses) -> dict:
    """Groupes (série, condition) notés par une source plafond (plan, points 6 à 9 ; « Métrique ») : `sonde` (sonde et 800
    directions), `nul` (sondes du nul), `enc` (lecteur honnête), `sc` (lecture sans le champ du coût) ; `enc_positifs`."""
    dec = [("O", positifs), ("O", H)]
    if positifs == INSTRUIT:
        sonde = dec + [("Jinstruit", INSTRUIT), ("O", TEMOIN_INSTRUIT)]
        nul, enc = list(dec), [("Jinstruit", INSTRUIT), ("O", H)]
        for d in doses:
            c, j = nom_dose(d), nom_jumeau(nom_dose(d))
            sonde += [("O", c), (j, c), (f"A{centiemes(d)}", H)]
            nul.append(("O", c))
            enc.append((j, c))
        return {"sonde": sonde, "nul": nul, "enc": enc, "sc": [], "enc_positifs": ("Jinstruit", INSTRUIT)}
    d = next((x for x in doses if nom_dose(x) == positifs), None)
    if d is None:
        raise GardeArret(f"source {positifs!r} hors des doses {doses}")
    j = nom_jumeau(positifs)
    sonde = dec + [(j, positifs), (f"A{centiemes(d)}", H), ("O", T100), ("AT", H)]
    nul, enc = list(dec), [(j, positifs), ("O", H)]
    if float(d) == 1.0:
        sonde += [("O", INSTRUIT), ("Jinstruit", INSTRUIT)]
        nul.append(("O", INSTRUIT))
        enc.append(("Jinstruit", INSTRUIT))
    return {"sonde": sonde, "nul": nul, "enc": enc, "sc": [("O", positifs), ("O", H), (j, positifs)], "enc_positifs": (j, positifs)}


def nom_groupe(groupe: tuple) -> str:
    return f"{groupe[0]}-{groupe[1]}"


def _actions(acts, groupes, taches) -> list[tuple]:
    """(série, condition, clé) des actions des groupes dont la tâche est dans `taches` (ordre stable)."""
    taches = set(map(str, taches))
    return [(s, c, k) for s, c in groupes for k in acts.cles(s, c) if str(acts.tache(k)) in taches]


def _sequences(acts, actions, couche) -> list:
    return [acts.lire(s, k, couche) for s, _, k in actions]


# --------------------------------------------------------------------------------------------------- apprentissage, choix

@dataclass
class Contexte:
    acts: object
    graines: object
    couches: tuple
    appareil: str = "cpu"
    debit: GardeDebit | None = None
    familles: tuple = FAMILLES
    reelle: bool = True
    epoques: int = EPOQUES
    n_plis_internes: int = N_PLIS_INTERNES
    journal: list = field(default_factory=list)

    def __post_init__(self):
        if self.reelle and int(self.epoques) != EPOQUES:
            raise GardeArret(f"marche réelle : {self.epoques} époques, {EPOQUES} fixées par le texte (point 5)")
        if self.reelle and int(self.n_plis_internes) != N_PLIS_INTERNES:
            raise GardeArret(f"marche réelle : {self.n_plis_internes} plis internes, {N_PLIS_INTERNES} fixés par le texte")
        if self.reelle and tuple(self.familles) not in (FAMILLES, ("lineaire",)):
            raise GardeArret(f"marche réelle : familles {self.familles} : {FAMILLES} (texte) ou ('lineaire',) (variante (r1)) "
                             "seulement")


def _entrainer_chrono(ctx: Contexte, lot, reglage, nom, y, cle_graine):
    t0 = time.perf_counter()
    try:
        return ac.entrainer(lot, reglage["famille"], nom, reglage["couche"], y, reglage["l2"], ctx.graines.entier(cle_graine),
                            epoques=int(ctx.epoques))
    finally:
        if ctx.debit is not None:
            ctx.debit.noter(time.perf_counter() - t0, reglage["famille"])


def apprendre_recette(ctx: Contexte, serie_nom: str, cellule: str, k: int, positifs: tuple, negatifs: tuple,
                      taches_app, taches_lues, internes) -> dict:
    """Grille × plis internes, choix du réglage, sonde finale (sonde ou ENC). Rend {reglage, sonde, lot, sequences_app, y_app,
    actions_app, echecs_internes} ou {echec, …}. Aucune aire n'est rendue."""
    exiger_disjonction(taches_app, taches_lues, f"apprentissage {serie_nom}/{cellule}/e{k}")
    for interne in internes:
        exiger_disjonction(interne, taches_lues, f"réglage {serie_nom}/{cellule}/e{k}")
    regs = grille(ctx.couches, ctx.familles)
    sommes, echecs = {r["nom"]: [] for r in regs}, 0
    for j, interne in enumerate(internes):
        exiger_sans_signal(f"l'apprentissage {serie_nom}/{cellule}/e{k}i{j}")
        app = [t for t in taches_app if t not in set(interne)]
        a_app, a_val = _actions(ctx.acts, [positifs, negatifs], app), _actions(ctx.acts, [positifs, negatifs], interne)
        y_app = np.array([1 if (s, c) == positifs else 0 for s, c, _ in a_app])
        y_val = np.array([1 if (s, c) == positifs else 0 for s, c, _ in a_val])
        t_val = [ctx.acts.tache(x) for _, _, x in a_val]
        for couche in ctx.couches:
            lot = ac.LotCarte(_sequences(ctx.acts, a_app, couche), ctx.appareil)
            seq_val = _sequences(ctx.acts, a_val, couche)
            for r in [x for x in regs if x["couche"] == couche]:
                nom = f"{serie_nom}-{cellule}-e{k}i{j}-{r['nom']}"
                try:
                    s = _entrainer_chrono(ctx, lot, r, nom, y_app, f"bbis/entrainement/{serie_nom}/{cellule}/e{k}i{j}/{r['nom']}")
                except ac.SondeEnEchec:
                    sommes[r["nom"]] = None
                    echecs += 1
                    continue
                if sommes[r["nom"]] is not None:
                    sommes[r["nom"]].append(aire_apprentissage(ac.scores(s, seq_val), y_val, t_val, taches_lues))
            del lot
    aires = {n: (float(sum(v) / len(v)) if v else None) for n, v in sommes.items()}
    try:
        retenu = choisir_reglage(aires, regs, ctx.couches)
    except GardeArret as e:
        return {"echec": str(e), "reglage": None, "echecs_internes": echecs}
    finally:
        del aires, sommes                                          # jamais écrites
    a_app = _actions(ctx.acts, [positifs, negatifs], taches_app)
    y_app = np.array([1 if (s, c) == positifs else 0 for s, c, _ in a_app])
    seqs = _sequences(ctx.acts, a_app, retenu["couche"])
    lot = ac.LotCarte(seqs, ctx.appareil)
    nom = f"{serie_nom}-{cellule}-e{k}"
    try:
        sonde = _entrainer_chrono(ctx, lot, retenu, nom, y_app, f"bbis/entrainement/{serie_nom}/{cellule}/e{k}/{retenu['nom']}")
    except ac.SondeEnEchec as e:
        return {"echec": str(e), "reglage": retenu, "echecs_internes": echecs}
    return {"reglage": retenu, "sonde": sonde, "lot": lot, "sequences_app": seqs, "y_app": y_app, "actions_app": a_app,
            "echecs_internes": echecs}


def reetiquetage(taches_ordonnees, rng) -> np.ndarray:
    """Échange par tâche (probabilité un demi), sur les tâches dans l'ordre donné (toutes les tâches d'évaluation, triées)."""
    return rng.random(len(taches_ordonnees)) < 0.5


def etiquettes_reetiquetees(actions, positifs: tuple, echanges: np.ndarray, index_taches: dict, acts) -> np.ndarray:
    """Étiquettes du jeu après échange des deux épisodes de la tâche (1 ↔ 0) dans les tâches échangées."""
    y = np.array([1 if (s, c) == positifs else 0 for s, c, _ in actions])
    e = np.array([bool(echanges[index_taches[str(acts.tache(k))]]) for _, _, k in actions])
    return np.where(e, 1 - y, y)


# ------------------------------------------------------------------------------------------------------------- notation

def scores_par_lots(sondes: list, seqs: list) -> np.ndarray:
    """(sondes, actions) : sondes linéaires de même couche et même agrégation notées par lots (`plancher_v3`, contrôle en ligne
    contre la boucle du harnais) ; une sonde absente (en échec) rend une ligne de `NaN`."""
    sortie = np.full((len(sondes), len(seqs)), np.nan)
    presentes = [i for i, s in enumerate(sondes) if s is not None]
    if presentes and seqs:
        sortie[presentes] = scores_plancher_vectorises([sondes[i] for i in presentes], seqs).T
    return sortie


def _scores_sc(acts, sonde, plancher, actions, couche) -> dict:
    """Second score par action, restreint aux jetons notés strictement avant le champ COST (frontière de `sondes_neuves_v1`) ;
    action sans champ lisible ou sans jeton avant le champ : exclue (`sc_valide` faux, comptée)."""
    valide, seqs = [], []
    for s, _, k in actions:
        p = position_champ_cout(acts.texte(k))
        n = frontiere_jetons(acts.tokeniseur, acts.ids(k), acts.texte(k), p) if p is not None else 0
        a = acts.lire(s, k, couche)
        n = min(n, a.shape[0])
        valide.append(n >= 1)
        if n >= 1:
            seqs.append(a[:n])
    v = np.array(valide, dtype=bool)
    sonde_sc = np.full(len(actions), np.nan)
    plancher_sc = np.full((len(plancher), len(actions)), np.nan)
    if seqs:
        sonde_sc[v] = ac.scores(sonde, seqs)
        plancher_sc[:, v] = scores_plancher_vectorises(plancher, seqs).T
    return {"sc_valide": v, "sc_sonde": sonde_sc, "sc_plancher": plancher_sc}


def noter_source(ctx: Contexte, cellule: str, k: int, plan: dict, sonde: dict, plancher: list, nuls: list, enc: dict,
                 taches_lues) -> dict:
    """Tableaux du fichier fermé pour une source et un pli : par groupe, clés, tâches, scores ; scores d'apprentissage. Aucun
    résumé, aucune aire."""
    sortie = {}
    couche = sonde["reglage"]["couche"]
    for groupe in plan["sonde"]:
        exiger_sans_signal(f"la notation {cellule}/e{k}/{groupe}")
        actions = _actions(ctx.acts, [groupe], taches_lues)
        g = nom_groupe(groupe)
        seqs = _sequences(ctx.acts, actions, couche)
        sortie[f"{g}__cles"] = np.array([x for _, _, x in actions])
        sortie[f"{g}__taches"] = np.array([str(ctx.acts.tache(x)) for _, _, x in actions])
        sortie[f"{g}__sonde"] = ac.scores(sonde["sonde"], seqs)
        sortie[f"{g}__plancher"] = scores_plancher_vectorises(plancher, seqs).T
        if groupe in plan["nul"] and nuls:
            sortie[f"{g}__nul"] = scores_par_lots(nuls, seqs)
        if groupe in plan["sc"]:
            for cle, v in _scores_sc(ctx.acts, sonde["sonde"], plancher, actions, couche).items():
                sortie[f"{g}__{cle}"] = v
    if enc is not None and "sonde" in enc:
        for groupe in plan["enc"]:
            actions = _actions(ctx.acts, [groupe], taches_lues)
            g = nom_groupe(groupe)
            if f"{g}__cles" not in sortie:
                sortie[f"{g}__cles"] = np.array([x for _, _, x in actions])
                sortie[f"{g}__taches"] = np.array([str(ctx.acts.tache(x)) for _, _, x in actions])
            elif list(sortie[f"{g}__cles"]) != [x for _, _, x in actions]:
                raise GardeArret(f"notation {cellule}/e{k} : clés du groupe {g} différentes entre la sonde et ENC : arrêt")
            sortie[f"{g}__enc"] = ac.scores(enc["sonde"], _sequences(ctx.acts, actions, enc["reglage"]["couche"]))
        sortie["app_enc__cles"] = np.array([x for _, _, x in enc["actions_app"]])
        sortie["app_enc__y"] = enc["y_app"]
        sortie["app_enc__enc"] = ac.scores(enc["sonde"], enc["sequences_app"])
    sortie["app__cles"] = np.array([x for _, _, x in sonde["actions_app"]])
    sortie["app__y"] = sonde["y_app"]
    sortie["app__sonde"] = ac.scores(sonde["sonde"], sonde["sequences_app"])
    if nuls:
        sortie["app__nul"] = scores_par_lots(nuls, sonde["sequences_app"])
    return sortie


def apprendre_source(ctx: Contexte, cellule: str, positifs_cond: str, plan: dict, k: int, plis: dict, taches_triees,
                     n_reetiquetages: int = N_REETIQUETAGES, n_directions: int = N_DIRECTIONS) -> dict:
    """Une source plafond et un pli lu k : sonde (grille, sonde finale), plancher, nul de réétiquetage, ENC, notation. Rend {meta
    (sans aire), tableaux, sonde, plancher, enc_sonde, sequences_app, y_app, reglage}."""
    taches_lues = sorted(t for t, p in plis.items() if p == k)
    taches_app = sorted(t for t, p in plis.items() if p != k)
    internes = plis_internes(taches_app, ctx.graines.rng(f"bbis/interne/e{k}"), int(ctx.n_plis_internes), reelle=ctx.reelle)
    pos, neg = ("O", positifs_cond), ("O", H)
    meta = {"cellule": cellule, "pli_lu": k, "taches_lues": taches_lues, "plis_internes": internes}
    sonde = apprendre_recette(ctx, "sonde", cellule, k, pos, neg, taches_app, taches_lues, internes)
    meta["reglage"] = sonde["reglage"]["nom"] if sonde.get("reglage") else None
    meta["echecs_internes"] = sonde["echecs_internes"]
    if "echec" in sonde:
        meta["echec"] = sonde["echec"]
        return {"meta": meta, "tableaux": {}}
    r = sonde["reglage"]
    exiger_disjonction([ctx.acts.tache(x) for _, _, x in sonde["actions_app"]], taches_lues, "covariance du plancher")
    plancher = plancher_apparie(f"{sonde['sonde'].nom}-bbis", r["couche"], sonde["sequences_app"], r["agregation"],
                                int(n_directions), ctx.graines.entier(f"bbis/plancher/{cellule}/e{k}"))
    index = {t: i for i, t in enumerate(taches_triees)}
    nuls, echanges = [], []
    for rr in range(int(n_reetiquetages)):
        e = reetiquetage(taches_triees, ctx.graines.rng(f"bbis/reetiquetage/{cellule}/{rr}"))
        echanges.append(e)
        y_r = etiquettes_reetiquetees(sonde["actions_app"], pos, e, index, ctx.acts)
        if len(set(y_r.tolist())) < 2:
            nuls.append(None)
            continue
        try:
            nuls.append(_entrainer_chrono(ctx, sonde["lot"], r, f"nul{rr}-{cellule}-e{k}", y_r,
                                          f"bbis/entrainement/nul{rr}/{cellule}/e{k}/{r['nom']}"))
        except ac.SondeEnEchec:
            nuls.append(None)
    enc = apprendre_recette(ctx, "enc", cellule, k, plan["enc_positifs"], neg, taches_app, taches_lues, internes)
    tableaux = noter_source(ctx, cellule, k, plan, sonde, plancher, nuls, enc, taches_lues)
    tableaux["nul__echanges"] = np.array(echanges, dtype=bool).reshape(int(n_reetiquetages), len(taches_triees))
    tableaux["nul__taches"] = np.array(list(taches_triees))
    meta.update({"empreinte_sonde": sonde["sonde"].empreinte(), "famille": r["famille"], "couche": r["couche"], "l2": r["l2"],
                 "agregation": r["agregation"], "nom_sonde": sonde["sonde"].nom, "n_plancher": len(plancher),
                 "noms_deux_premieres": [p.nom for p in plancher[:2]],
                 "empreintes_deux_premieres": [p.empreinte() for p in plancher[:2]],
                 "nuls_en_echec": sum(1 for n in nuls if n is None), "n_reetiquetages": int(n_reetiquetages),
                 "enc": ({"reglage": enc["reglage"]["nom"], "empreinte": enc["sonde"].empreinte(),
                          "echecs_internes": enc["echecs_internes"]} if "sonde" in enc
                         else {"echec": enc.get("echec"), "echecs_internes": enc.get("echecs_internes")})})
    return {"meta": meta, "tableaux": tableaux, "sonde": sonde["sonde"], "plancher": plancher, "enc_sonde": enc.get("sonde"),
            "sequences_app": sonde["sequences_app"], "y_app": sonde["y_app"], "reglage": r}


class ControleCarte:
    """Contrôle carte-processeur (plan, point 5) : le couple (cellule, pli) est tiré par la graine `bbis/egalite-carte` avant
    tout apprentissage ; `apres(…)` le joue dès que ce couple est appris (docstring du module)."""

    def __init__(self, graines, couples: list, n_actions: int = N_ACTIONS_CONTROLE_CARTE):
        if not couples:
            raise GardeArret("contrôle carte-processeur : aucun couple (cellule, pli)")
        self.rng = graines.rng("bbis/egalite-carte")
        self.graines = graines
        self.couples = sorted(couples)
        self.couple = self.couples[int(self.rng.integers(0, len(self.couples)))]
        self.n_actions = int(n_actions)
        self.resultat = None

    def apres(self, ctx: Contexte, cellule: str, k: int, positifs: str, res: dict, plis: dict) -> dict | None:
        if (cellule, k) != self.couple or self.resultat is not None:
            return None
        if "sonde" not in res:
            self.resultat = {"cellule": cellule, "pli": int(k), "sans_objet": "sonde du couple tiré en échec"}
            return self.resultat
        reglage = res["reglage"]
        taches_lues = sorted(t for t, p in plis.items() if p == k)
        a_lu = _actions(ctx.acts, [("O", positifs), ("O", H)], taches_lues)
        choix = sorted(self.rng.choice(len(a_lu), size=min(self.n_actions, len(a_lu)), replace=False).tolist())
        r = ac.controle_carte_processeur(res["sonde"], res["sequences_app"], res["y_app"], reglage,
                                         self.graines.entier(f"bbis/entrainement/sonde/{cellule}/e{k}/{reglage['nom']}"),
                                         _sequences(ctx.acts, [a_lu[i] for i in choix], reglage["couche"]),
                                         epoques=int(ctx.epoques))
        r.update({"cellule": cellule, "pli": int(k)})
        self.resultat = r
        return r


__all__ = ["plis_internes", "aire_apprentissage", "exiger_disjonction", "choisir_reglage", "GardeDebit", "ArretDebit",
           "apprentissages_prevus", "plan_de_notation", "nom_groupe", "Contexte", "apprendre_recette", "reetiquetage",
           "etiquettes_reetiquetees", "scores_par_lots", "noter_source", "apprendre_source", "ControleCarte", "LIMITE_H"]
