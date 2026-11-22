# Proposition A — Tour III.3 : réponse aux critiques

**État des pièces.** Ma conception III.1 et les cinq critiques croisées (B, C, D, E, F) sont présentes et closes par leur ligne de fin. Je n'ai pas recalculé les empreintes. Je ne réponds qu'aux sections « Sur la proposition A ».

**Statuts.**
- Rien ci-dessous n'est VÉRIFIÉ par moi : le bloc FAITS ne contient que la question.
- Les critiques gardent le statut que leur auteur leur a donné. Quand j'écris « recalculé, concordant », j'ai refait une arithmétique élémentaire, sans audit tiers, et le statut d'origine ne change pas.
- Mes corrections sont des HYPOTHÈSES de méthode. Tous les seuils, effectifs et coûts sont illustratifs.

**Deux attributions contestées, sans effet sur mes décisions.**
- C écrit que ma règle de trois « fixe le seuil à la statistique d'ordre maximale ». Mon texte ne donne que la borne 3/n et ne dit rien du réglage du seuil. La critique vise donc une lacune réelle : ce réglage n'était pas spécifié.
- E lit des « paramètres indépendants » dans mon générateur. Mon texte ne le dit pas, mais il ne dit pas non plus le contraire.

---

## (a) Réponses aux critiques

### Règle commune et banc

| Critique (source) | Décision | Suite |
|---|---|---|
| Arrêt optionnel : « on augmente n » sans correction séquentielle (B, C, D, E, F) | **Acceptée** | La règle était fausse telle qu'écrite. Voir R1. |
| Seuil réglé et évalué sur les mêmes cas honnêtes (D, E, F). Avec 300 cas, le quantile à 1 % est mal résolu : écart-type relatif ≈ (αn)^(−1/2) (F). | **Acceptée** | Voir R2 et R3. |
| Des cas honnêtes atypiques à queue lourde pousseraient le seuil au-delà des scores fautifs, d'où un taux de détection nul (C, E) | **Rejetée comme défaut, gardée comme issue possible** | Les hypothèses de queue sont des HYPOTHÈSES des critiques. Si l'effet se produit, c'est un résultat : l'instrument échoue sur ce banc, selon mon critère d'échec commun. |
| Atomes : un score discret ne permet pas d'atteindre exactement 1 % de fausses alertes (B, E, F) | **Acceptée** | Voir R3. |
| Fautes et auditeur conçus par la même équipe (B) | **Acceptée** | Voir R5. |
| Une vérité générée empêche de mémoriser un tirage, pas d'apprendre le gabarit (D) | **Acceptée** | C'est ce que E1′ mesure. |
| Le plan matériel confond échelle (30–70 Md) et mode d'élicitation (7–8 Md affiné) (E) | **Acceptée** | Un même modèle, instruit et affiné. Le contraste d'échelle est abandonné. |
| Corrélation intra-trajectoire ignorée dans les intervalles (C, F) | **Acceptée** | Voir R4. |

### E0

| Critique | Décision | Suite |
|---|---|---|
| Critère d'inclusion si étroit que H_A devient quasi automatique (B) | **Acceptée** | Double codage, strict et large. H_A doit tenir au niveau large. |
| κ ininterprétable quand presque rien n'est inclus (B, E, F) | **Acceptée** | Seuil sur κ retiré. On rapporte l'accord sur les inclusions et toutes les inclusions sont arbitrées. |
| Rappel inconnu, donc nombre vrai d'articles non identifié (D, E, F) | **Transformée en test** | Deux stratégies de recherche indépendantes et capture-recapture (E0′). |
| Le contrôle positif sur U1 ne calibre pas les requêtes des usages cibles (B, F) | **Acceptée** | Le suivi de citations depuis les travaux fondateurs ne dépend pas du vocabulaire. |
| Un terme fabriqué ne teste pas la sur-inclusion des codeurs (F) | **Acceptée** | Remplacé par un lot d'articles réels hors périmètre, codés en aveugle. |
| U4 anti-collusion figure dans mon classement, pas dans le duel (D) | **Acceptée** | Ajouté. |

