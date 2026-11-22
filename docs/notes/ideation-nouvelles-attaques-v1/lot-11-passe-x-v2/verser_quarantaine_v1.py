"""Versement de la quarantaine de la passe X — v1. Ne lit aucun contenu : il compte les noms de fichiers de `flux/`,
et dès qu'un compagnon `.sha256` neuf apparaît (la tentative est close), il committe et pousse `flux/` sur la branche
orpheline de l'arbre donné. Il s'arrête quand le fichier d'arrêt existe et que tout est versé. Aucune sortie de texte
de réponse : seuls des noms de fichiers et des empreintes de commit sont affichés.

    python3 -B verser_quarantaine_v1.py --arbre ARBRE --arret FICHIER_D_ARRET
"""
import argparse, os, subprocess, sys, time

BRANCHE = "prep/quarantaine-passe-x-reponses-v1"


def git(arbre, *a):
    return subprocess.run(["git", "-C", arbre, *a], capture_output=True, text=True)


def pousser(arbre):
    for essai in range(5):
        if git(arbre, "push", "-q", "origin", BRANCHE).returncode == 0:
            return True
        time.sleep(2 ** (essai + 1))
    return False


def verser(arbre):
    flux = os.path.join(arbre, "flux")
    if not os.path.isdir(flux):
        return 0
    git(arbre, "add", "flux")
    if git(arbre, "diff", "--cached", "--quiet").returncode == 0:
        return 0
    n = len([x for x in os.listdir(flux) if x.endswith(".sha256")])
    r = git(arbre, "commit", "-q", "-m", f"Quarantaine de la passe X : {n} tentatives closes, versées sans lecture")
    if r.returncode != 0:
        print("ÉCHEC du commit", file=sys.stderr)
        return 2
    ok = pousser(arbre)
    print(time.strftime("%H:%M:%SZ", time.gmtime()), n, "tentatives closes ;",
          git(arbre, "rev-parse", "--short", "HEAD").stdout.strip(), "poussé" if ok else "POUSSÉE EN ÉCHEC", flush=True)
    return 0 if ok else 2


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--arbre", required=True)
    a.add_argument("--arret", required=True)
    a.add_argument("--pas", type=int, default=20)
    o = a.parse_args()
    if git(o.arbre, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip() != BRANCHE:
        sys.exit("REFUS : l'arbre n'est pas sur la branche de quarantaine")
    vus = -1
    while True:
        flux = os.path.join(o.arbre, "flux")
        n = len([x for x in os.listdir(flux) if x.endswith(".sha256")]) if os.path.isdir(flux) else 0
        if n != vus:
            verser(o.arbre)
            vus = n
        if os.path.exists(o.arret):
            sys.exit(verser(o.arbre))
        time.sleep(o.pas)


if __name__ == "__main__":
    main()
