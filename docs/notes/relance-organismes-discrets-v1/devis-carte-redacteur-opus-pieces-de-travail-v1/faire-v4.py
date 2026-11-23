import sys, subprocess
v3, v4, calc_v4 = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(v3, encoding="utf-8").read()
sortie_v4 = subprocess.run([sys.executable, "-I", calc_v4], capture_output=True, text=True, check=True).stdout
code_v4 = open(calc_v4, encoding="utf-8").read()

def rep(old, new):
    global t
    n = t.count(old)
    assert n == 1, (n, old[:90])
    t = t.replace(old, new)

# --- Contre-lecture, mot pour mot ---
# M1 (quatre endroits)
rep("comme le disent 6.11 (ligne 960) et 13.2",
    "selon la lecture de la section 8, qui s'appuie sur 6.3 (a), ligne 753 (seuls le devis et la ligne de GO de la première ligne de carte avant toute dépense) et sur 8.1, ligne 1087 (« la case de 13.2 qui la conditionne »), contre la lettre de 13.2 (titre, ligne 1485 ; case « devis », ligne 1490), qui range ce devis parmi les conditions d'avant toute dépense")
rep("**Défaut sous 48 heures** : (b).",
    "**Défaut sous 48 heures** : (b), si Lazar confirme la lecture de la section 8 ; s'il retient la lettre de 13.2, (b) est un écart au texte scellé : nœud, sans défaut, et la ligne 1 attend aussi le devis des lectures et celui des moniteurs.")
rep("13.2 « devis », ligne 1490 ; 6.11, ligne 937 (« devis, contre-lecture et GO avant chaque ligne »)",
    "13.2 « devis », ligne 1490 ; 6.11, ligne 937 (« devis, contre-lecture et GO avant chaque ligne ») ; 6.3 (a), ligne 753 (« devis et ligne de GO de la première ligne de carte ») ; 8.1, ligne 1087")
rep("le moment du devis de la carte des deux moniteurs ; ",
    "le moment du devis de la carte des deux moniteurs ; avec la lecture de la case « devis » de 13.2, dont dépend le départ de la ligne 1 ; ")
# M2
rep("inconvénient : la session qui conduit la course écrit son plafond, que seule la contre-lecture vérifie.",
    "inconvénients : la session qui conduit la course écrit son plafond, que seule la contre-lecture vérifie ; le complément est le devis de la seconde ligne (6.11, ligne 959), pièce décisive que la règle « Économie de Fable » donne à Fable en effort maximal : l'option (a) en est un écart, à déclarer dans le complément, sauf si Fable est disponible à ce moment (quota rétabli le 29 novembre 2026).")
# m1
rep("Le doublement de la relance couvre cet écart ; aucune mesure ne le chiffre avant la ligne 2.",
    "Le doublement gardé pour une relance absorbe cet écart s'il n'y a pas de relance, non les deux ensemble ; aucune mesure ne le chiffre avant la ligne 2, et le complément le redit.")
# m2 (texte ; le programme de la section 13 est remplacé plus bas, avec sa sortie)
rep("(≈ 5,2 à 5,8 h de carte, ≈ 6,2 à 7,5 USD, C)",
    "(≈ 5,1 à 5,7 h de carte, ≈ 6,0 à 7,4 USD, C ; la prise ne se calcule pas pour un témoin bénin, métrique 7, ligne 627)")
# m3
rep("(c) partir sous GO-2026-11-18-62 — avantage : aucune ligne neuve ; inconvénient : son objet (256 épisodes, texte v1) n'est pas cette ligne, et le texte la dit inemployée.",
    "(c) partir sous GO-2026-11-18-62 — exclue : le texte scellé la dit inemployée (13.2, ligne 1490), et son objet (256 épisodes, texte v1) n'est pas cette ligne ; la retenir serait un écart au texte, donc un nœud.")
# m4
rep("(GO-2026-11-22-145, cité d'après le message de la session mère ; ",
    "(GO-2026-11-22-145, cité d'après le message de la session mère, qui en donne l'objet : [constat du quota | substitution accordée], à préciser par la session mère ; ")
