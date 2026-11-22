# Relance — pièce 2 : état repris du travail du monteur précédent, cycle 1 du scellement 2 — v1

- Classe C. Écrite le 2026-11-22 vers 14:55 UTC par le monteur de l'oracle du cycle 1, relance
  (`session_01XJ6MgmSDBZpPAuXLe3diix` ; attestation : `relance-piece-1-attestation-monteur-relance-v1.md`, `fa502c4d…`).
- Mandat v3, section 4, point 2. **Sans contenu de famille ni d'oracle** : cette pièce peut aller à la mère telle
  quelle. Les motifs de fond sont au coffre, dans les pièces que chaque ligne cite.
- Travail repris : dossier `donnees/bras-attaque-oracle-scellement-2-cycle-1-v1/`, tête `c05c604df3794528…` de cette
  branche ; monteur précédent `session_01Qi7Gr4BDyW322Ljw2o29ZT` (R-4638), injoignable (R-4779). Les 19 sceaux
  compagnons du dossier vérifiés conformes à 14:40 UTC ; rien n'est réécrit ni supprimé (R12).
- Tests du code repris, lancés à 14:46 UTC (`PYTHONPATH=src python -m pytest -q
  donnees/bras-attaque-oracle-scellement-2-cycle-1-v1`) : **46 réussis sur 46**. Le module de l'environnement du banc
  (`src/controle_ia/environnements/propositions.py`, `5d97b223…`) et les deux fichiers de tâches (`8d20a698…`,
  `76cdeace…`) sont identiques sur cette branche et sur `main` (`1af1bb22`).
- Trois mots : **accepté** (rien à refaire) ; **à reprendre** (à refaire ou à compléter avant usage, motif dit) ;
  **nœud ouvert** (attend une décision, qui est dite). Aucune des pièces A et B du prédécesseur n'a été contre-lue :
  c'est la première raison de « à reprendre » pour chacune.

## 1. Pièces

