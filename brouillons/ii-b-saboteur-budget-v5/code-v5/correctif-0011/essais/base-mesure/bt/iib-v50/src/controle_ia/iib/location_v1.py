"""Saboteur à budget : lecture par programme des sorties de l'outil de location, pour `scripts/lancer_iib_v2.sh` (version 2 du lanceur
de session ; corrections de la contre-lecture du 19 novembre 2026). Bibliothèque standard seulement ; lancé comme un fichier
(`python3 -I -B src/controle_ia/iib/location_v1.py SOUS-COMMANDE …`), sans rien importer du dépôt. Aucun appel au loueur.

Trois sous-commandes :
 - `masquer-en-place FICHIER` : masque les secrets d'une sortie du loueur, par analyse de la structure si c'est du JSON sans clé en
   double, par motifs sinon ; le fichier est remplacé par sa forme masquée seulement si tout a réussi ; en échec, il n'est pas touché
   et le code est 1. Le masquage n'est PAS une garde des secrets : la garde des secrets du dépôt reste exigée avant tout versement.
 - `creation FICHIER` : verdict de la réponse de création. L'identifiant créé se lit à la clé de premier niveau `new_contract` de la
   réponse analysée comme JSON, jamais par un motif cherché dans le texte ; toute autre valeur candidate dans la réponse est un refus.
 - `inventaire BRUT TRACE PREFIXE [ID] [REDUIT_D_AVANT]` : lit l'inventaire brut du compte ; écrit dans TRACE (fichier neuf) les seuls
   champs filtrés des instances du saboteur ; remplace BRUT par une forme réduite (identifiant, étiquette, état de chaque instance) ;
   en échec, BRUT n'est pas touché et le code est 1. Un inventaire illisible n'est jamais une preuve."""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone

MASQUE = "***"
CLES_ENVIRONNEMENT = ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY", "CONTAINER_API_KEY")
SENSIBLE = r"(?:key|token|secret|passw|credential|auth|jeton|cookie)"
NOM_SENSIBLE = re.compile(SENSIBLE, re.I)
_NOM = r"[A-Za-z0-9_. -]*" + SENSIBLE + r"[A-Za-z0-9_.-]*"
_VD, _VS, _VE = r'(?:\\.|[^"\\])*', r"(?:\\.|[^'\\])*", r'(?:(?!\\").)*'          # valeur entre guillemets doubles, simples, doubles échappés
MOTIFS = [(re.compile(m, re.I | re.S), r) for m, r in [
    # champs nommés : "NOM": "valeur", 'NOM': 'valeur', \"NOM\": \"valeur\"
    (r'("' + _NOM + r'"\s*:\s*")' + _VD + r'(")', r"\1***\2"),
    (r"('" + _NOM + r"'\s*:\s*')" + _VS + r"(')", r"\1***\2"),
    (r'(\\"' + _NOM + r'\\"\s*:\s*\\")' + _VE + r'(\\")', r"\1***\2"),
    # champs nommés à valeur nue (nombre, mot) : "NOM": 12345
    (r'(\\?["\']' + _NOM + r'\\?["\']\s*:\s*)(?!\\?["\'\[{])(?!true\b|false\b|null\b|None\b|True\b|False\b)[^\s,}\]]+', r"\1***"),
    # paires : ["NOM", "valeur"], ('NOM', 'valeur'), [\"NOM\", \"valeur\"]
    (r'([\[(]\s*"' + _NOM + r'"\s*,\s*")' + _VD + r'(")', r"\1***\2"),
    (r"([\[(]\s*'" + _NOM + r"'\s*,\s*')" + _VS + r"(')", r"\1***\2"),
    (r'([\[(]\s*\\"' + _NOM + r'\\"\s*,\s*\\")' + _VE + r'(\\")', r"\1***\2"),
    # affectations : NOM=valeur, NOM="valeur"
    (r"(\b[A-Za-z0-9_.-]*" + SENSIBLE + r"[A-Za-z0-9_.-]*=\\?[\"']?)(?!\*\*\*)[^\s\"',;&}\\\]]+", r"\1***"),
    # en-têtes d'autorisation et jetons à préfixe connu
    (r"(\b(?:Bearer|Basic)\s+)(?!\*\*\*)[A-Za-z0-9._~+/=-]{8,}", r"\1***"),
    (r"\b(?:hf_[A-Za-z0-9]{8,}|gh[pousr]_[A-Za-z0-9]{8,}|github_pat_[A-Za-z0-9_]{8,}|sk-[A-Za-z0-9_-]{8,}|xox[abprs]-[A-Za-z0-9-]{8,}|AKIA[0-9A-Z]{16}|eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{4,}\.[A-Za-z0-9_-]{4,})", MASQUE),
]]
CHAMPS_FILTRES = ("id", "label", "actual_status", "cur_state", "intended_status", "next_state", "dph_total", "dph_base", "storage_cost",
                  "storage_total_cost", "machine_id", "host_id", "gpu_name", "num_gpus", "disk_space", "start_date")


