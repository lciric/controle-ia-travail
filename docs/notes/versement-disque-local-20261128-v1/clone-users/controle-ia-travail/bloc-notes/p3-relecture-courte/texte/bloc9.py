import json, re, sys
from pathlib import Path
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.manifeste import graines
from controle_ia.premier_test_ia import donnees as dn
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.conditions import charger_consignes
from controle_ia.scellement import verifier
p, cfg, taches, cfg_pilote, versees = sys.argv[1:6]
racine = Path(".")
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
rp.exiger_config_p3(c)
assert c["mode"] == "reel", f"mode {c['mode']}"
assert c["duree_max_s"] == 16200 and c["budget_entrainement_s"] == 3600, "durées de la configuration"
assert c["n_faits_max"] is None, "n_faits_max non nul : les faits comptés au bloc 10 ne seraient plus ceux du run (CH-19)"
assert c["chemin_consignes"] == "prereg/P3-consignes-v1.md", "chemin des consignes de la configuration"
# environnement et génération : ceux du pilote (même agent, même révision, mêmes réglages d'épisode et de garde)
pil = json.loads(Path(cfg_pilote).read_text(encoding="utf-8"))
communs = ("N", "T", "actions_min_controle_negatif", "agent", "couches", "fils", "fraction_equivalence",
           "fraction_min_controle_negatif", "lot", "max_nouveaux", "noyau_attention", "positions_min_controle_negatif",
           "statistique_equivalence", "temperature", "tolerance_equivalence")
autres = [k for k in communs if c.get(k) != pil.get(k)]
assert not autres, f"paramètres différents de ceux du pilote : {autres}"
# bornes des scripts de l'instance (délai externe du run, plafond de l'amorce) et des copies versées (crédit, prix,
# surveillance, offre) : une seule ligne chacune, à la valeur du préenregistrement
inst = Path("scripts/p3_instance.sh").read_text(encoding="utf-8")
amorce = Path("scripts/amorce_instance_p3.sh").read_text(encoding="utf-8")
assert inst.count("DELAI=(timeout --signal=TERM --kill-after=5m 300m)") == 1, "délai externe du run"
assert amorce.count("timeout --signal=TERM --kill-after=5m 360m ") == 1, "plafond de l'amorce"
lanceur = Path(f"{versees}/lancer_p3_v1.sh").read_text(encoding="utf-8")
surv = Path(f"{versees}/surveiller_p3_v1.sh").read_text(encoding="utf-8")
cinq = Path(f"{versees}/controle_cinq_minutes_p3_v1.sh").read_text(encoding="utf-8")
def constante(texte, nom, motif=r"[0-9.]+"):
    return re.findall(rf"^{nom}=({motif}) ", texte, re.M)
assert constante(lanceur, "HEURES_CREDIT") == ["6.5"], "heures du crédit exigé"
assert constante(lanceur, "PRIX_MAX") == ["1.30"], "prix plafond du lanceur"
assert constante(cinq, "PRIX_MAX") == ["1.30"], "prix plafond du contrôle à cinq minutes"
assert constante(lanceur, "PLAFOND_SURVEILLANCE_S") == ["22200"], "plafond de la surveillance écrit par le lanceur"
assert constante(surv, "PLAFOND_S") == ["22200"], "plafond de la surveillance"
assert constante(lanceur, "COEURS_MIN") == ["16"], "cœurs effectifs exigés de l'offre"
assert constante(lanceur, "MEMOIRE_VIVE_MIN_MO") == ["128000"], "mémoire vive exigée de l'offre"
tel = constante(lanceur, "TELECHARGEMENT_MAX", r"[^ ]+")
assert len(tel) == 1 and re.fullmatch(r"0\.[0-9]{2,4}", tel[0]), f"borne de téléchargement du lanceur non fixée ({tel})"
texte = " ".join(Path(p).read_text(encoding="utf-8").split())
valeurs = ("16 200 s", "3 600 s", "300 minutes", "360 minutes", "22 200 s", "6,5 heures", "8,02 USD", "0,22 USD",
           "16 cœurs effectifs", "128 000 Mo", "72 heures", "7 faits", "200 sondes", "= 240 épisodes",
           "51 jetons pour chacune des trois consignes", "10 pour chacune des trois indications",
           "52 jetons pour les trois consignes sur 56 tâches et 51 sur 4", "10 pour les trois indications",
           f"téléchargement au plus {tel[0].replace('.', ',')} USD par Go")
for s in valeurs:
    assert s in texte, f"valeur non citée par le texte : {s}"
# gardes d'executer(), dans l'ordre, jusqu'au manifeste
t = charger_taches(taches)
sha_t = verifier(taches)
consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
charger_invite("H1-classification")
exiger_code_importe_sous(racine)
commit = exiger_code_cite(racine, Path(p))
ent = rp.exiger_citations_p3(Path(p), c, sha_t)
plan = rp.plan_p3(t)
assert len(plan) == 240, f"{len(plan)} épisodes au plan, 240 cités"
g = graines(rp.cles_des_graines(t, c), ent)
# données génériques : empreintes de la provenance (chargeurs du run)
faits = dn.charger_faits()
enjeux = dn.charger_enjeux()
print("commit cité :", commit, "; entropie citée :", ent, "; épisodes :", len(plan), "; graines :", len(g),
      "; faits :", len(faits), "; textes « enjeux élevés » :", len(enjeux), "; consignes :", consignes["sha256"][:12],
      "; téléchargement au plus", tel[0], "USD par Go")
