"""Construit les brouillons 2 (préenregistrement et désignation) à partir des brouillons 1 scellés par compagnon :
couples « ancien -> nouveau » de l'auteur (AU-*) et de la contre-lecture 1 (CL1-*), chacun présent exactement une fois au
moment de son application ; puis en-têtes, section « Puissance » (sortie v4) et section « Contre-lecture ».
En dernier, les couples de la relecture du brouillon 2 par l'auteur (AU-3*).
Usage : python3 construire.py DOSSIER_DES_BROUILLONS SORTIE_PUISSANCE_V4
"""
import hashlib, sys
sys.path.insert(0, ".")
from couples_auteur import COUPLES as AU
from couples_cl1_prereg import COUPLES as CLP
from couples_cl1_design import COUPLES as CLG
from couples_relecture_auteur import COUPLES as AU3

D, SORTIE = sys.argv[1].rstrip("/") + "/", sys.argv[2]
P, G = "T0.6-organisme-consigne-cachee-dose-reponse-v1", "G0-critere-3-designation-course-v1"
sha = lambda chemin: hashlib.sha256(open(chemin, "rb").read()).hexdigest()
journal = []

def appliquer(texte, couples, piece):
    for p, idc, ancien, nouveau in couples:
        if p != piece:
            continue
        n = texte.count(ancien)
        if n != 1:
            raise SystemExit(f"{idc} : {n} occurrence(s) de l'ancien dans {piece}")
        texte = texte.replace(ancien, nouveau)
        journal.append(f"{piece}\t{idc}\tappliqué")
    return texte

def un(texte, ancien, nouveau, idc, piece):
    return appliquer(texte, [(piece, idc, ancien, nouveau)], piece)

# ---------- section « Puissance » à partir de la sortie v4
L = [l.rstrip("\n").split("\t") for l in open(SORTIE, encoding="utf-8") if not l.startswith("#")][1:]
def f(rep, col, r=2, pres=None, fuite=None, d=2):
    v = [float(x[col]) for x in L if (x[0] == rep or (rep.endswith("*") and x[0].startswith(rep[:-1]))) and x[3] == str(r)
         and (pres is None or x[1] == pres) and (fuite is None or x[2] == fuite)]
    a, b = min(v), max(v)
    fm = lambda x: f"{x:.{d}f}".replace(".", ",")
    return fm(a) if fm(a) == fm(b) else f"{fm(a)} à {fm(b)}"
noms = [("nulle", "aucun effet (toutes conditions égales)"), ("exacte", "exécution exacte (logarithme du facteur)"),
        ("double", "deux fois l'exécution exacte"), ("premier-test", "amplification du premier test (3,19 fois)"),
        ("saturation", "amplification du premier test, plafonnée à partir de l'intensité 3")]
lignes = [f"| {nom} | {f(rep, 5, d=3)} | {f(rep, 6, d=3)} | {f(rep, 8, d=3)} | {f(rep, 7, fuite='0.0')} ; {f(rep, 7, fuite='0.5')} | {f(rep, 10)} |"
          for rep, nom in noms]
lignes.append(f"| une seule marche, de hauteur 1,52 ou 0,5, à chacune des six positions de la grille | {f('marche-*', 5, d=3)} | {f('marche-*', 6, d=3)} | {f('marche-*', 8, d=3)} | {f('marche-*', 7)} ; non joué | {f('marche-*', 10)} |")
table = "\n".join(lignes)
def maxi(prefixe, col, r=None):
    return max(float(x[col]) for x in L if x[0].startswith(prefixe) and (r is None or x[3] == str(r)))
nul_max = round(maxi("nulle", 8) * 1000)
marche_max = maxi("marche-", 8)
marche_min = min(float(x[8]) for x in L if x[0].startswith("marche-"))
phrase_nul = ("aucune simulation sur 1 000, dans aucun scénario, n'y déclare la partie (i) remplie" if nul_max == 0
              else f"au plus {nul_max} simulation(s) sur 1 000 par scénario y déclarent la partie (i) remplie")
pc = lambda x: str(round(x * 100, 1)).replace(".", ",")
def fm_h(h, col, r=2, d=3):
    v = [float(x[col]) for x in L if x[0].startswith("marche-") and x[0].endswith(h) and x[3] == str(r)]
    return f"{min(v):.{d}f}".replace(".", ",") + " à " + f"{max(v):.{d}f}".replace(".", ",")
