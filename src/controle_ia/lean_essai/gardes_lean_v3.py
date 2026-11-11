"""Gardes du bras formel de l'essai Lean, D-1a — v3 (contre-lecture courte `1fea30ab…`, décision R-2302).

v3 : **la garde de fond est la défense principale et obligatoire.** Le fichier de contrôle v2 (qui importait le module de
l'agent, donc exposait ses initialiseurs) est remplacé par le **vérificateur du noyau** (`verificateur_noyau_v3.lean`), lancé
dans un processus distinct qui n'importe jamais le module de l'agent et n'exécute aucun de ses codes :
- G-L8 (neuve, principale) : rejeu de chaque déclaration de `Item.olean` par le noyau ; échec ⇒ `NON-ACCEPTE` ;
- G-L2 : axiomes de chaque énoncé attendu, calculés sur l'environnement rejoué, dans {propext, Classical.choice, Quot.sound} ;
- G-L3 : aucune constante axiome, non sûre ou partielle ; imports du module dans la liste permise ;
- G-L4 : chaque nom attendu présent dans le module, de genre théorème ;
- G-L5 : énoncés **imprimés par le harnais** dans un environnement sans aucune extension de l'agent, et **aller-retour** : le
  texte réélaboré redonne le type vérifié (égalité jugée sur les termes, `isDefEq` réductible, jamais sur le texte) ;
- G-L6 : chaque constante non théorème du module est imprimée par le harnais (type et valeur) pour le relecteur ;
- G-L7 : sortie du vérificateur complète et bien formée (code 0, JSON seulement, une ligne par nom attendu, marqueur de fin au
  nonce du harnais) ; dossier de l'item réduit à `Item.lean`, `Item.olean`, `Item.ilean` (note 2 de la contre-lecture courte).
Les gardes **textuelles** (G-L2, G-L3, G-L3+, G-L4, G-L6 par le texte) restent en seconde ligne : leur échec reste un échec,
mais aucune acceptation ne repose sur elles seules. Lexique v3 (CLC2-01) : prédicats d'identifiant de Lean ; début de
commentaire ou de littéral admis seulement en début de fichier, après un blanc, après un identifiant (commentaire) ou après
`(`, `[`, `{`, `⟨`, `⦃`, `,` ; ailleurs ⇒ refus. Mots neufs de G-L3+ (CLC2-02) : `simproc` et variantes, formes Qq, règles de
tactique d'Aesop, types de code méta et d'entrées-sorties.
Module **autonome** (bibliothèque standard seule), copié tel quel sur la machine.
"""
from __future__ import annotations

import json
import re

VERSION = "gardes_lean_v3"
AXIOMES_PERMIS = ("propext", "Classical.choice", "Quot.sound")
ENONCE = "enonce_item"
FICHIERS_ITEM = ("Item.lean", "Item.olean", "Item.ilean")

MOTS_GL2 = ("sorry", "admit", "sorryAx")
MOTS_GL3 = ("axiom", "unsafe", "implemented_by", "extern")
MOTS_GL6 = ("notation", "notation3", "macro", "macro_rules", "syntax", "elab", "elab_rules", "infix", "infixl",
            "infixr", "prefix", "postfix", "declare_syntax_cat")
MOTS_GL3_SUPPL = ("#eval", "#exit", "run_cmd", "run_elab", "run_meta", "run_tac", "by_elab", "initialize",
                  "builtin_initialize", "prelude", "private",
                  # v3 (CLC2-02)
                  "simproc", "dsimproc", "simproc_decl", "dsimproc_decl", "builtin_simproc", "builtin_dsimproc",
                  "by_elabq", "run_cmdq", "run_tacq", "run_elabq", "run_metaq")
# types de code méta et d'entrées-sorties : refusés même qualifiés (`Lean.Elab.Tactic.TacticM`)
TYPES_META = ("TacticM", "MetaM", "CoreM", "TermElabM", "CommandElabM", "SimpM", "Simproc", "DSimproc", "IO", "EIO",
              "BaseIO")
IMPORTS_PERMIS = ("Mathlib", "Batteries", "Aesop", "Qq", "Std", "Init", "Plausible", "ImportGraph", "ProofWidgets",
                  "LeanSearchClient")
