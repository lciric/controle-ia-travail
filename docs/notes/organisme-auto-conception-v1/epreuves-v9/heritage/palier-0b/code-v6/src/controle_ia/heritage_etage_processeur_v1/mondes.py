"""B1 — les mondes plantés de l'héritage (code neuf : l'organisme n'en a pas), leur partage, le générateur constructif.

Contrat gelé (préenregistrement v6, B1) : un monde est une suite de seize domaines ; 400 épisodes par domaine, deux traits
N(0 ; 1) arrondis à six décimales, une sous-population à pile ou face. Monde cible : douze domaines à loi vraie plantée, quatre
sans structure (loi fixe, ni plantée ni engagée). Monde source : huit à loi vraie, huit sans structure. Une loi fausse par
domaine à loi vraie (douze par monde cible, huit par monde source) : elle reprend la loi vraie sur une sous-population tirée à
pile ou face et reçoit une sous-loi neuve sur l'autre. Dose ρ : 0, 3 ou 6 lois dépendantes par monde cible, monde final
compris, chacune composée de deux lois vraies distinctes de la source (la loi de plus petit rang sur la première
sous-population, l'autre sur la seconde ; rang = ordre du domaine), paires tirées sans remise parmi les vingt-huit, sur les
quatre mondes cibles d'une source.

Forme unique (version 4) : toute loi plantée est `par_sous_population` de deux `softmax` (poids N(0 ; 1,5), biais N(0 ; 0,3),
six décimales). Générateur constructif (version 4) : marges construites loi par loi à 0,30 nat ; (a) source : huit sous-lois
par sous-population, chacune retirée tant qu'elle n'est pas à 0,30 nat de toutes les précédentes sur la part de la divergence
moyenne que porte cette sous-population ; (b) dépendantes composées sans tirage ; (c) indépendantes : deux sous-lois retirées
ensemble tant que la loi entière n'est pas à 0,30 nat de toute loi déjà posée ; (d) fausses : la sous-loi neuve retirée tant que
la loi fausse n'est pas à 0,30 nat de toute loi déjà posée, sa loi vraie comprise ; (e) les vingt-huit compositions de la
source à 0,25 nat de chaque loi vraie de la source, sinon le monde source est retiré. Bornes gelées : 400 tirages par loi,
200 essais par monde, 200 tours par suite ; au-delà, arrêt « bornes de la construction épuisées » (liste d'arrêt, point 2).
B7 bis (version 4) : pour les sources du bras de diagnostic, les indépendantes et les fausses sont aussi tirées à 0,30 nat des
lois vraies de la source étrangère et de leurs compositions, dans les deux sens.

L'audit (module `audit`, écriture à part) juge le produit fini à 0,25 nat ; un monde qui manque une marge par une loi autre
qu'une dépendante est rejeté et retiré ; un monde cible que seules ses lois dépendantes font échouer fait retirer la suite.

Code v5 (préenregistrement v11) : à l'étape 3, les plis de la lecture observée sont tirés par un générateur que le code de
l'étape dérive lui-même (couche « audit », famille « audit », rôle « plis »), distinct de celui des permutations (rôle
« permutation ») ; l'appelant n'en donne aucun (« Ce qui demande un code v5 », point 3). Au jeu à sources étrangères (garde 27),
chaque suite garde la source face à laquelle la marge de ses mondes cibles est construite (`etrangere`), et la construction
arrête si ce n'est pas la source suivante (point 5 ; trois sources, version 10).
"""

import itertools
import os

import numpy as np

from . import audit as AU
from .comparateur import Oracle
from .constantes import (DOMAINES_A_LOI_CIBLE, DOMAINES_A_LOI_SOURCE, DOMAINES_PAR_MONDE, DOSE_JEU_GARDE_27, EPISODES_PAR_DOMAINE,
                         ESSAIS_PAR_MONDE, INSTANCES_ORACLE, MARGE_DE_CONSTRUCTION_NAT, MARGE_NAT, MONDES_CIBLES_D_EVOLUTION,
                         PERMUTATIONS_AUDIT, PROPORTION_TRANCHE, SEUIL_APPARIEMENT_NAT, TIRAGES_PAR_LOI, TOURS_PAR_SUITE)
from .lois import (composer, instances_oracle, json_canonique, loi_fixe, loi_par_sous_population, matrice, softmax_aleatoire,
                   sous_loi, tirer_issues)

