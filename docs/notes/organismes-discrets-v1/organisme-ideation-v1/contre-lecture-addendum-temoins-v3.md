# Contre-lecture de l'addendum des témoins du juge et du budget de pensée de Carbon, version 3 (organisme d'idéation, organismes discrets)

Contre-lecteur neuf (R2), modèle Opus 5.5. Je n'ai écrit ni l'addendum (v1, v2, v3), ni les témoins, ni leurs scripts, ni le
script d'épreuve, ni ses essais, ni les contre-lectures précédentes. 18 novembre 2026. Contre-lecture **courte**, limitée aux
parties changées depuis la v2, comme demandé.

Pièce lue : `addendum-temoins-et-carbon-v3.md` (`9dc26b54…`, non scellé au moment de la lecture, commit `a79c0de1`). Pièces
d'appui, empreintes vérifiées par leurs compagnons (toutes conformes) : `temoins-organisme-discrets-v5.json` (`8bec4254…`),
`ecrire_temoins_v5.py`, `temoins-organisme-discrets-v4.json`, `question-v3.md`, `faits-v3.md`,
`contre-lecture-addendum-temoins-v2.md` (`1db4f419…`), `scripts/epreuve_temoins_seuls_v3.py` (`31fd6e32…`),
`tests/test_epreuve_temoins_seuls_v3.py` (`102e81f3…`) ; journal de la relance (OD-024) ; `registres/go.md` (GO-2026-11-18-11,
-16) ; procédure `docs/procedures/relais-persistants-v1.md` § 2.1 ; orchestrateur épinglé (`a41b7b50`, arbre propre) :
`pole/ideation_v2.py`, `pole/adaptateurs.py`, `pole/relais_reel.py` ; journal du relais Claude des courses
(`/home/user/hors-depot/relais-organismes-discrets-v8/journal-relais-claude.jsonl`, usage et horaires seulement).

**Ce qui n'a pas été ouvert.** Aucune fiche de proposeur, aucun `fiches-*.json`, aucun dossier `proposeurs/`, aucun
`consigne.md` ni `reponse.md` de juge des courses. Écarts de forme, déclarés : `find … -name consigne.md` sous le dossier des
courses (noms de chemin seulement), puis `--verifier-gabarit` sur les deux consignes de juge (booléen seul affiché). Aucun
relais lancé, aucun appel payant ; rien n'écoutait sur 127.0.0.1:8787 (`/proc/net/tcp`, port 0x2253 absent) quand j'ai lancé
la commande exacte. Sorties de mes essais dans le bloc-notes de session, hors du dépôt ; aucun dossier
`runs/epreuve-temoins-seuls-v*` n'existe (vérifié avant et après).

## Verdict

**À corriger**, légèrement. Le bloquant de la v2 est levé : le relais à réserve 0,2 tient les deux requêtes du kit sous un
plafond de 0,5, et son état est contrôlé avant la création du dossier, comme le kit, le modèle, les noms de clé et le bac à
sable ; refus avant envoi en code 2, interruption pendant l'appel en code 3, rejeu refusé par le script v3, codes conformes au
§ 4 ; témoins v5 régénérés à l'identique, valides pour le code épinglé ; § 5 fidèle à la décision de la mère. Restent deux
significatifs, sans dépense : (1) le coût d'un appel en échec n'est toujours pas relevé là où il se perd (délai ou erreur du
kit : le résultat réel porte 0,0 USD et « coût connu »), et l'essai le masque ; (2) la distinction entre saboteur et jumeau
dérangé n'est écrite que dans le vrai témoin, alors que le jumeau doit franchir la porte seul et que le constat 5 la demandait
dans les deux fiches. Le premier se corrige par deux phrases de l'addendum (ou un script v4) ; le second par une phrase dans
le jumeau (témoins v6, consigne réépinglée) ou, à défaut, par l'aveu écrit que le jumeau est le plus exposé des deux.

## Vérifications faites