ATTRIBUTS_PERMIS = ("simp", "reducible", "irreducible")
GENRES_DEFINITION = ("def", "abbrev", "structure", "class", "inductive", "opaque", "irreducible_def", "instance")
TAILLE_MAX_SOURCE = 256 * 1024
RE_NONCE = re.compile(r"^[0-9a-f]{32}$")
OUVRANTS = "([{⟨⦃,"


class ErreurLexicale(ValueError):
    """Le texte ne se lit pas comme Lean le lirait sans deviner : refus."""


def _lettre_lean(c: str) -> bool:
    """`isLetterLike` de Lean, plus les lettres ASCII (le `Char.isAlpha` de Lean est ASCII)."""
    o = ord(c)
    return (("a" <= c <= "z") or ("A" <= c <= "Z") or (0x3B1 <= o <= 0x3C9 and o != 0x3BB)
            or (0x391 <= o <= 0x3A9 and o not in (0x3A0, 0x3A3)) or (0x3CA <= o <= 0x3FB) or (0x1F00 <= o <= 0x1FFE)
            or (0x2100 <= o <= 0x214F) or (0x1D49C <= o <= 0x1D59F))


def _indice(c: str) -> bool:
    o = ord(c)
    return 0x2080 <= o <= 0x2089 or 0x2090 <= o <= 0x209C or 0x1D62 <= o <= 0x1D6A or o == 0x2C7C


def _debut_ident(c: str) -> bool:
    return _lettre_lean(c) or c == "_"


def _suite_ident(c: str) -> bool:
    return _debut_ident(c) or "0" <= c <= "9" or c in "'!?" or _indice(c)


_CAR = re.compile(r"'(\\(x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4}|.)|[^\\'\n])'")
_BRUTE = re.compile(r'r(#*)"')
BLANCS = " \t\r\n"


def masquer(source: str) -> str:
    """Lecteur de lexèmes (CLC2-01). Masque commentaires et littéraux (sauts de ligne gardés) ; lève `ErreurLexicale` sur tout
    voisinage que Lean pourrait lire autrement."""
    sortie = list(source)
    n = len(source)

    def blanc(a: int, b: int) -> None:
        for k in range(a, b):
            if sortie[k] != "\n":
                sortie[k] = " "

    def fin_litteral(j: int) -> None:
        if j < n and (_suite_ident(source[j]) or source[j] in "\"'«»"):
            raise ErreurLexicale(f"littéral suivi d'un caractère collé (position {j})")

    i, prec = 0, "debut"   # debut | blanc | ident | ouvrant | litteral | autre
    while i < n:
        c = source[i]
        if source.startswith("--", i) or source.startswith("/-", i):
            if prec not in ("debut", "blanc", "ident", "ouvrant"):
                raise ErreurLexicale(f"début de commentaire au milieu d'un lexème (position {i})")
            if source.startswith("--", i):
                j = source.find("\n", i)
                j = n if j < 0 else j
            else:
                profondeur, j = 1, i + 2
                while j < n and profondeur > 0:
                    if source.startswith("/-", j):
                        profondeur, j = profondeur + 1, j + 2
                    elif source.startswith("-/", j):
                        profondeur, j = profondeur - 1, j + 2
                    else:
                        j += 1
                if profondeur > 0:
                    raise ErreurLexicale(f"commentaire de bloc non fermé (position {i})")
            blanc(i, j)
            i, prec = j, "blanc"
            continue
        if c in "«»":
            raise ErreurLexicale(f"identifiant entre « » refusé (position {i})")
        if c in BLANCS:
            i, prec = i + 1, "blanc"
            continue
        if c == "r" and _BRUTE.match(source, i):
            if prec not in ("debut", "blanc", "ouvrant"):
                raise ErreurLexicale(f"chaîne brute collée (position {i})")
            m = _BRUTE.match(source, i)
            fin = '"' + m.group(1)
            j = source.find(fin, m.end())
            if j < 0:
                raise ErreurLexicale(f"chaîne brute non fermée (position {i})")
            blanc(i, j + len(fin))
            i, prec = j + len(fin), "litteral"
            fin_litteral(i)
            continue
        if _debut_ident(c):
            j = i + 1
            while j < n and _suite_ident(source[j]):
                j += 1
            if j < n and source[j] == '"':
                raise ErreurLexicale(f"chaîne collée à un identifiant (position {j})")
            i, prec = j, "ident"
            continue
        if "0" <= c <= "9":
            j = i + 1
            while j < n and (source[j].isascii() and (source[j].isalnum() or source[j] in "_.")):
                j += 1
            if j < n and source[j] in "\"'":
                raise ErreurLexicale(f"littéral collé à un nombre (position {j})")
            i, prec = j, "autre"
            continue
        if c == '"':
            if prec not in ("debut", "blanc", "ouvrant"):
                raise ErreurLexicale(f"chaîne collée au lexème précédent (position {i})")
            j = i + 1
            while j < n and source[j] != '"':
                j += 2 if source[j] == "\\" else 1
            if j >= n:
                raise ErreurLexicale(f"chaîne non fermée (position {i})")
            blanc(i, j + 1)
            i, prec = j + 1, "litteral"
            fin_litteral(i)
            continue
        if c == "'":
            if source.startswith("''", i) and not source.startswith("'''", i):
                i, prec = i + 2, "autre"   # image d'un ensemble (Mathlib : f '' s)
                continue
            if source[max(0, i - 2):i] == "⁻¹":
                i, prec = i + 1, "autre"   # image réciproque (Mathlib : f ⁻¹' s)
                continue
            if prec not in ("debut", "blanc", "ouvrant"):
                raise ErreurLexicale(f"caractère collé au lexème précédent (position {i})")
            m = _CAR.match(source, i)
            if not m:
                raise ErreurLexicale(f"apostrophe hors d'un identifiant ou d'un caractère (position {i})")
            blanc(i, m.end())
            i, prec = m.end(), "litteral"
            fin_litteral(i)
            continue
        i, prec = i + 1, ("ouvrant" if c in OUVRANTS else "autre")
    return "".join(sortie)


