#!/usr/bin/env python3
"""Applique à la pièce des règles du banc de calibration complet MR-2 (v2) les corrections 7 à 14 de sa contre-lecture du tour 2.

Couples « ancien -> nouveau ». Le programme :
- refuse d'écraser la cible (v3) si elle existe (R12 ; ouverture en mode « x ») ;
- vérifie l'empreinte de la pièce de départ (v2) et celle du rapport de contre-lecture du tour 2 ;
- vérifie que chacun des dix couples des corrections 7 à 14 figure à la lettre dans le rapport
  (« - Ancien : `…` » suivi de « Nouveau : `…` », une seule fois) ;
- pose le « nouveau » de la correction 7 avec deux mots de plus (« pris avant elle » -> « pris avant ou pendant elle ») et
  vérifie que le texte posé égale celui du rapport à ces deux mots près (motif : section « Contre-lecture », tour 2, de la v3) ;
  les neuf autres « nouveaux » sont posés à la lettre du rapport ;
- vérifie que chaque « ancien » (couples du rapport, couples de l'en-tête et de la section « Contre-lecture ») figure
  exactement une fois dans la v2, chevauchements compris, et qu'aucun ne chevauche un autre ;
- remplace en une seule passe, sur les positions de la v2 (un « nouveau » n'est jamais relu par un autre couple) ;
- contrôle la longueur de la cible, la présence de chaque « nouveau » et l'absence de chaque « ancien » du rapport avant de
  l'écrire ;
- prend l'heure de scellement (lue par `date -u`) en argument et la contrôle.

Usage : python3 appliquer-corrections-regles-banc-calibration-mr2-tour2-v1.py "AAAA-MM-JJTHH:MM:SSZ"
"""
import datetime
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "regles-banc-calibration-mr2-v2.md"
SOURCE_SHA256 = "aa1f29dda476dc1492afb20d40714a0753df84c67ead5b126f84860b921d7a2c"
RAPPORT = ICI.parent / "contre-lecture-banc-complet-tour2-v1.md"
RAPPORT_SHA256 = "11086f65aba3c43b888ba048ebca9bfd2b1b757ed136bc597e823b4a4a3f6bc0"
CIBLE = ICI / "regles-banc-calibration-mr2-v3.md"
DIFFERENTIEL = "differentiel-regles-banc-calibration-mr2-v2-v3.diff"
PROGRAMME = pathlib.Path(__file__).name
DEBUT = "2026-11-17 03:48:04"  # `date -u`, rapport et v2 lus en entier

# Corrections 7 à 14 du rapport (section 2), couples recopiés à la lettre.
COUPLES_RAPPORT = [
    # Correction 7 : section 0, point 1.
    ("dernier** ; ensuite seulement, des mesures qui ne décident rien.",
     "dernier** ; ensuite seulement, des mesures qui ne décident rien (sauf trois relevés pris avant elle, M3, M5 (a) et M6, section 8)."),
    # Correction 8 : section 0, point 7.
    ("effet sur aucune valeur.",
     "effet sur aucune valeur des étapes 1 à 6, hormis le refus d'un tirage par C7 (M3, section 8)."),
    # Correction 9 : titre de la section 8.
    ("(jouées après l'étape 6 ; rapportées ; ne décident rien)",
     "(jouées après l'étape 6, sauf M3, M5 (a) et M6 relevées pendant le tirage et les étapes 3, 5 et 6 ; rapportées ; ne décident rien)"),
    # Correction 10 : section 4.3, pas 8.
    ("8. Mesures hors D-2 (section 8).",
     "8. Mesures hors D-2 (section 8) ; M3, M5 (a) et M6 ont déjà été relevées aux pas 6 et 7."),
    # Correction 10 : section 13, essai T-14.
    ("| T-14 | mesures après la règle |",
     "| T-14 | mesures hors D-2 après la règle (M3 exceptée : étape de tirage) |"),
    # Correction 11 : section 8, premier paragraphe (M3).
    ("étape de tirage S0",
     "étape de tirage (pas 6 de la section 4.3, « S0 » du devis v4)"),
    # Correction 11 : section 8, premier paragraphe (M5 (a)).
    ("tirages de S0)",
     "tirages du pas 6)"),
    # Correction 12 : section 12, ligne E-1.
    ("| module neuf égal à la v4 (section 2) |",
     "| module neuf égal à la v4 (section 2), sauf les flux des générations simulées (section 4.2 : sous-suite par carte, drapeau de masquage hors des clés), écart voulu |"),
    # Correction 13 : section 2, « Conséquences », première puce (essai R5-7).
    ("du champ `resultat` d'une génération simulée par le port de `course`)",
     "du champ `resultat` d'une génération simulée par le port de `course`, la référence recevant les cartes et les flux de jugement du banc, non ses propres flux ; ou, à défaut, égalité sur les contrôles seuls, écart écrit)"),
    # Correction 14 : section 12, « À trancher avant le banc », point 1.
    ("la pièce est refaite (v2).",
     "la pièce est refaite (version suivante)."),
]

