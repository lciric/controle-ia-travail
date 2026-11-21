"""Fabrique lanceur_v5.py à partir de lanceur_v4.py par remplacements exacts, chacun trouvé une fois et une seule.

Version 5 du lanceur de la première passe (GO-2026-11-20-56) : le message entier d'un arrêt d'égalité au vingtième rang d'une
direction lue (`EgaliteDirectionLue`) ou d'un arrêt des directions nulles (`EgaliteNulleDecisive`) va dans le seul fichier
d'arrêt, `arret.json` ; la ligne de commande n'affiche que le nom de l'arrêt et le chemin de ce fichier.

Emploi :
    python fabrique-lanceur-v5-v1.py <dossier du paquet> [<dossier des essais>]
- premier argument : `src/controle_ia/lentilles_sondes_bbis` (ou une copie) ; `lanceur_v5.py` y est écrit ;
- second argument, facultatif : `tests` (ou une copie) ; les fichiers d'essais qui importent `lanceur_v4` y sont copiés sous
  des noms neufs qui visent `lanceur_v5` (table `COPIES`), par deux remplacements de noms, et, pour le seul fichier de la garde
  d'égalité, par trois remplacements exacts des lignes qui affirmaient l'ancienne sortie de la ligne de commande.
Aucun fichier existant n'est réécrit par cet outil dans le dépôt : tous les noms écrits sont neufs (R12).
"""
import sys
from pathlib import Path

paquet = Path(sys.argv[1])
s = (paquet / "lanceur_v4.py").read_text(encoding="utf-8")


def rep(avant: str, apres: str, n: int = 1) -> None:
    global s
    assert s.count(avant) == n, (avant[:70], s.count(avant))
    s = s.replace(avant, apres)


# --- en-tête : les mots qui citent la version -----------------------------------------------------------------------------------------
rep('''  calcul (absent : rien ne part), et le manifeste le cite toujours.
"""''', '''  calcul (absent : rien ne part), et le manifeste le cite toujours.

Version 5 : messages d'arrêt cloisonnés (mot de Lazar, GO-2026-11-20-56 ; nœud 1 de la contre-lecture
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-premiere-passe-addendum-v1.md`,
`7954d0fc54320d76ed63a634893063425683806dfb327acec1443e1ed6a96fd4`). Seule différence avec `lanceur_v4` : quand le calcul
s'arrête sur une égalité au vingtième rang d'une direction lue (`EgaliteDirectionLue`, EC-6, étage (i)) ou sur une égalité d'une
direction nulle décisive pour un libellé (`EgaliteNulleDecisive`, étage (ii)), le message entier que l'addendum exige est écrit
dans le seul fichier d'arrêt, `versement/<run>/calcul-interrompu/arret.json` (champ `motif`) ; la sortie d'erreur ne porte que
le nom de l'arrêt et le chemin de ce fichier, la sortie standard rien. Le tri se fait ici (`ARRETS_CLOISONNES`,
`verser_arret_cloisonne`, `ligne_d_arret_cloisonne`) ; `statistiques_v3` est inchangé. Les autres arrêts gardent leur sortie.
Aucune ligne de calcul n'est changée depuis `lanceur_v4`.
"""''')

# --- liste des modules de la fiche du code : le lanceur lui-même ------------------------------------------------------------------------
rep('''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v4")''',
    '''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v5")''')

