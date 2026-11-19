# Relecture courte de l'erratum 1 du lanceur de session du saboteur à budget, version 2 — contre-lecteur 1

Pièce d'instrument (classe B), relue en une seule passe.
- Commit relu : `11cdc0a9`, posé sur `806bce0f`.
- Rapport de l'erratum : `rapport-developpeur-defauts-de-forme-v2-erratum-1.md`, empreinte `a43052c0…edc2`, vérifiée.
- Cadre tenu : l'arbre est intact (`git status` vide) ; seul le faux outil a servi, sans aucun appel au loueur ; la garde de calcul n'a pas été lue ; aucun refus d'outil.

## Verdict : **autorisable**

Les quatre mineurs de la vérification sont corrigés. L'erratum ouvre deux mineurs neufs. Aucun n'est bloquant ni majeur, car chacun exige soit une erreur de l'exécutante, soit un code remplacé. Ils sont à corriger par un erratum 2 ou à fermer par l'ordre neuf ; ce sont des recommandations, pas des conditions de forme.

Les conditions d'avant l'emploi réel ne changent pas :
- l'option `-y` de l'outil réel ;
- la forme réelle des sorties du loueur ;
- l'empreinte du module de lecture écrite dans la configuration neuve (voir R2).

## Les quatre mineurs

| Mineur | État | Preuve |
|---|---|---|
| N1, états d'arrêt élargissables par une variable | **corrigé** | Liste fermée `exited stopped` dans le code ; la variable, si elle est posée, est refusée (code 2). Attaque N1 : refus, code 2. |
| N2, étiquette jugée par son début | **corrigé** | Égalité exacte (`case "$ETIQ_VUE" in "$ETIQ")`). Liste des intouchables exigée, sauf attestation. Attaque E1 (autre machine absente de la liste, étiquette `iib-explo-v1-autre-chantier`) : refus, code 2. Attaque N2 : refus par la liste. |
| N3, un refus consomme un essai de création | **corrigé** | Les deux contrôles sont remontés avant l'écriture de `essai_creation`, et un commentaire le garde. |
| N4, module de lecture non vérifié | **corrigé dans la forme** (voir R2) | `verifier_module` est appelé avant tout emploi. Attaques N5 et E5 : un module absent ou remplacé donne le code 4 ; une configuration et un environnement contradictoires donnent le code 4 ; le cas sain, avec la configuration seule, donne le code 0. |

Autres ajouts de l'erratum, vérifiés :
- une copie datée des journaux est faite à la fin de la surveillance ;
- la ligne `rapatriement_atteste` n'est écrite qu'après les gardes d'état et d'étiquette. Attaque E6 : un refus n'écrit pas la ligne.

## Restes (mineurs neufs)

**R1. L'attestation `IIB_AUCUNE_INTOUCHABLE=oui` n'est pas confrontée à l'inventaire.** Lanceur, garde des intouchables de `destruction`.
- Preuve : attaque E2. L'attestation est posée alors que l'inventaire d'avant montre deux autres machines, dont une porte exactement l'étiquette du saboteur, et la ligne `instance` est fausse. Résultat : « DÉTRUITE », code 0, et l'autre machine disparaît.
- Il faut trois fautes à la fois, et la création ne produit plus de ligne `instance` fausse (attaques A1 et N4).
- Correction : refuser l'attestation quand l'inventaire d'avant compte une autre instance que celle visée (`n > 1`). L'ordre neuf ne doit pas employer l'attestation : le compte porte cinq machines intouchables.

**R2. L'empreinte attendue du module peut venir de l'environnement seul.** `verifier_module`.
- Sans `config.json` dans le dossier, ou avec une configuration qui ne porte pas l'empreinte du module, `IIB_LOCATION_SHA256` fait foi seule. Or c'est le cas de la configuration scellée actuelle : sa liste des empreintes du code ne nomme pas `location_v1.py`.
- Preuve : attaque E4. Un module remplacé passe dès que l'environnement donne sa propre empreinte, et la commande de destruction est envoyée.
- Correction : quand `config.json` est présent, exiger qu'il porte l'empreinte du module, la variable ne pouvant que la confirmer. Réserver la variable aux essais, ou la retirer. La configuration neuve doit porter l'empreinte (le § 6 du rapport le prévoit, 37 fichiers).

**R3 (note, sans correction exigée).** Les copies de fin de surveillance versent `journal-dernier.txt` et `journal-instance.txt` aux traces. Ces journaux ne sont masqués que par les valeurs des clés de l'environnement. L'ordre neuf le couvre déjà : versement seulement après la garde des secrets.

## Sorties brutes

Essais ciblés, rejoués dans l'arbre (`PYTHONPATH=src python3 -m pytest -q tests/test_iib_lanceur_forme_v2.py tests/test_iib_scripts_v1.py`) ; fichier `sortie-essais-cibles-erratum-cl1.txt` :
```
........................................................................ [ 71%]
..........................................................               [100%]
202 passed in 51.28s
```

Attaques en version 2, rejouées contre l'erratum (`test_attaques_lanceur_v2_cl1_v2.py` ; fichier `sortie-essais-attaque-cl1-v2-sur-erratum.txt`) :
```
A1 : 4 CRÉATION INCERTAINE (... plusieurs valeurs candidates ...) | consigné : []
A1 bis (ligne instance fausse) : 2 identifiant 58936096 dans la liste des instances intouchables
A2 : 7 ABSENCE NON CONFIRMÉE ...   A3 : 4 DESTRUCTION INCERTAINE ...   A4 : 2 ×5   A5 : False False False   A6 : False False   A7 : 6 0 | traces : 2
N1 : défaut -> 2 | élargie à running -> 2 IIB_DESTRUCTION_ETATS_ARRET n'existe plus : la liste des états d'arrêt (exited stopped) est fermée
N2 : préfixe partagé -> 2 (liste des intouchables)   N3 : 2 ×5   N4 : 4 [] ×7
N5 module absent -> 4 (réponse gardée en .NON-MASQUE) ; destruction -> 4 ; module menteur, destruction -> 4 DESTRUCTION NON TENTÉE : module de lecture … empreinte
12 passed in 3.52s
```

Attaques neuves, version 3 (`test_attaques_lanceur_v2_cl1_v3.py` ; fichier `sortie-essais-attaque-cl1-v3.txt`). Chaque essai affirme le comportement sûr, donc un échec signale un défaut :
```
E1 : 2 REFUS : à l'inventaire, l'instance 58936096 porte l'étiquette « iib-explo-v1-autre-chantier », qui n'est pas exactement « iib-explo-v1 »
E2 : 0 DÉTRUITE : instance 58936096 absente de deux relectures concordantes de l'inventaire (relecture 2/2) | inventaire : [61414494, 61000001]
E3 {liste absente} -> 2 ; {vide, AUCUNE=yes} -> 2 ; {liste + AUCUNE=oui} -> 2 ; {AUCUNE=OUI} -> 2
E4 : module menteur + empreinte de l'environnement -> 6 DESTRUCTION NON OBTENUE ... | destroy envoyé : True
E5 : contradiction -> 4 | configuration seule, module remplacé -> 4 | sain, configuration seule -> 0
E6 : 2 | ligne d'attestation écrite : False
FAILED test_e2_attestation_aucune_intouchable_alors_que_le_compte_porte_d_autres_machines
FAILED test_e4_empreinte_du_module_fournie_par_l_environnement_seule
2 failed, 4 passed in 1.33s
```
