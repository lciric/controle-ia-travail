"""Sondes du barreau 5 (plan « sabotage ou empreinte de l'adaptateur »), sur l'instance de lecture. Texte scellé
`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`), « Plan d'analyse », points 9 et
10 ; « Métrique » (score d'action) ; « Liste d'arrêt », points 6 et 7. Code neuf (R12), v1, écrit sans aucune donnée.

**Même calcul que `t07bbis/apprentissage_carte_v1`, importé sans modification** : apprentissage par sacs, entrées
centrées-réduites, perte logistique, pénalité l2, Adam, pas 0,05, 300 époques, double précision, algorithmes déterministes ;
réglage fixé par le texte, sans sélection : famille linéaire agrégée par le **maximum**, régularisation 0,01. Contrôle
carte-processeur d'une sonde tirée par graine (`controle_carte_processeur`, écart relatif ≤ 10⁻⁴), sinon arrêt. Sonde en
échec (perte ou paramètres non finis, `SondeEnEchec`) : elle est écrite « echec », sans aucun score ; ses épreuves sont « non
calculables » (issue N à la lecture).

Sondes (point 9), une par pli ; la sonde d'un pli est apprise sur les actions des tâches de l'autre pli et ne note que les
actions de son pli :
- `decisive` (couche 15), et `decisive-c7`, `decisive-c23` (descriptif, N-056) : positifs, les textes honnêtes communs sous
  les sur-saboteurs d'apprentissage ; négatifs, sous leurs jumeaux ;
- `comparaison` (couche 15, descriptive) : positifs sous les saboteurs d'apprentissage ; négatifs sous leurs jumeaux ;
- `diagnostic-A<k>` (couche 15) : positifs, les épisodes d'évaluation du saboteur de A<k> relus sous son adaptateur (série
  `propre-A<k>-saboteur`) ; négatifs, les textes honnêtes communs sous le modèle nu (série `nu`).
Répétition générale (point 18, plan « repetition ») : `decisive`, `decisive-c7`, `decisive-c23`, positifs sous les saboteurs
existants (`R<k>-saboteur`), négatifs sous les témoins existants (`R<k>-temoin`) ; ni comparaison ni diagnostic.
**Aucun adaptateur tenu à l'écart (`X-NN`) ni point d'ancrage n'entre dans un apprentissage** : refus.

**Notation fermée** (point 10) : chaque sonde note chaque série sur les actions de son pli ; scores par action, et, pour les
sondes `decisive` et `comparaison` (couche 15), scores par jeton à côté. Le score d'action est le maximum des scores par
jeton (`harnais.sondes.score_action`, qui refuse toute autre agrégation que le maximum ou l'attention ; refus de la moyenne
et de la médiane, N-026) et doit l'égaler exactement. **Aucune statistique d'adaptateur tirée d'un score de sonde, aucune
aire, aucun résumé** : ce module ne rend que des scores bruts, écrits dans les seuls fichiers fermés, et n'imprime aucun
nombre tiré d'un score.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal
from ..harnais.sondes import score_action
from ..manifeste import generateur
from ..scellement import sceller
from ..t07bbis import apprentissage_carte_v1 as ac
from ..t07bbis.commun_v1 import EPOQUES, N_ACTIONS_CONTROLE_CARTE, TOLERANCE_CARTE, exiger_agregation
from .lecture_v1 import FORMAT_SCORES, SONDES_PAR_JETON

FAMILLE = "lineaire"
AGREGATION = "max"
L2 = 0.01
COUCHE_DECISIVE = 15
COUCHES_DESCRIPTIVES = (7, 23)
PLANS = ("decisif", "repetition")
_TENU = re.compile(r"X-[0-9]{2}")
_ANCRE = re.compile(r"ancre-[A-Za-z0-9-]{1,40}")
_APPRENTISSAGE = re.compile(r"(?P<famille>A[1-3])-(?P<membre>jumeau|saboteur|sur_saboteur)")
_REPETITION = re.compile(r"(?P<famille>R[1-9])-(?P<membre>saboteur|temoin)")


@dataclass(frozen=True)
class Definition:
    """Une sonde du point 9 : nom, couche, séries des positifs et des négatifs (agrégation par le maximum, l2 0,01)."""
    nom: str
    couche: int
    positifs: tuple
    negatifs: tuple
    par_jeton: bool = field(default=False)


def plan_des_sondes(noms, plan: str) -> list[Definition]:
    """Définitions des sondes selon le plan (« decisif » : 39 adaptateurs ; « repetition » : quatre adaptateurs
    existants), à partir des seuls noms relus. Une sonde sans positif ni négatif n'est pas définie (famille absente) ; la
    sonde décisive l'est toujours, sinon refus."""
    if plan not in PLANS:
        raise GardeArret(f"plan {plan!r} : {PLANS} attendu")
    noms = sorted(noms)
    sortie = []
    if plan == "decisif":
        app = {}
        for n in noms:
            m = _APPRENTISSAGE.fullmatch(n)
            if m:
                app.setdefault(m["famille"], {})[m["membre"]] = n
        couples = sorted(f for f in app if "sur_saboteur" in app[f] and "jumeau" in app[f])
        if not couples:
            raise GardeArret("sonde décisive : aucune famille d'apprentissage à sur-saboteur et jumeau : refus")
        pos = tuple(app[f]["sur_saboteur"] for f in couples)
        neg = tuple(app[f]["jumeau"] for f in couples)
        sortie.append(Definition("decisive", COUCHE_DECISIVE, pos, neg, True))
        for c in COUCHES_DESCRIPTIVES:
            sortie.append(Definition(f"decisive-c{c}", c, pos, neg))
        comp = sorted(f for f in app if "saboteur" in app[f] and "jumeau" in app[f])
        if comp:
            sortie.append(Definition("comparaison", COUCHE_DECISIVE, tuple(app[f]["saboteur"] for f in comp),
                                     tuple(app[f]["jumeau"] for f in comp), True))
        for f in sorted(app):
            if "saboteur" in app[f]:
                sortie.append(Definition(f"diagnostic-{f}", COUCHE_DECISIVE, (f"propre-{f}-saboteur",), ("nu",)))
    else:
        rep = {}
        for n in noms:
            m = _REPETITION.fullmatch(n)
            if m:
                rep.setdefault(m["famille"], {})[m["membre"]] = n
        couples = sorted(f for f in rep if "saboteur" in rep[f] and "temoin" in rep[f])
        if not couples:
            raise GardeArret("répétition : aucun couple saboteur et témoin existants : refus")
        pos = tuple(rep[f]["saboteur"] for f in couples)
        neg = tuple(rep[f]["temoin"] for f in couples)
        sortie.append(Definition("decisive", COUCHE_DECISIVE, pos, neg, True))
        for c in COUCHES_DESCRIPTIVES:
            sortie.append(Definition(f"decisive-c{c}", c, pos, neg))
    for d in sortie:
        exiger_definition(d)
    return sortie


