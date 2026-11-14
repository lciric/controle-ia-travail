"""Écrit essais/mutations_pilote_mr2_v72.py : les 46 mutations du banc v71 reciblées sur le code v72 (le texte visé est cherché
dans le module de la sonde v72 s'il y est recopié, sinon dans celui de la v71, que la v72 appelle), et les mutations neuves."""
import importlib.util, sys
racine = sys.argv[1]
s = importlib.util.spec_from_file_location("banc71", f"{racine}/essais/mutations_pilote_mr2_v71.py")
b71 = importlib.util.module_from_spec(s); s.loader.exec_module(b71)
src71 = open(f"{racine}/essais/mutations_pilote_mr2_v71.py", encoding="utf-8").read()
so72 = open(f"{racine}/pole/sonde_pilote_v72.py", encoding="utf-8").read()
sans_commentaire = {'    if r.get("configuration_sha256") != attendu["configuration_sha256"]:  # a-2\n':
                    '    if r.get("configuration_sha256") != attendu["configuration_sha256"]:\n',
                    '    if r.get("code_sha256") != attendu["code_sha256"]:  # a-2\n': '    if r.get("code_sha256") != attendu["code_sha256"]:\n'}
port = []
for m in b71.MUTATIONS:
    m = dict(m)
    if m["fichier"] == b71.SO:
        av = sans_commentaire.get(m["avant"], m["avant"])
        if so72.count(av) == 1:
            m["fichier"], m["avant"] = "SO72", av
            m["apres"] = m["apres"] if av == m["avant"] else m["apres"]
        else:
            m["fichier"] = "SO71"
    elif m["fichier"] == b71.LA:
        m["fichier"] = "LA"
    elif m["fichier"] == b71.PR:
        m["fichier"] = "PR"
    else:
        raise SystemExit(f"fichier inattendu {m['fichier']}")
    port.append(m)
def lit(m):
    return (f"    M({m['id']!r}, {m['fichier']}, {m['avant']!r},\n      {m['apres']!r}, {m['selection']!r}, {m['attendu']!r}),")
