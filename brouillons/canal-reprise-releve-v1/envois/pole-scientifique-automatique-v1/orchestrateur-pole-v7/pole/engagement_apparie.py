"""Engagement « apparié » (v7, versions 23 et 25) — la fiche du pari apparié borné, de bout en bout hors du cycle : construite
et scellée avant toute issue d'épreuve, puis jugée sur la banque de scores (conception v2 § 7 point 1 ; v3 à v6).

`construire(monde, ...)` fixe, **avant** toute lecture de l'épreuve : les contrastes nommés (coefficients vérifiés par la
règle double), τ, la strate, la partie lue, m_max (plafond, D-S27), la garde (cellules A et B, δ), le budget d'entrée
(α_c, m_c ; D-S25 bis), les **seuils**, calculés sur le seul calibrage, et la **clé de l'héritage** (D-S18 : contrastes et
coefficients ; pondération et m_max ; τ ; strate ; comparateurs ; seuils scellés ; population = empreinte de la banque ou
vivier déclaré ; plus la garde). L'empreinte de l'engagement fixe l'ordre secret de lecture.

`evaluer(monde, engagement)` lit la partie d'épreuve : parts, contrastes dans l'ordre secret, garde, e-valeur du minimum
des processus arrêtée au seuil m_c/α_c (`pari_apparie.evaluer`), bornes basses rapportées (jamais une condition).

Version 25 (contre-lecture de la conception v7) : la **partie lue** et la grille **Λ** entrent dans la clé de l'héritage
(K7-3) ; `evaluer` rend l'**empreinte des unités lues** (banque, partie, identifiants), à passer à
`Course.ajouter_trajectoire` qui refuse une répétition (K7-2). Restent à la charge de l'orchestrateur : consigner
l'empreinte de l'engagement **hors de l'objet** (journal, mémoire) avant l'épreuve — le scellement détecte une altération,
il ne l'empêche pas (K7-4) ; et, tant que la garde et les contrastes ne portent pas sur les mêmes unités, les processus
sont alignés par rang et non par unité (K7-6 : niveau tenu, espérance au franchissement joint non garantie ≤ 1).
"""

from . import pari_apparie as pa
from .outils import empreinte_objet


class EngagementInvalide(ValueError):
    pass


def construire(monde, contrastes, tau, alpha_c=0.05, m_c=1, strate=None, partie="epreuve", m_max=None, garde=None,
               population=None):
    """`contrastes` : {nom: {"coefficients": {cellule: a}, "constante": a₀}} — l'affirmation « chaque contraste a une
    espérance > 0 » (intersection-union) ; `garde` : {"a": cellule, "b": cellule, "delta": δ} ou None."""
    if not contrastes:
        raise EngagementInvalide("au moins un contraste")
    if partie == "calibrage":
        raise EngagementInvalide("la partie de calibrage ne se lit jamais comme épreuve")
    cellules = set()
    propres = {}
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
        propres[nom] = {"coefficients": coefficients, "constante": constante}
    if garde is not None:
        if garde.get("a") not in monde.cellules or garde.get("b") not in monde.cellules or not 0.0 < garde.get("delta", 0) < 1.0:
            raise EngagementInvalide("garde : cellules connues et δ dans ]0 ; 1[")
        cellules |= {garde["a"], garde["b"]}
        garde = {"a": garde["a"], "b": garde["b"], "delta": float(garde["delta"])}
    if not (isinstance(m_c, int) and m_c >= 1) or not 0.0 < alpha_c < 1.0:
        raise EngagementInvalide("budget d'entrée : m_c entier ≥ 1, α_c dans ]0 ; 1[")
    if m_max is not None and not (isinstance(m_max, int) and m_max >= 1):
        raise EngagementInvalide("m_max : entier ≥ 1")
    seuils = {c: monde.seuil(c, tau, strate) for c in sorted(cellules)}
    insuffisants = sorted(c for c, s in seuils.items() if s["calibrage_insuffisant"])
    if insuffisants:
        raise EngagementInvalide(f"calibrage insuffisant pour τ = {tau} : {insuffisants}")
    cle = {"contrastes": propres, "ponderation": ("plafond" if m_max is not None else "par_unite"), "m_max": m_max,
           "partie": partie, "lambdas": list(pa.LAMBDAS),
           "tau": tau, "strate": dict(sorted((strate or {}).items())), "comparateurs": sorted(propres),
           "seuils": {c: s["seuil"] for c, s in seuils.items()}, "population": population or monde.empreinte,
           "garde": garde}
    engagement = {"type": "apparie", "cle_heritage": cle, "empreinte_cle": empreinte_objet(cle), "partie": partie,
                  "alpha_c": alpha_c, "m_c": m_c, "seuils_detail": seuils, "monde": monde.empreinte}
    engagement["empreinte"] = empreinte_objet(engagement)
    return engagement


def evaluer(monde, engagement):
    if engagement.get("type") != "apparie" or engagement.get("empreinte") != empreinte_objet(
            {k: v for k, v in engagement.items() if k != "empreinte"}):
        raise EngagementInvalide("engagement altéré ou d'un autre type")
    if engagement["monde"] != monde.empreinte:
        raise EngagementInvalide("engagement scellé sur une autre banque")
    cle = engagement["cle_heritage"]
    parts = monde.parts(cle["seuils"], engagement["partie"], cle["strate"] or None)
    ordre = monde.ordre_secret(parts, engagement["empreinte"])
    valeurs = {nom: monde.contrastes(parts, c["coefficients"], c["constante"], ordre, cle["m_max"])
               for nom, c in cle["contrastes"].items()}
    if len({len(v) for v in valeurs.values()}) != 1:
        raise EngagementInvalide("contrastes sur des unités différentes")
    g = None
    if cle["garde"] is not None:
        g = monde.ecarts_faux_positifs(parts, cle["garde"]["a"], cle["garde"]["b"], ordre)
    r = pa.evaluer(valeurs, ecarts_faux_positifs=g, delta=(cle["garde"] or {}).get("delta"),
                   alpha=engagement["alpha_c"], m=engagement["m_c"])
    r["bornes_basses"] = {nom: pa.borne_basse(v) for nom, v in valeurs.items() if v}
    r["empreinte_cle"] = engagement["empreinte_cle"]
    r["unites_lues"] = len(ordre)
    r["empreinte_unites"] = empreinte_objet({"banque": monde.empreinte, "partie": engagement["partie"],
                                             "unites": sorted(ordre)})
    return r
