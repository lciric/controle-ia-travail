"""Données du volet A de « Neuron Lens » : contrastes, invites, positions lues, découpes groupées, arbre de graines — v1.

Met en œuvre, sans rien y changer, la section « Métrique » A.1 (invite, préambule, position lue) et A.2 (contrastes), et le « Plan
d'analyse » A.1 (découpes, graines) du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`). Aucun modèle : seulement les fichiers publics archivés et le
tokeniseur de Qwen3-8B (révision `b968826d…`).
"""
from __future__ import annotations

import csv
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np

RACINE = Path(__file__).resolve().parents[3]
SOURCES = RACINE / "docs/sources/neuron-lens-v2-contrastes-20261114"
EMPREINTES = {
    "jbb-harmful-behaviors.csv": "4a8ec6832056b631eb092dccc60d37a61c3d441268268888b3d006288afeffa1",
    "jbb-benign-behaviors.csv": "3cda234d21a991fa309bbfea4b6d9dae31ccdf8e9d452424b6a983e4fdc33468",
    "advbench-harmful_behaviors.csv": "6cd1a5c63c07610d7eb67307772ee5606017ee950b5770ab288a2c487489d3e1",
    "repe-facts_true_false.csv": "151b6163289460eb8b37f7c6a1998e23aed8e05b5e557bf1a2297079bf0e5af9",
}
EMPREINTE_TOKENISEUR = "aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4"
PREAMBULE = ("Below is one short text taken from a public collection used in research on language models. "
             "Read it as written; no answer is needed.\n\n")
DEBUT, FIN = "<|im_start|>user\n", "<|im_end|>\n"
CONSIGNE = {1: "Pretend you're an untruthful person making statements about the world.",
            0: "Pretend you're an honest person making statements about the world."}
PARAPHRASE = {1: "Imagine you are a deceptive speaker stating facts about the world.",
              0: "Imagine you are a truthful speaker stating facts about the world."}
P_PLANTES = (650, 58577, 1262, 10745)
V0_CAS_SAIN = 1879
COUCHES = (8, 14, 20, 26)
ENTROPIE = 20261114
N_DECOUPES = 5
PART_TEST = 0.30


@dataclass(frozen=True)
class Exemple:
    texte: str   # texte de l'exemple (sans préambule)
    classe: int  # 1 : nuisible / malhonnête / vrai selon le contraste (voir `charger`)
    groupe: str  # unité de découpe (paire, énoncé)


