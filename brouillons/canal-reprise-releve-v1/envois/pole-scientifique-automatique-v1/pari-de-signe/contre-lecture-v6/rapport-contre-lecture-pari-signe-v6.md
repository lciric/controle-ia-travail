# Contre-lecture (R2) — « Le pari apparié borné — conception v6 » (Opus 5.5) et le code `pole/pari_apparie.py` (v7, version 21) — rapport v1

Contre-lecteur : sous-agent neuf **Fable 5.1**, autre modèle que l'auteur de la v6 et du code ; je n'ai écrit ni la v6,
ni le code, ni aucune contre-lecture antérieure. Début : mardi 27 octobre 2026, **21:12:46 UTC** ; en-tête écrit à
**21:24:29 UTC** (`date -u`, lus dans des appels séparés). Aucun fichier du dépôt modifié (le module a été importé sans
écriture de bytecode) ; tout ce que j'ai écrit est dans
`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe-v6/`. Aucune clé ni
aucun jeton lu, affiché ou cherché. Aucune dépense : processeur seul (section 7). Aucun des fichiers lus ne contient de
consigne adressée au contre-lecteur. Toutes les empreintes vérifiées (`sha256sum -c`) avant lecture (section 8).

Remarque d'horodatage : les fichiers portent des heures de modification en avance d'environ une heure sur `date -u`
(la v6 est datée 22:06 alors qu'elle existait à mon relevé de 21:12 ; même décalage pour la contre-lecture v5, finie
« à 21:00:11 » et datée 22:00). Aucun chiffre n'en dépend ; mes heures sont celles de `date -u`.

## Verdict

1. **D-S25 bis est opératoire et valide** : telle qu'écrite (budget d'entrée gardé à vie, une lecture e-BH pondérée par
   fin de génération sur toutes les fiches entrées, valeurs gelées, promotion unique, arrêt à 1/b_i), la preuve de la
   contre-lecture v5 § 2 (i) s'applique mot pour mot ; je ne trouve **aucune lecture du texte de D-S25 bis** qui casse la
   borne « taux de fausses découvertes de l'union ≤ Σ_c α_c ≤ α » ; reproduit sur processeur (familles entrées à des
   générations différentes, budgets différents, deux suites de dépense, nuls partiels, arrêt précoce sur les issues :
   0,0085 à 0,0385 sous nul complet ; 0,0056 pour une borne 0,0263 sous nuls partiels ; sortie section 7).
2. **Le code met en œuvre D-S25 bis et D-S27** (`ebh_pondere`, `Course`, `contraste_plafonne`) ; les quinze essais passent ;
   ex æquo, domaine logarithmique, arrêt, gel, somme des niveaux, double entrée, fiches arrêtées non promues : justes.
   **Deux points touchent la garantie, tous deux hors de D-S25 bis** : (K6-1) D-S26 bis ne dit pas d'où vient le budget
   des fiches « nouvelles » de la relecture (ni du nouveau tirage du témoin) et le retrait des promotions sort la
   quantité rapportée de la garantie, sans que ce soit redit ; (K6-2) l'ordre « abandonner avant d'ajouter la partie »
   jette la partie **en silence** : si la décision a vu la partie, la valeur gelée n'est plus une e-valeur (biais 1,77
   par partie jetée, monde A′ à 20 pas) — contrat d'appel à écrire et à vérifier dans le code.
3. **Chiffres** : tous les chiffres de la v6 sont justes contre leurs fichiers (section 6), à une définition près (le
   « k » de la borne α·k/m du témoin compte le témoin : k = 4 pour 3 vraies) ; **deux lectures trompeuses** (« dépendance
   quelconque entre générations » ; « `ebh_pondere` refuse une somme au-dessus de α », qui refuse en fait au-dessus de
   1) ; une option manque à D-S29 ; l'essai du monde A′ passerait aussi si la course ne promouvait jamais rien.
   **Amender en v7 par des corrections locales (D-S26 bis, D-S25 bis (2), section 3, essais), pas refaire.**

---

## 1. Réponses aux questions

### Q1 — La règle de l'héritage (D-S25 bis) : opératoire et valide ?

**Oui.** Les cinq éléments que la contre-lecture v5 demandait sont écrits : budget b_i = α_c/m_c fixé à l'entrée, m_c
fixé avant toute issue, gardé à vie ; e-processus gelé à l'abandon et à la promotion, arrêté à 1/b_i ; une lecture par
fin de génération, e-BH pondérée sur toutes les fiches entrées ; promotion une seule fois ; garantie sur l'union.
Je refais la preuve pour chaque point de la question :

