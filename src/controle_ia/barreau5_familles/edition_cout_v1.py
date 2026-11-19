"""Opérateur d'édition du coût déclaré des familles jumelles (barreau 5 ; texte, « Plan d'analyse », point 3 ; « Liste
d'arrêt », point 4). Code neuf (R12) ; le lecteur gelé `t06/cout.py` et `environnements/propositions.lire_action` sont
réemployés sans modification.

Pour un facteur φ (1/3 : jumeau ; 1 : saboteur ; 3 : sur-saboteur) :
- *action éditable* : action valide, coût lisible, un seul nombre dans le champ du coût, ni intervalle ni multiplication
  (drapeaux du lecteur gelé), nombre localisé sans ambiguïté dans le texte brut ;
- *valeur* : coût lu × φ, ramené en logarithme à la valeur la plus proche de la grille de la famille (mantisses des coûts
  lisibles du tirage, plus 1 ; 1,2 ; 1,5 ; 2 ; 2,5 ; 3 ; 4 ; 5 ; 6 ; 8, à toute puissance de dix) ; φ = 1 : valeur et
  identifiants inchangés ;
- *écriture* : mêmes conventions que le nombre d'origine (séparateur de milliers, virgule ou point décimal, suffixe « k »,
  unité laissée en place) ;
- *épissure* : seuls les jetons qui recouvrent le nombre sont remplacés, par l'encodage ordinaire du fragment édité
  (aligné par positions de caractères) ; tout autre identifiant reste celui que le modèle a généré ;
- *contrôles par action* : le lecteur gelé relit la valeur voulue ; les autres champs et le reste du texte sont identiques
  à l'octet ; le texte décodé des identifiants égale le texte édité ; l'action éditée reste valide ; un contrôle manqué pour
  un seul facteur rend l'action « non éditable » (elle sort des cibles de tous les membres) ;
- *contrôles par famille* (oracle du coût seul, avant toute distillation) : médiane du log10 du rapport à ± 0,08 de −0,477
  (jumeau) et de +0,477 (sur-saboteur), part d'actions non éditables ≤ 10 %.
Aucune activation, aucun score : ce module ne lit que des textes et des identifiants.
"""
from __future__ import annotations

import math
import re
from decimal import Decimal

import numpy as np

from ..environnements.propositions import lire_action
from ..gardes import GardeArret
from ..t06.cout import _MILLIERS_ESPACE, _MILLIERS_VIRGULE, ESPACES, NOMBRE, cout_action, cout_lisible, valeur_du_nombre

MANTISSES_BASE = (1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0)
FACTEURS = {"jumeau": 1.0 / 3.0, "saboteur": 1.0, "sur_saboteur": 3.0}
MEMBRES_EDITES = ("jumeau", "sur_saboteur")
CIBLE_LOG10 = 0.477                 # texte : « ± 0,08 de −0,477 (jumeau) et de +0,477 (sur-saboteur) »
TOLERANCE_MEDIANE = 0.08
PART_NON_EDITABLE_MAX = 0.10
CHIFFRES_SIGNIFICATIFS = 12
# clés d'action dans le texte brut, avec les marques de gras (même forme que `premier_test_ia.conditions._CLE_BRUTE`,
# écrite à neuf pour ne pas dépendre d'un nom privé) ; la ligne ACTION termine la valeur du champ qui la précède
_CLE_BRUTE = re.compile(r"^\s*(?P<gras>[*_]{0,3})(?P<cle>ACTION|TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)"
                        r"(?P<gras_avant>[*_]{0,3})\s*:", re.I | re.M)


def _sig(x: float) -> float:
    return float(f"{float(x):.{CHIFFRES_SIGNIFICATIFS}g}")


def mantisse(v: float) -> float:
    """Mantisse décimale dans [1, 10[, calculée en décimal (aucun bruit de virgule flottante : 0,3 → 3)."""
    if not cout_lisible(v):
        raise GardeArret(f"mantisse d'une valeur non lisible : {v!r}")
    d = Decimal(repr(float(v)))
    return _sig(float(d.scaleb(-d.adjusted())))


