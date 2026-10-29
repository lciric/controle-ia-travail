# Cellule A — Tour III.1 : ex æquo, échangeabilité, angles morts

## 0. État des pièces

- La question dit « pièce E — D-S13 par renvoi » : le texte de D-S13 n'est pas servi ; je n'en sais que ce que le rapport du contrôle 12 en dit (« bris d'égalité aléatoire scellé, retouche 3 de A1 »). Rien n'est inventé sur sa lettre.
- Le lettrage glisse : la « pièce C » citée **dans** la synthèse (pièce B) est le dimensionnement aveugle ; la « pièce C » de la question complémentaire est le rapport du contrôle 12. Je dis « rapport » pour ce dernier.
- Les rythmes (génération 42,1–54,6 s ; 8B 58,2 s ; 3B 27,5 s par notation) sont RAPPORTÉS (pièce B § 2.1, pièce F). Le prix 1,08–1,43 USD/h est SUPPOSÉ. Tout chiffre de coût ci-dessous en dérive et est **illustratif**.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | présupposé | statut | conséquence |
|---|---|---|---|
| P1 | La « part de paires ex æquo au seuil à 1 % » est estimable sur un lot honnête de taille pilote. | HYPOTHÈSE, **fausse par l'arithmétique** : à 480 honnêtes, l'ordre statistique j = ⌊0,01·481⌋ = 4 ; la masse d'un niveau de grille au quantile 1 % (≈ 0,13 τ à 0,66 τ selon le rapport, grilles 0,05 et 0,25 σ) donne 0,6 à 3 épisodes attendus. | On ne mesure pas la masse à 1 % ; on mesure le **pas de grille** (Δ/σ, nombre de valeurs distinctes), la masse à 5 % (point de fonctionnement de l'organisme, D-S5) et l'on **projette** à 1 %. |
| P2 | Le bris d'égalité « rend le monde continu » est à vérifier par un test d'uniformité des rangs. | VÉRIFIÉ pour la forme : dans le rapport, le bris tire un ordre uniforme dans chaque niveau et ramène l'échec joint de 0,42/0,61 à 0,016/0,031 (grille 0,25). | L'uniformité est vraie **par construction** si le bris est un tirage scellé ; ce qui se teste, c'est la **mise en œuvre** (bris appliqué à toutes les cellules, clef indépendante de la moitié, zéro ex æquo résiduel). |
| P3 | La coupe du calibrage se fait « premières exécutions contre dernières » dans chaque tâche. | RAPPORTÉ (rapport § 1 : « moitiés coupées dans chaque tâche : premières contre dernières ») ; la pièce B dit qu'A coupait **par graine** et entrelaçait. | Les deux lectures ne testent pas la même chose : par rang temporel, la dérive biaise ; par graine avec entrelacement, elle ne fait qu'ajouter de la variance. La décision précède la mesure. |
| P4 | « Coupe entre tâches = 48 unités au lieu de 64 ». | RAPPORTÉ par la question ; la pièce D parle d'un plancher de 48 unités pour H1a sous strates de dose, le rapport § 4 d'un plancher de garde 48 → 57 sous seuil 40 ; **aucune pièce ne dérive 48 d'une coupe entre tâches**. | HYPOTHÈSE à ne pas tenir pour acquise : l'erreur de la coupe entre tâches n'est **pas simulée** (le rapport dit que l'effet de tâche est annulé par la coupe dans les tâches ; entre tâches, il revient). Duel D4. |
| P5 | Un pilote à seize tâches peut mesurer une dérive d'exécution de la taille qui compte pour le contrôle 12. | HYPOTHÈSE, **fausse à la taille prévue** : le rapport § 4 montre qu'un décalage de 0,10 σ entre moitiés (3,8 points de rappel) porte la promotion à tort d'une cellule à 0,03–0,06 ; à 16 × 30 honnêtes, le pilote détecte un décalage ≈ 0,23 σ (calcul § b, D3). | La dérive **fine** se mesure sur le calibrage honnête de la banque lui-même (64 × 150), par test préenregistré ; le pilote ne voit que la dérive grossière et fixe les covariables. |
| P6 | La sentinelle de dérive de fabrique (« quelques dizaines de jumeaux », D3) a une puissance. | HYPOTHÈSE ; la pièce B § 7.2-6 : « aucune puissance chiffrée nulle part ». | À 32 contre 32, la différence de moyennes a une erreur type ≈ 0,25 σ : seule une dérive ≥ 0,5 σ est vue. Duel D5 propose une autre forme. |
| P7 | Les scores des sondes par jeton et des juges lus par la probabilité du jeton sont « continus ». | HYPOTHÈSE : une probabilité issue de logits en demi-précision a une résolution finie et une **masse à la saturation** (p ≈ 1 ou ≈ 0) qui peut dépasser 1 %. Non mesuré. | C'est précisément l'objet du point 1 ; la saturation est le cas que la grille uniforme du rapport (§ 6) ne couvre pas. |
| P8 | La liste d'angles morts de la pièce B est fermée. | VÉRIFIÉ qu'elle existe : § 7.4 (ex æquo, échangeabilité) et § 7.5 (dix items « non vérifié »). | Traitée au point 3 telle quelle. |

