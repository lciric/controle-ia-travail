"""Réduction du script de démarrage, v6 (appelée par fabriquer-donnees-demarrage-v6.sh).

Retire les lignes de commentaire entières (premier signe non blanc « # », sauf la ligne « #! » de tête) et les lignes
vides (vides ou faites de blancs). Ne touche à rien d'autre : ni aux commentaires en fin de ligne, ni à l'ordre, ni aux
octets des lignes gardées.

Garde-fou (choix : les lignes « à l'intérieur » sont GARDÉES) : un lecteur d'état suit, signe par signe, les guillemets
simples, doubles, $'…', les substitutions $( … ), ${ … } et `…`, les fins de ligne échappées (« \\ » final) et les
documents en ligne (<<, <<-, délimiteur cité ou non ; <<< n'en est pas un). Une ligne n'est retirable que si elle
commence hors de tout guillemet, de toute substitution, de tout document en ligne et après une ligne qui ne finit pas
par « \\ ». Si l'état final n'est pas fermé (guillemet ou substitution ouverts, document en ligne sans délimiteur), refus.

Emploi : python -I reduire-script-v6.py ENTREE SORTIE
Codes : 0 fait (sortie neuve écrite) ; 2 usage ou sortie présente ; 3 état non fermé (refus).
"""
import os
import re
import sys

MOT = set(" \t\n;&|()<>")


def lignes_retirables(texte):
    """Rend (liste des lignes avec fin, liste de booléens « commence à l'état propre »), ou lève ValueError."""
    pile = ["N"]           # N normal ; C $( ) (profondeur) ; B ${ } (profondeur) ; K `…` ; S '…' ; A $'…' ; D "…"
    prof = [0]
    attente = []           # documents en ligne annoncés sur la ligne en cours : (délimiteur, retrait des tabulations)
    corps = []             # documents en ligne en cours de lecture
    suite = False          # la ligne précédente finit par une barre oblique inverse (hors guillemets simples)
    lignes = texte.splitlines(keepends=True)
    propre = []
    for ligne in lignes:
        if corps:
            propre.append(False)
            delim, tab = corps[0]
            nue = ligne.rstrip("\n")
            if (nue.lstrip("\t") if tab else nue) == delim:
                corps.pop(0)
            continue
        propre.append(pile == ["N"] and not suite)
        suite = False
        i, n = 0, len(ligne)
        while i < n:
            c = ligne[i]
            haut = pile[-1]
            if haut in ("N", "C", "B", "K"):
                if c == "\\":
                    if i + 1 < n and ligne[i + 1] == "\n":
                        suite = True
                    i += 2
                    continue
                if c == "#" and haut != "B" and (i == 0 or ligne[i - 1] in MOT):
                    break  # commentaire jusqu'à la fin de la ligne
                if c == "'":
                    pile.append("S"); prof.append(0)
                elif c == '"':
                    pile.append("D"); prof.append(0)
                elif c == "$" and ligne[i + 1:i + 2] == "'":
                    pile.append("A"); prof.append(0); i += 1
                elif c == "$" and ligne[i + 1:i + 2] == "(":
                    pile.append("C"); prof.append(1); i += 1
                elif c == "$" and ligne[i + 1:i + 2] == "{":
                    pile.append("B"); prof.append(1); i += 1
                elif c == "`":
                    if haut == "K":
                        pile.pop(); prof.pop()
                    else:
                        pile.append("K"); prof.append(0)
                elif haut == "C" and c == "(":
                    prof[-1] += 1
                elif haut == "C" and c == ")":
                    prof[-1] -= 1
                    if prof[-1] == 0:
                        pile.pop(); prof.pop()
                elif haut == "B" and c == "{":
                    prof[-1] += 1
                elif haut == "B" and c == "}":
                    prof[-1] -= 1
                    if prof[-1] == 0:
                        pile.pop(); prof.pop()
                elif haut != "B" and c == "<" and ligne[i + 1:i + 2] == "<":
                    if ligne[i + 2:i + 3] == "<":
                        i += 3
                        continue
                    m = re.match(r"<<(-?)[ \t]*(['\"]?)([A-Za-z0-9_]+)\2", ligne[i:])
                    if not m:
                        raise ValueError("document en ligne illisible : " + ligne.rstrip())
                    attente.append((m.group(3), m.group(1) == "-"))
                    i += m.end()
                    continue
            elif haut == "S":
                if c == "'":
                    pile.pop(); prof.pop()
            elif haut == "A":
                if c == "\\":
                    i += 2
                    continue
                if c == "'":
                    pile.pop(); prof.pop()
            elif haut == "D":
                if c == "\\":
                    if i + 1 < n and ligne[i + 1] == "\n":
                        suite = True
                    i += 2
                    continue
                if c == '"':
                    pile.pop(); prof.pop()
                elif c == "$" and ligne[i + 1:i + 2] == "(":
                    pile.append("C"); prof.append(1); i += 1
                elif c == "$" and ligne[i + 1:i + 2] == "{":
                    pile.append("B"); prof.append(1); i += 1
                elif c == "`":
                    pile.append("K"); prof.append(0)
            i += 1
        if attente:
            corps.extend(attente)
            attente = []
    if pile != ["N"] or corps or attente:
        raise ValueError("état non fermé en fin de texte : %s, documents en ligne ouverts : %d" % (pile, len(corps) + len(attente)))
    return lignes, propre


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip().splitlines()[-2], file=sys.stderr)
        return 2
    entree, sortie = sys.argv[1], sys.argv[2]
    if os.path.lexists(sortie):
        print("refus : %s présent" % sortie, file=sys.stderr)
        return 2
    with open(entree, "r", encoding="utf-8", newline="") as f:
        texte = f.read()
    try:
        lignes, propre = lignes_retirables(texte)
    except ValueError as e:
        print("refus (garde-fou) : %s" % e, file=sys.stderr)
        return 3
    garde, retire, protege = [], 0, 0
    for k, (ligne, ok) in enumerate(zip(lignes, propre)):
        s = ligne.strip()
        candidat = s == "" or (s.startswith("#") and not (k == 0 and ligne.startswith("#!")))
        if candidat and ok:
            retire += 1
            continue
        if candidat:
            protege += 1
        garde.append(ligne)
    with open(sortie, "x", encoding="utf-8", newline="") as f:
        f.write("".join(garde))
    print("réduction : %d lignes, %d retirées, %d gardées dont %d d'allure de commentaire ou vides mais protégées "
          "(guillemets, substitution, document en ligne ou ligne continuée)" % (len(lignes), retire, len(garde), protege))
    return 0


if __name__ == "__main__":
    sys.exit(main())
