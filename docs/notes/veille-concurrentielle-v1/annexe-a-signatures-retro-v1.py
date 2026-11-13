"""Règle mécanique des signatures du rétro-test (protocole de veille v2, annexe A).
Entrée : le programme v2 (empreinte de lancement) ; sortie : signatures par pièce.
Aucun identifiant d'article n'est lu ni écrit ; garde : refus de toute signature contenant 2609/2610/2611."""
import re, sys, json, hashlib

PROG = sys.argv[1]
ATTENDU = "2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c"
data = open(PROG, "rb").read()
assert hashlib.sha256(data).hexdigest() == ATTENDU, "empreinte du programme v2 non conforme"
L = data.decode("utf-8").split("\n")

def ligne(n): return L[n - 1]
def cellule_b_43(): return ligne(43).split("|")[4]

# pièce -> textes sources (numéros de ligne du programme v2)
SOURCES = {
 "A-H1": [93], "A-H2": [94], "A-L": [55, 56], "A-T": [62], "A-H6": [97], "A-Tr": [98], "A-H8": [99],
 "B-POP": [208], "B-ST": [211, "43B"], "B-H3": [111], "B-H4'": [112], "B-H5": [113], "B-H7": [114],
 "C-HC1": [102], "C-HC2": [103], "C-HC2b": [104], "C-HC3": [105], "C-HC4": [106], "C-HC5": [107], "C-HC6": [108],
}
MARQUES_CEDE = ["revendicable :", "est déjà décrit", "sont publiées"]  # v1.1 : correctif de coupe (déclaré)

def nettoyer(t):
    t = re.sub(r"^\s*-\s*\*\*[^*]+\*\*\s*(\([^)]*\))?\.?\s*", "", t)   # titre gras et parenthèse de poids
    t = re.sub(r"^\s*\*\*[^*]+\*\*\s*", "", t)                          # titre gras seul (ligne de T)
    t = re.sub(r"^(Hypothèses|Énoncé)\s*:\s*", "", t)
    return t.replace("**", "")

def couper(t):
    phrases = re.split(r"(?<=[.;])\s+", t)
    garde, cede, coupe = [], [], False
    for p in phrases:
        if not coupe and any(m in p.lower() for m in MARQUES_CEDE): coupe = True
        (cede if coupe else garde).append(p)
    return " ".join(garde), " ".join(cede)

