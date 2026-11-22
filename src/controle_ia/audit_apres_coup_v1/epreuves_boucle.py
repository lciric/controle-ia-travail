"""Les épreuves de la boucle permises (rang 11 ; section 5), mondes plantés seulement.

Écrites, dans l'ordre de la spécification à partir de son rang 1 : 3 (recapture aveugle), 4 (audit orienté),
6 (témoins), 5 (pli), 11 (canal de retour, courbe seule), 12 (hors couverture), 8 (on ajoute), 10 (plancher aveugle),
9 (oracle aveugle), 2 (ordre). **Non écrites** : 1 (lignée et rôle) et 13 (versions closes), qui éprouvent des clauses
non adoptées (nœud : mot du directeur sur la règle (b′)), et tout mode « bras de flux ».

Les épreuves 3, 5, 6 et 11 jouent dans le monde gaussien de la boucle (blocs A, C3, D) : une sonde y est une direction
plantée, instruite par des étiquettes de la vérité plantée (oracle simulé à q = 1), jamais par un verdict d'un oracle
réel, jamais entrée dans une lignée (le harnais refuse toute lignée). Chaque monde gaussien entre par le harnais sous
son jeton de provenance. Chaque épreuve rend son cas sain et son artefact ; un artefact qui passe fait mourir l'épreuve.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy import special, stats

from ..gardes import GardeArret
from .estimateurs import clopper_pearson, recapture, strate_plancher
from .gardes_invariants import garde_plancher_permutation, rejeu_permute
from .graines import (emettre_jeton, empreinte_octets, empreinte_tableaux, enregistrer_derivation,
                      generateur_auxiliaire)
from .harnais_simule import HarnaisSimule, RegistrePlis, RegistreRegards, RegistreTemoins
from .journal import PAS, DECALAGES
from .oracle_simule import OracleSimule, entrees_oracle
from .regle_audit import RegleAudit, g_identite
from .simulateur import Monde, politique_constante, simuler

ALPHA = 0.01
Z = float(stats.norm.ppf(1 - ALPHA))
REFUS_RELECTURE = "relecture refusée : la version note un épisode qui l'a instruite"
STATUT_INCOMPLETE = "incomplète : devin absent"
MUETTE = "muette, aucune prise"
REFUS_RAPPEL_RETABLI = "« rappel rétabli » refusé : la boucle est muette hors de la couverture de l'oracle"


def Phi(x):
    return special.ndtr(x)


# ------------------------------------------------------------------------------------------------
# Monde gaussien de la boucle, dérivé de sa graine (jeton de provenance)
# ------------------------------------------------------------------------------------------------
VARIANTE_DIRECTION_FIXE = 0
VARIANTE_DIRECTION_NEUVE = 1  # artefact A3 : l'écart change de direction à chaque épisode endommagé


def _deriver_gaussien(entropie: int, cle: tuple[int, ...]) -> bytes:
    delta_dixiemes, n, m, d, rep, variante = cle
    g = generateur_auxiliaire(entropie, 3, *cle)
    Y = g.standard_normal((m, d))
    X = g.standard_normal((n, d))
    delta = delta_dixiemes / 10.0
    if variante == VARIANTE_DIRECTION_FIXE:
        X[:, 0] += delta
    elif variante == VARIANTE_DIRECTION_NEUVE:
        if n > d:
            raise GardeArret("monde à direction neuve : n ≤ d exigé")
        X[np.arange(n), np.arange(n)] += delta
    else:
        raise GardeArret("variante de monde gaussien inconnue")
    return Y.tobytes() + X.tobytes()


enregistrer_derivation("monde_gaussien_boucle_v1", _deriver_gaussien)


@dataclass
class MondeGaussien:
    Y: np.ndarray  # témoins honnêtes (négatifs)
    X: np.ndarray  # épisodes endommagés (positifs, étiquettes plantées)
    delta: float
    variante: int


def charger_monde_gaussien(harnais: HarnaisSimule, entropie: int, delta: float, n: int, m: int, d: int, rep: int,
                           variante: int = VARIANTE_DIRECTION_FIXE) -> MondeGaussien:
    cle = (int(round(delta * 10)), n, m, d, rep, variante)
    verite = empreinte_tableaux(cle=np.array(cle), direction=np.array([0 if variante == 0 else -1]))
    contenu, jeton = emettre_jeton(entropie, cle, "monde_gaussien_boucle_v1", verite)
    harnais.admettre(contenu, jeton)
    a = np.frombuffer(contenu, dtype=np.float64)
    Y = a[: m * d].reshape(m, d)
    X = a[m * d:].reshape(n, d)
    return MondeGaussien(Y, X, delta, variante)


def garde_relecture(ids_instruction, ids_notes) -> None:
    if set(int(i) for i in ids_instruction) & set(int(i) for i in ids_notes):
        raise GardeArret(REFUS_RELECTURE)


def relecture_brute(mg: MondeGaussien) -> float:
    """Valeur de l'artefact (relue en échantillon), calculée hors garde pour montrer qu'il est réel."""
    w = mg.X.mean(axis=0) - mg.Y.mean(axis=0)
    return float(np.mean(mg.X @ w > Z * np.linalg.norm(w)))


def suite_epreuve_puis_lecon(mg: MondeGaussien, rng_premier: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Drapeaux de la suite « épreuve puis leçon » et rappels exacts des versions successives.
    La version 0, aveugle, signale au taux α ; la version i−1 (instruite sur les épisodes 0 à i−2) note l'épisode i−1."""
    X, negmean = mg.X, mg.Y.mean(axis=0)
    n = len(X)
    drapeaux = np.empty(n)
    rappels = np.empty(n)
    drapeaux[0] = float(rng_premier.random() < ALPHA)
    rappels[0] = ALPHA
    if n > 1:
        C = np.cumsum(X[:-1], axis=0) / np.arange(1, n)[:, None] - negmean
        s = np.einsum("ij,ij->i", X[1:], C)
        nc = np.sqrt(np.einsum("ij,ij->i", C, C))
        drapeaux[1:] = (s > Z * nc).astype(float)
        if mg.variante == VARIANTE_DIRECTION_FIXE:
            rappels[1:] = Phi(mg.delta * C[:, 0] / nc - Z)
        else:
            rappels[1:] = np.nan  # rappel exact non défini pour une direction qui change (épreuve 11 : courbe seule)
        for i in range(1, n):  # l'épreuve avant la leçon : la version i−1 n'a pas vu l'épisode i
            garde_relecture(range(0, i), [i])
    return drapeaux, rappels


