"""Comparateur des échecs d'essais attendus — v1 (fichier neuf, R12 ; décision de routine R-3686).

Lit une ou plusieurs sorties de pytest (lancé avec `-rf`, ou `-ra`/`-rA`, pour que le résumé court liste chaque échec
par une ligne `FAILED <identifiant>` ou `ERROR <identifiant>`) et la liste des échecs attendus d'une note d'écart (par
exemple `docs/notes/essais-dates-t06-v1/echecs-attendus-dates-v1.md`), puis rend :

- code 0 : les échecs vus sont exactement ceux de la liste, ou un sous-ensemble ; les attendus non vus en échec sont
  nommés (ils passent désormais, ou leur fichier n'a pas été joué) ;
- code 1 : au moins un échec neuf (absent de la liste) ; chacun est nommé ;
- code 2 : entrée illisible, jamais un repli silencieux (R5) : note sans marqueurs, liste vide ou en double, sortie
  sans ligne de bilan de pytest, ou bilan qui compte plus d'échecs que de lignes `FAILED`/`ERROR` (sortie lancée sans
  `-rf`, ou tronquée).

La liste de la note est lue entre les deux marqueurs `<!-- debut-liste-echecs-attendus -->` et
`<!-- fin-liste-echecs-attendus -->` : une ligne par identifiant d'essai (`tests/…py::…`), lignes vides, clôtures de bloc
(```) et commentaires (#) ignorés. Les identifiants sont comparés après décodage des échappements que pytest écrit dans
les identifiants paramétrés (`\\xe9` pour « é », `\\u2260` pour « ≠ »).

    python scripts/comparer_echecs_attendus_v1.py NOTE.md SORTIE_PYTEST.txt [SORTIE_PYTEST.txt ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEBUT = "<!-- debut-liste-echecs-attendus -->"
FIN = "<!-- fin-liste-echecs-attendus -->"
_ECHAPPEMENT = re.compile(r"\\(x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4}|U[0-9a-fA-F]{8})")
_LIGNE_ECHEC = re.compile(r"^(FAILED|ERROR) (\S.*)$")
_BILAN = re.compile(r"(\d+ (passed|failed|errors?|skipped|xfailed|xpassed|deselected)\b.*|no tests ran) in \d+(\.\d+)?s\b")


class EntreeIllisible(Exception):
    pass


def normaliser(identifiant: str) -> str:
    """Décode les échappements `\\xNN`, `\\uNNNN`, `\\UNNNNNNNN` que pytest écrit dans les identifiants ; rien d'autre."""
    return _ECHAPPEMENT.sub(lambda m: chr(int(m.group(1)[1:], 16)), identifiant.strip())


def lire_attendus(texte_note: str) -> list[str]:
    if texte_note.count(DEBUT) != 1 or texte_note.count(FIN) != 1:
        raise EntreeIllisible("note : un marqueur de début et un marqueur de fin de liste exactement attendus")
    if texte_note.index(FIN) < texte_note.index(DEBUT):
        raise EntreeIllisible("note : marqueur de fin avant le marqueur de début")
    bloc = texte_note.split(DEBUT, 1)[1].split(FIN, 1)[0]
    attendus = []
    for ligne in bloc.splitlines():
        s = ligne.strip()
        if not s or s.startswith("```") or s.startswith("#"):
            continue
        if not re.fullmatch(r"tests/\S+\.py::\S.*", s):
            raise EntreeIllisible(f"note : ligne de liste illisible {s!r} (identifiant `tests/…py::…` attendu)")
        attendus.append(normaliser(s))
    if not attendus:
        raise EntreeIllisible("note : liste des échecs attendus vide")
    doublons = sorted({a for a in attendus if attendus.count(a) > 1})
    if doublons:
        raise EntreeIllisible(f"note : identifiants en double {doublons}")
    return attendus


def _identifiant(reste: str) -> str:
    """Coupe « <identifiant> - <message> » au premier « - » hors des crochets du paramétrage."""
    profondeur = 0
    for i, c in enumerate(reste):
        if c == "[":
            profondeur += 1
        elif c == "]":
            profondeur = max(0, profondeur - 1)
        elif profondeur == 0 and reste.startswith(" - ", i):
            return reste[:i]
    return reste


def lire_echecs(texte_sortie: str, nom: str = "sortie") -> list[str]:
    lignes = texte_sortie.splitlines()
    bilans = [l for l in lignes if _BILAN.search(l)]
    if not bilans:
        raise EntreeIllisible(f"{nom} : aucune ligne de bilan de pytest (« N passed … in Xs ») : sortie tronquée ou absente")
    bilan = bilans[-1]
    comptes = sum(int(n) for n in re.findall(r"(\d+) failed\b", bilan)) + sum(int(n) for n in re.findall(r"(\d+) errors?\b", bilan))
    echecs = []
    for l in lignes:
        m = _LIGNE_ECHEC.match(l)
        if m:
            echecs.append(normaliser(_identifiant(m.group(2))))
    uniques = sorted(set(echecs))
    if comptes > len(uniques):
        raise EntreeIllisible(f"{nom} : le bilan compte {comptes} échec(s) mais {len(uniques)} ligne(s) FAILED/ERROR : "
                              "relancer pytest avec -rf (résumé court des échecs)")
    return uniques


def comparer(attendus: list[str], echecs: list[str]) -> dict:
    a, e = set(attendus), set(echecs)
    return {"neufs": sorted(e - a), "attendus_vus": sorted(e & a), "attendus_non_vus": sorted(a - e)}


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__.strip().splitlines()[-1].strip(), file=sys.stderr)
        return 2
    try:
        note = Path(argv[0])
        attendus = lire_attendus(note.read_text(encoding="utf-8"))
        echecs: set[str] = set()
        for s in argv[1:]:
            echecs.update(lire_echecs(Path(s).read_text(encoding="utf-8"), s))
    except (EntreeIllisible, OSError, UnicodeDecodeError) as exc:
        print(f"ILLISIBLE : {exc}")
        return 2
    r = comparer(attendus, sorted(echecs))
    print(f"attendus : {len(attendus)} ; échecs vus : {len(echecs)} ; attendus vus en échec : {len(r['attendus_vus'])} ; "
          f"attendus non vus en échec : {len(r['attendus_non_vus'])} ; échecs neufs : {len(r['neufs'])}")
    for i in r["attendus_non_vus"]:
        print(f"ATTENDU NON VU EN ÉCHEC (passe désormais, ou fichier non joué) : {i}")
    for i in r["neufs"]:
        print(f"ÉCHEC NEUF : {i}")
    if r["neufs"]:
        print(f"NON CONFORME : {len(r['neufs'])} échec(s) hors de la liste de {note}")
        return 1
    print(f"CONFORME : échecs vus inclus dans la liste de {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
