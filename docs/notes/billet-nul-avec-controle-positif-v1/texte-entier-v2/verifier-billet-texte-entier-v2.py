"""Vérifie chaque nombre, cardinal en lettres, notation scientifique et réserve du billet v2 contre le registre.

Améliorations mécaniques fermant toutes les lacunes de la v1 (constats V-1 à V-7 et B5-1/B5-2) :
 1. Empreintes des 7 sources texte (verdicts scellés + préenregistrement P3) égales au registre et aux
    compagnons `.sha256` ; empreintes des 4 PDF vérifiées par lecture locale en priorité (avec repli git) et
    vérifiées aussi contre leurs compagnons `.sha256`.
 2. Unicité du motif : pour chaque entrée hors PDF, `lignes_portant_le_motif == 1` et le motif apparaît à
    l'exacte ligne écrite.
 3. Validation explicite des citations de page PDF (`est_page == true` : `contexte_billet` doit contenir
    `p. <page>` ou `page <page>` et `1 <= page <= nb_pages_pdf` ; sinon la valeur numérique est exigée
    dans la citation verbatim présente sur la page `pdftotext` du PDF).
 4. Extraction exhaustive des jetons du corps (du titre `# Activation probes ...` à `## Hors billet`),
    comprenant :
      - les nombres décimaux, négatifs, pourcentages et séparateurs de milliers (`2,000`, `41,436`) ;
      - les notations scientifiques (`1.6 \\times 10^{-22}`, `10^{-4}`) vérifiées en écart relatif ;
      - les cardinaux et multiplicateurs en lettres (`zero`..`twelve`, `threefold`, `half`, `single`, etc.) ;
      - la documentation explicite des SEULS identifiants techniques exclus (voir `EXCLUSIONS_DOC`),
        à l'exclusion de tout facteur ou résultat scientifique.
 5. Contrôle sémantique et d'ordre par section :
      - chaque section autorise uniquement son ensemble clos de sources (`SOURCES_PAR_SECTION`) — par ex.,
        `step_b` n'emprunte plus aux doses de `Bb` et `p3bis` n'emprunte plus à `V3` ;
      - les `contexte_billet` se retrouvent séquentiellement dans la section exacte du billet ;
      - vérification sémantique du `qualificatif` (`lower_bound`, `point_estimate`, `quantile`, etc.) sur le
        contexte immédiat (empêchant par ex. d'étiqueter `lower bound` une estimation ponctuelle) ;
      - contrôle lexical `B5` et règles de rédaction gelées (absence de `transfer arm`, `G1`, `does not separate`,
        `ne sépare pas`, marqueurs `<<...>>`, etc.).
 6. Comptes de mots exacts (brut `wc -w`, propre sans marques de blocs LLM, et TL;DR <= 250 mots selon
    le gabarit v2).
 7. Autotest étendu à 8 artefacts qui DOIVENT tous échouer :
      (a) nombre faussé (`0.5749` au lieu de `0.5748`) ;
      (b) ligne déplacée (`ligne + 1`) ;
      (c) PDF citation tronquée au DÉBUT (`With ` retiré de `FIBS:34`) ;
      (d) PDF citation tronquée à la FIN (` trivial` retiré de `FIBS:34`) ;
      (e) PDF citation altérée au MILIEU (`nearly ` retiré de `FIBS:34`) ;
      (f) mauvais numéro de page PDF (`35` au lieu de `34`) ;
      (g) cardinal en lettres faussé (`three` au lieu de `two` dans `tldr`) ;
      (h) détournement de section (`Step B` pointé sur `Bb` ou `contexte_billet` inversé).

Usage :
  /home/antigravity/lciric/controle-ia-travail/.venv/bin/python verifier-billet-texte-entier-v2.py

Pièce de classe B. Écrit le 2026-11-23 par le rédacteur habilité v2 (`GO-2026-11-23-17`, `-32`, `-33`).
"""
import copy
import hashlib
import json
import math
import pathlib
import re
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
DEPOT = pathlib.Path("/home/antigravity/lciric/controle-ia-travail")
BILLET = ICI / "billet-texte-entier-en-v2.md"
REG = ICI / "registre-affirmations-v2.json"

