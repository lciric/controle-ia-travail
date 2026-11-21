"""Fabrique lanceur_v6.py à partir de lanceur_v5.py par remplacements exacts, chacun trouvé une fois et une seule.

Version 6 du lanceur de la première passe : correction 1 de la contre-lecture du lanceur version 5
(`contre-lectures/contre-lecture-lanceur-v5-messages-arret-v1.md`, `d821cf66…`). Les fenêtres où une interruption du clavier
exposait, dans sa trace, le message entier d'un arrêt cloisonné sont fermées :
- `principal` : la ligne de l'arrêt est calculée et affichée hors du bloc `except` ;
- `calculer` : toute interruption levée pendant le tri et le versement d'un arrêt est relevée sans enchaînement (`from None`) ;
- `verser_arret_cloisonne` : tout son corps, première ligne comprise, est sous la même coupure.
Les mots fixes de la ligne affichée ne changent pas ; ils sont tenus par des constantes (`LIGNE_ARRET_CLOISONNE` en tête).

Emploi :
    python fabrique-lanceur-v6-v1.py <dossier du paquet> [<dossier des essais>]
- premier argument : `src/controle_ia/lentilles_sondes_bbis` (ou une copie) ; `lanceur_v6.py` y est écrit ;
- second argument, facultatif : `tests` (ou une copie) ; les fichiers d'essais qui importent `lanceur_v5` y sont copiés sous
  des noms neufs qui visent `lanceur_v6` (table `COPIES`) : deux remplacements de noms partout, et, pour le seul fichier des
  essais du lanceur version 5, les accords de la table `ACCORDS` (ses copies jetables défont des lignes de la version 6) et le
  retrait de ses deux derniers essais (fabrique et lignes retirées), repris dans le fichier neuf des essais de la version 6.
Aucun fichier existant n'est réécrit : tous les noms écrits sont neufs (R12).
"""
import sys
from pathlib import Path

paquet = Path(sys.argv[1])
s = (paquet / "lanceur_v5.py").read_text(encoding="utf-8")


def rep(avant: str, apres: str, n: int = 1) -> None:
    global s
    assert s.count(avant) == n, (avant[:70], s.count(avant))
    s = s.replace(avant, apres)


# --- en-tête : les mots qui citent la version -----------------------------------------------------------------------------------------
rep('''Aucune ligne de calcul n'est changée depuis `lanceur_v4`.
"""''', '''Aucune ligne de calcul n'est changée depuis `lanceur_v4`.

Version 6 : correction 1 de la contre-lecture du lanceur version 5
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-lanceur-v5-messages-arret-v1.md`,
`d821cf66698537c8649a3b55ffebdf13b321abfd066bbde1d9df1af6aa82be9b`). Seule différence avec `lanceur_v5` : une interruption du
clavier qui tombe pendant le traitement d'un arrêt cloisonné n'en porte plus le message dans sa trace. `principal` ne fait
dans son bloc `except` que retenir l'arrêt, et calcule et affiche la ligne après ; `calculer` relève sans enchaînement toute
interruption levée pendant le tri et le versement ; `verser_arret_cloisonne` tient tout son corps sous la même coupure. Les
mots fixes de la ligne affichée sont inchangés, et tenus par des constantes. Aucune ligne de calcul n'est changée.
"""''')

# --- liste des modules de la fiche du code : le lanceur lui-même ------------------------------------------------------------------------
rep('''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v5")''',
    '''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v6")''')

# --- versement d'un arrêt cloisonné : tout le corps, première ligne comprise, sous la coupure de l'enchaînement ---------------------------
rep('''    dest = ctx.sortie / "versement" / ctx.run / "calcul-interrompu"
    arret.fichier_d_arret, arret.versement_en_echec = None, False
    try:
        contenu = {"run": ctx.run, "motif": str(arret), "morceaux": [], "travail": None}
        try:
            if parti:
                contenu["morceaux"] = ecrire_morceaux(tableaux, dest / "lectures-interrompues-non-lues") if tableaux else []
                contenu["travail"] = verser_travail(ctx.travail, ctx.sortie, ctx.run, "arret")
            else:
                contenu["avant_le_depart_du_calcul"] = True
        except Exception as e:
            arret.versement_en_echec = True
            contenu["versement_en_echec"] = f"{type(e).__name__} : {e}"
        _ecrire_ferme(dest / "arret.json", contenu)
        arret.fichier_d_arret = dest / "arret.json"
    except Exception:
        arret.fichier_d_arret = None        # `arret.json` non écrit (il existe déjà, R12, ou le disque refuse) : dit par son nom seul
    except BaseException as e:              # interruption pendant le versement : sa trace ne porte pas le message de l'arrêt
        raise e from None
''', '''    try:                                    # version 6 : rien de cette fonction n'est hors de la coupure, première ligne comprise
        arret.fichier_d_arret, arret.versement_en_echec = None, False
        dest = ctx.sortie / "versement" / ctx.run / "calcul-interrompu"
        try:
            contenu = {"run": ctx.run, "motif": str(arret), "morceaux": [], "travail": None}
            try:
                if parti:
                    contenu["morceaux"] = ecrire_morceaux(tableaux, dest / "lectures-interrompues-non-lues") if tableaux else []
                    contenu["travail"] = verser_travail(ctx.travail, ctx.sortie, ctx.run, "arret")
                else:
                    contenu["avant_le_depart_du_calcul"] = True
            except Exception as e:
                arret.versement_en_echec = True
                contenu["versement_en_echec"] = f"{type(e).__name__} : {e}"
            _ecrire_ferme(dest / "arret.json", contenu)
            arret.fichier_d_arret = dest / "arret.json"
        except Exception:
            pass                            # `arret.json` non écrit (il existe déjà, R12, ou le disque refuse) : `fichier_d_arret` reste vide
    except BaseException as e:              # interruption pendant le versement : sa trace ne porte pas le message de l'arrêt
        raise e from None
''')

