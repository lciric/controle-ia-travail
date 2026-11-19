# -*- coding: utf-8 -*-
"""Écrit la version 7 du préenregistrement de la ligne 3 (et le devis v7,
un seul renvoi) par remplacements exacts sur la version 6.

Usage : python3 -B appliquer_v7.py DOSSIER_LIGNE_3 DOSSIER_SORTIE HEURE_FIN

- Les textes des quatre corrections sont TIRÉS de la vérification de la
  version 6 (§ 10), sans recopie à la main.
- Chaque texte ancien doit figurer une fois et une seule dans la source ;
  sinon le programme s'arrête et n'écrit rien.
- Lecture seule dans le dépôt ; écriture dans DOSSIER_SORTIE seulement.
- Bibliothèque standard seule ; aucun réseau ; aucun autre fichier lu.
"""
import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tenue_v7 as T  # noqa: E402

N_VERIF = "verification-ligne-3-v6-v1.md"
N_V6 = "preenregistrement-ligne-3-votes-effectifs-juges-v6.md"
N_V7 = "preenregistrement-ligne-3-votes-effectifs-juges-v7.md"
N_DEVIS_V6 = "devis-ligne-3-etage-payant-v6.md"
N_DEVIS_V7 = "devis-ligne-3-etage-payant-v7.md"


class Arret(Exception):
    pass


def lire(chemin, empreinte_attendue):
    with open(chemin, "rb") as f:
        octets = f.read()
    e = hashlib.sha256(octets).hexdigest()
    if e != empreinte_attendue:
        raise Arret("empreinte inattendue pour %s : %s" % (chemin, e))
    return octets.decode("utf-8")


def entre(texte, debut, fin, depuis=0):
    """Rend (contenu, position après `fin`) ; `debut` puis `fin` cherchés
    à partir de `depuis`. S'arrête si l'un manque."""
    i = texte.find(debut, depuis)
    if i < 0:
        raise Arret("ancre de début introuvable : %r" % debut)
    i += len(debut)
    j = texte.find(fin, i)
    if j < 0:
        raise Arret("ancre de fin introuvable : %r" % fin)
    return texte[i:j], j


def point(verif, n):
    """Rend le texte du point n du § 10 (une ligne)."""
    i = verif.find("\n## 10. Corrections\n")
    if i < 0:
        raise Arret("§ 10 introuvable")
    j = verif.find("\n## ", i + 5)
    section = verif[i:j if j > 0 else len(verif)]
    lignes = [l for l in section.split("\n") if re.match(r"^%d\. \*\*" % n, l)]
    if len(lignes) != 1:
        raise Arret("point %d du § 10 : %d lignes" % (n, len(lignes)))
    return lignes[0] + "\n"


def corrections(verif):
    """Tire du § 10 les couples (nom, ancien, nouveau), à la lettre."""
    c = []

    # Correction 1 : deux remplacements.
    p = point(verif, 1)
    a1, k = entre(p, "Remplacer « ", " » par « ")
    n1, k = entre(p, " » par « ", " » À l'annexe A, remplacer « ", k)
    a2, k = entre(p, " » À l'annexe A, remplacer « ", " » par « ", k)
    n2, k = entre(p, " » par « ", " ».\n", k)
    c.append(("correction 1, (3) Sortie", a1, n1))
    c.append(("correction 1, annexe A", a2, n2))

    # Correction 2 : un ajout après une phrase.
    p = point(verif, 2)
    a, k = entre(p, ", après « ", " », ajouter : « ")
    ajout, k = entre(p, " », ajouter : « ", " »\n", k)
    c.append(("correction 2, puce « Repli »", a, a + " " + ajout))

    # Correction 3 : deux remplacements.
    p = point(verif, 3)
    a1, k = entre(p, "Remplacer « ", " » par « ")
    n1, k = entre(p, " » par « ", " » À la liste d'arrêt, ligne « recouvrement », remplacer « ", k)
    a2, k = entre(p, " » À la liste d'arrêt, ligne « recouvrement », remplacer « ", " » par « ", k)
    n2, k = entre(p, " » par « ", " ».\n", k)
    c.append(("correction 3, (5) journal", a1, n1))
    c.append(("correction 3, liste d'arrêt", a2, n2))

    # Correction 4 : deux remplacements.
    p = point(verif, 4)
    a1, k = entre(p, "À l'en-tête, remplacer « ", " » par « ")
    n1, k = entre(p, " » par « ", " » Au (4), remplacer « ", k)
    a2, k = entre(p, " » Au (4), remplacer « ", " » par « ", k)
    n2, k = entre(p, " » par « ", " ».\n", k)
    c.append(("correction 4, en-tête", a1, n1))
    c.append(("correction 4, (4)", a2, n2))

    for nom, a, n in c:
        if not a or not n or a == n:
            raise Arret("extraction vide ou nulle : %s" % nom)
    return c


