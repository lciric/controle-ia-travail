# Complément 1 au manifeste de l'exécutant de la relance de l'étage 2 de la ligne 3 — fin du geste 9 et redémarrage de la machine — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21. Complète `manifeste-executant-relance-etage-2-v1.md` (`3ad5952f…`), dont la rubrique « Reste » est ici remplie autant que les faits le permettent. Aucune requête aux relais, aucune valeur de clé.

## Fin du geste 9 (pas 7, ligne)
- Ligne unique du journal `/home/user/journaux-etage-2-relance-v2/journal-geste-9-relance-v2.log`, écrite à 10:18:12Z : `{"envois_partis": 1005, "cumul_compte_usd": "33.3702", "arret": null}`.
- Code de sortie : **non relevé** (lancement détaché ; le lanceur n'écrit pas le code). Le processus 30833 était absent à 10:39Z (`stat -c %n /proc/30833` en échec).
- Pas 6 (relevé à mi-course) : **non fait** ; la course était finie avant le premier relevé.

## Relevé des relais après la fin (10:39Z)
- Relais Claude, identifiant 23274 : dépense 2,710388 USD ; 102 appels ; 0 refus ; restant 85,649612 USD.
- Relais Argon, identifiant 23457 : 204 appels ; 0 refus.
- Le relevé brut du relais Claude d'avant lancement (`releve-relais-claude-avant-lancement-v1.json`) n'est **pas versé** : il porte la liste des modèles permis par leurs identifiants. Ses valeurs : plafond 88,36 ; dépense 0,0 ; 0 appel ; 0 refus ; restant 88,36 ; réserve par appel 0,4. Il reste dans le bloc-notes de la session.

## Redémarrage de la machine et arrêt des relais
- La machine a redémarré vers 10:49:37Z (temps de marche de 96 s relevé à 10:51Z). Les deux relais sont morts avec elle.
- L'arrêt par identifiant (R10) et le relevé final n'ont donc pas pu être faits. Preuve d'arrêt : `/proc/23274` et `/proc/23457` absents après le redémarrage.
- Écart au pas 7 du mot de relance : arrêt par la panne et non par identifiant ; relevé final remplacé par celui de 10:39Z, fait après la fin de la course et avant la panne.

## Verdicts de la moitié « lecture »
Scellés par le programme, non ouverts par cette session.

## Pièces versées avec ce complément
Le manifeste, le lanceur et son compagnon, le fichier d'identifiant, le journal (une ligne), la ligne de commande du processus 30833 (`cmdline-30833.bin`, séparateurs nuls), la commande attendue du geste 9.
