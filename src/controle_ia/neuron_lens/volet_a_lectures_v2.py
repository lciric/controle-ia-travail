"""Lectures du volet A de « Neuron Lens » par la lentille S et sans lentille : A1, A2, jetons de A3, cas sains — v2 (remplace la v1 après sa
contre-lecture, `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-1-code-volet-a-lot1.md`, remarques 3 et 5).

Met en œuvre la section « Métrique » A.1 (points 1 à 5), A.3 (témoins de A1 et A2) et les cas sains (i) à (iii) du « Plan d'analyse » A.1
du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`),
avec les fonctions scellées de `decisions_volet_a_v4.py` (`bff713d2…`). Aucun modèle ici : matrices de lentille, plongements, poids.

Convention : `gardes` est la liste triée des identifiants de jetons gardés (`catalog.kept`) ; les lectures se font sur ces lignes ; les
rangs sont parmi les jetons gardés. `idx_P` : positions des jetons de P **dans la liste des gardés**.

Lectures déclarées (v2) : A2 rapporte, hors condition, les ρ des témoins « sonde à étiquettes permutées » et « direction de la sonde de
C3 » ; les tirages appariés de A3 excluent les 20 jetons retirés et tirent **sans remise** à l'intérieur d'un tirage (pas de doublon dans
un ensemble de 20) ; une classe de fréquence trop petite pour cela fait échouer la course (aucun repli silencieux).
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from controle_ia.neuron_lens import decisions_volet_a_v4 as da

N_ALEATOIRES = 100


@dataclass
class LecteurCouche:
    """Lectures `_z` d'une couche : empreintes S (`K_L (W_E[v] − m)`) et sans lentille (`W_E[v] − m`) sur les jetons gardés, et leurs
    statistiques sur les 1 000 covecteurs de référence (graine de la couche, commune aux contrastes et aux découpes)."""
    F_s: np.ndarray
    F_0: np.ndarray
    stats_s: tuple = field(default=None)
    stats_0: tuple = field(default=None)

    @classmethod
    def construire(cls, E, gardes, K, graine_reference):
        F_s = da.empreintes(E, gardes, K)
        F_0 = da.empreintes(E, gardes, None)
        # une seule graine pour les deux lectures : mêmes covecteurs de référence (même dimension d)
        return cls(F_s, F_0, da.stats_reference(F_s, graine_reference), da.stats_reference(F_0, graine_reference))

    def z_s(self, w):
        return da.lecture_z(self.F_s, w, *self.stats_s)

    def z_0(self, w):
        return da.lecture_z(self.F_0, w, *self.stats_0)

    def rang_p(self, w, idx_P, sans_lentille=False):
        F, st = (self.F_0, self.stats_0) if sans_lentille else (self.F_s, self.stats_s)
        return da.meilleur_rang_deux_signes(F, w, *st, idx_P)


def directions_aleatoires(d, graine, n=N_ALEATOIRES):
    rng = np.random.default_rng(graine)
    U = rng.normal(size=(n, d))
    return U / np.linalg.norm(U, axis=1, keepdims=True)


def rangs_temoins_a1(lecteur: LecteurCouche, idx_P, U_alea, w_permutee, w_c3, sans_lentille=False):
    """102 rangs : 100 directions aléatoires, sonde à étiquettes permutées, direction de la sonde de C3 (chacun sur les deux signes)."""
    ws = list(U_alea) + [w_permutee, w_c3]
    return [lecteur.rang_p(w, idx_P, sans_lentille) for w in ws]


def mesure_a1(lecteur, idx_P, w, U_alea, w_permutee, w_c3):
    """Pour une découpe et une couche : (condition A1 pour S, rang de S, rang sans lentille, composantes rapportées)."""
    r_s = lecteur.rang_p(w, idx_P)
    r_0 = lecteur.rang_p(w, idx_P, sans_lentille=True)
    temoins = rangs_temoins_a1(lecteur, idx_P, U_alea, w_permutee, w_c3)
    cond = da.condition_a1(r_s, temoins)
    return {"condition": cond, "rang_s": r_s, "rang_sans_lentille": r_0, "s_place_p": r_s <= 10,
            "un_temoin_place_p": any(r <= 10 for r in temoins), "s_mieux_a1": r_s < r_0}


def mesure_a2(lecteur, w, poids_sac_sur_gardes, presents, U_alea, w_permutee=None, w_c3=None):
    """ρ de S et sans lentille avec les poids du sac de jetons (jetons gardés présents dans au moins 2 invites d'apprentissage) ;
    condition A2 (ρ de S au-dessus du 99ᵉ centile des 100 directions aléatoires) ; « S strictement meilleur » ; ρ (lecture S) des
    témoins « sonde permutée » et « direction de C3 », rapportés hors condition (`None` si non fournis)."""
    rho_s = da.rho_a2(lecteur.z_s(w), poids_sac_sur_gardes, presents)
    rho_0 = da.rho_a2(lecteur.z_0(w), poids_sac_sur_gardes, presents)
    rho_al = [da.rho_a2(lecteur.z_s(u), poids_sac_sur_gardes, presents) for u in U_alea]
    temoin = (lambda u: None if u is None else da.rho_a2(lecteur.z_s(u), poids_sac_sur_gardes, presents))
    return {"condition": da.condition_a2(rho_s, rho_al), "rho_s": rho_s, "rho_sans_lentille": rho_0, "s_mieux_a2": rho_s > rho_0,
            "rho_permutee": temoin(w_permutee), "rho_c3": temoin(w_c3)}


def jetons_a3(lecteur, w, gardes, k=10):
    """Les 20 jetons de la lecture S `_z` (10 premiers de +w, 10 premiers de −w), en identifiants de vocabulaire."""
    gardes = np.asarray(gardes)
    plus = np.argsort(-lecteur.z_s(w), kind="stable")[:k]
    moins = np.argsort(-lecteur.z_s(-w), kind="stable")[:k]
    return [int(gardes[i]) for i in plus] + [int(gardes[i]) for i in moins]


def tirages_apparies_a3(jetons, frequences_app, gardes, graine, n=200):
    """200 tirages de 20 jetons : chacun apparié à un jeton retiré par classe de fréquence d'apprentissage (classe « 0 » pour les absents ;
    déciles parmi les présents). `frequences_app` : dict identifiant → nombre d'invites d'apprentissage le contenant. Les jetons retirés
    sont exclus des candidats ; dans un tirage, aucun jeton n'est tiré deux fois (sans remise, classe par classe)."""
    rng = np.random.default_rng(graine)
    gardes = [int(g) for g in gardes]
    pres = np.array([frequences_app.get(g, 0) for g in gardes])
    seuils = np.quantile(pres[pres > 0], np.linspace(0, 1, 11)[1:-1]) if np.any(pres > 0) else np.array([])

    def classe(f):
        return 0 if f == 0 else 1 + int(np.searchsorted(seuils, f, side="right"))

    exclus = {int(j) for j in jetons}
    par_classe = {}
    for g, f in zip(gardes, pres):
        if g not in exclus:
            par_classe.setdefault(classe(f), []).append(g)
    besoin = {}
    for i, j in enumerate(jetons):
        besoin.setdefault(classe(frequences_app.get(int(j), 0)), []).append(i)
    for c, pos in besoin.items():
        if len(par_classe.get(c, [])) < len(pos):
            raise ValueError(f"classe de fréquence {c} : {len(par_classe.get(c, []))} candidats pour {len(pos)} jetons")
    out = []
    for _ in range(n):
        t = [0] * len(jetons)
        for c in sorted(besoin):
            pos = besoin[c]
            for i, v in zip(pos, rng.choice(par_classe[c], size=len(pos), replace=False)):
                t[i] = int(v)
        out.append(t)
    return out


