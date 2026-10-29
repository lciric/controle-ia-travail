# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces reçues.** Les conceptions A et C sont présentes et complètes : chacune se termine par sa ligne de clôture. Les pièces C et D des faits sont des extraits, comme le dit leur en-tête. Je n'invente rien au-delà.

Conventions de statut :
- les chiffres de la pièce B gardent le statut RAPPORTÉ ;
- les propositions A et C sont des HYPOTHÈSES de conception ;
- les calculs que je fais sur des chiffres de B sont marqués « dérivé (B-cellule) » : l'arithmétique est la mienne et n'est pas auditée ;
- les autres chiffres sont marqués « illustratif ».

---

## Sur la proposition A

### (a) Défauts de méthode

**A-1. Vérité synthétique écrite avec les mêmes variables que le score (fuite construction → évaluation).** Les mondes étendus de A définissent le « pont conceptuel vrai » ainsi : champs différents, et « ≥ 2 opérateurs latents non-moyeux partagés ou 1 opérateur rare ». Le score d'O-paires vaut w_p = q_i q_j · c_ij^α · (1 − s_ij)^β, où c_ij est un recouvrement de concepts pondéré par la rareté.

Si le vecteur de concepts est une observation bruitée des opérateurs latents, le score est une fonction monotone et bruitée de la règle de vérité. E1 (α = 1 contre α = 0) mesurerait alors surtout le **bruit du canal d'observation**, pas l'utilité de la proximité conceptuelle. Le gain est acquis par construction dès que le bruit est faible.

La pièce B s'en protégeait en partie avec deux mécanismes de pont, greffes et jumeaux (B § 6, RAPPORTÉ). A n'en garde qu'un seul, qui est la traduction directe de son propre score.

**A-2. Le facteur de domaine est dominé par q au réglage par défaut.**
- Sur les cosinus de B, la paire « même champ » donne (1 − s) = 0,72 et la paire « champs différents » 0,97, soit un rapport de 1,35 à β = 1.
- Le produit q_i q_j, lui, varie jusqu'à un facteur 9 (B § 3 : q² varie d'un facteur 9).
- Pour que l'éloignement pèse autant que q, il faut β ≈ ln 9 / ln 1,35 ≈ 7 (dérivé, B-cellule).

Au réglage par défaut β = 1, O-paires répète donc, en plus atténué, le défaut que B § 3 a mis au jour : l'ordre suit q. Dans les mondes de B, q est indépendant de la vérité (B § 3, RAPPORTÉ). La pondération par q y est du bruit pur, et elle peut masquer l'effet de α dans E1.

**A-3. O-paires dégénère en tirage stratifié déterministe ; E2 confond deux facteurs.** Avec φ_p = [strate ; λ(e_i + e_j)], deux paires de strates différentes sans fiche commune ont ⟨φ_p, φ_q⟩ = 0. Pour γ → 0, le glouton prend donc la meilleure w_p de chaque strate. C'est un **argmax pondéré par strate**, sans tirage aléatoire.

E2 oppose ce glouton à un tirage indépendant ∝ w_p. Les deux bras diffèrent à la fois par la répulsion et par le passage de l'échantillonnage à l'argmax. Une issue de E2 ne peut pas être attribuée à la répulsion. Il manque un bras « argmax de w par strate, sans déterminant ». Le duel 3 de C contient ce bras (option 1b) : sur ce point, je me sers de C.

**A-4. E3 n'oppose pas deux hypothèses exclusives.** « La perte vient de l'ensemble de base » et « la perte vient de la platitude de cos² » peuvent être vraies ensemble.

De plus, l'issue dépend de la géométrie : avec 2 champs, 4 articles ne peuvent pas être tous dans des champs différents (B § 5 : 2 à 4 champs par monde). Un noyau tranchant sur articles produira donc des paires proches dans les mondes à 2 champs, quel que soit τ. E3 doit être stratifié par nombre de champs.

Enfin, τ est choisi sans jeu de réglage séparé. S'il est balayé sur les mondes de décision, c'est une fuite.

**A-5. Le test de séparabilité (E4) confond « capter le concept » et « être indépendant du domaine ».** Le critère « classifieur domaine-depuis-concepts ≤ hasard + 0,10 » rejetterait un extracteur parfait dès que les vrais concepts dépendent du domaine, ce que A reconnaît lui-même en A4.

