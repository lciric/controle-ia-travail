# Contre-lecture (R2) — « Le pari apparié borné — conception v7 » (Opus 5.5) et le code v7, version 24 (`pari_apparie`, `monde_banque_scores`, `engagement_apparie`) — rapport v1

Contre-lecteur : sous-agent neuf **Fable 5.1**, autre modèle que l'auteur ; je n'ai écrit ni la v7, ni le code, ni une
contre-lecture antérieure. Début : mardi 27 octobre 2026, **21:37:13 UTC** (`date -u`, appel séparé). Aucun fichier du dépôt
modifié (module importé sans écriture de bytecode ; le dossier `pole/__pycache__` existant date de 15:05 UTC, avant ma
session) ; tout ce que j'ai écrit est dans
`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe-v7/`. Aucune clé ni
aucun jeton lu, affiché ou cherché ; aucune dépense (processeur seul, 8 secondes). Toutes les empreintes vérifiées
(`sha256sum -c`) avant lecture (section 8) ; le code conforme à `EMPREINTES-orchestrateur-pole-v7-v24.txt` (126 lignes
« OK », aucune autre). Les heures de modification « en avance d'une heure » sont bien l'affichage `TZ=Europe/Paris`
(la v7 est datée 22:36 par `ls`, `date -u` disait 21:37 à mon début) : K6-12 fermé sur ce point.

## Verdict

1. **La v7 ferme K6-1, K6-3, K6-5 à K6-12 ; K6-2 n'est fermé qu'à moitié.** Le contrat d'abandon ferme le chemin
   « abandonner avant d'ajouter » (refus, drapeau explicite), mais son jumeau reste ouvert **sans erreur ni mensonge** : une
   partie calculée et **jamais ajoutée** est invisible au code (« une partie par génération » est tenu comme « au plus
   une »). Reproduit avec la `Course` v24 : une politique « j'ajoute la partie si elle monte, je la saute sinon » donne
   **0,379** de fausse promotion sur 10 générations et **0,982** sur 30 (nul complet, monde A′, α = 0,05), contre 0,034
   quand toutes les parties sont ajoutées (K7-1). Le code ne peut pas le voir ; il peut le rendre bruyant (`lire()` exigeant
   une partie ou une déclaration par fiche active) ; l'orchestrateur doit garantir « toute partie calculée est ajoutée ».
