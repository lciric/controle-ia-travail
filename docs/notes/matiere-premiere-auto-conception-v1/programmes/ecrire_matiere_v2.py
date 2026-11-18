#!/usr/bin/env python3
"""Écrit matiere-premiere-v2.md : version corrigée par la contre-lecture neuve du catalogue
(contre-lecture-catalogue-v1.md). Mêmes entrées que la v1 (releve-mecanismes-v1.json, programmes/regroupements-v1/),
corrections de la contre-lecture appliquées en mémoire (aucun fichier d'entrée n'est réécrit ; la v1 reste en place, R12).
Gardes : empreintes des entrées vérifiées ; chaque correction vérifie son « avant » (identifiant présent, famille,
regroupement, texte) ; chaque mécanisme décrit des huit familles est rangé exactement une fois ; la garde est testée au
début sur un cas sain et sur un artefact (R5).
Usage (depuis docs/notes/matiere-premiere-auto-conception-v1) :
  python -I programmes/ecrire_matiere_v2.py > programmes/ecrire_matiere_v2.sortie.txt"""
import collections, copy, hashlib, json, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
ICI = "docs/notes/matiere-premiere-auto-conception-v1/"
FAM8 = ["exploration", "originalité", "épreuve", "jugement", "mémoire", "sélection", "coût", "auto-conception"]
FICH = {"exploration": "exploration", "originalité": "originalite", "épreuve": "epreuve", "jugement": "jugement",
        "mémoire": "memoire", "sélection": "selection", "coût": "cout", "auto-conception": "auto-conception"}
EPR = ["oui, mesuré", "oui, affirmé", "non", "inconnu"]
PROF = {"lecture approfondie sur PDF": "lecture approfondie", "page ou résumé": "page ou résumé", "notice seule": "notice seule"}

def sha(chemin):
    return hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest()

# --- entrées et empreintes ------------------------------------------------------------------------------------------
ATTENDU = {ICI + "releve-mecanismes-v1.json": "1110ef784e5c628dc2017e9aab1abbd57ca10ba784ecb4f18d2c732bdc453faa",
           ICI + "matiere-premiere-v1.md": "98f63ecc2820a77fb8e36eabd7ad1a0f7d11f94da1a23a7e503b0e1cc67f6fc3"}
for f in FICH.values():
    p = ICI + f"programmes/regroupements-v1/{f}.txt"
    ATTENDU[p] = (RACINE / (p + ".sha256")).read_text().split()[0]
for p, h in ATTENDU.items():
    if sha(p) != h:
        sys.exit(f"ARRÊT : empreinte non conforme pour {p}")
REL = json.loads((RACINE / (ICI + "releve-mecanismes-v1.json")).read_text(encoding="utf-8"))

# --- corrections de la contre-lecture (contre-lecture-catalogue-v1.md, section 6) -----------------------------------
SUGG_PLUS = ["126.2", "236.2", "391.0", "391.1", "445.0"]          # connus par le seul titre, comptés comme décrits en v1
EXCLUS = ["552.0", "552.1", "466.1"]                                # cloisonnement : famille exclue
DEPLACE = {"240.2": ("sélection", 4, 5), "562.0": ("jugement", 12, 2), "472.2": ("mémoire", 12, 7)}
TEXTE = {"221.0": (" ; utile pour nommer rôles et compositions.", "."),
         "457.0": (" (utile seulement comme porte d'entrée bibliographique).", ".")}

def lire_regroupements():
    CL = {}
    for fam in FAM8:
        CL[fam] = []
        for ligne in (RACINE / (ICI + f"programmes/regroupements-v1/{FICH[fam]}.txt")).read_text(encoding="utf-8").splitlines():
            if ligne.startswith("## "):
                CL[fam].append(dict(nom=ligne[3:].strip(), ids=[]))
            elif ligne.startswith("ids:"):
                CL[fam][-1]["ids"] += ligne[4:].split()
    return CL

def appliquer(rel, CL, sugg, exclus, deplace, texte):
    """Applique les corrections sur des copies ; lève ValueError si un « avant » ne correspond pas."""
    rel = copy.deepcopy(rel); CL = copy.deepcopy(CL)
    M = {m["id"]: (e, m) for e in rel["travaux"] for m in e["mecanismes"]}
    for i in sugg:
        if i not in M or M[i][1]["suggere_par_le_titre"] or "titre" not in M[i][1]["mecanisme_en_une_phrase"]:
            raise ValueError(f"avant différent (suggéré) : {i}")
        M[i][1]["suggere_par_le_titre"] = True
        for c in CL[M[i][1]["famille"]]:
            if i in c["ids"]:
                c["ids"].remove(i)
    for i in exclus:
        if i not in M:
            raise ValueError(f"identifiant inconnu (exclu) : {i}")
        e, m = M[i]
        e["mecanismes"] = [x for x in e["mecanismes"] if x["id"] != i]
        for c in CL[m["famille"]]:
            if i in c["ids"]:
                c["ids"].remove(i)
        if not e["mecanismes"]:
            e["statut"] = "exclue"
    for i, (fam, de, vers) in deplace.items():
        if i not in M or M[i][1]["famille"] != fam or i not in CL[fam][de - 1]["ids"]:
            raise ValueError(f"avant différent (déplacement) : {i}")
        CL[fam][de - 1]["ids"].remove(i)
        CL[fam][vers - 1]["ids"].append(i)
    for i, (avant, apres) in texte.items():
        if i not in M or avant not in M[i][1]["mecanisme_en_une_phrase"]:
            raise ValueError(f"avant différent (texte) : {i}")
        M[i][1]["mecanisme_en_une_phrase"] = M[i][1]["mecanisme_en_une_phrase"].replace(avant, apres)
    # couverture : chaque mécanisme décrit des huit familles rangé exactement une fois
    M = {m["id"]: (e, m) for e in rel["travaux"] for m in e["mecanismes"]}
    for fam in FAM8:
        vus = collections.Counter(i for c in CL[fam] for i in c["ids"])
        attendus = {i for i, (e, m) in M.items() if m["famille"] == fam and not m["suggere_par_le_titre"]}
        if any(n > 1 for n in vus.values()) or set(vus) != attendus or any(not c["ids"] for c in CL[fam]):
            raise ValueError(f"couverture rompue : {fam}")
    return rel, CL

CL0 = lire_regroupements()
appliquer(REL, CL0, SUGG_PLUS, EXCLUS, DEPLACE, TEXTE)                       # cas sain
try:                                                                          # artefact : un « avant » faux doit arrêter
    appliquer(REL, CL0, SUGG_PLUS, EXCLUS, {"240.2": ("sélection", 5, 4)}, TEXTE)
    sys.exit("ARRÊT : la garde n'a pas refusé l'artefact")
except ValueError:
    print("garde « avant » : cas sain accepté, artefact refusé")
rel, CL = appliquer(REL, CL0, SUGG_PLUS, EXCLUS, DEPLACE, TEXTE)
T = {e["indice"]: e for e in rel["travaux"]}
M = {m["id"]: (e, m) for e in rel["travaux"] for m in e["mecanismes"]}
CLEF = {i: (fam, n, c["nom"]) for fam in FAM8 for n, c in enumerate(CL[fam], 1) for i in c["ids"]}
print("regroupements v2 :", sum(len(CL[f]) for f in FAM8), "; mécanismes rangés :", len(CLEF))

# --- machines (liste de la v1, reprise telle quelle) ----------------------------------------------------------------------
MACH_LUES = [593, 112, 121, 57]
MACH_NOTICE = [136, 240, 239, 236, 629, 241, 254, 245, 125, 595, 396, 482, 259, 384, 607, 625, 110, 70, 126, 611, 398, 513, 594, 358, 576, 577,
               2, 13, 133, 139, 142, 141, 135, 134, 150, 128, 279, 452, 102, 107, 118, 120, 395, 441, 488, 491, 332, 30, 541, 550, 529, 370, 198, 397, 104, 111, 407]