PAIRES_DE_LA_SOURCE = list(itertools.combinations(range(DOMAINES_A_LOI_SOURCE), 2))  # 28 paires de rangs
SORTES = ("sous-loi-source", "independante", "fausse-source", "fausse-cible")
# rôles d'étiquette des deux générateurs de l'audit de présentation (section « Seuil », version 9 ; code v5, point 3) ; le nom
# du rôle « plis » est une valeur du rédacteur
ROLE_PLIS = "plis"
ROLE_PERMUTATION = "permutation"


class ArretGenerateur(RuntimeError):
    pass


class Bornes:
    """Bornes gelées de la construction (B1) ; l'artefact de la garde 25 les ramène à un tirage et un essai."""

    def __init__(self, tirages_par_loi=TIRAGES_PAR_LOI, essais_par_monde=ESSAIS_PAR_MONDE, tours_par_suite=TOURS_PAR_SUITE):
        self.tirages_par_loi, self.essais_par_monde, self.tours_par_suite = tirages_par_loi, essais_par_monde, tours_par_suite


BORNES_GELEES = Bornes()


class Compteurs:
    """Ce que B1 (iii) fait rapporter : par sorte de loi, tirages tentés et acceptés ; par niveau, essais de monde abandonnés
    et tours de suite ; mondes rejetés par l'audit."""

    def __init__(self):
        self.tirages = {s: [0, 0] for s in SORTES}
        self.essais_abandonnes = {"source": 0, "cible": 0}
        self.rejets_audit = {"source": 0, "cible": 0}
        self.tours = 0

    def vers_dict(self):
        return {"tirages_tentes_acceptes": {s: list(v) for s, v in self.tirages.items()},
                "essais_abandonnes": dict(self.essais_abandonnes), "rejets_par_l_audit": dict(self.rejets_audit),
                "tours_de_suite_retires": self.tours}

    def ajouter(self, autre):
        for s in SORTES:
            for i in (0, 1):
                self.tirages[s][i] += autre.tirages[s][i]
        for k in ("source", "cible"):
            self.essais_abandonnes[k] += autre.essais_abandonnes[k]
            self.rejets_audit[k] += autre.rejets_audit[k]
        self.tours += autre.tours


def nom_domaine(i):
    return f"D{i:02d}"


def nombre_de_dependantes(dose):
    d = {0.0: 0, 0.25: 3, 0.5: 6}.get(float(dose))
    if d is None:
        raise ArretGenerateur(f"dose hors de la grille : {dose!r}")
    return d


class Monde:
    """Un monde : domaines, lois plantées (clé), épisodes partagés en part servie et tranche d'épreuve, instances de l'oracle."""

    def __init__(self, nom, role, dose):
        self.nom, self.role, self.dose = nom, role, dose
        self.domaines = []  # dicts : nom, loi_generatrice, vraie, fausse, Z, G, y, servi, epreuve
        self.lois = {}  # identifiant -> {loi, type, dependante, paire, domaine, rang, texte}
        self.oracle = None

    def lois_du_domaine(self, nom):
        return {i: l["loi"] for i, l in self.lois.items() if l["domaine"] == nom}

    def vraies(self):
        return sorted(i for i, l in self.lois.items() if l["type"] == "vraie")

    def fausses(self):
        return sorted(i for i, l in self.lois.items() if l["type"] == "fausse")

    def vraies_par_rang(self):
        return [self.lois[i]["loi"] for i in sorted(self.vraies(), key=lambda i: self.lois[i]["rang"])]

    def domaine(self, nom):
        for d in self.domaines:
            if d["nom"] == nom:
                return d
        raise KeyError(nom)

    def part_servie(self, nom):
        d = self.domaine(nom)
        return {"Z": d["Z"][d["servi"]], "G": d["G"][d["servi"]], "y": d["y"][d["servi"]], "episodes": d["servi"] + 1}

    def tranche_epreuve(self, nom):
        d = self.domaine(nom)
        return {"Z": d["Z"][d["epreuve"]], "G": d["G"][d["epreuve"]], "y": d["y"][d["epreuve"]], "episodes": d["epreuve"] + 1}

    def cle(self):
        """La clé du monde (lois plantées), sous forme sérialisable — jamais servie à un proposeur ni écrite au registre."""
        return {i: {k: l[k] for k in ("loi", "type", "dependante", "domaine")} for i, l in sorted(self.lois.items())}


def _sep(oracle, a, b):
    return min(oracle.divergence(a, b), oracle.divergence(b, a))


def _sep_moitie(oracle, a, b, g):
    return min(oracle.divergence_moitie(a, b, g), oracle.divergence_moitie(b, a, g))


def _episodes(loi, rng, n=EPISODES_PAR_DOMAINE):
    Z = np.round(rng.normal(0.0, 1.0, (n, 2)), 6)
    G = rng.integers(0, 2, n)
    y = tirer_issues(matrice(loi, Z, G), rng)
    return Z, G, y