| point | résultat |
|---|---|
| Essais (`.venv`, `PYTHONPATH=src`) | 19 passés |
| Commande exacte, sans relais | `{"code": 2, "refus": "relais Claude illisible : URLError"}`, code 2, aucun dossier créé ; les contrôles de clé, de modèle et de kit sont passés avant (le refus vient du relais) |
| Épreuve à sec (`--a-sec --dossier <neuf>`) | code 0 ; 24 596 caractères ; empreinte `15e5b0d0…` = `CONSIGNE_ATTENDUE` = addendum l. 67-68 |
| Gabarit | égal aux consignes de juge d'Astra et d'Argon (code 0 les deux fois) |
| Environnement de la commande exacte | `claude_agent_sdk` 0.2.172 ; `etat_bac_a_sable_detaille()` : actif, `/proc` neuf ; `noms_de_cle_presents` : vide ; `verifier_modele_reel("claude-opus-5-5")` : passe ; `construire_options` (rôle `juge_ideation`, interdits = dossier imposé, dépôt, `~`) puis `options_sdk` : bâtis sans erreur — `tools` [], effort « medium », 2 tours, 0,5 USD : aucun `ValueError` ne peut sortir de `lancer` après la création du dossier |
| Ordre des contrôles (script l. 190-222) | empreinte de la consigne, dossiers `v*` existants, `verifier_avant_envoi` (clé, modèle, kit, relais), `adaptateur_reel` (bac à sable actif, `/proc` neuf sous root) : **tous avant** `os.makedirs(SORTIE)` (l. 222), dans le `try` qui rend 2 |
| Contrôle de l'état du relais (l. 164-168) | égalité exacte sur `plafond_usd` 0,5, `reserve_par_appel_usd` 0,2, `modeles_permis` [Opus 5.5], `depense_usd` 0, `appels` 0 ; les noms de champs sont ceux de `Compteur.etat()` et de `do_GET` (`relais_reel.py` l. 169-175, l. 228) ; `float("0.2")` = 0,2 : la comparaison exacte tient ; lecture sans mandataire (`ProxyHandler({})`) |
| Réserve 0,2 sous plafond 0,5 (`relais_reel.py` l. 152-157) | annexe réservée (0,2), appel principal 25 à 30 ms après : 0 + 0,2 + 0,2 = 0,4 ≤ 0,5, accepté. Annexe réglée en ≈ 2 s (≈ 0,04 USD) : une reprise du kit ou une troisième requête tient encore (0,04 + 0,2 + 0,2 = 0,44). Seules trois requêtes simultanées avant le règlement de l'annexe seraient refusées ; le journal des courses n'en montre que deux par session (juges d'Astra et d'Argon, proposeurs Opus). Un appel principal au-dessus de 0,2 n'est pas refusé (déjà réservé) : il est compté en dépassement ; le plafond n'est franchi au pire que de (coût du principal − 0,2) |
| Coût attendu d'un juge sur 4 fiches | par proportion au journal des courses (proposeur : 5 352 jetons en cache pour ≈ 11 000 caractères ; juge d'Astra : annexe 32 069, principal 31 459 en cache et 9 415 en sortie) : consigne de 24 596 caractères ≈ 10 000 jetons ; annexe ≈ 10 000 × 4 USD/M ≈ 0,04 ; principal ≈ 10 000 × 5 USD/M ≈ 0,05 plus 2 500 à 9 000 jetons de sortie × 20 USD/M ≈ 0,05 à 0,19 ; **total ≈ 0,14 à 0,28 USD**, sous les deux plafonds de 0,5, marge ≈ 2 (constat 6) |
| Coût lu (script l. 128-129) | champs réels de `Resultat` (`cout_declare_usd`, `cout_inconnu` ; `adaptateurs.py` l. 146-164) ; exception ou interruption : 0,5 et inconnu (l. 125-127). Mais voir constat 1 |
| Interruption (l. 122-127) | `except BaseException` autour de `lancer` : `KeyboardInterrupt`, `SystemExit`, `CancelledError` → code 3, `issue.json` écrit ; essai « interruption » passé. Hors de l'appel : constat 3 |
| Rejeu (l. 211-214) | refus si un dossier `runs/epreuve-temoins-seuls-v*` existe (essais : v2 présent → 2 ; seconde passe après un 3 → 2). Limite : constat 4 |
| Codes contre le § 4 | 0 (quatre témoins tenus), 4 (un manqué), 3 (statut non « ok », refus, autre modèle servi, lecture en échec, exception, interruption), 2 (tout refus avant `makedirs`) : conformes ; `--verifier-gabarit` rend 2 sur inégalité, sans appel |
| Témoins v5 | `ecrire_temoins_v5.py` rejoué sur la v1 : sortie identique octet pour octet ; deux faux égaux à ceux de la v1 ; `valider_fiche_ideation` : les quatre passent ; `signaux_niveau_methode(vue_servie(·))` : vide pour les quatre ; `charger_temoins` avec la liste blanche `8bec4254…` : quatre classes, `jumeau_de` = nom du vrai ; longueurs servies 4 768, 3 650, 2 407, 2 606 = addendum l. 50-51 |
| Changements annoncés (différence v4 → v5) | titre neuf sans « contrôle positif » : **fait** ; distinction saboteur / jumeau dérangé : **dans le vrai seulement** (constat 2) ; antériorité (mutation, DeMillo, Lipton et Sayward 1978, SUPPOSÉ ; sabotages plantés ; témoins ajoutés) et part nouvelle ramenée à la règle à trois issues : **fait** dans les deux fiches (le jumeau cite les sabotages plantés dans son texte, pas dans sa liste) ; doses du jumeau « quatre doses non nulles » : **fait** (l. 68, l. 89) |
| Termes absents de la question et des faits | « contrôle positif », « hors ligne », « attach », « fautes plant », « trois issues », « insensib » : 0 ; « mutation » seulement dans « permutation » ; conforme à l. 48-49 |
| § 5 (Carbon) | tableau inchangé et déjà vérifié en v2 ; options (A)/(B), recommandation (B) et défaut (B) de la v2 **retirés** ; la décision écrite (lot à 8 192, courses jumelles, 2 048 retiré de la lignée) concorde avec OD-024 ; § 6 (lanceur v12 par lot) et ordre de la mère cohérents ; aucune recommandation contraire ne reste (le § 7 l. 166, « décision au format », décrit la v2, ce que dit l. 156) |

