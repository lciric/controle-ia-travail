# Rapport du rédacteur — préenregistrement court v8 et devis v6 de la course « nouvelles attaques » — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 13:04:51Z avant l'écriture. Demande de la session de l'organisme (seconde passe, puis précision de la mère de 13:04Z), mêmes interdits que le mandat `09ad78ba…`. Rédacteur : celui de la v7 et du devis v5. Processeur seul : aucun appel, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucune valeur de clé, aucun identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

- **La v8 est écrite** depuis la v7 (`1837a685…`) : 36 remplacements à texte exact, une passe de l'outil, sans refus. Validateur : huit sections présentes, aucune absente, « problemes : aucun ».
- **Le devis v6 est écrit** depuis le devis v5 (`41a09f77…`) : 29 remplacements. Ligne de course inchangée, 570 USD ; **plafond total 576,05 USD**.
- **Le calcul v5** rend tous les chiffres refaits par le contre-lecteur, au centime.
- Les deux branches de l'épreuve 4 restent ouvertes.

## 1. Pièces lues

Contre-lecture (`acb02c441ce1b7285ff09929bbe532dca57adb513ced56efa156b6cdef340a18`, lue en entier) et son jeu (`c73ad347519266bc87c00dc1c62da432657a8a869da4ad2d9906c43887d11fa3`), empreintes recalculées. `registres/decisions.md` sur `origin/main`, commit `6085c291c3ee92f4b05a6b43365c3ffe43ce0907` (`d765bb74…`) : R-4261 à R-4268 lues, dont R-4265 et R-4266.

## 2. La v8 : 36 remplacements

`remplacements-preenregistrement-court-v7-vers-v8-v1.json`.

| lot | remplacements | contenu |
|---|---|---|
| K'1, K'2, K'6 à K'12 | 9 | mot pour mot du jeu du contre-lecteur ; K'2 reçoit en plus une ligne de table pour R-4266 (versement des deux errata 1) |
| K'3, K'4, K'5 | 3 | la lettre du jeu, mais le devis nommé est le devis v6 (chemin, empreinte, calcul v5), comme K'3 le prévoit si le devis est récrit ; K'5 récrit toute la clause (d), qui disait « garde […] le plafond total du devis v4 » |
| passe R-4265 | 13 | aux lieux du § 4 de la contre-lecture : prédiction (548,70 ; 576,05), table des seuils (sonde 0,05 ; plafond total 576,05), « ce qui change à six espèces », deux valeurs ouvertes, paragraphe de la sonde (4 359 jetons ; plafond ; refus du relais), table « un par un », arrêt n° 2, points 10 et 11 de « ce qui reste » |
| précisions de la mère (13:04Z) | 5 | arrêt n° 16 et valeur ouverte : la liste des motifs s'écrit contre le gabarit servi et la synthèse servie v5, se joue sur les témoins plantés, faux refus sur les requêtes de l'aiguilleur et des juges ; ligne de case : l'identifiant se construit à l'additif, renvoi à sa clé de tirage ; clé et relais de l'espèce 6 vérifiés par la mère, par le nom, avant la sonde, au complément de valeurs ; reste net comptable cité « sur `main` » |
| contre-lecture 5 | 1 | le texte du § 7 de la contre-lecture, mot pour mot ; empreinte du rapport et traitement laissés à la mère |
| tenue | 5 | titre, date, statut (deux lieux), phrase de version |

## 3. Le devis v6 : 29 remplacements, et le calcul v5

`remplacements-devis-v5-vers-v6-v1.json` ; `calcul_devis_course_nouvelles_attaques_v5.py`, sortie jouée deux fois, `cmp` muet. Deux changements seuls au programme : plafond de la sonde de l'espèce 6 à 0,05 USD ; manques calculés sur le besoin exact, arrondis une fois.

