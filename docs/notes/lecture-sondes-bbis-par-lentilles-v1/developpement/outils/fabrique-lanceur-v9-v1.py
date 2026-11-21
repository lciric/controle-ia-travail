"""Fabrique lanceur_v9.py à partir de lanceur_v8.py par remplacements exacts, chacun trouvé une fois et une seule.

Version 9 du lanceur de la première passe (correctif du tokeniseur pour le script voisin du corpus des jetons gardés ; mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-tokeniseur-act-corpus-v1.md`,
`4420c6df06ff…`) : le cache du tokeniseur est posé par `cache_tokeniseur_v2.poser_cache_tokeniseur`, qui ajoute aux fichiers
posés les marqueurs d'absence des fichiers que le dépôt du modèle ne porte pas (absence vérifiée sur l'arbre du dépôt), et
non plus par `montage_v1.poser_cache_tokeniseur` seul ; un essai du tokeniseur **en ligne et sans clé** suit l'essai hors
ligne, avant tout flux long. Le module neuf entre dans la liste des modules de la fiche du code.

Emploi :
    python fabrique-lanceur-v9-v1.py <dossier du paquet> [<dossier des essais>]
- premier argument : `src/controle_ia/lentilles_sondes_bbis` (ou une copie) ; `lanceur_v9.py` y est écrit ;
- second argument, facultatif : `tests` (ou une copie) ; les fichiers d'essais qui importent `lanceur_v8` (hors le fichier
  des essais du correctif de la pagination, propre à la version 8) y sont copiés sous des noms neufs qui visent `lanceur_v9`
  (table `COPIES`) : remplacements de noms partout (table `NOMS`) ; accords de la table `ACCORDS` (l'arbre du dépôt du modèle
  des jouets liste aussi les petits fichiers et un dossier, comme un arbre de racine ; les essais qui comptaient quatorze
  modules en comptent quinze ; la liste des gardes du rapport du montage porte deux gardes de plus).
Aucun fichier existant n'est réécrit : tous les noms écrits sont neufs (R12).
"""
import sys
from pathlib import Path

paquet = Path(sys.argv[1])
s = (paquet / "lanceur_v8.py").read_text(encoding="utf-8")


def rep(avant: str, apres: str, n: int = 1) -> None:
    global s
    assert s.count(avant) == n, (avant[:70], s.count(avant))
    s = s.replace(avant, apres)


# --- en-tête : les mots qui citent la version -----------------------------------------------------------------------------------------
rep('''de données, et non plus de `montage_v1.cibles_corpus`, qui n'en lit que la première page ; `corpus_pagine_v1` entre dans la
liste des modules dont la fiche du code porte l'empreinte. Aucune ligne de calcul n'est changée.
"""''', '''de données, et non plus de `montage_v1.cibles_corpus`, qui n'en lit que la première page ; `corpus_pagine_v1` entre dans la
liste des modules dont la fiche du code porte l'empreinte. Aucune ligne de calcul n'est changée.

Version 9 : correctif du tokeniseur pour le script voisin du corpus des jetons gardés (mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-tokeniseur-act-corpus-v1.md`, `4420c6df…`).
Seule différence avec `lanceur_v8` : au montage, le cache du tokeniseur est posé par
`cache_tokeniseur_v2.poser_cache_tokeniseur` : mêmes fichiers posés qu'avant, plus le marqueur d'absence de chaque fichier que
la bibliothèque de chargement demande et que le dépôt du modèle ne porte pas, absence vérifiée sur l'arbre du dépôt lu avec la
clé par le lanceur (sans ces marqueurs, le script du corpus, joué en ligne et sans clé, s'arrête sur le refus du dépôt à
porte) ; juste après l'essai hors ligne du tokeniseur, un second essai le charge **en ligne et sans clé**, comme le script du
corpus le fera, puis le cache est relu sur disque ; le rapport du montage porte le relevé du cache et ce second essai ;
`cache_tokeniseur_v2` entre dans la liste des modules dont la fiche du code porte l'empreinte. Aucune ligne de calcul n'est
changée.
"""''')

# --- le module neuf : son import, sa place dans la liste des modules de la fiche du code ---------------------------------------------------
rep('''from . import audits_v1 as au
from . import constantes_v1 as K
''', '''from . import audits_v1 as au
from . import cache_tokeniseur_v2 as ct
from . import constantes_v1 as K
''')
rep('''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "corpus_pagine_v1", "lanceur_v8")''',
    '''"statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "corpus_pagine_v1", "cache_tokeniseur_v2",
           "lanceur_v9")''')

