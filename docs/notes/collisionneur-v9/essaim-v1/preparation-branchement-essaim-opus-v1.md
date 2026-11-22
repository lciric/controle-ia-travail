# Mode « essaim » du collisionneur : où il se branche dans la v8d, budget égal entre modes, devis

22 novembre 2026, vers 05:45Z. Pièce de travail (classe C), préparée sans dépense par la session fille des collisionneurs (Opus 5.5), en attendant la conception de Fable (réponses 7 et 8, GO-2026-11-22-17 et -18). Elle ne conçoit pas le mode essaim : elle dit où le brancher et ce qu'il faut tenir égal. La conception de Fable prime.

## 1. Où le mode se branche dans la v8d (b7803838…)

La nouvelle version sera un fichier neuf, `collisionneur_v9_essaim_v1.py`, copie de la v8d (R12). Le mode isolé reste celui de la v8d, inchangé. Ce qui ne bouge pas :
- `executer_cellule` et tout ce qu'il appelle : garde v3 des réglages de Google, comptage de l'entrée, plafond, ligne, relances déclarées, zéro pensée = défaut, coupure comptée au pire ;
- les appelants, le journal, les sceaux, la ligne de reprise.

Ce qui change, cinq lieux :

| lieu de la v8d | rôle aujourd'hui | pour l'essaim |
|---|---|---|
| `TOURS`, `ORDRE_ETAGE` (l. 460-470) | trois tours fixes de l'étage III, limite de mots par tour | un étage neuf (par exemple « E4 ») dont les tours sont ceux de Fable (salon, prépublication, revue entre pairs, correction publique) ; limites de mots fixées pour que la somme par modèle égale celle du mode isolé (section 2) |
| `entrees(tour, lettre, retenues)` (l. 842) | qui lit quoi : T2 lit les T1 des autres, T3 lit son T1 et les T2 des autres | le graphe de lecture de l'essaim : tableau commun des prépublications, revues adressées à une lettre, corrections publiques. C'est le cœur du mode : à écrire comme une table, essayée |
| `CONSIGNES`, `PREAMBULE_GABARIT` (l. 470-505) | consignes par tour ; préambule « N×3 » | consignes des tours de Fable, mot pour mot ; préambule rendu neutre sur le nombre de tours (il dit « N×3 ») |
| `lancer_etage` (l. 2308) | boucle tour par tour, lettre par lettre, porte fermée si une cellule manque | même boucle sur l'étage neuf ; si Fable veut un ordre non synchrone (salon où l'on répond au fil de l'eau), il faut un ordre fixe et scellé, sinon la reprise n'est pas déterministe |
| `verifier`, `cellules_du_run`, `devis`, `pire_tours_2_3` | contrôles et devis des trois tours | étendus à l'étage neuf, avec les mêmes essais (copies des dossiers, faux appelants) |

Points à trancher par la conception, pas par moi :
- le nombre de tours de l'essaim et l'ordre ;
- si un modèle peut ne pas publier ou ne pas revoir (absence voulue) : la v8d ferme la porte sur toute cellule manquante ;
- si les pièces circulent sous leur lettre (comme aujourd'hui) ou sans auteur.

## 2. Garder le budget égal entre modes

En mode isolé, chaque modèle écrit au plus 3 500 + 3 000 + 3 500 = **10 000 mots** de texte en trois appels, sous le même réglage par appel (plafond, provision de réflexion, niveau « high » chez Google, effort « high » chez Anthropic).

Je propose de tenir égal, par modèle et par question :
1. **la somme des limites de mots** des tours (10 000 par modèle) : c'est la seule grandeur que le script fixe d'avance ;
2. **le réglage par appel** (plafond, provision, niveau, effort) : identique, pour que les deux modes réfléchissent autant par appel ;
3. **le nombre d'appels** si la conception le permet (trois par modèle) ; sinon, le déclarer.

Ce qui ne peut pas être égal d'avance : les jetons d'entrée (l'essaim fait lire plus de pièces) et les jetons de pensée. Je propose de les **mesurer et de les rapporter** par mode et par modèle (entrée, sortie, pensée, coût, depuis le journal), et de fixer une garde : un dossier essaim dont le pire cas dépasse de plus de X % celui du dossier isolé de la même question est refusé avant l'envoi (X à fixer par la conception ; je suggère 25 %).

## 3. Devis par dossier

Mode isolé (v8d, cinq modèles de la percée), mesuré par `devis` sur les trois questions des protocoles X déjà accordés : **27,15 à 27,16 USD au pire sans relance**, 15 cellules. Réel observé sur les cinq dossiers de cette nuit pour les tours III.2 et III.3 : 13 à 17 USD par dossier complet.

Mode essaim : à recalculer quand le graphe de lecture sera fixé. Ordre de grandeur, si l'essaim a trois tours par modèle dont deux lisent le tableau entier (cinq pièces de 3 500 mots) : pire cas par cellule voisin de celui du tour III.3 (1,85 à 2,97 USD selon le modèle), soit **28 à 32 USD au pire** par dossier ; réel attendu 15 à 20 USD.

Pour quatre à cinq questions dans les deux modes : 8 à 10 dossiers, **230 à 300 USD au pire**, 120 à 180 USD attendus, plus les trois dossiers essaim des protocoles X déjà accordés (mêmes ordres de grandeur). Au-delà de 45 USD par dossier : nœud, selon la règle de la mère.

## 4. Suite

À réception des réponses 7 et 8 : écrire la v9-essaim (code par Opus 5.5), les essais, puis la contre-lecture par un Opus neuf et la vérification des corrections par le même ; devis par dossier dans vers-mere avant le premier appel.
