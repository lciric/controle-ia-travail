# Proposition B — Tour III.1

## Bloc 1 — Le tableau complet face aux trois écueils

### Écueil 1 : Influence croisée

**Convergence.**
*Mécanisme.* Un proposeur P₂ lit à la passe 2 les entrées du tableau (titres, résumés, pistes) écrites par P₁ à la passe 1. Le chemin : P₁ écrit → tableau → consigne passe 2 de P₂ → fiche de P₂. Sans cloisonnement, P₂ reformule ce qu'il a lu ; la diversité de la case baisse.
*Protocole.* Entrées du tableau à gabarit fermé (titre ≤ 15 mots, résumé ≤ 1 ligne, type pris dans une liste fermée), anonymisées par le noyau (identifiant d'auteur remplacé par un jeton opaque propre à chaque lecteur), taille bornée par proposeur (≤ K entrées, K fixé) et au total (≤ N entrées par case). Le noyau normalise la typographie et applique le caviardage existant (fait 2).
*Mesure.* Diversité intra-case (distance par paires, bloc 2) comparée entre condition « avec tableau » et condition « sans tableau » (même case, même proposeur, passe 2 seule). H_A : la diversité médiane baisse de plus de δ (illustratif : δ = 0,10 de la diversité sans tableau). H_B : elle ne baisse pas. Contrôle négatif : cases sans tableau dans le même pré-pilote. Effectif minimal : ≥ 4 cases par condition (illustratif). Si H_A non falsifiée, convergence non évitée.

**Poids du plus prolifique.**
*Mécanisme.* Un proposeur écrit plus d'entrées ; sa part du tableau excède sa part des proposeurs.
*Protocole.* Borne K par proposeur par case. Le noyau refuse toute entrée au-delà de K. Part maximale d'un proposeur = K / N.
*Mesure.* Fraction des idées distinctes attribuables (par le détecteur de doublons) à un seul proposeur, comparée entre conceptions. Seuil : aucun proposeur ne dépasse 1/p + ε (p proposeurs, ε illustratif = 0,15). Contrôle négatif : tirage au sort de l'ordre des entrées servies.

**Atteinte au juge.**
*Mécanisme.* Chemin : tableau → fiche (un proposeur recopie un fragment) → juge. Ou : tableau → consigne → juge (fuite de code). Second chemin : un témoin apparaît dans le tableau, un proposeur le cite, le juge le reconnaît.
*Protocole.* Le tableau n'est jamais servi au juge (séparation vérifiée par construction du code, comme l'anonymisation existante, fait 2). Les témoins sont exclus du tableau (comme de la mémoire du pôle, fait 7). Le noyau mesure le recouvrement de n-grammes entre le tableau et chaque fiche servie au juge ; au-dessus d'un seuil r (illustratif : r = 0,30 des trigrammes de caractères), quarantaine.
*Mesure.* (i) Chaîne inerte plantée dans une entrée du tableau ; recherche exacte dans les fiches servies aux juges. Taux de fuite attendu : 0. Contrôle négatif : chaîne inerte absente du tableau, vérifier qu'elle n'apparaît pas non plus. (ii) Reconnaissabilité des témoins : mêmes témoins servis à des juges figés de même configuration, avec et sans tableau ; taux de reconnaissance comparé. Seuil : la différence de taux ne dépasse pas ε_t (illustratif : 0,05). Contrôle négatif : condition sans tableau.

**Conclusion convergence :** évité sous condition (δ et effectif au pré-pilote). **Poids :** évité (borne K mécanique). **Atteinte au juge :** évité sous condition (mesure de fuite et reconnaissabilité des témoins au pré-pilote).

### Écueil 2 : Instructions glissées

