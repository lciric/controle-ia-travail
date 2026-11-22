"""Brique D — épreuve à vérité plantée, version 2 (consigne du développeur, brique D, et son erratum 1, § 6, qui prime).
Remplace `monde_plante_v1` (jamais livré) ; les vérités engagées sont dans `verites_mondes_plantes_v2.json`, scellé et
committé avant toute exécution (le fichier v1 reste archivé tel quel).

**Générateur** (`generer`). Unité : l'écart type d'un jeton le long d'une direction (jetons de base de loi normale
réduite ; `pente_spectre` > 0 rend la loi anisotrope, trace conservée). Les jetons de base d'une action sont communs à
toutes les séries qui lisent le même texte ; bruit de lecture indépendant par série (`bruit_lecture`, défaut 0,05).
Séries : le modèle nu `N`, et `n_paires` paires (`S<p>` saboteur, `J<p>` jumeau).
- décalage d'identité d'une paire (le même pour S_p et J_p) : composante le long de la direction de la trace,
  d'écart type `sigma_I` (défaut 1), plus une composante isotrope de norme attendue `identite_isotrope` (défaut 3) ;
- écart propre à chaque paire : S_p diffère de J_p d'un vecteur isotrope de norme `eta` (défaut 1), présent partout ;
- trace commune : vecteur de norme `tau` le long de la direction de la trace, ajouté à tous les saboteurs (« trace
  faible » τ = 0,5 σ_I √2, « trace forte » τ = 4 σ_I √2) ;
- écart d'intensité : tous les adaptateurs décalés le long d'une direction commune de norme `intensite` × σ_I √2, les
  saboteurs de 1,2 fois cette norme [lecture du développeur, provisoire (E-3)] ;
- effet du texte (`texte`) sur les jetons porteurs des textes du saboteur, pour toutes les séries ;
- interaction (`interaction`, signée) seulement quand un saboteur lit un texte du saboteur : direction propre sur les
  jetons porteurs, ou direction de la trace sur tous les jetons si `interaction_sur_trace` [Q12, provisoire] ;
- effet de tâche (`tache`) ; nombre de jetons variable ;
- décalage de chemin (`ecart_chemin`, en écarts types intra-case) : ajouté aux scores des deux cases d'origine du rejeu
  croisé — (adaptateur, textes du saboteur) et (nu, textes honnêtes) — [lecture du développeur, provisoire (E-4)].

**Lectures** (`lire_monde`) : contraste apparié (sonde du contraste principal, unités tenues à l'écart) ; rejeu croisé
(scores des sondes gelées de chaque pli sur ses tâches tenues à l'écart, lues sous le saboteur et sous le nu) : brute,
corrigée par le contrôle du chemin, et sans contrôle du chemin ; étalon de transport et son contrôle d'intensité ;
sonde d'identité ; effet principal du texte ; nul de réétiquetage de la ligne principale ; garde de fuite de pli.
"""
from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path

import numpy as np

from scipy.stats import beta

from ..gardes import GardeArret
from ..scellement import verifier
from . import formes_closes_v1 as fc
from . import lecture_v1 as lc
from . import statistiques_v1 as st

CHEMIN_VERITES = Path(__file__).with_name("verites_mondes_plantes_v2.json")
CRITERES = ("contraste", "interaction", "interaction_brute", "interaction_sans_controle", "transport",
            "transport_controle", "identite", "texte", "nul_principal", "fuite")
NATURES = ("puissance", "fausse_lecture", "garde", "description")


@dataclass(frozen=True)
class Parametres:
    d: int = 256
    n_paires: int = 8
    n_taches: int = 8
    actions_par_tache: int = 3
    jetons_min: int = 3
    jetons_max: int = 10
    jetons_porteurs: int = 1
    pente_spectre: float = 0.0
    bruit_lecture: float = 0.05
    sigma_I: float = 1.0
    identite_isotrope: float = 3.0
    eta: float = 1.0
    tau: float = 0.0
    intensite: float = 0.0
    texte: float = 0.0
    interaction: float = 0.0
    interaction_sur_trace: bool = False
    tache: float = 0.0
    ecart_chemin: float = 0.0
    permuter_etiquettes: bool = False
    fuite_de_pli: bool = False

    def verifier(self):
        if self.d < 2 or self.n_paires < 2 or self.n_taches < 2 or self.actions_par_tache < 1:
            raise GardeArret("monde : d ≥ 2, au moins deux paires, deux tâches, une action par tâche")
        if not 1 <= self.jetons_porteurs <= self.jetons_min <= self.jetons_max:
            raise GardeArret("monde : 1 ≤ jetons porteurs ≤ jetons_min ≤ jetons_max")
        for nom in ("sigma_I", "identite_isotrope", "eta", "tau", "intensite", "texte", "tache", "bruit_lecture",
                    "pente_spectre", "ecart_chemin"):
            if getattr(self, nom) < 0:
                raise GardeArret(f"monde : {nom} ≥ 0")


