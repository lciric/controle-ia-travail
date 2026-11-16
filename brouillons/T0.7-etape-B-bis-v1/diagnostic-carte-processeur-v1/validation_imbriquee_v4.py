"""Validation croisée imbriquée de l'étape B bis, v4 (proposition du diagnostic `rapport-diagnostic-carte-processeur-v1.md`) : la
v3, dont **le seul contrôle carte-processeur change** ; tout le reste est celui de la v3 (donc de la v1), importé sans
modification ; les v1, v2 et v3 restent (R12).

**Pourquoi** : la course du 16 novembre s'est arrêtée sur « linéaire à 300 époques : écart relatif 1,004 > 10⁻⁴ ». Le diagnostic
(données fabriquées, processeur seulement) montre que la sonde linéaire agrégée par le maximum, apprise 300 époques par Adam
(pas 0,05) avec une régularisation faible, peut rendre **une autre sonde** sur une autre pile de calcul, sans aucune erreur de
chaîne, quand beaucoup de jetons d'une action sont des quasi-copies les uns des autres (quasi-égalités au maximum, décidées par
l'arrondi) : même problème, seuls les ordres des sommes changent, et l'écart du contrôle atteint 1 à 5 ; à 3 époques, il reste
au plus de l'ordre de 10⁻¹⁰ (rapport, § 4). C'est le mécanisme déjà reconnu pour l'attention (addendum EC-1), étendu à la linéaire.

**Contrôle v4** (`controle_deux_horizons`) : dans **chaque** famille de la marche (variante (r1) : la linéaire seule), à la
couche et à la régularisation du réglage retenu du couple :
- **carte contre processeur à 3 époques** (`EPOQUES_CONTROLE`) : la sonde apprise 3 époques sur la carte depuis le même départ
  (graine `bbis/entrainement/sonde/<cellule>/e<k>/<réglage de la famille>`) contre la même réapprise 3 époques par
  `sondes.familles` (`Reglages(epoques=3)`) ; écart relatif maximal des scores sur les 256 actions ≤ 10⁻⁴, sinon arrêt ;
- **déterminisme à 300 époques sur la carte** : la sonde de 300 époques de la famille (la sonde finale du couple si sa famille
  est retenue, sinon apprise sur la carte à ce réglage) est réapprise une seconde fois sur la carte : paramètres égaux au bit
  près (w, b, q), sinon arrêt ;
- **information, sans arrêt** (linéaire seulement, `informer_300`) : l'écart carte-processeur à 300 époques de la sonde
  linéaire, comme en v3, est calculé et écrit (`ecart_300_information`) ; il ne décide rien (R-PILE l'explique à la lecture).
Une sonde de contrôle en échec (perte ou paramètres non finis, `SondeEnEchec`), à 3 ou à 300 époques : arrêt (erreur de chaîne).
Tirage du couple : celui de la v3 (fin de l'apprentissage, parmi les sondes finales finies, graine `bbis/egalite-carte`, mêmes
actions). Champ écrit : `lineaire` et `attention` portent `ecart_relatif_max` (à 3 époques) et `epoques` = 3 ;
`determinisme_lineaire` et `determinisme_attention` portent `egal_au_bit` vrai : `lecture_v2.exiger_controle_carte` le lit sans
changement (essai `essai_controle_v4_v1.py`).

Coût déclaré, en plus de la v3 : sur la carte, une linéaire de 3 époques et une linéaire de 300 (seconde copie) ; sur le
processeur, une linéaire de 3 époques (la linéaire de 300 époques du processeur est celle de la v3, gardée pour l'information).

**Ce que ce changement touche dans le texte** : les fragments EC-1 et EC-4 de l'addendum scellé (« la linéaire à 300 époques »)
et la réserve R-PILE (EC-2, EC-3 : « sonde « attention » ») : c'est un **écart à déclarer** (rapport du diagnostic, § 6), pas une
correction du code « sous ce texte ». Ce module n'est qu'une proposition : il n'est importé par aucune marche.
"""
from __future__ import annotations

import numpy as np

from controle_ia.gardes import GardeArret
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import validation_imbriquee_v1 as v1
from controle_ia.t07bbis import validation_imbriquee_v3 as v3
from controle_ia.t07bbis.commun_v1 import (AGREGATION_DE, EPOQUES, FAMILLES, N_ACTIONS_CONTROLE_CARTE, TOLERANCE_CARTE, H,
                                           reglage_nom)
