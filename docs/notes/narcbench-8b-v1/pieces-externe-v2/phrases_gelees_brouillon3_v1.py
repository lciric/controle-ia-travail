"""Contrôle par programme des phrases gelées du code contre le texte court (brouillon 3, `fae8a96c…`), v1.

Lit dans le texte, sans rien recopier à la main : les états de la règle C (table de la section « Critères de lecture gelés »),
les qualificatifs (plancher, placebo) et le signe (sections « Critères » et « Seuil »), les états de la règle T, les cinq
phrases par famille et les six lignes de réponse R0 à R5. Chaque phrase du texte devient un modèle : le texte exact, où les
marqueurs `<…>`, « famille F » et les parenthèses descriptives de la règle T valent « un texte quelconque ». Le code
(`cellules_externe_v2`) produit chaque phrase sur un exemple ; elle doit suivre son modèle **en entier**. Usage :
PYTHONPATH=src python phrases_gelees_brouillon3_v1.py <brouillon 3>"""
import hashlib
import re
import sys
from pathlib import Path

from controle_ia.narcbench import cellules_externe_v2 as CE

ATTENDUE = "fae8a96ccc75e592e8ca12c5b156a19775388c14f345d94fbf77d6fd8cbc0a90"
chemin = Path(sys.argv[1])
if hashlib.sha256(chemin.read_bytes()).hexdigest() != ATTENDUE:
    raise SystemExit(f"{chemin} : empreinte ≠ {ATTENDUE[:12]}…")
texte = chemin.read_text(encoding="utf-8")
criteres = texte[texte.index("## Critères de lecture gelés"):texte.index("## Liste d'arrêt")]
seuil = texte[texte.index("## Seuil"):texte.index("## Puissance")]
plat = lambda s: re.sub(r"\s+", " ", s)                                     # lignes repliées du texte


def entre_guillemets(s: str, debut: int = 0) -> tuple:
    """Premier « … » à partir de `debut`, guillemets imbriqués compris : (contenu, fin)."""
    i = s.index("«", debut)
    profondeur, j = 0, i
    while True:
        if s[j] == "«":
            profondeur += 1
        elif s[j] == "»":
            profondeur -= 1
            if profondeur == 0:
                return s[i + 1:j].strip(), j + 1
        j += 1


def modele(phrase: str, libres=()) -> re.Pattern:
    """Texte exact ; marqueurs `<…>` et morceaux `libres` → n'importe quel texte."""
    jetons = re.split(r"(<[^<>]*>|" + "|".join(re.escape(x) for x in libres) + ")" if libres else r"(<[^<>]*>)", phrase)
    return re.compile("".join("(.+?)" if (j.startswith("<") and j.endswith(">")) or j in libres else re.escape(j)
                              for j in jetons if j))


def table(section: str, cle: str) -> str:
    ligne = next(l for l in section.splitlines() if re.match(r"\| \d \| " + cle + r" \|", l))
    return entre_guillemets(ligne.split("|")[4])[0]


ecarts, vus = [], 0


def verifier(nom: str, motif: re.Pattern, produite: str) -> None:
    global vus
    vus += 1
    if not motif.fullmatch(produite):
        ecarts.append(f"{nom} :\n  texte  : {motif.pattern[:300]}\n  code   : {produite[:300]}")


# règle C : états
etats_c = {"C0": CE.GARDE_CONSTANTS, "C1": CE.NON_CALCULABLE, "C2": CE.REPRODUIT, "C3": CE.NON_REPRODUIT, "C4": CE.NON_TRANCHE}
for k, v in etats_c.items():
    verifier(f"règle C, {k}", re.compile(re.escape(table(criteres, k))), v)
# qualificatifs et signe
qualif = plat(criteres[criteres.index("Qualificatifs ajoutés"):criteres.index("**Règle T")])
morceaux, pos = [], 0
while "«" in qualif[pos:]:
    m, pos = entre_guillemets(qualif, pos)
    morceaux.append(m)
attendus = [CE.QUALIF_PLANCHER[CE.AU_DESSUS], CE.QUALIF_PLANCHER[CE.PAS_AU_DESSUS], "plancher par tirage équivalent en loi",
            CE.QUALIF_PLANCHER[CE.SANS_PLANCHER], "placebo déclenché ; audit R4"]
for t, c in zip(morceaux, attendus):
    verifier("qualificatif", re.compile(re.escape(t)), c)
