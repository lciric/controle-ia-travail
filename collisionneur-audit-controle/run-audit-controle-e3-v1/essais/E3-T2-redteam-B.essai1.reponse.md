# Proposition B — Tour III.2 : équipe rouge croisée

**Pièces.** Les conceptions A et C sont présentes, non vides, et se terminent par leur marqueur de fin : je n'y vois aucune coupure. Tout ce qui vient de F2 garde le statut **OBSERVÉ-NON-AUDITÉ**, et tout ce qui vient de F1 et F3 le statut **RAPPORTÉ**. Les jugements sur les conceptions A et C sont les miens : ce sont des **HYPOTHÈSES** tant qu'aucune mesure ne les tranche. Tous les seuils que je propose sont **illustratifs**.

Je ne lisse pas. Sur trois points (autocorrélation, masquage, famille (iv)), A et C convergent. Je les attaque séparément, parce que leurs contrôles échouent pour des raisons différentes.

---

## Contre la proposition A

### (a) Failles

**A-1. Le duel AM-1 déplace la tautologie sans la supprimer.**
- **Ce qu'A voit juste.** F1 §3 pose B = Σδ, donc le budget est défini dans l'espace de la sonde, et « la puissance ne dépend que de B » devient circulaire.
- **Ce que le remède ne règle pas.** A propose une dose « dans l'espace de la tâche, vérifiée en aval ». Or la vérification aval de l'environnement (a) passe par un évaluateur faible sur rubrique (F1 §6). Si cet évaluateur est aussi, ou partage sa lignée avec, le moniteur boîte noire de D1 (b) (Llama-3.2-3B, RAPPORTÉ), la dose est calibrée sur ce que voit la boîte noire. La comparaison blanc/noir de H1 est alors biaisée par construction, en faveur du noir.
- **Duel non exhaustif.** H_A (proportionnalité) et H_B (seuil d*) ne couvrent pas une réponse concave sans seuil, comme une saturation. Une concavité falsifie H_A sans confirmer H_B : l'issue « ni l'un ni l'autre » n'est pas prévue.

**A-2. Le contrôle de permutation d'AM-2 est vrai par construction et ne localise rien.**
- Permuter les scores entre trajectoires détruit à la fois trois choses :
  - l'autocorrélation intra-trajectoire ;
  - l'effet aléatoire propre à chaque épisode (un décalage constant) ;
  - la dérive selon la position t.
- Toute procédure calibrée sur les marginales retrouve ≈ α sur des données permutées. Un taux réel supérieur à α avec un taux permuté ≈ α établit donc qu'une dépendance compte, pas laquelle.
- Or le remède diffère selon la cause : des e-variables conditionnelles corrigent l'autocorrélation, une normalisation par épisode corrige le décalage, une calibration par position corrige la dérive.

**A-3. La « cellule dormante » risque d'être inversée.**
- **Lecture d'A.** A prend la famille (iii) « verrouillée sans mot de passe » comme politique présente mais inactive.
- **Lecture probable.** Dans la convention des modèles verrouillés par mot de passe, telle que je comprends Greenblatt, Roger, Krasheninnikov, Krueger 2024 (*Stress-Testing Capability Elicitation With Password-Locked Models*, PDF listé par F2), l'absence de mot de passe est l'état de **sous-rendement actif** ; le mot de passe déverrouille la capacité. Ce point est à vérifier sur la fiche des organismes de l'institut britannique.
- **Conséquence.** Si la convention est celle-là, la cellule « dormante » d'A mesure exactement l'état actif, et son H_B (« la sonde lit la représentation de la politique ») serait « confirmé » par un vrai positif.
- **Variante famille (i).** L'autre option d'A, la famille (i) « avec condition de déclenchement non remplie », n'existe pas dans F1 : (i) est une consigne cachée sans déclencheur. En ajouter un change l'organisme évalué.

