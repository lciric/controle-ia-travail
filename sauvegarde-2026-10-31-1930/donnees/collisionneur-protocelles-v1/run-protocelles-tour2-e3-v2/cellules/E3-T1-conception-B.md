# Proposition B — Tour III.1

## (a) Résolution des divergences non résolues

### a.1 Valeur de *n*

**Position : *n* ne peut pas être fixé avec les informations disponibles ; je retire mon choix n = 3 du tour 1.**

Mon choix n = 3 reposait sur l'idée qu'un lot de 6 fiches correspondait à 2n (deux filles de taille n après division binomiale). C'était une conjecture non étayée. La synthèse (section 2, ligne « Protocelle, n ») note que le contexte donne des lots de 6 (critère 8), mais que n dépend de la règle de division, non transmise. Pire, mon choix a alimenté I21 : j'ai lu U_c(3) dans la colonne n = 2 de la Table S1a (synthèse, section 9 : p. 42, l. 2880 vs l. 2884), et toute la chaîne de raisonnement en aval (q > 0,638, R > 1,57) est fausse. Cette erreur confirme que fixer n sans connaître la règle de division est dangereux pour les valeurs numériques qui en découlent.

**Ce qui trancherait** : l'audit du code de l'orchestrateur (section 8, étape (i)). La règle de formation des lots — combien de fiches entrent, combien en sortent, comment sont-elles réparties — fixe n et la règle de division ensemble. Sans ce code, choisir n = 3 ou n = 6 est une HYPOTHÈSE.

### a.2 Identité de *q* côté organisme

**Position : *q* n'est pas identifié sans choix préalable du noyau. Je maintiens ma position du tour 1, en la précisant.**

Dans le papier, q est la probabilité qu'une copie soit fidèle quand un catalyseur copie un modèle (synthèse, section 3 : p. 16, l. 1554–1557). Dans l'organisme, le bisociateur prend deux parents passifs, sans distinction catalyseur–modèle, et produit quelque chose qui n'est pas une copie au sens du papier mais une recombinaison. La définition de C — « probabilité qu'une paire vraie donne une fiche vraie » — est opérationnelle et mesurable, mais c'est un q_vv du noyau à deux parents (synthèse, section 3.1, point 3), pas le q du papier. L'appeler q sans avertissement importe les théorèmes du noyau à un modèle dans un noyau à deux parents. La synthèse (section 2, trait 1) confirme qu'aucune espèce ne tire la conséquence de ce changement de noyau sur les bornes.

**Ce qui trancherait** : (1) l'épreuve « trans contre cis » (section 12, question 1 ; P3) ; (2) si la stérilité de la fiche seule est confirmée, le q pertinent est q_vv, mesurable par type de paire (synthèse, section 3.1, point 3) après scellement. Le q du papier n'existe tout simplement pas dans l'organisme, et il faut l'admettre.

### a.3 Applicabilité à la pince et à l'arène

**(i) Pince.** Les théorèmes ne donnent pas de prédiction testable dans la pince telle que je comprends sa structure. Le levier r̄ du papier est une règle de division qui garde des paires de molécules ensemble (synthèse, section 5, réserve du lecteur : p. 68, l. 5013–5016) ; un juge qui promeut des fiches n'en est pas une par construction. C maintient une condition nécessaire (P9), mais elle repose sur une correspondance « population d'attaques d'un tour ↔ protocelle » que ni D ni moi n'acceptons (synthèse, section 2). Je ne vois pas quelle mesure trancherait cette divergence sans un modèle formel de la pince comme processus de branchement, ce qu'aucune espèce n'a fourni.

**(ii) Arène.** Le modèle est inapplicable dans tout régime adaptatif (le générateur s'adapte, les paramètres changent). Un régime à attaquant gelé rendrait q et θ stationnaires, mais la synthèse (section 5) note qu'aucun modèle de remplacement n'a été proposé, et les deux camps (B + D : inapplicable ; C : condition nécessaire) n'ont jamais convergé. Je maintiens que l'arène est hors de portée du papier.

### a.4 Extinction quadratique à fécondité infinie avec deux parents

**Position : l'extinction est plausible sous les conditions de C, mais pas démontrée au standard du papier. Je suis plus proche de D que de C.**

L'argument de C (synthèse, section 5 : « sans hybride fertile, naissances vraies en O(1/N²) par pas, ρ → 1/2, extinction à grande taille ») suppose que seules les paires vraie–vraie produisent du vrai (paires mixtes stériles) et une fécondité infinie (seule la suite des copies compte). La synthèse (section 5) rapporte que D juge l'extinction non démontrée sans la loi du taux d'événements.

Le nœud est le suivant. À fécondité infinie, le papier peut se permettre de ne compter que les événements de copie, puisque la mort intervient seulement à la division (synthèse, section 3 : p. 16, l. 1558). Mais avec deux parents, le taux de rencontres vraie–vraie dépend de la composition courante de la protocelle, pas seulement de la fréquence des réplicases. L'esquisse de la synthèse (section 3.1, point 3) montre que la densité de paires φ reste une surmartingale sous q_vv ≤ 1/2, mais cette esquisse est annotée « à contre-lire (R2) avant tout usage — jamais un résultat ». De plus, elle suppose un retrait indépendant du statut (synthèse, section 3.1, point 3 : condition omise par l'esquisse).

