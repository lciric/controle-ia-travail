import sys, re, subprocess
src, dst, calc, date_v2, hm = sys.argv[1:6]
t = open(src, encoding="utf-8").read()
def rep(old, new, n=1):
    global t
    c = t.count(old)
    assert c == n, (c, old[:100])
    t = t.replace(old, new)

# ===== M1 =====
rep("- **Pire cas** : 9,62 h × 4 × 1,38 + 4 = 57,09 USD ; **plafond de repli : 60 USD** (C).",
    "- **Pire cas** : 9,62 h × 4 × 1,38 = 53,09 USD, sans téléchargement (compté à la ligne A ; une relance reprend sur la même instance, réponse 4) ; **plafond de repli : 55 USD** (C).")
rep("plafonds de repli 55 + 60 = 115 USD", "plafonds de repli 55 + 55 = 110 USD")
rep("`PB = 2 × 1,38 × (6 400 × tB / 3 600 + L) + 4`",
    "`PB = 2 × 1,38 × (6 400 × tB / 3 600 + L)` (sans téléchargement : compté à `PA`)")
rep("`L` = 1 h : 28 + 31 = **59 USD**", "`L` = 1 h : 28 + 27 = **55 USD**")
rep("47 + 52 = 99 USD ; `d` = 42,8 s, 49 + 55 = **104 USD** ; `d` = 45 s, 51 + 57 = 108 USD",
    "47 + 48 = 95 USD ; `d` = 42,8 s, 49 + 51 = **100 USD** ; `d` = 45 s, 51 + 53 = 104 USD")
rep("**60 USD** ; ensemble **115 USD** (C)", "**55 USD** ; ensemble **110 USD** (C)")
rep("≈ 28 + 31 = **59 USD**", "≈ 28 + 27 = **55 USD**")
rep("≈ 47 à 51 + 52 à 57 USD, **99 à 108 USD** : 6 à 14 % sous le repli (C)",
    "≈ 47 à 51 + 48 à 53 USD, **95 à 104 USD** : 5 à 14 % sous le repli (C)")
rep("plafond du juge 60 USD au lieu de 80", "plafond du juge 55 USD au lieu de 80")
rep("restent à 6 à 14 % du repli", "restent à 5 à 14 % du repli")
rep("(115 USD de repli)", "(110 USD de repli)")
rep("(55 et 60 USD)", "(55 et 55 USD)")
rep("6 à 14 % sur le repli (99 à 108 USD contre 115, section 4)", "5 à 14 % sur le repli (95 à 104 USD contre 110, section 4)")
rep("115 USD de plafonds", "110 USD de plafonds")
rep("1 − 99 ÷ 115 = 0,139 et 1 − 108 ÷ 115 = 0,061", "1 − 95 ÷ 110 = 0,136 et 1 − 104 ÷ 110 = 0,055")

# ===== M2 =====
rep("et la ligne B (juge, ouvertures, lecture commune), que le lanceur exige avant la production des scores du juge.",
    "et la ligne B (juge, ouvertures, lecture commune) ; les deux identifiants de GO sont cités dans la commande de création de l'instance, qui ne se crée pas sans l'un d'eux ; rien n'est demandé au lanceur de l'étape de discrétion.")
rep("inconvénient : la ligne B se vérifie dans le lanceur, en cours d'exécution, non à la création de l'instance.",
    "inconvénient : la ligne B doit être accordée avant la création de l'instance, bien qu'elle ne serve qu'après les ≈ 8 h de la ligne A ; la dépense des deux lignes, sur une seule instance, se partage par la règle de la section 4.")
rep("confiance moyenne à haute (la vérification de la ligne B par le lanceur est du côté habilité)", "confiance moyenne à haute")
rep("la sienne | la sienne", "les deux, citées à la création de l'instance | (citée à la création)")