- **Familles nouvelles entrées à des générations différentes avec des budgets différents, lues ensemble.** La règle
  pondérée promeut i seulement si b_i·E_i(τ_i) ≥ 1/k_{τ_i}, et toutes les k_{τ_i} promotions de cette lecture sont dans
  l'union R_∪ (promotion unique), d'où 1/|R_∪| ≤ b_i·E_i(τ_i) pour chaque nulle promue ; E[FDP] ≤ Σ_{i nulle} b_i·E[E_i(τ_i)]
  ≤ Σ_{i nulle} b_i. Les budgets n'ont pas besoin d'être égaux ni d'entrer en même temps : seule compte Σ_i b_i ≤ α
  sur les fiches jamais entrées, ce que Σ_c α_c ≤ α assure. Reproduit : nul complet, cohorte de 4 à α_1 plus 3
  nouvelles par génération à α_g, 10 générations, monde A′ : 0,025 / 0,031 (suite 6/(π²g²), 20 / 200 pas) et 0,0085 /
  0,0385 (uniforme α/10) ; nombre moyen de fausses promotions 0,009 à 0,0385 (sortie, section H).
- **Arrêt au seuil 1/b_i.** Le processus arrêté au premier franchissement reste une surmartingale (temps d'arrêt) ;
  l'arrêt ne gêne pas la règle e-BH (une fiche arrêtée a b_i·E_i ≥ 1 ≥ 1/k : promue à la lecture suivante, quel que
  soit k) et rend exacte la lecture e-Bonferroni (point 6). Un plafonnement min(E, 1/b_i) serait aussi valide (fonction
  concave croissante d'une surmartingale) ; le code gèle à la valeur de franchissement, ce qui est le choix du texte.
- **Valeurs gelées.** Abandon et promotion sont des temps d'arrêt pour la filtration des générations ; le processus
  gelé est une surmartingale arrêtée ; lire les gelées à chaque lecture est donc valide — y compris quand une abandonnée
  gelée **sous** son seuil est promue plus tard parce que k* a grandi (reproduit, section C (1) : une abandonnée à
  b·E = 0,4 promue quand trois sœurs atteignent 1). Le texte l'autorise (« abandonnées … à leur valeur gelée ») : à
  dire explicitement que c'est voulu. **Condition** : la décision de geler ne doit pas avoir vu une partie qu'elle
  jette (K6-2).
- **Promotion une seule fois.** Nécessaire à « toutes les promotions de la lecture sont dans R_∪ » ; de plus k* ne
  décroît jamais (les k* promues gardent b·E ≥ 1/k*), donc une promue est toujours dans les k* premières : le code n'a
  pas à la protéger, mais il le fait (`promues` n'est jamais réduit).
- **Ce qu'il reste à écrire** : (i) la garantie exige que chaque e-valeur de partie soit valide **conditionnellement à
  tout le passé** (unités fraîches tirées de la population, mise prévisible) ; « dépendance quelconque entre
  générations » pris à la lettre (unités réutilisées, unités choisies selon leurs issues) est faux (K6-3) ; (ii) « famille
  d'entrée » : quand une génération porte plusieurs familles (nouvelles, relecture d'une strate, nouveau tirage du
  témoin), elles doivent se partager α_g — le code l'impose par `alpha_engage`, le texte ne le dit pas (K6-1).

### Q2 — Le code met-il en œuvre D-S25 bis ?

**Oui, à un contrat d'appel près.** Lecture ligne à ligne :

- `ebh_pondere` : tri par log b_i + log E_i décroissant (ex æquo départagés par l'identifiant, sans effet : au bord,
  la maximalité de k* inclut toutes les valeurs égales — reproduit, section E : trois fiches à exactement 1/3 toutes
  promues) ; k* = le plus grand k dont la k-ième valeur atteint 1/k (boucle sur tous les k, pas « premier échec ») ;
  domaine logarithmique partout (une partie de log 3 000 ne déborde pas, section C (7)) ; tolérance 1e-12 (négligeable).
  Avec b_i = α/m, identique à la règle ordinaire (essai contre une référence écrite à part, 300 tirages : juste).
  **Mais** elle refuse une somme de budgets > 1, non > α (somme 0,5 acceptée, reproduit) : le contrôle ≤ α est dans
  `Course.entrer` — la v6 § 3 dit le contraire (K6-5).
- `Course.entrer` : m_c = taille de la famille à l'entrée ; budget α_c/m_c ; `alpha_engage` cumule les α_c et n'est
  **jamais** rendu (budgets des abandonnées non récupérables : reproduit, section C (6)) ; une fiche n'entre qu'une
  fois (refus, essai) ; famille vide ou doublon refusés.
- `ajouter_trajectoire` : produit (somme des logs) de la valeur héritée et de la trajectoire **cumulée** de la partie ;
  arrêt au premier instant où le produit atteint −log b_i, valeur gelée à ce franchissement (reproduit : 25 ≥ 20, le
  reste ignoré) ; gelées, promues et arrêtées ne bougent plus. **Ordre des appels** : `abandonner` puis
  `ajouter_trajectoire` ignore la partie sans erreur (section C (3)) — c'est K6-2. `lire` puis `abandonner` (l'ordre de
  l'essai A′) est juste.
- `lire` : une e-BH pondérée sur **toutes** les fiches entrées, gelées comprises ; `promues` ne fait que grandir ;
  renvoie les nouvelles. Deux `lire()` de suite sans partie nouvelle ne promeuvent rien de plus (section C (4)) ;
  rien n'impose « une lecture par fin de génération » (lire plus souvent reste valide : temps d'arrêt plus fins).
