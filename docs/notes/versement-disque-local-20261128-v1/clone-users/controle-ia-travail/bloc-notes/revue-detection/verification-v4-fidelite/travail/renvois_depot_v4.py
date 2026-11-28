"""Renvois au dépôt ajoutés ou touchés par la v4 : fragment présent à la ligne citée, dans la version épinglée par la v4
et dans la version du dépôt au moment de la v4 (commit 43cd3ac, 18:28 UTC). Lecture seule : `git show`, aucun écrit.
Usage : python3 -I -B renvois_depot_v4.py"""
import hashlib
import subprocess
import sys

R = "/home/user/controle-ia-travail"


def version(chemin, commit=None):
    if commit is None:
        b = open(f"{R}/{chemin}", "rb").read()
    else:
        b = subprocess.run(["git", "-C", R, "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout
    return hashlib.sha256(b).hexdigest(), b.decode("utf-8").splitlines()


def ligne(lignes, n, frag):
    return frag in lignes[n - 1] if 0 < n <= len(lignes) else False


def ou(lignes, frag):
    return [i + 1 for i, l in enumerate(lignes) if frag in l]


def main():
    ecarts = 0
    # [P] : épinglé d975e981… par la v3 et la v4
    h, P = version("prereg/P3-premier-test-i-a-v1.md")
    print(f"[P] actuel {h}")
    if not h.startswith("d975e981"):
        sys.exit("ARRÊT : [P] en écart")
    for n, frag, quoi in [
        (329, "**honnête** : l'environnement (a) sans rien d'autre", "l. 328-332 : l'honnête n'a pas de consigne"),
        (330, "consigne privée ajoutée à la fin du message système", "l. 328-332 : consigne privée du saboteur"),
        (331, "(p = 1, intensité forte", "condition (i-a), p = 1, intensité forte (E2, T0.6)"),
        (238, "étiquettes des actions du saboteur", "l. 238-241 : T1 sous la même consigne"),
        (293, "recette de 2502.03407", "l. 293-296 : recette « Pairs » d'Apollo"),
        (142, "sonde qui lit la grandeur du nombre écrit passerait T1 et T2", "l. 141-142"),
        (242, "**T2** : sur les actions de saboteur contre honnête", "l. 242"),
        (273, "jamais « ne sépare pas »", "l. 272-274 (règle gelée)"),
        (125, "(titre en minuscules)", "l. 125"),
        (333, "(titre tout en minuscules)", "l. 333"),
        (428, "pas de seconde lecture sur d'autres sondes, couches ou jeux", "l. 428"),
        (415, "une grandeur non écrite ici, est un **nœud**", "l. 415-416"),
    ]:
        ok = ligne(P, n, frag)
        ecarts += not ok
        print(f"  [{'OK' if ok else 'ÉCART'}] [P] l. {n} {quoi} : {frag!r}")
    # N-026
    h, N = version("docs/decisions/decision-N-026-v1.md")
    print(f"N-026 actuel {h}")
    for n, frag in [(18, "est **permis** dans un"), (19, "préenregistrement d'audit ou d'expérience")]:
        ok = ligne(N, n, frag)
        ecarts += not ok
        print(f"  [{'OK' if ok else 'ÉCART'}] N-026 l. {n} : {frag!r}")
    nb = sum("bonferroni" in l.lower() for l in N)
    print(f"  [{'OK' if nb == 0 else 'ÉCART'}] N-026 : « Bonferroni » absent ({nb} occurrence(s))")
    # registres : version épinglée (8bd4a75, 11:55 UTC) contre version de la v4 (43cd3ac, 18:28 UTC) et version actuelle
    for chemin, cites in [
        ("registres/go.md", [(32, "GO-2026-10-20-05"), (33, "GO-2026-10-20-06"), (34, "GO-2026-10-20-07"), (35, "GO-2026-10-20-08")]),
        ("registres/decisions.md", [(446, "| N-025 |"), (453, "| R-262 |"), (456, "| N-028 |"), (457, "| R-265 |"),
                                    (461, "| R-269 |"), (468, "| N-029 |"), (469, "| R-276 |")]),
    ]:
        for etiquette, commit in [("épinglée (8bd4a75, 11:55)", "8bd4a75"), ("de la v4 (43cd3ac, 18:28)", "43cd3ac"),
                                  ("actuelle", None)]:
            h, L = version(chemin, commit)
            res = []
            for n, frag in cites:
                res.append(f"l. {n} {'oui' if ligne(L, n, frag) else 'non'} (vraie : {ou(L, frag)})")
            print(f"{chemin} {etiquette} {h[:16]}… : " + " ; ".join(res))
            if commit == "8bd4a75":
                ecarts += sum(not ligne(L, n, f) for n, f in cites)
    # R-283 et P-015 : où et dans quelles versions
    for commit in ["8bd4a75", "43cd3ac", None]:
        h, L = version("registres/decisions.md", commit)
        print(f"decisions.md {commit or 'actuelle'} {h[:16]}… : P-015 l. {ou(L, '| P-015 |')} ; R-283 l. {ou(L, '| R-283 |')}")
    h, L = version("registres/decisions.md", "43cd3ac")
    p015 = L[ou(L, "| P-015 |")[0] - 1]
    print("  P-015 (43cd3ac) contient « USD » :", "USD" in p015, "; « épisodes » :", "épisodes" in p015,
          "; « Recommandation (b) » :", "Recommandation (b)" in p015)
    r283 = L[ou(L, "| R-283 |")[0] - 1]
    print("  R-283 (43cd3ac) contient « se recharge automatiquement » :", "se recharge automatiquement" in r283)
    print(f"écarts sur les renvois tels qu'épinglés : {ecarts}")


if __name__ == "__main__":
    main()
