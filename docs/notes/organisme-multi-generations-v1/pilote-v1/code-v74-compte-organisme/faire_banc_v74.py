"""Écrit essais/mutations_pilote_mr2_v74.py : les mutations du banc v73 (lanceur, configuration) reciblées sur le lanceur v74 et
les essais v74, et les mutations neuves de la sonde v74 et de la garde du pilote (S01 à S07, G01 à G05, L02, L03)."""
import importlib.util, sys
racine = sys.argv[1]
s = importlib.util.spec_from_file_location("banc73", f"{racine}/essais/mutations_pilote_mr2_v73.py")
b73 = importlib.util.module_from_spec(s); s.loader.exec_module(b73)
src73 = open(f"{racine}/essais/mutations_pilote_mr2_v73.py", encoding="utf-8").read()
la74 = open(f"{racine}/demonstrations/pilote_mr2_v74.py", encoding="utf-8").read()
so74 = open(f"{racine}/pole/sonde_pilote_v74.py", encoding="utf-8").read()
conf = open(f"{racine}/exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json", encoding="utf-8").read()
port = []
for m in b73.MUTATIONS:
    m = dict(m, fichier="LA" if m["fichier"] == b73.LA else "CONF")
    for k in ("avant", "apres"):
        m[k] = m[k].replace("pilote-v73", "pilote-v74").replace("pilote_mr2_v73.py", "pilote_mr2_v74.py")
    if m["id"].startswith("N20"):
        m["avant"] = '"<!-- empreintes-du-code-pilote-v74 : début -->", "<!-- empreintes-du-code-pilote-v74 : fin -->"'
        m["apres"] = '"<!-- empreintes-du-code-pilote-v73 : début -->", "<!-- empreintes-du-code-pilote-v73 : fin -->"'
    if m["id"].startswith("N14"):
        continue  # le lanceur v74 n'importe plus la sonde v72 sous ce texte : remplacée par L02
    port.append(m)