from controle_ia.t07bbis.validation_imbriquee_v3 import (FACTEUR_DEBIT, LIMITE_H, MARGE_H, N_PREMIERS, ArretDebit,  # noqa: F401
                                                         Contexte, GardeDebit, aire_apprentissage, apprendre_recette,
                                                         apprendre_source, apprentissages_prevus, choisir_reglage,
                                                         egales_au_bit, etiquettes_reetiquetees, exiger_disjonction,
                                                         nom_groupe, noter_source, plan_de_notation, plis_internes,
                                                         reetiquetage, scores_par_lots, sonde_finie)

EPOQUES_CONTROLE = 3
ORDRE = ("lineaire", "attention")


def controle_deux_horizons(lot, sequences_app, y_app, couche: int, l2: float, graine_de, sequences_controle,
                           familles=FAMILLES, sondes_300: dict | None = None, epoques: int = EPOQUES,
                           epoques_controle: int = EPOQUES_CONTROLE, tolerance: float = TOLERANCE_CARTE,
                           nom: str = "controle", informer_300: bool = True) -> dict:
    """Contrôle v4 du couple (docstring du module). Mêmes arguments que la v3 (`epoques_controle` remplace
    `epoques_attention` et vaut pour les deux familles). Arrêt (`GardeArret`, « erreur de chaîne ») au premier écart."""
    if int(epoques_controle) >= int(epoques) or int(epoques_controle) < 1:
        raise GardeArret(f"horizon du contrôle {epoques_controle} hors de [1, {epoques}[ : refus")
    inconnues = [f for f in familles if f not in ORDRE]
    if inconnues or not familles:
        raise GardeArret(f"familles {familles} : linéaire et attention seulement")
    sondes_300 = dict(sondes_300 or {})
    sortie = {"tolerance": float(tolerance), "couche": int(couche), "l2": float(l2), "familles": [f for f in ORDRE if f in familles],
              "version_controle": "v4"}
    ec = int(epoques_controle)

    def apprendre(f, ep, suffixe):
        return ac.entrainer(lot, f, f"{nom}-{f}-{suffixe}", int(couche), y_app, float(l2), int(graine_de(f)), epoques=int(ep))

    for f in sortie["familles"]:
        reglage = {"famille": f, "couche": int(couche), "l2": float(l2), "agregation": AGREGATION_DE[f],
                   "nom": reglage_nom(f, couche, l2)}
        try:
            s = apprendre(f, ec, f"e{ec}")
        except ac.SondeEnEchec as e:
            raise GardeArret(f"{f} à {ec} époques : sonde de contrôle en échec ({e}) : arrêt (erreur de chaîne)") from None
        try:
            r = ac.controle_carte_processeur(s, sequences_app, y_app, reglage, int(graine_de(f)), sequences_controle,
                                             tolerance=tolerance, epoques=ec)
        except GardeArret as e:
            raise GardeArret(f"{f} à {ec} époques : {e}") from None
        sortie[f] = {**r, "epoques": ec}
        try:
            a = sondes_300.get(f)
            a = a if a is not None else apprendre(f, epoques, f"e{epoques}")
            b = apprendre(f, epoques, f"e{epoques}-bis")
        except ac.SondeEnEchec as e:
            raise GardeArret(f"{f} à {epoques} époques (déterminisme) : sonde en échec ({e}) : arrêt (erreur de chaîne)") from None
        if not egales_au_bit(a, b):
            raise GardeArret(f"{f} à {epoques} époques réapprise sur la carte : paramètres différents au bit près "
                             "(apprentissage non déterministe) : arrêt (erreur de chaîne)")
        sortie[f"determinisme_{f}"] = {"epoques": int(epoques), "egal_au_bit": True}
        if f == "lineaire" and informer_300:
            try:
                i = ac.controle_carte_processeur(a, sequences_app, y_app, reglage, int(graine_de(f)), sequences_controle,
                                                 tolerance=float("inf"), epoques=int(epoques))
                sortie[f]["ecart_300_information"] = {"ecart_relatif_max": float(i["ecart_relatif_max"]),
                                                      "epoques": int(epoques), "decide": False}
            except GardeArret as e:                     # écart non fini : écrit comme information, sans arrêt
                sortie[f]["ecart_300_information"] = {"refus": str(e)[:500], "epoques": int(epoques), "decide": False}
    return sortie


class ControleCarte(v3.ControleCarte):
    """Contrôle carte-processeur de la v4 : tirage de la v3 (une fois, à la fin de l'apprentissage, parmi les sondes finales
    finies, même ordre trié, même graine) ; contrôle `controle_deux_horizons` de ce module."""

    def jouer(self, ctx: Contexte, sources: dict, plis: dict) -> dict:
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


__all__ = list(v3.__all__) + ["EPOQUES_CONTROLE"]