# --- enveloppe du calcul : le tri entre le fichier d'arrêt et la ligne de commande ----------------------------------------------------------
rep('''def calculer(ctx: Contexte, racine_entrees: Path, registre_bbis: Path, nettoyage: bool = True) -> dict:
    """Enveloppe du calcul : à tout arrêt après le départ du calcul, ce qui existe est versé (dossier de travail inventorié et
    ses fichiers hors licence copiés ; tableaux déjà calculés écrits, fermés, scellés, marqués « interrompus, non lus »), rien
    n'est supprimé, puis l'arrêt est relevé tel quel."""
    tableaux: dict[str, np.ndarray] = {}
    etat = {"parti": False}
    try:
        return _calculer(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat)
    except Arret as arret:
        if not etat["parti"]:
''', '''# Arrêts cloisonnés (version 5) : le message entier ne va que dans `arret.json` ; la ligne de commande n'en affiche que le nom.
# (classe, nom affiché) : le nom affiché est un code fixe, égal au nom de la classe.
ARRETS_CLOISONNES = ((st.EgaliteDirectionLue, "EgaliteDirectionLue"), (st.EgaliteNulleDecisive, "EgaliteNulleDecisive"))


def nom_d_arret_cloisonne(arret: BaseException) -> str | None:
    """Nom affiché d'un arrêt cloisonné ; `None` pour tout autre arrêt (sa sortie est celle de `lanceur_v4`)."""
    for classe, nom in ARRETS_CLOISONNES:
        if isinstance(arret, classe):
            return nom
    return None


def verser_arret_cloisonne(ctx: Contexte, arret: Arret, tableaux: dict, parti: bool) -> None:
    """Versement à l'arrêt d'un arrêt cloisonné. Le message entier (`str(arret)`) est écrit dans le seul `arret.json`, champ
    `motif` ; il n'entre dans aucune autre exception ni aucune impression. Ne lève aucune exception de la classe `Exception` :
    un échec du versement (R12, disque, copie) est écrit dans `arret.json` (`versement_en_echec`) quand ce fichier peut
    l'être, et noté sur l'arrêt (`versement_en_echec`, `fichier_d_arret`), que la ligne de commande lit. Un arrêt cloisonné
    levé avant le départ du calcul (aucun chemin du code n'y mène ; défense) écrit quand même son `arret.json`, sans rien
    verser du dossier de travail."""
    dest = ctx.sortie / "versement" / ctx.run / "calcul-interrompu"
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


def ligne_d_arret_cloisonne(arret: Arret) -> str:
    """La seule ligne que la ligne de commande affiche pour un arrêt cloisonné : des mots fixes, le nom de l'arrêt et le
    chemin du fichier d'arrêt (une existence). Jamais le message : ni identifiant de jeton, ni valeur, ni borne de valeur p,
    ni nom de statistique."""
    fichier = getattr(arret, "fichier_d_arret", None)
    ligne = f"ARRÊT : {nom_d_arret_cloisonne(arret)} ; "
    ligne += f"fichier d'arrêt : {fichier}" if fichier is not None else "fichier d'arrêt non écrit"
    if getattr(arret, "versement_en_echec", False):
        ligne += " ; versement à l'arrêt en échec : rien n'est supprimé"
    return ligne


def calculer(ctx: Contexte, racine_entrees: Path, registre_bbis: Path, nettoyage: bool = True) -> dict:
    """Enveloppe du calcul : à tout arrêt après le départ du calcul, ce qui existe est versé (dossier de travail inventorié et
    ses fichiers hors licence copiés ; tableaux déjà calculés écrits, fermés, scellés, marqués « interrompus, non lus »), rien
    n'est supprimé, puis l'arrêt est relevé tel quel. Un arrêt cloisonné (`ARRETS_CLOISONNES`) est versé par
    `verser_arret_cloisonne`, puis relevé tel quel, pour l'appelant Python ; son message ne sort que dans `arret.json`."""
    tableaux: dict[str, np.ndarray] = {}
    etat = {"parti": False}
    try:
        return _calculer(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat)
    except Arret as arret:
        if nom_d_arret_cloisonne(arret) is not None:
            verser_arret_cloisonne(ctx, arret, tableaux, etat["parti"])
            raise
        if not etat["parti"]:
''')

# --- ligne de commande : un arrêt cloisonné n'affiche que son nom et le chemin de son fichier d'arrêt -----------------------------------------
rep('''    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 3
''', '''    except Arret as e:
        print(f"ARRÊT : {e}" if nom_d_arret_cloisonne(e) is None else ligne_d_arret_cloisonne(e), file=sys.stderr)
        return 3
''')

