#!/usr/bin/env python3
"""Calcul illustratif v1 — complexité perturbationnelle transposée sur GPT-2 petit.

Suit le plan `plan-calcul-illustratif-v1.md` (écrit et empreinté avant exécution).
Processeur seul, numpy seul. Usage :
    python3 -I calcul_illustratif_v1.py DOSSIER_POIDS FICHIER_SORTIE_JSON
"""
import json
import math
import re
import struct
import sys
import time

import numpy as np

GRAINE_MAITRE = 20261122
N_COUCHES, N_TETES, D = 12, 12, 768
T, L0, T0, K_DIR, EPS = 64, 3, 16, 8, 1.0
N_DIM_LZ = 128

# ------------------------------------------------------------------ poids


def lire_safetensors(chemin):
    with open(chemin, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        entete = json.loads(f.read(n))
        base = 8 + n
        poids = {}
        for cle, info in entete.items():
            if cle == "__metadata__" or cle.endswith(".attn.bias"):
                continue
            assert info["dtype"] == "F32", (cle, info["dtype"])
            a, b = info["data_offsets"]
            f.seek(base + a)
            arr = np.frombuffer(f.read(b - a), dtype="<f4").reshape(info["shape"])
            poids[cle] = np.array(arr, dtype=np.float32)
    return poids


def reinitialiser(poids, graine):
    """Poids réinitialisés à la manière de l'initialisation publique de GPT-2."""
    rng = np.random.default_rng(graine)
    neuf = {}
    for cle, w in poids.items():
        if ".ln_" in cle or cle.startswith("ln_f"):
            neuf[cle] = (np.ones_like(w) if cle.endswith("weight") else np.zeros_like(w))
        elif cle.endswith("bias"):
            neuf[cle] = np.zeros_like(w)
        else:
            ecart = 0.02 / np.sqrt(2 * N_COUCHES) if cle.endswith("c_proj.weight") else 0.02
            neuf[cle] = rng.normal(0.0, ecart, size=w.shape).astype(np.float32)
    return neuf


def melanger(poids, graine):
    """Entrées de chaque tenseur entraîné permutées au hasard (même loi marginale)."""
    rng = np.random.default_rng(graine)
    neuf = {}
    for cle in sorted(poids):
        w = poids[cle]
        plat = w.reshape(-1).copy()
        rng.shuffle(plat)
        neuf[cle] = plat.reshape(w.shape)
    return neuf


# ------------------------------------------------------------------ jetons


def octets_vers_unicode():
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(2 ** 8):
        if b not in bs:
            bs.append(b)
            cs.append(2 ** 8 + n)
            n += 1
    return dict(zip(bs, [chr(c) for c in cs]))


class Decoupeur:
    MOTIF = re.compile(r"'s|'t|'re|'ve|'m|'ll|'d| ?[A-Za-z]+| ?[0-9]+| ?[^\sA-Za-z0-9]+|\s+(?!\S)|\s+")

    def __init__(self, chemin_vocab, chemin_fusions):
        with open(chemin_vocab, encoding="utf-8") as f:
            self.vocab = json.load(f)
        with open(chemin_fusions, encoding="utf-8") as f:
            lignes = f.read().split("\n")[1:-1]
        self.rangs = {tuple(l.split()): i for i, l in enumerate(lignes)}
        self.octets = octets_vers_unicode()
        self.cache = {}

    def bpe(self, jeton):
        if jeton in self.cache:
            return self.cache[jeton]
        mot = tuple(jeton)
        while len(mot) > 1:
            paires = {(mot[i], mot[i + 1]) for i in range(len(mot) - 1)}
            meilleure = min(paires, key=lambda p: self.rangs.get(p, float("inf")))
            if meilleure not in self.rangs:
                break
            a, b = meilleure
            neuf, i = [], 0
            while i < len(mot):
                if i < len(mot) - 1 and mot[i] == a and mot[i + 1] == b:
                    neuf.append(a + b)
                    i += 2
                else:
                    neuf.append(mot[i])
                    i += 1
            mot = tuple(neuf)
        self.cache[jeton] = mot
        return mot

    def coder(self, texte):
        ids = []
        for morceau in self.MOTIF.findall(texte):
            morceau = "".join(self.octets[b] for b in morceau.encode("utf-8"))
            ids.extend(self.vocab[m] for m in self.bpe(morceau))
        return ids


# ------------------------------------------------------------------ modèle


def norme_couche(x, g, b):
    m = x.mean(-1, keepdims=True)
    v = ((x - m) ** 2).mean(-1, keepdims=True)
    return (x - m) / np.sqrt(v + 1e-5) * g + b


def gelu(x):
    return 0.5 * x * (1.0 + np.tanh(math.sqrt(2.0 / math.pi) * (x + 0.044715 * x * x * x)))


def passe(W, ids, perturbation=None, alpha=1.0, eta=0.0, graine_bruit=None, avec_logits=True):
    """Passe avant. Rend (flux résiduel de sortie du dernier bloc, logits ou None, norme du site).

    perturbation : vecteur ajouté au flux résiduel à l'entrée du bloc L0, position T0.
    alpha : facteur des mises à jour (attention et perceptron) de tous les blocs.
    eta : norme relative d'un bruit gaussien ajouté après chaque bloc (même graine = même tirage).
    """
    n = len(ids)
    x = W["wte.weight"][ids] + W["wpe.weight"][:n]
    masque = np.triu(np.full((n, n), -1e9, dtype=np.float32), k=1)
    rng = np.random.default_rng(graine_bruit) if eta > 0 else None
    n_site = None
    for c in range(N_COUCHES):
        if c == L0:
            n_site = float(np.linalg.norm(x[T0]))
            if perturbation is not None:
                x = x.copy()
                x[T0] = x[T0] + perturbation
        p = f"h.{c}."
        a = norme_couche(x, W[p + "ln_1.weight"], W[p + "ln_1.bias"])
        qkv = a @ W[p + "attn.c_attn.weight"] + W[p + "attn.c_attn.bias"]
        q, k, v = np.split(qkv, 3, axis=-1)
        q = q.reshape(n, N_TETES, -1).transpose(1, 0, 2)
        k = k.reshape(n, N_TETES, -1).transpose(1, 0, 2)
        v = v.reshape(n, N_TETES, -1).transpose(1, 0, 2)
        s = q @ k.transpose(0, 2, 1) / math.sqrt(q.shape[-1]) + masque
        s = s - s.max(-1, keepdims=True)
        e = np.exp(s)
        att = e / e.sum(-1, keepdims=True)
        o = (att @ v).transpose(1, 0, 2).reshape(n, D)
        x = x + alpha * (o @ W[p + "attn.c_proj.weight"] + W[p + "attn.c_proj.bias"])
        m = norme_couche(x, W[p + "ln_2.weight"], W[p + "ln_2.bias"])
        h = gelu(m @ W[p + "mlp.c_fc.weight"] + W[p + "mlp.c_fc.bias"])
        x = x + alpha * (h @ W[p + "mlp.c_proj.weight"] + W[p + "mlp.c_proj.bias"])
        if rng is not None:
            eff = np.sqrt((x ** 2).mean(-1, keepdims=True))
            x = x + eta * eff * rng.standard_normal(x.shape).astype(np.float32)
    logits = None
    if avec_logits:
        logits = norme_couche(x, W["ln_f.weight"], W["ln_f.bias"]) @ W["wte.weight"].T
    assert x.dtype == np.float32, x.dtype
    return x, logits, n_site


def perte(logits, ids):
    z = logits[:-1].astype(np.float64)
    z = z - z.max(-1, keepdims=True)
    lp = z - np.log(np.exp(z).sum(-1, keepdims=True))
    return float(-lp[np.arange(len(ids) - 1), ids[1:]].mean())


# ------------------------------------------------------------------ mesures


def lz76(s):
    n, i, c = len(s), 0, 0
    while i < n:
        l = 1
        while i + l <= n and s[i:i + l] in s[0:i + l - 1]:
            l += 1
        c += 1
        i += l
    return c


def indice_lz(binaire):
    """binaire : matrice [positions, dimensions] de 0/1, lue position par position."""
    plat = binaire.reshape(-1)
    L = plat.size
    p = float(plat.mean())
    if p <= 0.0 or p >= 1.0:
        return 0.0
    H = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    s = "".join("1" if b else "0" for b in plat)
    return float(lz76(s) * np.log2(L) / (L * H))


def rapport_participation(R):
    R = R / (np.linalg.norm(R, axis=1, keepdims=True) + 1e-30)
    lam = np.clip(np.linalg.eigvalsh(R @ R.T), 0, None)
    return float(lam.sum() ** 2 / ((lam ** 2).sum() + 1e-30))


def mesurer(W, entrees, dims_lz, graine_dir, alpha=1.0, eta=0.0, graine_bruit=None, thetas=(1.0, 0.5, 2.0)):
    propres = [passe(W, ids, alpha=alpha, eta=eta, graine_bruit=graine_bruit) for ids in entrees]
    tous = np.concatenate([x for x, _, _ in propres], axis=0)
    sigma = tous.std(axis=0) + 1e-12
    rng = np.random.default_rng(graine_dir)
    res = {f"lz_theta{t}": [] for t in thetas}
    res.update({"etendue_hors_site": [], "participation": [], "gain_norme_final": []})
    for ids, (x0, _, n_site) in zip(entrees, propres):
        reps = []
        for _ in range(K_DIR):
            u = rng.standard_normal(D).astype(np.float32)
            u = u / np.linalg.norm(u) * EPS * n_site
            x1, _, _ = passe(W, ids, perturbation=u, alpha=alpha, eta=eta, graine_bruit=graine_bruit, avec_logits=False)
            d = (x1 - x0)[T0:]
            z = np.abs(d) / sigma
            for t in thetas:
                res[f"lz_theta{t}"].append(indice_lz(z[:, dims_lz] > t))
            res["etendue_hors_site"].append(float((z[1:] > 1.0).mean()))
            res["gain_norme_final"].append(float(np.linalg.norm(d[1:]) / (np.linalg.norm(u) + 1e-30)))
            reps.append(d[1:].reshape(-1))
        res["participation"].append(rapport_participation(np.stack(reps)))
    out = {k: [float(np.mean(v)), float(np.std(v))] for k, v in res.items()}
    out["n"] = len(res["lz_theta1.0"])
    return out, propres


# ------------------------------------------------------------------ entrées

PASSAGES = [
    "The river begins in the northern hills and runs south for many miles before it reaches the plain. Farmers along its banks have long used the water for their fields, and small towns grew up wherever a bridge could be built. In spring the snow melts and the level rises, so the old houses near the shore were raised on stone walls. Travelers who follow the road beside it can see mills, orchards and quiet harbors.",
    "A good loaf of bread needs only flour, water, salt and time. The baker mixes the dough in the evening and leaves it to rest through the night, so that it slowly rises and develops its taste. In the morning the oven is heated until the bricks are hot, and the loaves are placed inside with a long wooden paddle. After forty minutes the crust is brown and the kitchen smells warm and sweet.",
    "The committee met on Tuesday to review the budget for the coming year. Several members argued that the library should receive more money, because the number of visitors had grown and the roof needed repair. Others replied that the roads were in worse condition and that safety had to come first. After two hours of discussion they agreed to divide the extra funds, and the chairman promised a written report by the end of the month.",
    "Light from distant stars takes many years to reach the Earth, so when we look at the night sky we are looking into the past. Some of the stars we see may have changed greatly since their light began its journey. Astronomers measure the colors of this light to learn what the stars are made of, how hot they are, and how fast they move. Large telescopes on high mountains collect enough light to study very faint objects.",
    "When the train finally arrived, the platform was crowded with people carrying bags and umbrellas. Anna found a seat by the window and watched the city slide away behind the rain. She had not seen her brother for six years, and she wondered whether he would recognize her at the station. The letter in her pocket said only that he would wait near the clock, wearing a gray coat and holding a newspaper.",
    "A simple program reads a list of numbers, adds them together and prints the result. To write it, the student first decides where the numbers come from, then chooses a name for the running total and sets it to zero. A loop visits each number in turn and adds it to the total. When the loop ends, the program shows the answer on the screen. Testing it with a short list makes mistakes easy to find.",
    "The old market opens before sunrise, when the fishermen bring their boxes from the harbor and the first customers arrive with baskets. By eight o'clock the narrow street is full of voices, and the smell of coffee mixes with the smell of the sea. Prices are written on small pieces of paper, but most people still argue a little before they pay. At noon the stalls are closed and the stones are washed with buckets of water.",
    "Doctors advise adults to sleep about seven or eight hours each night, yet many people sleep much less during the working week. A lack of sleep makes it harder to pay attention, to remember new facts and to control one's mood. Regular hours, a dark and quiet room, and less coffee in the afternoon usually help. People who still feel tired after several weeks should speak with a physician about other possible causes.",
]
MOTS_REPETES = [" hello", " the", " water", " seven", " and", " house", " blue", " time"]


def main():
    dossier, sortie = sys.argv[1], sys.argv[2]
    t_debut = time.time()
    ss = np.random.SeedSequence(GRAINE_MAITRE)
    g = [int(s.generate_state(1)[0]) for s in ss.spawn(12)]
    graines = {"dims_lz": g[0], "directions": g[1], "reinit": g[2:5], "melange": g[5:8], "bruit": g[8:10]}

    W = lire_safetensors(dossier + "/model.safetensors")
    dec = Decoupeur(dossier + "/vocab.json", dossier + "/merges.txt")
    naturels = []
    for txt in PASSAGES:
        ids = dec.coder(txt)
        assert len(ids) >= T, len(ids)
        naturels.append(np.array(ids[:T]))
    repetes = [np.array((dec.coder(m) * T)[:T]) for m in MOTS_REPETES]
    dims_lz = np.sort(np.random.default_rng(graines["dims_lz"]).choice(D, N_DIM_LZ, replace=False))

    resultats = {"graines": graines, "parametres": dict(T=T, L0=L0, T0=T0, K_DIR=K_DIR, EPS=EPS, N_DIM_LZ=N_DIM_LZ),
                 "partie1": {}, "partie2": {}}

    def perte_moyenne(propres, entrees):
        return float(np.mean([perte(lg, ids) for (_, lg, _), ids in zip(propres, entrees)]))

    # ---- Partie 1 : systèmes et entrées
    systemes = [("E_entraine", W)]
    systemes += [(f"R{i+1}_reinitialise", reinitialiser(W, s)) for i, s in enumerate(graines["reinit"])]
    systemes += [(f"M{i+1}_melange", melanger(W, s)) for i, s in enumerate(graines["melange"])]
    for nom, Ws in systemes:
        for nom_e, entrees in (("naturel", naturels), ("repetitif", repetes)):
            m, propres = mesurer(Ws, entrees, dims_lz, graines["directions"])
            m["perte_nats"] = perte_moyenne(propres, entrees)
            resultats["partie1"][f"{nom}|{nom_e}"] = m
            print(nom, nom_e, json.dumps(m), flush=True)

    # ---- Partie 2 : lésion graduée et bruit factice, sur E, entrées naturelles
    for alpha in (1.0, 0.85, 0.7, 0.55, 0.4, 0.2, 0.0):
        m, propres = mesurer(W, naturels, dims_lz, graines["directions"], alpha=alpha)
        m["perte_nats"] = perte_moyenne(propres, naturels)
        resultats["partie2"][f"amortissement|alpha={alpha}"] = m
        print("amortissement", alpha, json.dumps(m), flush=True)
    for eta in (0.05, 0.1, 0.2, 0.4, 0.8):
        for j, gb in enumerate(graines["bruit"]):
            m, propres = mesurer(W, naturels, dims_lz, graines["directions"], eta=eta, graine_bruit=gb)
            m["perte_nats"] = perte_moyenne(propres, naturels)
            resultats["partie2"][f"bruit|eta={eta}|graine{j+1}"] = m
            print("bruit", eta, j + 1, json.dumps(m), flush=True)

    resultats["duree_s"] = round(time.time() - t_debut, 1)
    resultats["versions"] = {"python": sys.version.split()[0], "numpy": np.__version__}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultats, f, indent=1, ensure_ascii=False)
    print("duree_s", resultats["duree_s"])


if __name__ == "__main__":
    main()