def _motif_mots(mots) -> re.Pattern:
    alternatives = "|".join(re.escape(m) for m in sorted(mots, key=len, reverse=True))
    return re.compile(r"(?<![\w'.!?])(" + alternatives + r")(?![\w'])")


_RE_GL2 = _motif_mots(MOTS_GL2)
_RE_GL3 = _motif_mots(MOTS_GL3)
_RE_GL3_UNSAFE = re.compile(r"(?<![\w'.!?])(unsafe\w+)")
_RE_GL6 = _motif_mots(MOTS_GL6)
_RE_GL3_SUPPL = _motif_mots(MOTS_GL3_SUPPL)
_RE_TYPES_META = re.compile(r"(?<![\w'!?])(" + "|".join(sorted(TYPES_META, key=len, reverse=True)) + r")(?![\w'])")
_RE_AESOP_TACTIQUE = re.compile(r"(?<![\w'.!?])aesop\b[^\n]*(?<![\w'.!?])tactic(?![\w'])")
_RE_DERIVING = _motif_mots(("deriving",))
_RE_DEBUG = re.compile(r"set_option\s+debug\.|skipKernelTC")
_RE_IMPORT = re.compile(r"^[ \t]*(?:(?:public|meta|private)[ \t]+)*import[ \t]+(?:all[ \t]+)?([^\n]*)$", re.M)
_RE_THEOREME = re.compile(r"(?<![\w'.!?])(?:theorem|lemma)\s+([^\s:({\[⦃]+)")
_RE_DEF = re.compile(r"(?<![\w'.!?])(" + "|".join(GENRES_DEFINITION) + r")(?![\w'])")
_RE_ATTR = re.compile(r"@\[([^\]]*)\]|(?<![\w'.!?])attribute\s*\[([^\]]*)\]")


def _ligne(texte: str, position: int) -> int:
    return texte.count("\n", 0, position) + 1


def _occurrences(motif: re.Pattern, texte: str) -> list[str]:
    return [f"« {m.group(1)} » ligne {_ligne(texte, m.start())}" for m in motif.finditer(texte)]


def attributs_hors_liste(masque: str) -> list[str]:
    motifs = []
    for m in _RE_ATTR.finditer(masque):
        contenu = m.group(1) if m.group(1) is not None else m.group(2)
        for entree in contenu.split(","):
            e = re.sub(r"^\s*(?:(?:local|scoped)\s+)?-?\s*", "", entree)
            nom = (e.split() or [""])[0]
            if nom not in ATTRIBUTS_PERMIS:
                motifs.append(f"attribut hors liste « {nom or entree.strip()} » ligne {_ligne(masque, m.start())}")
    return motifs


