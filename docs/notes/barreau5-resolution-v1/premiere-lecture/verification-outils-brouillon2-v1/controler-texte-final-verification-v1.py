"""Controle, pour la session mere, du texte et du devis qu'elle ecrira a partir des brouillons 2 : chaque couple du
verificateur (couples-proposes-verification-v1.json, meme dossier) est applique (« apres » present une fois, « avant »
parti) ; chaque « apres » de la contre-lecture reste present, sauf ceux que le verificateur change expres ; le validateur
des preenregistrements est appele sur le texte. N'ecrit que la sortie nommee. Aucun score ouvert.
Usage : python3 -B controler-texte-final-verification-v1.py <racine du depot> <texte> <devis> <sortie .json>
"""
import json
import re
import sys
from pathlib import Path

RACINE = Path(sys.argv[1]).resolve()
TEXTE, DEVIS = Path(sys.argv[2]).read_text(encoding="utf-8"), Path(sys.argv[3]).read_text(encoding="utf-8")
ICI = Path(__file__).parent
RAPPORT = RACINE / "docs/notes/barreau5-resolution-v1/premiere-lecture/contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md"
CHANGES_EXPRES = {"M4.1": "V2", "M8.1": "V5", "M7.2": "V10"}


def couples_du_rapport(md):
    lignes = md[md.index("## 2. Remarques numérotées"):md.index("## 3. Outils de la contre-lecture")].split("\n")
    entete = re.compile(r"^\*\*Correction (\S+)\*\* \((texte|devis) : `([^`]+)` ;")
    out, i = [], 0
    while i < len(lignes):
        m = entete.match(lignes[i])
        if not m:
            i += 1
            continue
        blocs = []
        for etiquette in ("Avant :", "Après :"):
            while lignes[i] != etiquette:
                i += 1
            i += 2
            bloc = []
            while i < len(lignes) and lignes[i].startswith(">"):
                bloc.append(lignes[i][2:] if lignes[i].startswith("> ") else lignes[i][1:])
                i += 1
            blocs.append("\n".join(bloc))
        out.append(dict(id=m.group(1), genre=m.group(2), avant=blocs[0], apres=blocs[1]))
    return out


cible = {"texte": TEXTE, "devis": DEVIS}
sortie = {"couples_du_verificateur": [], "couples_de_la_contre_lecture": [], "anomalies": []}
for c in json.loads((ICI / "couples-proposes-verification-v1.json").read_text(encoding="utf-8")):
    n_ap, n_av = cible[c["genre"]].count(c["apres"]), cible[c["genre"]].count(c["avant"])
    sortie["couples_du_verificateur"].append(dict(id=c["id"], apres=n_ap, avant=n_av))
    if n_ap != 1 or (n_av != 0 and c["avant"] not in c["apres"]):
        sortie["anomalies"].append(c["id"])
for c in couples_du_rapport(RAPPORT.read_text(encoding="utf-8")):
    n = cible[c["genre"]].count(c["apres"])
    sortie["couples_de_la_contre_lecture"].append(dict(id=c["id"], apres=n, change_par=CHANGES_EXPRES.get(c["id"])))
    if c["id"] not in CHANGES_EXPRES and n < 1:
        sortie["anomalies"].append(c["id"])
sys.path.insert(0, str(RACINE / "src"))
from controle_ia.prereg import problemes  # noqa: E402

sortie["validateur"] = problemes(Path(sys.argv[2]))
sortie["pret"] = not sortie["anomalies"] and not sortie["validateur"]
Path(sys.argv[4]).write_text(json.dumps(sortie, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({k: sortie[k] for k in ("anomalies", "validateur", "pret")}, ensure_ascii=False, indent=1))
