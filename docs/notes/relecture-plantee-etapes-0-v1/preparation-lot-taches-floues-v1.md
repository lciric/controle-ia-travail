# Préparation du lot des tâches floues (liste ouverte), v1

Pièce de travail (classe C), Claude Opus 5.5, 21 novembre 2026. La liste n'est pas figée : un erratum 2 de la
conception v2 et du brouillon v2, avec un programme de calculs v3, est en écriture. Quand ils seront rendus :

1. Compléter les deux listes ci-dessous (ajouter les fichiers de l'erratum 2 et des calculs v3 au rôle « correction » ;
   ajouter au rôle « remarques » la pièce dont l'erratum 2 dit porter les constats, si elle n'y est pas déjà ; décider
   si le programme de calculs v2 et sa sortie entrent au rôle « avant »).
2. Nettoyer, dans un dossier neuf (le premier lot, `lot-taches-floues/`, est gardé et marqué « à ne pas envoyer ») :

```
PYTHONPATH=src python3 -m controle_ia.nettoyage_lots_relecture_v1 \
  --table docs/notes/relecture-plantee-etapes-0-v1/table-remplacement-taches-floues-v1.json \
  --manifeste docs/notes/relecture-plantee-etapes-0-v1/manifeste-nettoyage-taches-floues-v2.json \
  --lot docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-v2 \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/conception-etape-0-taches-floues-v2-erratum-1.md \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/preenregistrement-admission-etape-0-taches-floues-v2-brouillon-erratum-1.md \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/essai-garde-g1-erratum-1-v1.py docs/notes/verite-plantee-etapes-0-v1/taches-floues/essai-garde-g1-erratum-1-v1.txt \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/recalcul-e3-erratum-1-v1.py docs/notes/verite-plantee-etapes-0-v1/taches-floues/recalcul-e3-erratum-1-v1.txt \
    [ERRATUM 2 DE LA CONCEPTION] [ERRATUM 2 DU BROUILLON] [CALCULS V3 .py ET .txt] \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/verification-corrections-etape-0-taches-floues-v2-opus-v1.md \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/verification-erratum-1-etape-0-taches-floues-opus-v1.md \
    [REMARQUES DE L'ERRATUM 2, SI NEUVES] \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/conception-etape-0-taches-floues-v2.md \
    docs/notes/verite-plantee-etapes-0-v1/taches-floues/preenregistrement-admission-etape-0-taches-floues-v2-brouillon.md
```

   Si une paire de la table ne s'applique plus, ou si un motif reste, le programme le dit (codes 5 et 4) et n'écrit
   rien : écrire alors une table v2, chaque paire neuve justifiée dans une note, sans écraser la v1.
3. Copier `consigne-relecture-taches-floues-v1.md` (ce dossier ; écrite sans liste de fichiers, elle vaut pour l'erratum
   2) dans le lot neuf, puis écrire `commande-taches-floues-v1.txt` sur le modèle des deux autres commandes (rôles
   « piece », « remarques », « avant » dans l'ordre ci-dessus ; `--sortie docs/notes/relecture-plantee-etapes-0-v1/sortie-relecture-taches-floues-v1`) et la
   repasser à blanc comme elles (arrêt attendu au comptage, code 10).

Hors du lot, par consigne de la mère : l'extrait de la section 4, le mandat sur le monde du jumeau périmé, et tout
fichier du dossier du protocole X sur le dommage.

Essai en mémoire de la liste actuelle (sans l'erratum 2), table restreinte : paires appliquées [4, 1, 8, 1, 4], aucun
motif restant ; copies 165 482 caractères, consigne 3 144.
