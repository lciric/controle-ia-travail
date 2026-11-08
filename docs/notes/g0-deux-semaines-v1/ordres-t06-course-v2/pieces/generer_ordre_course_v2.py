"""Brouillon v2 de l'ordre de la course de T0.6 = brouillon v1 (`ordres-t06-course-v1/ordre-fille-6-t06-course-v1-brouillon.md`) + les 7 couples de la contre-lecture de la chaîne de la course (fille 9, `couples-ordre-course-v1.json`,
copie dans `pieces/`) + la chaîne v12 (lanceur v12, amorce v10, bras B v4, liste figée v2) + la suite à 67 minutes mesurée à E3 bis et le devis v3 + « motifs=28 » + la borne de l'annexe du bras B. Chaque remplacement doit
trouver son texte exactement une fois, sinon arrêt sans rien écrire.

    python3 -I -B generer_ordre_course_v2.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

D2 = "docs/notes/g0-deux-semaines-v1/ordres-t06-course-v2/"
V1 = "docs/notes/g0-deux-semaines-v1/ordres-t06-course-v1/ordre-fille-6-t06-course-v1-brouillon.md"
SORTIE = D2 + "ordre-fille-6-t06-course-v2-brouillon.md"
COUPLES = D2 + "pieces/couples-ordre-course-v1.json"
SHA_COUPLES = "67b9c8eae03172d5ec8f4d1f6fe920dbe0ca42200a0a4a89cbc6eab551f9e888"


def main(racine: Path) -> int:
    src, sortie, cp = racine / V1, racine / SORTIE, racine / COUPLES
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    if hashlib.sha256(cp.read_bytes()).hexdigest() != SHA_COUPLES:
        raise SystemExit("couples : empreinte non conforme")
    t = src.read_text(encoding="utf-8")

    def une(nom, ancien, nouveau):
        nonlocal t
        n = t.count(ancien)
        if n != 1:
            raise SystemExit(f"{nom} : « {ancien[:80]}… » trouvé {n} fois, une attendue : arrêt, rien écrit")
        t = t.replace(ancien, nouveau)

    # 1. les 7 couples de la contre-lecture (v10 → textes d'origine ; l'adaptation à la chaîne v12 suit)
    couples = json.loads(cp.read_text(encoding="utf-8"))
    assert len(couples) == 7
    for i, c in enumerate(couples, 1):
        une(f"couple {i}", c["ancien"], c["nouveau"])
    # 2. chaîne v12
    for ancien, nouveau, n in (("scripts/lancer_t06_v10.sh", "scripts/lancer_t06_v12.sh", None), ("amorce v8", "amorce v10", None), ("prep/t06-course-v1", "prep/t06-course-v12", None),
                               ("audit-fuite-r1-v4-bras-b-v1.json", "audit-fuite-r1-v4-bras-b-v4.json", None)):
        if ancien not in t:
            raise SystemExit(f"chaîne v12 : « {ancien} » absent")
        t = t.replace(ancien, nouveau)
    une("titre", "bras B en annexe — brouillon v1", "bras B v4 en annexe — brouillon v2")
    une("statut", "Brouillon v1 de la fille 10 (session de développement, Sonnet 5.5), à contre-lire (Opus) et à sceller par la session mère `session_01Qi7Gr6NLmhhAcdmnACBC7G`. **Non scellé.**",
        "Brouillon v2 de la fille 10 (session de développement, Sonnet 5.5), à contre-lire et à sceller par la session mère (R12 : le brouillon v1 reste). **Non scellé.** Il applique les 7 couples de la contre-lecture de la chaîne de la course (`couples-ordre-course-v1.json`, `67b9c8ea…`) et adopte la **chaîne v12** : lanceur `scripts/lancer_t06_v12.sh`, amorce `scripts/amorce_instance_t06_v10.sh` (bras B v4 par défaut, suite d'essais figée v2 de 83 fichiers), `session_v11`, `lanceur_v5`, `configuration_v5`.")
    une("devis", "la ligne d'engagement du devis v2 (`docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v2.md`).",
        "la ligne d'engagement du devis v3 (`docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v3.md`, suite d'essais mesurée à 67 minutes).")
    une("engagement", "**attendu ≈ 17 à 27 USD sur A100, ≈ 43 à 74 USD sur H200 NVL ; pire cas ≈ 160 USD ; arrêt par identifiant à 200 USD cumulés**",
        "**attendu ≈ 18 à 28 USD sur A100, ≈ 46 à 78 USD sur H200 NVL ; pire cas ≈ 173 USD aux prix constatés, ≈ 198 USD à la borne de 4,70 USD/h (marge ≈ 2 USD sous les 200) ; arrêt par identifiant à 200 USD cumulés ; au-delà de 180 USD toute relance est un nœud de Lazar** ; la A100 la moins chère valait 2,07 USD/h le 8 novembre (E3 bis) : la fenêtre de trois heures peut s'épuiser et la course se jouer sur la H200 NVL")
    une("clonage", "`CLONAGE mode=reel …` (au plus 600 Mo, dans les 20 minutes) ; installation ;",
        "`CLONAGE mode=reel … motifs=28` (au plus 600 Mo, dans les 20 minutes ; **28 motifs, et non 27**) ; installation ;")
    une("tests", "ligne `nvidia-smi` (A100-SXM4-80GB ou H200 NVL) ; `MATERIEL …` ; « tests : N passed » ;",
        "ligne `nvidia-smi` (A100-SXM4-80GB ou H200 NVL) ; `MATERIEL …` ; « suite ciblée : 83 fichiers d'essais, liste scripts/tests-cibles-t06-v2.txt sha256 … » ; **« tests : 1914 passed in … » environ 68 minutes après `MATERIEL`** (E3 bis : « 1878 passed in 4009.60s (1:06:49) » pour la liste v1 ; la liste v2 compte 1 914 essais en local, 2 % de plus ; **la liste v2 n'a pas été relevée sur l'instance** : si l'instance compte autre chose, l'amorce s'arrête avant le run avec « tests : … ≠ 1914 passed » ; c'est la garde voulue, environ une heure de machine perdue, aucune donnée fausse : **ne détruis pas**, relève la ligne et écris à la mère) ; « tests : N passed » ne doit pas manquer plus de **90 minutes** après `MATERIEL` (sinon attendu manquant) ;")
    une("calendrier", "**Étape 3 — surveillance.**", "**Calendrier de la surveillance (chaîne v12).** Compter, à partir de la création : démarrage de l'amorce ≈ 30 s ; clonage ≈ 1 minute ; installation ≈ 4 minutes ; **suite d'essais ≈ 68 minutes** (la mesure d'E3 bis est de 67 minutes sur 255 cœurs) ; le premier `PROGRES` du run n'arrive donc qu'environ **1 h 15 après la création** ; le run (11 à 17 h de marche au devis v3) ; le bras B ; l'arrêt. Une absence de `PROGRES` avant 1 h 30 n'est pas encore un attendu manquant ; l'alerte « sans `PROGRES` depuis 2 h » du lanceur est inchangée.\n\n**Étape 3 — surveillance.**")
    une("bras B config", "configuration du bras B `docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json` (`.sha256` écrit par la mère)",
        "configuration du bras B `docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json` (`.sha256` écrit par la mère ; inchangée, la configuration ne nomme pas le module) ; addendum du bras B v3 (`addendum-bras-b-v2-brouillon-v3.md`), scellé par la mère avant toute lecture")
    une("bras B module", "Régi par `prereg/audit-fuite-r1-v4-v1.md` (point 7), non par ce texte ni par T0.6.",
        "Régi par `prereg/audit-fuite-r1-v4-v1.md` (point 7) et par l'addendum scellé du bras B (tolérance de G4 **0,3** en log-cote, borne incluse ; **lecture stricte** : sur A100-SXM4-80GB aux mêmes versions tout écart au bit arrête ; GO-2026-11-08-01), non par ce texte ni par T0.6. Module joué par défaut par l'amorce v10 : `controle_ia.audit_fuite_r1_v4.bras_b_v4`. **Sur la H200 NVL, le bras B peut s'arrêter en code 1 à G4 sans défaut réel** (autre carte : tolérance de score) : attendu manquant isolé, rien à relancer.")
    une("sortie bras B", "`traces/bras-b-…/bras-b.out` porte l'issue du bras B (`{\"issue\": …}`) : **ne l'ouvre pas**, ni `bras-b.err` (noms et tailles seulement).",
        "`traces/bras-b-…/bras-b.out` ne porte que le chemin et l'empreinte de la sortie scellée du bras B (le module v4 n'imprime jamais l'issue), mais l'issue est dans `diag/bras-b-…/audit-fuite-r1-v4-bras-b-v4.json` : **ne l'ouvre pas**, ni `bras-b.out` ni `bras-b.err` (noms et tailles seulement).")
    # 3. réserves
    une("réserves", "## 7. Compte rendu (message à la mère,",
        "## 6 bis. Réserves de ce brouillon (à ne pas masquer au compte rendu)\n- **Amorce v10, lanceur v12, `lanceur_v5`, `session_v11` et le bras B v4 n'ont jamais été joués sur une instance** : E3 bis joue la chaîne v11 (amorce v9, liste v1) ; la course est leur premier vol réel. Tout écart de comportement est un attendu manquant, à relever sans relancer.\n- **La liste figée v2 n'a pas été relevée sur l'instance** : 1 914 est la valeur du poste local (Python 3.11.18), égale à celle de l'instance sur la liste v1 (1 878 = 1 878).\n- **Débit de la H200 NVL non mesuré** (supposé égal à celui de la A100) ; bras B jamais joué sur une carte.\n- **Le devis v3 reste sous le plafond de 200 USD**, mais le pire cas à la borne de 4,70 USD/h (≈ 198 USD) n'a qu'environ 2 USD de marge : au-delà de 180 USD cumulés, relance = nœud de Lazar.\n\n## 7. Compte rendu (message à la mère,")
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(t, encoding="utf-8")
    print(hashlib.sha256(sortie.read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