# Seul écart à la lettre du rapport : deux mots ajoutés au « nouveau » de la correction 7 (rang 0 ci-dessus).
# Motif : M6 relève aussi les durées des regroupements de l'étape 6, donc pendant la règle (section 8, ligne M6 ;
# corrections 9 et 10) ; sans ces deux mots, la section 0 dirait M6 prise avant la règle.
AMENDEMENTS = {0: ("pris avant elle", "pris avant ou pendant elle")}


def sha256(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def occurrences(texte, motif):
    """Nombre d'occurrences de `motif` dans `texte`, chevauchements compris."""
    n, i = 0, texte.find(motif)
    while i != -1:
        n += 1
        i = texte.find(motif, i + 1)
    return n


def couples_poses():
    """Couples du rapport tels qu'ils sont posés : à la lettre, sauf l'amendement déclaré."""
    poses = []
    for i, (ancien, nouveau) in enumerate(COUPLES_RAPPORT):
        if i in AMENDEMENTS:
            avant, apres = AMENDEMENTS[i]
            if occurrences(nouveau, avant) != 1:
                sys.exit(f"refus : amendement du couple {i + 1} : « {avant} » non trouvé une seule fois dans le « nouveau » du rapport")
            pose = nouveau.replace(avant, apres)
            # Le texte posé égale celui du rapport, à l'insertion des deux mots près.
            if len(pose) - len(nouveau) != len(apres) - len(avant) or pose.replace(apres, avant) != nouveau:
                sys.exit(f"refus : amendement du couple {i + 1} hors de ce qui est déclaré")
            poses.append((ancien, pose))
        else:
            poses.append((ancien, nouveau))
    return poses


def section_contre_lecture(heure):
    return f"""
### Tour 2 (v2 → v3)

- **Rapport** : `contre-lecture-banc-complet-tour2-v1.md` (dossier `docs/notes/organisme-multi-generations-v1/`), empreinte
  `{RAPPORT_SHA256}` ; lecteur : modèle C, contre-lecteur neuf (R2) ;
  verdict : **corrections (0 majeure, 7 mineures exigées ; 3 remarques facultatives)** ; le rapport numérote en fait huit
  corrections exigées, 7 à 14 (dix couples), toutes sur cette pièce ; les huit sont traitées ci-dessous.
- **Pièce lue par le rapport** : la v2 de cette pièce, `{SOURCE_SHA256}` ; la v2
  reste intacte (R12).
- **Application** : par le programme `banc-calibration-mr2-v1/{PROGRAMME}`
  (scellé à côté avant son passage). Les dix couples « ancien → nouveau » des corrections 7 à 14 sont ceux du rapport : le
  programme vérifie que chacun y figure à la lettre. Il pose le « nouveau » de la correction 7 avec deux mots de plus (« ou
  pendant », motif ci-dessous) et vérifie qu'il égale celui du rapport à ces deux mots près ; les neuf autres sont posés à la
  lettre. Il vérifie aussi l'empreinte de la v2 et du rapport, que chaque « ancien » figure une seule fois dans la v2 sans en
  chevaucher un autre, remplace en une seule passe sur les positions de la v2, refuse d'écraser la v3, puis contrôle la longueur
  de la v3, la présence de chaque « nouveau » et l'absence de chaque « ancien » du rapport. Différentiel v2 → v3 :
  `banc-calibration-mr2-v1/{DIFFERENTIEL}` (scellé).
- **Rédacteur des corrections** : un rédacteur neuf, sous-agent d'un script d'orchestration, que sa consigne déclare du modèle C
  (la même consigne porte aussi « corrections par le modèle A en fichiers neufs », comme au tour 1) ; je n'ai écrit ni la v1, ni
  la v2, ni les rapports des tours 1 et 2, ni la conception, ni le préenregistrement, ni le code du pilote, ni le devis.
  **Même lignée** (rapport, section 5) : le rapport du tour 2, celui du tour 1 et le rédacteur des corrections du tour 1 se
  déclarent aussi du modèle C ; si les déclarations sont exactes, le même modèle a lu et corrigé à ce tour encore (provenance non
  établie au-delà des consignes). Un tour 3 est à confier à un lecteur neuf qui n'a écrit ni la v2, ni le rapport, ni ces
  corrections, d'une autre lignée que A (rédacteur de la pièce) et que C (lectures et corrections des tours 1 et 2) si la mère
  le peut.
- **Ce qui a changé** : les dix couples du rapport (la correction 7 avec les deux mots dits) ; dans l'en-tête, le titre, le
  statut, le renvoi de la ligne « Version v2 » (« dernière ligne » n'y était plus vrai ; « reste » y devient « restait ») et la
  ligne neuve « Version v3 » ; cette sous-section. Rien d'autre.

Réponse point par point :

| point du rapport | où dans la pièce | suite |
|---|---|---|
| **Correction 7** (mineure) — section 0, point 1 : « ensuite seulement » contredit l'exception de M3, M5 (a) et M6 | section 0, point 1 | **appliquée, avec deux mots de plus** : « pris avant elle » devient « pris avant ou pendant elle » ; le reste est le texte du rapport. Motif : M6 relève aussi les durées des regroupements de l'étape 6 (section 8, ligne M6 ; texte des corrections 9 et 10 : « pendant le tirage et les étapes 3, 5 et 6 », « aux pas 6 et 7 »), donc pendant la règle ; à la lettre du rapport, la section 0 dirait M6 prise avant la règle et la section 8 pendant elle, la contradiction même que la correction ferme. Refus de la lettre limité à ces deux mots, à juger au tour 3 |
| **Correction 8** (mineure) — section 0, point 7 : C7 « sans effet sur aucune valeur » alors qu'il refuse un tirage | section 0, point 7 | **appliquée** (texte du rapport) |
| **Correction 9** (mineure) — titre de la section 8 | section 8, titre | **appliquée** (texte du rapport) |
| **Correction 10** (mineure) — pas 8 de l'ordre des engagements ; nom de l'essai T-14 | section 4.3, pas 8 ; section 13, ligne T-14 | **appliquée** (deux couples, texte du rapport) ; relu : pas 6 = tirage (M3, M5 (a)), pas 7 = étapes 1 à 6 (M6 aux étapes 3, 5 et 6) : exact |
| **Correction 11** (mineure) — « S0 » non défini dans la pièce | section 8, premier paragraphe (M3 et M5 (a)) | **appliquée** (deux couples, texte du rapport) ; relu au devis v4 (`a64ad406…`, ligne 59 : « S0, tirage et vérification ») et au pas 6 de la section 4.3 (« Tirage et vérification des 24 mondes ») : exact |
| **Correction 12** (mineure) — E-1 : flux des générations simulées autres que ceux de la v4, écart à déclarer à la mère | section 12, ligne E-1 | **appliquée** (texte du rapport) ; relu à la section 4.2 (flux `proposition` indexé par g et le rang de carte ; flux des générations simulées indépendants de la passe et du drapeau de masquage) : exact ; colonne « qui tranche » inchangée (la mère confirme) ; voir les observations 2 et 3 |
| **Correction 13** (mineure) — R5-7 : égalité du champ `resultat` impossible aux flux de la section 4.2 | section 2, « Conséquences », première puce | **appliquée** (texte du rapport) ; voir les observations 3 et 4 |
| **Correction 14** (mineure) — « la pièce est refaite (v2) » devenu ambigu | section 12, « À trancher avant le banc », point 1 | **appliquée** (texte du rapport) ; ferme l'observation 5 du tour 1 |
| verdict : « 7 mineures exigées » | — | le rapport en numérote huit (7 à 14) ; les huit sont traitées ; sans autre suite |
| section 1 du rapport : le point 4 de la section 12 renvoie au « devis v4 », « à mettre à jour avec le devis v5 » | section 12, point 4 (et les autres renvois au devis v4 : section 0, point 9 ; section 4.3, pas 3 ; garde B-10 ; fin de la section 13) | **non porté** : ce n'est pas un couple exigé, et le devis v5 n'existe pas encore (dossier relu : devis v1 à v4 seulement) ; à porter, avec tous ces renvois, dans la version qui suivra le devis v5 |
| remarque 1 — second cas de T-14 : exception de C7 au tirage → « banc non jugeable » | section 13, ligne T-14 ; section 11, garde B-6 | facultative ; non portée (consigne : seules les corrections exigées) ; à prendre dans la version finale si le lecteur du tour 3 ou la mère le veut |
| remarque 2 — remarques 1 à 7 du tour 1 non exigées, dont « τ non mesurable » | — | facultatives ; non portées ; réponse du tour 1 inchangée |
| remarque 3 — nommer « exception de C7 au tirage » dans la première ligne de la table de lecture | section 10, table de lecture | facultative ; non portée ; le cas y tombe déjà par « nombre de mondes tirés ≠ 24 » (observation 4 du tour 1) |
| points pour la session mère (rapport, section 5) | en-tête ; section 12 | même lignée : dite ci-dessus ; devis v5 : hors de cette pièce ; écart des flux : porté en E-1 (correction 12) et en R5-7 (correction 13), confirmation de la mère attendue, voir l'observation 3 ; nœuds de Lazar (sous-choix de τ ; Q-4, Q-6, étendue de Q-5 et de Q-8) et points de la mère (E-1, E-2, E-10, E-11) : inchangés, section 12 ; risque (code non écrit, échéance du 30 novembre) : inchangé |

Aucune correction exigée n'est refusée en entier ; de la lettre de la correction 7, seuls deux mots sont ajoutés (ci-dessus).

**Observations sans changement** (hors des couples du rapport, donc non appliquées ; pour le lecteur du tour 3 et la mère) :

1. Des observations du tour 1, les points 2, 3 et 5 sont clos par les corrections 7 à 11 et 14 ; le point 4 reste ouvert (remarque 3
   du rapport, facultative) ; le point 1 est jugé exact par le rapport (section 1) et n'appelait aucun changement.
2. La section 0 (point 2) et la section 2 (lecture (b)) disent encore le module neuf « égal à la v4 » sans l'exception que la
   correction 12 écrit en E-1. Lecture qui les accorde : le module (générateur, vérificateur, port de `course` réservé aux essais)
   est égal à la v4 ; les générations simulées du banc sont jouées par le lanceur avec la chaîne de la course et les flux de la
   section 4.2 (section 3, paragraphe sous la table). Si la mère veut l'exception écrite là aussi, ce sont deux couples de plus.
3. La même différence de flux touche la seconde clause de R5-8 (conception v7 §2.4, phrase qui suit la table R5-1 à R5-7 : « les
   passes à masquage vrai restent égales à la v4 (R5-7) ») et la parenthèse de la section 3 sur le port de `course` (« graines de
   la v4 ») : l'égalité y passerait par la voie que la correction 13 écrit pour R5-7 (cartes et flux de jugement du banc donnés à
   la référence). Non changé ici ; à confirmer par la mère avec E-1.
4. Le repli de la correction 13 (« à défaut, égalité sur les contrôles seuls, écart écrit ») ne dit ni qui constate le défaut, ni
   si ce repli compte comme un succès de R5-7, dont l'échec est un nœud (puce suivante de la section 2) ; à fixer par la
   contre-lecture du code.

**Lectures et interdits de la v3** : le rapport du tour 2 et la v2 lus en entier ; pour relire les constats des corrections : le
rapport du tour 1 (entier), le devis v4 (recherche de « S0 », ligne 59), la conception v7 (§2.4 : table R5-1 à R5-7 et phrase de
R5-8), toutes empreintes recalculées, égales à leur compagnon ; la liste du dossier `banc-calibration-mr2-v1/` (pas de devis v5) ;
les lignes GO-2026-11-13-01 et -13-02 du registre `registres/go.md` ; forme du programme et du différentiel reprise du tour 1.
Aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune dépense ; aucune branche du pilote ouverte ; aucun
secret, aucun monde ; rien sous `diag/`, `runs/`, `donnees/` ; aucun fichier existant modifié ; rien committé ; aucune commande
git ; aucun identifiant de modèle écrit. Le programme a été mis au point au bloc-notes, sur des copies, hors du dépôt, puis versé
d'un seul coup dans le dossier et scellé avant son passage ; la v3 et le différentiel sont écrits chacun d'un seul coup, puis
scellés.

Version v3 scellée : {heure} (`date -u`, relevée juste avant le scellement).
"""


def couples(heure):
    return [
        # En-tête : titre (version).
        ("# Règles du banc de calibration complet de la famille MR-2 (mondes riches à doublons) — v2\n",
         "# Règles du banc de calibration complet de la famille MR-2 (mondes riches à doublons) — v3\n"),
        # En-tête : statut (version).
        ("**v2, à contre-lire (R2, tour 2)**. Elle ne lance rien,",
         "**v3, à contre-lire (R2, tour 3)**. Elle ne lance rien,"),
        # En-tête : renvoi de la ligne « Version v2 » (elle n'est plus la dernière), et ligne neuve « Version v3 ».
        ("  dernière ligne). Elle reste **à contre-lire (tour 2)** et **non finale** (sous-choix de τ et points ouverts de la section 12).\n",
         "  ligne « Version v2 scellée », à la fin du tour 1 de la section « Contre-lecture »). Elle restait **à contre-lire (tour 2)** et\n"
         "  **non finale** (sous-choix de τ et points ouverts de la section 12).\n"
         "- **Version v3** (corrections du tour 2) : la v2 (`banc-calibration-mr2-v1/regles-banc-calibration-mr2-v2.md`,\n"
         f"  `{SOURCE_SHA256}`, versée inchangée, R12) avec les seules corrections 7 à 14\n"
         f"  exigées par sa contre-lecture du tour 2 (`contre-lecture-banc-complet-tour2-v1.md`, `{RAPPORT_SHA256[:8]}…`), appliquées par couples\n"
         "  « ancien → nouveau » (la correction 7 avec deux mots de plus, motivés à la section « Contre-lecture », tour 2), et l'en-tête mis\n"
         "  à jour (titre, statut, renvoi de la ligne « Version v2 », cette ligne) ; rédacteur des corrections, réponse point par point et\n"
         f"  observations : section « Contre-lecture », tour 2, en fin de pièce. Début de la v3 (rapport et v2 lus) : {DEBUT} ;\n"
         f"  **v3 scellée le {heure}** (`date -u`, relevée juste avant le scellement ; dernière ligne). Elle reste **à contre-lire\n"
         "  (tour 3)** et **non finale** (sous-choix de τ et points ouverts de la section 12).\n"),
    ] + couples_poses() + [
        # Section « Contre-lecture » : sous-section « Tour 2 » ajoutée après la dernière ligne de la v2.
        ("Version v2 scellée : 2026-11-17T03:39:37Z (`date -u`, relevée juste avant le scellement).\n",
         "Version v2 scellée : 2026-11-17T03:39:37Z (`date -u`, relevée juste avant le scellement).\n"
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
            sys.exit(f"refus : couple {i}, « ancien » trouvé {k} fois dans la v2 (exigé : 1)")
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
        sys.exit(f"refus : longueur de la v3 {len(resultat)} au lieu de {attendu}")
    for i, (_, nouveau) in enumerate(tous, 1):
        if nouveau not in resultat:
            sys.exit(f"refus : « nouveau » du couple {i} absent de la v3")
    for i, (ancien, _) in enumerate(COUPLES_RAPPORT, 1):
        k = occurrences(resultat, ancien)
        if k != 0:
            sys.exit(f"refus : « ancien » du couple {i} du rapport encore présent {k} fois dans la v3")
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(resultat)
    print(f"écrit : {CIBLE.name} ({len(tous)} couples, dont {len(COUPLES_RAPPORT)} du rapport, "
          f"{len(AMENDEMENTS)} amendé) ; empreinte {sha256(CIBLE)}")


if __name__ == "__main__":
    main()
