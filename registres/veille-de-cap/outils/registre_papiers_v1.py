"""Registre vivant des papiers et fiches « décidé, non lancé » au journal des idées — veille de cap, v1 (23 novembre 2026).
Classe B, non contre-lu. Entrée : la sortie JSONL de papiers_du_depot_v1.py. Sorties : le registre Markdown (une ligne de
600 signes au plus par papier) et une partie neuve du journal (naissances P- des papiers « decide », extrait mot pour mot de
la ligne de décision qui les cite). Rang : chantier déduit du dossier de versement et du texte de décision (table CHANTIERS),
puis statut. Usage : python3 -I registre_papiers_v1.py ENTREE.jsonl COMMIT REGISTRE.md JOURNAL_BASE.jsonl PARTIE.jsonl QUAND"""
import importlib.util, json, os, re, subprocess, sys
ENT, COMMIT, REG, JBASE, PARTIE, QUAND = sys.argv[1:7]
RAC = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
s = importlib.util.spec_from_file_location("pj", os.path.join(RAC, "docs/notes/memoire-conception-v1/fusion-outils-v1/partition_journal_v3.py"))
pj = importlib.util.module_from_spec(s); s.loader.exec_module(pj)
INTERNES = re.compile(r"CV_|_CV_|/cv-v9/|memoire-conception-v1-copie-pdf|collisionneur-v9/notes-de-sortie|rapports-directeur|candidature-taif")
CHANTIERS = [  # (motif sur chemins + décision, chantier, poids)
    (r"Diffuse|fuzzy|controle-diffus|2611\.04556|2611\.10620|2609\.03035", "entretien du 1er décembre", 6),
    (r"mecanisme-adjudant|adjudant-opus|percee-controle-securite|science-de-la-detection|protocole-x-attaquant|lie-detector|N-075|N-076|N-047|N-077|marge-asymetrique|steganographie|lentille|neuron", "saboteur et sondes (G1)", 5),
    (r"couverture-de-l-oracle|dommages-plantes|audit-recapture|N-060", "bras A (oracle, dommages)", 4),
    (r"anteriorite-P-041|N-067|N-069|N-073|N-064|N-071|arxiv-26|exploration-idees|ideation|society-ai-scientists|co-scientist|popper|good-1953", "organisme d'idéation", 3),
    (r"juges-de-cartes|universalite|programmation-de-poids", "hors des trois chantiers (G0/G1 à terme)", 2),
    (r"mathematiques-nouvelles", "mathématiques nouvelles (gelé)", 1),
]
STATUTS = {"verse": "versé, jamais cité", "cite": "lu ou cité, aucune exploitation décidée", "decide": "exploitation décidée, rien de lancé",
           "lance": "exploitation lancée"}
def chantier(e):
    txt = " ".join(e["chemins"]) + " " + (e["premier_decide"] or [""])[0] + " " + " ".join(e["decisions"])
    for m, nom, p in CHANTIERS:
        if re.search(m, txt): return nom, p
    return "non rattaché", 0
def action(e):
    if e["statut"] == "decide":
        d = (e["premier_decide"] or ["?", 0])
        return f"lecture sur PDF des passages que cite {os.path.basename(d[0])} (ligne {d[1]}), note de lecture d'une page, pages citées (R7)"
    if e["statut"] == "verse":
        return "lecture du résumé et de l'introduction sur PDF ; classer : à citer (papier A, B ou C), à tester, ou hors cap, avec décision nommée"
    if e["r7"]: return "vérifier sur PDF, page citée, le chiffre de la ligne qui le cite (R7)"
    return "—"
L = [json.loads(l) for l in open(ENT, encoding="utf-8")]
for e in L:
    e["interne"] = bool(INTERNES.search(" ".join(e["chemins"])))
    e["chantier"], e["poids"] = chantier(e)
