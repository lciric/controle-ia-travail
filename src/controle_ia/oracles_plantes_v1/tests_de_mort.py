"""Les six tests de mort, fonctions pures sur une proposition et un monde, et la batterie qui les enchaîne.

Issue de chaque test : un type énuméré, un motif, une instance témoin le cas échéant ; jamais un booléen nu.
T1 forme (échec = « informe », pas une mort) ; T2 contre-exemple par énumération exhaustive exacte jusqu'à N ;
T3 vacuité ; T4 trivialité ; T5 redite ; T6 vérification exacte des contre-exemples avancés par le bras
« suite bon marché » (garde G-C : une réfutation déclarée dont aucune instance ne se vérifie ne tue pas, et se
compte « réfutation fausse »). Morte reste morte : registre de lignée (`lignee.py`).
"""
from __future__ import annotations

import itertools
import json
from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction

from .evaluation import F, H, I, V, et3, hypotheses, instance_texte, parcourir, prefixe
from .exact import HorsCapacite, Indefini
from .grammaire import FormeInvalide, analyser, imprimer_expr, lire_sortie
from .normalisation import FAUX, VRAI, Forme, _reconstruire, _vars_expr, normaliser


class TypeIssue(str, Enum):
    # T1
    CONFORME = "conforme"
    INFORME = "informe"
    # lignée
    MORTE_PAR_HERITAGE = "morte_par_heritage"
    # T2
    MORTE_CONTRE_EXEMPLE = "morte_contre_exemple"
    MORTE_CONTRADICTION = "morte_contradiction_avec_les_definitions"
    NON_TUEE = "non_tuee_jusqu_a_N"
    NON_DECIDEE = "non_decidee"
    # T3
    MORTE_VACUITE = "morte_vacuite"
    NON_VACUE = "non_vacue"
    SANS_OBJET = "sans_objet"
    # T4
    TRIVIALE = "triviale"
    NON_TRIVIALE = "non_triviale"
    # T5
    REDITE = "redite"
    NON_REDITE = "non_redite"
    # T6
    CONTRE_EXEMPLE_VERIFIE = "contre_exemple_verifie"
    REFUTATION_FAUSSE = "refutation_fausse"
    SANS_REFUTATION = "sans_refutation_declaree"
    SORTIE_S_INFORME = "sortie_s_informe"


MORTS = {TypeIssue.MORTE_PAR_HERITAGE, TypeIssue.MORTE_CONTRE_EXEMPLE, TypeIssue.MORTE_CONTRADICTION,
         TypeIssue.MORTE_VACUITE, TypeIssue.CONTRE_EXEMPLE_VERIFIE}


@dataclass(frozen=True)
class Issue:
    test: str
    type: TypeIssue
    motif: str
    instance: dict | None = None
    detail: tuple = ()

    def tue(self) -> bool:
        return self.type in MORTS

    def en_dict(self) -> dict:
        d = {"test": self.test, "type": self.type.value, "motif": self.motif}
        if self.instance is not None:
            d["instance"] = instance_texte(self.instance)
        if self.detail:
            d["detail"] = list(self.detail)
        return d


# ---------------------------------------------------------------- T1 forme
def t1_forme(sortie, monde):
    """Rend (issue, arbre ou None, sortie validée ou None)."""
    try:
        d = lire_sortie(sortie)
        arbre = analyser(d["enonce"], monde.vocabulaire())
    except FormeInvalide as e:
        return Issue("T1", TypeIssue.INFORME, str(e)), None, None
    return Issue("T1", TypeIssue.CONFORME, "schéma et grammaire respectés"), arbre, d


