# Contre-lecture du différentiel v68 → v69 du code du pilote MR-2 — v1

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), le contre-lecteur du code v68, repris avec son contexte (session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`). Je n'ai écrit ni le code, ni le texte, ni la mesure. Réserve de lignée inchangée (même
  maison que le développeur ; Fable 5.2 est proposeur du pilote).
- **Demande** : message de la mère (contre-lecture du différentiel, neuf points) ; mêmes interdits et écarts que ma consigne
  d'origine (`11c4141a…`). Consigne des corrections lue : `consigne-developpeur-code-pilote-corrections-v1.md`,
  `20c8384a74213c5f719cdfe69e07350bcfa4dacf9268be0d9229eced520cd5b0`, égale à son compagnon.
- **Heures** (`date -u`, 13 novembre 2026) : début 15:23:58 ; 88 essais 15:24:26 à 15:26:39 ; cinq mutations neuves 15:29:26 à
  15:42:52 ; N8 et M34 rejouées 15:42:52 à 15:46:35 ; épreuves directes 15:46:43 ; essai à blanc A et épreuve X9 15:47:02 à
  15:48:15 ; fin : dernière ligne.
- **Aucune dépense, aucun appel de modèle, aucune clé lue.** Réseau : la seule boucle locale (relais à amont factice, doublures
  des essais, une doublure d'amont déclarée par mon outil avec une clé factice). Tous mes lancements sous `env -i` : aucune
  variable de l'environnement réel n'a atteint un essai. Un processus de calcul à la fois, `ulimit -v 6000000`,
  `OMP_NUM_THREADS=2`. Aucune écriture git ; un clone en lecture neuf (`organisme-v69`) dans mon bac à sable. Aucun
  `git status` sur l'arbre du développeur. Aucun refus de permission ni de classifieur.

## 0. Verdict

**Autorisable après corrections.** Les deux bloquants et les dix majeurs de la v68 sont corrigés pour de bon, à trois réserves
près (M-5, M-7, m-12, ci-dessous). La partie neuve la plus sensible tient à la lecture : clé par son nom, environnement filtré,
adresses figées, aucun repli de modèle, aucun `ANTHROPIC_BASE_URL`, corps de Claude exact. **Mais cinq constats majeurs neufs**
demandent un petit code v70 et une sonde avant le scellement du texte : 0 bloquant, 5 majeurs, 8 mineurs. Deux des majeurs
changent un fichier gelé ; le bloc `7aa62798…` est donc encore provisoire.

Mes cinq mutations neuves, placées là où je ne voyais pas d'artefact, **survivent toutes** aux 88 essais (cinq trous de R5, pas un
taux). N8 et M34, rejouées par le banc du développeur, sont tuées pour la raison attendue.

## 1. Intégrité (conforme)

| contrôle | résultat |
|---|---|
| livrables v69 (rapport `c396ec43…`, paquet `89aa20ba…`, patch `4ea88233…`, différentiel `4721f53c…`, bloc `7aa62798…`, journal `86a94224…`, bancs `06405c78…` et `cc41e675…`) | égaux à leurs compagnons |
| branche du dépôt de travail du développeur | tête `bf92eb6dec81c62c22907f8e8e36906b4e05a899` |
| `git bundle verify` | tête `2ca17ea3243979837890e1243876299a202b7748`, exige `276b6afd…` |
| patch | égal à l'octet à `git format-patch --stdout 276b6af..2ca17ea` que je recalcule |
| différentiel | **égal à l'octet** à celui que je recalcule (`git diff --no-index`, neuf paires de fichiers) |
| ajouts seulement | `git diff --name-status 276b6af 2ca17ea` : neuf « A », aucune modification de la v68 |
| bloc gelé contre les fichiers | 27 lignes, 27 « OK » ; `bloc` rend `7aa62798…` ; gabarit recalculé `e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2` |
| code gelé entre les deux commits v69 | identique (`616d9e8` → `2ca17ea` ne change que les essais et le banc) |

Remarque : le passage entier du banc (88 mutations) a tourné avant la correction de l'essai du rapatriement ; N8 y survivait ;
seules N8 et M34 ont été rejouées après. Dit par le développeur, exact.

## 2. Ce que j'ai fait par moi-même

- **88 essais** dans mon clone, sous environnement vidé : `88 passed, 112 subtests passed in 132.64s`
  (`contre-lecture-code-v69-outils/essais-88-contre-lecteur-v1.txt`, `c7960798…`).
- **N8 et M34** rejouées par le banc du développeur : toutes deux « tuée (raison attendue) », essai `test_rapatriement_artefacts`
  (`n8-m34-rejouees-par-le-contre-lecteur-v1.json`, `318f3911…`).
- **Essai à blanc A** rejoué par la ligne de commande : 16 complets ; `CARTES.json` `d61dfc80…` et corps de la mesure
  `78d30796…`, égaux à ceux du développeur ; `mesurer` une seconde fois : refus, code 2 ; `lire` : P-2 avec réserve R-1, écarts
  nuls ; rapatriement : 110 copies, 6 laissés (`prive/`), aucun monde ; mode réel : refus (numpy 2.4.6 ≠ 2.5.3), rien créé.
- **Cinq mutations neuves sur le code neuf**, suite entière à chaque fois (`mutations_contre_lecteur_v69_v1.py` `df7e9452…`,
  résultat `mutations-contre-lecteur-v69-v1.json` `d4574f05…`) :

| # | garde mutée | où (v69) | issue |
|---|---|---|---|
| W1 | l'environnement **entier** du lanceur passe au relais (filtre supprimé) | `proposeurs_pilote_v69.py` l. 278 | **survit** |
| W2 | l'engagement ne lie plus le fichier des mondes (le texte seul) | `pilote_mr2_v69.py` l. 886 | **survit** |
| W3 | témoin : consigne lue par la commande non comparée au texte servi | `proposeurs_pilote_v69.py` l. 245 | **survit** |
| W4 | relecture du texte servi : gabarit non comparé au gabarit gelé | `pilote_mr2_v69.py` l. 735 | **survit** |
| W5 | `mesurer` : manifeste différent de son compagnon admis | lanceur l. 299 | **survit** |

- **Épreuves directes** (`epreuves_contre_lecteur_v69_v1.py` `e6b0df05…`, sortie `7682d360…` ; `epreuve_mesure_autres_mondes_v69_v1.py`
  `24f78d06…`, sortie `6a16ccb1…`), citées X1 à X9.

## 3. Constats majeurs

**D-1 — La règle des graines écrite au manifeste est fausse, et les épisodes servis ont changé sans qu'on le dise.**
Où : `pilote_mr2_v69.py` l. 86 (`ETIQUETTE_EPISODES = "pilote-mr2-v69|episodes-developpement"`) ; lanceur l. 65 (`REGLE_DES_GRAINES`
dit « pilote-mr2-v68|episodes-developpement| ») ; rapport v69, section 6 (« étiquette héritée de la v68, gardée pour que les épisodes
ne changent pas »).
Preuve : X1, sur les quatre mondes de développement : les épisodes servis égalent ceux de l'étiquette v69, **pas** ceux de
l'étiquette v68 ; les empreintes des épisodes des manifestes versés diffèrent entre l'essai à blanc v68 et v69 pour les quatre
mondes. Le manifeste (R9) et la phrase proposée pour le texte décrivent donc une dérivation qui ne redonne pas les épisodes.
Correction : choisir (étiquette v69, la plus simple) et écrire la même chaîne au code, au manifeste et au texte ; essai qui
recalcule les épisodes depuis la règle écrite. Change un fichier gelé.

**D-2 — Astra : la réflexion est comptée deux fois, et un « coût au-dessus du pire cas » abandonne le proposeur.**
Où : commande l. 140 (sortie = `completion_tokens` + `reasoning_tokens`), l. 231 (cause `cout_excessif`) ; relais l. 114 ;
`proposeurs_pilote_v69.py` l. 34 (`cout_excessif` parmi les causes d'abandon).
Preuve : X2. Une réponse valide (30 000 jetons facturés, dont 25 000 de réflexion, sous la borne de 36 000, carte lisible) est lue
55 000 jetons, 2,95 USD contre un pire cas de 2,30 : **« échec », cause `cout_excessif`, abandon d'Astra**. Si le fournisseur
compte déjà la réflexion dans `completion_tokens` (ce que je crois de mémoire, non vérifié), toute réponse à longue réflexion
est jetée et les appels restants sont perdus. Le collisionneur ajoute aussi la réflexion, mais seulement pour compter haut ; il
ne jette rien.
Deux choses distinctes : (a) l'abandon sur coût excessif n'est pas dans la décision de la mère sur Q-8 (modèle servi différent,
usage absent) ; c'est un ajout du développeur, à décider ; (b) la règle de comptage ne peut être fixée qu'après la sonde.
Correction : la sonde tranche (un mot en réponse : `completion_tokens` ≈ réflexion + 1 si elle y est comprise) ; champ gelé à la
configuration (« réflexion comprise : oui / non ») ; tant que ce n'est pas tranché, aucune réponse rendue sous la borne ne doit
devenir un échec. Même question pour Argon (`thoughtsTokenCount` et la borne `maxOutputTokens`).

**D-3 — `mesurer` ne lie pas les mondes mesurés à ceux du manifeste.**
Où : lanceur l. 306 (`charger_mondes_prives(args.mondes, args.mondes_sha256)` : le fichier contre l'empreinte tapée, rien contre
le manifeste) ; `lire` ne compare pas `mondes_sha256` de la sortie à ceux du manifeste.
Preuve : X9. Après un essai à blanc sur les mondes de développement, `mesurer` lancé avec un autre fichier de quatre mondes
publics d'essai rend le code 0, et `lire` aussi ; les mondes mesurés diffèrent de ceux du manifeste. M-5 est donc corrigé pour
les cartes, pas pour les mondes.
Correction : `mesurer` exige l'empreinte du fichier égale à `controles.mondes.fichier_mondes_sha256` du manifeste ; `lire`
exige les `mondes_sha256` de la sortie égaux à ceux du manifeste ; un artefact chacun.

**D-4 — Plus rien dans le code n'attend une confirmation, alors que cinq faits restent à vérifier ; la voie de Claude n'a jamais
lu un vrai flux.**
Où : configuration v10 (champ « a_confirmer » retiré, remplacé par un texte « sources … À vérifier par la sonde ») ; relais
l. 121-159 (`lire_flux_anthropic`) ; doublure des essais (`test_pilote_mr2_v69.py` l. 1168-1233, écrite par le développeur du
lecteur de flux).
Ce qui reste non vérifié : prix de Claude (table en cache), prix d'Argon et d'Astra (« supposés »), réflexion comprise ou non
(D-2), besoin d'un en-tête d'espace de travail, forme réelle du flux (usage final dans `message_delta`, événements, raison
d'arrêt), bornes de 64 000, 89 000 et 36 000 admises. La consigne des corrections demandait « plus aucun à confirmer » : le champ
a disparu, pas l'incertitude. Le plafond n'est dur que si les prix sont les vrais.
Correction : la sonde (section 6) **avant** le scellement, son relevé scellé cité au texte ; le mode réel exige l'empreinte de
ce relevé (champ de la configuration, donc au bloc).

**D-5 — Cinq gardes neuves sans artefact (R5).**
W1 à W5 survivent. La plus sérieuse : W1 — le filtrage de l'environnement du relais, cœur de « clés par leur nom », n'a aucun
essai qui regarde ce que le relais reçoit ; X2 montre que le code fait bien le filtrage (seuls `LANG`, `PATH`, `RELAIS_JETON` et
la clé du proposeur passent ; ni les autres clés, ni `ANTHROPIC_BASE_URL`, ni `OPENAI_BASE_URL`), mais rien ne le garde. Aussi
sans artefact à ma lecture : la condition « session neuve » du témoin, le « monde public » du texte servi.
Correction : un artefact par garde ; rejouer W1 à W5, attendues tuées.

## 4. Constats mineurs

- **d-1** Le manifeste porte `recrite` par monde et par loi (`pilote_mr2_v69.py` l. 707) : il dit quels mondes ont une loi hors de
  ±4. Même esprit que M-3 : à garder dans les contrôles privés.
- **d-2** Délai de l'adaptateur : l'appel est compté 0 USD (X8 ; `proposeurs_pilote_v69.py` l. 215), alors que l'amont a pu
  facturer. Compter le plafond de session ; le rapprochement des coûts le montrera sinon.
- **d-3** Flux : un second `message_delta` sans raison d'arrêt écrase la première (X6 : `stop_reason` nul, donc « raison
  inconnue ») ; le délai d'amont vaut par lecture, pas pour le flux entier (la commande et l'adaptateur tiennent le délai total).
- **d-4** `CARTES-partiel.json` n'est pas dans la liste des noms rapatriés (`audit_pilote_v69.py` l. 27) : après un arrêt, il
  reste sur la machine (les réponses brutes, elles, sortent).
- **d-5** Le refus « aucun scénario factice » en mode réel tombe après la création du dossier de sortie (lanceur l. 219-220) ;
  à remonter dans `exiger_mode_reel`.
- **d-6** M-1 : huit chiffres quelconques passent pour une date (`gpt-6-astra-99999999` admis, X3). Rien de plus large qu'un
  suffixe de date en forme ; suffisant.
- **d-7** Un fichier au nom permis portant une loi compilée ou une graine est toujours copié (m-13 corrigé pour le contexte
  servi seulement). Aucun chemin du code gelé n'en écrit.
- **d-8** Rapport : pire cas de la sonde 7,98 USD et non 7,97 (7,975968) ; le reste des chiffres est exact.

## 5. Les neuf points de la demande

**(2) Constats de la v68, un par un.**

| constat | jugement |
|---|---|
| B-1 | corrigé : voie écrite et branchée, plus aucun refus sur « à confirmer » ; reste D-4 (jamais éprouvée sur un vrai flux) |
| B-2 | corrigé : relais lancés par le lanceur, état contrôlé champ par champ, `appelant == dialecte` et clé présente en mode réel, adresse figée, mode réel de bout en bout sur doublure avec dix artefacts |
| M-1 | corrigé (X3) ; abandon au premier modèle non conforme |
| M-2 | corrigé : statut et type seulement ; motifs d'identifiant au rapatriement |
| M-3 | corrigé ; reste d-1 |
| M-4 | corrigé (trois artefacts) |
| M-5 | corrigé pour les cartes, une seule fois vérifiée par moi ; **reste D-3** pour les mondes |
| M-6 | corrigé : textes servis gardés dans `prive/`, relecture, contrôle des épisodes, liste des refusées |
| M-7 | corrigé pour les versions et le commit ; **règle des graines fausse (D-1)** |
| M-8 | corrigé : pire cas calculé par le relais, borne refusée au-dessus de la sienne |
| M-9 | corrigé du côté de la consigne servie ; le texte doit écrire la règle |
| M-10 | corrigé pour les gardes citées ; reste D-5 |
| m-1 à m-7, m-9 à m-11, m-13 | corrigés (m-7 : d-2 ; m-13 : d-7) |
| m-12 | corrigé à la lettre, mais ouvre D-2 |
| m-8 (en partie), m-14 | **refus fondés** : le texte dit « aucune reprise » ; la mesure est scellée. Les deux restent à dire à Lazar |

**(3) Partie neuve sensible.** Voie de Claude : `POST https://api.anthropic.com/v1/messages`, `x-api-key`, `anthropic-version`,
corps `{model, max_tokens, stream, messages, output_config}` et rien d'autre (vérifié par l'essai sur doublure et par lecture) ;
aucun `thinking`, aucun `fallbacks`, aucun en-tête bêta, aucun `ANTHROPIC_BASE_URL` (recherche dans les sept fichiers : zéro) ;
clé lue par le nom passé en argument, jamais sur la ligne de commande (X2). Reconstitution du flux : juste sur les formes
essayées ; fragile sur d-3. Lancement des relais : environnement bâti par filtrage (dix noms, plus le jeton et la clé du
proposeur) ; non gardé par un essai (W1). `/relais/etat` : complet. Adresse d'Astra : figée, `https`, hôte exact ; X7 : variantes
refusées. Règle M-1 : X3, d-6.

