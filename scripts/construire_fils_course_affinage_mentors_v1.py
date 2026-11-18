#!/usr/bin/env python3
"""Liste des fils servis et des entrées retirées de la course d'affinage des idées des mentors — version 1.

Lit le relevé d'ensemble des idées des mentors (`mentors-releve-d-ensemble-v1.md`, empreinte épinglée `f7eaec6f…`, sur
`main`), par programme seulement :
- la table des idées (§ 1.1 à 1.6 : 93 lignes « | n° | idée | espèces | provenance | sert | ») ;
- la table des seize fils communs (§ 2 : « | fil commun | où | espèces | remarque | ») ;
- les entrées sous réserve et les réserves de cloisonnement (§ 4), recopiées ci-dessous en constantes **nommées**, chacune
  avec la phrase du relevé qui la fonde (vérifiée présente dans le relevé, mot pour mot).

Écrit un JSON (clés triées) : pour chaque fil, son titre, la liste des idées servies (numéro, texte servi, ligne du relevé,
empreinte du texte source) et la liste des idées retirées (numéro, motif) ; la colonne « où » du relevé n'est gardée que par
son empreinte (elle nomme des espèces) ; la liste globale des retraits ; les contrôles
faits par programme. **Rien n'est reformulé** : le texte servi est la colonne « idée » du relevé, à une exception près,
écrite ici en table exacte (`NEUTRALISATIONS`) : les attributions à une espèce ou à une lettre du collisionneur sont retirées
(les proposeurs servis ne doivent pas savoir quelle espèce a dit quoi ; aucune pièce versée ne nomme un modèle). Chaque
remplacement vise une chaîne exacte, donnée par son empreinte et sa longueur, qui doit figurer une fois dans le texte source ;
sinon, refus.

Usage (aucun réseau ; le relevé est lu sur disque, par exemple extrait de `main` par `git show`) :

    python3 -I -B scripts/construire_fils_course_affinage_mentors_v1.py RELEVE.md SORTIE.json

Code 0 : écrit ; 2 : refus (motif sur la sortie d'erreur). Bibliothèque standard seulement.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

VERSION = "construire_fils_course_affinage_mentors_v1"
RELEVE_SHA256 = "f7eaec6f097859864433f69413233a756ebf241ea541f7eb54b3648818caf9c0"
RELEVE_CHEMIN = "docs/notes/quatre-lectures-inventaire-v1/mentors-releve-d-ensemble-v1.md"

PREFIXES = {"Heimersheim": "H", "Kirchner": "K", "Ibrahim": "I", "Scheurer": "S", "Colognese-Ward": "CW", "Jang-Feng": "JF"}
COMPTES_ATTENDUS = {"H": 22, "K": 17, "I": 16, "S": 13, "CW": 17, "JF": 8}

# --- § 4 du relevé : entrées sous réserve (non reformulées par le relevé, donc absentes de la table des idées) -------------
SOUS_RESERVE = (
    {"entree": "fiche f15ac43332d34 (Kirchner)", "jetons": ["f15ac43332d34"],
     "fondement": "réserve du contre-lecteur Kirchner (§ 6) : partage « classe W2 » à soumettre au même traitement que la fiche 4 de B, exclue au titre de la famille 2"},
    {"entree": "fiche f2ef512adbbf0 (Kirchner)", "jetons": ["f2ef512adbbf0"], "fondement": "même réserve"},
    {"entree": "expérience C1 de C au T3 (Kirchner, 19e1814 T3-C l.32-46)", "jetons": ["T3-C l.32-46"], "fondement": "même réserve"},
    {"entree": "expérience E4 de A au T1 (Kirchner, 19e1814 T1-A l.75-84)", "jetons": ["T1-A l.75-84"], "fondement": "même réserve"},
    {"entree": "fusion inachevée f939b5f14c392 (Kirchner)", "jetons": ["f939b5f14c392"],
     "fondement": "réserve étendue par le rédacteur de ce relevé : ses deux parents sont les deux fiches ci-dessus"},
    {"entree": "règle de strate « injection » et chiffre associé (Scheurer)", "jetons": [],
     "fondement": "réserve du contre-lecteur Scheurer : à retirer si la famille 2 est lue plus largement ; non reprise ici"},
)

# --- § 4 du relevé : réserves de cloisonnement « à trancher par la mère », non levées au scellement -------------------------
# Chaque réserve nomme des lignes de la table (retirées en entier) et des fiches (toute ligne dont la provenance cite l'une
# d'elles est retirée aussi : contrôle par programme).
CLOISONNEMENT = (
    {"reserve": "Scheurer : fusions dont un parent est exclu", "lignes": ["S3", "S5", "S6", "S7"],
     "fiches": ["fed946652c619", "fce8e9166cc32", "f96bab815edbd"],
     "fondement": "Scheurer : trois fusions complètes et la fusion inachevée dont un parent est exclu"},
    {"reserve": "Colognese-Ward (a) : éditions de transcription de D et d'E", "lignes": ["CW1"], "fiches": [],
     "fondement": "(a) les éditions de transcription de D et d'E (CW1) sont les entrées les plus proches de la frontière de la famille 2"},
    {"reserve": "Colognese-Ward (a), extension prudente : « tout le thème CW1 peut être resserré »", "lignes": ["CW2"], "fiches": [],
     "fondement": "tout le thème CW1 peut être resserré selon le rédacteur"},
    {"reserve": "Colognese-Ward (b) : fiches qui entraînent de nouveaux modèles trichant en silence", "lignes": ["CW3", "CW5", "CW10"],
     "fiches": ["f5ae991b0647d", "f811bbace8962", "fe0d4ddfc165a", "f6095565862b6"],
     "fondement": "(b) les fiches qui entraînent de nouveaux modèles trichant en silence"},
    {"reserve": "Jang-Feng : organismes de sous-performance reconstruits d'après des recettes publiées", "lignes": ["JF2", "JF3", "JF5", "JF8"],
     "fiches": ["fe2f9cb3b665c", "feee16a806f32", "f527257af5a2d"],
     "fondement": "huit fiches reconstruisent des organismes de sous-performance d'après des recettes publiées"},
    {"reserve": "Ibrahim : fiche signalée pour l'invariant de N-053", "lignes": ["I16"], "fiches": ["fc62b4ca23035"],
     "fondement": "Ibrahim : `fc62b4ca23035` (I16), signalée pour l'invariant de N-053, non exclue"},
)

# --- attributions retirées du texte servi (chaînes exactes, une occurrence chacune) ----------------------------------------
NEUTRALISATIONS = {
    "H2": [("1aee58ee02f3229edb443957beb56c4ecb7abfaaf95a111b6dbb3c9116b1aeec", 139, "(selon les proposeurs : deux traits pour les uns, une facette pour d'autres ; pour un autre, l'exposant comme prédicteur de la fenêtre d'effet)")],
    "K1": [("2f315a0117507a18eb11006b75a45eac6a64ac85a4ae75ff1d7ca47e9037231b", 5, '.')],
    "K15": [("49b1dc48be6620a43834433a099335a073fe719b6047aacd4636d448a75e0d44", 15, '.')],
    "I6": [("17de1546812f422bc5db38344b5d834e975e2ca50883ff2db8d58efca0fc7a02", 30, '(historique croisé chez un proposeur)')],
    "S1": [("ab56c37599449ff8c2b58d454549e0b24f268df0d75d9486231c599846ed4477", 47, '.')],
    "S8": [("74daae3d91699d96d21d25d36c1b27ddf0d2a76adad093f122e9da35d0a1deff", 47, "(avis d'un proposeur) ; ailleurs, simple covariable")],
    "S10": [("f6be07df1e87b7f6a55e9adb321fd0cbcd2ebe1e0300e2dccb17a7031b158ce4", 6, ' ;'), ("05a301071c3cd5b7fbbe9f6bc52c4b62caca5aaaa52737b0a5a39c3b5bcf4115", 5, '.')],
    "CW6": [("d0e8fab0e227ce9884a160f0f9ececaa9d53c37c0389fbd65902f2a313b3833e", 85, "sens opposés entre deux proposeurs (plus de fausses alertes chez l'anti-triche pour l'un, moins pour l'autre)")],
    "CW7": [("3773d3d6f58684bacb1e423d1860a86e21bd096f2dca5e9de6c57e609f9049dd", 23, '.')],
    "CW16": [("ac30de76b99615fae1f562f56c905f5f7ad1f0d6499d8a3556f686bd78703d79", 5, '.')],
}
# Ce qui ne doit jamais figurer dans un texte servi (contrôle final, mot entier, casse ignorée).
INTERDITS_SERVIS = ("Argon", "Astra", "Kimi", "Carbon", "Gemini", "GPT", "Moonshot", "OpenAI", "Google", "Anthropic", "avis de A",
                    "lettre", "lettres")
# Noms de la famille prioritaire et de ses modèles : gardés par leur empreinte (minuscules), jamais écrits dans une pièce versée.
EMPREINTES_INTERDITES_SERVIES = ("e12ce8285efc67c6d93d3a122e2589ed95089bcbb775ba5634d94e2b8385db07", "09cf980b5ff304ac11b7f6d2c5c263da2a867425798ef5cc5d2ebcf55c4fcd23", "c857d09db23e6822e3600bc06ad8d58f92ed62bc8efd81c753f77048662cb97d")
EMPREINTES_NOMS_CLAUDE = ("e12ce8285efc67c6d93d3a122e2589ed95089bcbb775ba5634d94e2b8385db07", "09cf980b5ff304ac11b7f6d2c5c263da2a867425798ef5cc5d2ebcf55c4fcd23", "c857d09db23e6822e3600bc06ad8d58f92ed62bc8efd81c753f77048662cb97d", "c9ad8f2cc1294afa0ef22fc2c019ff7243cdd272b2147ddca3f34c5036b05768", "5a5110ebe1544b31e6d4207a419bc1deb148735f89ae984ff0a2ab809b51f1df", "553133ea03bb73bd9d747281fdfc7d1164d8cb59f4d638d198c7443c681c6848")

LIGNE_IDEE = re.compile(r"^\| (H|K|I|S|CW|JF)(\d+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$")
LIGNE_FIL = re.compile(r"^\| \*\*(.+?)\*\*(.*?) \| (.*?) \| (.*?) \|(.*)\|$")


class Refus(RuntimeError):
    pass


def sha256_texte(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def lire_idees(lignes: list) -> dict:
    idees = {}
    for n, l in enumerate(lignes, 1):
        m = LIGNE_IDEE.match(l)
        if m:
            ident = m.group(1) + m.group(2)
            if ident in idees:
                raise Refus(f"numéro d'idée en double : {ident}")
            idees[ident] = {"ligne": n, "texte": m.group(3), "provenance": m.group(5)}
    comptes = {p: sum(1 for i in idees if re.fullmatch(p + r"\d+", i)) for p in COMPTES_ATTENDUS}
    if comptes != COMPTES_ATTENDUS or len(idees) != 93:
        raise Refus(f"table des idées : comptes {comptes} (attendus {COMPTES_ATTENDUS}, 93 au total)")
    return idees


def developper_ou(ou: str, idees: dict) -> list:
    """Numéros cités dans la colonne « où » : « X1 à X4 » développé ; « Question (toute la question) » = toutes ses lignes."""
    cites = []
    for question, p in PREFIXES.items():
        if re.search(re.escape(question) + r" \(toute la question\)", ou):
            cites += sorted((i for i in idees if re.fullmatch(p + r"\d+", i)), key=lambda i: int(re.sub(r"\D", "", i)))
    for m in re.finditer(r"\b(H|K|I|S|CW|JF)(\d+) à (H|K|I|S|CW|JF)(\d+)\b", ou):
        if m.group(1) != m.group(3):
            raise Refus(f"intervalle mal formé dans « {ou} »")
        cites += [f"{m.group(1)}{k}" for k in range(int(m.group(2)), int(m.group(4)) + 1)]
    for m in re.finditer(r"\b(H|K|I|S|CW|JF)(\d+)\b", ou):
        cites.append(m.group(1) + m.group(2))
    vus, sortie = set(), []
    for c in cites:
        if c not in idees:
            raise Refus(f"numéro {c} cité par un fil, absent de la table des idées")
        if c not in vus:
            vus.add(c)
            sortie.append(c)
    return sortie


def lire_fils(lignes: list, idees: dict) -> list:
    debut = next(i for i, l in enumerate(lignes) if l.startswith("## 2. Les idées qui reviennent"))
    fin = next(i for i, l in enumerate(lignes) if l.startswith("## 3. Ce qui manque"))
    fils = []
    for n in range(debut, fin):
        m = LIGNE_FIL.match(lignes[n])
        if m:
            fils.append({"rang": len(fils) + 1, "titre": (m.group(1) + m.group(2)).strip(), "ligne": n + 1,
                         "ou": m.group(3), "idees": developper_ou(m.group(3), idees)})
    if len(fils) != 16:
        raise Refus(f"table des fils communs : {len(fils)} lignes, 16 attendues")
    return fils


def texte_servi(ident: str, texte: str) -> tuple:
    """Chaque neutralisation est donnée par l'empreinte et la longueur de la chaîne exacte à remplacer (elle nomme une espèce) :
    une seule position du texte doit avoir cette empreinte, sinon refus."""
    faits = []
    for empreinte, longueur, nouveau in NEUTRALISATIONS.get(ident, ()):
        positions = [i for i in range(len(texte) - longueur + 1) if sha256_texte(texte[i:i + longueur]) == empreinte]
        if len(positions) != 1:
            raise Refus(f"{ident} : chaîne de neutralisation {empreinte[:12]}… trouvée {len(positions)} fois (une exigée)")
        i = positions[0]
        texte = texte[:i] + nouveau + texte[i + longueur:]
        faits.append({"ancien_sha256": empreinte, "nouveau": nouveau})
    return texte, faits


def mots_haches(texte: str) -> set:
    """Empreintes des mots (lettres seules, minuscules) d'un texte."""
    return {sha256_texte(m.lower()) for m in re.findall(r"[^\W\d_]+", texte)}


