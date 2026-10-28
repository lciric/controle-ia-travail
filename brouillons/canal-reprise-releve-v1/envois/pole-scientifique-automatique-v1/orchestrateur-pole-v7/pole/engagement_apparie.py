"""Engagement « apparié » (v7, versions 23, 25, 26, 27 et 28) — la fiche du pari apparié borné, de bout en bout hors du cycle : construite
et scellée avant toute issue d'épreuve, puis jugée sur la banque de scores (conception v2 § 7 point 1 ; v3 à v6).

`construire(monde, ...)` fixe, **avant** toute lecture de l'épreuve : les contrastes nommés (coefficients vérifiés par la
règle double), τ, la strate, la partie lue, m_max (plafond, D-S27), la garde (cellules A et B, δ), le budget d'entrée
(α_c, m_c ; D-S25 bis), les **seuils**, calculés sur le seul calibrage, et la **clé de l'héritage** (D-S18 : contrastes et
coefficients ; pondération et m_max ; τ ; strate ; comparateurs ; seuils scellés ; population = empreinte de la banque ou
vivier déclaré ; plus la garde). L'empreinte de l'engagement fixe l'ordre secret de lecture.

`evaluer(monde, engagement)` lit la partie d'épreuve : parts, contrastes dans l'ordre secret, garde, e-valeur du minimum
des processus arrêtée au seuil m_c/α_c (`pari_apparie.evaluer`), bornes basses rapportées (jamais une condition).

Version 25 (contre-lecture de la conception v7) : la **partie lue** et la grille **Λ** entrent dans la clé de l'héritage
(K7-3) ; `evaluer` rend les **identifiants des unités lues** (banque, partie, unité) et leur empreinte, à passer à
`Course.ajouter_trajectoire(unites=…)` qui refuse toute intersection (K7-2, K8-1 : fraîcheur, pas seulement répétition). Restent à la charge de l'orchestrateur : consigner
l'empreinte de l'engagement **hors de l'objet** (journal, mémoire) avant l'épreuve — le scellement détecte une altération,
il ne l'empêche pas (K7-4) ; et, tant que la garde et les contrastes ne portent pas sur les mêmes unités, les processus
sont alignés par rang et non par unité (K7-6 : niveau tenu, espérance au franchissement joint non garantie ≤ 1).

Version 28 (contre-lecture de la conception v9, K9-1 à K9-6, K9-9) : la clé est **canonique** (contrastes par cellules et
coefficients triés, sans nom libre : renommer un contraste ne fait pas une autre affirmation, K9-3), elle porte la
**version de l'e-processus** (K8-4, K9-4) et le **plan des tranches** (unités par génération, scellé avec l'engagement,
dérivé de la banque et jamais des scores, K9-5) ; `evaluer(monde, engagement, generation=g, fiche=…, journal=…)` lit la
tranche de la génération dans l'ordre dérivé de l'empreinte et de la génération (plus d'étiquette libre), **journalise
lui-même** la partie (K9-6) ; plusieurs gardes, une par comparateur (K9-9) ; identifiants d'unités par l'**identité** de la
banque (K9-2) ; `Lignees` refuse aussi une seconde clé pour une fiche.
"""

from . import pari_apparie as pa
from .outils import empreinte_objet


class EngagementInvalide(ValueError):
    pass


def canonique(coefficients, constante):
    """Forme canonique d'un contraste (K9-3) : cellules triées, coefficients et constante arrondis à 1e-12 ; le nom n'y est pas."""
    return [[c, round(float(a), 12)] for c, a in sorted(coefficients.items())] + [["constante", round(float(constante), 12)]]


