# Vérification par programme des nombres des sections des étapes B et B bis contre les verdicts cités.
# Usage : python3 -I verif.py RACINE_DU_DEPOT
import sys, re, hashlib, os
R = sys.argv[1]
D = os.path.join(R, "docs/notes/billet-nul-avec-controle-positif-v1/sections-etapes-b-v1")
P_SEC = os.path.join(D, "sections-etape-b-et-b-bis-en-v1.md")
P_TAB = os.path.join(D, "table-des-nombres-v1.md")
V = {"B": os.path.join(R, "docs/verdicts/verdict-T0.7-etape-B-v1.md"),
     "Bb": os.path.join(R, "docs/verdicts/verdict-T0.7-etape-B-bis-v1.md")}
H = {"B": "077ab789b36f2a4e9b0b99a3dcc7cacbbea240406cba38584670a40cd4a5c62f",
     "Bb": "1561399a11855f4921dc8fcb4be72755d2b39f5ff9b6362301b33aba0e0301f3"}
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
print("== 1. empreintes")
for k in V:
    print(k, sha(V[k]) == H[k], sha(V[k]))
for p in (P_SEC, P_TAB):
    comp = open(p + ".sha256").read().split()[0]
    print(os.path.basename(p), sha(p) == comp, sha(p))
L = {k: open(V[k], encoding="utf-8").read().split("\n") for k in V}

NUM = re.compile(r"(?<![\w.,])[-−]?\d+(?:[   ]\d{3})*(?:[.,]\d+)?(?![\w])")
def nombres(txt):
    """Nombres d'un texte de verdict : décimales à point ou à virgule, milliers à espace."""
    out = []
    for m in NUM.finditer(txt):
        t = m.group(0).replace("−", "-").replace(" ", "").replace(" ", "")
        t = re.sub(r"(?<=\d) (?=\d{3})", "", t)
        t = t.replace(",", ".")
        try: out.append(float(t))
        except ValueError: pass
    return out
MOTS_FR = {"un":1,"une":1,"deux":2,"trois":3,"quatre":4,"cinq":5,"six":6,"sept":7,"huit":8,"neuf":9,"dix":10}
def nombres_mots(txt):
    return [float(v) for w, v in MOTS_FR.items() if re.search(r"(?<!\w)" + w + r"(?!\w)", txt.lower())]
DOSES = {"S25":0.25,"S50":0.5,"S75":0.75,"S100":1.0,"T100":1.0}
def nombres_doses(txt):
    return [v for k, v in DOSES.items() if k in txt]
def present(x, txt, dec=4):
    cands = nombres(txt) + nombres_mots(txt) + nombres_doses(txt)
    for c in cands:
        if abs(round(c, dec) - x) < 1e-9: return True
        if abs(c - x) < 1e-12: return True
    return False

print("\n== 2. sections : chaque nombre du corps contre les lignes citées par le crochet qui le suit")
sec = open(P_SEC, encoding="utf-8").read().split("\n")
i0 = [i for i, l in enumerate(sec) if l.startswith("### Step B:")][0]
i1 = [i for i, l in enumerate(sec) if l.startswith("## Hors billet")][0]
corps = "\n".join(sec[i0:i1])
CRO = re.compile(r"\[(B|Bb) ([0-9a-f]{8}) l\.(\d+)(?:-(\d+))?\]")
EN = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}
NUM_EN = re.compile(r"(?<![\w.])[-−]?\d+(?:,\d{3})*(?:\.\d+)?(?![\w])")
pos = 0; n_ok = n_ko = 0; ko = []
tous = []
for m in CRO.finditer(corps):
    seg = corps[pos:m.start()]; pos = m.end()
    k, h8, a, b = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
    assert H[k].startswith(h8), (k, h8)
    cite = "\n".join(L[k][a-1:b])
    toks = []
    for t in NUM_EN.finditer(seg):
        s = t.group(0)
        # l'expression « 1 − 0.05/3 » et les dates sont traitées à part
        toks.append((s, float(s.replace("−", "-").replace(",", ""))))
    for w, v in EN.items():
        for _ in re.finditer(r"(?<!\w)" + w + r"(?!\w)", seg, flags=re.I):
            toks.append((w, float(v)))
    for s, x in toks:
        ok = present(x, cite)
        ailleurs = ""
        if not ok:
            ou = [str(j+1) for j, l in enumerate(L[k]) if present(x, l)][:12]
            ailleurs = " | ailleurs au même verdict, lignes : " + (", ".join(ou) if ou else "aucune")
            n_ko += 1; ko.append((s, k, a, b))
        else: n_ok += 1
        tous.append(s)
        print(f"  {'OK ' if ok else 'ABSENT'} {s:>10} -> {k} l.{a}" + (f"-{b}" if b != a else "") + ailleurs)