def construire(chemin_releve: Path) -> dict:
    octets = chemin_releve.read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != RELEVE_SHA256:
        raise Refus(f"relevé d'empreinte {h}, {RELEVE_SHA256} exigée (R11)")
    texte = octets.decode("utf-8")
    lignes = texte.splitlines()
    for r in SOUS_RESERVE + CLOISONNEMENT:
        if r["fondement"].replace("`", "") not in texte.replace("`", ""):
            raise Refus(f"fondement absent du relevé, mot pour mot : {r['fondement']!r}")
    idees = lire_idees(lignes)
    fils = lire_fils(lignes, idees)

    retraits = {}
    for r in CLOISONNEMENT:
        for ident in r["lignes"]:
            retraits.setdefault(ident, []).append("réserve de cloisonnement non levée : " + r["reserve"])
    fiches_reservees = sorted({f for r in CLOISONNEMENT for f in r["fiches"]} | {j for r in SOUS_RESERVE for j in r["jetons"]})
    for ident, d in idees.items():
        for f in fiches_reservees:
            if f in d["provenance"] and not any(f in m for m in retraits.get(ident, [])):
                retraits.setdefault(ident, []).append(f"provenance cite une entrée réservée ({f})")

    sortie_fils, servies_toutes = [], set()
    for f in fils:
        servies, retirees = [], []
        for ident in f["idees"]:
            if ident in retraits:
                retirees.append({"numero": ident, "motifs": retraits[ident]})
                continue
            t, neutre = texte_servi(ident, idees[ident]["texte"])
            servies.append({"numero": ident, "texte_servi": t, "ligne_releve": idees[ident]["ligne"],
                            "texte_releve_sha256": sha256_texte(idees[ident]["texte"]), "neutralisations": neutre})
            servies_toutes.add(ident)
        if not servies:
            raise Refus(f"fil {f['rang']} sans aucune idée servie après retraits")
        sortie_fils.append({"rang": f["rang"], "titre": f["titre"], "ligne_releve": f["ligne"], "ou_releve_sha256": sha256_texte(f["ou"]),
                            "idees_citees": f["idees"], "idees_servies": servies, "idees_retirees": retirees})

    # --- contrôles par programme -------------------------------------------------------------------------------------------
    controles = {}
    croisement = sorted(servies_toutes & set(retraits))
    if croisement:
        raise Refus(f"entrée servie figurant dans la liste des retraits : {croisement}")
    controles["aucune_entree_servie_dans_les_retraits"] = True
    servis_seuls = "\n".join(s["texte_servi"] for f in sortie_fils for s in f["idees_servies"]) + "\n" + \
        "\n".join(f["titre"] for f in sortie_fils)
    for jeton in fiches_reservees:
        if jeton in servis_seuls:
            raise Refus(f"jeton d'une entrée réservée dans un texte servi : {jeton}")
    controles["aucun_jeton_reserve_dans_les_textes_servis"] = fiches_reservees
    for mot in INTERDITS_SERVIS:
        if re.search(r"(?<![\w-])" + re.escape(mot) + r"(?![\w-])", servis_seuls, re.I):
            raise Refus(f"mot interdit dans un texte servi : {mot!r}")
    if mots_haches(servis_seuls) & set(EMPREINTES_INTERDITES_SERVIES):
        raise Refus("nom de la famille prioritaire ou de l'un de ses modèles dans un texte servi")
    controles["aucun_nom_d_espece_ni_de_lettre_dans_les_textes_servis"] = \
        f"{len(INTERDITS_SERVIS) + len(EMPREINTES_INTERDITES_SERVIES)} mots (liste et empreintes dans le script)"
    controles["textes_servis_hors_neutralisation_egaux_au_releve"] = True
    objet = {
        "version": VERSION,
        "statut": ("matière première : chaque idée est l'avis d'un proposeur, jamais un fait ni une preuve ; tout chiffre ou travail "
                   "publié cité reste non vérifié (R7) ; toute zone dite vierge est une question (R8)"),
        "releve": {"chemin": RELEVE_CHEMIN, "branche": "main", "sha256": RELEVE_SHA256},
        "fils": sortie_fils,
        "retraits": {
            "idees_de_la_table": [{"numero": i, "motifs": m, "ligne_releve": idees[i]["ligne"]} for i, m in sorted(retraits.items())],
            "entrees_sous_reserve": [{"entree": r["entree"], "fondement": r["fondement"]} for r in SOUS_RESERVE],
            "reserves_de_cloisonnement": [{k: r[k] for k in ("reserve", "lignes", "fiches", "fondement")} for r in CLOISONNEMENT],
            "exclusions_des_releves": ("jamais servies : les relevés sources les ont exclues avant le relevé d'ensemble (familles 1 et 2) ; "
                                       "elles ne figurent ni dans la table des idées ni ici"),
            "levee": "une entrée retirée ne revient que si la mère lève sa réserve par écrit ; nouvelle version de cette liste (R12)",
        },
        "comptes": {"fils": len(sortie_fils), "idees_table": len(idees), "idees_citees_par_les_fils": len({i for f in fils for i in f["idees"]}),
                    "idees_servies_distinctes": len(servies_toutes), "idees_retirees": len(retraits),
                    "entrees_sous_reserve": len(SOUS_RESERVE)},
        "controles": controles,
    }
    controles["aucun_nom_de_la_famille_prioritaire_dans_la_liste"] = f"{len(EMPREINTES_NOMS_CLAUDE)} mots (empreintes dans le script)"
    if mots_haches(json.dumps(objet, ensure_ascii=False)) & set(EMPREINTES_NOMS_CLAUDE):
        raise Refus("nom de la famille prioritaire ou de l'un de ses modèles dans la liste écrite (aucune pièce versée n'en nomme)")
    return objet


def principal(argv: list) -> int:
    if len(argv) != 2:
        print(json.dumps({"refus": "usage : RELEVE.md SORTIE.json"}, ensure_ascii=False), file=sys.stderr)
        return 2
    releve, sortie = Path(argv[0]), Path(argv[1])
    try:
        if sortie.exists():
            raise Refus(f"{sortie} existe déjà (R12)")
        objet = construire(releve)
    except (Refus, OSError, StopIteration) as e:
        print(json.dumps({"refus": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print(json.dumps({"ecrit": str(sortie), "comptes": objet["comptes"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))
