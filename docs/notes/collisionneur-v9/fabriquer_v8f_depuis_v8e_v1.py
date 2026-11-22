"""Fabrique collisionneur_v9_v8f.py depuis la v8e par remplacements exacts."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8e.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest() == "0d591933032e249d17d618e406fe6390ee2536569abc9a232289168122186957"

def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)

src = remplacer(src, """#   de la mère. Détail : rapport-developpeur-collisionneur-v9-v8e-v1.md, même dossier.
""", """#   de la mère. Détail : rapport-developpeur-collisionneur-v9-v8e-v1.md, même dossier.
# v9-v8f (même développeur, 22 novembre 2026) : copie du v9-v8e (0d591933…, inchangé, R12), corrigée selon la
#   contre-lecture d'un Opus neuf (verification-collisionneur-v9-v8e-opus-v1.md). Changements, et seulement ceux-là :
#   (B1) seuls les essais de l'étage III (cellules « E3- ») font refuser un dossier sans consignes-etage3.json : un dossier
#   ouvert sous ce script aux étages I et II passe à l'étage III ; (B2) ce refus est contrôlé avant tout versement (faits,
#   question, composition) : un dossier refusé ne reçoit aucun fichier neuf (etat.md, dérivé, reste réécrit par l'except) ;
#   (NB) `verifier` signale, pour les essais des tours III.1 et III.3 faits sous ce script, un consignes-etage3.json absent
#   et une invite qui ne contient pas la consigne scellée de son tour. Texte de Fable et places du tour III.3 inchangés.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8e"', 'VERSION = "collisionneur-v9-v8f"')
src = remplacer(src, '''    if any("essai" in e for e in lire_journal(dossier)):
        raise Arret(CODE_USAGE, "dossier qui a déjà des essais sans consignes-etage3.json (commencé sous un autre script, "
                                "consignes non balisées) : la v8e ne le reprend pas ; ouvre un nouveau dossier")
    ecrire_neuf(chemin, texte)''', '''    controler_dossier_etage3(dossier)
    ecrire_neuf(chemin, texte)


def controler_dossier_etage3(dossier):
    """v9-v8f (B1, B2) : sans consignes-etage3.json, un dossier qui a déjà des essais de l'étage III (consignes non
    balisées déjà servies) est refusé ; appelé avant tout versement. Les essais des étages I et II ne comptent pas."""
    if (Path(dossier) / "consignes-etage3.json").exists():
        return
    if any(str(e.get("cellule", "")).startswith("E3-") for e in essais_journal(dossier)):
        raise Arret(CODE_USAGE, "dossier qui a déjà des essais de l'étage III sans consignes-etage3.json (commencé sous "
                                "un autre script, consignes non balisées) : ce script ne le reprend pas ; ouvre un "
                                "nouveau dossier ; rien n'est écrit")''')
src = remplacer(src, '''        if etage == 3:  # v9-v8e : place contrôlée avant toute écriture
            fixer_place_iii3(a.place_iii3)''', '''        if etage == 3:  # v9-v8e : place contrôlée avant toute écriture ; v9-v8f (B2) : dossier aussi
            fixer_place_iii3(a.place_iii3)
            controler_dossier_etage3(dossier)''')
src = remplacer(src, '''            problemes.append(f"{nom} : modèle servi {e['modele_servi']} au lieu de {JEV['id']}")
    return problemes
''', '''            problemes.append(f"{nom} : modèle servi {e['modele_servi']} au lieu de {JEV['id']}")
    problemes.extend(problemes_consignes_etage3(dossier, essais))  # v9-v8f
    return problemes


def problemes_consignes_etage3(dossier, essais):
    """v9-v8f : pour les essais des tours III.1 et III.3 faits sous ce script, consignes-etage3.json doit exister et
    chaque invite doit contenir la consigne scellée de son tour."""
    miens = [e for e in essais if e.get("sha256_script") == empreinte_script()
             and str(e.get("cellule", "")).startswith(("E3-T1", "E3-T3"))]
    if not miens:
        return []
    chemin = Path(dossier) / "consignes-etage3.json"
    if not chemin.exists():
        return ["essais des tours III.1 et III.3 sous ce script sans consignes-etage3.json"]
    try:
        consignes = json.loads(lire_sceau(chemin)[0])["consignes"]
    except (Arret, ValueError, KeyError) as x:
        return [f"consignes-etage3.json illisible : {x}"]
    probl = []
    for e in miens:
        base = Path(dossier) / "essais" / f"{e['cellule']}.essai{e['essai']}"
        try:
            prompt = lire_sceau(str(base) + ".prompt.txt")[0]
        except Arret as x:
            probl.append(f"{e['cellule']} essai {e['essai']} : {x}")
            continue
        if consignes.get(e["cellule"][:5]) not in prompt:
            probl.append(f"{e['cellule']} essai {e['essai']} : invite sans la consigne scellée de son tour")
    return probl
''')
(D / "collisionneur_v9_v8f.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
