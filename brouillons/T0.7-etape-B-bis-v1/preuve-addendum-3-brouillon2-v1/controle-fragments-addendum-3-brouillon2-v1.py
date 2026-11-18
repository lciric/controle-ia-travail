"""Contrôle mécanique du brouillon 2 du troisième addendum de B bis : processeur seulement, aucun réseau, aucune donnée.

Lit le texte scellé T, le premier addendum A1, le second addendum A2, le brouillon 1 et le brouillon 2 du troisième addendum.
Pour chacun des fragments TA-1 à TA-5 du brouillon 2 :
  - l'« ancien » figure une seule fois dans A2, aucune fois dans T, aucune fois dans A1 ;
  - deux « anciens » ne se chevauchent pas ;
  - l'endroit de A2 où il tombe (section « ## », bloc « ### SA-k ») est relevé ; pour un bloc SA, la section de T que ce bloc
    remplace est retrouvée par l'« ancien » du bloc SA dans T+1 (T lu avec EC-1 à EC-8 de A1) ;
  - aucun « ancien » ne tombe dans une section protégée de T (Hypothèse, Prédiction chiffrée, Métrique, Seuil, Plan d'analyse,
    Critères de lecture gelés, Liste d'arrêt) ni ne recouvre un autre bloc SA que SA-8 ;
  - le compte des parenthèses de l'« ancien » et du « nouveau » est le même.
Puis applique les cinq remplacements à A2, vérifie que chaque « nouveau » figure une fois dans le résultat, que les blocs SA autres
que SA-8 (dont SA-5 et SA-15, liste d'arrêt) sont inchangés, et écrit A2 lu avec le troisième addendum (pièce de travail ; si le
fichier existe déjà, il est comparé, jamais réécrit, R12). Compare enfin les fragments au brouillon 1.

Jouer depuis la racine du dépôt : `python <ce fichier>`. Code 0 : conforme ; code 1 : un écart (motif écrit)."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

RACINE = Path.cwd()
ICI = Path(__file__).resolve().parent
T_CHEMIN = RACINE / "prereg/T0.7-etape-B-bis-v1.md"
A1_CHEMIN = RACINE / "prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md"
A2_CHEMIN = RACINE / "prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md"
B1_CHEMIN = RACINE / "brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon1.md"
B2_CHEMIN = RACINE / "brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon2.md"
SORTIE_A2 = ICI / "a2-lu-avec-le-troisieme-addendum-brouillon2-v1.md"
ATTENDU = {
    "T": "0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb",
    "A1": "f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7",
    "A2": "18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26",
    "B1": "0056edaa66b20c2e5b40cfecf7ef9752834ae68c76db9e2cf4c3cc7efe75b58d",
}
PROTEGEES = ("Hypothèse", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse", "Critères de lecture gelés",
             "Liste d'arrêt")
BLOC = re.compile(r"Ancien :\n\n```text\n(.*?)\n```\n\nNouveau, qui fait foi :\n\n```text\n(.*?)\n```", re.S)


def echec(motif: str) -> None:
    print(f"ÉCART : {motif}")
    raise SystemExit(1)


def sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def blocs(texte: str, prefixe: str) -> list[tuple[str, str, str, str]]:
    """(identifiant, titre, ancien, nouveau) pour chaque section « ### <prefixe>-k — … »."""
    sortie = []
    parts = re.split(rf"^### ({prefixe}-\d+) — (.*)$", texte, flags=re.M)
    for i in range(1, len(parts), 3):
        ident, titre, corps = parts[i], parts[i + 1], parts[i + 2]
        m = BLOC.search(corps)
        if not m:
            echec(f"{ident} : blocs « Ancien » et « Nouveau » introuvables")
        sortie.append((ident, titre, m.group(1), m.group(2)))
    return sortie


def entetes(texte: str) -> list[tuple[int, int, str]]:
    """(position, niveau, titre) de chaque titre « ## » ou « ### »."""
    return [(m.start(), len(m.group(1)), m.group(2)) for m in re.finditer(r"^(#{2,3}) (.*)$", texte, flags=re.M)]


