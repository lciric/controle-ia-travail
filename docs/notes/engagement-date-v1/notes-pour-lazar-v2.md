# Engagement daté sous embargo — notes pour Lazar (v2)

- **Écrit** le 14 novembre 2026 entre 01:25 et 01:45 UTC (`date -u`) par le rédacteur de la v1, d'après la lecture adverse `docs/notes/engagement-date-v1/lecture-adverse-engagement-v1.md` (`43bd0e57…`, R-2634, verdict « figeable après corrections ») et les choix de la mère transmis avec elle. La v1 du texte (`630cf444…`) et des notes (`edea9cda…`) reste, intacte (R12).
- **Texte v2** : `docs/notes/engagement-date-v1/texte-engagement-date-v2.md`, sha256 `cf445a1f0abc0d09f0df6095175101811f6bb6c436439eb5e673a534568c51ce`, scellé. **Journal des couples appliqués** : `docs/notes/engagement-date-v1/journal-couples-v1-vers-v2.md`, scellé.
- **Rien n'est soumis, rien n'est commité, aucun compte n'est créé, personne n'est contacté.** Aucune lecture dans les chemins interdits.

## 0. Verdict

Neuf énoncés, en anglais, datés, sans résultat ni chiffre de résultat. Les dix-neuf couples de la lecture adverse sont appliqués (4 bloquants, 8 majeurs, 7 mineurs), aucun n'est écarté. Choix de la mère suivis : clause « juges » retirée de S9 ; champs à ta main sous deux marqueurs ; motif « avant tout échange avec des chercheurs extérieurs » retiré. Avant de figer, il reste : remplir les deux marqueurs, puis calculer l'empreinte du fichier rempli ; trancher la co-élévation (S4) et le moment du dépôt.

## 1. Les deux marqueurs et l'empreinte

