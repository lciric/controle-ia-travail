#!/usr/bin/env python3
# verif_hc2.py -- relit le devis compose (brouillon 2) et cherche chacun de ses nombres
# dans la sortie de calc_hc2.py (chiffres calcules) ou dans les pieces lues (chiffres releves).
# Un nombre trouve nulle part est affiche : il est a justifier a la main ou a corriger.
#
# Usage : python3 -I verif_hc2.py DEVIS.md RACINE_DU_DEPOT DOSSIER_DES_EXTRAITS
# Le dossier des extraits contient cinq fichiers que le mandat ne permet de lire que par
# une commande precise, ou qui vivent sur une autre branche ; ils se refont ainsi :
#   texte-b43-section-6-11.txt : awk '/^### 6.11/{f=1} /^### 6.12/{exit} f' prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md
#   regle-google.txt           : git show origin/main:CLAUDE.md | awk '/^## Appels aux modèles de Google/{f=1} f{print} /^## Qui conçoit/{exit}'
#   lignes-go.txt              : git show origin/main:registres/go.md | grep -E '^\| GO-2026-11-21-(63|68|69|71) '
#   avenant-2.md               : git show origin/relance-bras-a/avenant-2:docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v1.md
#   verification.md            : git show <branche de la session du bras A>:docs/notes/relance-organismes-discrets-v1/verification-devis-lectures-hors-carte-brouillon1-v1.md
# Facultatif : premiere-composition-brouillon2.md, la premiere composition du brouillon 2 (17fbf6c4...),
# gardee au bloc-notes du redacteur ; sans elle, son empreinte abregee est dite « non verifiable ici ».
# Aucun reseau, aucune ecriture.
import glob
import json
import os
import re
import subprocess
import sys
from decimal import Decimal

devis, racine, extraits = sys.argv[1], sys.argv[2], sys.argv[3]
ici = os.path.dirname(os.path.abspath(__file__))
REL = os.path.join(racine, "docs", "notes", "relance-organismes-discrets-v1")

NB = re.compile(r"(?<![\w.,])(\d{1,3}(?:[ \u00a0\u202f]\d{3})+(?:,\d+)?|\d+(?:,\d+)?)(?![\w]|[.,]\d)")
NB_EN = re.compile(r"(?<![\w.,])(\d+(?:,\d{3})*\.\d+|\d+)(?![\w]|[.,]\d)")


