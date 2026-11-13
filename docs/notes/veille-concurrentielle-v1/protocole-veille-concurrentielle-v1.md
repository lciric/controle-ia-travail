# Protocole de veille concurrentielle par pièce — v1

- **Écrit** le 13 novembre 2026, commencé à 18:53:54 UTC, achevé à 19:18:16 UTC (heures relevées par `date -u`).
- **Rédacteur** : sous-agent neuf (Claude Opus 5.5), lancé par la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Il n'a écrit
  ni le programme, ni la synthèse de niveau 3, ni les décisions N-067 à N-070, ni aucun rapport de lecture.
- **Mandat** : mots de Lazar R-2562 et R-2563 (`registres/decisions.md`, l. 2521 et 2522 : « go les deux demandes »). Demande
  reformulée qui fait foi : veille par équipe sur flux bruts, sous protocole scellé avant la première requête, double lecture
  aveugle, fourchettes de sortie, délai réel du programme, regret attendu, décision par pièce, rétro-test au 1er octobre et
  prédictions datées. **Phase 1 seulement** : ce protocole.
- **Statut** : écrit et scellé **avant toute requête réseau**. Pour l'écrire : aucune requête, aucune dépense, aucune écriture
  git, aucune lecture des chemins interdits (section 10). Avant la première requête, il est **contre-lu par un sous-agent neuf
  (R2)**, à qui la mère donne ce fichier et la liste de la section 0.3 ; toute correction va dans une v2 (R12), et seule la
  version contre-lue et scellée autorise la phase 2.

## 0. Cadre

### 0.1 Règles de lecture
1. « Libre » veut dire « non trouvé dans les pièces lues », jamais « trou du champ » (R8). Une zone libre séduisante est
   vérifiée plus durement, pas moins.
2. Aucun chiffre sur un travail d'autrui sans PDF empreinté et page (R7) ; pour un billet, numéro de ligne du rendu texte
   archivé et empreinté, noté « l. ». Un résumé d'interface, un contexte de citation de Semantic Scholar, une sortie de modèle
   sont des **pistes**, jamais un verdict.
3. Les chiffres de ce protocole qui ne viennent pas d'un fichier du dépôt sont marqués **« a priori »** (choisis sans donnée,
   avant toute requête) ou **« hypothèse de volume »** (à remplacer par un décompte gratuit avant toute dépense).
4. Le protocole s'applique **deux fois, avec les mêmes règles** : d'abord le **rétro-test** (date de coupe
   t0 = 2026-10-01T00:00:00Z, section 8), puis la **veille vivante** (t0 = heure de lancement de la phase 2). Le rétro-test est
   mené, scellé et comparé à sa liste de référence **avant** toute lecture d'un élément du corpus vivant daté après le
   30 septembre 2026.
5. **Aucun paramètre n'est réglé après la lecture d'un résultat du rétro-test.** Tout changement passe par une v2 de ce
   protocole, qui rapporte les résultats de la v1 tels quels (R1, R12).

### 0.2 Ce que le protocole produit, au bout de la phase 4
Par pièce : l'équipe la mieux placée, ce qui lui manque, sa fourchette de sortie et sa probabilité ; notre délai réel jusqu'au
premier résultat publiable ; le regret attendu ; une décision parmi **accélérer, tenir, mettre en sommeil, abandonner** ; le
plus petit résultat qui resterait à nous ; l'ordre des travaux et ce qui se mène en parallèle. Puis des prédictions datées,
scellées, relues huit semaines plus tard (section 9).

### 0.3 Fichiers lus pour écrire ce protocole (empreintes contrôlées le 13 novembre 2026 contre leurs compagnons)
| fichier | empreinte | usage |
|---|---|---|
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` | `e30a013d08b03e8d…` | pièces libres, liste de référence |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` | `f1580ddcedd495b5…` | resserrements de H5, H9 ; pièces non déclarables (R-2567) |
| `docs/decisions/decision-N-067-v1-brouillon1.md` … `N-070-v1-brouillon1.md` | `d83d067c…`, `76be8b44…`, `823a3c35…`, `8b52e368…` | énoncés resserrés |
| `docs/decisions/decision-N-067-v1-brouillon2.md` … `N-070-v1-brouillon2.md` | `cb3f3719…`, `414fc6b4…`, `69f8f699…`, `a7eeb395…` | écarts avec les brouillons 1 (section 1.3) |
| `docs/decisions/contre-lecture-decisions-N-067-a-N-070-v1.md` | `db44d99516973d18…` | voisins omis (2609.03035 v2, Sargsyan) |
| `docs/programme-controle-ia-v2.md` ; `docs/etat-de-l-art-controle-ia-v1.md` | `2fd63bad…` ; `a7d6846d…` (empreintes de lancement, `sha256sum -c` conforme) | énoncés d'origine ; ancrages connus au lancement |
| `docs/decisions/decision-N-013-v1.md` ; `…N-007-N-008-v1.md` ; `…N-035-v1.md` ; `…N-064-v1.md` ; `…N-065-v1.md` | `157d388e…` ; `ab7dc9bb…` ; `55df073d…` ; `387c9d4e…` ; `f820e90d…` | énoncés retenus d'origine |
| `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` | `c5465a9b…` | énoncés d'origine de HC2 et du papier B |
| `docs/notes/devis-mini-course-kimi-argon-nuit-v1/devis-mini-course-kimi-argon-nuit-v1.md` | `18e8495f…` | prix des lecteurs d'autres familles |
| `docs/notes/collisionneur-diversite-idees-v1/devis-v1.md` ; `…/depense-et-incidents-v1.md` | `1b511a8d…` ; `822cc5c6…` | coût d'un tour du collisionneur |
| `registres/decisions.md`, R-2551 à R-2568 ; `registres/depenses.md`, l. 389 | registre vivant, non scellé | mandat, liste de référence, prix public d'Argon |

---

## 1. Pièces à couvrir, découpées en éléments (point a)

### 1.1 Les sept axes et leur vocabulaire fermé
Les lecteurs extérieurs codent chaque article sur ces sept axes, **sans jamais recevoir nos énoncés** (section 4.4). Les codes
sont neutres ; plusieurs codes par axe sont permis ; chaque code porte une page.

| axe | codes |
|---|---|
| **OS — objet surveillé** | OS1 agent qui agit (états internes ou sorties de l'agent qui exécute la tâche) ; OS2 agent **auteur** d'un contenu destiné au moniteur ; OS3 agent **victime** (agit sous un contenu écrit par un tiers) ; OS4 modèle **lecteur** d'un contenu (garde, classifieur d'entrée) ; OS5 moniteur ou juge génératif lui-même ; OS6 plusieurs copies d'un même modèle ; OS7 plusieurs agents de modèles différents ; OS8 chaîne de délégation (agent vers sous-agent) ; OS9 juge **statistique** de recherche automatisée ; OS10 juge **génératif** de recherche automatisée ; OS11 proposeur d'hypothèses ; OS0 autre |
| **TA — type d'accès** | TA1 boîte noire, actions et sorties ; TA2 boîte noire avec raisonnement visible ; TA3 boîte blanche en lecture (activations, sondes, états cachés, lentilles) ; TA4 boîte blanche en écriture (activations ou poids modifiés) ; TA5 statistique calculée hors des agents par un code de confiance ; TA6 intervention non spécifique (paraphrase, rééchantillonnage, remise à zéro du contexte) ; TA0 sans objet |
| **AC — accumulation** | AC1 par action ou par étape, sans cumul ; AC2 maximum ou pic sur la trajectoire ; AC3 moyenne sur la trajectoire ou les tours ; AC4 somme cumulée ou processus e additif ; AC5 autocorrélation ou dépendance temporelle ; AC6 coupe transversale entre agents à un instant ; AC7 statistique conjointe temps × agents ; AC8 agrégation sur les jetons d'une seule sortie ; AC0 verdict unique |
| **GA — garantie** | GA1 aucune ; GA2 seuil réglé sur données, fausses alarmes mesurées ; GA3 garantie conforme ou de type « probablement approximativement correcte » sur l'épisode ; GA4 garantie toujours valide (inégalité de Ville, processus e, martingale) ; GA5 durée moyenne avant fausse alarme ; GA6 contrôle des comparaisons multiples ; GA7 engagement scellé par empreinte avant les données ; GA8 nul formé des lois connues (archive, facteurs connus, englobement) ; GA9 borne ou théorème (puissance, impossibilité) |
| **ME — menace** | ME1 sabotage diffus : aucune action prise seule n'est étiquetable ; ME2 sabotage d'agent étiquetable par étape ; ME3 sous-performance volontaire ; ME4 collusion ou coordination entre agents ; ME5 attaque par le contenu sur un moniteur (flatterie, autorité, approbations forgées, usurpation de style, ordres en bande) ; ME6 injection par un tiers ; ME7 évasion de sonde par consigne ou contexte ; ME8 évasion par écriture dans les activations ou les poids, ou par optimisation ; ME9 proposeur ou générateur qui optimise contre un juge ; ME10 perte d'une contrainte à la délégation ; ME11 adversaire adaptatif qui répartit un budget dans le temps ou entre agents, ou préserve les marginales ; ME0 aucune |
| **CA — cadre** | CA1 évaluation de contrôle (moniteur de confiance, équipes rouge et bleue) ; CA2 banc d'agents à outils ; CA3 tâches floues à vérité différée ; CA4 pipeline de code à plusieurs rôles ; CA5 recherche automatisée ou découverte d'hypothèses ; CA6 conversation sans outil ; CA7 théorie ou simulation seule ; CA8 garde ou classifieur de production |
| **EC — échelle** | champs chiffrés, chacun avec sa page : plus grand modèle à poids ouverts lu (milliards de paramètres) ; modèles d'interface employés ; nombre d'agents (min–max) ; horizon (pas ou tours, max) ; nombre d'épisodes ou d'essais |

