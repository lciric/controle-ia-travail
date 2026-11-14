"""Écrit essais/mutations_pilote_mr2_v73.py : les mutations du banc v72 qui visent le lanceur, reciblées sur le lanceur v73
(essais v73), et des mutations neuves du bloc gelé v73. Les mutations des modules de lecture et de sonde (inchangés depuis la
v72) sont jugées par le banc v72."""
import importlib.util, sys
racine = sys.argv[1]
s = importlib.util.spec_from_file_location("banc72", f"{racine}/essais/mutations_pilote_mr2_v72.py")
b72 = importlib.util.module_from_spec(s); s.loader.exec_module(b72)
src72 = open(f"{racine}/essais/mutations_pilote_mr2_v72.py", encoding="utf-8").read()
la73 = open(f"{racine}/demonstrations/pilote_mr2_v73.py", encoding="utf-8").read()
port = []
for m in b72.MUTATIONS:
    if m["fichier"] != b72.LA:
        continue
    m = dict(m, fichier="LA")
    m["avant"] = m["avant"].replace("pilote-v72", "pilote-v73")
    m["apres"] = m["apres"].replace("pilote-v72", "pilote-v73") if "N20" not in m["id"] else m["apres"]
    if m["id"].startswith("N20"):
        m["avant"] = '"<!-- empreintes-du-code-pilote-v73 : début -->", "<!-- empreintes-du-code-pilote-v73 : fin -->"'
        m["apres"] = '"<!-- empreintes-du-code-pilote-v72 : début -->", "<!-- empreintes-du-code-pilote-v72 : fin -->"'
        m["attendu"] = "test_bloc_gele_v72"
    port.append(m)
V = "V73"
neuves = [
 dict(id="B01-bloc-renomme-les-modeles", fichier="LA",
      avant="        lignes.append(f\"borne-de-sortie {nom} {p['borne_sortie_jetons']} jetons ; plafond de session \"",
      apres="        lignes.append(f\"borne-de-sortie {nom} {p['modele']} {p['borne_sortie_jetons']} jetons ; plafond de session \"",
      selection=V, attendu="test_bloc_sans_identifiant_de_modele"),
 dict(id="B02-ligne-d-identite-retiree", fichier="LA",
      avant="    lignes.append(\"identite-des-proposeurs celle de la configuration (clé modele de chaque proposeur), gelée par l'empreinte du \"\n",
      apres="    lignes.append(\"\"\n", selection=V, attendu="test_bloc_sans_identifiant_de_modele"),
 dict(id="B03-lanceur-v73-hors-du-bloc", fichier="LA", avant='    "demonstrations/pilote_mr2_v73.py", "pole/pilote_mr2_v70.py",',
      apres='    "pole/pilote_mr2_v70.py",', selection="V72", attendu="test_lanceur_v72"),
 dict(id="U01-proposeur-libre", fichier="LA", avant="    if nom not in SONDE_UN:\n", apres="    if False:\n",
      selection="SondeUnRelais", attendu="test_artefacts"),
 dict(id="U02-perimetre-libre", fichier="LA", avant='SONDE_UN = {"astra": {"montant_usd": 2.0, "perimetre_contient": ["sonde", "seul relais Astra"]}}',
      apres='SONDE_UN = {"astra": {"montant_usd": 2.0, "perimetre_contient": ["sonde"]}}', selection="SondeUnRelais", attendu="test_artefacts"),
 dict(id="U03-pire-au-dela-de-la-part", fichier="LA", avant="    if pire > part + 1e-9 or part > montant + 1e-9:\n", apres="    if False:\n",
      selection="SondeUnFonctions", attendu="test_pire_sous_part"),
 dict(id="U04-registre-non-lu", fichier="LA",
      avant="    reprise = S.exiger_premier_lancement(args.registre_lancements, [args.go_sonde], args.reprise, args.registre_decisions)\n",
      apres="    reprise = None\n", selection="SondeUnRelais", attendu="test_sain"),
 dict(id="U05-lancement-non-consigne", fichier="LA",
      avant="        S.consigner_lancement(args.registre_lancements, [args.go_sonde], args.sortie, debut, reprise)\n        for quoi",
      apres="        for quoi", selection="SondeUnRelais", attendu="test_sain"),
 dict(id="U06-motif-non-porte", fichier="LA", avant="    motif = S.motif_reflexion_absente(nom, p, rel[\"conclusions\"])\n",
      apres="    motif = None\n", selection="SondeUnRelais", attendu="test_reflexion_nulle_nommee"),
 dict(id="U07-modele-recopie", fichier="LA", avant='"identite": {k: p[k] for k in S.IDENTITE if k != "modele"}',
      apres='"identite": {k: p[k] for k in S.IDENTITE}', selection="SondeUnRelais", attendu="test_sain"),
 dict(id="U08-etat-du-relais-non-controle", fichier="LA", avant="        if ecarts:\n            raise P.Refus(f\"relais {nom} : état non conforme ({ecarts})\")\n        relais = {nom",
      apres="        relais = {nom", selection="SondeUnRelais", attendu="test_artefacts"),
 dict(id="U09-relais-au-plafond-du-pilote", fichier="LA", avant="python=sys.executable, plafond=part, max_appels=len(S.APPELS))",
      apres="python=sys.executable, max_appels=len(S.APPELS))", selection="SondeUnRelais", attendu="test_sain"),
 dict(id="U10-go-non-lue", fichier="LA", avant="    go = PR.lire_go_de_lignes(SONDE_UN, args.registre_go, {nom: args.go_sonde})\n", apres="    go = None\n",
      selection="SondeUnRelais", attendu="test_artefacts"),
 dict(id="U11-pire-non-exige", fichier="LA", avant="    exiger_pire_sous_part(pire, part, SONDE_UN[nom][\"montant_usd\"])\n", apres="",
      selection="SondeUnArrets", attendu="test_pire_au_dessus_de_la_ligne"),
 dict(id="U12-releve-a-la-version-du-mode-reel", fichier="LA", avant='VERSION_RELEVE_UN = "releve-sonde-un-relais-v73"',
      apres='VERSION_RELEVE_UN = "releve-sonde-pilote-v72"', selection="SondeUnRelais", attendu="test_sain"),
 dict(id="U13-dossier-existant-admis", fichier="LA", avant="        raise P.Refus(\"sonde d'un relais : dossier de sortie existant\")\n",
      apres="        pass\n", selection="SondeUnRelais", attendu="test_artefacts"),
 dict(id="U15-appel-parti-non-porte", fichier="LA", avant="                faits.append(S.faits_depuis_les_pieces(conf, nom, en_cours, args.sortie))\n",
      apres="                pass\n", selection="SondeUnArrets", attendu="test_cout_excessif_arret_et_appel_porte"),
 dict(id="N18b-consignes-de-la-v11", fichier="CONF",
      avant='"borne_gelee": "Combien d\'entiers de 1 à 10000 sont divisibles par 7 ou 11, mais pas par 13 ? Le seul nombre."',
      apres='"borne_gelee": "Réponds par le seul mot OK."', selection="V72", attendu="test_consignes_v12_mot_pour_mot"),
]
for m in port + neuves:
    cible = la73 if m["fichier"] == "LA" else open(f"{racine}/exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json", encoding="utf-8").read()
    assert cible.count(m["avant"]) == 1, (m["id"], cible.count(m["avant"]))
