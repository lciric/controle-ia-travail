"""Brouillon 5 de la consigne du lecteur B, écrit par couples « ancien → nouveau » appliqués au brouillon 4 — v1.

Raison unique : appliquer les corrections C1 à C4 de la contre-lecture du brouillon 4, tour 2
(`contre-lecture-consigne-lecteur-b-v1-tour2-v1.md`, a205571e138e1ca3e35737e89831c83f674921457e2a5b23f40ae37e2cea694e,
même dossier), chacune telle que le rapport l'écrit (§ 3) ; mettre à jour le titre et la puce « État du fichier » (version,
heure lue par `date -u` au sceau d'intégrité, passée en argument) ; mettre à jour la section « Contre-lecture » (rapport du
tour 2, empreinte, réponse point par point). Rien d'autre ne change. Ne sont pas appliqués : les remarques facultatives R-b
et R-c du rapport ; les points que le rapport laisse à la session mère (§ 7) ne sont pas tranchés. Le jeton
`EMPREINTE-COMMANDE-V4-A-REMPLIR` reste tel quel.

Usage : python3 -I -B couples_consigne_b_brouillon5_v1.py --heure AAAA-MM-JJTHH:MM:SSZ [--cible CHEMIN]
(`--cible` : pour un essai dans un dossier jetable seulement ; par défaut, `consigne-lecteur-b-v1-brouillon5.md`, même dossier.)
Gardes : heure de la forme `date -u +%Y-%m-%dT%H:%M:%SZ` ; empreinte du brouillon 4 égale à l'attendue ; chaque « ancien »
présent exactement une fois dans le brouillon 4, et encore une seule fois au moment où il est remplacé ; aucun « nouveau »
égal à son « ancien » ; aucun recouvrement entre deux « anciens » ; aucun marqueur `{heure}` restant ; cible absente
(création exclusive : jamais d'écrasement). Tout écart : code 1, rien n'est écrit. Le sceau (compagnon `.sha256`) est posé
ensuite par `controle_ia.scellement sceller`.
"""
import hashlib
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "consigne-lecteur-b-v1-brouillon4.md"
EMPREINTE_SOURCE = "ce397083f351d21fbf72a72b7b1c14a1e5acc6744ac1de762e38f5eb9fe313ab"
CIBLE = ICI / "consigne-lecteur-b-v1-brouillon5.md"
FORME_HEURE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

TITRE_ANCIEN = "mode « coût ») — v1 — brouillon 4\n"
TITRE_NOUVEAU = "mode « coût ») — v1 — brouillon 5\n"

ETAT_ANCIEN = (
    "- **État du fichier** : brouillon 4, écrit le 2026-11-16 (heure du scellement, `date -u` : 2026-11-16T14:17:10Z) par un troisième\n"
    "  rédacteur, sous-agent neuf (modèle C) de la session mère, qui n'a écrit ni le texte de T0.7, ni aucune autre pièce de ta\n"
    "  liste, ni aucun brouillon antérieur de cette consigne, et n'a ouvert aucune donnée ni aucun résultat de 7a, de 7b ou de\n"
    "  T0.7 ; **brouillon 4 = brouillon 3** (`consigne-lecteur-b-v1-brouillon3.md`,\n"
    "  `12881d63d3cc5056b1246a3816da5d4a67d28970178085eca8c21d9bdd9cce85`, gardé tel quel, règle R12 ; lui-même brouillon 2\n"
    "  plus les seuls changements de la décision R-2980, qui te remet `sondes-t07.json`) **plus les corrections K1 à K22 de sa\n"
    "  contre-lecture, tour 1** (réponse point par point : section « Contre-lecture », à la fin) ; changements faits par le\n"
    "  programme de couples « ancien → nouveau » `couples_consigne_b_brouillon4_v1.py` (même dossier). **Non scellé comme\n"
    "  consigne** (son compagnon n'atteste que l'intégrité, règle R6). Contre-lu une fois, sur le brouillon 3 ; à contre-lire\n"
    "  par différentiel (règle R2) par un sous-agent neuf qui n'en a écrit aucun brouillon, puis à sceller par la session mère\n"
    "  sous son nom définitif. Cette puce est réécrite au scellement.\n")

