"""Gardes mécaniques du bras formel de l'essai Lean (G-L1 à G-L7), D-1a — v2.

v2 : corrections de la contre-lecture du harnais (`docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/contre-lecture-harnais-d1a-v1.md`,
`2077ae26…`, R-2300). La v1 (`gardes_lean_v1.py`) reste telle quelle (R12).
- CLL-01 : lexique refait comme un lecteur de lexèmes (identifiants lus en entier) ; `«` ou `»` hors commentaire et chaîne ⇒
  refus ; littéral collé à un identifiant, à un nombre ou à un autre littéral ⇒ refus ; apostrophe isolée ⇒ refus.
- CLL-02 : chaque nom attendu doit figurer dans l'énumération du contrôle, de genre « theoreme » ; toute constante du module
  « non sûre » ou « partielle » (sûreté imprimée par le contrôle) fait échouer G-L3.
- CLL-03 : une constante non théorème n'est couverte que si elle est **imprimée**, ou descendante d'un inductif imprimé (son
  `#print` montre constructeurs et champs), ou auxiliaire d'une liste **fermée** sous un nom imprimé ou attendu.
- CLL-04 : le fichier de contrôle passe par l'**entrée standard** du processus Lean (il n'est sur aucun disque que le bac voit) ;
  le marqueur de fin porte un **nonce** tiré par le harnais ; constantes et marqueur ne sont lus que dans le message JSON de la
  ligne de l'énumération ; code de sortie 0 exigé ; toute ligne brute, tout message hors des commandes, tout doublon ⇒ G-L7.
- CLL-08 et CLL-10 : `import Lean` après `import Item` ; aucun `open` ; noms pleinement qualifiés `_root_.Lean.…` ;
  `Lean.Name.toString` et `String.append` explicites, sans interpolation (réserve : non éprouvé sans Lean).
- CLL-09 : liste **fermée** des attributs permis (`@[…]` et `attribute […]`) ; `deriving` refusé (instance sans nom) ; énoncés
  imprimés aussi avec `set_option pp.notation false` (G-L5, transmis au relecteur).
- G-L7 exige G-L3+ : sans elle, du code de l'agent peut tourner à l'import du contrôle (CLL-04, CLL-09).
- CLL-14 : sortie tronquée et énoncé absent éprouvés.
Module **autonome** (bibliothèque standard seule), copié tel quel sur la machine.
"""
from __future__ import annotations

import hashlib
import json
import re

VERSION = "gardes_lean_v2"
MODULE_AGENT = "Item"
AXIOMES_PERMIS = ("propext", "Classical.choice", "Quot.sound")
ENONCE = "enonce_item"

MOTS_GL2 = ("sorry", "admit", "sorryAx")
MOTS_GL3 = ("axiom", "unsafe", "implemented_by", "extern")
MOTS_GL6 = ("notation", "notation3", "macro", "macro_rules", "syntax", "elab", "elab_rules", "infix", "infixl",
            "infixr", "prefix", "postfix", "declare_syntax_cat")
# G-L3+ : ajout du développeur (proposé) ; G-L7 en dépend (CLL-04, CLL-09)
MOTS_GL3_SUPPL = ("#eval", "#exit", "run_cmd", "run_elab", "run_meta", "run_tac", "by_elab", "initialize",
                  "builtin_initialize", "prelude", "private")
IMPORTS_PERMIS = ("Mathlib", "Batteries", "Aesop", "Qq", "Std", "Init", "Plausible", "ImportGraph", "ProofWidgets",
                  "LeanSearchClient")
ATTRIBUTS_PERMIS = ("simp", "reducible", "irreducible")
GENRES_DEFINITION = ("def", "abbrev", "structure", "class", "inductive", "opaque", "irreducible_def", "instance")
# auxiliaires admis sous un nom imprimé ou attendu sans être imprimés (liste fermée, à confirmer sur la chaîne installée)
AUXILIAIRES = re.compile(r"^(match_\d+|_nativeDecide_\d+(_\d+)?|_proof_\d+(_\d+)?|proof_\d+|_auxLemma\.\d+|eq_\d+|eq_def)$")
MARQUEUR_CONSTANTE = "CONSTANTE "
MARQUEUR_FIN = "CONSTANTES-FIN"
TAILLE_MAX_SOURCE = 256 * 1024
RE_NONCE = re.compile(r"^[0-9a-f]{32}$")