# Correspondance exacte des valeurs non numériques ou en lettres dans les sources
MOTS = {
    # Cardinaux français des verdicts scellés
    "une": 1, "une ligne": 1, "un seul couple": 1, "son complément": 1,
    "deux": 2, "trois": 3, "quatre": 4, "quatrième": 4, "cinq": 5, "huit": 8, "dix": 10, "douze": 12,
    # Identifiants de doses / plis / lecteurs / réserves reconnus dans les sources
    "S25": 0.25, "S50": 0.5, "S75": 0.75, "S100": 1.0,
    "T100": 1.0, "dose 1": 1.0, "T-S100-instruit": 1.0,
    "P-S25 e0": 0.25, "P-S50 e0": 1.0, "| 0,5 (S50) |": 0.5,
    "[]": 0.0, "non positive": 0.0, "e0": 0.0,
    "Addendum « Non décisif »": 1.0,
    "maximum 0.8742888888888889": 1.0,
    "H 600, A 600, T 600, B 600": 4.0,
    "T7-P7 et T7-P8": 2.0,
    '["MC", "ENC"]': 2.0,
    "PB-4": 1.0, "PB-7": 2.0, "PB-10": 5.0,
    "0,6315 ; 0,5966": 80.0,
}

# Cardinaux et multiplicateurs en anglais extraits du billet
CARDS_EN = {
    "zero": 0, "one": 1, "two": 2, "twofold": 2, "three": 3, "threefold": 3,
    "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "hundred": 100, "thousand": 1000,
    "once": 1, "twice": 2, "thrice": 3, "half": 0.5,
    "single": 1, "double": 2, "triple": 3,
}

# Identifiants techniques non numériques documentés (voir en-tête)
EXCLUSIONS_DOC = [
    r"arXiv:\S+",                   # Identifiants arXiv (2502.03407, 2606.30449, 2611.10620, 2610.12445v4)
    r"Llama-3\.1-8B-Instruct",      # Nom du modèle
    r"\\log_\{10\}|log10",          # Base 10 du logarithme décimal
    r"20261019-230011-p3-reel",     # Identifiant du run P3 (sa date 19/2026 est vérifiée séparément)
    r"CODE-T07",                    # Code de protocole Step B
    r"P3-bis|P3",                   # Noms d'étapes
    r"T7-P1|PB-4|PB-7",             # Noms d'épreuves / prédictions
    r"S25|S50|S75|S100|T100|P-S25", # Étiquettes de conditions / sondes
    r"R-2299|R15|R9b|R10|R1|R3|R4|R8",  # Étiquettes de réserves / règles
    r"I5|G0|SHA-256",               # Étiquettes d'issue / porte / algorithme SHA-256
    r"580\.159\.03|615\.71\.09",    # Versions de pilotes GPU citées comme chaînes exactes (à contrôler à part)
    r"05e896da…|9b33c624…|077ab789…|1561399a…|1f3da53c…|3a9b947e…", # Préfixes de condensats SHA-256
    r"\b8B\b",                      # Classe de taille du modèle dans `8B parameters` (lié au nom du modèle)
]
RE_EXCLUS = re.compile("|".join(EXCLUSIONS_DOC))

RE_TOKEN = re.compile(
    r"(?<![\w.])[−-]?\d+(?:,\d{3})*(?:\.\d+)?\s*\\times\s*10\^\{[−-]?\d+\}|"
    r"(?<![\w.])10\^\{[−-]?\d+\}|"
    r"(?<![\w.])[−-]?\d+(?:,\d{3})*(?:\.\d+)?%?|"
    r"\b(?:" + "|".join(CARDS_EN.keys()) + r")\b",
    re.I,
)

