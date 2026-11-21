# Contrôle borné de la conception v5 du véhicule NA-1 — v1

- Contre-lecteur, modèle O : le même que pour les versions v1 à v4 (règle R2). Je n'ai écrit ni la conception, ni la v9, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 08:09:52Z, après la lecture, avant l'écriture.
- Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt. Je n'ai ouvert aucune branche de quarantaine ni de matière première.
- Aucun refus de permission, de classifieur ni de garde rencontré.
- Objet : les seuls points de mon contrôle de la v4 (`3fda0db5…`), plus le choix de la mère de 08:04Z (voie 1 pour A3).

## Pièces

| pièce | empreinte | contrôle |
|---|---|---|
| conception v5 (CO5) | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` | égale au compagnon et au mandat |
| différentiel v4 → v5 | `99f6e8c3b5408ce8162d78fe66b1c8cb6ca9ba6cfe2b70ceb076fc9589dae96b` | égale au compagnon ; lu en entier (225 lignes) |
| rapport v5 | `8772321d6dba07e21643fda5e2b1965ee7fa92a1fd4059430a5a389469afc6a5` | égale au compagnon |
| table v5 | `b424a34739b833d1ffbe6f3fb8f0ba87a20d3e141a3acffea9cbdda81e4d345a` | égale au compagnon |

## Verdict

**Conforme. Le lot 6 peut partir à son tour.** Une retouche de lettre reste à porter : la sixième ligne de la pièce de relevés (point 4). Elle ne touche pas le lot 6. Elle doit être portée avant les mandats du lot 8 (le lanceur, qui lit la pièce) et du lot 10 a (qui en dépend).

## 1. La voie 1 pour A3 : écrite fidèlement, la formule retirée

- **Retirés** : la formule 1 + ⌈150 / c⌉ et la valeur d'un million. CO5, § 2.13 donne les deux raisons de mon contrôle : un appel en erreur peut coûter zéro (`noyau_v56.py`, l. 170), et un million était une désactivation qui ne disait pas son nom. Aucune occurrence active ne reste ; seul l'historique des versions les nomme (l. 9).
- **A3, échecs consécutifs** : « désactivée pour tous les rôles de cette course ».
  - La raison est écrite : V9, l. 97 et 101 ; aucun seuil d'arrêt sur M6.
  - Mise en œuvre : une valeur hors d'atteinte, écrite à l'additif sous le nom de désactivation.
  - Vérifiée au départ : la configuration est refusée si la valeur diffère.
- **A14** : désactivée par écrit de la même façon (part à 1, sous le nom de désactivation, vérifiée au départ), non plus « inerte ».
- **Le délai d'A3 reste actif**, aligné sur 3 600 s.
- **La garde de remplacement porte sur les refus écrits, non sur M6** :
  - proposeur : onze refus écrits dans une génération déclenchent un arrêt nommé de course, numéroté à l'additif ;
  - portier : l'arrêt n° 5 ;
  - juge : un rapport, sous I1 ;
  - le compte repart de zéro à chaque génération.
- **Épreuves** (§ 6.2) :
  - désactivation : la valeur héritée ou toute autre est refusée par son nom ; mutation « vérification au départ retirée » ; plus de onze réponses sans texte de suite pour chaque rôle sans arrêt ; délai lu entre 1 800 et 3 600 s, coupé au-delà ;
  - garde de remplacement : dix refus écrits, la course continue ; onze, arrêt nommé ; portier et juge comme ci-dessus.
- **Remarque, sans correction.** Un rôle arrêté le reste jusqu'à la fin de la génération. Un proposeur arrêté à sa k-ième case ne produit donc que 12 − k refus écrits, et la borne de onze n'est atteinte que s'il manque dès sa première case. Une absence partielle est comptée (« cases non jouées ») sans arrêter la course. C'est la lettre de la voie 1 que j'ai proposée et que la mère a retenue ; je le dis pour que le mandat du lot 6 ne le lise pas autrement. Comme A3 est désactivée, ce cas ne survient que par un défaut de programme.

## 2. Les mots de 08:00Z, écrits comme tranchés

- **Dernier octet** : gardé tel quel, l'empreinte prise sur la pièce entière (§ 0 bis, mot 1 ; § 5.3). L'option du retrait est dite « ne vaut pas ».
- **V9, l. 83** : la lettre est citée, et la lecture B donnée dans les termes de la mère : le registre servi est une entrée de la course, versée sous GO-2026-11-21-19, et la l. 83 vise les sorties (§ 2.14). La branche A est retirée. Le lot 10 a ne dépend plus d'aucun mot sur cette ligne (§ 7, table ; § 8 ; § 9, point 18). La règle 6 de 07:21Z est dite remplacée.
- **État 1, « garde seule »** : aucun additif à la v9. Il s'écrit à la pièce de relevés, qui vaut complément de valeurs (CV, l. 68), avec l'empreinte du registre servi ; le lanceur lit cette ligne et vérifie l'empreinte (arrêt n° 14).
- **État 2, « lecture de fin »** : l'additif à la v9, l'arrêt n° 14, le devis sur une ligne à part et le mot de Lazar et sa ligne, plus les lecteurs inscrits et la branche orpheline (§ 2.14, règle d'allumage).

## 3. A17 et les deux retouches de lettre

- **A17** (`SansPasseport`) est ajoutée à la table du § 2.13 : arrêt nommé de course, numéroté à l'additif, sous le passeport du portier neuf. L'épreuve est au § 6.2 (lot 6).
- **« Cette v3 et sa contre-lecture »** est remplacé au § 7. Le texte dit aussi que les lots 1 à 5 partent sans attendre.
- **Les points ouverts** sont retirés au § 9, points 18, 19 et 21, et au rapport. Restent ouverts, sans mot : les lignes de compte permutées, la case des témoins, l'affinage, et les anciennes propositions des points 9, 10, 12, 13, 15 et 16.

## 4. La ligne de l'état 1 hors des cinq libellés fixes de la pièce de relevés

**Ce n'est pas un écart à la lettre, mais une retouche est due.** AC, § 6 (l. 136 à 144) fixe une ligne à libellé fixe par clé, sans dire que la pièce n'en porte pas d'autre. La mère veut l'état 1 « au complément de valeurs », et la pièce de relevés en tient lieu (CV, l. 68) : une ligne de plus est la lecture la plus simple de son mot. Trois conséquences restent à écrire :

1. **Le libellé fixe de cette sixième ligne** : l'interrupteur, son état, l'empreinte du registre servi, la date. Il doit être écrit à l'additif du véhicule avant que la mère écrive la pièce, comme les cinq autres le sont à AC.
2. **Le programme qui calcule la pièce de relevés** (R-4306 : calculée par programme, constatée par `cmp`) doit porter cette ligne. C'est à dire à la mère, qui tient ce programme.
3. **L'arrêt n° 11 du lanceur** est resté inchangé dans la v5 : « dans ses cinq lignes à libellé fixe » (CO5, § 2.11, l. 381). À écrire : les cinq lignes de clé, lues par l'arrêt n° 11, et la sixième, lue par la garde de la colonne et par l'arrêt n° 14. Une ligne absente ou d'un autre libellé refuse le départ, par son nom.

Cette retouche touche les lots 8 et 10 a, non le lot 6. La mère peut aussi désigner une autre pièce : le concepteur le dit, et la conception n'en changerait que par ce renvoi.

## 5. Le différentiel : rien d'autre n'a changé

Les 225 lignes ne touchent que :
- l'en-tête de version ;
- le § 0 (calendrier) et le § 0 bis (mots de 08:00Z ; deux renvois de 07:51Z et 07:21Z) ;
- le § 2.13 (voie 1, tables A3, A14 et A17) ;
- le § 2.14 (table de l'interrupteur, règle d'allumage, l. 83) ;
- le § 5.3 (dernier octet) ;
- le § 6.2 (trois lignes d'épreuve remplacées ou ajoutées) ;
- le § 7 (lot 6, lot 10 a, chemin critique) ;
- le § 8 (lot 6 à 7,5 h, somme à 41,5 h, colonne) ;
- le § 9, points 18, 19 et 21.

Aucun autre lieu n'est touché, et aucun ajout ne dépasse les points demandés.

Le calcul est juste : le chemin 2, 3, 5, 6, 8, 9 fait 2 + 2 + 6 + 7,5 + 6,5 + 4,75 = 28,75 h ; la somme des lots fait 41,5 h. L'attente reste de 48 à 60 h.

## Ce qui reste à porter

1. Écrire la sixième ligne de la pièce de relevés et son libellé fixe, et la faire lire par le lanceur à côté des cinq lignes de clé (point 4). Avant les mandats des lots 8 et 10 a ; le lot 6 n'en dépend pas.

— contre-lecteur de la conception du véhicule, modèle O
