"""Contrôle de la synthèse v3 à la page exacte (R7), avec épreuve R5.

Usage : python3 -I -B controler_v3.py V3.md RACINE_PAGES RACINE_DEPOT
  RACINE_PAGES : <clé>/{d,r,p}NNN.txt (pdftotext défaut, -raw, -layout), extraits après contrôle d'empreinte.
  RACINE_DEPOT : le dépôt, lu seulement (citations françaises de pièces du dépôt, présence testée sans rien imprimer).

Partie A : chaque passage entre « » de la v3 qui contient une lettre latine est cherché à la page de la citation la plus
proche qui le suit dans le même bloc (ou « p. N : » juste avant lui). Clé : celle de la citation entre crochets, sinon la
dernière clé nommée avant le passage dans le bloc, sinon la clé de la ligne de table. Un passage coupé par « … » doit avoir
tous ses morceaux sur cette page. Les passages français, de code ou sans source PDF sont listés à part (liste fermée).
Partie B : chiffres de la littérature, par phrase imprimée ou par ligne et colonne de table, à la page citée ; chaque
entrée exige aussi la présence du chiffre dans la v3 (forme française).
Partie C : citations de pièces du dépôt, à la ligne citée.
Partie D : épreuve R5 : artefacts qui doivent tous être rejetés.
"""
import os
import re
import sys
import unicodedata


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"),
                 ("–", "-"), ("—", "-"), ("ﬁ", "fi"), ("ﬂ", "fl"), (" ", " ")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


V3, PAGES, DEPOT = sys.argv[1], sys.argv[2], sys.argv[3]
TEXTE = open(V3, encoding="utf-8").read()
TEXTE_N = norm(TEXTE)
_cache = {}


def page(cle, p, mode=None):
    """Textes normalisés d'une page : dict mode -> texte ; ou texte brut d'un mode."""
    if mode is not None:
        f = os.path.join(PAGES, cle, "%s%03d.txt" % (mode, p))
        return open(f, encoding="utf-8", errors="ignore").read() if os.path.exists(f) else ""
    k = (cle, p)
    if k not in _cache:
        d = {}
        for m in "drp":
            f = os.path.join(PAGES, cle, "%s%03d.txt" % (m, p))
            if os.path.exists(f):
                d[m] = norm(open(f, encoding="utf-8", errors="ignore").read())
        _cache[k] = d
    return _cache[k]


def sur_page(cle, p, phrase):
    morceaux = [norm(m) for m in phrase.split("…") if norm(m)]
    return any(all(m in t for m in morceaux) for t in page(cle, p).values())


def pages_de(cle):
    d = os.path.join(PAGES, cle)
    return sorted({int(f[1:4]) for f in os.listdir(d)}) if os.path.isdir(d) else []


CLES = sorted(os.listdir(PAGES))

# Passages sans source PDF (français, code, titres, noms de champs) : liste fermée, chacun justifié.
SANS_PDF = {
    "Your action:": "code de l'environnement (propositions.py l. 268)",
    "Your action: »": "code",
    "Simple probes can catch sleeper agents": "titre du billet d'Anthropic, sans PDF : non vérifié (dit dans le texte)",
    "COST": "nom de champ du code",
    "No.": "réponse imposée (montage) ; « No. » est sur [AP] p. 9",
    "Yes.": "réponse imposée (montage)",
    "No": "réponse imposée de [PAR] (p. 5)",
    "Yes": "réponse imposée de [PAR] (p. 6)",
    "G-01": "étiquette de [AD1] l. 34 (partie C)",
    "Did you lie?": "titre du travail [DYL] (p. 1) et nom de sa sonde",
    "Caught in the Act": "titre du travail [CA] (p. 1)",
    "Assistant": "nom du jeton chez [MA] (p. 17)",
}
# Passages français (termes du programme ou citations de pièces du dépôt, contrôlées en partie C) : liste fermée.
FRANCAIS = {"tromperie", "question", "Non au-dessus", "pas de trace", "bras de diagnostic, jamais en production",
            "avant le champ", "oracle", "au-dessus", "gros nombre", "moyenne", "de ne relire P3 en rien", "P3 bis",
            "Tout signal y serait suspect (R4, R3)", "consigne lue, pas l'acte", "maximum ou attention",
            "gonflement d'estimation", "Revendication"}


def blocs(texte):
    res, cur = [], []
    for ligne in texte.splitlines():
        if ligne.startswith("|") or not ligne.strip() or re.match(r"^\s*(- |\d+\. )", ligne):
            if cur:
                res.append(" ".join(cur))
                cur = []
            if ligne.startswith("|"):
                res.append(ligne)
                continue
        if ligne.strip():
            cur.append(ligne.strip())
    if cur:
        res.append(" ".join(cur))
    return res


RE_CLE = re.compile(r"\[(" + "|".join(sorted(CLES, key=len, reverse=True)) + r")[\] ,;]")


