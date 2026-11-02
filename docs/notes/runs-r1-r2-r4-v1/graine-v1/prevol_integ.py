"""Pré-vol d'intégration sur processeur, vraies pièces de P3 (liens symboliques dans un dossier temporaire), sans modèle
8B : configuration réelle `prereg/R1-graine-config-v1.json` ; contrôles d'avant-installation du script (son code python
extrait tel quel) avec cas sain et artefacts ; gardes du cœur et du lot ; classement 147 / 7 ; plan des lots de P3 et
lots des 4 non résolus ; cibles du lot ; graines. Comptes seulement : aucun texte, aucun score, aucune étiquette."""
import collections, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

ARBRE, PRINCIPAL, R, TOK = (Path(x) for x in sys.argv[1:5])
from controle_ia.gardes import GardeArret
from controle_ia.runs_nuit import resolution_graine_lot_v1 as rl
from controle_ia.runs_nuit import resolution_graine_v1 as rg
from controle_ia.scellement import sceller

for d in ("donnees/20261019-230011-p3-reel", "donnees/t05-pilote-v1", "diag/20261019-230011-p3-reel",
          "runs/20261019-230011-p3-reel"):
    (R / d).parent.mkdir(parents=True, exist_ok=True)
    (R / d).symlink_to(PRINCIPAL / d)
(R / "prereg").mkdir(exist_ok=True)
for n in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
    (R / "prereg" / n).symlink_to(PRINCIPAL / "prereg" / n)
shutil.copy(ARBRE / "prereg/R1-table-tokenisation-v2.json", R / "prereg/R1-table-tokenisation-v2.json")
shutil.copy(ARBRE / "prereg/R1-graine-config-v1.json", R / "prereg/R1-graine-config-v1.json")
config = json.loads((R / "prereg/R1-graine-config-v1.json").read_text(encoding="utf-8"))
os.chdir(R)
canon = rg.empreinte_config(config)
print("configuration réelle : clés", len(config), "; empreinte canonique", canon[:12])

# ---- 1. avant-installation (code python du script, extrait tel quel)
s = (ARBRE / "scripts/r1_resolution_graine_instance_v1.sh").read_text(encoding="utf-8")
code = re.search(r"<<'PY'\n(import hashlib, json, os, sys\nfrom controle_ia\.scellement import verifier.*?)\nPY\n", s,
                 re.S).group(1)
bloc = re.search(r'read -r N_PIECES.*?\nfi\n', s, re.S).group(0)
mep = int(re.search(r"^MISE_EN_PLACE_MAX_MIN=(\d+)$", s, re.M).group(1))
marge = int(re.search(r"^MARGE_ETAPE_MIN=(\d+)$", s, re.M).group(1))
dc = int(re.search(r"^DELAI_CIBLES_MIN=(\d+)$", s, re.M).group(1))
dt = int(re.search(r"^DELAI_TABLE_MIN=(\d+)$", s, re.M).group(1))
plafond_amorce = int(re.search(r'PLAFOND_MIN="\$\{PLAFOND_MIN:-(\d+)\}"',
                               (ARBRE / "scripts/amorce_instance_r1_resolution_graine_v1.sh").read_text()).group(1))
texte_ok = "\n".join(["- " + rg.CONFIG_CITEE.format(canon), "- " + rl.CONFIG_CITEE.format(canon), ""])
Path("prereg-ok.md").write_text(texte_ok, encoding="utf-8")
Path("prereg-sans-lot.md").write_text("- " + rg.CONFIG_CITEE.format(canon) + "\n", encoding="utf-8")
Path("prereg-faux.md").write_text(texte_ok.replace(canon, "0" * 64), encoding="utf-8")
Path("prereg-double.md").write_text(texte_ok + texte_ok, encoding="utf-8")


def avant(conf, prereg=None, table="prereg/R1-table-tokenisation-v3.json"):
    Path("config-prevol.json").write_text(json.dumps(conf, ensure_ascii=False), encoding="utf-8")
    if prereg is None:                     # texte qui cite cette configuration-ci sous ses deux libellés
        c = rg.empreinte_config(conf)
        Path("prereg-cite.md").write_text("- " + rg.CONFIG_CITEE.format(c) + "\n- " + rl.CONFIG_CITEE.format(c) + "\n",
                                          encoding="utf-8")
        prereg = "prereg-cite.md"
    return subprocess.run([sys.executable, "-", "config-prevol.json", "0", prereg, table], input=code, text=True,
                          capture_output=True, env={**os.environ, "PYTHONPATH": str(ARBRE / "src")})


