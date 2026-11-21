# Essai Lean D-1a, troisième essai : contre-lecture des causes et des corrections (v1)

- **Quoi** : contre-lecture de classe B (instrument) du rapport `rapport-causes-et-corrections-essai-3-v1.md` (`887cf4c9…f9d9`) et du code de la branche `prep/lean-outillage-d1a-v11`, commit `6675009c`. Pas 6 de l'arbitrage Fable 5.2, point 7 (`docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md`, `44d1e86f…dd06`).
- **Qui** : Claude Fable 5.2, contre-lecteur, le 21 novembre 2026. Le développeur est Claude Opus 5.5 : autre modèle. Aucune dépense, aucune machine louée.
- **Pièces lues** : le rapport ; les huit pièces de `pieces-causes-essai-3-v1/` (empreintes vérifiées, 8 sur 8) ; `executeur_bac_v7.py` (`be0b847f…d8ed`) et `epreuve_isolement_v7.py` (`78d0cbdc…66ac`), par différence avec les v6 ; `attendus-v6.json` (`c370ca41…51c4`), par différence avec les v5 ; les cinq items sondes v3, par différence avec les v2 ; `limite_code137_v1.py`, `limite_memoire_lean_v1.lean`, `compiler_comme_bac_v1.sh`, `piloter_poste_v11.sh` (`2aea807f…c011`), `mutations_gardes_v11.py`, les trois fichiers d'essais ; sur la branche des données de la machine (`donnees/lean-outillage-d1a-poste-local-v4`), `installation-v6.txt` et `epreuve-isolement-v6.json`.

## 1. Verdict

**Conforme après ces corrections** (liste fermée, § 6 : deux points bloquants). La cause des cinq échecs est établie sur pièce et n'est pas un fait d'isolement. Les corrections du temps de processeur, de l'épreuve morte et du refus d'un échec « processus non lancé » font ce qu'elles disent, sans garde affaiblie. Deux défauts restent : le cas Lean de la limite de mémoire peut réussir sans que la compilation ait été arrêtée par la mémoire ; le relevé de la mémoire peut arrêter l'exécuteur sur une lecture concurrente du retrait du cgroupe.

La définition de « délai » par le compte de l'unité est **acceptée**, sous les trois phrases que la procédure doit porter (§ 3.1).

## 2. La cause est-elle établie ?

Oui.

1. La pièce `sortie-compilation-sondes-v2-v1.json` (`acbd15be…1166`) porte, pour les cinq items v2, le code 1 et la même erreur à la ligne 5, colonne 88 : « Application type mismatch … `r.take 120` has type `String.Slice` but is expected to have type `String` », puis une erreur « depends on the 'sorry' axiom » par `#eval`. Aucune ligne « ISOLEMENT », sortie d'erreur vide.
2. Rejoué ici avec la chaîne installée dans le conteneur (Lean 4.35.0, commit `eb6cafb7…`) : le cas sain v2 (`iso_persistance_ecrire_v2.lean`) sort en code 1 avec ce même message ; les dix essais « avec la chaîne » passent (cinq v2 en échec pour cette cause, cinq v3 qui rendent toutes leurs tentatives).
3. La machine du troisième essai avait le même binaire : `installation-v6.txt` porte « Lean (version 4.35.0, …, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release) » et le même commit de Mathlib. `epreuve-isolement-v6.json` y donne, pour les cinq cas, code 1 et 0,34 à 0,40 s de processeur.
4. L'erreur est une erreur de typage, à l'élaboration, avant toute lecture ou écriture de l'item. Elle dépend de la source et de la chaîne, qui sont les mêmes ; elle ne dépend pas du bac. Les items v2 ne peuvent compiler sous aucun isolement.