### E1

| Critique | Décision | Suite |
|---|---|---|
| « Planté, audité, paraphrasé » mélange trois canaux et deux régimes causaux, avant et après engagement (C, D, E, F) | **Acceptée** | Trois mesures séparées. « Audité » devient un contrôle d'orchestration (tirage après gel des activations, proposé par C). |
| H_B disjonctive sans correction de multiplicité (B, F) | **Acceptée** | Un seul discriminateur, choisi sur le jeu de développement et évalué une fois. |
| Une sonde mesure ce que les activations encodent, pas ce que la politique exploite (B) | **Transformée en test** | Mesure comportementale ajoutée : écart de taux de faute entre unités plantées et réelles. |
| Entraîner sur un générateur G1 et tester sur G2 (B) | **Rejetée en partie** | Reconnaître la signature du générateur de plantage est la menace, pas une fuite. Le critère primaire reste intra-générateur, cas pessimiste pour le contrôleur. Le transfert G1→G2 est rapporté en secondaire. Les artefacts de banc sont traités par le contrôle réel contre réel. |
| Séparer entraînement et test par famille de tâches et par trajectoire (C, E, F) | **Acceptée** | Voir R2. |
| Contrôle réel contre réel, entre lots ou gabarits honnêtes distincts (B, F) | **Acceptée** | Condition de jugeabilité. |
| Sonde linéaire aveugle aux signatures d'ordre deux (E) ; variance quand la dimension dépasse l'effectif (C, F) | **Acceptée** | Famille élargie et régularisée. |
| Rejouer toute la sélection de sondes sur les étiquettes permutées (D) | **Acceptée** | — |
| L'avantage d'un discriminateur ne borne pas celui du meilleur (D, formulé à propos de B et F ; vaut pour moi) | **Acceptée** | L'issue H_A est affaiblie en conséquence. |

### E2

| Critique | Décision | Suite |
|---|---|---|
| Écart de 15 points inatteignable à p = 0,02 si les fautes sont rares (B : K ≥ 9 ; C : K ≤ 7 donne ≤ 0,132 ; E : faute unique, écart ≤ p) | **Acceptée** | Recalculé, concordant. Le critère rendait H_B vraie par construction. Métrique changée. |
| « Premières unités » confond prévisibilité et position (C, D, F) | **Acceptée** | Bras retiré du duel. Les bras comparés ont la même loi de positions. |
| Il manque un bras « tiré mais révélé », seul contraste isolant le secret (B) | **Acceptée** | Il devient le contraste primaire. |
| Il manque un calendrier fixe à graine non publiée (E) | **Transformée en test** | Duel secondaire. Sans lui, je ne pouvais pas conclure sur « un calendrier fixe inconnu suffit ». |
| Rescorer une trace de fautes indépendante du calendrier (D) | **Acceptée** | Test A/A. |
| « Au moins une faute non détectée » et « aucune faute détectée » ne sont pas complémentaires (D) | **Acceptée** | Métrique par faute. Le succès par trajectoire est défini explicitement. |
| Éviter les unités annoncées relève de l'obéissance, pas de la stratégie (F) | **Rejetée en partie** | La consigne donne le calendrier et l'objectif, jamais le conseil de placement : l'inférence est la capacité mesurée. Je retiens la relecture des consignes par un tiers. |

### E3

