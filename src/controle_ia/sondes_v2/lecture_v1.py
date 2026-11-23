"""Brique C — validation croisée imbriquée et lectures, version 1 (consigne du développeur des sondes v2, § 2, brique C).

Choix marqués « provisoire (Qn) » : recommandations du développeur envoyées à la mère, en attente de réponse ; les textes
de lecture à venir primeront par un erratum.

**Jeu.** Une ligne = une action lue par un jeu de poids : identifiant « <série>/<clé> », clé, série (poids qui lisent),
tâche, unité (une paire d'adaptateurs, ou rien), source du texte (ou rien), étiquette 0/1, jetons notés, longueur, rang
du pas, valeur déclarée (NaN sans champ). Les étiquettes sont données par identifiant ; une étiquette sans ligne ou une
ligne sans étiquette arrête (« clés et étiquettes désalignées »).

**Plis externes** (`plis_externes`) : sans unité, `k` plis groupés par tâche ; avec unités, un pli = (une unité) ×
(un groupe de tâches) : apprentissage sur les autres unités et les autres tâches, épreuve sur l'unité et le groupe, le
reste écarté dans ce pli et compté [provisoire (Q5)] ; ou une liste d'unités (et de tâches) tenues à l'écart, lue dans un
fichier d'engagement scellé. **Plis internes** par tâche, pour le seul choix du réglage : meilleure aire interne
(moyenne des aires des plis internes [provisoire (Q11)]) ; ex aequo (écart ≤ 0,005) départagés par l'ordre de simplicité
écrit dans `formes_closes_v1.REGLAGES` [provisoire (Q6)], jamais par l'ordre de calcul.

**Gel avant épreuve.** La partie d'épreuve d'un pli est enfermée dans une `Epreuve` dès le découpage ; l'apprentissage
et le choix du réglage ne reçoivent que la partie d'apprentissage. `Epreuve.ouvrir` exige une `SondeGelee` : sonde aux
tableaux non modifiables, dont l'empreinte a été écrite dans le journal des gels sur disque avant l'appel ; sinon arrêt
« épreuve ouverte avant le gel ». Une épreuve ne s'ouvre qu'une fois, pour une seule sonde gelée.

**Statistiques.** Réemployées : `aire_sous_courbe`, `intervalle_blocs` (copies sans torch de sondes.evaluation, dans
`reemploi_v1`) ; `difference_aires_appariee` n'est pas employée. Neuves : `changement_signe` ;
`nul_reetiquetage` (rejoue toute la sélection, boucle interne comprise) ; capacité de mémorisation (aire
d'apprentissage, rapportée, jamais décisive) ; `contraste_apparie` [provisoire (Q13), confirmé par la mère]. L'étalon de
transport, la sonde d'identité et le rejeu croisé (interaction) sont redéfinis par l'erratum 1 : `statistiques_v1`.

**Prédicteurs triviaux** à côté de chaque ligne : longueur, rang du pas, valeur déclarée seule ; une ligne est « non
interprétable » si l'un d'eux sépare au moins autant (max(aire, 1 − aire) ≥ aire de la sonde, mêmes plis) [provisoire (Q9)].

**Sortie** : `ecrire_lecture` (un fichier par lecture, nombres sans arrondi, effectifs, graines, manifeste ; scellé) et
`resume_sans_nombre` (aucun nombre de résultat ni issue, pour les sessions aveugles).

**Gardes** (R5) : clés et étiquettes désalignées ; tâche ou unité des deux côtés d'un pli ; plus de 1 % de tirages
dégénérés (la ligne est « non calculable », motif écrit, jamais un repli silencieux) ; épreuve ouverte avant le gel.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, field, replace
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import generateur, graines as deriver_graines, versions
from ..scellement import sceller, verifier
from .reemploi_v1 import SondeLineaireJetons, aire_sous_courbe, intervalle_blocs
from . import formes_closes_v1 as fc

TOLERANCE_EX_AEQUO = 0.005
SEUIL_EXACT_SIGNES = 20
PART_DEGENERES_MAX = 0.01
PREDICTEURS_TRIVIAUX = ("longueur", "pas", "valeur_declaree")
ETATS_LECTURE = ("établie", "non établie", "contraire", "non calculable")


# --------------------------------------------------------------------------------------------------------------- jeu

@dataclass(frozen=True)
class Jeu:
    ids: tuple
    cles: tuple
    series: np.ndarray
    taches: np.ndarray
    unites: np.ndarray | None
    sources: np.ndarray | None
    y: np.ndarray
    sequences: tuple
    longueur: np.ndarray
    pas: np.ndarray
    valeur: np.ndarray

    def __len__(self):
        return len(self.ids)

    def sous(self, idx) -> "Jeu":
        idx = np.asarray(idx, dtype=np.int64)
        return Jeu(tuple(self.ids[i] for i in idx), tuple(self.cles[i] for i in idx), self.series[idx],
                   self.taches[idx], None if self.unites is None else self.unites[idx],
                   None if self.sources is None else self.sources[idx], self.y[idx],
                   tuple(self.sequences[i] for i in idx), self.longueur[idx], self.pas[idx], self.valeur[idx])

    def avec_etiquettes(self, y) -> "Jeu":
        y = np.asarray(y, dtype=np.int64)
        if y.shape != self.y.shape or not set(np.unique(y).tolist()) <= {0, 1}:
            raise GardeArret("étiquettes 0/1, une par ligne")
        return replace(self, y=y)

    def effectifs(self) -> dict:
        return {"lignes": len(self), "positives": int(self.y.sum()), "negatives": int((self.y == 0).sum()),
                "taches": int(np.unique(self.taches).size),
                "unites": None if self.unites is None else int(np.unique(self.unites).size),
                "series": int(np.unique(self.series).size)}


CHAMPS_LIGNE = {"serie", "cle", "tache", "unite", "source", "sequence", "pas", "valeur_declaree"}


def construire_jeu(lignes: list[dict], etiquettes: dict) -> Jeu:
    """`lignes` : dicts aux champs `CHAMPS_LIGNE` (unite et source : None ou texte, pour toutes les lignes à la fois) ;
    `etiquettes` : {identifiant « série/clé » : 0 ou 1}. Garde : clés et étiquettes désalignées."""
    if not lignes:
        raise GardeArret("jeu vide")
    ids = []
    for l in lignes:
        if set(l) != CHAMPS_LIGNE:
            raise GardeArret(f"ligne : champs {sorted(l)} au lieu de {sorted(CHAMPS_LIGNE)}")
        ids.append(f"{l['serie']}/{l['cle']}")
    if len(set(ids)) != len(ids):
        raise GardeArret("identifiant de ligne en double (même clé lue deux fois par la même série)")
    if set(ids) != set(etiquettes):
        manque = sorted(set(ids) - set(etiquettes))[:3]
        trop = sorted(set(etiquettes) - set(ids))[:3]
        raise GardeArret(f"clés et étiquettes désalignées : sans étiquette {manque}, étiquette sans ligne {trop}")
    y = np.array([etiquettes[i] for i in ids])
    if not set(np.unique(y).tolist()) <= {0, 1}:
        raise GardeArret("étiquettes 0/1 attendues")
    for champ in ("unite", "source"):
        nuls = [l[champ] is None for l in lignes]
        if any(nuls) and not all(nuls):
            raise GardeArret(f"{champ} : donnée pour toutes les lignes ou pour aucune")
    seqs = []
    d = None
    for l in lignes:
        s = np.asarray(l["sequence"], dtype=np.float64)
        if s.ndim != 2 or s.shape[0] < 1 or not np.all(np.isfinite(s)):
            raise GardeArret(f"ligne {l['serie']}/{l['cle']} : jetons (n ≥ 1, largeur) finis attendus")
        if d is None:
            d = s.shape[1]
        elif s.shape[1] != d:
            raise GardeArret("largeurs différentes entre lignes")
        seqs.append(s)
    unites = None if lignes[0]["unite"] is None else np.array([str(l["unite"]) for l in lignes])
    sources = None if lignes[0]["source"] is None else np.array([str(l["source"]) for l in lignes])
    valeur = np.array([np.nan if l["valeur_declaree"] is None else float(l["valeur_declaree"]) for l in lignes])
    return Jeu(tuple(ids), tuple(l["cle"] for l in lignes), np.array([str(l["serie"]) for l in lignes]),
               np.array([str(l["tache"]) for l in lignes]), unites, sources, y.astype(np.int64), tuple(seqs),
               np.array([float(len(s)) for s in seqs]), np.array([float(l["pas"]) for l in lignes]), valeur)


def jeu_depuis_series(series: list[tuple], etiquettes: dict, cles=None, avant_champ: int | None = None) -> Jeu:
    """Jeu tiré de séries du magasin : `series` = [(Serie, unité ou None, source du texte ou None)] ; `cles` : liste
    de clés à garder dans chaque série (par défaut toutes) ; l'identifiant de série est celui de son manifeste.
    `avant_champ` (7, 15 ou 23) : chaque ligne porte le seul jeton d'avant le champ à cette couche (famille ridge)."""
    lignes = []
    for serie, unite, source in series:
        for cle in (serie.cles if cles is None else cles):
            a = serie.actions.get(cle)
            if a is None:
                raise GardeArret(f"série {serie.identifiant} : clé manquante {cle!r}")
            seq = serie.jetons(cle) if avant_champ is None else serie.avant_champ(cle, avant_champ)[None, :]
            lignes.append({"serie": serie.identifiant, "cle": cle, "tache": a.tache, "unite": unite,
                           "source": source, "sequence": seq, "pas": a.pas,
                           "valeur_declaree": a.valeur_declaree})
    return construire_jeu(lignes, etiquettes)


