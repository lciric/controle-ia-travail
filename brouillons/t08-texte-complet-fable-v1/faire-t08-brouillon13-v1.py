#!/usr/bin/env python3
"""Écrit le brouillon 13 (candidat 4, texte complet) de T0.8 à partir du brouillon 12, par opérations déclarées.

Usage (depuis la racine du dépôt) :
    python3 brouillons/t08-texte-complet-fable-v1/faire-t08-brouillon13-v1.py [--verifier]

Même construction que le programme du brouillon 12, écrite pour un numéro de brouillon donné (constantes `N` et
`SHA_DEPART`) : application des opérations par la fonction `appliquer` du programme du brouillon 11, inchangé et scellé ;
contrôle du gel par `controle_gel_t08_v1.py` (phrase T5-19 épinglée à l'octet et à sa place contre le brouillon 10) ;
aucune opération dans une section gelée. Entrées lues : les brouillons 4, 10 et N − 1 (empreintes épinglées), le fichier
des textes neufs du brouillon N, et, pour l'histoire de la phrase T5-19, les brouillons 5 à 12. Aucun fichier de données,
de diagnostic ni de run.
"""
from __future__ import annotations

import difflib
import importlib.util
import json
import re
import sys
from pathlib import Path

N = 13
SHA_DEPART = "e55a33ce78ab6b7b97b6b9a53b84c054898ca9823ee30ca64df573394aca8d73"   # brouillon 12

ICI = Path("brouillons/t08-texte-complet-fable-v1")
sys.path.insert(0, str(ICI))
import controle_gel_t08_v1 as gel  # noqa: E402

DEPART = Path(f"brouillons/T0.8-bases-boite-noire-v0-v1-brouillon{N - 1}.md")
ECRIT = Path(f"brouillons/T0.8-bases-boite-noire-v0-v1-brouillon{N}.md")
TEXTES = ICI / f"textes-neufs-t08-brouillon{N}-v1.json"
COUPLES = ICI / f"couples-t08-brouillon{N}-v1.json"
DIFF = ICI / f"differentiel-gel-t08-brouillon{N}-v1.md"
PROGRAMME_11 = ICI / "faire-t08-brouillon11-v1.py"
SHA_PROGRAMME_11 = "d33c2ea7d962a3099704d454a0ee8162e0fe1d980e0021a6de4eb3c985c54d8b"


def arret(message: str):
    raise SystemExit("ARRÊT : " + message)


def charger_programme_11():
    if gel.sha(PROGRAMME_11.read_bytes()) != SHA_PROGRAMME_11:
        arret("programme du brouillon 11 : empreinte ≠ celle de son compagnon scellé")
    spec = importlib.util.spec_from_file_location("faire_b11", PROGRAMME_11)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def differentiel(ecrit: str, couples: list[dict], info: dict, section_de) -> str:
    l4 = gel.lire_epingle(gel.B4, gel.SHA_B4).split("\n")
    l = ecrit.split("\n")
    (d4, f4), (d, f) = gel.plage_gelee(l4), gel.plage_gelee(l)
    s = [f"# Différentiel du brouillon {N} de T0.8 contre le brouillon 4 gelé (ligne GEL-T08) — v1", "",
         f"Produit par `{ICI}/faire-t08-brouillon{N}-v1.py` ; aucune ligne n'est écrite à la main.", "",
         f"- Brouillon 4 gelé : `{gel.B4}`, `{gel.SHA_B4}`.",
         f"- Brouillon 10 (candidat du compte 4) : `{gel.B10}`, `{gel.SHA_B10}`.",
         f"- Brouillon {N - 1} (départ) : `{DEPART}`, `{SHA_DEPART}`.",
         f"- Brouillon {N} : `{ECRIT}`, `{gel.sha(ecrit.encode('utf-8'))}`.", "",
         "## 1. Sections « Hypothèse » à « Liste d'arrêt »", "",
         f"Brouillon 4 : lignes {d4 + 1} à {f4} ({f4 - d4} lignes), empreinte de la plage `{info['sha_plage_b4']}`. Brouillon 10 : "
         f"empreinte de la plage `{info['sha_plage_b10']}`. Brouillon {N} : lignes {d + 1} à {f} ({f - d} lignes), empreinte de la "
         f"plage `{info['sha_plage_texte']}`.", "",
         "**Contrôle par programme, tenu** (`controle_gel_t08_v1.py`) : (a) la plage du brouillon 10, une fois retirée la phrase "
         f"T5-19, est égale à l'octet à celle du brouillon 4 ; (b) la plage du brouillon {N}, une fois remis le nom de chaque "
         "marqueur à la place de sa valeur, est égale à l'octet à celle du brouillon 10. La phrase T5-19 est donc celle du "
         f"brouillon 10, dans son texte et à sa place (rang {info['rang_t5_19']} de la plage).", "",
         "Différences avec le brouillon 4, toutes :", ""]
    k = 0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, l4[d4:f4], l[d:f], autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        k += 1
        s += [f"### Différence {k} — {section_de(l, d + j1)} (brouillon 4, l. {d4 + i1 + 1}-{d4 + i2} ; brouillon {N}, l. {d + j1 + 1}-{d + j2})", ""]
        if tag == "insert":
            s += ["Ligne ajoutée (phrase T5-19, brouillon 5 ; gardée par le mot de Lazar, R-2657) :", ""]
            s += ["> " + x for x in l[d + j1:d + j2]]
        else:
            for a, b in zip(l4[d4 + i1:d4 + i2], l[d + j1:d + j2]):
                reste = b
                for nom, valeur in info["marqueurs_remis"].items():
                    if f"`<<{nom}>>`" in a and valeur in b:
                        s.append(f"- marqueur `{nom}` rempli : au brouillon 4, le nom du marqueur entre chevrons ; au brouillon {N} : « {valeur} »")
                        reste = reste.replace(valeur, f"`<<{nom}>>`")
                s.append("- hors de ces valeurs, la ligne est égale à l'octet à celle du brouillon 4" if reste == a
                         else "- ÉCART : la ligne diffère aussi hors des valeurs de marqueurs")
        s.append("")
    s += ["## 2. La phrase T5-19 d'un brouillon à l'autre", "",
          f"Empreinte épinglée de la ligne (brouillon 10) : `{gel.SHA_T5_19}`. Table des brouillons 5 à 12 : "
          "`differentiel-gel-t08-brouillon12-v1.md`, section 2 ; la ligne du brouillon " + str(N) + " est celle du brouillon 10 "
          "(contrôle (b) ci-dessus).", "",
          f"## 3. Hors des sections gelées : opérations du brouillon {N - 1} au brouillon {N}", "",
          "| id | nature | section | motif |", "|---|---|---|---|"]
    for c in couples:
        s.append(f"| {c['id']} | {c['nature']} | {c['section']} | {c['motif']} |")
    s += ["", f"Texte ancien et texte nouveau de chaque opération : `{COUPLES}`. Opérations antérieures : différentiels des "
          "brouillons 11 et 12, même dossier, sections 3.", "",
          f"## 4. Opérations du brouillon {N} qui touchent une section gelée", "", "Aucune (contrôlé par le programme).", ""]
    return "\n".join(s)


