"""Assemble les faits v2 du collisionneur des nœuds (question v12, liste A v6). Usage : assembler-v2.py DEPOT SORTIE [--releve].

Différences avec assembler-v1.py : pièces de conv-audit lues au commit d'envoi de la liste A v6 (règle 5) ; pièces de
session-depot n° 20 et 21 recopiées telles qu'assemblées dans faits-noeuds-v1.md ; pièce 24 = extraits de Bailey et
collègues préparés à part (piece-24-bailey-v1.md) ; chaque identifiant de registre doit apparaître une seule fois.
"""
import hashlib, re, subprocess, sys
from pathlib import Path

DEPOT, SORTIE = Path(sys.argv[1]), Path(sys.argv[2])
RELEVE = "--releve" in sys.argv
ENVOI = "e5410a42"  # commit d'envoi de la liste A v6 sur canal/conv-audit-n04 (12:56 UTC)
MAIN = "origin/main"
P = "brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/"
PP = P + "pre-pilote-course-2-v1/"
B10 = PP + "preenregistrement-pre-pilote-course-2-brouillon10.md"
LV = P + "bisociation-deux-espaces-v1/experience-v2/lancement-v2/"
SR5 = "prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon5.md"
NOEUDS = DEPOT / "donnees/collisionneur-noeuds-v1"
FAITS_V1 = NOEUDS / "faits-noeuds-v1.md"
EXTRAIT_24 = Path(__file__).resolve().parent.parent / "piece-24-bailey-v1.md"
NOTE_COLLISION = ("la liste A v6 écrit « lignes de `main` » pour R-630 à R-685 ; sur `main`, ces numéros portent d'autres "
                  "décisions (collision d'identifiants entre lignées, R-892) ; servies depuis la branche de conv-audit, comme "
                  "dans les faits v1, parce que leur contenu est celui que les nœuds citent (R-660 : verdict de la validation "
                  "de la bisociation v2)")