def construire(monde, contrastes, tau, alpha_c=0.05, m_c=1, strate=None, partie="epreuve", m_max=None, garde=None,
               population=None, plan_tranches=None):
    """`contrastes` : {nom: {"coefficients": {cellule: a}, "constante": a₀}} — l'affirmation « chaque contraste a une
    espérance > 0 » (intersection-union) ; `garde` : {"a": cellule, "b": cellule, "delta": δ}, ou une **liste** de telles
    gardes (une par comparateur, K9-9), ou None ; `plan_tranches` : {génération (entier) : [unités de la partie]} scellé
    avec l'engagement — tranches disjointes, dérivées de la banque et jamais des scores (K9-5) ; sans plan, la partie
    entière se lit en une fois."""
    if not contrastes:
        raise EngagementInvalide("au moins un contraste")
    if partie == "calibrage":
        raise EngagementInvalide("la partie de calibrage ne se lit jamais comme épreuve")
    cellules = set()
    propres, noms = {}, {}
    for nom, c in sorted(contrastes.items()):
        coefficients, constante = dict(c["coefficients"]), float(c.get("constante", 0.0))
        try:
            pa.verifier_coefficients(coefficients, constante)
        except pa.ContrasteInvalide as e:
            raise EngagementInvalide(f"contraste {nom!r} : {e}") from None
        inconnues = set(coefficients) - set(monde.cellules)
        if inconnues:
            raise EngagementInvalide(f"contraste {nom!r} : cellules inconnues {sorted(inconnues)}")
        cellules |= set(coefficients)
        forme = empreinte_objet(canonique(coefficients, constante))[:16]
        if forme in propres:
            raise EngagementInvalide(f"contraste {nom!r} : même affirmation que {noms[forme]!r} (K9-3)")
        propres[forme] = {"coefficients": coefficients, "constante": constante}
        noms[forme] = nom
    gardes = [] if garde is None else (list(garde) if isinstance(garde, (list, tuple)) else [garde])
    propres_gardes = []
    for g in gardes:
        if g.get("a") not in monde.cellules or g.get("b") not in monde.cellules or not 0.0 < g.get("delta", 0) < 1.0:
            raise EngagementInvalide("garde : cellules connues et δ dans ]0 ; 1[")
        cellules |= {g["a"], g["b"]}
        propres_gardes.append({"a": g["a"], "b": g["b"], "delta": float(g["delta"])})
    propres_gardes.sort(key=lambda g: (g["a"], g["b"], g["delta"]))
    garde = propres_gardes or None
    if plan_tranches is not None:
        if not plan_tranches or any(not isinstance(g, int) or g < 1 for g in plan_tranches):
            raise EngagementInvalide("plan des tranches : générations entières ≥ 1")
        toutes = set(monde.unites(partie))
        vues = set()
        for g, unites_g in plan_tranches.items():
            u = set(unites_g)
            if not u or u - toutes or u & vues:
                raise EngagementInvalide(f"plan des tranches : génération {g} vide, hors partie ou non disjointe")
            vues |= u
        plan_tranches = {str(g): sorted(plan_tranches[g]) for g in sorted(plan_tranches)}
    if not (isinstance(m_c, int) and m_c >= 1) or not 0.0 < alpha_c < 1.0:
        raise EngagementInvalide("budget d'entrée : m_c entier ≥ 1, α_c dans ]0 ; 1[")
    if m_max is not None and not (isinstance(m_max, int) and m_max >= 1):
        raise EngagementInvalide("m_max : entier ≥ 1")
    seuils = {c: monde.seuil(c, tau, strate) for c in sorted(cellules)}
    insuffisants = sorted(c for c, s in seuils.items() if s["calibrage_insuffisant"])
    if insuffisants:
        raise EngagementInvalide(f"calibrage insuffisant pour τ = {tau} : {insuffisants}")
    cle = {"contrastes": propres, "ponderation": ("plafond" if m_max is not None else "par_unite"), "m_max": m_max,
           "partie": partie, "lambdas": list(pa.LAMBDAS), "e_processus": dict(pa.E_PROCESSUS),
           "tau": tau, "strate": dict(sorted((strate or {}).items())), "comparateurs": sorted(propres),
           "seuils": {c: s["seuil"] for c, s in seuils.items()}, "population": population or monde.identite,
           "garde": garde, "plan_tranches": plan_tranches}
    engagement = {"type": "apparie", "cle_heritage": cle, "empreinte_cle": empreinte_objet(cle), "partie": partie,
                  "alpha_c": alpha_c, "m_c": m_c, "seuils_detail": seuils, "monde": monde.empreinte, "noms": noms}
    engagement["empreinte"] = empreinte_objet(engagement)
    return engagement