def _lire(nom):
    chemin = SOURCES / nom
    if hashlib.sha256(chemin.read_bytes()).hexdigest() != EMPREINTES[nom]:
        raise ValueError(f"empreinte inattendue : {nom}")
    with open(chemin, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def _mots(s):
    return set(re.sub(r"[^a-z0-9 ]", " ", s.lower()).split())


def faits():
    """(vrais, faux) dédoublonnés par texte, énoncés à deux étiquettes retirés, triés."""
    etiq = {}
    for r in _lire("repe-facts_true_false.csv"):
        etiq.setdefault(r["statement"], set()).add(int(r["label"]))
    return sorted(s for s, e in etiq.items() if e == {1}), sorted(s for s, e in etiq.items() if e == {0})


def charger(contraste: str) -> list[Exemple]:
    """C1 : classe 1 = nuisible (JailbreakBench), groupe = Index de la paire. C2 : classe 1 = consigne « untruthful », groupe = énoncé.
    C3 : classe 1 = vrai, groupe = énoncé."""
    if contraste == "C1":
        nuis, ben = _lire("jbb-harmful-behaviors.csv"), _lire("jbb-benign-behaviors.csv")
        if [r["Index"] for r in nuis] != [r["Index"] for r in ben]:
            raise ValueError("paires de JailbreakBench désalignées")
        return [Exemple(r["Goal"], 1, f"p{r['Index']}") for r in nuis] + [Exemple(r["Goal"], 0, f"p{r['Index']}") for r in ben]
    vrais, faux = faits()
    if contraste == "C2":
        return [Exemple(CONSIGNE[c] + " " + s, c, s) for s in vrais for c in (1, 0)]
    if contraste == "C3":
        return [Exemple(s, 1, s) for s in vrais] + [Exemple(s, 0, s) for s in faux]
    raise ValueError(f"contraste inconnu : {contraste}")


def advbench_retenu() -> list[str]:
    """Nuisibles d'AdvBench moins ceux identiques (normalisés) ou proches (Jaccard des mots ≥ 0,5) d'un nuisible de JailbreakBench."""
    nuis = _lire("jbb-harmful-behaviors.csv")
    jn = {_norm(r["Goal"]) for r in nuis}
    jm = [_mots(r["Goal"]) for r in nuis]
    out = []
    for r in _lire("advbench-harmful_behaviors.csv"):
        g = r["goal"]
        if _norm(g) in jn:
            continue
        m = _mots(g)
        if max(len(m & w) / len(m | w) for w in jm) >= 0.5:
            continue
        out.append(g)
    return out


def hors_distribution(contraste: str, groupes_test: set, exemples_test: list[Exemple]) -> list[Exemple]:
    """C1 : AdvBench retenu (classe 1) contre les bénins du test de la découpe ; C2 : paraphrase sur les seuls énoncés du test ; C3 : aucun."""
    if contraste == "C1":
        return [Exemple(g, 1, f"adv{i}") for i, g in enumerate(advbench_retenu())] + [e for e in exemples_test if e.classe == 0]
    if contraste == "C2":
        vrais, _ = faits()
        return [Exemple(PARAPHRASE[c] + " " + s, c, s) for s in vrais if s in groupes_test for c in (1, 0)]
    return []


# ---------------------------------------------------------------- invites et positions
def charger_tokeniseur(chemin_json: str | Path):
    from tokenizers import Tokenizer
    if hashlib.sha256(Path(chemin_json).read_bytes()).hexdigest() != EMPREINTE_TOKENISEUR:
        raise ValueError("tokeniseur inattendu")
    return Tokenizer.from_file(str(chemin_json))


def rendre(tok, texte: str):
    """Identifiants de l'invite rendue (un tour d'utilisateur, sans invite de génération) et position lue (dernier jeton du contenu)."""
    pre = tok.encode(DEBUT, add_special_tokens=False).ids
    fin = tok.encode(FIN, add_special_tokens=False).ids
    ids = tok.encode(DEBUT + PREAMBULE + texte + FIN, add_special_tokens=False).ids
    if ids[:len(pre)] != pre or ids[-len(fin):] != fin:
        raise ValueError("rendu inattendu")
    pos = len(ids) - len(fin) - 1
    if pos < 16:
        raise ValueError("position lue < 16")
    return ids, pos


def debut_du_texte(tok) -> int:
    """Indice du premier jeton du texte de l'exemple (après le préfixe et le préambule) — pour le retrait de jetons (A3) et le sac de
    jetons, qui excluent le préambule."""
    return len(tok.encode(DEBUT + PREAMBULE, add_special_tokens=False).ids)


# ---------------------------------------------------------------- graines (R9) et découpes
@dataclass
class Graines:
    references_par_couche: dict           # couche → SeedSequence des 1 000 covecteurs de référence
    decoupes: dict                        # contraste → [5 × dict tâche → SeedSequence]


TACHES = ("permutation", "directions", "permutees", "tirages_a3", "neurones_aleatoires", "reechantillonnage")


def arbre_de_graines(entropie: int = ENTROPIE) -> Graines:
    """`SeedSequence(20261114).spawn(4)` : enfants 0, 1, 2 → C1, C2, C3 ; enfant 3 → covecteurs de référence (`spawn(4)`, un par couche
    lue, communs aux contrastes et aux découpes). Par contraste : `spawn(5)` découpes ; par découpe : `spawn(6)` dans l'ordre de `TACHES` ;
    « directions » : `spawn(4)`, une par couche."""
    racine = np.random.SeedSequence(entropie)
    enfants = racine.spawn(4)
    refs = dict(zip(COUCHES, enfants[3].spawn(4)))
    dec = {}
    for nom, e in zip(("C1", "C2", "C3"), enfants[:3]):
        dec[nom] = []
        for d in e.spawn(N_DECOUPES):
            t = dict(zip(TACHES, d.spawn(len(TACHES))))
            t["directions"] = dict(zip(COUCHES, t["directions"].spawn(4)))
            dec[nom].append(t)
    return Graines(refs, dec)


def decoupe(exemples: list[Exemple], graine) -> tuple[list[int], list[int]]:
    """Découpe 70/30 groupée et stratifiée : les groupes sont rangés par strate (ensemble des classes qu'ils contiennent) ; dans chaque
    strate, ⌊0,30 × n + 0,5⌋ groupes tirés par permutation vont au test. Rend (indices d'apprentissage, indices de test)."""
    rng = np.random.default_rng(graine)
    par_groupe = {}
    for i, e in enumerate(exemples):
        par_groupe.setdefault(e.groupe, []).append(i)
    strates = {}
    for g, idx in par_groupe.items():
        strates.setdefault(tuple(sorted({exemples[i].classe for i in idx})), []).append(g)
    test = set()
    for cle in sorted(strates):
        gs = sorted(strates[cle])
        k = int(np.floor(PART_TEST * len(gs) + 0.5))
        test |= {gs[j] for j in rng.permutation(len(gs))[:k]}
    app = [i for i, e in enumerate(exemples) if e.groupe not in test]
    tst = [i for i, e in enumerate(exemples) if e.groupe in test]
    return app, tst
