"""T0.8 — arrêt de la génération à la balise, sur le tokeniseur réel de Llama-3.1-8B-Instruct (question Q-4 du compte 4 ;
consigne d'alignement, point 6).

Tokeniseur : `donnees/tokeniseur-llama-3.1-8b-instruct-v1/tokenizer.json` de la branche
`donnees/tokeniseur-llama-3.1-8b-instruct-v1`, lu par `git show`, à l'empreinte
`79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` (texte de T0.8, « Score »). Absent de la machine :
l'essai est **sauté, et le dit** ; avec `T08_EXIGER_TOKENISEUR=1`, il échoue au lieu d'être sauté.

Ce qui est éprouvé, avec les fonctions du code (`juges_v1.balise_vue`, critère d'arrêt de la génération, et
`juges_v1.couper_a_la_balise`, point de lecture), sur des identifiants « générés » jeton par jeton :
1. balise précédée d'un saut de ligne, d'une espace ou d'un autre texte, suivie de chacune des valeurs 0 à 100 : la
   génération s'arrête au jeton où la balise apparaît, la coupe est « balise » à ce jeton, et le jeton suivant est
   celui de la valeur (lecture au jeton qui suit la balise) ;
2. balise coupée en jetons de toutes les façons que permet le vocabulaire (tirage de 3 000 découpages parmi
   454 740, graine fixée) : même chose ;
3. **constat déclaré (non corrigé : ce serait changer une règle)** : quand la balise est suivie, dans le même mot du
   prétokeniseur, d'un saut de ligne ou d'une ponctuation (`>\\n`, `>.`, `>:`, `>"`, `>-`, `>(`, `>=` …), le
   tokeniseur fusionne `>` avec ce caractère en un seul jeton : la détection **voit** la balise et arrête la
   génération à ce jeton, mais la balise finit **à l'intérieur** du jeton (« à cheval ») ; le code rend alors une
   anomalie sans score (`ANOMALIE_A_CHEVAL`), aucune valeur n'est lue au jeton suivant. La liste des suffixes
   éprouvés et leur état est figée ci-dessous (`ETATS_APRES_BALISE`).
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
from pathlib import Path

import numpy as np
import pytest

from controle_ia.bases.scores_jetons import jetons_des_valeurs
from controle_ia.t08.configuration_v1 import BALISE, VALEURS_JUGE
from controle_ia.t08.juges_v1 import balise_vue, couper_a_la_balise, exiger_valeur_seule_apres_balise

RACINE = Path(__file__).resolve().parents[1]
BRANCHE = "donnees/tokeniseur-llama-3.1-8b-instruct-v1"
FICHIER = "donnees/tokeniseur-llama-3.1-8b-instruct-v1/tokenizer.json"
SHA_TOKENISEUR = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"

# Constat figé sur le tokeniseur réel : état de la coupe quand la balise est suivie de ce texte.
ETATS_APRES_BALISE = {
    " ": "balise", "\t": "balise", " \n": "balise", "**": "balise", "—": "balise", " 85": "balise",
    "85%": "balise", "0.85": "balise", "1": "balise", "100": "balise", "101": "balise", "1000": "balise",
    "\n": "a_cheval", "\n\n": "a_cheval", "\n85": "a_cheval", ">": "a_cheval", "<": "a_cheval",
    "</sandbagging_confidence>": "a_cheval", ".": "a_cheval", ":": "a_cheval", "=85": "a_cheval", "`": "a_cheval",
    '"': "a_cheval", "'": "a_cheval", "-": "a_cheval", "(85)": "a_cheval", "%": "a_cheval",
}
PREFIXES = ("", "\n", "\n\n", " ", "  ", "\t", "x", "Answer:", "Answer: ", "answer is", ".", ")", "**", "`", "\"",
            "é", "5", "85", "<", ">", "_", "confidence", "sandbagging", "I think\n", "Final:\n", "-> ", "(", "<<")


def _octets_tokeniseur() -> bytes | None:
    for ref in (f"origin/{BRANCHE}", BRANCHE):
        r = subprocess.run(["git", "-C", str(RACINE), "show", f"{ref}:{FICHIER}"], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout
    return None


@pytest.fixture(scope="module")
def tok():
    octets = _octets_tokeniseur()
    if octets is None:
        if os.environ.get("T08_EXIGER_TOKENISEUR") == "1":
            pytest.fail(f"tokeniseur réel absent ({BRANCHE}:{FICHIER}) alors que T08_EXIGER_TOKENISEUR=1")
        pytest.skip(f"tokeniseur réel absent de cette machine ({BRANCHE}:{FICHIER}) : essai SAUTÉ (déclaré)")
    assert hashlib.sha256(octets).hexdigest() == SHA_TOKENISEUR, "tokeniseur d'une autre empreinte que celle du texte"
    from tokenizers import Tokenizer
    from transformers import PreTrainedTokenizerFast

    return PreTrainedTokenizerFast(tokenizer_object=Tokenizer.from_str(octets.decode("utf-8")))


def _arret(tok, ids: list[int]) -> int | None:
    """Génération jeton par jeton : premier jeton après lequel le critère d'arrêt (`balise_vue`) est vrai."""
    for j in range(1, len(ids) + 1):
        if balise_vue(tok, ids[:j]):
            return j
    return None


