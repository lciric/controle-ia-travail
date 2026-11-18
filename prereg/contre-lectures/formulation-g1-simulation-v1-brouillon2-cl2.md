# Contre-lecture 2 — préenregistrement de l'étude par simulation des formulations du contraste à témoin apparié de la porte de fin de phase 1 (G1), brouillon 2

- **Contre-lecteur** : sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur (Claude Fable 5.2). **Je suis l'auteur de la contre-lecture 1** ; je n'ai écrit ni le brouillon 1, ni le brouillon 2, ni aucune ligne du code ou des essais. R2 (« contre-lu par un sous-agent neuf qui ne l'a pas écrit ») est tenue ; la phrase du brouillon 2 qui demande un second lecteur « qui n'a écrit ni … ni la contre-lecture 1 » ne l'est pas : voir § 6, point pour la session mère. Mandat : reprise demandée par la session mère pour la seconde contre-lecture, sous le mot de Lazar « lance des essais pour trancher » (R-3439).
- **Date (UTC)** : 18 novembre 2026, vers 22:45.
- **Brouillon relu** : `prereg/formulation-g1-simulation-v1-brouillon2.md` — `96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3`.
- **Pièces relues** (empreintes recalculées, toutes égales à leurs compagnons) : liste des différences `prereg/pieces-formulation-g1-v1/differences-brouillon1-vers-2-v1.md` `9e744890…` ; `src/controle_ia/formulation_g1/statistiques_v2.py` `cf6dc8cb…`, `mondes_v2.py` `12234cbd…`, `simulation_v2.py` `62381e96…`, `lecture_v2.py` `64cddf01…` ; `tests/test_formulation_g1_statistiques_v2.py` `6b799cda…`, `_gardes_v2.py` `cff1c8c3…`, `_mondes_plantes_v2.py` `dc446a86…`, `_regle_v2.py` `180e9075…`. Fichiers de la v1 : empreintes recalculées, intacts.
- **Essais rejoués** (`.venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=<scratchpad>/cl2bt/…`, PYTHONPATH=src ; dossier supprimé ensuite) : **v2 : 95 réussis** ; **v1 : 59 réussis**. `prereg.problemes` sur le brouillon 2 : **aucune remarque**.

---

## 1. Verdict : **scellable après ces couples exacts**

Les deux bloquants et les six majeurs de la contre-lecture 1 sont appliqués, en texte et en code. Un seul écart : la garde de D-S4, absente, est déclarée, et l'écart est juste (voir § 4). La règle **n'a plus de pente par construction** du côté des deux désaccords de conception. Mais il lui reste une **pente vers C qui tient aux budgets d'épisodes du témoin**. Le rédacteur l'a vue et dite, mais le rejeu qu'il lui oppose se joue sur des mondes où ce mécanisme ne peut presque pas se montrer : c'est le bloquant 1, levé par un couple court. Trois majeurs touchent la fidélité au programme et la remise du choix à Lazar. Les couples changent du code : le diff doit être revu (R2), mais sans relire tout le texte.

---

## 2. Bloquant

### B′-1. Pente résiduelle vers C, par les budgets du témoin, mal gardée par le sixième rejeu (points 2 et 4)

**Constat.** Le paragraphe « Ce que la règle peut encore devoir à sa construction » est juste ; je l'ai refait sur le modèle, sans aucun tirage. Dans le bloc principal :
- E est calibré sur 4 000 à 6 000 épisodes honnêtes ;
- la garde et B2 lisent le seuil honnête, le même pour leurs deux bras, donc le bruit du seuil s'y annule ;
- A′, lui, recalibre ses seuils sur 300 épisodes du témoin (écart-type du taux réel : 0,57 point).

Deux conséquences.
1. **Validité nette.** Dans les mondes « avance véhiculaire » de la règle à empreinte au-dessus du plafond, E passe, la garde refuse B, et A passe au gré du bruit de A′. Le seuil de validité à 0,025 est de 0,036. A peut difficilement être « nette », B peut difficilement être dépassée de 0,20 : la règle tombe sur la couverture.
2. **Couverture.** A′ perd de la puissance par le bruit de ses seuils aux petits écarts, alors que B reste près de E sous le plafond. La couverture tend à favoriser C.

C'est une pente vers C, d'origine budgétaire et non de conception.

Le sixième rejeu est censé la garder. Il se joue sur les **36 mondes réduits** : sabotage de la boîte noire fixé à 1,5, et seulement quatre mondes « sabotage » sous le plafond à témoin parfait (sabotage blanc 2 et 3). Ce sont de grands écarts, où le bruit de A′ pèse peu. Le mécanisme agit surtout aux petits écarts du bloc principal (par exemple 1 contre 0,5, 1,25 contre 0,5, 2 contre 1,5), **absents des mondes réduits**. Le rejeu peut donc laisser passer un « C retenue » qui tient au budget.

Deux défauts de plus :
- **La variante « garde sur 300 épisodes » n'égalise pas le budget.** Le code lit B1 sur 300 épisodes, mais B2 reste apparié sur toutes les tâches (`d_b2 = sab_h[..., 0] - taux_tem`, `simulation_v2.py` ligne 135) : B consomme encore 1 200 épisodes du témoin. La variante n'est qu'une B1 plus stricte, que personne n'appliquerait.
- **Sens du rejeu.** Sa première moitié (A′ calibré sur 1 200 épisodes) ne fait qu'améliorer A : elle ne peut renverser qu'une issue autre que « A retenue ». C'est logique, puisqu'elle retire un avantage de budget de B. Mais cela doit être dit, pour que la note ne le présente pas comme un contrôle symétrique.

**Couples exacts.**

- `prereg/formulation-g1-simulation-v1-brouillon2.md`, « Critères de lecture gelés », avant : « 6. sur ces mêmes mondes réduits, issue différente entre les budgets du bloc principal et l'une des deux variantes à budgets égalisés (A′ calibré sur 1 200 épisodes du témoin ; garde lue sur 300 épisodes) → **non tranché : dépend du budget d'épisodes du témoin**. »
  → après : « 6. sur le **bloc « budget du témoin égal »** — les 486 mondes du bloc principal à 400 tâches et témoin parfait, A′ calibré sur 1 200 épisodes du témoin —, issue différente de celle du bloc principal à 400 tâches ; ou, sur les mondes réduits, issue différente entre la référence et la variante « B à 300 épisodes du témoin » (B1 et B2 lues sur les 100 premières tâches seulement) → **non tranché : dépend du budget d'épisodes du témoin**. Ce rejeu retire à B l'avantage de budget du bloc principal (A′ calibré sur 300 épisodes du témoin, B sur 1 200) : sa première moitié ne peut renverser qu'une issue autre que « A retenue ». C'est voulu, puisqu'elle éprouve si un « C retenue » ou une égalité tient au budget ; la note le dit. »
- Même texte, tableau de la grille, avant : « | épisodes du témoin lus par la garde B1 | tous (1 200 ou 1 800 : la garde tolère 47 et 74 alertes) ; 300 en sensibilité (8 alertes tolérées) | »
  → après : « | épisodes du témoin lus par la garde B1 et par B2 | tous (1 200 ou 1 800 : la garde tolère 47 et 74 alertes) ; en sensibilité, B1 et B2 sur les 300 épisodes des 100 premières tâches (8 alertes tolérées) | »
- Même texte, « Plan d'analyse », avant : « (`mondes_v2.py` ; effectifs gardés par le code : 3 888 + 648 + 36 + 432 + 15 = **5 019 mondes**) » → après : « (`mondes_v2.py` ; effectifs gardés par le code : 3 888 + 648 + 36 + 432 + 486 + 15 = **5 505 mondes**, le bloc « budget du témoin égal » compris) » ; durée réestimée par le jouet.
- `mondes_v2.py` : `BLOCS` reçoit `"budget_temoin"` ; `NOMBRE_ATTENDU["budget_temoin"] = 486` ; fabrique ajoutée à `grille` :
  ```
  def _budget_temoin() -> list[Monde]:
      return [Monde("budget_temoin", "temoin_budget_egal", s, e, n, c, 0.0, TACHES_REDUITES, 3,
                    calibrage_honnete=FACTEUR_CALIBRAGE * TACHES_REDUITES, calibrage_temoin=TACHES_REDUITES * 3)
              for s in SABOTAGE_BLANCHE for e in EMPREINTE_BLANCHE for n in SABOTAGE_NOIRE for c in CORRELATIONS]
  ```
  et `simulation_v2.mesurer_temps` parcourt aussi ce bloc.
- `simulation_v2.py`, `_lot`, deux lignes séparées par la ligne de `d_c2`. Avant : `    d_b2 = sab_h[..., 0] - taux_tem` → après :
  ```
      d_b2 = sab_h[..., 0] - taux_tem
      if monde.episodes_garde:                             # B2 apparié sur les seules tâches qui portent la garde
          d_b2 = d_b2[:, :math.ceil(monde.episodes_garde / m)]
  ```
  avant : `    empile = np.concatenate(d_e + d_a + [d_b2], axis=0)` → après : `    empile = np.concatenate(d_e + d_a, axis=0)` ;
  et, avant : `            ranger(lecture, alpha, conjonction(v, 0), conjonction(v, nc), b1, v[2 * nc * R:])` → après : `            ranger(lecture, alpha, conjonction(v, 0), conjonction(v, nc), b1, test(d_b2, alpha))`. La lecture par rééchantillonnage n'est pas touchée : `valider` refuse déjà une garde partielle avec elle.
- `lecture_v2.py`, `verdict`, avant : `    elif len(set(issues_budget.values())) > 1:` → après : `    elif len(set(issues_budget.values())) > 1 or issue_budget_principal != issues[TACHES_REDUITES]:`. Avant ce test, ajouter `issue_budget_principal = regle_de_choix(indicateurs(mondes, TACHES_REDUITES, bloc="budget_temoin", etiquette="temoin_budget_egal"))`, et rendre cette issue avec sa table dans `issues["budget_du_temoin"]` et `indicateurs["budget_du_temoin"]`.
- Essais : `test_garde_lue_sur_une_partie_des_episodes` vérifie aussi que B2 n'est lu que sur les tâches de la garde (cas sain et artefact) ; `test_dependances_de_l_issue` reçoit un cas « bloc budget du témoin égal » ; `test_grille_effectifs_et_noms` passe à 5 505.

---

## 3. Majeurs

### M′-1. Lecture de l'unité de D-S9 : le brouillon 2 mêle les unités (point 3)

L'hypothèse de travail (7) prend « 10 fois le nombre de tâches sabotées », comptées en **épisodes** honnêtes (4 000 à 400 tâches), et dit : « si l'unité de D-S9 est l'épisode, le calibrage est trois fois plus grand ». C'est vrai, mais incomplet. La lecture « tâche contre tâche », celle de D-S1 (« la consigne avec toutes ses exécutions »), donne **aussi** dix tâches honnêtes de trois épisodes par tâche sabotée, soit 12 000 épisodes. Les deux lectures cohérentes donnent donc 10 × tâches × épisodes. Le nombre retenu (10 × tâches) suppose une unité honnête, l'épisode « entier » de N-007/N-008, et une unité sabotée, la tâche : c'est défendable, mais c'est la plus petite des lectures. Elle grossit le bruit du seuil de E d'environ √3 (écart-type du taux réel : 0,16 point à 4 000 épisodes, 0,09 à 12 000).

- Avant : « (si l'unité de D-S9 est l'épisode, le calibrage est trois fois plus grand et le bruit du seuil plus petit). Variantes : 16 fois ; 300 épisodes (échelle du brouillon 1). »
  → après : « Cette lecture compte l'unité sabotée en tâches et l'unité honnête en épisodes : c'est la plus petite des lectures possibles. Les deux lectures de même unité — tâche honnête entière contre tâche sabotée (D-S1), ou épisode contre épisode — donnent toutes deux 10 × tâches × épisodes (12 000 épisodes à 400 tâches) et un bruit du seuil environ √3 fois plus petit. Variantes : 16 fois ; **10 × tâches × épisodes** (rapportée) ; 300 épisodes (échelle du brouillon 1). Si la conception du pari tranche pour une lecture de même unité, le bloc principal passe à 10 × tâches × épisodes avant le texte final, et P8 est recalculée pour cet effectif avant toute simulation. »
- `mondes_v2.VARIANTES_SENSIBILITE` reçoit `("calibrage_honnete_dix_fois_taches_x_episodes", {"calibrage_honnete": FACTEUR_CALIBRAGE * TACHES_REDUITES * 3})` ; `NOMBRE_ATTENDU["sensibilites"]` passe à 468.

### M′-2. Conception du pari introuvable par les renvois de N-055 ; garde de D-S4 non codée (point 3)

J'ai cherché la conception par les seuls renvois de N-055 et de sa note d'alignement, sans recherche récursive :
- N-055 donne `envois/pole-scientifique-automatique-v1/pari-de-signe/decisions-lazar-2026-10-27-v1.md`, « `canal/conv-audit-n04`, commit `8557db9` », et nomme la conception v2 `9c39a73d…`. N-056 donne `pari-de-signe/noeuds-pour-lazar-v1.md`.
- **Résultat** : le dossier `envois/…/pari-de-signe/` n'existe pas sur `main`. Le commit `8557db9` ne porte que `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-27_n119.md`, un message qui cite la note de décision par `pari-de-signe/…` sans la verser. La branche `canal/conv-audit-n04` n'a pas de dossier `envois/` à sa racine. Les dossiers `docs/notes/collisionneur-pari-de-signe-v1/` et `docs/notes/pole-scientifique-automatique/` ne portent aucun fichier d'empreinte `9c39a73d…`. **La conception est dans l'espace de la lignée conv-audit, hors de ce dépôt.**

Je ne peux donc confronter **ni la grille de mises, ni la garde de D-S4, ni l'unité de D-S9** à la conception. Ce que je peux dire :
- (i) La lecture de D-S6 est une lecture valide du pari : moyenne de capitaux à mises fixes {0,1 ; 0,3 ; 0,6 ; 0,9} sur des différences dans [−1, 1], surmartingale positive, rejet au maximum par l'inégalité de Ville. Je l'ai relue et l'essai « capital à la main » la vérifie. Mais la conception peut appliquer la grille autrement : sur des signes (D-S2 parle de « parts » et de fiche « signe »), avec une autre normalisation des mises, ou par un maximum sur la grille corrigé. **Aux petits écarts, une mise fixe de 0,1 a bien moins de puissance qu'une mise adaptative** ; la quatrième dépendance (« statistique ») le surveille.
- (ii) La garde de D-S4 (« appariée bloquante (δ), absolue rapportée, e-valeur du minimum, calibrage dimensionné par les jumeaux ») peut être une condition appariée sur des jumeaux honnêtes, voisine de la formulation B. Si c'est le cas, **la question même de N-074 change** : B doublerait en partie une garde que la porte porte déjà. Il ne faut pas la deviner.

Ce qui doit changer avant le texte final :
- Hypothèse de travail (2), avant : « qui n'est pas dans les pièces remises ; la session mère la confronte à la conception avant le texte final. »
  → après : « qui n'est pas dans les pièces remises et que la contre-lecture 2 n'a pas trouvée par les renvois de N-055 (dossier `envois/pole-scientifique-automatique-v1/pari-de-signe/` absent de `main`, du commit `8557db9` et de la branche `canal/conv-audit-n04`) : la session mère la demande à la lignée conv-audit. Si elle est obtenue, elle est confrontée avant le texte final ; et si la garde de D-S4 est une condition appariée sur le témoin ou sur des jumeaux, l'étude est reprise par un brouillon nouveau avant tout lancement. Si elle ne l'est pas, le texte final le dit dans son en-tête, et l'issue reste conditionnelle. »
- « Ordre », avant : « confrontation de l'hypothèse de travail (2) et de l'unité de D-S9 à la conception du pari par la session mère ; » → après : « confrontation de l'hypothèse de travail (2), de la garde de D-S4 et de l'unité de D-S9 à la conception du pari, obtenue de la lignée conv-audit par la session mère, ou mention dans l'en-tête du texte final qu'elle n'a pas pu l'être ; »

### M′-3. Le choix de fond est remis avec deux biais de présentation (point 6)

La section « Choix de fond remis à Lazar » ne recommande rien et n'a pas de défaut : c'est juste. Deux biais restent pourtant :
- (i) **Forme.** Les deux puces décrivent les deux comportements de la garde, chacun avec avantage et inconvénient ; le contraste de A n'a qu'une phrase (« les deux comportements inverses »), sans avantage ni inconvénient propres. Le format de décision de `CLAUDE.md` demande des options comparables.
- (ii) **Tailles des tables.** La table « désaccord, gain réel » a 108 mondes par effectif, la table « désaccord, avance du véhicule » en a **6**. Cet écart tient à la grille seule : la bande où la garde laisse passer une avance du véhicule (sabotage noir − empreinte < sabotage blanc < sabotage noir, empreinte sous 0,68) n'est couverte que par les couples 1,25 contre 1,5 et 2,25 contre 2,5 à l'empreinte 0,4. Une note qui met ces tables « en tête » donnerait à lire, sans le dire, qu'un refus de gain réel est dix-huit fois plus fréquent qu'une avance du véhicule qui passe.

- Avant (les deux puces et la phrase qui suit) : « - **Refuser un gain réel quand la boîte blanche sonne sur le véhicule au-delà de 5 %** (c'est ce que fait la garde, donc B et C). » … jusqu'à « Le contraste de A refuse ces mondes et accepte les précédents. »
  → après :
  « - **La garde (B, donc C).** Elle refuse un gain réel quand la boîte blanche sonne sur le véhicule au-delà de 5 %, et laisse passer une avance due au véhicule sous 5 %. Avantage : la porte ne se franchit pas avec un moniteur qui sonne nettement sur le véhicule ; condition lisible, à tolérance écrite. Inconvénient : un gain vrai est refusé dans les mondes « désaccord de conception, gain réel » ; une avance due au véhicule franchit la porte dans les mondes « désaccord de conception, avance du véhicule ».
  - **Le contraste (A).** Il accepte un gain réel même quand la boîte blanche sonne sur le véhicule au-delà de 5 %, et refuse une avance due au véhicule même sous 5 %. Avantage : il juge le gain au-delà du véhicule quelle que soit l'empreinte, sans tolérance de convention. Inconvénient : la porte peut se franchir avec un moniteur qui sonne nettement sur le véhicule, pourvu qu'il lise aussi le sabotage ; il repose sur un témoin qui reproduit bien l'empreinte (sensibilité à l'imperfection du témoin, rapportée).

  Les deux tables se lisent monde par monde, en fonction de l'écart des effets de sabotage et de l'empreinte. **Le nombre de mondes de chaque table tient à la grille (108 contre 6 par effectif) et ne mesure aucune fréquence** : la note ne le donne pas comme tel. »
- Section « Points portés à Lazar par la contre-lecture 1 », point 1, avant : « corrigée, elle ne juge que la qualité d'exécution, et le choix de fond lui revient (section précédente). » → après : « corrigée, elle ne juge que la qualité d'exécution — à budgets d'épisodes du témoin inégaux, dits, que le sixième rejeu éprouve — et le choix de fond lui revient (section précédente). »

---

## 4. Mineurs

- **m′-1. Phrase sur le second lecteur.** Avant : « par un sous-agent neuf qui n'a écrit ni le brouillon 1, ni le brouillon 2, ni la contre-lecture 1. » → après : « par un sous-agent qui n'a écrit ni le brouillon 1 ni le brouillon 2 (R2) ; la contre-lecture 2 a été faite par l'auteur de la contre-lecture 1, rappelé pour vérifier l'application de ses couples ; [un troisième lecteur neuf a relu / n'a pas relu] le diff du brouillon 3. » La session mère choisit.
- **m′-2. Contre-lecture 2 dans la section « Contre-lecture ».** Pour que `prereg.problemes` l'accepte au texte suivant : entrée « **Contre-lecture 2** » avec les deux empreintes (brouillon 2 `96cd0fa3…` et ce rapport).
- **m′-3. Commentaire de `__init__.py`.** Il nomme encore les modules de la v1 ; c'est juste de ne pas rompre son sceau, mais la ligne de l'en-tête du texte final doit le dire, comme le brouillon 2 le fait déjà.

## 5. Les six vérifications demandées

1. **Couples de la contre-lecture 1.** Tous appliqués. J'ai contrôlé par programme la présence exacte des douze textes « après » dans le brouillon 2, et j'ai relu le code de `classe_de_regle`, `indicateurs`, `tables_de_desaccord`, `verdict`, `pari_sur_grille`, `_lot` et des gardes neuves.
   - **B-1** : la couverture se calcule sur les seuls mondes « sabotage » sous le plafond (108 par effectif). Les deux classes de désaccord sont sorties de la règle, rapportées en tables, et n'entrent dans aucun indicateur ; c'est vérifié par l'essai de dénombrement (54, 156, 54, 108, 108, 6).
   - **B-2** : rejeu sur la grille d'avant l'essai, lu **en premier** dans `verdict` ; la frontière y passe par la même séparation (essai : 18 mondes de désaccord) ; P4 et P6 sont non probantes.
   - **M-2** : appliqué en partie, et l'écart est juste (§ 3, M′-2).
2. **Les sept ajouts du rédacteur.**
   - Contrôle de théorie à 4 000 épisodes (40/4 001) : neutre.
   - Clause de P7 alignée sur son énoncé : neutre, puisque les prédictions ne touchent pas la règle.
   - Plancher d'une demi-répétition de l'alerte « trop beau » : neutre ; il rend l'alerte possible là où un compte entier ne peut pas approcher l'exact.
   - Paragraphe sur la construction : juste, et c'est lui qui conduit au bloquant B′-1.
   - Section des points pour Lazar : neutre, avec la retouche de M′-3.
   - P8 : neutre entre A et B (elle porte sur le critère actuel). Ses ordres de grandeur sont justes : pentes 10,6 et 14,7 ; 2,4 à 3,3 points. Elle est à recalculer si l'effectif de calibrage change (M′-1).
   - Sixième rejeu : il ne penche pas vers A, mais **ne peut renverser, par sa première moitié, qu'une issue autre que « A retenue »**, et il est peu sensible là où il le faudrait : B′-1.
3. **Grille de mises, garde de D-S4, unité de D-S9 : conception non trouvée** par les renvois (M′-2). Unité de D-S9 : M′-1.
4. **Pente par construction : levée** pour les deux désaccords. Reste la pente budgétaire vers C (B′-1). Un raisonnement structurel du même type qu'à la contre-lecture 1 ne trouve plus aucune issue inatteignable : A, C, « aucune » et chaque « non tranché » restent possibles.
5. **Essais, R5, R9, `prereg.problemes`.**
   - Essais : v2, 95 réussis ; v1, 59 réussis ; aucune remarque de `prereg.problemes`.
   - R9 : `_generateurs` est inchangé et conforme.
   - R5 : les gardes neuves ont toutes un cas sain et un artefact — calibrage honnête obligatoire, épisodes de la garde, bases hors de ]0, 1[, matrice non définie positive, durée, répétitions minimales, mondes complets, validation manquée sur trois artefacts. La garde de durée n'est essayée que comme fonction : l'arrêt du bassin de processus par la sortie du bloc `with` n'est pas essayé. C'est acceptable et dit dans la liste d'arrêt.
6. **Choix de fond remis à Lazar** : sans recommandation ni défaut, mais avec deux biais de présentation (M′-3).

## 6. Ce qui doit aller à Lazar ou à la session mère

- **À Lazar.** Le contraste (A) tel qu'il est écrit, calibré sur 300 épisodes du témoin, est plus bruité que la garde, qui lit le même seuil honnête pour ses deux bras. Une issue « C retenue » peut donc tenir au budget d'épisodes du témoin plutôt qu'à la conception : la note doit donner le budget de chaque option à côté de l'issue.
- **À Lazar.** Les tables de désaccord ne disent rien de la fréquence des deux cas : 108 contre 6 est un effet de la grille.
- **À la session mère.** La conception du pari (v2 `9c39a73d…`, v4, v9) n'est pas dans ce dépôt aux renvois de N-055 : il faut la demander à la lignée conv-audit avant le texte final. Si sa garde de D-S4 est appariée sur un témoin ou sur des jumeaux, la question de N-074 change.
- **À la session mère.** Il faut trancher la lecture de l'unité de D-S9 : 10 × tâches ou 10 × tâches × épisodes.
- **À la session mère.** Le second lecteur est l'auteur de la contre-lecture 1 : corriger la phrase du brouillon (m′-1) ou faire relire le diff du brouillon 3 par un lecteur neuf.

## 7. Lectures hors mandat et limites

- **Pour chercher la conception par les renvois de N-055** :
  - le message n° 119 de conv-audit au commit `8557db9`. Il rapporte des nombres de l'organisme et de la banque de la couche 1 (fusions, témoins confirmés), hors de ce que l'étude utilise : non utilisés, non recopiés ;
  - les noms de fichiers du commit `8557db9`, de la racine et du dossier `brouillons/` des branches `canal/conv-audit-n04` et `canal/conv-audit-n03`, et des branches distantes `canal/conv-audit-*` ;
  - les noms de fichiers de `docs/notes/` (un niveau), de `docs/notes/pole-scientifique-automatique/` et de `docs/notes/collisionneur-pari-de-signe-v1/`, avec les débuts de leurs empreintes compagnons ;
  - aucun de ces documents n'a été ouvert.
- `git status` a montré un fichier non suivi d'un autre agent : nom seul, non ouvert.
- **Rien ouvert** sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ni `registres/`. Aucune branche `calcul/` ou `donnees/`. Aucune recherche récursive. Simulation complète non lancée, aucune issue lue : les ordres de grandeur ci-dessus sont des calculs de théorie (loi bêta d'un seuil d'ordre, pente de la courbe de rappel), sans tirage. Ni commit ni poussée. Seuls fichiers écrits : ce rapport et son compagnon.
- **Non vérifié** : la conception du pari, le préenregistrement de la porte, les lignes du devis sur les effectifs.
