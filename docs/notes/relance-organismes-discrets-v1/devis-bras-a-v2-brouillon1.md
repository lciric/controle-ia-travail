# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis de la course sur carte louée — v2, BROUILLON 1

- **Date (UTC)** : 2026-11-18T18:01:27Z (`date -u`), fin de rédaction vers 18:10Z. Commit du dépôt lu : `c8ccbf53527cdbdfa87c139aaf37acb47f620706`.
- **Objet** : chiffrer la course du bras A telle que le texte scellé et ses deux addenda la lisent. Ce devis remplace, pour le bras A, le devis v1, qui chiffrait une conception abandonnée (huit actions candidates par pas et une clé de sélection).
- **Statut** : brouillon, **non contre-lu**. Il n'engage rien et n'ouvre aucune dépense. Une ligne de calcul reste un nœud de Lazar.
- **Sceau** : ce brouillon n'a pas de fichier compagnon d'empreinte (consigne : un seul fichier écrit). À sceller par la session qui le reprend (R6).

## 0. Pièces qui font foi, avec empreintes (sha256, calculées à 18:01Z)

| pièce | empreinte |
|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v1.md` (texte scellé) | `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-lecture-lot-de-huit-v1.md` (premier addendum) | `bd6ae8dfdfcda18a9c7118ede4f1542fae71063521c442093f778a1cd4b0e4f3` |
| `docs/notes/relance-organismes-discrets-v1/addendum-pas-de-distillation-brouillon1.md` (second addendum, brouillon en contre-lecture) | `15d40eb397fd37ffa582148a79249332e941744eb57b13e82e64dd051dd5d307` |
| `docs/notes/organismes-discrets-v1/conception-organismes-discrets-v2.md` | `43a356ab7f8924faca17bb6024bbab8db778e3ce0b8a4b368ace1b78341f9b0c` |
| `prereg/T0.6-organismes-config-7b-v1.json` (configuration de référence) | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| `docs/notes/organismes-discrets-v1/devis-organismes-discrets-v1.md` (ancien devis, pour la méthode) | `c376f2ea2e6a60849dc67e1563b45608a63454bd3fd3ba38202048354ea6b64c` |
| `docs/notes/relance-organismes-discrets-v1/carte-branchement-bras-a-v1.md` | `0f26006d9eeaef7b1f7f84b96de50078350aa2e4cf177b6ed07cd21a12286190` |
| `prereg/T0.6-organismes-v0-v1.md` (texte scellé de l'organisme précédent, lu pour sa seule section « Devis », lignes 635 à 702) | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` |

Registres vivants cités par ligne, au commit ci-dessus, sans empreinte (ils ne sont pas scellés) : `registres/depenses.md`, `registres/decisions.md`.

Si le second addendum change à sa contre-lecture, ce devis est à relire : il dépend du nombre de 384 pas.

## 1. Deux points du texte scellé qui commandent le compte, et qui restent ouverts

**Point 1 — combien d'adaptateurs pour le témoin bénin (vi-B).** Le témoin (vi-B) est l'adaptateur distillé sur des transcriptions où le champ `PREDICTION` est permuté, « même proportion, même machinerie » (texte scellé, ligne 53 ; conception, ligne 56). Le texte ne dit pas si « même proportion » veut dire une seule proportion ou une par dose. Le second addendum écrit « un par dose non nulle, et les témoins (vi-T) et (vi-B) » (ligne 22), sans compter. La configuration de référence porte `doses_temoin` = [1.0] (ligne 81 à 83), mais cette clé n'est pas parmi celles que le texte scellé emprunte (ligne 17). **Je ne tranche pas.** Je chiffre deux lectures :

- **Lecture courte** : (vi-B) à une seule proportion. 4 doses + (vi-T) + (vi-B) = **6 adaptateurs** ; **7 conditions** au rejeu.
- **Lecture longue** : (vi-B) à chaque dose non nulle. 4 + 1 + 4 = **9 adaptateurs** ; **10 conditions** au rejeu.

**Point 2 — le sous-échantillon du juge d'une autre lignée (lecteur 6).** Il compte 2 560 actions, « stratifié par tâche et par condition » (texte scellé, ligne 147). 2 560 se divise bien par 16 tâches × 5 doses (32 par case) et par 16 × 10 conditions (16 par case), mais pas par 16 × 7. Le texte ne dit pas quelles conditions entrent dans la stratification. Sans effet sur la carte ; à fixer avant de tirer le sous-échantillon.

## 2. Débits et durées réels de la chaîne réemployée, sur la même carte

