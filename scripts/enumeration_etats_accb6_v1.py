#!/usr/bin/env python3
"""Énumération des états et des phrases du barreau 6 (`ACCB6`) — v1.

Texte : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon2.md` (sha256 `9f070e31734be21d753967e0df11ee2aae174906d170a36f27a45c52714494c3`),
sections « Seuil » (états des couples et des jeux, multiplicité) et « Critères de lecture gelés » (phrase de (i), table « Phrase du
barreau 6 ») ; section « Code neuf » : « énumération de tous les états de couples et de jeux (exactement un état par cas, aucun
trou) et de la séquence fixée, et des phrases gelées : une phrase et une seule par combinaison d'aiguillage (G-1 à G-4), d'état de
(i), d'état de `S100` et de dose d'arrêt de la séquence ».

Méthode : chaque règle du texte est **transcrite ici une seconde fois**, indépendamment du module (`TRANSCRIPTION_*`), en liste de
conditions dans l'ordre du texte ; pour chaque cas, toutes les règles vraies sont relevées, la première donne l'état (ou la ligne de
la table), et elle est comparée à la fonction du module (`etats_v1.etat_couple`, `etats_v1.etat_jeu`, `etats_v1.sequence_fixee`,
`phrases_v1.ligne_de_la_table`, `phrases_v1.phrase_gelee`). Une ligne par cas ; tout cas sans état, sans phrase, ou en écart avec le
module arrête le script (code 1). Les crochets des phrases sont remplis de marques symboliques (`phrases_v1.remplissage_symbolique`).
Aucune donnée n'est lue ; sortie déterministe (aucune heure).

Lancement : `python3 -I -B scripts/enumeration_etats_accb6_v1.py SORTIE.txt` (le module est importé depuis `src/` de l'arbre qui porte
ce script ; son chemin et son empreinte sont écrits en tête de la sortie).
"""
from __future__ import annotations

import hashlib
import sys
from itertools import combinations_with_replacement, product
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from controle_ia.accumulation_b6 import etats_v1 as et  # noqa: E402
from controle_ia.accumulation_b6 import phrases_v1 as ph  # noqa: E402

TEXTE = ("brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon2.md",
         "9f070e31734be21d753967e0df11ee2aae174906d170a36f27a45c52714494c3")

# ------------------------------------------------------------------------------------- transcription indépendante des règles
TRANSCRIPTION_COUPLE = (                     # « Seuil », état d'un couple : (règle, condition, état rendu)
    ("1 E", lambda e: e["echec"], lambda e: "E"),
    ("2 F", lambda e: e["fuite"] == "nommée", lambda e: "F"),
    ("3 P", lambda e: not e["dessus_somme"] and not e["dessus_max"], lambda e: "P"),
    ("4 S", lambda e: e["sature_somme"] and e["sature_max"], lambda e: "S"),
    ("5 A/N", lambda e: e["delta"] == "bas>0" and e["dessus_somme"], lambda e: "N" if e["trivial_somme"] else "A"),
    ("6 M/N", lambda e: e["delta"] == "haut<0" and e["dessus_max"], lambda e: "N" if e["trivial_max"] else "M"),
    ("7 Z", lambda e: True, lambda e: "Z"),
)
TRANSCRIPTION_JEU = (                        # « Seuil », état d'un jeu
    ("(0)", lambda c, f: f, "non tranché : fuite nommée"),
    ("(1)", lambda c, f: "A" in c and "M" in c, "partagé"),
    ("(2)", lambda c, f: "A" in c, "accumuler bat"),
    ("(3)", lambda c, f: "M" in c, "le maximum bat"),
    ("(4)", lambda c, f: "N" in c, "non interprétable"),
    ("(5)", lambda c, f: all(x == "E" for x in c), "échec"),
    ("(6)", lambda c, f: all(x in ("P", "E") for x in c), "sous le plancher"),
    ("(7)", lambda c, f: all(x in ("S", "P", "E") for x in c), "saturé"),
    ("(8)", lambda c, f: True, "non départagé à cette puissance"),
)
DOSES = ("S100", "S75", "S50", "S25")        # « Multiplicité » : ordre fixé
TRANSCRIPTION_TABLE = (                      # « Phrase du barreau 6 » : (ligne, condition) ; les lignes après G-3 valent sous G-4
    ("G-1", lambda g, i, s: g == "G-1"),
    ("G-2", lambda g, i, s: g == "G-2"),
    ("G-3", lambda g, i, s: g == "G-3"),
    ("(ii) : S100 « accumuler bat »", lambda g, i, s: g == "G-4" and s == "accumuler bat"),
    ("(ii) : S100 « le maximum bat »", lambda g, i, s: g == "G-4" and s == "le maximum bat"),
    ("(ii) : S100 ni A ni M ; (i) « accumuler bat »",
     lambda g, i, s: g == "G-4" and s not in ("accumuler bat", "le maximum bat") and i == "accumuler bat"),
    ("(ii) : S100 ni A ni M ; (i) « le maximum bat »",
     lambda g, i, s: g == "G-4" and s not in ("accumuler bat", "le maximum bat") and i == "le maximum bat"),
    ("ni (i) ni S100 en A ou en M",
     lambda g, i, s: g == "G-4" and i not in ("accumuler bat", "le maximum bat") and s not in ("accumuler bat", "le maximum bat")),
)
ETATS_JEU_TEXTE = tuple(x[2] for x in TRANSCRIPTION_JEU)


