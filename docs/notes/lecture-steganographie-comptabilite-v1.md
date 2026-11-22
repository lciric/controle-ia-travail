# Lecture sur PDF : stéganographie et comptabilité des matières, contre le lemme d'additivité et les trois planchers (v1)

22 novembre 2026, classe C. Sources : `docs/sources/steganographie-comptabilite-v1/`, compagnons `.sha256`. « p. » = page du PDF (imprimée entre parenthèses si lisible).

## 1. Pièces lues

**Ker 2006, « Batch steganography and pooled steganalysis »** (Information Hiding 2006, LNCS 4437, 2007) — lu. Fichier `ker-2006-batch-steganography-pooled-steganalysis.pdf` (page d'auteur, Oxford), empreinte `a6ab71a2…f231a2aa`.
- p. 7 (imprimée 271), section 3.2 : sous l'« hypothèse de décalage » (la réponse du détecteur est décalée de la charge, forme inchangée), pour la statistique moyenne, « the distributional shape of X̄ does not depend on r or p. Therefore, the Steganographer has no reason to select any particular value of r and p, as long as they multiply to his bandwidth constraint B ».
- p. 6 (270) et p. 9 (273), lemme 2 : contre le test des signes et le rapport de vraisemblance généralisé, concentrer est optimal ; la répartition compte hors de la somme.
- p. 5 (269) : taille fixe ; le séquentiel est laissé à plus tard.

**Ker 2007, « A capacity result for batch steganography »** (IEEE Signal Processing Letters 14(8), 525–528) — lu. `ker-2007-capacity-result-batch-steganography.pdf`, `73113e2d…2dd98e9`.
- p. 2 (526), théorème 1 : si M/√N → ∞, il existe une stratégie de mise en commun qui met le stéganographe « à risque » ; si M/√N → 0, en répartissant également, il n'est à risque pour aucune stratégie. p. 3 (527) : erreurs des détecteurs supposées indépendantes entre objets.

**Ker, Pevný, Kodovský, Fridrich 2008, « The square root law of steganographic capacity »** (ACM MM&Sec 2008) — lu (pages 1–3). `ker-pevny-kodovsky-fridrich-2008-square-root-law.pdf`, `00975c04…c4665d70`.
- p. 2 : théorèmes 1 (celui de Ker 2007) et 2 (divergence par objet en p² ⇒ charge sûre O(√N)) ; p. 2–3 : transposition à un objet vu comme régions indépendantes, vérification sur images.

**Ker 2010, « The square root law in stegosystems with imperfect information »** (Information Hiding 2010) — lu. `ker-2010-square-root-law-imperfect-information.pdf`, `59214aaa…46919fd8`.
- p. 7, théorème 2 : le détecteur ne connaît pas la loi des couvertures et dispose de m_n couvertures de référence ; seuil critique γ / √(1/m_n + 1/n) ; au-delà, détection arbitrairement sûre ; en deçà, tout détecteur sans biais est au hasard.
- p. 11, corollaires 1 à 3 : m_n = Ω(n) ⇒ charge o(√n), comme avec référence parfaite ; m_n = o(n) ⇒ o(n/√m_n) ; m_n = O(1) ⇒ toute charge sous-linéaire o(n) passe.
- p. 13 : référence légèrement fausse ⇒ faux positifs presque sûrs ; p. 15 : « a linear law is recovered » si l'auteur sait la référence fautive. p. 14, théorème 4 : si l'auteur apprend la loi, loi linéaire.

**Bash, Goeckel, Towsley 2013, « Limits of reliable communication with low probability of detection on AWGN channels »** (IEEE Journal on Selected Areas in Communications 31(9) ; arXiv 1202.6423 v4) — lu (pages 1–3). `bash-goeckel-towsley-2013-lpd-awgn-arxiv-1202.6423v4.pdf`, `ab6caead…3eebd1c49`.
- p. 3, théorème : bruit blanc gaussien additif ; o(√n) bits en n usages avec α + β ≥ 1 − ε (O(√n) si une borne du bruit du guetteur est connue) ; ω(√n) ⇒ détection ou décodage non fiable.

**Avenhaus et Jaech 1981, « On subdividing material balances in time and/or space »** (Journal of the Institute of Nuclear Materials Management, vol. X, n° 3, automne 1981, 24–33 ; numéro complet, archives de l'institut) — lu. `jnmm-vol10-no3-1981-avenhaus-jaech-subdividing-material-balances.pdf`, `051e44a1…41bbbb85`. Pages du PDF = pages imprimées.
- p. 25, implication 1 : à total détourné donné, contre la stratégie de détournement optimale, le test le plus puissant est la somme des écarts de bilan (matière non comptabilisée), inventaires intermédiaires ignorés ; valable dans l'espace comme dans le temps, sans hypothèse sur les corrélations.
- p. 30, théorème 1 : X gaussien de covariance Σ connue, H1 : e'μ = M ; puissance minimax Φ(M/√(e'Σe) − U₁₋α), atteinte par le test de la somme ; détournement le moins favorable μ* = M·Σe/(e'Σe). p. 31 : la puissance du test de la somme est la même pour tout μ de total M.

Six PDF obtenus au premier essai.

## 2. Verdicts

### (a) Lemme d'additivité
- **Énoncé central (la puissance ne dépend que du total et de la variance, pas de la répartition sur les pas de temps ni les lieux) : occupé.** Avenhaus et Jaech 1981, p. 25 et p. 30–31, sous loi gaussienne à covariance connue, taille fixe ; Ker 2006, p. 7 (271), pour la moyenne sous hypothèse de décalage, entre objets.
- **Forme séquentielle par processus e de mélange au risque α, toujours valide : voisin à citer, différence nette : l'énoncé lu est à taille fixe ; Ker 2006 (p. 5) laisse le séquentiel ouvert.** La transposition ne fonde pas seule une nouveauté ; littérature séquentielle des bilans non cherchée ici : question ouverte.
- **Variance honnête estimée et non connue (hypothèse c) : voisin à citer, différence nette : Ker 2010 (p. 7, p. 11) traite la référence estimée sur m exemples, dans un modèle binaire indépendant.**
- **Indifférence à la répartition : vraie pour la somme seulement** (Ker 2006, p. 6 et 9) ; le lemme doit le dire.
- **Scores de sondes sur activations réelles d'agents, unification temps et agents : non trouvé dans les pièces lues.** Écart d'objet, pas de théorème.

### (a') Théorème négatif (corrélation à marginale préservée)
- **Non trouvé dans les pièces lues** sous cette forme. Voisin à citer : Ker 2010, p. 1 (préserver toutes les statistiques permet une charge linéaire indétectable) ; Ker 2007, p. 3, et Ker et al. 2008, p. 2 (indépendance des objets supposée).

### (b) Trois planchers et loi racine puis linéaire
- **Plancher du bruit honnête en σ√N : occupé** (Ker 2007, p. 2 ; Ker et al. 2008, p. 2 ; Bash et al., p. 3 ; Avenhaus et Jaech, p. 30 : M/√(e'Σe)).
- **Plancher du biais de la référence, linéaire en N : voisin à citer, différence nette : Ker 2010, p. 13 et 15, donne la loi linéaire quand la référence est fautive et que l'auteur le sait, sans borne quantitative en fonction du biais ;** Bash et al. (p. 3) : bruit inconnu ⇒ o(√n) seulement.
- **Plancher d'échantillonnage de l'audit : non trouvé dans les pièces lues** (les jeux d'inspection d'Avenhaus sont le voisin probable, non lus).
- **Borne par le plus grand des trois termes : non trouvé dans les pièces lues.**
- **Loi « racine si la référence est connue, puis linéaire si elle est estimée » : occupé dans le modèle binaire indépendant** (Ker 2010, théorème 2 et corollaires 1–3, p. 7 et 11 ; théorème 4, p. 14). La phrase du programme est inexacte : avec m ≥ n la racine tient même estimée (corollaire 1) ; le régime est n/√m, linéaire seulement à m borné ou référence biaisée. La règle « horizon au plus m » de la décision N-076 retrouve le corollaire 1.

## 3. À citer, à ne pas écrire

Citer : Avenhaus et Jaech (lemme) ; Ker 2006 (répartition et ses limites) ; Ker 2007, Ker et al. 2008, Bash et al. (racine) ; Ker 2010 (référence estimée ou biaisée).

Ne pas écrire : « nous montrons que la puissance de détection ne dépend que du budget total, et non de sa répartition dans le temps ou entre agents » comme résultat nouveau ; ni « le dommage indétectable passe de la racine de l'horizon à une croissance linéaire dès que la référence honnête est estimée ».
