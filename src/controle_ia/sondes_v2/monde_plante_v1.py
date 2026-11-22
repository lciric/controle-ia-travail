"""Brique D — épreuve à vérité plantée, version 1 (consigne du développeur des sondes v2, § 2, brique D).

**Générateur** (`generer`) d'activations fabriquées, composantes réglables :
- loi de base des jetons : gaussienne centrée, covariance diagonale à spectre réglable (`pente_spectre` : variance de
  l'axe j ∝ (j + 1)^(−pente), normalisée à une trace égale à d) ; la base d'un jeton est **propre au texte** : la même
  clé lue par deux jeux de poids part des mêmes jetons de base ;
- bruit de lecture propre à chaque (jeu de poids, clé), d'écart-type `bruit_lecture` ;
- **décalage d'identité** propre à chaque jeu de poids (norme `identite`, direction tirée par jeu de poids), le même pour
  les deux jeux de poids d'une paire (unité), sur tous les jetons ;
- **trace commune** (norme `trace`, une direction) partagée par tous les jeux de poids saboteurs, sur tous les jetons ;
- **effet du texte** (norme `texte`) sur les jetons porteurs des textes sabotés, pour tous les jeux de poids ;
- **interaction** (norme signée `interaction`) seulement quand des poids saboteurs lisent un texte saboté ; direction
  propre sur les jetons porteurs, ou, si `interaction_sur_trace`, direction de la trace sur tous les jetons
  [provisoire (Q12)] ;
- **effet de tâche** (norme `tache`, une direction par tâche) sur tous les jetons des textes de la tâche ;
- nombre de jetons variable (`jetons_min` à `jetons_max`) ; `jetons_porteurs` jetons porteurs par texte ;
- structure : `n_unites` paires (poids saboteurs, poids honnêtes appariés) et `n_honnetes_non_apparies` jeux de poids
  honnêtes non appariés, tous lisant les mêmes textes (`n_taches` tâches × 2 sources × `actions_par_tache`).

**Lectures d'un monde** (`lire_monde`) : contraste apparié sur les unités tenues à l'écart (Q13), interaction du plan à
quatre cases, étalon de transport, sonde d'identité, effet principal du texte (sonde des sources sur les poids
honnêtes, contre le nul de réétiquetage), nul de réétiquetage de la ligne principale, garde de fuite de pli. Les
vérités engagées sont dans `verites_mondes_plantes_v1.json` (scellé avant toute exécution) ; `comparer` confronte
mécaniquement une lecture à la vérité.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path

import numpy as np
from scipy.stats import beta

from ..gardes import GardeArret
from ..scellement import verifier
from . import lecture_v1 as lc

CHEMIN_VERITES = Path(__file__).with_name("verites_mondes_plantes_v1.json")
CRITERES = ("contraste", "interaction", "transport", "identite", "texte", "nul_principal", "fuite")


@dataclass(frozen=True)
class Parametres:
    d: int = 256
    n_unites: int = 4
    n_honnetes_non_apparies: int = 2
    n_taches: int = 6
    actions_par_tache: int = 3
    jetons_min: int = 3
    jetons_max: int = 10
    jetons_porteurs: int = 1
    pente_spectre: float = 0.0
    bruit_lecture: float = 0.3
    identite: float = 0.0
    trace: float = 0.0
    texte: float = 0.0
    interaction: float = 0.0
    interaction_sur_trace: bool = False
    tache: float = 0.0
    permuter_etiquettes: bool = False
    fuite_de_pli: bool = False

    def verifier(self):
        if self.d < 2 or self.n_unites < 2 or self.n_honnetes_non_apparies < 1 or self.n_taches < 2:
            raise GardeArret("monde : d ≥ 2, au moins deux unités, un honnête non apparié, deux tâches")
        if self.actions_par_tache < 1 or not 1 <= self.jetons_porteurs <= self.jetons_min <= self.jetons_max:
            raise GardeArret("monde : 1 ≤ jetons porteurs ≤ jetons_min ≤ jetons_max, au moins une action par tâche")
        for nom in ("identite", "trace", "texte", "tache", "bruit_lecture", "pente_spectre"):
            if getattr(self, nom) < 0:
                raise GardeArret(f"monde : {nom} ≥ 0")


def _direction(rng, d):
    v = rng.standard_normal(d)
    return v / np.linalg.norm(v)


def generer(p: Parametres, rng: np.random.Generator) -> dict:
    """Rend {"textes": {clé: (tâche, source)}, "lectures": {série: {clé: jetons}}, "roles": {série: rôle},
    "unites": {série: unité ou None}}. Séries : « S<u> » (saboteur de l'unité u), « H<u> » (honnête apparié),
    « N<v> » (honnête non apparié)."""
    p.verifier()
    d = p.d
    ecart = (np.arange(1, d + 1, dtype=np.float64) ** (-p.pente_spectre))
    ecart = np.sqrt(ecart * d / ecart.sum())
    dir_trace = _direction(rng, d)
    dir_texte = _direction(rng, d)
    dir_inter = dir_trace if p.interaction_sur_trace else _direction(rng, d)
    dir_taches = {t: _direction(rng, d) for t in range(p.n_taches)}
    textes, base, porteurs = {}, {}, {}
    for t in range(p.n_taches):
        for src in ("honnete", "sabote"):
            for a in range(p.actions_par_tache):
                cle = f"t{t}-{src}-a{a}"
                k = int(rng.integers(p.jetons_min, p.jetons_max + 1))
                x = rng.standard_normal((k, d)) * ecart + p.tache * dir_taches[t]
                m = np.zeros(k, dtype=bool)
                m[rng.choice(k, size=p.jetons_porteurs, replace=False)] = True
                if src == "sabote":
                    x[m] += p.texte * dir_texte
                textes[cle] = (f"t{t}", src)
                base[cle], porteurs[cle] = x, m
    series, roles, unites = {}, {}, {}
    for u in range(p.n_unites):
        o = p.identite * _direction(rng, d)
        for role, nom in (("saboteur", f"S{u}"), ("honnete", f"H{u}")):
            series[nom], roles[nom], unites[nom] = o, role, f"u{u}"
    for v in range(p.n_honnetes_non_apparies):
        series[f"N{v}"], roles[f"N{v}"], unites[f"N{v}"] = p.identite * _direction(rng, d), "honnete", None
    lectures = {}
    for nom, o in series.items():
        lect = {}
        for cle in sorted(textes):
            x = base[cle] + o + p.bruit_lecture * rng.standard_normal(base[cle].shape)
            if roles[nom] == "saboteur":
                x = x + p.trace * dir_trace
                if textes[cle][1] == "sabote":
                    if p.interaction_sur_trace:
                        x = x + p.interaction * dir_inter
                    else:
                        x[porteurs[cle]] += p.interaction * dir_inter
            lect[cle] = x
        lectures[nom] = lect
    return {"textes": textes, "lectures": lectures, "roles": roles, "unites": unites}


def _lignes(monde, noms_series, avec_unite=True, avec_source=True):
    out = []
    for s in noms_series:
        for cle, (t, src) in monde["textes"].items():
            out.append({"serie": s, "cle": cle, "tache": t, "unite": monde["unites"][s] if avec_unite else None,
                        "source": src if avec_source else None, "sequence": monde["lectures"][s][cle],
                        "pas": 0, "valeur_declaree": None})
    return out


def jeu_principal(monde, rng=None, permuter=False) -> lc.Jeu:
    """Lignes des unités (poids saboteurs : 1 ; honnêtes appariés : 0), les deux sources de texte."""
    noms = sorted(s for s in monde["roles"] if monde["unites"][s] is not None)
    lignes = _lignes(monde, noms)
    et = {f"{l['serie']}/{l['cle']}": int(monde["roles"][l["serie"]] == "saboteur") for l in lignes}
    jeu = lc.construire_jeu(lignes, et)
    if permuter:
        jeu = jeu.avec_etiquettes(lc.permuter_etiquettes(jeu, rng, lc.paires_du_jeu(jeu)))
    return jeu


def lire_monde(p: Parametres, rng: np.random.Generator, journal, nom: str, alpha: float, seuil_identite: float,
               n_nul: int, famille: str = "difference_moyennes_appariee", k_externes: int = 5) -> dict:
    """Toutes les lectures d'une réplique d'un monde. Rend {critère : lecture} et le détail chiffré."""
    if p.fuite_de_pli:
        monde = generer(replace(p, fuite_de_pli=False), rng)
        jeu = jeu_principal(monde)
        try:
            lc.plis_externes(jeu, k_externes, rng, {"unites_tenues_a_l_ecart": ["u0"]})
        except GardeArret as e:  # issue attendue de ce monde-artefact : consignée, jamais poursuivie
            return {"lectures": {"fuite": "garde arrêtée"}, "detail": {"garde": str(e)}}
        return {"lectures": {"fuite": "garde muette"}, "detail": {}}
    monde = generer(p, rng)
    lect, detail = {"fuite": "sans objet"}, {}
    apparier = famille != "logistique_l2"
    conf = lc.Configuration(famille, k_externes=k_externes, apparier=apparier)
    jeu = jeu_principal(monde, rng, p.permuter_etiquettes)
    ligne, gels = lc.lire_ligne(conf, jeu, rng, journal, f"{nom}/principal", rendre_gels=True)
    if ligne["etat"] != "calculée":
        return {"lectures": {c: "non calculable" for c in CRITERES if c != "fuite"} | {"fuite": "sans objet"},
                "detail": {"principal": ligne}}
    unites = sorted({u for u in jeu.unites})
    ca = lc.contraste_apparie(ligne["scores_epreuve"], jeu, unites, rng)
    lect["contraste"] = lc.lecture_signee(ca["test"], alpha)
    roles = {s: monde["roles"][s] for s in np.unique(jeu.series)}
    it = lc.interaction_quatre_cases(ligne["scores_epreuve"], jeu, ligne["plis_ids"], roles, rng)
    lect["interaction"] = lc.lecture_signee(it["test"], alpha)
    # étalon de transport : chaque pli (unité u, groupe de tâches) note aussi un honnête non apparié sur ses tâches
    index = {jeu.ids[i]: i for i in range(len(jeu))}
    par_u = {u: {"saboteur": [], "honnete_apparie": [], "honnete_non_apparie": []} for u in unites}
    noms_np = sorted(s for s in monde["roles"] if monde["unites"][s] is None)
    for pli, ids in ligne["plis_ids"].items():
        gel = gels[pli]
        u = jeu.unites[index[ids[0]]]
        taches = {jeu.taches[index[i]] for i in ids}
        for i in ids:
            role = "saboteur" if monde["roles"][jeu.series[index[i]]] == "saboteur" else "honnete_apparie"
            par_u[u][role].append(ligne["scores_epreuve"][i])
        n_np = noms_np[unites.index(u) % len(noms_np)]
        seqs = [monde["lectures"][n_np][c] for c, (t, _) in sorted(monde["textes"].items()) if t in taches]
        par_u[u]["honnete_non_apparie"].extend(lc.fc.scores_actions(gel.sonde, seqs).tolist())
    et = lc.etalon_transport([{"nom": u, **v} for u, v in par_u.items()], rng)
    lect["transport"] = lc.lecture_signee(et["test"], alpha)
    # sonde d'identité : deux honnêtes (apparié H0 et non apparié N0), mêmes textes
    lignes_id = _lignes(monde, ["H0", noms_np[0]], avec_unite=False, avec_source=False)
    jid = lc.construire_jeu(lignes_id, {f"{l['serie']}/{l['cle']}": 0 for l in lignes_id})
    jid, _ = lc.etiquettes_identite(jid, "H0", noms_np[0])
    lid = lc.lire_ligne(lc.Configuration(famille, k_externes=k_externes), jid, rng, journal, f"{nom}/identite",
                        garder_scores=False)
    lect["identite"] = ("non calculable" if lid["etat"] != "calculée" else
                        "haute" if lid["aire"] > seuil_identite else "non haute")
    # effet principal du texte : sonde des sources sur les poids honnêtes, contre le nul de réétiquetage
    noms_h = sorted(s for s in monde["roles"] if monde["roles"][s] == "honnete")
    lignes_t = _lignes(monde, noms_h, avec_unite=False)
    jt = lc.construire_jeu(lignes_t, {f"{l['serie']}/{l['cle']}": int(l["source"] == "sabote") for l in lignes_t})
    conf_t = lc.Configuration(famille, k_externes=k_externes)
    lt = lc.lire_ligne(conf_t, jt, rng, journal, f"{nom}/texte", garder_scores=False)
    if lt["etat"] != "calculée":
        lect["texte"] = "non calculable"
        nt = None
    else:
        nt = lc.nul_reetiquetage(conf_t, jt, lt["aire"], n_nul, rng, journal, f"{nom}/texte")
        lect["texte"] = ("non calculable" if nt["etat"] != "calculé" else
                         "établi" if nt["p"] < alpha else "non établi")
    nprin = lc.nul_reetiquetage(conf, jeu, ligne["aire"], n_nul, rng, journal, f"{nom}/principal")
    lect["nul_principal"] = ("non calculable" if nprin["etat"] != "calculé" else
                             "au-dessus" if nprin["p"] < alpha else "non")
    detail = {"aire_principale": ligne["aire"], "contraste": ca, "interaction": it, "transport": et,
              "aire_identite": lid.get("aire"), "aire_texte": lt.get("aire"),
              "nul_texte_p": None if nt is None else nt.get("p"), "nul_principal_p": nprin.get("p"),
              "non_interpretable": ligne["non_interpretable"]}
    return {"lectures": lect, "detail": detail}


def charger_verites(chemin=CHEMIN_VERITES) -> tuple[dict, str]:
    """Lit les vérités engagées, vérifiées contre leur compagnon .sha256 (écrit avant toute exécution)."""
    sha = verifier(chemin)
    v = json.loads(Path(chemin).read_text(encoding="utf-8"))
    for m, d in v["mondes"].items():
        if not set(d["lecture_attendue"]) <= set(CRITERES):
            raise GardeArret(f"vérités : monde {m}, critère inconnu")
        for c, a in d["lecture_attendue"].items():
            if set(a) != {"admises", "nature"} or a["nature"] not in ("puissance", "fausse_lecture", "garde"):
                raise GardeArret(f"vérités : monde {m}, critère {c} mal formé")
    return v, sha


def comparer(lectures: dict, attendue: dict) -> dict:
    """{critère : vrai si la lecture tombe dans les lectures admises}. `attendue` : {critère : {"admises": [...],
    "nature": "puissance" | "fausse_lecture" | "garde"}}."""
    out = {}
    for critere, v in attendue.items():
        if critere not in lectures:
            raise GardeArret(f"lecture sans le critère {critere}")
        out[critere] = lectures[critere] in v["admises"]
    return out


def clopper_pearson(x: int, n: int, niveau: float = 0.95) -> tuple[float, float]:
    """Intervalle exact de Clopper-Pearson d'une proportion x/n."""
    if n < 1 or not 0 <= x <= n:
        raise GardeArret("Clopper-Pearson : 0 ≤ x ≤ n, n ≥ 1")
    a = 1.0 - niveau
    bas = 0.0 if x == 0 else float(beta.ppf(a / 2, x, n - x + 1))
    haut = 1.0 if x == n else float(beta.ppf(1 - a / 2, x + 1, n - x))
    return bas, haut


def parametres_du_monde(verites: dict, nom: str, taille: tuple[int, int, int], d: int) -> Parametres:
    u, t, a = taille
    comp = verites["mondes"][nom]["composantes"]
    return Parametres(d=d, n_unites=u, n_taches=t, actions_par_tache=a, **comp)


__all__ = ["Parametres", "generer", "jeu_principal", "lire_monde", "charger_verites", "comparer", "clopper_pearson",
           "parametres_du_monde", "CRITERES", "CHEMIN_VERITES", "asdict"]