### 1.2 Règle d'appariement d'un article à une pièce
Chaque pièce a une **signature** : une valeur exigée sur certains axes (section 1.3), et une **forme de résultat** (comparaison,
loi, théorème, prédiction, courbe). Pour un article codé, le script calcule par pièce
`c = moyenne, sur les axes exigés, de 1 (code exigé présent), 0,5 (code « voisin » listé pour cet axe), 0 (sinon)`.
Un couple (article, pièce) passe au **jugement par pièce** (section 4.3) dès que `c ≥ 0,5` selon le codage de **l'un ou l'autre**
lecteur. Le jugement par pièce, qui seul fait foi, emploie l'échelle de la synthèse : **occupe**, **occupe en partie** (avec la
liste des axes couverts, page par page), **voisin**, **ne touche pas**. La forme du résultat ne se juge qu'à cette étape.

### 1.3 Pièces de la veille vivante (énoncés courants)
Sources : synthèse de niveau 3 (sections 2 à 5) ; brouillons 1 de N-067 à N-070, comme demandé. **Écarts des brouillons 2**
(R-2568), repris ici sans changer de pièce : HC2 précise « en fonction de l'intensité de l'attaque » et cite 2609.03035 v2
(p. 8, 29) comme comparaison sonde contre juge sous simple avertissement ; O4 et O2 ne sont déclarés libres publiquement
qu'après lecture de SSRN 6569258, sinon avec réserve écrite. **Règle** : la phase 2 lit la version scellée la plus récente de
chaque décision (finale si elle existe) et consigne, avant toute requête, tout écart avec les signatures ci-dessous ; un écart
qui change une signature est une v2 de ce protocole.
« Cédé » = déjà publié selon la synthèse ; un article qui ne couvre que du cédé ne compte pas comme collision.
« V » = valeur par défaut (section 7.1). « Décisions permises » : toutes les quatre, sauf mention.

**Papier A — le temps**

- **A-H1** (programme l. 93 ; synthèse § 2 ; R-2567 : « à fausses alarmes égales et à agrégation égale »). Signature :
  OS1 · TA3 **et** TA1 ou TA2, comparés · même AC des deux côtés, sur la trajectoire · GA2 à 1 % de fausses alarmes, égales
  entre bras · **ME1** · **CA3** (CA1 voisin) · modèle ouvert lu ≥ 7 milliards. Forme : comparaison. Cédé : le gain en général ;
  le gain par étape sur sabotage étiquetable (2610.12445). V = 1.
- **A-H2** (N-007, l. 28). Signature : OS1 contexte privé compris · TA3 · **AC4** · **GA4**, seuil calibré sur épisodes honnêtes
  sans exemple de sabotage · ME1 sous un seuil par action à 1 % (ME11 voisin) · CA1 ou CA3 · horizon variable. Forme : rappel
  qui croît avec l'horizon. Cédé : squelette séquentiel en boîte noire ; somme cumulée sur états internes sans garantie
  (SafeDream). V = 1.
- **A-L** (N-004 ; programme § 3). Signature : TA3 (scores de sondes) · AC4 (processus e de mélange) · GA4 et **GA9** (borne
  fonction du seul budget total ; invariances exactes dans le temps et entre agents) · ME11 à budget total borné · CA7 puis
  mesure. Forme : théorème et mesure. Cédé : cœur statistique classique. V = 1.
- **A-T** (N-003). Signature : TA3 (mesure sur activations) · AC5 contre AC2, AC3, AC4 · GA9 (classes « multi-ensemble » et
  « marginales », impossibilité par rebrassage sur un groupe, garanties des statistiques locales) · ME11 à marginale préservée
  · écriture commune temps et agents (AC7). Forme : théorème. Cédé : contraste en boîte noire pour un agent (2606.10456). V = 1.
- **A-H6** (N-013 l. 78 ; N-015). Signature : OS1 · TA6 (paraphrase, rééchantillonnage, remise à zéro ; bruit d'activations
  mesuré, non revendiqué) · ME1 ou ME2 · CA1. Forme : succès d'attaque contre utilité honnête selon l'intensité. Cédé : bruit
  sur les poids. V = 1.
- **A-Tr** (programme l. 98). Signature : OS1 · TA3 · AC2 ou attention, au niveau de l'action et de la trajectoire, avec AC4 ·
  ME8 par apprentissage par renforcement au niveau de l'action · CA1 ou CA2. Forme : tenue de la robustesse. V = 1.
- **A-H8** (programme l. 99). Signature : OS1 · TA3 · ME7 ou ME8. Forme : **prédiction** de la robustesse adverse par un
  construit mesuré d'abord (intention contre conscience d'évaluation). Cédé : le socle (ce que lit la sonde décide où elle
  échoue ; lien construit → tenue hors distribution). V = 1.

**Papier B — l'essaim**

- **B-POP** (N-069 brouillon 1, § 4, point 1). Signature : OS6 avec OS1 (scores de sondes de l'agent qui agit, entre copies) ·
  TA3 · AC6 ou AC7 sous forme de **montée conjointe** · GA2 à fausses alarmes égales, **à sonde égale**, contre le pic et
  l'agrégation par agent · ME4 coalition de taille inconnue > 2 **et** ME1 · CA4 · nombre d'agents ≥ 3. Forme : comparaison
  avec contrôles de construit. Cédé : score de paire sur états internes (J-PACT) ; balayages de sous-groupes sur sondes
  (2611.10620) ; coupe transversale (NARCBench). V = 1.
- **B-ST** (N-069, § 4, point 2 ; E3.1). Signature : OS6 · TA3 · **AC7** · **GA4 tenue sous dépendance** · ME11 et ME1, sous le
  seuil par action · CA4 ou CA1 · horizon long. Forme : **démonstration** de supériorité sur le séquentiel par agent et la
  coupe transversale, à fausses alarmes égales, sous adversaire. Cédé : squelette en boîte noire (2601.05427 ; 2605.11135) ;
  forme de la grille (2611.10620). V = 1.
- **B-H3** (programme l. 111 ; synthèse § 3). Signature : OS6 ou OS7 · TA3 **et** TA1 · ME4 ou ME1 · CA1 ou CA4 · nombre
  d'agents variable. Forme : **deux courbes sécurité(N) à budget total constant**. Cédé : courbes en boîte noire. V = 1.
- **B-H4′** (programme l. 112). Signature : OS6 en variantes (personas, réglages fins) · TA3 · ME4. Forme : compromis
  décorrélation des signatures internes contre capacité de coordination, chiffré. V = 1.
- **B-H5** (N-013 l. 84 ; R-2567 B3). Signature : panel de moniteurs à sondes · TA3 · ME7 ou ME8 transférée. Forme : **loi** de
  la sécurité selon le nombre de moniteurs, par la seule diversité effective. Cédé : la matrice de transfert d'attaque, hors
  et sous attaque (2604.13386 ; 2609.36490, p. 8) ; le résultat sur des juges (2608.16190). V = 1.
- **B-H7** (N-013 l. 85). Signature : ME11 adaptatif · CA1. Forme : **prédiction** de la pente d'adaptation de l'équipe rouge
  par l'information mutuelle (fuite) ; politiques de riposte comparées. Cédé : mécanisme et comparaison de politiques. V = 1.
- **B-H9** (N-070 ; R-2567 B1). Pas de revendication. Questions surveillées : moniteur qui lit chaque passation, croisé avec la
  profondeur ; **taux conditionnel par relais sur chaînes linéaires à tâche égale, pour la force graduée d'une contrainte** (le
  profil par rang de relais est publié : MasDrift, tableau 18, p. 23) ; érosion sous un agent qui sabote ; lecture interne du
  sous-agent (hors énoncé). Signature : OS8 · ME10 · CA4. V = 0,3. Décisions permises : tenir, mettre en sommeil, abandonner
  (accélérer demande une décision nouvelle de Lazar).

**Papier C — l'instrument**

- **C-HC1** (N-013 l. 20 ; N-005). Signature : OS5 · TA1 ou TA2, face à TA3 · ME5 par famille · CA1. Forme : **destination libre**
  testée contre la cible de l'attaquant et contre la moyenne du corpus, par régression sur plusieurs intensités, par famille ;
  opposition juge contre sonde. Cédé : forme à destination imposée, phénomène, probabilité du jeton. V = 1.
- **C-HC2** (N-068, § 4). Signature : **OS2** · TA3 face aux juges TA1 ou TA2 sous les mêmes attaques · plusieurs AC dont AC2 ·
  ME5 ou ME7 écrite par l'agent auteur · CA1. Forme : déplacement continu g en fonction de l'intensité, en plan apparié,
  comparé au g des juges. Cédé : absence d'évasion à seuil sur un agent victime (MIRAGE) ; plan apparié en soi. V = 1.
- **C-HC2b** (N-013). Signature : OS2 · TA3 · ME5. Forme : le score de sonde monte quand l'agent tente de manipuler, contrôlé
  contre le style. V = 1.
- **C-HC3** (N-013 l. 38-40). Signature : OS5 · ME5 (ordres en bande sous « contenu = données » ; usurpation stylistique sans
  ordre) · CA1 ; versant sonde : OS2, TA3. Forme : détection chiffrée des ordres en bande ; g résiduel > 0 sur juges en loi
  continue, nul sur sondes de l'agent auteur. V = 1.
- **C-HC4** (N-013 l. 48). Signature : OS5 et OS2 · régimes d'accès comparés (contexte seul, TA4) · CA1. Forme : **coût**
  juge contre sonde dans un même cadre, par régime, à durcissement égal. V = 1.