Ce que la pièce écarte : l'hypothèse d'un refus du bac comme cause des cinq échecs. Ce qu'elle n'établit pas : que l'isolement Lean tienne. La sortie de la machine n'avait pas été gardée (c'était le défaut) ; le pas 3 est donc une identité de binaire et de source, non une lecture directe. Le quatrième essai la confirmera (`sonde_muette` à faux, code 0).

L'attendu a été écrit avant la compilation (`attendu-avant-compilation-v1.md`), avec ce qui l'aurait démenti. Le temps de 0,4 s est expliqué : ces items n'importent pas Mathlib.

## 3. Les corrections, une par une

### 3.1 La définition de « délai » (`executeur_bac_v7.py`, l. 168 à 188)

Le classement lit le résultat de systemd et le temps de processeur de l'unité. Le code de sortie et la fin du processus ne comptent plus. Les deux cas R5 sont joués sur les résumés réels du troisième essai : l'item qui brûle (5,011 s, code 137) sort « délai » ; un item qui sort en 137 en 31 ms ne sort pas « délai ». La v6 est rejouée sur le premier et rend « aucun incident » : le défaut est reproduit.

**Le compte de l'unité contre une limite par processus : acceptable.** Motifs :
- pour un processus seul (Lean et ses fils d'exécution, Python sans enfant), les deux comptes coïncident à l'enveloppe du bac près ;
- pour obtenir « délai », un item doit faire consommer la limite à son unité. Il ne peut plus l'obtenir par un code de sortie ;
- l'écart ne joue que pour un item à plusieurs processus, et dans un seul sens : il sort « délai » sans qu'aucun de ses processus ait été tué par la limite.

**Ce que la procédure doit dire**, en trois phrases :
1. « Délai » veut dire : l'unité n'a pas réussi et a consommé, tous processus confondus, au moins la limite de temps de processeur ; ou systemd a rendu `timeout`. Cela ne veut pas dire qu'un processus a été tué par la limite.
2. Une réussite n'est jamais un incident, même au-delà de la limite. Un item à plusieurs processus peut consommer plus que la limite au total : la borne de l'unité est la durée murale.
3. « Délai » ne doit jamais valoir mieux qu'un échec dans ce qui lit le bac (ni rejeu, ni retrait du dénominateur). Sinon un item à plusieurs processus pourrait l'acheter.

**Réserve, non établie ici** : la marge du cas qui brûle est de 11 ms sur une seule mesure (5,011 contre 5). Le noyau tue le processus sur un temps compté par battements d'horloge ; systemd rapporte un temps exact du cgroupe. Je n'ai pas pu mesurer l'écart entre les deux (pas de systemd ici). Si le compte de l'unité tombait juste sous 5 s, le cas sortirait « aucun incident ». Ce n'est pas une voie de forge (il faut brûler la limite) ; c'est un risque de faux « non conforme ». Voir la recommandation R1.

Le défaut de v6 corrigé par la mutation survivante (limite fixe au lieu de celle de la configuration) est bien fermé : trois points d'appel, trois mutations tuées.

### 3.2 Le refus d'un ECHEC « processus non lancé » (`epreuve_isolement_v7.py`, l. 155 à 162)

Fait ce qu'il dit, et renforce la garde : un ECHEC dont le détail porte « could not execute external process » devient un écart. Vérifié sur la pièce v3 (les deux tentatives Python du développeur portent ce motif) et par la mutation e704. Sur la machine, `curl` est installé par l'installeur et `python3` est dans `/usr/bin` : ce motif ne doit pas sortir.

Limite : c'est une liste de refus, sur le seul item réseau. Objet de contrôle joué : un ECHEC « code 127 … python3: No such file » n'est pas refusé. De plus l'item coupe la sortie d'erreur à ses 160 premiers caractères ; pour Python, c'est le début de la trace, pas la raison. Non bloquant : le réseau fermé est éprouvé par ailleurs (isolement Python, sonde de l'hôte). Voir R4.

### 3.3 L'épreuve morte (`epreuve_isolement_v7.py`, l. 191 à 202 et 315 à 321)

Fait ce qu'elle dit. Un cas sain qui ne rend pas ses tentatives fait sortir son genre et l'épreuve « épreuve morte », code 3 ; jamais « conforme ». Le troisième essai rejoué sur un bac factice sort « épreuve morte ». La sortie de compilation entre dans le JSON, bornée, avec le drapeau de troncature.

Limite : un genre sans cas marqué `sain` sort « non conforme » sans que rien signale l'absence du témoin (objet joué : `statuts_genres` avec `sains` vide). Les marques sont tenues par un essai et par l'empreinte des attendus. Voir R2.

### 3.4 La mémoire

**La cause du pic à 336 Kio** : lue dans les sources de systemd 255, que je n'ai pas relues. Elle s'accorde avec les chiffres de la machine (valeur juste sous `oom-kill` et `timeout`, fausse ailleurs). Le retrait du chiffre est juste.

**Le relevé échantillonné, comme minorant** : la description est exacte à une phrase près. `memory.peak` est un plus-haut que le noyau tient : un pic bref entre deux relevés n'est pas perdu, le relevé suivant le porte. Seul est perdu ce qui monte après le dernier relevé. Le rapport dit les deux (l. 141 juste, l. 186 fausse). Autre phrase fausse, l. 187 : la somme des trois pics « majore » le pic simultané. C'est vrai de pics exacts, non de minorants.

**Défaut bloquant B2** : `relever_memoire_pic` (l. 191 à 196) n'attrape que « fichier absent ». Une lecture qui tombe pendant le retrait du cgroupe lève une autre erreur du système (« No such device ») ; un contenu vide lève une erreur de valeur. Objets joués : les deux lèvent, et l'exécuteur s'arrête au milieu d'un essai payant. L'événement est rare ; la correction est d'une ligne.

**Défaut bloquant B1** : le cas Lean de la limite de mémoire ne peut pas échouer sur ce qu'il prétend établir. `juger_limite_lean` (l. 181 à 188) lit `incident_bac`, qui vaut « incident de la compilation, ou à défaut du vérificateur » (`executeur_bac_v7.py`, l. 442). Sous les limites d'essai, le vérificateur est lui-même arrêté (le rapport le dit, § 7). Objet de contrôle joué : compilation en code 1 d'elle-même, sans « ALLOUE », 0,4 s ; vérificateur en `oom-kill`. Le juge rend zéro écart. C'est le défaut du troisième essai en miroir : un item qui ne compile pas passerait pour un item tué par la mémoire. L'item compile ici (témoin à 1 000 000 cases rejoué : code 0, « ALLOUE 7000000 ») ; le juge, lui, ne le garantit pas.

### 3.5 Le pilote v11

Différence avec le v10 lue : les deux programmes v7 dans la phase « apres », la ligne du code de sortie, rien d'autre. Syntaxe vérifiée. Les artefacts neufs partent avec le dossier copié en entier. Non éprouvé sur une machine, comme le dit le rapport.

## 4. Essais et mutations rejoués

- Chaîne Lean présente dans le conteneur (bloc-notes partagé, `chaine.json`) : Lean 4.35.0, commit `eb6cafb7…`.
- Les trois fichiers d'essais neufs, avec la chaîne : **49 réussis, 0 sauté**, 5 s.
- `mutations_gardes_v11.py`, avec la chaîne, dossier neuf : **31 tuées sur 31**, témoin 49 réussis.
- Mes objets de contrôle, sur le code v7 : cas Lean de mémoire qui échoue de lui-même (zéro écart : B1) ; lecture du cgroupe en retrait et contenu vide (lèvent : B2) ; genre sans cas sain (silencieux : R2) ; ECHEC Python d'une autre cause (admis : R4) ; seuils 4,999 / 5,0 / 5,011 (rien, délai, délai).
- Non rejoués : la suite entière du harnais (29 min, interdite par le mandat) ; les deux essais hors machine de 39 cas (20 min chacun ; pièces lues, empreintes justes). Rien de ce qui passe par systemd et bwrap ne se rejoue ici.
- Fichiers temporaires supprimés ; l'arbre du développeur n'a pas été modifié.

## 5. Recommandations non bloquantes

- **R1, marge du « délai »** (`executeur_bac_v7.py`, l. 187). Soit une tolérance fixe écrite avant l'essai (par exemple 0,05 s sous la limite, avec ses deux cas d'essai) ; soit la procédure écrit d'avance la lecture d'un cas qui brûle, sort en 137 et porte un temps entre 4,95 et 5 s. À trancher par écrit avant le quatrième essai, pas après.
- **R2, témoin sain obligatoire** (`epreuve_isolement_v7.py`, l. 315) : arrêt si « isolement Lean » ou « Python » n'a aucun cas `sain`.
- **R3, rapport** (l. 186 et 187) : erratum sur les deux phrases du § 3.4.
- **R4, item réseau** : garder la fin de la sortie d'erreur plutôt que le début ; la procédure demande de lire le détail des trois tentatives.
- **R5, mesures** : un pic relevé sur moins de trois échantillons n'est pas rapporté comme un pic. La durée murale de chaque lancement est allongée d'au plus 0,1 s par la boucle de relevé.

