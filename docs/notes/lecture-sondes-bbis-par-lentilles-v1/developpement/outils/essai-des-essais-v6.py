"""Essai des essais du lanceur de la première passe, version 7 (garde du fichier d'arrêt déjà présent) :
un témoin sans altération et des altérations de `lanceur_v7.py`, une à la fois, chacune sur une copie jetable de l'arbre ; les
essais du cas sain doivent voir chacune.

Emploi :
    python essai-des-essais-v6.py <racine du dépôt> <dossier jetable, hors du dépôt> [<nom>]
Sans troisième argument, la liste des noms est imprimée, un par ligne ; le premier, `temoin-sans-alteration`, est le cas sain
de cet outil. Pour chaque nom : `src/`, les fichiers d'essais du paquet, la copie versée de `readout.py` et les outils de
fabrique sont copiés sous `<dossier jetable>/alterations/<nom>/` ; `lanceur_v7.py` y est altéré par un remplacement exact,
trouvé une fois et une seule ; les trois fichiers d'essais du lanceur de la version 7 y sont joués, sans leurs essais d'artefact et sans
les essais qui comparent le fichier à l'octet (ils voient toute altération). Rien n'est écrit dans le dépôt. Une ligne par
nom : « VUE » ou « NON VUE » (témoin : « SAIN » ou « TÉMOIN EN ÉCHEC »), le décompte de pytest, les noms des essais tombés.
Les altérations a à q sont celles de l'essai des essais de la version 6 (`essai-des-essais-v5.py`), inchangées ; r à v
touchent la garde de la version 7.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = ("tests/test_lentilles_sondes_bbis_lanceur_v7_v1.py", "tests/test_lentilles_sondes_bbis_lanceur_v7_interruptions_v1.py",
          "tests/test_lentilles_sondes_bbis_lanceur_v7_garde_arret_present_v1.py")
READOUT = "docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-readout.py.txt"
OUTILS = "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils"
TRI = ('        print(f"ARRÊT : {arret}" if nom_d_arret_cloisonne(arret) is None else ligne_d_arret_cloisonne(arret), file=sys.stderr)\n')
PRINCIPAL = ("    except Arret as e:\n"
             "        arret = e                           # version 6 : rien d'autre dans ce bloc ; hors de lui, aucun arrêt n'est « en cours »\n"
             "    if arret is not None:\n" + TRI + "        return 3\n")
ENVELOPPE = ("        try:                                # version 6 : le tri et le versement sous la coupure de l'enchaînement\n"
             "            cloisonne = nom_d_arret_cloisonne(arret) is not None\n"
             "            if cloisonne:\n"
             "                verser_arret_cloisonne(ctx, arret, tableaux, etat[\"parti\"])\n"
             "        except BaseException as e:          # interruption entre l'arrêt et son relevé : sa trace ne porte pas le message\n"
             "            raise e from None\n"
             "        if cloisonne:\n"
             "            raise\n")
ALTERATIONS = {
    "a-ligne-de-commande-imprime-le-message": (TRI, '        print(f"ARRÊT : {arret}", file=sys.stderr)\n'),
    "b-enveloppe-de-la-version-4": ("            cloisonne = nom_d_arret_cloisonne(arret) is not None\n", "            cloisonne = False\n"),
    "c-interruption-du-versement-enchainee": (
        "    except BaseException as e:              # interruption pendant le versement : sa trace ne porte pas le message de l'arrêt\n"
        "        raise e from None\n",
        "    except BaseException as e:              # interruption pendant le versement : sa trace ne porte pas le message de l'arrêt\n"
        "        raise\n"),
    "d-motif-reduit-au-nom": ('"motif": str(arret), "morceaux": [], "travail": None}',
                              '"motif": nom_d_arret_cloisonne(arret), "morceaux": [], "travail": None}'),
    "e-ligne-porte-le-message-en-cas-d-echec": (
        'echec=MOTS_VERSEMENT_EN_ECHEC if getattr(arret, "versement_en_echec", False) else "")',
        'echec=f" ; versement à l\'arrêt en échec ({arret})" if getattr(arret, "versement_en_echec", False) else "")'),
    "f-arret-des-directions-nulles-oublie": (
        'ARRETS_CLOISONNES = ((st.EgaliteDirectionLue, "EgaliteDirectionLue"), (st.EgaliteNulleDecisive, "EgaliteNulleDecisive"))',
        'ARRETS_CLOISONNES = ((st.EgaliteDirectionLue, "EgaliteDirectionLue"),)'),
    "g-avant-le-depart-rien-n-est-ecrit": ("            if cloisonne:\n                verser_arret_cloisonne(",
                                           "            if cloisonne and etat[\"parti\"]:\n                verser_arret_cloisonne("),
    "h-echec-du-versement-non-attrape": ("            except Exception as e:\n                arret.versement_en_echec = True\n",
                                         "            except Arret as e:\n                arret.versement_en_echec = True\n"),
    "i-fichier-non-ecrit-leve": ("        except Exception:\n            pass", "        except Arret:\n            pass"),
    "j-echec-du-versement-tu": ("                arret.versement_en_echec = True\n", "                arret.versement_en_echec = False\n"),
    "k-chemin-du-fichier-tu": ('MOTS_FICHIER_D_ARRET_ECRIT = "fichier d\'arrêt : {chemin}"', 'MOTS_FICHIER_D_ARRET_ECRIT = "fichier d\'arrêt non écrit"'),
    "l-nom-remplace-par-le-message-nomme": ("        nom=nom_d_arret_cloisonne(arret),\n", "        nom=str(arret).split(' : ')[0],\n"),
    # les corrections de la version 6, défaites une à une
    "m-ligne-de-commande-traitee-dans-le-bloc-except": (PRINCIPAL, "    except Arret as arret:\n" + TRI + "        return 3\n"),
    "n-enveloppe-sans-coupure": (ENVELOPPE, "        cloisonne = nom_d_arret_cloisonne(arret) is not None\n        if cloisonne:\n"
                                            "            verser_arret_cloisonne(ctx, arret, tableaux, etat[\"parti\"])\n            raise\n"),
    "o-coupure-de-l-enveloppe-sans-from-none": ("            raise e from None\n        if cloisonne:\n", "            raise\n        if cloisonne:\n"),
    "p-premiere-ligne-du-versement-hors-du-bloc": (
        "    try:                                    # version 6 : rien de cette fonction n'est hors de la coupure, première ligne comprise\n"
        "        arret.fichier_d_arret, arret.versement_en_echec = None, False\n",
        "    arret.fichier_d_arret, arret.versement_en_echec = None, False\n    try:\n"),
    # la garde de la version 7
    "r-garde-non-appelee": ("    exiger_aucun_fichier_d_arret(ctx)\n", ""),
    "s-garde-sur-un-autre-chemin": ('    return ctx.sortie / "versement" / ctx.run / "calcul-interrompu" / "arret.json"',
                                    '    return ctx.sortie / "versement" / ctx.run / "arret.json"'),
    "t-lien-casse-non-vu": ("    if fichier.exists() or fichier.is_symlink():\n", "    if fichier.exists():\n"),
    "u-garde-qui-supprime-le-fichier-et-laisse-partir": (
        "    if fichier.exists() or fichier.is_symlink():\n        raise Arret(",
        "    if fichier.exists() or fichier.is_symlink():\n        fichier.unlink()\n    if False:\n        raise Arret("),
    "v-garde-appelee-dans-l-enveloppe-apres-le-calcul": (
        "    exiger_aucun_fichier_d_arret(ctx)\n    tableaux: dict[str, np.ndarray] = {}\n    etat = {\"parti\": False}\n    try:\n"
        "        return _calculer(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat)\n",
        "    tableaux: dict[str, np.ndarray] = {}\n    etat = {\"parti\": False}\n    try:\n"
        "        rendu = _calculer(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat)\n"
        "        exiger_aucun_fichier_d_arret(ctx)\n        return rendu\n"),
    "q-gabarit-de-la-ligne-change": ('LIGNE_ARRET_CLOISONNE = "ARRÊT : {nom} ; {fichier}{echec}"', 'LIGNE_ARRET_CLOISONNE = "ARRÊT : {nom} {fichier}{echec}"'),
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
(d / READOUT).parent.mkdir(parents=True, exist_ok=True)
shutil.copy(racine / READOUT, d / READOUT)
(d / OUTILS).mkdir(parents=True)
for f in sorted((racine / OUTILS).glob("fabrique-lanceur-v*.py")):
    shutil.copy(f, d / OUTILS / f.name)
p = d / "src/controle_ia/lentilles_sondes_bbis/lanceur_v7.py"
s = p.read_text(encoding="utf-8")
if nom != TEMOIN:
    assert s.count(avant) == 1, (nom, s.count(avant))
    p.write_text(s.replace(avant, apres), encoding="utf-8")
r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *ESSAIS, "-k", "not test_artefact",
                    "--deselect", f"{ESSAIS[2]}::test_l_outil_de_fabrique_rejoue_rend_le_lanceur_de_la_version_7_a_l_octet_pres",
                    "--deselect", f"{ESSAIS[2]}::test_lignes_de_la_version_6_toutes_gardees_hors_les_mots_de_version"],
                   cwd=d, capture_output=True, text=True, env=os.environ | {"PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1"})
lignes = r.stdout.strip().splitlines()
tombes = sorted({l.split("::")[1].split(" ")[0].split("[")[0] for l in lignes if l.startswith("FAILED")})
if nom == TEMOIN:
    verdict = "SAIN" if r.returncode == 0 and not tombes else "TÉMOIN EN ÉCHEC"
else:
    verdict = "VUE" if r.returncode == 1 and tombes else "NON VUE"
print(f"{nom} : {verdict} | {lignes[-1] if lignes else r.stderr[-300:]} | {', '.join(tombes)}")