## § 8 de l'addendum, ligne par ligne

| n° | dit fait | sur pièce |
|---|---|---|
| 1 | réserve 0,2 ; état du relais vérifié avant le dossier | **fait** (commande l. 78, script l. 152-169, l. 215 ; essais l. 89-100) ; la réserve suffit (tableau ci-dessus) |
| 2 | `cout_declare_usd`, `cout_inconnu` | **fait en partie** : les bons champs sont lus, mais l'état du relais **après** l'appel, demandé par le constat 2 de la v2, n'est pas lu, et le cas où le coût se perd n'est pas couvert (constat 1) |
| 3 | refus avant envoi en code 2 | **fait** (clé, modèle, kit, relais, bac à sable avant `makedirs`) |
| 4 | essais avec le type réel ; refus avant envoi essayés | **fait** (`Resultat` réel ; clé, kit absent, relais non conforme ou illisible) ; le chemin du bac à sable n'est pas essayé (les essais passent toujours un adaptateur), vérifié à la main ; l'essai du coût en erreur masque le constat 1 |
| 5 | paire v5 ; échec probable dit d'avance | titre, antériorité, doses : **faits** ; distinction : **vrai seulement** (constat 2) ; l'échec probable est écrit honnêtement (l. 54-58), à compléter par le constat 2 |
| 6 | interruption attrapée, code 3 | **fait** pour l'appel ; « tout autre code vaut 3 » non écrit au § 4 (constat 3) |
| 7 | « taille réelle » précisé ; OD-024 | **fait** (l. 138-139 ; OD-024 au journal) |
| 8-15 | mineurs | doses (9), GO-16 (11), réponse caviardée et clé après l'appel (13), `texte_final` (14), décision (15) : **faits**. Mais le constat 8 (zone 0,05 à 0,15 non classée) n'est ni nommé ni traité ; le constat 12 (prix du lot) est nommé, **pas corrigé** (l. 121 inchangée) ; le constat 10 (rejeu depuis une autre copie) reçoit « refus toutes versions », qui répond à autre chose (constat 5) |

## Constats

### Bloquant

Aucun.

### Significatifs

