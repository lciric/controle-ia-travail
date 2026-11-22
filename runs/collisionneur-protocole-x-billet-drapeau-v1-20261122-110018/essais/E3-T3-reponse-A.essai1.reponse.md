# Proposition A — Tour III.3 : réponse aux critiques

## 0. État des pièces

- **FAITS** : le bloc reproduit la question, sous la même empreinte déclarée (non recalculée). Il ne contient aucun fait à statut.
- **Pièces reçues** : ma conception III.1 et les critiques B, C, D, E, F, toutes terminées par FIN-DE-CELLULE. Je ne réponds qu'aux sections « Sur la proposition A ».
- **Statuts** : je ne modifie aucun statut posé par les critiques. C marque VÉRIFIÉ plusieurs propriétés de lois ; je signale lesquelles j'ai recalculées, sans requalifier les autres. Mes verdicts sont des HYPOTHÈSES de méthode.
- **Chiffres** : tous sont illustratifs, y compris mes recalculs.
- **« Test de devinette »** : son protocole et ses résultats restent non transmis. D le relève aussi.

---

## (a) Verdict sur chaque critique

### D1 et I4 (fuite du texte candidat)

| Critique (source) | Verdict | Conséquence |
|---|---|---|
| Double verdict : un intervalle inclus dans ]0 ; 5[ points valide H_A et H_B (D, E, F) | **Acceptée.** Erreur logique de ma règle, B4 violée | Hypothèses complémentaires autour d'une seule marge d |
| Questionnaire et T0 rédigés par qui connaît S (B, E) | **Acceptée pour T0.** **Rejetée dans la forme de B** pour le questionnaire : on ne peut pas transcrire S en étant aveugle à S | T0 par des tiers aveugles à S et à T ; questionnaire par un tiers qui connaît S mais pas T |
| Le choix fermé fournit l'espace des réponses (C, F) | **Rejetée comme biais sur l'écart** : T et T0 reçoivent les mêmes options, l'artefact relève les deux bras. **Acceptée** comme risque de plafond et de validité externe | Bras sans texte T∅ ; réponse ouverte recueillie avant le choix fermé |
| T+ ne borne que les fuites grossières (B) | **Acceptée** | Gamme graduée de fuites plantées |
| Réécrire T puis le revalider sur les mêmes questions et devineurs (D, F) | **Acceptée** | Items de développement et de confirmation séparés ; devineurs neufs ; nombre de réécritures plafonné |
| Corrélation entre items d'un même devineur ; 10 humains ne peuvent pas juger H_A (B, F) | **Acceptée.** Recalcul : √(2 × 0,25 / 10) ≈ 0,22 | Unité d'analyse = le devineur, score agrégé |
| Corrélation entre devineurs sur un même item, non-jugeabilité « pour tout n » (C, E) | **Acceptée pour les modèles**, qui ne sont pas un échantillon. **Rejetée pour des humains tirés indépendamment** sur un item fixé : le modèle de C suppose une composante commune que rien n'impose. Valeur 0,0015 non reproduite | Modèles traités en effets fixes, résultats par modèle, sans généralisation |
| 20 tests par élément sans correction (B, C). Recalcul : 1 − 0,95²⁰ ≈ 0,64 | **Acceptée** | Une seule métrique principale ; l'analyse par élément devient exploratoire et corrigée |
| Augmenter l'effectif en cas d'indétermination gonfle l'erreur (E) | **Acceptée** | Effectif fixé d'avance, au plus une analyse intermédiaire déclarée |
| Plafond si p_T0 est proche de 1 (B, D, F) | **Acceptée** | Règle d'exclusion écrite d'avance, appliquée sur les items de développement |
| Secret leurre S′ (B) | **Transformée en test** | Les mêmes réponses sont notées contre une clé fictive |
| Placebo stylométrique d'auteurs (E) ; placebo unique (F) | **Transformée en test** | Trois T0 de rédacteurs distincts, plus un T0 tiré des articles antérieurs de l'équipe |
| Humains et modèles mélangés sans règle (F) | **Acceptée** | Analyses séparées, règle de combinaison écrite |
| Exclusion des personnes exposées (B) | **Acceptée**, pour D1, D3 et D5 | Registre tenu par un tiers |

### D2 et I1 (adversaire informé)

| Critique (source) | Verdict | Conséquence |
|---|---|---|
| Rien n'interdit de retoucher le détecteur après D2 (B) | **Acceptée** | Empreinte du détecteur avant D2, contrôlée après ; attaques de D2 disjointes du jeu scellé de l'étude |
| Seuil fixé et évalué sur le même lot honnête ; règle de trois invalide si le seuil vient des mêmes cas (C, D, F, B) | **Acceptée** | Lots honnêtes de calibrage et de test disjoints |
| Quantile à 1 % bruité (B, C, E, F). Je retrouve le rapport de densités ≈ 16,2 de C avec z = 1,96 | **Acceptée** | Point de fonctionnement relevé ou effectif accru ; rééchantillonnage qui réestime le seuil |
| Deux ou trois attaquants : la variance entre attaquants domine (B, E) | **Acceptée** | Attaquants en effets fixes ; la conclusion vaut « pour ces attaquants » |
| Plancher, plafond, baisse de δ impossible si p_naïf < δ (B, D) | **Acceptée** | Précondition sur le taux du bras naïf |
| Bras et période confondus avec des personnes (B) | **Acceptée** | Bras naïf rejoué en fin de campagne ; aucun bras humain sans témoin simultané |
| « Aucune baisse » peut signifier « l'attaquant n'a pas utilisé l'information » (D) | **Transformée en test** | Contrôle de manipulation |
| L'échec d'un attaquant en boîte blanche est aussi compatible avec un dispositif robuste (D) | **Acceptée.** Mon contrôle positif n'était pas indépendant de ce qu'il devait calibrer | Contrôle positif sur un détecteur de référence faible. L'idée d'un détecteur factice vient de E, telle que la rapportent B et C ; je m'en sers comme contrôle positif, ce qu'ils disent qu'il est |
| T0 non apparié en longueur à T+M (F) | **Acceptée** | Second placebo, neutre et sans faux mécanisme |
| Fausses alertes possiblement variables selon le contexte fourni (E) | **Transformée en test** | Cas honnêtes produits sous chaque contexte, sans consigne adverse |
| Les modèles figés annulent par construction la contamination par moissonnage (E) | **Rejetée comme défaut** : périmètre déclaré en III.1 (d). **Acceptée comme limite** | D2 mesure l'effet sous exposition forcée, pas la probabilité d'exposition |
| Plafond de capacité des modèles ouverts (F) | **Acceptée comme limite** | Jamais « robuste » sans complément de nom |

### D3 (reconnaissance)

| Critique (source) | Verdict | Conséquence |
|---|---|---|
| Transfert ou fuite : il faut choisir (B) | **Acceptée** | Cas fictif d'un domaine adjacent ; le transfert reste une HYPOTHÈSE déclarée |
| Plan intra-sujet et effet de demande (B, C, E, F) | **Acceptée** | Option retirée |
| Marge d'équivalence absente en 3b ; cas « la note fait moins bien » omis (B, D) | **Acceptée** | Trois zones et marge écrite |
| Montrer la note à tous ne mesure pas l'attention spontanée (D) | **Acceptée** | Je retire « parce que c'est l'attention qui compte » de H_A′ |
| 60 évaluateurs : puissance ≤ 0,18 (C, recalculé) | **Acceptée** | Borne basse retirée |
| Note pertinente datée après le rival (F) | **Transformée en test** | Bras ajouté |
| Participation sélective (E) ; déclaration ≠ citation (D) | **Acceptées comme limites** | Taux de réponse rapporté |

### D4 (taux de base)

| Critique (source) | Verdict | Conséquence |
|---|---|---|
| Intervalle de Poisson trop large (B, C, F). Recalcul : à p* = 20 %, P(N ≤ 1) ≈ 0,978, et N = 0 laisse une borne haute ≈ 0,975 | **Acceptée.** Une des deux issues est presque inatteignable, B4 non satisfaite | D4 retirée comme duel |
| Non-stationnarité non identifiable depuis l'historique (B, C, D, F) | **Acceptée** | La projection reste une HYPOTHÈSE |
| Grille écrite après avoir vu les parutions qu'elle code (E) | **Acceptée** | Grille par un tiers, sur une fenêtre antérieure |
| Leurre « thème voisin » ambigu (B, D, F) | **Acceptée** | Paires de référence établies indépendamment |
| Parutions ≠ projets en cours (D) | **Acceptée comme limite** | Non corrigeable |

### D5, I2, I3

| Critique (source) | Verdict | Conséquence |
|---|---|---|
| Sans bras public, H_A ne réfute pas « l'avantage exclusif de publier avant » (B, D, E) | **Acceptée.** La falsification annoncée ne découlait pas du plan | Affirmation retirée ; D5 devient un test de sensibilité absolue |
| k petit : puissance nulle sous 5 défauts, faible sous 18 (C ; premier seuil recalculé) | **Acceptée** | k relevé, réparti sur plusieurs copies |
| Style du tiers qui plante les défauts (C) | **Transformée en test** | Copie réécrite d'une seule main ; modifications neutres comme négatifs |
| Défauts plantés ≠ défauts réels (D, E, F) | **Acceptée comme limite** | Le verdict ne vaut que pour les classes plantées |
| Lecteurs non experts (E) ; relecteurs aveugles à l'audit (F) | **Transformées en tests** | Bras et consigne ajoutés |
| L'unicité globale des dépôts n'est pas testable (D) | **Acceptée** | V2 réduite à l'unicité dans un registre nommé |
| C1 « rien, par construction » ignore les métadonnées (E, F) | **Acceptée** | « Par construction » restreint au contenu |
| V5 sur le même lot (D) ; canaris jamais publiés (D, F) | **Acceptées** | V5 sur un lot neuf ; canaris privés interrogés à l'identique |
| V6 réutilise la grille de l'équipe (F) | **Acceptée en partie** : réutiliser une grille figée est ce qui fait de V6 une prédiction | Seconde grille, rédigée par un tiers, appliquée en parallèle |

---

## (b) Expériences corrigées

**Règle commune.** Chaque duel oppose H_A : θ < d à H_B : θ ≥ d (forme reprise de D). Un intervalle entièrement d'un côté réfute l'autre hypothèse. Un intervalle à cheval ne réfute rien et n'autorise pas d'agrandir l'effectif hors du plan écrit.

### D1′ — Le texte candidat laisse-t-il deviner S ?

- **Grandeur** : θ = score moyen sous T moins score moyen sous les placebos, agrégé par devineur. La marge est d = 5 points.
- **Construction**
  - Le questionnaire est rédigé par un tiers qui connaît S et ignore T. Les distracteurs suivent une procédure écrite d'avance.
  - Les items sont scindés en un lot de développement et un lot de confirmation.
  - Trois T0 viennent de rédacteurs distincts, aveugles à S et à T. Un T0-auteurs est tiré des articles publics antérieurs de l'équipe.
- **Bras** : T∅ (aucun texte), les T0, T0-auteurs, T, et T+ à trois niveaux de fuite (littérale, paraphrasée, déductible seulement en croisant avec les travaux voisins).
- **Devineurs**
  - Les modèles figés sont traités en effets fixes, avec un résultat par modèle.
  - Pour les humains, l'unité est la personne. Sous un écart-type de 0,10 par score, il en faut environ 50 par bras pour qu'une borne haute passe sous 5 points.
  - Avec une dizaine d'humains, seule une fuite massive est détectable. Le verdict « pas de fuite ≥ d » ne repose alors que sur les modèles, et je le dirai ainsi.
- **Étape 1, les contrôles**
  - T∅ et T0 contre le hasard. Si T∅ dépasse le hasard, le questionnaire trahit la réponse. Si seul T0 le dépasse, le secret est déjà devinable depuis le domaine public et P4 tombe.
  - Clé S′ : l'excès de T noté contre S′ doit être nul.
  - T+ gradué : le plus faible niveau détecté fixe la résolution du test. Aucun verdict d'innocuité ne vaut en dessous.
- **Étape 2, confirmation** : au plus deux réécritures de T, sur les items de développement. La confirmation est passée une seule fois, avec des devineurs neufs.
- **Falsification** : un intervalle sous d réfute « ce texte fuit d'au moins d », à la résolution mesurée. Un intervalle au-dessus réfute « ce texte est sûr ». Un excès positif sous la marge est rapporté tel quel.

### D2′ — Adversaire informé contre adversaire naïf

- **Gel** : l'empreinte du détecteur est prise avant et contrôlée après. Les familles d'attaques de D2′ sont disjointes du jeu scellé de l'étude principale.
- **Cas honnêtes** : deux lots disjoints, l'un pour le seuil, l'autre pour le test. Le taux de fausses alertes réalisé est rapporté avec son intervalle.
- **Bras** : naïf, T0, T, T0′ (remplissage neutre de la longueur de T+M), T+M, puis naïf rejoué en fin de campagne.
- **Contrôle de manipulation** : l'attaquant informé répond à des questions sur T et M. Un classifieur doit distinguer ses attaques de celles du bras naïf. En cas d'échec, l'issue « pas de baisse » est ininterprétable.
- **Contrôle positif** : les mêmes attaquants, informés, doivent faire chuter un détecteur de référence faible (marqueur lexical). La boîte blanche sur le vrai détecteur est rapportée, sans conditionner la validité.
- **Contrôles négatifs** : T0 contre naïf et T0′ contre naïf doivent donner un écart nul. Les fausses alertes doivent rester invariantes sur des cas honnêtes produits sous chaque contexte.
- **Précondition** : le taux de détection naïf doit se situer entre δ + 10 points et 90 %. Sinon le duel n'est pas jugeable.
- **Falsification** : H_A (baisse < δ) réfute « la validité exige l'ignorance de ce contenu », pour ces attaquants et sous exposition forcée. H_B réfute la robustesse à ce contenu. D2′ ne dit rien de la probabilité qu'un système réel ingère le texte.
- **Personnes** : le bras naïf humain de l'étude principale doit toujours précéder toute publication.

### D3′ — Reconnaissance

- **Plan** : vignette sur un cas fictif d'un domaine adjacent, entre sujets uniquement.
- **Bras** : rien ; note sans rapport de même date ; note pertinente datée après le rival ; empreinte ouverte datée avant ; note publique datée avant.
- **3a** : note avant contre note après et contre rien. Détecter 15 points à puissance 0,8 demande environ 175 évaluateurs par bras.
- **3b** : trois zones (la note fait mieux, équivalence, l'empreinte fait mieux). Une marge de 10 points exige environ 430 évaluateurs par bras. À 150 par bras, seule une marge d'environ 17 points est tranchable. Je tiens donc 3b pour probablement non jugeable à effectif réaliste.
- **Portée** : attribution déclarée, sous exposition forcée, dans une vignette.

### D4′ — Retirée comme duel

Elle devient une estimation descriptive.

- La grille est écrite par un tiers sur une fenêtre antérieure. Sa sensibilité et sa spécificité sont mesurées sur des paires de référence.
- Seule l'issue N ≥ 2 autorise un verdict (« p ≥ p* »), et seulement sous stationnarité. N ≤ 1 ne réfute rien.
- D4′ n'est plus une condition de bascule de mon choix.

### D5′ — Sensibilité de la relecture scellée

- **Hypothèses** : H_A, sensibilité ≥ 70 % ; H_B, sensibilité < 70 %. Elles portent sur les classes de défauts plantées.
- **Protocole**
  - Au moins 20 défauts, répartis sur plusieurs copies.
  - Chaque copie est réécrite en entier par le tiers, pour un style homogène.
  - Les relecteurs ne sont pas informés de l'audit.
- **Contrôles** : copies saines, reformulations neutres, bras de lecteurs non experts. Si ces derniers font aussi bien, les défauts plantés sont triviaux.
- **Falsification** : chaque issue réfute l'énoncé opposé, pour ces classes seulement.
- **Portée** : D5′ ne dit rien de ce qu'une exposition publique trouverait. Cette comparaison n'est testée par aucun de mes duels.

### Instruments

- **I1** : la règle de trois ne s'applique qu'à un lot honnête indépendant du réglage du seuil.
- **I2 et V2** : l'unicité n'est vérifiable que dans un registre nommé. La critique de D crée un arbitrage que je n'avais pas vu :
  - un registre public lié à l'identité rend les dépôts multiples comptables, mais révèle l'existence et la date du projet (objection de E et F) ;
  - un dépôt confidentiel chez un tiers cache davantage, mais repose sur la confiance dans ce tiers.
- **V4** : canaris jamais publiés, soumis aux mêmes interrogations.
- **V5** : lot neuf issu du procédé scellé.

**Compte révisé.** Quatre duels gardent deux issues réfutantes (D1′, D2′, D3′a, D5′), soit huit. D3′b est probablement non jugeable et D4′ n'a qu'une issue. En III.1 j'annonçais douze issues : quatre ne tenaient pas.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

Aucun fait empirique : le bloc FAITS ne contient que l'énoncé. Tiennent seulement :

1. **Par l'énoncé (RAPPORTÉ)** : aucune mesure n'est faite, des travaux voisins paraissent, certaines mesures exigent une ignorance.
2. **Par logique** :
   - un texte antérieur aux résultats n'atteste qu'une intention et un plan ;
   - publier les éléments scellés avant la fin détruit les mesures qui en dépendent ;
   - une publication ne se retire pas et l'ignorance d'une personne ne se reconstitue pas, alors qu'attendre reste réversible.
3. **Par l'examen croisé** : ma règle D1 était contradictoire, D4 ne pouvait pas réfuter l'urgence, D5 ne testait pas ce qu'elle annonçait, et l'empreinte ne cache pas ses métadonnées. Ce sont des constats logiques et arithmétiques sur un plan, pas des résultats.

### Ce qui ne l'est pas

Tout ce qui suit reste une HYPOTHÈSE :

- Le texte candidat laisse-t-il deviner les éléments scellés, et le secret tient-il encore aujourd'hui ?
- Le dispositif résiste-t-il à un adversaire qui a lu le texte ou le mécanisme ?
- Un texte daté sans résultat procure-t-il du crédit, et autant qu'une empreinte ? Ce second point est probablement hors de portée d'un effectif réaliste.
- Quel est le signe de l'effet d'une note sur le devancement ? Il n'est pas identifiable sur un cas, et le taux de base ne l'est guère mieux.
- La critique publique trouve-t-elle plus que la relecture scellée ? Aucun plan transmis ne l'établit sans publier.
- « Le choix était-il le bon » n'est pas vérifiable. Seules le sont des prédictions écrites d'avance.

### Argument le plus fort pour chaque option

- **Publier avant** : un dispositif destiné à servir affrontera un adversaire informé. L'engagement public discipline aussi l'analyse avant la dépense.
- **Publier après** : c'est la seule option qui ne consomme rien d'irréversible avant d'avoir mesuré.
- **Ne rien publier** : si le dispositif ne vaut que contre un adversaire ignorant, tout texte en est le manuel d'évitement.

### Mon choix

Il est inchangé dans sa structure et corrigé dans ses appuis.

1. Engagement scellé du protocole complet, en sachant qu'il révèle une date, et peut-être une identité selon le registre.
2. Sans rien publier : D1′, D5′, puis D2′.
3. Texte public limité à la question, aux hypothèses et aux métriques, seulement si D1′ réfute la fuite à une résolution suffisante.
4. Mécanisme : après le bras naïf, ou avant si D2′ conclut à l'absence de baisse.
5. Éléments scellés : jamais avant la fin.

### Ce qui me ferait changer

- D1′ réfute l'innocuité après deux réécritures : engagement scellé seul.
- L'étape 1 de D1′ montre que les placebos devinent S : la contrainte d'ignorance ne tient déjà plus et l'argument de validité contre la publication tombe.
- D2′ conclut à l'absence de baisse, contrôle de manipulation réussi : le mécanisme peut précéder les mesures.
- D5′ conclut à une sensibilité insuffisante : le silence a un coût de qualité, ce qui plaide pour une exposition plus tôt.
- Des mesures existent déjà : l'engagement n'a plus valeur de préenregistrement pour elles.

Je ne fais plus dépendre le choix de D4, ni d'une équivalence entre empreinte et note.

### L'expérience à faire en premier

**L'étape 1 de D1′, sur modèles figés hors ligne : les contrôles avant le texte.** On mesure T∅ et les placebos contre le hasard, la clé leurre S′ et la gamme de fuites plantées.

- **Pourquoi elle** : elle ne publie rien et n'expose aucune personne. Elle coûte quelques heures de calcul. Elle conditionne tout le reste.
- **Première opposition** : le secret est devinable sans le texte, ou il ne l'est pas. La première issue réfute P4 et retire son objet au débat sur la fuite. La seconde réfute « le domaine public suffit déjà ».
- **Seconde opposition** : le test repère des fuites diffuses, ou seulement des fuites grossières. La seconde issue interdit tout verdict d'innocuité ultérieur. La première fixe la résolution à laquelle D1′ pourra conclure.

Tant que cette étape n'est pas faite, aucune affirmation sur la sûreté d'un texte public n'est permise, dans un sens comme dans l'autre.

FIN-DE-CELLULE