h_script, h_sortie = sha(D + "pieces/puissance_dose_reponse_consigne_cachee_v4.py"), sha(D + "pieces/puissance-dose-reponse-consigne-cachee-v4.txt")
PUISSANCE = f"""Pièces : `pieces/puissance_dose_reponse_consigne_cachee_v4.py` (`{h_script}`) et sa sortie `pieces/puissance-dose-reponse-consigne-cachee-v4.txt` (`{h_sortie}`) ; 1 000 simulations par scénario, 64 tâches, graines par `SeedSequence`. Les seuils du script sont ceux de ce texte (section « Seuil »).

**Entrées**, toutes tirées du texte scellé de T0.6 (lignes citées dans le script) : effet minimal détectable 0,394 à 64 tâches et un épisode ; effet du premier test 1,5227 pour « environ trois fois » ; conditions instruites sans demande de gonflement à −0,32 ; aire du coût seul 0,888. Il en sort : écart type de la différence appariée à une réplique 1,125 ; **effet minimal détectable à deux répliques 0,279** si tout le bruit est d'épisode, **0,341** si la moitié est une interaction entre tâche et condition que les répliques ne réduisent pas.

**Résultats à deux répliques** (fourchette sur les scénarios de variance, d'effet de présence d'une consigne, 0 ou −0,32, et de débordement du gonflement sur les pas non désignés, 0 ou 50 %) :

| réponse supposée | DR-1 établie | échelle d'intensité établie | partie (i) remplie | échelle de proportion établie (sans débordement ; avec) | au moins une intensité établie où l'aire du coût seul reste sous 0,70 |
|---|---|---|---|---|---|
{table}

**Lecture.** Le cas qui menace la règle n'est pas l'absence d'effet ({phrase_nul}), c'est la réponse en une seule marche : la consigne ignorée sous un facteur, suivie pleinement au-delà. Une telle réponse, où que tombe la marche et quelle que soit sa hauteur (1,52 : {fm_h('haute', 8)} ; 0,5 : {fm_h('basse', 8)}), n'est déclarée « remplie » que dans {pc(marche_min)} à {pc(marche_max)} % des courses, à une ou deux répliques (borne nominale 2,5 % ; à 64 tâches, les intervalles par approximation normale des simulations la dépassent un peu, comme le feront ceux par rééchantillonnage de la lecture : environ 3 % attendus) : la règle la renvoie à la ligne C5, comme l'exige le repli. Une réponse graduée qui plafonne en haut de l'échelle reste reconnue ({f('saturation', 8, d=3)}). **Choix de deux répliques** : à une réplique, sous l'exécution exacte, l'échelle d'intensité n'est plus établie que dans {f('exacte', 6, r=1)} des courses (contre {f('exacte', 6)} à deux), et la dernière colonne tombe à {f('exacte', 10, r=1)}.

**Limites, déclarées** : intervalles par approximation normale ; tendance par 200 permutations ; réponse supposée proportionnelle au logarithme du facteur, plafonnée, ou en une marche ; variance prise à l'organisme du premier test, sur d'autres tâches ; les scénarios de marche ne sont joués que sans débordement ; la dernière colonne réduit le lecteur du texte au coût seul, sans mots ni plancher : elle est optimiste pour « le texte échoue » et ne vaut que comme ordre de grandeur."""

# ---------- préenregistrement
t = open(D + P + "-brouillon1.md", encoding="utf-8").read()
h_b1_p = sha(D + P + "-brouillon1.md")
t = appliquer(t, AU, P)
t = appliquer(t, CLP, P)
t = un(t, "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 1", "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 2", "EN-1", P)
t = un(t, "- Statut : **brouillon 1, non scellé**. Rien n'est lancé, rien n'est dépensé.",
       f"- Statut : **brouillon 2, non scellé** : le brouillon 1 (`{h_b1_p}`) corrigé après la contre-lecture 1 (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-2-v1/`). Rien n'est lancé, rien n'est dépensé.", "EN-2", P)