ETAT_NOUVEAU = (
    "- **État du fichier** : brouillon 5, écrit le 2026-11-16 (heure du sceau d'intégrité, `date -u` : {heure}) par un\n"
    "  quatrième rédacteur, sous-agent neuf (modèle C) de la session mère, qui n'a écrit ni le texte de T0.7, ni aucune autre\n"
    "  pièce de ta liste, ni aucun brouillon antérieur de cette consigne, et n'a ouvert aucune donnée ni aucun résultat de 7a,\n"
    "  de 7b ou de T0.7 ; **brouillon 5 = brouillon 4** (`consigne-lecteur-b-v1-brouillon4.md`,\n"
    "  `ce397083f351d21fbf72a72b7b1c14a1e5acc6744ac1de762e38f5eb9fe313ab`, gardé tel quel, règle R12 ; lui-même brouillon 3\n"
    "  plus les corrections K1 à K22 de la contre-lecture, tour 1) **plus les corrections C1 à C4 de sa contre-lecture,\n"
    "  tour 2** (réponse point par point : section « Contre-lecture », à la fin) ; changements faits par le programme de\n"
    "  couples « ancien → nouveau » `couples_consigne_b_brouillon5_v1.py` (même dossier). **Non scellé comme consigne** (son\n"
    "  compagnon n'atteste que l'intégrité, règle R6). Contre-lu deux fois, sur les brouillons 3 et 4 ; à contre-lire par\n"
    "  différentiel (règle R2) par un sous-agent neuf qui n'en a écrit aucun brouillon, puis à sceller par la session mère\n"
    "  sous son nom définitif. Cette puce est réécrite au scellement.\n")

# Corrections du rapport du tour 2 (§ 3), « ancien » et « nouveau » recopiés tels quels.
COUPLES = [
    # C1 (majeure ; 6.3, point 2)
    ("C1",
     "`SCELLEMENT-T07` est permise, non exigée, à l'étape B),",
     "neuf sont exigées par le texte (R109) ; `SCELLEMENT-T07`, que le texte permet à l'étape B sans l'y exiger, est exigée "
     "ici parce que les points 3 et 5 la comparent et que G1 refuse déjà sans elle (T0.7 l. 1725) : choix de cette consigne),"),

    # C2 (mineure ; 12, point 3)
    ("C2",
     "l'état de BA-L2 (section 6.9) ; la phrase de R019.",
     "l'état de BA-L2 et la phrase « Lecture prudente » (section 6.9) ; la phrase de R019."),

    # C3 (mineure ; 6.9)
    ("C3",
     "la phrase « Lecture prudente » de T08A l. 139 (R143), à",
     "la ligne 139 de T08A (R143) entière, intitulé en gras compris, à"),

    # C4 (mineure ; 6.1)
    ("C4",
     "Ordre : (1) les noms sous `<ESPACE>/pieces/`, comparés aux chemins du bordereau et à la liste fermée, sans ouvrir aucun",
     "Ordre : (1) l'empreinte du bordereau et de son compagnon, puis les noms sous `<ESPACE>/pieces/`, comparés aux chemins "
     "du bordereau et à la liste fermée, sans ouvrir aucun autre"),
]

INTRO_ANCIEN = "d'où viennent les changements du brouillon 4.\n"
INTRO_NOUVEAU = (
    "d'où viennent les changements des brouillons 4 et 5.\n"
    "\n"
    "### Tour 1 : brouillon 3, corrections K1 à K22 (brouillon 4)\n")

FIN_ANCIEN = (
    "- **Contrôle des renvois** rejoué sur ce brouillon : sortie `verification-renvois-consigne-b-sortie-v4.txt` (même\n"
    "  dossier), code 0 exigé.\n")