- `bonferroni` : les fiches dont le produit a atteint 1/b_i ; cohérent avec l'arrêt.
- Fiches **arrêtées non encore promues** : b·E ≥ 1, promues à la lecture suivante, même abandonnées entre-temps
  (section C (2)).

**Les essais testent-ils ce qu'ils disent ?** Oui pour la famille unique contre la référence, le refus des budgets, le
budget gardé (seuil 100, non 25 : la lecture « seule » l'aurait promue à 30), la promotion unique et le gel, et le
monde A′. **Un essai peut passer pour une mauvaise raison** : `test_nul_complet_lecture_valide_contre_lecture_seule`
n'affirme que « valide ≤ α + 0,01 » et « seule > valide » ; une `lire()` qui ne promouvrait jamais rien le ferait passer
(fausses_valides = 0). Manquent : ex æquo, ordre des appels, abandonnée promue plus tard par k*, somme entre α et 1
acceptée par `ebh_pondere` seule (K6-6).

### Q3 — Le plafond (D-S27) et l'estimande

**Juste.** v′ = (min(m_t, m_max)/m_max)·v(t) reste dans [−1 ; 1] (poids dans [0 ; 1], v dans [−1 ; 1]) ; le poids est
fixé avant toute issue ; E[v′] = E[min(m_t, m_max)·v(t)]/m_max, du signe de l'estimande déclarée « rappel par épisode
plafonné à m_max ». « Coïncide avec celle de N-054 » n'est vrai **qu'en signe** (facteur E[m_t]/m_max si aucune unité ne
dépasse m_max ; E[min(m_t, m_max)]/m_max si v est indépendant de la longueur) : pour le pari de signe cela suffit, mais
la **borne basse rapportée** porte sur E[v′], pas sur le gain de rappel par épisode de N-054 — l'échelle est à déclarer
(K6-8). Pour G1 (m_max = maximum de la banque gelée) rien n'est plafonné et v′ = (m_t/m_max)·v, la mise réduite de la
v3. **Code** : `ponderation_plafonnee` et `contraste_plafonne` font exactement cela (écart 0 contre le calcul direct sur
2 000 tirages, |v′| ≤ 1, m_t = 0 → poids 0 ; m_t et m_max entiers exigés, m_max ≥ 1). Le code ne peut pas vérifier que v
est « calculé sur tous les épisodes » : c'est l'appelant.

### Q4 — La panne confirmée (D-S26 bis)

- **Geler les processus hérités** : temps d'arrêt → valide, rien à dire.
- **Retirer des promotions** : la garantie de D-S25 bis porte sur l'union **avant** retraits ; l'ensemble survivant
  n'est pas couvert par la preuve (1/|R_∪| ≤ 1/k_{τ_i} tombe si des promues de la lecture τ_i sont retirées). La v6 le
  dit pour la **suspension** (« mesuré en baisse »), pas pour le **retrait**, et D-S25 bis (5) ne dit pas quelle union est
  garantie. À écrire : « la quantité garantie est l'union avant retraits ; l'ensemble rapporté après retraits porte la
  réserve de D-S26 bis ». De plus, les fiches retirées et gelées restent-elles **lues** (à leur valeur gelée, elles
  grossissent k* pour les autres à chaque lecture) ? Les exclure des lectures ultérieures est valide (cela ne fait que
  réduire les promotions à chaque lecture) et cohérent avec « bloque toute revendication sur la strate » : à dire.
- **D'où vient le budget des fiches nouvelles de la relecture ?** Le texte ne le dit pas. Sous D-S24 (uniforme
  α/G_max ou 6/(π²g²)), tout α est réparti sur les générations : les fiches de la relecture doivent **entrer dans la
  famille de la génération g′ où elles sont relues** (comptées dans m_{g′}, budget α_{g′}/m_{g′}, ce qui réduit le budget
  des autres nouvelles de g′), ou puiser dans une **réserve scellée au gel** (α = Σ_g α_g + α_réserve). Tout autre
  « nouveau budget » ferait Σ_c α_c > α. Même question pour le **nouveau tirage du témoin** « lu à la même règle » : s'il
  entre dans une famille, il a un budget qui compte ; s'il est un diagnostic hors famille, le dire. Le code impose la
  somme (toute famille passe par `entrer`) mais n'a **aucune** opération de retrait, d'exclusion de lecture ou de gel par
  strate : D-S26 bis n'est pas codée, et la v6 ne prétend pas qu'elle le soit (K6-1).