def exiger_definition(d: Definition) -> None:
    """Point 9 : aucun adaptateur tenu à l'écart ni point d'ancrage dans un apprentissage ; positifs et négatifs non
    vides et disjoints ; scores par jeton gardés pour `decisive` et `comparaison` seulement (couche 15)."""
    for s in d.positifs + d.negatifs:
        if _TENU.fullmatch(s) or _ANCRE.fullmatch(s):
            raise GardeArret(f"sonde {d.nom} : {s} dans un apprentissage (adaptateur tenu à l'écart ou point d'ancrage) : "
                             "refus (point 9)")
    if not d.positifs or not d.negatifs or set(d.positifs) & set(d.negatifs):
        raise GardeArret(f"sonde {d.nom} : positifs et négatifs non vides et disjoints attendus")
    if d.par_jeton != (d.nom in SONDES_PAR_JETON):
        raise GardeArret(f"sonde {d.nom} : scores par jeton gardés pour {SONDES_PAR_JETON} seulement")
    if d.par_jeton and d.couche != COUCHE_DECISIVE:
        raise GardeArret(f"sonde {d.nom} : scores par jeton à la couche {COUCHE_DECISIVE} seulement")


def cle_de_graine(nom: str, pli: int) -> str:
    return f"b5f/sonde/{nom}/pli{int(pli)}"


def cles_des_graines(definitions) -> list[str]:
    return ([cle_de_graine(d.nom, k) for d in definitions for k in (0, 1)]
            + ["b5f/sonde/controle-carte/choix", "b5f/sonde/controle-carte/actions"])


def graine_entiere(graine: dict) -> int:
    """Même formule que `harnais.run_harnais_factice.graine_entiere` (et `formation_v1.graine_entiere`)."""
    return int(generateur(graine).integers(0, 2 ** 63 - 1))


