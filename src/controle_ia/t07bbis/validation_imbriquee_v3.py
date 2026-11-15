"""Validation croisée imbriquée de l'étape B bis, v3 : la v2 (contrôle carte-processeur aux deux horizons), **sans aucune issue
« sans objet »** (décision de la mère R-2919, voie (b) du majeur M2 de `contre-lecture-brouillon5-et-code-v2-v1.md` ; brouillon 6
du texte, plan, point 5, et liste d'arrêt) : une sonde apprise pour le contrôle en échec (perte ou paramètres non finis), à 3 ou
à 300 époques, déterminisme compris, **arrête** (erreur de chaîne) ; le couple du contrôle est tiré **à la fin de l'apprentissage,
parmi les couples dont la sonde finale est finie**, dans le même ordre trié et avec la même graine que la v1 (`bbis/egalite-carte` :
même couple et mêmes actions que la v1 quand toutes les sondes finales sont finies) ; aucun : arrêt. Tout le reste est **celui de
la v1, importé sans modification** (`validation_imbriquee_v1` : plis, grille, sélection, sonde finale, plancher, nul de
réétiquetage, ENC, garde de débit, notation) ; les v1 et v2 restent (R12).

**Contrôle à la marche** (`ControleCarte.jouer`, `controle_deux_horizons`) : à la fin de l'apprentissage, le (cellule, pli) est
tiré parmi ceux dont la sonde finale est finie (graine `bbis/egalite-carte`, couples triés, puis les 256 actions de contrôle de
son pli lu, même générateur) ; à la couche et à la régularisation de son réglage retenu, **dans les deux familles de la marche**
(variante (r1) : la linéaire seule) :
- **linéaire, 300 époques** : la sonde linéaire de la carte (la sonde finale si le réglage retenu est linéaire, sinon apprise sur la
  carte à ce réglage, graine `bbis/entrainement/sonde/<cellule>/e<k>/<réglage linéaire>`) contre la même sonde réapprise sur le
  processeur par `sondes.familles` ; écart relatif maximal des scores ≤ 10⁻⁴ ;
- **attention, 3 époques** (`EPOQUES_CONTROLE_ATTENTION`) : la sonde « attention » apprise **3 époques** sur la carte, depuis le même
  départ (graine `bbis/entrainement/sonde/<cellule>/e<k>/<réglage attention>`), contre la même réapprise 3 époques par
  `sondes.familles` (`Reglages(epoques=3)`) ; écart ≤ 10⁻⁴ ;
- **déterminisme de l'attention à 300 époques** : la sonde « attention » de 300 époques (la sonde finale si le réglage retenu est
  « attention », sinon apprise sur la carte à ce réglage) est réapprise **une seconde fois sur la carte** ; paramètres égaux au bit
  près (w, b, q), sinon arrêt.
Tout écart : `GardeArret` « … : arrêt (erreur de chaîne) ». Raison (écrite au texte avant toute lecture) : sans signal appris, les
300 époques de l'attention amplifient les écarts d'arrondi entre deux piles de calcul au-delà de 10⁻⁴ ; à 3 époques, non
(`diagnostic-ecart-attention-carte-v1.md`, `diagnostic-stabilite-aires-attention-v1.md`). Variante (r1) (famille linéaire seule) :
seul le contrôle linéaire est joué. Une sonde de contrôle en échec (perte ou paramètres non finis, `SondeEnEchec`) : **arrêt**
(depuis w = 0 et b = 0, trois pas d'Adam ne peuvent rendre une perte non finie qu'à partir d'activations non finies : une erreur de
chaîne).

Coût déclaré : sur la carte, au plus une linéaire de 300 époques, une attention de 3 époques et deux de 300 ; sur le processeur,
une linéaire de 300 époques et une attention de 3 (au lieu de 300 époques de la famille retenue en v1).
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from . import apprentissage_carte_v1 as ac
from . import validation_imbriquee_v1 as v1
from .commun_v1 import AGREGATION_DE, EPOQUES, FAMILLES, N_ACTIONS_CONTROLE_CARTE, TOLERANCE_CARTE, H, reglage_nom
from .validation_imbriquee_v1 import (FACTEUR_DEBIT, LIMITE_H, MARGE_H, N_PREMIERS, ArretDebit, Contexte, GardeDebit, aire_apprentissage, apprendre_recette,  # noqa: F401
                                      apprendre_source, apprentissages_prevus, choisir_reglage, etiquettes_reetiquetees,
                                      exiger_disjonction, nom_groupe, noter_source, plan_de_notation, plis_internes,
                                      reetiquetage, scores_par_lots)

EPOQUES_CONTROLE_ATTENTION = 3
ORDRE = ("lineaire", "attention")


def egales_au_bit(a, b) -> bool:
    """Deux sondes de même famille aux paramètres égaux au bit près (w, b, q)."""
    return bool(np.array_equal(a.w, b.w) and a.b == b.b and ((a.q is None and b.q is None) or
                                                            (a.q is not None and b.q is not None and np.array_equal(a.q, b.q))))


def controle_deux_horizons(lot, sequences_app, y_app, couche: int, l2: float, graine_de, sequences_controle,
                           familles=FAMILLES, sondes_300: dict | None = None, epoques: int = EPOQUES,
                           epoques_attention: int = EPOQUES_CONTROLE_ATTENTION, tolerance: float = TOLERANCE_CARTE,
                           nom: str = "controle") -> dict:
    """Contrôle du couple (docstring du module). `lot` : jetons d'apprentissage du couple, à la couche, sur l'appareil de la marche
    (`apprentissage_carte_v1.LotCarte`) ; `graine_de(famille)` : graine entière du réglage (famille, couche, l2) ; `sondes_300` :
    {famille: sonde de `epoques` époques déjà apprise sur la carte à ce réglage} (la sonde finale du couple), réutilisée telle quelle.
    Rend les écarts, horizons et le déterminisme ; arrêt (`GardeArret`, « erreur de chaîne ») au premier écart."""
    if int(epoques_attention) >= int(epoques) or int(epoques_attention) < 1:
        raise GardeArret(f"horizon de l'attention {epoques_attention} hors de [1, {epoques}[ : refus")
    inconnues = [f for f in familles if f not in ORDRE]
    if inconnues or not familles:
        raise GardeArret(f"familles {familles} : linéaire et attention seulement")
    sondes_300 = dict(sondes_300 or {})
    sortie = {"tolerance": float(tolerance), "couche": int(couche), "l2": float(l2), "familles": [f for f in ORDRE if f in familles]}

    def apprendre(f, ep, suffixe):
        return ac.entrainer(lot, f, f"{nom}-{f}-{suffixe}", int(couche), y_app, float(l2), int(graine_de(f)), epoques=int(ep))

    for f in sortie["familles"]:
        reglage = {"famille": f, "couche": int(couche), "l2": float(l2), "agregation": AGREGATION_DE[f],
                   "nom": reglage_nom(f, couche, l2)}
        ep = int(epoques) if f == "lineaire" else int(epoques_attention)
        try:
            if f == "lineaire":
                s = sondes_300.get(f)
                s = s if s is not None else apprendre(f, ep, f"e{ep}")
            else:
                s = apprendre(f, ep, f"e{ep}")
        except ac.SondeEnEchec as e:
            raise GardeArret(f"{f} à {ep} époques : sonde de contrôle en échec ({e}) : arrêt (erreur de chaîne)") from None
        try:
            r = ac.controle_carte_processeur(s, sequences_app, y_app, reglage, int(graine_de(f)), sequences_controle,
                                             tolerance=tolerance, epoques=ep)
        except GardeArret as e:
            raise GardeArret(f"{f} à {ep} époques : {e}") from None
        sortie[f] = {**r, "epoques": ep}
        if f == "attention":
            try:
                a = sondes_300.get(f)
                a = a if a is not None else apprendre(f, epoques, f"e{epoques}")
                b = apprendre(f, epoques, f"e{epoques}-bis")
            except ac.SondeEnEchec as e:
                raise GardeArret(f"attention à {epoques} époques (déterminisme) : sonde en échec ({e}) : arrêt (erreur de "
                                 "chaîne)") from None
            if not egales_au_bit(a, b):
                raise GardeArret(f"attention à {epoques} époques réapprise sur la carte : paramètres différents au bit près "
                                 "(apprentissage non déterministe) : arrêt (erreur de chaîne)")
            sortie["determinisme_attention"] = {"epoques": int(epoques), "egal_au_bit": True}
    return sortie


def sonde_finie(res: dict) -> bool:
    """La source porte une sonde finale aux paramètres finis (w, b, q)."""
    s = res.get("sonde") if isinstance(res, dict) else None
    return bool(s is not None and np.all(np.isfinite(s.w)) and np.isfinite(s.b) and (s.q is None or np.all(np.isfinite(s.q))))


class ControleCarte:
    """Contrôle carte-processeur de la v3 : joué **une fois, à la fin de l'apprentissage** (`jouer`), sur un couple tiré parmi
    ceux dont la sonde finale est finie (même ordre trié, même graine que la v1) ; aucune issue « sans objet »."""

    def __init__(self, graines, couples: list, n_actions: int = N_ACTIONS_CONTROLE_CARTE):
        if not couples:
            raise GardeArret("contrôle carte-processeur : aucun couple (cellule, pli)")
        self.graines = graines
        self.couples = sorted(couples)
        self.n_actions = int(n_actions)
        self.couple = None
        self.resultat = None

    def jouer(self, ctx: Contexte, sources: dict, plis: dict) -> dict:
        """`sources` : {(cellule, pli) : (positifs, res de `apprendre_source`)}. Tire le couple parmi les sondes finales finies,
        puis joue `controle_deux_horizons` ; arrêt si aucun couple n'a de sonde finale finie, ou au premier écart."""
        if self.resultat is not None:
            raise GardeArret("contrôle carte-processeur déjà joué : une seule fois")
        finis = [c for c in self.couples if c in sources and sonde_finie(sources[c][1])]
        if not finis:
            raise GardeArret(f"contrôle carte-processeur : aucun des {len(self.couples)} couples n'a de sonde finale finie : arrêt "
                             "(erreur de chaîne)")
        rng = self.graines.rng("bbis/egalite-carte")
        self.couple = finis[int(rng.integers(0, len(finis)))]
        cellule, k = self.couple
        positifs, res = sources[self.couple]
        reglage = res["reglage"]
        taches_lues = sorted(t for t, p in plis.items() if p == k)
        a_lu = v1._actions(ctx.acts, [("O", positifs), ("O", H)], taches_lues)
        choix = sorted(rng.choice(len(a_lu), size=min(self.n_actions, len(a_lu)), replace=False).tolist())
        controle = v1._sequences(ctx.acts, [a_lu[i] for i in choix], reglage["couche"])
        lot = ac.LotCarte(res["sequences_app"], ctx.appareil)

        def graine_de(f):
            return self.graines.entier(f"bbis/entrainement/sonde/{cellule}/e{k}/{reglage_nom(f, reglage['couche'], reglage['l2'])}")

        r = controle_deux_horizons(lot, res["sequences_app"], res["y_app"], reglage["couche"], reglage["l2"], graine_de, controle,
                                   familles=tuple(ctx.familles), sondes_300={reglage["famille"]: res["sonde"]},
                                   epoques=int(ctx.epoques), nom=f"controle-{cellule}-e{k}")
        r.update({"cellule": cellule, "pli": int(k), "reglage_retenu": reglage["nom"], "actions": len(choix),
                  "tirage": {"couples": len(self.couples), "sondes_finales_finies": len(finis)}})
        self.resultat = r
        return r


__all__ = list(v1.__all__) + ["controle_deux_horizons", "egales_au_bit", "sonde_finie", "EPOQUES_CONTROLE_ATTENTION",
                              "N_ACTIONS_CONTROLE_CARTE"]
