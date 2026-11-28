"""Produit en mémoire, pour chaque option de P-020, P-021 et P-022, le texte que le verrou 1 du brouillon 7 laisse au
texte scellé (en-têtes entre crochets et marqueurs retirés ; versions écartées retirées ; exception de P-021 sous (B) et
(C) appliquée telle qu'écrite), puis cherche les restes : « en attente », « de repli », « Version recommandée »,
renvois « (verrou 1) », marqueurs, lectures « établie » sous (C), passages dépendants d'une version retirée.
N'écrit aucun texte : seulement des numéros de ligne du brouillon 7 et des extraits de 160 caractères au plus,
pris dans le brouillon (aucune configuration lue) — v1.
Usage : python3 -B -I versions_retenues_b7_v1.py BROUILLON7"""
import sys, re
L = open(sys.argv[1], encoding="utf-8").read().split("\n")
TETE = re.compile(r"\*\*\[(Décision de Lazar en attente|Version de repli si Lazar [^\]]*?) : (P-02[012])\]\*\* `<<TRANCHER_P02[012]>>` ?")

def ligne(debut):
    """indice (0) de l'unique ligne qui commence (après espaces) par debut"""
    t = [i for i, l in enumerate(L) if l.lstrip().startswith(debut)]
    assert len(t) == 1, (debut, t)
    return t[0]

# sites : (décision, fin exclusive = ligne d'ancrage qui suit le dernier en-tête)
FINS = {
    "point5": ("P-022", "6. **Déplacement**"),
    "point1.4": ("P-022", "1.5 **Lisibilité du mode raisonné**"),
    "prediction": ("P-021", "**Contre-indices déclarés (R4).**"),
    "P020": ("P-020", "**Sondes.** Sondes de l'auteur"),
    "TC1": ("P-022", "**TC.2 — sondes et juges"),
    "reserve9": ("P-022", "10. **Écart à la note du vivier**"),
    "criteres": ("P-021", "**Combinaisons.**"),
}
# repérer les en-têtes (ligne, position) dans l'ordre du texte
tetes = []
for i, l in enumerate(L):
    for m in TETE.finditer(l):
        tetes.append((i, m.start(), m.end(), m.group(2), m.group(1)))
print("en-têtes trouvés :", len(tetes), {d: sum(1 for t in tetes if t[3] == d) for d in ("P-020", "P-021", "P-022")})
# grouper les en-têtes en sites, par ordre, avec leur fin
sites = []
for nom, (dec, ancre) in FINS.items():
    fin = ligne(ancre)
    ts = [t for t in tetes if t[3] == dec and t[0] < fin and all(t not in s["tetes"] for s in sites)]
    # garder seulement le groupe contigu le plus proche de la fin
    groupe = []
    for t in reversed(ts):
        if not groupe or groupe[0][0] - t[0] < 40:
            groupe.insert(0, t)
        else:
            break
    sites.append({"nom": nom, "dec": dec, "fin": fin, "tetes": groupe})
for s in sites:
    print(f"site {s['nom']:10s} {s['dec']} : en-têtes aux lignes {[t[0] + 1 for t in s['tetes']]}, fin avant la ligne {s['fin'] + 1}")
assert sum(len(s["tetes"]) for s in sites) == len(tetes)

def option_de(tete_txt):
    if tete_txt.startswith("Décision"): return "rec"
    m = re.search(r"option \(([^)]*)\)( ou \(([^)]*)\))?", tete_txt)
    if m: return {m.group(1)} | ({m.group(3)} if m.group(3) else set())
    if "refuse" in tete_txt: return {"refus"}
    raise ValueError(tete_txt)

def versions(s):
    """liste de (options, texte de la version sans en-tête ni marqueur), en caractères"""
    out = []
    for k, t in enumerate(s["tetes"]):
        i, a, b = t[0], t[1], t[2]
        if k + 1 < len(s["tetes"]):
            j, c = s["tetes"][k + 1][0], s["tetes"][k + 1][1]
            txt = "\n".join([L[i][b:]] + L[i + 1:j] + [L[j][:c]])
            if j == i: txt = L[i][b:c]
        else:
            txt = "\n".join([L[i][b:]] + L[i + 1:s["fin"]])
        out.append((option_de(t[4]), txt))
    return out