# --- la ligne affichée : mots fixes tenus par des constantes -------------------------------------------------------------------------------
rep('''def ligne_d_arret_cloisonne(arret: Arret) -> str:
    """La seule ligne que la ligne de commande affiche pour un arrêt cloisonné : des mots fixes, le nom de l'arrêt et le
    chemin du fichier d'arrêt (une existence). Jamais le message : ni identifiant de jeton, ni valeur, ni borne de valeur p,
    ni nom de statistique."""
    fichier = getattr(arret, "fichier_d_arret", None)
    ligne = f"ARRÊT : {nom_d_arret_cloisonne(arret)} ; "
    ligne += f"fichier d'arrêt : {fichier}" if fichier is not None else "fichier d'arrêt non écrit"
    if getattr(arret, "versement_en_echec", False):
        ligne += " ; versement à l'arrêt en échec : rien n'est supprimé"
    return ligne
''', '''# Mots fixes de la ligne affichée pour un arrêt cloisonné (inchangés depuis la version 5). Pour n'afficher que le nom de
# l'arrêt, une seule constante change : `LIGNE_ARRET_CLOISONNE = "{nom}"` (nœud posé au directeur ; non tranché ici).
LIGNE_ARRET_CLOISONNE = "ARRÊT : {nom} ; {fichier}{echec}"
MOTS_FICHIER_D_ARRET_ECRIT = "fichier d'arrêt : {chemin}"
MOTS_FICHIER_D_ARRET_NON_ECRIT = "fichier d'arrêt non écrit"
MOTS_VERSEMENT_EN_ECHEC = " ; versement à l'arrêt en échec : rien n'est supprimé"


def ligne_d_arret_cloisonne(arret: Arret) -> str:
    """La seule ligne que la ligne de commande affiche pour un arrêt cloisonné : des mots fixes, le nom de l'arrêt et le
    chemin du fichier d'arrêt (une existence). Jamais le message : ni identifiant de jeton, ni valeur, ni borne de valeur p,
    ni nom de statistique."""
    fichier = getattr(arret, "fichier_d_arret", None)
    return LIGNE_ARRET_CLOISONNE.format(
        nom=nom_d_arret_cloisonne(arret),
        fichier=MOTS_FICHIER_D_ARRET_ECRIT.format(chemin=fichier) if fichier is not None else MOTS_FICHIER_D_ARRET_NON_ECRIT,
        echec=MOTS_VERSEMENT_EN_ECHEC if getattr(arret, "versement_en_echec", False) else "")
''')

# --- enveloppe du calcul : toute interruption levée pendant le tri et le versement est relevée sans enchaînement ------------------------------
rep('''        if nom_d_arret_cloisonne(arret) is not None:
            verser_arret_cloisonne(ctx, arret, tableaux, etat["parti"])
            raise
''', '''        try:                                # version 6 : le tri et le versement sous la coupure de l'enchaînement
            cloisonne = nom_d_arret_cloisonne(arret) is not None
            if cloisonne:
                verser_arret_cloisonne(ctx, arret, tableaux, etat["parti"])
        except BaseException as e:          # interruption entre l'arrêt et son relevé : sa trace ne porte pas le message
            raise e from None
        if cloisonne:
            raise
''')

# --- ligne de commande : le bloc `except` ne fait que retenir l'arrêt ; la ligne est calculée et affichée après -------------------------------
rep('''    a = p.parse_args(argv)
    try:
''', '''    a = p.parse_args(argv)
    arret = None
    try:
''')
rep('''    except Arret as e:
        print(f"ARRÊT : {e}" if nom_d_arret_cloisonne(e) is None else ligne_d_arret_cloisonne(e), file=sys.stderr)
        return 3
''', '''    except Arret as e:
        arret = e                           # version 6 : rien d'autre dans ce bloc ; hors de lui, aucun arrêt n'est « en cours »
    if arret is not None:
        print(f"ARRÊT : {arret}" if nom_d_arret_cloisonne(arret) is None else ligne_d_arret_cloisonne(arret), file=sys.stderr)
        return 3
''')

(paquet / "lanceur_v6.py").write_text(s, encoding="utf-8")
print("lanceur_v6.py écrit")

