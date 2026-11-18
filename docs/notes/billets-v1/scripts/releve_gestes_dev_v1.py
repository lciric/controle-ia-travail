"""Tâche 4, aide : relevé par programme de traces de gestes de rédaction, sur la SEULE moitié
« développement » (refuse tout chemin de la moitié tenue à l'écart)."""
import json, re, sys

RACINE = "/home/user/billets-corpus-v1/developpement"
m = json.load(open("/home/user/controle-ia-travail/docs/notes/billets-v1/manifeste-corpus-v1.json"))
MOTIFS = {
    "tldr": r"\b(tl;?dr|summary|overview|abstract|key (findings|takeaways|results))\b",
    "statut": r"epistemic (status|state)",
    "images": r"!\[[^\]]*\]\(",
    "tableaux": r"^\s*\|[\s:-]+\|",
    "code": r"github\.com|colab\.research|huggingface\.co",
    "papier": r"arxiv\.org",
    "limites": r"\blimitations?\b|\bcaveats?\b",
    "negatif": r"negative results?|did not work|didn'?t work|failed to|no (significant )?effect",
    "ouvertes": r"open questions?|future work|next steps",
    "bases": r"\bbaselines?\b",
    "choix": r"\bwe (chose|choose|decided|opted)\b|\bwhy we\b|\bbecause\b",
    "contributions": r"\bcontributions?\b|\bwe (show|find|found)\b",
}
out = []
for e in m["billets"]:
    if e["moitie"] != "developpement":
        continue
    t = open(f"{RACINE}/billets/{e['identifiant']}.md").read()
    tete = " ".join(t.split()[:150])
    titres = [l.strip() for l in t.splitlines() if re.match(r"^#{1,3} |^[^\n]+\n[=-]{3,}", l) or
              re.match(r"^\*\*[^*]{3,60}\*\*\s*$", l.strip())]
    lignes = t.splitlines()
    titres += [lignes[i].strip() for i in range(1, len(lignes)) if re.match(r"^[=-]{3,}\s*$", lignes[i]) and lignes[i-1].strip()]
    c = {k: len(re.findall(v, t, re.I | re.M)) for k, v in MOTIFS.items()}
    c["tldr_tete"] = bool(re.search(MOTIFS["tldr"], " ".join(t.split()[:250]), re.I))
    c["statut_tete"] = bool(re.search(MOTIFS["statut"], " ".join(t.split()[:250]), re.I))
    out.append({"id": e["identifiant"], "classe": e["classe"], "score": e["votes_score"],
                "titre": e["titre"], "mots": len(t.split()), "comptes": c, "tete": tete,
                "intertitres": titres[:40]})
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(out))
