"""Inventaire des épingles de l'empreinte 73be0638… de la garde de calcul, et des expressions de GO à deux chiffres.
Lit origin/main par git (aucun fichier de travail touché). Sortie : Markdown sur la sortie standard."""
import re
import subprocess
import sys

REF = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
EMPREINTE = "73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850"


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout


def grep(motif, *chemins, etendu=False):
    a = ["grep", "-n", "-I"] + (["-E"] if etendu else ["-F"]) + ["-e", motif, REF, "--", *chemins]
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    out = []
    for l in r.stdout.splitlines():
        _, chemin, n, texte = l.split(":", 3)
        out.append((chemin, int(n), texte))
    return out


FAMILLES = [  # (motif de chemin, nom en clair, motif de recherche dans les registres)
    (r"prealables-course-etape-b-bis|t07-etape-b-bis", "feux de l'étape B bis (apprentissage des sondes sur la tâche)",
     r"[ÉéEe]tape B bis|B bis"),
    (r"organisme-bassins-etroits", "lanceur v3 de l'organisme d'idéation « bassins étroits »",
     r"bassins[ -][ée]troits"),
    (r"procedure-pilote-v74", "procédure du pilote v74 de l'organisme (multi-générations)", r"v74"),
    (r"machine-jeu-idee-1-1", "machine du jeu de l'idée du poids du nul", r"jeu de l'idée|idee-1-1|idée 1\.1"),
    (r"etape-a-t07", "préalables de l'étape A de T0.7", r"[ÉéEe]tape A\b"),
    (r"registres/decisions\.md", "registre des décisions (journal)", None),
    (r"\.claude/hooks/garde_calcul\.py\.sha256", "compagnon de la garde (mis à jour par la demande n° 71)", None),
]


def famille(chemin):
    for motif, nom, cle in FAMILLES:
        if re.search(motif, chemin):
            return nom, cle
    return "autre", None


def derniere_mention(cle):
    """Dernière ligne datée du registre des décisions et des passations qui cite la famille."""
    if cle is None:
        return "—", "—"
    dec = grep(cle, "registres/decisions.md", etendu=True)
    rs = [t for _, _, t in dec if re.match(r"- R-\d+ \(20", t) and not re.match(r"- R-(5013|5026) ", t)]
    der_dec = "aucune"
    if rs:
        t = rs[-1]
        m = re.match(r"- (R-\d+) \((\S+?)[,)\s]", t)
        der_dec = f"{m.group(1)} ({m.group(2)})" if m else t[:40]
    pas = sorted({c for c, _, _ in grep(cle, "registres/passations", etendu=True)
                  if re.search(r"/20\d\d-\d\d-\d\d-\d{4}", c)})
    der_pas = pas[-1].split("/")[-1] if pas else "aucune"
    return der_dec, der_pas


def date_commit(chemin):
    return git("log", "-1", "--format=%cs %h", REF, "--", chemin).strip()


print("## 1. Pièces qui épinglent l'empreinte de la garde `73be0638…`\n")
print(f"Référence lue : `{REF}` = `{git('rev-parse', '--short', REF).strip()}`. Recherche : `git grep -F 73be0638`"
      " (forme abrégée comprise). Décisions R-5013 et R-5026 (la correction elle-même) exclues des colonnes de mention.\n")
lignes = grep("73be0638")
par_chemin = {}
for c, n, t in lignes:
    par_chemin.setdefault(c, []).append((n, t))
print(f"{len(lignes)} lignes dans {len(par_chemin)} fichiers.\n")
print("| fichier | lignes | forme | famille | dernière décision qui cite la famille |"
      " dernière passation qui cite la famille |")
print("|---|---|---|---|---|---|")
for c in sorted(par_chemin, key=lambda x: (famille(x)[0], x)):
    nom, cle = famille(c)
    ns = ", ".join(str(n) for n, _ in par_chemin[c])
    forme = "entière" if any(EMPREINTE in t for _, t in par_chemin[c]) else "abrégée"
    dd, dp = derniere_mention(cle)
    print(f"| `{c}` | {ns} | {forme} | {nom} | {dd} | {dp} |")

print("\n## 2. Fichiers de `src/` et `scripts/` qui gardent l'expression de GO à deux chiffres\n")
motif2 = r"GO-\\d\{4\}-\\d\{2\}-\\d\{2\}-\\d\{2\}([^,]|$)"
l2 = grep(motif2, "src", "scripts", etendu=True)
p2 = {}
for c, n, t in l2:
    p2.setdefault(c, []).append(n)
print(f"Recherche : `git grep -E '{motif2}'` (rang `\\d{{2}}` non suivi de `,`, donc hors `\\d{{2,3}}`)."
      f" {len(l2)} lignes dans {len(p2)} fichiers.\n")
print("| fichier | lignes |")
print("|---|---|")
for c in sorted(p2):
    print(f"| `{c}` | {', '.join(map(str, p2[c]))} |")