1. **Le coût d'un appel en échec se perd, et l'essai le masque** (script l. 128-129, l. 225-231 ; `pole/adaptateurs.py`
   l. 481, l. 538-551 ; essais l. 45, l. 85). Sur délai de session dépassé (`asyncio.TimeoutError`) ou erreur du kit
   (`ClaudeSDKError`), l'adaptateur réel rend `statut` « erreur », `cout_declare_usd` = 0,0 et `cout_inconnu` = **faux** : seul
   un refus marque le coût inconnu ; la course, elle, lit l'écart au relais. Le script écrit `etat-relais-avant.json` mais ne
   relit pas le relais après l'appel : dans les échecs les plus probables d'un code 3, `issue.json` portera
   `"cout_usd": 0.0`, `"cout_inconnu": false`, alors que l'appel principal a pu être facturé, et la règle 4.2 fonde l'addendum
   suivant sur le coût de `issue.json`. L'essai « erreur » rend 0,137 USD et affirme « le champ réel du résultat, jamais
   nul » : faux pour l'adaptateur réel. Le journal du relais (`--journal`, l. 78) garde le vrai montant : rien n'est perdu
   pour les registres, mais la pièce désignée ment. **À faire**, au choix : (a) sans toucher au script, écrire au § 3 et au
   § 4.2 que le coût de l'épreuve est l'écart lu au relais (`/relais/etat` après l'appel, ou son journal) et que
   `issue.json` peut porter 0,0 en code 3 ; (b) script v4 : relire `/relais/etat` après `juger` (dans un `try`), écrire
   `etat-relais-apres.json` et `cout_usd = max(cout_declare_usd, écart de dépense)`, essai couvrant « erreur à coût 0 ».
   (a) suffit pour autoriser.

2. **La distinction saboteur / jumeau dérangé manque au jumeau, qui doit franchir la porte seul**
   (`temoins-organisme-discrets-v5.json` l. 11 contre l. 66 ; `ecrire_temoins_v5.py` l. 18-20 ; addendum l. 36-37 et
   l. 188 ; `pole/ideation_v2.py` l. 949-957). Le constat 5 de la v2 demandait de « dire, dans les deux fiches, ce qui
   distingue le saboteur d'un jumeau dérangé » ; la phrase n'est ajoutée qu'à l'énoncé du vrai, et l'addendum dit « écrit
   dans la fiche ». Or `lecture_temoins` exige pour le jumeau, comme pour le vrai, `max(avantage, originalité) ≥ 2`, plus le
   signalement en doublon. Un juge qui lit les faits l. 8 (« p = 0 correspondant au jumeau honnête », « dérangement uniforme
   tiré par graine », « mêmes graines d'action ») peut prendre le jumeau dérangé de la question pour le Bras A lui-même à une
   autre graine et lui refuser l'originalité : le jumeau est désormais le plus exposé des deux, ce que l'aveu d'échec
   probable (l. 54-58), écrit pour la paire, ne dit pas. **À faire**, au choix : ajouter la même phrase à l'énoncé du jumeau
   (témoins v6 générés par un `ecrire_temoins_v6.py`, consigne et empreinte réépinglées, script v4 qui ne change que ces
   constantes, essais rejoués ; aucune dépense) — **recommandé**, une phrase de plus avant de payer l'épreuve ; ou écrire au
   § 2 que la distinction n'est que dans le vrai et que le jumeau porte le risque le plus haut, et corriger la ligne 5 du
   § 8.

### Mineurs

3. Interruption hors de l'appel (script l. 135-140, l. 222-231) : une interruption pendant la lecture de la réponse
   (`except Exception`) ou l'écriture des pièces, et tout arrêt par signal non intercepté (`SIGTERM`, `SIGKILL`), laissent le
   dossier sans `issue.json`, avec un code hors de 0, 2, 3, 4. Le rejeu reste refusé (le dossier existe) ; ajouter au § 4,
   comme le demandait le constat 6 de la v2 : « tout autre code, ou un dossier sans `issue.json`, vaut 3 ».
4. Rejeu « toutes versions » : vrai **du script v3 seulement**. Le script v2 (`scripts/epreuve_temoins_seuls_v2.py`
   l. 165-166) ne refuse que son propre dossier et ne lit pas le relais ; le v1 prend son dossier en argument (l. 99). Après
   une tentative v3, l'un ou l'autre reste lançable. Barrière de règle : écrire au § 3 que les scripts v1 et v2 sont retirés
   et ne se lancent plus. Le rejeu depuis une autre copie du dépôt (constat 10 de la v2) reste, lui aussi, une règle ; le
   contrôle `appels` = 0 l'atténue sans l'empêcher (un relais neuf se relance).
5. § 8, ligne « 8-15 » (l. 190) : la parenthèse nomme huit mineurs, mais le constat 8 de la v2 (zone de 0,05 à 0,15 point
   non classée ; v5 l. 14 et l. 69 inchangées) n'y figure pas, et le constat 12 (prix du lot) y figure sans correction :
   l. 121 dit toujours « 0,004 au prix public (2 / 10) » pour un prix de lot (moitié du public). Corriger l. 121 et la ligne
   du § 8, ou dire « non traité ».
6. Coût attendu (l. 86) : « ≈ 0,1 à 0,2 USD » est un peu bas en haut de fourchette ; mon estimation est ≈ 0,14 à 0,28 USD
   (tableau ci-dessus). Les deux plafonds de 0,5 tiennent avec une marge d'environ deux. Si le kit compte la session
   au-dessus de 0,5 (plafond de session ; 2,0 pour le juge en course), il rend `error_max_budget_usd`, statut
   « budget_depasse », code 3 : improbable, à écrire avec le chiffre corrigé.
7. Distinction du vrai (v5 l. 11) : « le saboteur génère son propre texte » s'appuie sur une lecture des faits (l. 8 : « agent
   saboteur », budget de jetons apparié ; l. 21 : écart de coût d'exécution entre saboteur et jumeau, qui suppose deux
   générations), plausible mais non écrite telle quelle ; les faits l. 8 se lisent aussi comme un dérangement mécanique dont
   la dose 0 est le jumeau. Pas faux ; un « au vu des faits l. 8 et l. 21 » dans la phrase la rendrait opposable. La
   `perte_traduction` du vrai garde « Le contrôle positif » (générateur l. 29) ; sans effet, le titre ne s'y appuie plus.
8. Le chemin `adaptateur_reel` (bac à sable inactif ou sans `/proc` neuf → code 2) n'est couvert par aucun essai (tous
   passent un adaptateur) ; vérifié à la lecture : il est dans le `try` qui rend 2, avant `makedirs`.
