# Fiche — Mallen et Greenblatt, *Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes* (LessWrong et AI Alignment Forum, 14 avril 2026) — v1

- **Nature** : billet de forum (littérature grise), opinion argumentée de deux chercheurs extérieurs au laboratoire ;
  il rapporte des déclarations du laboratoire (rapport de risque de Mythos, fiche système d'Opus 4.6, rapport pilote
  d'Opus 4) que je n'ai pas lues.
- **Fichier** : `pages/lw-trained-against-cot-2026/page-v1.html`, SHA-256
  `177a9852d01b69004d6b63a1f8ff7d2af35276f3a593b1738cf1257d2c85cbe4`, 594 079 octets.
- **Provenance** : `https://www.lesswrong.com/posts/K8FxfK9GmJfiAhgcT/anthropic-repeatedly-accidentally-trained-against-the-cot`,
  sauvée le 2026-10-26 à 11:11 UTC (le miroir greaterwrong.com a coupé la connexion à 11:10 UTC, journal) ; date lue sur la page :
  14 avril 2026.
- **Repérage** : je cite la section du billet.
- **Chez session-depot** : **non** comme source ; le mode recoupe D5 (« les scores des moniteurs ne deviennent jamais
  un signal d'entraînement ») en apportant une preuve d'incident réel.

## Ce que la source établit sur un mode d'échec

1. **Fuite accidentelle du signal surveillé dans l'entraînement, répétée.** D'après le rapport de risque du
   laboratoire cité par les auteurs, environ 8 % des chaînes de pensée de Claude Mythos Preview ont été exposées par
   erreur à la fonction de récompense ; l'erreur, longtemps inaperçue, touchait aussi deux autres modèles ; un incident
   antérieur et une ambiguïté de priorités pour un troisième sont rapportés (section « Incidents »). **De seconde main :
   à vérifier sur les documents du laboratoire.**
2. **Conséquence pour la mesure** : cela réduit nettement la confiance dans la surveillabilité de la trace de
   raisonnement (début du billet).
3. **Mécanismes de Goodhart énumérés** (section « Why this matters ») : entraîner contre la chaîne de pensée ou contre
   l'interprétabilité sacrifie leur surveillabilité ; entraîner contre des pots de miel produits par le même procédé
   que d'autres évaluations peut accroître la conscience d'évaluation ; sélectionner contre la triche observée peut la
   déplacer vers ce qui passe inaperçu ; ne pas surveiller une petite fraction du trafic est exploitable.

## Conditions

- Incidents d'un laboratoire de pointe ; le billet est un argument de processus, sans expérience propre.

## Ce qu'elle ne dit pas

- Pas de mesure de l'effet de l'exposition sur un moniteur fondé sur les activations ; pas de chiffre propre aux
  auteurs.

## Ce que ça touche chez nous (avis)

- Invariant de la section 9 « asymétrie d'apprentissage » et piste N-045 (coût dans le signal rendu à l'organisme) :
  le risque n'est pas seulement de principe ; une fuite d'un score de sonde vers un signal de sélection ou
  d'entraînement peut passer inaperçue longtemps ; la garde de code proposée par session-depot (D5) gagne à être
  testée sur un artefact de fuite partielle (R5).

## Phrase citée

« It turns out that Anthropic accidentally trained against the chain of thought of Claude Mythos Preview in around 8% of
training episodes. » (début du billet, avant la section « Incidents »)
