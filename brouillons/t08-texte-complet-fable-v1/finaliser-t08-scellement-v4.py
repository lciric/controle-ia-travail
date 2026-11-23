#!/usr/bin/env python3
"""Remplit les cinq marqueurs restants du texte de T0.8, écrit le texte à sceller, son différentiel contre le gel et le
fichier des marqueurs que lit le programme de la configuration de la course.

Version 4 (mot de la session mère du 22 novembre, 21:35Z ; développeur de la chaîne de lancement) : comme la version 3,
plus le fichier des marqueurs `T0.8-marqueurs-scellement-v1.json` et son compagnon, écrits avec le texte, sous trois
contraintes :
  (1) **une seule source** : chaque valeur du fichier est lue, par une forme fixe (`FORMES`), dans la chaîne même qui est
      écrite dans le texte à la place de son marqueur (`remplissages`) ; aucune seconde saisie. Les trois marqueurs
      remplis ici sortent des arguments (commit, entropie, ligne de dépense) par cette chaîne ; les quatre remplis au
      brouillon 11 sortent des textes neufs épinglés (`valeurs_marqueurs_en_sections_gelees` pour trois d'entre eux, la
      même variable que contrôle le gel ; l'opération « marqueur GO_T08 rempli » pour `GO_T08`) ;
  (2) **code de T0.8 rejoué** : `configuration_v1.exiger_marqueurs` et `exiger_marqueurs_au_texte` sont joués, dans un
      processus à part, par le code de l'arbre `--src-code`, dont la tête doit être `--commit-code` (arbre propre sous
      `src/`), sur le fichier et sur une copie scellée du texte ; un arrêt n'écrit rien ;
  (3) **à la place de son marqueur, une seule fois** (limite VCT8-04 du code) : `controler_place` exige que chaque
      remplissage figure une seule fois dans le texte, que la forme lue dans ce remplissage égale le fichier, et que,
      hors des remplissages des sept marqueurs, chaque valeur figure exactement le nombre de fois déclaré
      (`CITATIONS_DECLAREES`, comptées par programme sur le brouillon 15 ; zéro pour toute autre valeur).
Version 3 : valeur du marqueur `LIGNE_MOT_LAZAR_T5_19` (GO-2026-11-22-122, option (a)). Version 2 : contre-lecture 8 (B-1,
M-8, m-2).

À jouer par la session mère, au scellement, depuis la racine du dépôt (branche qui porte ces brouillons) :

    PYTHONPATH=src python3 brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v4.py \
        --entree brouillons/T0.8-bases-boite-noire-v0-v1-brouillon15.md --sha-entree <empreinte du brouillon vérifié> \
        --rapport-verification <chemin du rapport de vérification des corrections> \
        --commit-code <40 caractères> --empreintes-code <pièce des empreintes du code aligné> \
        --contre-lecture-code <rapport de contre-lecture de l'alignement> \
        --src-code <dossier src d'un arbre extrait au commit du code, propre> \
        --ligne-gardes R-XXXX --ligne-depense "<date> : engagement, T0.8, GO-2026-11-10-12, GO-2026-11-22-79" \
        [--entropie <entier déjà tiré et consigné>] [--a-blanc] [--dossier-sortie prereg]

Ordre : (1) arguments, compagnons, textes neufs épinglés ; (2) brouillon d'entrée épinglé ; (3) les trois sorties et le
compagnon du fichier des marqueurs n'existent pas (R12) ; (4) entropie, une fois ; (5) remplissage, chaque marqueur une
seule fois ; (5 bis) marqueurs lus dans les remplissages ; (6) contrôle du gel ; (7) validateur ; (7 bis) contrôle « à la
place » ; (7 ter) code de T0.8 au commit, rejoué ; (8) écriture du texte, du différentiel, du fichier des marqueurs et de
son compagnon. Il ne scelle pas le texte et n'écrit dans aucun registre.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import controle_gel_t08_v1 as gel  # noqa: E402

TEXTES = ICI / "textes-neufs-t08-brouillon12-v1.json"
SHA_TEXTES = "2b89c5c88bc0fc05e1f2e88b28a2f8698c38da0bd287959d7a4f56ef34360c7f"
TEXTES_B11 = ICI / "textes-neufs-t08-brouillon11-v1.json"
SHA_TEXTES_B11 = "f4eea2c85aa5877c738f5f02b56fa04d794a8d072d261d84050f86a1350db37e"
MOTIF_GO = "marqueur GO_T08 rempli"
NOM_SORTIE = "T0.8-bases-boite-noire-v0-v1.md"
NOM_DIFF = "T0.8-bases-boite-noire-v0-v1-differentiel-gel-v1.md"
NOM_MARQUEURS = "T0.8-marqueurs-scellement-v1.json"
MARQUEURS = ("COMMIT_CODE_T08", "ENTROPIE_T08", "LIGNE_DEPENSE_T08", "LIGNE_MOT_LAZAR_T5_19", "VERIFICATION_CL8_T08")
EN_SECTION_GELEE = ("ENTROPIE_T08", "LIGNE_MOT_LAZAR_T5_19")
# les sept marqueurs que lit le code de la course (configuration_v1.MARQUEURS)
MARQUEURS_MACHINE = ("COMMIT_CODE_T08", "CODE_MOTS_ET_COUT_T06", "RUN_7B", "EMPREINTES_ENTREES_7B", "ENTROPIE_T08",
                     "GO_T08", "LIGNE_DEPENSE_T08")
PREALABLES = ("CODE_MOTS_ET_COUT_T06", "RUN_7B", "EMPREINTES_ENTREES_7B")     # remplis au brouillon 11, sections gelées
FICHIERS_7B = ("mesures-t06.npz", "textes-actions-t06.jsonl", "episodes-t06.json", "manifeste.json", "lecture-cout-t06.json")
# à blanc seulement : jamais écrite, jamais une graine ; longue (chiffres de e), pour que le contrôle « à la place » la
# compte comme une vraie entropie (la version 3 prenait 1, présent partout dans le texte)
ENTROPIE_FICTIVE = 271828182845904523536028747135266249775
NON_SCELLE = "**non scellé** ; il ne vaut pas préenregistrement (R1)"
A_SCELLER = ("**texte à sceller** : les cinq derniers marqueurs sont remplis par programme ; il vaut préenregistrement à "
             "l'inscription de la ligne `SCELLEMENT-T08` (R1)")

_H40, _H64 = r"[0-9a-f]{40}", r"[0-9a-f]{64}"
# forme de chaque remplissage (correspondance entière) ; les groupes nommés sont les valeurs du fichier des marqueurs
FORMES = {
    "COMMIT_CODE_T08": re.compile(rf"`(?P<v>{_H40})` \(pièce de ses empreintes `[^`]+`, `{_H64}` ; contre-lecture de "
                                  rf"l'alignement `[^`]+`, `{_H64}`\)"),
    "ENTROPIE_T08": re.compile(r"`(?P<v>[1-9][0-9]*)`"),
    "LIGNE_DEPENSE_T08": re.compile(r"ligne inscrite au scellement : (?P<v>[^\n]*T0\.8[^\n]*)"),
    "CODE_MOTS_ET_COUT_T06": re.compile(
        rf"ligne du \d{{4}}-\d{{2}}-\d{{2}}T\d{{2}}:\d{{2}}:\d{{2}}Z, qui cite le fichier d'inscription "
        rf"`(?P<fichier_inscription>[^`]+)`, `(?P<sha256_inscription>{_H64})` : commit `(?P<commit>{_H40})`, module "
        rf"`(?P<module>[^`]+)`, `(?P<sha256_module>{_H64})`, lanceur `[^`]+`, `{_H64}` ; R-\d+"),
    "RUN_7B": re.compile(
        rf"run `(?P<run_id>[0-9]{{8}}-[0-9]{{6}}-[a-z0-9-]+)`, branche de sortie `(?P<branche>[^`]+)` \(tête `{_H40}`\), "
        rf"manifeste `runs/(?P<run_chemin>[^`/]+)/manifeste\.json`, `(?P<manifeste_sha256>{_H64})` ; ligne inscrite le "
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"),
    "EMPREINTES_ENTREES_7B": re.compile(
        r"lues le \d{4}-\d{2}-\d{2} sur les compagnons seuls, sans ouvrir les fichiers : "
        + " ; ".join(f"`{re.escape(f)}`, `(?P<f{i}>{_H64})`" for i, f in enumerate(FICHIERS_7B))),
    "GO_T08": re.compile(r"`(?P<id>GO-\d{4}-\d{2}-\d{2}-\d{2})` \(type « calcul », plafond (?P<plafond_usd>[1-9][0-9]*) USD, "
                         r"[^\n]*"),
}
# Citations hors des remplissages des sept marqueurs, déclarées : comptées par programme sur le brouillon 15 ; toute autre
# valeur : zéro. Un autre brouillon d'entrée qui les change arrête le programme (comptes à revoir, nouvelle version).
CITATIONS_DECLAREES = {
    "GO_T08.id": 9,                        # l'accord : en-tête, devis, ligne d'engagement proposée, calendrier, faits, décisions
    "RUN_7B.run_id": 1,                    # « Faits du registre » : course de confirmation 7b jouée
    "RUN_7B.branche": 1,                   # même phrase
    "CODE_MOTS_ET_COUT_T06.module": 1,     # contrat lu par T0.8 (section « Depuis le gel »)
    "CODE_MOTS_ET_COUT_T06.sha256_module": 1,
}
NON_COMPTEES = {"GO_T08.plafond_usd": "nombre court (« 120 ») cité partout ; la configuration contrôle à part la phrase "
                                      "« 120 USD cumulés »",
                "LIGNE_DEPENSE_T08": "phrase entière, tenue par son remplissage (une seule occurrence)"}


def arret(message: str):
    raise SystemExit("ARRÊT : " + message)


def compagnon_conforme(chemin: Path) -> str:
    c = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not c.is_file():
        arret(f"{chemin} : fichier ou compagnon .sha256 absent (R6)")
    s = gel.sha(chemin.read_bytes())
    if c.read_text(encoding="utf-8").split()[0] != s:
        arret(f"{chemin} : empreinte ≠ compagnon (R11)")
    return s


def lire_json_epingle(chemin: Path, attendu: str) -> dict:
    octets = chemin.read_bytes()
    if gel.sha(octets) != attendu:
        arret(f"{chemin} : empreinte {gel.sha(octets)} ≠ {attendu} épinglée (R11)")
    return json.loads(octets.decode("utf-8"))


def remplissages_prealables(neufs: dict, neufs_b11: dict) -> dict[str, str]:
    """Remplissages des quatre marqueurs remplis au brouillon 11, lus dans les textes neufs épinglés (mêmes variables
    que celles qu'emploient le gel et le brouillon 11)."""
    r = {m: neufs["valeurs_marqueurs_en_sections_gelees"][m] for m in PREALABLES}
    ops = [o for o in neufs_b11["operations"] if o.get("motif") == MOTIF_GO]
    if len(ops) != 1:
        arret(f"textes neufs du brouillon 11 : opération « {MOTIF_GO} » : {len(ops)} trouvée(s), une attendue")
    r["GO_T08"] = ops[0]["nouveau"]
    return r


def analyser(nom: str, remplissage: str):
    """Valeur du marqueur `nom` lue dans son remplissage, par sa forme fixe ; arrêt si la forme n'est pas tenue."""
    m = FORMES[nom].fullmatch(remplissage)
    if m is None:
        arret(f"remplissage du marqueur {nom} : forme non tenue ({remplissage[:80]!r}…)")
    g = m.groupdict()
    if nom in ("COMMIT_CODE_T08", "LIGNE_DEPENSE_T08"):
        return g["v"]
    if nom == "ENTROPIE_T08":
        return int(g["v"])
    if nom == "CODE_MOTS_ET_COUT_T06":
        return {k: g[k] for k in ("commit", "fichier_inscription", "sha256_inscription", "module", "sha256_module")}
    if nom == "RUN_7B":
        if g["run_chemin"] != g["run_id"]:
            arret("RUN_7B : le chemin du manifeste ne porte pas l'identifiant du run")
        return {"run_id": g["run_id"], "branche": g["branche"], "manifeste_sha256": g["manifeste_sha256"]}
    if nom == "EMPREINTES_ENTREES_7B":
        return {f: g[f"f{i}"] for i, f in enumerate(FICHIERS_7B)}
    return {"id": g["id"], "plafond_usd": int(g["plafond_usd"])}          # GO_T08


def marqueurs_de(remplissages: dict[str, str]) -> dict:
    return {m: analyser(m, remplissages[m]) for m in MARQUEURS_MACHINE}


def feuilles(marqueurs: dict) -> dict[str, str]:
    """Nom → valeur (texte) de chaque valeur du fichier des marqueurs."""
    out = {}
    for m, v in marqueurs.items():
        if isinstance(v, dict):
            for k, x in v.items():
                out[f"{m}[{k}]" if m == "EMPREINTES_ENTREES_7B" else f"{m}.{k}"] = str(x)
        else:
            out[m] = str(v)
    return out


def _occurrences(texte: str, valeur: str) -> list[int]:
    """Positions de `valeur` dans `texte`, bornée comme dans le code de T0.8 (`configuration_v1._tel_quel`)."""
    return [x.start() for x in re.finditer(r"(?<![0-9A-Za-z_-])" + re.escape(valeur) + r"(?![0-9A-Za-z_-])", texte)]


def compter_hors(texte: str, remplissages: dict[str, str], marqueurs: dict) -> dict[str, int]:
    spans = []
    for m in MARQUEURS_MACHINE:
        f = remplissages[m]
        n = texte.count(f)
        if n != 1:
            arret(f"contrôle « à la place » : remplissage du marqueur {m} : {n} occurrence(s) dans le texte, une seule attendue")
        i = texte.index(f)
        spans.append((i, i + len(f)))
    return {cle: len([p for p in _occurrences(texte, v) if not any(a <= p < b for a, b in spans)])
            for cle, v in feuilles(marqueurs).items() if cle not in NON_COMPTEES}


def controler_place(texte: str, remplissages: dict[str, str], marqueurs: dict) -> dict[str, int]:
    """Contrainte (3) : chaque valeur du fichier des marqueurs est celle écrite à la place de son marqueur, dont le
    remplissage figure une seule fois ; hors des remplissages des sept marqueurs, chaque valeur figure exactement le
    nombre de fois déclaré. Arrêt sinon ; rend les comptes."""
    if not isinstance(marqueurs, dict) or set(marqueurs) != set(MARQUEURS_MACHINE):
        arret(f"fichier des marqueurs : clés {sorted(marqueurs) if isinstance(marqueurs, dict) else marqueurs!r} ≠ les sept attendues")
    comptes = compter_hors(texte, remplissages, marqueurs)
    for m in MARQUEURS_MACHINE:
        if analyser(m, remplissages[m]) != marqueurs[m]:
            arret(f"contrôle « à la place » : valeur du marqueur {m} dans le fichier ≠ celle écrite à sa place dans le texte")
    for cle, n in comptes.items():
        if n != CITATIONS_DECLAREES.get(cle, 0):
            arret(f"contrôle « à la place » : valeur {cle} : {n} occurrence(s) hors des remplissages des marqueurs, "
                  f"{CITATIONS_DECLAREES.get(cle, 0)} déclarée(s)")
    return comptes


def code_au_commit(src_code: Path, commit: str) -> None:
    """L'arbre de `src_code` (dossier `src` d'une extraction) est à la tête `commit`, propre sous ce dossier."""
    try:
        tete = subprocess.run(["git", "-C", str(src_code), "rev-parse", "HEAD"], capture_output=True, text=True,
                              check=True).stdout.strip()
        sale = subprocess.run(["git", "-C", str(src_code), "status", "--porcelain", "--untracked-files=all", "--", "."],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as e:
        arret(f"--src-code {src_code} : arbre git illisible ({e})")
    if tete != commit:
        arret(f"--src-code : tête {tete} ≠ --commit-code {commit} : le code rejoué n'est pas celui que cite le texte")
    if sale:
        arret(f"--src-code : arbre non propre ({sale.splitlines()[0]}…)")
    if not (src_code / "controle_ia" / "t08" / "configuration_v1.py").is_file():
        arret("--src-code : controle_ia/t08/configuration_v1.py absent")


VERIF_CODE = """
import json, sys
from pathlib import Path
from controle_ia.t08 import configuration_v1 as cf
mq = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
cf.exiger_marqueurs(mq)
print(json.dumps(cf.exiger_marqueurs_au_texte(sys.argv[2], mq)))
"""


def rejouer_code(src_code: Path, texte: str, contenu_marqueurs: str) -> dict:
    """Contrainte (2) : le code de T0.8 au commit rejoue ses deux contrôles sur le fichier des marqueurs et sur une copie
    scellée du texte, dans un processus à part (son paquet ne se mêle pas à celui de cet arbre)."""
    with tempfile.TemporaryDirectory() as d:
        t, j = Path(d) / NOM_SORTIE, Path(d) / NOM_MARQUEURS
        t.write_text(texte, encoding="utf-8")
        Path(str(t) + ".sha256").write_text(f"{gel.sha(texte.encode('utf-8'))}  {t.name}\n", encoding="utf-8")
        j.write_text(contenu_marqueurs, encoding="utf-8")
        env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
        env["PYTHONPATH"] = str(src_code.resolve())
        r = subprocess.run([sys.executable, "-B", "-c", VERIF_CODE, str(j), str(t)], capture_output=True, text=True,
                           env=env, cwd=d)
    if r.returncode != 0:
        dernier = (r.stderr.strip().splitlines() or ["?"])[-1]
        arret(f"code de T0.8 au commit : exiger_marqueurs ou exiger_marqueurs_au_texte refuse : {dernier[:200]}")
    return json.loads(r.stdout.strip().splitlines()[-1])


def main() -> int:
    p = argparse.ArgumentParser()
    for nom in ("--entree", "--sha-entree", "--rapport-verification", "--commit-code", "--empreintes-code",
                "--contre-lecture-code", "--src-code", "--ligne-gardes", "--ligne-depense"):
        p.add_argument(nom, required=True)
    p.add_argument("--entropie", type=int)
    p.add_argument("--a-blanc", action="store_true")
    p.add_argument("--dossier-sortie", default="prereg")
    a = p.parse_args()

    # (1) arguments, compagnons, textes neufs épinglés
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit_code):
        arret("--commit-code : 40 caractères hexadécimaux attendus")
    if not re.fullmatch(r"[0-9a-f]{64}", a.sha_entree):
        arret("--sha-entree : 64 caractères hexadécimaux attendus")
    if not re.fullmatch(r"R-\d{3,5}", a.ligne_gardes):
        arret("--ligne-gardes : une clé du registre des décisions, de la forme R-1234")
    if "T0.8" not in a.ligne_depense or "\n" in a.ligne_depense:
        arret("--ligne-depense : une seule ligne, qui cite T0.8 (le code de la course l'exige)")
    if a.entropie is not None and a.entropie <= 0:
        arret("--entropie : entier positif attendu")
    sha_empreintes = compagnon_conforme(Path(a.empreintes_code))
    sha_cl_code = compagnon_conforme(Path(a.contre_lecture_code))
    sha_verification = compagnon_conforme(Path(a.rapport_verification))
    if a.commit_code not in Path(a.empreintes_code).read_text(encoding="utf-8"):
        arret("la pièce des empreintes ne cite pas le commit donné")
    if a.sha_entree not in Path(a.rapport_verification).read_text(encoding="utf-8"):
        arret("le rapport de vérification ne cite pas l'empreinte du brouillon d'entrée : ce n'est pas le brouillon vérifié (R2)")
    neufs = lire_json_epingle(TEXTES, SHA_TEXTES)
    neufs_b11 = lire_json_epingle(TEXTES_B11, SHA_TEXTES_B11)
    src_code = Path(a.src_code)

    # (2) brouillon d'entrée épinglé (M-8)
    entree = Path(a.entree)
    if compagnon_conforme(entree) != a.sha_entree:
        arret("brouillon d'entrée : empreinte ≠ --sha-entree ; seul le brouillon déclaré conforme par la vérification se scelle (R2)")
    texte = entree.read_text(encoding="utf-8")
    restants = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    if restants != sorted(f"<<{m}>>" for m in MARQUEURS):
        arret(f"marqueurs du brouillon d'entrée : {restants} ; attendus : {list(MARQUEURS)}")

    # (3) sorties absentes, avant tout tirage (m-2)
    dossier = Path(a.dossier_sortie)
    sortie, diff_chemin, mq_chemin = dossier / NOM_SORTIE, dossier / NOM_DIFF, dossier / NOM_MARQUEURS
    if not a.a_blanc:
        for chemin in (sortie, diff_chemin, mq_chemin, Path(str(mq_chemin) + ".sha256")):
            if chemin.exists():
                arret(f"{chemin} existe : on n'écrase jamais (R12) ; aucune entropie n'a été tirée")

    # (4) entropie
    if a.a_blanc:
        entropie = ENTROPIE_FICTIVE if a.entropie is None else a.entropie
    elif a.entropie is not None:
        entropie = a.entropie
    else:
        import numpy
        entropie = int(numpy.random.SeedSequence().entropy)

    # (5) remplissage
    valeurs = {
        "COMMIT_CODE_T08": (f"`{a.commit_code}` (pièce de ses empreintes `{a.empreintes_code}`, `{sha_empreintes}` ; "
                            f"contre-lecture de l'alignement `{a.contre_lecture_code}`, `{sha_cl_code}`)"),
        "ENTROPIE_T08": f"`{entropie}`",
        "LIGNE_DEPENSE_T08": f"ligne inscrite au scellement : {a.ligne_depense}",
        "LIGNE_MOT_LAZAR_T5_19": ("R-2657 (mot de Lazar inscrit le 14 novembre), GO-2026-11-22-122 (garde d'antériorité "
                                  f"gardée, option (a) ; sort de VT5-07) et {a.ligne_gardes} (trois autres gardes de code plus "
                                  "strictes confirmées)"),
        "VERIFICATION_CL8_T08": (f"rapport `{a.rapport_verification}`, `{sha_verification}` ; brouillon déclaré conforme : "
                                 f"`{a.entree}`, `{a.sha_entree}`"),
    }
    for nom, valeur in valeurs.items():
        jeton = f"`<<{nom}>>`"
        if texte.count(jeton) != 1:
            arret(f"marqueur {nom} : {texte.count(jeton)} occurrence(s) du jeton entre accents graves, une seule attendue")
        texte = texte.replace(jeton, valeur)
    if re.search(r"<<[A-Z0-9_]+>>", texte):
        arret("un marqueur reste après remplissage")
    lignes = texte.split("\n")
    statuts = [i for i, l in enumerate(lignes) if l.startswith("- **Statut** : ")]
    if len(statuts) != 1 or lignes[statuts[0]].count(NON_SCELLE) != 1:
        arret("ligne « Statut » ou sa phrase « non scellé » introuvable ou en double : statut à revoir à la main")
    lignes[statuts[0]] = lignes[statuts[0]].replace(NON_SCELLE, A_SCELLER)   # la ligne d'en-tête seule ; l'annexe reste à l'octet
    texte = "\n".join(lignes)

    # (5 bis) marqueurs lus dans les remplissages : une seule source (contrainte 1)
    remplissages = {**remplissages_prealables(neufs, neufs_b11),
                    **{m: valeurs[m] for m in ("COMMIT_CODE_T08", "ENTROPIE_T08", "LIGNE_DEPENSE_T08")}}
    contenu_marqueurs = json.dumps(marqueurs_de(remplissages), ensure_ascii=False, indent=1, sort_keys=True) + "\n"

    # (6) contrôle du gel
    toutes = dict(neufs["valeurs_marqueurs_en_sections_gelees"])
    toutes.update({m: valeurs[m] for m in EN_SECTION_GELEE})
    info = gel.controler_gel(texte, toutes)

    # (7) validateur, sur une copie temporaire
    sys.path.insert(0, "src")
    from controle_ia.prereg import problemes
    with tempfile.TemporaryDirectory() as d:
        copie = Path(d) / NOM_SORTIE
        copie.write_text(texte, encoding="utf-8")
        restes = problemes(copie)
    if restes:
        arret("validateur : " + " ; ".join(restes) + " ; rien n'est écrit")

    # (7 bis) à la place de son marqueur, une seule fois (contrainte 3), sur le fichier tel qu'il sera écrit
    comptes = controler_place(texte, remplissages, json.loads(contenu_marqueurs))

    # (7 ter) code de T0.8 au commit cité, rejoué (contrainte 2)
    code_au_commit(src_code, a.commit_code)
    rejeu = rejouer_code(src_code, texte, contenu_marqueurs)

    if a.a_blanc:
        print("à blanc : arguments, brouillon épinglé, cinq marqueurs, contrôle du gel, validateur, contrôle « à la place » "
              f"({len(comptes)} valeurs) et code de T0.8 au commit ({rejeu['valeurs_verifiees']} valeurs au texte) tenus ; "
              "aucune entropie tirée ; rien n'est écrit")
        return 0

    # (8) écriture
    sha_texte = gel.sha(texte.encode("utf-8"))
    sha_mq = gel.sha(contenu_marqueurs.encode("utf-8"))
    d = ["# Différentiel du texte de T0.8 à sceller contre le brouillon 4 gelé (ligne GEL-T08) — v1", "",
         "Produit par `brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v4.py` ; exigé par la règle « Gel vérifiable » du texte.", "",
         f"- Brouillon 4 gelé : `{gel.B4}`, `{gel.SHA_B4}` ; plage gelée, lignes {info['plage_b4'][0]} à {info['plage_b4'][1]}, `{info['sha_plage_b4']}`.",
         f"- Brouillon 10 : `{gel.B10}`, `{gel.SHA_B10}` ; plage gelée `{info['sha_plage_b10']}`.",
         f"- Brouillon d'entrée, déclaré conforme par la vérification : `{entree}`, `{a.sha_entree}` ; rapport de vérification `{a.rapport_verification}`, `{sha_verification}`.",
         f"- Texte à sceller : `{sortie}`, `{sha_texte}` ; plage gelée, lignes {info['plage_texte'][0]} à {info['plage_texte'][1]}, `{info['sha_plage_texte']}`.",
         f"- Fichier des marqueurs (lu par le programme de la configuration de la course) : `{mq_chemin}`, `{sha_mq}` ; "
         f"valeurs lues dans les remplissages du texte ; contrôle « à la place » tenu ({len(comptes)} valeurs comptées) ; "
         f"code de T0.8 au commit `{a.commit_code}` rejoué (`exiger_marqueurs`, `exiger_marqueurs_au_texte`) : tenu.", "",
         "**Contrôle par programme, tenu** : (a) la plage gelée du brouillon 10, une fois retirée la phrase T5-19, est égale à l'octet "
         "à celle du brouillon 4 ; (b) la plage gelée du texte à sceller, une fois remis le nom de chaque marqueur à la place de sa "
         "valeur, est égale à l'octet à celle du brouillon 10 : la phrase T5-19 y est celle du brouillon 10, dans son texte et à sa "
         f"place (rang {info['rang_t5_19']} de la plage ; empreinte épinglée `{gel.SHA_T5_19}`).", "",
         "## Phrase T5-19 (ajoutée au brouillon 5, gardée par le mot de Lazar ; ici avec le nom de son marqueur)", "",
         "> " + info["ligne_t5_19_b10"], "", "## Valeurs des marqueurs dans les sections gelées", ""]
    for nom, valeur in toutes.items():
        d += [f"- `{nom}` : {valeur}", ""]
    d += ["## Valeurs des marqueurs hors des sections gelées", ""]
    for nom in ("COMMIT_CODE_T08", "LIGNE_DEPENSE_T08", "VERIFICATION_CL8_T08"):
        d += [f"- `{nom}` : {valeurs[nom]}", ""]
    d += ["## Hors des sections gelées", "",
          "Le texte à sceller est le brouillon d'entrée, à l'octet, hors les cinq valeurs de marqueurs et la phrase de statut de "
          "l'en-tête (« non scellé » devient « texte à sceller »). Opérations depuis le brouillon 10 : "
          "`brouillons/t08-texte-complet-fable-v1/differentiel-gel-t08-brouillon11-v1.md` et les suivants, sections 3.", ""]
    sortie.write_text(texte, encoding="utf-8")
    diff_chemin.write_text("\n".join(d), encoding="utf-8")
    mq_chemin.write_text(contenu_marqueurs, encoding="utf-8")
    Path(str(mq_chemin) + ".sha256").write_text(f"{sha_mq}  {mq_chemin.name}\n", encoding="utf-8")
    print(f"écrit : {sortie} {sha_texte}")
    print(f"écrit : {diff_chemin}")
    print(f"écrit : {mq_chemin} {sha_mq} (et son compagnon)")
    print(f"entropie racine tirée (à consigner au registre des décisions) : {entropie}")
    print("suite, à la main : sceller le texte (controle_ia.prereg.sceller_prereg) et le différentiel ; écrire la "
          f"configuration de la course avec --marqueurs {mq_chemin} ; texte, configuration et fichier des marqueurs dans le "
          "même commit S ; inscrire SCELLEMENT-T08, puis CODE-T08 ; passage à blanc sur le registre réel ; alors seulement la "
          "création de l'instance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