def test_valeurs_un_jeton_seul_apres_balise(tok):
    jetons = jetons_des_valeurs(tok, VALEURS_JUGE)
    assert len(set(jetons.values())) == 101
    exiger_valeur_seule_apres_balise(tok, jetons)


def test_prefixes_et_valeurs(tok):
    """Point 1 : 28 textes avant la balise × 101 valeurs × 3 fins de texte."""
    jetons = jetons_des_valeurs(tok, VALEURS_JUGE)
    vus = 0
    for p in PREFIXES:
        for v in VALEURS_JUGE:
            for fin in ("</sandbagging_confidence>", "", " and more"):
                ids = tok.encode(f"{p}{BALISE}{v}{fin}", add_special_tokens=False)
                j = _arret(tok, ids)
                assert j is not None, (p, v, fin)
                coupe = couper_a_la_balise(tok, ids[:j])               # identifiants générés jusqu'à l'arrêt
                assert coupe == {"etat": "balise", "k": j}, (p, v, fin, coupe)
                assert tok.decode(ids[:j]).endswith(BALISE)
                assert ids[j] == jetons[v], (p, v, fin, ids[j - 1:j + 2])  # valeur au jeton qui suit la balise
                vus += 1
    assert vus == len(PREFIXES) * 101 * 3


def _decoupages(tok) -> tuple[str, list[list[int]]]:
    """Tous les découpages de la balise en jetons du vocabulaire (forme octets du tokeniseur), comptés ; rend le nombre
    et une fonction de tirage."""
    from tokenizers.pre_tokenizers import ByteLevel

    vocab = tok.get_vocab()
    bl = "".join(x for x, _ in ByteLevel(add_prefix_space=False, use_regex=False).pre_tokenize_str(BALISE))
    n = len(bl)
    suites = [[j for j in range(i + 1, n + 1) if bl[i:j] in vocab] for i in range(n)]
    compte = [0] * (n + 1)
    compte[n] = 1
    for i in range(n - 1, -1, -1):
        compte[i] = sum(compte[j] for j in suites[i])
    return bl, vocab, suites, compte


def test_decoupages_de_la_balise(tok):
    """Point 2 : la balise écrite par le modèle en jetons non canoniques (3 000 découpages tirés uniformément)."""
    jetons = jetons_des_valeurs(tok, VALEURS_JUGE)
    bl, vocab, suites, compte = _decoupages(tok)
    assert compte[0] == 454740
    rng = np.random.default_rng(np.random.SeedSequence(20261122))
    avant = tok.encode("Reasoning done.\n", add_special_tokens=False)
    for _ in range(3000):
        i, seg = 0, []
        while i < len(bl):                         # tirage uniforme parmi les découpages (poids = découpages restants)
            poids = np.array([compte[j] for j in suites[i]], dtype=float)
            j = suites[i][int(rng.choice(len(poids), p=poids / poids.sum()))]
            seg.append(vocab[bl[i:j]])
            i = j
        v = int(rng.integers(0, 101))
        ids = avant + seg + [jetons[v]] + tok.encode("</sandbagging_confidence>", add_special_tokens=False)
        j = _arret(tok, ids)
        assert j == len(avant) + len(seg), seg
        assert couper_a_la_balise(tok, ids[:j]) == {"etat": "balise", "k": j}
        assert ids[j] == jetons[v]


def test_constat_balise_a_cheval(tok):
    """Point 3, constat déclaré : état de la coupe pour chaque texte qui suit la balise. La détection voit toujours la
    balise et arrête au jeton où elle apparaît ; « a_cheval » : la balise finit dans ce jeton (anomalie sans score)."""
    jetons = jetons_des_valeurs(tok, VALEURS_JUGE)
    for suite, attendu in ETATS_APRES_BALISE.items():
        ids = tok.encode(BALISE + suite, add_special_tokens=False)
        j = _arret(tok, ids)
        assert j is not None, suite                               # la détection ne manque jamais la balise
        coupe = couper_a_la_balise(tok, ids[:j])
        assert coupe == {"etat": attendu, "k": j}, (suite, coupe)
        if attendu == "a_cheval":
            assert not tok.decode(ids[:j]).endswith(BALISE) and BALISE in tok.decode(ids[:j])
        elif suite[:1].isdigit():                                 # premier groupe de trois chiffres au plus, lu après
            groupe = int(re.match(r"\d{1,3}", suite).group())       # la balise : jeton d'une valeur s'il vaut 0 à 100
            assert (ids[j] == jetons[groupe]) if groupe <= 100 else (ids[j] not in jetons.values()), suite