- Le texte v2 porte exactement deux marqueurs, chacun une seule fois : `<<DATE_FIN_EMBARGO>>` (en-tête, date de fin d'embargo, au format AAAA-MM-JJ) et `<<AUTEURS>>` (en-tête, noms et, si tu veux, affiliations). Rien d'autre n'est à remplir.
- **L'empreinte qui fait foi se calcule sur le fichier rempli**, pas sur la v2 scellée ici : remplir les marqueurs change l'empreinte. Geste proposé : copier la v2 sous un nom neuf (`texte-engagement-date-v2-rempli.md`), remplacer les deux marqueurs, vérifier par programme qu'il ne reste aucun `<<`, sceller, puis joindre **ce fichier-là** à la registration et publier **son** empreinte (section 4, point 9).
- La différence entre la v2 scellée et le fichier rempli doit se limiter aux deux lignes des marqueurs (vérifiable par `diff`).

## 2. Les neuf énoncés et leurs sources

Empreintes : N-005/N-006 `cd49afbc…`, N-007/N-008 `ab7dc9bb…`, N-013 `157d388e…`, N-023 `1297f509…`, N-055 `371879d5…`, N-067 `966dd9dc…`, N-068 `ba6b2db3…`, N-069 `6e0d9d40…`, N-070 `7c4ce221…`, contre-lecture de la synthèse finale (R-2567) `f1580ddc…`, synthèse finale de niveau 3 `e30a013d…`, programme v2 `2fd63bad…`, lecture adverse `43bd0e57…`.

| énoncé du texte | hypothèse | source de la lettre | ce qui la rend déclarable |
|---|---|---|---|
| S1 | H1 | programme v2, l. 93 ; N-055 (H1a porte la revendication, H1b rapportée comme information) ; qualificatifs de R-2567, constat M1 | R-2567, section 6 : « H1 (texte de M1) » |
| S2 | H2 | N-007, section 1 ; pièces de R-2567, constat m6 ; configuration de référence du billet du 30 octobre 2026 (synthèse finale, H2) | R-2567 : « H2 (conjonction, avec l'annonce de NARCBench datée, m6) » |
| S3 | statistique conjointe du papier B | N-069, section 4, point 2 (texte de R-2567, constat M2) | R-2567 : « statistique conjointe du papier B (texte de M2) » ; N-069, section 9 |
| S4 | co-élévation (statistique de population) | N-069, section 4, point 1 ; contrôles de construit attribués à 2611.10620 | **N-069 seule** (section 9) ; absente des deux listes de R-2567 (section 4, point 1) |
| S5 | H3 | programme v2, l. 111 ; synthèse finale, H3 | R-2567 : « H3 (deux courbes à budget total constant) » |
| S6 | H5 | programme v2, l. 113 ; N-013, section 7 ; R-2567, constat B3 | R-2567 : « H5 (la loi, texte de B3) » |
| S7 | H7 | programme v2, l. 114 ; N-013, section 7 ; R-2567, constat m1 | R-2567 : « H7 (texte de m1) » |
| S8 | HC1 | N-005/N-006 (destination libre ĉ ; prédiction 1 et prédiction 3 de stabilité **de rang**, magnitudes non revendiquées) ; N-013, section 1 ; N-023 et R-2554 ; R-2567, constat M7 | R-2567 : « HC1 (pièce sans l'opposition juge contre sonde, texte de M7) » |
| S9 | HC2 | N-068, section 4, **sans la comparaison aux juges** | N-068, section 8 ; absente des deux listes de R-2567 |

Dates « wording fixed internally » : 4 octobre 2026 (programme v2, N-005, N-007) ; 6 octobre (N-013) ; 27 octobre (N-055) ; 13 novembre (R-2567, N-068, N-069). Les qualificatifs datés du 13 novembre (S1, S5, S6, S7, et le retrait de l'opposition dans S8) viennent de la contre-lecture R-2567, pas d'un mot de toi ; le texte v2 dit donc « internal decisions and verification reports ». Les montrer à toi avant le gel en fait ta décision.

Mentions de R-2567 : en entier sous chaque énoncé. Pour S4 et S9, absentes de la table d'exposition de R-2567, le texte ajoute « No dedicated inventory of unread sources was made for this statement ».

## 3. Ce qui est laissé dehors, et pourquoi

| laissé dehors | raison | pièce |
|---|---|---|
| **comparaison des déplacements de la sonde et des juges sous les mêmes attaques (S9, HC2)** | **retirée sur choix de la mère** (lecture adverse, B1) : c'est l'opposition juge contre sonde que R-2567 interdit de déclarer tant que 2607.00415 n'est pas lue. **Elle reviendra dans une version suivante du texte (ou une registration à part qui cite celle-ci) après lecture de 2607.00415 sur PDF**, si la lecture la laisse libre. Le texte v2 dit qu'aucune revendication sur cette comparaison n'y est enregistrée et nomme 2607.00415 | R-2567, section 6 et constat M7 ; N-068, section 4 ; lecture adverse, B1 |
| stabilité de g « pour un moniteur donné » (S8 de la v1) | plus forte que N-005, qui ne prédit que la stabilité de rang ; remplacée par la lettre de N-005 avec ses contre-indices | lecture adverse, B2 |
| motif « before any substantive exchange with outside researchers » | retiré sur choix de la mère : il sera public à l'échéance, présente le dépôt comme une prise de date, et sort du cadre « plan de recherche en cours » du registre | lecture adverse, M6 |
| L, T | collision la plus probable versée et non lue ; le registre refuse « proofs, or other theoretical pieces » | R-2567, section 6 ; guide archivé |
| H6, Tr, prédiction de H8, H4′, HC2b, coût de HC4, quorum de HC5, HC6 par moniteur | « à ne pas déclarer libres en l'état » | R-2567, section 6 |
| H9 | retirée ; mesure descriptive sans revendication | N-070 |
| HC3 | classée dans aucune des deux listes de R-2567 ; aucune décision ne la range dans l'enregistrement | R-2567 |
| O4 et énoncé retenu de O2 | assemblage de pièces publiées, jamais libre ni neuf | R-2587 ; N-067 |
| forme de O12 | nœud ouvert | R-2581 ; plan des cinq comptes, D-5 |
| O1, sceau de O3, O11, O17, O8, rôle 1, N-044, N-045 | plus revendiqués, ou non déclarables, ou sans vérification dédiée | N-067 ; R-2567 |
| tout ce qui est sous embargo | consigne ; le texte ne dit même pas que ces pièces existent | — |
| bases de G1 et règle « dans chaque mode » (N-056) | détail de conception de G1, non scellé ; appelle la famille tenue à l'écart | N-056 |
| contre-indices chiffrés | aucun chiffre de tiers figé sans page (R7) ; les contre-indices sont nommés sans chiffre (S8, S9) | — |
| noms de la littérature du « poids du conseil » (Harvey et Fischer 1997 ; Yaniv et Kleinberger 2000) | PDF non lus (N-005 dit « à lire, R7 ») ; formule générique gardée | lecture adverse, section 4 |
| adresses des trois billets | non relevées dans les rapports des lecteurs ; le texte donne titre, lieu et date (fichiers archivés sur la branche `prep/etat-de-l-art-niveau3-pieces-v1`, rapports des lots 2-A et 2-B) ; à compléter si tu veux une adresse | lecture adverse, section 4 |

## 4. Ce que tu dois choisir

1. **S4, la co-élévation, entre-t-elle ?** N-069 la met dans l'enregistrement, R-2567 ne la classe pas, ses contre-indices sont forts (N-069, section 7). Options : (a) garder, ce qui date la forme ; (b) retirer, ce qui laisse S3 seul. Recommandation : (a), confiance 0,6. Défaut proposé : (a).
2. **Moment du dépôt (D-8 du plan).** (a) Après la tranche de veille du 10 au 13 novembre et la synthèse version 2, ce qui raccourcit les mentions ; (b) maintenant. Recommandation du plan : (a), sauf si un rival paraît ; je la reprends, confiance 0,6. Si (a), les neuf lignes de statut changent : nouvelle version du texte, jamais une réécriture. Si tu veux que l'engagement précède un échange extérieur (TASTE), c'est (b), décidé par toi. Ce motif ne figure plus dans le texte.
3. **Lire 2607.00415 avant de figer ?** Avantage : la clause des juges de S9 revient dans la même registration. Inconvénient : une lecture de plus avant le dépôt. Sinon elle revient plus tard, sous la forme d'une version qui cite celle-ci.
4. **`<<DATE_FIN_EMBARGO>>`.** **L'embargo finit de lui-même à la date choisie** (section 5) : tout ce qui est figé deviendra public à cette date, sans geste de personne, quatre ans au plus après la soumission. Recommandation : une date bien en deçà de quatre ans (par exemple deux ans), et une levée anticipée quand le premier papier sort. Confiance faible sur la bonne durée.
5. **Titre.** Proposé : « White-box control against diffuse threats — dated statement of hypotheses, no results ». Il est à vérifier s'il est visible pendant l'embargo. S'il l'est, choisis un titre plus neutre.
6. **`<<AUTEURS>>`.** Chaque contributeur administrateur approuve (ou laisse passer 48 heures) le dépôt, la levée et un éventuel retrait.
7. **Compte.** Le registre dit qu'un compte existe (R-1580 : projet privé `dr57c` créé par script le 5 novembre). Le plan te repose la question : à confirmer.
8. **Gabarit.** Recommandation : « Open-Ended Registration », avec le texte rempli collé dans le résumé **et** le fichier joint seul. Le guide le décrit comme « Only use if another template doesn't fit your study design or registering a completed project ». Le choix reste défendable (plan de programme, non d'une expérience unique), « OSF Preregistration » étant l'autre option.
9. **Ancre publique de l'empreinte du fichier rempli** (R-2563). Une registration sous embargo est invisible et n'a pas de DOI. La date ne se prouve à un tiers, pendant l'embargo, que par une empreinte publiée ailleurs. Options : (a) une ligne datée sur la page publique de l'organisme, sur un lieu que tu tiens, mais qui signale l'existence d'un engagement ; (b) un horodatage tiers de l'empreinte seule, qui n'expose rien, avec un outil à choisir et à vérifier. Recommandation : (a), confiance 0,5. Publication : nœud.

**Interdit (lecture adverse, M7) : ne jamais créer la registration depuis le projet `dr57c`.** La registration se crée par le circuit des registrations, sans projet (« from scratch »), avec **un seul fichier joint : le texte rempli**, rien d'autre. Raison : depuis un projet, tous ses fichiers (jusqu'à 5 Go) sont joints et figés (guide). Or les manifestes déposés dans `dr57c` listent, en chemins et empreintes, le préenregistrement des sondes de T0.7 et le texte scellé de P3-bis et ses consignes (R-2384, R-2397, vérifiés par nom de ligne). Comme l'embargo finit seul et qu'une registration publique ne redevient jamais privée, ces chemins deviendraient publics à l'échéance, sans retour. Les notes ne se joignent jamais non plus. Le nœud R-1580 (rendre `dr57c` public et le geler) reste distinct et ouvert. Il porte la même exposition.

## 5. Règles de l'Open Science Framework (lecture corrigée)

Pages d'aide lues le 14 novembre 2026 vers 01:14 UTC, archivées et scellées sous `docs/notes/engagement-date-v1/sources-osf-20261114/` (`adresses.txt`, `2cb459da…`) : guide des registrations `5e1ba9b5…` (« Last updated on November 1, 2026 ») ; « Addressing Fear of Scooping » `98fcf79f…` (3 août 2026) ; transition, questions des registrations `09ad29e8…` (12 novembre 2026) ; transition, page « Registrations » `cff1f9f2…` (30 septembre 2026).

**Corrections par rapport aux notes v1** (lecture adverse, section 5) :
- **Fin d'embargo automatique.** Guide : « enter your registration into embargo, which will make it private until the end of the embargo date » ; « Select a date that the embargo will end and the registration will be made public » ; « the registration embargo will end at midnight ». Page 768 : « Embargoed registrations will remain embargoed until their scheduled end date ». La phrase que la v1 tenait pour contraire (« The only way to make a registration public is to actively end the embargo ») répond à une autre question, celle d'un projet rendu public. **Il n'y a pas de contradiction** : la v1 se trompait.
- **Registration possible sans projet après le 16 novembre.** Page 768 : « You can continue creating new registrations through the OSF Registration workflow after new projects can no longer be created. An OSF Project is not required to create a registration. » L'enregistrement depuis un projet existant reste ouvert jusqu'au 19 février 2027. Ce n'est plus un point « à vérifier ». Il reste une tension mineure : le guide dit qu'un projet « will be made available » pour une registration créée sans projet, et ce que devient ce projet après le 16 novembre n'est écrit nulle part. L'année du « November 16 » n'est pas écrite.
- **Registre général non modéré.** Guide : « OSF registrations are a non-moderated service. This means that you are in charge of accepting your submission » ; « Registrations that are not submitted to a Community-run Registry are reviewed and approved by the administrators on the registration ». Pas de refus à l'entrée. La règle d'acceptation (« plans for research that is underway, with explanation of the current state of the study » ; refus des « commentaries, proofs, or other theoretical pieces ») reste opposable après coup, d'où le retrait du motif (M6).
- **Durée : trois formules** pour le point de départ des quatre ans : « from the first submission » (page 634), « from creation date » (guide, préparation), « from the date of submission » (guide, questions). Une date de fin bien en deçà de quatre ans rend l'écart sans effet.

**Inchangé** : embargo choisi à la soumission ; « page not found » pour les tiers ; lien en lecture seule, anonymisable, par un administrateur ; approbation automatique après 48 heures, date retenue égale à la date de soumission ; levée anticipée soumise aux administrateurs, automatique après 48 heures ; DOI seulement pour une registration publique ; fichiers figés, 5 Go au plus, mises à jour par « update » avec historique ; retrait irréversible, embargo à lever d'abord ; jamais de retour au privé.

**Encore à vérifier à la source avant le dépôt** :
1. Titre, contributeurs et description : visibles ou non pendant l'embargo (moteur de recherche du site, profils, métadonnées envoyées pour le DOI).
2. Conditions d'utilisation et licence du contenu déposé.
3. Fuseau de la date retenue (le guide ne dit que « from midnight »).
4. Comportement de l'interface elle-même : toutes ces règles sont lues sur des pages d'aide, jamais observées sur l'interface.

## 6. Réserves

- La phrase « Pilot and instrument-validation runs exist; none of them is reported here » est à confirmer par toi (lecture adverse, m7).
- S2 garde « the guarantee is uniform over the episode horizon and calibrated on whole honest episodes ». N-007 en fait une lecture portée au préenregistrement de G1, qui « ne change pas l'énoncé ». La synthèse l'inclut dans la conjonction dite libre (lecture adverse, m5) : acceptable, je te le signale.
- Identifiants : tous tracés dans le dépôt par la lecture adverse, aucun vérifié sur arXiv ni sur SSRN. Les versions ajoutées (m3) sont celles que la lecture adverse nomme.
- Aucun nom de modèle dans le texte ni dans ces notes.

Version 2 ; ne sera jamais réécrite (R12).