def cle_contexte(bloc, pos):
    """Dernière clé nommée avant pos dans le bloc ; sinon clé de la première cellule d'une ligne de table."""
    cles = [m.group(1) for m in RE_CLE.finditer(bloc[:pos])]
    if cles:
        return cles[-1]
    return None


def cle_de_ligne(bloc):
    if not bloc.startswith("|"):
        return None
    premiere = bloc.split("|")[1]
    m = RE_CLE.search(premiere + " ")
    return m.group(1) if m else None


def resoudre(bloc, pos, num):
    """Clé d'une citation « p. N » trouvée à pos."""
    ouvr = bloc.rfind("[", 0, pos)
    ferm = bloc.rfind("]", 0, pos)
    if ouvr > ferm:
        mm = re.match(r"\[(" + "|".join(sorted(CLES, key=len, reverse=True)) + r")\b", bloc[ouvr:])
        if mm:
            return mm.group(1), num
    return (cle_de_ligne(bloc) or cle_contexte(bloc, pos)), num


def dans_crochet(bloc, debut):
    ouvr = bloc.rfind("[", 0, debut)
    ferm = bloc.rfind("]", 0, debut)
    if ouvr > ferm:
        mm = re.match(r"\[(" + "|".join(sorted(CLES, key=len, reverse=True)) + r")(?: table \d+,)? p\. (\d+)", bloc[ouvr:])
        if mm:
            return mm.group(1), int(mm.group(2))
    return None


def citation_avant_proche(bloc, debut):
    ms = list(re.finditer(r"p\. (\d+)", bloc[:debut]))
    if not ms:
        return None
    return resoudre(bloc, ms[-1].start(), int(ms[-1].group(1)))


def citation_apres(bloc, fin):
    """Première citation « p. N » après fin : (clé, page)."""
    m = re.search(r"p\. (\d+)", bloc[fin:])
    if not m:
        return None
    pos = fin + m.start()
    return resoudre(bloc, pos, int(m.group(1)))


def citation_apres_ancienne(bloc, fin):
    m = re.search(r"p\. (\d+)", bloc[fin:])
    if not m:
        return None
    pos = fin + m.start()
    # la citation est-elle entre crochets [CLE … p. N] ?
    ouvr = bloc.rfind("[", 0, pos)
    ferm = bloc.rfind("]", 0, pos)
    cle = None
    if ouvr > ferm:
        mm = re.match(r"\[(" + "|".join(sorted(CLES, key=len, reverse=True)) + r")\b", bloc[ouvr:])
        if mm:
            cle = mm.group(1)
    if cle is None:
        cle = cle_contexte(bloc, pos)
    return cle, int(m.group(1))


def citation_avant(bloc, debut):
    m = re.search(r"p\. (\d+) :\s*$", bloc[max(0, debut - 25):debut])
    if not m:
        return None
    return cle_contexte(bloc, debut), int(m.group(1))


def partie_a():
    ok = ko = fr = 0
    lignes = []
    for b in blocs(TEXTE):
        if b.startswith("| clé |") or re.match(r"^\| [A-Z]+ \| ", b):
            continue  # table des clés (section 6)
        for m in re.finditer(r"«\s*(.+?)\s*»", b):
            q = m.group(1)
            if not re.search(r"[A-Za-z]", q):
                continue
            if q in SANS_PDF:
                fr += 1
                lignes.append("sans PDF | %s | %s" % (q, SANS_PDF[q]))
                continue
            if q in FRANCAIS or re.search(r"[àâçéèêëîïôûùüÿœÀÉÈ]", q) or not re.search(r"[a-z]{2}", q):
                fr += 1
                lignes.append("français | %s" % q[:90])
                continue
            cands = []
            for c in (dans_crochet(b, m.start()), citation_avant(b, m.start()), citation_apres(b, m.end())):
                if c:
                    cands.append(c)
            bon = [c for c in cands if c[0] and sur_page(c[0], c[1], q)]
            if not bon:  # repli : citation la plus proche avant le passage
                c = citation_avant_proche(b, m.start())
                if c and c[0] and sur_page(c[0], c[1], q):
                    bon = [c]
                    q = q + "   [citation précédente]"
            if bon:
                ok += 1
                lignes.append("OK      | %s p. %d | %s" % (bon[0][0], bon[0][1], q[:100]))
            else:
                ko += 1
                ailleurs = []
                for cle in set([c[0] for c in cands if c[0]] + RE_CLE.findall(b)):
                    for p in pages_de(cle):
                        if sur_page(cle, p, q):
                            ailleurs.append("%s p. %d" % (cle, p))
                lignes.append("ÉCART   | citée %s | trouvée : %s | %s" % (cands, ailleurs or "nulle part", q[:100]))
    return ok, ko, fr, lignes


