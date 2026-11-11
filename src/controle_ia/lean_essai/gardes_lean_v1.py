"""Gardes mécaniques du bras formel de l'essai Lean (G-L1 à G-L7), D-1a — v1.

Source : brouillon 3 du dessin et du devis, § 3.1 (`717259ed…`), contre-lecture 1 (CLP-12 a à d), vérification courte (VL-05).
Module **autonome** (bibliothèque standard seule) : le même fichier sert hors de la machine (harnais) et sur la machine dédiée
(exécuteur du bac), où aucun autre fichier du programme n'est copié.

Le verdict `ACCEPTE` d'un item du bras L exige toutes les gardes :
- G-L1 compilation du fichier de l'agent sans erreur (code de sortie nul, aucun message d'erreur, `.olean` produit) ;
- G-L2 aucun `sorry` ni `admit` (texte, et avertissement « declaration uses 'sorry' ») et `#print axioms` de `enonce_item` et
  de chaque `etape_i` ne liste que `propext`, `Classical.choice`, `Quot.sound` (lu dans la sortie du fichier de contrôle) ;
- G-L3 aucun `axiom`, `unsafe`, `implemented_by`, `extern` dans le fichier ; aucune constante de genre « axiome » dans le
  module de l'agent (énumération du fichier de contrôle) ;
- G-L3+ (**ajout du développeur, proposé, non dans le devis** ; désactivable par `supplementaires=False`) : aucune commande
  qui exécute du code à l'élaboration ou touche au noyau (`#eval`, `#exit`, `run_cmd`, `run_elab`, `run_meta`, `run_tac`,
  `by_elab`, `initialize`, `builtin_initialize`, `prelude`, `private`, `set_option debug.…`, `skipKernelTC`) et aucun
  import hors de `IMPORTS_PERMIS` ;
- G-L4 présence de `etape_1` à `etape_m` et de `enonce_item` (texte, et `#check` du fichier de contrôle sans erreur) ;
- G-L5 les énoncés **imprimés par Lean** (`#check @nom` du fichier de contrôle) sont ce que reçoit le relecteur de fidélité ;
- G-L6 aucune `notation`, `macro`, `macro_rules`, `syntax`, `elab`, `infix`, `prefix`, `postfix` (ni variantes) ; toute
  définition, abréviation, structure, classe, inductif, opaque ou instance introduite est imprimée en entier (`#print`) et
  envoyée au relecteur ; toute constante non théorème du module de l'agent qui n'est ni imprimée ni descendante d'un nom
  imprimé ou attendu (instance anonyme, instance dérivée…) fait échouer la garde ;
- G-L7 `#print axioms`, `#check` et `#print` sont lancés par le harnais dans un fichier à lui (`fichier_controle`), qui
  importe le module de l'agent ; seule la sortie de ce fichier est lue ; le fichier n'a pas changé pendant son exécution
  (empreinte avant et après) et sa sortie est complète (marqueur de fin de l'énumération).

Aucun repli silencieux (R5) : une sortie illisible, un lexique non fermé ou un message manquant fait échouer la garde avec
son motif ; rien n'est deviné.
"""
from __future__ import annotations

import hashlib
import json
import re

VERSION = "gardes_lean_v1"
MODULE_AGENT = "Item"
AXIOMES_PERMIS = ("propext", "Classical.choice", "Quot.sound")
ENONCE = "enonce_item"

MOTS_GL2 = ("sorry", "admit", "sorryAx")
MOTS_GL3 = ("axiom", "unsafe", "implemented_by", "extern")
MOTS_GL6 = ("notation", "notation3", "macro", "macro_rules", "syntax", "elab", "elab_rules", "infix", "infixl",
            "infixr", "prefix", "postfix", "declare_syntax_cat")
# G-L3+ : ajout du développeur (proposé) — commandes qui exécutent du code à l'élaboration ou touchent au noyau
MOTS_GL3_SUPPL = ("#eval", "#exit", "run_cmd", "run_elab", "run_meta", "run_tac", "by_elab", "initialize",
                  "builtin_initialize", "prelude", "private")
IMPORTS_PERMIS = ("Mathlib", "Batteries", "Aesop", "Qq", "Std", "Init", "Plausible", "ImportGraph", "ProofWidgets",
                  "LeanSearchClient")