# (numéro, source, chemin, plages, règle 2, nœuds, note)
PIECES = [
 ("1", ENVOI, LV + "verdict-validation-v1.md", None, True, "N1", ""),
 ("2", ENVOI, LV + "diagnostic-v5-v1/diagnostic-v5-v1.md", None, True, "N1", ""),
 ("3", ENVOI, "prereg/preenregistrement-bisociation-deux-espaces-v2.md", [(283,300),(555,586),(617,688),(689,735)], True, "N1", ""),
 ("4", ENVOI, B10, [(5,17),(18,80)], True, "N3, N4", "résumé et table des seuils et décisions"),
 ("5", ENVOI, B10, [(254,254)], True, "N4", "prédiction P14"),
 ("6", ENVOI, B10, [(412,418)], True, "N5", "ordre des étapes, règle de lecture, É5"),
 ("7", ENVOI, B10, [(622,628),(665,667)], True, "N5", "liste d'arrêt A15 à A21 ; table R5, lignes 30 à 32"),
 ("8", ENVOI, B10, [(722,732)], True, "N3", "« Décisions à Lazar » : en-tête, D-g à D-j"),
 ("9", ENVOI, PP + "calcul-puissance-pre-pilote-course-2-v9.sortie.txt", [(182,190)], True, "N4", ""),
 ("10", ENVOI, PP + "contre-lecture-annexe-bras-meta-v1-brouillon1.md", [(19,22),(49,87),(125,None)], True, "N4", ""),
 ("11", ENVOI, PP + "annexe-bras-meta-v1-brouillon1.md", [(18,30),(85,102),(116,224)], True, "N4", ""),
 ("12", ENVOI, "docs/notes/ideation-organisme-v1/contre-lecture-cl19-orchestrateur-v54-v1.md", [(14,22),(100,114),(149,172)], True, "N5", ""),
 ("13", ENVOI, "docs/notes/ideation-organisme-v1/orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md", [(65,105)], True, "N5", ""),
 ("14", ENVOI, "docs/notes/ideation-organisme-v1/orchestrateur-v54/LISEZMOI-orchestrateur-pole-v7-v54.md", [(95,120)], True, "N5", "borne de fin portée à 120 (choix 10 à 12), comme dans les faits v1"),
 ("15", ENVOI, SR5, [(9,21),(22,148),(150,157),(158,189)], True, "N6", ""),
 ("16", ENVOI, SR5, [(335,355),(666,666)], True, "N6", ""),
 ("17", ENVOI, SR5, [(598,627)], True, "N6", ""),
 ("18", ENVOI, "prereg/brouillons/verification-identification-semi-reel-v1-brouillon5.md", [(14,23)], True, "N6", ""),
 ("19", MAIN, "docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md", [(22,40)], True, "N1", "verdict seul"),
 ("20", "V1", "SD-3 SD-4 N9-1", None, False, "N3, N9", "pièces de session-depot gardées telles qu'assemblées dans les faits v1"),
 ("21", "V1", "N10-1 N10-2", None, False, "N10", "pièces de session-depot gardées telles qu'assemblées dans les faits v1"),
 ("22", ENVOI, P + "arene-melange-equilibre-v1/preenregistrement-arene-melange-equilibre-v1-brouillon3.md", [(117,151),(434,451)], True, "N10", ""),
 ("23", ENVOI, P + "arene-melange-equilibre-v1/contre-lecture-arene-melange-v3-brouillon3.md", [(7,10),(61,67)], True, "N10", ""),
 ("24", "EXTRAIT", "docs/sources/pdf/2412.09565v2.pdf", None, False, "N10", "extraits par pdftotext (p. 3, 23, 25–26), une phrase retirée (règle 4)"),
 ("25", ENVOI, "registres/decisions.md", "R:630,634,635,638,643,660,661,674,675,678,679,680,685,718,719,733,739", True, "tous", NOTE_COLLISION + " ; R-718, R-719, R-733, R-739 : branche de conv-audit, comme la liste le dit"),
 ("26a", MAIN, "registres/decisions.md", "R:910", True, "N11", "demande du directeur, verbatim ; proposition de session-depot retirée (règle 2)"),
 ("26b", MAIN, "docs/decisions/decision-N-058-v1.md", None, True, "N11", "texte scellé de la décision N-058"),
]
RETIRER = set(a for a in sys.argv[3:] if not a.startswith("--"))
# Règle 2 sans objet (aucune recommandation d'auteur ; faux positifs seulement) : 1, 2 (négations « n'est pas une
# recommandation »), 3 (seuils gelés par Lazar « égaux à la recommandation », texte scellé), 19 (« selon le défaut » =
# option par défaut d'une décision), 26b (texte scellé d'une décision de Lazar).
SANS_REGLE2 = {"1", "2", "3", "19", "26b"} | set(a[len("--sans-regle2="):] for a in sys.argv[3:] if a.startswith("--sans-regle2="))
R2 = "⟦R2⟧"  # retrait manuel, remplacé par PROPRE après nettoyage
TRANCHE = "tranchée par Lazar le 31 octobre"
# Remplacements faits à la main avant nettoyage (chaque ancien texte doit apparaître une seule fois dans la pièce).
# Pièce 4 et R-674 : « recommandée » nommait la configuration D-g (b), D-h (a), D-i (2), tranchée par Lazar le
# 31 octobre (10:32–10:33 UTC, R-718, R-719) : ce n'est plus une recommandation mais un fait ; D-j reste ouverte (N3) et
# sa recommandation est retirée par la règle 2. Pièce 15 : intitulé d'option rendu sans le mot. Pièce 22 et R-679 :
# seule la recommandation est retirée, les faits voisins restent ; « une par défaut du banc » = défaillance du banc.
REMPLACEMENTS = {
 "4": [
  ("**et sur la configuration recommandée (D-g b, D-i 2 : 0,173)**", f"**et sur la configuration {TRANCHE} (D-g b, D-i 2 : 0,173)**"),
  ("(0,631 recommandée)", "(0,631 configuration tranchée)"),
  ("porte 0,173 (0,167) recommandée,", "porte 0,173 (0,167) configuration tranchée,"),
  ("**C13 budget 0,926 (0,897) recommandée,", "**C13 budget 0,926 (0,897) configuration tranchée,"),
  ("dépense médiane 40,1 USD (42,3) recommandée,", "dépense médiane 40,1 USD (42,3) configuration tranchée,"),
  ("**fusions retirées 0,20 (0,57) recommandée,", "**fusions retirées 0,20 (0,57) configuration tranchée,"),
  ("(configuration recommandée, porte d'emblée)", "(configuration tranchée, porte d'emblée)"),
  ("(0,074 recommandée)", "(0,074 configuration tranchée)"),
  ("USD (40,1 recommandée),", "USD (40,1 configuration tranchée),"),
  ("0,74 recommandée, sensibilité", "0,74 configuration tranchée, sensibilité"),
  ("(§ 3.3, configuration recommandée : sacrifice", "(§ 3.3, configuration tranchée : sacrifice"),
  ("≈ 1,4 USD, recommandé ; ou déclarer le vide)", f"≈ 1,4 USD, option (b), {TRANCHE} ; ou déclarer le vide)"),
  ("(retarder le gel jusqu'à l'annexe, recommandé ;", f"(retarder le gel jusqu'à l'annexe, option (a), {TRANCHE} ;"),
  ("sortie v9 ; recommandé)", f"sortie v9 ; option (2), {TRANCHE})"),
  ("**≈ 32,1 USD pour la configuration recommandée**", "**≈ 32,1 USD pour la configuration tranchée**"),
  ("(texte 30,1 ; recommandée 32,1)", "(texte 30,1 ; tranchée 32,1)"),
  ("Le script v9 les joue par défaut :", "Le script v9 les joue d'office :"),
 ],
 "15": [
  ("Option 1 — geler toutes les recommandations en une ligne.", "Option 1 — geler en une ligne toutes les valeurs proposées par l'auteur (non servies ici)."),
  ("**Sections touchées par une option non recommandée (CS4-12).** Si Lazar choisit une autre option que la recommandation, ces sections sont à réécrire (version nouvelle, R12) :",
   "**Sections touchées selon l'option retenue (CS4-12).** Selon l'option que Lazar retient, ces sections sont à réécrire (version nouvelle, R12) :"),
 ],
 "22": [(" ; recommandation 0,10)", ")" + R2)],
 "26a": [(re.compile(r"Proposition \(« proposer avec recommandation ».*$"), R2 + " | — |")],
 "25": [
  (", selon mes recommandations : (1) **Q2 gardée**", " : (1) **Q2 gardée**"),
  ("(une par défaut du banc, refaite : garde éprouvée)", "(une pour chaque défaut du banc, refaite : garde éprouvée)"),
  ("recommandation : amender A21 et la ligne 30, journaliser la lecture au coffre, ne pas lire la clé d'antériorité en É9 (liste de réduction scellée), ordre des appels d'É6 tiré ou trié par identifiant.", R2),
  ("(34,6 en configuration recommandée D-g b / D-i 2)", f"(34,6 en configuration {TRANCHE}, D-g b / D-i 2)"),
  ("**recommandation 50 / 45 avec plafonds de relais du brouillon 5 rendus souples pour les étapes protégées**", "**configuration retenue par Lazar (GO-2026-10-31-03) : 50 / 45 avec plafonds de relais du brouillon 5 rendus souples pour les étapes protégées**"),
 ],
}
# Lignes servies sans nettoyage : citations verbatim de décisions de Lazar (« je recommande 50 USD plutôt que 45. : ok »).
EXEMPTES = {"4": ["décisions de Lazar du 31 octobre 2026, lues sur `origin/main`"],
            "25": ["| R-719 |"]}  # R-719 : décisions de Lazar seulement (dont la règle « confiance ≤ 0,6 → option collisionneur »)

