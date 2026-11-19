
## 2. Ce que je n'ai pas changé, et pourquoi

- **Énoncés de HC1, HC2b et HC3** : mot pour mot ceux du brouillon 5 (N-005, N-013, N-023). N-068 (section 7) dit
  qu'ils ne changent pas. Seules des sources s'y ajoutent.
- **Prédictions C-P1, C-P1b, C-P2, C-P5, C-P6 et leurs seuils** : inchangés, sauf la précision « intervalle bilatéral
  BCa » et la règle conjointe de C-P1. Les contre-indices publiés contre les prédictions 1 et 3 de HC1 sont dits, mais
  je n'ai changé aucune prédiction : c'est une modification d'hypothèse, donc un nœud (décision D-13).
- **Marge d'équivalence de HC2, [−0,10 ; 0,10]** : inchangée. N-068 dit la prédiction « inchangée dans son signe » et
  « à chiffrer au préenregistrement » ; je n'ai aucune pièce qui commande une autre marge.
- **Pilote, addendum de dérivation, vivier, familles, juges, consignes, gardes, graines existantes, effectifs {60, 90,
  120}, banc de reproduction** : inchangés. Aucune décision postérieure au brouillon 5 n'y touche, hors les points
  listés à la section 1.
- **Chiffres du projet précédent et empreintes sous `donnees/`** : repris du brouillon 5 sans recalcul ; le mandat
  m'interdit d'ouvrir `donnees/`. C'est dit dans le texte.
- **Marqueurs `<<…>>` gardés**, tous légitimes au scellement seulement : `<<COMMIT_ANALYSE>>`, `<<NOMBRE_TESTS>>`,
  `<<LIGNES_MODULE_PAPIER_C>>`, `<<EMPREINTE_CONFIG>>`, `<<ENTROPIE>>`, `<<REVISION_LLAMA>>`, `<<REVISION_QWEN>>`,
  `<<REVISION_MISTRAL>>`, `<<EMPREINTE_TACHES_SOURCE_64>>`, `<<CHEMIN_PROPOSITIONS_PILOTE_T05>>`,
  `<<EMPREINTE_PROPOSITIONS_PILOTE_T05>>`, `<<CHEMIN_NOTE_VIVIER>>`, `<<EMPREINTE_MESURES_V2>>` (treize).
- **Marqueurs retirés** : `<<DECISION_STABILITE_RANG>>`, `<<DECISION_BRAS_USURPATION>>` (tranchés par défaut, R-326) ;
  `<<DECISION_VOISINS>>` (converti : verrou 2 et décision D-12) ; les six marqueurs des contre-lectures 5 et 6 (elles
  ont eu lieu en session 16).
- **Organisme d'idéation (N-064, N-065, N-067, N-071, N-073)** : rien n'entre au texte, sauf la phrase de périmètre.
  Le texte ne présente pas l'organisme ; les citations obligatoires de ces décisions valent pour les textes qui le
  présentent (décision D-10).
- **N-066** (garde adaptée de T0.7) : sans objet pour ce texte.
- **HC4, HC5, HC6** : hors du critère 7 et du texte. La restriction de la lettre de N-013 pour HC4 (N-068, section 8) et
  les contre-indices de 2611.04556 sur HC4 et HC6 (R-2554) sont renvoyés aux préenregistrements de TC.4 à TC.6.
- **Propositions du rapport C9, § 6, pour HC1** (tirer la cible indépendamment de v₀ ; bras de reconsidération
  neutre) : non appliquées. Ici v* est une constante de l'échelle, et le témoin de longueur appariée joue le rôle du
  bras neutre. Je le signale dans D-13 plutôt que de changer le plan.

## 3. Ce que j'ai repris des brouillons 6 et 7 de l'archive, et ce que j'ai laissé

Matière première : `papier-C/brouillon6/…-brouillon6.md` (`fadc74c3…`) et `papier-C/brouillon7/…-brouillon7.md`
(`541f1511…`), dans l'archive `registres/passations/bloc-notes-session16-complement-2026-10-21.tar.gz` (`0c15862c…`) ;
tables de traitement `74b5ae16…` et `351ab375…` ; rapports de contre-lecture `0c492f02…` (méthode, brouillon 5) et
`45a0d875…` (vérification courte, brouillon 6). J'ai comparé le corps du brouillon 5 à celui du brouillon 7 par
programme (63 blocs de différences) et jugé chaque bloc.

