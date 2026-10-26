import hashlib, pathlib
d = pathlib.Path("/home/claude/pilote4/essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/objet-v6-2-1-v1")
src = d / "mots-de-lazar-2026-10-25-26-v4.md"; dst = d / "mots-de-lazar-2026-10-25-26-v5.md"
t = src.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode()).hexdigest().startswith("7e0837e6")
assert not dst.exists()
t = t.replace("(relevé verbatim) — v4", "(relevé verbatim) — v5", 1)
old = "de R-466 à R-472 (`main`, `3c94802`)."
assert t.count(old) == 1
t = t.replace(old, old + " La v5 reprend la v4 (`7e0837e6…`) mot pour mot et ajoute le message de 02:17.", 1)
marker = "| 02:10 | compte rendu de session-depot collé par Lazar"
i = t.index(marker); j = t.index("\n", i)
row = "\n| 02:17 | « Recommandation : (a), confiance moyenne-haute : go; des boucles « proposer, tester, éliminer, itérer » menées par des agents existent déjà (par exemple « The AI Scientist », Sakana AI, 2024 ; « AlphaEvolve », Google DeepMind, 2025 — à vérifier) : : va lire leurs papiers et la litterature sur le sujet pour t'en inspirer, que le collisionneur fasse de meme » | **(a) retenue** : boucle extérieure à la fin de chaque course du pilote 4 (agents neufs : analyste, correcteur, contre-lecteur ; registre d'hypothèses écrit avant tout score ; relance sur le mot de Lazar) ; la boucle intérieure est le chantier R-471 de session-depot ; lecture de la littérature par un sous-agent (fiche sur PDF empreinté) ; question au collisionneur `question-litterature-boucles-agents-collisionneur-v1.md` (`962130b7…`, canal `a65dbfd`), dépense soumise au mot de Lazar chez session-depot |"
t = t[:j] + row + t[j:]
dst.write_text(t, encoding="utf-8")
h = hashlib.sha256(dst.read_bytes()).hexdigest()
(d / (dst.name + ".sha256")).write_text(f"{h}  {dst.name}\n", encoding="utf-8")
print(h)