## 6. Corrections bloquantes (liste fermée)

- **B1** — `src/controle_ia/lean_essai/epreuve_isolement_v7.py`, l. 181 à 188 (`juger_limite_lean`). Juger sur la compilation seule : exiger que le résultat de systemd de la compilation soit `oom-kill` (`res["compilation"]["resultat"]`), ou exposer l'incident de la compilation à part dans `executeur_bac_v7.py`, l. 442. Essai neuf : compilation en `exit-code` et vérificateur en `oom-kill` doit rendre un écart. Mutation neuve : retour à `incident_bac`.
- **B2** — `src/controle_ia/lean_essai/executeur_bac_v7.py`, l. 195 (`relever_memoire_pic`). Attraper toute erreur du système et l'erreur de valeur, et rendre « aucun relevé ». Essai neuf : les deux cas rendent `None` et le lancement se termine.

Versions neuves (R12), puis vérification par ce même contre-lecteur.

## 7. Ce qui reste avant le quatrième essai

1. **B1 et B2**, leurs essais, leurs mutations ; vérification des corrections.
2. **À rejouer hors machine** après correction : les trois fichiers d'essais avec la chaîne ; les mutations (31, plus les neuves) ; l'essai hors machine de 39 cas contre le code corrigé, puisqu'il est gratuit.
3. **Procédure v12**, à écrire. Elle porte : les trois phrases du § 3.1 ; la décision R1 ; l'ordre de lecture (`statut`, `genres`, puis les cas) ; « épreuve morte » arrête la lecture du genre ; les cinq sondes à `sonde_muette` faux et code 0 ; le détail des trois tentatives réseau lu ; le cas « 137 sans consommer » sans incident ; le cas Lean de mémoire lu sur le résultat de la compilation ; `memoire_echantillons` à zéro dit que le chemin du cgroupe est faux, et le pic n'est alors pas rapporté ; aucun « conforme » ne dépend du pic.
4. **Mémoire de la machine entière pour trois passages en parallèle.** Les trois pics par unité ne la donnent pas. Proposition : lancer les trois unités du passage en parallèle dans une tranche réservée, de nom neuf, et relever le `memory.peak` de cette tranche. Le noyau y tient le plus-haut de la somme simultanée ; le relevé n'en perd que la fin. En recoupement, relever la mémoire disponible de la machine (`/proc/meminfo`) avant, pendant et après, à la même cadence. Critères à écrire d'avance : aucun `oom-kill`, pic de la tranche sous un seuil fixé contre la mémoire de la machine (32 857 436 160 octets, `installation-v6.txt`). C'est un changement de `mesurer` et du lancement : à joindre aux versions neuves, ou à laisser de côté, auquel cas le quatrième essai ne compte aucun passage en parallèle, comme l'arbitre l'a dit.
5. **À jouer sur la machine**, parce que rien ne le rejoue ici : le classement v7 ; le chemin du cgroupe ; le classement « mémoire » du cas Lean ; les issues des sondes v3 sous bwrap et l'utilisateur `bac`. Tout se rejoue : 18 cas du noyau, 36 cas de l'épreuve.

