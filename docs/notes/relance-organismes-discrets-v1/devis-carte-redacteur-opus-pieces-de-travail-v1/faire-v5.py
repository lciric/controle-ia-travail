import sys
src, dst, date_v5 = sys.argv[1:4]
t = open(src, encoding="utf-8").read()
def rep(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:80])
    t = t.replace(old, new)
# le seul changement de fond : le crochet de m4
rep("[constat du quota | substitution accordée]", "substitution accordée")
# en-tête de version
rep("— devis de la course sur carte louée — v4, sur le texte v2", "— devis de la course sur carte louée — v5, sur le texte v2")
rep("; version 4 écrite le 2026-11-22T22:37:51Z (`date -u`).",
    "; version 4 écrite le 2026-11-22T22:37:51Z ; version 5 écrite le " + date_v5 + " (`date -u`).")
rep("- **Statut** : version 4 : la version 3, corrigée mot pour mot de sa contre-lecture (table « Corrections depuis la v3 »), non recontre-lue.",
    "- **Statut** : version 5 : la version 4, dont seul change le crochet de la correction m4, tranché par la session mère (« substitution accordée », transmis par la session du bras A le 2026-11-22 vers 22:52Z), comme le demande la vérification des corrections de la v4 (`docs/notes/relance-organismes-discrets-v1/verification-corrections-devis-bras-a-v4-v1.md`, `1d42bd6c059092ed3063b979cb5e2a96d0d4a311e7a7431c5e06602654b07c6b`, « corrections vérifiées, engageable ») ; la version 4 était la version 3, corrigée mot pour mot de sa contre-lecture (table « Corrections depuis la v3 »).")
rep("- **Version antérieure, gardée telle quelle (R12)** : version 3, même dossier,",
    "- **Versions antérieures, gardées telles quelles (R12)** : version 4, même dossier, `devis-bras-a-v4.md`, `f82514e9326df61f2fbd73f3eab644107f910aae620afe70b3d6ef9fcde7e0f3` (commit `643d4817`) ; version 3, même dossier,")
rep("- **Sceau** : empreinte compagnon `devis-bras-a-v4.md.sha256`", "- **Sceau** : empreinte compagnon `devis-bras-a-v5.md.sha256`")
assert "[constat du quota" not in t and "@@" not in t
open(dst, "w", encoding="utf-8").write(t)
print("v5 écrite ;", date_v5)
