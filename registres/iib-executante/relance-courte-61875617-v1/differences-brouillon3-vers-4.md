# Différences : texte de relance courte de 61875617, brouillon 3 vers brouillon 4 ; script v2 vers v3 (une ligne par changement)

- Le brouillon 4 complète le brouillon 3 sans le remplacer ; le script v3 prend la place du v2 (la relance `jouer` est inchangée).
- Analyse franche des moyens : `rm` ne peut pas désarmer la minuterie (identifiant et clé du loueur lus dans l'environnement) ; `update instance` rejeté (« recreate » : risque de perte du disque) ; `copy` local inutilisable (ssh) ; copie d'instance à instance et `cloud copy` laissées en nœud ; `execute` retenu pour lister.
- Constat : les transcriptions des épisodes (identifiants des actions en jetons, `ids-lot-*`) partent avec les lots, dans la même poussée.
- Constat : les journaux complets, `run.err`, `tests.txt` et les autres fichiers de diagnostic ne sont pas pris par le chemin de redémarrage de l'amorce, et aucun moyen sûr ne les rapporte.
- Script : sous-commande `lister` ajoutée (trois `execute` fixes, `ls` et `du`, refus si la machine n'est pas arrêtée).
- Script : sous-commande `archiver` ajoutée (tar en morceaux de 95 Mo au plus, empreintes, réassemblage vérifié, refus si le dossier existe).
- Méthode : préalable P11 (liste du disque rendue), branche cloisonnée faite par la session depuis le clone vérifié, heure au plus tôt du start, nœuds N8 à N10.
- Essais : tous rejoués sur le script v3, plus les essais de `lister` et d'`archiver` (`essais-blanc-relance-courte-v3.txt`).