# m5
rep("(80 sur 640 au plus, C)",
    "(80 sur 640 au plus, C) (640 = 8 tâches d'épreuve ouvertes × 8 épisodes × 10 actions : 6.1, ligne 684 ; 6.11, table des lectures, « 640 »)")

# --- Section 13 : programme et sortie (conséquence de m2), rejoués ---
debut_code = t.index("```python\n") + len("```python\n")
fin_code = t.index("```\n", debut_code)
t = t[:debut_code] + code_v4 + t[fin_code:]
debut_sortie = t.index("Sortie :\n\n```\n") + len("Sortie :\n\n```\n")
fin_sortie = t.index("```\n", debut_sortie)
assert t[debut_sortie:fin_sortie].count("Trois adaptateurs de plus") == 1
t = t[:debut_sortie] + sortie_v4 + t[fin_sortie:]
rep("joué tel quel le 2026-11-22 vers 22:12Z :", "joué tel quel le 2026-11-22 vers @@HEURE_PROGRAMME@@ (version 4 ; à la version 3, vers 22:12Z) :")

# --- Note de la session du bras A : devis des lectures accordé ---
rep("670 USD de plafonds (brouillon 3, non accepté)",
    "670 USD de plafonds (brouillon 3 ; accordé par Lazar le 22 novembre, GO-2026-11-22-143 et -146, d'après la session du bras A)")
rep("devis des lectures, brouillon 3, non accepté (sections 0 et 5.2)",
    "devis des lectures, brouillon 3 (sections 0 et 5.2) ; accordé par Lazar (GO-2026-11-22-143 et -146, d'après la session du bras A)")
rep("Hors de la course : l'essai de mesure",
    "**Devis des lectures** : « accordé par Lazar ce soir (GO-2026-11-22-143 et -146 : D1 (a), D2 (a) avec 900 s chez Google, D3 quatre appels à la fois et juge un à la fois avec garde-fous, D4 (a), D5 (a), D6 oui) », cité tel quel d'après le message de la session du bras A (2026-11-22, vers 22:24Z), sans vérification au registre (cloisonnement). Les chiffres de ce tableau sont ceux du brouillon 3, seule version que j'ai lue ; si la version accordée en diffère, le total suit la version accordée.\n\nHors de la course : l'essai de mesure")
rep("GO-2026-11-22-140 et -145 (d'après le mandat et le message de la session mère).",
    "GO-2026-11-22-140 et -145 (d'après le mandat et le message de la session mère) ; GO-2026-11-22-143 et -146 (d'après le message de la session du bras A).")

# --- En-tête de la version 4 ---
rep("— devis de la course sur carte louée — v3, sur le texte v2",
    "— devis de la course sur carte louée — v4, sur le texte v2")
rep("- **Date (UTC)** : commencé le 2026-11-22T21:57:13Z, écrit le 2026-11-22T22:14:09Z (`date -u`).",
    "- **Date (UTC)** : version 3 commencée le 2026-11-22T21:57:13Z et écrite le 2026-11-22T22:14:09Z ; version 4 écrite le @@DATE_V4@@ (`date -u`).")
rep("— aller vite, mais tout départ dans le cadre d'un devis scellé.",
    "— aller vite, mais tout départ dans le cadre d'un devis scellé. **Version 4** : sur la demande de la session du bras A (`session_013QMayn5HfnqnuvfPbwUUQf`, message du 2026-11-22 vers 22:24Z, « sur l'accord de la session mère »), @@CONFIRMATION_MERE@@.")
rep("- **Statut** : version 3, non contre-lue.",
    "- **Statut** : version 4 : la version 3, corrigée mot pour mot de sa contre-lecture (table « Corrections depuis la v3 »), non recontre-lue.")
rep("gardé tel quel (R12).\n",
    "gardé tel quel (R12).\n- **Version antérieure, gardée telle quelle (R12)** : version 3, même dossier, `devis-bras-a-v3.md`, `be7ce98899ffdeda046aa7b65dfbf9e70a9a9fc15629130d4c3ffcbed06158e9` (branche `relance-bras-a/devis-carte-v3`, commit `0206e87d`) ; sa contre-lecture, `docs/notes/relance-organismes-discrets-v1/contre-lecture-devis-bras-a-v3-v1.md`, `d458ed7f3fcef9c88a7081e4a143f29977b3aa3f0ee2c586c481f92e1d223611` (branche `claude/pensive-bardeen-1fv7hw`, commit `507c9133` ; « engageable après corrections », aucun bloquant, deux majeurs, cinq mineurs).\n")
