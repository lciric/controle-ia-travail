# Lacunes du texte relevées par le développeur du code de la lecture, avec la phrase proposée — v1

Déposé par la conductrice côté moniteurs le 2026-11-19 vers 01:50Z, par transcription du rapport d'étape du développeur du code de la lecture (Fable 5.2). Les numéros de ligne sont ceux du brouillon 8 (`prereg-lecture-sondes-barreau8-v1-brouillon8.md`, `d8992b575a4e03fa6647b7d5af663596f80870925164b328adc0985c29f98b3a`). Aucun résultat du programme. État de ses essais sur données synthétiques, dernière ligne : `125 passed in 160.83s (0:02:40)`.

## Les seize lacunes

**1. Formats de la livraison** — section « Passe », « Ce qui est livré », l. 251 à 256. Le texte fixe le contenu, pas les noms, les conteneurs ni les champs.
Ajouter après la l. 256 : « **Noms et champs, liste fermée** : (table des noms de fichiers, du conteneur, de la règle des morceaux, des champs de l'index, de la trace et du bordereau, reprise de la notice du développeur de la passe). Tout fichier, toute clé ou tout champ hors de cette table est un refus de la garde de réception (r2, r3, r4). »

**2. Fichier de sondes absent : refus ou « sans objet »** — le plan (l. 167, fin) dit que la lecture refuse de tourner ; la règle mécanique (l. 311) et la liste d'arrêt (ligne 8) disent « sans objet ». Implémenté : la règle, puis refus r4 si l'état diffère de la trace ; un fichier présent sans compagnon conforme est un refus (ligne 7).
- Remplacer, l. 167, « les fichiers de sondes et de planchers à leurs empreintes (D-8) » par : « la règle mécanique des sondes lues appliquée à la réception (D-8) : un fichier absent ou d'empreinte différente rend sa sonde "sans objet" ; la lecture refuse de tourner si l'état d'une sonde à la réception diffère de celui de la trace de la passe, ou si un fichier présent à son empreinte n'a pas de compagnon conforme ».
- Ajouter à r4 (l. 264) : « l'état de chaque sonde dans la trace est celui que la règle mécanique rend à la réception ; sinon refus ».

**3. S3 « modèle » et S4 inatteignables ; nombre de couches absent de la trace** — l. 345, 346, 255. r4 refuse un modèle autre, r5 refuse une livraison sans les 640 actions de `H`. Gardées comme gardes ; S4 lue comme « aucune action notée de `H` ».
- S3 (l. 345), ajouter au verdict : « ; ligne de mémoire pour la branche "modèle" : la garde r4 refuse alors la livraison ; seuls le nom et la révision sont lus dans la trace, le nombre de couches étant tenu par la garde P2 ».
- S4 (l. 346), remplacer l'issue par : « aucune action de la condition `H` n'a de jeton noté (la livraison porte les 640 actions de `H`, garde r5) ».

**4. « Adaptateur et dose relus : non » dans la trace** — r4, l. 264, ne le cite pas. Implémenté : refus.
Ajouter à r4 : « "adaptateur et dose relus égaux à I-5" vaut "oui" à chaque condition ; ».

**5. Clé de graine des aires « hors jugement » des sondes de la couche 15** — l. 155 et l. 169 ne la nomment pas. Implémenté : `descriptif/<sonde>/<jeu>`.
Ajouter, l. 155, après « marquées "hors jugement" » : « (aire et intervalle propre par blocs de tâches, 2 000 tirages, niveau 0,95, sans comparaison au plancher, graine `descriptif/<sonde>/<jeu>`, pour chaque sonde lue, contre `H` et contre `TJ100`) ».

**6. Essai de la chaîne : une seule clé par essai ; écart-type non défini** — l. 370 à 372. Implémenté : la même graine entière sert au tirage et au rééchantillonnage ; « s » pris sans correction.
- Ajouter au chapeau (l. 369) : « Pour chaque essai, la graine entière de sa clé sert d'abord au tirage de l'essai (tâches étiquetées, jeton injecté, permutation) par un générateur neuf, puis, telle quelle, au rééchantillonnage par blocs (2 000 tirages). »
- En (ii), après « s étant l'écart-type » : « (de population, diviseur n) ».

**7. Déclencheur d4 et « bornes au niveau 0,95 »** — l. 159 (d4) et l. 377. Implémenté : d4 avec « au-dessus » recalculé à 0,95 sous la même graine (déclenche plus facilement).
Remplacer, l. 377, « bornes au niveau 0,95 sauf d1 (niveau décisif) » par : « d2 et d3 sur les estimations ponctuelles ; d4 avec "au-dessus" recalculé au niveau 0,95 sur chaque jeu décisif, sous la graine du jeu ; d1 au niveau décisif ».

**8. Classe vide dans un jeu ; tâches différentes pour la dose** — l. 131, liste d'arrêt ligne 9 (l. 394), B8-P3 (l. 117). Implémenté : « échec » dans les deux cas.
- Ajouter, l. 131, après « (`sondes/evaluation.py`, ligne 59) » : « ; une classe sans aucune action notée sur un jeu tombe sous la même règle : "échec" ».
- Ajouter à B8-P3, colonne « réfutation » : « ; "échec", cause écrite, si les deux jeux ne portent pas les mêmes tâches ou si plus de 1 % des tirages n'ont pas les deux classes dans l'un des deux ».

**9. Ordre des lignes S et de l'essai de la chaîne** — l. 339, l. 352 (L5), l. 369. Implémenté : S1, S3, S4 : rien n'est joué. S2, S5 : l'essai est joué ; s'il échoue, L5 s'ajoute et rien de descriptif n'est calculé.
Ajouter après la table (l. 355) : « Sous S1, S3 ou S4, l'essai A0 n'est pas joué. Sous S2 ou S5, il l'est avant tout descriptif ; s'il échoue, la ligne L5 est écrite à côté de la ligne S, et aucune aire, même descriptive, n'est calculée. »

**10. Réserve de validité de la sonde de dissimulation** — l. 105 dit « un état U porté par elle seule à une condition jugée » ; l. 360 dit « L1 avec… ». Implémenté : écrite dès qu'une condition jugée est U par elle seule.
Remplacer, l. 360, « L1 avec, à une condition jugée, la sonde de dissimulation pour seule porteuse » par : « Toute issue où, à une condition jugée d'état U, la sonde de dissimulation est la seule porteuse ».

**11. Recette de la puissance** — l. 175, 180, 181.
- l. 175, remplacer « Une fraction f des actions de chaque condition sabotée, tirée au hasard, » par : « Exactement round(f × 640) actions de chaque condition sabotée, tirées sans remise, ».
- l. 181, remplacer « l'issue "porteuse à `B100` seule" » par : « les issues "porteuse à `B100`" (`B100` considérée seule) et "porteuse à `B100` et non à `B50`" ».
- Ajouter à la l. 180 : « Graines : de la séquence de la clé `puissance`, une séquence fille par (rang de la case dans l'ordre de la grille, rang de la répétition, usage), usage 0 pour les données, 1 à 4 pour les quatre jeux dans l'ordre `B50` contre `H`, `B50` contre `TJ100`, `B100` contre `H`, `B100` contre `TJ100`. Le budget est contrôlé avant chaque répétition ; la case en cours quand il est atteint est "non calculée". »

**12. Pièces de D-5 et D-6 pour le code de la lecture** — l. 89, 90. Implémenté : les deux mandats scellés citant deux empreintes passées en option, et une pièce scellée pour l'ordre, jamais ouverte.
- D-5 : « ; le code de la lecture exige les deux mandats scellés et refuse si l'un ne cite pas les deux empreintes qui lui sont données ».
- D-6 : « ; le code de la lecture exige la pièce scellée de cette comparaison (existence et empreinte seulement, jamais ouverte) ».

**13. Écriture de F-3** — l. 75. Implémenté : refus si l'entropie donnée ne figure pas en décimal dans le texte scellé.
Proposition du développeur : remplacer l'état de F-3 par « (entier écrit en décimal, sans séparateur) ; le code de la lecture et celui de la recette refusent de tourner si l'entropie qui leur est donnée ne figure pas ainsi dans le texte scellé ».
Note de la conductrice : la cellule « état et raison » de F-3 doit rester exactement la chaîne que la procédure de remplissage remplace par l'entier seul ; cette phrase est donc à porter AILLEURS (colonne du champ, ou plan d'analyse, point des graines), jamais dans la cellule remplacée.

**14. Taille totale de r2** — l. 262. Implémenté : somme de tous les fichiers du dossier.
Remplacer « la taille totale est d'au plus 2 000 000 000 octets » par : « la somme des tailles de tous les fichiers reçus, compagnons d'empreinte et bordereau compris, est d'au plus 2 000 000 000 octets ».

**15. Écart-type du repère r8** — l. 268. Ajouter après « l'écart-type » : « (de population) ».

**16. Sonde des couches 7 ou 23 présente sous son nom mais d'une autre famille** — l. 137. Implémenté : refus (liste d'arrêt, ligne 15).
Ajouter : « Une sonde trouvée sous l'un de ces noms qui n'est pas une `SondeLineaireJetons` agrégée par le maximum à la couche de son nom est un écart : refus (liste d'arrêt, ligne 15). »

## Trois points de plus

**17. Bordereau du code** — section « Code, registre et contrôle de conformité » ; le brouillon 8 ne le décrit pas.
Proposition : « La ligne `CODE-LECTURE-SONDES-IIB` cite un bordereau du code scellé, à six clés fermées : `texte_scelle`, `modules`, `commit`, `rapport_conformite`, `notice`, `accord_lecture`. À l'ouverture : texte égal à celui de la ligne `SCELLEMENT-SONDES-IIB`, rapport et notice présents à leur empreinte, modules chargés aux empreintes du bordereau ; sinon refus. »

**18. Conditions ajoutées au registre par le développeur, à confirmer ou à retirer** : la ligne `ETATS-COURSE-IIB` doit être strictement postérieure au scellement ; la ligne `LIVRAISON-PASSE-IIB` n'a aucune condition d'ordre ; toute clé de registre hors des six, sur une ligne à quatre colonnes datée, est refusée.

**19. Essai de la chaîne** : dans le code, c'est l'étape (d) de la commande de lecture (plan, point 4), pas une commande à part ; le jouer seul lirait des scores avant le manifeste.

## Forme des lignes du registre propre (transmise par la session mère, sur le précédent du programme)
En-tête : « # Registre propre … — texte `<chemin du texte scellé>` ; lignes ajoutées, jamais réécrites ; format : | CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 | ». Chaque ligne : une clé, une heure en temps universel à la seconde, un chemin relatif au dépôt, une empreinte entière. Mêmes quatre colonnes pour les six clés ; une seule ligne par clé. Les deux lignes de code citent chacune un bordereau du code scellé (décision de routine de la conductrice, une ligne ne portant qu'un chemin et une empreinte).

## Forme de l'extrait scellé du côté exposé qui accompagne la note d'interface (réponse du côté exposé, sans mécanisme, transmise par la session mère)
Premier niveau, exactement six clés : `avertissement` (chaîne constante « EXPLORATOIRE, NON OPPOSABLE (R-522) : extrait sans mécanisme pour le côté moniteurs ») ; `run_id` (forme AAAAMMJJ-HHMMSS-<minuscules, chiffres, tirets>) ; `commit_lancement` (40 caractères hexadécimaux minuscules) ; `versions` (objet chaîne → chaîne, clés triées, sous-ensemble de python, plateforme, numpy, scipy, matplotlib, torch, transformers, tokenizers, safetensors, huggingface_hub, transformer-lens, vllm, peft ; toute autre clé refusée) ; `fichiers_de_la_passe` (objet d'exactement quatre clés, qui sont les CHEMINS RELATIFS au dépôt `donnees/<run_id>/ids-actions-iib-evaluation.npz`, `donnees/<run_id>/textes-actions-iib-evaluation.jsonl`, `donnees/<run_id>/adaptateur-eleve.pt`, `donnees/<run_id>/adaptateur-temoin-jumeau.pt`, chacune portant une empreinte de 64 caractères hexadécimaux) ; `etats_par_lot_evaluation` (liste non vide de lignes à exactement six clés : `adaptateur` « eleve » ou « temoin-jumeau », `condition` « H », « B50 », « B100 » ou « TJ100 », `dose_avant` nombre, `dose_apres` nombre égal à la dose de la condition, `empreinte` 64 caractères hexadécimaux, `lot` entier d'au moins 1 ; lignes rangées par condition dans cet ordre, puis par lot).
