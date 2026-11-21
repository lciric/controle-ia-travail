# Rapport de l'auteur v3 du lanceur et du gardien — palier 0b, essai court de mesure — v3

Erratum 2 (68faf068…3848, vérifié par `sha256sum`), vérification v2 et ses essais lus en entier ; mandat et erratum 1 restent en vigueur. Dossier (D) : `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-lanceur-gardien-palier-0b-v3/`. Je n'ai lancé que des factices, jamais le vrai programme. Je n'ai rien écrit sous `/home/user/palier-0b-racine/` ni sous `/home/user/journaux-palier-0b-essai-court-v1/`. Aucun commit (seule une racine git factice jetable existe sous D/essais), aucune dépense, aucun refus de permission, de classifieur ou de garde. Je n'ai arrêté que mes factices, par leur identifiant, et j'ai vérifié leur absence par `stat`.

## Fichiers et empreintes (sha256)

Seules deux pièces changent :
- `gardien-essai-court-v3.py` — d8fd650b0e96144fd40261fc244bd28636ba2e51215dd3606520aa67f068b4c7 (corrections 1 et 2) ;
- `demarrer-gardien-essai-court-v3.sh` — 97586b7b4e5b9a3f139b3e921626336d0a37232bbbb0a8bde937b963b94de428 (seul changement : le nom du gardien lancé).

Inchangées, copiées à l'octet dans D pour que le rejeu ne dépende de rien d'autre :
- `lancer-essai-court-v2.sh` — 4c96c703…13f3 ;
- `demarrer-essai-court-v2.sh` — 2ec06e95…0e38 ;
- `verifier-commande-v2.py` — 68a74c7c…861f ;
- les deux extractions du complément 1 v3 — 1484cd75…7268 et 56ed20f8…b867.

Emploi : copier ces quatre pièces dans le dossier de tenue, puis lancer `demarrer-essai-court-v2.sh TENUE` et aussitôt `demarrer-gardien-essai-court-v3.sh TENUE`.

Essais (D/essais/, empreintes dans `essais/empreintes-essais-v3.txt`) :
- `rejouer-tout-v3.sh` : la base est tirée de l'emplacement du script et n'écrit que sous D ;
- `scenario-v3.sh`, `jouer-scenario-v3.sh`, `lanceur-py-v3.sh`, `lanceur-bref-v3.sh`, `prog-v3.py`, `decoy-v3.sh`, `decoy-perime-v3.sh`, `argv-v3.sh`, `ecrivain-externe-v3.sh` ;
- copies non modifiées : `auteur-v1-copie/`, `contre-lecture-v1-copie/`, `verification-v2-copie/`, `v2-copie/`.

Sorties dans `essais/resultats/final-*.txt`.

## Ce qui change dans le gardien

1. **Garde continuée sur les descendants.**
   - Dès qu'un relevé a vu le processus lancé identifié, le gardien le retient.
   - Si ce processus devient absent alors que des descendants relevés vivent encore (identifiant et heure de départ égaux), le gardien écrit une ligne « la garde continue sur eux ». Il garde ses lignes de minute et applique les deux arrêts.
   - Ces arrêts se font en mode « descendants » : signal de fin par identifiant, et au groupe tant qu'il porte un descendant relevé ; puis arrêt forcé au délai, de la même façon.
   - Il ne part que lorsque tous ont disparu, avec la dernière ligne « programme et tous les descendants relevés absents : dernière ligne, fin du gardien ».
2. **Dossier figé prouvé.**
   - Après l'arrêt et avant la mesure, le gardien relève deux fois, à une seconde d'écart : n, le nombre de fichiers, les octets apparents et alloués de `etape-4`.
   - Si les deux relevés sont égaux, il écrit « dossier figé (paire k) » avec les deux relevés.
   - Sinon il refait au plus dix paires, puis écrit « dossier NON figé » avec les deux derniers relevés. Chaque ligne de projection est alors préfixée « [dossier NON figé] ».
   - n et s4 sont pris sur le dernier relevé. t_arrêt reste l'heure d'envoi du signal.

## Table des essais (rejeu `final`, 17:17:18Z à 17:22:02Z, puis trois compléments jusqu'à 17:24Z)

