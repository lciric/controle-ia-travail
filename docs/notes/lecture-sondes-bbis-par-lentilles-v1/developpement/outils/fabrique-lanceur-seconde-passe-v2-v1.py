"""Fabrique lanceur_seconde_passe_v2.py à partir de lanceur_seconde_passe_v1.py par remplacements exacts, chacun trouvé le
nombre de fois dit (une, sauf mention).

Version 2 du lanceur de la seconde passe (corrections après contre-lecture ; mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-seconde-passe-lentilles-v2.md`, `a2132568…` ;
contre-lecture `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-seconde-passe-v1.md`,
`0c90e0f6…`). Ce que les remplacements font, dans l'ordre du fichier :
- B1 : `corpus_pagine_v1` entre dans `MODULES` ; les cibles du corpus des jetons gardés sont prises explicitement de
  `corpus_pagine_v1.cibles_corpus` (comme `lanceur_v8`), le point de branchement des réglages disparaît ;
- B2 : `cache_tokeniseur_v2` entre dans `MODULES` ; le cache du tokeniseur est posé par lui ; un essai du tokeniseur en ligne et
  sans clé suit l'essai hors ligne, puis le cache est relu ; en cas d'échec de cet essai, le cache est relu pour nommer la cause ;
- N5 : la condition de lecture passe par `nos_lentilles_v2` (une seule ligne « Lentille nommée : … » par pièce) ;
- N2, N2 bis, N4 : la tête passe par `phrases_v3` ;
- N3 : une note accompagne la phrase gelée quand le recouvrement des deux moitiés n'est pas calculable.

Emploi :
    python fabrique-lanceur-seconde-passe-v2-v1.py <dossier du paquet> [<dossier des essais>]
- premier argument : `src/controle_ia/lentilles_sondes_bbis` (ou une copie) ; `lanceur_seconde_passe_v2.py` y est écrit ;
- second argument, facultatif : `tests` (ou une copie) ; les jouets et les essais du lanceur de la seconde passe y sont copiés
  sous des noms neufs qui visent `lanceur_seconde_passe_v2` (table `COPIES`), avec les accords dits plus bas.
Aucun fichier existant n'est réécrit : tous les noms écrits sont neufs (R12).
"""
import sys
from pathlib import Path

paquet = Path(sys.argv[1])
s = (paquet / "lanceur_seconde_passe_v1.py").read_text(encoding="utf-8")


def rep(avant: str, apres: str, n: int = 1) -> None:
    global s
    assert s.count(avant) == n, (avant[:70], s.count(avant))
    s = s.replace(avant, apres)


# --- en-tête ---------------------------------------------------------------------------------------------------------------------------
rep('''passe n'a pas de garde d'égalité : elle ne lève aucun des deux arrêts cloisonnés de la première ; le canal est gardé tel quel.
"""''', '''passe n'a pas de garde d'égalité : elle ne lève aucun des deux arrêts cloisonnés de la première ; le canal est gardé tel quel.

Version 2 : corrections demandées par la contre-lecture du code de la seconde passe
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-seconde-passe-v1.md`, `0c90e0f6…` ; mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-seconde-passe-lentilles-v2.md`, `a2132568…`).
Différences avec `lanceur_seconde_passe_v1`, et aucune autre ; aucune ligne de calcul n'est changée :
- **B1** : au montage, les cibles des essais d'un octet du corpus des jetons gardés viennent explicitement de
  `corpus_pagine_v1.cibles_corpus` (qui suit les pages de l'arbre d'un jeu de données), comme dans `lanceur_v8` ; le point de
  branchement des réglages (`Reglages.cibles_corpus`) et l'import paresseux de `montage_v2` ne sont plus employés ;
  `corpus_pagine_v1` entre dans `MODULES`, dont la fiche du code porte les empreintes ;
- **B2** : le cache du tokeniseur est posé par `cache_tokeniseur_v2.poser_cache_tokeniseur` (mêmes fichiers posés, plus les
  marqueurs d'absence vérifiés sur l'arbre du dépôt du modèle lu avec la clé) ; après l'essai hors ligne, un essai charge le
  tokeniseur **en ligne et sans clé**, comme le script du corpus des jetons gardés le fera (`essayer_tokeniseur_en_ligne`,
  recopiée de `lanceur_v9` et complétée), puis le cache est relu sur disque (`cache_tokeniseur_v2.exiger_cache`) ; le rapport du
  montage porte les deux champs neufs `cache_du_tokeniseur` et `essai_du_tokeniseur_en_ligne_sans_cle` ; `cache_tokeniseur_v2`
  entre dans `MODULES` ; **si l'essai en ligne échoue, le cache est relu pour nommer la cause** (branche du dépôt qui a bougé) ;
- **N5** : la condition de lecture est celle de `nos_lentilles_v2` (celle de `nos_lentilles_v1`, plus : une seule ligne
  « Lentille nommée : … » dans la pièce du nœud N12, sinon arrêt) ;
- **N2, N2 bis, N4** : la tête est celle de `phrases_v3` (ligne d'ensemble de la lecture de la seconde course recopiée au premier
  palier, aussi pour une seule lentille, et seulement si cette lecture est inscrite ; phrase de tête de la reproduction exacte
  quand l'état de la première passe a changé depuis le montage : nœud N-dev-9, option (a)) ;
- **N3** : quand le recouvrement des deux moitiés de notre R n'est pas calculable, une note accompagne la phrase gelée qui le
  cite (aucun mot gelé ne change).
`MODULES_DIFFERENTS` : `statistiques_v4` (inchangé) et ce lanceur.
"""''')

