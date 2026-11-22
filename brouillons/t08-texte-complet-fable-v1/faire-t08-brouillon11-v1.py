#!/usr/bin/env python3
"""Écrit le brouillon 11 (candidat 2, texte complet) de T0.8 à partir du brouillon 10, par opérations déclarées.

Usage (depuis la racine du dépôt) :
    python3 brouillons/t08-texte-complet-fable-v1/faire-t08-brouillon11-v1.py [--verifier]

Entrées lues, et seulement elles : le brouillon 10 (candidat du compte 4), le brouillon 4 gelé (ligne GEL-T08), le
fichier des textes neufs (`textes-neufs-t08-brouillon11-v1.json`), et les fichiers du dépôt dont une empreinte est citée
(vérifiée ici contre la constante écrite). Aucun fichier de données, de diagnostic ni de run n'est ouvert.

Sorties : le brouillon 11, le fichier des couples (ancien, nouveau, section, nature) et le différentiel contre le gel.
Avec `--verifier`, rien n'est écrit : le brouillon 11 présent sur disque est comparé à celui que le programme reproduit.

Contrôle du gel (règle « Gel vérifiable » du texte) : dans les sections « Hypothèse » à « Liste d'arrêt », le brouillon 11
doit être égal à l'octet au brouillon 4, une fois (a) retirée la ligne T5-19 du point 1 du plan (ajoutée au brouillon 5,
gardée par le mot de Lazar) et (b) remise, à la place de chaque valeur de marqueur remplie, le nom du marqueur. Sinon arrêt.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ICI = Path("brouillons/t08-texte-complet-fable-v1")
B4 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md")
B10 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon10.md")
B11 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon11.md")
TEXTES = ICI / "textes-neufs-t08-brouillon11-v1.json"
COUPLES = ICI / "couples-t08-brouillon11-v1.json"
DIFF = ICI / "differentiel-gel-t08-brouillon11-v1.md"

SHA_B4 = "7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5"
SHA_B10 = "fb004b96bf7fd70d6fe4f1938cba8bcd1afa9a3261135b5ddea336a9e0c68ba1"

# Fichiers du dépôt dont le texte neuf cite l'empreinte : vérifiés ici (R6, R11). Aucun n'est un résultat.
EMPREINTES_CITEES = {
    "prereg/validite-adaptateur-v1.md": "7e78909d7ca88e0834d277bcf2cad78112f28b23a75d2a07c0503c765062363d",
    "registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json": "e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b",
    "scripts/mots_et_cout_t06_v3.py": "9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674",
    "scripts/lancer_mots_et_cout_t06_v3.sh": "e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5",
    "src/controle_ia/bases/sequentiel.py": "35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8",
    "brouillons/t08-code-compte4-v1/empreintes-code-t08-453a71e1-v1.md": "797ac9672963a118d246d8161c4fe6da19cbdcdf8a24c30be175c6bac85af204",
    "docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md": "49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78",
    "prereg/brouillon-G0-grille-lecture-v8.md": "0c2ea83c7dc1612649f457d99c71e047fd919021b78b16c889cb42eec6658a3e",
    "registres/qui-a-lu-quoi-v18.md": "dad59f6c0e83864940b91c7357c850e0db0bedcd0cd3b4083b98d5764e813b95",
    "prereg/T0.8-base-A-mots-et-cout-v1.md": "72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d",
}
# Lignes du registre des scellements que le texte neuf cite (clé → date, chemin, empreinte), relues ici.
LIGNES_REGISTRE = {
    "GEL-T08": ("2026-11-10T14:57:57Z", "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md", SHA_B4),
    "RUN-CONFIRMATION-T06": ("2026-11-13T18:52:43Z", "runs/20261111-151701-t06-reel/manifeste.json",
                             "7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6"),
    "CODE-MOTS-ET-COUT-T06": ("2026-11-14T14:55:41Z", "registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json",
                              "e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b"),
    "LECTURE-T08-BASE-A": ("2026-11-16T21:01:43Z", "diag/20261116-205721-mots-et-cout-t06/base-a-t08.json",
                           "a2113f9a5c5f92fdb50e6b5390304e57c8fe51e59c99aa36f7e5cf99fb5e7d35"),
    "ISSUE-MOTS-ET-COUT-T06": ("2026-11-16T21:02:42Z", "diag/20261116-205721-mots-et-cout-t06/issue-mots-et-cout-t06.json",
                               "1b84d7c4440638699ac14711365fb865c1f5c57b50c39f44259a61b2aca53657"),
}
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
SECTION_APRES_GEL = "Machine, devis et dépense"


class Arret(SystemExit):
    pass


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire(chemin: Path, attendu: str | None = None) -> str:
    octets = chemin.read_bytes()
    if attendu is not None and sha(octets) != attendu:
        raise Arret(f"{chemin} : empreinte {sha(octets)} ≠ {attendu} attendue : arrêt (R11)")
    return octets.decode("utf-8")


def section_de(lignes: list[str], i: int) -> str:
    """Titre de niveau 2 qui gouverne la ligne i (indice à partir de 0) ; « en-tête » avant le premier."""
    for j in range(i, -1, -1):
        if lignes[j].startswith("## "):
            return lignes[j][3:].strip()
    return "en-tête"


def plage_gelee(lignes: list[str]) -> tuple[int, int]:
    debut = next(i for i, l in enumerate(lignes) if l.strip() == "## Hypothèse")
    fin = next(i for i, l in enumerate(lignes) if l.strip() == "## " + SECTION_APRES_GEL)
    titres = [l[3:].strip() for l in lignes[debut:fin] if l.startswith("## ")]
    if tuple(titres) != GELEES:
        raise Arret(f"sections gelées inattendues : {titres}")
    return debut, fin


def une_ligne(lignes: list[str], prefixe: str) -> int:
    trouvees = [i for i, l in enumerate(lignes) if l.startswith(prefixe)]
    if len(trouvees) != 1:
        raise Arret(f"préfixe {prefixe[:60]!r} : {len(trouvees)} ligne(s), une seule attendue")
    return trouvees[0]


def appliquer(texte: str, operations: list[dict]) -> tuple[str, list[dict]]:
    """Applique les opérations dans l'ordre ; rend le texte et les couples (ancien, nouveau) effectivement appliqués."""
    couples = []
    for op in operations:
        lignes = texte.split("\n")
        nature, ident = op["nature"], op["id"]
        if nature == "remplacer":            # sous-chaîne exacte, présente une seule fois
            ancien, nouveau = op["ancien"], op["nouveau"]
            if texte.count(ancien) != 1:
                raise Arret(f"{ident} : texte ancien présent {texte.count(ancien)} fois, une seule attendue")
            i = next(k for k, l in enumerate(lignes) if ancien in l)
            texte = texte.replace(ancien, nouveau)
        elif nature == "remplacer_ligne":    # ligne entière désignée par son préfixe unique
            i = une_ligne(lignes, op["prefixe"])
            ancien, nouveau = lignes[i], op["nouveau"]
            lignes[i] = nouveau
            texte = "\n".join(lignes)
        elif nature == "ajouter_en_fin_de_ligne":
            i = une_ligne(lignes, op["prefixe"])
            ancien, nouveau = lignes[i], lignes[i] + op["ajout"]
            lignes[i] = nouveau
            texte = "\n".join(lignes)
        elif nature == "ajouter_en_debut_de_valeur":   # après le préfixe exact de la ligne
            i = une_ligne(lignes, op["prefixe"])
            ancien = lignes[i]
            nouveau = op["prefixe"] + op["ajout"] + lignes[i][len(op["prefixe"]):]
            lignes[i] = nouveau
            texte = "\n".join(lignes)
        elif nature == "inserer_apres":      # bloc inséré après la ligne désignée par son préfixe unique
            i = une_ligne(lignes, op["prefixe"])
            ancien, nouveau = lignes[i], lignes[i] + "\n" + op["bloc"]
            lignes[i] = nouveau
            texte = "\n".join(lignes)
        elif nature == "inserer_avant":
            i = une_ligne(lignes, op["prefixe"])
            ancien, nouveau = lignes[i], op["bloc"] + "\n" + lignes[i]
            lignes[i] = nouveau
            texte = "\n".join(lignes)
        elif nature == "annexe_ligne_citee":  # la ligne désignée est recopiée à l'octet, citée, en fin de texte
            i = une_ligne(lignes, op["prefixe"])
            ancien = ""
            nouveau = op["titre"] + "\n\n" + op["intro"] + "\n\n> " + lignes[i]
            texte = texte.rstrip("\n") + "\n\n" + nouveau + "\n"
            i = len(texte.split("\n")) - 2
            lignes = texte.split("\n")
        else:
            raise Arret(f"{ident} : nature {nature!r} inconnue")
        couples.append({"id": ident, "nature": nature, "section": op.get("section") or section_de(lignes, i),
                        "motif": op["motif"], "ancien": ancien, "nouveau": nouveau})
    return texte, couples


