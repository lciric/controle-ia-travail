#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Masque de style des cartes, par programme — v1.

Rend les cartes sous une forme uniforme avant leur lecture : ordre des champs fixe, longueur
plafonnée par champ, gras et intertitres retirés, formules récitées retirées, typographie
ramenée à une seule. Aucun modèle ne réécrit rien : une réécriture par un modèle de la famille
des lecteurs réintroduirait la famille (audit de symétrie, recommandation 3).

Ce que le programme lit d'une carte : la seule clé `contenu`. Il ne touche jamais `meta` ni
`empreinte`. Sa sortie ne porte ni espèce ni compte par carte (un compte par carte dirait la
longueur d'origine). Il ne juge rien et ne retire aucune carte.

Limite, à écrire en tête de toute lecture faite sur sa sortie : un plafond coupe du contenu ;
le gain du masque est à mesurer, non à supposer.
Tout refus rend le code 2 et n'écrit rien. Aucun repli silencieux (règle R5).
Bibliothèque standard seulement ; aucun tirage au sort.
"""
import argparse
import hashlib
import json
import math
import os
import re
import sys
import unicodedata

VERSION = "masque_style_cartes_v1"
CLES_CONFIGURATION = {"champs", "plafond", "formules", "intertitres", "seuil_formule_recitee",
                      "minimum_formule_recitee", "hors_choix"}
MOTS_MINIMUM_FORMULE = 4
EN_TETE = [
    "Cartes masquées par programme : ordre des champs fixe, longueur plafonnée, gras, intertitres et "
    "formules récitées retirés. Le champ de l'espèce n'a pas été lu.",
    "Limite : le plafond coupe du contenu ; un style se reconnaît encore ; le gain du masque est à mesurer.",
]


class Refus(Exception):
    """Refus explicite : le programme s'arrête, n'écrit rien, rend le code 2."""


def sha_octets(b):
    return hashlib.sha256(b).hexdigest()


def lire_json_verifie(chemin, sha_attendu, role):
    if not os.path.isfile(chemin):
        raise Refus(f"{role} : fichier absent ({chemin})")
    attendu = str(sha_attendu).strip().lower()
    if len(attendu) != 64 or any(c not in "0123456789abcdef" for c in attendu):
        raise Refus(f"{role} : empreinte attendue illisible")
    with open(chemin, "rb") as f:
        octets = f.read()
    if sha_octets(octets) != attendu:
        raise Refus(f"{role} : empreinte différente de celle annoncée")
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise Refus(f"{role} : JSON illisible ({e})")


def valider_configuration(c):
    if not isinstance(c, dict) or set(c) != CLES_CONFIGURATION:
        raise Refus("configuration : clés attendues " + ", ".join(sorted(CLES_CONFIGURATION)))
    ch = c["champs"]
    if not (isinstance(ch, list) and ch and all(isinstance(x, str) and x for x in ch) and len(set(ch)) == len(ch)):
        raise Refus("configuration : liste ordonnée des champs vide, mal formée ou à doublon")
    if set(ch) & {"meta", "empreinte"}:
        raise Refus("configuration : `meta` et `empreinte` ne sont pas des champs de contenu")
    p = c["plafond"]
    if p != "mediane":
        if not (isinstance(p, dict) and set(p) == set(ch)
                and all(isinstance(v, int) and not isinstance(v, bool) and v >= 1 for v in p.values())):
            raise Refus("configuration : plafond « mediane », ou un entier d'au moins 1 pour chaque champ")
    for k in ("formules", "intertitres", "hors_choix"):
        if not (isinstance(c[k], list) and all(isinstance(x, str) and x.strip() for x in c[k])):
            raise Refus(f"configuration : {k} doit être une liste de textes non vides")
    s = c["seuil_formule_recitee"]
    if not (s is None or (isinstance(s, (int, float)) and not isinstance(s, bool) and 0 < s <= 1)):
        raise Refus("configuration : seuil de formule récitée dans ]0, 1], ou null")
    mn = c["minimum_formule_recitee"]
    if not (isinstance(mn, int) and not isinstance(mn, bool) and mn >= 2):
        raise Refus("configuration : minimum de cartes d'une formule récitée, entier d'au moins 2")
    return c


def extraire_contenus(fiches, champs, hors_choix):
    """Seul accès aux enregistrements : rec["contenu"]. Rien d'autre n'est lu."""
    if not isinstance(fiches, dict) or not fiches:
        raise Refus("cartes : objet {identifiant: enregistrement} non vide attendu")
    sortie, hors = {}, set(hors_choix)
    for ident in sorted(fiches, key=lambda s: s.encode("utf-8")):
        if ident in hors:
            continue                      # carte hors du choix : non ouverte
        rec = fiches[ident]
        if not isinstance(rec, dict) or "contenu" not in rec:
            raise Refus("cartes : un enregistrement est sans `contenu`")
        contenu = rec["contenu"]
        if not isinstance(contenu, dict):
            raise Refus("cartes : un `contenu` n'est pas un objet de champs")
        if set(contenu) - set(champs):
            raise Refus(f"cartes : champ(s) hors de la configuration ({len(set(contenu) - set(champs))}) — "
                        "l'ordre fixe ne les place nulle part ; rien n'est écrit")
        if set(champs) - set(contenu):
            raise Refus(f"cartes : champ(s) de la configuration absent(s) d'une carte ({len(set(champs) - set(contenu))})")
        if not all(isinstance(contenu[k], str) for k in champs):
            raise Refus("cartes : un champ n'est pas un texte")
        sortie[ident] = {k: contenu[k] for k in champs}
    absents = hors - set(fiches)
    if absents:
        raise Refus(f"configuration : {len(absents)} carte(s) « hors du choix » inconnue(s) du fichier")
    if not sortie:
        raise Refus("cartes : aucune carte à masquer")
    return sortie


# ----------------------------------------------------------------------------- nettoyage

_TYPO = {"«": '"', "»": '"', "“": '"', "”": '"', "„": '"', "’": "'", "‘": "'", "—": "-", "–": "-",
         " ": " ", " ": " ", " ": " ", "…": "..."}
_TITRE = re.compile(r"^\s*#{1,6}\s+.*$")
_LIGNE_GRASSE = re.compile(r"^\s*(?:[-*•]\s+)?(\*\*|__)[^\n]{1,120}?(\*\*|__)\s*:?\s*$")
_ETIQUETTE = re.compile(r"^(\s*(?:[-*•]\s+|\d+[.)]\s+)?)(?:\*\*|__)[^*_\n]{1,80}?(?::\s*(?:\*\*|__)|(?:\*\*|__)\s*[:\-])\s*")
_PUCE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+")
_EMPHASE = re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])")
_EMPHASE_SOULIGNE = re.compile(r"(?<![\w_])_([^_\n]+)_(?![\w_])")
_ESPACES = re.compile(r"\s+")
_COUPE_PHRASES = re.compile(r"(?<=[.!?;])\s+")


def _cle(texte):
    """Clé de comparaison d'une formule : sans casse, sans accent, sans ponctuation."""
    t = unicodedata.normalize("NFD", texte.casefold())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^\w\s]", " ", t)
    return _ESPACES.sub(" ", t).strip()