# --- les modules neufs : imports, liste de la fiche du code --------------------------------------------------------------------------------
rep('''from . import audits_v2 as au
from . import comparaisons_lentilles_v1 as co
from . import constantes_v1 as K
from . import constantes_v2 as K2
''', '''from . import audits_v2 as au
from . import cache_tokeniseur_v2 as ct
from . import comparaisons_lentilles_v1 as co
from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import corpus_pagine_v1 as cp
''')
rep('''from . import nos_lentilles_v1 as nl
from . import nuls_v1 as nu
from . import phrases_v2 as ph
''', '''from . import nos_lentilles_v1 as nl
from . import nos_lentilles_v2 as n2
from . import nuls_v1 as nu
from . import phrases_v2 as ph
from . import phrases_v3 as p3
''')
rep('''           "audits_v2", "phrases_v1", "phrases_v2", "nos_lentilles_v1", "comparaisons_lentilles_v1", "reproduction_v1",
           "lanceur_v7", "lanceur_seconde_passe_v1")
MODULES_DIFFERENTS = ("statistiques_v4", "lanceur_seconde_passe_v1")
''', '''           "audits_v2", "phrases_v1", "phrases_v2", "phrases_v3", "nos_lentilles_v1", "nos_lentilles_v2",
           "comparaisons_lentilles_v1", "reproduction_v1", "corpus_pagine_v1", "cache_tokeniseur_v2", "lanceur_v7",
           "lanceur_seconde_passe_v2")
MODULES_DIFFERENTS = ("statistiques_v4", "lanceur_seconde_passe_v2")
''')

# --- B1 : plus de point de branchement ; les cibles du corpus viennent de la lecture paginée ----------------------------------------------
rep('''    sha256_piece_meta_s: str = K2.EMPREINTE_PIECE_META_S
    cibles_corpus: object = None                        # point de branchement (nœud N-dev-1) : voir `montage_v2.cibles_du_corpus`
''', '''    sha256_piece_meta_s: str = K2.EMPREINTE_PIECE_META_S
''')
rep('''mo.essais_un_octet(transport, cle, m2.cibles_du_corpus(voisin, transport, r.cibles_corpus))''',
    '''mo.essais_un_octet(transport, cle, cp.cibles_corpus(voisin, transport))''')

# --- N5 : la condition de lecture ------------------------------------------------------------------------------------------------------------
rep('''    return etat, issue, fiche, nl.condition_de_lecture(fiche, etat, ctx.racine_depot)''',
    '''    return etat, issue, fiche, n2.condition_de_lecture(fiche, etat, ctx.racine_depot)''')

