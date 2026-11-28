# Traitement de la vérification de la synthèse « comment détecter » — tour 2, v1

- **Correcteur neuf.** Je n'ai écrit ni la v1, ni la v2, ni les extractions, ni les vérifications, ni le traitement du
  tour 1. 2026-10-20, de 11:35 à 12:20 UTC environ. Dépôt lu seulement : lectures et `git show`, `git log`, aucune
  écriture. Non ouverts : `prereg/P3-consignes-v1.md`, textes d'action, clés. Aucune recherche web, aucun service payant,
  aucun contact, aucune commande Vast.ai.
- **Entrées** (compagnons égaux) : synthèse v2 `…/revue-detection/synthese-comment-detecter-v2.md` (`90ad38bf…`, non
  modifiée) ; rapports du tour précédent : fidélité `…/revue-detection/verification-v2-fidelite-v1.md` (`12a9fac2…`,
  VV2-fidelite-01 à 14, noté F-01 à F-14 ci-dessous) et sens `…/revue-detection/verification-v2-sens-v1.md`
  (`8ec6aa0e…`, VV2-sens-01 à 19, noté S-01 à S-19). Aussi : v1 (`a47f9141…`), vérification du tour 1 (`43986648…`),
  traitement du tour 1 (`c87ecdec…`). `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Sortie** : `…/revue-detection/synthese-comment-detecter-v3.md`, sha256
  `ec4239e9da0a6b8282ce0b685695fcb71b2777038fd18618b096797502ae6890` (compagnon écrit). Les numéros de ligne ci-dessous
  sont ceux de ce fichier.
- **Méthode.**
  1. Empreintes des 22 PDF (RO compris) recalculées : toutes égales ; texte de chaque page extrait à nouveau par
     `pdftotext` (modes défaut, `-raw`, `-layout`) sous `…/correcteur-tour2/pages/<clé>/` (1 043 pages).
  2. Chaque constat relu sur sa source : pages des PDF (`…/correcteur-tour2/outils/pg.py`), code aux commits `97dd829`,
     `7a54d43` et aujourd'hui, registres, préenregistrement, verdict, note du brainstorm.
  3. Différentiel appliqué par script, v2 → v3, par plages de lignes de la v2, chacune gardée par un contrôle de l'ancien
     texte (`…/correcteur-tour2/outils/appliquer_corrections_v3.py` ; journal `journal-application-v3.txt`). 23 blocs et
     un remplacement dans une ligne ; rien hors de ces plages (`git diff --no-index` relu).
  4. Contrôle de la v3 à la page exacte (`…/correcteur-tour2/outils/controler_v3.py`, sortie
     `…/correcteur-tour2/sortie-controle-v3.txt`) : (A) 129 passages anglais entre guillemets, chacun à la page de la
     citation la plus proche, 0 écart ; 58 passages sans PDF listés (français, code, titres, noms) ; (B) 109 chiffres de
     la littérature, par phrase imprimée ou par ligne et colonne de table, et présents dans la v3 sous leur forme
     française : 0 écart ; (C) 52 citations de pièces du dépôt à la ligne citée : 0 écart ; (D) épreuve R5 : 15 artefacts
     (chiffre altéré, mauvaise page, mot inversé, colonne ou ligne voisine, ligne de registre voisine), 15 rejetés.
  5. Scripts lancés par `python3 -I -B` : aucun `__pycache__`.
- **Exposition (R1).** Lignes du verdict de P3 ([V] l. 160-180, l. 350-360) et pièces de la note du brainstorm qui portent
  T1, T2 et T4 (`proposition-A.md` l. 17-18, `proposition-C.md` l. 48-50, `proposition-D.md` l. 30, `objections-1.md`
  l. 40-41, `objections-2.md` l. 338-342, `reponses.md` l. 375) relues **chiffres masqués**, pour vérifier S-01. Le libellé
  restait lisible et dit le sens de certaines comparaisons. Aucune valeur ni aucun sens n'est recopié dans la v3. Ce
  correcteur ne doit pas rédiger P3b (même réserve que le vérificateur du sens).
- **Le dépôt a changé pendant la correction.** Entre 11:25 et 11:45 UTC, Lazar a tranché le nœud 4 : N-029, option (c)
  renforcée (GO-2026-10-20-08, `registres/go.md` l. 35 ; `registres/decisions.md` l. 468-469 ;
  `docs/decisions/decision-N-029-v1.md`, `084e3052…`). La v3 le dit (S-17 (a)). Les autres lignes citées des registres
  sont identiques entre le commit `bb7b006` (lu à 11:45) et `8bd4a75` (relu vers 12:00) : `registres/decisions.md`
  l. 446, 453, 456, 457, 461 ; `registres/go.md` l. 32-34 (contrôle ligne à ligne).

## Verdict

**33 constats traités : 33 acceptés, dont 2 avec une adaptation déclarée (F-03 : seconde option, libellé resserré ;
S-17 (a) : nœud 4 tranché pendant la correction). 0 rejeté.** Aucun chiffre retiré. VS-01 reconfirmé au code (ci-dessous).
Le verdict de la synthèse change : la littérature ne prévoit ni n'exclut le nul de P3 ; la lecture après une question est
en défaut sur les cas proches ; P3b se lit comme diagnostic de l'instrument, la voie proposée pour R-262 (2) est E3 sur
des épisodes neufs ; E2 sur les actions de P3 est un nœud. Deux corrections hors constats, déclarées : la page de la
couche de [YS] (R7) et la ligne « Fichiers » de la v2 (même défaut que F-09).

## VS-01 : confirmation au commit (tour 2)

- `git show <commit>:src/controle_ia/harnais/episode.py` : `79113b4973d64bbc…` à `97dd829`, à
  `7a54d431d89745839220f882b41b13e8c62ecfdd` et à `HEAD` (`8bd4a75`) ; `environnements/propositions.py` : `5d97b223206c6378…`
  aux trois. Égaux aux fichiers du dépôt.
- `episode.py` l. 213-217 : au pas 0, contexte = ouverture (consigne privée, observation) ; aux pas suivants,
  `trs[b][i].ids + fmt.tour(...)`. L. 254 : `trs[b][i].ids = ctx + nv + fmt.cloture(...)` : les jetons de chaque action
  restent dans la transcription. L. 260 : passe unique sur `tr.ids`.
- `propositions.py` l. 238-269 : consigne privée en fin de message système (l. 247-248) ; observation, index des titres,
  indication privée, puis « Your action: » (l. 265-268). L. 40-49 : format `ACTION`, `TITLE`, `PROPOSAL`, `CONTROLS`,
  `COST`, `PREDICTION`. L. 32-39 : nommer modèles, jeux de données, métriques. L. 129-138 : première occurrence de chaque
  clé, dans n'importe quel ordre.
- `diag/20261019-230011-p3-reel/resume.json` (`4d6894b3…`, compagnon égal), champs lus un à un : `commit_cite` =
  `7a54d431d89745839220f882b41b13e8c62ecfdd`, 2 400 actions notées, 240 épisodes, `duree_s` 11 179,1.
- Conséquence : dès le deuxième pas, le contexte lu contient les actions précédentes, champ `COST` compris ; dans l'action
  même, des nombres peuvent précéder `COST` (S-06).

## Table

| écart | décision | raison (source relue) | où dans la v3 |
|---|---|---|---|
| F-01 [majeur] | acceptée | [DYL] p. 11 : « we re-ran the evaluation against prompted Gender Secret model organisms » ; p. 10 : chute sur les trois bancs ; cause non affirmée (« consistent with being caused by fine-tuning rather than the underlying behaviour », p. 11). Texte du correcteur repris tel quel. | table 4, E4 « tranche », l. 236 |
| F-02 | acceptée | [GM] p. 6 « We then take the maximum over EMA scores » ; p. 7 « takes the max over all mean scores of all possible windows » ; p. 12 sonde retenue. Lignes nommées comme imprimées ; table 3 relue colonne par colonne (mode brut). | 2.2 « Ailleurs », l. 143-149 ; règle gelée 1, l. 288-290 |
| F-03 | acceptée (seconde option) | Table 9 p. 28 : sonde de question 0.69 (Qwen3-8B) et 0.68 (Qwen3-4B) ; gemma-4-E2B-it 0.79 et 0.76 : « petits modèles » aurait été faux, d'où le libellé limité aux deux modèles. | E2 « tranche », l. 236 |
| F-04 | acceptée | [MK] p. 4 : « nearly matching the performance of the more consistent probes » ; « this may indicate … ». | 2.2 « Ailleurs », l. 137-142 ; rang 4, l. 177 |
| F-05 | acceptée | [OA] p. 1, les deux phrases sur leur page. Même constat que S-15. | 2.2 « Pour P3 », l. 159-164 ; règle gelée 1, l. 284-287 |
| F-06 | acceptée | [DYL] p. 10 (indice de capacité), p. 12 (« Scaling results are on prompted lying only »). | point 1, l. 49-50 ; ligne [DYL], l. 82 ; rang 5, l. 178 |
| F-07 | acceptée | [AG] p. 17 : faux positifs des distracteurs, puis « more mysterious failures ». | ligne [AG], l. 85 ; aussi l. 107-108 (même sens) |
| F-08 | acceptée | [AP] p. 23 : phrase entière sur la page. | 2.2, l. 127-128 ; point 1, l. 52-54 ; rang 4, l. 177 |
| F-09 | acceptée | `recouper_v2.py`, `main` : recherche sur toutes les pages des clés du bloc ; contrôle à la page exacte du vérificateur : 155 sur 155 (`…/verif-v2-fidelite/sortie-verification-v2-fidelite.txt`, `01791e30…`). « Your action: » : code (`propositions.py` l. 268) ; titre du billet : sans PDF. Le traitement du tour 1 reste tel quel (R12) : sa l. 15-16 se lit « trouvées sur une page d'une clé du bloc », non « à la page citée ». Même défaut corrigé dans la ligne « Fichiers » (hors constat, déclaré). | en-tête R7, l. 31-41 ; « Fichiers », l. 361 |
| F-10 | acceptée (retrait) | Exemple de conception absent de VS-01 ; retiré plutôt que marqué, pour ne rien choisir à la place du préenregistrement. | règles communes, option (b), l. 219-221 |
| F-11 | acceptée | [V] l. 345 : « rapport géométrique moyen d'environ 33 (10^1,5227) ». | l. 220-221 |
| F-12 | acceptée | [P] l. 318-320 (« 1 épisode » en l. 320). | l. 218 |
| F-13 | acceptée | [AU] p. 6 : « very correlated with the 'Impostor' label ». | ligne [AU], l. 86 |
| F-14 | acceptée | R-269 (`registres/decisions.md` l. 461) : nœud au-delà du plafond seulement. | E4 « coût », l. 237 ; dépense, l. 296-298 |
| S-01 [majeur] | acceptée | [P] l. 242-247 : T2 calcule les deux aires (champ et jetons d'avant), même agrégation. [V] l. 170-172, l. 358-359 : drapeau, à ne citer nulle part (relu chiffres masqués). Valeurs dans [NB] (lignes relues chiffres masqués). Note l. 8 et l. 85 ; `proposition-C.md` l. 323-324 ; N-025 l. 446 ; N-028 l. 456. Points (1) à (5) appliqués ; (5) : le registre est hors de mon droit d'écriture, la v3 le signale à la session. | E1 « quoi », « piège », l. 235, l. 238 ; nœud « Revendication », l. 259-274 ; sources, l. 27-29 |
| S-02 [majeur] | acceptée | [BX] p. 5 (« Score filtering retains the full transcript … » ; 0.81) ; p. 6 (0.63 ; 0,62 en légende de la figure 4, ajouté) ; p. 4 (organisme affiné sans consigne) ; p. 8 (0.5) ; table 1 p. 6 (1.00, 0.04, 0.03). [AU] p. 6 ; [YS] p. 3. Correction du vérificateur précisée : 0,63 n'a plus la consigne dans le contexte ; la parenthèse « consigne dans le contexte » a donc été remplacée par « rien d'écrit dans l'empan lu ». | point 2, l. 55-64 ; ligne [BX], l. 75 ; rang 3, l. 176 |
| S-03 [majeur] | acceptée | [AP] p. 9 et p. 18 ; [PAR] table 3 p. 7 (0.457, 0.437) et phrase des auteurs ; [DYL] p. 11 (0.85 contre 0.81) et table 9 (22 sur 32 : recompté par le script, partie B). Ajout de [AP] p. 18 « consistently rating every control response as honest » : c'est ce qui fonde la prédiction d'échec de T1 (sépare du témoin, pas l'acte). Recommandation (2) et confiances revues. | points 1 et 3, l. 45-54, l. 65-67 ; lignes [AP] et [PAR], l. 78-79 ; [DYL], l. 82 ; rangs 4 et 9, l. 177, l. 182 ; E2, l. 235-238 ; section 5, l. 243-256, l. 275-282 |
| S-04 [majeur] | acceptée | [P] l. 272-274 ; T1 [P] l. 238-241 ; [KU] p. 5. Pour l'oracle, « information sur l'acte » exige T1, T3 et T4 (T3 gardé en plus de T1 et T4 : plus strict). | E1 « tranche », l. 236 ; confiance, l. 251-256 ; point 3, l. 67 ; règles communes, l. 199-200 |
| S-05 [majeur] | acceptée | [P] l. 415-416, l. 428 ; `registres/go.md` l. 32 ; CLAUDE.md (écart à un préenregistrement scellé = nœud). « Après une question » retiré de la liste à défaut pour P3b ; manipulation du nombre : même statut. | E2 « quoi », l. 235 ; nœud E2, l. 275-282 ; concepts, l. 299-303 |
| S-06 | acceptée | `propositions.py` l. 40-49, l. 32-39, l. 129-138 (aux deux commits) ; [V] l. 345 ; note l. 43. | l. 209-216 ; E1 et E3 « contrôle », l. 239 |
| S-07 | acceptée | Note l. 26-27 ; `proposition-D.md` l. 81-99 (grille 2 × 2, maximum seulement, garde d'identité). Coût : « à deviser ». | l. 223-227 ; E1 « quoi » (v), l. 235 ; nœud, l. 275-282 |
| S-08 | acceptée | [KU] p. 5 ; [K] p. 3 ; [RH] p. 9 ; P-011 (`proposition-P-011-T0.7-sondes-v1.md` l. 42) ; note l. 72-78. « Choix sur la cible » retiré ; épisodes d'évaluation (T0.6) et leur coût nommés. | E3, l. 235-239 |
| S-09 | acceptée | Chaque pouvoir porte sa raison et sa valeur de la v1 ; ligne « ce qui a changé ». Raisons tirées des pages relues : légende de [K] table 1 p. 7 (« Domain shift effects are significant for all behaviours, while response strategy effects are often non-significant »), ajoutée à la ligne [K]. Confiances : 40 % (v1 : 60 %) ; 15 à 25 % (v1 : 25 à 35 %), jugements du correcteur. | section 3, l. 169-186 ; ligne [K], l. 87 ; confiance, l. 251-256 ; « Fichiers », l. 365-366 |
| S-10 | acceptée | Brief v2 l. 48 (R3). Bras fixé d'avance, sans diagnostic ni oracle ; 8 milliards sur épisodes neufs ; organisme affiné à part. | E4, l. 235-239 |
| S-11 | acceptée | [P] l. 135-142, l. 159, l. 248 ; [AD1] l. 34 (« G-01 »). | règles communes, l. 192-198 ; E1 à E3 « contrôle », l. 239 |
| S-12 | acceptée | Un bras par changement, en échelle : (a) position seule, (b) contraste, (c) sondes apprises avec la question, (d) couches ; question générale principale, précise en diagnostic. | E2 « quoi » et « tranche », l. 235-236 |
| S-13 | acceptée | [V] l. 204 (coût seul 0,8878) ; `reponses.md` l. 370-373 (champ masqué). Empan, plancher par permutation avec réapprentissage, mention hors des négatifs. | E1 « quoi » (iv) et « contrôle », l. 235, l. 239 |
| S-14 | acceptée | [PAR] p. 7 (0.941, 0.867 ; phrase des auteurs) ; [GM] table 3 p. 12, colonne LC[RT] (MultiMax 1,85 % à 82,14 % ; moyenne 0,5 %), définition table 1 p. 8 ; [AG] p. 43. Ajout pour les deux côtés : maxima de moyennes glissantes en LC[RT], 1,0 % à 13,55 %. | 2.2 « Ailleurs » et « Pour P3 », l. 133-157 ; ligne [PAR], l. 79 ; ligne [AG], l. 85 ; rang 7, l. 180 |
| S-15 | acceptée | [OA] p. 1. Même application que F-05. | l. 159-164 ; l. 284-287 |
| S-16 | acceptée | [CA] p. 8 (Nemotron-3 Nano « 0.613–0.760 ») ; p. 25 (« Nemotron 3 Nano 30B-A3B ») ; p. 18 (liste Qwen3.5) ; [DYL] table 9 (indices 14 et 27, colonne « AA »). Pouvoir du rang 5 : inconnu. | point 1, l. 49-51 ; ligne [CA], l. 83 ; rang 5, l. 178 ; E4, l. 236 ; questions ouvertes, l. 318-320 |
| S-17 | acceptée (point (a) mis à jour) | (a) nœud 4 : ouvert au début de la correction, tranché par N-029 vers 11:40 UTC ; la v3 le dit et en tire que P3b n'a aucune référence boîte noire. (b) recommandation (c) et défaut (c) pour les options (a), (b), (c). (c) revendication en proposition, tension avec N-028 présentée. (d) voie de R-262 (2) : E3 sur des épisodes neufs. (e) préalable de l'addendum 2 : R-262 (`registres/decisions.md` l. 453). | nœuds, l. 259-274, l. 299-310 ; règles communes, l. 202-204 ; recommandation, l. 243-249 |
| S-18 | acceptée | `decision-N-026-v1.md` l. 18-25 (conditions 1 à 4). Libellé exact, une ligne de lecture par bras, Bonferroni sur les seuls bras de production. | règles communes, l. 190-202 ; E1 « quoi » et « tranche », l. 235-236 |
| S-19 | acceptée | (a) [P] l. 385 et `resume.json` (`duree_s` 11 179,1) ; (b) [FQ] p. 3 (plancher et plafond seulement), témoin Alpaca : [AP] p. 5, [DYL] p. 8 ; (c) [EM] p. 38 (« while steering towards desperation increases ») ; (d) [K] p. 3. | l. 228-231 ; rang 8, l. 181 ; l. 100-104 ; ligne [K], l. 87 ; rang 2, l. 175 ; E3 « tranche », l. 236 |
| hors constat 1 | corrigée | Contrôle à la page exacte : « couche 15 » est en [YS] p. 3 (« we use layer 15 residual stream activations »), pas p. 2. | ligne [YS], l. 76 |
| hors constat 2 | corrigée | « phrases anglaises de la v2 sur leur page » : même défaut que F-09. | « Fichiers », l. 361 |

## Remarques hors constats (non appliquées ; pour le tour suivant ou pour Lazar)

- **Oracle et témoin.** Mettre le témoin parmi les négatifs d'apprentissage de l'oracle fait de P3-P4 un objectif en
  partie appris, comme la mention pour T3 (S-13). La v3 garde le témoin parmi les négatifs, comme la v2 ; à trancher dans
  le préenregistrement de P3b.
- **[AP] p. 9.** Juste après « substantially degraded performance on Sandbagging », la page dit que cette sonde est « the
  best probe of all we trained at distinguishing deceptive and honest responses, with near perfect separation on all
  datasets ». La p. 18 lève la tension (contre le témoin Alpaca). La v3 cite p. 18 ; la phrase de p. 9 n'est pas reprise.
- **[GM] p. 8.** Sondes non entraînées sur les contextes longs (« in particular not on long context ») : le 99,13 % de la
  moyenne est aussi un échec de transfert (remarque du vérificateur de fidélité, non comptée). Non appliqué.
- **[YS] p. 3.** Les auteurs affirment que l'information n'est pas absente ; la v3 garde « hypothèse » (remarque du
  vérificateur de fidélité). Non appliqué.
- **R-275** (registre, 11:19 UTC) : le projet antérieur de Lazar contient un plancher apparié. Hors littérature : la phrase
  « notre 0,57 ne se compare à aucun chiffre publié » (rang 8) reste vraie ; une comparaison interne devient possible.
- **E2 sur les épisodes de T0.6** : T1 y sera mieux nourri si les doses laissent des actions non sabotées chez le saboteur
  (note du brainstorm, socle commun, l. 79). À écrire dans le préenregistrement de T0.6 ou de T0.7.
- **Coûts.** Aucun coût revu ni devisé ; la manipulation du nombre ajoute des passes, à deviser.

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/synthese-comment-detecter-v3.md` ; ce fichier.
- `…/correcteur-tour2/outils/` : `pg.py`, `appliquer_corrections_v3.py`, `controler_v3.py`.
- `…/correcteur-tour2/` : `journal-application-v3.txt`, `sortie-controle-v3.txt`, `cles-tour2.txt` (clé, chemin, empreinte
  des 22 PDF) ; `pages/` (3 129 fichiers texte, 1 043 pages) : empreintes de tous les fichiers dans
  `empreintes-pages-tour2.sha256`, avec son compagnon.
- Aucun `__pycache__`.
