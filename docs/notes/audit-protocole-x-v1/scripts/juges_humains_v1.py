"""Tire l'échantillon mêlé pour les juges humains à l'aveugle (Lazar ou un mentor).

15 propositions retenues et 15 non retenues ou « à reprendre », tirées au hasard (graine dérivée), hors
« règles de texte », une par dossier au plus dans chaque groupe tant que possible ; noms de modèles,
lettres et marques de soutien retirés ; ordre mélangé. Fiche servable aux juges et clé séparée.
Sorties : ../juges-humains/fiche-juges-v1.md (servable) ; ../reponses-ne-pas-servir/cle-juges-v1.json.
"""
import json
import re
import sys

from audit_commun_v2 import SORTIES, graine

ICI = SORTIES.parent


def masquer(t):
    """Garde le seul énoncé : premier segment avant « : », « — » ou la première phrase ; retire parenthèses,
    cellules de lettre, motifs de rejet et comptes de soutien (ils trahiraient le statut)."""
    m = re.match(r"^\s*(?:\d+[.)]\s*|[-|]\s*)?\*\*(.+?)\*\*", t)
    if m and len(m.group(1)) > 25:
        t = m.group(1)
    t = re.sub(r"^\s*\|?\s*[A-I]?\s*\|\s*", "", t)          # cellule de lettre d'un tableau
    cel = [c for c in re.split(r"\s*\|\s*", t) if c.strip()]
    if len(cel) > 1:
        t = next((c for c in cel if len(c) >= 25), cel[0])        # première cellule utile d'un tableau
    t = re.sub(r"\([^)]*\)", "", t)
    t = re.split(r"\s:\s|\s—\s|(?<=[a-zé])\.\s", t)[0]
    t = re.sub(r"\*\*|\*|`", "", t)
    t = re.sub(r"(?i)\b(fable|opus|argon|carbon|neon|astra|kimi|gpt[-\w.]*|gemini[-\w.]*|claude[-\w.]*)\b", "[modèle]", t)
    t = re.sub(r"(?<![A-Za-zÀ-ÿ])([A-I])(?=\s*[,;)]|\s+et\s+[A-I]\b)", "[x]", t)
    t = re.sub(r"(?i)(soutien[^.]*\.|port[ée]e? par[^.|]*|les (trois|quatre|cinq|six|sept) )", "", t)
    t = re.sub(r"^\s*(\d+[.)]|[-|])\s*", "", t)
    return re.sub(r"\s+", " ", t).strip(" .;,")[:300]


def tirer(groupe, n, rng):
    par = {}
    for j in groupe:
        par.setdefault(j["dossier"], []).append(j)
    dossiers = sorted(par)
    rng.shuffle(dossiers)
    choix = []
    tour = 0
    while len(choix) < n and any(par.values()):
        for d in dossiers:
            if par[d] and len(choix) < n:
                k = int(rng.integers(len(par[d])))
                choix.append(par[d].pop(k))
        tour += 1
    return choix


def main():
    J = json.loads((SORTIES / "jeu-des-propositions-v1.json").read_text())
    J = [j for j in J if j["nature"] == "proposition" and len(j["texte"]) > 60]
    # énoncés jugeables seulement : au moins 30 signes après masquage, ni liste d'exclusions ni reste de tableau
    J = [j for j in J if len(masquer(j["texte"])) >= 30 and not re.match(r"^(les?|la|l'|\d)", masquer(j["texte"]))]
    rng, meta = graine("juges-humains-echantillon")
    ret = tirer([j for j in J if j["genre"] == "retenue"], 15, rng)
    non = tirer([j for j in J if j["genre"] != "retenue"], 15, rng)
    tous = ret + non
    ordre = rng.permutation(len(tous))
    fiche = ["# Fiche des juges — propositions du protocole X, à l'aveugle (v1)", "",
             "Trente propositions issues de dossiers différents, mêlées. Ni modèle, ni source, ni statut ne sont donnés. Pour chacune, note de 1 à 5 :",
             "", "- **Testabilité** : une épreuve décisive peu chère est-elle évidente ?",
             "- **Nouveauté** : est-elle neuve pour toi, au regard de la littérature que tu connais ?",
             "- **Survie attendue** : chance qu'elle survive à son épreuve (en pourcentage).",
             "- **Priorité** : la financerais-tu ce mois-ci (oui ou non) ?", "",
             "Compte environ 45 minutes. Ne consulte ni le dépôt ni un modèle pendant la notation.", ""]
    cle = []
    for k, i in enumerate(ordre):
        j = tous[int(i)]
        fiche.append(f"**J-{k + 1:02d}.** {masquer(j['texte'])}")
        fiche.append("")
        fiche.append("Testabilité : _ ; Nouveauté : _ ; Survie attendue : _ % ; Priorité : _")
        fiche.append("")
        cle.append({"fiche": f"J-{k + 1:02d}", "id": j["id"], "genre": j["genre"], "dossier": j["dossier"],
                    "especes_porteuses": j["especes_porteuses"]})
    (ICI / "juges-humains").mkdir(exist_ok=True)
    (ICI / "juges-humains" / "fiche-juges-v1.md").write_text("\n".join(fiche) + "\n")
    (ICI / "reponses-ne-pas-servir" / "cle-juges-v1.json").write_text(json.dumps({"graine": meta, "cle": cle}, ensure_ascii=False, indent=1))
    print(len(ret), len(non), len({c["dossier"] for c in cle}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