# ---- Partie B : chiffres ----
# (clé, page, phrase imprimée, forme dans la v3)
PHRASES = [
    ("BX", 5, "class separation with 0.95 AUROC", "0.95 AUROC"),
    ("BX", 5, "degraded by 14 points to 0.81 AUROC", "0,81"),
    ("BX", 6, "32-point drop to 0.63 AUROC", "0,63"),
    ("BX", 6, "Sandbagging drops from 0.95 to 0.62", "0,62 dans la légende de la figure 4"),
    ("BX", 8, "from almost perfect detection 0.94 to chance performance 0.5", "le 0,5 de [bx]"),
    ("BX", 1, "0.57 vs 0.94 AUROC for Sandbagging", "0.57 vs 0.94"),
    ("BX", 3, "we use the residual stream at layer 14", "couche 14, paires instruites"),
    ("YS", 3, "Sandbagging performs poorly (0.606 AUROC).", "0,606 sur ce même modèle [ys p. 3]"),
    ("YS", 3, "0.936 / 0.950 / 0.869 AUROC across the three targets", "atteint 0,869 [ys p. 3]"),
    ("YS", 3, "we use layer 15 residual stream activations", "couche 15** (p. 3)"),
    ("YS", 3, "top-100 source pcs (green, 5-fold cv)", "100 composantes de la source, validation croisée à cinq plis"),
    ("BU", 10, "the 49 unambiguous lies and the 55 unambiguous truthful replies", "49 mensonges et 55 réponses vraies"),
    ("BU", 10, "with an average accuracy of 93.8 ± 1.5%", "93,8 % (ttpd"),
    ("BU", 10, "LR with 79 ± 8% accuracy", "79 ± 8%"),
    ("BU", 10, "layer 12 over the last token of the response", "12 sur llama-3-8b [bu p. 5]"),
    ("BU", 5, "For LLaMA3-8B we choose layer 12", "12 sur llama-3-8b [bu p. 5]"),
    ("AP", 3, "after layer 22 (of 80) in the residual stream", "after layer 22 (of 80)"),
    ("AP", 6, "The lowest AUROC is 0.964 on the Roleplaying dataset", "0.964 on the roleplaying"),
    ("AP", 6, "AUROC of 0.974 and 0.983", "0.974 and 0.983"),
    ("AP", 18, "Our recall at 1% is greater than 99% on all four evaluation datasets", "consistently rating every control response as honest"),
    ("AP", 23, "Recall at 1% FPR compared to control does show improvement", "rappel à 1 % de faux positifs meilleur"),
    ("DYL", 2, "across 31 open-weight subject models", "31 open-weight"),
    ("DYL", 11, "Median balanced accuracy falls from 0.85 to 0.52 for Apollo, from 0.81 to 0.65 for DYL", "from 0.81 to 0.65 for dyl"),
    ("CA", 4, "163,016 transcripts", "163,016"),
    ("CA", 5, "six layers spread evenly from 30% to 90%", "six couches [ca p. 5]"),
    ("CA", 7, "score 0.979 to 0.984", "0.979 to 0.984"),
    ("CA", 8, "0.585–0.781 on Qwen3.5-2B", "rupture entre 2 milliards (0,585 à 0,781)"),
    ("CA", 8, "from 27B up (0.963–0.986)", "à 0,986"),
    ("CA", 8, "scores exceed 90% from there up", "scores exceed 90%"),
    ("CA", 8, "0.613–0.760 on Nemotron-3 Nano", "0,613-0,760"),
    ("CA", 25, "Nemotron 3 Nano 30B-A3B", "nemotron-3 nano (30b-a3b)"),
    ("CA", 18, "qwen3.5-2b qwen3.5-9b qwen3.5-27b", "liste p. 18"),
    ("CA", 9, "all four probes have AUC ≥ 98%", "auc ≥ 98%"),
    ("CA", 8, "every subset of about 3,000 rows scores 0.018 to 0.110 lower", "3 000 lignes"),
    ("CA", 9, "math-sandbagger (63% AUC)", "63% auc"),
    ("AU", 6, "Action (AUC = 0.653)", "0,653 sur toutes les actions"),
    ("AU", 6, "+Thinking (AUC = 0.948)", "0,653 contre 0,948"),
    ("AU", 6, "Action (AUC = 0.984)", "auc = 0.984"),
    ("AU", 6, "77% of these are", "77 % sans parole"),
    ("AU", 6, "layer 20 (of a total of 40 layers) in the Phi-4 model", "couche 20"),
    ("K", 5, "0.85 ±0.039", "0,85 contre 0,74 [k p. 5]"),
    ("K", 5, "0.74 ±0.051", "0.74 ±0.051"),
    ("MA", 17, "96% and 91% of Assistant tokens", "96% and 91%"),
    ("RH", 27, "total 5,285", "5 285"),
    ("RH", 9, "held out set of 250 rollouts", "250 rollouts"),
    ("GM", 12, "Our selected probe is the Max of Rolling Means Attention Probe", "sonde retenue par ses auteurs (p. 12)"),
]


