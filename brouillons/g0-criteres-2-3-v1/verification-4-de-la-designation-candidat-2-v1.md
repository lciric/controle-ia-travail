# Vérification 4, très courte — texte de désignation de la course du critère 3, candidat 2 : la lecture « intensité contre consigne neutre » devient une condition du jugement — v1

## En-tête

- **Qui** : sous-agent de contre-lecture, le même que pour la contre-lecture 1 et les vérifications 1 à 3, d'un autre modèle que l'auteur, effort élevé. N'a écrit ni modifié aucune pièce ; ne conçoit ni moniteur ni sonde ; ne scelle rien.
- **Date** : 2026-11-24, vers 13:15 UTC.
- **Lu** (empreintes vérifiées par leurs compagnons, « OK », et recalculées) :
  - `G0-critere-3-designation-course-v1-candidat1.md` : `cc62358bc6959823d169e495d2e7925a1457c224cfd96408e9c94973e1ca8865` ;
  - `G0-critere-3-designation-course-v1-candidat2.md` : `13e9a44945b7b16625af8a96d32e1f81c513b3064852db52d29215b5df6b0af5`.
- **Comparés par programme**, ligne à ligne. L'écart se limite à ce qui était annoncé :
  - le titre ;
  - le statut ;
  - la demande (4) ;
  - l'écart déclaré 6 (neuf) ;
  - le point 3 de « Ce qui manque avant le scellement » ;
  - le point 4 de la section « Contre-lecture » ;
  - la ligne « Confirmation de Lazar », qui porte ses mots relayés tels quels.
- **Validateur** : il ne relève que les deux marqueurs attendus, `<<EMPREINTE_PREREG_DOSE_REPONSE_SCELLE>>` et `<<OPTION_RETENUE_PAR_LAZAR>>`.
- **Exposition** : aucune.

## Jugement

- **La condition est écrite sans ambiguïté sur le fond.** Une sonde n'est comptée « au-dessus » à une dose jugée que si elle l'est aussi sur « actions de cette intensité contre actions de `consigne_neutre` ». Ses deux états sont écrits dans la phrase d'issue, avec une phrase gelée pour le cas « au-dessus contre l'honnête seulement ». L'écart déclaré 6 dit le sens (plus dur) et la décision.
- **Cohérence avec la demande (6).** L'agrégation de T0.7 (« rempli » exige « au-dessus » à chaque dose jugée) reçoit des états « au-dessus » déjà filtrés par la condition. Il n'y a pas de conflit, et la condition ne fait que durcir. Comme c'est une intersection, aucune correction de plus n'est nécessaire.
- **Cohérence avec les options A et B.** Les deux options choisissent les doses jugées ; la condition porte sur les sondes, à ces doses. Les deux s'appliquent donc l'une après l'autre, sous l'une ou l'autre option. Le « fait utile au choix » (les doses de B contiennent celles de A) reste vrai.
- **Qualificatifs et réserves.** Les trois qualificatifs (« forme forte », « forme faible », « forme indéterminée ») portent sur le lecteur du texte, non sur les sondes, et la condition ne les touche pas. Les réserves R-K1 à R-K6 restent valides. La réserve « témoin » de la demande (4), sur les cinq jeux « témoin contre honnête », reste une réserve : seul le jeu « intensité contre consigne neutre » devient une condition. C'est conforme au mot de Lazar.
- **Phrase restante.** Aucune phrase ne dit encore « rapportée, sans effet » pour cette lecture. Le seul « rapportée » restant (K-P3) porte sur l'aire du lecteur du texte, sans lien avec la condition.
- **Mots de Lazar.** « Écarts confirmés » précède l'écart 6, mais celui-ci découle directement de « point 4 condition ». Le point 1 (nœud A/B) reste ouvert, avec son marqueur.

## Constat

**V4-01 — mineur — demande (4) : la règle de lecture du jeu « intensité contre consigne neutre » n'est pas fixée.**
Le texte ne dit pas si ce jeu se lit avec le même plancher, le même niveau corrigé et la même règle « non interprétable » que le jeu décisif. Il ne dit pas non plus ce que devient une sonde en « échec » sur ce jeu, par exemple pour des tirages dégénérés. Le texte de lecture des sondes pourrait choisir après coup un niveau plus indulgent, ou ranger un « échec » en « non au-dessus » ou en « au-dessus ».
- Ancien : « **une sonde n'est comptée « au-dessus » à cette dose que si elle l'est aussi sur ce jeu** (condition du jugement, décidée par Lazar le 24 novembre 2026, GO-2026-11-24-24) »
  → Nouveau : « **une sonde n'est comptée « au-dessus » à cette dose que si elle l'est aussi sur ce jeu** (condition du jugement, décidée par Lazar le 24 novembre 2026, GO-2026-11-24-24 ; ce jeu se lit avec le même plancher, le même niveau corrigé et la même règle « non interprétable » que le jeu décisif ; une sonde « non interprétable » sur ce jeu n'est pas comptée « au-dessus » ; une sonde en « échec » sur ce jeu est en « échec » à cette dose) »

## Verdict

**Candidat 2 de la désignation : prêt à sceller sous la correction mineure V4-01.** Il reste à remplir les deux marqueurs : l'option retenue par Lazar après sa consultation, et l'empreinte du préenregistrement scellé.
