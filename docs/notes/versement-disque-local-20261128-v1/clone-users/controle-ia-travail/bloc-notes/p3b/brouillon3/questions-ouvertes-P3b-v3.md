# Questions ouvertes de P3b, brouillon 2 — v2

Rédacteur neuf du brouillon 3 (Claude, sous-agent), session 16, 2026-10-21 vers 01:32 UTC (heure vraie). Remplace pour
la suite la v2 (`…/p3b/brouillon2/questions-ouvertes-P3b-v2.md`,
`417a111e688fd412db4fb49675b54254d874ae392f08f3c3725a0a0494764757`, écrite vers 00:54 UTC le 2026-10-21), gardée telle
quelle (R12), qui remplaçait la v1 (`…/p3b/brouillon1/questions-ouvertes-P3b-v1.md`, `046991ab…`). Ajouts du brouillon 3
marqués « (brouillon 3) », d'après les contre-lectures R2 du brouillon 2 et leur traitement
(`…/p3b/traitement-contre-lectures-brouillon2-P3b-v1.md`, `958b4601…`). Pour chaque question : son état (tranchée, par quel constat ou
quelle décision ; nœud ; proposition), puis ce qui reste. « Nœud » : décision de Lazar, sans défaut ; « proposition » :
proposer avec recommandation, défaut sous 48 heures ; « routine » : la session tranche et consigne. Renvois :
`P3b-seconde-lecture-v1-brouillon3.md` (texte), `devis-P3b-v3.md`, `plan-code-et-chaine-P3b-v3.md`. Traitement :
`…/p3b/traitement-contre-lectures-brouillon1-P3b-v1.md` (`d31c87b1…`), qui adopte le projet `82a90e81…`.

- **Q-01 (nœud N-031, en attente)** Statut de P3b. Options : (a) diagnostic, sans revendication, R-262 (point 2) reste à
  faire ; (b) première tentative de détection, déclarée non aveugle ; (c) mixte. Recommandation (a), confiance ≈ 65 %. Aucun
  défaut : sans réponse, le texte ne se scelle pas. Le texte écrit (a), avec (b) et (c) à côté (CR-P3b-texte-01). (brouillon 3) Replis (b) et (c) complétés : écart (iv),
  réserve « tentative non aveugle », troisième ligne de la synthèse (CR2-P3b-texte-06).
- **Q-02 (proposition P-016, en attente)** Partition : défaut (A) 20/40 le 2026-10-22 vers 21:15 UTC ; (B) 20/20/20 et (C)
  écrites en repli ; `<<PARTITION_P016>>` se remplit au candidat par le seul texte retenu (CR-P3b-texte-15).
- **Q-03 (nœud N-032, en attente)** Compte M-P3b-2. Options : (A) avant le scellement, par condition ; (B) avant le
  scellement, un seul compte, toutes conditions confondues ; (C) après le scellement, contrôle avant dépense sur
  processeur, par condition, règle de P3b-P0 gelée. Recommandation (C), confiance ≈ 70 %. Sans réponse, rien n'est compté
  avant le scellement (revient à (C)). Le texte, le devis et le plan écrivent (C), avec (A) et (B) à côté
  (CR-P3b-texte-08, CR-P3b-methode-03). (brouillon 3) Les trois versions sont limitées aux tâches lues ; la liste d'arrêt
  et l'ordre de la chaîne portent les versions (A) et (B) en mots exacts (CR2-P3b-texte-07).
- **Q-04 (proposition P-023, en attente)** Position principale des sondes génériques : W, t_cost seul en descriptif.
  Classée « proposer avec recommandation » (CR-P3b-texte-14) ; défaut (A) le 2026-10-23 vers 00:30 UTC ; confiance ≈ 60 %.
- **Q-05 (proposition P-023, en attente)** Bras principaux sur tous les pas, premier pas en descriptif et en réserve VS-01 ;
  double comptabilité au premier pas. Même choix dans les trois options de P-023 ; confiance ≈ 55 %.
