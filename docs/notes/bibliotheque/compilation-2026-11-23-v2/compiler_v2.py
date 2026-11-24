"""Compilation navigable du dépôt distant (GO-2026-11-23-09), version 2. Classe C (travail), session bibliothécaire.
Entrée : un miroir sans contenus (git fetch --filter=blob:none de toutes les branches) ; les contenus ne sont lus que sur main
et seulement pour des fichiers de registres/ ou docs/decisions/ ouverts par la liste stricte. Branches cloisonnées
(coffre/, verdict/, calcul/, lecture/, archives/journaux-mere-) : noms, commits, empreintes git (identifiants d'objets) seulement.
Usage : python -I compiler_v2.py MIROIR.git SORTIE_DIR V1_DIR
Nouveau en v2 : passations citées sans branche porteuse (noms de fichiers seuls, toutes branches) ; 08 nouveautés depuis la v1 (branches neuves, têtes déplacées, branches disparues).
"""
import importlib.util, os, re, subprocess, sys, collections

ICI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("ll3", os.path.join(ICI, "../../memoire-conception-v1/fusion-outils-v1/listes_lecture_v3.py"))
ll3 = importlib.util.module_from_spec(_s); _s.loader.exec_module(ll3)

M, OUT, V1 = sys.argv[1], sys.argv[2], sys.argv[3]
CLOISONNE = re.compile(r"^(coffre/|verdict/|calcul/|lecture/|archives/journaux-mere-|quarantaine|prep/quarantaine-|lot/compte-4-v1|matiere-premiere/)")

def git(*a, check=True):
    r = subprocess.run(["git", "-C", M, *a], capture_output=True, text=True)
    if check and r.returncode: raise RuntimeError(r.stderr[:300])
    return r.stdout

CHANTIERS = [
 ("saboteur et sondes", r"saboteur|sonde|iib|ii-b|sabotage|lentille"),
 ("bras A (moniteurs, organismes discrets)", r"bras-a|relance-bras|moniteur|discret|pensive-bardeen"),
 ("organisme d'idéation et organisme", r"organisme|ideation|idees|exploration"),
 ("T0.8 (chaîne, course)", r"^t08/|t08"),
 ("barreau 5", r"barreau|b5f|-b5|marche-b5|formation-b5"),
 ("G1 (énoncé, tiers, avis)", r"^g1/|g1-|avis/g1"),
 ("papiers A, B, C", r"papier|^papier-c|juge/"),
 ("collisionneurs et protocole X", r"collisionn|protocole-x|astra|carbon|neon|raisons-ou-regard|puits"),
 ("veille de cap et bibliothèque", r"veille|bibliothe|memoire|compilation"),
 ("mathématiques", r"mathematiques"),
 ("gardes, outils et scellement", r"^garde/|garde|outils/|scellement|habilite|service/"),
 ("passations, état, archives, versements", r"passation|^etat|archives|verse|recuperation|sauvegarde|journal"),
 ("canaux et échanges entre sessions", r"^canal/"),
 ("données, préparations, essais, calcul (noms seuls)", r"^donnees/|^prep/|^essai|^calcul/|^runs/|^diag/|kits-abonnement|^ordres?/|^course/|^rapports/|^traces/|^pilotes/"),
]
def chantier(b):
    for nom, rx in CHANTIERS:
        if re.search(rx, b): return nom
    return "autres"

def role(b):
    p = b.split("/")[0]
    return {"canal":"canal d'échange","calcul":"calcul (cloisonné)","coffre":"coffre (cloisonné)","verdict":"verdict (cloisonné)","lecture":"lecture (cloisonné)",
            "donnees":"données brutes","prep":"préparation","essai":"essai","outils":"outil","claude":"session de travail","avis":"avis de conseiller",
            "kits-abonnement":"kit d'abonnement","course":"course","ordres":"ordre de course","ordre":"ordre de course","t08":"chaîne T0.8"}.get(p, p)

