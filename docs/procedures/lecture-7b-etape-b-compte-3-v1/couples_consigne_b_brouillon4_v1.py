"""Brouillon 4 de la consigne du lecteur B, écrit par couples « ancien → nouveau » appliqués au brouillon 3 — v1.

Raison unique : appliquer les corrections K1 à K22 de la contre-lecture du brouillon 3, tour 1
(`contre-lecture-consigne-lecteur-b-v1-tour1-v1.md`, 2594d8c63cbcd83615811d927f46aaca1d04f9a9ac6a5aec5fa53e6274d7cc7d,
même dossier), chacune telle que le rapport l'écrit (§ 5) ; mettre à jour le titre et la puce « État du fichier » (version,
heure lue par `date -u` au scellement, passée en argument) ; ajouter la section « Contre-lecture » (rapport, empreinte,
réponse point par point). Rien d'autre ne change. Ne sont pas appliqués : l'option O1, O2 (option de la session mère) et les
remarques facultatives du rapport ; les points du rapport laissés à la session mère (§ 7) ne sont pas tranchés.

Usage : python3 -I -B couples_consigne_b_brouillon4_v1.py --heure AAAA-MM-JJTHH:MM:SSZ
Gardes : heure de la forme `date -u +%Y-%m-%dT%H:%M:%SZ` ; empreinte du brouillon 3 égale à l'attendue ; chaque « ancien »
présent exactement une fois dans le brouillon 3 ; aucun « nouveau » égal à son « ancien » ; aucun recouvrement entre deux
« anciens » ; cible absente (création exclusive : jamais d'écrasement). Tout écart : code 1, rien n'est écrit. Le sceau
(compagnon `.sha256`) est posé ensuite par `controle_ia.scellement sceller`.
"""
import hashlib
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "consigne-lecteur-b-v1-brouillon3.md"
EMPREINTE_SOURCE = "12881d63d3cc5056b1246a3816da5d4a67d28970178085eca8c21d9bdd9cce85"
CIBLE = ICI / "consigne-lecteur-b-v1-brouillon4.md"
FORME_HEURE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

ETAT_ANCIEN = (
    "- **État du fichier** : brouillon 3, écrit le 2026-11-16 par un second rédacteur, sous-agent neuf (modèle A) de la session\n"
    "  mère, qui n'a écrit ni le texte de T0.7 ni aucune autre pièce de ta liste, et n'a ouvert aucune donnée ni aucun résultat\n"
    "  de 7a, de 7b ou de T0.7 ; **brouillon 3 = brouillon 2**\n"
    "  (`consigne-lecteur-b-v1-brouillon2.md`, `6bcfa40005d8e194249568c98be6f855a39ac46792339bb6049895c892ecf421`, gardé tel\n"
    "  quel, règle R12 ; lui-même brouillon 1 plus neuf retouches, `rapport-redacteur-consigne-b-v1.md`, § 4) **plus les seuls\n"
    "  changements que demande la décision R-2980** : la commande de la phase C passe en version 4 et te remet un quinzième\n"
    "  fichier, `sondes-t07.json`, avec son compagnon (liste fermée et bordereau de 29 lignes ; ce que tu y lis, et à quelle\n"
    "  passe ; mentions « non remis » devenues fausses pour ce fichier) ; changements faits par le programme de couples\n"
    "  « ancien → nouveau » `couples_consigne_b_brouillon3_v2.py` (même dossier). **Non contre-lu, non scellé comme consigne**\n"
    "  (son compagnon n'atteste que l'intégrité, règle R6). À contre-lire (règle R2) par un sous-agent neuf qui n'en a écrit\n"
    "  aucun brouillon (son modèle est fixé par la session mère : brouillons 1 et 2 d'un rédacteur du modèle B, changements du\n"
    "  brouillon 3 d'un rédacteur du modèle A), puis à sceller par la session mère sous son nom définitif. Cette puce est\n"
    "  réécrite au scellement.\n")