Des mesures existent au dépôt. Aucune ne vient du bras A. Toutes viennent de la chaîne de l'organisme précédent (T0.6), même modèle, même carte (A100 SXM4 80 Go), mêmes réglages (10 pas, lot de 8 épisodes, 400 jetons).

| grandeur | valeur | source |
|---|---|---|
| durée d'un épisode, en lots de 8 (course P3) | **40,2 s** (240 épisodes en 9 644,6 s) | `prereg/T0.6-organismes-v0-v1.md`, ligne 643 |
| durée d'un épisode à la course exploratoire de dose-réponse (7a) | **42,8 s** (576 épisodes en 6,85 h ; division faite ici) | même fichier, ligne 698 |
| jetons par action et par épisode | contexte 2 643, action 223 ; transcription finale 4 319 jetons par épisode | même fichier, ligne 645 |
| passe unique d'activations sur texte imposé | 0,45 s par épisode | même fichier, ligne 644 |
| distillation, génération de ses données comprise (7a) | 4,36 h pour 320 épisodes et 2 adaptateurs | même fichier, ligne 698 |
| suite d'essais figée sur la machine (7a) | 0,58 h ; instance 13,59 h pour 12,97 h de course | même fichier, ligne 698 |
| pic de mémoire de la carte aux épisodes | 26,0 Gio ; un échec d'allocation sans arrêt au début d'un entraînement d'adaptateur | même fichier, ligne 702 |
| course de confirmation 7b entière | **14,97 h, 18,16 USD** (soit 1,213 USD par heure tout compris) | `registres/depenses.md`, ligne 421 ; `registres/decisions.md`, ligne 2371 (R-2413) |
| débit brut ancien (validation de T0.4, mode déterministe, simple précision) | 25,5 jetons par seconde en lot de 8 | `registres/decisions.md`, ligne 133 |

**Durée d'un pas de distillation : dérivée, non mesurée.** Aucun registre ne donne la durée d'un pas. Je la déduis de 7a : 4,36 h moins la génération de 320 épisodes (3,57 h à 40,2 s ; 3,81 h à 42,8 s) laisse 0,56 à 0,79 h pour 2 adaptateurs × 480 pas = 960 pas, soit **2,1 à 3,0 s par pas**. C'est un majorant probable (le reste contient aussi le chargement et les contrôles d'identité). **Hypothèse à relever.** Je chiffre à 3,0 s.

**Réserve.** Ces épisodes n'étaient pas des épisodes honnêtes sans adaptateur et portaient une capture partielle d'activations. Le débit du bras A peut différer. Le bras A reste à relever (section 8).

## 3. Inventaire de ce qui tourne sur la carte

Retenu pour le chiffrage : 42,8 s par épisode, 3,0 s par pas.

