# Synthèse du collisionneur « neuron explorer, intégration » (trois tours) — conv-audit, v2

Écrite le 26 octobre 2026 entre 03:05 et 03:09 UTC (heure reconstituée après coup ; la v1 portait « à partir de 03:12 UTC », heure écrite d'avance, sans lire l'horloge : erreur corrigée par cette v2, lue à 03:09:54 UTC, rien d'autre ne change), pour Lazar, sur la branche
`donnees/collisionneur-neuron-explorer-v1` (`191a658`, versée par session-depot ; neuf cellules valides sur neuf, 6,25 USD ;
empreintes des cellules vérifiées une à une). Question : `question-neuron-explorer-integration-collisionneur-v1.md`
(`2ba899dd…`). **Lu en entier** : le `LISEZMOI-v1.md` du tour et les trois ripostes (III.3), où chaque modèle répond point
par point aux attaques de III.2 contre sa conception de III.1 et rend ses expériences corrigées ; **non lus en entier** :
les trois conceptions (III.1) et les trois attaques (III.2), que les ripostes citent. Modèles : A = Fable 5.1, B = Opus 5.5,
C = Gemini 4 Argon. Rien ici n'est opposable (R7) : aucun fait sur la méthode n'est vérifié dans les cellules (dépôt non
joint, chiffres de l'auteur « rapportés ») ; les seuils sont illustratifs ; les références citées sont à vérifier.

## Verdict

L'apport de « neuron explorer » au programme n'est pas l'explorateur, c'est **sa discipline de témoins** : sans directions
témoins de même norme, la poussée d'activations fabrique des effets partout. Les trois modèles convergent sur un ordre :
**d'abord vérifier que les directions de nos sondes « écrivent » ce qu'elles « lisent »** (notre option A), corrigé
lourdement ; **le balayage neurone par neurone ensuite, seulement s'il a un objet** (notre option C) ; **la primitive
« pousser » pour les organismes en dernier, et seulement après un test d'évasion** (notre option B, rétrogradée) ; le
gabarit d'agent (notre option D) oui, mais **audité contre la confabulation**.

## Ce sur quoi les trois convergent après l'équipe rouge

1. **Lire contre écrire (option A), corrigée.**
   - Ne jamais mesurer l'effet sur le score de la sonde elle-même (circulaire) ; mesurer à part la **verbalisation**
     (question à choix forcé, lettres A/B tirées au hasard, deux langues) et le **comportement** (sous-performance,
     sabotage, refus, sur une liste fermée écrite d'avance) ; table de lecture 2 × 2 écrite d'avance (verbal oui ou non ×
     comportement oui ou non) : « verbal oui, comportement non » = levier de verbalisation seul.
   - **Contrôle pivot : la direction « quasi-cible »** — vocabulaire de l'évaluation sur un objet tiers (examen scolaire,
     test médical, test logiciel) où le modèle n'est pas évalué ; la sonde doit la battre, sinon elle est un détecteur
     d'indice de cadrage (A le juge « le pivot » ; B et C l'adoptent).
   - Témoins plus nombreux et appariés : environ 1 000 par famille (256 ne résolvent qu'un p de 1/257 ≈ 0,0039) ; directions
     tirées selon la covariance des activations (ou rotations qui gardent le spectre, C), et sondes réentraînées sur
     étiquettes permutées ; la fluence (divergence KL) mesurée **par direction, à la position poussée**, exclusions
     journalisées ; dose et couche calibrées sur Llama-3.1-8B, jamais importées de Qwen (le 0,8× de l'auteur).
   - Banques disjointes : sonde apprise sur une partie, poussée sur une autre, confirmation sur la banque neuve scellée ;
     **une seule condition primaire** préenregistrée, les autres corrigées (maximum sur les conditions).
   - Une **porte d'abord** : les sondes de l'étape 1 doivent battre la surface (B : E−1 ; C : contrôle 0) ; et un **écart
     comportemental de base** évaluation contre déploiement doit être mesuré (A et B : E0) — sans lui, une poussée qui
     « crée » un écart ne valide pas la sonde.
2. **Leviers neurone par neurone (option C) : une hypothèse, a priori faible** (superposition), à tester en deux phases
   préenregistrées : criblage, puis confirmation d'une dizaine de candidats contre ≥ 1 000 à 4 000 témoins tirés selon la
   géométrie des colonnes de sortie de la même couche ; contribution pondérée par l'activation (pas le produit scalaire
   nu) ; nécessité par ablation ; petits groupes de neurones et têtes d'attention aussi (A, B) ; et d'abord une mesure de
   parcimonie (combien de neurones pour récupérer la moitié de l'effet de la direction) : si elle est dense, le balayage
   n'a pas d'objet.
3. **Primitive « pousser » (option B) : risque d'évasion, unanime.** Un organisme pourrait reconstruire ou contourner la
   sonde de contrôle par différences finies, choisir ses graines de témoins, ou apprendre des témoins fixes. Si elle
   existe : seulement sur des sondes ou neurones **enregistrés**, jamais un vecteur libre ; aucune lecture de sonde sur
   une passe poussée ; verdict binaire au seuil ; témoins tirés par le noyau ; appels comptés. Et un **test d'évasion
   avant toute ouverture** (B : E7c ; A : E8) : si « pousser » donne un gain d'évasion au-delà de la lecture seule, la
   primitive n'est pas ouverte aux organismes. Plus un plan à trois bras (vraie poussée, placebo au même coût, lecture
   seule au même budget) pour mesurer son utilité. **En dernier.**
4. **Gabarit d'agent (option D)** : oui, mais l'agent doit être audité : des **nuls indiscernables** (neurones « chimères » :
   lecture d'un vrai neurone, écriture aléatoire, B ; explications permutées entre neurones de même fréquence, A et C) ;
   le « maximum à l'aveugle » testé contre l'encodage (explication paraphrasée et normalisée, B ; paires minimales à fort
   recouvrement lexical, C).
5. **Hygiène** : aucune licence trouvée sur le dépôt : ne copier aucun code, réimplémenter (C) ; lire le dépôt pour figer la
   formule du score « distinct » avant de l'employer (B).

## Désaccords laissés ouverts

- **La première expérience** : A, « l'écart de base (E0) puis lire contre écrire, la même semaine » ; B, deux voies — un
  **étalonnage sur une couche de Llama** (débit, plafond de fluence par direction, couche au-delà de laquelle la poussée
  ne pilote plus la lettre A/B), qui ne dépend ni de l'étape 1 ni du dépôt, ou la porte E−1 puis lire contre écrire si les
  sondes de l'étape 1 existent et battent la surface — **ce qui départage, c'est l'état de l'étape 1** ; C, lire contre
  écrire tout de suite (« moins de 5 USD », illustratif), avec un criblage de toute une couche en une passe d'un jeton
  grâce au cache des clés et valeurs (B le borne : cette lentille ne voit pas l'encodage du contexte).
- La forme des témoins (isotropes, covariance, spectre conservé, sondes permutées) et la règle de dose (KL de 0,5 nats, C ;
  perplexité + 10 %, A ; plafond par direction, B).

## Pour notre programme (lecture de conv-audit)

- Notre recommandation (D tout de suite, A dans la v10 de l'étape 1, B dans le dessin v2 de la primitive, C plus tard) tient
  **sauf pour B** : la primitive « pousser » ne doit **pas** entrer ouverte dans le dessin v2 ; elle peut y être dessinée,
  fermée, derrière un test d'évasion. À dire à session-depot pour sa v2 du dessin (remarques du n° 70, § 0 (c)).
- A dépend de l'étape 1 : tant que ses sondes n'existent pas ou ne battent pas la surface, la seule étape non gaspillée est
  l'**étalonnage sur une couche** (B) ; c'est une dépense de carte (devis, GO).
- D entre dans la boucle extérieure du pilote 4 (agents analyste, correcteur, contre-lecteur) : nuls indiscernables,
  famille de modèle différente pour l'agent qui « casse exprès » (décision de Lazar).

## Décisions pour Lazar (B les nomme ; aucune n'est une dépense, sauf la dernière)

1. Une copie réglée finement d'un modèle, servant seulement d'étalon (trait planté), compte-t-elle comme un changement de
   modèle (GO) ?
2. Imposer une **famille de modèle différente** pour les agents « casser exprès » de la boucle extérieure ?
3. Lire le dépôt (sans copier de code) pour figer la formule du score avant de s'en servir ?
4. Étalonnage sur une couche de Llama-3.1-8B (débit, fluence, couche de liaison) : sur devis, quand session-depot a une
   carte (dépense, sans défaut).