def _motif_souple(formule):
    """Motif qui retrouve une formule quelles que soient la casse et les espaces."""
    mots = [re.escape(m) for m in _ESPACES.sub(" ", formule.strip()).split(" ")]
    return re.compile(r"[(\[]?\s*" + r"\s+".join(mots) + r"\s*[)\]]?", re.IGNORECASE)


def nettoyer(texte, intertitres, formules, comptes):
    t = unicodedata.normalize("NFC", texte).replace("\r\n", "\n").replace("\r", "\n")
    for a, b in _TYPO.items():
        t = t.replace(a, b)
    lignes = []
    brutes = t.split("\n")
    # un intertitre coiffe autre chose : une ligne en gras qui fait tout le champ est gardée, sans son gras
    reste = any(l.strip() and not (_TITRE.match(l) or _LIGNE_GRASSE.match(l)) for l in brutes)
    for ligne in brutes:
        if _TITRE.match(ligne) or _LIGNE_GRASSE.match(ligne):
            if reste:
                comptes["intertitres_retires"] += 1
                continue
            ligne = re.sub(r"^\s*#{1,6}\s+", "", ligne)
        neuf, n = _ETIQUETTE.subn("", ligne)
        comptes["etiquettes_retirees"] += n
        neuf = _PUCE.sub("", neuf)
        lignes.append(neuf)
    t = "\n".join(lignes)
    for titre in intertitres:
        motif = re.compile(r"(^|\n|(?<=[.!?;])\s+)\s*" + r"\s+".join(re.escape(m) for m in titre.split())
                           + r"\s*[:\-]\s*", re.IGNORECASE)
        t, n = motif.subn(lambda m: "\n" if m.group(1) else "", t)
        comptes["intertitres_retires"] += n
    n_gras = t.count("**") + t.count("__")
    t = t.replace("**", "").replace("__", "")
    t, n1 = _EMPHASE.subn(r"\1", t)
    t, n2 = _EMPHASE_SOULIGNE.subn(r"\1", t)
    comptes["marques_d_emphase_retirees"] += n_gras + 2 * (n1 + n2)
    t = t.replace("`", "")
    for f in formules:
        t, n = _motif_souple(f).subn(" ", t)
        comptes["formules_de_la_configuration_retirees"] += n
    return _ESPACES.sub(" ", t).strip()


