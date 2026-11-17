"""Conception v6 -> v7 : couples « ancien -> nouveau » de la contre-lecture v5, tour 2 (C-1, en trois couples ; C-2 ; C-3),
en-tête et section « Contre-lecture (v7 …) ». Vérifie l'empreinte de la v6 et du rapport, que chaque « ancien » figure exactement
une fois dans la v6 et dans le texte courant au moment où il s'applique, et refuse d'écraser la cible (ouverture en mode « x »).

Usage : python appliquer_corrections_v7_v1.py HEURE_UTC   (heure lue par `date -u` juste avant le passage et le scellement)
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ICI / "conception-monde-riche-doublons-v6.md"
SHA_SOURCE = "59bdeff4ad5914ebeed8751ae645134f04ed57a15e9ff2178c9f13d183d8cdde"
RAPPORT = ICI / "contre-lecture-conception-v5-tour2-v1.md"
SHA_RAPPORT = "3ea95e1cfb65d40d82b8cbb60146f6bb7a80d6a17dbfbc2055540ae5c717b466"
CIBLE = ICI / "conception-monde-riche-doublons-v7.md"
DEBUT_V7 = "2026-11-17 01:16:23"

# Textes « nouveau » des corrections, recopiés du rapport caractère pour caractère.
C1A_ANCIEN = "- **Rédacteur de la v6** : modèle C, sous-agent neuf d'un script d'orchestration ; je n'ai écrit ni la v4, ni la v5, ni"
C1A_NOUVEAU = ("- **Rédacteur de la v6** : modèle A (même lignée que le rédacteur de la v5), sous-agent neuf d'un script d'orchestration ;"
               " je n'ai écrit ni la v4, ni la v5, ni")
C1B_ANCIEN = "Rédacteur de la v6 : modèle C, neuf, qui n'a écrit ni la v5 ni son rapport."
C1B_NOUVEAU = "Rédacteur de la v6 : modèle A (même lignée que le rédacteur de la v5), neuf, qui n'a écrit ni la v5 ni son rapport."
C1C_ANCIEN = "la condition de lignée posée au §7 (réserve « Lignée ») est remplie pour la v5."
C1C_NOUVEAU = ("la condition de lignée posée au §7 (réserve « Lignée ») est remplie pour la v5 ; pour la v6, elle exige un lecteur d'une"
               " autre lignée que le modèle A du rédacteur de la v6.")
C2_ANCIEN = "et l'égalité des flux entre passes."
C2_NOUVEAU = ("et l'égalité des flux entre passes (la passe 0,25 « sans masquage » exceptée tant que le module neuf n'a pas séparé la"
              " graine du drapeau de masquage, voir « Passes rapportées » ; un écart de flux sur une autre passe est une anomalie).")
C3_ANCIEN = "Ces essais sont du **code**, non de la conception : ils ne sont pas faits ici."
C3_NOUVEAU = ("Ces essais sont du **code**, non de la conception : ils ne sont pas faits ici. S'y ajoute, exigé par la correction m-1"
              " de la contre-lecture v5, un essai R5-8 : cas sain, le flux de proposition de la passe 0,25 « sans masquage » est égal"
              " à celui des autres passes sur les 12 graines de développement et les passes à masquage vrai restent égales à la v4"
              " (R5-7) ; artefact, la graine rendue dépendante du drapeau : écart de flux détecté.")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def couples(heure):
    section = f"""
## Contre-lecture (v7 : réponse à la contre-lecture de la v5, tour 2)

- **Rapport** : `contre-lecture-conception-v5-tour2-v1.md`, `{SHA_RAPPORT}` (égale à son
  compagnon) ; lecteur neuf (modèle C), qui n'a écrit aucune des pièces ; il a lu la v6 entière et ses deux différentiels.
- **Verdict du rapport** : « Corrections » ; **aucune majeure, trois mineures (C-1 à C-3)** ; les six couples du tour 1 jugés
  appliqués fidèlement, le différentiel v5 → v6 refait et trouvé identique, aucun chiffre changé ; trois remarques facultatives ;
  quatre points pour la mère.
- **Pièce de départ** : v6, `{SHA_SOURCE}` (égale à son compagnon). Le brief de la tâche l'appelle « conception v5 » ; la pièce
  neuve prend le numéro de fichier suivant, v7 (R12).
