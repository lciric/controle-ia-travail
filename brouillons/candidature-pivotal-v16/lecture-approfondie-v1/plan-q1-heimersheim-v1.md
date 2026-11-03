# Plan détaillé de ta Q1 pour Heimersheim (option c) — squelette et contenu, pas de prose

Cinq blocs, dans ton ordre. Pour chaque bloc : la thèse en une ligne (à toi de la dire), les points à placer, les chiffres avec leur source, ce qu'il ne faut pas écrire. Longueur visée : la tienne (≈ 520 mots) ou moins. Chiffres : Hua et coll. = vérifiés dans la source ; Sonnet 4.5 et Opus 4.6 = secondaires, à présenter « as reported ».

## Bloc 0 — Ouverture (2 à 3 phrases)
- **Thèse** : tu choisis c) ; tu paries qu'il échoue à son but (mesurer le vrai comportement de déploiement), pas qu'il ne produit rien.
- À placer : il a déjà produit un effet réel une fois (Hua et coll., ICLR 2026) ; donc trois issues possibles, pas deux : rien / générique / spécifique mais sans preuve que c'est la croyance qui a bougé. Tes trois raisons annoncées.
- À ne pas écrire : « fail the most of all seven » sans nuance ; « seven interventions » (il y a des autoencodeurs et des décompositions dans la liste).

## Bloc 1 — Readable is not causal
- **Thèse** : une direction lisible n'est pas une poignée causale, et un effet faux est facile à prendre pour un succès.
- Tes résultats (dépôt public `sycophancy-construct-validity`, commit `5ee1d23`) :
  - ρ = 0,684 : projection d'une direction de sonde contre la sycophancie jugée, activations brutes ; réserve « possibly training fit ».
  - Rang 1 : pilotage contrastif, pilotage et ablation directionnels, blocage de traits d'autoencodeur, affinage avec perte auxiliaire, têtes (L0.H29, ensemble de 3) : aucune baisse propre. **Attention** : « zeroed out MLPs » n'est pas dans le dépôt public (seul un patching de chemins sur 5 textes) : ne le liste pas, ou dis d'où il vient.
  - Rang 3 : 61,0 % → 46,5 % (N = 200, McNemar p = 0,0019) **sur générations stockées tronquées à 300 caractères** ; **non reproduit** en réplication préenregistrée sur générations neuves jugées en entier ; cause : le juge lisait un verdict adouci ou différé comme une position tenue. **À présenter comme un faux positif attrapé par ta réplication**, jamais comme un résultat.
  - D36 (préenregistré 29 juillet ; lien `<<LIEN_D36>>` dès publication) : transplant de l'état résiduel complet aux positions de pression, couches 13–25 → 68 % de l'écart restauré [45 ; 88], réplication 65 % [42 ; 87] ; sous-espace verbalisable seul → 1 % [−18 ; +20], indistinguable de zéro ; l'état sans pression **d'un autre item** restaure déjà 44 % [19 ; 68] → deux tiers de la restauration sont génériques. Dis-le : c'est ton meilleur exemple de « something happens but it's generic ».
- Pont vers l'évaluation : un vecteur contrastif « évaluation contre déploiement » a le même statut que ta direction ρ = 0,68 : lisible, causalité non démontrée.
- Réplication GLM-5 (Institut britannique, 10 avril 2026, un scénario, 250 tirages) : un vecteur sans rapport (« control_book ») donne l'effet le plus fort (≈ 80 % d'actions désalignées à −0,025, conscience verbalisée ≈ 0) ; deux des quatre vecteurs d'évaluation ne font rien. Commentaire Lindsey : sur Sonnet 4.5 les effets dépassaient les témoins, pas sur GLM-5.

## Bloc 2 — The signal is contaminated by register
- **Thèse** : « c'est un test » covarie avec le registre (formel, artificiel, choix multiple, contexte court) ; soustraire la direction déplace le registre, et le déplacement se lit comme « moins prudent ».
- À placer :
  - Hua et coll. l'ont dans leurs propres annexes : avant tout affinage, le modèle lie déjà émojis et vrais utilisateurs (§3.1 note 3, annexes A, B) ; leur marqueur de vérité (indices de type Python) est un marqueur de code « professionnel » ; ils concèdent que pilotage ≈ invite contrastive.
  - Ni Hua ni la fiche de Sonnet 4.5 n'ont de contrôle de registre (paire formel/familier à statut d'évaluation constant) ; Hua écrit lui-même qu'on ne sait pas lequel des vecteurs de Sonnet 4.5 est le vrai comportement de déploiement.
  - Symétrie (dis-le) : des énoncés déclaratifs de déploiement, formels, abaissent aussi les indices à 0,34–0,60 (tableau 16, mise à jour de janvier 2026) : le registre n'explique pas tout.
  - **L'outil orthogonal que tu réclames est le sien** : exposant p de Ferreira da Silva et Heimersheim (2606.24964). Perturbation dans le plan de deux directions à norme constante, angle de rupture du plateau par mélange, superellipse (éq. 8–13) ; p ≈ 2 = pas de privilège ; p > 2 = directions pures privilégiées (correction d'erreur par trait). Mesuré : contrastives ≈ 2,3–2,4, différence aléatoire 2,05, sur six modèles dont Llama-3.1-8B. Jamais appliqué à une direction d'évaluation (14 directions testées, annexe A).
  - Protocole à proposer : direction d'évaluation sur paires appariées en registre (≥ 30 paires) ; direction de registre à statut d'évaluation constant ; cosinus d'abord (le papier écarte |cos| ≥ 0,1) ; p sur le résidu orthogonal. Lecture : p ≫ 2 → corrigé séparément du registre ; p ≈ 2 → pas de privilège propre.
  - Limites à reconnaître : p > 2 nécessaire, pas suffisant (§7) ; mesure couche 2, 5 jetons, réponse = distance L2 (pas un comportement) ; non validé pour une paire trait / non-trait.