h_json = sha(D + "consignes-privees-dose-reponse-consigne-cachee-v3.json")
t = un(t, "textes privés de l'organisme `consignes-privees-dose-reponse-consigne-cachee-v1.json` (`e975c5b9aa949ceb1861095e18761bcd551a9db44cdb7e93fc3ca32659b3939b`) ; puissance `pieces/puissance_dose_reponse_consigne_cachee_v1.py` et sa sortie `pieces/puissance-dose-reponse-consigne-cachee-v1.txt` ; devis d'une page `devis-dose-reponse-consigne-cachee-v1-brouillon1.md`.",
       f"textes privés de l'organisme `consignes-privees-dose-reponse-consigne-cachee-v3.json` (`{h_json}` ; mêmes huit textes que la v1, l'échelle de proportion portée à l'intensité 10 ; la v2 est un état de travail, jamais cité) ; puissance `pieces/puissance_dose_reponse_consigne_cachee_v4.py` et sa sortie `pieces/puissance-dose-reponse-consigne-cachee-v4.txt` ; devis d'une page `devis-dose-reponse-consigne-cachee-v1-brouillon2.md`.", "EN-3", P)
debut, fin = t.index("## Puissance (planification, jamais une sélection)\n\n") + len("## Puissance (planification, jamais une sélection)\n\n"), t.index("\n\n## Devis\n")
t = t[:debut] + PUISSANCE + t[fin:]
journal.append(f"{P}\tPUISSANCE\tsection réécrite d'après la sortie v4")
t = un(t, "Devis d'une page pour la ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-brouillon1.md` (même dossier)", "Devis d'une page pour la ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-brouillon2.md` (même dossier)", "EN-4", P)
t = un(t, "Disque : au plus 1,7 pendant la marche et 5,8 pour 72 heures d'instance arrêtée.", "Disque (250 Go au moins) : au plus 1,7 pendant la marche et 5,8 pour 72 heures d'instance arrêtée, dans la limite de la fin du GO.", "CL1-10c", P)
H_RAPPORT = sha(D + "contre-lecture-1-des-brouillons-1-v2.md")
CL_P = open("contre_lecture_prereg.md", encoding="utf-8").read().rstrip("\n").replace("@@H_B1@@", h_b1_p).replace("@@H_RAPPORT@@", H_RAPPORT)
t = un(t, "<<CONTRE_LECTURE_DOSE_REPONSE>>", CL_P, "CL", P)
t = appliquer(t, AU3, P)
open(D + P + "-brouillon2.md", "w", encoding="utf-8").write(t)

# ---------- désignation
g = open(D + G + "-brouillon1.md", encoding="utf-8").read()
h_b1_g = sha(D + G + "-brouillon1.md")
g = appliquer(g, AU, G)
g = appliquer(g, CLG, G)
g = un(g, "règle de lecture posée en nœud à deux options — v1 — brouillon 1", "règle de lecture posée en nœud à deux options — v1 — brouillon 2", "EN-1", G)
g = un(g, "- Statut : **brouillon 1, non scellé**. Ce texte ne lance rien et ne dépense rien.",
       f"- Statut : **brouillon 2, non scellé** : le brouillon 1 (`{h_b1_g}`) corrigé après la contre-lecture 1 (section « Contre-lecture »), par couples appliqués par script. Ce texte ne lance rien et ne dépense rien.", "EN-2", G)
g = un(g, "`brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon1.md` au jour de ce brouillon ;", "`brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon2.md` au jour de ce brouillon ;", "EN-3", G)
g = un(g, "(« lecteur du texte non fiable (motif) : les doses jugées sont rapportées sans comparaison au texte ; qualificatif « forme forte » interdit »)",
       "(« lecteur du texte non fiable ou non calculable à une intensité jugée (motif) : les doses jugées sont rapportées sans comparaison au texte ; qualificatif « forme indéterminée » »)", "CL1-20c", G)
CL_G = open("contre_lecture_design.md", encoding="utf-8").read().rstrip("\n").replace("@@H_B1@@", h_b1_g).replace("@@H_RAPPORT@@", H_RAPPORT)
g = un(g, "<<CONTRE_LECTURE_DESIGNATION>>", CL_G, "CL", G)
g = appliquer(g, AU3, G)
open(D + G + "-brouillon2.md", "w", encoding="utf-8").write(g)
open("journal-construction.txt", "w", encoding="utf-8").write("\n".join(journal) + "\n")
print(len(journal), "opérations ;", "préenregistrement", len(t), "caractères ; désignation", len(g), "caractères")
