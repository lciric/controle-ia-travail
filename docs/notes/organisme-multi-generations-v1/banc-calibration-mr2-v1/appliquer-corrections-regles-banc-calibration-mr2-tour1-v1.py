#!/usr/bin/env python3
"""Applique à la pièce des règles du banc de calibration complet MR-2 (v1) les corrections 1 à 4 de sa contre-lecture du tour 1.

Couples « ancien -> nouveau ». Le programme :
- refuse d'écraser la cible (v2) si elle existe (R12 ; ouverture en mode « x ») ;
- vérifie l'empreinte de la pièce de départ (v1) et celle du rapport de contre-lecture du tour 1 ;
- vérifie que chacun des huit couples des corrections 1 à 4 figure à la lettre dans le rapport
  (« - Ancien : `…` » suivi de « Nouveau : `…` », une seule fois) ;
- vérifie que chaque « ancien » (couples du rapport, couples de l'en-tête et de la section « Contre-lecture ») figure
  exactement une fois dans la v1, chevauchements compris, et qu'aucun ne chevauche un autre ;
- remplace en une seule passe, sur les positions de la v1 (un « nouveau » n'est jamais relu par un autre couple) ;
- contrôle la longueur de la cible et la présence de chaque « nouveau » avant de l'écrire ;
- prend l'heure de scellement (lue par `date -u`) en argument et la contrôle.

Les corrections 5 et 6 du rapport portent sur le devis v4 : elles ne sont pas appliquées ici.

Usage : python3 appliquer-corrections-regles-banc-calibration-mr2-tour1-v1.py "AAAA-MM-JJTHH:MM:SSZ"
"""
import datetime
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "regles-banc-calibration-mr2-v1.md"
SOURCE_SHA256 = "87d7536ee10a4f240aec7fe1ee4200e1a5d7d168daab816a4e8ca7e6139d87f7"
RAPPORT = ICI.parent / "contre-lecture-banc-complet-tour1-v1.md"
RAPPORT_SHA256 = "55e33514ca163280c9c3ffbd3873a92110d7031d0e16cba23122ac469c445a36"
CIBLE = ICI / "regles-banc-calibration-mr2-v2.md"
DIFFERENTIEL = "differentiel-regles-banc-calibration-mr2-v1-v2.diff"
PROGRAMME = pathlib.Path(__file__).name
DEBUT = "2026-11-17 03:29:30"  # `date -u`, rapport et v1 lus en entier

# Corrections 1 à 4 du rapport (section 5, « Pièce des règles »), couples recopiés à la lettre.
COUPLES_RAPPORT = [
    # Correction 1 : section 8, premier paragraphe.
    ("Elles se jouent **après** la règle (dont la passe qui décide est déjà scellée) : ainsi la règle reste la dernière étape de D-2 et",
     "Elles se jouent **après** la règle (dont la passe qui décide est déjà scellée), sauf trois relevés qui ne coûtent aucun calcul de plus et ne sont que rapportés après elle : M3 (C7 est un contrôle du tirage, étape de tirage S0, donc avant l'étape 1 ; seule une égalité à six décimales refuse un tirage, règle du vérificateur v2 inchangée, ce qui fait partie de la définition des mondes, non d'une mesure qui décide ; une exception de C7 est une exception d'étape : « banc non jugeable »), M5 (a) (relevé sur les tirages de S0) et M6 (durées relevées pendant les étapes 3, 5 et 6) : ainsi la règle reste la dernière étape de D-2 et"),
    # Correction 1 : section 12, ligne E-10.
    ("mesures jouées après la règle, lues avant elle (section 8, section 10)",
     "mesures jouées après la règle, sauf M3, M5 (a) et M6 relevées pendant le tirage et les étapes 3, 5 et 6 (section 8), toutes lues avant elle (section 10)"),
    # Correction 1 : section 11, garde B-6.
    ("dans une mesure hors D-2 → mesure « en échec », cause écrite",
     "dans une mesure hors D-2 (M3 exceptée : C7 relève du tirage, une exception y est une exception d'étape) → mesure « en échec », cause écrite"),
    # Correction 2 : section 4.2, table des flux, ligne `proposition`.
    ("| `proposition` | g | cartes synthétiques de la génération (une uniforme par composante et par carte, tirée quelle que soit sa probabilité) |",
     "| `proposition` | g, rang de carte | cartes synthétiques de la génération : une sous-suite par carte, qui tire d'abord une uniforme par effet du monde, connu ou non, quelle que soit sa probabilité, puis les bruits de la carte ; la taille de S d'une carte ne décale ainsi aucune autre carte, et deux passes ne diffèrent que par le seuil appliqué à la même uniforme (le code de la v4 tire uniformes et bruits d'un seul flux : à ne pas porter tel quel) |"),
    # Correction 3 : section 0, point 9.
    ("confirmation de Q-4 et Q-6 (Lazar ou la mère, brouillon 6, point",
     "confirmation de Q-4, de Q-6 et de l'étendue de Q-5 et de Q-8 (Lazar ou la mère, brouillon 6, point"),
    # Correction 3 : section 12, point 2.
    ("2. **Q-4 (nul v8) et Q-6 (retirage automatique)** : le banc en dépend (juge, tirage des mondes) ;",
     "2. **Q-4 (nul v8), Q-6 (retirage automatique) et l'étendue de Q-5 (règle de n) et de Q-8 (regroupement avant le juge)** : le banc en dépend (juge, tirage des mondes, règle de n, regroupement) ;"),
    # Correction 4 : Déclaration, « Interdits tenus ».
    ("aucun fichier existant modifié ; rien committé ;",
     "aucun fichier existant modifié ; rien committé de la main du rédacteur (voir Incidents) ;"),
    # Correction 4 : Déclaration, « Incidents ».
    ("des `__pycache__` ignorés par git peuvent en naître.",
     "des `__pycache__` ignorés par git peuvent en naître ; un autre processus de la session a committé des états non scellés de cette pièce pendant sa rédaction (commits `2687202c`, `48497ef3`, `c70b2261`, puis `a0993b93` dont le contenu égale la version scellée, `87d7536e…`) : seule la version scellée fait foi (R12)."),
]