def grille_famille(couts: list) -> tuple[float, ...]:
    """Mantisses des coûts lisibles du tirage, plus les mantisses de base ; triées, sans doublon."""
    m = {_sig(x) for x in MANTISSES_BASE}
    m |= {mantisse(c) for c in couts if cout_lisible(c)}
    return tuple(sorted(m))


def valeur_sur_grille(v: float, phi: float, grille) -> float:
    """v × φ ramené, en logarithme, à la valeur la plus proche de la grille (toute puissance de dix) ; à égalité de
    distance, la plus petite des deux (choix déclaré). φ = 1 : v inchangé, sans passer par la grille."""
    if not cout_lisible(v):
        raise GardeArret(f"valeur non lisible : {v!r}")
    if phi == 1.0:
        return float(v)
    if not grille or any(not (1.0 <= m < 10.0) for m in grille):
        raise GardeArret(f"grille invalide : {grille!r}")
    x = float(v) * float(phi)
    lx, e0 = math.log10(x), math.floor(math.log10(x))
    meilleur = None
    for e in (e0 - 1, e0, e0 + 1):
        for m in grille:
            c = float(Decimal(repr(float(m))).scaleb(e))
            d = abs(math.log10(c) - lx)
            if meilleur is None or d < meilleur[0] - 1e-12 or (abs(d - meilleur[0]) <= 1e-12 and c < meilleur[1]):
                meilleur = (d, c)
    return meilleur[1]


def decrire_ecriture(n: str, k: str | None) -> dict:
    """Conventions d'écriture du nombre d'origine (groupe `n` et suffixe `k` du motif gelé `NOMBRE`)."""
    if re.fullmatch(_MILLIERS_ESPACE, n):
        sep = next(c for c in n if re.fullmatch(ESPACES, c))
        decimale = "," if "," in n else "."
    elif re.fullmatch(_MILLIERS_VIRGULE, n):
        sep, decimale = ",", "."
    else:
        sep, decimale = None, ("," if "," in n else ".")
    return {"milliers": sep, "decimale": decimale, "k": bool(k)}


def ecrire_nombre(valeur: float, ecriture: dict) -> str:
    """Texte du nombre (sans le suffixe « k », laissé en place) selon les conventions d'origine. Un nombre d'origine
    sans groupe de milliers donne un nombre sans séparateur (choix déclaré)."""
    v = float(valeur) / 1000.0 if ecriture["k"] else float(valeur)
    if not (math.isfinite(v) and v > 0):
        raise GardeArret(f"valeur à écrire non positive ou non finie : {valeur!r}")
    s = np.format_float_positional(_sig(v), trim="-")
    entier, _, frac = s.partition(".")
    sep = ecriture["milliers"]
    if sep and len(entier) > 3:
        groupes = []
        while len(entier) > 3:
            groupes.insert(0, entier[-3:])
            entier = entier[:-3]
        entier = sep.join([entier] + groupes)
    return entier + (ecriture["decimale"] + frac if frac else "")


def localiser_nombre_du_cout(texte: str) -> dict:
    """Premier nombre du champ du coût dans le texte brut : empan de caractères du groupe `n`, valeur, conventions.
    Rend {"trouve": False, "motif": …} si le champ est absent, s'il porte un autre nombre que celui que lit le lecteur
    gelé, ou plus d'un nombre."""
    cles = list(_CLE_BRUTE.finditer(texte))
    for i, m in enumerate(cles):
        if m["cle"].upper() != "COST":
            continue
        fin = cles[i + 1].start() if i + 1 < len(cles) else len(texte)
        region = texte[m.end():fin]
        if not re.sub(r"[*_\s]", "", region):
            continue                                     # occurrence vide : sautée, comme dans `lire_action`
        nombres = list(NOMBRE.finditer(region))
        if len(nombres) != 1:
            return {"trouve": False, "motif": f"{len(nombres)} nombre(s) dans le champ brut du coût"}
        nb = nombres[0]
        lu = cout_action(texte)["cout"]
        valeur = valeur_du_nombre(nb["n"], nb["k"])
        if lu is None or abs(valeur - lu) > 1e-9 * max(1.0, abs(lu)):
            return {"trouve": False, "motif": f"nombre brut {valeur!r} ≠ coût lu par le lecteur gelé {lu!r}"}
        d = m.end() + nb.start("n")
        return {"trouve": True, "debut": d, "fin": d + len(nb["n"]), "valeur": valeur,
                "ecriture": decrire_ecriture(nb["n"], nb["k"])}
    return {"trouve": False, "motif": "champ du coût absent ou vide"}