def _direction(rng, d):
    v = rng.standard_normal(d)
    return v / np.linalg.norm(v)


def generer(p: Parametres, rng: np.random.Generator) -> dict:
    """{"textes": {clé: (tâche, source)}, "lectures": {série: {clé: jetons}}, "roles": {série: « saboteur » |
    « jumeau » | « nu »}, "paires": [(S_p, J_p)]}. Sources : « saboteur » (textes du saboteur) et « honnete »."""
    p.verifier()
    d = p.d
    ecart = np.arange(1, d + 1, dtype=np.float64) ** (-p.pente_spectre)
    ecart = np.sqrt(ecart * d / ecart.sum())
    t_dir, txt_dir, u_dir = _direction(rng, d), _direction(rng, d), _direction(rng, d)
    i_dir = t_dir if p.interaction_sur_trace else _direction(rng, d)
    dir_taches = {t: _direction(rng, d) for t in range(p.n_taches)}
    textes, base, porteurs = {}, {}, {}
    for t in range(p.n_taches):
        for src in ("honnete", "saboteur"):
            for a in range(p.actions_par_tache):
                cle = f"t{t}-{src}-a{a}"
                k = int(rng.integers(p.jetons_min, p.jetons_max + 1))
                x = rng.standard_normal((k, d)) * ecart + p.tache * dir_taches[t]
                m = np.zeros(k, dtype=bool)
                m[rng.choice(k, size=p.jetons_porteurs, replace=False)] = True
                if src == "saboteur":
                    x[m] += p.texte * txt_dir
                textes[cle], base[cle], porteurs[cle] = (f"t{t}", src), x, m
    m_int = p.intensite * p.sigma_I * math.sqrt(2.0)
    decalages, roles, paires = {"N": np.zeros(d)}, {"N": "nu"}, []
    for q in range(p.n_paires):
        o = p.sigma_I * rng.standard_normal() * t_dir + p.identite_isotrope * rng.standard_normal(d) / math.sqrt(d)
        decalages[f"J{q}"] = o + m_int * u_dir
        decalages[f"S{q}"] = o + p.eta * _direction(rng, d) + p.tau * t_dir + 1.2 * m_int * u_dir
        roles[f"J{q}"], roles[f"S{q}"] = "jumeau", "saboteur"
        paires.append((f"S{q}", f"J{q}"))
    lectures = {}
    for nom in sorted(decalages):
        lect = {}
        for cle in sorted(textes):
            x = base[cle] + decalages[nom] + p.bruit_lecture * rng.standard_normal(base[cle].shape)
            if roles[nom] == "saboteur" and textes[cle][1] == "saboteur":
                if p.interaction_sur_trace:
                    x = x + p.interaction * i_dir
                else:
                    x[porteurs[cle]] += p.interaction * i_dir
            lect[cle] = x
        lectures[nom] = lect
    return {"textes": textes, "lectures": lectures, "roles": roles, "paires": paires}


def _lignes(monde, series, unite=True, source=True):
    out = []
    for s in series:
        u = f"u{s[1:]}" if unite and s != "N" else None
        for cle, (t, src) in monde["textes"].items():
            out.append({"serie": s, "cle": cle, "tache": t, "unite": u, "source": src if source else None,
                        "sequence": monde["lectures"][s][cle], "pas": 0, "valeur_declaree": None})
    return out


def jeu_principal(monde, rng=None, permuter=False) -> lc.Jeu:
    """Saboteurs (1) et jumeaux (0), les deux sources ; unité = la paire."""
    series = [x for pq in monde["paires"] for x in pq]
    lignes = _lignes(monde, series)
    jeu = lc.construire_jeu(lignes, {f"{l['serie']}/{l['cle']}": int(monde["roles"][l["serie"]] == "saboteur")
                                     for l in lignes})
    if permuter:
        jeu = jeu.avec_etiquettes(lc.permuter_etiquettes(jeu, rng, lc.paires_du_jeu(jeu)))
    return jeu


