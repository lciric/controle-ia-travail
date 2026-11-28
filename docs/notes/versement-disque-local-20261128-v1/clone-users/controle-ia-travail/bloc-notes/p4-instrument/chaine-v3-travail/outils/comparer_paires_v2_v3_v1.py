"""Comparaison des paires de la chaîne v3 à celles de la chaîne v2 et aux « Texte à ajouter » des deux vérifications :
paires inchangées égales ; blocs des rapports recopiés mot pour mot (blocs de code du rapport « dépense » : à l'identique,
sauts de ligne compris ; phrases du rapport « données » : à espaces près, le rapport les cite sur une ligne).
Usage : python3 -I -B comparer_paires_v2_v3_v1.py PAIRES_V2 PAIRES_V3 RAPPORT_DEPENSE RAPPORT_DONNEES"""
import json, re, sys
v2, v3 = (json.load(open(x, encoding="utf-8")) for x in sys.argv[1:3])
dep, don = (open(x, encoding="utf-8").read() for x in sys.argv[3:5])
ok = len(v2) == len(v3) == 11 and all(a["ancien"] == b["ancien"] for a, b in zip(v2, v3))
print(f"onze paires, mêmes ancres : {ok}")
changees = [i + 1 for i, (a, b) in enumerate(zip(v2, v3)) if a["nouveau"] != b["nouveau"]]
print(f"paires dont le « nouveau » change : {changees}")
ok &= changees == [2, 5, 7, 9, 11]
ok &= all(a == b for i, (a, b) in enumerate(zip(v2, v3)) if i + 1 not in changees)
blocs = re.findall(r"```\n(.*?)\n```", dep.split("## Texte à ajouter au candidat")[1], re.S)
print(f"blocs du rapport « dépense » : {len(blocs)}")
for k, (b, i) in enumerate(zip(blocs, (1, 8))):
    r = b in v3[i]["nouveau"]
    print(f"  bloc {k + 1} recopié à l'identique dans la paire {i + 1} : {r}"); ok &= r
sec = don.split("## Texte à ajouter")[1].split("## Méthode")[0]
# phrases à ajouter : citations « … » de plus de 50 caractères qui finissent par un point (les autres citations de la
# section désignent une ancre : « paragraphes », « … une ligne qui porte … »)
phrases = [x for x in re.findall(r"« (.*?) »", sec, re.S) if len(x) > 50 and x.rstrip().endswith(".") and not x.startswith("…")]
print(f"phrases du rapport « données » : {len(phrases)}")
norm = lambda s: " ".join(s.split())
n7 = norm(v3[6]["nouveau"])
for p in phrases:
    if p.startswith("jamais dans l'arbre contrôlé.") :
        continue                                  # ancien segment remplacé (phrase 4), pas une phrase à ajouter
    r = norm(p) in n7
    print(f"  phrase « {norm(p)[:60]}… » dans la paire 7 (à espaces près) : {r}"); ok &= r
r = "jamais dans l'arbre contrôlé." not in n7
print(f"  ancien « jamais dans l'arbre contrôlé. » remplacé : {r}"); ok &= r
print("PAIRES : CONFORMES" if ok else "PAIRES : ÉCART")
sys.exit(0 if ok else 1)