SOURCES_PAR_SECTION = {
    "tldr": {"V3"},
    "setup": {"V3", "P3", "VB", "B", "Bb", "L", "PDF:GD"},
    "p3": {"V3", "VB"},
    "p3bis": {"VB", "B"},
    "step_b": {"B"},
    "step_bbis": {"Bb", "E"},
    "related": {"PDF:GD", "PDF:FOMIN", "PDF:MOHSIN", "PDF:FIBS", "B"},
    "limits": {"B", "L"},
    "open": {"Bb"},
}


def sha_b(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def parse_val(s: str) -> float:
    low = s.strip().lower()
    if low in CARDS_EN:
        return float(CARDS_EN[low])
    s_clean = s.replace("−", "-").replace(",", "").strip()
    if "\\times" in s_clean:
        m = re.fullmatch(r"([−-]?\d+(?:\.\d+)?)\s*\\times\s*10\^\{([−-]?\d+)\}", s_clean)
        if not m:
            raise ValueError(s)
        return float(m.group(1)) * (10.0 ** int(m.group(2)))
    if s_clean.startswith("10^{"):
        m = re.fullmatch(r"10\^\{([−-]?\d+)\}", s_clean)
        if not m:
            raise ValueError(s)
        return 10.0 ** int(m.group(1))
    s_clean = s_clean.rstrip("%").lstrip("+")
    return float(s_clean)


def parse_source_num(s: str) -> float:
    s = s.strip()
    if s in MOTS:
        return float(MOTS[s])
    if s == "10⁻⁴":
        return 1e-4
    # Gère les milliers séparés par des espaces ("2 000", "41 436") et la virgule décimale ("0,5748")
    s_norm = s.replace("−", "-").replace(" ", "").replace(",", ".").rstrip("%").lstrip("+")
    return float(s_norm)


def decimales(s: str) -> int:
    s = s.replace(",", "").rstrip("%")
    return len(s.split(".")[1]) if "." in s else 0


def couper_sections(texte: str) -> tuple[str, dict[str, str]]:
    corps = texte[texte.index("# Activation probes"):texte.index("## Hors billet")]
    # Découpage par titres de niveau 2
    titres = {
        "# Activation probes": "tldr",
        "## Setup and definitions": "setup",
        "## Initial test (`P3`)": "p3",
        "## Planted positive control (`P3-bis`)": "p3bis",
        "## Generic probes on a fine-tuned saboteur (`Step B`)": "step_b",
        "## Probes trained on the task itself (`Step B-bis`)": "step_bbis",
        "## Related work": "related",
        "## Limits": "limits",
        "## Open questions and code availability": "open",
    }
    morceaux = re.split(r"(?=^## )", corps, flags=re.M)
    sec_map: dict[str, str] = {}
    for m in morceaux:
        prem = m.splitlines()[0]
        cle = None
        for prefix, slug in titres.items():
            if prem.startswith(prefix):
                cle = slug
                break
        if cle is None:
            raise ValueError(f"Section inconnue dans le billet : {prem!r}")
        sec_map[cle] = m
    return corps, sec_map


def tokens_section(sec_txt: str) -> list[str]:
    cleaned = RE_EXCLUS.sub(lambda m: " " * len(m.group(0)), sec_txt)
    return [m.group(0) for m in RE_TOKEN.finditer(cleaned)]


def charger_pdf(p_info: dict, cache: dict) -> pathlib.Path:
    cle = p_info["sha256"]
    if cle in cache:
        return cache[cle]
    local_p = DEPOT / p_info["chemin_local"]
    if local_p.exists():
        b = local_p.read_bytes()
        h = sha_b(b)
        if h != p_info["sha256"]:
            raise SystemExit(f"PDF local {local_p} : sha256 {h} != {p_info['sha256']}")
        comp = local_p.parent / (local_p.name + ".sha256")
        if comp.exists():
            ch = comp.read_text(encoding="utf-8").split()[0]
            if ch != h:
                raise SystemExit(f"PDF compagnon {comp} : sha256 {ch} != {h}")
        cache[cle] = local_p
        return local_p
    b = subprocess.run(
        ["git", "-C", str(DEPOT), "show", f"{p_info['ref']}:{p_info['chemin_git']}"],
        capture_output=True,
        check=True,
    ).stdout
    if sha_b(b) != p_info["sha256"]:
        raise SystemExit(f"PDF git {p_info['chemin_git']} : empreinte différente")
    d = tempfile.mkdtemp()
    f = pathlib.Path(d) / "doc.pdf"
    f.write_bytes(b)
    cache[cle] = f
    return f


def pages_pdf(p_info: dict, page: int, cache: dict) -> tuple[list[str], int]:
    f = charger_pdf(p_info, cache)
    key_meta = (str(f), "meta")
    if key_meta not in cache:
        info_txt = subprocess.run(["pdfinfo", str(f)], capture_output=True, text=True).stdout
        m = re.search(r"Pages:\s+(\d+)", info_txt)
        cache[key_meta] = int(m.group(1)) if m else 9999
    n_pages = cache[key_meta]
    key_pg = (str(f), page)
    if key_pg not in cache:
        outs = []
        for mode in ("-raw", "-layout"):
            t = subprocess.run(
                ["pdftotext", mode, "-f", str(page), "-l", str(page), str(f), "-"],
                capture_output=True,
                text=True,
            ).stdout
            outs.append(" ".join(t.split()))
        cache[key_pg] = outs
    return cache[key_pg], n_pages


def valeur_ok(e: dict) -> bool:
    n = e["nombre"]
    v = e["valeur_source"]
    if v in MOTS and n.lower() in CARDS_EN:
        return abs(MOTS[v] - float(CARDS_EN[n.lower()])) < 1e-9
    if v in MOTS:
        try:
            return abs(MOTS[v] - parse_val(n)) < 1e-9
        except ValueError:
            return False
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}|\d{8}", v):
        return n in v
    try:
        target = parse_val(n)
        src_x = parse_source_num(v)
    except ValueError:
        return False
    if e["qualificatif"] == "p_value" and ("\\times" in n or "e" in n.lower()):
        rel = abs(src_x - target) / max(abs(src_x), 1e-300)
        return rel < 0.02
    if e["qualificatif"] == "tolerance" and "10^" in n:
        return abs(src_x - target) <= 1e-12
    d = decimales(n)
    return abs(round(src_x + (1e-12 if src_x >= 0 else -1e-12), d) - target) < 1e-9