def appliquer(source, remplacements, nom_source):
    """Tous les anciens cherchés dans la SOURCE d'origine : une fois et une
    seule, sans chevauchement. Appliqués d'un coup."""
    zones = []
    for nom, ancien, nouveau in remplacements:
        compte = source.count(ancien)
        if compte != 1:
            raise Arret("%s — « %s » : texte ancien trouvé %d fois (attendu 1)"
                        % (nom_source, nom, compte))
        i = source.find(ancien)
        zones.append((i, i + len(ancien), nouveau, nom))
    zones.sort()
    for (d1, f1, _, nom1), (d2, f2, _, nom2) in zip(zones, zones[1:]):
        if d2 < f1:
            raise Arret("chevauchement : « %s » et « %s »" % (nom1, nom2))
    morceaux, curseur = [], 0
    for d, f, nouveau, _ in zones:
        morceaux.append(source[curseur:d])
        morceaux.append(nouveau)
        curseur = f
    morceaux.append(source[curseur:])
    return "".join(morceaux)


def ecrire(chemin, texte):
    if os.path.exists(chemin):
        os.remove(chemin)  # bloc-notes seulement ; jamais dans le dépôt
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        f.write(texte)
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(argv):
    if len(argv) != 4:
        raise Arret("usage : appliquer_v7.py DOSSIER_LIGNE_3 DOSSIER_SORTIE HEURE_FIN")
    dossier, sortie, heure_fin = argv[1], argv[2], argv[3]
    if not re.match(r"^\d\d:\d\d$", heure_fin):
        raise Arret("HEURE_FIN attendue sous la forme HH:MM")
    if "archives-reponses-modeles" in dossier or "archives-reponses-modeles" in sortie:
        raise Arret("chemin interdit")
    if not os.path.abspath(sortie).startswith("/tmp/"):
        raise Arret("la sortie doit être dans le bloc-notes")

    verif = lire(os.path.join(dossier, N_VERIF), T.E_VERIF_V6)
    v6 = lire(os.path.join(dossier, N_V6), T.E_V6)
    devis6 = lire(os.path.join(dossier, N_DEVIS_V6), T.E_DEVIS_V6)

    corr = corrections(verif)
    tenue = [(n, a, b.replace("{HEURE_FIN}", heure_fin)) for n, a, b in T.PREREG_TENUE]
    if not v6.endswith("\n") or not devis6.endswith("\n"):
        raise Arret("fin de fichier inattendue")

    v7 = appliquer(v6, corr + tenue, N_V6) + T.PREREG_FIN
    devis7 = appliquer(devis6, T.DEVIS_TENUE, N_DEVIS_V6) + T.DEVIS_FIN

    # Contrôles après coup : chaque texte neuf des corrections présent une
    # fois et une seule dans la version 7.
    for nom, ancien, nouveau in corr:
        if v7.count(nouveau) != 1:
            raise Arret("après coup — « %s » : texte neuf trouvé %d fois"
                        % (nom, v7.count(nouveau)))
    if "{HEURE_FIN}" in v7:
        raise Arret("heure non remplie")

    os.makedirs(sortie, exist_ok=True)
    e7 = ecrire(os.path.join(sortie, N_V7), v7)
    ed7 = ecrire(os.path.join(sortie, N_DEVIS_V7), devis7)
    for nom, ancien, nouveau in corr:
        print("%s\n  ancien : %s\n  neuf   : %s" % (nom, ancien, nouveau))
    print("remplacements : %d corrections (textes tirés du § 10), %d de tenue ; devis : %d"
          % (len(corr), len(tenue), len(T.DEVIS_TENUE)))
    print("%s  %s" % (e7, N_V7))
    print("%s  %s" % (ed7, N_DEVIS_V7))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Arret as e:
        print("ARRÊT, rien n'est écrit : %s" % e, file=sys.stderr)
        sys.exit(2)
