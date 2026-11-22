"""Construit la version c5 du brouillon 7 de relance du préenregistrement du papier C, par remplacements exacts sur
la version c4 : décision de la chaîne de décision sur le point H-1 (registres/go.md, GO-2026-11-22-125), trois lignes
rapportées ajoutées à la précision 37, erratum 1 de la version c4 intégré (remarque CY-01 ; devis en brouillon 5).

Usage (depuis la racine du dépôt) :
    python3 registres/papier-c/redaction-brouillon7-relance-v1/travail/construire_brouillon7_relance_c5_v1.py SORTIE JOURNAL

Gardes : source à l'empreinte attendue ; chaque fragment trouvé une fois ; titres de section inchangés ; un seul
« À REMPLIR » dans la section « Contre-lecture », aucun ajouté ni retiré ailleurs ; marqueurs de gabarit : ceux de
la version c4 moins « MOT_DU_DIRECTEUR_H1 », et rien d'autre. Refuse d'écraser une sortie (R12).
"""
import hashlib
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SOURCE = RACINE / "brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c4.md"
EMPREINTE_SOURCE = "51eea9c5d061a5c4f3d838512d69a1b4715530ca84e0cec803dd17e2870fcc99"
DOSSIER = "registres/papier-c/redaction-brouillon7-relance-v1"
VERIF3 = f"{DOSSIER}/contre-lecteur/rapport-verification-c3-et-devis-brouillon3-v1.md"
H_VERIF3 = "265f62e7cfada908e93aa0d1da3e1e7e90583107a04da46b23eab378cfc55b6e"
VERIF4 = f"{DOSSIER}/contre-lecteur/rapport-verification-c4-et-devis-brouillon4-v1.md"
H_VERIF4 = "c530b6df31e9d58f61b67dc2e29751fb89de863d62ba02798d7cdeadc369b45d"
ERRATUM = f"{DOSSIER}/erratum-1-version-c4-brouillon7-relance-v1.md"
H_ERRATUM = "3c6793fb0390655f0fe263960066f71107693782dbf78fc5013ab73794e01580"
MARQUEUR_RETIRE = "<<MOT_DU_DIRECTEUR_H1>>"


