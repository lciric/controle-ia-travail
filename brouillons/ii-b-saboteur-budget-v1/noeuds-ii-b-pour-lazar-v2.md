# Points à trancher avant la course du saboteur à budget — pour Lazar — v2

Écrit le 2026-11-18 vers 20:10 UTC par un rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`). Brouillon scellé, non contre-lu. Remplace la v1 (`noeuds-ii-b-pour-lazar-v1.md`, `66cd18df…`, intacte), après la contre-lecture `docs/notes/barreau8-iib-v1/contre-lecture-ordre-et-devis-iib-v1.md` (`d398bf5c…`). Accompagne l'ordre, brouillon 4 (`ordre-exploratoire-ii-b-v1-brouillon4.md`, `91a592ff776efd4a9cf2293cfee2a837a25b4bee6d33fcff087662cbf2f715c8`) et le devis, brouillon 4 (`devis-ii-b-v1-brouillon4.md`, `08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`).

**En bref.** La course coûte environ 16 dollars attendus, 52,5 au pire, et tient dans ta ligne de 60 dollars. Six points à trancher. Deux d'entre eux (1 et 3) portent sur des conditions écrites dans ta ligne de dépense : **ils n'ont pas de défaut, il faut ton mot exprès**. Sans ce mot, l'ordre n'est pas scellé, le devis n'est pas inscrit, rien n'est créé.

Ta ligne d'accord est `GO-2026-11-10-08` (60 dollars, coupure à 55, échéance le 27 novembre). Elle contient deux sortes de texte, à ne pas confondre :
- **tes mots**, recopiés verbatim (registre des décisions, ligne R-2175, 10 novembre 2026) : « Lancer le saboteur à budget avant le 27, avec l'activité interne enregistrée. C'est une dépense : sans ton mot, rien ne part. Recommandation : oui, confiance 0,55, une fois son code et son devis rendus. : go » ;
- **la lecture écrite par la session mère** (ce ne sont pas tes mots) : la course part « seulement après le code rendu et contre-lu, le devis rendu et inscrit ici en complément, l'ordre exploratoire contre-lu et scellé, les six épreuves de l'oracle passées ».

---

## 1. L'activité interne : enregistrée pendant la course, ou recalculable plus tard

**Décision** : choisir entre enregistrer l'activité interne de l'agent pendant la course (branche A) et garder seulement de quoi la recalculer plus tard (branche B).

**Enjeu** : ta ligne cite la décision « D-4, option (a) ». Son texte, tel quel :
- **tes mots**, registre des décisions, ligne R-2175, 10 novembre 2026, verbatim : « Lancer le saboteur à budget avant le 27, avec l'activité interne enregistrée. C'est une dépense : sans ton mot, rien ne part. Recommandation : oui, confiance 0,55, une fois son code et son devis rendus. : go » ;
- **lecture consignée ce jour-là par la session mère** (pas tes mots) : « saboteur à budget avec activations (GO-2026-11-10-08, plafond 60 USD, après code, devis et ordre contre-lus) ».

La conception de la course et son code font l'inverse : **rien n'est enregistré** ; une garde arrête la course si la configuration en parle. Ce que la course garde : les textes exacts de toutes les actions (au jeton près) et les deux adaptateurs. Avec eux, l'activité se recalcule plus tard par une passe sur une carte. Le résultat est **égal aux arrondis du calcul près, pas au bit près** (autre passe, autre machine).

**Les deux branches** (devis brouillon 4, § 8.1 ; ordres de grandeur, non mesurés) :
- **(A) Enregistrer pendant la course.**
  - Avantage : ta phrase est tenue à la lettre ; une seule location.
  - Coût : environ 0 à 0,9 dollar de plus dans la ligne de 60 (1,7 au pire) ; le pire cas monte à environ 54,2 dollars, sous la coupure de 55, avec 1,3 heure de marge.
  - Inconvénients :
    - Le code, la conception et l'ordre sont à refaire : gardes à changer, capture à écrire, essais, nouvelle contre-lecture. Cela pèse sur le calendrier du 25.
    - Il faut décider d'abord, côté moniteurs, quoi enregistrer (couches, jetons, précision).
    - Le disque compte : 0,7 à 1,9 gigaoctet pour un vecteur par action sur toutes les couches, et des dizaines de gigaoctets s'il faut tous les jetons.
    - Des fichiers d'activité existeraient avant le verdict du test de transfert : la règle de non-lecture tiendrait par discipline seulement.
- **(B) Garder de quoi recalculer.**
  - Avantage : aucun changement de code avant le 25 ; 0 dollar de plus dans la ligne ; la règle de non-lecture tient par construction.
  - Coût : une passe plus tard, sur une location à part, avec son devis et ta ligne à part : environ 4,2 à 4,7 dollars attendus (8,9 à 10,4 au pire).
  - Inconvénients : ta phrase n'est pas tenue à la lettre ; le résultat est égal aux arrondis près, pas au bit ; le modèle de base n'est pas gardé par le programme (il dépend de sa mise à disposition publique) ; une seconde location.

**Recommandation** : aucune. Le choix porte sur le sens que tu donnais à « enregistrée » ; je ne le connais pas.
**Sans défaut : mot exprès.** Ta ligne porte ces mots, et c'est une ligne de dépense. Sans ton mot exprès, consigné au registre des décisions, l'ordre n'est pas scellé, le devis n'est pas inscrit, rien n'est créé.

---

## 2. Si 7b n'est pas créée le 25 novembre

**Décision** : dire ce qu'on fait si la course de confirmation 7b n'est pas créée au plus tard le 25 novembre.

**Enjeu** : la proposition que tu as tranchée (registre des décisions, R-2044, cité par l'ordre brouillon 2) prévoit la création de cette course « après la création de 7b ». Le code refuse toute création sans la ligne de création de 7b au registre des décisions. La dernière commande de création possible sous ta ligne est le **25 novembre à 23:00 UTC** : l'instance rejoue le calendrier à son démarrage et se détruit si le jour a changé. Ta ligne finit le 27. Je ne connais pas l'état de 7b ; la session mère, si.

**Options** :
- **(a) Attendre 7b ; si elle n'est pas créée le 25, laisser passer le 27, et une ligne neuve sera à te demander.**
  - Avantage : l'ordre « 7b d'abord » est tenu ; aucun code ne change.
  - Inconvénient : la course peut ne pas partir sous cette ligne.
- **(b) Lever « 7b d'abord » pour cette course.**
  - Avantage : la course peut partir le 25 quoi qu'il arrive à 7b.
  - Inconvénient : il faut changer le code et la conception, contre-lire, revenir sur ta décision ; deux courses en même temps se disputent l'attention de la session mère.
- **(c) Reporter l'échéance par une ligne neuve, dès maintenant.**
  - Avantage : de la marge pour 7b et pour cette course.
  - Inconvénient : une ligne de dépense neuve ; le « avant le 27 » de ta ligne n'est plus tenu.

**Recommandation** : (a), confiance moyenne.
**Défaut sous 48 heures** : (a). C'est l'état présent : sans mot de toi, rien ne change.

---

## 3. Où passer les six épreuves de l'instrument de mesure

**Décision** : dire si les six épreuves de l'instrument de mesure (« l'oracle ») se passent au début de la course, sur la même carte, ou sur une location préalable à part.

**Enjeu** : ta ligne porte, dans la lecture que la session mère y a écrite (ce ne sont pas tes mots), que la course part « seulement après … les six épreuves de l'oracle passées ». Ces épreuves n'ont tourné que sur un modèle jouet. Le code les joue au début de la course, avant tout épisode de l'agent de test, et s'arrête au premier échec (environ 2,4 heures, 5,6 dollars). Défaut relevé par la contre-lecture : dans le code actuel, la ligne qui annonce le passage des épreuves n'atteint jamais la surveillance. Elle sera corrigée ; d'ici là, le passage se lit sur la première ligne du premier tour de l'agent.

**Options** :
- **(a) Épreuves au début de la course, même carte, arrêt au premier échec ; la mère consigne « six épreuves passées » au vu de la ligne de progrès ; la course continue sans interruption.**
  - Avantage : une seule location ; un échec coûte 5,6 dollars au plus.
  - Inconvénient : on lit cette phrase de la mère comme si « la course » commençait au premier épisode de l'agent, et non à la création de l'instance.
- **(b) Location préalable pour les seules épreuves, puis la course sur une seconde location.**
  - Avantage : lecture la plus stricte de la phrase.
  - Inconvénient : deux créations ; environ 5,6 dollars de plus ; un mode « épreuves seules » à écrire et contre-lire dans le code.

**Recommandation** : (a), confiance moyenne.
**Sans défaut : mot exprès.** C'est une condition écrite dans ta ligne de dépense.

---

## 4. Plafond de la course

**Décision** : garder la variante inscrite, 60 dollars avec coupure à 55, carte A100 seule.

**Enjeu** : ta ligne porte déjà 60 dollars, coupure à 55 (« option B »). Le code refuse tout autre plafond sous cette ligne (vérifié : 55 accepté, 75 refusé). Avec les gardes, la dépense ne peut pas dépasser environ 59,8 dollars.

**Options** :
- **(B) 60 dollars, coupure à 55, A100 seule ; si aucune A100 n'est libre pendant les trois heures de recherche, rien n'est créé et on revient vers toi.**
  - Avantage : déjà accordée ; couvre l'attendu (12 à 20 dollars) et le pire cas (52,5 dollars), avec 2,5 à 5,1 heures de marge.
  - Inconvénient : sans A100 libre, la course glisse.
- **(A) 80 dollars, coupure à 75, repli sur une carte H200 plus chère.**
  - Avantage : la course part même sans A100.
  - Inconvénient : une ligne neuve ; sur H200, seulement 2 heures de marge sur l'attendu haut ; au moindre ralentissement, la minuterie coupe avant la fin (environ 75 dollars pour des résultats partiels).

**Recommandation** : (B), confiance haute.
**Défaut sous 48 heures** : (B). C'est l'état présent : sans mot de toi, rien ne change.

---

## 5. Les essais encore manquants doivent-ils précéder la course ?

**Décision** : fixer quels essais et quelles corrections du code doivent être faits avant la création de l'instance.

**Enjeu** : le code est « autorisable après corrections ». Restent :
- l'essai qui garantit qu'aucun fragment du texte privé de l'agent ne traîne dans le code est inerte ;
- plusieurs gardes neuves n'ont pas d'essai qui les fait échouer exprès ;
- les résultats écrits phase par phase ne sont jamais poussés vers le dépôt : un arrêt en route les perdrait ;
- la ligne qui annonce le passage des épreuves n'atteint pas la surveillance ;
- les étapes de préparation sont à remettre dans un ordre sans cercle (certaines valeurs exigées par la configuration n'étaient prévues qu'après elle) ;
- deux améliorations d'essais, jugées non bloquantes par le développeur.

**Options** :
- **(a) Avant la course : tout sauf les deux améliorations, qui passent après la course et avant toute lecture des résultats.**
  - Avantage : ferme ce qui peut faire perdre de l'argent, des résultats ou faire fuir le texte privé ; tient le calendrier.
  - Inconvénient : un tour de développeur et une vérification courte de plus (processeur, sans dépense).
- **(b) Tout avant la course, améliorations comprises.**
  - Avantage : rien ne reste ouvert.
  - Inconvénient : un tour de plus ; risque sur le 25.
- **(c) Seulement les deux corrections majeures du code ; le reste en réserve.**
  - Avantage : le plus rapide.
  - Inconvénient : un arrêt en route perdrait les résultats partiels payés ; le passage des épreuves ne se lirait que par le repli.

**Recommandation** : (a), confiance haute.
**Défaut sous 48 heures** : (a).

---

## 6. Que devient la branche de la version 2 du code ?

**Décision** : supprimer du dépôt distant la branche `prep/iib-code-v2`, ou la garder gelée.

**Enjeu** : cette branche porte deux courts fragments du texte privé de l'agent de test ; la version 3 en est propre. Le texte privé entier est déjà sur `main`, ainsi que des fragments dans trois fichiers anciens : la branche v2 n'ajoute presque rien à ce qui est exposé. Le dépôt est privé. Toucher au dépôt distant est un nœud à toi.

**Options** :
- **(a) Supprimer la branche du dépôt distant.**
  - Avantage : plus de fragment hors des fichiers du texte privé.
  - Inconvénient : touche au distant ; les objets peuvent rester accessibles un temps ; n'enlève rien de `main`.
- **(b) La garder gelée, exclue de la copie publique, inscrite au registre « qui a lu quoi », interdite au lecteur des sondes.**
  - Avantage : aucun geste sur le distant ; même traitement que la branche v1.
  - Inconvénient : reste lisible par qui a accès au dépôt.
- **(c) La geler maintenant, la supprimer après la course et les lectures.**
  - Avantage : rien ne bouge pendant la course.
  - Inconvénient : deux gestes ; le même nœud à rouvrir.

**Recommandation** : (b), confiance moyenne.
**Défaut sous 48 heures** : (b). C'est l'état présent : sans mot de toi, rien ne change.

---

## Renvoi (pas un nœud de cette note)

Les réglages de la seconde lecture qui reprennent la base textuelle des moniteurs doivent être fixés **avant** le commit du code revu, donc sur le chemin du 25. Ils sont relevés à part, du côté des moniteurs : `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md`. Je ne les fixe pas.