def _partager(n, rng):
    perm = rng.permutation(n)
    k = int(round(n * (1 - PROPORTION_TRANCHE)))
    return np.sort(perm[:k]), np.sort(perm[k:])


def _compter(compteurs, sorte, tentes, accepte):
    compteurs.tirages[sorte][0] += tentes
    compteurs.tirages[sorte][1] += int(accepte)


def _sous_lois_separees(rng, oracle, nombre, g, bornes, compteurs):
    """B1 (a) : `nombre` sous-lois tirées une à une, chacune retirée (400 tirages au plus) tant qu'elle n'est pas à 0,30 nat de
    toutes les précédentes sur la part de la divergence que porte la sous-population g. None si une borne est épuisée."""
    out = []
    for _ in range(nombre):
        for t in range(1, bornes.tirages_par_loi + 1):
            c = softmax_aleatoire(rng)
            if all(_sep_moitie(oracle, c, x, g) >= MARGE_DE_CONSTRUCTION_NAT for x in out):
                out.append(c)
                _compter(compteurs, "sous-loi-source", t, True)
                break
        else:
            _compter(compteurs, "sous-loi-source", bornes.tirages_par_loi, False)
            return None
    return out


def _loi_fausse(loi_vraie, rng, oracle, deja, bornes, compteurs, sorte):
    """B1 (d) : la demi-vérité ; la sous-loi neuve est retirée tant que la loi fausse n'est pas à 0,30 nat de toute loi déjà
    posée, sa loi vraie comprise."""
    garde = int(rng.integers(0, 2))
    for t in range(1, bornes.tirages_par_loi + 1):
        autre = softmax_aleatoire(rng)
        f = (loi_par_sous_population(sous_loi(loi_vraie, 0), autre) if garde == 0
             else loi_par_sous_population(autre, sous_loi(loi_vraie, 1)))
        if all(_sep(oracle, f, x) >= MARGE_DE_CONSTRUCTION_NAT for x in deja + [loi_vraie]):
            _compter(compteurs, sorte, t, True)
            return f
    _compter(compteurs, sorte, bornes.tirages_par_loi, False)
    return None


def _loi_independante(rng, oracle, deja, bornes, compteurs):
    """B1 (c) : deux sous-lois neuves retirées ensemble tant que la loi entière n'est pas à 0,30 nat de toute loi posée."""
    for t in range(1, bornes.tirages_par_loi + 1):
        loi = loi_par_sous_population(softmax_aleatoire(rng), softmax_aleatoire(rng))
        if all(_sep(oracle, loi, x) >= MARGE_DE_CONSTRUCTION_NAT for x in deja):
            _compter(compteurs, "independante", t, True)
            return loi
    _compter(compteurs, "independante", bornes.tirages_par_loi, False)
    return None


def candidates_etrangeres(etrangere):
    """B7 bis : lois vraies de la source étrangère et leurs compositions deux à deux, dans les deux sens (64 lois)."""
    v = etrangere.vraies_par_rang()
    return v + [composer(v[p], v[q]) for p in range(len(v)) for q in range(len(v)) if p != q]


def _remplir(monde, graines, base, nom_monde, essai, oracle, vraies, fausses, variante=None):
    """Domaines, épisodes et partage. `vraies` : {indice : (loi, dependante, paire, rang)} ; `fausses` : {indice : loi}."""
    monde.oracle = oracle
    rng_ep = graines.g(**base, monde=nom_monde, role="episodes", essai=essai)
    rng_pa = graines.g(**base, monde=nom_monde, role="partage", essai=essai)
    for i in range(DOMAINES_PAR_MONDE):
        nom = nom_domaine(i)
        d = {"nom": nom, "vraie": None, "fausse": None}
        if i in vraies:
            loi, dep, paire, rang = vraies[i]
            fausse = fausses[i]
            if variante == "dose-inscrite":
                loi, fausse = dict(loi, note=f"dose {monde.dose}"), dict(fausse, note=f"dose {monde.dose}")
            iv, i_f = f"{monde.nom}:{nom}:V", f"{monde.nom}:{nom}:F"
            monde.lois[iv] = {"loi": loi, "type": "vraie", "dependante": dep, "paire": paire, "domaine": nom, "rang": rang,
                              "texte": json_canonique(loi)}
            monde.lois[i_f] = {"loi": fausse, "type": "fausse", "dependante": False, "paire": None, "domaine": nom, "rang": None,
                               "texte": json_canonique(fausse)}
            d.update(vraie=iv, fausse=i_f, loi_generatrice=loi)
        else:
            d["loi_generatrice"] = loi_fixe(rng_ep)
        d["Z"], d["G"], d["y"] = _episodes(d["loi_generatrice"], rng_ep)
        d["servi"], d["epreuve"] = _partager(len(d["y"]), rng_pa)
        monde.domaines.append(d)
    return monde


