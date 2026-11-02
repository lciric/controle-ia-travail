"""Pré-vol du complément de validation du rejeu à graine (processeur, sans modèle 8B ; comptes seulement : aucun texte,
aucun score, aucune étiquette, aucune activation de P3). Arguments : ARBRE (arbre de travail au commit lancé ou à sa
base `ab808842`, avec le texte et la configuration du complément dans `prereg/`), PRINCIPAL (dépôt principal, d'où les
vraies pièces de P3 sont liées), R (dossier temporaire neuf, liens symboliques seulement), TOK (tokeniseur de Llama 3.1 à
la révision de P3).
A. gardes de configuration (272, durées) ; B. garde R3 du cœur et du lot sur l'arbre qui porte les manifestes du
2 novembre (cas sain : configuration du complément ; artefact : configuration de la v2) ; C. gardes de citation du texte
(libellés lus une fois, empreinte canonique, entropie, commit du code, `exiger_code_cite`, `problemes`) ; D. pièces
réelles par liens symboliques (empreintes, agent comparé au manifeste de P3), ouverture, classement 147 / 7."""
import json, os, re, shutil, sys, time
from pathlib import Path

ARBRE, PRINCIPAL, R, TOK = (Path(x).resolve() for x in sys.argv[1:5])
TEXTE = ARBRE / "prereg/R1-addendum-relance-v2-complement-validation-v1.md"
CONF = ARBRE / "prereg/R1-graine-config-complement-v2.json"
CONF_V2 = ARBRE / "prereg/R1-graine-config-v1.json"
from controle_ia.gardes import GardeArret
from controle_ia.harnais.validation_reelle import COMMIT_CITE, ENTROPIE_CITEE, exiger_code_cite
from controle_ia.prereg import problemes
from controle_ia.runs_nuit import resolution_graine_lot_v1 as rl
from controle_ia.runs_nuit import resolution_graine_v1 as rg

config = json.loads(CONF.read_text(encoding="utf-8"))
config_v2 = json.loads(CONF_V2.read_text(encoding="utf-8"))
canon = rg.empreinte_config(config)
print(f"configuration du complément : {len(config)} clés ; empreinte canonique {canon[:12]} ; v2 {rg.empreinte_config(config_v2)[:12]}")
print("clés changées / v2 :", sorted(k for k in config if config[k] != config_v2.get(k)), "; clés absentes :",
      sorted(set(config) ^ set(config_v2)))


def arret(f, *a):
    try:
        f(*a)
        return "PASSE (aucun arrêt)"
    except GardeArret as e:
        return "arrêt : " + str(e)[:150]


# ---- A. gardes de configuration
rg.exiger_config(config); rg.exiger_reglages_execution(config); rl.exiger_config(config)
print("A. gardes rg.exiger_config, rg.exiger_reglages_execution, rl.exiger_config : passent (combinaisons 272, durées "
      f"{config['duree_max_episode_s']} / {config['duree_max_s']} s)")
for nom, c in (("combinaisons_max_validation ≠ combinaisons_max", {**config, "combinaisons_max_validation": 271}),
               ("duree_max_episode_s > duree_max_s", {**config, "duree_max_episode_s": config["duree_max_s"] + 1}),
               ("clé de répétition en mode réel", {**config, rg.CLE_REPETITION: []})):
    print(f"   artefact {nom} : {arret(rg.exiger_reglages_execution, c)}")

# ---- B. garde R3 (une exécution par étape) sur l'arbre qui porte les manifestes du 2 novembre
runs = sorted(p.parent.name for p in (ARBRE / "runs").glob("*/manifeste.json"))
print(f"B. arbre : {len(runs)} manifestes sous runs/, dont ceux du 2 novembre :",
      [x for x in runs if "r1-graine" in x])
for etape in ("validation", "resolution"):
    print(f"   cœur, étape {etape}, configuration du complément (cas sain) : "
          f"{arret(rg.exiger_execution_unique, ARBRE, config, etape)}")
    print(f"   cœur, étape {etape}, configuration de la v2 (artefact : PREREG oublié) : "
          f"{arret(rg.exiger_execution_unique, ARBRE, config_v2, etape)}")
print(f"   lot, étape resolution-lot, configuration du complément : {arret(rl.exiger_execution_unique, ARBRE, config, 'resolution-lot')}")