MOTIF = re.compile(r"recommand|confiances?\s*(?:d'environ\s*)?[0-9]|confiances? (?:de l'auteur|d'auteur)|"
                   r"\bdéfauts?\s*(?::|=|\((?:[a-e]|[0-9]+)\)|proposé|recommandé|sous 48|à 48|si )|par défaut", re.I)
ENTETE = re.compile(r"^\s*\**\s*(?:recommandations?|confiances?|options? recommandées?)\b[^|]{0,40}$", re.I)
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


def nettoyer(lignes, exemptes=()):
    """Règle 2 : colonnes « Recommandation » et « Confiance » retirées des tables ; ailleurs, la proposition porteuse."""
    sortie, retirer = [], None
    for i, l in enumerate(lignes):
        if any(e in l for e in exemptes):
            sortie.append(l); continue
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


def git_show(ref, chemin):
    return subprocess.run(["git", "-C", str(DEPOT), "show", f"{ref}:{chemin}"], capture_output=True, text=True, check=True).stdout


def blocs_v1(ids):
    """Recopie des blocs de faits-noeuds-v1.md, en-tête et méta compris, sans aucun changement."""
    t = FAITS_V1.read_text(encoding="utf-8")
    morceaux = []
    for i in ids:
        m = re.search(rf"^### Pièce {re.escape(i)} — .*?<<<FIN PIÈCE {re.escape(i)}>>>", t, re.S | re.M)
        assert m, ("bloc absent des faits v1", i)
        morceaux.append(m.group(0))
    return morceaux