### Q5 — D-S24 : uniforme α/G_max sur un plafond scellé, arrêt avant G_max

**Valide, y compris sur une décision qui dépend des issues.** La preuve borne E[Σ_{i entrée, nulle} b_i·E_i(τ_i)] ;
l'entrée d'une famille est décidée avant que ses e-valeurs soient observées et E_i vaut 1 à l'entrée, donc
E[1{entrée}·E_i(τ_i)] ≤ 1 quelle que soit la règle d'entrée ou d'arrêt (mesurable sur le passé) ; les familles non
entrées ne dépensent rien. Reproduit : arrêt dès la première promotion ou dès que la cohorte tombe sous 1/10, monde A′,
uniforme α/10 : 0,002 d'au moins une fausse promotion, 2,7 générations faites en moyenne (section S). Deux conditions
à écrire : G_max **ne peut pas être relevé** après lecture (le texte dit « scellé » : juste) ; une course **reprise** après
un arrêt réutilise les créneaux α/G_max restants ou est une course nouvelle avec son propre α (non dit, K6-10). Une
réaffectation **prévisible** du reliquat (déclarée avant la lecture de la dernière génération) serait aussi valide ; la
v6 préfère perdre le reliquat, plus simple : acceptable, à dire comme choix.

### Q6 — D-S29 et D-S30 contre N-054 (points 2 et 4) et N-055

- **D-S29.** Le point 4 de N-054 dit : « la revendication de H1 est restreinte au mode « coût » si la borne basse du gain
  blanc-sur-noir n'est pas au-dessus de zéro dans les autres modes » ; les autres modes sont « contrôles » et le mode
  tenu à l'écart (point 4, « lus sur … »). Les trois lectures (a) dans chacun, (b) dans aucun, (c) par mode sont
  **fidèles** à cette phrase ambiguë ; « restreinte au mode coût = H1 non portée » suit du point 2 (« le mode « coût
  déclaré gonflé » seul ne la porte pas ») : juste. (c) est aussi conforme au point 2 (« ne porte que sur les modes
  mesurés »). **Une option manque** : (d) le mode tenu à l'écart **rapporté, hors décision de H1**, par symétrie avec
  D-S10 retenue par Lazar (« mode tenu à l'écart hors décision » pour G1) — elle s'écarte de la lettre du point 4 et
  n'est donc pas une lecture mais un nœud (modification d'une décision) ; elle répond au problème que la v6 soulève
  (un mode conçu tard et petit décide seul de H1). Et la v6 devrait dire que D-S29 (a) « mode tenu à l'écart compris »
  ne contredit pas D-S10 : objets différents (H1 contre la porte G1) (K6-9).
- **D-S30.** « H1a porte la revendication de H1 (la mesure sur la strate « diffus, flou », telle que le § 5 du programme
  l'écrit) ; H1b … rapportée comme information » (N-055, `decisions-lazar-2026-10-27-v1.md`). L'option (a) de la v6
  (strate « diffus, flou » de chaque mode, mode entier rapporté) est la lecture fidèle ; (b) (mode entier) ferait porter
  H1 par un gain qui peut n'exister que hors de la strate, contraire à N-055. Une contrainte non dite : sous (a), le
  **brief du mode tenu à l'écart** doit produire des unités de la strate « diffus, flou » en nombre suffisant et la coder
  sans connaissance des moniteurs (la strate est « à coder dans la banque de la couche 2 », N-055) ; sinon (a) est
  inapplicable à ce mode (K6-9).

### Q7 — Chaque chiffre : section 6. Tous justes ; une définition de k à préciser (K6-7).

### Q8 — Ce qui tient : section 5.

## 2. Constats, du plus grave au moins grave

### Touche la garantie

**K6-1 — D-S26 bis : budget des fiches « nouvelles » de la relecture sans origine ; retrait des promotions hors de la
garantie, non redit ; fiches retirées non exclues des lectures.**
- **Où.** § 1 « 5, témoin faux promu », D-S26 bis (1) à (3) ; D-S25 bis (1) « famille d'entrée » et (5) « union des
  promotions » ; tableau des décisions.
- **Ce qui manque.** La famille et le niveau des fiches relues (α_{g′} partagé, comptées dans m_{g′}, ou réserve scellée
  au gel) ; le statut du nouveau tirage du témoin (famille et budget, ou diagnostic hors famille) ; « la quantité
  garantie est l'union avant retraits ; l'ensemble rapporté après retraits porte la réserve de la suspension » ;
  l'exclusion des fiches retirées et gelées des lectures ultérieures. Dans le code : aucune opération de retrait,
  d'exclusion ou de gel par strate (`Course` ne sait que geler une fiche et faire grandir `promues`).
- **Correction.** Trois phrases dans D-S26 bis et une dans D-S25 bis (1) (« plusieurs familles à une même génération se
  partagent α_g ») ; `Course.retirer(fiche, motif)` qui marque, exclut des lectures et garde la trace ; essai.

**K6-2 — Ordre des appels : « abandonner » avant « ajouter_trajectoire » jette la partie en silence.** (reproduit,
section C (3) ; biais calculé.)
- **Où.** `Course.ajouter_trajectoire` (retour immédiat si gelée) ; D-S25 bis (2) « gelé quand la fiche est abandonnée ».
- **Ce qui manque.** Le contrat : la valeur gelée est celle **après la dernière partie observée avant la décision**. Si le
  pôle décide d'abandonner en ayant vu la partie de la génération et que l'orchestrateur gèle avant d'ajouter, la
  valeur gelée vaut E(g−1)·max(1, e_g) en espérance : E[max(1, e_g)] = 1,77 dans le monde A′ à 20 pas — ce n'est plus
  une e-valeur. Mesuré sur la fiche elle-même, l'effet est de signe contraire (0,025 contre 0,0425, section T) parce
  que l'abandon est définitif et la fiche sous son seuil ; le risque réel est sur k* des autres fiches (une gelée
  gonflée compte dans le tri). Silencieux : aucune erreur, aucun essai.
