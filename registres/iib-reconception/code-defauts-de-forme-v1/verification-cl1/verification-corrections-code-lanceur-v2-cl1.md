# Vérification courte des corrections du lanceur de session du saboteur à budget, version 2 — contre-lecteur 1

Pièce d'instrument (classe B), vérifiée par le même contre-lecteur que la première lecture.
- Commit vérifié : `806bce0f`, posé sur `e2c90f97`, branche locale `prep/iib-code-v5`.
- Fichiers : `scripts/lancer_iib_v2.sh`, `src/controle_ia/iib/location_v1.py` (module neuf), `tests/test_iib_lanceur_forme_v2.py`.
- Rapport du développeur, version 2 : empreinte `534c84b1…3c7b`, vérifiée.
- Cadre tenu :
  - l'arbre est intact (`git status` vide) ;
  - le faux outil seul a servi, sans aucun appel au loueur ;
  - la garde de calcul n'a pas été lue ;
  - aucun refus d'outil n'est survenu.

## Verdict : **autorisable**

Aucun bloquant ni majeur ne reste. Le bloquant et les trois majeurs sont corrigés, et mes sept attaques passent contre la version corrigée.

Deux mineurs neufs, ouverts par les corrections, sont à corriger par erratum avant l'ordre neuf. Ce sont des recommandations, pas des conditions de forme du code :
- la garde d'étiquette se contente d'un préfixe ;
- les états d'arrêt peuvent être élargis par une simple variable.

Deux conditions restent avant tout emploi réel, et le rapport les dit lui-même : l'option `-y` de l'outil réel, et la forme réelle des sorties du loueur.

## Table : remarque de la contre-lecture → état

| Remarque | État | Preuve |
|---|---|---|
| 1, bloquant : réponse piégée → destruction d'une autre machine | **corrigée** | `location_v1.py` l. 162-189 : JSON strict sans clé en double, clé `new_contract` au premier niveau seulement, refus sur toute autre valeur candidate. Lanceur l. 403-427 : intouchables, étiquette et état vérifiés avant tout appel. Attaque A1 : code 4, rien de consigné ; même avec une ligne `instance` fausse, refus (code 2) sur l'étiquette « a1-v4 ». Attaque N4 : sept réponses piégées (clé en double, identifiant en chaîne, valeur imbriquée, texte échappé, `repr`, décimal, texte avant le JSON) donnent toutes le code 4, rien de consigné. |
| 2, majeur : inventaire vide pris pour preuve | **corrigée** | l. 423-424 : code 7, sans `destruction_verifiee`. l. 438-457 : deux relectures concordantes, et les autres instances d'avant toujours présentes. Attaque A2 : code 7. |
| 3, majeur : secrets des autres machines dans les traces | **corrigée** | `location_v1.py` l. 226-247 : seuls les champs filtrés des instances `iib` vont aux traces ; le fichier de travail est réduit à identifiant, étiquette et état. Attaque A5 : ni le secret, ni le jeton, ni même la valeur neutre ne restent où que ce soit dans le dossier de session. |
| 4, majeur : secrets en paires et formes échappées | **corrigée** (dans les limites dites, § 5 e du rapport) | Analyse de la structure, motifs de paires, formes échappées des valeurs de l'environnement. Attaque A6 : `MY_API_KEY` et `My_Db_Passwd` masqués. |
| 5, traces écrasées | **corrigée**, sauf le journal de la surveillance (point à trancher 2) | Création exclusive, `mktemp`, `creation-brute-essai<n>.json`. Attaque A7 : deux traces distinctes, rien d'écrasé. |
| 6, « gardée » inexact | **corrigée** | Sortie écrite sur disque d'abord, puis gardée entière en `….NON-MASQUE`, droits 600 (l. 113-119, 145-162, 432-435). Attaque N5 : avec le module absent, la réponse reste entière en `creation-brute-x.json.NON-MASQUE`. |
| 7, sortie d'erreur jetée | **corrigée** | l. 149-152 : fichier `.err` daté et masqué. |
| 8, course entre deux écritures | **corrigée** | l. 127-129 : `noclobber`, empreinte de la copie relue. |
| 9, extrait non masqué | **corrigée** | l. 328 : aucun champ imprimé si le masquage a échoué. |
| 10, identifiant vide | **corrigée** | l. 400 : code 2 (attaque A4). |
| 11, aucune garde d'état ni de calendrier | **corrigée** | l. 404 : `RAPATRIEMENT_VERIFIE=oui` exigé. l. 428-429 : états d'arrêt exigés. Voir le mineur neuf N1. |
| 12, essais biaisés | **corrigée** | 136 essais dans le fichier neuf ; les attaques y sont reprises. |

