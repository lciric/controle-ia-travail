# Correctif v4 du texte pilote4-gemini-organisme-v4.md : décisions de Lazar de 02:05 à 02:17 (26 octobre 2026, Paris),
# lignes R-464 à R-472 lues, relevé v5, point 3 (agents neufs), point 4 bis (graines : texte nouveau), pièces.
# Chaque remplacement exige une occurrence unique ; sinon arrêt sans écrire.
import hashlib, pathlib, sys

p = pathlib.Path("/home/claude/pilote4/essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md")
t = p.read_text(encoding="utf-8")
h0 = hashlib.sha256(t.encode("utf-8")).hexdigest()
assert h0.startswith("dcc98d09"), h0

R = []

def rep(old, new):
    n = t.count(old)
    if n != 1:
        sys.exit(f"occurrences = {n} pour : {old[:80]!r}")
    R.append((old, new))

# 1. Statut
rep("sur les décisions de Lazar de 23:54 à 01:56 Paris (§ Décisions)",
    "sur les décisions de Lazar de 23:54 à 02:17 Paris (§ Décisions)")
rep("corrigée à partir de 01:03 UTC, après la contre-lecture 5 et les décisions de 01:48 à 01:56.",
    "corrigée à partir de 01:03 UTC, après la contre-lecture 5 et les décisions de 01:48 à 01:56 ; complétée à partir de\n01:16 UTC pour les décisions de 02:05 à 02:17 (boucle extérieure, graines, littérature).")

# 2. Ce qui a été lu
rep("les lignes R-445 à R-463 du registre des décisions de `main` (mots de Lazar,\n"
    "départs du collisionneur et du test H-M1, prononcé du test H-M1 v3 — R-459 : sa mesure principale déclarée non valide,\n"
    "aucun verdict — ; aucun score d'un pilote) ;",
    "les lignes R-445 à R-472 du registre des décisions de `main` (`3c94802` ; mots de Lazar,\n"
    "départs du collisionneur et du test H-M1, prononcé du test H-M1 v3 — R-459 : sa mesure principale déclarée non valide,\n"
    "aucun verdict —, refus consignés du collisionneur, GO de Lazar sur la primitive d'expérience bornée — R-471 — ; aucun\n"
    "score d'un pilote) et le brouillon de dessin de cette primitive (`docs/notes/dessin-primitive-experience-v1.md`, `main`\n"
    "`ce25bcc` ; aucun score) ; les messages n° 55 et 56 de session-depot (26 octobre, 00:36 et 01:03 UTC) et son compte rendu\n"
    "à Lazar que celui-ci a collé dans la session de conv-audit à 02:10 Paris (coûts et états des tours du collisionneur ;\n"
    "aucun score) ;")

# 3. Relevé v5
rep("`objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v3.md` (§ Pièces).",
    "`objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v5.md` (§ Pièces ; la v5 reprend les v1 à v4 mot pour mot).")