MACH = set(MACH_LUES) | set(MACH_NOTICE)
NON_RECENSES = [10, 66, 97, 108, 129, 140, 143, 145, 178, 212, 375, 400, 454, 455, 514, 583, 605, 618]
for k in NON_RECENSES:
    assert k not in MACH and sum(1 for m in T[k]["mecanismes"] if m["id"] in CLEF) >= 2, k
UN_SEUL = sorted(k for k in MACH if sum(1 for m in T[k]["mecanismes"] if m["id"] in CLEF) == 1)

# même idée chez une machine recensée, rangée sous un autre regroupement (contre-lecture, section 4)
MEME_IDEE = {
    ("exploration", 4): [("259.0", "une direction de recherche distincte, courte et vague, assignée à chaque agent"),
                         ("128.0", "une expertise distincte, distillée d'un graphe, servie à chaque agent du débat")],
    ("exploration", 11): [("30.0", "les agents de code à longue durée convergent vers une seule approche"),
                          ("513.0", "la sélection des parents homogénéise l'archive")],
    ("originalité", 5): [("513.1", "diversité de l'archive suivie et protégée contre l'homogénéisation"),
                         ("13.4", "carte des « bassins d'idées » des artefacts")],
    ("épreuve", 2): [("441.0", "chaque facteur noté sur les seuls rendements révélés après son dépôt")],
    ("épreuve", 12): [("332.1", "résultats énoncés sous forme falsifiable, fiche d'expérience immuable")],
    ("jugement", 2): [("441.0", "l'arbitre note sur les rendements révélés après le dépôt"),
                      ("550.1", "alignement avec la suite réelle de la lignée de citations")],
    ("jugement", 5): [("441.1", "l'arbitre éprouvé sur un monde synthétique à vérité plantée"),
                      ("104.0", "le tri des preuves éprouvé sur des mécanismes plantés")],
    ("jugement", 7): [("2.1", "sélecteur appris sur les propositions déjà vérifiées, qui écarte la moitié des candidats")],
    ("jugement", 11): [("491.0", "vérification par programme des citations, des chiffres et des affirmations du texte produit")],
    ("jugement", 14): [("121.0", "découverte définie par un écart de croyance face à une référence informée"),
                       ("198.1", "nouveauté mesurée par l'écart de croyance avant et après la preuve"),
                       ("576.0", "porte par pari séquentiel valide sous arrêt optionnel")],
    ("sélection", 12): [("513.0", "homogénéisation de l'archive par la sélection des parents"),
                        ("576.1", "l'auto-piratage statistique de la règle gloutonne est nommé"),
                        ("593.0", "le choix glouton sur le score immédiat est dénoncé")],
    ("coût", 5): [("136.0", "audit à budget d'appels strictement apparié contre des tirages indépendants"),
                  ("13.3", "comparaison à budget de calcul égal avec le meilleur de N courses")],
}
VOISIN = {
    ("coût", 13): [("126.0", "« plus d'agents ou d'itérations ne donne pas de meilleures découvertes », constat de départ")],
    ("mémoire", 12): [("126.1", "garde contre la propagation d'affirmations non étayées par la mémoire partagée")],
    ("jugement", 1): [("550.1", "comparaisons par paires et classement à l'aveugle par dix chercheurs")],
    ("coût", 7): [("13.3", "le travail des N − 1 courses perdantes du meilleur de N est perdu")],
}
for d in (MEME_IDEE, VOISIN):
    for k, lst in d.items():
        for i, _ in lst:
            assert i in CLEF and M[i][0]["indice"] in MACH and CLEF[i][:2] != k, (k, i)

def court(nom):
    return nom.split(" : ")[0]
def lib(e):
    d = f" ({e['date']})" if e["date"].strip() else " (date non donnée)"
    return f"{e['titre']}{d} — {e['adresse']}"
def ou(i):
    fam, n, nom = CLEF[i]
    return f"{fam} n° {n}"

# --- comptes recalculés -----------------------------------------------------------------------------------------------------
ms = [(e["indice"], m) for e in rel["travaux"] for m in e["mecanismes"]]
decr = [(i, m) for i, m in ms if not m["suggere_par_le_titre"]]
sugg = [(i, m) for i, m in ms if m["suggere_par_le_titre"]]
sans = collections.Counter(e.get("statut", "?") for e in rel["travaux"] if not e["mecanismes"])
cpt_fam = collections.Counter(m["famille"] for _, m in decr)
cpt_ep = collections.Counter(m["eprouve_contre_le_reel"] for _, m in decr)
cpt_prof = collections.Counter(e["profondeur_de_lecture"] for e in rel["travaux"])
cpt_sugg_fam = collections.Counter(m["famille"] for _, m in sugg)
notice = [e for e in rel["travaux"] if e["profondeur_de_lecture"] == "notice seule"]
n_notice_sugg = sum(1 for e in notice for m in e["mecanismes"] if m["suggere_par_le_titre"])
n_notice_decr = sum(1 for e in notice for m in e["mecanismes"] if not m["suggere_par_le_titre"])
n_notice_vide = sum(1 for e in notice if not e["mecanismes"])

out = []
w = out.append
w("# Matière première de l'auto-conception de l'organisme d'idéation — mécanismes publiés d'exploration, d'originalité, d'épreuve, de jugement, de mémoire, de sélection, de coût et d'auto-conception — v2\n")
w("Pièce servie telle quelle à des proposeurs. Elle décrit ce que dit un moissonnage de 630 travaux ; elle ne juge aucun mécanisme et ne dit pas lequel est bon. Version 2, écrite le 18 novembre 2026 par la contre-lecture neuve du catalogue (`docs/notes/matiere-premiere-auto-conception-v1/contre-lecture-catalogue-v1.md`), par `programmes/ecrire_matiere_v2.py`, à partir des mêmes entrées que la v1 : le relevé `releve-mecanismes-v1.json` et les regroupements `programmes/regroupements-v1/`, corrigés en mémoire. La v1 (`matiere-premiere-v1.md`, sha256 `98f63ecc…`) reste en place, inchangée (R12).\n")
w("## Changements par rapport à la v1\n")
w("1. **Section 3.** La v1 disait que le relevé « ne trouve l'assemblage dans aucun des systèmes recensés » pour les regroupements de 3.1 ; c'est faux pour douze d'entre eux : une machine de la section 2 y porte la même idée, rangée sous un regroupement voisin (chaque mécanisme n'est rangé qu'une fois). L'introduction dit maintenant ce que le programme calcule, et chacun des douze porte la ligne « Même idée chez une machine recensée ».")
w("2. **Section 2.** La définition « au moins deux mécanismes » était contredite par sept machines (huit en v2) qui n'ont qu'un mécanisme rangé ; la liste des machines est un choix codé dans le programme d'écriture, non une marque du relevé ; ShinkaEvolve y figure deux fois ; des systèmes complets du relevé n'y sont pas (nommés).")
w("3. **Regroupements.** 240.2 (machine de Darwin-Gödel : développement des agents au meilleur score immédiat, supposition contestée par les auteurs de la machine de Huxley-Gödel) était rangé sous « Crédit par la descendance » : il passe en « sélection n° 5 ». 562.0 (relecteurs jugés par l'impact réalisé, « non par l'imitation des humains ») passe de « jugement n° 12 » à « jugement n° 2 ». 472.2 (liens retenus qui réensemencent la mémoire, mécanisme et non dérive mesurée) passe de « mémoire n° 12 » à « mémoire n° 7 ».")
w("4. **Suggérés par le titre.** Cinq mécanismes connus par le seul titre étaient comptés comme décrits : 126.2, 236.2, 391.0, 391.1, 445.0. Ils passent en section 6.")
w("5. **Cloisonnement.** 552.0, 552.1 et 466.1 : exclue (famille exclue de cette pièce) ; ils sortent du catalogue, l'indice 552 passe en section 8. Le relevé v1 les porte encore, avec une proposition de 259.3 et une source de 439.0 et 439.1 qui relèvent de la même réserve : section 9.")
w("6. **Section 4.** 4.3 § 1 et § 5 complétés à la lettre de N-073 (phrases à ne plus écrire, citations obligatoires, deux indices contraires nommés) ; réserves de N-071 jointes au juge ; héritage récompensé rattaché à Wang et al. ; ajout de ce que N-059 et la décision sur la matière première des mentors disent de l'organisme ; lettre de l'invariant de N-053 signalée.")
w("7. **Section 5.** Comptes recalculés ; la question 10 disait à tort que les mécanismes des travaux lus sur notice seule sont tous en section 6.")
w("8. **Section 7.** Deux gloses de valeur du relevé retirées à l'affichage (221.0, 457.0).")
w("9. **Section 10, nouvelle.** Seize mécanismes absents du relevé, relevés par la contre-lecture dans dix travaux à lecture approfondie permise ou à PDF versé, avec chemin, empreinte et page.")
w("10. **Section 11, nouvelle.** Réserves de regroupement : mécanismes rangés sous un nom qui ne les décrit pas, et mêmes idées rangées sous plusieurs familles.\n")