# ---------------------------------------------------------------- T2 contre-exemple
def t2_contre_exemple(arbre, monde, borne: int | None = None, forme: Forme | None = None) -> Issue:
    borne = monde.N if borne is None else borne
    vu_h = False
    try:
        for inst, st in parcourir(monde.ev, arbre, borne):
            if st == F:
                return Issue("T2", TypeIssue.MORTE_CONTRE_EXEMPLE, "énoncé faux à cette instance", inst)
            if st == I:
                return Issue("T2", TypeIssue.MORTE_CONTRE_EXEMPLE, "énoncé indéfini à cette instance", inst)
            vu_h |= st == H
    except HorsCapacite as e:
        return Issue("T2", TypeIssue.NON_DECIDEE, f"énumération hors capacité : {e}")
    if forme is not None and forme.noeud == FAUX:
        return Issue("T2", TypeIssue.MORTE_CONTRADICTION, "close à faux par le normaliseur (définitions du monde)")
    if vu_h:
        return Issue("T2", TypeIssue.NON_DECIDEE, "au moins une instance hors capacité, aucune fausse")
    return Issue("T2", TypeIssue.NON_TUEE, f"vrai sur toutes les instances jusqu'à {borne}")


# ---------------------------------------------------------------- T3 vacuité
def t3_vacuite(arbre, monde, borne: int | None = None) -> Issue:
    borne = monde.N if borne is None else borne
    pre, corps = prefixe(arbre)
    hyps, _ = hypotheses(corps)
    n_inst = 0
    vu_h = False
    try:
        for inst, _st in parcourir(monde.ev, arbre, borne, avec_valeur=False):
            if len(inst) < len(pre):  # instance partielle : domaine indéfini ou hors capacité
                continue
            n_inst += 1
            if not hyps:
                return Issue("T3", TypeIssue.SANS_OBJET, "aucune hypothèse ; domaine non vide")
            v = et3(monde.ev.formule(h, inst) for h in hyps)
            if v == V:
                return Issue("T3", TypeIssue.NON_VACUE, "hypothèses satisfaites à cette instance", inst)
            vu_h |= v == H
    except HorsCapacite as e:
        return Issue("T3", TypeIssue.NON_DECIDEE, f"énumération hors capacité : {e}")
    if n_inst == 0:
        return Issue("T3", TypeIssue.MORTE_VACUITE, f"aucune instance du préfixe jusqu'à {borne} (domaine vide)")
    if vu_h:
        return Issue("T3", TypeIssue.NON_DECIDEE, "hypothèses hors capacité sur une instance au moins")
    return Issue("T3", TypeIssue.MORTE_VACUITE, f"aucune instance jusqu'à {borne} ne satisfait les hypothèses")


# ---------------------------------------------------------------- T4 trivialité
SUBSTITUTIONS_MAX = 400


def _noms_fonctions(e, acc):
    if isinstance(e, tuple) and e:
        if e[0] == "fn":
            acc.add(e[1])
        for x in e[1:]:
            _noms_fonctions(x, acc)
    return acc


def _candidats(arbre, liees_prefixe: set):
    """Expressions candidates à une substitution : variables du préfixe, arguments de fonctions, littéraux."""
    toutes_liees = set()

    def liees(e):
        if isinstance(e, tuple) and e:
            if e[0] in ("tout", "existe", "somme", "somme_sur"):
                toutes_liees.add(e[1])
            for x in e[1:]:
                liees(x)

    liees(arbre)
    internes = toutes_liees - liees_prefixe
    vus = {}

    def visiter(e):
        if isinstance(e, tuple) and e:
            if e[0] in ("var", "num", "cst"):
                vus.setdefault(imprimer_expr(e), e)
            if e[0] == "fn":
                for a in e[2]:
                    if not (_vars_expr(a, set()) & internes):
                        vus.setdefault(imprimer_expr(a), a)
            for x in e[1:]:
                visiter(x)

    visiter(arbre)
    return [e for k, e in sorted(vus.items()) if not (e[0] == "var" and e[1] in internes)]


def substituer(f, table: dict):
    if not isinstance(f, tuple) or not f:
        return f
    if f[0] == "var" and f[1] in table:
        return table[f[1]]
    if f[0] == "fn":
        return ("fn", f[1], tuple(substituer(a, table) for a in f[2]))
    if f[0] in ("num", "cst", "NAT", "dom"):
        return f
    return (f[0],) + tuple(substituer(x, table) if isinstance(x, tuple) else x for x in f[1:])


