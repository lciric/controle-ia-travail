"""Outils des essais de la chaîne de P4-instrument (v1) : candidat d'essai, monde jouet, configuration réelle de
référence, textes synthétiques des fenêtres. Servent à la répétition jouet et aux bancs, jamais au lancement.

Aucun texte d'action de P3 n'est lu ni écrit ici : le monde jouet vient du run jouet de P3 des tests du module
(`test_instrument_p4_v1.construire_p3_jouet` : code gelé de P3, modèle jouet, données synthétiques) ; les textes des
fenêtres sont fabriqués ici, synthétiques. La configuration réelle de référence vient du module
(`config_de_reference`), avec B et B′ lus dans la sortie scellée des mesures de conception (phrases du texte, aucune
action).

Usage (Python de la session, -B ; PYTHONDONTWRITEBYTECODE=1) :
  outils_essais_p4_v1.py candidat BROUILLON SORTIE DEPOT COMMIT CONFIG_SHA TESTS [--jouet] [--rapport NOM=SHA …]
      candidat d'essai tiré du brouillon 4 : commit du code, empreinte canonique de la configuration, lignes « Module de
      P4 » (empreintes des fichiers de DEPOT/docs/procedures/P4-instrument-v1/), tests attendus, scripts de l'instance
      (empreintes des fichiers de DEPOT), ligne « Lancement », rapports cités ; --jouet : entropie et révision du jouet.
  outils_essais_p4_v1.py monde DEPOT MODULE TRAVAIL CONFIG_SORTIE
      run jouet de P3 (dans TRAVAIL), copié dans DEPOT (donnees/, diag/, runs/ ; données synthétiques sous
      donnees/synth/) ; configuration jouet de P4 écrite et scellée à CONFIG_SORTIE ; rend l'empreinte canonique.
  outils_essais_p4_v1.py config-reelle DEPOT MODULE SORTIE
      configuration réelle de référence (`config_de_reference`, B et B′ de la sortie scellée de MC-1), écrite et scellée.
  outils_essais_p4_v1.py jouet CANDIDAT SORTIE DEPOT CONFIG_SHA TESTS
      préenregistrement jouet de la répétition, tiré d'un candidat : quatre citations changées, une fois chacune
      (empreinte canonique de la configuration jouet, tests collectés, entropie et révision du modèle jouet), scellé par
      `sceller_prereg` du dépôt (R1/R2 : sections exigées) ; rien d'autre ne change.
  outils_essais_p4_v1.py fenetres SORTIE
      textes synthétiques au format du fichier des textes de P3 (quatre textes honnêtes longs et distinctifs, deux
      dégénérés d'un seul caractère répété, une ligne d'une autre condition), scellés.
Code 0, ou 1 avec un message ; 2 sur un usage faux.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True

DOSSIER_MODULE = "docs/procedures/P4-instrument-v1"
NOMS_MODULE = ("mesures_conception_p4_v1.py", "instrument_p4_v1.py", "lecture_p4_v1.py", "test_instrument_p4_v1.py",
               "test_lecture_p4_v1.py", "test_gardes_p4_v1.py")
AMORCE = f"{DOSSIER_MODULE}/amorce_instance_p4_v1.sh"
INSTANCE = f"{DOSSIER_MODULE}/p4_instance_v1.sh"
PREREG = "prereg/P4-instrument-v1.md"
BRANCHE = "calcul/p4-reel-v1"
ENTROPIE_JOUET = 20261020
REVISION_JOUET = "0" * 40
MC = "docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json"
# quatre textes honnêtes synthétiques, longs et distinctifs (au moins 64 caractères : fenêtres de 48 caractères)
TEXTES_FENETRES = (
    "ACTION: ADD\nTITLE: Synthetic probe zanzibar alpha\nPROPOSAL: Train a calibrated quokka probe on layer seven, "
    "then compare it with the frozen floor.\nCOST: 12\nPREDICTION: gain",
    "ACTION: EDIT\nTITLE: Synthetic probe zanzibar beta\nPROPOSAL: Replace the marmoset baseline by a held-out "
    "sweep over twelve synthetic tasks.\nCOST: 30\nPREDICTION: neutral",
    "ACTION: DROP\nTITLE: Synthetic probe zanzibar gamma\nPROPOSAL: Remove the axolotl ablation, which duplicates "
    "the second sweep on every synthetic task.\nCOST: 5\nPREDICTION: loss",
    # fenêtre du milieu à cheval sur un saut de ligne : échappée en JSON, visible seulement dans les chaînes décodées
    "ACTION: ADD\nTITLE: Synthetic zanzibar delta probe on layer fifteen\nPROPOSAL: Sweep the pangolin baseline twice "
    "on held-out tasks.\nCOST: 8",
)


def _sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _sceller(p: Path) -> str:
    e = _sha(p)
    Path(str(p) + ".sha256").write_text(f"{e}  {Path(p).name}\n", encoding="utf-8")
    return e


def _une(t: str, a: str, b: str) -> str:
    if t.count(a) != 1:
        raise SystemExit(f"candidat d'essai : « {a[:60]} » trouvé {t.count(a)} fois (une attendue)")
    return t.replace(a, b)


def candidat(brouillon: str, sortie: str, depot: str, commit: str, config_sha: str, tests: str, jouet: bool,
             rapports: list[str]) -> str:
    d = Path(depot)
    t = Path(brouillon).read_text(encoding="utf-8")
    t = _une(t, "Commit du code d'analyse : au candidat (le module de P4 n'est pas écrit).",
             f"Commit du code d'analyse : `{commit}`.")
    t = _une(t, "Configuration de P4 (empreinte canonique) : `<au candidat>`",
             f"Configuration de P4 (empreinte canonique) : `{config_sha}`")
    for n in NOMS_MODULE:
        c = f"{DOSSIER_MODULE}/{n}"
        t = _une(t, f"Module de P4 : `{c}` : `<empreinte au candidat>`", f"Module de P4 : `{c}` : `{_sha(d / c)}`")
    t = _une(t, "Tests attendus : au candidat (", f"Tests attendus : `{tests}` (")
    t = _une(t, "- Run source (P3) : ",
             f"- Scripts de l'instance, gelés par le scellement : `{AMORCE}` (`{_sha(d / AMORCE)}`, sha256) ; "
             f"`{INSTANCE}` (`{_sha(d / INSTANCE)}`, sha256).\n"
             f"- Lancement : `PREREG={PREREG}`, `BRANCHE={BRANCHE}`.\n- Run source (P3) : ")
    if rapports:
        cites = " ; ".join(f"`prereg/contre-lectures/{x.split('=', 1)[0]}` (`{x.split('=', 1)[1]}`)" for x in rapports)
        t = t.rstrip("\n") + f"\n- **Rapports versés (essai)** : {cites}.\n"
    if jouet:
        t = _une(t, "Entropie : `53867522133019232757448053239299230533`", f"Entropie : `{ENTROPIE_JOUET}`")
        t = _une(t, "Révision du modèle : `0e9e39f249a16976918f6564b8830bc894c89659`", f"Révision du modèle : `{REVISION_JOUET}`")
    Path(sortie).write_text(t, encoding="utf-8")
    return _sceller(Path(sortie))


def jouet(candidat_: str, sortie: str, depot: str, config_sha: str, tests: str) -> str:
    import re
    t = Path(candidat_).read_text(encoding="utf-8")
    for motif, valeur in ((r"Configuration de P4 \(empreinte canonique\) : `([0-9a-f]{64})`", config_sha),
                          (r"Tests attendus : `([0-9]+)`", str(tests)),
                          (r"Entropie : `([0-9]+)`", str(ENTROPIE_JOUET)),
                          (r"Révision du modèle : `([0-9a-f]{40})`", REVISION_JOUET)):
        if len(re.findall(motif, t)) != 1:
            raise SystemExit(f"citation absente ou en double dans le candidat : {motif}")
        t = re.sub(motif, lambda m: m.group(0).replace(m.group(1), valeur), t)
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(t, encoding="utf-8")
    sys.path.insert(0, str(Path(depot).resolve() / "src"))
    from controle_ia.prereg import sceller_prereg
    return sceller_prereg(p)


def _importer(depot: Path, module: Path):
    sys.path.insert(0, str(Path(depot).resolve() / "src"))
    sys.path.insert(0, str(Path(module).resolve()))
    import instrument_p4_v1 as ip  # noqa: E402
    return ip


def monde(depot: str, module: str, travail: str, config_sortie: str) -> dict:
    d, m = Path(depot).resolve(), Path(module).resolve()
    ip = _importer(d, m)
    import test_instrument_p4_v1 as t  # noqa: E402  (run jouet de P3 des tests du module)
    d3 = t.construire_p3_jouet(Path(travail).resolve() / "p3-jouet")
    run3 = t.RUN_P3
    for rel in (f"donnees/{run3}", f"diag/{run3}", f"runs/{run3}", "donnees/synth"):
        if (d / rel).exists():
            raise SystemExit(f"{rel} existe déjà dans le dépôt d'essai (R12)")
        shutil.copytree(d3 / rel, d / rel)
    shutil.copy(d3 / "taches.json", d / "donnees/synth/taches.json")
    _sceller(d / "donnees/synth/taches.json")
    cfg = t.config_p4_jouet(d3)
    cfg["empreintes_sources"]["taches"] = {"chemin": "donnees/synth/taches.json",
                                           "sha256": _sha(d / "donnees/synth/taches.json")}
    ip.exiger_config_p4(cfg)
    p = Path(config_sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(cfg, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    _sceller(p)
    return {"config": ip.empreinte_config(cfg), "entropie": ENTROPIE_JOUET, "revision": REVISION_JOUET, "run_p3": run3,
            "taches": len(cfg["taches_niveau_1"]), "T": cfg["T"]}


def config_reelle(depot: str, module: str, sortie: str) -> dict:
    d = Path(depot).resolve()
    ip = _importer(d, Path(module))
    mc = json.loads((d / MC).read_text(encoding="utf-8"))["MC-1"]
    cfg = ip.config_de_reference(mc["B"], mc["Bprime"])
    ip.exiger_config_p4(cfg)
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(cfg, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    _sceller(p)
    return {"config": ip.empreinte_config(cfg), "B": mc["B_nom"], "Bprime": mc["Bprime_nom"]}


def fenetres(sortie: str) -> dict:
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    lignes = [{"episode": f"honnete/t{k}/e0", "condition": "honnete", "tache": f"t{k}", "pas": 0, "texte": x}
              for k, x in enumerate(TEXTES_FENETRES)]
    lignes += [{"episode": "honnete/t3/e0", "condition": "honnete", "tache": "t3", "pas": 0, "texte": "." * 80},
               {"episode": "honnete/t4/e0", "condition": "honnete", "tache": "t4", "pas": 0, "texte": "=" * 80},
               {"episode": "saboteur/t0/e0", "condition": "saboteur", "tache": "t0", "pas": 0,
                "texte": "ACTION: ADD\nTITLE: Synthetic line of another condition, never read for the windows of P4.\n"}]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in lignes), encoding="utf-8")
    return {"textes": len(lignes), "sha256": _sceller(p)}


def main(argv: list[str]) -> int:
    if len(argv) >= 8 and argv[1] == "candidat":
        brouillon, sortie, depot, commit, config_sha, tests = argv[2:8]
        reste, mode_jouet, rapports = argv[8:], False, []
        while reste:
            if reste[0] == "--jouet":
                mode_jouet, reste = True, reste[1:]
            elif reste[0] == "--rapport" and len(reste) >= 2 and "=" in reste[1]:
                rapports.append(reste[1]); reste = reste[2:]
            else:
                print("usage : candidat … [--jouet] [--rapport NOM=SHA …]", file=sys.stderr)
                return 2
        print(candidat(brouillon, sortie, depot, commit, config_sha, tests, mode_jouet, rapports))
    elif len(argv) == 6 and argv[1] == "monde":
        print(json.dumps(monde(*argv[2:6])))
    elif len(argv) == 5 and argv[1] == "config-reelle":
        print(json.dumps(config_reelle(*argv[2:5]), ensure_ascii=False))
    elif len(argv) == 7 and argv[1] == "jouet":
        print(jouet(*argv[2:7]))
    elif len(argv) == 3 and argv[1] == "fenetres":
        print(json.dumps(fenetres(argv[2])))
    else:
        print("usage : candidat BROUILLON SORTIE DEPOT COMMIT CONFIG_SHA TESTS [--jouet] [--rapport NOM=SHA …] | "
              "monde DEPOT MODULE TRAVAIL CONFIG_SORTIE | config-reelle DEPOT MODULE SORTIE | "
              "jouet CANDIDAT SORTIE DEPOT CONFIG_SHA TESTS | fenetres SORTIE",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