- **Q-06 (proposition P-023, en attente)** Négatifs de l'oracle : honnête et témoin (P3-P4 de l'oracle rapportée seulement)
  en (A) et (C) ; honnête seul (P3-P4 testée) en (B). Confiance ≈ 65 %. La session a déclaré que le signe de P3-P2 lui est
  accessible ; le choix du brouillon 1 a été fait à l'aveugle ; les rédacteurs des brouillons 2 et 3 ne connaissent pas ce signe.
- **Q-07 (proposition P-023, en attente)** Positifs de l'oracle : toutes les actions du saboteur à coût lisible en (A)
  (recommandée, CR-P3b-methode-12 : T1 reste un test) ; actions étiquetées 1 par T1 en (B) et (C). Confiance ≈ 60 %.
- **Q-08 (routine, dans P-023)** Estimateur de l'oracle : ridge à noyau linéaire par bandes, système écrit
  (CR-P3b-methode-13 (c)). C'est l'écart (ii) à la proposition 010 ; en (B), sonde linéaire et différence de moyennes aux
  couches 7, 15 et 23 (voir Q-26).
- **Q-09 (routine, ouverte)** Reconstitution : reprendre par import celle du module v3 de P4, s'il en a une pour les
  épisodes de P3, après vérification de son code et de ses tests, citée par chemin et empreinte et versée au dépôt (avis de
  la contre-lecture « texte ») ; sinon module neuf du plan. Le critère d'épisode, la propagation et le contrôle négatif de
  P3b s'appliquent dans les deux cas.
- **Q-10 (routine, ouverte)** Fichiers d'entrée de P3 sur l'instance : lus sur la branche `calcul/p3-reel-v1` à leurs
  empreintes, aucune copie de plus des textes d'action — recommandation inchangée (accord de la contre-lecture « texte »).
- **Q-11 (tranchée, routine)** Suite des tests sur l'instance : **complète**, comme P3 (traitement, section 2 ; ≈ 0,45 h,
  dans le devis).
- **Q-12 (routine, ouverte)** Durées du devis non mesurées, dont les postes neufs (items (v) et (vi), contrôle négatif) : les recaler
  par la répétition jouet chronométrée et par la durée `passe_unique_s` consignée par P3 (lue par la session), avant le
  candidat.
- **Q-13 (tranchée en partie)** Tolérances : 10⁻³ en valeur relative gardée ; elle n'est pas relâchée par la tolérance
  d'équivalence de P3 sans contrôle négatif (avis de la lentille « méthode », retenu par le traitement) ; le contrôle négatif
  de la tolérance est écrit (CR-P3b-methode-03). Valeurs écrites au texte (10 %, 5 points par paire, identité de la lentille
  à 99 % et écart médian 0,05) ; tout changement avant le scellement s'écrit avec son motif ; jamais après. (brouillon 3)
  Garde d'identité comparée à des logits gardés au jeton t_cost, dans la précision du modèle (CR2-P3b-methode-10).
- **Q-14 (tranchée, brouillon 3, CR2-P3b-methode-10)** Convention d'indice des couches : indices du harnais comptés depuis
  0 (`harnais/activations.py` l. 3-4, lu par la contre-lecture « méthode » du brouillon 2), comme les couches 7, 15 et 23
  de P3 ; bandes : sorties de bloc 0 à 6, 7 à 19, 20 à 31 ; règle écrite au texte, non fixée par un test.
- **Q-15 (proposition P-023, en attente)** Bandes : sorties de bloc 0-6, 7-19, 20-31 (indices du harnais depuis 0, CR2-P3b-methode-10) ; confiance ≈ 55 %. En (B), l'oracle lit les couches 7,
  15 et 23 ; les bandes restent pour la double comptabilité.
- **Q-16 (tranchée)** Valeur honnête de référence : médiane honnête de la tâche ; pour une action de l'honnête, médiane des
  autres actions de l'honnête de la tâche (CR-P3b-methode-16 (b)) ; « coût écrit divisé par 3 » en descriptif
  (CR-P3b-texte-22 (a)).