# 4. § Décisions : puce 02:05 à 02:17 après la puce 01:54 à 01:56
rep("  recommandation de conv-audit et l'avis du collisionneur (01:56) ; ce texte n'en dépend pas.\n",
    "  recommandation de conv-audit et l'avis du collisionneur (01:56) ; ce texte n'en dépend pas.\n"
    "- **02:05 à 02:17** : « je veux un pilote qui sépare du bruit, pilote 4 le fait-il ? » (02:05) — réponse de conv-audit :\n"
    "  non, à une course par objet (point 4 bis : dans une course, seuls des changements au-delà du bruit des tâches sont\n"
    "  lisibles ; aucune comparaison entre objets) ; décision soumise, dépense sans défaut : (a) trois graines par objet\n"
    "  (quatre courses de plus, lanceur dérivé, texte nouveau), recommandée ; (b) cinq ; (c) garder une course par objet.\n"
    "  **Sans réponse à l'écriture de ce texte : ce texte garde une course par objet** ; des graines de plus se feraient par\n"
    "  un texte nouveau (version nouvelle, R12) et un GO nouveau, jamais par ce texte ; ses deux courses n'en seraient les\n"
    "  premières graines que si ce texte nouveau le dit avant toute lecture de leurs scores. Puis (02:06, renvoyé à 02:07) :\n"
    "  « et je veux un pilote qui appelle des agents qui font les tests et éliminent les hypothèses fausses et font relancer un\n"
    "  nouveau tour ou une nouvelle génération de l'organisme » ; décision soumise à 02:07 : (a) une **boucle extérieure**\n"
    "  entre les courses (agents neufs) puis une **boucle intérieure** dans la course (noyau nouveau) ; (b) l'intérieure\n"
    "  d'abord ; (c) l'extérieure seule. À 02:10, Lazar a collé le compte rendu de session-depot : son « go » dans la session\n"
    "  de session-depot (R-471, vers 01:09 UTC) a déjà tranché la boucle intérieure (primitive d'expérience bornée dans le\n"
    "  noyau, par une version nouvelle du noyau ; « aucun pilote scellé n'est modifié ») ; conv-audit a retiré cette moitié.\n"
    "  **02:17 : « go » sur (a)**, désormais la boucle extérieure seule : à la fin de chaque course de ce pilote, des agents\n"
    "  neufs de conv-audit (un analyste, un correcteur, un contre-lecteur) exécutent la lecture des points 3 et 4 bis selon un\n"
    "  **registre d'hypothèses de conception écrit avant tout score**, statuent par hypothèse (éliminée, tenue, indécidable\n"
    "  dans le bruit), proposent la ronde suivante ; toute relance est une course nouvelle, nommée et versionnée, sur le mot\n"
    "  direct de Lazar dans la session de session-depot (dépense). Lazar a aussi demandé la lecture des papiers de telles\n"
    "  boucles (« The AI Scientist », « AlphaEvolve » et la littérature ; fiche de lecture sur PDF empreinté, R7) et la même\n"
    "  lecture par le collisionneur (question `question-litterature-boucles-agents-collisionneur-v1.md`, `962130b7…`, canal\n"
    "  `a65dbfd` ; dépense soumise à son mot). **Ce texte n'en dépend pas** : ses deux courses partent telles quelles, sur le\n"
    "  noyau `8e5e2f7b` inchangé ; le registre d'hypothèses, le protocole et les briefs des agents sont des pièces nouvelles,\n"
    "  poussées sur le canal avec leurs empreintes avant la fin de la première course, qui ne modifient ni ce texte ni ses\n"
    "  règles de lecture ; aucune hypothèse du registre ne porte sur la manière de classer une tâche, et rien du registre ni\n"
    "  des verdicts des agents n'est servi à un organisme.\n")

# 5. § Plan, point 3 : agents neufs
rep("de `test` et les faits mécaniques peuvent l'être après la fin d'une course, pour corriger un organisme.\n",
    "de `test` et les faits mécaniques peuvent l'être après la fin d'une course, pour corriger un organisme. La lecture de fin\n"
    "   de course peut être exécutée par des agents neufs de conv-audit (boucle extérieure, § Décisions, 02:05 à 02:17) ;\n"
    "   ils n'ouvrent rien avant la fin de la course, ne lisent ni textes de tâches, ni vérités, ni fichiers de clé, et ne\n"
    "   changent ni ce texte ni ses règles ; ce qu'ils concluent sur la banque v3 est exploratoire.\n")

# 6. Point 4 bis : graines
rep("aussi » ; option (a), sans course de plus) :",
    "aussi » ; option (a), sans course de plus ; la décision de 02:05 sur des graines de plus, § Décisions, ne change pas ce\n"
    "   texte) :")

# 7. Pièces : relevé v1 à v5
rep("le relevé verbatim des mots de Lazar, v1 à v3)",
    "le relevé verbatim des mots de Lazar, v1 à v5)")

for old, new in R:
    t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
h1 = hashlib.sha256(t.encode("utf-8")).hexdigest()
print("appliqué", len(R), "remplacements ;", h0[:16], "->", h1)
