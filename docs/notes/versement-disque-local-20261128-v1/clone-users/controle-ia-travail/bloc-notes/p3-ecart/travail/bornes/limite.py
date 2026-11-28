"""Compare les champs lus par lire_action (module gelé) et les bornes de bornes_champs (commit 7a54d43) sur des cas
écrits à la main : clé en gras vide, gras non fermé, cas sains. Tokeniseur par caractères (rang du jeton = rang du caractère)."""
from controle_ia.environnements.propositions import lire_action
from controle_ia.harnais.modeles import tokeniseur_caracteres_chat
from controle_ia.premier_test_ia import conditions as cd
tok = tokeniseur_caracteres_chat()
tete = "ACTION: ADD\nTITLE: a\nPROPOSAL: x\nCONTROLS: c\n"
cas = {
    "sain": tete + "COST: 30\nPREDICTION: y\n",
    "sain gras ferme": tete + "**COST:** 30\n**PREDICTION:** y\n",
    "cle en gras vide puis cle": tete + "**COST:**\n**PREDICTION:** y\n",
    "cle en gras vide puis cle nue": tete + "**COST:**\nPREDICTION: 40\n",
    "gras non ferme": tete + "**COST: 30\nPREDICTION: y\n",
    "gras non ferme puis gras": tete + "**COST: 30\n**PREDICTION:** y\n",
}
for nom, t in cas.items():
    a = lire_action(t)
    b = cd.bornes_champs(tok, tok(t, add_special_tokens=False)["input_ids"], t)
    vus_lire = sorted(k for k in a.champs if k in ("COST", "PREDICTION"))
    vus_bornes = sorted(k for k in ("COST", "PREDICTION") if b[k] != -1)
    print(f"{nom:32s} lire_action {vus_lire} (COST={a.champs.get('COST')!r}) ; bornes {vus_bornes}")
