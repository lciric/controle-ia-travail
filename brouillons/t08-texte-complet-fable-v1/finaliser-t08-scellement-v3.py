#!/usr/bin/env python3
"""Remplit les cinq marqueurs restants du texte de T0.8 et écrit le texte à sceller, avec son différentiel contre le gel.

Version 3 : comme la version 2, sauf la valeur du marqueur `LIGNE_MOT_LAZAR_T5_19`, qui cite la décision de Lazar du
22 novembre sur la garde d'antériorité (GO-2026-11-22-122, option (a)) ; le reste est inchangé.
Version 2 : corrige la version 1 selon la contre-lecture 8 (B-1 : la phrase T5-19 est épinglée à l'octet et à sa place ;
M-8 : le brouillon d'entrée est épinglé à l'empreinte que la vérification déclare conforme ; m-2 : aucun tirage d'entropie
avant le contrôle « n'écrase jamais », aucun tirage à blanc) et un défaut trouvé en l'écrivant (la version 1 aurait changé
la phrase « non scellé » jusque dans l'annexe recopiée à l'octet).

À jouer par la session mère, au scellement, depuis la racine du dépôt :

    PYTHONPATH=src python3 brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v3.py \
        --entree brouillons/T0.8-bases-boite-noire-v0-v1-brouillon13.md --sha-entree <empreinte du brouillon vérifié> \
        --rapport-verification <chemin du rapport de vérification des corrections> \
        --commit-code <40 caractères> --empreintes-code <pièce des empreintes du code aligné> \
        --contre-lecture-code <rapport de contre-lecture de l'alignement> \
        --ligne-gardes R-XXXX --ligne-depense "<date> : engagement, T0.8, GO-2026-11-10-12, GO-2026-11-22-79, GO-2026-11-22-93" \
        [--entropie <entier déjà tiré et consigné>] [--a-blanc] [--dossier-sortie prereg]

Ordre : (1) contrôle des arguments et des compagnons ; (2) le brouillon d'entrée a l'empreinte donnée, égale à son
compagnon ; (3) les sorties n'existent pas (R12) ; (4) tirage de l'entropie racine, une fois, sans lecture de données
(à blanc : aucune entropie n'est tirée, une valeur fictive déclarée sert au contrôle) ; (5) remplissage, chaque marqueur
présent une seule fois ; (6) contrôle du gel (`controle_gel_t08_v1.py`) ; (7) validateur `controle_ia.prereg.problemes`
sur une copie temporaire ; (8) écriture du texte et du différentiel. Il ne scelle pas et n'écrit dans aucun registre.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import controle_gel_t08_v1 as gel  # noqa: E402

TEXTES = ICI / "textes-neufs-t08-brouillon12-v1.json"
NOM_SORTIE = "T0.8-bases-boite-noire-v0-v1.md"
NOM_DIFF = "T0.8-bases-boite-noire-v0-v1-differentiel-gel-v1.md"
MARQUEURS = ("COMMIT_CODE_T08", "ENTROPIE_T08", "LIGNE_DEPENSE_T08", "LIGNE_MOT_LAZAR_T5_19", "VERIFICATION_CL8_T08")
EN_SECTION_GELEE = ("ENTROPIE_T08", "LIGNE_MOT_LAZAR_T5_19")
ENTROPIE_FICTIVE = 1          # à blanc seulement : jamais écrite, jamais une graine
NON_SCELLE = "**non scellé** ; il ne vaut pas préenregistrement (R1)"
A_SCELLER = ("**texte à sceller** : les cinq derniers marqueurs sont remplis par programme ; il vaut préenregistrement à "
             "l'inscription de la ligne `SCELLEMENT-T08` (R1)")


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


def main() -> int:
    p = argparse.ArgumentParser()
    for nom in ("--entree", "--sha-entree", "--rapport-verification", "--commit-code", "--empreintes-code",
                "--contre-lecture-code", "--ligne-gardes", "--ligne-depense"):
        p.add_argument(nom, required=True)
    p.add_argument("--entropie", type=int)
    p.add_argument("--a-blanc", action="store_true")
    p.add_argument("--dossier-sortie", default="prereg")
    a = p.parse_args()

    # (1) arguments et compagnons
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit_code):
        arret("--commit-code : 40 caractères hexadécimaux attendus")
    if not re.fullmatch(r"[0-9a-f]{64}", a.sha_entree):
        arret("--sha-entree : 64 caractères hexadécimaux attendus")
    if not re.fullmatch(r"R-\d{3,5}", a.ligne_gardes):
        arret("--ligne-gardes : une clé du registre des décisions, de la forme R-1234")
    if "T0.8" not in a.ligne_depense:
        arret("--ligne-depense : la ligne d'engagement cite T0.8 (le code de la course l'exige)")
    if a.entropie is not None and a.entropie <= 0:
        arret("--entropie : entier positif attendu")
    sha_empreintes = compagnon_conforme(Path(a.empreintes_code))
    sha_cl_code = compagnon_conforme(Path(a.contre_lecture_code))
    sha_verification = compagnon_conforme(Path(a.rapport_verification))
    if a.commit_code not in Path(a.empreintes_code).read_text(encoding="utf-8"):
        arret("la pièce des empreintes ne cite pas le commit donné")
    if a.sha_entree not in Path(a.rapport_verification).read_text(encoding="utf-8"):
        arret("le rapport de vérification ne cite pas l'empreinte du brouillon d'entrée : ce n'est pas le brouillon vérifié (R2)")

    # (2) brouillon d'entrée épinglé (M-8)
    entree = Path(a.entree)
    if compagnon_conforme(entree) != a.sha_entree:
        arret("brouillon d'entrée : empreinte ≠ --sha-entree ; seul le brouillon déclaré conforme par la vérification se scelle (R2)")
    texte = entree.read_text(encoding="utf-8")
    neufs = json.loads(TEXTES.read_text(encoding="utf-8"))
    restants = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    if restants != sorted(f"<<{m}>>" for m in MARQUEURS):
        arret(f"marqueurs du brouillon d'entrée : {restants} ; attendus : {list(MARQUEURS)}")

    # (3) sorties absentes, avant tout tirage (m-2)
    sortie, diff_chemin = Path(a.dossier_sortie) / NOM_SORTIE, Path(a.dossier_sortie) / NOM_DIFF
    if not a.a_blanc:
        for chemin in (sortie, diff_chemin):
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

    if a.a_blanc:
        print("à blanc : arguments, brouillon épinglé, cinq marqueurs, contrôle du gel et validateur tenus ; aucune entropie "
              "tirée ; rien n'est écrit")
        return 0

    # (8) écriture
    d = ["# Différentiel du texte de T0.8 à sceller contre le brouillon 4 gelé (ligne GEL-T08) — v1", "",
         "Produit par `brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v3.py` ; exigé par la règle « Gel vérifiable » du texte.", "",
         f"- Brouillon 4 gelé : `{gel.B4}`, `{gel.SHA_B4}` ; plage gelée, lignes {info['plage_b4'][0]} à {info['plage_b4'][1]}, `{info['sha_plage_b4']}`.",
         f"- Brouillon 10 : `{gel.B10}`, `{gel.SHA_B10}` ; plage gelée `{info['sha_plage_b10']}`.",
         f"- Brouillon d'entrée, déclaré conforme par la vérification : `{entree}`, `{a.sha_entree}` ; rapport de vérification `{a.rapport_verification}`, `{sha_verification}`.",
         f"- Texte à sceller : `{sortie}`, `{gel.sha(texte.encode('utf-8'))}` ; plage gelée, lignes {info['plage_texte'][0]} à {info['plage_texte'][1]}, `{info['sha_plage_texte']}`.", "",
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
    print(f"écrit : {sortie} {gel.sha(texte.encode('utf-8'))}")
    print(f"écrit : {diff_chemin}")
    print(f"entropie racine tirée (à consigner au registre des décisions) : {entropie}")
    print("suite, à la main : sceller les deux fichiers (controle_ia.prereg.sceller_prereg pour le texte) ; inscrire "
          "SCELLEMENT-T08, puis CODE-T08 ; passage à blanc sur le registre réel ; alors seulement la création de l'instance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
