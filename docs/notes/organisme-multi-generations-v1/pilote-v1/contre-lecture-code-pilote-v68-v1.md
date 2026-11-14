# Contre-lecture du code v68 du pilote MR-2 (C-1 à C-18) — v1

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), sous-agent neuf de la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. Je n'ai écrit
  ni le code, ni le texte du pilote, ni la mesure. **Réserve de lignée** : même maison que le développeur (Claude Opus 5.5) ; Fable 5.2
  est aussi proposeur du pilote.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-contre-lecteur-code-pilote-v68-v1.md`,
  `11c4141ac460fd7447d8a350e82ad24953ba3259d4fe6eed4894f39c7ef65e1b`, égale à son compagnon.
- **Heures** (`date -u`, 13 novembre 2026) : début 12:50:59 ; suite des 51 essais 12:57:47 à 12:59:27 ; huit mutations 13:01:00 à
  13:16:02 ; épreuves directes 13:16:12 ; essai à blanc A 13:16:28 à 13:16:32 ; fin : dernière ligne.
- **Aucune dépense, aucun appel de modèle, aucune clé lue.** Réseau : la seule boucle locale des essais (relais à amont factice).
  Calculs : un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`. Aucune écriture git ; un clone en lecture de l'arbre de
  l'organisme dans mon bac à sable. Aucun refus de permission ni de classifieur.
- **Deux écarts de ma part, dits** : (1) une commande `git status --short | head -5` sur l'arbre de travail du développeur a affiché
  cinq **noms** de fichiers sous `diag/` (courses du 4 octobre : factice et T0.3) ; aucun contenu lu, aucun chemin de 7a, de 7b ni du
  bras d'attaque ; non répété. (2) Pour Q-4 et Q-5, j'ai lu la table des modèles de la compétence locale `claude-api` (cache du
  3 novembre, celle que cite le plan des crédits) : lecture locale, sans réseau ; ce qu'elle dit est **non opposable** (R7).

## 0. Verdict

**Autorisable après corrections.** La chaîne hors ligne est saine : intégrité entière, 51 essais passés chez moi, essai à blanc A
rejoué à l'empreinte près, mesure égale à l'originale à l'octet, gabarit conforme à R-2504. Rien de ce que j'ai lu ne fausse la
mesure ni ne sort un devis de monde. **Mais le code gelé ne peut pas partir en mode réel, et ce qui garde le mode réel n'est ni
complet ni éprouvé** : 2 constats bloquants, 10 majeurs, 14 mineurs. Le bloc gelé `27311ce3…` est provisoire : le relais et la
configuration doivent changer avant tout appel, donc une **contre-lecture du différentiel** est due.

Mes huit mutations (choisies là où la lecture montrait une garde sans artefact) **survivent toutes** à la suite entière des 51 essais.

## 1. Intégrité (tout conforme, deux remarques)

| contrôle | résultat |
|---|---|
| pièces du dépôt de travail (brouillon 4 `04ada9fa…`, mesure `676d5f37…`, consigne du développeur `3b4f570c…`) | égales à leurs compagnons |
| livrables du développeur (rapport `6635e43a…`, paquet `43d09adc…`, patch `70c68837…`, bloc `27311ce3…`, journal `f19dee5c…`, bancs `f2198fd1…` et `2f20ecf5…`, paquet du jalon 1 `0c990e83…`) | égaux à leurs compagnons |
| `git bundle verify` du paquet v1 | « is okay » ; exige `ab53b7f4…` ; tête `276b6afde8310b12af6f7c776ab4ee4c58d50e79` |
| branche du dépôt de travail du développeur | `prep/pilote-mr2-v1`, tête `dec76f42…` |
| patch contre `git diff ab53b7f 276b6afd` | **le patch n'est pas ce différentiel** (`00f6bfb8…`, 406 673 octets) : c'est `git format-patch --stdout ab53b7f..276b6afd` (deux commits), **égal à l'octet** à celui que je recalcule (`70c68837…`) ; appliqué sur `ab53b7f` dans un second clone, il rend les 35 fichiers de `276b6afd` (35 comparés, 0 différent) ; 35 ajouts, aucune modification |
| bloc gelé contre les fichiers | 27 lignes d'empreintes, 27 « OK » (`sha256sum -c`) ; `pilote_mr2_v68.py bloc` rend `27311ce3…` |
| empreinte du gabarit | recalculée : `2b1b33ec0e72ad64cde462487a87108e03b1d63690d81f609a9ad728ef3ce753` |
| copie portée de la mesure | `cmp` : égale à l'octet à `pilote-v1/outils/mesure_pilote_v4.py` ; les 13 outils portés et leurs 13 compagnons égaux à ceux du dépôt de travail (13 comparés, 0 différent) |

