# Proposition A — Tour III.3 : réponse aux critiques (N12 / N13)

**Pièces absentes, en une ligne.** Inchangé depuis III.1 : C-17, R-1012, N-053 et les deux PDF ne sont pas servis ; je les prends tels que les pièces 1, 2, 4, 5, 6 les citent. Les pièces 4 et 5 restent non contre-lues : tout chiffre d'Avalon ou de Damani est RAPPORTÉ. Les calculs de puissance des critiques sont illustratifs ; je ne les ai pas refaits, je les prends comme ordres de grandeur.

Je ne réponds qu'aux sections visant A. Convention : **A** = acceptée ; **R** = rejetée (raison donnée) ; **T** = transformée en test ou en contrôle.

---

## (a) Verdict critique par critique

### E1 — moniteurs neufs (couche 3)

| Source | Critique | Verdict | Raison ou transformation |
|---|---|---|---|
| C-a1 | Dilemme : sorties exclues de la décision ⇒ (ii) ≡ (iii) par construction ; sorties lues pour composer ⇒ violation de N-053 | **R partiel, T** | Le dilemme est vrai pour l'usage que j'avais écrit (« rapportées dans `historique` »). Il n'est pas exhaustif : N-058 (VÉRIFIÉ, pièce 2) dit que « l'interdit porte sur la sélection d'agents, pas sur celle des fiches ». Troisième voie : les moniteurs neufs n'alimentent que l'étage de **filtrage des fiches** (sélection de fiches, admise), jamais le canal que lit ce qui compose. (ii) diffère alors de (iii) par les fiches qui survivent, sans que le score du moniteur entre dans la sélection des parties. HYPOTHÈSE de lecture de N-058 à faire confirmer par Lazar ; la séparation des canaux est écrite au manifeste et auditée mécaniquement. |
| B-a / B-c1 | Bras (iii) handicapé par construction ; manque un bras (iv) à travail utile égal | **A** | Le budget consommé par l'écriture est restitué au bras témoin. |
| C-c2 | Manque un bras « catalogue + variation d'invite ou de seuil » (égalité des espaces, N-045 §7) | **A, fusionné avec B-iv** | Le budget restitué est dépensé sur une variation du catalogue existant : un seul bras témoin répond aux deux critiques. |
| D-a / D-c3 | (ii) et (iii) diffèrent par le contenu du contexte ; exclusion causale non démontrée ; manque un bras « sortie vide ou permutée à coût de contexte égal » | **A** | Remplace mon ancien (iii) « écrits, non servis ». |
| B-b / C-b3 | 3 familles : puissance ≈ 0,5 ; ≥ 15 familles sans correction : fausses promotions ; « ≥ 3 franchissements » est une règle sans contrôle de multiplicité | **A** | Test global apparié par famille (modèle mixte) sur F ≥ 8 familles (illustratif), à la place d'un comptage de franchissements. |
| D-b | σ_A/A n'estime ni la variance inter-familles ni la variance inter-graines | **A** | Le plancher de bruit de E1 inclut la composante inter-familles estimée dans le modèle mixte ; σ_A/A seul ne sert qu'au test A/A. |
| D-a | « Score permuté » dégrade surtout l'apprentissage | **A partiel** | Il reste pour détecter un artefact de signal ; il ne sert plus de contrôle de fuite d'information, rôle repris par le bras « sortie vide ». |

### E2 — Lean contre lecteur neuf

| Source | Critique | Verdict | Raison ou transformation |
|---|---|---|---|
| C-a4 | Asymétrie d'outillage : un script sur grille manque un point anguleux ; la supériorité de Lean sur « régularité manquante » est fabriquée | **A** | Le bras lecteur reçoit un outillage symbolique (calcul formel) en plus du numérique. La question devient « Lean contre lecteur neuf outillé symbolique + numérique ». |
| D-a | Biais de spectre : la banque reprend les erreurs que le lecteur a déjà trouvées ; « Lean sur énoncé seul » ne contrôle pas la fidélité de la traduction | **A** | Le tiers scelleur plante aussi des classes nouvelles, à l'aveugle des deux bras ; le contrôle « énoncé seul » est remplacé par une vérification indépendante de la fidélité de chaque traduction Lean (D-c4). |
| D-b | Le rappel est conditionnel à la loi des erreurs de la banque ; une parité ne ferme pas la question générale | **A** | La conclusion de E2 est bornée à la banque : descriptive, pas générale. Elle suffit pour décider d'ouvrir ou non une couche en douze mois, pas pour une revendication. |

