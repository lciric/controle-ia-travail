# Contre-lecture courte de la commande de lecture, version 3 — port des corrections — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Écrite le 2026-11-18 par le contre-lecteur de la version 2 (sous-agent, Opus 5.5), sur la suite de son mandat donnée par la conductrice. Par simple lecture : `diff` entre la version 2 et la version 3, contrôle de syntaxe (`bash -n`) des seize blocs de la version 3 et du fichier des paramètres, recopiés hors du dépôt (aucune erreur). Rien n'a été joué sur le réel.

## Pièces (compagnons égaux)

- `commande-lecture-bbis-v3.md` : `195207cf9180c0c667b9dd087f768278ee8ffafea8351a654b2899d32f3df0b3`
- `differences-commande-lecture-bbis-v2-v3.md` : `eb69fe85594d8b8b39e9787033c43e0488eca1d79012b2a5cf88b2cca8a92211`
- Référence : `commande-lecture-bbis-v2.md` (`4eea2d8a…`) ; mon rapport sur elle, `contre-lecture-commande-lecture-bbis-v2.md` (`146b4d04…`).

## Conclusion : **jouable telle quelle**

## 1. Port de m1 à m7

Le `diff` montre chaque remplacement, à l'octet de mon rapport, à sa place :
- m1 : § 5.1 (boucle d'attente retirée ; plus aucune commande d'attente fixe dans un bloc), § 5.1 bis (identifiant lu une fois, « non écrit » distinct d'« absent »), § 5.2 (identifiant non écrit : rendu, rien d'autre).
- m2 : § 5.2 (compte non ancré ; état « sortie non gardée » avant « arrêt avant le seuil ») ; ligne neuve de la table du § 5.3.
- m3 : § 5.2 (heures seulement hors du code 0), constat de forme pour le juge (heures ajoutées), rendu du § 5.4.
- m4 : sept empreintes de la table des modules gelés ajoutées à la liste du § 1.4.
- m5 : § 1.1, comparaison des noms et des têtes ; puce explicative ajustée.
- m6 : pièce de la preuve commitée et poussée entre les deux temps (§ 4.1, § 6) ; puce retirée de la liste « Après ».
- m7 : § 6, liste de l'étape 0.

Les deux écarts de forme déclarés (puce de m6 retirée avec son retour de ligne ; m7 nommant la version 3 et ses pièces) sont sans effet : le premier évite une ligne vide dans une liste, le second nomme la version qui sera commitée.

## 2. Passages changés, fondement, rien d'élargi

Hors m1 à m7, le `diff` ne porte que : le titre, l'en-tête « Version 3 », le paramètre du numéro de lancement, le statut des points ouverts (N1, N1 bis, N2, N4, N6, N8, conformes à mon classement), et :
- **récupération complète du distant par la conductrice** (étape 0, `git fetch origin`, en lecture seule, avant la fusion) : écrite comme geste de la conductrice ; la permission de l'opérateur reste celle des trois branches et de la lecture des têtes. Rien d'élargi.
- **pièce de la preuve commitée et poussée par la conductrice** entre les deux temps, sur la branche de travail (`git add` des deux seuls fichiers) : ne touche pas l'arbre de lecture, dont le parent reste `TETE_TRAVAIL` ; le § 4.2 reste juste. Rien d'élargi.
- **aucune relance jouée sur cette version** (§ 4.1, § 5.3, § 5.5) : restreint.
- **correction de la mère (R-3530)** : toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar ; la preuve après coup n'est jouée que sur ordre écrit de la conductrice et portée à Lazar. Conforme au complément au quatrième addendum, § 7, point 7 ; restreint.

Aucun passage sans fondement. Ce que l'opérateur rend à la conductrice : dans l'état « écrit », le relevé ne porte plus ni les heures ni le compte du seuil ; le rendu du § 5.4 non plus. Rien ne distingue une lecture faite d'une issue « non lue » de fond (reste hors de la commande le temps de retour de l'opérateur, note n10 de mon premier rapport).

## 3. Note n9 (format entier des compagnons) : **sans objet**

- Après le seuil, seules quatre entrées sont vérifiées par des fonctions qui exigent le nom de base dans le compagnon : le manifeste de la course de confirmation (`lire_manifeste`, `lecture_v5.py`, l. 1515, et `verifier_resultat`), `episodes-t06.json` (`verifier_resultat`, l. 936), `mesures-t06.npz` et `textes-actions-t06.jsonl` (`scellement.verifier`, l. 940). Les autres entrées ne sont comparées qu'à une empreinte (`rg.sha256_de`, l. 969, 988) ou par le premier champ du compagnon (`sceau_conforme`).
- Le § 1.3 compare chacun des 32 fichiers extraits, **compagnons compris**, à l'objet git de sa branche d'origine (`git rev-parse <branche>:<chemin>` contre `git hash-object`) : sur le disque, chaque compagnon est donc à l'octet celui de sa branche.
- Relevé par les noms (champ du nom des compagnons, lu sur les branches) : les quinze compagnons des entrées de la course et de la course de confirmation, dont les quatre ci-dessus, portent exactement leur nom de base.
- Un compagnon mal nommé ne peut donc pas atteindre le lancement : le contrôle du format entier n'ajoute rien à la justesse. S'il était voulu par prudence, il se jouerait sans ouvrir aucune donnée (un compagnon ne porte qu'une empreinte et un nom) ; il n'est pas nécessaire.

## 4. Conséquence de m5 : la comparaison échoue si le distant avance entre la récupération et le relevé

**C'est le bon comportement ; ne pas le remplacer par une comparaison à l'instantané de la récupération.**
- L'échec ne consomme rien (« on ne lance pas ») et la suite est écrite (la conductrice refait la récupération ; l'opérateur rejoue le § 1.1 sous un nom de relevé neuf).
- La comparaison à un instantané écrit par la conductrice prouverait seulement que sa récupération était complète au moment où elle l'a faite ; elle accepterait sans le dire un commit poussé ensuite, alors que la garde cherche le premier ajout du fichier de lecture de l'étape B sur les références locales au moment du lancement, et que le texte demande l'histoire complète (plan, point 2 ; feu, § 12).
- Pour réduire les échecs répétés (la session mère pousse souvent sur `main`), il suffit que la récupération de la conductrice précède de peu le § 1.1. La conductrice peut aussi faire rejouer ces trois lignes au § 4.2, juste avant le lancement : recommandé, non exigé (l'écart restant, entre ce relevé et le lancement, ne peut porter qu'un commit daté d'avant le scellement et poussé tard, ce qui ne change pas le premier ajout relevé aujourd'hui).
- Les poussées de la conductrice elle-même ne font pas échouer la comparaison : une poussée met à jour la branche de suivi locale ; les commits non poussés de l'étape 0 ne sont que des commits locaux en plus.

## Fichiers ouverts

Aucun fichier de résultat. Lus : les deux pièces ci-dessus et la version 2 ; `lecture_v5.py` (l. 960-1008) ; rien d'autre de neuf depuis mon premier rapport (relevés de noms de compagnons repris de lui). Rien dans `.claude/`. Aucun refus reçu.
