# Contre-lecture R2 du brouillon 4 du préenregistrement du papier C — lentille « voisins » — v1

- Contre-lecteur : sous-agent neuf, le 2026-10-20. Je n'ai écrit ni le brouillon 4, ni ses brouillons antérieurs, ni les
  notes de lecture des voisins, ni la configuration.
- Lentille : les voisins de HC1 et leurs citations, c'est-à-dire les sources « citées comme publiées », les contre-indices
  et les grilles publiées. J'ai vérifié les pages sur les PDF empreintés (R7) et jugé l'occupation (R8). J'ajoute, en fin
  de liste, quatre points de la session hors de ma lentille, parce que le texte transmis les demande (A1, A2, A7, chemin
  du module).
- Règles : R1, R2, R4, R6, R7, R8. Dépôt lu en lecture seule ; aucune recherche récursive ; aucun service payant.

## Verdict

**Scellable après corrections.** Aucun constat critique dans ma lentille. Les énoncés et la pièce revendiquée de HC1 sont
repris fidèlement de N-005, N-013 et N-023 (l. 124-157). Les deux voisins Bajaj et Tiganj et « The Silent Judge » ne
l'occupent pas (« non occupé confirmé », rapport compagnon `contre-lecture-note-voisins-v1.md`).

Il reste 13 constats : 4 majeurs, 8 mineurs, 1 de forme.
- Dans ma lentille : la description de Bajaj et Tiganj omet ses deux formes les plus proches de HC1 (CR-voisins-01). Le
  banc sur carte filtre sur un gain mesuré sur les textes mêmes du corpus B, ce qui contredit la leçon de Panin que le texte
  dit appliquer (CR-voisins-02). Une affirmation sur 2608.25869 est un calcul de notre lecteur, attribué au papier
  (CR-voisins-04).
- Hors de ma lentille : le chemin du module (CR-voisins-11) et le manque de tâches neuves (CR-voisins-12) doivent être
  corrigés avant tout scellement.

## Pièces lues (empreintes vérifiées)

| pièce | empreinte |
|---|---|
| brouillon 4 : `…/scratchpad/papier-C/papier-C-preenregistrement-HC1-HC3-v1-brouillon4.md` | `40bf1d4f7ca0c8ea0927230bade704980bb75e5b0ea57f5e6e68761803035517` (égale au compagnon) |
| points ouverts : `…/scratchpad/papier-C/points-ouverts-brouillon4-v1.md` | `babe4b4d64d697b8d0a72705e1ad89dbd2cb160d88c239c007495c00c1a5145f` (égale au compagnon) |
| note relue : `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md` | `9beecd71485678fd5d894825e1223fca42ca3a9dcb9fd24b7dea8388a7e062a5` |
| `docs/sources/pdf/2602.13568v1.pdf` (lu en entier) | `eca410e0375d9cfb23f334f85b93d073c0157ffe88960cd4a7884c5f38499da8` |
| `docs/sources/pdf/2509.26072v2.pdf` (lu en entier) | `c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba` |
| `docs/sources/pdf/ssrn-7424179-panin-2026-v1.pdf` (p. 10-11 seulement) | `27f88ed7d3b438f596b3b8cbb5ef8805b057e332c1444d8faebd0bd4b3e9a5c0` (égale au compagnon et au brouillon) |
| `docs/sources/pdf/2608.25869v1.pdf` (p. 1-8) | `f54d19a56474a4821b8e66df88e71bcb0d012e950363cdc38bdff6d468100599` (égale au compagnon) |
| `docs/sources/pdf/2606.14037v1.pdf` (p. 1-5, p. 12-14) | `682a2dad52698d06ecf1aa6515e90f5264b02c6fe7b97fe09d7672d1a4d533ac` (égale au compagnon) |
| `docs/sources/lecture-pdf-niveau2/rapport-lot3-Ca-juges-ancrage-v1.md` (lignes sur 2608.25869) | `ba7f52af73494dbb9e0a6576b17c8a77336c64961db57a2eb8df9f18ec964d0c` |
| décisions N-005 et N-006, N-013, N-023 | `cd49afbc…`, `157d388e…`, `1297f509…` : égales à celles du brouillon (l. 80-83) |
| `docs/programme-controle-ia-v2.md` (sections 5 et 10) | `2fd63bad…` : égale à celle du brouillon (l. 78) |