def main() -> int:
    verifier = "--verifier" in sys.argv[1:]
    depart = gel.lire_epingle(DEPART, SHA_DEPART)
    p11 = charger_programme_11()
    neufs = json.loads(TEXTES.read_text(encoding="utf-8"))
    if neufs["sha_ligne_t5_19_brouillon10"] != gel.SHA_T5_19 or neufs["debut_ligne_t5_19"] != gel.DEBUT_T5_19:
        arret("phrase T5-19 : épingles du fichier des textes neufs ≠ celles du contrôle du gel")
    ecrit, couples = p11.appliquer(depart, neufs["operations"])
    restants = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", ecrit)))
    attendus = sorted(f"<<{m}>>" for m in neufs["marqueurs_restants"])
    if restants != attendus:
        arret(f"marqueurs restants {restants} ≠ {attendus}")
    for m in attendus:
        if ecrit.count(m) != 1:
            arret(f"marqueur {m} : {ecrit.count(m)} occurrences, une seule attendue")
    if "À REMPLIR" in ecrit:
        arret("« À REMPLIR » présent : le validateur le refuserait")
    info = gel.controler_gel(ecrit, neufs["valeurs_marqueurs_en_sections_gelees"])
    touchees = [c["id"] for c in couples if c["section"] in gel.GELEES]
    if touchees:
        arret(f"opérations dans une section gelée : {touchees} ; ce brouillon n'en a aucune")
    doc = {"brouillon_de_depart": {"chemin": str(DEPART), "sha256": SHA_DEPART},
           "brouillon_gele": {"chemin": str(gel.B4), "sha256": gel.SHA_B4},
           "brouillon_ecrit": {"chemin": str(ECRIT), "sha256": gel.sha(ecrit.encode("utf-8"))},
           "textes_neufs": {"chemin": str(TEXTES), "sha256": gel.sha(TEXTES.read_bytes())},
           "controle_gel": {k: v for k, v in info.items() if k != "ligne_t5_19_b10"},
           "marqueurs_restants": neufs["marqueurs_restants"], "couples": couples}
    if verifier:
        if ECRIT.read_text(encoding="utf-8") != ecrit:
            arret(f"le brouillon {N} sur disque ≠ celui que le programme reproduit")
        print(f"brouillon {N} reproduit à l'octet : {gel.sha(ecrit.encode('utf-8'))} ; {len(couples)} opérations ; gel tenu")
        return 0
    if ECRIT.exists() and ECRIT.read_text(encoding="utf-8") != ecrit:
        arret(f"{ECRIT} existe et diffère : on n'écrase jamais (R12)")
    ECRIT.write_text(ecrit, encoding="utf-8")
    COUPLES.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    DIFF.write_text(differentiel(ecrit, couples, info, p11.section_de), encoding="utf-8")
    print(f"écrit : {ECRIT} {gel.sha(ecrit.encode('utf-8'))} ; {len(couples)} opérations ; marqueurs restants : {neufs['marqueurs_restants']}")
    print(f"gel tenu : plage du brouillon 4 {info['sha_plage_b4'][:16]}… ; phrase T5-19 épinglée au rang {info['rang_t5_19']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
