"""Brouillon 2 du préenregistrement du crible (v) : application des corrections du tour 1 de contre-lecture.

Couples « ancien → nouveau » : les 31 couples des corrections C-01 à C-21 sont lus dans le rapport de contre-lecture
lui-même (lignes « ANCIEN: » et « NOUVEAU: » entre clôtures), sans retouche ; s'y ajoutent des couples propres, chacun
nommé et déclaré dans la section « Contre-lecture » de la cible : en-tête, statut, validateur, report des « W_R ≥ 4 »
et des « 16 mondes » demandé par C-02, mots de tête demandés par C-05 et C-06, décisions de R-2977 demandées par C-07,
cohérence avec C-10, entrée « Contre-lecture 1 ».
Gardes : empreinte de la pièce de départ et du rapport ; 31 couples exactement dans le rapport ; chaque « ancien »
figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque « nouveau » présent
dans la cible ; la cible (et son compagnon) ne doit pas exister (ouverture en mode « x ») ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon2.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon1.md")
SOURCE_SHA = "ec8d04962b570b97f16f49b289dfbb3e8b32fcb8468090fafb164434ed59678a"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-tour1-v1.md")
RAPPORT_SHA = "749d55ab13c6b28ee3465d1256d9015b66971c3591824788f07d16885dc2ca56"
CIBLE = os.path.join(ICI, "crible-v-brouillon2.md")
NOM_PROGRAMME = "appliquer-corrections-crible-v-brouillon2.py"
NOMBRE_COUPLES_RAPPORT = 31


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# 1. Empreintes des entrées ; cible absente.
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

with open(SOURCE, encoding="utf-8") as f:
    source = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()

# 2. Couples du rapport : chaque bloc « ANCIEN: » suivi de « NOUVEAU: », rattaché à la correction qui le précède.
couples = []
correction = None
lignes = rapport.splitlines()
for i, ligne in enumerate(lignes):
    m = re.match(r"^\*\*(C-\d\d)\b", ligne)
    if m:
        correction = m.group(1)
        rang = 0
    if ligne.startswith("ANCIEN: "):
        if i + 1 >= len(lignes) or not lignes[i + 1].startswith("NOUVEAU: "):
            arret(f"bloc ANCIEN sans NOUVEAU à la ligne {i + 1} du rapport")
        if correction is None:
            arret(f"bloc ANCIEN hors de toute correction à la ligne {i + 1} du rapport")
        rang += 1
        couples.append((f"{correction}.{rang}", ligne[len("ANCIEN: "):], lignes[i + 1][len("NOUVEAU: "):]))
if len(couples) != NOMBRE_COUPLES_RAPPORT:
    arret(f"{len(couples)} couples lus dans le rapport, {NOMBRE_COUPLES_RAPPORT} attendus")

# 3. Heure lue par `date -u` au moment de l'écriture (le scellement suit aussitôt).
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

# 4. Couples propres (déclarés dans la section « Contre-lecture » de la cible).
ENTREE_CL = f"""