# --- B2 : la pose du cache, l'essai en ligne et sans clé, la relecture du cache ----------------------------------------------------------------
rep('''    mo.poser_cache_tokeniseur(hf_home, {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA},
                              r.depot_llama, r.revision_llama)
''', '''    poses = {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA}
    attendus = {n: r.petits[n] for n in poses}
    rapport["cache_du_tokeniseur"] = ct.poser_cache_tokeniseur(transport, cle, hf_home, poses, attendus, r.depot_llama,
                                                               r.revision_llama)
''')
rep('''    rapport["essai_du_tokeniseur_hors_ligne"] = {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}
''', '''    rapport["essai_du_tokeniseur_hors_ligne"] = {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}
    essayer_tokeniseur_en_ligne(ctx, voisin, hf_home, attendus)
    ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)
    rapport["essai_du_tokeniseur_en_ligne_sans_cle"] = {"tenu": True, "journal": JOURNAL_ESSAI_EN_LIGNE}
''')
rep('''"petits fichiers", "tokeniseur lu du cache hors ligne",
''', '''"petits fichiers", "tokeniseur lu du cache hors ligne",
        "fichiers absents du dépôt du modèle vérifiés sur son arbre et marqués absents dans le cache",
        "tokeniseur lu par le voisin, en ligne et sans clé",
''')
rep('''@dataclass
class Charge:
''', '''JOURNAL_ESSAI_EN_LIGNE = "journal-essai-tokeniseur-en-ligne.txt"
CAUSE_CACHE_INCHANGE = ("cache relu sur disque après l'échec : inchangé, la branche principale y désigne toujours la révision du "
                        "texte ; la cause est dans le journal")


def essayer_tokeniseur_en_ligne(ctx, voisin: Path, hf_home: Path, attendus: dict) -> None:
    """Juste après l'essai hors ligne, avant tout flux long : un processus enfant **en ligne et sans clé** charge le tokeniseur
    par le catalogue du voisin et décode un jeton, comme le script du corpus des jetons gardés le fera (fonction recopiée de
    `lanceur_v9`, même script que l'essai hors ligne de `lanceur_v7`). Un échec ici (un fichier ni posé ni marqué absent est
    demandé au dépôt à porte) évite de le découvrir après les flux de poids : arrêt ; nœud.
    Ajout de cette version (contre-lecture du correctif du tokeniseur, correction non bloquante 1) : à l'échec, le cache est
    relu sur disque par `cache_tokeniseur_v2.exiger_cache`, et l'arrêt **nomme la cause** quand la relecture la trouve (la
    bibliothèque a réécrit la branche principale dans le cache : la branche du dépôt a bougé) ; sinon il dit que le cache est
    inchangé. Le message ne porte que des mots du code : ni le journal, ni la clé."""
    r = ctx.reglages
    try:
        mo.jouer_script([ctx.python, "-c", l7.SCRIPT_TOKENISEUR], voisin, mo.environnement_enfant(voisin, hf_home, False, ctx.env),
                        ctx.travail / JOURNAL_ESSAI_EN_LIGNE)
    except Arret:
        try:
            ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)
            cause = CAUSE_CACHE_INCHANGE
        except Arret as relecture:
            cause = f"cause relue dans le cache : « {relecture} »"
        raise Arret(f"le code voisin ne lit pas le tokeniseur en ligne et sans clé ({JOURNAL_ESSAI_EN_LIGNE}) ; {cause} : "
                    "arrêt avant tout flux long ; nœud") from None


@dataclass
class Charge:
''')

# --- N2, N2 bis, N4 : la tête ------------------------------------------------------------------------------------------------------------------
rep('''    tete = ph.tete(conditions, fiche, conditions["course"], bool(etat_registre.presentes(K2.CLE_LECTURE_SECONDE_COURSE)), reproduction,
                   MODULES_DIFFERENTS, issue["phrases_de_tete"], non_tenues)
''', '''    ligne_seconde_course = _ligne_de_la_seconde_course(fiche, conditions["course"], etat_registre)
    tete = p3.tete(conditions, fiche, conditions["course"], bool(etat_registre.presentes(K2.CLE_LECTURE_SECONDE_COURSE)), reproduction,
                   MODULES_DIFFERENTS, issue["phrases_de_tete"], non_tenues, ligne_seconde_course)
''')
rep('''                          "ligne_de_la_lecture_de_la_seconde_course": _ligne_de_la_seconde_course(fiche, conditions["course"], etat_registre),
''', '''                          "ligne_de_la_lecture_de_la_seconde_course": ligne_seconde_course,
''')