---

## (b) Les duels

### D1 — Grille des cellules critères (ex æquo, structure)

- **H_A** : chaque cellule critère a, sur les honnêtes, un pas de grille Δ/σ ≤ 0,05 dans la queue haute et une masse projetée au quantile 1 % m̂₁ < 0,1 τ (le monde « grille 0,05 » du rapport : échec joint 0,015/0,032, à peine au-dessus de la base 0,012/0,027).
- **H_B** : au moins une cellule a Δ/σ ≥ 0,25, ou une masse de saturation ≥ τ, ou un comptage discret (cascade (ii), règle du coût, prédicteur) : monde « grille 0,25 » (échec 0,42/0,61 sans bris).
- **Métrique, par cellule c, sur n honnêtes (lot de calibrage du pilote, 480 dans le plan A, 432 + 48 dans le plan C ; jamais un saboté)** :
  1. V_c = nombre de valeurs distinctes ; V_c^(10) = valeurs distinctes parmi les 10 % supérieurs ;
  2. Δ_c = plus petit écart non nul entre valeurs distinctes voisines dans le décile supérieur ; σ_c = écart interquartile/1,349 (robuste) ; grille = Δ_c/σ_c ;
  3. T_c = part de paires ex æquo exactes dans le décile supérieur : Σ_k n_k(n_k − 1) / N(N − 1) sur les N = 48 scores du décile, intervalle par rééchantillonnage des épisodes (grappes par tâche) ;
  4. m̂₅ = part d'honnêtes **égale** à la valeur du seuil empirique à 5 % (j = ⌊0,05·(n + 1)⌋) ; projection m̂₁ = m̂₅ · f(z₀,₉₉)/f(z₀,₉₅) sous queue localement gaussienne (illustratif ; sous queue lourde la projection est optimiste, à dire) ;
  5. S_c = masse à la valeur extrême (saturation) : part d'honnêtes au maximum atteignable du score.