def main():
    blocs, table, total, releve = [], [], 0, []
    hv1 = hashlib.sha256(FAITS_V1.read_bytes()).hexdigest()
    for num, src, chemin, plages, regle2, noeuds, note in PIECES:
        if num in RETIRER:
            table.append((num, chemin, "RETIRÉE (budget de mots)", "", 0)); continue
        if num in SANS_REGLE2:
            regle2 = False
        if src == "V1":
            for b in blocs_v1(chemin.split()):
                corps = b.split("<<<DÉBUT PIÈCE", 1)[1]
                mots = len(corps.split("\n", 1)[1].rsplit("<<<FIN", 1)[0].split())
                total += mots
                bid = re.match(r"### Pièce (\S+)", b).group(1)
                blocs.append(b.replace(f"### Pièce {bid} — ", f"### Pièce {num} ({bid}) — ", 1)
                             .replace(f"<<<DÉBUT PIÈCE {bid}>>>", f"<<<DÉBUT PIÈCE {num} ({bid})>>>")
                             .replace(f"<<<FIN PIÈCE {bid}>>>", f"<<<FIN PIÈCE {num} ({bid})>>>"))
                table.append((f"{num} ({bid})", "recopie de `donnees/collisionneur-noeuds-v1/faits-noeuds-v1.md`", "bloc entier, inchangé", hv1, mots))
            continue
        if src == "EXTRAIT":
            texte = EXTRAIT_24.read_text(encoding="utf-8")
            h = hashlib.sha256((DEPOT / chemin).read_bytes()).hexdigest()
            extrait, desc = texte.split("\n"), "extraits p. 3, 23, 25–26"
        else:
            texte = git_show(src, chemin)
            h = hashlib.sha256(texte.encode("utf-8")).hexdigest()
            L = texte.split("\n")
            if plages is None:
                extrait, desc = L, "entier"
            elif isinstance(plages, str):
                ids = plages[2:].split(",")
                for i in ids:
                    n = sum(l.startswith(f"| R-{i} |") for l in L)
                    assert n == 1, (num, f"R-{i}", n)
                extrait = [l for l in L if any(l.startswith(f"| R-{i} |") for i in ids)]
                desc = "lignes " + ", ".join("R-" + i for i in ids)
            else:
                extrait, morceaux = [], []
                for a, b in plages:
                    b = b or len(L)
                    if extrait:
                        extrait.append("[…]")
                    extrait.extend(L[a - 1:b]); morceaux.append(f"{a}–{b}")
                desc = "l. " + " ; ".join(morceaux)
        brut = extrait
        for vieux, neuf in REMPLACEMENTS.get(num, []):
            if isinstance(vieux, re.Pattern):
                n = sum(len(vieux.findall(l)) for l in extrait)
                assert n == 1, ("remplacement", num, vieux.pattern[:60], n)
                extrait = [vieux.sub(neuf, l) for l in extrait]
                continue
            n = sum(l.count(vieux) for l in extrait)
            assert n == 1, ("remplacement", num, vieux[:60], n)
            extrait = [l.replace(vieux, neuf) for l in extrait]
        if regle2:
            extrait = nettoyer(extrait, EXEMPTES.get(num, ()))
        extrait = [l.replace(")" + R2, ") " + PROPRE).replace(R2, PROPRE) for l in extrait]
        for x, y in zip(brut, extrait):
            if x != y:
                releve.append(f"[{num}] AVANT : {x}\n[{num}] APRÈS : {y}")
        if REMPLACEMENTS.get(num) or EXEMPTES.get(num):
            note = (note + " ; " if note else "") + "remplacements ou exemptions écrits à la main avant la règle 2 (liste et raisons dans `assembler-v2.py`, versé avec ces faits)"
        corps = "\n".join(extrait).strip("\n")
        mots = len(corps.split())
        total += mots
        origine = {ENVOI: f"branche de conv-audit au commit d'envoi `{ENVOI}`", MAIN: "main", "EXTRAIT": "PDF de `main`, extraits"}[src]
        tete = f"### Pièce {num} — `{chemin}` ({desc}) — nœuds {noeuds}"
        meta = f"Origine : {origine} ; empreinte du fichier source `{h}` ; {mots} mots" + (f" ; {note}" if note else "") + (" ; règle 2 appliquée." if regle2 else ".")
        blocs.append(f"{tete}\n\n{meta}\n\n<<<DÉBUT PIÈCE {num}>>>\n{corps}\n<<<FIN PIÈCE {num}>>>")
        table.append((num, chemin, desc, h, mots))
    return blocs, table, total, releve