class Illisible(Exception):
    pass


def _valeurs_environnement() -> list:
    """Chaque valeur de clé connue de l'environnement, avec ses formes échappées en JSON (barres obliques, \\uXXXX)."""
    formes = set()
    for k in CLES_ENVIRONNEMENT:
        v = os.environ.get(k)
        if v and len(v) >= 8:
            echappee = json.dumps(v, ensure_ascii=True)[1:-1]
            formes.update({v, echappee, echappee.replace("/", "\\/"), json.dumps(v, ensure_ascii=False)[1:-1], "".join("\\u%04x" % ord(c) for c in v),
                           "".join("\\u%04X" % ord(c) for c in v)})
    return sorted(formes, key=len, reverse=True)


def masquer_texte(t: str) -> tuple:
    """Masquage par motifs : valeurs des clés de l'environnement, puis champs nommés, paires, affectations, jetons à préfixe."""
    n = 0
    for v in _valeurs_environnement():
        n += t.count(v)
        t = t.replace(v, MASQUE)
    for motif, par in MOTIFS:
        t, k = motif.subn(par, t)
        n += k
    return t, n


def _refuser_les_doubles(paires):
    cles = [k for k, _ in paires]
    if len(set(cles)) != len(cles):
        raise Illisible("clé en double")
    return dict(paires)


def analyser_json(t: str):
    """JSON strict, sans clé en double. Lève Illisible sinon."""
    try:
        return json.loads(t, object_pairs_hook=_refuser_les_doubles)
    except Illisible:
        raise
    except Exception as e:  # noqa: BLE001
        raise Illisible("pas du JSON (" + type(e).__name__ + ")")


def _tout_masquer(v, compte):
    if isinstance(v, dict):
        return {k: _tout_masquer(x, compte) for k, x in v.items()}
    if isinstance(v, list):
        return [_tout_masquer(x, compte) for x in v]
    if v is None or isinstance(v, bool):
        return v
    compte[0] += 1
    return MASQUE


def _masquer_structure(v, compte):
    if isinstance(v, dict):
        return {k: (_tout_masquer(x, compte) if NOM_SENSIBLE.search(str(k)) else _masquer_structure(x, compte)) for k, x in v.items()}
    if isinstance(v, list):
        if len(v) == 2 and isinstance(v[0], str) and NOM_SENSIBLE.search(v[0]) and not isinstance(v[1], (dict, list)):
            return [v[0], _tout_masquer(v[1], compte)]
        return [_masquer_structure(x, compte) for x in v]
    if isinstance(v, str):
        t, k = masquer_texte(v)
        compte[0] += k
        return t
    return v