def evaluer(monde, engagement, generation=None, fiche=None, journal=None, unites=None):
    """Version 28 : la lecture d'une génération se fait par `generation=g` — la tranche est celle du **plan scellé** dans
    l'engagement (K9-5), l'ordre secret est dérivé de l'empreinte de l'engagement et de g (plus d'étiquette libre) ; sans
    plan, la partie entière est lue (génération None) ; `unites` n'est accepté que sans plan et avec une génération
    (tranche dérivée par l'orchestrateur de la banque, jamais des scores — à sa charge, dit). Avec `journal` (un
    `Lignees`), la partie est **journalisée ici même** sous le nom `fiche` (K9-6) ; une seconde évaluation d'une même fiche
    dans une génération est refusée par le journal."""
    if engagement.get("type") != "apparie" or engagement.get("empreinte") != empreinte_objet(
            {k: v for k, v in engagement.items() if k != "empreinte"}):
        raise EngagementInvalide("engagement altéré ou d'un autre type")
    if engagement["monde"] != monde.empreinte:
        raise EngagementInvalide("engagement scellé sur une autre banque")
    cle = engagement["cle_heritage"]
    plan = cle.get("plan_tranches")
    if plan is not None:
        if generation is None or unites is not None:
            raise EngagementInvalide("engagement à plan de tranches : passer generation=g, jamais d'unités libres (K9-5)")
        if str(generation) not in plan:
            raise EngagementInvalide(f"génération {generation} absente du plan des tranches")
        unites = plan[str(generation)]
    elif unites is not None:
        if generation is None:
            raise EngagementInvalide("une tranche libre demande sa génération (ordre dérivé de l'empreinte et de g)")
        absentes = set(unites) - set(monde.unites(engagement["partie"]))
        if absentes:
            raise EngagementInvalide(f"tranche : {len(absentes)} unité(s) hors de la partie {engagement['partie']!r} : "
                                     f"{sorted(map(str, absentes))[:3]}")
    if (journal is None) != (fiche is None):
        raise EngagementInvalide("journal et fiche vont ensemble (K9-6)")
    etiquette = engagement["empreinte"] if generation is None else f"{engagement['empreinte']}|g{int(generation)}"
    parts = monde.parts(cle["seuils"], engagement["partie"], cle["strate"] or None, unites)
    ordre = monde.ordre_secret(parts, etiquette)
    valeurs = {nom: monde.contrastes(parts, c["coefficients"], c["constante"], ordre, cle["m_max"])
               for nom, c in cle["contrastes"].items()}
    if len({len(v) for v in valeurs.values()}) != 1:
        raise EngagementInvalide("contrastes sur des unités différentes")
    g, deltas = None, None
    if cle["garde"]:
        g = {f"{k['a']}-{k['b']}": monde.ecarts_faux_positifs(parts, k["a"], k["b"], ordre) for k in cle["garde"]}
        deltas = {f"{k['a']}-{k['b']}": k["delta"] for k in cle["garde"]}
    r = pa.evaluer(valeurs, ecarts_faux_positifs=g, delta=deltas, alpha=engagement["alpha_c"], m=engagement["m_c"])
    r["log_richesse_finale_par_comparateur"] = {engagement["noms"].get(k, k): v for k, v in r["log_richesse_finale_par_comparateur"].items()}
    r["bornes_basses"] = {engagement["noms"].get(nom, nom): pa.borne_basse(v) for nom, v in valeurs.items() if v}
    r["empreinte_cle"] = engagement["empreinte_cle"]
    r["unites_lues"] = len(ordre)
    # version 26 (K8-1) : les identifiants des unités (banque, partie, unité), à passer à `Course.ajouter_trajectoire(unites=…)`,
    # qui refuse toute intersection avec les unités déjà lues par la fiche ; l'empreinte reste pour le manifeste
    r["identifiants_unites"] = [(monde.identite, engagement["partie"], u) for u in sorted(ordre)]
    r["empreinte_unites"] = empreinte_objet({"banque": monde.identite, "partie": engagement["partie"],
                                             "unites": sorted(ordre)})
    r["generation"] = generation
    if journal is not None:
        journal.journaliser(generation, fiche, r)
    return r


class Lignees:
    """Version 27 — la **mémoire des lignées de clé** (D-S25 bis (5), « à coder » dans la conception v9) : une affirmation
    (clé de l'héritage) n'est portée que par **une** fiche ; une relance sous un autre nom (même clé, autre fiche) est
    refusée — la fiche d'origine garde son budget d'entrée et ses unités lues. Le **journal des parties** (K8-2 : « le
    monde journalise toute partie calculée ») vit ici aussi : `journaliser` est appelé par le monde (ou l'orchestrateur,
    à chaque `evaluer`) avant toute lecture ; `verifier_sans_partie` confronte une déclaration « sans partie » au journal
    et refuse la déclaration mensongère (0,40 puis 0,98 de fausse promotion sinon, contre-lecture de la v8)."""

    def __init__(self):
        self.proprietaire = {}
        self.journal = []

    def entrer(self, fiche, engagement):
        cle = engagement["empreinte_cle"]
        if cle in self.proprietaire and self.proprietaire[cle] != fiche:
            raise EngagementInvalide(f"fiche {fiche!r} : même clé de l'héritage que {self.proprietaire[cle]!r} — relance "
                                     f"sous un autre nom refusée (D-S25 bis (5) : une affirmation, une fiche, un budget)")
        autres = [c for c, f in self.proprietaire.items() if f == fiche and c != cle]
        if autres:
            raise EngagementInvalide(f"fiche {fiche!r} : déjà liée à une autre clé de l'héritage — une fiche, une affirmation (K9-2)")
        self.proprietaire[cle] = fiche

    def journaliser(self, generation, fiche, resultat):
        if any(j["generation"] == generation and j["fiche"] == fiche for j in self.journal):
            raise EngagementInvalide(f"fiche {fiche!r} : seconde évaluation dans la génération {generation} refusée (K9-6)")
        self.journal.append({"generation": generation, "fiche": fiche, "empreinte_unites": resultat["empreinte_unites"],
                             "empreinte_cle": resultat["empreinte_cle"], "unites": len(resultat["identifiants_unites"])})

    def parties_calculees(self, generation):
        return {j["fiche"] for j in self.journal if j["generation"] == generation}

    def verifier_sans_partie(self, generation, sans_partie):
        calculees = self.parties_calculees(generation)
        menteuses = sorted(str(f) for f in (sans_partie or {}) if f in calculees)
        if menteuses:
            raise EngagementInvalide(f"génération {generation} : déclaration « sans partie » contredite par le journal "
                                     f"des parties pour {menteuses[:5]} (K8-2 : toute partie calculée est ajoutée)")