- **Contre-lecture 1** (tour 1, sur le brouillon 1) : sous-agent neuf du modèle C, qui n'a écrit ni ce texte, ni [NOTE], ni
  [PILOTE], ni le code du pilote ; lecture de 13:24:10Z à 13:34:13Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-tour1-v1.md`, empreinte
  `{RAPPORT_SHA}` ; brouillon relu : `crible-v-brouillon1.md`, empreinte
  `{SOURCE_SHA}`. Verdict : **corrections** (10 majeures C-01 à C-10, 11 mineures C-11 à C-21,
  4 remarques facultatives R-1 à R-4) ; aucun « a_refaire ».
  - **Application** : par un rédacteur neuf (modèle C ; il n'a écrit ni le brouillon 1, ni le rapport, ni aucune pièce citée),
    au moyen du programme `{NOM_PROGRAMME}` (même dossier, empreinte dans son compagnon `.sha256`) :
    les 31 couples « ancien → nouveau » des corrections C-01 à C-21 sont lus dans le rapport lui-même et appliqués sans
    retouche ; chaque « ancien » vérifié présent une seule fois dans le brouillon 1 ; aucun chevauchement ; cible neuve ;
    écriture le {heure} (`date -u`). Aucun appel de modèle, aucune dépense, aucune donnée lue (rien sous `diag/`, `runs/`,
    `donnees/` ; relevé de v67 et sortie du pilote non ouverts).
  - **Réponse point par point** :
    - C-01 (durée) : appliquée (deux couples : borne par appel B_a, mondes à la fois M, budget de pire cas ≤ 17 h, appel
      au-delà de B_a compté « échec » ; garde de minuterie sur ce budget). Point 9 de « En dix lignes » mis d'accord (couple
      propre « dix-lignes-9 »).
    - C-02 (nombre de mondes, minimum, seuil de perte) : appliquée (trois couples : 20 ou 24 mondes par règle écrite,
      minimum 0,8 × mondes tirés, table W_min(n_c)). Report demandé par le rapport, fait par couples propres :
      « W_R ≥ 4 » et « W_B ≥ 4 » deviennent « W_min » dans « En dix lignes » (point 6), la table des prédictions (V3, V4),
      l'étage 3 et l'étage 5 ; « n_c < 16 » (étage 1), « 16 mondes complets » (liste d'arrêt) et « le minimum de 16 »
      (points à remesurer) renvoient au minimum de la section « Seuil » ; n_c « 20 au plus, ou 24 ». La phrase de la section
      « Taille » à p = 0,10 … 0,26 (« W_R ≥ 4 ») est laissée : elle porte sur 20 mondes, où W_min vaut 4. **Réserve** : avec
      24 mondes, le minimum de 20 (0,8 × 24) est plus exigeant que le minimum de 16 sur lequel le rapport calcule 0,98 et
      0,55 ; la probabilité d'atteindre le minimum est à recalculer par programme (règle de la section « Taille »), avant
      scellement.
    - C-03 (règle d'avance sur ce qui sera refait d'après le pilote) : appliquée. Le texte du rapport ne nomme pas le minimum
      de mondes complets ni la définition de « monde complet » parmi ce qui peut changer, alors que C-02 les fait recalculer
      avant scellement : couple propre « etape-2 » à la fin de l'étape 2, qui les rattache à la règle de la section « Taille »
      et gèle la table W_min(n_c) (seuils de perte gelés, comme le dit le rapport, « hors W_min(n_c) » : la table elle-même ne
      bouge pas).
    - C-04 (seuil d'épargne) : appliquée (trois couples).
    - C-05 (puissance) : appliquée (deux couples). La phrase demandée hors couple (« W_R de 1 à 3 : perte observée, non
      établie ») est ajoutée à la lecture de H-v (couple propre « lecture-H-v-d »).
    - C-06 (cas dégénéré) : appliquée (deux couples : « H-v non éprouvée au crible » si k_R < 4 ou k_R > n_c − 4 ; règle au
      rang et rejeu de la seule décision sous une archive fictive, en sensibilités). Le « dis-le en tête » du rapport (point 2)
      est fait au point 7 de « En dix lignes » (couple propre « dix-lignes-7 »).
    - C-07 (décisions de R-2977) : appliquée (deux couples : titre de la section « Choix et doutes », « données déjà vues »).
      Les décisions sont aussi reportées au point de chacune (couples propres « choix-2 », « choix-4 », « choix-5 »,
      « choix-6 », « choix-9 », « choix-11 ») ; la lecture de GO-2026-11-15-06 dans « Écarts » est dite confirmée pour l'essai
      par R-2977 (« GO-2026-11-15-06 vaut pour l'essai, non pour l'adoption » ; couple propre « ecarts-GO ») ; R-2977, R-2981
      et R-2982 ajoutés aux documents qui font foi ; point 10 de « En dix lignes » mis d'accord. Restent ouverts, comme le dit le
      titre : points 1, 3, 7, 8, 10, et l'entrée de l'ablation aux critères gelés de (v) (R-2977 ne le tranche que pour (iii)).
    - C-08 (partie A et lois retenues) : appliquée.
    - C-09 (audit de symétrie ciblé) : appliquée.
    - C-10 (devis) : appliquée (trois couples). Mis d'accord par couples propres : point 3 de « Choix et doutes » (≈ 65 %
      remplacé par les parts de C-10) ; étape 2 et ligne d'arrêt « relevé de sonde » (la sonde neuve est exigée ou non par
      décision écrite avant le scellement, non « si le lanceur l'exige »).
    - C-11 à C-17, C-19 à C-21 : appliquées, un couple chacune.
    - C-18 : appliquée (lecteur du tour 1 nommé). L'entrée demandée « sous Contre-lecture 1 » est celle-ci, avec les deux
      empreintes entières exigées par `controle_ia.prereg.problemes`.
    - Remarques facultatives R-1 à R-4 : **non appliquées** (non exigées ; consigne de ce tour bornée aux corrections) ;
      laissées à la version qui fera foi.
    - Chiffres que le rapport demande « à refaire par programme et recopier en annexe » (table W_min(n_c), puissance à 17
      mondes à risque, probabilité d'atteindre le minimum) : **non recopiés ici** ; les textes appliqués les renvoient à la
      version qui fera foi (C-02, C-05, C-20).
    - « Points pour la mère » 1 à 6 du rapport : transmis, non tranchés ici (date de lancement fixée par le code neuf ;
      risque « non concluant » selon la définition de « monde complet » ; le crible éprouve surtout l'ablation ; étage 5 de
      (v), lecture de GO-2026-11-15-06, sens de la distance ; enveloppe des cinq cribles ; mots de Lazar sur l'adoption).
  - **Rôles** : la règle de R-2982 veut les corrections écrites par le modèle A ; celles-ci l'ont été par un rédacteur du
    modèle C sur consigne de la session mère : à elle de dire qui relit le tour 2 (ni l'auteur du brouillon 1, ni ce
    rédacteur, ni le lecteur du tour 1). **Fichiers à donner en plus au tour 2** : le rapport du tour 1 et le programme
    `{NOM_PROGRAMME}`, avec le brouillon 1 pour la comparaison."""

PROPRES = [
    ("titre",
     "(regroupement, sans juge) — brouillon 1",
     "(regroupement, sans juge) — brouillon 2"),
    ("date",
     "  branches lues par `git show`, sans clone ; aucun commit, aucune poussée.",
     "  branches lues par `git show`, sans clone ; aucun commit, aucune poussée.\n"
     "- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées par un rédacteur neuf (modèle C ; il n'a écrit ni le\n"
     f"  brouillon 1, ni le rapport, ni aucune pièce citée), écrit et scellé le {heure} (`date -u`) ; aucun commit, aucune poussée\n"
     "  (section « Contre-lecture »)."),
    ("registre",
     "R-2883, R-2968 à R-2970 (registre vivant) ;",
     "R-2883, R-2968 à R-2970, R-2977 (décisions de la mère sur les choix de ce texte), R-2981, R-2982 (registre vivant) ;"),
    ("statut",
     "**Statut.** Brouillon 1, **non scellé, non contre-lu** (R1, R2).",
     "**Statut.** Brouillon 2, **contre-lu une fois** (tour 1, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2) ; tour 2 de contre-lecture à faire."),
    ("validateur",
     "lu**. Validateur `controle_ia.prereg.problemes` : un seul défaut attendu à ce stade, la section « Contre-lecture » sans les\n"
     "deux empreintes (aucune contre-lecture n'existe) ; rien d'autre.",
     "lu**. Brouillon 2 : le pilote MR-2 est fini et sa machine détruite (R-2981) ; son issue et son taux de réussite par appel ne\n"
     "sont pas lus ici, aucune donnée du pilote n'entre dans ce brouillon ; ce qui en sera refait suit les règles écrites d'avance\n"
     "(« Étapes », point 2 ; « Taille »). Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 2 (vérifié avant\n"
     "son scellement comme pièce de travail)."),
    ("dix-lignes-6",
     "« perte établie » dès W_R ≥ 4\n   sur 20 ;",
     "« perte établie » dès W_R ≥ W_min(n_c)\n   (4 de 16 à 22 mondes complets, 5 à 23 ou 24) ;"),
    ("dix-lignes-7",
     "la comparaison au placebo sera probablement « non éprouvable ».",
     "la comparaison au placebo sera probablement « non éprouvable » : le crible\n"
     "   éprouverait alors l'ablation (QO1), non la règle (« H-v non éprouvée au crible », section « Critères de lecture gelés »)."),
    ("dix-lignes-9",
     "borne par monde ou mondes en parallèle à décider sur la durée mesurée du pilote.",
     "borne par appel B_a et nombre M de mondes à la fois fixés avant le scellement\n"
     "   d'après la durée mesurée du pilote, budget de pire cas ≤ 17 h (section « Devis », « Durée ») ; le code est neuf, la date de\n"
     "   lancement en dépend."),
    ("dix-lignes-10",
     "choix soumis à la mère (section « Choix et doutes »).",
     "choix tranchés en partie par la mère (R-2977), les autres à trancher\n"
     "    avant scellement (section « Choix et doutes »)."),
    ("n_c",
     "n_c = nombre de mondes complets (20 au plus).",
     "n_c = nombre de mondes complets (20 au plus, ou 24 par la règle de la section « Taille »)."),
    ("V3",
     "W_R ≥ 4 (« perte établie »)",
     "W_R ≥ W_min (« perte établie »)"),
    ("V4",
     "| W_B ≥ 4 | W_B = 0 |",
     "| W_B ≥ W_min | W_B = 0 |"),
    ("etape-2",
     "   mère ; sonde neuve si le lanceur la demande.",
     "   mère ; sonde neuve exigée ou non, décidé avant le scellement (section « Devis »). Le minimum de mondes complets et la\n"
     "   définition de « monde complet » suivent la règle de la section « Taille » (recalcul par programme sur le taux d'appels\n"
     "   répondus du pilote) ; la table W_min(n_c) de la section « Seuil » est gelée dès ce texte."),
    ("etage-1",
     "| 1 | n_c < 16, ou un fournisseur perdu en entier |",
     "| 1 | n_c sous le minimum (section « Seuil »), ou un fournisseur perdu en entier |"),
    ("etage-3",
     "(b) perte établie (W_R ≥ 4) ;",
     "(b) perte établie (W_R ≥ W_min(n_c)) ;"),
    ("etage-5",
     "/ « ajoute, établi » (W_B ≥ 4) /",
     "/ « ajoute, établi » (W_B ≥ W_min(n_c)) /"),
    ("lecture-H-v-d",
     "tranchée ». **Toujours dit avec l'étage 4**",
     "tranchée » (W_R de 1 à 3 : perte observée, non établie, alors que H-v dit « sans perte de couverture »). **Toujours dit\n"
     "avec l'étage 4**"),
    ("arret-sonde",
     "| relevé de sonde absent, invalide ou d'un autre code (si le lanceur l'exige) |",
     "| relevé de sonde absent, invalide ou d'un autre code (si la sonde neuve est exigée, décision écrite avant le scellement) |"),
    ("arret-minimum",
     "| fournisseur abandonné alors que 16 mondes complets ne sont plus possibles |",
     "| fournisseur abandonné alors que le minimum de mondes complets (section « Seuil ») n'est plus possible |"),
    ("remesurer-3",
     "16 mondes complets en dépend :",
     "mondes complets, sa définition et le nombre de mondes en dépendent, règle de la section « Taille » :"),
    ("ecarts-GO",
     "— **lecture à confirmer par la mère**. Toute adoption",
     "— **lecture confirmée par la mère pour l'essai** (R-2977 : « GO-2026-11-15-06 vaut pour\n"
     "  l'essai, non pour l'adoption »). Toute adoption"),
    ("choix-2",
     "configuration. Recommandation : oui (c'est ce que l'épargne veut dire) ; confiance 0,6.",
     "configuration. Recommandation : oui (c'est ce que l'épargne veut dire) ; confiance 0,6. **Tranché (R-2977)** : oui."),
    ("choix-3",
     "met ≈ 65 % de l'attendu sur crédits, le maximum permis par la",
     "met ≈ 50 à 53 % de la fourchette aux prix publics sur crédits (≈ 37 à 39 % au compte\n"
     "   de la configuration, ≈ 51 % du pire cas ; section « Devis »), le maximum permis par la"),
    ("choix-4",
     "éprouver la règle dans une course à plusieurs générations plus tard ; confiance 0,55.",
     "éprouver la règle dans une course à plusieurs générations plus tard ; confiance 0,55. **Tranché (R-2977)** : (a), archive\n"
     "   réduite à K1 ; deux lectures sans appel de plus, rapportées sans verdict (règle au rang ; rejeu de la seule décision sous une\n"
     "   archive fictive : « Métrique », « Sensibilités »)."),
    ("choix-5",
     "pilote montre moins de 0,95 par appel.",
     "pilote montre moins de 0,95 par appel. **Tranché (R-2977)** : 24 mondes si le taux d'appels répondus par appel\n"
     "   du pilote est sous 0,95, 20 sinon (section « Taille »)."),
    ("choix-6",
     "Recommandation : mondes séparés ; confiance 0,6.",
     "Recommandation : mondes séparés ; confiance 0,6. **Tranché (R-2977)** : mondes séparés."),
    ("choix-9",
     "sans aucun verdict du juge : permis ?",
     "sans aucun verdict du juge : permis ? **Tranché (R-2977)** : permis, partie A déclarée descriptive, sur des\n"
     "   données déjà vues, sans aucun verdict du juge (les lois retenues de la génération 2 : « Partie A », « Interdits »)."),
    ("choix-11",
     "même si le crible donne « sans perte ».",
     "même si le crible donne « sans perte ». **Tranché (R-2977)** : à dire à Lazar avec le nœud\n"
     "    d'adoption."),
    ("contre-lecture-tete",
     "Aucune à ce jour : ce texte est le brouillon 1, soumis à la contre-lecture (R2) d'un sous-agent neuf d'un **autre modèle** que",
     "Tour 1 fait (entrée « Contre-lecture 1 » ci-dessous) : le brouillon 1 a été soumis à la contre-lecture (R2) d'un sous-agent\n"
     "neuf d'un **autre modèle** que"),
    ("contre-lecture-1",
     "devis contre le bloc gelé ; la faisabilité de la durée ; la tension avec [V3] § 4.3 ; les onze choix ci-dessus.",
     "devis contre le bloc gelé ; la faisabilité de la durée ; la tension avec [V3] § 4.3 ; les onze choix ci-dessus." + ENTREE_CL),
]

tous = couples + PROPRES

# 5. Chaque « ancien » une seule fois dans la pièce de départ ; aucun chevauchement.
places = []
for nom, ancien, nouveau in tous:
    n = source.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » trouvé {n} fois (une seule attendue)")
    debut = source.index(ancien)
    places.append((debut, debut + len(ancien), nom, nouveau))
places.sort()
for (d1, f1, n1, _), (d2, f2, n2, _) in zip(places, places[1:]):
    if d2 < f1:
        arret(f"chevauchement entre {n1} et {n2}")

# 6. Application par positions dans la pièce de départ.
morceaux, curseur = [], 0
for debut, fin, nom, nouveau in places:
    morceaux.append(source[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(source[curseur:])
cible = "".join(morceaux)

for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"cible écrite : {CIBLE}")
print(f"heure (date -u) : {heure}")
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres) : "
      + ", ".join(n for _, _, n, _ in places))
print(f"empreinte de la cible : {sha(CIBLE)}")
