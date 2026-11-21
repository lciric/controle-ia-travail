"""Fabrique lanceur_v8.py à partir de lanceur_v7.py par remplacements exacts, chacun trouvé une fois et une seule.

Version 8 du lanceur de la première passe (correctif de la pagination de l'arbre du corpus ; mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-pagination-corpus-v1.md`,
`c0c07faaaa36adb1f6d45f2066d337711d6fdc849d7fb916e3253f223f15b96f`) : les cibles des essais d'un octet du corpus des jetons
gardés viennent de `corpus_pagine_v1.cibles_corpus`, qui suit les pages de l'arbre d'un jeu de données, et non plus de
`montage_v1.cibles_corpus`, qui n'en lit que la première. Le module neuf entre dans la liste des modules de la fiche du code.

Emploi :
    python fabrique-lanceur-v8-v1.py <dossier du paquet> [<dossier des essais>]
- premier argument : `src/controle_ia/lentilles_sondes_bbis` (ou une copie) ; `lanceur_v8.py` y est écrit ;
- second argument, facultatif : `tests` (ou une copie) ; les fichiers d'essais qui importent `lanceur_v7` y sont copiés sous
  des noms neufs qui visent `lanceur_v8` (table `COPIES`) : remplacements de noms partout (table `NOMS`) ; accords de la table
  `ACCORDS` (le transport simulé des jouets reçoit la lecture d'une page ; les essais qui comptaient treize modules en comptent
  quatorze) ; pour le fichier de la garde du fichier d'arrêt, le retrait de ses deux derniers essais (fabrique de la version 7
  rejouée, lignes retirées de la version 6 à la version 7), dont les pareils pour la version 8 sont dans le fichier neuf des
  essais du correctif.
Aucun fichier existant n'est réécrit : tous les noms écrits sont neufs (R12).
"""
import sys
from pathlib import Path

paquet = Path(sys.argv[1])
s = (paquet / "lanceur_v7.py").read_text(encoding="utf-8")


def rep(avant: str, apres: str, n: int = 1) -> None:
    global s
    assert s.count(avant) == n, (avant[:70], s.count(avant))
    s = s.replace(avant, apres)


# --- en-tête : les mots qui citent la version -----------------------------------------------------------------------------------------
rep('''message ne porte que le chemin et sort comme celui des autres arrêts. Les mots fixes de la ligne affichée sont gardés tels
quels. Aucune ligne de calcul n'est changée.
"""''', '''message ne porte que le chemin et sort comme celui des autres arrêts. Les mots fixes de la ligne affichée sont gardés tels
quels. Aucune ligne de calcul n'est changée.

Version 8 : correctif de la pagination de l'arbre du corpus (mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-pagination-corpus-v1.md`, `c0c07faa…`).
Seule différence avec `lanceur_v7` : au montage, les cibles des essais d'un octet du corpus des jetons gardés viennent de
`corpus_pagine_v1.cibles_corpus`, qui suit les pages de l'arbre d'un jeu de données jusqu'à la première qui porte un fichier
de données, et non plus de `montage_v1.cibles_corpus`, qui n'en lit que la première page ; `corpus_pagine_v1` entre dans la
liste des modules dont la fiche du code porte l'empreinte. Aucune ligne de calcul n'est changée.
"""''')

# --- le module neuf : son import, sa place dans la liste des modules de la fiche du code ---------------------------------------------------
rep('''from . import constantes_v1 as K
from . import entrees_v3 as en
''', '''from . import constantes_v1 as K
from . import corpus_pagine_v1 as cp
from . import entrees_v3 as en
''')
rep('''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v7")''',
    '''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "corpus_pagine_v1", "lanceur_v8")''')

# --- le seul appel changé -----------------------------------------------------------------------------------------------------------------------
rep('''    rapport["essais_un_octet"] += mo.essais_un_octet(transport, cle, mo.cibles_corpus(voisin, transport))
''', '''    rapport["essais_un_octet"] += mo.essais_un_octet(transport, cle, cp.cibles_corpus(voisin, transport))
''')

(paquet / "lanceur_v8.py").write_text(s, encoding="utf-8")
print("lanceur_v8.py écrit")

