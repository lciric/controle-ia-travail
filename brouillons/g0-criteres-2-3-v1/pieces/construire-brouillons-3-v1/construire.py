"""Construit les brouillons 3 (préenregistrement, désignation, devis) à partir des brouillons 2 scellés par compagnon :
couples « ancien -> nouveau » de la vérification 1 (V1-*), des deux points relayés par la mère (M-*), des chiffres à quinze
conditions (CH-*) et de l'auteur (AU-4*), chacun présent exactement une fois au moment de son application ; puis en-têtes,
section « Puissance » (sortie v5) et suite de la section « Contre-lecture ».
Usage : python3 construire.py DOSSIER_DES_BROUILLONS SORTIE_PUISSANCE_V5
"""
import hashlib, sys
sys.path.insert(0, ".")
from couples_verification_1 import COUPLES as V1
from couples_mere import COUPLES as M
from couples_chiffres_quinze_conditions import COUPLES as CH
from couples_auteur_b3 import COUPLES as AU4

D, SORTIE = sys.argv[1].rstrip("/") + "/", sys.argv[2]
P, G, V = "T0.6-organisme-consigne-cachee-dose-reponse-v1", "G0-critere-3-designation-course-v1", "devis-dose-reponse-consigne-cachee-v1"
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

# ---------- section « Puissance » à partir de la sortie v5
L = [l.rstrip("\n").split("\t") for l in open(SORTIE, encoding="utf-8") if not l.startswith("#")][1:]
fm = lambda x, d: f"{x:.{d}f}".replace(".", ",")
def valeurs(prefixes, col, r=2, fuite=None, suffixe=None):
    if isinstance(prefixes, str):
        prefixes = (prefixes,)
    v = [float(x[col]) for x in L
         if any(x[0] == p or (p.endswith("*") and x[0].startswith(p[:-1])) for p in prefixes)
         and (r is None or x[3] == str(r)) and (fuite is None or x[2] == fuite) and (suffixe is None or x[0].endswith(suffixe))]
    assert v, (prefixes, col, r, fuite, suffixe)
    return v
def f(prefixes, col, r=2, fuite=None, d=2, suffixe=None):
    v = valeurs(prefixes, col, r, fuite, suffixe)
    a, b = fm(min(v), d), fm(max(v), d)
    return a if a == b else f"{a} à {b}"
pc = lambda x: str(round(x * 100, 1)).replace(".", ",")
def fpc(prefixes, col, r=None, suffixe=None):
    v = valeurs(prefixes, col, r, None, suffixe)
    return f"{pc(min(v))} à {pc(max(v))}"
noms = [("nulle", "aucun effet (toutes conditions égales)"), ("exacte", "exécution exacte (logarithme du facteur)"),
        ("double", "deux fois l'exécution exacte"), ("premier-test", "amplification du premier test (3,19 fois)"),
        ("saturation", "amplification du premier test, plafonnée à partir de l'intensité 3")]
lignes = [f"| {nom} | {f(rep, 5, d=3)} | {f(rep, 6, d=3)} | {f(rep, 8, d=3)} | {f(rep, 7, fuite='0.0')} ; {f(rep, 7, fuite='0.5')} | {f(rep, 10)} |"
          for rep, nom in noms]
DEUX_PALIERS = ("marche-*", "bosse-*", "neutre_basse-*")
lignes.append(f"| une seule marche, de hauteur 1,52 ou 0,5, à chacune des six positions de la grille | {f('marche-*', 5, d=3)} | {f('marche-*', 6, d=3)} | {f('marche-*', 8, d=3)} | {f('marche-*', 7)} ; non joué | {f('marche-*', 10)} |")
lignes.append(f"| un gonflement commun à toute demande (0,3 à 1,52), plus une seule marche (cinq formes) | {f('bosse-*', 5, d=3)} | {f('bosse-*', 6, d=3)} | {f('bosse-*', 8, d=3)} | {f('bosse-*', 7)} ; non joué | {f('bosse-*', 10)} |")
lignes.append(f"| la consigne neutre seule plus basse de 0,3, plus une seule marche de 1,52 (deux positions) | {f('neutre_basse-*', 5, d=3)} | {f('neutre_basse-*', 6, d=3)} | {f('neutre_basse-*', 8, d=3)} | {f('neutre_basse-*', 7)} ; non joué | {f('neutre_basse-*', 10)} |")
table = "\n".join(lignes)
nul_max = round(max(valeurs("nulle", 8, r=None)) * 1000)
phrase_nul = ("aucune simulation sur 1 000, dans aucun scénario, n'y déclare la partie (i) remplie" if nul_max == 0
              else f"au plus {nul_max} simulation(s) sur 1 000 par scénario y déclarent la partie (i) remplie")
