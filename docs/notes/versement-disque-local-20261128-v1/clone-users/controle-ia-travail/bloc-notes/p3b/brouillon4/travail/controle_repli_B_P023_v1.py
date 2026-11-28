# Controle en memoire : chaines du repli (B) de P-023 presentes dans le texte principal (blancs reduits). Rien n'est ecrit.
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
debut = t.index("  - **Version de repli (B) de P-023**")
fin = t.index("- **Hors périmètre")
principal = re.sub(r"\s+", " ", t[:debut] + t[fin:])
def n(s): return principal.count(re.sub(r"\s+", " ", s))
etapes = [
 ("G6 recouvrement", "sinon T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit (recouvrement insuffisant) » ; ", ""),
 ("G6 spécification", "sinon T4 résiduel non établi (spécification) → « séparation qui dépend de la forme de la régression : non établie » ; ", ""),
 ("O5 recouvrement", " (ou « recouvrement insuffisant », motif écrit)", ""),
 ("O5 spécification", "T4 résiduel non établi (spécification) → « séparation qui dépend de la forme de la régression : non établie » ; sinon ", ""),
 ("H-P3b-1 parenthèse", " (T4 de P3 corrigé du coût de la tâche et des coûts déjà déclarés, R-295)", ""),
 ("H-P3b-2", "ni au nombre écrit, à la tâche ou aux coûts déjà déclarés (T4 résiduel)", "ni au nombre écrit (T4 de P3 ; tâche et coûts déjà déclarés non contrôlés)"),
 ("G5", "du nombre écrit, de la tâche et des coûts déjà déclarés (au sens de ces tests)", "et du nombre écrit (au sens de ces tests ; tâche et coûts déjà déclarés non contrôlés)"),
 ("O7", "ni au nombre écrit, ni à la tâche ou aux coûts déjà déclarés, au sens de ces tests", "ni au nombre écrit, au sens de ces tests (tâche et coûts déjà déclarés non contrôlés)"),
 ("P3b-P5 prédiction", "aire du résidu de l'oracle au-dessus de son plancher", "aire de l'oracle stratifiée par quintiles du coût déclaré (T4 de P3) au-dessus de son plancher"),
 ("motif des coûts", "non séparé du nombre écrit, de la tâche ou de l'historique des coûts", "non séparé du nombre écrit"),
 ("motif", "non séparé du nombre écrit, de la tâche ou de l'historique", "non séparé du nombre écrit"),
 ("P3b-P5 motif", "non séparé du nombre, de la tâche ou de l'historique", "non séparé du nombre écrit"),
]
for nom, old, new in etapes:
    k = n(old)
    print(f"{nom}: {k}")
    principal = principal.replace(re.sub(r"\s+", " ", old), new)
g6 = principal[principal.index("| G6 :"):]; g6 = g6[:g6.index("| G7")]
print("G6 après retraits (T4 résiduel encore non renommé) :", g6.replace("T4 résiduel", "T4 de P3"))
