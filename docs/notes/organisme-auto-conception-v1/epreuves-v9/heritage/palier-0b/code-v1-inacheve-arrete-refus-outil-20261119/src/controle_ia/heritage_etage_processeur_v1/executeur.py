"""B4, B5 — l'exécuteur simulé du test de mort, la forme imposée des engagements, les échecs de l'expérimentateur.

Ce que l'exécuteur reproduit (plan, § 3.0) : un engagement scellé par son empreinte avant toute exécution ; une statistique
calculée sur la seule tranche d'épreuve du monde en cours ; une comparaison au seuil scellé, sans arrondi ; trois classes et
le statut « non éprouvée (budget) » (porté par l'enveloppe) ; `gardee` vaut oui si et seulement si la classe est « tient ».

Forme imposée (tour fermé de l'organisme) : `texte_du_test` et `test_de_mort_impose` sont recopiés à l'octet de
`tour_ferme_v64.py` (l. 450-466) ; l'essai d'accord avec l'organisme le vérifie. La statistique est celle de
`evaluateur_lois_v62.gains` : gain de log-score par épisode sur la marginale empirique de la tranche (comptes + 0,5).

`ecrire_champs_programme` est la fonction d'écriture de l'invariant (plan, § 3.1) : ses seules entrées sont l'engagement scellé,
la tranche d'épreuve, le fichier brut de l'exécution (None si l'expérimentateur n'a rendu aucune exécution réussie) et le
journal des coûts. `contre_calcul` est la garde 16 (script qui fabrique ses lignes).
"""

import math
import re

import numpy as np

from .comparateur import empreinte_engagement, loi_de_l_engagement_scelle
from .constantes import (FICHIER_EVALUATEUR, MARQUE_LOI, NE_TIENT_PAS, NOMBRE_ISSUES, NON_EXECUTABLE, PLANCHER, SEUIL_SENS,
                         SEUIL_TEST, SEUIL_VALEUR, TIENT)
from .lois import json_canonique, matrice, proba

TOLERANCE_CONTRE_CALCUL = 1e-9


class ArretExecuteur(RuntimeError):
    pass


# --- forme imposée (recopiée de tour_ferme_v64) ----------------------------------------------------------------------------


def texte_du_test(loi):
    return ("Gain moyen par épisode du log-score de la loi gelée L sur la marginale empirique de la tranche (comptes + 0,5 ; nat), "
            f"calculé sur episodes.csv par l'évaluateur de référence {FICHIER_EVALUATEUR} (même fichier pour toutes les fiches). "
            "gains.csv : colonnes episode, gain ; une ligne par épisode ; valeurs en pleine précision (repr de Python), jamais "
            f"arrondies. Script attendu, tel quel : import json, runpy ; ev = runpy.run_path('tranche/{FICHIER_EVALUATEUR}') ; "
            "ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv') ; où LOI est le texte JSON de L ci-dessous, "
            "recopié exactement. " + MARQUE_LOI + json_canonique(loi))


def test_de_mort_impose(loi, seuil=SEUIL_TEST):
    return {"seuil": seuil, "donnees": ["episodes.csv", FICHIER_EVALUATEUR], "test": texte_du_test(loi),
            "statistique": {"fichier": "gains.csv", "colonne": "gain", "statistique": "moyenne"}}


def engagement(domaine, loi, seuil=SEUIL_TEST):
    """L'engagement d'une tentative : le domaine visé et le champ de test à la forme imposée."""
    return {"domaine": domaine, "test_de_mort": test_de_mort_impose(loi, seuil)}


def sceller(engagement_):
    return empreinte_engagement(engagement_)


# --- seuil lu dans une phrase (tests_de_mort_v2.lire_seuil, recopié) ---------------------------------------------------------

NOMBRE = re.compile(r"[-+]?(?:\d+(?:[.,]\d+)?|[.,]\d+)(?:[eE][-+]?\d+)?")
COMPARATEURS = (
    (re.compile(r"≥|>=|⩾|\bau moins\b|\bsupérieur(?:e)? ou égal|\bgreater or equal|\bat least\b", re.I), "≥"),
    (re.compile(r"≤|<=|⩽|\bau plus\b|\binférieur(?:e)? ou égal|\bless or equal|\bat most\b", re.I), "≤"),
    (re.compile(r">|\bstrictement supérieur|\bplus grand que\b|\bplus de\b|\bgreater than\b", re.I), ">"),
    (re.compile(r"<|\bstrictement inférieur|\bplus petit que\b|\bmoins de\b|\bless than\b", re.I), "<"),
)
COMPARATEUR_PAR_SIGNE = {"+": "≥", "-": "≤", "0": "|x| ≤"}