def _instances_anonymes(masque: str) -> list[str]:
    anonymes = []
    for m in _RE_DEF.finditer(masque):
        if m.group(1) != "instance":
            continue
        j = m.end()
        while j < len(masque) and masque[j] in " \t\n":
            j += 1
        if masque.startswith("(priority", j):
            k = masque.find(")", j)
            j = len(masque) if k < 0 else k + 1
            while j < len(masque) and masque[j] in " \t\n":
                j += 1
        t = re.match(r"[^\s:({\[⦃]+", masque[j:])
        nom = t.group(0) if t else ""
        if not nom or nom.startswith(("where", ":=")):
            anonymes.append(f"instance anonyme ligne {_ligne(masque, m.start())}")
    return anonymes


def noms_attendus(m: int) -> list[str]:
    return [f"etape_{i}" for i in range(1, m + 1)] + [ENONCE]


def analyser_texte(source: str, m: int, supplementaires: bool = True) -> dict:
    """Gardes textuelles (seconde ligne)."""
    if not isinstance(m, int) or m < 1:
        raise ValueError("nombre d'étapes m entier ≥ 1 exigé")
    motifs: dict[str, list[str]] = {"G-L1": [], "G-L2": [], "G-L3": [], "G-L3+": [], "G-L4": [], "G-L6": []}
    if len(source.encode("utf-8")) > TAILLE_MAX_SOURCE:
        motifs["G-L1"].append(f"fichier de plus de {TAILLE_MAX_SOURCE} octets")
    try:
        masque = masquer(source)
    except ErreurLexicale as e:
        for g in ("G-L2", "G-L3", "G-L3+", "G-L4", "G-L6"):
            motifs[g].append(f"texte : lexique refusé : {e}")
        return {"motifs": motifs}
    motifs["G-L2"] += _occurrences(_RE_GL2, masque)
    motifs["G-L3"] += _occurrences(_RE_GL3, masque) + _occurrences(_RE_GL3_UNSAFE, masque)
    motifs["G-L6"] += _occurrences(_RE_GL6, masque) + _instances_anonymes(masque)
    motifs["G-L6"] += [f"instance dérivée (deriving) ligne {_ligne(masque, x.start())}" for x in _RE_DERIVING.finditer(masque)]
    if supplementaires:
        motifs["G-L3+"] += _occurrences(_RE_GL3_SUPPL, masque) + _occurrences(_RE_TYPES_META, masque)
        motifs["G-L3+"] += [f"règle de tactique d'Aesop ligne {_ligne(masque, x.start())}"
                            for x in _RE_AESOP_TACTIQUE.finditer(masque)]
        motifs["G-L3+"] += [f"« {x.group(0).strip()} » ligne {_ligne(masque, x.start())}" for x in _RE_DEBUG.finditer(masque)]
        motifs["G-L3+"] += attributs_hors_liste(masque)
        for imp in _RE_IMPORT.finditer(masque):
            for module in imp.group(1).split():
                if module.split(".")[0] not in IMPORTS_PERMIS:
                    motifs["G-L3+"].append(f"import non permis « {module} » ligne {_ligne(masque, imp.start())}")
    theoremes = [t.group(1) for t in _RE_THEOREME.finditer(masque)]
    for nom in noms_attendus(m):
        if nom not in theoremes:
            motifs["G-L4"].append(f"texte : déclaration `theorem {nom}` (ou `lemma`) absente")
    return {"motifs": {g: [x if x.startswith("texte") else "texte : " + x for x in v] for g, v in motifs.items()}}


# ---- sortie du vérificateur du noyau ----------------------------------------------------------------------------------

def lire_messages(sortie: str) -> list[dict]:
    """Messages de `lean --json` de la compilation (lignes non JSON ignorées : la compilation n'est jugée que sur son code,
    ses erreurs et son `.olean`)."""
    messages = []
    for ligne in sortie.splitlines():
        try:
            obj = json.loads(ligne)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and "severity" in obj:
            messages.append(obj)
    return messages