def nettoie(txt):
    """Retire ce qui n'est pas un chiffre du devis : empreintes, dates, heures, identifiants entre accents graves."""
    txt = re.sub(r"`[^`\n]*`", " ", txt)
    txt = re.sub(r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?Z?\b", " ", txt)
    txt = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", " ", txt)
    txt = re.sub(r"\b\d{1,2}:\d{2}(?::\d{2})?Z?\b", " ", txt)
    txt = re.sub(r"GO-\d{4}-\d{2}-\d{2}-\d+", " ", txt)
    txt = re.sub(r"\b[0-9a-f]{8,64}…?", " ", txt)
    return txt


def nombres_fr(txt):
    out = set()
    for m in NB.finditer(txt):
        s = re.sub(r"[ \u00a0\u202f]", "", m.group(1)).replace(",", ".")
        out.add(Decimal(s))
    return out


def nombres_source(txt):
    """Nombres d'une piece lue : ecriture francaise, et ecriture anglaise (pages de prix, citations)."""
    out = nombres_fr(txt)
    for m in NB_EN.finditer(txt):
        try:
            out.add(Decimal(m.group(1).replace(",", "")))
        except Exception:
            pass
    return out


# ---- le devis, sans la sortie du calcul recopiee en section 13
doc = open(devis, encoding="utf-8").read()
tete, _, queue = doc.partition("## 13. Calculs, par programme")
assert queue, "section 13 introuvable"
corps = nettoie(tete)

# ---- chiffres calcules
brut = subprocess.run([sys.executable, "-I", os.path.join(ici, "calc_hc2.py"), "--json"],
                      check=True, capture_output=True, text=True).stdout
d = json.loads(brut)
calc = nombres_fr("\n".join(d["trace"]) + "\n" + "\n".join(d["valeurs"].values()))
# la sortie du calcul recopiee dans le devis doit etre celle du programme, a la lettre
assert "\n".join(d["trace"]) in queue, "la section 13 du devis n'est pas la sortie de calc_hc2.py"

# ---- chiffres releves : les pieces lues
sources = {}


def charge(nom, chemin):
    sources[nom] = nombres_source(nettoie(open(chemin, encoding="utf-8", errors="replace").read()))


charge("texte, section 6.11", os.path.join(extraits, "texte-b43-section-6-11.txt"))
charge("règle des appels à Google", os.path.join(extraits, "regle-google.txt"))
charge("lignes du registre", os.path.join(extraits, "lignes-go.txt"))
charge("avenant 2", os.path.join(extraits, "avenant-2.md"))
charge("vérification", os.path.join(extraits, "verification.md"))
charge("devis de course", os.path.join(REL, "devis-bras-a-v2.md"))
charge("devis des essais", os.path.join(REL, "devis-essais-admission-mistral-neon-bras-a-v1.md"))
charge("avenant 1, version 3", os.path.join(REL, "avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md"))
charge("index des pages de prix", os.path.join(REL, "pages-de-prix-essais-admission-v1", "index-pages-de-prix-v1.md"))
charge("mandat", os.path.join(REL, "mandat-redacteur-fable-devis-lectures-hors-carte-v1.md"))
charge("brouillon 1", os.path.join(REL, "devis-lectures-hors-carte-bras-a-v1-brouillon1.md"))
for f in sorted(glob.glob(os.path.join(REL, "mots-de-lazar-*.md"))):
    charge(os.path.basename(f), f)
# la section de Gemini 4 Neon de la page de prix de Google (texte brut de la page)
page = open(os.path.join(REL, "pages-de-prix-essais-admission-v1", "google-gemini-pricing-2026-11-21.html"), encoding="utf-8", errors="replace").read()
a = page.find("## Gemini 4 Neon")
assert a > 0
sources["page de prix de Google, section de Neon"] = nombres_source(page[a:page.find("\n## ", a + 10)])
fiche = open(os.path.join(REL, "pages-de-prix-essais-admission-v1", "mistral-large-4-0-2026-11-21.html"), encoding="utf-8", errors="replace").read()
sources["fiche de Mistral Large 4"] = {Decimal(x) for x in re.findall(r"\$(\d+(?:\.\d+)?)", fiche)}

# ---- comptes de signes des dix lignes de calcul, recomptes ici sur le devis compose
signes = {}
sec8 = tete[tete.index("## 8. Lignes de calcul proposées"):tete.index("**Chaque ligne ajoute**")]
for m in re.finditer(r"^(\d+)\. \*\*[^*]+\*\* : (.*)$", sec8, flags=re.M):
    signes[int(m.group(1))] = len(m.group(2))
assert sorted(signes) == list(range(1, 11)), sorted(signes)
assert max(signes.values()) <= 600, signes
print("signes des dix lignes de calcul :", ", ".join(f"{i} : {signes[i]}" for i in sorted(signes)))
# le texte que la verification proposait pour la ligne 1 : la ligne 1 du brouillon 1, sa correction C-6 appliquee
b1 = open(os.path.join(REL, "devis-lectures-hors-carte-bras-a-v1-brouillon1.md"), encoding="utf-8").read()
ligne1_b1 = re.search(r"^1\. \*\*Premier lecteur, lots d'épreuve\*\* : (.*)$", b1, flags=re.M).group(1)
verif_txt = open(os.path.join(extraits, "verification.md"), encoding="utf-8").read()
m = re.search(r"Ligne 1, remplacer « (.*?) » par « (.*?) »", verif_txt)
assert m and ligne1_b1.count(m.group(1)) == 1
ligne1_verif = ligne1_b1.replace(m.group(1), m.group(2))
print("ligne 1 du brouillon 1 :", len(ligne1_b1), "signes ; avec la correction C-6 de la vérification :", len(ligne1_verif), "signes")
comptes_de_signes = {Decimal(v_) for v_ in signes.values()} | {Decimal(len(ligne1_verif))}

# ---- empreintes : chaque empreinte entiere de la section 12 est recalculee sur le fichier qu'elle nomme
import hashlib


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


sec12 = tete[tete.index("## 12. Ce que j'ai ouvert"):]
connues = {}
n_emp = 0
for ligne in sec12.split("\n"):
    m = re.match(r"^\| `([^`]+)`[^|]*\| `([0-9a-f]{64})` \|", ligne)
    if not m:
        continue
    nom, emp = m.group(1), m.group(2)
    if nom.endswith("verification-devis-lectures-hors-carte-brouillon1-v1.md"):
        chemin = os.path.join(extraits, "verification.md")
    elif nom.endswith("avenant-2-devis-essais-admission-plafond-google-65536-v1.md"):
        chemin = os.path.join(extraits, "avenant-2.md")
    elif nom.startswith("…/"):
        chemin = os.path.join(REL, nom[2:])
    else:
        chemin = os.path.join(racine, nom)
    reel = sha(chemin)
    assert reel == emp, ("empreinte inegale", nom, emp, reel)
    connues[nom] = emp
    n_emp += 1
assert n_emp == 19, n_emp
# les fichiers du dossier des extraits comptent aussi (une composition anterieure gardee au bloc-notes, par exemple)
for f in sorted(glob.glob(os.path.join(extraits, "*"))):
    if os.path.isfile(f):
        connues["extrait " + os.path.basename(f)] = sha(f)
m = re.search(r"`calc_hc2\.py` \(`([0-9a-f]{64})`\)", sec12)
assert m and m.group(1) == sha(os.path.join(ici, "calc_hc2.py")), "empreinte de calc_hc2.py inegale"
# chaque empreinte abregee du devis est le debut d'une empreinte recalculee, ou se lit dans une piece lue
textes_bruts = ""
for f in ([os.path.join(extraits, x) for x in ("texte-b43-section-6-11.txt", "verification.md", "avenant-2.md")]
          + [os.path.join(REL, "devis-essais-admission-mistral-neon-bras-a-v1.md"),
             os.path.join(REL, "devis-lectures-hors-carte-bras-a-v1-brouillon1.md"),
             os.path.join(REL, "pages-de-prix-essais-admission-v1", "index-pages-de-prix-v1.md")]):
    textes_bruts += open(f, encoding="utf-8", errors="replace").read()
tete_git = subprocess.run(["git", "-C", racine, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
abregees = sorted(set(re.findall(r"`([0-9a-f]{8})…`", tete)))
# pieces nommees par le devis mais non livrees : verifiees si le dossier des extraits les contient, dites sinon
NON_LIVREES = {"17fbf6c4": "première composition du brouillon 2, gardée au bloc-notes du rédacteur"}
for a8 in abregees:
    bon = any(e.startswith(a8) for e in connues.values()) or (a8 in textes_bruts) or tete_git.startswith(a8)
    if not bon and a8 in NON_LIVREES:
        print(f"empreinte abrégée d'une pièce non livrée, non vérifiable ici : {a8}… — {NON_LIVREES[a8]}")
        continue
    assert bon, "empreinte abregee introuvable : " + a8
print(f"empreintes entières recalculées : {n_emp}, et celle de calc_hc2.py ; empreintes abrégées retrouvées : {len(abregees)}")

# ---- confrontation
dans_doc = sorted(nombres_fr(corps))
petits = {Decimal(n) for n in range(0, 21)}   # numeros de section, de ligne, de garde, de decision
nulle_part, par_calcul, par_piece = [], 0, 0
for n in dans_doc:
    if n in calc:
        par_calcul += 1
    elif any(n in s for s in sources.values()):
        par_piece += 1
    elif n in petits or n in comptes_de_signes:
        pass
    else:
        nulle_part.append(n)
print(f"nombres distincts du devis, hors section 13 : {len(dans_doc)} ; trouvés dans la sortie du calcul : {par_calcul} ; dans une pièce lue seulement : {par_piece} ; trouvés nulle part : {len(nulle_part)}")
for n in nulle_part:
    s = str(n).replace(".", ",")
    # les lignes du devis qui portent ce nombre
    lieux = []
    for i, ligne in enumerate(tete.split("\n"), 1):
        if n in nombres_fr(nettoie(ligne)):
            lieux.append(i)
    print(f"  NULLE PART : {s} — lignes {lieux[:8]}")
if "--detail" in sys.argv:
    for n in dans_doc:
        if n not in calc and n not in petits:
            ou = [nom for nom, s in sources.items() if n in s]
            print(f"  relevé : {str(n).replace('.', ',')} — {', '.join(ou[:4])}")
sys.exit(0 if not nulle_part else 1)
