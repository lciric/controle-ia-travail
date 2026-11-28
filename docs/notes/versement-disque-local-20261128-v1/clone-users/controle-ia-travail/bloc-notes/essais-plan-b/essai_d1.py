import time, sys, torch
from controle_ia.harnais.modeles import modele_jouet, tokeniseur_caracteres_chat, regler_determinisme
from controle_ia.harnais.formats import FormatChat
from controle_ia.environnements import juges_simplifies as js
from controle_ia.environnements import juges
regler_determinisme(1)
vrai = juges.charger_invite
juges.charger_invite = lambda i, **k: ("## Scoring Rubric\nSPECIFICITY: <score>\n" if i == "H4" else vrai(i, **k))
tok = tokeniseur_caracteres_chat()
fmt = FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
m = modele_jouet(5, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
dem = [{"cle": f"k{i}", "questions": "Why do routers matter?", "ensemble": f"PROPOSAL 1: idee {i}", "classification": None} for i in range(4)]
g = {d["cle"]: 100 + i for i, d in enumerate(dem)}
for var in ("b0", "RS1"):
  for dtype in (torch.float32, torch.bfloat16):
    mm = m.to(dtype)
    for dec in (0, 1):
        t = time.perf_counter()
        L = js.jouer_lot_de_notations(mm, fmt, dem, g, var, [0, 1, 2], 12, 1.0, 1e-5, "max", decalage_positions=dec)
        print(var, dtype, "dec", dec, f"{time.perf_counter()-t:.1f}s", [x["notation"]["jetons_contexte"] for x in L][:1],
              [round(max(x["rapport"]["ecarts"].values()), 8) for x in L],
              [round(max(p["generee"]["max"] for p in x["rapport"]["profils"].values()), 8) for x in L],
              [round(max(p["contexte"]["max"] for p in x["rapport"]["profils"].values()), 8) for x in L])
    m = m.to(torch.float32)
