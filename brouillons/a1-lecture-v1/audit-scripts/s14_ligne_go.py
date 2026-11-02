"""Écart (c) : lit sur l'entrée standard le registre des GO tel que `git show 2eb66705:registres/go.md` le rend (seule
commande git permise dans le dépôt privé) ; n'imprime QUE les lignes qui contiennent « GO-2026-11-02-07 », leur numéro,
leurs cellules ; plus l'empreinte SHA-256 du fichier, son nombre de lignes et son identifiant d'objet git recalculé
(sha1 de « blob <taille>\\0 » + contenu), sans afficher d'autre ligne."""
import sys, hashlib, datetime
brut = sys.stdin.buffer.read()
print("sha256 :", hashlib.sha256(brut).hexdigest(), "| lignes :", brut.count(b"\n"), "| identifiant git recalculé :",
      hashlib.sha1(b"blob " + str(len(brut)).encode() + b"\0" + brut).hexdigest())
CH = "GO-2026-11-02-07"
for n, l in enumerate(brut.decode("utf-8").splitlines(), 1):
    if CH in l:
        cell = [c.strip() for c in l.strip().strip("|").split("|")]
        print(f"ligne {n} : {len(cell)} cellules")
        for nom, c in zip(("identifiant", "accordé le", "type", "périmètre", "plafond", "échéance", "accordé par", "réf."), cell):
            print(f"   {nom} : {c}")
        if len(cell) == 8:
            print("   type = calcul :", cell[2] == "calcul", "| accordé par Lazar :", cell[6] == "Lazar", "| identifiant exact :", cell[0] == CH,
                  "| 2 nov. 2026 dans [accordé ; échéance] :", datetime.date.fromisoformat(cell[1]) <= datetime.date(2026, 11, 2) <= datetime.date.fromisoformat(cell[5]))
