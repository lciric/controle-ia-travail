"""v9 — construit `rapport-puissance-garde-delta-v9.md` depuis le gabarit `rapport-v9-gabarit.md` : les tableaux sont insérés par programme depuis `tableaux-v9.md`
(aucun tableau recopié à la main) ; `{{EMPREINTES}}` devient la liste de tous les fichiers du dossier v9 (sous-dossiers compris) avec leur empreinte, calculée à la
construction, et le contrôle de leurs compagnons `.sha256`. Marqueurs : `{{TABLE:Tn}}` (section « ## Tn. » de tableaux-v9.md, sans son titre), `{{TABLE:T2-288}}`
(sous-section « #### T2-288. »), `{{DATE}}`. Refus si un marqueur reste ou si un compagnon manque ou diffère. Manifeste écrit par ce script (GD8-09).
Usage (depuis le dossier v9) : python3 -I -B construire-rapport-v9.py COMMIT GABARIT TABLEAUX_MD SORTIE.md
"""
import hashlib
import json
import os
import platform
import re
import sys
from datetime import datetime, timezone

COMMIT, GAB, TAB, SORTIE = sys.argv[1:5]
ICI = os.path.dirname(os.path.abspath(__file__))
h = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
texte = open(GAB, encoding="utf-8").read()
tab = open(TAB, encoding="utf-8").read().splitlines()


def section(cle):
    if "-" in cle:  # sous-section ####
        debut = next(i for i, l in enumerate(tab) if l.startswith(f"#### {cle}."))
        fin = next((i for i in range(debut + 1, len(tab)) if tab[i].startswith("#### ") or tab[i].startswith("## ")), len(tab))
    else:
        debut = next(i for i, l in enumerate(tab) if l.startswith(f"## {cle}."))
        fin = next((i for i in range(debut + 1, len(tab)) if tab[i].startswith("## ")), len(tab))
    titre = re.sub(r"^#+\s*", "", tab[debut])
    return f"*{titre}* (inséré depuis `tableaux-v9.md`)\n\n" + "\n".join(tab[debut + 1:fin]).strip() + "\n"


texte = re.sub(r"\{\{TABLE:([A-Za-z0-9-]+)\}\}", lambda m: section(m.group(1)), texte)
texte = texte.replace("{{DATE}}", datetime.now(timezone.utc).strftime("%d/%m/%Y, %H:%M UTC"))
lignes, ecarts, manquants = [], [], []
for racine, dossiers, fichiers in os.walk(ICI):
    dossiers.sort()
    for f in sorted(fichiers):
        p = os.path.join(racine, f)
        rel = os.path.relpath(p, ICI)
        if f.endswith(".sha256") or rel in (SORTIE, "manifeste-" + SORTIE[:-3] + ".json"):
            continue
        e = h(p)
        c = p + ".sha256"
        if not os.path.exists(c):
            manquants.append(rel)
        elif open(c).read().split()[0] != e:
            ecarts.append(rel)
        lignes.append(f"| `{rel}` | `{e}` |")
if ecarts or manquants:
    raise SystemExit(f"refus : compagnons en écart {ecarts} ou manquants {manquants[:20]}")
texte = texte.replace("{{EMPREINTES}}", f"{len(lignes)} fichiers, chacun avec son compagnon `.sha256` (vérifié à la construction : 0 écart, 0 manquant).\n\n"
                      "| fichier | sha256 |\n| --- | --- |\n" + "\n".join(lignes))
if "{{" in texte:
    raise SystemExit("refus : marqueur non remplacé : " + texte[texte.index("{{"):texte.index("{{") + 60])
with open(SORTIE, "x", encoding="utf-8") as f:
    f.write(texte)
man = {"passage": os.path.basename(SORTIE)[:-3], "ecrit_par": os.path.basename(__file__), "commit_lu_par_l_appelant": COMMIT,
       "date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "commande": sys.argv, "script_sha256": h(__file__),
       "graines": "aucun tirage", "environnement": {"python": platform.python_version()},
       "entrees": {os.path.basename(GAB): h(GAB), os.path.basename(TAB): h(TAB)}, "fichiers": {os.path.basename(SORTIE): h(SORTIE)}}
with open("manifeste-" + SORTIE[:-3] + ".json", "x", encoding="utf-8") as f:
    json.dump(man, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("rapport écrit :", SORTIE, h(SORTIE))
