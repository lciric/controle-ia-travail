"""Fabrique lanceur_v7.py à partir de lanceur_v6.py par remplacements exacts, chacun trouvé une fois et une seule.

Version 7 du lanceur de la première passe (mot de Lazar, GO-2026-11-21-06) : une garde neuve au départ de la sous-commande
`calcul`. Si un `arret.json` existe déjà au chemin où l'arrêt de cette course serait écrit
(`<sortie>/versement/<run>/calcul-interrompu/arret.json`), le lanceur refuse de partir : rien n'est écrit, rien n'est
supprimé. Les mots fixes de la ligne affichée pour un arrêt cloisonné sont gardés tels quels.

Emploi :
    python fabrique-lanceur-v7-v1.py <dossier du paquet> [<dossier des essais>]
- premier argument : `src/controle_ia/lentilles_sondes_bbis` (ou une copie) ; `lanceur_v7.py` y est écrit ;
- second argument, facultatif : `tests` (ou une copie) ; les fichiers d'essais qui importent `lanceur_v6` y sont copiés sous
  des noms neufs qui visent `lanceur_v7` (table `COPIES`) : deux remplacements de noms partout ; pour le fichier des essais
  du lanceur, l'accord de la table `ACCORDS` (le seul essai qui relançait le calcul sur un `arret.json` déjà présent) ; pour
  le fichier des interruptions, le retrait de ses deux derniers essais (fabrique et lignes retirées), repris dans le fichier
  neuf des essais de la version 7.
Aucun fichier existant n'est réécrit : tous les noms écrits sont neufs (R12).
"""
import sys
from pathlib import Path

paquet = Path(sys.argv[1])
s = (paquet / "lanceur_v6.py").read_text(encoding="utf-8")


def rep(avant: str, apres: str, n: int = 1) -> None:
    global s
    assert s.count(avant) == n, (avant[:70], s.count(avant))
    s = s.replace(avant, apres)


# --- en-tête : les mots qui citent la version -----------------------------------------------------------------------------------------
rep('''mots fixes de la ligne affichée sont inchangés, et tenus par des constantes. Aucune ligne de calcul n'est changée.
"""''', '''mots fixes de la ligne affichée sont inchangés, et tenus par des constantes. Aucune ligne de calcul n'est changée.

Version 7 : garde du fichier d'arrêt déjà présent (mot de Lazar, GO-2026-11-21-06 ; nœud 2 de la contre-lecture `d821cf66…`).
Seule différence avec `lanceur_v6` : au départ de la sous-commande `calcul`, avant toute lecture de registre, toute requête,
tout chargement et tout calcul, `exiger_aucun_fichier_d_arret` arrête si un `arret.json` existe déjà au chemin où l'arrêt de
cette course serait écrit (`<sortie>/versement/<run>/calcul-interrompu/arret.json`) : la règle de non-réécriture (R12) y
ferait perdre le message d'un second arrêt. Rien n'est écrit, rien n'est supprimé. Ce n'est pas un arrêt cloisonné : son
message ne porte que le chemin et sort comme celui des autres arrêts. Les mots fixes de la ligne affichée sont gardés tels
quels. Aucune ligne de calcul n'est changée.
"""''')

# --- liste des modules de la fiche du code : le lanceur lui-même ------------------------------------------------------------------------
rep('''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v6")''',
    '''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v7")''')

# --- la garde, et son appel au départ de l'enveloppe du calcul ------------------------------------------------------------------------------
rep('''def calculer(ctx: Contexte, racine_entrees: Path, registre_bbis: Path, nettoyage: bool = True) -> dict:
''', '''def chemin_du_fichier_d_arret(ctx: Contexte) -> Path:
    """Le chemin où l'arrêt d'une course est écrit par l'enveloppe du calcul."""
    return ctx.sortie / "versement" / ctx.run / "calcul-interrompu" / "arret.json"


def exiger_aucun_fichier_d_arret(ctx: Contexte) -> None:
    """Garde de la version 7 (GO-2026-11-21-06) : un `arret.json` existe déjà au chemin où l'arrêt de cette course serait
    écrit : rien ne part. Rien n'est écrit, rien n'est supprimé. Sans elle, un second arrêt dans le même dossier de sortie ne
    pourrait pas écrire son message (R12 : on n'écrase pas). Arrêt ordinaire, non cloisonné : son message ne porte que le chemin."""
    fichier = chemin_du_fichier_d_arret(ctx)
    if fichier.exists() or fichier.is_symlink():
        raise Arret(f"un fichier d'arrêt existe déjà pour cette course ({fichier}) : rien ne part ; rien n'est écrit, rien n'est "
                    "supprimé")


def calculer(ctx: Contexte, racine_entrees: Path, registre_bbis: Path, nettoyage: bool = True) -> dict:
''')
rep('''    `verser_arret_cloisonne`, puis relevé tel quel, pour l'appelant Python ; son message ne sort que dans `arret.json`."""
    tableaux: dict[str, np.ndarray] = {}
''', '''    `verser_arret_cloisonne`, puis relevé tel quel, pour l'appelant Python ; son message ne sort que dans `arret.json`.
    Version 7 : avant tout, la garde du fichier d'arrêt déjà présent (`exiger_aucun_fichier_d_arret`), hors de l'enveloppe."""
    exiger_aucun_fichier_d_arret(ctx)
    tableaux: dict[str, np.ndarray] = {}
''')