def sha256(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def occurrences(texte, motif):
    """Nombre d'occurrences de `motif` dans `texte`, chevauchements compris."""
    n, i = 0, texte.find(motif)
    while i != -1:
        n += 1
        i = texte.find(motif, i + 1)
    return n


def section_contre_lecture(heure):
    return f"""
## Contre-lecture

### Tour 1 (v1 → v2)

- **Rapport** : `contre-lecture-banc-complet-tour1-v1.md` (dossier `docs/notes/organisme-multi-generations-v1/`), empreinte
  `{RAPPORT_SHA256}` ; lecteur : modèle C, contre-lecteur neuf (R2) ;
  verdict : **corrections (0 majeure, 6 mineures exigées ; 7 remarques facultatives)** ; les corrections 1 à 4 portent sur cette
  pièce, les corrections 5 et 6 sur le devis v4.
- **Pièce lue par le rapport** : la v1 de cette pièce, `{SOURCE_SHA256}` ; la v1
  reste intacte (R12).
- **Application** : par le programme `banc-calibration-mr2-v1/{PROGRAMME}`
  (scellé à côté avant son passage). Les huit couples « ancien → nouveau » des corrections 1 à 4 sont ceux du rapport, à la
  lettre : le programme vérifie que chacun y figure tel quel. Il vérifie aussi l'empreinte de la v1 et du rapport, que chaque
  « ancien » figure une seule fois dans la v1 sans en chevaucher un autre, remplace en une seule passe sur les positions de la v1,
  refuse d'écraser la v2, puis contrôle la longueur de la v2 et la présence de chaque « nouveau ». Différentiel v1 → v2 :
  `banc-calibration-mr2-v1/{DIFFERENTIEL}` (scellé).
- **Rédacteur des corrections** : un rédacteur neuf, sous-agent d'un script d'orchestration, que sa consigne déclare du modèle C
  (la même consigne porte aussi « corrections par le modèle A en fichiers neufs ») ; je n'ai écrit ni la v1, ni le rapport, ni la
  conception, ni le préenregistrement, ni le code du pilote, ni le devis. Le rapport est lui aussi du modèle C : si la
  déclaration est exacte, le même modèle a lu et corrigé à ce tour (provenance non établie au-delà de la consigne) ; un tour 2
  est à confier à un lecteur neuf qui n'a écrit ni la v1, ni le rapport, ni ces corrections, de préférence d'un autre modèle.
- **Ce qui a changé** : les huit couples du rapport ; dans l'en-tête, le titre, le statut, la ligne « Heures » et la ligne neuve
  « Version v2 » ; cette section. Rien d'autre.

Réponse point par point :

| point du rapport | où dans la pièce | suite |
|---|---|---|
| **Correction 1** (mineure) — M3 (C7) n'est ni jouée « après la règle » ni « sans décision » ; M5 (a) et M6 sont des relevés du tirage et des étapes 3, 5 et 6 | section 8, premier paragraphe ; section 12, ligne E-10 ; section 11, garde B-6 | **appliquée** (trois couples, texte du rapport) ; voir les observations 2 à 4 |
| **Correction 2** (mineure) — passes couplées seulement si chaque carte a sa propre sous-suite | section 4.2, table des flux, ligne `proposition` | **appliquée** (un couple, texte du rapport) ; le motif du rapport est inexact pour la v4 sur un point, la correction tient pour une autre raison (observation 1) |
| **Correction 3** (mineure) — étendue de Q-5 et de Q-8 oubliée | section 0, point 9 ; section 12, point 2 | **appliquée** (deux couples, texte du rapport) ; relu au brouillon 6 (`4deec525…`), « Points ouverts », point 11 : « Q-4 (nul v8), Q-6 (retirage automatique) et l'étendue de Q-5 et de Q-8 » : exact |
| **Correction 4** (mineure) — incident de provenance non déclaré | Déclaration, « Interdits tenus » et « Incidents » | **appliquée** (deux couples, texte du rapport) ; relu sur l'historique git du dépôt de travail (lecture seule) : quatre commits de la v1, `2687202c`, `48497ef3`, `c70b2261`, `a0993b93` ; seul le dernier rend `87d7536e…` : exact |
| **Corrections 5 et 6** (mineures) — devis v4 | aucune (autre pièce) | **non appliquées ici** : elles portent sur `devis-banc-calibration-mr2-v4.md`, hors de cette pièce ; à prendre dans une version suivante du devis |
| remarque 1 — δ_bas = 0,005 et médiane : point (ii) de la règle de n clément | 7.3, points 4 et 6 | facultative ; non portée (rien d'autre ne change) ; le rapport juge le choix recevable (E-5) |
| remarque 2 — « τ non mesurable » absent de la table de lecture | section 10 | facultative ; non portée ; à prendre dans la version finale si le lecteur du tour 2 ou la mère le veut |
| remarque 3 — sous-choix de τ : changer le seul mot de la règle 5 | 7.5, point 3 ; section 12, point 1 | facultative ; non portée ; la version finale, écrite après le mot de Lazar, est de toute façon un fichier neuf (voir l'observation 5) |
| remarque 4 — garde de durée et de mémoire en B-15 | section 11 ; section 13 | facultative ; non portée ; la garde reste dite en fin de section 13 et au devis v4 |
| remarque 5 — marqueurs [GRAINES-BANC] et [CHAMP-BORNE-HAUTE] ouverts | 4.2 ; 7.6 | facultative ; non portée ; le code gelé les lève, avec empreinte, avant la poussée (garde B-2) |
| remarque 6 — copies exactes de la règle de forme, cas le plus défavorable à la moyenne | 7.4 ; E-6 | facultative ; non portée ; choix du brouillon 6 (E-6) |
| remarque 7 — attendu du devis au juge de la course | aucune (devis) | hors de cette pièce |
| points pour la session mère (rapport, section 7) | section 0, point 9 ; section 12 | rien de plus à porter : Q-4, Q-6 et l'étendue de Q-5 et de Q-8 le sont par la correction 3 ; E-1, E-2, E-10, E-11 et le message à Lazar sont déjà en section 12 ; l'hypothèse (b) et l'indépendance des flux `choix` et `juge` restent à vérifier sur le code (annexe A ; V-22, V-23, garde 25) ; provenance de la v2 : paragraphe « Lectures et interdits de la v2 » ci-dessous |

Aucune correction exigée n'est refusée.

**Observations sans changement** (hors des couples du rapport, donc non appliquées ; pour le lecteur du tour 2 et la mère) :

1. **Motif de la correction 2, relu sur le code : inexact pour la v4 sur un point ; la correction tient pour une autre
   raison.** `course` (`outils-v4/monde_riche_v4.py`, `4b165847…`, lignes 212 à 229) tire bien uniformes et bruits d'un seul
   flux ; mais `_bruiter` (`outils-v1/puissance_monde_riche_v1.py`, `7344b107…`, lignes 234 à 242) tire un bruit par effet du
   monde entier, puis le vecteur des biais, avant de restreindre la carte à S (`monde_restreint`, sans tirage) : le nombre de ses
   tirages ne dépend pas de la taille de S ; comme chaque carte tire aussi une uniforme par effet du monde, la taille de S ne
   décale pas les cartes suivantes, et en génération 1, où le seul connu est l'effet de K1, deux passes de même drapeau de
   masquage sont déjà couplées carte par carte. Le découplage de la v4 est ailleurs : le flux porte le drapeau de masquage
   (`rng_de("v4-gen", w, masquage)`), et les uniformes vont d'abord aux effets connus (dans leur ordre trié), puis aux inconnus
   dans l'ordre des effets du monde ; dès la génération 2, si les connus diffèrent entre deux passes, une même uniforme tombe sur
   des effets différents. Le texte neuf (une sous-suite par carte, une uniforme par effet du monde, connu ou non) règle ces deux
   cas et rend l'énoncé de la section 4.2 vrai par construction.
2. Après la correction 1, d'autres endroits disent encore les mesures hors D-2 jouées après la règle ou sans effet, sans
   l'exception de M3, M5 (a) et M6 : le titre de la section 8 (« jouées après l'étape 6 ; rapportées ; ne décident rien »), la
   section 0 (point 1 : « ensuite seulement » ; point 7 : C7 parmi les mesures « sans effet sur aucune valeur »), la section 4.3
   (pas 8, après les étapes) et le nom de l'essai T-14 (« mesures après la règle ») ; l'exception n'est écrite qu'au premier
   paragraphe de la section 8, en E-10 et en B-6.
3. « S0 », dans le texte neuf de la correction 1, est le nom que le devis v4 donne au tirage et à la vérification des mondes
   (pas 6 de la section 4.3 de cette pièce) ; la pièce ne le définit pas ailleurs.
4. La garde B-6 neuve fait d'une exception de C7 une exception d'étape (« banc non jugeable ») ; la première ligne de la table de
   lecture (section 10) ne nomme que l'exception « dans une étape de D-2 », dont le tirage ne fait pas partie ; le cas y tombe
   par « nombre de mondes tirés ≠ 24 » si le tirage s'arrête.
5. Section 12, point 1 : « la pièce est refaite (v2) », écrit dans la v1, désigne la version qui suivrait un mot de Lazar pour la
   borne haute de Wilson, non cette v2 de corrections ; à lire « version suivante ».

**Lectures et interdits de la v2** : le rapport et la v1 lus en entier ; pour relire les constats des corrections 2 à 4 :
`course` (`outils-v4/monde_riche_v4.py`), `_bruiter` et `rng_de` (`outils-v1/puissance_monde_riche_v1.py`), la liaison `P1`
(`outils-v2/puissance_monde_riche_v2.py`, ligne 33), `monde_restreint` et `compiler_monde` (`outils-v1/monde_riche_outils_v1.py`),
le point ouvert 11 du brouillon 6 et le nom « S0 » du devis v4 (par recherche), toutes empreintes recalculées, égales à leur
compagnon ; l'historique git de la v1 (`git log`, `git show`, lecture seule) ; forme du programme reprise des programmes de
corrections du devis (tours 1 et 2). Aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune dépense ;
aucune branche du pilote ouverte ; aucun secret, aucun monde ; rien sous `diag/`, `runs/`, `donnees/` ; aucun fichier existant
modifié ; rien committé ; aucun git avec `GIT_DIR`, `GIT_WORK_TREE` ou `GIT_INDEX_FILE` ; aucun identifiant de modèle écrit. Le
programme, la v2 et le différentiel sont écrits chacun d'un seul coup, dans leur état final (programme mis au point au bloc-notes,
hors du dépôt), puis scellés.

Version v2 scellée : {heure} (`date -u`, relevée juste avant le scellement).
"""


def couples(heure):
    return [
        # En-tête : titre (version).
        ("# Règles du banc de calibration complet de la famille MR-2 (mondes riches à doublons) — v1\n",
         "# Règles du banc de calibration complet de la famille MR-2 (mondes riches à doublons) — v2\n"),
        # En-tête : statut (version).
        ("**v1, à contre-lire (R2)**. Elle ne lance rien,",
         "**v2, à contre-lire (R2, tour 2)**. Elle ne lance rien,"),
        # En-tête : heures, et ligne neuve « Version v2 ».
        ("  développement) 02:51:19 à 02:59:56 ; calcul du devis 03:05:41 ; fin de la rédaction : dernière ligne.\n",
         "  développement) 02:51:19 à 02:59:56 ; calcul du devis 03:05:41 ; fin de la rédaction de la v1 : ligne « Fin de la rédaction »,\n"
         "  juste avant la section « Contre-lecture ».\n"
         "- **Version v2** (corrections du tour 1) : la v1 (`banc-calibration-mr2-v1/regles-banc-calibration-mr2-v1.md`,\n"
         f"  `{SOURCE_SHA256}`, versée inchangée, R12) avec les seules corrections 1 à 4\n"
         f"  exigées par sa contre-lecture du tour 1 (`contre-lecture-banc-complet-tour1-v1.md`, `{RAPPORT_SHA256[:8]}…`), appliquées par couples\n"
         "  « ancien → nouveau », et l'en-tête mis à jour (titre, statut, heures, cette ligne) ; rédacteur des corrections, réponse point\n"
         "  par point et observations : section « Contre-lecture », en fin de pièce. Début de la v2 (rapport et v1 lus) :\n"
         f"  {DEBUT} ; **v2 scellée le {heure}** (`date -u`, relevée juste avant le scellement ;\n"
         "  dernière ligne). Elle reste **à contre-lire (tour 2)** et **non finale** (sous-choix de τ et points ouverts de la section 12).\n"),
    ] + COUPLES_RAPPORT + [
        # Section « Contre-lecture » créée (absente de la v1), après la dernière ligne de la v1.
        ("Fin de la rédaction : 2026-11-17T03:10:34Z (`date -u`, relevée juste avant le scellement).\n",
         "Fin de la rédaction : 2026-11-17T03:10:34Z (`date -u`, relevée juste avant le scellement).\n"
         + section_contre_lecture(heure)),
    ]


def main():
    if len(sys.argv) != 2:
        sys.exit("refus : donner l'heure de scellement lue par `date -u`, forme AAAA-MM-JJTHH:MM:SSZ")
    heure = sys.argv[1]
    try:
        datetime.datetime.strptime(heure, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        sys.exit(f"refus : heure {heure!r} illisible (forme AAAA-MM-JJTHH:MM:SSZ, lue par `date -u`)")
    if CIBLE.exists():
        sys.exit(f"refus : la cible {CIBLE.name} existe déjà ; on n'écrase jamais (R12)")
    if sha256(SOURCE) != SOURCE_SHA256:
        sys.exit(f"refus : empreinte de {SOURCE.name} inattendue")
    if sha256(RAPPORT) != RAPPORT_SHA256:
        sys.exit(f"refus : empreinte de {RAPPORT.name} inattendue")
    rapport = RAPPORT.read_text(encoding="utf-8")
    for i, (ancien, nouveau) in enumerate(COUPLES_RAPPORT, 1):
        motif = f"- Ancien : `{ancien}`\n  Nouveau : `{nouveau}`\n"
        k = occurrences(rapport, motif)
        if k != 1:
            sys.exit(f"refus : couple {i} du rapport trouvé {k} fois dans le rapport (exigé : 1, à la lettre)")
    texte = SOURCE.read_text(encoding="utf-8")
    tous = couples(heure)
    places = []
    for i, (ancien, nouveau) in enumerate(tous, 1):
        k = occurrences(texte, ancien)
        if k != 1:
            sys.exit(f"refus : couple {i}, « ancien » trouvé {k} fois dans la v1 (exigé : 1)")
        places.append((texte.index(ancien), i, ancien, nouveau))
    places.sort()
    for (p1, i1, a1, _), (p2, i2, _, _) in zip(places, places[1:]):
        if p1 + len(a1) > p2:
            sys.exit(f"refus : les « anciens » des couples {i1} et {i2} se chevauchent")
    morceaux, curseur = [], 0
    for p, _, ancien, nouveau in places:
        morceaux.append(texte[curseur:p])
        morceaux.append(nouveau)
        curseur = p + len(ancien)
    morceaux.append(texte[curseur:])
    resultat = "".join(morceaux)
    attendu = len(texte) + sum(len(n) - len(a) for a, n in tous)
    if len(resultat) != attendu:
        sys.exit(f"refus : longueur de la v2 {len(resultat)} au lieu de {attendu}")
    for i, (_, nouveau) in enumerate(tous, 1):
        if nouveau not in resultat:
            sys.exit(f"refus : « nouveau » du couple {i} absent de la v2")
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(resultat)
    print(f"écrit : {CIBLE.name} ({len(tous)} couples, dont {len(COUPLES_RAPPORT)} du rapport) ; "
          f"empreinte {sha256(CIBLE)}")


if __name__ == "__main__":
    main()