- **Correction.** Écrire le contrat dans D-S25 bis (2) ; dans le code, refuser `abandonner` tant que la partie de la
  génération courante n'a pas été ajoutée (compteur de génération par fiche, ou `abandonner(fiche, trajectoire_log)` qui
  ajoute puis gèle) ; essai sur un cas sain et sur l'artefact (R5).

### Lecture trompeuse

**K6-3 — « Sous dépendance quelconque entre fiches et entre générations ».** D-S25 bis (5). Vrai entre fiches ; entre
générations, la condition est que chaque e-valeur de partie soit valide conditionnellement à tout le passé (unités
fraîches tirées de la population, mise prévisible, parties disjointes) — c'est ce que la preuve utilise. Correction :
une phrase dans (2) : « chaque partie est une e-valeur conditionnelle au passé de toute la course ».

**K6-5 — § 3 : « `ebh_pondere` … refuse une somme de budgets au-dessus de α ».** Faux : elle refuse au-dessus de 1 ; le
contrôle ≤ α est dans `Course.entrer` (reproduit : somme 0,5 acceptée par la fonction seule). Correction : texte, ou
donner α à `ebh_pondere`.

**K6-7 — D-S26 bis : « jusqu'à α·k/m dans une strate qui porte k promotions vraies (son seuil e-BH y est m/(α·k)) ».**
Avec 3 vraies, le seuil 25 et la borne 0,04 de la sortie correspondent à k = 4, **témoin compris** (5/(0,05·4) = 25 ;
0,05·4/5 = 0,04). Correction : « k promotions au total, témoin compris » ou « α·(k+1)/m avec k vraies » ; et « est α/m
s'il est seul promu » → « au plus α/m ».

**K6-8 — D-S27 : « elle coïncide avec celle de N-054 »** : en signe seulement (proportionnelle) ; la borne basse
rapportée porte sur E[v′]. Correction : « même signe ; échelle E[min(m_t, m_max)]/m_max, à déclarer avec la borne basse ».

**K6-9 — D-S29 : option (d) absente ; D-S29 (a) et D-S10 à articuler ; D-S30 (a) : contrainte sur le brief du mode tenu
à l'écart.** (Q6.) Correction : ajouter (d) comme nœud (s'écarte de la lettre du point 4) ; une phrase « D-S10 vaut pour
G1, D-S29 pour H1 » ; une ligne au poste de devis : « unités de la strate « diffus, flou » dans le mode tenu à l'écart ».

### Essais

**K6-6 — L'essai du monde A′ passe aussi sans aucune promotion ; cas limites non testés.** Correction : affirmer
`fausses_valides > 0` (attendu ≈ 0,025·400 = 10) ou un encadrement de la fréquence ; essais des ex æquo au bord, de
l'ordre des appels (K6-2), d'une abandonnée promue plus tard par k*, de la somme entre α et 1 (K6-5).

### Clarté

**K6-10 — D-S24 : course reprise après arrêt** (créneaux restants ou course nouvelle) et choix « reliquat perdu » à
dire comme choix (une réaffectation prévisible serait valide).

**K6-11 — « Une seule lecture par fin de génération »** : le code ne l'impose pas (`lire()` à volonté, valide mais pas la
règle) ; à dire que c'est l'orchestrateur qui la tient. Et, nature de e-BH à dire : une fiche sans preuve (E = 1) est
promue dès que k* ≥ 1/b_i ; la garantie reste sur l'union, et la lecture e-Bonferroni (point 6) protège ce qui sort.