Dans les mondes de B, ce critère est en plus fixé par construction : « 3 opérateurs latents par groupe, avec un mot de surface différent dans chaque domaine » (B § 5, RAPPORTÉ).
- Si le vecteur de concepts est fait des mots de surface, il prédit le domaine : échec par construction.
- S'il est fait des opérateurs latents, il prédit le groupe : le résultat dépend de ce que « groupe » recouvre dans `monde_v1.py`, qui n'est pas dans les pièces.

**A-6. E5 confond q et la promotion, et le jugement aveugle est impossible.**
- **Confusion par q.** O-paires pondère par q_i q_j. Le stratifié tire au hasard dans la strate (pièce A, `tirage_stratifie` : `rng.randrange`, VÉRIFIÉ). Si q provient du juge dans la course réelle, un gain de promotion peut venir de q seul. Cette confusion est fatale sans un bras stratifié pondéré par q ou une ablation q ≡ 1.
- **Vivier déjà sélectionné.** Les survivantes ont été sélectionnées par le même juge. La promotion des filles mesure la compatibilité avec ce juge, ce qui est voisin de la sélection sur le verdict (N-053).
- **Anonymat insuffisant.** Retirer l'identité du bras ne rend pas le juge aveugle : une fille issue de domaines éloignés se reconnaît à son contenu. Un a priori du juge pour ou contre l'interdisciplinaire suffit à créer l'écart.

**A-7. Témoin `b_eloigne` aux entrées non établies.** A le présente comme « deux lignes de code ». Or B le qualifie d'« a priori d'éloignement grossier » et d'« idéalisé » (B § 4, § 7.3, RAPPORTÉ), sans dire s'il lit les champs vrais ou observés. Qu'il n'utilise que des observables est une HYPOTHÈSE, à vérifier dans `methodes_v1.py` (`2f7a8b11…`) avant d'en faire un témoin. S'il lit la vérité de champ, il n'existe pas sur les fiches réelles et le seuil « ≥ b_eloigne − 2 » devient un plafond d'oracle.

**A-8. Intégrité.** L'énoncé « la différence [plafond 0,750 contre 0,322] vient du bruit d'observation, pas du tirage » est donné sans statut. C'est une HYPOTHÈSE.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Mesure ou critère de A | Condition sur les lois | Effet |
|---|---|---|
| Écart apparié de précision (E1, E2) | P(D_w = 0) → 1, où D_w est l'écart par monde : les deux variantes emboîtées tirent les mêmes 12 paires dans presque tous les mondes | Loi de D_w gonflée en zéro. Le bootstrap sur peu de mondes non nuls donne des intervalles instables. L'estimation de puissance de A (σ ≈ 15 points, dérivée de B) ne s'applique plus |
| Précision sur 12 paires | Le nombre de vrais ponts bisociatifs valides par monde descend vers 1 à 3 (illustratif) quand on exclut les ponts « de surface » intra-champ. B en compte 9,5 en « bien », RAPPORTÉ | Granularité de 1/12, plafond bas, majorité de mondes à précision nulle : l'écart n'est plus jugeable à 400 mondes |
| Facteur c_ij pondéré par la rareté | P(rare ∣ vrai pont) ≈ P(rare ∣ homonyme ou faux pont), c'est-à-dire une rareté indépendante du statut | Plus aucun pouvoir discriminant pour α. Dans les mondes de A, cette loi est fixée par le générateur, donc le résultat aussi |
| Rareté estimée sur le vivier | Vivier de 20 à 40 fiches : la fréquence documentaire d'une étiquette rare est 1 ou 2. Le passage de 1 à 2 change log(41/df) de 3,0 à 2,6 (dérivé, B-cellule) | Le poids d'une étiquette rare est dominé par le bruit d'échantillonnage du vivier |
| Facteur (1 − s)^β | Les cosinus des paires valides se concentrent entre 0,03 et 0,28 (B), alors que Var log(q_i q_j) ≫ Var β log(1 − s) | β inopérant (voir A-2) |
| E4, séparabilité | P(concept ∣ domaine) non uniforme dans la vérité | Le critère « ≤ hasard + 0,10 » rejette un bon extracteur. Non jugeable sans test conditionnel |
| E5, promotion | Avec 12 filles par bras et p ≈ 0,5, l'écart-type de la différence vaut ≈ 0,20, soit une demi-largeur à 95 % de ≈ 40 points (illustratif). Si p est proche de 0 ou de 1, c'est pire | Le seuil de +10 points n'est pas détectable. E5 ne peut falsifier ni H_A ni H_B |
| E5, contrôle de répétition | Bruit de fusion propre à chaque bras (hétéroscédastique) | Le bruit de fusion, mesuré sur le seul stratifié, ne borne pas celui d'O-paires |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Placebo de concepts qui conserve les marges.** A propose de permuter les vecteurs de concepts. Il faut que la permutation conserve la loi des fréquences d'étiquettes et l'**étage commun** (mêmes paires valides). Sinon l'ensemble candidat change et la comparaison n'est plus appariée.
2. **Monde à vérité découplée du score.** Les ponts vrais sont plantés par un mécanisme que c_ij ne recopie pas (par exemple un opérateur latent partagé observé par un canal calibré à part). On ajoute un monde où le recouvrement d'étiquettes est sans lien avec la vérité. Sans ces deux mondes, un succès de E1 reste un résultat vrai par construction (A-1).
3. **Ablation q ≡ 1** dans tous les bras, synthétiques et réels. Sans elle, E5 ne sépare pas « deux espaces » de « pondération par le juge » (A-6).
4. **Placebo de domaine.** On permute les vecteurs de domaine en gardant les strates, pour vérifier que β n'agit que par la vraie distance.
5. **Placebo d'éloignement dans E5.** On ajoute un bras de paires tirées uniformément sous contrainte d'avoir la même loi de distance de domaine qu'O-paires. Sans ce bras, l'a priori du juge sur l'interdisciplinaire n'est pas contrôlé.

