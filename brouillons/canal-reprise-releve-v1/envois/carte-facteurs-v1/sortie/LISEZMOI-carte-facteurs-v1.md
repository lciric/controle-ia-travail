# LISEZMOI — carte des facteurs et zones interdites de la v6.2.1 — v1

Écrit le 2026-10-26 à 06:44:57 UTC (heure lue sur `date -u` dans la commande qui écrit ce fichier) par un sous-agent neuf de la lignée conv-audit, sur le brief `LISEZMOI-brief-carte-facteurs-v1.md` (`d0d29df8dc60699cd9abf0f8c46d1057d00820828ffcfae14e8df6405fc80d7d`, empreinte vérifiée). Pièce de travail pour la boucle extérieure du pilote 4 (protocole v2, § 6 et § 14) ; ni préenregistrement ni scellement ; à contre-lire par un agent neuf avant le premier usage. L'auteur n'a écrit ni l'objet, ni ses textes, ni la boucle extérieure ; il n'a lu aucun résultat de course, aucun score, aucune tâche de la banque.

## 1. Pièces écrites

Sous `/var/tmp/carte-facteurs-v1/sortie/`, chacune avec son compagnon `.sha256` (« empreinte, deux espaces, nom nu ») :

| pièce | rôle | empreinte |
|---|---|---|
| `carte-facteurs-v1.md` | carte des facteurs, lisible | `47fa6100ae32ec7a0879b14397a3ee4dc5731a98958acd920a9f279110346d2e` |
| `carte-facteurs-v1.json` | la même, pour G5 | `2aaedd08a719e93d2e18437377e9cc565dc4de230ef1af97b0a6e6ef807cec25` |
| `zones-interdites-v1.md` | zones interdites, lisibles | `be486ea8600e48d17a2c3b16a1540e7b49fa3f28982fc8af60edc4963b5b37eb` |
| `zones-interdites-v1.json` | les mêmes, pour G5 | `0082519cc0ef2400c198c89a8504f52948e7abb9b7e35e113db9ba1319f0b342` |
| `LISEZMOI-carte-facteurs-v1.md` | ce fichier | dans son compagnon |

**En bref.** Seize facteurs : les neuf de la liste de départ (F01 à F09 ; les deux seuils du critère de fin forment un seul facteur, F03) et sept révélés par le code (F10 à F16), déclarés comme tels. Quatre points hors boucle (trois 0,01, un 0,03). Trois lignes partagées entre deux facteurs, séparées par segments. Onze zones interdites (Z01 à Z11) : cinq viennent de la liste de départ du § 14 (Z01, Z02, Z05, Z06, Z07, dont deux complétées) et six sont des ajouts depuis le code (Z03, Z04, Z08, Z09, Z10, Z11) ; la frontière de l'exception « défaut du chemin des réponses » sépare les lignes R des lignes E.

## 2. Méthode

