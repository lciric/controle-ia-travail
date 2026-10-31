"""Assemble les faits du collisionneur des nœuds (question v9). Usage : assembler.py DEPOT SORTIE [--releve]."""
import hashlib, json, re, subprocess, sys
from pathlib import Path

DEPOT, SORTIE = Path(sys.argv[1]), Path(sys.argv[2])
RELEVE = "--releve" in sys.argv
CA, MAIN = "origin/canal/conv-audit-n04", "origin/main"
E = "brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/"
PP = E + "pre-pilote-course-2-v1/"
B7 = PP + "preenregistrement-pre-pilote-course-2-brouillon7.md"
LV = E + "bisociation-deux-espaces-v1/experience-v2/lancement-v2/"

# (numéro, source, chemin, plages, règle 2, nœuds, note de recoupement)
PIECES = [
 ("1", CA, LV + "verdict-validation-v1.md", None, False, "N1", ""),
 ("2", CA, LV + "diagnostic-v5-v1/diagnostic-v5-v1.md", None, False, "N1", ""),
 ("3", CA, "prereg/preenregistrement-bisociation-deux-espaces-v2.md", [(283,300),(555,586),(617,688),(689,735)], False, "N1", ""),
 ("4", CA, B7, [(1,78)], True, "N3, N4", ""),
 ("5", CA, B7, [(283,283),(296,296)], True, "N3 (S31)", "l. 296 (S31) ajoutée par la liste v2"),
 ("6", CA, B7, [(336,356)], True, "N5", "fin portée de 360 à 356 : les l. 357 à 360 sont le titre et l'en-tête d'une table hors pièce ; règle 2 étendue (configuration recommandée)"),
 ("7", CA, B7, [(543,587)], False, "N5", "fin portée de 585 à 587 : lignes 31 et 32 de la table R5 annoncées par la liste"),
 ("8", CA, B7, [(619,619)], False, "N5 (DEP4)", ""),
 ("9", CA, B7, [(639,None)], True, "N3", ""),
 ("10", CA, PP + "calcul-puissance-pre-pilote-course-2-v6.sortie.txt", None, False, "N2 (retiré)", "servie entière (liste v2)"),
 ("11", MAIN, "docs/notes/ideation-organisme-v1/course-2/devis-course-2-et-pre-pilote-v6.md", [(20,36),(184,232),(370,443)], True, "N2 (retiré)", ""),
 ("12", CA, PP + "contre-lecture-annexe-bras-meta-v1-brouillon1.md", [(19,22),(49,87),(125,None)], True, "N4", "règle 2 étendue (confiance d'auteur)"),
 ("13", CA, PP + "annexe-bras-meta-v1-brouillon1.md", [(18,30),(85,102),(116,224)], True, "N4", "règle 2 étendue (option recommandée)"),
 ("14", CA, "docs/notes/ideation-organisme-v1/contre-lecture-cl19-orchestrateur-v54-v1.md", [(14,22),(100,114),(149,172)], True, "N5", ""),
 ("15", CA, "docs/notes/ideation-organisme-v1/orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md", [(65,105)], True, "N5", ""),
 ("16", CA, "docs/notes/ideation-organisme-v1/orchestrateur-v54/LISEZMOI-orchestrateur-pole-v7-v54.md", [(95,120)], False, "N5", "fin portée de 116 à 120 : choix 10 à 12 (le choix 10, indices de forme, est cité par N5)"),
 ("17", CA, "prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon3.md", [(9,101),(166,176),(359,393),(687,698)], True, "N6", "fin portée de 394 à 393 : la l. 394 est un titre hors pièce"),
 ("18", MAIN, "docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md", [(22,40),(83,83),(164,249),(250,262)], True, "N1", "l. 83 ajoutée par la liste v2"),
 ("19", CA, "registres/decisions.md", "R:630,634,635,638,643,660,661,674,675,678,679,680,685", True, "tous", "lignes de la branche de conv-audit"),
 ("20", CA, "docs/notes/ideation-organisme-v1/contre-lecture-cl18-orchestrateur-v53-v1.md", [(35,35),(156,156)], True, "N5 (portée du plafond, CL18-11)", "ajoutée par la liste v2"),
 ("SD-1", "LOCAL", "donnees/collisionneur-question-6-v1/run-question-6-e3-v1/etat.md", None, False, "N6", "pièce de session-depot ; état du run seul, aucune réponse de cellule"),
 ("SD-2", "LOCAL", "donnees/collisionneur-question-7-v1/run-question-7-e3-v1/etat.md", None, False, "N6, N1", "pièce de session-depot ; état du run seul, aucune réponse de cellule"),
 ("SD-3", MAIN, "registres/decisions.md", "R:866,868,869,870,871,873", True, "N3, N6, N9", "lignes de session-depot (main)"),
 ("SD-4", MAIN, "docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md", [(1,20),(202,321)], True, "N3, N9", "en-tête, § 4 (test hors échantillon) à § 6 (critère de mort)"),
 ("N9-1", MAIN, "docs/notes/gu-krenn-v1/prereg-gu-krenn-reproduction-et-hors-echantillon-v2.md", [(40,95),(122,140),(220,240)], True, "N9", "hypothèse, prédiction, seuil, B3 et encadré D-GK-1"),
 ("N10-1", MAIN, "docs/notes/anteriorite-P-041-v1/collisionneur-organisme-coevolutif-v1/synthese-organisme-coevolutif-tour2-v1.md", [(1,76)], True, "N10", "verdict et convergences"),
 ("N10-2", MAIN, "registres/decisions.md", "R:880,888,889,890,891", True, "N10", "lignes de session-depot (main)"),
]
RETIRER = set(a for a in sys.argv[3:] if not a.startswith("--"))