# --- copies des essais qui importent lanceur_v5, sous des noms neufs qui visent lanceur_v6 ---------------------------------------------------
COPIES = (("lentilles_sondes_bbis_jouets_v5.py", "lentilles_sondes_bbis_jouets_v6.py"),
          ("test_lentilles_sondes_bbis_addendum_concentration_v3.py", "test_lentilles_sondes_bbis_addendum_concentration_v4.py"),
          ("test_lentilles_sondes_bbis_corrections_contre_lecture_v4.py", "test_lentilles_sondes_bbis_corrections_contre_lecture_v5.py"),
          ("test_lentilles_sondes_bbis_garde_egalite_v2.py", "test_lentilles_sondes_bbis_garde_egalite_v3.py"),
          ("test_lentilles_sondes_bbis_gardes_non_vues_v4.py", "test_lentilles_sondes_bbis_gardes_non_vues_v5.py"),
          ("test_lentilles_sondes_bbis_montage_v5.py", "test_lentilles_sondes_bbis_montage_v6.py"),
          ("test_lentilles_sondes_bbis_procedure_v5.py", "test_lentilles_sondes_bbis_procedure_v6.py"),
          ("test_lentilles_sondes_bbis_lanceur_v5_v1.py", "test_lentilles_sondes_bbis_lanceur_v6_v1.py"))
NOMS = (("lanceur_v5", "lanceur_v6"), ("lentilles_sondes_bbis_jouets_v5", "lentilles_sondes_bbis_jouets_v6"))
# Le fichier des essais du lanceur version 5 : ses copies jetables défont des lignes qui ont changé de forme à la version 6.
ACCORDS = {"test_lentilles_sondes_bbis_lanceur_v5_v1.py": (
    ('''def _copie_jetable(avant: str, apres: str):
    """Artefact : le lanceur de la version 5 dont un passage, trouvé une fois et une seule, est remplacé ; tenu en mémoire,''',
     '''def _copie_jetable(avant: str, apres: str, n: int = 1):
    """Artefact : le lanceur de la version 6 dont un passage, trouvé `n` fois exactement, est remplacé ; tenu en mémoire,'''),
    ('''    assert source.count(avant) == 1, (avant[:60], source.count(avant))''',
     '''    assert source.count(avant) == n, (avant[:60], source.count(avant))'''),
    ('''LIGNE_DU_TRI = "        print(f\\"ARRÊT : {e}\\" if nom_d_arret_cloisonne(e) is None else ligne_d_arret_cloisonne(e), file=sys.stderr)\\n"
BRANCHE_DE_L_ENVELOPPE = ("        if nom_d_arret_cloisonne(arret) is not None:\\n"
                          "            verser_arret_cloisonne(ctx, arret, tableaux, etat[\\"parti\\"])\\n"
                          "            raise\\n")''',
     '''LIGNE_DU_TRI = ("        print(f\\"ARRÊT : {arret}\\" if nom_d_arret_cloisonne(arret) is None else ligne_d_arret_cloisonne(arret), "
                "file=sys.stderr)\\n")
BRANCHE_DE_L_ENVELOPPE = ("            cloisonne = nom_d_arret_cloisonne(arret) is not None\\n"
                          "            if cloisonne:\\n"
                          "                verser_arret_cloisonne(ctx, arret, tableaux, etat[\\"parti\\"])\\n")'''),
    ('''    return _copie_jetable(LIGNE_DU_TRI, "        print(f\\"ARRÊT : {e}\\", file=sys.stderr)\\n")''',
     '''    return _copie_jetable(LIGNE_DU_TRI, "        print(f\\"ARRÊT : {arret}\\", file=sys.stderr)\\n")'''),
    ('''    return _copie_jetable(BRANCHE_DE_L_ENVELOPPE, "")''',
     '''    return _copie_jetable(BRANCHE_DE_L_ENVELOPPE, "            cloisonne = False\\n")'''),
    ('''    copie = _copie_jetable("        raise e from None\\n", "        raise\\n")''',
     '''    copie = _copie_jetable("raise e from None\\n", "raise\\n", 2)          # les deux coupures : le versement, l'enveloppe'''))}
COUPE = "\n\ndef test_l_outil_de_fabrique_rejoue_rend_le_lanceur_de_la_version_5_a_l_octet_pres("   # les deux derniers essais

if len(sys.argv) > 2:
    essais = Path(sys.argv[2])
    for origine, copie in COPIES:
        t = (essais / origine).read_text(encoding="utf-8")
        for avant, apres in ACCORDS.get(origine, ()):
            assert t.count(avant) == 1, (origine, avant[:70], t.count(avant))
            t = t.replace(avant, apres)
        if origine in ACCORDS:
            assert t.count(COUPE) == 1, origine
            t = t[:t.index(COUPE)].rstrip("\n") + "\n"
        assert "lanceur_v5" in t, origine
        for avant, apres in NOMS:                   # le fichier des jouets ne se nomme pas lui-même : second nom facultatif
            t = t.replace(avant, apres)
        assert "lanceur_v5" not in t and "jouets_v5" not in t, origine
        (essais / copie).write_text(t, encoding="utf-8")
        print(f"{copie} écrit")
