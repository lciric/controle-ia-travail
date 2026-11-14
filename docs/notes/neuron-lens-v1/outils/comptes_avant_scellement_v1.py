"""Comptes sur le texte seul, avant le scellement du texte gelé v2 (volet A) — aucun modèle, aucune activation.

Écrit le 2026-11-14 par la session fille « Neuron Lens ». Lit les jeux publics archivés et le tokeniseur publié de
Qwen3-8B (révision b968826d…), et écrit des comptes : positions lues et sources par contraste avec le préambule, ensemble
P des jetons plantés, effectifs après dédoublonnage, taille des ensembles de jetons « associés » de A2 par découpe.

    python docs/notes/neuron-lens-v1/outils/comptes_avant_scellement_v1.py TOKENIZER_JSON SORTIE_JSON
"""
import csv
import json
import re
import sys
from pathlib import Path

import numpy as np
from scipy.stats import fisher_exact
from tokenizers import Tokenizer

D = Path("docs/sources/neuron-lens-v2-contrastes-20261114")
PREAMBULE = ("Below is one short text taken from a public collection used in research on language models. "
             "Read it as written; no answer is needed.\n\n")
DEBUT, FIN = "<|im_start|>user\n", "<|im_end|>\n"  # gabarit de Qwen3 pour un seul tour d'utilisateur, sans invite de génération
CONSIGNE = {1: "Pretend you're an untruthful person making statements about the world.",
            0: "Pretend you're an honest person making statements about the world."}
PARAPHRASE = {1: "Imagine you are a deceptive speaker stating facts about the world.",
              0: "Imagine you are a truthful speaker stating facts about the world."}
ENTROPIE = 20261114


