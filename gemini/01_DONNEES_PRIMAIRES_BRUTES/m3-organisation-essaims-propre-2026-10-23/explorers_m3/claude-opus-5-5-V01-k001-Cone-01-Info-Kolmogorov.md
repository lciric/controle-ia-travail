BASSIN_MATH: Loi de Compression Disjointe Minimale (LCDM)

LOI_PROPOSEE: spawn(j) ⇔ [L(D|M) − L(D|M⊕j) − α·C_W(E_j; E_M)] / c_j > λ_t, avec λ_t = λ₀·(B_restant/B₀)⁻¹.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

L'essaim M est un programme de description du corpus D (claims, citations, expériences). Son apprentissage consiste à réduire sa longueur MDL L(M) + L(D|M) sans toucher aux poids. Il opère par mutation de topologie, de prompts et de mémoire externe compressée.

- **Arêtes** : i parle à j si NCD(E_i, E_j) > τ, où E désigne les traces d'erreurs. On relie ainsi des agents complémentaires, et non redondants.
- **Spawn explorateur** : il est déclenché quand le résidu L(D|M) reste incompressible, ce qui signale des régions non couvertes.
- **Spawn démolisseur Red-Team** : il est déclenché quand le taux de compression de D par M est anormalement élevé, signe suspect de régularité artificielle.
- **Monoculture vs chimère** : une famille est conservée seule si l'information commune de Wyner C_W(E_claude; E_gemini), estimée par jev-1.14.0, est faible. Sinon on hybride, car des erreurs corrélées par poids partagés (H4') impliquent un C_W élevé.
- **Budget** : le coût c_j vaut 100 USD pour Claude et 20 USD pour Gemini.
- **Anti-dérive (H9)** : la dérive d'une chaîne de délégation est mesurée par drift = K(consigne | chaîne) − K(consigne). Une branche est élaguée si drift > δ.

**2. Fonction objectif et anti-Goodhart**

R_t = [ΔL_vérifié − α·Σ C_W(E_i;E_j) − β·Rec − γ·drift − η·Goo] / coût_t

- **ΔL_vérifié** : gain de compression mesuré uniquement sur des faits validés par arXiv, Semantic Scholar et Crossref.
- **Rec (récitation)** : Rec = 1 − K(y|x)/K(y), estimé par compression conditionnelle. Une sortie très compressible depuis la seule requête x signale une restitution de mémoire paramétrique.
- **Goo (Goodhart)** : Goo = I(y; features_jev) − I(y; vérité_externe). Il pénalise les sorties qui optimisent les traits du juge plutôt que la vérité.
- **Contre-mesures supplémentaires** : le juge est rotatif (seeds et seuils tirés aléatoirement) et le jeu de test reste caché.

**3. Duel décisif de validation M3 (H_A ⊥ H_B)**

Le budget est identique pour chaque bras : 100 USD Claude et 20 USD Gemini, sur 30 tâches bibliographiques et expérimentales pré-enregistrées.

- **Bras A** : LCDM adaptatif.
- **Bras B** : essaim fixe, avec topologie figée.
- **Bras C** : essaim i.i.d., avec échantillons indépendants et vote majoritaire.
- **Contrôle négatif N** : LCDM dont les signaux R_t sont permutés aléatoirement, au même budget.

Métriques :
- claims vérifiés par dollar ;
- C_W des erreurs ;
- taux d'hallucinations de citations ;
- drift.

Hypothèses testées :
- **H_A** : A > max(B, C) en claims vérifiés par dollar, avec IC bootstrap à 95 % ne contenant pas 0.
- **H_B** : A > N. Si A ≈ N, le gain provient de la diversité brute et non de la loi, et LCDM est réfutée.

Critère complémentaire : la réduction de C_W doit prédire la baisse d'erreurs corrélées. Une corrélation de Spearman ρ < −0,4 est exigée.
