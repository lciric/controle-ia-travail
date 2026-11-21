"""Modèle réel (Llama-3.1-8B-Instruct, transformers, bfloat16) et découpeur au même contrat que le jouet (exploratoire).

Contrat du découpeur : `encoder(texte) -> list[int]` (avec le jeton de début, comme vLLM sur une invite textuelle),
`decoder(ids) -> str`, `eos_ids` (ensemble), `pad_id`. Tout autre modèle que celui du programme est un nœud : le nom est
vérifié ici.
"""
from __future__ import annotations

from ..gardes import GardeArret

MODELE_DU_PROGRAMME = "meta-llama/Llama-3.1-8B-Instruct"


class DecoupeurHF:
    def __init__(self, tok, eos_ids):
        self.tok = tok
        self.eos_ids = {int(i) for i in eos_ids}
        if not self.eos_ids:
            raise GardeArret("aucun jeton de fin")
        self.pad_id = tok.pad_token_id if tok.pad_token_id is not None else min(self.eos_ids)

    def encoder(self, texte: str) -> list[int]:
        """Jeton de début ajouté seulement si le texte ne le porte pas déjà (gabarit de dialogue : jamais deux)."""
        bos = self.tok.bos_token
        speciaux = not (bos and texte.startswith(bos))
        return [int(i) for i in self.tok(texte, add_special_tokens=speciaux)["input_ids"]]

    def decoder(self, ids) -> str:
        return self.tok.decode(list(ids), skip_special_tokens=False)

    def gabarit(self, systeme: str, utilisateur: str) -> str:
        return self.tok.apply_chat_template([{"role": "system", "content": systeme},
                                             {"role": "user", "content": utilisateur}], tokenize=False,
                                            add_generation_prompt=True)


ENTETE_REPONSE_LLAMA = "<|start_header_id|>assistant<|end_header_id|>\n\n"


def charger(nom: str, chemin_local: str | None = None, appareil: str = "cuda"):
    """(modèle en bfloat16, découpeur). `nom` doit être celui du programme."""
    if nom != MODELE_DU_PROGRAMME:
        raise GardeArret(f"modèle {nom!r} : seul {MODELE_DU_PROGRAMME} est admis (tout autre modèle est un nœud)")
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

    source = chemin_local or nom
    tok = AutoTokenizer.from_pretrained(source)
    gc = GenerationConfig.from_pretrained(source)
    eos = gc.eos_token_id if isinstance(gc.eos_token_id, list) else [gc.eos_token_id]
    modele = AutoModelForCausalLM.from_pretrained(source, dtype=torch.bfloat16).to(appareil)
    modele.eval()
    return modele, DecoupeurHF(tok, eos)