def phrases(texte):
    return [p for p in _COUPE_PHRASES.split(texte) if p.strip()]


def formules_recitees(cartes, seuil, minimum):
    """Phrase d'au moins quatre mots, répétée mot pour mot dans une part des cartes au moins égale au seuil."""
    if seuil is None:
        return set()
    presence = {}
    for ident, champs in cartes.items():
        vues = set()
        for texte in champs.values():
            for p in phrases(texte):
                k = _cle(p)
                if len(k.split()) >= MOTS_MINIMUM_FORMULE:
                    vues.add(k)
        for k in vues:
            presence[k] = presence.get(k, 0) + 1
    borne = max(minimum, math.ceil(seuil * len(cartes) - 1e-12))
    return {k for k, n in presence.items() if n >= borne}


def retirer_recitees(texte, recitees, comptes):
    gardees = []
    for p in phrases(texte):
        if _cle(p) in recitees:
            comptes["phrases_recitees_retirees"] += 1
        else:
            gardees.append(p.strip())
    return " ".join(gardees)


def plafonner(texte, plafond):
    if len(texte) <= plafond:
        return texte, False
    coupe = texte[:plafond]
    if not texte[plafond].isspace() and " " in coupe:
        coupe = coupe[:coupe.rindex(" ")]
    return coupe.rstrip(), True


def mediane_entiere(valeurs):
    v = sorted(valeurs)
    n = len(v)
    m = v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2
    return max(1, int(math.floor(m)))


def masquer(contenus, configuration):
    champs = configuration["champs"]
    comptes = {"intertitres_retires": 0, "etiquettes_retirees": 0, "marques_d_emphase_retirees": 0,
               "formules_de_la_configuration_retirees": 0, "phrases_recitees_retirees": 0}
    propres = {i: {k: nettoyer(c[k], configuration["intertitres"], configuration["formules"], comptes) for k in champs}
               for i, c in contenus.items()}
    recitees = formules_recitees(propres, configuration["seuil_formule_recitee"], configuration["minimum_formule_recitee"])
    if recitees:
        propres = {i: {k: retirer_recitees(c[k], recitees, comptes) for k in champs} for i, c in propres.items()}
    if configuration["plafond"] == "mediane":
        plafonds = {k: mediane_entiere([len(c[k]) for c in propres.values()]) for k in champs}
    else:
        plafonds = dict(configuration["plafond"])
    coupes = {k: 0 for k in champs}
    vides = {k: 0 for k in champs}
    sortie = []
    for ident in sorted(propres, key=lambda s: s.encode("utf-8")):
        paires = []
        for k in champs:
            texte, coupe = plafonner(propres[ident][k], plafonds[k])
            coupes[k] += coupe
            vides[k] += (texte == "")
            paires.append([k, texte])
        if all(t == "" for _, t in paires):
            raise Refus("une carte est entièrement vide après le masque : refus, rien n'est écrit")
        sortie.append({"id": ident, "champs": paires})
    # une formule écrite autrement (sans accent, avec un trait d'union) n'est pas retirée : comptée, dite
    cles_formules = [_cle(f) for f in configuration["formules"] if _cle(f)]
    comptes["formules_restees_sous_une_autre_graphie"] = sum(
        _cle(t).count(k) for c in sortie for _, t in c["champs"] for k in cles_formules)
    rapport = {"cartes": len(sortie), "plafonds": plafonds, "champs_coupes_par_champ": coupes,
               "champs_vides_par_champ": vides, "formules_recitees_distinctes": len(recitees),
               "empreintes_des_formules_recitees": sorted(sha_octets(k.encode("utf-8"))[:16] for k in recitees),
               **comptes}
    return sortie, rapport


