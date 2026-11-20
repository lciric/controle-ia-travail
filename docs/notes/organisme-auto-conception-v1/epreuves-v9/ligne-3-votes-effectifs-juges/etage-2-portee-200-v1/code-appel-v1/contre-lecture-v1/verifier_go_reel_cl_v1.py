"""Contre-lecture S : la garde « ligne de GO » du code (copie du dossier C) jouée sur le registre réel tiré de origin/main
(go-main.md, lu seulement). Aucun appel, aucun mode réel : seule `verifier_ligne_de_go` est appelée, avec des dates fixées.
Usage : python3 -I -B verifier_go_reel_cl_v1.py
"""
import datetime as dt
import hashlib
import sys

DOSSIER = "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-code-appel-etage-2"
sys.path.insert(0, DOSSIER + "/copie")
import epreuve_juges_reels_ligne_3_v1 as M  # noqa: E402

octets = open(DOSSIER + "/go-main.md", "rb").read()
print("registre sha256", hashlib.sha256(octets).hexdigest())
texte = octets.decode("utf-8")
for go_id in ("GO-2026-11-20-26", "GO-2026-11-20-36"):
    for jour in (dt.date(2026, 11, 20), dt.date(2026, 11, 30), dt.date(2026, 12, 1)):
        try:
            r = M.verifier_ligne_de_go(texte, go_id, jour)
            print(go_id, jour, "ACCEPTEE", r["plafond"], r["echeance"])
        except M.Refus as e:
            print(go_id, jour, "REFUS", str(e)[:140])
print("constantes", M.PLAFOND_C, M.SESSION_C, M.RACINE_ORDRE, M.CLES_TACHES)
# ordre tire, deux fois : reproductible
ids = [f"L3-T{k:03d}" for k in range(1, 201)]
a = M.ordre_tire("ordre-bloc-A", ids)
b = M.ordre_tire("ordre-bloc-A", ids)
print("ordre A reproductible", a == b, "permutation", sorted(a) == sorted(ids), a[:3])
print("tarifs", M.TARIF_DES_CARTES)
