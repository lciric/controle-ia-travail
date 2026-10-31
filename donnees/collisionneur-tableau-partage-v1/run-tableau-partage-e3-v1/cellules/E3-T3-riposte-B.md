# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Réponse critique par critique

Je traite chaque critique adressée à B par les propositions A, C et D. J'indique pour chacune : **acceptée**, **rejetée** (avec raison), ou **transformée en test**.

### Critiques de A

**A-1. La garde contre les instructions glissées est confondue avec sa mesure.**
**Acceptée.** A a raison : ma formulation du bloc 1 faisait de la recherche de la chaîne inerte à la fois la garde et l'évaluation. Le périmètre dit explicitement que la chaîne inerte sert de traceur, jamais de base pour la garde. La garde doit reposer sur autre chose (gabarit fermé, borne de taille, caviardage existant — fait 2) ; la chaîne inerte ne sert qu'à mesurer la prise en aval. Les taux de détection annoncés au livrable (c) étaient tautologiques. Je corrige en (b).

**A-2. « Évité » sans mesure pour le poids du plus prolifique.**
**Acceptée en partie.** La borne K borne la part du tableau, non la part des idées distinctes. J'avais omis la règle d'attribution quand une composante contient des fiches de plusieurs proposeurs. Je corrige : attribution fractionnaire (1/nombre d'auteurs dans la composante), et le « contrôle négatif » par tirage de l'ordre est remplacé par une condition sans tableau (même case, même proposeurs). Je maintiens que la borne K reste un mécanisme utile, mais « évité » est changé en « évité sous condition » : la mesure doit montrer qu'aucun proposeur ne dépasse 1/p + ε en part fractionnaire des idées distinctes.

**A-3. Contrôle inadapté pour la convergence : comparer au vide confond l'effet de toute lecture avec l'effet propre de l'écriture libre.**
**Acceptée.** Le contrôle négatif de la convergence doit être le tableau minimal (A), non l'absence de tableau. Je corrige en (b).

**A-4. Diversité par plongement : instrument non compté ; confusion titre/résumé et contenu du tableau.**
**Acceptée en partie.** Le modèle de plongement est un instrument à sceller : je l'ajoute au compte de code. La mesure sur titre + résumé mesure d'abord la recopie lexicale si c'est le même texte que celui échangé. **Transformée en test** : mesurer la diversité aussi sur le corps de la fiche (pas seulement titre + résumé), et comparer les deux ; si la diversité titre/résumé baisse mais la diversité du corps ne baisse pas, c'est une convergence de formulation, non d'idée.

**A-5. Sélection sur les fiches promues comprime les médianes.**
**Acceptée.** Conditionner sur la promotion tronque la distribution et favorise l'équivalence par construction. Je corrige : « qualité jugée égale » se mesure sur toutes les fiches validées, non sur les seules promues. La médiane porte sur l'ensemble des notes.

**A-6. Recommandation de C sans opérationnalisation de la mesure de prise dans C.**
**Acceptée.** Ma recommandation de C au bloc 4 exigeait un taux de prise = 0 dans C, mais je n'avais pas dit où une instruction glissée se plante dans une piste typée ni comment l'apparier à une piste honnête. Je corrige : le tiers plante des instructions glissées dans des pistes typées de même format (même type, même borne de taille), la chaîne inerte y est insérée, et l'appariement se fait par type et par taille.

**A-7. Réglage et évaluation non séparés.**
**Acceptée.** Je n'avais nommé aucune partition réglage/évaluation. Je corrige : les cas plantés sont séparés en deux familles disjointes (réglage et évaluation), gelées avant le pré-pilote. Les seuils sont fixés sur la famille de réglage ; les performances sont rapportées sur la famille d'évaluation. J'emprunte à D (en le disant) le principe de la séparation réglage/évaluation.

### Critiques de C

**C-1. Redéfinition du tableau complet en tableau intermédiaire.**
**Acceptée.** Le gabarit fermé, les types fermés et les bornes que j'imposais au « tableau complet » le rendaient identique à ma propre conception intermédiaire. Le vrai tableau complet est en lecture et écriture libres (fait 6). Je corrige le bloc 1 : le tableau complet est évalué sans gabarit fermé ni borne de type ; les protections sont le caviardage existant (fait 2), la borne de taille par entrée et par proposeur, et la séparation du juge. Le gabarit fermé et les types appartiennent à la conception intermédiaire.

**C-2. Fuite fatale entre évaluation et instrument sur les instructions glissées.**
**Acceptée.** Même critique qu'A-1, formulée plus précisément. Déjà corrigée ci-dessus.

**C-3. Incohérence des coûts de lecture entre conceptions.**
**Acceptée.** Les chiffres illustratifs du bloc 2 étaient arithmétiquement incohérents : la lecture des fiches entières (C) ne peut pas coûter moins que la lecture d'entrées courtes (B complet). Je corrige le tableau : C coûte plus cher en jetons lus que le tableau complet si les entrées du complet sont bornées ; si le complet est vraiment libre (correction C-1), son coût de lecture dépend du volume écrit et peut dépasser C. Les ordres de grandeur sont révisés en (b).

**C-4. Confusion entre sélection des fiches promues et qualité.**
**Acceptée.** Même critique qu'A-5. Déjà corrigée.

### Critiques de D

**D-1. Le « tableau complet » évalué n'est plus en lecture et écriture libres.**
**Acceptée.** Même critique que C-1. Déjà corrigée.

**D-2. « Poids : évité » ne suit pas de la borne mécanique.**
**Acceptée.** Même critique qu'A-2. Déjà corrigée.

**D-3. La garde est circulaire.**
**Acceptée.** Même critique qu'A-1 et C-2. Déjà corrigée.

**D-4. La qualité sur fiches promues est post-traitement.**
**Acceptée.** Déjà corrigée (A-5).

**D-5. Le duel des rôles se contredit : la supériorité des étiquettes sans consigne falsifie H_A même si le gain sur l'absence de rôle est réalisé.**
**Acceptée.** H_A doit exiger que les rôles assignés dépassent à la fois l'absence de rôle *et* les étiquettes sans consigne. Je corrige le duel 3.

**D-6. Aucun duel direct C contre B.**
**Transformée en test.** J'ajoute un duel C contre B au pré-pilote : H_A : C produit au moins autant d'idées distinctes par dollar que B, à qualité égale, avec un taux de prise ≤ celui de B. H_B : non.

**D-7. Les comptes de code ne sont pas des unités reproductibles.**
**Acceptée en partie.** Je définis l'unité : un élément est une fonction ou un fichier nouveau à sceller (empreinte propre). Le compte reste illustratif : il appartient au directeur de fixer la granularité.

**D-8. Partage placebo sans information croisée.**
**Acceptée.** J'ajoute ce contrôle : un contexte de même taille que le tableau, mais composé de chaînes inertes (sans information de passe 1), servi en passe 2. Cela isole l'effet du contenu de celui de la longueur du contexte.

---

## (b) Expériences corrigées

### Détecteur de doublons (corrigé)

Cas appariés : paires de fiches avec et sans doublon planté (même idée reformulée par le tiers), tirées de la famille d'évaluation (disjointe du réglage). Lecteurs à part : 2, avec un 3e arbitre sur les désaccords. Base à battre : recouvrement de trigrammes de caractères sur un échantillon *non préfiltré* (j'emprunte à D et A cette exigence). Contrôle négatif : paires de fiches de même case, même proposeur, idées différentes connues (non-doublons certifiés, distincts des paires inter-cases). Effectif minimal : ≥ 12 cas plantés en évaluation (illustratif). Seuils : détection ≥ 0,80, fausses alertes ≤ 0,10 sur la famille d'évaluation ; si la borne inférieure à 95 % de la détection est < 0,60 (illustratif, calculable par Clopper-Pearson), le détecteur est non jugeable.