(paquet / "lanceur_v7.py").write_text(s, encoding="utf-8")
print("lanceur_v7.py écrit")

# --- copies des essais qui importent lanceur_v6, sous des noms neufs qui visent lanceur_v7 ---------------------------------------------------
COPIES = (("lentilles_sondes_bbis_jouets_v6.py", "lentilles_sondes_bbis_jouets_v7.py"),
          ("test_lentilles_sondes_bbis_addendum_concentration_v4.py", "test_lentilles_sondes_bbis_addendum_concentration_v5.py"),
          ("test_lentilles_sondes_bbis_corrections_contre_lecture_v5.py", "test_lentilles_sondes_bbis_corrections_contre_lecture_v6.py"),
          ("test_lentilles_sondes_bbis_garde_egalite_v3.py", "test_lentilles_sondes_bbis_garde_egalite_v4.py"),
          ("test_lentilles_sondes_bbis_gardes_non_vues_v5.py", "test_lentilles_sondes_bbis_gardes_non_vues_v6.py"),
          ("test_lentilles_sondes_bbis_montage_v6.py", "test_lentilles_sondes_bbis_montage_v7.py"),
          ("test_lentilles_sondes_bbis_procedure_v6.py", "test_lentilles_sondes_bbis_procedure_v7.py"),
          ("test_lentilles_sondes_bbis_lanceur_v6_v1.py", "test_lentilles_sondes_bbis_lanceur_v7_v1.py"),
          ("test_lentilles_sondes_bbis_lanceur_v6_interruptions_v1.py", "test_lentilles_sondes_bbis_lanceur_v7_interruptions_v1.py"))
NOMS = (("lanceur_v6", "lanceur_v7"), ("lentilles_sondes_bbis_jouets_v6", "lentilles_sondes_bbis_jouets_v7"))
# Le seul essai repris qui relançait le calcul sur un `arret.json` déjà présent : la garde de la version 7 refuse désormais
# cette relance (essai neuf). L'essai repris garde la défense du versement : le fichier apparu après la garde du départ.
ACCORDS = {"test_lentilles_sondes_bbis_lanceur_v6_v1.py": (
    ('''    """Échec non simulé : le calcul est relancé après un premier arrêt, dans le même dossier de sortie. Rien n'est réécrit
    (R12) : le premier `arret.json` reste, entier ; la seconde sortie d'erreur dit par des mots fixes que le fichier d'arrêt
    n'a pas été écrit et que le versement a échoué, sans un mot du message."""''',
     '''    """Échec non simulé, défense du versement : un `arret.json` et un versement sont déjà là quand le second arrêt est versé,
    comme s'ils étaient apparus après la garde du départ (version 7 : la garde, qui refuse la relance, est ici mise de côté ;
    elle a son propre fichier d'essais). Rien n'est réécrit (R12) : le premier `arret.json` reste, entier ; la seconde sortie
    d'erreur dit par des mots fixes que le fichier d'arrêt n'a pas été écrit et que le versement a échoué, sans un mot du message."""'''),
    ('''    empreinte = verifier(d.fichier)
    monkeypatch.setattr(la, "_calculer", _faux_calcul(cas.arret()))
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, None, echec=True)''',
     '''    empreinte = verifier(d.fichier)
    monkeypatch.setattr(la, "_calculer", _faux_calcul(cas.arret()))
    monkeypatch.setattr(la, "exiger_aucun_fichier_d_arret", lambda ctx: None)       # le fichier apparu après la garde du départ
    code, sortie = _ligne_de_commande(la, d, capsys)
    _exiger_ligne_cloisonnee(code, sortie, cas, None, echec=True)'''))}
COUPES = {"test_lentilles_sondes_bbis_lanceur_v6_interruptions_v1.py":
          "\n\n# --- la version 6 est la version 5 plus cette seule correction "}

if len(sys.argv) > 2:
    essais = Path(sys.argv[2])
    for origine, copie in COPIES:
        t = (essais / origine).read_text(encoding="utf-8")
        for avant, apres in ACCORDS.get(origine, ()):
            assert t.count(avant) == 1, (origine, avant[:70], t.count(avant))
            t = t.replace(avant, apres)
        if origine in COUPES:
            assert t.count(COUPES[origine]) == 1, origine
            t = t[:t.index(COUPES[origine])].rstrip("\n") + "\n"
        assert "lanceur_v6" in t, origine
        for avant, apres in NOMS:                   # le fichier des jouets ne se nomme pas lui-même : second nom facultatif
            t = t.replace(avant, apres)
        assert "lanceur_v6" not in t and "jouets_v6" not in t, origine
        (essais / copie).write_text(t, encoding="utf-8")
        print(f"{copie} écrit")