def _normaliser_signes(texte):
    return texte.replace("−", "-").replace("–", "-")


def nombre_dans(texte, a_partir_de=0):
    if not isinstance(texte, str):
        return None
    m = NOMBRE.search(_normaliser_signes(texte), a_partir_de)
    if not m:
        return None
    try:
        v = float(m.group(0).replace(",", "."))
    except ValueError:
        return None
    return v if math.isfinite(v) else None


def lire_seuil(texte_seuil, signe="+"):
    if not isinstance(texte_seuil, str):
        return None, None
    texte = _normaliser_signes(texte_seuil)
    trouves = []
    for motif, comparateur in COMPARATEURS:
        m = motif.search(texte)
        if m:
            trouves.append((m.start(), -(m.end() - m.start()), comparateur, m.end()))
    if trouves:
        _, _, comparateur, fin = min(trouves)
        valeur = nombre_dans(texte, fin)
        if valeur is None:
            valeur = nombre_dans(texte)
    else:
        comparateur, valeur = COMPARATEUR_PAR_SIGNE.get(signe), nombre_dans(texte)
    return valeur, comparateur


def comparer(valeur, comparateur, seuil):
    return {"≥": valeur >= seuil, "≤": valeur <= seuil, ">": valeur > seuil, "<": valeur < seuil,
            "|x| ≤": abs(valeur) <= seuil}[comparateur]


def verifier_seuil_scelle(engagement_, voulu=(SEUIL_VALEUR, SEUIL_SENS)):
    """Garde 15 : le seuil relu dans la phrase scellée (valeur et sens) est celui que l'enveloppe voulait ; sinon arrêt."""
    lu = lire_seuil(engagement_["test_de_mort"]["seuil"])
    if lu != tuple(voulu):
        raise ArretExecuteur(f"garde 15 : seuil scellé relu {lu}, voulu {tuple(voulu)} : arrêt")
    return lu


# --- statistique ---------------------------------------------------------------------------------------------------------------


def marginale_empirique(y):
    comptes = np.full(NOMBRE_ISSUES, 0.5)
    np.add.at(comptes, np.asarray(y, dtype=np.int64), 1.0)
    return comptes / comptes.sum()


def gains_evaluateur(loi, Z, G, y):
    """`evaluateur_lois_v62.gains`, vectorisé : log max(p_y, 1e-12) − log marg_y, épisode par épisode."""
    y = np.asarray(y, dtype=np.int64)
    P = matrice(loi, Z, G)
    marg = marginale_empirique(y)
    return np.log(np.maximum(P[np.arange(len(y)), y], PLANCHER)) - np.log(marg[y])


def statistique_moyenne(loi, Z, G, y):
    g = gains_evaluateur(loi, Z, G, y)
    return math.fsum(g.tolist()) / len(g)


def fichier_brut(gains):
    """Le fichier brut `gains.csv` (episode, gain ; pleine précision), comme `evaluateur_lois_v62.ecrire_gains`."""
    return ("episode,gain\n" + "".join("%d,%r\n" % (i, float(x)) for i, x in enumerate(gains, 1))).encode("utf-8")


def lire_fichier_brut(octets):
    lignes = octets.decode("utf-8").splitlines()
    if not lignes or lignes[0] != "episode,gain":
        raise ArretExecuteur("fichier brut sans l'en-tête attendu")
    valeurs = [float(l.split(",")[1]) for l in lignes[1:] if l.strip()]
    if not valeurs or not all(math.isfinite(v) for v in valeurs):
        raise ArretExecuteur("fichier brut vide ou non fini")
    return valeurs


def script_fidele(loi, tranche):
    return fichier_brut(gains_evaluateur(loi, tranche["Z"], tranche["G"], tranche["y"]))


def script_fabrique(loi, tranche):
    """Artefact de la garde 16 : un script qui écrit un gain constant (0,5) au lieu de le calculer."""
    return fichier_brut([0.5] * len(tranche["y"]))