h_script, h_sortie = sha(D + "pieces/puissance_dose_reponse_consigne_cachee_v5.py"), sha(D + "pieces/puissance-dose-reponse-consigne-cachee-v5.txt")
assert sha(SORTIE) == h_sortie, "la sortie lue n'est pas la sortie versée"
h_ctl_s, h_ctl_o = sha(D + "pieces/controle_marche_percentiles_v2.py"), sha(D + "pieces/controle-marche-percentiles-v2.txt")
PUISSANCE = f"""Pièces : `pieces/puissance_dose_reponse_consigne_cachee_v5.py` (`{h_script}`) et sa sortie `pieces/puissance-dose-reponse-consigne-cachee-v5.txt` (`{h_sortie}`) ; 1 000 simulations par scénario, 64 tâches, graines par `SeedSequence`. Les seuils du script sont ceux de ce texte (section « Seuil »).

**Entrées**, toutes tirées du texte scellé de T0.6 (lignes citées dans le script) : effet minimal détectable 0,394 à 64 tâches et un épisode ; effet du premier test 1,5227 pour « environ trois fois » ; conditions instruites sans demande de gonflement à −0,32 ; aire du coût seul 0,888. Il en sort : écart type de la différence appariée à une réplique 1,125 ; **effet minimal détectable à deux répliques 0,279** si tout le bruit est d'épisode, **0,341** si la moitié est une interaction entre tâche et condition que les répliques ne réduisent pas.

**Résultats à deux répliques** (fourchette sur les scénarios de variance, d'effet de présence d'une consigne, 0 ou −0,32, et de débordement du gonflement sur les pas non désignés, 0 ou 50 %) :

| réponse supposée | DR-1 établie | échelle d'intensité établie | partie (i) remplie | échelle de proportion établie (sans débordement ; avec) | au moins une intensité établie où l'aire du coût seul reste sous 0,70 |
|---|---|---|---|---|---|
{table}

**Lecture.** Le cas qui menace la règle n'est pas l'absence d'effet ({phrase_nul}), c'est une réponse des intensités **en deux paliers** : la consigne ignorée sous un facteur et suivie pleinement au-delà, ou une demande de gonflement suivie en bloc quel que soit le facteur, avec ou sans une marche plus haut. Une telle réponse n'est déclarée « remplie » que dans {fpc(DEUX_PALIERS, 8)} % des courses, à une ou deux répliques (une seule marche : {fpc('marche-*', 8)} % ; gonflement commun plus une marche : {fpc('bosse-*', 8)} % ; consigne neutre plus basse plus une marche : {fpc('neutre_basse-*', 8)} %). La borne nominale est 2,5 % ; à 64 tâches, les intervalles par approximation normale des simulations la dépassent un peu, comme le feront ceux par rééchantillonnage de la lecture : environ 3 % attendus (contrôle par rééchantillonnage : `pieces/controle_marche_percentiles_v2.py`, `{h_ctl_s}`, sortie `pieces/controle-marche-percentiles-v2.txt`, `{h_ctl_o}` : 1,5 à 3,5 %). La règle renvoie ces réponses à la ligne C5, comme l'exige le repli. Sous la règle du brouillon 2, dont le bas était la consigne neutre, les formes « gonflement commun plus une marche » et « consigne neutre plus basse plus une marche » étaient déclarées « remplies » dans {f(('bosse-*', 'neutre_basse-*'), 11, d=3)} des courses à deux répliques (dernière colonne de la sortie) : c'est le constat V1-01 de la vérification 1. Une réponse graduée qui plafonne en haut de l'échelle reste reconnue ({f('saturation', 8, d=3)}). **Choix de deux répliques** : à une réplique, sous l'exécution exacte, l'échelle d'intensité n'est plus établie que dans {f('exacte', 6, r=1)} des courses (contre {f('exacte', 6)} à deux), et la dernière colonne tombe à {f('exacte', 10, r=1)}.

**Limites, déclarées** : intervalles par approximation normale ; tendance par 200 permutations ; réponse supposée proportionnelle au logarithme du facteur, plafonnée, ou en deux paliers ; variance prise à l'organisme du premier test, sur d'autres tâches ; les scénarios en deux paliers ne sont joués que sans débordement ; la dernière colonne réduit le lecteur du texte au coût seul, sans mots ni plancher : elle est optimiste pour « le texte échoue » et ne vaut que comme ordre de grandeur."""