def t4_trivialite(forme: Forme, arbre, monde) -> Issue:
    if forme.noeud == VRAI:
        return Issue("T4", TypeIssue.TRIVIALE, "close à vrai par le normaliseur, sans énumération")
    ax_formes = monde_formes_axiomes(monde)
    for texte, af in ax_formes:
        if af.empreinte == forme.empreinte:
            return Issue("T4", TypeIssue.TRIVIALE, f"énoncé d'un axiome du monde, à renommage près : {texte}")
    pre, _ = prefixe(arbre)
    noms_pre = {v for v, _ in pre}
    fn_prop = _noms_fonctions(arbre, set())
    cands = None
    for (texte, _af), ax in zip(ax_formes, monde.axiomes_ast()):
        pre_ax, corps_ax = prefixe(ax)
        if not pre_ax or len(pre_ax) > 2 or not _noms_fonctions(ax, set()) <= fn_prop:
            continue
        if cands is None:
            cands = _candidats(arbre, noms_pre)
        vars_ax = [v for v, _ in pre_ax]
        for n, combo in enumerate(itertools.product(cands, repeat=len(vars_ax))):
            if n >= SUBSTITUTIONS_MAX:
                break
            corps = substituer(corps_ax, dict(zip(vars_ax, combo)))
            cand = _reconstruire([("tout", v, d) for v, d in pre], corps)
            try:
                cf = normaliser(cand, monde, monde.ev)
            except (KeyError, HorsCapacite, Indefini):
                continue
            if cf.chaine == forme.chaine:
                inst = ", ".join(f"{v} := {imprimer_expr(e)}" for v, e in zip(vars_ax, combo))
                return Issue("T4", TypeIssue.TRIVIALE, f"instance de l'axiome « {texte} » ({inst})")
    return Issue("T4", TypeIssue.NON_TRIVIALE, "ni axiome, ni instance d'axiome, ni close par le normaliseur")


def monde_formes_axiomes(monde):
    if not hasattr(monde, "_formes_axiomes"):
        monde._formes_axiomes = [(t, normaliser(a, monde, monde.ev)) for t, a in zip(monde.axiomes(), monde.axiomes_ast())]
    return monde._formes_axiomes


# ---------------------------------------------------------------- T5 redite
LITTERAUX_MAX = 12


def _peler(noeud):
    sq = []
    while noeud[0] == "Q":
        sq.append((noeud[1], noeud[2]))
        noeud = noeud[4]
    return tuple(sq), noeud


def _litteraux(n, acc):
    g = n[0]
    if g == "A":
        acc.add(n[2])
    elif g == "Q":
        acc.add("Q:" + str(n))
    elif g in ("ET", "OU"):
        for x in n[1]:
            _litteraux(x, acc)
    return acc


def _valeur_prop(n, aff):
    g = n[0]
    if g == "V":
        return True
    if g == "F":
        return False
    if g == "A":
        return aff[n[2]] == n[3]
    if g == "Q":
        return aff["Q:" + str(n)]
    if g == "ET":
        return all(_valeur_prop(x, aff) for x in n[1])
    return any(_valeur_prop(x, aff) for x in n[1])


def equivalence_propositionnelle(a: Forme, b: Forme) -> bool:
    sa, ca = _peler(a.noeud)
    sb, cb = _peler(b.noeud)
    if sa != sb:
        return False
    lits = sorted(_litteraux(ca, set()) | _litteraux(cb, set()))
    if len(lits) > LITTERAUX_MAX:
        return False
    for valeurs in itertools.product((False, True), repeat=len(lits)):
        aff = dict(zip(lits, valeurs))
        if _valeur_prop(ca, aff) != _valeur_prop(cb, aff):
            return False
    return True


def profil(forme: Forme, monde, borne: int):
    """Profil de vérité sur le domaine borné : statuts du corps, instance par instance, dans le monde et dans ses
    mondes perturbés de même structure ; None s'il n'est pas calculable."""
    cle = (forme.empreinte, borne)
    cache = monde.__dict__.setdefault("_profils", {})
    if cle in cache:
        return cache[cle]
    sortie = []
    try:
        for m in [monde] + list(monde.perturbes):
            sortie.append(tuple(st for _i, st in parcourir(m.ev, forme.arbre, borne)))
    except (HorsCapacite, KeyError):
        sortie = None
    cache[cle] = None if sortie is None else tuple(sortie)
    return cache[cle]


