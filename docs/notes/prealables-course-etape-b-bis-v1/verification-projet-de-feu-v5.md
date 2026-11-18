# Vérification courte du projet de feu version 5 de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) — v1

**Verdict : « à corriger légèrement ».** Les sept corrections de la contre-lecture (C1 à C7) et les onze points mineurs sont portés, et justes, sauf deux bémols (C5 : une seule lecture « course absente » détruisait encore ; C2 : le geste 14 ne vérifiait pas que la machine créée serait lisible ensuite). Quatre points sont à corriger, tous de texte et circonscrits : recharges (champ 3, réserve 11), échéance de l'accord de l'opérateur, deux contrôles du geste 14, verdict « absente ». **Une version 6 est écrite et scellée** (`projet-de-feu-v6.md`) ; elle remplace la version 5, laissée intacte. La version 6 doit être relue par un autre lecteur neuf, **sur sa seule liste des changements** : j'en suis l'auteur et je ne peux pas la contre-lire (règle R2).

- **Lecteur** : sous-agent neuf, qui n'a écrit aucune des pièces (ni texte scellé, ni chaîne, ni projets de feu 3 à 5, ni contre-lectures, ni mesures).
- **Date (`date -u`)** : 2026-11-18, de 07:38Z à 07:55Z environ. Processeur seulement.
- **Pièces lues** : `projet-de-feu-v5.md` (`1846b3091a177dce6bd92734f7e86ca755c51c7fdef568b899574952e5055a05`, 997 lignes, empreinte vérifiée), `projet-de-feu-v4.md` (`92b1502b…`) et `contre-lecture-projet-de-feu-v4.md` (`98bedba8…`) (empreintes vérifiées), `scripts/amorce_bbis_v6.sh` (`26f954e9…`), `scripts/lancer_bbis_v6.sh` (`3224ce14…`), `scripts/lancer_repetition_bbis_v3.sh` (sous-commande `credit`), `.claude/hooks/garde_calcul.py` (`73be0638…`), `registres/go.md` (lignes GO-2026-11-14-09, -11-16-06, -11-18-06, -07, -08, -18), `registres/decisions.md` (R-3245, R-3246, R-3248).
- **Cloisonnement tenu** : aucun résultat de T0.7, de l'étape B ni de l'étape B bis ouvert ; rien sous `diag/`, `runs/`, `donnees/` ; aucune clé lue ni affichée ; aucun appel au loueur ni à un service payant ; aucune instance créée ou détruite ; aucun commit, aucune poussée ; rien dans `registres/`.
- **Écrit** : ce fichier, `projet-de-feu-v6.md` et leurs compagnons d'empreinte. Rien d'autre sous le dépôt. Essais dans le bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/verif-feu-v5/`.

---

## 1. Corrections demandées par la mère (à porter, non à discuter) — portées dans la version 6

1. **Recharges (champ 3, réserve 11 et alentours).** Le champ 3 et la réserve 11 de la version 5 disaient « plus aucune recharge » (GO-2026-11-18-07). Cet ordre a pris fin (GO-2026-11-18-18, R-3235) ; Lazar garde la recharge automatique allumée (R-3245) et a ajouté 25 EUR à la main (R-3246). Mis à jour : champ 2 (fin de l'ordre), champ 3 (recharges ; la condition de départ reste le relevé du geste 8, jamais une recharge à venir), § 1, § 6 (dernier point), réserve 11. La recharge automatique ne protège pas la course : elle se déclenche sous 5 USD, la course se détruit sous 8 USD. Les citations de Lazar sont recopiées à l'identique, fautes comprises.
2. **GO-2026-11-16-06 échoit aujourd'hui** (`registres/go.md`, l. 347). Dit au § 0 condition 5 et au § 1. La création est refusée **par programme** (geste 14) après 2026-11-18T22:59:59Z (lecture prudente : fin du jour de Paris). L'accord couvre « création, et destruction de cette machine si elle échoit à l'opérateur » : le suivi au-delà de cette heure est repris par la mère, ou Lazar renouvelle (alors feu neuf, R12). Le crochet ne contrôle pas cet accord (il ne lit que les numéros cités dans la commande, ici GO-2026-11-14-09, valide jusqu'au 2026-11-22) : sans le contrôle de programme, rien n'empêchait une création après minuit.
3. **Choix gardés** : tolérance de 120 secondes de l'adoption par l'étiquette ; maintien de 12 heures des arrêts qui laissent des résultats sur le disque. Non touchés.

## 2. Autres corrections, avec preuve

4. **Le geste 14 pouvait créer une machine que le tour ne saurait pas relire.** Le geste 14 ne vérifie ni `plafond.sh` ni `temoin.sh` ni que le geste 13 s'est bien achevé. Preuve : les gestes 15 (b), 16, 17, 19 et 23 les lisent par `. "$TD/plafond.sh"` / `. "$TD/temoin.sh"` dans une chaîne `&&` ; fichier absent, la chaîne s'arrête avant toute lecture, l'opérateur n'a plus de verdict et la convention commande la destruction : **une machine saine détruite, la dernière course consommée**. Correction (version 6) : le geste 14 exige, dans sa liste, `offre-retenue.sh`, `plafond.sh`, `temoin.sh` non vides et la marque `geste-13-conforme`, écrite par le geste 13 seulement après ses quatre contrôles. Rejoué : chacun des quatre fichiers ôté (et la marque) : « AUCUNE CREATION TENTEE », 0 création, le diagnostic dit lequel manque.
5. **Une seule lecture « course absente, témoin présent » détruisait.** Commande L, gestes 16, 17, 19 : verdict `ABSENTE` (code 4) commandait aussitôt les gestes 22 et 23. Or une instance créée à l'instant peut ne pas encore figurer dans la liste du loueur (cohérence différée, jamais observée par cette chaîne : réserve). C'est exactement le cas « lecture passagère » que C5 voulait écarter. Correction (version 6) : `ABSENTE` est une lecture sans verdict, comptée par le programme (`awk` étendu à `ABSENTE`, aux deux endroits), trois au plus à une minute d'écart, puis destruction. Rejoué : trois lectures `ABSENTE` de suite, compteur 1, 2, 3 ; un verdict conforme remet à 0.
6. **Motif `'premier tour'`** : le geste 7 (a) l'emploie, la commande O dit n'accepter que quatre motifs, dont il ne fait pas partie. Ajouté à la liste.
7. **Cas « zéro instance » du geste 15 (b)** : `a-detruire.txt` est écrit vide et le geste ne se relit pas (`test ! -e`, et le programme écrit sans réécrire) ; une création retardée n'aurait pas de relecture. Dit, avec le recours : relecture de la mère au rappel de création plus 30 minutes.
8. **« Absence non prouvée » deux fois (geste 23)** : l'instance reste vivante, sans autre issue écrite que « nœud ». Ajouté : la mère la détruit elle-même ; la minuterie et le rappel à l'échéance sont des recours de plus.
9. **Réserve 13** : la clé `driver_version` de la fiche d'instance n'a jamais été lue ; une forme inattendue donne `HORS_BORNES` à la première lecture et commande la destruction d'une machine saine. Dit, avec le garde-fou : nœud avant toute destruction si le premier relevé du geste 16 montre une forme inattendue.
10. **Condition 7 et § 15** : la version 6 est relue par un lecteur neuf sur sa liste de changements ; le § 15 garde les chiffres de la version 5 et le dit.

Aucun programme n'est changé : les trois empreintes du geste 5 sont inchangées. Seule l'empreinte du préambule (geste 1) change (noms `-v6`) : `ca96724887e478ffbaef7926d78f5a537fa1cca1e8731e45ffec5a337754ef64`, recalculée sur le texte et retrouvée par le rejeu.

## 3. Les sept corrections et les onze points mineurs de la contre-lecture : portés ?

| point | porté | juste | preuve |
|---|---|---|---|
| C1 (geste 2 (a) arrêtait un opérateur sain) | oui | oui | Dans ma session (sous-agent), `CLAUDE_PROJECT_DIR` rend « vide » alors que le crochet est chargé : il a refusé deux de mes commandes. (a) n'est plus qu'un relevé. |
| C2 (fenêtres du geste 14) | oui | oui, avec bémol (n° 4 ci-dessus) | Rejoué avec un faux outil : commande de plus de 30 minutes, relevé de plus d'une heure, clé absente, ligne courte déjà présente, création déjà tentée, ligne imprimée altérée, fenêtre dépassée **et** ligne courte présente : 0 création chaque fois, « AUCUNE CREATION TENTEE PAR CET APPEL » + diagnostic. Cas sain : 1 création ; un second jeu : 0 ; commande O après la création : refusée. |
| C3 (reprises sous des noms neufs) | oui | oui | Dossier par tour, commande O : tours 1 à 3 ouverts, quatrième refusé, aucun tour après une création tentée (`find … t-creation.sh`). |
| C4 (ligne du geste 20 pour une marche qui tombe) | oui | oui | Rapprochement avec `amorce_bbis_v6.sh` : les textes « BBIS ARRET » cités (poussée impossible, branche locale, ajout, fichier de plus de …, commit, marche : code N, arrêt écrit, garde de débit) existent tels quels ; sur `marche : code N`, les traces sont poussées avant l'arrêt. |
| C5 (lecture passagère) | oui | oui, avec bémol (n° 5) | `prix-relu.sh` écrit une fois (empreinte inchangée après 8 lectures dont échec, liste vide, prix nul, prix au-dessus du plafond) ; liste vide : « INCOMPLETE » code 5 ; témoin présent : « ABSENTE » code 4 ; prix nul : code 6 ; plafond : code 3. Crédit illisible au geste 19 : « CREDIT ILLISIBLE » sans destruction. |
| C6 (planchers de crédit) | oui | oui | Rejoué par programme (geste 8) : (20,00 ; 0) insuffisant ; (24,28 ; 0) suffisant ; (24,27 ; 0) insuffisant ; (19,99 ; 0) insuffisant ; (40,14 ; 1,22) suffisant ; (40,13 ; 1,22) insuffisant ; crédit « abc », absent ou négatif : insuffisant ; débit illisible : insuffisant. Dans les cas insuffisants, `credit-heure.sh` n'est pas écrit : le geste 14 ne peut pas créer. |
| C7 (minuterie / filet de la mère) | oui | oui | Heures des deux rappels imprimées au geste 16 (création plus 30 minutes ; échéance plus 15 minutes) ; § 5 et § 6 disent que les pires cas supposent la minuterie armée. |
| m1 (geste B.3 à la lettre) | oui | oui | Geste 3 (b) rejoué sur un feu substitut et un registre de décisions substitut : 13 lignes, « GESTE 3 CONFORME ». |
| m2 (heure de rédaction) | oui | oui | Fichier daté de 07:35:58Z, fin de rédaction annoncée 07:35:52Z. |
| m3 (jetons factices) | oui | oui | Sortie du geste 6 (c) coupée à 80 caractères : pas de jeton ; leur place en fin d'`--env` comptée par programme. |
| m4 (geste 5) | oui | oui | Chemins absolus, un programme par appel ; les trois empreintes retrouvées (`2d32e1ac…`, `3e40e355…`, `1fa46d02…`). |
| m5 (étiquette déjà portée, débit) | oui | oui | Étiquette déjà portée au geste 7 : code 3, aucune écriture ; aucune autre instance : code 2 ; débit des seules instances « running » (1,22 sur 1,22 + 0,05). |
| m6 (code de la garde de dépense) | oui | oui | Cumul de 40,57 USD : « GARDE DE DEPENSE : REFUS AVEC ORDRE DE DESTRUCTION » ; cas sain : « ACCEPTEE ». |
| m7 (qui répond aux autorisations) | oui | oui, non éprouvé | Texte seulement : toute demande refusée ou expirée est un arrêt. Voir § 5. |
| m8 (fichiers `.err`) | oui | oui | Jamais affichés ; effacés au geste 24 (24 fichiers effacés dans mon rejeu ; aucune liste brute ni réponse de création restante). |
| m9 (garde de 12 heures, instance encore en marche) | oui | oui | Texte (commande L dès l'arrêt, puis toutes les heures ; « running » ou « loading » : gestes 22 et 23). |
| m10 (réponse illisible, instance saine) | oui | oui | Rejoué : illisible ou `success` faux avec une instance saine créée après la commande, sur la bonne machine : adoptée ; deux instances, zéro, créée 600 s avant, autre machine, témoin absent, ancienne instance étiquetée en plus : non adoptée ou sans verdict, `a-detruire.txt` correct. |
| m11 (journal) | oui | oui | Journal conforme : « JOURNAL CONFORME » ; doublon de la ligne minuterie, ligne REFUS, lecture du journal en échec : « NON CONFORME ». Réserve 13 dit la limite. |

## 4. Ce que j'ai rejoué (faux outil du loueur, aucun appel réseau, état fabriqué)

- Les 32 blocs de commandes du texte (version 5, puis version 6) sont tirés par programme, jamais retapés ; substitutions déclarées : dossier d'envoi et outil vers le bloc-notes, feu et registre des décisions vers des substituts. Le faux outil lit et écrit des fichiers d'état ; il garde un journal de ses appels (créations, destructions).
- **Crochet de garde** : les 32 blocs, passés comme données au code de décision du crochet (jamais exécutés), sont **acceptés** (code 0), dont les blocs 6 (c), 13 et 14 (qui portent `vastai create`) ; le chiffre qui manquait à la version 5 (« acceptation par le crochet non rejouée »). Vrai pour les deux versions.
- Gestes 1, 2 (c), 3 (a) et (b), 5, 6 (a), (b), (c), 7 à 16, 18, 19 (b), 22 à 24, commande O, commande L : tous joués ; chemin sain de bout en bout (création fabriquée, lecture, relecture, journal, suivi, destruction fabriquée, absence prouvée, témoin disparu puis témoin neuf).
- Calcul d'empreinte : préambule version 5 `d33b8100…` (égale au texte) ; version 6 `ca967248…`.
- Version 6, gestes modifiés : 13, 14 (quatre refus neufs + cas sain + les refus de la version 5), 15 (a), 16, commande L (compteur et `ABSENTE`), crochet sur les 32 blocs.
- Lanceur et amorce **réels** (lecture seule) : `bash scripts/lancer_bbis_v6.sh commande …` sur l'offre fabriquée et sur l'offre issue de la recherche fabriquée (commit de la course `438a9c52…`, `git fetch` et `git ls-remote` en lecture seule) : ligne imprimée égale à la ligne reconstruite (geste 13).
- Geste 4 : non joué (il installerait l'outil réel). Syntaxe de tous les blocs vérifiée par `bash -n`.

## 5. Ce que je n'ai pas pu vérifier

- Tout ce qui exige le loueur : forme réelle des réponses (création, liste, crédit, recherche, journal), clés `start_date`, `machine_id`, `driver_version` de la fiche d'instance, comportement de `-y`, de `logs`, délai d'apparition d'une instance dans la liste.
- **Les demandes d'autorisation** : `.claude/settings.json` n'autorise d'avance que l'étiquette de la répétition ; l'opérateur sous-agent rencontrera une demande aux gestes 6, 13, 14 (texte de création). Qui y répond, je ne l'ai pas vu. Le feu dit : refusée ou expirée = arrêt.
- La présence des trois clés dans l'environnement de l'opérateur (je n'ai pas lu l'environnement) ; le geste 14 la teste avant de créer.
- Le geste 4 (installation de l'outil 1.8.3, option `-y`, `unshare`).
- Le « modèle B » de la condition 5 (disponible le 21 novembre) ; la lecture de l'échéance de GO-2026-11-16-06 comme fin du jour de Paris (22:59:59Z) est une lecture prudente de ma part, à confirmer par la mère ; Lazar peut la renouveler.
- Les accords cités aux champs 1 et 2 au-delà de leur présence au registre.

## 6. Refus du crochet pendant ma vérification (non contournés)

Deux de mes commandes ont été refusées par le crochet de garde de calcul, comme le prévoit le feu : (1) une commande d'essai qui portait le motif d'arrêt du cas témoin (« R10 — arrêt par motif de ligne de commande interdit ») ; (2) une commande d'essai dont le texte citait `vastai create` avec le numéro de GO-2026-11-16-06 (« est un GO de type 'décision', pas calcul »). Je ne les ai ni reformulées, ni découpées, ni déplacées dans un fichier : ces deux essais ne sont pas faits. Ils confirment, par comportement, que le crochet est chargé dans une session de sous-agent alors que `CLAUDE_PROJECT_DIR` y est vide (C1). Observation utile à l'opérateur : le crochet lit le **texte** de la commande ; toute commande qui cite à la fois `vastai create` et un numéro d'accord autre que GO-2026-11-14-09 est refusée.

## 7. Questions ouvertes pour la mère

- Lire l'échéance de GO-2026-11-16-06 à 22:59:59Z (fin du jour de Paris) ou à 23:59:59Z : à confirmer ; la version 6 retient la lecture prudente. Elle se change dans le texte du geste 14 (valeur d'une date) et au § 0 condition 5 ; la création est prévue vers 09:30Z.
- Si une offre disparaît entre la recherche et la création (cas courant chez ce loueur), le geste 15 (b) déclare « la course consommée » et la commande O refuse tout tour neuf après une création tentée : la mère jugera. Ce n'est pas un défaut de sécurité.
- La version 6 est de ma main : un autre lecteur neuf la relit sur sa liste de changements (`diff -u projet-de-feu-v5.md projet-de-feu-v6.md`).