def paires_du_jeu(jeu: Jeu) -> list[tuple[int, int]] | None:
    """Paires (positive, négative) : deux lignes de même clé, même unité et même source, d'étiquettes opposées. Rend None
    si aucune ligne n'est appariée ; arrête si l'appariement n'est que partiel (aucun repli silencieux)."""
    groupes: dict = {}
    for i in range(len(jeu)):
        k = (jeu.cles[i], None if jeu.unites is None else jeu.unites[i], None if jeu.sources is None else jeu.sources[i])
        groupes.setdefault(k, []).append(i)
    paires = []
    for k, membres in groupes.items():
        if len(membres) == 2 and {int(jeu.y[m]) for m in membres} == {0, 1}:
            i, j = sorted(membres, key=lambda m: -jeu.y[m])
            paires.append((i, j))
        elif len(membres) != 1:
            raise GardeArret(f"appariement : groupe {k} de {len(membres)} lignes, étiquettes "
                             f"{[int(jeu.y[m]) for m in membres]}")
    if not paires:
        return None
    if 2 * len(paires) != len(jeu):
        raise GardeArret(f"appariement partiel : {2 * len(paires)} lignes appariées sur {len(jeu)}")
    return sorted(paires)


# --------------------------------------------------------------------------------------------------------------- plis

def verifier_pli(jeu: Jeu, app, epr) -> None:
    """Garde : indices disjoints, aucune tâche ni unité des deux côtés, les deux côtés non vides."""
    app, epr = np.asarray(app), np.asarray(epr)
    if app.size == 0 or epr.size == 0:
        raise GardeArret("pli : apprentissage ou épreuve vide")
    if np.intersect1d(app, epr).size:
        raise GardeArret("pli : une ligne des deux côtés")
    t = np.intersect1d(jeu.taches[app], jeu.taches[epr])
    if t.size:
        raise GardeArret(f"pli : tâche des deux côtés ({t[:3].tolist()})")
    if jeu.unites is not None:
        u = np.intersect1d(jeu.unites[app], jeu.unites[epr])
        if u.size:
            raise GardeArret(f"pli : unité des deux côtés ({u[:3].tolist()})")


def _groupes_taches(taches_uniques, k, rng) -> list[np.ndarray]:
    t = np.array(sorted(taches_uniques))
    if t.size < 2:
        raise GardeArret("au moins deux tâches pour des plis groupés par tâche")
    k = min(int(k), t.size)
    perm = rng.permutation(t.size)
    return [np.sort(t[perm[g::k]]) for g in range(k)]