class ErreurLexicale(ValueError):
    """Le texte ne se lit pas comme Lean le lirait sans deviner : refus."""


def _debut_ident(c: str) -> bool:
    return c.isalpha() or c == "_"


def _suite_ident(c: str) -> bool:
    return c.isalnum() or c in "_'!?"


_CAR = re.compile(r"'(\\(x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4}|.)|[^\\'\n])'")
_BRUTE = re.compile(r'r(#*)"')


def masquer(source: str) -> str:
    """Lecteur de lexèmes : commentaires (`--`, `/- … -/` imbriqués), chaînes, chaînes brutes et caractères remplacés par des
    espaces (sauts de ligne gardés) ; identifiants lus en entier. Refus (`ErreurLexicale`) : `«`/`»` hors commentaire et
    chaîne ; élément non fermé ; littéral collé à un identifiant, à un nombre ou à un autre littéral ; apostrophe isolée."""
    sortie = list(source)
    n = len(source)

    def blanc(a: int, b: int) -> None:
        for k in range(a, b):
            if sortie[k] != "\n":
                sortie[k] = " "

    def fin_litteral(j: int) -> None:
        if j < n and (_suite_ident(source[j]) or source[j] in "\"'«»"):
            raise ErreurLexicale(f"littéral suivi d'un caractère collé (position {j})")

    i = 0
    while i < n:
        c = source[i]
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
        if c in "«»":
            raise ErreurLexicale(f"identifiant entre « » refusé (position {i})")
        if c == "r":
            m = _BRUTE.match(source, i)
            if m:
                fin = '"' + m.group(1)
                j = source.find(fin, m.end())
                if j < 0:
                    raise ErreurLexicale(f"chaîne brute non fermée (position {i})")
                blanc(i, j + len(fin))
                i = j + len(fin)
                fin_litteral(i)
                continue
        if _debut_ident(c):
            j = i + 1
            while j < n and _suite_ident(source[j]):
                j += 1
            if j < n and source[j] == '"':
                raise ErreurLexicale(f"chaîne collée à un identifiant (position {j})")
            i = j
            continue
        if c.isdigit():
            j = i + 1
            while j < n and (source[j].isalnum() or source[j] in "_."):
                j += 1
            if j < n and source[j] in "\"'":
                raise ErreurLexicale(f"littéral collé à un nombre (position {j})")
            i = j
            continue
        if c == '"':
            j = i + 1
            while j < n and source[j] != '"':
                j += 2 if source[j] == "\\" else 1
            if j >= n:
                raise ErreurLexicale(f"chaîne non fermée (position {i})")
            blanc(i, j + 1)
            i = j + 1
            fin_litteral(i)
            continue
        if c == "'":
            m = _CAR.match(source, i)
            if not m:
                raise ErreurLexicale(f"apostrophe hors d'un identifiant ou d'un caractère (position {i})")
            blanc(i, m.end())
            i = m.end()
            fin_litteral(i)
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
_RE_DERIVING = _motif_mots(("deriving",))
_RE_DEBUG = re.compile(r"set_option\s+debug\.|skipKernelTC")
_RE_IMPORT = re.compile(r"^[ \t]*(?:(?:public|meta|private)[ \t]+)*import[ \t]+(?:all[ \t]+)?([^\n]*)$", re.M)
_RE_THEOREME = re.compile(r"(?<![\w'.!?])(?:theorem|lemma)\s+([^\s:({\[⦃]+)")
_RE_DEF = re.compile(r"(?<![\w'.!?])(" + "|".join(GENRES_DEFINITION) + r")(?![\w'])")
_RE_NOM_LEAN = re.compile(r"^[^\W\d][\w'!?]*(\.[^\W\d][\w'!?]*)*$")
_RE_ATTR = re.compile(r"@\[([^\]]*)\]|(?<![\w'.!?])attribute\s*\[([^\]]*)\]")


