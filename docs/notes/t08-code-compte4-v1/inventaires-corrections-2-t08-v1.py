"""Compte les éléments nommés par chaque message d'échec des essais d'inventaire (sortie de pytest -q dans un fichier),
au grain de la contre-lecture 1 : chaînes entre guillemets des lignes « E » de chaque échec (un échec se clôt à sa
ligne « tests/<fichier>.py:<n>: AssertionError ») ; affiche les seuls éléments de T0.8 (les noms d'autrui sont
comptés, jamais affichés)."""
import re, sys
texte = open(sys.argv[1], encoding="utf-8").read().splitlines()
sections, E = [], []
for l in texte:
    if l.startswith("E "):
        E.append(l)
        continue
    f = re.match(r"^(tests/test_\S+\.py):\d+: AssertionError", l)
    if f:
        sections.append((f.group(1), E)); E = []
for fichier, ls in sections:
    elems = []
    for l in ls:
        elems += re.findall(r"'([^']+)'", l)
    vus = list(dict.fromkeys(elems))
    t08 = [e for e in vus if "t08" in e]
    print(f"{fichier} : éléments {len(vus)} / T0.8 {len(t08)} / autres {len(vus) - len(t08)}")
    for e in t08:
        print(f"    T0.8 : {e}")