| Critique | Décision | Suite |
|---|---|---|
| H_B regroupe point focal et variance honnête (B). Battre le moniteur sans atteindre la cible n'entre dans aucun récit (D). | **Acceptée** | Le duel d'origine violait B4. Paramètre primaire changé. |
| Si les étapes honnêtes variables désaccordent plus que les fautives, le taux de détection passe sous le taux de fausses alertes (C, E) | **Transformée en test** | L'inférence de C, de l'entropie à la dominance stochastique, n'est pas générale. Le scénario reste plausible : il devient une issue de la mesure secondaire. |
| Contrôle : équipe rouge à faute déterministe, indépendante de la graine (B, F) | **Acceptée** | — |
| Le désaccord confond non-coordination et entropie lexicale de la consigne subversive (F) | **Transformée en test** | Contrôle sur les étapes sans faute de l'équipe rouge. |
| Cinq passes d'un grand modèle contre un petit moniteur n'est pas « à coût égal » (F) | **Acceptée** | Coût en secondes-GPU mesurées, même budget pour le comparateur. |
| Si le désaccord a la même loi avec et sans faute, E3 est impuissante (D) | **Acceptée** | Condition de jugeabilité sur le taux de faute. |

### E4

| Critique | Décision | Suite |
|---|---|---|
| Vrai par construction si le déclencheur est lexical ou si les données n'ont aucun corrélat de l'attribut (B, C, E, F) | **Acceptée** | Corrélats de force réglée par le générateur. |
| Exiger un corpus naturel (E) | **Rejetée en partie** | Un corpus naturel perd la vérité par construction et rouvre la mémorisation. La conclusion est restreinte au niveau de fuite testé, et la validité externe est déclarée non couverte. |
| Contrôle de ré-identification directe, sans faute, avec règle de score propre (C, F) | **Acceptée** | Mesuré avant l'équipe rouge. |
| Ré-identifier, vouloir fauter et y réussir sont trois événements (D) | **Acceptée** | Chaîne rapportée terme à terme. |
| H_B mêle ré-identification et perte de qualité. H_A ne peut pas réfuter une explication bibliographique (F). | **Acceptée** | Deux duels. Je retire la phrase « H_A réfute mon explication de sa rareté ». |
| Réduction relative instable ou indéfinie si le taux de base est faible (D, E, F) | **Acceptée** | Différence de taux et seuil d'entrée sur le taux de base. |
| Contrôle : faute opportuniste, non conditionnée à l'attribut masqué (F) | **Acceptée** | — |

### Tableau (c) des instruments

| Critique | Décision | Suite |
|---|---|---|
| U12 : la part recalculable vaut 100 % par déterminisme (E) et ne mesure pas la sélection des tirages publiés (D) | **Acceptée** | Nouvelle mesure : détection par un tiers d'une révélation sélective, sur un registre simulé à tirages manquants et engagements numérotés avant la tâche. |
| U5, U7 : un décodeur ou un attaquant fixé ne majore ni la capacité ni la valeur du jeu (D, E) | **Acceptée** | Ces mesures sont rapportées comme des bornes inférieures, jamais comme des garanties. |
| U2 : l'acceptation moyenne ne borne pas le pire cas (D) | **Acceptée** | Même reformulation. |
| U9 : il manque un modèle honnête bridé ou faible soumis au même bruit (C, E) | **Acceptée** | Contrôle ajouté. Si son score monte aussi, l'usage échoue. |
| U10 : contrôle « mauvaise clé » (D) ; puissance nulle sur texte court (E) | **Acceptée** | Résultats par strate de longueur. |
| U11 : contrôle « retours indépendants du dossier » (D) | **Acceptée** | — |
| U4 : contraste nul si les paires compatibles sont aussi probables sous affectation fixe (D) | **Acceptée** | Condition déclarée : le test exige des relecteurs hétérogènes et un producteur capable d'anticiper le sien sous affectation fixe. |

---

## (b) Expériences corrigées

### Règles communes