# ---- C. citations du texte
texte = TEXTE.read_text(encoding="utf-8")
for lib in ("Tests attendus : `", "Chemin de la configuration de la résolution à graine : `",
            "Configuration de la résolution à graine (empreinte canonique) : `",
            "Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `", "Entropie : `",
            "Commit du code d'analyse : `"):
    lignes = [x for x in texte.splitlines() if lib in x]
    valeur = re.search(re.escape(lib) + r"([^`]*)`", lignes[0]).group(1) if lignes else None
    print(f"C. « {lib[:-4]} » : {len(lignes)} ligne(s) ; valeur {valeur[:16] + '…' if valeur and len(valeur) > 16 else valeur}")
print("   cœur, exiger_config_citee (complément) :", arret(rg.exiger_config_citee, texte, config, "texte"))
print("   cœur, exiger_config_citee (artefact : configuration de la v2) :", arret(rg.exiger_config_citee, texte, config_v2, "texte"))
print("   lot, libellé cité avec l'empreinte du complément :", rl.CONFIG_CITEE.format(canon) in texte)
print("   entropie lue :", ENTROPIE_CITEE.search(texte).group(1), "; commit cité :", COMMIT_CITE.search(texte).group(1))
print("   exiger_code_cite (HEAD de l'arbre contre le commit cité) :", exiger_code_cite(ARBRE, TEXTE)[:12], "passe")
print("   problemes() :", problemes(TEXTE))

# ---- D. pièces réelles (liens symboliques dans un dossier temporaire neuf), classement
if R.exists():
    raise SystemExit(f"{R} existe déjà")
for d in ("donnees/20261019-230011-p3-reel", "donnees/t05-pilote-v1", "diag/20261019-230011-p3-reel",
          "runs/20261019-230011-p3-reel"):
    (R / d).parent.mkdir(parents=True, exist_ok=True)
    (R / d).symlink_to(PRINCIPAL / d)
(R / "prereg").mkdir()
for n in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
    (R / "prereg" / n).symlink_to(PRINCIPAL / "prereg" / n)
for n in ("R1-table-tokenisation-v2.json", "R1-table-tokenisation-v2.json.sha256"):
    shutil.copy(ARBRE / "prereg" / n, R / "prereg" / n)
os.chdir(R)
t0 = time.time()
p = rg.charger_pieces(config, Path("."))
print("D. pièces chargées (empreintes vérifiées ; agent comparé au manifeste de P3) en %.1f s ; épisodes %d ; actions %d"
      % (time.time() - t0, len(p.par_episode), len(p.lignes)))
print("   artefact agent ≠ P3 (révision changée) :",
      arret(rg.charger_pieces, {**config, "agent": {**config["agent"], "revision": "0" * 40}}, Path(".")))
from transformers import AutoTokenizer
from controle_ia.harnais.formats import FormatChat
tok = AutoTokenizer.from_pretrained(str(TOK))
fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
fmt.fins = {int(x) for x in p.table["fins_du_format"]} | {fmt._pieces(("x", "y"))["cloture"][0]}
T = int(config["T"])
rg.exiger_ouverture(fmt, rg.EpisodeP3(p, next(iter(p.par_episode)), T).env(), config["agent"]["texte_attendu_ouverture"], True)
print("   ouverture : texte attendu présent (exiger_ouverture passe)")
t0 = time.time()
cl = rg.classer(p, fmt, T)
val = rg.episodes_de_l_etape("validation", config, cl)
res = rg.episodes_de_l_etape("resolution", config, cl)
rg.exiger_seuil_atteignable(config["seuil_validation"], len(val))
rg.exiger_compte_validation(len(val), config["seuil_validation"])
corr = [e for e, x in cl.items() if x["entree"] and x["entree"]["methode"] != "non_resolu"]
print("   classement %.1f s : identiques de base %d ; corrigés par la table v2 %d ; validation %d (exiger_compte_validation "
      "passe) ; résolution %d" % (time.time() - t0, sum(x["identique_base"] for x in cl.values()), len(corr), len(val),
                                  len(res)))
print("   rangs des 3 de C-6 dans la liste de la validation :", [val.index(e) for e in res[:3]])
print("   artefact seuil_validation 146 :", arret(rg.exiger_compte_validation, len(val), 146))