REC = {"P-020": "a", "P-021": "A", "P-022": "b"}
OPTS = {"P-020": ["a", "refus"], "P-021": ["A", "B", "C"], "P-022": ["a", "b", "c"]}

def texte_site(s, opt):
    vs = versions(s)
    garde = [txt for o, txt in vs if (o == "rec" and opt == REC[s["dec"]]) or (o != "rec" and opt in o)]
    rec = [txt for o, txt in vs if o == "rec"][0]
    if s["dec"] == "P-021" and opt in ("B", "C"):
        # exception du verrou 1, appliquée telle qu'écrite
        lignes = rec.split("\n")
        tab = [l for l in lignes if l.startswith("|")]
        par = "\n".join(l for l in lignes if not l.startswith("|"))
        blocs = [b.strip() for b in par.split("\n\n") if b.strip()]
        trois = [b for b in blocs if b.startswith("**Trois lectures.**")]
        clause = [b for b in blocs if b.startswith("**Clause de repli mécanique.**")]
        sans = [b for b in blocs if b.startswith("Sans le bras")]
        if opt == "B":
            tab2 = [("[LIGNE C-P3b « REMPLACÉE PAR LA VERSION (B)  » : MOTS NON ÉCRITS]" if l.startswith("| C-P3b") else l) for l in tab]
            kept = "\n".join(tab2) + "\n\n" + ("\n\n".join(trois + clause + sans) if s["nom"] == "prediction" else "")
        else:
            if s["nom"] == "prediction":
                tab2 = ["| " + " | ".join(c.strip() for c in l.strip("|").split("|")[:2]) + " |" for l in tab]
                kept = "\n".join(tab2) + "\n\n" + "\n\n".join(trois + sans)
            else:
                kept = ""
        return kept + "\n\n" + "\n\n".join(garde)
    return "\n\n".join(garde)

def assembler(choix):
    """texte entier (liste de lignes, sans numéros) pour un choix {décision: option}"""
    morceaux = []
    pos = 0
    for s in sorted(sites, key=lambda s: s["tetes"][0][0]):
        i0, a0 = s["tetes"][0][0], s["tetes"][0][1]
        morceaux.append(("\n".join(L[pos:i0] + [L[i0][:a0]]), pos + 1))
        morceaux.append(("⟦" + texte_site(s, choix[s["dec"]]) + "⟧", None))
        pos = s["fin"]
    morceaux.append(("\n".join(L[pos:]), pos + 1))
    return morceaux

MOTIFS = [("en attente", r"en attente"), ("de repli", r"de repli"), ("Version recommandée", r"[Vv]ersion recommandée"),
          ("(verrou 1)", r"verrou 1"), ("marqueur TRANCHER", r"<<TRANCHER"), ("en-tête [", r"\*\*\["),
          ("« établie »", r"établie"), ("constat nu", r"constat nu|g_constat|constat_nu"),
          ("usurpation de l'agent / HU, SU", r"usurpation écrite par l'agent|\bHU\b|\bSU\b|usurpation de l'agent"),
          ("ci-dessus", r"ci-dessus")]
def chercher(choix, quoi):
    res = []
    for txt, l0 in assembler(choix):
        if l0 is None:
            for nom, rx in quoi:
                for m in re.finditer(rx, txt):
                    a = max(0, m.start() - 70); b = min(len(txt), m.end() + 70)
                    res.append(("VERSION", nom, txt[a:b].replace("\n", " ")))
    return res

for dec in ("P-021", "P-020", "P-022"):
    for opt in OPTS[dec]:
        choix = dict(REC); choix[dec] = opt
        print(f"\n===== {dec} = ({opt}) ; autres à leur défaut =====")
        for s in sorted(sites, key=lambda s: s["tetes"][0][0]):
            if s["dec"] != dec: continue
            t = texte_site(s, opt)
            print(f"--- site {s['nom']} ({len(t)} caractères gardés)")
            for nom, rx in MOTIFS:
                for m in re.finditer(rx, t):
                    a = max(0, m.start() - 60); b = min(len(t), m.end() + 60)
                    print(f"    [{nom}] …{t[a:b]}…".replace("\n", " ")[:200])
