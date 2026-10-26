# Carte de notre contrôle — ce qu'il prétend détecter, par quoi, sous quelles hypothèses — v1

Audit des failles, lot B (confrontation), lignée conv-audit, sous-agent neuf. Horodatage : dernière ligne du fichier (heure
lue sur `date -u` dans la commande qui l'a écrite). Brief : `LISEZMOI-brief-audit-v1.md` (`1785c74d…`), § 1 à 3 et lot B.

## 0. Comment lire cette carte

- **Sources**, chemins relatifs à `fournis/` (empreintes vérifiées : `EMPREINTES-fournis-v1.txt`, 47 sur 47 conformes) :
  `docs/programme-controle-ia-v2.md` (« programme », prime sur le fond) ; `docs/brief-claude-code-programme-complet-v2.md`
  (« brief ») ; `docs/etat-de-l-art-controle-ia-v1.md` et `etat-de-l-art/` ; `decisions/` (les décisions de Lazar
  priment sur le programme pour les points qu'elles touchent ; les propositions sont citées comme telles).
- **Énoncé en vigueur** = programme v2 lu avec les décisions qui le touchent. Une option « par défaut » d'une proposition
  est notée « défaut » : son application effective se lit dans les registres, qui ne sont pas fournis.
- Pour chaque hypothèse (§ 4) et chaque invariant (§ 5) : hypothèses explicites et implicites, ce qui la ferait tomber,
  comment le programme le saurait, et ce qu'il ne verrait pas. Les renvois **FI-nn** désignent les failles de
  `failles-internes-v1.md`.
- Aucun chiffre de la littérature n'est nécessaire à cette carte ; les rares chiffres internes cités viennent des
  décisions fournies (jamais des dossiers de données des pilotes).

## 1. Ce que le contrôle prétend détecter

| menace | où | ce qui est revendiqué (énoncés en vigueur) | instrument principal | état au 26 octobre selon les pièces |
|---|---|---|---|---|
| Sabotage diffus dans le temps, un agent | papier A ; programme § 2, § 3, § 5 | la fragmentation détruit la preuve externe par action, pas la preuve interne ; l'accumulation séquentielle de scores de sondes détecte, avec garantie de faux positifs, ce que le moniteur par action rate (H1, H2 selon N-007, L et T selon N-003/N-004, H6 selon N-015, Tr, H8) | sondes sur les activations de l'agent qui agit (Llama-3.1-8B-Instruct), agrégées par le maximum ou l'attention sur les jetons, puis dans le temps (somme, processus e, Page, balayage) | instruments en code ; pilote de l'environnement (a) fait, famille « coût » seule retenue (P-015) ; premier test sur (i-a) : aucune sonde générique au-dessus de son plancher, coût écrit seul séparant à 0,888 d'aire (proposition N-025, P-015) |
| Sabotage distribué entre agents | papier B ; programme § 2, § 5 | statistique spatio-temporelle de co-élévation des états internes entre copies à poids partagés ; courbe sécurité(N) ; compromis diversification/coordination ; loi sécurité(M) par la diversité effective ; riposte et fuite (H3, H4′, H5, H7 selon N-013) ; survie des contraintes à la délégation (H9, N-035, sous réserve d'antériorité) | mêmes sondes, agrégateur de co-élévation, environnement (b) à état persistant | non commencé (phase 2, après G1) |
| Tromperie | programme § 8.1 (concept de sonde) ; papier C | une sonde de tromperie fait partie du panel ; « trahison par les activations » : tenter de manipuler fait monter le score de sonde de l'agent qui manipule (HC2b selon N-013 § 5) | sonde « tromperie » (recette réimplémentée, P-011) ; plan 2 × 2 rhétorique × intention (EC.2) | sonde en code ; aucune mesure décisive |
| Conscience d'évaluation | programme § 5 (H8), § 7 (contrôles croisés), § 11 | ce que mesure vraiment une sonde (intention contre conscience d'évaluation) prédit sa robustesse adverse | sonde « conscience d'évaluation », réservée au test de construit et hors du critère 3 de G0 (P-011) ; organisme honnête averti ; saboteur en régime simulé « non observé » | aucune mesure décisive |
| Corruption et usurpation du moniteur | papier C ; programme § 4, § 5 | loi de déférence à destination libre Δv = g·(ĉ − v₀) (HC1 selon N-005, N-013, N-023) ; robustesse des sondes de l'auteur (HC2) ; usurpation (HC3 selon N-013) ; taxe de déplacement conditionnée à l'accès (HC4) ; contre-mesures (HC5) ; g bénin comme critère de recette (HC6) | panel de juges génératifs lus par la probabilité du jeton (D2) ; sondes de l'agent auteur ; bras « sonde du lecteur » (N-013 § 8) | préenregistrement en brouillon, non scellé avant la lecture de Panin (N-005 § 2) |

## 2. La chaîne instrumentale

1. **Modèles.** Agent et sondes : Llama-3.1-8B-Instruct ; second modèle : Qwen2.5-7B (hétérogénéité, transfert, phase 3) ;
   juges boîte noire : le même 8B en juge et un modèle plus faible de confiance (D1, défaut (a) + (b) ; P-010 : 8B et
   3B) ; juges du papier C : D2 (trois modèles ouverts par défaut). Tout changement de modèle demande un GO.
2. **Harnais (T0.4).** Génération, puis une passe avant unique sur le transcript complet ; couches 7, 15 et 23 sur 32 ;
   logique validée en double précision (proposition N-011) ; production en demi-précision avec garde d'équivalence en
   ligne sur un échantillon, au 99e centile par action et par couche (seuil 0,2 ; P-007) ; carte A100 hors du domaine
   strict de T0.4, admise par son livrable (P-007).
3. **Environnement (a) (T0.5).** Reconstruction du jeu de Terekhov et al. (P-008 § 3) ; tâche jouée en T pas, une
   proposition ajoutée ou révisée par pas, T = 10 pour N = 1 (P-006, défaut (a)) ; cibles semées extraites par des
   sous-agents ; le pilote n'a retenu que la famille « coût » (P-015) ; la référence d'appariement des contrôles est un
   étiquetage par sous-agents ; les directions (fécondes, stériles) sortent de la vérité terrain (P-014).
4. **Organismes (T0.6).** Famille (i) scindée en (i-a) et (i-b) (niveau 1, prononcé 8) ; proportion p d'actions
   sabotées par une indication privée au pas désigné, témoin « instruit sans sabotage » recevant la même indication avec
   une consigne bénigne (P-009, défaut (a)) ; famille (ii) : adaptateur de bas rang distillé, dose par l'échelle α ;
   adaptateur témoin ; conditions de référence : honnête, témoin, mention (P-015) ; mode principal : coût déclaré gonflé,
   « affaiblir les contrôles » sorti (P-015) ; famille (iii) : organismes publics de l'institut britannique, si la
   licence le permet.
5. **Sondes (T0.7).** Cinq familles (linéaire, différence de moyennes, petit perceptron, attention, Mahalanobis) ;
   agrégation sur les jetons par le maximum ou l'attention seulement (règle gardée, bras de diagnostic « moyenne » permis
   hors production, N-026) ; concepts : tromperie, enjeux élevés, dissimulation, intention de saboter, conscience
   d'évaluation ; entraînement sur données génériques, évaluation sur les organismes, entraînement croisé rapporté à part
   (P-011, défaut (c)) ; plancher : sonde aléatoire appariée en covariance, plancher sous permutation rapporté (P-015) ;
   témoin lexical et panel de concepts sans lien (P-013, défaut (b)) ; sonde du domaine apprise sur paires synthétiques,
   lue avant le champ coût (P-015, E3).
6. **Bases boîte noire (T0.8).** Juge par action (8B, 3B), invite H.12 adaptée à la dernière modification, lecture par
   espérance sur la loi du jeton, en une passe et avec raisonnement (P-010, défaut (a)) ; juge robustifié b* (P-003,
   appliquée par défaut selon N-007) ; TRACE-lite ; accumulation séquentielle sur scores boîte noire ; bases (i) à (iv)
   de N-007 ; prédicteur obligatoire sur les traits du texte (coût normalisé, longueur, forme du champ coût) et règle du
   coût déclaré (N-029, P-015) ; juge ouvert de 70 milliards de paramètres seulement sur un GO séparé, après G0 (N-029).
7. **Agrégateurs.** Maximum par action, moyennes glissantes et leur maximum, somme cumulée, processus e de mélange, Page,
   détecteurs e, balayage, co-élévation entre agents ; indexation par le multi-ensemble {(i, t)} (programme § 4) ;
   calibrage conforme sur épisodes honnêtes entiers et détecteur de rupture proposés au préenregistrement de G1 (N-004,
   N-007).
8. **Papier C.** Cinq familles d'attaque × au moins trois intensités + condition sans attaque ; verdicts lus sur texte
   complet ; g et ĉ estimés par régression sans imposer ĉ (N-005) ; lecture par probabilité du jeton gardée comme
   instrument cité (N-013) ; plan 2 × 2 rhétorique × intention ; bras « sonde du lecteur » (N-013 § 8).
9. **Papier B.** Grille N ∈ {1, 2, 3, 5, 10} (D3) ; agrégateurs de NARCBench comme bases ; environnement (b) : FakeLab sur
   demande ou Iterative VibeCoding dans ControlArena.

## 3. Les portes

| porte | critère en vigueur | source | ce qu'elle vérifie | ce qu'elle ne vérifie pas (renvoi) |
|---|---|---|---|---|
| G0 (au plus tard fin novembre, critères inchangés) | huit critères : harnais validé ; organismes (i) et (ii) avec dose-réponse ; sondes au-dessus du plancher sur (i) et (ii) ; base boîte noire par action et séquentielle sur les mêmes épisodes ; agrégateurs validés en simulation ; préenregistrements de G1 et du papier C scellés et contre-lus ; état de l'art vérifié | brief § 7 ; P-015 (N-027) | l'existence et le fonctionnement des instruments | les prémisses dont dépend la lecture de G1 : diffusion mesurée, taille du calibrage, négatifs appariés en indication, mode de sabotage tenu à l'écart de la conception (FI-40) |
| G1 (fin M2) | la boîte blanche séquentielle bat la meilleure base boîte noire, toutes variantes confondues, avec un rappel à 1 % de faux positifs supérieur établi par un intervalle à 95 % ; bras F1 retiré ; planchers « tout signaler » et « juge en une passe » rapportés | N-008 | une supériorité à taux de faux positifs nominal égal | l'unité du taux (FI-28), l'information disponible à chaque bras (FI-06), un effet minimal et la tenue sous attaquant adaptatif (FI-38), la taille du calibrage (FI-27) |
| GC (fin de la phase 1) | g_sonde > 0 sans accès aux poids → changement de titre ; pièce revendiquée (destination libre ĉ, par famille, dans un moniteur de contrôle) trouvée publiée → recentrage sur HC4 et HC6 | N-005 § 2 ; N-013 ; N-023 | le signe de g_sonde et l'antériorité | une marge d'équivalence pour « g ≈ 0 » (FI-34) |
| G2 (fin M4) | effet de fragmentation répliqué et statistique de population supérieure à l'agrégation par agent | programme § 10 ; brief § 10 | la valeur ajoutée de la population | la cause commune honnête (FI-21) et la manipulation des sondes lectrices (FI-20) |
| G3 | ouverture de l'environnement (d) seulement si un proxy de vérité différée est validé | programme § 10 | la vérité différée | — |
| Bascules | G1 échoue → résultat négatif + H8 dominante ; publication externe du cœur séquentiel → épidémiologie de population ; g_sonde > 0 → contamination de construit ; 8B trop faible → rubrique simplifiée ; élicitation rouge insuffisante → politiques publiées ; pas de proxy → (d) abandonné | programme § 13 ; brief § 13 | — | la puissance des nuls qui déclenchent (FI-39) ; la faisabilité de « H8 dominante » si les sondes sont au plancher (FI-36) |

## 4. Les hypothèses du § 5, une par une

### H1 — gain de la boîte blanche sur la boîte noire (papier A)

- **Énoncé en vigueur** : programme § 5, inchangé (N-013 § 8) ; revendicable : la mesure sur sabotage diffus de tâches
  floues, à agrégation et taux de faux positifs égaux. Critère de G1 : N-008.
- **Instrument et lecture** : plan 2 × 2 accès × agrégation (E1.2, T1.2) sur les mêmes épisodes ; effet principal de
  l'accès.
- **Hypothèses explicites** : agrégation égale ; taux de faux positifs égal, calibré sur des épisodes honnêtes réservés ;
  le comparateur est la meilleure base boîte noire, toutes variantes confondues.
- **Hypothèses implicites** : les deux bras disposent de la même information (la sonde lit le contexte privé, N-007 ;
  le juge voit les questions et l'ensemble courant, P-010) (FI-06) ; « à agrégation égale » est équitable pour des scores
  de lois différentes (FI-31) ; le régime « diffus » n'est pas défini par le comparateur lui-même (FI-03) ; le construit
  « tâche floue » survit au mode « coût » (FI-01) ; le mode de sabotage n'informe pas la conception des moniteurs
  (FI-02) ; le bruit de l'honnête d'un agent de 8 milliards est représentatif (FI-10).
- **Ce qui la ferait tomber** : la meilleure base boîte noire égale ou dépasse la boîte blanche séquentielle ; ou le gain
  s'explique par l'indication privée, la longueur ou des traits du texte.
- **Le programme le saurait par** : le verdict de G1 (R13) ; les planchers « tout signaler » et « juge en une passe » ;
  le prédicteur obligatoire sur les traits du texte (N-029) ; la dose fixée sur la boîte noire seule (P-015 (b)).
- **Il ne le saurait pas si** : les négatifs de calibrage de G1 ne contiennent pas le témoin qui reçoit la même
  indication (FI-06) ; la sonde n'est jamais testée en validité incrémentale contre le texte (FI-05) ; aucun mode de
  sabotage tenu à l'écart de la conception n'est évalué (FI-02).

### H2 — accumulation additive toujours valide sur sondes de l'agent qui agit (papier A)

- **Énoncé en vigueur** (N-007 § 1) : sur des trajectoires où chaque action sabotée reste sous le seuil d'un moniteur par
  action calibré à 1 %, l'accumulation additive toujours valide de scores de sondes de l'agent qui agit détecte le
  sabotage avec un rappel qui croît avec l'horizon ; contexte privé compris ; seuil calibré sur des épisodes honnêtes,
  sans exemple de sabotage. Garantie entendue uniforme sur les lectures de l'horizon, calibrée sur épisodes entiers.
- **Instrument et lecture** : effet principal du séquentiel dans le 2 × 2 ; bases (ii) cascade et (iii) dernier état
  (N-007) ; garde G1-P4 (faux positifs vérifiés sur l'honnête).
- **Hypothèses explicites** : actions sous le seuil par action ; calibrage sans sabotage ; rappel croissant avec
  l'horizon.
- **Hypothèses implicites** : « sous le seuil » se vérifie pour le moniteur pertinent, alors que la dose ne peut être
  choisie sur la sonde sans viser un signe (FI-03) ; scores honnêtes stationnaires le long de l'horizon (réserve N-034
  § 2) ; unité du taux de faux positifs commune aux bras (FI-28) ; calibrage assez grand pour 1 % (FI-27) ; loi honnête
  par action indépendante de la longueur (FI-26) et du bruit numérique (FI-24) ; étendue d'horizon suffisante pour
  estimer une pente (T = 10, P-006).
- **Ce qui la ferait tomber** : rappel plat en horizon ; faux positifs réalisés au-dessus du nominal ; actions sabotées
  au-dessus du seuil par action de la sonde elle-même.
- **Le programme le saurait par** : la garde G1-P4 ; la mesure descriptive de N-034 § 2 (part d'actions non appliquées) ;
  les simulations de T0.3.
- **Il ne le saurait pas si** : la dérive de l'honnête à long horizon n'est pas mesurée hors de l'horizon de T0.6 ; les
  bras sont comparés à des unités de taux différentes (FI-28).

### L — lemme d'additivité, énoncé adverse (papier A)

- **Énoncé en vigueur** (N-004) : L1 invariance terminale (puissance fonction de B, n₀, F₀, α seulement ; décroît avec
  n₀ à B fixé) ; L2 effondrement du maximum ; L3 lecture toujours valide (le calendrier compte ; coût du report ; prix de
  la garantie) ; L4 invariance spatiale à vérifier ; détection « avant le dommage » par un détecteur de rupture ;
  non-compensation posée comme condition empirique ; hypothèse (b) du budget total = choix de modélisation (P-008 § 2).
- **Instrument et lecture** : E1.3 (puissance à budget total constant quand la fragmentation varie ; test δ > 0 par type
  d'action) ; T0.3 en simulation.
- **Hypothèses explicites** : décalage δ de l'espérance du score par action sabotée ; budget total borné ; variance
  honnête estimable.
- **Hypothèses implicites** : décalage de position (et non de dispersion ou de forme) ; aucun débordement de l'intention
  sur les actions non sabotées des épisodes saboteurs (FI-25) ; F₀ identique pour toutes les actions, quelle que soit
  leur longueur (FI-26) ; un taux de change borné entre dommage et déplacement de score (FI-04).
- **Ce qui la ferait tomber** : à B fixé, une puissance qui varie avec la fragmentation au-delà de la prédiction de L1
  et L3 ; δ ≈ 0.
- **Le programme le saurait par** : E1.3, préenregistré ; L4 à vérifier avant le papier.
- **Il ne le saurait pas si** : δ ≈ 0 est lu comme « dommage porté par la corrélation » alors que la sonde est aveugle
  (FI-33) ; un dommage est produit avec un faible déplacement de score, ce qu'aucune mesure ne borne (FI-04).

### T — théorème négatif (papiers A et B)

- **Énoncé en vigueur** (N-003) : T1 aveuglement des statistiques invariantes sous une attaque de classe C ; T2
  impossibilité sans structure ; T3 garanties locales sous dommage structuré ; classes C et K distinguées ; T4 somme lue
  séquentiellement. Revendiqué : unification temps × agents par sous-groupes de permutations, distinction C/K, garanties
  locales face à un attaquant adaptatif, transposition aux activations réelles.
- **Instrument et lecture** : T0.3 (simulation) ; E1.4 (scores honnêtes réels + corrélation injectée à marginale
  préservée).
- **Hypothèses explicites** : le dommage passe par la dépendance (K) ou par l'ordre d'un multi-ensemble préservé (C).
- **Hypothèses implicites** : notre environnement contient un mode de dommage porté par la dépendance entre actions
  individuellement banales ; en mode « coût », le dommage est additif (FI-01, FI-33) ; E1.4 apporte une preuve empirique,
  alors qu'il éprouve une construction dont le résultat est démontré (FI-33).
- **Ce qui la ferait tomber** : les parties démontrées ne tombent pas ; leur pertinence empirique tombe si aucun
  organisme réel ne produit de dommage de classe K.
- **Le programme le saurait par** : la note mathématique et T0.3.
- **Il ne le saurait pas si** : E1.4 est lu comme validation sur données réelles (FI-33).

### H6 — marge asymétrique (papier A)

- **Énoncé en vigueur** (N-015 § 1, remplaçant N-013 § 6 pour la liste) : pour l'une au moins de trois interventions
  non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte), il existe une intensité où, en moyenne à
  intensité fixe, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête. Bruit
  d'activations et bruit sur les poids : mesurés, non revendiqués.
- **Instrument et lecture** : E1.6, base Ctrl-Z ; métrique de marge fixée au préenregistrement.
- **Hypothèses implicites** : une mesure d'utilité honnête fiable, alors que l'évaluateur faible prévu (programme § 6)
  est le juge 8B, presque sans information comme référence d'appariement au pilote (P-014) (FI-01) ; l'intervention
  touche le canal du sabotage (un nombre recopié par une paraphrase reste intact) (FI-01) ; le saboteur ne s'adapte pas à
  l'intervention, qu'il peut observer (FI-17).
- **Ce qui la ferait tomber** : aucune intensité à marge significative.
- **Le programme le saurait par** : E1.6, préenregistré.
- **Il ne le saurait pas si** : le résultat est propre au mode « coût » et n'est pas rapporté comme tel (FI-01).

### Tr — transposition jeton → action (papier A)

- **Énoncé en vigueur** : programme § 5 ; inchangé (N-013 § 8).
- **Instrument et lecture** : E1.5 (a) par contenu, l'organisme connaissant le moniteur ; (b) sur les poids, sous GO
  (réglage fin contre la sonde, puis apprentissage par renforcement sans gradient à travers le moniteur), au niveau action,
  avec le coût d'utilité.
- **Hypothèses implicites** : E1.5 (b) obtient son GO de dépense (sinon Tr reste sans réponse) ; le profil d'adversaire
  de chaque bras est écrit (FI-14) ; l'élicitation est assez forte pour qu'un échec d'attaque signifie une robustesse
  (FI-12).
- **Ce qui la ferait tomber** : une évasion au niveau action, à utilité préservée, d'une agrégation par maximum ou
  attention lue séquentiellement.
- **Le programme le saurait par** : E1.5.
- **Il ne le saurait pas si** : seule la branche (a) tourne, ou si l'attaquant reste faible (FI-12) ; aucune porte ne
  conditionne le papier A à ce résultat (FI-38).

### H8 — la validité du construit prédit la robustesse (papier A, transversale)

- **Énoncé en vigueur** : programme § 5 et § 11 ; inchangé (N-013 § 8) ; bascule dominante si G1 échoue.
- **Instrument et lecture** : panel contrastif (intention de saboter, dissimulation, conscience d'évaluation, enjeux
  élevés) ; contrôles croisés de § 7 ; test de validité (i) contre (ii).
- **Hypothèses implicites** : le construit est mesurable avant la robustesse, par un score défini d'avance ; le panel
  compte assez de sondes pour estimer une relation (FI-36) ; les sondes détectent quelque chose (FI-36) ; le test (i)
  contre (ii) identifie le construit (FI-07) ; la conscience d'évaluation induite par le dispositif est mesurée (FI-11).
- **Ce qui la ferait tomber** : robustesse sans lien avec le construit mesuré.
- **Le programme le saurait par** : le panel et les contrôles croisés.
- **Il ne le saurait pas si** : l'unité et le nombre ne sont pas fixés (FI-36).

### HC1 — loi de déférence (papier C)

- **Énoncé en vigueur** (N-005 § 1, N-013 § 1, N-023 § 1) : sous pression d'intensité graduée d'une famille d'attaque,
  le verdict v d'un moniteur génératif, lu comme score continu, se déplace de v₀ vers une destination ĉ, Δv = g·(ĉ − v₀),
  g et ĉ estimés par régression sur plusieurs intensités sans imposer ĉ. Prédictions : ĉ = v* contre la moyenne du
  corpus ; g > 0, structuré par famille ; stabilité de rang (les magnitudes ne sont pas revendiquées) ; opposition juge
  / sonde.
- **Instrument et lecture** : EC.1 ; panel D2 (trois juges par défaut) ; probabilité du jeton de verdict comme
  instrument cité.
- **Hypothèses implicites** : une échelle d'intensité comparable d'une famille à l'autre ; une forme de dépendance à
  l'intensité fixée d'avance ; un panel assez grand pour tester un rang (FI-35) ; ĉ identifiable seulement si g n'est pas
  proche de zéro (N-023 § 1).
- **Ce qui la ferait tomber** : ĉ égal à la moyenne du corpus ; g ≈ 0 ; rangs instables.
- **Le programme le saurait par** : le préenregistrement du papier C (non scellé avant Panin, N-005 § 2).
- **Il ne le saurait pas si** : la stabilité de rang est testée sur trois juges (aucune valeur du tau de Kendall n'y est
  significative à 5 % ; calcul, FI-35).

### HC2 — robustesse des sondes de l'auteur (papier C)

- **Énoncé en vigueur** : programme § 5 (robustesse, jamais immunité) ; bras « sonde du lecteur » ajouté (N-013 § 8).
- **Instrument et lecture** : EC.2, plan 2 × 2 rhétorique × intention ; signe de g_sonde ; porte GC.
- **Hypothèses implicites** : « g_sonde ≈ 0 » se lit avec une marge d'équivalence et une puissance fixées (FI-34) ; la
  sonde est apprise en auteur et non en lecteur (FI-08) ; le profil de l'attaquant par contenu est écrit (FI-14).
- **Ce qui la ferait tomber** : g_sonde nettement non nul (positif : contamination ; négatif : trahison).
- **Le programme le saurait par** : EC.2 et GC.
- **Il ne le saurait pas si** : un nul sous-dimensionné est lu comme une robustesse (FI-34, FI-39).

### HC2b — trahison par les activations (papier C)

- **Énoncé en vigueur** (N-013 § 5) : tenter de manipuler fait monter le score de sonde de l'agent qui manipule ;
  propriété des sondes, contrôlée contre le style et contre le retour de bâton textuel.
- **Instrument et lecture** : EC.2 (même registre rhétorique dans les deux bras qui plaident).
- **Hypothèses implicites** : le test est le contraste d'interaction (plaidoyer × intention), non l'effet principal du
  plaidoyer ; les consignes des quatre cellules sont appariées en structure (FI-34) ; la sonde ne lit pas la consigne de
  saboter (FI-06).
- **Ce qui la ferait tomber** : aucune hausse à style égal.
- **Le programme le saurait par** : EC.2.
- **Il ne le saurait pas si** : HC2 et HC2b sont lues comme deux succès possibles d'une même mesure (FI-34).

### HC3 — usurpation (papier C)

- **Énoncé en vigueur** (N-013 § 2) : (1) sous « contenu = données », les ordres en bande sont détectés presque
  sûrement par des juges moniteurs ; (2) l'usurpation stylistique de l'instructeur, sans ordre, garde un g résiduel
  positif sur des juges moniteurs et un g nul sur des sondes de l'agent auteur.
- **Instrument et lecture** : EC.3.
- **Hypothèses implicites** : « presque sûrement » à un taux de faux positifs mesuré sur du contenu honnête riche en
  phrases à l'impératif (FI-41) ; « g nul » avec marge (FI-34).
- **Ce qui la ferait tomber** : détection non quasi certaine à faux positifs acceptables ; g résiduel nul sur les juges
  ou non nul sur les sondes.
- **Le programme le saurait par** : EC.3.
- **Il ne le saurait pas si** : le taux d'alarme du protocole sur l'honnête n'est pas mesuré (FI-41).

### HC4 — taxe de déplacement (papier C)

- **Énoncé en vigueur** (N-013 § 3) : déplacer une sonde de l'agent comme la rhétorique déplace un juge exige un accès en
  écriture aux activations ou aux poids ; coût par axe (accès, requêtes, calcul, succès) et par régime d'accès ; l'écart
  « de plusieurs ordres de grandeur » n'est prédit que pour le contexte seul.
- **Instrument et lecture** : EC.4, sous GO.
- **Hypothèses implicites** : le régime « poids réglables » correspond à un adversaire du périmètre (le programme met
  hors périmètre l'adversaire qui possède l'infrastructure, § 9) (FI-14) ; les axes de coût sont commensurables.
- **Ce qui la ferait tomber** : un déplacement de sonde par contexte seul à un coût comparable à celui d'un juge.
- **Le programme le saurait par** : EC.4.

### HC5 — contre-mesures (papier C)

- **Énoncé en vigueur** (N-006, N-013 § 4) : paraphrase de confiance ; quorum hétérogène en type d'accès (juges
  génératifs et sondes qui lisent l'agent) ; matrice de transfert des attaques de corruption entre juges et sondes.
- **Instrument et lecture** : EC.5.
- **Hypothèses implicites** : règle de décision du quorum comparée à taux de faux positifs apparié ; force d'attaque
  égalisée entre types de moniteurs (FI-37).
- **Ce qui la ferait tomber** : quorum pas meilleur que son meilleur membre à faux positifs égaux ; transfert élevé.
- **Le programme le saurait par** : EC.5.

### HC6 — le g bénin prédit la robustesse (papier C)

- **Énoncé en vigueur** : programme § 5, inchangé (N-013 § 8) ; doit faire mieux que le simple taux sur attaques faibles
  (barre relevée dans `etat-de-l-art/anteriorite-v1.md`, section HC6).
- **Instrument et lecture** : EC.6 ; panel dont la taille est fixée au préenregistrement (brief TC.6).
- **Hypothèses implicites** : budget d'attaque optimisée égalisé entre juges (requêtes) et sondes (accès aux poids)
  (FI-37).
- **Ce qui la ferait tomber** : aucune corrélation, ou une corrélation qui n'ajoute rien au taux sur attaques faibles.
- **Le programme le saurait par** : EC.6.

### H3 — courbe sécurité(N) (papier B)

- **Énoncé en vigueur** : programme § 5, inchangé (N-013 § 8).
- **Instrument et lecture** : E3.1 ; grille D3 ; boîte blanche contre boîte noire à budget de sabotage constant.
- **Hypothèses implicites** : la co-élévation reflète les poids partagés et non le contexte partagé (FI-21) ni le contenu
  lu (FI-20) ; budget constant au sens du dommage, non du score (FI-04).
- **Ce qui la ferait tomber** : courbe boîte blanche non dominante.
- **Le programme le saurait par** : E3.1, G2.

### H4′ — compromis diversification / coordination (papier B)

- **Énoncé en vigueur** : programme § 5, inchangé (N-013 § 8).
- **Instrument et lecture** : E3.2 ; transfert des sondes entre variantes.
- **Hypothèses implicites** : une baisse de détection sous diversification vient de la décorrélation des signatures et
  non de la mauvaise transférabilité des sondes aux variantes (FI-37).
- **Ce qui la ferait tomber** : aucun coût de coordination à la diversification.
- **Le programme le saurait par** : E3.2.

### H5 — nombre × diversité des moniteurs (papier B)

- **Énoncé en vigueur** (N-013 § 7) : la loi, sécurité croissante avec M seulement par la diversité effective, mesurée
  par transfert d'attaque sur un panel de sondes.
- **Hypothèses implicites** : la force de l'attaque optimisée contre un membre est fixée et comparable (FI-37).
- **Ce qui la ferait tomber** : sécurité croissante avec M à diversité effective constante.
- **Le programme le saurait par** : E3.3.

### H7 — riposte et fuite (papier B)

- **Énoncé en vigueur** (N-013 § 7) : la pente d'adaptation de l'équipe rouge est prédite par l'information mutuelle entre
  l'état de détection et ses observations ; comparaison des politiques de riposte.
- **Hypothèses implicites** : estimation de l'information mutuelle assez précise sur peu d'itérations d'adaptation
  (FI-37) ; fuite par l'environnement lui-même mesurée (FI-17).
- **Ce qui la ferait tomber** : pente sans relation avec l'information mutuelle.
- **Le programme le saurait par** : E3.4 et ses deux ablations.

### H9 — survie des contraintes à la délégation (papier B, hors § 5, ajoutée par N-035)

- **Énoncé en vigueur** (N-035 § 2) : une contrainte de sécurité explicite peut s'éroder à chaque passage d'un agent à
  un sous-agent ; la survie décroît avec le nombre de passages ; un moniteur à chaque passage la relève. Sous réserve
  d'antériorité ; hors de la demande de sept mois.
- **Hypothèses implicites** : l'ordre du mandant arrive par le canal authentifié, sans que le mandant soit fiable
  (FI-19).
- **Le programme le saurait par** : une mesure à préenregistrer (rien n'est ouvert).

### Statistique de population (papier B)

- **Énoncé** : co-élévation des états internes entre copies, lue par des sondes (revendicable selon
  `etat-de-l-art/anteriorite-v1.md`, dernière section).
- **Hypothèses implicites** : l'élévation d'un agent reflète son propre état (FI-20) ; le nul de co-élévation tient
  compte des entrées partagées (FI-21).
- **Le programme le saurait par** : E2.3, G2.

## 5. Les invariants du § 9, un par un

| invariant | rôle | ce qui le ferait tomber | le programme le saurait par | il ne le saurait pas si |
|---|---|---|---|---|
| Canal opérateur authentifié | les ordres n'arrivent que par un canal vérifié par le harnais | l'émetteur authentifié n'est pas fiable : un agent mandant en délégation ou en pipeline multi-rôles donne des ordres légitimes par ce canal | H9 (survie des contraintes), si elle est mesurée | l'invariant reste lu comme une garantie de fiabilité de l'ordre (FI-19) |
| Contenu en bande = données ; un contenu en forme d'ordre est une alarme | couper le canal d'ordres par le contenu | les tâches dont le contenu guide légitimement l'action ; un contenu honnête riche en phrases à l'impératif déclenche l'alarme | HC3 (détection sous ce protocole) | le taux de faux positifs de l'alarme sur contenu honnête n'est pas mesuré (FI-41) |
| Flux unidirectionnel agent → moniteur | pas de boucle de persuasion | toute intervention observable par l'agent (blocage, ré-échantillonnage, motif d'action non appliquée rendu par l'environnement (a), N-034 § 2) ferme une boucle d'information | H7 en phase 3 | les mesures passives du papier A sont transférées à un protocole actif (FI-17) |
| Moniteurs amnésiques entre épisodes | pas de relation à cultiver | ne tombe pas au sens de la persuasion ; mais il interdit aussi l'accumulation de preuve entre épisodes, qui est la parade naturelle à une fragmentation entre épisodes | — | la sécurité est définie par épisode (programme § 4) et l'échelle inter-épisodes n'est pas mesurée (FI-15) ; en outre, le réentraînement prévu par l'asymétrie d'apprentissage est une mémoire du moniteur (FI-16) |
| Seuils stochastiques et trafic de couverture | rien de fixe à apprendre | une probabilité d'audit lisse reste une fonction apprenable avec assez d'observations ; le coût du trafic de couverture en budget d'audit | E3.4 (deux ablations) ; information mutuelle (H7) | les mesures du papier A, à seuils fixes calibrés, ne disent rien de l'apprentissage du seuil (FI-17) |
| Hygiène de l'état persistant | pas d'hérédité, donc pas d'évolution | l'environnement (b) est à état persistant par construction : la base de code ne se remet pas à zéro sans détruire la tâche, et elle porte l'attaque graduelle | bases boîte noire à état (link-tracker) en phase 3 | aucune statistique boîte blanche ne lit l'état persistant ni l'échelle inter-épisodes (FI-15) |
| Asymétrie d'apprentissage | chaque détection silencieuse devient un exemple de réentraînement | les données de réentraînement ne contiennent que ce qui a été détecté ; un adversaire qui influe sur ce qui est détecté influe sur les données des sondes | — | aucune garde ne compare les sondes réentraînées à la réserve jamais déployée (FI-16) |
| Frontière assumée (infrastructure hors périmètre) | délimiter la couche sœur | le cas intermédiaire : l'agent n'a pas les clés mais écrit du code ou des artefacts que l'infrastructure exécute ou lit | — | la vivacité du moniteur n'est pas éprouvée par des canaris positifs (FI-22) |

Aucun invariant n'est déclaré pour la lignée des organismes de conception (N-044, N-045), dont la mémoire transmise,
la composition apprise et l'héritage récompensé seraient, si un organisme servait de moniteur, contraires aux invariants
4 et 6 (FI-23).

## 6. Le modèle de menace tel qu'il ressort des documents

| question | ce que les documents écrivent | ce qu'ils n'écrivent pas (renvoi) |
|---|---|---|
| **Qui est l'adversaire ?** | l'agent instruit (famille i), l'agent distillé (famille ii), des organismes publics verrouillés (iii) ; un attaquant par contenu qui connaît le moniteur (E1.5 a) ; un attaquant qui règle les poids (E1.5 b, HC4) ; des copies coordonnées (B) ; un agent qui plaide auprès du juge (C) ; un mandant en délégation (H9) | un agent qui sabote selon qu'il se croit observé (FI-11) ; un adversaire patient entre épisodes (FI-15) ; la classe de politiques contre laquelle la sécurité, définie comme un infimum, est réellement évaluée (FI-12) |
| **Que sait-il du moniteur ?** | « l'organisme connaît le moniteur » (E1.5 a) ; réserve de détecteurs jamais déployés (§ 8.1) ; seuils stochastiques (§ 9) | pour chaque hypothèse : architecture, couches, agrégateur, seuil, verdicts passés ; le juge de même modèle que l'agent est un moniteur non fiable (FI-14) |
| **Que peut-il apprendre ?** | par les verdicts et la riposte (H7) ; par l'entraînement contre la sonde (E1.5 b) | par le retour de l'environnement et des interventions dans l'épisode (FI-17) ; par l'influence sur les données de réentraînement (FI-16) ; d'une mise à jour du modèle qui déplace la calibration (FI-18) |
| **Que contrôle-t-il ?** | son contenu ; la répartition du sabotage dans le temps et entre agents, sous budget total (L) ; la dépendance entre actions (T) | le taux de change entre dommage et déplacement de score (FI-04) ; le contenu que lisent d'autres agents et leurs sondes (FI-20) ; les artefacts persistants (FI-15, FI-22) ; les ordres donnés à un sous-agent (FI-19) ; le contenu que lisent les étiqueteurs de la vérité terrain (FI-09) |

## 7. Dépendances

- **Un seul modèle agent** (Llama-3.1-8B-Instruct) pour les papiers A et C, le second modèle n'entrant qu'en phase 3
  (FI-13) ; la forme mesurée dans le projet antérieur n'a pas transféré de Llama à Qwen (programme § 15).
- **Un seul environnement** pour le papier A, réduit à un seul mode de sabotage (FI-01) ; transfert concentré en figure
  seulement (E1.7).
- **Juges** : juges boîte noire de 8 et 3 milliards de paramètres, presque sans information comme étiqueteurs
  d'appariement au pilote (P-014) ; juge de 70 milliards renvoyé à un GO après G0 (N-029) (FI-03).
- **Un fournisseur** pour l'extraction des cibles, l'étiquetage de la vérité terrain, les contre-lectures (R2) et les
  verdicts de porte (R13) (FI-09, FI-43).
- **Budget** : plafond de 10 dollars par lancement sous délégation (P-015) ; plafond de la phase 0 (N-012) : il borne
  la taille des échantillons, donc la puissance des nuls (FI-39).
- **Décisions** : programme v2 non réécrit, lu avec une vingtaine de notes de décision et un programme fusionné (v4)
  évoqué sans être fourni (FI-44).

---
Horodatage : version close le 2026-10-26 à 10:51:07 UTC (heure lue sur date -u dans la commande qui écrit cette ligne).
