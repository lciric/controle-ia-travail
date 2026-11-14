#!/usr/bin/env python3
"""Dernier couple mécanique de l'étape B bis : du brouillon 3 au texte scellé — v1.

Écrit par la session mère le 2026-11-14 (R-2746). Applique seulement ce que le brouillon 3 annonce dans sa
section « Marqueurs à remplir avant le scellement » :
  - `<<CODE_MOTS_ET_COUT_T06>>` est rempli par l'état de la ligne `CODE-MOTS-ET-COUT-T06` à l'heure du scellement ;
  - `<<CODE_BBIS>>`, `<<ENTROPIE_BBIS>>` et `<<EPREUVE_NIVEAU_DEUX_PLIS>>` sont remplacés par le renvoi à la ligne
    `CODE-BBIS` du registre propre (écart accordé, R-2740) ;
  - dans la section des marqueurs elle-même, les noms perdent leurs chevrons (le validateur refuse tout gabarit
    restant) et une phrase dit quand et par quel script ils ont été remplis.
Aucun autre contenu ne change. Chaque remplacement doit trouver exactement une occurrence, sinon arrêt (R5).

Usage : couples-scellement-v1.py BROUILLON3 SORTIE HEURE_UTC COMMIT_MAIN ETAT
  HEURE_UTC   : relevée par `date -u +%Y-%m-%dT%H:%M:%SZ`
  COMMIT_MAIN : commit de `main` où l'état de la ligne est relevé
  ETAT        : « absente » ou « présente »
"""
import hashlib
import re
import sys

EMPREINTE_BROUILLON3 = "f104917f"  # début de l'empreinte attendue du brouillon 3 (R-2745)
RENVOI = ("inscrit par la ligne `CODE-BBIS` du registre propre, après le scellement et avant toute exécution "
          "(écart accordé, R-2740)")
NOMS = ("CODE_BBIS", "ENTROPIE_BBIS", "EPREUVE_NIVEAU_DEUX_PLIS", "CODE_MOTS_ET_COUT_T06")


def arret(motif):
    sys.stderr.write(f"ARRÊT : {motif}\n")
    sys.exit(2)


def main():
    if len(sys.argv) != 6:
        arret("cinq arguments attendus (voir l'en-tête)")
    entree, sortie, heure, commit, etat = sys.argv[1:]
    if not re.fullmatch(r"2026-11-\d\dT\d\d:\d\d:\d\dZ", heure):
        arret(f"heure mal formée : {heure!r}")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        arret(f"commit mal formé : {commit!r}")
    if etat not in ("absente", "présente"):
        arret(f"état inconnu : {etat!r}")
    if etat == "présente":
        arret("ligne présente : l'état doit alors citer son empreinte ; ce script ne traite que l'absence")
    brut = open(entree, "rb").read()
    if not hashlib.sha256(brut).hexdigest().startswith(EMPREINTE_BROUILLON3):
        arret("le fichier d'entrée n'est pas le brouillon 3 attendu")
    texte = brut.decode("utf-8")

    # 1. Section des marqueurs : les noms perdent leurs chevrons ; une phrase dit quand ils ont été remplis.
    lignes = texte.split("\n")
    idx = [i for i, l in enumerate(lignes) if l.startswith("**Restent ouverts quatre marqueurs**")]
    if len(idx) != 1:
        arret(f"paragraphe des marqueurs trouvé {len(idx)} fois")
    l = lignes[idx[0]]
    attendus = {"CODE_BBIS": 1, "ENTROPIE_BBIS": 1, "EPREUVE_NIVEAU_DEUX_PLIS": 1, "CODE_MOTS_ET_COUT_T06": 2}
    for nom, n in attendus.items():
        if l.count(f"`<<{nom}>>`") != n:
            arret(f"{nom} : {l.count(f'`<<{nom}>>`')} occurrence(s) dans la section des marqueurs, {n} attendue(s)")
        l = l.replace(f"`<<{nom}>>`", f"`{nom}`")
    l += (f" **Remplis au scellement** ({heure}, `date -u`) par `pieces/couples-scellement-v1.py` (dossier des "
          f"brouillons) : `CODE_MOTS_ET_COUT_T06` par l'état de la ligne à cette heure (absente au commit "
          f"`{commit}` de `main`) ; les trois autres par le renvoi à la ligne `CODE-BBIS`.")
    lignes[idx[0]] = l
    texte = "\n".join(lignes)

    # 2. Les quatre marqueurs du corps : une occurrence chacun.
    etat_texte = (f"ligne **absente** de `registres/scellements-v1.md` au commit `{commit}` de `main`, relevé le "
                  f"{heure} (`date -u`) ; le repli ci-dessous s'applique si elle n'est pas inscrite le mercredi "
                  f"18 novembre à 12:00 UTC")
    couples = {
        "`<<CODE_BBIS>>`": RENVOI,
        "`<<ENTROPIE_BBIS>>`": RENVOI,
        "`<<EPREUVE_NIVEAU_DEUX_PLIS>>`": RENVOI,
        "`<<CODE_MOTS_ET_COUT_T06>>`": etat_texte,
    }
    for avant, apres in couples.items():
        if texte.count(avant) != 1:
            arret(f"{avant} : {texte.count(avant)} occurrence(s) dans le corps, une attendue")
        texte = texte.replace(avant, apres)

    restes = re.findall(r"<<[A-Z0-9_]+>>", texte)
    if restes:
        arret(f"marqueurs restants : {restes}")
    open(sortie, "wb").write(texte.encode("utf-8"))
    print(f"ÉCRIT {sortie} {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