Remarques : le rapport dit « 31 fichiers gelés », le bloc en porte 27 (mineur m-1) ; l'essai nommé « …égaux aux compagnons et au
dépôt de travail » ne compare qu'aux compagnons (je l'ai fait à la main).

## 2. Ce que j'ai fait par moi-même

- **Suite des 51 essais** dans mon clone : `51 passed, 42 subtests passed in 100.06s` (`contre-lecture-code-v68-outils/essais-51-contre-lecteur-v1.txt`, `6a2012ff…`).
- **Essai à blanc A** sur les mondes de développement existants : 16 complets ; `CARTES.json` `d61dfc80…` et corps de la mesure
  `78d30796…`, **égaux à ceux du développeur** ; issue P-2 avec réserve R-1 ; écarts de coût nuls ; rapatriement 109 fichiers, aucun
  monde ; mode réel refusé (code 2, rien créé).
- **Huit mutations hors de la liste du développeur**, suite entière à chaque fois (`mutations_contre_lecteur_v1.py` `240d9d1c…`,
  résultat `mutations-contre-lecteur-v1.json` `37c2b79a…`) :

| # | garde mutée | fichier | issue |
|---|---|---|---|
| N1 | mode réel : lecture des deux lignes de GO supprimée (`go = None`) | lanceur l. 150 | **survit** |
| N2 | mode réel : empreinte du texte scellé non comparée | lanceur l. 146 | **survit** |
| N3 | relais non branché admis avant tout appel | `proposeurs_pilote_v68.py` l. 259 | **survit** |
| N4 | relais : modèle, plafond = part, appels et dépense à zéro non contrôlés | idem l. 261-263 | **survit** |
| N5 | relais : usage absent réglé à 0 au lieu du pire cas | relais l. 276-277 | **survit** |
| N6 | commande : coût lu au-dessus du pire cas admis | commande l. 207 | **survit** |
| N7 | témoin d'isolement : « aucun outil » non contrôlé par l'adaptateur | `proposeurs_pilote_v68.py` l. 204 | **survit** |
| N8 | rapatriement : marques de contenu d'un monde ignorées | `audit_pilote_v68.py` l. 70 | **survit** |

  Lecture honnête : ces huit mutations ne sont pas un échantillon ; je les ai placées là où je ne voyais pas d'artefact. Elles
  prouvent huit trous de R5, pas un taux.
- **Épreuves directes** (`epreuves_contre_lecteur_v1.py` `eec45146…`, sortie `epreuves-contre-lecteur-v1.json` `ec047888…`), citées
  E1 à E17 dans les constats.

## 3. Constats bloquants

**B-1 — Le code gelé ne peut pas faire le pilote ; le gel est provisoire.**
Où : `relais_pilote_v68.py` l. 178-179 (`NonBranche` pour Claude), l. 184-186 (Astra) ; `configuration-pilote-mr2-v9.json` (quatre
listes « a_confirmer » non vides) ; lanceur l. 143.
Preuve : `jouer --mode reel` rend « points à confirmer », code 2 (rejoué). Brancher Claude (flux, reconstitution du message),
confirmer Astra et Argon changent le relais, donc son empreinte, donc la configuration, donc le bloc `27311ce3…`.
Conséquence : la partie du code la plus sensible (clé, dépense, lecture de la réponse de 8 appels sur 16) **n'existe pas encore** et
n'est donc pas contre-lue. Le préalable « code contre-lu, gelé » du texte n'est pas rempli par cette lecture.
Correction : écrire la voie de Claude sous un nom neuf, vider les « a_confirmer », régénérer le bloc, puis **contre-lecture du
différentiel** par un autre modèle avant le scellement du texte. Ce n'est pas une faute du développeur : sa consigne disait « à
décrire, pas à brancher ».