(paquet / "lanceur_v5.py").write_text(s, encoding="utf-8")
print("lanceur_v5.py écrit")

# --- copies des essais qui importent lanceur_v4, sous des noms neufs qui visent lanceur_v5 ---------------------------------------------------
COPIES = (("lentilles_sondes_bbis_jouets_v4.py", "lentilles_sondes_bbis_jouets_v5.py"),
          ("test_lentilles_sondes_bbis_addendum_concentration_v2.py", "test_lentilles_sondes_bbis_addendum_concentration_v3.py"),
          ("test_lentilles_sondes_bbis_corrections_contre_lecture_v3.py", "test_lentilles_sondes_bbis_corrections_contre_lecture_v4.py"),
          ("test_lentilles_sondes_bbis_garde_egalite_v1.py", "test_lentilles_sondes_bbis_garde_egalite_v2.py"),
          ("test_lentilles_sondes_bbis_gardes_non_vues_v3.py", "test_lentilles_sondes_bbis_gardes_non_vues_v4.py"),
          ("test_lentilles_sondes_bbis_montage_v4.py", "test_lentilles_sondes_bbis_montage_v5.py"),
          ("test_lentilles_sondes_bbis_procedure_v4.py", "test_lentilles_sondes_bbis_procedure_v5.py"))
NOMS = (("lanceur_v4", "lanceur_v5"), ("lentilles_sondes_bbis_jouets_v4", "lentilles_sondes_bbis_jouets_v5"))
# Le seul essai existant qui affirmait l'ancienne sortie : l'arrêt d'une direction lue, par la ligne de commande.
ACCORDS = {"test_lentilles_sondes_bbis_garde_egalite_v1.py": (
    ('''    par la garde, arrête le calcul avant toute écriture de table ; ce qui existe est versé, rien n'est supprimé ; la ligne de
    commande rend le code 3 et le message nommé. L'égalité est ici déclarée par la garde elle-même (la quarantième liste
    relevée), le reste du chemin étant celui du code."""''',
     '''    par la garde, arrête le calcul avant toute écriture de table ; ce qui existe est versé, rien n'est supprimé ; la ligne de
    commande rend le code 3, le nom de l'arrêt et le chemin du fichier d'arrêt, jamais le message (version 5 du lanceur).
    L'égalité est ici déclarée par la garde elle-même (la quarantième liste relevée), le reste du chemin étant celui du code."""'''),
    ('''    # la ligne de commande : code 3, message nommé sur la sortie d'erreur, rien sur la sortie standard''',
     '''    # la ligne de commande : code 3, nom de l'arrêt et chemin du fichier d'arrêt sur la sortie d'erreur, rien sur la sortie standard'''),
    ('''    assert code == 3 and sortie.err.startswith(f"ARRÊT : {st.MESSAGE_EGALITE_LUE}") and sortie.out == ""''',
     '''    fichier = autre.ctx.sortie / "versement" / J.RUN / "calcul-interrompu" / "arret.json"
    assert code == 3 and sortie.err == f"ARRÊT : EgaliteDirectionLue ; fichier d'arrêt : {fichier}\\n" and sortie.out == ""
    assert json.loads(fichier.read_text(encoding="utf-8"))["motif"].startswith(st.MESSAGE_EGALITE_LUE)'''))}

if len(sys.argv) > 2:
    essais = Path(sys.argv[2])
    for origine, copie in COPIES:
        t = (essais / origine).read_text(encoding="utf-8")
        for avant, apres in ACCORDS.get(origine, ()):
            assert t.count(avant) == 1, (origine, avant[:70], t.count(avant))
            t = t.replace(avant, apres)
        assert "lanceur_v4" in t, origine
        for avant, apres in NOMS:                   # le fichier des jouets ne se nomme pas lui-même : second nom facultatif
            t = t.replace(avant, apres)
        assert "lanceur_v4" not in t and "jouets_v4" not in t, origine
        (essais / copie).write_text(t, encoding="utf-8")
        print(f"{copie} écrit")