class Ecart(Exception):
    pass


def premier(regles, *args):
    vraies = [r for r in regles if r[1](*args)]
    if not vraies:
        raise Ecart(f"aucune règle vraie (trou) pour {args}")
    return vraies


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(sortie: Path) -> int:
    lignes = []
    out = lignes.append
    out("# Énumération des états et des phrases du barreau 6 (ACCB6) — v1")
    out(f"texte : {TEXTE[0]} ({TEXTE[1]})")
    for m in (et, ph):
        p = Path(m.__file__).resolve()
        out(f"module : src/controle_ia/accumulation_b6/{p.name} ({sha(p)})")
    if tuple(et.ETATS_JEU) != ETATS_JEU_TEXTE:
        raise Ecart(f"états de jeu du module {et.ETATS_JEU} ≠ transcription {ETATS_JEU_TEXTE}")
    if tuple(et.ORDRE_DOSES) != DOSES:
        raise Ecart(f"ordre des doses du module {et.ORDRE_DOSES} ≠ {DOSES}")

    # 1. couples
    out("")
    out("## 1. États des couples (jeu, sonde) — règles 1 à 7 de « Seuil », la première qui s'applique")
    out("entrées : E = échec (une des quatre causes de la règle 1) ; F = fuite (nommée, aucune, sans objet) ; Σ↑, max↑ = borne basse "
        "de l'aire d'épisode au-dessus du quantile 0,95 de son plancher ; Σs, maxs = aire d'épisode ≥ 0,99 ; Δ = borne basse > 0, "
        "borne haute < 0, ou ni l'un ni l'autre ; Σt, maxt = un prédicteur trivial sépare au moins autant que S_Σ, que S_max")
    n, comptes = 0, {}
    for (echec, fuite, ds, dm, ss, sm, delta, ts, tm) in product((False, True), ("aucune", "nommée", "sans objet"), (False, True),
                                                                 (False, True), (False, True), (False, True),
                                                                 ("ni", "bas>0", "haut<0"), (False, True), (False, True)):
        e = {"echec": echec, "fuite": fuite, "dessus_somme": ds, "dessus_max": dm, "sature_somme": ss, "sature_max": sm,
             "delta": delta, "trivial_somme": ts, "trivial_max": tm}
        vraies = premier(TRANSCRIPTION_COUPLE, e)
        attendu = vraies[0][2](e)
        module = et.etat_couple(et.EntreesCouple(echec=echec, fuite=fuite, dessus_somme=ds, dessus_max=dm, sature_somme=ss,
                                                 sature_max=sm, bas_delta_positif=delta == "bas>0",
                                                 haut_delta_negatif=delta == "haut<0", trivial_somme=ts, trivial_max=tm))
        if module != attendu:
            raise Ecart(f"couple {e} : module {module} ≠ transcription {attendu}")
        n += 1
        comptes[attendu] = comptes.get(attendu, 0) + 1
        b = lambda x: "1" if x else "0"
        out(f"C{n:04d} | E={b(echec)} F={fuite:<10} Σ↑={b(ds)} max↑={b(dm)} Σs={b(ss)} maxs={b(sm)} Δ={delta:<6} Σt={b(ts)} "
            f"maxt={b(tm)} | règles vraies : {', '.join(r[0] for r in vraies)} | état : {attendu} ({et.NOMS_COUPLE[attendu]})")
    out(f"bilan des couples : {n} cas ; cas sans état : 0 ; écarts module / transcription : 0 ; par état : "
        + ", ".join(f"{k} {comptes.get(k, 0)}" for k in et.ETATS_COUPLE))
    if set(comptes) != set(et.ETATS_COUPLE):
        raise Ecart(f"états de couple jamais atteints : {set(et.ETATS_COUPLE) - set(comptes)}")

    # 2. jeux
    out("")
    out("## 2. États des jeux — règles (0) à (8) de « Seuil », sur 1 à 4 sondes (k = 2 à 4 sondes lues ; 1 à 3 pour les familles "
        "de B6-D6) ; fuite nommée : chaque couple est E ou F (règle 2 des couples) ; sans fuite : jamais F")
    n2, comptes2 = 0, {}
    for k in (1, 2, 3, 4):
        for fuite, alphabet in ((False, ("E", "P", "S", "A", "M", "N", "Z")), (True, ("E", "F"))):
            for couples in combinations_with_replacement(alphabet, k):
                vraies = premier(TRANSCRIPTION_JEU, couples, fuite)
                attendu = vraies[0][2]
                module = et.etat_jeu(list(couples), fuite)
                if module != attendu:
                    raise Ecart(f"jeu {couples} (fuite {fuite}) : module {module} ≠ transcription {attendu}")
                n2 += 1
                comptes2[attendu] = comptes2.get(attendu, 0) + 1
                out(f"J{n2:04d} | k={k} | fuite nommée={'oui' if fuite else 'non'} | couples={','.join(couples)} | règles vraies : "
                    f"{', '.join(r[0] for r in vraies)} | état : {attendu}")
    out(f"bilan des jeux : {n2} cas ; cas sans état : 0 ; écarts module / transcription : 0 ; par état : "
        + ", ".join(f"{k} : {comptes2.get(k, 0)}" for k in ETATS_JEU_TEXTE))
    if set(comptes2) != set(ETATS_JEU_TEXTE):
        raise Ecart("états de jeu jamais atteints")

    # 3. séquence fixée
    out("")
    out("## 3. Séquence fixée de (ii) — `S100`, puis `S75`, `S50`, `S25` tant que la dose précédente est « accumuler bat » ; l'état de "
        "la dose d'arrêt est décisif, les doses suivantes descriptives")
    issues = {}
    for etats in product(ETATS_JEU_TEXTE, repeat=4):
        j = 0
        while j < 4 and etats[j] == "accumuler bat":
            j += 1
        attendu = (tuple(DOSES[:j]), DOSES[j] if j < 4 else None, etats[j] if j < 4 else None)
        s = et.sequence_fixee(dict(zip(DOSES, etats)))
        module = (tuple(s["franchies"]), s["arret"], s["etat_arret"])
        if module != attendu:
            raise Ecart(f"séquence {etats} : module {module} ≠ transcription {attendu}")
        issues[attendu] = issues.get(attendu, 0) + 1
    ordre = sorted(issues, key=lambda x: (len(x[0]), ETATS_JEU_TEXTE.index(x[2]) if x[2] else 99))
    for n3, (fr, arret, etat) in enumerate(ordre, start=1):
        out(f"S{n3:02d} | doses franchies : {', '.join(fr) or 'aucune'} | dose d'arrêt : {arret or 'aucune (les quatre franchies)'} | "
            f"état de la dose d'arrêt : {etat or '—'} | doses descriptives : {', '.join(DOSES[len(fr) + 1:]) or 'aucune'} | "
            f"combinaisons des 9⁴ : {issues[(fr, arret, etat)]}")
    out(f"bilan de la séquence : {9 ** 4} combinaisons d'états par dose → {len(issues)} issues ; trou : 0 ; écarts : 0")
    if len(issues) != 33 or sum(issues.values()) != 9 ** 4:
        raise Ecart("séquence : 33 issues attendues")

    # 4. phrases
    out("")
    out(f"## 4. Phrases gelées — une par combinaison d'aiguillage, d'état de (i), d'état de `S100` et de dose d'arrêt (avec son "
        f"état) ; « Barreau 6 » écrit « {ph.BARREAU} » (option (a) de N-B6-3) ; crochets symboliques")
    r = ph.remplissage_symbolique()
    n4, par_ligne, produit, distinctes = 0, {}, 0, {}
    for g in ph.AIGUILLAGES:
        for i in ETATS_JEU_TEXTE:
            for fr, arret, etat in ordre:
                s100 = "accumuler bat" if fr else etat
                cas = {"aiguillage": g, "etat_i": i, "sequence": {"franchies": list(fr), "arret": arret, "etat_arret": etat}}
                vraies = premier(TRANSCRIPTION_TABLE, g, i, s100)
                if len(vraies) != 1:
                    raise Ecart(f"plusieurs lignes vraies pour {cas} : {[v[0] for v in vraies]}")
                p = ph.phrase_gelee(cas, r)
                if p["ligne"] != vraies[0][0] or not p["phrase"].strip(" .;"):
                    raise Ecart(f"phrase {cas} : module {p['ligne']!r} ≠ transcription {vraies[0][0]!r}, ou phrase vide")
                produit += 1
                # G-1 ne lit rien ; G-2 ne lit pas (ii) : une ligne par cas de ce qui est lu, les autres combinaisons contrôlées
                cle = (g,) if g == "G-1" else (g, i) if g == "G-2" else (g, i, fr, arret, etat)
                if cle in distinctes:
                    if distinctes[cle] != p["phrase"]:
                        raise Ecart(f"{g} : la phrase dépend de ce qui n'est pas lu ({cas})")
                    continue
                distinctes[cle] = p["phrase"]
                n4 += 1
                par_ligne[p["ligne"]] = par_ligne.get(p["ligne"], 0) + 1
                quoi = ("—" if g == "G-1" else f"(i) {i}") + ("" if g in ("G-1", "G-2") else
                                                             f" | S100 {s100} | franchies {', '.join(fr) or 'aucune'} | arrêt "
                                                             f"{arret or 'aucune'} ({etat or '—'})")
                out(f"P{n4:04d} | {g} | {quoi} | ligne : {p['ligne']} | phrase : {p['phrase']}")
    out(f"bilan des phrases : {n4} cas ({produit} combinaisons du produit complet 4 × 9 × 33 contrôlées : sous G-1 et G-2 la "
        "phrase ne dépend pas de ce qui n'est pas lu) ; cas sans phrase : 0 ; écarts module / transcription : 0 ; par ligne : "
        + ", ".join(f"{k} : {par_ligne.get(k, 0)}" for k in ph.LIGNES))
    out("")
    out("## Bilan")
    out(f"cas sans état : 0 (couples {n}, jeux {n2}, séquence {len(issues)}) ; cas sans phrase : 0 (phrases {n4}) ; écarts : 0")
    Path(sortie).write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{sortie} : couples {n}, jeux {n2}, séquence {len(issues)}, phrases {n4} ; cas sans état : 0 ; cas sans phrase : 0")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage : python3 -I -B scripts/enumeration_etats_accb6_v1.py SORTIE.txt", file=sys.stderr)
        sys.exit(2)
    try:
        sys.exit(main(Path(sys.argv[1])))
    except Ecart as e:
        print(f"ÉCART : {e}", file=sys.stderr)
        sys.exit(1)
