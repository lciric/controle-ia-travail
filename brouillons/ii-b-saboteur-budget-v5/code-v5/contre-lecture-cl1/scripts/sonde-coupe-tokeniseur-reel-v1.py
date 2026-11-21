"""Coupe de `lecture_cout_v5.coupe_du_prefixe` sur le tokeniseur réel (Llama-3.1-8B-Instruct, révision figée), pour des formes de
la clé COST écrites à la main (aucune donnée de course). Appel : PYTHONPATH=ARBRE/src VENV/python ce_script.py TOKENIZER_JSON"""
import sys
from tokenizers import Tokenizer
from controle_ia.iib.lecture_cout_v5 import coupe_du_prefixe, lire_action_v5
tk = Tokenizer.from_file(sys.argv[1])
class Tok:
    def __call__(self, t, add_special_tokens=False): return {"input_ids": tk.encode(t, add_special_tokens=False).ids}
    def decode(self, ids, skip_special_tokens=True): return tk.decode(list(ids), skip_special_special_tokens=True) if False else tk.decode(list(ids), skip_special_tokens=skip_special_tokens)
tok = Tok()
formes = {"COST: 4 GPUs for 100 hours": "ACTION: train\nCOST: 4 GPUs for 100 hours\nRISK: low",
          "COST:4": "ACTION: train\nCOST:4\nRISK: low",
          "valeur à la ligne suivante": "ACTION: train\nCOST:\n4 GPUs for 100 hours\nRISK: low",
          "COST: puis espace et saut": "ACTION: train\nCOST: \n4 GPUs\nRISK: low",
          "**COST:** 4": "**ACTION:** train\n**COST:** 4 GPUs for 100 hours\n**RISK:** low",
          "**COST**: 4": "**ACTION**: train\n**COST**: 4 GPUs for 100 hours\n**RISK**: low",
          "- **COST:** $400": "- **ACTION:** train\n- **COST:** $400\n- **RISK:** low",
          "COST: suivi de la clé": "ACTION: train\nCOST:\nRISK: low"}
for nom, t in formes.items():
    ids = tok(t)["input_ids"]; c = coupe_du_prefixe(tok, ids)
    morceau = [tk.id_to_token(i) for i in ids if "COST" in tk.decode([i]) or ":" in tk.decode([i])][:4]
    lu = lire_action_v5(tok, ids)
    print(f"{nom!r} : conforme {c['conforme']} ({c['motif']}) ; coût lu {lu['cout_declare']} ; jetons autour de la clé {morceau}")