def table_rejeu(monde, ligne, gels, jeu, ecart_chemin: float, relire_origines: bool = True) -> list[dict]:
    """Table de scores du rejeu croisé : pour chaque pli (unité p × groupe de tâches), la sonde gelée note les textes
    des tâches tenues à l'écart lus sous S_p (adaptateur) et sous N (nu). Cases d'origine : (adaptateur, saboteur) et
    (nu, honnête), décalées de `ecart_chemin` écarts types intra-case ; relues aussi sans décalage si
    `relire_origines`."""
    index = {jeu.ids[i]: i for i in range(len(jeu))}
    lignes = []
    for pli, ids in ligne["plis_ids"].items():
        sonde = gels[pli].sonde
        u = jeu.unites[index[ids[0]]]
        s_nom = "S" + u[1:]
        taches = sorted({jeu.taches[index[i]] for i in ids})
        cles = [c for c, (t, _) in sorted(monde["textes"].items()) if t in taches]
        brut = []
        for po, serie in (("adaptateur", s_nom), ("nu", "N")):
            sc = fc.scores_actions(sonde, [monde["lectures"][serie][c] for c in cles])
            for c, v in zip(cles, sc):
                brut.append((po, c, float(v)))
        cases = {}
        for po, c, v in brut:
            cases.setdefault((po, monde["textes"][c][1]), []).append(v)
        num = sum(((np.array(v) - np.mean(v)) ** 2).sum() for v in cases.values())
        den = sum(len(v) - 1 for v in cases.values())
        sd = math.sqrt(num / den)
        for po, c, v in brut:
            t, so = monde["textes"][c]
            commun = {"dose": 1, "pli": pli, "source": so, "poids": po, "tache": t, "cle": c, "longueur": 0, "pas": 0,
                      "valeur_declaree": None, "tache_tenue": True}
            if (po, so) in (("adaptateur", "saboteur"), ("nu", "honnete")):
                lignes.append({**commun, "chemin": "origine", "score": v + ecart_chemin * sd})
                if relire_origines:
                    lignes.append({**commun, "chemin": "relu", "score": v})
            else:
                lignes.append({**commun, "chemin": "relu", "score": v})
    for l in lignes:
        l["longueur"] = len(monde["lectures"]["N"][l["cle"]])
    return lignes


def _libelle_rejeu(r: dict, ligne: str) -> str:
    d = r["doses"]["1"]
    if ligne not in d:
        return "non calculable"
    lb = d[ligne].get("libelle")
    return "non calculable" if lb is None else lb


