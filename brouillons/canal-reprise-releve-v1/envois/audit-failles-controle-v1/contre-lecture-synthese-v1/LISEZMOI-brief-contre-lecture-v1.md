# Brief — contre-lecture de la synthèse de l'audit des failles de notre contrôle — v1

De : conv-audit, le 2026-10-26 à 13:02:03 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : un sous-agent neuf de la lignée conv-audit, d'un autre modèle que l'auteur de la synthèse (décision de Lazar,
N-052 : analyste sur Opus 5.5, contre-lecteur sur Fable 5.1). Tu n'as écrit aucune pièce de l'audit.

## 1. Ce que tu attaques

`fournis/synthese-v1/audit-failles-controle-v1.md` (`1e43b69c…`, 1 128 lignes) : la synthèse que Lazar lira. Elle juge le
rapport consolidé de Lazar du 26 octobre (v1, `fournis/programme-recu-v1/`, 7 pages, `e066f298…`), affirmation par
affirmation ; elle liste les failles de notre contrôle (documentées, candidates), des rapprochements mathématiques et
seize décisions pour Lazar. Une **v2 de la synthèse est en écriture** (sur la v2 du rapport, 10 pages,
`fournis/programme-recu-v2/`, qui ajoute une troisième partie : cinq failles E à I avec des expériences H1 à H5) : tu
recevras un message pour l'étendre ; commence par la v1.

Les deux rapports sont **confidentiels** (montants, financeur, nom de la page de titre) : ton rapport n'en cite ni
montant, ni financeur, ni nom propre hors Lazar ; vérifie que la synthèse ne le fait pas non plus.

## 2. Pièces

`fournis/` (vérifier : `cd fournis && sha256sum -c ../EMPREINTES-fournis-v1.txt`) : les briefs de l'audit et de la
synthèse (ses règles : niveau de la méthode, jamais de recette ; R7 : chiffre → page ; R8 ; jamais « premier ») ;
`programme/` (programme v2, brief, état de l'art vérifié, décisions) ; `lot-A/` (moisson : 47 modes d'échec, fiches) ;
`lot-B/` (carte, 44 failles internes, grille) ; `complement/` (audit de littérature de session-depot ; neuf cellules du
collisionneur ; brouillons de G1, du papier C, de T0.6 ; lignes de registre) ; les deux rapports et leurs extractions.
Les PDF de la littérature sont sous `/var/tmp/audit-failles-controle-v1/pdf/`, `pages/` et `pdf-main/` (lecture seule) :
tu peux y relire une page citée.

## 3. Ce que tu vérifies, en attaquant

1. **Exactitude** : prends au moins douze affirmations de la synthèse qui portent un chiffre, une page ou une citation
   (choisies pour peser : les cinq failles de tête, les sept formulations du rapport dites fausses, le calcul sur
   l'invariance spectrale de 2.1, les « dix-sept chiffres sans source ») et refais chacune sur la source (page du PDF,
   section de la pièce, script `calculs-synthese-v1.py` rejoué avec `python3 -I`). Dis pour chacune : conforme ; nuance ;
   faux.
2. **Justice envers le rapport** : chaque jugement « ne tient pas », « faux », « voisin publié » est-il établi par une
   source précise, ou est-ce une opinion ? Là où la synthèse dit « voisin », le voisin couvre-t-il vraiment la même
   chose ? Là où elle dit « inédit non trouvé », a-t-elle cherché assez (annexe A) ? Cherche toi-même deux antériorités
   de plus, sur deux « failles candidates » de ton choix, avec les outils que tu as (WebSearch, WebFetch), et consigne tes
   requêtes.
3. **Traçabilité** : chaque faille candidate a-t-elle un mécanisme, ce qu'elle ferait tomber, une antériorité consignée,
   un remède et une expérience ? Chaque décision pour Lazar a-t-elle le format (décision ; enjeu ; options avec avantage
   et inconvénient ; recommandation et confiance ; défaut, aucun pour une dépense) ? Les décisions déjà prises (N-053,
   N-054) sont-elles bien sorties de la liste, et appliquées là où elles changent un verdict ?
4. **Sûreté** : la synthèse reste-t-elle au niveau de la méthode partout ? Signale toute phrase qui serait une recette
   contre un moniteur, même recopiée d'une cellule du collisionneur : elle doit sortir.
5. **Ancrage** : trois « failles candidates » de la synthèse, niées (par exemple « la sonde ne peut pas lire l'indication
   privée »), reçoivent-elles de toi un verdict contraire sur les mêmes pièces ? Si une négation passe aussi bien que
   l'affirmation, la faille n'est pas établie : dis-le.
6. **Ce qui manque** : une faille ou un angle mort de notre contrôle que tu vois et que la synthèse ne voit pas, avec sa
   source ou son statut.

## 4. Ce que tu écris

`sortie/rapport-contre-lecture-synthese-v1.md` et son compagnon : verdict (« transmissible », « transmissible après
corrections », « à refaire ») ; constats `CLS-NN` (bloquant ; à corriger avant transmission ; mineur), chacun avec le
lieu (ligne de la synthèse), ce qui ne va pas, la source, la correction ; les vérifications conformes ; ce que tu n'as
pas pu vérifier ; écarts. Tu ne corriges pas la synthèse.

## 5. Interdits

Rien hors de ce dossier et des dossiers de PDF nommés ; aucun `git`, aucune clé, aucun sous-agent ; réseau seulement
pour les deux recherches d'antériorité du point 2 ; Python avec `-I` ; heures lues sur `date -u` dans la commande qui les
écrit ; écrire seulement sous `sortie/`. Aucun montant, financeur ni nom propre des rapports dans ton rapport.

## 6. Fin

Réponse finale en quelques lignes : verdict, constats bloquants ou à corriger, empreinte du rapport.