def controler_gel(b4: str, b11: str, valeurs_marqueurs: dict[str, str], ligne_t5_19: str) -> dict:
    l4, l11 = b4.split("\n"), b11.split("\n")
    d4, f4 = plage_gelee(l4)
    d11, f11 = plage_gelee(l11)
    gel4 = l4[d4:f4]
    gel11 = l11[d11:f11]
    # (a) la ligne T5-19 (une seule, repérée par son début exact)
    t5 = [i for i, l in enumerate(gel11) if l.startswith(ligne_t5_19)]
    if len(t5) != 1:
        raise Arret(f"ligne T5-19 : {len(t5)} occurrence(s) dans les sections gelées, une seule attendue")
    ligne_t5 = gel11[t5[0]]
    ramene = gel11[:t5[0]] + gel11[t5[0] + 1:]
    # (b) chaque valeur de marqueur remplie redevient le nom du marqueur
    texte = "\n".join(ramene)
    remises = {}
    for nom, valeur in valeurs_marqueurs.items():
        n = texte.count(valeur)
        if n != 1:
            raise Arret(f"valeur du marqueur {nom} : {n} occurrence(s) dans les sections gelées, une seule attendue")
        texte = texte.replace(valeur, f"`<<{nom}>>`")
        remises[nom] = valeur
    if texte != "\n".join(gel4):
        a, b = "\n".join(gel4).split("\n"), texte.split("\n")
        ecarts = [(k + 1, x, y) for k, (x, y) in enumerate(zip(a, b)) if x != y]
        raise Arret(f"SECTIONS GELÉES ≠ brouillon 4 après remise des marqueurs : {len(ecarts)} ligne(s) en écart "
                    f"(première : {ecarts[0][0] if ecarts else 'longueurs différentes'}) : écart, nœud de Lazar")
    return {"lignes_gelees_b4": len(gel4), "lignes_gelees_b11": len(gel11), "ligne_t5_19": ligne_t5,
            "marqueurs_remis": remises, "sha_gel_b4": sha("\n".join(gel4).encode("utf-8")),
            "sha_gel_b11": sha("\n".join(gel11).encode("utf-8"))}


