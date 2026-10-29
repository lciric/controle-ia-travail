VOLET: I
FAMILLE_ET_AUTEURS: Sondes linéaires de détection de la tromperie stratégique. Référence principale : Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (Apollo Research), *Detecting Strategic Deception Using Linear Probes*, arXiv:2502.03407, 2025. Antériorité connexe : Hubinger et al., *Sleeper Agents*, arXiv:2401.05566, 2024. (Références à vérifier.)
REQUETE_API: linear probes strategic deception residual stream intent detection
AFFIRMATION_ANCREE: Des sondes linéaires lisent une intention trompeuse dans le flux résiduel (Llama-3.3-70B) avant ou pendant la génération. Les auteurs rapportent des AUROC d'environ 0,96 à 0,999 et un rappel élevé à 1 % de faux positifs sur un corpus de contrôle (valeurs à vérifier). En revanche, l'évaluation est agrégée par AUROC. Il n'y a ni appariement intra-bloc, ni taille d'effet appariée, ni contrôle contrefactuel neutralisant la surface lexicale. Les auteurs reconnaissent eux-mêmes que la sonde peut capter des indices de scénario plutôt que l'intention.
WHITE_SPACE_NOTRE_FUSEE: Le jumeau nié à k=0 (σ_r^0) fixe la trace lexicale et ne fait varier que l'intention pré-acte, via le contraste entre `P2` (saboteur inactif) et `P4` (acte imposé). L'inférence repose sur le d_z de Hedges et sur une distribution nulle exacte obtenue par retournement de signe intra-bloc, dans un régime S_TD < 1 %. Différenciateur revendiqué : passer de « une sonde détecte » à « l'intention est séparée de la lexicalité, avec une garantie inférentielle appariée ».

VOLET: II
FAMILLE_ET_AUTEURS: Effacement de concept par projection affine en forme close. Référence principale : LEACE, Belrose, Schneider-Joseph, Ravfogel, Cotterell, Raff, Biderman, *LEACE: Perfect Linear Concept Erasure in Closed Form*, NeurIPS 2023. Lignée Koopman : EDMD, Williams, Kevrekidis, Rowley, 2015. (Références à vérifier.)
REQUETE_API: closed-form linear concept erasure affine projection activations
AFFIRMATION_ANCREE: LEACE fournit un opérateur affine (projection oblique, donc idempotent) qui empêche tout classifieur linéaire de récupérer le concept, avec une perturbation minimale au sens des moindres carrés. Ses limites sont les suivantes : l'opérateur est statique, couche par couche et sans dynamique temporelle. Il n'existe aucun traitement de la dérive cumulée sur des tours successifs de rejet, et la garantie se limite aux lecteurs linéaires, sans relevé non linéaire de type Koopman.
WHITE_SPACE_NOTRE_FUSEE: L'idempotence P_do2 = P_do n'est **pas** nouvelle en soi, puisque LEACE l'a déjà. La niche réelle tient à trois éléments combinés : appliquer l'opérateur dans un dictionnaire d'observables Koopman relevées, l'associer à une rétraction radiale C1 contrôlée, et le cibler explicitement sur la dérive sous rejets répétés (0,49 → 0,65). Il faut cadrer l'innovation sur ce couplage dynamique, et non sur la projection.

VOLET: III
FAMILLE_ET_AUTEURS: Architectures duales LLM privilégié/quarantaine à capacités. Référence principale : CaMeL, Debenedetti, Shumailov, Fan, Hayes, Carlini, Fabian, Kern, Shi, Terzis, Tramèr, *Defeating Prompt Injections by Design*, arXiv:2503.18813, 2025. Antériorité Merkle : Certificate Transparency, Laurie, Langley, Kasper, RFC 6962, 2013. (Références à vérifier.)
REQUETE_API: dual LLM capability prompt injection defense design
AFFIRMATION_ANCREE: CaMeL sépare le flot de contrôle (LLM privilégié) des données non fiables (LLM quarantaine) et applique des politiques de capacités sur les flux de données. Il obtient une sécurité démontrable sur une fraction des tâches AgentDojo (environ 67 % selon la v1, à vérifier). Il ne fournit en revanche aucun journal infalsifiable anti-déni ni aucun suivi statistique distributionnel de l'écart entre les deux agents. La sécurité y est purement déterministe et politique.
WHITE_SPACE_NOTRE_FUSEE: Notre pare-feu fusionne trois couches en un seul pare-feu dyadique *Sol/Astra* :
- une couche syntaxique : enveloppe JSON typée S_strict et prédicat Π0 ;
- une couche cryptographique : arbre de Merkle `sha256`, emprunté à la lignée RFC 6962 mais transposé aux échanges inter-agents ;
- une couche statistique : divergence de Jensen-Shannon en base 2 avec correction de biais Miller-Madow, pour détecter une collusion ou une dérive invisible à la politique.