- Non lus : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, les textes des items et des prompts, la
  configuration (hors lentille). Pour `donnees/P1-items-gabarit-v1/`, j'ai fait un listing seul, sans rien ouvrir.
- Les citations de Bajaj et Tiganj et de « The Silent Judge » sont vérifiées par script (rapport compagnon).

## Constats

Format : identifiant, gravité, ligne du brouillon 4, preuve, correction en mots exacts.

### Dans la lentille « voisins »

**CR-voisins-01 — majeur — l. 140-143 (Bajaj et Tiganj).**
- Preuve : 2602.13568v1, p. 3 : « we fit a logistic regression predicting conformity from source framing
  (Friends/Experts/Other LLMs), prior correctness, and group size (log-transformed), including interactions ».
- Preuve : p. 3 : « For Llama-3.3 70B we additionally extracted the log-probabilities assigned to the forced-choice answer
  tokens YES and NO ».
- Preuve : p. 5, légende de la figure 3 : « Mean change in log-odds toward the unanimous prior (relative to no-prior
  baseline, k=0) as a function of group size ».
- Défaut : l'entrée ne dit que « verdict binaire ». Elle omet la régression sur l'intensité et la mesure continue par les
  jetons, les deux formes que le papier C doit créditer. Elle appelle aussi « verdict » la réponse OUI/NON à une question.
- Correction : remplacer les l. 140-143 par :
  « – pression sociale graduée (taille du groupe, k ∈ {1, 3, 5, 9}) sur des grands modèles de langage qui répondent par OUI
  ou NON, vers une réponse donnée, plus forte quand la source est étiquetée « experts humains » ; régression logistique sur
  la taille du groupe ; pour un modèle (Llama-3.3 70B, BoolQ), déplacement continu des log-cotes des jetons OUI/NON vers la
  réponse donnée, croissant avec k, jamais régressé sur la base : aucune destination estimée, aucun moniteur de contrôle,
  aucun attaquant (Bajaj et Tiganj, 2602.13568v1, `docs/sources/pdf/2602.13568v1.pdf`,
  `eca410e0375d9cfb23f334f85b93d073c0157ffe88960cd4a7884c5f38499da8`, p. 1 à p. 5) ; »

**CR-voisins-02 — majeur — l. 338-340 et l. 537 (banc sur carte), contre l. 34 et l. 315-317 (leçon de Panin).**
- Preuve : le banc exige, par juge, « ĝ_critique > 0, ĝ_éloge > 0 » (l. 288-290). Ce gain est lu sur les 30 textes qui
  forment aussi le corpus B (l. 332, l. 402-403). Un échec donne « arrêt avant l'étape 2, nœud » (l. 340, l. 537).
- Preuve : Panin, p. 11 : « a deference screen must not threshold the outcome ».
- Défaut : un nœud qui retirerait ou remplacerait le seul juge en échec filtrerait ce juge sur son gain, mesuré sur les
  textes mêmes de C-P3b. C'est contraire à la l. 316 (« Aucun juge ni aucune famille n'est retiré sur son gain au
  pilote ») et à la condition de la session pour A1 (« les lectures du banc n'entrent dans aucun test décisif »).
- Correction : écrire à la l. 340 (et reprendre à la l. 537) :
  « Échec chez un juge : arrêt avant l'étape 2 pour les trois juges, nœud. Le nœud ne retire ni ne remplace un juge pour ce
  motif, car le banc lit un gain sur les textes du corpus B (leçon de Panin, p. 11). Il choisit entre deux voies : corriger
  l'instrument pour les trois juges (nouvelle version du texte, contre-lue), ou poursuivre avec les trois juges et la
  réserve « contrôle positif en échec ». »

**CR-voisins-03 — mineur — l. 144-147 (« The Silent Judge »).**
- Preuves :
  - p. 1, pied de page : « 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Reliable ML
    from Unreliable Data. » ;
  - p. 2 : « We consider two families of cues. » ;
  - p. 4 : « Authoritative provenance cues further amplify bias: Expert > Human. » et « the Cue Acknowledgment Rate (CAR)
    is exactly zero » ;
  - p. 5, tableau 1 : « VSR is computed as the difference in first-response selection rate between complementary cue
    assignments ».
- Défaut : la plage « p. 1 à p. 3 » ne couvre pas la non-reconnaissance (p. 4). Le statut de publication manque.
  « Taux de bascule » est inexact pour le calcul publié.
- Correction : remplacer les l. 144-147 par :
  « – biais de provenance (et de date) de juges génératifs en choix entre deux réponses, mesuré par l'écart signé des taux
  de choix entre affectations complémentaires ; deux familles d'indices comparées en ampleur ; hiérarchie Expert > Humain >
  LLM > Inconnu ; justifications qui ne mentionnent jamais l'indice ; aucune intensité graduée, aucune destination, aucun
  moniteur de contrôle ; touche la famille « revendication d'autorité » (Marioriyad, Rohban et Soleymani Baghshah, « The
  Silent Judge », 2509.26072v2, atelier de NeurIPS 2025 « Reliable ML from Unreliable Data » d'après le pied de page de la
  p. 1, `docs/sources/pdf/2509.26072v2.pdf`, `c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba`, p. 1 à
  p. 5). »