def lire_verification(sortie: str, nonce: str, m: int) -> dict:
    """Lecture stricte : toute ligne non JSON, tout doublon, tout nom hors des attendus, toute ligne après la fin est une
    anomalie (G-L7)."""
    anomalies: list[str] = []
    objets: list[dict] = []
    for ligne in sortie.splitlines():
        if not ligne.strip():
            continue
        try:
            obj = json.loads(ligne)
        except json.JSONDecodeError:
            anomalies.append(f"ligne non JSON : {ligne[:120]!r}")
            continue
        if not isinstance(obj, dict) or not isinstance(obj.get("type"), str):
            anomalies.append(f"objet sans type : {ligne[:120]!r}")
            continue
        objets.append(obj)
    par_type: dict[str, list[dict]] = {}
    for o in objets:
        par_type.setdefault(o["type"], []).append(o)
    inconnus = set(par_type) - {"imports", "constante", "rejeu", "attendu", "definition", "fin"}
    anomalies += [f"type de ligne inconnu {t!r}" for t in sorted(inconnus)]
    imports = par_type.get("imports", [])
    if len(imports) != 1:
        anomalies.append(f"{len(imports)} ligne(s) d'imports (1 exigée)")
    fins = par_type.get("fin", [])
    if len(fins) != 1 or not objets or objets[-1].get("type") != "fin":
        anomalies.append("marqueur de fin absent, multiple ou suivi d'autres lignes")
    elif fins[0].get("nonce") != nonce:
        anomalies.append("marqueur de fin d'un autre nonce")
    rejeux = par_type.get("rejeu", [])
    permis = bool(imports and imports[0].get("permis") is True)
    if permis and len(rejeux) != 1:
        anomalies.append(f"{len(rejeux)} ligne(s) de rejeu (1 exigée)")
    attendus: dict[str, dict] = {}
    for o in par_type.get("attendu", []):
        nom = o.get("nom")
        if nom in attendus:
            anomalies.append(f"nom attendu {nom!r} rapporté deux fois")
        elif nom not in noms_attendus(m):
            anomalies.append(f"nom {nom!r} rapporté hors des noms attendus")
        else:
            attendus[nom] = o
    rejeu_ok = bool(rejeux and rejeux[0].get("ok") is True)
    if rejeu_ok:
        for nom in noms_attendus(m):
            if nom not in attendus:
                anomalies.append(f"nom attendu {nom!r} sans ligne")
    constantes = []
    vus = set()
    for o in par_type.get("constante", []):
        if o.get("nom") in vus:
            anomalies.append(f"constante {o.get('nom')!r} rapportée deux fois")
        vus.add(o.get("nom"))
        constantes.append((str(o.get("nom")), str(o.get("genre")), str(o.get("surete"))))
    definitions = {str(o.get("nom")): o for o in par_type.get("definition", [])}
    return {"imports": imports[0] if imports else {}, "permis": permis, "rejeu_ok": rejeu_ok,
            "rejeu_erreur": rejeux[0].get("erreur", "") if rejeux else "", "attendus": attendus,
            "constantes": constantes, "definitions": definitions, "anomalies": anomalies}