def _ligne(texte: str, position: int) -> int:
    return texte.count("\n", 0, position) + 1


def _occurrences(motif: re.Pattern, texte: str) -> list[str]:
    return [f"« {m.group(1)} » ligne {_ligne(texte, m.start())}" for m in motif.finditer(texte)]


def attributs_hors_liste(masque: str) -> list[str]:
    """CLL-09 : tout attribut hors de `ATTRIBUTS_PERMIS` (formes `@[…]` et `attribute […]`, préfixes `local`, `scoped`, `-`)."""
    motifs = []
    for m in _RE_ATTR.finditer(masque):
        contenu = m.group(1) if m.group(1) is not None else m.group(2)
        for entree in contenu.split(","):
            e = re.sub(r"^\s*(?:(?:local|scoped)\s+)?-?\s*", "", entree)
            nom = (e.split() or [""])[0]
            if nom not in ATTRIBUTS_PERMIS:
                motifs.append(f"attribut hors liste « {nom or entree.strip()} » ligne {_ligne(masque, m.start())}")
    return motifs


def _definitions(masque: str) -> tuple[list[str], list[str]]:
    noms: list[str] = []
    anonymes: list[str] = []
    for m in _RE_DEF.finditer(masque):
        genre = m.group(1)
        j = m.end()
        while j < len(masque) and masque[j] in " \t\n":
            j += 1
        if genre == "class" and masque.startswith("inductive", j):
            continue
        if genre == "instance" and masque.startswith("(priority", j):
            k = masque.find(")", j)
            j = len(masque) if k < 0 else k + 1
            while j < len(masque) and masque[j] in " \t\n":
                j += 1
        t = re.match(r"[^\s:({\[⦃]+", masque[j:])
        nom = t.group(0) if t else ""
        if genre == "instance" and (not nom or nom.startswith(("where", ":="))):
            anonymes.append(f"instance anonyme ligne {_ligne(masque, m.start())}")
            continue
        if nom:
            noms.append(nom)
    return noms, anonymes


def analyser_texte(source: str, m: int, supplementaires: bool = True) -> dict:
    if not isinstance(m, int) or m < 1:
        raise ValueError("nombre d'étapes m entier ≥ 1 exigé")
    motifs: dict[str, list[str]] = {"G-L1": [], "G-L2": [], "G-L3": [], "G-L3+": [], "G-L4": [], "G-L6": []}
    if len(source.encode("utf-8")) > TAILLE_MAX_SOURCE:
        motifs["G-L1"].append(f"fichier de plus de {TAILLE_MAX_SOURCE} octets")
    try:
        masque = masquer(source)
    except ErreurLexicale as e:
        for g in ("G-L2", "G-L3", "G-L3+", "G-L4", "G-L6"):
            motifs[g].append(f"lexique refusé : {e}")
        return {"motifs": motifs, "definitions": [], "theoremes": []}
    motifs["G-L2"] += _occurrences(_RE_GL2, masque)
    motifs["G-L3"] += _occurrences(_RE_GL3, masque)
    motifs["G-L6"] += _occurrences(_RE_GL6, masque)
    motifs["G-L6"] += [f"instance dérivée (deriving) ligne {_ligne(masque, x.start())}" for x in _RE_DERIVING.finditer(masque)]
    if supplementaires:
        motifs["G-L3+"] += _occurrences(_RE_GL3_SUPPL, masque)
        motifs["G-L3+"] += [f"« {x.group(0).strip()} » ligne {_ligne(masque, x.start())}" for x in _RE_DEBUG.finditer(masque)]
        motifs["G-L3+"] += attributs_hors_liste(masque)
        for imp in _RE_IMPORT.finditer(masque):
            for module in imp.group(1).split():
                if module.split(".")[0] not in IMPORTS_PERMIS:
                    motifs["G-L3+"].append(f"import non permis « {module} » ligne {_ligne(masque, imp.start())}")
    theoremes = [t.group(1) for t in _RE_THEOREME.finditer(masque)]
    for nom in noms_attendus(m):
        if nom not in theoremes:
            motifs["G-L4"].append(f"déclaration `theorem {nom}` (ou `lemma`) absente")
    definitions, anonymes = _definitions(masque)
    motifs["G-L6"] += anonymes
    for d in definitions:
        if not _RE_NOM_LEAN.match(d):
            motifs["G-L6"].append(f"nom de définition non imprimable « {d} »")
    return {"motifs": motifs, "definitions": [d for d in definitions if _RE_NOM_LEAN.match(d)], "theoremes": theoremes}