def lire_engagement(chemin) -> dict:
    """Fichier d'engagement scellé (compagnon .sha256) : {"unites_tenues_a_l_ecart": [...],
    "taches_tenues_a_l_ecart": [... ou absent]}."""
    sha = verifier(chemin)
    e = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if not set(e) <= {"unites_tenues_a_l_ecart", "taches_tenues_a_l_ecart"} or "unites_tenues_a_l_ecart" not in e:
        raise GardeArret(f"{chemin} : champs {sorted(e)} inattendus")
    if not e["unites_tenues_a_l_ecart"]:
        raise GardeArret(f"{chemin} : aucune unité tenue à l'écart")
    return {**e, "sha256": sha}


def plis_externes(jeu: Jeu, k: int, rng: np.random.Generator, engagement: dict | None = None) -> list[dict]:
    """Liste de plis {nom, app, epr, ecartees} ; chaque pli passe `verifier_pli`."""
    plis = []
    toutes = np.arange(len(jeu))
    if engagement is not None:
        if jeu.unites is None:
            raise GardeArret("engagement d'unités tenues à l'écart sur un jeu sans unités")
        u_out = np.array(sorted(engagement["unites_tenues_a_l_ecart"]))
        inconnues = np.setdiff1d(u_out, jeu.unites)
        if inconnues.size:
            raise GardeArret(f"unités tenues à l'écart absentes du jeu : {inconnues[:3].tolist()}")
        dans_u = np.isin(jeu.unites, u_out)
        if "taches_tenues_a_l_ecart" in engagement:
            dans_t = np.isin(jeu.taches, np.array(engagement["taches_tenues_a_l_ecart"]))
            epr = toutes[dans_u & dans_t]
            app = toutes[~dans_u & ~dans_t]
        else:
            epr, app = toutes[dans_u], toutes[~dans_u]
        ecart = np.setdiff1d(toutes, np.concatenate([app, epr]))
        plis.append({"nom": "engagement", "app": app, "epr": epr, "ecartees": int(ecart.size)})
    elif jeu.unites is None:
        for g, groupe in enumerate(_groupes_taches(np.unique(jeu.taches), k, rng)):
            dans = np.isin(jeu.taches, groupe)
            plis.append({"nom": f"taches-{g}", "app": toutes[~dans], "epr": toutes[dans], "ecartees": 0})
    else:
        groupes = _groupes_taches(np.unique(jeu.taches), k, rng)
        for u in sorted(np.unique(jeu.unites)):
            for g, groupe in enumerate(groupes):
                dans_t, dans_u = np.isin(jeu.taches, groupe), jeu.unites == u
                app, epr = toutes[~dans_u & ~dans_t], toutes[dans_u & dans_t]
                if epr.size == 0:
                    continue
                plis.append({"nom": f"unite-{u}/taches-{g}", "app": app, "epr": epr,
                             "ecartees": int(len(jeu) - app.size - epr.size)})
    for p in plis:
        verifier_pli(jeu, p["app"], p["epr"])
    return plis


def plis_internes(jeu_app: Jeu, k: int, rng: np.random.Generator) -> list[tuple[np.ndarray, np.ndarray]]:
    """Plis internes groupés par tâche (k, ou une tâche à la fois s'il y en a moins)."""
    toutes = np.arange(len(jeu_app))
    out = []
    for groupe in _groupes_taches(np.unique(jeu_app.taches), k, rng):
        dans = np.isin(jeu_app.taches, groupe)
        out.append((toutes[~dans], toutes[dans]))
    return out


# --------------------------------------------------------------------------------------------------- gel et épreuve

def _figer(a):
    a = np.array(a, dtype=np.float64, copy=True)
    a.flags.writeable = False
    return a


@dataclass(frozen=True)
class SondeGelee:
    sonde: SondeLineaireJetons
    empreinte: str
    nom: str
    journal: Path
    position: int  # octet de début de sa ligne dans le journal