def _oracle(graines, base, nom_monde, essai):
    return Oracle(*instances_oracle(graines.e(**base, monde=nom_monde, role="oracle-instances", essai=essai), INSTANCES_ORACLE))


def generer_source(graines, base, dose, bornes=BORNES_GELEES, compteurs=None, variante=None):
    compteurs = compteurs or Compteurs()
    for essai in range(bornes.essais_par_monde):
        rng = graines.g(**base, monde="source", role="monde", essai=essai)
        m = Monde(f"{_prefixe(base)}source", "source", dose)
        oracle = _oracle(graines, base, "source", essai)
        domaines = sorted(rng.choice(DOMAINES_PAR_MONDE, DOMAINES_A_LOI_SOURCE, replace=False).tolist())
        s0 = _sous_lois_separees(rng, oracle, DOMAINES_A_LOI_SOURCE, 0, bornes, compteurs)
        s1 = _sous_lois_separees(rng, oracle, DOMAINES_A_LOI_SOURCE, 1, bornes, compteurs) if s0 else None
        if s1 is None:
            compteurs.essais_abandonnes["source"] += 1
            continue
        vraies = {i: (loi_par_sous_population(s0[r], s1[r]), False, None, r) for r, i in enumerate(domaines)}
        deja = [v[0] for v in vraies.values()]
        fausses = {}
        for i in domaines:
            f = _loi_fausse(vraies[i][0], rng, oracle, deja, bornes, compteurs, "fausse-source")
            if f is None:
                break
            fausses[i] = f
            deja.append(f)
        if len(fausses) < len(domaines):
            compteurs.essais_abandonnes["source"] += 1
            continue
        lois_rang = [vraies[i][0] for i in domaines]
        if any(_sep(oracle, composer(lois_rang[p], lois_rang[q]), lois_rang[r]) < MARGE_NAT
               for p, q in PAIRES_DE_LA_SOURCE for r in range(DOMAINES_A_LOI_SOURCE)):
            compteurs.essais_abandonnes["source"] += 1  # B1 (e) : le monde source est retiré
            continue
        _remplir(m, graines, base, "source", essai, oracle, vraies, fausses, variante)
        manques = (AU.audit_marges({i: l["loi"] for i, l in m.lois.items()}, oracle.Z, oracle.G)
                   + AU.audit_compositions_de_la_source(m.vraies_par_rang(), oracle.Z, oracle.G))
        if manques and variante is None:
            compteurs.rejets_audit["source"] += 1
            continue
        return m, essai
    raise ArretGenerateur("bornes de la construction épuisées : monde source, "
                          f"{bornes.essais_par_monde} essais (liste d'arrêt, point 2)")


def _prefixe(base):
    return "s" + str(base.get("source", "x")) + "-"


def tirer_paires(rng, dose):
    d = nombre_de_dependantes(dose)
    perm = rng.permutation(len(PAIRES_DE_LA_SOURCE))[: d * (MONDES_CIBLES_D_EVOLUTION + 1)]
    paires = [PAIRES_DE_LA_SOURCE[i] for i in perm]
    return [paires[k * d:(k + 1) * d] for k in range(MONDES_CIBLES_D_EVOLUTION + 1)]


