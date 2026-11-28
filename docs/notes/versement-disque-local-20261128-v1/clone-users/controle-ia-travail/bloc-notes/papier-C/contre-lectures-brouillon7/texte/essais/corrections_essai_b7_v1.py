"""Applique en mémoire au brouillon 7 les corrections proposées par cette contre-lecture (ancien texte trouvé une seule
fois, espaces et sauts de ligne indifférents, sinon arrêt), puis produit le texte de chaque option de P-021 sous la
règle corrigée du verrou 1 et cherche les restes. N'écrit rien sur disque — v1.
Usage : python3 -B -I corrections_essai_b7_v1.py BROUILLON7"""
import sys, re
T = open(sys.argv[1], encoding="utf-8").read()
def rx(s):
    return re.compile(r"\s+".join(re.escape(w) for w in s.split()))
C = [
 # CB7-texte-01
 ("leur ligne C-P3b étant remplacée par la version (B)",
  "avec deux changements dans la ligne C-P3b du tableau de la section « Prédiction » : « concordant : p unilatéral ≤ 0,05 par rééchantillonnage centré » y devient « sans verdict : p unilatéral rapporté, par rééchantillonnage centré », et « aucune ; p > 0,05 : « non établie » » y devient « aucune » ; la ligne C-P3b du tableau des « Critères de lecture gelés » est retirée"),
 ("sous (C), seul le tableau de la section « Prédiction » reste, réduit à ses colonnes « id » et « grandeur », avec le paragraphe « Trois lectures » et la phrase « Sans le bras … ».",
  "sous (C), seul le tableau de la section « Prédiction » reste, entier, avec le paragraphe « Trois lectures » et la phrase « Sans le bras … », dont la version (C) dit que les seuils ne sont pas lus."),
 ("comme au tableau de la version recommandée, gardé (verrou 1), trois lectures", "comme au tableau ci-dessus, trois lectures"),
 ("les statistiques définies à la colonne « grandeur » du tableau de la version recommandée, gardé (verrou 1) (W de C-P3a,",
  "les statistiques définies au tableau ci-dessus (W de C-P3a,"),
 ("sont écrites sans lecture « établie » ni réfutation.",
  "sont écrites sans lecture « établie » ni réfutation. Leurs valeurs p sont celles que le tableau définit (loi exacte ; rééchantillonnage centré) ; les seuils du tableau, la condition « « établie » seulement si les trois lectures concluent » et la règle « établie seulement si W = 1 » ne sont pas lus."),
 ("C-P3a et C-P3c comme au tableau de la version recommandée, gardé (verrou 1) ;", "C-P3a et C-P3c comme au tableau ci-dessus ;"),
 # CB7-texte-02
 ("la décision est écrite aux champs du scellement et dans la configuration.",
  "la décision est écrite aux champs du scellement et dans la configuration. Sous la version retenue, l'amorce « Version recommandée » et sa parenthèse deviennent « Version retenue (champs du scellement, « Décisions ») » ; sous (B) ou (C) de P-021, l'amorce de la version recommandée de la section « Prédiction », jusqu'à « clause de repli mécanique. », est retirée avec son en-tête. Au scellement, le texte de ce verrou est remplacé par « Décisions de Lazar P-021, P-020 et P-022 : écrites aux champs du scellement (« Décisions ») et dans la configuration ; correction de P-021 : `<<LIGNE_CORRECTION_P021>>`. »"),
 ("et sa ligne de correction, verrou 1)", "et sa ligne de correction, `<<LIGNE_CORRECTION_P021>>`)"),
 # CB7-texte-03
 ("insertion remplie du constat nu, pour les deux corpus (Métrique, point 5)",
  "insertion remplie du constat nu, pour les deux corpus (Métrique, point 5 ; option (b) de P-022 seulement)"),
 ("ou l'insertion du constat nu (bloc P-022)", "ou l'insertion du constat nu (bloc P-022, option (b))"),
 ("déclenche, le cas échéant, la clause de repli du bloc P-021.", "déclenche, le cas échéant, la clause de repli du bloc P-021 (options (A) et (B))."),
 ("rééchantillonnage centré pour son verdict (et pour celui de C-P3a, avec la loi exacte)",
  "rééchantillonnage centré pour sa valeur p (et pour celle de C-P3a, avec la loi exacte)"),
 ("restent en attente, sous leurs marqueurs.", "étaient en attente à l'écriture de ce brouillon, sous leurs marqueurs."),
 ("Décision de Lazar en attente, versions de repli écrites.", "Décision de Lazar alors en attente, versions de repli écrites."),
 ("décision de Lazar en attente (P-022), versions de repli écrites.", "décision de Lazar alors en attente (P-022), versions de repli écrites."),
 # CB7-texte-04
 ("Contre-lecture « texte » du brouillon 6 (contre-lecture 9, avec la question : la déclaration de la réserve 14 suffit-elle ?)",
  "Contre-lecture « texte » du brouillon 7 (contre-lecture 9 ; la question de R-309 a reçu sa réponse de la contre-lecture « texte » du brouillon 6 : la déclaration suffit)"),
 ("**Contre-lecture 9** — lentille « texte » du brouillon 6 (application du traitement ; question explicite : la déclaration de la réserve 14 suffit-elle, R-309 ?)",
  "**Contre-lecture 9** — lentille « texte » du brouillon 7 (constats du brouillon 6 et décisions de la session appliqués ; versions de P-020, P-021 et P-022 produites option par option ; énoncés ; configuration par indices ; sortie de `problemes` rejouée)"),
]
for k, (a, b) in enumerate(C, 1):
    m = list(rx(a).finditer(T))
    if len(m) != 1:
        sys.exit(f"correction {k} : ancien texte trouvé {len(m)} fois — arrêt")
    T = T[:m[0].start()] + b + T[m[0].end():]