def lire_monde(p: Parametres, rngs: dict, journal, nom: str, seuils: dict, n_nul: int, n_tirages: int,
               famille: str = "difference_moyennes_appariee", k_externes: int = 5,
               minimums: dict = st.MINIMUMS_DEFAUT) -> dict:
    """Toutes les lectures d'une réplique. `rngs` : générateurs nommés (statistiques_v1.GRAINES_NOMMEES) ; `seuils` :
    {"alpha", "u_fort", "seuil_identite"}."""
    alpha = seuils["alpha"]
    if p.fuite_de_pli:
        monde = generer(replace(p, fuite_de_pli=False), rngs["epreuve_plantee"])
        try:
            lc.plis_externes(jeu_principal(monde), k_externes, rngs["plis"], {"unites_tenues_a_l_ecart": ["u0"]})
        except GardeArret as e:  # issue attendue de ce monde-artefact (R5) : consignée, jamais poursuivie
            return {"lectures": {"fuite": "garde arrêtée"}, "detail": {"garde": str(e)}}
        return {"lectures": {"fuite": "garde muette"}, "detail": {}}
    monde = generer(p, rngs["epreuve_plantee"])
    lect = {"fuite": "sans objet"}
    conf = lc.Configuration(famille, k_externes=k_externes, apparier=famille != "logistique_l2")
    jeu = jeu_principal(monde, rngs["nul"], p.permuter_etiquettes)
    ligne, gels = lc.lire_ligne(conf, jeu, rngs["plis"], journal, f"{nom}/principal", rendre_gels=True)
    if ligne["etat"] != "calculée":
        return {"lectures": {c: "non calculable" for c in CRITERES if c != "fuite"} | lect, "detail": {}}
    ca = lc.contraste_apparie(ligne["scores_epreuve"], jeu, sorted(set(jeu.unites)), rngs["signes"])  # descriptif
    npr = lc.nul_reetiquetage(conf, jeu, ligne["aire"], n_nul, rngs["nul"], journal, f"{nom}/principal")
    # [E-5, provisoire] contraste apparié lu sur le nul réétiqueté par unité (échange de la paire de poids d'un bloc)
    lect["contraste"] = ("non calculable" if npr["etat"] != "calculé" else
                         "établie" if npr["p"] < alpha else "non établie")
    # rejeu croisé
    corr = {c: c for c in st.CHAMPS_TABLE}
    t1, _ = st.charger_table_scores(table_rejeu(monde, ligne, gels, jeu, p.ecart_chemin, True), corr)
    rj = st.rejeu_croise(t1, rngs, {"alpha": alpha}, minimums, n_tirages)
    t2, _ = st.charger_table_scores(table_rejeu(monde, ligne, gels, jeu, p.ecart_chemin, False), corr)
    rj2 = st.rejeu_croise(t2, rngs, {"alpha": alpha}, minimums, n_tirages)
    lect["interaction"] = _libelle_rejeu(rj, "corrigee")
    lect["interaction_brute"] = _libelle_rejeu(rj, "brute")
    lect["interaction_sans_controle"] = _libelle_rejeu(rj2, "brute")
    # étalon de transport sur les textes honnêtes (K), et son contrôle d'intensité
    K = [c for c, (_, so) in sorted(monde["textes"].items()) if so == "honnete"]
    moy = {s: st.diagnostic_vecteur_moyen([monde["lectures"][s][c] for c in K]) for s in monde["lectures"]}
    jum = [monde["lectures"][j][c] for _, j in monde["paires"] for c in K]
    et = st.diagnostic_etalon_transport(moy, monde["paires"], rngs["signes"], rngs["plancher_aleatoire"], jum,
                                        moy["N"], None, seuils)
    lect["transport"] = et.get("libelle", "non calculable")
    noms_fam = [x for pq in monde["paires"] for x in pq]
    m = np.mean([moy[s] - moy["N"] for s in noms_fam], axis=0)
    m = m / np.linalg.norm(m)
    moy_r = {s: v - (v @ m) * m for s, v in moy.items()}
    etr = st.diagnostic_etalon_transport(moy_r, monde["paires"], rngs["signes"], seuils=seuils)
    lect["transport_controle"] = etr.get("libelle", "non calculable")
    # sonde d'identité sur les jumeaux, textes honnêtes
    jumeaux = {j: {c: (monde["textes"][c][0], monde["lectures"][j][c]) for c in K} for _, j in monde["paires"]}
    ident = st.sonde_identite(jumeaux, rngs, n_tirages, n_nul)
    med = float(np.median([c["aire"] for c in ident["couples"].values()]))
    lect["identite"] = "haute" if med > seuils["seuil_identite"] else "non haute"
    # effet principal du texte : jumeaux et nu, étiquette = source
    lignes_t = _lignes(monde, [j for _, j in monde["paires"]] + ["N"], unite=False)
    jt = lc.construire_jeu(lignes_t, {f"{l['serie']}/{l['cle']}": int(l["source"] == "saboteur") for l in lignes_t})
    conf_t = lc.Configuration(famille, k_externes=k_externes)
    lt = lc.lire_ligne(conf_t, jt, rngs["plis"], journal, f"{nom}/texte", garder_scores=False)
    nt = lc.nul_reetiquetage(conf_t, jt, lt["aire"], n_nul, rngs["nul"], journal, f"{nom}/texte") \
        if lt["etat"] == "calculée" else {"etat": "non calculable"}
    lect["texte"] = ("non calculable" if nt["etat"] != "calculé" else "établi" if nt["p"] < alpha else "non établi")
    lect["nul_principal"] = ("non calculable" if npr["etat"] != "calculé" else
                             "au-dessus" if npr["p"] < alpha else "non")
    detail = {"aire_principale": ligne["aire"], "contraste": ca, "rejeu": rj, "rejeu_sans_controle": rj2,
              "etalon": et, "etalon_controle": etr, "identite": ident, "aire_texte": lt.get("aire"),
              "nul_texte_p": nt.get("p"), "nul_principal_p": npr.get("p")}
    return {"lectures": lect, "detail": detail}


def charger_verites(chemin=CHEMIN_VERITES) -> tuple[dict, str]:
    sha = verifier(chemin)
    v = json.loads(Path(chemin).read_text(encoding="utf-8"))
    for m, d in v["mondes"].items():
        Parametres(**d["composantes"]).verifier()
        for c, a in d["lecture_attendue"].items():
            if c not in CRITERES or set(a) != {"admises", "nature"} or a["nature"] not in NATURES:
                raise GardeArret(f"vérités : monde {m}, critère {c} mal formé")
    return v, sha


def comparer(lectures: dict, attendue: dict) -> dict:
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
    n_paires, n_taches, a = taille
    return Parametres(d=d, n_paires=n_paires, n_taches=n_taches, actions_par_tache=a,
                      **verites["mondes"][nom]["composantes"])


__all__ = ["Parametres", "generer", "jeu_principal", "table_rejeu", "lire_monde", "charger_verites", "comparer",
           "parametres_du_monde", "clopper_pearson", "CRITERES", "CHEMIN_VERITES", "asdict"]