# --- la pose du cache, et l'essai en ligne et sans clé -----------------------------------------------------------------------------------------
rep('''    mo.poser_cache_tokeniseur(hf_home, {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA},
                              r.depot_llama, r.revision_llama)
''', '''    poses = {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA}
    attendus = {n: r.petits[n] for n in poses}
    rapport["cache_du_tokeniseur"] = ct.poser_cache_tokeniseur(transport, cle, hf_home, poses, attendus, r.depot_llama,
                                                               r.revision_llama)
''')
rep('''    rapport["essai_du_tokeniseur_hors_ligne"] = {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}
''', '''    rapport["essai_du_tokeniseur_hors_ligne"] = {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}
    essayer_tokeniseur_en_ligne(ctx, voisin, hf_home)
    ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)
    rapport["essai_du_tokeniseur_en_ligne_sans_cle"] = {"tenu": True, "journal": JOURNAL_ESSAI_EN_LIGNE}
''')
rep('''        "tokeniseur lu du cache par le voisin, hors ligne et sans clé",
''', '''        "tokeniseur lu du cache par le voisin, hors ligne et sans clé",
        "fichiers absents du dépôt du modèle vérifiés sur son arbre et marqués absents dans le cache",
        "tokeniseur lu par le voisin, en ligne et sans clé",
''')
rep('''                    "arrêt avant tout flux long ; nœud") from None


@dataclass
class Charge:''', '''                    "arrêt avant tout flux long ; nœud") from None


JOURNAL_ESSAI_EN_LIGNE = "journal-essai-tokeniseur-en-ligne.txt"


def essayer_tokeniseur_en_ligne(ctx: Contexte, voisin: Path, hf_home: Path) -> None:
    """Juste après l'essai hors ligne, avant tout flux long : un processus enfant **en ligne et sans clé** charge le tokeniseur
    par le catalogue du voisin et décode un jeton, comme le script du corpus des jetons gardés le fera. Un échec ici (un fichier
    ni posé ni marqué absent est demandé au dépôt à porte) évite de le découvrir après les flux de poids : arrêt ; nœud."""
    try:
        mo.jouer_script([ctx.python, "-c", SCRIPT_TOKENISEUR], voisin, mo.environnement_enfant(voisin, hf_home, False, ctx.env),
                        ctx.travail / JOURNAL_ESSAI_EN_LIGNE)
    except Arret:
        raise Arret(f"le code voisin ne lit pas le tokeniseur en ligne et sans clé ({JOURNAL_ESSAI_EN_LIGNE}) : "
                    "arrêt avant tout flux long ; nœud") from None


@dataclass
class Charge:''')

(paquet / "lanceur_v9.py").write_text(s, encoding="utf-8")
print("lanceur_v9.py écrit")

# --- copies des essais qui importent lanceur_v8, sous des noms neufs qui visent lanceur_v9 ---------------------------------------------------
COPIES = (("lentilles_sondes_bbis_jouets_v8.py", "lentilles_sondes_bbis_jouets_v9.py"),
          ("test_lentilles_sondes_bbis_addendum_concentration_v6.py", "test_lentilles_sondes_bbis_addendum_concentration_v7.py"),
          ("test_lentilles_sondes_bbis_corrections_contre_lecture_v7.py", "test_lentilles_sondes_bbis_corrections_contre_lecture_v8.py"),
          ("test_lentilles_sondes_bbis_garde_egalite_v5.py", "test_lentilles_sondes_bbis_garde_egalite_v6.py"),
          ("test_lentilles_sondes_bbis_gardes_non_vues_v7.py", "test_lentilles_sondes_bbis_gardes_non_vues_v8.py"),
          ("test_lentilles_sondes_bbis_montage_v8.py", "test_lentilles_sondes_bbis_montage_v9.py"),
          ("test_lentilles_sondes_bbis_procedure_v8.py", "test_lentilles_sondes_bbis_procedure_v9.py"),
          ("test_lentilles_sondes_bbis_lanceur_v8_v1.py", "test_lentilles_sondes_bbis_lanceur_v9_v1.py"),
          ("test_lentilles_sondes_bbis_lanceur_v8_interruptions_v1.py", "test_lentilles_sondes_bbis_lanceur_v9_interruptions_v1.py"),
          ("test_lentilles_sondes_bbis_lanceur_v8_garde_arret_present_v1.py",
           "test_lentilles_sondes_bbis_lanceur_v9_garde_arret_present_v1.py"))