---

## Sur la proposition C

### (a) Défauts de méthode

**C-1. Le facteur de volume de l'objectif retenu (option 1c) est plat : C reproduit le défaut qu'il a diagnostiqué.** Q_e contient √(1 − ⟨d_i, d_j⟩²).
- Aux cosinus de B, ce facteur vaut 0,960 (même champ, cos 0,28) et 0,9995 (champs différents, cos 0,03). L'écart est de 4 %.
- Dans la diagonale de K, qui porte Q_e², l'écart passe à 8 %.
- Pendant ce temps, q_i q_j varie jusqu'à un facteur 9, et la dérivée de 1 − x² est presque nulle autour de 0 (dérivé, B-cellule).

C écrit lui-même que « la dérivée de 1 − x⁴ en x → 0 est nulle ». Le même argument, en plus faible, s'applique à 1 − x². Prédiction falsifiable : dans 1c, ôter le facteur de volume ne change le tirage que dans une petite fraction des mondes. Tout gain viendrait alors de ⟨c_i, c_j⟩_IDF et de la répulsion par strates de S^paire. La conclusion du duel 2, « la combinaison des deux espaces », serait mal attribuée.

**C-2. La règle « ingrédient manquant » confond l'ingrédient et la forme sous laquelle il est mis en œuvre.** « Si (f) ne bat pas (b_eloigne), seul l'éloignement compte » ne suit pas, parce que (f) met l'éloignement en œuvre sous une forme presque inerte (C-1). (f) peut perdre contre b_eloigne par faiblesse de son terme de distance, même si la proximité conceptuelle aide.

Il faut un plan factoriel : distance oui/non × concept oui/non × répulsion oui/non, avec la **même forme fonctionnelle** pour chaque terme. A s'en approche avec ses deux réglages α et β : je me sers de A ici.

**C-3. Faux ponts définis pour que la pondération par la rareté gagne.** Les « ponts de surface » de C sont des termes génériques (« seuil », « moyenne », « régression »), donc fréquents. La pondération par la rareté les écarte par construction. B contenait des homonymes à 0,05 / 0,10 / 0,20 (B § 5, RAPPORTÉ). Rien n'impose, chez C, d'homonymes **rares**, c'est-à-dire le cas où la rareté et le statut de pont sont indépendants. Le monde de décision ne contient pas la condition qui ferait échouer (f).

**C-4. La vérité contient « champs différents ».** Les « partages intra-champ » sont classés comme piège. Tout terme de distance gagne donc par construction, comme dans B. C'est acceptable seulement si une condition à vérité inversée **pour les concepts** existe. C n'en a pas : son monde inversé ne retourne que la distance de domaine.

**C-5. Fuites de réglage.**
- Duel 1 : τ est balayé sur {1, 5, 10, 20} sur les mondes de décision, puis « le meilleur Node-DPP » est comparé. Le meilleur de quatre biaise la réfutation de H_A.
- Course 2, étage 1 : « le choix de l'extracteur […] se fait ici » sur le vivier même dont on mesure ensuite les propriétés géométriques. Construction et évaluation portent sur les mêmes fiches.