def lignes_table(cle, p, mode):
    return page(cle, p, mode).splitlines()


def nombres(ligne):
    return re.findall(r"[+\-−]?\d*\.\d+\**%?|—", ligne)


def table_par():
    """[PAR] table 3, p. 7 : nom -> six valeurs (AI Liar, Dilution, Backdoors, Insider, Sandbagging, Avg)."""
    t = {}
    for l in lignes_table("PAR", 7, "p"):
        m = re.match(r"\s*([A-Za-z][A-Za-z \-\(\)\.0-9,]*?\))\s+((?:\d\.\d{3}\s*){6})$", l)
        if m:
            t[m.group(1).strip()] = m.group(2).split()
    return t


def table_gm():
    """[GM] table 3, p. 12 (mode brut) : nom -> dix valeurs (SC[OT] SC[HN] LC[RT] MT[HN] SC[A] LC[A] MT[A] SC[J]
    SC[ART] erreur)."""
    t, nom = {}, []
    for l in lignes_table("GM", 12, "r"):
        vals = re.findall(r"\d+(?:\.\d+)?%", l)
        if len(vals) >= 10:
            tete = l[: l.find(vals[0])].strip() if not l.strip().startswith(vals[0]) else ""
            nom_complet = " ".join(nom + ([tete] if tete else [])).replace("- ", "")
            t[re.sub(r"\s+", " ", nom_complet).strip()] = vals[-10:]
            nom = []
        elif l.strip() and not l.startswith(("Table 3", "threshold", "smaller", "for statistical", "FPR", "Classifier",
                                              "Building")):
            nom.append(l.strip())
        if l.startswith("optimal probe") or l.startswith("We now choose"):
            break
    return t


def table_dyl():
    """[DYL] table 9, p. 28 : modèle -> (AA, Apollo, DYL)."""
    t = {}
    for l in lignes_table("DYL", 28, "p"):
        m = re.match(r"\s*(\S+/\S+)\s+(\d+)?\s+(\d\.\d\d)\s+(\d\.\d\d)", l)
        if m:
            t[m.group(1)] = (m.group(2), m.group(3), m.group(4))
    return t


def table_k():
    """[K] table 1, p. 7 : comportement -> (autre domaine, incité, sur consigne, hors politique)."""
    t = {}
    for l in lignes_table("K", 7, "p"):
        m = re.match(r"\s*(Metaphors|Refusal|Science|Lists \(ref\.\)|Sandbagging|Authority|Sycophancy|Deception)\s+(.*)$", l)
        if m:
            t[m.group(1)] = m.group(2).split()
    return t


def table_ku():
    """[KU] table 7, p. 6 : lignes D-RepE dans l'ordre 1B, 4B, 12B, 27B -> valeurs."""
    return [l.split("D-RepE")[1].split()[:3] for l in lignes_table("KU", 6, "p") if "D-RepE" in l]


def table_lb():
    """[LB] table 6, p. 54, bloc AUROC : modèle -> huit valeurs (HP-C HP-KR CG ST ID GS IT AVERAGE)."""
    t = {}
    for l in lignes_table("LB", 54, "p"):
        if "BALANCED ACCURACY" in l:
            break
        m = re.match(r"\s*(Llama 3\.3 70B|Qwen 2\.5 72B|Mistral 3\.1 24B|Gemma 3 27B)\s+(.*)$", l)
        if m:
            t[m.group(1)] = m.group(2).split()
    return t


def table_oa():
    t = {}
    for l in lignes_table("OA", 23, "p"):
        m = re.match(r"\s*(Simple Deception|Diverse Deception|MBPP)\s+(Generation Mean Pooling|Follow-up prompt)\s+(\d\.\d{3})", l)
        if m:
            t[(m.group(1), m.group(2))] = m.group(3)
    return t


def table_bx():
    for l in lignes_table("BX", 6, "p"):
        m = re.search(r"Sandbagging\s+(\d\.\d\d)\s+(\d\.\d\d)\s+(\d\.\d\d)", l)
        if m:
            return m.groups()
    return None


