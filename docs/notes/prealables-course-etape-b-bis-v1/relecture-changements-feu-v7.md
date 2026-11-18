# Relecture de la liste des changements du feu v7 (étape B bis) — lecteur neuf

Date : 2026-11-18 (heure `date -u` au moment de l'écriture : 08:40Z environ). Lecteur neuf (R2) : n'a écrit ni la v5, ni la v6, ni la v7, ni leurs relectures. Aucun appel au loueur, aucune clé lue, aucun commit, rien dans `registres/`.

Pièces lues (empreintes vérifiées par `sha256sum`) : `projet-de-feu-v7.md` `9b41b040…cfd0f73`, `projet-de-feu-v6.md` `b29ece0b…55cb7`, `relecture-changements-feu-v6.md` `e1f16a33…7a3`, choix de la mère `registres/decisions.md` R-3265.

## Verdict : **employable**

Aucun défaut de fond ni de texte trouvé. Trois remarques non bloquantes en fin de document.

## 1. Différences v6 → v7 contre la liste

Comparaison ligne à ligne, le renommage `-v6` → `-v7` appliqué seulement aux trois noms visés (dossier d'envoi, outil du loueur, feu versé) ; les noms `-v6` de l'historique et le fichier `arbitrage-contre-lecture-amorce-v6-v1.md` sont gardés tels quels dans la v7, ce qui est correct (un remplacement global les aurait faussés). Les 52 blocs de différences restants sont tous dans la liste :
en-tête et sources (liste n° 6) ; § 0 conditions 5 et 7 ; § 1 ; § 5 (filet) ; § 6 (suivi horaire) ; § 10 (motif neuf, pilote illisible, commande L) ; gestes 1, 5, 7, 14, 15, 16, 17, 18, 19, 20 (tableau), garde de 12 heures, phases C et D, geste 23 (b), geste 24 ; § 11 ; réserve 13 ; § 15 ; programme d'inventaire version 3 (`pilote_lu`, mode `course`, code 8). Aucune différence non listée. Réciproquement, chaque changement de la liste (1 à 6) est dans le texte, avec ses renvois (geste 15 (b), deux renvois ; geste 16, ligne des rappels ; `inventaire_v3.py` aux gestes 7 (b), 15 (b), 16, 23 (b), commande L ; plus aucun appel opérationnel à `inventaire_v2.py`).

## 2. Justesse et conformité à R-3265

- (a) Rappel « création + 30 min » : `rappel-creation.sh` écrit dans l'accolade de création, après `t-creation.sh`, imprimé ; le geste 16 ne pose plus que l'échéance + 15 min et vérifie la même heure. Conforme.
- (b) Inventaire version 3 : `HORS_BORNES` (code 3) pour un pilote lu de forme chiffres-points hors séries 595 et 580 ; `PILOTE_ILLISIBLE` (code 8) pour champ absent ou de forme inattendue. Commande L, geste 16, 17, 19 en accord (compteurs `n` et `q` par programme, `q` remis à 0 par un verdict conforme ou hors bornes). `prix-relu.sh` écrit sous `noclobber` dès le prix lu (codes 0 et 8). Empreinte `2dc4333a…` : le programme extrait du texte du geste 5 (b) a bien cette empreinte. Empreinte du préambule `f5aabd6b…` : le texte du geste 1 la donne bien.
- (c) Remède du geste 14 : les quatre éléments (témoin, offre retenue, plafond, marque) sont les bons ; tour neuf par la commande O, qui refuse tout tour après un `t-creation.sh` : jamais de seconde création.
- (d) Responsables écrits aux gestes : paragraphe avant le geste 15 (opérateur, 15 à 18, avec 22 et 23 qu'ils commandent), fin du geste 18 (rend la course), avant le geste 19 et en-tête du tableau du geste 20 (mère), avant le geste 21 (mère), geste 24 (mère), phase D (qui joue 22 et 23). Conforme au choix 4 : suivi horaire et destruction par la mère à toute heure.

## 3. Ce que j'ai rejoué (copies sans effet, faux outil du loueur, jetons factices, aucun réseau utile)

Les 31 blocs extraits par programme du texte v7 (non retapés), avec substitution des seuls dossiers et du motif. Dossiers `w-t1`, `w-t2`, `w-t3` dans `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/relecture-feu-v7/`, avec `harness.sh`.
1. Création tentée, réponse illisible, aucune instance visible : « CREATION TENTEE », rappel imprimé (09:07:41Z = création + 30 min) et `rappel-creation.sh` écrit ; geste 15 (b) : `NON_ADOPTEE`, `a-detruire.txt` vide ; 0 destruction ; nouvelle commande O refusée après la création.
2. Pilote absent (geste 16) : code 8, `prix-relu.sh` écrit, compteur 1 ; commande L deux fois : 2 puis 3 ; 0 destruction ; verdict conforme : compteur 0. « NVIDIA 595.58.03 » et `null` : `PILOTE_ILLISIBLE`.
3. Pilote 615.71.09 : `HORS_BORNES`.
4. Remède du geste 14 : plafond vide et marque absente : « AUCUNE CREATION TENTEE », 0 création ; rejeu d'un geste dans le même tour refusé ; tour neuf (motif `'element du tour manquant au geste 14'`) : une seule création ; tour 3 impossible après création.
5. Empreintes du programme v3 et du préambule recalculées sur le texte.
Aussi : le diff complet (§ 1).

## 4. Non vérifié

- Les gestes 22 et 23 réels (lanceur du dépôt) : non joués ici ; le texte du rédacteur dit les avoir joués, je ne l'ai pas refait.
- La forme réelle de `driver_version` chez le loueur ; le délai d'apparition d'une instance.
- L'attente de 15 minutes et le partage opérateur/mère sont des règles de texte, non de programme : lues, non rejouables.
- Le crochet de garde sur les 31 blocs (non rejoué).

## 5. Remarques non bloquantes

1. Au geste 17, les lectures se font toutes les 30 à 60 s : trois `PILOTE_ILLISIBLE` peuvent tomber alors que l'état est encore « loading », et déclencher le nœud (15 minutes) avant « running ». Dans la règle écrite ; la mère le sait.
2. Après le mot « continuer », le compteur `q` continue d'afficher 3 ou plus ; le texte dit que `PILOTE_ILLISIBLE` vaut alors `CONFORME` : lecture humaine, à ne pas confondre avec un arrêt.
3. Lecture « à toute heure » du choix 4 : déclarée par le rédacteur ; si la mère voulait « après l'heure limite seulement », les phrases marquées « v7 » sont à restreindre.
