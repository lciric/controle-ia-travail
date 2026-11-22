#!/usr/bin/env python3
"""Écrit le brouillon 12 (candidat 3, texte complet) de T0.8 à partir du brouillon 11, par opérations déclarées.

Usage (depuis la racine du dépôt) :
    python3 brouillons/t08-texte-complet-fable-v1/faire-t08-brouillon12-v1.py [--verifier]

Entrées lues, et seulement elles : les brouillons 4, 10 et 11 (empreintes épinglées), le fichier des textes neufs du
brouillon 12, le rapport de la contre-lecture 8 et les deux errata de N-076 (empreintes citées par le texte neuf, vérifiées
ici), et, pour l'histoire de la phrase T5-19, les brouillons 5 à 9. Aucun fichier de données, de diagnostic ni de run.

Application des opérations : la fonction `appliquer` du programme du brouillon 11, inchangé et scellé, chargée par son
chemin. Contrôle du gel : `controle_gel_t08_v1.py` (constat B-1 de la contre-lecture 8 : la phrase T5-19 est épinglée à
l'octet et à sa place contre le brouillon 10).
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ICI = Path("brouillons/t08-texte-complet-fable-v1")
sys.path.insert(0, str(ICI))
import controle_gel_t08_v1 as gel  # noqa: E402

B11 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon11.md")
B12 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon12.md")
SHA_B11 = "4342b1a5e1aae3d5595ccac86fc8488a5c3e97b7c57c8355d7cb38db8df33456"
TEXTES = ICI / "textes-neufs-t08-brouillon12-v1.json"
COUPLES = ICI / "couples-t08-brouillon12-v1.json"
DIFF = ICI / "differentiel-gel-t08-brouillon12-v1.md"
PROGRAMME_11 = ICI / "faire-t08-brouillon11-v1.py"
SHA_PROGRAMME_11 = "d33c2ea7d962a3099704d454a0ee8162e0fe1d980e0021a6de4eb3c985c54d8b"
EMPREINTES_CITEES = {
    "prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon11-cl8-v1.md": "c3e6b0ee1e7d1d1305d94fb6e7f492cfdc3432dcd49af83043b0d45a3e03e0d9",
    "docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md": "49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78",
    "docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-1.md": "34a59c49436d5239ccf2e8c4df5945a50e54665bae96bf1e32c524a643916484",
    "docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-2.md": "c2943188b4906993a1092f0bd5dd9faa5d87162d4ce1ff58e0dab2cff923ada7",
}


def arret(message: str):
    raise SystemExit("ARRÊT : " + message)


def charger_programme_11():
    if gel.sha(PROGRAMME_11.read_bytes()) != SHA_PROGRAMME_11:
        arret("programme du brouillon 11 : empreinte ≠ celle de son compagnon scellé")
    spec = importlib.util.spec_from_file_location("faire_b11", PROGRAMME_11)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def differentiel(b12: str, couples: list[dict], info: dict, section_de) -> str:
    import difflib
    l4 = gel.lire_epingle(gel.B4, gel.SHA_B4).split("\n")
    l12 = b12.split("\n")
    (d4, f4), (d12, f12) = gel.plage_gelee(l4), gel.plage_gelee(l12)
    s = ["# Différentiel du brouillon 12 de T0.8 contre le brouillon 4 gelé (ligne GEL-T08) — v1", "",
         "Produit par `brouillons/t08-texte-complet-fable-v1/faire-t08-brouillon12-v1.py` ; aucune ligne n'est écrite à la main.", "",
         f"- Brouillon 4 gelé : `{gel.B4}`, `{gel.SHA_B4}`.",
         f"- Brouillon 10 (candidat du compte 4) : `{gel.B10}`, `{gel.SHA_B10}`.",
         f"- Brouillon 11 : `{B11}`, `{SHA_B11}`.",
         f"- Brouillon 12 : `{B12}`, `{gel.sha(b12.encode('utf-8'))}`.", "",
         "## 1. Sections « Hypothèse » à « Liste d'arrêt »", "",
         f"Brouillon 4 : lignes {d4 + 1} à {f4} ({f4 - d4} lignes), empreinte de la plage `{info['sha_plage_b4']}`. Brouillon 10 : "
         f"empreinte de la plage `{info['sha_plage_b10']}`. Brouillon 12 : lignes {d12 + 1} à {f12} ({f12 - d12} lignes), empreinte "
         f"de la plage `{info['sha_plage_texte']}`.", "",
         "**Contrôle par programme, tenu** (`controle_gel_t08_v1.py`) : (a) la plage du brouillon 10, une fois retirée la phrase "
         "T5-19, est égale à l'octet à celle du brouillon 4 ; (b) la plage du brouillon 12, une fois remis le nom de chaque marqueur "
         "à la place de sa valeur, est égale à l'octet à celle du brouillon 10. La phrase T5-19 est donc celle du brouillon 10, dans "
         f"son texte et à sa place (rang {info['rang_t5_19']} de la plage).", "", "Différences avec le brouillon 4, toutes :", ""]
    sm = difflib.SequenceMatcher(None, l4[d4:f4], l12[d12:f12], autojunk=False)
    k = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        k += 1
        s += [f"### Différence {k} — {section_de(l12, d12 + j1)} (brouillon 4, l. {d4 + i1 + 1}-{d4 + i2} ; brouillon 12, l. {d12 + j1 + 1}-{d12 + j2})", ""]
        if tag == "insert":
            s += ["Ligne ajoutée (phrase T5-19, brouillon 5 ; gardée par le mot de Lazar, R-2657) :", ""]
            s += ["> " + x for x in l12[d12 + j1:d12 + j2]]
        else:
            for a, b in zip(l4[d4 + i1:d4 + i2], l12[d12 + j1:d12 + j2]):
                reste = b
                for nom, valeur in info["marqueurs_remis"].items():
                    if f"`<<{nom}>>`" in a and valeur in b:
                        s.append(f"- marqueur `{nom}` rempli : au brouillon 4, le nom du marqueur entre chevrons ; au brouillon 12 : « {valeur} »")
                        reste = reste.replace(valeur, f"`<<{nom}>>`")
                s.append("- hors de ces valeurs, la ligne est égale à l'octet à celle du brouillon 4" if reste == a
                         else "- ÉCART : la ligne diffère aussi hors des valeurs de marqueurs")
        s.append("")
    s += ["## 2. La phrase T5-19 d'un brouillon à l'autre", "",
          f"Empreinte épinglée de la ligne (brouillon 10) : `{gel.SHA_T5_19}`. « Fond » : la phrase avant sa parenthèse de statut.", "",
          "| brouillon | empreinte de la ligne | empreinte du fond |", "|---|---|---|"]
    for h in gel.histoire_t5_19():
        s.append(f"| {h['brouillon']} | `{h.get('sha_ligne', '—')}` | `{h.get('sha_fond', '—')}` |")
    s += ["", "Lecture : le fond change une fois, du brouillon 5 au brouillon 6 (couple VT5C-04 du vérificateur du brouillon 5, "
          "appliqué le 14 novembre à 03:57 UTC, avant le mot de Lazar de 06:26 UTC) ; il est égal à l'octet du brouillon 6 au "
          "brouillon 12. La ligne entière ne change plus à partir du brouillon 8, qui y écrit le mot de Lazar.", "",
          "## 3. Hors des sections gelées : opérations du brouillon 11 au brouillon 12", "",
          "| id | nature | section | motif |", "|---|---|---|---|"]
    for c in couples:
        s.append(f"| {c['id']} | {c['nature']} | {c['section']} | {c['motif']} |")
    touchees = [c for c in couples if c["section"] in gel.GELEES]
    s += ["", "Texte ancien et texte nouveau de chaque opération : `brouillons/t08-texte-complet-fable-v1/couples-t08-brouillon12-v1.json`. "
          "Opérations du brouillon 10 au brouillon 11 : `differentiel-gel-t08-brouillon11-v1.md`, section 3.", "",
          "## 4. Opérations du brouillon 12 qui touchent une section gelée", "",
          f"{len(touchees)} opération(s)." + ("" if not touchees else " " + " ; ".join(f"{c['id']} ({c['section']})" for c in touchees)), ""]
    return "\n".join(s)


def main() -> int:
    verifier = "--verifier" in sys.argv[1:]
    b11 = gel.lire_epingle(B11, SHA_B11)
    for chemin, attendu in EMPREINTES_CITEES.items():
        gel.lire_epingle(Path(chemin), attendu)
    p11 = charger_programme_11()
    neufs = json.loads(TEXTES.read_text(encoding="utf-8"))
    if neufs["sha_ligne_t5_19_brouillon10"] != gel.SHA_T5_19 or neufs["debut_ligne_t5_19"] != gel.DEBUT_T5_19:
        arret("phrase T5-19 : épingles du fichier des textes neufs ≠ celles du contrôle du gel")
    b12, couples = p11.appliquer(b11, neufs["operations"])
    restants = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", b12)))
    attendus = sorted(f"<<{m}>>" for m in neufs["marqueurs_restants"])
    if restants != attendus:
        arret(f"marqueurs restants {restants} ≠ {attendus}")
    for m in attendus:
        if b12.count(m) != 1:
            arret(f"marqueur {m} : {b12.count(m)} occurrences, une seule attendue")
    if "À REMPLIR" in b12:
        arret("« À REMPLIR » présent : le validateur le refuserait")
    info = gel.controler_gel(b12, neufs["valeurs_marqueurs_en_sections_gelees"])
    touchees = [c["id"] for c in couples if c["section"] in gel.GELEES]
    if touchees:
        arret(f"opérations dans une section gelée : {touchees} ; le brouillon 12 n'en a aucune")
    diff = differentiel(b12, couples, info, p11.section_de)
    doc = {"brouillon_de_depart": {"chemin": str(B11), "sha256": SHA_B11},
           "brouillon_gele": {"chemin": str(gel.B4), "sha256": gel.SHA_B4},
           "brouillon_ecrit": {"chemin": str(B12), "sha256": gel.sha(b12.encode("utf-8"))},
           "textes_neufs": {"chemin": str(TEXTES), "sha256": gel.sha(TEXTES.read_bytes())},
           "controle_gel": {k: v for k, v in info.items() if k != "ligne_t5_19_b10"},
           "marqueurs_restants": neufs["marqueurs_restants"], "couples": couples}
    if verifier:
        if B12.read_text(encoding="utf-8") != b12:
            arret("le brouillon 12 sur disque ≠ celui que le programme reproduit")
        print(f"brouillon 12 reproduit à l'octet : {gel.sha(b12.encode('utf-8'))} ; {len(couples)} opérations ; gel tenu")
        return 0
    if B12.exists() and B12.read_text(encoding="utf-8") != b12:
        arret(f"{B12} existe et diffère : on n'écrase jamais (R12)")
    B12.write_text(b12, encoding="utf-8")
    COUPLES.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    DIFF.write_text(diff, encoding="utf-8")
    print(f"écrit : {B12} {gel.sha(b12.encode('utf-8'))} ; {len(couples)} opérations ; marqueurs restants : {neufs['marqueurs_restants']}")
    print(f"gel tenu : plage du brouillon 4 {info['sha_plage_b4'][:16]}… ; phrase T5-19 épinglée au rang {info['rang_t5_19']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