def contre_calcul(loi, tranche):
    """Garde 16 : la statistique recalculée hors du script, instance par instance (`proba`, indépendant de `matrice`)."""
    Z, G, y = tranche["Z"], tranche["G"], tranche["y"]
    comptes = [0.5] * NOMBRE_ISSUES
    for v in y:
        comptes[int(v)] += 1
    s = sum(comptes)
    marg = [c / s for c in comptes]
    g = []
    for z, gg, v in zip(Z.tolist(), G.tolist(), y.tolist()):
        p = proba(loi, {"z": z, "g": int(gg)})
        g.append(math.log(max(p[v], 1e-12)) - math.log(marg[v]))
    return math.fsum(g) / len(g)


# --- la fonction d'écriture de l'invariant ------------------------------------------------------------------------------------


def ecrire_champs_programme(engagement_scelle, engagement_sha256, tranche_epreuve, fichier_brut_octets, journal_couts):
    """Rend (resultat, gardee). Entrées : l'engagement scellé (et son empreinte), la tranche d'épreuve, le fichier brut (None :
    aucune exécution réussie), le journal des coûts ({"cout_usd": …}). Rien d'autre n'est lu."""
    loi = loi_de_l_engagement_scelle(engagement_scelle, engagement_sha256)
    cout = float(journal_couts["cout_usd"])
    if fichier_brut_octets is None:
        return {"classe": NON_EXECUTABLE, "cout_usd": cout}, False
    try:
        valeurs = lire_fichier_brut(fichier_brut_octets)
    except ArretExecuteur:
        return {"classe": NON_EXECUTABLE, "cout_usd": cout}, False
    valeur = math.fsum(valeurs) / len(valeurs)
    seuil, comparateur = lire_seuil(engagement_scelle["test_de_mort"]["seuil"])
    if seuil is None or comparateur is None:
        return {"classe": NON_EXECUTABLE, "cout_usd": cout}, False
    mienne = contre_calcul(loi, tranche_epreuve)
    if abs(mienne - valeur) > TOLERANCE_CONTRE_CALCUL:
        raise ArretExecuteur(f"garde 16 : contre-calcul en désaccord avec le noyau ({valeur!r} contre {mienne!r}) : arrêt, "
                             "aucune issue lue")
    classe = TIENT if comparer(valeur, comparateur, seuil) else NE_TIENT_PAS
    return {"classe": classe, "cout_usd": cout}, classe == TIENT


class Executeur:
    """Exécuteur simulé. `script` : `script_fidele` (défaut) ou l'artefact `script_fabrique` ; `sens_inverse` : artefact de la
    garde 17 (seuil comparé dans l'autre sens) ; `toujours_tient` : artefact de la garde 24."""

    def __init__(self, script=script_fidele, sens_inverse=False, toujours_tient=False):
        self.script, self.sens_inverse, self.toujours_tient = script, sens_inverse, toujours_tient

    def classe_sans_echec(self, loi, tranche):
        """La comparaison au seuil, sans le tirage d'échec (mesure M12 par loi)."""
        if self.toujours_tient:
            return TIENT
        v = statistique_moyenne(loi, tranche["Z"], tranche["G"], tranche["y"])
        ok = v >= SEUIL_VALEUR
        if self.sens_inverse:
            ok = v <= SEUIL_VALEUR
        return TIENT if ok else NE_TIENT_PAS

    def eprouver(self, engagement_scelle, engagement_sha256, prediction_sha256, tranche, echec_experimentateur, cout_usd):
        if not prediction_sha256:
            raise ArretExecuteur("garde 3 : tentative sans empreinte de prédiction : refus d'éprouver")
        if empreinte_engagement(engagement_scelle) != engagement_sha256:
            raise ArretExecuteur("engagement non scellé ou modifié : refus d'éprouver")
        loi = loi_de_l_engagement_scelle(engagement_scelle, engagement_sha256)
        if self.toujours_tient or self.sens_inverse:
            classe = NON_EXECUTABLE if echec_experimentateur else self.classe_sans_echec(loi, tranche)
            return {"classe": classe, "cout_usd": float(cout_usd)}, classe == TIENT
        brut = None if echec_experimentateur else self.script(loi, tranche)
        return ecrire_champs_programme(engagement_scelle, engagement_sha256, tranche, brut, {"cout_usd": cout_usd})