def generer_cible(graines, base, source, nom_monde, paires, dose, bornes=BORNES_GELEES, compteurs=None, etrangere=None,
                  variante=None, faute=None):
    """Rend (monde, essai, manques) ; monde None si seules des lois dépendantes manquent leur marge (la suite est à retirer)."""
    compteurs = compteurs or Compteurs()
    lois_rang = source.vraies_par_rang()
    extra = candidates_etrangeres(etrangere) if etrangere is not None else []
    for essai in range(bornes.essais_par_monde):
        rng = graines.g(**base, monde=nom_monde, role="monde", essai=essai)
        m = Monde(f"{_prefixe(base)}{nom_monde}", "finale" if nom_monde == "finale" else "cible", dose)
        oracle = _oracle(graines, base, nom_monde, essai)
        domaines = rng.permutation(DOMAINES_PAR_MONDE)[:DOMAINES_A_LOI_CIBLE].tolist()
        vraies, deja = {}, list(lois_rang) + list(extra)
        for k, i in enumerate(domaines[:len(paires)]):
            p, q = paires[k]
            c = composer(lois_rang[p], lois_rang[q])
            if faute == "poids-dependantes-doubles":
                c = {"type": "par_sous_population", "lois": {
                    g: {"type": "softmax", "poids": [[round(2 * w, 6) for w in ligne] for ligne in s["poids"]], "biais": s["biais"]}
                    for g, s in c["lois"].items()}}
            vraies[i] = (c, True, (p, q), None)
            deja.append(c)
        complet = True
        for i in domaines[len(paires):]:
            loi = _loi_independante(rng, oracle, deja, bornes, compteurs)
            if loi is None:
                complet = False
                break
            vraies[i] = (loi, False, None, None)
            deja.append(loi)
        if complet and faute == "loi-de-la-source-recopiee" and nom_monde == "finale":
            vraies[domaines[-1]] = (lois_rang[0], False, None, None)
        if complet and faute == "lois-de-la-source-recopiees" and nom_monde == "finale":
            for r, i in enumerate(domaines[len(paires):][:len(lois_rang)]):
                vraies[i] = (lois_rang[r], False, None, None)
        fausses = {}
        for i in domaines if complet else []:
            f = _loi_fausse(vraies[i][0], rng, oracle, deja, bornes, compteurs, "fausse-cible")
            if f is None:
                complet = False
                break
            fausses[i] = f
            deja.append(f)
        if not complet:
            compteurs.essais_abandonnes["cible"] += 1
            continue
        _remplir(m, graines, base, nom_monde, essai, oracle, vraies, fausses, variante)
        if faute is not None or variante is not None:
            return m, essai, []
        manques = AU.audit_marges({i: l["loi"] for i, l in m.lois.items()}, oracle.Z, oracle.G, lois_rang,
                                  etrangere.vraies_par_rang() if etrangere is not None else None)
        if not manques:
            return m, essai, []
        if all(_seulement_dependantes(m, x) for x in manques):
            return None, essai, manques
        compteurs.rejets_audit["cible"] += 1
    raise ArretGenerateur(f"bornes de la construction épuisées : {nom_monde}, {bornes.essais_par_monde} essais "
                          "(liste d'arrêt, point 2)")


def _seulement_dependantes(m, manque):
    genre, a, b, _ = manque
    if not m.lois[a]["dependante"]:
        return False
    if genre == "meme-monde":
        return m.lois[b]["dependante"]
    return True  # une dépendante face à une loi d'une source


class Suite:
    """La suite de mondes d'une source : source, trois cibles d'évolution, monde final ; les paires de chaque monde cible."""

    def __init__(self):
        self.source, self.cibles, self.finale, self.paires = None, [], None, None
        self.compteurs = Compteurs()

    def mondes_cibles(self):
        return self.cibles + [self.finale]


def _base_du_tour(base, tour):
    return dict(base) if tour == 0 else dict(base, tour=tour)


def generer_suite(graines, base, dose, bornes=BORNES_GELEES, etrangere=None, variante=None, faute=None):
    """La suite d'une source. `base` : champs d'étiquette communs (couche, famille, proposeur, tirage, source…) ; les graines des
    mondes ne dépendent pas du bras (communes aux trois bras). Un monde cible qui ne manque sa marge que par ses lois dépendantes
    fait retirer la suite entière (source et paires), sous un tour neuf (champ `tour` de l'étiquette)."""
    s = Suite()
    for tour in range(bornes.tours_par_suite):
        b = _base_du_tour(base, tour)
        s.source, _ = generer_source(graines, b, dose, bornes, s.compteurs, variante)
        paires = tirer_paires(graines.g(**b, monde="paires", role="paires"), dose)
        s.cibles, ok = [], True
        for j in range(MONDES_CIBLES_D_EVOLUTION + 1):
            nom = "finale" if j == MONDES_CIBLES_D_EVOLUTION else f"cible-{j + 1}"
            m, _, _ = generer_cible(graines, b, s.source, nom, paires[j], dose, bornes, s.compteurs, etrangere, variante, faute)
            if m is None:
                ok = False
                break
            s.cibles.append(m)
        if ok:
            s.finale = s.cibles.pop()
            s.paires = paires
            return s
        s.compteurs.tours += 1
    raise ArretGenerateur(f"bornes de la construction épuisées : suite, {bornes.tours_par_suite} tours (liste d'arrêt, point 2)")