def sha(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


assert sha(RACINE / VERIF4) == H_VERIF4
assert sha(RACINE / ERRATUM) == H_ERRATUM
R = []


def remplace(ident, lieu, motif, ancien, nouveau):
    R.append((ident, lieu, motif, ancien, nouveau))


def ajoute(ident, lieu, motif, ancre, ajout):
    R.append((ident, lieu, motif, ancre, ancre + ajout))


remplace(
    "N-01", "titre", "version neuve (R12)",
    "version c4 (contre-lecture et trois vérifications traitées ; décisions D-21, D-23 et D-24 portées) : version r3 "
    "reprise",
    "version c5 (contre-lecture et quatre vérifications traitées ; décisions D-21, D-23 et D-24 portées ; point H-1 "
    "porté d'après la ligne d'accord qui le tranche) : version r3 reprise",
)

remplace(
    "N-02", "en-tête, « État en bref »", "point H-1 : décision de la chaîne, GO-2026-11-22-125",
    "GO-2026-11-19-74) et les décisions D-21, D-23 et D-24 (GO-2026-11-22-123). **Reste avant le scellement**, sans\n"
    "aucune dépense : (1) la vérification, par le même contre-lecteur, des dernières corrections de cette version c4\n"
    "(verrou 7) ;",
    "GO-2026-11-19-74) et les décisions D-21, D-23 et D-24 (GO-2026-11-22-123). **Tranché par la chaîne de\n"
    "décision, non par un mot du directeur, et révisable par lui jusqu'au scellement** : la lecture des deux\n"
    "statistiques de rang de la précision 37 (point H-1 ; GO-2026-11-22-125 ; verrou 1). **Reste avant le\n"
    "scellement**, sans aucune dépense : (1) la vérification, par le même contre-lecteur, de ce que cette version c5\n"
    "écrit de neuf (verrou 7) ;",
)

remplace(
    "N-03", "en-tête, « État en bref »", "le point H-1 ne retient plus le scellement",
    "D-22 de ce rédacteur ; (8) le mot du directeur sur la précision 37, portée comme nœud, sans défaut (point H-1 ;\n"
    "verrou 1). Le bras de la décision D-23",
    "D-22 de ce rédacteur. Le bras de la décision D-23",
)

ajoute(
    "N-04", "en-tête, « Nom (R12) »", "version neuve (R12)",
    "  c3 s'appelle « brouillon7-relance-2026-11-22-c4 ».",
    " La version qui porte la décision de la chaîne\n"
    "  sur le point H-1 et intègre l'erratum 1 de c4 s'appelle « brouillon7-relance-2026-11-22-c5 ».",
)

remplace(
    "N-05", "en-tête, « Historique »", "R12 : la version c4 entre dans l'historique",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, version c3 (2026-11-22) :",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, version c4 (2026-11-22) :\n"
    "  `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c4.md`\n"
    f"  (`{EMPREINTE_SOURCE}`, 268 273 octets), déclarée scellable par le\n"
    "  contre-lecteur (section « Contre-lecture »), lue avec son erratum 1\n"
    f"  (`{ERRATUM}`,\n"
    f"  `{H_ERRATUM}`) ; point de départ de cette version c5 ;\n"
    "- brouillon 7 de relance, version c3 (2026-11-22) :",
)

remplace(
    "N-06", "en-tête, « Historique »", "la version c3 est le point de départ de la version c4",
    "  (section « Contre-lecture ») ; point de départ de cette version c4 ;\n",
    "  (section « Contre-lecture ») ; point de départ de la version c4 ;\n",
)

remplace(
    "N-07", "en-tête, « Ce que change… »", "paragraphe neuf : ce que change la version c5",
    "**Ce que change la version c4 du brouillon 7 de relance** (2026-11-22). Une source : la vérification de la\n",
    "**Ce que change la version c5 du brouillon 7 de relance** (2026-11-22). Trois sources. (1) La décision sur le\n"
    "point H-1 : la lecture des deux statistiques de rang écrite à la précision 37 est gardée ; c'est une décision de\n"
    "la chaîne de décision, non un mot du directeur, révisable par lui jusqu'au scellement (`registres/go.md`,\n"
    "GO-2026-11-22-125) ; le marqueur qui retenait le scellement est remplacé par cette décision (verrou 1 ;\n"
    "précision 37). (2) Trois lignes rapportées, recommandées par les deux juges de cette décision (R-5037) et\n"
    "acceptées par ce rédacteur : le nombre de couples où la destination n'est pas identifiable, écrit sur les lignes\n"
    "C-P3a et C-P3b ; la mention « rangs sans gain mesuré : stabilité non éprouvée » ; les mêmes statistiques de rang\n"
    "sur le gain de la loi séparée, sans verdict (précisions 36 et 37 ; phrase sous le tableau des critères). Aucune\n"
    "ne change une règle, un seuil ni un verdict. (3) La vérification de la version c4 par le même contre-lecteur\n"
    f"(rapport `{VERIF4}`,\n"
    f"`{H_VERIF4}` : avis « scellable » ; une remarque mineure de forme,\n"
    "CY-01), dont l'erratum 1 est intégré (section « Contre-lecture » ; verrou 8 : devis du pilote en brouillon 5).\n"
    f"Table des remplacements : `{DOSSIER}/note-differences-brouillon7-relance-c5-v1.md`. Aucun énoncé d'hypothèse,\n"
    "aucune prédiction, aucune marge, aucun seuil ne change ; aucune revendication n'est ajoutée.\n"
    "\n"
    "**Ce que change la version c4 du brouillon 7 de relance** (2026-11-22). Une source : la vérification de la\n",
)

remplace(
    "N-08", "verrou 1", "liste des points ouverts en version 4",
    "points-ouverts-pour-le-directeur-brouillon7-relance-v3.md`, lue avec son erratum 1) : D-21",
    "points-ouverts-pour-le-directeur-brouillon7-relance-v4.md`) : D-21",
)

remplace(
    "N-09", "verrou 1", "point H-1 : marqueur remplacé par la décision de la chaîne (GO-2026-11-22-125)",
    "La précision 37 (tirages dégénérés et statistiques de\n"
    "   rang), tranchée le 19 novembre sans mot du directeur, est portée comme nœud, sans défaut, à la demande du\n"
    "   contre-lecteur du brouillon 7 de relance (remarque CB-04 ; point H-1) : `" + MARQUEUR_RETIRE + "`.",
    "La précision 37 (tirages dégénérés et statistiques de\n"
    "   rang), tranchée le 19 novembre sans mot du directeur, a été portée comme nœud, sans défaut, à la demande du\n"
    "   contre-lecteur du brouillon 7 de relance (remarque CB-04 ; point H-1). **Elle est tranchée par la chaîne de\n"
    "   décision, non par un mot du directeur** : option (a), les deux statistiques sont toujours lues, la\n"
    "   précision 37 telle qu'écrite (`registres/go.md`, GO-2026-11-22-125, au titre de l'autonomie\n"
    "   GO-2026-11-22-106 : étage 3, deux juges indépendants et concordants, de deux modèles différents, effort\n"
    "   maximal ; R-5037 ; directeur hors ligne). La décision est **révisable par le directeur jusqu'au\n"
    "   scellement** ; la lecture écartée et tout changement de grandeur restent de son ressort. Au scellement, la\n"
    "   conduite écrit ici s'il l'a revue.",
)

remplace(
    "N-10", "verrou 7 (contre-lecture)", "vérification de la version c4 faite ; reste la vérification de c5",
    "**Reste** : la vérification de\n"
    "   ces deux corrections par ce même contre-lecteur.",
    "Vérification de la version c4 faite par ce même contre-lecteur\n"
    f"   (rapport `{H_VERIF4}` : CX-01 et CX-02 levées ; l'ajout du\n"
    "   rédacteur sur la différence de modèle du bras jugé juste et tenable ; avis « scellable » ; une mineure de\n"
    "   forme, CY-01, que cette version c5 intègre). **Reste** : la vérification, par ce même contre-lecteur, de ce\n"
    "   que la version c5 écrit de neuf (décision de la chaîne sur le point H-1 ; trois lignes rapportées de la\n"
    "   précision 37).",
)

remplace(
    "N-11", "verrou 8 (accord de dépense du pilote)", "devis en brouillon 5 (erratum 1 de la version c4)",
    f"   `{DOSSIER}/devis-pilote-papier-C-v1-brouillon4.md`.",
    f"   `{DOSSIER}/devis-pilote-papier-C-v1-brouillon5.md`.",
)

ajoute(
    "N-12", "verrou 10 (grille de la clause de repli)", "la décision sur le point H-1 garde la lecture sous laquelle la grille se joue",
    "    de l'issue qu'il désigne. Aucune conclusion par ligne n'est écrite dans ce texte avant cela.",
    " La décision sur le\n"
    "    point H-1 (GO-2026-11-22-125) garde la lecture sous laquelle ces cases se jouent (précision 37) et rappelle\n"
    "    que la clause se joue sur la liste finie entière avant le scellement.",
)

remplace(
    "N-13", "Plan, section 8, précision 36", "trois lignes rapportées de plus",
    "mention de la réserve 20 (précision 39). S'y ajoute la part des tirages où ĉ s'échappe, écrite à côté de chaque\n"
    "    Ḡ (précision 37).",
    "mention de la réserve 20 (précision 39). S'y ajoutent la part des tirages où ĉ s'échappe, écrite à côté de\n"
    "    chaque Ḡ, et les trois lignes de la fin de la précision 37 (nombre de couples où ĉ n'est pas identifiable ;\n"
    "    mention « rangs sans gain mesuré : stabilité non éprouvée » ; statistiques de rang sur le gain de la loi\n"
    "    séparée).",
)

remplace(
    "N-14", "Plan, section 8, précision 37, « Statut »", "point H-1 : décision de la chaîne ; trois lignes rapportées",
    "Parce qu'elle fixe quand deux prédictions peuvent être « établies », elle est portée au directeur\n"
    "    comme nœud, sans défaut (point H-1) : `" + MARQUEUR_RETIRE + "`. Tant que ce mot manque, le texte ne se scelle\n"
    "    pas. Si le directeur retient la lecture écartée, une version neuve l'écrit, et la grille de la clause de\n"
    "    repli est rejouée sous elle avant le scellement.\n",
    "Parce qu'elle fixe quand deux prédictions peuvent être « établies », elle a été portée au directeur\n"
    "    comme nœud, sans défaut (point H-1). **Décision** : la lecture retenue est gardée telle qu'écrite ci-dessus\n"
    "    (option (a) du point H-1). C'est une décision de la chaîne de décision, non un mot du directeur\n"
    "    (`registres/go.md`, GO-2026-11-22-125, au titre de l'autonomie GO-2026-11-22-106 : étage 3, deux juges\n"
    "    indépendants et concordants, de deux modèles différents, effort maximal ; R-5037), prise pendant que le\n"
    "    directeur était hors ligne. Elle reste **révisable par le directeur jusqu'au scellement** ; la lecture\n"
    "    écartée et tout changement de grandeur restent de son ressort. La réserve de méthode tient : cette lecture\n"
    "    a été écrite après lecture de taux simulés et n'est pas la plus sévère pour l'« établie » de C-P3a et de\n"
    "    C-P3b. Le risque est borné par la clause de repli, jouée sous cette lecture sur la liste finie entière\n"
    "    avant le scellement (verrou 10). Si le directeur retient la lecture écartée, une version neuve l'écrit, et\n"
    "    la grille de la clause de repli est rejouée sous elle avant le scellement.\n"
    "    **Trois lignes rapportées, ajoutées avec cette décision** (recommandations des deux juges, R-5037,\n"
    "    acceptées par le rédacteur de la version c5). Aucune ne change une règle, un seuil ni un verdict ; aucune\n"
    "    n'entre dans une combinaison, dans une correction pour comparaisons multiples ni dans la clause de repli.\n"
    "    (1) **Nombre de couples où ĉ n'est pas identifiable.** Sur les lignes C-P3a et C-P3b, quelle que soit leur\n"
    "    issue, est écrit, par corpus et par lecture, le nombre de couples juge × famille, sur quinze, où ĉ n'est\n"
    "    pas identifiable : ĉ estimé au bord de [−30 ; 40] ou au-delà, ou plus de 1 % de tirages où ĉ en sort\n"
    "    (Métrique, point 11).\n"
    "    (2) **Mention « rangs sans gain mesuré : stabilité non éprouvée ».** Elle est écrite sur les lignes C-P3a\n"
    "    et C-P3b, qu'elles sortent « établie » ou « non établie » (R4), quand aucune famille n'est « positive » ni\n"
    "    « négative » pour aucun des trois juges au sens de C-P2 (section « Seuil » ; corpus A). Elle dit que les\n"
    "    rangs comparés ne portent aucun gain mesuré : une « établie » n'y montre pas que la vulnérabilité des juges\n"
    "    garde son rang, une « non établie » n'y montre pas qu'elle le perd.\n"
    "    (3) **Statistiques de rang sur le gain de la loi séparée.** Pour chaque juge × famille × corpus, Ḡ_sép est\n"
    "    la moyenne, sur les k_f rangs retenus, des g_m de la loi séparée nette (Métrique, point 7, appliqué à Δᵃ_m\n"
    "    sur X, point 8 bis : g_m = −pente, qui ne dépend d'aucune destination ; valeur non finie : précision 5).\n"
    "    Les statistiques de C-P3a et de C-P3b sont recalculées avec Ḡ_sép à la place de Ḡ, mêmes tirages, mêmes\n"
    "    trois lectures, mêmes valeurs p. Elles sont rapportées sans verdict : jamais « établie », jamais citées à\n"
    "    la place d'une ligne de C-P3a ou de C-P3b, quel que soit le sort de ces lignes.\n",
)

ajoute(
    "N-15", "Critères de lecture gelés, sous le tableau de la stabilité de rang", "renvoi aux trois lignes rapportées de la précision 37",
    "calibrée par ρ̂/r̂) : « établie » seulement si les trois concluent ; clause de repli mécanique (bloc P-021, section\n"
    "« Prédiction »).",
    " Sur les lignes C-P3a et C-P3b sont écrits, quelle que soit leur issue, le nombre de couples où ĉ\n"
    "n'est pas identifiable et, s'il y a lieu, la mention « rangs sans gain mesuré : stabilité non éprouvée » ; les\n"
    "mêmes statistiques sur le gain de la loi séparée sont rapportées sans verdict (Plan, section 8, précision 37) ;\n"
    "rien de cela ne change une règle ni un verdict.",
)

remplace(
    "N-16", "section « Contre-lecture »", "erratum 1 de la version c4 intégré (CY-01) ; vérification de la version c4 consignée ; vérification de la version c5 à faire",
    f"`{H_VERIF3}` ; le programme rejoué rend la version c3, aucun changement\n"
    "hors de sa table ; CW-01 à CW-03 levées (pour CW-01 : la lettre de la décision D-21 suivie par le texte est celle\n"
    "de la ligne d'accord, confirmée par la session de conduite) ; rien de ce qui est tranché n'a bougé ; deux\n"
    "remarques neuves (CX-01, majeure ; CX-02, mineure), avis « scellable après corrections ». Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c3-brouillon7-relance-v1.md`, dont cette version c4 est le résultat.\n"
    "Vérification de la version c4 par le même contre-lecteur, et chemins de versement : À REMPLIR par la session de\n"
    "conduite.\n",
    f"`{H_VERIF3}` ; le programme rejoué rend la version c3, aucun changement\n"
    "hors de sa table ; CW-01 à CW-03 levées ; CW-01 levée sous la confirmation de la conduite, venue ensuite\n"
    "(message de 19:29Z, verrou 7) ; rien de ce qui est tranché n'a bougé ; deux remarques neuves (CX-01, majeure ;\n"
    "CX-02, mineure), avis « scellable après corrections ». Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c3-brouillon7-relance-v1.md`, dont la version c4\n"
    f"(`{EMPREINTE_SOURCE}`) est le résultat.\n"
    "\n"
    "Vérification de la version c4 par le même contre-lecteur (le 2026-11-22) : rapport\n"
    f"`{VERIF4}`,\n"
    f"`{H_VERIF4}` ; le programme rejoué rend la version c4, aucun changement\n"
    "hors de sa table ; CX-01 et CX-02 levées ; l'ajout du rédacteur sur la différence de modèle du bras « saboteur\n"
    "sans consigne » jugé juste et tenable ; rien de ce qui est tranché n'a bougé ; une remarque mineure de forme\n"
    "(CY-01) ; avis « scellable ». Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c4-et-devis-brouillon4-v1.md` et erratum 1 de la version c4\n"
    f"(`{H_ERRATUM}`), que cette version c5 intègre.\n"
    "Vérification de la version c5 par le même contre-lecteur (décision de la chaîne sur le point H-1, trois lignes\n"
    "rapportées de la précision 37), et chemins de versement : À REMPLIR par la session de conduite.\n",
)


def main():
    sortie, journal = Path(sys.argv[1]), Path(sys.argv[2])
    for p in (sortie, journal):
        if p.exists():
            sys.exit(f"refus d'écraser {p} (R12)")
    if sha(SOURCE) != EMPREINTE_SOURCE:
        sys.exit("source : empreinte inattendue")
    texte = SOURCE.read_text(encoding="utf-8")
    titres_avant = re.findall(r"^## .+$", texte, flags=re.M)
    marqueurs_avant = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
    remplir_avant = texte.partition("\n## Contre-lecture\n")[0].count("À REMPLIR")
    h = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
    lignes = ["identifiant\tlieu\tremarque ou motif\tsignes retirés\tsignes écrits\tsha256 du fragment retiré\tsha256 du fragment écrit"]
    vus = set()
    for ident, lieu, motif, ancien, nouveau in R:
        if ident in vus:
            sys.exit(f"{ident} : identifiant doublé")
        vus.add(ident)
        if texte.count(ancien) != 1:
            sys.exit(f"{ident} : fragment trouvé {texte.count(ancien)} fois (attendu : 1)")
        if ancien == nouveau:
            sys.exit(f"{ident} : remplacement vide")
        texte = texte.replace(ancien, nouveau)
        lignes.append("\t".join([ident, lieu, motif, str(len(ancien)), str(len(nouveau)), h(ancien), h(nouveau)]))
    if re.findall(r"^## .+$", texte, flags=re.M) != titres_avant:
        sys.exit("les titres de section ont changé")
    tete, _, contre_lecture = texte.partition("\n## Contre-lecture\n")
    if tete.count("À REMPLIR") != remplir_avant:
        sys.exit("« À REMPLIR » ajouté ou retiré hors de la section « Contre-lecture »")
    if contre_lecture.count("À REMPLIR") != 1:
        sys.exit("la section « Contre-lecture » doit porter un seul « À REMPLIR »")
    marqueurs_apres = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
    if marqueurs_apres != marqueurs_avant - {MARQUEUR_RETIRE} or MARQUEUR_RETIRE not in marqueurs_avant:
        sys.exit("marqueurs de gabarit : seul « MOT_DU_DIRECTEUR_H1 » doit disparaître")
    sortie.write_text(texte, encoding="utf-8")
    journal.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(R)} remplacements ; sortie {sha(sortie)} ; {len(texte.encode('utf-8'))} octets ; {len(marqueurs_apres)} marqueurs")


if __name__ == "__main__":
    main()