*Mécanisme.* Chemin : proposeur P₁ écrit dans le tableau une entrée dont le texte agit comme consigne sur P₂ lorsque le noyau la sert en passe 2.
*Protocole.* Gabarit fermé (titre, résumé d'une ligne, type dans une liste fermée). Borne de taille par entrée (illustratif : ≤ 200 caractères). Caviardage du noyau (fait 2). Garde dédiée : le noyau plante des instructions glissées inertes (chaîne inerte unique, sans sens, plantée par un tiers, jamais rédigée par les proposeurs) à fréquence connue ; la garde mesure si la chaîne inerte apparaît hors de sa place (l'entrée du tableau où elle a été plantée). Le tableau est servi comme donnée, jamais comme consigne (spécification, fait 5).
*Mesure.* Instructions glissées plantées dans le tableau (illustratif : 2 par case). La chaîne inerte est recherchée dans les fiches rendues par les autres proposeurs. Taux de prise = occurrences hors de la place / nombre planté. H_A : taux de prise > 0. H_B : taux de prise = 0. Contrôle négatif : chaîne inerte non plantée, vérifier absence. Effectif minimal : ≥ 8 plantations par conception (illustratif). Garde à battre : la garde lexicale existante (fait 2) ou la borne de taille seule, sans chaîne inerte.

**Conclusion :** évité sous condition (taux de prise = 0 au pré-pilote ; sinon, le tableau complet est abandonné).

### Écueil 3 : Surcroît de code

*Mécanisme — chemins nouveaux.* Le tableau complet ajoute par rapport au noyau (fait 2) : (1) écriture du tableau par chaque proposeur (format, validation de gabarit, borne K), (2) lecture du tableau par chaque proposeur (anonymisation, filtrage des témoins), (3) garde contre instructions glissées (recherche de chaîne inerte, borne de taille par entrée), (4) mesure du recouvrement tableau-fiches (séparation du juge), (5) plantation d'instructions glissées inertes, (6) stockage et scellement du tableau.

*Ce qui se reprend.* La validation de gabarit et le caviardage existent (fait 2). L'exclusion des témoins et la liste blanche de champs existent dans la mémoire du pôle (fait 7). L'anonymisation existe (fait 2).

*Par rapport au tableau minimal.* Le tableau minimal (fait 5) requiert déjà : écriture (titres + résumés), lecture (servie en passe 2), anonymisation, séparation du juge, stockage. Éléments nouveaux du tableau complet par rapport au tableau minimal : (+) écriture libre (types supplémentaires, pistes), (+) garde contre instructions glissées (chaîne inerte + borne de taille), (+) mesure de recouvrement tableau-fiches, (+) plantation d'instructions glissées. Soit 4 éléments nouveaux.

**Conclusion :** évité sous condition — 4 éléments nouveaux à contre-lire et sceller par rapport au tableau minimal ; le directeur accepte ou non ce nombre.

---

## Bloc 2 — Trois conceptions sur un même estimand

**Estimand opérationnel.** *Idée distincte :* deux fiches portent la même idée si un lecteur à part (ni proposeur ni juge ; humain ou modèle distinct) juge leur paire « même idée », avec accord exigé entre deux lecteurs (κ ≥ 0,60 illustratif). On construit le graphe des paires (fait 4) ; les idées distinctes sont les composantes connexes. *Diversité :* distance cosinus moyenne par paires d'énoncés (titre + résumé), dans un espace de plongement fixé. *Dépense :* jetons lus + écrits, convertis en dollars au tarif du modèle. *Qualité jugée égale :* la note médiane des fiches promues ne diffère pas de plus de m (illustratif : m = 0,5 point sur l'échelle des juges) entre conceptions, vérifiée sur les témoins communs. Ce que cette comparaison sert à choisir : la conception du tableau, non les modèles proposeurs. HYPOTHÈSE : ce choix échappe à la règle du fait 13 parce qu'il porte sur le protocole, non sur « quels modèles, quel rôle, quelle part du budget ». Si cette hypothèse ne tient pas, la qualité jugée ne peut pas entrer et seuls les idées distinctes, la diversité et le coût décident.

| | (A) Minimal | (B) Complet | (C) Intermédiaire |
|---|---|---|---|
| Lecture passe 2 | Titres + résumés | Tout le tableau | Fiches entières + pistes courtes typées (≤ 200 car., type dans {prolongement, contradiction, lacune}) |
| Écriture | Aucune au-delà des fiches | Libre (borné K/proposeur) | Pistes typées uniquement |
| Échange, idées ensemble, rôles | Non | Oui | Partiel (pistes seulement) |
| Coût jetons lus (illustratif, passe 2, 4 proposeurs) | ~2 000 jetons/proposeur | ~8 000 | ~5 000 |
| Code nouveau vs noyau | ~3 éléments | ~7 éléments | ~5 éléments |
| Piège principal | Redites non évitées si résumé trop court | Instructions glissées, convergence | Écriture semi-libre reste un canal |