NOMS = (("lanceur_v8", "lanceur_v9"), ("lentilles_sondes_bbis_jouets_v8", "lentilles_sondes_bbis_jouets_v9"))
ACCORDS = {
    # L'arbre du dépôt du modèle des jouets devient un arbre de racine : les petits fichiers y figurent (le module neuf exige
    # que chaque fichier posé dans le cache y soit, témoin de la lecture), avec un dossier (qui porte, dans le dépôt réel, le
    # fichier que la bibliothèque de chargement cherche à la racine).
    "lentilles_sondes_bbis_jouets_v8.py": (
        ('''                    [{"type": "file", "path": f, "oid": r.poids[f][1], "size": len(c), "lfs": {"oid": sha(c), "size": len(c)}}
                     for f, c in poids.items()]).encode()}''',
         '''                    [{"type": "file", "path": f, "oid": r.poids[f][1], "size": len(c), "lfs": {"oid": sha(c), "size": len(c)}}
                     for f, c in poids.items()]
                    + [{"type": "file", "path": n, "oid": mo.identifiant_git(c), "size": len(c)} for n, c in petits.items()]
                    + [{"type": "directory", "path": "original", "oid": "0" * 40, "size": 0}]).encode()}'''),),
    "test_lentilles_sondes_bbis_lanceur_v8_v1.py": (
        # Treize modules à la version 4, quinze à la version 9 : les modules des deux correctifs, à côté du nom du lanceur.
        ('''    assert set(v4.manifeste["code"]) ^ set(v5.manifeste["code"]) == {"lanceur_v4.py", "lanceur_v8.py", "corpus_pagine_v1.py"}''',
         '''    assert set(v4.manifeste["code"]) ^ set(v5.manifeste["code"]) == {"lanceur_v4.py", "lanceur_v8.py", "corpus_pagine_v1.py",
                                                                      "cache_tokeniseur_v2.py"}'''),
        ('''    assert len(la4.MODULES) == 13 and len(la.MODULES) == 14
    assert la.MODULES == la4.MODULES[:-1] + ("corpus_pagine_v1", "lanceur_v8") and la4.MODULES[-1] == "lanceur_v4"''',
         '''    assert len(la4.MODULES) == 13 and len(la.MODULES) == 15
    assert la.MODULES == la4.MODULES[:-1] + ("corpus_pagine_v1", "cache_tokeniseur_v2", "lanceur_v8")
    assert la4.MODULES[-1] == "lanceur_v4"'''),
        # La fiche à la liste de la version 4 manque de trois empreintes, lues dans l'ordre de la liste des modules : le module
        # du correctif de la pagination, celui du correctif du tokeniseur, puis le lanceur (objet de l'essai repris).
        ('''    J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers=fichiers_v4)        # avec le module du correctif : il manque le lanceur
''',
         '''    J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers=fichiers_v4)        # il manque le module du second correctif
    with pytest.raises(Refus, match=r"cache_tokeniseur_v2\\.py : empreinte absente de la fiche"):
        la.exiger_fiche_code(tmp_path / "depot", propre)
    fichiers_v4[f"{la.CHEMIN_PAQUET}/cache_tokeniseur_v2.py"] = J.sha((PAQUET / "cache_tokeniseur_v2.py").read_bytes())
    J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers=fichiers_v4)        # avec les modules des correctifs : il manque le lanceur
'''),
        # Rapport du montage : la liste des gardes de la version 9 est celle de la version 4 plus les deux gardes du correctif
        # du tokeniseur ; le reste est comparé comme avant.
        ('''    for cle in ("gardes", "jetons_gardes", "lignes_de_sortie_egales", "garde_fonction_lecture", "graines", "texte", "addendum", "poids",
                "petits_fichiers"):
        assert v4.montage[cle] == v5.montage[cle], cle''',
         '''    for cle in ("jetons_gardes", "lignes_de_sortie_egales", "garde_fonction_lecture", "graines", "texte", "addendum", "poids",
                "petits_fichiers"):
        assert v4.montage[cle] == v5.montage[cle], cle
    neuves = ["fichiers absents du dépôt du modèle vérifiés sur son arbre et marqués absents dans le cache",
              "tokeniseur lu par le voisin, en ligne et sans clé"]
    assert v5.montage["gardes"]["toutes_tenues"] is v4.montage["gardes"]["toutes_tenues"] is True
    assert [g for g in v5.montage["gardes"]["liste"] if g not in neuves] == v4.montage["gardes"]["liste"]
    assert [g for g in v5.montage["gardes"]["liste"] if g in neuves] == neuves and set(v5.montage["gardes"]) == {"toutes_tenues", "liste"}'''))}

if len(sys.argv) > 2:
    essais = Path(sys.argv[2])
    for origine, copie in COPIES:
        t = (essais / origine).read_text(encoding="utf-8")
        for avant, apres in ACCORDS.get(origine, ()):
            assert t.count(avant) == 1, (origine, avant[:70], t.count(avant))
            t = t.replace(avant, apres)
        assert "lanceur_v8" in t, origine
        for avant, apres in NOMS:                   # le fichier des jouets ne se nomme pas lui-même : second nom facultatif
            t = t.replace(avant, apres)
        assert "lanceur_v8" not in t and "jouets_v8" not in t, origine
        (essais / copie).write_text(t, encoding="utf-8")
        print(f"{copie} écrit")