# 1. branches
refs = git("for-each-ref", "--format=%(refname:short)\t%(objectname:short=9)\t%(committerdate:short)", "refs/heads").splitlines()
rows = []
for l in refs:
    b, c, d = l.split("\t")
    clo = bool(CLOISONNE.match(b))
    names = git("ls-tree", "-r", "--name-only", f"refs/heads/{b}", "--", "registres/passations").splitlines() if not clo else []
    pas = sorted([n for n in names if n.endswith(".md") and "passation" in n.lower() or re.search(r"/\d{4}-\d{2}-\d{2}-\d{4}", n) and n.endswith(".md")])
    rows.append((chantier(b) if not clo else "cloisonné (noms et commits seulement)", b, c, d, role(b), pas[-1].split("/")[-1] if pas else ""))
rows.sort()
g = collections.defaultdict(list)
for r in rows: g[r[0]].append(r)

def ecrire(nom, texte):
    with open(os.path.join(OUT, nom), "x", encoding="utf-8") as f: f.write(texte)

L = ["# 1. Index des branches par chantier — compilation du 23 novembre 2026 (v2)", "",
     f"Classe C. {len(rows)} branches distantes (git ls-remote). Colonnes : branche, tête (9 signes), date de la tête, rôle, passation la plus récente portée par la branche (nom seul).", ""]
for nom in sorted(g, key=lambda k: (k.startswith("cloisonné"), k)):
    L += [f"## {nom} ({len(g[nom])})", "", "| branche | tête | date | rôle | passation la plus récente |", "|---|---|---|---|---|"]
    L += [f"| {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |" for r in g[nom]] + [""]
ecrire("01-index-des-branches-v2.md", "\n".join(L))

# 1bis. cloisonnées : empreintes git (identifiants d'objets) sans contenu
L = ["# 1 bis. Branches cloisonnées : noms de fichiers et identifiants d'objets git (aucun contenu ouvert, aucune taille : une taille exigerait de télécharger le contenu)", ""]
for r in rows:
    if r[0].startswith("cloisonné"):
        ent = git("ls-tree", "-r", f"refs/heads/{r[1]}", check=False).splitlines()
        L += [f"## {r[1]} — tête {r[2]}, {r[3]}, {len(ent)} fichiers", ""]
        L += [f"- `{e.split(chr(9))[1]}` {e.split()[2][:12]}" for e in ent[:40]]
        if len(ent) > 40: L.append(f"- … {len(ent)-40} autres (voir `git ls-tree -r`)")
        L.append("")
ecrire("01bis-branches-cloisonnees-inventaire-v2.md", "\n".join(L))

# fichiers de main (noms)
tout = git("ls-tree", "-r", "--name-only", "refs/heads/main").splitlines()
def lire_main(p):
    if not ll3.autorise_stricte(p): return None
    return git("show", f"refs/heads/main:{p}", check=False)

# 2. décisions
dec = sorted(p for p in tout if p.startswith("docs/decisions/") and p.endswith(".md") and not p.startswith("docs/decisions/brouillons/"))
L = ["# 2. Index des hypothèses, revendications et décisions (docs/decisions)", "", f"{len(dec)} fichiers sur main. Titre = première ligne ; état = ligne contenant « État » ou « Statut » si présente (sinon « non indiqué »).", "", "| fichier | titre | état |", "|---|---|---|"]
for p in dec:
    t = lire_main(p)
    if t is None: L.append(f"| {p.split('/')[-1]} | (hors liste stricte) | |"); continue
    ls = t.splitlines()
    titre = ls[0].lstrip("# ").strip()[:140] if ls else ""
    etat = next((x.strip()[:140] for x in ls[:30] if re.search(r"\b(État|Etat|Statut)\b", x)), "non indiqué")
    L.append(f"| {p.split('/')[-1]} | {titre.replace('|','/')} | {etat.replace('|','/')} |")
ecrire("02-index-decisions-et-revendications-v2.md", "\n".join(L) + "\n")

