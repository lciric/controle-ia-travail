"""Paires de la section « Contre-lecture » du candidat 2 de P4-instrument, et liste finale des pièces versées.

Usage : python -B ecrire_paires_contre_lecture_v1.py PIECES_JSON ENTREES_CHAINE_MD SORTIE_JSON
  PIECES_JSON : liste de {"nom": nom sous prereg/contre-lectures/, "source": chemin dans le bloc-notes} ; l'empreinte
    est lue sur la source (R6) ; chaque nom porte « P4 » (famille des contrôles et du scellement).
  ENTREES_CHAINE_MD : texte exact des entrées « Vérifications de la chaîne v2 » (et de leur traitement), écrit par la
    session au retour des vérifications ; « <<SHA:nom>> » y est remplacé par l'empreinte de la pièce de ce nom.
  SORTIE_JSON : deux paires {"ancien", "nouveau", "source"}, à appliquer après celles du module v3 et de la chaîne v2,
    à la place de la paire « rapports attendus (RC-fidelite-12) » de la chaîne v2 (même ancre, liste complétée).
Écrit seulement SORTIE_JSON et son compagnon ; imprime la liste des noms (pour `RAPPORTS_NOMS` de la chaîne).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ENTREE_EN_ATTENTE = (
    "- **Au candidat, vérification des corrections du brouillon 4** : par un sous-agent neuf, avec la décision R-284 et la\n"
    "  fidélité du module et de la chaîne au texte (Chaîne de lancement). Fichiers à lui donner explicitement : ce candidat,\n"
    "  le brouillon 4, le brouillon 3, le rapport de la contre-lecture 2 et son traitement ; le plan v2 ; le module et ses\n"
    "  tests, avec `NOTES-MODULE.md` ; la chaîne et ses relectures ; la configuration ; les sorties de MC-1 à MC-3 ;\n"
    "  `registres/decisions.md`, `registres/go.md`, `registres/depenses.md` ; le code cité ; `.claude/hooks/garde_calcul.py`.\n"
    "  À ne pas lui donner : `prereg/P3-consignes-v1.md`, le contenu des textes d'action, aucune clé.\n"
)
ANCRE_LISTE = "  À ne pas lui donner : `prereg/P3-consignes-v1.md`, le contenu des textes d'action, aucune clé.\n"

ENTREES = """- **Contre-lecture 3, vérification du candidat 1** : `prereg/contre-lectures/contre-lecture-3-P4-instrument-candidat1-v1.md`
  (`<<SHA:contre-lecture-3-P4-instrument-candidat1-v1.md>>`), sur le candidat 1
  (`<<SHA:P4-instrument-v1-candidat1.md>>`), son module et la décision R-284, sous-agent neuf :
  « scellable après corrections », un majeur (CL3-01 : une lecture sans `--prereg` lit un run décisif avant le verdict
  complété de P3), cinq mineurs, sept de forme.
- **Relectures de la chaîne v1**, par trois sous-agents neufs qui n'ont écrit ni la chaîne ni ce texte :
  « dépense et arrêts », `prereg/contre-lectures/relecture-chaine-depense-P4-instrument-v1.md`
  (`<<SHA:relecture-chaine-depense-P4-instrument-v1.md>>`) : « conforme après corrections », deux
  majeurs (RC-depense-01 : l'arrêt de l'instance n'est ni exécuté ni vérifié par la chaîne ; RC-depense-03 : révocations
  sous des formes voisines, vues ni par le module ni par la garde), sept mineurs, deux informations ; « données et
  fuites », `prereg/contre-lectures/relecture-chaine-donnees-P4-instrument-v1.md`
  (`<<SHA:relecture-chaine-donnees-P4-instrument-v1.md>>`) : « conforme après corrections », six
  mineurs, quatre informations ; « fidélité au texte », `prereg/contre-lectures/relecture-chaine-fidelite-P4-instrument-v1.md`
  (`<<SHA:relecture-chaine-fidelite-P4-instrument-v1.md>>`) : « conforme après corrections », deux
  majeurs (RC-fidelite-01 : cinq citations exigées par la chaîne manquaient au texte ; RC-fidelite-02 : la lecture d'un
  run réel sans `--prereg` ignorait le verdict complété), six mineurs, quatre informations.