ETAT_NOUVEAU = (
    "- **État du fichier** : brouillon 4, écrit le 2026-11-16 (heure du scellement, `date -u` : {heure}) par un troisième\n"
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

FIN_ANCIEN = "commentaire : ce que tu sais du verdict reste dans `verdict-ferme/`.\n"

SECTION_CONTRE_LECTURE = (
    "\n"
    "## Contre-lecture (historique pour la session mère ; n'ajoute rien à ta consigne)\n"
    "\n"
    "Cette section ne t'ajoute aucune règle, aucun critère ni aucun geste : pour toi, les sections 0 à 14 font foi. Elle dit\n"
    "d'où viennent les changements du brouillon 4.\n"
    "\n"
    "- **Rapport** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/contre-lecture-consigne-lecteur-b-v1-tour1-v1.md`\n"
    "  (`2594d8c63cbcd83615811d927f46aaca1d04f9a9ac6a5aec5fa53e6274d7cc7d`), tour 1, par un sous-agent neuf (modèle C), sur le\n"
    "  brouillon 3 ; verdict « corrections » : une majeure (K1), vingt et une mineures dont une facultative (K22), plus une\n"
    "  option de procédure laissée à la session mère (O1, O2). Il juge au § 4 la lecture à blanc du brouillon 3\n"
    "  (`docs/procedures/lecture-7b-etape-b-compte-3-v1/lecture-a-blanc-consigne-lecteur-b-brouillon3-v1.md`,\n"
    "  `4b4e9af99696e93e1e4079a9e6c54b8b2ee638b8dd92d5589978638a89567841`) point par point.\n"
    "- **Réponse point par point** (chaque correction appliquée telle que le rapport l'écrit, § 5) :\n"
    "\n"
    "| point du rapport | réponse | où |\n"
    "|---|---|---|\n"
    "| K1 (majeure) : heure de fin | appliqué | 6.10 |\n"
    "| K2 : code `critere-inapplicable` sans clause de jugement | appliqué | 13 |\n"
    "| K3 : aucun texte libre après le code d'arrêt | appliqué | 14 |\n"
    "| K4 : § 2.1 de AUD borné (l. 122-191) | appliqué | 2, pièce 9 |\n"
    "| K5 : les dix clés de l'étape B nommées | appliqué | 6.3, point 2 |\n"
    "| K6 : clé d'une ligne par égalité exacte | appliqué | 6.3, point 2 |\n"
    "| K7 : noms d'abord, empreintes ensuite ; un code par cas | appliqué | 6.1 |\n"
    "| K8 : scripts qui ouvrent les textes en entier | appliqué | 2 |\n"
    "| K9 : lecture de tes propres fichiers de `<ESPACE>/verdict-ferme/` | appliqué | 1 |\n"
    "| K10 : scripts et empreinte du verdict | appliqué | 6 |\n"
    "| K11 : clés de la première passe restreintes | appliqué | 6.5 |\n"
    "| K12 : journal des ouvertures lu après tes dérivations | appliqué | 6.3, point 6 |\n"
    "| K13 : motif de Q « illisible » vérifié par le fait qu'il décrit | appliqué | 6.5, point 4 |\n"
    "| K14 : préfixe `<n>:` des trois sections de l'extrait | appliqué | 5, pièce 2 |\n"
    "| K15 : ensembles balayés par deux déclencheurs de la ligne R9 | appliqué | 7, point 1 |\n"
    "| K16 : lecture prudente de T08A l. 139 recopiée | appliqué | 6.9 |\n"
    "| K17 à K19 : état de BA-L2 lu par chaînes fixes | appliqués ; la forme de la ligne dédiée reste à la session mère (rapport, § 7, point 1) | 6.9 |\n"
    "| K20, K21 : marque « choix de cette consigne » | appliqués | 6.4, points 2 et 4 |\n"
    "| K22 (facultative) : « trop beau » | appliqué : la mention « sens prudent » était inexacte (la lecture large ne déclenche que si l'étroite le fait) ; aucune ligne ni issue ne change | 7, point 2 |\n"
    "| O1, O2 : verdict assemblé par programme | non appliqués : option laissée à la session mère (rapport, § 7, point 4) | aucun |\n"
    "| remarques facultatives (copie du message par un script ; préfixes « ligne », « réserve », « règle » ; code `contradiction-consigne-texte`) | non appliquées : non exigées | aucun |\n"
    "| points pour la session mère (rapport, § 7) | non tranchés ici | aucun |\n"
    "\n"
    "- **Contrôle des renvois** rejoué sur ce brouillon : sortie `verification-renvois-consigne-b-sortie-v4.txt` (même\n"
    "  dossier), code 0 exigé.\n")

COUPLES = [
    ("titre",
     "# T0.7 — consigne du lecteur du verdict de l'étape B (sondes v0, critère 3 de G0, mode « coût ») — v1 — brouillon 3\n",
     "# T0.7 — consigne du lecteur du verdict de l'étape B (sondes v0, critère 3 de G0, mode « coût ») — v1 — brouillon 4\n"),

    ("etat-du-fichier", ETAT_ANCIEN, ETAT_NOUVEAU),

    # K1 (majeure, 6.10)
    ("K1",
     "seule fois. Heure de fin par `date -u`. Puis ton rapport final (section 14).",
     "seule fois. L'heure de fin s'écrit dans l'en-tête du verdict (section 12, point 2) : tu la lis par `date -u` juste avant\n"
     "d'écrire la version achevée du verdict en prose, jamais après le fichier d'issue (règle R12 : le verdict n'est plus retouché).\n"
     "Puis ton rapport final (section 14)."),

    # K2 (13)
    ("K2",
     ", ligne mécanique hors des lignes L, condition d'une ligne que tes pièces ne permettent pas de juger et dont la ligne "
     "dépend (G et A, que tu prends du module comme la section 6.5 le dit, ne sont pas ce cas)",
     ", ligne mécanique hors des lignes L (G et A, que tu prends du module comme la section 6.5 le dit, ne sont pas ce cas ; "
     "une condition que tes pièces ne permettent pas de juger s'écrit « non vérifiable depuis mes pièces » et, si la ligne en "
     "dépend, l'arrêt est `autre`)"),

    # K3 (14)
    ("K3",
     "`<code>` est l'un des neuf codes de la section 13, seul. Deux exceptions : `refus` est suivi d'un tiret et du texte du\n"
     "refus, tel quel, **sauf** si ce texte cite un nombre, une issue ou le contenu d'une pièce : alors la ligne porte\n"
     "`arret refus` seul et le texte entier du refus va au fichier d'arrêt ; `autre` est suivi d'un tiret et d'un motif d'une\n"
     "ligne, sans nombre ni issue.",
     "`<code>` est l'un des neuf codes de la section 13, seul, sans aucun texte après lui : pour `refus` et pour `autre` aussi, la\n"
     "ligne `STATUT` porte `arret refus` ou `arret autre` seul ; le texte entier du refus, ou le motif de `autre`, va au fichier\n"
     "d'arrêt."),

    # K4 (2, pièce 9)
    ("K4", "§ 2.1 (à partir de l. 122)", "§ 2.1 (l. 122-191)"),

    # K5 (6.3, point 2)
    ("K5",
     "`SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `ISSUE-MOTS-ET-COUT-T06` (clés de l'étape B : R109, l. 2174-2178 ; G1 : R169),",
     "`SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `ISSUE-MOTS-ET-COUT-T06` (clés de l'étape B : R109, l. 2174-2178 ; G1 : R169 ; ces dix\n"
     "   clés, de `SCELLEMENT-T07` à `ISSUE-MOTS-ET-COUT-T06` dans l'ordre écrit ici, sont « les dix clés de l'étape B » du point 5 ;\n"
     "   `SCELLEMENT-T07` est permise, non exigée, à l'étape B),"),

    # K6 (6.3, point 2)
    ("K6",
     "`LECTURE-T08-BASE-A` (R110) et `SCELLEMENT-T08-BASE-A`. Absente ou en double : arrêt `piece-non-conforme`.",
     "`LECTURE-T08-BASE-A` (R110) et `SCELLEMENT-T08-BASE-A`. Absente ou en double : arrêt `piece-non-conforme`. La clé d'une\n"
     "   ligne est son premier champ entre barres (après le préfixe `<n>:` de l'extrait), comparé par égalité exacte, jamais par\n"
     "   recherche d'une sous-chaîne (`AUDIT-FUITES-T07` est une sous-chaîne de `CONSIGNE-AUDIT-FUITES-T07`)."),

    # K7 (6.1)
    ("K7",
     "Écart : arrêt `piece-non-conforme` ou `fichier-interdit-recu`.",
     "Ordre : (1) les noms sous `<ESPACE>/pieces/`, comparés aux chemins du bordereau et à la liste fermée, sans ouvrir aucun\n"
     "fichier ; (2) seulement ensuite, les empreintes. Un nom hors du bordereau ou de la liste fermée : arrêt\n"
     "`fichier-interdit-recu` (le fichier n'est pas ouvert) ; un fichier du bordereau manquant, une empreinte, un compagnon ou une\n"
     "citation différents : arrêt `piece-non-conforme`."),

    # K8 (2)
    ("K8",
     "**Comment lire le texte scellé** : par plages de lignes (numéros de la section 3), jamais en entier d'un seul geste. Une",
     "**Comment lire le texte scellé** : par plages de lignes (numéros de la section 3), jamais en entier d'un seul geste (les\n"
     "scripts de contrôle des sections 6.1 et 6.5 ouvrent les fichiers en entier et n'en affichent que les plages et les écarts). Une"),

    # K9 (1)
    ("K9",
     "ni aucun autre fichier ou dossier que `<ESPACE>/pieces/`, le",
     "ni aucun autre fichier ou dossier que `<ESPACE>/pieces/`, les fichiers que tu as toi-même écrits dans `<ESPACE>/verdict-ferme/`, le"),

    # K10 (6)
    ("K10",
     "ils ne lisent que tes pièces et n'écrivent que leur sortie,",
     "ils ne lisent que tes pièces (et, pour l'empreinte du verdict, ce verdict) et n'écrivent que leur sortie,"),

    # K11 (6.5)
    ("K11",
     "`resultat.entrees`, `p3bis`, `table_A`, `doses`, `fuites`, `bases`, `scores_ouverts`, `scores_ii_ouverts`,",
     "`resultat.entrees` (sous-clés `G`, `P`, `A`, `Q` et `F` seules), `p3bis`, `table_A`, `doses` (hors `etat_ii_par_dose_jugee` et\n"
     "`ecart_a_la_base`), `fuites`, `bases`, `scores_ouverts`, `scores_ii_ouverts`,"),

    # K12 (6.3, point 6)
    ("K12",
     "6. Journal : une seule ligne `OUVERTURE-T07 … etape-B/…` ;",
     "6. Journal (le script « controles » n'affiche de la ligne `scores-t07/…` que sa clé, sa date et son chemin ; ce qui suit\n"
     "   « (Q = » n'est lu qu'en 6.5, point 6, après tes dérivations) : une seule ligne `OUVERTURE-T07 … etape-B/…` ;"),

    # K13 (6.5, point 4)
    ("K13",
     "et tu vérifies ce motif sur la pièce 12 si tu le peux ; motif introuvable dans la",
     "et tu vérifies sur la pièce 12, si tu le peux, que le fait que ce motif décrit (clé absente, dose manquante, valeur hors\n"
     "   domaine, `null` interdit) est exact (le motif est un message du module, non une chaîne de la pièce) ; fait décrit non retrouvé dans la"),

    # K14 (5)
    ("K14",
     "(toutes les lignes du registre, chacune précédée de son numéro, `<n>:| CLÉ | date |",
     "(toutes les lignes du registre, chacune précédée de son numéro ; les lignes des trois sections portent le même préfixe `<n>:`, `<n>:| CLÉ | date |"),

    # K15 (7, point 1)
    ("K15",
     "de son plancher. Sous une ligne où aucun score n'est ouvert, tu écris que rien n'est à juger.",
     "de son plancher. Les balayages « aire hors de [0,05 ; 0,95] » et « quantile 0,95 d'un plancher au-dessus de 0,70 » portent sur\n"
     "   toute lecture écrite qui porte une aire contre un plancher : `jeux`, `jeux_hors_jugement`, et les lectures de validité T7-P3,\n"
     "   T7-P4, T7-P6, T7-P9, T7-P15 et T7-P18 ; jamais `couples_figes_descriptif` ni `planchers_p3_descriptif` (lecture de cette\n"
     "   consigne : l'ensemble que le module balaie, le texte ne le bornant pas). Sous une ligne où aucun score n'est ouvert, tu écris que rien n'est à juger."),

    # K16 (6.9 ; A6)
    ("K16",
     "jamais de ta main qu'un texte « ne porte rien » ni qu'un organisme « est flagrant » ; tu recopies.",
     "jamais de ta main qu'un texte « ne porte rien » ni qu'un organisme « est flagrant » ; tu recopies. Dans tous les cas (BA-L2\n"
     "qui s'applique ou non), tu recopies une fois, à la section « Verdict », la phrase « Lecture prudente » de T08A l. 139 (R143), à\n"
     "l'octet et entre guillemets (les mots « ne porte rien » et « flagrant » y sont une citation, non ton propos), et tu écris\n"
     "« (lecture prudente de T08A l. 139) » après toute phrase de ton verdict sur le critère 3 (lecture de cette consigne, sens\n"
     "prudent : une réserve gelée de plus, qui ne change ni ligne ni issue)."),

    # K17 (6.9)
    ("K17",
     "- la ligne dit que BA-L2 **ne s'applique pas** : tu l'écris une fois, à la section « Verdict » ;",
     "- la ligne contient la chaîne « ne s'applique pas » (recherche de chaîne ; forme que la session mère fixe en écrivant la ligne\n"
     "  dédiée) : BA-L2 **ne s'applique pas** : tu l'écris une fois, à la section « Verdict » ;"),

    # K18 (6.9)
    ("K18",
     "- la ligne dit que BA-L2 **s'applique** et porte le mot de Lazar : la réserve R-BA1 accompagne chaque phrase de ton",
     "- la ligne dit que BA-L2 **s'applique** et porte le mot de Lazar (elle contient la chaîne « mot de Lazar », et non « ne\n"
     "  s'applique pas ») : la réserve R-BA1 accompagne chaque phrase de ton"),

    # K19 (6.9)
    ("K19",
     "- la ligne dit que BA-L2 s'applique **sans** mot de Lazar, ou ne dit pas l'état : arrêt `ecart-au-texte` (R110, R191).",
     "- la ligne dit que BA-L2 s'applique **sans** mot de Lazar, ou ne contient aucune des deux chaînes : arrêt `ecart-au-texte` (R110, R191)."),

    # K20 (6.4, point 2)
    ("K20",
     "Toute autre inégalité est écrite clé par clé et laissée en question.",
     "Toute autre inégalité est écrite clé par clé et laissée en question (choix de cette consigne, pour ce point : le texte ne\n"
     "   fait pas de l'égalité de la configuration et du manifeste un point de sa liste d'arrêt)."),

    # K21 (6.4, point 4)
    ("K21",
     "Écart : écrit ; s'il touche une clé de l'étape B : arrêt `ecart-au-texte`.",
     "Écart : écrit ; s'il touche une clé de l'étape B : arrêt `ecart-au-texte` (choix de cette consigne)."),

    # K22 (facultative, 7, point 2)
    ("K22",
     "(lecture de cette consigne, sens prudent ; une réserve ne change pas la ligne).",
     "(lecture de cette consigne : l'une ou l'autre lecture suffit, la large ne pouvant déclencher que si l'étroite le fait ; une réserve ne change pas la ligne)."),

    # Section « Contre-lecture », ajoutée à la fin
    ("contre-lecture", FIN_ANCIEN, FIN_ANCIEN + SECTION_CONTRE_LECTURE),
]


def main(argv) -> int:
    if len(argv) != 3 or argv[1] != "--heure" or not FORME_HEURE.match(argv[2]):
        print("usage : python3 -I -B couples_consigne_b_brouillon4_v1.py --heure AAAA-MM-JJTHH:MM:SSZ (lue par date -u)")
        return 2
    heure = argv[2]
    if CIBLE.exists():
        print(f"ARRÊT : {CIBLE.name} existe déjà : rien n'est écrit (règle R12)")
        return 1
    octets = SOURCE.read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != EMPREINTE_SOURCE:
        print(f"ARRÊT : empreinte de {SOURCE.name} = {h}, attendue {EMPREINTE_SOURCE} : rien n'est écrit")
        return 1
    texte = octets.decode("utf-8")
    places, fautes = [], 0
    for nom, ancien, nouveau in COUPLES:
        nouveau = nouveau.replace("{heure}", heure)
        n = texte.count(ancien)
        if n != 1:
            print(f"FAUTE : couple {nom} : « ancien » présent {n} fois (une attendue)")
            fautes += 1
            continue
        if ancien == nouveau:
            print(f"FAUTE : couple {nom} : « nouveau » égal à « ancien »")
            fautes += 1
            continue
        debut = texte.index(ancien)
        places.append((debut, debut + len(ancien), nom, nouveau))
    places.sort()
    for (a1, b1, n1, _), (a2, b2, n2, _) in zip(places, places[1:]):
        if a2 < b1:
            print(f"FAUTE : couples {n1} et {n2} : « anciens » qui se recouvrent")
            fautes += 1
    if fautes:
        print(f"ARRÊT : {fautes} faute(s) : rien n'est écrit")
        return 1
    morceaux, curseur = [], 0
    for debut, fin, _, nouveau in places:
        morceaux.append(texte[curseur:debut])
        morceaux.append(nouveau)
        curseur = fin
    morceaux.append(texte[curseur:])
    sortie = "".join(morceaux)
    with open(CIBLE, "x", encoding="utf-8", newline="\n") as f:          # création exclusive : jamais d'écrasement
        f.write(sortie)
    hc = hashlib.sha256(CIBLE.read_bytes()).hexdigest()
    print(f"source : {SOURCE.name} ({h}) ; {len(COUPLES)} couples appliqués, chacun à un seul endroit, sans recouvrement ; heure {heure}")
    for debut, fin, nom, nouveau in places:
        ligne = texte.count("\n", 0, debut) + 1
        print(f"  {nom} : ligne {ligne} du brouillon 3 ; {texte.count(chr(10), debut, fin)} → {nouveau.count(chr(10))} sauts de ligne")
    print(f"cible écrite : {CIBLE.name} ; {sortie.count(chr(10))} lignes ; {len(sortie.encode('utf-8'))} octets ; sha256 {hc}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
