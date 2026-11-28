"""Rejoue la seule recherche de chaînes du bloc 9 des contrôles du brouillon 3 (valeurs citées par le texte, aux espaces
réduites), sans le reste du bloc. Usage : python3 -I bloc9_valeurs.py TEXTE DOSSIER_VERSEES"""
import re, sys
from pathlib import Path
p, versees = sys.argv[1:3]
lanceur = Path(f"{versees}/lancer_p3_v1.sh").read_text(encoding="utf-8")
def constante(texte, nom, motif=r"[0-9.]+"):
    return re.findall(rf"^{nom}=({motif}) ", texte, re.M)
tel = constante(lanceur, "TELECHARGEMENT_MAX", r"[^ ]+")
assert len(tel) == 1 and re.fullmatch(r"0\.[0-9]{2,4}", tel[0]), tel
sto = constante(lanceur, "STOCKAGE_MAX", r"[^ ]+")
assert len(sto) == 1 and re.fullmatch(r"0\.[0-9]{2,4}", sto[0]), sto
module = Path(f"{versees}/verifications_p3_v1.py").read_text(encoding="utf-8")
prefixes = [re.findall(rf'^{n} = "([^"]+)"', module, re.M) for n in ("PREFIXE_REVOCATION", "PREFIXE_ACCORD")]
assert all(len(x) == 1 for x in prefixes), prefixes
texte = " ".join(Path(p).read_text(encoding="utf-8").split())
valeurs = ("16 200 s", "3 600 s", "300 minutes", "360 minutes", "22 200 s", "6,5 heures", "8,02 USD", "0,22 USD",
           "16 cœurs effectifs", "128 000 Mo", "72 heures", "7 faits", "200 sondes", "= 240 épisodes",
           "51 jetons pour chacune des trois consignes", "10 pour chacune des trois indications",
           "52 jetons pour les trois consignes sur 56 tâches et 51 sur 4", "10 pour les trois indications",
           f"téléchargement au plus {tel[0].replace('.', ',')} USD par Go",
           f"stockage au plus {sto[0].replace('.', ',')} USD de l'heure", prefixes[0][0], prefixes[1][0])
manque = 0
for s in valeurs:
    n = texte.count(s)
    print(f"{'OK ' if n else 'KO '} {n:2d}  {s}")
    manque += (n == 0)
print(len(valeurs), "valeurs ;", manque, "absente(s)")
sys.exit(1 if manque else 0)
