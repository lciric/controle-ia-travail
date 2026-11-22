#!/usr/bin/env python3
"""Applique au brouillon N du texte du bras A les opérations rendues par un rédacteur appelé par l'API — version 1.

Usage : appliquer_operations_brouillon_v1.py SOURCE REPONSE TABLE SORTIE RAPPORT [--regles A-B]
  SOURCE  : le brouillon de base (non nettoyé).
  REPONSE : la réponse du rédacteur ; le premier bloc ```json … ``` porte {"operations": [...]}.
  TABLE   : table des marques ⟦Xn⟧ → texte d'origine (extraits_nettoyes_brouillon_v1.py).
  SORTIE  : le brouillon neuf (refus s'il existe : on n'écrase jamais).
  RAPPORT : JSON du contrôle (opérations, lignes touchées, règles inchangées, diff résumé).
  --regles A-B : lignes de SOURCE qui doivent rester égales caractère pour caractère (défaut 529-537).

Chaque opération :
  {"type": "remplacer", "ligne": n, "ancien": s, "nouveau": t}  — s (marques rétablies) figure exactement une fois
      dans la ligne n de SOURCE ; sinon refus ;
  {"type": "inserer_apres", "ligne": n, "texte": t}             — lignes neuves après la ligne n (0 : en tête).
Toute marque inconnue de TABLE restant après rétablissement est un refus. Refus (code 2) : rien n'est écrit.
Les remplacements sont faits d'abord, puis les insertions, de la plus grande ligne à la plus petite.
"""
import difflib, hashlib, json, re, sys
from pathlib import Path

BLOC = re.compile(r"```json\s*\n(.*?)\n```", re.S)
MARQUE = re.compile(r"⟦[A-Z]\d+⟧")


class Refus(Exception):
    pass


def retablir(texte: str, table: dict) -> str:
    def un(m):
        if m.group(0) not in table:
            raise Refus(f"marque inconnue {m.group(0)}")
        return table[m.group(0)]
    t = MARQUE.sub(un, texte)
    if "⟦" in t or "⟧" in t:
        raise Refus("marque mal formée restante")
    return t


def appliquer(source: str, operations: list, table: dict, regles: tuple) -> tuple:
    lignes = source.split("\n")
    n_total = len(lignes)
    remp = [o for o in operations if o.get("type") == "remplacer"]
    ins = [o for o in operations if o.get("type") == "inserer_apres"]
    autres = [o for o in operations if o.get("type") not in ("remplacer", "inserer_apres")]
    if autres:
        raise Refus(f"type d'opération inconnu : {autres[0].get('type')}")
    a, b = regles
    touchees = set()
    for o in remp:
        n = o["ligne"]
        if not (isinstance(n, int) and 1 <= n <= n_total):
            raise Refus(f"ligne hors du brouillon : {n}")
        if a <= n <= b:
            raise Refus(f"remplacement dans une règle gelée, ligne {n}")
        ancien, nouveau = retablir(o["ancien"], table), retablir(o["nouveau"], table)
        if not ancien:
            raise Refus(f"ancien vide, ligne {n}")
        compte = lignes[n - 1].count(ancien)
        if compte != 1:
            raise Refus(f"ligne {n} : « ancien » trouvé {compte} fois")
        lignes[n - 1] = lignes[n - 1].replace(ancien, nouveau, 1)
        touchees.add(n)
    for o in sorted(ins, key=lambda o: o["ligne"], reverse=True):
        n = o["ligne"]
        if not (isinstance(n, int) and 0 <= n <= n_total):
            raise Refus(f"insertion hors du brouillon : {n}")
        if a <= n < b:
            raise Refus(f"insertion au milieu des règles gelées, après la ligne {n}")
        neuves = retablir(o["texte"], table).split("\n")
        lignes[n:n] = neuves
    return "\n".join(lignes), sorted(touchees)


def main(argv):
    src, rep, tab, sortie, rapport = argv[:5]
    regles = (529, 537)
    for x in argv[5:]:
        if x.startswith("--regles="):
            regles = tuple(int(v) for v in x.split("=", 1)[1].split("-"))
    if Path(sortie).exists() or Path(rapport).exists():
        print("refus : la sortie ou le rapport existe déjà", file=sys.stderr); return 2
    source = Path(src).read_text(encoding="utf-8")
    reponse = Path(rep).read_text(encoding="utf-8")
    table = json.loads(Path(tab).read_text(encoding="utf-8"))
    try:
        m = BLOC.search(reponse)
        if not m:
            raise Refus("aucun bloc JSON dans la réponse")
        operations = json.loads(m.group(1))["operations"]
        neuf, touchees = appliquer(source, operations, table, regles)
    except (Refus, KeyError, ValueError, TypeError) as e:
        print(f"refus : {e}", file=sys.stderr); return 2
    av, ap = source.split("\n"), neuf.split("\n")
    regles_avant = av[regles[0] - 1:regles[1]]
    # retrouver les règles dans le neuf, à l'identique et contiguës
    pos = [i for i in range(len(ap) - len(regles_avant) + 1) if ap[i:i + len(regles_avant)] == regles_avant]
    if len(pos) != 1:
        print("refus : les règles gelées ne se retrouvent pas une seule fois, à l'identique", file=sys.stderr); return 2
    sm = difflib.SequenceMatcher(a=av, b=ap, autojunk=False)
    blocs = [(t, i1 + 1, i2, j1 + 1, j2) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal"]
    Path(sortie).write_text(neuf, encoding="utf-8")
    sha = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()
    r = {"source": src, "source_sha256": sha(source), "reponse_sha256": sha(reponse), "sortie": sortie,
         "sortie_sha256": sha(neuf), "operations": len(operations), "lignes_remplacees": touchees,
         "lignes_avant": len(av), "lignes_apres": len(ap),
         "regles": {"avant": list(regles), "apres": [pos[0] + 1, pos[0] + len(regles_avant)],
                    "sha256": sha("\n".join(regles_avant))},
         "differences": [{"type": t, "avant": [a, b], "apres": [c, d]} for t, a, b, c, d in blocs]}
    Path(rapport).write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: r[k] for k in ("operations", "lignes_remplacees", "lignes_avant", "lignes_apres", "regles")},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