**CR-voisins-04 — mineur — l. 195 (2608.25869, mode raisonné).**
- Preuve : 2608.25869v1, p. 7 : « CoT increases both the total shift and the slope » ; « within-C2 slopes are 0.267,
  0.506, and −0.007, respectively ».
- Preuve : le « ne tient plus » vient d'un calcul du lecteur de `lot3-Ca`. Il suppose la pente égale au gain, sur une seule
  paire GPT-4.1 de résumé. Le rapport l'écrit lui-même : « Deux chiffres pour trois inconnues … l'identification exige une
  hypothèse » (`rapport-lot3-Ca-juges-ancrage-v1.md`, l. 49 ; conclusion l. 215).
- Défaut : le brouillon présente un calcul de notre lecteur comme un résultat du papier, sans page (R7).
- Correction : remplacer la l. 195 et le début de la l. 196 par :
  « – Mode raisonné : sur une seule paire GPT-4.1 de résumé, la chaîne de pensée accroît le déplacement total et la pente de
  la note selon l'ancre (2608.25869v1, `f54d19a5…`, tableau 7, p. 7) ; un calcul de notre lecteur (`lot3-Ca`), qui suppose
  la pente égale au gain, la juge incompatible avec « destination = ancre » à gain constant ; ce n'est pas une affirmation
  des auteurs. Le mode raisonné est un modérateur rapporté, sans prédiction. »

**CR-voisins-05 — mineur — l. 188-196 (contre-indices, R4).**
- Preuve : 2608.25869v1, p. 6 : « Within C2, slopes over anchor value are approximately zero ». Dans la sonde GPT-4.1
  d'écriture créative, la masse passe du chiffre 5 au chiffre 4 pour les ancres 1,0 à 3,9 (tableau 4, p. 6). Le rapport
  `lot3-Ca` (l. 215) range ce résultat en « contre-indice faible pour ĉ = v* ».
- Défaut : le brouillon déclare le contre-indice de Venkatesh et al., pas celui-ci (symétrie, R4).
- Correction : ajouter après la l. 190 :
  « – Destination autre que la cible : dans une sonde GPT-4.1 d'écriture créative, sous une note antérieure forgée de 1,0 à
  3,9, la masse passe du chiffre 5 au chiffre 4 quelle que soit l'ancre (2608.25869v1, p. 6). Contrepoids : sur une paire
  de résumé, la note suit en partie l'ancre (pente 0,267, p. 7). Juge de qualité, une intensité, aucun moniteur de
  contrôle : contre-indice faible pour ĉ = v* (`lot3-Ca`). »

**CR-voisins-06 — mineur — l. 424-425 (grille 2606.14037).**
- Preuve : 2606.14037v1, p. 4 : « we vary nudge strength across weak, medium, and strong templates ». Le tableau 4 (p. 12)
  croise « Authority, Bandwagon » et « Weak, Medium, Strong ». Le format est binaire (« binary-choice (A/B) », p. 4) ; la
  mesure est un taux de bascule (p. 4).
- Défaut : la citation n'a ni page ni empreinte (R6, R7). Mon contrôle R8 : comparaison de deux familles de HC1 sur trois
  intensités, en ampleur ; direction imposée ; aucune destination ; aucun moniteur. Non occupé.