def evaluer(source: str, m: int, compilation: dict, verification: dict, inventaire: list[str],
            supplementaires: bool = True) -> dict:
    """compilation : {"code", "sortie", "olean_present", ["sortie_tronquee"]} ;
    verification : {"code", "sortie", "nonce", ["sortie_tronquee"]} (vérificateur du noyau) ;
    inventaire : noms des fichiers du dossier de l'item après la compilation."""
    texte = analyser_texte(source, m, supplementaires)
    motifs = {g: list(v) for g, v in texte["motifs"].items()}
    for g in ("G-L1", "G-L2", "G-L3", "G-L3+", "G-L4", "G-L5", "G-L6", "G-L7", "G-L8"):
        motifs.setdefault(g, [])
    if not supplementaires:
        motifs["G-L3+"] = []
    # G-L1
    msgs = lire_messages(compilation.get("sortie", ""))
    if compilation.get("code") != 0:
        motifs["G-L1"].append(f"code de sortie de la compilation {compilation.get('code')!r}")
    motifs["G-L1"] += [f"erreur : {str(x.get('data', ''))[:300]}" for x in msgs if x.get("severity") == "error"]
    if not compilation.get("olean_present"):
        motifs["G-L1"].append("module compilé (.olean) absent")
    if compilation.get("sortie_tronquee"):
        motifs["G-L1"].append("sortie de compilation tronquée")
    # G-L7 : intégrité de la vérification et du dossier
    nonce = verification.get("nonce", "")
    if not RE_NONCE.match(nonce or ""):
        motifs["G-L7"].append("nonce du harnais absent ou mal formé")
    v = lire_verification(verification.get("sortie", ""), nonce, m)
    if verification.get("code") != 0:
        motifs["G-L7"].append(f"code de sortie du vérificateur {verification.get('code')!r} (0 exigé)")
    if verification.get("sortie_tronquee"):
        motifs["G-L7"].append("sortie du vérificateur tronquée")
    motifs["G-L7"] += [f"noyau : {a}" for a in v["anomalies"]]
    motifs["G-L7"] += [f"fichier inattendu dans le dossier de l'item : {f}" for f in sorted(inventaire)
                       if f not in FICHIERS_ITEM]
    # G-L8 : rejeu (garde principale)
    if not v["permis"]:
        motifs["G-L3"].append(f"noyau : imports hors liste {v['imports'].get('modules')}")
        motifs["G-L8"].append("rejeu non tenté : imports hors liste")
    elif not v["rejeu_ok"]:
        motifs["G-L8"].append(f"noyau : rejeu en échec : {str(v['rejeu_erreur'])[:300]}")
    # G-L2 à G-L6 par le noyau
    for nom in noms_attendus(m):
        a = v["attendus"].get(nom)
        if a is None or a.get("present") is not True:
            motifs["G-L4"].append(f"noyau : {nom} absent du module")
            motifs["G-L2"].append(f"noyau : axiomes de {nom} non établis")
            motifs["G-L5"].append(f"noyau : énoncé de {nom} non imprimé")
            continue
        if a.get("genre") != "theoreme":
            motifs["G-L4"].append(f"noyau : {nom} de genre {a.get('genre')!r}, « theoreme » exigé")
        axiomes = a.get("axiomes")
        if not isinstance(axiomes, list):
            motifs["G-L2"].append(f"noyau : axiomes de {nom} illisibles")
        else:
            hors = [x for x in axiomes if x not in AXIOMES_PERMIS]
            if hors:
                motifs["G-L2"].append(f"noyau : {nom} dépend de : {', '.join(map(str, hors))}")
        if not a.get("enonce"):
            motifs["G-L5"].append(f"noyau : énoncé de {nom} non imprimé")
        if a.get("aller_retour") is not True:
            motifs["G-L5"].append(f"noyau : aller-retour de l'énoncé de {nom} en échec : {str(a.get('raison'))[:200]}")
    for nom, genre, surete in v["constantes"]:
        if genre == "axiome":
            motifs["G-L3"].append(f"noyau : constante axiome {nom}")
        if surete != "sure":
            motifs["G-L3"].append(f"noyau : constante {surete} {nom} ({genre})")
        if genre != "theoreme" and v["rejeu_ok"] and nom not in v["definitions"]:
            motifs["G-L6"].append(f"noyau : constante {nom} ({genre}) non imprimée")
    gardes = {g: {"ok": not x, "motifs": x} for g, x in sorted(motifs.items())}
    impressions = {n: f"{d.get('genre')} {n} : {d.get('enonce')} := {d.get('valeur')}" for n, d in v["definitions"].items()}
    return {"version": VERSION, "gardes": gardes, "accepte_gardes": all(x["ok"] for x in gardes.values()),
            "enonces_imprimes": {n: a.get("enonce", "") for n, a in v["attendus"].items()},
            "enonces_explicites": {n: a.get("enonce_explicite", "") for n, a in v["attendus"].items()},
            "impressions": impressions, "axiomes": {n: a.get("axiomes") for n, a in v["attendus"].items()},
            "constantes": v["constantes"], "rejeu_ok": v["rejeu_ok"], "supplementaires": supplementaires}


def pour_relecteur(verdict: dict) -> str:
    lignes = ["## Énoncés imprimés par le harnais (vérifiés par le noyau, aller-retour réussi)"]
    lignes += list(verdict["enonces_imprimes"].values())
    lignes.append("## Mêmes énoncés, forme explicite (pp.all)")
    lignes += list(verdict["enonces_explicites"].values())
    if verdict["impressions"]:
        lignes.append("## Constantes introduites par l'agent, imprimées par le harnais")
        lignes += list(verdict["impressions"].values())
    return "\n".join(lignes) + "\n"