def verifier_citations() -> None:
    for chemin, attendu in EMPREINTES_CITEES.items():
        lire(Path(chemin), attendu)
    registre = lire(Path("registres/scellements-v1.md"))
    for cle, (date, chemin, empreinte) in LIGNES_REGISTRE.items():
        attendue = f"| {cle} | {date} | {chemin} | {empreinte} |"
        if registre.count(attendue) != 1:
            raise Arret(f"registre des scellements : ligne {cle} attendue une fois sous la forme citée")
    for cle in ("SCELLEMENT-T08 ", "CODE-T08 ", "COURSE-T08 ", "LECTURE-T08 ", "VERDICT-T08 "):
        if f"| {cle}|" in registre:
            raise Arret(f"registre des scellements : la clé {cle.strip()} existe déjà ; ce programme suppose qu'aucune n'existe")
    vadapt = lire(Path("registres/validite-adaptateur-v1.md"))
    cles = [l.split("|")[1].strip() for l in vadapt.split("\n") if l.startswith("| ")]
    if cles != ["SCELLEMENT-VADAPT"]:
        raise Arret(f"registre du texte de validité : clés {cles} ; le texte neuf écrit « une seule ligne, SCELLEMENT-VADAPT »")


def differentiel(b4: str, b10: str, b11: str, couples: list[dict], gel: dict) -> str:
    import difflib
    l4, l11 = b4.split("\n"), b11.split("\n")
    d4, f4 = plage_gelee(l4)
    d11, f11 = plage_gelee(l11)
    sortie = ["# Différentiel du brouillon 11 de T0.8 contre le brouillon 4 gelé (ligne GEL-T08) — v1", "",
              "Produit par `brouillons/t08-texte-complet-fable-v1/faire-t08-brouillon11-v1.py` ; aucune ligne n'est écrite à la main.", "",
              f"- Brouillon 4 gelé : `{B4}`, `{sha(b4.encode())}`.",
              f"- Brouillon 10 (candidat du compte 4) : `{B10}`, `{sha(b10.encode())}`.",
              f"- Brouillon 11 : `{B11}`, `{sha(b11.encode())}`.", "",
              "## 1. Sections « Hypothèse » à « Liste d'arrêt »", "",
              f"Brouillon 4 : lignes {d4 + 1} à {f4} ({f4 - d4} lignes), empreinte de la plage `{gel['sha_gel_b4']}`. "
              f"Brouillon 11 : lignes {d11 + 1} à {f11} ({f11 - d11} lignes), empreinte de la plage `{gel['sha_gel_b11']}`.", "",
              "**Contrôle par programme, tenu** : la plage du brouillon 11, une fois retirée la ligne T5-19 du point 1 du plan et "
              "remis le nom de chaque marqueur à la place de sa valeur, est égale à l'octet à la plage du brouillon 4.", "",
              "Différences, toutes :", ""]
    sm = difflib.SequenceMatcher(None, l4[d4:f4], l11[d11:f11], autojunk=False)
    k = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        k += 1
        sortie.append(f"### Différence {k} — {section_de(l11, d11 + j1)} (brouillon 4, l. {d4 + i1 + 1}-{d4 + i2} ; brouillon 11, l. {d11 + j1 + 1}-{d11 + j2})")
        sortie.append("")
        if tag == "insert":
            sortie.append("Ligne ajoutée (phrase T5-19, brouillon 5 ; gardée par le mot de Lazar, R-2657) :")
            sortie.append("")
            sortie.extend("> " + l for l in l11[d11 + j1:d11 + j2])
        else:
            for a, b in zip(l4[d4 + i1:d4 + i2], l11[d11 + j1:d11 + j2]):
                reste = b
                for nom, valeur in gel["marqueurs_remis"].items():
                    if f"`<<{nom}>>`" in a and valeur in b:
                        sortie.append(f"- marqueur `{nom}` rempli : au brouillon 4, le nom du marqueur entre chevrons ; au brouillon 11 : « {valeur} »")
                        reste = reste.replace(valeur, f"`<<{nom}>>`")
                sortie.append("- hors de ces valeurs, la ligne est égale à l'octet à celle du brouillon 4"
                              if reste == a else "- ÉCART : la ligne diffère aussi hors des valeurs de marqueurs")
        sortie.append("")
    sortie += ["## 2. Valeurs remises pour le contrôle", ""]
    for nom, valeur in gel["marqueurs_remis"].items():
        sortie += [f"- `{nom}` : {valeur}", ""]
    sortie += ["## 3. Hors des sections gelées : opérations du brouillon 10 au brouillon 11", "",
               "| id | nature | section | motif |", "|---|---|---|---|"]
    for c in couples:
        sortie.append(f"| {c['id']} | {c['nature']} | {c['section']} | {c['motif']} |")
    sortie += ["", "Texte ancien et texte nouveau de chaque opération : `brouillons/t08-texte-complet-fable-v1/couples-t08-brouillon11-v1.json`.", ""]
    gelees = [c for c in couples if c["section"] in GELEES]
    sortie += ["## 4. Opérations qui touchent une section gelée", ""]
    for c in gelees:
        sortie.append(f"- {c['id']} ({c['section']}) : {c['motif']}")
    sortie += ["", f"Soit {len(gelees)} opération(s), toutes des valeurs de marqueurs ; aucune autre opération n'écrit dans la plage gelée "
               "(contrôle de la section 1).", ""]
    return "\n".join(sortie)


