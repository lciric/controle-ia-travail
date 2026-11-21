#!/usr/bin/env python3
"""Fabrique `ordre-etalonnage-ii-b-v5-brouillon5.md` depuis le brouillon 4 : les deux corrections de forme (F1, F2) et le
mineur (m1) de la vérification courte de l'ordre, rien d'autre.

Usage : python3 -I -B fabriquer-ordre-etalonnage-ii-b-v5-brouillon5-v1.py RACINE_DU_DEPOT DOSSIER DATE

Méthode : empreinte du brouillon 4 vérifiée ; empreinte et compagnon de la note de vérification vérifiés ; chaque changement est
un remplacement dont l'ancre est trouvée le nombre de fois attendu, sinon rien n'est écrit ; les champs restent les mêmes.
Écrit le brouillon 5, la note des différences (une par ligne), leurs compagnons ; n'écrase rien (R12).
"""
import hashlib
import re
import sys
from pathlib import Path

B4 = "ordre-etalonnage-ii-b-v5-brouillon4.md"
B4_SHA = "12fb6dac586ebd6410b69e7af600beb4b6e429c0cc829f2d37fce5dbfa8b7e32"
B5 = "ordre-etalonnage-ii-b-v5-brouillon5.md"
NOTE = "differences-ordre-etalonnage-v5-brouillon4-vers-5-v1.md"
VO_CHEMIN = "brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/note-verification-ordre-etalonnage-v5-brouillon4-cl1-v1.md"
VO = "958b5f94350f46011e523d255b34bd9a5979d11e6add72a7c27caf017eaf15e4"
D = "distillateur-v5/correctifs/"

CHANGEMENTS = [
    ("titre", "machine à part — brouillon 4\n", "machine à part — brouillon 5\n", 1),
    ("statut", "- **Statut** : **brouillon 4**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme",
     "- **Statut** : **brouillon 5**, pièce décisive (ordre d'une course payante). Fabriqué par programme (`fabriquer-ordre-etalonnage-ii-b-v5-brouillon5-v1.py`) depuis le brouillon 4 (`" + B4 + "`, `" + B4_SHA + "`, intact, R12), le @@DATE@@, par le même rédacteur, sous le même mandat : il porte les deux corrections de forme et le mineur de la vérification courte du brouillon 4 par un autre modèle (`" + VO_CHEMIN + "`, `" + VO + "` : « scellable une fois les champs remplis, après deux corrections de forme » ; aucune ne touche une règle), et rien d'autre ; ces corrections ne sont pas encore vérifiées par ce vérificateur ; différences, une par ligne : `" + NOTE + "`. Le brouillon 4, non contre-lu alors, avait été fabriqué par programme", 1),
    ("m1, § 3, marques de progrès", "- **Marques de progrès** (M2) : une ligne par lot, par passe d'oracle et pour les épreuves, lue par la surveillance.",
     "- **Marques de progrès** (M2), lues par la surveillance : le chargement, le début, chaque lot, les oracles écrits, la fin, et l'arrêt s'il y en a un ; les épreuves ne se jouent pas sur la machine : elles se jouent au passage des conditions, sur processeur (§ 5 étape 6).", 1),
    ("F1, § 7, phrase des noms", "après chaque lot de huit épisodes, les sorties d'oracle sous `diag/<run>/lots/` et les identifiants des actions sous `donnees/<run>/lots/`, scellés et poussés ;",
     "après chaque lot de huit épisodes, les sorties d'oracle sous `diag/<run>/lots/lot-*.json` et les identifiants des actions sous `donnees/<run>/lots/ids-lot-*.json`, scellés et poussés ; aucun fichier d'ensemble des identifiants n'est écrit ;", 1),
    ("F1, § 7, ligne des lots et de l'ensemble",
     "| par lot, puis fin de l'étalonnage | `etalonnage-oracles-iib-v5.json`, `ids-actions-etalonnage-iib-v5.json` | sorties des deux oracles, sans aucun texte ; identifiants des actions ; durées mesurées, une par oracle |",
     "| après chaque lot | `diag/<run>/lots/lot-*.json` ; `donnees/<run>/lots/ids-lot-*.json` | sorties des deux oracles pour le lot, sans aucun texte ; identifiants des actions du lot |\n| fin de l'étalonnage | `diag/<run>/etalonnage-oracles-iib-v5.json` | sorties des deux oracles, sans aucun texte |\n| fin de l'étalonnage | `diag/<run>/graines-etalonnage-iib-v5.json` | entropie, préfixe et clés des graines |", 1),
    ("F1, § 7, ligne des rapportés", "| fin de l'étalonnage | `rapportes-etalonnage-iib-v5.json` | rapportés sans règle (texte scellé, section 13), contrôle du premier coût compris |",
     "| fin de l'étalonnage | `diag/<run>/rapportes-etalonnage-iib-v5.json` | rapportés sans règle (texte scellé, section 13), contrôle du premier coût et durées mesurées par oracle compris |", 1),
    ("F1, § 7, ligne de l'arrêt", "| tout arrêt | ce qui existe, avec le motif | versé avant tout le reste |",
     "| toute garde, toute erreur, tout signal d'arrêt | `diag/<run>/arret.json`, et les lots déjà écrits | étape, motif, liste de ce qui est écrit ; versé avant tout le reste ; ni fichier d'ensemble ni issue |", 1),
    ("F2, § 11, correctif de rang 9", "| `correctifs/0001-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 9) |", "| `" + D + "0001-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 9) |", 1),
    ("F2, § 11, correctif de rang 10", "| `correctifs/0002-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 10) |", "| `" + D + "0002-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 10) |", 1),
    ("F2, § 11, correctif de rang 11", "| `correctifs/0003-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 11) |", "| `" + D + "0003-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 11) |", 1),
    ("F2, § 11, phrase des chemins", "les lignes 7 à 13 sont sous `brouillons/ii-b-saboteur-budget-v5/code-v5/` ;",
     "les six premières lignes sont sous `brouillons/ii-b-saboteur-budget-v5/code-v5/correctifs/` ; les lignes 7 à 13 sont écrites depuis `brouillons/ii-b-saboteur-budget-v5/code-v5/`, celles des rangs 9 à 11 sous `brouillons/ii-b-saboteur-budget-v5/code-v5/distillateur-v5/correctifs/` ;", 1),
]