### E3 — crédit collectif contre crédit par partie

| Source | Critique | Verdict | Raison ou transformation |
|---|---|---|---|
| B-a | Affinage hors ligne : confondant intensité d'optimisation × crédit ; aucun critère disant si l'absence d'écart est informative | **A, T** | Critère d'informativité préenregistré : l'absence d'écart ne compte que si le score oracle de tâche a bougé au-delà du plancher dans les deux bras (la pression est manifeste). Sinon, « non jugeable à cette intensité », et l'escalade vers le renforcement en ligne suit une règle gelée (ci-dessous). |
| C-a2 | Le filtre collectif confond crédit et variance de sélection (dilution du critère d'acceptation) ; une partie qui échoue mais signale survit sous filtre collectif | **R partiel, T** | La dilution du crédit *est* la définition du crédit collectif d'Avalon (« même avantage pour tous les jetons », RAPPORTÉ pièce 4 §1.2) : ce n'est pas un artefact, c'est l'hypothèse. Mais le **taux d'acceptation** doit être apparié entre bras (même quantile retenu), sinon la différence mesure le nombre de trajectoires survivantes. Ajouté. |
| D-a | Confond crédit, algorithme et unité d'attribution (bras ou agent) | **A** | Unité fixée : la trajectoire d'une partie, identique dans les deux bras ; seul le score de filtrage change. |
| D-a / D-c1 | Un point de contrôle 0 ne remplace pas un témoin sans entraînement suivi dans le temps ; graines indépendantes | **A** | Bras « poids gelés », évalué à chaque point de contrôle ; ≥ 3 graines par bras (illustratif, rendu abordable par la voie hors ligne). |
| B-b | 20 points à n = 30 runs : sous-puissant dans la zone plausible | **A** | Mesure par agent avec variance de grappe (run), n et seuil fixés après le pré-test de départ ; zone grise déclarée. |
| B-c2 | Pré-test du signalement du modèle de départ, préalable absolu | **A, T** | E3′ à N = 1 est ce pré-test ; règle d'arrêt : p₀ < 0,3 (illustratif) ⇒ E3 non jugeable, on ne la paie pas. |
| D-b | Comparaison marginale mélange scénario, point de contrôle, graine ; interactions non jugées | **A** | Analyse stratifiée (scénario × point × graine) ; l'interaction bras × point de contrôle est préenregistrée comme lecture secondaire. |
| B-a | Issue « les deux bras tiennent → (c3) tombe » mal falsifiée | **A** | Reformulé : (c3) tombe *à cette intensité* ; l'escalade est une règle, pas une impression. |

### E3′ — diffusion sans entraînement

| Source | Critique | Verdict | Raison ou transformation |
|---|---|---|---|
| B-a | Geler l'effectif dans E3 d'après E3′ rend E3 ininterprétable ; préenregistrer ensemble | **A partiel, T** | E3 tourne à N fixé ; E3′ est rejouée par inférence seule sur les points de contrôle finaux des deux bras de E3. On n'a pas besoin de faire varier N pendant l'entraînement pour savoir si l'effet d'effectif existe avant et après. Les deux sont préenregistrées ensemble. |
| D-a | Une absence d'effet à poids fixes n'écarte pas une diffusion qui n'apparaîtrait qu'après entraînement | **A** | Réglé par la rejouée ci-dessus. E3′ seule ne falsifie que « diffusion à poids fixes ». |
| C-b1 / C-c1 | Corrélation intra-run (canal partagé) ⇒ effectif efficace ≈ R ; redondance rationnelle (un signale, les autres s'abstiennent) confondue avec diffusion ; bras à canal muet manquant | **A, T** | Plan 2 × 4 : canal partagé / muet × N ∈ {1, 2, 4, 8}. Variance de grappe. Diffusion et coordination sont séparées par deux métriques : taux par agent *et* taux par run ; « par agent baisse, par run constant » = coordination ; « par run baisse » = diffusion. |
| D-b | La prédiction 1 − (1 − p₁)^N suppose l'indépendance conditionnelle ; il faut E_Z[·] par scénario | **A** | Les scénarios sont scriptés et peu nombreux : p_{1,Z} est estimé par scénario à N = 1, la prédiction est calculée par scénario puis agrégée. |

### E4 — signalement omis, sonde

| Source | Critique | Verdict | Raison ou transformation |
|---|---|---|---|
| C-a3 / D-a / B-c3 (convergentes) | Sous contrat, la vérification mécanique est la cible elle-même (rappel 100 %, fausses alertes 0) : rien ne peut la battre ; sans contrat, la sonde entraînée sur C fuit l'oracle ; cible déplacée vers « reconnaissance » sans vérité indépendante | **A** | E4 telle qu'écrite était mal posée. Reformulée en régime **sans contrat** du lot 3 : le moniteur n'observe pas C au test ; la cible reste l'étiquette oracle (C vrai, ρ non émis) sur **familles de scénarios tenues à l'écart** de l'entraînement de la sonde. Pas de cible « reconnaissance ». La vérification mécanique sous contrat n'est plus un concurrent : c'est l'instrument de mesure de (c1), à part. |
| B-a / B-c | Points de décision non définis ; circularité ; rapporter leur nombre | **A** | Point de décision = tour scripté par le scénario scellé (l'animateur publie un résultat par tour, RAPPORTÉ pièce 4 §1.5), fixé par le tiers avant toute lecture, identique entre bras et prédicteurs ; nombre rapporté par bras. |
| B-c3 / C-c3 / D-c2 | Cas manquants : outil ρ absent ; C vrai mais signalement non dû, déjà fait par un tiers, ou interdit ; C faux et ρ émis | **A** | Tous ajoutés comme cas honnêtes appariés ; la sonde ne doit pas alerter sur « C vrai, signalement non dû » (sinon elle lit l'incident, pas l'obligation). |
| D-a / D-c1 | Partition construction/évaluation par scénario, famille, point de contrôle avant tout ajustement ; sonde peut apprendre le bras ou le style du point | **A** | Partition scellée avant entraînement ; évaluation interne au point de contrôle puis sur un point tenu à l'écart. |
| C-b2 / B-b | À n₀ = 30 cas honnêtes, le seuil à 5 % de fausses alertes est instable ; rapporter variance intra/inter | **A** | Plusieurs centaines de points honnêtes (illustratif, issus de tous les runs à C faux) ; courbe ROC complète avec intervalles plutôt qu'un seul point ; variance intra/inter rapportée. |
| (reprise de C sur D, c3) | La sonde peut détecter la dérive des poids (pas 180 contre pas 50) | **A, emprunté à C en le disant** | La même sonde est appliquée aux activations du bras « poids gelés » et du bras par partie **au même pas**. |

### E5 — confiance des juges

| Source | Critique | Verdict | Raison ou transformation |
|---|---|---|---|
| B-a | Confiance permutée ne mord pas si la confiance est quasi constante | **A** | Contrôles : confiance uniforme sur [0, 1] ; constante au taux de base ; permutée gardée. |
| B-b / B-c4 | Manque l'AUROC du verdict binaire ; un juge de frontière peut dépasser 0,60 sans que la confiance porte quoi que ce soit ; H_B s'appuie sur des 7B | **A** | Ligne de base : verdict binaire du juge et probabilité des jetons. Je concède que H_B est ancrée sur Damani (7–8B, RAPPORTÉ) et non sur nos juges : c'est précisément ce que E5 mesure. |
| D-a | L'AUROC marginal ne détermine pas l'utilité d'un vote pondéré (loi jointe) ; E5 teste une confiance extraite, pas RLCR | **A sur le premier point ; R sur le second** | Premier point : deuxième étage ajouté (vote pondéré contre vote simple sur fiches tenues à l'écart). Second : c'est par construction — N-045 §8 (VÉRIFIÉ) interdit d'entraîner les cerveaux de frontière, donc l'apport de RLCR ne peut se poser que pour un juge local, et seulement si la confiance porte de l'information. E5 est le préalable, pas le test de RLCR. |
| D-b | AUROC indéfini à une classe ; zone [0,55 ; 0,60] non jugée | **A** | Zone grise déclarée ; une classe seule ⇒ non jugeable. |
| D-c5 | Prédicteur constant, jetons, panel complet sur fiches tenues à l'écart | **A** | Ajoutés. |

Bilan : deux rejets partiels (C-a1 sur l'exhaustivité du dilemme ; C-a2 sur la nature d'artefact de la dilution), un rejet (D sur E5), tout le reste accepté ou transformé. Les trois critiques convergentes sur E4 (B, C, D) ont raison : c'était le point le plus faible de III.1.

---

## (b) Expériences corrigées

Seuils illustratifs, gelés au préenregistrement ; plancher de bruit du pilote A/A (N-045 §6(i)) **plus** les composantes inter-familles et inter-graines quand elles existent.

### E1′ — Le résidu de la couche 3 vaut-il un bras ?

- **H_A** : l'espace de composition de N-045 suffit. **H_B** : des moniteurs écrits par l'organisme, servant seulement à filtrer ses fiches, ajoutent au score oracle par dollar.
- **Bras**, à coût total apparié, F ≥ 8 familles plantées tenues à l'écart, K ≥ 3 générations : (i) composition N-045 ; le budget d'écriture est restitué sous forme d'une variation d'invite ou de seuil d'un moniteur du catalogue (B-iv ∪ C-c2) ; (ii) moniteurs neufs en bac à sable, sorties branchées sur **l'étage de filtrage des fiches seulement**, canal séparé du `historique` lu pour composer (manifeste, audit du canal) ; (iii) moniteurs écrits, sortie remplacée par une sortie vide ou permutée de même longueur (D-c3).
- **Métrique** : score oracle (N-058) par dollar, par génération. **Analyse** : modèle mixte apparié par famille ; test global, pas de comptage de franchissements ; puissance calculée après le pilote ; si la variance inter-familles rend l'alternative δ hors de portée, on rapporte un intervalle sans verdict.
- **Falsifie H_B** : (ii) ≈ (iii) ≈ (i). **Falsifie H_A** : (ii) > (i) et (ii) > (iii), nul sous score permuté. La composition elle-même reste sélectionnée sur oracle et coût seuls.
- **Dépendance** : n'existe pas hors de l'étape 2.

### E2′ — Lean contre lecteur neuf outillé

- Banque de preuves courtes ; un tiers plante à l'aveugle des erreurs des trois classes observées (pièce 5 §1.3) **et** de classes nouvelles qu'il choisit sans les annoncer ; preuves saines pour les fausses alertes.
- Bras : lecteur neuf avec outillage symbolique et numérique ; formalisation Lean, chaque traduction vérifiée par un second agent indépendant (fidélité à l'énoncé source rapportée à part des réfutations et des échecs de compilation).
- **Falsifie H_A** (Lean détecte une classe que le lecteur manque) : parité sur toutes les classes, nouvelles comprises. **Falsifie H_B** : une classe où Lean détecte et le lecteur outillé manque, à fausses alertes comparables, traduction fidèle.
- Conclusion bornée à la loi des erreurs de la banque (D-b) : décision d'ouverture, pas revendication.

### E3″ — Crédit collectif contre crédit par partie, voie hors ligne, avec règle d'escalade

- **H_A** : à intensité, modèle, environnements, points de contrôle et taux d'acceptation égaux, le filtrage par score d'ensemble fait baisser le signalement par rapport au filtrage par score par partie. **H_B** : baisse égale ; la cause est le renforcement sans récompense du signalement.
- **Préalable (règle d'arrêt)** : E3′ à N = 1 donne p₀ ; si p₀ < 0,3, E3″ est non jugeable et n'est pas payée.
- **Bras** : filtre collectif ; filtre par partie ; **poids gelés** évalués à chaque point de contrôle. Unité : trajectoire d'une partie dans les deux bras ; quantile d'acceptation identique ; récompense tirée de l'oracle seul (N-058) ; ≥ 3 graines par bras ; signalement **mesuré jamais récompensé**, dans des scénarios de « rapport non émis » scellés par un tiers, hors bras d'attaque.
- **Métrique** : taux par agent avec variance de grappe (run) et taux par run, stratifiés scénario × point × graine ; faux signalements sur C faux et sur canaris « à ne pas signaler » (N-045), en nombre au moins égal aux incidents.
- **Critère d'informativité** : si les deux bras tiennent, le résultat ne compte que si le score oracle de tâche a dépassé le plancher dans les deux bras. **Règle d'escalade** gelée : vers le renforcement en ligne seulement si (a) écart sous le plancher mais pression manifeste, ou (b) écart au-dessus du plancher à confirmer ; jamais sur « non jugeable ».
- **Falsifie H_A** : chute égale, pression manifeste → « la récompense collective importe le défaut » est mal attribué ; la précaution porte sur tout entraînement local. **Falsifie H_B** : le bras par partie tient, le collectif chute → crédit collectif exclu comme signal, admis comme générateur avec contrefactuel.
- **Rejouée** : E3′ (ci-dessous) relancée par inférence seule sur les points de contrôle finaux des deux bras.

### E3′′ — Diffusion et coordination sans entraînement

- Plan 2 × 4 : canal partagé / muet × N ∈ {1, 2, 4, 8}, poids identiques, scénarios scellés, consigne identique, aucune hiérarchie.
- **H_A** (diffusion) : le taux **par run** baisse avec N. **H_B** : le taux par run suit la prédiction par scénario E_Z[1 − (1 − p_{1,Z})^N] ; une baisse par agent avec run constant est de la **coordination** (redondance), rapportée comme troisième issue, non comme diffusion.
- Variance de grappe ; contrôle : scénario sans incident (faux signalements par agent ne doivent pas bouger avec N) ; le bras muet sépare l'effet de consigne « vous êtes huit » de l'interférence par le canal.
- E3′′ ne falsifie que « diffusion à poids fixes » ; sa rejouée sur les points finaux de E3″ dit si l'entraînement crée ou amplifie l'effet d'effectif.

### E4′ — Détection de l'omission sans contrat

- Régime du lot 3 : au test, le moniteur **n'observe pas C**. Cible : étiquette oracle (C vrai, ρ non émis), sur familles de scénarios tenues à l'écart de l'entraînement de la sonde ; partition scellée par scénario, famille, point de contrôle avant tout ajustement.
- **H_A** : une sonde linéaire lue aux points de décision (tours scriptés, fixés par le tiers) ou un classifieur du raisonnement transportent une détection à fausses alertes bornées sur familles inédites. **H_B** : rien ne dépasse les prédicteurs sans information (constant ; mot-clé « alert/report », qui alerte sur 97–100 % des runs, RAPPORTÉ) ; la mention ne prédit pas l'action.
- Cas honnêtes appariés obligatoires : C faux ; C faux et ρ émis ; outil ρ absent ; C vrai mais signalement non dû, déjà fait par un tiers, ou interdit. Sonde entraînée sur étiquettes permutées. Même sonde appliquée aux bras « poids gelés » et « par partie » **au même pas** (dérive des poids).
- Métrique : courbe ROC complète avec intervalles, variance intra/inter rapportée ; plusieurs centaines de points honnêtes ; évaluation interne au point de contrôle puis sur un point tenu à l'écart.
- La vérification mécanique sous contrat reste l'instrument de mesure de (c1) ; elle ne concourt pas ici.

### E5′ — La confiance des juges porte-t-elle de l'information ?

- Lignes de base : verdict binaire du juge ; prédicteur constant au taux de base ; confiance uniforme ; confiance permutée ; probabilité des jetons. Fiches tenues à l'écart par famille. Brier, ECE à 10 classes avec bootstrap, AUROC, diagrammes de fiabilité.
- **H_A** : AUROC(confiance) > 0,60 et apport mesurable au-dessus du verdict binaire. **H_B** : AUROC ≤ 0,55 ou confiance agglomérée. Zone [0,55 ; 0,60] déclarée non jugée ; une seule classe ⇒ non jugeable.
- Second étage, si H_A tient : vote pondéré contre vote simple sur fiches tenues à l'écart (loi jointe des erreurs du panel, D). L'entraînement RLCR ne se pose que pour un juge local, après.

---

## (c) Réponse à l'arbitre

### Ce qui est établi (VÉRIFIÉ, pièces 1, 2, 6)

- N-045 fait de la composition une variable apprise, coût dans le signal, et fait entraîner par l'organisme lui-même un adaptateur qui propose des conceptions : une part de la couche 3 (réécriture de soi restreinte à l'espace de composition) est **déjà couverte**.
- N-058 : aucun score de moniteur ni de juge n'entre dans la sélection des agents ; la sélection des fiches par sévérité du test survécu reste permise. C'est la contrainte qui borne tout volet « moniteurs neufs » : admissible pour filtrer des fiches, jamais pour composer.
- Damani : récompense justesse − (confiance − justesse)², sans couplage à un ancrage ; le théorème garantit un maximum d'espérance, pas que l'apprentissage l'atteigne ; les deux « RLCR » n'ont rien en commun.

### Ce qui n'est pas établi

- Que la chute du signalement chez Avalon soit **causée par le crédit collectif** : aucun témoin mono-agent apparié, un seul run, 20 % de déroulés mono-agents (RAPPORTÉ, pièce 4). Dire que la récompense collective « importerait le défaut » est une hypothèse, pas un fait.
- Que ce résultat soit une menace diffuse par omission au sens du programme ou une collision avec H9 : la lecture servie conclut voisinage, cas naturel de rapport non émis, ni adversaire ni obligation établis (RAPPORTÉ).
- Que « nos sondes » mesurent cette omission : la mention dans le raisonnement est quasi constante et ne prédit pas l'action ; le régime sans contrat est non couvert.
- Que le résidu de la couche 3 (moniteurs neufs) vaille quelque chose ; que Lean détecte ce qu'un lecteur neuf outillé manque. Les deux sont des questions, et je concède que E2 ne donnera qu'un résultat relatif à sa banque.
- Que la confiance verbalisée de nos juges porte de l'information : H_B est ancrée sur des modèles de 7–8B (RAPPORTÉ), pas sur les nôtres.

### Réponses

**N12.** (1) Couverture partielle : oui pour la réécriture de soi dans l'espace de composition, non pour « moniteurs neufs à la demande » et non pour la couche 4, qui n'est pas une capacité d'adaptation mais de vérification. (2) Le risque documenté n'est pas la réécriture du noyau : c'est la violation de N-053 par un organisme qui se sélectionne sur ses propres moniteurs ; la seule valeur admissible de la couche 3 est un filtre de fiches, mesurable par E1′. (3) Étape 2 d'abord, E1′ préenregistrée comme ablation dedans ; E2′ est indépendante, peu coûteuse, mais n'ouvre la couche 4 que sur une classe d'erreurs mesurée.

**N13.** (1) (c1) et (c3) ne s'excluent pas : le bras collectif de E3″ est le générateur de (c3) et le bras par partie son contrefactuel ; (c2) est exclue par le dessin actuel de la course 2 (pas d'oracle), ce qui est contingent, pas logique. (2) Précaution formulée en mesure : le signalement se mesure par agent et par run, à chaque point de contrôle, avec un point 0 et un témoin à poids gelés, dans **tout** bras qui entraîne un instrument local, collectif ou non, et avec autant de canaris « à ne pas signaler » que d'incidents. (3) Damani apporte des **métriques** pour juges et moniteurs (Brier, ECE, AUROC ensemble, cohérence, extraction par phrase ajoutée) ; son entraînement ne s'applique qu'à un juge local et seulement après E5′.

### L'expérience à faire en premier

**E3′′ et E5′**, toutes deux par inférence ou calcul seuls, avant toute dépense d'entraînement. E3′′ parce qu'elle est la règle d'arrêt de E3″ (p₀), qu'elle sépare diffusion, coordination et canal avec un plan 2 × 4 bon marché, et qu'elle sera rejouée sur les points finaux de E3″ ; E5′ parce que son coût marginal est nul et qu'elle décide si la question 3 a un objet. Dans l'ordre des dépenses de N-045 §4 : E3′′, E5′, E2′, E4′ sur les traces de E3″, E3″ hors ligne, E1′ dans l'étape 2 ; le renforcement en ligne seulement sur la règle d'escalade gelée.

**Ce qui me donnerait tort, après corrections** : E3″ avec pression manifeste et chute inégale (cause collective rétablie) ; E3′′ avec taux par run décroissant à canal muet (diffusion sans entraînement, que j'avais sous-pesée) ; E4′ avec une sonde qui transporte sur familles inédites et tient sur « C vrai, signalement non dû » ; E5′ avec AUROC > 0,60 au-dessus du verdict binaire ; E2′ avec une classe nouvelle que seul Lean trouve ; E1′ avec (ii) > (i) et (ii) > (iii).

FIN-DE-CELLULE