def masquer(t: str) -> tuple:
    """Rend (texte masqué, nombre de masques, mode). JSON sans clé en double : analyse de la structure ; sinon : motifs."""
    try:
        brut = analyser_json(t)
    except Illisible:
        masque, n = masquer_texte(t)
        return masque, n, "motifs"
    compte = [0]
    masque = json.dumps(_masquer_structure(brut, compte), ensure_ascii=False, indent=1) + "\n"
    masque, n = masquer_texte(masque)                    # seconde passe sur le texte rendu (noms de clés compris)
    return masque, compte[0] + n, "structure"


def _remplacer(chemin: str, texte: str) -> None:
    tmp = chemin + ".ecriture-%d.tmp" % os.getpid()
    with os.fdopen(os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "w", encoding="utf-8") as f:
        f.write(texte)
    os.replace(tmp, chemin)


def cmd_masquer_en_place(fichier: str) -> int:
    t = open(fichier, "rb").read().decode("utf-8", "replace")
    masque, n, mode = masquer(t)
    _remplacer(fichier, masque)
    print("%d %s" % (n, mode))
    return 0


# --- réponse de création -----------------------------------------------------------------------------------------------------
CANDIDAT = re.compile(r"new_contract\\?[\"']?\s*[:=]\s*\\?[\"']?\s*(-?[0-9]+)")


def _valeurs_de_cle(v, cle, profondeur=0):
    if isinstance(v, dict):
        for k, x in v.items():
            if k == cle:
                yield profondeur, x
            yield from _valeurs_de_cle(x, cle, profondeur + 1)
    elif isinstance(v, list):
        for x in v:
            yield from _valeurs_de_cle(x, cle, profondeur + 1)


def verdict_creation(t: str) -> tuple:
    """Rend (verdict, identifiant ou None, raison, champs). Verdicts : « cree », « refusee », « incertain »."""
    try:
        brut = analyser_json(t)
    except Illisible as e:
        return "incertain", None, "réponse non analysable comme JSON (%s)" % e, "aucun champ lu"
    if not isinstance(brut, dict):
        return "incertain", None, "la réponse n'est pas un objet JSON", "aucun champ lu"
    champs = " ; ".join("%s=%s" % (c, masquer_texte(json.dumps(brut[c], ensure_ascii=False))[0][:300] if c in brut else "absent")
                        for c in ("success", "new_contract", "error", "msg"))
    dans_la_structure = list(_valeurs_de_cle(brut, "new_contract"))
    dans_le_texte = {int(m) for m in CANDIDAT.findall(t)}
    succes = brut.get("success")
    if "new_contract" not in brut:
        if dans_la_structure or dans_le_texte:
            return "incertain", None, "clé `new_contract` absente du premier niveau, mais citée ailleurs dans la réponse", champs
        if succes is False:
            return "refusee", None, "`success` faux au premier niveau, aucun identifiant nulle part", champs
        return "incertain", None, "clé `new_contract` absente du premier niveau", champs
    ident = brut["new_contract"]
    if isinstance(ident, bool) or not isinstance(ident, int) or ident <= 0:
        return "incertain", None, "`new_contract` n'est pas un entier positif", champs
    autres = sorted(({x for p, x in dans_la_structure if p > 0 and x != ident and not isinstance(x, (dict, list))} | dans_le_texte) - {ident}, key=str)
    if autres or any(p > 0 for p, _ in dans_la_structure):
        return "incertain", None, "plusieurs valeurs candidates pour l'identifiant créé (%d valeur(s) en plus de celle du premier niveau)" % max(len(autres), 1), champs
    if succes is not True:
        return "incertain", None, "identifiant présent mais `success` n'est pas vrai au premier niveau", champs
    return "cree", ident, "clé `new_contract` de premier niveau, seule valeur candidate, `success` vrai", champs


def cmd_creation(fichier: str) -> int:
    v, ident, raison, champs = verdict_creation(open(fichier, "rb").read().decode("utf-8", "replace"))
    print("verdict=%s id=%s" % (v, ident if ident is not None else "aucun"))
    print(raison)
    print(champs)
    return 0