**Repris, parce que commandé par une décision en vigueur.**
- Stabilité de rang selon P-021, option (A) (défaut appliqué, R-326). Les versions de repli (B) et (C) sont retirées.
- Bras « usurpation écrite par l'agent » inclus (P-020, R-326). La version de repli est retirée.
- Condition « constat nu » (P-022, option (b), R-326), avec sa réserve 16 et la correction de la réserve 9.
- Clause d'ouverture et réserve 14 (décisions de Lazar R-307 et R-309).
- Réserve 17 (personne grammaticale ; décision de routine de la session 16, R-316).

**Repris, parce que je les juge fondés** (chaque motif est à la ligne du changement, section 1).
- Identification du calibrage, lecture sans calibrage, règle conjointe de C-P1, réserve 15 (CL5-methode-01).
- C-P4b lu sur l'excédent du paragraphe (CL5-methode-04). L'alarme définie quand p̂ vaut 0 ou 1 (CL5-methode-05).
- Lectures restées sur la loi brute, ramenées à la loi nette ou dites brutes (CL5-methode-06).
- Préséance entre décompte et intervalles (07) ; tests du module précisés (08) ; réserve d'intention par intervalle
  (09) ; ordre d'appariement des témoins (11) ; « intervalle bilatéral BCa » (12) ; unité d'indépendance au pilote (14).
- Constats de la lentille « texte » : statistiques lues sur la loi nette (texte-05) ; exception de C-P4b (06) ;
  validation croisée par tâches (07) ; tirage uniforme sans strate (08) ; empreinte de la procédure d'extraction (10),
  recalculée par moi ; jackknife sur les grappes (11).
- La troisième lecture des statistiques de rang (calibrage par ρ̂/r̂ ; CB6-methode-courte-01) et la clause de repli
  mécanique (02). La troisième lecture dépasse la lettre de P-021 au registre : décision D-9.
- La garde « aucun jeton spécial de gabarit de conversation » (CQ-04), sans les chiffres des articles qui la motivent.

**Laissé.**
- **Tous les précédents et contre-indices tirés des notes de voisins de la session 16** (Joswin et al., Hu et Qu,
  Hussain et Nielbo, Kumaran et al., Barkett, Zhu et al., Weng et al., Wang K. et al., Wang Q. et al., Choi et al.,
  Geng et al., Chang et al., Jiang et al., Zeng, Chen et al., Vennemeyer et al., Germani et Spitale). Ces notes et la
  plupart de leurs PDF ne sont pas au dépôt (j'ai vérifié l'absence de `docs/sources/pdf/2607.05545v1.pdf`). La
  consigne interdit un chiffre de l'état de l'art qui ne figure pas dans une pièce vérifiée du dépôt (R7). Cela
  représente environ 150 lignes du brouillon 7. C'est un manque réel pour l'audit de symétrie : plusieurs de ces
  contre-indices sont défavorables au programme. Décision D-11.
- Le verrou 2 détaillé du brouillon 7 (une ligne par note) : remplacé par un verrou court qui dit où sont les notes.
- La citation de Hu et Qu dans la réserve 16 et celle de Wang K. et al. dans la réserve 17 : les deux réserves sont
  écrites sur les seuls faits de la configuration.
- Les indices des formulations qui portent le constat (réserve 16) : je ne les ai pas recomptés ; renvoyés au script de
  la configuration.
- La configuration brouillon 4 de l'archive (`6734fbd0…`) : non reprise, non relue ; je n'écris aucune configuration
  (verrou 4).
- Les marqueurs `<<TRANCHER_P020>>`, `<<TRANCHER_P021>>`, `<<TRANCHER_P022>>`, `<<DECISION_CONSTAT_NU>>`,
  `<<LIGNE_CORRECTION_P021>>` et les entrées de contre-lecture 7 à 10 de l'archive : sans objet, les trois propositions
  ont pris leur défaut le 24 octobre.
- Les versions de repli des trois propositions.
- La phrase « six lignes neutres… » du point 10 et les grilles publiées ajoutées à « Familles et échafaudage ».
