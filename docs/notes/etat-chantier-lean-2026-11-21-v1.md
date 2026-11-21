# État du chantier Lean (preuve formelle et mathématiques nouvelles, couche 4 de l'organisme d'idéation) — 21 novembre 2026 — v1

- Pièce de travail (classe C), écrite le 2026-11-21 vers 06:12 UTC (`date -u`) par un sous-agent Opus 5.5 (`claude-opus-5-5`) de la session mère, à sa demande, pour répondre à la question du directeur : « on peut reprendre la partie Lean, élaboration de nouvelles mathématiques pour l'attaque et la défense ? ».
- Sources lues : registres (décisions, GO, état, dépenses, arrêts, passations du 12 au 14 novembre), notes et brouillons du chantier. Aucun résultat d'expérience lu (ni 7a, 7b, T0.6, étapes B et B bis, P3-bis, ni barreau 5). Rien n'a été lu sous `docs/notes/bras-attaque/` (cloison).
- Les numéros de ligne renvoient aux fichiers tels qu'ils étaient au commit `1e092ee0` de `main`. Les empreintes sont tronquées à 8 ou 16 signes ; chaque compagnon `.sha256` a été recalculé et trouvé conforme.

## Verdict

1. **Oui, on peut reprendre, et c'est surtout du travail sans dépense.** Le chantier s'est arrêté le 13 novembre, juste avant le **troisième essai de l'outillage** (installation isolée de Lean et Mathlib, sans aucun appel de modèle). Tout était prêt : harnais réparé et contre-lu, consigne du poste scellée, mot de Lazar pour lancer sur son poste. Depuis, plus rien n'a été inscrit aux registres sur ce chantier.
2. **L'accord de dépense de l'outillage court encore jusqu'au 30 novembre** : 0,56 USD dépensés sur 65 (GO-2026-11-10-13). Le pilote avec appels de modèle et le pilier « génération » (les mathématiques nouvelles proprement dites) n'ont **ni préenregistrement scellé, ni ligne de GO**. Le pilier reste fermé par deux décisions de Lazar : N12 (b), qui attend les résultats de l'étape 2, et DP-1 (a).
3. **« Attaque et défense »** : dans les pièces, l'attaque n'apparaît qu'au niveau de la méthode. Il s'agit d'attaquer l'arbitre formel et le juge de nouveauté (Goodhart, papier C) ; les recettes d'attaque sont exclues (R-607). La défense, elle, prend la forme d'énoncés sur les panels de moniteurs (agrégateur sous corrélation adverse, lemme d'impossibilité). Le bras d'attaque en quarantaine, qui figurait dans une ancienne numérotation de la couche 4, n'en fait plus partie.

## 1. Ce qu'est ce chantier

- **Origine.** Le 31 octobre, Lazar pose la question « réécriture de soi et de concepts mathématiques inédits avec lean en soutien ? ». La session-dépôt répond que la couche 4 de l'organisme est le « pôle théorie et Lean » et qu'elle n'existe pas encore (`registres/decisions.md:1149`, R-920). Définition (ordre de conception, point 4) : le juge est un vérificateur de preuves (Lean), le proposeur est nourri par le moissonneur et la recombinaison. Les questions visées sont l'agrégateur sous corrélation adverse et le théorème négatif. Consigne de Lazar du 27 octobre : « ne pas promettre de révolution, mesurer ce qui sort » (`docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v2.md:225-252`, `dffe0b63…` ; famille MAT, l. 1319-1331).
- **Fermeture.** N12 (b) du 1er novembre : les couches 3 et 4 restent fermées jusqu'aux résultats de l'étape 2. Une seule exception : un **essai sur processeur « preuve formelle contre suite bon marché »**, sur devis (`registres/decisions.md:1188`, R-959).
- **Trois pas fixés par Lazar le 10 novembre** pour le pilier « mathématiques nouvelles » (`registres/decisions.md:2157`, R-2199) :
  - (a) lecture du tour 2 du collisionneur sur N12 et N13, faite (`docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md`, `6ef6bc2e…`). Aucune espèce n'y parle de génération de mathématiques nouvelles (§ E.3) ;
  - (b) devis de l'essai, puis GO ;
  - (c) note de conception du pilier « génération ».
- **L'essai (b), ou la défense par vérification.** Banque de preuves courtes où un tiers plante des erreurs de cinq classes (K1 à K5). On compare deux bras, avec le même modèle et le même plafond par item :
  - le bras L : formalisation en Lean 4 avec Mathlib, puis noyau de Lean et audit de fidélité ;
  - le bras S : une « suite bon marché » (calcul symbolique et numérique, contre-exemples, mutations, relecture par une autre famille).

  L'essai ne rouvre pas la couche 4 et ne dit rien de la génération (`brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md:13-38, 67-75, 508-557`, `717259ed…`). Il se paie en trois pas :
  - **D-1a**, l'outillage seul, sur une machine dédiée isolée, sans appel de modèle ;
  - **D-1b**, le pilote, seulement après un préenregistrement complet, contre-lu et scellé ;
  - la phase 2 de confirmation (`registres/decisions.md:2188`, R-2230).
- **Le pilier (c), ou les mathématiques nouvelles.** C'est une chaîne de six maillons : proposeurs, formalisation, Lean comme arbitre, juge de nouveauté, juge d'utilité, relecture humaine. « Vrai », « neuf » et « utile » s'y mesurent sur des oracles plantés, jamais sur le verdict d'un juge seul (N-058). Cinq questions du programme y sont visées (`docs/notes/ideation-organisme-v1/pilier-generation-v1/note-conception-pilier-generation-v1.md:25-51, 92-112`, `94532165…`) :
  - Q1 : clôture de l'archive pour le juge de l'organisme ;
  - Q2 : plafond d'horizon face à H2 ;
  - Q3 : agrégateur sous corrélation adverse, ce qui est **défensif** ;
  - Q4 : lemme maître d'impossibilité ;
  - Q5 : sonde qui ne lit que l'indication.

  **Côté attaque**, la note ne prévoit que l'attaque contre la chaîne elle-même : banc de tricheurs, cibles fausses plantées, attaque adaptative de Goodhart sur l'arbitre (§ 2.4, § 3.4, B4). Elle exclut toute recette d'attaque (l. 89, 368).
- **Décisions de Lazar sur la note** (« go recos », `registres/decisions.md:2223`, R-2265) :
  - **DP-1 (a)** : la note est une pièce au dossier ; **rien ne se prépare avant l'étape 2 et l'essai Lean** ;
  - **DP-5 (c)** : le rattachement au papier C se décide après l'essai et la collision avec Qu, Chen et Wang ;
  - DP-2 (a), DP-3 (a), DP-4 (c) et DP-6 (a) sont gardées comme dessin ;
  - D-1a (i) et D-2 (i) sont accordées pour l'essai (GO-2026-11-10-13).
- **Pas de lien avec G0.** Aucun document qui fait foi ne nomme Lean, et les critères de G0 n'en dépendent pas (`registres/etat.md:356-357`). Les consignes de ce chantier sont seulement rangées sous `docs/notes/g0-deux-semaines-v1/`. La « couche 4 » de ce chantier est celle de l'organisme d'idéation, pas une couche de réseau (comme la « couche 4 » de la lentille neuronale, R-3083).

## 2. Où il s'est arrêté

- **Harnais de l'outillage.** Dix versions, de `prep/lean-outillage-d1a-v1` à `v10`, toutes poussées. La dernière est la branche **`prep/lean-outillage-d1a-v10`, tête `ae894d8d`** (code `5103a7f3`). Elle porte le vérificateur du noyau v6, compilé contre Lean 4.35.0 et Mathlib `56a00585…`. Hors machine, 39 cas sur 39 sont conformes et 176 mutations sur 176 sont tuées (`registres/decisions.md:2445`, R-2486).
- **Dernière contre-lecture** (Claude Fable 5.2) : « utilisable après corrections », aucune garde affaiblie. Une réserve E3 est gardée : les mutations ne prouvent pas que les artefacts détectent le retrait du rejeu (`docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/contre-lecture-courte-harnais-d1a-v10.md`, `e7bdbb15…` ; `registres/decisions.md:2446`, R-2487).
- **Dernière pièce scellée** : la consigne du poste pour le troisième essai, `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/consigne-poste-local-lean-d1a-v3.md` (`17914672…`). Sa vérification courte la juge « exécutable » (`verification-courte-consigne-v3-v1.md`, `82734f0d…` ; `registres/decisions.md:2447`, R-2488).
- **Dernier mot de Lazar** (13 novembre, 07:47 UTC) : « Lean : le troisième essai est à lancer sur ton poste. :go » (`registres/decisions.md:2451`, R-2492). La passation `registres/passations/2026-11-13-1553.md:48` le reporte, et `registres/etat.md:142` aussi (13 novembre, 17:32 UTC). **Aucune ligne de registre, aucune passation et aucune dépense ne mentionne Lean après le 13 novembre.**
- **Derniers essais faits** :
  - premier essai, le 12 novembre, serveur 175751342 : pas `noyau` non conforme (0 sur 18), parce que les fichiers compilés de Mathlib étaient illisibles pour l'utilisateur isolé (`registres/decisions.md:2372`, R-2414) ;
  - second essai, le 12 novembre, serveur 175838427 : `noyau` non conforme (0 sur 18), parce que le vérificateur v4 ne compilait pas sous Lean 4.35.0. Les autres corrections ont été éprouvées conformes (`registres/decisions.md:2396`, R-2438). Le mot « Réparer d'abord, puis relancer » a conduit au harnais v10 (`registres/decisions.md:2397`, R-2439).
- **Dernier verdict** : aucun verdict de porte ; il n'y a pas de préenregistrement sur ce chantier. Le dernier « verdict » est l'issue de fin normale du second essai : `noyau` non conforme.
- **Branches des données du poste** :
  - `donnees/lean-outillage-d1a-poste-local-v1` (tête `1311bc44`) ;
  - `donnees/lean-outillage-d1a-poste-local-v2` (tête `3b2a74a2`) ;
  - **`donnees/lean-outillage-d1a-poste-local-v3` existe sur le dépôt distant à `ae894d8d`, sans aucun commit propre** (relevé par `git ls-remote` ce jour). La branche du troisième essai a donc été poussée, mais aucun rapport L3 n'y figure. Qu'est-ce qui a été fait sur le poste ? **Inconnu, à demander à Lazar.**
- **Serveurs.** Les deux serveurs Lean ont été détruits par leur identifiant : 175751342 le 2026-11-12 à 00:24:07Z, et 175838427 le même jour à 14:39:50Z. Clés et pare-feu ont été supprimés (`registres/arrets.md:94, 101`). Leurs tâches de destruction ont été supprimées (`registres/decisions.md:2375, 2396`). **Inventaire Hetzner relu ce jour vers 06:10 UTC, en lecture seule : aucun serveur dans le projet.**
- **Dépense totale** : 0,56 USD, soit deux fois 0,28 USD (`registres/depenses.md:416, 422, 427`).

## 3. Ce qui manque pour reprendre

- **Troisième essai de l'outillage (D-1a)** :
  - **GO en vigueur** : GO-2026-11-10-13 (65 USD, 0,56 dépensés, **échéance 2026-11-30**), avec une troisième machine accordée par R-2439 (`registres/go.md:303`). Coût attendu : environ 0,28 USD par essai (une heure facturée d'une `ccx33`).
  - **Machine** : le **poste de Lazar sous WSL**, terminal ouvert pendant tout l'essai. Le serveur loué est une Hetzner `ccx33`, créée et détruite par la procédure. Le poste est nécessaire parce que le nuage refusait le SSH sortant le 11 novembre (`registres/decisions.md:2255`, R-2297). Ce refus n'a pas été revérifié depuis.
  - **Pièces à reprendre avant de lancer** (travail, sans dépense) :
    - la consigne v3 nomme une ancienne session mère (`session_01XJ6Mgn4MZR4nxqK44C8Ea3`, l. 3 et 5) et la branche `…-poste-local-v3`, déjà poussée. Il faut un erratum ou une v4 qui nomme la mère actuelle et, si besoin, une branche neuve, puis une vérification courte ;
    - de son côté, la mère doit faire les gestes M1 à M6 au rapport L3 : vérifier le fichier de rattrapage, armer les tâches de destruction T1 à T3 et écrire la ligne « en tâche jusqu'à ».
- **Pilote D-1b (essai preuve formelle contre suite bon marché)**. Il se prend seulement après un outillage conforme.
  - **À écrire** : le préenregistrement complet, à partir du brouillon 3 (`717259ed…`). Restent 20 pièces « À REMPLIR » (§ 9, décompte de R-2240) et le marqueur `<<SOURCE_TANGO>>`, qui demande la lecture sur PDF de la source du score apparié (R7). Les § 3.6, A8 et § 4.5 n'ont jamais été contre-lus (`registres/decisions.md:2198`, R-2240).
  - **Rédaction** : par Fable 5.2, avec contre-lecture par Opus 5.5 (`CLAUDE.md:58`).
  - **Devis v5** (dans le brouillon, pas un GO) :
    - D-1b : plafond **578 USD d'appels plus 35 USD de machine**, pour un attendu d'environ 337 à 457 USD (606 à 726 au profil pire réaliste) ;
    - phase 2 : plafond indicatif **1 950 USD plus 91** ;
    - somme des plafonds : 2 719 USD, enveloppe d'environ 3 252 à 3 865 USD au profil pire réaliste.
  - **Ligne de GO neuve exigée** : aucune n'existe.
- **Pilier « génération »** (mathématiques nouvelles) :
  - **fermé** tant que l'étape 2 n'a pas rendu de résultats (N12 (b)), et DP-1 (a) interdit toute préparation avant l'étape 2 et l'essai Lean. Rouvrir le pilier, c'est **modifier une décision de Lazar** (nœud) ;
  - aucun devis, seulement des ordres de grandeur d'un pilote : environ **600 à 3 000 USD d'appels**, 3 à 130 USD de machine, 2,5 à 20 heures de relecture humaine (note du pilier, Verdict, point 4) ;
  - antériorités du § 6.3 non vérifiées sur PDF (DP-6).
- **Règle des trois chantiers actifs** : Lean n'en fait pas partie. Les trois chantiers actifs sont le saboteur et les sondes pour l'entretien, le bras A et l'organisme v9 (`CLAUDE.md:56`). Reprendre Lean au-delà d'un geste ponctuel demande donc de fermer un chantier actif, ou un mot de Lazar.

## 4. Liens avec les chantiers actifs

- **Organisme d'idéation (v9).** Le chantier Lean est sa couche 4. Il dépend de l'étape 2 de l'organisme (N12 (b)), dont je n'ai pas lu l'état dans cette pièce. N-058 (les proposeurs se jugent sur des oracles plantés et le coût) s'étend au pilier par DP-4 (c).
- **Papier C (juges de la recherche automatisée sous attaque, N-065).** L'attaque de Goodhart sur l'arbitre formel et sur le juge de nouveauté (B4) suit la méthode de l'attaque A1. Le rattachement au papier C est une décision de revendication, renvoyée après l'essai (DP-5 (c)).
- **Saboteur et sondes, G1.** Les questions Q2 à Q5 du pilier touchent H2, l'agrégation des moniteurs et le lemme d'impossibilité. Elles reposent sur une carte des hypothèses que la note dit hors de `main` : aucune cible ne se scelle avant sa version corrigée (note, l. 108-111). Je n'ai trouvé aucun lien opérationnel avec le saboteur ni avec le bras A.
- **G0.** Aucun lien (§ 1).
- **« Monde riche »** : c'est un chantier de l'organisme (course à plusieurs générations, `registres/decisions.md:2431, 2451`). Il partageait seulement le conteneur avec le développeur Lean lors des redémarrages du 12 novembre (R-2472, R-2473).

## 5. Voies de reprise

1. **Finir l'outillage avant le 30 novembre** (sous GO-2026-11-10-13, environ 0,28 USD).
   - Premier pas : demander à Lazar ce que la session de son poste a fait sur `donnees/lean-outillage-d1a-poste-local-v3` ;
   - puis faire écrire l'erratum ou la consigne v4 (mère actuelle, branche neuve si besoin), avec une vérification courte ;
   - ensuite, Lazar lance sur son poste WSL et la mère arme la destruction.
   - C'est la seule voie sans nouveau GO.
2. **Préparer le pilote D-1b**, une fois l'outillage conforme.
   - Premier pas : un mandat à un rédacteur Fable 5.2 pour tirer le préenregistrement du brouillon 3 (20 pièces, source du score apparié lue sur PDF), contre-lu par Opus 5.5 ;
   - puis une demande de GO sur une ligne neuve (environ 578 plus 35 USD).
   - C'est un quatrième chantier : il faut le mot de Lazar.
3. **Rouvrir le pilier « mathématiques nouvelles »** (attaque et défense au sens théorique).
   - Premier pas : soumettre à Lazar un nœud, au format de décision, sur la levée partielle de DP-1 (a) et de N12 (b) pour un seul pas sans dépense de modèle. Exemple : formaliser dans Lean la cible d'étalonnage (le score apparié, énoncé connu) une fois l'outillage conforme. On pourrait aussi lire d'abord les antériorités du § 6.3 (DP-6), ce qui relève de la veille, aujourd'hui gelée.
   - Aucun objet d'attaque ne se construit (R-607).
