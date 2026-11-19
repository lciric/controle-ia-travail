# Journal de la session fille « barreau 8, côté moniteurs » — v2

Session `session_013QMayjujdhnn94JyDTmgSs`, branche `claude/barreau8-cote-moniteurs-v1`. Suite du journal v1 (`dd7840fe3492ef5cf368dfcb1f47de81a54c83324619aadb91b9d4c5271d5d44`), qui n'est pas réécrit. Heures en temps universel. Faits seulement ; aucun résultat du programme. Les seuls chiffres cités viennent d'essais sur modèle jouet et sur données synthétiques.

## 2026-11-18, 23:25Z au 2026-11-19, 05:00Z

### Routine de reprise
- Point 5 : la suite d'essais entière n'a jamais rendu de dernière ligne (une fois coupée par la limite de durée des tâches d'arrière-plan, une fois par un redémarrage du conteneur vers 00:13Z, une fois arrêtée par son identifiant de tâche parce que ses fichiers temporaires, environ 20 Go, avaient rempli le disque vers 00:40Z). La mère en a dispensé la session (écart à la routine déclaré par elle, R-3565). Suite ciblée jouée à la place sur seize fichiers d'essais des sondes, du préenregistrement, du scellement et du manifeste : « 263 passed, 1 warning in 144.03s (0:02:24) ».
- Point 2 : non fait, confirmé par la mère (le mandat prime).

### Refus d'outil, tous rendus à la mère avec leur texte exact, aucun rejoué
1. 23:47Z, conductrice : poussée de la branche refusée par le classifieur du mode automatique (« [Destructive or Unwanted Actions] »), après un gel des poussées demandé puis levé par la mère. Depuis, AUCUNE poussée : tout le travail de la session n'existe que sur le disque du conteneur. La mère a porté le refus à Lazar ; aucun mot de Lazar tapé ici à l'heure de ce journal.
2. Vers 00:05Z, premier contre-lecteur : commande refusée par le classifieur (« [Unauthorized Access] ») ; elle cherchait dans l'ordre du saboteur hors des plages permises. Rien d'affiché selon lui. Vérification reprise par un contre-lecteur neuf, accordée par la mère.
3. Vers 01:27Z et 01:45Z, les deux développeurs : attente par temporisation au premier plan bloquée par le cadre d'exécution. Cause : un message de la conductrice avait basculé leur commande d'essais en arrière-plan. Reprise accordée par la mère (R-3581), essais relancés au premier plan.

### Texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne »
- Quatorze brouillons, tous scellés avec leur compagnon sous `brouillons/barreau8-lecture-sondes-v1/`, chacun avec sa note de différences ; rédacteur : un agent sur Fable 5.2 ; treize rapports de contre-lecture par des agents sur Opus 5.5, dont huit agents neufs successifs.
- Texte jugé prêt : `prereg-lecture-sondes-barreau8-v1-brouillon14.md`, `5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891`. Contre-lecture finale : `contre-lecture-brouillon14-v1.md`, `d7d688f7bf5c5c39dae902f886bb9c4c8417697f563d8e60cc23a495d8f4341e`, conclusion « PRÊT : le brouillon 14 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». Deux marqueurs restants, lignes 76 (entropie racine des graines, tirée par la mère) et 442 (entrée de la contre-lecture finale). La mère scelle ; la conductrice ne scelle pas.
- Décisions appliquées par anticipation par la mère sous GO-2026-11-18-61 et portées par elle à Lazar, figées par le scellement : trois sondes figées à la couche 15 (tromperie, enjeux élevés, dissimulation), la sonde du domaine n'ayant jamais été scellée ; passe aux couches 7, 15 et 23 ; sonde « porteuse » par deux contrastes positifs, « lit aussi le réglage fin seul » en réserve ; lectures du dommage et de la diffusion exploratoires, états seuls ; texte scellé avant le code ; passe conduite par le côté exposé ; livraison d'au plus 2 Go : scores par action et scores par jeton des neuf sondes, sous-échantillon d'activité brute (1 502 781 440 octets au pire pour les quatre tableaux) ; essai de la chaîne de lecture par cinq actions sur dix étiquetées dans chaque tâche, avec égalité exacte des deux chemins de lecture du score.
- Choix de routine de la conductrice, signalés à la mère : plancher haut en réserve et non en défaut ; les deux lignes de code du registre citent chacune un bordereau du code scellé ; trois conditions d'ordre du registre ; une tâche réduite à une classe dans l'essai de la chaîne reste dans le jeu ; refus si le nom de la course diffère entre la trace de la passe et l'extrait des états.

### Codes, sous `src/controle_ia/barreau8_moniteurs/`, chacun avec essais et notice, versions antérieures scellées et intactes
- Passe de recalcul, version 5 : `passe_recalcul_v5.py`, `a5eeef6203b558dbc0c1b58085d2dd4d13617a7c76e9aa374aa224304b19759f` ; essais sur modèle jouet : « 103 passed ».
- Lecture des sondes, version 5 : `lecture_sondes_v5.py`, `aa1476fd6bf6bb5536fba0c16d2aa481393bf408fe68825d3b7987359666e139` ; essais sur données synthétiques : « 171 passed ».
- Contre-lectures par un autre modèle (Opus 5.5) et trois essais d'intégration, sous `docs/notes/barreau8-cote-moniteurs-sorties-v1/` ; le troisième (passe version 5, lecture version 4) : rien de bloquant, de bout en bout par les commandes sur le jouet.
- Non éprouvé : le chemin réel de la passe (carte, modèle, jetoniseur, vrais fichiers de sondes) ; les tailles réelles ; la recette de puissance entière ; la lecture version 5 contre une livraison de la passe (elle ne diffère de la version 4 que par la portée d'un contrôle).

### Autres pièces
- Devis de la passe, brouillon 2, et projets de mandats du lecteur et du juge, brouillon 1 : `docs/notes/barreau8-cote-moniteurs-sorties-v1/` ; fondés sur le brouillon 6 du texte, à réaligner sur le texte scellé ; la notice de la passe exige maintenant environ 24 Go de mémoire vive.
- Incident : disque plein vers 00:40Z, réglé par la suppression des fichiers temporaires des essais et du cache d'installation ; fichiers scellés vérifiés intacts.

## Reste
Poussée de la branche (attend un mot de Lazar tapé ici ou une règle de permission) ; scellement par la mère ; après le scellement : bordereaux du code et contrôle de conformité des deux codes au texte scellé ; devis de la passe et mandats réalignés.