# ===== M3 =====
debut = t.index("**Arrêts** : plafond atteint, arrêt de la ligne")
fin = t.index("\n", debut)
rep(t[debut:fin] + "\n", t[debut:fin] + "\n\n**Partage sur une seule instance** : la coupure de l'instance est la somme des plafonds des deux lignes ; le compteur de la ligne A court de la création de l'instance à l'horodatage de la dernière lecture du moniteur boîte noire, écrit au manifeste de sa production ; celui de la ligne B, de cet horodatage à la destruction de l'instance ; chaque ligne s'arrête à son propre plafond sur son compteur, relevé au registre des dépenses. Un arrêt au plafond de la ligne A, au milieu de l'exécution unique, suit la règle de la panne (13.2, ligne 1499) : scores déjà produits versés et scellés sans être ouverts, aucun agent ne reçoit de fichier de scores avant la ligne d'ouverture ; reprise par nœud (8.2, ligne 1091).\n")

# ===== M4 =====
rep("(6.10, lignes 922 et 925 ; configuration de référence, lignes 103 et 105) | (1)",
    "(6.10, lignes 922 et 925 ; configuration de référence, lignes 103 et 105) ; **réserve** : une action de l'agent génère 223 jetons en moyenne (devis v2, ligne 44), une lecture avec raisonnement jusqu'à 400 ; si les lectures vont souvent au bout, le décodage peut être jusqu'à ≈ 1,8 fois plus long : la borne haute écrite (le double) couvre ce débit plus lent ou une relance, non les deux | (1)")
rep("| le temps de S1, plus une passe sur le contexte",
    "| le débit de génération du juge (7 milliards de paramètres, autre tokeniseur) pris égal à celui du moniteur boîte noire (supposé) ; le temps de S1, plus une passe sur le contexte")
rep("l'hypothèse vient de l'agent, sur une autre chaîne.",
    "l'hypothèse vient de l'agent, sur une autre chaîne. L'action de l'agent génère 223 jetons en moyenne, la lecture jusqu'à 400 : l'attendu peut être sous-estimé jusqu'à ≈ 1,8 fois, et le doublement du pire cas n'absorbe alors plus une relance (devis v4, 5.2).")
rep("**Le point fragile est ailleurs** : aucun débit des moniteurs n'est mesuré (réponse 1)",
    "**Le point fragile est ailleurs** : aucun débit des moniteurs n'est mesuré (réponse 1), et la lecture avec raisonnement peut générer jusqu'à ≈ 1,8 fois plus de jetons qu'une action de l'agent")

# ===== M5 =====
rep("utilisables seulement après la garde de production ; ",
    "utilisables seulement après la garde de production ; échéance de chaque ligne fixée au-delà de la date prévue de l'étape (m) ; ")
rep("accordés longtemps avant leur emploi.",
    "accordés longtemps avant leur emploi ; si l'échéance des lignes passe avant l'étape (m), la garde de calcul refuse la création et un tour de GO revient à la fin.")
ligne_go = [l for l in t.split("\n") if l.startswith("| ligne de GO de la lecture")]
assert len(ligne_go) == 1
rep(ligne_go[0] + "\n", ligne_go[0] + "\n| échéance de la ligne de GO non passée le jour de la création | garde de calcul du dépôt | oui | oui |\n")

# ===== mineurs =====
rep("avec raisonnement ; 400 jetons générés au plus ; température 1,0 ; balise absente imposée ; lots de 8",
    "avec raisonnement ; cinq réglages : 400 jetons générés au plus ; température 1,0 ; balise absente imposée ; seuil de masse faible 0,5 ; lots de 8")  # m1
rep("## 5. Ce que les réponses du lecteur habilité ont changé\n",
    "## 5. Ce que les réponses du lecteur habilité ont changé\n\nLa colonne « avant » décrit l'état de travail de ce devis avant les réponses du 22 novembre, non versé et sans empreinte ; ses nombres ne sont opposables à rien.\n")  # m2
