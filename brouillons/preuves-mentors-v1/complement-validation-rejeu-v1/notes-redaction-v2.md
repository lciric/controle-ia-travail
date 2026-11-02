# Notes de rédaction — complément de validation du rejeu à graine — v2 (brouillon 2)

- Auteur : sous-agent de rédaction (Opus 5.5). Rédigé le 2026-11-02 entre 19:09 et 19:16 UTC (`date -u`), sur les
  décisions transmises par la session (repli à 272, durées 4 h et 72 h, `GO-2026-11-02-30` à 40 USD, script complet).
- Fichiers neufs : `R1-addendum-relance-v2-complement-validation-v1-brouillon2.md`, `R1-graine-config-complement-v2.json`,
  ces notes. Le brouillon 1, la configuration v1 du complément et les notes v1 sont intacts. Aucun `.sha256`, aucun
  commit, aucun réseau, rien sous `donnees/`, rien de l'analyse de R1-R2.

## Vérifié dans le code (commit `c2a8b6e1`), en plus des notes v1

1. **Frontière du repli = 272 au plus.** Cœur : niveau 1 = `quasi_egalites(pas, seuil_ecart, quasi_egalites_max)`
   (l. 730), donc au plus 16 ; chaque combinaison du niveau 1 ajoute au plus 16 quasi-égalités de son rejeu, après sa
   bascule (l. 767-770) ; `bascules_max` = 2 niveaux (l. 736). Deux paires ne peuvent pas être identiques (le premier
   élément fixe la combinaison du niveau 1, les seconds sont des positions distinctes). Total au plus 16 + 256 = 272 ;
   avec `cmax` = 272, `essayees >= cmax` (l. 739, 771) ne coupe jamais une combinaison de la frontière. Lot : même
   structure (l. 708, 714, 717, 747-752), mêmes clés : 272 l'épuise aussi.
2. **Gardes sur les combinaisons** : `combinaisons_max_validation` = `combinaisons_max` exigé (l. 1108-1110) ;
   `combinaisons_max_lot` : entier ≥ 0 seulement (module du lot, l. 839-841), aucune égalité exigée ; mis à 272 par
   cohérence. Entiers ≥ 0 pour les deux autres (l. 1075-1079). La validation lit `combinaisons_max_validation`, la
   résolution `combinaisons_max` (l. 1540).
3. **Durées** : 0 < 14 400 ≤ 259 200 passe `exiger_reglages_execution` (l. 1103-1105), le lot (l. 845-846) et le script
   (l. 165-171). Somme du script : 40 + 2 × (4 320 + 10) + 5 + (4 320 + 10) + 15 + 5 = **13 055 min** = `PLAFOND_MIN`.
4. **Garde R3** : nouvelle empreinte canonique `70b0b771…` ≠ `f91716bf…` : passe pour le cœur (l. 1192-1211) et le lot
   (l. 968-978), code inchangé.
5. **Citations du texte**, simulées sur le brouillon 2 avec les commandes du script et les expressions des modules :
   « Tests attendus » une fois → `71` ; « Chemin de la configuration … » une fois →
   `prereg/R1-graine-config-complement-v2.json` ; les deux libellés de l'empreinte canonique une fois chacun, égaux à
   `70b0b771…` ; commit `c2a8b6e1…` (40 caractères) trouvé ; entropie trouvée. Le texte ne cite que `GO-2026-11-02-30`.
6. **Comptes du 2 novembre** : 90 non tentés et 3 coupés (93 manqués), d'après le verdict scellé ; le brouillon 1 ne
   contenait aucun « 87 non tentés » (vérifié par recherche) ; le brouillon 2 dit que tout autre compte est faux.

## Configuration v2 : différences clé par clé avec `R1-graine-config-v1.json`

- `combinaisons_max` : 136 → 272
- `combinaisons_max_validation` : 136 → 272 (égalité exigée par le code)
- `combinaisons_max_lot` : 136 → 272 (non exigé ; cohérence)
- `duree_max_episode_s` : 600 → 14 400
- `duree_max_s` : 2 400 → 259 200
- `duree_max_episode_lot_s` : 900 → 14 400
- `duree_max_lot_s` : 3 600 → 259 200
- 35 autres clés identiques ; 42 clés ; même format que la v1. Empreinte canonique
  `70b0b77135594b8566833c57535086e26379787b2735b8a3372ece2a3922ff5e`.

## Devis (au prix plafond de 1,40 USD/h, plus le disque)

- Bas ≈ 3 h ≈ 4 USD ; **central ≈ 10 h ≈ 14 USD** ; haut ≈ 24 h ≈ 34 USD ; pire : borné par la garde de dépense, arrêt
  à 40 USD (≈ 28 h). La ligne du GO annonce ≈ 6 à 20 USD : le central y est ; le haut la dépasse, sous le plafond.
- L'incertitude vient presque toute des épisodes « difficiles » (bascules simples épuisées) : 3 connus (rangs 0, 20,
  56 : au moins 1 564 s rejouées à l'identique, au plus ≈ 4,7 h à frontière épuisée) et ≈ 4,6 attendus parmi les 90 − 3
  non tentés (intervalle large, de 1 à ≈ 11, sur 3 cas observés sur 57).

