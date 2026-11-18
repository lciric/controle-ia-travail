# Points à trancher avant la course du saboteur à budget — pour Lazar — v1

Écrit le 2026-11-18 vers 19:30 UTC par un rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`), sous le mandat `docs/notes/barreau8-iib-v1/mandat-redacteur-ordre-exploratoire-iib-v1.md` (`55b1e348…`). Brouillon scellé, non contre-lu. Il accompagne l'ordre exploratoire, brouillon 3 (`ordre-exploratoire-ii-b-v1-brouillon3.md`, `eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f`) et le devis, brouillon 3 (`devis-ii-b-v1-brouillon3.md`, `016979ba01926f08be8ac243df75b716cf49ea63ea01e16dedd4302e61f991d4`).

**En bref.** La course du saboteur à budget coûte environ 16 dollars attendus, 52,5 au pire sur la carte prévue ; elle tient dans ta ligne de 60 dollars. Cinq points à trancher ; le deuxième est une divergence entre le texte de ta ligne d'accord et ce que le code fait.

Ce qu'est la course : une seule instance de location, une carte A100, qui fabrique un agent de test discret et mesure ce qu'il fait. Course exploratoire, non opposable : rien n'entre dans la porte de sortie de la phase 0. Ta ligne d'accord est `GO-2026-11-10-08` (60 dollars, échéance le 27 novembre).

---

## 1. Plafond de la course

**Décision** : confirmer la variante « 60 dollars, coupure à 55, carte A100 seule ».

**Enjeu** : ta ligne inscrite porte déjà 60 dollars avec coupure à 55 (« option B »). Le code refuse tout autre plafond sous cette ligne : je l'ai vérifié sur processeur (55 accepté, 75 refusé). L'autre variante demanderait une ligne neuve.

**Options** :
- **(B) 60 dollars, coupure à 55, A100 seule ; si aucune A100 n'est libre pendant trois heures, rien n'est créé et je reviens vers toi.** Avantage : déjà accordée ; couvre l'attendu (12 à 20 dollars) et le pire cas sur A100 (52,5 dollars, hôte deux fois plus lent), avec 4,5 heures de marge au pire prix. Inconvénient : si aucune A100 n'est libre, la course glisse.
- **(A) 80 dollars, coupure à 75, repli sur une carte H200 plus chère si aucune A100 n'est libre.** Avantage : la course part même sans A100. Inconvénient : ligne neuve à accorder ; sur H200, la marge n'est que de 2 heures sur l'attendu haut ; au moindre ralentissement, la minuterie coupe avant la fin (environ 75 dollars pour des résultats partiels).

**Recommandation** : (B), confiance haute.
**Défaut sous 48 heures** : (B).

Dates retenues dans le devis (pour information) : dernier jour de création le **25 novembre** ; la minuterie de l'instance coupe d'elle-même le **27 à 22 h UTC**, deux heures avant la fin de ta ligne, pour que les résultats soient poussés et l'instance détruite à temps. Une création le 25 au soir finit le pire cas le 27 vers 9 h UTC.

---

## 2. « Avec l'activité interne enregistrée » : ta ligne et le code divergent

**Décision** : dire si la course doit **enregistrer l'activité interne de l'agent** pendant qu'elle tourne, ou seulement **garder de quoi la recalculer** plus tard.

**Enjeu** : ta ligne d'accord dit « Lancer le saboteur à budget avant le 27, **avec l'activité interne enregistrée** ». La conception de la course et le code font l'inverse : **aucune activité interne n'est enregistrée** ; une garde arrête la course si la configuration en parle. La course garde en revanche les textes exacts de toutes les actions (au jeton près) et les deux adaptateurs : l'activité interne se recalcule de façon exacte par une passe plus tard, sur une carte. La conception justifie ce choix par la règle « aucune lecture des sondes avant le verdict du test de transfert » et par un préenregistrement à écrire à part. Je n'ai pas lu la décision citée dans ta ligne (« D-4, option (a) »), ni ce que la mère en a compris.

**Options** :
- **(a) Garder le code tel quel : rien n'est enregistré pendant la course ; tout ce qu'il faut pour recalculer l'activité est gardé et poussé.** Avantage : aucun changement de code avant le 27 ; respecte la règle de non-lecture des sondes ; rien de plus à contre-lire. Inconvénient : ta phrase est lue comme « recalculable » et non « enregistrée » ; une passe de carte plus tard, sur devis et accord à part (non chiffrée ici).
- **(b) Ajouter l'enregistrement pendant la course.** Avantage : conforme à la lettre de ta ligne ; pas de seconde location. Inconvénient : code à changer (garde à retirer, essais neufs, contre-lecture neuve) ; plus de disque et de temps ; risque réel de manquer le 27.
- **(c) Ajouter une passe d'enregistrement à la fin de la même instance, après l'évaluation.** Avantage : une seule location ; rien ne change pendant la fabrication de l'agent. Inconvénient : même travail de code que (b), un peu moins de risque ; la course s'allonge.

**Recommandation** : (a), confiance moyenne (je ne sais pas ce que tu voulais dire par « enregistrée »).
**Défaut sous 48 heures** : (a), la mère consignant au registre que ta ligne est lue ainsi.

---

## 3. Les essais encore manquants doivent-ils précéder la course ?

**Décision** : fixer quels essais du code doivent être faits avant la création de l'instance.

**Enjeu** : le code est « autorisable après corrections » (vérification courte du code v3). Restent :
- l'essai qui doit garantir qu'aucun fragment du texte privé de l'agent ne traîne dans le code est **inerte** (il ne vérifie rien) ;
- plusieurs gardes neuves n'ont pas d'essai qui les fait échouer exprès (sur un cas fabriqué) ;
- **défaut que j'ai relevé en lisant le script qui démarre l'instance** : les résultats écrits phase par phase (étalonnage, chaque tour) ne sont **jamais poussés** vers le dépôt (le dossier des données est ignoré et le script n'ajoute de force que les fichiers de fin de course). Si la course s'arrête en route, ces résultats restent sur l'instance et disparaissent à sa destruction. Non éprouvé par un essai ; correction de deux lignes plus un essai ;
- deux améliorations d'essais signalées par la contre-lecture, jugées non bloquantes par le développeur : un espion plus fort sur les appels aux modules des moniteurs, et deux cas de plus pour la seconde lecture.

**Options** :
- **(a) Avant la course : l'essai de non-fuite rendu actif, les essais d'échec manquants, la correction du défaut de poussée ; les deux améliorations après la course, avant toute lecture des résultats.** Avantage : ferme tout ce qui peut faire perdre de l'argent ou fuir le texte privé ; tient le calendrier. Inconvénient : un tour de développeur et une vérification courte de plus (processeur, sans dépense).
- **(b) Tout avant la course, améliorations comprises.** Avantage : rien ne reste ouvert. Inconvénient : un tour de plus ; risque sur le 25.
- **(c) Seulement les deux corrections majeures ; le défaut de poussée laissé en réserve.** Avantage : le plus rapide. Inconvénient : un arrêt en route perdrait les résultats partiels déjà payés.

**Recommandation** : (a), confiance haute.
**Défaut sous 48 heures** : (a).

---

## 4. Où passer les six épreuves de l'oracle et les essais sur le vrai découpage en jetons

**Décision** : dire si les six épreuves de l'instrument de mesure (« l'oracle ») se passent au début de la course, sur la même carte, ou sur une location préalable à part.

**Enjeu** : ta ligne dit que la course part « seulement après … les six épreuves de l'oracle passées ». Elles n'ont tourné que sur un modèle jouet. Le code les joue au début de la course, avant tout épisode de l'agent de test, et s'arrête au premier échec (environ 2,4 heures et 5,6 dollars dépensés). Par ailleurs, quatre essais dépendent du vrai découpage en jetons du modèle et n'ont jamais tourné (coupure du texte avant le nombre, arrêt au saut de ligne, réécriture du nombre, longueur du texte privé en jetons) ; ils n'ont besoin que des fichiers de découpage, pas du modèle.

**Options** :
- **(a) Épreuves au début de la course, même carte ; arrêt au premier échec ; la mère consigne « six épreuves passées » quand la ligne de progrès l'annonce, et la course continue sans interruption. Les quatre essais de découpage tournent avant, sur processeur, si la mère obtient les fichiers de découpage sans dépense ; sinon par un court script au démarrage de l'instance.** Avantage : une seule location ; un échec coûte 5,6 dollars au plus. Inconvénient : lecture de ta phrase où « la course » commence au premier épisode de l'agent, pas à la création de l'instance.
- **(b) Location préalable pour les seules épreuves, puis la course sur une seconde location.** Avantage : conforme à la lettre la plus stricte de ta phrase. Inconvénient : deux créations ; environ 5,6 dollars de plus pour la location préalable (devis, § 4 et § 8), selon que la course refait ou non l'étalonnage ; un mode « épreuves seules » à écrire et contre-lire dans le code.

**Recommandation** : (a), confiance moyenne.
**Défaut sous 48 heures** : (a).

---

## 5. Que devient la branche de la version 2 du code ?

**Décision** : supprimer du dépôt distant la branche `prep/iib-code-v2`, ou la garder gelée.

**Enjeu** : cette branche porte, dans un fichier d'essai et dans un rapport, deux courts fragments du texte privé de l'agent de test (constat bloquant de la contre-lecture du code v2) ; la version 3 en est propre. Le texte privé entier est par ailleurs déjà sur `main` (ses deux fichiers), et trois fichiers anciens de `main` en portent aussi des fragments (vérification courte, § 5.2) : la branche v2 n'ajoute presque rien à ce qui est exposé. Le dépôt est privé. Le risque réel est qu'un futur lecteur des sondes tombe sur ces fragments sans le savoir. Toucher au dépôt distant est un nœud à toi.

**Options** :
- **(a) Supprimer la branche du dépôt distant.** Avantage : plus de fragment hors des fichiers du texte privé. Inconvénient : touche au distant ; les objets peuvent rester accessibles un temps ; n'enlève rien de `main`.
- **(b) La garder gelée, exclue de la copie publique, inscrite au registre « qui a lu quoi », et interdite au lecteur des sondes (déjà écrit dans l'ordre).** Avantage : aucun geste sur le distant ; même traitement que la branche v1 (gelée sans réécriture). Inconvénient : la branche reste lisible par qui a accès au dépôt.
- **(c) La geler maintenant, la supprimer après la course et les lectures.** Avantage : rien ne bouge pendant la course. Inconvénient : deux gestes ; même nœud à rouvrir.

**Recommandation** : (b), confiance moyenne.
**Défaut sous 48 heures** : (b).

---

## Renvoi (pas un nœud de cette note)

Les réglages de la seconde lecture qui reprennent la base textuelle des moniteurs (choix du portage complet ou de la forme actuelle, liste des traits, unité de longueur, méthode d'ajustement) doivent être fixés **avant** la course, car le code les lit dans la configuration de la course. Ils sont relevés à part par un agent du côté des moniteurs : `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md`. Je ne les fixe pas ; l'ordre les laisse en marqueur nommé.