ordre = {"decide": 0, "verse": 1, "cite": 2, "lance": 3}
L.sort(key=lambda e: (e["interne"], ordre[e["statut"]], -e["poids"], e["cle"]))
from collections import Counter
papiers = [e for e in L if not e["interne"]]
cpt = Counter(e["statut"] for e in papiers)
lignes = ["# Papiers du dépôt — registre vivant de la veille de cap (v1)", "",
  f"Fichier vivant (registres/veille-de-cap/). Dernier calcul : {QUAND}, commit `{COMMIT[:8]}`, par `outils/papiers_du_depot_v1.py` et `outils/registre_papiers_v1.py` (classe B, non contre-lus). Demande de Lazar du 23 novembre vers 06:20Z, relayée par la mère (R-5147).", "",
  "**Méthode et limites.** Aucun PDF n'est ouvert : la boucle ne lit les PDF que par leur nom (liste de lecture v3, « noms seuls »). Un papier = une clé (identifiant arXiv, sinon nom de fichier sans extension) ; ses copies sont regroupées. Statut par recherche de la clé dans les 12 201 textes ouvrables au bras « boucle » (docs/notes, docs/decisions, docs/sources, registres permis, papiers/) ; `prereg/` n'est lu que par ses noms. **Heuristiques déclarées** : « lancée » = citée dans une note de lecture ou de vérification sur PDF ; « décidée » = citée dans docs/decisions/ ou une ligne R-/GO- des registres ; « R7 ? » = une ligne de décision ou de préenregistrement cite la clé avec un nombre décimal ou un pourcentage sans page : **à vérifier, pas un défaut établi**. Titres non établis (PDF non ouverts) : le nom de fichier en tient lieu.", "",
  f"**Comptes** (hors {sum(e['interne'] for e in L)} pièces internes : CV, copies PDF de notes, rapports au directeur) : " +
  " ; ".join(f"{STATUTS[k]} {cpt[k]}" for k in ("verse", "cite", "decide", "lance")) + f" ; drapeau R7 à vérifier {sum(e['r7'] for e in papiers)}. Total {len(papiers)}.", "",
  "**Rang** : statut prioritaire (décidé, puis versé), puis utilité : entretien du 1er décembre > saboteur et sondes (G1) > bras A > organisme > autres. Plus petite action proposée en dernière colonne.", "",
  "| rang | clé | statut | chantier | versé le | empreinte | chemin (premier) | R7 ? | citations | décision | plus petite action |", "|---|---|---|---|---|---|---|---|---|---|---|"]
for i, e in enumerate(papiers, 1):
    dec = ", ".join(e["decisions"]) or (os.path.basename(e["premier_decide"][0]) if e["premier_decide"] else "")
    l = f"| {i} | {e['cle'][:50]} | {STATUTS[e['statut']]} | {e['chantier']} | {e['verse_le']} | `{e['empreinte'][:12]}` | `{e['chemins'][0][:110]}`{' (+'+str(len(e['chemins'])-1)+')' if len(e['chemins'])>1 else ''} | {'oui' if e['r7'] else ''} | {e['n_citations']} | {dec[:70]} | {action(e) if e['statut'] in ('decide','verse') or e['r7'] else ''} |"
    assert len(l) <= 600, l
    lignes.append(l)
lignes += ["", "## Pièces internes (hors registre des papiers)", ""] + [f"- `{e['chemins'][0]}` — {STATUTS[e['statut']]}" for e in L if e["interne"]]
with open(REG, "x", encoding="utf-8") as f: f.write("\n".join(lignes) + "\n")
# fiches au journal
journal_txt = "".join(open(p, encoding="utf-8").read() for p in sorted({JBASE} | {os.path.join(os.path.dirname(JBASE), x) for x in os.listdir(os.path.dirname(JBASE)) if x.startswith(os.path.basename(JBASE)[:-6] + "-partie-") and x.endswith(".jsonl")}))
maxp = max(int(m) for m in re.findall(r'"fiche": ?"P-(\d{4})"', journal_txt))
out, sautes = [], []
for e in papiers:
    if e["statut"] != "decide": continue
    if e["cle"] in journal_txt: sautes.append(e["cle"]); continue
    chem, num = e["premier_decide"]
    ligne = subprocess.run(["git", "-C", RAC, "show", f"{COMMIT}:{chem}"], capture_output=True).stdout.decode().split("\n")[num - 1]
    j = ligne.find(e["cle"]); deb = max(0, j - 120)
    while deb > 0 and ligne[deb - 1] != " ": deb -= 1
    ext = ligne[deb:deb + 280].rstrip()
    while len(ext) > 1 and ext[-1] != " " and deb + len(ext) < len(ligne): ext = ext[:-1]
    ext = ext.strip()
    dec = (e["decisions"] or re.findall(r"N-0\d\d|P-0\d\d", os.path.basename(chem)) or ["?"])[0]
    maxp += 1
    ev = {"quand": QUAND, "fiche": f"P-{maxp:04d}", "evenement": "naissance",
          "nom": f"Exploiter le papier {e['cle']} (exploitation décidée par {dec}, rien de lancé)", "etat": "retenue",
          "source": {"chemin": chem, "commit": COMMIT[:8], "repere": f"ligne {num}", "extrait": ext},
          "porteur": "synthèse ou décision", "sert": e["chantier"], "issue": None, "raison": None, "reveil": None,
          "mots": ["papier", e["cle"][:40], "exploitation", dec], "origine": QUAND[:10], "derniere_trace": QUAND[:10],
          "decision": dec, "note": f"boucle des papiers du dépôt ; plus petite action : {action(e)} ; PDF : {e['chemins'][0]}"}
    bas = pj.ll2.sans_accents(" ".join([ev["nom"], *ev["mots"], ev["sert"], ext])).lower()
    if any(m in bas for m in pj.MOTS_INTERDITS): sautes.append(e["cle"] + " (nom exclu)"); maxp -= 1; continue
    out.append(json.dumps(ev, ensure_ascii=False))
with open(PARTIE, "x", encoding="utf-8") as f: f.write("\n".join(out) + "\n")
print(json.dumps({"papiers": len(papiers), "internes": sum(e["interne"] for e in L), "statuts": cpt, "fiches": len(out), "sautes": sautes}, ensure_ascii=False))
