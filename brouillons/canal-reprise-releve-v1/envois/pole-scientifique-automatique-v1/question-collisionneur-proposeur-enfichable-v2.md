# Question pour le collisionneur — organisme propre ou hybride : les chercheurs automatiques de la littérature branchés devant notre juge — v2 (brouillon de conv-audit ; session-depot fige sa version)

v2 écrite par conv-audit (instance du 27 octobre 2026) à partir de 14:49 UTC (heure lue sur `date -u` : 14:49:17) ; la
v1 (13:20 UTC, `b45c0578…`) est remplacée et gardée (R12) : **ne pas lancer la v1**. Correction, sur la remarque de
Lazar de 15:32 heure de Paris (« je croyais que les AI scientists de la littérature n'étaient pas juste des proposeurs
mais qu'ils testaient leurs hypothèses aussi ? va vérifier ») : vérifié, il a raison (section « Correction » ci-dessous).
Mot de Lazar de 14:17 heure de Paris, verbatim : « demande au collisionneur avant qu'on ne se décide dessus ». Objet : la recommandation que j'ai faite à Lazar à 14:08 heure de Paris (reproduite ci-dessous comme **position à
attaquer**, pas comme fait). Forme « arbitre », trois modèles, trois tours, une tentative par cellule, un refus arrête le
tour. **Dépense : seulement sur le mot direct de Lazar dans la session de session-depot.** Contrainte posée par Lazar le
même jour (14:17) : dans l'organisme, côté Claude, seulement Opus 5.5 et Fable 5.1.

## Correction de la v1 (faits vérifiés le 27 octobre 2026, liens à la fin)

- **AI Scientist v2 (Sakana, arXiv 2504.08066)** exécute ses propres expériences : recherche arborescente en quatre
  étapes (investigation, réglage des hyperparamètres, programme de recherche, ablations), « the generated code is
  immediately executed in a Python interpreter » ; relecture des figures par un modèle de vision, rédaction, relecteur
  automatique ; les humains ont choisi les idées et le meilleur manuscrit ; code ouvert (licence à vérifier).
- **Agent Laboratory (arXiv 2501.04227)** : revue de littérature, expérimentation (code d'apprentissage automatique
  généré), rapport.
- **Co-scientist (Google)** : génère, critique, classe (tournois) et fait évoluer des hypothèses ; les expériences sont
  faites par des humains.
- **Robin (FutureHouse, arXiv 2505.13400)** : propose et classe (tournois jugés par un modèle) ; les expériences de
  paillasse sont faites par des humains ; un agent (Finch) analyse les données.
- **Conséquence** : la v1 ne prévoyait qu'une prise, « proposeur ». Il y en a deux : (1) **proposeur** (pour tous) ;
  (2) **exploration** (pour ceux qui expérimentent) : le système explore librement, itère et règle sur une **partie de
  développement** d'une banque (traits et issues visibles), puis **gèle** des fiches, que notre noyau juge sur une
  **partie d'épreuve** jamais vue. Leur recherche arborescente devient la phase exploratoire, notre juge la phase
  confirmatoire ; on ne retire que leur relecteur modèle. Notre organisme a reçu la même phase exploratoire (v7, pièce 4
  bis), pour que le duel soit à armes égales (mêmes données de développement, même épreuve, même budget).

## Question

« Un pôle de recherche automatique (pièce C, conception ; pièces E1, E2, D4 : ce qui est vérifié en simulation) est fait
d'agents (expérimentateurs, vérificateurs d'un autre modèle, recombinaison, synthèse) autour d'un **noyau** tenu hors des
agents : juge à mise contre une bibliothèque de nuls (inférence universelle, seuil 1/α), ordre d'exécution secret tiré
après le gel, nul des filles pour la recombinaison, mémoire à empreinte prédictive qui refuse les redites et hérite la
preuve, clés jamais vues par les agents. Il n'a tourné qu'en simulation ; un premier lancement avec de vrais agents est
devisé (pièce D). Le tour du collisionneur du 26 octobre (pièce S) avait conclu : « ni perfectionner le nôtre tel quel, ni
adopter un système de la littérature : voie hybride ancrée sur notre noyau », et écarté tout moteur dont les agents
héritent des clés. Depuis, le juge, le nul des filles et la mémoire ont été éprouvés en simulation (E1, E2, D4).

