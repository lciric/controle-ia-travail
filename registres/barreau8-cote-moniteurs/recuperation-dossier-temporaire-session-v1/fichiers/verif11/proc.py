import sys, subprocess, shutil
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia import prereg
SRC = Path("/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon11.md")
ICI = Path(__file__).parent
t = SRC.read_text(encoding="utf-8")
M1 = "À REMPLIR — À FIXER : tirée par la session mère au scellement"
DEB = "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :"
FIN = "versée avec l'empreinte du texte scellé."
ENT = "123456789012345678901234567890123456789"
GAB = ("- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, "
       "ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucun code ; vérification de la différence "
       "du brouillon 10 au brouillon 11. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon11.md`, "
       "empreinte `32c6da0125e3280e5b15316947f768da5025499613e9be8c97c0f2fb6e08fdf7`. Rapport : "
       "`brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon11-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. "
       "Conclusion : « PRÊT : le brouillon 11 peut être scellé une fois l'entropie des graines versée et cette entrée de "
       "contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par "
       "cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée "
       "remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte "
       "du texte scellé.")
def remplir(t, entropie=True, rapport="2"*64):
    if entropie:
        assert t.count(M1) == 1; t = t.replace(M1, ENT)
    L = t.split("\n")
    idx = [i for i, l in enumerate(L) if l.startswith(DEB) and l.endswith(FIN)]
    assert len(idx) == 1, idx
    L[idx[0]] = GAB.replace("<EMPREINTE DU RAPPORT>", rapport) if rapport else GAB.replace(", empreinte `<EMPREINTE DU RAPPORT>`", "")
    return "\n".join(L)
cas = {"sain": remplir(t), "artefact_entropie_ouverte": remplir(t, entropie=False),
       "artefact_sans_empreinte_rapport": remplir(t, rapport=None)}
for nom, txt in cas.items():
    p = ICI / f"copie-{nom}.md"; p.write_text(txt, encoding="utf-8")
    print(nom, "problemes:", prereg.problemes(p))
    if nom == "sain":
        d = subprocess.run(["diff", str(SRC), str(p)], capture_output=True, text=True).stdout
        print("diff:", [l for l in d.split("\n") if l and l[0].isdigit()])
        print("ligne 76:", txt.split("\n")[75])
        print("deux empreintes distinctes:", len(set(prereg.EMPREINTE.findall(txt.split("\n")[430]))))