## Ce qui reste (mineurs, neufs)

**N1. La garde d'état tombe par une variable.** Lanceur, l. 411 et 413.
- `IIB_DESTRUCTION_ETATS_ARRET` accepte n'importe quel mot.
- Preuve : attaque N1. Avec la valeur par défaut, une instance « running » est refusée (code 2). Avec `IIB_DESTRUCTION_ETATS_ARRET=running`, elle donne « DÉTRUITE », code 0.
- La variable est consignée au journal, et `RAPATRIEMENT_VERIFIE=oui` reste exigé : il faut deux réglages explicites, d'où le rang de mineur.
- Correction : une liste fermée dans le code (`exited stopped`, plus au besoin un état d'arrêt réel relevé sur l'outil). Tout état hors de cette liste est refusé, même si la variable le nomme. Un état neuf passe par un erratum, pas par l'environnement.

**N2. L'étiquette est jugée par préfixe, pas par égalité.** Lanceur, l. 426.
- Une autre machine dont l'étiquette commence par celle du saboteur (`iib-explo-v1-autre-chantier`) passe la garde.
- Preuve : attaque N2. Avec une ligne `instance` fausse, l'autre machine est « DÉTRUITE », code 0, alors que la liste des intouchables est vide (permise, l. 405-406).
- La ligne fausse n'est plus produite par `apres-creation` (A1, N4), donc le cas exige deux fautes : rang de mineur.
- Correction :
  - exiger l'égalité exacte avec l'étiquette posée à la création (`--label $ETIQ` est exacte), au lieu d'un préfixe ;
  - en plus, si l'on veut, l'égalité de `machine_id` avec `machine_proposee` de `lancement.txt` ;
  - et, dans l'ordre neuf, une liste d'intouchables non vide.

