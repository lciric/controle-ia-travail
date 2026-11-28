import time, sys
sys.path.insert(0, "src")
from controle_ia.harnais.modeles import modele_jouet, tokeniseur_caracteres_chat, regler_determinisme
from controle_ia.harnais.formats import FormatChat
from controle_ia.environnements.pilote_a import noter_ensembles
from controle_ia.harnais.activations import passe_unique
regler_determinisme(1)
tok = tokeniseur_caracteres_chat()
fmt = FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
m = modele_jouet(5, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
dem = [{"cle": f"k{i}", "questions": "Why do routers matter?", "ensemble": f"PROPOSAL 1: idee {i}", "classification": None, "variante": "b0"} for i in range(2)]
t = time.perf_counter()
s = noter_ensembles(m, fmt, dem, {"k0": 1, "k1": 2}, 2, 6, 1.0)
print("noter 2", time.perf_counter() - t, s[0]["jetons_contexte"])
from controle_ia.environnements.juges import messages_juge_ensemble
msgs, _ = messages_juge_ensemble("Why?", "PROPOSAL 1: x", "b0")
ids = fmt.ouverture(msgs[0]["content"], msgs[1]["content"])
t = time.perf_counter()
passe_unique(m, ids, [0, 1, 2])
print("passe", time.perf_counter() - t, len(ids))
