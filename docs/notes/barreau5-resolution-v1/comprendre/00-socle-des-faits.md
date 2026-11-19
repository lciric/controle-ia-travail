# Barreau 5 — socle consolidé des faits (critique de complétude)

- Rédigé le 2026-11-19 vers 12:30Z par le critique de complétude (Claude Opus 5.5), lecture seule du dépôt `/home/user/controle-ia-travail` (tête `a9d6acb4…` à 12:07Z). Rien créé ni commis dans le dépôt. Aucune dépense, aucun refus d'outil.
- Sources : les six notes `01-texte-scelle.md` à `06-chantiers-voisins.md` de ce dossier, plus mes propres lectures (marquées « relu » ou « ajout du critique »).
- Aucun chiffre de résultat du programme hors de l'apprentissage des sondes sur la tâche (étape B bis). Les chiffres publiés d'un article sont cités avec leur page.
- Abréviations des chemins : PV = `prereg/validite-adaptateur-v1.md` (texte scellé de validité de l'adaptateur) ; PB = `prereg/T0.7-etape-B-bis-v1.md` ; VB = `docs/verdicts/verdict-T0.7-etape-B-bis-v1.md` ; LB = `diag/20261119-000444-bbis-t07-lecture-v1/lecture-bbis.json` ; T06 = `prereg/T0.6-organismes-v0-v1.md`.

## 0. Ce que la critique a tranché ou corrigé

1. **Pas de contradiction de fond entre les six lecteurs.** Trois écarts apparents s'expliquent :
   - Aire minimale détectable du contraste « actions gonflées contre non gonflées » à adaptateur constant : 0,66 à 0,72 (note 01) contre 0,65 à 0,70 ou 0,70 à 0,76 (note 02). Les deux sont justes dans leur cadre. La note 01 calcule pour les sondes génériques du texte scellé : comptes réunis, une sonde, niveaux de Bonferroni de l'étude des sondes génériques. La note 02 calcule pour les sondes de l'étape B bis : deux plis moyennés, 95 % ; la formule du texte donne 0,65 à 0,70, les largeurs réalisées 0,70 à 0,76.
   - Coût de la relecture à texte constant : « < 1 USD » dans l'accord GO-2026-11-10-07 (relecture prévue sur l'instance de l'étape A) ; « 2,5 à 4,6 USD » dans PV, sur une instance à part, après la lecture large R-2207. Le chiffre du texte scellé fait foi (`registres/go.md` l. 297 ; PV l. 218-224) [relu].
   - « Une journée de carte » (note 03) désigne une session de 7 à 8 heures, pas 24 heures (note 03 l. 250).
2. **Inconnue levée (note 04)** : `sondes-bbis.npz` porte, par cellule et par pli, les poids des sondes apprises (`sonde_w` de forme (4096,), `sonde_b`, `sonde_q` pour la famille attention), deux directions (`direction0_*`, `direction1_*`) et le lecteur honnête (`enc_*`). Les scores de l'étape B bis sont **par action** : 320 par groupe et par pli (relevé des en-têtes `outils/formes-sondes-bbis.txt`, `outils/formes-scores-bbis-000.txt`) [vérifié].
3. **Fait monté de « déduit » à « vérifié »** : l'étiquette d'apprentissage de l'étape B bis est confondue avec la présence de l'adaptateur. Le code apprend `pos, neg = ("O", positifs_cond), ("O", H)` (`src/controle_ia/t07bbis/validation_imbriquee_v1.py` l. 357). Les groupes relus (jumeau, textes honnêtes sous adaptateur, témoin) ne sont que notés (l. 142-162). L'honnête est le modèle nu (T06 l. 495). [relu]
4. **Affirmation trop forte (note 05)** : « aucune source du dépôt » ne parlerait d'effacement de concept. En réalité, LEACE (Belrose et al. 2023) est nommé trois fois dans `docs/notes/regard-ou-raisons-confondants-v1/`, toujours « référence à vérifier » (`bilan-mere-v1.md` l. 80 ; `croisement-v1/synthese-croisement-v1.md` l. 75 ; `collisionneur-v1/consultations-a-part-v1/argon/texte.md` l. 62). Une recherche arXiv « amnesic probing », « concept erasure » et LEACE est aussi consignée dans `brouillons/pain-axis-programme-fusionne-v1/revue-croisee-NK1-NK19-v1.md` l. 125. Le constat de la note 05 tient pour les seuls dossiers qu'elle a parcourus.
5. **Source manquée par la note 05, vérifiée sur PDF par moi** : « Caught in the Act », arXiv 2610.12445v1, PDF versé `docs/sources/pdf/2610.12445v1.pdf` (sha256 `7e141758…`, égal au compagnon). Elle porte un contraste publié **à adaptateur constant** (§ 5).
6. **Inventaire complété (note 04)** : la course exploratoire de la même recette a, elle aussi, gardé un sous-ensemble d'activations en treize morceaux, deux adaptateurs, les mesures et les textes. Ils sont sur `origin/essai/t06-explo-v3`, dossier `donnees/20261109-070232-t06-reel/` (noms seulement) [vérifié]. Aucune activation complète des courses 7b, de l'étape A ou de l'étape B bis n'existe sous un nom de fichier sur les branches regardées : `calcul/t07bbis-repetition-v1`, `-v2`, `-v4`, `donnees/t07-etape-b-bis-v1`, `coffre/audit-fuites-t07-v1`, `journaux/etape-a-t07-b-v1` et `-v2`. Il n'y a que des fichiers d'essai factices et un `rejeu-activations.json`. Les 600 autres branches n'ont pas été parcourues.
7. **Pas de contradiction sur « Fable »** : les notes 01 et 02 sont signées Fable 5.2, la note 05 Opus 5.5. R-3791 (`registres/decisions.md` l. 3929, 12:07:50Z) consigne la limite d'usage de Fable atteinte vers 12:05Z, avec remise à zéro le 22 novembre à 18:00Z. Les trois agents arrêtés ont été relancés sur Opus. [relu]
8. **Drapeaux de cloisonnement** : la note 02 a lu, en différentiel seulement, `docs/verdicts/verdict-T0.7-etape-B-bis-v1-erratum-1-v2.md`. Ce fichier est absent de la liste permise du mandat ; la note dit qu'aucune valeur n'y change. Les notes 01 et 02 ont ouvert la note « pour Lazar seul » (`lecture-verdict-bbis-reservee-lazar-v1.md`), comme le mandat le demandait. La session mère ne doit pas la lire. La note 04 a laissé environ 100 Mo d'extraits sous `extraits/` de ce dossier : l'effacement a été refusé par une garde de sécurité, il reste à faire par une personne ou par la mère.

## 1. Le texte scellé de validité de l'adaptateur : ce qu'il prévoit, son état

- **État.** Scellé le 2026-11-14T09:45:18Z (empreinte `7e78909d…`) [vérifié, note 01]. Son registre propre `registres/validite-adaptateur-v1.md` porte une seule ligne. Il n'a ni code, ni fiche de code, ni course, ni dépense, ni lecture.
- **Portée.** Il ne vise que les sondes principales de l'étude des sondes génériques : « pour une sonde principale p de T0.7 », PV l. 34. Il est hors du critère 3 de G0 (PV l. 25) et ne nomme pas l'étape B bis. Il exclut par déclaration la « sonde d'existence purgée de l'adaptateur », c'est-à-dire une sonde apprise contre un témoin d'adaptateur (PV l. 30). [vérifié]
- **Trois pièces.**
  - **Lecture au processeur, 0 USD.** Contraste dans la dose, tendance avec l'excès déclaré, saboteur contre témoin à dose 1, deux différences contre l'honnête.
  - **Relecture à texte constant sur carte, 2,5 à 4,6 USD.** Adaptateur seul sur textes honnêtes ; textes du saboteur relus sous le modèle nu ; divergences de Kullback-Leibler.
  - **Course du témoin distillé honnête, 8,5 à 12,5 USD, environ 7,5 heures.** Même recette, épisodes honnêtes, quatre doses, plus l'adaptateur honnête remis à l'intensité du saboteur, à texte constant seulement.
  - Les trois pièces sont détaillées dans la note 01 (a), (c) et (d) [vérifié].
- **Accord de calcul GO-2026-11-10-07.** 30 USD pour les deux pièces, échéance 2026-11-27. Il est valide, non consommé et non prolongé (`registres/go.md` l. 297). [relu] L'échéance tombe 4 jours avant l'entretien. La conception par Fable ne peut reprendre qu'à partir du 22 novembre à 18:00Z (R-3791), ce qui laisse environ 4,5 jours. [déduit]
- **Trois pièges d'ordre** [relu, PV l. 115-126] :
  - La lecture est unique : « lecture déjà écrite : refus ». Sans la relecture sur carte, les lignes payantes deviennent « non calculables ». Lire d'abord le gratuit ferme donc le payant. [déduit]
  - L'aiguillage G-2 : si la lecture de l'étape B porte `scores_ouverts` faux ou `scores_ii_ouverts` faux, « rien n'est lu », et il faut une version neuve du texte. [inconnu, valeur interdite ici]
  - Toute pièce lancée « sur la foi d'une sortie » est invalide, alors que la règle de lancement disait « jouée » dès l'issue « vu » du 14 novembre. Le texte ne tranche pas le lancement tardif.
- **Deux faits de conception.**
  - Telles que scellées, les deux courses ne gardent aucune activation (PV l. 113, 116, 241).
  - Le contraste « textes du saboteur relus sous le modèle nu contre l'honnête » est un **soutien** dans PV (l. 57). Dans PB (l. 60), le même contraste est une **réserve** : « elle lit aussi le texte ». [vérifié]

## 2. L'étape B bis : ce qu'elle a établi, ce qu'elle n'a pas établi

**Établi** (scellé, accepté par Lazar, GO-2026-11-19-44, `registres/go.md` l. 477) :
- La sonde apprise sépare l'organisme de l'honnête aux quatre doses, mieux que les trois lecteurs du texte, et à texte égal : 0,9436 ; 0,9532 ; 0,9967 ; 0,9885.
- L'adaptateur saboteur seul, posé sur des textes honnêtes, la déplace autant : 0,9252 ; 0,9822 ; 0,9942 ; 0,9986.
- La différence « texte égal moins adaptateur seul » n'est établie positive à aucune dose. Le sens contraire est établi à la dose 1 : −0,0102 [−0,0209 ; −0,0019]. Le libellé « lecture dure » est refusé. (VB l. 15, 27, 97)
- L'adaptateur témoin allume aussi la sonde : épisodes 0,7452 à 0,9209 ; textes honnêtes sous le témoin 0,7271 ; 0,8764 ; 0,8484 ; 0,8562.
- À adaptateur constant, le contraste « actions gonflées contre non gonflées » n'est au-dessus du plancher à aucune dose : 0,4704 ; 0,5913 ; 0,5403 ; 0,6231. Sources : LB et `docs/notes/entretien-g0-priorites-v1/lignes-descriptives-bbis-pour-dossier-v1.md` l. 24-31, 66-73.
- Formule du dossier : « confusion mesurée, non levée » (`lecture-verdict-bbis-reservee-lazar-v1.md` l. 40).

**Pas établi**, avec la raison de chaque limite :
- **Pas d'absence** : le contraste à adaptateur constant ne détecte qu'une aire de 0,65 à 0,76 (§ 0.1). [déduit, note 02 § 4]
- **Plafond géométrique** : aux doses 0,5 à 1, l'adaptateur seul vaut déjà 0,98 à 0,999. La place restante (0,0178 ; 0,0058 ; 0,0014) est plus petite que la différence détectable (0,054 ; 0,007 ; 0,013). L'état « au-delà de l'adaptateur seul » n'était atteignable qu'à la dose 0,25. Cette dose est aussi la plus instable : 0,9357 devient 0,7929 sous l'autre ordre de calcul. [déduit, note 02 § 4.4]
- **Comparaisons absentes** : rien ne sépare l'organisme d'un adaptateur honnête. Il n'y a aucune intensité mesurée et aucun contraste « organisme contre témoin » (VB l. 156).
- **Constats non exploités**, valeurs relues par la note 02 dans LB :
  - La sonde apprise **sans aucun adaptateur** (sur l'organisme à consigne cachée) est déplacée elle aussi par l'adaptateur seul : 0,6233 ; 0,7792 ; 0,8712 ; 0,9074.
  - La sonde de la dose 1 sépare le saboteur instruit de l'honnête, tous deux sous le modèle nu (0,9675) ; la présence d'une consigne n'est pas écartée.
  - À la dose 0,25, sans les jetons du champ du coût, la séparation tombe à 0,6829.
  - Les deux bornes basses positives du bras de transfert ne sont pas citables, parce que les cellules s'arrêtent avant (note du dossier v2, l. 143).
- **Audit de symétrie** : « transmissible avec réserve ». L'égalité entre l'ancien et le nouveau chemin de calcul n'est comparée que sur 8 épisodes sur 64, au modèle nu et à la dose 1. (`docs/notes/audit-symetrie-bbis-v1/audit-symetrie-bbis-v1-resume-sans-resultat.md` l. 11, 26)

## 3. L'organisme et son unité expérimentale

- **Modèle et adaptateur** [vérifié, note 03].
  - Llama-3.1-8B-Instruct, révision `0e9e39f2…`.
  - Un seul adaptateur de rang faible, codé dans le dépôt : rang 16, alpha 32, sur q, k, v et o des 32 couches, 13 631 488 paramètres.
  - Distillé en 480 pas sur 160 épisodes neufs du saboteur instruit (32 tâches de réserve), rejoués sans consigne, sans aucun tri sur le coût.
  - Les textes de distillation ne sont pas gardés : `diag/20261111-151701-t06-reel/distillation-t06.json` ne porte que des comptes.
- **La dose** est l'échelle du terme ajouté, appliquée à l'inférence, sur le même adaptateur. À dose 0, le terme n'est pas calculé : c'est le modèle nu au bit près. L'écart est linéaire pour une couche, non linéaire pour le modèle entier. (`src/controle_ia/organismes/lora.py` l. 1-11) [relu]
- **Le témoin** (`T100`) est distillé d'une consigne bénigne (titres en minuscules), à la dose 1 seulement. Ce n'est pas un honnête distillé (T06 l. 375-377 ; PV l. 23). [vérifié]
- **Le sabotage** n'a qu'un mode : le champ du coût. Une action est « gonflée » si son coût vaut au moins 2 fois la médiane honnête de la tâche, sans oracle du coût réel. Sous un même adaptateur, il varie d'une action à l'autre ; à la dose 1, sur 640 actions : 367 gonflées, 85 non gonflées. [vérifié]
- **Unité expérimentale** : un adaptateur par condition, un épisode par tâche et par condition. Les intervalles rééchantillonnent les tâches, adaptateurs fixés. Toute comparaison « saboteur contre témoin » est un contre un : elle confond le sabotage avec la graine, les données et l'intensité. [déduit, note 03]
- **Réplique** : une seconde paire d'adaptateurs de la même recette, à graines différentes, existe sur la course exploratoire (`origin/essai/t06-explo-v3`). La liste d'arrêt du texte scellé interdit d'y appliquer une sonde sous ce texte (PV, liste d'arrêt, point 12). [vérifié]

## 4. Données brutes : ce qui existe, ce qui se recalcule, ce qui est perdu

**Existe**, sur les branches, empreintes recalculées par les notes 03 et 04 :
- **Course de confirmation**, `origin/calcul/t06-confirmation-7b-v1` :
  - les deux adaptateurs (27,3 Mo chacun) ;
  - `mesures-t06.npz`, 19 colonnes de 5 760 actions, dont `cle`, `condition`, `tache`, `pas`, `dose`, `cout` ;
  - `textes-actions-t06.jsonl`, avec les identifiants de jetons ;
  - un sous-ensemble d'activations : 576 actions sur 5 760, couche 15 seule, par jeton, (jetons, 4096) en float16, 1,06 Go.
- **Étude des sondes génériques**, `origin/donnees/t07-etape-a-v1` : un score par action (`scores_<k>` de forme (5 760,), `plancher_<k>` de forme (800, 5 760)), poids et directions des sondes.
- **Étape B bis**, `origin/donnees/t07-etape-b-bis-v2` :
  - un score par action, 320 par groupe et par pli, pour la sonde, sa jumelle du second ordre de calcul, 800 directions et 100 sondes du nul ;
  - groupes notés : origine de l'organisme, origine de l'honnête, jumeau, textes honnêtes sous l'adaptateur saboteur, épisodes du témoin, textes honnêtes sous le témoin ;
  - poids des dix sondes (§ 0.2).
- **Course exploratoire**, `origin/essai/t06-explo-v3` : même jeu de fichiers (§ 0.6).

**Se recalcule au processeur, sans carte** : aucune de ces lectures n'a été faite. Chacune serait une lecture neuve de résultats, donc un texte scellé et le mot de Lazar (CLAUDE.md, « Récupérer ce qui est récupérable »). [déduit, note 02 § 7.3]
- l'organisme contre l'adaptateur témoin, sous la sonde apprise ;
- les textes honnêtes sous l'adaptateur saboteur contre les mêmes sous le témoin, en différence appariée par action ;
- la tendance du score avec l'excès déclaré, en joignant `cout` par `cle` ;
- le contraste du dommage chez l'honnête ;
- ces lignes sous la sonde du second ordre de calcul ;
- la géométrie entre les poids des sondes (4096) et les matrices B de `o_proj` des adaptateurs (4096 × 16), qui écrivent dans le même flux résiduel. Ce dernier point est une possibilité [déduit des formes, aucune valeur lue].

**Demande une carte** : toute lecture par jeton ou à une autre couche, toute version « sans le champ du coût » de l'adaptateur seul, toute mesure d'intensité, tout adaptateur honnête. La relecture de l'étape B bis coûte environ 0,5 heure de carte (PB l. 213).

**Perdu** :
- les activations complètes des trois courses (machines détruites ; `registres/arrets.md` l. 92, 138) ;
- les textes de distillation.

**Inconnu** : on ne sait pas si un rejeu à graines égales reproduirait ces textes.

## 5. Méthodes de l'état de l'art, par statut de vérification

**Vérifié sur PDF versé, page citée** :
- **Contraste publié à adaptateur constant.** 2610.12445v1 (« Caught in the Act »), relu par moi.
  - Huit organismes, tous des adaptateurs de rang faible (rang 128) sur Qwen3.6-27B, dont sept publiés par l'institut britannique de sécurité de l'IA (p. 7, 23).
  - Les sondes sont « trained through each organism's adapter » et lisent les mensonges sur le but propre de l'organisme contre ses dénégations honnêtes sur d'autres buts, **dans le même organisme** (p. 26, table 10).
  - L'organisme bird-labs est distillé par divergence de Kullback-Leibler contre un professeur à consigne (p. 25). Sa même dénégation est un mensonge sous une ligne de consigne et vraie sous une autre. La même sonde donne 0,997 dans le premier cas, 0,745 dans le second (p. 9, 26, figure 9 p. 29).
  - Leur figure 1b (p. 1, 98,0 %) oppose deux organismes **différents** : elle porte elle-même la confusion d'adaptateur.
  - Les poids des sept organismes de l'institut sont publiés (référence Cooney et al. 2026, 2606.12618, p. 12). Ce dernier article n'est connu que par citation.
- **Taylor et collègues, 2512.07810.** Des comportements mis par réglage fin dans des modèles bénins allument les sondes (p. 17). Le contraste à poids constants (mot de passe donné ou non) ne sépare pas l'organisme Oak (p. 17). Le recentrage sur un modèle de référence échoue (p. 22). Les organismes sont des 70 milliards, renvoyés en phase 1 (P-002). [note 05]
- **2609.36490.** Un adaptateur de rang 1 sur Llama-3.1-8B laisse une signature générique, que l'entraînement efface ; les sondes des autres concepts servent de témoin (p. 6-7). [note 05]
- **Kumar, 2605.27958 ; 2611.10620.** La sonde lit le régime de consigne plutôt que la décision. [note 05]
- **2606.22864.** Une aire élevée peut venir de la construction du jeu ; il faut une base de métadonnées. [note 05]
- **2610.22460 (p. 8, par N-034).** Une direction placebo de même norme ne fait pas moins bien. [note 05]

**Vérifié par un auditeur, PDF non versé** : 2607.25907, « lisible n'est pas contrôlable » ; Devbunova, 2603.19426, décorrélation à l'entraînement d'une sonde. [note 05]

**Listé, à vérifier** : LEACE (Belrose et al. 2023), § 0.4 ; Cooney et al. 2606.12618.

**Non trouvé dans les sources** : comparaison de modèles par différences d'activations ou par crosscoders ; plusieurs graines de réglage fin ; témoin bénin apparié de même chaîne sur un 8B. La recherche dédiée n'a jamais été faite (lot 9 non rendu, niveau 3 v6 l. 702-704). Zone peu cherchée, à traiter selon R8.

## 6. Chantiers voisins et nœuds de Lazar

**Chantiers voisins** [vérifié, note 06, lignes relues par moi] :
- **Contraste à témoin apparié pour G1.** Accepté en principe : GO-2026-11-18-48, « bien sur !!! », énoncé à soumettre (`registres/go.md` l. 412).
  - Le brouillon N-074 (`docs/decisions/decision-N-074-v1-brouillon2.md`) définit le témoin : même recette, transcriptions honnêtes, remis à l'intensité du saboteur. Il n'est pas retenu et N-074 est absent de CLAUDE.md.
  - L'étude de simulation rend « non tranché ».
  - Le choix entre le contraste (A) et la garde avec contraste rapporté (C) reste à Lazar, sans défaut.
- **Brouillon 6 du préenregistrement de G1** (le dernier présent) : il juge la porte sur l'organisme à adaptateur contre le modèle nu, sans témoin d'adaptateur.
- **Second cycle de l'accumulation** (brouillon 6, non scellé) : il porte la recette la plus complète (témoin de même intensité, second témoin honnête). Il est gelé (GO-2026-11-19-27, `registres/go.md` l. 460).
- **Lecture par lentille** : descriptive ; elle ne lit aucune direction propre à l'adaptateur.
- **Texte du barreau 8** : pas de contraste à organisme constant.
- **N-062** : en cas d'échec, les sondes se reconçoivent ; ce qu'elles lisent à la place est rapporté.
- **Invariant de N-053** : aucun score de moniteur dans l'entraînement d'un adaptateur.

**Nœuds**, selon la hiérarchie de décision de CLAUDE.md :
- jouer ou non le texte scellé avant le 27 novembre ;
- texte neuf pour les sondes apprises sur la tâche (écart à un texte scellé, modification d'hypothèse) ;
- sort de l'accord de 30 USD ;
- toute dépense de carte : témoin honnête, répliques d'adaptateurs, relecture ;
- réemploi des scores fermés de l'étape B bis et de la course exploratoire ;
- sens du contraste « saboteur relu sous le modèle nu » ;
- énoncé du critère de G1 et réserve D9 ;
- dégel du second cycle ou place dans les trois chantiers ;
- conception avant le 22 novembre à 18:00Z sur un autre modèle que Fable (changement de modèle) ;
- revendication éventuelle de la séparation « comportement contre trace de l'adaptateur » (zone peu cherchée) ;
- message au statisticien externe (contact).

## 7. Inconnues qui restent, et comment les lever

1. **Aiguillage G-2.** La lecture de l'étape B a-t-elle fermé les scores de l'organisme ? Cela décide si le texte scellé peut se lire tel quel. Un agent autorisé lit `resultat.scores_ouverts` et `resultat.scores_ii_ouverts` dans `diag/20261114-001352-t07-lecture-reel/lecture-t07.json`, sur la branche `origin/verdict/t07-etape-b-compte-3-v1`. Aucune pièce permise ne les recopie : vérifié par recherche dans LB, PB, VB et les notes de l'entretien.
2. **Pièces citées par PV et absentes de main** : contre-lecture 2, brouillons 4 à 7, script d'énumération des grilles. Elles sont sur la branche du compte 4, interdite ici. Une session autorisée les verse et vérifie l'antériorité du script.
3. **Intensité des adaptateurs.** Ni la divergence ni la norme du terme ajouté ne sont mesurées, pour aucun adaptateur. Cela demande une carte, sauf pour la norme des poids, que les fichiers d'adaptateur permettent de calculer au processeur.
4. **Effectif des actions honnêtes « gonflées ».** Il n'est publié nulle part. Il se lit sur `mesures-t06.npz` (colonne `cout`, condition « honnete ») sous un texte de lecture.
5. **Variabilité entre deux apprentissages de la même recette.** Elle n'a jamais été mesurée. La paire de la course exploratoire la permettrait, sous un texte neuf, parce que PV l'interdit sous lui.
6. **Zone de l'état de l'art.** Comparaison de modèles, crosscoders, suites de Taylor (lot 9), effacement de concept. Il faut une lecture sur PDF (R7) avant toute phrase du dossier.
7. **Autres branches.** Activations ou code du texte scellé sur l'une des 600 branches non parcourues : non cherché.
8. **Rejeu des textes de distillation.** Un rejeu à graines égales redonnerait-il les mêmes textes ? Cela se lève par lecture de la chaîne de génération, sans carte.
9. **Calendrier.** Le temps de code et de contre-lecture n'est compté nulle part. La fenêtre réelle va du 22 novembre à 18:00Z au 27 novembre.