**C-6. Le juge de la pièce C n'est pas un instrument établi pour cet usage.** La pièce C est un « brouillon de conv-audit, non contre-lu, non servi » (en-tête des faits, VÉRIFIÉ). Ses points de déroulé portent « [à trancher par Lazar] ». Sa porte K3 est taillée pour la détection : « rappel à 1 % par famille ».

L'étage 3 de C fait de K1 à K5 le critère de promotion des filles. Le critère n'est donc pas jugeable tel quel. De plus, « peut invalider la porte K1 » ne correspond pas au texte de la pièce C, où K1 porte sur les livrables de l'axe.

**C-7. Plan de la course 2.**
- **Doublons.** Une paire tirée par les deux bras est « créditée aux deux bras ». Cela induit une corrélation positive et rapproche l'écart de 0, ce qui biaise contre la détection.
- **Lecture de log W.** log W est la « preuve en mémoire », cumulée sur des classes et des lignées (pièce A, en-tête v0.4, VÉRIFIÉ quant au texte). Le lire en sortie revient à lire des verdicts ultérieurs : c'est une sélection sur le verdict.
- **Confusion par q.** Elle est la même que chez A (A-6), puisque (f) porte (q_i q_j)^β.

**C-8. Intégrité des statuts (règle 1).** Plusieurs statuts sont gonflés ou mal attribués :
- « VÉRIFIÉ mathématiquement », « VÉRIFIÉ conceptuellement dans la littérature » (Koestler), « puissance > 0,99 (VÉRIFIÉ) », « 0,00 USD (VÉRIFIÉ) » : ces statuts ne sont pas admis pour des dérivations ou des estimations. Au mieux : HYPOTHÈSE ou démonstration à contre-lire.
- « VÉRIFIÉ dans le code (Pièce A, l. 182-194) » pour la dominance des paires proches : le code ne contient aucune densité. C'est B § 3, RAPPORTÉ.
- « Moyeux rares (5 %, Pièce B § 4) » : B § 4 donne une sensibilité aux moyeux à **0,10**.
- « Un changement d'une décimale contourne `signature_prediction` ; FPR 1,00 » : `signature_prediction` vient de `memoire`, absent des pièces. HYPOTHÈSE non signalée.
- « AUC 0,50 de `_domaine_estime` » : aucune source.
- Lehman & Stanley 2011 : C donne l'ordre « Stanley, Lehman », A l'ordre inverse. Référence à vérifier.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Mesure ou critère de C | Condition sur les lois | Effet |
|---|---|---|
| Puissance annoncée « > 0,99 » | Le critère réel est une borne inférieure de l'intervalle au-dessus d'un seuil, pas un test contre 0. Avec l'erreur-type de C (≈ 0,6 à 0,77), un effet vrai de +3 et une borne exigée > +1, la puissance est ≈ 0,74 à 0,82 (dérivé, B-cellule) | La puissance est surestimée |
| « Point ≥ +5 sur d1 », « ≥ +3 sur b_eloigne » | L'effet vrai est égal au seuil | Puissance ≈ 0,5 par construction. Le critère est aussi souvent faux qu'une pièce |
| Adoption « +12 et +6, bornes > +9 et > +4 » | b_eloigne fait déjà +11,9 / +6,6 (B, RAPPORTÉ). La règle « bat b_eloigne de +3 » exige donc ≈ +15 / +9,6 sur (b) (dérivé) | Seuil proche du plafond pratique. C cite la critique de B § 7.3 puis la reconduit |
| Monde inversé « chute ≤ −10 sur (c) » | Le score de (f) est presque constant en distance (C-1) | Le contrôle n'est pas informatif sur la distance. Il peut échouer pour une raison étrangère à la distance, ou passer grâce à la seule répulsion par strates |
| ⟨c_i ⊙ c_j⟩ normalisé dans Φ(e) | P(c_i ⊙ c_j = 0 ∣ paire valide) > 0, c'est-à-dire une étiquette d'opérateur partagée sans concept partagé | Division par zéro : noyau non défini sur ces paires. Leur traitement n'est pas spécifié |
| Séparabilité « r de Mantel < 0,10 », information mutuelle ajustée | Même confusion qu'en A-5. Les 780 paires d'une matrice de Mantel ne sont pas indépendantes | Le seuil fixe n'a pas de loi nulle. Il faut un test par permutation, sinon le critère n'est pas jugeable |
| Instrument 1, « FPR ≤ 0,05 » sur 50 négatifs | Même à 0 erreur sur 50, la borne supérieure à 95 % reste ≈ 0,06 à 0,07 (dérivé, B-cellule) | Le critère n'est pas certifiable à cette taille |
| Instrument 2, « AUC ≥ 0,92 » sur les mondes de B | Les cosinus y sont exacts et séparés (0,28 contre 0,03, B) | AUC ≈ 1 par construction. Ne valide rien hors synthèse |
| Course 2, +15 points ou Wilcoxon sur log W | 9 fusions par bras : demi-largeur ≈ ±46 points à p ≈ 0,5 (illustratif). log W est dépendant entre générations | Aucune des deux issues n'est falsifiable |
| Duel 3, contrôle m = 1 | Les deux formes prennent l'argmax de Q_e | Écart nul par construction. C'est un test d'implémentation, pas un contrôle négatif |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Placebo de concepts (absent chez C).** On permute les vecteurs c_i en conservant les fréquences et l'étage commun. Sans lui, aucun gain de (f) ne peut être attribué à l'espace des concepts. Tous les contrôles de C portent sur la distance de domaine.
2. **Monde à concepts inversés (absent chez C).** Les vrais ponts y relient des fiches conceptuellement éloignées qui partagent une étiquette de surface. On exige Δ_inversé − Δ_normal < 0, intervalle sous 0, comme B § 7.2 le recommande. A le prévoit : je m'en sers pour dire ce qui manque à C.
3. **Homonymes rares.** Il faut une condition où la rareté est indépendante du statut de pont. Sinon C-3 rend la victoire de la pondération par la rareté acquise par construction.
4. **Ablation du facteur de volume seul**, (f) sans √(1 − cos²). Sans elle, la part « deux espaces » n'est pas identifiée (C-1, C-2).
5. **Réglage sur des graines distinctes** pour τ (duel 1) et pour l'extracteur (course 2, étage 1).
6. **Témoins reproduits.** À réglages emboîtés, (b), (d1) et b_eloigne doivent retrouver dans les mondes étendus les chiffres de B à leur intervalle près. Sinon le générateur étendu a changé autre chose que ce qu'il prétend changer. A le demande, C ne le demande pas.
7. **Ablation q ≡ 1 et placebo d'éloignement** pour l'étage réel, mêmes raisons qu'en A-6.

