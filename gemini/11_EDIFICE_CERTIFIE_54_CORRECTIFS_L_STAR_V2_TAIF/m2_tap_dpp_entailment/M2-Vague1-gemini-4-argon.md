`VOLET: I`
`FAMILLE_ET_AUTEURS: Representation Engineering (RepE) & Linear Artificial Tomography (LAT) — Zou et al. (2023)`
`REQUETE_API: Representation Engineering Linear Artificial Tomography LLM honesty`
`AFFIRMATION_ANCREE: RepE/LAT extrait des directions de concepts (comme la tromperie ou l'intention) par analyse en composantes principales sur des paires de prompts contrastifs globaux, mais échoue à neutraliser la fuite d'information lexicale du jeton généré lorsque l'acte est forcé ou nié à $k=0$, faute de protocole d'appariement strict intra-bloc.`
`WHITE_SPACE_NOTRE_FUSEE: Notre protocole du Jumeau Nié ($\sigma_r^0$) à $k=0$ croisant Saboteur Inactif (P2) et Acte Imposée (P4) opère exclusivement sur le sous-espace épuré $S_{\text{TD}} < 1\%$ (Xu et al.) et garantit une inférence exacte à faible échantillon par retournement de signe intra-bloc exact et $d_z$ de Hedges, éliminant tout biais de surface lexicale.`

`VOLET: II`
`FAMILLE_ET_AUTEURS: LEACE (LEAst-squares Concept Erasure) — Belrose et al. (2023)`
`REQUETE_API: LEACE least squares concept erasure affine projection`
`AFFIRMATION_ANCREE: LEACE construit un projecteur oblique affine idempotent pour effacer linéairement l'information d'un concept dans les représentations statiques d'un transformeur, mais ne modélise pas la dynamique temporelle non-linéaire du flux résiduel et s'effondre sous la dérive d'état induite par des rejets et ré-échantillonnages séquentiels répétés.`
`WHITE_SPACE_NOTRE_FUSEE: Notre opérateur Do-Clamp couple la projection affine idempotente ($P_{\text{do}}^2 = P_{\text{do}}$) à un dictionnaire d'observables liftées de Koopman muni d'une rétraction radiale $C^1$ contrôlée, endiguant mathématiquement la dérive de rejet séquentielle (0,49 -> 0,65) sur la trajectoire dynamique multi-tours.`

`VOLET: III`
`FAMILLE_ET_AUTEURS: Guardrails Typés & Décodage Contraint (LMQL / Outlines) — Beurer-Kellner et al. (2023) / Willard & Louf (2023)`
`REQUETE_API: Outlines finite state machine constrained decoding JSON`
`AFFIRMATION_ANCREE: Ces moteurs compilent des schémas JSON et des expressions régulières en automates à états finis pour masquer les logits invalides à la volée, mais restent totalement aveugles à la dérive d'entropie sémantique intra-schéma (stéganographie ou évasion dans les champs libres) et ne fournissent aucune preuve cryptographique d'auditabilité.`
`WHITE_SPACE_NOTRE_FUSEE: L'architecture dyadique Sol/Astra combine l'enveloppe typée $\mathcal{S}_{\text{strict}}$ et le prédicat $\Pi_0$ avec un arbre de Merkle `sha256` anti-déni et une mesure de divergence de Jensen-Shannon en base 2 corrigée du biais d'échantillon fini par Miller-Madow sur le tenseur $S_{\text{TD}}$.`

`VOLET: IV-H9`
`FAMILLE_ET_AUTEURS: Détection de Point de Rupture sur Flux Textuels & Séries Temporelles — Tartakovsky et al. (2014) / Page (1954)`
`REQUETE_API: CUSUM prewhitening autoregressive semantic drift LLM multi-agent`
`AFFIRMATION_ANCREE: Les cartes de contrôle CUSUM classiques appliquées à la dérive des modèles supposent des résidus indépendants et identiquement distribués (i.i.d.), ce qui génère un taux rédhibitoire de fausses alarmes face à l'autocorrélation naturelle des états cachés lors de chaînes de délégation multi-agents.`
`WHITE_SPACE_NOTRE_FUSEE: Notre moniteur H9 applique un pré-blanchiment AR(1) exact sur la trace $S_{\text{TD}}$ à travers $d=1..6$ sauts de délégation, couple la détection au test non-paramétrique de tendance ordonnée de Jonckheere-Terpstra, et verrouille l'exécution par un Jeton de Capacité Monotone ($\Pi_{d+1} \subseteq \Pi_d$).`

`VOLET: V-Essaims`
`FAMILLE_ET_AUTEURS: Débat Multi-Agents & Consensus Byzantin — Du et al. (2023) / Castro & Liskov (1999)`
`REQUETE_API: multi-agent debate LLM consensus Byzantine fault tolerance`
`AFFIRMATION_ANCREE: Les protocoles de débat multi-agents agrègent les réponses par vote majoritaire ou juge LLM mais souffrent de vulnérabilité au paradoxe de Simpson inter-modèles (biais de corrélation d'erreurs entre architectures proches) et ne permettent pas d'auditer cryptographiquement un saboteur adaptatif infiltré a priori.`
`WHITE_SPACE_NOTRE_FUSEE: Notre contrôle d'essaim chimérique Tri-Espèces ($N=9, f=2$) neutralise le paradoxe de Simpson par un test stratifié de Cochran-Mantel-Haenszel couplé au test d'homogénéité de Breslow-Day, valide l'équivalence par TOST Newcombe-Wilson à $z_{0,95}$, et audite un saboteur LoRA hors-famille sous protocole Commit-Reveal SHA-256 de Kerckhoffs.`