| chiffre | devis v5 | devis v6 |
|---|---|---|
| ligne de course | 570 | 570 |
| plafond total | 576,01 | **576,05** |
| attendu | 262,23 | 262,23 |
| total au cas haut | 548,66 | 548,70 |
| écarts à cinq espèces (plafond ; haut) | +120,01 ; +129,23 | +120,05 ; +129,27 |
| variante à 450 USD, plafond total | 456,01 | 456,05 |
| sortie de la sonde (un jeton par octet ; 2,5 octets par jeton) | 359 ; 743 | 4 359 ; 4 743 |
| clé de l'espèce 6, sonde comprise : bas / haut / pire | 35,20 / 88,56 / 199,66 | 35,24 / 88,60 / 199,70 |
| ses manques sur 32,24 | 2,96 / 56,32 / 167,42 | 3,00 / 56,35 / 167,46 |
| avec le collisionneur au pire, bas | 9,54 | 9,58 |
| Rigaud, lots à 45, au cas haut | 15,75 à 32,46 | 15,76 à 32,47 |
| troisième relais, au cas haut | 5,50 à 8,10 | 5,51 à 8,11 |
| repère : pire par appel que le reste de la clé de l'espèce 6 permet | 0,9768 | 0,9756 (90 466 jetons) |

Les trois remarques de lettre sont portées : « 2,5 caractères » de R-4251 compté ici en octets, dit plus prudent ; « préenregistrement court v4 » et « v7 » se lisent « en vigueur : la v8, que la mère scelle avec ce devis » ; les cinq centimes.

## 4. Écarts

1. **K'3, K'4, K'5 ne sont pas mot pour mot** : ils nomment le devis v6, ce que la demande exige (« la ligne du devis dans la table nomme le devis v6 ») ; K'5 est fondu dans la récriture de la clause (d).
2. **K'2 porte une ligne de plus** (R-4266), que le jeu n'avait pas : les errata sont versés depuis. Leurs chemins et leurs empreintes entières ne sont pas dans la table : je ne les ai pas (préfixes seuls au registre) ; à porter par la mère si elle les veut à la table. K'8 et K'12 disent encore que la mère « écrit et scelle » ces errata, mot pour mot du jeu, alors que R-4266 les dit versés.
3. **Chemin du devis v6 et de son calcul à la table** : `NA/preenregistrement-court-v7/`, le dossier que K'3 donnait au devis v5 ; si la mère les verse ailleurs, la ligne se corrige avant le scellement.
4. **Mot sur l'épreuve 4** : je n'ai pas relu `registres/go.md` au commit `6085c291` ; la mère dit que les branches restent ouvertes, et le texte de la v7 est gardé.
5. Le paragraphe « La sonde de refus de l'espèce 6 (v3) » du devis garde sa lettre de la v3 (0,01 USD) ; son titre dit que le paragraphe « recalculées » prime.
6. Compte des ancres par l'outil, comme à la première passe.

## 5. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-preenregistrement-court-v7/`. Chacun a son compagnon.

- `preenregistrement-court-course-nouvelles-attaques-v8.md` (`4970d531d0f2fa63d88642c70aee7275c21ad339abf140bc1be13edd71660313`) et son journal
- `devis-course-nouvelles-attaques-v6.md` (`d825cb313898ea5111ede1ef3103ab25b1b923e1f52103481427919ce9d19c2c`) et son journal
- `calcul_devis_course_nouvelles_attaques_v5.py` (`cdec1d2da65f9e17534b1fd6f28f6d5eb07af7b6982315cbab9a0537da46f1e8`) ; `calcul-devis-course-nouvelles-attaques-v5.json` (`2a0d2a588bfa2ecd19c6c04e0ab3add858d02bcb7ae22edff3b495572334f18e`) ; son second lancement
- `remplacements-preenregistrement-court-v7-vers-v8-v1.json` ; `remplacements-devis-v5-vers-v6-v1.json`
- `differentiel-preenregistrement-court-v7-v8-v1.diff` ; `differentiel-devis-v5-v6-v1.diff`
- `sortie-validateur-preenregistrement-court-v8-v1.txt`
- `rapport-redacteur-preenregistrement-court-v8-devis-v6-v1.md` (cette pièce)

— rédacteur neuf, modèle F