---

## Deux vérifications communes, en inférence forte

Ces deux expériences tranchent des défauts partagés par A et C. Je ne fusionne pas les deux propositions : je teste chacune séparément.

**V1. Le terme de distance est-il opérant dans la forme proposée ?**
- **Protocole.** Pour chaque forme (O-paires de A à β = 1, option 1c de C), on mesure sur les 400 mondes « bien » la part π des mondes où ôter le terme de distance change au moins une des 12 paires.
- **H_A : le terme est opérant**, π ≥ 0,5 et écart de précision avec ou sans le terme dont l'intervalle exclut 0.
- **H_B : le terme est inerte**, π ≤ 0,1 et écart contenu dans [−1 ; +1] (seuils illustratifs).
- **Ce que chaque issue falsifie.** H_A réfute l'argument C-1 / A-2 pour cette forme. H_B impose de retirer « volume de domaine » des conclusions de la forme, et de passer à β élevé ou à un noyau tranchant avant tout test de l'ingrédient.

**V2. Le gain conceptuel survit-il à une vérité découplée ?**
- **Protocole.** Les mondes sont plantés par opérateur latent observé par un canal calibré à part. On y ajoute une condition placebo de concepts.
- **H_A : la proximité conceptuelle aide au-delà de la règle de construction.** Gain de α = 1 sur α = 0 (A) ou de (f) sur (f) sans facteur conceptuel (C), intervalle au-dessus de 0, et gain nul au placebo.
- **H_B : le gain observé dans les mondes de A ou de C reproduit la règle de vérité.** Gain nul dans le monde découplé, gain positif seulement quand la vérité recopie le score.
- **Ce que chaque issue falsifie.** H_A réfute l'objection de circularité (A-1, C-3). H_B réfute l'usage de ces mondes comme preuve de l'« ingrédient manquant ».

Ni V1 ni V2 ne demande d'appel de modèle : processeur seul, comme la pièce B.

FIN-DE-CELLULE