rep("| lectures | 6 400 au plus (M) × 4,02 à 4,28 s (S1) |",
    "| table et préparation des demandes (13.2, ligne 1499, étapes 2 et 3) | une fois | négligeable (S) |\n| lectures | 6 400 au plus (M) × 4,02 à 4,28 s (S1) |")  # m3
rep("plafond de repli arrondi aux 5 USD supérieurs",
    "plafond de repli arrondi aux 5 USD supérieurs (les deux lignes sont des replis : un recalcul est prévu à l'étape (m), comme pour la ligne 2 de la v4, 5.2)")  # m4
rep("au prix d'un tour de GO au bout de la course.",
    "au prix d'un tour de GO au bout de la course. Aucune étape du texte ne mesure le débit des moniteurs avant l'étape (m) : sans dépense de plus, le gain de l'option (a) est celui-là.")  # m5
rep("comptée **0,45 s**", "comptée **0,45 s** (en lots, comme à l'autre chaîne : supposé)")  # m6
rep("la garde de calcul du dépôt lie une création d'instance à une ligne de GO.",
    "la garde de calcul du dépôt lie une création d'instance à une ligne de GO. Le rattachement de la mise en route (deux modèles) à la ligne A, et des ouvertures et de la lecture commune à la ligne B, est un choix de ce devis : la lettre de 13.2 nomme une ligne par lecture de moniteur, non le partage de ces postes.")  # m7

# ===== section 9 : programme corrigé (M1), rejoué =====
code = open(calc, encoding="utf-8").read()
sortie = subprocess.run([sys.executable, "-I", calc], capture_output=True, text=True, check=True).stdout
d = t.index("```python\n") + len("```python\n"); f = t.index("```\n", d)
t = t[:d] + code + t[f:]
d = t.index("Sortie :\n\n```\n") + len("Sortie :\n\n```\n"); f = t.index("```\n", d)
t = t[:d] + sortie + t[f:]
rep("joué tel quel le 2026-11-22 vers 22:40Z :", "joué tel quel le 2026-11-22 vers " + hm + " (version 2 ; à la version 1, vers 22:40Z) :")

# ===== en-tête de la version 2 =====
rep("— devis de la carte des deux moniteurs à modèle de langue — v1, sur le texte v2",
    "— devis de la carte des deux moniteurs à modèle de langue — v2, sur le texte v2")
rep("- **Date (UTC)** : écrit le 2026-11-22T22:40:07Z (`date -u`).",
    "- **Date (UTC)** : version 1 écrite le 2026-11-22T22:40:07Z ; version 2 écrite le " + date_v2 + " (`date -u`).")
rep("- **Commit du dépôt lu** : `643d4817` (branche `relance-bras-a/devis-carte-v3`).",
    "- **Commit du dépôt lu** : `643d4817` (branche `relance-bras-a/devis-carte-v3`) ; pour la version 2, `06416a69`, même branche.")
rep("- **Statut** : version 1, non contre-lue.",
    "- **Statut** : version 2 : la version 1, corrigée mot pour mot de sa contre-lecture (table « Corrections depuis la v1 »), sur la demande de la session du bras A (2026-11-22 vers 22:56Z) ; non recontre-lue.")
rep("- **Marques** :",
    "- **Version antérieure, gardée telle quelle (R12)** : version 1, même dossier, `devis-carte-moniteurs-bras-a-v1.md`, `6559f7886a599550090cde361fb7d5856631c27c3f008afb8e2bc3c46313fabc` (commit `76514065`) ; sa contre-lecture, `docs/notes/relance-organismes-discrets-v1/contre-lecture-devis-carte-moniteurs-bras-a-v1-v1.md`, `c0e299045a3a5878e22fc79e388accef8c3c3b993c2989ef76947b4d3c18d4b9` (branche `claude/pensive-bardeen-1fv7hw`, commit `9ef54de3` ; « engageable après corrections », aucun bloquant, cinq majeurs, sept mineurs).\n- **Marques** :")