Position de conv-audit à attaquer : « Ce que les chercheurs automatiques publiés font mieux que nous, c'est **proposer**
(idées ancrées dans la littérature, tournois d'idées, longues courses autonomes) ; ce qu'ils ne font pas, c'est **juger
avec une garantie** (relecteur modèle ou classement entre modèles, inflation documentée, conscience d'évaluation partagée
avec l'expérimentateur). Donc : hybride sensé = un proposeur de la littérature **devant** notre noyau et notre juge ;
hybride insensé = prendre leur relecteur. Recommandation : notre organisme, rôle « proposeur » rendu enfichable, et un bras
de comparaison avec un proposeur ouvert, mesuré par notre juge en **fiches promues par dollar**. » (Position de la v1,
corrigée ci-dessus : deux prises, et la phase exploratoire des deux côtés.)

1. **Les candidats.** Parmi les chercheurs automatiques publiés ou en code ouvert (par exemple AI Scientist v1 et v2 de
   Sakana, le co-scientist de Google, Agent Laboratory, Robin et Kosmos de FutureHouse et Edison, CodeScientist, Zochi,
   AI-Researcher, et tout autre que vous connaissez, y compris de 2026), lesquels peuvent être branchés **à la prise
   « proposeur »** et lesquels **à la prise « exploration »** (explorer et régler sur une partie de développement, puis
   geler des fiches jugées ailleurs), **sans que leurs agents héritent de clés ni de réseau** ? Que perd un système à
   boucle complète quand on lui retire son relecteur et qu'on lui impose de geler avant l'épreuve ? Pour chacun : licence, ce que l'étage prend en entrée et rend en sortie, ce
   qu'il coûte par idée, et ce que vous savez de sa valeur (mesures publiées, avec titre, année, lien ; dites ce qui est
   rapporté et ce qui est supposé — nous vérifierons sur les PDF).
2. **Le format de la fiche.** Notre juge exige une fiche qui engage une **loi prédictive des issues sachant les traits
   des instances**, sur un espace d'instances déclaré. Les étages de proposition de la littérature produisent des idées
   en texte libre. Qui fait la traduction (un agent de notre organisme, l'étage lui-même sous consigne, un gabarit
   mécanique) ? Que perd-on à la traduction, et comment mesurer qu'une idée « traduite » est encore l'idée proposée ?
3. **Le proposeur propre.** Qu'est-ce qu'un bon proposeur maison, avec seulement Opus 5.5 et Fable 5.1 : quelles entrées
   (mémoire du pôle, moisson de littérature par un rôle lecteur servi par le noyau, fiches survivantes, redites refusées),
   quelle diversité imposée, quelle garde contre l'enfermement (le proposeur apprend à plaire au juge) ? Le juge étant
   figé et le nul composite, où un proposeur peut-il encore tricher (paris couverts, fiches à domaine étroit, lois qui
   collent à la marginale, fiches jumelles qui contournent la mémoire) ?
4. **La mesure.** « Fiches promues par dollar » : est-ce la bonne métrique ? Que compte-t-elle mal (fiches vraies mais
   sans intérêt, découvertes en double, coût caché de la traduction, lignées fécondes contre coups isolés) ? Proposez la
   métrique, le plan d'un duel à budget égal entre proposeur maison et proposeur de la littérature sous le **même** juge,
   le nul (même consigne, même budget, idées tirées au hasard de la mémoire), la taille d'échantillon, et le seuil qui
   ferait conclure que le proposeur de la littérature n'apporte rien — ou que le nôtre n'apporte rien.
5. **Recommandation.** Faut-il décider maintenant, ou après le premier lancement réel (pièce D, option a) ? Qu'est-ce qui
   vous ferait changer d'avis ? »

## Faits à servir (noms neutres ; aucun sigle ; aucun score de pilote ; rien de tout ceci n'est servi à un organisme)

- C : la conception du pôle (`conception-pole-scientifique-v1.md`, `a4f94148…`).
- S : la synthèse du tour du 26 octobre (`docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md` sur `main`,
  `4d6ddf40…`, commit `3490779`).
- E1 : la lecture de l'expérience 1, le juge v1 (`experience-1-juge/lecture-experience-1-v1.md`, `d3036f4e…`).
- E2 : la lecture de l'expérience 2, le nul des filles v2 (`nul-des-filles-v2/lecture-experience-2-v1.md`, `1aeeb5d0…`).
- D4 : la lecture des démonstrations du cycle v4 (`demonstration-cycle-v4/lecture-demonstration-cycle-v4-v1.md`,
  `985300f8…`) et le LISEZMOI de l'orchestrateur v5 (`orchestrateur-pole-v5/LISEZMOI-orchestrateur-pole-v5-v1.md`,
  `6c8cc598…`).
- D : le devis du premier lancement réel (`premier-lancement-reel/devis-premier-lancement-reel-v1.md`, `aabfc2e6…`).
- N : la décision N-053 sur `main` (`docs/decisions/decision-N-053-v1.md`, `2204256d…`) : fuite textuelle, conscience
  d'évaluation du dispositif, juge d'une autre lignée.
- M : ma réponse de 13:13 heure de Paris à « on n'utilise pas un chercheur automatique déjà existant ? on crée le
  nôtre ? », collée par Lazar à 14:26 (`piece-M-reponse-conv-audit-1313-v1.md`, empreinte dans son `.sha256`) : à servir
  telle quelle, avec la mention « position de conv-audit, non vérifiée ».
- X : l'état de v7 au 27 octobre, 14:50 UTC — LISEZMOI v4 de `orchestrateur-pole-v7/` (empreintes dans
  `EMPREINTES-orchestrateur-pole-v7-v4.txt`) et la lecture de la démonstration « proposeur »
  (`demonstration-couche1-proposeur-v7/lecture-couche1-proposeur-v7-v1.md`, empreinte dans son `.sha256`).
- K : la contre-lecture d'aptitude du pôle par un sous-agent neuf (Fable 5.1), 27 octobre
  (`premier-lancement-reel/contre-lecture-aptitude-v1/rapport-contre-lecture-aptitude-v1.md`, `d4c6ef64…`) : partie 1
  seulement (aptitude ; absence d'un rôle de formulation, nul aveugle aux traits, ce que le juge sait juger) ; ses
  chiffres de littérature sont non opposables (R7).

Chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` sur la branche
`canal/conv-audit-n04`, sauf mention.

Liens vérifiés (pages lues le 27 octobre 2026 ; chiffres et citations non opposables tant que non vérifiés sur PDF
empreinté, R7) : https://huggingface.co/papers/2504.08066.md ; https://arxiv.org/abs/2501.04227 ;
https://www.eesel.ai/blog/google-ai-co-scientist ; https://arxiv.org/pdf/2505.13400
