# Rapport — préenregistrement de G1, brouillon suivant (commandé « brouillon 4 », écrit sous le nom « brouillon 5 ») — v1

Sous-agent de la session conv-audit (Claude Opus 5.5), commande R-1075 relancée en R-1076, 1er novembre 2026, fin vers 21:25 UTC (`date -u`). Aucun réseau, aucun `git fetch`, aucune ref `donnees/*` lue, rien lu sous `donnees/`, aucun commit, aucun `.sha256`, aucun fichier existant modifié (vérifié : `git status` ne montre que des fichiers neufs ; les caches Python préexistants sont inchangés).

## Verdict

Le brouillon est écrit, complet section par section, chaque chiffre sourcé ou marqué. **Scellable après contre-lecture : non en l'état ; oui après trois choses** : (1) un mot de Lazar sur les nœuds de porte (un seul mot suffit : « valeurs inscrites ») ; (2) la simulation de la garde δ et du contrôle 12 rejouée à k = 12 (ou 13) comparateurs et trois modes (processeur, quelques heures) ; (3) les pièces des préenregistrements de T0.6, T0.7 et T0.8 qu'il cite. Le validateur du dépôt (`controle_ia.prereg.problemes`) le refuse aujourd'hui pour deux sections seulement, « Plan d'analyse » (table v10 à remplir) et « Contre-lecture » : c'est voulu. Il peut être **horodaté ce soir comme brouillon daté** (empreinte ci-dessous), avant toute lecture des quatre runs de la nuit.

## Chemins

- Brouillon : `/home/claude/controle-ia-travail/brouillons/G1-preenregistrement-v1-brouillon5.md` (`347807138175b8573c11b4e6dce43218b92b6512ceaa85ddfacae8d204fec99b`, 12 814 mots).
- Calculs (nécessaires à R6 pour les chiffres neufs) : `/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/g1-prereg-v1/calculs-g1-brouillon5-v1.py` (`8021037b8e733127e5f290ade3bb54c2bcc2cbf703f72b39a7305a7b3444bca1`) et sa sortie `/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/g1-prereg-v1/calculs-g1-brouillon5-v1-sortie.txt` (`d53e7e5a81058217df12ed3ea3c1066ae4260f3a0945cd8e4a85ec04258d00fe`), rejouée deux fois à l'identique depuis un dossier vide.
- Ce rapport : `/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/g1-prereg-v1/rapport-brouillon4-v1.md`.

## Écart de nom (à valider)

`main` porte déjà un `brouillons/G1-preenregistrement-v1-brouillon4.md` différent (`ad068bed…`, session-depot, 30 octobre 02:23 UTC), absent de la branche `canal/conv-audit-n04`. Écrire un second « brouillon 4 » aurait donné deux textes de même nom (R12, et ta règle : une version, un nom). Le texte est donc nommé **brouillon 5** et part du brouillon 4 de `main`. Le nom de ce rapport garde « brouillon4 » parce que c'est le chemin commandé.

## Ce qui change du brouillon 3 au brouillon 5