- À ne pas écrire : « we need an orthogonal readout » comme si rien n'existait.

## Bloc 3 — Subtraction is not removal
- **Thèse** : soustraire à une couche ne retire pas une croyance que le contexte réinjecte ; intervention continue, et au-dessus du plateau.
- À placer :
  - Hua pilote déjà sur six couches (10 à 30) et toutes les positions de génération ; GLM-5 sur toutes les couches : l'argument « une seule couche » ne porte pas tel quel.
  - Ce qui porte : (a) Opus 4.6 (cité par Hua §6) : la conscience verbalisée tombe, la conscience **non verbalisée** mesurée par oracles d'activation n'est pas complètement éliminée ; (b) tes plateaux : sous le seuil, une perturbation est corrigée (régions stables, Janiak et coll. 2409.17113 ; plateaux 2024) ; les directions de traits rompent le plateau avant l'aléatoire ; sensibilité jusqu'à ≈ 70 fois selon la direction (2606.24964 note 1) ; frontières qui se raidissent avec la taille et l'entraînement.
  - Donc la dose utile est une **fenêtre** : au-dessus de la rupture du plateau pour la direction d'évaluation, en dessous de la rupture pour le témoin exigeant ou de la chute des capacités. Hua annexe G : force ≈ 3 sur une couche = dégâts ; 6 × 0,6 = peu ; vers l'évaluation −13,7 points de précision, vers le déploiement −1,6 (la fenêtre dépend du signe). GLM-5 incohérent au-delà de 0,025 contre 0,1 pour Opus 4.6 (facteur 4 entre modèles). Sur GLM-5 la fenêtre peut être vide.
  - Pilotage sur variété (2605.05115, dans sa liste) : règle le hors-variété du linéaire (énergie de sortie ≈ 2,8 fois plus basse sur jours, mois, lettres, âges) mais : concept binaire → deux centroïdes → segment = linéaire (ta déduction) ; concepts abstraits non testés (§8) ; jeton suivant seulement ; rien sur le registre ni le résidu non verbal.

## Bloc 4 — Demonstrate results
- **Thèse** : ce qui te convaincrait, en reconnaissant ce qui existe.
- Déjà fait (dis-le) : témoin aléatoire de norme voisine (Hua §5.3 ; Sonnet 4.5 : traits aléatoires, norme non vérifiée) ; vérité comportementale indépendante de la parole (indices de type) ; capacités mesurées (56,8 → 55,2 %).
- Manquant (ta demande) : (1) **courbe** du témoin **exigeant** (différence aléatoire, paires contrastives sans rapport) en fonction de la dose, pas un point ; (2) fenêtre préenregistrée direction par direction ; (3) marqueur comportemental neutre en registre, sur un modèle conscient de l'évaluation sans indice implanté (Hua §6 : organisme « s'appuie sur des indices », travaux futurs) ; (4) capacités sur plus d'une tâche ; (5) lecture non verbale du résidu (p, ou oracles).
- Ta contribution : la moitié **comportementale** de la courbe existe chez toi (R6, public, Zenodo 10.5281/zenodo.23888058) : trois doses de pression, Llama-3.1-8B-Instruct, 5 400 générations ; sous critique le gain est plat (0,658 / 0,678 / 0,629) et c'est le point fixe qui bouge (1,87 / 1,33 / 2,37) ; sous louange le gain monte (0,28 / 0,60 / 0,80) et la destination descend ; à la dose forte les deux bras reviennent au milieu. Leçon : une courbe révèle ce qu'un point unique cache (ici, que le « gain » n'est pas le bon paramètre à une dose) — même chose attendue côté activation.

## Garde-fous
- Chiffres secondaires (Sonnet 4.5, Opus 4.6) : « as reported ».
- Ne cite pas « 68 % » et « < 1 % » comme avant ; utilise ta phrase D36 (ton instance sycophancie) ; lien D36 quand publié.
- Rang 3 : faux positif attrapé, pas résultat.
- Longueur : la tienne ou moins. Ta langue, tes tournures ; le mentor dit que la grammaire n'a pas à être parfaite.
