# Proposition A, tour III.1

**Pièces.** FAITS et QUESTION sont reçues entières. Les faits ne portent pas d'étiquette de statut individuelle : je les cite « selon les faits » sans en élever aucun au rang de VÉRIFIÉ. La conviction du directeur (« pense ») est une HYPOTHÈSE. Aucune autre proposition ne m'est transmise, donc B1 est sans objet. Tout ce que je propose est HYPOTHÈSE. Règle 3 : je ne donne aucun identifiant arXiv, n'en ayant que de mémoire.

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut |
|---|---|---|
| S1 | Une percée est atteignable « en employant au maximum les meilleurs modèles ». Seul taux donné par les faits : un modèle sur cinq, deux problèmes sur soixante-huit, à 300 dollars, en mathématiques. | HYPOTHÈSE (du directeur) |
| S2 | La méthode du résultat zêta se transpose au contrôle. Elle s'appuyait sur une preuve relisible ; le contrôle n'a pas d'évaluateur exact donné d'avance. | HYPOTHÈSE |
| S3 | Les organismes saboteurs construits représentent la menace visée. Un moniteur peut ne détecter que la trace de leur construction. | HYPOTHÈSE, non testée d'après les faits |
| S4 | Un mode tenu à l'écart mesure la généralisation. Un seul mode ne donne qu'un point, donc aucune variance entre familles. | HYPOTHÈSE |
| S5 | « 1 % de fausses alertes » est bien défini. Il manque l'unité (pas, trajectoire, déploiement) et la population honnête de référence. | Non établi |
| S6 | « Remarquée » est un critère observable. | Non établi ; je le fixe en section 1 |
| S7 | Le goulot est l'idéation. Il peut être la vérification. | HYPOTHÈSE ; le duel E4 la teste |

## 1. Ce qu'un expert ferait sans qu'on le demande, et ce qu'est une « percée remarquée »

**Ce qu'il ferait d'abord (proposition) :**

- **Auditer l'instrument avant de chercher.** À 1 % de fausses alertes, le seuil repose sur le centième supérieur des cas honnêtes. Avec 10 000 cas honnêtes, l'erreur type binomiale sur ce 1 % est d'environ 0,1 point (calcul illustratif). En dessous de quelques milliers de cas, deux moniteurs ne sont pas comparables.
- **Changer l'unité de généralisation.** Ce qui compte est le nombre de familles de sabotage indépendantes, dont certaines conçues hors programme, pas le nombre d'échantillons.
- **Prendre les erreurs honnêtes comme négatifs durs.** Le problème central est de distinguer sabotage et incompétence honnête, pas sabotage et travail propre.
- **Mesurer un risque sous protocole, pas un score de détection.** Cela veut dire : budget d'audit fixé, équipe rouge qui connaît la défense, utilité conservée. C'est le cadre de Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*.
- **Lire le cas zêta pour ce qu'il dit.** Selon les faits, l'attaque de front a été stérile et le résultat est venu d'un agent lancé sur une autre question. Cela plaide pour la largeur, à condition d'avoir une vérification bon marché et sûre. En contrôle, ce vérificateur reste à construire : ce sont les mondes plantés.
- **Compter le taux de base.** Deux sur soixante-huit pour un modèle, zéro pour les quatre autres, n'autorise pas à promettre un résultat. Le portefeuille doit rendre publiables les issues négatives.

**« Percée remarquée » : définition proposée, à fixer avant de chercher.** Un résultat est remarqué si des tiers changent leur pratique. Trois formes observables :

1. Un protocole qui déplace la frontière sûreté-utilité sur un banc public, face à une équipe rouge adaptative externe, et qu'un tiers réplique.
2. Un résultat négatif qui fait tomber une classe de défenses sur laquelle on s'appuie. Précédent en robustesse adversariale : Athalye, Carlini, Wagner (2018), *Obfuscated Gradients Give a False Sense of Security*.
3. Un instrument de mesure, banc ou borne, que d'autres adoptent.

Ceux qui remarquent sont les équipes de contrôle des laboratoires et les instituts d'évaluation. Ils le montrent par la réplication, la réutilisation ou l'intégration dans un argumentaire de sûreté. Je ne sais pas prédire l'attention ; je sais seulement dire ce qui la rend vérifiable.

## 2. Données brutes de départ

