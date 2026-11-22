# Contre-lecture du lanceur de la première passe, version 5 (messages d'arrêt cloisonnés) — v1

Rendu du contre-lecteur, Opus 5.5, le même que pour la contre-lecture `7954d0fc…`. Il est versé tel quel par la session des lentilles le 2026-11-20.
Commit jugé : `8015a8f9`, branche `claude/brave-galileo-jhp684`.
Mot qui fonde le travail : GO-2026-11-20-56.
Mandat du développeur : `mandats/mandat-developpeur-lanceur-v5-messages-arret-v1.md` (`1ba9f15a…`).

## 1. Verdict

**Conforme, aucun écart bloquant.**
- `lanceur_v5` fait ce que demande le mot de Lazar et ne change aucune ligne de calcul.
- Dans tous les chemins demandés, le message entier des deux arrêts ne va que dans `arret.json`.
- **Un trou reste, étroit.** Une interruption du clavier peut tomber dans les quelques instructions qui suivent le versement. La trace affiche alors le message entier. Je l'ai reproduit. C'est la correction 1 : non bloquante, mais à faire avant que l'opérateur lance le calcul.
- Restent aussi deux nœuds pour Lazar.

## 2. Empreintes : toutes OK

- Tête de la branche : `8015a8f97`.
- Pièces vérifiées :
  - le mandat : `1ba9f15a…` ;
  - `lanceur_v5.py` : `599f4a19…` ;
  - le fichier d'essais neuf : `e37bdae9…` ;
  - `empreintes-code-v5.txt` : `c4dc325b…`, 29 lignes sur 29 OK contre le disque.
- Les compagnons `.sha256` sont OK.
- Sous `src/`, seul `lanceur_v5.py` est neuf, et `statistiques_v3.py` est inchangé.

## 3. Décompte

**Paquet entier** : 1 413 réussis, aucun sauté, aucun en échec, de 14:30:35Z à 14:55:32Z. C'est le décompte du développeur.

**Fichier d'essais neuf**, sur une copie sans altération : 43 réussis.

**Treize altérations de `lanceur_v5`**, chacune dans une copie jetable : toutes vues. Chacune fait tomber au moins un essai, en plus de l'essai de la fabrique.

| Altération | Essais tombés |
|---|---|
| ligne affichée portant le message | 20 |
| fichier d'arrêt ne portant que le nom | 19 |
| enchaînement de l'interruption non coupé | 5 |
| enveloppe de la version 4 remise | 25 |
| échec du versement non attrapé | 7 |
| rien d'écrit avant le départ du calcul | 3 |
| ligne affichée sur la sortie standard | 28 |
| nom affiché faux | 11 |
| mention de l'échec du versement tue | 7 |
| fichier d'arrêt impossible à écrire, erreur remontée | 5 |
| un seul des deux arrêts cloisonné | 14 |
| sortie des autres arrêts changée | 7 |
| ligne de calcul changée | 3 |

## 4. Points 1 à 8

1. **Empreintes** : OK.
2. **Fabrique** :
   - Rejouée sur une copie de `lanceur_v4`, elle rend `lanceur_v5` et les sept copies d'essais à l'octet près.
   - La différence de `lanceur_v4` à `lanceur_v5` se limite à :
     - l'en-tête et `MODULES` ;
     - la table `ARRETS_CLOISONNES` et trois fonctions neuves ;
     - une branche de trois lignes en tête du `except` de `calculer` ;
     - la ligne qui imprime l'arrêt dans `principal`.
   - Aucune ligne de calcul n'a bougé.
3. **Aucun mot du message sur la sortie d'erreur ni sur la sortie standard** :
   - Chemins joués, chacun dans un processus séparé et avec des valeurs témoins :
     - versement fait ;
     - versement en échec, par un arrêt ou par une erreur du disque ;
     - `arret.json` déjà présent ;
     - arrêt avant le départ du calcul ;
     - interruption pendant le versement.
   - Résultat : aucune fuite.
   - **Une fuite reproduite** : une interruption levée pendant le bloc `except Arret` de `principal`. Python affiche alors l'arrêt en cours sous « During handling of the above exception ».
   - **Le même trou existe à deux autres endroits**, plus étroits encore :
     - dans `calculer`, entre le retour de `verser_arret_cloisonne` et le `raise` ;
     - à la première ligne de `verser_arret_cloisonne`, qui est hors du `try`.
4. **Les autres arrêts gardent leur sortie** : identique à la version 4, octet pour octet.
5. **Les deux arrêts ne peuvent pas survenir avant le départ du calcul** : l'argument du développeur est juste.
   - Ils ne sont construits que dans `exiger_sans_egalite` et `libelle_sous_departage`.
   - Ces fonctions ne sont atteintes que par `_Couche` et `_etiqueter`, après `etat["parti"] = True`, à la ligne 998.
6. **Essais** : voir le § 3.
7. **Deux questions ouvertes** :
   - **(a) Mots fixes autour du nom** (« ARRÊT : », « fichier d'arrêt : <chemin> », « fichier d'arrêt non écrit », « versement à l'arrêt en échec : rien n'est supprimé »).
     - Le mot de Lazar ne les exige pas, et sa lettre ne les permet pas expressément.
     - Sur le fond, ce sont des existences.
     - C'est le nœud 1.
   - **(b) Message perdu quand `arret.json` ne peut pas être écrit.**
     - Trois cas : une relance dans le même dossier de sortie, un disque qui refuse l'écriture, une interruption pendant le versement.
     - La consigne à l'opérateur est permise.
     - Une garde qui refuse de partir quand un fichier d'arrêt existe déjà serait une règle neuve. C'est le nœud 2.
8. **Deux champs ajoutés à `arret.json`**, `versement_en_echec` et `avant_le_depart_du_calcul` : permis, ni exigés ni interdits. Le second est une défense qu'aucun chemin n'atteint.

## 5. Corrections

**Bloquantes** : aucune.

**Non bloquantes** :

1. **Fermer les fenêtres où une interruption expose le message** (`lanceur_v5.py`).
   - Où :
     - `principal`, ligne 1204 ;
     - `calculer`, lignes 972 à 974 ;
     - la première ligne de `verser_arret_cloisonne`.
   - Ce qu'il faut faire :
     - calculer et afficher la ligne hors du bloc `except` ;
     - couper l'enchaînement de toute `BaseException` levée entre le versement et le `raise`, par `from None` ;
     - placer l'affectation initiale dans le `try`.
   - Essai à ajouter : une interruption injectée dans `ligne_d_arret_cloisonne`.
2. **Fiche du code et commande de l'opérateur** :
   - la fiche du code porte les treize modules de `lanceur_v5.MODULES` ;
   - la commande devient `python -m controle_ia.lentilles_sondes_bbis.lanceur_v5`.

## 6. Nœuds pour Lazar

1. **Mots fixes de la ligne affichée** : les garder comme existences, ou afficher le nom seul.
2. **Message perdu quand `arret.json` ne peut pas être écrit** : s'en tenir à la consigne donnée à l'opérateur, ou ajouter une garde neuve qui refuse de partir quand un `arret.json` existe déjà.

## 7. Expositions

- **Copié sans être lu** : la copie versée de `readout.py`, pour les altérations.
- **Jamais ouverts** : aucun registre, aucune branche de données, de calcul ou de verdict, ni `diag/`, `runs/`, aucune table, aucun verdict.
- **`git pull`** : fait en nommant la branche, il n'a affiché aucun nom de branche.
- **Refus d'outil** : aucun.
- **Dépôt** : aucun commit, aucun push.