# lexique : (terme, axe, codes acceptés) ; plus long d'abord ; insensible à la casse
LEX = [
 ("obfuscation d'activations", "TA", ["TA4"]), ("obfuscation d'activations", "ME", ["ME8"]),
 ("bruit d'activations", "TA", ["TA6"]),
 ("taux de faux positifs", "GA", ["GA2", "GA3", "GA4"]),
 ("accumulation séquentielle", "AC", ["AC4"]),
 ("séquentiel par agent", "AC", ["AC4"]),
 ("statistique spatio-temporelle", "AC", ["AC7"]),
 ("statistique de population", "AC", ["AC6", "AC7"]),
 ("coupe transversale", "AC", ["AC6"]),
 ("agrégation par agent", "AC", ["AC2", "AC4"]),
 ("autocorrélation", "AC", ["AC5"]), ("co-élévation", "AC", ["AC6", "AC7"]),
 ("somme cumulée", "AC", ["AC4"]), ("processus e", "AC", ["AC4"]), ("processus e", "GA", ["GA4"]),
 ("toujours valide", "GA", ["GA4"]), ("puissance", "GA", ["GA9"]),
 ("niveau token", "AC", ["AC8"]), ("niveau action", "AC", ["AC1"]), ("max", "AC", ["AC2"]), ("moyenne", "AC", ["AC3"]),
 ("sabotage diffus", "ME", ["ME1"]), ("sous le seuil", "ME", ["ME1"]),
 ("budget total de sabotage", "ME", ["ME11"]), ("budget de sabotage", "ME", ["ME11"]), ("répartition du sabotage", "ME", ["ME11"]),
 ("marginale préservée", "ME", ["ME11"]), ("attaquant adaptatif", "ME", ["ME8", "ME11"]),
 ("sabotage", "ME", ["ME1", "ME2"]), ("fragmentation", "ME", ["ME1", "ME4"]), ("coordination", "ME", ["ME4"]),
 ("attaque par contenu", "ME", ["ME5", "ME7"]), ("famille d'attaque", "ME", ["ME5"]), ("ordres en bande", "ME", ["ME5"]),
 ("usurpation stylistique", "ME", ["ME5"]), ("rhétorique", "ME", ["ME5"]), ("manipuler", "ME", ["ME5"]),
 ("attaques de corruption", "ME", ["ME5"]), ("attaque optimisée", "ME", ["ME5", "ME8"]), ("pression", "ME", ["ME5"]),
 ("robustesse adverse", "ME", ["ME7", "ME8"]), ("adaptation de l'équipe rouge", "ME", ["ME11"]),
 ("transfert d'attaque", "ME", ["ME7", "ME8"]),
 ("fondé sur les activations", "TA", ["TA3"]), ("signatures internes", "TA", ["TA3"]), ("activations", "TA", ["TA3"]),
 ("boîte blanche", "TA", ["TA3"]), ("boîte noire", "TA", ["TA1", "TA2"]),
 ("score de sonde", "TA", ["TA3"]), ("scores de sondes", "TA", ["TA3"]), ("panel de sondes", "TA", ["TA3"]),
 ("g_sonde", "TA", ["TA3"]), ("sondes", "TA", ["TA3"]), ("sonde", "TA", ["TA3"]),
 ("paraphrase", "TA", ["TA6"]), ("ré-échantillonnage", "TA", ["TA6"]), ("remise à zéro de contexte", "TA", ["TA6"]),
 ("moniteur génératif", "OS", ["OS5"]), ("juges génératifs", "OS", ["OS5"]), ("juges", "OS", ["OS5"]), ("juge", "OS", ["OS5"]),
 ("quorum", "OS", ["OS5", "OS7"]),
 ("copies", "OS", ["OS6"]), ("partagent leurs poids", "OS", ["OS6"]), ("essaim", "OS", ["OS6"]),
 ("agent isolé", "OS", ["OS1"]), ("agents", "OS", ["OS6", "OS7"]),
 ("tâches floues", "CA", ["CA3"]), ("équipe rouge", "CA", ["CA1"]), ("protocole", "CA", ["CA1"]),
 ("déploiement", "CA", ["CA1", "CA8"]),
 ("horizon", "EC", ["horizon variable (au moins deux valeurs)"]),
 ("avec n", "EC", ["nombre d'agents variable (au moins deux valeurs)"]),
 ("nombre m de moniteurs", "EC", ["nombre de moniteurs variable (au moins deux valeurs)"]),
]
LEX = sorted(LEX, key=lambda e: -len(e[0]))
ORDRE_AXES = ["ME", "TA", "AC", "GA", "OS", "CA", "EC"]

def deriver(texte):
    t = " " + texte.lower() + " "
    entrees = []
    for terme, axe, codes in LEX:
        motif = r"(?<![\w-])" + re.escape(terme) + r"(?![\w-])"
        if re.search(motif, t):
            entrees.append((axe, tuple(codes), terme))
            t = re.sub(motif, " # ", t)
    sig = {}
    for axe, codes, terme in entrees:
        lst = sig.setdefault(axe, [])
        if codes not in [c for c, _ in lst]: lst.append((codes, terme))
    return sig