| Correction | Cas sain | Artefact | Attendu | Rendu |
|---|---|---|---|---|
| E2.1 descendant vivant | `e2c1-sain` : chef tué de l'extérieur à 3 s, descendant qui finit seul à 8 s ; `chef-tue` de la vérification : descendant de 20 s | `e2c1-place` : chef tué, descendant qui écrit 300 Mo et passe sous un seuil de place factice (place libre au départ moins 100 Mo), avec un témoin sans lien ; `e2c1-mesure` : chef tué, n atteint 12 ; `e2c1-sourd` : chef tué, descendant sourd au signal de fin | Sain : garde continuée, aucun arrêt, départ quand le descendant a fini. Artefacts : arrêt du descendant par identifiant et au groupe, arrêt forcé si sourd, témoin intact | Sain : « la garde continue sur eux [2011] », aucun `arret-gardien.txt`, dernière ligne « …tous les descendants relevés absents… » ; même chose pour `chef-tue` (n = 40). Place : « arrêt de place… arrêt des descendants relevés… [2104] », signal de fin au groupe, tous absents, témoin vivant. Mesure : arrêt sur n = 13, « dossier figé (paire 1) ». Sourd : « après 5.0 s, encore présents [2395] », arrêt forcé du groupe, n = 23 figé. |
| E2.2 dossier figé | Toute mesure ordinaire : s4, s6, s8, h1, h3 (833 = 833), h4, c2, c5, rapide (818 = 818), sourd-groupe, sourd-hors, docile-hors, e2c1-mesure, e2c1-sourd, s7bis | `ecrivain-externe-v3.sh` : écrivain hors de l'arbre du programme, déterministe ; `orphelin` de la vérification | Sain : « figé ». Artefacts : « NON figé » et projection marquée | Sain : « dossier figé : … (paire 1) » partout. Écrivain : « NON figé : 10 paires… n 53 puis 58 », projection préfixée. Orphelin, deuxième passage : « NON figé », n 54 puis 59 ; B arrêté ensuite par moi. Orphelin, premier passage : le gardien a relevé B pendant la courte vie de A et l'a arrêté par identifiant ; le dossier était alors réellement figé et a été déclaré tel (n = 8). C'est conforme, voir l'écart 2. |
| Erratum 1, corrections 1 à 6, rejouées | — | — | — | Identité : decoy sans fichier d'heure, heure décalée de −7, fichiers périmés : aucun signal, témoins vivants ; heure exacte (objet vrai) : signal, témoin arrêté par le gardien. s9 : aucun signal. Groupe : h4 et sourd-groupe, arrêt forcé ; c2-sain, pas d'arrêt forcé. Hors groupe : h1, sourd-hors, docile-hors, par identifiant ; témoin h1 intact. c5 : empreinte de l'inventaire égale à `sha256sum` (345d7a…a277), mêmes décisions qu'en sain. c6 : « aucun » contre « oui (1 : …/arret-factice.txt) ». `essai-arret.py` : lien brisé, fichier à profondeur 6 et dossier comptés ; `darret` et `Arret` non comptés. Projections v1 et v2 : 0 échec. |
| Auteur v1 | — | — | — | Refus v0 à v7 : 0 échec. s1, s3, s5 : code 0, aucun arrêt. s2 : arrêt de place. s4 : arrêt sur n, figé. s6 : arrêt sur la durée. s8 : « projection impossible ». s9 : aucun signal. s7bis (délai d'emploi 60 s) : « après 60 s, encore présents [4436, 4456] », arrêt forcé du groupe, tous absents. |
| Commande | lanceur v2, deux extractions | trois lanceurs altérés | Sain : ÉGAL (0). Artefacts : ÉCHEC (1) | Conforme. Seul le 10e argument diffère ; les deux extractions sont égales entre elles. |

Calcul refait à la main (écrivain) : 2,039446 s × 648 / 57 = 23,2 s, égal au fichier de mesure.

## Écarts
1. **s7 dans le rejeu `final`.** Il était déclenché par la place dès le premier tour. Le signal de fin est parti avant que le programme factice ait posé son refus de ce signal : arrêt sans forçage. C'est une course de l'essai, la même que la trouvaille (b) de la vérification, et non un défaut du gardien. J'ai rejoué le cas en s7bis, déclenché par n = 2 : arrêt forcé à 60 s. `rejouer-tout-v3.sh` a été corrigé dans ce sens après le rejeu, sur cette seule ligne ; le rejeu `final` a tourné avec la version d'avant.
2. **Petit-enfant détaché.** Le cas dépend d'une course : sur trois passages, deux rendent « NON figé », un relève B et l'arrête. D'où l'artefact déterministe ajouté (écrivain externe).
3. **Seuil de place factice de `e2c1-place`.** Il est fixé à la place libre moins 100 Mo, et le descendant écrit 300 Mo, laissés sous D. Ce n'est pas un remplissage du disque (environ 38 Go libres), mais le cas dépend de l'absence d'autres écritures de plus de 100 Mo pendant les quelques secondes de l'essai.
4. **Mesure plus lente.** Elle prend au moins 1 s et au plus 10 s de plus, pendant lesquelles aucune ligne de minute n'est écrite.
5. **Garde sans fin possible.** Un descendant relevé qui ne finit jamais garde le gardien en vie. C'est voulu par l'erratum : les arrêts s'appliquent toujours à ce descendant.

## Limites
- Un descendant détaché puis orphelin entre deux relevés échappe toujours aux signaux. Il est désormais **signalé** par « NON figé », s'il écrit encore pendant la mesure.
- Une réécriture de même taille, ou une écriture qui ne change ni les noms, ni le nombre de fichiers, ni les tailles, n'est pas vue par la preuve de gel. Le gardien ne lit que les noms et les tailles.
- Le vrai programme n'est pas éprouvé ; les factices sont plus simples que lui, et l'intervalle des essais est de 1 s.

## Relevé de méthode

**Chaîne de raisonnement.**
1. Le défaut 2 de la vérification (le gardien part, le descendant vit) est reproduit par `chef-tue` sur la v2 (vérification, mode 2). En v3, la boucle ne rend la main que si le processus lancé est absent **et** qu'aucun descendant relevé ne vit (`garder`). Les contrôles s'appliquent dans ce cas (`controles`), et `arreter` a un mode « descendants » (lecture du code ; essais `e2c1-*`, `chef-tue`).
2. Le signal au groupe en mode « descendants » ne part que si le groupe porte encore un descendant relevé (`groupe_continu`). Un numéro de groupe ne peut être repris tant qu'un membre le porte.
3. Le gel est prouvé par l'égalité de deux relevés (`figer`) : l'écrivain externe et l'orphelin rendent « NON figé », les dossiers réellement figés rendent « figé ».
4. Rien d'autre ne change : identité, groupe, hors groupe, contenu, colonne, projections et commande sont rejoués (table).
5. Supposé : la conduite du vrai programme au signal de fin.

**Objets de contrôle.**
- Garde continuée : faux par construction (descendant fini seul) → attendu : aucun arrêt ; rendu : aucun arrêt. Vrai par construction (descendant sous seuil de place, n atteint, sourd) → attendu : arrêté ; rendu : arrêté. Témoin sans lien → intact.
- Gel : vrai (dossiers finis) → « figé » ; faux (écrivain externe, orphelin) → « NON figé ».
- Les objets vrai et faux de l'erratum 1 sont rejoués et conformes. Aucun mécanisme n'a réussi là où la conclusion était fausse.

**Premier pas non justifié.** Pas 5 : le comportement du vrai programme au signal de fin. Le justifierait un essai du vrai programme dans un dossier jetable, hors de mon mandat.

**Mode d'échec affecté.** Sans objet : je suis l'auteur, non un relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation.

**Trouvaille de côté.**
- (a) Le petit-enfant détaché n'échappe que par une course (voir l'écart 2).
- (b) Un essai déclenché au premier tour peut ne rien éprouver d'un programme qui ignore le signal de fin (s7 du rejeu `final`).

**Évaluateur et conseil.** Me jugeront un contre-lecteur, puis la session ; mes témoins admis sont les objets vrai et faux construits. Le produit pourrait être bien jugé sans le mériter de trois façons :
- les factices sont écrits par moi ;
- le seuil de place factice dépend de la place libre au moment de l'essai ;
- l'orphelin dépend d'une course.
