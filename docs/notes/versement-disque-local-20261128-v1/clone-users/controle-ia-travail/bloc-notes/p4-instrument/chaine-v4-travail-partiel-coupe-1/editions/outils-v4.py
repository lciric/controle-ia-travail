P = [
('''"""Outils des essais de la chaîne de P4-instrument (v1, chaîne v3) : candidat d'essai, monde jouet, configuration réelle
de référence, configuration jouet d'arrêt, textes synthétiques des fenêtres, phrases du texte lues par la chaîne v2 et
corrigées par la chaîne v3 (traitement des vérifications de la chaîne v2, 10664a97…).''',
'''"""Outils des essais de la chaîne de P4-instrument (v1, chaîne v4) : candidat d'essai, monde jouet, configuration réelle
de référence, configuration jouet d'arrêt, textes synthétiques des fenêtres, phrases du texte lues par la chaîne v2,
corrigées par la chaîne v3 (traitement des vérifications de la chaîne v2, 10664a97…) puis par la chaîne v4 (traitement
de la vérification « fidélité » de la chaîne v2, dde35f6f…).'''),
('''  outils_essais_p4_v1.py paires-v3 SORTIE [--rapport NOM=SHA …]
      paires exactes (ancien → nouveau) qui portent au candidat 1 les phrases lues par la chaîne (PHRASES_V3 : celles de
      la chaîne v2, dont quatre corrigées par la chaîne v3, et la phrase « Rapports versés » aux vingt-six noms), au
      format de `ecrire_candidat2_v1.py` ; rapports sans empreinte donnée : « <empreinte au versement> ». (La commande
      `paires-v2` de la chaîne v2 est retirée : ses phrases ne sont plus celles du code.)''',
'''  outils_essais_p4_v1.py paires-v4 SORTIE [--rapport NOM=SHA …]
      paires exactes (ancien → nouveau) qui portent au candidat 1 les phrases lues par la chaîne (PHRASES_V4 : celles de
      la chaîne v2, corrigées par la chaîne v3 puis par la chaîne v4, et la phrase « Rapports versés » aux vingt-sept
      noms, avec la règle des rapports postérieurs au candidat), au format de `ecrire_candidat2_v2.py` ; rapports sans
      empreinte donnée : « <empreinte au versement> ». (Les commandes `paires-v2` et `paires-v3` sont retirées : leurs
      phrases ne sont plus celles du code.)'''),
('''Le candidat d'essai (`candidat`) porte à sa fin les mêmes phrases (PHRASES_V3) : les bancs lisent ce que lira le texte.''',
'''Le candidat d'essai (`candidat`) porte à sa fin les mêmes phrases (PHRASES_V4) : les bancs lisent ce que lira le texte.'''),
('''# rapports attendus (noms exacts du module commun, RAPPORTS_NOMS : vingt-six noms, chaîne v3) et leur empreinte quand le
# fichier existe déjà (fichier source du bloc-notes de la session, empreinte égale à son sceau compagnon quand il en a un)''',
'''# rapports attendus (noms exacts du module commun, RAPPORTS_NOMS : vingt-sept noms, chaîne v4) et leur empreinte quand le
# fichier existe déjà (fichier source du bloc-notes de la session, empreinte égale à son sceau compagnon quand il en a un)'''),
('''    "verification-chaine-v2-fidelite-P4-instrument-v1.md": None,
    "traitement-verifications-chaine-v2-P4-v1.md": "10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e",
    "verification-chaine-v3-P4-instrument-v1.md": None,''',
'''    "verification-chaine-v2-fidelite-P4-instrument-v1.md": "4e92c3deed0df22b76ebffd16997c8b9e0e471783b54567313385457c4392da4",
    "traitement-verifications-chaine-v2-P4-v1.md": "10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e",
    "traitement-verification-fidelite-chaine-v2-P4-v1.md": "dde35f6f8def8a43c0def9ca98c432b34bb472893bc0c8a2602327ebc4c6c898",
    "verification-chaine-v4-P4-instrument-v1.md": None,'''),
('''PHRASES_V3 = _phrases_v3()
ANCRE_RAPPORTS''',
'''PHRASES_V3 = _phrases_v3()
# chaîne v4 : phrases de la chaîne v3 corrigées par le traitement de la vérification « fidélité » de la chaîne v2
# (dde35f6f…), chacune par des remplacements exacts dans son « nouveau » (segment trouvé une seule fois) :
#   accord-forme-150 : VC2-fidelite-10 (alerte écrite dans les traces du lancement ; la session la rapporte) ;
#   revocation-voisine : VC2-fidelite-06 (types de R-281 absents de l'en-tête), -11 (débuts tels quels ; codes du
#   module commun) ;
#   precision-5 : VC2-fidelite-11 (codes du module commun) ;
#   liste-d-arret : VC2-fidelite-03 (une seule définition de l'heure limite, son dépassement écrit, observables nommés,
#   volume téléchargé non relu, rappel de la session), -04 (trois refus en code 2) ;
#   paragraphes : VC2-fidelite-08 (repli de l'affichage à la forme stricte ; la ligne de l'instance gardée reste
#   réécrite entière, CV3-03) ;
#   tokeniseur-metrique : VC2-fidelite-09 (phrase du rapport mot pour mot, empreinte écrite en entier).
CORRECTIONS_V4 = {
    "accord-forme-150": ("VC2-fidelite-10", (
        ("l'alerte de GO-2026-10-04-08 est écrite à l'accord.",
         "l'alerte de GO-2026-10-04-08 est écrite dans les traces du\\n"
         "    lancement à chaque relecture de l'accord ; la session la rapporte à Lazar."),)),
    "revocation-voisine": ("VC2-fidelite-06, -11", (
        ("    type « Révocation », « revocation » ou absent de l'en-tête du registre des GO ; toute cellule d'une ligne de GO,\\n"
         "    de tout type, ou d'une ligne de décision qui commence par « Révocation », « révoque », « annulation » ou « retrait » ;\\n",
         "    type « Révocation », « revocation » ou absent de l'en-tête du registre des GO (« lecture complémentaire », « règle »\\n"
         "    et « décision », écrits par R-281, en sont absents) ; toute cellule d'une ligne de GO, de tout type, ou d'une ligne\\n"
         "    de décision qui commence, sans casse ni accent, par « revoc », « revoqu », « annul », « retrait » ou « retir » ;\\n"),
        ("arrête aussi le lancement (code 2, lignes affichées) :",
         "arrête aussi le lancement (code 2 du module commun, lignes affichées) :"))),
    "precision-5": ("VC2-fidelite-11", (
        ("5. Révocation : les formes écrites à l'en-tête bloquent (code 1) ; une forme voisine qui nomme l'un des cinq\\n"
         "   identifiants bloque aussi (code 2) ;",
         "5. Révocation : les formes écrites à l'en-tête bloquent (code 1 du module commun) ; une forme voisine qui nomme\\n"
         "   l'un des cinq identifiants bloque aussi (code 2 du module commun) ; le lanceur sort en code 2 dans les deux cas ;"),)),
    "liste-d-arret": ("VC2-fidelite-03, -04", (
        ("- Contrôle à cinq minutes en échec (il relit aussi le téléchargement, au plus 0,05 USD par Go, et le stockage, au\\n"
         "  plus 0,03 USD de l'heure) ; dépense au-delà de la borne de l'étape : arrêt de l'instance par son identifiant\\n"
         "  (`arreter_p4_v1.sh`, appelé par le contrôle à cinq minutes en échec).",
         "- Contrôle à cinq minutes en échec (il relit une fois, entre 3 et 5 minutes après la création, les prix de l'offre :\\n"
         "  prix de l'heure, téléchargement au plus 0,05 USD par Go, stockage au plus 0,03 USD de l'heure) : arrêt de\\n"
         "  l'instance par son identifiant (`arreter_p4_v1.sh`, appelé par le contrôle à cinq minutes en échec). Dépense\\n"
         "  au-delà de la borne de l'étape : ses observables sont ces prix, le plafond de la surveillance (création + 9 600 s,\\n"
         "  puis arrêt), l'heure de l'arrêt relu (`arret.txt`) et l'heure limite de destruction ; le volume téléchargé\\n"
         "  (≈ 20 Go supposés) n'est relu par aucun code."),
        ("- Récupération en échec (code 1, ou refus en code 2 faute de place disque ou de clonage) : aucune destruction ;\\n"
         "  la récupération écrit l'état de l'instance et l'heure limite de destruction (création + 9 600 s + 24 heures) ;\\n"
         "  nœud de Lazar.",
         "- Récupération en échec (code 1, ou refus en code 2 faute de place disque, de clonage ou pour des traces d'un autre\\n"
         "  lancement) : aucune destruction ; la récupération écrit l'état de l'instance et l'heure limite de destruction ;\\n"
         "  nœud de Lazar. L'heure limite de destruction est 24 heures après l'heure d'arrêt relue dans `arret.txt` (écrit par\\n"
         "  `arreter_p4_v1.sh`, passé à la récupération) ; sans lui, la récupération écrit le repli déclaré « création\\n"
         "  + 9 600 s + 24 heures » et sa raison. Toute récupération écrit cette heure ; dépassée, elle écrit « heure limite\\n"
         "  dépassée de N s : borne du disque dépassée : nœud de Lazar », sans retarder la destruction. La session programme\\n"
         "  au lancement un rappel à l'heure de repli, puis le remet à 24 heures après l'arrêt relu (consigne écrite dans\\n"
         "  `lancement.txt`)."))),
    "paragraphes": ("VC2-fidelite-08", (
        ("la récupération est en échec (KO 4f, aucune destruction) et chaque ligne n'est affichée que par\\n"
         "  ses 40 premiers caractères, sa longueur et son empreinte courte. La ligne",
         "la récupération est en échec (KO 4f, aucune destruction) ; seules les lignes OK, KO et « -- »\\n"
         "  de forme fixe (motifs fermés, sans donnée de la branche) s'affichent, et toute autre ligne n'est affichée que par\\n"
         "  sa longueur et son empreinte courte (avec, pour une ligne OK, KO ou « -- », son statut et le numéro de son\\n"
         "  contrôle), sans aucun caractère de son texte. La ligne"),)),
    "tokeniseur-metrique": ("VC2-fidelite-09", (
        ("    citée (copie de la session, versée avec MC-1 sous `donnees/P4-tokeniseur-v1/tokenizer.json`,\\n"
         "    `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` ; Chaîne de lancement)",
         "    citée (copie de la session, à verser par la session avant S sous `donnees/P4-tokeniseur-v1/tokenizer.json`\\n"
         "    (`79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`) ; Chaîne de lancement)"),)),
}


def _phrases_v4() -> tuple:
    """(clé, constats, ancien, nouveau, version) : PHRASES_V3, chaque correction de CORRECTIONS_V4 appliquée à son
    « nouveau » (segment trouvé une seule fois, sinon arrêt)."""
    sortie = []
    for k, c, a, b, v in PHRASES_V3:
        if k not in CORRECTIONS_V4:
            sortie.append((k, c, a, b, v))
            continue
        constats, remplacements = CORRECTIONS_V4[k]
        for x, y in remplacements:
            if b.count(x) != 1:
                raise SystemExit(f"phrase {k} : segment à corriger (chaîne v4) trouvé {b.count(x)} fois (une attendue)")
            b = b.replace(x, y)
        sortie.append((k, f"{c} ; chaîne v4 : {constats}", a, b, "v4"))
    if set(CORRECTIONS_V4) - {k for k, *_ in PHRASES_V3}:
        raise SystemExit("correction de la chaîne v4 sans phrase de la chaîne v3")
    return tuple(sortie)


PHRASES_V4 = _phrases_v4()
REGLE_POSTERIEURS = ("Les rapports qui vérifient le candidat 2 sont cités par le texte final, qui leur est postérieur ; "
                     "aucun fichier de la famille « P4 » n'entre dans `prereg/contre-lectures/` après S.")
ANCRE_RAPPORTS'''),
('''    return ("- **Rapports versés** (sous `prereg/contre-lectures/`, avec leurs sceaux ; noms exacts, seuls de leur famille,\\n"
            f"  relus par les contrôles et le scellement) :\\n  {cites}.")''',
'''    return ("- **Rapports versés** (sous `prereg/contre-lectures/`, avec leurs sceaux ; noms exacts, seuls de leur famille,\\n"
            f"  relus par les contrôles et le scellement) :\\n  {cites}.\\n  {REGLE_POSTERIEURS}")'''),
('''    # phrases lues par la chaîne (les mêmes que les paires du candidat 1, chaîne v3), à la fin du texte d'essai
    t = t.rstrip("\\n") + "\\n" + "\\n".join(nouveau for _, _, _, nouveau, _ in PHRASES_V3) + "\\n"''',
'''    # phrases lues par la chaîne (les mêmes que les paires du candidat 1, chaîne v4), à la fin du texte d'essai
    t = t.rstrip("\\n") + "\\n" + "\\n".join(nouveau for _, _, _, nouveau, _ in PHRASES_V4) + "\\n"'''),
('''def paires_v3(sortie: str, rapports: list[str]) -> int:
    """Paires exactes (ancien → nouveau) qui portent au candidat 1 les phrases de la chaîne (v2, corrigées par la v3) ;
    la source d'une paire inchangée reste celle de la chaîne v2."""''',
'''def paires_v4(sortie: str, rapports: list[str]) -> int:
    """Paires exactes (ancien → nouveau) qui portent au candidat 1 les phrases de la chaîne (v2, corrigées par la v3 puis
    par la v4) ; la source d'une paire inchangée reste celle de la version qui l'a écrite."""'''),
('''    paires = [{"ancien": a, "nouveau": b, "source": f"chaîne {v}, {k} ({c})"} for k, c, a, b, v in PHRASES_V3]
    paires.append({"ancien": ANCRE_RAPPORTS, "nouveau": ANCRE_RAPPORTS + "\\n" + phrase_rapports(connus),
                   "source": "chaîne v3, rapports attendus (RC-fidelite-12 ; RAPPORTS_NOMS de la chaîne v3, vingt-six noms)"})''',
'''    paires = [{"ancien": a, "nouveau": b, "source": f"chaîne {v}, {k} ({c})"} for k, c, a, b, v in PHRASES_V4]
    paires.append({"ancien": ANCRE_RAPPORTS, "nouveau": ANCRE_RAPPORTS + "\\n" + phrase_rapports(connus),
                   "source": "chaîne v4, rapports attendus (RC-fidelite-12, VC2-fidelite-01 ; RAPPORTS_NOMS de la chaîne v4, "
                             "vingt-sept noms ; règle des rapports postérieurs au candidat)"})'''),
('''    for p in v.PASSAGES:
        l.append(p + "; durée totale 1 s")
        l.extend(f"    | 2026-10-20T00:00:00Z {x} (essai)" for x in v.DANS_LE_PASSAGE.get(p, ()))
    for x in v.CONFORMES:
        l.append(x)
        l.append("    --  3f versions non comparées (essai)")
        if v.DANS_LA_RECUPERATION.get(x):
            l.append(v.DANS_LA_RECUPERATION[x] + '{"etape": "essai", "motif": "essai"}')''',
'''    for p in v.PASSAGES:
        l.append(p + "; durée totale 1 s")
        l.extend(f"    | 2026-10-20T00:00:00Z {x} (essai)" for x in v.DANS_LE_PASSAGE.get(p, ()))
    for x in v.CONFORMES:
        l.append(x)
        l.append("    --  3f versions non comparées (essai)")
        # chaîne v4 : lignes exigées (début, texte qu'elles contiennent)
        l.extend(f"{debut}{dedans} (essai)" for debut, dedans in v.DANS_LA_RECUPERATION.get(x, ()))'''),
('''    l.append(v.REPLI)''',
'''    l.extend(v.REPLIS)'''),
('''    elif len(argv) >= 3 and argv[1] == "paires-v3":
        reste = argv[3:]
        if len(reste) % 2 or any(reste[i] != "--rapport" or "=" not in reste[i + 1] for i in range(0, len(reste), 2)):
            print("usage : paires-v3 SORTIE [--rapport NOM=SHA …]", file=sys.stderr)
            return 2
        print(paires_v3(argv[2], reste[1::2]))''',
'''    elif len(argv) >= 3 and argv[1] == "paires-v4":
        reste = argv[3:]
        if len(reste) % 2 or any(reste[i] != "--rapport" or "=" not in reste[i + 1] for i in range(0, len(reste), 2)):
            print("usage : paires-v4 SORTIE [--rapport NOM=SHA …]", file=sys.stderr)
            return 2
        print(paires_v4(argv[2], reste[1::2]))'''),
('''              "config-arret DEPOT MODULE CONFIG_ENTREE CONFIG_SORTIE DUREE | paires-v3 SORTIE [--rapport NOM=SHA …] | "''',
'''              "config-arret DEPOT MODULE CONFIG_ENTREE CONFIG_SORTIE DUREE | paires-v4 SORTIE [--rapport NOM=SHA …] | "'''),
]