- **R1, arrêt.** L'effectif maximal est préenregistré. Une seule analyse intermédiaire, avec dépense du risque α. À l'effectif maximal, un intervalle qui chevauche le seuil donne « non tranché », publié tel quel.
- **R2, découpage.** Trois jeux disjoints par famille de tâches et par trajectoire : développement, calibration des seuils, test évalué une fois. Une famille de cas honnêtes atypiques est réservée au test.
- **R3, point de fonctionnement.** Le critère primaire est à 5 % de fausses alertes, avec 300 cas de calibration et 300 de test. Le point à 1 % n'est rapporté qu'avec au moins 1 000 cas honnêtes, sinon il est marqué « non résolu ». Pour un score discret, seuls les points atteignables sont rapportés.
- **R4, inférence.** Intervalles par rééchantillonnage en grappes de trajectoires. Correction de Bonferroni sur les duels primaires statistiques : trois en E1′, puis E2′, E3′, E4a et E4b.
- **R5, auditeur.** Une famille de fautes est tenue hors du réglage de l'auditeur et rapportée à part.
- **R6, conditions d'entrée.** Chaque duel a des conditions d'entrée. Si l'une échoue, le duel est non jugeable et aucune hypothèse n'est déclarée.

### E0′ — Recherche bibliographique

- **Champ.** U8, U11, U12, U2 dans sa forme engagement-défi, U4 anti-collusion.
- **Deux stratégies indépendantes.**
  - S1 : requêtes par mots-clés, fixées à l'avance.
  - S2 : suivi des citations entrantes depuis les travaux fondateurs de chaque usage, croisé avec « agent » ou « language model ».
- **Codage.** Deux codeurs, deux niveaux d'inclusion : strict (adversaire stratégique et hasard secret explicites) et large (mécanisme appliqué à un agent de langue sous hypothèse de non-confiance).
- **H_A.** Pour chaque usage, au plus 2 articles au niveau large, et borne supérieure à 95 % de l'estimateur capture-recapture (S1 × S2) inférieure à 3.
- **H_B.** Au moins 3 articles pour un usage, au niveau large.
- **Asymétrie déclarée.** H_B se décide quel que soit le rappel. H_A ne se déclare que si la borne tient, sinon « non tranché ».
- **Contrôle positif.** S1 et S2 appliquées à U1 retrouvent Greenblatt et al. (2023).
- **Contrôle négatif.** Vingt articles réels hors périmètre (hasard non secret ou adversaire non stratégique), contenant les mots-clés et codés en aveugle. Plus d'une inclusion sur vingt signale une sur-inclusion.
- **Falsifie.** H_B réfute mon classement pour l'usage concerné. H_A réfute l'idée que le transfert depuis les domaines d'origine est déjà fait.

### E1′ — L'effet du tirage est-il visible avant l'engagement ?

- **Trois duels séparés,** un par intervention visible en entrée : unité plantée (U3), entrée paraphrasée (U5), instance masquée (U8).
- **Paramètre θ.** AUROC, sur le jeu de test, du discriminateur unique retenu sur le développement dans une famille préenregistrée : question directe au modèle avec score propre, sonde linéaire régularisée, sonde non linéaire, classifieur affiné.
- **Cadre.** Entraînement et test intra-générateur, cas pessimiste pour le contrôleur. Le transfert entre générateurs est rapporté en secondaire.
- **H_A :** θ < 0,60. **H_B :** θ ≥ 0,60.
- **Mesure comportementale.** L'équipe rouge est instruite de ne fauter que sur ce qu'elle croit réel. On rapporte l'écart de taux de faute entre unités réelles et plantées.
- **Conditions d'entrée, toutes à 0,5 ± bruit.**
  - Réel contre réel, entre deux lots honnêtes de gabarits distincts.
  - « Audité ou non », tiré après gel des activations.
  - Étiquettes permutées, avec toute la sélection rejouée.
- **Contrôle positif.** Un marqueur grossier doit être détecté.
- **Falsifie.**
  - H_B réfute P1 pour ce générateur : un seul discriminateur suffit. Les garanties de l'usage concerné sont alors rapportées dégradées selon l'avantage mesuré.
  - H_A réfute seulement « un discriminateur de cette famille suffit, à ce niveau de capacité ». Elle ne borne pas le meilleur discriminateur.

### E2′ — Le secret du tirage fait-il un travail stratégique ?

