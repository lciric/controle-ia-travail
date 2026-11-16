"""Programme de couples : commande de la phase B du compte 3, du brouillon v2 à la version 3 — v1.

Écrit le 2026-11-16 (à partir de 13:12:02Z, `date -u`) par le préparateur de la version 3 (sous-agent neuf de la session mère,
modèle A ; aucun identifiant de modèle écrit). Le brouillon v2 (`commande-compte-3-phase-b-v2.md`, empreinte ci-dessous, scellé par la
mère pour son intégrité seulement) n'est pas touché (R12) : ce programme écrit un fichier neuf, et refuse si ce fichier existe.

Chaque couple (ancien, nouveau) doit trouver son ancien texte exactement une fois dans le texte courant ; sinon rien n'est écrit.
Bibliothèque standard seule ; n'écrit que le fichier de sortie ; n'affiche que des noms, des comptes et des empreintes.

    python3 -I -B couples_commande_phase_b_v3_v1.py <brouillon v2> <version 3, fichier neuf>
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

H_V2 = "e0dba2aad0accfba58dd6e77d4f74e264ae704be3b96ada5edb29ed84080e94f"

COUPLES: list[tuple[str, str, str]] = [
    ("titre", "(appel unique) — v2\n", "(appel unique) — v3\n"),
    ("statut : phase C v3 ou v4",
     "  (`commande-compte-3-phase-c-v3.md`). Aucune dépense",
     "  (`commande-compte-3-phase-c-v3.md`, ou sa version 4, en cours). Aucune dépense"),
    ("version 3, puis brouillon v2",
     "- **Version 2** : la version 1 est le gabarit de la section 9 de `commande-compte-3-v1.md` (`21d891c5…`, gardée, R12 : « Ne joue aucun\n",
     "- **Version 3** : écrite à partir du brouillon v2 (`commande-compte-3-phase-b-v2.md`,\n"
     "  `e0dba2aad0accfba58dd6e77d4f74e264ae704be3b96ada5edb29ed84080e94f`, scellé par la mère pour son intégrité seulement, jamais remis\n"
     "  ni contre-lu, gardé, R12) par un programme de couples versé (`couples_commande_phase_b_v3_v1.py`, même dossier). Changements, et\n"
     "  seulement eux : (1) noms des pièces de cette version (`commande-compte-3-phase-b-v3.md`, `repetition-phase-b-v3/`,\n"
     "  `rapport-preparateur-phase-b-v3.md`) et du journal provisoire (`…-v3.md`) ; (2) bloc B2 : `pip install --no-cache-dir` (le cache\n"
     "  de pip doublerait la place prise par torch) ; (3) bloc B3 : la somme des tailles des cinq entrées est imprimée, à comparer aux\n"
     "  tailles lues au distant (`prealables-v1.md`, P1.4) ; (4) bloc 1B : `bbis` et `b-bis` ajoutés aux noms interdits, comme à la\n"
     "  phase A ; (5) section 15, point 2 : la condition de l'audit R4 de la base (A) (T0.8, l. 111) avant la ligne\n"
     "  `ISSUE-MOTS-ET-COUT-T06`, que cette commande ne lève pas (nœud porté à la mère) ; (6) rédacteurs, pièces et annexe à jour. Noms du\n"
     "  bac et des fichiers de marque **inchangés depuis le brouillon v2, à dessein** (comme la phase C de sa v2 à sa v4) : un bac déjà\n"
     "  ouvert arrête le bloc 1B, et le marqueur d'appel est le même d'une version à l'autre (aucun second appel possible).\n"
     "- **Brouillon v2** : la version 1 est le gabarit de la section 9 de `commande-compte-3-v1.md` (`21d891c5…`, gardée, R12 : « Ne joue aucun\n"),
    ("renvoi au rapport v3",
     "  choix et limites : `rapport-preparateur-phase-b-v2.md`, même dossier.\n",
     "  choix et limites : `rapport-preparateur-phase-b-v3.md`, même dossier (différentiel avec le gabarit et avec le brouillon v2).\n"),
    ("rédacteurs",
     "- **Rédacteur** : préparateur neuf, sous-agent de la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` (même modèle qu'elle, noté\n"
     "  « modèle A » dans ce dossier ; aucun identifiant de modèle écrit), le 2026-11-16 à partir de 12:06:54Z (`date -u`) ; ni lecteur ni juge\n"
     "  d'aucun verdict ; aucune entrée ni sortie de 7a, de 7b ou de T0.7 ouverte (noms, tailles et empreintes seulement) ; répétitions sur\n"
     "  données factices fabriquées par lui.\n",
     "- **Rédacteurs** (aucun identifiant de modèle écrit ; lettres de ce dossier) : brouillon v2, un préparateur neuf, sous-agent de la\n"
     "  session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` (modèle B), le 2026-11-16 à partir de 12:06:54Z (`date -u`), arrêté par une limite\n"
     "  d'usage vers 13:05Z avant d'avoir fini ; version 3, un préparateur neuf, sous-agent de la même session mère (modèle A), le\n"
     "  2026-11-16 à partir de 13:12:02Z (`date -u`). Ni l'un ni l'autre n'est lecteur ni juge d'aucun verdict ; aucune entrée ni sortie de\n"
     "  7a, de 7b ou de T0.7 ouverte (noms, tailles et empreintes seulement) ; répétitions sur données factices fabriquées par eux.\n"),
    ("pièces : répétition v3",
     "- **Pièces** (sous-dossier `repetition-phase-b-v2/` de `docs/procedures/lecture-7b-etape-b-compte-3-v1/`, chacune scellée) :\n",
     "- **Pièces** (sous-dossier `repetition-phase-b-v3/` de `docs/procedures/lecture-7b-etape-b-compte-3-v1/`, chacune scellée) :\n"),
    ("pièces : scripts et sortie de la répétition",
     "| `repetition_phase_b_jouet_v2.sh`, `fabrique_depots_jouets_phase_b_v2.py`, sortie `repetition-phase-b-jouet-sortie-v2.txt` |",
     "| `repetition_phase_b_jouet_v3.sh`, `fabrique_depots_jouets_phase_b_v3.py`, sortie `repetition-phase-b-jouet-sortie-v3.txt` |"),
    ("pièces : constantes",
     "| `verification_constantes_phase_b_v2.sh`, sortie `verification-constantes-phase-b-sortie-v2.txt` |",
     "| `verification_constantes_phase_b_v3.sh`, sortie `verification-constantes-phase-b-sortie-v3.txt` |"),
    ("point 4 : sans cache de pip",
     "dans ta copie du dépôt, le bloc B2 l'installe là (dossier ignoré par git ; environ 6 Go ; 10 à 20 minutes ; 9 Gio libres exigés) :",
     "dans ta copie du dépôt, le bloc B2 l'installe là (dossier ignoré par git ; sans cache de pip ; environ 6 Go ; 10 à 20 minutes ; 9 Gio\n"
     "   libres exigés) :"),
    ("bloc 0b-B : commande v3",
     "F=docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-b-v2.md\n",
     "F=docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-b-v3.md\n"),
    ("bloc 1B : noms interdits de B bis",
     "INTERDITS_NOMS='lecture-sondes|resume\\.json|activations|adaptateur|distillation|bras-attaque|mode-tenu|etiqueteur|quarantaine|mesure-unanime|t07|t0\\.7'\n",
     "INTERDITS_NOMS='lecture-sondes|resume\\.json|activations|adaptateur|distillation|bras-attaque|mode-tenu|etiqueteur|quarantaine|mesure-unanime|t07|t0\\.7|bbis|b-bis'\n"),
    ("bloc B2 : sans cache de pip",
     "{ python3 -m venv \"$1\" && \"$1/bin/pip\" install -q --disable-pip-version-check -r \"$2\"; }",
     "{ python3 -m venv \"$1\" && \"$1/bin/pip\" install -q --disable-pip-version-check --no-cache-dir -r \"$2\"; }"),
    ("bloc B3 : somme des tailles des cinq entrées",
     "echo \"entrées placées hors du dépôt : $n fichiers, $(du -sb \"$ENTREES\" | cut -f1) octets ; aucun nom interdit ; aucun ouvert\"\n"
     "# attendu : compagnons « OK » (silencieux) ; « manifeste de 7b égal … » ; dix fichiers, environ 18 960 000 octets (dossiers compris : un peu\n"
     "# plus) ; aucun « ARRÊT ». Relancé : dix « déjà là, égal ».\n",
     "o=0; for f in runs/$R6/manifeste.json diag/$R6/episodes-t06.json diag/$R6/lecture-cout-t06.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do\n"
     "    o=$(( o + $(stat -c %s \"$ENTREES/$f\") )); done\n"
     "echo \"entrées placées hors du dépôt : $n fichiers ; cinq entrées : $o octets ; aucun nom interdit ; aucun ouvert\"\n"
     "# attendu : compagnons « OK » (silencieux) ; « manifeste de 7b égal … » ; « 10 fichiers ; cinq entrées : 18959392 octets » (somme des\n"
     "# tailles lues au distant à la tête 55c3e3eb, prealables-v1.md, P1.4 : 8 509, 1 556 085, 125 598, 1 830 726 et 15 438 474 octets) ;\n"
     "# aucun « ARRÊT ». Une autre somme n'arrête pas (les empreintes font foi) : dis-la à Lazar en une ligne. Relancé : dix « déjà là, égal ».\n"),
    ("bloc F-B : nom du journal v3",
     "echo \"registres-provisoires/compte-3-phase-b-$(date -u +%Y-%m-%d-%H%M)-v2.md\" > \"$BAC/nom-provisoire-p-v2.txt\"",
     "echo \"registres-provisoires/compte-3-phase-b-$(date -u +%Y-%m-%d-%H%M)-v3.md\" > \"$BAC/nom-provisoire-p-v2.txt\""),
    ("bloc F-B : titre du journal v3",
     "sur 7b — journal provisoire (v2)\"; echo",
     "sur 7b — journal provisoire (v3)\"; echo"),
    ("bloc F-B : commande v3 exécutée",
     "  echo \"- P3B-001 : commande phase B v2 exécutée depuis",
     "  echo \"- P3B-001 : commande phase B v3 exécutée depuis"),
    ("section 15, point 2 : audit R4 de la base (A)",
     "   Code 3 : aucune ligne (BA-L0) ; nœud de Lazar. Code 2 : rien ; la mère lève la cause et fait écrire une version nouvelle.\n",
     "   Code 3 : aucune ligne (BA-L0) ; nœud de Lazar. Code 2 : rien ; la mère lève la cause et fait écrire une version nouvelle.\n"
     "   **Condition que cette commande ne lève pas, avant la ligne `ISSUE-MOTS-ET-COUT-T06`** : la base (A) scellée (T0.8, l. 111, « Audit\n"
     "   R4 ») veut, si l'audit R4 se déclenche, une relecture « avant l'inscription de `ISSUE-MOTS-ET-COUT-T06`, par un lecteur neuf » ;\n"
     "   la pièce en écrit l'état dans `base-a-t08.json` (réserve R-BA6), que la mère n'ouvre pas (elle n'en lit que l'état de BA-L2, par\n"
     "   programme, R-2741) : qui lit cet état, et comment, est à trancher par Lazar avant cette ligne (nœud ; rapport du préparateur v3,\n"
     "   point M-1). Rien ici ne change l'ordre de la phase C (section 15) : les deux lignes, puis le bloc M.\n"),
    ("section 15, point 3 : bloc M identique dans la v4",
     "3. **Bloc M** de la phase C v3 (section 15), avec `BRP='verdict/t06-mots-et-cout-compte-3-v1'` :",
     "3. **Bloc M** de la phase C v3 (section 15 ; le même, à l'octet, dans le brouillon 1 de sa v4), avec\n"
     "   `BRP='verdict/t06-mots-et-cout-compte-3-v1'` :"),
    ("annexe : répétition v3",
     "  `repetition-phase-b-v2/repetition_phase_b_jouet_v2.sh`, sortie `repetition-phase-b-v2/repetition-phase-b-jouet-sortie-v2.txt` (résultat\n"
     "  au rapport).",
     "  `repetition-phase-b-v3/repetition_phase_b_jouet_v3.sh`, sortie `repetition-phase-b-v3/repetition-phase-b-jouet-sortie-v3.txt` (résultat\n"
     "  au rapport v3)."),
    ("annexe : bloc M des deux versions de la phase C",
     "  bloc M de la phase C v3 rejoué sur la branche jouet (état de BA-L2 lu dans une vraie sortie de la pièce) ;",
     "  bloc M de la phase C v3 (égal à celui du brouillon 1 de sa v4, comparé par la répétition) rejoué sur la branche jouet (état de\n"
     "  BA-L2 lu dans une vraie sortie de la pièce) ;"),
    ("annexe : constantes v3",
     "- **Constantes** : `repetition-phase-b-v2/verification_constantes_phase_b_v2.sh`, sortie\n"
     "  `repetition-phase-b-v2/verification-constantes-phase-b-sortie-v2.txt` :",
     "- **Constantes** : `repetition-phase-b-v3/verification_constantes_phase_b_v3.sh`, sortie\n"
     "  `repetition-phase-b-v3/verification-constantes-phase-b-sortie-v3.txt` :"),
]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[-1])
        return 1
    src, dst = Path(argv[0]), Path(argv[1])
    if dst.exists():
        print(f"ARRÊT : {dst} existe déjà (R12)")
        return 1
    octets = src.read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != H_V2:
        print(f"ARRÊT : brouillon v2 d'empreinte {h}, {H_V2} attendue")
        return 1
    t = octets.decode("utf-8")
    for nom, ancien, nouveau in COUPLES:
        n = t.count(ancien)
        if n != 1:
            print(f"ARRÊT : couple « {nom} » : ancien texte trouvé {n} fois (une exigée) ; rien n'est écrit")
            return 1
        t = t.replace(ancien, nouveau)
        print(f"couple appliqué : {nom}")
    reste = [x for x in ("commande-compte-3-phase-b-v2.md\n", "repetition-phase-b-v2/", "rapport-preparateur-phase-b-v2")
             if x in t.replace("(`commande-compte-3-phase-b-v2.md`,\n", "")]
    if reste:
        print(f"ARRÊT : noms de la version 2 restants hors du renvoi au brouillon : {reste} ; rien n'est écrit")
        return 1
    dst.write_text(t, encoding="utf-8")
    print(f"{len(COUPLES)} couples ; {dst} : {hashlib.sha256(t.encode('utf-8')).hexdigest()} ; {t.count(chr(10))} lignes ; "
          f"{t.count('```bash')} blocs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
