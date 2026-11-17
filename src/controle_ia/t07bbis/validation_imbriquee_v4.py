"""Validation croisée imbriquée de l'étape B bis, v4 (second addendum d'écart, `brouillon-second-addendum-bbis-v1.md` ; proposition
du diagnostic `rapport-diagnostic-carte-processeur-v1.md`, `ba127aa0…`) : la v3, dont **le contrôle carte-processeur change**, plus
**une mesure d'information** (dispersion des aires entre deux ordres de calcul, réserve R-D, GO-2026-11-16-12) ; tout le reste
est celui de la v3 (donc de la v1), importé sans modification ; les v1, v2 et v3 restent (R12).

**Pourquoi** : la course du 16 novembre s'est arrêtée sur « linéaire à 300 époques : écart relatif 1,004 > 10⁻⁴ ». Le diagnostic
(données fabriquées, processeur seulement) et sa contre-lecture (`0da982fb…`) montrent que la sonde linéaire agrégée par le
maximum, apprise 300 époques par Adam (pas 0,05) avec une régularisation faible, peut rendre **une autre sonde** sur une autre
pile de calcul, sans aucune erreur de chaîne, quand elle ajuste mal (régimes anisotropes de bas rang, avec ou sans jetons
presque identiques : réserve R-A de la contre-lecture ; la présence de quasi-copies n'est ni nécessaire ni suffisante) : même
problème, seuls les ordres des sommes changent, et l'écart du contrôle atteint 0,6 à 12,8 ; à 3 époques, il reste au plus de
l'ordre de 10⁻¹⁰. C'est le mécanisme déjà reconnu pour l'attention (addendum EC-1), étendu à la linéaire.

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
`determinisme_lineaire` et `determinisme_attention` portent `egal_au_bit` vrai ; `version_controle` = « v4 » (lu par
`lecture_v3.exiger_controle_carte`).

Coût déclaré, en plus de la v3 : sur la carte, une linéaire de 3 époques et une linéaire de 300 (seconde copie) ; sur le
processeur, une linéaire de 3 époques (la linéaire de 300 époques du processeur est celle de la v3, gardée pour l'information).

**Mesure de dispersion entre deux ordres de calcul** (`mesurer_dispersion`, information seulement ; second addendum, MD) : après
le contrôle, pour chaque source et chaque pli dont la sonde finale est apprise, la **recette entière de la sonde** (grille ×
plis internes, choix du réglage par la même règle et les mêmes ex aequo, sonde finale sur les 32 tâches) est rejouée sur la carte
dans l'**ordre 2** : chaque lot d'apprentissage prend ses actions dans l'**ordre inverse** (étiquettes de même), mêmes clés de
graines que la sonde lue (même départ), mêmes réglages, mêmes époques : même problème, seul l'ordre des sommes change. La sonde
de l'ordre 2 est notée sur les mêmes actions que la sonde lue (groupes `sonde` du plan de notation), scores écrits fermés
(`<groupe>__sonde_o2`, poids `o2__w`, `o2__b`, `o2__q`) ; son réglage retenu et son empreinte vont dans le fichier des sondes
(`ordre2`). Aucune aire n'est écrite sur l'instance (les aires de validation interne de l'ordre 2 servent au seul choix de son
réglage, jamais écrites) ; l'écart des aires est calculé à la lecture, sur processeur (`lecture_v3`). Ni ENC, ni le plancher, ni le
nul ne sont rejoués. Une sonde de l'ordre 2 en échec (`SondeEnEchec`) : la source est « échec » pour la mesure (motif écrit) ; une
erreur d'exécution qui n'est pas une garde (`RuntimeError` de torch, mémoire de la carte) : **toute** la mesure est « non faite »
(motif écrit, tableaux partiels retirés), la marche continue et écrit ses scores ; une garde (`GardeArret`) arrête la marche comme
ailleurs. La mesure ne change aucun score, aucun état, aucune issue ni aucun seuil.
"""
from __future__ import annotations