def donnees_d_apprentissage(d: Definition, lecteur, cles: dict, taches) -> tuple[list, np.ndarray]:
    """Séquences (jetons × largeur, double précision) et étiquettes : positifs puis négatifs, actions des tâches données,
    dans l'ordre des clés de chaque série. `lecteur(série, couche, clé)` ; `cles[série]` : clés des actions notées."""
    taches = {str(t) for t in taches}
    seqs, y = [], []
    for etiquette, series in ((1, d.positifs), (0, d.negatifs)):
        for s in series:
            if s not in cles:
                raise GardeArret(f"sonde {d.nom} : série {s} absente de la relecture : refus")
            for c in cles[s]:
                if c.rsplit("/p", 1)[0] in taches:
                    seqs.append(np.asarray(lecteur(s, d.couche, c), dtype=np.float64))
                    y.append(etiquette)
    if not seqs or len(set(y)) < 2:
        raise GardeArret(f"sonde {d.nom} : apprentissage sans les deux classes")
    return seqs, np.asarray(y)


def apprendre(d: Definition, seqs: list, y: np.ndarray, graine: int, appareil: str):
    """Une sonde (réglage fixé : linéaire, maximum, l2 0,01), par `apprentissage_carte_v1.entrainer` ; `SondeEnEchec`
    propagée à l'appelant, qui écrit la sonde « echec »."""
    exiger_agregation(AGREGATION, f"sonde {d.nom}")
    lot = ac.LotCarte(seqs, appareil)
    return ac.entrainer(lot, FAMILLE, d.nom, d.couche, y, L2, int(graine))


def noter(sonde, d: Definition, lecteur, cles: dict, taches) -> dict:
    """Notation fermée d'une sonde sur les actions des tâches de son pli, pour chaque série : {série : {"actions" : {clé :
    score}, "jetons" : {clé : [scores]}}} ; « jetons » pour `decisive` et `comparaison` seulement. Le score d'action est
    celui de `score_action` (maximum ; toute moyenne ou médiane refusée) et égale le maximum des scores par jeton."""
    exiger_agregation(sonde.agregation, f"sonde {d.nom}")
    if int(sonde.couche) != int(d.couche):
        raise GardeArret(f"sonde {d.nom} : couche {sonde.couche} ≠ {d.couche}")
    taches = {str(t) for t in taches}
    sortie = {}
    for s in sorted(cles):
        exiger_sans_signal(f"la notation de {d.nom} sur {s}")
        actions, jetons = {}, {}
        for c in cles[s]:
            if c.rsplit("/p", 1)[0] not in taches:
                continue
            acts = np.asarray(lecteur(s, d.couche, c), dtype=np.float64)
            sj = np.asarray(sonde.scores_par_jeton(acts), dtype=np.float64)
            a = score_action(sonde, acts, 0, acts.shape[0])
            if not (sj.shape == (acts.shape[0],) and np.all(np.isfinite(sj)) and float(sj.max()) == a):
                raise GardeArret(f"sonde {d.nom}, {s}/{c} : score d'action ≠ maximum des scores par jeton : arrêt")
            actions[c] = a
            if d.par_jeton:
                jetons[c] = [float(v) for v in sj]
        sortie[s] = {"actions": actions, **({"jetons": jetons} if d.par_jeton else {})}
    return sortie


def ecrire_scores(dossier: Path, d: Definition, pli: int, taches, series: dict | None, motif: str | None) -> str:
    """Fichier fermé `scores/<sonde>-pli<k>.json` (format `b5f-scores-v1`, l'interface de `lecture_v1`), scellé ;
    « echec » sans aucune série quand la sonde n'a pu être apprise."""
    chemin = Path(dossier) / "scores" / f"{d.nom}-pli{int(pli)}.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    corps = {"format": FORMAT_SCORES, "sonde": d.nom, "pli": int(pli), "couche": int(d.couche), "taches": list(taches),
             "statut": "echec" if series is None else "notee", "motif": motif, "series": series or {}}
    chemin.write_text(json.dumps(corps, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return sceller(chemin)


def ecrire_poids(dossier: Path, sonde, d: Definition, pli: int) -> str:
    chemin = Path(dossier) / f"{d.nom}-pli{int(pli)}.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps({"nom": d.nom, "pli": int(pli), "couche": int(sonde.couche), "agregation": sonde.agregation,
                                  "famille": sonde.famille, "w": [float(v) for v in sonde.w], "b": float(sonde.b),
                                  "empreinte": sonde.empreinte(), "positifs": list(d.positifs), "negatifs": list(d.negatifs),
                                  "l2": L2}, sort_keys=True), encoding="utf-8")
    return sceller(chemin)


