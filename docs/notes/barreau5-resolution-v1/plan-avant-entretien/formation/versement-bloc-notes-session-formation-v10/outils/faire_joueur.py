"""python -I faire_joueur.py COMMANDE.txt JOUEUR.sh CHEMIN_VAST_BIN : joueur = PATH, GH_TOKEN par son nom, ligne imprimée à l'octet."""
import sys
lignes = open(sys.argv[1], encoding="utf-8").read().split("\n")
assert lignes[0].startswith("B5F COMMANDE"), "en-tête inattendu"
cmd = lignes[1]
assert cmd.startswith("GO_ID=GO-2026-11-19-86 vastai create instance "), "ligne inattendue"
with open(sys.argv[2], "x", encoding="utf-8") as f:
    f.write(f'export PATH="{sys.argv[3]}:$PATH"\nGH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"\n{cmd}\n')