L'axe statistique débiaisé est absent de CaMeL.

VOLET: IV-H9
FAMILLE_ET_AUTEURS: Atténuation monotone de capacités déléguées. Référence principale : Macaroons, Birgisson, Politz, Erlingsson, Taly, Vrable, Lentczner, NDSS 2014. Baseline statistique : CUSUM sur résidus d'un AR(1), Lu & Reynolds, *Journal of Quality Technology*, 2001. Érosion sémantique : Perez et al., *When LLMs Play the Telephone Game*, arXiv:2407.04503, 2024. (Références à vérifier.)
REQUETE_API: macaroons caveat attenuation delegation chained authorization
AFFIRMATION_ANCREE: Les Macaroons garantissent cryptographiquement, par chaînage HMAC des caveats, que chaque délégataire ne peut que restreindre ses droits. C'est exactement la propriété Π_{d+1} ⊆ Π_d, mais elle ne dit rien de l'érosion sémantique du contenu transmis. De son côté, Lu & Reynolds montrent qu'après pré-blanchiment d'un AR(1), un saut de moyenne δ se réduit dans les résidus à (1−φ)δ après le premier pas. Cela ampute la sensibilité du CUSUM quand φ > 0.
WHITE_SPACE_NOTRE_FUSEE: Notre approche couple, sur une même échelle d = 1..6, deux éléments :
- l'invariant cryptographique de monotonie des capacités ;
- l'érosion sémantique mesurée sur S_TD, avec un CUSUM pré-blanchi AR(1) et un test de tendance ordonnée de Jonckheere-Terpstra sur la profondeur de délégation.

Le différenciateur revendiqué est de prouver que les droits décroissent pendant qu'on mesure statistiquement que le sens se dégrade, et de corriger explicitement la perte (1−φ)δ.

VOLET: V-Essaims
FAMILLE_ET_AUTEURS: Résilience des systèmes multi-agents LLM à agents malveillants. Référence principale : Huang, Zhou, Liang et al., *On the Resilience of Multi-Agent Systems with Malicious Agents*, arXiv:2408.00989, 2024. Référence connexe : Amayuelas et al., *MultiAgent Collaboration Attack*, arXiv:2406.14711, 2024. Antériorité LoRA : Liu et al., *LoRA-as-an-Attack!*, arXiv:2403.00108, 2024. (Références à vérifier.)
REQUETE_API: multi-agent LLM malicious agents resilience topology
AFFIRMATION_ANCREE: Ces travaux comparent des topologies (hiérarchique, linéaire, plate) sous injection d'agents fautifs, et la hiérarchie s'y révèle la plus robuste (chiffres de dégradation à vérifier). Leurs limites sont triples :
- les tests portent sur des différences, sans test d'équivalence (TOST) ;
- il n'y a pas d'analyse stratifiée par famille de modèles avec test d'homogénéité, d'où un risque de paradoxe de Simpson ;
- la malveillance est induite par prompt, et non par des poids LoRA engagés cryptographiquement.
WHITE_SPACE_NOTRE_FUSEE: La chimère tri-espèces (Llama-3.1, Mistral et Qwen, avec N = 9 et f = 2, soit N ≥ 3f + 1) repose sur quatre briques :
- un test CMH corrigé en continuité, stratifié par famille ;
- un test de Breslow-Day comme garde anti-Simpson ;
- une équivalence TOST par intervalles de Newcombe-Wilson à z_{0,95} ;
- un saboteur LoRA engagé par `SHA-256` (commit-reveal, principe de Kerckhoffs) puis audité hors-famille.

Le différenciateur revendiqué est de passer d'une robustesse simplement observée à une équivalence certifiée, stratifiée et pré-engagée.

---
*Note d'intégrité : les références et chiffres ci-dessus sont restitués de mémoire et doivent être vérifiés via les requêtes fournies. Je ne peux pas confirmer `arXiv:2602.00986v2` ni Jhaveri/Tagliabue 2026. Le caractère « 100 % inédit » relève d'une revendication à valider par une recherche d'antériorité exhaustive ; le Volet II est le plus exposé.*