rep("- **Sceau** : empreinte compagnon `devis-bras-a-v3.md.sha256`",
    "- **Sceau** : empreinte compagnon `devis-bras-a-v4.md.sha256`")

# --- Table des corrections, avant la section 0 ---
table = """## Corrections depuis la v3 : remarque → correction

Appliquées par programme : chaque texte remplacé a été trouvé une seule fois dans la v3 ; les textes de remplacement sont ceux de la contre-lecture (`d458ed7f…`), mot pour mot.

| remarque | où | correction |
|---|---|---|
| M1 | décision 3, option (b) | « comme le disent 6.11 (ligne 960) et 13.2 » remplacé : la lecture de la section 8, sur 6.3 (a) et 8.1, contre la lettre de 13.2 |
| M1 | décision 3, défaut | (b) seulement si Lazar confirme la lecture de la section 8 ; sous la lettre de 13.2, nœud sans défaut |
| M1 | section 8, ligne « devis », colonne « source » | 6.3 (a), ligne 753, et 8.1, ligne 1087, ajoutés |
| M1 | section 0, point 7 | la lecture de la case « devis » de 13.2 ajoutée aux décisions |
| M2 | décision 2, option (a) | inconvénient ajouté : le complément est une pièce décisive (règle « Économie de Fable ») |
| m1 | 5.2, dernier point | le doublement gardé pour une relance n'absorbe pas à la fois une relance et un débit plus lent |
| m2 | décision 4, option (b) ; section 13 | coût refait sans prise pour un témoin bénin ; `+ h(256 * prise)` retiré des lignes `un_b` et `un_h` |
| m3 | décision 1, option (c) | option exclue : écart au texte scellé |
| m4 | en-tête | objet de GO-2026-11-22-145 laissé entre crochets, à préciser par la session mère, tel que la contre-lecture l'écrit |
| m5 | section 7 | source du dénominateur 640 |

**Conséquences mécaniques, hors de la contre-lecture** : section 13, le commentaire de la décision 4 (« 256 passes » retiré), l'heure du jeu du programme et la dernière ligne de sa sortie, programme rejoué ; en-tête : titre, date, statut, version antérieure, sceau, origine de la version 4 ; section 14, un point pour la version 4.

**Note de la session du bras A** (message du 2026-11-22 vers 22:24Z), citée telle quelle, sans vérification au registre : « le devis des lectures est accordé par Lazar ce soir (GO-2026-11-22-143 et -146 : D1 (a), D2 (a) avec 900 s chez Google, D3 quatre appels à la fois et juge un à la fois avec garde-fous, D4 (a), D5 (a), D6 oui) ». Portée : section 0, point 5 ; section 11, tableau et une phrase ; réserve 9. La section 8 liste les conditions sans les remplir : elle n'est pas touchée.

**Rien d'autre ne change** : chiffres, volumes, règles, conditions et décisions, hors des textes ci-dessus.

"""
rep("## 0. En une page\n", table + "## 0. En une page\n")

# --- Déclaration : un point pour la version 4 ---
rep("- **Ce que je n'ai pas pu faire** :",
    "- **Pour la version 4, de plus** : la contre-lecture de la v3, lue en entier par `git show` sur la branche `claude/pensive-bardeen-1fv7hw` (récupérée en lecture, commit `507c9133`), empreinte recalculée `d458ed7f…` ; le message de la session du bras A ; la réponse de la session mère. Rien d'autre n'est ouvert ; le cloisonnement reste celui du mandat.\n- **Ce que je n'ai pas pu faire** :")

open(v4, "w", encoding="utf-8").write(t)
print("v4 écrite ;", t.count("@@"), "marques à remplir :", sorted(set(x.split("@@")[0] for x in t.split("@@")[1::2])))
