import subprocess, sys
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.prereg import problemes

D = Path("/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif9")
SRC = Path("/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md")
t = SRC.read_text(encoding="utf-8")
lignes = t.split("\n")
ENT = "123456789012345678901234567890123456789"
M1 = "À REMPLIR — À FIXER : tirée par la session mère au scellement"
DEB = "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :"
FIN = "versée avec l'empreinte du texte scellé."
E1 = "1" * 64
E2 = "2" * 64


def entree(e_relu, e_rapport):
    s = ("- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, "
         "ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; vérification de la différence du brouillon 8 "
         "au brouillon 9. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, "
         f"empreinte `{e_relu}`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon9-v1.md`")
    if e_rapport:
        s += f", empreinte `{e_rapport}`"
    s += (". Conclusion : « PRÊT : le brouillon 9 peut être scellé une fois l'entropie des graines versée et cette entrée de "
          "contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette "
          "contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le "
          "marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.")
    return s


def remplir(entropie=True, rapport=True):
    L = list(lignes)
    assert t.count(M1) == 1
    i = [k for k, l in enumerate(L) if l.startswith(DEB)]
    assert len(i) == 1 and L[i[0]].endswith(FIN)
    if entropie:
        j = [k for k, l in enumerate(L) if M1 in l]
        L[j[0]] = L[j[0]].replace(M1, ENT)
    L[i[0]] = entree(E1, E2 if rapport else None)
    return "\n".join(L)


for nom, kw in [("sain", {}), ("art-sans-rapport", {"rapport": False}), ("art-entropie-ouverte", {"entropie": False})]:
    p = D / f"copie-{nom}.md"
    p.write_text(remplir(**kw), encoding="utf-8")
    print(nom, problemes(p))
    if nom == "sain":
        r = subprocess.run(["diff", str(SRC), str(p)], capture_output=True, text=True)
        print([l for l in r.stdout.splitlines() if l[:1].isdigit()])
        print([l[:60] for l in r.stdout.splitlines() if l.startswith(">")])