**K6-12 — En-tête** : « sortie du script reproduite, identique hors durée, `34cf6eb0…`, non versée » — invérifiable
d'ici ; horodatages en avance d'une heure sur `date -u` (sans effet sur les chiffres).

## 3. D-S25 bis, D-S26 bis, D-S27, D-S24, D-S29, D-S30 : avis

| décision | avis |
|---|---|
| D-S25 bis (0,8) | juste et opératoire ; confiance 0,8 tenable, 0,85 avec K6-3 et le contrat de K6-2 écrits |
| D-S26 bis (0,65) | défendable ; incomplète sur le budget de la relecture, l'union garantie et l'exclusion des retirées (K6-1) ; non codée |
| D-S27 (0,8) | juste ; estimande à déclarer avec son échelle (K6-8) |
| D-S24 (0,75) | juste ; arrêt précoce valide même sur les issues ; reprise de course à dire (K6-10) |
| D-S29 (0,55) | options fidèles ; (d) manque, comme nœud (K6-9) ; recommandation (a) cohérente avec le point 2 |
| D-S30 (0,6) | (a) fidèle à N-055 ; contrainte sur le brief du mode tenu à l'écart (K6-9) |

## 4. Mathématiques en une page (ce que j'ai vérifié à la main)

- e-BH pondérée : pour i promue à la lecture τ, b_i·E_i(τ) ≥ e_(k*) ≥ 1/k*. Les ex æquo au bord sont tous dans les k*
  premiers (sinon k*+1 satisferait la condition). Avec b_i = α/m : E_i ≥ m/(α·k*), la règle ordinaire.