# ---- fichier de contrôle (G-L7), passé par l'entrée standard ---------------------------------------------------------------

_GENRE_SURETE = """    let ci := _root_.Lean.Environment.find? env n
    let genre := match ci with
      | _root_.Option.some (_root_.Lean.ConstantInfo.thmInfo _) => "theoreme"
      | _root_.Option.some (_root_.Lean.ConstantInfo.defnInfo _) => "definition"
      | _root_.Option.some (_root_.Lean.ConstantInfo.axiomInfo _) => "axiome"
      | _root_.Option.some (_root_.Lean.ConstantInfo.opaqueInfo _) => "opaque"
      | _root_.Option.some (_root_.Lean.ConstantInfo.inductInfo _) => "inductif"
      | _root_.Option.some (_root_.Lean.ConstantInfo.ctorInfo _) => "constructeur"
      | _root_.Option.some (_root_.Lean.ConstantInfo.recInfo _) => "recurseur"
      | _root_.Option.some (_root_.Lean.ConstantInfo.quotInfo _) => "quotient"
      | _root_.Option.none => "absent"
    let surete := match ci with
      | _root_.Option.some (_root_.Lean.ConstantInfo.defnInfo v) =>
        match v.safety with
        | _root_.Lean.DefinitionSafety.safe => "sure"
        | _root_.Lean.DefinitionSafety.unsafe => "non-sure"
        | _root_.Lean.DefinitionSafety.partial => "partielle"
      | _root_.Option.some c => _root_.cond (_root_.Lean.ConstantInfo.isUnsafe c) "non-sure" "sure"
      | _root_.Option.none => "absente"
    _root_.String.append acc (_root_.String.append "CONSTANTE " (_root_.String.append (_root_.Lean.Name.toString n)
      (_root_.String.append " " (_root_.String.append genre (_root_.String.append " " (_root_.String.append surete "\\n"))))))
"""

_FIN = """  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text
    (_root_.String.append texte "CONSTANTES-FIN {nonce}")))
"""

ENUMERATION_A = """#eval show _root_.Lean.CoreM _root_.Unit from do
  let env ← _root_.Lean.getEnv
  let some idx := _root_.Lean.Environment.getModuleIdx? env `{module}
    | _root_.Lean.throwError "CONTROLE-MODULE-ABSENT"
  let noms := _root_.Lean.ModuleData.constNames ((_root_.Lean.Environment.header env).moduleData[idx.toNat]!)
  let ligne := fun (acc : _root_.String) (n : _root_.Lean.Name) =>
""" + _GENRE_SURETE + """  let texte := _root_.Array.foldl ligne "" noms
""" + _FIN

ENUMERATION_B = """#eval show _root_.Lean.CoreM _root_.Unit from do
  let env ← _root_.Lean.getEnv
  let some idx := _root_.Lean.Environment.getModuleIdx? env `{module}
    | _root_.Lean.throwError "CONTROLE-MODULE-ABSENT"
  let dans := fun (n : _root_.Lean.Name) =>
    match _root_.Lean.Environment.getModuleIdxFor? env n with
    | _root_.Option.some j => _root_.Nat.beq j.toNat idx.toNat
    | _root_.Option.none => _root_.Bool.false
  let noms := _root_.Std.HashMap.fold
    (fun (acc : _root_.Array _root_.Lean.Name) n _ => _root_.cond (dans n) (_root_.Array.push acc n) acc) #[]
    (_root_.Lean.SMap.map₁ (_root_.Lean.Environment.constants env))
  let ligne := fun (acc : _root_.String) (n : _root_.Lean.Name) =>
""" + _GENRE_SURETE + """  let texte := _root_.Array.foldl ligne "" noms
""" + _FIN
ENUMERATIONS = {"A": ENUMERATION_A, "B": ENUMERATION_B}


