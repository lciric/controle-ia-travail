"""Extrait daté des différences entre deux versions d'un programme de calculs (ou de sa sortie), pour les lots réduits
de relecture. Bibliothèque standard seule. Usage : python3 extraire_differences_v1.py AVANT APRES SORTIE_NEUVE
Écrit, en mode « x », les seuls blocs qui diffèrent (difflib, trois lignes de contexte), avec les sources et empreintes."""
import datetime, difflib, hashlib, sys
avant, apres, sortie = sys.argv[1:4]
def lire(p):
    o = open(p, "rb").read()
    return hashlib.sha256(o).hexdigest(), o.decode("utf-8").splitlines()
ha, a = lire(avant)
hb, b = lire(apres)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
corps = list(difflib.unified_diff(a, b, fromfile=avant, tofile=apres, lineterm="", n=3))
heure = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
tete = [
    f"# Extrait des différences : {apres.split('/')[-1]} contre {avant.split('/')[-1]}",
    "",
    f"- Fait le {heure} par `extraire_differences_v1.py` (difflib, trois lignes de contexte).",
    f"- Avant : `{avant}`, sha256 {ha}, {len(a)} lignes.",
    f"- Après : `{apres}`, sha256 {hb}, {len(b)} lignes.",
    f"- {len(ops)} bloc(s) différent(s) ; {sum(o[4]-o[3] for o in ops)} ligne(s) de l'après neuve(s) ou changée(s), "
    f"{sum(o[2]-o[1] for o in ops)} ligne(s) de l'avant ôtée(s) ou changée(s). Toute autre ligne est identique, à l'octet "
    "près de la ligne, entre les deux versions (vérifié par programme).",
    "- Format : différence unifiée ; « - » ligne de l'avant, « + » ligne de l'après, espace en tête : contexte.",
    "",
]
with open(sortie, "x", encoding="utf-8") as f:
    f.write("\n".join(tete + corps) + "\n")