# 3. pistes et idées (noms seuls pour la veille ; brainstorms)
bs = sorted(p for p in tout if p.startswith("docs/notes/") and re.search(r"brainstorm|idee|ideation|piste|exploration|hypothese|remue|mentor", p, re.I) and p.endswith(".md"))
vc = [p for p in tout if p.startswith("registres/veille")]
L = ["# 3. Index des pistes et idées", "", "Le registre des idées de la veille de cap vit sous registres/veille-de-cap/ : je n'en lis pas le contenu (liste stricte) ; noms seuls.", ""]
L += [f"- {p}" for p in vc if not p.endswith(".sha256")]
L += ["", f"## Notes d'idées, d'exploration et de remue-méninges sur main ({len(bs)})", ""] + [f"- {p}" for p in bs]
ecrire("03-index-des-pistes-et-idees-v2.md", "\n".join(L) + "\n")

# 4. échecs
L = ["# 4. Index des échecs et faux échecs", "", "Lignes des registres arrets.md et decisions.md qui contiennent « faux échec », « jamais parti », « non évaluable », « non concluant », « verdict valide » ; puis passations dont le nom évoque un échec.", ""]
for reg in ("registres/arrets.md", "registres/decisions.md"):
    t = lire_main(reg) or ""
    hits = [x[:300] for x in t.splitlines() if re.search(r"faux échec|jamais parti|non évaluable|non concluant", x, re.I)]
    L += [f"## {reg} — {len(hits)} lignes", ""] + [f"- {h}" for h in hits[:200]] + [""]
L += ["## Passations dont le nom évoque un échec", ""] + [f"- {p}" for p in tout if p.startswith("registres/passations/") and re.search(r"echec|arret|panne", p) and p.endswith(".md")]
ecrire("04-index-des-echecs-et-faux-echecs-v2.md", "\n".join(L) + "\n")

# 5. réponses des modèles externes et collisionneurs
rep = sorted(p for p in tout if p.startswith("docs/") and re.search(r"collisionn|protocole-x|reponses?-|notes?-collisionneur|carbon|neon|astra|argon", p, re.I) and not re.search(r"archives-reponses-modeles|ne-pas-lire|consigne-privee|conception-ii-b|verite|rendu|scores", p))
dossiers = collections.Counter("/".join(p.split("/")[:4]) for p in rep)
L = ["# 5. Index des réponses des modèles externes et des collisionneurs", "", "Par dossier de main (nombre de fichiers) ; le dossier archives-reponses-modeles n'est pas listé (cloisonné). Notes pédagogiques de collisionneur : fichiers dont le nom porte « note ».", ""]
L += [f"- {d} : {n} fichiers" for d, n in sorted(dossiers.items())]
L += ["", "## Notes pédagogiques de collisionneur", ""] + [f"- {p}" for p in rep if re.search(r"note", p.split('/')[-1], re.I) and p.endswith(".md")]
ecrire("05-index-reponses-modeles-et-collisionneurs-v2.md", "\n".join(L) + "\n")

# 6. GO et décisions ouvertes
etat = lire_main("registres/etat.md") or ""
ls = etat.splitlines()
def section(titre):
    out, on = [], False
    for x in ls:
        if x.startswith("## "):
            if on: break
            on = x.startswith("## " + titre)
        elif on: out.append(x[:400])
    return out
L = ["# 6. GO en attente et décisions ouvertes (copie de registres/etat.md à la date de la compilation)", "", "## GO et nœuds en attente", ""] + section("GO et nœuds en attente") + ["", "## Décisions ouvertes (défaut sous 48 heures)", ""] + section("Décisions ouvertes")
ecrire("06-go-en-attente-et-decisions-ouvertes-v2.md", "\n".join(L) + "\n")