def main() -> int:
    verifier_seulement = "--verifier" in sys.argv[1:]
    b4 = lire(B4, SHA_B4)
    b10 = lire(B10, SHA_B10)
    verifier_citations()
    neufs = json.loads(lire(TEXTES))
    b11, couples = appliquer(b10, neufs["operations"])
    restants = sorted({m for m in __import__("re").findall(r"<<[A-Z0-9_]+>>", b11)})
    attendus = sorted(f"<<{m}>>" for m in neufs["marqueurs_restants"])
    if restants != attendus:
        raise Arret(f"marqueurs restants {restants} ≠ {attendus}")
    for m in attendus:
        if b11.count(m) != 1:
            raise Arret(f"marqueur {m} : {b11.count(m)} occurrences, une seule attendue")
    if "À REMPLIR" in b11:
        raise Arret("« À REMPLIR » présent : le validateur le refuserait")
    gel = controler_gel(b4, b11, neufs["valeurs_marqueurs_en_sections_gelees"], neufs["debut_ligne_t5_19"])
    # même contrôle contre le brouillon 10 : sa plage gelée ne diffère de celle du brouillon 11 que par les valeurs
    l10 = b10.split("\n")
    d10, f10 = plage_gelee(l10)
    plage11 = "\n".join(b11.split("\n")[slice(*plage_gelee(b11.split("\n")))])
    for nom, valeur in neufs["valeurs_marqueurs_en_sections_gelees"].items():
        plage11 = plage11.replace(valeur, f"`<<{nom}>>`")
    if plage11 != "\n".join(l10[d10:f10]):
        raise Arret("plage gelée du brouillon 11 ≠ celle du brouillon 10 hors valeurs de marqueurs : arrêt")
    diff = differentiel(b4, b10, b11, couples, gel)
    doc_couples = {"brouillon_de_depart": {"chemin": str(B10), "sha256": SHA_B10},
                   "brouillon_gele": {"chemin": str(B4), "sha256": SHA_B4},
                   "brouillon_ecrit": {"chemin": str(B11), "sha256": sha(b11.encode("utf-8"))},
                   "textes_neufs": {"chemin": str(TEXTES), "sha256": sha(TEXTES.read_bytes())},
                   "controle_gel": {k: v for k, v in gel.items() if k != "ligne_t5_19"},
                   "marqueurs_restants": neufs["marqueurs_restants"], "couples": couples}
    if verifier_seulement:
        present = lire(B11)
        if present != b11:
            raise Arret("le brouillon 11 sur disque ≠ celui que le programme reproduit")
        print(f"brouillon 11 reproduit à l'octet : {sha(b11.encode('utf-8'))} ; {len(couples)} opérations ; gel tenu")
        return 0
    if B11.exists() and lire(B11) != b11:
        raise Arret(f"{B11} existe et diffère : on n'écrase jamais (R12) ; changer de nom ou supprimer à la main")
    B11.write_text(b11, encoding="utf-8")
    COUPLES.write_text(json.dumps(doc_couples, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    DIFF.write_text(diff, encoding="utf-8")
    print(f"écrit : {B11} {sha(b11.encode('utf-8'))} ; {len(couples)} opérations ; marqueurs restants : {neufs['marqueurs_restants']}")
    print(f"gel tenu : plage du brouillon 4 {gel['sha_gel_b4'][:16]}…, {gel['lignes_gelees_b4']} lignes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
