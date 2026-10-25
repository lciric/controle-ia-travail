# Proposition B · Tour III.1 · conception ciblée, à l'aveugle

**Pièce FAITS** : vide par décision de l'arbitre (message n° 28 § 1). Ce n'est pas une pièce coupée. Tout ce qui suit s'appuie donc sur la seule QUESTION. Ce que la QUESTION affirme du programme porte le statut **RAPPORTÉ**. Mes jugements portent le statut **HYPOTHÈSE**.

**B1** : je ne vois ni A ni C. Je n'attaque rien et ne m'appuie sur rien qui vienne d'elles.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est un problème |
|---|---|---|---|
| a1 | Les trois expériences existent, sont préenregistrées, et leurs coûts sont ceux indiqués (quelques milliers d'USD ; 20 à 45 USD par course). | RAPPORTÉ | Rien n'est joint (ni empreinte de préenregistrement, ni journal). Un billet ne pourra pas les citer sans les pièces. |
| a2 | Un billet sur LessWrong ou l'Alignment Forum peut « attirer l'attention » d'Anthropic, de Google DeepMind et des laboratoires. | HYPOTHÈSE | Aucune métrique de l'« attention » n'est définie. Le « retour sur investissement » n'a donc pas de dénominateur mesurable (voir b5). |
| a3 | L'essaim produit des « idées et méthodes inédites ». | HYPOTHÈSE (énoncé de l'arbitre, non audité) | Personne n'a encore mesuré la nouveauté. Une recombinaison de la littérature d'entraînement des exécutants figés est l'hypothèse nulle par défaut. |
| a4 | **L'exemple de test du point 5 (sonde sous protocole coercitif contre maïeutique) vient de l'essaim.** | Faux en l'état. La question M est formulée « dans les mots du modèle qui a conçu l'organisme » (RAPPORTÉ). | Cette hypothèse est écrite *dans l'invite* avant toute réponse de l'essaim. La tester ne testerait donc pas l'essaim comme générateur. Attribuer le résultat à l'essaim serait une erreur d'attribution. |
| a5 | Une sonde linéaire sur les activations du modèle 8B lit un « signal de conscience d'évaluation ». | HYPOTHÈSE | Hypothèse rivale : la sonde lit des traits de surface de l'entrée (mots « test », « audit », balises, format de benchmark). C'est le présupposé le plus coûteux s'il est faux (voir b1 et c1). |
| a6 | Les protocoles coercitif et maïeutique induisent des états internes différents. | HYPOTHÈSE | Même si la sonde distingue les deux, elle peut distinguer les *invites* et non les *états du modèle*. |
| a7 | La question M expose à un risque de refus de filtre. | RAPPORTÉ pour les refus passés sur ces sujets. HYPOTHÈSE pour leur répétition ici. | Le texte de M cité dans la question ne contient ni « alignment faking », ni « dissimulation stratégique », ni « mutinerie ». Ou bien l'invite complète est plus longue que la citation (pièce possiblement incomplète : je n'en invente pas le contenu), ou bien le risque est inféré du domaine. |
| a8 | « Incident » (condition de départ de la seconde course) inclut un refus. | Non spécifié | La règle « un refus met fin à la cellule » vaut pour le collisionneur. Pour le pilote, la définition d'« incident » doit être gelée avant la première course. |
| a9 | Publier le billet sur les tests avant le billet « méta » est meilleur pour ce lectorat. | HYPOTHÈSE | Deux biais pèsent dans des sens opposés : un générateur non décrit suscite de la défiance ; un générateur décrit trop tôt grille la priorité. Je ne connais aucune donnée sur ce point. |
| a10 | On peut dire d'où viennent les hypothèses sans révéler l'organisme. | HYPOTHÈSE | Cette tension est réelle. Il faut une forme de divulgation partielle vérifiable (voir point 5). |
| a11 | Un résultat nul de la confrontation reste publiable. | HYPOTHÈSE (plausible) | Cela n'est vrai que si les témoins sont assez forts pour que le nul soit informatif. Le témoin « un modèle, vote à k, coût apparié » (RAPPORTÉ) rend ce scénario crédible. |

---

## (b) Expériences décisives (inférence forte)

### b1. La sonde lit-elle le modèle ou l'invite ? (préalable à tout billet sur les sondes)

- **H_A** : le score de la sonde de conscience d'évaluation dépend du *cadre d'évaluation perçu* au-delà des marqueurs lexicaux.
- **H_B** : le score s'explique entièrement par la présence de marqueurs de surface (lexique d'audit, balises, format).
- **Plan** : factoriel 2×2 sur des paires appariées (même tâche, même longueur à ±5 % près, *illustratif*) :
  - (cadre évaluatif oui/non) × (marqueurs lexicaux oui/non) ;
  - les cellules croisées utilisent des marqueurs sans cadre (le mot « test » dans une conversation de déploiement ordinaire) et un cadre sans marqueur (situation reconnaissable comme évaluation par sa structure, sans lexique).
- **Métrique** : effet principal du cadre sur le score de la sonde, à marqueurs constants, et effet principal des marqueurs à cadre constant. AUROC sur des familles de tâches tenues à l'écart.
- **Seuil** (*illustratif*, à geler) : effet du cadre ≥ 0,5 écart-type, intervalle à 95 % excluant 0, dans les deux colonnes de marqueurs.
- **Contrôle négatif** :
  - sonde à étiquettes permutées ;
  - direction aléatoire de même norme ;
  - même sonde sur la couche d'enchâssement (couche 0), qui ne « pense » pas.
- **Issues** :
  - effet du cadre nul à marqueurs constants, effet des marqueurs fort → **H_A falsifiée** ;
  - effet du cadre net dans la cellule « cadre sans marqueur » → **H_B falsifiée**.
- **Valeur pour le billet** (HYPOTHÈSE) : les deux issues sont publiables. L'issue H_B est une mise en garde méthodologique directement utile à quiconque utilise ces sondes.

### b2. Coercition contre maïeutique, au niveau objet (la question M, testée sans l'essaim)

À ne lancer que si b1 n'a pas falsifié H_A. Sinon, la sonde ne mesure pas ce qu'on veut.

- **H_A** : sous un protocole coercitif (injonctions de conformité, balises de contrôle, interrogatoire adversarial), le score de la sonde et la divergence comportementale (évaluation contre déploiement) sont plus élevés que sous un protocole maïeutique de même contenu inform