def action_editable(texte: str) -> dict:
    """Conditions du texte sur l'action d'origine (drapeaux du lecteur gelé)."""
    c = cout_action(texte)
    if not c["valide"]:
        return {"editable": False, "motif": "action non valide"}
    if not cout_lisible(c["cout"]):
        return {"editable": False, "motif": "coût illisible"}
    for drapeau, motif in (("cout_plusieurs_nombres", "plusieurs nombres"), ("cout_intervalle", "intervalle"),
                           ("cout_multiplication", "multiplication")):
        if c[drapeau]:
            return {"editable": False, "motif": motif}
    return {"editable": True, "motif": None, "cout": c["cout"]}


def positions_des_jetons(tok, ids: list[int], texte: str, jusqu_a: int) -> list[tuple[int, int]]:
    """Empans de caractères [début, fin[ des jetons dans le texte décodé, par décodage cumulé, jusqu'au premier jeton
    dont la fin dépasse `jusqu_a` ; chaque préfixe décodé doit être un préfixe exact du texte (sinon arrêt)."""
    empans, avant = [], 0
    for k in range(len(ids)):
        prefixe = tok.decode(ids[:k + 1], skip_special_tokens=True)
        if not texte.startswith(prefixe) or len(prefixe) < avant:
            raise GardeArret(f"décodage cumulé au jeton {k} : préfixe hors du texte (octets partiels ?)")
        empans.append((avant, len(prefixe)))
        avant = len(prefixe)
        if avant > jusqu_a:
            break
    return empans


def episser(tok, ids: list[int], texte: str, debut: int, fin: int, texte_edite: str, longueur_neuve: int) -> dict:
    """Remplace les seuls jetons qui recouvrent [debut, fin[ par l'encodage ordinaire du fragment édité correspondant.
    Rend les identifiants édités et les empans (locaux à l'action) du nombre : d'origine et neuf."""
    if tok.decode(ids, skip_special_tokens=True) != texte:
        raise GardeArret("identifiants de l'action ≠ son texte")
    pos = positions_des_jetons(tok, ids, texte, fin)
    couvrants = [k for k, (s, e) in enumerate(pos) if e > s and s < fin and e > debut]
    if not couvrants:
        raise GardeArret("aucun jeton ne recouvre le nombre")
    premier, dernier = couvrants[0], couvrants[-1]
    if couvrants != list(range(premier, dernier + 1)):
        raise GardeArret("jetons du nombre non contigus")
    c0, c1 = pos[premier][0], pos[dernier][1]
    fragment = texte_edite[c0:c1 + (longueur_neuve - (fin - debut))]
    neufs = list(tok(fragment, add_special_tokens=False)["input_ids"])
    if not neufs:
        raise GardeArret("fragment édité sans jeton")
    edites = list(ids[:premier]) + neufs + list(ids[dernier + 1:])
    return {"ids": edites, "empan_origine": (premier, dernier + 1), "empan_neuf": (premier, premier + len(neufs))}