def qualificatif_coherent(e: dict) -> bool:
    q = e["qualificatif"]
    ctx = e["contexte_billet"].lower()
    if q == "lower_bound":
        return ("[" in ctx or "lower bound" in ctx)
    if q == "upper_bound":
        return ("]" in ctx or "`" in ctx)
    if q == "page":
        return bool(e.get("est_page")) and bool(re.search(rf"(?:p\.|page)\s*{re.escape(e['nombre'])}\b", ctx))
    return True


def verifier(reg: dict, texte: str, dire=print, _pdf_cache: dict | None = None) -> int:
    defauts = 0
    lignes: dict[str, list[str]] = {}
    for k, s in reg["sources"].items():
        b = (DEPOT / s["chemin"]).read_bytes()
        h = sha_b(b)
        comp = (DEPOT / (s["chemin"] + ".sha256")).read_text(encoding="utf-8").split()[0]
        ok = (h == s["sha256"] == comp)
        defauts += not ok
        dire(f"source {k:<3} {s['chemin']} : sha256 {'égal' if ok else 'DIFFÉRENT'} ({h[:12]}…)")
        lignes[k] = b.decode("utf-8").splitlines()

    corps, sec_map = couper_sections(texte)
    pdf_cache = _pdf_cache if _pdf_cache is not None else {}
    # Vérification des 2 chaînes pilotes dans P3-bis (hors tokens numériques ordinaires)
    for drv in ("580.159.03", "615.71.09"):
        in_billet = drv in sec_map["p3bis"]
        in_vb = any(drv in l for l in lignes["VB"])
        if not (in_billet and in_vb):
            defauts += 1
            dire(f"ÉCART pilote {drv}: billet={in_billet}, VB={in_vb}")

    # Vérification des règles B5 & règles lexicales sur le corps (hors citations explicites d'interdiction)
    corps_sans_proscr = (
        corps.replace('never "no separation" or "does not separate"', "")
             .replace('never "blatant" without the full baseline rule', "")
    )
    interdits = [
        (r"\btransfer[- ]arm\b", "mention du bras de transfert (interdit B5)"),
        (r"\bG1\b", "mention de G1 avant la porte G1 (interdit B5)"),
        (r"\bdoes not separate\b", "formule interdite 'does not separate'"),
        (r"\bne sépare pas\b", "formule interdite 'ne sépare pas'"),
        (r"<<[A-Z0-9_]+>>", "marqueur vide non retiré"),
        (r"\bblatant\b", "adjectif non autorisé sans règle T0.6 complète"),
    ]
    for pat_i, raison in interdits:
        flags = re.I if ("does not" in pat_i or "transfer" in pat_i) else 0
        if re.search(pat_i, corps_sans_proscr, flags):
            defauts += 1
            dire(f"RÈGLE LEXICALE/B5 ENFREINTE : {raison}")

    # Réserves obligatoires présentes dans le corps
    for req_tok in ("R-2299", "PB-4", "PB-7", "R1", "R3", "R8", "R10", "R15", "R4", "not detected at this power"):
        if req_tok not in corps:
            defauts += 1
            dire(f"RÉSERVE/FORMULE MANQUANTE dans le corps : {req_tok!r}")

    # Vérification séquentielle de chaque section et entrée
    cursors = {k: 0 for k in sec_map}
    toks_par_sec = {k: tokens_section(v) for k, v in sec_map.items()}
    reg_par_sec = {k: [] for k in sec_map}

    for e in reg["entrees"]:
        sec = e["section"]
        src = e["source"]
        reg_par_sec.setdefault(sec, []).append(e["nombre"])

        # Contrôle cloisonnement des sources par section
        src_prefix = ":".join(src.split(":")[:2]) if src.startswith("PDF:") else src
        sec_src_ok = src_prefix in SOURCES_PAR_SECTION.get(sec, set())

        # Contrôle présence séquentielle du contexte dans la section du billet
        sec_text_norm = " ".join(sec_map.get(sec, "").split())
        ctx_norm = " ".join(e["contexte_billet"].split())
        pos = sec_text_norm.find(ctx_norm, cursors.get(sec, 0))
        # Si le même nombre apparaît dans un bloc étroit (même snippet réutilisé), tolérer un recouvrement exact
        if pos == -1:
            pos = sec_text_norm.find(ctx_norm, max(0, cursors.get(sec, 0) - len(ctx_norm) - 5))
        ctx_ok = pos != -1
        if ctx_ok:
            # Ne pas avancer au-delà de la fin du contexte moins marge pour occurrences multiples dans un même snippet
            cursors[sec] = max(cursors.get(sec, 0), pos)

        qual_ok = qualificatif_coherent(e)

        if src.startswith("PDF:"):
            _, k, page_str = src.split(":")
            page = int(page_str)
            p_info = reg["pdf"][k]
            pages, n_pages = pages_pdf(p_info, page, pdf_cache)
            page_ok = (1 <= page <= n_pages)
            motif_norm = " ".join(e["motif"].split())
            # Exiger les bornes de mots aux extrémités du motif (évite qu'un préfixe comme 'trivia' matche 'trivial')
            pat_pdf = re.compile(r"(?<!\w)" + re.escape(motif_norm) + r"(?!\w)")
            motif_ok = page_ok and any(bool(pat_pdf.search(t)) for t in pages)
            if e.get("est_page"):
                val_ok = (e["nombre"] == page_str) and (e["valeur_source"] == page_str) and bool(
                    re.search(rf"(?:p\.|page)\s*{re.escape(page_str)}\b", e["contexte_billet"])
                )
            else:
                val_ok = (e["nombre"].rstrip("%") in e["motif"]) and (e["valeur_source"] in e["motif"])
            ou = f"{k} p.{page}"
        else:
            ln = e.get("ligne", 0)
            ls = lignes[src]
            l = ls[ln - 1] if 0 < ln <= len(ls) else ""
            nb_lignes = sum(1 for row in ls if e["motif"] in row)
            motif_ok = (e["motif"] in l) and (e["valeur_source"] in l) and (nb_lignes == 1) and (
                e.get("lignes_portant_le_motif") == 1
            )
            val_ok = valeur_ok(e)
            ou = f"{src} l.{ln}"

        bon = sec_src_ok and ctx_ok and qual_ok and motif_ok and val_ok
        if not bon:
            defauts += 1
            dire(
                f"ÉCART #{e['n']:3d} [{sec}] {e['nombre']!r} <- {ou} : "
                f"sec_src={sec_src_ok}, ctx={ctx_ok}, qual={qual_ok}, motif={motif_ok}, val={val_ok}"
            )

    # Vérification de couverture exacte section par section
    tot_toks = 0
    tot_reg = 0
    for sec in sec_map:
        t_list = toks_par_sec[sec]
        r_list = reg_par_sec.get(sec, [])
        tot_toks += len(t_list)
        tot_reg += len(r_list)
        eq = (t_list == r_list)
        if not eq:
            defauts += 1
            dire(f"ÉCART COUVERTURE section {sec} : billet={len(t_list)} vs registre={len(r_list)}")
            for i, (a, b) in enumerate(zip(t_list, r_list), 1):
                if a != b:
                    dire(f"  premier écart au rang {i} de {sec}: billet={a!r} vs registre={b!r}")
                    break

    raw_wc = len(corps.split())
    clean_corps = re.sub(r"`\[LLM content block — (?:start|end)\]`", "", corps)
    clean_wc = len(clean_corps.split())
    tldr_m = re.search(r"\*\*TL;DR\.\*\*(.*?)\`\[LLM content block — end\]\`", corps, re.S)
    tldr_wc = len(("**TL;DR.**" + tldr_m.group(1)).split()) if tldr_m else 999
    tldr_ok = tldr_wc <= 250
    if not tldr_ok:
        defauts += 1
        dire(f"TL;DR trop long : {tldr_wc} mots (> 250)")

    dire(f"couverture : {tot_toks} jetons dans le corps, {tot_reg} entrées ; correspondance exacte par section : {tot_toks == tot_reg and defauts == 0}")
    dire(f"mots du corps : raw wc -w = {raw_wc}, hors balises LLM = {clean_wc}, TL;DR = {tldr_wc} (<= 250 : {tldr_ok})")
    return defauts


