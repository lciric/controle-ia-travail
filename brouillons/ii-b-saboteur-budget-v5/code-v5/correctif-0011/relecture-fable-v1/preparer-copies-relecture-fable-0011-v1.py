"""Prépare les copies envoyées à la relecture du correctif 0011 par Fable 5.2 (outil relecture_fable_api_v2 de main).
Voie (a) retenue par la mère : on RETIRE ce que la garde interdit, sans le maquiller.
- Chemins du bloc-notes : remplacés par « [bloc-notes] » ; identifiants de session et au format UUID : « [identifiant] » ;
  courriels : « [courriel] » ; noms de personnes : « [nom] ».
- Toute ligne qui porte « donnees/ » (ou « données/ »), ou « rendu », « scores », « verite » dans un chemin ou un nom (jeton
  avec « / », « \\ », « _ », « - », une extension, ou entre accents graves), est remplacée par
  « [ligne retirée : chemin réservé, voir la table] ».
- Une table de remplacement (fichier, numéro de ligne, raison ; jamais le texte retiré) est écrite à côté.
Usage, depuis la racine du dépôt : python3 <ce fichier>."""
import hashlib, json, pathlib, re, subprocess

ICI = pathlib.Path(__file__).resolve().parent
RACINE = pathlib.Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=ICI, text=True).strip())
SRC = {
    "correctif-0011.patch": "brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/correctifs/0011-Organisme-retenu-du-saboteur-budget-code-en-version-.patch",
    "rapport-developpeur-correctif-0011.md": "brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/rapport-developpeur-correctif-0011-v1.md",
    "remarques-mandat-correctif-0011.md": "registres/iib-reconception/mandat-developpeur-correctif-0011-environnement-machine-v1.md",
}
RETIREE = "[ligne retirée : chemin réservé, voir la table]"
TOKEN = re.compile(r"\S+")
def token_reserve(tok):
    low = tok.lower()
    if not re.search(r"rendu|scores|v[eé]rit[eé]", low):
        return False
    return bool(re.search(r"[/\\_\-]|\.[a-z0-9]{1,5}\b|`", tok))
def nettoyer(t):
    t = re.sub(r"/tmp/claude-0/[^\s`'\")]*", "[bloc-notes]", t)
    t = re.sub(r"session[_-][0-9A-Za-z]{20,}", "[identifiant]", t, flags=re.I)
    t = re.sub(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", "[identifiant]", t)
    t = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[courriel]", t)
    t = re.sub(r"(?i)lazar", "[nom]", t)
    t = re.sub(r"(?i)[cć]iri[cć]", "[nom]", t)
    return t

def main():
    table = []
    for nom, chemin in SRC.items():
        lignes = nettoyer((RACINE / chemin).read_text(encoding="utf-8")).split("\n")
        for i, l in enumerate(lignes, 1):
            raison = None
            if re.search(r"(?i)donn[eé]es/", l):
                raison = "dossier des données (chemin réservé)"
            elif any(token_reserve(tok) for tok in TOKEN.findall(l)):
                raison = "mot réservé dans un chemin ou un nom"
            elif re.search(r"(?i)consigne[-_ ]priv[eé]e|conception[-_ .()]ii[-_ .()]b", l):
                raison = "nom de pièce réservé"
            if raison:
                prefixe = l[:1] if nom.endswith(".patch") and l[:1] in "+- " and not l.startswith(("+++", "---")) else ""
                lignes[i - 1] = prefixe + RETIREE
                table.append({"fichier": nom, "ligne": i, "raison": raison})
        texte = "\n".join(lignes)
        (ICI / "entrees" / nom).write_text(texte, encoding="utf-8")
        (ICI / "entrees" / (nom + ".sha256")).write_text(hashlib.sha256(texte.encode()).hexdigest() + "  " + nom + "\n")
        print(nom, "source", hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest()[:12])
    tt = json.dumps({"lignes_retirees": table, "sources": SRC}, ensure_ascii=False, indent=1) + "\n"
    (ICI / "entrees" / "table-des-lignes-retirees.json").write_text(tt, encoding="utf-8")
    (ICI / "entrees" / "table-des-lignes-retirees.json.sha256").write_text(hashlib.sha256(tt.encode()).hexdigest() + "  table-des-lignes-retirees.json\n")
    print("lignes retirées :", len(table))

main()