blocs, table, total, releve = main()
if RELEVE:
    print("\n".join(releve)); print(f"TOTAL {total} mots", file=sys.stderr); sys.exit(0)
q = (NOEUDS / "question-noeuds-decisionnels-collisionneur-v12.md").read_bytes()
hq = hashlib.sha256(q).hexdigest()
hl = hashlib.sha256((NOEUDS / "faits-a-assembler-noeuds-v6.md").read_bytes()).hexdigest()
tete = f"""# Faits — tour du collisionneur sur les nœuds de décision du 31 octobre 2026 — v2

Assemblés par session-depot le 31 octobre 2026 pour la question v12 de conv-audit (`question-noeuds-decisionnels-collisionneur-v12.md`, sha256 `{hq}`), selon la liste A v6 (`faits-a-assembler-noeuds-v6.md`, sha256 `{hl}`). Remplacent les faits v1 (question v9 et v10, liste A v4), qui restent archivés.

Règles appliquées : (1) ni le mémo des décisions en attente, ni la fiche des décisions du pré-pilote, ni les avis ou analyses de conv-audit ; (2) dans les pièces marquées, toute phrase portant une recommandation, une confiance d'auteur ou un défaut est retirée et remplacée par « {PROPRE} » ; les recommandations par nœud sont servies au tour 2 par l'annexe v5 ; (3) table des empreintes en fin de document ; (4) balayage avant scellement (fichier `balayage-faits-noeuds-v2.txt`) : rien de `donnees/` hormis les pièces de session-depot déjà assemblées, aucune clé ni jeton, aucun texte de fiche réelle, aucun contenu d'attaque ; (5) numéros de ligne recoupés sur le contenu des fichiers au commit d'envoi `{ENVOI}` de la branche `canal/conv-audit-n04` (pièces inchangées depuis à la tête de la branche) et sur `main` ; chaque bornage corrigé ou chaque écart à la liste est noté dans l'en-tête de sa pièce.

Total : {total} mots dans les pièces.

"""
lignes = ["## Table des empreintes", "", "| Pièce | Chemin | Partie | sha256 du fichier source | Mots |", "|---|---|---|---|---:|"]
lignes += [f"| {n} | `{c}` | {d} | `{h}` | {m} |" for n, c, d, h, m in table]
SORTIE.write_text(tete + "\n\n".join(blocs) + "\n\n" + "\n".join(lignes) + "\n", encoding="utf-8")
print(f"{SORTIE} : {total} mots dans les pièces")