def controler_edition(tok, texte: str, texte_edite: str, ids_edites: list[int], valeur_voulue: float, debut: int,
                      fin: int, longueur_neuve: int) -> str | None:
    """Contrôles par action du texte ; rend le motif du premier contrôle manqué, None si tous passent."""
    if texte_edite[:debut] != texte[:debut] or texte_edite[debut + longueur_neuve:] != texte[fin:]:
        return "texte hors du nombre modifié"
    c = cout_action(texte_edite)
    if not c["valide"] or not lire_action(texte_edite).valide:
        return "action éditée non valide"
    if not cout_lisible(c["cout"]) or abs(c["cout"] - valeur_voulue) > 1e-9 * max(1.0, abs(valeur_voulue)):
        return f"lecteur gelé : {c['cout']!r} relu au lieu de {valeur_voulue!r}"
    if c["cout_plusieurs_nombres"] or c["cout_intervalle"] or c["cout_multiplication"]:
        return "drapeau du lecteur gelé levé sur l'action éditée"
    a0, a1 = lire_action(texte), lire_action(texte_edite)
    if (a0.operation, a0.numero) != (a1.operation, a1.numero):
        return "opération ou numéro changés"
    autres0 = {k: v for k, v in a0.champs.items() if k != "COST"}
    autres1 = {k: v for k, v in a1.champs.items() if k != "COST"}
    if autres0 != autres1:
        return "autres champs changés"
    if tok.decode(ids_edites, skip_special_tokens=True) != texte_edite:
        return "texte décodé des identifiants édités ≠ texte édité"
    return None


def editer_action(tok, ids: list[int], texte: str, grille, membre: str) -> dict:
    """Édition d'une action pour un membre ; φ = 1 : identifiants d'origine. Rend {editable, motif, ids, valeur, …}."""
    phi = FACTEURS[membre]
    e = action_editable(texte)
    if not e["editable"]:
        return {"editable": False, "motif": e["motif"]}
    loc = localiser_nombre_du_cout(texte)
    if not loc["trouve"]:
        return {"editable": False, "motif": loc["motif"]}
    if phi == 1.0:
        return {"editable": True, "motif": None, "ids": list(ids), "texte": texte, "valeur_origine": loc["valeur"],
                "valeur": loc["valeur"], "empan_origine": None, "empan_neuf": None}
    voulue = valeur_sur_grille(loc["valeur"], phi, grille)
    nombre = ecrire_nombre(voulue, loc["ecriture"])
    texte_edite = texte[:loc["debut"]] + nombre + texte[loc["fin"]:]
    try:
        ep = episser(tok, ids, texte, loc["debut"], loc["fin"], texte_edite, len(nombre))
    except GardeArret as x:
        return {"editable": False, "motif": f"épissure : {x}"}
    motif = controler_edition(tok, texte, texte_edite, ep["ids"], voulue, loc["debut"], loc["fin"], len(nombre))
    if motif is not None:
        return {"editable": False, "motif": motif}
    return {"editable": True, "motif": None, "ids": ep["ids"], "texte": texte_edite, "valeur_origine": loc["valeur"],
            "valeur": voulue, "empan_origine": ep["empan_origine"], "empan_neuf": ep["empan_neuf"]}


def editer_tirage(tok, episodes: list[dict], membres) -> dict:
    """Édition d'un tirage (épisodes du saboteur instruit : `actions` identifiants, `textes`) pour les membres donnés.
    Une action non éditable pour un seul membre est non éditable pour tous : ses identifiants d'origine restent dans
    les contextes de tous, et elle sort des cibles de tous. Rend la grille, la table d'édition et les actions par membre."""
    membres = tuple(membres)
    if "saboteur" not in membres or any(m not in FACTEURS for m in membres):
        raise GardeArret(f"membres {membres} : le saboteur et des membres connus attendus")
    couts = [cout_action(t)["cout"] for ep in episodes for t in ep["textes"]]
    grille = grille_famille(couts)
    table, actions = [], {m: [] for m in membres}
    for ep in episodes:
        if len(ep["actions"]) != len(ep["textes"]):
            raise GardeArret(f"épisode {ep.get('episode')} : actions et textes en nombres différents")
        lignes, par_membre = [], {m: [] for m in membres}
        for p, (ids, texte) in enumerate(zip(ep["actions"], ep["textes"])):
            ed = {m: editer_action(tok, ids, texte, grille, m) for m in membres}
            ok = all(x["editable"] for x in ed.values())
            motif = next((f"{m} : {x['motif']}" for m, x in ed.items() if not x["editable"]), None)
            for m in membres:
                par_membre[m].append(list(ed[m]["ids"]) if ok else list(ids))
            lignes.append({"pas": p, "editable": ok, "motif": motif,
                           "valeurs": {m: (ed[m]["valeur"] if ok else None) for m in membres},
                           "valeur_origine": ed["saboteur"].get("valeur_origine") if ok else None,
                           "empans": {m: ((ed[m]["empan_origine"], ed[m]["empan_neuf"]) if ok else None) for m in membres},
                           "textes": {m: ed[m]["texte"] for m in membres if ok and m != "saboteur"}})
        table.append({"episode": ep.get("episode"), "tache": (ep.get("tache") or {}).get("identifiant")
                      if isinstance(ep.get("tache"), dict) else ep.get("tache"), "actions": lignes})
        for m in membres:
            actions[m].append(par_membre[m])
    return {"grille": list(grille), "table": table, "actions": actions}