**(4) Q-2 (d).** Conforme à la décision. Chaque feuille softmax hors de ±4 devient `transformee{base: softmax/g, puissance: g}` ;
égalité vérifiée à 10⁻⁹ sur le jeu factice et 2 000 instances de l'oracle ; la loi récrite repasse le gardien entier ; C-16 ne
s'arrête que si g > 50, si la loi récrite est refusée, ou si elle n'est pas équivalente. Cas sain (le monde public qui arrêtait
la v68) et deux artefacts, passés chez moi. Ni la famille, ni le gardien, ni la mesure ne changent. La K1 servie passe telle
quelle, sans réécriture : juste.

**(5) Q-1, Q-4, Q-8.**
- Q-1 : 64 000 / 89 000 / 36 000 / 36 000 ; plafonds 3,00 / 2,00 / 2,34 / 2,34 ; parts 12 / 8 / 9,36 / 9,36 ; π1 20,00 ; π2 21,72 ;
  **total 41,72** (X4). Aucun « 19 » ni « 39 » en dur hors des artefacts d'essai.
- Q-4 : `output_config.effort = "high"` envoyé à Fable 5.2 et à Opus 5.5 ; rien à Argon ni à Astra. **C'est bien ce que fait le
  collisionneur** : `EFFORT = "high"` (l. 136), envoyé par `appeler_anthropic` seul (l. 433) ; `appeler_gemini` n'envoie que
  `contents` et `generationConfig.maxOutputTokens` (l. 453-454) ; `appeler_openai` que `model`, `messages`,
  `max_completion_tokens` (l. 568-570) ; le journal consigne l'effort « None » hors Anthropic (l. 716). Une limite : le
  collisionneur a éprouvé Fable 5.1 et Opus 4.6, pas Fable 5.2 ni Opus 5.5.