w("## 0. Comment lire cette pièce\n")
w("- **Qui affirme quoi.** Chaque mécanisme est ce qu'*affirment les auteurs* de chaque travail, d'après la notice, le résumé, la page ou la lecture approfondie du dépôt selon la « lecture » indiquée. Rien n'est vérifié par nous : aucun chiffre n'est opposable avant lecture sur PDF empreinté, page citée (R7).")
for k in EPR:
    w(f"- **Éprouvé contre le réel : « {k} »** — {rel['legende'][k]}.")
w(f"- **Lecture** — {rel['legende']['profondeur de lecture']}.")
w(f"- **Suggéré par le titre** — {rel['legende']['suggéré par le titre']}. Ils sont en section 6.")
w(f"- **Absence** — {rel['legende']['absence']}. Une absence dans cette pièce veut seulement dire : non trouvé dans ce moissonnage, à la profondeur de lecture indiquée.")
w("- **Identifiants.** « 593.3 » veut dire : quatrième mécanisme (position 3) du travail d'indice 593 de la table fusionnée. Le relevé `releve-mecanismes-v1.json` donne, pour chaque identifiant, la phrase complète du mécanisme et sa source (chemin et empreinte sha256) ; **il porte encore des lignes écartées par cette version (section 9) et ne se sert pas tel quel aux proposeurs**. Un travail peut figurer sous plusieurs regroupements.")
w("- **Regroupement.** Les mécanismes décrits sont regroupés par ressemblance de ce qu'ils font ; chacun n'est rangé qu'une fois, si bien qu'une même idée peut apparaître sous deux regroupements de familles différentes (section 11). Le regroupement est un choix de lecture, rejouable par `programmes/ecrire_matiere_v2.py` ; il n'est pas une classification des auteurs.\n")
w("### Comptes\n")
w(f"- 630 travaux ; {sum(1 for e in rel['travaux'] if e['mecanismes'])} portent au moins un mécanisme ; {sum(sans.values())} n'en portent aucun : " + ", ".join(f"{sans[k]} « {k} »" for k in ['exclue', 'hors sujet', 'liste sans mécanisme', 'notice muette']) + " (section 8).")
w(f"- {len(ms)} mécanismes au total, dont **{len(decr)} décrits** et **{len(sugg)} suggérés par le titre** (comptés à part, jamais additionnés) ; trois lignes du relevé sont écartées par cloisonnement (section 9).")
w("- Mécanismes décrits par famille : " + " ; ".join(f"{k} {cpt_fam[k]}" for k in FAM8 + ["autre"]) + ".")
w("- Mécanismes décrits par éprouvé contre le réel (selon les auteurs) : " + " ; ".join(f"{k} {cpt_ep[k]}" for k in EPR) + ".")
w("- Travaux par lecture : " + " ; ".join(f"{k} {cpt_prof[k]}" for k in PROF) + ".")
w("- Trois travaux de la dernière tranche (indices 605, 612, 625) ont une lecture approfondie au dépôt qui n'a pas été ouverte pour cette pièce : ils sont relevés d'après l'entrée de la table seulement.\n")

# --- section 1 ---------------------------------------------------------------------------------------------------------------
w("## 1. Mécanismes distincts, par famille\n")
w("Format d'une ligne : *titre (date) — adresse · identifiant(s) du mécanisme · éprouvé contre le réel selon les auteurs · lecture · « machine » si le travail est l'un des systèmes de la section 2.*\n")
STAT = {}
for fam in FAM8:
    w(f"### Famille « {fam} »\n")
    for n, cl in enumerate(CL[fam], 1):
        ids = cl["ids"]
        par_travail = collections.OrderedDict()
        for i in sorted(ids, key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1]))):
            e, m = M[i]
            par_travail.setdefault(e["indice"], []).append((i, m))
        ep = collections.Counter(M[i][1]["eprouve_contre_le_reel"] for i in ids)
        pr = collections.Counter(T[k]["profondeur_de_lecture"] for k in par_travail)
        nm = sum(1 for k in par_travail if k in MACH)
        STAT[(fam, n)] = dict(nom=cl["nom"], n_trav=len(par_travail), n_mach=nm, ep=ep, hors=[k for k in par_travail if k not in MACH],
                              mesures=ep["oui, mesuré"], ids=ids)
        w(f"**{fam} n° {n} — {cl['nom']}**\n")
        w(f"{len(ids)} mécanismes, {len(par_travail)} travaux ({nm} sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : "
          + ", ".join(f"{k} {ep[k]}" for k in EPR if ep[k]) + ". Lecture : " + ", ".join(f"{PROF[k]} {pr[k]}" for k in PROF if pr[k]) + ".\n")
        for k, lst in par_travail.items():
            e = T[k]
            etiq = sorted({m["eprouve_contre_le_reel"] for _, m in lst})
            w(f"- {lib(e)} · {', '.join(i for i, _ in lst)} · {' / '.join(etiq)} · {PROF[e['profondeur_de_lecture']]}" + (" · machine" if k in MACH else ""))
        w("")

# --- section 2 ---------------------------------------------------------------------------------------------------------------
w("## 2. Machines : systèmes complets et les mécanismes qu'ils assemblent\n")
w("« Machine » veut dire ici : un système ou une boucle complète décrit comme tel par ses auteurs (ou par le dépôt de code), dont le relevé range au moins un mécanisme décrit. "
  "La liste est un choix de lecture, codé dans `programmes/ecrire_matiere_v1.py` et repris tel quel (listes `MACH_LUES` et `MACH_NOTICE`) : le relevé ne porte aucune marque « machine ». "
  f"Elle n'est pas exhaustive (R8) : des travaux du relevé décrits comme des systèmes complets par leur titre ou leur notice n'y sont pas, par exemple les indices {', '.join(str(k) for k in NON_RECENSES)} (titres en section 1). "
  "ShinkaEvolve y figure deux fois (article, indice 236 ; dépôt de code, indice 629). "
  f"{len(UN_SEUL)} machines n'ont qu'un mécanisme décrit dans le relevé (indices {', '.join(str(k) for k in UN_SEUL)}). "
  "Pour chaque machine : les mécanismes décrits qu'elle assemble, avec le regroupement où chacun se range (section 1) ; ses mécanismes suggérés par le titre (section 6) ou classés « autre » (section 7) ne sont pas repris ici.\n")
def ecrire_machine(k):
    e = T[k]
    items = [m for m in e["mecanismes"] if m["id"] in CLEF]
    if not items:
        return
    parts = [f"{CLEF[m['id']][0]} n° {CLEF[m['id']][1]} ({court(CLEF[m['id']][2])}) [{m['id']}, {m['eprouve_contre_le_reel']}]" for m in items]
    w(f"- **{e['titre']}** ({e['date']}) — {e['adresse']} — lecture : {PROF[e['profondeur_de_lecture']]}\n  - assemble : " + " ; ".join(parts))