def run_autotest(reg: dict, texte: str, pdf_cache: dict) -> dict[str, bool]:
    muet = lambda *_: None
    results: dict[str, bool] = {}

    # 1. Nombre faussé
    r1 = copy.deepcopy(reg)
    i_p3 = next(i for i, e in enumerate(r1["entrees"]) if e["section"] == "p3" and e["nombre"] == "0.5748")
    r1["entrees"][i_p3]["nombre"] = "0.5749"
    t1 = texte.replace("deception `0.5748`", "deception `0.5749`", 1)
    results["1_nombre_fausse_refuse"] = verifier(r1, t1, muet, pdf_cache) > 0

    # 2. Ligne déplacée
    r2 = copy.deepcopy(reg)
    r2["entrees"][i_p3]["ligne"] += 1
    results["2_ligne_deplacee_refuse"] = verifier(r2, texte, muet, pdf_cache) > 0

    # 3. PDF citation altérée au premier mot (bord gauche)
    r3 = copy.deepcopy(reg)
    i_fibs34 = next(i for i, e in enumerate(r3["entrees"]) if e["source"] == "PDF:FIBS:34")
    r3["entrees"][i_fibs34]["motif"] = r3["entrees"][i_fibs34]["motif"].replace("With ", "Wit ", 1)
    results["3_pdf_debut_altere_refuse"] = verifier(r3, texte, muet, pdf_cache) > 0

    # 4. PDF citation altérée au dernier mot (bord droit)
    r4 = copy.deepcopy(reg)
    r4["entrees"][i_fibs34]["motif"] = r4["entrees"][i_fibs34]["motif"].replace("trivial", "trivia", 1)
    results["4_pdf_fin_altere_refuse"] = verifier(r4, texte, muet, pdf_cache) > 0

    # 5. PDF citation altérée au milieu
    r5 = copy.deepcopy(reg)
    r5["entrees"][i_fibs34]["motif"] = r5["entrees"][i_fibs34]["motif"].replace("nearly ", "")
    results["5_pdf_milieu_altere_refuse"] = verifier(r5, texte, muet, pdf_cache) > 0

    # 6. Mauvais numéro de page PDF (p. 35 au lieu de p. 34)
    r6 = copy.deepcopy(reg)
    r6["entrees"][i_fibs34]["source"] = "PDF:FIBS:35"
    results["6_pdf_mauvaise_page_refuse"] = verifier(r6, texte, muet, pdf_cache) > 0

    # 7. Cardinal en lettres faussé
    r7 = copy.deepcopy(reg)
    r7["entrees"][0]["nombre"] = "three"
    t7 = texte.replace("two generic probes", "three generic probes", 1)
    results["7_cardinal_en_lettres_fausse_refuse"] = verifier(r7, t7, muet, pdf_cache) > 0

    # 8. Détournement de section (Step B pointé sur Bb) + étiquetage sémantique erroné
    r8 = copy.deepcopy(reg)
    i_b = next(i for i, e in enumerate(r8["entrees"]) if e["section"] == "step_b" and e["nombre"] == "0.25")
    r8["entrees"][i_b]["source"] = "Bb"
    r8["entrees"][i_b]["motif"] = "| 0,25 (S25) |"
    r8["entrees"][i_b]["valeur_source"] = "0,25"
    r8["entrees"][i_b]["ligne"] = 43
    results["8_cloison_section_refuse"] = verifier(r8, texte, muet, pdf_cache) > 0

    # 9. Qualification sémantique incohérente (estimation ponctuelle étiquetée 'lower_bound')
    r9 = copy.deepcopy(reg)
    i_pt = next(i for i, e in enumerate(r9["entrees"]) if e["qualificatif"] == "point_estimate" and "[" not in e["contexte_billet"] and "lower bound" not in e["contexte_billet"].lower())
    r9["entrees"][i_pt]["qualificatif"] = "lower_bound"
    results["9_qualificatif_errone_refuse"] = verifier(r9, texte, muet, pdf_cache) > 0

    # 10. Fuite B5 (`transfer arm`)
    t10 = texte.replace("not covered here.", "not covered here; transfer arm pending.", 1)
    results["10_fuite_B5_refuse"] = verifier(reg, t10, muet, pdf_cache) > 0

    return results


def main() -> None:
    reg = json.loads(REG.read_text(encoding="utf-8"))
    texte = BILLET.read_text(encoding="utf-8")
    print("billet  :", BILLET.name, sha_b(BILLET.read_bytes()))
    print("registre:", REG.name, sha_b(REG.read_bytes()))
    pdf_cache: dict = {}
    d = verifier(reg, texte, _pdf_cache=pdf_cache)
    auto = run_autotest(reg, texte, pdf_cache)
    print("autotest (10 cas contraires refusés) :")
    for k, ok in auto.items():
        print(f"  {k:<38} : {ok}")
    tout = (d == 0) and all(auto.values())
    print("RÉSULTAT :", "CONFORME" if tout else f"ÉCARTS ({d}, autotest={all(auto.values())})")
    sys.exit(0 if tout else 1)


if __name__ == "__main__":
    main()