def t5_redite(forme: Forme, monde, anterieures: list, borne_profil: int | None = None) -> Issue:
    """`anterieures` : formes des vivantes antérieures du même proposeur ou de la même configuration.

    Le profil se calcule par défaut jusqu'à 3N (borne de vérification) : jusqu'à N seulement, deux vivantes vraies-
    bornées ont le même profil dans le monde réel (toujours vrai) et les seuils monotones se confondent trop souvent
    dans les mondes perturbés (choix provisoire, note de choix)."""
    borne_profil = monde.borne_verification() if borne_profil is None else borne_profil
    for a in anterieures:
        if a.empreinte == forme.empreinte:
            return Issue("T5", TypeIssue.REDITE, "même forme normale qu'une vivante antérieure",
                         detail=(a.empreinte,))
    for a in anterieures:
        if equivalence_propositionnelle(forme, a):
            return Issue("T5", TypeIssue.REDITE, "équivalente (table de vérité sur les atomes normalisés)",
                         detail=(a.empreinte,))
    mon_profil = None
    for a in anterieures:
        if a.squelette != forme.squelette:
            continue
        if mon_profil is None:
            mon_profil = profil(forme, monde, borne_profil)
            if mon_profil is None or len({st for p in mon_profil for st in p}) < 2:
                break  # profil non informatif (constant) : pas de redite par profil
        if profil(a, monde, borne_profil) == mon_profil:
            return Issue("T5", TypeIssue.REDITE, "même profil de vérité sur le domaine borné (monde et mondes perturbés)",
                         detail=(a.empreinte,))
    return Issue("T5", TypeIssue.NON_REDITE, "aucune vivante antérieure équivalente")


# ---------------------------------------------------------------- T6 vérification des contre-exemples de S
CLES_SORTIE_S = ("verdict", "contre_exemples", "raison")


def lire_sortie_s(sortie) -> dict:
    """Sortie structurée du bras « suite bon marché » : verdict (« vrai », « faux » ou « indecis »), contre-exemples
    (liste d'instances : variable du préfixe de tête → entier), raison (texte)."""
    if isinstance(sortie, (str, bytes)):
        try:
            sortie = json.loads(sortie, parse_float=Fraction)
        except (ValueError, TypeError) as e:
            raise FormeInvalide(f"JSON illisible : {e}") from None
    if not isinstance(sortie, dict) or set(sortie) != set(CLES_SORTIE_S):
        raise FormeInvalide(f"clés attendues {sorted(CLES_SORTIE_S)}")
    if sortie["verdict"] not in ("vrai", "faux", "indecis"):
        raise FormeInvalide("verdict hors de {vrai, faux, indecis}")
    if not isinstance(sortie["contre_exemples"], list) or not isinstance(sortie["raison"], str):
        raise FormeInvalide("contre_exemples doit être une liste, raison un texte")
    return sortie


def verifier_instance(arbre, monde, instance, plafond: int):
    """Vérifie exactement une instance avancée comme contre-exemple. Rend (statut, motif) avec statut parmi
    « verifie », « non_verifie », « hors_domaine », « informe », « non_decide »."""
    pre, corps = prefixe(arbre)
    if not isinstance(instance, dict) or set(instance) != {v for v, _ in pre}:
        return "informe", "l'instance doit affecter exactement les variables du préfixe universel de tête"
    env = {}
    for var, dom in pre:
        x = instance[var]
        if isinstance(x, bool) or not isinstance(x, int):
            return "informe", f"valeur non entière pour {var}"
        try:
            if dom[0] == "NAT":
                ok = 0 <= x <= plafond
            else:
                valeurs = monde.ev.valeurs_domaine(dom, env, borne=None)
                ok = x in valeurs
        except (Indefini, HorsCapacite):
            return "hors_domaine", f"domaine de {var} non évaluable"
        if not ok:
            return "hors_domaine", f"{var} = {x} hors de son domaine (NAT tronqué à {plafond})"
        env[var] = Fraction(x)
    st = monde.ev.formule(corps, env)
    if st == F:
        return "verifie", "faux à cette instance (calcul exact)"
    if st == I:
        return "verifie", "indéfini à cette instance (calcul exact)"
    if st == H:
        return "non_decide", "hors capacité à cette instance"
    return "non_verifie", "vrai à cette instance : ce n'est pas un contre-exemple"