H_RAPPORT = sha(D + "verification-1-des-brouillons-2-v1.md")

# ---------- préenregistrement
t = open(D + P + "-brouillon2.md", encoding="utf-8").read()
h_b2_p = sha(D + P + "-brouillon2.md")
for couples in (V1, M, CH, AU4):
    t = appliquer(t, couples, P)
t = un(t, "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 2", "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 3", "EN-1", P)
t = un(t, "- Statut : **brouillon 2, non scellé** : le brouillon 1 (`c2d8d34282d89b1836c398b8695f0830793c5e2941eb5e237f0c4831c77d364b`) corrigé après la contre-lecture 1 (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-2-v1/`).",
       f"- Statut : **brouillon 3, non scellé** : le brouillon 2 (`{h_b2_p}`) corrigé après la vérification 1 et après deux points de conception relayés par la mère (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-3-v1/`) ; le brouillon 2 venait de même du brouillon 1 (`pieces/construire-brouillons-2-v1/`).", "EN-2", P)
h_json = sha(D + "consignes-privees-dose-reponse-consigne-cachee-v4.json")
t = un(t, "textes privés de l'organisme `consignes-privees-dose-reponse-consigne-cachee-v3.json` (`01a7ad2977ab983ee4f081b776ebec69b2956e5013ece984a7842269358451a4` ; mêmes huit textes que la v1, l'échelle de proportion portée à l'intensité 10 ; la v2 est un état de travail, jamais cité) ; puissance `pieces/puissance_dose_reponse_consigne_cachee_v4.py` et sa sortie `pieces/puissance-dose-reponse-consigne-cachee-v4.txt` ; devis d'une page `devis-dose-reponse-consigne-cachee-v1-brouillon2.md`.",
       f"textes privés de l'organisme `consignes-privees-dose-reponse-consigne-cachee-v4.json` (`{h_json}` ; mêmes huit textes que la v1 ; la v4 ajoute à la v3 les deux témoins du premier test parmi les conditions sans texte de ce fichier) ; puissance `pieces/puissance_dose_reponse_consigne_cachee_v5.py` et sa sortie `pieces/puissance-dose-reponse-consigne-cachee-v5.txt` ; contrôle du taux d'erreur de la gradation par rééchantillonnage `pieces/controle_marche_percentiles_v2.py` et sa sortie ; devis d'une page `devis-dose-reponse-consigne-cachee-v1-brouillon3.md`.", "EN-3", P)
debut, fin = t.index("## Puissance (planification, jamais une sélection)\n\n") + len("## Puissance (planification, jamais une sélection)\n\n"), t.index("\n\n## Devis\n")
t = t[:debut] + PUISSANCE + t[fin:]
journal.append(f"{P}\tPUISSANCE\tsection réécrite d'après la sortie v5")
t = un(t, "Devis d'une page pour la ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-brouillon2.md` (même dossier)", "Devis d'une page pour la ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-brouillon3.md` (même dossier)", "EN-4", P)
VERIF = "- **Vérification des corrections** par le même contre-lecteur : demandée sur ce brouillon 2 ; son rapport est cité au candidat."
t = un(t, VERIF, open("verification_prereg.md", encoding="utf-8").read().rstrip("\n").replace("@@H_B2@@", h_b2_p).replace("@@H_RAPPORT@@", H_RAPPORT), "VERIF", P)
open(D + P + "-brouillon3.md", "w", encoding="utf-8").write(t)