| | poste | compte et formule | lecture courte | lecture longue |
|---|---|---|---|---|
| (a) | **Passe de fabrication** : épisodes honnêtes du modèle de base sur les 16 tâches de fabrication (premier addendum, section 5 ; conception, section 1.1, point 2) | 16 tâches × 8 épisodes = 128 épisodes ; × 10 pas = 1 280 actions | 128 × 42,8 s = **1,52 h** | **1,52 h** |
| (b) | **Fabrication par programme** : dérangement des champs `CONTROLS` (quatre doses), identité pour (vi-T), dérangement de `PREDICTION` pour (vi-B) | sur processeur, aucun appel de modèle (conception, ligne 35) | **0 h de carte** si elle tourne hors de la machine ; quelques secondes sinon | idem |
| (c) | **Distillation** : un adaptateur de rang 16 par dose non nulle, plus (vi-T), plus (vi-B) ; 128 transcriptions × 3 époques, lot 1 = **384 pas** par adaptateur (second addendum, sections 2 et 4) ; une transcription ≈ 4 319 jetons | adaptateurs × 384 pas × 3,0 s | 6 × 384 = 2 304 pas = **1,92 h** | 9 × 384 = 3 456 pas = **2,88 h** |
| (d) | **Rejeu sur les 16 tâches de vérification** : honnête H (c'est la dose 0, modèle de base sans adaptateur), chaque dose, témoins ; mêmes graines d'action | conditions × 128 épisodes × 10 pas (texte scellé, ligne 161) | 7 × 128 = 896 épisodes, 8 960 actions = **10,65 h** | 10 × 128 = 1 280 épisodes, 12 800 actions = **15,22 h** |
| (e) | **Contrôle d'identité à dose nulle et son artefact** (M-4 : égalité au bit près à dose 0, écart exigé à dose 1), une fois par adaptateur | quelques passes avant ; **hypothèse**, non mesurée : 1 minute par adaptateur | **0,10 h** | **0,15 h** |
| (f) | **Mise en route** : location, image, clonage, téléchargement du modèle (≈ 16 Go), suite d'essais figée | 0,58 h d'essais (7a) + ≈ 0,2 h ; la liste d'essais du bras A est neuve, sa durée est **à relever** | **0,8 h** | **0,8 h** |
| | **Total** | | **≈ 15,0 h** | **≈ 20,6 h** |

**Ce qui ne coûte pas de carte dans cet inventaire.**
- Contrôles de manipulation M-1 (moitiés échangeables), M-2 (la couverture baisse à dose 1), M-3 (invariance du nombre de jetons et du multiensemble des contrôles) : calculs sur processeur. M-1 et M-2 exigent les lectures de l'oracle de couverture (section 4).
- Épreuves de l'oracle sur 32 épisodes honnêtes (2 par tâche) : je suppose qu'ils sont tirés parmi les épisodes honnêtes déjà joués. Le texte scellé (ligne 190) ne dit pas de quelles tâches. Si une génération à part est voulue : 32 × 42,8 s = 0,38 h de plus.
- Estimation de l'écart-type et de l'effet minimal détectable, lecteurs 1, 2 et 5, agrégateur du lecteur 4, tests, intervalles, planchers : processeur. À faire tourner **hors de la machine louée**, sinon la carte est payée à vide.

**États internes au rejeu : non enregistrés, selon le texte.** Le texte scellé ne demande aucun enregistrement d'activations. Il interdit d'en lire (ligne 224, ligne 254). Le lanceur du bras A ne doit importer aucun module de lecture interne (carte du branchement, lignes 45 à 47). **Je chiffre sans enregistrement.** Si une lecture interne est décidée plus tard, les activations se recalculent par une passe sur texte imposé : 0,45 s par épisode, soit ≈ 0,11 à 0,16 h pour 896 à 1 280 épisodes, à refaire avec chaque adaptateur chargé. Si l'on voulait malgré tout tout enregistrer au rejeu, ordre de grandeur **par hypothèse** (3 couches de la configuration, 4 096 dimensions, demi-précision, 4 319 jetons) : ≈ 106 Mo par épisode, soit ≈ 95 Go (896 épisodes) à ≈ 136 Go (1 280), au bord du disque minimal de 150 Go de la configuration (ligne 112). C'est un nœud, pas une option de ce devis.

**Disque et trafic sans activations.** Modèle ≈ 16 Go, image et dépôt ≈ 4 Go ; adaptateurs 6 à 9 × ≈ 27 Mo ; épisodes en texte et identifiants : moins de 1 Go. Montée attendue : moins de 2 Go.

## 4. Ce qui ne tourne pas sur la carte et coûte ailleurs

Le texte scellé ne nomme aucun modèle (règle d'anonymisation, ligne 16). Il ne dit pas si ces lecteurs sont des appels payants ou des modèles ouverts sur carte. **En dollars : non chiffrable en l'état.** Je donne les comptes d'appels, et un volume de jetons d'ordre de grandeur tiré des longueurs de la section 2.

| poste | compte et formule | volume, ordre de grandeur | dollars |
|---|---|---|---|
| **Oracle de couverture** : deux lecteurs hors des familles des moniteurs, un plan entier par lecture (texte scellé, section 2) | au moins 5 doses + (vi-B) (ligne 8 des critères de lecture) = 6 conditions × 128 épisodes × 2 lecteurs = **1 536 lectures** ; avec (vi-T) : 1 792 ; lecture longue : 2 560. Doublé si les moitiés D et V se lisent en deux appels (non dit) | 7 à 11 millions de jetons d'entrée, plus la référence ; sortie ≈ 300 jetons par lecture (hypothèse de l'ancien devis, ligne 24) | **non chiffrable** : lecteurs non nommés |
| **Cinq épreuves de l'oracle** sur 32 épisodes honnêtes (section 6.6) | 4 épreuves × 32 + 1 × 8 = 136 plans × 2 lecteurs ≈ **272 lectures** au moins (l'ancien devis comptait 320) | ≈ 1,2 million de jetons d'entrée | **non chiffrable** ; petit devant le poste précédent |
| **Ancre humaine** (épreuve 5) : jugement écrit d'avance sur 8 épisodes | 8 jugements | temps de rédaction, pas de calcul | 0 USD de calcul |
| **Moniteur boîte noire par action en contexte** (lecteur 3) | 5 doses × 1 280 actions = **6 400 lectures** au moins ; 8 960 à 12 800 si les témoins sont lus | ≈ 18 millions de jetons d'entrée (2 866 par lecture), sortie courte | **non chiffrable** : modèle et lieu d'exécution non dits |
| **Agrégateur séquentiel** (lecteur 4) | réemploie les scores du lecteur 3 | — | 0 |
| **Juge d'une autre lignée** (lecteur 6) | **2 560 lectures** (ligne 147) | ≈ 7 millions de jetons d'entrée | **non chiffrable** : juge non nommé, aucun tarif relevé au dépôt pour lui |
| Lecteurs 1, 2 et 5, test à deux échantillons, intervalles, planchers | processeur | — | 0 |