V = "V72"
neuves = [
 ("N01-version-v12-non-exigee", "PC", '    if conf.get("version") != VERSION_CONFIGURATION:\n', '    if False:\n', V, "test_versions_de_configuration"),
 ("N02-version-v11-exigee", "PC", 'VERSION_CONFIGURATION = "configuration-pilote-mr2-v12"', 'VERSION_CONFIGURATION = "configuration-pilote-mr2-v11"', V, "test_versions_de_configuration"),
 ("N03-section-sonde-non-verifiee", "PC", "    _V70.verifier_section_sonde(conf, props)\n", "", V, "test_versions_de_configuration"),
 ("N04-reflexion-toujours-observee", "SO72", "    return any(_entier_positif(reflexion_brute(dialecte, f.get(\"usage_brut\"))) for f in faits)",
  "    return True", 'ModeReelBoutEnBout and test_v72_champ_de_reflexion_absent_refuse', "test_v72_champ_de_reflexion_absent_refuse"),
 ("N05-reflexion-nulle-observee", "SO72", " and x > 0\n", " and x >= 0\n", V, "test_reflexion_observee"),
 ("N06-booleen-admis", "SO72", "    return isinstance(x, int) and not isinstance(x, bool) and x > 0", "    return isinstance(x, int) and x > 0", V, "test_reflexion_observee"),
 ("N07-astra-sortie-prise-pour-reflexion", "SO72", '"astra": ("completion_tokens_details", "reasoning_tokens")}', '"astra": ("completion_tokens", None)}', V, "test_reflexion_observee"),
 ("N08-refus-nomme-retire", "SO72", '        motif = motif_reflexion_absente(nom, p, recalculees)\n', "        motif = None\n",
  'ModeReelBoutEnBout and test_v72_champ_de_reflexion_absent_refuse', "test_v72_champ_de_reflexion_absent_refuse"),
 ("N09-reflexion-non-exigee", "SO72", "    return CONCLUSIONS_EXIGEES + CONCLUSIONS_REFLEXION\n", "    return CONCLUSIONS_EXIGEES\n", V, "test_conclusions_exigees"),
 ("N10-conclusion-non-calculee", "SO72", '    if d != "claude":\n        c["reflexion_observee"]', '    if False:\n        c["reflexion_observee"]',
  'ModeReelBoutEnBout and test_v72_sonde_saine_confirmee', "test_v72_sonde_saine_confirmee"),
 ("N11-version-du-releve-v71", "SO72", 'VERSION_RELEVE = "releve-sonde-pilote-v72"', 'VERSION_RELEVE = "releve-sonde-pilote-v71"',
  'ModeReelBoutEnBout and test_v72_releve_de_la_v71_refuse', "test_v72_releve_de_la_v71_refuse"),
 ("N12-releve-v71-admis", "SO72", '    if not isinstance(r, dict) or r.get("version") != VERSION_RELEVE:\n',
  '    if not isinstance(r, dict) or r.get("version") not in (VERSION_RELEVE, _S71.VERSION_RELEVE):\n',
  'ModeReelBoutEnBout and test_v72_releve_de_la_v71_refuse', "test_v72_releve_de_la_v71_refuse"),
 ("N13-lancement-sous-le-module-v71", "SO72", '"reprise": reprise,\n                            "module": VERSION}', '"reprise": reprise,\n                            "module": _S71.VERSION}',
  'ModeReelBoutEnBout and test_v72_sonde_saine_confirmee', "test_v72_sonde_saine_confirmee"),
 ("N14-lanceur-sur-la-sonde-v71", "LA", "from pole import sonde_pilote_v72 as S  # noqa: E402\n", "from pole import sonde_pilote_v71 as S  # noqa: E402\n", V, "test_lanceur_v72"),
 ("N15-lanceur-sur-la-configuration-v11", "LA", '"pilote-mr2-v70", "configuration-pilote-mr2-v12.json")\nPROGRAMME',
  '"pilote-mr2-v70", "configuration-pilote-mr2-v11.json")\nPROGRAMME', V, "test_lanceur_v72"),
 ("N16-sonde-v72-hors-du-bloc", "LA", '"pole/sonde_pilote_v71.py", "pole/sonde_pilote_v72.py",\n', '"pole/sonde_pilote_v71.py",\n', "BlocGele", "test_fermeture_des_imports"),
 ("N17-lecture-v72-hors-du-bloc", "LA", '    "pole/proposeurs_pilote_v72.py", "pole/sonde_pilote_v71.py"', '    "pole/sonde_pilote_v71.py"', "BlocGele", "test_fermeture_des_imports"),
 ("N18-consignes-de-la-v11", "CONF", '"borne_gelee": "Combien d\'entiers de 1 à 10000 sont divisibles par 7 ou 11, mais pas par 13 ? Le seul nombre."',
  '"borne_gelee": "Réponds par le seul mot OK."', V, "test_configuration_v12_seules_les_consignes_changent"),
 ("N19-regle-d-argon-changee", "CONF", '"reflexion_comprise": false', '"reflexion_comprise": true', V, "test_configuration_v12_seules_les_consignes_changent"),
 ("N21-consigne-courte-de-la-v11", "CONF", '"borne_courte": "Énumère un à un les nombres premiers entre 1000 et 1200, en justifiant chacun par ses divisions."',
  '"borne_courte": "Écris un très long texte, de plusieurs milliers de mots, sur l\'histoire de la navigation."', V, "test_consignes_v12_mot_pour_mot"),
 ("N22-reflexion-aux-deux-appels", "SO72", '    return any(_entier_positif(reflexion_brute(dialecte, f.get("usage_brut"))) for f in faits)',
  '    return all(_entier_positif(reflexion_brute(dialecte, f.get("usage_brut"))) for f in faits)', V, "test_reflexion_observee"),
 ("N23-details-non-objet", "SO72", "        x = x.get(b) if isinstance(x, dict) else None", "        x = x.get(b)", V, "test_reflexion_observee"),
 ("N24-argon-candidats-pris-pour-reflexion", "SO72", 'CHAMP_DE_REFLEXION = {"gemini": ("thoughtsTokenCount", None),',
  'CHAMP_DE_REFLEXION = {"gemini": ("candidatesTokenCount", None),', V, "test_reflexion_observee"),
 ("N25-configuration-v12-hors-du-bloc", "LA", '    "exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json",\n',
  '    "exemples/pilote-mr2-v70/configuration-pilote-mr2-v11.json",\n', V, "test_lanceur_v72"),
 ("N26-jouer-lit-par-la-v70", "LA", "    conf, _ = PC.lire_configuration(args.configuration)\n", "    conf, _ = PR.lire_configuration(args.configuration)\n",
  'ModeReelBoutEnBout and test_sain_bout_en_bout', "test_sain_bout_en_bout"),
 ("N27-refus-nomme-sur-appel-en-echec", "SO72", ' and c.get("statut") is True and c.get("usage_entier") is True \\\n', ' \\\n', V, "test_motif_reflexion_absente"),
 ("N20-marqueurs-du-bloc-v71", "LA", '"<!-- empreintes-du-code-pilote-v72 : début -->", "<!-- empreintes-du-code-pilote-v72 : fin -->"',
  '"<!-- empreintes-du-code-pilote-v71 : début -->", "<!-- empreintes-du-code-pilote-v71 : fin -->"', V, "test_bloc_gele_v72"),
]
i = src71.index("\ndef preparer_copie(")
harnais = src71[i:]
assert harnais.count('    if m["fichier"] in (CO, RE):') == 1
entete = '''"""Banc de mutations du code v72 du pilote MR-2 (configuration v12, lecture v72, sonde v72, lanceur v72). Deux parts : (1) les
46 mutations du banc v71 (`mutations_pilote_mr2_v71.py`), **reciblées** sur le code que la v72 exécute — le texte visé est
cherché dans le module de la sonde v72 s'il y est recopié (`exiger_releve`), sinon dans le module v71, que la v72 appelle ; le
lanceur visé est le lanceur v72 ; les essais sont ceux de `test_pilote_mr2_v72.py` ; (2) vingt-sept mutations neuves (N01 à N27 ; N21 à N27 proposées par la contre-lecture du code v72) du
code v72. Méthode de la v71, inchangée : copie neuve de `orchestrator/` par mutation, remplacement présent **une seule fois**
(sinon défaut du banc), empreintes de la commande et du relais recopiées quand l'un d'eux est muté, essais sains d'abord sur la
copie non mutée, « tuée » seulement si l'essai attendu échoue ; un seul processus à la fois. Banc écrit par
`faire_banc_v72.py` (outil versé avec le rapport).

  OMP_NUM_THREADS=2 python3 -I -B essais/mutations_pilote_mr2_v72.py [--sortie RESULTAT.json] [--seulement ID,ID]
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
T = "essais/test_pilote_mr2_v72.py"
PR, LA = "pole/proposeurs_pilote_v70.py", "demonstrations/pilote_mr2_v72.py"
PC = "pole/proposeurs_pilote_v72.py"
SO71, SO72 = "pole/sonde_pilote_v71.py", "pole/sonde_pilote_v72.py"
CO, RE = "exemples/pilote-mr2-v70/commandes/commande_pilote_v70.py", "exemples/pilote-mr2-v70/commandes/relais_pilote_v70.py"
CONF = "exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json"


def M(ident, fichier, avant, apres, selection, attendu):
    return {"id": ident, "fichier": fichier, "avant": avant, "apres": apres, "selection": selection, "attendu": attendu}


MR = "ModeReelBoutEnBout"
EB = "EssaiABlanc"
AP = "C7C8C10Appel"
MUTATIONS = [
    # --- (1) les 46 mutations du banc v71, reciblées sur le code v72 ---
'''
corps = "\n".join(lit(m) for m in port) + "\n    # --- (2) neuves de la v72 ---\n" + "\n".join(
    lit({"id": a, "fichier": b, "avant": c, "apres": d, "selection": e, "attendu": f}) for a, b, c, d, e, f in neuves) + "\n]\n\n"
t = entete + corps + harnais.lstrip("\n")
open(f"{racine}/essais/mutations_pilote_mr2_v72.py", "x", encoding="utf-8").write(t)
# contrôle à sec : chaque texte avant présent une seule fois dans son fichier
s = importlib.util.spec_from_file_location("banc72", f"{racine}/essais/mutations_pilote_mr2_v72.py")
b72 = importlib.util.module_from_spec(s); s.loader.exec_module(b72)
defauts = [m["id"] for m in b72.MUTATIONS if open(f"{racine}/{m['fichier']}", encoding="utf-8").read().count(m["avant"]) != 1]
print(len(b72.MUTATIONS), "mutations ;", sum(1 for m in b72.MUTATIONS if m["fichier"] == b72.SO72), "sur la sonde v72 ;",
      "défauts :", defauts)
