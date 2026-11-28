P = [
("""# relue au cas sain.
# Usage : essais_lanceur_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE""",
"""# relue au cas sain.
# Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) : GO de type « décision », « règle » (R-281,
# hors de l'en-tête) qui nomme l'un des cinq identifiants : code 2, aucune création (XL07, XL08 ; G04b2) ; témoins
# XL09 (type « décision » sans identifiant) et G04b (mention libre dans un GO de calcul) (VC2-fidelite-06) ; ligne de
# lancement.txt de l'heure limite de destruction (repli : création + 9 600 s + 24 h) et du rappel de la session, et
# récupération appelée avec l'arret.txt de l'arrêt, relues au cas sain (VC2-fidelite-03).
# Usage : essais_lanceur_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"""),
("""     "destruction après la récupération écrite": "détruite par son identifiant après la récupération vérifiée" in t,""",
"""     "destruction après la récupération écrite": "détruite par son identifiant après la récupération vérifiée" in t,
     "récupération appelée avec arret.txt (chaîne v4)": "<dossier neuf> <arret.txt de l arrêt>), 24 heures au plus après l arrêt relu dans arret.txt" in t,
     "heure limite de repli et rappel écrits une fois (chaîne v4)": bool(c) and len(re.findall(
         r"^heure limite de destruction : 24 heures après l arrêt relu dans arret\\.txt ; sans arret\\.txt, repli déclaré par la "
         r"récupération : (\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z) \\(création \\+ 9 600 s \\+ 24 h\\) ; rappel programmé par la session "
         r"au lancement, puis remis à 24 heures après l arrêt relu \\(geste de session\\) ; dépassée : nœud de Lazar$", t, re.M)) == 1
         and __import__("datetime").datetime.strptime(re.search(r"repli déclaré par la récupération : (\\S+Z) ", t).group(1),
                                                       "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=__import__("datetime").timezone.utc).timestamp()
         == int(c.group(1)) + 9600 + 86400,"""),
("""echo "| GO-2026-10-20-97 | $JOUR | décision | essai : aucune révocation de $GO | — | $JOUR | Lazar | essai |" >> registres/go.md
cas G04b-ligne-qui-mentionne-une-revocation 0 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md""",
"""# chaîne v4 (VC2-fidelite-06) : mention libre sans effet dans un GO d'un type de l'en-tête (G04b) ; dans un GO de type
# « décision » (hors de l'en-tête), elle arrête en code 2 (G04b2)
echo "| GO-2026-10-20-97 | $JOUR | calcul | essai : aucune révocation de $GO | 1 USD | $JOUR | Lazar | essai |" >> registres/go.md
cas G04b-ligne-qui-mentionne-une-revocation 0 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-20-97 | $JOUR | décision | essai : aucune révocation de $GO | — | $JOUR | Lazar | essai |" >> registres/go.md
MOTIF_CAS="révocation possible sous une forme voisine" cas G04b2-ligne-de-type-decision-qui-mentionne-le-go 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md"""),
("""MOTIF_CAS="révocation possible sous une forme voisine" cas XL06-temoin-tiret-insecable-sans-gras 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md""",
"""MOTIF_CAS="révocation possible sous une forme voisine" cas XL06-temoin-tiret-insecable-sans-gras 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
# chaîne v4 (VC2-fidelite-06) : types écrits par R-281 hors de l'en-tête du registre des GO
echo "| GO-2026-10-21-01 | $JOUR | décision | Lazar révoque R-269 (essai) | — | $JOUR | Lazar | essai |" >> registres/go.md
MOTIF_CAS="révocation possible sous une forme voisine" cas XL07-go-de-type-decision-qui-dit-lazar-revoque 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-21-01 | $JOUR | règle | GO-2026-10-20-07 suspendu (essai) | — | $JOUR | Lazar | essai |" >> registres/go.md
MOTIF_CAS="révocation possible sous une forme voisine" cas XL08-go-de-type-regle-qui-nomme-le-go-cite 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-21-01 | $JOUR | décision | nœud tranché par Lazar, sans lien avec P4 (essai) | — | $JOUR | Lazar | essai |" >> registres/go.md
cas XL09-temoin-go-de-type-decision-sans-identifiant 0 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md"""),
]