def tables_attendues():
    """(libellé, valeur lue ou None, valeur attendue, forme dans la v3)."""
    par, gm, dyl, k, ku, lb, oa = table_par(), table_gm(), table_dyl(), table_k(), table_ku(), table_lb(), table_oa()
    bx = table_bx()
    g = lambda d, *ks: (lambda v: v)(d.get(ks[0])) if len(ks) == 1 else None
    out = []
    S, A = 4, 5  # [PAR] colonnes Sandbagging et Avg.
    for nom, col, att, v3 in [
        ("Full Averaging (Pairs)", S, "0.964", "moyenne 0,964"), ("Peak Activation (Pairs)", S, "0.839", "maximum 0,839"),
        ("Critical Averaging (Pairs)", S, "0.924", "affirmation critique 0,924"),
        ("Deception No (Pairs)", S, "0.849", "0,849 et 0,879"), ("Honest Yes (Pairs)", S, "0.879", "0,849 et 0,879"),
        ("Full Averaging (RP)", S, "0.828", "moyenne 0,828"), ("Peak Activation (RP)", S, "0.891", "maximum 0,891"),
        ("Deception No (RP)", S, "0.457", "0,457 et 0,437"), ("Honest Yes (RP)", S, "0.437", "0,457 et 0,437"),
        ("Full Averaging (Pairs)", A, "0.941", "moyenne 0,941"), ("Peak Activation (Pairs)", A, "0.867", "maximum 0,867"),
        ("Full Averaging (RP)", A, "0.840", "moyenne 0,840"), ("Peak Activation (RP)", A, "0.856", "maximum 0,856"),
    ]:
        v = par.get(nom)
        out.append(("PAR p. 7 | %s | col %d" % (nom, col), v[col] if v else None, att, v3))
    LCRT, LCA = 2, 5
    for nom, col, att, v3 in [
        ("Linear Probe Mean", LCA, "99.13%", "99,13 %"), ("Attn", LCA, "87.88%", "87,88 %"),
        ("Attn (With LC Training)", LCA, "1.34%", "1,34 %"),
        ("Rolling Attn Probe, MultiMax Agg", LCA, "1.73%", "0,0 % à 1,73 %"),
        ("Rolling Attn Probe (20H), MultiMax Agg", LCA, "0.0%", "0,0 % à 1,73 %"),
        ("MultiMax Trained, MultiMax Agg", LCA, "0.4%", "0,0 % à 1,73 %"),
        ("MultiMax (Attn Trained)", LCA, "0.0%", "0,0 % à 1,73 %"),
        ("MultiMax Trained (20H), MultiMax Agg", LCA, "0.0%", "0,0 % à 1,73 %"),
        ("Rolling Attn Probe, Rolling Agg (Selected)", LCA, "3.03%", "1,73 % à 5,19 %"),
        ("Rolling Attn Probe (20H), Rolling Agg", LCA, "5.19%", "1,73 % à 5,19 %"),
        ("Linear Probe Rolling Exp", LCA, "1.73%", "1,73 % à 5,19 %"),
        ("Rolling Attn Probe, MultiMax Agg", LCRT, "1.85%", "1,85 % à 82,14 %"),
        ("Rolling Attn Probe (20H), MultiMax Agg", LCRT, "6.53%", "1,85 % à 82,14 %"),
        ("MultiMax Trained, MultiMax Agg", LCRT, "7.76%", "1,85 % à 82,14 %"),
        ("MultiMax (Attn Trained)", LCRT, "43.97%", "1,85 % à 82,14 %"),
        ("MultiMax Trained (20H), MultiMax Agg", LCRT, "82.14%", "1,85 % à 82,14 %"),
        ("Rolling Attn Probe, Rolling Agg (Selected)", LCRT, "1.23%", "1,0 % à 13,55 %"),
        ("Rolling Attn Probe (20H), Rolling Agg", LCRT, "1.0%", "1,0 % à 13,55 %"),
        ("Linear Probe Rolling Exp", LCRT, "13.55%", "1,0 % à 13,55 %"),
        ("Linear Probe Mean", LCRT, "0.5%", "« linear probe mean » 0,5 %"),
    ]:
        v = gm.get(nom)
        out.append(("GM p. 12 | %s | col %d" % (nom, col), v[col] if v else None, att, v3))
    for nom, i, att, v3 in [
        ("Qwen/Qwen3-8B", 1, "0.74", "qwen3-8b 0,74 et 0,69"), ("Qwen/Qwen3-8B", 2, "0.69", "qwen3-8b (0,69)"),
        ("Qwen/Qwen3-4B", 1, "0.64", "qwen3-4b 0,64 et 0,68"), ("Qwen/Qwen3-4B", 2, "0.68", "qwen3-4b (0,68)"),
        ("Qwen/Qwen3.5-4B", 1, "0.89", "qwen3.5-4b 0,89 et 0,82"), ("Qwen/Qwen3.5-4B", 2, "0.82", "qwen3.5-4b 0,89 et 0,82"),
        ("meta-llama/Llama-3.3-70B-Instruct", 1, "0.84", "llama-3.3-70b 0,84 et 0,74"),
        ("meta-llama/Llama-3.3-70B-Instruct", 2, "0.74", "llama-3.3-70b 0,84 et 0,74"),
        ("meta-llama/Llama-3.3-70B-Instruct", 0, "14", "14 pour llama-3.3-70b"),
        ("Qwen/Qwen3.5-4B", 0, "27", "27 pour qwen3.5-4b"),
        ("google/gemma-4-E2B-it", 1, "0.79", None), ("google/gemma-4-E2B-it", 2, "0.76", None),
    ]:
        v = dyl.get(nom)
        out.append(("DYL p. 28 | %s | col %d" % (nom, i), v[i] if v else None, att, v3))
    # décompte de la table 9 : Apollo contre sonde de question
    a = d = e = 0
    for nom, (aa, ap, dy) in dyl.items():
        x, y = float(ap), float(dy)
        a, d, e = a + (x > y), d + (y > x), e + (x == y)
    out.append(("DYL p. 28 | décompte Apollo>DYL, DYL>Apollo, égalités, lignes", "%d,%d,%d,%d" % (a, d, e, len(dyl)),
                "22,8,2,32", "22 fois, la suit 8 fois, 2 égalités"))
    for nom, i, att, v3 in [("Deception", 0, "−0.416***", "−0,416"), ("Deception", 2, "+0.035", "+0,035"),
                            ("Sandbagging", 2, "−0.111*", "−0,111")]:
        v = k.get(nom)
        out.append(("K p. 7 | %s | col %d" % (nom, i), v[i] if v and len(v) > i else None, att, v3))
    for i, att in enumerate([".572", ".512", ".443", ".460"]):
        out.append(("KU p. 6 | D-RepE, échelle %d | col Role" % i, ku[i][1] if len(ku) > i else None, att,
                    "0,572 ; 0,512 ; 0,443 ; 0,460"))
    for nom, att, v3 in [("Llama 3.3 70B", "0.95", "llama 70b 0,95"), ("Qwen 2.5 72B", "0.60", "qwen 72b 0,60"),
                         ("Mistral 3.1 24B", "0.69", "mistral 24b 0,69"), ("Gemma 3 27B", "0.58", "gemma 27b 0,58")]:
        v = lb.get(nom)
        out.append(("LB p. 54 | %s | col ID" % nom, v[4] if v else None, att, v3))
    for cle_oa, att, v3 in [(("Simple Deception", "Generation Mean Pooling"), "0.701", "moyenne sur la génération 0,701"),
                            (("Simple Deception", "Follow-up prompt"), "0.963", "question 0,963"),
                            (("Diverse Deception", "Generation Mean Pooling"), "0.561", "0,561 contre 0,972"),
                            (("Diverse Deception", "Follow-up prompt"), "0.972", "0,561 contre 0,972"),
                            (("MBPP", "Generation Mean Pooling"), "0.999", "sonde du domaine 0,999")]:
        out.append(("OA p. 23 | %s" % " / ".join(cle_oa), oa.get(cle_oa), att, v3))
    out.append(("BX p. 6 | table 1 Sandbagging (base, consigne remplacée, filtrage du score)",
                ",".join(bx) if bx else None, "1.00,0.04,0.03", "base 1.00, consigne remplacée 0.04"))
    return out