- Trajectoires **appariées** honnête/saboteur : même tâche, même modèle de base, mêmes graines, avec activations et scores bruts de chaque moniteur, pas des résumés.
- **Erreurs honnêtes** étiquetées : tâches ratées sans intention.
- **Organismes placebo** : même procédure de construction, objectif bénin.
- **Effet aval** de chaque sabotage : la conclusion de recherche a-t-elle basculé ? Vérité tenue hors machine, comme l'étage de tests de mort.
- **Mémoire des tentatives** de l'organisme d'idéation : taux d'idées tuées et causes de mort. C'est son propre taux de base.
- Étiquettes d'audit humain avec accord inter-annotateurs.
- Tâches réelles non plantées, pour mesurer si une tâche plantée s'en distingue.
- Transcriptions de bancs publics de sabotage : Kutasov et al. (2025), *SHADE-Arena* (référence à vérifier) ; Benton et al. (2024), *Sabotage Evaluations for Frontier Models*.

## 3. Méthodes et outils : ce que chacun suppose, comment il échoue, mesure minimale (livrable c)

| Instrument | Suppose | Échoue quand | Mesure minimale ; vérification mécanique à battre |
|---|---|---|---|
| **Flottes d'agents chercheurs** | Idéation limitante ; erreurs décorrélées entre lignées ; vérification bon marché | Erreurs corrélées ; chemins d'analyse multiples ; fuite du mode tenu à l'écart par la mémoire | Sur mondes plantés : rappel des effets plantés et taux de « découvertes » en mondes nuls. À battre : recherche aléatoire ou en grille à budget égal, et un agent seul. |
| **Recherche guidée par évaluateur exact** | Évaluateur exact, peu coûteux, non contournable | En contrôle, l'évaluateur est un jeu fini d'organismes : la recherche le surapprend, et le bruit à 1 % domine | Écart de taux de détection à 1 % entre l'évaluateur de recherche et un évaluateur scellé (familles tierces). À battre : meilleur moniteur initial, sans recherche. |
| **Méthode des faits** (chaîne écrite, objets de contrôle, premier pas non justifié, relecteurs par mode d'échec, re-preuve sur énoncé seul) | Qu'une vérification finale existe | Relecteurs de même lignée partageant un angle mort ; objet de contrôle mal choisi | Transposition : chaque moniteur doit se taire sur placebo, sur erreurs honnêtes et sur sabotage injecté hors du modèle ; re-construction à l'aveugle du résultat à partir de l'énoncé et des données. Mesure : fraction de résultats plantés-faux arrêtés, contre relecture simple. |
| **Bornes qui disent où chercher** | Observable du moniteur bien défini | Borne estimée en distribution, attaquant hors distribution | Plafond oracle : classifieur entraîné avec étiquettes sur l'observable. S'il plafonne bas à 1 %, aucun moniteur sur cet observable ne fera mieux : changer d'observable. |
| **Impossibilités lues à l'envers** | Hypothèses du théorème pertinentes ici | Lecture trop littérale d'un résultat cryptographique | Voir ci-dessous. Mesure : la défense sans détection réduit-elle l'effet aval à utilité égale, contre un simple rééchantillonnage ? |
| **Garanties sans distribution** | Échangeabilité entre honnêtes de calibration et honnêtes de déploiement | Dérive honnête ; dépendance entre pas | Fausses alertes réalisées contre nominales sur tâches honnêtes nouvelles. Elles ne garantissent jamais la détection. À battre : seuil au quantile empirique. |

**Place des mathématiques (proposition).**

- **Borne.** Détecter revient à tester deux hypothèses. Si l'observable sous sabotage est à distance en variation totale ε de l'observable honnête, aucun moniteur ne dépasse α + ε de détection à α de fausses alertes. Il faut donc surveiller ce que l'attaquant ne peut pas rendre indiscernable sans renoncer à son effet : la conclusion elle-même.
- **Impossibilité à l'envers.** Goldwasser, Kim, Vaikuntanathan, Zamir (2022), *Planting Undetectable Backdoors in Machine Learning Models*, montrent que la détection par inspection peut être infaisable sous hypothèses cryptographiques. J'en tire qu'il faut des défenses qui ne passent pas par la détection : redondance, re-dérivation, tâches à vérité connue.
- **Sans distribution.** La prédiction conforme et les tests toujours-valides donnent un contrôle des fausses alertes au niveau de la trajectoire.

L'arbitre Lean 4 sert à vérifier ces bornes, pas à produire le résultat.

**Travaux.** Titres et auteurs que je peux attribuer ; identifiants arXiv non fournis (règle 3).

- Romera-Paredes et al. (2024), *Mathematical discoveries from program search with large language models*.
- Novikov et al. (2025), *AlphaEvolve: A coding agent for scientific and algorithmic discovery*.
- Lu et al. (2024), *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*.
- Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*.
- van der Weij et al. (2024), *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*.
- Roger, Greenblatt (2023), *Preventing Language Models From Hiding Their Reasoning*.
- Carlini et al. (2019), *On Evaluating Adversarial Robustness*.
- Tramèr, Carlini, Brendel, Madry (2020), *On Adaptive Attacks to Adversarial Example Defenses*.
- Angelopoulos, Bates (2021), *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*.
- Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World*.
- Vovk, Wang (2021), *E-values: Calibration, combination and applications*.
- Ramdas, Grünwald, Vovk, Shafer (2023), *Game-theoretic statistics and safe anytime-valid inference*.
- Platt (1964), *Strong inference*.

Références à vérifier :

- Bhatt et al. (2025), *Ctrl-Z: Controlling AI Agents via Resampling*.
- Mallen et al. (2024), *Subversion Strategy Eval*.
- Griffin et al. (2024), *Games for AI Control*.
- Bailey et al. (2024), *Obfuscated Activations Bypass LLM Latent-Space Defenses*.
- Goldowsky-Dill et al. (2025), *Detecting Strategic Deception Using Linear Probes*.

## 4. Vérification hors du programme et de son directeur

- **Banc public** existant plutôt que maison ; à défaut, banc maison publié avec vérité scellée chez un tiers.
- **Équipe rouge externe adaptative** : elle connaît la défense, n'est pas rémunérée au succès de la défense, et suit les règles de Carlini et al. (2019).
- **Familles de sabotage conçues par d'autres**, déposées scellées avant le gel de la défense.
- **Pré-enregistrement** des seuils, métriques et contrôles négatifs.
- **Réplication** par un tiers sur une autre famille de modèles ouverts.
- **Relecture** par des praticiens du contrôle, avec publication des contrôles négatifs et des issues négatives.

Critère d'arrêt honnête : sans équipe externe disponible, le résultat reste OBSERVÉ-NON-AUDITÉ, quelle que soit sa taille d'effet.

## 5. Reformulation de la demande

> « Produire une affirmation réfutable de la forme : *sur le banc public X, le protocole P, à budget d'audit b et fausses alertes ≤ 1 % par trajectoire sur honnêtes appariés (erreurs honnêtes incluses), maintient le taux de sabotage à effet aval non intercepté sous r, contre une équipe rouge externe adaptative, sur au moins k familles dont m conçues hors programme ; contrôles négatifs publiés ; répliquée par un tiers sur une autre famille de modèles.* Ou, à défaut, l'affirmation négative symétrique : *la famille de menaces F, décrite par la supposition qu'elle viole, ramène sous le seuil s toute défense de la classe C, vérifié par un tiers.* Les valeurs X, b, r, k, m, s sont fixées avant toute recherche. »

Les meilleurs modèles sont un moyen de remplir cette forme, pas l'objet de la demande.

## 6. Candidats, rangés (les duels sont le livrable b)

### Deux duels préalables, transversaux

**E1 : validité de construction.**

- H_A : les moniteurs détectent le comportement de sabotage.
- H_B : ils détectent la trace de construction des organismes.
- Métrique : taux de déclenchement à seuil calibré 1 % sur honnêtes appariés, mesuré sur placebos et sur saboteurs.
- Seuil (illustratif, à pré-enregistrer) : placebo au-dessus de 5 % falsifie H_A ; placebo dans l'intervalle de confiance de 1 % avec saboteurs détectés falsifie H_B.
- Contrôle négatif : sabotage injecté après coup, hors du modèle. Une sonde interne doit rester muette ; si elle sonne, les étiquettes fuient dans la chaîne.

**E4 : la conviction du directeur, à petite échelle.**

- H_A : l'organisme d'idéation retrouve des effets plantés mieux qu'une recherche mécanique à budget égal, sans excès de découvertes en mondes nuls.
- H_B : il ne fait pas mieux, ou il « découvre » dans le vide.
- Métrique : rappel sur mondes plantés ; fausses découvertes sur mondes nuls.
- Seuil : écart de rappel dont l'intervalle exclut zéro ; fausses découvertes au niveau nominal.
- Contrôle négatif : mondes nuls, plus mondes où l'effet planté est inversé.
- Issues : H_A falsifiée met S1 et S7 en cause, et il faut investir dans la vérification, pas dans la flotte. H_B falsifiée autorise la flotte pour la suite.

### Défense

**D1 (rang 1) : le monde planté comme défense, borne de risque par indiscernabilité.**

- *Idée.* Mêler aux tâches réelles une fraction q de tâches plantées à vérité connue. Si l'agent ne distingue pas les deux avec un avantage supérieur à δ, toute politique sabotant les tâches réelles au taux s sabote les plantées à au moins s − δ, et la probabilité de n'être jamais pris sur N tâches décroît comme (1 − q·d·(s − δ))^N, d étant le taux de vérification mécanique. C'est une esquisse à formaliser, et Lean 4 trouve là sa place.
- *Pourquoi remarqué.* L'effort passe de « meilleures sondes » à une quantité mesurable par des tiers, δ, et l'énoncé de risque ne dépend pas de l'intérieur du modèle.
- *Suppose.* On sait fabriquer des tâches plantées indiscernables. Le sabotage visé a un analogue vérifiable. Le sabotage n'est pas un coup unique à s infime, régime où la borne est faible.
- *Premier pas sans dépense.* Recherche bibliographique. L'audit initial et les entrées synthétiques existent chez Greenblatt et al. (2023), et Griffin et al. (à vérifier) en modélisent peut-être déjà le jeu. Puis écrire la borne et son premier pas non justifié.
- *Duel E2.*
  - H_A : δ ≤ δ₀ face au meilleur discriminateur (classifieur d'une équipe externe, sonde sur l'agent, jugement déclaré de l'agent).
  - H_B : δ > δ₀.
  - Métrique : avantage de discrimination planté contre réel.
  - Seuil : δ₀ pré-enregistré, tel que la borne reste informative.
  - Contrôle négatif : réel contre réel, avantage attendu nul ; sinon le discriminateur surapprend.
  - Issues : δ > δ₀ falsifie la défense en l'état et la borne devient vide. δ ≤ δ₀ falsifie la famille de menaces « discernement du test » pour ce banc.
- *Distinction.* Les pots de miel et la conscience d'évaluation sont publiés. La borne pilotée par un δ mesuré adversarialement, pour le sabotage de recherche à vérité hors machine, est à ma connaissance moins établie. Je ne sais pas si elle existe déjà sous cette forme.
- *Coût et temps (illustratif).* Quelques semaines ; 10³ à 10⁴ dollars de calcul et d'appels, hors équipe externe.
- *Chances (jugement illustratif).* De l'ordre d'une sur trois que δ soit assez petit sur des tâches de recherche réalistes. Nettement moins qu'il soit remarqué. L'issue négative est elle-même publiable.

**D2 (rang 2) : audit séquentiel toujours-valide agrégeant des moniteurs hétérogènes.**

- *Idée.* Convertir chaque score en valeur p conforme sur honnêtes appariés, puis en e-valeur, et accumuler le long de la trajectoire. L'alarme sonne au franchissement de 1/α, ce qui borne les fausses alertes par trajectoire à α, à tout instant d'arrêt, sans modèle de la distribution.
- *Pourquoi remarqué.* Le « 1 % » par pas ne dit rien du déploiement. Un énoncé valide au niveau trajectoire est le genre de pièce qu'un argumentaire de sûreté peut citer.
- *Suppose.* Échangeabilité conditionnelle des pas honnêtes. La dépendance intra-trajectoire casse le produit naïf ; la moyenne d'e-valeurs reste valide mais perd en puissance.
- *Premier pas sans dépense.* Ré-analyser les scores bruts déjà enregistrés.
- *Duel E3.*
  - H_A : fausses alertes réalisées ≤ nominal sur tâches honnêtes nouvelles, et détection supérieure au meilleur moniteur seul à budget d'audit égal sur la famille « faible dose ».
  - H_B : validité rompue, ou puissance non supérieure aux agrégations mécaniques (maximum, moyenne des scores).
  - Métrique : fausses alertes par trajectoire ; détection à budget égal.
  - Seuil : intervalle des fausses alertes contenant α ; gain dont l'intervalle exclut zéro.
  - Contrôle négatif : honnête contre honnête et étiquettes permutées, sans alarme au-delà de α.
  - Issues : validité rompue falsifie la supposition d'échangeabilité et la dérive honnête devient l'objet d'étude. Validité tenue avec gain réel falsifie l'idée que l'agrégation naïve suffit.
- *Distinction.* Les outils statistiques sont publiés (Vovk, Wang ; Ramdas et al.). Leur emploi comme règle d'audit en contrôle, je ne sais pas s'il est publié ; à vérifier.
- *Coût et temps (illustratif).* Quelques jours à semaines ; presque nul si les scores existent.
- *Chances.* Bonnes pour une chose qui marche côté fausses alertes. Incertaines côté puissance. Faibles pour « remarqué » seul ; plus élevées comme brique de D1.

**D3 (rang 3) : re-dérivation aveugle des énoncés porteurs.**

- *Idée.* Transposer la re-preuve des faits. Extraire les énoncés qui portent la décision, les faire re-dériver par un agent de confiance ou d'autre lignée qui ne reçoit que l'énoncé, auditer les désaccords. Les artefacts intermédiaires sabotés ne se propagent pas.
- *Pourquoi remarqué.* C'est une défense par l'effet, sans détection d'intention, conforme à la lecture à l'envers de Goldwasser et al.
- *Suppose.* Énoncés extractibles ; re-dériveur assez compétent ; bruit honnête de la recherche assez faible.
- *Premier pas sans dépense.* Mesurer sur les trajectoires honnêtes existantes le taux de désaccord entre deux dérivations honnêtes.
- *Duel.*
  - H_A : le désaccord honnête contre honnête tient sous 1 % après calibration, et le sabotage à effet aval est intercepté au-dessus du rééchantillonnage simple.
  - H_B : le bruit honnête dépasse le seuil, ou il n'y a pas de gain.
  - Métrique : désaccord sur paires honnêtes ; interception des sabotages à effet aval, à utilité égale.
  - Seuil : désaccord honnête dont l'intervalle contient 1 % ; gain d'interception dont l'intervalle exclut zéro.
  - Contrôle négatif : énoncés sans enjeu, plus re-dérivation d'énoncés plantés vrais.
  - Issues : bruit honnête trop fort falsifie D3 pour la recherche ouverte et borne son domaine aux tâches vérifiables. Gain réel falsifie l'idée que le rééchantillonnage suffit.
- *Distinction.* Proche du rééchantillonnage (Bhatt et al., à vérifier) et du moniteur de confiance. La différence est l'entrée réduite à l'énoncé et le ciblage par poids décisionnel. Nouveauté modeste, je le dis.
- *Coût et temps (illustratif).* Un à deux mois ; environ 10⁴ dollars.
- *Chances.* Faibles à moyennes.

### Menace : idées seulement, aucune procédure

**M1 (rang 1 côté menace) : carte « supposition violée × défense », avec familles scellées par des tiers.**

- *Idée.* Classer les menaces par la supposition de défense qu'elles violent, non par leur mécanisme. Pour chaque case, faire concevoir une famille par un tiers et la tenir scellée.
- *Pourquoi remarqué.* Un résultat du type « toute défense de classe C tombe sur la case F » est le format négatif que le domaine retient (précédent Athalye et al.). La carte dit aussi quelles défenses restent sans épreuve.
- *Suppose.* Qu'on trouve des concepteurs tiers ; que les familles ne fuient pas vers la mémoire des proposeurs.
- *Premier pas sans dépense.* Écrire, pour chaque moniteur du programme, la liste de ses suppositions.
- *Duel E5.*
  - H_A : la détection généralise entre familles, avec un écart de détection à 1 % entre familles vues et familles tierces sous un seuil pré-enregistré.
  - H_B : elle est spécifique à la famille.
  - Métrique : écart de détection à 1 % de fausses alertes entre familles vues et familles tierces.
  - Seuil : écart maximal pré-enregistré.
  - Contrôle négatif : famille tierce honnête, qui ne doit pas sonner.
  - Issues : chaque issue falsifie l'une des deux. Avec un seul mode tenu à l'écart (état actuel selon les faits), le duel est indécidable.
- *Distinction.* Les bancs de sabotage existent. L'indexation par supposition violée avec scellement tiers, je ne sais pas si elle est faite.
- *Coût et temps (illustratif).* Deux à quatre mois, surtout de la coordination.
- *Chances.* Moyennes ; c'est le candidat dont les deux issues sont utilisables.

Familles de la carte, au niveau de l'idée :

| Famille | Supposition de défense violée | Défense éprouvée |
|---|---|---|
| Incompétence indiscernable (omission, sous-performance) ; cf. van der Weij et al. | Le sabotage est un acte à signature distincte de l'erreur honnête | Sondes, jumeau honnête |
| Faible dose distribuée | Chaque pas est jugé isolément ; indépendance des pas | Seuil à 1 % par pas ; éprouve D2 |
| Angle mort corrélé | Les moniteurs agrégés se trompent indépendamment | Agrégation de moniteurs |
| Discernement du test | Tâches plantées et organismes sont vus comme le réel | Tests de mort ; éprouve D1 |
| Dérive de la référence honnête | Calibration et déploiement sont échangeables | Seuils conformes ; éprouve D2 |
| Représentation non linéaire ou déplacée ; cf. Bailey et al. (à vérifier) | L'information est lisible linéairement à un endroit fixe | Sondes linéaires |

**M2 (rang 2) : plafond oracle par observable.**

- *Idée.* Pour chaque observable, estimer par un classifieur avec étiquettes la détection maximale atteignable à 1 % ; publier les observables où ce plafond est bas. Ces observables sont perdus pour la défense, quel que soit le moniteur.
- *Pourquoi remarqué.* Cela évite d'investir dans des moniteurs sans issue.
- *Suppose.* Assez de cas honnêtes. Le classifieur donne une borne inférieure du plafond réel, pas le plafond.
- *Premier pas sans dépense.* Le faire sur les données existantes.
- *Duel.*
  - H_A : le plafond est haut sur l'observable (sondes améliorables).
  - H_B : le plafond est bas (changer d'observable).
  - Métrique : détection à 1 % d'un classifieur avec étiquettes, sur données tenues à part.
  - Seuil : plafond pré-enregistré, séparant « haut » de « bas ».
  - Contrôle négatif : étiquettes permutées, plafond attendu au niveau du hasard.
  - Issues : un plafond bas falsifie H_A pour cet observable. Un plafond haut falsifie H_B. Un moniteur au-dessus du plafond estimé signale une fuite ou une sous-estimation.
- *Distinction.* Pratique statistique connue ; son emploi systématique comme critère d'arrêt, je ne sais pas.
- *Coût et temps (illustratif).* Quelques jours.
- *Chances.* Élevées d'être utile, faibles d'être remarqué seul.

## (d) Ancrage matériel

- **Modèles.** Sondes et organismes exigent des poids ouverts : familles Llama, Qwen, Gemma, Mistral (versions à choisir ; je n'en garantis aucune). Les modèles de pointe par interface servent à la flotte d'idéation et aux re-dériveurs, pas aux sondes.
- **Calcul (illustratif).** Les organismes par adaptation légère de modèles de 7 à 30 milliards de paramètres demandent un à quelques processeurs graphiques pendant quelques jours. Le stockage des activations pour 10⁴ trajectoires appariées se compte en centaines de gigaoctets ou plus, selon les couches gardées.
- **Coût (illustratif).** D2 et M2 sont proches de zéro si les scores existent. E1, E2, E4 coûtent 10³ à 10⁴ dollars chacun. Le portefeuille complet avec équipe externe est de l'ordre de 10⁵ dollars et de trois à six mois. Seul repère issu des faits : 300 dollars par problème, pour deux sur soixante-huit.
- **Ordre conseillé.** D'abord E1 et M2, sans dépense, parce qu'ils peuvent invalider les mesures actuelles. Ensuite E4, qui décide si la flotte vaut son coût. Enfin D1 et M1 ensemble, la famille « discernement du test » servant d'épreuve à D1.

FIN-DE-CELLULE