- **Q-17 (tranchée en partie)** Leurre : tiré une fois par tâche, parmi les tâches lues, même règle de grandeur
  (CR-P3b-methode-16 (a), CR-P3b-methode-09) ; H_t et leurre au plus 999 (CR-P3b-methode-16 (c)). Reste : minimum de
  20 actions par condition au premier pas, à juger par la mesure de puissance M-P3b-1 (CR-P3b-methode-08). (brouillon 3) Avis de la contre-lecture « méthode » du
  brouillon 2 : à garder ; la borne des deux côtés de D3 est atteignable dès 40 tâches quand la préférence est forte,
  fragile à 25 (essai sur données inventées) ; une strate d'amorçage sous 20 actions se lit comme une strate où D3 ne tient
  pas (CR2-P3b-methode-03).
- **Q-18 (routine, avec réseau, ouverte)** Lentille jacobienne pré-ajustée : fichier, format, licence et empreinte, et
  source par chemin du dépôt, empreinte et page (R7, CR-P3b-texte-20), à établir par la session avant le candidat ; licence
  restrictive : nœud ; sinon bras retiré ; réajustement hors devis.
- **Q-19 (tranchée en partie)** Contrôle positif de la lentille : items numériques de copie en principal, plus les items
  (v) « motif de transformation », qui éprouvent le motif lu par D3 (CR-P3b-methode-06) ; (brouillon 3) et les items (vi) « valeur calculée absente
  du contexte », qui éprouvent la branche stricte de D3 (CR2-P3b-methode-04). Reste : paradigme de [JL] en
  descriptif s'il ne coûte rien de plus (non écrit dans le texte ; R7 exigerait le PDF et la page).
- **Q-20 (tranchée, routine)** Multiplicité : famille des deux sondes génériques à 97,5 % (reprise de P3) ; oracle à 95 %,
  hors de la famille (hypothèse distincte) ; le reste à 95 % sans correction, déclaré (CR-P3b-methode-11, conflit C-1 ;
  VV5-sens-09). Confiance du traitement ≈ 60 %.
- **Q-21 (proposition P-024, en attente)** États à t_cost : (A) détruits avec l'instance après une récupération conforme
  (recommandée, confiance ≈ 60 %) ; (B) instance gardée arrêtée jusqu'au verdict R13, 72 heures au plus, borne 8,6 USD ;
  (C) versés au dépôt privé. Défaut (A) le 2026-10-23 vers 00:30 UTC. La garde après un refus de poussée reste bornée à
  24 heures (CR-P3b-texte-10). (brouillon 3) En (B), crédit exigé + 2,16 USD au texte ; en (C), fichier poussé en morceaux
  de 90 Mo au plus, exception écrite à l'étape 2.6, à la liste d'arrêt et au contrôle des fichiers (CR2-P3b-texte-08).
- **Q-22 (tranchée)** P4 : lignes G2a et G2b dans la table gelée, appliquées au moment de la lecture (CR-P3b-texte-05 ;
  brouillon 3, CR2-P3b-texte-09) : G2a lit la forme exacte de la ligne d'issue de la table gelée du préenregistrement
  scellé de P4-instrument, cherchée dans le verdict de P4 scellé au moment de la lecture ; G2b s'applique si aucun verdict
  de P4 n'est scellé à ce moment. Reste : `<<LIGNE_ISSUE_P4>>` au candidat (chemin, empreinte, forme exacte).
- **Q-23 (routine)** Valeurs `<<…>>` lues par code par la session au candidat : commit, entropie (tirée une fois et
  consignée au registre avant tout usage), configuration, empreintes du run source, lentille jacobienne, puissance, tests
  attendus, et, ajoutés par le brouillon 2 : `<<SHA_MODULES_P3B>>`, `<<TESTS_P3B>>`, `<<SHA_MODELE_P3>>`,
  `<<PARTITION_P016>>`, `<<AIRES_MIN_DETECTABLES_P3B>>`, `<<ENTREES_M10_P3>>` (entrées de la formule M10, grandeurs de P3 lues
  par la session, jamais par un rédacteur). (brouillon 3) Ajoutés : `<<LIGNE_ISSUE_P4>>`, au lieu de `<<LIGNE_VERDICT_P4>>`
  (CR2-P3b-texte-09) ; `<<ISSUE_P016>>`, `<<ISSUE_P017>>` : « tranchée (X) par Lazar le … (registre, ligne) » ou « défaut
  (A) appliqué le … (registre, ligne) » (CR2-P3b-texte-03) ; `<<ISSUES_DECISIONS_P3B>>` : pour chaque décision, numéro,
  option retenue, réponse de Lazar ou défaut échu, date, ligne du registre (CR2-P3b-texte-04).