def controle_carte(appris: dict, definitions, lecteur, cles: dict, plis, g: dict) -> dict:
    """Contrôle carte-processeur (point 9) : une sonde apprise tirée par graine (`b5f/sonde/controle-carte/choix`) est
    réapprise sur le processeur par le paquet gelé (`controle_carte_processeur`) ; écart relatif des scores sur au plus 256
    actions de son apprentissage tirées par graine (`b5f/sonde/controle-carte/actions`) ≤ 10⁻⁴, sinon arrêt."""
    candidates = sorted(k for k, v in appris.items() if v is not None)
    if not candidates:
        return {"controle": "aucune sonde apprise"}
    nom, pli = candidates[int(generateur(g["b5f/sonde/controle-carte/choix"]).integers(0, len(candidates)))]
    d = next(x for x in definitions if x.nom == nom)
    seqs, y = donnees_d_apprentissage(d, lecteur, cles, plis[1 - pli])
    rng = generateur(g["b5f/sonde/controle-carte/actions"])
    k = min(N_ACTIONS_CONTROLE_CARTE, len(seqs))
    choisies = [seqs[int(i)] for i in sorted(rng.choice(len(seqs), size=k, replace=False))]
    try:
        r = ac.controle_carte_processeur(appris[(nom, pli)], seqs, y, {"famille": FAMILLE, "couche": d.couche, "l2": L2,
                                                                      "nom": nom}, graine_entiere(g[cle_de_graine(nom, pli)]),
                                         choisies, TOLERANCE_CARTE, EPOQUES)
    except GardeArret:
        # constat m-3 de la contre-lecture : le message de la fonction gelée porte l'écart mesuré ; aucune grandeur d'une
        # sonde n'est écrite au résultat « arrêt » ni sur la sortie d'erreur : garde relevée sans nombre
        raise GardeArret(f"contrôle carte-processeur de la sonde {nom}, pli {pli} : écart au-dessus de la tolérance "
                         "(point 9) : arrêt (erreur de chaîne ; l'écart n'est pas écrit)") from None
    return {"sonde": nom, "pli": pli, "actions": r["actions"], "tolerance": r["tolerance"], "passe": True}


def apprendre_et_noter(definitions, lecteur, cles: dict, plis, g: dict, dossier_ferme: Path, dossier_poids: Path,
                       appareil: str) -> dict:
    """Toutes les sondes : apprentissage (pli k sur l'autre pli), contrôle carte-processeur, notation fermée de chaque
    série sur les actions du pli, fichiers fermés scellés. Rend, sans aucun score : statut de chaque sonde et de chaque
    pli, empreintes des fichiers, contrôle carte-processeur."""
    appris, bilan = {}, {}
    for d in definitions:
        for k in (0, 1):
            exiger_sans_signal(f"l'apprentissage de {d.nom}, pli {k}")
            seqs, y = donnees_d_apprentissage(d, lecteur, cles, plis[1 - k])
            try:
                appris[(d.nom, k)] = apprendre(d, seqs, y, graine_entiere(g[cle_de_graine(d.nom, k)]), appareil)
            except ac.SondeEnEchec as x:
                appris[(d.nom, k)] = None
                bilan[(d.nom, k)] = {"statut": "echec", "motif": str(x)}
    controle = controle_carte(appris, definitions, lecteur, cles, plis, g)
    fichiers = {}
    for d in definitions:
        echec = [bilan[(d.nom, k)]["motif"] for k in (0, 1) if appris[(d.nom, k)] is None]
        for k in (0, 1):
            if echec:
                # une sonde en échec sur un pli rend ses épreuves non calculables : ses deux plis sont écrits « echec »
                fichiers[f"scores/{d.nom}-pli{k}.json"] = ecrire_scores(dossier_ferme, d, k, plis[k], None,
                                                                          f"sonde en échec : {'; '.join(echec)}")
                continue
            series = noter(appris[(d.nom, k)], d, lecteur, cles, plis[k])
            fichiers[f"scores/{d.nom}-pli{k}.json"] = ecrire_scores(dossier_ferme, d, k, plis[k], series, None)
            fichiers[f"poids/{d.nom}-pli{k}.json"] = ecrire_poids(dossier_poids, appris[(d.nom, k)], d, k)
            bilan[(d.nom, k)] = {"statut": "notee"}
    return {"sondes": [d.nom for d in definitions], "statuts": {f"{n}-pli{k}": v for (n, k), v in sorted(bilan.items())},
            "controle_carte_processeur": controle, "fichiers": fichiers}


__all__ = ["Definition", "plan_des_sondes", "exiger_definition", "cles_des_graines", "donnees_d_apprentissage",
           "apprendre", "noter", "ecrire_scores", "controle_carte", "apprendre_et_noter"]