- **Traitement de la contre-lecture 3 et des relectures** :
  `prereg/contre-lectures/traitement-CL3-et-relectures-chaine-P4-v1.md`
  (`<<SHA:traitement-CL3-et-relectures-chaine-P4-v1.md>>`) : tous les constats acceptés ; CL3-01 et
  CL3-03 par le module v2 ; les relectures par la chaîne v2 ; CL3-02 et CL3-04 à CL3-12 en mots exacts du rapport.
- **Vérifications du module v2**, par deux sous-agents neufs : « contournement »,
  `prereg/contre-lectures/verification-module-v2-contournement-P4-instrument-v1.md`
  (`<<SHA:verification-module-v2-contournement-P4-instrument-v1.md>>`) : « conforme après
  corrections », deux mineurs, quatre de forme, deux informations ; « fidélité »,
  `prereg/contre-lectures/verification-module-v2-fidelite-P4-instrument-v1.md`
  (`<<SHA:verification-module-v2-fidelite-P4-instrument-v1.md>>`) : « conforme après corrections »,
  trois mineurs, deux de forme. Traitement : `prereg/contre-lectures/traitement-verifications-module-v2-P4-v1.md`
  (`<<SHA:traitement-verifications-module-v2-P4-v1.md>>`) : tous acceptés ; module v3.
- **Vérification du module v3**, par un sous-agent neuf : `prereg/contre-lectures/verification-module-v3-P4-instrument-v1.md`
  (`<<SHA:verification-module-v3-P4-instrument-v1.md>>`) : « conforme après corrections », un constat
  de forme (VM3-01 : deux phrases proposées pour ce texte, corrigées par le vérificateur et appliquées ici), sept
  informations ; 258 tests passés (71, 49 et 138).
<<ENTREES_CHAINE>>- **Au candidat 2, vérification des corrections** : par un sous-agent neuf, qui n'a écrit ni ce texte, ni le module,
  ni la chaîne, ni aucun rapport. Fichiers à lui donner explicitement : ce candidat, le candidat 1, les rapports et
  traitements ci-dessus ; le module v3 et ses tests, avec ses notes ; la chaîne retenue, ses notes et ses
  vérifications ; la configuration ; les sorties de MC-1 à MC-3 ; `registres/decisions.md`, `registres/go.md`,
  `registres/depenses.md` ; le code cité ; `.claude/hooks/garde_calcul.py`.
  À ne pas lui donner : `prereg/P3-consignes-v1.md`, le contenu des textes d'action, aucune clé.
"""


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    pieces = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    noms = [p["nom"] for p in pieces]
    if len(set(noms)) != len(noms) or any("P4" not in n or "/" in n for n in noms):
        raise SystemExit("noms en double, sans « P4 » ou avec un dossier")
    empreintes = {p["nom"]: sha(Path(p["source"])) for p in pieces}
    chaine = Path(argv[2]).read_text(encoding="utf-8")
    nouveau = ENTREES.replace("<<ENTREES_CHAINE>>", chaine)

    def remplir(m: re.Match) -> str:
        if m.group(1) not in empreintes:
            raise SystemExit(f"pièce citée hors de la liste : {m.group(1)}")
        return empreintes[m.group(1)]

    nouveau = re.sub(r"<<SHA:([^>]+)>>", remplir, nouveau)
    if "<<" in nouveau or nouveau.count(ANCRE_LISTE) != 1:
        raise SystemExit("gabarit non rempli, ou ancre de la liste absente ou en double")
    liste = (ANCRE_LISTE
             + "- **Rapports, traitements et brouillons versés** (sous `prereg/contre-lectures/`, avec leurs sceaux ; noms\n"
             + "  exacts, seuls de leur famille « P4 », relus par les contrôles et le scellement) :\n"
             + " ;\n".join(f"  `prereg/contre-lectures/{n}` (`{empreintes[n]}`)" for n in noms) + ".\n")
    paires = [
        {"ancien": ENTREE_EN_ATTENTE, "nouveau": nouveau,
         "source": "session : section « Contre-lecture » (contre-lecture 3, relectures, vérifications du module et de la chaîne)"},
        {"ancien": ANCRE_LISTE, "nouveau": liste,
         "source": "session : liste des pièces versées (chaîne v2, RC-fidelite-12, complétée : traitements, vérifications, brouillons)"},
    ]
    sortie = Path(argv[3])
    sortie.write_text(json.dumps(paires, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    Path(str(sortie) + ".sha256").write_text(f"{sha(sortie)}  {sortie.name}\n", encoding="utf-8")
    print(" ".join(noms))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
