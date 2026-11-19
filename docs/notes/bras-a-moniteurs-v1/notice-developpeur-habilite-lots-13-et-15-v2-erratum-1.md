# Erratum 1 — notice du développeur habilité, lots 13 et 15, version 2 du code

Corrige `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-lots-13-et-15-v2.md` (`2a8863f9f0d7326512cf213fe19e0708818cecc559cef581228b4d1b71d44d2d`), qui reste telle quelle. Écrit le 19 novembre 2026 par le développeur habilité côté moniteurs, après la fin de l'épreuve par retrait jouée sans le dossier du tokeniseur.

**« En bref », troisième point.**
Avant : « Chaque garde des deux modules, retirée seule, fait échouer un essai : 39 sur 39 pour l'extraction, 28 sur 28 pour le tokeniseur, avec ou sans le dossier du tokeniseur. »
Après : « Chaque garde des deux modules, retirée seule, fait échouer un essai : 39 sur 39 pour l'extraction ; 28 sur 28 pour le tokeniseur **avec** le dossier du tokeniseur du juge, 27 sur 28 **sans** lui. La garde qui survit sans le dossier est « `vocab.json` ≠ vocabulaire de `tokenizer.json` » : elle se trouve dans la fonction qui lit les vrais fichiers, et son artefact (`test_vrai_tokeniseur_altere_arrete`) demande ces fichiers. »

La partie 4 de la notice se lit de même.

**Fait de plus, pour la contre-lecture des lots 14 et 16.** La même épreuve par retrait, jouée sur les modules de ces deux lots en version 1, laisse survivre treize gardes :
- module des moniteurs à modèle de langue (`moniteurs_langue_v1.py`, 38 gardes, 9 survivent) : l'empreinte de la consigne au chargement du fichier (doublée par le contrôle du texte qui suit) ; deux gardes internes du message (action appliquée sans opération ; rendu par proposition ≠ rendu de l'ensemble) ; deux gardes de la lecture chiffre par chiffre (écritures ≠ 0 à 100 ; espérance ou masse hors domaine) ; trois gardes du lecteur du cas B (chiffre en plusieurs jetons ; deux chiffres sur un jeton ; jeton de chiffre mal décodé) ; contexte vide ;
- module des autres moniteurs (`autres_moniteurs_v1.py`, 22 gardes, 4 survivent) : nombre de traits de forme ; trait interdit (l'essai est arrêté par la garde de la liste, placée avant) ; score non fini (l'essai est arrêté plus loin par une fonction gelée) ; tâches des actions ≠ les seize tâches de vérification.

Ces treize gardes recevront un artefact, ou deviendront des assertions marquées « hors R5 » quand elles sont impliquées par une autre, dans la version 2 de chacun des deux modules, avec les corrections de leur contre-lecture.