---

## Bloc 3 — Les rôles

HYPOTHÈSE : assigner des rôles (explorateur, critique, synthétiseur) augmente la diversité des idées distinctes. Le choix des rôles est un choix « dans quel rôle » (fait 13) : il ne se juge pas sur le verdict du juge.

*Chemin de transparence.* Consigne de rôle → proposeur → fiche. Si la fiche porte des marqueurs stylistiques du rôle, le juge pourrait désanonymiser. Le noyau normalise la typographie (fait 2) et caviarderait toute mention explicite du nom de rôle dans la fiche (ajout au lexique de caviardage).

*Mesure.* Trois conditions : (i) rôles assignés par l'orchestrateur ; (ii) sans rôle ; (iii) étiquettes de rôle sans consigne de conduite (contrôle négatif). Métrique : idées distinctes par dollar, diversité. Les témoins servent uniquement à vérifier que le juge reste étalonné entre conditions (taux de reconnaissance stable à ε_t près). HYPOTHÈSE : ces mesures (idées distinctes, diversité, coût) tiennent lieu de l'oracle du monde planté du fait 13, absent de la course. Vérification de l'anonymat : un classifieur (recouvrement de n-grammes) tente de prédire le rôle d'après la fiche ; si son taux dépasse le hasard (1/3 + illustratif 0,10), le caviardage est insuffisant.

---

## (a) Hypothèses non établies

1. La passe 2 reçoit la même question sans voir ce qui est déjà écrit — cause des 12 doublons. RAPPORTÉ, non mis à l'épreuve (fait 3).
2. Le choix de la conception du tableau échappe à la règle du fait 13 (porte sur le protocole, non sur la composition). HYPOTHÈSE.
3. Les mesures d'idées distinctes, diversité et coût tiennent lieu de l'oracle du monde planté pour juger les rôles. HYPOTHÈSE.
4. Le gabarit fermé et la borne de taille suffisent à empêcher les instructions glissées. HYPOTHÈSE.
5. Le recouvrement de n-grammes détecte la fuite tableau → juge. HYPOTHÈSE.
6. Deux lecteurs à part suffisent pour l'accord sur « même idée ». HYPOTHÈSE.

## (b) Expériences décisives

**Duel 1 — Tableau complet vs tableau minimal.**
H_A : à dépense égale par case, le tableau complet (B) produit plus d'idées distinctes que le minimal (A), sans perte de qualité jugée (marge m). H_B : il n'en produit pas plus, ou la qualité jugée baisse au-delà de m. Métrique : idées distinctes / dollar, diversité. Seuil : rapport ≥ 1,20 (illustratif). Unité d'analyse : la case. Contrôle négatif : cases sans tableau. Dépendance intra-proposeur : modèle mixte, proposeur en effet aléatoire. Falsifie H_A : rapport < 1,20 ou perte de qualité > m. Falsifie H_B : rapport ≥ 1,20 et qualité stable.

**Duel 2 — Tableau intermédiaire vs tableau minimal.**
H_A : (C) intermédiaire produit ≥ 1,15 fois les idées distinctes de (A) sans perte de qualité. H_B : non. Mêmes métriques, même contrôle. Falsification symétrique.

**Duel 3 — Rôles.**
H_A : rôles assignés (condition i) produisent plus d'idées distinctes par dollar que sans rôle (condition ii). H_B : non. Contrôle négatif : étiquettes sans consigne (condition iii). Métrique : idées distinctes / dollar. Seuil : rapport ≥ 1,15 (illustratif). Unité : case. Dépendance : même modèle mixte. Falsifie H_A : rapport < 1,15 ou condition iii ≥ condition i. Falsifie H_B : ratio ≥ 1,15 et condition i > condition iii.