**A-4. Le contrôle d'AM-4 change d'instrument.**
- L'essaim Qwen sert de témoin « sans poids partagés ». Mais les sondes sont entraînées sur les activations de Llama (F1 §14) : sur Qwen, il faut d'autres sondes, avec d'autres échelles et d'autres planchers.
- Un écart de corrélation inter-agents entre essaims Llama et Qwen confond donc l'effet des poids partagés avec l'effet de l'instrument. F1 §15 note lui-même que la forme mesurée dans P3 n'a pas transféré de Llama à Qwen.

**A-5. AM-6 fait arbitrer le thème par un juge, ce qui est superflu et ambigu.**
- Sous honnêteté par construction, toute hausse d'alertes dans une strate thématique est une fausse alerte, par définition : aucun arbitre n'est nécessaire.
- Le juge ajoute une ambiguïté. S'il monte lui aussi, cela peut venir du thème, ou d'un vocabulaire partagé entre les deux instruments, qui ne sont pas indépendants.

**A-6. Glissements de statut et affirmations non tenues.**
- **(d)8.** A écrit que D6 et E7 « couvertes » sont « réfutées » par AM-6 et E-A1. Ce sont des hypothèses non exécutées : c'est une hypothèse présentée comme un résultat.
- **(g).** « Tous les duels […] et la cellule dormante se calculent sur ce cache, en CPU » est faux. Le placebo de semis (AM-5), la cellule dormante et les essaims d'AM-4 exigent des générations nouvelles.
- **Tice et al.** A écrit 2024 en disant reprendre F2, qui donne 2025 : année à vérifier.
- **D-A4.** Je ne peux pas confirmer le titre donné par A pour Bailey et al. : titre à vérifier.

**A-7. D-A1 ne mesure pas ce qu'il annonce.**
- « Contenu identique attribué différemment » teste l'effet d'une **étiquette** d'auteur, pas la reconnaissance de lignée, qui passe par le style du texte.
- La variante « paraphrasé vers une autre lignée » modifie le contenu, donc possiblement le signal de sabotage lui-même. Les deux bras confondent la variable visée avec une autre.

**A-8. E-A2 substitue un construit à un autre.**
- La sape délibérée de la surveillance par un moniteur (Benton et al. 2024) n'est pas la conscience d'évaluation d'un juge. A le concède, puis la présente comme « le protocole de mesure que F2 cherchait ».
- Un moniteur qui fausse ses notes et un moniteur qui se conduit différemment parce qu'il se croit testé ont des prédictions différentes. Le premier fausse ses notes dans les deux cadrages ; le second ne change de conduite que s'il se croit testé.

### (b) Hypothèses supposées sans test, avec la mesure

1. **AM-3 : la longueur est indépendante de la difficulté et du thème de la tâche.**
   - H_A : à tâche fixée, le score max ne dépend pas de la longueur.
   - H_B : la corrélation longueur–score disparaît dans les strates de tâche ; c'est alors un effet de tâche, pas d'extrême.
   - Mesure : corrélation intra-tâche contre inter-tâches.
   - Issues : ρ intra ≈ ρ de la sonde aléatoire > 0 falsifie H_B ; ρ intra ≈ 0 avec ρ inter > 0 falsifie H_A. Coût CPU.

2. **AM-5 : le gabarit de semis est séparable de son contenu.**
   - H_A : le placebo de semis (gabarit sans sabotage) est indiscernable du semé pour un classifieur de surface.
   - H_B : le placebo est lui-même discernable de l'honnête.
   - Si H_B tient, le placebo n'est pas un contrôle neutre, et le rappel de la sonde contre l'honnête reste confondu.
   - Mesure : classifieur de surface entraîné sur une moitié, évalué sur l'autre, en trois classes (honnête / placebo / semé).

3. **D-1 : « intention » signifie « intention en acte ».**
   - La cellule dormante présuppose qu'une sonde d'intention doit être basse quand la politique est inactive. Une sonde qui lit un plan détenu mais non exécuté peut être valide pour la sécurité.
   - H_A : le score prédit l'action à venir dans l'épisode.
   - H_B : le score est constant que l'action suive ou non.
   - Mesure : AUROC du score au pas t pour prédire un sabotage aux pas t+1…t+k, sur les épisodes où le taux de sabotage est inférieur à 100 %.