- **Méthode** : programme `outils-v7/appliquer_corrections_v7_v1.py` (empreinte dans son compagnon `.sha256`, scellé avant son
  passage) : il vérifie l'empreinte de la v6 et du rapport, que chaque « ancien » figure exactement une fois dans la v6 et dans
  le texte courant au moment où il s'applique, et refuse d'écraser la cible. Différentiel `differentiel-conception-v6-v7.diff`
  (`diff -u`, compagnon `.sha256`). Les textes « nouveau » de C-1 à C-3 sont ceux du rapport, recopiés caractère pour caractère.
- **Contrôles faits avant d'appliquer** (lecture seule) : chaque « ancien » du rapport figure une fois dans la v6 ; dans `course`
  de `monde_riche_v4.py` (`4b165847…`), les graines du flux de proposition (ligne 212), du juge (ligne 231) et du test de mort
  (ligne 237) portent bien le drapeau `masquage` : C-2 et C-3 reposent sur un fait exact.

| point | réponse | où | ancien (v6) → nouveau (v7) |
|---|---|---|---|
| **C-1** : lettre « modèle C » donnée au rédacteur de la v6 | **appliquée** (trois couples), **sous réserve de la mère** | en-tête, « Rédacteur de la v6 » ; section « Contre-lecture (v6 …) », points « Rapport » et « Méthode » | « modèle C » → « modèle A (même lignée que le rédacteur de la v5) » (deux fois) ; « est remplie pour la v5. » → « est remplie pour la v5 ; pour la v6, elle exige un lecteur d'une autre lignée que le modèle A du rédacteur de la v6. ». Fondement : le brief dit que les corrections sont écrites par le modèle A ; le même brief dit à leur rédacteur « tu es du modèle C », et c'est cette lettre que la v6 a recopiée. Je reçois ce même brief contradictoire et je suis une instance du modèle auquel la table de m-3 (section « Contre-lecture (v6 …) ») donne la lettre A ; il est donc **probable, non établi par une pièce**, que le rédacteur de la v6 soit lui aussi A. La mère confirme (point 1 du rapport) ; si c'était un modèle C, les trois couples se défont dans une version neuve et le tour 2 n'était pas d'une autre lignée |
| **C-2** : l'audit de symétrie lit « l'égalité des flux entre passes » sans l'exception de m-1 | **appliquée** | §3.2, « Audit de symétrie » | « et l'égalité des flux entre passes. » → la même phrase, suivie de : la passe 0,25 « sans masquage » exceptée tant que le module neuf n'a pas séparé la graine du drapeau de masquage ; un écart de flux sur une autre passe est une anomalie |
| **C-3** : séparation de la graine « à essayer (R5) » sans essai qui la porte | **appliquée** | §2.4, phrase qui suit la table R5-1 à R5-7 | ajout d'un essai **R5-8** (cas sain : flux de la passe 0,25 égal à celui des autres passes sur les 12 graines de développement, passes à masquage vrai égales à la v4 ; artefact : graine rendue dépendante du drapeau, écart détecté). La table R5-1 à R5-7 elle-même n'est pas touchée : le rapport place R5-8 dans la phrase qui la suit |
| remarques facultatives (« cette v5 » au §7 ; remarques du tour 1 ; « Je n'ai écrit ni la v4… » dans la ligne « Rédacteur ») | **non appliquées** | — | non exigées ; la tâche borne la v7 aux corrections exigées |
| points pour la mère (qui a écrit la v6 ; M-1 ouverte ; noms de modèles cités du verdict et des GO ; risques de la règle) | **non tranchés ici** | — | ils relèvent de la mère et de Lazar, non d'une correction ; le point 1 est la réserve de C-1 ci-dessus |
| en-tête | mis à jour | titre, « Statut », « Rédacteur de la v7 », « Heures » | version v6 → v7 ; heures de la v7 par `date -u` |

**Rien d'autre ne change** : aucun chiffre de la v6 n'est modifié ; la section « Contre-lecture (v6 …) » reste en place, avec les
seuls couples de C-1 qui la visent ; les suggestions S-1 à S-6 de la contre-lecture v4 restent non appliquées. **Reste à faire** :
les couples appliqués sont à revoir par un lecteur neuf (tour 3), qui ne soit ni le rédacteur de la v7 ni celui du rapport, et
d'une autre lignée que le modèle A ; la lettre du rédacteur de la v6 (C-1), la lecture de « code v68 gelé » (M-1) et les noms
cités du verdict (m-3, suite) attendent la mère.
"""
    fin_v6 = ("la v6 ni celui du rapport ; la lecture de « code v68 gelé » (M-1) et les noms cités du verdict (m-3, suite) attendent"
              " la mère.\n")
    return [
        ("titre",
         "— v6 (famille MR-2, corrections des contre-lectures v4 et v5, règle de garde opératoire)",
         "— v7 (famille MR-2, corrections des contre-lectures v4 et v5, tours 1 et 2, règle de garde opératoire)"),
        ("en-tête, statut",
         "- **Statut** : conception **v6** (aucun préenregistrement, aucun GO consommé, aucune dépense). Elle est la v5",
         "- **Statut** : conception **v7** (aucun préenregistrement, aucun GO consommé, aucune dépense). Elle est la v6\n"
         f"  (`conception-monde-riche-doublons-v6.md`, `{SHA_SOURCE}`, versée inchangée,\n"
         "  R12) avec les seules corrections exigées par la contre-lecture de la v5, tour 2 (C-1 à C-3 ; section « Contre-lecture\n"
         "  (v7 …) », en fin de pièce), et l'en-tête mis à jour. La v6 était la v5"),
        ("C-1 (a)", C1A_ANCIEN, C1A_NOUVEAU),
        ("en-tête, rédacteur de la v7",
         "- **Interpréteur** : Python 3.13.18",
         "- **Rédacteur de la v7** : modèle A, sous-agent neuf d'un script d'orchestration (la consigne de la tâche me nomme\n"
         "  « modèle C » ; A est la lettre que la table de m-3 donne au modèle dont je suis une instance, écrite ici pour ne pas\n"
         "  refaire le défaut de C-1) ; je n'ai écrit ni la v4, ni la v5, ni la v6, ni leurs contre-lectures ; j'ai appliqué les\n"
         "  couples de la contre-lecture v5, tour 2, par un programme (section « Contre-lecture (v7 …) »), sous l'interpréteur du\n"
         "  venv du dépôt ; aucun calcul neuf, aucun chiffre neuf.\n"
         "- **Interpréteur** : Python 3.13.18"),
        ("en-tête, heures",
         "scellement\n  2026-11-17 01:13:01.",
         "scellement\n"
         f"  2026-11-17 01:13:01 (v6). **v7** : début {DEBUT_V7} ; application des couples et scellement {heure}."),
        ("C-3", C3_ANCIEN, C3_NOUVEAU),
        ("C-2", C2_ANCIEN, C2_NOUVEAU),
        ("C-1 (c)", C1C_ANCIEN, C1C_NOUVEAU),
        ("C-1 (b)", C1B_ANCIEN, C1B_NOUVEAU),
        ("section Contre-lecture (v7)", fin_v6, fin_v6 + section),
    ]


def main():
    if len(sys.argv) != 2:
        sys.exit("usage : appliquer_corrections_v7_v1.py HEURE_UTC")
    heure = sys.argv[1]
    if sha(SOURCE) != SHA_SOURCE:
        sys.exit("empreinte de la v6 inattendue : arrêt")
    if sha(RAPPORT) != SHA_RAPPORT:
        sys.exit("empreinte du rapport inattendue : arrêt")
    if CIBLE.exists():
        sys.exit("cible déjà présente : refus d'écraser")
    original = SOURCE.read_text(encoding="utf-8")
    rapport = RAPPORT.read_text(encoding="utf-8")
    for nom, txt in [("C-1 (a) nouveau", C1A_NOUVEAU), ("C-1 (b) nouveau", C1B_NOUVEAU), ("C-1 (c) nouveau", C1C_NOUVEAU),
                     ("C-2 nouveau", C2_NOUVEAU), ("C-3 nouveau", C3_NOUVEAU), ("C-1 (a) ancien", C1A_ANCIEN),
                     ("C-1 (b) ancien", C1B_ANCIEN), ("C-1 (c) ancien", C1C_ANCIEN), ("C-2 ancien", C2_ANCIEN),
                     ("C-3 ancien", C3_ANCIEN)]:
        if f"`{txt}`" not in rapport:
            sys.exit(f"{nom} : texte absent du rapport, entre accents graves : arrêt")
    texte = original
    for nom, ancien, nouveau in couples(heure):
        n0, n1 = original.count(ancien), texte.count(ancien)
        if n0 != 1 or n1 != 1:
            sys.exit(f"couple {nom} : « ancien » trouvé {n0} fois dans la v6, {n1} fois dans le texte courant : arrêt")
        texte = texte.replace(ancien, nouveau, 1)
        print(f"appliqué : {nom}")
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE.name} {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
