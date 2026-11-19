# Note — Bailey : relance de la confirmation finie (2026-11-19, 10:25Z)

**Fin de la course** (champs techniques seulement) :
- conduite v16 terminée à 10:09:50Z (poste v14) ; marque `poste-fini-v14.json` à 10:09:58Z ; liste des répertoires de
  la sortie écrite (8 entrées) ;
- bilan scellé `sortie-conduite-v16/bilan-conduite-v5.json` : instance 61170458, `detruite` vrai, `transfert_complet`
  vrai, `marque_rapatrie` vrai ; transferts en foi « transfert-1 » pour `mise-en-place`, `controle-juge` et
  `principal-relance` ; `relance_seule` K = 72, c = 1,2194 USD/h. Journal du chien « non transféré
  (CalledProcessError) » : à rapporter ;
- journal des durées transféré : 72 lignes, tours 0 à 71, sans double ; empreinte conforme ;
- `poste-v5.json` : 61170458 créée le 18 novembre à 03:00:10Z, détruite le 19 à 10:09:26Z (31,15 h) ;
- D selon la règle D : 22,93 USD (61049303) + 37,99 USD (61170458) = 60,92 USD, sous B = 85.

**Inventaire de l'instance avant sa destruction** (mot de Lazar) : poste v2, passes à 09:58:37Z et 10:09:11Z. La
seconde passe précède de 15 s la destruction de l'instance et de 39 s la fin de la conduite. 761 fichiers copiés sur
son disque, dont les 157 de `/root/x/principal-relance` ; index des empreintes scellé sur la branche ; fin des passes
à 10:20:21Z.

**Anomalies du poste v2.**
- Sa marque de fin porte le nom de la v1 (`poste-fini-inventaire-instance-v1.json`, commit `ae9447ef`) : défaut de
  renommage de la session. Pas de collision, car la v1, éteinte, n'en a jamais écrit.
- Son journal versé manque : le compagnon est vide, le fichier n'a pas été créé. Le journal reste sur son disque.

**Ce qui suit, avant toute destruction** (mot de Lazar) : inventaire par instantané des postes v14 (176575468),
d'inventaire v1 (176778587, éteint) et d'inventaire v2 (176780521). Les pièces par instantané v1 ne sont pas
utilisables : la contre-lecture est rendue, le constructeur refuse toujours, et un secret pourrait passer par trois voies.
Une v2 est à écrire : elle ne verse que des noms, des tailles, des dates et des empreintes, plus les journaux texte
nettoyés des valeurs exactes. Les contenus restent dans l'instantané, protégé jusqu'à la clôture. Elle sera contre-lue
avant tout usage.