w("### 2.1 Machines relevées d'après une lecture approfondie du dépôt\n")
for k in MACH_LUES:
    ecrire_machine(k)
w("\nAutres études lues en profondeur, qui ne sont pas des machines mais des protocoles d'étude (leurs mécanismes sont en section 1) : indices 98, 450, 456 et 581. L'indice 136, dont les pages 1 à 4 du PDF ont été relues pour le relevé, figure en 2.2 faute de fiche de lecture approfondie au dépôt.\n")
w("### 2.2 Machines relevées d'après la notice, le résumé ou la page (non opposable, R7)\n")
for k in MACH_NOTICE:
    ecrire_machine(k)
w("")

# --- section 3 ---------------------------------------------------------------------------------------------------------------
w("## 3. Mécanismes hors de toute machine\n")
w("Ce que le programme calcule, et rien de plus : en 3.1, les regroupements dont aucun des travaux qui y sont rangés n'est une machine de la section 2 ; en 3.2, les autres. "
  "Chaque mécanisme n'étant rangé qu'une fois, une machine peut porter la même idée sous un regroupement voisin : la contre-lecture l'a relevé pour douze regroupements de 3.1, marqués par une ligne « Même idée chez une machine recensée » (et quatre ressemblances plus lâches, marquées « Voisin chez une machine recensée »). "
  "« Hors de toute machine » ne dit donc ni « inédit », ni « absent des systèmes recensés » : le mécanisme peut figurer dans une machine recensée sous un autre regroupement, ou dans un système non recensé (R8).\n")
w("### 3.1 Regroupements dont aucun travail n'est une machine recensée\n")
n_hors = 0
for fam in FAM8:
    for n, cl in enumerate(CL[fam], 1):
        s = STAT[(fam, n)]
        if s["n_mach"]:
            continue
        n_hors += 1
        w(f"**{fam} n° {n} — {cl['nom']}** ({s['n_trav']} travaux ; éprouvé selon les auteurs : " + ", ".join(f"{k} {s['ep'][k]}" for k in EPR if s['ep'][k]) + ")\n")
        for k in s["hors"]:
            ids = [i for i in cl["ids"] if int(i.split('.')[0]) == k]
            w(f"- {T[k]['titre']} ({T[k]['date'].strip() or 'date non donnée'}) · {', '.join(ids)}")
        for etiquette, d in (("Même idée chez une machine recensée", MEME_IDEE), ("Voisin chez une machine recensée", VOISIN)):
            if (fam, n) in d:
                w(f"- *{etiquette}, rangée sous un autre regroupement :* " + " ; ".join(
                    f"{i} ({T[int(i.split('.')[0])]['titre'].split(':')[0]} : {g} ; sous « {ou(i)} »)" for i, g in d[(fam, n)]) + ".")
        nr = [k for k in s["hors"] if k in NON_RECENSES]
        if nr:
            w(f"- *Travail de ce regroupement décrit comme un système complet, non recensé en section 2 :* " + " ; ".join(f"{k} ({T[k]['titre'].split(':')[0]})" for k in nr) + ".")
        w("")
for k in list(MEME_IDEE) + list(VOISIN):
    assert STAT[k]["n_mach"] == 0, k
w("### 3.2 Regroupements portés à la fois par des machines et par d'autres travaux\n")
w("Pour chacun : nombre de travaux hors machine (liste complète en section 1, sans la marque « machine »).\n")
for fam in FAM8:
    for n, cl in enumerate(CL[fam], 1):
        s = STAT[(fam, n)]
        if s["n_mach"]:
            w(f"- {fam} n° {n} — {court(cl['nom'])} : {s['n_mach']} travaux sous forme de machine, {len(s['hors'])} hors machine ({', '.join(str(k) for k in s['hors']) or 'aucun'})")
w("")
print("regroupements de 3.1 :", n_hors)

# --- section 4 ---------------------------------------------------------------------------------------------------------------
D = ["decision-N-044-v1.md", "decision-N-045-v2.md", "decision-N-049-v1.md", "decision-N-050-v1.md", "decision-N-053-v1.md", "decision-N-058-v1.md",
     "decision-N-059-v1.md", "decision-N-064-v1.md", "decision-N-065-v1.md", "decision-N-067-v1.md", "decision-resserrement-juge-au-nul-v1.md",
     "decision-matiere-premiere-mentors-v1.md", "decision-N-073-revendications-apres-veille-exploration-idees-v1.md"]
w("## 4. Ce que l'organisme actuel fait déjà\n")
w("**Cette section est remplie d'après les décisions de Lazar nommées ci-dessous, et d'elles seules** : elle dit ce que ces décisions retiennent ou interdisent, non ce que le code ou les courses ont réalisé. Plusieurs énoncés valent « à partir de l'étape 2 » ou « sur devis » ; une décision qui retient un énoncé n'est pas une mesure faite. La décision sur la matière première des mentors est nommée N-072 au `CLAUDE.md` ; celle sur le juge au nul, N-071. Pièces lues, avec empreinte :\n")
for d in D:
    p = f"docs/decisions/{d}"
    w(f"- `{p}` — sha256 `{sha(p)}`")