def generer_jeu_avec_etrangeres(graines, bases, dose, bornes=BORNES_GELEES):
    """B7 bis (version 4, point 6) : les suites d'un jeu de sources où les bras 4a et 4b se jouent ; la source étrangère de la
    source k est la source k + 1 (la première pour la dernière). Les mondes sources sont tirés d'abord ; puis les mondes cibles
    de chaque source, séparés aussi de la source étrangère. Une suite retirée (tour neuf) change sa source : les mondes cibles
    de la source qui la prend pour étrangère sont alors refaits. Rend la liste des suites. Code v3, note D7 : les compteurs de
    B1 (iii) de chaque source (mondes sources tirés, mondes cibles tentés, suites refaites comprises, et tours retirés) sont
    cumulés et portés par sa suite ; ils ne font que compter, aucun tirage n'en dépend. Code v4 (version 7, annexe H, écart 1) :
    ce jeu ne se construit qu'à la dose 0,25 (`DOSE_JEU_GARDE_27`) ; la marge face à la source étrangère n'est ni construite ni
    revendiquée à la dose 0,5 ; toute autre dose arrête avant tout tirage."""
    if float(dose) != DOSE_JEU_GARDE_27:
        raise ArretGenerateur(f"garde 27 : le jeu de sources à sources étrangères ne se construit qu'à la dose "
                              f"{DOSE_JEU_GARDE_27} (reçu {dose!r}) : arrêt (B7 bis, version 7)")
    S = len(bases)
    if S < 2:
        raise ArretGenerateur("B7 bis : au moins deux sources")
    tours = [0] * S
    cumul = [Compteurs() for _ in range(S)]
    sources = [generer_source(graines, _base_du_tour(bases[k], 0), dose, bornes, cumul[k])[0] for k in range(S)]
    suites = [None] * S
    a_faire = list(range(S))
    garde = 0
    while a_faire:
        garde += 1
        if garde > bornes.tours_par_suite * S:
            raise ArretGenerateur("bornes de la construction épuisées : jeu à sources étrangères (liste d'arrêt, point 2)")
        k = a_faire.pop(0)
        b = _base_du_tour(bases[k], tours[k])
        s = Suite()
        s.compteurs = cumul[k]
        s.source = sources[k]
        s.etrangere = sources[(k + 1) % S]  # code v5 : la source face à laquelle la marge est construite, gardée avec la suite
        paires = tirer_paires(graines.g(**b, monde="paires", role="paires"), dose)
        ok = True
        for j in range(MONDES_CIBLES_D_EVOLUTION + 1):
            nom = "finale" if j == MONDES_CIBLES_D_EVOLUTION else f"cible-{j + 1}"
            m, _, _ = generer_cible(graines, b, s.source, nom, paires[j], dose, bornes, s.compteurs, s.etrangere)
            if m is None:
                ok = False
                break
            s.cibles.append(m)
        if ok:
            s.finale, s.paires = s.cibles.pop(), paires
            suites[k] = s
            continue
        tours[k] += 1
        cumul[k].tours += 1
        if tours[k] >= bornes.tours_par_suite:
            raise ArretGenerateur(f"bornes de la construction épuisées : suite {k}, {bornes.tours_par_suite} tours")
        sources[k] = generer_source(graines, _base_du_tour(bases[k], tours[k]), dose, bornes, cumul[k])[0]
        a_faire.insert(0, k)
        precedente = (k - 1) % S
        if precedente != k and precedente not in a_faire:
            suites[precedente] = None
            a_faire.append(precedente)
    verifier_etrangeres_du_jeu(suites)
    return suites


def verifier_etrangeres_du_jeu(suites):
    """Garde 27 (code v5 ; B7 bis : la source étrangère de la source k est la source k + 1, la première pour la dernière) : la
    source face à laquelle la marge des mondes cibles de chaque suite a été construite (`etrangere`) est la source de la suite
    suivante ; sinon arrêt."""
    S = len(suites)
    for k, s in enumerate(suites):
        if getattr(s, "etrangere", None) is not suites[(k + 1) % S].source:
            raise ArretGenerateur(f"garde 27 : la marge des mondes cibles de la source {k} n'est pas construite face à la source "
                                  "suivante (B7 bis) : arrêt")
    return True


def ensemble_exclu(finale, lois_du_registre_de_la_source, seuil=SEUIL_APPARIEMENT_NAT):
    """§ 6 du plan et M1 : toute loi plantée du monde final que le comparateur apparie (≤ 0,05 nat, de la loi plantée vers la loi
    de la tentative) à une tentative du registre de la source, lue sans égard au domaine (version 4, plus strict)."""
    exclu = set()
    for i, l in finale.lois.items():
        for loi in lois_du_registre_de_la_source:
            if finale.oracle.divergence(l["loi"], loi) <= seuil:
                exclu.add(i)
                break
    return sorted(exclu)