**B-2 — En mode réel, le lanceur ne sait pas quel relais lui répond, et aucune garde du mode réel n'a d'essai.**
Où : `exiger_relais_prets`, `proposeurs_pilote_v68.py` l. 250-265 ; `/relais/etat`, relais l. 236-239 ; `appel_reel` l. 184-186 ;
lanceur l. 142-150.
Preuve par lecture : (a) un relais lancé avec `--appelant factice:…` a `branche` vrai (relais l. 209) et passe `exiger_relais_prets` :
**un « mode réel » peut tourner sur des proposeurs factices** et rendre des cartes exportées comme réelles (seul le manifeste garde
`appelant`). (b) Ni le prix du relais, ni `max_appels`, ni l'adresse d'amont, ni l'empreinte du fichier qui tourne ne sont
contrôlés (E12 : champs de `/relais/etat`). (c) Pour Astra, la clé part en `Authorization: Bearer` vers `--url-amont`, argument
libre, sans contrôle de schéma ni d'hôte ; le collisionneur, lui, refuse toute adresse autre que celle d'OpenAI ou la boucle locale
(`collisionneur_v8_plafonds_bas_v1.py` l. 564-567). (d) Aucune procédure écrite ne lance les relais réels (`lancer_relais` n'est
appelé qu'à blanc).
Preuve par mutation : N1, N2, N3, N4 survivent. Le seul essai du mode réel s'arrête au premier refus (« à confirmer ») : la lecture
des GO, l'empreinte du texte, le bloc et l'état des relais ne sont jamais traversés par le lanceur dans un essai. R5 n'est pas tenu
pour les gardes qui autorisent la dépense.
Correction : le lanceur lance lui-même les relais en mode réel (clé passée par son **nom**, environnement bâti par filtrage) ou,
à défaut, `/relais/etat` rend l'empreinte du fichier, les prix, `max_appels`, l'hôte d'amont et `cle_presente`, et le lanceur exige
`appelant == dialecte` ; adresse d'Astra figée dans la configuration gelée (hôte exact, `https`) ; un essai du mode réel de bout en
bout sur relais factices **déclarés comme tels par une doublure d'essai seulement**, avec un artefact par garde (GO absent, montant
faux, texte altéré, bloc altéré, relais non branché, plafond ≠ part, appels déjà faits, appelant factice).

## 4. Constats majeurs

**M-1 — La règle du modèle servi refuse la forme datée d'OpenAI ; quatre appels payés peuvent être perdus par fournisseur.**
`commande_pilote_v68.py` l. 88-96 et l. 209. E3 : `gpt-6-astra-2026-10-15` refusé, `gemini-4-argon-preview-10-2026` refusé,
`gpt-6-astra-20261015` admis. Un modèle servi « différent » est un « échec » **sans abandon** (Q-8) : le défaut étant systématique,
les 4 appels du fournisseur sont payés et perdus, et n tombe à 12 au mieux.
Correction : lire la forme réellement servie dans les journaux du collisionneur (12 et 13 novembre, `gpt-6-astra` et
`gemini-4-argon`) ; écrire dans la configuration la liste exacte des identifiants servis admis par proposeur ; abandonner le
proposeur au premier modèle non conforme.

**M-2 — Un identifiant de fournisseur peut entrer dans ce qui est rapatrié.**
Relais l. 192 et l. 282 : le corps d'erreur de l'amont (2 000 caractères) est rendu à la commande, qui l'écrit dans
`corps-relais.json` (commande l. 179-180), pièce rapatriée. Les corps d'erreur des fournisseurs peuvent nommer une organisation, un
projet ou une clé masquée (su de mémoire, non vérifié ici). E6 : un `corps-relais.json` portant « organization org-… » et « sk-…
masquée » est **copié sans refus**. Le collisionneur masque la clé dans tout message d'erreur (l. 586, l. 593) ; le relais v68 non.
Correction : le relais ne rend de l'erreur d'amont que le statut et le type ; ou `rapatrier` refuse tout fichier qui porte un motif
d'identifiant (liste écrite) ; essai R5.