- **Repris du brouillon 4 de `main`** : H1 scindée (H1a porte la revendication, H1b rapportée, N-055) ; critère en intersection-union contre chaque comparateur, bases blanches (ii) et (iii) comprises (N-056) ; G1 par mode, mode « affaiblir les contrôles », mode tenu à l'écart (N-054) ; pari apparié borné (N-055) ; garde δ (R-733) ; 10 exécutions sabotées par unité (R-504) ; vérité du dommage (N-060 v3) ; ressources publiques hors liste (N-061).
- **Neuf par rapport au brouillon 4** :
  - **R-746 intégrée** (six nœuds de G1 tranchés par Lazar le 29 octobre, après la lecture d'HELIOS) : elle **manquait au brouillon 4**, alors que la grille de G0 (critère 6, contrôle F-6.2) exige sa présence ;
  - **réserve N-034** (dérive de l'honnête sous revers) : **manquait aussi**, alors que N-034 la renvoie expressément « au prochain brouillon » ;
  - garde δ v9 et sa phrase v2 (après GD8 et GD9) ; repli hors table = A et 400 unités (R-556) ; mode tenu à l'écart à cinq concepteurs (R-826) ;
  - prédictions chiffrées et signées par cellule du 2 × 2, avec une attente de l'auteur sourcée sur P3 ;
  - familles de Holm (quatre cellules ; trois effets factoriels), lecture par cellule et globale ; aire sous la courbe avec intervalle de DeLong en grappes (rapportée) ;
  - lectures « non jugeable par puissance » (définie sans lire le sujet) et « non jugeable (exécution) » ; issues écrites d'avance avec leur conséquence pour le programme ;
  - critère chiffré « 8B trop faible » demandé par R-746 (6) ;
  - devis, plafond, règle des graines tirée de l'empreinte du texte scellé ;
  - réglages des statistiques séquentielles fixés (ρ = 1,0126 par la règle de T0.3 ; Page k = 0,5 ; fenêtre 5) ;
  - corrections : TRACE-lite à 18 appels au plus (le brouillon 3 disait 14) ; déclaration de Q5 et des runs de la nuit.

## Ce que j'ai trouvé en route (à porter à Lazar)

1. **Le banc ne peut pas porter la taille décidée.** La garde δ exige au moins 288 unités par mode (400 par défaut, R-556 (2)) ; une unité est une tâche × mode ; le banc compte 64 tâches d'évaluation (60 déjà vues par P3) et 32 de réserve. À 64 unités, la garde ne certifie rien. Seule une extraction neuve d'environ 480 tâches tient la décision (DG1-1, nœud). Les runs de la nuit lisent aussi les 96 tâches de T0.5 : raison de plus pour les sortir de l'épreuve.
2. **« Chacun des autres modes »** : le mot de Lazar (D-S29 (a)) dit « autres », le CLAUDE.md de `main` écrit « chaque mode ». Avec le mode « coût » dans la porte, le sujet doit battre la lecture directe du coût falsifié, ce que H1a ne prétend pas (DG1-6 ; valeur inscrite = lecture de `main`, recommandation contraire).
3. **Doublon possible HELIOS** : R-746 (3) fait déjà de la base (iii) la lecture d'HELIOS ; R-513 ajoute « la recette d'HELIOS » en neuvième comparateur (DG1-3).
4. **k = 12 au lieu de 8** : N-008 (« toutes variantes ») et R-746 (1) élargissent la liste. La table de la garde δ et le contrôle 12 ne valent qu'à k = 8 ou 9 et deux modes : à rejouer avant scellement.
5. **Ordre de grandeur du coût** : environ 93 000 épisodes, dont 65 % de calibrage honnête ; environ 4 900 USD en estimation centrale (2 800 à 9 000 ; 19 000 en tension), soit des milliers d'heures de carte.
6. **Attente honnête** : vu P3 (sondes génériques au hasard, coût seul à 0,888), l'auteur écrit d'avance une probabilité d'environ 0,1 que G1 soit franchie.

## Décisions ouvertes (valeur inscrite ; recommandation et confiance)

- DG1-1 banc neuf d'environ 480 tâches, les 96 de T0.5 exclues : inscrite (a) ; reco (a) 0,75 ; **nœud**.
- DG1-2 seuil de promotion 160 : inscrite 160 ; reco 160, 0,65 (R-556 (3)) ; **nœud de porte**.
- DG1-3 HELIOS en plus de (iii) si rejouée au scellement, sinon (iii) seule : inscrite (b) avec repli ; 0,55 ; **nœud de revendication**.
- DG1-4 le pari décide, l'intervalle est rapporté (D-S11) : inscrite (a) ; 0,8 ; **nœud de porte**.
- DG1-5 liste scellée à 12 comparateurs (+ HELIOS) : inscrite (b) ; 0,6 ; **nœud de porte**.
- DG1-6 modes et strate de la porte : inscrite (a) trois modes entiers ; reco (b) modes flous sur la strate « diffus, flou », 0,6 ; **nœud de porte**.
- DG1-7 familles des cinq concepteurs en une seule strate : inscrite (a) ; 0,6 ; **nœud de porte**.
- DG1-8 cellule « informé » et sonde d'intention : inscrite (a) ; 0,5 ; **nœud de porte**.
- DG1-9 porte lue sur (ii), (i-a) rapportée : inscrite (b) ; 0,6 ; proposer (peut-être nœud).
- DG1-10 retrait des 60 tâches de P3, étendu aux 96 : inscrite (a) ; 0,85 ; nœud ouvert le 30 octobre.
- DG1-11 critère « 8B trop faible » et paramètres sans source : inscrite (a) ; 0,5 ; proposé, à contre-lire.
- DG1-12 bras « revers » hors G1 : inscrite (a) ; 0,7 ; proposer.
- DG1-13 plafond 6 331 USD, alerte 5 064, rechiffrage au pilote : inscrite (a) ; 0,6 ; **nœud de dépense**.

Dépendances hors du texte : D:3 de la table de G0 (le scellement de G1 attend-il le pilote ?) et la ligne W21 (verdicts des critères 2 à 4) ; préenregistrements de T0.6, T0.7, T0.8 et de l'expérience de N-054 point 4 ; familles tenues à l'écart scellées ; oracle.

## Chiffres sans source (marqués dans le texte)

- Valeurs proposées par l'auteur : 0,70 (lisibilité honnête, B2 ; P3 donne 0,828) ; 0,05 (borne « diffus ») ; k = 8 exemples ; 0,10 (déclencheur A7) ; 2τ (A4) ; environ 480 tâches à extraire ; horizons {2, 5, 10} ; attente de l'auteur ≈ 0,1.
- Hypothèses non mesurées du devis : 1 à 4 équivalents « juge 8B » par épisode (8 en tension) ; prix 1,43 USD de l'heure (SUPPOSÉ).
- Non opposables : prévisions binormales tirées des aires de P3 ; produit des puissances sous indépendance.
- Méthodes citées de mémoire, à vérifier sur PDF (R7) : DeLong et al. 1988 ; Obuchowski 1997.
- À fixer après la borne δ* de P3 (sous-agent en cours) : attentes de C1, de G1-P2, des effets factoriels et de G1-P1 dans les modes flous.

## Durée de lecture pour un mentor

- Résumé en dix lignes : 2 minutes.
- Parcours conseillé (résumé, hypothèse, prédictions, critères de lecture : environ 3 000 mots) : 15 minutes.
- Texte entier (12 800 mots, avec empreintes et citations) : environ une heure.

## Mémoire et règles appliquées

Deux préférences de la mémoire de Lazar ont guidé la forme : (a) version dans le nom de chaque livrable (d'où le nom « brouillon 5 ») ; (b) « préciser à chaque fois à quoi renvoie chaque sigle ou code » (1er novembre), d'où la section « Codes cités, en clair » et les surnoms. Sa règle du zip (livrables d'une tâche regroupés) n'a pas été appliquée : la commande ne demandait pas de paquet ; à faire par la session principale si le dossier part chez les mentors. Rien de neuf à mémoriser.