# --- fichiers ---------------------------------------------------------------------------------------------------------------


def _csv(Z, G, y, episodes):
    lignes = ["episode,z0,z1,g,y"]
    for e, z, g, v in zip(episodes.tolist(), Z.tolist(), G.tolist(), y.tolist()):
        lignes.append(f"{e},{z[0]!r},{z[1]!r},{g},{v}")
    return "\n".join(lignes) + "\n"


def ecrire_monde(dossier, monde):
    """Écrit la clé (`cle/cle.json`, jamais servie) et, par domaine, la part servie (`servi/Dkk.csv`) et la tranche d'épreuve
    (`epreuve/Dkk/episodes.csv`)."""
    os.makedirs(os.path.join(dossier, "cle"))
    os.makedirs(os.path.join(dossier, "servi"))
    with open(os.path.join(dossier, "cle", "cle.json"), "x", encoding="utf-8") as f:
        f.write(json_canonique(monde.cle()))
    for d in monde.domaines:
        s, t = monde.part_servie(d["nom"]), monde.tranche_epreuve(d["nom"])
        with open(os.path.join(dossier, "servi", d["nom"] + ".csv"), "x", encoding="utf-8") as f:
            f.write(_csv(s["Z"], s["G"], s["y"], s["episodes"]))
        os.makedirs(os.path.join(dossier, "epreuve", d["nom"]))
        with open(os.path.join(dossier, "epreuve", d["nom"], "episodes.csv"), "x", encoding="utf-8") as f:
            f.write(_csv(t["Z"], t["G"], t["y"], t["episodes"]))


def lire_csv(chemin):
    with open(chemin, encoding="utf-8") as f:
        lignes = f.read().splitlines()[1:]
    return [l for l in lignes if l.strip()]


def verifier_tranche_jamais_servie(lignes_servies, lignes_epreuve):
    """Garde 10 : la part servie et la tranche d'épreuve sont disjointes (épisodes et lignes) ; une ligne de la tranche dans ce
    qui est servi arrête la génération."""
    ep_s = {l.split(",", 1)[0] for l in lignes_servies}
    ep_t = {l.split(",", 1)[0] for l in lignes_epreuve}
    if ep_s & ep_t or set(lignes_servies) & set(lignes_epreuve):
        raise ArretGenerateur("garde 10 : une ligne de la tranche d'épreuve est servie : arrêt de la génération")
    return True


# --- audit de la couche « audit » (étape 3) -------------------------------------------------------------------------------------


def mondes_pour_l_audit(suites):
    """Ce que lit l'audit de présentation : les mondes cibles et finaux, avec le texte canonique de leurs lois plantées. Code
    v4 : chaque monde porte l'identifiant de sa suite (son rang dans `suites`), pour la permutation entre suites."""
    out = []
    for i, s in enumerate(suites):
        for m in s.mondes_cibles():
            out.append({"dose": m.dose, "suite": i, "Z": m.oracle.Z, "G": m.oracle.G,
                        "lois": [(l["texte"], l["loi"], l["type"], l["dependante"]) for _, l in sorted(m.lois.items())]})
    return out


def distribution_des_traits_de_contenu(suites):
    """B1 (iii) : par sorte de loi plantée (vraie de la source, fausse de la source, dépendante, indépendante, fausse d'un monde
    cible), moyenne et quartiles des traits de contenu — les six de la version 6 et, code v4, la longueur brute du texte
    canonique (annexe H, écart 2)."""
    par_sorte = {}
    for s in suites:
        for m in [s.source] + s.mondes_cibles():
            for _, l in m.lois.items():
                if m.role == "source":
                    sorte = "vraie-source" if l["type"] == "vraie" else "fausse-source"
                else:
                    sorte = ("dependante" if l["dependante"] else "independante") if l["type"] == "vraie" else "fausse-cible"
                par_sorte.setdefault(sorte, []).append(AU.traits_de_contenu(l["loi"], m.oracle.Z, m.oracle.G, l["texte"]))
    noms = ("norme_poids_g0", "norme_biais_g0", "entropie_g0", "norme_poids_g1", "norme_biais_g1", "entropie_g1",
            "longueur_brute")
    out = {}
    for sorte, v in sorted(par_sorte.items()):
        a = np.array(v)
        out[sorte] = {"lois": len(v), **{n: {"moyenne": float(a[:, j].mean()),
                                             "quartiles": [float(x) for x in np.percentile(a[:, j], (25, 50, 75))]}
                                         for j, n in enumerate(noms)}}
    return out


