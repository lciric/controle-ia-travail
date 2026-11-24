"""Construit les brouillons 4 (préenregistrement, désignation, devis) à partir des brouillons 3 scellés par compagnon :
couples « ancien -> nouveau » de la vérification 2 et de la relecture de l'article sur PDF (V2-*, REF-*), puis du retrait,
par Lazar, du lancement de l'organisme à adaptateur (L-*), chacun présent exactement une fois au moment de son application ;
puis en-têtes et suite de la section « Contre-lecture ».
Usage : python3 construire.py DOSSIER_DES_BROUILLONS
"""
import hashlib, sys
sys.path.insert(0, ".")
from couples_verification_2 import COUPLES as V2
from couples_retrait_lancement_adaptateur import COUPLES as L, RETRAIT, BORNE_DEBUT, BORNE_FIN

D = sys.argv[1].rstrip("/") + "/"
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

H_V2 = sha(D + "verification-2-des-brouillons-3-v1.md")
SUITE = "- **Vérification 2**, du seul écart entre le brouillon 2 et ce brouillon 3, par le même contre-lecteur : demandée ; son rapport est cité au candidat."

# ---------- préenregistrement
t = open(D + P + "-brouillon3.md", encoding="utf-8").read()
h_b3_p = sha(D + P + "-brouillon3.md")
for couples in (V2, L):
    t = appliquer(t, couples, P)
t = un(t, "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 3", "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 4", "EN-1", P)
t = un(t, f"- Statut : **brouillon 3, non scellé** : le brouillon 2 (`6a2745f808d9b748163df84073b4c43d99822f1536a4f46f021fa07e816844f5`) corrigé après la vérification 1 et après deux points de conception relayés par la mère (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-3-v1/`) ; le brouillon 2 venait de même du brouillon 1 (`pieces/construire-brouillons-2-v1/`).",
       f"- Statut : **brouillon 4, non scellé** : le brouillon 3 (`{h_b3_p}`) corrigé après la vérification 2 (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-4-v1/`) ; les brouillons 2 et 3 venaient de même de leur prédécesseur (`pieces/construire-brouillons-2-v1/`, `pieces/construire-brouillons-3-v1/`).", "EN-2", P)
t = un(t, "devis d'une page `devis-dose-reponse-consigne-cachee-v1-brouillon3.md`.", "devis d'une page `devis-dose-reponse-consigne-cachee-v1-brouillon4.md`.", "EN-3", P)
t = un(t, "Devis d'une page pour la ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-brouillon3.md` (même dossier)", "Devis d'une page pour la ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-brouillon4.md` (même dossier)", "EN-4", P)
t = un(t, SUITE, open("verification2_prereg.md", encoding="utf-8").read().rstrip("\n").replace("@@H_B3@@", h_b3_p).replace("@@H_V2@@", H_V2), "VERIF-2", P)
assert "<<REFERENCE_SOOPAL_ET_AL>>" not in t
open(D + P + "-brouillon4.md", "w", encoding="utf-8").write(t)

# ---------- désignation
g = open(D + G + "-brouillon3.md", encoding="utf-8").read()
h_b3_g = sha(D + G + "-brouillon3.md")
assert g.count(BORNE_DEBUT) == 1 and g.count(BORNE_FIN) == 1
a, b = g.index(BORNE_DEBUT), g.index(BORNE_FIN)
g = g[:a] + RETRAIT + g[b:]
journal.append(f"{G}\tL-3\tbloc du lancement 2 ({b - a} caractères) remplacé par la note de retrait")
for couples in (V2, L):
    g = appliquer(g, couples, G)
g = un(g, "règle de lecture posée en nœud à deux options — v1 — brouillon 3", "règle de lecture posée en nœud à deux options — v1 — brouillon 4", "EN-1", G)
g = un(g, "- Statut : **brouillon 3, non scellé** : le brouillon 2 (`c0208ceb8089016516485cfcaf1932a9145fc0f5bd3badacadd6b91917e06a0a`) corrigé après la vérification 1 et après deux points de conception relayés par la mère (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-3-v1/`).",
       f"- Statut : **brouillon 4, non scellé** : le brouillon 3 (`{h_b3_g}`) corrigé après la vérification 2 et après le retrait, par Lazar, du lancement de l'organisme à adaptateur (section « Contre-lecture »), par couples appliqués par script (`pieces/construire-brouillons-4-v1/`).", "EN-2", G)
g = un(g, "`brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon3.md` au jour de ce brouillon ;", "`brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon4.md` au jour de ce brouillon ;", "EN-3", G)
g = un(g, SUITE, open("verification2_design.md", encoding="utf-8").read().rstrip("\n").replace("@@H_B3@@", h_b3_g).replace("@@H_V2@@", H_V2), "VERIF-2", G)
assert "<<ECHEANCE_CLAUSE_LANCEMENT_2>>" not in g
open(D + G + "-brouillon4.md", "w", encoding="utf-8").write(g)

# ---------- devis d'une page
v = open(D + V + "-brouillon3.md", encoding="utf-8").read()
h_b3_v = sha(D + V + "-brouillon3.md")
for couples in (V2, L):
    v = appliquer(v, couples, V)
v = un(v, "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 3", "(partie (i) du critère 2 de la porte G0) — v1 — brouillon 4", "EN-1", V)
v = un(v, "Pièce de classe A, jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon3.md`. Écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3` ; brouillon 2 (`68201f2731348a1af7c8dddfd842ed43e18144322ff6e71d04a582bb42de4b30`) corrigé après la vérification 1 (constat V1-08) et après le message de la mère du 24 novembre (les deux témoins instruits du premier test s'ajoutent : quinze conditions, 1 920 épisodes au lieu de 1 664 ; arithmétique : `pieces/construire-brouillons-3-v1/calcul-devis-quinze-conditions.txt`) ; le brouillon 2 corrigeait le brouillon 1 après la contre-lecture 1.",
       f"Pièce de classe A, jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon4.md`. Écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3` ; brouillon 3 (`{h_b3_v}`) corrigé après la vérification 2 (constat V2-07 : disque d'au moins 300 Go) et après le retrait, par Lazar, du lancement de l'organisme à adaptateur. Le brouillon 3 avait porté la course à quinze conditions, 1 920 épisodes (arithmétique : `pieces/construire-brouillons-3-v1/calcul-devis-quinze-conditions.txt`), après la vérification 1 et le message de la mère du 24 novembre.", "EN-2", V)
open(D + V + "-brouillon4.md", "w", encoding="utf-8").write(v)
open("journal-construction.txt", "w", encoding="utf-8").write("\n".join(journal) + "\n")
print(len(journal), "opérations ;", "préenregistrement", len(t), "caractères ; désignation", len(g), "caractères ; devis", len(v), "caractères")