lit = lambda m: f"    M({m['id']!r}, {m['fichier']}, {m['avant']!r},\n      {m['apres']!r}, {m['selection']!r}, {m['attendu']!r}),"
i = src72.index("\ndef preparer_copie(")
harnais = src72[i:]
entete = f'''"""Banc de mutations du code v73 du pilote MR-2, restreint au lanceur v73 (seul fichier neuf depuis la v72) : les {len(port)}
mutations du banc v72 qui visent le lanceur, reciblées sur le lanceur v73 et jugées par les essais v73, trois mutations neuves du
bloc gelé (B01 à B03 : identifiant de modèle recopié, ligne d'identité retirée, lanceur hors de la liste gelée) quatorze de la
sous-commande `sonde-un` (U01 à U13, U15 ; U09 à U15 proposées par la contre-lecture v73 ; U14 sans artefact atteignable
depuis la doublure, dit au rapport) et N18b (N18 du banc v72 reciblée sur l'essai des consignes mot pour mot). Les mutations
des modules de lecture et de sonde, inchangés depuis la v72, sont jugées par le banc v72 (`mutations_pilote_mr2_v72.py`). Méthode
inchangée (copie neuve par mutation, remplacement présent une seule fois, essais sains d'abord, « tuée » seulement si l'essai
attendu échoue). Écrit par `faire_banc_v73.py`.

  OMP_NUM_THREADS=2 python3 -I -B essais/mutations_pilote_mr2_v73.py [--sortie RESULTAT.json] [--seulement ID,ID]
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
T = "essais/test_pilote_mr2_v73.py"
LA = "demonstrations/pilote_mr2_v73.py"
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
open(f"{racine}/essais/mutations_pilote_mr2_v73.py", "x", encoding="utf-8").write(t)
s = importlib.util.spec_from_file_location("banc73", f"{racine}/essais/mutations_pilote_mr2_v73.py")
b73 = importlib.util.module_from_spec(s); s.loader.exec_module(b73)
print(len(b73.MUTATIONS), "mutations :", [m["id"] for m in b73.MUTATIONS])
