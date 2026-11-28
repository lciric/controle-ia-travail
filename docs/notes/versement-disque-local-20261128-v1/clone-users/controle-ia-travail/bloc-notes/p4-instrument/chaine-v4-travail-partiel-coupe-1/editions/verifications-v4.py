P = [
("""  - répétition : refus du clonage en code 2, état de l'instance gardée et heure limite dans les refus de la place et du
    clonage (VC2-depense-03) ; repli de l'affichage de la récupération (VC2-donnees-01).
""",
"""  - répétition : refus du clonage en code 2, état de l'instance gardée et heure limite dans les refus de la place et du
    clonage (VC2-depense-03) ; repli de l'affichage de la récupération (VC2-donnees-01).
Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2, `traitement-verification-fidelite-chaine-v2-P4-v1.md`,
dde35f6f…) :
  - VC2-fidelite-01 : RAPPORTS_NOMS, liste de vingt-sept noms ;
  - VC2-fidelite-06 : TYPES_GO réduit aux sept types de l'en-tête du registre des GO (« lecture complémentaire »,
    « règle » et « décision », écrits par R-281 hors de la liste, sont inconnus : une telle ligne qui nomme l'un des
    cinq identifiants arrête, code 2) ;
  - répétition : sixième passage, délai externe du run (VC2-fidelite-07 : TERM du `timeout` de l'instance converti en
    arrêt consigné, partiels poussés, récupération conforme avec le motif) ; neuf récupérations conformes, dont l'heure
    limite de destruction relue dans `arret.txt`, son repli déclaré et son dépassement écrit sans retarder la
    destruction (VC2-fidelite-03) ; état et heure limite dans les trois refus en code 2 (VC2-fidelite-04) ; deux replis
    de l'affichage à la forme stricte (module commun de S illisible, textes de S absents ; VC2-fidelite-08).
"""),
("""      journal de la répétition jouet : commit répété, candidat répété, cinq passages à leur code, sept récupérations
      conformes (instance détruite), vingt-sept artefacts refusés chacun par un seul KO au préfixe attendu, chacun avec
      l'état de l'instance gardée et l'heure limite de destruction, trois refus en code 2 (place, traces d'un autre
      lancement, clonage ; état et heure limite dans ceux de la place et du clonage), le repli de l'affichage, aucun
      jeton ni aucune fenêtre affichés ;""",
"""      journal de la répétition jouet : commit répété, candidat répété, six passages à leur code (le sixième : délai
      externe du run), neuf récupérations conformes (instance détruite ; heure limite de destruction relue, en repli
      déclaré ou dépassée), vingt-sept artefacts refusés chacun par un seul KO au préfixe attendu, chacun avec l'état
      de l'instance gardée et l'heure limite de destruction, trois refus en code 2 (place, traces d'un autre lancement,
      clonage ; état et heure limite dans chacun), deux replis de l'affichage, aucun jeton ni aucune fenêtre affichés ;"""),
("""# types de l'en-tête du registre des GO (et ceux de R-281), sans casse ni accent
TYPES_GO = ("calcul", "porte", "depot distant", "publication", "contact", "revendication", "revocation",
            "lecture complementaire", "regle", "decision")""",
"""# types de l'en-tête du registre des GO, sans casse ni accent ; chaîne v4 (VC2-fidelite-06) : les types écrits par R-281
# hors de cette liste (« lecture complémentaire », « règle », « décision ») sont inconnus : une telle ligne qui nomme
# l'un des cinq identifiants arrête (code 2), comme toute ligne d'un type inconnu
TYPES_GO = ("calcul", "porte", "depot distant", "publication", "contact", "revendication", "revocation")"""),
("""# rapports attendus sous prereg/contre-lectures/ (seuls de leur famille : nom qui contient « P4 »), noms exacts ; chaîne
# v3 : liste finale de vingt-six noms, dans l'ordre de la section « Liste RAPPORTS_NOMS » du traitement des vérifications
# de la chaîne v2 (`traitement-verifications-chaine-v2-P4-v1.md`, 10664a97…)""",
"""# rapports attendus sous prereg/contre-lectures/ (seuls de leur famille : nom qui contient « P4 »), noms exacts ; chaîne
# v4 : liste de vingt-sept noms, dans l'ordre de la section « Liste RAPPORTS_NOMS de la chaîne v4 » du traitement de la
# vérification « fidélité » de la chaîne v2 (`traitement-verification-fidelite-chaine-v2-P4-v1.md`, dde35f6f…) ; les
# rapports qui vérifient le candidat 2 sont cités par le texte final, qui leur est postérieur (VC2-fidelite-01)"""),
("""    "traitement-verifications-chaine-v2-P4-v1.md",
    "verification-chaine-v3-P4-instrument-v1.md",             # vérification de la chaîne v3 (à venir)
    "verification-candidat2-P4-instrument-v1.md",             # vérification du candidat 2 (à venir)""",
"""    "traitement-verifications-chaine-v2-P4-v1.md",
    "traitement-verification-fidelite-chaine-v2-P4-v1.md",
    "verification-chaine-v4-P4-instrument-v1.md",             # vérification de la chaîne v4 (à venir)
    "verification-candidat2-P4-instrument-v1.md",             # vérification du candidat 2 (à venir)"""),
("""PASSAGES = ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ", "passage 3-manque : code 1 ",
            "passage 4-plafond-de-l-amorce : code 124 ", "passage 5-arret-du-module : code 1 ")
# lignes exigées dans le bloc indenté d'un passage (journal de l'instance, préfixe « | »)
DANS_LE_PASSAGE = {"passage 5-arret-du-module : code 1 ": ("ARRÊT pendant run ", "branche calcul/p4-jouet-r-v1 poussée")}""",
"""PASSAGES = ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ", "passage 3-manque : code 1 ",
            "passage 4-plafond-de-l-amorce : code 124 ", "passage 5-arret-du-module : code 1 ",
            "passage 6-delai-externe : code 1 ")
# lignes exigées dans le bloc indenté d'un passage (journal de l'instance, préfixe « | ») ; chaîne v4 (VC2-fidelite-07) :
# sixième passage, copie du script de l'instance dont seule la ligne DELAI change : TERM du délai externe pendant le run,
# arrêt consigné par le module (résumé avec motif), code 124 du run, partiels poussés
DANS_LE_PASSAGE = {"passage 5-arret-du-module : code 1 ": ("ARRÊT pendant run ", "branche calcul/p4-jouet-r-v1 poussée"),
                   "passage 6-delai-externe : code 1 ": ("ARRÊT pendant run (code 124)", "signal TERM reçu (délai externe du run",
                                                         "branche calcul/p4-jouet-s-v1 poussée")}"""),
("""             f"récupération (textes-degeneres) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}")
# ligne exigée dans le bloc d'une récupération conforme
DANS_LA_RECUPERATION = {f"récupération (passage-5-arret-du-module) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}":
                        "    --  4a arrêt : "}""",
"""             f"récupération (textes-degeneres) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (passage-6-delai-externe) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (limite-depassee) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}")
# lignes exigées dans le bloc d'une récupération conforme : (début de la ligne, texte qu'elle contient) ; chaîne v4 :
# motif TERM du délai externe (VC2-fidelite-07) ; heure limite de destruction relue dans arret.txt, en repli déclaré
# (arret.txt absent, ou sans arrêt confirmé de cette instance) et dépassée sans retarder la destruction (VC2-fidelite-03)
_LIMITE = "    --  8 heure limite de destruction "
DANS_LA_RECUPERATION = {
    CONFORMES[0]: ((_LIMITE, "(arrêt relu à "),),
    CONFORMES[1]: ((_LIMITE, "(repli déclaré : arret.txt absent ; création + 9 600 s + 24 h)"),),
    CONFORMES[3]: (("    --  4a arrêt : ", ""),),
    CONFORMES[5]: ((_LIMITE, "(repli déclaré : arret.txt sans arrêt confirmé de l'instance 99999999 ; création + 9 600 s + 24 h)"),),
    CONFORMES[7]: (("    --  4a arrêt : ", "signal TERM reçu (délai externe du run"),),
    CONFORMES[8]: (("    --  8 heure limite dépassée de ", " s : borne du disque dépassée : nœud de Lazar"),)}"""),
("""# chaîne v3 (VC2-depense-03) : refus en code 2 après la lecture des traces (place, clonage) : état de l'instance gardée et
# heure limite de destruction écrits dans le bloc du refus
DANS_LE_REFUS = {REFUS[0]: GARDEE, REFUS[2]: GARDEE}
# chaîne v3 (VC2-donnees-01) : repli de l'affichage (module commun de S illisible) : ligne écrite par la répétition après
# ses propres contrôles de la sortie de cette récupération
REPLI = ("récupération en repli de l'affichage (artefact-repli-de-l-affichage) : code 1 ; KO 4f ; chaque ligne filtrée "
         "réduite à ses 40 premiers caractères, sa longueur et son empreinte courte ; instance gardée, état et heure "
         "limite de destruction écrits ; aucune destruction")""",
"""# chaîne v3 (VC2-depense-03), chaîne v4 (VC2-fidelite-04) : refus en code 2 (place, traces d'un autre lancement,
# clonage) : état de l'instance gardée et heure limite de destruction écrits dans le bloc de chaque refus
DANS_LE_REFUS = {REFUS[0]: GARDEE, REFUS[1]: GARDEE, REFUS[2]: GARDEE}
# chaîne v4 (VC2-fidelite-08, forme la plus stricte) : repli de l'affichage (module commun de S illisible ; textes de S
# absents) : lignes écrites par la répétition après ses propres contrôles de la sortie de ces récupérations
REPLIS = tuple(f"récupération en repli de l'affichage ({x}) : code 1 ; KO 4f ; seules les lignes OK, KO et -- de forme "
               "fixe affichées, les autres par leur longueur et leur empreinte courte ; instance gardée réécrite entière, "
               "état et heure limite de destruction écrits ; aucune destruction"
               for x in ("artefact-repli-de-l-affichage", "artefact-textes-absents"))"""),
("""               *ARTEFACTS, *REFUS, *SANS_AFFICHAGE, REFUS_LECTURE, REPLI]""",
"""               *ARTEFACTS, *REFUS, *SANS_AFFICHAGE, REFUS_LECTURE, *REPLIS]"""),
("""        attendu = DANS_LA_RECUPERATION.get(etiquette)
        if attendu and not any(x.startswith(attendu) for x in bloc):
            raise SystemExit(f"{etiquette} : « {attendu.strip()} » absent de son bloc")""",
"""        for debut, dedans in DANS_LA_RECUPERATION.get(etiquette, ()):
            if not any(x.startswith(debut) and dedans in x for x in bloc):
                raise SystemExit(f"{etiquette} : « {(debut.strip() + ' … ' + dedans).strip(' …')} » absent de son bloc")"""),
]