# --- N3 : note à côté de la phrase gelée quand le recouvrement des moitiés n'est pas calculable ----------------------------------------------
rep('''def rendre_phrases(tables: dict) -> dict:
''', '''LIBELLES_QUI_CITENT_LES_MOITIES = (co.LECTURE_COMMUNE, co.LECTURE_PROPRE)
NOTE_MOITIES_NON_CALCULABLES = ("recouvrement des deux moitiés de notre R non calculable ({motif}) : dans la phrase gelée, « les deux "
                                "moitiés de notre R : […] sur vingt » porte « non calculable » à la place d'un nombre ; le texte ne "
                                "fixe pas ce cas (note du code, non une phrase gelée)")


def rendre_phrases(tables: dict) -> dict:
''')
rep('''                "renvois": ph.renvois(K2.LENTILLE_NOTRE_R, d["couche"], palier[K2.LENTILLE_NOTRE_R], seconde)})
''', '''                "renvois": ph.renvois(K2.LENTILLE_NOTRE_R, d["couche"], palier[K2.LENTILLE_NOTRE_R], seconde)})
            if c["libelle"] in LIBELLES_QUI_CITENT_LES_MOITIES and e["moities"].get("libelle") == co.NON_CALCULABLE:
                sortie["comparaisons_entre_lentilles"][-1]["note"] = NOTE_MOITIES_NON_CALCULABLES.format(motif=e["moities"].get("motif"))
''')

assert "lanceur_seconde_passe_v1" not in s.replace("`lanceur_seconde_passe_v1`", ""), "une mention de la v1 hors de l'en-tête"
cible = paquet / "lanceur_seconde_passe_v2.py"
assert not cible.exists(), f"{cible} existe déjà (R12)"
cible.write_text(s, encoding="utf-8")