GENRES_DEFINITION = ("def", "abbrev", "structure", "class", "inductive", "opaque", "irreducible_def", "instance")
MARQUEUR_CONSTANTE = "CONSTANTE "
MARQUEUR_FIN = "CONSTANTES-FIN"
TAILLE_MAX_SOURCE = 256 * 1024


class ErreurLexicale(ValueError):
    """Commentaire de bloc, chaîne ou chaîne brute non fermés : le texte ne se lit pas sans deviner."""


def _est_ident(c: str) -> bool:
    return c.isalnum() or c in "_'!?"


_CAR = re.compile(r"'(\\(x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4}|.)|[^\\'\n])'")
_BRUTE = re.compile(r'r(#*)"')


def masquer(source: str) -> str:
    """Remplace commentaires (`--`, `/- … -/` imbriqués), chaînes, chaînes brutes et caractères littéraux par des espaces ;
    les sauts de ligne sont gardés (positions inchangées). Lève `ErreurLexicale` sur un élément non fermé."""
    sortie = list(source)
    n = len(source)

    def blanc(a: int, b: int) -> None:
        for k in range(a, b):
            if sortie[k] != "\n":
                sortie[k] = " "

    i = 0
    while i < n:
        c = source[i]
        precedent = source[i - 1] if i > 0 else ""
        if source.startswith("--", i):
            j = source.find("\n", i)
            j = n if j < 0 else j
            blanc(i, j)
            i = j
            continue
        if source.startswith("/-", i):
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
            i = j
            continue
        if c == "r" and not _est_ident(precedent):
            m = _BRUTE.match(source, i)
            if m:
                fin = '"' + m.group(1)
                j = source.find(fin, m.end())
                if j < 0:
                    raise ErreurLexicale(f"chaîne brute non fermée (position {i})")
                blanc(i, j + len(fin))
                i = j + len(fin)
                continue
        if c == '"':
            j = i + 1
            while j < n and source[j] != '"':
                j += 2 if source[j] == "\\" else 1
            if j >= n:
                raise ErreurLexicale(f"chaîne non fermée (position {i})")
            blanc(i, j + 1)
            i = j + 1
            continue
        if c == "'" and not _est_ident(precedent):
            m = _CAR.match(source, i)
            if m:
                blanc(i, m.end())
                i = m.end()
                continue
        i += 1
    return "".join(sortie)


def _motif_mots(mots) -> re.Pattern:
    alternatives = "|".join(re.escape(m) for m in sorted(mots, key=len, reverse=True))
    return re.compile(r"(?<![\w'.!?])(" + alternatives + r")(?![\w'])")


_RE_GL2 = _motif_mots(MOTS_GL2)
_RE_GL3 = _motif_mots(MOTS_GL3)
_RE_GL6 = _motif_mots(MOTS_GL6)
_RE_GL3_SUPPL = _motif_mots(MOTS_GL3_SUPPL)
_RE_DEBUG = re.compile(r"set_option\s+debug\.|skipKernelTC")
_RE_IMPORT = re.compile(r"^[ \t]*(?:(?:public|meta|private)[ \t]+)*import[ \t]+(?:all[ \t]+)?([^\n]*)$", re.M)
_RE_THEOREME = re.compile(r"(?<![\w'.!?])(?:theorem|lemma)\s+(«[^»\n]+»|[^\s:({\[⦃]+)")
_RE_DEF = re.compile(r"(?<![\w'.!?])(" + "|".join(GENRES_DEFINITION) + r")(?![\w'])")
_RE_NOM_LEAN = re.compile(r"^[^\W\d][\w'!?]*(\.[^\W\d][\w'!?]*)*$")


def _ligne(texte: str, position: int) -> int:
    return texte.count("\n", 0, position) + 1


def _occurrences(motif: re.Pattern, texte: str) -> list[str]:
    return [f"« {m.group(1)} » ligne {_ligne(texte, m.start())}" for m in motif.finditer(texte)]


