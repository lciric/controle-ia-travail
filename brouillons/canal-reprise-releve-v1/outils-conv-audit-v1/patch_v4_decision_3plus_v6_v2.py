"""Applique au texte v4 du pilote 4 les décisions de Lazar du 26 octobre (01:48 Paris : (3+), deux paliers, δ = 0,10 ;
01:52 Paris : banque v6 pour (b)) : moment de lecture tranché — les scores de ce pilote restent fermés pour tout usage,
aucune course versée dans (b) —, relevé v3 des mots de Lazar, pièces lues. Remplacements exacts, chacun au nombre
attendu ; refuse sinon. Remplace le correctif v1 (règle d'inclusion), devenu sans objet à 01:52 et jamais appliqué.
Usage : python -I patch_v4_decision_3plus_v6_v2.py TEXTE"""
import pathlib, sys

p = pathlib.Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(ancien, nouveau, n=1):
    global t
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)


rep("sur les décisions de Lazar de 23:54 à 00:59 Paris (§ Décisions)",
    "sur les décisions de Lazar de 23:54 à 01:52 Paris (§ Décisions)")
rep("`objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v2.md` (§ Pièces).",
    "`objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v3.md` (§ Pièces).")
rep("""départs du collisionneur et du test H-M1 ; aucun score) ; les rapports finaux des sous-agents des étapes 1 et 2 (aucun
score).""", """départs du collisionneur et du test H-M1 ; aucun score) ; les rapports finaux des sous-agents des étapes 1 et 2 et le
brouillon du préenregistrement de l'étape 2 (aucun score) ; les neuf réponses du collisionneur « lecture du pilote »
(branche `donnees/collisionneur-lecture-pilote-v1`, `7ac475b` ; aucun score).""")
rep("""  session-depot) ; ce texte ne contient rien de (b).""",
    """  session-depot ; à 01:48 et 01:52, deux paliers, δ = 0,10, banque v6) ; ce texte ne contient rien de (b).""")

debut = t.index("Le moment où les scores de ce pilote peuvent être lus pour écrire les\n  hypothèses de (b) : **décision soumise à Lazar**")
fin_marque = "  usage, les scores de ce pilote restent fermés selon P4v3.\n"
fin = t.index(fin_marque) + len(fin_marque)
rep(t[debut:fin], """Le moment où les scores de ce pilote pourraient être lus pour écrire les
  hypothèses de (b) a été soumis à Lazar le 25 octobre à 23:56 UTC (options : (1) garder la règle de P4v3 ; (2) et (2')
  un agent neuf lit les scores dès la fin de ce pilote ; (3) écrire (b) sans eux), puis au collisionneur (00:59, « demande
  au collisionneur » ; trois tours sur son mot dans la session de session-depot, R-451, R-452 ; synthèse
  `synthese-collisionneur-lecture-pilote-conv-audit-v1.md`, `a8e1ed64…`, sur le canal) : une course par objet n'apprend
  presque rien à (b) sur le signe de l'effet, et la direction de (b) est donnée par la question de 00:49.
- **01:48** : « Je recommande (3+), confiance moyenne. : go » ((3) en y versant les deux courses de ce pilote comme
  graines) ; plan de (b) en deux paliers et δ = 0,10 : « go » ; leviers (une seule mesure principale, courses
  entrelacées, plus de tâches) : « go a tout ». Puis, **01:52**, sur la banque de (b) : « Banque v6 (lot 3) : deux fois
  plus de tâches, mais il faut attendre qu’elle soit construite, et le pilote 4 ne peut plus compter. : go ». **Les
  hypothèses de (b) sont écrites sans aucun score de ce pilote, et (b) court sur la banque v6 : aucune course de ce pilote
  n'y est versée. Les scores de ce pilote restent fermés selon P4v3, pour tout usage ; les options (2) et (2') n'existent
  plus.**
""")
rep("le relevé verbatim des mots de Lazar, v1 et v2)", "le relevé verbatim des mots de Lazar, v1 à v3)")

p.write_text(t, encoding="utf-8")
print("appliqué")