E2E = "ModeReelBoutEnBout and test_v74_sans_reflexion_admise_puis_garde_du_pilote"
neuves = [
 dict(id="S01-champ-nul-admis", fichier="SO74", avant='    if not isinstance(u, dict) or "thoughtsTokenCount" in u:\n', apres="    if not isinstance(u, dict):\n",
      selection="V74", attendu="test_sans_effet_d_un_appel"),
 dict(id="S02-jetons-caches-admis", fichier="SO74", avant="    return _entier(p) and _entier(c) and _entier(total) and total == p + c\n",
      apres="    return _entier(p) and _entier(c)\n", selection="V74", attendu="test_sans_effet_d_un_appel"),
 dict(id="S03-un-seul-appel-suffit", fichier="SO74", avant="    return sorted(par_appel) == sorted(APPELS) and len(faits) == len(APPELS) \\\n        and all(",
      apres="    return any(", selection="V74", attendu="test_faits_reels_de_la_sonde_v73"),
 dict(id="S04-regle-toujours-confirmee", fichier="SO74",
      avant='        c["regle_confirmee_ou_sans_effet"] = c["verdict_egal_a_la_regle"] is True or c["reflexion_sans_effet"] is True\n',
      apres='        c["regle_confirmee_ou_sans_effet"] = True\n', selection="V74", attendu="test_regle_contredite_refusee"),
 dict(id="S05-exigences-de-la-v72", fichier="SO74", avant="    if dialecte == \"gemini\":\n        return CONCLUSIONS_GEMINI\n",
      apres="    if False:\n        return CONCLUSIONS_GEMINI\n", selection="V74", attendu="test_exigences"),
 dict(id="S06-refus-nomme-sans-exception", fichier="SO74",
      avant='        if not (p["dialecte"] == "gemini" and recalculees.get("reflexion_sans_effet") is True):\n', apres="        if True:\n",
      selection=E2E, attendu="test_v74_sans_reflexion_admise_puis_garde_du_pilote"),
 dict(id="S07-aucun-proposeur-sans-reflexion", fichier="SO74",
      avant='                  if c.get("reflexion_sans_effet") is True and c.get("verdict_egal_a_la_regle") is not True)',
      apres='                  if False)', selection=E2E, attendu="test_v74_sans_reflexion_admise_puis_garde_du_pilote"),
 dict(id="G01-garde-du-pilote-retiree", fichier="LA",
      avant='                garder_reflexion_absente(conf, nom, dossier_appel, r, sans_reflexion)  # v74',
      apres='                pass  # v74', selection=E2E, attendu="test_v74_sans_reflexion_admise_puis_garde_du_pilote"),
 dict(id="G02-champ-brut-non-lu", fichier="LA", avant="    if S.champ_de_reflexion_present(d, u) or (t is not None and t != 0):\n",
      apres="    if (t is not None and t != 0):\n", selection="V74", attendu="test_garde_du_pilote"),
 dict(id="G03-jetons-non-lus", fichier="LA", avant="    if S.champ_de_reflexion_present(d, u) or (t is not None and t != 0):\n",
      apres="    if S.champ_de_reflexion_present(d, u):\n", selection="V74", attendu="test_garde_du_pilote"),
 dict(id="G04-champ-gemini-jamais-vu", fichier="SO74", avant='        return "thoughtsTokenCount" in u\n', apres="        return False\n",
      selection="V74", attendu="test_champ_de_reflexion_present"),
 dict(id="G05-corps-illisible-admis", fichier="LA", avant="        except (OSError, ValueError, AttributeError):\n            raise PR.ArretPilote(f\"{nom} : corps du relais illisible",
      apres="        except (OSError, ValueError, AttributeError):\n            return\n            raise PR.ArretPilote(f\"{nom} : corps du relais illisible",
      selection="V74", attendu="test_garde_du_pilote"),
 dict(id="L02-lanceur-sur-la-sonde-v72", fichier="LA", avant="from pole import sonde_pilote_v74 as S  # noqa: E402\n",
      apres="from pole import sonde_pilote_v72 as S  # noqa: E402\n", selection="V74", attendu="test_lanceur_v74"),
 dict(id="L03-sonde-v74-hors-du-bloc", fichier="LA", avant='    "pole/sonde_pilote_v74.py",\n', apres="", selection="V74", attendu="test_lanceur_v74"),
 dict(id="S08-total-au-plus-egal", fichier="SO74", avant="    return _entier(p) and _entier(c) and _entier(total) and total == p + c\n",
      apres="    return _entier(p) and _entier(c) and _entier(total) and total <= p + c\n", selection="V74", attendu="test_sans_effet_d_un_appel"),
 dict(id="S09-faits-hors-pieces-non-relus", fichier="SO74", avant='        if f != faits_depuis_les_pieces(conf, f["proposeur"], f["appel"], racine):\n',
      apres="        if False:\n", selection="ModeReelBoutEnBout and test_artefacts_releve", attendu="test_artefacts_releve"),
 dict(id="G07-garde-apres-la-depense", fichier="LA",
      avant='                garder_reflexion_absente(conf, nom, dossier_appel, r, sans_reflexion)  # v74 : avant de compter la dépense (comptée une fois, à l\'arrêt)\n                depense[nom] += r["cout_usd"]\n',
      apres='                depense[nom] += r["cout_usd"]\n                garder_reflexion_absente(conf, nom, dossier_appel, r, sans_reflexion)\n',
      selection=E2E, attendu="test_v74_sans_reflexion_admise_puis_garde_du_pilote"),
 dict(id="G08-sans-reflexion-pour-tous", fichier="SO74",
      avant='                  if c.get("reflexion_sans_effet") is True and c.get("verdict_egal_a_la_regle") is not True)', apres="                  if True)",
      selection=E2E, attendu="test_v74_sans_reflexion_admise_puis_garde_du_pilote"),
 dict(id="G09-total-cache-non-garde", fichier="LA",
      avant='    if d == "gemini" and isinstance(u, dict) and "totalTokenCount" in u and not S.sans_effet_d_un_appel(u):\n', apres="    if False:\n",
      selection="V74", attendu="test_garde_du_pilote_total_cache"),
 dict(id="G10-total-absent-arrete", fichier="LA",
      avant='    if d == "gemini" and isinstance(u, dict) and "totalTokenCount" in u and not S.sans_effet_d_un_appel(u):\n',
      apres='    if d == "gemini" and isinstance(u, dict) and not S.sans_effet_d_un_appel(u):\n', selection="V74", attendu="test_garde_du_pilote_total_cache"),
 dict(id="M01-trace-absente-du-manifeste", fichier="LA", avant=' "proposeurs_sans_reflexion": sans_reflexion,  # v74\n', apres="  # v74\n",
      selection=E2E, attendu="test_v74_sans_reflexion_admise_puis_garde_du_pilote"),
]
cibles = {"LA": la74, "SO74": so74, "CONF": conf}
for m in port + neuves:
    assert cibles[m["fichier"]].count(m["avant"]) == 1, (m["id"], cibles[m["fichier"]].count(m["avant"]))