def _definitions(masque: str) -> tuple[list[str], list[str]]:
    """Noms introduits par `def`, `abbrev`, `structure`, `class`, `inductive`, `opaque`, `irreducible_def`, `instance`
    (à imprimer) et liste des instances anonymes (ligne)."""
    noms: list[str] = []
    anonymes: list[str] = []
    for m in _RE_DEF.finditer(masque):
        genre = m.group(1)
        j = m.end()
        while j < len(masque) and masque[j] in " \t\n":
            j += 1
        if genre == "class" and masque.startswith("inductive", j):
            continue  # `class inductive Nom` : le nom est lu après `inductive`
        if genre == "instance" and masque.startswith("(priority", j):
            k = masque.find(")", j)
            j = len(masque) if k < 0 else k + 1
            while j < len(masque) and masque[j] in " \t\n":
                j += 1
        t = re.match(r"«[^»\n]+»|[^\s:({\[⦃]+", masque[j:])
        nom = t.group(0) if t else ""
        if genre == "instance" and (not nom or nom.startswith(("where", ":="))):
            anonymes.append(f"instance anonyme ligne {_ligne(masque, m.start())}")
            continue
        if nom:
            noms.append(nom)
    return noms, anonymes


def analyser_texte(source: str, m: int, supplementaires: bool = True) -> dict:
    """Gardes textuelles (G-L2, G-L3, G-L3+, G-L4, G-L6) sur le fichier de l'agent. Rend, par garde, la liste des motifs
    (vide si la garde passe), et la liste des définitions à imprimer."""
    if not isinstance(m, int) or m < 1:
        raise ValueError("nombre d'étapes m entier ≥ 1 exigé")
    motifs: dict[str, list[str]] = {"G-L2": [], "G-L3": [], "G-L3+": [], "G-L4": [], "G-L6": []}
    if len(source.encode("utf-8")) > TAILLE_MAX_SOURCE:
        motifs["G-L1"] = [f"fichier de plus de {TAILLE_MAX_SOURCE} octets"]
    try:
        masque = masquer(source)
    except ErreurLexicale as e:
        for g in motifs:
            motifs[g].append(f"lexique illisible : {e}")
        return {"motifs": motifs, "definitions": [], "theoremes": []}
    motifs["G-L2"] += _occurrences(_RE_GL2, masque)
    motifs["G-L3"] += _occurrences(_RE_GL3, masque)
    motifs["G-L6"] += _occurrences(_RE_GL6, masque)
    if supplementaires:
        motifs["G-L3+"] += _occurrences(_RE_GL3_SUPPL, masque)
        motifs["G-L3+"] += [f"« {x.group(0).strip()} » ligne {_ligne(masque, x.start())}" for x in _RE_DEBUG.finditer(masque)]
        for imp in _RE_IMPORT.finditer(masque):
            for module in imp.group(1).split():
                if module.split(".")[0] not in IMPORTS_PERMIS:
                    motifs["G-L3+"].append(f"import non permis « {module} » ligne {_ligne(masque, imp.start())}")
    theoremes = [t.group(1) for t in _RE_THEOREME.finditer(masque)]
    for nom in [f"etape_{i}" for i in range(1, m + 1)] + [ENONCE]:
        if nom not in theoremes:
            motifs["G-L4"].append(f"déclaration `theorem {nom}` (ou `lemma`) absente")
    definitions, anonymes = _definitions(masque)
    motifs["G-L6"] += anonymes
    for d in definitions:
        if _identifiant(d) is None:
            motifs["G-L6"].append(f"nom de définition non imprimable « {d} »")
    return {"motifs": motifs, "definitions": [d for d in definitions if _identifiant(d) is not None],
            "theoremes": theoremes}


def _identifiant(nom: str) -> str | None:
    if nom.startswith("«") and nom.endswith("»") and "»" not in nom[1:-1]:
        return nom
    if _RE_NOM_LEAN.match(nom):
        return nom
    return None


# ---- fichier de contrôle (G-L7) -------------------------------------------------------------------------------------------

ENUMERATION_A = """open Lean in #eval show CoreM Unit from do
  let env ← getEnv
  let some idx := env.getModuleIdx? `{module} | throwError "CONTROLE-MODULE-ABSENT"
  for n in env.header.moduleData[idx.toNat]!.constNames do
    let genre := match env.find? n with
      | some (ConstantInfo.thmInfo _) => "theoreme"
      | some (ConstantInfo.defnInfo _) => "definition"
      | some (ConstantInfo.axiomInfo _) => "axiome"
      | some (ConstantInfo.opaqueInfo _) => "opaque"
      | some (ConstantInfo.inductInfo _) => "inductif"
      | some (ConstantInfo.ctorInfo _) => "constructeur"
      | some (ConstantInfo.recInfo _) => "recurseur"
      | some (ConstantInfo.quotInfo _) => "quotient"
      | none => "absent"
    IO.println s!"CONSTANTE {{n}} {{genre}}"
  IO.println "CONSTANTES-FIN"
"""