## Relevé de méthode

**Chaîne de raisonnement.**
1. Les cinq items v2 échouent au typage sous Lean 4.35.0 : pièce `sortie-compilation-sondes-v2-v1.json` (`acbd15be…1166`), rejouée (§ 4).
2. La machine avait ce binaire : `installation-v6.txt`, branche des données.
3. Une erreur de typage ne dépend pas du bac : suit de 1 et 2.
4. Le classement v7 ne se forge pas par le code de sortie : `executeur_bac_v7.py`, l. 168 à 188 ; mutations x703 et x704 tuées.
5. Le compte du cgroupe atteint la limite quand le noyau tue : **supposé**, une mesure à 5,011 s.
6. Le juge du cas Lean de mémoire admet un item qui échoue de lui-même : calcul rejouable, § 3.4.
7. Le relevé lève hors de « fichier absent » : calcul rejouable, § 3.4.

**Objets de contrôle.** Faux : compilation en échec propre et vérificateur tué (le juge devait rendre un écart ; il n'en rend pas). Vrai : compilation en `oom-kill` (zéro écart attendu et rendu). Faux : sortie en 137 en 31 ms (pas « délai » : tenu). Vrai : 5,011 s (« délai » : tenu).

**Premier pas non justifié.** Le pas 5. Le justifierait : le cas qui brûle rejoué plusieurs fois sur la machine, ou la lecture du noyau 6.8 sur les deux comptes.

**Mode d'échec affecté.** Aucune ligne dans le mandat. J'ai visé « épreuve qui ne peut pas échouer, ou pas réussir » et « objet de contrôle oublié ou inopérant ».

**Trouvaille de côté.** Le motif du troisième essai revient : un artefact R5 jamais compilé contre la chaîne épinglée avant la machine. Une règle simple le fermerait : tout artefact Lean neuf est compilé hors machine avant de partir. Non poursuivi.

**Évaluateur et conseil.** Ce qui juge ces programmes : leurs essais, les mutations, puis la machine. Les essais sont admis sur des résumés réels du troisième essai. Par où un bon jugement non mérité : tout ce qui passe par systemd et bwrap est joué sur des bacs factices écrits par l'auteur.