import numpy as np

from controle_ia.gardes import GardeArret, exiger_sans_signal
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import validation_imbriquee_v1 as v1
from controle_ia.t07bbis import validation_imbriquee_v3 as v3
from controle_ia.t07bbis.commun_v1 import (AGREGATION_DE, EPOQUES, FAMILLES, N_ACTIONS_CONTROLE_CARTE, TOLERANCE_CARTE, H,
                                           grille, reglage_nom)
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


# ------------------------------------------------------------------------------- mesure de dispersion entre ordres de calcul

ORDRE_2 = "ordre inverse des actions de chaque lot d'apprentissage, sur la carte (même départ, mêmes graines, mêmes réglages)"
CHAMP_O2 = "sonde_o2"


def apprentissages_mesure(n_sources: int, n_reglages: int, n_plis_internes: int) -> int:
    """Apprentissages de la mesure (comptés par la garde de débit) : par source et par pli externe, grille × plis internes + 1."""
    return int(n_sources) * 2 * (int(n_reglages) * int(n_plis_internes) + 1)


def apprendre_recette_ordre2(ctx: Contexte, serie_nom: str, cellule: str, k: int, positifs: tuple, negatifs: tuple,
                             taches_app, taches_lues, internes) -> dict:
    """`validation_imbriquee_v1.apprendre_recette` (grille × plis internes, choix du réglage, sonde finale) dans l'ordre 2 : les
    actions de chaque lot d'apprentissage sont prises dans l'ordre inverse (étiquettes de même) ; mêmes clés de graines, mêmes
    réglages, même règle de choix. Rend {reglage, sonde, echecs_internes} ou {echec, reglage, echecs_internes}. Aucune aire n'est
    rendue ni écrite."""
    exiger_disjonction(taches_app, taches_lues, f"apprentissage {serie_nom}-ordre2/{cellule}/e{k}")
    for interne in internes:
        exiger_disjonction(interne, taches_lues, f"réglage {serie_nom}-ordre2/{cellule}/e{k}")
    regs = grille(ctx.couches, ctx.familles)
    sommes, echecs = {r["nom"]: [] for r in regs}, 0
    for j, interne in enumerate(internes):
        exiger_sans_signal(f"la mesure de l'ordre 2 {serie_nom}/{cellule}/e{k}i{j}")
        app = [t for t in taches_app if t not in set(interne)]
        a_app = v1._actions(ctx.acts, [positifs, negatifs], app)[::-1]                     # ordre 2 : ordre inverse
        a_val = v1._actions(ctx.acts, [positifs, negatifs], interne)
        y_app = np.array([1 if (s, c) == positifs else 0 for s, c, _ in a_app])
        y_val = np.array([1 if (s, c) == positifs else 0 for s, c, _ in a_val])
        t_val = [ctx.acts.tache(x) for _, _, x in a_val]
        for couche in ctx.couches:
            lot = ac.LotCarte(v1._sequences(ctx.acts, a_app, couche), ctx.appareil)
            seq_val = v1._sequences(ctx.acts, a_val, couche)
            for r in [x for x in regs if x["couche"] == couche]:
                nom = f"{serie_nom}-ordre2-{cellule}-e{k}i{j}-{r['nom']}"
                try:
                    s = v1._entrainer_chrono(ctx, lot, r, nom, y_app,
                                             f"bbis/entrainement/{serie_nom}/{cellule}/e{k}i{j}/{r['nom']}")
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
    a_app = v1._actions(ctx.acts, [positifs, negatifs], taches_app)[::-1]
    y_app = np.array([1 if (s, c) == positifs else 0 for s, c, _ in a_app])
    lot = ac.LotCarte(v1._sequences(ctx.acts, a_app, retenu["couche"]), ctx.appareil)
    try:
        sonde = v1._entrainer_chrono(ctx, lot, retenu, f"{serie_nom}-ordre2-{cellule}-e{k}", y_app,
                                     f"bbis/entrainement/{serie_nom}/{cellule}/e{k}/{retenu['nom']}")
    except ac.SondeEnEchec as e:
        return {"echec": str(e), "reglage": retenu, "echecs_internes": echecs}
    return {"reglage": retenu, "sonde": sonde, "echecs_internes": echecs}