w("")
w("### 4.1 Ce que les décisions disent que l'organisme est ou fait\n")
w("- **Un organisme qui se conçoit seul** sur un vivier de tâches à vérité connue, avec le droit de se réécrire ; sa méta-architecture est ensuite figée, et il répond à des questions nouvelles sans réentraînement ni réorganisation (N-044, énoncé 1). L'universalité se mesure sur des familles jamais vues à la conception, non sur des items inédits des familles de conception — **distinction que N-073 interdit de présenter comme nôtre** (section 4.3).")
w("- **Trois régimes de budget** (conception, usage, re-conception) : proposés à Lazar, en attente de son mot pour l'étape 1 (N-044, énoncé 2) ; **vivier de conception** à part de la banque scellée, identifiants disjoints du test et du test final (énoncé 3) ; le vivier existe en code dans le noyau de l'étape 1 (N-049, § 1) ; **questions ouvertes** posées aux organismes avant tout matériau, réponses archivées comme matière et jamais comme consigne (énoncé 4).")
w("- **Diversité des candidats** : trois bras à l'étape 2 (mission avec miroir fonctionnel ; contrainte câblée ; rien), le juge étant la seule pression ; un résultat négatif se publie (N-044, énoncé 5).")
w("- **Composition apprise** : nombre de parties, rôles, modèle par rôle (modèle de frontière ou instrument local entraîné), ordre des échanges, règle d'agrégation, mémoire transmise, part de budget (N-045 v2, énoncé 1) ; **coût dans le signal** rendu à l'organisme à côté de l'exactitude, score net gelé au préenregistrement (énoncé 2) ; **nécessité de la frontière mesurée** comme sortie, par rôle (énoncé 3) ; **voies bon marché avant la voie chère** : éliminations successives, matrices en cache, substituts à 8 milliards, affinage sur réponses filtrées ou préférences hors ligne, modèle de substitution du score, transitions depuis un tampon de rejeu, récompense dense par génération, distillation du concepteur figé (énoncé 4) ; **héritage d'une génération récompensé**, signal sur K générations avec K au moins 3 (énoncé 5) — principe publié par Wang et al. (machine de Huxley-Gödel, arXiv 2510.21614) : lettre à employer et citations obligatoires en 4.3 § 1 ; **deux expériences bon marché** avant tout concepteur entraîné : pilote de bruit puis « poids contre archive » (énoncé 6) ; **espaces de conception égaux** entre concepteur contraint et libre (énoncé 7). Inchangé : les modèles de frontière ne sont jamais entraînés, la vérité du test caché ne nourrit ni l'organisme ni un concepteur (énoncé 8). Ces énoncés valent à partir de l'étape 2 ; pour les courses actuelles, l'historique servi contient déjà toutes les générations passées (énoncé 5 ; « servir tout l'historique au concepteur » ne s'écrit pas comme une idée du programme, 4.3 § 1).")
w("- **Tâches fraîches** : à chaque génération, la part de test tirée dans un vivier plutôt que servie fixe ; banque sœur construite d'avance par quelqu'un qui n'a lu aucun score, lue une seule fois ; confirmation sur la banque scellée, famille tenue à l'écart (N-049 ; la construction de la banque sœur est une dépense sur devis, non décidée). **Part de test final lue une seule fois, à la fin de la boucle** (N-050).")
w("- **Composition des proposeurs jugée sur l'oracle du monde planté et sur le coût mesuré, seuls** ; le verdict du juge, aveugle à l'identité du proposeur, n'entre pas dans ce choix (N-058, point 1) ; l'invariant « aucun score de moniteur ni de juge dans l'entraînement ou la sélection de l'agent » vaut aussi pour l'organisme (N-053, point 5 — dont la lettre complète porte une exception qui relève d'une famille exclue de cette pièce ; N-065, point 4). La sélection des fiches par la sévérité du test survécu reste permise (N-058).")
w("- **Règles de course de l'organisme** (décision sur la matière première des mentors, § 1, point 2) : proposeurs de plusieurs familles ; aiguilleur sur la forme seulement ; juges croisés aveugles les uns aux autres ; mémoire anti-répétition ; aucune promotion décidée par un modèle ; verdicts du juge et témoins jamais servis aux proposeurs, sauf décision de Lazar, encore ouverte, sur la règle « note du juge montrée ou non aux proposeurs ».")
w("- **Affinage** (N-059) : témoins en générations d'étalonnage entières, à calendrier secret, et témoins silencieux à chaque génération de production, aucun témoin ne passant par un proposeur en production (point 1) ; un budget d'erreur par génération et un contrôle des fausses découvertes en fin de course, procédure à fixer sur devis (point 2) ; banque de familles inédites de confirmation distincte de la famille tenue à l'écart de l'évaluation finale (point 7) ; épreuve lue jusqu'au budget, partout, seuil de réfutation fixé par la course et jamais par le proposeur (point 11) ; taux par proposeur entre deux courses lus par le directeur seul, changement de composition fondé sur l'étalonnage seul (point 14).")
w("- **Juge statistique** : statistique calculée par l'orchestrateur hors de tout agent, à partir d'un engagement scellé avant que les données existent, contre un nul formé des lois connues (l'archive), avec contrôle des comparaisons multiples (N-064) ; après N-067, **ne reste revendiqué en propre que le nul formé des lois déjà connues** (O2 resserrée, O4 seul porteur de la revendication du juge) ; après N-071, ce nul d'archive est occupé dans ses deux moitiés séparément, **seule leur réunion reste revendicable** (nul formé de l'archive entière et croissante, mis en commun et ajusté avant le gel, dans une règle de promotion à garantie valide à tout instant, sur prédictions scellées, hors des agents), **sous deux réserves de N-071** : la défendabilité de ses composantes n'est pas tranchée (point 3) et « libre hors du dépôt » n'est pas déclarable (point 11) ; « lois prédictives et non rendements » n'est plus présenté comme une différence nette ; dans tout énoncé public, ne pas écrire que personne ne mesure l'apport d'une proposition de modèle de langue au-delà d'une mise en commun ajustée, mais dire que ce qui n'est pas trouvé est le nul désigné, l'archive, la règle de promotion et sa garantie (point 4).")
w("- **Place dans le programme** : l'organisme est un second terrain du papier C (juges de la recherche automatisée), et un atelier d'idées du programme : ses fiches sont du matériau, jamais une preuve ; tout usage décisif passe par un préenregistrement scellé (N-065, rôles 1 et 2). Le banc de tricheurs et l'attaque de Goodhart du juge (revendications O11 et O12 de N-064 et N-067) relèvent d'une famille exclue de lecture de contenu pour cette pièce : **exclue** ; voir `docs/decisions/decision-N-064-v1.md` et `docs/decisions/decision-N-067-v1.md`.")
w("")
w("### 4.2 Ce que les décisions retirent de ce qui était revendiqué comme propre (N-064, N-067, N-071)\n")
w("Plus revendiqués comme propres : le recours aux e-valeurs et à un seuil posé hors des agents ; la statistique calculée hors des agents ; l'engagement scellé par empreinte ; le contrôle des comparaisons multiples ; le principe d'architecture « séparer qui propose de qui juge » (O1) ; le sceau par empreinte (O3) ; le gel avant lecture et l'interdit du repli silencieux comme idées (O17) — publiés dans leur principe ou occupés en partie, citations obligatoires dans tout texte qui présente l'organisme : POPPER, Dwork et al., Blum et Hardt (« The Ladder »), Co-Scientist, et les pièces nommées par N-067 (§ 6) et N-071 (point 5).\n")
w("### 4.3 Ce que N-073 interdit désormais de présenter comme nôtre\n")
w("Lettre de `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (version de travail, contre-lecture à venir selon son texte) :\n")
w("1. **Héritage d'une génération récompensé** (N-045 v2, énoncé 5) : principe occupé par la machine de Huxley-Gödel (Wang et al., arXiv 2510.21614). Ne plus écrire comme idée ou constat du programme : « récompenser l'héritage d'une génération », « créditer une génération (ou un agent) par les résultats de sa descendance », « le mérite d'une génération inclut ce que ses descendants obtiennent » ; « le score immédiat est un mauvais guide du potentiel d'amélioration à long terme », « la sélection gloutonne sur le score immédiat est trop courte », « exclure le bandit à un pas » présenté comme un apport ; « un signal sur plusieurs générations, tronqué à K et actualisé » présenté comme une idée ; « faire compter dans le mérite d'une génération ce qu'elle construit et qui ne sert qu'aux suivantes », quel que soit l'objet ; « ce qui conçoit est jugé sur plusieurs générations » quand ce qui conçoit est sélectionné ; « servir tout l'historique au concepteur » (attribué par les auteurs à Robeyns et al.). Lettre retenue pour tout texte sortant : celle de N-073 § 1, qui commence par « Suivant Wang et al. (2025) ». Citations obligatoires dans tout texte qui touche à l'énoncé 5 : Wang et al. (arXiv 2510.21614) ; Zhang, Hu, Lu, Lange, Clune, « Darwin Gödel Machine » (arXiv 2505.22954) ; Robeyns, Szummer, Aitchison (arXiv 2504.15228) ; Sutton et Barto ; Schmidhuber et Zhao (1996), Schmidhuber, Zhao et Wiering (1997), Kirsch et Schmidhuber (2022) — ces trois derniers à lire sur source avant de les citer. Restent décrits sans être dits nouveaux ni propres : les objets (mémoire transmise, sondes et adaptateurs servis à la génération suivante), le concepteur entraîné avec le coût dans le signal, la question causale « l'archive héritée cause-t-elle les découvertes ? ». Indice contraire à dire avec la prémisse : chez Qin et al. (arXiv 2611.05108), ce qui est légué rapporte surtout au départ (chiffres : N-073 § 1).")
w("2. **« Le séquentiel doit battre le meilleur de N tirages, à budget égal »** (N-045 v2, énoncés 4 et 6) : protocole occupé (Oved et al., arXiv 2610.23977 ; compagnon arXiv 2609.19799), issue occupée en partie ; les gardes de la porte (familles tenues à l'écart, témoin « un modèle, vote à k ») sont très probablement prises aussi, d'après des notices seulement (à lire sur PDF avant toute phrase publique, Gideoni et al. et Wang et al. d'abord). La porte reste une condition du programme, présentée comme **pratique publiée, citée** ; six lignes sont gelées dans tout préenregistrement de cette porte (N-073 § 2).")
w("3. **« Familles inédites contre items inédits des familles vues »** (N-044) : distinction faite en mots propres par Srikanth et al. (arXiv 2609.26457, p. 6) ; elle se cite. Ce qui se décrit comme mise en œuvre, sans priorité : la mesure par famille préenregistrée.")
w("4. **Banque sœur** (N-049) : elle sépare « adapté aux textes » de « adapté à la famille telle que ce générateur la rend », non de « adapté au générateur » (Zhu et al., « Bad Genius », arXiv 2609.18366, p. 5 : contredit faible) ; le générateur est audité avant toute banque sœur. La lecture unique du lot final est une pratique ancienne, citée.")
w("5. **Proposeurs de plusieurs fournisseurs** (N-045 v2, énoncés 1 à 3 ; N-067) : l'énoncé reste « voisin » ; tout texte qui présente la diversité des fournisseurs cite l'indice contraire de Ferreira, Liu, Zheng (« Beyond Symmetric Agents », arXiv 2609.35875) avec sa borne de terrain (réponses fermées, petits modèles ouverts, aucune production d'idées, aucun modèle de frontière), à côté des deux déjà au dépôt : le tirage au hasard (arXiv 2611.04420) et l'a priori fixe sans modèle (CADS). À l'étape 2, sur devis : deux bras témoins jugés sur l'oracle du monde planté et le coût (N-073 § 5).")
w("")
w("Les restrictions antérieures (« lois prédictives et non rendements » ; e-valeurs ; calcul hors des agents ; sceau ; etc.) sont en 4.2. Rien dans cette section n'est une déclaration « libre » : « non trouvé dans les pièces lues » ne veut jamais dire « trou du champ » (R8).\n")