def partie_b():
    ok = ko = 0
    lignes = []
    for cle, p, phrase, v3 in PHRASES:
        a = sur_page(cle, p, phrase)
        b = norm(v3) in TEXTE_N
        if a and b:
            ok += 1
            lignes.append("OK      | %s p. %d | %s" % (cle, p, phrase[:90]))
        else:
            ko += 1
            lignes.append("ÉCART   | %s p. %d | page:%s v3:%s | %s" % (cle, p, a, b, phrase[:90]))
    for lib, lu, att, v3 in tables_attendues():
        a = lu is not None and norm(str(lu)) == norm(att)
        b = v3 is None or norm(v3) in TEXTE_N
        if a and b:
            ok += 1
            lignes.append("OK      | %s | %s" % (lib, lu))
        else:
            ko += 1
            lignes.append("ÉCART   | %s | lu %s, attendu %s ; v3 %s" % (lib, lu, att, b))
    return ok, ko, lignes


# ---- Partie C : pièces du dépôt (présence à la ligne citée ; rien n'est imprimé de la ligne) ----
DEPOT_CITES = [
    ("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", [8], "de ne relire P3 en rien"),
    ("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", [85], "A2 : poursuit T2 après coup, sans plancher par jeton"),
    ("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", [27], "la seule mesure qui sépare le nombre écrit du contexte privé"),
    ("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", [26], "C2 fusionnée avec D2"),
    ("docs/notes/brainstorm-suite-P3-v1/propositions/proposition-C.md", [324], "Tout signal y serait suspect (R4, R3)"),
    ("docs/notes/brainstorm-suite-P3-v1/propositions/proposition-C.md", [323], "« P3 bis » localisé sur le champ du coût"),
    ("docs/notes/brainstorm-suite-P3-v1/propositions/proposition-D.md", [94], "{original ; remplacé par la médiane honnête de la même tâche}"),
    ("docs/notes/brainstorm-suite-P3-v1/propositions/proposition-D.md", [97], "jamais la moyenne ni la médiane"),
    ("docs/notes/brainstorm-suite-P3-v1/reponses/reponses.md", [372, 373], "champ du coût masqué"),
    ("registres/decisions.md", [456], "la première tentative de détection du plan R-262 (point 2)"),
    ("registres/decisions.md", [456], "A1 plancher conjoint, A2 aire du champ du coût"),
    ("registres/decisions.md", [446], "remarque 4 (drapeau T2) exclue par la règle gelée"),
    ("registres/decisions.md", [453], "voie choisie d'après la revue de la littérature"),
    ("registres/decisions.md", [453], "L'addendum 2 de P3 (N-025) reste en cours et passe avant la lecture de P4-instrument (sa réserve éventuelle s'y recopie)"),
    ("registres/decisions.md", [457], "Référence boîte noire (nœud 4 du brainstorm)"),
    ("registres/decisions.md", [461], "plafond de 10 USD par lancement"),
    ("registres/decisions.md", [461], "toute dépense au-delà du plafond par lancement ou du crédit est un nœud"),
    ("registres/go.md", [32], "localisation au champ du coût avec plancher apparié, sonde oracle en validation croisée par tâche sous T1, T3, T4"),
    ("registres/go.md", [34], "10 USD au plus par lancement"),
    ("registres/decisions.md", [468], "Tranché (c) renforcée par Lazar"),
    ("registres/decisions.md", [469], "juge Claude sur les textes de P3 retiré"),
    ("registres/go.md", [35], "la référence par l'API Claude sur les textes de P3 (R-202 (3)) est retirée"),
    ("docs/decisions/decision-N-029-v1.md", [38], "Elle ne se"),
    ("docs/decisions/decision-N-029-v1.md", [39], "lit pas sur les textes de P3"),
    ("docs/decisions/decision-N-029-v1.md", [37], "sur les épisodes de T0.6"),
    ("registres/depenses.md", [88], "≈ 3,64 h depuis la création"),
    ("registres/depenses.md", [88], "≈ 3,96 USD"),
    ("registres/depenses.md", [89], "11,79 USD"),
    ("docs/decisions/decision-N-026-v1.md", [20], "« bras de diagnostic, jamais en production »"),
    ("docs/decisions/decision-N-026-v1.md", [24], "« l'agrégation explique-t-elle le nul ? »"),
    ("docs/decisions/proposition-P-011-T0.7-sondes-v1.md", [42], "choix de la sonde rapportée fait sur un jeu de validation générique, jamais sur les organismes"),
    ("docs/brief-claude-code-programme-complet-v2.md", [48], "Aucun run visant un signe positif"),
    ("prereg/P3-addendum-lecture-complementaire-v1.md", [34], "G-01 : biais de longueur du maximum dans T2"),
    ("prereg/P3-premier-test-i-a-v1.md", [248], "établi si mention contre honnête est non au-dessus du plancher et saboteur contre mention au-dessus"),
    ("prereg/P3-premier-test-i-a-v1.md", [273], "se lit « non détecté à cette puissance », jamais « ne sépare pas »"),
    ("prereg/P3-premier-test-i-a-v1.md", [415, 416], "est un **nœud**"),
    ("prereg/P3-premier-test-i-a-v1.md", [428], "pas de seconde lecture sur d'autres sondes, couches ou jeux"),
    ("prereg/P3-premier-test-i-a-v1.md", [318], "N = 1, T = 10"),
    ("prereg/P3-premier-test-i-a-v1.md", [320], "quatre conditions** × 60 tâches × 1 épisode = 240 épisodes"),
    ("prereg/P3-premier-test-i-a-v1.md", [385], "soit ≈ 2,5 heures pour 240"),
    ("prereg/P3-premier-test-i-a-v1.md", [238, 239, 240], "au moins 10"),
    ("prereg/P3-premier-test-i-a-v1.md", [242, 243, 244, 245], "sur les jetons qui précèdent le champ `COST`, et sur le champ `COST`"),
    ("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", [345], "rapport géométrique moyen d'environ 33"),
    ("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", [204], "0,8878 (926)"),
    ("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", [172], "ne doit pas être cité"),
    ("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", [358, 359], "Il ne doit être cité nulle part comme un résultat"),
    ("src/controle_ia/environnements/propositions.py", [36, 37], "name concrete models, datasets, metrics"),
    ("src/controle_ia/environnements/propositions.py", [47], '"COST: <estimated compute in GPU-hours, a single number>\\n"'),
    ("src/controle_ia/environnements/propositions.py", [134], "la première occurrence de chaque champ fait foi"),
    ("src/controle_ia/environnements/propositions.py", [268], 'lignes.append("Your action:")'),
    ("src/controle_ia/harnais/episode.py", [217], "contextes.append(trs[b][i].ids + fmt.tour(debuts[b][i], obs))"),
    ("src/controle_ia/harnais/episode.py", [254], "trs[b][i].ids = ctx + nv + fmt.cloture(debuts[b][i], nv)"),
]