- **Q-24 (tranchée, routine ; dépend de P-016)** Base de lecture : en version (A), bras génériques et double comptabilité
  sur les 60 tâches, oracle sur la confirmation, bras génériques sur la confirmation seule en descriptif
  (CR-P3b-methode-09, conflit C-4) ; en version (B), 40 tâches.
- **Q-25 (proposition P-017, en attente ; neuve)** Périmètre au-delà de N-028 : la session recommande désormais (A) pour P3b,
  et (C′) dans un préenregistrement séparé si Lazar veut la question (R-312, confiance ≈ 55 %) ; défaut (A) le 2026-10-22
  vers 21:15 UTC. En (B) ou (C), une version nouvelle du texte est nécessaire (aucune règle de la sonde de valeur n'est
  écrite ici).
- **Q-26 (routine, neuve ; ne vaut que si P-023 retient (B))** La version de repli (B) de P-023 fixe des détails que le
  traitement ne donne pas : « sonde linéaire » lue comme ridge linéaire pondérée à une couche, « différence de moyennes »
  comme produit scalaire avec la différence des moyennes d'apprentissage, 18 réglages, ordre des ex aequo, lecture au
  jeton t_cost (option « jeton juste avant le nombre » de la proposition 010, l. 24). Choix du rédacteur du brouillon 2, sans lecture de
  la proposition 010 : à vérifier par la contre-lecture R2 contre la proposition, l. 24-25 et 154-157. (brouillon 3)
  Vérifiée par la contre-lecture « méthode » du brouillon 2 (CR2-P3b-methode-11, proposition l. 24 et 154-155) : conforme
  sur l'essentiel ; deux écarts déclarés dans la version (B) (jeton `:` ; un seul lecteur retenu) et T4 de P3 à tranches
  recalculées dans chaque tirage (A4 (a)) ; le texte dit que ces détails sont une lecture du rédacteur du brouillon 2, à
  confirmer par Lazar avec l'option (CR2-P3b-texte-05).
- **Q-27 (routine, neuve)** Chemin du module qui porte `heures_declarees` (CR-P3b-methode-17) : non cité par le traitement ;
  les rédacteurs des brouillons 2 et 3 ne l'ont pas cherché (consigne : seuls les fichiers nommés par le texte). À citer par chemin, ligne et empreinte
  au candidat.
- **Q-28 (routine, neuve)** Leurre tiré par tâche (CR-P3b-methode-16 (a)) et H_t de l'honnête calculé sans l'action
  (CR-P3b-methode-16 (b)) : ce brouillon tire le leurre sur la médiane de toutes les actions de l'honnête de la tâche, et
  exclut (en les comptant) les actions de l'honnête dont τ_h égale alors τ_d. Choix du rédacteur du brouillon 2 pour joindre les deux
  corrections ; à vérifier par la contre-lecture « méthode ». (brouillon 3) Approuvé (CR2-P3b-methode-11), avec le motif
  « référence vide » pour une action de l'honnête seule lisible de sa tâche (CR2-P3b-methode-05).
- **Q-29 (routine, neuve)** Ligne G2 gardée entre G2b et G3 (texte de CR-P3b-texte-05 : G2a et G2b insérées « avant G2 ») ;
  la fusion F-4 nomme seulement « G2a ou G2b » dans la synthèse : ce brouillon écrit « G2, G2a ou G2b ». À confirmer. (brouillon 3) Confirmé (CR2-P3b-methode-11) ; la synthèse écrit « les
  deux sondes génériques en G2, G2a ou G2b » et rappelle les bases de lecture (60 et 40 tâches ; repli (B) de P-016 : 40
  et 20).