1. **Vérifications d'entrée.** Brief : `sha256sum`, égal à l'empreinte donnée. Pièces : `cd fournis && sha256sum -c ../EMPREINTES-fournis-v1.txt`, 28 sur 28 OK (les 26 fichiers de l'objet, le protocole `0c71a74b…`, le texte du pilote `782b858c…`) ; le générateur des JSON a revérifié les 26 empreintes de l'objet avant d'écrire. L'empreinte d'arbre `4f13647a…` n'a pas été recalculée (D14).
2. **Lectures.** Protocole : § 6 et § 14, le reste pour le contexte. Texte du pilote : section « Objet de la première course : la v6.2.1 », le reste par recherche ciblée, pour le contexte. Tout le code de l'objet (`principal.py`, `memoire_isvd.py`, `politique_endogene.py`, `mitose_spectrale.py`, `metrique/`), `CONCEPTION.md`, `CORRECTIONS-v1.md` à `CORRECTIONS-v5.md`, `manifeste.json`. Les essais, par recherche (`grep`) et lecture des passages utiles.
3. **Lignes.** Chaque plage citée vérifiée par `sed -n` ; la fonction de chaque entrée tirée de l'arbre syntaxique (`python3 -I`, module `ast` : la fonction la plus intérieure qui contient toute la plage) ; les segments trouvés par leur texte exact, unique sur la ligne, en colonnes de caractères, avec l'empreinte SHA-256 du segment ; les essais hérités situés par leur nom dans l'arbre syntaxique.
4. **Contrôles avant écriture,** dans la commande qui écrit les JSON : aucune ligne entière dans deux facteurs ; facteurs et zones disjoints ligne à ligne ; segments d'une même ligne disjoints ; une ligne partagée ne porte que des segments de facteurs ; un segment interdit ne tient que dans une ligne de facteur ; chaque point hors boucle tient dans une ligne de son facteur ; aucune plage à cheval sur deux fonctions. Le domaine de F09 est calculé comme complément.
5. **Les `.md` et les JSON disent les mêmes lignes :** les tableaux des deux `.md` sont produits depuis les JSON dans la commande qui écrit chaque `.md`.
6. **Ce qui n'a pas été fait.** Aucune exécution du code de l'objet (lecture, `grep`, `sed -n`, analyse syntaxique seulement) ; aucun `git`, aucun accès réseau, aucun sous-agent, aucune clé ; rien lu hors de `/var/tmp/carte-facteurs-v1/` (hors l'interpréteur Python et sa bibliothèque) ; rien écrit hors de `sortie/` ; aucun fichier écrasé (écriture en mode exclusif) ; chaque heure écrite lue sur `date -u` dans la commande qui écrit la pièce.

## 3. Choix de lecture

- **Facteurs hors liste.** Ajoutés quand un levier n'est couvert qu'en partie par la liste (F10, F11 et F12, détachés de F03, F01 et F05), ou quand le § 14 le nomme modifiable sans que le § 6 le liste (F13 : castes des tâches et appels par tâche ; F14 : castes de la question ; F15 : forme de la règle de récompense ; F16 : délais). Les autres mécanismes (induction, moisson des tâches hors formulation, corpus d'archive, sondes, mémoire, journal d'ablations, contrôle de la règle mutée, parallélisme, successeur, métrique proposée, version) sont listés sans être érigés (carte, § 6) : leurs lignes libres ne sont atteignables que par F09.
- **F03.** Un seul facteur : même grandeur comparée, même disjonction, même fichier écrit, et des rôles qui dépendent de l'ordre des deux valeurs (carte, F03).
- **Zones.** Sont interdits : les textes d'appel et ce qui en choisit le contenu ; la règle qui choisit une classe et ses seuils ; les constantes de mots-clés et ce qui les lit ; les exemples à vérité et leur choix ; le chemin de la question ouverte ; les identifiants d'appel ; les instruments et documents de l'arbre. Les paramètres numériques et les interrupteurs des mécanismes ne sont pas interdits pour autant : ils sont à un facteur, ou dans le domaine de F09.
- **Frontière R/E.** R : ce qui décide de ce qui compte comme la réponse d'un modèle et de la façon de combiner les réponses. E : ce qui trouve et lit ce que le modèle a écrit, ou règle le temps (zones, § 4).

## 4. Doutes, et ce qui n'a pas pu être tranché

- **D1. G5 et les colonnes.** La séparation des lignes partagées (l. 997, 2103, 2104) et des segments interdits (l. 1009, 1011, 1039) suppose que G5 compare les caractères changés aux colonnes. Si G5 ne lit que des lignes, voir le repli de la carte (§ 5). **Non tranché** : à conv-audit.
- **D2. `seuil_confiance_caste1`.** Le § 14 ouvre « le contrat de l'architecte » ; la carte gèle pourtant ce paramètre du contrat (zone Z03), parce qu'il est un seuil du routage de la règle de classe dans la branche avec sonde (l. 1724 et 1732 ; commentaire de C-14, l. 1734–1737). **À confirmer** par la contre-lecture ou par Lazar ; si le gel est levé, ses lignes passent à F04 comme élément à part.
- **D3. Ajouts aux zones.** Z03, Z04, Z08, Z09, Z10, Z11 et les compléments de Z02 et de Z07 sont des choix de cette pièce, chacun avec sa raison. Les plus discutables : Z09 (tout le chemin de la question ouverte), Z11 (la métrique externe), Z10 (les rôles) et, dans Z07, l'assainissement et le choix des passages (l. 251–281).
- **D4. Rôles d'appel.** La raison de Z10 vient du texte du pilote et des essais ; la spécification du relevé mécanique n'est pas dans les pièces. **Non vérifié** que le relevé lise ces noms.
- **D5. Numérotation des rondes.** `int(ronde_conception or 1)` (l. 2102) rend 1 pour une ronde absente ou nulle ; la numérotation du noyau n'est pas dans les pièces. Ce que valent « au moins deux rondes » (F01) et « dernière ronde » (F11) en dépend. **Non tranché.**
- **D6. Les trois 0,01.** Le texte du pilote rattache la stagnation à la mutation (PHB-1, F05) ; la carte gèle aussi les copies de la mitose (PHB-2, F13 ; PHB-3, F14). Lazar dit si sa décision les couvre. **Non tranché.**
- **D7. `VERSION`** (`principal.py` l. 27) : hors facteur et hors fichiers d'accompagnement (le § 6 ne nomme que `manifeste.json`, champs de version et de description) ; une correction ne peut donc pas la changer. **À conv-audit** : l'ajouter aux fichiers d'accompagnement, ou la laisser.
- **D8. F01 et la l. 2106.** La ligne de la disjonction est à F01 pour qu'un minimum de rondes puisse valoir pour toute la déclaration ; G5 ne peut pas vérifier que le changement n'y porte que sur une condition de ronde : le contre-lecteur le fait.
- **D9. Règle d'insertion.** Proposition de la carte (§ 0, point 9) ; G5 peut en retenir une autre.
- **D10. F07.** Une seule borne par tâche est une constante propre de l'organisme ; « appels par tâche » coïncide avec F13 (mêmes lignes) et en prend la condition du § 14 sur les castes.
- **D11. Leviers non érigés** (carte, § 6) : atteignables par F09 seulement (défaut nommé) jusqu'à une carte v2.
- **D12. Frontière R/E.** Classés R par prudence : l'ordre de préférence entre objets JSON (l. 661) et la confiance lue hors de l'objet (l. 701–703). Les fonctions E partagées (`_normaliser`, `_extraire_json_candidat`, `_confiance_finie`, `_enregistrer_appel`) servent aussi hors du chemin des réponses (zones, § 4, avec l'erratum du § 5 ci-dessous).
- **D13. Essais hérités cités** : repérés par lecture, non exécutés ; la liste n'est pas exhaustive.
- **D14. Empreinte d'arbre** non recalculée : la fonction `empreinte_arbre` du noyau n'est pas dans les pièces ; les 26 empreintes de fichiers en tiennent lieu.

## 5. Errata des pièces écrites (non réécrites, R12)

- **`zones-interdites-v1.md`, § 4, dernier point.** La l. 694 y est rangée parmi les usages de `_normaliser` par le routage : c'est le rapprochement des étiquettes dans l'analyse de la réponse (Z02, statut R), un usage du chemin lui-même ; la conséquence dite reste vraie. La même liste omet deux usages de `_confiance_finie`, par la question ouverte (l. 726 et 732, zone Z09).
- **Raison de Z10** (`zones-interdites-v1.md`, § 2 ; champ `raison` de `zones-interdites-v1.json`). « Le texte du pilote nomme le rôle de l'architecte dans sa liste d'arrêt » se lit plus exactement : le texte v4 (l. 206 et 326–327) renvoie à la ligne de la liste d'arrêt de P4v3 qui nomme l'appel de l'architecte, transposée ; il désigne aussi des appels par leur rôle (l. 323).

## 6. Écarts déclarés

1. Le brief et le § 14 placent l'exemple de format à la l. 794 ; il commence à la l. 793 (une chaîne sur deux lignes) : Z06 couvre la consigne entière, l. 787–795.
2. « Ce qui les lit » (Z05) est pris au sens large : lecteurs indirects (par le détecteur et par la pondération) et essais hérités.
3. Les JSON ajoutent aux champs demandés (identifiant, fichier, ligne de début, ligne de fin, fonction) des champs facultatifs : colonnes, empreinte et texte des segments (texte pour du code seulement), statut et type d'exception (zones), note, éléments (F04), instance (F07), essais hérités, domaine de F09, empreintes des fichiers de l'objet, conventions.
4. Le domaine de F09 se limite aux quatre modules de code ; les essais, les documents et le manifeste suivent le § 6 du protocole.
5. F01 comprend la ligne de la disjonction (l. 2106), en plus de l'indice de ronde et de la constante.
6. Les deux errata du § 5.

## 7. Table « point du brief → traitement »

| point du brief | traitement | où |
|---|---|---|
| § 1 : deux cartes écrites d'avance depuis le code, par qui n'a lu aucun résultat | fait ; aucun résultat, score ni fait de course lu | les quatre pièces |
| § 2 : pièces vérifiées | brief et 28 empreintes OK ; arbre non recalculé (D14) | § 2 |
| § 3.1 : nombre minimal de rondes avant la déclaration de fin | F01 : l. 2102, segment de la l. 2104, l. 2106 | carte, F01 |
| § 3.1 : nombre de tâches d'entraînement du score interne | F02 : l. 31 et 1932 | carte, F02 |
| § 3.1 : les deux seuils du critère de fin, un facteur ou deux | un seul, F03, raisons tirées du code | carte, F03 |
| § 3.1 : un élément du contrat de l'architecte | F04, sept éléments ; `seuil_confiance_caste1` gelé (D2) | carte, F04 |
| § 3.1 : la mutation en génération notée | F05 ; la mutation en conception à part (F12) | carte, F05 et F12 |
| § 3.1 : le retour arrière | F06 | carte, F06 |
| § 3.1 : une borne interne par tâche | F07 (plafond de jetons) ; appels par tâche dans F13 (D10) | carte, F07 et F13 |
| § 3.1 : le chemin de formulation de la moisson | F08 | carte, F08 |
| § 3.1 : un défaut de code nommé, forme de la déclaration | F09 : domaine et forme en sept points, sans liste de défauts | carte, F09 |
| § 3.1 : paramètres qui bougent ensemble, avec la raison | pour chaque facteur | carte, § 2 et § 3 |
| § 3.1 : seuils 0,01 et 0,03 | 0,01 à F05 (copies à F13 et F14) ; 0,03 à F06 ; points hors boucle PHB-1 à PHB-4 (D6) | carte, § 4 ; JSON, `points_hors_boucle` |
| § 3.1 : facteurs hors liste | F10 à F16, déclarés comme tels | carte, § 3 |
| § 3.1 : deux facteurs ne se recouvrent jamais, sinon le dire et proposer la séparation | trois lignes partagées (l. 997, 2103, 2104), séparées par segments ; repli si G5 ne lit que des lignes (D1) | carte, § 5 |
| § 3.2 : zones de la liste de départ | Z01, Z02, Z05, Z06, Z07 | zones, § 2 |
| § 3.2 : complétées depuis le code | Z03, Z04, Z08, Z09, Z10, Z11 ; compléments de Z02 et Z07 (D3) | zones, § 2 |
| § 3.2 : frontière de l'exception « défaut du chemin des réponses » | lignes R et E, par fonction | zones, § 4 |
| § 3.3 : JSON lisibles par G5 | deux fichiers ; champs demandés et champs facultatifs (écart 3) | JSON |
| § 3.3 : lignes vérifiées par `sed -n` ou par l'analyse syntaxique | oui | § 2 |
| § 3.4 : LISEZMOI | ce fichier | — |
| § 3.5 : compagnons `.sha256` | cinq | `sortie/` |
| § 4 : jamais de critère, de texte d'appel, de tâche, de score, de fait de course | tenu : consignes, listes de mots et seuils du routage désignés par lignes, jamais recopiés | toutes les pièces |
| § 5 : interdits | tenus | § 2, point 6 |
| § 6 : réponse finale | en quelques lignes | — |