## (c) Mesure minimale des instruments

**Détecteur de doublons.** Cas appariés : paires de fiches d'un même proposeur, passe 1 vs passe 2, avec et sans doublon planté (même idée reformulée par le tiers). Taux de détection ≥ 0,80 ; fausses alertes ≤ 0,10. Vérification mécanique à battre : recouvrement de trigrammes de caractères (seuil brut). Contrôle négatif : paires de fiches d'idées différentes connues. Le pré-pilote doit comprendre au minimum : 2 proposeurs, ≥ 4 cas plantés, 2 lecteurs à part.

**Garde contre les instructions glissées.** Cas appariés : entrées du tableau avec et sans chaîne inerte plantée par un tiers. Taux de détection de la chaîne inerte hors de sa place : ≥ 0,90 (si prise > 0). Fausses alertes (chaîne détectée alors qu'elle n'a pas été plantée) : ≤ 0,05. Base à battre : la garde lexicale existante (fait 2) ou la borne de taille seule, sans recherche de chaîne inerte. Contrôle négatif : entrées sans plantation. Minimum : ≥ 8 plantations (illustratif), 2 proposeurs.

**Séparation d'avec le juge.** Cas appariés : fiches servies au juge, avec et sans tableau dans la même case. Mesure : recherche exacte de la chaîne inerte du tableau dans les fiches servies au juge ; recouvrement de trigrammes entre tableau et fiches servies. Taux de fuite attendu : 0. Fausses alertes : recouvrement fortuit ≤ r (illustratif : 0,05). Base à battre : recherche exacte de la chaîne inerte. Contrôle négatif : cases sans tableau. Minimum : ≥ 4 cases avec tableau, mêmes témoins (illustratif).

## (d) Ancrage matériel

Coûts : voir bloc 2. Dépense par course (illustratif) : ~2 M jetons lus + écrits pour 4 proposeurs, 2 passes, ~30 fiches ; ~$15–40 selon modèle. Code à contre-lire : 3 éléments (A), 5 (C), 7 (B) au-delà du noyau. Aucun modèle ouvert requis.

---

## Bloc 4 — Ce qu'il faut rapporter au directeur

**Décision :** quelle conception du tableau adopter pour la course 2. **Enjeu :** réduire les doublons (12/29 en course 1) tout en préservant la diversité et l'intégrité du jugement.

| Option | Avantage | Inconvénient |
|---|---|---|
| (A) Tableau minimal (défaut) | Code léger (+3 éléments), pas d'instruction glissée possible | Pas d'échange ni de rôles ; diversité incertaine |
| (B) Tableau complet | Échange, rôles, idées ensemble | +4 éléments vs A ; instructions glissées à mesurer ; convergence possible |
| (C) Intermédiaire | Échange partiel, canal contrôlé | +2 éléments vs A ; canal réduit mais non nul |

**Recommandation : (C) intermédiaire, conditionnelle. Confiance : moyenne.** Le tableau complet offre ce que le directeur souhaite (échange, rôles), mais l'évitement des instructions glissées et de la convergence reste HYPOTHÈSE tant que le pré-pilote ne l'a pas mesuré. L'intermédiaire réduit le canal d'écriture libre tout en permettant les pistes. Si l'hypothèse ne tient pas (fait 13 englobe ce choix), seuls les idées distinctes et le coût décident, et la recommandation reste la même.

**Conditions par écueil :**
- Influence croisée : diversité condition C ≥ diversité condition A − δ au pré-pilote.
- Instructions glissées : taux de prise de la chaîne inerte = 0 dans C au pré-pilote.
- Surcroît de code : 2 éléments nouveaux vs A, acceptés par le directeur.

**Ce qui reste HYPOTHÈSE :** (i) le choix du tableau échappe au fait 13 ; (ii) le gabarit fermé suffit contre les instructions glissées ; (iii) les mesures d'idées distinctes et diversité tiennent lieu de l'oracle du monde planté pour les rôles. Le pré-pilote doit mesurer en premier le taux de prise des instructions glissées plantées dans la conception C : s'il est > 0, revenir au tableau minimal (A).

FIN-DE-CELLULE