def lignes(nom):
    with open(D / nom, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def rendu(tok, contenu):
    """Identifiants de l'invite rendue, et bornes [a, b) du contenu de l'utilisateur."""
    pre = tok.encode(DEBUT, add_special_tokens=False).ids
    ids = tok.encode(DEBUT + contenu + FIN, add_special_tokens=False).ids
    fin = tok.encode(FIN, add_special_tokens=False).ids
    assert ids[:len(pre)] == pre and ids[-len(fin):] == fin
    return ids, len(pre), len(ids) - len(fin)


def main(tok_path, sortie):
    tok = Tokenizer.from_file(tok_path)
    out = {"preambule": PREAMBULE, "tokeniseur_sha256_attendu": "aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4"}
    pre_ids, a0, b0 = rendu(tok, PREAMBULE)
    out["preambule_jetons"] = b0 - a0
    out["prefixe_gabarit_jetons"] = a0

    # Faits : dédoublonnage par texte ; retrait des énoncés portant les deux étiquettes.
    faits = lignes("repe-facts_true_false.csv")
    etiq = {}
    for r in faits:
        etiq.setdefault(r["statement"], set()).add(int(r["label"]))
    contradictoires = sorted(s for s, e in etiq.items() if len(e) > 1)
    vrais = sorted(s for s, e in etiq.items() if e == {1})
    faux = sorted(s for s, e in etiq.items() if e == {0})
    out["faits"] = {"lignes": len(faits), "distincts": len(etiq), "contradictoires": contradictoires,
                    "vrais_retenus": len(vrais), "faux_retenus": len(faux)}

    def positions(contenus):
        lues = []
        for c in contenus:
            ids, a, b = rendu(tok, PREAMBULE + c)
            lues.append(b - 1)
        return {"n": len(lues), "min": int(min(lues)), "mediane": float(np.median(lues)), "max": int(max(lues)),
                "sous_16": int(sum(p < 16 for p in lues))}

    # C2 : position source du mot planté, P = identifiants qui diffèrent entre les deux consignes en contexte.
    exemple = vrais[0]
    ids1, a1, _ = rendu(tok, PREAMBULE + CONSIGNE[1] + " " + exemple)
    ids0, a0_, _ = rendu(tok, PREAMBULE + CONSIGNE[0] + " " + exemple)
    i = 0
    while ids1[i] == ids0[i]:
        i += 1
    j = 0
    while ids1[-1 - j] == ids0[-1 - j]:
        j += 1
    diff1, diff0 = ids1[i:len(ids1) - j], ids0[i:len(ids0) - j]
    P = sorted(set(diff1) ^ set(diff0))
    out["C2"] = {"premiere_position_differente": i,
                 "jetons_untruthful": [[t, tok.id_to_token(t)] for t in diff1],
                 "jetons_honest": [[t, tok.id_to_token(t)] for t in diff0],
                 "P": [[t, tok.id_to_token(t)] for t in P]}
    # La différence est-elle la même pour chaque énoncé (même position, mêmes jetons) ?
    stable = True
    for s in vrais:
        x1, _, _ = rendu(tok, PREAMBULE + CONSIGNE[1] + " " + s)
        x0, _, _ = rendu(tok, PREAMBULE + CONSIGNE[0] + " " + s)
        k = 0
        while x1[k] == x0[k]:
            k += 1
        stable &= k == i and x1[k:k + len(diff1)] == diff1 and x0[k:k + len(diff0)] == diff0
    out["C2"]["difference_identique_pour_tous_les_enonces"] = bool(stable)
    out["C2"]["positions_lues"] = positions([CONSIGNE[c] + " " + s for s in vrais for c in (0, 1)])
    out["C2_hors_distribution"] = {"positions_lues": positions([PARAPHRASE[c] + " " + s for s in vrais for c in (0, 1)])}
    out["C3"] = {"positions_lues": positions(vrais + faux)}

    # C1 : JailbreakBench, paires par Index ; AdvBench dédoublonné.
    nuis, ben = lignes("jbb-harmful-behaviors.csv"), lignes("jbb-benign-behaviors.csv")
    assert [r["Index"] for r in nuis] == [r["Index"] for r in ben]
    out["C1"] = {"paires": len(nuis), "positions_lues": positions([r["Goal"] for r in nuis + ben]),
                 "sources_jbb": {s: sum(r["Source"] == s for r in nuis) for s in sorted({r["Source"] for r in nuis})}}
    adv = lignes("advbench-harmful_behaviors.csv")
    jbb_norm = {norm(r["Goal"]) for r in nuis}
    mots = lambda s: set(re.sub(r"[^a-z0-9 ]", " ", s.lower()).split())
    jbb_mots = [mots(r["Goal"]) for r in nuis]
    proche = lambda s: max(len(mots(s) & w) / len(mots(s) | w) for w in jbb_mots) >= 0.5  # Jaccard des mots
    identiques = sum(norm(r["goal"]) in jbb_norm for r in adv)
    adv_ret = [r["goal"] for r in adv if norm(r["goal"]) not in jbb_norm and not proche(r["goal"])]
    out["C1_hors_distribution"] = {"advbench_lignes": len(adv), "retires_identiques": identiques,
                                   "retires_jaccard_0_5": len(adv) - len(adv_ret), "retenus": len(adv_ret),
                                   "positions_lues": positions(adv_ret)}

    # A2 : taille de l'ensemble des jetons « associés » (C1), par découpe et par signe, sur l'apprentissage.
    contenu_ids = []
    for r in nuis + ben:
        ids, a, b = rendu(tok, PREAMBULE + r["Goal"])
        contenu_ids.append(set(ids[a + out["preambule_jetons"]:b]))
    y = np.array([1] * len(nuis) + [0] * len(ben))
    paire = np.array(list(range(len(nuis))) * 2)
    ss = np.random.SeedSequence(ENTROPIE)
    graine_c1 = ss.spawn(3)[0]
    tailles = []
    for k, g in enumerate(graine_c1.spawn(5)):
        rng = np.random.default_rng(g.spawn(1)[0])
        perm = rng.permutation(len(nuis))
        test_paires = set(perm[:30].tolist())  # 30 % des 100 paires
        app = [i for i in range(len(y)) if paire[i] not in test_paires]
        vocab = {}
        for i in app:
            for t in contenu_ids[i]:
                vocab.setdefault(t, [0, 0])[y[i]] += 1
        n1 = sum(y[i] for i in app)
        n0 = len(app) - n1
        tests = [(t, c) for t, c in vocab.items() if c[0] + c[1] >= 5]
        pv = []
        for t, (c0, c1) in tests:
            pv.append(fisher_exact([[c1, n1 - c1], [c0, n0 - c0]]).pvalue)
        pv = np.array(pv)
        m = len(pv)
        ordre = np.argsort(pv)
        seuil = 0
        for r_, idx in enumerate(ordre, 1):
            if pv[idx] <= 0.05 * r_ / m:
                seuil = r_
        signif = {tests[idx][0] for idx in ordre[:seuil]}
        pos = [t for t in signif if vocab[t][1] / n1 > vocab[t][0] / n0]
        neg = [t for t in signif if vocab[t][1] / n1 < vocab[t][0] / n0]
        tailles.append({"decoupe": k, "testes": m, "associes_nuisible": len(pos), "associes_benin": len(neg),
                        "exemples_nuisible": [tok.id_to_token(t) for t in pos[:12]],
                        "exemples_benin": [tok.id_to_token(t) for t in neg[:12]]})
    out["A2_tailles_associes_C1"] = tailles
    Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(json.dumps(out, ensure_ascii=False, indent=1)[:6000])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