# --- section 5 ---------------------------------------------------------------------------------------------------------------
w("## 5. Questions ouvertes\n")
w("Ce sont des questions posées par la matière, jamais des affirmations d'absence : chacune dit ce que ce moissonnage montre et ce qu'il ne montre pas. Les comptes viennent du relevé corrigé de la v2, recalculés par programme.\n")
nul = [(f, n) for (f, n), s in STAT.items() if s["mesures"] == 0]
w(f"1. **Regroupements sans aucun mécanisme marqué « oui, mesuré »** ({len(nul)} sur {len(STAT)}) : " + " ; ".join(f"{f} n° {n} ({court(STAT[(f, n)]['nom'])})" for f, n in nul) + ". Question : ces mécanismes sont-ils éprouvés quelque part hors de ce moissonnage, et sur quelle vérité ?")
mm = [m for k in MACH for m in T[k]["mecanismes"] if m["id"] in CLEF]
w(f"2. **Éprouvé contre le réel et machines.** Parmi les travaux sous forme de machine (section 2), la part de mécanismes éprouvés « oui, mesuré » est {sum(1 for m in mm if m['eprouve_contre_le_reel'] == 'oui, mesuré')} sur {len(mm)} (selon les auteurs). Question : quels mécanismes d'une machine sont isolés par une ablation, et lesquels ne sont éprouvés qu'ensemble ? (Le relevé note plusieurs cas d'absence d'ablation : indices 112 et 593 ; une ablation publiée, chez Fork-and-Flush, indice 13, est relevée en section 10.)")
w("3. **Largeur et profondeur à budget apparié.** Le regroupement « coût n° 3 » et le regroupement « coût n° 5 » portent les comparaisons à dépense totale égale et les témoins à calcul apparié. Question : quelle part de ces comparaisons distingue le gain d'une architecture du gain d'un calcul d'inférence ajouté, sur des familles de tâches tenues à l'écart ?")
w("4. **Vérité de l'épreuve.** Le relevé range sous « épreuve » des vérités très différentes (monde planté, futur, redécouverte, exécutable ; l'avis d'experts est rangé sous « jugement »). Question : un même mécanisme d'exploration garde-t-il son classement quand on change la vérité de l'épreuve, à coût égal ?")
w("5. **Originalité.** La nouveauté se mesure par distance dans un espace, par antériorité, par juge ou par écart de croyance. Question : ces quatre mesures s'accordent-elles sur les mêmes idées, et laquelle suit un résultat réel obtenu plus tard ?")
w("6. **Diversité.** Le relevé porte des diagnostics d'effondrement et des remèdes dont plusieurs sont notés sans effet par leurs auteurs (exploration n° 12 et n° 15). Question : quels remèdes survivent quand on juge sur l'oracle d'un monde planté et sur le coût plutôt que sur un juge de nouveauté ?")
w("7. **Mémoire.** La mémoire se mesure surtout par comparaison « avec / sans » ; plusieurs mesures du regroupement « mémoire n° 11 » ne trouvent pas, selon leurs auteurs, de gain constant au résultat final. Question : que lègue réellement une génération à la suivante, au départ, à mi-budget et à l'échéance, une fois l'effet de départ séparé ?")
w("8. **Jugement.** Les juges sont mesurés contre des experts, des issues ou des preuves traçables ; plusieurs travaux du regroupement « jugement n° 6 » rapportent des erreurs corrélées entre juges modèles (selon les auteurs). Question : quelle composition d'un collège de juges garde un nombre de votes effectifs supérieur à celui d'un seul juge sur des idées de recherche ?")
w("9. **Auto-conception.** Le relevé range des systèmes qui se réécrivent (auto-conception n° 1 à 4). D'après la lecture approfondie de l'indice 112, relayée par N-073 (§ 3), sa mesure sur une famille inédite tient en une tâche et trois graines. Question : que devient une auto-modification sélectionnée quand la famille de tâches de la mesure est inédite à la conception, avec plus de familles et de graines ?")
w(f"10. **Entrées lues sur notice seule.** {len(notice)} travaux ne sont lus que par le titre ou une courte description de la table (souvent un condensé de recherche) : {n_notice_sugg} de leurs mécanismes sont suggérés par le titre (section 6), {n_notice_decr} sont décrits d'après cette courte description (section 1, marque « notice seule »), {n_notice_vide} de ces travaux n'en portent aucun. Ce sont des hypothèses de lecture. Question : lesquels, lus sur PDF, tiennent ?")
w("11. **Limites du moissonnage.** Une seconde passe de recherche, limitée à la périphérie du juge (finance empirique, découverte de modèles, billets de laboratoire), est accordée par N-073 (§ 7) après le 22 novembre 2026 ; les voisins nommés par N-073 à lire sur PDF ne le sont pas encore. Les lectures approfondies des travaux d'indices 605, 612 et 625 n'ont pas été ouvertes pour cette pièce.")
w("")

# --- section 6 ---------------------------------------------------------------------------------------------------------------
w("## 6. Mécanismes suggérés par le titre (comptés à part)\n")
w(f"{len(sugg)} mécanismes dont la phrase du relevé dit qu'ils sont inférés du seul titre ou d'après le titre (dont les cinq reclassés par la v2). Ce sont des hypothèses de lecture : ni description des auteurs, ni mesure. Par famille : " + " ; ".join(f"{k} {cpt_sugg_fam[k]}" for k in FAM8 + ["autre"]) + ".\n")
for fam in FAM8 + ["autre"]:
    lst = [(e, m) for e in rel["travaux"] for m in e["mecanismes"] if m["suggere_par_le_titre"] and m["famille"] == fam]
    if not lst:
        continue
    w(f"### {fam} ({len(lst)})\n")
    for e, m in lst:
        w(f"- {lib(e)} — {m['id']} — {m['eprouve_contre_le_reel']} — lecture : {PROF[e['profondeur_de_lecture']]} — {m['mecanisme_en_une_phrase']}")
    w("")

# --- section 7 ---------------------------------------------------------------------------------------------------------------
w("## 7. Mécanismes classés « autre » : reclassés ou justifiés\n")
w("Quarante mécanismes étaient classés « autre » dans les lots. Neuf ont été reclassés dans une des huit familles, un a été retiré (cloisonnement), trente sont conservés avec une justification (dix-neuf ci-dessous, onze suggérés par le titre en section 6 ; table `programmes/corrections-v1.json`, correction 4 de la première contre-lecture). Deux gloses de valeur du relevé (221.0, 457.0) sont retirées à l'affichage.\n")
for e in rel["travaux"]:
    for m in e["mecanismes"]:
        if m["famille"] == "autre" and not m["suggere_par_le_titre"]:
            w(f"- {lib(e)} — {m['id']} — {m['eprouve_contre_le_reel']} — lecture : {PROF[e['profondeur_de_lecture']]} — {m['mecanisme_en_une_phrase']} — *{m['justification_autre']}*")
