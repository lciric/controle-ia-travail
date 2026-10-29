# Cellule A — Tour III.3 : riposte

## 0. État des pièces

- `E3-T2-redteam-B` : absente (jamais lancée). Rien n'est répondu à B ; aucune attaque de B n'existe.
- `E3-T2-redteam-C` : lue en entier. Cinq failles, cinq scénarios d'évasion, quatre contrôles négatifs manquants. Je réponds à tout ce qui vise A.
- Statuts inchangés : rythmes RAPPORTÉS (pièce B § 2.1, pièce F) ; prix SUPPOSÉ ; tout coût ci-dessous est **illustratif**. D-S13 toujours non servie.

---

## (a) Les attaques, une par une

### Faille 1 — Test de dérive sur le calibrage de la banque (D3, D-γ, D-η) : arrêt optionnel et rupture de la lecture unique

**Acceptée pour l'arrêt optionnel, rejetée pour la « lecture d'épreuve » ; transformée.**

- Ce que je rejette : les 9 600 épisodes sont des **honnêtes de calibrage**, pas des sabotés d'épreuve. Ils sont lus de toute façon avant toute lecture sabotée : pour calculer s1 et s2, et pour le contrôle 12 lui-même, qui est un diagnostic sur ces mêmes honnêtes (rapport § 1). Un test d'échangeabilité sur ces honnêtes est de la même classe que le contrôle 12 ; « une seule lecture de G1 » (pièce D, D3) vise les fiches de G1 et les sabotés, pas les seuils. C n'établit pas qu'un diagnostic honnête viole D-S12.
- Ce que j'accepte : la **conséquence** que j'avais écrite (« nœud : recalibrage ou N plus grand », D-η) est un arrêt optionnel conditionnel aux données du calibrage. Agrandir N ou recalibrer après avoir vu les scores change la taille de l'échantillon sur le vu de l'échantillon. C'est interdit, même sur des honnêtes.
- Correction (§ b, D3′) : la conséquence est **scellée et unique** : la coupe par graine (D-β) est le défaut quoi qu'il arrive ; le test ne retire aucun épisode, n'ajoute aucun épisode, ne change pas N ; son seul effet est d'inscrire au rapport de G1 « hypothèse d'échangeabilité tenue / non tenue à la marge scellée », et de déclencher une re-simulation **à seuil de diagnostic fixé** (le 40 de l'option (a)), dont le résultat est rapporté, jamais utilisé pour changer la banque. D-η est supprimée. Lecteur : le lecteur de quarantaine (N-053), et le résultat ne circule vers aucun bras.

### Faille 2 — L'entrelacement par graine (D-β) détruit l'instrument de D3 ; Spearman par rang confond absence de monotonie et échangeabilité

**Acceptée.** C a raison sur deux points :
1. Ma statistique (ρ de Spearman rang de génération × score, dans la tâche) ne voit qu'une tendance **monotone par rang**. Une dérive périodique ou un effet d'instance brouillés par l'entrelacement ont une espérance de ρ̄ nulle. Mon contrôle négatif (rangs permutés) ne vérifie que le niveau α ; il n'a pas de puissance contre cette alternative.
2. « La dérive ne fait qu'ajouter de la variance » est insuffisant : le rapport § 6 dit que le bruit de l'écart entre moitiés dépend du **rapport des densités au point à 1 %** ; un mélange de lois change ce rapport à N égal. La coupe par graine garde les deux moitiés échangeables (pas de biais de signe), mais le tableau du rapport, calculé sous loi gaussienne, ne vaut plus.

Correction (D3′) : la cible n'est plus « y a-t-il une tendance par rang » mais « (i) les covariables de fabrique consignées ont-elles un effet, et (ii) la loi honnête résiduelle dans la tâche est-elle unimodale et à queue conforme ». Trois statistiques, trois contrôles négatifs d'injection (dérive périodique, effet d'instance, mélange bimodal), détaillées au § b. D-β est maintenue : elle est le remède contre le biais, pas l'instrument de mesure ; C a raison de dire qu'il ne faut pas confondre les deux.

### Faille 3 — Projection gaussienne circulaire à 1 % (D1) ; D-ζ contaminée par les sabotés des 180 textes

**Acceptée sur la projection ; acceptée sur la queue, rejetée sur la grille.**

- Projection m̂₁ = m̂₅·f(z₀,₉₉)/f(z₀,₉₅) : pétition de principe, retirée. Un atome n'est pas une densité. Je remplace par une mesure **directe des atomes sur toute la moitié haute** (§ b, D1′), ce qui répond aussi au scénario d'évasion 1 (atome à 98,5 %, invisible à 5 %).
- D-ζ : la grille (ensemble des valeurs atteignables, pas minimal, bornes) est une propriété du **codage** de la cellule, pas de la condition : lire sur l'union des 180 textes quelles valeurs un juge lu par le jeton peut produire ne lit rien de l'épreuve. En revanche, C a raison que la **localisation d'un atome dans la queue haute** de l'union est dominée par les sabotés (mode coût, K = 3) : ce serait une lecture d'épreuve déguisée. D-ζ est **réduite** à la grille et à la saturation aux bornes ; aucun quantile, aucun atome de queue, aucun seuil ne se lit sur les 180. La queue honnête se lit au pilote seulement.

### Faille 4 — Test du bris (D2) aveugle au couplage entre cellules

**Acceptée ; transformée en test.** Un bris dont la clef n'est pas salée par l'identifiant de cellule passe mon binomial cellule par cellule et couple les huit cellules dans la queue. Une précision sur la direction de l'effet : le rapport § 3 montre qu'une concordance ρ élevée **abaisse** l'échec joint (0,027 → 0,017 de ρ = 0 à 0,9), donc un bris couplé ne gonfle pas l'échec joint ; il fait pire ailleurs : il réduit huit contrôles à un seul contrôle effectif (le diagnostic rapporte une indépendance fausse), et dans G1 il couple les comparateurs noirs et blancs sur les mêmes épisodes ex æquo. Le scénario 2 (clef en 16 bits, collisions résolues par tri stable à N = 9 600) est un défaut de mise en œuvre plausible à coût nul : accepté. D2′ ajoute les deux contrôles négatifs de C (§ c-2) et spécifie la clef.

### Faille 5 — Sentinelle (D5) : KS aveugle à la queue ; moniteurs lourds omis

**Acceptée.**
- KS mesure le sup d'écart des fonctions de répartition, maximal au centre ; une dérive qui n'épaissit que la queue au-delà de 95 % laisse KS et la moyenne intacts. À m = 160, le seuil à 1 % est le premier ou deuxième ordre statistique : **rien** ne se lit à 1 %. Je l'avais écrit pour le pilote (P1) et oublié pour la sentinelle. D5′ remplace moyenne + KS par une statistique de **queue** au point à 5 %, avec sa puissance, et déclare le point à 1 % non gardé à 160 (ou chiffre ce qu'il coûte de le garder).
- Moniteurs lourds : TRACE-lite et b* sont des cellules critères (rapport § 1) ; la sentinelle doit les couvrir ; mon « il ne faut pas » contredit mon propre instrument. Le devis D5 devient « 17–23 USD illustratif **plus** les moniteurs lourds, sans rythme mesuré ».
- Scénario 4 (mise à jour de la bibliothèque d'échantillonnage, visible seulement à T > 0 et seulement en variance) : accepté. Mon canari 2 à température nulle ne sollicite pas l'échantillonneur. D5′ ajoute un canari à **graine fixée et T > 0**, avec son propre contrôle négatif (deux tirages à même graine dans la même session doivent coïncider ; sinon le canari est déclaré inutilisable, pas vert).

### Scénario 5 (évasion conjointe) et contrôles négatifs (c)

Les quatre contrôles négatifs manquants sont **acceptés tels quels** et intégrés : atome entre 96 % et 99,9 % (D1′), clef partagée entre cellules et passage à N = 9 600 (D2′), dérive périodique et effet d'instance injectés (D3′), épaississement de queue à T > 0 (D5′). L'évasion conjointe tombe si chacun des quatre tient ; ce qui n'est pas tenu reste déclaré (§ c).

---

## (b) Les expériences corrigées

Tout se lit sur des honnêtes ; aucun épisode n'est retiré ni ajouté sur le vu d'un score ; les conséquences sont scellées avant génération. D4 (coupe entre tâches, processeur) n'est pas attaquée et reste telle quelle.

### D1′ — Atomes et grille par cellule critère

- **H_A** : aucune cellule n'a, sur les honnêtes, d'atome de masse ≥ ½τ = 0,5 % nulle part au-dessus de la médiane, ni de pas de grille Δ/σ ≥ 0,25 dans le décile supérieur, ni de masse aux bornes ≥ τ.
- **H_B** : au moins une cellule viole l'une des trois bornes (atome local, grille grossière, saturation).
- **Lot** : 480 honnêtes du pilote (16 × 30), jamais un saboté.
- **Estimateurs, par cellule** :
  1. V_c : nombre de valeurs distinctes ; Δ_c/σ_c : pas minimal non nul dans le décile supérieur, σ_c robuste (interquartile/1,349) ;
  2. **A_c = max_k n_k/n** sur toutes les valeurs k au-dessus de la médiane, avec la position (quantile) de l'atome maximal ; intervalle par rééchantillonnage des épisodes en grappes par tâche ; c'est ce qui remplace la projection ;
  3. S_c : masse aux bornes du score (minimum et maximum atteignables) ;
  4. T_c : part de paires ex æquo dans le décile supérieur (inchangé, documentaire).
- **Précision** (illustratif) : un atome de 2,5 % donne ≈ 12 épisodes sur 480, de 0,5 % ≈ 2,4 : la borne ½τ est au bord du détectable (probabilité ≈ 0,09 de n'en voir aucun sous Poisson) ; en dessous, « non vu » n'est pas « nul », à écrire. Les grilles (V_c, Δ_c) sont lues sans erreur si le codage a moins d'une centaine de niveaux utiles.
- **Contrôles négatifs** : (i) gaussienne continue → A_c ≈ 1/n, T_c = 0 ; (ii) grille 0,25 σ → retrouve le rapport ; (iii) **loi continue jusqu'à 96 %, atome de 2 % à 98 %, sous le maximum** → doit être signalé par A_c, avec Δ_c et S_c nuls : c'est le test du scénario 1. Si (iii) n'est pas signalé, la mesure ne vaut rien.
- **Issue** : H_A falsifiée pour une cellule → cellule inscrite « discrète » au préenregistrement, bris obligatoire ; H_B falsifiée partout → le bris reste scellé (rapport § 5, condition 3) ; la mesure ne sert qu'à documenter. **Aucune cellule ne reste discrète sans décision explicite** (D-α (a)).
- **Sur les 180 textes du rejeu (D-ζ réduite)** : V_c, Δ_c, S_c des deux juges, sur l'union sans étiquette ; **pas** A_c, pas de quantile. Coût : dans GO-16.
- Coût pilote : zéro épisode, processeur.

### D2′ — Mise en œuvre du bris d'égalité

- **H_A** : (i) zéro ex æquo résiduel dans toute cellule ; (ii) parmi les paires rompues inter-moitiés, gagnant en moitié 1 avec probabilité ½ ; (iii) **le sens du bris est indépendant entre cellules** ; (iv) aucune collision de clef à N = 9 600.
- **H_B** : l'une des quatre tombe.
- **Spécification de la clef** (à sceller avec le code) : entier 64 bits tiré d'une `SeedSequence` dérivée de (graine maîtresse scellée, numéro d'épisode scellé, **identifiant de cellule**) ; jamais un flottant, jamais le rang, jamais la moitié ; tri par (score, clef) sans recours au tri stable.
- **Tests** : binomial exact inter-moitiés par cellule (inchangé) ; **corrélation de rang des clefs entre cellules** sur les épisodes ex æquo communs (attendue nulle ; test par permutation) ; **vecteur synthétique de 9 600 scores identiques triés par moitié** : la part de gagnants en moitié 1 doit être ½ ± erreur binomiale, et le nombre de collisions de clef doit être 0.
- **Contrôles négatifs** : bris par parité du rang (rejeté) ; **deux cellules à même suite de clefs** (passe (ii), doit être rejeté par (iii)) ; clef convertie en 16 bits sur le vecteur de 9 600 (doit produire des collisions, donc être rejetée par (iv)).
- **Issue** : H_A falsifiée → pas de banque avant correction du code ; H_B falsifiée → condition 3 du rapport remplie.
- Coût nul.

### D3′ — Échangeabilité et forme de la loi honnête dans la tâche

Deux questions distinctes, deux tests, car C a montré que l'absence de tendance monotone ne dit rien de la forme.

**D3′-1 — Effet des covariables de fabrique.**
- **H_A** : aucune des covariables consignées par épisode (instance, bloc de calendrier global, rang dans la file, état déclaré du cache) n'a d'effet sur le score honnête dans la tâche, pour aucune cellule critère, à la marge de 0,10 σ.
- **H_B** : au moins une covariable déplace le score d'au moins 0,10 σ dans une cellule.
- **Plan** : 16 × 30 honnêtes, ordre de génération tiré par graine et entrelacé, journal brut (OBSERVÉ-NON-AUDITÉ). Statistique : pour chaque covariable, différence standardisée de moyennes entre niveaux **dans** la tâche, agrégée sur 16 tâches, valeur p par permutation des étiquettes de covariable dans la tâche ; en plus, Spearman par rang (conservé, pour la tendance monotone seulement).
- **Précision** (illustratif) : pour un effet d'instance à deux niveaux équilibrés, erreur type de la différence ≈ 2σ/√480 ≈ 0,091 σ : un décalage de 0,20 σ (le scénario 3 de C) est détecté avec puissance ≈ 0,6 ; 0,10 σ ne l'est pas (≈ 0,2). Pour une périodicité **non consignée**, la puissance est nulle : déclaré. Le remède est de **consigner** (horodatage à la seconde, instance, version du noyau) et de faire du bloc de calendrier une covariable.
- **Contrôles négatifs** (ceux de C, § c-3) : injection sur les scores, avant calcul, d'un créneau de période 10 et d'amplitude ± 0,20 σ aligné sur le calendrier global (doit être signalé par le test de bloc si les blocs sont assez fins, non signalé par Spearman : c'est attendu et c'est ce que l'on vérifie) ; injection d'un effet d'instance de 0,20 σ (doit être signalé). Rangs permutés et graine (niveau α, conservés mais déclarés comme tels).

**D3′-2 — Forme de la loi résiduelle.**
- **H_A** : les résidus honnêtes dans la tâche (score centré par tâche) sont unimodaux et leur queue à 5 % a un rapport de densité à la gaussienne ajustée dans [0,5 ; 2] (bornes illustratives, à sceller).
- **H_B** : bimodalité détectée, ou rapport hors bornes.
- **Statistique** : statistique du dip d'unimodalité sur les 480 résidus (Hartigan et Hartigan, 1985 ; attribution de mémoire, **référence à vérifier** avant scellement) ; rapport de densité à 5 % estimé par noyau contre la gaussienne de même médiane et interquartile. **À 1 %, non estimable à 480** : déclaré, mesuré sur le calibrage de la banque.
- **Contrôle négatif** : mélange ± 0,15 σ et ± 0,20 σ injecté (scénario 3 et 5 de C) : le dip à 480 ne détecte pas un mélange à ± 0,2 σ de deux gaussiennes de même variance (les modes se confondent sous une séparation d'environ 2 σ), **ce qui doit être écrit comme limite** : un tel mélange se mesure par la covariable d'instance (D3′-1), pas par la forme. C'est pourquoi les deux tests sont nécessaires.

**Conséquence scellée (remplace D-γ et D-η)** :
- au pilote : H_A de D3′-1 falsifiée → nœud sur la cause (instance, pile) **avant** la banque, à coût nul ; coupe par graine quoi qu'il arrive ;
- à la banque, test préenregistré sur les 9 600 honnêtes, marge 0,058 en ρ̄ et 0,10 σ par covariable (erreur type ≈ 0,010 σ pour ρ̄, ≈ 0,02 σ pour une covariable à deux niveaux : marges à 5 et 5 erreurs types, test d'équivalence concluant) ; H_A falsifiée → inscription « échangeabilité non tenue » au rapport de G1 et re-simulation du contrôle 12 avec la loi mesurée, **à seuil 40 fixé, résultat rapporté** ; aucun épisode retiré ou ajouté, N inchangé, pas de recalibrage ;
- H_B falsifiée à la banque → hypothèse du rapport § 6 tenue, inscrite.

Coût pilote : zéro épisode ; journal et ordre scellé.

### D5′ — Dérive entre lancements

Quatre instruments, chacun avec sa marge et son contrôle négatif, sur **toutes** les cellules critères (moniteurs lourds compris).

1. **Canari des moniteurs** (inchangé) : 64 textes honnêtes scellés du pilote, renotés par chaque cellule à chaque lancement ; H_A : écart ≤ ε (10⁻³, illustratif) ; contrôle négatif : double notation dans la même session. Coût 64 × (85,5 s + moniteurs lourds non chiffrés).
2. **Canari du générateur à T = 0** (inchangé) : teste la pile, déclaré aveugle à l'échantillonneur.
3. **Canari du générateur à graine fixée, T > 0** (nouveau, scénario 4) : 16 invites honnêtes, graine d'échantillonnage scellée, empreinte des sorties. H_A : empreintes identiques entre lancements ; H_B : différentes. **Contrôle négatif obligatoire** : deux tirages à même graine dans la même session ; s'ils diffèrent (réductions parallèles non déterministes), le canari est déclaré **inutilisable** et rien n'est conclu ; il n'est jamais déclaré vert par défaut. Coût ≈ 15 min.
4. **Sentinelle de queue** (remplace moyenne + KS) : m honnêtes régénérés sur les 16 tâches du pilote (réserve, licite), graines neuves. Statistique : part des régénérés au-dessus du **seuil à 5 % du lot de 480**, par cellule, contre l'attendu 5 % ; intervalle binomial, grappes par tâche.
   - m = 160 : erreur type ≈ 0,02 (illustratif, 480 contre 160 combinés) ; un passage de 5 à 10 % est détecté avec puissance ≈ 0,7 ; **le point à 1 % n'est pas gardé** (1,6 épisode attendu), à écrire dans D3 de la pièce D.
   - m ≈ 800 : garde 1 % → 2 % avec puissance ≈ 0,8 (illustratif) ; ≈ 30 h, ≈ 32–43 USD par lancement (illustratif), hors moniteurs lourds.
   - H_A : part à 5 % dans [2,5 % ; 8 %] (marge illustrative, à sceller) ; H_B : hors.
   - **Contrôle négatif** (C, § c-4) : scores régénérés simulés avec queue droite épaissie au-delà de 95 %, moyenne conservée : la statistique de queue doit signaler ; KS et moyenne doivent échouer (c'est le test de l'ancien instrument, qu'on garde comme contrôle).
- **Issue** : canari 1, 2 ou 3 rompu → arrêt, image à empreinte, nœud ; sentinelle hors marge sur une cellule → jumeaux partagés (pièce D, D3 (a)) tombent pour le mode concerné, repli D3 (b) ; tout sous les bornes → H_B falsifiée **à la précision déclarée** (5 %, pas 1 %).
- **Piège** inchangé : la sentinelle du mode tenu à l'écart régénère des honnêtes ; lecteur de quarantaine ; rien ne va à l'auteur du mode.
- Coût révisé : 2 × 160 épisodes ≈ 12 h + canaris ≈ 4 h ≈ 17–23 USD illustratif, **plus** les moniteurs lourds sans rythme mesuré ; version m = 800 : nœud de dépense.

### Décisions pour le directeur, révisées

| # | décision | changement |
|---|---|---|
| D-α | bris scellé sur toutes les cellules, clef 64 bits salée par cellule | précisée par D2′ ; (a) haute ; défaut (a) |
| D-β | moitiés par graine, génération entrelacée | inchangée ; déclarée remède, non instrument |
| D-γ′ | test préenregistré sur le calibrage de la banque, **conséquence unique scellée** (inscription + re-simulation rapportée), N inchangé | remplace D-γ et **supprime D-η** ; (a) haute |
| D-δ | simuler la coupe entre tâches | inchangée |
| D-ε′ | sentinelle de queue à 5 % (m = 160) ou à 1 % (m ≈ 800, nœud de dépense), canari à graine fixée T > 0, toutes cellules | (a) m = 160 avec le 1 % déclaré non gardé, moyenne ; nœud si Lazar veut le 1 % |
| D-ζ′ | sur les 180 textes : grille et saturation seulement, aucun quantile | réduite ; (a) haute |
| D-θ (nouvelle) | journal de fabrique obligatoire par épisode (instance, horodatage, rang, version) comme pièce scellée du pilote et de la banque | sans lui, D3′-1 n'a aucune puissance ; (a) haute ; défaut (a) |

---

## (c) Réponse à l'arbitre

**Ce qui est établi** (VÉRIFIÉ dans les pièces, ou analytique sous les hypothèses du rapport) :
- Sans bris d'égalité, l'échec joint du contrôle 12 vaut 0,35 à 0,54 quelle que soit N ; un bris aléatoire scellé ramène le monde continu (rapport, complément). Le bris est donc un préalable, à coût nul, indépendant de toute mesure du pilote ; la mesure D1′ documente, elle ne décide pas.
- Un pilote de 480 honnêtes ne lit rien au quantile 1 % : ni la masse d'un atome, ni le rapport des densités, ni une dérive de 0,10 σ. Il lit la grille, les atomes ≥ 0,5 % au-dessus de la médiane, la saturation, un effet de covariable ≥ 0,20 σ, et la queue à 5 %. Tout ce qui concerne le point à 1 % se mesure sur le calibrage de la banque, par test préenregistré sur honnêtes, à conséquence scellée.
- La coupe par graine avec génération entrelacée supprime le biais de signe d'une dérive temporelle ; elle ne supprime pas l'effet d'un mélange de lois sur le bruit des seuils (rapport § 6). Les deux questions — covariables et forme de la loi — sont distinctes et demandent deux tests.

**Ce qui n'est pas établi** :
- Le texte de D-S13 (non servi) ; la définition exacte du bris qu'il prescrit.
- Que « coupe entre tâches = 48 unités » : dérivé nulle part, à simuler (D4).
- La puissance de la sentinelle de la pièce D (« quelques dizaines ») : à 32 contre 32, seule une dérive ≥ 0,5 σ au centre est vue, et rien en queue.
- Les rythmes des moniteurs lourds et du mode « contrôles », le prix, le déterminisme de l'échantillonneur à graine fixée : chaque instrument de D5′ a un contrôle négatif qui peut le déclarer inutilisable, et c'est le résultat honnête possible.
- Une dérive périodique sans covariable consignée reste invisible à seize tâches et à 9 600 : déclarée, non gardée.

**L'expérience à faire en premier** : D2′ et D1′-contrôles négatifs, sur processeur, avant tout épisode. Précisément : (1) écrire et sceller la clef de bris (64 bits, salée par cellule) et faire passer les trois contrôles négatifs de D2′, dont le vecteur de 9 600 ex æquo ; (2) faire passer au code de D1′ le contrôle « atome de 2 % à 98 % » ; (3) sceller le journal de fabrique (D-θ) et l'ordre entrelacé par graine. Les deux hypothèses opposées sont « la mise en œuvre du bris est correcte et le mesureur d'atomes voit un atome de queue » contre « l'un des deux échoue » ; dans le premier cas, le pilote peut partir et ses lectures ont un sens ; dans le second, aucune mesure du pilote sur les ex æquo ne vaudrait, et la banque telle que dimensionnée ne doit pas être lancée. Coût : secondes à minutes, zéro dollar, aucune tâche consommée, aucune lecture d'épreuve.

FIN-DE-CELLULE