### Garde contre les instructions glissées (corrigé)

**Garde** : gabarit fermé (intermédiaire) ou borne de taille (complet) + caviardage existant (fait 2). La chaîne inerte n'entre pas dans la garde.

**Mesure de la prise** : instructions glissées plantées par le tiers dans le tableau, portant chacune une chaîne inerte. La prise est mesurée en aval : la chaîne inerte est recherchée hors de sa place dans les fiches des autres proposeurs. Cas appariés : la même entrée honnête, avec et sans chaîne inerte, pour séparer recopie légitime de prise (j'emprunte à C ce contrôle, en le disant). Famille de réglage/évaluation : disjointes. Effectif minimal : ≥ 12 plantations en évaluation par conception (illustratif). Base à battre : la garde lexicale existante (fait 2) seule, sans borne de taille ni gabarit ; la prise est mesurée avec et sans garde. Borne supérieure à 95 % du taux de prise sur n = 12 : ≈ 3/12 = 0,25 (illustratif) si 0 prise observée. Cela ne garantit pas un taux vrai < 0,05 : je reconnais la limite (critique A, b) et note que le pré-pilote ne peut exclure qu'un taux vrai > 0,25, non un taux vrai > 0,05. Si le directeur exige une borne plus fine, l'effectif de plantations doit augmenter.

### Séparation d'avec le juge (corrigé)

Le tableau n'est jamais servi au juge (vérification de code, fait 2). Le filtre de recouvrement de n-grammes entre tableau et fiches servies au juge **exclut la correspondance d'une entrée du tableau avec la fiche dont elle est tirée** (correction du défaut transversal 1 de A, que j'accepte). Seuil de quarantaine : fixé sur la famille de réglage. Contrôle négatif : fiches honnêtes de passe 2 *sans tableau* soumises au même filtre, pour mesurer le taux de quarantaine de base (j'emprunte à A ce contrôle). Mesure de la reconnaissabilité des témoins : taux de reconnaissance (et non score moyen — j'accepte la critique de C sur ce point), comparé entre condition avec et sans tableau, sur les mêmes témoins. Effectif : avec n = 20 témoins par condition, la résolution est de 5 points (1/20) ; la marge d'équivalence réaliste est ± 10 points (illustratif), non ± 5 (ma version initiale) ni ± 2 (D). Je reconnais que même ± 10 points n'est concluable par TOST qu'avec un effectif nettement supérieur (critique C-b-4 et A-b) ; au pré-pilote, la mesure est descriptive et ne conclut pas à l'équivalence.

### Convergence (corrigé)

Contrôle négatif : le tableau minimal (A), non l'absence de tableau. Contrôle placebo : contexte de même taille, composé de chaînes inertes, pour isoler l'effet de la longueur du contexte (j'emprunte à D). Diversité mesurée sur le corps de la fiche, pas seulement sur titre + résumé (correction de A-4). H_A : la diversité médiane (corps) de la conception B ou C baisse de plus de δ par rapport à A. H_B : elle ne baisse pas. Unité : la case. Effectif minimal : ≥ 6 cases par condition (illustratif). Le modèle de plongement est compté comme un élément de code à sceller.

### Poids du plus prolifique (corrigé)

Attribution fractionnaire : si une composante contient des fiches de k proposeurs, chaque proposeur reçoit 1/k de l'idée. Part maximale d'un proposeur : mesurée par case, comparée entre conditions avec et sans tableau (minimal). Seuil : aucun proposeur ne dépasse 1/p + ε (illustratif : ε = 0,15) en part fractionnaire. Contrôle négatif : condition sans tableau (même case, même proposeurs). Statut : évité sous condition (la borne K borne le tableau ; la mesure vérifie que la part des idées est aussi bornée).

### Duels corrigés

**Duel 1 — B (complet, en lecture/écriture libre, borné en taille par entrée et par proposeur) vs A (minimal).**
H_A : à dépense égale par case, B produit plus d'idées distinctes que A, sans perte de qualité jugée (note médiane sur toutes les fiches validées, marge m illustratif = 0,5 point). H_B : B n'en produit pas plus, ou la qualité baisse au-delà de m. Contrôle négatif : cases avec contexte placebo (même taille, chaînes inertes). Unité : case. Dépendance intra-proposeur : les cas sont appariés par case ; analyse par test de rangs signés (Wilcoxon) sur les différences par case. Effectif : ≥ 6 cases par condition (illustratif). Falsifie H_A : différence d'idées distinctes ≤ 0 ou perte de qualité > m. Falsifie H_B : différence > 0 et qualité stable (marge m). Famille d'évaluation uniquement.

**Duel 2 — C (intermédiaire : fiches entières lisibles, écriture limitée à des pistes typées) vs A (minimal).**
H_A : C produit ≥ 1 idée distincte de plus par case que A (seuil illustratif), sans perte de qualité. H_B : non. Mêmes contrôles et mêmes analyses. Falsification symétrique.

**Duel 2bis (ajouté) — C vs B.**
H_A : C produit au moins autant d'idées distinctes par dollar que B, à qualité égale, avec un taux de prise (chaîne inerte) ≤ celui de B. H_B : non. Contrôle négatif : condition A. Ce duel est nécessaire pour justifier la recommandation de C plutôt que B (correction de A-6 et D-6).

**Duel 3 — Rôles (corrigé).**
H_A : rôles assignés par l'orchestrateur (condition i) produisent plus d'idées distinctes par dollar que sans rôle (condition ii) *et* que les étiquettes sans consigne (condition iii). H_B : non (condition i ≤ condition ii, ou condition i ≤ condition iii). Contrôle négatif : étiquettes sans consigne (condition iii). Métrique : idées distinctes / dollar, diversité (corps). Seuil : ratio ≥ 1,15 (illustratif). Anonymat : classifieur (n-grammes) en validation croisée par case et par proposeur (correction de D), avec permutation des étiquettes (j'emprunte à D) ; la borne supérieure de l'intervalle de son exactitude doit rester sous 1/3 + 0,15 (illustratif). HYPOTHÈSE : ces mesures tiennent lieu de l'oracle du monde planté (fait 13).

---

## (c) Réponse à la question de l'arbitre — ce qu'il faut rapporter au directeur

### Ce qui est établi

1. Le tableau minimal (A) est la décision du directeur (fait 5, RAPPORTÉ). Il suffit à réduire les doublons de passe 1 → passe 2 sans canal d'écriture inter-proposeurs, et son surcroît de code est le plus faible.
2. Le tableau complet en lecture et écriture libres (B) ouvre les trois écueils : influence croisée, instructions glissées, surcroît de code. Les critiques croisées ont montré que les protections que j'avais proposées (gabarit fermé, types fermés) transformaient B en un intermédiaire déguisé (C-1, D-1). Évalué sans ces restrictions, B reste exposé à la convergence et aux instructions glissées, et les mesures de prise disponibles au pré-pilote ne peuvent exclure qu'un taux vrai > 0,25 (sur 12 plantations).
3. La séparation du juge repose sur une vérification de code (le tableau n'est jamais servi au juge) et un filtre de recouvrement, qui doit exclure l'auto-correspondance entrée ↔ fiche source (défaut transversal 1 de A) et être étalonné sur un taux de quarantaine de base (fiches honnêtes sans tableau).

### Ce qui n'est pas établi (HYPOTHÈSE)

1. Que le choix de la conception du tableau échappe à la règle du fait 13 (porte sur le protocole, non sur la composition des proposeurs). Si ce n'est pas le cas, la qualité jugée ne peut pas entrer dans la comparaison des conceptions, et seuls les idées distinctes, la diversité et le coût décident.
2. Que le gabarit fermé ou la borne de taille suffisent à empêcher les instructions glissées dans l'intermédiaire (C). Le pré-pilote doit le mesurer.
3. Que les mesures d'idées distinctes, de diversité et de coût tiennent lieu de l'oracle du monde planté pour juger les rôles (fait 13).
4. Que la passe 2 sans tableau reçoit la même question sans voir ce qui est déjà écrit — cause rapportée des 12 doublons (fait 3) ; non mis à l'épreuve.

### Recommandation au format décision

**Décision :** quelle conception du tableau adopter pour la course 2. **Enjeu :** réduire les doublons (12/29 en course 1, RAPPORTÉ) tout en préservant la diversité et l'intégrité du jugement, et en permettant l'échange voulu par le directeur.

| Option | Avantage | Inconvénient |
|---|---|---|
| **(A) Minimal** (défaut) | Code léger ; aucun canal d'écriture inter-proposeurs ; pas d'instruction glissée possible par le tableau | Pas d'échange, pas de rôles via le tableau ; diversité dépend de la seule consigne |
| **(B) Complet** | Échange, rôles, idées ensemble possibles | Canal d'écriture libre ; prise non excluable sous 0,25 au pré-pilote réduit ; convergence à mesurer ; surcroît de code maximal |
| **(C) Intermédiaire** | Échange partiel (pistes typées) ; canal d'écriture contrôlé par gabarit ; lecture des fiches entières pour réduire les redites | Surcroît de code modéré ; la prise dans les pistes typées reste à mesurer ; ne permet pas l'écriture libre |

**Recommandation : (A) minimal, le défaut, jusqu'au pré-pilote. Confiance : moyenne.**

Raison : les critiques croisées ont montré que mes protections pour le complet le transformaient en intermédiaire, et que les effectifs du pré-pilote ne permettent pas de conclure à l'évitement des écueils avec une borne fine. Le défaut tient tant que le pré-pilote n'a pas mesuré les conditions ci-dessous. Si le pré-pilote confirme les trois conditions, la recommandation passe à (C) intermédiaire, conditionnelle.

### Mesures du pré-pilote par écueil (une ligne chacune)

- **Influence croisée :** diversité (corps) de C ≥ diversité de A − δ (illustratif : 0,10), mesurée sur ≥ 6 cases par condition, avec un contrôle placebo de même taille.
- **Instructions glissées :** taux de prise (chaîne inerte hors de sa place) dans C = 0 sur ≥ 12 plantations en évaluation (borne supérieure à 95 % ≈ 0,25 ; si le directeur exige une borne plus fine, augmenter l'effectif).
- **Surcroît de code :** liste close des fonctions/fichiers nouveaux à sceller, comparée au minimal ; le directeur accepte ou non le nombre.

### Expérience à faire en premier

Le taux de prise des instructions glissées plantées dans les pistes typées de la conception (C) au pré-pilote, mesuré par la chaîne inerte hors de sa place, avec la garde (gabarit + borne de taille + caviardage existant) activée. Si le taux de prise est > 0 sur la famille d'évaluation, revenir au minimal (A) ; s'il est 0, passer aux mesures de convergence et de séparation du juge.

FIN-DE-CELLULE