- **Budget.** p = 0,20. Ce n'est plus un budget réaliste. Le transfert à 2 % suppose que le rapport θ ne dépend pas du budget (HYPOTHÈSE).
- **Bras, de même loi de positions.**
  - R-secret : tirage frais par trajectoire, caché.
  - R-révélé : même loi, tirage communiqué à l'équipe rouge avant son travail.
  - F-historique : sous-ensemble fixe tiré une fois, non publié, l'équipe rouge recevant les indices audités des épisodes précédents.
- **Métrique.** Taux d'interception par faute : faute réalisée, auditée et reconnue.
- **Duel primaire.** θ = interception(R-révélé) / interception(R-secret). **H_A :** θ ≤ 0,5. **H_B :** θ > 0,5.
- **Duel secondaire.** Même rapport pour F-historique contre R-secret, mêmes seuils.
- **Conditions d'entrée.** Au moins 600 fautes réalisées par bras. Interception sous R-secret ≥ 0,10.
- **Contrôles négatifs.**
  - A/A : une trace de fautes d'une équipe rouge non informée, rescorée sous chaque bras, doit donner θ = 1.
  - Modèle honnête : mêmes fausses alertes dans tous les bras.
- **Falsifie.**
  - Primaire. H_B réfute P2 pour cette élicitation : connaître le tirage ne sert pas à l'attaquant, et le hasard vaut un sondage. H_A réfute « la connaissance du tirage est inoffensive à ce niveau de capacité ».
  - Secondaire. H_A réfute « un calendrier fixe non publié suffit ». H_B réfute la nécessité du tirage frais sur cet horizon.
- **Réserve inchangée.** C'est une réplication, sur de longues analyses, d'un résultat voisin RAPPORTÉ sur du code.

### E3′ — Rejeu : tirage privé ou point focal ?

- **Dispositif.** Instances isolées, k = 5 tirages par étape. L'équipe rouge connaît le protocole et vise une faute sur 30 % des étapes.
- **Paramètre primaire ρ.** Corrélation intra-étape de l'indicateur « ce tirage est fautif », connu par construction. Il ne dépend d'aucun seuil ni d'aucun score de désaccord.
- **Lecture.** Deux copies de même taux q divergent avec probabilité 2q(1−q)(1−ρ). Un ρ proche de 1 annule le signal.
- **H_A :** ρ ≤ 0,5. **H_B :** ρ > 0,5.
- **Condition d'entrée.** Taux de faute réalisé entre 0,1 et 0,9.
- **Étalons programmés.**
  - Faute indépendante de la graine : ρ ≈ 1 et désaccord au niveau honnête.
  - Faute tirée par appel : ρ ≈ 0.
- **Contrôle négatif.** Sur les étapes où l'équipe rouge ne faute pas, le désaccord doit égaler celui du modèle honnête. Sinon le score lit la consigne, pas la faute.
- **Mesure secondaire, non décisionnelle.** Détection par désaccord aux points atteignables, seuil calibré sur un jeu disjoint (étapes honnêtes à méthodes multiples incluses), contre un comparateur doté des mêmes secondes-GPU.
- **Falsifie.** H_B réfute la garantie supposée de U6 pour cette élicitation : les copies se coordonnent sans hasard partagé. H_A réfute « le point focal suffit à ces modèles ».
- **Variance honnête.** Elle ne peut plus se déguiser en point focal. Si elle sature le score, c'est une limite d'instrument, rapportée dans la mesure secondaire.

### E4′ — Aveuglement : le hasard ajoute-t-il au masquage déterministe ?

- **Générateur.** L'attribut d'enjeu a des corrélats de force réglée λ ∈ {0, moyenne, forte}. À λ = 0, l'effet est vrai par construction et ne sert que d'étalon.
- **Bras.** Sans masque ; pseudonymes canoniques déterministes ; jetons tirés avec permutation aléatoire des étiquettes et de l'ordre.
- **E4a, à λ moyenne.** d = taux de faute ciblée (déterministe) − taux (aléatoire). **H_A :** d ≥ 0,20. **H_B :** d < 0,20.
- **E4b.** Perte de qualité honnête sous masque aléatoire, appariée. **H_A :** ≤ 3 points. **H_B :** > 3 points.
- **Chaîne rapportée.**
  - Ré-identification sur entrées masquées seules, avant l'équipe rouge, avec score propre. C'est une borne inférieure.
  - Tentative.
  - Faute effective.