reste = corps[pos:]
print("  texte après le dernier crochet, nombres non rattachés :", [t.group(0) for t in NUM_EN.finditer(reste)])
print(f"  bilan : {n_ok} trouvés à la ligne citée, {n_ko} absents de la ligne citée")

print("\n== 3. table : texte au verdict présent à la ligne citée ; arrondi du nombre")
tab = open(P_TAB, encoding="utf-8").read().split("\n")
t_ok = t_ko = 0
for l in tab:
    if not l.startswith("| B"): continue
    c = [x.strip() for x in re.split(r"(?<!\\)\|", l)[1:-1]]
    section, nb, texte, verdict, chemin, emp, ligne, note = c
    k = "B" if verdict == "étape B" else "Bb"
    texte = texte.replace("\\|", "|")
    ln = int(ligne)
    okh = emp.strip("`") == H[k]
    okc = chemin.strip("`") == os.path.relpath(V[k], R)
    okt = texte in L[k][ln-1]
    # arrondi : chaque décimale à quatre chiffres de la colonne « nombre » doit être l'arrondi d'un nombre du texte au verdict
    arr = []
    for t in re.finditer(r"[-−]?\d+\.\d{4}(?!\d)", nb):
        x = float(t.group(0).replace("−", "-"))
        arr.append((t.group(0), present(x, texte)))
    bon = okh and okc and okt and all(a for _, a in arr)
    t_ok += bon; t_ko += (not bon)
    print(f"  {'OK ' if bon else 'ECART'} l.{ln:<4} {k:<2} | {nb[:38]:<38} | texte présent : {okt} | empreinte : {okh} | chemin : {okc} | arrondis : {arr}")
print(f"  bilan : {t_ok} lignes conformes, {t_ko} en écart")

print("\n== 4. nombres du corps absents de la colonne « nombre » de la table")
col = " ".join(re.split(r"(?<!\\)\|", l)[2] for l in tab if l.startswith("| B")).replace("−", "-")
manq = sorted({s for s in tous if s.replace("−", "-").lower() not in col.lower()})
print("  ", manq)

print("\n== 5. contrôles d'arithmétique sur les nombres recopiés (aucun calcul neuf sur des scores)")
print("  1 - 0.05/3 =", 1 - 0.05/3)
te = [0.9436, 0.9532, 0.9967, 0.9885]; art = [0.9252, 0.9822, 0.9942, 0.9986]; dif = [0.0184, -0.0290, 0.0025, -0.0102]
for a, b, d in zip(te, art, dif):
    print(f"  texte égal {a} - artefact {b} = {a-b:+.4f} ; écrit {d:+.4f} ; écart {abs(a-b-d):.4f}")
print("  étape B, tromperie : aire - quantile =", 0.58160400390625 - 0.5737883300781249, "(D estimation écrite 0.007815673828125091)")
print("  étape B, base à S25 : bas 0.4918449096679688 > quantile 0.51850732421875 ?", 0.4918449096679688 > 0.51850732421875, "; aire >= 0.7 ?", 0.56906005859375 >= 0.7)

print("\n== 6. longueur des deux sections, crochets de source retirés (mots séparés par des blancs)")
sB = "\n".join(sec[i0+1:[i for i, l in enumerate(sec) if l.startswith("### Step B-bis")][0]])
sBb = "\n".join(sec[[i for i, l in enumerate(sec) if l.startswith("### Step B-bis")][0]+1:i1]).replace("---", "")
for nom, s in (("étape B", sB), ("étape B bis", sBb)):
    print("  ", nom, len(CRO.sub("", s).split()), "mots")