| n° | pièce | empreinte | état | motif |
|---|---|---|---|---|
| 1 | `piece-1-attestation-monteur-cycle-1-v1.md` | `c5f000943140b75b…` | accepté | attestation de sa session ; la mienne s'y ajoute (relance, pièce 1) |
| 2 | `piece-2-oracle-monte-famille-1-v1.md` | `758e404a4327f5a3…` | à reprendre | (a) jamais contre-lue (classe A pour ses sections 3 à 5) ; (b) ses réglages d'appel ne tiennent pas la règle permanente des appels aux modèles de Google (`CLAUDE.md` sur `main`, GO-2026-11-21-71) si un lecteur de Google est retenu ; (c) l'erratum promis sur les lecteurs n'a jamais été écrit ; (d) la forme de ses paramètres ne se ramène pas à la règle des questions fermées de la pièce de sécurité v16 et du brouillon 17 de la course : nœud n° 4 ci-dessous |
| 3 | `oracle_famille_1_v1.py` | `43c4c8f1de288781…` | à reprendre | tests réussis ; jamais contre-lu (classe B) ; suit la pièce 2 sur les points (b) et (d) |
| 4 | `controle_agent_p1_v1.py` | `42a2a0437473546f…` | à reprendre | contre-lecture de classe B seule ; aucun défaut vu ; non exécuté (épreuve, attend son tour) |
| 5 | `test_oracle_famille_1_v1.py` | `216c2f3213ce5044…` | à reprendre | contre-lecture de classe B seule ; 46 sur 46 |
| 6 | `piece-3-plan-des-epreuves-oracle-famille-1-v1.md` | `10e1f85ac7802623…` | à reprendre | jamais contre-lu (classe A) ; dépend des nœuds n° 4 et n° 11 ; ses épreuves doivent passer avec les lecteurs, versions et réglages exacts du champ n° 18 (condition 12 de la pièce de sécurité) |
| 7 | `piece-4-repli-oracle-famille-1-v1.md` | `7583d5ff11668be5…` | à reprendre | jamais contre-lu (classe A) ; un cas à y ajouter par renvoi : la règle des questions non tenue, « rien ne part » (liste d'arrêt de la course) |
| 8 | `piece-5-esquisse-de-devis-epreuves-oracle-v1.md` | `c46daeae33d116be…` | accepté | esquisse sans prix, comme elle le dit ; le devis chiffré reste à faire, après le nœud n° 1 |
| 9 | `message-mere-proposition-lecteurs-v1.md` | `162738588e5c8436…` | accepté | remplacée par la v2, gardée |
| 10 | `message-mere-proposition-lecteurs-v2.md` | `ffc82cb9362d6879…` | nœud ouvert | nœud n° 1 |
| 11 | `constat-lecture-humaine-et-conservation-fournisseurs-v1.md` et `sources-conditions-fournisseurs-v1/` (5 pages) | `f892fc6caaeb98e0…` | accepté | sources versées, sceaux conformes ; lues le 2026-11-21 : à relire au devis. Sa conclusion est le nœud n° 2 |
| 12 | `message-mere-oracle-mode-connu-faisabilite-v1.md` | `bfb639a108b401ef…` | accepté | point de départ du champ R-5 (relance, pièce 5) |
| 13 | `message-mere-forme-des-questions-v12-v1.md` | `fd3dbb42bf2b90e4…` | nœud ouvert | ses quatre nœuds n'ont reçu aucun mot trouvé au registre ; les points 1 et 2 sont repris au nœud n° 4, les points 3 et 4 au nœud n° 11 |
| 14 | `message-mere-attestations-voie-envoi-v13-v1.md` | `6a8234f420dbe1b3…` | nœud ouvert | attestation 2 (un programme compare, aucun modèle) : acceptée, conforme à la course (section D6). Attestation 1 : son nœud reste ouvert, repris au nœud n° 4 |
| 15 | `journal-acces-v1.md` | `c67877f58af0619d…` | accepté | trouvé **non scellé** (aucun compagnon ; « scellé à la fin », la fin n'a pas eu lieu) ; dernière ligne à 19:20 UTC le 21 ; empreinte relevée ici, fichier laissé tel quel dans le commit `c05c604d`. Mon journal est neuf : `journal-acces-relance-v1.md` |

## 2. Nœuds

Recherche faite à 14:45–14:47 UTC dans `registres/go.md` et `registres/decisions.md` de `main` (`1af1bb22`), par
mots, hors lignes R-604 à R-610 : aucun mot de Lazar trouvé sur les nœuds n° 1 à 4 et 8 à 11.

| n° | nœud | à qui | état |
|---|---|---|---|
| 1 | Choix des deux lecteurs du dommage (proposition v2 du prédécesseur, non confirmée) ; modèle exact et version datée de chacun | la mère, puis le champ n° 18 | nœud ouvert ; voir la relance, pièce 3 |
| 2 | Lecture humaine possible chez les fournisseurs des deux lecteurs proposés (« oui » pour les deux) : selon la règle de la pièce de sécurité (R-4674), ces lecteurs ne lisent pas, ou Lazar dit en toutes lettres que l'envoi est alors un partage ; sans défaut à 48 heures | Lazar | nœud ouvert |
| 3 | Critère d'une précondition de l'oracle qui peut échouer sans faute de l'oracle (signalement 2 du prédécesseur, pièce 2, section 6 ; remarque 2 de la vérification de la famille) : changement de critère par une version nouvelle de la spécification | l'auteur de la famille, par la voie prévue ; contre-lecture | nœud ouvert |
| 4 | **Règle des questions fermées** (pièce de sécurité v16, section 3.5 ; course, brouillon 17, section D6 et liste d'arrêt) : l'oracle de la famille, tel que sa spécification le fixe, ne permet ni l'attestation de provenance « au caractère près, toutes, dans l'ordre », ni l'attestation « paramètres tirés ni de la pièce 2 ni de la pièce 3 ». Selon la course : rien ne part ; nœud pour Lazar | Lazar | nœud ouvert ; motifs, options et recommandation au coffre : `relance-noeud-regle-des-questions-v1.md` |
| 5 | Onze précisions du monteur (pièce 2, section 3) et deux de la pièce 4 (seuil de refus, relance unique) | la contre-lecture | à reprendre (rien n'a été contre-lu) |
| 6 | Oracle du mode connu de la répétition générale : mandat, écart « Qui conçoit », réserve de cloisonnement, spécification de « altéré » et « conforme » | la mère, Lazar | voir la relance, pièce 5 (champ R-5) |
| 7 | Réserve écrite du prédécesseur : si l'observateur de la base (iv), le juge robustifié de la proposition P-003, le juge ouvert de grande taille ou la lecture de plus grande taille de N-053 reçoit la famille d'un lecteur retenu, ce lecteur ne lit pas et l'oracle se remonte | la mère (familles de ces quatre sièges) | nœud ouvert ; même condition dans la vérification de l'audit des lignées (`8718c80b…`, « Liste finale ») |
| 8 | Précondition « l'agent ne voit pas la référence ; aucun moniteur ne la lit », moitié côté moniteurs : une main qui peut lire les moniteurs, désignée par la mère, reçoit la seule question écrite à la pièce 3 du prédécesseur, section 6 | la mère | nœud ouvert |
| 9 | Hérité de la famille : l'auteur de la famille a écrit la vérité du dommage de son propre mode, écart à N-060 v3 point 4 ; nœud à Lazar avant toute exécution de l'oracle (vérification de la famille, section 4 ; vérification de l'audit des lignées, écart 6) | Lazar | nœud ouvert |
| 10 | Agent de l'ancre et main auxiliaire des épreuves (pièce 2 du prédécesseur, section 4.2) : famille proposée dont la lecture humaine est « non établi » | la mère, puis Lazar | nœud ouvert |
| 11 | **Envois des épreuves** : les épreuves de l'oracle envoient aux lecteurs externes des plans honnêtes et des plans altérés par programme, dont la dose flagrante construite par une autre main et gardée au coffre. La pièce de sécurité v16 (condition 9 : « Rien d'autre ne suit cette voie ») ne couvre que les produits de la course. Sous quelle règle partent ces envois ? Ma lecture : la voie de la section 3.5 ne les couvre pas ; c'est une extension, donc un nœud et une version nouvelle de la pièce de sécurité, ou une règle propre aux épreuves | la mère, puis Lazar | nœud ouvert, neuf |
| 12 | Ce que j'ajoute : le lieu d'où part l'envoi change de session | la mère (remplacement exact dans la course) | voir la relance, pièce 6 |