def section(texte: str, pos: int, niveau: int) -> str:
    titre = ""
    for p, n, t in entetes(texte):
        if p > pos:
            break
        if n == niveau:
            titre = t
        elif n < niveau:
            titre = ""
    return titre


def etendues_sa(a2: str) -> dict[str, tuple[int, int]]:
    """Étendue [début, fin) de chaque bloc « ### SA-k » de A2 (jusqu'au titre suivant)."""
    h = entetes(a2)
    sortie = {}
    for k, (p, n, t) in enumerate(h):
        m = re.match(r"(SA-\d+) — ", t)
        if n == 3 and m:
            fin = h[k + 1][0] if k + 1 < len(h) else len(a2)
            sortie[m.group(1)] = (p, fin)
    return sortie


def parentheses(s: str) -> int:
    return s.count("(") - s.count(")")


def main() -> int:
    T = T_CHEMIN.read_text(encoding="utf-8")
    A1 = A1_CHEMIN.read_text(encoding="utf-8")
    A2 = A2_CHEMIN.read_text(encoding="utf-8")
    B1 = B1_CHEMIN.read_text(encoding="utf-8")
    B2 = B2_CHEMIN.read_text(encoding="utf-8")
    for nom, texte in (("T", T), ("A1", A1), ("A2", A2), ("B1", B1)):
        e = sha(texte)
        if e != ATTENDU[nom]:
            echec(f"empreinte de {nom} : {e} au lieu de {ATTENDU[nom]}")
        print(f"{nom} : empreinte {e} (attendue)")

    # T+1 : T lu avec EC-1 à EC-8 de A1 (chaque « ancien » unique dans T).
    T1 = T
    for ident, _, ancien, nouveau in blocs(A1, "EC"):
        if T1.count(ancien) != 1:
            echec(f"A1 {ident} : « ancien » trouvé {T1.count(ancien)} fois dans T")
        T1 = T1.replace(ancien, nouveau)
    sa = {ident: (titre, ancien, nouveau) for ident, titre, ancien, nouveau in blocs(A2, "SA")}
    sa_etendue = etendues_sa(A2)
    print(f"A1 : EC lus et appliqués ; A2 : {len(sa)} blocs SA lus")

    ta = blocs(B2, "TA")
    if [i for i, *_ in ta] != [f"TA-{k}" for k in range(1, 6)]:
        echec(f"fragments du brouillon 2 : {[i for i, *_ in ta]} au lieu de TA-1 à TA-5")
    etendues = []
    for ident, titre, ancien, nouveau in ta:
        n_a2, n_t, n_a1 = A2.count(ancien), T.count(ancien), A1.count(ancien)
        if (n_a2, n_t, n_a1) != (1, 0, 0):
            echec(f"{ident} : ancien trouvé {n_a2} fois dans A2, {n_t} dans T, {n_a1} dans A1 (attendu 1, 0, 0)")
        debut = A2.index(ancien)
        fin = debut + len(ancien)
        ligne_debut = A2.count("\n", 0, debut) + 1
        ligne_fin = A2.count("\n", 0, fin) + 1
        sec2 = section(A2, debut, 2)
        sec3 = section(A2, debut, 3)
        dans_sa = [k for k, (p, q) in sa_etendue.items() if debut < q and p < fin]
        cible_t = ""
        if dans_sa:
            if dans_sa != ["SA-8"]:
                echec(f"{ident} : recouvre les blocs {dans_sa} (seul SA-8 permis)")
            _, ancien_sa, nouveau_sa = sa["SA-8"]
            if ancien not in nouveau_sa:
                echec(f"{ident} : dans le bloc SA-8 mais hors de son « nouveau »")
            if T1.count(ancien_sa) != 1:
                echec(f"SA-8 : « ancien » trouvé {T1.count(ancien_sa)} fois dans T+1")
            cible_t = section(T1, T1.index(ancien_sa), 2)
            if any(cible_t.startswith(p) for p in PROTEGEES):
                echec(f"{ident} : SA-8 porte sur la section protégée « {cible_t} » de T")
        else:
            if not (sec2.startswith("5. ") or sec2.startswith("7. ")):
                echec(f"{ident} : dans la section « {sec2} » de A2 (attendu § 5 ou § 7)")
        if parentheses(ancien) != parentheses(nouveau):
            echec(f"{ident} : parenthèses {parentheses(ancien)} dans l'ancien, {parentheses(nouveau)} dans le nouveau")
        etendues.append((debut, fin, ident))
        lieu = f"bloc « {sec3} », « nouveau » de SA-8, section de T « {cible_t} »" if dans_sa else f"section « {sec2} »"
        print(f"{ident} ({titre}) : ancien 1 fois dans A2, 0 dans T, 0 dans A1 ; A2 l. {ligne_debut}-{ligne_fin}, {lieu} ; "
              f"parenthèses égales ({parentheses(ancien):+d}) ; ancien {len(ancien)} → nouveau {len(nouveau)} caractères ; "
              f"ancien {sha(ancien)[:16]}, nouveau {sha(nouveau)[:16]}")
    etendues.sort()
    for (d1, f1, i1), (d2, f2, i2) in zip(etendues, etendues[1:]):
        if d2 < f1:
            echec(f"{i1} et {i2} se chevauchent dans A2")
    print("aucun chevauchement entre les cinq anciens")

    A2lu = A2
    for ident, _, ancien, nouveau in ta:
        A2lu = A2lu.replace(ancien, nouveau)
    for ident, _, ancien, nouveau in ta:
        if A2lu.count(nouveau) != 1:
            echec(f"{ident} : « nouveau » trouvé {A2lu.count(nouveau)} fois dans A2 lu avec le troisième addendum")
    sa_lu = {ident: (t, a, n) for ident, t, a, n in blocs(A2lu, "SA")}
    changes = sorted(k for k in sa if sa[k] != sa_lu.get(k))
    if changes != ["SA-8"]:
        echec(f"blocs SA changés : {changes} (seul SA-8 attendu)")
    for k in ("SA-4", "SA-5", "SA-15", "SA-19"):
        if sa[k] != sa_lu[k]:
            echec(f"bloc {k} (liste d'arrêt) changé")
    for phrase in ("sous ce texte et ses deux addenda", "sous le second addendum"):
        if A2.count(phrase) != 1 or A2lu.count(phrase) != 1:
            echec(f"phrase de la liste d'arrêt « {phrase} » : {A2.count(phrase)} fois dans A2, {A2lu.count(phrase)} après")
    print("blocs SA inchangés hors SA-8 (dont SA-4, SA-5, SA-15, SA-19 de la liste d'arrêt) ; "
          "« sous ce texte et ses deux addenda » et « sous le second addendum » : une fois avant, une fois après")
    for mot in ("même entropie", "reprise telle quelle", "liste le code v4"):
        print(f"« {mot} » : {A2.count(mot)} fois dans A2, {A2lu.count(mot)} fois après les cinq remplacements")
        if A2lu.count(mot) != 0:
            echec(f"« {mot} » reste dans A2 lu avec le troisième addendum")

    contenu = ("<!-- A2 lu avec TA-1 à TA-5 du brouillon 2 du troisième addendum, produit par "
               "controle-fragments-addendum-3-brouillon2-v1.py ; pièce de travail, ne fait pas foi. -->\n" + A2lu)
    if SORTIE_A2.exists():
        if SORTIE_A2.read_text(encoding="utf-8") != contenu:
            echec(f"{SORTIE_A2.name} existe et diffère (R12 : jamais réécrit)")
        print(f"{SORTIE_A2.name} : existe, identique")
    else:
        SORTIE_A2.write_text(contenu, encoding="utf-8")
        print(f"{SORTIE_A2.name} : écrit")
    print(f"{SORTIE_A2.name} : empreinte {sha(contenu)}")

    ta1 = {i: (a, n) for i, _, a, n in blocs(B1, "TA")}
    for ident, _, ancien, nouveau in ta:
        a1, n1 = ta1[ident]
        print(f"{ident} par rapport au brouillon 1 : ancien {'inchangé' if a1 == ancien else 'étendu' if a1 in ancien else 'changé'}"
              f", nouveau {'inchangé' if n1 == nouveau else 'changé'}")
    print("CONFORME")
    return 0


if __name__ == "__main__":
    sys.exit(main())