def derniere(r):
    return (r.stderr.strip().splitlines() or [""])[-1][:120]


r = avant(config, "prereg-ok.md")
print("avant-installation, table v2 sans sceau (copie) : code", r.returncode, "|", derniere(r))
sceller("prereg/R1-table-tokenisation-v2.json")             # sceau de la copie temporaire seulement
r = avant(config, "prereg-ok.md")
print("avant-installation, cas sain : code", r.returncode, "| sortie (pièces, min duree_max_s, min duree_max_lot_s, "
      "canonique) :", " ".join(x[:12] for x in r.stdout.split()))
n_p, de, dl, can = r.stdout.split()
assert r.returncode == 0 and can == canon
besoin = mep + 2 * (int(de) + marge) + dc + (int(dl) + marge) + dt + 5
print(f"budgets (règle du script) : {mep} + 2 × {int(de) + marge} + {dc} + {int(dl) + marge} + {dt} + 5 = {besoin} min ; "
      f"plafond de l'amorce {plafond_amorce} min ; {'≤' if besoin <= plafond_amorce else '>'}")
for nom, conf, pr, tb in (
        ("préenregistrement sans le libellé du lot", config, "prereg-sans-lot.md", None),
        ("empreinte canonique citée fausse", config, "prereg-faux.md", None),
        ("libellés cités deux fois", config, "prereg-double.md", None),
        ("table v3 déjà présente", config, "prereg-ok.md", "prereg/R1-table-tokenisation-v2.json"),
        ("empreinte du manifeste de P3 fausse", {**config, "manifeste_p3_sha256": "0" * 64}, None, None),
        ("duree_max_episode_lot_s > duree_max_lot_s", {**config, "duree_max_episode_lot_s": 4000}, None, None),
        ("duree_max_lot_s absent", {k: v for k, v in config.items() if k != "duree_max_lot_s"}, None, None)):
    conf2 = conf
    r = avant(conf2, pr, tb or "prereg/R1-table-tokenisation-v3.json")
    print(f"artefact {nom} : code {r.returncode} | {derniere(r)}")
    assert r.returncode != 0

# ---- 2. gardes des modules
rg.exiger_config(config); rg.exiger_reglages_execution(config); rl.exiger_config(config)
print("gardes : rg.exiger_config, rg.exiger_reglages_execution, rl.exiger_config passent ; clé de répétition absente")
for nom, conf in (("clé de répétition en mode réel", {**config, rg.CLE_REPETITION: []}),
                  ("regle_validation absente", {k: v for k, v in config.items() if k != "regle_validation"}),
                  ("seuil_lecture_lot hors [0, 1]", {**config, "seuil_lecture_lot": 1.5}),
                  ("combinaisons_max_validation ≠ combinaisons_max", {**config, "combinaisons_max_validation": 16})):
    try:
        rl.exiger_config(conf); print("ÉCHEC : garde muette", nom)
    except GardeArret as e:
        print(f"artefact {nom} : arrêt ({str(e)[:70]})")
print("R3 sur le dossier temporaire : exécutions antérieures (validation, résolution) =",
      rg.executions_anterieures(R, config, "validation"), rg.executions_anterieures(R, config, "resolution"))

# ---- 3. pièces, ouverture, classement
t0 = time.time()
p = rg.charger_pieces(config, Path("."))
print("pièces chargées en %.1f s ; épisodes %d ; actions %d" % (time.time() - t0, len(p.par_episode), len(p.lignes)))
from transformers import AutoTokenizer
from controle_ia.harnais.formats import FormatChat
tok = AutoTokenizer.from_pretrained(str(TOK))
fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
fmt.fins = {int(x) for x in p.table["fins_du_format"]} | {fmt._pieces(("x", "y"))["cloture"][0]}
T = int(config["T"])
e0 = rg.EpisodeP3(p, next(iter(p.par_episode)), T).env()
rg.exiger_ouverture(fmt, e0, config["agent"]["texte_attendu_ouverture"], True)
print("ouverture : texte attendu présent (exiger_ouverture passe)")
t0 = time.time()
cl = rg.classer(p, fmt, T)
val = rg.episodes_de_l_etape("validation", config, cl)
res = rg.episodes_de_l_etape("resolution", config, cl)
rg.exiger_seuil_atteignable(config["seuil_validation"], len(val))
rg.exiger_compte_validation(len(val), config["seuil_validation"])
nr = [e for e, x in cl.items() if x["entree"] and x["entree"]["methode"] == "non_resolu"]
print("classement %.1f s : identiques de base %d ; corrigés par la table %d ; non résolus de la table %d ; validation %d "
      "(exiger_compte_validation passe) ; résolution %d" % (
          time.time() - t0, sum(x["identique_base"] for x in cl.values()),
          sum(1 for x in cl.values() if x["entree"] and x["entree"]["methode"] != "non_resolu"), len(nr), len(val),
          len(res)))
