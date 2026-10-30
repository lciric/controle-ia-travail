"""Brouillon 7 = brouillon 6 + R2 (3) de la vérification (verification-retouches-brouillon6-v1.md).
Usage : python3 -I appliquer-verification-brouillon7-v1.py BROUILLON6 BROUILLON7 HH:MM"""
import sys
src, dst, heure = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="utf-8").read()
def rep(old, new, n=1):
    global t
    c = t.count(old); assert c == n, (c, old[:80]); t = t.replace(old, new)
rep("BROUILLON 6 (version soumise au gel de Lazar ; corrections de la contre-lecture 4 et de leur vérification)",
    "BROUILLON 7 (version soumise au gel de Lazar ; corrections de la contre-lecture 4 et de leur vérification)")
rep(" UTC ; aucun chiffre ni seuil changé.",
    " UTC ; aucun chiffre ni seuil changé. **Brouillon 7** : point R2 (3) resté ouvert (`verification-retouches-brouillon6-v1.md`), "
    "une note de lecture ajoutée à l'audit, par conv-audit (Opus 5.5) à " + heure + " UTC ; aucun chiffre ni seuil changé.")
rep("(iii) y porte sur Δ(d1c, c) dans les miroirs de validation de `M_inertes`. Ses issues sont les mêmes.",
    "(iii) y porte sur Δ(d1c, c) dans les miroirs de validation de `M_inertes`. Ses issues sont les mêmes. **Note de lecture "
    "(vérification, R2 (3))** : si gain_contrôle est vrai sur les mondes de décision alors que (ii) est négatif sur les graines de "
    "validation (« aucun artefact »), ce n'est pas une divergence : les tables s'appliquent telles quelles et gain_contrôle décide "
    "(Table 1 ligne 5, Table 2 ligne 3 : N non adoptée, direction prudente). La non-régression (C11), sans code de contraste au § 7, "
    "n'entre pas dans la liste de (iii).")
rep("(brouillon 6) aux valeurs", "(brouillon 7) aux valeurs")
rep("lues dans le brouillon 6", "lues dans le brouillon 7")
rep("Ni le brouillon 5 ni le brouillon 6 ne sont la version relue.", "Ni le brouillon 5, ni le 6, ni le 7 ne sont la version relue.")
rep("suppression de la confiance de P4 nommée dans l'en-tête.\n\n",
    "suppression de la confiance de P4 nommée dans l'en-tête.\n"
    "9. **Vérification des retouches (brouillon 7)** — Sonnet 5.5 neuf, `verification-retouches-brouillon6-v1.md` : R1 et R3 conformes, "
    "script rejoué au bit près ; R2 (3) (gain_contrôle sur décision et (ii) négatif sur validation) : note de lecture ajoutée ; "
    "non-régression hors de (iii), dit.\n\n")
open(dst, "w", encoding="utf-8").write(t)
print("REMPLIR restants:", t.count("À REMPLIR"))