# Variante B (même sortie) si l'interface `Environment.header` de la chaîne installée diffère : choisie **une fois, à
# l'installation**, par l'essai sain de la chaîne, consignée dans `chaine-v1.json` ; jamais par item.
ENUMERATION_B = """open Lean in #eval show CoreM Unit from do
  let env ← getEnv
  let some idx := env.getModuleIdx? `{module} | throwError "CONTROLE-MODULE-ABSENT"
  let noms := env.constants.map₁.fold (fun acc n _ => if env.getModuleIdxFor? n == some idx then acc.push n else acc) #[]
  for n in noms do
    let genre := match env.find? n with
      | some (ConstantInfo.thmInfo _) => "theoreme"
      | some (ConstantInfo.defnInfo _) => "definition"
      | some (ConstantInfo.axiomInfo _) => "axiome"
      | some (ConstantInfo.opaqueInfo _) => "opaque"
      | some (ConstantInfo.inductInfo _) => "inductif"
      | some (ConstantInfo.ctorInfo _) => "constructeur"
      | some (ConstantInfo.recInfo _) => "recurseur"
      | some (ConstantInfo.quotInfo _) => "quotient"
      | none => "absent"
    IO.println s!"CONSTANTE {{n}} {{genre}}"
  IO.println "CONSTANTES-FIN"
"""
ENUMERATIONS = {"A": ENUMERATION_A, "B": ENUMERATION_B}


def noms_attendus(m: int) -> list[str]:
    return [f"etape_{i}" for i in range(1, m + 1)] + [ENONCE]


def fichier_controle(m: int, definitions: list[str], variante: str = "A",
                     module: str = MODULE_AGENT) -> tuple[str, dict[int, tuple[str, str]]]:
    """Texte du fichier de contrôle du harnais et carte « ligne → (genre, nom) » de ses commandes. Une commande par ligne :
    chaque message de Lean (`--json`) se rattache à sa commande par son numéro de ligne."""
    if variante not in ENUMERATIONS:
        raise ValueError(f"variante d'énumération inconnue {variante!r}")
    lignes = [f"import {module}", ""]
    carte: dict[int, tuple[str, str]] = {}

    def ajouter(texte: str, genre: str, nom: str) -> None:
        lignes.append(texte)
        carte[len(lignes)] = (genre, nom)

    for nom in noms_attendus(m):
        ajouter(f"#check @{nom}", "enonce", nom)
    for nom in noms_attendus(m):
        ajouter(f"#print axioms {nom}", "axiomes", nom)
    vus = set()
    for d in definitions:
        ident = _identifiant(d)
        if ident is None or ident in vus:
            continue
        vus.add(ident)
        ajouter(f"#print {ident}", "impression", d)
    lignes.append("")
    carte[len(lignes) + 1] = ("constantes", "*")
    lignes += ENUMERATIONS[variante].format(module=module).splitlines()
    return "\n".join(lignes) + "\n", carte


def empreinte_texte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


# ---- lecture des sorties de Lean ---------------------------------------------------------------------------------------

def lire_messages(sortie: str) -> tuple[list[dict], list[str]]:
    """Messages de `lean --json` (un objet par ligne) et lignes brutes non JSON (gardées, jamais jetées)."""
    messages, brut = [], []
    for ligne in sortie.splitlines():
        s = ligne.strip()
        if not s:
            continue
        try:
            obj = json.loads(s)
        except json.JSONDecodeError:
            brut.append(ligne)
            continue
        if isinstance(obj, dict) and "severity" in obj and "data" in obj:
            messages.append(obj)
        else:
            brut.append(ligne)
    return messages, brut


_RE_AXIOMES = re.compile(r"depends on axioms:\s*\[(.*?)\]", re.S)
_RE_SANS_AXIOME = re.compile(r"does not depend on any axioms")