9. Décision de la mère (§ 5, l. 127-130) : R-3241 n'est pas dans `registres/decisions.md` de ce dépôt ; la seule pièce est le
   résumé d'OD-024, qui concorde. La clause « ne peut revenir que comme bras déclaré « Carbon sans pensée », hors lignée, sur
   un mot de Lazar » n'est vérifiable sur aucune pièce ; donner l'empreinte ou la ligne de la source quand elle existe.

## Ce qui tient

- Le bloquant de la v2 est levé : réserve 0,2 sous plafond 0,5, deux requêtes simultanées admises, état du relais neuf
  exigé avant tout, en code 2 ; les autres refus de l'adaptateur sans envoi sont tous rapatriés avant le dossier, et rien
  après `makedirs` ne peut lever avant envoi (options bâties à vide dans l'environnement exact).
- Le juge est appelé comme en course (rôle, consigne système, effort, aucun outil, tours, bac à sable, kit 0.2.172) ; la
  consigne est épinglée et son gabarit égal aux deux courses ; la réponse écrite est caviardée, la clé écrite après l'appel.
- Les témoins v5 sont générés par programme, reproductibles, valides pour l'orchestrateur épinglé ; les faux sont ceux de la
  v1 ; les corrections de titre, d'antériorité et de doses sont faites ; l'addendum dit franchement que l'échec est probable
  et ce qu'il coûte.
- Le § 5 reprend la décision de la mère sans recommandation contraire restante.

## Pour que l'addendum soit autorisable

Coût de l'épreuve défini comme l'écart lu au relais, `issue.json` non opposable pour le coût en code 3 (1, option (a) :
texte seul) ; distinction ajoutée au jumeau (témoins v6, script v4 à constantes réépinglées), ou risque du jumeau écrit et
§ 8 ligne 5 corrigé (2). Les mineurs 3 à 6 se corrigent dans le même passage, en texte. Si l'option (a) et l'aveu écrit
sont retenus, aucune pièce scellée ne change et une relecture de ces seuls paragraphes suffit ; si des témoins v6 et un
script v4 sont écrits, contre-lecture courte du script, de ses essais et de la différence v5 → v6.