- **C-HC5** (N-013 § 4). Signature : OS5 avec OS1 ou OS2 (sondes qui lisent l'agent) · CA1. Forme : cellules juge ↔ sonde de la
  matrice de transfert ; quorum de juges et de sondes lisant l'agent ; paraphrase de confiance. Cédé : matrice entre juges,
  quorum avec moteur de règles (2610.29178). V = 1.
- **C-HC6** (programme l. 108). Signature : OS5 · ME5 optimisée · CA1. Forme : **prédiction par moniteur** de l'effondrement sous
  attaque optimisée à partir du g bénin. Cédé : le niveau de l'item (2608.12645). V = 1.

**Organisme d'idéation**

- **O-O4** (N-067 § 4, points 1 et 2). Signature : OS9 · TA5 · **GA8** · CA5, sur hypothèses écrites librement. Forme : promotion
  seulement si la prédiction scellée bat ce que l'archive prédit. Cédé : GA4, GA6, GA7 et TA5 hors des agents. V = 1.
- **O-O12** (N-067 § 4, point 3). Signature : OS9 et OS11 · ME9 avec **consigne de tromper**, **lecture de la description exacte
  du juge**, propositions libres · CA5. Forme : bras avec et sans verdicts, comparés, sur mondes tout faux. Cédé : verdicts
  servis, mondes négatifs, zéro promotion (CONFIRM). V = 1.
- **O-R1** (N-065, rôle 1, pièce propre ; R-2554). Signature : OS9 **et** OS10 sous la même attaque ME9 · CA5. Forme : gain
  continu comparé des deux juges. Cédé : la prémisse du bras « juge génératif » (2611.04556 ; 2611.00643). V = 1.
- **O-O8** (synthèse § 5). Signature : OS11 de plusieurs fournisseurs · CA5. Forme : valeur de la diversité des fournisseurs.
  V = 1.
- **O-INS** (N-067 § 4, points 4, 6, 7 ; non revendiqués). Instruments non trouvés ailleurs : tirages semés par l'empreinte de
  l'engagement (O3) ; forme « aucun verdict » de la mémoire (O9) ; mutations du code du juge (O11) ; banc de mutations du
  scellement (O17). V = 0,2. Décisions permises : tenir, mettre en sommeil, abandonner.

Soit **26 pièces** pour la veille vivante.

### 1.4 Pièces du rétro-test (énoncés d'origine)
Le rétro-test emploie les énoncés **d'avant** les resserrements, sinon il serait truqué : les énoncés courants excluent par
construction ce qui a été pris après le 1er octobre. Signatures identiques à la section 1.3, sauf :
- **B-POP d'origine** : « co-élévation d'états internes entre copies, lue par des sondes » (`anteriorite-v1.md`, l. 392) :
  OS6 · TA3 · AC6 ou AC7 · ME4.
- **B-ST d'origine** : « statistique spatio-temporelle contre séquentiel par agent seul et contre coupe transversale »
  (programme, l. 211) : OS6 · TA3 · AC7 · ME4.
- **B-H9 d'origine** (N-035, option (a)) : survie de la contrainte à chaque passage, décroissance avec le nombre de passages,
  moniteur à chaque passage ; V = 1.
- **C-HC2 d'origine** (programme, l. 103 ; `anteriorite-v1.md`, l. 233) : sonde lisant l'agent, agrégation robuste, attaque
  par contenu en boîte noire, g ≈ 0.
- **Organisme d'origine** (N-064 et table de `note-anteriorite-co-scientist-v1.md`, l. 257 à 273) : douze pièces O1, O2 (quatre
  composantes : TA5, GA7, GA8, GA6), O3 (sceau et tirages), O4, O8, O9, O10, O11 (trois gestes), O12 (forme d'origine),
  O17, O19, rôle 1 (N-065).
Soit **33 pièces** pour le rétro-test (7 du papier A, 7 du papier B, 7 du papier C, 12 de l'organisme).

### 1.5 Valeurs
V vaut 1 pour une pièce revendiquée, 0,3 pour une mesure descriptive, 0,2 pour un instrument non revendiqué (**a priori**).
Lazar peut donner ses propres valeurs avant la phase 4 (section 13, point 3) ; à défaut, ces valeurs s'appliquent et la
section 7.5 rapporte la sensibilité des décisions à V.

---

## 2. Sources brutes et requêtes exactes (point b)

### 2.0 Règles communes à toute requête
1. **Journal** : chaque requête écrit une ligne dans `docs/notes/veille-concurrentielle-v1/brut/journal-requetes-v1.jsonl` :
   heure UTC, méthode, adresse complète (sans aucun secret), code de retour, taille, empreinte du corps reçu, chemin du corps
   archivé. Le journal est scellé à la fin de chaque phase.
2. **Hôtes permis** (et eux seuls) : `export.arxiv.org`, `arxiv.org`, `api.semanticscholar.org`, `api.openalex.org`,
   `neurips.cc` (un essai, section 2.6), `huggingface.co` (un essai, section 2.7), `www.lesswrong.com` et
   `www.alignmentforum.org` (section 2.9). Tout autre hôte : refus du script, garde testée (R5).
3. **En-tête** : agent utilisateur neutre `veille-bibliographique/1.0` ; **aucun nom, aucune adresse électronique, aucune
   donnée du programme** dans une requête (pas de paramètre `mailto`).
4. **Cadence** : une seule connexion ; arXiv, une requête toutes les 3 secondes ; Semantic Scholar, une toutes les 3 secondes ;
   OpenAlex, une toutes les 2 secondes. Sur un code 429 ou 503 : attente de 30, 60, 120 puis 240 secondes, puis échec
   consigné ; **jamais** de changement d'adresse, de mandataire ou d'identité pour passer.
5. **Refus** : un refus du mandataire réseau (403) ou d'un contrôle de permissions ou d'un classifieur arrête la requête ;
   il est consigné **tel quel** et rapporté à la mère ; aucune reformulation ni aucun contournement.
6. **Dates** : toute date d'article est celle de sa **première version** (champ `published` de l'interface d'arXiv), en UTC.
   Les versions suivantes sont datées à part (champ `updated`, page `arxiv.org/abs/<identifiant>`).

### 2.1 Interface d'arXiv (métadonnées)
Pour chaque catégorie `C` ∈ {cs.LG, cs.AI, cs.CL, cs.CR, cs.MA, stat.ML} et chaque tranche de dix jours
`[D1, D2]` de 2026-09-01 à la date de lancement (tranches : 09-01→09-10, 09-11→09-20, 09-21→09-30, 10-01→10-10, …) :

```
https://export.arxiv.org/api/query?search_query=cat:C+AND+submittedDate:[D10000+TO+D22359]&sortBy=submittedDate&sortOrder=ascending&start=S&max_results=500
```
(`D1` et `D2` s'écrivent `AAAAMMJJ`, suivis sans espace de `0000` et de `2359` ; exemple pour la première tranche de cs.LG :
`…search_query=cat:cs.LG+AND+submittedDate:[202609010000+TO+202609102359]…` ; `S` = 0, 500, 1000, … jusqu'à une page de
moins de 500 entrées.) Contrôle : le champ `published` de chaque entrée doit tomber dans la tranche ; toute entrée hors tranche
est consignée et rangée par sa date réelle.
**Variante unique si l'opérateur `submittedDate` est refusé ou rend zéro** sur une tranche dont la liste (section 2.2) annonce
des entrées : moissonnage `https://export.arxiv.org/oai2?verb=ListRecords&set=cs&metadataPrefix=arXiv&from=D1&until=D2` (puis
`set=stat`), filtré sur les catégories ; le recours est consigné.
**Par identifiant** (articles manquants, ancrages, liste de référence, témoins) :
`https://export.arxiv.org/api/query?id_list=ID1,ID2,…&max_results=200` (au plus 200 identifiants par requête).

### 2.2 Listes d'arXiv (complétude)
Pour chaque catégorie `C` et chaque mois `M` ∈ {2026-09, 2026-10, 2026-11} :
```
https://arxiv.org/list/C/M?skip=K&show=2000
```
(`K` = 0, 2000, 4000, … jusqu'à épuisement). On relève le total annoncé et l'ensemble des identifiants. Tout identifiant de la
liste absent de la section 2.1 est récupéré par `id_list`. **Décompte d'écart** par catégorie et par mois, rapporté.

### 2.3 Semantic Scholar : citations en aval des quinze ancrages
**Règle de choix** (fixée pour limiter le savoir rétrospectif) : un ancrage doit être **connu du programme au lancement** — cité
par le programme v2 ou par l'état de l'art v1, deux documents du 4 octobre 2026 sous empreinte de lancement — avec une
première version au plus tard le 30 septembre 2026 ; on en prend un ou deux par groupe de pièces, en préférant la pièce la plus
proche de l'énoncé, puis la plus citée par ces deux documents, puis celle dont les citants n'ont jamais été cherchés.
**Exception unique** : l'organisme d'idéation n'existait pas au lancement ; son ancrage est POPPER, la pièce que N-064
(9 novembre 2026) nomme comme occupant et dont elle demande de lire les citants. Ce choix est fait après coup : au rétro-test,
les résultats de l'organisme sont rapportés à part, et le seuil (section 8.4) est aussi calculé sans eux, pour information.
**Le même ensemble sert au rétro-test et à la veille vivante.**

| n° | identifiant | pièce, équipe (telles qu'écrites dans l'état de l'art v1) | pièces couvertes | justification |
|---|---|---|---|---|
| 1 | 2512.07810 | Taylor et al. (institut britannique / FAR.AI), jeux d'audit de la sous-performance | A-H1, A-H8 | équipe nommée par la bascule (programme § 13) ; citants jamais cherchés (synthèse § 9, point 2 ; R-2567) |
| 2 | 2606.08892 | Terekhov et al., « Diffuse AI Control on Fuzzy Tasks » | A-H1, A-H2, A-H6 | cadre du diffus et base de l'environnement (a) ; citants jamais cherchés (mêmes sources) |
| 3 | 2606.10456 | « The Distributed Detectability Band » | A-T, A-L, A-H2 | veille du programme (§ 16) ; citants jamais cherchés |
| 4 | 2512.03109 | E-valuator (Sadhuka et al.) | A-H2, A-L | base séquentielle en boîte noire (programme § 8.3) |
| 5 | 2609.03035 | Das, Ponde, More, Gupta, « You Can't Escape Your Own Activations » | A-H8, C-HC2b, B-H7, B-H4′ | la plus citée de l'état de l'art v1 (cinq fois) ; voisin direct de HC2 (contre-lecture N-067 à N-070, 68-1) |
| 6 | 2604.01151 | NARCBench (Rose, Cullen, Kaplowitz, Schroeder de Witt) | B-POP, B-ST, B-H3 | équipe nommée par la bascule ; suites en veille (§ 16) |
| 7 | 2607.07368 | Makins, Angelini, Shams, Phuong (institut britannique / MATS) | B-H3, environnement (b) | effet de fragmentation ; équipe de l'institut |
| 8 | 2608.02698 | Ghanem et Keele | B-POP, A-L | détection de collusion au niveau de la population |
| 9 | 2607.08066 | moniteurs de contrôle déplacés | C-HC1, C-HC5, C-HC6 | porte GC ; veille du programme (§ 16) ; 2611.04556 s'en dit la suite |
| 10 | 2605.15377 | Koran et al. (Yale / SPAR), ensembles de moniteurs | C-HC5, B-H5 | quorum et diversité des moniteurs |
| 11 | 2605.27958 | Kumar, « Pressure-Testing Deception Probes » | C-HC2, C-HC2b, A-H8 | sondes de tromperie sous pression |
| 12 | 2506.14261 | Gupta et Jenner, évasion par apprentissage par renforcement | C-HC4, A-Tr | coût de l'évasion et choix des agrégations (programme § 0) |
| 13 | 2606.14037 | Kim et al., plan factoriel à trois intensités | C-HC1, C-HC6 | dose-réponse de la conformité |
| 14 | 2603.12277 | style à argument constant (N-013, précédent de HC3) | C-HC3 | seule source de l'usurpation stylistique connue au lancement |
| 15 | 2502.09858 | POPPER (Huang, Jin, Li, Li, Candès, Leskovec) | O-O4, O-O12, O-R1, O-O8 | N-064 demande « la lecture des travaux qui citent POPPER » (R8) |

**Écartés, avec raison** : Ctrl-Z 2504.10374 et les sondes d'Apollo 2502.03407 (citants attendus très nombreux, non comptés ; le champ est couvert par
les listes ; Ctrl-Z va aux semences forcées, section 2.10) ; 2506.10805, 2605.31593, 2607.02514, 2606.07054, 2601.20022, 2608.16190,
2605.26047, 2605.18549 (pièce déjà couverte par un ancrage plus proche). **Sans ancrage propre** : B-H9 (absente du lancement)
et O-O8 en partie ; elles ne sont couvertes que par les listes, limite rapportée par strate au rétro-test.
**Limite déclarée (R4)** : le rédacteur connaît la liste de référence ; la règle de choix est écrite pour la tenir à distance,
et le rétro-test rapporte ses résultats **avec et sans** ce flux (section 8.5).

Requêtes, pour chaque ancrage `ID` :
```
https://api.semanticscholar.org/graph/v1/paper/arXiv:ID?fields=paperId,title,authors,publicationDate,externalIds,citationCount
https://api.semanticscholar.org/graph/v1/paper/arXiv:ID/citations?fields=paperId,externalIds,title,abstract,authors,publicationDate,venue,contexts,intents&offset=O&limit=1000
```
(`O` = 0, 1000, … jusqu'à épuisement.) Pour l'équipe de chaque article retenu à l'étage 2 (section 5.1), par auteur `A` :
```
https://api.semanticscholar.org/graph/v1/author/A/papers?fields=title,publicationDate,externalIds,venue,authors&limit=1000
```
Le contexte de citation (`contexts`) est une piste : il oriente la lecture, il ne prouve rien.
**Ancrages vivants** (veille vivante seulement, hors des quinze, hors rétro-test) : citations en aval, mêmes requêtes, des
collisions constatées depuis le 1er octobre (section 8.3, strate 1) et de 2608.07556, 2609.27051 : le prochain rival citera
probablement la dernière collision.

### 2.4 OpenAlex (contre-contrôle des citations, affiliations)
```
https://api.openalex.org/works/doi:10.48550/arXiv.ID
https://api.openalex.org/works?filter=cites:W&per-page=200&cursor=*
```
(`W` = identifiant OpenAlex rendu par la première requête ; on suit `next_cursor`.) Usage : écart de couverture avec Semantic
Scholar, rapporté ; affiliations quand le PDF ne les imprime pas. Pour le rétro-test, **seules comptent les affiliations
imprimées dans une version antérieure au 1er octobre**.

### 2.5 Soumissions d'ICLR 2027 (OpenReview refusé, 403)
L'interface d'OpenReview est refusée depuis cette session (R-2562). On ne la contourne pas (ni miroir, ni copie tierce, ni
autre mandataire). On fait :
1. **Mandataire arXiv** : `https://export.arxiv.org/api/query?search_query=co:%22ICLR+2027%22&start=S&max_results=500` puis
   `…search_query=abs:%22ICLR+2027%22…` ; on garde ce qui tombe dans les six catégories. Limite rapportée : une soumission
   anonyme absente d'arXiv est invisible.
2. **Options pour Lazar** (section 13, point 2) : ajouter l'hôte `api2.openreview.net` à l'environnement (décision de Lazar,
   proposée par la mère) ; ou déposer lui-même un export des titres et résumés dans
   `docs/notes/veille-concurrentielle-v1/brut/manuel/`, avec empreinte et date, traité ensuite comme toute source.
3. Rétro-test : les soumissions d'ICLR 2027 ne sont pas publiques au 1er octobre ; ce flux n'y entre pas, sauf ce qui était
   déjà sur arXiv à cette date.

### 2.6 Acceptés de NeurIPS 2026
Essais dans cet ordre, **une seule requête chacun** ; on s'arrête au premier qui rend la liste :
1. `https://neurips.cc/virtual/2026/papers.html?filter=titles`
2. Semantic Scholar :
   `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=monitor|probe|collusion|sabotage|judge|agent&venue=NeurIPS&year=2026&fields=paperId,externalIds,title,abstract,authors,publicationDate,venue`
   (on suit le jeton `token` rendu jusqu'à épuisement).
3. Mandataire arXiv : `search_query=co:%22NeurIPS+2026%22` puis `co:%22Neural+Information+Processing+Systems%22+AND+co:2026`.
L'ordre retenu et chaque refus sont consignés. Les acceptés sans version sur arXiv sont lus par leur PDF public s'il est sur un
hôte permis, sinon restent « titre et résumé seulement ».

### 2.7 Dépôts de code rivaux (GitHub refusé, 403)
1. **Sans requête** : on extrait les adresses `github.com`, `gitlab.com`, `huggingface.co` des champs `comment` et `summary`
   d'arXiv et du texte des PDF de l'étage 2. Elles donnent l'indicateur « code annoncé » du modèle d'équipe (section 5.3) ; on
   ne les suit pas.
2. **Hugging Face**, un essai : `https://huggingface.co/api/datasets?search=collusion&limit=100`. S'il rend 200, mêmes requêtes
   pour `sabotage`, `monitor`, `probe`, `deception`, `control`, puis `https://huggingface.co/api/models?search=…` ; sinon refus
   consigné.
3. **Aucun contournement** de GitHub : ni miroir, ni archive tierce de son contenu (Software Heritage compris), ni autre
   mandataire. Options pour Lazar : section 13, point 2. La cadence des dépôts (validations, versions) reste **non observée** et
   le modèle d'équipe ne l'emploie pas.

### 2.8 Phrases « travaux futurs », avec leur page
Pour chaque article de l'étage 2 : PDF de la **dernière version au plus tard le 30 septembre 2026** pour le rétro-test, de la
dernière version pour la veille vivante, par `https://arxiv.org/pdf/IDvK` ; empreinte consignée ; texte extrait page par page
(`pdftotext -layout -f P -l P`). Phrases retenues par expressions figées (anglais, insensibles à la casse) : `future work`,
`in future`, `we plan to`, `we leave`, `left for future`, `next step`, `we intend`, `remains open`, `open question`,
`we hope to`, `follow-up`, `ongoing work`, `forthcoming`, `companion paper`, `will release`, `we will`, et toute phrase des
sections dont le titre contient `Limitation`, `Future`, `Conclusion` ou `Discussion`. Chaque phrase garde sa page. Les lecteurs
la codent (section 4.2) : annonce-t-elle un code d'un axe, et lequel.

### 2.9 Billets (source complémentaire)
LessWrong et Alignment Forum sont joignables (R-2562). Requête :
```
POST https://www.lesswrong.com/graphql
{"query":"{ posts(input:{terms:{view:\"new\", after:\"2026-09-01\", before:\"DATE_LANCEMENT\", limit:1000}}) { results { _id title postedAt pageUrl htmlBody user { displayName } } } }"}
```
puis la même sur `https://www.alignmentforum.org/graphql`. Variante unique si la requête est refusée : flux
`https://www.alignmentforum.org/feed.xml` (récent seulement ; la lacune est dite). Les billets passent par le même tri ; un
billet n'est cité qu'archivé en texte, empreinté, avec ses lignes. **Tous les résultats sont rapportés avec et sans billets** ;
le seuil du rétro-test se juge **sans** billets.

### 2.10 Semences forcées (veille vivante seulement)
Versées à l'étage 2 sans passer l'étage 1, parce que des lecteurs les ont nommées et que personne ne les a lues contre nos
pièces : SSRN 6569258 (contre O-O4, priorité haute ; par son titre sur Semantic Scholar, PDF à prendre à la main s'il n'est
pas sur un hôte permis) ; 2504.10374 (A-H6) ; 2607.00415 (C-HC1) ; 2601.04603 (C-HC5) ; 2608.11247 (C-HC6) (R-2567) ;
2609.03035 v2 (C-HC2, B-POP ; contre-lecture 68-1, 69-1) ; 2609.00731, 2606.06769, 2607.26642, 2608.20290 (O-O4 ; N-067 § 8) ;
2607.06807, 2510.04303 (B-ST) ; 2602.01425 (A-H8) ; 2607.05545, 2605.03255 (C-HC1) (synthèse § 9, point 7). **Elles n'entrent
jamais dans le rétro-test.**

---

## 3. Tri à deux étages, avec décomptes (point c)

### 3.1 Dédoublonnage et préfiltre lexical (gratuits)
- Dédoublonnage par identifiant d'arXiv, puis par identifiant de Semantic Scholar, puis par titre normalisé (minuscules, sans
  accents ni ponctuation).
- **Préfiltre** sur titre et résumé, insensible à la casse ; `*` marque un préfixe. Passe si (au moins un terme de L1 **et** au
  moins un de L2) **ou** au moins un terme de L3.
  - **L1** : monitor*, oversight, probe*, probing, activation*, hidden state*, internal state*, residual stream,
    representation*, white-box, white box, interpretab*, detector*, detection, judge*, LLM-as-a-judge, verifier*, audit*,
    classifier*, guardrail*, red team*, red-team*, blue team*, sequential, e-value*, e-process*, anytime-valid, anytime valid,
    martingale*, CUSUM, change-point, change point, conformal, false discovery, multiple testing, hypothesis test*,
    null hypothesis, falsification, safety case*, control protocol*.
  - **L2** : agent*, agentic, multi-agent, language model*, LLM*, sabotage, sandbagging, deception, deceptive, scheming,
    collusion, colluding, coordination, backdoor*, misalign*, persuasion, persuasive, manipulat*, sycophan*, flattery,
    prompt injection, injection*, jailbreak*, evasion, evade*, obfuscat*, delegation, delegate*, subagent*, sub-agent*,
    handoff*, hypothesis generation, automated research, AI scientist, research agent*, Goodhart, reward hacking,
    specification gaming, untrusted.
  - **L3** : AI control, control evaluation, control setting, untrusted monitor*, trusted monitor*, trusted monitoring,
    linear probe*, deception probe*, white-box monitor*, activation monitor*, probe-based monitor*, e-process, anytime-valid,
    collusion, sandbagging, scheming, sabotage, LLM-as-a-judge, judge robustness, monitor evasion, obfuscated activations,
    constraint drift, delegation chain, AI scientist, automated hypothesis, hypothesis validation, diffuse threat*,
    low-stakes, high-stakes, SHADE-Arena, BashArena, ControlArena, NARCBench.
- **Contrôle de rappel du préfiltre, avant l'étage 1**, sur un **jeu de témoins** : les quinze ancrages et les pièces citées par
  la synthèse de niveau 3 dont la première version date d'avant le 1er septembre 2026 (titres et résumés pris par `id_list`).
  Exigence : rappel ≥ 0,95. Sinon, **un seul** addendum scellé ajoute aux listes des termes tirés des seuls témoins manqués,
  avant toute lecture de l'étage 1 ; il est rapporté comme écart. Les pièces de septembre de la liste de référence
  (section 8.3, strate 2) n'y entrent jamais : elles jugent le rétro-test.

### 3.2 Étage 1 — titre et résumé
Deux lecteurs (section 4), chacun seul, sur titre et résumé, **auteurs, affiliations et dates masqués**. Critère écrit, remis
tel quel aux lecteurs :

> Retenir l'article si le titre et le résumé laissent penser qu'il (i) étudie un objet parmi : agent qui agit, agent qui écrit un
> contenu destiné à un moniteur, agent qui agit sous un contenu écrit par un tiers, modèle qui lit un contenu, moniteur ou juge
> génératif, copies ou agents multiples, chaîne de délégation, juge ou proposeur d'une recherche automatisée ; **et** (ii) mesure,
> construit, attaque ou défend un dispositif de surveillance, de détection, de jugement ou de test statistique de ces objets, ou
> mesure une menace que ce dispositif doit détecter ou qui le vise ; **ou** (iii) établit un résultat théorique sur la détection
> séquentielle, la détection entre plusieurs flux ou la garantie de fausses alarmes, applicable à des agents. Exclure :
> entraînement de capacités sans surveillance ; alignement par entraînement sans mesure de surveillance ; banc générique sans
> moniteur ni juge ; sécurité informatique sans modèle de langue ; détection de texte généré ; évaluation de juges pour la
> qualité de réponses sans adversaire ni contrôle. **Dans le doute, retenir.**

Règle : **retenu si l'un des deux lecteurs retient** (union : le rappel prime en veille). Accord mesuré (section 4.5).
Les billets passent par le même critère.

### 3.3 Étage 2 — texte
- Texte : PDF de la version fixée en section 2.8 ; **corps** (jusqu'aux références) et pages d'annexe qui contiennent un terme de
  L1, L2 ou L3, plafonné à 30 000 jetons (pages de corps d'abord ; troncature consignée). En-tête d'auteurs, affiliations,
  remerciements et tampon d'arXiv masqués par expressions figées (le masque est testé sur dix PDF avant usage).
- Chaque lecteur rend, seul : les codes des sept axes avec une page par code ; une à cinq phrases de résultat avec leur page ;
  le codage des phrases « travaux futurs » (section 2.8) ; les champs d'échelle ; « code annoncé » oui ou non.
- Le script calcule `c` par pièce (section 1.2) ; les couples (article, pièce) avec `c ≥ 0,5` chez l'un ou l'autre lecteur
  vont au **jugement par pièce** (section 4.3).
- **Article retenu à l'étage 2** : jugé au moins « voisin » sur une pièce par au moins un juge. **Article qui compte pour la
  veille** : verdict de consensus, ou d'arbitrage, au moins « occupe en partie » sur une pièce, sur un élément non cédé.

### 3.4 Décomptes rendus à chaque étage, par flux et en tout (gabarit fixé)
| étage | arXiv (interface et listes) | citations en aval | ICLR (mandataire) | NeurIPS | billets | semences | total |
|---|---|---|---|---|---|---|---|
| reçus bruts | | | | | | | |
| après dédoublonnage | | | | | | | |
| après préfiltre lexical | | | | | | | |
| étage 1 : retenus par A, par B, par les deux, par l'un des deux ; accord | | | | | | | |
| étage 2 : lus ; retenus ; comptés (au moins « en partie ») | | | | | | | |
| par pièce : occupe / en partie / voisin | | | | | | | |
Deux tableaux : rétro-test (t0 = 1er octobre) et veille vivante. Les écarts entre listes et interface d'arXiv (section 2.2),
les refus et les troncatures sont rapportés à côté.

---

## 4. Grille de codage et double lecture aveugle (point d)

### 4.1 Les lecteurs
- **Codage par article (étages 1 et 2)** : deux lecteurs de **familles autres que celle du rédacteur** (Claude) et différentes
  entre elles. Choix par défaut, si Lazar accorde la dépense (section 11) : **A = `kimi-k3.1-pro`** (par le relais du dépôt),
  **B = `gemini-4-argon`** (appel direct), modèles déjà employés et chiffrés par le dépôt. Repli sans dépense : deux sous-agents
  Claude de deux modèles différents entre eux et différents du rédacteur (par défaut Claude Fable 5.x et Claude Opus 4.6),
  limite dite : même lignée que le rédacteur.
- **Jugement par pièce** : deux sous-agents Claude de deux modèles différents entre eux et du rédacteur. Ils reçoivent la pièce
  et le texte masqué, jamais les codes des lecteurs A et B ni l'avis de l'autre juge.
- **Arbitre** : un troisième modèle, distinct des deux lecteurs et du rédacteur, pour chaque désaccord (section 4.5).
- Aucun lecteur n'a écrit ce protocole ni ne le reçoit ; chacun reçoit seulement ses consignes et son lot.

### 4.2 Consignes du codage par article
Le vocabulaire fermé de la section 1.1, recopié tel quel ; une page pour chaque code, sinon le code est nul ; « absent » est un
code permis ; aucune inférence au-delà du texte ; sortie JSON fixée (identifiant interne masqué, codes, pages, phrases de
résultat, phrases « travaux futurs » codées, champs d'échelle). Lots de 25 articles par appel à l'étage 1, un article par appel
à l'étage 2.

### 4.3 Consignes du jugement par pièce
L'échelle « occupe / occupe en partie / voisin / ne touche pas », avec les axes couverts et leurs pages ; la pièce est décrite par
sa signature, sa forme de résultat et sa liste « cédé ». « Occupe » exige tous les axes exigés **et** la forme de résultat.
Le juge dit aussi si une phrase « travaux futurs » de l'article annonce un axe manquant, avec sa page.

### 4.4 Aveuglement et confidentialité
- Les lecteurs ignorent les auteurs, les affiliations, les dates, l'avis de l'autre lecteur, et l'existence du rétro-test.
- **Aucun énoncé du programme n'est envoyé à un fournisseur extérieur** : A et B ne reçoivent que des textes publics et le
  vocabulaire neutre des axes ; le jugement par pièce, qui porte nos énoncés, reste chez les sous-agents de la session.
- **Sonde de connaissance** avant le rétro-test, hors de tout lot : on demande à chaque lecteur ce qu'il sait de cinq
  identifiants de la strate 1 (section 8.3) et de cinq identifiants inventés. Un lecteur qui décrit correctement une pièce de
  la strate 1 est **contaminé** pour le rétro-test : ses lectures du corpus d'avant le 1er octobre sont refaites par l'arbitre,
  et le rapport le dit.

### 4.5 Accord mesuré et règle de désaccord
- Étage 1 : kappa de Cohen sur « retenu », pourcentage d'accord, nombre de retenus par un seul lecteur.
- Étage 2 : kappa de Cohen par code, regroupé par axe ; kappa pondéré (quadratique) sur l'échelle à quatre niveaux du jugement
  par pièce.
- **Seuil** : kappa ≥ 0,6 par axe et pour le jugement par pièce. En dessous, l'axe est marqué « accord faible » dans tous les
  résultats ; **dans tous les cas, chaque désaccord** sur un jugement par pièce et sur un code qui change `c` d'au moins 0,25 va
  à l'arbitre ; accords avant et après arbitrage rapportés ; aucun désaccord n'est tranché en silence.
- **Témoins des lecteurs**, avant le lot principal : 20 témoins positifs (pris dans le jeu de la section 3.1) et 20 négatifs
  tirés au hasard (graine, section 7.4) parmi les articles de septembre écartés par le préfiltre. Exigence à l'étage 1 :
  au moins 18 positifs retenus sur 20 par chaque lecteur. Sinon, une révision de consigne (addendum scellé), un second essai ;
  en cas de nouvel échec, le lecteur est remplacé par l'arbitre et le rapport le dit.

---

## 5. Modèle de fourchette de sortie par équipe (point e)

Tout est calculé par script à partir du corpus d'avant t0, sans réglage à la main. Les multiplicateurs sont **a priori** :
aucune donnée ne permet de les ajuster avant le rétro-test, et ils ne sont pas ajustés après (section 0.1, point 5).

### 5.1 Équipe
Deux articles sont de la même équipe s'ils partagent le dernier auteur, ou au moins deux auteurs, ou si l'indice de Jaccard
de leurs listes d'auteurs vaut au moins 1/3 ; les équipes sont les composantes ainsi reliées. Identité d'un auteur : identifiant
de Semantic Scholar, sinon nom normalisé (initiale du prénom et nom, sans accents). Nom d'équipe : dernier auteur et affiliation
la plus fréquente **imprimée** dans ses articles antérieurs à t0.

### 5.2 Position sur une pièce, et ce qui lui manque
`c(T,p)` = maximum, sur les articles de l'équipe T, de : 1 si « occupe » ; part des axes exigés couverts si « occupe en
partie » ; 0,1 si « voisin » ; 0 sinon. **Ce qui lui manque** : les axes exigés de p qu'aucun de ses articles ne couvre, et la
forme de résultat si elle n'est pas faite.

### 5.3 Taux de publication sur la pièce
Pour une équipe T et une pièce p, en articles par semaine :

`h(T,p) = λ(T) × π(T,p) × g(T,p) × r(T,p) × a(T,p) + Σ_articles ν × 0,2 × a(T,p)`

- **Cadence** `λ(T) = (n + 1) / 104`, où n = premières versions de l'équipe dans les 365 jours avant t0 (Semantic Scholar,
  section 2.3) : un article par an d'a priori, pesant un an.
- **Part du sujet** `π(T,p) = (m + 1) / (n + 2)`, où m = articles de l'équipe des 365 jours qui passent le préfiltre lexical.
- **Proximité** `g(T,p) = 0,25 + 1,5 × c(T,p)` (a priori).
- **Ressources** `r(T,p)` = 1,5 si l'équipe a déjà employé, dans un article antérieur à t0, le type d'accès et l'échelle que
  demandent les axes manquants (par exemple TA3 sur un modèle ouvert ≥ 7 milliards ; au moins trois agents pour le papier B) ;
  0,5 si aucun de ses articles n'emploie ce type d'accès ; 1 sinon. « Code annoncé » est rapporté, non employé.
- **Annonce** `a(T,p)` = 3 si une phrase « travaux futurs » de l'équipe, page citée, annonce au moins un axe manquant de p ;
  1 sinon (a priori).
- **Versions** : pour chaque article de l'équipe jugé au moins « en partie » sur p, `ν = (k − 0,5) / (âge en semaines + 26)`,
  k = nombre de versions ; 0,2 = probabilité a priori qu'une version nouvelle ajoute un axe manquant.
- **Équipe nouvelle** (non nommée) : pour chaque famille F de pièces (A, B, C, organisme), `h_nouv(p) = (k_F + 0,5) / (26 × |F|)`,
  k_F = articles des 26 semaines avant t0, comptés sur une pièce de F, dont l'équipe n'avait aucun article antérieur dans le
  corpus. Les collisions viennent souvent d'équipes inconnues ; ce terme les représente sans les nommer.

### 5.4 Fourchette et probabilité
Temps jusqu'à la sortie : loi exponentielle de taux h. Rendus pour chaque couple (équipe, pièce) : quantiles 10 %, 50 %, 90 %
(`t_q = −ln(1 − q) / h`) et probabilités de sortie à 4, 8, 13 et 26 semaines. Pour la pièce : `P_p(w) = 1 − exp(−w × (Σ_T h(T,p)
+ h_nouv(p)))`. **Équipe la mieux placée** : la plus grande probabilité à 8 semaines, égalité départagée par c. « Sortie » veut
dire première version publique d'un article ou d'un billet, pas l'acceptation dans une conférence.

---

## 6. Notre délai réel jusqu'au premier résultat publiable

- **Premier résultat publiable** d'une pièce : le plus petit résultat qui resterait à nous (section 7.3), avec préenregistrement
  scellé et contre-lu, mesure faite, analyse, verdict et texte d'atelier prêt pour arXiv.
- **Plan restant** : étapes et durées prévues, lues dans le programme v2 (§ 10, § 14), le brief v2, `registres/etat.md`,
  `registres/go.md`, les préenregistrements sous `prereg/` et les devis ; chaque étape typée par voie (section 7.6). Aucune
  lecture des chemins interdits (section 10).
- **Glissement mesuré** : pour chaque jalon achevé ou daté de nouveau qui a une date prévue écrite (registres, passations,
  décisions), rapport `durée réelle / durée prévue`. Premier point déjà écrit : phase 0 prévue du 5 octobre au 1er novembre 2026
  (programme, l. 178) ; porte G0 « au plus tard fin novembre » (N-027, `CLAUDE.md`), point encore ouvert, donc borne basse.
  Il faut au moins cinq jalons ; sinon le rapport le dit et emploie la plage des points disponibles.
- **Délai** : `T_n = durée restante prévue × glissement`, le glissement tiré d'une loi log-normale de médiane et d'écart
  interquartile ceux des rapports mesurés. Rendu par pièce : quantiles 10 %, 50 %, 90 % de T_n, et `P(T_n < T_r)`, probabilité
  de sortir avant le premier rival, mis face à face.

---

## 7. Regret attendu, décision par pièce, ordre des travaux (point f)

### 7.1 Utilité
Pour une pièce p, un tirage ω (temps du premier rival `T_r`, tiré de `P_p`, et notre délai `T_n`) et une décision d :
- **tenir** : `U = V × [1(T_n < T_r) + s × 1(T_n ≥ T_r)]`.
- **accélérer** : même forme avec `T_n × 0,6`, moins `0,4 × W × ρ` (capacité prise aux autres pièces).
- **mettre en sommeil** : même forme avec `T_n + 8 semaines`, plus `8 × (W / T_n) × ρ` (capacité rendue pendant le sommeil).
- **abandonner** : `U = W × ρ` (toute la capacité restante rendue ; la pièce est citée chez le rival).
Où **W** = semaines de travail restantes de la pièce (plan, section 6) ; **ρ = Σ V / Σ W** sur toutes les pièces (valeur moyenne
d'une semaine de capacité) ; **s** = valeur qui reste si le rival sort d'abord : `s = max(0,1 ; 1 − e)`, avec
`e = c* + (1 − c*) × 0,5` (× 1,5 si l'équipe la mieux placée annonce un axe manquant ; plafonné à 1) et c* = position de
l'équipe la mieux placée. 0,6, 8 semaines, 0,5 et 0,1 sont **a priori**.

### 7.2 Regret attendu et classement
`R(d) = E_ω[ max_d′ U(d′, ω) − U(d, ω) ]`, estimé par 20 000 tirages par pièce. **Classement des pièces par `R(tenir)`**, le
regret de poursuivre au rythme actuel, décroissant. **Décision** = la d qui minimise R(d), sous deux contraintes : décisions
permises de la pièce (section 1.3) ; capacité : la somme des `0,4 × W` des pièces à accélérer ne dépasse pas la capacité rendue
par les pièces mises en sommeil ou abandonnées. Si la contrainte mord, on accélère par ordre de `(R(tenir) − R(accélérer)) /
(0,4 × W)` décroissant, les autres restent à leur seconde meilleure décision.

### 7.3 Le plus petit résultat qui resterait à nous
Par pièce : le plus petit ensemble d'axes exigés, avec une forme de résultat mesurable, qui n'est couvert par aucun article
compté **et** n'est annoncé par aucune équipe (phrase « travaux futurs » à page citée) ; parmi les candidats, celui de plus court
délai T_n. Proposé par le script à partir des codes, vérifié par un juge, rendu avec son délai.

### 7.4 Graines
`numpy.random.SeedSequence(entropie = int(16 premiers caractères hexadécimaux de l'empreinte de ce protocole scellé, base 16))`,
une graine fille par pièce et par usage (`spawn`), consignées au manifeste du calcul (R9), comme pour tout tirage du protocole
(témoins négatifs, perturbations).

### 7.5 Sensibilité
200 perturbations : V × exp(N(0 ; 0,5²)) ; facteur d'accélération uniforme sur [0,4 ; 0,8] ; glissement × uniforme sur
[0,75 ; 1,5] ; chaque multiplicateur de la section 5.3 × uniforme sur [0,5 ; 2]. Une décision est **stable** si elle reste la
même dans au moins 80 % des perturbations, sinon **fragile** ; le rang de chaque pièce est rendu avec son intervalle de 80 %.

### 7.6 Ordre des travaux et parallélisme
Quatre voies : (1) calcul sur processeur graphique, sous GO ; (2) appels de modèles payants, sous GO ; (3) processeur et
écriture (théorie, préenregistrements, rédaction) ; (4) lecture et veille. Graphe des dépendances tiré du programme (phases et
portes : G0 avant G1 ; G1 et GC avant les papiers A et C ; G2 avant la phase 3) et des registres. Ordonnancement par liste : à
chaque pas, parmi les étapes prêtes, celle qui réduit le plus le regret par semaine de capacité va à la première voie libre de
son type. **Capacité** : une étape à la fois par voie, par défaut (Lazar peut en donner davantage). Rendu : ordre, prochaine
étape, voie, dépendances, ce qui court en parallèle.

### 7.7 Forme du rendu (phase 4)
Une ligne par pièce, dans l'ordre de `R(tenir)` : pièce ; équipe la mieux placée ; ce qui lui manque ; fourchette (10, 50,
90 %) et probabilité à 8 semaines ; probabilité « équipe nouvelle » ; notre délai (10, 50, 90 %) ; `P(T_n < T_r)` ;
`R(tenir)` ; décision et sa stabilité ; plus petit résultat à nous ; prochaine étape, voie, ce qui court en parallèle. Puis
les décisions qui touchent une revendication sont **portées à Lazar** (nœuds) : le protocole ne tranche aucune revendication.

---

## 8. Rétro-test au 1er octobre 2026 (point g)

### 8.1 Ce qu'on refait
Toute la chaîne, sections 2 à 7, avec t0 = 2026-10-01T00:00:00Z : listes et interface d'arXiv du 1er au 30 septembre ;
citations en aval des quinze ancrages limitées aux citants publiés au plus tard le 30 septembre (date d'arXiv, sinon
`publicationDate` ; sans date, exclu) ; NeurIPS : ce qui était public au 30 septembre ; PDF de la dernière version antérieure
au 1er octobre ; cadences et affiliations antérieures à t0 ; **pièces d'origine** (section 1.4) ; aucune semence forcée, aucun
ancrage vivant. Horizon jugé : **H = du 1er octobre au 13 novembre 2026**.

### 8.2 Gardes contre la fuite d'information
1. Garde de date dans le script : tout élément de date postérieure au 30 septembre fait **échouer** la construction du corpus du
   rétro-test (pas de filtrage silencieux) ; testée sur un corpus sain et sur un corpus piégé (R5).
2. Sonde de connaissance des lecteurs (section 4.4).
3. Aucun geste discrétionnaire de l'opérateur entre la collecte et le scellement des prédictions du rétro-test ; tout geste à la
   main est consigné.
4. Les prédictions du rétro-test (probabilités par pièce et par équipe) sont **scellées avant** leur comparaison à la liste de
   référence ; la comparaison est faite par un **sous-agent neuf**, qui n'a ni conduit la collecte ni écrit les prédictions.
5. Limite résiduelle déclarée : le rédacteur de ce protocole et l'opérateur connaissent la liste ; d'où les règles fixées à
   l'avance et l'exécution par script.

### 8.3 Liste de référence, figée avant toute requête
Tirée de la synthèse finale (`e30a013d…`) et de R-2551 à R-2553. Une pièce est **collision** si la synthèse ou ces lignes la
donnent comme occupant, au moins en partie, un élément d'une pièce d'origine **que rien de daté d'avant le 1er octobre
n'occupait déjà**. Date = première version (ce qui a été ajouté par une version suivante n'est pas daté ; limite dite).

**Strate 1 — collisions publiées dans H (jugent l'annonce).**

| n° | identifiant | première version | équipe connue | pièces d'origine touchées | éléments occupés | source |
|---|---|---|---|---|---|---|
| 1 | 2610.12445 | 8 oct. 2026 (v4 du 20 oct.) | FAR.AI | A-H1 | sondes contre moniteurs en boîte noire, par étape, à 1, 2 et 5 % de fausses alarmes, sabotage d'agent | synthèse § 2 (C5, S-3A) |
| 2 | 2611.10620 | 7 nov. 2026 | Mohsin, Rahman | B-POP, B-ST, A-H8, B-H3 | grille temps × agents sur scores de sondes, balayages de sous-groupes, alarme à seuil conforme ; lien construit → tenue du seuil ; rappel par taille de coalition | synthèse § 2 (H8), § 3 ; N-069 |
| 3 | 2611.02153 | 1er nov. 2026 | Molinari, Bettineschi | B-POP, B-ST | score de paire sur états internes de copies, cumulé sur les tours | synthèse § 3 ; N-069 |
| 4 | 2611.04556 | 3 nov. 2026 | Smith, …, Hammond | rôle 1 | prémisse du bras « juge génératif » (relecteur génératif qui approuve un écart à un préenregistrement) | R-2551, R-2553, R-2554 ; synthèse § 5 |
| 5 | 2610.29178 | octobre 2026 (jour à relever) | à relever | C-HC5 | matrice de transfert entre juges ; quorum avec moteur de règles | synthèse § 4 (S-7C) |
| 6 | 2611.01449 (CONFIRM) | novembre 2026 (v1 à relever ; v2 du 3 nov.) | Wei et al. | O2, O3, O12 | engagement haché avant lecture ; diagnostic du juge servi sur contrôles négatifs | synthèse § 5 ; N-067 |
| 7 | 2611.06607 | 4 nov. 2026 | Zhang | O2, O3 | contrat de campagne haché avant la première proposition | synthèse § 5 ; N-067 |
| 8 | 2610.38392 | 28 oct. 2026 | So, Liu, Long | O3 | prédictions des auteurs gelées et hachées avant chaque essai | synthèse § 5 ; N-067 |
| 9 | 2611.00643 | novembre 2026 (jour à relever) | à relever | O12, rôle 1 | harnais optimisé contre un juge modèle | synthèse § 5 ; N-067 |

**Pièces d'origine touchées dans H** (issue figée) : A-H1, A-H8, B-POP, B-ST, B-H3, C-HC5, O2, O3, O12, rôle 1 — **10 sur 33**.
Toutes les autres sont « non touchées dans H ».

**Strate 2 — pièces de septembre 2026 (jugent la détection), hors ancrages.**

| n° | identifiant | première version | équipe connue | pièces d'origine | source |
|---|---|---|---|---|---|
| 1 | 2609.27051 | 22 sept. 2026 | Qu, Chen, Wang | O1, O2, O11, O3 (principe) | synthèse § 5 ; N-067 |
| 2 | 2609.19587 | septembre 2026 (27 sept. selon C5) | à relever | C-HC3 (ordres en bande neutralisés) | synthèse § 4 |
| 3 | 2609.36490 | septembre 2026 | à relever | B-H5 (matrice sous attaque), C-HC4 (régime « poids ») | synthèse § 3 ; R-2567 B3 ; N-013 |
| 4 | 2609.02246 (PROCTOR) | 2 sept. 2026 | Wahi | O1, O10, O17 (principe) | synthèse § 5 ; N-067 |
| 5 | 2609.33180 (REUSE) | septembre 2026 (v2 du 29 sept.) | Sun, Zeng, She, Wang | O9, O19 (principe), O12 (adversaire théorique) | synthèse § 5 ; N-067 |
| 6 | 2609.10739 | septembre 2026 | à relever | A-H8 (socle) | synthèse § 2 (C8) |
| 7 | 2609.17560 (DISCERN) | septembre 2026 | à relever | O11 (validation préenregistrée) | N-067 § 3 (C7) |

**Écartés de la liste, avec raison** (rapportés à côté, jamais comptés) : 2610.04575 (« voisin » selon lot3-Aa) ; 2610.17301
(« n'occupe ni H1 ni H2 ») ; 2610.24052 (boîte noire, cédée) ; 2610.26935 (contre-indice) ; 2610.37679, 2611.11172, 2610.18408
(lecteur ou victime, voisins de HC2) ; CADS 2610.24597, Hegazy et al. 2610.06432, 2611.04420, N×N v5 (éléments déjà occupés
avant le 1er octobre par Qu, Chen, Wang, Sargsyan ou PACE) ; versions postérieures de NARCBench, MasDrift, Sun (première version
antérieure) ; billets du 30 octobre (H2) et du 14 septembre (HC5), comptés seulement dans le score « avec billets » ;
2609.03035 v2 (venu de la contre-lecture, pas de la synthèse ; de plus ancrage).
**Strate 2b** (information, non jugée) : pièces de la synthèse antérieures au 1er septembre 2026 et non ancrages (MIRAGE
2606.10304, 2608.12645, CURA 2608.27808, 2608.02464, 2606.20746, 2606.04141, 2607.11751, 2604.13386, PACE 2606.08106, N×N
2608.06621, SafeDream 2604.16824, MasDrift 2608.07556, Sun 2608.24569, AgentCollabBench 2605.08647, Li 2605.10481, 2606.05384,
2603.15809, 2602.13568, 2608.25869, 2607.13346, Sargsyan 2511.06701, SGM 2510.10232) : part retrouvée par le seul flux des
citations, rapportée.

### 8.4 Critères et seuil de réussite (écrits avant toute requête)
1. **Détection** : parmi les 7 pièces de la strate 2, **au moins 6** présentes dans le corpus du rétro-test après dédoublonnage,
   **et au moins 5** retenues à l'étage 2 avec un verdict de consensus ou d'arbitrage au moins « occupe en partie » sur l'une des
   pièces d'origine qui leur sont attribuées.
2. **Annonce par pièce** : sur les 33 pièces d'origine, l'aire sous la courbe de `P_p(H)` contre l'issue « touchée dans H » vaut
   **au moins 0,70**, et n'est pas inférieure de plus de 0,05 à celle de la **base de volume** (nombre d'articles de septembre
   comptés sur la pièce).
3. **Annonce par équipe** : pour **au moins 3** des 9 collisions de la strate 1, une équipe qui partage au moins un auteur avec
   l'article figure parmi les **trois premières** équipes (probabilité sur H) de l'une des pièces qu'il touche.
**Réussite = 1 et 2 et 3.** Rapportés en plus, sans seuil : score de Brier et score de Brier relatif à la fréquence observée sur
les 33 pièces ; diagramme de fiabilité ; tout avec et sans le flux des citations, avec et sans billets.

### 8.5 Conséquences écrites d'avance
- **1 échoue** : le corpus ou le tri ne voient pas ce qui existe ; arrêt de la veille vivante ; correction par une v2, puis
  nouveau rétro-test avec t0 = 15 octobre 2026 et la sous-liste de la strate 1 postérieure à cette date (fuite résiduelle dite).
- **1 et 2 tiennent, 3 échoue** : probabilités par pièce employées ; noms d'équipes rendus comme **information non validée**.
- **2 échoue** : les décisions de la section 7 emploient la base de volume (taux proportionnel au nombre d'articles comptés sur
  la pièce dans les 13 semaines avant t0, même normalisation que `h_nouv`) ; noms d'équipes en information.
- **Trop beau (R4)** : aire ≥ 0,95 et 9 sur 9 en 3 déclenchent un audit de fuite (dates, sonde de connaissance, gestes de
  l'opérateur) avant toute acceptation.

---

## 9. Prédictions datées (point h)

- **Forme** : une ligne par prédiction : identifiant `PV-AAAAMMJJ-NNN` ; date d'émission UTC ; pièce ; axes visés ; équipe
  (nom, auteurs) ou « équipe nouvelle » ; fenêtre `[émission ; émission + 56 jours]` ; probabilité à deux décimales ;
  composantes du taux (section 5.3). Les fenêtres de 13 et 26 semaines sont écrites aussi, relues plus tard.
- **Quelles prédictions** : **toutes** les pièces au niveau « au moins une équipe » (les faibles comprises, pour que le score
  ait un sens) ; tous les couples (équipe, pièce) de probabilité ≥ 0,05 à 8 semaines.
- **Critère d'appariement** : une prédiction est réalisée si un article ou un billet dont la **première version** tombe dans la
  fenêtre, d'au moins un auteur de l'équipe (ou de toute équipe pour une prédiction de pièce), est jugé par deux juges aveugles
  au moins « occupe en partie » sur au moins un axe visé non cédé.
- **Scellement** : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller` sur le fichier ; jamais réécrit (R12).
- **Relecture à émission + 56 jours** par un sous-agent neuf, qui n'a ni écrit ni conduit les prédictions : mêmes requêtes que
  la section 2, limitées à la fenêtre ; jugement aveugle ; score de Brier, score logarithmique (probabilités bornées à 0,01 et
  0,99), fiabilité par classes (0–0,1 ; 0,1–0,3 ; 0,3–0,6 ; 0,6–1) ; part des équipes nommées réalisées. Résultat scellé,
  rapporté à Lazar avec les décisions qu'il change.

---

## 10. Ce qui ne se fait pas (point i)

1. **Aucun chiffre sans page** (R7) ; aucun chiffre d'un résumé, d'un contexte de citation ou d'une sortie de modèle cité
   comme fait.
2. **Aucune lecture de nos chemins interdits**, ni recherche récursive qui les traverse ; les scripts refusent d'ouvrir un
   chemin qui y correspond (garde testée, R5) : `diag/*/lecture-sondes-t06.json` ; la lecture B de 7a ;
   `donnees/lecture-b-7a-quarantaine-v1` ; `donnees/mesure-unanime-v15-sortie-v1` ; `essai/t06-explo-v3` ; tout `diag/` et
   `runs/` de 7a ou 7b ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; la branche `calcul/p3bis-reel-v2` ;
   `donnees/bras-attaque*` ; `donnees/mode-tenu-a-l-ecart*` ; `docs/notes/bras-attaque/` ; `registres/index-bras-attaque*` ;
   `anteriorite-bras-informe*` ; la branche `claude/compassionate-meitner-d4ryyk`. Le calcul du délai réel (section 6) lit les
   registres et le plan, jamais ces chemins.
3. **Aucun appel payant** (lecteurs d'autres familles, collisionneur) sans devis ferme et ligne de GO dans `registres/go.md` ;
   devis en section 11. Plafond dur tenu par le script ; arrêt au plafond, sans repli silencieux (R5).
4. Aucune valeur de clé lue ni affichée ; clés appelées par leur nom seul.
5. **Aucun contact** avec une équipe rivale ; aucune publication ; rien de ce travail ne sort du dépôt (l'enregistrement sous
   embargo de R-2563 est une autre tâche).
6. **Aucun contournement** d'un refus (OpenReview, GitHub, classifieur, permission) : on consigne, on rapporte, on s'arrête.
7. Aucun énoncé du programme envoyé à un fournisseur extérieur (section 4.4), sauf le collisionneur, s'il est accordé (section
   11, ligne 3).
8. Le protocole ne tranche **aucune** revendication ; toute pièce trouvée occupée est un nœud porté à Lazar.
9. Aucune requête, aucune dépense et aucune écriture git n'ont servi à écrire ce protocole.

---

## 11. Devis des appels payants

### 11.1 Prix retenus (du dépôt, non de mémoire)
- `kimi-k3.1-pro` : **2 et 10 USD par million de jetons** d'entrée et de sortie, « vérifiés »
  (`devis-mini-course-kimi-argon-nuit-v1.md`, l. 62).
- `gemini-4-argon` : prix public **2 et 10 USD par million** (`registres/depenses.md`, l. 389) ; **barème prudent 10 et 50 USD**,
  « supposé » (`devis-mini-course-kimi-argon-nuit-v1.md`, l. 63), employé pour le pire cas et le plafond.
- Collisionneur : **15 USD au plus par tour** sous la ligne GO-2026-11-12-04 ; un tour réel a coûté **9,54 USD**
  (`depense-et-incidents-v1.md`, l. 48 ; devis `1b511a8d…`, pire cas 14,51).
- Sous-agents Claude (jugement par pièce, arbitre) : aucun appel facturé par clé ; capacité de la session (R-2550 rappelle que
  cette capacité peut s'épuiser).

### 11.2 Coût par unité (deux lecteurs, A et B)
| unité | jetons par lecteur (entrée ; sortie) | attendu, prix publics | pire cas, Argon au barème prudent |
|---|---|---|---|
| article à l'étage 1 (lot de 25, consigne amortie) | 430 ; 60 | 0,0029 USD | 0,0088 USD |
| article à l'étage 2 (texte plafonné à 30 000 jetons) | 20 500 attendu, 32 500 au plus ; 1 200 | 0,106 USD | 0,462 USD |
| sonde de connaissance (10 questions par lecteur) | 1 500 ; 300 par question | 0,12 USD | 0,36 USD |

### 11.3 Enveloppe (hypothèses de volume, à remplacer par les décomptes gratuits)
Étage 1 : de 1 500 à 8 000 articles après préfiltre ; étage 2 : de 100 à 600 articles.
| ligne | attendu, prix publics | pire cas prudent |
|---|---|---|
| 1. Étage 1, deux lecteurs | 4,4 à 23,4 USD | 13,1 à 70,1 USD |
| 2. Étage 2, deux lecteurs, sonde comprise | 10,7 à 63,7 USD | 46,6 à 277,6 USD |
| **Sous-total sans collisionneur** | **15 à 87 USD** | **60 à 348 USD** |
| 3. Collisionneur, facultatif : un tour sur chacune des cinq premières pièces au classement, pour durcir leur « libre » (R8) | 35 à 55 USD (7 à 11 par tour) | 75 USD (5 × 15) |

### 11.4 Procédure de GO
Devis **ferme en deux temps**, chacun après le décompte gratuit qui le précède : (a) après le préfiltre, ligne de l'étage 1 au
plafond `N1 × 0,0088 × 1,2` ; (b) après l'étage 1, ligne de l'étage 2 au plafond `N2 × 0,462 × 1,2 + 0,36`. Le rétro-test passe
en premier dans chaque ligne. La ligne 3 est une ligne à part, **qui envoie nos énoncés à d'autres fournisseurs** : à accorder
expressément, ou à refuser. Chaque ligne est inscrite à `registres/depenses.md` à l'engagement et à la clôture.

---

## 12. Phases, livrables, gardes, liste d'arrêt

| phase | contenu | dépense | livrables (sous `docs/notes/veille-concurrentielle-v1/`) |
|---|---|---|---|
| 1 | ce protocole, scellé ; contre-lecture (R2) | aucune | `protocole-veille-concurrentielle-v1.md`, `contre-lecture-protocole-veille-concurrentielle-v1.md` |
| 2 | collecte (section 2), préfiltre, témoins, décomptes ; devis ferme (a) | aucune | `brut/journal-requetes-v1.jsonl`, `corpus/corpus-retro-2026-10-01-v1.jsonl`, `corpus/corpus-vivant-AAAAMMJJ-v1.jsonl`, `decomptes-v1.md`, `devis/devis-ferme-etage1-v1.md` |
| 3 | étages 1 et 2, jugement par pièce, accord ; rétro-test d'abord | sous GO | `codage/…-v1.jsonl`, `codage/accord-v1.md`, `retro-test/predictions-retro-v1.md` (scellé avant comparaison), `retro-test/resultat-retro-test-v1.md` |
| 4 | équipes, délai réel, regret, décisions, ordre | aucune | `equipes/…-v1.json`, `decisions/regret-et-decisions-v1.md` |
| 5 | prédictions datées, scellées | aucune | `predictions/predictions-datees-v1.md` |
| 6 | relecture à émission + 56 jours | aucune ou sous GO | `predictions/relecture-predictions-v1.md` |

Scripts sous `scripts/veille_*_v1.py`, essais sous `tests/` ; chaque garde (date du rétro-test, hôtes permis, plafond de
dépense, chemins interdits, masque des auteurs) testée sur un cas sain et sur un artefact (R5). Manifeste de calcul par phase
(R9). Tout fichier rendu reçoit son compagnon `.sha256` (R6) ; nouvelle version, nouveau nom (R12). Les commits et la poussée
sont faits par la session mère.

**Liste d'arrêt** (on s'arrête, on consigne, on rapporte tel quel) : refus d'un contrôle de permissions ou d'un classifieur ;
requête vers un hôte non permis ; plafond de dépense atteint ; garde de date du rétro-test déclenchée ; lecteur contaminé sans
remplaçant ; chemin interdit touché ; rappel des témoins < 0,95 après l'addendum ; contre-lecture du protocole qui demande une
v2.

---

## 13. Décisions demandées à Lazar (proposer avec recommandation, défaut sous 48 heures, sauf la dépense)

1. **Lecteurs du codage par article.** Enjeu : indépendance des lecteurs contre dépense. (a) `kimi-k3.1-pro` et
   `gemini-4-argon` : deux autres lignées, comme le veut N-053 / dépense de 15 à 87 USD attendus, 348 au pire. (b) deux
   sous-agents Claude d'autres modèles : aucune dépense / même lignée que le rédacteur, capacité de session. Recommandation : (a),
   confiance 0,6. **La dépense est un nœud : sans GO, défaut (b).**
2. **OpenReview et GitHub refusés.** (a) proposer l'ajout des hôtes `api2.openreview.net` et `api.github.com` à
   l'environnement : flux complets / élargit l'accès réseau. (b) export déposé à la main par Lazar : aucun changement réseau /
   son temps. (c) mandataires arXiv seuls (sections 2.5, 2.7) : rien à faire / soumissions anonymes et cadence des dépôts
   invisibles. Recommandation : (c) pour commencer, (b) pour ICLR si le rétro-test réussit ; confiance 0,6. Défaut : (c).
3. **Valeurs V des pièces.** Défaut : section 1.5 ; Lazar peut les remplacer avant la phase 4.
4. **Collisionneur (ligne 3).** Recommandation : ne pas l'accorder avant le rétro-test ; ensuite, sur les cinq premières pièces
   seulement ; confiance 0,5. Défaut : non.