MOTIF = re.compile(r"recommand|confiances?\s*(?:d'environ\s*)?[0-9]|confiances? (?:de l'auteur|d'auteur)|"
                   r"\bdéfauts?\s*(?::|=|\((?:[a-e]|[0-9]+)\)|proposé|recommandé|sous 48|à 48|si )|par défaut", re.I)
ENTETE = re.compile(r"^\s*\**\s*(?:recommandations?|confiances?)\b[^|]{0,40}$", re.I)
PROPRE = "[retiré, règle 2 : recommandation ou confiance d'auteur]"


def nettoyer_propositions(texte):
    avant = texte
    texte = re.sub(r"\s*\((?:[^()]|\([^()]*\))*?(?:recommand|confiances?\s*(?:d'environ\s*)?[0-9])(?:[^()]|\([^()]*\))*?\)", "", texte, flags=re.I)
    retire_parenthese = texte != avant
    texte = re.sub(r"\s+recommandée?s?\b(?=\**\s*[:)])", "", texte, flags=re.I)
    if not MOTIF.search(texte):
        return texte + " " + PROPRE if retire_parenthese else texte
    props = re.split(r"(?:(?<=[.;])|(?<=[.;]\*\*)|(?<=[.;]\*))\s+|\s+(?=→)", texte)
    for i, p in enumerate(props):
        if re.match(r"^[\s*_-]*recommandations?\b", p, re.I):
            props_coupees = props[:i]
            break
    else:
        props_coupees = props
    gardees = [p for p in props_coupees if not MOTIF.search(p)]
    if len(gardees) == len(props):
        return texte
    return " ".join(gardees + [PROPRE]).strip()


RELABEL = {  # N9-1 : étiquette neutre au lieu de la recommandation (la question v9 présente les deux options)
    "décision D-GK-1 : recommandée F = ": "décision D-GK-1, option (a) : F = ",
    "si F recommandée est retenue": "si F de l'option (a) est retenue",
    "(texte écrit pour la fenêtre recommandée de D-GK-1)": "(texte écrit pour la fenêtre de l'option (a) de D-GK-1)",
}


def nettoyer(lignes):
    """Règle 2 : colonnes « Recommandation » et « Confiance » retirées des tables ; ailleurs, la proposition porteuse."""
    sortie, retirer = [], None
    for i, l in enumerate(lignes):
        est_table = l.lstrip().startswith("|")
        if not est_table:
            retirer = None
            sortie.append(nettoyer_propositions(l) if MOTIF.search(l) else l); continue
        cell = l.split("|")
        suivante = lignes[i + 1] if i + 1 < len(lignes) else ""
        if re.match(r"^\s*\|[\s:|-]+\|\s*$", suivante) and not re.match(r"^\s*\|[\s:|-]+\|\s*$", l):
            retirer = {j for j, c in enumerate(cell) if ENTETE.search(c)}
        if retirer:
            cell = [c for j, c in enumerate(cell) if j not in retirer]
        cell = [nettoyer_propositions(c) if MOTIF.search(c) else c for c in cell]
        sortie.append("|".join(cell))
    return sortie


def lire(src, chemin):
    if src == "LOCAL":
        return (DEPOT / chemin).read_text(encoding="utf-8")
    return subprocess.run(["git", "-C", str(DEPOT), "show", f"{src}:{chemin}"],
                          capture_output=True, text=True, check=True).stdout