def noms_attendus(m: int) -> list[str]:
    return [f"etape_{i}" for i in range(1, m + 1)] + [ENONCE]


def fichier_controle(m: int, definitions: list[str], nonce: str, variante: str = "A",
                     module: str = MODULE_AGENT) -> tuple[str, dict[int, tuple[str, str]]]:
    """Texte du contrôle (passé par l'entrée standard de `lean --stdin --json`) et carte « ligne → (genre, nom) »."""
    if variante not in ENUMERATIONS:
        raise ValueError(f"variante d'énumération inconnue {variante!r}")
    if not RE_NONCE.match(nonce or ""):
        raise ValueError("nonce de 32 caractères hexadécimaux exigé")
    lignes = [f"import {module}", "import Lean", ""]
    carte: dict[int, tuple[str, str]] = {}

    def ajouter(texte: str, genre: str, nom: str) -> None:
        lignes.append(texte)
        carte[len(lignes)] = (genre, nom)

    for nom in noms_attendus(m):
        ajouter(f"#check @{nom}", "enonce", nom)
    for nom in noms_attendus(m):
        ajouter(f"set_option pp.notation false in #check @{nom}", "enonce_brut", nom)
    for nom in noms_attendus(m):
        ajouter(f"#print axioms {nom}", "axiomes", nom)
    vus = set()
    for d in definitions:
        if not _RE_NOM_LEAN.match(d) or d in vus:
            continue
        vus.add(d)
        ajouter(f"#print {d}", "impression", d)
    lignes.append("")
    carte[len(lignes) + 1] = ("constantes", "*")
    lignes += ENUMERATIONS[variante].format(module=module, nonce=nonce).splitlines()
    return "\n".join(lignes) + "\n", carte


def empreinte_texte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


# ---- lecture des sorties de Lean ---------------------------------------------------------------------------------------

def lire_messages(sortie: str) -> tuple[list[dict], list[str]]:
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


def lire_controle(sortie: str, carte: dict[int, tuple[str, str]], nonce: str) -> dict:
    """Une commande = exactement un message d'information sur sa ligne ; tout le reste est une anomalie de G-L7."""
    messages, brut = lire_messages(sortie)
    par_ligne: dict = {}
    for msg in messages:
        par_ligne.setdefault(_ligne_message(msg), []).append(msg)
    anomalies = [f"ligne brute hors JSON : {b[:120]!r}" for b in brut]
    erreurs: list[str] = []
    erreurs_par_nom: dict[str, list[str]] = {}
    avertissements: list[str] = []
    enonces, enonces_bruts, axiomes, impressions = {}, {}, {}, {}
    constantes: list[tuple[str, str, str]] = []
    fin_vue = False
    for ligne, msgs in par_ligne.items():
        if ligne not in carte:
            anomalies.append(f"message hors des commandes du contrôle (ligne {ligne})")
        for msg in msgs:
            data = str(msg.get("data", ""))
            genre, nom = carte.get(ligne, ("?", "?"))
            if msg.get("severity") == "error":
                erreurs.append(f"ligne {ligne} ({genre} {nom}) : {data[:300]}")
                erreurs_par_nom.setdefault(nom, []).append(data[:300])
            elif msg.get("severity") == "warning":
                avertissements.append(f"ligne {ligne} ({genre} {nom}) : {data[:200]}")
            if genre != "constantes" and (MARQUEUR_CONSTANTE in data or MARQUEUR_FIN in data):
                anomalies.append(f"marqueur de l'énumération hors de sa ligne (ligne {ligne})")
    for ligne, (genre, nom) in carte.items():
        msgs = par_ligne.get(ligne, [])
        infos = [x for x in msgs if x.get("severity") == "information"]
        if len(infos) > 1:
            anomalies.append(f"{len(infos)} messages d'information pour une commande (ligne {ligne}, {genre} {nom})")
            continue
        if not infos:
            if not any(x.get("severity") == "error" for x in msgs):
                anomalies.append(f"commande sans réponse (ligne {ligne}, {genre} {nom})")
            continue
        texte = str(infos[0].get("data", ""))
        if genre == "enonce":
            enonces[nom] = texte.strip()
        elif genre == "enonce_brut":
            enonces_bruts[nom] = texte.strip()
        elif genre == "axiomes":
            axiomes[nom] = lire_axiomes(texte)
        elif genre == "impression":
            impressions[nom] = texte.strip()
        elif genre == "constantes":
            lignes = [x.strip() for x in texte.splitlines() if x.strip()]
            if lignes and lignes[-1] == f"{MARQUEUR_FIN} {nonce}":
                fin_vue = True
                lignes = lignes[:-1]
            for x in lignes:
                parties = x[len(MARQUEUR_CONSTANTE):].rsplit(" ", 2) if x.startswith(MARQUEUR_CONSTANTE) else []
                if len(parties) == 3:
                    constantes.append((parties[0], parties[1], parties[2]))
                else:
                    anomalies.append(f"ligne d'énumération illisible : {x[:120]!r}")
    return {"enonces": enonces, "enonces_bruts": enonces_bruts, "axiomes": axiomes, "impressions": impressions,
            "erreurs": erreurs, "erreurs_par_nom": erreurs_par_nom, "avertissements": avertissements,
            "constantes": constantes, "fin_enumeration": fin_vue, "anomalies": anomalies}