**Conditions pour que l'extinction tienne** : paires mixtes stériles (q_vf = q_ff = 0), retrait indépendant du statut, et l'esquisse contre-lue. **Conditions pour qu'elle tombe** : hybride fertile (q_vf > 0), ou retrait sélectif favorisant les fiches vraies (ce qui augmente φ après retrait d'une fausse), ou un taux d'événements qui dépend de la composition de façon à surcompenser la dilution quadratique.

### a.5 Source de la première mesure

**Position modifiée : expérience prospective (position de D) avec un préalable au processeur (audit du code). Je ne défends plus « nouveaux appels d'abord » de façon absolue.**

Mon choix du tour 1 pour de nouveaux appels venait de la crainte de biais dans les journaux existants. La synthèse (section 8) montre que l'audit du code de l'orchestrateur est un préalable à toute mesure : il fixe n, θ, la règle de division, et dit si un brouillon peut revenir au vivier. Cet audit est au processeur, sans dépense, sans journaux.

**Pourquoi pas les journaux d'abord** (position de C) : lire les journaux de la course 2 avant scellement expose au biais de confirmation. C-T3 propose de les lire « à 0 USD » comme première étape (synthèse, section 11.5) ; mais les prédictions ne sont pas scellées, et la course 2 a une puissance quasi nulle à trois lots par bras (synthèse, section 4, P6 ; section 8 (iii)). Le risque est de trouver un résultat non concluant et de recalibrer les seuils après coup.

**Pourquoi pas de nouveaux appels d'abord** (ma position du tour 1) : l'audit du code peut révéler que la correspondance est absente (par exemple, le bisociateur consomme les parents) ou que n et θ sont des paramètres d'ingénierie modifiables, rendant les appels existants suffisants. Dépenser avant de savoir est un gaspillage.

**Ordre** : (1) audit du code, (2) étalonnage au processeur, (3) préenregistrement scellé, (4) lecture des journaux seulement si les calculs de puissance montrent qu'ils sont jugeables, (5) runs prospectifs sinon.

### a.6 Destruction contre archivage

**Position modifiée : archiver hors du vivier, pas détruire.**

Ma position « perdu » du tour 1 était fondée sur le texte du papier (identité (i) : perdre une inachevée ne coûte rien sur la charge à fécondité infinie, synthèse, section 6 : p. 10, l. 863). Mais la synthèse (section 6) montre que détruire et archiver sont équivalents pour la dynamique, sous un même τ pour tous les modèles (p. 56, l. 4049–4052). Archiver garde la possibilité de mesurer θ′ et q_B sur épreuve séparée. Détruire perd cette mesure sans gain.

**Mesure qui trancherait la réinjection** : P4 (C) ou P5 (D), après étalonnage de l'estimateur spectral. Avant cela : audit du code pour savoir si un brouillon peut revenir au vivier, et si l'abandon dépend du statut des parents.

---

## (b) Politique consolidée sur les fusions inachevées

### b.1 Acceptation

**J'accepte la politique consolidée de la synthèse (section 6), avec une précision.**

La précision concerne la condition de réinjection. La synthèse dit « garde dans le vivier permise seulement si θ′ < 2(1 − τ) ». Le passage du papier (synthèse, section 6 : p. 59, l. 4286) porte sur le bain de copies lentes non re-tronquées. Mais la synthèse (section 6) corrige aussi la lecture de la p. 59 : le bain ne bat que la perte des seules copies lentes face à des copies rapides présentes (I12). Donc la réinjection n'a un domaine que si : (1) θ′ < 2(1 − τ), (2) il y a déjà des copies rapides dans le vivier, (3) pas de re-troncation. Si (2) n'est pas satisfait — et dans l'organisme on ne sait pas si des copies rapides existent —, le bain n'apporte rien de plus que l'archivage hors vivier.

**Référence** : synthèse, section 6 : p. 10, l. 863 (la perte ne coûte rien sur la charge à fécondité infinie) ; p. 56, identité (i) ; p. 59, l. 4278–4281 et I12 (comparateur mal lu par C).