sortie = {}
for piece, srcs in SOURCES.items():
    brut = " ".join(cellule_b_43() if s == "43B" else ligne(s) for s in srcs)
    garde, cede = couper(nettoyer(brut))
    sig = deriver(garde)
    blob = json.dumps(sig, ensure_ascii=False)
    assert not re.search(r"26(09|10|11)\.\d{4,5}", blob + garde + cede), "garde : identifiant postérieur"
    axes = [a for a in ORDRE_AXES if a in sig]
    discr = None
    for a in ORDRE_AXES:
        if a in sig and a != "EC": discr = (a, list(sig[a][0][0])); break
    sortie[piece] = {"lignes": srcs, "texte_exigence": garde, "texte_cede": cede, "axes": axes, "n_axes": len(axes),
                     "signature": {a: [list(c) for c, _ in sig[a]] for a in axes},
                     "termes": {a: [term for _, term in sig[a]] for a in axes}, "discriminant": discr,
                     "statut": "garde" if len(axes) >= 3 else ("garde, signature pauvre" if len(axes) == 2 else "sort du rétro-test")}
print(json.dumps(sortie, ensure_ascii=False, indent=1))

# ---- Annexe A.2 : organisme, à part (information seulement ; pièces nées après t0) ----
if len(sys.argv) > 3:
    NOTE, N065 = sys.argv[2], sys.argv[3]
    assert hashlib.sha256(open(NOTE, "rb").read()).hexdigest().startswith("08a3738af518f597")
    assert hashlib.sha256(open(N065, "rb").read()).hexdigest().startswith("f820e90da0920d50")
    SUPP = [
     ("juge statistique", "OS", ["OS9"]), ("juges modèles", "OS", ["OS10"]), ("juge-tournoi", "OS", ["OS10"]),
     ("juge génératif", "OS", ["OS10"]), ("proposeurs", "OS", ["OS11"]), ("proposeur", "OS", ["OS11"]),
     ("plusieurs fournisseurs", "OS", ["OS7"]),
     ("orchestrateur", "TA", ["TA5"]), ("hors de tout agent", "TA", ["TA5"]),
     ("e-valeurs", "GA", ["GA4"]), ("scellées", "GA", ["GA7"]), ("scellement", "GA", ["GA7"]), ("empreinte", "GA", ["GA7"]),
     ("préenregistrée", "GA", ["GA7"]), ("préenregistrés", "GA", ["GA7"]), ("lois connues", "GA", ["GA8"]), ("archive", "GA", ["GA8"]),
     ("tricheurs", "ME", ["ME9"]), ("goodhart", "ME", ["ME9"]), ("toute promotion est fausse", "ME", ["ME9"]),
     ("idée", "CA", ["CA5"]), ("hypothèses", "CA", ["CA5"]), ("fiche", "CA", ["CA5"]), ("affirmations de recherche", "CA", ["CA5"]),
     ("vérité plantée", "GA", ["GA2"]), ("témoins plantés", "GA", ["GA2"]),
    ]
    LEX2 = sorted(LEX + SUPP, key=lambda e: -len(e[0]))
    def deriver2(texte):
        global LEX
        sauve = LEX; LEX = LEX2
        try: return deriver(texte)
        finally: LEX = sauve
    N = open(NOTE, encoding="utf-8").read().split("\n")
    textes = {}
    for n in range(257, 277):
        cols = N[n - 1].split("|")
        cle = cols[1].strip(); txt = re.sub(r"\((README|`)[^)]*\)", "", cols[2]).strip()
        textes[cle] = (f"note l. {n}", txt)
    R = open(N065, encoding="utf-8").read().split("\n")
    textes["rôle 1"] = ("N-065 l. 15-17", re.sub(r"\*\*", "", " ".join(R[14:17])))
    org = {}
    for cle, (src, txt) in textes.items():
        sig = deriver2(txt); axes = [a for a in ORDRE_AXES if a in sig]
        org[cle] = {"source": src, "texte": txt, "axes": axes, "signature": {a: [list(c) for c, _ in sig[a]] for a in axes},
                    "statut": "garde" if len(axes) >= 3 else ("garde, signature pauvre" if len(axes) == 2 else "hors du résultat à part")}
    json.dump(org, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
