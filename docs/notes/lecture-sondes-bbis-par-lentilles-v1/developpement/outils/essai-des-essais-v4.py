"""Essai des essais du lanceur de la première passe, version 5 (messages d'arrêt cloisonnés) : douze altérations de
`lanceur_v5.py`, une à la fois, chacune sur une copie jetable de l'arbre ; les essais du cas sain doivent voir chacune.

Emploi :
    python essai-des-essais-v4.py <racine du dépôt> <dossier jetable, hors du dépôt> [<nom d'une altération>]
Sans troisième argument, la liste des noms est imprimée, un par ligne (à passer un à un, en parallèle si l'on veut) ; le
premier, `temoin-sans-alteration`, est le cas sain de cet outil : la même copie, sans altération, où aucun essai ne doit tomber.
Pour chaque altération : `src/`, les fichiers d'essais du paquet, la copie versée de `readout.py` et l'outil de fabrique sont
copiés sous `<dossier jetable>/alterations/<nom>/` ; `lanceur_v5.py` y est altéré par un remplacement exact, trouvé une fois et
une seule ; `tests/test_lentilles_sondes_bbis_lanceur_v5_v1.py` y est joué sans ses essais d'artefact (ils éprouvent des copies
jetables qui défont déjà une ligne) et sans les deux essais qui comparent le fichier à l'octet (ils voient toute altération).
Rien n'est écrit dans le dépôt. Une ligne par altération : « VUE » si au moins un essai tombe, « NON VUE » sinon, le décompte
de pytest, et les noms des essais tombés ; pour le témoin : « SAIN » si aucun essai ne tombe, « TÉMOIN EN ÉCHEC » sinon.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = "tests/test_lentilles_sondes_bbis_lanceur_v5_v1.py"
READOUT = "docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-readout.py.txt"
OUTIL = "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-v5-v1.py"
TRI = ('        print(f"ARRÊT : {e}" if nom_d_arret_cloisonne(e) is None else ligne_d_arret_cloisonne(e), file=sys.stderr)\n')
BRANCHE = ('        if nom_d_arret_cloisonne(arret) is not None:\n'
           '            verser_arret_cloisonne(ctx, arret, tableaux, etat["parti"])\n'
           '            raise\n')
ALTERATIONS = {
    # la ligne de commande imprime le message entier, comme la version 4
    "a-ligne-de-commande-imprime-le-message": (TRI, '        print(f"ARRÊT : {e}", file=sys.stderr)\n'),
    # l'enveloppe du calcul est celle de la version 4 (message enchaîné à l'échec du versement ; rien d'écrit avant le départ)
    "b-enveloppe-de-la-version-4": (BRANCHE, ''),
    # une interruption pendant le versement garde l'arrêt dans sa chaîne : la trace porte le message
    "c-interruption-enchainee": ("        raise e from None\n", "        raise\n"),
    # le fichier d'arrêt ne porte que le nom de l'arrêt
    "d-motif-reduit-au-nom": ('"motif": str(arret), "morceaux": [], "travail": None}',
                              '"motif": nom_d_arret_cloisonne(arret), "morceaux": [], "travail": None}'),
    # à l'échec du versement, la ligne affichée reprend le message
    "e-ligne-porte-le-message-en-cas-d-echec": (
        '        ligne += " ; versement à l\'arrêt en échec : rien n\'est supprimé"\n',
        '        ligne += f" ; versement à l\'arrêt en échec ({arret}) : rien n\'est supprimé"\n'),
    # l'arrêt des directions nulles n'est plus cloisonné
    "f-arret-des-directions-nulles-oublie": (
        'ARRETS_CLOISONNES = ((st.EgaliteDirectionLue, "EgaliteDirectionLue"), (st.EgaliteNulleDecisive, "EgaliteNulleDecisive"))',
        'ARRETS_CLOISONNES = ((st.EgaliteDirectionLue, "EgaliteDirectionLue"),)'),
    # avant le départ du calcul, un arrêt cloisonné n'écrit pas son fichier d'arrêt
    "g-avant-le-depart-rien-n-est-ecrit": (BRANCHE, BRANCHE.replace('is not None:', 'is not None and etat["parti"]:')),
    # un échec du versement qui n'est pas un arrêt (erreur du disque) n'est plus attrapé
    "h-echec-du-versement-non-attrape": ("        except Exception as e:\n            arret.versement_en_echec = True\n",
                                         "        except Arret as e:\n            arret.versement_en_echec = True\n"),
    # un fichier d'arrêt impossible à écrire lève une erreur du système (trace)
    "i-fichier-non-ecrit-leve": ("    except Exception:\n        arret.fichier_d_arret = None",
                                 "    except Arret:\n        arret.fichier_d_arret = None"),
    # l'échec du versement n'est plus dit sur la ligne de commande
    "j-echec-du-versement-tu": ("            arret.versement_en_echec = True\n", "            arret.versement_en_echec = False\n"),
    # le chemin du fichier d'arrêt n'est plus donné
    "k-chemin-du-fichier-tu": ('    ligne += f"fichier d\'arrêt : {fichier}" if fichier is not None else "fichier d\'arrêt non écrit"\n',
                               '    ligne += "fichier d\'arrêt non écrit"\n'),
    # le nom de l'arrêt est remplacé par le message nommé de la liste d'arrêt (un mot du message)
    "l-nom-remplace-par-le-message-nomme": ('    ligne = f"ARRÊT : {nom_d_arret_cloisonne(arret)} ; "\n',
                                            '    ligne = f"ARRÊT : {str(arret).split(\' : \')[0]} ; "\n'),
}

TEMOIN = "temoin-sans-alteration"
if len(sys.argv) < 4:
    print("\n".join([TEMOIN, *ALTERATIONS]))
    sys.exit(0)

racine, jetable, nom = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), sys.argv[3]
assert racine not in jetable.parents and jetable != racine, "le dossier jetable est hors du dépôt"
avant, apres = ALTERATIONS[nom] if nom != TEMOIN else ("", "")
d = jetable / "alterations" / nom
d.mkdir(parents=True)
shutil.copytree(racine / "src", d / "src", ignore=shutil.ignore_patterns("__pycache__"))
(d / "tests").mkdir()
for f in sorted((racine / "tests").glob("*lentilles_sondes_bbis*.py")) + [racine / "tests" / "conftest.py"]:
    shutil.copy(f, d / "tests" / f.name)
for chemin in (READOUT, OUTIL):
    (d / chemin).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(racine / chemin, d / chemin)
p = d / "src/controle_ia/lentilles_sondes_bbis/lanceur_v5.py"
s = p.read_text(encoding="utf-8")
if nom != TEMOIN:
    assert s.count(avant) == 1, (nom, s.count(avant))
    p.write_text(s.replace(avant, apres), encoding="utf-8")
r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", ESSAIS, "-k", "not test_artefact",
                    "--deselect", f"{ESSAIS}::test_l_outil_de_fabrique_rejoue_rend_le_lanceur_de_la_version_5_a_l_octet_pres",
                    "--deselect", f"{ESSAIS}::test_aucune_ligne_de_calcul_changee_depuis_la_version_4"],
                   cwd=d, capture_output=True, text=True, env=os.environ | {"PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1"})
lignes = r.stdout.strip().splitlines()
tombes = sorted({l.split("::")[1].split(" ")[0].split("[")[0] for l in lignes if l.startswith("FAILED")})
if nom == TEMOIN:
    verdict = "SAIN" if r.returncode == 0 and not tombes else "TÉMOIN EN ÉCHEC"
else:
    verdict = "VUE" if r.returncode == 1 and tombes else "NON VUE"
print(f"{nom} : {verdict} | {lignes[-1] if lignes else r.stderr[-300:]} | {', '.join(tombes)}")
