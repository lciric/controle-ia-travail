"""NON LANCÉ — EN ATTENTE DU MOT DE LAZAR. Programme de lancement des étapes 8 et 9 du palier 0b (code v6), écrit à part du
paquet (un fichier de plus dans le paquet ferait refuser le verrou) ; il n'a été exécuté que sur une racine factice, où le verrou
le refuse avant toute dérivation.

Usage, dossier courant : le dossier du code (celui qui porte `src/`), `PYTHONPATH=src` seul, interpréteur avec `-B` :

    python -B outils-dev/lancer_etapes_8_et_9_v1.py TEXTE RACINE FREQUENCES SHA_FREQUENCES REGLAGES SHA_REGLAGES \
        DOSSIER_8 DOSSIER_9 COMMIT

- TEXTE, RACINE : le texte présenté et la racine de l'arbre lancé, tels que la pièce de contrôle de la mère les fixe (silence
  n° 14) ; le verrou (`graines.Autorisation`) les contrôle avec la pièce d'autorisation du verrou et la table du texte ;
- FREQUENCES, SHA_FREQUENCES, REGLAGES, SHA_REGLAGES : les fichiers gelés des étapes 5 et 6 et leurs empreintes attendues ;
- DOSSIER_8, DOSSIER_9 : deux dossiers neufs (les sorties scellées et le manifeste de chaque étape) ;
- COMMIT : le commit du code lancé, inscrit au manifeste (silence n° 8 : la mère le compare à la main, après le lancement).

Il n'a ni paramètre de couche ni paramètre de taille : l'étape 8 tire sous la couche « decisif », aux tailles gelées, toutes les
cases du plan en un seul lancement ; l'étape 9 lit ses seules sorties scellées et tire, s'il y en a, les cases de C1 et de C4 à
confirmer sous la couche « confirmation », à 100 000 tirages. Il n'écrit à la sortie standard que les chemins et les empreintes
des manifestes, et le nombre de cases tirées : aucun taux, aucun compte, aucun statut (ils se lisent à l'étape 10)."""

import os
import sys

from controle_ia.heritage_etage_processeur_v1 import constantes as K
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1 import graines as GR


def main(arguments):
    if len(arguments) != 9:
        raise SystemExit(__doc__)
    texte, racine, frequences, sha_f, reglages, sha_r, dossier_8, dossier_9, commit = arguments
    for d in (dossier_8, dossier_9):
        if os.path.exists(d):
            raise SystemExit(f"dossier déjà présent : {d} (un dossier neuf est exigé) ; rien n'est lancé")
    autorisation = GR.Autorisation(texte, racine)
    graines = GR.Graines(K.RACINE_GRAINES, autorisation=autorisation)
    r8 = EP.etape_8(graines, dossier_8, commit, frequences, sha_f, reglages, sha_r)
    print("étape 8 :", r8["manifeste"], open(r8["manifeste"] + ".sha256", encoding="ascii").read().split()[0],
          len(r8["cases"]), "cases", flush=True)
    r9 = EP.etape_9(graines, dossier_8, dossier_9, commit, frequences, sha_f, reglages, sha_r)
    if r9["manifeste"] is None:
        print("étape 9 : aucune case à confirmer ; rien n'est écrit", flush=True)
    else:
        print("étape 9 :", r9["manifeste"], open(r9["manifeste"] + ".sha256", encoding="ascii").read().split()[0],
              len(r9["cases"]), "cases", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