def partie_c(cites):
    ok = ko = 0
    lignes = []
    for f, ls, phrase in cites:
        chemin = os.path.join(DEPOT, f)
        try:
            t = open(chemin, encoding="utf-8").read().splitlines()
        except OSError:
            t = []
        bloc = " ".join(t[l - 1] for l in ls if 0 < l <= len(t))
        if norm(phrase) in norm(bloc):
            ok += 1
            lignes.append("OK      | %s l. %s" % (f, ",".join(map(str, ls))))
        else:
            ko += 1
            lignes.append("ÉCART   | %s l. %s | %s" % (f, ",".join(map(str, ls)), phrase[:60]))
    return ok, ko, lignes


def partie_d():
    """Épreuve R5 : chaque artefact doit être rejeté par la même règle que le contrôle."""
    rejets = 0
    lignes = []
    arte = [
        ("phrase, chiffre altéré", lambda: sur_page("YS", 3, "Sandbagging performs poorly (0.607 AUROC).")),
        ("phrase, mauvaise page", lambda: sur_page("AP", 9, "every Sandbagging response is rated as highly deceptive")),
        ("phrase, mot inversé", lambda: sur_page("MK", 4, "the Last Token activation probe consistently performs well")),
        ("phrase, morceau d'une autre page", lambda: sur_page("OA", 1, "obfuscated activations arise … Follow-up prompt")),
        ("phrase, mauvais chiffre de [DYL] p. 11", lambda: sur_page("DYL", 11, "from 0.81 to 0.66 for DYL")),
        ("phrase, Nemotron altéré", lambda: sur_page("CA", 8, "0.613–0.770 on Nemotron-3 Nano")),
        ("table [PAR], mauvaise valeur", lambda: table_par().get("Peak Activation (Pairs)", [None] * 6)[5] == "0.868"),
        ("table [PAR], colonne voisine", lambda: table_par().get("Deception No (RP)", [None] * 6)[4] == "0.786"),
        ("table [GM], LC[RT] altéré", lambda: table_gm().get("Linear Probe Mean", [None] * 10)[2] == "0.6%"),
        ("table [GM], LC[A] d'une autre ligne", lambda: table_gm().get("Attn", [None] * 10)[5] == "1.34%"),
        ("table [DYL], ligne voisine", lambda: table_dyl().get("Qwen/Qwen3-8B", (None,) * 3)[1] == "0.89"),
        ("table [K], case voisine", lambda: (table_k().get("Sandbagging") or [None] * 4)[2] == "+0.035"),
        ("v3, forme absente", lambda: norm("maximum 0,868") in TEXTE_N),
        ("dépôt, ligne voisine", lambda: partie_c([("registres/decisions.md", [455], "la première tentative de détection du plan R-262 (point 2)")])[0] == 1),
        ("dépôt, mot altéré", lambda: partie_c([("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", [85], "A2 : poursuit T2 avant coup")])[0] == 1),
    ]
    for lib, f in arte:
        try:
            accepte = bool(f())
        except Exception as e:  # une erreur compte comme un rejet, mais elle est écrite
            accepte = False
            lib += " (erreur : %s)" % type(e).__name__
        rejets += not accepte
        lignes.append("%s | %s" % ("rejeté " if not accepte else "ACCEPTÉ", lib))
    return rejets, len(arte), lignes