def constantes_non_couvertes(constantes: list[tuple[str, str, str]], imprimees: set[str], attendus: set[str]) -> list[str]:
    """CLL-03 : couverte = imprimée, ou descendante d'un inductif imprimé, ou auxiliaire de la liste fermée sous un nom
    imprimé ou attendu. Théorèmes et axiomes sont jugés ailleurs (G-L4, G-L3)."""
    genres = {nom: genre for nom, genre, _ in constantes}
    inductifs = {n for n in imprimees if genres.get(n) == "inductif"}
    manquantes = []
    for nom, genre, _ in constantes:
        if genre in ("theoreme", "axiome") or nom in imprimees:
            continue
        if any(nom.startswith(r + ".") for r in inductifs):
            continue
        if any(nom.startswith(r + ".") and AUXILIAIRES.match(nom[len(r) + 1:]) for r in imprimees | attendus):
            continue
        manquantes.append(f"{nom} ({genre})")
    return manquantes


# ---- verdict des gardes -------------------------------------------------------------------------------------------------

def evaluer(source: str, m: int, compilation: dict, controle: dict, supplementaires: bool = True) -> dict:
    """compilation : {"code", "sortie", "olean_present", ["sortie_tronquee"]} ;
    controle : {"code", "sortie", "texte", "carte", "nonce", ["sortie_tronquee"]}."""
    texte = analyser_texte(source, m, supplementaires)
    motifs = {g: list(v) for g, v in texte["motifs"].items()}
    for g in ("G-L1", "G-L2", "G-L3", "G-L3+", "G-L4", "G-L5", "G-L6", "G-L7"):
        motifs.setdefault(g, [])
    if not supplementaires:
        motifs["G-L3+"] = []
        motifs["G-L7"].append("G-L7 exige G-L3+ : sans elle, du code de l'agent peut tourner à l'import du contrôle")

    # G-L1
    messages_agent, _ = lire_messages(compilation.get("sortie", ""))
    if compilation.get("code") != 0:
        motifs["G-L1"].append(f"code de sortie de la compilation {compilation.get('code')!r}")
    motifs["G-L1"] += [f"erreur : {str(x.get('data', ''))[:300]}" for x in messages_agent if x.get("severity") == "error"]
    if not compilation.get("olean_present"):
        motifs["G-L1"].append("module compilé (.olean) absent")
    if compilation.get("sortie_tronquee"):
        motifs["G-L1"].append("sortie de compilation tronquée")
    for x in messages_agent:
        if x.get("severity") == "warning" and "sorry" in str(x.get("data", "")):
            motifs["G-L2"].append(f"avertissement de la compilation : {str(x.get('data'))[:200]}")

    # G-L7
    nonce = controle.get("nonce", "")
    lu = lire_controle(controle.get("sortie", ""), controle.get("carte", {}), nonce)
    if controle.get("code") != 0:
        motifs["G-L7"].append(f"code de sortie du contrôle {controle.get('code')!r} (0 exigé)")
    if not RE_NONCE.match(nonce or "") or f"{MARQUEUR_FIN} {nonce}" not in controle.get("texte", ""):
        motifs["G-L7"].append("nonce du contrôle absent ou différent du texte envoyé")
    if not lu["fin_enumeration"]:
        motifs["G-L7"].append("marqueur de fin à nonce absent du message de l'énumération")
    if controle.get("sortie_tronquee"):
        motifs["G-L7"].append("sortie du contrôle tronquée")
    motifs["G-L7"] += lu["anomalies"]
    attendus = noms_attendus(m)
    motifs["G-L7"] += [f"erreur du contrôle : {e}" for e in lu["erreurs"]
                       if not any(f" {n}) :" in e for n in attendus)]

    # G-L4 et G-L5
    genres = {nom: genre for nom, genre, _ in lu["constantes"]}
    for nom in attendus:
        if nom in lu["erreurs_par_nom"]:
            motifs["G-L4"].append(f"contrôle en erreur sur {nom} : {lu['erreurs_par_nom'][nom][0][:200]}")
        if genres.get(nom) != "theoreme":
            motifs["G-L4"].append(f"{nom} de genre {genres.get(nom, 'absent')!r} dans le module, « theoreme » exigé")
        if not lu["enonces"].get(nom):
            motifs["G-L5"].append(f"énoncé imprimé de {nom} absent")
        if not lu["enonces_bruts"].get(nom):
            motifs["G-L5"].append(f"énoncé imprimé sans notation de {nom} absent")
    # G-L2
    for nom in attendus:
        if nom not in lu["axiomes"]:
            motifs["G-L2"].append(f"`#print axioms {nom}` sans réponse")
        elif lu["axiomes"][nom] is None:
            motifs["G-L2"].append(f"`#print axioms {nom}` illisible")
        else:
            hors = [a for a in lu["axiomes"][nom] if a not in AXIOMES_PERMIS]
            if hors:
                motifs["G-L2"].append(f"{nom} dépend de : {', '.join(hors)}")
    # G-L3
    for nom, genre, surete in lu["constantes"]:
        if genre == "axiome":
            motifs["G-L3"].append(f"constante de genre axiome dans le module : {nom}")
        if surete != "sure":
            motifs["G-L3"].append(f"constante {surete} dans le module : {nom} ({genre})")
    # G-L6
    for d in texte["definitions"]:
        if not lu["impressions"].get(d):
            motifs["G-L6"].append(f"`#print {d}` sans réponse")
    manquantes = constantes_non_couvertes(lu["constantes"], set(lu["impressions"]), set(attendus))
    motifs["G-L6"] += [f"constante non imprimée : {x}" for x in manquantes]

    gardes = {g: {"ok": not v, "motifs": v} for g, v in sorted(motifs.items())}
    return {"version": VERSION, "gardes": gardes, "accepte_gardes": all(x["ok"] for x in gardes.values()),
            "enonces_imprimes": lu["enonces"], "enonces_sans_notation": lu["enonces_bruts"],
            "impressions": lu["impressions"], "axiomes": lu["axiomes"], "constantes": lu["constantes"],
            "avertissements_controle": lu["avertissements"], "supplementaires": supplementaires}


def pour_relecteur(verdict: dict) -> str:
    lignes = ["## Énoncés imprimés par Lean (ordre du fichier de contrôle)"]
    lignes += list(verdict["enonces_imprimes"].values())
    lignes.append("## Mêmes énoncés sans notation (pp.notation false)")
    lignes += list(verdict["enonces_sans_notation"].values())
    if verdict["impressions"]:
        lignes.append("## Définitions introduites, imprimées en entier")
        lignes += list(verdict["impressions"].values())
    return "\n".join(lignes) + "\n"