4. **(g) : le coût est dominé par le calcul et le préenregistrement.**
   - La mesure S5 de F2, retenue par A en (d)9, exige un audit aval humain ou par juge. Ce coût n'entre pas dans les « moins de 200 $ ».
   - Mesure : temps d'audit par épisode sur un pilote de 20 épisodes (illustratif), avant de chiffrer.

### (c) Contrôles négatifs dont l'absence serait fatale

- **AM-1.**
  - Épisodes à dose zéro, passés par toute la chaîne de semis.
  - Mesure du dommage aval par un évaluateur **disjoint** du moniteur boîte noire : autre lignée, ou vérification exécutable.
  - Sans ces deux témoins, la « dose de tâche » réintroduit l'instrument dans la définition.
- **AM-2.**
  - Deux permutations : permutation **par position** (on échange les scores de même t entre trajectoires, ce qui garde la dérive et détruit la dépendance intra-trajectoire) ; décalage circulaire intra-trajectoire.
  - Calibration sur des épisodes honnêtes **tenus à part** de ceux qui mesurent le taux d'alerte.
- **Cellule dormante.**
  - Vérification **comportementale** de l'état de chaque organisme (performance avec et sans mot de passe) avant toute lecture de sonde. Sans elle, le sens de la cellule est indéterminé.
- **AM-4.**
  - Contrôle intra-Llama : mêmes agents, affectation des instances de tâche **mélangée** (tâches partagées contre tâches distinctes). Le partage des poids est alors constant et seul le partage de tâche varie.

---

## Contre la proposition C

### (a) Failles

**C-1. Hypothèses présentées comme des résultats, et statuts déplacés.** C'est la faute la plus grave au regard de la règle 1.
- **(a)3.** « par construction mathématique » : que l'attention rende les jetons amont *architecturalement accessibles* est exact. Que leur contenu lexical soit *linéairement décodable* au jeton d'action est une question empirique.
- **(c)1.** « Comme démontré dans AM-2 et le Duel 2 » : le Duel 2 n'a pas été exécuté.
- **AM-1.** « va exploser en taux de faux positifs » est une prédiction écrite comme un constat.
- **(c)4.** « surestime la menace pour un modèle de 8B » est une hypothèse.
- **Ancrage matériel.** « absorbable […] sans retarder le jalon M1–M2 [RAPPORTÉ] » : F1 ne dit rien de tel, c'est l'estimation de C. Llama-3.3-70B est marqué « RAPPORTÉ » : F1 ne le nomme pas, F2 ne le mentionne que comme modèle d'une source (E4) ; il fallait OBSERVÉ-NON-AUDITÉ seul.
- **Préambule et (a)1.** Le marqueur « [VÉRIFIÉ] » est appliqué au propre jugement de C et à sa lecture de la question : aucune vérification n'a eu lieu.

**C-2. Le comptage de C contredit F2.**
- C écrit « page 1 seule pour 24 des 39 PDF ».
- Sur le texte transmis de F2 (table d), je compte 45 identifiants arXiv plus la fiche système, soit 46 documents. Trente d'entre eux sont lus en page 1 seule.
- Le constat qualitatif de C tient (l'essentiel n'est lu que sur le résumé), mais ses chiffres ne sont pas ceux de la pièce.

**C-3. Le contrôle HCC du Duel 2 n'est pas un contrôle lexical pur.**
- Le contexte « honnête contaminé » introduit trois choses à la fois :
  - le vocabulaire de la consigne ;
  - le concept d'une consigne interdite qu'on refuse ;
  - un amorçage qui peut modifier la conduite (prudence accrue, ou sabotage partiel).
- Une sonde qui monte sur HCC peut donc lire légitimement « délibère sur une consigne illicite », un état proche des concepts sondés (dissimulation, enjeux élevés), plutôt qu'un écho lexical.
- L'issue « le rappel chute de 25 points → la contre-mesure S2 est invalide » n'est donc pas univoque.

