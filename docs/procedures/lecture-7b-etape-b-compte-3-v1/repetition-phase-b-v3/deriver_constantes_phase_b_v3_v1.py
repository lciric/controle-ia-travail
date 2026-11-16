"""Dérivation de la vérification des constantes v3 de la phase B du compte 3 à partir de celle du brouillon v2 — v1.

Écrit le 2026-11-16 par le préparateur de la version 3 (modèle A ; aucun identifiant de modèle écrit). Le script v2 n'est pas touché
(R12) : ce programme écrit un fichier neuf, et refuse s'il existe ; chaque couple doit trouver son ancien texte le nombre de fois dit.

    python3 -I -B deriver_constantes_phase_b_v3_v1.py <vérification v2> <vérification v3, fichier neuf>
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

H_V2 = "2266850598c3d39a3ee4788cd81b2b7ff6a964f9d296633365b4d26f67fcd804"

AJOUT = r'''# --- ajouts de la v3 : noms interdits contre les chemins des entrées ; somme des tailles du bloc B3 contre prealables-v1.md (P1.4)
n=0; for f in runs/$R6/manifeste.json diag/$R6/episodes-t06.json diag/$R6/lecture-cout-t06.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do
    for g in "$f" "$f.sha256"; do printf '%s\n' "./$g" | grep -q -i -E "$INTERDITS_NOMS" && n=$((n + 1)); done; done
[ "$n" = 0 ] && bon "INTERDITS_NOMS (bbis et b-bis compris) ne touche aucun des dix chemins des entrées (cas sain du bloc B3)" || mauvais "INTERDITS_NOMS touche $n chemin(s) des entrées"
P=$(git show "$M:$ICI_REL/prealables-v1.md" | grep '^| P1.4 |')
S=0; k=0; for nom in lecture-cout-t06.json episodes-t06.json manifeste.json mesures-t06.npz textes-actions-t06.jsonl; do
    o=$(printf '%s' "$P" | grep -o -E "${nom//./\\.}\` \(([0-9]{1,3}( [0-9]{3})*) o" | head -1 | grep -o -E '\(([0-9 ]+) o' | tr -dc '0-9')
    [ -n "$o" ] && { S=$((S + o)); k=$((k + 1)); }; done
[ "$k" = 5 ] && [ "$S" = 18959392 ] && grep -q -F '« 10 fichiers ; cinq entrées : 18959392 octets »' "$CMD" \
    && bon "somme des tailles des cinq entrées lue à P1.4 de prealables-v1.md (main distant) : $S octets, égale à l'attendu du bloc B3" || mauvais "somme des tailles ($k tailles lues, $S octets)"
[ "$(h "$ICI_REL/prealables-v1.md")" = 0cd96b629cb181246a8c2b15ad235719d72eaea64650552e0d482b630506c129 ] && bon "prealables-v1.md sur main : empreinte citée par la commande v1 (0cd96b62…)" || mauvais "prealables-v1.md"
'''

COUPLES: list[tuple[str, str, int]] = [
    ("# commande-compte-3-phase-b-v2.md (règle R6", "# commande-compte-3-phase-b-v3.md (règle R6", 1),
    ("# Écrit le 2026-11-16 par le préparateur de la commande (sous-agent de la session mère, même modèle qu'elle).\n",
     "# Écrit le 2026-11-16 par le préparateur du brouillon v2 (modèle B) ; version 3 par le préparateur de la v3 (modèle A), dérivée par\n"
     "# deriver_constantes_phase_b_v3_v1.py : noms v3, et deux contrôles ajoutés (noms interdits contre les chemins des entrées ; somme des\n"
     "# tailles du bloc B3 contre prealables-v1.md, P1.4, sur main distant).\n", 1),
    ("#     bash verification_constantes_phase_b_v2.sh", "#     bash verification_constantes_phase_b_v3.sh", 1),
    ('CMD="${3:-$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-b-v2.md}"', 'CMD="${3:-$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-b-v3.md}"', 1),
    ('case "$(git remote get-url origin)" in', AJOUT + 'case "$(git remote get-url origin)" in', 1),
]


def main(argv: list[str]) -> int:
    src, dst = Path(argv[0]), Path(argv[1])
    if dst.exists():
        print(f"ARRÊT : {dst} existe déjà (R12)")
        return 1
    b = src.read_bytes()
    if hashlib.sha256(b).hexdigest() != H_V2:
        print("ARRÊT : vérification v2 d'une autre empreinte")
        return 1
    t = b.decode("utf-8")
    for ancien, nouveau, n in COUPLES:
        if t.count(ancien) != n:
            print(f"ARRÊT : « {ancien[:70]}… » trouvé {t.count(ancien)} fois ({n} exigée(s)) ; rien n'est écrit")
            return 1
        t = t.replace(ancien, nouveau)
    dst.write_text(t, encoding="utf-8")
    print(f"{len(COUPLES)} couples ; {dst} : {hashlib.sha256(t.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