**N3. Une création refusée consomme un des trois essais.** Lanceur, l. 291-295.
- Les refus de la ligne 293 (réponse d'essai déjà présente, R12) et de la ligne 294 (étiquette hors du préfixe) arrivent après l'écriture de `essai_creation` dans `lancement.txt`.
- Correction : déplacer les deux contrôles avant le `printf` de la ligne 291.

**N4. Le module de lecture n'est pas vérifié par le lanceur.** Lanceur, l. 109-110.
- Le module est cherché à côté du lanceur.
- S'il est absent, tout échoue du côté sûr : code 4, aucune destruction, réponse gardée entière (attaque N5).
- S'il est remplacé, le lanceur lui fait confiance : un module qui ment fait envoyer la commande de destruction (attaque N5, sans affirmation de sûreté).
- C'est du code de confiance, au même titre que le lanceur : il doit entrer dans la liste des empreintes du code (le rapport, § 6, le prévoit : 37 fichiers). Ce n'est pas un défaut du code.

## Avis sur les six points à trancher (sans les trancher)

1. **Forme `repr` de Python refusée.** D'accord pour refuser à l'aveugle. Mais si `--raw` ne rend pas du JSON pur, chaque création réelle finira au code 4, ce qui veut dire inventaire et aucune seconde création. Avant l'ordre neuf, il faut relever la forme réelle. Source à lire : la copie faite par l'exécutante le 19 novembre (écart de R-3687, `creation-brute-copie-<n>.json`), en champs filtrés seulement et après la garde des secrets.
2. **Journal de la surveillance réécrit à chaque relevé.** Garder ce régime m'est acceptable, puisque `progres.txt` et `journal-instance.txt` gardent l'essentiel. Je recommande en plus une copie datée, une seule, à `FIN` et à `ARRET`, pour satisfaire R-3661 sans coût de place.
3. **`IIB_DESTRUCTION_ETATS_ARRET`.** Figer la liste (voir N1). Une porte réglable par l'environnement sur une capacité irréversible n'est pas justifiée.
4. **Chemin de l'outil avec une espace refusé.** D'accord : le chemin réel n'en porte pas, et le refus est clair.
5. **`RAPATRIEMENT_VERIFIE=oui` est une attestation.** Elle suffit si l'ordre neuf l'attache à un fait écrit. Je recommande d'exiger en plus une ligne `rapatriement_verifie <date> <ligne de registre du mot de la mère>` dans `lancement.txt`, lue par le lanceur : c'est peu de code, et cela laisse une trace.
6. **Essais du poste absents de la liste jouée dans l'instance.** Ne pas les y ajouter : ils éprouvent le poste, pas l'instance. Garder 456 et l'amorce telle quelle. En revanche, faire entrer les trois fichiers neufs dans la liste des empreintes du code (§ 6 du rapport).

Le § 6 du rapport traite maintenant le changement de configuration comme une pièce décisive : c'est juste. J'y ajoute deux points : une liste d'intouchables non vide dans `ENVI`, et l'étiquette exacte (N2).

## Sorties brutes

Essais ciblés, rejoués dans l'arbre (`PYTHONPATH=src python3 -m pytest -q tests/test_iib_lanceur_forme_v2.py tests/test_iib_scripts_v1.py`), sortie dans `sortie-essais-cibles-verif-cl1.txt` :
```
........................................................................ [ 79%]
......................................                                   [100%]
182 passed in 37.22s
```

Attaques, version 2 (`test_attaques_lanceur_v2_cl1_v2.py`, ce dossier ; sortie complète dans `sortie-essais-attaque-cl1-v2.txt`). Chaque essai affirme le comportement sûr, donc un échec signale un défaut :
```
A1 : 4 CRÉATION INCERTAINE (code 0, identifiant « aucun » ; plusieurs valeurs candidates pour l'identifiant créé (1 valeur(s) en plus de celle du premier niveau)) | consigné : []
A1 bis (ligne instance fausse) : 2 REFUS : à l'inventaire, l'instance 58936096 porte l'étiquette « a1-v4 », qui ne commence pas par « iib-explo-v1 »
A2 : 7 ABSENCE NON CONFIRMÉE : l'instance 61414494 n'est pas à l'inventaire d'avant (0 instance(s) au compte) ; aucune commande
A3 : 4 DESTRUCTION INCERTAINE : commande de destruction rendue avec le code 1 ; inventaire d'après illisible après 2 relecture(
A4 '061414494' -> 2 ; '61414494 ' -> 2 ; '61414494\n' -> 2 ; '' -> 2 ; '-1' -> 2
A5 secret / jeton / valeur neutre dans le dossier : False False False
A6 : False False
A7 : 6 0 | sorties de travail : 2 | traces : 2
N1 : défaut -> 2 | élargie à running -> 0 DÉTRUITE : instance 61414494 absente de deux relectures concordantes de l'inventaire (relecture 2/2)
N2 : préfixe partagé -> 0 DÉTRUITE : instance 58936096 absente de deux relectures concordantes de l'inventaire (relecture 2/2)
N3 ' 58936096' -> 2 ; '58936096,' -> 2 ; '058936096' -> 2 ; '58936096;61414494' -> 2 ; 'a1-v4' -> 2
N4 cle_en_double / identifiant_en_chaine / imbrique / echappe_dans_texte / repr_python / decimal / texte_avant -> 4 []
N5 module absent, après création -> 4 | consigné : [] | fichiers : ['creation-brute-x.json.NON-MASQUE']
N5 module absent, destruction -> 4 DESTRUCTION NON TENTÉE : inventaire d'avant illisible ou en erreur
N5 module menteur, destruction -> 6 DESTRUCTION NON OBTENUE (commande envoyée : le module est du code de confiance)
FAILED test_n1_etats_arret_elargis_detruisent_une_instance_qui_tourne
FAILED test_n2_etiquette_d_une_autre_machine_au_meme_prefixe
2 failed, 10 passed in 5.52s
```
