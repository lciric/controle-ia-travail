"""Vérifie, à l'octet, que la ligne de commande du lanceur v3 est celle du complément 1 v3, hors des trois chemins — v3.

Usage : verifier-commande-v3.py COMPLEMENT LANCEUR
Rend 0 si égal, 1 sinon (2 : usage) ; écrit ce qu'il compare.

Méthode (aucune valeur codée ici : les trois chemins sont lus dans le complément) :
  1. une seule ligne commençant par « env -C » de chaque côté ;
  2. dans le complément, la ligne se coupe sur les espaces en 11 mots : env, -C, CODE, PYTHONPATH=src, INTERPRETE, -B,
     PROGRAMME, PREENREGISTREMENT, RACINE, ORCHESTRATEUR, SORTIES ; RACINE est le 9e, INTERPRETE le 5e, SORTIES le 11e ;
     CODE, PROGRAMME, PREENREGISTREMENT et ORCHESTRATEUR doivent commencer par RACINE + « / » ;
  3. ligne attendue du lanceur : la même, où INTERPRETE devient "$INTERPRETE", SORTIES "$SORTIES", RACINE "$RACINE", et le
     préfixe RACINE des quatre chemins sous la racine "$RACINE" (le reste de chaque chemin gardé à l'octet) ;
  4. égalité à l'octet de la ligne du lanceur avec la ligne attendue ; et, en garde contre un chemin resté codé, aucune des
     trois valeurs du complément (RACINE, INTERPRETE, SORTIES) n'apparaît telle quelle dans la ligne du lanceur.
Ce que le vérificateur ne voit pas : la valeur que prennent "$RACINE", "$INTERPRETE" et "$SORTIES" à l'exécution (essai
dynamique à part : argv enregistré par un interpréteur factice).
"""
import hashlib
import sys

ATTENDUS_MOTS = 11


def lignes_de_commande(octets):
    return [l for l in octets.split(b"\n") if l.startswith(b"env -C ")]


def ligne_attendue(c):
    """(ligne attendue du lanceur, (racine, interprète, sorties)) ou (None, raison)."""
    mots = c.split(b" ")
    if len(mots) != ATTENDUS_MOTS:
        return None, f"complément : {len(mots)} mots, {ATTENDUS_MOTS} attendus"
    if mots[0] != b"env" or mots[1] != b"-C" or mots[3] != b"PYTHONPATH=src" or mots[5] != b"-B":
        return None, "complément : mots fixes inattendus (env, -C, PYTHONPATH=src, -B)"
    racine, interprete, sorties = mots[8], mots[4], mots[10]
    sous = [2, 6, 7, 9]
    for i in sous:
        if not mots[i].startswith(racine + b"/"):
            return None, f"complément : le mot {i + 1} ne commence pas par la racine"
    nouveaux = list(mots)
    nouveaux[4] = b'"$INTERPRETE"'
    nouveaux[8] = b'"$RACINE"'
    nouveaux[10] = b'"$SORTIES"'
    for i in sous:
        nouveaux[i] = b'"$RACINE"' + mots[i][len(racine):]
    return b" ".join(nouveaux), (racine, interprete, sorties)


def main(args):
    if len(args) != 2:
        print(__doc__)
        return 2
    complement, lanceur = args
    with open(complement, "rb") as fh:
        oc = fh.read()
    with open(lanceur, "rb") as fh:
        ol = fh.read()
    print("complément sha256 :", hashlib.sha256(oc).hexdigest())
    print("lanceur sha256    :", hashlib.sha256(ol).hexdigest())
    lc, ll = lignes_de_commande(oc), lignes_de_commande(ol)
    print("lignes « env -C » : complément", len(lc), "; lanceur", len(ll))
    if len(lc) != 1 or len(ll) != 1:
        print("ÉCHEC : une seule ligne de commande attendue de chaque côté")
        return 1
    c, l = lc[0], ll[0]
    attendue, info = ligne_attendue(c)
    if attendue is None:
        print("ÉCHEC :", info)
        return 1
    racine, interprete, sorties = info
    print("chemins lus dans le complément : racine", racine.decode(errors="replace"), "; interpréteur",
          interprete.decode(errors="replace"), "; sorties", sorties.decode(errors="replace"))
    print("ligne du complément : ", len(c), "octets, sha256", hashlib.sha256(c).hexdigest())
    print("ligne attendue      : ", len(attendue), "octets, sha256", hashlib.sha256(attendue).hexdigest())
    print("ligne du lanceur    : ", len(l), "octets, sha256", hashlib.sha256(l).hexdigest())
    egal = l == attendue
    restes = [v.decode(errors="replace") for v in (racine, interprete, sorties) if v in l]
    if not egal:
        n = next((i for i in range(min(len(l), len(attendue))) if l[i] != attendue[i]), min(len(l), len(attendue)))
        print(f"première différence à l'octet {n} : lanceur « {l[max(0, n - 30):n + 30].decode(errors='replace')} » ; "
              f"attendu « {attendue[max(0, n - 30):n + 30].decode(errors='replace')} »")
    if restes:
        print("chemins du complément restés codés dans la ligne du lanceur :", restes)
    ok = egal and not restes
    print("ÉGAL à l'octet hors des trois chemins" if ok else "ÉCHEC : différence")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