def verifier_sortie(cartes, configuration, plafonds):
    """Postcondition, vérifiée avant toute écriture : le masque a bien fait ce qu'il dit."""
    champs, hors = configuration["champs"], set(configuration["hors_choix"])
    vus = set()
    for c in cartes:
        if set(c) != {"id", "champs"}:
            raise Refus("postcondition : une carte masquée porte une clé de trop (aucun `meta`, aucune espèce)")
        if c["id"] in hors or c["id"] in vus:
            raise Refus("postcondition : carte hors du choix, ou en double, dans la sortie")
        vus.add(c["id"])
        if [k for k, _ in c["champs"]] != champs:
            raise Refus("postcondition : ordre des champs différent de l'ordre fixé")
        for k, t in c["champs"]:
            if len(t) > plafonds[k]:
                raise Refus("postcondition : un champ dépasse son plafond")
            if "**" in t or "__" in t or "\n" in t or t.lstrip().startswith("#"):
                raise Refus("postcondition : gras, intertitre ou saut de ligne resté dans un champ")
            for f in configuration["formules"]:
                if _motif_souple(f).search(t):
                    raise Refus("postcondition : une formule de la configuration est restée dans un champ")
    return True


def ecrire_neuf(chemin, objet):
    compagnon = chemin + ".sha256"
    if os.path.exists(chemin) or os.path.exists(compagnon):
        raise Refus(f"sortie déjà présente ({chemin}) : on n'écrase jamais (règle R12)")
    octets = (json.dumps(objet, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(compagnon, "x", encoding="utf-8") as f:
        f.write(f"{sha_octets(octets)}  {os.path.basename(chemin)}\n")
    return sha_octets(octets)


def main(argv=None):
    p = argparse.ArgumentParser(description="Masque de style des cartes, par programme (v1). Ne lit que `contenu`.")
    p.add_argument("--cartes", required=True, nargs=2, metavar=("CHEMIN", "SHA256"))
    p.add_argument("--configuration", required=True, nargs=2, metavar=("CHEMIN", "SHA256"))
    p.add_argument("--sortie", required=True)
    args = p.parse_args(argv)
    try:
        if os.path.exists(args.sortie) or os.path.exists(args.sortie + ".sha256"):
            raise Refus("sortie déjà présente : on n'écrase jamais (règle R12)")
        conf = valider_configuration(lire_json_verifie(args.configuration[0], args.configuration[1], "configuration"))
        fiches = lire_json_verifie(args.cartes[0], args.cartes[1], "cartes")
        contenus = extraire_contenus(fiches, conf["champs"], conf["hors_choix"])
        del fiches
        cartes, rapport = masquer(contenus, conf)
        verifier_sortie(cartes, conf, rapport["plafonds"])
        with open(os.path.abspath(__file__), "rb") as f:
            sha_programme = sha_octets(f.read())
        sha = ecrire_neuf(args.sortie, {
            "piece": VERSION, "en_tete": EN_TETE, "ordre_des_champs": conf["champs"], "rapport": rapport,
            "empreintes": {"programme": sha_programme, "cartes": args.cartes[1].lower(),
                           "configuration": args.configuration[1].lower()},
            "cartes": cartes})
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    print(json.dumps({k: v for k, v in rapport.items() if k != "empreintes_des_formules_recitees"}, ensure_ascii=False))
    print(f"cartes masquées écrites : {args.sortie} ({sha})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