- Q-8 : refus du modèle sans abandon ; modèle servi différent et usage absent avec abandon : appliqué. En plus, non décidé :
  abandon sur coût excessif (D-2).

**(6)** Section 2.

**(7) La doublure ne s'active-t-elle que par les essais ?** Pas mécaniquement. Elle s'active par la **configuration** : une
adresse `http://127.0.0.1:PORT/…` est admise par `lire_configuration` (l. 99) et par le relais (l. 78-79), et l'état du relais
passe alors le contrôle du mode réel (X2 : aucun écart). Ce qui l'empêche dans la vraie course : le mode réel n'accepte que la
configuration de l'arbre (lanceur l. 180), dont l'empreinte est au bloc du texte scellé ; il faut donc un texte forgé, son
empreinte et un engagement des mondes refait. Le manifeste dit `amont_boucle_locale`. Jugement : suffisant contre l'accident ;
à durcir à peu de frais : `lire` recopie ce drapeau et le mode du manifeste devient « réel sur doublure ».

**(8) La sonde.** Section 6.

**(9) Ce que le texte doit changer (section 6 du rapport v69).** Exacte sauf une ligne ; incomplète sur sept points.
- **Fausse** : la dérivation de la graine des épisodes (D-1).
- **Manquent** : (a) numpy 2.5.3 exigé par le mode réel, à écrire aux préalables (la machine doit l'avoir) ; (b) le plan
  d'analyse, étape 2, et la ligne de commande de « Métrique » : la mesure se lance par `pilote_mr2_v69.py mesurer` ; (c) l'ordre :
  `generer --texte` et son engagement, empreintes des mondes du registre passées à `jouer`, registre des lancements ; (d) la
  version du code citée (« code v68 gelé » à la ligne P-2, « chaîne v67 ») ; (e) l'isolement : un relais par proposeur, lancé par
  le lanceur, jeton du lancement ; (f) la sonde : préalable, ligne de dépense, relevé cité ; (g) l'abandon sur coût excessif, s'il
  est gardé (D-2), et le risque de P-0 sur une erreur passagère (m-8).
- Le reste est juste : C-5, C-16, liste d'arrêt, phrase sur l'effort, règle d'extraction, limite du plafond dur, 41,72 USD,
  textes servis gardés pour l'audit R4.

## 6. La sonde payante

**Ce qu'elle doit vérifier, par relais** (ce que liste le développeur est juste ; j'ajoute les trois derniers) : statut ;
identifiant servi exact ; raison d'arrêt ; champs d'usage présents et entiers ; bornes gelées admises ; `output_config.effort`
admis sans en-tête bêta ; besoin d'un en-tête d'espace de travail ; Fable 5.2 servi sur ce compte ; prix contre la console (lu
par Lazar) ; **le flux réel relu par `lire_flux_anthropic` et comparé au flux brut** (usage final, événements) ; **réflexion
comprise ou non dans la sortie comptée** (Astra, Argon) ; **un second appel à borne courte** (256 jetons, texte long demandé) :
raison d'arrêt « tronqué » de chaque dialecte, et la réflexion tenue ou non sous la borne — c'est ce qui rend le plafond dur.