# --- inventaire --------------------------------------------------------------------------------------------------------------
def lire_inventaire(t: str) -> list:
    brut = analyser_json(t)
    liste = brut.get("instances") if isinstance(brut, dict) and set(brut) == {"instances"} else brut
    if liste is None and isinstance(brut, dict):
        liste = []
    if not isinstance(liste, list):
        raise Illisible("ni une liste d'instances ni {instances: liste ou null}")
    for i in liste:
        if not isinstance(i, dict) or isinstance(i.get("id"), bool) or not isinstance(i.get("id"), int) or i["id"] <= 0:
            raise Illisible("une entrée sans identifiant entier positif")
    if len({i["id"] for i in liste}) != len(liste):
        raise Illisible("un identifiant en double")
    return liste


def _scalaire(v):
    if isinstance(v, str):
        return masquer_texte(v)[0][:200]
    return v if v is None or isinstance(v, (bool, int, float)) else None


def _mot(v) -> str:
    return re.sub(r"[^A-Za-z0-9_.+-]", "?", str(v))[:80] if v not in (None, "") else "aucun"


def cmd_inventaire(brut_f: str, trace_f: str, prefixe: str, ident: str = "", avant_f: str = "") -> int:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", prefixe):
        raise Illisible("préfixe d'étiquette illisible")
    liste = lire_inventaire(open(brut_f, "rb").read().decode("utf-8", "replace"))
    reduit = [{"id": i["id"], "label": _scalaire(i.get("label")), "actual_status": _scalaire(i.get("actual_status"))} for i in liste]
    du_saboteur = [{c: _scalaire(i[c]) for c in CHAMPS_FILTRES if c in i} for i in liste if str(i.get("label") or "").startswith(prefixe)]
    cible = [r for r in reduit if ident and str(r["id"]) == ident]
    manquants = "sans-objet"
    if avant_f:
        avant = json.load(open(avant_f, encoding="utf-8"))
        manquants = str(len({a["id"] for a in avant if str(a["id"]) != ident} - {r["id"] for r in reduit}))
    trace = {"releve_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "nombre_d_instances_du_compte": len(liste),
             "prefixe_d_etiquette_du_saboteur": prefixe, "instances_du_saboteur_champs_filtres": du_saboteur,
             "instance_visee": (cible[0] if cible else None) if ident else "sans objet",
             "note": "champs filtrés des seules instances du saboteur à budget ; l'inventaire entier du compte n'est pas conservé"}
    with os.fdopen(os.open(trace_f, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644), "w", encoding="utf-8") as f:      # jamais d'écrasement (R12)
        f.write(json.dumps(trace, ensure_ascii=False, indent=1) + "\n")
    _remplacer(brut_f, json.dumps(reduit, ensure_ascii=False) + "\n")
    print("n=%d etat=%s etiquette=%s statut=%s autres_manquants=%s" % (
        len(liste), ("present" if cible else "absent") if ident else "sans-objet", _mot(cible[0]["label"]) if cible else "aucun",
        _mot(cible[0]["actual_status"]) if cible else "aucun", manquants))
    return 0


def main(argv: list) -> int:
    try:
        if len(argv) == 2 and argv[0] == "masquer-en-place":
            return cmd_masquer_en_place(argv[1])
        if len(argv) == 2 and argv[0] == "creation":
            return cmd_creation(argv[1])
        if 4 <= len(argv) <= 6 and argv[0] == "inventaire":
            return cmd_inventaire(*argv[1:])
        print("usage : masquer-en-place FICHIER | creation FICHIER | inventaire BRUT TRACE PREFIXE [ID] [REDUIT_D_AVANT]")
        return 2
    except Illisible as e:
        print("illisible : %s" % e)
        return 1
    except Exception as e:  # noqa: BLE001  (aucun détail de l'exception : il pourrait citer le contenu)
        print("échec : %s" % type(e).__name__)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