### b.2 Testabilité avant lecture des journaux

**Les trois options sont testables au processeur et par runs prospectifs, sans lire les journaux de la course 2.**

- **Détruire** et **archiver hors vivier** : équivalents pour la dynamique (synthèse, section 6 : p. 56, l. 4043–4049). L'audit du code (section 8 (i)) tranche s'ils sont vraiment équivalents — c'est-à-dire si le critère d'abandon ne voit pas le contenu.
- **Garder dans le vivier sous condition** : testable par P4 (bain contrôlé à θ′ = 1,2 contre quarantaine, 40 lots par bras, synthèse, section 4) ou P5 (vivier contre quarantaine, synthèse, section 4). Les deux exigent des runs prospectifs (étape 4 de la section 8), pas les journaux.

La seule donnée des journaux qui pourrait être utile est le taux d'abandon par type de paire (pour vérifier si τ dépend du statut), mais elle n'est interprétable qu'après scellement et après avoir fixé n et la règle de division par l'audit du code.

### b.3 Origine de ma position

**Ma position du tour 1 venait du papier, pas du cadrage de la question.** Le passage décisif est l'identité (i) (synthèse, section 6 : p. 56, l. 4043–4049) : un arrêt est une boucle sur place, et le modèle est le modèle principal au débit R(1 − τ). Le fait que « la perte ne coûte rien sur la charge à fécondité infinie » (p. 10, l. 863) m'avait conduit à « perdu » comme défaut sûr. Ma modification vers « archiver » vient de la synthèse elle-même (section 6) : archiver garde la mesure sans changer la dynamique.

