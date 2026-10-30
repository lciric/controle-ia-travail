# Vérification des retouches R1 à R3 — brouillon 6 du préenregistrement bisociation v2

- Vérificateur : sous-agent neuf (non-auteur du brouillon 5, du brouillon 6, du script de retouches ; pas le vérificateur des corrections du brouillon 5 dont je lis le rapport)
- Modèle : Sonnet 5.5 (claude-sonnet-5-5)
- Heure UTC : 2026-10-30T02:34:46Z
- Pièces lues : `verification-corrections-brouillon5-v1.md`, `appliquer-verification-brouillon6-v1.py`, diff brouillon 5 / brouillon 6, brouillon 6 aux passages voisins (résumé, § 6, § 7, § 9, audit, liste d'arrêt, tableau de traitement, ligne de gel), sortie `calcul-puissance-bisociation-v2-brouillon4-v2-sortie.txt` (§ 11, § 17, § 21). Rien sous `donnees/`, aucun réseau.
- Contrôle mécanique : script rejoué sur le brouillon 5 (`2dc810ab…`, conforme à son empreinte compagnon) avec l'heure 02:32 : résultat identique octet pour octet au brouillon 6 (`7bc9fb9c…`, conforme à son empreinte compagnon). Le diff ne contient donc que le texte du script ; 27 marqueurs « À REMPLIR » avant et après.

## Verdict

**À reprendre, retouche mineure** : R1 et R3 sont conformes ; R2 est faite aux points (1) et (2) mais le point (3) de la vérification n'est ni fait ni écarté. Aucun seuil ni chiffre calculé n'a changé.

## R1 — conforme
Ligne 799 (entrée (f)) : « V7 : version nouvelle, sans réglage » est remplacée par « lue par J, A7 et les déclencheurs d'audit ; V7 sans conséquence depuis le brouillon 5 ». Cela s'accorde avec le § 6 (ligne 579 : « V7 ne déclenche rien » ; J, A7 et les déclencheurs d'audit sont les seules lectures du canal). Plus aucune occurrence de « V7 : version nouvelle » (le seul reste est la mention, dans l'historique 8, de l'ancienne phrase corrigée). La répétition de « aucun paramètre n'est modifié après sa lecture » (ligne 579) subsiste : facultative, sans effet. La formule de remplacement diffère de celle proposée mais dit la même chose.

## R2 — faite en partie
- **(1) Audit déclenché par V9 : fait et cohérent.** Le texte dit : relecture du code et relance des seuls témoins d1c et c sur les graines de validation ; aucun bras candidat (N, ses ablations, ses placebos dont N_PCg) exécuté ; (i) s'applique, (ii) non, (iii) porte sur Δ(d1c, c) dans les miroirs de validation de `M_inertes`. Aucune contradiction : le § 6 (V9 « ne calcule que d1c et c, jamais N »), le § 9 (audit rendu et scellé avant l'invocation unique) et la ligne d'arrêt (« J vraie sur les miroirs (V9) : audit R4, non concluant tant que non rendu ») disent la même chose. L'audit de V9 n'exécute donc aucun bras candidat. La relecture du code des bras candidats reste permise (lire n'est pas exécuter).
- **(2) X de (ii) et contrastes de (iii) : fait.** (ii) lit la borne basse à 99 % de Δ(N_PCg, N_β0) « en M_bien ou en M_moyen (l'une suffit) », conforme au contraste 8 et à la définition de gain_contrôle (ligne 635). (iii) renvoie aux « contrastes décisifs du § 7 (1 à 9 et 11 à 15, plus 20 si S17 = option 1) » : ces numéros existent tous au § 7 (liste « Décisifs » : 1 à 9, 11 à 15 ; le 20 est « décisif à 95 % si S17 = option 1 »).
  - Remarque sans gravité : le contraste de non-régression (C11 du § 8, niveau 99 %) est décisif mais n'a aucun code au § 7 ; la liste de (iii) l'omet donc sans le dire. À signaler ou à coder avant scellement du code.
- **(3) Cas gain_contrôle sur les mondes de décision et (ii) négatif sur la validation : absent.** La vérification demandait une phrase (le verdict suit alors la direction prudente des lignes 5 de la Table 1 et 3 de la Table 2, pour que le lecteur de la porte n'y voie pas une divergence). Le script ne l'ajoute pas, et le point 8 de l'historique ne dit pas qu'il est écarté. Soit écrire la phrase, soit consigner le refus avec sa raison.

## R3 — conforme
- Résumé point 4 et réserve 5 : la condition « avance de N_β0 sur b en “moyen” d'au moins +3 points ; à P4 = 3, 0,00 pour une avance de +1 point ou moins ; adoption exigeant P4 ≥ 3 environ et avance + P4 ≥ 5 environ » est écrite. Contrôle sur la sortie § 17 (forme b4) : avance 3 et 6,6 donnent 0,88 / 0,82 à P4 = 3, 0,23 / 0,23 à 2,5, 0,00 à 1,5 ; avance de −1 à 1 donne 0,00 / 0,00 à P4 = 3 ; la somme ≥ 5 environ se retrouve (avance −0,5 avec P4 = 5,5 : 0,93 / 0,79 ; avance 0 avec P4 = 4,5 : 0,49 / 0,19 ; avance 1 avec P4 = 3,5 : 0,49 / 0,19) et P4 ≥ 3 aussi (avance 6,6 avec P4 = 2,5 : 0,23 seulement). Les « environ » sont honnêtes ; la case avance 2 n'est pas calculée et le texte ne la cite pas.
- Ligne de gel : « 0,23 à P4 = 2,5 au mieux ; 0,00 à P4 = 3 si l'avance … est de +1 point ou moins » : exact (0,23 est le maximum de la colonne 2,5).
- En-tête : la suppression de la confiance de P4 est nommée.
- Reste un renvoi sans condition (ligne 809, tableau de traitement : « 0,88 / 0,82 ; 0,23 ; 0,00 ») : c'est un pointeur vers le résumé, non un énoncé autonome ; sans effet.

## Chiffres et seuils
Le diff ne touche aucun seuil S1 à S17, aucun chiffre du script, aucune valeur recommandée. Nombres nouveaux : +3, +1, 5, 3 (condition R3, tous lisibles dans le § 17), 02:32 (heure du script), et les numéros de contrastes de R2 (présents au § 7).

## Retouche demandée
- **R2(3)** : ajouter une phrase (ou consigner son refus) sur le cas gain_contrôle sur les mondes de décision avec (ii) négatif sur la validation : le verdict suit les tables telles quelles (N non adoptée, ligne 5 de la Table 1 ; non, ligne 3 de la Table 2), sans y voir une divergence.
- Facultatif : code de contraste pour la non-régression au § 7, ou une demi-phrase dans (iii).
