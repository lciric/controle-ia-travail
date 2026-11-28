"""Vérification : lignes de citation et table « Configuration » du brouillon 4 face au code (lanceur et lecteur), et
valeurs citées face aux fichiers du clone. Copie aux marqueurs remplis écrite dans un dossier temporaire, puis effacée.
Usage : PYTHONPATH=<clone>/src python -B controle_citations_config_b4.py <brouillon 4> <clone> <dossier temporaire>"""
import hashlib, json, re, subprocess, sys
from pathlib import Path
from controle_ia.environnements import requalifier_juges as rq, lire_requalification as lr
from controle_ia.environnements.lancer_pilote_a import empreinte_config, TACHES_CITEES
from controle_ia.harnais.validation_reelle import exiger_code_cite, COMMIT_CITE, ENTROPIE_CITEE
from controle_ia.gardes import GardeArret
B4, D, TMP = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
texte = B4.read_text(encoding="utf-8")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
# table Configuration
debut = texte.index("**Configuration** (`prereg/T0.5-plan-B-juges-config-v1.json`")
fin = texte.index("**Avant le scellement**", debut)
config = {}
for l in texte[debut:fin].split("\n"):
    m = re.match(r"^\| `([a-z_0-9]+)` \| `(.*)` \| .* \|$", l)
    if m:
        assert m[1] not in config, m[1]
        config[m[1]] = json.loads(m[2])
print("clés de la table :", len(config), "; ordre = rq.CLES :", list(config) == list(rq.CLES),
      "; en plus :", sorted(set(config) - set(rq.CLES)), "; en moins :", sorted(set(rq.CLES) - set(config)))
rq.exiger_config_planb(config); print("exiger_config_planb : acceptée")
ecarts = {k: (config.get(k), v) for k, v in lr.CONSTANTES_CONFIG.items() if config.get(k) != v}
print("écarts à lr.CONSTANTES_CONFIG :", ecarts)
lr.exiger_config_de_l_etape({"config": config}, config["run_pilote"], config["manifeste_pilote_sha256"],
                            config["run_notations"]); print("lr.exiger_config_de_l_etape : acceptée")
pil = json.loads((D / "prereg/T0.5-pilote-config-v1.json").read_text(encoding="utf-8"))
mp = json.loads((D / "runs" / config["run_pilote"] / "manifeste.json").read_text(encoding="utf-8"))
print("écarts au pilote (CLES_EGALES_AU_PILOTE, manifeste) :",
      {k: (config[k], mp["config"].get(k)) for k in rq.CLES_EGALES_AU_PILOTE if config[k] != mp["config"].get(k)},
      "; variante du rejeu = variante_juge du pilote :", config["variante_rejeu"] == mp["config"].get("variante_juge"))
cfg_sha = empreinte_config(config); print("empreinte canonique de la table :", cfg_sha)
# valeurs citées face aux fichiers
rp, rn = config["run_pilote"], config["run_notations"]
attendus = {"configuration": cfg_sha, "run du pilote": rp,
            "manifeste du pilote": sha(D / "runs" / rp / "manifeste.json"),
            "épisodes du pilote": sha(D / "diag" / rp / "episodes.json"),
            "tâches": sha(D / "donnees/t05-pilote-v1/taches-pilote-60-v1.json"), "run des notations": rn,
            "manifeste des notations": sha(D / "runs" / rn / "manifeste.json"),
            "résumé des notations": sha(D / "diag" / rn / "resume.json"),
            "invite RS1": sha(D / "docs/sources/invites-plan-b-v1/invites/RS1.txt"),
            "index de l'invite RS1": sha(D / "docs/sources/invites-plan-b-v1/index.json")}
notations = {j: sha(D / "diag" / rn / f"notations-{j}-decisives.json") for j in ("8B", "3B")}
print("manifeste_pilote_sha256 de la table = manifeste du pilote :", config["manifeste_pilote_sha256"] == attendus["manifeste du pilote"])
# texte tel quel : refusé (marqueurs)
for f, args in ((rq.exiger_citations_planb, (B4, attendus, notations)), (exiger_code_cite, (D, B4))):
    try:
        f(*args); print(f.__name__, "texte tel quel : ACCEPTÉ")
    except GardeArret as e:
        print(f.__name__, "texte tel quel : refusé :", e)
# copie aux marqueurs remplis
commit = subprocess.run(["git", "-C", str(D), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
rempli = (texte.replace("`<<COMMIT_CODE>>`", f"`{commit}`").replace("`<<EMPROINTE>>`", "")
          .replace("`<<EMPREINTE_CONFIG>>`", f"`{cfg_sha}`").replace("`<<ENTROPIE>>`", "`123456789012345678901234567890`"))
p = TMP / "T0.5-plan-B-juges-v1-rempli.md"
p.write_text(rempli, encoding="utf-8")
try:
    for nom, rx in list(rq.CITATIONS.items()) + [("commit", COMMIT_CITE), ("notations", rq.NOTATIONS_CITEES)]:
        print(f"  {nom:24s} occurrences : {len(rx.findall(rempli))}")
    print("exiger_citations_planb (copie remplie) :", rq.exiger_citations_planb(p, attendus, notations))
    print("exiger_code_cite (copie remplie) :", exiger_code_cite(D, p))
    for nom, (avant, apres) in {"résumé cité deux fois": ("- Résumé des notations rejoué : `", "- Résumé des notations rejoué : `" + "0" * 64 + "`\n- Résumé des notations rejoué : `"),
                                "invite autre": ("Invite RS1 : `b1e3e003", "Invite RS1 : `11111111")}.items():
        q = TMP / "artefact.md"; q.write_text(rempli.replace(avant, apres, 1), encoding="utf-8")
        try:
            rq.exiger_citations_planb(q, attendus, notations); print("artefact", nom, ": ACCEPTÉ (défaut)")
        except GardeArret as e:
            print("artefact", nom, ": arrêt :", e)
        q.unlink()
finally:
    p.unlink()