lit = lambda m: f"    M({m['id']!r}, {m['fichier']}, {m['avant']!r},\n      {m['apres']!r}, {m['selection']!r}, {m['attendu']!r}),"
harnais = src73[src73.index("\ndef preparer_copie("):]
entete = f'''"""Banc de mutations du code v74 du pilote MR-2 : les {len(port)} mutations du banc v73 (lanceur, configuration) reciblées sur le
lanceur v74 et les essais v74 (N14 retirée : son texte n'existe plus, remplacée par L02), et {len(neuves)} neuves de la v74 (S01 à
S09 : module de la sonde v74 ; G01 à G05, G07 à G10 : garde du pilote (G10 : réserve R2 de la relecture courte du jalon 3) ; M01 : manifeste ; L02, L03 : lanceur ; les
mutations S08, S09, G07, G08 sont celles que la contre-lecture v74 prédisait survivantes, et sont visées sur des essais neufs ou
renforcés ; G06 est sans objet : le dossier de l'appel n'est plus calculé qu'une fois). Les modules de lecture et de sonde v72 et v71,
inchangés, sont jugés par le banc v72. Méthode inchangée. Écrit par `faire_banc_v74.py`.

  OMP_NUM_THREADS=2 python3 -I -B essais/mutations_pilote_mr2_v74.py [--sortie RESULTAT.json] [--seulement ID,ID]
Codes : 0 toutes tuées pour la raison attendue ; 1 au moins une autre issue ; 2 défaut du banc.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
T = "essais/test_pilote_mr2_v74.py"
LA = "demonstrations/pilote_mr2_v74.py"
SO74 = "pole/sonde_pilote_v74.py"
CO, RE = "exemples/pilote-mr2-v70/commandes/commande_pilote_v70.py", "exemples/pilote-mr2-v70/commandes/relais_pilote_v70.py"
CONF = "exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json"


def M(ident, fichier, avant, apres, selection, attendu):
    return {{"id": ident, "fichier": fichier, "avant": avant, "apres": apres, "selection": selection, "attendu": attendu}}


MR = "ModeReelBoutEnBout"
EB = "EssaiABlanc"
AP = "C7C8C10Appel"
MUTATIONS = [
'''
t = entete + "\n".join(lit(m) for m in port + neuves) + "\n]\n\n" + harnais.lstrip("\n")
open(f"{racine}/essais/mutations_pilote_mr2_v74.py", "x", encoding="utf-8").write(t)
s = importlib.util.spec_from_file_location("banc74", f"{racine}/essais/mutations_pilote_mr2_v74.py")
b74 = importlib.util.module_from_spec(s); s.loader.exec_module(b74)
print(len(b74.MUTATIONS), "mutations")