def main():
    blocs, table, total, releve = [], [], 0, []
    for num, src, chemin, plages, regle2, noeuds, note in PIECES:
        if num in RETIRER:
            table.append((num, chemin, "RETIRÉE (budget de mots)", "", 0)); continue
        texte = lire(src, chemin)
        h = hashlib.sha256(texte.encode("utf-8")).hexdigest()
        L = texte.split("\n")
        if plages is None:
            extrait, desc = L, "entier"
        elif isinstance(plages, str):
            ids = plages[2:].split(",")
            extrait = [l for l in L if any(l.startswith(f"| R-{i} |") for i in ids)]
            trouve = [i for i in ids if any(l.startswith(f"| R-{i} |") for l in L)]
            assert trouve == ids, (num, set(ids) - set(trouve))
            desc = "lignes " + ", ".join("R-" + i for i in ids)
        else:
            extrait, morceaux = [], []
            for a, b in plages:
                b = b or len(L)
                if extrait:
                    extrait.append("[…]")
                extrait.extend(L[a - 1:b]); morceaux.append(f"{a}–{b}")
            desc = "l. " + " ; ".join(morceaux)
        if num == "N9-1":
            for a, b in RELABEL.items():
                assert sum(a in l for l in extrait) == 1, (num, a)
                extrait = [l.replace(a, b) for l in extrait]
        if regle2:
            avant = extrait
            extrait = nettoyer(extrait)
            for x, y in zip(avant, extrait):
                if x != y:  # même nombre de lignes : nettoyer ne retire jamais une ligne entière
                    releve.append(f"[{num}] AVANT : {x}\n[{num}] APRÈS : {y}")
        corps = "\n".join(extrait).strip("\n")
        mots = len(corps.split())
        total += mots
        origine = "branche de conv-audit" if src == CA else ("main" if src == MAIN else "dépôt de session-depot (état de run)")
        tete = f"### Pièce {num} — `{chemin}` ({desc}) — nœuds {noeuds}"
        meta = f"Origine : {origine} ; empreinte du fichier source `{h}` ; {mots} mots" + (f" ; {note}" if note else "") + (" ; règle 2 appliquée." if regle2 else ".")
        blocs.append(f"{tete}\n\n{meta}\n\n<<<DÉBUT PIÈCE {num}>>>\n{corps}\n<<<FIN PIÈCE {num}>>>")
        table.append((num, chemin, desc, h, mots))
    return blocs, table, total, releve


blocs, table, total, releve = main()
if RELEVE:
    print("\n".join(releve)); print(f"TOTAL {total} mots", file=sys.stderr); sys.exit(0)
q = (SORTIE.parent / "question-noeuds-decisionnels-collisionneur-v9.md").read_bytes()
hq = hashlib.sha256(q).hexdigest()
tete = f"""# Faits — tour du collisionneur sur les nœuds de décision du 31 octobre 2026 — v1

Assemblés par session-depot le 31 octobre 2026 pour la question v9 de conv-audit (`question-noeuds-decisionnels-collisionneur-v9.md`, sha256 `{hq}`), selon la liste A de `faits-a-assembler-noeuds-v4.md` (`95e12a34…`) et ses changements v2 et v3, plus les pièces de session-depot que la liste nomme et une pièce par nœud nouveau (N9, N10).

Règles appliquées : (1) ni le mémo des décisions en attente ni les avis de conv-audit ; (2) dans les pièces marquées, toute phrase portant une recommandation, une confiance d'auteur ou un défaut est retirée et remplacée par « {PROPRE} » ; les recommandations par nœud sont servies au tour 2 par l'annexe ; (3) table des empreintes en fin de document ; (4) balayage avant scellement (fichier `balayage-faits-noeuds-v1.txt`) ; (5) numéros de ligne recoupés sur le contenu des fichiers de la branche `canal/conv-audit-n04` et de `main` au moment de l'assemblage ; chaque bornage corrigé est noté dans l'en-tête de sa pièce. Les pièces citent des versions antérieures à la dernière (pré-pilote brouillon 7, semi-réel brouillon 3, calcul de puissance v6), parce que la question les nomme : une version plus récente existe pour chacune (brouillon 10, brouillon 5, v9), non servie ici.

Total : {total} mots dans les pièces.

"""
lignes = ["## Table des empreintes", "", "| Pièce | Chemin | Partie | sha256 du fichier source | Mots |", "|---|---|---|---|---:|"]
lignes += [f"| {n} | `{c}` | {d} | `{h}` | {m} |" for n, c, d, h, m in table]
SORTIE.write_text(tete + "\n\n".join(blocs) + "\n\n" + "\n".join(lignes) + "\n", encoding="utf-8")
print(f"{SORTIE} : {total} mots dans les pièces")