def lire_axiomes(texte: str) -> list[str] | None:
    """Axiomes d'un message `#print axioms` ; `None` si le message ne se lit pas (jamais deviné)."""
    m = _RE_AXIOMES.search(texte)
    if m:
        return [a.strip() for a in m.group(1).replace("\n", " ").split(",") if a.strip()]
    if _RE_SANS_AXIOME.search(texte):
        return []
    return None


def _ligne_message(msg: dict) -> int | None:
    pos = msg.get("pos")
    if isinstance(pos, dict) and isinstance(pos.get("line"), int):
        return pos["line"]
    return None


def lire_controle(sortie: str, carte: dict[int, tuple[str, str]]) -> dict:
    """Rattache chaque message du fichier de contrôle à sa commande."""
    messages, brut = lire_messages(sortie)
    enonces: dict[str, str] = {}
    axiomes: dict[str, list[str] | None] = {}
    impressions: dict[str, str] = {}
    erreurs: list[str] = []
    erreurs_par_nom: dict[str, list[str]] = {}
    constantes: list[tuple[str, str]] = []
    fin_vue = False
    lignes_constantes: list[str] = []
    for msg in messages:
        ligne = _ligne_message(msg)
        genre, nom = carte.get(ligne, ("?", "?"))
        data = str(msg.get("data", ""))
        if msg.get("severity") == "error":
            erreurs.append(f"ligne {ligne} ({genre} {nom}) : {data[:300]}")
            erreurs_par_nom.setdefault(nom, []).append(data[:300])
            continue
        if genre == "enonce":
            enonces[nom] = data.strip()
        elif genre == "axiomes":
            axiomes[nom] = lire_axiomes(data)
        elif genre == "impression":
            impressions[nom] = data.strip()
        else:
            lignes_constantes += data.splitlines()
    lignes_constantes += brut
    for ligne in lignes_constantes:
        s = ligne.strip()
        if s == MARQUEUR_FIN:
            fin_vue = True
        elif s.startswith(MARQUEUR_CONSTANTE):
            parties = s[len(MARQUEUR_CONSTANTE):].rsplit(" ", 1)
            if len(parties) == 2:
                constantes.append((parties[0], parties[1]))
    return {"enonces": enonces, "axiomes": axiomes, "impressions": impressions, "erreurs": erreurs,
            "erreurs_par_nom": erreurs_par_nom, "constantes": constantes, "fin_enumeration": fin_vue,
            "brut": brut}


def constantes_non_couvertes(constantes: list[tuple[str, str]], imprimees: set[str], attendus: set[str]) -> list[str]:
    """Constantes non théorèmes du module de l'agent qui ne sont ni imprimées ni descendantes d'un nom imprimé ou attendu."""
    racines = {n.strip("«»") for n in imprimees | attendus}
    manquantes = []
    for nom, genre in constantes:
        if genre in ("theoreme", "axiome"):
            continue
        brut = nom.strip("«»")
        if brut in racines or any(brut.startswith(r + ".") for r in racines):
            continue
        manquantes.append(f"{nom} ({genre})")
    return manquantes


# ---- verdict des gardes -------------------------------------------------------------------------------------------------