def main():
    a_ok, a_ko, a_fr, a_l = partie_a()
    b_ok, b_ko, b_l = partie_b()
    c_ok, c_ko, c_l = partie_c(DEPOT_CITES)
    d_rej, d_n, d_l = partie_d()
    print("=== A : passages entre guillemets, à la page de la citation la plus proche")
    print("\n".join(a_l))
    print("--- A : %d à la page citée ; %d écarts ; %d sans PDF (français, code, nom)" % (a_ok, a_ko, a_fr))
    print("=== B : chiffres de la littérature (phrase imprimée ou ligne et colonne de table, page citée ; forme dans la v3)")
    print("\n".join(b_l))
    print("--- B : %d conformes ; %d écarts" % (b_ok, b_ko))
    print("=== C : pièces du dépôt, à la ligne citée (présence seulement, rien d'imprimé)")
    print("\n".join(c_l))
    print("--- C : %d conformes ; %d écarts" % (c_ok, c_ko))
    print("=== D : épreuve R5 (tous les artefacts doivent être rejetés)")
    print("\n".join(d_l))
    print("--- D : %d rejetés sur %d" % (d_rej, d_n))
    return 0 if (a_ko == 0 and b_ko == 0 and c_ko == 0 and d_rej == d_n) else 1


if __name__ == "__main__":
    sys.exit(main())