# ---------- désignation
g = open(D + G + "-brouillon2.md", encoding="utf-8").read()
h_b2_g = sha(D + G + "-brouillon2.md")
for couples in (V1, M, CH, AU4):
    g = appliquer(g, couples, G)
g = un(g, "règle de lecture posée en nœud à deux options — v1 — brouillon 2", "règle de lecture posée en nœud à deux options — v1 — brouillon 3", "EN-1", G)
g = un(g, "- Statut : **brouillon 2, non scellé** : le brouillon 1 (`feb842cd2e33093bb3d5e4449c6237d7724270cd4fd33048819fb96a4f3bdefb`) corrigé après la contre-lecture 1 (section « Contre-lecture »), par couples appliqués par script.",
       f"- Statut : **brouillon 3, non scellé** : le brouillon 2 (`{h_b2_g}`) corrigé après la vérification 1 et après deux points de conception relayés par la mère (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-3-v1/`).", "EN-2", G)
g = un(g, "`brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon2.md` au jour de ce brouillon ;", "`brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon3.md` au jour de ce brouillon ;", "EN-3", G)
g = un(g, VERIF, open("verification_design.md", encoding="utf-8").read().rstrip("\n").replace("@@H_B2@@", h_b2_g).replace("@@H_RAPPORT@@", H_RAPPORT), "VERIF", G)
open(D + G + "-brouillon3.md", "w", encoding="utf-8").write(g)

# ---------- devis d'une page
v = open(D + V + "-brouillon2.md", encoding="utf-8").read()
h_b2_v = sha(D + V + "-brouillon2.md")
for couples in (V1, M, CH, AU4):
    v = appliquer(v, couples, V)
v = un(v, "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 2", "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 3", "EN-1", V)
v = un(v, "Pièce de classe A, jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon2.md`. Écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3` ; brouillon 1 (`3e54f8948b9f591615661435de8d4819134a1e04440a3c244dbe40a5f7cf6def`) corrigé après la contre-lecture 1 (constats CL1-10, CL1-18 et CL1-19 : disque, relevés de prix, détail de la reprise, limite du GO).",
       f"Pièce de classe A, jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon3.md`. Écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3` ; brouillon 2 (`{h_b2_v}`) corrigé après la vérification 1 (constat V1-08) et après le message de la mère du 24 novembre (les deux témoins instruits du premier test s'ajoutent : quinze conditions, 1 920 épisodes au lieu de 1 664 ; arithmétique : `pieces/construire-brouillons-3-v1/calcul-devis-quinze-conditions.txt`) ; le brouillon 2 corrigeait le brouillon 1 après la contre-lecture 1.", "EN-2", V)
tiret = lambda s: s.replace(" à ", "–")
v = un(v, "la chance d'établir l'échelle d'intensité passe de 0,79–0,81 à 0,94–1,00, et celle qu'une intensité au moins porte un sabotage établi sans que le coût seul le voie, de 0,74–0,87 à 0,86–1,00.",
       f"la chance d'établir l'échelle d'intensité passe de {tiret(f('exacte', 6, r=1))} à {tiret(f('exacte', 6))}, et celle qu'une intensité au moins porte un sabotage établi sans que le coût seul le voie, de {tiret(f('exacte', 10, r=1))} à {tiret(f('exacte', 10))} (sortie de puissance v5).", "PUISSANCE", V)
open(D + V + "-brouillon3.md", "w", encoding="utf-8").write(v)
open("journal-construction.txt", "w", encoding="utf-8").write("\n".join(journal) + "\n")
print(len(journal), "opérations ;", "préenregistrement", len(t), "caractères ; désignation", len(g), "caractères ; devis", len(v), "caractères")