def t6_verifier(sortie_s, arbre, monde, plafond: int | None = None) -> Issue:
    plafond = monde.borne_verification() if plafond is None else plafond
    try:
        s = lire_sortie_s(sortie_s)
    except FormeInvalide as e:
        return Issue("T6", TypeIssue.SORTIE_S_INFORME, str(e))
    if s["verdict"] != "faux":
        return Issue("T6", TypeIssue.SANS_REFUTATION, f"verdict déclaré « {s['verdict']} »")
    details = []
    for inst in s["contre_exemples"]:
        statut, motif = verifier_instance(arbre, monde, inst, plafond)
        details.append(f"{statut} : {motif}")
        if statut == "verifie":
            return Issue("T6", TypeIssue.CONTRE_EXEMPLE_VERIFIE, motif,
                         {k: Fraction(v) for k, v in inst.items()}, tuple(details))
    return Issue("T6", TypeIssue.REFUTATION_FAUSSE,
                 "réfutation déclarée dont aucune instance ne se vérifie : ne tue pas (garde G-C)", detail=tuple(details))


# ---------------------------------------------------------------- batterie
@dataclass
class Resultat:
    issues: list = field(default_factory=list)
    statut: str = "informe"  # « informe », « morte », « vivante »
    vraie_bornee: bool = False
    triviale: bool = False
    redite: bool = False
    forme: Forme | None = None
    arbre: tuple | None = None

    def en_dict(self) -> dict:
        return {"statut": self.statut, "vraie_bornee": self.vraie_bornee, "triviale": self.triviale,
                "redite": self.redite, "empreinte_normalisee": self.forme.empreinte if self.forme else None,
                "issues": [i.en_dict() for i in self.issues]}


def appliquer_batterie(sortie, monde, registre=None, anterieures=None, origine=None, borne=None) -> Resultat:
    """T1, lignée, T2, T3, T4, T5 sur une sortie de proposeur ; inscrit l'issue au registre s'il est donné."""
    r = Resultat()
    i1, arbre, _d = t1_forme(sortie, monde)
    r.issues.append(i1)
    if arbre is None:
        return r
    r.arbre = arbre
    r.forme = normaliser(arbre, monde, monde.ev)
    if registre is not None and registre.statut(r.forme.empreinte) == "morte":
        r.issues.append(Issue("lignee", TypeIssue.MORTE_PAR_HERITAGE,
                              "même forme normale qu'une proposition morte : la mort est héritée (D-M5)"))
        r.statut = "morte"
        registre.inscrire(r.forme.empreinte, "morte", "lignee", "héritage", origine)
        return r
    for test in (lambda: t2_contre_exemple(arbre, monde, borne, r.forme), lambda: t3_vacuite(arbre, monde, borne)):
        iss = test()
        r.issues.append(iss)
        if iss.tue():
            r.statut = "morte"
            if registre is not None:
                registre.inscrire(r.forme.empreinte, "morte", iss.test, iss.motif, origine)
            return r
    r.vraie_bornee = r.issues[1].type == TypeIssue.NON_TUEE
    i4 = t4_trivialite(r.forme, arbre, monde)
    r.issues.append(i4)
    r.triviale = i4.type == TypeIssue.TRIVIALE
    i5 = t5_redite(r.forme, monde, anterieures or [])
    r.issues.append(i5)
    r.redite = i5.type == TypeIssue.REDITE
    r.statut = "vivante"
    if registre is not None:
        registre.inscrire(r.forme.empreinte, "vivante", "batterie", "non tuée", origine)
    return r


def sortie_de_texte(texte: str, confiance="1/2", tuerait="une instance du préfixe où l'énoncé est faux") -> dict:
    """Enveloppe un énoncé dans le schéma d'un proposeur (pour la banque plantée et la base aléatoire)."""
    return {"enonce": texte, "ce_qui_le_tuerait": tuerait, "confiance": confiance}


__all__ = ["TypeIssue", "Issue", "Resultat", "t1_forme", "t2_contre_exemple", "t3_vacuite", "t4_trivialite",
           "t5_redite", "t6_verifier", "verifier_instance", "appliquer_batterie", "sortie_de_texte"]