**M-3 — Le manifeste rapatrié dit la structure de chaque monde.**
`jouer_c16`, `pilote_mr2_v68.py` l. 634, et lanceur l. 128 : `controles.c16["r:monde_sans_latente"].conditions` (nombre de conditions
emboîtées de la loi du monde) est écrit par monde. Le manifeste déjà versé de l'essai à blanc A le montre : la valeur change d'un
monde à l'autre. Le texte a retiré de la mesure la composition des mondes « jamais publiés » (S-9, R-2510) ; le manifeste la
réintroduit en partie. `exiger_manifeste_sans_loi` (liste de clés interdites) ne le voit pas.
Correction : n'écrire au manifeste que `admise` (et l'empreinte de la loi) ; garder `conditions` dans une sortie privée.

**M-4 — Un appel « complet » sans le corps du relais sur disque n'arrête rien.**
`appeler`, `proposeurs_pilote_v68.py` l. 182-190. E1 : état « complet », témoin conforme, `corps_relais_sha256` nul, **aucun arrêt** ;
E1b : corps présent, aucune empreinte rendue par la commande, admis (l. 189 accepte `None`). Le texte dit : réponse brute (corps
entier, raison d'arrêt, modèle servi, usage) absente → arrêt, code 3.
Correction : pour `complet` et `tronque`, exiger le corps sur disque, égal à son compagnon et à `brut_sha256` rendu ; essai R5.

**M-5 — « La mesure, une seule fois, sortie scellée » ne tient qu'à la main.**
Lanceur l. 21-22 (la mesure n'est pas lancée par le lanceur). Le programme de la mesure n'écrit pas de compagnon (vérifié sur mon
essai à blanc), ne consigne pas l'empreinte de `CARTES.json`, et accepte tout second lancement vers un autre chemin. `lire`
(l. 209-237) ne relie pas la sortie au `CARTES.json` du manifeste.
Correction : une sous-commande `mesurer` du lanceur : vérifie `CARTES.json` contre son compagnon et le manifeste, refuse si une
sortie de mesure existe déjà dans le dossier, lance le programme `676d5f37…` sans le modifier, scelle la sortie, écrit les deux
empreintes ; `lire` exige cette pièce.

**M-6 — L'audit R4 du texte n'a pas ses pièces après la destruction de la machine.**
Le texte demande, si x = 0 ou x ≥ 3, de « vérifier que les épisodes servis contiennent les traits », qu'« aucune pièce servie ne
décrit la famille », et de relire toutes les cartes refusées. Le lanceur ne garde aucun texte servi (empreintes seules, l. 122-133),
le contrôle `pieces_du_texte` y est une tautologie (l. 118-126 : le texte est comparé à lui-même), et `cartes_a_relire`
(`audit_pilote_v68.py` l. 51-62) ne rend que le tirage, pas la liste des refusées.
Correction : écrire au manifeste un contrôle mécanique des épisodes servis (400 épisodes, 8 traits finis et non constants, issues et
sous-populations vues : E8-E10 le montre faisable sans rien dire du monde) ; garder les textes servis dans le dossier privé, jamais
rapatriés ; dire dans le texte que l'audit R4, s'il est déclenché, se fait avant la destruction ; ajouter la liste des refusées à
l'outil.

**M-7 — Le manifeste ne tient pas R9.**
Lanceur l. 194-198 : ni version de Python ni de numpy, ni commit, ni règle des graines. Le texte dit numpy 2.5.3 ; les essais
tournent sous 2.4.6 (corps de la mesure égal, dit par le développeur ; la machine jetable aura la sienne).
Correction : versions, plate-forme, commit (ou empreinte du paquet) et règle de dérivation des épisodes au manifeste ; le lanceur
refuse en mode réel une version de numpy autre que celle du bloc.

**M-8 — La garantie « dure » du relais repose sur ce que la commande déclare, et sur du code sans artefact.**
Relais l. 246 et l. 255-262 : la réserve est `pire_cas_usd` lu dans la requête. E12 : deux requêtes déclarant 0,000001 USD pour
10⁶ jetons de sortie sont servies. Le relais connaît les prix et la consigne : il peut calculer son propre pire cas. N5 et N6
survivent : l'usage absent réglé au pire cas et le coût au-dessus du pire cas n'ont aucun essai.
Correction : le relais recalcule le pire cas (octets + 1024, borne, ses prix) et refuse une requête dont la borne dépasse celle de
son lancement ; essais R5 pour l'usage absent au relais et le coût au-dessus du pire cas.
Limite à dire dans le texte : le plafond n'est dur que si le fournisseur tient sa borne de sortie (réflexion comprise) et si les
prix de la configuration sont les vrais ; ceux de Claude et d'Astra sont « à confirmer ».

**M-9 — La règle d'extraction des cartes est fixée en silence et peut sortir un appel du dénominateur.**
`extraire_propositions`, `pilote_mr2_v68.py` l. 587-599 (héritée de la v64). E5 : bloc sans étiquette, étiquette en majuscules,
phrase avant un JSON nu, ou deux blocs dont le second seul porte la liste → 0 carte, donc « sans carte », hors du dénominateur. La
consigne servie dit « un bloc JSON », sans dire la clôture attendue.
Correction (texte, avant scellement) : écrire la règle dans « Métrique » ; ou dire dans la consigne servie « un seul bloc
```json » (l'empreinte du gabarit change) ; rapporter au relevé le nombre d'appels complets illisibles (déjà dans `gardien`).

**M-10 — Six gardes n'ont pas d'artefact (R5).**
Outre N1 à N4 (B-2) : N5, N6 (M-8), N7 (les huit conditions du témoin ne sont éprouvées qu'ensemble, par deux empreintes fausses),
N8 (un monde n'est reconnu dans l'essai que par l'empreinte du fichier ; or `--mondes-sha256` est facultatif et la marque de contenu
est alors la seule garde). Non mutées mais sans essai à ma lecture : contrôle du modèle par le relais (l. 251), garde des octets du
texte servi (lanceur l. 120), « chaque proposeur dans une seule ligne de GO » (`proposeurs_pilote_v68.py` l. 94).
Correction : un artefact par garde ; rejouer mes huit mutations, attendues tuées.

## 5. Constats mineurs

- **m-1** Rapport : « 31 fichiers gelés » pour 27 ; le patch est un `format-patch`, pas un `git diff` (équivalent, section 1).
- **m-2** `charger_mondes_prives` sait comparer les empreintes des mondes à une liste du registre ; le lanceur ne la passe pas
  (l. 108). L'empreinte « du registre » est un argument tapé.
- **m-3** `generer` prend `--texte-sha256` sans le comparer à un fichier ; rien ne lie les mondes au texte que `jouer` vérifie.
- **m-4** Le lecteur des GO ne regarde pas le périmètre : toute ligne de calcul valide au montant exact passe.
- **m-5** À un arrêt (code 3), ni relevé ni manifeste partiels : seules les pièces par appel restent. Une exception imprévue sort
  en code 1.
- **m-6** Le plafond d'une ligne de GO vaut pour **un** lancement de `jouer` : des relais neufs repartent à zéro. À écrire : un seul
  lancement réel ; tout second lancement est un nœud.
- **m-7** Délai de l'adaptateur (commande tuée) → arrêt du pilote entier (E2), alors que l'en-tête du module range le délai parmi les
  pannes (échec, abandon, on continue). Le délai propre de la commande tombe 30 secondes avant : cas rare, à dire.
- **m-8** Une erreur passagère de l'amont (429, 5xx) abandonne le proposeur dès la première et se compte au pire cas : conforme au
  texte (« aucune reprise »), mais le collisionneur reprend quatre fois. Risque de P-0 à dire à Lazar.
- **m-9** `subprocess.run(text=True)` sans `encoding="utf-8"` (l. 176) : sous une autre locale, les empreintes divergent et le pilote
  s'arrête (échec sûr, pas silencieux).
- **m-10** La K1 servie n'est pas passée au gardien avant les appels ; une K1 hors de ±4 ferait refuser toute carte bâtie sur elle
  (E8 : admise sur les quatre mondes de développement). À ajouter à C-16.
- **m-11** Le relais écoute sans authentification sur la boucle locale ; tout processus de la machine peut consommer un appel.
- **m-12** Astra : un refus servi par le champ `refusal` avec `finish_reason` « stop » est lu « complet » puis « sans carte »
  (le collisionneur le lit « refus ») ; `completion_tokens` est supposé contenir la réflexion, le collisionneur l'ajoute.
- **m-13** `lire` vérifie les modules listés, pas que la liste est complète ; `rapatrier` ne vérifie ni compagnons ni schéma : un
  fichier au nom permis portant une loi compilée, une graine ou des épisodes est copié (E6). Aucun chemin du code gelé n'en écrit.
- **m-14** `secondes_de_chaine.appels` de la mesure (scellée) dit le nombre de secondes conditionnelles des mondes : à relire au
  regard de S-9 (hors de mon mandat).

## 6. Conformité au texte, C-1 à C-18

| # | verdict | ce que le code fait de plus, de moins ou d'autre |
|---|---|---|
| C-1 | conforme | moins : empreintes des mondes non comparées au registre par le lanceur (m-2) |
| C-2 | **écart** | le manifeste porte `conditions` par monde (M-3) |
| C-3 | conforme | dérivation des épisodes fixée par le code (Q-10) |
| C-4 | conforme | outils portés à l'octet ; étiquette « v52b » fausse sur la machine (Q-12) |
| C-5 | conforme | plus : indices entiers, bornes de sûreté 50, profondeur 40, énoncé ≤ 400, `defaut` compté (Q-3), égalité des deux évaluateurs au gardien ; 3 admise et 4 refusée essayées |
| C-6 | conforme | six types (ceux de la v64) ; rien sur les conditions du monde ; empreinte recalculée |
| C-7 | **incomplet** | voie de Claude non écrite (B-1) ; un relais par proposeur et non par fournisseur (plus fin, cohérent avec le minimum) ; effort et réflexion non réglés (Q-4) ; délais 3 600 et 1 800 s fixés par le code |
| C-8 | conforme sous hypothèse | champs d'Astra supposés ; modèle servi lu dans le corps, pas dans un en-tête ; règle du suffixe (M-1) |
| C-9 | conforme | parts `fable52` 12 et `opus55` 8 au lieu d'une part « claude » ; gardes sans essai en mode réel (B-2) |
| C-10 | **écart** | corps entier non exigé (M-4) ; témoin éprouvé en bloc (M-10) |
| C-11 | conforme à blanc | mode réel non éprouvé (B-2) |
| C-12 | conforme | K1 de la mesure, six décimales contrôlées ; K1 non gardée (m-10) |
| C-13 | conforme | export relu par la mesure, empreinte égale à celle du développeur |
| C-14 | **incomplet** | lecture du champ `regle` et coûts conformes ; mesure et scellement à la main (M-5) |
| C-15 | conforme | graine appelée dans le programme v4 ; `--texte-sha256` non vérifié (m-3) |
| C-16 | conforme | arrêt essayé ; Q-2 ouverte |
| C-17 | conforme | écart maximal 3,9·10⁻¹⁶ à l'essai à blanc ; artefact essayé |
| C-18 | **incomplet** | rapatriement : garde de contenu sans essai (N8), identifiants de fournisseur (M-2) ; audit sans ses pièces (M-6) |

Réglages que le texte ne fixe pas et que le code fixe : règle d'extraction (M-9) ; suffixes du modèle servi (M-1) ; aucun réglage
d'effort ni de réflexion (Q-4) ; délais ; `octets_entree_max` 52 000 ; ports ; bornes de sûreté 50, profondeur 40, énoncé 400 ; jeu
factice de 90 instances ; 256 épisodes par monde pour C-17 ; graine des épisodes ; identifiant opaque de K1 ; codes de la commande
rangés en « panne » (2, 3, 4, 6) ou « non conforme » (5).

## 7. Secrets, plafonds, isolement, mesure : ce qui tient

- **Secrets** : clé lue par son nom dans le seul relais (l. 314), jamais en argument, jamais au journal ; environnement de la
  commande bâti à neuf, cinq noms, aucune clé (l. 171-172) ; aucun `ANTHROPIC_BASE_URL` ; aucun repli de modèle ; en-têtes d'amont
  réduits à trois. Restent B-2 (c) et M-2.
- **Plafonds** : pire cas par appel vérifié deux fois (configuration et commande) ; troncature : état « tronque », coût lu ; refus :
  échec, coût lu ; usage absent : pire cas des deux côtés (non éprouvé au relais, N5). Restent M-8, m-6.
- **Isolement** : texte servi = consigne, gabarit, {K1}, 400 épisodes, rien d'autre (E8-E10 : quatre clés au contexte) ; un message,
  aucun outil, aucun système ; empreinte du texte suivie du lanceur au relais.
- **Mesure** : dénominateurs, tronqués, échecs, sans carte, témoin et issues rendus par le programme scellé, appelé sans copie ; graines
  par `SeedSequence` (épisodes, cartes relues).

## 8. Avis sur Q-1 à Q-12

| # | option recommandée | pourquoi | ce que cela change |
|---|---|---|---|
| Q-1 | **(c) relever Argon et Astra, garder Fable 64 000 et Opus 89 000** | 29 000 est sous les « ≈ 30 000 jetons » de six arbres pleins, réflexion comprise : troncatures probables, donc P-0 probable | chiffres ci-dessous ; décision de Lazar (dépense) ; configuration, bloc, texte |
| Q-2 | **(d) neuve : récrire la loi hors bornes en `transformee`** ; à défaut (c) | E4 : une feuille à 5,25 est refusée, la même loi écrite avec `puissance` est admise, écart 1,4·10⁻¹⁵ : la loi du monde **est** dans la grammaire servie | texte (S-b, C-16) et lanceur ; ni famille, ni gardien, ni mesure |
| Q-3 | garder le compte du gardien (`defaut` compris) | c'est la phrase du gabarit servi (« tout chemin de la racine à une feuille ») ; égal à la référence sans `defaut` | une ligne du texte (C-5) |
| Q-4 | écrire l'effort dans la configuration et l'envoyer | la table locale dit défaut « high » pour Fable 5.2 et « medium » pour Opus 5.5 : deux proposeurs inégaux sans l'avoir décidé | décision de Lazar ; relais, gabarit du texte |
| Q-5 | voie = interface Messages, clé d'organisation, en flux, sans repli | voir ci-dessous | relais (B-1) ; ligne π1 |
| Q-6 | reprendre la voie du collisionneur | voir ci-dessous | relais, configuration |
| Q-7 | relais v68 pour Argon | même corps que `appeler_gemini`, éprouvé ; le relais v6 ne satisfait pas C-10 | un essai en ligne (dépense) |
| Q-8 | refus du modèle : échec sans abandon ; **modèle servi différent ou usage absent : abandon** | ces deux défauts sont systématiques (M-1) | texte (liste d'arrêt), lanceur |
| Q-9 | aucune borne de taille au pilote ; la course reprend ce gabarit | sinon p_c ne se transporte pas | texte de la course |
| Q-10 | garder ; écrire la dérivation au texte | déterministe, rejouable depuis le monde | une ligne du texte |
| Q-11 | ne rien pousser vers le dépôt public avant la fin de la course | le générateur et la mesure y seraient | décision de Lazar |
| Q-12 | garder ; dire que l'étiquette « v52b » est fausse sur la machine | chemin inerte ; même validateur que C-4 | rien au pilote ; outil neuf pour la course |

**Q-1, chiffres** (prix 10 / 50, entrée 52 000 octets + 1 024, vérifiés par `lire_configuration`, E11) :

| | par appel, au pire | plafond de session | part (4 appels) | ligne |
|---|---|---|---|---|
| Argon, Astra à 29 000 (gelé) | 1,98024 | 2,00 | 8,00 | π2 = 19,00 |
| Argon, Astra à 36 000, au plus juste | 2,33024 | **2,34** (2,33 refusé : borne payée 35 995) | 9,36 | π2 = **21,72** |
| Argon, Astra à 36 000, arrondi | 2,33024 | **2,50** (borne payée jusqu'à 39 395) | 10,00 | π2 = **23,00** |
| Fable 5.2 à 64 000 | 2,984192 | 3,00 | 12,00 | π1 = 20,00 |
| Opus 5.5 à 89 000 | 1,992096 | 2,00 | 8,00 | (même ligne) |

Total au pire : **41,72** (au plus juste) ou **43,00** (arrondi), contre 39. **Cohérent avec le code** : part = 4 × plafond, somme des
parts = montant, borne ≤ borne payée, bloc régénéré ; à changer aussi : l'essai des GO (« 19 USD » en dur), la table des
proposeurs, le devis, la ligne π2 et le « 39 USD » du texte. 36 000 reste mince si la réflexion est longue : le texte le dit déjà.

**Q-2, pesée de la règle de tirage (c).** Famille : elle devient « MR-2 dont aucune loi de référence ne sort de ±4 » ; un coefficient
passe 4 quand plusieurs effets s'empilent sur un trait, et la conditionnelle y contribue (− p, puis + 2p) : la sélection peut donc
toucher **la grandeur mesurée**. Mesure : formules inchangées, mais p_c ne vaut plus que pour la famille tronquée. Course et banc :
même règle, même code, sinon « p_c ne vaut que pour ce gabarit » tombe. Mise en œuvre : `generer_v4` (scellé) rend le premier tirage
conforme ; il faut une enveloppe neuve qui parcourt les mêmes huit sous-graines et écarte un tirage pour ce motif, oracle et K1
calculés par tirage ; les mondes écartés se rapportent par leur compte et leur motif seulement. (a) coûte environ une chance sur
trois d'arrêt (estimation du développeur, 2 sur 20 mondes non vérifiés) ; (b) laisse passer une loi que le gardien refuserait à un
proposeur. **(d)** n'a aucun de ces effets ; confiance 0,6 ; à voir avec le concepteur.

**Q-5, sans appel.** Le dépôt confirme : la route (`appeler_anthropic` du collisionneur : flux, aucun `thinking`, aucun `fallbacks`,
effort explicite, en-tête d'espace de travail si la clé l'exige) ; la variable nommée du compte (`RR_ANTHROPIC_API_KEY_RIGAUD` au
plan, quand le relais lit `ANTHROPIC_API_KEY` : à relier par le nom au lancement) ; les prix 8 / 40 et 4 / 20 (plan l. 44-47, table
en cache : à relire sur la page publique). Le plan ne prévoit **pas** la ligne π1 : ≈ 165 USD restants sur ce compte pour 160 USD de
plafonds déjà répartis ; dire le compte dans la ligne. Exige une sonde payante (ou une lecture de console par Lazar) : que
`claude-fable-5-2` et `claude-opus-5-5` sont servis sur ce compte à ces bornes (la table locale dit 128 000 jetons de sortie au plus
et une rétention de 30 jours exigée pour Fable 5.2), et la forme de l'identifiant servi.

**Q-6, sans appel.** Le dépôt confirme la forme : adresse `https://api.openai.com/v1/chat/completions`, `max_completion_tokens`,
`Authorization: Bearer`, champs `usage.prompt_tokens`, `completion_tokens`, `completion_tokens_details.reasoning_tokens`,
`finish_reason` (`stop`, `length`, `content_filter`), champ `refusal`. Les journaux des tours des 12 et 13 novembre (non nommés par ma
consigne, non ouverts) disent sans appel : l'identifiant servi exact (M-1), et si la réflexion est comprise dans
`completion_tokens`. Exige la page publique ou une sonde : le prix (10 / 50 est « supposé » partout).

## 9. Ce que je n'ai pas vérifié

Le banc des 43 mutations (lu, non rejoué) ; la génération des mondes et les contrôles C0 à C8 (non rejoués) ; l'essai à blanc B (lu) ;
le fond de la mesure v4 (scellée, relue par d'autres) ; les routes réelles (aucun appel) ; les registres et décisions R-25xx (non
nommés) ; l'écart entre le validateur de la v52b et celui de l'arbre ; tout fait d'interface de fournisseur au-delà du dépôt.

Fin de la rédaction : 2026-11-13 13:19:50 UTC (`date -u`).
