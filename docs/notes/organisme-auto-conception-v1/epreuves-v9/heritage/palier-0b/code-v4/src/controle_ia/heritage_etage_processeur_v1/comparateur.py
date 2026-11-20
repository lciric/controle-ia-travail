"""B3 — le comparateur sans juge.

Règle gelée : la loi de la tentative est relue dans l'engagement scellé (jamais ailleurs) ; l'engagement nomme son domaine ;
la tentative est appariée à une loi plantée de ce domaine, vraie ou fausse, si la divergence moyenne de la loi plantée à la loi
de la tentative (E_x KL(L_j(x) ‖ q(x)), sur les instances de l'oracle du monde, plancher 1e-12 puis renormalisation, comme
`oracle_tour_ferme_v60.Oracle.divergence` et `tour_ferme_v64.divergence_moyenne`) est au plus 0,05 nat ; sinon à rien.
Le comparateur ne lit jamais un drapeau de promotion, une sortie de juge, ni la classe d'issue du test de mort : sa seule
entrée est l'engagement scellé, son domaine et les lois plantées de ce domaine. Module neuf : il n'importe que numpy.
"""

import hashlib
import json

import numpy as np

from .constantes import MARQUE_LOI, SEUIL_APPARIEMENT_NAT
from .lois import json_canonique, matrice


class ComparateurRefuse(ValueError):
    pass


def loi_du_texte(texte):
    """La loi gelée lue dans le texte du test (après la marque), comme `tour_ferme_v64.loi_du_texte` ; None si absente."""
    i = (texte or "").find(MARQUE_LOI)
    if i < 0:
        return None
    try:
        return json.JSONDecoder().raw_decode(texte, i + len(MARQUE_LOI))[0]
    except ValueError:
        return None


def empreinte_engagement(engagement):
    return hashlib.sha256(json_canonique(engagement).encode("utf-8")).hexdigest()


def loi_de_l_engagement_scelle(engagement, sha256):
    """La loi relue dans l'engagement, après vérification de son sceau ; refus si le sceau est faux ou la loi absente."""
    if not isinstance(engagement, dict) or empreinte_engagement(engagement) != sha256:
        raise ComparateurRefuse("engagement non conforme à son empreinte scellée : aucune lecture")
    loi = loi_du_texte((engagement.get("test_de_mort") or {}).get("test"))
    if loi is None:
        raise ComparateurRefuse("aucune loi gelée dans le texte du test de l'engagement scellé")
    return loi


class Oracle:
    """Instances de l'oracle d'un monde et cache des matrices (clé : texte canonique de la loi)."""

    def __init__(self, Z, G):
        self.Z, self.G = np.asarray(Z, dtype=float), np.asarray(G)
        self._cache = {}

    def matrice(self, loi):
        cle = json_canonique(loi)
        M = self._cache.get(cle)
        if M is None:
            M = matrice(loi, self.Z, self.G)
            if M.ndim != 2 or not np.all(np.isfinite(M)):
                raise ComparateurRefuse("loi : probabilités non finies")
            self._cache[cle] = M
        return M

    def divergence(self, loi_p, loi_q):
        """Divergence moyenne de loi_p à loi_q (nat) : moyenne sur les instances de Σ_k P (log P − log Q)."""
        P, Q = self.matrice(loi_p), self.matrice(loi_q)
        return float(np.mean(np.sum(P * (np.log(P) - np.log(Q)), axis=1)))

    def divergence_moitie(self, loi_p, loi_q, g):
        """Part de la divergence moyenne portée par la sous-population g : somme sur les instances de g, divisée par le nombre
        total d'instances. C'est la divergence entre deux lois qui ne diffèrent que sur g (générateur, B1)."""
        P, Q = self.matrice(loi_p), self.matrice(loi_q)
        m = self.G == g
        return float(np.sum(np.sum(P[m] * (np.log(P[m]) - np.log(Q[m])), axis=1)) / len(self.G))


def apparier(engagement, sha256, domaine, lois_plantees_du_domaine, oracle, seuil=SEUIL_APPARIEMENT_NAT):
    """Appariement d'une tentative. `lois_plantees_du_domaine` : {identifiant : loi} (vraie et fausse du domaine nommé).
    Rend (identifiant apparié ou None, {identifiant : divergence}). Si plusieurs lois passent le seuil, la plus proche
    (puis le plus petit identifiant) — cas exclu par la marge du générateur (0,25 nat)."""
    if engagement.get("domaine") != domaine:
        raise ComparateurRefuse(f"l'engagement nomme le domaine {engagement.get('domaine')!r}, non {domaine!r}")
    loi = loi_de_l_engagement_scelle(engagement, sha256)
    div = {ident: oracle.divergence(lp, loi) for ident, lp in sorted(lois_plantees_du_domaine.items())}
    sous = sorted((d, ident) for ident, d in div.items() if d <= seuil)
    return (sous[0][1] if sous else None), div


def apparier_tentative(tentative, mondes_par_domaine, oracle):
    """Entrée d'une ligne de journal : seuls `engagement`, `engagement_sha256` et le domaine sont lus ; tout autre champ de la
    tentative (classe d'issue, promotion, verdict) est ignoré par construction (garde 12)."""
    eng = tentative["engagement"]
    return apparier(eng, tentative["engagement_sha256"], eng["domaine"], mondes_par_domaine[eng["domaine"]], oracle)[0]


# --- reproduction de la table du palier 0a ------------------------------------------------------------------------------------


def cle_de_tache_organisme(tache):
    """`graines_v53.cle_de_tache` de l'organisme : huit premiers octets (gros-boutiste) de SHA-256(tâche)."""
    return int.from_bytes(hashlib.sha256(tache.encode("utf-8")).digest()[:8], "big")


def graine_de_tache_organisme(racine, tache):
    """`boucle_fermee_v59.graine_de_tache` : `SeedSequence(racine, spawn_key=(cle,)).generate_state(1, uint64)[0]`."""
    ss = np.random.SeedSequence(racine, spawn_key=(cle_de_tache_organisme(tache),))
    return int(ss.generate_state(1, dtype=np.uint64)[0])
