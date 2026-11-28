"""Remplit les marqueurs du brouillon 8 de l'addendum de P3 et écrit le texte final (à verser, puis sceller).

Usage : python3 remplir_texte_final_v1.py NOMBRE_TESTS VERDICT_B7
Chaque empreinte est recalculée sur le fichier qu'elle désigne ; tout marqueur restant arrête.
"""
import hashlib
import pathlib
import re
import sys

A = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3")
V = A / "verification-finale"


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    nombre, verdict_b7 = sys.argv[1], sys.argv[2]
    b8 = A / "P3-addendum-lecture-complementaire-v1-brouillon8.md"
    # Empreintes relues par la contre-lecture 5 (VB7-09) : tout écart arrête avant de remplir.
    relues = {b8: "bde1b2437c0caa24cd6feabe959351e3fb1342973dc2338f01271aa2d5479484",
              A / "final-b4/test_complements_p3_v1.py": "7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3",
              A / "final-b4/complements_p3_v1.py": "2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996"}
    for chemin, attendu in relues.items():
        if sha(chemin) != attendu:
            raise SystemExit(f"ARRÊT : {chemin} ({sha(chemin)}) n'est pas la version relue ({attendu})")
    if nombre != "165":
        raise SystemExit(f"ARRÊT : nombre de tests {nombre} ≠ 165 (en tête du fichier de tests relu)")
    t = b8.read_text(encoding="utf-8")
    valeurs = {
        "EMPREINTE_MODULE": sha(A / "final-b4/complements_p3_v1.py"),
        "EMPREINTE_TESTS": sha(A / "final-b4/test_complements_p3_v1.py"),
        "NOMBRE_TESTS": nombre,
        "EMPREINTE_TRAITEMENT": sha(A / "traitement-R2-addendum-P3-v1.md"),
        "EMPREINTE_VERIFICATION_TEXTE": sha(V / "verification-code-final-addendum-P3-v1-texte.md"),
        "EMPREINTE_VERIFICATION_MUTANTS": sha(V / "verification-code-final-addendum-P3-v1-mutants.md"),
        "EMPREINTE_VERIFICATION_CALCULS": sha(V / "verification-code-final-addendum-P3-v1-calculs.md"),
        "VERDICT_VERIFICATION_TEXTE": "scellable après corrections",
        "VERDICT_VERIFICATION_MUTANTS": "scellable après corrections",
        "VERDICT_VERIFICATION_CALCULS": "scellable après corrections",
        "EMPREINTE_BROUILLON8": sha(b8),
        "EMPREINTE_VERIFICATION_B7": sha(V / "verification-corrections-brouillon7-addendum-P3-v1.md"),
        "VERDICT_VERIFICATION_B7": verdict_b7,
    }
    for cle, valeur in valeurs.items():
        if f"<<{cle}>>" not in t:
            raise SystemExit(f"ARRÊT : marqueur <<{cle}>> absent du brouillon 8")
        t = t.replace(f"<<{cle}>>", valeur)
    restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t)))
    if restes:
        raise SystemExit(f"ARRÊT : marqueurs restants {restes}")
    sortie = A / "P3-addendum-lecture-complementaire-v1-final.md"
    if sortie.exists():
        raise SystemExit(f"ARRÊT : {sortie} existe déjà (R12 : on n'écrase jamais)")
    sortie.write_text(t, encoding="utf-8")
    for cle, valeur in valeurs.items():
        print(f"{cle} = {valeur}")
    print(f"texte final : {sortie} ({sha(sortie)})")


if __name__ == "__main__":
    main()