C6 = res[:3]
print("résolution : les 3 de C-6 en tête, à identifiants connus :",
      all(cl[e]["entree"] and cl[e]["entree"]["methode"] != "non_resolu" and rg.verite(p, fmt, T, cl, e) is not None
          for e in C6), "; les 4 suivants = les non résolus de la table v2 :", sorted(res[3:]) == sorted(nr))

# ---- 4. plan des lots de P3, lots des 4 non résolus, lignes exactes / approchées, cibles du lot
from controle_ia.environnements.pilote_a import charger_taches
taille = rl.exiger_meme_lot_que_p3(config, p.manifeste_p3)
lots = rl.plan_des_lots(charger_taches(config["chemin_taches"]), taille, p.lignes)
print(f"plan des lots de P3 (taille {taille}, noyau {config['noyau_attention']} comme P3) : {len(lots)} lots, "
      f"tailles {sorted(collections.Counter(len(x) for x in lots).items())} ; vérifié contre l'ordre des textes")
for e in sorted(nr, key=lambda x: rl.lot_de(lots, x)[0]):
    k, lot, rang = rl.lot_de(lots, e)
    lignes = rl.lignes_du_lot(p, fmt, T, cl, lot, e)
    sources = collections.Counter(x.source for x in lignes if x.source != rl.SOURCE_CIBLE)
    print(f"  cible {e} : lot {k}, rang {rang} ; voisines exactes {sum(1 for x in lignes if x.exacte) - 1}, approchées "
          f"{sum(1 for x in lignes if not x.exacte)} ; sources {dict(sorted(sources.items()))}")
for nom, nrv1 in (("les 4 non résolus et un de C-6", nr + C6[:1]), ("aucun non résolu", [])):
    cibles, hors = rl.cibles_du_lot(config, p, nrv1, vide_permis=True)
    print(f"cibles du lot si le cœur laisse {nom} : {len(cibles)} cible(s) ; hors cibles {len(hors)} "
          f"({'C-6' if hors and 'C-6' in hors[0]['cause'] else '—'})")

# ---- 5. graines
par_tache = collections.defaultdict(set)
for e in p.par_episode:
    ep = rg.EpisodeP3(p, e, T)
    assert len(ep.graines) == T and len(set(ep.graines)) == T
    par_tache[ep.tache].add(tuple(ep.graines))
print("graines lues pour %d épisodes (T = %d, distinctes dans chaque épisode) ; tâches %d ; tâches à graines identiques "
      "entre conditions %d ; jeux distincts %d" % (len(p.par_episode), T, len(par_tache),
                                                   sum(len(v) == 1 for v in par_tache.values()),
                                                   len({g for v in par_tache.values() for g in v})))
print("équivalence du tirage (multinomial = argmax p / q, V = 128 256) :",
      rg.exiger_equivalence_tirage(128256))
pas_v = sum(sum(rg.EpisodeP3(p, e, T).jetons) for e in val)
pas_r = sum(sum(rg.EpisodeP3(p, e, T).jetons) for e in res)
pas_l = sum(sum(rg.EpisodeP3(p, e, T).jetons) for e in nr)
print("pas (jetons tirés) : validation", pas_v, "; résolution", pas_r, "; cibles possibles du lot", pas_l)
print("U+FFFD : dans les 7", sum(x["texte"].count(rg.FFFD) for e in res for x in rg.EpisodeP3(p, e, T).lignes),
      "; dans les 147", sum(x["texte"].count(rg.FFFD) for e in val for x in rg.EpisodeP3(p, e, T).lignes))