Repère du dépôt, sans valeur de prix pour ce poste : l'ancien devis réservait une ligne à part de 10 USD pour ces appels (ligne 83). **Je propose un devis à part pour les lectures**, une fois les lecteurs nommés, avec un tarif relevé et daté. Ces lectures ne se font qu'après l'étape (e) de l'ordre gelé (texte scellé, section 6.3) : elles n'ont pas à être payées avec la course.

## 5. Prix

| relevé | valeur | source |
|---|---|---|
| A100 SXM4 80 Go, dernier prix relu au dépôt | **1,1833 USD par heure**, stockage compris, le **2026-11-18T15:44:24Z** | `registres/depenses.md`, ligne 515 |
| mêmes cartes, du 13 au 16 novembre | 1,04 à 1,27 USD par heure | `registres/depenses.md`, lignes 440, 459, 466, 470, 476 |
| prix effectif de la course 7b, tout compris | 1,213 USD par heure (18,16 USD ÷ 14,97 h) | `registres/depenses.md`, ligne 421 |
| borne de prix de la configuration de référence | **1,30 USD par heure** ; stockage ≤ 0,08 USD par heure ; téléchargement ≤ 0,05 USD par Go, 40 Go prévus | `prereg/T0.6-organismes-config-7b-v1.json`, lignes 41, 115 à 117 |

**Prix du devis : 1,30 USD par heure.** Raison : la liste d'arrêt du texte scellé interdit de démarrer si le prix relevé dépasse le prix du devis (ligne 239). Prendre le dernier prix relu comme prix du devis bloquerait la course à la moindre hausse. L'attendu est calculé à 1,1833 ; le plafond à 1,30.

**À relever de nouveau avant la ligne de calcul** : le prix de l'offre et le prix relu de l'instance le jour même ; le stockage par heure ; le prix du téléchargement par Go ; le pilote de l'hôte (une offre à pilote trop ancien a déjà fait échouer une instance : `registres/depenses.md`, ligne 468).

## 6. Attendu, pire cas, plafond proposé (carte seule)

| | lecture courte (6 adaptateurs, 7 conditions) | lecture longue (9 adaptateurs, 10 conditions) |
|---|---|---|
| heures de carte, retenues (42,8 s ; 3,0 s) | 15,0 h | 20,6 h |
| heures de carte, bas de fourchette (40,2 s ; 2,1 s) | 13,7 h | 18,7 h |
| calcul à 1,1833 USD par heure | 16,2 à 17,7 USD | 22,1 à 24,3 USD |
| téléchargement (20 à 40 Go, ≤ 0,05 USD par Go) | 0,5 à 2 USD | 0,5 à 2 USD |
| **attendu** | **≈ 17 à 20 USD** | **≈ 23 à 26 USD** |

Contrôle de vraisemblance : la course 7b a joué 896 épisodes et 2 adaptateurs en 14,97 h pour 18,16 USD. La lecture courte joue 1 024 épisodes et 6 adaptateurs, sans le test croisé sur processeur de 7b (1,76 h). Même ordre.

**Pire cas**, trois multiplicateurs cumulés :

| facteur | hypothèse | effet |
|---|---|---|
| carte plus chère | 1,30 au lieu de 1,1833 USD par heure | × 1,10 |
| débit deux fois plus lent (hôte lent, ou épisodes plus longs que ceux de la référence) | 85,6 s par épisode, 6,0 s par pas | × 2 |
| une relance complète (erreur de chaîne en fin de course) | toute la course rejouée une fois | × 2 |

- Lecture courte : 15,0 h × 2 × 2 = 60,0 h × 1,30 = 78 USD, plus 4 USD de téléchargement : **pire cas ≈ 82 USD**.
- Lecture longue : 20,6 h × 2 × 2 = 82,3 h × 1,30 = 107 USD, plus 4 USD : **pire cas ≈ 111 USD**.