def retirer(ids_texte, jetons):
    """Retrait de toutes les occurrences des jetons, sans nouvelle tokenisation."""
    s = set(jetons)
    return [t for t in ids_texte if t not in s]


# ---------------------------------------------------------------- cas sains
def forme(tok_decode, i):
    return tok_decode(int(i)).replace(" ", "").replace("Ġ", "").lower()


def cas_sain_owl(lecture_r_ecriture, gardes, tok_decode):
    """(i) : un jeton parmi les 10 premiers de la lecture R brute de l'écriture de `L8 n344 +` qui commence par « owl » ou « noct » ou vaut
    « night »."""
    top = np.asarray(gardes)[np.argsort(-np.asarray(lecture_r_ecriture), kind="stable")[:10]]
    f = [forme(tok_decode, i) for i in top]
    return any(x.startswith("owl") or x.startswith("noct") or x == "night" for x in f), f


def cas_sain_german(lecture_s_brute, gardes, tok_decode):
    """(ii) : un jeton parmi les 10 premiers de la lecture S brute de l'entrée de `L1 n11672 −` qui contient « german » ou « 德 »."""
    top = np.asarray(gardes)[np.argsort(-np.asarray(lecture_s_brute), kind="stable")[:10]]
    f = [forme(tok_decode, i) for i in top]
    return any("german" in x or "德" in x for x in f), f


def direction_lecture(a_porte, b_montee, gamma, signe, lobe_negatif):
    """Direction de lecture d'un pôle (définition de `08_reads.py`, en-tête, et `neurons.read_rows`) : lignes de porte et de montée
    multipliées par le poids de la norme d'après l'attention, normées ; `â + signe·b̂`, ou `−signe·b̂` sur le lobe négatif."""
    a = np.asarray(a_porte, float) * np.asarray(gamma, float)
    b = np.asarray(b_montee, float) * np.asarray(gamma, float)
    a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
    return (-signe * b) if lobe_negatif else (a + signe * b)


def cas_sain_synthetique(lecteur: LecteurCouche, pos_v0):
    """(iii) : `w = K_L (W_E[v0] − m)` normé place v0 au rang 1 en `_z` ; de même sans lentille avec `W_E[v0] − m`."""
    w_s = lecteur.F_s[pos_v0] / np.linalg.norm(lecteur.F_s[pos_v0])
    w_0 = lecteur.F_0[pos_v0] / np.linalg.norm(lecteur.F_0[pos_v0])
    return (int(da.rangs(lecteur.z_s(w_s))[pos_v0]) == 1, int(da.rangs(lecteur.z_0(w_0))[pos_v0]) == 1)