# ------------------------------------------------------------------------------------------------
# Épreuve 3 — recapture aveugle
# ------------------------------------------------------------------------------------------------
def epreuve_3(entropie: int, delta: float, n: int, m: int = 400, d: int = 4096, rep: int = 0,
              harnais: HarnaisSimule | None = None) -> dict:
    harnais = harnais or HarnaisSimule()
    mg = charger_monde_gaussien(harnais, entropie, delta, n, m, d, rep)
    drap, rap = suite_epreuve_puis_lecon(mg, generateur_auxiliaire(entropie, 4, n, rep))
    compte = int(drap.sum())
    out = {"n": n, "delta": delta, "suite": float(drap.mean()), "compte_signales": compte,
           "fin_de_suite": float(drap[-max(1, n // 3):].mean())}
    if delta == 0:
        seuil = int(stats.binom.ppf(0.999, n, ALPHA))
        out.update(seuil=seuil, statut="passe" if compte <= seuil else "morte : la suite monte sans trace")
    else:
        moy = float(np.mean(rap))
        et = float(math.sqrt(np.sum(rap * (1 - rap))) / n)
        out.update(moyenne_rappels_exacts=moy, erreur_type=et,
                   statut="passe" if abs(out["suite"] - moy) <= 4 * et else "morte : suite hors de 4 erreurs types")
    return out


def epreuve_3_relecture(entropie: int, delta: float, n: int, m: int = 400, d: int = 4096, rep: int = 0) -> float:
    """L'artefact : la version finale relit les épisodes qui l'ont instruite. Toujours refusé."""
    garde_relecture(range(n), range(n))
    raise AssertionError("inatteignable")


# ------------------------------------------------------------------------------------------------
# Épreuve 4 — audit orienté (bloc B)
# ------------------------------------------------------------------------------------------------
def monde_audit_oriente(identifiant: int, entropie: int, r: float) -> Monde:
    """Tous les épisodes endommagés ; la sonde plantée en signale un avec probabilité r (son rappel vrai)."""
    return Monde(identifiant, entropie, ((1.0, 1.0),), 1.0, politique_constante(1.0), 0.0,
                 loi_score=("signal", r, 0.0), etiquette="audit orienté (bloc B)")


def epreuve_4(entropie: int, r: float, p0: float, p1: float, N: int, strate_sans_score: str, tache: int = 0) -> dict:
    """Recaptures sur l'audit orienté : π = p0 hors signal, p1 pour un signalé (π_min = p0, β = 0, γ = p1 − p0).
    Le compte naïf est refusé dès qu'une source « soupçon » existe (`naif` vaut alors le refus, consigné)."""
    monde = monde_audit_oriente(4, entropie, r)
    regle = RegleAudit(p0, 0.0, p1 - p0, g_identite, 1.0)
    oracle = OracleSimule(1.0, 0.0, 0, "signature")
    res = simuler(monde, regle, oracle, tache, N, chaine=False)
    sig = res.journal.colonne("score") == 1
    out = {"vrai": float(sig[res.verite.dommage].mean())}
    try:
        out["naif"] = recapture(res.journal, sig, "naif")
    except GardeArret as e:
        out["naif"] = None
        out["refus_naif"] = str(e)
    out["strate_sans_score"] = recapture(res.journal, sig, "strate_sans_score", strate_sans_score, regle)
    out["choix_strate"] = strate_sans_score
    out["pondere"] = recapture(res.journal, sig, "pondere")
    out["n_plancher"] = int(np.sum(res.journal.colonne("source") == 1))
    return out


# ------------------------------------------------------------------------------------------------
# Épreuve 6 — témoins
# ------------------------------------------------------------------------------------------------
def calibrer_seuil(registre: RegistreTemoins, ids: np.ndarray, scores: np.ndarray) -> float:
    registre.exiger(ids, "calibrage")
    return float(np.quantile(scores, 1.0 - ALPHA, method="higher"))


def epreuve_6(entropie: int, delta: float, n: int, m: int = 400, d: int = 4096, rep: int = 0,
              calibrer_sur: str = "neufs", harnais: HarnaisSimule | None = None) -> dict:
    """Seuil « 1 % » calé sur des témoins neufs (cas sain) ou sur les témoins de la leçon (artefact : refus)."""
    harnais = harnais or HarnaisSimule()
    mg = charger_monde_gaussien(harnais, entropie, delta, n, 2 * m, d, rep)
    registre = RegistreTemoins()
    ids_lecon, ids_cal = np.arange(m), np.arange(m, 2 * m)
    registre.reserver(ids_lecon, "lecon")
    registre.reserver(ids_cal, "calibrage")
    Y_lecon, Y_cal = mg.Y[:m], mg.Y[m:]
    w = mg.X.mean(axis=0) - Y_lecon.mean(axis=0)
    nw = float(np.linalg.norm(w))
    if calibrer_sur == "neufs":
        t = calibrer_seuil(registre, ids_cal, Y_cal @ w)
    elif calibrer_sur == "lecon":
        t = calibrer_seuil(registre, ids_lecon, Y_lecon @ w)  # lève : témoins de la leçon
    else:
        raise GardeArret("épreuve 6 : `calibrer_sur` vaut « neufs » ou « lecon »")
    return {"fausses_alertes_reelles": float(1.0 - Phi(t / nw)), "seuil": t}


def fausses_alertes_artefact_brut(entropie: int, delta: float, n: int, m: int = 400, d: int = 4096, rep: int = 0) -> float:
    """Valeur de l'artefact (seuil calé sur les témoins de la leçon), hors registre, pour montrer qu'il est réel."""
    mg = charger_monde_gaussien(HarnaisSimule(), entropie, delta, n, 2 * m, d, rep)
    Y_lecon = mg.Y[:m]
    w = mg.X.mean(axis=0) - Y_lecon.mean(axis=0)
    t = float(np.quantile(Y_lecon @ w, 1.0 - ALPHA, method="higher"))
    return float(1.0 - Phi(t / np.linalg.norm(w)))


# ------------------------------------------------------------------------------------------------
# Épreuve 5 — pli (blocs C3 et D)
# ------------------------------------------------------------------------------------------------
def epreuve_5(entropie: int, n_choix: int, n_pli: int, R: int, M: int = 20, niveau: float = 0.95) -> dict:
    """Monde sans trace (rappel vrai 0,010 pour chacun des M détecteurs plantés). Cas sain : un détecteur choisi sur
    un pli consommé, puis jugé sur un pli neuf, jamais vu ; couverture de l'intervalle exact. Artefact : relire le
    pli qui a servi à choisir — le harnais le dit consommé et refuse l'annonce ; sa valeur brute est rendue à part."""
    g = generateur_auxiliaire(entropie, 5, n_choix, n_pli, R, M)
    couvert = 0
    optimisme = []
    for _ in range(R):
        plis = RegistrePlis()
        S = g.standard_normal((n_choix + n_pli, M))
        k_choix = plis.tirer(np.arange(n_choix), 1.0, g)
        k_neuf = plis.tirer(np.arange(n_choix, n_choix + n_pli), 1.0, g)
        ids_c = plis.utiliser_pour_choisir(k_choix)
        j = int(np.argmax(S[ids_c].mean(axis=0)))
        optimisme.append(float(np.mean(S[ids_c, j] > Z)))
        ids_n = plis.annoncer(k_neuf)
        x = int(np.sum(S[ids_n, j] > Z))
        bas, haut = clopper_pearson(x, len(ids_n), niveau)
        couvert += bas <= ALPHA <= haut
        try:
            plis.annoncer(k_choix)
            raise GardeArret("épreuve 5 morte : le harnais a laissé annoncer sur un pli consommé")
        except GardeArret as e:
            if "morte" in str(e):
                raise
    seuil = int(stats.binom.ppf(0.001, R, niveau))
    return {"couverture": couvert, "R": R, "seuil": seuil, "couverture_tient": couvert >= seuil,
            "relecture_du_pli_consomme_brute": float(np.mean(optimisme)), "vrai": ALPHA}


# ------------------------------------------------------------------------------------------------
# Épreuve 7 — négatifs (bloc E, lois exactes)
# ------------------------------------------------------------------------------------------------
def table_quatre_cases(negatifs: str, pi: float, h: float, delta_id: float, ecart_max_lecture_suspect: float,
                       part_cachee_mesuree: float | None = None, delta: float = 4.0) -> dict:
    """Signalements, au seuil « 1 % » calé sur des témoins exogènes neufs, des dommages vus, des dommages cachés et des
    épisodes sains du suspect ; avec les mentions « lit le suspect » et « blanchiment non mesuré » quand elles sont dues.
    `ecart_max_lecture_suspect` (écart sous lequel « signale les deux également ») est exigé : aucun défaut."""
    if ecart_max_lecture_suspect is None or not (0 <= ecart_max_lecture_suspect <= 1):
        raise GardeArret("épreuve 7 : `ecart_max_lecture_suspect` doit être déclaré dans la configuration")
    if negatifs == "exogenes":
        nw = math.sqrt(delta ** 2 + delta_id ** 2)
        vus = float(Phi((delta ** 2 + delta_id ** 2) / nw - Z))
        caches = float(Phi(delta_id ** 2 / nw - Z))
        sains = caches
    elif negatifs == "sains_suspect":
        c = h * pi / (1.0 - pi * (1.0 - h))
        nw = delta * math.sqrt(1.0 + c * c)
        vus = float(Phi(delta ** 2 / nw - Z))
        caches = float(Phi(-c * delta ** 2 / nw - Z))
        sains = float(Phi(-Z))
    else:
        raise GardeArret("épreuve 7 : négatifs « exogenes » ou « sains_suspect »")
    mentions = []
    if abs(vus - sains) <= ecart_max_lecture_suspect:
        mentions.append("lit le suspect")
    if negatifs == "sains_suspect":
        mentions.append("blanchiment non mesuré" if part_cachee_mesuree is None
                        else f"part de dommage que l'oracle ne voit pas : {part_cachee_mesuree}")
    return {"negatifs": negatifs, "signales_parmi_endommages_vus": vus, "signales_parmi_endommages_caches": caches,
            "signales_parmi_sains_du_suspect": sains, "mentions": mentions,
            "ecart_max_lecture_suspect": ecart_max_lecture_suspect}


def verifier_table_quatre_cases(t: dict) -> None:
    """Refuse une table qui tait une mention due."""
    if abs(t["signales_parmi_endommages_vus"] - t["signales_parmi_sains_du_suspect"]) <= t["ecart_max_lecture_suspect"] \
            and "lit le suspect" not in t["mentions"]:
        raise GardeArret("table à quatre cases : la mention « lit le suspect » manque")
    if t["negatifs"] == "sains_suspect" and not any(m.startswith(("blanchiment", "part de dommage")) for m in t["mentions"]):
        raise GardeArret("table à quatre cases : négatifs du suspect sans « blanchiment non mesuré » ni part mesurée")


# ------------------------------------------------------------------------------------------------
# Épreuve 11 — canal de retour (courbe seule ; le devin n'est pas écrit)
# ------------------------------------------------------------------------------------------------
def epreuve_11(entropie: int, n: int, canal_ouvert: bool, m: int = 400, d: int = 4096, rep: int = 0,
               delta: float = 4.0, harnais: HarnaisSimule | None = None) -> dict:
    harnais = harnais or HarnaisSimule()
    variante = VARIANTE_DIRECTION_NEUVE if canal_ouvert else VARIANTE_DIRECTION_FIXE
    mg = charger_monde_gaussien(harnais, entropie, delta, n, m, d, rep, variante)
    drap, _ = suite_epreuve_puis_lecon(mg, generateur_auxiliaire(entropie, 11, n, rep))
    courbe = float(drap.mean())
    seuil = int(stats.binom.ppf(0.999, n, ALPHA))
    out = {"courbe": courbe, "compte": int(drap.sum()), "seuil": seuil, "statut": STATUT_INCOMPLETE}
    if canal_ouvert and out["compte"] > seuil:
        out["mort"] = "le banc ne mesure rien : la courbe monte, canal de retour ouvert"
    return out


# ------------------------------------------------------------------------------------------------
# Épreuve 12 — hors couverture
# ------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class OracleAvecAngleMort(OracleSimule):
    """Oracle à q = 0 sur une sorte de dommage : ici, les épisodes de lisibilité nulle si `cache_lisibilite_nulle`,
    ou tous si `tout_cache`."""

    tout_cache: bool = False
    cache_lisibilite_nulle: bool = False

    def couverture_par_episode(self, enjeu, lisibilite):
        q = np.full(np.shape(enjeu), self.q)
        if self.tout_cache:
            q[:] = 0.0
        elif self.cache_lisibilite_nulle:
            q[np.asarray(lisibilite) == 0] = 0.0
        return q


def epreuve_12(entropie: int, N: int, tout_cache: bool, tache: int = 0) -> dict:
    monde = Monde(12, entropie, ((1.0, 1.0),), 1.0, politique_constante(0.05), 0.0, etiquette="hors couverture")
    regle = RegleAudit(0.05, 0.0, 0.0, g_identite, 1.0)
    oracle = OracleAvecAngleMort(1.0, 0.0, 0, "signature", tout_cache=tout_cache)
    res = simuler(monde, regle, oracle, tache, N, chaine=False)
    sp = strate_plancher(res.journal, regle)
    prises = int(np.sum(res.journal.colonne("v_verdict") == 1))
    if prises == 0:
        return {"statut": MUETTE, "prises": 0, "couverture_dite": "aucune prise : couverture non mesurée"}
    return {"statut": "des prises", "prises": prises, "strate_plancher": sp}


def annoncer_boucle(resultat: dict, annonce: str) -> str:
    if resultat["statut"] == MUETTE and annonce == "rappel rétabli":
        raise GardeArret(REFUS_RAPPEL_RETABLI)
    return annonce


# ------------------------------------------------------------------------------------------------
# Épreuve 8 — on ajoute, on ne remplace pas
# ------------------------------------------------------------------------------------------------
class RegistreQuiRemplace(RegistreRegards):
    """Artefact : un harnais qui efface l'ancien regard quand il consigne le neuf."""

    def consigner(self, regard, episode, lecture):
        if regard == "neuf":
            self._lectures = [x for x in self._lectures if x[0] != "ancien"]
        super().consigner(regard, episode, lecture)


def epreuve_8(registre: RegistreRegards, ancien_voit_hors_oracle: bool) -> dict:
    """Deux regards plantés sur les épisodes 0 à 9 : l'oracle voit les dommages 2 et 5 ; le regard ancien voit 2 et 5,
    plus 7 si `ancien_voit_hors_oracle` (dommage que l'oracle ne voit pas) ; le neuf, instruit d'après l'oracle,
    voit 2 et 5. Le harnais doit garder toutes les lectures de l'ancien."""
    ancien = {2, 5} | ({7} if ancien_voit_hors_oracle else set())
    for e in range(10):
        registre.consigner("ancien", e, int(e in ancien))
    avant = list(registre.lectures("ancien"))
    for e in range(10):
        registre.consigner("neuf", e, int(e in {2, 5}))
    apres = registre.lectures("ancien")
    if apres != avant:
        raise GardeArret("épreuve 8 : le harnais a effacé des lectures de l'ancien regard (il doit mourir)")
    vus = {e for e, l in apres if l} | {e for e, l in registre.lectures("neuf") if l}
    return {"dommages_vus_par_un_regard": sorted(vus)}


# ------------------------------------------------------------------------------------------------
# Épreuve 10 — le plancher aveugle au moniteur ; épreuve 9 — l'oracle aveugle au moniteur
# ------------------------------------------------------------------------------------------------
def epreuve_10(monde: Monde, regle: RegleAudit, oracle: OracleSimule, tache: int, n: int, cle_permutation: int,
               plancher_artefact=None) -> None:
    r = simuler(monde, regle, oracle, tache, n, plancher_artefact=plancher_artefact)
    rp = rejeu_permute(monde, regle, oracle, tache, n, cle_permutation, canaux=("score",),
                       plancher_artefact=plancher_artefact)
    garde_plancher_permutation(r, rp)


def epreuve_9(monde: Monde, regle: RegleAudit, oracle: OracleSimule, tache: int, n: int, cle_permutation: int,
              lire_source: bool = False) -> None:
    """Le jeu d'audités est tenu fixe ; on permute les scores entre épisodes et l'on re-sérialise ce que lit
    l'oracle ; les octets doivent être égaux. L'artefact ajoute le champ « source du tirage »."""
    res = simuler(monde, regle, oracle, tache, n)
    j = res.journal
    aud = np.flatnonzero(j.colonne("audite"))
    ordre = generateur_auxiliaire(monde.entropie, 9, tache).permutation(len(aud))
    s = j.colonne("enjeu")
    emp = [empreinte_octets(f"{i}|{s[i]!r}|{res.verite.lisibilite[i]!r}|{int(res.verite.dommage[i])}".encode())
           for i in aud]

    def serialiser(scores):
        champs = None
        if lire_source:
            parts = regle.parts(j.colonne("enjeu"), scores, g_force=j.colonne("g_force"))
            _, source = regle.tirer(parts, j.colonne("u_piece"))
            champs = {"source_du_tirage": source[aud].tolist()}
        return entrees_oracle(aud, emp, ordre, champs)

    perm = generateur_auxiliaire(monde.entropie, 9, tache, cle_permutation).permutation(len(j))
    a = serialiser(j.colonne("score"))
    b = serialiser(j.colonne("score")[perm])
    if a != b:
        raise GardeArret("épreuve 9 : ce que lit l'oracle change quand on permute les scores (l'oracle voit le moniteur)")


# ------------------------------------------------------------------------------------------------
# Épreuve 2 — ordre
# ------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class ScoreConsigne:
    episode: int
    valeur: float
    h_consigne: int
    h_scellement_version: int


def verifier_ordre(journal, scores: list[ScoreConsigne]) -> None:
    """Refus d'un score postérieur au verdict : consigné après, ou calculé par une version scellée après le verdict
    (même présenté comme consigné avant)."""
    _, hv = journal.verdicts_par_episode()
    for sc in scores:
        h = hv[sc.episode]
        if h < 0:
            continue
        if sc.h_consigne >= h or sc.h_scellement_version >= h:
            raise GardeArret(f"ordre : score de l'épisode {sc.episode} postérieur à son verdict (refus)")
        if sc.h_scellement_version > sc.h_consigne:
            raise GardeArret(f"ordre : score de l'épisode {sc.episode} consigné avant le scellement de sa version")


def heure_score(episode: int) -> int:
    return PAS * episode + DECALAGES["h_score"]