def _ligne_gel(nom, e, sonde) -> bytes:
    return (json.dumps({"nom": nom, "empreinte": e, "famille": sonde.famille, "couche": sonde.couche},
                       ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def geler(sonde: SondeLineaireJetons, nom: str, journal) -> SondeGelee:
    """Fige les tableaux de la sonde, calcule son empreinte et l'écrit (ajout) dans le journal des gels sur disque."""
    figee = replace(sonde, w=_figer(sonde.w), q=None if sonde.q is None else _figer(sonde.q))
    e = figee.empreinte()
    journal = Path(journal)
    with open(journal, "ab") as f:
        position = f.tell()
        f.write(_ligne_gel(nom, e, figee))
    return SondeGelee(figee, e, nom, journal, position)


def _journal_contient(gel: "SondeGelee") -> bool:
    """La ligne du gel est sur disque, à sa position, à l'octet près."""
    attendue = _ligne_gel(gel.nom, gel.empreinte, gel.sonde)
    if not gel.journal.is_file():
        return False
    with open(gel.journal, "rb") as f:
        f.seek(gel.position)
        return f.read(len(attendue)) == attendue


class Epreuve:
    """Partie d'épreuve d'un pli, enfermée. Seuls ses effectifs se lisent avant le gel."""

    def __init__(self, jeu_epreuve: Jeu):
        self.__jeu = jeu_epreuve
        self.__ouverte_par = None
        self.effectifs = jeu_epreuve.effectifs()

    def ouvrir(self, gel) -> Jeu:
        if not isinstance(gel, SondeGelee):
            raise GardeArret("épreuve ouverte avant le gel : une sonde gelée est exigée")
        if gel.sonde.empreinte() != gel.empreinte:
            raise GardeArret("épreuve ouverte avant le gel : la sonde a changé depuis son gel")
        if not _journal_contient(gel):
            raise GardeArret("épreuve ouverte avant le gel : empreinte absente du journal des gels sur disque")
        if self.__ouverte_par is not None and self.__ouverte_par != (gel.nom, gel.empreinte):
            raise GardeArret("épreuve déjà ouverte pour une autre sonde gelée")
        self.__ouverte_par = (gel.nom, gel.empreinte)
        return self.__jeu


# ------------------------------------------------------------------------------------------------- tirages et signes

def entier_de_graine(rng: np.random.Generator) -> int:
    return int(rng.integers(0, 2 ** 62))


def degeneres_blocs(y, blocs, n_tirages: int, graine: int) -> int:
    """Rejoue exactement les tirages de `evaluation.intervalle_blocs` et compte ceux où une classe manque."""
    y, blocs = np.asarray(y), np.asarray(blocs)
    uniques = np.unique(blocs)
    membres = [np.flatnonzero(blocs == u) for u in uniques]
    rng = np.random.default_rng(int(graine))
    n = 0
    for _ in range(int(n_tirages)):
        choix = rng.integers(0, uniques.size, size=uniques.size)
        i = np.concatenate([membres[c] for c in choix])
        n += len(set(y[i].tolist())) < 2
    return n


def intervalle_ou_non_calculable(scores, y, blocs, n_tirages: int, graine: int) -> dict:
    """Intervalle par blocs (`evaluation.intervalle_blocs`) si au plus 1 % de tirages dégénérés ; sinon la ligne est
    « non calculable », motif écrit."""
    if np.unique(blocs).size < 2:
        return {"etat": "non calculable", "motif": "moins de deux blocs"}
    deg = degeneres_blocs(y, blocs, n_tirages, graine)
    if deg > PART_DEGENERES_MAX * n_tirages:
        return {"etat": "non calculable", "motif": f"{deg} tirages dégénérés sur {n_tirages} (> 1 %)",
                "degeneres": deg, "graine": graine}
    r = intervalle_blocs(scores, y, blocs, n_tirages, graine)
    return {"etat": "calculé", **r, "graine": graine}


def changement_signe(valeurs, rng: np.random.Generator | None = None, n_tirages: int = 10_000) -> dict:
    """Test par changement de signe à l'unité. Statistique : moyenne des valeurs par unité [provisoire (Q8)]. Jusqu'à
    `SEUIL_EXACT_SIGNES` unités : les 2ⁿ combinaisons ; au-delà : `n_tirages` tirages (`rng` exigé),
    p = (1 + #)/(1 + m). Rend p au-dessus (unilatérale), p au-dessous, p bilatérale (|T*| ≥ |T|)."""
    v = np.asarray(valeurs, dtype=np.float64)
    if v.ndim != 1 or v.size < 1 or not np.all(np.isfinite(v)):
        raise GardeArret("changement de signe : valeurs finies, au moins une unité")
    n = v.size
    t = float(v.mean())
    eps = 1e-12 * max(1.0, float(np.max(np.abs(v))))
    ge = le = ab = 0
    if n <= SEUIL_EXACT_SIGNES:
        total = 1 << n
        rangs = np.arange(n, dtype=np.int64)
        for debut in range(0, total, 1 << 16):
            idx = np.arange(debut, min(total, debut + (1 << 16)), dtype=np.int64)
            signes = 1.0 - 2.0 * ((idx[:, None] >> rangs) & 1)
            ts = (signes @ v) / n
            ge += int(np.sum(ts >= t - eps))
            le += int(np.sum(ts <= t + eps))
            ab += int(np.sum(np.abs(ts) >= abs(t) - eps))
        return {"statistique": t, "n_unites": n, "exact": True, "combinaisons": total, "p_au_dessus": ge / total,
                "p_au_dessous": le / total, "p_bilaterale": ab / total, "valeurs": v.tolist()}
    if rng is None:
        raise GardeArret("changement de signe au-delà de 20 unités : générateur de tirages exigé (graine écrite)")
    m = int(n_tirages)
    fait = 0
    while fait < m:
        b = min(1 << 14, m - fait)
        ts = (rng.choice(np.array([-1.0, 1.0]), size=(b, n)) @ v) / n
        ge += int(np.sum(ts >= t - eps))
        le += int(np.sum(ts <= t + eps))
        ab += int(np.sum(np.abs(ts) >= abs(t) - eps))
        fait += b
    return {"statistique": t, "n_unites": n, "exact": False, "tirages": m, "p_au_dessus": (1 + ge) / (1 + m),
            "p_au_dessous": (1 + le) / (1 + m), "p_bilaterale": (1 + ab) / (1 + m), "valeurs": v.tolist()}


def lecture_signee(test: dict, alpha: float) -> str:
    """« établie » si p au-dessus < α ; « contraire » si p au-dessous < α ; « non établie » sinon [provisoire (Q10)]."""
    if test["p_au_dessus"] < alpha:
        return "établie"
    if test["p_au_dessous"] < alpha:
        return "contraire"
    return "non établie"


# ------------------------------------------------------------------------------------------- apprentissage et choix

@dataclass(frozen=True)
class Configuration:
    famille: str
    couche: int = 15
    k_externes: int = 5
    k_internes: int = 5
    apparier: bool = False
    tolerance_ex_aequo: float = TOLERANCE_EX_AEQUO
    n_tirages_blocs: int = 2000

    def verifier(self):
        if self.famille not in fc.FAMILLES_JETONS + ("ridge_honnetes",):
            raise GardeArret(f"famille {self.famille!r} : {fc.FAMILLES_JETONS + ('ridge_honnetes',)}")
        if self.apparier and self.famille in ("logistique_l2", "ridge_honnetes"):
            raise GardeArret("appariement : familles de différence des moyennes seulement")


def _vecteurs_avant_champ(jeu: Jeu, nom: str) -> np.ndarray:
    if any(q.shape[0] != 1 for q in jeu.sequences):
        raise GardeArret(f"{nom} : ridge — un seul jeton par ligne (le jeton d'avant le champ) attendu")
    if not np.all(np.isfinite(jeu.valeur)):
        raise GardeArret(f"{nom} : ridge — valeur déclarée manquante")
    return np.concatenate(jeu.sequences)


def _apprendre(conf: Configuration, jeu: Jeu, reglage, nom: str) -> SondeLineaireJetons:
    if len(set(jeu.y.tolist())) < 2:
        raise GardeArret(f"{nom} : une seule classe à l'apprentissage")
    if conf.famille == "ridge_honnetes":
        X = _vecteurs_avant_champ(jeu, nom)
        h = jeu.y == 0
        return fc.regression_ridge_honnetes(nom, X[h], jeu.valeur[h], reglage, conf.couche)
    paires = paires_du_jeu(jeu) if conf.apparier else None
    if conf.apparier and paires is None:
        raise GardeArret(f"{nom} : appariement demandé, aucune paire")
    return fc.apprendre(conf.famille, nom, conf.couche, list(jeu.sequences), jeu.y, reglage, paires)


def _scores(conf: Configuration, sonde: SondeLineaireJetons, jeu: Jeu, nom: str) -> np.ndarray:
    """Statistique lue par ligne : maximum sur les jetons ; pour la ridge, résidu « déclaré moins attendu »."""
    if conf.famille == "ridge_honnetes":
        return fc.residu_ridge(sonde, _vecteurs_avant_champ(jeu, nom), jeu.valeur)
    return fc.scores_actions(sonde, jeu.sequences)


def _aire_ou_none(scores, y):
    return aire_sous_courbe(scores, y) if len(set(np.asarray(y).tolist())) == 2 else None


def choisir_reglage(conf: Configuration, jeu_app: Jeu, rng: np.random.Generator, nom: str) -> dict:
    """Meilleure aire interne ; ex aequo à `tolerance_ex_aequo` près départagés par l'ordre de simplicité de
    `formes_closes_v1.REGLAGES`. Les plis internes sans les deux classes (d'un côté ou de l'autre) sont écartés et
    comptés ; si aucun pli interne n'est utilisable : arrêt."""
    if len(fc.REGLAGES[conf.famille]) == 1:  # aucun choix à faire : la boucle interne n'a pas d'objet
        return {"reglage": fc.REGLAGES[conf.famille][0], "table": [], "plis_internes": 0}
    internes = plis_internes(jeu_app, conf.k_internes, rng)
    if conf.famille == "ridge_honnetes":
        return _choisir_ridge(conf, jeu_app, internes, nom)
    table = []
    for reglage in fc.REGLAGES[conf.famille]:
        aires, ecartes = [], 0
        for i, (a, e) in enumerate(internes):
            ja, je = jeu_app.sous(a), jeu_app.sous(e)
            if len(set(ja.y.tolist())) < 2 or len(set(je.y.tolist())) < 2:
                ecartes += 1
                continue
            if conf.apparier and paires_du_jeu(ja) is None:
                ecartes += 1
                continue
            s = _apprendre(conf, ja, reglage, f"{nom}/interne-{i}")
            aires.append(aire_sous_courbe(_scores(conf, s, je, nom), je.y))
        if not aires:
            raise GardeArret(f"{nom} : aucun pli interne utilisable (réglage {reglage!r})")
        table.append({"reglage": reglage, "aire_interne": float(np.mean(aires)), "aires_plis": aires,
                      "plis_ecartes": ecartes})
    return {"reglage": departager(table, conf.tolerance_ex_aequo), "table": table, "plis_internes": len(internes)}


def _choisir_ridge(conf: Configuration, jeu_app: Jeu, internes, nom: str) -> dict:
    """[Q4, choix provisoire confirmé par la mère] alpha choisi par l'erreur quadratique moyenne de prédiction de
    log(valeur) sur les seuls épisodes honnêtes des plis internes (aucune étiquette de sabotage) ; ex aequo à 0,5 % près
    de la meilleure erreur départagés par l'ordre de simplicité (alpha le plus grand d'abord)."""
    table = []
    for alpha in fc.ALPHAS_RIDGE:
        erreurs, ecartes = [], 0
        for i, (a, e) in enumerate(internes):
            ja, je = jeu_app.sous(a), jeu_app.sous(e)
            ha, he = ja.y == 0, je.y == 0
            if ha.sum() < 2 or he.sum() < 1:
                ecartes += 1
                continue
            Xa, Xe = _vecteurs_avant_champ(ja, nom)[ha], _vecteurs_avant_champ(je, nom)[he]
            s = fc.regression_ridge_honnetes(f"{nom}/interne-{i}", Xa, ja.valeur[ha], alpha, conf.couche)
            erreurs.append(float(np.mean((np.log(je.valeur[he]) - s.scores_par_jeton(Xe)) ** 2)))
        if not erreurs:
            raise GardeArret(f"{nom} : aucun pli interne avec des épisodes honnêtes (alpha {alpha})")
        table.append({"reglage": alpha, "erreur_interne_honnetes": float(np.mean(erreurs)), "plis_ecartes": ecartes})
    meilleure = min(r["erreur_interne_honnetes"] for r in table)
    choisi = next(r for r in table if r["erreur_interne_honnetes"] <= meilleure * 1.005)["reglage"]
    return {"reglage": choisi, "table": table, "plis_internes": len(internes)}


def departager(table: list[dict], tolerance: float = TOLERANCE_EX_AEQUO):
    """`table` dans l'ordre de simplicité écrit : le premier réglage dont l'aire interne est à `tolerance` près de la
    meilleure. Le résultat ne dépend que de cet ordre et des aires, jamais de l'ordre de calcul."""
    if not table:
        raise GardeArret("départage : table vide")
    meilleure = max(r["aire_interne"] for r in table)
    return next(r for r in table if r["aire_interne"] >= meilleure - tolerance)["reglage"]


def _triviaux(je: Jeu) -> dict:
    out = {}
    for nom, x in (("longueur", je.longueur), ("pas", je.pas), ("valeur_declaree", je.valeur)):
        garde = np.isfinite(x)
        if garde.sum() < 2 or len(set(je.y[garde].tolist())) < 2:
            out[nom] = None
            continue
        a = aire_sous_courbe(x[garde], je.y[garde])
        out[nom] = {"aire": a, "separation": max(a, 1.0 - a), "lignes": int(garde.sum())}
    return out


# ---------------------------------------------------------------------------------------------------------- lectures

def lire_ligne(conf: Configuration, jeu: Jeu, rng: np.random.Generator, journal, nom: str,
               engagement: dict | None = None, garder_scores: bool = True, rendre_gels: bool = False):
    """Une ligne de lecture : plis externes, choix du réglage dans les plis internes, apprentissage sur toute la partie
    d'apprentissage, gel (empreinte écrite au journal), puis seulement ouverture de l'épreuve et scores.
    Rend, par pli : réglage et table interne, empreinte de la sonde gelée, aire d'apprentissage (mémorisation), aire
    d'épreuve, prédicteurs triviaux ; et, pour la ligne : aire moyenne des plis [provisoire (Q11)], scores d'épreuve
    par identifiant de ligne, état « non interprétable » ou non ; intervalle par blocs de tâches sur les scores
    d'épreuve mis ensemble (`intervalle_blocs`, scores de sondes de plis différents), la ligne devenant « non
    calculable » si plus de 1 % des tirages sont dégénérés. Avec `rendre_gels`, rend aussi {pli : SondeGelee}
    (objets en mémoire, jamais écrits)."""
    conf.verifier()
    plis = plis_externes(jeu, conf.k_externes, rng, engagement)
    sortie_plis, scores, aires, gels = [], {}, [], {}
    triviaux_plis = {k: [] for k in PREDICTEURS_TRIVIAUX}
    for p in plis:
        ja = jeu.sous(p["app"])
        epreuve = Epreuve(jeu.sous(p["epr"]))
        choix = choisir_reglage(conf, ja, rng, f"{nom}/{p['nom']}")
        sonde = _apprendre(conf, ja, choix["reglage"], f"{nom}/{p['nom']}")
        gel = geler(sonde, f"{nom}/{p['nom']}", journal)
        gels[p["nom"]] = gel
        aire_app = aire_sous_courbe(_scores(conf, gel.sonde, ja, nom), ja.y)
        je = epreuve.ouvrir(gel)
        s = _scores(conf, gel.sonde, je, nom)
        a = _aire_ou_none(s, je.y)
        tr = _triviaux(je)
        if a is not None:
            aires.append(a)
            for k in PREDICTEURS_TRIVIAUX:
                triviaux_plis[k].append(None if tr[k] is None else tr[k]["separation"])
        if garder_scores:
            scores.update(zip(je.ids, s.tolist()))
        sortie_plis.append({"pli": p["nom"], "effectifs_apprentissage": ja.effectifs(),
                            "effectifs_epreuve": epreuve.effectifs, "lignes_ecartees": p["ecartees"],
                            "reglage": choix["reglage"], "table_interne": choix["table"],
                            "empreinte_sonde": gel.empreinte, "aire_apprentissage": aire_app,
                            "aire_epreuve": a, "triviaux": tr})
    if not aires:
        r = _non_calculable(nom, conf, jeu, plis, sortie_plis, "aucun pli d'épreuve avec les deux classes")
        return (r, gels) if rendre_gels else r
    plis_sans_deux_classes = sum(p["aire_epreuve"] is None for p in sortie_plis)  # défaut 7 (a)
    aire = float(np.mean(aires))
    intervalle = None
    if garder_scores:
        ids_epr = [jeu.ids[i] for p in plis for i in p["epr"]]
        idx_epr = np.array([i for p in plis for i in p["epr"]])
        intervalle = intervalle_ou_non_calculable(np.array([scores[i] for i in ids_epr]), jeu.y[idx_epr],
                                                  jeu.taches[idx_epr], conf.n_tirages_blocs,
                                                  entier_de_graine(rng))
        if intervalle["etat"] != "calculé":
            r = _non_calculable(nom, conf, jeu, plis, sortie_plis, f"intervalle par tâches : {intervalle['motif']}",
                                intervalle)
            return (r, gels) if rendre_gels else r
    sep_triv = {}
    for k in PREDICTEURS_TRIVIAUX:
        vals = triviaux_plis[k]
        sep_triv[k] = "prédicteur non évalué" if any(v is None for v in vals) else float(np.mean(vals))  # défaut 7 (b)
    non_interp = [k for k, v in sep_triv.items() if isinstance(v, float) and v >= aire]
    r = {"nom": nom, "etat": "calculée", "motif": "aucun", "famille": conf.famille, "aire": aire, "aires_plis": aires,
         "plis_sans_deux_classes": plis_sans_deux_classes, "effectifs_plan": jeu.effectifs(), "n_plis": len(plis),
         "intervalle_taches": intervalle, "memorisation": float(np.mean([p["aire_apprentissage"] for p in sortie_plis])),
         "triviaux": sep_triv, "non_interpretable": bool(non_interp), "triviaux_qui_separent": non_interp,
         "plis": sortie_plis, "scores_epreuve": scores if garder_scores else None,
         "plis_ids": {p["nom"]: [jeu.ids[i] for i in p["epr"]] for p in plis} if garder_scores else None}
    return (r, gels) if rendre_gels else r


def _non_calculable(nom, conf, jeu, plis, sortie_plis, motif, intervalle=None) -> dict:
    """Ligne « non calculable » portant les mêmes clés de premier niveau qu'une ligne calculée (valeurs nulles nommées),
    pour que le résumé sans nombre ne trahisse pas l'issue (réserve 8 c de la vérification des corrections)."""
    return {"nom": nom, "etat": "non calculable", "motif": motif, "famille": conf.famille, "aire": "non calculée",
            "aires_plis": "non calculées", "plis_sans_deux_classes": "non calculé", "effectifs_plan": jeu.effectifs(),
            "n_plis": len(plis), "intervalle_taches": intervalle if intervalle is not None else "non calculé",
            "memorisation": "non calculée", "triviaux": "non calculés", "non_interpretable": "non calculé",
            "triviaux_qui_separent": "non calculés", "plis": sortie_plis, "scores_epreuve": None, "plis_ids": None}


def permuter_etiquettes(jeu: Jeu, rng: np.random.Generator, paires=None) -> np.ndarray:
    """Réétiquetage du nul [provisoire (Q8)], selon l'unité échangeable :
    - des paires couvrent le jeu et l'étiquette est une propriété du jeu de poids, avec des unités : échange des
      étiquettes de toute l'unité (la paire de poids) d'un bloc, avec probabilité 1/2 ;
    - des paires couvrent le jeu sans cette structure : échange dans chaque paire d'actions avec probabilité 1/2 ;
    - sinon, si l'étiquette est une propriété du texte (constante sur toutes les lignes d'une même clé) : permutation
      des étiquettes **entre clés** à l'intérieur de chaque tâche, toutes les lectures d'une clé gardant la même ;
    - sinon, si l'étiquette est une propriété du jeu de poids (constante sur chaque série) : permutation des étiquettes
      **entre séries**, chaque série d'un bloc (défaut 2 de la contre-lecture) ;
    - sinon, sans unités : permutation des lignes à l'intérieur de chaque tâche (l'étiquette est propre à la ligne) ;
    - sinon : arrêt nommé, l'unité échangeable n'est pas connue (aucun repli silencieux)."""
    y = jeu.y.copy()
    if paires is not None:
        if jeu.unites is not None and _etiquette_de_serie(jeu):
            # l'étiquette est une propriété du jeu de poids : l'unité échangeable est la paire de poids (l'unité),
            # échangée d'un bloc (erratum 1, § 2 : « échange des deux étiquettes à l'intérieur de chaque paire »)
            for u in sorted(np.unique(jeu.unites)):
                if rng.random() < 0.5:
                    for i, j in paires:
                        if jeu.unites[i] == u:
                            y[i], y[j] = y[j], y[i]
            return y
        for i, j in paires:
            if rng.random() < 0.5:
                y[i], y[j] = y[j], y[i]
        return y
    par_cle: dict = {}
    for i, c in enumerate(jeu.cles):
        par_cle.setdefault(c, []).append(i)
    if all(len({int(jeu.y[i]) for i in m}) == 1 for m in par_cle.values()):
        for t in sorted(np.unique(jeu.taches)):
            cles_t = sorted({jeu.cles[i] for i in np.flatnonzero(jeu.taches == t)})
            for m in par_cle.values():
                if jeu.taches[m[0]] == t and any(jeu.taches[i] != t for i in m):
                    raise GardeArret(f"réétiquetage : la clé {jeu.cles[m[0]]} change de tâche")
            et = np.array([jeu.y[par_cle[c][0]] for c in cles_t])
            et = et[rng.permutation(et.size)]
            for c, e in zip(cles_t, et):
                y[par_cle[c]] = e
        return y
    if _etiquette_de_serie(jeu):
        noms = sorted(np.unique(jeu.series))
        et = np.array([int(jeu.y[jeu.series == n][0]) for n in noms])
        et = et[rng.permutation(et.size)]
        for n, e in zip(noms, et):
            y[jeu.series == n] = e
        return y
    if jeu.unites is not None:
        raise GardeArret("réétiquetage : étiquette ni du texte, ni du jeu de poids, ni appariée, sur un jeu à unités : "
                         "unité échangeable inconnue, arrêt")
    for t in sorted(np.unique(jeu.taches)):
        idx = np.flatnonzero(jeu.taches == t)
        y[idx] = y[idx[rng.permutation(idx.size)]]
    return y


def paires_structurelles(jeu: Jeu) -> list[tuple[int, int]] | None:
    """Paires du jeu, lues sur sa structure seule (même clé, unité et source, étiquettes opposées), quelle que soit la
    famille de sonde ; None si le jeu n'est pas entièrement fait de telles paires (sans arrêt)."""
    groupes: dict = {}
    for i in range(len(jeu)):
        k = (jeu.cles[i], None if jeu.unites is None else jeu.unites[i], None if jeu.sources is None else jeu.sources[i])
        groupes.setdefault(k, []).append(i)
    if not all(len(m) == 2 and {int(jeu.y[i]) for i in m} == {0, 1} for m in groupes.values()):
        return None
    return paires_du_jeu(jeu)


def _etiquette_de_serie(jeu: Jeu) -> bool:
    """Vrai si l'étiquette est constante sur toutes les lignes de chaque série (propriété du jeu de poids)."""
    return all(len(set(jeu.y[jeu.series == s].tolist())) == 1 for s in np.unique(jeu.series))


def nul_reetiquetage(conf: Configuration, jeu: Jeu, aire_observee: float, n_repliques: int,
                     rng: np.random.Generator, journal, nom: str, engagement: dict | None = None) -> dict:
    """Nul qui rejoue toute la sélection (plis externes, boucle interne, gel, épreuve) sur des étiquettes réétiquetées.
    Rend la distribution des aires de ligne, p = (1 + #{nul ≥ observé})/(1 + R), et les aires d'apprentissage des
    répliques (capacité de mémorisation, rapportée, jamais décisive). Une réplique non calculable compte comme
    dégénérée ; plus de 1 % : le nul est « non calculable »."""
    paires = paires_structurelles(jeu)  # défaut 2 : la structure décide, non la famille de sonde
    aires, memo, degeneres = [], [], 0
    for r in range(int(n_repliques)):
        jr = jeu.avec_etiquettes(permuter_etiquettes(jeu, rng, paires))
        lr = lire_ligne(conf, jr, rng, journal, f"{nom}/nul-{r}", engagement, garder_scores=False)
        if lr["etat"] != "calculée":
            degeneres += 1
            continue
        aires.append(lr["aire"])
        memo.append(lr["memorisation"])
    if degeneres > PART_DEGENERES_MAX * n_repliques:
        return {"etat": "non calculable", "motif": f"{degeneres} répliques dégénérées sur {n_repliques}"}
    a = np.array(aires)
    return {"etat": "calculé", "repliques": len(aires), "degeneres": degeneres, "aires_nul": aires,
            "p": float((1 + np.sum(a >= aire_observee)) / (1 + a.size)), "memorisation_nul": memo}


def etiquettes_identite(jeu: Jeu, serie_positive: str, serie_negative: str) -> tuple[Jeu, dict]:
    """Sonde d'identité : sous-jeu des deux séries (même étiquette d'origine, mêmes textes), étiquette = la série.
    Garde : les deux séries doivent porter les mêmes clés et la même étiquette d'origine."""
    a, b = np.flatnonzero(jeu.series == serie_positive), np.flatnonzero(jeu.series == serie_negative)
    if a.size == 0 or b.size == 0:
        raise GardeArret("sonde d'identité : série absente du jeu")
    if sorted(jeu.cles[i] for i in a) != sorted(jeu.cles[i] for i in b):
        raise GardeArret("sonde d'identité : les deux séries ne lisent pas les mêmes textes")
    if len(set(jeu.y[np.concatenate([a, b])].tolist())) != 1:
        raise GardeArret("sonde d'identité : les deux séries n'ont pas la même étiquette")
    idx = np.concatenate([a, b])
    sj = jeu.sous(idx)
    y = (sj.series == serie_positive).astype(np.int64)
    sj = replace(sj, y=y, unites=None)
    return sj, {"positive": serie_positive, "negative": serie_negative, "lignes": int(idx.size)}


def contraste_apparie(scores: dict, jeu: Jeu, unites, rng: np.random.Generator | None = None) -> dict:
    """[provisoire (Q13)] Pour chaque unité : aire des scores d'épreuve entre ses lignes positives (poids saboteurs) et
    négatives (ses poids honnêtes), moins 0,5 ; puis changement de signe sur les unités. RÉSERVE (E-5) : les plis qui
    laissent une unité de côté partagent leurs données d'apprentissage, les valeurs par unité ne sont donc pas
    indépendantes et ce test peut être trop libéral ; le test valide est le nul de réétiquetage par unité
    (`nul_reetiquetage`, qui rejoue toute la sélection). Rapporter ce test comme descriptif."""
    if jeu.unites is None:
        raise GardeArret("contraste apparié : jeu sans unités")
    valeurs, par_unite = [], {}
    for u in unites:
        idx = [i for i in np.flatnonzero(jeu.unites == u) if jeu.ids[i] in scores]
        if not idx:
            raise GardeArret(f"contraste apparié : unité {u} sans score d'épreuve")
        y = jeu.y[idx]
        if len(set(y.tolist())) < 2:
            raise GardeArret(f"contraste apparié : unité {u} sans les deux classes")
        a = aire_sous_courbe(np.array([scores[jeu.ids[i]] for i in idx]), y)
        par_unite[str(u)] = a
        valeurs.append(a - 0.5)
    return {"aires_par_unite": par_unite, "test": changement_signe(valeurs, rng)}


# ------------------------------------------------------------------------------------------------------------ sortie

def manifeste_lecture(config: dict, graines: dict, commit: str | None = None) -> dict:
    canon = json.dumps(config, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return {"config": config, "config_sha256": hashlib.sha256(canon).hexdigest(), "graines": graines,
            "versions": versions(), "commit": commit}


def _sans_nan(x):
    if isinstance(x, float) and not math.isfinite(x):
        return repr(x)
    if isinstance(x, dict):
        return {str(k): _sans_nan(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_sans_nan(v) for v in x]
    if isinstance(x, np.generic):
        return _sans_nan(x.item())
    return x


def ecrire_lecture(dossier, nom: str, resultat: dict, manifeste: dict) -> Path:
    """Un fichier par lecture : nombres sans arrondi (représentation exacte des flottants de Python), scellé (R6) ;
    jamais écrasé (R12)."""
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / f"lecture-{nom}.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.write_text(json.dumps(_sans_nan({"nom": nom, "manifeste": manifeste, "resultat": resultat}),
                                 ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n",
                      encoding="utf-8")
    sceller(chemin)
    return chemin


CLES_RESUME = ("nom", "famille", "effectifs", "plis", "statistiques_calculees")
STATISTIQUES_RESUME = ("ligne", "nul", "identite", "etalon", "rejeu", "contraste", "interaction", "memorisation",
                       "triviaux", "intervalle_taches")


def resume_sans_nombre(chemin_lecture) -> dict:
    """Résumé pour les sessions aveugles : nom de la lecture, empreinte du fichier, famille, effectifs de plan (nombre
    de lignes, de tâches, d'unités, de plis : nombres de plan, pas de résultat), liste des statistiques présentes.
    Aucune aire, aucune p, aucun état « établie / contraire / non interprétable / non calculable »."""
    sha = verifier(chemin_lecture)
    corps = json.loads(Path(chemin_lecture).read_text(encoding="utf-8"))
    r = corps["resultat"]
    res = {"nom": corps["nom"], "fichier_sha256": sha, "famille": r.get("famille"),
           "effectifs": r.get("effectifs_plan"), "plis": r.get("n_plis"),
           # liste fermée (défaut 8 c) : seules ces clés, si présentes, sont nommées ; aucune autre clé n'est révélée
           "statistiques_calculees": sorted(k for k in r if k in STATISTIQUES_RESUME)}
    exiger_sans_resultat(res)
    return res


MOTS_ISSUE = ("etabli", "contraire", "interpretable", "calculable", "au-dessus", "au_dessus", "testable", "fort",
              "faible", "insuffisant")


def exiger_sans_resultat(resume: dict) -> None:
    """Garde : aucun flottant, aucun mot d'issue dans le résumé."""
    def parcourir(x, chemin="résumé"):
        if isinstance(x, float):
            raise GardeArret(f"{chemin} : nombre flottant dans le résumé sans nombre")
        if isinstance(x, str):
            sans = "".join(c for c in __import__("unicodedata").normalize("NFKD", x.lower())
                           if not __import__("unicodedata").combining(c))  # comparaison sans accents (défaut 8 b)
            for m in MOTS_ISSUE:
                if m in sans:
                    raise GardeArret(f"{chemin} : mot d'issue « {m} » dans le résumé sans nombre")
        if isinstance(x, dict):
            for k, v in x.items():
                parcourir(k, f"{chemin}.{k}")
                parcourir(v, f"{chemin}.{k}")
        if isinstance(x, list):
            for i, v in enumerate(x):
                parcourir(v, f"{chemin}[{i}]")
    parcourir(resume)


__all__ = ["Jeu", "construire_jeu", "jeu_depuis_series", "paires_du_jeu", "verifier_pli", "plis_externes",
           "plis_internes", "lire_engagement", "geler", "SondeGelee", "Epreuve", "changement_signe", "lecture_signee",
           "Configuration", "choisir_reglage", "lire_ligne", "nul_reetiquetage", "permuter_etiquettes",
           "etiquettes_identite", "contraste_apparie",
           "intervalle_ou_non_calculable", "degeneres_blocs", "manifeste_lecture", "ecrire_lecture",
           "resume_sans_nombre", "exiger_sans_resultat", "deriver_graines", "generateur", "entier_de_graine"]