# --- copies des essais qui importent lanceur_v7, sous des noms neufs qui visent lanceur_v8 ---------------------------------------------------
COPIES = (("lentilles_sondes_bbis_jouets_v7.py", "lentilles_sondes_bbis_jouets_v8.py"),
          ("test_lentilles_sondes_bbis_addendum_concentration_v5.py", "test_lentilles_sondes_bbis_addendum_concentration_v6.py"),
          ("test_lentilles_sondes_bbis_corrections_contre_lecture_v6.py", "test_lentilles_sondes_bbis_corrections_contre_lecture_v7.py"),
          ("test_lentilles_sondes_bbis_garde_egalite_v4.py", "test_lentilles_sondes_bbis_garde_egalite_v5.py"),
          ("test_lentilles_sondes_bbis_gardes_non_vues_v6.py", "test_lentilles_sondes_bbis_gardes_non_vues_v7.py"),
          ("test_lentilles_sondes_bbis_montage_v7.py", "test_lentilles_sondes_bbis_montage_v8.py"),
          ("test_lentilles_sondes_bbis_procedure_v7.py", "test_lentilles_sondes_bbis_procedure_v8.py"),
          ("test_lentilles_sondes_bbis_lanceur_v7_v1.py", "test_lentilles_sondes_bbis_lanceur_v8_v1.py"),
          ("test_lentilles_sondes_bbis_lanceur_v7_interruptions_v1.py", "test_lentilles_sondes_bbis_lanceur_v8_interruptions_v1.py"),
          ("test_lentilles_sondes_bbis_lanceur_v7_garde_arret_present_v1.py",
           "test_lentilles_sondes_bbis_lanceur_v8_garde_arret_present_v1.py"))
NOMS = (("lanceur_v7", "lanceur_v8"), ("lentilles_sondes_bbis_jouets_v7", "lentilles_sondes_bbis_jouets_v8"))
ACCORDS = {
    # Le transport simulé apprend à rendre une page et l'adresse de la suivante (`suites` : URL → URL de la page suivante).
    "lentilles_sondes_bbis_jouets_v7.py": (
        ('''        self.appels: list[tuple] = []

    def _contenu(self, url, cle):''',
         '''        self.appels: list[tuple] = []
        self.suites: dict = {}

    def page(self, url):
        """Une page, demandée sans clé, et l'adresse de la page suivante (`suites` : URL → URL de la suivante ; absente : `None`)."""
        self.appels.append(("page", url, False, None, None))
        return self._contenu(url, None), self.suites.get(url)

    def _contenu(self, url, cle):'''),),
    # Treize modules à la version 4, quatorze à la version 8 : le module neuf du correctif, à côté du nom du lanceur.
    "test_lentilles_sondes_bbis_lanceur_v7_v1.py": (
        ('''    assert set(v4.manifeste["code"]) ^ set(v5.manifeste["code"]) == {"lanceur_v4.py", "lanceur_v7.py"}''',
         '''    assert set(v4.manifeste["code"]) ^ set(v5.manifeste["code"]) == {"lanceur_v4.py", "lanceur_v7.py", "corpus_pagine_v1.py"}'''),
        ('''    assert len(la.MODULES) == len(la4.MODULES) == 13
    assert la.MODULES == tuple("lanceur_v7" if m == "lanceur_v4" else m for m in la4.MODULES) and la.MODULES[-1] == "lanceur_v7"''',
         '''    assert len(la4.MODULES) == 13 and len(la.MODULES) == 14
    assert la.MODULES == la4.MODULES[:-1] + ("corpus_pagine_v1", "lanceur_v7") and la4.MODULES[-1] == "lanceur_v4"'''),
        # La fiche à la liste de la version 4 manque de deux empreintes : celle du module du correctif, lue la première, puis
        # celle du lanceur ; l'essai repris garde son objet (le lanceur) en ajoutant d'abord le module du correctif à la fiche.
        ('''    assert la4.exiger_fiche_code(tmp_path / "depot", propre)["sha256"]
    with pytest.raises(Refus, match=r"lanceur_v7\\.py : empreinte absente de la fiche"):''',
         '''    assert la4.exiger_fiche_code(tmp_path / "depot", propre)["sha256"]
    with pytest.raises(Refus, match=r"corpus_pagine_v1\\.py : empreinte absente de la fiche"):
        la.exiger_fiche_code(tmp_path / "depot", propre)
    fichiers_v4[f"{la.CHEMIN_PAQUET}/corpus_pagine_v1.py"] = J.sha((PAQUET / "corpus_pagine_v1.py").read_bytes())
    J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers=fichiers_v4)        # avec le module du correctif : il manque le lanceur
    with pytest.raises(Refus, match=r"lanceur_v7\\.py : empreinte absente de la fiche"):'''))}
COUPES = {"test_lentilles_sondes_bbis_lanceur_v7_garde_arret_present_v1.py":
          "\n\n# --- la version 7 est la version 6 plus cette seule garde "}

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
        assert "lanceur_v7" in t, origine
        for avant, apres in NOMS:                   # le fichier des jouets ne se nomme pas lui-même : second nom facultatif
            t = t.replace(avant, apres)
        assert "lanceur_v7" not in t and "jouets_v7" not in t, origine
        (essais / copie).write_text(t, encoding="utf-8")
        print(f"{copie} écrit")
