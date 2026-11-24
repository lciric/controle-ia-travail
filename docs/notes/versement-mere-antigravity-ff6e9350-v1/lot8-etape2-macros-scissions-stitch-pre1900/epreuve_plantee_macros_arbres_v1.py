#!/usr/bin/env python3
"""Épreuve sur monde planté et gardes d'arrêt (règle R5) pour la détection ex ante
de sous-arbres d'équations répétés et de macros locales convergentes entre bassins
thématiques disjoints avant Fomin et Zelevinsky (IDE-2026-11-23-032).

Ce module vérifie sur processeur central, sans aucune modification du dépôt principal
et sans écrire de code octet compilé :
1. Quatre gardes d'arrêt strictes (règle R5), chacune éprouvée sur un cas sain et sur
   un artefact déclenchant immédiatement `GardeArret` sans aucun repli silencieux :
   - `garde_coupure_temporelle` : rejet strict de tout document postérieur ou égal au
     dépôt initial `math/0104151v1` du 13 avril 2001 (`2001-04-12T23:59:59Z` au plus tard) ;
   - `garde_expansion_macros_acyclique` : expansion déterministe des définitions locales
     de composition typographique mathématique (`\\newcommand`, `\\def`) et arrêt sur
     cycle récursif ou discordance d'arité ;
   - `garde_disjonction_auteurs` : vérification des identifiants d'auteurs normalisés
     et déduplication par composante connexe de co-autorat ;
   - `garde_non_degenerescence_corpus` : vérification de la structure des arbres
     d'opérateurs canonisés et de la présence d'au moins deux bassins faiblement co-cités.
2. Un moteur d'anti-unification syntaxique du premier ordre (Plotkin, 1970) couplé au
   calcul exact du gain de longueur de description minimale (Rissanen, 1978) inter-bassins
   à équipes d'auteurs disjointes, normalisé par permutation des opérateurs de même arité.
3. Un banc d'épreuve synthétique à quarante réplications de Monte-Carlo confrontant :
   - le cas positif planté (gestation convergente du schéma d'échange binomial divisé
     des mutations d'amas dans trois bassins éloignés) ;
   - trois témoins négatifs « doit mourir » : (a) inflation syntaxique triviale dans un
     seul bassin, (b) diffusion par une même équipe d'auteurs entre deux bassins, et
     (c) ubiquité algébrique élémentaire de science normale.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import dataclasses
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

from controle_ia.gardes import GardeArret, exiger_numpy_minimal

DATE_COUPURE_FOMIN_ZELEVINSKY = "2001-04-12T23:59:59Z"
ENTROPIE_GRAINE_MACROS = 20261123032
COUT_OPERATEUR_BITS = 10.0
COUT_TROU_BITS = 2.0
COUT_VARIABLE_BITS = 3.0
COUT_APPEL_MACRO_BITS = 4.0
PENALITE_ARITE_BITS = 3.0


# ---------------------------------------------------------------------------
# Représentation des arbres d'opérateurs et des définitions locales de macros
# ---------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ArbreOperateur:
    """Arbre syntaxique d'opérateurs typés après expansion et renommage canonique."""

    etiquette: str
    enfants: tuple["ArbreOperateur", ...] = ()

    def est_feuille(self) -> bool:
        return len(self.enfants) == 0

    def est_trou(self) -> bool:
        return self.etiquette.startswith("#") and self.etiquette[1:].isdigit()

    def est_variable(self) -> bool:
        return self.etiquette.startswith("v_") and self.etiquette[2:].isdigit()

    def taille(self) -> int:
        return 1 + sum(e.taille() for e in self.enfants)

    def profondeur(self) -> int:
        if not self.enfants:
            return 0
        return 1 + max(e.profondeur() for e in self.enfants)

    def nb_operateurs_internes(self) -> int:
        if not self.enfants:
            return 0
        return 1 + sum(e.nb_operateurs_internes() for e in self.enfants)

    def vers_chaine_lisp(self) -> str:
        if not self.enfants:
            return self.etiquette
        interieur = " ".join(e.vers_chaine_lisp() for e in self.enfants)
        return f"({self.etiquette} {interieur})"


@dataclasses.dataclass(frozen=True)
class MacroLocale:
    """Définition locale ad hoc extraite d'un préambule d'article."""

    nom: str
    arite: int
    corps: ArbreOperateur


@dataclasses.dataclass(frozen=True)
class ArticleMathematique:
    """Article horodaté muni de son bassin thématique, de ses auteurs et de ses formules."""

    identifiant: str
    date_depot_utc: str
    bassin: str
    auteurs: tuple[str, ...]
    macros: tuple[MacroLocale, ...]
    expressions_brutes: tuple[ArbreOperateur, ...]


# ---------------------------------------------------------------------------
# Gardes d'arrêt conformes à la règle R5 (aucun repli silencieux)
# ---------------------------------------------------------------------------