rep("- **Sceau** : empreinte compagnon `devis-carte-moniteurs-bras-a-v1.md.sha256`",
    "- **Sceau** : empreinte compagnon `devis-carte-moniteurs-bras-a-v2.md.sha256`")

# ===== table des corrections, avant la section 0 =====
table = """## Corrections depuis la v1 : remarque → correction

Appliquées par programme : chaque texte remplacé a été trouvé une seule fois dans la v1 (« 28 + 31 = **59 USD** », présent deux fois, l'a été avec son contexte) ; les textes de remplacement et d'ajout sont ceux de la contre-lecture (`c0e29904…`), mot pour mot.

| remarque | où | correction |
|---|---|---|
| M1 | section 4 (ligne B, ensemble, formule `PB`, exemples) ; section 0, points 3 et 4 ; section 5 ; section 7 ; section 9 | téléchargement retiré du pire cas de la ligne B : plafond 55 USD au lieu de 60, ensemble 110 au lieu de 115 ; recalculés 55, 95, 100, 104 USD ; écarts au repli 5 à 14 % |
| M2 | décision 1 (décision, option (a), recommandation) ; section 6 | les deux identifiants de GO cités à la création de l'instance ; rien n'est demandé au lanceur |
| M3 | section 4, après « Arrêts » | règle du partage de la dépense et de la coupure sur une seule instance |
| M4 | S1 et S2 (fondement) ; réserve 1 ; section 0, point 5 | décodage jusqu'à ≈ 1,8 fois plus long ; débit du juge pris égal à celui du moniteur boîte noire, marqué supposé |
| M5 | décision 2 (décision, option (b)) ; section 6 | échéance des lignes de GO |
| m1 | section 2 | cinq réglages, seuil de masse faible compris |
| m2 | section 5 | statut de la colonne « avant » |
| m3 | section 4, ligne A | table et préparation des demandes, négligeables |
| m4 | section 3 | arrondi du repli justifié |
| m5 | décision 2, enjeu | aucune mesure des moniteurs avant l'étape (m) |
| m6 | S2 | passe de contexte en lots, supposé |
| m7 | décision 1, enjeu | rattachement des postes aux deux lignes : un choix de ce devis |

**Conséquences mécaniques, hors de la contre-lecture** : section 9, le programme corrigé (M1) est rejoué, sa sortie et l'heure du jeu remplacées ; en-tête : titre, date, commit lu, statut, version antérieure, sceau ; section 10, un point pour la version 2.

**Rien d'autre ne change.**

"""
rep("## 0. En une page\n", table + "## 0. En une page\n")

# ===== déclaration =====
rep("- **Aucune machine lancée, aucune clé, aucune dépense, aucun modèle extérieur consulté.**",
    "- **Pour la version 2, de plus** : la contre-lecture de la v1, lue en entier par `git show` sur la branche `claude/pensive-bardeen-1fv7hw` (récupérée en lecture, commit `9ef54de3`), empreinte recalculée `c0e29904…` ; le message de la session du bras A. Rien d'autre n'est ouvert.\n- **Aucune machine lancée, aucune clé, aucune dépense, aucun modèle extérieur consulté.**")

# ===== contrôles =====
assert "@@" not in t
blocs = re.findall(r"^```(\w*)\n(.*?)^```$", t, flags=re.S | re.M)
assert [l for l, _ in blocs] == ["python", ""]
assert subprocess.run([sys.executable, "-I", "-c", blocs[0][1]], capture_output=True, text=True, check=True).stdout == blocs[1][1]
for mot in ("57,09", "115 USD", "**59 USD**", "60 USD"):
    print("reste", repr(mot), ":", t.count(mot))
open(dst, "w", encoding="utf-8").write(t)
print("v2 écrite ;", date_v2)
