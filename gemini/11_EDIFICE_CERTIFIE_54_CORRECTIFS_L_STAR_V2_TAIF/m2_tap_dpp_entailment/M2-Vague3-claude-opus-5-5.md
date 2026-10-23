Avertissement : je ne peux pas certifier qu'un opérateur est « 100 % inédit ». Le champ WHITE_SPACE présente donc des **écarts revendicables, à confirmer par une recherche systématique**. Je n'ai pas pu vérifier Xu et al. (`arXiv:2602.00986v2`) ni Jhaveri/Tagliabue 2026.

---

`VOLET: I`
`FAMILLE_ET_AUTEURS:` Planification latente pré-token et décodage du futur depuis un état caché.
- Wu, Morris, Levine, *Do Language Models Plan Ahead for Future Tokens?*, COLM 2024, arXiv:2404.00859.
- Pal, Sun, Yuan, Wallace, Bau, *Future Lens: Anticipating Subsequent Tokens from a Single Hidden State*, CoNLL 2023, arXiv:2311.04897.
- Antériorité du nul par retournement de signe : Nichols & Holmes, *Nonparametric Permutation Tests for Functional Neuroimaging*, Human Brain Mapping 2002.

(Références à vérifier.)

`REQUETE_API: future token planning hidden state pre-caching breadcrumbs probe`

`AFFIRMATION_ANCREE:`
- **Wu et al.** distinguent deux mécanismes : le *pre-caching* (calcul délibéré au profit des positions futures) et les *breadcrumbs* (traits utiles au présent, réutilisés incidemment). Ils les séparent par un entraînement myope qui coupe le gradient inter-positions.
- **Future Lens** montre qu'un seul état caché en position *t* permet de prédire les tokens *t+1...t+N* au-delà du hasard.
- **Limite commune :** aucune de ces méthodes ne construit de contrôle apparié à intention nulle. Un signal « futur » décodable peut donc n'être qu'une anticipation lexicale. Ni l'une ni l'autre n'est évaluée en régime de faible prévalence.

`WHITE_SPACE_NOTRE_FUSEE:`
- **Plan factoriel :** le triplet σ_r^0 / `P2` / `P4` croise intention × exécution (intention sans acte, acte sans intention). Il attribue ainsi le signal pré-acte à l'intention plutôt qu'à la trace lexicale future, sur S_TD < 1 %.
- **Statistique :** d_z intra-bloc avec nul exact par retournement de signe, apparié par graine et par prompt.
- **Vigilance :** `P4` (acte imposé) est le test décisif contre l'hypothèse *breadcrumbs*. Si la sonde y répond, c'est une trace lexicale, pas une intention.
- **À vérifier ensuite :** Ashok & May, *Language Models Can Predict Their Own Behavior*, 2025.

---

`VOLET: II`
`FAMILLE_ET_AUTEURS:` Pilotage affine optimal en forme close.
- Singh, Ravfogel, Herzig, Aharoni, Cotterell, Kumaraguru, *Representation Surgery: Theory and Practice of Affine Steering*, ICML 2024, arXiv:2402.09631.
- Connexe (clamp de traits SAE) : Templeton et al. (Anthropic), *Scaling Monosemanticity*, 2024.
- Connexe : Farrell, Lau, Conmy, *Applying Sparse Autoencoders to Unlearn Knowledge in Language Models*, arXiv:2410.19278.

(Références à vérifier.)

`REQUETE_API: optimal affine steering closed form representation surgery`

`AFFIRMATION_ANCREE:`
- **Singh et al.** dérivent la fonction de pilotage affine à perturbation minimale qui égalise les moyennes, voire les covariances (lien avec le transport optimal gaussien), entre concepts.
- **Limites de Singh et al. :**
  - l'opérateur est appliqué une seule fois, sans analyse de stabilité sous applications répétées en boucle multi-tour ;
  - la variante moyenne + covariance n'est pas idempotente en général ;
  - la norme n'est pas contrôlée, d'où un risque hors-distribution.
- **Limite du clamp SAE :** il fixe dur la valeur d'un trait. Il est non C^1 et opère dans la base SAE, pas sur des observables dynamiques.

`WHITE_SPACE_NOTRE_FUSEE:`
- **Idempotence :** P_do2 = P_do donne un point fixe en une seule application, sans accumulation tour après tour.
- **Rétraction radiale C^1 :** elle borne la norme sans la discontinuité du clamp dur.
- **Lift de Koopman :** il permet d'analyser la propagation de la composante supprimée entre les tours.
- **Vigilance 1 :** LEACE est déjà idempotent. La nouveauté ne peut donc pas reposer sur l'idempotence seule.
- **Vigilance 2 :** l'idempotence n'empêche pas la dérive si le modèle réinjecte la composante entre deux tours. La revendication doit porter sur le système bouclé (spectre de K restreint au complément de P_do), pas sur P_do isolé.

---

`VOLET: III`
`FAMILLE_ET_AUTEURS:` Détection d'injection par réponse connue et détecteur minimax.
- Liu, Jia, Geng, Jia, Gong, *Formalizing and Benchmarking Prompt Injection Attacks and Defenses*, USENIX Security 2024, arXiv:2310.12815.
- Liu et al., *DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks*, IEEE S&P 2025, arXiv:2504.11358.
- Antériorité journal inviolable : Crosby & Wallach, *Efficient Data Structures for Tamper-Evident Logging*, USENIX Security 2009.

(Références à vérifier.)

`REQUETE_API: prompt injection known-answer detection game-theoretic detector`

