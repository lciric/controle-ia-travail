"""Épreuve du contre-lecteur (aucun réseau) : Argon, appel à borne courte dont les 256 jetons sont tous de la réflexion et dont
`candidatesTokenCount` est absent (un champ nul est omis du JSON) : lecture de la commande et du relais contre lecture de la
sonde. Usage : python -I -B epreuve_argon_champ_absent_v70_v1.py RACINE_ORCHESTRATOR"""
import importlib.util, os, sys
RACINE = sys.argv[1]
sys.path.insert(0, RACINE)
from pole import proposeurs_pilote_v70 as PR, sonde_pilote_v70 as S
conf, _ = PR.lire_configuration(os.path.join(RACINE, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v11.json"))
def charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
C, R = charger("c", conf["commande"]["chemin_absolu"]), charger("r", conf["relais"]["chemin_absolu"])
corps = {"modelVersion": "gemini-4-argon", "candidates": [{"finishReason": "MAX_TOKENS", "content": {"role": "model"}}],
         "usageMetadata": {"promptTokenCount": 21, "thoughtsTokenCount": 256, "totalTokenCount": 277}}
texte, raison, servi, jetons, refus = C.lire_dialecte("gemini", corps, False)
print("commande :", {"raison": raison, "jetons": jetons, "usage lu entier": C._entier(jetons["entree"]) and C._entier(jetons["sortie"])})
print("relais   : usage_du_corps →", R.usage_du_corps("gemini", corps, False))
u = S.usage_brut("gemini", corps)
print("sonde    : usage_brut →", u)
print("sonde    : usage_entier →", S.usage_entier("gemini", u), "; sortie_comptee →", S.sortie_comptee("gemini", u, False),
      "; verdict →", S.verdict_reflexion("gemini", u))
f1 = {"appel": "borne_gelee", "borne": 36000, "etat": "complet", "statut_amont": 200, "modele_servi_conforme": True,
      "usage_brut": {"promptTokenCount": 9, "candidatesTokenCount": 1, "thoughtsTokenCount": 120, "totalTokenCount": 130},
      "au_dessus_du_pire_cas": False}
f2 = {"appel": "borne_courte", "borne": 256, "etat": "tronque", "statut_amont": 200, "modele_servi_conforme": True, "usage_brut": u,
      "au_dessus_du_pire_cas": False}
c = S.conclusions(conf, "argon", [f1, f2])
print("sonde    : conclusions d'Argon non vraies →", [k for k in S.conclusions_exigees("gemini") if c[k] is not True])