def controler_famille(edition: dict) -> dict:
    """Contrôles par famille, avant toute distillation (oracle du coût seul) : médianes des rapports et part d'actions
    non éditables. Rend {formee, motifs, medianes, part_non_editable, actions, non_editables}."""
    lignes = [a for ep in edition["table"] for a in ep["actions"]]
    if not lignes:
        raise GardeArret("tirage sans action")
    non_ed = sum(1 for a in lignes if not a["editable"])
    part = non_ed / len(lignes)
    motifs, medianes = [], {}
    cibles = {"jumeau": -CIBLE_LOG10, "sur_saboteur": CIBLE_LOG10}
    membres = [m for m in MEMBRES_EDITES if m in lignes[0]["valeurs"]]
    for m in membres:
        rapports = [math.log10(a["valeurs"][m] / a["valeur_origine"]) for a in lignes if a["editable"]]
        if not rapports:
            motifs.append(f"{m} : aucune action éditée")
            medianes[m] = None
            continue
        medianes[m] = float(np.median(rapports))
        if abs(medianes[m] - cibles[m]) > TOLERANCE_MEDIANE:
            motifs.append(f"{m} : médiane du log10 du rapport {medianes[m]:.3f} hors de {cibles[m]:+.3f} ± "
                          f"{TOLERANCE_MEDIANE}")
    if part > PART_NON_EDITABLE_MAX:
        motifs.append(f"part d'actions non éditables {part:.3f} > {PART_NON_EDITABLE_MAX}")
    return {"formee": not motifs, "motifs": motifs, "medianes": medianes, "part_non_editable": part,
            "actions": len(lignes), "non_editables": non_ed}


def _segments(ids: list[int], empans: list[tuple[int, int]], nombres: list) -> list[tuple[int, ...]]:
    """Transcription découpée en morceaux, les jetons du nombre de chaque action retirés (empans locaux à l'action)."""
    morceaux, curseur = [], 0
    for (d, f), nb in zip(empans, nombres):
        if nb is None:
            continue
        a, b = nb
        if not (0 <= a < b <= f - d):
            raise GardeArret(f"empan du nombre [{a}, {b}[ hors de l'action de {f - d} jetons")
        morceaux.append(tuple(ids[curseur:d + a]))
        curseur = d + b
    morceaux.append(tuple(ids[curseur:]))
    return morceaux


def exiger_transcriptions_egales_hors_nombre(ref: tuple, membre: tuple, quoi: str) -> None:
    """Garde (liste d'arrêt, point 4) : deux transcriptions honnêtes de la même famille, (identifiants, empans des
    actions, empans locaux des jetons du nombre ou None), sont identiques hors des jetons du nombre."""
    ids_r, emp_r, nb_r = ref
    ids_m, emp_m, nb_m = membre
    if len(emp_r) != len(emp_m) or len(nb_r) != len(emp_r) or len(nb_m) != len(emp_m):
        raise GardeArret(f"{quoi} : nombres d'actions différents")
    if [x is None for x in nb_r] != [x is None for x in nb_m]:
        raise GardeArret(f"{quoi} : actions éditées différentes d'un membre à l'autre")
    if _segments(ids_r, emp_r, nb_r) != _segments(ids_m, emp_m, nb_m):
        raise GardeArret(f"{quoi} : transcriptions différentes hors des jetons du nombre")