FIN_NOUVEAU = (
    "- **Contrôle des renvois** rejoué sur le brouillon 4 : sortie `verification-renvois-consigne-b-sortie-v4.txt` (même\n"
    "  dossier), code 0.\n"
    "\n"
    "### Tour 2 : brouillon 4, corrections C1 à C4 (brouillon 5)\n"
    "\n"
    "- **Rapport** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/contre-lecture-consigne-lecteur-b-v1-tour2-v1.md`\n"
    "  (`a205571e138e1ca3e35737e89831c83f674921457e2a5b23f40ae37e2cea694e`), tour 2, par un sous-agent neuf (modèle C), sur le\n"
    "  brouillon 4, par différentiel ; verdict « corrections » : une majeure (C1), trois mineures (C2 à C4), quatre remarques\n"
    "  facultatives (R-a à R-d), sept points pour la session mère (§ 7). Il trouve K1 à K22 appliquées fidèlement.\n"
    "- **Réponse point par point** (chaque correction appliquée telle que le rapport l'écrit, § 3 ; chaque « ancien » trouvé une\n"
    "  seule fois) :\n"
    "\n"
    "| point du rapport | réponse | où |\n"
    "|---|---|---|\n"
    "| C1 (majeure) : `SCELLEMENT-T07` exigée ici, que le texte permet sans l'exiger à l'étape B (T0.7 l. 2174-2178, l. 1725) | appliqué ; l'autre lecture (clé permise : « absente » écrite, points 3 et 5 non jugés pour elle) reste à la session mère (rapport, § 7, point 2) | 6.3, point 2 |\n"
    "| C2 : phrase « Lecture prudente » nommée au contenu de la section « Verdict » | appliqué | 12, point 3 |\n"
    "| C3 : ligne 139 de T08A recopiée entière, intitulé compris | appliqué | 6.9 |\n"
    "| C4 : empreinte du bordereau vérifiée avant de l'ouvrir | appliqué | 6.1 |\n"
    "| R-a : « heure du scellement » inexacte dans la puce « État du fichier » | puce réécrite pour ce brouillon (« heure du sceau d'intégrité ») ; sa forme définitive et la lettre du rédacteur restent au sceau (rapport, § 7, points 3 et 4) | en-tête |\n"
    "| R-b : garder ou retirer cette section au sceau | non tranché : choix de la session mère | aucun |\n"
    "| R-c : codes `contradiction-consigne-texte` et `critere-inapplicable` gardés tels quels | rien à changer : remarque sans demande | aucun |\n"
    "| R-d : rejouer le contrôle des renvois après la mise au propre | rejoué sur ce brouillon (ci-dessous) ; à rejouer au sceau, après le remplacement du jeton | aucun |\n"
    "| points pour la session mère (rapport, § 7, points 1 à 7) | non tranchés ici | aucun |\n"
    "\n"
    "- **Lecture à blanc du brouillon 3, jugée de nouveau** (retenu ou non, et pourquoi) : B1 et B3 retenus, corrigés par K1\n"
    "  et K3 (sections 6.10 et 14). B2 non retenu comme correction : le risque de faute de recopie est réel, mais c'est une\n"
    "  option de procédure (O1, O2) laissée à la session mère, sans écart au texte scellé. m1 à m4 retenus (K6 ; K5, complété\n"
    "  par C1 ; K7, complété par C4 ; K8). m5 et m6 non retenus : la copie du message est comparée au message scellé par la\n"
    "  session hôte (une différence arrête, sans repli silencieux) et l'ordre du premier geste est écrit en 6.0. m7 à m9 et\n"
    "  m11 retenus (K9, K11, K12, K14). m10 retenu pour le motif de Q « illisible » (K13), non retenu pour les trois domaines\n"
    "  à ajouter : le texte range tout défaut de forme en Q « illisible » et la consigne ne fait pas refaire la validation du\n"
    "  domaine. m12 retenu (K17 à K19) ; la forme de la ligne dédiée reste à la session mère. m13 retenu (K15, K22). m14 non\n"
    "  retenu : l'en-tête fixe les trois familles de noms, et une règle du programme y porte toujours le mot « règle ». m15 non\n"
    "  retenu : une propreté hors des déclencheurs gelés ne s'écrit qu'en question, sans changer la ligne ; un seuil en ferait\n"
    "  un critère neuf. m16 non retenu dans cette consigne : c'est une garde de la session hôte (bloc C7), point pour la\n"
    "  session mère. m17 : mise au propre au sceau, par la session mère.\n"
    "- **Ambiguïtés A1 à A7 du rapport du rédacteur, jugées** : A1 : lecture fidèle et prudente ; le texte confie R-BA1 à la\n"
    "  session mère (R111) et la consigne le rappelle ; la double marque est admise parce qu'elle ne change ni les doses jugées\n"
    "  ni aucune ligne (R112). A2 : fidèle ; cellule entière, phrase du module en regard, différence écrite sans arrêt (seule\n"
    "  une ligne ou une sous-phrase différente arrête). A3 : bornée par K15 et K22, fidèle à l'ensemble que le module balaie ;\n"
    "  une lecture plus large (les deux tableaux descriptifs balayés aussi, en réserve seulement) serait plus prudente :\n"
    "  remontée à la session mère, non appliquée. A4 : fidèle (R163). A5 : fidèle et prudente, aucun calcul neuf (section 8).\n"
    "  A6 : la ligne 139 de T08A est recopiée une fois, entière (C3), et une marque la rappelle après toute phrase sur le\n"
    "  critère 3 ; la lettre de T08A (« à écrire telle quelle avec toute phrase sur le barreau 3 ») admet aussi sa recopie\n"
    "  entière après chaque phrase : remontée à la session mère, non appliquée. A7 : mécanique, fidèle. Aucune n'est un écart\n"
    "  à un texte scellé qui demande le mot de Lazar.\n"
    "- **Contrôle des renvois** rejoué sur ce brouillon : sortie `verification-renvois-consigne-b-sortie-v5.txt` (même\n"
    "  dossier), code 0 exigé.\n")


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv):
    if len(argv) not in (3, 5) or argv[1] != "--heure" or (len(argv) == 5 and argv[3] != "--cible"):
        print(__doc__.split("\n\n")[2])
        return 2
    heure = argv[2]
    cible = pathlib.Path(argv[4]) if len(argv) == 5 else CIBLE
    if not FORME_HEURE.match(heure):
        print("FAUTE : heure hors de la forme AAAA-MM-JJTHH:MM:SSZ")
        return 1
    if cible.exists():
        print(f"FAUTE : la cible existe déjà, rien n'est écrit : {cible.name}")
        return 1
    if sha(SOURCE) != EMPREINTE_SOURCE:
        print("FAUTE : empreinte du brouillon 4 autre que l'attendue")
        return 1
    texte = SOURCE.read_text(encoding="utf-8")
    tous = [("titre", TITRE_ANCIEN, TITRE_NOUVEAU), ("etat", ETAT_ANCIEN, ETAT_NOUVEAU.replace("{heure}", heure))]
    tous += COUPLES
    tous += [("intro", INTRO_ANCIEN, INTRO_NOUVEAU), ("fin", FIN_ANCIEN, FIN_NOUVEAU)]
    fautes = 0
    places = []
    for nom, ancien, nouveau in tous:
        n = texte.count(ancien)
        if n != 1:
            print(f"FAUTE : {nom} : « ancien » présent {n} fois dans le brouillon 4")
            fautes += 1
            continue
        if ancien == nouveau:
            print(f"FAUTE : {nom} : « nouveau » égal à « ancien »")
            fautes += 1
        debut = texte.index(ancien)
        places.append((debut, debut + len(ancien), nom))
    places.sort()
    for (a1, b1, n1), (a2, b2, n2) in zip(places, places[1:]):
        if a2 < b1:
            print(f"FAUTE : recouvrement entre {n1} et {n2}")
            fautes += 1
    if fautes:
        print(f"{fautes} faute(s) : rien n'est écrit")
        return 1
    neuf = texte
    for nom, ancien, nouveau in tous:
        if nom == "etat":
            nouveau = ETAT_NOUVEAU.replace("{heure}", heure)
        if neuf.count(ancien) != 1:
            print(f"FAUTE : {nom} : « ancien » plus présent une seule fois au moment du remplacement : rien n'est écrit")
            return 1
        neuf = neuf.replace(ancien, nouveau, 1)
        print(f"appliqué : {nom}")
    if "{heure}" in neuf:
        print("FAUTE : marqueur d'heure restant : rien n'est écrit")
        return 1
    with open(cible, "x", encoding="utf-8") as f:
        f.write(neuf)
    print(f"écrit : {cible.name} ; {len(neuf.splitlines())} lignes ; sha256 {sha(cible)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