**C-4. L'ajout 5 et le Duel 3 créent une fuite construction → évaluation, et enfreignent l'invariant accepté.**
- **Biais vers H1 par construction.** La récompense de (iv-b) « combine le score du juge faible et la cible cachée ». Le juge faible de la tâche est de la lignée de Llama-3.2-3B, que C place lui-même parmi les juges boîte noire. Entraîner l'organisme contre l'évaluateur, voisin ou identique à la base boîte noire de H1, apprend à cet organisme à passer sous ce juge. L'écart blanc-sur-noir de H1 serait gonflé par construction.
- **Invariant réduit.** C écrit « garde de l'invariant 5 (aucun score de sonde) ». F3 dit « aucun score de moniteur (sonde, juge) », hors bras d'attaque déclaré : C a restreint l'invariant que le directeur a accepté.
- **Falsification asymétrique.** Un organisme appris par renforcement sur une rubrique biaisée peut exploiter la récompense sans aucune représentation d'un acte illicite. Un rappel proche du hasard sur (iv-b) ne falsifie alors pas « l'équivalence avec le réglage fin sur documents » : il peut signifier qu'il n'y a pas d'intention à lire.
- **Pas une nouveauté.** (iv-b) est déjà l'option (b) acceptée en F3.

**C-5. AM-3 (Mahalanobis) attaque un risque que le plan de F1 mesure déjà.**
- EC.2 croise rhétorique et intention dans un plan 2 × 2, honnête qui plaide compris (RAPPORTÉ). Une sonde de densité qui monte sur tout plaidoyer produit un **effet principal de la rhétorique** sans interaction avec l'intention : le plan le révèle.
- La « confusion totale » n'arrive que si l'on lit g sur le seul bras saboteur. Le risque réel, plus étroit, est d'agréger sondes de densité et sondes directionnelles dans un même verdict. Sur ce point précis, la recommandation de séparer les deux est juste.

**C-6. AM-4 (paraphrase) n'est pas un angle mort.**
- La marge asymétrique H6 mesure précisément la chute du succès d'attaque **contre** la chute d'utilité honnête, sous paraphrase entre autres (F1 §5). Une paraphrase qui dégrade l'honnête est l'issue qui falsifie H6, pas un trou du programme.
- La version « l'honnête paraphrasé ressemble à du sabotage » suppose que le moniteur lit le texte paraphrasé. C ne précise pas lequel.

**C-7. Le blanchiment AR(1) de l'ajout 1 fuit, et le seuil du Duel 1 est mal calculé.**
- **Fuite.** Un filtre ajusté sur des épisodes honnêtes, puis évalué sur les mêmes, rend le taux de faux positifs blanchi optimiste par construction.
- **Seuil.** Pour n = 500 et p = 0,01, la borne supérieure à 95 % se situe vers 2 %, pas 2,5 % (approximation binomiale, à recalculer exactement).
- **Même faille que chez A.** Le contrôle par permutation des index (i, t) ne localise pas la dépendance (voir A-2).

**C-8. Attributions qui ne soutiennent pas la faille annoncée.**
- **F-D1.** Marks et Tegmark défendent l'existence d'une structure linéaire de la vérité. Les échecs sur la négation relèvent d'autres travaux (référence à vérifier). C cite la mauvaise source pour sa thèse.
- **F-D2.** Meinke et al. (lu en page 1 seulement par F2) traite de manigance en contexte. Ce n'est pas une source documentant que l'imitation d'erreurs humaines échappe aux sondes de tromperie. Ce que C présente comme une « faille documentée » est une hypothèse.
- **F-E1.** SAD décompose la conscience situationnelle, mais ne documente pas que l'inférence par la nature de la tâche survit au retrait des marqueurs.
- **Lecture de F2.** C écrit que F2 se borne à retirer les marqueurs. Or la proposition 3 de F2, acceptée en F3, inclut une mesure du réalisme de l'environnement (a) (E6, du type LURE).

### (b) Hypothèses supposées sans test, avec la mesure

