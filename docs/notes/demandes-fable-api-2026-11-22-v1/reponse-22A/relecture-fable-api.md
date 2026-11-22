# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHovkrSL1oZh94qEhKqF`
- Heure (UTC) : 2026-11-22T10:31:02Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-22A-revue-revendications-papier-A-v1.md` — sha256 4da7de88376c10df1825791634ae407646ee3f06660e363795928279c543f8f7 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-2/relecture-fable-api.md` — sha256 542b7bfc86497c0c9bc45ed7f1651162a47789b6b2f00325f989daaac42c59f3 (compagnon : vérifié)
  - remarques : `docs/notes/seconde-lecture-these-v1.md` — sha256 a4f751ce3981aa100d026e9b90a9214897f639717bdcc9c31a5680d32cfcfdf4 (compagnon : vérifié)
  - remarques : `docs/notes/lecture-steganographie-comptabilite-v1.md` — sha256 6d52ba5d033d5a71237337a6c27f6f257d80c8ecbfb7a32dbae30cc569ce8ac6 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22/relecture-fable-api.md` — sha256 22c5652113797a399d1d1df7fc8d4d6b100bcf04bd655118d51238c5ef3d7b64 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 9f05a9b14f16df48ae57cd9bbd726f3f25c7c8ff69e2cfe97f34ee9f1c5876c6
- Jetons : entrée 71640, sortie 11965 (dont réflexion 3657), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.051720 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 22A — revue des revendications du papier A : réponse approfondie

**Conclusion d'abord.** Sur les huit revendications du papier A, deux sont retirées comme résultats (lemme, théorème négatif), une l'était déjà (marge asymétrique, N-077), une est à remplacer (accumulation toujours valide, vraie par construction sous la loi héritée), deux sont à resserrer (gain de l'accès interne, transposition du jeton à l'action) et deux ne sont pas touchées. La thèse retenue tient, mais son modèle nul n'est pas celui qu'on cite. Avec une référence faite d'exécutions jumelles, le régime n/√m n'apparaît pas, et le nul effectif est « racine, plus un terme entre tâches, plus une dérive ». La porte G1 porte un problème de référence que personne n'a compté : le seuil à 1 % de faux positifs est lui-même estimé. Confiance d'ensemble : 0,6.

**Réserves.**
- Je n'ai lu aucun PDF ; les trois notes de lecture sont mon seul accès aux pages.
- Je n'ai ni le texte des décisions (N-003, N-004, N-075 à N-077), ni la ligne exacte de la thèse retenue.
- Les identifiants arXiv de 2026 viennent des notes ; je n'en confirme aucun.
- Les réponses 2, 9 et 22 sortent du même modèle que celle-ci : mon accord avec elles n'est pas une confirmation indépendante.
- Les empreintes ne sont pas recalculées. Je ne nomme que les auteurs des travaux cités.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Écrire le nul dans le plan réel du programme** [PROPOSITION]. La loi de Ker 2010 compte m et n dans la même unité. Il faut la dériver pour r exécutions jumelles par tâche, puis pour une référence par régime.
- **Compter la référence du seuil** [PROPOSITION]. Un rappel « à 1 % de faux positifs » suppose un quantile honnête connu ; il est estimé sur un nombre fini d'épisodes.
- **Rejouer l'antécédent avant de le qualifier** [PROPOSITION]. Le tableau 2 de Zhang et Gao peut se recalculer à la main (constat 3).
- **Chercher, pour chaque énoncé gardé, s'il est vrai par construction** sous le nul cité [PROPOSITION].
- **Graduer chaque « non trouvé »** par la recherche qui le fonde [PROPOSITION] : six pièces lues, 13 pages sur 39 chez Parrack et collaborateurs, quatre arbres de citations non parcourus.

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.
- Les scores pas à pas des exécutions honnêtes au dépôt : tâche, exécution, rang du pas, pour chaque moniteur sur les mêmes actions.
- Le nombre d'épisodes honnêtes qui fixe chaque seuil de G1.
- Le texte de N-003, N-004, N-076 et de la thèse retenue.
- Les pages non lues : Parrack et collaborateurs, p. 12 et 15 à 39 ; Zhang et Gao, p. 10 et 11, ainsi que le paramètre d'autocorrélation de leur attaque.
- Les arbres de citations de Ker 2006, 2007 et 2010, d'Arias-Castro et collaborateurs, d'Avenhaus et Jaech.

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS.
- **Tableau de revendications** élément par élément contre la page, typé : théorème, méthode, mesure, protocole.
- **Modèle à composantes de variance** (tâche, exécution, pas), avec rééchantillonnage par tâche.
- **Intervalle de la loi bêta** sur le taux réel de fausses alertes d'un seuil empirique.
- **Banc à vérité plantée** : scores synthétiques d'exposant et de terme entre tâches connus, pour vérifier que l'ajustement retrouve ce qu'on y a mis.
- **Substituts par permutation des pas** ; simulation du franchissement séquentiel (sabotage tôt, tard, étalé).
- **Unions recalées** au même taux total de fausses alertes, pour la complémentarité.

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.
- Le recalcul du tableau 2 de Zhang et Gao : une page et un paramètre suffisent.
- Le banc à vérité plantée et l'essai « jumeau contre jumeau », dont l'issue ne dépend d'aucun avis.
- Un spécialiste de stéganalyse, sur la table de transport du nul.
- Les auteurs de Parrack et collaborateurs, à qui l'on demande : « avez-vous analysé les cas manqués par la boîte noire ? »
- Des énoncés témoins au statut connu, mêlés aux nôtres dans l'envoi au collisionneur.
- La prévision scellée, puis une seconde famille de modèles.

## Demande reformulée

« Pour le seul papier A, voici la table des revendications du 19 novembre, la thèse retenue (loi héritée comme modèle nul, bilan mesuré chez des agents, complémentarité en second axe ; lemme et théorème retirés comme résultats) et trois notes de lecture sur PDF. Pour chaque revendication, la porte G1 et chaque axe de la thèse : (1) découpe l'énoncé en éléments et confronte chacun à la page de l'antériorité la plus proche ; (2) dis s'il est exact tel qu'écrit, et s'il est vrai par construction sous le modèle nul cité ; (3) écris ce modèle nul dans les unités et le plan de référence réels du programme, et dis quels régimes y sont observables ; (4) rends un verdict : tenue, à resserrer, à retirer, à remplacer, non touchée ; (5) pour tout énoncé neuf, donne l'épreuve qui le réfute et la taille d'échantillon qu'elle demande ; (6) gradue chaque "non trouvé" ; (7) signale tout retrait excessif ; (8) liste les phrases à ne plus écrire. Marque fait rapporté, hypothèse, proposition. Aucune zone vierge n'est déclarée libre. Les autres papiers : une ligne de dépendance chacun. »

## Réponse à la demande reformulée

### Quatre constats avant la table

1. **Le nul effectif n'est pas √(n + n²/m)** [HYPOTHÈSE, dérivation reprise de la réponse 9 et poussée].
   - Avec r jumelles de même longueur, m = r·n. Le seuil reste en racine, gonflé de √(1 + 1/r).
   - Le régime n/√m ne s'observe donc que si une référence courte est extrapolée, ce qui suppose des pas stationnaires.
   - Le nul à ajuster devient : variance du cumul ≈ σ²·n^(2H)·(1 + 1/r) + τ²·n², où τ est l'écart entre tâches et H l'exposant.
   - La loi de Ker 2010 se cite ; ce que le papier mesure, ce sont H et τ.

2. **La porte G1 a sa propre référence** [HYPOTHÈSE, ordre de grandeur de ma main, à refaire].
   - Un seuil placé au 99ᵉ centile de 200 épisodes honnêtes repose sur deux dépassements attendus.
   - Son taux réel de fausses alertes se situe alors, à 95 %, entre environ 0,1 % et 3 %.
   - Deux moniteurs comparés « à 1 % » peuvent donc l'être à des taux réels qui diffèrent d'un facteur dix.
   - N-076 demande déjà de déclarer m ; il faut l'appliquer au seuil, en épisodes.

3. **Le tableau 2 de Zhang et Gao se lit comme un cas de la distinction de N-003** [HYPOTHÈSE, calcul de ma main].
   - Leur attaque préserve les marginales par coordonnée, non le multi-ensemble des scores à longueur finie.
   - Sous autocorrélation ρ, la variance de la moyenne est multipliée par environ (1 + ρ)/(1 − ρ).
   - Une puissance de 0,048 à 1 % (seconde lecture, p. 7) correspond à un facteur proche de 1,95, soit ρ ≈ 0,3.
   - Si leur paramètre est de cet ordre, la réserve de la seconde lecture est confirmée sans simulation. S'il en est loin, notre lecture est à revoir.

4. **La puissance annoncée par la réponse 22 se retrouve** [HYPOTHÈSE, calcul de ma main].
   - Sur une décade d'horizons, un exposant de 0,6 au lieu de 0,5 change l'écart-type du cumul de 26 %.
   - Le déceler à 80 % de puissance demande environ 150 tâches indépendantes à chaque extrémité, sous loi normale.
   - Le terme τ se décèle bien plus tôt, car il croît en n. C'est la prévision la plus sûre à sceller.

### Table

« Stég » désigne la lecture de la stéganographie, « Lect2 » la seconde lecture, « Rech » la recherche exhaustive. La colonne « antériorité » est FAIT RAPPORTÉ par la pièce citée ; verdicts, énoncés neufs et épreuves sont des PROPOSITIONS.

| Revendication | Antériorité qui la touche | Verdict | Énoncé neuf | Épreuve qui le réfuterait |
|---|---|---|---|---|
| Gain de l'accès interne (H1a) | Parrack, Attubato, Heimersheim 2025, p. 1-8 (Lect2, § 3) : gain moyen par réponse sur la tromperie ; portes dérobées dans le code, boîte blanche 0,776 contre 0,899. | Tenue, à resserrer : parent et indice contraire écrits à côté de la prévision. | Second axe : « à taux total de fausses alertes égal, l'union "meilleure boîte noire et sonde" rattrape plus de sabotages diffus que l'union "meilleure boîte noire et seconde boîte noire d'une autre lignée". » | Borne haute de l'écart inférieure ou égale à zéro sur la famille tenue à l'écart. |
| Interaction flou contre net (H1b) | Aucune des trois pièces. | Non touchée (mesure). | — | — |
| Accumulation toujours valide (H2) | Ker 2010, p. 7 et 11 (Stég) ; Filler, Ker, Fridrich 2009, p. 3-5 (Lect2) ; Khilar 2610.13083, propositions 3-4 ; Makins et collaborateurs 2607.07368, p. 45 (Rech). | À remplacer : « rappel qui croît avec l'horizon » découle du nul. | « À déplacement par acte fixé, le rappel suit le nul (racine, terme entre tâches, dérive) ; la garantie vaut sous une référence honnête déclarée ; l'écart au nul est le résultat. » | Jumeau contre jumeau : la surface du seuil honnête s'ajuste au nul sans résidu, avec H = 0,5 et τ = 0. |
| Théorème négatif (T) | Zhang et Gao 2606.10456, p. 3, 7-8 ; Arias-Castro, Bubeck, Lugosi 2012, p. 14-20 (Lect2) ; Khilar, proposition 1 (Rech). | Retiré comme résultat (décidé). La distinction de N-003 reste exacte : remarque citée. | Question de diagnostic : le sabotage des organismes déplace-t-il la position des scores de sondes, leur dépendance, ou les deux ? | Tests de position et de dépendance, étalonnés sur substituts permutés : aucun ne dépasse son niveau. |
| Lemme d'additivité (L) | Avenhaus et Jaech 1981, p. 25, 30-31 ; Ker 2006, p. 6-7, 9 (Stég) ; Tailor 2510.04303, p. 12 ; Ghanem 2608.02698, p. 5 (Rech). | Retiré comme résultat (décidé) ; cité en outil ; repli de N-004 à fermer. | Question : en séquentiel, l'étalement est-il le cas le moins favorable au défenseur ? | Simulation : taux de franchissement égaux pour tôt, tard, étalé. |
| Marge asymétrique (H6) | Aucune des trois pièces ; N-077. | Déjà retirée ; ligne de la table à corriger. | Mesure descriptive. | — |
| Transposition du jeton à l'action (Tr) | Makins et collaborateurs, p. 1 (Rech) : le maximum baisse sous fragmentation. Arias-Castro et collaborateurs, p. 18-20 (Lect2) : histogramme puissant en régime rare. | À resserrer : « angle mort identifié » devient une question. | « La robustesse du maximum mesurée au jeton tient-elle à l'action, sous fragmentation ? » | Montage de fragmentation : le maximum par action ne baisse pas. |
| Validité et robustesse (H8) | Aucune des trois pièces. | Non touchée (diagnostic). | — | — |
| Porte G1 | Aucune ; constat 2. | À compléter. | « Chaque seuil déclare son nombre d'épisodes honnêtes et l'intervalle de son taux réel. » | Intervalles disjoints entre moniteurs comparés. |
| Règle de la référence (N-076) | Ker 2010, corollaire 1, p. 11 (Stég) ; Wen et collaborateurs 2411.17693, p. 18 (Rech). | À resserrer : « application du corollaire 1 », unité commune à fixer. | Aucun. | — |
| Thèse, axe « bilan mesuré » | Khilar, proposition 4, p. 5 (loi chiffrée contre l'extraction) ; Makins, p. 45 ; Zhang et Gao, p. 8 (dépendance honnête en boîte noire) (Rech, Lect2). | Tenue, resserrée : le propre se réduit aux scores de sondes, au plan de référence et aux composantes de variance. | Constat 1. | Banc à vérité plantée : l'ajustement ne retrouve pas H et τ plantés. |

### La thèse retenue, revue

- **Ce qui se cite** [FAIT RAPPORTÉ, Stég et Rech]. La loi en racine, la référence estimée, l'indifférence de la somme et la transposition au suivi des usages (Khilar 2026) sont publiées.
- **Ce qui se mesure** [PROPOSITION]. Quatre grandeurs, sur des scores de sondes d'agents :
  - l'exposant H ;
  - le terme entre tâches τ ;
  - la constante de chaque moniteur ;
  - le gain de l'union.
- **Prévisions à sceller, par ordre de solidité** [HYPOTHÈSE ; chances en jugement].
  - Avec une référence par régime, le terme τ domine avant la fin des tâches longues (0,6).
  - Le rapport des constantes entre sonde et juge de texte ne dépend pas de l'horizon (0,5).
  - L'union avec la sonde dépasse l'union avec une seconde boîte noire (0,4).
  - H dépasse 0,5 (non chiffré tant que la puissance n'est pas calculée).
- **Hypothèse la plus exposée** [HYPOTHÈSE]. Filler, Ker et Fridrich gardent l'exposant un demi sous une chaîne stationnaire (Lect2, p. 3-5). Une tâche d'agent a un début et une fin.
- **Biais de la complémentarité** [HYPOTHÈSE]. Conditionner sur les cas manqués par la meilleure boîte noire avantage tout moniteur peu corrélé au premier. Seule la comparaison de deux unions recalées est juste.
- **Retrait excessif à éviter** [FAIT RAPPORTÉ, table]. N-003 avait déjà déclaré la forme « puissance égale au taux de faux positifs » fausse pour les marginales par coordonnée. La critique vise la lettre du programme, version 2.

### Phrases à ne plus écrire

Elles s'ajoutent aux listes des réponses 9 et 22 et de la note de stéganographie [PROPOSITION].

1. « La bascule en n ≈ m », pour un plan à jumelles : elle n'y est pas observable.
2. « Nous mesurons le régime n/√m », sans dire quelle référence est extrapolée.
3. « À 1 % de faux positifs », sans le nombre d'épisodes honnêtes du seuil.
4. « Le rappel croît avec l'horizon », comme résultat.
5. « Angle mort identifié », pour la transposition du jeton à l'action.
6. « La sonde détecte ce que la boîte noire manque », sans l'union à taux total égal ni le chiffre contraire de Parrack et collaborateurs.
7. « Le gain de l'accès interne n'a pas été mesuré sur les cas manqués », sans « 13 pages lues sur 39 ».
8. « Antécédent défectueux ». Écrire : « proposition exacte quand le multi-ensemble est préservé ; à longueur finie, leur tableau 2 montre l'écart ».
9. « Marge asymétrique, resserrée » : elle est retirée depuis N-077.

### Dépendances vers les autres demandes

- **Papier B** : la question « position ou dépendance » en devient l'ouverture, et la somme globale une base obligatoire de la statistique conjointe.
- **Papier C** : Parrack et collaborateurs est un voisin du quorum par type d'accès, et H8 reste à attribuer à l'un des deux papiers.
- **Programme** : la table est à refaire après N-075 à N-077, et l'unité de m est à fixer pour toutes les accumulations.

## Question neutre pour le collisionneur

« Un dispositif note chaque action d'un agent logiciel autonome au fil d'une longue tâche. Certains détecteurs lisent le texte produit, d'autres l'état interne de l'agent. Le dispositif cumule les scores et alerte au-delà d'un seuil réglé sur des exécutions sans faute. On vous remet une liste d'énoncés sur ce dispositif, dans un ordre tiré au hasard ; rien n'indique leur origine ni leur sort. Pour chacun : (1) est-il exact tel qu'écrit ? Donnez une preuve ou un contre-exemple. (2) Suit-il sans mesure d'un résultat que vous connaissez, dans quelque domaine que ce soit ? Citez-le et dites ce qu'il énonce. (3) De quelles quantités non dites dépend-il (tailles d'échantillon, unités, hypothèses sur les données) ? (4) Classez-le : établi ailleurs, conséquence immédiate, ouvert, ou faux. (5) Quelle expérience unique le trancherait, et avec quelle taille d'échantillon ? Dites votre certitude et ce que vous citez de mémoire. »

La liste jointe reprend en mots courants les énoncés en vigueur, les énoncés neufs de la table et six à huit témoins au statut connu [PROPOSITION].

## Décisions qui reviennent au directeur

**Décision 1 — Remplacer ou non l'énoncé de l'accumulation toujours valide par l'énoncé « écart au nul ».**
- *Enjeu.* L'énoncé en vigueur est vrai par construction sous la loi citée ; un relecteur le dira.
- *Option a : le remplacer maintenant.* Avantage : une revendication réfutable. Inconvénient : le préenregistrement de G1 est à récrire sur ce point.
- *Option b : le garder et ajouter le nul en base.* Avantage : continuité. Inconvénient : deux énoncés dont l'un ne peut pas échouer.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 2 — Fixer le plan de référence et l'unité de m avant de sceller.**
- *Enjeu.* Le régime cité comme nul n'est pas observable avec des jumelles ; la prévision porterait sur un terme absent.
- *Option a : mesurer référence par tâche et référence par régime sur les mêmes exécutions.* Avantage : la comparaison est le résultat propre. Inconvénient : analyse plus lourde.
- *Option b : référence par tâche seule.* Avantage : simple, sans terme τ. Inconvénient : indisponible pour une tâche nouvelle en service.
- *Option c : référence par régime seule.* Avantage : déployable. Inconvénient : τ peut tout dominer.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 3 — Exiger pour G1 le nombre d'épisodes honnêtes de chaque seuil et l'intervalle de son taux réel.**
- *Enjeu.* Sans cela, « à taux égal » peut cacher un facteur dix entre moniteurs.
- *Option a : l'exiger, et porter la référence à un millier d'épisodes si le coût le permet.* Avantage : comparaison défendable. Inconvénient : calcul honnête en plus.
- *Option b : garder 1 % nominal et rapporter l'intervalle.* Avantage : aucun coût. Inconvénient : G1 peut rester indécise.
- *Option c : passer à un taux plus haut, 5 % par exemple.* Avantage : seuil mieux estimé. Inconvénient : change une porte fixée.
- *Recommandation.* Option a, repli sur b. Confiance : 0,6, car mon ordre de grandeur est à refaire.

**Décision 4 — Sceller l'ordre des prévisions : terme entre tâches d'abord, exposant sans prévision tant que la puissance manque.**
- *Enjeu.* Environ 150 tâches par extrémité sont nécessaires pour l'exposant ; le terme entre tâches se décide bien plus tôt.
- *Option a : calcul de puissance et banc à vérité plantée d'abord, puis scellement.* Avantage : aucune prévision indécidable. Inconvénient : quelques jours.
- *Option b : tout sceller maintenant.* Avantage : aucun délai. Inconvénient : issue indéterminée probable sur l'exposant.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 5 — Approuver la demande reformulée et la question neutre, avec témoins, et fermer le repli du lemme.**
- *Enjeu.* Sans témoins, un accord du collisionneur ne se distingue pas d'un biais. Par ailleurs N-004 laisse un repli activable sans décision.
- *Option a : envoi avec témoins écrits par un agent neuf, et repli fermé par une ligne au registre.* Avantage : taux de détection mesuré, plus de retour silencieux du lemme. Inconvénient : une préparation de plus.
- *Option b : envoi sans témoins.* Avantage : immédiat. Inconvénient : convergence ininterprétable.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE
