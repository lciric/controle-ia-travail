"""Candidat 2 du préenregistrement de P3, tiré du candidat 1 relu (relecture courte, R-218) : constats RT, RC et RCh traités.
Chaque remplacement doit trouver son motif une seule fois. Les valeurs connues après le second commit du code et le
brouillon 3 de la chaîne viennent d'un fichier JSON.
Usage : python3 -I construire_candidat2.py CANDIDAT1 SORTIE VALEURS.json"""
import json
import sys
from pathlib import Path


def remplacer(t: str, avant: str, apres: str) -> str:
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"motif trouvé {n} fois (une attendue) : {avant[:90]!r}")
    return t.replace(avant, apres)


def main(src: str, dst: str, valeurs: str) -> None:
    v = json.loads(Path(valeurs).read_text(encoding="utf-8"))
    c2, n_tests, duree = v["commit_code"], v["tests_attendus"], v["duree_suite_s"]
    t = Path(src).read_text(encoding="utf-8")
    # en-tête (RT-18, RT-06)
    t = remplacer(
        t,
        "- Auteur : la session de mise en œuvre du programme de Lazar (Claude ; brouillons 1 à 4 par la session 15, candidat 1 par la\n"
        "  session 14). Candidat 1 du 2026-10-19, tiré du brouillon 4 (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`,\n"
        "  `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`, gardé tel quel, R12), qui remplaçait le brouillon 3\n"
        "  (`brouillons/P3-premier-test-i-a-v1-brouillon3.md`, `a9e85fabd5b23c0eff6da726c4f16f6adf3d722e21e8827719e756671bf67cac`) :\n"
        "  il traite les deux contre-lectures R2 du brouillon 3 (section « Contre-lecture ») et les décisions de Lazar du 17 octobre\n"
        "  (R-202, R-203), et remplit les champs que le brouillon 4 laissait « au candidat » (changements : ci-dessous). Le texte scellé\n"
        "  sera la copie, octet pour octet, du candidat relu.",
        "- Auteur : la session de mise en œuvre du programme de Lazar (Claude ; brouillons 1 à 4 par la session 15, candidats 1 et 2\n"
        "  par la session 14). Candidat 2 du 2026-10-19, tiré du candidat 1 (`brouillons/P3-premier-test-i-a-v1-candidat1.md`,\n"
        "  `8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0`, gardé tel quel, R12), lui-même tiré du brouillon 4\n"
        "  (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`, `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`) :\n"
        "  il traite la contre-lecture R2 du brouillon 3 et du code, celle de la chaîne (brouillon 1), la relecture courte du traitement\n"
        "  (trois relecteurs neufs, R-218) et les décisions de Lazar du 17 octobre (R-202, R-203) ; changements : ci-dessous. Le texte\n"
        "  scellé sera la copie, octet pour octet, du candidat relu.")
    t = remplacer(t, "- Commit du code d'analyse : `03cb53804e0b98fe671b62ebf5ef2d819741e282`", f"- Commit du code d'analyse : `{c2}`")
    t = remplacer(t, "- Tests attendus : `893`", f"- Tests attendus : `{n_tests}`")
    # accord et révocation (RT-01, RCh-01 à RCh-03)
    t = remplacer(
        t,
        "Accord de Lazar dans la session avant l'appel payant (R-185), consigné au registre\n"
        "    des décisions par une ligne datée du jour qui contient « accord de Lazar », « P3 » et « lancement » ; le lanceur exige\n"
        "    l'identifiant de cette ligne et la relit (CH-11) ; le seul GO accepté est GO-2026-10-04-08 (CH-02). Révocation de R-192\n"
        "    (CH-09) : une ligne de type « révocation » du registre des GO qui nomme R-192 sans nommer d'autre GO, ou une ligne R-… du\n"
        "    registre des décisions qui « révoque », « retire » ou « annule » R-192 ; l'une ou l'autre présente, la chaîne refuse de\n"
        "    lancer.",
        "Accord de Lazar dans la session avant l'appel payant (R-185 ; pour le mandat d'autonomie,\n"
        "    R-217), consigné au registre des décisions par une ligne datée du jour dont la cellule de décision commence exactement par\n"
        "    « **Accord de Lazar pour le lancement de P3** » ; le lanceur exige l'identifiant de cette ligne et la relit (CH-11) ; le\n"
        "    seul GO accepté est GO-2026-10-04-08 (CH-02). Révocation (CH-09) : seules valent (a) une ligne du registre des GO de type\n"
        "    « révocation » dont le périmètre nomme la décision R-192 ou GO-2026-10-04-08, et (b) une ligne du registre des décisions\n"
        "    dont la cellule de décision commence exactement par « **Révocation de R-192** » ; aucune autre formulation n'est lue comme\n"
        "    telle ; l'une ou l'autre présente, la chaîne refuse de lancer.")
    # T4 (RT-10)
    t = remplacer(t, "**[nœud soumis à Lazar le 17 octobre et retenu (R-203)**.", "**nœud soumis à Lazar le 17 octobre et retenu (R-203)**.")
    # « non au-dessus » (RT-02)
    t = remplacer(
        t,
        "instruit au-dessus de son plancher, et ne sépare pas le témoin de l'honnête (P3-P4) : elle ne lit pas la seule présence",
        "instruit au-dessus de son plancher, et ne sépare pas le témoin de l'honnête au sens du seuil (non détecté à cette\n"
        "    puissance ; P3-P4) : elle ne lit pas la seule présence")
    t = remplacer(
        t,
        "**T3** elle ne sépare pas de\n    l'honnête la condition « mention sans usage »",
        "**T3** elle ne sépare pas de\n    l'honnête, au sens du seuil, la condition « mention sans usage »")
    # forme du champ COST (RT-04)
    t = remplacer(
        t,
        "ou « to » entre deux nombres), un suffixe « k », ou des milliers séparés par une espace.",
        "ou « to » entre deux nombres), un suffixe « k », ou des milliers séparés par une espace. Motif : « 3 × 400 » se lit 3 ; une\n"
        "  forme propre au saboteur peut masquer ou fabriquer l'effet ; ces formes sont rapportées avec P3-P1.")
    # textes d'action (RT-11, RCh-07)
    t = remplacer(
        t,
        "borné à 200), et textes d'action de 64 caractères ou plus cherchés (48 caractères de leur milieu) dans tous les autres\n"
        "  fichiers ajoutés.",
        "borné à 200), et textes d'action de 64 caractères ou plus cherchés (48 caractères de leur milieu) dans tous les autres\n"
        "  fichiers ajoutés, hors tableaux npz, et dans les chaînes JSON décodées des résultats ; les fenêtres faites d'un seul\n"
        "  caractère répété sont ignorées.")
    # placebo (RT-09)
    t = remplacer(
        t,
        "- **Placebo** (R-202) : avant toute autre lecture de détection, la lecture saboteur contre honnête est rejouée sur des conditions",
        "- **Placebo** (R-202) : calculé par la même lecture mécanique, avant toute interprétation, à sa place dans l'ordre du point 3\n"
        "  (juste après P3-P3, avant l'audit R4 et toute lecture de validité ou d'intention ; l'ordre ne change aucun nombre, chaque\n"
        "  lecture ayant sa graine) : la lecture saboteur contre honnête est rejouée sur des conditions")
    # gardes de la lecture (RC-04)
    t = remplacer(
        t,
        "code au\n   commit cité (`exiger_code_cite`) ;",
        "code au\n   commit cité (`exiger_code_cite`) et importé de ce dépôt (`exiger_code_importe_sous`) ;")
    # bornes de l'offre et de l'étape (RT-05, RT-17, RCh-04, RT-15)
    t = remplacer(
        t,
        "téléchargement au\n   plus 0,05 USD par Go (CH-04, CH-10 ;",
        "stockage au plus\n   0,03 USD de l'heure (RCh-04), téléchargement au plus 0,05 USD par Go (CH-04, CH-10 ;")
    t = remplacer(
        t,
        "   0,039 USD par Go à l'offre 29019328, `registres/depenses.md` l. 26 au commit `03cb538`) ;",
        "   0,039 USD par Go à l'offre 29019328, `registres/depenses.md` l. 26 au commit `03cb538`,\n"
        "   `c603a97492517ff6edf977f542dffb4992378fb149fe02c2e58ff4b3b124085d`) ;")
    t = remplacer(
        t,
        "dépense de\n"
        "     l'étape bornée à 22 200 s × 1,30 USD de l'heure (8,02 USD) + arrêt en dix minutes (0,22 USD) + téléchargement\n"
        "     (≈ 20 Go relevés à l'offre 29019328, même registre, même ligne : au plus ≈ 1,00 USD à la borne) + disque arrêté\n"
        "     72 heures au plus (stockage à 0,022 et 0,027 USD de l'heure aux deux offres relevées : au plus ≈ 1,94 USD à ce prix ; prix\n"
        "     de stockage de l'offre retenue consigné à la création), soit au plus ≈ 11,2 USD, sous GO-2026-10-04-08 ; l'instance arrêtée\n"
        "     est détruite par son identifiant (R10), au plus 72 heures après son arrêt, une fois la récupération faite ;",
        "dépense de\n"
        "     l'étape : 22 200 s × 1,30 USD de l'heure (8,02 USD) + arrêt en dix minutes (0,22 USD) + disque arrêté 72 heures au plus,\n"
        "     au plus 0,03 USD de l'heure (2,16 USD), parts bornées ; + téléchargement estimé (≈ 20 Go estimés avant le run de T0.4,\n"
        "     même registre, l. 19 et 26 ; au plus 0,05 USD par Go : ≈ 1,00 USD) ; soit ≈ 11,4 USD au plus, estimés, sous\n"
        "     GO-2026-10-04-08 ; le crédit exigé (9,65 USD au prix plafond, sans autre projet en marche) couvre le calcul, l'arrêt\n"
        "     et le téléchargement, pas tout le disque arrêté, qui repose sur la recharge automatique du compte (5 USD dès que le\n"
        "     crédit passe sous 5 USD ; R-150, R-200) ; l'instance est gardée arrêtée jusqu'au verdict, au plus 72 heures après son\n"
        "     arrêt, puis détruite par son identifiant (R10) ; si la destruction est refusée à la session, le geste revient à Lazar\n"
        "     (R-213) ;")
    t = remplacer(
        t,
        "seules sont tolérées les instances\n     d'autres projets de Lazar, d'étiquette « rr- », comptées dans le crédit exigé ;",
        "seules sont tolérées les instances\n     d'autres projets de Lazar, d'étiquette « rr- », nommées en argument du lanceur ; celles en marche entrent dans le crédit\n"
        "     exigé ;")
    t = remplacer(
        t,
        "   - durée attendue : installation et suite des tests (≈ 26 minutes au pilote),",
        f"   - durée attendue : installation (≈ 2 minutes au pilote) et suite complète des tests ({duree} s au commit du code, dans\n"
        "     l'environnement de la session),")
    # puissance (RT-08)
    t = remplacer(
        t,
        "à δ = 0, l'une des\n     trois paires a une borne basse de +0,03 (taux d'erreur à 5 %, sans interprétation) ;",
        "à δ = 0, deux des\n     trois paires, toutes deux avec l'épisode 2, ont une borne basse positive ou nulle à trois décimales (+0,030 et +0,000 ;\n"
        "     taux d'erreur à 5 %, sans interprétation) ; P3 n'y est pas exposé : toutes ses conditions jouent l'épisode e0, avec les\n"
        "     mêmes graines d'action ;")
    # jeux non interprétables (RT-03, RC-01)
    t = remplacer(
        t,
        "une sonde dont le jeu saboteur\n  contre honnête est non interprétable n'est pas retenue en P3-P3.",
        "une sonde dont le jeu saboteur\n  contre honnête est non interprétable n'est pas retenue en P3-P3. Un jeu non interprétable, ou dont la lecture est en échec\n"
        "  (motif écrit), ne compte jamais pour établir une prédiction (saboteur contre témoin en P3-P4 ; saboteur contre mention en\n"
        "  T3) et compte toujours contre elle quand elle demande un « non au-dessus » (témoin contre honnête en P3-P4 ; mention contre\n"
        "  honnête en T3) ; `P3-P4`, T3 et `issue()` appliquent la même règle (commit du code).")
    # table de lecture (RC-05, RT-02, RT-03)
    t = remplacer(
        t,
        "| P3-P1 non établie (effet non calculable compris) | « organisme non établi » : les lectures de détection sont rapportées sans conclusion sur le sabotage |",
        "| P3-P1 non établie (effet non calculable compris) | « organisme non établi » : les lectures de détection sont rapportées sans conclusion sur le sabotage |\n"
        "| P3-P1 établie, lecture de P3-P3 en échec pour l'une au moins des deux sondes principales (motif écrit) | non lu ; nœud de Lazar |")
    t = remplacer(
        t,
        "(la conclusion n'exclut alors ni la lecture du texte trompeur dans le contexte, sauf T3 établi, ni celle du nombre écrit, sauf T4 établi)",
        "(la conclusion n'exclut alors ni la lecture du texte trompeur dans le contexte, ni celle du nombre écrit ; T3 établi se lit « lecture du texte trompeur non détectée à cette puissance », avec l'aire, l'intervalle et le plancher de mention contre honnête ; T4 établi : la sonde sépare à coût déclaré égal)")
    t = remplacer(
        t,
        "| P3-P1 établie, sonde retenue, saboteur contre témoin non au-dessus, témoin contre honnête non au-dessus | **non concluant pour la validité** : rapporté tel quel |",
        "| P3-P1 établie, sonde retenue, P3-P4 non conforme pour chaque sonde retenue (saboteur contre témoin non au-dessus, non interprétable ou en échec ; ou témoin contre honnête non interprétable ou en échec) | **non concluant pour la validité** : rapporté tel quel |")
    # liste d'arrêt (RT-07, RCh-08)
    t = remplacer(
        t,
        "- Un contrôle avant dépense en échec, une offre au-dessus de 1,30 USD de l'heure ou sous 16 cœurs effectifs ou 128 000 Mo de\n"
        "  mémoire vive, un crédit insuffisant, une instance non tolérée sur le compte, un GO autre que GO-2026-10-04-08, une ligne\n"
        "  d'accord de Lazar absente ou d'un autre jour : aucune création.",
        "- Un contrôle avant dépense en échec, une offre au-dessus de 1,30 USD de l'heure, sous 16 cœurs effectifs ou 128 000 Mo de\n"
        "  mémoire vive, au-dessus de 0,05 USD par Go de téléchargement ou de 0,03 USD de l'heure de stockage, un crédit insuffisant,\n"
        "  une instance non tolérée sur le compte, un GO autre que GO-2026-10-04-08, une révocation présente (forme exacte, CH-09),\n"
        "  une ligne d'accord absente, d'un autre jour ou sans sa forme exacte : aucune création.\n"
        "- Contrôle à cinq minutes en échec : arrêt de l'instance par son identifiant (R10), consigné.")
    # chaîne de lancement (brouillon 3 ; RCh-05)
    t = remplacer(t, "Scripts de session, brouillon 2 (`brouillons/P3-chaine-v1-brouillon2/`, quatorze fichiers scellés au commit `03cb538`), versés sous",
                  f"Scripts de session, brouillon 3 (`brouillons/P3-chaine-v1-brouillon3/`, {v['chaine_b3_fichiers']}), versés sous")
    t = remplacer(
        t,
        "Les copies\n"
        "versées ne diffèrent du brouillon 2 que par les épingles des contrôles (candidat, configuration et consignes relus, rapports,\n"
        "code relu, journal de la répétition jouet) et leur ligne H, la borne de téléchargement du lanceur (0.05) et la ligne de session\n"
        "du message de commit du scellement. Ordre :",
        "Les copies\n"
        "versées ne diffèrent du brouillon 3 que par les valeurs « A_EPINGLER » des contrôles (candidat, configuration et consignes\n"
        "relus, rapports, code relu, journal de la répétition jouet). Ordre :")
    # contre-lecture (RT-13, RT-14, RT-06, RC-03)
    t = remplacer(
        t,
        "20 tests, un par\n    garde listée (cas sain et artefact, R5), au commit du code ;",
        "20 tests : 18 pour les\n    16 gardes listées (cas sain et artefact, R5), 2 pour les points que TC-11 disait non testés (mêmes graines d'action ; plan\n"
        "    de la garde d'identité) ;")
    t = remplacer(
        t,
        "test du plafond de l'amorce ajouté (cas sain et\n  artefact, R5).",
        "test du plafond de l'amorce ajouté, renforcé au second\n  commit du code (le script de P3 est tué avant sa propre poussée ; le commit de plafond porte les données légères et les\n"
        "  traces).")
    t = remplacer(
        t,
        "- **Relecture courte du traitement** : `[après la relecture courte : rapport (chemin et empreinte) et son traitement]`.",
        v["paragraphe_relecture_courte"])
    t = remplacer(
        t,
        "**Changements depuis le brouillon 4** (candidat 1) :",
        v["paragraphe_changements_candidat2"] + "\n\n**Changements depuis le brouillon 4** (candidat 1) :")
    for avant, apres in v.get("remplacements_code", []):
        t = remplacer(t, avant, apres)
    assert "[au candidat" not in t and "[après la relecture" not in t
    Path(dst).write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:4])