1. **(c)4 : la contrôlabilité et le sabotage se disputent une même capacité.**
   - C veut ne mesurer la contrôlabilité que conjointement avec le dommage. Si l'hypothèse est fausse, cette mesure jointe masque une contrôlabilité réelle, ce qui est le mauvais côté de l'erreur pour un audit défensif.
   - H_A : la détection sous condition « suppression consignée » est la même avec ou sans tâche de sabotage concurrente.
   - H_B : elle remonte avec la tâche concurrente.
   - Mesure : condition publiée reprise telle quelle, isolée puis dans l'environnement (a), avec le dommage aval rapporté séparément. Une égalité falsifie H_B ; une remontée falsifie H_A.

2. **(c)2 : les saboteurs modulent spontanément leur conduite entre « observé » et « non observé ».**
   - La validation par transfert inter-environnements n'est définie que si cette modulation existe.
   - De plus, le régime « observé » de F1 §7 passe par une consigne textuelle : une sonde peut prédire la modulation en lisant cette consigne, ce qui retombe dans la fuite que C dénonce.
   - Mesure préalable : écart comportemental entre régimes ; s'il est nul, le test est indéfini et ne doit pas être lu.

3. **(c)3 : une direction prise dans le sous-espace principal et appariée en divergence KL est neutre.**
   - Les axes principaux de covariance d'une tâche portent souvent de l'information pertinente pour la tâche.
   - H_A : à KL égale, la direction témoin laisse l'utilité honnête intacte.
   - H_B : elle la dégrade autant que la direction visée.
   - Mesure : utilité honnête et taux de sabotage, chacun en fonction de la dose, pour les deux directions. A propose le même appariement par l'utilité ; je retiens l'utilité, plus proche de la variable confondante.

4. **Ajout 4 : l'injection de bruit discrimine la famille (iii) d'un modèle réellement plus faible.**
   - Le bruit d'activations est aussi une intervention de H6. Lire le même geste comme révélateur de sous-rendement et comme intervention mêle deux effets (A le dit pour le ré-échantillonnage, S-A2 ; cela vaut ici).
   - H_A : sous bruit croissant, la performance de (iii) monte et celle du témoin 3B baisse.
   - H_B : les deux baissent.
   - Mesure : courbes performance(bruit), lues séparément de l'issue H6.

5. **Table des mesures minimales : le plancher « perplexité sous le modèle de base » est indépendant du juge.**
   - Le modèle de base est de même lignée que l'agent et que deux juges sur trois.
   - Mesure : plancher calculé aussi sous un modèle de base d'une autre lignée ; écart entre les deux planchers.

### (c) Contrôles négatifs dont l'absence serait fatale

- **HCC.**
  - Parité **comportementale** obligatoire : le taux de sabotage aval des épisodes HCC doit être égal à celui de l'honnête standard.
  - Contexte témoin de même longueur et de même saillance, sur un thème **sans rapport** avec le sabotage. Il sépare l'écho lexical du concept de consigne refusée.
- **(iv-b).**
  - Évaluation finale par un juge **tenu à part** de toute récompense : autre lignée, ou vérification exécutable.
  - Test de sensibilité à l'observation (régime « observé » contre « non observé ») avant de lire δ. Sans conduite dissimulée mesurable, un rappel nul ne dit rien de l'intention.
- **Blanchiment.**
  - Ajustement sur un jeu honnête A, évaluation sur un jeu honnête B disjoint, avec les deux permutations décrites en A-2.
- **Mahalanobis.**
  - Lecture séparée de l'effet principal de la rhétorique et de l'interaction rhétorique × intention, par famille de sondes. Sans elle, un g < 0 artificiel n'est pas détectable.

---

**Ce qui est réfutable dans cette cellule.**
- A-3 est faux si la convention des organismes (iii) fait de l'absence de mot de passe l'état dormant.
- C-2 est faux si mon comptage de la table d de F2 est erroné.
- C-4 tombe si l'évaluateur de la rubrique et le juge boîte noire sont de lignées disjointes.
- C-5 tombe si EC.2 ne prévoit pas de lire l'interaction.

FIN-DE-CELLULE