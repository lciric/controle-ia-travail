"""Contrôles mécaniques du brouillon 5 (hors du dépôt ; rien n'est écrit dans le clone), repris de ceux du brouillon 4
et de la vérification des corrections, plus les deux gardes changées par les corrections VCB.

Usage : PYTHONPATH=<clone>/src python -B controles_brouillon5.py <clone> <brouillon 4> <brouillon 5> <dossier neuf>
1. annexe A : lignes de début et de fin ; commande de `LISEZMOI.md`, telle qu'écrite, sur une copie nommée
   `T0.5-plan-B-juges-v1.md` ; bloc égal, octet pour octet, à celui du brouillon 4 ; `exiger_annexe_a_egale_a_rs1`
   (cas sain ; artefacts : un caractère changé, seconde ligne de fin après l'annexe, VCB-07) ;
2. lignes de citation : texte tel quel (marqueurs : refus attendu) ; copie aux marqueurs remplis de valeurs de bonne
   forme (cas sain) ; artefacts : résumé cité deux fois, commit cité deux fois avec deux valeurs (VCB-03) ; copies
   effacées ;
3. table « Configuration » : clés et ordre de `rq.CLES`, `exiger_config_planb`, égalité à `CONSTANTES_CONFIG`,
   `lr.exiger_config_de_l_etape` (rend `lot_juge`, VCB-02), clés égales au pilote.
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

CLONE, B4, B5, TRAVAIL = (Path(x) for x in sys.argv[1:5])
TRAVAIL.mkdir(parents=False, exist_ok=False)

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.harnais.validation_reelle import COMMIT_CITE, exiger_code_cite  # noqa: E402
from controle_ia.environnements import requalifier_juges as rq  # noqa: E402
from controle_ia.environnements import rubrique_simplifiee as rs  # noqa: E402
from controle_ia.environnements import lire_requalification as lr  # noqa: E402
from controle_ia.environnements.lancer_pilote_a import empreinte_config  # noqa: E402


def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def essai(nom, f, *a):
    try:
        r = f(*a)
        print(f"  {nom} : rend {r!r}")
        return r
    except GardeArret as e:
        print(f"  {nom} : arrêt (GardeArret) : {e}")
        return None


def bloc(t: str) -> str:
    lignes = t.split("\n")
    d = lignes.index(rs.DEBUT_ANNEXE_A)
    f = max(i for i, x in enumerate(lignes) if x.startswith(rs.FIN_ANNEXE_A))
    return "\n".join(lignes[d:f + 1])


texte = B5.read_text(encoding="utf-8")
print("brouillon 4 :", sha(B4))
print("brouillon 5 :", sha(B5), f"({texte.count(chr(10))} lignes)")

# ------------------------------------------------------------------------------------------------ 1. annexe A
print("1. annexe A")
lignes = texte.split("\n")
print(f"  lignes égales au début : {[i + 1 for i, x in enumerate(lignes) if x == rs.DEBUT_ANNEXE_A]} ; lignes qui "
      f"commencent par la fin : {[i + 1 for i, x in enumerate(lignes) if x.startswith(rs.FIN_ANNEXE_A)]}")
print("  bloc de l'annexe A égal à celui du brouillon 4, octet pour octet :",
      bloc(texte).encode("utf-8") == bloc(B4.read_text(encoding="utf-8")).encode("utf-8"))
lisezmoi = (rs.RACINE_INVITES_RS1 / "LISEZMOI.md").read_text(encoding="utf-8")
code, = re.findall(r'^python3 -I -c "(.*)" T0\.5-plan-B-juges-v1\.md$', lisezmoi, re.M)
copie = TRAVAIL / "lisezmoi"
copie.mkdir()
shutil.copy2(B5, copie / "T0.5-plan-B-juges-v1.md")
p = subprocess.run(["python3", "-I", "-c", code, "T0.5-plan-B-juges-v1.md"], cwd=copie, capture_output=True, text=True)
print("  commande de LISEZMOI.md sur la copie :", p.stdout.strip(), "(code", p.returncode, ")",
      "; copie = brouillon 5 :", sha(copie / "T0.5-plan-B-juges-v1.md") == sha(B5))
print("  empreinte de RS1.txt :", sha(rs.RACINE_INVITES_RS1 / "invites" / "RS1.txt"))
essai("cas sain, exiger_annexe_a_egale_a_rs1(brouillon 5)", rs.exiger_annexe_a_egale_a_rs1, B5)
cible = "    Score the whole set of proposals on four criteria."
fin = rs.FIN_ANNEXE_A + " After the JUSTIFICATION line, stop."
assert texte.count(cible) == 1 and texte.count(fin + "\n") == 1
for nom, altere in (("un caractère changé dans l'annexe A", texte.replace(cible, cible[:-2] + "A.", 1)),
                    ("seconde ligne de fin juste après l'annexe (VCB-07)", texte.replace(fin + "\n",
                                                                                          f"{fin}\n\n{fin}\n", 1))):
    q = TRAVAIL / "artefact-annexe.md"
    q.write_text(altere, encoding="utf-8")
    essai(f"artefact, {nom}", rs.exiger_annexe_a_egale_a_rs1, q)
    q.unlink()

# ------------------------------------------------------------------------------------------------ 3. configuration
print("3. table « Configuration »")
section = texte[texte.index("**Configuration** (`prereg/T0.5-plan-B-juges-config-v1.json`"):]
section = section[:section.index("\n\n**Avant le scellement**")]
config = {}
for m in re.finditer(r"^\| `([a-z0-9_]+)` \| `(.*)` \| .* \|$", section, re.M):
    assert m.group(1) not in config, m.group(1)
    config[m.group(1)] = json.loads(m.group(2))
print("  clés :", len(config), "; ordre de rq.CLES :", list(config) == list(rq.CLES))
essai("exiger_config_planb", rq.exiger_config_planb, config)
print("  écarts à lr.CONSTANTES_CONFIG :", {k: (config.get(k), v) for k, v in lr.CONSTANTES_CONFIG.items()
                                             if config.get(k) != v})
essai("lr.exiger_config_de_l_etape (rend lot_juge, VCB-02)", lr.exiger_config_de_l_etape, {"config": config},
      config["run_pilote"], config["manifeste_pilote_sha256"], config["run_notations"])
mp = json.loads((CLONE / "runs" / config["run_pilote"] / "manifeste.json").read_text(encoding="utf-8"))
print("  écarts au pilote (CLES_EGALES_AU_PILOTE) :",
      {k: (config[k], mp["config"].get(k)) for k in rq.CLES_EGALES_AU_PILOTE if config[k] != mp["config"].get(k)})
cfg_sha = empreinte_config(config)
print("  empreinte canonique de la table :", cfg_sha)

# ------------------------------------------------------------------------------------------------ 2. citations
print("2. lignes de citation")
rp, rn = config["run_pilote"], config["run_notations"]
attendus = {"configuration": cfg_sha, "run du pilote": rp, "manifeste du pilote": sha(CLONE / "runs" / rp /
                                                                                      "manifeste.json"),
            "épisodes du pilote": sha(CLONE / "diag" / rp / "episodes.json"),
            "tâches": sha(CLONE / "donnees/t05-pilote-v1/taches-pilote-60-v1.json"), "run des notations": rn,
            "manifeste des notations": sha(CLONE / "runs" / rn / "manifeste.json"),
            "résumé des notations": sha(CLONE / "diag" / rn / "resume.json"),
            "invite RS1": sha(rs.RACINE_INVITES_RS1 / "invites" / "RS1.txt"),
            "index de l'invite RS1": sha(rs.RACINE_INVITES_RS1 / "index.json")}
notations = {j: sha(CLONE / "diag" / rn / f"notations-{j}-decisives.json") for j in ("8B", "3B")}
essai("texte tel quel, exiger_citations_planb", rq.exiger_citations_planb, B5, attendus, notations)
essai("texte tel quel, exiger_code_cite", exiger_code_cite, CLONE, B5)
commit = subprocess.run(["git", "-C", str(CLONE), "rev-parse", "HEAD"], capture_output=True, text=True,
                        check=True).stdout.strip()
rempli = (texte.replace("`<<COMMIT_CODE>>`", f"`{commit}`").replace("`<<EMPREINTE_CONFIG>>`", f"`{cfg_sha}`")
          .replace("`<<ENTROPIE>>`", "`123456789012345678901234567890`"))
q = TRAVAIL / "T0.5-plan-B-juges-v1-rempli.md"
q.write_text(rempli, encoding="utf-8")
try:
    for nom, rx in list(rq.CITATIONS.items()) + [("commit", COMMIT_CITE), ("notations", rq.NOTATIONS_CITEES)]:
        print(f"  {nom:24s} occurrences : {len(rx.findall(rempli))}")
    essai("copie remplie, exiger_citations_planb", rq.exiger_citations_planb, q, attendus, notations)
    essai("copie remplie, exiger_code_cite", exiger_code_cite, CLONE, q)
    racine = subprocess.run(["git", "-C", str(CLONE), "rev-list", "--max-parents=0", "HEAD"], capture_output=True,
                            text=True, check=True).stdout.split()[0]
    for nom, (avant, apres) in {
            "résumé cité deux fois": ("- Résumé des notations rejoué : `",
                                      "- Résumé des notations rejoué : `" + "0" * 64 + "`\n- Résumé des notations "
                                                                                       "rejoué : `"),
            "commit cité deux fois, deux valeurs (VCB-03)": (f"- Commit du code d'analyse : `{commit}`\n",
                                                             f"- Commit du code d'analyse : `{commit}`\n- Commit du "
                                                             f"code d'analyse : `{racine}`\n")}.items():
        assert rempli.count(avant) == 1
        a = TRAVAIL / "artefact-citation.md"
        a.write_text(rempli.replace(avant, apres, 1), encoding="utf-8")
        essai(f"artefact, {nom}, exiger_code_cite", exiger_code_cite, CLONE, a)
        essai(f"artefact, {nom}, exiger_citations_planb", rq.exiger_citations_planb, a, attendus, notations)
        a.unlink()
finally:
    q.unlink()
print("copies aux valeurs factices effacées :", not any(TRAVAIL.glob("*.md")))