w("")

# --- section 8 ---------------------------------------------------------------------------------------------------------------
w("## 8. Travaux sans mécanisme relevé\n")
w("Pour chacun, le statut dit pourquoi. Les travaux « exclue » relèvent de familles exclues de toute lecture de contenu pour cette pièce : seuls l'indice, le statut et le chemin sont donnés.\n")
for e in rel["travaux"]:
    if not e["mecanismes"]:
        st = e.get("statut", "?")
        if st == "exclue":
            w(f"- indice {e['indice']} — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[{e['indice']}]")
        else:
            w(f"- indice {e['indice']} — {st} — {lib(e)}")
w("")

# --- section 9 ---------------------------------------------------------------------------------------------------------------
w("## 9. Retraits, exclusions et pièces\n")
w("- Retraits de la v1 : " + " ; ".join(f"indice {r['indice']} (correction {r['correction']})" for r in rel["retraits"]) + " — lignes retirées du relevé parce qu'elles reprenaient une facette d'une famille exclue ; leur contenu n'est pas reproduit.")
w("- Écartés par la contre-lecture du catalogue : 552.0, 552.1 (l'indice 552 passe en section 8) et 466.1 — **exclue**. Ils restent dans `releve-mecanismes-v1.json`, qui porte aussi, sous la même réserve, la seconde proposition de 259.3 et une source de 439.0 et 439.1 (`lecture-01-v1.md:96`, lecture fermée à cette contre-lecture, dont le relevé dit qu'elle porte sur une pièce exclue) : le relevé v1 ne se sert pas tel quel aux proposeurs avant une version qui les retire.")
for p in ["releve-mecanismes-v1.json", "programmes/corrections-v1.json", "programmes/fusionner_v1.py", "programmes/ecrire_matiere_v1.py", "programmes/ecrire_matiere_v2.py", "matiere-premiere-v1.md"]:
    w(f"- `{ICI}{p}` — sha256 `{sha(ICI + p)}`")
w(f"- Contre-lecture qui fonde cette version : `{ICI}contre-lecture-catalogue-v1.md` (empreinte dans son compagnon `.sha256`).")
w("")

# --- section 10 --------------------------------------------------------------------------------------------------------------
V = "docs/notes/veille-exploration-idees-v1/"
P = "docs/sources/pdf/veille-exploration-idees-v1/"
OUBLIS = [
 (593, "épreuve", "oui, mesuré", "Épreuve du critère de sélection contre la productivité observée de la lignée : pour chaque nœud de l'arbre final, la cible est la meilleure moyenne de sa descendance, nœud exclu ; le prédicteur de lignée est privé des évaluations du nœud et du sous-arbre de l'enfant qui contient ce maximum, contre la fuite de la cible ; corrélations pondérées 0,778 contre 0,285 et 0,444 sur 60 tâches de SWE-bench Verified, 0,626 contre 0,383 et 0,274 sur Polyglot (table 1 p. 8, annexe D p. 19) ; les auteurs disent eux-mêmes que l'agrégat met en commun plus d'échantillons (p. 6), effet que la mesure ne sépare pas.",
  [(V + "lecture-05-v1.md", "section 5"), (V + "lecture-huxley-godel-v2.md", "section 2")]),
 (593, "sélection", "inconnu", "Choix de l'agent rendu : celui dont un quantile de la loi a posteriori sur ses seuls résultats propres est le plus haut (ε = 1 dans les expériences, p. 7) ; selon la lecture Huxley-Gödel v2, la règle écrite ne départage personne à ε = 1 et le papier ne dit pas comment l'agent final a été choisi en pratique.",
  [(V + "lecture-huxley-godel-v2.md", "section 2"), (V + "lecture-05-v1.md", "section 3")]),
 (593, "coût", "oui, affirmé", "Biais de l'exécution asynchrone nommés par les auteurs : les premières expansions finies captent les évaluations (corrigé en développant cinq fois l'agent initial) ; les tâches faciles finissent plus tôt et gonflent la moyenne des agents peu évalués, biais « barely observed » au-delà de 50 évaluations (p. 17).",
  [(V + "lecture-huxley-godel-v2.md", "section 2")]),
 (593, "mémoire", "oui, affirmé", "Des agents écrivent leurs modifications dans un fichier de différences que leurs descendants héritent et réécrivent (différences emboîtées), lu par les auteurs comme un format qui inspire une amélioration à long terme ; observation sans mesure (annexe F, p. 21).",
  [(V + "lecture-05-v1.md", "section 3"), (V + "lecture-huxley-godel-v2.md", "section 2")]),
 (112, "épreuve", "oui, affirmé", "Un mécanisme décrit de l'agent final est sans effet de l'aveu des auteurs : sa règle de pénalité « never changed which candidate the agent selected » (p. 10) ; la lecture 08 en tire un audit sur processeur : rejouer chaque mécanisme accepté pour voir s'il change une seule décision.",
  [(V + "lecture-08-v1.md", "sections 4 et 7")]),
 (112, "épreuve", "oui, mesuré", "Transfert des points de contrôle figés à d'autres modèles (annexe C, p. 26 ; trois modèles en tout), budget par tâche relevé de 5 à 20 dollars : selon les auteurs, l'avance de l'agent final sur l'agent de départ se transfère, sauf sur MLE-Bench avec le modèle le plus fort, où il reste à une erreur type.",
  [(V + "lecture-08-v1.md", "section 3.1")]),
 (112, "sélection", "oui, mesuré", "Écart chiffré entre le signal public vu par l'agent et la note privée : environ un quart des réécritures rejetées et notées dépassaient le tenant sur le signal public et ont été rejetées sur la note privée (p. 26).",
  [(V + "lecture-08-v1.md", "section 3.2")]),
 (121, "originalité", "oui, mesuré", "La référence informée par les résultats passés n'est pas monotone : elle retire 45,6 ± 15,9 surprises par lancement de 200 mais en crée 13,7 ± 4,3 nouvelles (p. 5) ; même quand l'archive déplace fortement la croyance, 14 à 24 % des hypothèses restent surprenantes (figure 8, p. 14) ; les auteurs disent qu'elle peut écarter des hypothèses qui méritaient d'être reprises (p. 10).",
  [(V + "lecture-04-v1.md", "sections 3 et 4.1")]),
 (121, "originalité", "oui, mesuré", "Mesure de la diversité des hypothèses : la similarité cosinus moyenne par paires sépare les variantes (0,518 à 0,527 contre 0,448 à 0,453) ; le volume de l'enveloppe convexe « is unable to provide meaningful discrimination » (p. 8, p. 15).",
  [(V + "lecture-04-v1.md", "section 3")]),
 (57, "épreuve", "inconnu", "Borne de précision jointe au score : un gain de « vrai en excès » ne compte que si la précision reste au moins à 0,8 fois celle du bras comparé (p. 5-6) ; la borne elle-même n'est pas éprouvée à part.",
  [(V + "lecture-03-v1.md", "section 3")]),
 (57, "originalité", "oui, affirmé", "Le panel qui porte le déjà-su doit être au moins aussi informé que le générateur : un générateur qui se souvient de plus que son panel est crédité pour du rappel et non du raisonnement (p. 16, recommandation des auteurs) ; la lecture 03 en tire la même réserve pour une archive de lois moins informée qu'un proposeur.",
  [(V + "lecture-03-v1.md", "section 5.1")]),
 (450, "jugement", "oui, mesuré", "Les probabilités que l'agent déclare avant les données sont mal étalonnées : pentes de 0,36, 0,12 et 0,11 contre 1 selon le modèle (p. 12), résultat préspécifié selon la lecture 02.",
  [(V + "lecture-02-v1.md", "sections 3 et 5")]),
 (13, "épreuve", "oui, mesuré", "Ablation des deux composants sur 11 tâches : vidage du contexte seul 0,55, bifurcation seule 0,57, les deux 0,71, contre 0,45 pour la course unique (score normalisé moyen, tableau 2) ; selon les auteurs, aucun des deux seul ne porte l'effet entier, la bifurcation apportant un peu plus.",
  [(P + "citations-arxiv-2610.07447v1.pdf", "p. 6")]),
 (13, "coût", "oui, mesuré", "Calendrier fixe plutôt que détection de plateau : une première ronde de quatre agents depuis un espace vide, puis deux bifurcations déclenchées à 33 % et 66 % du budget, chaque branche recevant environ 6 % du budget (sensibilité en annexe D, non lue ici) ; écart-type normalisé moyen des résultats 0,16 contre 0,26 (course unique) et 0,21 (meilleur de 4).",
  [(P + "citations-arxiv-2610.07447v1.pdf", "p. 5 et 6")]),
 (10, "mémoire", "oui, mesuré", "Un « réducteur » décide à chaque tour quels candidats l'agent voit dans son espace de travail et quelle session il poursuit ; chaque configuration comparée (agent seul, agents parallèles, équipe qui communique, oubli) est un réglage de ce réducteur (section 3.3 et figure 3).",
  [(P + "citations-arxiv-2610.20563v1.pdf", "p. 5")]),
 (10, "coût", "oui, mesuré", "Témoin apparié sur l'état : depuis le même état plafonné, les 30 propositions suivantes par agent continuent les mêmes sessions ou oublient ; selon les auteurs, l'oubli monte plus haut en moyenne et coûte moins, le contexte étant plus court (figure 4) ; 32 oublis sur 36 mènent à un nouveau meilleur candidat dans la manche suivante, l'essentiel du gain venant du premier (tableau 2).",
  [(P + "citations-arxiv-2610.20563v1.pdf", "p. 6 et 7")]),
]
w("## 10. Mécanismes absents du relevé v1, relevés par la contre-lecture\n")
w("Lus dans dix travaux : les huit à lecture approfondie permise (57, 98, 112, 121, 450, 456, 581, 593) et deux à PDF versé dont le relevé n'avait lu que les premières pages (10, 13). Rien à ajouter pour 98, 456 et 581 au-delà de détails. Même règle que le reste de la pièce : affirmations des auteurs selon la lecture citée, non opposables (R7). Sans identifiant de relevé : à verser au relevé dans sa prochaine version.\n")
for k, fam, ep, txt, srcs in OUBLIS:
    assert fam in FAM8 and ep in EPR and k in T
    s = " ; ".join(f"`{p}` (sha256 `{sha(p)}`), {d}" for p, d in srcs)
    w(f"- **{T[k]['titre']}** (indice {k}) — {fam} — {ep} — lecture : {'lecture approfondie' if k in (57, 112, 121, 450, 593) else 'PDF versé, pages citées'} — {txt} — source : {s}")