**Pire cas** (consigne de 100 octets) :

| | borne gelée | borne de 256 | somme |
|---|---|---|---|
| Fable 5.2 | 2,568992 | 0,019232 | 2,588224 |
| Opus 5.5 | 1,784496 | 0,009616 | 1,794112 |
| Argon | 1,811240 | 0,024040 | 1,835280 |
| Astra | 1,811240 | 0,024040 | 1,835280 |
| **total** | 7,975968 | 0,076928 | **8,052896** |

Soit 4,39 USD au pire sur crédits de Claude et 3,68 hors crédits ; attendu : quelques centimes.

**Où l'écrire.** Avant le scellement, pas après : son résultat peut changer la configuration (comptage de la réflexion, en-tête
d'espace, prix), donc le bloc, donc l'empreinte du texte dont dérivent les graines. Elle ne lit aucun monde et aucun résultat :
elle n'est pas sous R1. Elle ne peut pas passer sous π1 ni π2, qui exigent le texte scellé : **deux lignes à part** (crédits
4,39 ; hors crédits 3,68), nœud de Lazar. Au texte : un préalable (« sonde des quatre relais faite, relevé scellé, empreinte
citée ») et une ligne du devis, hors des 41,72. Il lui faut une sous-commande du lanceur (aucune n'existe ; lancer les relais
à la main défait « clés par leur nom ») : à écrire dans la v70, avec la borne courte en option.

## 7. Ce que je n'ai pas vérifié

Le banc des 88 mutations (lu, non rejoué, sauf N8 et M34) ; la génération des mondes ; l'essai à blanc B (lu) ; le journal masqué
du collisionneur cité par le développeur (non nommé par ma demande, non ouvert) ; toute route réelle ; les faits d'interface des
fournisseurs au-delà du dépôt et de la table locale en cache ; les registres et R-2534.

Fin de la rédaction : 2026-11-13 15:50:25 UTC (`date -u`).
