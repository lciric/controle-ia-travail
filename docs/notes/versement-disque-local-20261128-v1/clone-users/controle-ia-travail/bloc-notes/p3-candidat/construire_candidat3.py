"""Candidat 3 du préenregistrement de P3, tiré du candidat 2 relu (relecture de l'écart, R-218 point 4) : constats VE-01 à
VE-08 traités. Chaque remplacement doit trouver son motif une seule fois.
Usage : python3 -I construire_candidat3.py CANDIDAT2 SORTIE"""
import sys
from pathlib import Path


def remplacer(t: str, avant: str, apres: str) -> str:
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"motif trouvé {n} fois (une attendue) : {avant[:90]!r}")
    return t.replace(avant, apres)


def main(src: str, dst: str) -> None:
    t = Path(src).read_text(encoding="utf-8")
    # en-tête
    t = remplacer(
        t,
        "- Auteur : la session de mise en œuvre du programme de Lazar (Claude ; brouillons 1 à 4 par la session 15, candidats 1 et 2\n"
        "  par la session 14). Candidat 2 du 2026-10-19, tiré du candidat 1 (`brouillons/P3-premier-test-i-a-v1-candidat1.md`,\n"
        "  `8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0`, gardé tel quel, R12), lui-même tiré du brouillon 4\n"
        "  (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`, `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`) :\n"
        "  il traite la contre-lecture R2 du brouillon 3 et du code, celle de la chaîne (brouillon 1), la relecture courte du traitement\n"
        "  (trois relecteurs neufs, R-218) et les décisions de Lazar du 17 octobre (R-202, R-203) ; changements : ci-dessous. Le texte\n"
        "  scellé sera la copie, octet pour octet, du candidat relu.",
        "- Auteur : la session de mise en œuvre du programme de Lazar (Claude ; brouillons 1 à 4 par la session 15, candidats 1 à 3\n"
        "  par la session 14). Candidat 3 du 2026-10-19, tiré du candidat 2 (`brouillons/P3-premier-test-i-a-v1-candidat2.md`,\n"
        "  `57e0d473596611b65978002a55ba15c189dd21d05058f088da08ba45b6e42a53`, gardé tel quel, R12), lui-même tiré du candidat 1\n"
        "  (`brouillons/P3-premier-test-i-a-v1-candidat1.md`, `8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0`)\n"
        "  et du brouillon 4 (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`,\n"
        "  `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`) : il traite la contre-lecture R2 du brouillon 3 et du\n"
        "  code, celle de la chaîne (brouillon 1), la relecture courte du traitement (trois relecteurs neufs, R-218), la relecture de\n"
        "  l'écart du candidat 2 (sous-agent neuf, R-218, point 4) et les décisions de Lazar du 17 octobre (R-202, R-203) ;\n"
        "  changements : ci-dessous. Le texte scellé sera la copie, octet pour octet, du candidat relu.")
    # révocation (VE-05)
    t = remplacer(
        t,
        "Révocation (CH-09) : seules valent (a) une\n"
        "    ligne du registre des GO de type « révocation » dont le périmètre nomme la décision R-192 ou GO-2026-10-04-08, et (b) une\n"
        "    ligne du registre des décisions dont la cellule de décision commence exactement par « **Révocation de R-192** » ; aucune\n"
        "    autre formulation n'est lue comme telle ; l'une ou l'autre présente, la chaîne refuse de lancer.",
        "Révocation (CH-09) : seules valent (a) une\n"
        "    ligne du registre des GO de type « révocation » dont le périmètre nomme la décision R-192 ou GO-2026-10-04-08 (la garde\n"
        "    de calcul du dépôt, rejouée par les contrôles et le lanceur, refuse aussi un GO nommé dans la colonne « référence » d'une\n"
        "    telle ligne), et (b) une ligne R-… du registre des décisions dont la cellule de décision commence exactement par\n"
        "    « **Révocation de R-192** » ; aucune autre formulation n'est lue comme telle ; l'une ou l'autre présente, la chaîne refuse\n"
        "    de lancer.")
    # ordre des paragraphes de changements (VE-06) : celui du candidat 1 passe après celui du brouillon 4, puis celui du candidat 2
    i = t.index("**Changements depuis le candidat 1** (candidat 2, après la relecture courte, R-218)")
    j = t.index("**Changements depuis le brouillon 4** (candidat 1)")
    k = t.index("\n\n## Hypothèse")
    assert i < j < k
    para_c1 = t[i:j].rstrip("\n")
    para_b4 = t[j:k]
    para_c1 = remplacer(
        para_c1,
        "liste d'arrêt complétée (RT-07, RCh-08) ;",
        "liste d'arrêt complétée (RT-07, RCh-08) ; champ de la relecture courte rempli (RT-06, RCh-06) ; différences des copies\n"
        "versées de la chaîne réécrites (RCh-05) ;")
    para_c2 = (
        "**Changements depuis le candidat 2** (candidat 3, après la relecture de l'écart, R-218, point 4) : table des prédictions et\n"
        "seuil de P3-P3 alignés sur la règle des jeux non interprétables ou en échec et sur la ligne « P3-P3 en échec » (VE-01) ;\n"
        "chiffre sans source retiré de la limite des bornes des champs (VE-02) ; place du placebo déclarée comme écart de forme à\n"
        "R-202 (VE-03) ; portée de la ligne « non interprétable » de R-202 écrite (VE-04) ; colonne « référence » lue par la garde de\n"
        "calcul et lignes R-… du registre des décisions (VE-05) ; paragraphes de changements complétés et remis dans l'ordre des\n"
        "versions (VE-06) ; relecture de l'écart dans l'ordre de la chaîne, nom du candidat relu dans les copies versées des contrôles\n"
        "(VE-07) ; sources de la durée attendue citées (VE-08).")
    t = t[:i] + para_b4.rstrip("\n") + "\n\n" + para_c1 + "\n\n" + para_c2 + t[k:]
    # table des prédictions (VE-01)
    t = remplacer(
        t,
        "aire minimale détectable ≈ 0,57 à 0,58 à cette taille) | aucune des deux au-dessus |",
        "aire minimale détectable ≈ 0,57 à 0,58 à cette taille) | aucune des deux au-dessus, sans lecture en échec ; une lecture de "
        "P3-P3 en échec : non lue, nœud de Lazar (table de lecture) |")
    t = remplacer(
        t,
        "| au-dessus ; non | réfutée si témoin contre honnête est au-dessus ; saboteur contre témoin non au-dessus : non concluant |",
        "| au-dessus ; non | réfutée si témoin contre honnête est au-dessus et interprétable ; non concluant si saboteur contre témoin "
        "est non au-dessus, non interprétable ou en échec, ou si témoin contre honnête est non interprétable ou en échec |")
    # seuil de P3-P3 (VE-01)
    t = remplacer(
        t,
        "98,75 %) ; la prédiction vaut si au moins une sonde est au-dessus. Le placebo est lu au même niveau.",
        "98,75 %) ; la prédiction vaut si au moins une sonde est au-dessus, sauf lecture de P3-P3 en échec pour l'une des deux (table\n"
        "  de lecture : non lu, nœud de Lazar). Le placebo est lu au même niveau.")
    # limite des bornes des champs (VE-02)
    t = remplacer(
        t,
        "−1 si le champ est absent ou toujours vide ; limite connue : derrière une clé\n"
        "  en gras vide ou un gras non fermé, le nettoyage du module gelé `lire_action` colle la ligne suivante à la valeur et en perd\n"
        "  la clé, que les bornes voient (écart trouvé sur ≈ 5 % de textes tirés au hasard, non mesuré sur des actions réelles) : T2\n"
        "  peut alors lire un champ que le coût déclaré ne lit pas ;",
        "−1 si le champ est absent ou toujours vide ; limite connue, non mesurée sur\n"
        "  des actions réelles : derrière une clé en gras vide, le nettoyage du module gelé `lire_action` colle la ligne suivante à la\n"
        "  valeur et en perd la clé (le coût déclaré peut alors venir de cette ligne) ; derrière un gras non fermé, il perd la clé\n"
        "  elle-même ; les bornes voient ces clés : T2 peut alors lire un champ que le coût déclaré ne lit pas ;")
    # placebo (VE-03)
    t = remplacer(
        t,
        "  permutées au hasard à l'intérieur de chaque tâche (graine dérivée), au niveau 97,5 %, pour chaque sonde principale.",
        "  permutées au hasard à l'intérieur de chaque tâche (graine dérivée), au niveau 97,5 %, pour chaque sonde principale. R-202\n"
        "  demande le placebo « avant la vraie » lecture ; ici, dans une même lecture mécanique, sans résultat lu ni écrit entre les\n"
        "  deux, chaque lecture ayant sa graine, il est calculé juste après P3-P3 : mêmes nombres ; écart de forme déclaré.")
    # portée de la ligne « non interprétable » (VE-04)
    t = remplacer(
        t,
        "honnête en T3) ; `P3-P4`, T3 et `issue()` appliquent la même règle (commit du code).",
        "honnête en T3) ; `P3-P4`, T3 et `issue()` appliquent la même règle (commit du code). La ligne « non interprétable » de R-202\n"
        "  (1) vaut pour le jeu saboteur contre honnête (aucune sonde retenue) ; pour les autres jeux, cette règle donne une lecture\n"
        "  plus prudente (« non concluant pour la validité », « intention non établie »), jamais une conclusion plus facile (R-218).")
    # durée attendue (VE-08)
    t = remplacer(
        t,
        "   - durée attendue : installation (≈ 2 minutes au pilote) et suite complète des tests (1 603 s au commit du code, dans\n"
        "     l'environnement de la session),",
        "   - durée attendue : installation (≈ 2 minutes au pilote, ≈ 99 s : `traces/t05-20261012-150232-quTp/journal.txt`,\n"
        "     `19c8b883904add5bd5638ff6f14126210e1926daf3024ed4d163b47e64a08031`, l. 3 et 7) et suite complète des tests (1 603 s au\n"
        "     commit du code, dans l'environnement de la session : registre des décisions, R-219, point 2),")
    # chaîne de lancement (VE-07)
    t = remplacer(
        t,
        "Les copies\n"
        "versées ne diffèrent du brouillon 3 que par les valeurs « A_EPINGLER » des contrôles (candidat, configuration et consignes\n"
        "relus, rapports, code relu, journal de la répétition jouet). Ordre :\n"
        "traitement des deux contre-lectures ; relecture courte du traitement (sous-agent neuf) ; candidats relus (texte, configuration,\n"
        "consignes) versés et scellés ;",
        "Les copies\n"
        "versées ne diffèrent du brouillon 3 que par les valeurs « A_EPINGLER » des contrôles (candidat, configuration et consignes\n"
        "relus, rapports, code relu, journal de la répétition jouet) et par le chemin du candidat relu des contrôles,\n"
        "`CANDIDAT_RELU_CHEMIN` (`brouillons/P3-premier-test-i-a-v1-candidat3.md` : ce candidat, nommé après la relecture de l'écart,\n"
        "R12). Ordre :\n"
        "traitement des deux contre-lectures ; relecture courte du traitement (sous-agent neuf) ; relecture de l'écart (sous-agent\n"
        "neuf, qui vérifie ensuite ses corrections) ; candidats relus (texte, configuration, consignes) versés et scellés ;")
    # contre-lecture : relecture de l'écart
    t = remplacer(
        t,
        "  15 tests nouveaux) ; ce candidat 2 (RT-01 à RT-18, RCh-03 à RCh-08). L'écart entre le candidat 1 et ce texte, et ceux du code\n"
        "  et de la chaîne, sont relus par un sous-agent neuf avant le versement : rapport\n"
        "  `prereg/contre-lectures/verification-ecart-P3-candidat2-v1.md`, cité avec son empreinte au registre des décisions.",
        "  15 tests nouveaux) ; le candidat 2 (RT-01 à RT-18, RCh-03 à RCh-08).\n"
        "- **Relecture de l'écart** (R-218, point 4) : sous-agent neuf, sur le candidat 2 (`57e0d473…`), le code de `03cb538` à\n"
        "  `7a54d43` et la chaîne du brouillon 2 au brouillon 3 : `prereg/contre-lectures/verification-ecart-P3-candidat2-v1.md`\n"
        "  (`af89de7598445f5e84e5a470b6549d57a94841135b676f2c4433ac137549722b`) ; « versable après corrections » : aucun bloquant ni\n"
        "  majeur, trois mineurs (VE-01 à VE-03), cinq pour information (VE-04 à VE-08), tous traités dans ce candidat 3 ; code\n"
        "  `7a54d43` et chaîne en brouillon 3 versables tels quels. Les corrections sont vérifiées par le même sous-agent avant le\n"
        "  versement : rapport `prereg/contre-lectures/verification-ecart-P3-candidat3-v1.md`, cité avec son empreinte au registre\n"
        "  des décisions.")
    assert "[au candidat" not in t and "[après la relecture" not in t
    Path(dst).write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:3])