w("")

# --- section 11 --------------------------------------------------------------------------------------------------------------
RESERVES = [
 "**Mêmes idées sous plusieurs familles** (à ne pas compter comme idées distinctes) : « exploration n° 11 » (diagnostics de l'effondrement de la diversité) et « originalité n° 5 » (diversité et homogénéité des sorties) ; « coût n° 1 » (filtrer avant d'exécuter), « sélection n° 7 » (tri avant exécution par un prédicteur entraîné) et « jugement n° 7 » (juge ou vérificateur entraîné) ; « épreuve n° 6 » (séparer le signal de recherche de la mesure finale) et « épreuve n° 11 » (évaluation sans fuite).",
 "**épreuve n° 3 (redécouverte)** : 490.0 n'est pas une redécouverte ; le relevé lui-même dit que la direction est donnée et que la veille le classe « exécution, pas idéation » ; la barre est fixée par le scientifique (490.1).",
 "**originalité n° 6 (contamination)** : 260.1 décrit un raccourci lexical et une composition des données d'un banc de jugement, non une contamination par les données d'entraînement ; il relève d'une base simple (« épreuve n° 7 »). 98.4, rangé en « épreuve n° 11 », est au contraire une garde contre la mémorisation (noms neutres).",
 "**coût n° 10 (le coût entre dans la preuve)** : 472.3 nomme le coût d'une boucle de fond (« taxe de rêverie ») sans le faire entrer dans un seuil de preuve.",
 "**coût n° 7 (rendement décroissant mesuré)** : 129.1 dose le raisonnement coûteux (allocation), éprouvé « inconnu ».",
 "**auto-conception n° 3 (procédure d'amélioration modifiable)** : 299.0 optimise le critère d'évaluation lui-même par agrégation d'objectifs écrits par des modèles ; ce n'est pas l'agent qui modifie sa procédure d'amélioration.",
 "**épreuve n° 13 (environnements et bancs)** : 169.0 est une méthode qui boucle hypothèses et expériences par mise à jour bayésienne, non un environnement ni un banc.",
 "**mémoire n° 2 (archive relue avant de proposer)** : pour la machine de Huxley-Gödel (593.4), l'arbre est lu par la règle de sélection, non par le proposeur (lecture 05, section 4).",
 "**mémoire n° 3 (trajectoire lue par le contrôleur ou le proposeur)** : 152.0 est un jeu de trajectoires dont l'usage n'est pas précisé par la notice.",
 "**mémoire n° 7 (base partagée entre agents et sessions)** : 157.1, 309.0 et 524.1 sont des archives tirées de la littérature ou de dépôts, servies comme données ; rien n'y est partagé entre agents.",
 "**exploration n° 14 (un seul agent, une seule lignée)** : pour 254.0, la notice ne dit pas que la chaîne suit une seule lignée.",
 "**sélection n° 8 (choix de la prochaine direction)** : 534.1 décrit l'admission d'une croyance dans l'état, non le choix de la suite.",
 "**épreuve n° 10 (dispersion)** : 145.2 dit que tous les lancements sont rapportés sans sélection humaine ; ce n'est pas une mesure de dispersion.",
 "**jugement n° 1 (préférences d'experts)** : 262.0 et 559.0 prennent pour vérité la vélocité de citation ou des suites documentées (vérité différée, « jugement n° 2 ») ; 63.0 et 412.0 apprennent un goût (juge entraîné) ; 260.0 audite un banc par une règle triviale (base simple) ; 51.1 porte des préférences partagées entre modèles juges (« jugement n° 6 »).",
 "**jugement n° 15 (évaluer l'ensemble ou le processus)** : seuls 522.0 et 523.0 répondent au nom ; 159.1, 163.0, 309.2, 483.0 et 526.0 sont des bancs d'idéation dont la notation n'est pas précisée ou qui comparent à des publications.",
 "**originalité n° 5 (diversité)** : 160.1 compare la nouveauté avec et sans structure, non la diversité.",
]
w("## 11. Réserves sur les regroupements (contre-lecture)\n")
w("Regroupements dont un ou plusieurs membres ne répondent pas au nom (phrases complètes au relevé) ; les trois déplacements faits par la v2 sont listés en tête. Ce sont des choix de lecture, comme les regroupements eux-mêmes.\n")
for r in RESERVES:
    w(f"- {r}")
w("")

(RACINE / (ICI + "matiere-premiere-v2.md")).write_text("\n".join(out) + "\n", encoding="utf-8")
txt = "\n".join(out) + "\n"
print("comptes v2 :", dict(travaux_avec_mecanisme=sum(1 for e in rel['travaux'] if e['mecanismes']), sans=dict(sans), total=len(ms), decrits=len(decr), suggeres=len(sugg),
      par_famille=dict(cpt_fam), par_eprouve=dict(cpt_ep)))
print("machines à un seul mécanisme :", UN_SEUL)
print("écrit matiere-premiere-v2.md :", txt.count("\n"), "lignes,", len(txt), "caractères, sha256", hashlib.sha256(txt.encode("utf-8")).hexdigest())
