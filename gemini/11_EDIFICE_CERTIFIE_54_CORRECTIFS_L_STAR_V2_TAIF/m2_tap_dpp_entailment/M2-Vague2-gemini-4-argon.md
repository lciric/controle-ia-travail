`VOLET: I`
`FAMILLE_ET_AUTEURS: Spurious Correlation Removal via Concept Probing and Counterfactual Data Augmentation – Ravfogel, Elazar,onen, Goldberg (INLP, ACL 2020, arXiv:2004.07667) & Feder, Oved, Shalit, Reichart (CausaLM, Computational Linguistics 2021, arXiv:2005.13407 ; références à vérifier)`
`REQUETE_API: counterfactual text pairs concept probing spurious lexical correlation`
`AFFIRMATION_ANCREE: Ces méthodes tentent d'isoler un concept latent des corrélations lexicales de surface via des paires contrefactuelles ou des projections itératives dans l'espace nul (INLP), mais elles opèrent au niveau de la représentation globale de séquence sans verrouiller la position pré-acte exacte $k=0$ ni dissocier un Saboteur Inactif (P2) d'un Acte Imposé (P4) par test d'échangeabilité apparié intra-bloc.`
`WHITE_SPACE_NOTRE_FUSEE: Notre opérateur enracine l'inférence exclusivement au token charnière $k=0$ sur le sous-espace $S_{\text{TD}} < 1\%$ via le protocole tripartite ($\sigma_r^0$ Jumeau Nié, P2, P4) et certifie l'absence de fuite lexicale par la statistique $d_z$ de Hedges couplée à une distribution nulle exacte par retournement de signe intra-bloc ($2^B$ permutations).`

`VOLET: II`
`FAMILLE_ET_AUTEURS: Inference-Time Intervention (ITI) & Activation Addition (ActAdd) – Li, Patel, Viégas, Pfister, Wattenberg (NeurIPS 2023, arXiv:2306.03341) & Turner, Thiergart, Leech, Udell, Vazquez, Mini, MacDiarmid (arXiv:2308.10248, 2023 ; références à vérifier)`
`REQUETE_API: Inference-Time Intervention Activation Addition steering vector LLM`
`AFFIRMATION_ANCREE: ITI et ActAdd translatent les activations du flux résiduel selon un vecteur de direction fixe pendant l'inférence, ce qui est non-idempotent ($T(T(h)) \neq T(h)$) et induit une divergence géométrique cumulative ainsi qu'un effondrement de la perplexité lors de boucles de rejets multi-tours.`
`WHITE_SPACE_NOTRE_FUSEE: Notre opérateur `Do-Clamp` impose un projecteur affine strictement idempotent ($P_{\text{do}}^2 = P_{\text{do}}$) doublé d'une rétraction radiale $C^1$ contrôlée par un dictionnaire d'observables liftées de Koopman, garantissant une stabilité spectrale absolue face à la dérive sous rejets répétés (`0,49 -> 0,65`).`

`VOLET: III`
`FAMILLE_ET_AUTEURS: SecGPT / Dual-LLM Execution Isolation & Spotlighting – Wu, Roesner, Kohno, Zhang, Mireshghallah (SecGPT, arXiv:2403.04960, 2024) & Hines, Lopez, Hall, Zarfati, Zunger, Kiciman (Spotlighting, arXiv:2403.14720, 2024 ; références à vérifier)`
`REQUETE_API: SecGPT Spotlighting prompt injection execution isolation LLM`
`AFFIRMATION_ANCREE: Ces architectures isolent les flux d'exécution d'applications LLM ou marquent les données non fiables par encodage (Spotlighting), mais ne mesurent pas la fuite informationnelle résiduelle en théorie de l'information sur le canal de sortie typé ni ne garantissent l'auditabilité cryptographique de chaque transition par arbre de Merkle.`
`WHITE_SPACE_NOTRE_FUSEE: Le pare-feu dyadique *Sol/Astra* combine l'enveloppe JSON strictement typée $\mathcal{S}_{\text{strict}}$ filtrée par le prédicat $\Pi_0$, un scellement anti-déni par arbre de Merkle `sha256` et une borne de fuite sémantique quantifiée par la divergence de Jensen-Shannon en base 2 débiaisée par la correction analytique de Miller-Madow.`

`VOLET: IV-H9`
`FAMILLE_ET_AUTEURS: Capability-Based Access Control for LLM Agents & Delegation Chains – Watson, Piet,jyothi, Raluca Ada Popa et al. / Wu et al. (Information Flow Control for LLM Agents, 2024 ; références à vérifier) & Alpernas et al. (Secure Serverless / Dynamic IFC, OOPSLA 2018 ; référence à vérifier)`
`REQUETE_API: LLM agents delegation chain capability access control attenuation`
`AFFIRMATION_ANCREE: Les systèmes de contrôle de flux d'information dynamique (DIFC) appliquent des étiquettes de sécurité discrètes le long des appels d'outils, mais restent aveugles à la dérive continue et autocorrélée du tenseur interne des états cachés au fil des sauts de délégation $d=1..6$.`
`WHITE_SPACE_NOTRE_FUSEE: Notre architecture couple directement le Jeton de Capacité Monotone ($\Pi_{d+1} \subseteq \Pi_d$) à la dynamique géométrique interne sur $S_{\text{TD}}$ via un filtre CUSUM pré-blanchi AR(1) et certifie la monotonie de l'érosion multi-sauts par le test non-paramétrique directionnel de Jonckheere-Terpstra.`

`VOLET: V-Essaims`
`FAMILLE_ET_AUTEURS: Heterogeneous LLM Ensembles & Mixture-of-Agents (MoA) – Wang, Wang, Athiwaratkun, Zhang, Zou (Mixture-of-Agents Enhances Large Language Model Capabilities, arXiv:2406.04692, 2024) & Jiang, Ren, Lin (LLM-Blender, ACL 2023, arXiv:2306.02561 ; références à vérifier)`
`REQUETE_API: Mixture-of-Agents LLM-Blender heterogeneous ensemble multi-agent aggregation`
`AFFIRMATION_ANCREE: MoA et LLM-Blender agrègent les sorties de familles de modèles hétérogènes pour maximiser la qualité de génération, mais supposent des agents coopératifs et sont dépourvus de tests statistiques stratifiés contre le paradoxe de Simpson ou de protocole d'engagement cryptographique pour débusquer un saboteur furtif.`
`WHITE_SPACE_NOTRE_FUSEE: Notre protocole `H4'` sur Chimère Tri-Espèces ($N=9, f=2$) neutralise les biais inter-familles via le test stratifié de Cochran-Mantel-Haenszel couplé au test d'homogénéité des odds-ratios de Breslow-Day, valide l'équivalence par TOST Newcombe-Wilson à $z_{0,95}$, et audite hors-famille un saboteur `LoRA` sous schéma Commit-Reveal `SHA-256` (principe de Kerckhoffs).`