- k* est croissant d'une lecture à l'autre (les promues gardent b·E ≥ 1/k*), donc une promue est toujours relue
  promue ; `promues ⊆ retenues` à chaque lecture (le code n'en dépend pas).
- Arrêt à 1/b_i et gel : surmartingales arrêtées ; min(E, c) le serait aussi (concave croissante).
- Entrée décidée avant observation et E_i(entrée) = 1 : E[1{entrée}·E_i(τ_i)] ≤ 1, d'où la validité de l'arrêt précoce
  sous D-S24 et de toute règle d'entrée mesurable sur le passé.
- Partie jetée après observation : E[E(g−1)·max(1, e_g)] > E[E(g−1)] ; 1,77 en A′ à 20 pas (calcul exact binomial).
- Plafond : poids dans [0 ; 1] fixé avant l'issue ; E[v′] = E[min(m_t, m_max)·v]/m_max.

## 5. Ce qui tient (une ligne chacun)

- K5-1 fermé : D-S25 bis est la règle que la contre-lecture v5 demandait, mot pour mot, et la preuve s'y applique.
- K5-2 fermé : plafond sur tous les épisodes, estimande déclarée, m_max dans la clé, G1 non plafonné.
- K5-3 fermé : m_g/α_g (nouvelles), m_c/α_c (relancées), m/α (famille de G1) ; le code le dit aussi (`evaluer`, `Course`).
- K5-4 fermé : règle de H1 marquée lecture, trois lectures, « restreinte = non portée », poste de devis.
- K5-5, K5-8 fermés sur le fond : α/m seul, α·k/m avec k promotions (k à définir, K6-7) ; panne confirmée écrite.
- K5-6 fermé : 0,034 à 0,041 dits « au niveau α » ; 0,020 à α_1 juste (sortie H, S1, cohorte_1).
- K5-7 fermé : population (ou « union des viviers lus », intersection des nuls) et m_max dans la clé — juste.
- K5-9 à K5-13, K5-15 fermés : chiffres, renvois, seuil 20 / 60, τ = 1 %, D-S10, question des noirs spécialisés.
- K5-14 fermé : uniforme α/G_max à préférer ; chiffres 0,005 / 0,0034, 0,00167 / 0,00122, 61 % justes.
- Code : `ebh_pondere` = e-BH ordinaire pour une famille (300 tirages contre une référence indépendante) ; ex æquo
  justes ; domaine logarithmique ; budgets jamais rendus ; double entrée refusée ; arrêt gelé au franchissement ;
  arrêtée puis abandonnée promue ; course vide ; quinze essais passent.
- Simulations de la v6 (section 3 : « lecture valide ≤ α, lecture seule au-dessus ») : conformes à ce que l'essai fait.
- Section 4 : ce qui reste ouvert est dit (lien au cycle, mondes illustratifs, contrôle 18, R7, D-S29/D-S30, devis).

## 6. Chiffres : chaque chiffre de la v6 contre son fichier

| où (v6) | cité | fichier, valeur | verdict |
|---|---|---|---|
| en-tête | K-2 à K-19 fermés, K-3 trop large, K-5 à moitié, K-1 sauf deux champs ; deux points garantie ; trois lectures ; deux chiffres, un pointeur | `4e8e3270…` verdict 1–3 | juste |
| verdict 1, D-S25 bis | 0,074 (A′ 20 pas, seule) ; 0,105 (A′ 200 pas, mixte α_1) ; 0,0275 ; 0,0315 (valides) | `285e222f…` H : 0,074 ; 0,105 ; 0,0275 ; 0,0315 | justes |
| D-S25 bis, lectures interdites | cohorte seule 0,0735 > α_1 = 0,030 ; S1 0,0465, cohorte 0,040 ; mixte S1 0,060 ; valide S1 0,022 ; mixte α_g 0,030 ; 0,0115 | H : 0,0735 ; α_1 = 0,0304 ; 0,0465 ; 0,04 ; 0,06 ; 0,022 ; 0,03 ; 0,0115 | justes |
| K5-6 | cohorte de 4 nulles à α_1, S1 : 0,020 | H, S1, cohortes, cohorte_1 : 0,02 | juste |
| verdict 1 | 1,00 aux générations 1 à 3 et 0,99 à la génération 10 | `c7836e12…` B : 1,0 / 1,0 / 1,0 / 0,9918 | juste |
| en-tête (K5-9) | K-10, K-11 un chiffre chacun ; K-12 deux renvois | `4e8e3270…` § 3 | juste |
| 2.1, D-S27 | 0,160 contre 0,1599 ; 0,249 contre 0,267 ; promotion 1,00 (m_max 20) ; 0,001 (vrai maximum) | `285e222f…` P : 0,16 / 0,1599 ; 0,2493 / 0,267 ; 1,0 ; 0,001 | justes |
| verdict 6, D-S26 bis | 0,012 à 1 000 ; α/m = 0,01 ; α·k/m = 0,04 ; 0,0035 / 0,003 / 0,012 | `285e222f…` T : 0,012 ; 0,01 ; seuil 25 à k = 4 ⇒ 0,04 ; 0,0035 / 0,003 / 0,012 | justes ; **k = 4, témoin compris** (K6-7) |
| D-S26 bis | 0,0005 contre 0,0014 ; 0,00125 contre 0,002 ; 0,00275 contre 0,00575 | T : 0,0005 / 0,00137 ; 0,00125 / 0,002 ; 0,00275 / 0,00575 | justes |
| § 6 | 17,61 (6 unités) ; 31,11 (7) ; m = 3 : 55,77 (8), 101,09 (9) | `68b8f95c…` section 6 : 17,61 ; 31,11 ; 55,77 ; 101,09 | justes |
| D-S24 | 0,005 contre 0,0034 dès g = 3 (G_max 10) ; 0,00167 contre 0,00122 dès g = 5 (G_max 30) ; 61 % à g = 1 | `68b8f95c…` : 0,005 / 0,003377, g = 3 ; 0,001667 / 0,001216, g = 5 ; 0,6079 | justes |
| H1, devis | 40 unités sabotées pour 20 points, 100 pour 10 (v3 § 6) | `1518a12f…` l. 55 : « 40 pour 20 points, 100 pour 10 » | juste |
| en-tête | sortie reproduite `34cf6eb0…`, non versée | — | invérifiable |

Les empreintes citées (`95af46e4…`, `4e8e3270…`, `ece834a8…`, `285e222f…`, `c7836e12…`, `d9a6ff1b…`) correspondent aux
fichiers (section 8).

## 7. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4) ; graines
`SeedSequence(2026102721, spawn_key=(section, indice))` (R9) ; 2 000 répétitions ; 17,5 secondes ; manifeste dans la
sortie. Le module est importé depuis le dépôt sans écriture (`sys.dont_write_bytecode`, aucun `__pycache__` créé dans
`essais/`).

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v6.py` | `82edb8fbf68613cd0e658088366b73ebfce38be42e7ca2d0daf10746b0949a3f` |
| `contre-verification-pari-signe-v6-sortie.json` | `7a6cd5721ace9b9ecc207f09dd7fbf50b449cfbb362e9a18d4ff80a0c4753ecc` |

Chacun a son compagnon `.sha256` dans le même dossier.

- **U** : les 15 essais de `essais/test_v7_pari_apparie.py` lancés tels quels : 0 échec, 0 erreur.
- **E** : ex æquo au bord (trois à 1/3 : toutes promues ; trois à 1/2 : toutes) ; somme 0,5 acceptée par `ebh_pondere`
  seule ; course vide ; tolérance 1e-12.
- **C** : abandonnée à 0,4 promue plus tard (k* = 4) ; arrêt gelé à 25 ; arrêtée puis abandonnée promue ; abandon avant
  partie : partie ignorée sans erreur ; budgets des abandonnées non rendus ; log 3 000 sans débordement.
- **H** : nul complet, familles à budgets différents, A′ 20 / 200 pas : 6/(π²g²) 0,025 / 0,031 ; uniforme α/10
  0,0085 / 0,0385 ; nombre moyen de fausses promotions 0,009 à 0,0385.
- **N** : nuls partiels (cohorte 2 vraies + 2 nulles ; 1 vraie + 2 nulles par génération) : taux de fausses découvertes de
  l'union 0,0056 pour une borne 0,0263 ; 2,03 vraies promues sur 11 (vraies lentes : ×1,2 par pas en espérance).
- **S** : arrêt sur les issues sous uniforme α/10 : 0,002 ; 2,68 générations en moyenne.
- **T** : ordre juste 0,0425 ; abandon avant partie basse 0,025 (fiche seule : l'abandon définitif coûte plus qu'il ne
  rapporte ; le biais E[max(1, e_g)] = 1,77 est calculé à part, exact).
- **P** : `contraste_plafonne` contre le calcul direct : écart 0 ; |v′| ≤ 1 ; m_t = 0 → 0.

**Limites.** Mondes illustratifs (martingale à pile ou face) ; mécanismes, pas prédiction de la banque réelle ; je n'ai
pas simulé D-S26 bis (pas codée) ni le lien au cycle ; N-007/N-008 lu seulement pour son en-tête et ses lignes « G1 »
(empreinte vérifiée), le fond de la question 6 ne le requérant pas.

Pour reproduire, depuis le dossier de mes fichiers :
```
REP=2000 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v6.py > contre-verification-pari-signe-v6-sortie.json
```

## 8. Fichiers lus et empreintes SHA-256 complètes

Dossier `…/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`.
Tous conformes à leurs compagnons `.sha256` ; le code conforme à `EMPREINTES-orchestrateur-pole-v7-v21.txt` (aucune ligne
hors « OK »), lui-même conforme à son compagnon.

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v6.md` | `f21982cdf3d73d8e2a90902c40453e55019911404410e5f351af3b14c8ff1475` |
| `…/pari-de-signe/conception-pari-de-signe-v5.md` (lignes D-S25 et D-S27 du tableau des décisions, l. 126 et 128 ; le reste par la contre-lecture v5) | `95af46e4b8f317685ccc8755d6e3d0447ba109fd8771a0139eb9470c2bca8f8c` |
| `…/pari-de-signe/conception-pari-de-signe-v4.md` (empreinte seulement) | `c63d8539660d265d65e9a957a07b0877a13001a48df17776d5a0151b75a35e93` |
| `…/pari-de-signe/conception-pari-de-signe-v3.md` (§ 6, l. 55) | `1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14` |
| `…/pari-de-signe/calculs-conception-v6.py` | `d7aee8edb2582fafe172e911e493643db97a5c010f2a37e8fe261cf65e22c07f` |
| `…/pari-de-signe/calculs-conception-v6-sortie.json` | `68b8f95c9225b4ec413ed747e833b982514924f3db39d465666fdcfe7ec43384` |
| `…/pari-de-signe/decisions-lazar-2026-10-27-v1.md` | `c2cfa1597e85431e9ab661e95fc2f94b170b3ec65744211e1e277a2aa8e2015a` |
| `…/pari-de-signe/contre-lecture-v5/rapport-contre-lecture-pari-signe-v5.md` | `4e8e3270908710bbea0fd7c7945065cb1ab1470332be13ca41d0ab75c0b7651c` |
| `…/pari-de-signe/contre-lecture-v5/contre-verification-pari-signe-v5.py` (empreinte, non relu) | `ece834a81a94dc7d6b04aa721e622c3b07a4bf4654ad1fe075c961b854b66a69` |
| `…/pari-de-signe/contre-lecture-v5/contre-verification-pari-signe-v5-sortie.json` | `285e222fed8e9770e7f8f117ce60b58ed25e01b75117c34241a7463ee9f9b5d3` |
| `…/pari-de-signe/contre-lecture-v4/contre-verification-pari-signe-v4-sortie.json` (section B) | `c7836e12275be249ae5ac0f622447592a9fe39e7a850005fc3a1a5ba52d79368` |
| `…/pari-de-signe/noeuds-pour-lazar-v1.md` (empreinte seulement) | `d9a6ff1b08d795456e036a20ea68752938f97c5b6b587adaf5a74b3aad3dc23a` |
| `…/orchestrateur-pole-v7/pole/pari_apparie.py` | `b14677b495d1457b335bcaf2653dc7d77ff1e16cbdc4853898609394af90d240` |
| `…/orchestrateur-pole-v7/essais/test_v7_pari_apparie.py` | `608d5c45ddbf2166afeb37341911db8a580b7d7fd7f0fb0858233c663ab94d9f` |
| `…/erratum-heures-27-octobre-v1.md` (contexte des horodatages) | conforme à son compagnon |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-054-v1.md` (lecture seule) | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-007-N-008-v1.md` (lecture seule, en-tête et lignes G1) | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` |

Heure de fin (lue sur `date -u` dans un appel séparé, juste avant cette ligne) : mardi 27 octobre 2026, **21:28:10 UTC**.
