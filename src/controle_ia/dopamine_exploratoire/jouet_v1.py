"""Modèle jouet minuscule (processeur) et son découpeur, pour jouer toute la chaîne dans les essais (exploratoire).

Découpeur à vingt jetons : remplissage, fin, les deux balises ChatML, deux jetons-boîtes `\\boxed{0}` et `\\boxed{1}`,
les dix chiffres, espace, saut de ligne, « + », et « ? » pour tout autre caractère (encodage avec perte : seuls les
jetons comptent, la chaîne ne redécoupe jamais un texte décodé). Les questions jouets demandent la parité d'une somme
(réponse « 0 » ou « 1 ») : un modèle aux poids tirés au hasard répond juste assez souvent pour que les deux issues
existent. Modèle : `LlamaForCausalLM` de transformers, 24 blocs (les couches 2 à 4 et 7, 15, 23 existent), largeur 16.
"""
from __future__ import annotations

import numpy as np

SPECIAUX = ("<pad>", "<eos>", "<|im_start|>", "<|im_end|>", "\\boxed{0}", "\\boxed{1}")
SIMPLES = tuple("0123456789") + (" ", "\n", "+", "?")


class DecoupeurJouet:
    def __init__(self):
        self.vocabulaire = list(SPECIAUX) + list(SIMPLES)
        self.indice = {t: i for i, t in enumerate(self.vocabulaire)}
        self.pad_id, self.eos_id = 0, 1
        self.eos_ids = {1}
        self._longs = sorted((t for t in self.vocabulaire if len(t) > 1), key=len, reverse=True)

    def encoder(self, texte: str) -> list[int]:
        ids, i = [], 0
        while i < len(texte):
            for t in self._longs:
                if texte.startswith(t, i):
                    ids.append(self.indice[t])
                    i += len(t)
                    break
            else:
                ids.append(self.indice.get(texte[i], self.indice["?"]))
                i += 1
        return ids

    def decoder(self, ids) -> str:
        return "".join(self.vocabulaire[int(i)] for i in ids if int(i) not in (self.pad_id,) and int(i) != self.eos_id)

    def __len__(self) -> int:
        return len(self.vocabulaire)


def modele_jouet(graine: int = 0, couches: int = 24, largeur: int = 16, biais_boite: float = 2.0):
    import torch
    from transformers import LlamaConfig, LlamaForCausalLM

    d = DecoupeurJouet()
    cfg = LlamaConfig(vocab_size=len(d), hidden_size=largeur, intermediate_size=2 * largeur, num_hidden_layers=couches,
                      num_attention_heads=2, num_key_value_heads=1, max_position_embeddings=1024, pad_token_id=d.pad_id,
                      eos_token_id=d.eos_id, bos_token_id=None, tie_word_embeddings=False, initializer_range=0.5)
    torch.set_num_threads(1)          # jouet seulement : un fil, cinq fois plus vite sur ces opérations minuscules
    torch.manual_seed(int(graine))
    m = LlamaForCausalLM(cfg)
    # tête de sortie avec un biais : les deux jetons-boîtes sont favorisés, pour que les deux issues soient fréquentes
    tete = torch.nn.Linear(largeur, len(d), bias=True)
    with torch.no_grad():
        tete.weight.copy_(m.lm_head.weight)
        tete.bias.zero_()
        tete.bias[d.indice["\\boxed{0}"]] = tete.bias[d.indice["\\boxed{1}"]] = biais_boite
    m.lm_head = tete
    m.eval()
    return m, d


def questions_jouets(n: int, graine: int = 0, familles: int | None = None) -> list[dict]:
    """Questions « a+b » à réponse de parité ; `familles` : nombre de familles de tâches (étape 2a jouée)."""
    rng = np.random.default_rng(graine)
    qs = []
    for i in range(n):
        a, b = (int(x) for x in rng.integers(0, 50, size=2))
        q = {"id": f"jouet-{i:04d}", "probleme": f"{a}+{b}", "reponse_attendue": str((a + b) % 2)}
        if familles:
            q["famille"] = f"famille-{i % familles:02d}"
        qs.append(q)
    return qs