- Correction : « Grille publiée la plus proche, citée : autorité et consensus (« bandwagon ») en faible, moyen, fort (Kim
  et Flanigan, 2606.14037v1, `docs/sources/pdf/2606.14037v1.pdf`, `682a2dad…`, p. 4 et tableau 4, p. 12) ; choix binaire,
  direction imposée, taux de bascule, aucune destination estimée ni moniteur de contrôle (p. 4). »

**CR-voisins-07 — mineur — l. 34 et l. 315-317 (portée de la leçon de Panin).**
- Preuve : Panin, p. 11, contexte : le critère qui a retiré trois modèles était « a threshold on the outcome itself ». Le
  brouillon choisit ses formulations sur leur gain au pilote (l. 367-370 ; réserve 1, l. 458-459).
- Défaut : « est appliquée » est trop large. La leçon vaut pour les juges et les familles ; les formulations, elles, sont
  choisies sur leur gain.
- Correction de la l. 34 : « La leçon de Panin (p. 11) est appliquée aux juges et aux familles : aucun n'est filtré sur
  son gain. Les formulations, elles, sont choisies sur leur gain au pilote, sans seuil, par cibles étalées, sur des
  contenus disjoints de l'étape 2 (réserves 1 à 3). »

**CR-voisins-08 — mineur — l. 133 (Venkatesh et al.).**
- Preuve : N-023, section 1 : « L'effet croît avec l'écart au seuil et reste nul quand l'évalué passe déjà ».
- Défaut : « et reste nulle quand l'évalué passe déjà » se rapporte à « la note » : le sens est faux.
- Correction : « …monte vers la note de passage, d'autant plus que le seuil est loin ; l'effet reste nul quand l'évalué
  passe déjà : … ».

**CR-voisins-09 — mineur — l. 134 et l. 41-45 (statut des ajouts ; point A2).**
- Preuve : la contre-lecture de la note conclut « non occupé confirmé ». Aucune prédiction de HC1 n'est prise,
  contrairement à N-023, où la destination « cible » était prise en qualitatif.
- Correction de la l. 134, après la contre-lecture de la note sur Panin : « **ajouts du brouillon 4** (notes de lecture
  finales `docs/notes/lecture-voisin-panin-v1.md` (`<<EMPREINTE_NOTE_PANIN_FINALE>>`) et
  `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1.md` (`<<EMPREINTE_NOTE_VOISINS_FINALE>>`), contre-lues ; aucun
  énoncé changé, aucune prédiction prise ; ajout de routine, `<<R-xxx>>`) : ».
- Avis sur A2 : routine pour ces deux sources. Une ligne d'information à Lazar est recommandée, vu le précédent N-023.

**CR-voisins-10 — forme — l. 127 (instrument cité).**
- Preuve : N-013, section 1, cite aussi 2411.17693 (`lot3-Aa`), 2402.14016 (`lot2-C2b`) et « recommandée par 2606.07612,
  p. 25 ».
- Correction : ajouter « ; 2411.17693 ; 2402.14016 ; recommandée par 2606.07612, p. 25 (N-013, section 1) ».

### Hors de ma lentille (demandés par le texte de la session)

**CR-voisins-11 — majeur — l. 46, l. 53, l. 327, l. 357 (chemin du module).**
- Preuve : décision de la session (non revérifiée par moi). P4 et P3b exigent un arbre gelé égal à celui du commit 7a54d43,
  hors dossiers documentaires et sorties. Un module sous `src/` le casserait.