Cependant, je reconnais que la question (« t'es sûr ? ») et la conclusion du papier (p. 16, l. 1542–1543) orientaient le doute. La réserve R4 de la synthèse est fondée.

---

## (c) Prédictions à signer et ordre des travaux

### c.1 Tri des prédictions

| N° | Verdict | Raison |
|---|---|---|
| P1 | **(A) Abandonner** | Non signée (mesure invalidée, synthèse, section 4). De plus, sous ses conditions et à θ ≥ 1, la borne du prix l'implique déjà (section 4 : à R = 2, U_c ≤ ln(4/3) = 0,288 < 0,40). P1 est redondante et sans mesure. |
| P2 | **(F) À corriger** | Signée par C, mais le seuil 0,02 est illustratif et la dérive négative invoquée est un transfert de l'esquisse du §3.1, annotée « à contre-lire avant tout usage ». Corrections : (1) contre-lire l'esquisse (R2), (2) fixer le seuil après l'étalonnage de l'estimateur, (3) conditionner au résultat de l'audit du code (la mesure par type de paire exige de connaître la règle de tirage). |
| P3 | **(F) À corriger** | Ma version (B-T3 E-B2) n'est pas signée (seuil manquant). La version de D est signée par règle (δ fixé par le bruit de branchement simulé). Corrections : (1) fixer un seuil pour ma version ou adopter la règle de D, (2) reconnaître le coût (B-T3 disait « sans coût » ; synthèse, section 11.6 : elle demande des appels au bisociateur), (3) conditionner à l'audit du code (si le bisociateur consomme les parents, le bras « un parent » n'a pas de sens tel quel). |
| P4 | **(S) Signée**, conditionnelle à l'étape (i) et (ii) de la section 8 | Seuils illustratifs, mais la structure est complète : bain contrôlé vs quarantaine, noyau exact recalculé à n = 6 d'abord, estimateur étalonné. Prête pour le préenregistrement après les étapes au processeur. |
| P5 | **(S) Signée**, conditionnelle à l'étalonnage | Même structure que P4, estimateur étalonné par simulation. |
| P6 | **(A) Abandonner en l'état** | Ma propre prédiction. La synthèse (section 4) reconnaît la puissance nulle à trois lots par bras. Non jugeable sur la course 2. Si des runs prospectifs avec ≥ 6 à 10 lots par bras sont possibles, elle pourrait renaître, mais je n'ai pas fixé la taille d'effet. Abandon comme prédiction, conservation comme motif de conception des runs futurs. |
| P7 | **(S) Signée conditionnelle** | Bien structurée (ρ > 1 contre ρ ≤ 1, persistance sur horizon scellé). Conditionnelle à l'audit du code (pour séparer l'injection exogène) et à l'étalonnage de l'estimateur. |
| P8 | **(S) Signée conditionnelle** | Conditionnelle à la validation du noyau littéral avec θ = 1. Si le noyau est validé, q ≤ 1/2 ⇒ extinction est un théorème du papier (synthèse, section 9 : Théorème 2, p. 4, l. 355–358). Testable par P2 et P3 ensemble. |
| P9 | **(A) Abandonner** | Repose sur une correspondance que D et moi rejetons (section a.3 ci-dessus). La synthèse (section 5) note la réserve du lecteur sur le levier. Pas de consensus pour un préenregistrement. |
| P10 | **(S) Signée, asymétrique** | Certifier les boîtes de H2 est un calcul au processeur (arithmétique exacte). Un échec ne réfute pas H2. Prête. |
| P11 | **(A) Abandonner** | Ma propre prédiction, rendue qualitative en B-T3 après critique. Non signée, pas de métrique. |
| P12 | **(F) À corriger** | Signées mais hors papier (synthèse, section 4). Elles ne testent pas les théorèmes du papier. Les garder seulement si le tour 2 décide d'étendre le périmètre au-delà du papier. |

**Résumé** : 4 signées (P4, P5, P7, P10), 1 signée conditionnelle (P8), 3 à corriger (P2, P3, P12), 4 à abandonner (P1, P6, P9, P11).

### c.2 Ordre des travaux

**J'accepte l'ordre de la section 8 avec un ajustement.**

L'ajustement : l'étape (vi) — preuve écrite de l'esquisse du §3.1 et contre-lecture — doit précéder le préenregistrement (étape 2), car P2 et P8 en dépendent. Si l'esquisse est réfutée par la contre-lecture, P2 perd son ancrage théorique et passe de (F) à (A).

Ordre révisé :
1. Audit du code (étape (i) de la section 8).
2. Étalonnage de l'estimateur spectral (étape (ii)).
3. Calculs de puissance (étape (iii)).
4. Noyaux exacts aux petites tailles (étape (iv)).
5. Preuve de l'esquisse, contre-lue (étape (vi)).
6. **Certification H2** (étape (v)) — en parallèle de 4 et 5.
7. Préenregistrement scellé.
8. Lecture des journaux, seulement si les calculs de puissance la justifient.
9. Runs prospectifs sur devis.

### c.3 Préalables au processeur — recodage des noyaux

**Difficulté : modérée.**

Les formules sont dans le papier. Le noyau K = BH + 2^(1−2n) I est donné explicitement (synthèse, section 9 : p. 17, l. 1577–1586), avec les types f ≥ 2 et la recherche du rayon par Brent à 10⁻⁷. Les bornes à toute taille sont des formules fermées (synthèse, section 4 : p. 40, l. 2786–2789 ; p. 35, l. 2538–2541). La Table S1a est un contrôle.

Ce qui rend le recodage modéré plutôt que trivial : (1) le noyau exact à n = 6 et R = 1 à 4 avec la règle réelle de division (pas seulement la partition binomiale) exige de programmer la matrice de transition pour toute règle aveugle servie par le code ; (2) les bornes à fécondité finie à n = 6 ne figurent pas dans les tables du papier (synthèse, section 4 : n = 6 absent de la Table S2) ; (3) le noyau à deux parents (si l'esquisse tient) est à écrire de zéro, le papier ne le donnant pas.

Estimation de travail (illustratif) : quelques jours-personnes pour un développeur familier des processus de branchement multitype, si les formules du papier sont prises comme spécification. Le code du papier, s'il est obtenu de l'auteur, raccourcirait l'étape mais n'est pas indispensable.

### c.4 Impact des inexactitudes majeures

**I21 change le classement de P11 (de F à A), et aurait changé P1 si elle n'était pas déjà à A.**

- **I21** (ma lecture de U_c(3) = 0,450 au lieu de 0,644) : c'était le premier argument chiffré de non-allumage de B (synthèse, section 9). Toute la chaîne q > 0,638, R > 1,57 est fausse. Ma prédiction P11 (non-allumage « au sens du papier ») reposait en partie sur ces chiffres ; elle était déjà qualitative en B-T3, mais l'erreur sur le seuil la rend sans fondement quantitatif. Elle passe de « à corriger éventuellement » à « abandonner ».

- **I4** (ma loi d'échelle R_min ≈ 0,66 à n = 3) : même erreur en aval, extrapolation asymptotique hors domaine. Confirme l'abandon de P11.

- **I10** (C : R_min ≈ 1,32 à n = 6) : affecte P1 de C, mais P1 est déjà à (A) pour d'autres raisons.

- **I11** (C : condition nécessaire prise pour suffisante) : affecte P9 de C, mais P9 est déjà à (A) dans mon classement.

- **I12** (C : le bain bat le rejet) : affecte la justification de la réinjection dans P4, mais pas sa structure (P4 teste précisément cette question). P4 reste à (S).

**Aucune des quatre inexactitudes majeures ne fait passer une prédiction de (S) à (F) ou (A).** Elles confirment les abandons déjà décidés.

FIN-DE-CELLULE