print(f"{len(C)} corrections appliquées en mémoire, chacune trouvée une seule fois")
L = T.split("\n")
def i_de(debut):
    t = [i for i, l in enumerate(L) if l.lstrip().startswith(debut)]; assert len(t) == 1, (debut, t); return t[0]
def bloc(debut, fin):
    return i_de(debut), i_de(fin)
TETE = re.compile(r"\*\*\[[^\]]*P-021\]\*\* `<<TRANCHER_P021>>` ?")
def site(a, b):
    lignes = L[a:b]; s = "\n".join(lignes)
    parts = TETE.split(s); assert len(parts) == 4, len(parts)
    return parts[1], parts[2], parts[3]   # rec, B, C
idx = [i for i, l in enumerate(L) if l.startswith("**[Décision de Lazar en attente : P-021]**")]
assert len(idx) == 2
pa = idx[0]; pb = i_de("**Contre-indices déclarés (R4).**"); ca = idx[1]; cb = i_de("**Combinaisons.**")
P_rec, P_B, P_C = site(pa, pb); C_rec, C_B, C_C = site(ca, cb)
def amorce(rec):
    # retire l'amorce « Version recommandée (…) » jusqu'au premier « : » de fin de parenthèse
    return re.sub(r"^Version recommandée \((?:[^()]|\([^()]*\))*\) :", "Version retenue (champs du scellement, « Décisions ») :", rec.strip())
def tab(rec): return [l for l in rec.split("\n") if l.startswith("|")]
def blocs(rec):
    par = "\n".join(l for l in rec.split("\n") if not l.startswith("|"))
    return [b.strip() for b in par.split("\n\n") if b.strip()]
def garder(rec, noms): return [b for b in blocs(rec) if any(b.startswith(n) for n in noms)]
out = {}
out["A"] = (amorce(P_rec), amorce(C_rec))
tB = []
for l in tab(P_rec):
    if l.startswith("| C-P3b"):
        assert l.count("concordant : p unilatéral ≤ 0,05 par rééchantillonnage centré") == 1 and l.count("aucune ; p > 0,05 : « non établie »") == 1
        l = l.replace("concordant : p unilatéral ≤ 0,05 par rééchantillonnage centré", "sans verdict : p unilatéral rapporté, par rééchantillonnage centré").replace("aucune ; p > 0,05 : « non établie »", "aucune")
    tB.append(l)
cB = [l for l in tab(C_rec) if not l.startswith("| C-P3b")]
out["B"] = ("\n".join(tB) + "\n\n" + "\n\n".join(garder(P_rec, ["**Trois lectures.**", "**Clause de repli mécanique.**", "Sans le bras"])) + "\n\n" + P_B.strip(),
            "\n".join(cB) + "\n\n" + C_B.strip())
out["C"] = ("\n".join(tab(P_rec)) + "\n\n" + "\n\n".join(garder(P_rec, ["**Trois lectures.**", "Sans le bras"])) + "\n\n" + P_C.strip(), C_C.strip())
MOTIFS = [("en attente", r"en attente"), ("de repli (hors « Clause de repli »)", r"(?<!Clause )(?<!clause )de repli"), ("version recommandée", r"[Vv]ersion recommandée"),
          ("verrou", r"verrou"), ("marqueur", r"<<"), ("en-tête", r"\*\*\["), ("ci-dessus", r"ci-dessus")]
for o, (p, c) in out.items():
    print(f"\n=== P-021 ({o}) : prédiction {len(p)} car., critères {len(c)} car.")
    for nom, r in MOTIFS:
        for lieu, t in (("prédiction", p), ("critères", c)):
            for m in re.finditer(r, t):
                print(f"  [{nom}] {lieu} : …{t[max(0, m.start() - 60):m.end() + 60]}…".replace("\n", " "))
    if o == "B":
        print("  ligne C-P3b (prédiction), cellules 3 et 4 :", [x.strip()[:70] for x in [l for l in tB if l.startswith('| C-P3b')][0].strip('|').split('|')[2:4]])
        print("  lignes du tableau des critères :", [l.split('|')[1].strip() for l in cB[2:]])
print("\nmarqueurs restants hors TRANCHER (texte corrigé entier) :", sorted(set(re.findall(r"<<[A-Z0-9_]+>>", T)) - {"<<TRANCHER_P020>>", "<<TRANCHER_P021>>", "<<TRANCHER_P022>>"}).__len__())