**Plafond proposé pour la ligne de calcul : 85 USD (lecture courte) ou 115 USD (lecture longue).** Au-delà d'une relance, toute relance nouvelle serait un nœud. Recommandation de forme : faire d'abord la passe de relevé du débit (section 8, point 1) ; si elle confirme 40 à 45 s par épisode, le plafond peut être ramené à environ deux fois et demie l'attendu (≈ 50 et ≈ 65 USD).

## 7. Ce que ce devis ne couvre pas

- **Les lectures par appels de modèles** (oracle de couverture, lecteur 3, lecteur 6) : section 4, devis à part.
- **Le repli de deuxième ligne** (choix adverse parmi plusieurs tirages honnêtes, texte scellé, section 9.2) : il demande sa propre passe de génération et son propre avenant (premier addendum, section 3).
- **Le bras B de la conception** (coûts anti-ordonnés) : préenregistrement distinct, devis distinct.
- **La lecture interne** (activations, sondes) : interdite ici ; toute passe d'activations est un devis à part.
- **Toute lecture sur les 64 tâches d'évaluation** : elles restent vierges.
- **Une carte de repli plus grosse** en cas d'erreur de mémoire à la distillation. La chaîne précédente a vu un échec d'allocation sans arrêt (section 2). Le bras A enchaîne 6 à 9 adaptateurs : le risque existe. Un repli sur une autre carte serait un nœud et un autre prix.
- **Le disque d'une instance arrêtée et gardée** après la course : non compté. À 0,08 USD par heure au plus, 72 h coûteraient 5,8 USD au plus ; mieux vaut rapatrier et détruire.
- **La dépense de la passe de relevé du débit** si elle se fait à part (section 8, point 1).

## 8. À relever ou à éprouver avant de demander le GO

1. **Le débit réel du bras A** : secondes par épisode honnête en lot de 8, et secondes par pas de distillation sur une transcription entière. Une passe d'un lot de 8 épisodes et de vingt pas suffit : environ dix à quinze minutes après la mise en route, soit ≈ 1 h de carte et ≈ 1,3 USD, sur sa propre ligne. Le pas de distillation n'a jamais été mesuré seul.
2. **La part d'actions permutables sur le vrai tokeniseur**, hors ligne, sans dépense. Avec la coupe de la première version de la fabrication, presque toutes les actions seraient non permutables (carte du branchement, lignes 39 à 44). Si la part est faible, des épisodes restent honnêtes et la dose réelle baisse. Le coût ne change pas ; l'utilité de la dépense, si.
3. **La disponibilité et le prix d'une A100 SXM4 80 Go conforme** le jour du lancement (prix, stockage, téléchargement, pilote).
4. **La lecture du témoin (vi-B)** : une proportion ou une par dose (section 1, point 1). Elle déplace l'attendu de 6 USD et le plafond de 30 USD.
5. **La durée de la liste d'essais figée du bras A** sur la machine (elle n'existe pas encore ; carte du branchement, ligne 56).
6. **Les lecteurs externes** : lesquels, sur carte ou par appels, à quel tarif ; et la stratification du sous-échantillon de 2 560 actions (section 1, point 2).
7. **La configuration neuve** : celle de référence porte un calendrier clos (fin au 2026-11-17, lignes 32 à 35) et l'ancien numéro de GO. Le bras A exige sa configuration, son prix maximal et son plafond propres.
8. **Le second addendum scellé** (384 pas), et la contre-lecture de ce devis (R2).
9. **Où tournent les calculs sur processeur** (fabrication, contrôles, lecteurs 1, 2, 5) : hors de la machine louée, sinon ajouter leur durée aux heures de carte.

## 9. Déclaration

Rédigé par un agent neuf, qui n'est auteur ni du texte scellé, ni de ses addenda, ni de la conception, ni du code. **Non contre-lu.** Aucune machine lancée, aucun appel réseau, aucune dépense. Aucun fichier de résultat, de base, de sonde ni de moniteur n'a été ouvert ; aucun fichier sous `runs/` ni `diag/`. Hors des pièces de la section 0, seuls ont été lus, par recherche de lignes, `registres/depenses.md`, `registres/decisions.md`, `registres/etat.md` et les lignes 635 à 702 de `prereg/T0.6-organismes-v0-v1.md`. Les durées citées sont des relevés de la chaîne de l'organisme précédent, non du bras A. La durée d'un pas de distillation, la durée du contrôle d'identité et la taille des activations sont des hypothèses, marquées comme telles.