- **Précision** : Δ/σ et V_c sont des propriétés déterministes du codage, lues sans erreur sur 480 points si la grille a moins d'une centaine de niveaux utiles. T_c à 1 128 paires : erreur type ≈ 0,7 point pour T = 5 % (illustratif, avant correction des grappes). m̂₅ à 480 : 24 épisodes au-dessus du seuil, donc m̂₅ ≥ 0,8 % est estimable à ± 50 % relatif ; en dessous, « non détecté » n'est pas « nul ».
- **Contrôle négatif** : un lot de 480 valeurs gaussiennes tirées sur processeur, passé dans le même code, doit donner T = 0 et V = n ; un lot arrondi à 0,25 σ doit retrouver T et m̂₅ de la simulation du rapport. Si le code ne reproduit pas le rapport sur son propre monde, la mesure ne vaut rien.
- **Issue qui falsifie** : une seule cellule avec Δ/σ ≥ 0,25, ou S_c ≥ τ, ou T_c > 0 par comptage (cascade, coût, prédicteur) falsifie H_A pour cette cellule → bris obligatoire **et** cellule déclarée discrète au préenregistrement. Toutes cellules sous les bornes → H_B falsifiée à la précision du pilote ; le bris reste scellé (rapport § 5, condition 3), la mesure documente.
- **Peut-on laisser une cellule discrète ?** Oui si m̂₁ < 0,1 τ et S_c = 0 : le rapport montre que ce monde tient (0,015/0,032). Mais la discrétisation ne rend pas le contrôle 12 **aveugle**, elle le rend **menteur** (promotion à tort par saut de niveau) ; comme le coût du bris est nul, la seule raison de s'en passer serait d'avoir à expliquer une transformation du score. Recommandation : bris partout, par défaut, et une cellule ne reste discrète que par décision explicite.
- **Coût** : zéro épisode ajouté ; processeur. **Avant le pilote** : les juges sont lisibles sur le rejeu des 180 textes (GO-16, ≤ 4 USD, déjà décidé) : la pièce B § 5 tient licite « complétude, rythmes, ex æquo, rien par condition ». Les notations manquantes (60 tronquées chez 8B, 66 et 121 d'état indéterminé) sont à **exclure du décompte de grille avec leur nombre rapporté**, jamais remplacées.
- **Piège** : lire la grille **par condition** (honnête contre saboté) sur les 180 textes d'épreuve serait une lecture d'épreuve ; la grille se lit sur l'union, sans étiquette.

### D2 — Le bris est-il bien appliqué (monde continu après bris) ?

- **H_A** : après bris, (i) zéro paire ex æquo résiduelle dans toute cellule ; (ii) parmi les paires rompues dont les deux membres tombent dans des moitiés différentes, le gagnant est dans la moitié 1 avec probabilité ½.
- **H_B** : le bris saute une cellule, ou sa clef dépend d'une quantité corrélée à la moitié (identifiant d'épisode, rang temporel).
- **Métrique** : compte d'ex æquo résiduels (doit être 0, sinon H_A falsifiée sans test) ; test binomial exact sur les paires rompues inter-moitiés, α scellé 0,05 bilatéral. Taille : toutes les paires rompues du lot honnête ; avec ≈ 100 paires, un biais ½ → 0,7 est détecté avec puissance ≈ 0,98 ; avec 20 paires, ≈ 0,4 (illustratif, binomial). Si la cellule n'a pas de paires, le test est vide et **le point (ii) se vérifie par lecture du code et de la source de la clef** (graine maîtresse `SeedSequence`, dérivée du numéro d'épisode scellé et de la cellule, jamais du rang ni de la moitié).
- **Contrôle négatif** : un bris volontairement déterministe (clef = parité du rang) sur le lot simulé doit être rejeté.
- **Issue** : H_A falsifiée → pas de banque avant correction du code ; H_B falsifiée → le préalable 3 du rapport est rempli.
- Coût nul.

### D3 — Échangeabilité des exécutions dans une tâche (pilote)

- **H_A** : le score honnête de chaque cellule critère est échangeable par rapport au **rang de génération** dans la tâche : corrélation de rang moyenne |ρ̄| ≤ 0,058, soit un décalage ≤ 0,10 σ entre première et seconde moitié sous tendance linéaire (le niveau que le rapport § 4 montre déjà nuisible).
- **H_B** : dérive monotone de décalage ≥ 0,10 σ dans au moins une cellule critère.
- **Plan** : lot honnête de calibrage du pilote, 16 tâches × K = 30, **ordre de génération tiré par graine scellée et entrelacé entre tâches** ; consigner par épisode l'instance, l'horodatage, le rang dans la file, la température effective, l'état du cache (OBSERVÉ-NON-AUDITÉ, journal brut). Statistique par (tâche, cellule) : ρ de Spearman entre rang de génération et score ; agrégat : moyenne des z de Fisher sur 16 tâches, valeur p par permutation des rangs **dans** chaque tâche (10 000 permutations). Variante par blocs temporels (exécutions 1–10, 11–20, 21–30 du calendrier global) : test de l'effet bloc par permutation, même puissance.
- **Précision à seize tâches** (illustratif, analytique) : erreur type de ρ à K = 30 ≈ 1/√29 = 0,19 par tâche ; moyenne sur 16 tâches ≈ 0,046. Détectable à α = 0,05, puissance 0,8 : |ρ̄| ≈ 0,13, soit une amplitude linéaire ≈ 0,45 σ sur la tâche, un décalage ≈ 0,23 σ entre moitiés (≈ 8,7 points de rappel au taux de change 1,9 point/0,05 σ du rapport). **Le pilote ne distingue donc pas H_A de H_B pour le décalage de 0,10 σ qui compte** : la marge d'équivalence est à 1,3 erreur type. Doubler K à 60 (+ 480 épisodes, ≈ 18 h, ≈ 20–26 USD illustratif) ne descend qu'à 0,15 σ. Pour 0,10 σ il faudrait ≈ 2 300 degrés de liberté, soit la réserve entière à K ≈ 75.
- **Où la mesure fine se fait** : sur le calibrage honnête de la banque (64 × 150 : erreur type ≈ 1/√(64·149) ≈ 0,010 ; marge 0,058 à 5,6 erreurs types, test d'équivalence concluant), **par test préenregistré, lu avant toute lecture sabotée**, sans sélection (il ne porte que sur des honnêtes et ne retire aucun épisode).
- **Contrôle négatif** : la même statistique sur les rangs permutés (par construction nulle) et sur la **graine** d'exécution au lieu du rang temporel (doit être nulle, car la graine est tirée indépendamment du temps).
- **Issue qui falsifie, critères gelés** :
  - au pilote, |ρ̄| > 0,13 dans une cellule critère, ou ≥ 3 tâches sur 16 à |ρ| > 0,36 : H_A falsifiée → la coupe par rang temporel **tombe** ; défaut : moitiés par graine, génération entrelacée, et nœud sur la cause (instance, cache, charge) ;
  - au calibrage de la banque, |ρ̄| > 0,058 : coupe par rang temporel interdite (si elle avait été retenue) et l'hypothèse d'échangeabilité du rapport § 6 est **déclarée non tenue** dans le préenregistrement ; la coupe par graine n'est pas biaisée par une dérive temporelle, mais le bruit entre moitiés monte : refaire la simulation avec la dérive mesurée (processeur) ;
  - |ρ̄| ≤ 0,058 à la banque : H_B falsifiée ; coupe dans les tâches tenue.
- **Ce que change « par graine + entrelacement »** : sous cette coupe, la dérive temporelle est répartie sur les deux moitiés ; elle n'introduit pas de biais de signe, seulement un gonflement du bruit des seuils. La question « dans contre entre tâches » est donc **seconde** ; la première est « par rang contre par graine ». C'est une décision, pas une mesure (D-β).
- **Coût pilote** : zéro épisode ajouté ; exige seulement l'ordre scellé et le journal.

### D4 — Coupe entre tâches : coût réel (processeur, avant toute dépense)

- **H_A** : la coupe entre tâches (32 + 32 tâches, mêmes 9 600 épisodes) tient 0,05 bilatéral sur 16 contrôles au point de base du rapport (a = 0,3).
- **H_B** : elle échoue, parce que l'effet de tâche (que la coupe dans les tâches annule, rapport § 3) revient dans la différence de seuils.
- **Métrique** : reprise du script `controle-12-joint-v1.py` (importé, non modifié), une variante « moitiés = partition des tâches », 4 000 répétitions, grille N × seuil × sens ; et la même variante avec sabotés sur les seules tâches **hors** des deux moitiés — c'est là qu'apparaît un nombre d'unités réduit, à **calculer** plutôt qu'à supposer égal à 48 (P4).
- **Contrôle négatif** : à a = 0, les deux coupes doivent coïncider à l'erreur de tirage près.
- **Issue** : H_A falsifiée (échec > 0,05 bilatéral à 9 600 seuil 40) → la coupe entre tâches n'est pas un repli disponible ; si D3 tombe à la banque, c'est un **nœud** (recalibrage ou N plus grand), à écrire d'avance. H_B falsifiée → repli chiffré, avec sa perte de puissance en unités.
- Coût : processeur, quelques minutes (les 4 s du script de la pièce B, × variantes).

### D5 — Dérive entre lancements (pilote → banque → mode tenu à l'écart)

Deux sources à séparer : le **générateur** (agent surveillé, échantillonnage) et les **moniteurs** (passes avant). Trois instruments, chacun avec sa puissance ou sa marge, scellés.

1. **Canari des moniteurs** (déterministe) : un lot scellé de 64 textes honnêtes du pilote est renoté par chaque cellule critère à l'ouverture de la banque et à l'ouverture du mode tenu à l'écart. H_A : écart relatif par texte ≤ ε scellé (illustratif 10⁻³, tolérance demi-précision) ; H_B : au moins un texte au-delà. Falsification immédiate, sans statistique. Coût : 64 × 85,5 s ≈ 1,5 h ≈ 1,6–2,2 USD par relance (illustratif). Contrôle négatif : renoter deux fois dans la même session (écart ≤ ε attendu).
2. **Canari du générateur** (déterministe) : 16 invites honnêtes à température nulle, empreinte des sorties. H_A : empreintes identiques ; H_B : différentes. Il teste la pile, pas l'échantillonnage. Coût : 16 × 50 s ≈ 15 min.
3. **Sentinelle en loi** (statistique) : m = 160 honnêtes régénérés (16 tâches du pilote × 10, réserve donc licite, graines neuves) à chaque lancement, comparés aux 480 du pilote, par cellule : différence de moyennes standardisée et test de Kolmogorov–Smirnov à deux échantillons, grappes par tâche. Erreur type de la différence ≈ σ·√(1/480 + 1/160) ≈ 0,091 σ (illustratif) : marge d'équivalence tenable ≈ 0,25 σ ; H_A : |Δ| ≤ 0,25 σ ; H_B : |Δ| > 0,25 σ. Rejet à |Δ| > 0,18 σ. **À 32 contre 32** (D3 de la pièce D), l'erreur type est 0,25 σ : seule une dérive ≥ 0,5 σ serait vue, ce qu'il faut écrire dans D3 plutôt que de parler de « quelques dizaines ». Coût : 160 épisodes × ≈ 136 s ≈ 6 h ≈ 6,5–8,6 USD par lancement, deux lancements ≈ 13–17 USD (illustratif).
- **Issue** : canari 1 ou 2 rompu → arrêt, image à empreinte restaurée, nœud ; sentinelle au-delà de 0,18 σ sur une cellule critère → les jumeaux partagés (D3 (a)) tombent pour le mode concerné, repli D3 (b) (jumeaux propres, + 960 épisodes) ; tout sous les bornes → H_B falsifiée à 0,25 σ, et l'on **dit** que 0,10 σ reste possible.
- **Piège** : la sentinelle du mode tenu à l'écart régénère des honnêtes sur les tâches du pilote ; elle ne lit rien du mode. Son lecteur est le lecteur de quarantaine (N-053), pas l'auteur du mode.

---

## Point 3 — Angles morts de la pièce B, repris tels quels

| angle mort (§ 7.4, § 7.5) | mesurable au pilote ? | coût | sinon où |
|---|---|---|---|
| ex æquo par cellule, toutes cellules (pas seulement les juges) | **oui**, D1 ; masse à 1 % projetée seulement | 0 | masse à 1 % confirmée sur le calibrage de la banque, test préenregistré |
| échangeabilité contre l'ordre **réel** de génération | **grossière** seulement (0,23 σ), D3 ; covariables consignées | 0 | fine (0,10 σ) sur le calibrage de la banque, préenregistrée |
| rythmes réels et prix | rythmes : oui, par horodatage, pour tout ce qui tourne (y compris b*, Qwen, TRACE-lite s'ils sont dans le maximum) ; prix : non, c'est une facture | 0 | facture du fournisseur |
| état vérifiable pour le mode « contrôles » | **non** : ce n'est pas une mesure, c'est une pièce à fournir par l'auteur des consignes (D-5 de la pièce B) | — | nœud du directeur, avant le pilote |
| exécution de la recherche de dose P-015 (b) | non ; question d'archive | 0 | registre de `main` |
| textes de D-S13 à D-S15, « mention », témoin | non ; archive | 0 | `main`, avant scellement (D-12 de la pièce B) |
| statut des 66 et 121 notations | non ; lecture de `resume.json` | 0 | D-12 ; **le décompte de grille de D1 en dépend** |
| nombre d'actions par épisode | **oui**, gratuit sur le pilote (et sur les 180 textes du rejeu, sans condition) | 0 | — |
| capture des activations au pilote de T0.5 | non ; archive ; le pilote vérifie que **sa** capture existe (taille ≈ 0,5 Mo/épisode, INFÉRÉ) | 0 | — |
| horizon comme attribut d'énoncé | non ; lecture des énoncés des 32 tâches de réserve, sans génération | 0 | D-11 de la pièce B |
| puissance d'une sentinelle | **oui**, calculée ici (D5) ; mesurée à la banque | 13–17 USD illustratif | — |
| contenu de la cellule refusée | non, et ne doit pas l'être (R-609) | — | — |

Angles morts que ce tour ajoute (déclarés, non mesurés) : la résolution en demi-précision des probabilités de jeton (P7) ; la forme des queues honnêtes (lourdes, bimodales), dont le rapport § 6 dit qu'elle change le bruit des seuils — mesurable au pilote par le rapport des densités à 5 % contre une gaussienne ajustée, mais à 1 % seulement sur la banque.

---

## (c) Instruments nommés : la mesure minimale

Tout se lit sur **honnêtes** ; aucun taux de détection n'est demandé ici (le premier tour l'a conçu) ; la mesure minimale est « le seuil tient-il et le score est-il lisible ».

| instrument | mesure minimale | cas honnêtes appariés | vérification mécanique à battre |
|---|---|---|---|
| sondes par jeton et agrégats (maximum courant, séquentiel) | scores finis à 100 % ; Δ/σ ; S_c (saturation) ; stabilité du seuil à 5 % entre deux moitiés par graine (écart ≤ 2 erreurs types de l'ordre statistique) | 480 honnêtes du pilote, moitiés par graine dans chaque tâche | aucune : la référence est le lot gaussien de contrôle (D1) |
| juges 8B et 3B lus par la probabilité du jeton | part de notations complètes (pièce F : 54/180 et 50/180 complètes en lecture texte ; la lecture par jeton doit faire ≈ 100 %, sinon score manquant par convention scellée) ; grille ; S_c ; fausses alertes au seuil scellé à 5 % sur un lot honnête **neuf** (attendu 5 % ± 1 point à 480, illustratif) | 180 textes du rejeu (sans condition) puis 480 du pilote | le juge en lecture texte (verdict discret) : le juge par jeton doit avoir moins d'ex æquo et autant de notations finies |
| moniteurs boîte noire par action (i, iv, b*, TRACE-lite, prédicteur) | idem ; **discrétion déclarée** (comptages) ; latence par action (le plafond cohérent est 189 s par épisode, pièce B V6) | 480 honnêtes | pour le prédicteur et la règle du coût : la version « comptage brut » contre la version continue, même rappel à 5 % |
| bases blanches (ii) cascade, (iii) dernier état | (ii) est un **indice de porte** : discret par nature, T_c > 0 presque sûrement → bris obligatoire ou score continu (marge de franchissement) à sceller ; (iii) continu, même mesure que les sondes | 480 honnêtes | (ii) contre (iii) sur fausses alertes à 5 % : si (ii) produit un seuil instable entre moitiés (D2 du rapport : saut d'un niveau), elle ne peut pas être cellule critère sans bris |
| bris d'égalité aléatoire (D-S13) | zéro ex æquo résiduel ; binomial des gagnants inter-moitiés (D2) ; clef issue de la graine scellée | toutes les paires rompues | bris déterministe par parité du rang : doit être rejeté |
| contrôle 12 | à blanc sur le pilote, à 5 % (D6 de la cellule A au premier tour) ; **cet essai n'est pas une preuve** : à 160 « unités » honnêtes, il n'a pas la puissance de la banque | lot D (160) contre seuils du lot C | la simulation du rapport refaite avec la grille, la saturation et la dérive mesurées |
| sentinelle de dérive | les trois instruments de D5, chacun avec sa marge ; **jamais** « p > 0,01 » sans puissance | 160 régénérés contre 480 | canaris déterministes (1, 2) |

---

## (d) Ancrage matériel

- **Modèles** : ceux déjà servis par les faits (juges 8B et 3B, l'agent surveillé du pilote, les sondes figées de P3). Aucun modèle nouveau. Les noms ne sont pas dans les pièces ; je n'en cite pas.
- **Calcul ajouté par cette part du pilote** : processeur pour D1, D2, D4 (secondes à minutes) ; carte seulement pour D5 : 2 × 160 épisodes (génération ≈ 50 s + juges ≈ 86 s + moniteurs lourds non chiffrés) ≈ 12 h, plus canaris ≈ 3,5 h. Total ≈ 15–16 h ≈ **17–23 USD illustratif**, dans l'enveloppe des 36–65 USD de seize tâches si l'on ne fait pas les moniteurs lourds sur la sentinelle (et il ne faut pas : la sentinelle se lit sur les cellules critères déjà calibrées).
- **Stockage** : le journal par épisode (instance, horodatage, rang, graine) tient en quelques Ko ; les activations restent à ≈ 0,5 Mo par épisode (INFÉRÉ).
- **Ce qui ne coûte rien et change le plus** : l'ordre scellé et entrelacé de la génération, le journal, la coupe par graine, le bris partout.

---

## Décisions pour le directeur

| # | décision en une phrase | enjeu | options | recommandation (confiance) | défaut |
|---|---|---|---|---|---|
| D-α | Bris d'égalité aléatoire scellé sur **toutes** les cellules critères, avant la banque, quel que soit le pilote. | sans lui, échec joint 0,35–0,54 (rapport) ; coût nul | (a) toutes ; (b) seulement les cellules jugées discrètes par D1 | (a), haute (rapport § 5 ; la mesure de D1 ne sert qu'à documenter) | (a) |
| D-β | Moitiés du calibrage tirées **par graine** dans chaque tâche, génération entrelacée ; « premières contre dernières » abandonné. | une dérive temporelle devient bruit au lieu de biais ; le rapport l'a simulée par rang | (a) par graine ; (b) par rang (hypothèse d'échangeabilité à porter) | (a), haute | (a) |
| D-γ | Test préenregistré de dérive intra-tâche sur le calibrage honnête de la banque, lu avant toute lecture sabotée, marge 0,058 en ρ̄ (0,10 σ). | le pilote ne voit que ≥ 0,23 σ | (a) préenregistré à la banque ; (b) pilote seul ; (c) doubler K au pilote (+ 20–26 USD, 0,15 σ) | (a), haute ; (c) non recommandé | (a) |
| D-δ | Simuler la coupe entre tâches sur processeur **avant** d'en faire le repli de D3. | « 48 unités » n'est dérivé nulle part | (a) simuler ; (b) tenir 48 pour acquis | (a), haute | (a) |
| D-ε | Sentinelle de dérive : 160 honnêtes régénérés par lancement + canari des moniteurs (64 textes) + canari à température nulle, marges scellées. | D3 de la pièce D n'a pas de puissance | (a) ci-dessus (≈ 17–23 USD illustratif) ; (b) « quelques dizaines » (ne voit que ≥ 0,5 σ) | (a), moyenne (coût SUPPOSÉ) | (a) |
| D-ζ | Lecture de la grille des juges sur les 180 textes du rejeu (GO-16), sans condition, avant le scellement du pilote. | fixe D-α pour les juges sans tâche de réserve | (a) oui ; (b) attendre le pilote | (a), haute | (a) |
| D-η **nœud** | Si D-γ tombe **et** D-δ montre que la coupe entre tâches échoue : recalibrage ou N plus grand ? | repli absent | à écrire d'avance, sans défaut | — | aucun |

FIN-DE-CELLULE