p = CE.phrase_cellule("C2", CE.REPRODUIT, 0.98, 1.0, CE.PAS_AU_DESSUS, True, repli=True)
for t in (morceaux[1], morceaux[2], morceaux[4]):
    if t not in p:
        ecarts.append(f"phrase de cellule : « {t} » absent de « {p} »")
signe = plat(seuil[seuil.index("**Signe**"):seuil.index("Les deux issues")])
s_morceaux, pos = [], 0
while "«" in signe[pos:]:
    m, pos = entre_guillemets(signe, pos)
    s_morceaux.append(m)
for t, c in zip([x for x in s_morceaux if x != "non reproduit"], (CE.signe(0.6, 0.9), CE.signe(0.2, 0.4), CE.signe(0.4, 0.6))):
    verifier("signe", re.compile(re.escape(t)), c)
# règle T
regle_t = plat(criteres[criteres.index("**Règle T"):criteres.index("**Phrases par famille")])
etats_t = {}
for ligne_t in ("T0", "T1", "T2", "T3", "T4"):
    debut = regle_t.index(ligne_t + " ")
    etats_t[ligne_t] = entre_guillemets(regle_t, regle_t.index("→", debut))[0]
r = {"T0": CE.regle_t({"a": ("C0", CE.GARDE_CONSTANTS)}), "T1": CE.regle_t({"a": ("C2", CE.REPRODUIT)}),
     "T2": CE.regle_t({"a": ("C3", CE.NON_REPRODUIT)}),
     "T3": CE.regle_t({"a": ("C2", CE.REPRODUIT), "b": ("C3", CE.NON_REPRODUIT)}), "T4": CE.regle_t({"a": ("C4", CE.NON_TRANCHE)})}
for k, t in etats_t.items():
    verifier(f"règle T, {k}", modele(t, ("(cellule nommée)", "(cellules nommées)", "(cellules nommées, état des autres)")),
             r[k]["phrase"])
    etiquette = t.split(" (")[0]
    verifier(f"règle T, état {k}", re.compile(re.escape(etiquette)), r[k]["etat"])
# phrases par famille
familles = plat(criteres[criteres.index("**Phrases par famille"):criteres.index("**Réponse au barreau")])
puces = familles.split(" - ")[1:]
cas = [(CE.REPRODUIT, CE.REPRODUIT), (CE.REPRODUIT, CE.NON_REPRODUIT), (CE.REPRODUIT, CE.NON_TRANCHE), (CE.NON_REPRODUIT, CE.EN_PARTIE),
       (CE.NON_TRANCHE, CE.NON_LU)]
for i, (puce, (t, e)) in enumerate(zip(puces, cas), 1):
    phrase = entre_guillemets(puce, puce.index("→"))[0]
    for f in CE.CO_PRINCIPALES:
        verifier(f"phrase F{i} ({f})", modele(phrase, ("famille F",)), CE.phrase_famille(f, t, e)["phrase"])
# réponse au barreau
cellules8 = {f"c{i}": CE.REPRODUIT for i in range(8)}
planchers = {"témoin de recette, Qwen3-32B, pic": CE.AU_DESSUS, "linéaire, Llama-3.1-70B, écart": CE.PAS_AU_DESSUS}
etats_f = {"difference_moyennes": CE.NON_TRANCHE, "lineaire": CE.NON_LU}
reponses = {"R0": CE.reponse(CE.NON_TRANCHE, cellules8, planchers, etats_f),
            "R1": CE.reponse(CE.REPRODUIT, cellules8, planchers, etats_f),
            "R2": CE.reponse(CE.REPRODUIT, {k: CE.NON_REPRODUIT for k in cellules8}, planchers, etats_f),
            "R3": CE.reponse(CE.REPRODUIT, dict(cellules8, c1=CE.NON_REPRODUIT, c2=CE.NON_TRANCHE), planchers, etats_f),
            "R4": CE.reponse(CE.REPRODUIT, dict({k: CE.NON_TRANCHE for k in cellules8}, c0=CE.NON_REPRODUIT), planchers, etats_f),
            "R5": CE.reponse(CE.REPRODUIT, {k: CE.NON_TRANCHE for k in cellules8}, planchers, etats_f)}
for k, rep in reponses.items():
    if rep["ligne"] != k:
        ecarts.append(f"{k} : le code rend la ligne {rep['ligne']}")
    verifier(f"réponse {k}", modele(table(criteres, k)), rep["phrase"])
print(f"{vus} phrases gelées du code comparées au brouillon 3 ({ATTENDUE[:12]}…) : {len(ecarts)} écart(s)")
for e in ecarts:
    print(e)
sys.exit(1 if ecarts else 0)