def _analyser_date_iso_utc(chaine: str) -> datetime:
    if not isinstance(chaine, str) or not chaine.strip():
        raise GardeArret("horodatage vide ou non textuel dans un article")
    texte = chaine.strip()
    if texte.endswith("Z"):
        texte = texte[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(texte)
    except ValueError as exc:
        raise GardeArret(f"horodatage illisible {chaine!r} : {exc}") from exc
    if dt.tzinfo is None:
        raise GardeArret(f"horodatage sans fuseau explicite interdit : {chaine!r}")
    return dt.astimezone(timezone.utc)


def garde_coupure_temporelle(
    articles: Sequence[ArticleMathematique],
    coupure_utc: str = DATE_COUPURE_FOMIN_ZELEVINSKY,
) -> None:
    """Refuse tout article déposé après la coupure stricte précédant Fomin et Zelevinsky."""
    if not articles:
        raise GardeArret("corpus d'articles vide soumis à la garde temporelle")
    limite = _analyser_date_iso_utc(coupure_utc)
    for art in articles:
        dt = _analyser_date_iso_utc(art.date_depot_utc)
        if dt > limite:
            raise GardeArret(
                f"fuite temporelle détectée sur l'article {art.identifiant!r} "
                f"({art.date_depot_utc} > coupure {coupure_utc})"
            )


def _substituer_arguments(corps: ArbreOperateur, arguments: Sequence[ArbreOperateur]) -> ArbreOperateur:
    if corps.est_trou():
        indice = int(corps.etiquette[1:])
        if indice < 0 or indice >= len(arguments):
            raise GardeArret(
                f"indice de trou #{indice} hors bornes pour une macro d'arité {len(arguments)}"
            )
        return arguments[indice]
    return ArbreOperateur(
        corps.etiquette,
        tuple(_substituer_arguments(e, arguments) for e in corps.enfants),
    )


def garde_expansion_macros_acyclique(
    expression: ArbreOperateur,
    table_macros: dict[str, MacroLocale],
    profondeur_max: int = 16,
    _pile: tuple[str, ...] = (),
) -> ArbreOperateur:
    """Expands les macros locales et lève `GardeArret` sur récursion ou arité fautive."""
    if len(_pile) > profondeur_max:
        raise GardeArret(
            f"dépassement de la profondeur maximale d'expansion ({profondeur_max}) : {_pile}"
        )
    nom = expression.etiquette
    if nom in table_macros:
        if nom in _pile:
            cycle = " -> ".join((*_pile, nom))
            raise GardeArret(f"cycle de macros détecté lors de l'expansion : {cycle}")
        macro = table_macros[nom]
        if len(expression.enfants) != macro.arite:
            raise GardeArret(
                f"macro {nom!r} appelée avec {len(expression.enfants)} arguments "
                f"au lieu de {macro.arite}"
            )
        args_expanses = tuple(
            garde_expansion_macros_acyclique(arg, table_macros, profondeur_max, _pile)
            for arg in expression.enfants
        )
        remplace = _substituer_arguments(macro.corps, args_expanses)
        return garde_expansion_macros_acyclique(
            remplace, table_macros, profondeur_max, (*_pile, nom)
        )
    return ArbreOperateur(
        nom,
        tuple(
            garde_expansion_macros_acyclique(e, table_macros, profondeur_max, _pile)
            for e in expression.enfants
        ),
    )


def garde_disjonction_auteurs(articles: Sequence[ArticleMathematique]) -> dict[str, int]:
    """Construit les classes connexes de co-autorat et refuse toute métadonnée d'auteur invalide."""
    if not articles:
        raise GardeArret("aucun article fourni pour le calcul des classes d'auteurs")
    parent: dict[str, str] = {}

    def trouver(x: str) -> str:
        racine = x
        while parent[racine] != racine:
            racine = parent[racine]
        courant = x
        while courant != racine:
            suivant = parent[courant]
            parent[courant] = racine
            courant = suivant
        return racine

    def unir(a: str, b: str) -> None:
        ra, rb = trouver(a), trouver(b)
        if ra != rb:
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb

    for art in articles:
        if not art.auteurs:
            raise GardeArret(f"article {art.identifiant!r} dépourvu d'auteurs déclarés")
        propres = []
        for aut in art.auteurs:
            if not isinstance(aut, str) or not aut.strip():
                raise GardeArret(f"nom d'auteur vide ou invalide dans {art.identifiant!r}")
            cle = aut.strip().lower()
            propres.append(cle)
            parent.setdefault(cle, cle)
        premier = propres[0]
        for autre in propres[1:]:
            unir(premier, autre)

    racines_triees = sorted({trouver(a) for a in parent})
    indice_racine = {r: idx for idx, r in enumerate(racines_triees)}
    classe_par_article: dict[str, int] = {}
    for art in articles:
        cle0 = art.auteurs[0].strip().lower()
        classe_par_article[art.identifiant] = indice_racine[trouver(cle0)]
    return classe_par_article


def _verifier_arbre_sain(arbre: ArbreOperateur) -> None:
    if not isinstance(arbre.etiquette, str) or not arbre.etiquette.strip():
        raise GardeArret("étiquette de nœud vide ou invalide dans un arbre d'opérateurs")
    if "nan" == arbre.etiquette.strip().lower():
        raise GardeArret("étiquette NaN détectée dans un arbre d'opérateurs")
    for e in arbre.enfants:
        _verifier_arbre_sain(e)


def garde_non_degenerescence_corpus(
    expressions_par_bassin: dict[str, list[tuple[int, ArbreOperateur]]],
    cocitations_inter_bassins: dict[tuple[str, str], float],
    seuil_cocitation_max: float = 0.05,
) -> list[tuple[str, str]]:
    """Vérifie qu'au moins une paire de bassins non vides est faiblement co-citée."""
    bassins_valides = [b for b, exprs in expressions_par_bassin.items() if len(exprs) > 0]
    if len(bassins_valides) < 2:
        raise GardeArret(
            f"corpus dégénéré : {len(bassins_valides)} bassin non vide (au moins 2 requis)"
        )
    for b in bassins_valides:
        for _, arbre in expressions_par_bassin[b]:
            _verifier_arbre_sain(arbre)
    paires_eloignees: list[tuple[str, str]] = []
    for i, b1 in enumerate(sorted(bassins_valides)):
        for b2 in sorted(bassins_valides)[i + 1 :]:
            taux = cocitations_inter_bassins.get(
                (b1, b2), cocitations_inter_bassins.get((b2, b1), 0.0)
            )
            if not math.isfinite(taux) or taux < 0.0 or taux > 1.0:
                raise GardeArret(f"taux de co-citation invalide entre {b1} et {b2} : {taux}")
            if taux <= seuil_cocitation_max:
                paires_eloignees.append((b1, b2))
    if not paires_eloignees:
        raise GardeArret(
            "aucune paire de bassins faiblement co-citée sous le seuil fixé"
        )
    return paires_eloignees


# ---------------------------------------------------------------------------
# Renommage alpha-canonique, anti-unification de Plotkin et compression MDL
# ---------------------------------------------------------------------------

def renommer_variables_canonique(arbre: ArbreOperateur) -> ArbreOperateur:
    """Renomme les feuilles de variables libres/liées par ordre de premier parcours préfixe."""
    table: dict[str, str] = {}

    def parcourir(noeud: ArbreOperateur) -> ArbreOperateur:
        if not noeud.enfants:
            etq = noeud.etiquette
            if noeud.est_trou() or etq.lstrip("-").isdigit():
                return noeud
            if etq not in table:
                table[etq] = f"v_{len(table)}"
            return ArbreOperateur(table[etq])
        return ArbreOperateur(noeud.etiquette, tuple(parcourir(e) for e in noeud.enfants))

    return parcourir(arbre)


def _renumeroter_trous_canonique(patron: ArbreOperateur) -> tuple[ArbreOperateur, int]:
    table: dict[str, str] = {}

    def parcourir(noeud: ArbreOperateur) -> ArbreOperateur:
        if noeud.est_trou():
            if noeud.etiquette not in table:
                table[noeud.etiquette] = f"#{len(table)}"
            return ArbreOperateur(table[noeud.etiquette])
        return ArbreOperateur(noeud.etiquette, tuple(parcourir(e) for e in noeud.enfants))

    canon = parcourir(patron)
    return canon, len(table)


def anti_unifier_plotkin(t1: ArbreOperateur, t2: ArbreOperateur) -> tuple[ArbreOperateur, int]:
    """Plus petite généralisation commune du premier ordre (Plotkin, 1970)."""
    paires_vues: dict[tuple[ArbreOperateur, ArbreOperateur], str] = {}

    def generaliser(a: ArbreOperateur, b: ArbreOperateur) -> ArbreOperateur:
        if a.etiquette == b.etiquette and len(a.enfants) == len(b.enfants):
            if not a.enfants:
                if a.est_variable():
                    # Les variables locales d'articles différents ne portent pas la même identité
                    cle = (a, b)
                    if cle not in paires_vues:
                        paires_vues[cle] = f"#{len(paires_vues)}"
                    return ArbreOperateur(paires_vues[cle])
                return a
            return ArbreOperateur(
                a.etiquette,
                tuple(generaliser(ea, eb) for ea, eb in zip(a.enfants, b.enfants)),
            )
        cle = (a, b)
        if cle not in paires_vues:
            paires_vues[cle] = f"#{len(paires_vues)}"
        return ArbreOperateur(paires_vues[cle])

    brut = generaliser(t1, t2)
    return _renumeroter_trous_canonique(brut)


def extraire_sous_arbres(arbre: ArbreOperateur, ops_min: int = 2) -> list[ArbreOperateur]:
    """Extrait tous les sous-arbres contenant au moins `ops_min` opérateurs internes."""
    sortie: list[ArbreOperateur] = []

    def parcourir(n: ArbreOperateur) -> None:
        if n.nb_operateurs_internes() >= ops_min:
            sortie.append(renommer_variables_canonique(n))
        for e in n.enfants:
            parcourir(e)

    parcourir(arbre)
    return sortie


def longueur_description_arbre(arbre: ArbreOperateur) -> float:
    """Longueur de description en bits d'un arbre dans l'alphabet de base."""
    if arbre.est_trou():
        return COUT_TROU_BITS
    if not arbre.enfants:
        return COUT_VARIABLE_BITS
    return COUT_OPERATEUR_BITS + sum(longueur_description_arbre(e) for e in arbre.enfants)


def cout_definition_abstraction(patron: ArbreOperateur, arite: int) -> float:
    """Coût de description de l'abstraction ajoutée à la bibliothèque."""
    return PENALITE_ARITE_BITS * arite + longueur_description_arbre(patron)


def correspondance_patron(
    patron: ArbreOperateur, cible: ArbreOperateur
) -> dict[str, ArbreOperateur] | None:
    """Retourne la substitution des trous si `patron` filtre la racine de `cible`, sinon None."""
    liaisons: dict[str, ArbreOperateur] = {}

    def filtrer(p: ArbreOperateur, c: ArbreOperateur) -> bool:
        if p.est_trou():
            deja = liaisons.get(p.etiquette)
            if deja is None:
                liaisons[p.etiquette] = c
                return True
            return deja == c
        if p.etiquette != c.etiquette or len(p.enfants) != len(c.enfants):
            return False
        return all(filtrer(ep, ec) for ep, ec in zip(p.enfants, c.enfants))

    if filtrer(patron, cible):
        return liaisons
    return None


def gain_reecriture_arbre(arbre: ArbreOperateur, patron: ArbreOperateur, arite: int) -> float:
    """Gain maximal en bits obtenu en réécrivant `arbre` sans recouvrement avec `patron`."""
    economie_locale_base = (
        longueur_description_arbre(patron) - arite * COUT_TROU_BITS - COUT_APPEL_MACRO_BITS
    )
    if economie_locale_base <= 0.0:
        return 0.0

    def meilleur_gain(noeud: ArbreOperateur) -> float:
        gain_sans_racine = sum(meilleur_gain(e) for e in noeud.enfants)
        subst = correspondance_patron(patron, noeud)
        if subst is None:
            return gain_sans_racine
        # Si un trou apparaît k fois dans le patron, k-1 copies entières de l'argument sont économisées
        occurrences_trous: dict[str, int] = {}

        def compter_trous(p: ArbreOperateur) -> None:
            if p.est_trou():
                occurrences_trous[p.etiquette] = occurrences_trous.get(p.etiquette, 0) + 1
            for ep in p.enfants:
                compter_trous(ep)

        compter_trous(patron)
        economie_doublons = sum(
            (nb - 1) * longueur_description_arbre(subst[trou])
            for trou, nb in occurrences_trous.items()
            if nb > 1
        )
        gain_arguments = sum(meilleur_gain(arg) for arg in subst.values())
        gain_avec_racine = economie_locale_base + economie_doublons + gain_arguments
        return max(gain_sans_racine, gain_avec_racine)

    return meilleur_gain(arbre)


def sont_isomorphes_modulo_trous(p1: ArbreOperateur, p2: ArbreOperateur) -> bool:
    """Vérifie si deux schémas abstraits sont identiques à renommage bijectif des trous près."""
    c1, a1 = _renumeroter_trous_canonique(p1)
    c2, a2 = _renumeroter_trous_canonique(p2)
    return a1 == a2 and c1 == c2


# ---------------------------------------------------------------------------
# Score de compression convergente inter-bassins à équipes d'auteurs disjointes
# ---------------------------------------------------------------------------

def preparer_corpus_canonise(
    articles: Sequence[ArticleMathematique],
    coupure_utc: str = DATE_COUPURE_FOMIN_ZELEVINSKY,
) -> dict[str, list[tuple[int, ArbreOperateur]]]:
    """Applique les gardes temporelle, d'auteurs et de macros, puis retourne les arbres par bassin."""
    garde_coupure_temporelle(articles, coupure_utc=coupure_utc)
    classes_auteurs = garde_disjonction_auteurs(articles)
    par_bassin: dict[str, list[tuple[int, ArbreOperateur]]] = {}
    for art in articles:
        table = {m.nom: m for m in art.macros}
        if len(table) != len(art.macros):
            raise GardeArret(f"doublon de nom de macro dans l'article {art.identifiant!r}")
        classe = classes_auteurs[art.identifiant]
        liste = par_bassin.setdefault(art.bassin, [])
        for expr in art.expressions_brutes:
            expanse = garde_expansion_macros_acyclique(expr, table)
            canon = renommer_variables_canonique(expanse)
            _verifier_arbre_sain(canon)
            liste.append((classe, canon))
    return par_bassin


def candidats_abstractions_paire(
    bassin_a: Sequence[tuple[int, ArbreOperateur]],
    bassin_b: Sequence[tuple[int, ArbreOperateur]],
    ops_min: int = 3,
    arite_max: int = 6,
) -> list[tuple[ArbreOperateur, int]]:
    """Extrait par anti-unification inter-bassins les patrons candidats non triviaux."""
    sous_a: list[tuple[int, ArbreOperateur]] = []
    for cl, arb in bassin_a:
        for sa in extraire_sous_arbres(arb, ops_min=ops_min):
            sous_a.append((cl, sa))
    sous_b: list[tuple[int, ArbreOperateur]] = []
    for cl, arb in bassin_b:
        for sb in extraire_sous_arbres(arb, ops_min=ops_min):
            sous_b.append((cl, sb))

    vus: dict[ArbreOperateur, int] = {}
    for cl_a, sa in sous_a:
        for cl_b, sb in sous_b:
            if cl_a == cl_b:
                continue
            if sa.etiquette != sb.etiquette:
                continue
            patron, arite = anti_unifier_plotkin(sa, sb)
            if patron.nb_operateurs_internes() >= ops_min and arite <= arite_max:
                vus[patron] = arite
    return list(vus.items())


def score_compression_inter_bassins(
    bassin_a: Sequence[tuple[int, ArbreOperateur]],
    bassin_b: Sequence[tuple[int, ArbreOperateur]],
    tous_les_bassins: dict[str, list[tuple[int, ArbreOperateur]]],
    nom_a: str,
    nom_b: str,
    ops_min: int = 3,
) -> dict[str, object]:
    """Calcule le gain de longueur de description minimale inter-bassins spécifique.

    Pour neutraliser :
    - l'inflation mono-bassin : on prend le minimum des gains entre les deux bassins ;
    - la diffusion par une même équipe : seules des classes d'auteurs disjointes entre
      `bassin_a` et `bassin_b` peuvent contribuer simultanément, et chaque classe
      d'auteurs est plafonnée à une seule contribution maximale par bassin ;
    - l'ubiquité banale de science normale : on retranche le gain médian observé sur les
      autres bassins témoins du corpus (spécificité inter-bassins).
    """
    candidats = candidats_abstractions_paire(bassin_a, bassin_b, ops_min=ops_min)
    if not candidats:
        return {
            "score_specifique_bits": 0.0,
            "gain_brut_paire_bits": 0.0,
            "gain_global_naif_bits": 0.0,
            "meilleur_patron": None,
            "meilleure_arite": 0,
        }

    autres_noms = [b for b in sorted(tous_les_bassins) if b not in (nom_a, nom_b)]

    def gain_par_equipes_disjointes(
        bassin: Sequence[tuple[int, ArbreOperateur]],
        patron: ArbreOperateur,
        arite: int,
        exclure_classes: set[int] | None = None,
    ) -> tuple[float, set[int]]:
        meilleur_par_classe: dict[int, float] = {}
        for cl, arb in bassin:
            if exclure_classes and cl in exclure_classes:
                continue
            g = gain_reecriture_arbre(arb, patron, arite)
            if g > meilleur_par_classe.get(cl, 0.0):
                meilleur_par_classe[cl] = g
        # Exige au moins 2 équipes indépendantes dans le bassin pour éviter l'idiosyncrasie d'un seul article
        valeurs = sorted((v for v in meilleur_par_classe.values() if v > 0.0), reverse=True)
        if len(valeurs) < 2:
            return 0.0, set()
        classes_actives = {cl for cl, v in meilleur_par_classe.items() if v > 0.0}
        return float(sum(valeurs)), classes_actives

    meilleur_score = 0.0
    meilleur_brut = 0.0
    meilleur_patron: ArbreOperateur | None = None
    meilleure_arite = 0

    for patron, arite in candidats:
        cout_def = cout_definition_abstraction(patron, arite)
        gain_a, classes_a = gain_par_equipes_disjointes(bassin_a, patron, arite)
        gain_b_hors_a, _ = gain_par_equipes_disjointes(
            bassin_b, patron, arite, exclure_classes=classes_a
        )
        gain_b, classes_b = gain_par_equipes_disjointes(bassin_b, patron, arite)
        gain_a_hors_b, _ = gain_par_equipes_disjointes(
            bassin_a, patron, arite, exclure_classes=classes_b
        )
        gain_paire = max(
            min(gain_a, gain_b_hors_a),
            min(gain_a_hors_b, gain_b),
        ) - 0.5 * cout_def
        if gain_paire <= 0.0:
            continue

        gains_autres = []
        for b_autre in autres_noms:
            g_autre, _ = gain_par_equipes_disjointes(tous_les_bassins[b_autre], patron, arite)
            gains_autres.append(max(0.0, g_autre - 0.5 * cout_def))
        fond_ubiquite = float(np.median(gains_autres)) if gains_autres else 0.0
        score_spec = max(0.0, gain_paire - fond_ubiquite)
        if score_spec > meilleur_score:
            meilleur_score = score_spec
            meilleur_brut = gain_paire
            meilleur_patron = patron
            meilleure_arite = arite

    # Calcul également du score global naïf (sans filtre inter-bassins ni déduplication d'auteurs)
    # afin de démontrer quantitativement le piège de l'inflation syntaxique triviale.
    meilleur_naif = 0.0
    sous_tous = []
    for cl, arb in (*bassin_a, *bassin_b):
        for s in extraire_sous_arbres(arb, ops_min=ops_min):
            sous_tous.append(s)
    uniques_naifs: list[tuple[ArbreOperateur, int]] = list(candidats)
    for s in set(sous_tous):
        p_id, ar_id = anti_unifier_plotkin(s, s)
        if p_id.nb_operateurs_internes() >= ops_min and ar_id <= 6:
            uniques_naifs.append((p_id, ar_id))
    for p_n, ar_n in uniques_naifs:
        g_tot = sum(
            gain_reecriture_arbre(arb, p_n, ar_n) for _, arb in (*bassin_a, *bassin_b)
        ) - cout_definition_abstraction(p_n, ar_n)
        if g_tot > meilleur_naif:
            meilleur_naif = float(g_tot)

    return {
        "score_specifique_bits": round(meilleur_score, 4),
        "gain_brut_paire_bits": round(meilleur_brut, 4),
        "gain_global_naif_bits": round(meilleur_naif, 4),
        "meilleur_patron": meilleur_patron.vers_chaine_lisp() if meilleur_patron else None,
        "meilleur_patron_objet": meilleur_patron,
        "meilleure_arite": meilleure_arite,
    }


# ---------------------------------------------------------------------------
# Générateur de mondes plantés (Fomin-Zelevinsky contre 3 témoins « doit mourir »)
# ---------------------------------------------------------------------------

def schema_mutation_amas_cible() -> ArbreOperateur:
    """Schéma canonique d'échange binomial divisé : (/ (+ (* #0 #1) (* #2 #3)) #4)."""
    return ArbreOperateur(
        "/",
        (
            ArbreOperateur(
                "+",
                (
                    ArbreOperateur("*", (ArbreOperateur("#0"), ArbreOperateur("#1"))),
                    ArbreOperateur("*", (ArbreOperateur("#2"), ArbreOperateur("#3"))),
                ),
            ),
            ArbreOperateur("#4"),
        ),
    )


def _feuille_aleatoire(rng: np.random.Generator) -> ArbreOperateur:
    noms = ("x", "y", "z", "u", "w", "q", "t", "p")
    return ArbreOperateur(str(rng.choice(noms)))


def _arbre_bruit_aleatoire(rng: np.random.Generator, profondeur: int = 2) -> ArbreOperateur:
    ops_bin = ("+", "-", "*", "/", "pow", " compose ")
    ops_propres = ("+", "-", "*", "/", "pow", " lie ")
    ops = ("+", "-", "*", "/", "pow", "croch")
    if profondeur <= 0:
        return _feuille_aleatoire(rng)
    op = str(rng.choice(ops))
    gauche = _arbre_bruit_aleatoire(rng, profondeur - 1 if rng.random() < 0.8 else 0)
    droite = _arbre_bruit_aleatoire(rng, profondeur - 1 if rng.random() < 0.8 else 0)
    return ArbreOperateur(op, (gauche, droite))


def _combinaison_lineaire_ubiquitaire(rng: np.random.Generator) -> ArbreOperateur:
    """Schéma banal omniprésent en science normale : (+ (* a x) (+ (* b y) c))."""
    f = lambda: _feuille_aleatoire(rng)
    return ArbreOperateur(
        "+",
        (
            ArbreOperateur("*", (f(), f())),
            ArbreOperateur("+", (ArbreOperateur("*", (f(), f())), f())),
        ),
    )


def _inflation_lourde_locale() -> MacroLocale:
    """Grosse macro ad hoc de profondeur 4 répétée massivement dans un seul bassin."""
    corps = ArbreOperateur(
        "det3",
        (
            ArbreOperateur("-", (ArbreOperateur("*", (ArbreOperateur("#0"), ArbreOperateur("#1"))), ArbreOperateur("#2"))),
            ArbreOperateur("+", (ArbreOperateur("pow", (ArbreOperateur("#1"), ArbreOperateur("#0"))), ArbreOperateur("#2"))),
        ),
    )
    return MacroLocale(nom="\\detAdHocLocal", arite=3, corps=corps)


def simuler_monde_plante(rng: np.random.Generator) -> dict[str, object]:
    """Simule un corpus pré-2001 à 8 bassins incluant le cas sain et les 3 témoins négatifs."""
    bassins = (
        "b1_positivite_totale",
        "b2_systemes_somos",
        "b3_inflation_mono",
        "b4_temoin_vide",
        "b5_pont_meme_auteur",
        "b6_cible_meme_auteur",
        "b7_science_normale_a",
        "b8_science_normale_b",
    )
    articles: list[ArticleMathematique] = []
    compteur_aut = 0

    def nouvelle_equipe() -> tuple[str, ...]:
        nonlocal compteur_aut
        compteur_aut += 1
        return (f"auteur_{compteur_aut}_a", f"auteur_{compteur_aut}_b")

    # 0. Fond commun de science normale dans tous les bassins
    for b in bassins:
        for k in range(5):
            eq = nouvelle_equipe()
            exprs = (
                _combinaison_lineaire_ubiquitaire(rng),
                _arbre_bruit_aleatoire(rng, profondeur=2),
            )
            articles.append(
                ArticleMathematique(
                    identifiant=f"fond_{b}_{k}",
                    date_depot_utc="2000-06-15T12:00:00Z",
                    bassin=b,
                    auteurs=eq,
                    macros=(),
                    expressions_brutes=exprs,
                )
            )

    # 1. Cas positif sain : schéma de mutation d'amas sous macros locales différentes
    # dans b1_positivite_totale et b2_systemes_somos par des équipes strictement disjointes
    patron_cible = schema_mutation_amas_cible()
    for idx_b, (b, nom_macro) in enumerate(
        (("b1_positivite_totale", "\\echBruhat"), ("b2_systemes_somos", "\\recSomos"))
    ):
        for k in range(4):
            eq = nouvelle_equipe()
            macro = MacroLocale(nom=nom_macro, arite=5, corps=patron_cible)
            args1 = tuple(_arbre_bruit_aleatoire(rng, profondeur=1) for _ in range(5))
            args2 = tuple(_feuille_aleatoire(rng) for _ in range(5))
            appel1 = ArbreOperateur("=", (_feuille_aleatoire(rng), ArbreOperateur(nom_macro, args1)))
            appel2 = ArbreOperateur("+", (_feuille_aleatoire(rng), ArbreOperateur(nom_macro, args2)))
            articles.append(
                ArticleMathematique(
                    identifiant=f"sain_{idx_b}_{k}",
                    date_depot_utc="2001-02-10T08:30:00Z",
                    bassin=b,
                    auteurs=eq,
                    macros=(macro,),
                    expressions_brutes=(appel1, appel2),
                )
            )

    # 2. Témoin « doit mourir » 1 : inflation syntaxique massive dans un seul bassin (b3_inflation_mono)
    macro_inf = _inflation_lourde_locale()
    for k in range(6):
        eq = nouvelle_equipe()
        exprs_inf = tuple(
            ArbreOperateur(
                "\\detAdHocLocal",
                tuple(_arbre_bruit_aleatoire(rng, profondeur=1) for _ in range(3)),
            )
            for _ in range(4)
        )
        articles.append(
            ArticleMathematique(
                identifiant=f"inflation_{k}",
                date_depot_utc="2000-11-20T16:00:00Z",
                bassin="b3_inflation_mono",
                auteurs=eq,
                macros=(macro_inf,),
                expressions_brutes=exprs_inf,
            )
        )

    # 3. Témoin « doit mourir » 2 : même équipe d'auteurs publiant sa macro dans deux bassins (b5 et b6)
    equipe_commune = ("auteur_pont_unique_1", "auteur_pont_unique_2")
    corps_pont = ArbreOperateur(
        "croch",
        (
            ArbreOperateur("*", (ArbreOperateur("#0"), ArbreOperateur("#1"))),
            ArbreOperateur("-", (ArbreOperateur("#2"), ArbreOperateur("#0"))),
        ),
    )
    macro_pont = MacroLocale(nom="\\crochPerso", arite=3, corps=corps_pont)
    for b_pont in ("b5_pont_meme_auteur", "b6_cible_meme_auteur"):
        for k in range(3):
            articles.append(
                ArticleMathematique(
                    identifiant=f"meme_auteur_{b_pont}_{k}",
                    date_depot_utc="2000-09-05T10:00:00Z",
                    bassin=b_pont,
                    auteurs=equipe_commune,
                    macros=(macro_pont,),
                    expressions_brutes=(
                        ArbreOperateur("\\crochPerso", tuple(_feuille_aleatoire(rng) for _ in range(3))),
                        ArbreOperateur("\\crochPerso", tuple(_feuille_aleatoire(rng) for _ in range(3))),
                    ),
                )
            )

    par_bassin = preparer_corpus_canonise(articles)
    cocitations = {(b1, b2): 0.01 for i, b1 in enumerate(bassins) for b2 in bassins[i + 1 :]}
    garde_non_degenerescence_corpus(par_bassin, cocitations, seuil_cocitation_max=0.05)

    res_sain = score_compression_inter_bassins(
        par_bassin["b1_positivite_totale"],
        par_bassin["b2_systemes_somos"],
        par_bassin,
        "b1_positivite_totale",
        "b2_systemes_somos",
    )
    res_inflation = score_compression_inter_bassins(
        par_bassin["b3_inflation_mono"],
        par_bassin["b4_temoin_vide"],
        par_bassin,
        "b3_inflation_mono",
        "b4_temoin_vide",
    )
    res_meme_auteur = score_compression_inter_bassins(
        par_bassin["b5_pont_meme_auteur"],
        par_bassin["b6_cible_meme_auteur"],
        par_bassin,
        "b5_pont_meme_auteur",
        "b6_cible_meme_auteur",
    )
    res_ubiquite = score_compression_inter_bassins(
        par_bassin["b7_science_normale_a"],
        par_bassin["b8_science_normale_b"],
        par_bassin,
        "b7_science_normale_a",
        "b8_science_normale_b",
    )

    patron_extrait = res_sain["meilleur_patron_objet"]
    forme_retrouvee = bool(
        patron_extrait is not None
        and sont_isomorphes_modulo_trous(patron_extrait, patron_cible)
    )

    return {
        "sain_score_bits": res_sain["score_specifique_bits"],
        "sain_naif_bits": res_sain["gain_global_naif_bits"],
        "sain_patron": res_sain["meilleur_patron"],
        "sain_forme_mutation_exacte": forme_retrouvee,
        "temoin_inflation_score_bits": res_inflation["score_specifique_bits"],
        "temoin_inflation_naif_bits": res_inflation["gain_global_naif_bits"],
        "temoin_meme_auteur_score_bits": res_meme_auteur["score_specifique_bits"],
        "temoin_meme_auteur_naif_bits": res_meme_auteur["gain_global_naif_bits"],
        "temoin_ubiquite_score_bits": res_ubiquite["score_specifique_bits"],
        "temoin_ubiquite_naif_bits": res_ubiquite["gain_global_naif_bits"],
    }


# ---------------------------------------------------------------------------
# Vérification systématique R5 : cas sain et cas artefact pour chaque garde
# ---------------------------------------------------------------------------

def verifier_gardes_r5() -> dict[str, dict[str, object]]:
    """Exécute et vérifie chaque garde d'arrêt sur un cas sain et sur un artefact."""
    journal: dict[str, dict[str, object]] = {}

    art_sain = ArticleMathematique(
        identifiant="math/0011001",
        date_depot_utc="2000-11-01T18:00:00Z",
        bassin="alg-geom",
        auteurs=("sergey fomin",),
        macros=(MacroLocale("\\mSaine", 1, ArbreOperateur("+", (ArbreOperateur("#0"), ArbreOperateur("1")))),),
        expressions_brutes=(ArbreOperateur("\\mSaine", (ArbreOperateur("x"),)),),
    )

    # Garde 1 : coupure temporelle
    garde_coupure_temporelle([art_sain])
    art_fuite = dataclasses.replace(
        art_sain, identifiant="math/0104151", date_depot_utc="2001-04-13T00:00:00Z"
    )
    artefact_1_bloque = False
    motif_1 = ""
    try:
        garde_coupure_temporelle([art_sain, art_fuite])
    except GardeArret as exc:
        artefact_1_bloque = True
        motif_1 = str(exc)
    if not artefact_1_bloque:
        raise GardeArret("R5 violée : garde_coupure_temporelle a laissé passer math/0104151")
    journal["garde_coupure_temporelle"] = {
        "cas_sain_accepte": True,
        "cas_artefact_bloque": artefact_1_bloque,
        "motif_artefact": motif_1,
    }

    # Garde 2 : expansion acyclique des macros
    expr_exp = garde_expansion_macros_acyclique(
        art_sain.expressions_brutes[0], {"\\mSaine": art_sain.macros[0]}
    )
    if expr_exp.vers_chaine_lisp() != "(+ x 1)":
        raise GardeArret(f"expansion saine incorrecte : {expr_exp.vers_chaine_lisp()}")
    macros_cycle = {
        "\\a": MacroLocale("\\a", 1, ArbreOperateur("\\b", (ArbreOperateur("#0"),))),
        "\\b": MacroLocale("\\b", 1, ArbreOperateur("\\a", (ArbreOperateur("#0"),))),
    }
    artefact_2_bloque = False
    motif_2 = ""
    try:
        garde_expansion_macros_acyclique(
            ArbreOperateur("\\a", (ArbreOperateur("x"),)), macros_cycle
        )
    except GardeArret as exc:
        artefact_2_bloque = True
        motif_2 = str(exc)
    if not artefact_2_bloque:
        raise GardeArret("R5 violée : garde_expansion_macros_acyclique n'a pas bloqué un cycle")
    journal["garde_expansion_macros_acyclique"] = {
        "cas_sain_accepte": True,
        "cas_artefact_bloque": artefact_2_bloque,
        "motif_artefact": motif_2,
    }

    # Garde 3 : disjonction et intégrité des auteurs
    classes_ok = garde_disjonction_auteurs([art_sain])
    if len(classes_ok) != 1:
        raise GardeArret("échec inattendu sur auteurs sains")
    art_sans_auteur = dataclasses.replace(art_sain, auteurs=())
    artefact_3_bloque = False
    motif_3 = ""
    try:
        garde_disjonction_auteurs([art_sans_auteur])
    except GardeArret as exc:
        artefact_3_bloque = True
        motif_3 = str(exc)
    if not artefact_3_bloque:
        raise GardeArret("R5 violée : garde_disjonction_auteurs a toléré un article sans auteur")
    journal["garde_disjonction_auteurs"] = {
        "cas_sain_accepte": True,
        "cas_artefact_bloque": artefact_3_bloque,
        "motif_artefact": motif_3,
    }

    # Garde 4 : non-dégénérescence du corpus et des co-citations
    paires_ok = garde_non_degenerescence_corpus(
        {"b1": [(0, expr_exp)], "b2": [(1, expr_exp)]},
        {("b1", "b2"): 0.02},
    )
    if paires_ok != [("b1", "b2")]:
        raise GardeArret("échec inattendu sur corpus sain à deux bassins")
    artefact_4_bloque = False
    motif_4 = ""
    try:
        garde_non_degenerescence_corpus(
            {"b1": [(0, ArbreOperateur("NaN"))], "b2": [(1, expr_exp)]},
            {("b1", "b2"): 0.02},
        )
    except GardeArret as exc:
        artefact_4_bloque = True
        motif_4 = str(exc)
    if not artefact_4_bloque:
        raise GardeArret("R5 violée : garde_non_degenerescence_corpus a toléré un nœud NaN")
    journal["garde_non_degenerescence_corpus"] = {
        "cas_sain_accepte": True,
        "cas_artefact_bloque": artefact_4_bloque,
        "motif_artefact": motif_4,
    }

    return journal


def aire_mann_whitney(positifs: Sequence[float], negatifs: Sequence[float]) -> float:
    """Statistique de Mann-Whitney exacte (ex aequo comptés pour moitié)."""
    if not positifs or not negatifs:
        raise GardeArret("échantillon vide dans aire_mann_whitney")
    total = 0.0
    for xp in positifs:
        for xn in negatifs:
            if xp > xn:
                total += 1.0
            elif xp == xn:
                total += 0.5
    return total / (len(positifs) * len(negatifs))


def executer_banc_complet(nb_replications: int = 40, dossier_sortie: Path | None = None) -> dict[str, object]:
    """Lance la vérification R5 des gardes puis le banc Monte-Carlo à graine scellée."""
    version_np = exiger_numpy_minimal()
    gardes_r5 = verifier_gardes_r5()

    seq = np.random.SeedSequence(ENTROPIE_GRAINE_MACROS)
    enfants = seq.spawn(nb_replications)

    sains, inflations, memes_auteurs, ubiquites = [], [], [], []
    naifs_inflation, naifs_sain = [], []
    formes_exactes = 0
    exemple_patron = None

    for i, graine_enfant in enumerate(enfants):
        rng = np.random.default_rng(graine_enfant)
        res = simuler_monde_plante(rng)
        sains.append(float(res["sain_score_bits"]))
        naifs_sain.append(float(res["sain_naif_bits"]))
        inflations.append(float(res["temoin_inflation_score_bits"]))
        naifs_inflation.append(float(res["temoin_inflation_naif_bits"]))
        memes_auteurs.append(float(res["temoin_meme_auteur_score_bits"]))
        ubiquites.append(float(res["temoin_ubiquite_score_bits"]))
        if res["sain_forme_mutation_exacte"]:
            formes_exactes += 1
        if i == 0:
            exemple_patron = res["sain_patron"]

    seuil_detection_bits = 40.0
    taux_vrais_positifs = sum(x >= seuil_detection_bits for x in sains) / nb_replications
    taux_fp_inflation = sum(x >= seuil_detection_bits for x in inflations) / nb_replications
    taux_fp_meme_auteur = sum(x >= seuil_detection_bits for x in memes_auteurs) / nb_replications
    taux_fp_ubiquite = sum(x >= seuil_detection_bits for x in ubiquites) / nb_replications
    taux_piege_naif_inflation = sum(x >= seuil_detection_bits for x in naifs_inflation) / nb_replications

    auc_contre_inflation = aire_mann_whitney(sains, inflations)
    auc_contre_meme_auteur = aire_mann_whitney(sains, memes_auteurs)
    auc_contre_ubiquite = aire_mann_whitney(sains, ubiquites)

    if taux_vrais_positifs < 0.95:
        raise GardeArret(f"épreuve plantée échouée : rappel sur cas sain trop bas ({taux_vrais_positifs})")
    if max(taux_fp_inflation, taux_fp_meme_auteur, taux_fp_ubiquite) > 0.05:
        raise GardeArret("épreuve plantée échouée : un témoin « doit mourir » dépasse 5 % de fausses alertes")
    if formes_exactes / nb_replications < 0.95:
        raise GardeArret("épreuve plantée échouée : schéma de mutation d'amas non reconstruit")

    bilan = {
        "module": "epreuve_plantee_macros_arbres_v1.py",
        "identifiant_registre": "IDE-2026-11-23-032",
        "numpy_version": version_np,
        "entropie_seed_sequence": ENTROPIE_GRAINE_MACROS,
        "date_coupure_stricte_utc": DATE_COUPURE_FOMIN_ZELEVINSKY,
        "nb_replications_monte_carlo": nb_replications,
        "seuil_detection_bits": seuil_detection_bits,
        "gardes_r5": gardes_r5,
        "resultats_monde_plante": {
            "cas_sain_mutation_amas": {
                "moyenne_bits": round(float(np.mean(sains)), 4),
                "ecart_type_bits": round(float(np.std(sains, ddof=1)), 4),
                "min_bits": round(float(np.min(sains)), 4),
                "max_bits": round(float(np.max(sains)), 4),
                "gain_naif_moyen_bits": round(float(np.mean(naifs_sain)), 4),
                "taux_detection": round(taux_vrais_positifs, 4),
                "taux_reconstruction_forme_exacte": round(formes_exactes / nb_replications, 4),
                "patron_extrait_exemple": exemple_patron,
            },
            "temoin_doit_mourir_1_inflation_mono_bassin": {
                "score_specifique_moyen_bits": round(float(np.mean(inflations)), 4),
                "gain_global_naif_moyen_bits": round(float(np.mean(naifs_inflation)), 4),
                "taux_fausses_alertes_notre_score": round(taux_fp_inflation, 4),
                "taux_fausses_alertes_compression_naive": round(taux_piege_naif_inflation, 4),
                "aire_separation_contre_sain": round(auc_contre_inflation, 4),
            },
            "temoin_doit_mourir_2_meme_equipe_auteurs": {
                "score_specifique_moyen_bits": round(float(np.mean(memes_auteurs)), 4),
                "taux_fausses_alertes": round(taux_fp_meme_auteur, 4),
                "aire_separation_contre_sain": round(auc_contre_meme_auteur, 4),
            },
            "temoin_doit_mourir_3_ubiquite_science_normale": {
                "score_specifique_moyen_bits": round(float(np.mean(ubiquites)), 4),
                "taux_fausses_alertes": round(taux_fp_ubiquite, 4),
                "aire_separation_contre_sain": round(auc_contre_ubiquite, 4),
            },
        },
        "verdict_epreuve_r5": "CONFORME — 4/4 GARDES R5 VALIDÉES (SAIN/ARTEFACT) ET 3/3 TÉMOINS DOIT MOURIR ÉLIMINÉS",
    }

    if dossier_sortie is not None:
        dossier_sortie = Path(dossier_sortie)
        dossier_sortie.mkdir(parents=True, exist_ok=True)
        chemin_json = dossier_sortie / "sortie_epreuve_plantee_macros_arbres_v1.json"
        contenu = json.dumps(bilan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        chemin_json.write_text(contenu, encoding="utf-8")
        empreinte = hashlib.sha256(chemin_json.read_bytes()).hexdigest()
        (dossier_sortie / "sortie_epreuve_plantee_macros_arbres_v1.json.sha256").write_text(
            f"{empreinte}  {chemin_json.name}\n", encoding="utf-8"
        )

    return bilan


if __name__ == "__main__":
    sortie_dir = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path(__file__).resolve().parent
    )
    resultat = executer_banc_complet(nb_replications=40, dossier_sortie=sortie_dir)
    print(json.dumps(resultat, ensure_ascii=False, indent=2))