`AFFIRMATION_ANCREE:`
- **Liu et al. (2024)** formalisent l'injection comme une composition tâche cible / tâche injectée. Ils évaluent notamment la détection par « réponse connue » : le modèle doit restituer une clé secrète malgré les données, et un échec signale une contamination.
- **DataSentinel** durcit ce détecteur par un jeu minimax contre des injections adaptatives.
- **Limites de ces détecteurs :**
  - verdict binaire par entrée ;
  - pas d'enveloppe typée en amont ;
  - pas d'historique des verdicts vérifiable par un tiers (aucun anti-déni) ;
  - pas de statistique distributionnelle sur fenêtres.
- **Crosby-Wallach** fournit des preuves d'inclusion et de cohérence de logs, mais sans sémantique de sécurité LLM.

`WHITE_SPACE_NOTRE_FUSEE:`
- **Couplage tri-couche :**
  1. rejet déterministe S_strict + Π_0 avant tout appel au modèle ;
  2. engagement Merkle `sha256` de chaque verdict ;
  3. JSD base 2 débiaisée Miller-Madow, bornée dans [0,1], comme statistique de décalage entre canaux.
- **Baseline obligatoire :** Known-Answer.
- **Vigilance :** la correction Miller-Madow est d'ordre 1/N. La JSD débiaisée peut devenir négative à petit N, et le biais persiste si la taille du support K est proche de N. Prévoir un bootstrap ou l'estimateur NSB en contrôle.

---

`VOLET: IV-H9`
`FAMILLE_ET_AUTEURS:` E-détecteurs non paramétriques pour la rupture séquentielle.
- Shin, Ramdas, Rinaldo, *E-detectors: a Nonparametric Framework for Sequential Change Detection*, NEJSDS 2024, arXiv:2203.03532.
- Baseline bayésienne : Adams & MacKay, *Bayesian Online Changepoint Detection*, arXiv:0710.3742.
- Chaînes de délégation : Jones, Nadalin, Campbell, Bradley, Mortimore, *OAuth 2.0 Token Exchange*, RFC 8693, 2020.
- Défaillances inter-agents : Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, arXiv:2503.13657.

(Références à vérifier.)

`REQUETE_API: e-detectors nonparametric sequential change detection e-processes`

`AFFIRMATION_ANCREE:`
- **Shin et al.** généralisent CUSUM et Shiryaev-Roberts via des sommes d'e-processus. Ils obtiennent un contrôle non asymptotique de l'ARL (temps moyen avant fausse alarme), sans modèle paramétrique.
- **Limites de Shin et al. :** la classe pré-rupture n'est pas pensée pour l'autocorrélation pré-blanchie, ni pour un indice ordinal de profondeur.
- **BOCPD** n'offre pas de garantie fréquentiste de fausse alarme.
- **RFC 8693** trace la chaîne d'acteurs (revendications `act` imbriquées) sans imposer d'atténuation monotone des portées.

`WHITE_SPACE_NOTRE_FUSEE:`
- **Trois axes couplés,** que je n'ai pas vus réunis dans la littérature :
  - le temps : CUSUM sur résidus AR(1) ;
  - la profondeur : tendance de Jonckheere-Terpstra sur d = 1..6 ;
  - l'autorité : Π_{d+1} ⊆ Π_d, vérifiable.
- **Baseline SOTA à battre :** un e-détecteur appliqué aux mêmes résidus.
- **Vigilance 1 :** l'estimation plug-in de φ dégrade la calibration de l'ARL.
- **Vigilance 2 :** Jonckheere-Terpstra suppose des groupes indépendants. Si les mêmes chaînes sont mesurées à chaque saut, les données sont appariées : utiliser plutôt le test L de Page (1963).

---

`VOLET: V-Essaims`
`FAMILLE_ET_AUTEURS:` Collusion secrète stéganographique entre agents.
- Motwani, Baranchuk, Strohmeier, Bolina, Torr, Hammond, Schroeder de Witt, *Secret Collusion among AI Agents: Multi-Agent Deception via Steganography*, NeurIPS 2024, arXiv:2402.07510.
- Engagement cryptographique de modèle : Sun, Li, Zhang, *zkLLM: Zero Knowledge Proofs for Large Language Models*, ACM CCS 2024, arXiv:2404.16109.

(Références à vérifier.)

`REQUETE_API: secret collusion steganography multi-agent LLM detection`

`AFFIRMATION_ANCREE:`
- **Motwani et al.** formalisent la collusion par canaux cachés et évaluent les capacités stéganographiques des modèles (cadre CASE). Ils montrent que des modèles de pointe peuvent se coordonner secrètement et que les contre-mesures testées (paraphrase, monitoring) restent d'efficacité limitée.
- **Limites de Motwani et al. :** pas de test stratifié inter-familles, ni d'engagement préalable du saboteur.
- **zkLLM** prouve qu'une inférence provient de poids engagés, sans aucune évaluation comportementale.

`WHITE_SPACE_NOTRE_FUSEE:`
- **Protocole pré-enregistré :**
  - saboteur `LoRA` engagé par SHA-256 avant l'expérience (méthode publique, seul le saboteur reste secret) ;
  - CMH stratifié par espèce, avec Breslow-Day contre le paradoxe de Simpson ;
  - TOST Newcombe-Wilson à z_0,95, soit un IC à 90 %, pour démontrer la non-dégradation.
- **Apport :** le cas f = 2 colludants hors-famille est motivé, mais pas testé statistiquement, chez Motwani et al.
- **Vigilance 1 :** avec 3 strates, Breslow-Day a une puissance très faible. Un non-rejet ne prouve pas l'homogénéité.
- **Vigilance 2 :** l'unité statistique doit être l'épisode ou la tâche, pas l'agent (N = 9).
- **Vigilance 3 :** si l'engagement porte sur un choix parmi peu de candidats, ajouter un nonce. Sinon, le hash est attaquable par énumération.
