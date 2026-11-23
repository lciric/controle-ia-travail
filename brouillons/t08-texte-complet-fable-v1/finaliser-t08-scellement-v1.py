#!/usr/bin/env python3
"""Remplit les quatre marqueurs restants du texte de T0.8 et écrit le texte à sceller, avec son différentiel contre le gel.

À jouer par la session mère, au scellement, depuis la racine du dépôt, après : la contre-lecture du brouillon, le code
aligné et contre-lu, la ligne du registre qui confirme les gardes de code et dit le sort de VT5-07, et l'engagement.

    PYTHONPATH=src python3 brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v1.py \
        --entree brouillons/T0.8-bases-boite-noire-v0-v1-brouillon11.md \
        --commit-code <40 caractères> --empreintes-code <chemin de la pièce des empreintes> \
        --contre-lecture-code <chemin du rapport de contre-lecture de l'alignement> \
        --ligne-gardes R-XXXX --ligne-depense "<date> : engagement, T0.8, GO-2026-11-10-12" \
        [--entropie <entier déjà tiré>] [--a-blanc]

Ce qu'il fait : (1) tire l'entropie racine une seule fois (`numpy.random.SeedSequence().entropy`), sans lire aucune donnée,
sauf si `--entropie` redonne une entropie déjà tirée et consignée ; (2) remplace chaque marqueur, présent une seule fois ;
(3) rejoue le contrôle du gel : sections « Hypothèse » à « Liste d'arrêt » égales à l'octet au brouillon 4, hors la ligne
T5-19 et les valeurs de marqueurs ; (4) exige que le validateur `controle_ia.prereg.problemes` ne trouve rien ;
(5) écrit `prereg/T0.8-bases-boite-noire-v0-v1.md` et `prereg/T0.8-bases-boite-noire-v0-v1-differentiel-gel-v1.md`, sans
écraser (R12). Il ne scelle pas et n'écrit dans aucun registre : la session mère scelle les deux fichiers, puis inscrit
`SCELLEMENT-T08` et `CODE-T08`. Avec `--a-blanc`, rien n'est écrit et l'entropie tirée n'est pas affichée.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ICI = Path("brouillons/t08-texte-complet-fable-v1")
B4 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md")
SHA_B4 = "7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5"
TEXTES = ICI / "textes-neufs-t08-brouillon11-v1.json"
SORTIE = Path("prereg/T0.8-bases-boite-noire-v0-v1.md")
DIFF = Path("prereg/T0.8-bases-boite-noire-v0-v1-differentiel-gel-v1.md")
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
MARQUEURS = ("COMMIT_CODE_T08", "ENTROPIE_T08", "LIGNE_DEPENSE_T08", "LIGNE_MOT_LAZAR_T5_19")
EN_SECTION_GELEE = ("ENTROPIE_T08", "LIGNE_MOT_LAZAR_T5_19")


def arret(message: str):
    raise SystemExit("ARRÊT : " + message)


def sha_fichier(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def plage_gelee(lignes: list[str]) -> tuple[int, int]:
    debut = next(i for i, l in enumerate(lignes) if l.strip() == "## Hypothèse")
    fin = next(i for i, l in enumerate(lignes) if l.strip() == "## Machine, devis et dépense")
    titres = tuple(l[3:].strip() for l in lignes[debut:fin] if l.startswith("## "))
    if titres != GELEES:
        arret(f"sections gelées inattendues : {titres}")
    return debut, fin


def controler_gel(b4: str, texte: str, valeurs: dict[str, str], debut_t5_19: str) -> dict:
    l4, l = b4.split("\n"), texte.split("\n")
    d4, f4 = plage_gelee(l4)
    d, f = plage_gelee(l)
    gel = l[d:f]
    t5 = [i for i, x in enumerate(gel) if x.startswith(debut_t5_19)]
    if len(t5) != 1:
        arret(f"ligne T5-19 : {len(t5)} occurrence(s) dans les sections gelées")
    ligne_t5 = gel[t5[0]]
    ramene = "\n".join(gel[:t5[0]] + gel[t5[0] + 1:])
    for nom, valeur in valeurs.items():
        if nom == "LIGNE_MOT_LAZAR_T5_19":      # sa valeur vit dans la ligne T5-19, retirée
            if ligne_t5.count(valeur) != 1:
                arret("valeur de LIGNE_MOT_LAZAR_T5_19 absente de la ligne T5-19")
            continue
        if ramene.count(valeur) != 1:
            arret(f"valeur du marqueur {nom} : {ramene.count(valeur)} occurrence(s) dans les sections gelées, une attendue")
        ramene = ramene.replace(valeur, f"`<<{nom}>>`")
    if ramene != "\n".join(l4[d4:f4]):
        arret("SECTIONS GELÉES ≠ brouillon 4 hors la ligne T5-19 et les valeurs de marqueurs : écart, nœud de Lazar ; rien n'est écrit")
    return {"plage_b4": (d4 + 1, f4), "plage_texte": (d + 1, f), "ligne_t5_19": ligne_t5,
            "sha_plage_b4": hashlib.sha256("\n".join(l4[d4:f4]).encode()).hexdigest(),
            "sha_plage_texte": hashlib.sha256("\n".join(gel).encode()).hexdigest()}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--entree", required=True)
    p.add_argument("--commit-code", required=True)
    p.add_argument("--empreintes-code", required=True)
    p.add_argument("--contre-lecture-code", required=True)
    p.add_argument("--ligne-gardes", required=True)
    p.add_argument("--ligne-depense", required=True)
    p.add_argument("--entropie", type=int)
    p.add_argument("--a-blanc", action="store_true")
    a = p.parse_args()

    if not re.fullmatch(r"[0-9a-f]{40}", a.commit_code):
        arret("--commit-code : 40 caractères hexadécimaux attendus")
    if not re.fullmatch(r"R-\d{3,5}", a.ligne_gardes):
        arret("--ligne-gardes : une clé du registre des décisions, de la forme R-1234")
    if "T0.8" not in a.ligne_depense:
        arret("--ligne-depense : la ligne d'engagement cite T0.8 (le code de la course l'exige)")
    for chemin in (a.empreintes_code, a.contre_lecture_code):
        if not Path(chemin).is_file() or not Path(chemin + ".sha256").is_file():
            arret(f"{chemin} : fichier ou compagnon .sha256 absent (R6)")
        if Path(chemin + ".sha256").read_text().split()[0] != sha_fichier(Path(chemin)):
            arret(f"{chemin} : empreinte ≠ compagnon (R11)")
    if a.commit_code not in Path(a.empreintes_code).read_text(encoding="utf-8"):
        arret("la pièce des empreintes ne cite pas le commit donné")

    b4 = B4.read_text(encoding="utf-8")
    if hashlib.sha256(b4.encode()).hexdigest() != SHA_B4:
        arret("brouillon 4 : empreinte ≠ celle de la ligne GEL-T08")
    entree = Path(a.entree)
    if Path(a.entree + ".sha256").read_text().split()[0] != sha_fichier(entree):
        arret("brouillon d'entrée : empreinte ≠ compagnon (R11)")
    texte = entree.read_text(encoding="utf-8")
    neufs = json.loads(TEXTES.read_text(encoding="utf-8"))

    restants = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    if restants != sorted(f"<<{m}>>" for m in MARQUEURS):
        arret(f"marqueurs du brouillon d'entrée : {restants} ; attendus : {list(MARQUEURS)}")

    if a.entropie is not None:
        entropie = a.entropie
    else:
        import numpy
        entropie = int(numpy.random.SeedSequence().entropy)
    if entropie <= 0:
        arret("entropie non positive")

    valeurs = {
        "COMMIT_CODE_T08": (f"`{a.commit_code}` (pièce de ses empreintes `{a.empreintes_code}`, "
                            f"`{sha_fichier(Path(a.empreintes_code))}` ; contre-lecture de l'alignement "
                            f"`{a.contre_lecture_code}`, `{sha_fichier(Path(a.contre_lecture_code))}`)"),
        "ENTROPIE_T08": f"`{entropie}`",
        "LIGNE_DEPENSE_T08": f"ligne inscrite au scellement : {a.ligne_depense}",
        "LIGNE_MOT_LAZAR_T5_19": (f"R-2657 (mot de Lazar inscrit le 14 novembre) et {a.ligne_gardes} (gardes de code plus "
                                  "strictes confirmées ; sort de VT5-07)"),
    }
    for nom, valeur in valeurs.items():
        jeton = f"`<<{nom}>>`"
        if texte.count(jeton) != 1:
            arret(f"marqueur {nom} : {texte.count(jeton)} occurrence(s) du jeton entre accents graves, une seule attendue")
        texte = texte.replace(jeton, valeur)
    if re.search(r"<<[A-Z0-9_]+>>", texte):
        arret("un marqueur reste après remplissage")
    if "**non scellé** ; il ne vaut pas préenregistrement (R1)" not in texte:
        arret("phrase de statut « non scellé » introuvable : le statut du texte à sceller doit être revu à la main")
    texte = texte.replace("**non scellé** ; il ne vaut pas préenregistrement (R1)",
                          "**texte à sceller** : les quatre derniers marqueurs sont remplis par programme ; il vaut "
                          "préenregistrement à l'inscription de la ligne `SCELLEMENT-T08` (R1)")

    toutes = dict(neufs["valeurs_marqueurs_en_sections_gelees"])
    toutes.update({m: valeurs[m] for m in EN_SECTION_GELEE})
    gel = controler_gel(b4, texte, toutes, neufs["debut_ligne_t5_19"])

    if not a.a_blanc:
        for chemin in (SORTIE, DIFF):
            if chemin.exists():
                arret(f"{chemin} existe : on n'écrase jamais (R12)")
    diff = [
        "# Différentiel du texte de T0.8 à sceller contre le brouillon 4 gelé (ligne GEL-T08) — v1", "",
        "Produit par `brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v1.py` ; exigé par la règle « Gel vérifiable » du texte.", "",
        f"- Brouillon 4 gelé : `{B4}`, `{SHA_B4}` ; plage gelée, lignes {gel['plage_b4'][0]} à {gel['plage_b4'][1]}, `{gel['sha_plage_b4']}`.",
        f"- Texte à sceller : `{SORTIE}`, `{hashlib.sha256(texte.encode()).hexdigest()}` ; plage gelée, lignes {gel['plage_texte'][0]} à {gel['plage_texte'][1]}, `{gel['sha_plage_texte']}`.",
        f"- Brouillon d'entrée : `{entree}`, `{sha_fichier(entree)}`.", "",
        "**Contrôle par programme, tenu** : la plage gelée du texte à sceller, une fois retirée la ligne T5-19 du point 1 du plan "
        "et remis le nom de chaque marqueur à la place de sa valeur, est égale à l'octet à la plage du brouillon 4.", "",
        "## Ligne T5-19 (ajoutée au brouillon 5, gardée par le mot de Lazar)", "", "> " + gel["ligne_t5_19"], "",
        "## Valeurs des marqueurs dans les sections gelées", ""]
    for nom, valeur in toutes.items():
        diff += [f"- `{nom}` : {valeur}", ""]
    diff += ["## Valeurs des marqueurs hors des sections gelées", ""]
    for nom in ("COMMIT_CODE_T08", "LIGNE_DEPENSE_T08"):
        diff += [f"- `{nom}` : {valeurs[nom]}", ""]

    if a.a_blanc:
        print("à blanc : contrôle du gel tenu ; quatre marqueurs remplissables ; rien n'est écrit")
        return 0
    SORTIE.write_text(texte, encoding="utf-8")
    DIFF.write_text("\n".join(diff), encoding="utf-8")
    sys.path.insert(0, "src")
    from controle_ia.prereg import problemes
    restes = problemes(SORTIE)
    if restes:
        SORTIE.unlink()
        DIFF.unlink()
        arret("validateur : " + " ; ".join(restes) + " ; fichiers retirés")
    print(f"écrit : {SORTIE} {hashlib.sha256(texte.encode()).hexdigest()}")
    print(f"écrit : {DIFF}")
    print(f"entropie racine tirée (à consigner au registre des décisions) : {entropie}")
    print("suite, à la main : sceller les deux fichiers (controle_ia.prereg.sceller_prereg pour le texte) ; inscrire "
          "SCELLEMENT-T08, puis CODE-T08 ; passage à blanc sur le registre réel ; alors seulement la création de l'instance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
