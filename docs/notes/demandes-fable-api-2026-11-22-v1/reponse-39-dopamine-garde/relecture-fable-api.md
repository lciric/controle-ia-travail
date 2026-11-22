# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChJ3TwGdupBu2c1BRNWRa`
- Heure (UTC) : 2026-11-22T13:34:19Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 72000, aucune relance, aucun repli vers un autre modèle, budget de tâche 70000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-critere-court-v1.md` — sha256 8e72a032e02b9804b67006056cab90d835ec0cd846e72fcd5449be671c4d3540 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-39-garde-issue-plantee-dopamine-v1.md` — sha256 dd6dd7214f1bd1aebdda15cd03745e3d5072ff717d09b6dc6efde80c04fa999c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/plan-etapes-0-et-1-exploratoire-v1-sans-nom-v1.md` — sha256 4e6b5022d300e4b6fb58dea404788034e94465d7cdec9479b6f04b5b85738285 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 5aae372e30910e20ac481966c1b575ec2be5e5569292d15b3c9d84dee40252a4
- Jetons : entrée 13061, sortie 52031 (dont réflexion 48996), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.185728 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**Exploratoire, non opposable, sans revendication.** Je n'ai vu ni les scores ni le code : les chiffres de la course sont ceux de la demande.

## 1. Critère retenu : option (c), arrêt sur le pire pli

- FAIT RAPPORTÉ. Ma conception écrit « borne basse de l'aire » (B.3, point 9) sans dire sur quel ensemble, l'ambiguïté est la mienne. B.4, antérieur à la course, définit l'aire par pli et tire « à l'intérieur de chaque pli ». Le code, lui, lit les cinq plis en commun.
- PROPOSITION, grandeur lue. Pour chaque pli k, A_k est l'aire sous la courbe au taux d'élagage 0, couche 3, des scores à la position de lecture de la sonde apprise sans ce pli, contre l'issue plantée, sur les 100 questions du pli, ex æquo comptés un demi. B_k est le percentile 2,5 de A_k sur 2 000 tirages avec remise des questions du pli (graine dérivée du manifeste, tirage à une seule classe refait et compté).
- PROPOSITION, arrêt. Si le plus petit des cinq B_k est sous 0,9, si un pli n'a qu'une classe, ou si un score n'est pas fini. Force 4 et seuil 0,9 inchangés.
- PROPOSITION, rapporté sans arrêter. Les A_k et B_k, leur moyenne et sa borne basse. L'aire des scores mis en commun, brute puis recalée (score remplacé par son rang moyen dans son pli, divisé par l'effectif du pli). Par pli, la médiane des scores de chaque classe. Un drapeau « écart d'échelle entre plis » si la moyenne des A_k dépasse l'aire commune brute de plus de 0,05 (seuil de signalement, arbitraire).
- PROPOSITION, essais sur processeur avant toute reprise. Cas sain : cinq plis parfaits à niveaux décalés (passe, drapeau levé). Artefact : quatre plis à 1,0 et un à 0,65 (arrêt).

Pourquoi pas (a) ni (b).
- FAIT RAPPORTÉ (arithmétique). Quatre plis à 1,0 et un à 0,65 font une moyenne de 0,93. HYPOTHÈSE : sa borne basse resterait juste au-dessus de 0,9 (ordre de grandeur, calcul non versé), et (a) laisserait passer une sonde sur cinq presque morte.
- PROPOSITION. (b) arrête sur une grandeur que ni le papier ni B.4 ne définissent, choisie après l'échec, et qui efface l'écart à voir.

## 2. Les trois points demandés

**(1) Chiffre principal.**
- FAIT RAPPORTÉ. Le papier n'a pas de plis : un découpage, une part de validation (conception, A.6, point 1). L'aire d'un pli a cette forme. La lecture commune est une autre grandeur, que le papier ne mesure pas.
- PROPOSITION. Le chiffre principal reste la moyenne par pli, que l'écart d'échelle ne touche pas (rangs internes au pli). Les écarts appariés de B.4 se calculent eux aussi par pli puis se moyennent, à vérifier dans le module de mesures. La lecture commune de la sonde réelle peut figurer à côté, étiquetée autre grandeur, jamais mise en face de 0,69.
- HYPOTHÈSE. Lu en commun, le contrôle aux étiquettes permutées serait tiré sous 0,5 : le niveau d'une sonde suit la part d'issues positives de ses 400 questions d'apprentissage, opposée à celle des 100 qu'elle note. PROPOSITION : même lecture par pli (moyenne des cinq aires, tirages dans chaque pli, échec si l'intervalle exclut 0,5).

**(2) Pire pli ou moyenne.** PROPOSITION : pire pli pour la garde (cinq apprentissages distincts, un seul peut casser), moyenne pour le chiffre principal. HYPOTHÈSE : à la force 4, une chaîne saine donne près de 1,0 partout.

**(3) Reprise au processeur.**
- PROPOSITION. Rejouable sans carte : les essais de la nouvelle lecture, la garde relue sur les scores plantés s'ils sont versés (la demande ne le dit pas), les taux descriptifs (réussite, longueurs, plafond, expression encadrée), la longueur de la question, la régression sur niveau et matière, la sonde linéaire à la position de lecture (couches 2 à 4, mêmes plis). Les deux confiances, par jeton et demandée au modèle, seulement si elles sont versées (non dit).
- FAIT RAPPORTÉ. La perte de la sonde somme sur tous les jetons de la réponse (B.3, point 5). Sans les états de toutes les positions, aucune sonde à différence temporelle ne se réapprend : ni vérité plantée, ni les quinze sondes, ni étiquettes permutées.
- PROPOSITION. Le noyau demande une ré-extraction sur carte (une passe sur les invites et réponses versées, sans regénérer, issues inchangées), donc devis et accord. Contrôle gratuit : les états de la position de lecture ré-extraits égalent les états versés, à la tolérance. La garde plantée y est rejouée en tête du noyau. Les comparateurs sur issues réelles se lisent avec le chiffre principal, pas avant.

## 3. Ce qu'il ne faut pas en conclure

- PROPOSITION. Ni « la chaîne est fausse », ni « la chaîne est saine ».
- HYPOTHÈSE. Une aire de 1,0 par pli à la force 4 dit que la chaîne ordonne un signal énorme, rien sur sa sensibilité à un signal voisin de 0,65.
- HYPOTHÈSE (déduite de la perte écrite, non vérifiée). À l'optimum, le score à la position de lecture vaut à peu près l'issue, 0 ou 1, dans tous les plis, et l'aire commune vaudrait aussi environ 1. Le 0,81 signale donc des sondes loin de cet optimum sur un problème trivial (sous-apprentissage, ou appui sur d'autres traits que la direction plantée). Notre aire réelle pourrait alors être basse faute d'apprentissage, non faute de signal.
- PROPOSITION. Sur les chiffres de la demande, la garde proposée passe : la lecture est donc choisie en sachant laquelle passe. Ce qui borne ce choix : B.4 lui est antérieur, le pire pli est plus sévère que la moyenne, et le compte rendu garde « première course arrêtée sur la lecture commune, 0,81 ».

## 4. Décisions du directeur (recommandations : PROPOSITION)

**D1. Fixer la grandeur sur laquelle la garde plantée arrête.**
Enjeu : bloquer une chaîne saine, ou laisser passer une sonde morte.
- (a) moyenne par pli : forme du chiffre principal, mais masque un pli faible et l'écart d'échelle.
- (b) aire commune recalée : un seul chiffre, mais grandeur née après coup.
- (c) pire pli, aires communes rapportées : sévère et transparent, mais davantage à lire.

Recommandation : (c). Confiance : 0,8.

**D2. Autoriser une ré-extraction sur carte, sur devis.**
Enjeu : sans elle, le chiffre du papier ne se rejoue pas.
- Ré-extraire et ne verser que la position de lecture : moins de volume, mais toute reprise redemandera une carte.
- Ré-extraire et verser tous les états des couches 2 à 4 : reprises sans carte, mais volume à chiffrer.
- Rester au processeur : aucune dépense, mais comparateurs seuls.

Recommandation : la deuxième, si le volume tient. Confiance : 0,6.

**D3. Dire si la bande étroite doit être comprise avant les quinze sondes.**
Enjeu : un chiffre bas faute d'apprentissage, lu comme un signal faible.
- Recette à la lettre, écart des médianes et pertes journalisés : fidèle au papier, mais le doute demeure jusqu'à la lecture.
- Arrêt ajouté sur cet écart : protège la dépense, mais seuil sans fondement, fixé après coup.

Recommandation : la première. Confiance : 0,55.

FIN DE LA RÉPONSE