## À confirmer par la session qui lance (session-depot)

1. **Classe attendue** : même à 272, « graines validées » n'a que ≈ 0,1 de chance ; ≈ 3 manquées attendues (0 à 8), de
   cause « frontière épuisée ». Ce qui limite n'est plus une borne de travail mais la frontière gelée par la v2
   (`bascules_max` = 2, 16 quasi-égalités par niveau, bascule vers le second candidat seulement) et la règle gelée (une
   manquée suffit). Le brouillon lit alors une **mesure complète** et une réserve HG-2 **chiffrée**, sans nœud. Une
   frontière à trois bascules (jusqu'à 16 + 256 + 4 096 = 4 368 combinaisons, ≈ 30 h par épisode difficile au taux
   observé) ou une validation par le lot fidèle seraient un texte neuf : à proposer à Lazar, non à décider ici.
2. **Garde de dépense** : tenue par la session seule. Si la session s'interrompt, le plafond de l'amorce
   (13 055 min ≈ 217,6 h) laisserait l'instance tourner jusqu'à ≈ 305 USD au prix plafond. Poser à la création une
   vérification planifiée des dépenses (par exemple horaire) qui applique l'alerte à 30 USD et l'arrêt à 40 USD (TERM
   par PID, puis arrêt de l'instance par son identifiant), et confirmer le moyen d'atteindre le PID sur l'instance.
3. Commande de création du 2 novembre (offre, image, disque, forme de l'amorce) à reprendre mot pour mot ; vérifier que
   `BRANCHE`, `PREREG`, `TABLE_V3`, `PLAFOND_MIN` passés par `--env` atteignent le script (l'amorce les hérite par
   `env`).
4. Sur le `main` réel (mon `origin/main` local date de 09:01 UTC) : arbre gelé égal à `c2a8b6e1` ; table du sous-produit
   absente ; aucun manifeste illisible dans `runs/`.
5. Dépenses déjà imputées à `GO-2026-11-02-30` ; ligne neuve du registre qui corrige « 87 » de la ligne 72 (non modifiée).
6. Essai local `ARRET_AVANT_CALCUL=1` : il pousse la branche (l. 190) ; seulement contre un dépôt nu local ou sous une
   autre branche.
7. Le brouillon 2 fait ≈ 32 Ko (« sous un texte court », 18:53 UTC) : il garde toutes les sections exigées par R1 et
   les six lignes que lisent le script et les modules ; une coupe plus forte passerait par un renvoi plus large à la v2.

## Dix lignes pour le contre-lecteur

1. Vérifier que la frontière du repli compte au plus 16 + 16 × 16 = 272 combinaisons (l. 730, 736-773 du cœur ; l. 708-752
   du lot) et qu'à `combinaisons_max` = 272 la borne ne peut plus couper une combinaison de la frontière.
2. Vérifier la différence de configuration (sept clés), l'égalité `combinaisons_max_validation` = `combinaisons_max`
   (l. 1108-1110), l'absence de garde d'égalité pour le lot (l. 839-841), et recalculer l'empreinte canonique `70b0b771…`.
3. Vérifier que `lire_validation` (l. 854-886) et `declarer` sont inchangés et que la règle de « Seuil » les recopie.
4. Vérifier la somme des délais (13 055 min) contre le script (l. 172-187) et l'appel de l'amorce (`PLAFOND_MIN`).
5. Vérifier que les gardes R3 du cœur (l. 1192-1225) et du lot (l. 968-978) passent avec une autre empreinte de
   configuration et rien d'autre, code inchangé.
6. Juger les prédictions P-C1 et P-C2 (R = 147 à ≈ 0,1 ; « graines validées » à ≈ 0,1) au regard des 57 épisodes du
   2 novembre : chiffrées, signées, honnêtes ?
7. Juger la ligne « méthode non transposée, cause méthode » (mesure complète, réserve HG-2 chiffrée, aucun nœud) : est-elle
   gelée sans échappatoire et conforme à la règle de la v2 ?
8. Juger la lecture « répétabilité seulement » de la résolution rejouée et de la table du sous-produit : que lit-on si
   elles diffèrent, et la table `ead8a668…` reste-t-elle bien la seule référence ?
9. Juger la garde de dépense (alerte à 30 USD ; procédure lancée à 39,5 USD ; TERM par PID, puis arrêt de l'instance par
   son identifiant) contre « aucun budget de temps qui coupe », contre le plafond de 40 USD, et le risque d'une session
   interrompue.
10. Vérifier le devis (bas ≈ 4, central ≈ 14, haut ≈ 34 USD ; pire : arrêt à 40 USD) contre les mesures citées (33 min de
    mise en place, 798 s pour les 54, 1 564 s pour les 3 coupés, 8,3 à 33 s par combinaison, 13 min 24 s pour la
    résolution) et les corrections de libellé contre les lignes de code citées.