# 7. trous : branches citées par l'index des passations et absentes
idx = lire_main("registres/passations/index-passations-2026-11-23-v1.md") or ""
cit = set(re.findall(r"(?<![\w/.-])((?:claude|prep|lot|t08|g1|avis|juge|essais|service|garde|sondes-v2|conseiller-activations-b5|conducteur-b5f|lecture|coffre|donnees|calcul|verdict)/[\w./-]+)", idx))
bset = {r[1] for r in rows}
manq = sorted(c for c in cit if c.rstrip(".,;)") not in bset)

# 7b. passations citées par l'index et absentes de tout arbre de branche (noms seuls, ls-tree)
pcit = sorted(set(re.findall(r"((?:passation[\w.-]*|\d{4}-\d{2}-\d{2}-\d{4}[\w.-]*)\.md)", idx)))
noms_par_branche = {}
for r in rows:
    noms_par_branche[r[1]] = {n.split("/")[-1] for n in git("ls-tree", "-r", "--name-only", f"refs/heads/{r[1]}", check=False).splitlines()}
sans = [p for p in pcit if not any(p in v for v in noms_par_branche.values())]
SANS = [f"{len(pcit)} noms de passation cités par l'index ; {len(sans)} sans aucune branche qui porte un fichier de ce nom :", ""] + ([f"- {p}" for p in sans] or ["- aucune"])
L = ["# 7. Trous", "", "## Branches citées par l'index des passations du 23 novembre et absentes du dépôt distant", ""] + ([f"- {c}" for c in manq] or ["- aucune"])
L += ["", "## Passations sans branche porteuse identifiée", "", *SANS, "",
      "## Limites de cette compilation", "", "- Rôle et chantier : classés par le nom de la branche (règles dans compiler_v2.py), jamais par le contenu.",
      "- Tailles des fichiers des branches cloisonnées : non données (exigeraient de télécharger le contenu).",
      "- Registre des idées de la veille de cap, registres sous veille-de-cap/ : contenu non lu (liste stricte)."]
ecrire("07-trous-v2.md", "\n".join(L) + "\n")
print(len(rows), "branches;", len(dec), "décisions;", len(manq), "citées absentes")

# 8. nouveautés depuis la v1
v1 = {}
for l in open(os.path.join(V1, "01-index-des-branches-v1.md"), encoding="utf-8"):
    c = [x.strip() for x in l.split("|")]
    if len(c) > 3 and c[2] and re.fullmatch(r"[0-9a-f]{7,12}", c[2]): v1[c[1]] = c[2]
for l in open(os.path.join(V1, "01bis-branches-cloisonnees-inventaire-v1.md"), encoding="utf-8"):
    m = re.match(r"## (\S+) — tête ([0-9a-f]+),", l)
    if m: v1[m.group(1)] = m.group(2)
neuves = [r for r in rows if r[1] not in v1]
bougees = [r for r in rows if r[1] in v1 and not r[2].startswith(v1[r[1]][:7])]
parties = sorted(b for b in v1 if b not in bset)
L = ["# 8. Nouveautés depuis la compilation v1 (07:11Z)", "", f"Branches neuves : {len(neuves)} ; têtes déplacées : {len(bougees)} ; branches disparues : {len(parties)}.", "",
     "## Branches neuves", "", "| branche | tête | date | chantier |", "|---|---|---|---|"] + [f"| {r[1]} | {r[2]} | {r[3]} | {r[0]} |" for r in neuves]
L += ["", "## Têtes déplacées", "", "| branche | tête v1 | tête v2 | date | chantier |", "|---|---|---|---|---|"] + [f"| {r[1]} | {v1[r[1]]} | {r[2]} | {r[3]} | {r[0]} |" for r in bougees]
L += ["", "## Branches disparues", ""] + ([f"- {b} (tête v1 {v1[b]})" for b in parties] or ["- aucune"])
ecrire("08-nouveautes-depuis-v1-v2.md", "\n".join(L) + "\n")
print(len(neuves), "neuves;", len(bougees), "déplacées;", len(parties), "disparues;", len(sans), "passations sans porteuse")