def sha(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def ecrire(chemin: Path, texte: str) -> str:
    if chemin.exists() or Path(str(chemin) + ".sha256").exists():
        sys.exit(f"{chemin} existe déjà : refus d'écraser (R12)")
    chemin.write_bytes(texte.encode("utf-8"))
    e = sha(chemin)
    Path(str(chemin) + ".sha256").write_text(f"{e}  {chemin.name}\n", encoding="utf-8")
    return e


def main(argv) -> int:
    if len(argv) != 4:
        sys.exit("usage : RACINE_DU_DEPOT DOSSIER DATE")
    racine, dossier, date = Path(argv[1]), Path(argv[2]), argv[3]
    if sha(dossier / B4) != B4_SHA:
        sys.exit("brouillon 4 : empreinte différente de celle attendue")
    if sha(racine / VO_CHEMIN) != VO or (racine / (VO_CHEMIN + ".sha256")).read_text(encoding="utf-8").split()[0] != VO:
        sys.exit("note de vérification de l'ordre : empreinte ou compagnon différents")
    for rang in ("0001", "0002", "0003"):
        if not (racine / "brouillons/ii-b-saboteur-budget-v5/code-v5" / D / f"{rang}-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch").is_file():
            sys.exit(f"correctif {rang} du distillateur absent du chemin écrit")
    texte = (dossier / B4).read_text(encoding="utf-8")
    avant = sorted(set(re.findall(r"<<([A-Z0-9_]+)>>", texte)))
    lignes = []
    for nom, ancre, neuf, compte in CHANGEMENTS:
        n = texte.count(ancre)
        if n != compte:
            sys.exit(f"changement « {nom} » : ancre trouvée {n} fois, {compte} attendu : {ancre[:80]!r}")
        neuf = neuf.replace("@@DATE@@", date)
        texte = texte.replace(ancre, neuf)
        a, b = " ".join(ancre.split()), " ".join(neuf.split())
        lignes.append(f"- {nom} ({compte} fois) : « {a[:110]}{'…' if len(a) > 110 else ''} » remplacé par « {b[:260]}{'…' if len(b) > 260 else ''} ».")
    if "@@" in texte or sorted(set(re.findall(r"<<([A-Z0-9_]+)>>", texte))) != avant:
        sys.exit("jeton non rempli, ou champs changés")
    for interdit in ("ids-actions-etalonnage-iib-v5.json", "| `correctifs/000", "et pour les épreuves, lue"):
        if interdit in texte:
            sys.exit(f"reste inattendu : {interdit}")
    e5 = ecrire(dossier / B5, texte)
    note = ["# Différences — ordre de l'étalonnage de l'organisme retenu, du brouillon 4 au brouillon 5 — v1", "",
            f"Source : `{B4}` (`{B4_SHA}`). Produit : `{B5}` (`{e5}`). Écrite par le programme `fabriquer-ordre-etalonnage-ii-b-v5-brouillon5-v1.py`, le {date}. Cause : `{VO_CHEMIN}` (`{VO}`), corrections F1 et F2, mineur m1. Une différence par ligne ; tout le reste est recopié à l'octet ; les neuf champs sont inchangés.", "",
            "## Remplacements, un par ligne (ancre trouvée le nombre de fois attendu)", ""] + lignes
    note += ["", "## Champs gardés, un par ligne", ""] + [f"- `<<{n}>>`." for n in avant]
    e_note = ecrire(dossier / NOTE, "\n".join(note) + "\n")
    print(f"brouillon 5 : {e5} ; {len(CHANGEMENTS)} remplacements ; champs : {len(avant)}")
    print(f"note des différences : {e_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