- Correction de la l. 46 : « Module d'analyse et de lancement à écrire, tester et empreinter :
  `docs/procedures/papier-C-v1/` (hors de l'arbre gelé) ; ».
- Correction de la l. 53 : « Module : `docs/procedures/papier-C-v1/`, gelé par les lignes « Module du papier C : chemin :
  empreinte » de ce texte, une par fichier, comme P4 ; tests attendus : `<<NOMBRE_TESTS>>`. ».
- Correction de la l. 357 : « Calculé par le script de dérivation du module (`docs/procedures/papier-C-v1/…`, empreinte aux
  lignes « Module du papier C ») ».
- La l. 102 (`src/controle_ia/bases/scores_jetons.py`, réutilisé sans modification) reste juste.

**CR-voisins-12 — majeur — l. 65, l. 376-378, l. 385-386, l. 431, l. 555 (point A7 : tâches neuves).**
- Preuve : fait de la session (non revérifié par moi). La source compte 64 tâches ; le pilote de T0.5 en prend 60 ; il en
  reste 4. L'étape 2 demande n/2 = 30 à 120 tâches disjointes (l. 376-378, l. 431). La garde 16 (l. 555) arrêterait
  toujours l'étape 2. Le texte doit trancher avant le scellement.
- Option (a), partage écrit des 60 tâches, gelé avant le scellement :
  - le calibrage du pilote ne prend que les épisodes d'un sous-ensemble de tâches tiré par graine (par exemple 20 tâches,
    40 contenus) ;
  - l'étape 2 prend les autres tâches et les 4 restantes (44 au plus), avec des épisodes et des graines neufs.
  - Indépendance : tâches et contenus disjoints, comme aujourd'hui.
  - Coût : n ≤ 88. La liste {60, 90, 120, 180, 240} (l. 376-378) se réduit à {60}. La réserve « puissance faible » devient
    probable, et un n_cal plus petit élargit les erreurs types du vivier.
- Option (b), nouvelle extraction de 30 à 120 tâches neuves de l'environnement (a), fixée avant le scellement
  (`<<CHEMIN_TACHES_ETAPE2>>`), sans lecture de sortie de juge :
  - Indépendance complète : tâches, contenus et graines.
  - Coût : travail sur processeur si la source le permet (routine) ; sinon dépense et nœud. Risque d'écart de distribution
    entre les tâches du calibrage et celles de l'étape 2 (à ajouter à la réserve 2).
- Option (c), mêmes 60 tâches pour le calibrage et l'étape 2, avec des épisodes et des graines neufs :
  - Indépendance : contenus disjoints, tâches partagées. L'effet propre d'une tâche entre à la fois dans le choix des
    formulations et dans l'estimation ; la malédiction du vainqueur (réserve 3) devient corrélée.
  - Les l. 65, 385 et 550 sont à réécrire. Le plafond devient n ≤ 128, donc {60, 90, 120}.
  - Si le verdict de G0 a jugé les sondes sur des épisodes de ces mêmes tâches, c'est aussi une sélection sur les mêmes
    tâches, à déclarer.
- Recommandation : (b) si l'extraction reste sur processeur et donne au moins 120 tâches ; sinon (a), avec la liste des
  effectifs plafonnée et déclarée ; (c) en dernier. Confiance moyenne.
- Type de décision : périmètre interne d'une phase, donc « proposer avec recommandation » (défaut sous 48 heures), à
  trancher avant le scellement.

**CR-voisins-13 — mineur — l. 314-316, l. 346, l. 357-359, l. 464-466, l. 550-551 (point A1 : banc sur les 30 textes).**
- Le texte garantit la condition par ses règles, sauf le point traité en CR-voisins-02 :
  - aucune grandeur du pilote n'entre dans un test décisif (l. 314-316) ;
  - la consigne B n'est jamais lue sur les textes du corpus B au pilote (l. 346) ;
  - aucune grandeur du banc n'entre dans l'étape 2 (l. 464-466) ;
  - les règles de l'addendum (l. 361-380) n'utilisent que les contenus de calibrage.
- Il manque une garde exécutable.
- Correction, à ajouter à la fin du premier paragraphe de la section « 2. Addendum de dérivation » (l. 359) : « L'addendum
  ne lit aucune sortie du banc (point 1.2) ; le script de dérivation refuse en entrée tout fichier du banc (garde testée sur
  un cas sain et sur un artefact, R5). Le banc ne règle aucun paramètre de l'étape 2 : son issue ne fait que permettre ou
  arrêter l'étape 2 (CR-voisins-02). »
- La même phrase s'ajoute au point 12 de la liste d'arrêt (l. 550-551).

## Ce que je n'ai pas couvert

- La note sur Panin et la description de Panin (l. 135-139), hors la citation de la p. 11 (vérifiée, p. 11 du PDF).
- A3 et A4 : hors de ma lentille, sans avis.
- La configuration, le vivier et les mesures de conception : non lus.
- Le statut de l'atelier de « The Silent Judge » est lu sur le PDF ; la liste des papiers acceptés de l'atelier n'est pas
  vérifiée.