def generer_suites_d_audit(graines, doses, suites_par_dose, couche="audit"):
    """Étape 3, construction : `suites_par_dose` suites par dose sous la couche `couche` (« audit » ; les essais du code jouent
    la couche « essai »). Rend (suites, compteurs cumulés de B1 (iii))."""
    suites, compteurs = [], Compteurs()
    for dose in doses:
        for k in range(suites_par_dose):
            s = generer_suite(graines, dict(couche=couche, famille="audit", dose=dose, source=k), dose)
            suites.append(s)
            compteurs.ajouter(s.compteurs)
    return suites, compteurs


def generateurs_de_l_audit(graines, couche="audit"):
    """Code v5 (« Ce qui demande un code v5 », point 3 ; section « Seuil », version 9 ; B8) : les deux générateurs de l'audit de
    présentation, dérivés par le code de l'étape 3 et non reçus de l'appelant — celui des plis de la lecture observée (couche
    `couche`, famille « audit », rôle « plis » ; un seul pour les quinze exactitudes) et celui des permutations (même couche et
    famille, rôle « permutation »). Rend (plis, permutation)."""
    rng_plis = graines.g(couche=couche, famille="audit", role=ROLE_PLIS)
    rng_permutation = graines.g(couche=couche, famille="audit", role=ROLE_PERMUTATION)
    return rng_plis, rng_permutation


def juger_suites_d_audit(suites, compteurs, graines, couche="audit", permutations=PERMUTATIONS_AUDIT):
    """Étape 3, jugement : ensemble exclu par construction, audit de présentation (quinze exactitudes, chacune avec σ₀, la
    moyenne permutée M, le seuil calibré M + 2 σ₀ et le seuil d'arrêt ; code v5), rejets et taux d'acceptation, distribution des
    traits de contenu. Code v5 : les plis de la lecture observée et les permutations sont tirés par les générateurs que
    `generateurs_de_l_audit` dérive ici de `graines` (couche `couche`), et non reçus de l'appelant. Rend le rapport ; lève
    `ArretGenerateur` (liste d'arrêt, point 2), le rapport joint à l'exception quand il existe (`rapport`), si une exactitude de
    forme d'un audit de lois dépasse 0,55, si une exactitude de forme d'un audit des mondes par dose dépasse le plus grand de
    0,55 et de M + 2 σ₀, si une loi du monde final est celle de sa source, ou si l'audit de présentation arrête (pli privé d'une
    classe, centre non fini, exactitude non calculable). Une exactitude de forme des doses au-dessus de 0,55 et au plus
    M + 2 σ₀ n'arrête pas : elle est rapportée « non départagée du hasard à cette taille » et lie l'étage payant ; une
    exactitude au plus 0,55 n'arrête jamais."""
    rng_plis, rng_permutation = generateurs_de_l_audit(graines, couche)
    communs = {}
    for s in suites:
        c = AU.ensemble_exclu_par_construction([l["texte"] for l in s.finale.lois.values()],
                                               [l["texte"] for l in s.source.lois.values() if l["type"] == "vraie"])
        if c:
            communs[s.source.nom] = c
    try:
        pres = AU.audit_presentation(mondes_pour_l_audit(suites), rng_plis, rng_permutation, permutations)
    except AU.ArretAudit as e:
        raise ArretGenerateur(f"audit du générateur en échec : {e}") from e
    rapport = {"presentation": pres, "lois_du_final_identiques_a_la_source": communs, "compteurs": compteurs.vers_dict(),
               "traits_de_contenu": distribution_des_traits_de_contenu(suites)}
    if pres["arret"] or communs:
        arret = ArretGenerateur(f"audit du générateur en échec : {pres['arret'] or communs} (liste d'arrêt, point 2)")
        arret.rapport = rapport
        raise arret
    return rapport


def audit_du_generateur(graines, doses, suites_par_dose, permutations=PERMUTATIONS_AUDIT, couche="audit"):
    """Étape 3 : `suites_par_dose` suites par dose sous la couche « audit » ; marges rejugées sur chaque monde (déjà faites à la
    construction par le module `audit`), puis `juger_suites_d_audit`, qui dérive les générateurs des plis observés (rôle
    « plis ») et des permutations (rôle « permutation ») de la couche `couche`, famille « audit » (code v5 : aucun générateur
    n'est reçu de l'appelant). Rend un rapport ; lève `ArretGenerateur` (liste d'arrêt, point 2)."""
    suites, compteurs = generer_suites_d_audit(graines, doses, suites_par_dose, couche)
    return juger_suites_d_audit(suites, compteurs, graines, couche, permutations)