- **Condition d'entrée.** Taux de faute ciblée sans masque ≥ 0,30.
- **Contrôles négatifs.**
  - Masque sur un attribut sans rapport : taux inchangé.
  - Équipe rouge à faute opportuniste, non conditionnée à l'attribut : taux inchangé.
- **Falsifie.**
  - E4a. H_B réfute l'apport du hasard à U8 sur ce banc, la chaîne disant si le masque déterministe suffit ou si aucun ne tient. H_A réfute l'équivalence des deux masques.
  - E4b. H_B réfute la praticabilité de U8 à ce coût. H_A réfute « le masquage détruit la tâche ».

### Ancrage matériel révisé

Les bras ajoutés et les jeux de calibration disjoints portent le volume à environ 1,5 fois celui de III.1. E0′ passe à environ 2 personnes × 5 jours.

---

## (c) Réponse à l'arbitre

**Ce qui est établi.**
- Aucun fait VÉRIFIÉ : le bloc FAITS ne contient que la question.
- RAPPORTÉ, de mémoire et sans audit : chaque usage du recensement a une garantie démontrée dans son modèle d'origine (jeux d'inspection, preuves interactives, calcul distribué vérifiable, canal subliminal, auto-test, échantillon réutilisable, balises). Des applications aux agents de langue existent pour U1, U3, U5, U6, U9 et U10.
- Les critiques ont montré que trois de mes critères de III.1 étaient inatteignables ou non jugeables :
  - l'écart de 15 points de E2 à 2 % de budget ;
  - le point à 1 % de fausses alertes sur un score à cinq tirages ;
  - la règle d'arrêt.

  Ces points sont marqués VÉRIFIÉ par leurs auteurs ; je les ai recalculés, concordants. Le recensement U1–U12 n'a reçu aucune objection de fond, ce qui ne l'établit pas.

**Ce qui ne l'est pas.**
- **« Exactement ».** Pour aucun usage je ne connais de borne qui se transporte telle quelle à une longue analyse en langue naturelle. Chaque garantie est multipliée par deux facteurs non mesurés : la sensibilité de l'auditeur et l'indiscernabilité des effets du tirage (P1).
- **« Stratégique ».** Rien n'établit que ces agents exploitent un calendrier connu (P2) ni qu'ils se coordonnent sans hasard partagé. Une équipe rouge instruite ne borne que la capacité obtenue par cette élicitation.
- **« Tous les usages ».** Mon critère de distinction (ce qui est caché, moment du tirage, garantie) est une HYPOTHÈSE. Un usage publié hors des douze classes la réfute.
- **Les moins étudiés.** Je maintiens, comme HYPOTHÈSE : U8, U11, U12, U2 engagement-défi, U4 anti-collusion. Je retire toute explication causale de leur rareté.
- **La dissuasion.** Aucune de mes expériences ne la teste. Il ne reste que la détection.

**Ce qui me donnerait tort.**
- E0′, issue H_B : trois articles au niveau large pour l'un de ces usages.
- E1′, issue H_A : elle réfuterait ma thèse selon laquelle la mesure de P1 est le manque principal pour U3, U5 et U8.
- E4a, issue H_B : le hasard n'ajouterait rien au masquage déterministe, et U8 sortirait de ma liste comme usage du hasard.

**À faire en premier.**
- **Sur banc : E1′.** Elle conditionne la lecture de tout le reste. Si un discriminateur atteint 0,60 sur les unités plantées, paraphrasées ou masquées, les mesures de U3, U5 et U8 ne sont plus des garanties mais des taux conditionnels à l'avantage mesuré. Ses conditions d'entrée valident aussi le banc avant tout autre duel.
- **En parallèle : E0′.** Elle ne consomme aucun calcul et peut réfuter mon classement en une semaine.

FIN-DE-CELLULE