def _retirer_mesure(sources: dict) -> None:
    for _, res in sources.values():
        for n in [n for n in res.get("tableaux", {}) if n.endswith(f"__{CHAMP_O2}") or n.startswith("o2__")]:
            del res["tableaux"][n]
        res.get("meta", {}).pop("ordre2", None)


def mesurer_dispersion(ctx: Contexte, sources: dict, plis: dict, doses) -> dict:
    """Mesure d'information du second addendum (docstring du module), jouée après le contrôle carte-processeur, avant l'écriture
    des fichiers fermés. `sources` : {(cellule, pli) : (positifs, res de `apprendre_source`)}, complétées sur place (tableaux
    `<groupe>__sonde_o2`, `o2__w`, `o2__b`, `o2__q` ; `meta["ordre2"]`). Rend le résumé écrit dans `sondes-bbis.json` (aucune
    aire)."""
    resume = {"ordre": ORDRE_2, "decide": False, "sources": {}}
    try:
        for (cellule, k) in sorted(sources):
            positifs, res = sources[(cellule, k)]
            cle = f"{cellule}/e{k}"
            if "sonde" not in res:
                resume["sources"][cle] = "sans sonde lue (source en échec) : non jouée"
                continue
            taches_lues = sorted(t for t, p in plis.items() if p == k)
            taches_app = sorted(t for t, p in plis.items() if p != k)
            o2 = apprendre_recette_ordre2(ctx, "sonde", cellule, k, ("O", positifs), ("O", H), taches_app, taches_lues,
                                          res["meta"]["plis_internes"])
            meta = {"ordre": "inverse", "reglage": o2["reglage"]["nom"] if o2.get("reglage") else None,
                    "echecs_internes": o2["echecs_internes"]}
            if "echec" in o2:
                meta["echec"] = o2["echec"]
            else:
                s = o2["sonde"]
                for groupe in plan_de_notation(positifs, doses)["sonde"]:
                    actions = v1._actions(ctx.acts, [groupe], taches_lues)
                    g = nom_groupe(groupe)
                    if list(res["tableaux"][f"{g}__cles"]) != [x for _, _, x in actions]:
                        raise GardeArret(f"mesure de l'ordre 2 {cle} : clés du groupe {g} différentes de la sonde lue : arrêt")
                    res["tableaux"][f"{g}__{CHAMP_O2}"] = ac.scores(s, v1._sequences(ctx.acts, actions, s.couche))
                res["tableaux"]["o2__w"] = s.w
                res["tableaux"]["o2__b"] = np.array([s.b])
                if s.q is not None:
                    res["tableaux"]["o2__q"] = s.q
                meta.update({"empreinte_sonde": s.empreinte(), "famille": o2["reglage"]["famille"],
                             "couche": int(o2["reglage"]["couche"]), "l2": float(o2["reglage"]["l2"])})
            res["meta"]["ordre2"] = meta
            resume["sources"][cle] = "échec (motif dans le fichier des sondes)" if "echec" in meta else "jouée"
    except RuntimeError as e:
        if isinstance(e, GardeArret):                  # une garde n'est jamais attrapée pour continuer
            raise
        _retirer_mesure(sources)
        resume = {"ordre": ORDRE_2, "decide": False, "non_faite": f"{type(e).__name__}: {e}"[:2000]}
    return resume


__all__ = list(v3.__all__) + ["EPOQUES_CONTROLE", "ORDRE_2", "CHAMP_O2", "apprentissages_mesure", "apprendre_recette_ordre2",
                              "mesurer_dispersion"]
