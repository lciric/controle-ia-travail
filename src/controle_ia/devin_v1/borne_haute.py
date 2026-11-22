"""Pièce 8 — borne haute : couplage (spécification, section 5).

Deux branches du même état, mêmes graines, secret forcé à ses deux valeurs ; vues
comparées à l'octet. Par l'inégalité de couplage, la variation totale est au plus la
probabilité que les vues diffèrent ; zéro différence sur N paires la borne à
1 − 0,05^(1/N) (0,99 % pour N = 300, 0,10 % pour N = 3 000).

Exigences : harnais rejouable à l'octet ; horloge logique ou quantifiée vue de
l'agent ; témoin à secret identique dans les deux branches, qui doit rendre zéro
différence (sinon refus : p. ex. horloge réelle visible). La borne ne vaut que si la
vue captée est complète. L'étage 3 n'est pas couvert ici (aucun modèle ; on l'écrit).
"""
from __future__ import annotations

from typing import Callable, Hashable, Mapping, Sequence

from scipy.stats import beta

from . import RefusDevin
from .vue import Extracteur

Episode = Callable[[Hashable, Mapping[str, int]], dict]


def _octets(extracteur: Extracteur, episode: Episode, i, bits) -> bytes:
    return extracteur.extraire(episode(i, bits)).octets()


def compter_differences(episode: Episode, extracteur: Extracteur, identifiants: Sequence[Hashable],
                        source: str, bits_communs: Mapping[str, int], valeurs=(0, 1)) -> int:
    """Nombre de paires dont les vues diffèrent à l'octet, secret `source` forcé à `valeurs`."""
    if source in bits_communs:
        raise RefusDevin(f"bit {source!r} forcé et commun à la fois")
    d = 0
    for i in identifiants:
        b0 = dict(bits_communs, **{source: valeurs[0]})
        b1 = dict(bits_communs, **{source: valeurs[1]})
        d += int(_octets(extracteur, episode, i, b0) != _octets(extracteur, episode, i, b1))
    return d


def borne_superieure(differences: int, N: int, niveau: float = 0.95) -> float:
    """Borne haute de P(vues différentes) : 1 − (1 − niveau)^(1/N) à zéro différence ;
    sinon borne de Clopper-Pearson unilatérale au même niveau (choix laissé ouvert au rapport)."""
    if N <= 0 or not 0 <= differences <= N:
        raise RefusDevin("N ou nombre de différences invalide")
    if differences == 0:
        return 1 - (1 - niveau) ** (1 / N)
    if differences == N:
        return 1.0
    return float(beta.ppf(niveau, differences + 1, N - differences))


def couplage(episode: Episode, extracteur: Extracteur, identifiants: Sequence[Hashable], source: str,
             bits_communs: Mapping[str, int] | None = None, vue_complete: bool = False) -> dict:
    """Joue le témoin à secret identique puis les paires à secret forcé.

    Témoin : mêmes graines, même secret dans les deux branches ; une seule différence :
    refus (harnais non rejouable à l'octet, horloge réelle visible…).
    """
    bits_communs = dict(bits_communs or {})
    N = len(identifiants)
    if N == 0:
        raise RefusDevin("aucune paire")
    for v in (0, 1):
        t = compter_differences(episode, extracteur, identifiants, source, bits_communs, valeurs=(v, v))
        if t:
            raise RefusDevin(f"témoin à secret identique ({source} = {v}) : {t} différence(s) sur {N} ; "
                             "harnais non rejouable à l'octet (horloge réelle visible ?) : couplage refusé")
    d = compter_differences(episode, extracteur, identifiants, source, bits_communs)
    return {
        "source": source, "N": N, "differences": d, "borne_vt": borne_superieure(d, N),
        "temoin_secret_identique": "zéro différence",
        "vue_complete_declaree": bool(vue_complete),
        "portee": ("borne valable si la vue captée est complète" if vue_complete
                   else "vue captée non déclarée complète : borne non valable hors de la vue captée"),
        "etage_3": "non couvert (aucune comparaison des états internes)",
    }


def couplage_utile(chiffre_depend_d_une_fuite_petite: bool, devin_sans_rejet_au_budget: bool,
                   temoin_passe: bool, harnais_rejoue_deja: bool) -> bool:
    """Section 5, « Quand cela vaut la peine » : trois conditions réunies, ou la clause finale seule."""
    return harnais_rejoue_deja or (chiffre_depend_d_une_fuite_petite and devin_sans_rejet_au_budget and temoin_passe)
