"""Contrôles mécaniques du brouillon 4 (hors du dépôt ; rien n'est écrit dans le clone).

Usage : PYTHONPATH=<clone>/src python -B controles_brouillon4.py <clone> <brouillon 4> <dossier de travail neuf>
1. annexe A : `exiger_annexe_a_egale_a_rs1` (cas sain ; artefact : un caractère changé) ; lignes de début et de fin ;
2. lignes de citation : `exiger_citations_planb` et `exiger_code_cite` sur le brouillon 4 tel quel (marqueurs : refus
   attendu), puis sur une copie aux marqueurs remplis de valeurs de bonne forme (cas sain), puis sur deux artefacts ;
3. table « Configuration » : `exiger_config_planb`, égalité à `CONSTANTES_CONFIG` du lecteur, à la configuration du
   pilote (clés égales au pilote) et à la configuration réelle des tests (`_config_reelle`).
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

CLONE, B4, TRAVAIL = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
TRAVAIL.mkdir(parents=False, exist_ok=False)

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.harnais.validation_reelle import exiger_code_cite  # noqa: E402
from controle_ia.environnements import requalifier_juges as rq  # noqa: E402
from controle_ia.environnements import rubrique_simplifiee as rs  # noqa: E402
from controle_ia.environnements import lire_requalification as lr  # noqa: E402
from controle_ia.environnements.lancer_pilote_a import empreinte_config  # noqa: E402
from controle_ia.scellement import empreinte  # noqa: E402


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def essai(nom, f, *a):
    try:
        r = f(*a)
        print(f"  {nom} : rend {r!r}")
        return r
    except GardeArret as e:
        print(f"  {nom} : arrêt (GardeArret) : {e}")
        return None


texte = B4.read_text(encoding="utf-8")
print("brouillon 4 :", sha(B4))

# ------------------------------------------------------------------------------------------------ 1. annexe A
print("1. annexe A")
lignes = texte.split("\n")
debuts = [i + 1 for i, x in enumerate(lignes) if x == rs.DEBUT_ANNEXE_A]
fins = [i + 1 for i, x in enumerate(lignes) if x.startswith(rs.FIN_ANNEXE_A)]
print(f"  lignes égales au début {rs.DEBUT_ANNEXE_A!r} : {debuts} ; lignes qui commencent par la fin : {fins}")
essai("cas sain, exiger_annexe_a_egale_a_rs1(brouillon 4)", rs.exiger_annexe_a_egale_a_rs1, B4)
cible = "    Score the whole set of proposals on four criteria."
assert texte.count(cible) == 1
altere = TRAVAIL / "brouillon4-annexe-alteree-d-un-caractere.md"
altere.write_text(texte.replace(cible, cible[:-2] + "A.", 1), encoding="utf-8")
essai("artefact, un caractère changé dans l'annexe A", rs.exiger_annexe_a_egale_a_rs1, altere)
altere.unlink()

# ------------------------------------------------------------------------------------------------ 2. citations
print("2. lignes de citation")
racine = CLONE
attendus_fichiers = {
    "manifeste du pilote": racine / "runs/20261012-105125-t05-pilote-reel/manifeste.json",
    "épisodes du pilote": racine / "diag/20261012-105125-t05-pilote-reel/episodes.json",
    "tâches": racine / "donnees/t05-pilote-v1/taches-pilote-60-v1.json",
    "manifeste des notations": racine / "runs/20261017-193648-t05-notations-reel/manifeste.json",
    "résumé des notations": racine / "diag/20261017-193648-t05-notations-reel/resume.json",
}
notations = {j: sha(racine / f"diag/20261017-193648-t05-notations-reel/notations-{j}-decisives.json")
             for j in ("8B", "3B")}

# table « Configuration » lue dans le brouillon 4 (valeurs JSON de la deuxième colonne)
section = texte[texte.index("**Configuration** (`prereg/T0.5-plan-B-juges-config-v1.json`"):]
section = section[:section.index("\n\n**Avant le scellement**")]
config = {}
for m in re.finditer(r"^\| `([a-z0-9_]+)` \| `(.*)` \| .* \|$", section, re.M):
    if m.group(1) in config:
        sys.exit(f"clé {m.group(1)} en double dans la table")
    config[m.group(1)] = json.loads(m.group(2))
print(f"  table « Configuration » : {len(config)} clés lues")

attendus = {"configuration": empreinte_config(config), "run du pilote": config["run_pilote"],
            "run des notations": config["run_notations"],
            "invite RS1": rs.empreinte_invite_rs1(), "index de l'invite RS1": empreinte(rs.RACINE_INVITES_RS1 / "index.json"),
            **{k: sha(p) for k, p in attendus_fichiers.items()}}
print("  valeurs attendues recalculées :", json.dumps({k: str(v)[:16] for k, v in attendus.items()}, ensure_ascii=False))

essai("brouillon 4 tel quel (marqueurs), exiger_citations_planb", rq.exiger_citations_planb, B4, attendus, notations)
essai("brouillon 4 tel quel (marqueurs), exiger_code_cite", exiger_code_cite, racine, B4)

tete = subprocess.run(["git", "-C", str(racine), "rev-parse", "HEAD"], capture_output=True, text=True,
                      check=True).stdout.strip()
ENTROPIE_FACTICE = "123456789012345678901234567890123456789"
remplis = (texte.replace("`<<COMMIT_CODE>>`", f"`{tete}`")
           .replace("`<<EMPREINTE_CONFIG>>`", f"`{attendus['configuration']}`")
           .replace("`<<ENTROPIE>>`", f"`{ENTROPIE_FACTICE}`")
           .replace("`<<TESTS_ATTENDUS>>`", "`1234`")
           .replace("`<<SHA256_AMORCE>>`", "`" + "a" * 64 + "`")
           .replace("`<<SHA256_SCRIPT_INSTANCE>>`", "`" + "b" * 64 + "`"))
assert "<<" not in remplis.replace("`<<NOM>>`", ""), "marqueur restant"
copie = TRAVAIL / "T0.5-plan-B-juges-v1.md"
copie.write_text(remplis, encoding="utf-8")
print(f"  copie aux marqueurs remplis : commit {tete} (tête du clone), empreinte de la configuration de la table, "
      f"entropie factice {ENTROPIE_FACTICE}, tests 1234, empreintes de scripts factices")
r = essai("copie remplie, exiger_citations_planb (cas sain)", rq.exiger_citations_planb, copie, attendus, notations)
assert r == int(ENTROPIE_FACTICE)
essai("copie remplie, exiger_code_cite (cas sain)", exiger_code_cite, racine, copie)
essai("copie remplie, exiger_annexe_a_egale_a_rs1 (cas sain)", rs.exiger_annexe_a_egale_a_rs1, copie)
# artefacts : une citation répétée avec une autre valeur ; une valeur différente de l'attendu
art = TRAVAIL / "artefact-citation-repetee.md"
art.write_text(remplis + f"\n- Résumé des notations rejoué : `{'0' * 64}`\n", encoding="utf-8")
essai("artefact, résumé des notations cité deux fois avec deux valeurs", rq.exiger_citations_planb, art, attendus,
      notations)
art.write_text(remplis.replace(f"Invite RS1 : `{attendus['invite RS1']}`", "Invite RS1 : `" + "1" * 64 + "`"),
               encoding="utf-8")
essai("artefact, invite RS1 citée avec une autre empreinte", rq.exiger_citations_planb, art, attendus, notations)
art.unlink()

# ------------------------------------------------------------------------------------------------ 3. configuration
print("3. table « Configuration »")
print("  clés du lanceur absentes de la table :", [c for c in rq.CLES if c not in config])
print("  clés de la table absentes du lanceur :", [c for c in config if c not in rq.CLES])
print("  ordre de la table égal à CLES :", list(config) == list(rq.CLES))
essai("exiger_config_planb(table)", rq.exiger_config_planb, config)
ecarts = {k: (config.get(k), v) for k, v in lr.CONSTANTES_CONFIG.items() if config.get(k) != v}
print("  écarts à CONSTANTES_CONFIG du lecteur :", ecarts)
print("  juges de la table :", [j["nom"] for j in config["juges"]], "; lot_juge :", config["lot_juge"])
pilote = json.loads((racine / "prereg/T0.5-pilote-config-v1.json").read_text(encoding="utf-8"))
print("  écarts aux clés égales au pilote (configuration scellée du pilote) :",
      {k: (config[k], pilote.get(k)) for k in rq.CLES_EGALES_AU_PILOTE if config[k] != pilote.get(k)},
      "; variante du rejeu = variante du pilote :", config["variante_rejeu"] == pilote.get("variante_juge"))
sys.path.insert(0, str(racine / "tests"))
import test_plan_b_requalifier as t  # noqa: E402
reelle = t._config_reelle()
ecarts_tests = {k: (config.get(k), reelle[k]) for k in reelle if config.get(k) != reelle[k]}
print("  écarts à _config_reelle() des tests (le manifeste du pilote y est factice) :",
      {k: (str(a)[:20], str(b)[:20]) for k, (a, b) in ecarts_tests.items()})
print("  empreinte canonique de la table :", attendus["configuration"])