def evaluer(source: str, m: int, compilation: dict, controle: dict, supplementaires: bool = True) -> dict:
    """Verdict des gardes G-L1 à G-L7 d'un item.

    compilation : {"code": int, "sortie": str (`lean --json`), "olean_present": bool}
    controle : {"code": int, "sortie": str, "texte": str, "carte": {ligne: (genre, nom)},
                "empreinte_ecrite": str, "empreinte_apres": str}
    """
    texte = analyser_texte(source, m, supplementaires)
    motifs = {g: list(v) for g, v in texte["motifs"].items()}
    for g in ("G-L1", "G-L2", "G-L3", "G-L3+", "G-L4", "G-L5", "G-L6", "G-L7"):
        motifs.setdefault(g, [])
    if not supplementaires:
        motifs["G-L3+"] = []

    # G-L1 : compilation du fichier de l'agent
    messages_agent, brut_agent = lire_messages(compilation.get("sortie", ""))
    if compilation.get("code") != 0:
        motifs["G-L1"].append(f"code de sortie de la compilation {compilation.get('code')!r}")
    erreurs_agent = [str(x.get("data", ""))[:300] for x in messages_agent if x.get("severity") == "error"]
    motifs["G-L1"] += [f"erreur : {e}" for e in erreurs_agent]
    if not compilation.get("olean_present"):
        motifs["G-L1"].append("module compilé (.olean) absent")
    for x in messages_agent:
        if x.get("severity") == "warning" and "sorry" in str(x.get("data", "")):
            motifs["G-L2"].append(f"avertissement de la compilation : {str(x.get('data'))[:200]}")

    # G-L7 : intégrité et complétude du fichier de contrôle du harnais
    lu = lire_controle(controle.get("sortie", ""), controle.get("carte", {}))
    ecrite, apres = controle.get("empreinte_ecrite"), controle.get("empreinte_apres")
    if not ecrite or ecrite != apres:
        motifs["G-L7"].append("fichier de contrôle modifié ou empreinte manquante")
    if ecrite and empreinte_texte(controle.get("texte", "")) != ecrite:
        motifs["G-L7"].append("texte du fichier de contrôle différent de celui écrit par le harnais")
    if controle.get("code") is None:
        motifs["G-L7"].append("fichier de contrôle non exécuté")
    if not lu["fin_enumeration"]:
        motifs["G-L7"].append("énumération des constantes absente ou incomplète (marqueur de fin non vu)")
    erreurs_hors_noms = [e for e in lu["erreurs"] if not any(f" {n})" in e for n in noms_attendus(m))]
    motifs["G-L7"] += [f"erreur du contrôle : {e}" for e in erreurs_hors_noms]

    attendus = noms_attendus(m)
    # G-L4 et G-L5 : énoncés imprimés par Lean
    for nom in attendus:
        if nom in lu["erreurs_par_nom"]:
            motifs["G-L4"].append(f"`#check @{nom}` ou `#print axioms {nom}` en erreur : {lu['erreurs_par_nom'][nom][0][:200]}")
        if not lu["enonces"].get(nom):
            motifs["G-L5"].append(f"énoncé imprimé de {nom} absent")
    # G-L2 : axiomes
    for nom in attendus:
        ax = lu["axiomes"].get(nom, None)
        if nom not in lu["axiomes"]:
            motifs["G-L2"].append(f"`#print axioms {nom}` sans réponse")
        elif ax is None:
            motifs["G-L2"].append(f"`#print axioms {nom}` illisible")
        else:
            hors = [a for a in ax if a not in AXIOMES_PERMIS]
            if hors:
                motifs["G-L2"].append(f"{nom} dépend de : {', '.join(hors)}")
    # G-L3 : axiomes déclarés dans le module (même par un chemin que le texte ne voit pas)
    for nom, genre in lu["constantes"]:
        if genre == "axiome":
            motifs["G-L3"].append(f"constante de genre axiome dans le module : {nom}")
    # G-L6 : définitions imprimées en entier, constantes couvertes
    for d in texte["definitions"]:
        if not lu["impressions"].get(d):
            motifs["G-L6"].append(f"`#print {d}` sans réponse")
    manquantes = constantes_non_couvertes(lu["constantes"], set(lu["impressions"]), set(attendus))
    motifs["G-L6"] += [f"constante non imprimée : {x}" for x in manquantes]

    gardes = {g: {"ok": not v, "motifs": v} for g, v in sorted(motifs.items())}
    return {"version": VERSION, "gardes": gardes, "accepte_gardes": all(x["ok"] for x in gardes.values()),
            "enonces_imprimes": lu["enonces"], "impressions": lu["impressions"], "axiomes": lu["axiomes"],
            "constantes": lu["constantes"], "supplementaires": supplementaires}


def pour_relecteur(verdict: dict) -> str:
    """Ce que reçoit le relecteur de fidélité (G-L5, G-L6) : énoncés imprimés par Lean, puis définitions imprimées."""
    lignes = ["## Énoncés imprimés par Lean (ordre du fichier de contrôle)"]
    lignes += list(verdict["enonces_imprimes"].values())
    if verdict["impressions"]:
        lignes.append("## Définitions introduites, imprimées en entier")
        lignes += list(verdict["impressions"].values())
    return "\n".join(lignes) + "\n"