2. **Le retrait (D-S26 bis (5)) est valide** : l'exclusion ne fait que réduire les promotions (0 violation sur 3 000
   tirages), l'union d'avant les retraits reste garantie (0,0045 pour une borne 0,025 avec retraits aléatoires), les
   rapportées en sortent. Le partage de α_g entre familles n'est tenu par le code qu'au total Σ α_c ≤ α — ce que la preuve
   exige ; la répartition par génération est à l'orchestrateur (à dire). **`monde_banque_scores` tient son seuil
   conforme strict** (taux d'alerte des neufs ≈ j/(n+1) ≤ τ, moins avec des ex æquo), aucune fuite de l'épreuve vers les
   seuils. **`engagement_apparie`** : seuils du seul calibrage ; le scellement **détecte** une altération mais ne
   l'**empêche** pas (une altération re-scellée passe `evaluer` : l'empreinte doit être consignée hors de l'engagement avant
   l'épreuve) ; la clé porte tous les champs de D-S18, mais **ni la partie lue** (développement et épreuve ont la même clé)
   **ni l'identité des unités** : le même engagement évalué deux fois sur la même banque donne la même trajectoire et la
   `Course` l'accepte comme deux parties (K7-2, K7-3).
3. **Tous les chiffres de la v7 sont justes contre leurs fichiers** (section 6) ; 259 essais, 1,77 (exact 1,7666), 25 et
   0,04, 11 sur 400, `34cf6eb0…` versée. **À amender en v8 par des corrections locales** (K7-1 à K7-5), pas refaire.

---

## 1. Réponses aux questions

### Q1 — La v7 ferme-t-elle K6-1 à K6-12 ? (le rapport v6 n'a pas de K6-4)

| constat v6 | état | raison |
|---|---|---|
| K6-1 budget de la relecture, union garantie, exclusion | **fermé** | D-S26 bis (3) et (5) : famille de g′, témoin compté dans m_{g′}, union d'avant les retraits, retirées exclues ; codé (`retirer`, `exclues`, `promues_rapportees`) et testé (`test_retrait`) ; vérifié (section C) |
| K6-2 partie jetée en silence | **à moitié** | le chemin « abandonner puis ajouter » est fermé (refus, ou partie passée, ou drapeau) ; mais la partie **jamais ajoutée** reste invisible, sans erreur (K7-1) ; `abandonner(gelée, trajectoire)` ignore encore une partie en silence (K7-5) ; aucune trace de l'abandon |
| K6-3 dépendance entre générations | **fermé** | D-S25 bis (5) : e-valeur conditionnelle au passé de toute la course, unités fraîches, mise prévisible, parties disjointes — mais rien ne vérifie « unités fraîches » (K7-2) |
| K6-5 `ebh_pondere` et α | **fermé** | `alpha=` donné par `lire` ; refus au-dessus de α (vérifié : somme 0,5 refusée avec α = 0,05, acceptée sans) |
| K6-6 essai A′ sans promotion ; cas limites | **fermé** | `fausses_valides ≥ 3` (faible mais suffisant : attendu 11) ; ex æquo à 1/3, abandonnée promue par k*, somme entre α et 1 : testés |
| K6-7 k témoin compris | **fermé** | « au plus α/m » ; « k total, témoin compris » ; 25 et 0,04 justes |
| K6-8 estimande de D-S27 | **fermé** | même signe, échelle déclarée, « jamais un gain de rappel par épisode » |
| K6-9 D-S29 (d), D-S10/D-S29, brief du mode tenu à l'écart | **fermé** | (d) comme nœud (modification de N-054 point 4, dit) ; objets distincts ; contrainte sur le brief, ligne de devis |
| K6-10 reprise de course, reliquat | **fermé** | D-S24 : G_max jamais relevé, reprise = créneaux restants, reliquat perdu « par choix » |
| K6-11 une lecture par génération ; nature de e-BH | **fermé** | « la lecture ferme la génération », tenu par le code (`generation += 1` dans `lire`) ; promotion à E = 1 dite |
| K6-12 sortie non versée, horodatages | **fermé** | `34cf6eb0…` présente et conforme à son compagnon ; explication `TZ` juste |

### Q2 — Le contrat d'abandon

**Ce qu'il ferme.** `ajouter_trajectoire` refuse une gelée (vérifié) et une seconde partie dans la génération ; `abandonner`
sans partie de la génération courante refuse, sauf `avant_partie=True` ou partie passée ; passer la partie l'ajoute puis
gèle. L'artefact exact de K6-2 (« abandonner puis ajouter ») est fermé : l'ajout lève une erreur.

**Ce qu'il n'empêche pas (reproduit, sections A et B).**
- `avant_partie=True` à tort : indétectable par construction, et **sans trace** (`gelees` est un ensemble ; ni génération,
  ni mode, ni motif d'abandon ne sont gardés) — invérifiable après coup.
- Ordre `lire` / `abandonner` : la partie de g **calculée mais jamais ajoutée**, puis `lire()` (g → g+1), puis
  `abandonner(f, avant_partie=True)` est accepté **sans erreur**, et le drapeau est même véridique pour g+1 (A (3)).
- Plus simple encore, sans abandon : sauter les parties défavorables et ajouter les favorables. `lire()` n'exige aucune
  partie (A (4)). Mesure B : P(au moins une fausse promotion) **0,379** (10 générations), **0,982** (30), E[e-valeur]
  15,8 et 59,7 au lieu de ≤ 1 ; contrôle sain 0,034.
- `abandonner(f, trajectoire_log=…)` sur une fiche **déjà gelée** rend sans rien faire **avant** d'appeler
  `ajouter_trajectoire` : la partie est ignorée en silence (A (1)), contrairement à § 3 (« plus jamais ignorée en
  silence »). Sans biais (gel antérieur), mais contraire à R5.

**Ce que le code peut garantir** : une partie ajoutée n'est jamais jetée ; au plus une partie par génération ; un abandon
sans partie est déclaré. **Ce qu'il ne peut pas garantir** : qu'une partie calculée a été ajoutée, ni que la décision n'a
rien vu. **Ce que l'orchestrateur doit garantir** (à écrire dans D-S25 bis (2)) : toute partie calculée par le monde est
ajoutée à la course **avant** que quiconque la lise ; les décisions d'abandon « avant partie » sont prises dans une phase
où aucune issue de la génération n'est calculée. **Ce que le code peut rendre bruyant** : `lire()` refusant tant qu'une
fiche active (ni gelée, ni arrêtée, ni promue) n'a ni partie ni déclaration `sans_partie[fiche] = motif` ; une trace
`abandons[fiche] = (génération, mode, motif)`.

### Q3 — Le retrait et le partage de α_g

**Valide.** (i) Exclure une fiche de la lecture ne fait que réduire l'ensemble promu : si la retirée est dans les k*
premières, k*′ ≤ k*−1 (sinon s′_(k*) = s_(k*+1) ≥ 1/k* contredirait la maximalité) ; sinon le haut du tri est inchangé ;
dans les deux cas promues(sous-ensemble) ⊆ promues(ensemble) — 0 violation sur 3 000 tirages aléatoires (C (1)).
(ii) La preuve (1/|R_∪| ≤ 1/k_τ ≤ b_i·E_i(τ_i)) ne demande que « toutes les promotions de la lecture τ sont dans R_∪ »,
vrai puisque `promues` ne décroît jamais, retirées comprises : l'union d'avant les retraits est garantie ; reproduit sous
nuls partiels avec retraits aléatoires (30 % des promues) : 0,0045 pour une borne 0,025 (C (4)). (iii) L'ensemble rapporté
n'est pas couvert (retirer une vraie promue fait monter la proportion de fausses) : la v7 le dit, juste ; « la probabilité
d'au moins une fausse promotion ne peut que baisser » : juste. (iv) `bonferroni()` exclut les retirées : cohérent.
Détails : un second `retirer` écrase le motif (trace perdue, C (3)) ; `abandonner` après `retirer` est silencieux (sans
effet, acceptable).

**Partage de α_g.** Le code tient **Σ_c α_c ≤ α** sur toute la course (`alpha_engage`, jamais rendu) — c'est l'hypothèse
de la preuve. Il ne connaît pas α_g : deux familles entrées à la même génération avec 0,02 chacune sous α/10 = 0,005
passent (C (2)) ; la suite de dépense D-S24 est à l'orchestrateur. La garantie tient quand même (Σ ≤ α) ; ce qui glisse est
le plan de dépense (les générations suivantes seront refusées). À dire dans D-S25 bis (1) : « tenu par le code au total,
par l'orchestrateur par génération ».

### Q4 — `monde_banque_scores`

- **Seuil conforme strict** : j = ⌊τ(n+1)⌋, seuil = j-ième plus grand honnête du calibrage, alerte si score **>** seuil.
  Pour des scores échangeables continus, P(neuf > s_(j)) = j/(n+1) ≤ τ ; reproduit (D (1)) : 0,0103 et 0,0101 (τ = 0,01),
  0,0501 et 0,048 (τ = 0,05), 0,128 pour j/(n+1) = 0,125 (τ = 0,2, n = 7) ; avec des ex æquo lourds, bien moins (0 à
  0,05) : la convention « > » est conservatrice, la masse d'ex æquo est rapportée (0,5 sur l'exemple). Bord j entier :
  τ = 0,05, n = 19 → j = 1 ; τ = 0,1, n = 9 → j = 1 (le 1e-12 fait son office). **Tient ce qu'il dit.** Réserve (K7-8) :
  l'échangeabilité est au niveau de l'**épisode**, alors que les honnêtes du calibrage vont par unité (plusieurs exécutions
  d'une consigne) ; un honnête d'une unité neuve n'est pas échangeable avec eux en général (corrélation intra-unité) — la
  condition est bien écrite dans la docstring, mais la banque réelle ne la donne pas d'elle-même ; τ est un point de
  fonctionnement, la garantie des e-valeurs n'en dépend pas.
- **Parts** : r_c et f_c par unité avec la même convention « > » ; unités sans sabotés hors des contrastes, sans honnêtes
  hors de la garde : justes.
- **Ordre secret** : déterministe, indépendant de l'ordre d'entrée, change avec la graine, l'étiquette (ici l'empreinte de
  l'engagement) et la banque (D (4)). Réserve (K7-7) : il dérive de `self.empreinte`, empreinte de **toute** la banque,
  scores d'épreuve compris ; formellement l'ordre est une fonction (pseudo-aléatoire) des données qu'il ordonne. Pas
  exploitable sans inverser SHA-256, mais dériver de la graine, des identifiants et de l'empreinte du calibrage serait
  propre. Même chose pour la partition du jumeau (D (3) : « jumeau_identique » faux quand l'épreuve change — la partition
  bouge, pas les scores).
- **Jumeau calibré** : moitiés disjointes par unité, couvrant tout le calibrage (D (5)) : juste.
- **Fuite de l'épreuve vers les seuils** : impossible par le code (`seuil` ne lit que `partie == "calibrage"`, une unité ne
  chevauche jamais deux parties ; seuils identiques quand l'épreuve et le développement sont déplacés de ±100, D (3)). La
  seule fuite possible est en amont : l'étiquette `partie` est une donnée de la banque.

### Q5 — `engagement_apparie`

- **Seuils du seul calibrage** : oui, strate comprise (`seuil(c, tau, strate)` sur le calibrage de la strate ; E (4) :
  1,723 contre 1,654 global, égal au calcul direct).
- **Scellement** : `empreinte = empreinte_objet(engagement sans empreinte)` ; `evaluer` recalcule. Cela **détecte** une
  altération accidentelle, pas une altération volontaire : altérer un seuil puis recalculer `empreinte_cle` et `empreinte`
  passe `evaluer` (E (1)). « Scellée avant toute issue » n'est vrai que si l'empreinte est consignée **ailleurs** (journal,
  mémoire) avant l'épreuve ; le code ne le fait pas et la v7 § 4 dit que le lien au cycle manque — à dire explicitement
  (K7-4). Remarque : l'ordre secret dépend de l'empreinte de l'engagement, donc un engagement re-scellé lit dans un autre
  ordre (bien) — mais aussi, par `monde.empreinte`, des scores d'épreuve (K7-7).
- **Clé de l'héritage** (v6 § 3.6) : contrastes et coefficients ✓ ; pondération et m_max ✓ ; τ ✓ (un seul τ, pas
  « l'ensemble de τ déclaré ») ; strate ✓ ; comparateurs ✓ (= noms des contrastes, redondant avec `contrastes`) ; seuils
  scellés ✓ ; population ✓ (empreinte de la banque ou vivier déclaré) ; garde ✓ (en plus). Le budget est hors clé, dans
  l'engagement : juste (même affirmation, autre budget).
- **Ce qui manque pour un héritage valide** : (a) **la partie lue** — `partie` est dans l'engagement, pas dans la clé :
  développement et épreuve ont la **même** `empreinte_cle` (E (2)) ; un orchestrateur qui hérite par clé fusionnerait une
  lecture de développement et une d'épreuve (K7-3) ; (b) **l'identité des unités** — `evaluer` ne rend qu'un nombre
  (`unites_lues`) ; le même engagement sur la même banque donne la même trajectoire, et la `Course` l'accepte à la
  génération suivante comme une partie neuve (E (3)) : la condition « unités fraîches » de D-S25 bis (5) n'est vérifiable
  nulle part (K7-2) ; (c) la grille Λ (constante de module) n'est pas dans la clé : changer Λ entre versions changerait
  l'e-processus sous la même clé (mineur).

### Q6 — Les essais testent-ils ce qu'ils disent ?

Les 33 essais des trois fichiers passent (0 échec, 0 erreur) ; 259 `def test_` dans `essais/` au total (le « 259 »).
- `test_contrat_d_abandon` : cas sain, artefact refusé, partie passée, drapeau, gelée refusée, une partie par génération :
  teste ce qu'il dit. **Il ne teste pas** la partie jamais ajoutée (K7-1) ni `abandonner(gelée, trajectoire)` (K7-5), qui
  passerait pour une mauvaise raison si on l'ajoutait avec `assertRaises` : il ne lève rien.
- `test_retrait` : union, rapportées, exclusion qui empêche une promotion (k* = 2 au lieu de 4 — en fait k* = 3 si « a »
  comptait : 0,26 ≥ 1/4 demande k = 4, donc « d » n'est promue ni à 3 ni à 2 ; la **phrase** du commentaire est
  approximative, l'essai juste : sans « a », les scores sont b 1, c 0,3, d 0,26 → k* = 2 ; avec « a » : 1, 1, 0,3, 0,26 →
  k* = 4, « d » promue). Teste ce qu'il dit.
- `test_budgets_au_dessus_de_alpha`, `test_ex_aequo_au_bord_et_abandonnee_promue_plus_tard` : justes.
- `test_nul_complet_lecture_valide_contre_lecture_seule` : `fausses_valides ≥ 3` ferme K6-6 (une lecture muette échoue).
- `test_faux_positifs_neufs_au_plus_tau` : moyenne sur 30 calibrages ≤ 0,055, scores gaussiens indépendants — teste
  l'échangeabilité idéale, pas la structure par unité (K7-8).
- `test_scellement` : altération **sans** re-scellement, et autre banque : juste, mais ne dit pas que le re-scellement passe.
- `test_cle_de_l_heritage` : variantes de τ, m_max, strate, population, garde → clés distinctes ; **ne teste pas** `partie`
  (qui donnerait une clé identique : K7-3).
- `test_bout_en_bout` : vrai effet promu, nul « rappel ≥ 0,9 » non promu, 100 unités lues : juste ; dans la banque
  synthétique chaque unité d'épreuve a 10 sabotés et 10 honnêtes, donc contrastes et garde sont alignés par construction —
  l'essai ne couvre pas le désalignement (K7-6).

### Q7 — Chiffres : section 6. Tous justes.

### Q8 — Ce qui tient : section 5.

## 2. Constats, du plus grave au moins grave

### Touche la garantie

**K7-1 — Une partie calculée mais jamais ajoutée est invisible : le jumeau de K6-2 reste ouvert sans erreur.**
- **Où.** `Course.lire` (aucune exigence de partie par fiche active) ; `Course.ajouter_trajectoire` (« une seule partie par
  génération » = au plus une) ; v7 D-S25 bis (2) « une partie par fiche et par génération », lu « exactement une » par le
  texte, « au plus une » par le code ; `abandonner(f, avant_partie=True)` véridique après `lire()`.
- **Ce qui manque.** Mesuré (section B, `Course` v24 telle quelle) : politique « ajouter si la partie monte, sauter
  sinon », nul complet, A′ 20 pas, 4 fiches, α = 0,05 : **0,379** d'au moins une fausse promotion sur 10 générations,
  **0,982** sur 30 ; E[e-valeur finale] 15,8 et 59,7 ; 0,034 quand tout est ajouté. Aucune erreur levée. Le code ne peut pas
  distinguer « pas de partie » de « partie retenue ».
- **Correction.** Texte : « toute partie calculée par le monde est ajoutée avant toute lecture ou décision ; une fiche
  active sans partie dans une génération est déclarée avec son motif ». Code : `lire(sans_partie=None)` refusant tant
  qu'une fiche ni gelée, ni arrêtée, ni promue n'a ni partie ni déclaration ; trace `sans_partie` ; essai cas sain et
  artefact (R5). Mieux : le monde remet la partie à la course, pas au décideur (observation = ajout).

**K7-2 — L'identité des unités lues n'est ni rendue ni vérifiée : la même partie peut compter deux fois.**
- **Où.** `engagement_apparie.evaluer` (rend `unites_lues`, un nombre) ; `Course.ajouter_trajectoire` (sans empreinte
  d'unités) ; D-S25 bis (5) « unités fraîches ».
- **Ce qui manque.** Le même engagement évalué deux fois sur la même banque : trajectoires identiques, acceptées à deux
  générations (E (3)) — l'e-valeur est élevée au carré. Rien ne le refuse, rien ne le journalise.
- **Correction.** `evaluer` rend `empreinte_unites` (identifiants triés + empreinte de la banque + partie) ;
  `ajouter_trajectoire(fiche, traj, empreinte_unites)` refuse une répétition pour la fiche (et, par la mémoire, pour la
  lignée de la clé) ; essai.

**K7-3 — La partie lue n'est pas dans la clé de l'héritage.**
- **Où.** `construire` : `cle` sans `partie` ; développement et épreuve → même `empreinte_cle` (E (2)).
- **Ce qui manque.** Un héritage par clé peut multiplier une partie de développement à une d'épreuve. Λ absente aussi.
- **Correction.** `partie` (et `lambdas`) dans la clé, ou dire « l'héritage n'est permis qu'entre épreuves » et le vérifier ;
  essai « partie différente → clé différente ».

### Garantie, mais déjà dite ouverte par la v7 (lien au cycle)

**K7-4 — Le scellement détecte, n'empêche pas.** `evaluer` accepte un engagement altéré puis re-scellé (E (1)). « Scellée
avant toute issue » exige l'empreinte consignée hors de l'objet avant l'épreuve (journal, mémoire) : à écrire comme
obligation de l'orchestrateur ; le code ne peut rien de plus.

### Contrat (R5) et trace

**K7-5 — `abandonner(gelée, trajectoire_log)` ignore la partie en silence ; aucun abandon n'est tracé.** Le `return` sur
`gelees` précède l'ajout (A (1)) ; contraire à § 3 « plus jamais ignorée en silence ». Sans biais (gel antérieur). Et
`gelees` est un ensemble : ni génération, ni mode (`avant_partie`), ni motif ; `avant_partie` à tort est invérifiable
après coup. Correction : lever (ou au moins consigner) ; `abandons[fiche] = (génération, mode, motif)` ; `retirer` deux
fois écrase le motif (garder une liste).

### Réserves théoriques (monde et engagement)

**K7-6 — Garde et contrastes alignés par indice, non par position dans l'ordre secret.** `pa.evaluer` prend le minimum
à l'indice t des trajectoires (t-ième unité sabotée, t-ième unité honnête). Quand les ensembles d'unités diffèrent (E (5) :
30 unités sabotées, 20 honnêtes, 2 coïncidences d'indice), les processus vivent dans des filtrations différentes : le
niveau de fausse promotion reste protégé (Ville sur chaque composante, pour tout t), mais E[e-valeur au franchissement
joint] ≤ 1 n'est plus donné par l'arrêt optionnel (borne grossière : facteur ≤ 1,9 sur la part franchie). Exact quand
chaque unité porte les deux étiquettes (banque synthétique). Correction : une seule suite d'unités dans l'ordre secret,
chaque processus mis à jour quand son unité arrive, minimum après chaque unité ; ou déclarer la condition.

**K7-7 — Ordre secret et partition du jumeau dérivés de l'empreinte de toute la banque, épreuve comprise** (D (3), (4)) ;
l'engagement porte aussi `monde.empreinte`. Formellement une fonction des données ordonnées ; dériver de la graine, des
identifiants et de l'empreinte du calibrage.

**K7-8 — La garantie conforme est au niveau de l'épisode, la banque va par unité** : échangeabilité à déclarer par unité
(seuil sur des unités, ou un score par unité) ou τ dit « nominal ». Sans effet sur la garantie des e-valeurs.

### Clarté

**K7-9 — Partage de α_g** : tenu par le code au total seulement (C (2)) ; à dire (D-S25 bis (1), docstring de `entrer`).

**K7-10 — En-tête du module** : `pari_apparie.py` ligne 1 dit « version 20 », la v7 dit version 24 (les docstrings
internes disent 21 et 24) ; `test_retrait`, commentaire « promue à k = 4 si « a » comptait, pas à k = 3 » : juste pour
k = 4, mais c'est k* = 2 sans « a » (0,3 ≥ 1/2, 0,26 < 1/3).

## 3. Décisions de la v7 : avis

| décision | avis |
|---|---|
| D-S24 (0,75) | juste et complète (reprise, reliquat par choix) |
| D-S25 bis (0,85) | juste ; 0,85 tenable si « toute partie calculée est ajoutée » et la trace de l'abandon sont écrits (K7-1, K7-5) ; sinon 0,75 |
| D-S26 bis (0,7) | juste et codée ; retrait valide ; témoin dans m_{g′} juste ; non simulée (dit) |
| D-S27 (0,8) | juste ; échelle déclarée |
| D-S29 (0,55) | (d) bien posée comme nœud ; recommandation (a) cohérente |
| D-S30 (0,6) | (a) fidèle ; contrainte sur le brief juste |

## 4. Mathématiques en une page

- Exclusion : s′_(j) ≤ s_(j) pour tout rang j après retrait d'un élément ⇒ k*′ ≤ k* ; si le retiré est dans les k*
  premiers, k*′ ≤ k*−1 ⇒ promues(sous-ensemble) ⊆ promues(ensemble).
- Union d'avant les retraits : 1/|R_∪| ≤ 1/k_τ ≤ b_i·E_i(τ_i) demande seulement que les k_τ promues de τ soient dans R_∪ ;
  `promues` ne décroît jamais. L'ensemble rapporté : retirer une vraie fait monter la proportion de fausses.
- Partie sautée : E[E(g−1)·max(1, e_g)] = E(g−1)·1,7666 en A′ à 20 pas (exact, binomial) ; itéré, ×1,77 par génération.
- Désalignement (K7-6) : {∃t : min_t ≥ s} ⊆ {∃t : X_t ≥ s}, Ville ⇒ niveau tenu ; la valeur au franchissement ∈ [s ; 1,9 s]
  ⇒ E[E_T ; T < ∞] ≤ 1,9, non ≤ 1 sans filtration commune.
- Conforme strict : P(neuf > s_(j)) = j/(n+1) pour des échangeables continus, ≤ j/(n+1) avec ex æquo.

## 5. Ce qui tient (une ligne chacun)

- K6-1 fermé : relecture et témoin dans la famille de g′ ; union d'avant les retraits ; exclusion codée et valide.
- K6-3, K6-7, K6-8, K6-10, K6-11, K6-12 fermés par le texte, sans contradiction avec le code.
- K6-5 fermé : `ebh_pondere(..., alpha=)` refuse au-dessus de α ; `lire` le passe.
- K6-6 fermé : l'essai A′ exige des promotions ; ex æquo, abandonnée promue, somme entre α et 1 testés.
- K6-9 fermé : (d) comme nœud ; D-S10 / D-S29 distingués ; brief du mode tenu à l'écart.
- `ebh_pondere` : tri, k* maximal, ex æquo au bord, domaine logarithmique — inchangés et justes.
- `Course.entrer` : Σ α_c ≤ α tenu ; budgets jamais rendus ; double entrée refusée.
- `ajouter_trajectoire` : gelée refusée ; une partie par génération ; arrêt gelé au franchissement.
- `abandonner` : refus sans partie ni déclaration ; partie passée ajoutée puis gelée.
- `lire` : pool sans les exclues ; promues ne décroît jamais ; ferme la génération.
- `retirer`, `promues_rapportees`, `bonferroni` : cohérents ; FDR de l'union 0,0045 ≤ 0,025 avec retraits.
- Seuil conforme strict : j/(n+1) ≤ τ reproduit ; ex æquo conservateurs et rapportés ; calibrage insuffisant signalé.
- Aucune fuite de l'épreuve vers les seuils par le code ; jumeau disjoint et couvrant.
- Engagement : seuils du seul calibrage, strate comprise ; clé avec tous les champs de D-S18 et la garde ; altération
  non re-scellée et autre banque refusées.
- 33 essais des trois fichiers passent ; 259 `def test_` dans `essais/`.

## 6. Chiffres : chaque chiffre de la v7 contre son fichier

| où (v7) | cité | fichier, valeur | verdict |
|---|---|---|---|
| en-tête | v6 `f21982cd…` ; rapport v6 `490100af…` ; script `82edb8fb…` ; sortie `7a6cd572…` | empreintes vérifiées (section 8) | justes |
| en-tête | verdict v6 : « opératoire et valide » ; K6-1 et K6-2 hors D-S25 bis ; deux lectures trompeuses ; une option ; un essai ; « corrections locales, pas refaire » | rapport v6, verdict 1 à 3 | juste |
| D-S25 bis (2) | E(g−1)·max(1, e_g) ; **1,77** par partie jetée, A′ 20 pas, § 4 | rapport v6 § 4 et sortie v6 ; recalcul exact 1,7666 (section B) | juste |
| D-S26 bis, K6-7 | k = 4 pour 3 vraies : seuil 5/(0,05·4) = **25**, borne **0,04** | calcul : 25,0 ; 0,04 | justes |
| § 3 | version 24 ; `ebh_pondere(..., alpha=)` ; `abandonner(fiche, trajectoire_log=None, avant_partie=False)` ; `retirer(fiche, motif)` | `pari_apparie.py` l. 188, 282, 304 (en-tête du module : « version 20 », K7-10) | justes |
| § 3 | quatre essais de plus ; A′ affirme des promotions, attendu ≈ 11 sur 400 | `CorrectionsV7` : 4 essais ; `assertGreaterEqual(fausses_valides, 3)` ; 0,0275·400 = 11 (sortie v5 H) | justes |
| § 3 | **259 essais passent** | 259 `def test_` dans `essais/` ; les 33 des trois fichiers lancés : 0 échec | juste |
| en-tête K6-12 | `34cf6eb0…` versée, identique à `285e222f…` hors durée | `contre-lecture-v5/reproduction-conv-audit-v1/sortie-reproduite.json` = `34cf6eb0360d…`, conforme à son compagnon (identité hors durée non refaite) | juste (existence) |
| en-tête K6-12 | `TZ=Europe/Paris`, UTC+1 depuis le 25 octobre | `ls` 22:36 contre `date -u` 21:37 | juste |
| § 4 | versions 22 et 23 pour le monde et l'engagement | en-têtes des modules | justes |

## 7. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4) ; graines
`numpy.random.SeedSequence(2026102722, spawn_key=(section, indice))` → `random.Random` (R9) ; 1 000 répétitions ; 7,9
secondes ; manifeste dans la sortie. Module importé sans écriture de bytecode.

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v7.py` | `f6760b9df0ad31c1497b0eadea50d0d0353a7cb4dbbeb5dee237532b53ab8663` |
| `contre-verification-pari-signe-v7-sortie.json` | `a75668ecf265c6856bf598cdf70a080c7eaf88a23771fe9e31448d00dabaf1aa` |

- **U** : 33 essais des trois fichiers : 0 échec, 0 erreur ; 259 `def test_` dans `essais/`.
- **A** : `abandonner(gelée, traj)` sans erreur, partie ignorée ; drapeau contradictoire accepté ; partie sautée puis
  `lire` puis abandon « avant partie » : aucune erreur ; `lire` sans partie pour une fiche active : accepté ; aucune trace.
- **B** : partie sautée (ajout si ≥ 1) : 0,379 (10 générations), 0,982 (30) ; E[e] 15,8 / 59,7 ; contrôle 0,034 ;
  E[max(1, e_20)] = 1,7666.
- **C** : exclusion ⊆ : 0 violation / 3 000 ; Σ global tenu, pas α_g ; retrait : union {a, b, c}, rapportées {b, c},
  bonferroni {b}, partie après retrait refusée, motif écrasé ; nuls partiels avec retraits : FDR union 0,0045 (borne
  0,025), rapporté 0,0052, P(≥ 1 fausse) 0,034.
- **D** : conforme strict ≈ j/(n+1) (continu), ≤ (ex æquo) ; masse 0,5 rapportée ; bords j = 1 ; seuils invariants quand
  l'épreuve change, partition du jumeau non ; ordre secret déterministe, sensible à graine, étiquette, banque ; jumeau
  disjoint et couvrant (500 / 500).
- **E** : altération re-scellée acceptée ; clé identique développement / épreuve ; même engagement deux fois : trajectoires
  identiques, acceptées à deux générations ; seuils par strate du seul calibrage ; désalignement garde / contrastes (30 / 20,
  2 coïncidences).

**Limites.** Mondes illustratifs (A′) ; pas de simulation de K7-6 (borne théorique seulement) ; D-S26 bis relue sur le
code et une simulation de retraits aléatoires, pas sur la panne confirmée ; `conception-pari-de-signe-v5.md` et la
contre-lecture v5 non relues (empreintes citées vérifiées par la contre-lecture v6) ; `decision-N-054-v1.md` non relue
(la v7 n'y change rien de nouveau par rapport à la v6, dont la contre-lecture l'a lue).

Pour reproduire, depuis le dossier de mes fichiers :
```
REP=1000 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v7.py > contre-verification-pari-signe-v7-sortie.json
```

## 8. Fichiers lus et empreintes SHA-256 complètes

Dossier `…/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`.
Tous conformes à leurs compagnons `.sha256` ; le code conforme à `EMPREINTES-orchestrateur-pole-v7-v24.txt` (126 « OK »),
lui-même conforme à son compagnon.

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v7.md` | `fb422cbc2614eee112d5a0b430f4827ead879102892a039f388110e942995819` |
| `…/pari-de-signe/contre-lecture-v6/rapport-contre-lecture-pari-signe-v6.md` | `490100af6b30f09914f3a614b4698a6ca46cf30d6e622e1aae68b3affdedf201` |
| `…/pari-de-signe/contre-lecture-v6/contre-verification-pari-signe-v6.py` (empreinte, extrait l. 227–236) | `82edb8fbf68613cd0e658088366b73ebfce38be42e7ca2d0daf10746b0949a3f` |
| `…/pari-de-signe/contre-lecture-v6/contre-verification-pari-signe-v6-sortie.json` (empreinte seulement) | `7a6cd5721ace9b9ecc207f09dd7fbf50b449cfbb362e9a18d4ff80a0c4753ecc` |
| `…/pari-de-signe/conception-pari-de-signe-v6.md` (§ 3.6, l. 103–107 ; empreinte) | `f21982cdf3d73d8e2a90902c40453e55019911404410e5f351af3b14c8ff1475` |
| `…/pari-de-signe/contre-lecture-v5/reproduction-conv-audit-v1/sortie-reproduite.json` (existence, empreinte) | `34cf6eb0360dd08383781c216d06df02b93a298c1f959f8e6f8d04a347d12808` |
| `…/orchestrateur-pole-v7/pole/pari_apparie.py` | `7833d3cf1fbeaa6a89bddfff6be0ef38a76c3b5ca33176a80de78bd2a152e0c6` |
| `…/orchestrateur-pole-v7/pole/monde_banque_scores.py` | `306c47df85bef6732159467a42d49738db341f5d3b86bc29d3908b7847bb449e` |
| `…/orchestrateur-pole-v7/pole/engagement_apparie.py` | `b66bc157e87016202dafc0c9bef513a35362ee8eea0ba27a937293f9ec669da8` |
| `…/orchestrateur-pole-v7/essais/test_v7_pari_apparie.py` (l. 107–113, 120–276) | `fab97ba65eb517e1373baeb43df802f12842a562b0000e7af5d9983114bd7490` |
| `…/orchestrateur-pole-v7/essais/test_v7_monde_banque_scores.py` (l. 1–92, liste des essais) | `066026445e91900a4108f9e2dc22f2f3c6582232877d0a3eacaf06fcc9cb169b` |
| `…/orchestrateur-pole-v7/essais/test_v7_engagement_apparie.py` | `6d168694a6219701c095e0e8f40b14d7500a344c7658e94a9f51796f9654caaa` |
| `…/orchestrateur-pole-v7/pole/outils.py` (`empreinte_objet`, `graine_derivee`, l. 29–30, 82–89) | conforme à `EMPREINTES-…-v24.txt` |

Heure de fin (lue sur `date -u` dans un appel séparé, juste avant cette ligne) : mardi 27 octobre 2026, **21:50:08 UTC**.
