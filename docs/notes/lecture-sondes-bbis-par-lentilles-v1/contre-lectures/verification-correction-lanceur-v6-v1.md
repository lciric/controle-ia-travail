# Vérification de la correction 1 sur le lanceur de la première passe, version 6 — v1

Rendu du même contre-lecteur, sur Opus 5.5, versé tel quel par la session des lentilles le 2026-11-20.
- Commit jugé : `530b8070`, branche `claude/brave-galileo-jhp684`.
- Correction vérifiée : la correction 1 de `contre-lectures/contre-lecture-lanceur-v5-messages-arret-v1.md` (`d821cf66…`).

## 1. Verdict

**La correction 1 est portée. Le lanceur est conforme, sans écart bloquant.**
- La fuite reproduite sur la version 5 ne sort plus.
- Les interruptions injectées aux trois endroits ne font plus rien sortir. Les mêmes injections font fuir le message sur la version 5.
- Aucune ligne de calcul ne change, et rien d'autre ne change que la correction.
- Les fenêtres que le développeur déclare résiduelles existent. Sur CPython 3.13, une interruption ne peut pas y être levée : elle attend le point suivant, qui est couvert. Le risque est négligeable et aucune autre forme n'est nécessaire.

## 2. Empreintes

Toutes OK :
- `lanceur_v6.py` : `e0517259…`
- `…_lanceur_v6_interruptions_v1.py` : `9c2b503d…`
- `…_lanceur_v6_v1.py` : `7dc5deaf…`
- `empreintes-code-v6.txt` : `f2ff2de2…`, 32 lignes sur 32 OK contre le disque.

Les six compagnons de `developpement/` sont OK. Sous `src/`, seul `lanceur_v6.py` est neuf depuis `8015a8f9`.

## 3. Décompte

- Paquet entier, de 15:29:05Z à 15:52:05Z : 1 724 réussis, aucun sauté, aucun échec.
- Les deux fichiers d'essais neufs, sur une copie sans altération : 69 réussis.
- Quatre altérations des corrections, toutes vues :

| Altération | Essais tombés |
|---|---|
| L'impression est remise dans le bloc `except` de `principal` | 15 |
| La coupure est retirée de `calculer` | 9 |
| La première ligne de `verser_arret_cloisonne` est sortie de la coupure | 5 |
| Un mot fixe est changé | 7 |

## 4. Points

**1. Empreintes** : OK.

**2. Fabrique**
- Rejouée sur une copie de `lanceur_v5`, elle rend `lanceur_v6` et les huit copies d'essais à l'octet près.
- La différence se limite à l'en-tête, à `MODULES`, à la coupure de `verser_arret_cloisonne`, aux constantes des mots fixes, à la coupure dans `calculer` et à `principal`, qui imprime après le `try`.
- Aucune ligne de calcul ne change.

**3. Scénarios de la version 5 rejoués, et injections neuves aux trois endroits**
- 0 fuite.
- Le message entier est dans `arret.json` chaque fois que ce fichier peut être écrit.

**4. Fenêtres résiduelles**
- La déclaration du développeur est exacte. Les seules instructions hors coupure sont nues, sans appel de fonction :
  - dans `calculer`, `LOAD_GLOBAL`, `CHECK_EXC_MATCH`, `STORE_FAST`, `TO_BOOL`, `POP_JUMP_IF_FALSE` et `RAISE_VARARGS` ;
  - dans `principal`, `STORE_FAST`, `POP_EXCEPT`, `DELETE_FAST` et `JUMP_BACKWARD_NO_INTERRUPT` ;
  - dans `verser_arret_cloisonne`, un `NOP`.
- CPython ne lève une interruption du clavier qu'à l'entrée d'une fonction, sur un saut arrière ou à la fin d'un appel. Une interruption qui arrive dans ces fenêtres attend donc le point suivant, qui est couvert.
- Réserve : ce raisonnement tient au fonctionnement de CPython, non à une garantie du langage. Il cède sous un traceur actif (`sys.settrace`), que l'opérateur n'emploie pas.
- Deux autres formes sont possibles. Ni l'une ni l'autre n'est nécessaire ni recommandée :
  - ne pas relever l'arrêt jusqu'à la ligne de commande. Cela reste dans le cadre du mot GO-2026-11-20-56 ;
  - masquer le signal. Cela touche la conduite de l'opérateur et demanderait la confirmation de Lazar.

**5. Mots fixes et autres arrêts**
- Les mots fixes sont inchangés.
- Une seule constante suffit pour afficher le nom seul : `LIGNE_ARRET_CLOISONNE = "{nom}"`. L'opérateur ne verrait alors plus « fichier d'arrêt non écrit » ni « versement à l'arrêt en échec ».
- Les autres arrêts ont la même sortie qu'en version 5.

**6. Paquet et altérations** : voir § 3.

## 5. Corrections

**Bloquantes** : aucune.

**Non bloquante neuve** : aucune. La note du développeur pourrait ajouter qu'une interruption n'est pas délivrée dans ces fenêtres sur CPython 3.13.

## 6. Nœuds pour Lazar

Les nœuds 1 (les mots fixes) et 2 (le message perdu quand `arret.json` ne peut pas être écrit) sont inchangés.

Pour le nœud 1 : afficher le nom seul cache aussi les deux mentions d'état.

## 7. Expositions

- Lu : seulement les pièces nommées.
- Copié sans être lu : `readout.py`.
- Jamais ouverts : aucun registre, aucune branche de données, de calcul ou de verdict, aucun `diag/` ni `runs/`, aucune table.
- Aucun refus d'outil.
- Aucun commit, aucun push.