# =============================================================================================================================================
# Jouets et essais du lanceur : copies sous des noms neufs
# =============================================================================================================================================
if len(sys.argv) > 2:
    essais = Path(sys.argv[2])
    COPIES = {"lentilles_sondes_bbis_seconde_passe_jouets_v2.py": "lentilles_sondes_bbis_seconde_passe_jouets_v3.py",
              "test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py": "test_lentilles_sondes_bbis_seconde_passe_lanceur_v2.py"}
    # noms remplacés partout (nombre d'occurrences non fixé) : le monde de la première passe est celui des jouets de la version 9
    # (son réseau simulé sait servir un arbre par pages, et l'arbre du dépôt du modèle y liste les petits fichiers posés)
    NOMS = [("lentilles_sondes_bbis_jouets_v7", "lentilles_sondes_bbis_jouets_v9"), ("J7", "J9"),
            ("lentilles_sondes_bbis_seconde_passe_jouets_v2", "lentilles_sondes_bbis_seconde_passe_jouets_v3"), ("J2", "J3"),
            ("lanceur_seconde_passe_v1", "lanceur_seconde_passe_v2"), ("monde_v7", "monde_v9"), (".v7.", ".v9."), ("v7=m", "v9=m")]
    ACCORDS = {
        "lentilles_sondes_bbis_seconde_passe_jouets_v3.py": [
            # la première passe « faite » est jouée par le lanceur des jouets de la version 9 (celui que l'opérateur lance)
            ("jouée ici par `lanceur_v7`, tables inscrites", "jouée ici par le lanceur des jouets de la version 9, tables inscrites"),
            ("        l7.monter(m.ctx)\n        rendu = l7.calculer(m.ctx, m.entrees, m.registre_bbis)\n",
             "        J9.la.monter(m.ctx)\n        rendu = J9.la.calculer(m.ctx, m.entrees, m.registre_bbis)\n"),
            # B1 : plus de fonction injectée ; le montage suit `corpus_pagine_v1` sur le réseau simulé
            ("        cibles_corpus=mo.cibles_corpus,      # jouet : l'arbre simulé tient en une page ; la version paginée se branche ici\n",
             ""),
            ('''"""Monde miniature de la seconde passe, pour le lanceur `lanceur_seconde_passe_v2` : le monde de la première passe
(`lentilles_sondes_bbis_jouets_v9.monde` : Llama miniature, fausse lentille publique, faux voisin, réseau simulé, sondes
jouets, registres) auquel s'ajoutent de faux fichiers d'ajustement R et S écrits par `torch.save`, la fiche de rangement, la
pièce de `GO-LENTILLES-BBIS-V2`, la fiche du code de la seconde passe et les lignes de la v2 au registre propre.''', '''"""Monde miniature de la seconde passe, pour le lanceur `lanceur_seconde_passe_v2` : le monde de la première passe
(`lentilles_sondes_bbis_jouets_v9.monde` : Llama miniature, fausse lentille publique, faux voisin, réseau simulé qui sert un
arbre par pages, arbre du dépôt du modèle qui liste les petits fichiers posés, sondes jouets, registres) auquel s'ajoutent de
faux fichiers d'ajustement R et S écrits par `torch.save`, la fiche de rangement, la pièce de `GO-LENTILLES-BBIS-V2`, la fiche
du code de la seconde passe et les lignes de la v2 au registre propre.'''),
        ],
        "test_lentilles_sondes_bbis_seconde_passe_lanceur_v2.py": [
            ("repris de `lanceur_v7`. Cas sain et artefact pour chaque garde (R5).\"\"\"",
             "repris de `lanceur_v7`. Cas sain et artefact pour chaque garde (R5).\n\n"
             "Copie des essais de `lanceur_seconde_passe_v1`, accordée à la version 2 (fabrique\n"
             "`docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-seconde-passe-v2-v1.py`) ; les essais\n"
             "des corrections elles-mêmes sont dans `test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py`.\"\"\""),
            # point 6 du mandat : l'essai ne dépend plus de l'ordre (l'attribut du paquet est retiré aussi) ; le lanceur v2
            # n'a plus de point de branchement dans ses réglages
            ('''    monkeypatch.setitem(sys.modules, "controle_ia.lentilles_sondes_bbis.corpus_pagine_v1", None)
''', '''    import controle_ia.lentilles_sondes_bbis as paquet
    monkeypatch.setitem(sys.modules, "controle_ia.lentilles_sondes_bbis.corpus_pagine_v1", None)
    monkeypatch.delattr(paquet, "corpus_pagine_v1", raising=False)     # sinon l'import relatif rend le module déjà chargé
'''),
            ('''    """Nœud du développeur : sans fonction branchée ni module de lecture paginée, rien ne part."""''',
             '''    """`montage_v2.cibles_du_corpus` (gardé pour les jouets, plus appelé par le lanceur v2) : sans fonction branchée ni module
    de lecture paginée, rien ne part. L'essai ne dépend plus de l'ordre des fichiers : l'attribut du paquet est retiré avec
    l'entrée de la table des modules."""'''),
            ("    assert la.Reglages().cibles_corpus is None\n", '    assert not hasattr(la.Reglages(), "cibles_corpus")\n'),
            ('''    assert la.MODULES_DIFFERENTS == ("statistiques_v4", "lanceur_seconde_passe_v2") and "lanceur_v7" in la.MODULES
    assert not {"corpus_pagine_v1", "lanceur_v8"} & set(la.MODULES)
''', '''    assert la.MODULES_DIFFERENTS == ("statistiques_v4", "lanceur_seconde_passe_v2") and "lanceur_v7" in la.MODULES
    assert {"corpus_pagine_v1", "cache_tokeniseur_v2", "nos_lentilles_v2", "phrases_v3"} <= set(la.MODULES)
    assert not {"lanceur_v8", "lanceur_v9", "lanceur_seconde_passe_v1"} & set(la.MODULES)
'''),
        ],
    }
    for origine, copie in COPIES.items():
        t = (essais / origine).read_text(encoding="utf-8")
        for avant, apres in NOMS:
            t = t.replace(avant, apres)
        for avant, apres in ACCORDS[copie]:
            assert t.count(avant) == 1, (copie, avant[:70], t.count(avant))
            t = t.replace(avant, apres)
        assert not (essais / copie).exists(), f"{copie} existe déjà (R12)"
        (essais / copie).write_text(t, encoding="utf-8")
